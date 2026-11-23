// Colle express — interface
import { CONFIG } from './config.js';
import { api, on, DEMO } from './api.js';
import { ic, chapIcon } from './icons.js';
import { FIG } from './figures.js';
import { esc, rich, fmtEnonce, fmtCorrige } from './format.js';
import { presentationCourte, presentationPage } from './apropos.js';

const $ = s => document.querySelector(s);
const LV = {1: 'CCINP', 2: 'Mines-Centrale', 3: 'X-ENS'};
const LVD = {1: 'Fondamentaux et applications directes du cours', 2: 'Oraux Mines-Ponts et Centrale-Supélec', 3: 'Oraux X-ENS : exercices ouverts'};
const MAT_IC = {Maths: 'sigma', Physique: 'atom', Chimie: 'flask'};
const now = () => Date.now();
const mmss = s => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;
const fmtDate = t => t ? new Date(t).toLocaleString('fr-FR', {day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit'}) : '—';
const ago = t => { if (!t) return '—'; const s = Math.round((now() - new Date(t)) / 1000); if (s < 60) return 'à l’instant'; if (s < 3600) return `il y a ${Math.round(s / 60)} min`; if (s < 86400) return `il y a ${Math.round(s / 3600)} h`; return `il y a ${Math.round(s / 86400)} j`; };
const initials = n => (n || '?').split(/\s+/).filter(Boolean).slice(0, 2).map(w => w[0].toUpperCase()).join('');
const hue = s => { let h = 0; for (const c of String(s)) h = (h * 31 + c.charCodeAt(0)) % 360; return `hsl(${h} 55% 42%)`; };
const avatar = (id, name) => `<span class="avatar" style="background:${hue(id)}">${esc(initials(name))}</span>`;
const store = { get(k, d) { try { const v = localStorage.getItem('ce:' + k); return v ? JSON.parse(v) : d; } catch { return d; } }, set(k, v) { try { localStorage.setItem('ce:' + k, JSON.stringify(v)); } catch {} } };

/* ---------- état ---------- */
let BASE = [], BANK = [], CORR = {};
const all = () => BASE.concat(BANK);
const byId = id => all().find(e => e.id === id);
const F = Object.assign({lvl: 1, mat: '', chap: '', q: ''}, store.get('filters', {}));
let CUR = null, SUIVI = {}, CONF = {message: '', sel: {}}, CLASS = [], PRES = {}, LIVE = [];
const SESS = {};
const notice = h => { $('#notice').innerHTML = h || ''; };

/* ---------- textes fixes ---------- */
document.querySelectorAll('[data-site]').forEach(e => e.textContent = CONFIG.NOM_SITE);
document.querySelectorAll('[data-prof]').forEach(e => e.textContent = CONFIG.NOM_PROF);
$('#aboutMini').innerHTML = presentationCourte();
$('#yr').textContent = new Date().getFullYear();
$('#feat').innerHTML = [['camera', 'Photographie ta copie : correction étape par étape'], ['bulb', 'Des indices gradués, du plus vague au plus précis'], ['chart', 'Ton suivi par chapitre, du CCINP à l’X-ENS']]
  .map(([i, t]) => `<div>${ic(i)}<span>${t}</span></div>`).join('');
$('#searchIc').outerHTML = ic('search');
if (DEMO) $('#demo').hidden = false;

/* ---------- MathJax ---------- */
function typeset(el) {
  if (window.MathJax?.typesetPromise) { MathJax.typesetClear?.([el]); MathJax.typesetPromise([el]).catch(() => {}); }
  else setTimeout(() => typeset(el), 400);
}

/* ================= CONNEXION ================= */
function showAuth(mode = 'in') {
  $('#app').hidden = true; $('#auth').hidden = false;
  $('#fIn').hidden = mode !== 'in'; $('#fUp').hidden = mode !== 'up'; $('#fNew').hidden = mode !== 'new';
  $('#tIn').setAttribute('aria-pressed', mode === 'in'); $('#tUp').setAttribute('aria-pressed', mode === 'up');
  $('.tabs2').hidden = mode === 'new';
  $('#authTitle').textContent = mode === 'new' ? 'Nouveau mot de passe' : mode === 'up' ? 'Créer ton compte' : 'Bienvenue';
}
$('#tIn').onclick = () => showAuth('in');
$('#tUp').onclick = () => showAuth('up');
$('#fIn').onsubmit = async e => {
  e.preventDefault(); $('#inErr').textContent = '';
  const b = e.submitter; b.disabled = true;
  try { await api.signIn($('#inMail').value.trim(), $('#inPass').value); } catch (x) { $('#inErr').textContent = x.message; }
  b.disabled = false;
};
$('#fUp').onsubmit = async e => {
  e.preventDefault(); $('#upErr').textContent = '';
  const b = e.submitter; b.disabled = true;
  try {
    const r = await api.signUp({name: $('#upName').value.trim(), email: $('#upMail').value.trim(), password: $('#upPass').value, code: $('#upCode').value.trim(), niveau: +$('#upLvl').value});
    if (r === 'confirm') { $('#upErr').innerHTML = '<span class="ok">Compte créé ! Ouvre l’e-mail de confirmation reçu, puis connecte-toi.</span>'; }
  } catch (x) { $('#upErr').textContent = x.message; }
  b.disabled = false;
};
$('#forgot').onclick = async () => {
  const m = $('#inMail').value.trim();
  if (!m) { $('#inErr').textContent = 'Saisis d’abord ton adresse e-mail.'; return; }
  try { await api.resetPassword(m); $('#inErr').innerHTML = '<span class="ok">Un lien de réinitialisation t’a été envoyé.</span>'; } catch (x) { $('#inErr').textContent = x.message; }
};
$('#fNew').onsubmit = async e => {
  e.preventDefault();
  try { await api.updatePassword($('#newPass').value); start(); } catch (x) { $('#newErr').textContent = x.message; }
};
on('auth', ev => { if (ev === 'in') start(); else if (ev === 'out') { api.stopLive(); showAuth('in'); } else if (ev === 'recovery') showAuth('new'); });

/* ================= DÉMARRAGE APPLICATION ================= */
let started = false;
async function start() {
  if (!api.user) return showAuth('in');
  $('#auth').hidden = true; $('#app').hidden = false;
  const p = api.profile;
  $('#me').innerHTML = `${avatar(p.id, p.full_name)}<span class="small" style="color:var(--ink);font-weight:600">${esc(p.full_name || 'Moi')}</span><span class="dot" id="conn"></span><button class="btn ghost" id="out" title="Se déconnecter" aria-label="Se déconnecter">${ic('logout')}</button>`;
  $('#out').onclick = () => api.signOut();
  $('#nav').innerHTML = `<a href="#exercices" data-v="exercices">${ic('book')}<span class="lbl">Exercices</span></a><a href="#suivi" data-v="suivi">${ic('chart')}<span class="lbl">Mon suivi</span></a>` +
    (api.isProf ? `<a href="#prof" data-v="prof">${ic('users')}<span class="lbl">Tableau de bord</span> <span class="count-pill" id="liveN">0</span></a>` : '') +
    `<a href="#apropos" data-v="apropos">${ic('cap')}<span class="lbl">À propos</span></a>`;
  $('#bnav').innerHTML = $('#nav').innerHTML;
  if (!store.get('filters', null)) F.lvl = p.niveau || 1;
  [SUIVI, CONF, BANK] = await Promise.all([api.loadSuivi(), api.config(), api.banque()]);
  SUIVI = SUIVI && typeof SUIVI === 'object' ? SUIVI : {};
  if (!started) {
    started = true;
    on('config', async () => { CONF = await api.config(); rerender(); });
    on('banque', async () => { BANK = await api.banque(); rerender(); });
    on('classe', debounce(async () => { CLASS = await api.classe(); rerender(); }, 800));
    on('presence', st => { PRES = st; const n = Object.keys(PRES).length; document.querySelectorAll('#liveN').forEach(el => el.textContent = n); $('#conn')?.classList.add('on'); rerenderProf(); });
    on('activity', a => { if (!api.isProf || !a) return; LIVE.unshift({...a, d: now()}); LIVE = LIVE.slice(0, 60); rerenderProf(); });
  }
  if (api.isProf) CLASS = await api.classe();
  presence({v: 'exercices'});
  route();
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
function route() {
  if (!api.user) return;
  let h = location.hash.slice(1) || 'exercices';
  if (h.startsWith('ex-')) { const e = byId(h.slice(3)); if (e) { CUR = e.id; F.lvl = e.niveau; } h = 'exercices'; }
  document.body.classList.toggle('detail', h === 'exercices' && !!CUR);
  if (h === 'prof' && !api.isProf) h = 'exercices';
  if (!['exercices', 'suivi', 'prof', 'apropos'].includes(h)) h = 'exercices';
  document.querySelectorAll('.view').forEach(v => v.classList.toggle('on', v.id === 'v-' + h));
  document.querySelectorAll('#nav a, #bnav a').forEach(a => a.dataset.v === h ? a.setAttribute('aria-current', 'page') : a.removeAttribute('aria-current'));
  if (h === 'exercices') { renderStrip(); renderList(); renderCopy(); }
  if (h === 'suivi') renderSuivi();
  if (h === 'prof') renderProf(true);
  if (h === 'apropos') $('#v-apropos').innerHTML = presentationPage();
  if (pres.v !== h) presence({v: h});
}
addEventListener('hashchange', route);
function rerender() {
  const v = document.querySelector('.view.on')?.id;
  if (v === 'v-exercices') { renderStrip(); renderList(); if (!CUR || !sess(CUR).busy) renderCopy(); }
  else if (v === 'v-suivi') renderSuivi();
  else if (v === 'v-prof') renderProf(false);
}
const rerenderProf = debounce(() => { if (document.querySelector('.view.on')?.id === 'v-prof') renderProf(false); }, 200);

/* ================= EXERCICES ================= */
function renderStrip() {
  const lvl = F.lvl, atL = all().filter(e => e.niveau === lvl);
  const ok = atL.filter(e => SUIVI.ex?.[e.id]?.s === 'reussi').length;
  const first = (api.profile.full_name || '').split(' ')[0];
  $('#strip').innerHTML = `<div><h2>Bonjour ${esc(first)} !</h2>
      ${CONF.message ? `<p class="msg">${ic('msg')} ${esc(CONF.message)}</p>` : `<p>Niveau ${LV[lvl]} : ${esc(LVD[lvl])}. Choisis un exercice, rédige, photographie, fais corriger.</p>`}</div>
    <div class="mini"><div><b>${ok}</b><span>réussis</span></div><div><b>${atL.length}</b><span>exercices</span></div><div><b>${Object.values(SUIVI.ex || {}).reduce((a, x) => a + (x.e || 0), 0)}</b><span>copies</span></div></div>`;
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
function filtered() {
  const q = F.q.trim().toLowerCase();
  if (F.fav) return favs().map(byId).filter(Boolean).filter(e => !q || (e.titre + ' ' + e.chap + ' ' + e.enonce).toLowerCase().includes(q));
  return all().filter(e => e.niveau === F.lvl && (!F.mat || e.mat === F.mat) && (!F.chap || e.chap === F.chap) &&
    (!q || (e.titre + ' ' + e.chap + ' ' + e.enonce).toLowerCase().includes(q)));
}
const statusOf = id => SUIVI.ex?.[id]?.s || '';
function renderList() {
  $('#fLvl').innerHTML = [1, 2, 3].map(n => `<button data-n="${n}" aria-pressed="${n === F.lvl}" title="${LV[n]}">${{1: 'CCINP', 2: 'Mines-CS', 3: 'X-ENS'}[n]}</button>`).join('');
  $('#fMat').innerHTML = [['', 'Tout'], ['Maths', 'Maths'], ['Physique', 'Physique'], ['Chimie', 'Chimie']].map(([m, l]) => `<button data-m="${m}" aria-pressed="${m === F.mat}">${m ? ic(MAT_IC[m]) : ''}${l}</button>`).join('');
  const chaps = [...new Set(all().filter(e => e.niveau === F.lvl && (!F.mat || e.mat === F.mat)).map(e => e.chap))].sort((a, b) => a.localeCompare(b, 'fr'));
  if (F.chap && !chaps.includes(F.chap)) F.chap = '';
  $('#fChap').innerHTML = `<option value="">Tous les chapitres (${chaps.length})</option>` + chaps.map(c => `<option ${c === F.chap ? 'selected' : ''}>${esc(c)}</option>`).join('');
  if (document.activeElement !== $('#fQ')) $('#fQ').value = F.q;
  $('#fFav').setAttribute('aria-pressed', !!F.fav); $('#fFav').innerHTML = `${ic('heart')} Mes favoris <span class="nb">${favs().length}</span>`;
  document.querySelector('.filters').classList.toggle('favmode', !!F.fav);
  const sel = new Set(CONF.sel?.[F.lvl] || []), order = ['Maths', 'Physique', 'Chimie'];
  const list = filtered().sort((a, b) => (sel.has(b.id) - sel.has(a.id)) || order.indexOf(a.mat) - order.indexOf(b.mat) || a.chap.localeCompare(b.chap, 'fr'));
  $('#items').innerHTML = list.length ? list.map(e => {
    const s = statusOf(e.id);
    return `<button class="item" data-id="${esc(e.id)}" aria-current="${e.id === CUR}">
      <span class="tile ${e.mat}">${ic(chapIcon(e.mat, e.chap))}</span>
      <span class="t">${sel.has(e.id) ? `<span style="color:var(--gold)">★</span> ` : ''}${esc(e.titre)}</span>
      <span class="st ${s === 'reussi' ? 'ok' : s ? 'go' : ''}" title="${s === 'reussi' ? 'Réussi' : s ? 'En cours' : 'À faire'}">${s === 'reussi' ? ic('check') : s ? '•' : ''}</span>
      <span class="m">${F.fav ? LV[e.niveau] + ' · ' : ''}${esc(e.chap)} · ${e.duree} min${FIG[e.id] ? ' · schéma' : ''}${isFav(e.id) ? ' · <span class="fv">♥</span>' : ''}</span></button>`;
  }).join('') : `<div class="empty">${F.fav ? 'Aucun favori pour l’instant : touche le cœur d’un exercice pour l’enregistrer.' : 'Aucun exercice pour ces filtres.'}</div>`;
  const done = list.filter(e => statusOf(e.id) === 'reussi').length;
  $('#count').textContent = `${list.length} exercice${list.length > 1 ? 's' : ''} · ${done} réussi${done > 1 ? 's' : ''}`;
  store.set('filters', F);
}
$('#fLvl').onclick = e => { const b = e.target.closest('button'); if (b) { F.lvl = +b.dataset.n; renderStrip(); renderList(); } };
$('#fMat').onclick = e => { const b = e.target.closest('button'); if (b) { F.mat = b.dataset.m; renderList(); } };
$('#fChap').onchange = e => { F.chap = e.target.value; renderList(); };
$('#fQ').oninput = e => { F.q = e.target.value; renderList(); };
$('#fFav').onclick = () => { F.fav = !F.fav; renderList(); };
$('#items').onclick = e => { const b = e.target.closest('.item'); if (b) openEx(b.dataset.id); };
function openEx(id) {
  CUR = id; const ex = byId(id);
  history.replaceState(null, '', '#ex-' + id);
  renderList(); renderCopy();
  presence({v: 'exercices', ex: id, t: ex?.titre?.slice(0, 90) || '', n: ex?.niveau || 0, st: 'lit', since: now()});
  document.body.classList.add('detail');
  scrollTo({top: innerWidth < 820 ? 0 : scrollY});
}
function closeEx() {
  CUR = null; document.body.classList.remove('detail');
  history.replaceState(null, '', '#exercices');
  renderList(); renderCopy(); presence({v: 'exercices', ex: null, t: null, st: null});
}
const correctionURL = id => new URL('correction.html?id=' + encodeURIComponent(id), location.href).href;
async function shareEx(ex, withCorr) {
  const url = correctionURL(ex.id) + (withCorr ? '' : '&enonce=1');
  const title = (withCorr ? 'Corrigé — ' : 'Exercice — ') + ex.titre;
  try {
    if (navigator.share) { await navigator.share({title, text: `${title} (${CONFIG.NOM_SITE})`, url}); return; }
  } catch (e) { if (e?.name === 'AbortError') return; }
  try { await navigator.clipboard.writeText(url); notice(`Lien copié : <a href="${esc(url)}" target="_blank" rel="noopener">${esc(url)}</a>`); }
  catch { notice(`Lien à partager : <a href="${esc(url)}" target="_blank" rel="noopener">${esc(url)}</a>`); }
}

const sess = id => SESS[id] ||= {imgs: [], tours: [], hint: 0, start: now(), solution: '', busy: false, note: ''};
let tick = null;
function renderCopy() {
  const el = $('#copy'); clearInterval(tick);
  const ex = CUR && byId(CUR);
  if (!ex) {
    const sel = (CONF.sel?.[F.lvl] || []).map(byId).filter(Boolean);
    el.innerHTML = `<div class="welcome">
      <div class="kicker"><span class="stamp n${F.lvl}">${LV[F.lvl]}</span></div>
      <h2>Une colle courte, maintenant ?</h2>
      <p class="enonce">${esc(LVD[F.lvl])}. Choisis un exercice dans la liste.</p>
      <div class="steps">
        <div><b>${ic('pen')} 1. Rédige</b><span class="small">Sur papier, comme au tableau, en surveillant le chrono.</span></div>
        <div><b>${ic('camera')} 2. Photographie</b><span class="small">Une ou plusieurs pages, bien éclairées.</span></div>
        <div><b>${ic('bulb')} 3. Progresse</b><span class="small">Étapes validées, première erreur, un indice.</span></div>
      </div>
      ${sel.length ? `<h3 class="sec">${ic('star')} La sélection du professeur</h3><div class="actions">${sel.map(e => `<button class="btn" data-open="${esc(e.id)}">${ic(MAT_IC[e.mat])} ${esc(e.titre)}</button>`).join('')}</div>` : ''}</div>`;
    el.querySelectorAll('[data-open]').forEach(b => b.onclick = () => openEx(b.dataset.open));
    return;
  }
  const S = sess(ex.id), st = SUIVI.ex?.[ex.id], fig = FIG[ex.id];
  const nCopies = S.tours.filter(t => t.kind === 'copie').length;
  const K = CORR[ex.id];
  const canReveal = S.tours.some(t => t.verdict === 'juste') || nCopies >= 2 || st?.s === 'reussi' || (K && S.hint >= 3);
  const hintsLeft = K ? 3 - S.hint : 3;
  el.innerHTML = `
    <button class="back" id="bBack">${ic('back')} Exercices</button>
    <div class="kicker"><span class="stamp n${ex.niveau}">${LV[ex.niveau]}</span><span class="pill">${ic(MAT_IC[ex.mat])}${esc(ex.mat)}</span><span class="pill">${ic(chapIcon(ex.mat, ex.chap))}${esc(ex.chap)}</span>
      <span class="pill tm">${ic('clock')}<span class="timer" id="timer">0:00</span>&nbsp;/ ${ex.duree}:00</span></div>
    <div class="titlerow"><h2>${esc(ex.titre)}</h2>
      <div class="tools"><button class="iconbtn fav" id="bFav" aria-pressed="${isFav(ex.id)}">${ic('heart')}<span class="lbl">${isFav(ex.id) ? 'Enregistré' : 'Enregistrer'}</span></button>
      <button class="iconbtn" id="bShareEx" title="Partager l’exercice">${ic('share')}<span class="lbl">Partager</span></button></div></div>
    ${st ? `<div class="status ${st.s === 'reussi' ? 'ok' : ''}">${ic(st.s === 'reussi' ? 'trophy' : 'pen')} ${st.s === 'reussi' ? 'Déjà réussi' : 'En cours'} · ${st.e || 0} copie${(st.e || 0) > 1 ? 's' : ''} corrigée${(st.e || 0) > 1 ? 's' : ''}</div>` : ''}
    <div class="ex-body ${fig ? 'withfig' : ''}">
      <div class="enonce">${fmtEnonce(ex.enonce)}</div>
      ${fig ? `<figure class="fig">${fig.svg}<figcaption>${ic('eye')}<span>${esc(fig.legende)}</span></figcaption></figure>` : ''}
    </div>
    <div class="drop" id="drop">
      <label class="pick"><input type="file" id="file" accept="image/*" multiple>${ic('camera', 'lg')} Ajouter la photo de ma copie <span class="small" style="font-weight:400">(4 pages max., glisser-déposer possible)</span></label>
      ${S.imgs.length ? `<div class="thumbs" id="thumbs">${S.imgs.map((im, i) => `<div class="thumb"><img src="${im.url}" alt="Page ${i + 1}"><button data-rm="${i}" aria-label="Retirer la page ${i + 1}">${ic('x')}</button></div>`).join('')}</div>` : ''}
      <textarea class="note" id="note" placeholder="Facultatif : où bloques-tu ? que veux-tu faire vérifier ?">${esc(S.note)}</textarea>
    </div>
    <div class="actions" id="actions">
      <button class="btn primary" id="bCorr" ${S.busy || !S.imgs.length ? 'disabled' : ''}>${S.busy === 'copie' ? '<span class="spin"></span> Lecture de la copie…' : ic('pen') + ' Faire corriger ma copie'}</button>
      <button class="btn" id="bHint" ${S.busy || hintsLeft <= 0 ? 'disabled' : ''}>${S.busy === 'indice' ? '<span class="spin"></span> …' : ic('bulb') + (hintsLeft <= 0 ? ' Tous les indices sont donnés' : ` Indice ${Math.min(S.hint + 1, 3)}/3`)}</button>
      <button class="btn" id="bSol" ${S.busy || !canReveal ? 'disabled' : ''} title="${canReveal ? '' : 'Disponible après 2 copies corrigées, une réussite ou les 3 indices'}">${S.busy === 'solution' ? '<span class="spin"></span> Rédaction…' : ic('eye') + ' Voir le corrigé'}</button>
    </div>
    <div class="feed">${S.tours.map(tourHTML).join('')}</div>
    ${S.solution ? `<div class="sol" id="sol"><div class="solhead"><h3>${ic('book')} Corrigé détaillé</h3>
        ${K ? `<div class="soltools"><a class="btn" href="${esc(correctionURL(ex.id))}&pdf=1" target="_blank" rel="noopener">${ic('pdf')} PDF</a><button class="btn" id="bShareCorr">${ic('share')} Partager</button></div>` : ''}</div>
      ${S.reponse ? `<div class="result">${ic('target')}<div><span class="lab">Résultat</span><div>${rich(S.reponse)}</div></div></div>` : ''}
      <div class="corrige">${fmtCorrige(S.solution)}</div><p class="small">${K ? 'Corrigé de référence de la colle.' : 'Corrigé rédigé par IA : vérifie-le avec ton cours.'}</p></div>` : ''}`;
  typeset(el);
  const tm = $('#timer'); const upd = () => { const s = (now() - S.start) / 1000; tm.textContent = mmss(s); tm.classList.toggle('late', s > ex.duree * 60); };
  upd(); tick = setInterval(upd, 1000);
  $('#file').onchange = e => addFiles(ex.id, e.target.files);
  $('#note').oninput = e => { S.note = e.target.value; };
  $('#thumbs') && ($('#thumbs').onclick = e => { const b = e.target.closest('[data-rm]'); if (b) { S.imgs.splice(+b.dataset.rm, 1); renderCopy(); } });
  const d = $('#drop');
  d.ondragover = e => { e.preventDefault(); d.classList.add('over'); };
  d.ondragleave = () => d.classList.remove('over');
  d.ondrop = e => { e.preventDefault(); d.classList.remove('over'); addFiles(ex.id, e.dataTransfer.files); };
  $('#bCorr').onclick = () => ask(ex, 'copie');
  $('#bHint').onclick = () => ask(ex, 'indice');
  $('#bSol').onclick = () => ask(ex, 'solution');
  $('#bBack').onclick = closeEx;
  $('#bFav').onclick = () => toggleFav(ex.id);
  $('#bShareEx').onclick = () => shareEx(ex, false);
  $('#bShareCorr') && ($('#bShareCorr').onclick = () => shareEx(ex, true));
}
function tourHTML(t) {
  const vlab = {juste: 'Juste', partiel: 'Partiel', faux: 'Erreur', illisible: 'Illisible', bloque: 'Coup de pouce'}[t.verdict] || t.verdict;
  return `<div class="tour"><div class="h"><b>${t.kind === 'copie' ? 'Copie ' + t.n : 'Indice demandé'}</b><span class="verdict ${esc(t.verdict)}">${esc(vlab)}</span>
    ${t.score != null && t.kind === 'copie' ? `<span class="meter" title="Avancement estimé"><i style="width:${t.score}%"></i></span><span class="small">${t.score} %</span>` : ''}</div>
    ${t.resume ? `<div>${rich(t.resume)}</div>` : ''}
    ${t.points?.length ? `<ul class="pts">${t.points.map(p => `<li><span class="mk ${esc(p.statut)}">${p.statut === 'ok' ? ic('check') : p.statut === 'erreur' ? ic('x') : '·'}</span><span><b>${esc(p.etape)}</b>${p.note ? ' — ' + esc(p.note) : ''}</span></li>`).join('')}</ul>` : ''}
    ${t.retour ? `<div>${rich(t.retour)}</div>` : ''}
    ${t.indice ? `<div class="hint">${ic('bulb')}<div><span class="lab">Indice ${t.hint || ''}</span><div>${rich(t.indice)}</div></div></div>` : ''}
    ${t.question ? `<div class="q">« ${esc(t.question)} »</div>` : ''}</div>`;
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
  presence({st: 'redige'}); renderCopy();
}

/* ---------- IA ---------- */
async function ask(ex, mode) {
  const S = sess(ex.id), K = CORR[ex.id];
  if (mode === 'copie' && !S.imgs.length) return;
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
  presence({st: mode === 'copie' ? 'correction' : mode === 'indice' ? 'indice' : 'corrige'});
  try {
    const hist = S.tours.map(t => `- ${t.kind === 'copie' ? 'Copie ' + t.n : 'Indice'} : ${t.verdict}. ${t.retour || ''} ${t.indice ? 'Indice : ' + t.indice : ''}`).join('\n');
    const r = await api.ia({mode, exercice: {titre: ex.titre, mat: ex.mat, chap: ex.chap, niveau: ex.niveau, enonce: ex.enonce},
      images: mode === 'copie' ? S.imgs.map(i => i.data) : [], note: S.note, hint: Math.min(S.hint + 1, 3), historique: hist,
      reference: K ? `${K.corrige}\n\nRÉSULTAT ATTENDU : ${K.reponse}` : '', indices: K ? K.indices : []});
    if (mode === 'solution') { S.solution = String(r.corrige || ''); await record(ex, {kind: 'solution'}); }
    else {
      const t = {kind: mode, n: S.tours.filter(t => t.kind === 'copie').length + 1, hint: r.indice ? Math.min(S.hint + 1, 3) : 0,
        verdict: ['juste', 'partiel', 'faux', 'illisible', 'bloque'].includes(r.verdict) ? r.verdict : (mode === 'copie' ? 'partiel' : 'bloque'),
        score: r.score != null && Number.isFinite(+r.score) ? Math.max(0, Math.min(100, Math.round(+r.score))) : null,
        resume: String(r.resume || ''), retour: String(r.retour || ''), indice: String(r.indice || ''), question: String(r.question || ''),
        points: Array.isArray(r.points) ? r.points.slice(0, 8).map(p => ({etape: String(p.etape || ''), statut: ['ok', 'erreur', 'manquant'].includes(p.statut) ? p.statut : 'manquant', note: String(p.note || '')})) : []};
      if (t.indice) S.hint = Math.min(S.hint + 1, 3);
      S.tours.push(t); if (mode === 'copie') S.imgs = [];
      await record(ex, t);
      presence({st: t.verdict === 'juste' ? 'reussi' : 'redige'});
      api.activity({uid: api.user.id, name: api.profile.full_name, id: ex.id, k: t.kind, v: t.verdict, sc: t.score});
    }
  } catch (e) { notice(esc(e.message || 'Erreur')); }
  finally { S.busy = false; renderCopy(); }
}

/* ---------- suivi ---------- */
async function record(ex, t) {
  SUIVI.ex ||= {}; SUIVI.journal ||= []; SUIVI.cree ||= now();
  const st = SUIVI.ex[ex.id] ||= {s: 'en_cours', e: 0, i: 0, sc: 0, d: 0, t: 0};
  if (t.kind === 'copie') { st.e++; if (t.score != null) st.sc = Math.max(st.sc || 0, t.score); if (t.verdict === 'juste') { st.s = 'reussi'; st.sc = 100; } }
  if (t.kind === 'indice' || (t.kind === 'copie' && t.indice)) st.i++;
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
function renderSuivi() {
  const s = SUIVI, lvl = api.profile.niveau || 1;
  const exs = Object.values(s.ex || {}), atL = all().filter(e => e.niveau === lvl);
  const ok = atL.filter(e => s.ex?.[e.id]?.s === 'reussi').length;
  const tot = (k) => exs.reduce((a, v) => a + (v[k] || 0), 0);
  const rec = recommend(s, lvl);
  $('#v-suivi').innerHTML = `
    <div class="pagehead"><h2>Mon suivi</h2><span class="small">${esc(api.profile.full_name)} · ${DEMO ? 'mode démonstration' : 'enregistré sur ton compte'}</span></div>
    <div class="lvl" id="lvlPick">${[1, 2, 3].map(n => `<button data-n="${n}" aria-pressed="${n === lvl}"><b>${LV[n]}</b><span>${esc(LVD[n])}</span></button>`).join('')}</div>
    <div class="hero">
      <div class="panel stat" style="padding:24px"><div class="k">${ic('trophy')} Exercices réussis — ${LV[lvl]}</div>
        <div class="big">${ok}<span style="font-size:.42em;color:var(--soft)"> / ${atL.length}</span></div>
        <div class="bar" style="grid-template-columns:minmax(0,1fr);margin-top:10px"><span class="tr"><i style="width:${atL.length ? 100 * ok / atL.length : 0}%;background:var(--green)"></i></span></div></div>
      <div class="stats">
        <div class="panel stat"><div class="k">${ic('pen')} Copies corrigées</div><div class="v">${tot('e')}</div></div>
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
    <div class="panel scroll"><table class="stack"><thead><tr><th>Date</th><th>Exercice</th><th>Action</th><th class="r">Avancement</th></tr></thead><tbody>
    ${(s.journal || []).map(j => `<tr><td>${fmtDate(j.d)}</td><td>${esc(byId(j.id)?.titre || j.id)}</td><td>${j.k === 'copie' ? 'Copie : ' + esc({juste: 'juste', partiel: 'partielle', faux: 'erreur', illisible: 'illisible'}[j.v] || j.v) : j.k === 'indice' ? 'Indice' : 'Corrigé consulté'}</td><td class="r">${j.sc != null ? j.sc + ' %' : ''}</td></tr>`).join('') || '<tr><td colspan="4" class="empty">Pas encore d’activité.</td></tr>'}
    </tbody></table></div>`;
  $('#lvlPick').onclick = async e => { const b = e.target.closest('button'); if (!b) return; F.lvl = +b.dataset.n; await api.setMyLevel(F.lvl); renderSuivi(); };
  document.querySelectorAll('#v-suivi [data-open]').forEach(b => b.onclick = () => { location.hash = 'ex-' + b.dataset.open; });
}

/* ================= TABLEAU DE BORD ================= */
let built = false;
function renderProf(full) {
  if (!api.isProf) return;
  if (!built || full) buildProf();
  updateProf();
}
function buildProf() {
  built = true;
  $('#v-prof').innerHTML = `
    <div class="pagehead"><h2>Tableau de bord</h2><span class="small">${esc(CONFIG.NOM_PROF)} · ${new Date().toLocaleDateString('fr-FR', {weekday: 'long', day: 'numeric', month: 'long'})}</span></div>
    <div class="stats" id="pStats"></div>
    <h3 class="sec">${ic('live')} En direct</h3><div class="live" id="pLive"></div>
    <div class="grid2">
      <div><h3 class="sec">${ic('users')} Élèves</h3>
        <div class="panel scroll"><table class="stack"><thead><tr><th>Élève</th><th>Niveau</th><th class="r">Réussis</th><th class="r">Copies</th><th class="r">Indices</th><th>À revoir</th><th>Dernière activité</th></tr></thead><tbody id="pRows"></tbody></table></div></div>
      <div><h3 class="sec">${ic('msg')} Fil d’activité</h3><ul class="stream" id="pStream"></ul></div>
    </div>
    <div class="grid2">
      <div><h3 class="sec">${ic('star')} Message et sélection pour la classe</h3><div class="panel form" id="pConf"></div></div>
      <div><h3 class="sec">${ic('plus')} Ajouter un exercice</h3>
        <div class="panel form">
          <label class="btn" style="justify-self:start;cursor:pointer;position:relative"><input type="file" id="impFile" accept="image/*" class="sr">${ic('camera')} Importer depuis une photo d’énoncé</label>
          <span class="small" id="impSt">L’IA retranscrit l’énoncé en LaTeX ; relis avant d’enregistrer.</span>
          <div class="row"><label class="field">Titre<input id="aT"></label><label class="field">Matière<select id="aM"><option>Maths</option><option>Physique</option><option>Chimie</option></select></label></div>
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
  $('#impFile').onchange = e => importPhoto(e.target.files[0]);
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
  const st = {lit: 'lit l’énoncé', redige: 'rédige', correction: 'attend la correction', indice: 'demande un indice', corrige: 'lit le corrigé', reussi: 'a réussi'}[p.st] || '';
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
  for (const s of students) for (const j of s.data?.journal || []) if (j.d >= +today && j.k === 'copie') { triesToday++; if (j.v === 'juste') okToday++; }
  $('#pStats').innerHTML = `
    <div class="panel stat"><div class="k">${ic('live')} Connectés maintenant</div><div class="v">${people.length}</div></div>
    <div class="panel stat"><div class="k">${ic('users')} Élèves inscrits</div><div class="v">${students.length}</div></div>
    <div class="panel stat"><div class="k">${ic('pen')} Copies corrigées aujourd’hui</div><div class="v">${triesToday}</div></div>
    <div class="panel stat"><div class="k">${ic('trophy')} Réussites aujourd’hui</div><div class="v">${okToday}</div></div>`;
  $('#pLive').innerHTML = DEMO ? '<div class="empty">Le temps réel fonctionne une fois Supabase configuré.</div>' : people.map(p => `<div class="panel lc">
      <div class="person">${avatar(p.uid, p.name)}<b>${esc(p.name || 'Élève')}</b>${p.uid === api.user.id ? '<span class="small">(vous)</span>' : ''}${p.role === 'prof' ? '<span class="small">prof</span>' : ''}</div>
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
  $('#pStream').innerHTML = items.map(it => `<li>${ic(it.k === 'copie' ? (it.v === 'juste' ? 'trophy' : 'pen') : it.k === 'indice' ? 'bulb' : 'eye')}<span><b>${esc(it.name || 'Élève')}</b> · ${it.k === 'copie' ? 'copie ' + esc({juste: 'juste', partiel: 'partielle', faux: 'avec erreur', illisible: 'illisible'}[it.v] || it.v) : it.k === 'indice' ? 'indice demandé' : 'corrigé consulté'} — ${esc(byId(it.id)?.titre || it.id)} <span class="small">${ago(it.d)}</span></span></li>`).join('') || '<li class="small">Rien pour l’instant.</li>';
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
    <div class="scroll"><table class="stack"><thead><tr><th>Exercice</th><th>Statut</th><th class="r">Copies</th><th class="r">Indices</th><th class="r">Max</th><th>Date</th></tr></thead><tbody>
    ${Object.entries(d.ex || {}).sort((a, b) => b[1].d - a[1].d).map(([eid, v]) => `<tr><td>${esc(byId(eid)?.titre || eid)}</td><td>${v.s === 'reussi' ? '✓ réussi' : 'en cours'}${v.vu ? ' · corrigé vu' : ''}</td><td class="r">${v.e || 0}</td><td class="r">${v.i || 0}</td><td class="r">${v.sc || 0} %</td><td>${fmtDate(v.d)}</td></tr>`).join('') || '<tr><td colspan="6" class="empty">Rien encore.</td></tr>'}
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
    $('#aT').value = r.titre || ''; $('#aM').value = ['Maths', 'Physique', 'Chimie'].includes(r.mat) ? r.mat : 'Maths'; $('#aC').value = r.chap || '';
    $('#aN').value = [1, 2, 3].includes(+r.niveau) ? r.niveau : 2; $('#aD').value = r.duree || 20; $('#aE').value = r.enonce || '';
    $('#impSt').textContent = 'Énoncé retranscrit : relis-le puis clique sur « Ajouter ».';
  } catch (e) { $('#impSt').textContent = e.message; }
}

/* ================= LANCEMENT ================= */
(async function boot() {
  try { BASE = await (await fetch('data/exercices.json')).json(); } catch { BASE = []; }
  fetch('data/corriges.json').then(r => r.json()).then(d => { CORR = d || {}; if (api.user) rerender(); }).catch(() => {});
  await api.init();
  if (api.user) start(); else showAuth('in');
})();
