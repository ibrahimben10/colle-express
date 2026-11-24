// Carnet de progression (privé par défaut) et objectifs personnels.
// Les objectifs progressent UNIQUEMENT avec l'activité réelle, calculée par le serveur.
import { api } from './api.js';
import { ic } from './icons.js';
import { esc, rich } from './format.js';
import { toast } from './ui.js';
import { DOMAINES } from './profil.js';

let D = {};   // byId, all, typeset, current() (exercice ouvert)
export const initCarnet = deps => { D = deps; };

export const TYPES = {
  appris:   {l: 'Ce que j’ai appris', c: 'green', i: 'check'},
  difficile:{l: 'Exercice difficile', c: 'amber', i: 'target'},
  refaire:  {l: 'À refaire', c: 'cyan', i: 'clock'},
  erreur:   {l: 'Erreur fréquente', c: 'red', i: 'x'},
  theoreme: {l: 'Théorème à revoir', c: 'blue', i: 'book'},
  demo:     {l: 'Démonstration', c: 'violet', i: 'pen'},
  note:     {l: 'Note de révision', c: 'ink', i: 'msg'},
};
const OBJ = {
  exercices: {l: 'Travailler des exercices', u: 'exercices travaillés'},
  chapitres: {l: 'Réviser des chapitres', u: 'chapitres abordés'},
  refaire:   {l: 'Refaire des exercices de mon carnet', u: 'exercices refaits (notés « à refaire » ou « difficile »)'},
  autonomie: {l: 'Gagner en autonomie', u: 'réponses soumises sans aide'},
};
const PRESETS = [
  {t: 'exercices', cible: 10, j: 7, titre: 'Travailler 10 exercices cette semaine'},
  {t: 'chapitres', cible: 3, j: 14, dom: 'Analyse', titre: 'Réviser 3 chapitres d’analyse'},
  {t: 'refaire', cible: 5, j: 14, titre: 'Refaire 5 exercices difficiles'},
  {t: 'autonomie', cible: 5, j: 14, titre: '5 réponses sans aide'},
  {t: 'exercices', cible: 6, j: 10, dom: 'Électromagnétisme', titre: 'Préparer ma colle d’électromagnétisme'},
];
const iso = d => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;   // date locale (pas UTC)
const today = () => iso(new Date());
const plusJ = n => { const d = new Date(); d.setDate(d.getDate() + n); return iso(d); };
const dateFR = d => new Date(d.length === 10 ? d + 'T12:00' : d).toLocaleDateString('fr-FR', {day: 'numeric', month: 'long'});
const fmtJ = d => { const n = Math.round((new Date(d + 'T12:00') - new Date(today() + 'T12:00')) / 864e5); return n < 0 ? 'terminé' : n === 0 ? 'dernier jour' : n === 1 ? 'encore 1 jour' : `encore ${n} jours`; };

/* ===================== PAGE CARNET ===================== */
let F = {type: '', q: ''}, NOTES = [], OBJS = [];
export async function renderCarnet(el) {
  el.innerHTML = `<div class="panel"><span class="skel skel-h"></span><span class="skel skel-card"></span></div>`;
  try { [NOTES, OBJS] = await Promise.all([api.monCarnet(), api.mesObjectifs()]); }
  catch (e) { el.innerHTML = `<div class="panel empty">Carnet indisponible : la base de données doit être mise à jour (README, section Carnet).</div>`; return; }
  draw(el);
}
function draw(el) {
  const appris = NOTES.filter(n => n.type === 'appris'), autres = NOTES.filter(n => n.type !== 'appris');
  const counts = Object.fromEntries(Object.keys(TYPES).map(k => [k, NOTES.filter(n => n.type === k).length]));
  const actifs = OBJS.filter(o => !o.archive), archives = OBJS.filter(o => o.archive);
  el.innerHTML = `<div class="cn">
    <header class="cn-head"><div><p class="pf-kicker">Privé par défaut</p><h1>Carnet de progression</h1>
      <p class="cn-sub">Tes objectifs, ce que tu as compris, tes erreurs, les exercices à refaire. Personne d’autre ne le lit, sauf les notes que tu choisis de publier sur ton profil.</p></div>
      <button class="btn primary" type="button" data-new="note">${ic('plus')} Nouvelle note</button></header>

    <section class="cn-sec"><header class="pf-sh"><span class="pf-num">§1</span><h2>Objectifs du moment</h2><span class="pf-note">progression calculée sur ton activité réelle</span></header>
      <div class="obj-list">${actifs.map(objHTML).join('') || '<p class="pf-emptyline">Aucun objectif en cours. Un objectif modeste et précis aide plus qu’un grand objectif flou.</p>'}</div>
      <details class="obj-new"${actifs.length ? '' : ' open'}><summary>${ic('target')} Fixer un objectif</summary>${objFormHTML()}</details>
      ${archives.length ? `<details class="obj-arch"><summary>Objectifs archivés (${archives.length})</summary><div class="obj-list">${archives.map(objHTML).join('')}</div></details>` : ''}
    </section>
    <div class="pf-rule" aria-hidden="true">∎</div>

    <section class="cn-sec"><header class="pf-sh"><span class="pf-num">§2</span><h2>Ce que j’ai appris</h2><span class="pf-note">tes acquis, avec tes mots</span></header>
      <form class="learn-add" id="learnAdd"><label class="sr" for="learnT">Ce que j’ai appris</label><input id="learnT" maxlength="120" placeholder="Ex. : une série entière se dérive terme à terme sur son disque ouvert"><button class="btn" type="submit">${ic('plus')} Ajouter</button></form>
      <ol class="learn">${appris.map(n => `<li data-id="${esc(n.id)}"><span class="learn-ic">${ic('check')}</span><div><b>${esc(n.titre)}</b>${n.contenu ? `<div class="cn-rich">${rich(n.contenu)}</div>` : ''}
        <span class="small">${dateFR(n.created_at)}${n.exercice_id ? ` · <a href="#ex-${esc(n.exercice_id)}">${esc(D.byId(n.exercice_id)?.titre || 'exercice')}</a>` : ''}${n.public ? ' · <span class="badge pub">Public</span>' : ''}</span></div>
        <span class="cn-act"><button class="linkbtn" data-edit="${esc(n.id)}">Modifier</button><button class="linkbtn danger" data-del="${esc(n.id)}">Supprimer</button></span></li>`).join('') || '<li class="pf-emptyline">Rien encore. Après chaque exercice, note en une phrase ce que tu retiens.</li>'}</ol>
    </section>
    <div class="pf-rule" aria-hidden="true">∎</div>

    <section class="cn-sec"><header class="pf-sh"><span class="pf-num">§3</span><h2>Pages du carnet</h2><span class="pf-note">${autres.length} note${autres.length > 1 ? 's' : ''}</span></header>
      <div class="cn-tools"><div class="cn-filt" role="group" aria-label="Filtrer par type"><button type="button" data-ft="" aria-pressed="${!F.type}">Tout</button>${Object.entries(TYPES).filter(([k]) => k !== 'appris').map(([k, t]) => `<button type="button" data-ft="${k}" aria-pressed="${F.type === k}" class="t-${t.c}">${t.l}${counts[k] ? ` <span>${counts[k]}</span>` : ''}</button>`).join('')}</div>
        <label class="sr" for="cnQ">Rechercher</label><input id="cnQ" type="search" placeholder="Rechercher dans le carnet…" value="${esc(F.q)}"></div>
      <div class="cn-pages">${pagesHTML(autres)}</div>
    </section>
  </div>`;
  bind(el);
  D.typeset?.([...el.querySelectorAll('.cn-rich')]);
}
function pagesHTML(L) {
  const q = F.q.toLowerCase();
  const v = L.filter(n => (!F.type || n.type === F.type) && (!q || (n.titre + ' ' + n.contenu).toLowerCase().includes(q)));
  if (!v.length) return `<p class="pf-emptyline">${L.length ? 'Aucune note ne correspond.' : 'Ton carnet est vide. Depuis un exercice, le bouton « Carnet » garde une trace d’une difficulté, d’une erreur ou d’un exercice à refaire.'}</p>`;
  return v.map(n => { const t = TYPES[n.type] || TYPES.note, e = n.exercice_id && D.byId(n.exercice_id);
    return `<article class="cn-page t-${t.c}" data-id="${esc(n.id)}"><div class="cn-tag">${ic(t.i)} ${t.l}</div>
      <h3>${esc(n.titre)}</h3>${n.contenu ? `<div class="cn-rich">${rich(n.contenu)}</div>` : ''}
      <footer><span class="small">${dateFR(n.created_at)}${e ? ` · <a href="#ex-${esc(e.id)}">${esc(e.titre)}</a>` : ''}${n.public ? ` · <span class="badge pub">${ic('users')} Public</span>` : ` · ${ic('lock')} privé`}</span>
        <span class="cn-act"><button class="linkbtn" data-edit="${esc(n.id)}">Modifier</button><button class="linkbtn danger" data-del="${esc(n.id)}">Supprimer</button></span></footer></article>`; }).join('');
}
function objHTML(o) {
  const v = Math.min(o.progression || 0, o.cible), pct = Math.round(100 * v / o.cible), fini = o.fin < today(), ok = (o.progression || 0) >= o.cible;
  const etat = ok ? `<span class="obj-ok">${ic('check')} Objectif atteint</span>` : fini ? `<span class="small">Période terminée : ${o.progression || 0}/${o.cible}. Chaque exercice travaillé compte ; tu peux en fixer un nouveau.</span>` : `<span class="small">${fmtJ(o.fin)}</span>`;
  return `<article class="obj ${ok ? 'done' : ''}" data-id="${esc(o.id)}">
    <div class="obj-top"><h3>${esc(o.titre)}</h3><span class="obj-n"><b>${o.progression || 0}</b>/${o.cible}</span></div>
    <div class="obj-bar" role="progressbar" aria-valuemin="0" aria-valuemax="${o.cible}" aria-valuenow="${v}" aria-label="${esc(o.titre)}"><i style="width:${pct}%"></i></div>
    <div class="obj-meta"><span class="small">${OBJ[o.type]?.u || ''}${o.domaine ? ' · ' + esc(o.domaine) : ''} · du ${dateFR(o.debut)} au ${dateFR(o.fin)}</span>${etat}</div>
    <div class="obj-act"><label class="mini-tg"><input type="checkbox" data-share="${esc(o.id)}" ${o.partage ? 'checked' : ''}> Afficher sur mon profil</label>
      ${o.archive ? `<button class="linkbtn" data-unarch="${esc(o.id)}">Désarchiver</button>` : `<button class="linkbtn" data-arch="${esc(o.id)}">Archiver</button>`}<button class="linkbtn danger" data-delo="${esc(o.id)}">Supprimer</button></div></article>`;
}
function objFormHTML() {
  return `<form class="obj-form" id="objForm" novalidate>
    <div class="presets" role="group" aria-label="Idées d’objectifs">${PRESETS.map((p, i) => `<button type="button" class="chipbtn" data-preset="${i}">${esc(p.titre)}</button>`).join('')}</div>
    <div class="frow3">
      <div class="fld"><label for="ofType">Type</label><select id="ofType" name="type">${Object.entries(OBJ).map(([k, o]) => `<option value="${k}">${o.l}</option>`).join('')}</select></div>
      <div class="fld"><label for="ofCible">Nombre visé</label><input id="ofCible" name="cible" type="number" min="1" max="200" value="10" inputmode="numeric"></div>
      <div class="fld"><label for="ofDom">Domaine <span class="small">(facultatif)</span></label><select id="ofDom" name="domaine"><option value="">Tous</option>${DOMAINES.filter(d => d !== 'Informatique').map(d => `<option>${esc(d)}</option>`).join('')}</select></div>
    </div>
    <div class="frow3">
      <div class="fld" style="grid-column:span 2"><label for="ofTitre">Intitulé</label><input id="ofTitre" name="titre" maxlength="140" placeholder="Ex. : préparer ma colle de jeudi"></div>
      <div class="fld"><label for="ofFin">Jusqu’au</label><input id="ofFin" name="fin" type="date" min="${today()}" max="${plusJ(180)}" value="${plusJ(7)}"></div>
    </div>
    <label class="mini-tg"><input type="checkbox" name="partage"> Afficher cet objectif sur mon profil</label>
    <p class="small">La progression se met à jour toute seule avec les exercices que tu travailles (indice demandé ou réponse soumise). Rien à cocher à la main.</p>
    <div class="alert" id="ofErr" hidden></div>
    <button class="btn primary" type="submit">${ic('target')} Fixer l’objectif</button></form>`;
}

function bind(el) {
  const reload = async () => { [NOTES, OBJS] = await Promise.all([api.monCarnet(), api.mesObjectifs()]); draw(el); };
  el.querySelector('[data-new]').onclick = () => openNote({}, reload);
  // filtres
  el.querySelectorAll('[data-ft]').forEach(b => b.onclick = () => { F.type = b.dataset.ft; draw(el); });
  const q = el.querySelector('#cnQ'); q.oninput = () => { F.q = q.value; el.querySelector('.cn-pages').innerHTML = pagesHTML(NOTES.filter(n => n.type !== 'appris')); D.typeset?.([...el.querySelectorAll('.cn-pages .cn-rich')]); };
  // ce que j'ai appris (ajout rapide)
  el.querySelector('#learnAdd').onsubmit = async e => { e.preventDefault(); const t = el.querySelector('#learnT').value.trim(); if (!t) return;
    try { await api.noteCarnet({type: 'appris', titre: t}); toast('Ajouté à ce que tu as appris.', 'ok'); await reload(); el.querySelector('#learnT')?.focus(); } catch (x) { toast(x.message, 'error'); } };
  // modifier / supprimer des notes
  el.addEventListener('click', async e => {
    const b = e.target.closest('button'); if (!b) return;
    if (b.dataset.edit) openNote(NOTES.find(n => n.id === b.dataset.edit), reload);
    if (b.dataset.del && confirm('Supprimer définitivement cette note du carnet ?')) { try { await api.supprimerNote(b.dataset.del); await reload(); } catch (x) { toast(x.message, 'error'); } }
    if (b.dataset.arch || b.dataset.unarch) { try { await api.majObjectif(b.dataset.arch || b.dataset.unarch, {archive: !!b.dataset.arch}); await reload(); } catch (x) { toast(x.message, 'error'); } }
    if (b.dataset.delo && confirm('Supprimer cet objectif ?')) { try { await api.supprimerObjectif(b.dataset.delo); await reload(); } catch (x) { toast(x.message, 'error'); } }
  });
  el.querySelectorAll('[data-share]').forEach(c => c.onchange = async () => { try { await api.majObjectif(c.dataset.share, {partage: c.checked}); toast(c.checked ? 'Objectif affiché sur ton profil.' : 'Objectif retiré de ton profil.', 'ok'); } catch (x) { c.checked = !c.checked; toast(x.message, 'error'); } });
  // objectif : formulaire
  const f = el.querySelector('#objForm'); if (!f) return;
  let titreAuto = true;
  const autoTitre = () => { if (!titreAuto) return; const n = +f.cible.value || 0, d = f.domaine.value;
    f.titre.value = {exercices: `Travailler ${n} exercice${n > 1 ? 's' : ''}${d ? ' de ' + d.toLowerCase() : ''}`, chapitres: `Réviser ${n} chapitre${n > 1 ? 's' : ''}${d ? ' de ' + d.toLowerCase() : ''}`,
      refaire: `Refaire ${n} exercice${n > 1 ? 's' : ''} de mon carnet`, autonomie: `${n} réponse${n > 1 ? 's' : ''} sans aide${d ? ' en ' + d.toLowerCase() : ''}`}[f.type.value]; };
  autoTitre();
  f.titre.oninput = () => { titreAuto = !f.titre.value; };
  [f.type, f.cible, f.domaine].forEach(x => x.addEventListener('input', autoTitre));
  f.querySelectorAll('[data-preset]').forEach(b => b.onclick = () => { const p = PRESETS[+b.dataset.preset];
    f.type.value = p.t; f.cible.value = p.cible; f.domaine.value = p.dom || ''; f.fin.value = plusJ(p.j); f.titre.value = p.titre; titreAuto = false; });
  let busy = false;
  f.onsubmit = async e => { e.preventDefault(); if (busy) return;
    const err = f.querySelector('#ofErr'), cible = +f.cible.value, fin = f.fin.value;
    const bad = m => { err.hidden = false; err.className = 'alert error'; err.textContent = m; };
    if (!(cible >= 1 && cible <= 200)) return bad('Nombre visé : entre 1 et 200.');
    if (!fin || fin < today() || fin > plusJ(180)) return bad('Date de fin : entre aujourd’hui et dans 6 mois.');
    if (!f.titre.value.trim()) return bad('Donne un intitulé à ton objectif.');
    busy = true;
    try { await api.creerObjectif({type: f.type.value, cible, domaine: f.domaine.value, fin, titre: f.titre.value.trim(), partage: f.partage.checked}); toast('Objectif fixé. Bon courage !', 'ok'); await reload(); }
    catch (x) { bad(x.message); } finally { busy = false; }
  };
}

/* ===================== NOTE : création / modification ===================== */
export function openNote(n = {}, after) {
  const ex = n.exercice_id ? D.byId(n.exercice_id) : null;
  const dlg = document.createElement('dialog'); dlg.className = 'dlg';
  dlg.innerHTML = `<form method="dialog" class="dlg-in" novalidate>
    <header><h2>${n.id ? 'Modifier la note' : 'Ajouter au carnet'}</h2><button class="iconbtn" value="x" aria-label="Fermer">${ic('x')}</button></header>
    ${ex ? `<p class="small">${ic('book')} Liée à l’exercice <b>${esc(ex.titre)}</b></p>` : ''}
    <fieldset class="types"><legend class="lab">Type</legend>${Object.entries(TYPES).map(([k, t]) => `<label class="chipc t-${t.c}"><input type="radio" name="type" value="${k}" ${(n.type || 'note') === k ? 'checked' : ''}><span>${ic(t.i)} ${t.l}</span></label>`).join('')}</fieldset>
    <div class="fld"><label for="nTitre">Titre</label><input id="nTitre" name="titre" maxlength="120" value="${esc(n.titre || '')}" required></div>
    <div class="fld"><label for="nTxt">Contenu <span class="small">(formules entre $…$)</span></label><textarea id="nTxt" name="contenu" maxlength="8000" rows="6">${esc(n.contenu || '')}</textarea></div>
    <details class="nprev"><summary>Aperçu</summary><div class="cn-rich" id="nPrev"></div></details>
    <label class="mini-tg"><input type="checkbox" name="public" ${n.public ? 'checked' : ''}> Publier cette note sur mon profil <span class="small">(sinon, elle reste privée)</span></label>
    <p class="err" id="nErr"></p>
    <footer><button class="btn ghost" value="x">Annuler</button><button class="btn primary" value="ok" id="nOk">Enregistrer</button></footer></form>`;
  document.body.append(dlg);
  const f = dlg.querySelector('form');
  dlg.querySelector('.nprev').addEventListener('toggle', () => { const p = dlg.querySelector('#nPrev'); p.innerHTML = rich(f.contenu.value || '—'); D.typeset?.([p]); });
  dlg.addEventListener('close', async () => {
    if (dlg.returnValue === 'ok') {
      try { await api.noteCarnet({id: n.id, type: f.type.value, titre: f.titre.value.trim(), contenu: f.contenu.value.trim(), exercice_id: n.exercice_id || null, public: f.public.checked});
        toast(n.id ? 'Note mise à jour.' : 'Ajouté à ton carnet.', 'ok'); after?.(); }
      catch (x) { toast(x.message, 'error'); }
    }
    dlg.remove();
  });
  f.addEventListener('submit', e => { if (e.submitter?.value === 'ok' && !f.titre.value.trim()) { e.preventDefault(); dlg.querySelector('#nErr').textContent = 'Donne un titre à ta note.'; f.titre.focus(); } });
  dlg.showModal();
  (n.titre ? f.contenu : f.titre).focus();
}
