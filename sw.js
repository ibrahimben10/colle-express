// Service worker de Colle express : l'application s'ouvre instantanément et les
// énoncés, indices et corrigés restent consultables hors connexion.
// Les données personnelles (Supabase) ne sont jamais mises en cache.
const VERSION = 'ce-v14';
const SHELL = ['./', './index.html', './correction.html', './manifest.webmanifest',
  './css/style.css', './js/app.js', './js/api.js', './js/config.js', './js/format.js', './js/icons.js',
  './js/figures.js', './js/auth.js', './js/validation.js', './js/ui.js', './js/profil.js', './js/carnet.js', './js/biblio.js', './js/communaute.js', './js/modes.js', './fonts/source-sans-3-latin-wght-normal.woff2', './fonts/source-sans-3-latin-ext-wght-normal.woff2', './fonts/source-sans-3-latin-wght-italic.woff2', './fonts/fraunces-latin-wght-normal.woff2', './fonts/fraunces-latin-wght-italic.woff2', './fonts/jetbrains-mono-latin-wght-normal.woff2', './fonts/caveat-latin-wght-normal.woff2', './js/apropos.js', './js/correction.js', './js/mathjax-config.js',
  './data/exercices.json', './data/corriges.json', './icons/icon-192.png', './icons/icon-512.png', './img/embleme.png', './img/logo.webp'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(SHELL)
    .then(() => c.add('https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/+esm').catch(() => {})))
    .then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const req = e.request, url = new URL(req.url);
  if (req.method !== 'GET') return;
  if (/supabase\.co$/.test(url.hostname) || url.hostname.includes('formsubmit')) return;   // jamais en cache
  if (url.origin === location.origin) {
    // Site : réseau d'abord (mises à jour immédiates), cache si hors connexion.
    e.respondWith(fetch(req).then(r => { if (r.ok) { const c = r.clone(); caches.open(VERSION).then(x => x.put(req, c)); } return r; })
      .catch(() => caches.match(req, {ignoreSearch: req.mode === 'navigate'}).then(r => r || caches.match('./index.html'))));
  } else if (/cdn\.jsdelivr\.net|fonts\.(googleapis|gstatic)\.com/.test(url.hostname)) {
    // Bibliothèques versionnées (MathJax, polices, supabase-js) : cache d'abord.
    e.respondWith(caches.match(req).then(r => r || fetch(req).then(res => { if (res.ok || res.type === 'opaque') { const c = res.clone(); caches.open(VERSION).then(x => x.put(req, c)); } return res; })));
  }
});
