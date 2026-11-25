// Colle express — interface
import { CONFIG } from './config.js';
import { api, on, DEMO } from './api.js';
import { ic, chapIcon } from './icons.js';
import { FIG } from './figures.js';
import { legHTML } from './figures-annale.js';
import { esc, rich, fmtEnonce, fmtCorrige, hintsHTML, hintLevels, correctionHTML } from './format.js';
import { presentationCourte, presentationPage } from './apropos.js';
import { initAuth, showAuth, MSG } from './auth.js';
import { initTheme, syncTheme, reveal, toast, THEME_ICON } from './ui.js';
import { initProfil, renderProfil, renderEdition, profilURL, stats as statsProfil } from './profil.js';
import { initCarnet, renderCarnet, openNote } from './carnet.js';
import { initBiblio, renderCollection, openCollectionsPicker } from './biblio.js';
import { renderCorrection } from './modes.js';
import { rotator, countUp, heroBackground, carousel, celebrate } from './vivant.js';
import { initMouvement } from './mouvement.js';
import { initTactile } from './tactile.js';
import { initVitrine, extrait } from './vitrine.js';
import { niveauHTML } from './xp.js';
import { defis, defisHTML, nouveaux } from './defis.js';
import { initCommunaute, renderCommunaute, renderSolutions, openSignalement, renderModeration } from './communaute.js';

const $ = s => document.querySelector(s);
const SKEL = (n, cls = 'skel-item') => Array.from({length: n}, () => cls === 'skel-item' ? '<div class="skel-item" aria-hidden="true"><span class="skel"></span><span class="skel skel-l w80"></span><span class="skel skel-l w40"></span></div>' : `<span class="skel ${cls}" aria-hidden="true"></span>`).join('');
const LV = {1: 'CCINP', 2: 'Mines-Centrale', 3: 'X-ENS'};
const LVD = {1: 'Fondamentaux et applications directes du cours', 2: 'Oraux Mines-Ponts et Centrale-Supélec', 3: 'Oraux X-ENS : exercices ouverts'};
const MAT_IC = {Maths: 'sigma', Physique: 'atom', Chimie: 'flask', Informatique: 'code'};
const now = () => Date.now();
const mmss = s => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;
const fmtDate = t => t ? new Date(t).toLocaleString('fr-FR', {day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit'}) : '—';
const ago = t => { if (!t) return '—'; const s = Math.round((now() - new Date(t)) / 1000); if (s < 60) return 'à l’instant'; if (s < 3600) return `il y a ${Math.round(s / 60)} min`; if (s < 86400) return `il y a ${Math.round(s / 3600)} h`; return `il y a ${Math.round(s / 86400)} j`; };
const initials = n => (n || '?').split(/\s+/).filter(Boolean).slice(0, 2).map(w => w[0].toUpperCase()).join('');
const hue = s => { let h = 0; for (const c of String(s)) h = (h * 31 + c.charCodeAt(0)) % 360; return `hsl(${h} 55% 42%)`; };
const CARTES = {};   // auteurs hors de mes groupes (commentaires publics) : nom, identifiant, photo
const photoOf = id => (api.user && id === api.user.id ? SUIVI?.photo : (CLASS || []).find(c => c.id === id)?.data?.photo || CARTES[id]?.photo) || '';
const avatar = (id, name) => { const ph = photoOf(id);
  return /^data:image\/(jpeg|png|webp);base64,[A-Za-z0-9+/=]+$/.test(ph) ? `<img class="avatar" src="${ph}" alt="">` : `<span class="avatar" style="background:${hue(id)}">${esc(initials(name))}</span>`; };
const store = { get(k, d) { try { const v = localStorage.getItem('ce:' + k); return v ? JSON.parse(v) : d; } catch { return d; } }, set(k, v) { try { localStorage.setItem('ce:' + k, JSON.stringify(v)); } catch {} } };

/* ---------- application installable (PWA) ---------- */
if ('serviceWorker' in navigator && location.protocol !== 'file:') addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => {}));
// Nouvelle version mise en ligne : on recharge une fois, sauf si l'utilisateur est en train d'écrire.
if ('serviceWorker' in navigator && navigator.serviceWorker.controller) navigator.serviceWorker.addEventListener('controllerchange', () => {
  const busy = () => document.activeElement?.matches?.('input, textarea, [contenteditable=true]') || [...document.querySelectorAll('textarea')].some(t => t.value.trim());
  const go = () => { if (!busy()) location.reload(); };
  if (document.hidden) go(); else { go(); document.addEventListener('visibilitychange', () => document.hidden && go()); }
}, {once: true});
let installEvt = null;
const standalone = () => matchMedia('(display-mode: standalone)').matches || navigator.standalone === true;
const isIOS = () => /iphone|ipad|ipod/i.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
addEventListener('beforeinstallprompt', e => { e.preventDefault(); installEvt = e; if (api.user) renderMe(); });
addEventListener('appinstalled', () => { installEvt = null; if (api.user) renderMe(); });
async function installApp() {
  if (installEvt) { installEvt.prompt(); await installEvt.userChoice.catch(() => {}); installEvt = null; renderMe(); return; }
  $('#dlgT').textContent = 'Installer l’application';
  $('#dlgB').innerHTML = isIOS()
    ? `<ol class="steps-ios"><li>Ouvre ce site dans <b>Safari</b>.</li><li>Touche le bouton <b>Partager</b> (carré avec une flèche vers le haut).</li><li>Choisis <b>« Sur l’écran d’accueil »</b>, puis <b>Ajouter</b>.</li></ol><p class="small">L’icône Colle express apparaît alors sur ton écran d’accueil et s’ouvre en plein écran, comme une application.</p>`
    : `<ol class="steps-ios"><li>Ouvre ce site dans <b>Chrome</b> (ou Edge).</li><li>Menu <b>⋮</b> → <b>« Installer l’application »</b> (ou « Ajouter à l’écran d’accueil »).</li></ol><p class="small">Sur ordinateur, l’icône d’installation apparaît aussi à droite de la barre d’adresse.</p>`;
  $('#dlg').showModal();
}

/* ---------- état ---------- */
let BASE = [], BANK = [], CORR = {};
// Corrigés : un petit fichier par exercice, chargé à la première ouverture (puis gardé en mémoire).
const CORR_P = {}, CORR_W = new Set();   // promesses en cours ; exercices affichés en attente de leur corrigé
function loadCorr(id) {
  if (!id || CORR[id] || CORR_P[id]) return CORR_P[id] || Promise.resolve(CORR[id]);
  return CORR_P[id] = fetch('data/corr/' + encodeURIComponent(id) + '.json')
    .then(r => r.ok ? r.json() : null).then(d => { if (d) CORR[id] = d; return d; })   // pas de corrigé : on ne redemande pas
    .catch(() => { delete CORR_P[id]; return null; });
}
const all = () => BASE.concat(BANK);
const byId = id => all().find(e => e.id === id);
const F = Object.assign({lvl: 1, mat: '', chap: '', q: ''}, store.get('filters', {}));
let CUR = null, SUIVI = {}, CONF = {message: '', sel: {}}, CLASS = [], PRES = {}, LIVE = [];
const SESS = {};
let GROUPS = [], MES = [];
const FIL = {}, MEMB = {};
const ROLE = {responsable: 'Responsable', moderateur: 'Modérateur', membre: 'Membre'};
const ENGAGEMENT = 'Je déclare sur l’honneur que cette réponse est mon travail personnel, rédigé sans aide extérieure non signalée.';
const myGroups = () => GROUPS.filter(g => g.role || api.isProf);
const GSEL = () => { const g = store.get('groupe', null), l = myGroups(); return (l.find(x => x.id === g) || l.find(x => x.role) || l[0])?.id || null; };
const gById = g => GROUPS.find(x => x.id === g);
const myRole = g => gById(g)?.role || null;
const canMod = g => api.isProf || ['responsable', 'moderateur'].includes(myRole(g));
const moy = ns => ns?.length ? ns.reduce((a, n) => a + n.note, 0) / ns.length : null;
const fmtNote = v => v == null ? '—' : String(Math.round(v * 10) / 10).replace('.', ',');
const nameOf = (g, u) => u === api.user.id ? (api.profile.full_name || 'Moi') : (MEMB[g] || []).find(m => m.user_id === u)?.full_name || CARTES[u]?.nom || 'Ancien membre';
const who = (g, u) => `<a class="who" href="#u/${esc(CARTES[u]?.username || (u === api.user.id ? MYUSER || u : u))}">${esc(nameOf(g, u))}</a>`;
let MYUSER = '';
const mine = (ex, g) => MES.find(r => r.exercice_id === ex && (!g || r.groupe_id === g));
const notice = h => { $('#notice').innerHTML = h || ''; };

/* ---------- textes fixes ---------- */
document.querySelectorAll('[data-site]').forEach(e => e.textContent = CONFIG.NOM_SITE);
document.querySelectorAll('[data-prof]').forEach(e => e.textContent = CONFIG.NOM_PROF);
$('#aboutMini').innerHTML = presentationCourte();
document.querySelectorAll('#yr, .yr').forEach(e => e.textContent = new Date().getFullYear());
document.querySelectorAll('[data-ic]').forEach(e => { e.innerHTML = ic(e.dataset.ic); });
initTheme();
initMouvement();
initTactile();
document.querySelectorAll('[data-theme-toggle]').forEach(b => b.innerHTML = THEME_ICON);
reveal();
typeset($('#auth'));
rotator(); heroBackground(); carousel(document.querySelector('.car'));
initVitrine();
document.querySelectorAll('[data-count]').forEach(e => +e.dataset.count && countUp(e, e.dataset.count));
document.querySelectorAll('[data-nbfig]').forEach(e => countUp(e, Object.keys(FIG).length));
// chiffres réels de la page d'accueil (fichier statique, mis en cache par le service worker)
fetch('data/exercices.json').then(r => r.json()).then(L => { document.querySelectorAll('[data-nbex]').forEach(e => countUp(e, L.length));
  document.querySelectorAll('[data-nbchap]').forEach(e => countUp(e, new Set(L.map(x => x.mat + x.chap)).size)); }).catch(() => {});
$('#searchIc').outerHTML = ic('search');
if (DEMO) $('#demo').hidden = false;

/* ---------- MathJax ---------- */
// Le moteur de formules (≈ 250 Ko) se télécharge après l'affichage de la page, quand le réseau est libre,
// ou tout de suite si l'on ouvre un exercice avant. typeset() attend qu'il soit prêt.
let MJ = false;
function loadMathJax() {
  if (MJ || window.MathJax?.typesetPromise) return; MJ = true;
  const s = document.createElement('script'); s.src = 'https://cdn.jsdelivr.net/npm/mathjax@4.1.3/tex-chtml.js'; s.async = true;
  document.head.append(s);
}
addEventListener('load', () => (window.requestIdleCallback || setTimeout)(loadMathJax, {timeout: 1500}));
// Accepte un élément ou une liste. Le contenu des accordéons fermés est composé à leur ouverture
// (MathJax a besoin de la largeur réelle pour couper les formules longues).
function typeset(el) {
  const els = (Array.isArray(el) ? el : [el]).filter(Boolean);
  if (!els.length) return;
  if (window.MathJax?.typesetPromise) { MathJax.typesetClear?.(els); MathJax.typesetPromise(els).catch(() => {}); }
  else setTimeout(() => typeset(els), 400);
}
const visibleParts = el => [...el.children].flatMap(c => c.matches('details:not([open])') ? [c.querySelector('summary')] : c.querySelectorAll('details:not([open])').length
  ? [...c.querySelectorAll(':scope > :not(details), :scope details[open] > .acc-body, summary')] : [c]);
function lazyTypeset(d) {
  d.addEventListener('toggle', () => { const b = d.querySelector(':scope > .acc-body'); if (d.open && b && !b.dataset.ty) { b.dataset.ty = 1; typeset(b); } });
  if (d.open) { const b = d.querySelector(':scope > .acc-body'); if (b) b.dataset.ty = 1; }
}

/* ================= CONNEXION ================= */
initAuth({onSignedIn: () => start()});
on('auth', ev => { if (ev === 'in') start(); else if (ev === 'out') { api.stopLive(); showAuth('in'); } else if (ev === 'recovery') showAuth('new'); });

/* ================= DÉMARRAGE APPLICATION ================= */
let started = false;
async function start() {
  if (!api.user) return showAuth('in');
  $('#auth').hidden = true; $('#app').hidden = false; document.body.classList.remove('on-landing');
  renderMe();
  return afterLogin2();
}
function renderMe() {
  const p = api.profile;
  $('#me').innerHTML = `<button class="avbtn" id="mePhoto" title="Changer ma photo de profil" aria-label="Changer ma photo de profil">${avatar(p.id, p.full_name)}</button><span class="small" style="color:var(--ink);font-weight:600">${esc(p.full_name || 'Moi')}</span><span class="dot" id="conn"></span>${!standalone() && (installEvt || isIOS() || matchMedia('(max-width: 820px)').matches) ? `<button class="btn ghost" id="inst" title="Installer l’application">${ic('download')}<span class="lbl-inst">Installer</span></button>` : ''}<button class="themebtn" type="button" data-theme-toggle aria-label="Changer de thème">${THEME_ICON}</button><button class="btn ghost" id="out" title="Se déconnecter" aria-label="Se déconnecter">${ic('logout')}</button>`;
  syncTheme();
  $('#inst') && ($('#inst').onclick = installApp);
  $('#out').onclick = () => api.signOut();
  $('#mePhoto').onclick = pickPhoto;
}
async function afterLogin2() {
  const p = api.profile;
  $('#nav').innerHTML = `<a href="#exercices" data-v="exercices" title="Exercices">${ic('book')}<span class="lbl">Exercices</span></a><a href="#groupes" data-v="groupes" title="Groupes">${ic('users')}<span class="lbl">Groupes</span></a><a href="#suivi" data-v="suivi" title="Suivi">${ic('chart')}<span class="lbl">Suivi</span></a><a href="#carnet" data-v="carnet" title="Carnet">${ic('pen')}<span class="lbl">Carnet</span></a><a href="#communaute" data-v="communaute" title="Communauté">${ic('share')}<span class="lbl">Communauté</span></a><a href="#profil" data-v="profil" title="Profil">${ic('user')}<span class="lbl">Profil</span></a>` +
    (api.isProf ? `<a href="#prof" data-v="prof" title="Tableau de bord">${ic('live')}<span class="lbl lbl-long">Tableau de bord</span> <span class="count-pill" id="liveN">0</span></a>` : '') +
    '';   // « À propos » et l'envoi de sujets restent accessibles par le pied de page et « Mon suivi »
  initProfil({byId, all, LV, typeset, pickPhoto, ref: () => PREF, myAvatar: () => avatar(api.user.id, api.profile.full_name).replace('class="avatar"', 'class="avatar pe-av"'), setUsername: u => { MYUSER = u; }});
  api.monProfil().then(pp => { MYUSER = pp?.username || ''; }).catch(() => {});
  $('#bnav').innerHTML = $('#nav').innerHTML;
  $('#bnav a[data-v=suivi]')?.remove(); $('#bnav a[data-v=prof]')?.remove();   // sur téléphone, le tableau de bord s'ouvre depuis le profil   // 5 entrées au plus sur téléphone ; « Mon suivi » reste accessible depuis le profil
  initCarnet({byId, all, typeset});
  initBiblio({byId, LV});
  initCommunaute({byId, typeset, avatar, myId: () => api.user.id,
    cartes: async ids => { const need = ids.filter(u => u && u !== api.user.id && !CARTES[u]); if (need.length) for (const c of await api.cartes(need)) CARTES[c.id] = c; return CARTES; }});
  if (!store.get('filters', null)) F.lvl = p.niveau || 1;
  [SUIVI, CONF, BANK] = await Promise.all([api.loadSuivi(), api.config(), api.banque()]);
  SUIVI = SUIVI && typeof SUIVI === 'object' ? SUIVI : {};
  await loadGroups();
  renderMe();
  if (!started) {
    started = true;
    on('config', async () => { CONF = await api.config(); rerender(); });
    on('banque', async () => { BANK = await api.banque(); rerender(); });
    on('classe', debounce(async () => { CLASS = await api.classe(); rerender(); }, 800));
    on('presence', st => { PRES = st; const n = Object.keys(PRES).length; document.querySelectorAll('#liveN').forEach(el => el.textContent = n); $('#conn')?.classList.add('on'); rerenderProf(); });
    on('groupe', debounce(async ev => {
      if (ev?.t === 'groupe_membres' || !ev) { await loadGroups(); for (const k in MEMB) delete MEMB[k]; }
      else { MES = await api.mesReponses().catch(() => MES); syncNotes(); }
      const v = document.querySelector('.view.on')?.id;
      if (v === 'v-groupes') renderGroupes();
      else if (v === 'v-exercices' && CUR) { const G = GSEL(); if (G) await loadFil(CUR, G); renderRep(byId(CUR)); }
    }, 400));
    on('activity', a => { if (!api.isProf || !a) return; LIVE.unshift({...a, d: now()}); LIVE = LIVE.slice(0, 60); rerenderProf(); });
  }
  if (api.isProf) CLASS = await api.classe();
  presence({v: 'exercices'});
  route();
}
/* ---------- envoi de sujets d'oraux (PDF) par e-mail, via FormSubmit ---------- */
let SENT = false;
function bindEnvoi() {
  const f = $('#envoi form'); if (!f) return;
  f.querySelector('[name=_next]').value = location.href.split('#')[0] + '#merci';
  f.onsubmit = e => {
    const file = f.querySelector('[name=attachment]').files[0], err = f.querySelector('.err');
    if (!file) { e.preventDefault(); err.textContent = 'Choisis un fichier PDF.'; return; }
    if (!/pdf$/i.test(file.type) && !/\.pdf$/i.test(file.name)) { e.preventDefault(); err.textContent = 'Seuls les fichiers PDF sont acceptés.'; return; }
    if (file.size > 10e6) { e.preventDefault(); err.textContent = 'Fichier trop lourd (10 Mo maximum) : compresse-le ou envoie-le en plusieurs parties.'; return; }
    err.textContent = '';
    try { sessionStorage.setItem('ce:contrib', file.name.replace(/\.pdf$/i, '').slice(0, 120)); } catch {}
    if (f.dataset.native) return;                        // repli : envoi classique du formulaire
    e.preventDefault();
    const btn = f.querySelector('button[type=submit]'), lab = btn.innerHTML;
    btn.disabled = true; btn.textContent = 'Envoi en cours…';
    const reset = msg => { btn.disabled = false; btn.innerHTML = lab; if (msg) err.textContent = msg; };
    const ctl = new AbortController(), to = setTimeout(() => ctl.abort(), 60000);
    // Envoi en arrière-plan (point d'accès AJAX de FormSubmit) : la réponse s'affiche ici même.
    fetch(f.action.replace('formsubmit.co/', 'formsubmit.co/ajax/'), {method: 'POST', body: new FormData(f), headers: {Accept: 'application/json'}, signal: ctl.signal})
      .then(r => r.json().catch(() => ({})).then(j => ({ok: r.ok, j})))
      .then(({ok, j}) => {
        clearTimeout(to);
        if (ok && String(j.success) === 'true') { SENT = true; route(); setTimeout(() => $('#envoi')?.scrollIntoView({behavior: 'smooth'}), 60); return; }
        const m = String(j.message || '');
        reset(/activ/i.test(m) ? 'Le formulaire doit d’abord être activé : ouvre l’e-mail « Activate Form » reçu par ' + (CONFIG.ENVOI_EMAIL || 'l’administrateur') + ', puis renvoie le fichier.'
          : 'L’envoi a échoué' + (m ? ' : ' + m : '') + '. Réessaie dans un instant.');
      })
      .catch(x => {
        clearTimeout(to);
        if (x?.name === 'AbortError') return reset('L’envoi a pris trop de temps : vérifie ta connexion, ou compresse le PDF.');
        f.dataset.native = '1'; btn.disabled = false; f.requestSubmit ? f.requestSubmit() : f.submit();   // réseau ou CORS : envoi classique
      });
  };
}
// Retour arrière depuis la page de FormSubmit : le bouton redevient utilisable.
addEventListener('pageshow', () => document.querySelectorAll('#envoi button[type=submit]').forEach(b => { b.disabled = false; }));

/* ---------- photo de profil : recadrée en carré 160 px, enregistrée dans le suivi de l'élève ---------- */
function pickPhoto(after) {
  const inp = document.createElement('input');
  inp.type = 'file'; inp.accept = 'image/*';
  inp.onchange = async () => {
    const f = inp.files?.[0]; if (!f) return;
    if (!/^image\//.test(f.type)) return notice('Choisis une image (JPEG, PNG…).');
    try {
      const url = URL.createObjectURL(f);
      const img = await new Promise((res, rej) => { const i = new Image(); i.onload = () => res(i); i.onerror = rej; i.src = url; });
      const S = 160, c = document.createElement('canvas'); c.width = c.height = S;
      const side = Math.min(img.naturalWidth, img.naturalHeight);
      c.getContext('2d').drawImage(img, (img.naturalWidth - side) / 2, (img.naturalHeight - side) / 2, side, side, 0, 0, S, S);
      URL.revokeObjectURL(url);
      setPhoto(c.toDataURL('image/jpeg', 0.85)); after?.();
    } catch { notice('Image illisible : essaie une autre photo.'); }
  };
  inp.click();
}
function setPhoto(dataUrl) {
  if (dataUrl) SUIVI.photo = dataUrl; else delete SUIVI.photo;
  api.saveSuivi(SUIVI);
  renderMe(); rerender();
}
function debounce(f, ms) { let t; return (...a) => { clearTimeout(t); t = setTimeout(() => f(...a), ms); }; }

/* ---------- présence ---------- */
let pres = {};
function presence(patch) {
  Object.assign(pres, patch);
  if (patch.v && patch.v !== 'exercices') Object.assign(pres, {ex: null, t: null, st: null, n: null});
  api.live({...pres, name: api.profile.full_name, role: api.profile.role, since: pres.since || now()});
}

/* ---------- routage ---------- */
let LISTY = 0;   // position de la liste au moment d'ouvrir un exercice (téléphone)
const phone = () => innerWidth < 820;
function route() {
  if (!api.user) return;
  let h = location.hash.slice(1) || 'exercices';
  if (h === 'merci') { SENT = true; history.replaceState(null, '', '#apropos'); h = 'apropos'; }
  if (h.startsWith('ex-')) { const e = byId(h.slice(3)); if (e) { CUR = e.id; F.lvl = e.niveau; } h = 'exercices'; }
  else if (h === 'exercices' && CUR) {   // retour (geste ou bouton) depuis un exercice
    const back = document.body.classList.contains('detail'); CUR = null;
    presence({v: 'exercices', ex: null, t: null, st: null});
    if (back && phone()) setTimeout(() => scrollTo({top: LISTY, behavior: 'instant'}), 0);
  }
  document.body.classList.toggle('detail', h === 'exercices' && !!CUR);
  if (h === 'prof' && !api.isProf) h = 'exercices';
  if (h === 'envoyer') { h = 'apropos'; setTimeout(() => $('#envoi')?.scrollIntoView({behavior: 'smooth'}), 50); }
  let pref = null, pmode = '';
  let cref = null;
  if (h.startsWith('c/')) { cref = decodeURIComponent(h.slice(2)); h = 'collection'; }
  let ctab = '';
  if (h.startsWith('communaute')) { ctab = h.split('/')[1] || 'annuaire'; h = 'communaute'; }
  if (h.startsWith('u/')) { pref = decodeURIComponent(h.slice(2)); h = 'profil'; }
  else if (h === 'profil' || h.startsWith('profil/')) { pmode = h.split('/')[1] || ''; pref = MYUSER || api.user.id; h = 'profil'; }
  if (!['exercices', 'groupes', 'suivi', 'prof', 'apropos', 'profil', 'carnet', 'collection', 'communaute'].includes(h)) h = 'exercices';
  document.querySelectorAll('.view').forEach(v => v.classList.toggle('on', v.id === 'v-' + h));
  document.querySelectorAll('#nav a, #bnav a').forEach(a => a.dataset.v === h ? a.setAttribute('aria-current', 'page') : a.removeAttribute('aria-current'));
  if (h === 'exercices') { renderStrip(); renderList(); renderCopy(); }
  if (h === 'suivi') renderSuivi();
  if (h === 'groupes') renderGroupes();
  if (h === 'prof') renderProf(true);
  if (h === 'carnet') { renderCarnet($('#v-carnet')); scrollTo(0, 0); }
  if (h === 'communaute') { renderCommunaute($('#v-communaute'), ctab); }
  if (h === 'collection') { renderCollection($('#v-collection'), cref); scrollTo(0, 0); }
  if (h === 'profil') { PREF = pref; const v = $('#v-profil'); if (pmode === 'modifier') renderEdition(v); else renderProfil(v, pref, {apercu: pmode === 'apercu'}); scrollTo(0, 0);
    document.querySelectorAll('#nav a[data-v=profil], #bnav a[data-v=profil]').forEach(a => pref === MYUSER || pref === api.user.id ? a.setAttribute('aria-current', 'page') : a.removeAttribute('aria-current')); }
  if (SENT && h === 'apropos') { const t = sessionStorage.getItem('ce:contrib'); if (t != null) { sessionStorage.removeItem('ce:contrib'); api.contribution(t).catch(() => {}); } }
  if (h === 'apropos') { $('#v-apropos').innerHTML = presentationPage({nom: api.profile.full_name, email: api.user.email, merci: SENT}); bindEnvoi(); SENT = false; }
  if (pres.v !== h) presence({v: h});
}
let PREF = null;
addEventListener('hashchange', route);
function rerender() {
  const v = document.querySelector('.view.on')?.id;
  if (v === 'v-exercices') { renderStrip(); renderList(); if (!CUR || !sess(CUR).busy) renderCopy(); }
  else if (v === 'v-suivi') renderSuivi();
  else if (v === 'v-groupes') renderGroupes();
  else if (v === 'v-prof') renderProf(false);
}
const rerenderProf = debounce(() => { if (document.querySelector('.view.on')?.id === 'v-prof') renderProf(false); }, 200);

/* ================= EXERCICES ================= */
function renderStrip() {
  const lvl = F.lvl, atL = all().filter(e => e.niveau === lvl);
  const ok = atL.filter(e => SUIVI.ex?.[e.id]?.s === 'reussi').length;
  const first = (api.profile.full_name || '').split(' ')[0];
  $('#strip').innerHTML = `<div><h2>Bonjour ${esc(first)} !</h2>
      ${CONF.message ? `<p class="msg">${ic('msg')} ${esc(CONF.message)}</p>` : `<p>Niveau ${LV[lvl]} : ${esc(LVD[lvl])}. Choisis un exercice, cherche, soumets ta réponse sur l’honneur à ton groupe, puis note et discute celles des autres.</p>`}</div>
    <div class="mini"><div><b>${ok}</b><span>réussis</span></div><div><b>${atL.length}</b><span>exercices</span></div><div><b>${Object.values(SUIVI.ex || {}).reduce((a, x) => a + (x.e || 0), 0)}</b><span>réponses</span></div></div>`;
}
const favs = () => Array.isArray(SUIVI.fav) ? SUIVI.fav : [];
const isFav = id => favs().includes(id);
async function toggleFav(id) {
  SUIVI.fav = isFav(id) ? favs().filter(x => x !== id) : [id, ...favs()].slice(0, 300);
  renderList(); if (CUR === id) renderFavBtn();
  await api.saveSuivi(SUIVI);
}
function renderFavBtn() {
  const b = $('#bFav'); if (!b || !CUR) return;
  const on = isFav(CUR); b.setAttribute('aria-pressed', on); b.title = on ? 'Retirer des favoris' : 'Enregistrer dans mes favoris';
  b.querySelector('.lbl') && (b.querySelector('.lbl').textContent = on ? 'Enregistré' : 'Enregistrer');
}
const norm = t => String(t).normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
const HAY = new Map();   // texte de recherche pré-calculé par exercice
const hay = e => HAY.get(e.id) || (HAY.set(e.id, norm(e.titre + ' ' + e.chap + ' ' + e.mat + ' ' + (e.concours || '') + ' ' + e.enonce)), HAY.get(e.id));
const match = (e, q) => !q || q.split(/\s+/).every(w => hay(e).includes(w));   // tous les mots, dans n'importe quel ordre
function filtered() {
  const q = norm(F.q.trim());
  if (F.fav) return favs().map(byId).filter(Boolean).filter(e => match(e, q));
  return all().filter(e => e.niveau === F.lvl && (!F.mat || e.mat === F.mat) && (!F.chap || e.chap === F.chap) && match(e, q));
}
const statusOf = id => SUIVI.ex?.[id]?.s || '';
const finOf = id => !!SUIVI.ex?.[id]?.fin;   // « fait » : coché par l'élève lui-même (distinct de « réussi », validé par les pairs, et de « terminé », réponse soumise)
// exercices consultés récemment (sur cet appareil)
const VUS = () => store.get('vus', []);
const vu = id => store.set('vus', [id, ...VUS().filter(x => x !== id)].slice(0, 12));
function listOrder() {
  const sel = new Set(CONF.sel?.[F.lvl] || []), order = ['Maths', 'Physique', 'Chimie', 'Informatique'];
  return filtered().sort((a, b) => (sel.has(b.id) - sel.has(a.id)) || order.indexOf(a.mat) - order.indexOf(b.mat) || a.chap.localeCompare(b.chap, 'fr'));
}
function renderList() {
  $('#fLvl').innerHTML = [1, 2, 3].map(n => `<button data-n="${n}" aria-pressed="${n === F.lvl}" title="${LV[n]}"><span class="dots" aria-hidden="true">${'●'.repeat(n)}${'○'.repeat(3 - n)}</span>${{1: 'CCINP', 2: 'Mines-CS', 3: 'X-ENS'}[n]}</button>`).join('');
  $('#fMat').innerHTML = [['', 'Tout'], ['Maths', 'Maths'], ['Physique', 'Physique'], ['Chimie', 'Chimie'], ['Informatique', 'Info']].map(([m, l]) => `<button data-m="${m}" aria-pressed="${m === F.mat}">${m ? ic(MAT_IC[m]) : ''}${l}</button>`).join('');
  const chaps = [...new Set(all().filter(e => e.niveau === F.lvl && (!F.mat || e.mat === F.mat)).map(e => e.chap))].sort((a, b) => a.localeCompare(b, 'fr'));
  if (F.chap && !chaps.includes(F.chap)) F.chap = '';
  $('#fChap').innerHTML = `<option value="">Tous les chapitres (${chaps.length})</option>` + chaps.map(c => `<option ${c === F.chap ? 'selected' : ''}>${esc(c)}</option>`).join('');
  if (document.activeElement !== $('#fQ')) $('#fQ').value = F.q;
  $('#fFav').setAttribute('aria-pressed', !!F.fav); $('#fFav').innerHTML = `${ic('heart')} Favoris <span class="nb">${favs().length}</span>`;
  document.querySelector('.filters').classList.toggle('favmode', !!F.fav);
  $('#fVue').innerHTML = [['liste', 'list', 'Liste'], ['grille', 'grid', 'Grille']].map(([v, i, l]) => `<button data-vue="${v}" aria-pressed="${(F.vue || 'liste') === v}" title="Affichage en ${l.toLowerCase()}">${ic(i)}<span class="sr">${l}</span></button>`).join('');
  document.querySelector('.work')?.classList.toggle('vue-grille', F.vue === 'grille' && !CUR && innerWidth >= 1000);
  const sel = new Set(CONF.sel?.[F.lvl] || []);
  const list = listOrder();
  $('#items').innerHTML = list.length ? list.map(e => {
    const s = statusOf(e.id);
    return `<button class="item" data-id="${esc(e.id)}" aria-current="${e.id === CUR}">
      <span class="tile ${e.mat}">${ic(chapIcon(e.mat, e.chap))}</span>
      <span class="t">${sel.has(e.id) ? `<span style="color:var(--gold)">★</span> ` : ''}${esc(e.titre)}</span>
      <span class="st ${s === 'reussi' ? 'ok' : finOf(e.id) ? 'fin' : s ? 'go' : ''}" title="${s === 'reussi' ? 'Réussi : validé par tes pairs' : finOf(e.id) ? 'Fait (coché par toi)' : s ? 'En cours' : 'À faire'}">${s === 'reussi' ? ic('check') : finOf(e.id) ? ic('check') : s ? '•' : ''}</span>
      <span class="m">${F.fav ? LV[e.niveau] + ' · ' : ''}${esc(e.chap)} · ${e.duree} min${FIG[e.id] ? ' · schéma' : ''}${isFav(e.id) ? ' · <span class="fv">♥</span>' : ''}</span>${F.vue === 'grille' && !CUR ? `<span class="gx">${fmtEnonce(extrait(String(e.enonce).trim().replace(/^\s*(\d+|[a-z])[.)]\s+/gm, '').replace(/\n(?!\n)/g, ' '), 160)).replace(/<\/?(p|ol|ul|li)[^>]*>/g, ' ')}</span>` : ''}</button>`;
  }).join('') : `<div class="empty">${F.fav ? 'Aucun favori pour l’instant : touche le cœur d’un exercice pour l’enregistrer.' : 'Aucun exercice pour ces filtres.'}</div>`;
  if (F.vue === 'grille' && !CUR) typeset($('#items'));
  const done = list.filter(e => statusOf(e.id) === 'reussi').length;
  $('#count').textContent = `${list.length} exercice${list.length > 1 ? 's' : ''} · ${done} réussi${done > 1 ? 's' : ''}`;
  store.set('filters', F);
}
$('#fLvl').onclick = e => { const b = e.target.closest('button'); if (b) { F.lvl = +b.dataset.n; renderStrip(); renderList(); } };
$('#fMat').onclick = e => { const b = e.target.closest('button'); if (b) { F.mat = b.dataset.m; renderList(); } };
$('#fChap').onchange = e => { F.chap = e.target.value; renderList(); };
$('#fQ').oninput = e => { F.q = e.target.value; renderList(); };
$('#fFav').onclick = () => { F.fav = !F.fav; renderList(); };
$('#fVue').onclick = e => { const b = e.target.closest('[data-vue]'); if (b && b.dataset.vue !== (F.vue || 'liste')) { F.vue = b.dataset.vue; renderList(); } };
$('#items').onclick = e => { const b = e.target.closest('.item'); if (b) openEx(b.dataset.id); };
// on commence à télécharger le corrigé dès que le doigt se pose sur l'exercice
$('#items').addEventListener('pointerdown', e => { const b = e.target.closest('.item'); if (b) loadCorr(b.dataset.id); }, {passive: true});
function openEx(id) {
  loadMathJax(); vu(id);
  const from = CUR; CUR = id; const ex = byId(id);
  if (phone() && !from) { LISTY = scrollY; history.pushState({ce: 'ex'}, '', '#ex-' + id); }   // le geste « retour » du téléphone ramène à la liste
  else history.replaceState(history.state, '', '#ex-' + id);
  renderList(); renderCopy();
  presence({v: 'exercices', ex: id, t: ex?.titre?.slice(0, 90) || '', n: ex?.niveau || 0, st: 'lit', since: now()});
  document.body.classList.add('detail');
  scrollTo({top: innerWidth < 820 ? 0 : scrollY});
}
function closeEx() {
  if (history.state?.ce === 'ex') { history.back(); return; }   // même chemin que le geste retour
  history.replaceState(null, '', '#exercices'); route();
}
const correctionURL = id => new URL('correction.html?id=' + encodeURIComponent(id), location.href).href;
async function shareEx(ex, withCorr) {
  const url = correctionURL(ex.id) + (withCorr ? '' : '&enonce=1');
  const title = (withCorr ? 'Corrigé — ' : 'Exercice — ') + ex.titre;
  try {
    if (navigator.share) { await navigator.share({title, text: `${title} (${CONFIG.NOM_SITE})`, url}); return; }
  } catch (e) { if (e?.name === 'AbortError') return; }
  try { await navigator.clipboard.writeText(url); toast('Lien du corrigé copié dans le presse-papiers.', 'ok'); }
  catch { notice(`Lien à partager : <a href="${esc(url)}" target="_blank" rel="noopener">${esc(url)}</a>`); }
}

/* ---------- défis du jour et de la semaine ---------- */
const lesDefis = () => defis({S: SUIVI, byId, pick: dailyPick(api.profile.niveau || F.lvl || 1, SUIVI), lvl: api.profile.niveau || F.lvl || 1});
function feterDefis(anchor) {
  const N = nouveaux(lesDefis(), store);
  if (N.length) { toast(N.length > 1 ? `${N.length} défis réussis : ${N.map(d => d.titre).join(', ')}.` : `Défi réussi : ${N[0].titre}.`, 'ok', 5000); if (anchor) celebrate(anchor, 'Défi réussi'); }
}
/* ---------- terminé, précédent / suivant ---------- */
function toggleDone(ex) {
  SUIVI.ex ||= {};
  const st = SUIVI.ex[ex.id] ||= {s: 'en_cours', e: 0, i: 0, sc: 0, d: now(), t: 0};
  st.fin = st.fin ? 0 : 1; if (st.fin) st.df = now();
  api.saveSuivi(SUIVI); renderList(); renderCopy();
  if (st.fin) { const b = $('#bDone'); b?.classList.add('pop'); const before = store.get('defis-ok', []).length; feterDefis(b); if (store.get('defis-ok', []).length === before) toast('Exercice coché comme fait.', 'ok'); }
}
function voisins(ex) {
  const L = listOrder(), i = L.findIndex(e => e.id === ex.id);
  return i < 0 ? [null, null] : [L[i - 1] || null, L[i + 1] || null];
}
function exNavHTML(ex) {
  const [p, n] = voisins(ex); if (!p && !n) return '';
  const b = (e, dir) => e ? `<button class="exn ${dir}" data-open="${esc(e.id)}"><span class="k">${ic(dir === 'prev' ? 'back' : 'arrow')} ${dir === 'prev' ? 'Précédent' : 'Suivant'}</span><b>${esc(e.titre)}</b><span class="small">${esc(e.chap)} · ${e.duree} min</span></button>` : '<span></span>';
  return `<nav class="exnav" aria-label="Exercice précédent ou suivant">${b(p, 'prev')}${b(n, 'next')}</nav>`;
}
// raccourcis : ← → pour passer d'un exercice à l'autre (hors saisie)
addEventListener('keydown', e => {
  if (!CUR || e.altKey || e.ctrlKey || e.metaKey || e.shiftKey || e.target.closest?.('input,textarea,select,[contenteditable=true],.vx-track,[role=tablist]')) return;
  if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
  const ex = byId(CUR); if (!ex || !document.body.classList.contains('detail') && !$('#v-exercices.on')) return;
  const [p, n] = voisins(ex), t = e.key === 'ArrowLeft' ? p : n;
  if (t) { e.preventDefault(); openEx(t.id); }
});

/* ---------- accueil de la bibliothèque (aucun exercice ouvert) ---------- */
function renderAccueil(el) {
  const lvl = F.lvl, sel = (CONF.sel?.[lvl] || []).map(byId).filter(Boolean);
  const vus = VUS().map(byId).filter(Boolean);
  const last = vus.find(e => !finOf(e.id) && statusOf(e.id) !== 'reussi');
  const pour = recommend(SUIVI, lvl).filter(e => e.id !== last?.id).slice(0, 4);
  const neufs = all().filter(e => e.ajout && e.niveau === lvl).sort((a, b) => b.ajout.localeCompare(a.ajout)).slice(0, 4);
  const neufsAll = neufs.length ? neufs : all().filter(e => e.ajout).slice(0, 4);
  const row = e => `<li><button class="arow" data-open="${esc(e.id)}"><span class="tile ${e.mat}">${ic(chapIcon(e.mat, e.chap))}</span><span class="t">${esc(e.titre)}</span><span class="m">${esc(e.chap)} · ${e.duree} min</span>${statusOf(e.id) === 'reussi' ? `<span class="st ok">${ic('check')}</span>` : finOf(e.id) ? `<span class="st fin">${ic('check')}</span>` : ''}</button></li>`;
  const col = (t, icon, L, vide) => `<section class="acol"><h3>${ic(icon)} ${t}</h3>${L.length ? `<ul>${L.map(row).join('')}</ul>` : `<p class="small">${vide}</p>`}</section>`;
  el.innerHTML = `<div class="welcome accueil">
    <div class="kicker"><span class="stamp n${lvl}">${LV[lvl]}</span><span class="small">${esc(LVD[lvl])}</span></div>
    <h2>Une colle courte, maintenant&nbsp;?</h2>
    ${last ? `<button class="resume" data-open="${esc(last.id)}"><span class="k">Reprendre là où tu t’es arrêté</span><b>${esc(last.titre)}</b><span class="m">${esc(last.mat)} · ${esc(last.chap)} · ${last.duree} min</span><span class="go">${ic('arrow')}</span></button>` : ''}
    <div class="acc-defis">${defisHTML(lesDefis(), {compact: true})}</div>
    <div class="acols">
      ${col('Pour toi', 'target', pour, 'Termine ou réussis quelques exercices : les suggestions s’adaptent à tes chapitres les moins travaillés.')}
      ${col('Consultés récemment', 'clock', vus.filter(e => e.id !== last?.id).slice(0, 4), 'Les exercices que tu ouvres apparaîtront ici.')}
      ${col('Nouveautés', 'star', neufsAll, 'Rien de nouveau pour l’instant.')}
    </div>
    ${sel.length ? `<h3 class="sec">${ic('star')} Sélection de ton professeur</h3><div class="actions">${sel.map(e => `<button class="btn" data-open="${esc(e.id)}">${ic(MAT_IC[e.mat])} ${esc(e.titre)}</button>`).join('')}</div>` : ''}
    <ol class="methode" aria-label="Comment se passe une colle">
      <li><b>Cherche</b><span>sur papier, chrono lancé</span></li>
      <li><b>Débloque-toi</b><span>un indice, puis la correction étape par étape</span></li>
      <li><b>Soumets</b><span>ta réponse, sur l’honneur, à ton groupe</span></li>
      <li><b>Évalue</b><span>les copies des autres, sur 20</span></li>
    </ol>
  </div>`;
  el.querySelectorAll('[data-open]').forEach(b => b.onclick = () => openEx(b.dataset.open));
  // au téléphone, l'accueil est sous la liste : la carte « Reprendre » remonte au-dessus des filtres
  const rm = $('#resumeM');
  if (rm) { rm.innerHTML = last ? el.querySelector('.resume').outerHTML : ''; rm.querySelector('[data-open]')?.addEventListener('click', e => openEx(e.currentTarget.dataset.open)); }
}

const sess = id => SESS[id] ||= {imgs: [], tours: [], hint: 0, start: now(), solution: '', busy: false, note: ''};
let tick = null;
function renderCopy() {
  const el = $('#copy'); clearInterval(tick);
  const ex = CUR && byId(CUR);
  if (!ex) { renderAccueil(el); return; }
  const S = sess(ex.id), st = SUIVI.ex?.[ex.id], fig = FIG[ex.id];
  api.track(ex.id, 'vu');
  S.openH ||= [];
  const K = CORR[ex.id];
  if (!K && !CORR_W.has(ex.id)) { CORR_W.add(ex.id); loadCorr(ex.id).then(d => { CORR_W.delete(ex.id); if (d && CUR === ex.id) renderCopy(); }); }
  const nH = K ? hintLevels(K).length : 2;
  const G = GSEL();
  const locked = !(S.unlocked || mine(ex.id) || st?.s === 'reussi' || S.hint >= nH);
  const sol = K || (S.solution ? {corrige: S.solution, reponse: S.reponse, theoremes: S.theoremes, astuces: S.astuces} : null);
  const aiHints = S.tours.filter(t => t.kind === 'indice' && t.indice);
  el.innerHTML = `
    <button class="back" id="bBack">${ic('back')} Exercices</button>
    <div class="kicker"><span class="stamp n${ex.niveau}">${LV[ex.niveau]}</span><span class="pill">${ic(MAT_IC[ex.mat])}${esc(ex.mat)}</span><span class="pill">${ic(chapIcon(ex.mat, ex.chap))}${esc(ex.chap)}</span></div>
    <div class="titlerow"><h2>${esc(ex.titre)}</h2>
      <div class="tools"><button class="iconbtn done" id="bDone" aria-pressed="${finOf(ex.id)}" title="Cocher l’exercice comme fait, pour ton suivi personnel">${ic('done')}<span class="lbl">${finOf(ex.id) ? 'Fait' : 'Marquer comme fait'}</span></button>
      <button class="iconbtn fav" id="bFav" aria-pressed="${isFav(ex.id)}" title="Enregistrer dans tes favoris">${ic('heart')}<span class="lbl">${isFav(ex.id) ? 'Enregistré' : 'Enregistrer'}</span></button>
      <button class="iconbtn" id="bColl" title="Ranger dans une collection">${ic('book')}<span class="lbl">Collection</span></button>
      <button class="iconbtn" id="bNote" title="Ajouter au carnet de progression">${ic('pen')}<span class="lbl">Carnet</span></button>
      <button class="iconbtn" id="bShareEx" title="Partager l’exercice">${ic('share')}<span class="lbl">Partager</span></button></div></div>
    ${st ? `<div class="status ${st.s === 'reussi' ? 'ok' : st.fin ? 'fin' : ''}">${ic(st.s === 'reussi' ? 'trophy' : st.fin ? 'done' : 'pen')} ${st.s === 'reussi' ? 'Réussi (moyenne des pairs ≥ 12/20)' : mine(ex.id) ? 'Réponse soumise' + (st.fin ? ' · fait' : '') : st.fin ? 'Fait' : 'En cours'}</div>` : ''}

    <section class="co co-enonce">
      <div class="co-h"><span class="co-e" aria-hidden="true">📘</span>Énoncé<span class="co-meta">${ic('clock')}<span class="timer" id="timer">0:00</span>&nbsp;/ ${ex.duree} min</span></div>
      <div class="ex-body ${fig ? 'withfig' : ''}"><div class="enonce">${fmtEnonce(ex.enonce)}</div>
      ${fig ? `<figure class="fig">${fig.svg}<figcaption>${ic('eye')}<span>${legHTML(fig.legende)}</span></figcaption></figure>` : ''}</div>
    </section>

    <section class="co co-rep" id="repSec">
      <div class="co-h"><span class="co-e" aria-hidden="true">✍️</span>Ma réponse
        ${myGroups().length > 1 ? `<select id="gSel" class="gsel" aria-label="Groupe">${myGroups().map(g => `<option value="${esc(g.id)}" ${g.id === G ? 'selected' : ''}>${esc(g.nom)}${g.role ? '' : ' (admin)'}</option>`).join('')}</select>` : G ? `<span class="co-meta">${ic('users')} ${esc(gById(G).nom)}</span>` : ''}</div>
      <div id="repBox"></div>
    </section>

    <section class="co co-indices" id="hintsSec">
      <div class="co-h"><span class="co-e" aria-hidden="true">💡</span>Indices<span class="co-meta">ouvre-les seulement si tu bloques</span></div>
      ${K ? hintsHTML(K, S.openH) : `${aiHints.map((t, i) => `<div class="acc-static"><span class="hn">${i + 1}</span><div>${rich(t.indice)}${t.question ? `<p class="q">« ${esc(t.question)} »</p>` : ''}</div></div>`).join('')}
        ${!CONFIG.IA && !aiHints.length ? '<p class="small">Pas d’indice préparé pour cet exercice.</p>' : ''}${CONFIG.IA && S.hint < 2 ? `<button class="btn wide" id="bHintAI" ${S.busy ? 'disabled' : ''}>${S.busy === 'indice' ? '<span class="spin"></span> …' : ic('bulb') + ` Demander l’indice ${S.hint + 1} · ${['Piste globale', 'Méthode précise'][S.hint]}`}</button>` : ''}`}
    </section>

    <section class="co co-corr" id="corrSec" aria-label="Correction"></section>

    <section class="co co-grp" id="grpSec">
      <div class="co-h"><span class="co-e" aria-hidden="true">👥</span>Réponses du groupe<span class="co-meta" id="grpMeta"></span></div>
      <div id="repList">${G ? `<div role="status" aria-label="Chargement des réponses">${SKEL(2, 'skel-card')}</div>` : '<p class="small">Les réponses des membres de ton groupe s’afficheront ici.</p>'}</div>
    </section>

    <section class="co co-sol" id="solSec">
      <div class="co-h"><span class="co-e" aria-hidden="true">✍️</span>Solutions d’élèves<span class="co-meta">rédigées et publiées volontairement</span></div>
      <div id="solList"></div>
    </section>

    <section class="co co-disc" id="discSec">
      <div class="co-h"><span class="co-e" aria-hidden="true">💬</span>Discussion<span class="co-meta" id="discMeta"></span></div>
      <div id="comList"></div>
      ${G && myRole(G) ? `<div class="comform"><div class="replyto" id="replyTo" hidden></div>
        <textarea class="note" id="comTxt" placeholder="Une question, une autre méthode, une erreur repérée… (formules entre $…$)" maxlength="4000">${esc(S.com || '')}</textarea>
        <div class="comform-b"><div class="comvis" role="radiogroup" aria-label="Visibilité du message">
          <label><input type="radio" name="comVis" value="g" ${S.comPub ? '' : 'checked'}><span>${ic('lock')} Groupe</span></label>
          <label><input type="radio" name="comVis" value="p" ${S.comPub ? 'checked' : ''}><span>${ic('users')} Public</span></label></div>
          <span class="small" id="comVisH">${S.comPub ? 'Visible par tous les membres et sur ton profil' : 'Visible par ton groupe seulement'} · Ctrl+Entrée</span><button class="btn primary" id="comSend">${ic('msg')} Publier</button></div></div>` : ''}
    </section>

    <div class="actions" id="actions">
      <button class="btn" id="bGoCopy">${ic('pen')}<span>Réponse</span></button>
      <button class="btn" id="bHint">${ic('bulb')}<span>Indice</span></button>
      <button class="btn ${locked ? '' : 'primary'}" id="bSol">${ic(locked ? 'lock' : 'book')}<span>Correction</span></button>
      <button class="btn" id="bDisc">${ic('msg')}<span>Discussion</span></button>
    </div>`;
  typeset(visibleParts(el));
  el.querySelectorAll('details.acc').forEach(lazyTypeset);
  if (el.dataset.ex !== ex.id) { el.dataset.ex = ex.id; el.classList.remove('ex-in'); void el.offsetWidth; el.classList.add('ex-in'); }
  const tm = $('#timer'); const upd = () => { const s = (now() - S.start) / 1000; tm.textContent = mmss(s); tm.classList.toggle('late', s > ex.duree * 60); };
  upd(); tick = setInterval(upd, 1000);
  renderRep(ex);
  if (G) { if (FIL[G + '|' + ex.id]) renderFil(ex, G); loadFil(ex.id, G).then(() => { if (CUR === ex.id) renderFil(ex, G); }); }
  renderSolutions($('#solList'), ex, {locked, admin: api.isProf, me: api.user.id});
  $('#gSel') && ($('#gSel').onchange = e => { store.set('groupe', e.target.value); renderCopy(); });
  bindComForm(ex, G);
  $('#bHintAI') && ($('#bHintAI').onclick = () => ask(ex, 'indice'));
  // Indices préparés : ouvrir un accordéon compte comme un indice demandé.
  el.querySelectorAll('.hint-acc').forEach(dd => dd.addEventListener('toggle', async () => {
    const i = +dd.dataset.h; S.openH[i] = dd.open;
    if (!dd.open || i + 1 <= S.hint) return;
    S.hint = i + 1;
    presence({st: 'indice'});
    api.activity({uid: api.user.id, name: api.profile.full_name, id: ex.id, k: 'indice', v: 'bloque', sc: null});
    record(ex, {kind: 'indice', verdict: 'bloque'});
    if (S.hint >= nH) { unlockCorr(); S.cmode !== 'guide' && !S.forceOpen && $('#corrSec') && cctx.redraw?.(); }
  }));
  const isLocked = () => !(S.unlocked || mine(ex.id) || st?.s === 'reussi' || S.hint >= nH);
  const nextHint = () => go('#hintsSec', () => { const nx = [...el.querySelectorAll('.hint-acc')].find(x => !x.open); if (nx) nx.open = true; else if ($('#bHintAI')) $('#bHintAI').click(); else toast('Tu as déjà vu tous les indices.', 'ok'); });
  const cctx = {ex, K, S, shareURL: correctionURL(ex.id),
    sol: () => K || (S.solution ? {corrige: S.solution, reponse: S.reponse, theoremes: S.theoremes, astuces: S.astuces} : null),
    locked: isLocked, typeset, share: () => shareEx(ex, true), nextHint,
    ensureSolution: () => ask(ex, 'solution'),
    unlock: () => { if (S.unlocked) return; S.unlocked = true; unlockCorr(); },
    record: kind => {
      if (kind === 'guide') { presence({st: 'indice'}); return; }
      if (S.seen) return; S.seen = true; presence({st: 'corrige'}); record(ex, {kind: 'solution'});
    }};
  renderCorrection($('#corrSec'), cctx);
  function unlockCorr() {
    renderSolutions($('#solList'), ex, {locked: false, admin: api.isProf, me: api.user.id});
    $('#bSol').classList.add('primary'); $('#bSol').innerHTML = `${ic('book')}<span>Correction</span>`;
  }
  const go = (sec, f) => { f?.(); $(sec).scrollIntoView({behavior: 'smooth', block: 'start'}); };
  $('#bGoCopy').onclick = () => go('#repSec', () => $('#repTxt')?.focus({preventScroll: true}));
  $('#bDisc').onclick = () => go('#discSec', () => $('#comTxt')?.focus({preventScroll: true}));
  $('#bHint').onclick = nextHint;
  $('#bSol').onclick = () => go('#corrSec');
  $('#bBack').onclick = closeEx;
  $('#bFav').onclick = () => toggleFav(ex.id);
  $('#bColl').onclick = () => openCollectionsPicker(ex.id);
  $('#bNote').onclick = () => openNote({exercice_id: ex.id, titre: ex.titre, type: 'difficile'});
  $('#bShareEx').onclick = () => shareEx(ex, false);
  $('#bDone').onclick = () => toggleDone(ex);
  el.insertAdjacentHTML('beforeend', exNavHTML(ex));
  el.querySelectorAll('.exnav [data-open]').forEach(b => b.onclick = () => { openEx(b.dataset.open); if (!phone()) $('#copy').scrollIntoView({block: 'start', behavior: 'smooth'}); });
  $('#bShareCorr') && ($('#bShareCorr').onclick = () => shareEx(ex, true));
}

/* ================= GROUPES : réponses sur l'honneur, notes, discussion ================= */
async function loadGroups() {
  try { [GROUPS, MES] = await Promise.all([api.groupes(), api.mesReponses()]); } catch (e) { GROUPS = []; MES = []; notice(esc(e.message)); }
  syncNotes();
}
// La moyenne reçue des pairs alimente le suivi : réussi si au moins 2 notes et moyenne ≥ 12/20.
function syncNotes() {
  SUIVI.ex ||= {}; let ch = false;
  const best = {};
  for (const r of MES) { const m = moy(r.notes); best[r.exercice_id] = Math.max(best[r.exercice_id] ?? -1, m ?? -1); if ((r.notes?.length || 0) >= 2 && m >= 12) best[r.exercice_id + '!'] = 1; }
  for (const r of MES) {
    const id = r.exercice_id, st = SUIVI.ex[id] ||= {s: 'en_cours', e: 1, i: 0, sc: 0, d: Date.parse(r.created_at) || now(), t: 0};
    const sc = best[id] >= 0 ? Math.round(best[id] * 5) : 0;
    if (st.sc !== sc) { st.sc = sc; ch = true; }
    if (best[id + '!'] && st.s !== 'reussi') { st.s = 'reussi'; ch = true; }
  }
  if (ch) api.saveSuivi(SUIVI);
}
async function loadFil(ex, g) {
  try {
    const [f, m] = await Promise.all([api.fil(g, ex), MEMB[g] ? MEMB[g] : api.membres(g)]);
    FIL[g + '|' + ex] = f; MEMB[g] = m;
    const inconnus = [...new Set(f.commentaires.map(c => c.user_id))].filter(u => u !== api.user.id && !CARTES[u] && !m.some(x => x.user_id === u));
    if (inconnus.length) for (const c of await api.cartes(inconnus)) CARTES[c.id] = c;
  } catch (e) { FIL[g + '|' + ex] = {reponses: [], commentaires: [], err: e.message}; }
}

/* --- encadré « Ma réponse » --- */
function renderRep(ex) {
  const box = $('#repBox'); if (!box || !ex) return;
  const S = sess(ex.id), st = SUIVI.ex?.[ex.id], G = GSEL(), g = gById(G);
  if (!G) {
    box.innerHTML = `<p>Pour soumettre ta réponse et voir celles des autres, rejoins un groupe avec le code donné par ton responsable, ou crée le tien.</p>
      <a class="btn primary wide" href="#groupes">${ic('users')} Rejoindre ou créer un groupe</a>`;
    return;
  }
  if (!g.role) { box.innerHTML = `<p class="small">Tu consultes ce groupe en tant qu’administrateur : lecture et modération, sans soumission.</p>`; return; }
  const r = mine(ex.id, G);
  if (r) {
    const m = moy(r.notes), n = r.notes?.length || 0;
    box.innerHTML = `<div class="sub-ok">${ic('check')}<div><b>Réponse soumise sur l’honneur</b> le ${fmtDate(r.created_at)}
      <span class="small">Visible par les ${g.n} membres de « ${esc(g.nom)} » · non modifiable</span></div>
      <div class="avg-big" title="Moyenne des notes reçues"><b>${fmtNote(m)}</b><span>/20</span><small>${n} note${n > 1 ? 's' : ''}</small></div></div>
      <a class="btn wide" href="#rep-${esc(r.id)}" id="seeMine">${ic('eye')} Voir ma réponse et les autres</a>`;
    $('#seeMine').onclick = e => { e.preventDefault(); $('#rep-' + r.id)?.scrollIntoView({behavior: 'smooth', block: 'start'}); };
    return;
  }
  const aide = !!(st?.vu || st?.vr);
  box.innerHTML = `
    <label class="field">Ta réponse rédigée <span class="small">(formules entre $…$, ou photos de ta feuille)</span>
      <textarea class="note big" id="repTxt" maxlength="20000" placeholder="Ex. : On pose $u_n = …$. Par récurrence…">${esc(S.rep || '')}</textarea></label>
    <div class="reptools">
      <button class="btn" id="repPrev" type="button">${ic('eye')} Aperçu</button>
      <label class="btn pick"><input type="file" id="file" accept="image/*" multiple class="sr">${ic('camera')} Ajouter des photos <span class="small">(4 max.)</span></label>
    </div>
    <div class="prev" id="repPrevBox" hidden></div>
    ${S.imgs.length ? `<div class="thumbs" id="thumbs">${S.imgs.map((im, i) => `<div class="thumb"><img src="${im.url}" alt="Page ${i + 1}"><button data-rm="${i}" aria-label="Retirer la page ${i + 1}">${ic('x')}</button></div>`).join('')}</div>` : ''}
    ${aide ? `<p class="warnline">⚠️ Tu as déjà consulté la correction ou les réponses d’autres membres : ta réponse portera la mention « aide consultée ».</p>` : ''}
    <label class="honor"><input type="checkbox" id="repHon"><span><b>Engagement sur l’honneur.</b> ${esc(ENGAGEMENT)}</span></label>
    <p class="small">Dès l’envoi, ta réponse devient publique pour les ${g.n} membre${g.n > 1 ? 's' : ''} du groupe « ${esc(g.nom)} » et ne peut plus être modifiée.</p>
    <button class="btn primary wide" id="repSend" disabled>${ic('upload')} Soumettre ma réponse</button>`;
  const txt = $('#repTxt'), hon = $('#repHon'), send = $('#repSend');
  const upd = () => { send.disabled = !(hon.checked && (txt.value.trim() || S.imgs.length)) || S.busy === 'rep'; };
  txt.oninput = () => { S.rep = txt.value; upd(); };
  hon.onchange = upd; upd();
  $('#file').onchange = e => addFiles(ex.id, e.target.files);
  $('#thumbs') && ($('#thumbs').onclick = e => { const b = e.target.closest('[data-rm]'); if (b) { S.imgs.splice(+b.dataset.rm, 1); renderRep(ex); } });
  $('#repPrev').onclick = () => { const p = $('#repPrevBox'); p.hidden = !p.hidden; if (!p.hidden) { p.innerHTML = rich(txt.value) || '<span class="small">Rien à afficher.</span>'; typeset(p); } };
  send.onclick = async () => {
    if (!hon.checked) return;
    S.busy = 'rep'; send.disabled = true; send.innerHTML = '<span class="spin"></span> Envoi…'; notice('');
    try {
      await api.soumettre({g: G, ex: ex.id, contenu: txt.value.trim(), images: S.imgs.map(i => i.data), engagementTexte: ENGAGEMENT, aide});
      S.rep = ''; S.imgs = [];
      MES = await api.mesReponses();
      await record(ex, {kind: 'reponse'});
      presence({st: 'soumis'});
      api.activity({uid: api.user.id, name: api.profile.full_name, id: ex.id, k: 'reponse', v: '', sc: null});
      S.busy = false; await loadFil(ex.id, G); renderCopy();
      $('#grpSec')?.scrollIntoView({behavior: 'smooth', block: 'start'});
    } catch (e) { S.busy = false; notice(esc(e.message)); renderRep(ex); }
  };
}

/* --- encadrés « Réponses du groupe » et « Discussion » --- */
async function renderFil(ex, G) {
  const list = $('#repList'), cl = $('#comList'); if (!list || !ex) return;
  const f = FIL[G + '|' + ex.id]; if (!f) return;
  if (f.err) { list.innerHTML = `<p class="err">${esc(f.err)}</p>`; return; }
  const S = sess(ex.id), st = SUIVI.ex?.[ex.id], me = api.user.id, member = !!myRole(G);
  const reps = f.reponses, coms = f.commentaires;
  $('#grpMeta').textContent = `${reps.length} réponse${reps.length > 1 ? 's' : ''}`;
  $('#discMeta').textContent = `${coms.length} message${coms.length > 1 ? 's' : ''}`;
  const visible = !member || mine(ex.id, G) || st?.vr || S.showReps;
  if (!reps.length) list.innerHTML = '<p class="small">Personne n’a encore soumis de réponse dans ce groupe. Lance-toi !</p>';
  else if (!visible) {
    list.innerHTML = `<p>${reps.length} membre${reps.length > 1 ? 's ont' : ' a'} déjà répondu.</p>
      <button class="btn wide" id="reveal">${ic('eye')} Afficher les réponses</button>
      <p class="small">Conseil : soumets d’abord la tienne. Les consulter avant ajoutera la mention « aide consultée » à ta réponse.</p>`;
    $('#reveal').onclick = () => { S.showReps = true; SUIVI.ex ||= {}; (SUIVI.ex[ex.id] ||= {s: 'en_cours', e: 0, i: 0, sc: 0, d: now(), t: 0}).vr = 1; api.saveSuivi(SUIVI); renderFil(ex, G); renderRep(ex); };
  } else {
    list.innerHTML = reps.map(r => {
      const own = r.user_id === me, ns = r.notes || [], m = moy(ns), my = ns.find(n => n.evaluateur_id === me)?.note;
      return `<article class="rep ${own ? 'own' : ''}" id="rep-${esc(r.id)}">
        <header>${avatar(r.user_id, nameOf(G, r.user_id))}<div><b>${who(G, r.user_id)}${own ? ' (moi)' : ''}</b><span class="small">${fmtDate(r.created_at)}</span></div>
          <span class="badges"><span class="badge honor" title="${esc(r.engagement_texte)}">🤝 Sur l’honneur</span>${r.aide_consultee ? '<span class="badge aide" title="Correction ou autres réponses consultées avant l’envoi">aide consultée</span>' : ''}</span></header>
        ${r.contenu ? `<div class="rep-body">${rich(r.contenu)}</div>` : ''}
        ${r.photos?.length ? `<div class="thumbs">${r.photos.map((p, i) => `<a class="thumb" data-ph="${esc(p)}" target="_blank" rel="noopener"><img alt="Photo ${i + 1} de la réponse"></a>`).join('')}</div>` : ''}
        <div class="rate">
          <div class="avg" title="Moyenne des pairs">${m == null ? '<span class="small">Pas encore notée</span>' : `<b>${fmtNote(m)}</b>/20 <span class="small">· ${ns.length} note${ns.length > 1 ? 's' : ''}</span>`}</div>
          ${member && !own ? `<div class="scale" role="group" aria-label="Ta note sur 20 pour ${esc(nameOf(G, r.user_id))}">${[...Array(21).keys()].map(n => `<button data-rate="${n}" data-r="${esc(r.id)}" aria-pressed="${my === n}" title="${my === n ? 'Retirer ma note' : 'Noter ' + n + '/20'}">${n}</button>`).join('')}</div>`
            : own ? '<span class="small">Tu ne peux pas noter ta propre réponse.</span>' : ''}
        </div>
        <div class="rep-act">${member ? `<button class="linkbtn" data-reply="${esc(r.id)}">${ic('msg')} Commenter</button>` : ''}
          ${canMod(G) ? `<button class="linkbtn danger" data-delrep="${esc(r.id)}">${ic('trash')} Supprimer</button>` : ''}
          ${(k => k ? `<span class="small">${k} commentaire${k > 1 ? 's' : ''}</span>` : '')(coms.filter(c => c.reponse_id === r.id).length)}</div>
      </article>`;
    }).join('');
    typeset([...list.querySelectorAll('.rep-body')]);
    const paths = reps.flatMap(r => r.photos || []);
    if (paths.length) api.photoURLs(paths).then(u => list.querySelectorAll('[data-ph]').forEach(a => { const url = u[a.dataset.ph]; if (url) { a.href = url; a.querySelector('img').src = url; } }));
    list.onclick = async e => {
      const b = e.target.closest('button'); if (!b) return;
      if (b.dataset.rate != null) {
        const n = +b.dataset.rate, cur = b.getAttribute('aria-pressed') === 'true';
        b.parentElement.querySelectorAll('button').forEach(x => x.setAttribute('aria-pressed', 'false'));
        if (!cur) b.setAttribute('aria-pressed', 'true');
        try { await api.noter(b.dataset.r, cur ? null : n); await loadFil(ex.id, G); renderFil(ex, G); } catch (x) { notice(esc(x.message)); }
      } else if (b.dataset.reply) { S.replyTo = b.dataset.reply; showReply(G); $('#discSec').scrollIntoView({behavior: 'smooth', block: 'start'}); $('#comTxt')?.focus({preventScroll: true}); }
      else if (b.dataset.delrep) {
        const r = reps.find(x => x.id === b.dataset.delrep);
        if (!confirm(`Supprimer définitivement la réponse de ${nameOf(G, r.user_id)} (et ses notes et commentaires) ?`)) return;
        try { await api.supprimerReponse(r); await loadFil(ex.id, G); MES = await api.mesReponses(); renderFil(ex, G); renderRep(ex); } catch (x) { notice(esc(x.message)); }
      }
    };
  }
  // fil de discussion
  const refName = rid => { const r = reps.find(x => x.id === rid); return r ? nameOf(G, r.user_id) : null; };
  cl.innerHTML = coms.length ? coms.map(c => {
    const own = c.user_id === me, rn = c.reponse_id && refName(c.reponse_id);
    return `<div class="com" id="com-${esc(c.id)}">${avatar(c.user_id, nameOf(G, c.user_id))}<div class="com-in">
      <div class="com-h"><b>${who(G, c.user_id)}</b>${c.public ? `<span class="badge pub" title="Visible par tous les membres connectés et sur le profil de l’auteur">${ic('users')} Public</span>` : ''}<span class="small">${ago(c.created_at)}${c.edited_at ? ' · modifié' : ''}${c.groupe_id !== G ? ' · autre groupe' : ''}</span>
        ${rn ? `<a class="ref" href="#rep-${esc(c.reponse_id)}" data-goto="${esc(c.reponse_id)}">↪ réponse de ${esc(rn)}</a>` : ''}</div>
      <div class="com-b">${rich(c.contenu)}</div>
      <div class="com-act">${own ? `<button class="linkbtn" data-edit="${esc(c.id)}">Modifier</button>` : ''}${!own && c.public ? `<button class="linkbtn" data-sigc="${esc(c.id)}">Signaler</button>` : ''}${own || (c.groupe_id === G && canMod(G)) || api.isProf ? `<button class="linkbtn danger" data-delc="${esc(c.id)}">Supprimer</button>` : ''}</div>
    </div></div>`;
  }).join('') : '<p class="small">Aucun message. Pose une question ou propose une autre méthode.</p>';
  typeset([...cl.querySelectorAll('.com-b')]);
  cl.onclick = async e => {
    const a = e.target.closest('[data-goto]'); if (a) { e.preventDefault(); if (!visible) { $('#reveal')?.click(); } $('#rep-' + a.dataset.goto)?.scrollIntoView({behavior: 'smooth', block: 'start'}); return; }
    const b = e.target.closest('button'); if (!b) return;
    if (b.dataset.sigc) return openSignalement('commentaire', b.dataset.sigc);
    if (b.dataset.delc) { if (!confirm('Supprimer ce message ?')) return; try { await api.supprimerCommentaire(b.dataset.delc); await loadFil(ex.id, G); renderFil(ex, G); } catch (x) { notice(esc(x.message)); } }
    if (b.dataset.edit) {
      const c = coms.find(x => x.id === b.dataset.edit), body = $('#com-' + c.id + ' .com-b');
      body.innerHTML = `<textarea class="note" maxlength="4000">${esc(c.contenu)}</textarea><div class="comform-b"><button class="btn ghost" data-cancel>Annuler</button><button class="btn primary" data-save>Enregistrer</button></div>`;
      body.querySelector('[data-cancel]').onclick = () => renderFil(ex, G);
      body.querySelector('[data-save]').onclick = async () => { const v = body.querySelector('textarea').value.trim(); if (!v) return; try { await api.modifierCommentaire(c.id, v); await loadFil(ex.id, G); renderFil(ex, G); } catch (x) { notice(esc(x.message)); } };
    }
  };
  showReply(G);
}
function showReply(G) {
  const S = CUR && sess(CUR), box = $('#replyTo'); if (!box || !S) return;
  const f = FIL[G + '|' + CUR], r = S.replyTo && f?.reponses.find(x => x.id === S.replyTo);
  box.hidden = !r;
  if (r) { box.innerHTML = `↪ À propos de la réponse de <b>${esc(nameOf(G, r.user_id))}</b> <button class="linkbtn" id="noReply" aria-label="Annuler">${ic('x')}</button>`; $('#noReply').onclick = () => { S.replyTo = null; showReply(G); }; }
}
function bindComForm(ex, G) {
  const t = $('#comTxt'), b = $('#comSend'); if (!t) return;
  const S = sess(ex.id);
  t.oninput = () => { S.com = t.value; };
  document.querySelectorAll('[name=comVis]').forEach(r => r.onchange = () => { S.comPub = r.value === 'p' && r.checked; $('#comVisH').textContent = (S.comPub ? 'Visible par tous les membres et sur ton profil' : 'Visible par ton groupe seulement') + ' · Ctrl+Entrée'; });
  t.onkeydown = e => { if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) { e.preventDefault(); b.click(); } };
  b.onclick = async () => {
    const v = t.value.trim(); if (!v) return;
    b.disabled = true;
    if (S.comPub && S.replyTo) notice('Une réponse à la réponse d’un camarade reste visible par le groupe seulement.');
    try { await api.commenter({g: G, ex: ex.id, rid: S.replyTo, contenu: v, pub: S.comPub}); S.com = ''; S.replyTo = null; t.value = ''; await loadFil(ex.id, G); renderFil(ex, G); }
    catch (x) { notice(esc(x.message)); }
    b.disabled = false;
  };
}

/* --- page « Groupes » --- */
let GV = null;   // groupe affiché en détail
async function renderGroupes() {
  const el = $('#v-groupes');
  const mineL = GROUPS.filter(g => g.role), others = api.isProf ? GROUPS.filter(g => !g.role) : [];
  if (!GV || !gById(GV)) GV = GSEL();
  const card = g => `<button class="gcard" data-g="${esc(g.id)}" aria-current="${g.id === GV}"><b>${esc(g.nom)}</b>
      <span class="small">${g.n} membre${g.n > 1 ? 's' : ''}</span>${g.role ? `<span class="rolepill ${g.role}">${ROLE[g.role]}</span>` : '<span class="rolepill">Administrateur</span>'}</button>`;
  el.innerHTML = `
    <div class="pagehead"><h2>Groupes</h2><span class="small">Réponses sur l’honneur, notes de 0 à 10 et discussion entre membres</span></div>
    ${mineL.length || others.length ? `<div><h3 class="sec">${ic('users')} Mes groupes</h3>
        <div class="gcards">${mineL.map(card).join('') || '<div class="empty">Tu n’es dans aucun groupe pour l’instant.</div>'}</div>
        ${others.length ? `<h3 class="sec">${ic('eye')} Autres groupes de la classe</h3><div class="gcards">${others.map(card).join('')}</div>` : ''}</div>
    <div id="gDetail"></div>
    <details class="gmore"><summary>${ic('plus')} Rejoindre ou créer un autre groupe</summary><div class="grid2">      <div><h3 class="sec">${ic('key')} Rejoindre un groupe</h3>
        <form class="panel form" id="gJoin"><label class="field">Code d’invitation<input id="gCode" autocomplete="off" maxlength="12" placeholder="Ex. : 4F9A2C" style="text-transform:uppercase"></label>
          <button class="btn primary">Rejoindre</button><span class="small err" id="gJoinErr"></span></form>
        </div><div><h3 class="sec">${ic('plus')} Créer un groupe</h3>
        <form class="panel form" id="gNew"><label class="field">Nom du groupe<input id="gNom" maxlength="60" required placeholder="Ex. : MP* — trinôme du jeudi"></label>
          <label class="field">Description (facultatif)<input id="gDesc" maxlength="300"></label>
          <button class="btn primary">Créer et devenir responsable</button><span class="small err" id="gNewErr"></span></form>
      </div>
</div></details>`
    : `<div class="grid2">      <div>
        <h3 class="sec">${ic('key')} Rejoindre un groupe</h3>
        <form class="panel form" id="gJoin"><label class="field">Code d’invitation<input id="gCode" autocomplete="off" maxlength="12" placeholder="Ex. : 4F9A2C" style="text-transform:uppercase"></label>
          <button class="btn primary">Rejoindre</button><span class="small err" id="gJoinErr"></span></form>
        </div><div><h3 class="sec">${ic('plus')} Créer un groupe</h3>
        <form class="panel form" id="gNew"><label class="field">Nom du groupe<input id="gNom" maxlength="60" required placeholder="Ex. : MP* — trinôme du jeudi"></label>
          <label class="field">Description (facultatif)<input id="gDesc" maxlength="300"></label>
          <button class="btn primary">Créer et devenir responsable</button><span class="small err" id="gNewErr"></span></form>
      </div>
</div><div id="gDetail"></div>`}
    <h3 class="sec">${ic('key')} Les rôles</h3>
    <div class="panel roles">
      <div><span class="rolepill responsable">Responsable</span><span>Gère le groupe (nom, code d’invitation), attribue les rôles, exclut des membres, modère. Il en reste toujours au moins un.</span></div>
      <div><span class="rolepill moderateur">Modérateur</span><span>Voit le code d’invitation, supprime les réponses et messages inappropriés, exclut des membres simples.</span></div>
      <div><span class="rolepill membre">Membre</span><span>Soumet ses réponses sur l’honneur, note celles des autres de 0 à 10, participe à la discussion.</span></div>
      <div><span class="rolepill">Administrateur</span><span>Voit et modère tous les groupes de la classe.</span></div>
    </div>`;
  el.querySelectorAll('[data-g]').forEach(b => b.onclick = () => { GV = b.dataset.g; if (gById(GV)?.role) store.set('groupe', GV); renderGroupes(); });
  $('#gJoin').onsubmit = async e => { e.preventDefault(); $('#gJoinErr').textContent = '';
    try { GV = await api.rejoindre($('#gCode').value); store.set('groupe', GV); await loadGroups(); renderGroupes(); } catch (x) { $('#gJoinErr').textContent = x.message; } };
  $('#gNew').onsubmit = async e => { e.preventDefault(); $('#gNewErr').textContent = '';
    const nom = $('#gNom').value.trim(); if (nom.length < 2) { $('#gNewErr').textContent = 'Nom trop court.'; return; }
    try { GV = await api.creerGroupe(nom, $('#gDesc').value.trim()); store.set('groupe', GV); await loadGroups(); renderGroupes(); } catch (x) { $('#gNewErr').textContent = x.message; } };
  if (GV) renderGroupeDetail(GV);
}
async function renderGroupeDetail(gid) {
  const box = $('#gDetail'), g = gById(gid); if (!box || !g) return;
  box.innerHTML = `<div role="status" aria-label="Chargement du groupe" style="display:grid;gap:12px">${SKEL(1, 'skel-h')}${SKEL(2, 'skel-card')}</div>`;
  let membres = [], recent = [];
  try { [membres, recent] = await Promise.all([api.membres(gid), api.recentes(gid)]); MEMB[gid] = membres; } catch (e) { box.innerHTML = `<p class="err">${esc(e.message)}</p>`; return; }
  if (GV !== gid) return;
  const resp = api.isProf || g.role === 'responsable', mod = canMod(gid), me = api.user.id;
  box.innerHTML = `
    <div class="panel gdetail">
      <div class="gd-head"><div><h3>${esc(g.nom)}</h3>${g.description ? `<p class="small">${esc(g.description)}</p>` : ''}</div>
        ${resp ? `<button class="btn ghost" id="gEdit">${ic('pen')} Modifier</button>` : ''}</div>
      ${mod ? `<div class="gcode"><span>Code d’invitation</span><b id="gCodeV">${esc(g.code)}</b>
        <button class="btn ghost" id="gCopy">${ic('link')} Copier</button>${resp ? `<button class="btn ghost" id="gRegen" title="L’ancien code ne fonctionnera plus">Nouveau code</button>` : ''}</div>` : ''}
      <h4>${ic('users')} Membres (${membres.length})</h4>
      <div class="scroll"><table class="stack"><thead><tr><th>Membre</th><th>Rôle</th><th>Arrivée</th><th></th></tr></thead><tbody>
      ${membres.map(m => `<tr><td data-l="Membre"><span class="person">${avatar(m.user_id, m.full_name)}<a class="who" href="#u/${esc(m.user_id === me ? MYUSER || me : m.user_id)}">${esc(m.full_name)}</a>${m.user_id === me ? ' (moi)' : ''}</span></td>
        <td data-l="Rôle">${resp ? `<select data-role="${esc(m.user_id)}" aria-label="Rôle de ${esc(m.full_name)}">${Object.entries(ROLE).map(([k, v]) => `<option value="${k}" ${k === m.role ? 'selected' : ''}>${v}</option>`).join('')}</select>` : `<span class="rolepill ${m.role}">${ROLE[m.role]}</span>`}</td>
        <td data-l="Arrivée">${fmtDate(m.joined_at)}</td>
        <td>${m.user_id !== me && (resp || (mod && m.role === 'membre')) ? `<button class="linkbtn danger" data-kick="${esc(m.user_id)}">Exclure</button>` : ''}</td></tr>`).join('')}
      </tbody></table></div>
      <h4>${ic('clock')} Dernières réponses</h4>
      <div class="glist">${recent.map(r => { const e = byId(r.exercice_id); return `<a class="item" href="#ex-${esc(r.exercice_id)}"><span class="t">${esc(e?.titre || r.exercice_id)}</span>
        <span class="avgpill">${fmtNote(moy(r.notes))}/20</span><span class="m">${esc(nameOf(gid, r.user_id))} · ${ago(r.created_at)}${r.aide_consultee ? ' · aide consultée' : ''}</span></a>`; }).join('') || '<div class="empty">Aucune réponse soumise pour l’instant.</div>'}</div>
      <div class="gactions">${g.role ? `<button class="btn" id="gLeave">${ic('logout')} Quitter le groupe</button>` : ''}${resp ? `<button class="btn danger" id="gDel">${ic('trash')} Supprimer le groupe</button>` : ''}</div>
      <span class="small err" id="gErr"></span>
    </div>`;
  const err = m => { $('#gErr').textContent = m; };
  const reload = async () => { await loadGroups(); renderGroupes(); };
  box.querySelectorAll('[data-role]').forEach(s => s.onchange = async () => { try { await api.definirRole(gid, s.dataset.role, s.value); await reload(); } catch (x) { err(x.message); renderGroupeDetail(gid); } });
  box.querySelectorAll('[data-kick]').forEach(b => b.onclick = async () => { const m = membres.find(x => x.user_id === b.dataset.kick);
    if (!confirm(`Exclure ${m.full_name} du groupe ? Ses réponses restent visibles.`)) return; try { await api.exclure(gid, m.user_id); await reload(); } catch (x) { err(x.message); } });
  $('#gCopy') && ($('#gCopy').onclick = async () => { try { await navigator.clipboard.writeText(g.code); $('#gCopy').innerHTML = `${ic('check')} Copié`; toast('Code du groupe copié dans le presse-papiers.', 'ok'); } catch { err('Copie impossible : note le code à la main.'); } });
  $('#gRegen') && ($('#gRegen').onclick = async () => { if (!confirm('Générer un nouveau code ? L’ancien ne permettra plus de rejoindre le groupe.')) return; try { await api.regenererCode(gid); await reload(); } catch (x) { err(x.message); } });
  $('#gEdit') && ($('#gEdit').onclick = async () => { const nom = prompt('Nom du groupe', g.nom); if (nom == null) return; const desc = prompt('Description', g.description || ''); if (desc == null) return;
    if (nom.trim().length < 2) return err('Nom trop court.'); try { await api.majGroupe(gid, {nom: nom.trim().slice(0, 60), description: desc.trim().slice(0, 300)}); await reload(); } catch (x) { err(x.message); } });
  $('#gLeave') && ($('#gLeave').onclick = async () => { if (!confirm(`Quitter « ${g.nom} » ? Tes réponses y restent visibles.`)) return; try { await api.quitter(gid); GV = null; await reload(); } catch (x) { err(x.message); } });
  $('#gDel') && ($('#gDel').onclick = async () => { if (!confirm(`Supprimer « ${g.nom} » ainsi que toutes ses réponses, notes et discussions ? Action irréversible.`)) return; try { await api.supprimerGroupe(gid); GV = null; await reload(); } catch (x) { err(x.message); } });
}

/* ---------- images ---------- */
async function shrink(file) {
  const url = URL.createObjectURL(file);
  try {
    const img = await new Promise((ok, ko) => { const i = new Image(); i.onload = () => ok(i); i.onerror = ko; i.src = url; });
    const k = Math.min(1, 1568 / Math.max(img.naturalWidth, img.naturalHeight));
    const c = document.createElement('canvas'); c.width = Math.round(img.naturalWidth * k); c.height = Math.round(img.naturalHeight * k);
    const g = c.getContext('2d'); g.fillStyle = '#fff'; g.fillRect(0, 0, c.width, c.height); g.drawImage(img, 0, 0, c.width, c.height);
    const data = c.toDataURL('image/jpeg', 0.85);
    return {data, url: data};
  } finally { URL.revokeObjectURL(url); }
}
async function addFiles(id, files) {
  const S = sess(id);
  for (const f of [...files].filter(f => f.type.startsWith('image/')).slice(0, 4 - S.imgs.length)) {
    try { S.imgs.push(await shrink(f)); } catch { notice('Une image n’a pas pu être lue.'); }
  }
  presence({st: 'redige'}); renderRep(byId(id));
}

/* ---------- IA ---------- */
async function ask(ex, mode) {
  const S = sess(ex.id), K = CORR[ex.id] || await loadCorr(ex.id);
  if (K && mode === 'indice') {            // indices préparés : instantanés, sans IA
    if (S.hint >= 3) return;
    const t = {kind: 'indice', n: 0, hint: S.hint + 1, verdict: 'bloque', score: null, resume: '', retour: '', indice: K.indices[S.hint], question: '', points: []};
    S.hint++; S.tours.push(t); renderCopy();
    presence({st: 'indice'});
    await record(ex, t);
    api.activity({uid: api.user.id, name: api.profile.full_name, id: ex.id, k: 'indice', v: 'bloque', sc: null});
    return;
  }
  if (K && mode === 'solution') {          // corrigé préparé
    S.solution = K.corrige; S.reponse = K.reponse; renderCopy();
    presence({st: 'corrige'});
    await record(ex, {kind: 'solution'});
    return;
  }
  S.busy = mode; renderCopy(); notice('');
  presence({st: mode === 'indice' ? 'indice' : 'corrige'});
  try {
    const hist = S.tours.map(t => `- ${t.kind === 'copie' ? 'Copie ' + t.n : 'Indice'} : ${t.verdict}. ${t.retour || ''} ${t.indice ? 'Indice : ' + t.indice : ''}`).join('\n');
    const r = await api.ia({mode, exercice: {titre: ex.titre, mat: ex.mat, chap: ex.chap, niveau: ex.niveau, enonce: ex.enonce},
      images: [], note: '', hint: Math.min(S.hint + 1, 2), historique: hist,
      reference: K ? `${K.corrige}\n\nRÉSULTAT ATTENDU : ${K.reponse}` : '', indices: K ? K.indices : []});
    if (mode === 'solution') {
      const arr = v => Array.isArray(v) ? v.slice(0, 5).map(String) : [];
      S.solution = String(r.corrige || ''); S.reponse = String(r.reponse || ''); S.theoremes = arr(r.theoremes); S.astuces = arr(r.astuces);
      S.relu = !!r.relu; S.verif = r.verification && typeof r.verification === 'object' ? {statut: String(r.verification.statut || ''), remarques: arr(r.verification.remarques)} : null;
      S.openC = true; S.seen = true; await record(ex, {kind: 'solution'});
    }
    else {
      const t = {kind: mode, n: 0, hint: r.indice ? Math.min(S.hint + 1, 2) : 0, verdict: 'bloque',
        score: r.score != null && Number.isFinite(+r.score) ? Math.max(0, Math.min(100, Math.round(+r.score))) : null,
        resume: String(r.resume || ''), retour: String(r.retour || ''), indice: String(r.indice || ''), question: String(r.question || ''),
        points: Array.isArray(r.points) ? r.points.slice(0, 8).map(p => ({etape: String(p.etape || ''), statut: ['ok', 'erreur', 'manquant'].includes(p.statut) ? p.statut : 'manquant', note: String(p.note || '')})) : []};
      if (t.indice) S.hint = Math.min(S.hint + 1, 2);
      S.tours.push(t);
      await record(ex, t);
      presence({st: 'redige'});
      api.activity({uid: api.user.id, name: api.profile.full_name, id: ex.id, k: t.kind, v: t.verdict, sc: t.score});
    }
  } catch (e) { notice(esc(e.message || 'Erreur')); }
  finally { S.busy = false; renderCopy(); }
}

/* ---------- suivi ---------- */
async function record(ex, t) {
  SUIVI.ex ||= {}; SUIVI.journal ||= []; SUIVI.cree ||= now();
  const st = SUIVI.ex[ex.id] ||= {s: 'en_cours', e: 0, i: 0, sc: 0, d: 0, t: 0};
  api.track(ex.id, {indice: 'indice', solution: 'corrige', reponse: 'reponse'}[t.kind] || 'vu');
  if (t.kind === 'reponse') st.e++;
  if (t.kind === 'indice') st.i++;
  if (t.kind === 'solution') st.vu = 1;
  st.d = now(); st.t = Math.round((now() - sess(ex.id).start) / 1000);
  SUIVI.journal = [{d: now(), id: ex.id, k: t.kind, v: t.verdict || '', sc: t.score ?? null}].concat(SUIVI.journal).slice(0, 60);
  await api.saveSuivi(SUIVI);
  renderList(); renderStrip();
}

/* ================= MON SUIVI ================= */
function chapStats(lvl, src) {
  const m = {};
  for (const e of all().filter(e => e.niveau === lvl)) { const k = e.mat + ' · ' + e.chap; const o = m[k] ||= {k, mat: e.mat, chap: e.chap, tot: 0, ok: 0, go: 0}; o.tot++; const s = src?.ex?.[e.id]?.s; if (s === 'reussi') o.ok++; else if (s) o.go++; }
  return Object.values(m).sort((a, b) => (b.ok + b.go) / b.tot - (a.ok + a.go) / a.tot || a.k.localeCompare(b.k, 'fr'));
}
const bars = rows => rows.map(r => `<div class="bar"><span>${ic(chapIcon(r.mat, r.chap))} ${esc(r.k)}</span><span class="tr" role="img" aria-label="${r.ok} réussis, ${r.go} en cours sur ${r.tot}"><i style="width:${100 * r.ok / r.tot}%;background:var(--green)"></i><i style="width:${100 * r.go / r.tot}%;background:var(--amber)"></i></span><span class="num">${r.ok}/${r.tot}</span></div>`).join('');
function recommend(src, lvl) {
  const sel = (CONF.sel?.[lvl] || []).filter(id => src?.ex?.[id]?.s !== 'reussi');
  const going = Object.entries(src?.ex || {}).filter(([id, v]) => v.s !== 'reussi' && byId(id)?.niveau === lvl).sort((a, b) => b[1].d - a[1].d).map(([id]) => id);
  const fresh = [];
  for (const r of chapStats(lvl, src).sort((a, b) => a.ok / a.tot - b.ok / b.tot)) { const e = all().find(e => e.niveau === lvl && e.mat === r.mat && e.chap === r.chap && !src?.ex?.[e.id]); if (e) fresh.push(e.id); if (fresh.length >= 4) break; }
  return [...new Set([...sel, ...going, ...fresh])].slice(0, 6).map(byId).filter(Boolean);
}
/* ---------- espace personnel : données réelles uniquement ---------- */
const dayKey = t => { const d = new Date(t); return d.getFullYear() * 10000 + (d.getMonth() + 1) * 100 + d.getDate(); };
function activityDays(src) {
  const days = new Map();
  for (const j of src.journal || []) if (j.d) days.set(dayKey(j.d), (days.get(dayKey(j.d)) || 0) + 1);
  for (const v of Object.values(src.ex || {})) if (v.d && !days.has(dayKey(v.d))) days.set(dayKey(v.d), 1);
  return days;
}
function streakOf(days) {
  let n = 0; const d = new Date(); d.setHours(12);
  if (!days.has(dayKey(d))) d.setDate(d.getDate() - 1);   // la série tient encore si on a travaillé hier
  while (days.has(dayKey(d))) { n++; d.setDate(d.getDate() - 1); }
  return n;
}
function dailyPick(lvl, src) {
  const pool = all().filter(e => e.niveau === lvl && src.ex?.[e.id]?.s !== 'reussi');
  if (!pool.length) return null;
  const k = dayKey(now()); let h = 0; for (const c of String(k)) h = (h * 31 + c.charCodeAt(0)) >>> 0;
  return pool[h % pool.length];
}
function calHTML(days) {
  const end = new Date(); end.setHours(12); const start = new Date(end); start.setDate(end.getDate() - 7 * 12 + 1 - ((end.getDay() + 6) % 7));
  const cells = []; for (const d = new Date(start); d <= end; d.setDate(d.getDate() + 1)) { const n = days.get(dayKey(d)) || 0;
    cells.push(`<i class="h${n ? Math.min(3, n) : 0}" title="${d.toLocaleDateString('fr-FR', {weekday: 'short', day: 'numeric', month: 'short'})} : ${n ? n + ' action' + (n > 1 ? 's' : '') : 'rien'}"></i>`); }
  return `<div class="cal" role="img" aria-label="Activité des 12 dernières semaines : ${[...days.values()].length} jours travaillés">${cells.join('')}</div>`;
}
const streakHTML = (streak, week) => `<span class="k">Série en cours</span><b class="num">${streak}</b><span class="small">jour${streak > 1 ? 's' : ''} de travail consécutif${streak > 1 ? 's' : ''} · ${week}/7 cette semaine</span>`;
const calBoxHTML = days => `<span class="k">Douze semaines de travail</span>${calHTML(days)}<span class="small">${days.size} jour${days.size > 1 ? 's' : ''} actif${days.size > 1 ? 's' : ''} enregistré${days.size > 1 ? 's' : ''}</span>`;
function bentoHTML(lvl) {
  const s = SUIVI, days = activityDays(s), streak = streakOf(days), first = (api.profile.full_name || '').split(' ')[0];
  const recent = [...new Set((s.journal || []).map(j => j.id))].map(byId).filter(Boolean).slice(0, 4);
  const last = recent[0], pick = dailyPick(lvl, s);
  const week = [...days.keys()].filter(k => k >= dayKey(now() - 6 * 864e5)).length;
  const mot = streak >= 5 ? `${streak} jours d’affilée : c’est cette régularité qui paie en mai.` : streak >= 2 ? 'Belle série. Un exercice ce soir, même court, la prolonge.'
    : days.size ? 'Une colle de quinze minutes suffit pour relancer la machine.' : 'Commence par un exercice CCINP : vingt minutes, un énoncé court, et c’est parti.';
  return `<div class="bento">
    <section class="bx bx-hi"><p class="hand">${new Date().getHours() >= 18 || new Date().getHours() < 5 ? 'Bonsoir' : 'Bonjour'} ${esc(first)}</p><h3>${last ? 'On reprend où tu t’étais arrêté ?' : 'Prêt pour ta première colle ?'}</h3>
      <p class="small">${mot}</p>
      ${last ? `<button class="btn primary" data-open="${esc(last.id)}">${ic('arrow')} Reprendre : ${esc(last.titre)}</button>` : `<a class="btn primary" href="#exercices">${ic('arrow')} Choisir un exercice</a>`}</section>
    <section class="bx bx-streak" id="bxStreak">${streakHTML(streak, week)}</section>
    <section class="bx bx-day"><span class="k">Exercice du jour</span>${pick ? `<h3>${esc(pick.titre)}</h3><span class="small">${esc(pick.chap)} · ${LV[pick.niveau]} · ${pick.duree} min</span><button class="btn" data-open="${esc(pick.id)}">Le tenter</button>` : '<p class="small">Tout est réussi à ce niveau. Passe au niveau supérieur !</p>'}</section>
    <section class="bx bx-cal" id="bxCal">${calBoxHTML(days)}</section>
    <section class="bx bx-lvl" id="bxLvl"><span class="k">Progression</span><span class="skel skel-l w60"></span><span class="skel skel-l"></span></section>
    <section class="bx bx-goal" id="bxGoal"><span class="k">Objectif en cours</span><p class="small">Chargement…</p></section>
    <section class="bx bx-recent"><span class="k">Derniers exercices</span>${recent.length ? `<ul>${recent.map(e => `<li><button class="linkbtn" data-open="${esc(e.id)}">${esc(e.titre)}</button><span class="small">${esc(e.chap)}</span></li>`).join('')}</ul>` : '<p class="small">Rien pour l’instant : ton historique apparaîtra ici.</p>'}</section>
  </div>`;
}
async function fillNiveau() {
  const b = $('#bxLvl'); if (!b) return;
  let p = null; try { p = await api.profilPublic(MYUSER || api.user.id, false); } catch {}
  if (!$('#bxLvl')) return;
  if (!p || p.prive) { b.innerHTML = '<span class="k">Progression</span><p class="small">Indisponible pour le moment.</p>'; return; }
  const S = statsProfil(p);
  b.innerHTML = `<span class="k">Progression</span>${niveauHTML(S, {self: true, compact: true})}<a class="ul small" href="#u/${esc(p.username || '')}">Détail et jalons sur ton profil ${ic('arrow')}</a>`;
  const r = $('#rythme'); if (r) r.innerHTML = rythmeHTML(p.jours || []);
  // le serveur connaît toute l'activité (tous appareils) : on complète la série et la carte des 12 semaines
  if (p.jours?.length) {
    const days = activityDays(SUIVI);
    for (const j of p.jours) { const [y, m, d] = j.j.split('-').map(Number), k = y * 10000 + m * 100 + d; days.set(k, Math.max(days.get(k) || 0, (j.ids || []).length || 1)); }
    const week = [...days.keys()].filter(k => k >= dayKey(now() - 6 * 864e5)).length;
    $('#bxCal') && ($('#bxCal').innerHTML = calBoxHTML(days));
    $('#bxStreak') && ($('#bxStreak').innerHTML = streakHTML(streakOf(days), week));
  }
}
// Rythme : exercices distincts travaillés par semaine (12 dernières semaines) et par mois (6 derniers mois)
function rythmeHTML(jours) {
  const map = new Map(jours.map(j => [j.j, j.ids || []]));
  const ymd = d => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
  const today = new Date(); today.setHours(12);
  const monday = new Date(today); monday.setDate(today.getDate() - ((today.getDay() + 6) % 7));
  const weeks = []; for (let w = 11; w >= 0; w--) { const s0 = new Date(monday); s0.setDate(monday.getDate() - 7 * w); const ids = new Set();
    for (let k = 0; k < 7; k++) { const d = new Date(s0); d.setDate(s0.getDate() + k); (map.get(ymd(d)) || []).forEach(i => ids.add(i)); }
    weeks.push({lab: s0.toLocaleDateString('fr-FR', {day: 'numeric', month: 'short'}), n: ids.size}); }
  const months = []; for (let m = 5; m >= 0; m--) { const d0 = new Date(today.getFullYear(), today.getMonth() - m, 1), ids = new Set(), pre = ymd(d0).slice(0, 7);
    for (const [k, v] of map) if (k.startsWith(pre)) v.forEach(i => ids.add(i));
    months.push({lab: d0.toLocaleDateString('fr-FR', {month: 'short'}), n: ids.size}); }
  const bars = (L, cls) => { const mx = Math.max(1, ...L.map(x => x.n));
    return `<div class="ry ${cls}" role="img" aria-label="${L.map(x => `${x.lab} : ${x.n}`).join(', ')}">${L.map((x, i) => `<div class="ry-c"><span class="ry-v">${x.n || ''}</span><i style="--h:${(100 * x.n / mx).toFixed(0)}%;--d:${i * 30}ms"></i><span class="ry-l">${x.lab}</span></div>`).join('')}</div>`; };
  const tot = weeks.reduce((a, x) => a + x.n, 0);
  if (!tot && !months.some(x => x.n)) return `<p class="small">Ton rythme apparaîtra ici dès que tu auras travaillé un exercice (indice demandé ou réponse soumise).</p>`;
  return `<div class="ry-grid"><div><h4>Par semaine <span class="small">exercices distincts travaillés</span></h4>${bars(weeks, 'w')}</div><div><h4>Par mois</h4>${bars(months, 'm')}</div></div>`;
}
async function fillGoal() {
  const b = $('#bxGoal'); if (!b) return;
  let L = []; try { L = (await api.mesObjectifs()).filter(o => !o.archive); } catch {}
  const o = L.sort((a, b) => String(a.fin).localeCompare(String(b.fin)))[0];
  if (!$('#bxGoal')) return;
  b.innerHTML = o ? `<span class="k">Objectif en cours</span><h3>${esc(o.titre)}</h3><div class="gbar"><i style="--p:${Math.min(100, Math.round(100 * (o.progression || 0) / o.cible))}%"></i></div><span class="small">${Math.min(o.progression || 0, o.cible)} / ${o.cible} · jusqu’au ${new Date(o.fin).toLocaleDateString('fr-FR', {day: 'numeric', month: 'long'})}</span>`
    : `<span class="k">Objectif en cours</span><p class="small">Aucun objectif. Un objectif précis aide plus qu’une bonne résolution.</p><a class="btn" href="#carnet">Fixer un objectif</a>`;
}
function renderSuivi() {
  const s = SUIVI, lvl = api.profile.niveau || 1;
  const exs = Object.values(s.ex || {}), atL = all().filter(e => e.niveau === lvl);
  const ok = atL.filter(e => s.ex?.[e.id]?.s === 'reussi').length;
  const tot = (k) => exs.reduce((a, v) => a + (v[k] || 0), 0);
  const rec = recommend(s, lvl);
  $('#v-suivi').innerHTML = `
    <div class="pagehead"><h2>Mon suivi</h2><span class="small">${DEMO ? 'mode démonstration' : 'enregistré sur ton compte'}</span></div>
    ${bentoHTML(lvl)}
    <h3 class="sec">${ic('target')} Défis</h3><div class="panel defis-p" id="defisP">${defisHTML(lesDefis())}</div>
    <h3 class="sec">${ic('chart')} Mon rythme</h3><div class="panel rythme" id="rythme"><span class="skel skel-l"></span><span class="skel skel-l w60"></span></div>
    <div class="panel profile"><span class="ph">${avatar(api.user.id, api.profile.full_name)}</span>
      <div><b>${esc(api.profile.full_name || 'Moi')}</b><span class="small">${esc(api.user.email || '')}</span></div>
      <div class="pbtns"><button class="btn" id="phChange">${ic('camera')} ${SUIVI.photo ? 'Changer la photo' : 'Ajouter une photo'}</button>${SUIVI.photo ? `<button class="btn ghost" id="phDel">${ic('trash')} Retirer</button>` : ''}<a class="btn" href="#profil">${ic('user')} Mon profil</a></div></div>
    <div class="lvl" id="lvlPick">${[1, 2, 3].map(n => `<button data-n="${n}" aria-pressed="${n === lvl}"><b>${LV[n]}</b><span>${esc(LVD[n])}</span></button>`).join('')}</div>
    <div class="hero">
      <div class="panel stat" style="padding:24px"><div class="k">${ic('trophy')} Exercices réussis — ${LV[lvl]}</div>
        <div class="big">${ok}<span style="font-size:.42em;color:var(--soft)"> / ${atL.length}</span></div>
        <div class="bar" style="grid-template-columns:minmax(0,1fr);margin-top:10px"><span class="tr"><i style="width:${atL.length ? 100 * ok / atL.length : 0}%;background:var(--green)"></i></span></div></div>
      <div class="stats">
        <div class="panel stat"><div class="k">${ic('pen')} Réponses soumises</div><div class="v">${MES.length}</div></div>
        <div class="panel stat"><div class="k">${ic('star')} Note moyenne reçue</div><div class="v">${fmtNote(moy(MES.flatMap(r => r.notes || [])))}<span style="font-size:.5em"> /20</span></div></div>
        <div class="panel stat"><div class="k">${ic('bulb')} Indices demandés</div><div class="v">${tot('i')}</div></div>
        <div class="panel stat"><div class="k">${ic('clock')} Temps de travail</div><div class="v">${Math.round(tot('t') / 60)}<span style="font-size:.5em"> min</span></div></div>
        <div class="panel stat"><div class="k">${ic('target')} Exercices commencés</div><div class="v">${exs.length}</div></div>
      </div>
    </div>
    <div class="grid2">
      <div><h3 class="sec">${ic('chart')} Par chapitre</h3><div class="panel bars">${bars(chapStats(lvl, s))}</div>
        <p class="small"><span style="color:var(--green)">■</span> réussi · <span style="color:var(--amber)">■</span> en cours</p></div>
      <div><h3 class="sec">${ic('target')} À travailler ensuite</h3><div class="panel" style="padding:8px">${rec.map(e => `<button class="item" data-open="${esc(e.id)}"><span class="tile ${e.mat}">${ic(chapIcon(e.mat, e.chap))}</span><span class="t">${(CONF.sel?.[lvl] || []).includes(e.id) ? '★ ' : ''}${esc(e.titre)}</span><span></span><span class="m">${esc(e.chap)} · ${e.duree} min</span></button>`).join('') || '<div class="empty">Tout est réussi à ce niveau : passe au suivant !</div>'}</div></div>
    </div>
    <h3 class="sec">${ic('heart')} Mes exercices enregistrés</h3>
    <div class="panel" style="padding:8px">${favs().map(byId).filter(Boolean).map(e => `<button class="item" data-open="${esc(e.id)}"><span class="tile ${e.mat}">${ic(chapIcon(e.mat, e.chap))}</span><span class="t">${esc(e.titre)}</span><span></span><span class="m">${LV[e.niveau]} · ${esc(e.chap)} · ${e.duree} min</span></button>`).join('') || `<div class="empty">Aucun exercice enregistré. Appuie sur ${ic('heart')} dans un exercice pour le retrouver ici.</div>`}</div>
    <h3 class="sec">${ic('clock')} Historique</h3>
    <div class="panel scroll"><table class="stack"><thead><tr><th>Date</th><th>Exercice</th><th>Action</th><th class="r">Note</th></tr></thead><tbody>
    ${(s.journal || []).map(j => `<tr><td>${fmtDate(j.d)}</td><td>${esc(byId(j.id)?.titre || j.id)}</td><td>${j.k === 'reponse' ? 'Réponse soumise sur l’honneur' : j.k === 'copie' ? 'Copie : ' + esc({juste: 'juste', partiel: 'partielle', faux: 'erreur', illisible: 'illisible'}[j.v] || j.v) : j.k === 'indice' ? 'Indice' : 'Corrigé consulté'}</td><td class="r">${j.k === 'reponse' ? (() => { const r = mine(j.id); const m = r && moy(r.notes); return m != null ? fmtNote(m) + '/20' : ''; })() : j.sc != null ? j.sc + ' %' : ''}</td></tr>`).join('') || '<tr><td colspan="4" class="empty">Pas encore d’activité.</td></tr>'}
    </tbody></table></div>
    <a class="panel cta" href="#envoyer">${ic('upload')}<span><b>Tu as passé un oral ?</b><span class="small">Envoie ton sujet en PDF pour enrichir la plateforme.</span></span></a>`;
  $('#phChange').onclick = pickPhoto;
  if ($('#phDel')) $('#phDel').onclick = () => setPhoto('');
  $('#lvlPick').onclick = async e => { const b = e.target.closest('button'); if (!b) return; F.lvl = +b.dataset.n; await api.setMyLevel(F.lvl); renderSuivi(); };
  document.querySelectorAll('#v-suivi [data-open]').forEach(b => b.onclick = () => { location.hash = 'ex-' + b.dataset.open; });
  fillGoal(); fillNiveau();
}

/* ================= TABLEAU DE BORD ================= */
let built = false;
function renderProf(full) {
  if (!api.isProf) return;
  if (!built || full) { buildProf(); renderModeration($('#pMod')); }
  updateProf();
}
function buildProf() {
  built = true;
  $('#v-prof').innerHTML = `
    <div class="pagehead"><h2>Tableau de bord</h2><span class="small">${esc(CONFIG.NOM_PROF)} · ${new Date().toLocaleDateString('fr-FR', {weekday: 'long', day: 'numeric', month: 'long'})}</span></div>
    <div class="stats" id="pStats"></div>
    <h3 class="sec">${ic('key')} Modération <span class="small">signalements en attente</span></h3><div class="panel" style="padding:12px 16px" id="pMod"></div>
    <h3 class="sec">${ic('live')} En direct</h3><div class="live" id="pLive"></div>
    <div class="grid2">
      <div><h3 class="sec">${ic('users')} Élèves</h3>
        <div class="panel scroll"><table class="stack"><thead><tr><th>Élève</th><th>Niveau</th><th class="r">Réussis</th><th class="r">Réponses</th><th class="r">Indices</th><th>À revoir</th><th>Dernière activité</th></tr></thead><tbody id="pRows"></tbody></table></div></div>
      <div><h3 class="sec">${ic('msg')} Fil d’activité</h3><ul class="stream" id="pStream"></ul></div>
    </div>
    <div class="grid2">
      <div><h3 class="sec">${ic('star')} Message et sélection pour la classe</h3><div class="panel form" id="pConf"></div></div>
      <div><h3 class="sec">${ic('plus')} Ajouter un exercice</h3>
        <div class="panel form">
          ${CONFIG.IA ? `<label class="btn" style="justify-self:start;cursor:pointer;position:relative"><input type="file" id="impFile" accept="image/*" class="sr">${ic('camera')} Importer depuis une photo d’énoncé</label>
          <span class="small" id="impSt">L’IA retranscrit l’énoncé en LaTeX ; relis avant d’enregistrer.</span>` : ''}
          <div class="row"><label class="field">Titre<input id="aT"></label><label class="field">Matière<select id="aM"><option>Maths</option><option>Physique</option><option>Chimie</option><option>Informatique</option></select></label></div>
          <div class="row"><label class="field">Chapitre<input id="aC"></label><label class="field">Niveau<select id="aN"><option value="1">CCINP</option><option value="2">Mines-Centrale</option><option value="3">X-ENS</option></select></label><label class="field">Durée (min)<input id="aD" type="number" value="20" min="5" max="60"></label></div>
          <label class="field">Énoncé (formules en LaTeX entre $…$)<textarea id="aE"></textarea></label>
          <button class="btn primary" id="aSave">${ic('plus')} Ajouter à la banque</button><span class="small" id="aOk"></span>
        </div>
        <div id="pBank"></div>
      </div>
    </div>
    <h3 class="sec">${ic('key')} Code d’inscription de la classe</h3>
    <div class="panel form"><div class="row" style="align-items:end"><label class="field">Code à donner aux élèves<input id="cCode" autocomplete="off"></label><button class="btn" id="cCodeSave" style="flex:0 0 auto">Changer le code</button></div><span class="small" id="cCodeOk">Seuls les élèves qui ont ce code peuvent créer un compte.</span></div>`;
  $('#pRows').onclick = e => { const tr = e.target.closest('[data-st]'); if (tr) studentDialog(tr.dataset.st); };
  $('#pRows').onkeydown = e => { const tr = e.target.closest('[data-st]'); if (tr && e.key === 'Enter') studentDialog(tr.dataset.st); };
  $('#aSave').onclick = addExercise;
  $('#impFile') && ($('#impFile').onchange = e => importPhoto(e.target.files[0]));
  $('#pBank').onclick = async e => { const b = e.target.closest('[data-del]'); if (!b) return; b.disabled = true; try { await api.delBanque(b.dataset.del); BANK = await api.banque(); updateProf(); } catch { b.disabled = false; } };
  api.getCode().then(c => { $('#cCode').value = c; });
  $('#cCodeSave').onclick = async () => { const c = $('#cCode').value.trim(); if (c.length < 4) { $('#cCodeOk').textContent = '4 caractères minimum.'; return; } try { await api.setCode(c); $('#cCodeOk').textContent = 'Nouveau code enregistré.'; } catch { $('#cCodeOk').textContent = 'Échec.'; } };
  buildConfig();
}
function buildConfig() {
  $('#pConf').innerHTML = `
    <label class="field">Message affiché aux élèves (bandeau du tableau)<textarea id="cMsg" style="min-height:70px;font-family:inherit;font-size:16px">${esc(CONF.message || '')}</textarea></label>
    ${[1, 2, 3].map(n => `<label class="field">Sélection ${LV[n]} — Ctrl/⌘ pour en choisir plusieurs<select multiple size="5" data-sel="${n}">${all().filter(e => e.niveau === n).map(e => `<option value="${esc(e.id)}" ${(CONF.sel?.[n] || []).includes(e.id) ? 'selected' : ''}>${esc(e.mat + ' · ' + e.titre)}</option>`).join('')}</select></label>`).join('')}
    <button class="btn primary" id="cSave">${ic('check')} Enregistrer pour la classe</button><span class="small" id="cOk"></span>`;
  $('#cSave').onclick = async () => {
    const sel = {}; document.querySelectorAll('#pConf [data-sel]').forEach(s => sel[s.dataset.sel] = [...s.selectedOptions].map(o => o.value).slice(0, 20));
    try { await api.saveConfig({message: $('#cMsg').value.trim().slice(0, 500), sel}); CONF = await api.config(); $('#cOk').textContent = 'Enregistré : les élèves le voient tout de suite.'; } catch { $('#cOk').textContent = 'Échec de l’enregistrement.'; }
  };
}
function livePeople() {
  return Object.entries(PRES).map(([uid, metas]) => ({uid, ...(metas[metas.length - 1] || {})}));
}
function doing(p) {
  const st = {lit: 'lit l’énoncé', redige: 'rédige', soumis: 'a soumis sa réponse', correction: 'attend la correction', indice: 'demande un indice', corrige: 'lit le corrigé', reussi: 'a réussi'}[p.st] || '';
  if (p.v === 'suivi') return 'consulte son suivi';
  if (p.v === 'prof') return 'tableau de bord';
  if (p.ex) return `${st ? st + ' — ' : ''}<b>${esc(p.t || p.ex)}</b> <span class="stamp n${p.n || 1}" style="font-size:10px">${LV[p.n] || ''}</span>`;
  return 'parcourt les exercices';
}
function updateProf() {
  if (!$('#pStats')) return;
  const people = livePeople();
  const students = CLASS.filter(c => c.id !== api.user.id);
  const today = new Date(); today.setHours(0, 0, 0, 0);
  let triesToday = 0, okToday = 0;
  for (const s of students) for (const j of s.data?.journal || []) if (j.d >= +today && (j.k === 'reponse' || j.k === 'copie')) triesToday++;
  okToday = GROUPS.length;
  $('#pStats').innerHTML = `
    <div class="panel stat"><div class="k">${ic('live')} Connectés maintenant</div><div class="v">${people.length}</div></div>
    <div class="panel stat"><div class="k">${ic('users')} Élèves inscrits</div><div class="v">${students.length}</div></div>
    <div class="panel stat"><div class="k">${ic('pen')} Réponses soumises aujourd’hui</div><div class="v">${triesToday}</div></div>
    <div class="panel stat"><div class="k">${ic('users')} Groupes</div><div class="v">${okToday}</div></div>`;
  $('#pLive').innerHTML = DEMO ? '<div class="empty">Le temps réel fonctionne une fois Supabase configuré.</div>' : people.map(p => `<div class="panel lc">
      <div class="person">${avatar(p.uid, p.name)}<b>${esc(p.name || 'Élève')}</b>${p.uid === api.user.id ? '<span class="small">(vous)</span>' : ''}${p.role === 'prof' ? '<span class="small">admin</span>' : ''}</div>
      <div class="doing">${doing(p)}</div><div class="since">${ic('clock')} depuis ${mmss((now() - (p.since || now())) / 1000)}</div></div>`).join('') || '<div class="empty">Personne en ligne pour l’instant.</div>';
  const rows = students.map(c => {
    const v = Object.values(c.data?.ex || {});
    const weak = chapStats(c.niveau || 1, c.data).filter(r => r.go > 0).sort((a, b) => b.go - a.go)[0];
    return {c, ok: v.filter(x => x.s === 'reussi').length, tried: v.length, e: v.reduce((a, x) => a + (x.e || 0), 0), i: v.reduce((a, x) => a + (x.i || 0), 0), weak: weak?.k || '—', last: c.data?.journal?.[0]?.d || c.last_seen};
  }).sort((a, b) => new Date(b.last || 0) - new Date(a.last || 0));
  $('#pRows').innerHTML = rows.map(r => `<tr class="click" data-st="${esc(r.c.id)}" tabindex="0"><td><span class="person">${avatar(r.c.id, r.c.full_name)}${esc(r.c.full_name || 'Élève')}${PRES[r.c.id] ? ' <span class="dot on" title="en ligne"></span>' : ''}</span></td><td>${LV[r.c.niveau] || '—'}</td><td class="r">${r.ok}/${r.tried}</td><td class="r">${r.e}</td><td class="r">${r.i}</td><td>${esc(r.weak)}</td><td>${ago(r.last)}</td></tr>`).join('')
    || '<tr><td colspan="7" class="empty">Aucun élève inscrit. Donne-leur l’adresse du site et le code de la classe.</td></tr>';
  const fromDb = [];
  for (const s of students) for (const j of (s.data?.journal || []).slice(0, 8)) fromDb.push({d: j.d, uid: s.id, name: s.full_name, id: j.id, k: j.k, v: j.v, sc: j.sc});
  const seen = new Set(), items = [];
  for (const it of LIVE.concat(fromDb).sort((a, b) => b.d - a.d)) { const key = it.uid + it.id + it.k + Math.round(it.d / 8000); if (seen.has(key)) continue; seen.add(key); items.push(it); if (items.length >= 30) break; }
  $('#pStream').innerHTML = items.map(it => `<li>${ic(it.k === 'reponse' ? 'users' : it.k === 'copie' ? (it.v === 'juste' ? 'trophy' : 'pen') : it.k === 'indice' ? 'bulb' : 'eye')}<span><b>${esc(it.name || 'Élève')}</b> · ${it.k === 'reponse' ? 'réponse soumise sur l’honneur' : it.k === 'copie' ? 'copie ' + esc({juste: 'juste', partiel: 'partielle', faux: 'avec erreur', illisible: 'illisible'}[it.v] || it.v) : it.k === 'indice' ? 'indice demandé' : 'corrigé consulté'} — ${esc(byId(it.id)?.titre || it.id)} <span class="small">${ago(it.d)}</span></span></li>`).join('') || '<li class="small">Rien pour l’instant.</li>';
  $('#pBank').innerHTML = BANK.length ? `<h3 class="sec">Exercices ajoutés</h3><div class="panel" style="padding:8px">${BANK.map(e => `<div class="row" style="align-items:center;padding:6px"><span style="flex:3 1 200px"><b>${esc(e.titre)}</b> <span class="small">${LV[e.niveau]} · ${esc(e.chap)}</span></span><button class="btn" data-del="${esc(e.id)}" style="flex:0 0 auto">${ic('trash')} Supprimer</button></div>`).join('')}</div>` : '';
}
function studentDialog(id) {
  const c = CLASS.find(x => x.id === id); if (!c) return;
  const lvl = c.niveau || 1, d = c.data || {};
  $('#dlgT').innerHTML = `<span class="person">${avatar(c.id, c.full_name)}${esc(c.full_name || 'Élève')}</span>`;
  $('#dlgB').innerHTML = `
    <div class="row" style="align-items:end"><label class="field">Niveau de l’élève<select id="dLvl">${[1, 2, 3].map(n => `<option value="${n}" ${n === lvl ? 'selected' : ''}>${LV[n]}</option>`).join('')}</select></label><span class="small">Inscrit ${fmtDate(c.created_at)} · vu ${ago(c.last_seen)}</span></div>
    <h3 class="sec" style="font-size:20px">Chapitres (${LV[lvl]})</h3><div class="bars" style="padding:0">${bars(chapStats(lvl, d))}</div>
    <h3 class="sec" style="font-size:20px">Exercices travaillés</h3>
    <div class="scroll"><table class="stack"><thead><tr><th>Exercice</th><th>Statut</th><th class="r">Réponses</th><th class="r">Indices</th><th class="r">Note</th><th>Date</th></tr></thead><tbody>
    ${Object.entries(d.ex || {}).sort((a, b) => b[1].d - a[1].d).map(([eid, v]) => `<tr><td>${esc(byId(eid)?.titre || eid)}</td><td>${v.s === 'reussi' ? '✓ réussi' : 'en cours'}${v.vu ? ' · corrigé vu' : ''}</td><td class="r">${v.e || 0}</td><td class="r">${v.i || 0}</td><td class="r">${v.sc ? fmtNote(v.sc / 5) + '/20' : '—'}</td><td>${fmtDate(v.d)}</td></tr>`).join('') || '<tr><td colspan="6" class="empty">Rien encore.</td></tr>'}
    </tbody></table></div>`;
  $('#dLvl').onchange = async e => { try { await api.setLevel(id, +e.target.value); c.niveau = +e.target.value; updateProf(); } catch { notice('Modification impossible.'); } };
  $('#dlg').showModal();
}
$('#dlgX').onclick = () => $('#dlg').close();
async function addExercise() {
  const n = +$('#aN').value;
  const e = {titre: $('#aT').value.trim(), mat: $('#aM').value, chap: $('#aC').value.trim() || 'Divers', niveau: n, duree: Math.max(5, Math.min(60, +$('#aD').value || 20)),
    enonce: $('#aE').value.trim(), source: '', concours: LV[n]};
  if (!e.titre || !e.enonce) { $('#aOk').textContent = 'Titre et énoncé sont requis.'; return; }
  try { await api.addBanque(e); BANK = await api.banque(); $('#aOk').textContent = 'Exercice ajouté.'; ['#aT', '#aC', '#aE'].forEach(s => $(s).value = ''); updateProf(); }
  catch { $('#aOk').textContent = 'Échec de l’ajout.'; }
}
async function importPhoto(file) {
  if (!file) return;
  $('#impSt').innerHTML = '<span class="spin"></span> Lecture de l’énoncé…';
  try {
    const im = await shrink(file);
    const r = await api.ia({mode: 'import', images: [im.data]});
    $('#aT').value = r.titre || ''; $('#aM').value = ['Maths', 'Physique', 'Chimie', 'Informatique'].includes(r.mat) ? r.mat : 'Maths'; $('#aC').value = r.chap || '';
    $('#aN').value = [1, 2, 3].includes(+r.niveau) ? r.niveau : 2; $('#aD').value = r.duree || 20; $('#aE').value = r.enonce || '';
    $('#impSt').textContent = 'Énoncé retranscrit : relis-le puis clique sur « Ajouter ».';
  } catch (e) { $('#impSt').textContent = e.message; }
}

/* ================= LANCEMENT ================= */
(async function boot() {
  try { BASE = await (await fetch('data/exercices.json')).json(); } catch { BASE = []; }
  document.querySelectorAll('[data-nbex]').forEach(e => BASE.length && countUp(e, BASE.length));
  document.querySelectorAll('[data-nbchap]').forEach(e => BASE.length && countUp(e, new Set(BASE.map(x => x.mat + x.chap)).size));
  document.querySelectorAll('[data-nbfig]').forEach(e => countUp(e, Object.keys(FIG).length));
  try { await api.init(); }
  catch { showAuth('in', {alert: navigator.onLine ? 'Connexion au serveur impossible pour le moment. Réessayez dans un instant.' : 'Vous êtes hors connexion : reconnectez-vous à Internet pour accéder à votre compte.'}); return; }
  if (api.linkError === 'email_link') return showAuth('in', {alert: MSG.email_link});
  if (api.linkError) return showAuth('forgot', {alert: MSG[api.linkError]});
  if (api.recovery && api.user) return showAuth('new');
  if (api.user) start(); else showAuth('in');
})();
