// Profils personnels : page « carnet » (#u/identifiant), édition et confidentialité.
// Toutes les données viennent du serveur (fonction profil_public) qui applique la confidentialité ;
// rien n'est inventé : une section sans données affiche un état vide.
import { bannerSVG } from './vivant.js';
import { api } from './api.js';
import { ic } from './icons.js';
import { esc, rich } from './format.js';
import { toast } from './ui.js';
import { collectionsHTML, nouvelleCollection } from './biblio.js';
import { TYPES } from './carnet.js';
import { followBtn, bindFollow, openSignalement } from './communaute.js';

let D = {};   // dépendances fournies par app.js : byId, all, LV, MAT_IC, typeset, pickPhoto, ensurePhoto
export const initProfil = deps => { D = deps; };

export const FILIERES = ['MPSI', 'MP2I', 'MP', 'MP*', 'PCSI', 'PC', 'PC*', 'PSI', 'PSI*', 'PT', 'PT*', 'TSI', 'BCPST', 'Autre'];
export const DOMAINES = ['Analyse', 'Algèbre', 'Probabilités', 'Mécanique', 'Électromagnétisme', 'Thermodynamique', 'Optique & ondes', 'Physique quantique', 'Chimie', 'Informatique'];

// Domaine scientifique d'un exercice, à partir de sa matière et de son chapitre
export function domaine(ex) {
  if (!ex) return 'Autre';
  const c = ex.chap || '';
  if (ex.mat === 'Chimie') return 'Chimie';
  if (ex.mat === 'Maths') {
    if (/proba/i.test(c)) return 'Probabilités';
    if (/réduction|algèbre|groupe|arithm|polyn|déterminant|matric|espaces? vect/i.test(c)) return 'Algèbre';
    return 'Analyse';
  }
  if (/quantique/i.test(c)) return 'Physique quantique';
  if (/thermo|diffusion|statistique/i.test(c)) return 'Thermodynamique';
  if (/optique|ondes méca|ondes mécaniques|interf|diffraction/i.test(c)) return 'Optique & ondes';
  if (/électro|induction|maxwell|magnét|rayonnement|ondes électromagn/i.test(c)) return 'Électromagnétisme';
  if (/méca|fluide|gravit|référentiel/i.test(c)) return 'Mécanique';
  return 'Mécanique';
}

const initials = n => (n || '?').split(/\s+/).filter(Boolean).slice(0, 2).map(w => w[0].toUpperCase()).join('');
const hue = s => { let h = 0; for (const c of String(s)) h = (h * 31 + c.charCodeAt(0)) % 360; return h; };
const okPhoto = ph => /^data:image\/(jpeg|png|webp);base64,[A-Za-z0-9+/=]+$/.test(ph || '');
const dateFR = (d, o = {day: 'numeric', month: 'long', year: 'numeric'}) => new Date(d).toLocaleDateString('fr-FR', o);
const plural = (n, s, p = s + 's') => `${n} ${n > 1 ? p : s}`;
const ymd = d => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
export const profilURL = p => `#u/${encodeURIComponent(p?.username || p?.id || '')}`;

/* ===================== PAGE PROFIL ===================== */
export async function renderProfil(el, ref, {apercu = false} = {}) {
  el.innerHTML = `<div class="pf-skel" role="status" aria-label="Chargement du profil"><span class="skel" style="width:96px;height:96px;border-radius:50%"></span><span class="skel skel-h"></span><span class="skel skel-l w60"></span><span class="skel skel-card"></span></div>`;
  let p;
  try { p = await api.profilPublic(ref, apercu); }
  catch (e) { el.innerHTML = `<div class="panel empty">Impossible de charger ce profil pour le moment.</div>`; return; }
  if (!p) { el.innerHTML = `<div class="panel pf-missing"><h2>Profil introuvable</h2><p class="small">Cet identifiant n’existe pas, ou le compte a été supprimé.</p><a class="btn" href="#exercices">Retour aux exercices</a></div>`; return; }
  if (p.prive) {
    el.innerHTML = `<div class="panel pf-missing">${avatarXL(p)}<h2>${esc(p.nom || 'Profil privé')}</h2><p class="small">@${esc(p.username || '')} · Ce profil est privé : seuls son auteur et l’administrateur peuvent le voir.</p><a class="btn" href="#exercices">Retour aux exercices</a></div>`;
    return;
  }
  const S = stats(p), sections = [];
  let n = 0; const sec = (id, titre, html, note = '') => { n++; sections.push(`<section class="pf-sec" id="pf-${id}" aria-labelledby="pf-${id}-t">
    <header class="pf-sh"><span class="pf-num">${String(n).padStart(2,"0")}</span><h2 id="pf-${id}-t">${titre}</h2>${note ? `<span class="pf-note">${note}</span>` : ''}</header>${html}</section>`); };

  if (p.travailles) sec('stats', 'En chiffres', statsHTML(S, p), 'activité réelle, comptée depuis l’inscription');
  if (p.jours) sec('activite', 'Carte d’activité', heatHTML(p.jours), 'jours où des exercices ont été travaillés');
  if (p.travailles) sec('parcours', 'Parcours scientifique', parcoursHTML(p), 'couverture des chapitres, pas un niveau de maîtrise');
  if (p.favoris || p.collections) sec('favoris', 'Bibliothèque', (p.collections ? `<h3 class="pf-h3">Collections ${p.self ? `<button class="btn ghost" type="button" id="pfNewColl">${ic('plus')} Nouvelle collection</button>` : ''}</h3>${collectionsHTML(p.collections, p.self)}` : '')
    + (p.favoris ? `<h3 class="pf-h3">Exercices favoris</h3>${favorisHTML(p.favoris, p.self)}` : ''));
  if (p.solutions && (p.solutions.length || p.self)) sec('solutions', 'Solutions publiées', solutionsHTML(p.solutions, p.self), 'rédigées par l’élève, non vérifiées sauf mention');
  if (p.carnet && (p.carnet.length || p.self)) sec('carnet', 'Pages du carnet', carnetPublicHTML(p.carnet, p.self), 'notes publiées volontairement');
  if (p.badges && (p.badges.length || p.self)) sec('badges', 'Réalisations', badgesHTML(p.badges, p.self), 'critères publics et vérifiables');
  if (p.commentaires) sec('paroles', 'Commentaires publics', parolesHTML(p.commentaires));

  el.innerHTML = `
    ${apercu ? `<div class="pf-preview" role="status">${ic('eye')} Aperçu : voici ce que voient les autres membres. <a href="#profil">Revenir à mon profil</a></div>` : ''}
    <article class="pf" style="--h:${hue(p.id)}">
      ${bannerSVG(p.username || p.nom || '')}
      <header class="pf-head">
        <div class="pf-margin" aria-hidden="true"><span>∑</span><span>∫</span><span>∂</span></div>
        ${avatarXL(p)}
        <div class="pf-id">
          <p class="pf-kicker">${p.role === 'admin' ? 'Administrateur · ' : ''}${[p.filiere, p.annee ? p.annee + (p.annee === 1 ? 're' : 'e') + ' année' : '', p.etablissement].filter(Boolean).map(esc).join(' · ') || 'Membre de Colle express'}</p>
          <h1>${esc(p.nom || 'Membre')}</h1>
          <p class="pf-user">@${esc(p.username || '')}<span>· membre depuis ${dateFR(p.membre_depuis, {month: 'long', year: 'numeric'})}</span>${p.abonnes != null ? `<span>· <b>${p.abonnes}</b> abonné${p.abonnes > 1 ? 's' : ''} · suit <b>${p.abonnements}</b></span>` : ''}</p>
          ${p.bio ? `<p class="pf-bio">${esc(p.bio)}</p>` : p.self ? `<p class="pf-bio empty-bio">Ajoute une courte présentation : ce que tu prépares, ce que tu aimes en sciences…</p>` : ''}
          ${p.matieres?.length ? `<ul class="pf-tags" aria-label="Matières préférées">${p.matieres.map(m => `<li>${esc(m)}</li>`).join('')}</ul>` : ''}
          ${liensHTML(p.liens)}
        </div>
        <div class="pf-side">
          ${p.etoiles ? starsHTML(p) : ''}
          ${p.objectif ? `<div class="pf-goal"><span>Objectif du moment</span><p>${esc(p.objectif)}</p></div>` : ''}
          ${(p.objectifs || []).slice(0, 3).map(o => { const v = Math.min(o.progression || 0, o.cible);
            return `<div class="pf-goal pf-goal2"><span>Objectif · jusqu’au ${dateFR(o.fin + 'T12:00', {day: 'numeric', month: 'short'})}</span><p>${esc(o.titre)}</p>
              <div class="obj-bar" role="progressbar" aria-valuemin="0" aria-valuemax="${o.cible}" aria-valuenow="${v}" aria-label="${esc(o.titre)}"><i style="width:${Math.round(100 * v / o.cible)}%"></i></div><small>${o.progression || 0}/${o.cible}${(o.progression || 0) >= o.cible ? ' · atteint' : ''}</small></div>`; }).join('')}
          ${p.contributions ? `<div class="pf-contrib">${ic('upload')} ${plural(p.contributions, 'sujet envoyé', 'sujets envoyés')} pour enrichir la plateforme</div>` : ''}
        </div>
      </header>
      <div class="pf-bar">
        ${p.self ? `<span class="pf-vis ${p.public ? 'on' : ''}">${ic(p.public ? 'users' : 'lock')} ${p.public ? 'Visible par les membres connectés' : 'Privé : visible par toi seul'}</span>
          <a class="btn primary" href="#profil/modifier">${ic('pen')} Modifier</a>
          <a class="btn" href="#profil/apercu">${ic('eye')} Voir comme les autres</a><a class="btn ghost" href="#carnet">${ic('pen')} Carnet</a><a class="btn ghost" href="#suivi">${ic('chart')} Suivi détaillé</a>` : ''}
        ${!p.self && p.public && p.abonnes != null ? followBtn(p.id, p.je_suis) : ''}
        ${p.self && p.admin ? `<a class="btn ghost" href="#prof">${ic('live')} Tableau de bord</a>` : ''}
        <button class="btn ghost" type="button" id="pfShare">${ic('link')} Copier le lien</button>
        ${!p.self ? `<button class="linkbtn" type="button" id="pfSig">Signaler ce profil</button>` : ''}
      </div>
      ${sections.join('<div class="pf-rule" aria-hidden="true">∎</div>') || `<div class="panel empty">${p.self ? 'Tout est masqué pour l’instant.' : 'Ce membre n’affiche pas encore d’activité.'}</div>`}
      ${p.admin && !p.self && p.etoiles ? `<details class="pf-mod"><summary>${ic('key')} Modération des étoiles</summary><div id="pfMod" class="small">Chargement…</div></details>` : ''}
    </article>`;
  bindProfil(el, p);
  D.typeset?.([...el.querySelectorAll('.pf-quote')]);
}

function avatarXL(p) {
  return okPhoto(p.photo) ? `<img class="pf-av" src="${p.photo}" alt="">` : `<span class="pf-av" style="background:hsl(${hue(p.id)} 55% 42%)" aria-hidden="true">${esc(initials(p.nom))}</span>`;
}
function liensHTML(l = {}) {
  const L = [['github', 'GitHub'], ['linkedin', 'LinkedIn'], ['site', 'Site']].filter(([k]) => /^https:\/\//.test(l[k] || ''));
  return L.length ? `<p class="pf-links">${L.map(([k, n]) => `<a href="${esc(l[k])}" target="_blank" rel="noopener nofollow ugc">${ic('link')} ${n}</a>`).join('')}</p>` : '';
}

/* ---------- statistiques ---------- */
function stats(p) {
  const days = (p.jours || []).map(j => j.j).sort();
  const set = new Set(days);
  let serie = 0; const d = new Date();
  if (!set.has(ymd(d))) d.setDate(d.getDate() - 1);   // la série reste valable jusqu'à la fin de la journée
  while (set.has(ymd(d))) { serie++; d.setDate(d.getDate() - 1); }
  const doms = new Set((p.travailles || []).map(id => domaine(D.byId(id))).filter(x => x !== 'Autre'));
  return {vus: (p.vus || []).length, travailles: (p.travailles || []).length, termines: (p.termines || []).length, sansAide: (p.sans_aide || []).length,
    reussis: (p.reussis || []).length, favoris: (p.favoris || []).length, domaines: doms.size, jours: days.length, serie};
}
function statsHTML(S, p) {
  const big = [['travailles', 'travaillés'], ['termines', 'terminés'], ['reussis', 'réussis'], ['sansAide', 'sans aide']];
  const small = [['vus', 'consultés'], ['domaines', 'domaines'], ...(p.jours ? [['jours', 'jours actifs'], ['serie', 'jours d’affilée']] : []), ...(p.favoris ? [['favoris', 'favoris']] : [])];
  if (!S.travailles && !S.vus) return `<div class="pf-emptyline">${p.self ? `Aucun exercice travaillé pour l’instant. <a href="#exercices">Commence par une colle courte →</a>` : 'Pas encore d’exercice travaillé.'}</div>`;
  return `<div class="pf-figs">${big.map(([k, l]) => `<div class="pf-fig"><b>${S[k]}</b><span>${l}</span></div>`).join('')}</div>
    <p class="pf-figs2">${small.map(([k, l]) => `<span><b>${S[k]}</b> ${l}</span>`).join('<i aria-hidden="true">·</i>')}</p>
    <details class="pf-def"><summary>Comment ces nombres sont-ils comptés ?</summary><dl>
      <dt>Consulté</dt><dd>l’énoncé a été ouvert.</dd>
      <dt>Travaillé</dt><dd>un indice a été demandé ou une réponse soumise.</dd>
      <dt>Terminé</dt><dd>une réponse a été soumise sur l’honneur dans un groupe.</dd>
      <dt>Réussi</dt><dd>cette réponse a reçu au moins 2 notes de camarades, avec une moyenne d’au moins 12/20. Ouvrir le corrigé ne compte jamais comme une réussite.</dd>
      <dt>Sans aide</dt><dd>réponse soumise sans avoir consulté d’indice ni le corrigé avant.</dd></dl></details>`;
}

/* ---------- carte d'activité ---------- */
function heatHTML(jours) {
  const map = new Map(jours.map(j => [j.j, j.ids || []]));
  const end = new Date(); end.setHours(12, 0, 0, 0);
  const start = new Date(end); start.setDate(start.getDate() - 364);
  start.setDate(start.getDate() - ((start.getDay() + 6) % 7));   // commence un lundi
  const lvl = n => n === 0 ? 0 : n === 1 ? 1 : n === 2 ? 2 : n <= 4 ? 3 : 4;
  let cells = '', months = '', w = 0, lastM = -1, total = 0;
  for (const d = new Date(start); d <= end; d.setDate(d.getDate() + 1)) {
    const k = ymd(d), n = (map.get(k) || []).length, wd = (d.getDay() + 6) % 7;
    if (wd === 0) { if (d.getMonth() !== lastM && d.getDate() <= 7) { months += `<span style="grid-column:${w + 1}">${d.toLocaleDateString('fr-FR', {month: 'short'}).replace('.', '')}</span>`; lastM = d.getMonth(); } w++; }
    total += n;
    cells += `<button type="button" class="hm-c l${lvl(n)}" style="grid-column:${w};grid-row:${wd + 1}" data-d="${k}" aria-label="${dateFR(d)} : ${n ? plural(n, 'exercice travaillé', 'exercices travaillés') : 'aucune activité'}"${n ? '' : ' tabindex="-1"'}></button>`;
  }
  if (!total) return `<div class="pf-emptyline">Aucune activité sur les douze derniers mois.</div>`;
  return `<div class="hm-wrap" tabindex="0" aria-label="Carte d’activité des 12 derniers mois"><div class="hm-months" style="grid-template-columns:repeat(${w},var(--hm))">${months}</div>
      <div class="hm" style="grid-template-columns:repeat(${w},var(--hm))">${cells}</div></div>
    <div class="hm-foot"><span class="small">${plural(map.size, 'jour actif', 'jours actifs')} sur 12 mois · un exercice compte une fois par jour · l’activité n’est pas une mesure de maîtrise</span>
      <span class="hm-leg" aria-hidden="true">moins <i class="hm-c l0"></i><i class="hm-c l1"></i><i class="hm-c l2"></i><i class="hm-c l3"></i><i class="hm-c l4"></i> plus</span></div>
    <div class="hm-day" id="hmDay" aria-live="polite"></div>`;
}

/* ---------- parcours par domaine ---------- */
function parcoursHTML(p) {
  const T = new Set(p.travailles || []), F = new Set(p.termines || []), R = new Set(p.reussis || []);
  const byDom = {};
  for (const e of D.all()) { const dm = domaine(e); ((byDom[dm] ||= {})[e.chap] ||= []).push(e); }
  const rows = DOMAINES.filter(dm => byDom[dm]).map(dm => {
    const chaps = Object.entries(byDom[dm]);
    const touched = chaps.filter(([, ex]) => ex.some(e => T.has(e.id)));
    const nT = chaps.reduce((a, [, ex]) => a + ex.filter(e => T.has(e.id)).length, 0);
    const tot = chaps.reduce((a, [, ex]) => a + ex.length, 0);
    return {dm, chaps, touched, nT, tot};
  }).sort((a, b) => b.nT - a.nT);
  if (!rows.some(r => r.nT)) return `<div class="pf-emptyline">Le parcours se dessinera dès les premiers exercices travaillés.</div>`;
  return `<ol class="pc">${rows.map(r => `<li class="pc-row ${r.nT ? '' : 'idle'}">
      <details${r.nT ? '' : ''}><summary><span class="pc-dom">${esc(r.dm)}</span>
        <span class="pc-bar" role="img" aria-label="${r.touched.length} chapitres abordés sur ${r.chaps.length}">${r.chaps.map(([, ex]) => `<i class="${ex.some(e => R.has(e.id)) ? 'r' : ex.some(e => F.has(e.id)) ? 'f' : ex.some(e => T.has(e.id)) ? 't' : ''}"></i>`).join('')}</span>
        <span class="pc-n">${r.touched.length}/${r.chaps.length} chap. · ${r.nT}/${r.tot} ex.</span></summary>
        <ul class="pc-chaps">${r.chaps.map(([c, ex]) => { const t = ex.filter(e => T.has(e.id)).length, f = ex.filter(e => F.has(e.id)).length, rr = ex.filter(e => R.has(e.id)).length;
          return `<li><span>${esc(c)}</span><span class="small">${t ? `${t} travaillé${t > 1 ? 's' : ''}${f ? ` · ${f} terminé${f > 1 ? 's' : ''}` : ''}${rr ? ` · ${rr} réussi${rr > 1 ? 's' : ''}` : ''}` : 'pas encore abordé'} / ${ex.length}</span></li>`; }).join('')}</ul></details></li>`).join('')}</ol>
    <p class="pc-leg small"><i class="t"></i> travaillé <i class="f"></i> terminé <i class="r"></i> réussi — une case par chapitre</p>`;
}

/* ---------- favoris ---------- */
function favorisHTML(ids, self) {
  const ex = ids.map(D.byId).filter(Boolean);
  if (!ex.length) return `<div class="pf-emptyline">${self ? 'Aucun favori : utilise l’étoile ☆ sur un exercice pour le garder ici.' : 'Aucun exercice favori pour l’instant.'}</div>`;
  const mats = [...new Set(ex.map(e => e.mat))];
  return `<div class="fav-tools"><label class="sr" for="favQ">Rechercher dans les favoris</label><input id="favQ" type="search" placeholder="Rechercher dans ${plural(ex.length, 'favori')}…">
      <div class="fav-mats" role="group" aria-label="Filtrer par matière"><button type="button" data-fm="" aria-pressed="true">Tout</button>${mats.map(m => `<button type="button" data-fm="${esc(m)}" aria-pressed="false">${esc(m)}</button>`).join('')}</div></div>
    <ol class="fav-list">${ex.map((e, i) => `<li data-mat="${esc(e.mat)}" data-q="${esc((e.titre + ' ' + e.chap + ' ' + e.mat).toLowerCase())}">
      <a href="#ex-${esc(e.id)}"><span class="fav-n">${String(i + 1).padStart(2, '0')}</span><span class="fav-t"><b>${esc(e.titre)}</b><span class="small">${esc(e.mat)} · ${esc(e.chap)}</span></span>
      <span class="stamp n${e.niveau}">${esc(D.LV[e.niveau] || '')}</span></a></li>`).join('')}</ol>`;
}

/* ---------- solutions publiées ---------- */
function solutionsHTML(L, self) {
  if (!L.length) return `<p class="pf-emptyline">Aucune solution publiée. Sous un exercice, « Solutions d’élèves » permet de partager la tienne.</p>`;
  return `<ol class="fav-list">${L.map((s, i) => { const e = D.byId(s.ex);
    return `<li><a href="#ex-${esc(s.ex)}"><span class="fav-n">${String(i + 1).padStart(2, '0')}</span><span class="fav-t"><b>${esc(e?.titre || s.ex)}</b><span class="small">${e ? esc(e.mat) + ' · ' + esc(e.chap) + ' · ' : ''}${dateFR(s.d)}</span></span>
      ${s.verifiee ? `<span class="lab-ok">${ic('check')} vérifiée</span>` : s.statut === 'masquee' ? '<span class="lab-err">masquée</span>' : ''}</a></li>`; }).join('')}</ol>`;
}

/* ---------- carnet public ---------- */
function carnetPublicHTML(L, self) {
  if (!L.length) return `<p class="pf-emptyline">Aucune note publiée. Dans ton <a href="#carnet">carnet</a>, coche « Publier » sur une note pour la montrer ici.</p>`;
  return `<div class="cn-pages">${L.map(n => { const t = TYPES[n.type] || TYPES.note, e = n.ex && D.byId(n.ex);
    return `<article class="cn-page t-${t.c}"><div class="cn-tag">${ic(t.i)} ${t.l}</div><h3>${esc(n.titre)}</h3>${n.contenu ? `<div class="cn-rich pf-quote-like">${rich(n.contenu)}</div>` : ''}
      <footer><span class="small">${dateFR(n.d)}${e ? ` · <a href="#ex-${esc(e.id)}">${esc(e.titre)}</a>` : ''}</span></footer></article>`; }).join('')}</div>`;
}

/* ---------- badges ---------- */
const BADGE_IC = {premier_pas: 'pen', regularite: 'clock', explorateur: 'search', polyvalent: 'atom', autonome: 'key', reconnu: 'users', perseverant: 'target', specialiste: 'star', contributeur: 'upload'};
function badgesHTML(L, self) {
  const ok = L.filter(b => b.val >= b.cible), ko = L.filter(b => b.val < b.cible);
  const one = (b, got) => `<li class="bdg ${got ? 'got' : ''}"><span class="bdg-m" aria-hidden="true">${ic(BADGE_IC[b.id] || 'trophy')}</span>
    <span><b>${esc(b.titre)}</b><span class="small">${esc(b.critere)}</span>${got ? '' : `<span class="bdg-p"><i style="width:${Math.round(100 * Math.min(b.val, b.cible) / b.cible)}%"></i></span><span class="small">${Math.min(b.val, b.cible)}/${b.cible}</span>`}</span></li>`;
  if (!ok.length && !self) return `<p class="pf-emptyline">Pas encore de badge.</p>`;
  return `<ul class="bdgs">${ok.map(b => one(b, true)).join('')}${self ? ko.map(b => one(b, false)).join('') : ''}</ul>${self ? '<p class="small">Seuls les badges obtenus sont visibles des autres membres. Aucun badge ne récompense le simple fait d’ouvrir un corrigé.</p>' : ''}`;
}

/* ---------- commentaires publics ---------- */
function parolesHTML(list) {
  if (!list.length) return `<div class="pf-emptyline">Aucun commentaire public.</div>`;
  return `<ul class="pf-quotes">${list.slice(0, 12).map(c => { const e = D.byId(c.ex);
    return `<li><blockquote class="pf-quote">${rich(c.contenu.length > 600 ? c.contenu.slice(0, 600) + '…' : c.contenu)}</blockquote>
      <p class="small">sur <a href="#ex-${esc(c.ex)}">${esc(e?.titre || c.ex)}</a> · ${dateFR(c.d)}</p></li>`; }).join('')}</ul>`;
}

/* ---------- étoiles ---------- */
function starsHTML(p) {
  const e = p.etoiles, m = e.moy != null ? Number(e.moy) : null;
  const show = v => `<span class="st-show" aria-hidden="true">${[1, 2, 3, 4, 5].map(i => `<i class="${v >= i - .25 ? 'on' : v >= i - .75 ? 'half' : ''}">★</i>`).join('')}</span>`;
  return `<div class="pf-stars">
    <div class="st-avg">${m != null ? `${show(m)}<b>${m.toFixed(1).replace('.', ',')}</b><span class="small">sur 5 · ${plural(e.n, 'note')}</span>`
      : `${show(0)}<span class="small">${e.n ? `${plural(e.n, 'note')} · moyenne affichée à partir de 3` : 'Pas encore d’étoiles'}</span>`}</div>
    ${e.peut_noter ? `<div class="st-rate" role="radiogroup" aria-label="Ta note pour ${esc(p.nom)}">${[1, 2, 3, 4, 5].map(i => `<button type="button" role="radio" aria-checked="${e.mienne === i}" data-star="${i}" aria-label="${i} étoile${i > 1 ? 's' : ''}" class="${(e.mienne || 0) >= i ? 'on' : ''}">★</button>`).join('')}
      ${e.mienne ? `<button type="button" class="linkbtn" data-star="0">Retirer ma note</button>` : '<span class="small">Ta note reste anonyme</span>'}</div>` : ''}
  </div>`;
}

function bindProfil(el, p) {
  el.querySelector('#pfSig')?.addEventListener('click', () => openSignalement('profil', p.id));
  bindFollow(el, () => { p.je_suis = !p.je_suis; p.abonnes += p.je_suis ? 1 : -1; return p; }, () => renderProfil(el, D.ref()));
  el.querySelector('#pfNewColl')?.addEventListener('click', async () => { const c = await nouvelleCollection(); if (c) location.hash = '#c/' + c.id; });
  el.querySelector('#pfShare')?.addEventListener('click', async () => {
    const url = location.href.split('#')[0] + profilURL(p);
    try { await navigator.clipboard.writeText(url); toast('Lien du profil copié. Il s’ouvre pour les membres connectés.', 'ok'); }
    catch { prompt('Copie ce lien :', url); }
  });
  // étoiles
  el.querySelectorAll('[data-star]').forEach(b => b.addEventListener('click', async () => {
    const v = +b.dataset.star;
    el.querySelectorAll('[data-star]').forEach(x => x.disabled = true);
    try { await api.etoile(p.id, v === 0 || v === p.etoiles.mienne ? null : v); toast(v ? 'Note enregistrée, de façon anonyme.' : 'Note retirée.', 'ok'); renderProfil(el, D.ref()); }
    catch (x) { toast(x.message || 'Note impossible pour le moment.', 'error'); el.querySelectorAll('[data-star]').forEach(x => x.disabled = false); }
  }));
  // survol des étoiles
  const rate = el.querySelector('.st-rate');
  if (rate) {
    const btns = [...rate.querySelectorAll('[data-star]:not([data-star="0"])')];
    btns.forEach(b => b.addEventListener('mouseenter', () => btns.forEach(x => x.classList.toggle('hov', +x.dataset.star <= +b.dataset.star))));
    rate.addEventListener('mouseleave', () => btns.forEach(x => x.classList.remove('hov')));
  }
  // carte d'activité : détail d'un jour
  const hm = el.querySelector('.hm');
  if (hm) {
    const wrap = el.querySelector('.hm-wrap'); wrap.scrollLeft = wrap.scrollWidth;
    const map = new Map((p.jours || []).map(j => [j.j, j.ids || []]));
    hm.addEventListener('click', e => {
      const c = e.target.closest('.hm-c'); if (!c) return;
      hm.querySelectorAll('.sel').forEach(x => x.classList.remove('sel')); c.classList.add('sel');
      const ids = map.get(c.dataset.d) || [];
      el.querySelector('#hmDay').innerHTML = `<b>${dateFR(c.dataset.d + 'T12:00')}</b> — ${ids.length ? ids.map(id => { const e = D.byId(id); return `<a href="#ex-${esc(id)}">${esc(e?.titre || id)}</a>`; }).join(', ') : 'aucun exercice travaillé'}`;
    });
  }
  // favoris : recherche et filtre
  const q = el.querySelector('#favQ'), fl = el.querySelector('.fav-list');
  if (q && fl) {
    let mat = '';
    const apply = () => { const t = q.value.trim().toLowerCase(); let n = 0;
      fl.querySelectorAll('li').forEach(li => { const ok = (!mat || li.dataset.mat === mat) && (!t || li.dataset.q.includes(t)); li.hidden = !ok; n += ok; });
      fl.dataset.empty = n ? '' : 'Aucun favori ne correspond.'; };
    q.addEventListener('input', apply);
    el.querySelectorAll('[data-fm]').forEach(b => b.addEventListener('click', () => { mat = b.dataset.fm; el.querySelectorAll('[data-fm]').forEach(x => x.setAttribute('aria-pressed', x === b)); apply(); }));
  }
  // modération (administrateur)
  const mod = el.querySelector('.pf-mod');
  if (mod) mod.addEventListener('toggle', async () => {
    if (!mod.open) return;
    const box = el.querySelector('#pfMod'), L = await api.etoilesModeration(p.id);
    box.innerHTML = L.length ? `<table class="tbl"><tbody>${L.map(x => `<tr><td>${esc(x.auteur)}</td><td>${'★'.repeat(x.note)}</td><td>${dateFR(x.updated_at)}</td><td class="r"><button class="linkbtn danger" data-del="${esc(x.auteur_id)}">Supprimer</button></td></tr>`).join('')}</tbody></table>` : 'Aucune note.';
    box.onclick = async e => { const b = e.target.closest('[data-del]'); if (!b) return; try { await api.retirerEtoile(p.id, b.dataset.del); toast('Note supprimée.', 'ok'); renderProfil(el, D.ref()); } catch (x) { toast(x.message, 'error'); } };
  });
}

/* ===================== ÉDITION DU PROFIL ===================== */
export async function renderEdition(el) {
  el.innerHTML = `<div class="panel"><span class="skel skel-h"></span><span class="skel skel-card"></span></div>`;
  let p;
  try { p = await api.monProfil(); } catch { p = null; }
  if (!p) { el.innerHTML = `<div class="panel empty">Profil indisponible : l’administrateur doit d’abord mettre à jour la base de données (README, section Profils).</div>`; return; }
  const tog = (k, label, help) => `<label class="tg"><input type="checkbox" name="${k}" ${p[k] ? 'checked' : ''}><span class="tg-ui" aria-hidden="true"></span><span><b>${label}</b>${help ? `<small>${help}</small>` : ''}</span></label>`;
  el.innerHTML = `<form class="pf-edit" id="pfForm" novalidate>
    <div class="pagehead"><h2>Mon profil</h2><a class="btn ghost" href="#profil">${ic('back')} Retour au profil</a></div>
    <div class="alert" id="pfErr" hidden></div>
    <fieldset class="panel pe-sec"><legend><span class="pf-num">01</span> Identité</legend>
      <div class="pe-photo">${D.myAvatar()}<div><button type="button" class="btn" id="peAv">${ic('camera')} Changer la photo</button><p class="small">Carré recadré automatiquement, 160 px.</p></div></div>
      <div class="fld"><label>Nom affiché</label><input value="${esc(api.profile.full_name || '')}" disabled><p class="small">Ton nom vient de ton inscription. Pour le changer, contacte l’administrateur.</p></div>
      <div class="fld"><label for="peUser">Identifiant public</label><div class="pe-user"><span>@</span><input id="peUser" name="username" value="${esc(p.username || '')}" maxlength="20" autocomplete="off" spellcheck="false" aria-describedby="peUserH"></div>
        <p class="small" id="peUserH">3 à 20 caractères : lettres minuscules, chiffres, _. Adresse : <code>${esc(location.host)}/#u/<span id="peUserV">${esc(p.username || '')}</span></code></p></div>
      <div class="fld"><label for="peBio">Présentation <span class="small" id="peBioN"></span></label><textarea id="peBio" name="bio" maxlength="280" rows="3" placeholder="Ce que tu prépares, ce qui te plaît en sciences…">${esc(p.bio)}</textarea></div>
    </fieldset>
    <fieldset class="panel pe-sec"><legend><span class="pf-num">02</span> Parcours</legend>
      <div class="frow3">
        <div class="fld"><label for="peFil">Filière</label><select id="peFil" name="filiere"><option value="">—</option>${FILIERES.map(f => `<option ${p.filiere === f ? 'selected' : ''}>${f}</option>`).join('')}</select></div>
        <div class="fld"><label for="peAn">Année</label><select id="peAn" name="annee"><option value="">—</option>${[1, 2, 3, 4, 5].map(a => `<option value="${a}" ${p.annee === a ? 'selected' : ''}>${a}${a === 1 ? 're' : 'e'} année</option>`).join('')}</select></div>
        <div class="fld"><label for="peEt">Établissement <span class="small">(facultatif)</span></label><input id="peEt" name="etablissement" maxlength="80" value="${esc(p.etablissement)}"></div>
      </div>
      <div class="fld"><span class="lab">Matières préférées <span class="small">(8 au plus)</span></span><div class="pe-chips">${DOMAINES.map(d => `<label class="chipc"><input type="checkbox" name="mat" value="${esc(d)}" ${p.matieres?.includes(d) ? 'checked' : ''}><span>${esc(d)}</span></label>`).join('')}</div></div>
      <div class="fld"><label for="peObj">Objectif du moment <span class="small">(facultatif)</span></label><input id="peObj" name="objectif" maxlength="160" value="${esc(p.objectif)}" placeholder="Ex. : réussir l’oral de Centrale en juin"></div>
    </fieldset>
    <fieldset class="panel pe-sec"><legend><span class="pf-num">03</span> Liens <span class="small">(facultatifs)</span></legend>
      <div class="frow3">
        <div class="fld"><label for="peGh">GitHub</label><input id="peGh" name="lien_github" type="url" inputmode="url" placeholder="https://github.com/…" value="${esc(p.lien_github)}"></div>
        <div class="fld"><label for="peLi">LinkedIn</label><input id="peLi" name="lien_linkedin" type="url" inputmode="url" placeholder="https://www.linkedin.com/in/…" value="${esc(p.lien_linkedin)}"></div>
        <div class="fld"><label for="peSi">Site / portfolio</label><input id="peSi" name="lien_site" type="url" inputmode="url" placeholder="https://…" value="${esc(p.lien_site)}"></div>
      </div>
    </fieldset>
    <fieldset class="panel pe-sec"><legend><span class="pf-num">04</span> Confidentialité</legend>
      ${tog('public', 'Profil visible par les membres connectés', 'Désactivé : personne d’autre que toi (et l’administrateur) ne voit ton profil. Ton e-mail n’est jamais affiché.')}
      <div class="pe-vis" id="peVis">
        ${tog('annuaire', 'Apparaître dans l’annuaire de la communauté', 'Les membres pourront te trouver par ton nom, ta filière ou tes matières, et te suivre.')}
        ${tog('vis_stats', 'Statistiques')}${tog('vis_activite', 'Carte d’activité')}${tog('vis_parcours', 'Parcours scientifique')}
        ${tog('vis_favoris', 'Exercices favoris')}${tog('vis_collections', 'Collections', 'Seules les collections que tu partages apparaissent.')}${tog('vis_carnet', 'Pages du carnet', 'Seules les notes que tu publies apparaissent.')}${tog('vis_badges', 'Badges obtenus')}${tog('vis_commentaires', 'Commentaires publics')}${tog('vis_etoiles', 'Étoiles', 'Les membres peuvent te noter de 1 à 5 ; leurs notes restent anonymes.')}
      </div>
      <p class="small">Si tu as moins de 18 ans, parles-en avec un parent avant de rendre ton profil visible. Tu peux tout masquer à tout moment.</p>
    </fieldset>
    <div class="pe-actions"><button type="button" class="btn ghost danger" id="peWipe">${ic('trash')} Supprimer mon profil public</button>
      <span><a class="btn" href="#profil/apercu">${ic('eye')} Aperçu</a> <button class="btn primary" type="submit" id="peSave">Enregistrer</button></span></div>
  </form>`;
  const f = el.querySelector('#pfForm'), err = el.querySelector('#pfErr');
  const u = f.username, bio = f.bio;
  const syncVis = () => el.querySelector('#peVis').classList.toggle('off', !f.public.checked);
  const bioN = () => { el.querySelector('#peBioN').textContent = `${bio.value.length}/280`; };
  syncVis(); bioN();
  f.public.addEventListener('change', syncVis); bio.addEventListener('input', bioN);
  u.addEventListener('input', () => { u.value = u.value.toLowerCase().replace(/[^a-z0-9_]/g, ''); el.querySelector('#peUserV').textContent = u.value; });
  el.querySelector('#peAv').onclick = () => D.pickPhoto(() => { el.querySelector('.pe-photo').firstElementChild.outerHTML = D.myAvatar(); });
  const mats = [...f.querySelectorAll('[name=mat]')];
  mats.forEach(c => c.addEventListener('change', () => { if (mats.filter(x => x.checked).length > 8) { c.checked = false; toast('8 matières au plus.', 'error'); } }));
  el.querySelector('#peWipe').onclick = async () => {
    if (!confirm('Supprimer ton profil public ? Il redevient privé et ta présentation, ton établissement, ton objectif et tes liens sont effacés. Ton activité et tes exercices ne sont pas supprimés.')) return;
    try { await api.majProfil({public: false, bio: '', etablissement: '', objectif: '', matieres: [], lien_github: '', lien_linkedin: '', lien_site: '', filiere: '', annee: null}); toast('Profil public supprimé.', 'ok'); location.hash = '#profil'; }
    catch (x) { toast(x.message, 'error'); }
  };
  let busy = false;
  f.onsubmit = async e => {
    e.preventDefault(); if (busy) return;
    err.hidden = true;
    const v = n => f[n].value.trim();
    if (!/^[a-z0-9][a-z0-9_]{2,19}$/.test(u.value)) return showErr('Identifiant invalide : 3 à 20 caractères (lettres minuscules, chiffres ou _), en commençant par une lettre ou un chiffre.', u);
    for (const [n, re, lab] of [['lien_github', /^https:\/\/(www\.)?github\.com\/[A-Za-z0-9_.-]{1,60}\/?$/, 'GitHub'], ['lien_linkedin', /^https:\/\/([a-z]{2,3}\.)?linkedin\.com\/in\/[A-Za-z0-9_%-]{1,100}\/?$/, 'LinkedIn'], ['lien_site', /^https:\/\/[^\s<>"]{4,200}$/, 'site']])
      if (v(n) && !re.test(v(n))) return showErr(`Lien ${lab} invalide : colle l’adresse complète de ta page, commençant par https://.`, f[n]);
    const champs = {username: u.value, bio: v('bio'), filiere: v('filiere'), annee: v('annee') ? +v('annee') : null, etablissement: v('etablissement'), objectif: v('objectif'),
      matieres: mats.filter(x => x.checked).map(x => x.value), lien_github: v('lien_github'), lien_linkedin: v('lien_linkedin'), lien_site: v('lien_site'),
      public: f.public.checked, ...Object.fromEntries(['annuaire', 'vis_stats', 'vis_activite', 'vis_parcours', 'vis_favoris', 'vis_commentaires', 'vis_etoiles', 'vis_collections', 'vis_carnet', 'vis_badges'].filter(k => f[k]).map(k => [k, f[k].checked]))};
    busy = true; const b = el.querySelector('#peSave'); b.disabled = true; b.textContent = 'Enregistrement…';
    try { await api.majProfil(champs); D.setUsername?.(champs.username); toast('Profil enregistré.', 'ok'); location.hash = '#profil'; }
    catch (x) { showErr(x.message || 'Enregistrement impossible.'); }
    finally { busy = false; b.disabled = false; b.textContent = 'Enregistrer'; }
  };
  function showErr(m, field) { err.hidden = false; err.className = 'alert error'; err.innerHTML = `<span class="alert-ic">!</span><span></span>`; err.lastChild.textContent = m; field?.focus(); err.scrollIntoView({block: 'nearest'}); }
}
