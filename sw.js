// Service worker de Colle express : l'application s'ouvre instantanément, même sur un réseau lent.
// - Coquille (HTML, CSS, JS, polices) : servie depuis le cache ; elle change quand VERSION change.
//   => À CHAQUE MISE EN LIGNE, incrémenter VERSION (sinon les visiteurs gardent l'ancienne version).
// - Données (exercices, corrigés par exercice, schémas) : cache d'abord, mise à jour en arrière-plan.
//   Un corrigé ouvert une fois reste consultable hors connexion.
// Les données personnelles (Supabase) ne sont jamais mises en cache.
const VERSION = 'ce-v42';
const SHELL = ['./', './index.html', './correction.html', './manifest.webmanifest',
  './css/style.css', './js/app.js', './js/api.js', './js/config.js', './js/format.js', './js/icons.js',
  './js/figures.js', './js/figkit.js', './js/figures-corr.js', './js/figures-annale.js', './js/figures-annale-index.js', './fonts/latin-modern-roman-regular.woff2', './fonts/latin-modern-roman-italic.woff2', './js/auth.js', './js/validation.js', './js/ui.js', './js/profil.js', './js/carnet.js', './js/biblio.js', './js/communaute.js', './js/modes.js', './js/vivant.js', './js/mouvement.js', './js/tactile.js', './js/vitrine.js', './js/xp.js', './js/defis.js', './fonts/inter-latin-wght-normal.woff2', './fonts/inter-latin-ext-wght-normal.woff2', './fonts/inter-latin-wght-italic.woff2', './fonts/jetbrains-mono-latin-wght-normal.woff2', './fonts/caveat-latin-wght-normal.woff2', './js/apropos.js', './js/fiches.js', './js/fiches-kit.js', './js/fiches-fig-p1.js', './js/fiches-fig-p2.js', './js/fiches-fig-p4.js','./js/fiches-fig-p5.js','./js/fiches-fig-mpa.js','./js/fiches-fig-mpb.js','./js/fiches-fig-mpc.js','./js/fiches-fig-c.js', './js/correction.js', './js/mathjax-config.js',
  './data/exercices.json', './icons/icon-v2-192.png', './icons/icon-v2-512.png', './img/logo.webp', './img/logo-dark.webp', './img/logo.png', './icons/favicon-v2-64.png'];

// Une réponse arrivée après une redirection (Cloudflare redirige index.html vers /) ne peut pas
// servir à ouvrir une page : le navigateur la refuse. On la recopie donc sans la marque de redirection.
const clean = res => !res.redirected ? res : res.blob().then(b => new Response(b, {status: res.status, statusText: res.statusText, headers: res.headers}));
self.addEventListener('install', e => {
  e.waitUntil(caches.open(VERSION).then(c => Promise.all(SHELL.map(p =>
      fetch(p, {cache: 'reload'}).then(r => { if (!r.ok) throw new Error(p + ' : ' + r.status); return clean(r); }).then(r => c.put(p, r))))
    .then(() => c.add('https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/+esm').catch(() => {})))
    .then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
const SHELL_URLS = new Set(SHELL.map(p => new URL(p, self.registration.scope).href));
const put = (req, res) => { if (res.ok) { const c = res.clone(); Promise.resolve(clean(c)).then(r => caches.open(VERSION).then(x => x.put(req, r))); } return res; };
self.addEventListener('fetch', e => {
  const req = e.request, url = new URL(req.url);
  if (req.method !== 'GET') return;
  if (/supabase\.co$/.test(url.hostname) || url.hostname.includes('formsubmit')) return;   // jamais en cache
  if (url.origin === location.origin) {
    const scope = new URL(self.registration.scope).pathname, rest = url.pathname.slice(scope.length);
    if (req.mode === 'navigate' && !['', 'index.html', 'correction.html', 'index', 'correction'].includes(rest)) {
      // Autre page ou fichier ouvert directement (PDF…) : toujours le réseau.
      e.respondWith(fetch(req).catch(() => caches.match('./index.html').then(r => r && clean(r))));
      return;
    }
    if (req.mode === 'navigate') {
      // Pages de l'application : la version en cache s'affiche tout de suite ; le réseau sert si elle manque.
      const page = /^correction(\.html)?$/.test(rest) ? './correction.html' : './index.html';
      e.respondWith(caches.match(page).then(r => r ? clean(r) : fetch(req).then(res => put(req, res))).catch(() => caches.match('./index.html').then(r => r && clean(r))));
      return;
    }
    const href = url.origin + url.pathname;
    if (SHELL_URLS.has(href) && !url.pathname.includes('/data/')) {
      // Coquille : cache d'abord (elle est renouvelée en bloc à chaque nouvelle VERSION).
      e.respondWith(caches.match(req, {ignoreSearch: true}).then(r => r || fetch(req).then(res => put(req, res))));
      return;
    }
    // Données et schémas : réponse immédiate depuis le cache, rafraîchie en arrière-plan.
    e.respondWith(caches.open(VERSION).then(c => c.match(req).then(hit => {
      const net = fetch(req).then(res => { if (res.ok) c.put(req, res.clone()); return res; });
      if (hit) { e.waitUntil(net.catch(() => {})); return hit; }
      return net;
    })));
  } else if (/cdn\.jsdelivr\.net|fonts\.(googleapis|gstatic)\.com/.test(url.hostname)) {
    // Bibliothèques versionnées (MathJax, polices, supabase-js) : cache d'abord.
    e.respondWith(caches.match(req).then(r => r || fetch(req).then(res => { if (res.ok || res.type === 'opaque') { const c = res.clone(); caches.open(VERSION).then(x => x.put(req, c)); } return res; })));
  }
});
