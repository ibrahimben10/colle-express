// Communauté : annuaire, fil des abonnements, solutions publiées par des élèves,
// signalements et file de modération. Aucun classement académique n'est affiché.
import { api } from './api.js';
import { ic } from './icons.js';
import { esc, rich } from './format.js';
import { toast } from './ui.js';
import { FILIERES, DOMAINES } from './profil.js';

let D = {};   // byId, typeset, cartes(ids) -> map, myUser()
export const initCommunaute = deps => { D = deps; };
const initials = n => (n || '?').split(/\s+/).filter(Boolean).slice(0, 2).map(w => w[0].toUpperCase()).join('');
const hue = s => { let h = 0; for (const c of String(s)) h = (h * 31 + c.charCodeAt(0)) % 360; return h; };
const av = (id, nom, photo, cls = 'avatar') => /^data:image\/(jpeg|png|webp);base64,[A-Za-z0-9+/=]+$/.test(photo || '') ? `<img class="${cls}" src="${photo}" alt="">` : `<span class="${cls}" style="background:hsl(${hue(id)} 55% 42%)">${esc(initials(nom))}</span>`;
const ago = d => { const s = (Date.now() - Date.parse(d)) / 1000; return s < 60 ? 'à l’instant' : s < 3600 ? `il y a ${Math.floor(s / 60)} min` : s < 86400 ? `il y a ${Math.floor(s / 3600)} h` : new Date(d).toLocaleDateString('fr-FR', {day: 'numeric', month: 'short'}); };
const plural = (n, s, p = s + 's') => `${n} ${n > 1 ? p : s}`;

/* ===================== PAGE COMMUNAUTÉ ===================== */
let F = {q: '', filiere: '', matiere: '', etab: '', collections: false, suivis: false}, TAB = 'annuaire', PAGE = 0, LIST = [];
export async function renderCommunaute(el, tab) {
  if (tab) TAB = tab;
  el.innerHTML = `<div class="cm">
    <header class="cm-head"><div><h1>Les membres de Colle express</h1>
      <p class="cn-sub">Seuls les profils publics qui ont choisi d’apparaître ici sont listés, par ordre alphabétique : il n’y a aucun classement.</p></div>
      <div class="seg" role="tablist" aria-label="Communauté"><button role="tab" data-tab="annuaire" aria-selected="${TAB === 'annuaire'}">${ic('users')} Annuaire</button><button role="tab" data-tab="fil" aria-selected="${TAB === 'fil'}">${ic('live')} Mes abonnements</button></div></header>
    <div id="cmBody"></div></div>`;
  el.querySelectorAll('[data-tab]').forEach(b => b.onclick = () => { location.hash = b.dataset.tab === 'fil' ? '#communaute/fil' : '#communaute'; });
  const body = el.querySelector('#cmBody');
  if (TAB === 'fil') return renderFil(body);
  body.innerHTML = `<form class="cm-filters" id="cmF" role="search">
      <div class="cm-q"><span aria-hidden="true">${ic('search')}</span><label class="sr" for="cmQ">Rechercher un membre</label><input id="cmQ" type="search" placeholder="Nom, @identifiant ou mot de la présentation" value="${esc(F.q)}"></div>
      <label class="sr" for="cmFil">Filière</label><select id="cmFil"><option value="">Toutes filières</option>${FILIERES.map(f => `<option ${F.filiere === f ? 'selected' : ''}>${f}</option>`).join('')}</select>
      <label class="sr" for="cmMat">Matière d’intérêt</label><select id="cmMat"><option value="">Toutes matières</option>${DOMAINES.map(d => `<option ${F.matiere === d ? 'selected' : ''}>${esc(d)}</option>`).join('')}</select>
      <label class="sr" for="cmEt">Établissement</label><input id="cmEt" placeholder="Établissement" value="${esc(F.etab)}">
      <label class="mini-tg"><input type="checkbox" id="cmCol" ${F.collections ? 'checked' : ''}> Avec collections publiques</label>
      <label class="mini-tg"><input type="checkbox" id="cmSui" ${F.suivis ? 'checked' : ''}> Que je suis</label>
    </form>
    <div id="cmList" aria-live="polite"></div>`;
  const f = body.querySelector('#cmF');
  let t = 0;
  const go = () => { clearTimeout(t); t = setTimeout(async () => {
    F = {q: f.cmQ.value.trim(), filiere: f.cmFil.value, matiere: f.cmMat.value, etab: f.cmEt.value.trim(), collections: f.cmCol.checked, suivis: f.cmSui.checked};
    PAGE = 0; await load(body, false); }, 250); };
  f.addEventListener('input', go); f.addEventListener('submit', e => { e.preventDefault(); go(); });
  await load(body, false);
}
async function load(body, more) {
  const box = body.querySelector('#cmList');
  if (!more) box.innerHTML = `<div role="status" aria-label="Chargement">${'<div class="skel-item"><span class="skel"></span><span class="skel skel-l w60"></span><span class="skel skel-l w40"></span></div>'.repeat(4)}</div>`;
  let L;
  try { L = await api.annuaire(F, PAGE); } catch (x) { box.innerHTML = `<div class="panel empty">Annuaire indisponible pour le moment.</div>`; return; }
  LIST = more ? LIST.concat(L) : L;
  box.innerHTML = LIST.length ? `<ul class="cm-list">${LIST.map(cardHTML).join('')}</ul>${L.length === 24 ? '<button class="btn wide" id="cmMore">Afficher plus de membres</button>' : ''}`
    : `<div class="panel empty">${Object.values(F).some(Boolean) ? 'Aucun membre ne correspond à ces filtres.' : 'Personne n’apparaît encore dans l’annuaire. Pour y figurer : Profil → Modifier → « Apparaître dans l’annuaire ».'}</div>`;
  box.querySelector('#cmMore')?.addEventListener('click', () => { PAGE++; load(body, true); });
  bindFollow(box, id => { const m = LIST.find(x => x.id === id); m.suivi = !m.suivi; m.abonnes += m.suivi ? 1 : -1; return m; }, m => { box.querySelector(`[data-follow="${m.id}"]`).outerHTML = followBtn(m.id, m.suivi); });
}
function cardHTML(m) {
  return `<li class="cm-card"><a class="cm-id" href="#u/${esc(m.username || m.id)}">${av(m.id, m.nom, m.photo)}<span><b>${esc(m.nom)}</b><span class="small">@${esc(m.username || '')}${m.filiere ? ' · ' + esc(m.filiere) : ''}${m.annee ? ` · ${m.annee}${m.annee === 1 ? 're' : 'e'} année` : ''}${m.etablissement ? ' · ' + esc(m.etablissement) : ''}</span></span></a>
    ${m.bio ? `<p class="cm-bio">${esc(m.bio)}</p>` : ''}
    <div class="cm-foot">${(m.matieres || []).slice(0, 4).map(x => `<span class="cm-tag">${esc(x)}</span>`).join('')}
      <span class="small cm-n">${plural(m.abonnes, 'abonné')}${m.collections ? ` · ${plural(m.collections, 'collection')}` : ''}</span>
      ${m.id !== D.myId() ? followBtn(m.id, m.suivi) : '<span class="small">C’est toi</span>'}</div></li>`;
}
export const followBtn = (id, on) => `<button type="button" class="btn ${on ? '' : 'primary'} btn-follow" data-follow="${esc(id)}" aria-pressed="${!!on}">${ic(on ? 'check' : 'plus')} ${on ? 'Suivi' : 'Suivre'}</button>`;
// Lie chaque bouton « Suivre » présent dans root (idempotent : onclick est remplacé, jamais empilé)
export function bindFollow(root, toggle, redraw) {
  root.querySelectorAll('[data-follow]').forEach(b => b.onclick = async () => {
    const on = b.getAttribute('aria-pressed') !== 'true'; b.disabled = true;
    try { await api.suivre(b.dataset.follow, on); const m = toggle(b.dataset.follow); redraw(m); bindFollow(root, toggle, redraw);
      toast(on ? 'Tu suis ce profil : ses publications apparaîtront dans « Mes abonnements ».' : 'Tu ne suis plus ce profil.', 'ok'); }
    catch (x) { b.disabled = false; toast(x.message, 'error'); }
  });
}
async function renderFil(body) {
  body.innerHTML = `<div role="status" aria-label="Chargement">${'<span class="skel skel-card"></span>'.repeat(2)}</div>`;
  let L; try { L = await api.filAbonnements(); } catch { body.innerHTML = '<div class="panel empty">Fil indisponible pour le moment.</div>'; return; }
  const verbe = {solution: 'a publié une solution', commentaire: 'a commenté publiquement', collection: 'a partagé une collection', carnet: 'a publié une page de carnet'};
  body.innerHTML = L.length ? `<ol class="cm-feed">${L.map(e => { const ex = e.ex && D.byId(e.ex);
    const lien = e.k === 'collection' ? `#c/${esc(e.ref)}` : ex ? `#ex-${esc(ex.id)}` : `#u/${esc(e.username || e.u)}`;
    return `<li>${av(e.u, e.nom, e.photo)}<div><p><a class="who" href="#u/${esc(e.username || e.u)}"><b>${esc(e.nom)}</b></a> ${verbe[e.k] || ''}${ex ? ` sur <a href="#ex-${esc(ex.id)}">${esc(ex.titre)}</a>` : ''}${e.titre ? ` : <a href="${lien}">${esc(e.titre)}</a>` : ''} <span class="small">· ${ago(e.d)}</span></p>
      ${e.txt ? `<blockquote class="cm-ex">${esc(e.txt)}${e.txt.length >= 240 ? '…' : ''}</blockquote>` : ''}</div></li>`; }).join('')}</ol>`
    : `<div class="panel empty">Rien pour l’instant. Suis des membres depuis l’annuaire : leurs solutions, collections et notes publiques apparaîtront ici.</div>`;
}

/* ===================== SOLUTIONS D'ÉLÈVES (sous un exercice) ===================== */
const S = {};   // état par exercice : ouverture, brouillon
export async function renderSolutions(box, ex, {locked, admin, me}) {
  if (!box) return;
  const st = S[ex.id] ||= {open: false, draft: ''};
  if (locked) { box.innerHTML = `<p class="small">${ic('lock')} Les solutions rédigées par d’autres élèves s’ouvrent quand tu as soumis ta réponse ou consulté les indices, comme le corrigé.</p>`; return; }
  box.innerHTML = `<div role="status" aria-label="Chargement">${'<span class="skel skel-card"></span>'}</div>`;
  let L; try { L = await api.solutions(ex.id); } catch { box.innerHTML = '<p class="small">Solutions indisponibles pour le moment.</p>'; return; }
  const ids = [...new Set(L.flatMap(s => [s.user_id, ...s.commentaires.map(c => c.user_id)]))];
  const C = await D.cartes(ids);
  const nom = u => u === me ? 'Moi' : C[u]?.nom || 'Membre', link = u => `<a class="who" href="#u/${esc(C[u]?.username || u)}">${esc(nom(u))}</a>`;
  const mienne = L.find(s => s.user_id === me);
  box.innerHTML = `
    <p class="sol-warn">${ic('pen')} Solutions <b>rédigées par des élèves</b> : elles n’ont pas la valeur d’un corrigé et peuvent contenir des erreurs, sauf mention « Vérifiée par l’administrateur ». Signale une erreur si tu en vois une.</p>
    ${L.length ? `<ol class="sols">${L.map(s => { const errs = s.commentaires.filter(c => c.type === 'erreur').length;
      return `<li class="sol ${s.statut === 'masquee' ? 'hidden-sol' : ''}" id="sol-${esc(s.id)}">
        <header>${D.avatar(s.user_id, nom(s.user_id))}<div><b>${link(s.user_id)}</b><span class="small">${ago(s.created_at)}${s.updated_at && s.updated_at !== s.created_at ? ' · modifiée' : ''}</span></div>
          ${s.verifiee ? `<span class="lab-ok">${ic('check')} Vérifiée par l’administrateur</span>` : `<span class="lab-warn">Solution d’élève · non vérifiée</span>`}
          ${errs ? `<span class="lab-err">${plural(errs, 'erreur signalée', 'erreurs signalées')}</span>` : ''}${s.statut === 'masquee' ? '<span class="lab-err">Masquée (signalements)</span>' : ''}</header>
        <div class="sol-b">${rich(s.contenu)}</div>
        <div class="sol-act">
          ${s.user_id === me ? `<button class="linkbtn" data-sedit="${esc(s.id)}">Modifier</button><button class="linkbtn danger" data-sdel="${esc(s.id)}">Supprimer</button>`
            : `<button class="linkbtn" data-sig="solution|${esc(s.id)}">Signaler un abus</button>`}
          ${admin ? `<button class="linkbtn" data-sver="${esc(s.id)}|${s.verifiee ? 0 : 1}">${s.verifiee ? 'Retirer la vérification' : 'Marquer comme vérifiée'}</button>
            <button class="linkbtn" data-smask="${esc(s.id)}|${s.statut === 'masquee' ? 'publiee' : 'masquee'}">${s.statut === 'masquee' ? 'Rétablir' : 'Masquer'}</button>${s.user_id !== me ? `<button class="linkbtn danger" data-sdel="${esc(s.id)}">Supprimer</button>` : ''}` : ''}
        </div>
        <details class="sol-coms" ${st['c' + s.id] ? 'open' : ''} data-sc="${esc(s.id)}"><summary>${plural(s.commentaires.length, 'commentaire')}</summary>
          <ul>${s.commentaires.map(c => `<li class="${c.type === 'erreur' ? 'is-err' : ''}">${c.type === 'erreur' ? `<span class="lab-err">Erreur signalée</span>` : ''}<b>${link(c.user_id)}</b> <span class="small">${ago(c.created_at)}</span>
            <div class="sol-cb">${rich(c.contenu)}</div>${c.user_id === me || admin ? `<button class="linkbtn danger" data-cdel="${esc(c.id)}">Supprimer</button>` : `<button class="linkbtn" data-sig="solution_commentaire|${esc(c.id)}">Signaler</button>`}</li>`).join('')}</ul>
          <form class="sol-cf" data-sid="${esc(s.id)}"><div class="comvis" role="radiogroup" aria-label="Type de message">
              <label><input type="radio" name="t-${esc(s.id)}" value="commentaire" checked><span>${ic('msg')} Commentaire</span></label>
              <label><input type="radio" name="t-${esc(s.id)}" value="erreur"><span>${ic('x')} Signaler une erreur</span></label></div>
            <textarea class="note" maxlength="4000" rows="2" placeholder="Ta remarque (formules entre $…$)"></textarea><button class="btn" type="submit">Envoyer</button></form>
        </details></li>`; }).join('')}</ol>` : '<p class="small">Aucune solution d’élève pour l’instant.</p>'}
    ${mienne ? '' : `<details class="sol-new" ${st.open ? 'open' : ''}><summary>${ic('pen')} Publier ma solution</summary>
      <form id="solForm"><textarea class="note" id="solTxt" maxlength="20000" rows="8" placeholder="Rédige ta solution complète (formules entre $…$). Elle sera visible par tous les membres connectés.">${esc(st.draft)}</textarea>
        <details class="nprev"><summary>Aperçu</summary><div class="cn-rich" id="solPrev"></div></details>
        <label class="mini-tg"><input type="checkbox" id="solOk"> Je l’ai rédigée moi-même et j’accepte qu’elle soit visible par tous les membres, avec mon nom.</label>
        <button class="btn primary" type="submit">${ic('upload')} Publier</button></form></details>`}`;
  D.typeset?.([...box.querySelectorAll('.sol-b, .sol-cb')]);
  bindSolutions(box, ex, L, {admin, me});
}
function bindSolutions(box, ex, L, ctx) {
  const st = S[ex.id], redo = () => renderSolutions(box, ex, {locked: false, ...ctx});
  const f = box.querySelector('#solForm');
  if (f) {
    box.querySelector('.sol-new').addEventListener('toggle', e => { st.open = e.target.open; });
    f.solTxt.oninput = () => { st.draft = f.solTxt.value; };
    box.querySelector('#solForm .nprev').addEventListener('toggle', () => { const p = box.querySelector('#solPrev'); p.innerHTML = rich(f.solTxt.value || '—'); D.typeset?.([p]); });
    f.onsubmit = async e => { e.preventDefault();
      const v = f.solTxt.value.trim();
      if (v.length < 20) return toast('Ta solution est trop courte (20 caractères au moins).', 'error');
      if (!f.solOk.checked) return toast('Coche la case pour confirmer que tu l’as rédigée toi-même.', 'error');
      const b = f.querySelector('[type=submit]'); b.disabled = true;
      try { await api.publierSolution(ex.id, v); st.draft = ''; st.open = false; toast('Solution publiée. Merci pour ta contribution !', 'ok'); redo(); }
      catch (x) { b.disabled = false; toast(x.message, 'error'); } };
  }
  box.querySelectorAll('.sol-coms').forEach(d => d.addEventListener('toggle', () => { st['c' + d.dataset.sc] = d.open; }));
  box.querySelectorAll('.sol-cf').forEach(cf => cf.onsubmit = async e => { e.preventDefault();
    const t = cf.querySelector('textarea'), v = t.value.trim(); if (!v) return;
    const type = cf.querySelector('input[type=radio]:checked').value;
    try { await api.commenterSolution(cf.dataset.sid, v, type); st['c' + cf.dataset.sid] = true; toast(type === 'erreur' ? 'Erreur signalée à l’auteur et aux lecteurs.' : 'Commentaire envoyé.', 'ok'); redo(); }
    catch (x) { toast(x.message, 'error'); } });
  box.onclick = async e => {
    const b = e.target.closest('button'); if (!b) return;
    try {
      if (b.dataset.sedit) { const s = L.find(x => x.id === b.dataset.sedit), body = box.querySelector(`#sol-${CSS.escape(s.id)} .sol-b`);
        body.innerHTML = `<textarea class="note" maxlength="20000" rows="8">${esc(s.contenu)}</textarea><p class="small">Toute modification retire une éventuelle vérification.</p><div class="comform-b"><button class="btn ghost" data-cancel>Annuler</button><button class="btn primary" data-save>Enregistrer</button></div>`;
        body.querySelector('[data-cancel]').onclick = redo;
        body.querySelector('[data-save]').onclick = async () => { try { await api.publierSolution(ex.id, body.querySelector('textarea').value.trim(), s.id); toast('Solution modifiée.', 'ok'); redo(); } catch (x) { toast(x.message, 'error'); } };
        return; }
      if (b.dataset.sdel) { if (!confirm('Supprimer définitivement cette solution et ses commentaires ?')) return; await api.supprimerSolution(b.dataset.sdel); toast('Solution supprimée.', 'ok'); return redo(); }
      if (b.dataset.cdel) { if (!confirm('Supprimer ce commentaire ?')) return; await api.supprimerSolCom(b.dataset.cdel); return redo(); }
      if (b.dataset.sver) { const [id, v] = b.dataset.sver.split('|'); await api.majSolution(id, {verifiee: v === '1'}); return redo(); }
      if (b.dataset.smask) { const [id, v] = b.dataset.smask.split('|'); await api.majSolution(id, {statut: v}); return redo(); }
      if (b.dataset.sig) { const [t, id] = b.dataset.sig.split('|'); openSignalement(t, id); }
    } catch (x) { toast(x.message, 'error'); }
  };
}

/* ===================== MES ABONNÉS / MES ABONNEMENTS ===================== */
// Fenêtre ouverte depuis son propre profil. onChange(delta) : le compteur « suit N » du profil suit les clics.
const depuis = d => (Date.now() - Date.parse(d)) < 864e5 ? 'depuis aujourd’hui' : 'depuis le ' + new Date(d).toLocaleDateString('fr-FR', {day: 'numeric', month: 'short', year: new Date(d).getFullYear() === new Date().getFullYear() ? undefined : 'numeric'});
export function openRelations(sens = 'abonnes', onChange = () => {}) {
  const dlg = document.createElement('dialog'); dlg.className = 'dlg dlg-rel';
  const T = {abonnes: 'Mes abonnés', abonnements: 'Mes abonnements'};
  dlg.innerHTML = `<div class="dlg-in"><header><h2 id="relT">${T[sens]}</h2><button class="iconbtn" type="button" data-close aria-label="Fermer">${ic('x')}</button></header>
    <div class="rel-tabs" role="tablist">${Object.entries(T).map(([k, l]) => `<button type="button" role="tab" data-sens="${k}" aria-selected="${k === sens}">${k === 'abonnes' ? 'Abonnés' : 'Abonnements'}</button>`).join('')}</div>
    <div class="rel-body" aria-live="polite"></div></div>`;
  document.body.append(dlg);
  const body = dlg.querySelector('.rel-body');
  let L = [];
  const draw = async s => {
    sens = s; dlg.querySelector('#relT').textContent = T[s];
    dlg.querySelectorAll('[data-sens]').forEach(b => b.setAttribute('aria-selected', b.dataset.sens === s));
    body.innerHTML = `<div role="status" aria-label="Chargement">${'<span class="skel skel-item"></span>'.repeat(3)}</div>`;
    let R; try { R = await api.mesRelations(s); } catch (x) { body.innerHTML = `<p class="small">Liste indisponible : ${esc(x.message)}</p>`; return; }
    if (sens !== s) return;
    L = R.liste || [];
    const prives = R.prives ? `<p class="small rel-priv">${ic('lock')} ${R.prives === 1 ? '1 membre au profil privé' : R.prives + ' membres au profil privé'} ${s === 'abonnes' ? 'te suit' + (R.prives > 1 ? 'ent' : '') : ''} (non affiché${R.prives > 1 ? 's' : ''} par respect de leur choix).</p>` : '';
    body.innerHTML = L.length || R.prives ? `${L.length ? `<ul class="rel-list">${L.map(m => `<li><a class="cm-id" href="#u/${esc(m.username || m.id)}" data-close>${av(m.id, m.nom, m.photo)}<span><b>${esc(m.nom)}</b><span class="small">@${esc(m.username || '')}${m.filiere ? ' · ' + esc(m.filiere) : ''} · ${depuis(m.depuis)}</span></span></a>${followBtn(m.id, m.suivi)}</li>`).join('')}</ul>` : ''}${prives}`
      : `<p class="small rel-vide">${s === 'abonnes' ? 'Personne ne te suit encore. Rends ton profil public et publie une solution ou une collection pour te faire connaître.' : 'Tu ne suis personne pour l’instant. Trouve des camarades dans l’annuaire de la Communauté.'}</p>`;
    bindFollow(body, id => { const m = L.find(x => x.id === id); m.suivi = !m.suivi; onChange(m.suivi ? 1 : -1); return m; },
      m => { body.querySelector(`[data-follow="${m.id}"]`).outerHTML = followBtn(m.id, m.suivi); });
  };
  dlg.onclick = e => {
    const t = e.target.closest('[data-sens]'); if (t && t.dataset.sens !== sens) return draw(t.dataset.sens);
    if (e.target.closest('[data-close]') || e.target === dlg) dlg.close();
  };
  dlg.addEventListener('close', () => dlg.remove());
  dlg.showModal(); draw(sens);
}

/* ===================== SIGNALEMENT ===================== */
export function openSignalement(type, id) {
  const dlg = document.createElement('dialog'); dlg.className = 'dlg';
  dlg.innerHTML = `<form method="dialog" class="dlg-in"><header><h2>Signaler un contenu</h2><button class="iconbtn" value="x" aria-label="Fermer">${ic('x')}</button></header>
    <p class="small">L’administrateur examinera ce signalement. Il reste confidentiel : l’auteur ne sait pas qui l’a envoyé.</p>
    <fieldset class="types"><legend class="lab">Motif</legend>${[['spam', 'Spam ou publicité'], ['insulte', 'Propos blessants ou harcèlement'], ['inapproprie', 'Contenu inapproprié'], ['donnees', 'Données personnelles exposées'], ['autre', 'Autre']]
      .map(([k, l], i) => `<label class="chipc"><input type="radio" name="motif" value="${k}" ${i ? '' : 'checked'}><span>${l}</span></label>`).join('')}</fieldset>
    <div class="fld"><label for="sgD">Précisions <span class="small">(facultatif)</span></label><textarea id="sgD" name="details" maxlength="500" rows="3"></textarea></div>
    <p class="small">Pour une erreur mathématique dans une solution, utilise plutôt « Signaler une erreur » dans ses commentaires.</p>
    <footer><button class="btn ghost" value="x">Annuler</button><button class="btn primary" value="ok">Envoyer le signalement</button></footer></form>`;
  document.body.append(dlg);
  dlg.addEventListener('close', async () => {
    if (dlg.returnValue === 'ok') { const f = dlg.querySelector('form');
      try { await api.signaler(type, id, f.motif.value, f.details.value.trim()); toast('Signalement envoyé. Merci.', 'ok'); } catch (x) { toast(x.message, 'error'); } }
    dlg.remove();
  });
  dlg.showModal();
}

/* ===================== MODÉRATION (tableau de bord) ===================== */
export async function renderModeration(box) {
  if (!box) return;
  let L; try { L = await api.moderationFile(); } catch (x) { box.innerHTML = `<p class="small">Modération indisponible : ${esc(x.message)}</p>`; return; }
  const lib = {commentaire: 'Commentaire', solution: 'Solution d’élève', solution_commentaire: 'Commentaire de solution', profil: 'Profil', carnet: 'Page de carnet', collection: 'Collection', corrige: 'Erreur dans une correction'};
  const motif = {spam: 'spam', insulte: 'propos blessants', inapproprie: 'inapproprié', donnees: 'données personnelles', autre: 'autre', erreur: 'erreur scientifique'};
  box.innerHTML = L.length ? `<ul class="mod-list">${L.map(s => { const ex = s.exercice && D.byId(s.exercice);
    const voir = s.cible_type === 'profil' ? `#u/${esc(s.cible_id)}` : s.cible_type === 'collection' ? `#c/${esc(s.cible_id)}` : ex ? `#ex-${esc(ex.id)}` : '';
    return `<li class="mod"><div><b>${lib[s.cible_type] || s.cible_type}</b> <span class="lab-err">${plural(s.n, 'signalement')}</span> <span class="small">${(s.motifs || []).map(m => motif[m] || m).join(', ')} · ${ago(s.dernier)}</span>
      ${s.cible_type === 'corrige' ? `<p class="small">Exercice : ${esc(ex?.titre || s.cible_id)}</p>` : s.extrait ? `<blockquote class="cm-ex">${esc(s.extrait)}</blockquote>` : '<p class="small">Contenu déjà supprimé.</p>'}${(s.details || []).length ? `<p class="small">Précisions : ${s.details.map(esc).join(' · ')}</p>` : ''}</div>
      <div class="mod-act">${voir ? `<a class="btn ghost" href="${voir}">${ic('eye')} Voir</a>` : ''}
        ${s.cible_type === 'solution' ? `<button class="btn" data-mod="${esc(s.cible_type)}|${esc(s.cible_id)}|retablir">Rétablir</button>` : ''}
        ${s.cible_type === 'corrige' ? '' : `<button class="btn red" data-mod="${esc(s.cible_type)}|${esc(s.cible_id)}|supprimer">`}${s.cible_type === 'corrige' ? '' : `${s.cible_type === 'profil' ? 'Rendre privé et vider' : 'Supprimer'}</button>`}
        <button class="btn ghost" data-mod="${esc(s.cible_type)}|${esc(s.cible_id)}|classer">${s.cible_type === 'corrige' ? 'Traité' : 'Classer sans suite'}</button></div></li>`; }).join('')}</ul>`
    : '<p class="small">Aucun signalement en attente.</p>';
  box.onclick = async e => { const b = e.target.closest('[data-mod]'); if (!b) return;
    const [t, id, a] = b.dataset.mod.split('|');
    if (a === 'supprimer' && !confirm('Confirmer la suppression définitive de ce contenu ?')) return;
    try { await api.moderer(t, id, a); toast('Décision enregistrée.', 'ok'); renderModeration(box); } catch (x) { toast(x.message, 'error'); } };
}
