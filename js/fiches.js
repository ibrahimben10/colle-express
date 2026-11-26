// Fiches de cours : index (par matière, année et partie) et page d'une fiche.
// Le texte vient de data/fiches/<id>.md, les schémas de js/fiches-fig-*.js (dessinés en SVG, thème clair/sombre).
import { esc, rich, callout, inlineC } from './format.js';
import { ic } from './icons.js';

let IDX = null, FIGS = {};
const MODS = {p1: () => import('./fiches-fig-p1.js'), p2: () => import('./fiches-fig-p2.js'), p3: () => import('./fiches-fig-p2.js'), p4: () => import('./fiches-fig-p4.js'), p5: () => import('./fiches-fig-p5.js'), px: () => import('./fiches-fig-p5.js'),
  mpa: () => import('./fiches-fig-mpa.js'), mpb: () => import('./fiches-fig-mpb.js'), mpc: () => import('./fiches-fig-mpc.js'), c: () => import('./fiches-fig-c.js'), i: () => import('./fiches-fig-i.js')};
async function index() { if (!IDX) IDX = await fetch('data/fiches/index.json').then(r => r.json()); return IDX; }
async function figs(id) {
  let k = id.split('-')[0];
  if (k === 'mp') k = /^mp-(referentiels|non-galileen|frottement|signal|numerique|ondes-lumineuses|interferences|young|michelson|n-ondes)/.test(id) ? 'mpa'
    : /^mp-(systemes-ouverts|diffusion|quantique|libre|potentiel|statistique)/.test(id) ? 'mpc' : 'mpb';
  if (!MODS[k] || FIGS[k]) return FIGS[k] || {};
  try { FIGS[k] = (await MODS[k]()).FIGS; } catch { FIGS[k] = {}; }
  return FIGS[k];
}
const MAT = {Physique: 'atom', Chimie: 'flask', Informatique: 'code'};

function figure(F, key) {
  const f = F[key];
  if (!f) return `<figure class="fig ff ff-vide"><div class="ff-ph">${ic('eye')}<span>Schéma à venir</span></div></figure>`;
  return `<figure class="fig ff">${f[1]}<figcaption>${inlineC(f[0])}</figcaption></figure>`;
}
// Découpe en paragraphes (lignes vides), sans couper un bloc de code ``` qui contient des lignes vides.
function blocs(md) {
  const out = []; let cur = [], code = false;
  for (const l of md.split('\n')) {
    if (/^\s*```/.test(l)) code = !code;
    if (!code && !l.trim()) { if (cur.length) out.push(cur.join('\n')); cur = []; } else cur.push(l);
  }
  if (cur.length) out.push(cur.join('\n'));
  return out;
}
// Markdown des fiches : « ## Titre », « > **Définition — …** » (encadré), « [[fig:clé]] », tableaux, listes, formules.
function corps(md, F) {
  const toc = [];
  const html = blocs(md.replace(/^---[\s\S]*?---\s*/, '')).map(p => {
    const t = p.trim();
    let m;
    if ((m = t.match(/^##\s+(.+)$/))) { const id = 's' + toc.length; toc.push([id, m[1]]); return `<h2 class="fh2" id="${id}">${esc(m[1])}</h2>`; }
    if ((m = t.match(/^\[\[fig:([\w-]+)\]\]$/))) return figure(F, m[1]);
    if (/^>\s?/.test(t)) return callout(t.replace(/^>\s?/gm, ''));
    return rich(t);
  }).join('');
  return {html, toc};
}

export async function renderFiches(el, sub, typeset) {
  const L = await index().catch(() => null);
  if (!L) { el.innerHTML = `<div class="panel pad"><p>Les fiches ne sont pas disponibles hors ligne pour le moment.</p></div>`; return; }
  const f = sub && L.find(x => x.id === sub && x.pret);
  if (!f) return renderIndex(el, L);
  el.innerHTML = `<div class="fiche-page"><a class="btn ghost" href="#fiches">${ic('back')} Toutes les fiches</a><div class="panel pad"><p class="small">Chargement…</p></div></div>`;
  const [md, F] = await Promise.all([fetch(`data/fiches/${f.id}.md`).then(r => r.ok ? r.text() : Promise.reject()), figs(f.id)]).catch(() => [null, {}]);
  if (md == null) { el.querySelector('.panel').innerHTML = '<p>Fiche introuvable.</p>'; return; }
  const {html, toc} = corps(md, F);
  const same = L.filter(x => x.mat === f.mat && x.niveau === f.niveau), k = same.indexOf(f), prev = same[k - 1], next = same[k + 1];
  el.innerHTML = `<article class="fiche-page">
    <a class="btn ghost" href="#fiches">${ic('back')} Toutes les fiches</a>
    <header class="fiche-head"><p class="kicker">${ic(MAT[f.mat] || 'book')} ${esc(f.mat)} · ${esc(f.niveau)} · ${esc(f.partie)}</p><h1>${esc(f.titre)}</h1>
      <p class="fiche-actions"><a class="btn primary" href="#colle/${f.id}">${ic('msg')} Passer une colle sur ce chapitre</a></p>
      ${toc.length > 2 ? `<nav class="fiche-toc" aria-label="Sommaire">${toc.map(([id, t]) => `<a href="#f/${f.id}" data-s="${id}">${esc(t)}</a>`).join('')}</nav>` : ''}</header>
    <div class="fiche-corps">${html}</div>
    <p class="small fiche-src">Fiche rédigée à partir du programme officiel ; les schémas sont à valider avant publication définitive.</p>
    <nav class="fiche-nav">${prev ? `<a class="btn" href="#f/${prev.id}">${ic('back')} ${esc(prev.titre)}</a>` : '<span></span>'}${next ? `<a class="btn" href="#f/${next.id}">${esc(next.titre)} ${ic('arrow')}</a>` : ''}</nav>
  </article>`;
  el.querySelectorAll('.fiche-toc a').forEach(a => a.onclick = e => { e.preventDefault(); el.querySelector('#' + a.dataset.s)?.scrollIntoView({behavior: 'smooth', block: 'start'}); });
  typeset?.(el);
  scrollTo(0, 0);
}

const norm = t => String(t).normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();

function renderIndex(el, L) {
  const groupes = [];
  for (const f of L) {
    const g = `${f.mat} · ${f.niveau}`; let G = groupes.find(x => x.k === g); if (!G) groupes.push(G = {k: g, mat: f.mat, parties: []});
    let P = G.parties.find(x => x.t === f.partie); if (!P) G.parties.push(P = {t: f.partie, fs: []}); P.fs.push(f);
  }
  el.innerHTML = `<div class="fiches-idx">
    <header class="fiche-head"><p class="kicker">${ic('book')} Fiches de cours</p><h1>L’essentiel de chaque chapitre</h1>
      <p class="small">Définitions, lois, méthodes et pièges, avec les schémas à connaître. ${L.length} fiches.</p>
      <div class="searchbox"><span>${ic('search')}</span><input id="fqF" type="search" placeholder="Chercher une fiche : Gauss, pH, Michelson…" aria-label="Chercher une fiche" autocomplete="off" spellcheck="false"></div>
      <p class="fiche-count" id="fqN" aria-live="polite" hidden></p>
      <p class="fiche-actions"><a class="btn" href="#colle">${ic('msg')} Colleur virtuel : passer une colle de cours</a></p></header>
    ${groupes.map(G => `<section class="fgrp"><h2>${ic(MAT[G.mat] || 'book')} ${esc(G.k)}</h2>${G.parties.map(P => `<h3>${esc(P.t)}</h3><div class="fcards">${P.fs.map(f =>
      (f.pret ? `<a class="fcard" href="#f/${f.id}"` : `<div class="fcard off"`) + ` data-q="${esc(norm(f.titre + ' ' + f.partie + ' ' + f.mat + ' ' + f.niveau + ' ' + (f.k || '')))}"><b>${esc(f.titre)}</b><span>${f.pret ? `${f.n} schéma${f.n > 1 ? 's' : ''}` : 'en préparation'}</span>` + (f.pret ? '</a>' : '</div>')).join('')}</div>`).join('')}</section>`).join('')}
  </div>`;
  const q = el.querySelector('#fqF');
  const nb = el.querySelector('#fqN');
  q.oninput = () => {
    const mots = norm(q.value).split(/\s+/).filter(Boolean); let n = 0;
    el.querySelectorAll('.fcard').forEach(c => { const ok = mots.every(m => c.dataset.q.includes(m)); c.hidden = !ok; if (ok) n++; });
    el.querySelectorAll('.fcards').forEach(b => { const vide = ![...b.children].some(c => !c.hidden); b.hidden = vide; b.previousElementSibling.hidden = vide; });
    el.querySelectorAll('.fgrp').forEach(g => g.hidden = ![...g.querySelectorAll('.fcard')].some(c => !c.hidden));
    nb.hidden = !mots.length; nb.textContent = n ? `${n} fiche${n > 1 ? 's' : ''} trouvée${n > 1 ? 's' : ''}` : 'Aucune fiche ne correspond. Essayez un autre mot.';
  };
  scrollTo(0, 0);
}

// ---------- Fiche du cours depuis un exercice (oral) ----------
// Chapitre d'exercice → fiches correspondantes (dans l'ordre de pertinence).
const LIENS = {
  Maths: {
    'Algèbre & arithmétique': ['m1-arithmetique', 'm2-algebre'], 'Algèbre euclidienne': ['m2-euclidiens', 'm1-prehilbertiens'],
    'Algèbre linéaire': ['m2-algebre-lin', 'm1-ev', 'm1-dimension', 'm1-matrices'], 'Analyse asymptotique': ['m1-asymptotique'],
    'Anneaux': ['m2-algebre', 'm1-structures'], 'Approximation': ['m2-suites-fonctions', 'm2-topologie'], 'Arithmétique': ['m1-arithmetique', 'm2-algebre'],
    'Calcul différentiel': ['m2-differentiel'], 'Déterminants': ['m1-determinants'], 'Exponentielle de matrices': ['m2-reduction', 'm2-edl'],
    "Fonctions d'une variable": ['m1-derivabilite', 'm1-continuite', 'm1-fonctions'], 'Groupes': ['m2-algebre', 'm1-structures'],
    'Groupes & représentations': ['m2-algebre'], 'Groupes de matrices': ['m2-euclidiens', 'm2-algebre'], 'Géométrie euclidienne': ['m1-prehilbertiens', 'm2-euclidiens'],
    'Intégrales à paramètre': ['m2-parametre', 'm2-integration'], 'Intégration': ['m2-integration', 'm1-integration'], 'Polynômes': ['m1-polynomes'],
    'Probabilités': ['m2-probas', 'm1-probas', 'm1-denombrement'], 'Réduction': ['m2-reduction', 'm2-algebre-lin'], 'Suites': ['m1-suites'],
    'Suites de fonctions': ['m2-suites-fonctions'], 'Séries': ['m2-series', 'm1-series'], 'Séries de Fourier': ['m2-suites-fonctions'],
    'Séries de Fourier & EDP': ['m2-suites-fonctions'], 'Séries de fonctions': ['m2-suites-fonctions'], 'Séries entières': ['m2-series-entieres'],
    'Topologie & convexité': ['m2-topologie'], 'Topologie matricielle': ['m2-topologie'], 'Équations différentielles': ['m2-edl', 'm1-edl'],
  },
  Physique: {
    'Diffusion thermique': ['mp-diffusion'], 'Mécanique des fluides': [], 'Induction': ['p5-induction', 'p5-circuit-fixe', 'p5-circuit-mobile'], 'Magnétostatique': ['mp-magnetostatique', 'mp-dipole-m', 'p5-champ-b'],
    'Mécanique': ['p2-dynamique', 'p2-energie', 'p3-moment', 'p3-central', 'mp-non-galileen', 'mp-frottement'],
    'Mécanique quantique': ['mp-quantique', 'mp-potentiel', 'mp-libre'], 'Ondes mécaniques': ['p1-propagation', 'p1-superposition'],
    'Ondes électromagnétiques': ['mp-ondes-vide', 'mp-plasma', 'mp-conducteur'], 'Optique géométrique': ['p1-optique-geo'],
    'Optique ondulatoire': ['mp-interferences', 'mp-young', 'mp-michelson', 'mp-n-ondes', 'mp-ondes-lumineuses'], 'Physique statistique': ['mp-statistique'],
    'Rayonnement': ['mp-rayonnement'], 'Thermodynamique': ['p4-premier', 'p4-second', 'p4-machines', 'mp-systemes-ouverts'],
    'Électrocinétique': ['p1-arqs', 'p1-premier-ordre', 'p1-second-ordre', 'p1-sinusoidal', 'p1-filtrage'],
    'Électrostatique': ['mp-electrostatique', 'mp-exemples-e', 'mp-dipole-e'], 'Équations de Maxwell': ['mp-maxwell', 'mp-energie-em'],
  },
  Chimie: {
    'Acide-base': ['c-acide-base'], 'Atomistique': ['c-classification'], 'Cinétique': ['c-cinetique'], 'Cristallographie': ['c-cristal'],
    'Oxydoréduction': ['c-redox', 'c-e-ph'], 'Solubilité': ['c-solubilite'], 'Solutions aqueuses': ['c-acide-base', 'c-solubilite'],
    'Structure des molécules': ['c-lewis', 'c-intermoleculaire'], 'Thermochimie': ['c-matiere'], 'Électrochimie': ['c-redox', 'c-e-ph'],
  },
  Informatique: {
    'Apprentissage': ['i-ia'], 'Bases de données (SQL)': ['i-sql'], 'Complexité et preuves': ['i-complexite'], 'Graphes': ['i-graphes', 'i-plus-courts'],
    'Nombres flottants': ['i-nombres'], 'Piles, files et récursivité': ['i-piles', 'i-recursivite'], 'Programmation dynamique': ['i-progdyn', 'i-dictionnaires'],
    'Python : listes et fichiers': ['i-python', 'i-fichiers'], 'Théorie des jeux': ['i-jeux'], 'Tris': ['i-tris'],
  },
};

// Fiches proposées pour un exercice : table ci-dessus, sinon recherche par mots du chapitre dans l'index.
export async function fichesPour(mat, chap) {
  const L = (await index().catch(() => [])).filter(f => f.pret);
  const ids = LIENS[mat]?.[chap];
  if (ids) return ids.map(id => L.find(f => f.id === id)).filter(Boolean);
  const mots = norm(chap).split(/[^a-z0-9]+/).filter(m => m.length > 3);
  return L.filter(f => (f.mat === mat || (mat === 'Maths' && f.mat === 'Mathématiques')) && mots.some(m => norm(f.titre + ' ' + f.partie + ' ' + (f.k || '')).includes(m))).slice(0, 4);
}

// Panneau latéral qui affiche la fiche du cours sans quitter l'exercice.
export async function ouvrirFicheCours(mat, chap, typeset) {
  document.getElementById('ficheDlg')?.remove();
  const d = document.createElement('dialog');
  d.id = 'ficheDlg'; d.className = 'fdlg'; d.setAttribute('aria-label', 'Fiche du cours');
  d.innerHTML = `<div class="fdlg-h"><b>${ic('list')} Fiche du cours</b><button class="iconbtn" type="button" data-close aria-label="Fermer">${ic('x')}</button></div><div class="fdlg-c"><p class="small">Chargement…</p></div>`;
  document.body.appendChild(d);
  d.querySelector('[data-close]').onclick = () => d.close();
  d.addEventListener('close', () => d.remove());
  d.addEventListener('click', e => { if (e.target === d) d.close(); });
  d.showModal();
  const c = d.querySelector('.fdlg-c');
  const F = await fichesPour(mat, chap);
  if (!F.length) { c.innerHTML = `<p>Pas encore de fiche pour le chapitre « ${esc(chap)} ».</p><a class="btn" href="#fiches">${ic('list')} Toutes les fiches</a>`; c.querySelector('a').onclick = () => d.close(); return; }
  const montre = async f => {
    const zone = c.querySelector('.fdlg-f');
    zone.innerHTML = '<p class="small">Chargement…</p>';
    const [md, FG] = await Promise.all([fetch(`data/fiches/${f.id}.md`).then(r => r.ok ? r.text() : ''), figs(f.id)]);
    if (!md) { zone.innerHTML = '<p>Fiche introuvable.</p>'; return; }
    zone.innerHTML = `<h2 class="fdlg-t">${esc(f.titre)}</h2><p class="small">${esc(f.mat)} · ${esc(f.niveau)} · ${esc(f.partie)}</p><div class="fiche-corps">${corps(md, FG).html}</div>
      <p><a class="btn ghost" href="#f/${f.id}">${ic('book')} Ouvrir la fiche en pleine page</a></p>`;
    zone.querySelector('a[href^="#f/"]').onclick = () => d.close();
    zone.scrollTop = 0; typeset?.(zone);
  };
  c.innerHTML = (F.length > 1 ? `<div class="fdlg-tabs" role="tablist">${F.map((f, i) => `<button type="button" role="tab" aria-selected="${i === 0}" data-i="${i}">${esc(f.titre)}</button>`).join('')}</div>` : '') + '<div class="fdlg-f"></div>';
  c.querySelectorAll('[data-i]').forEach(b => b.onclick = () => { c.querySelectorAll('[data-i]').forEach(x => x.setAttribute('aria-selected', x === b)); montre(F[+b.dataset.i]); });
  montre(F[0]);
}
