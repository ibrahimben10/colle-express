// Page publique d'un exercice et de son corrigé : lecture, impression, PDF, partage.
import { CONFIG } from './config.js';
import { ic, chapIcon } from './icons.js';
import { FIG } from './figures.js';
import { legHTML } from './figures-annale.js';
import { figCorr } from './figures-corr.js';
import { anReady } from './figures-annale.js';
import { esc, fmtEnonce, hintsHTML, hintLevels, correctionHTML } from './format.js';

const $ = s => document.querySelector(s);
const LV = {1: 'CCINP', 2: 'Mines-Centrale', 3: 'X-ENS'};
const q = new URLSearchParams(location.search);
const id = q.get('id') || location.hash.slice(1);
const enonceOnly = q.get('enonce') === '1';
const toast = (t, ms = 3500) => { $('#toast').textContent = t; if (ms) setTimeout(() => { if ($('#toast').textContent === t) $('#toast').textContent = ''; }, ms); };

document.querySelectorAll('[data-site]').forEach(e => e.textContent = CONFIG.NOM_SITE);
$('#bPdf').innerHTML = `${ic('pdf')}<span class="lbl"> PDF / Imprimer</span>`;
$('#bShare').innerHTML = `${ic('share')}<span class="lbl"> Partager le lien</span>`;

let EX = null;
const typeset = el => new Promise(res => {
  const go = () => window.MathJax?.typesetPromise ? MathJax.typesetPromise([el]).then(res, res) : setTimeout(go, 200);
  go();
});

async function load() {
  const [exs, corr] = await Promise.all([fetch('data/exercices.json').then(r => r.json()), enonceOnly ? {} : fetch('data/corriges.json').then(r => r.json())]);
  EX = exs.find(e => e.id === id);
  const K = corr[id];
  if (!EX) { $('#sheet').innerHTML = '<p>Exercice introuvable.</p>'; return; }
  document.title = (enonceOnly ? 'Exercice' : 'Corrigé') + ' — ' + EX.titre;
  const fig = FIG[id];
  $('#sheet').innerHTML = `
    <header class="sh-head">
      <div class="t"><img class="shlogo" src="img/logo.png" alt="Colle express" width="232" height="48"><small>Prépa scientifique · ${esc(CONFIG.NOM_PROF)}</small></div>
      <div class="lvl"><span class="stamp n${EX.niveau}">${LV[EX.niveau]}</span><br>${esc(EX.mat)} · ${esc(EX.chap)}</div>
    </header>
    <h1>${esc(EX.titre)}</h1>
    <section class="co co-enonce"><div class="co-h"><span class="co-e" aria-hidden="true">📘</span>Énoncé<span class="co-meta">${EX.duree} min</span></div>
      <div class="enonce">${fmtEnonce(EX.enonce)}</div>
      ${fig ? `<figure class="fig">${fig.svg}<figcaption>${ic('eye')}<span>${legHTML(fig.legende)}</span></figcaption></figure>` : ''}</section>
    ${!enonceOnly && K ? `
      <section class="co co-indices"><div class="co-h"><span class="co-e" aria-hidden="true">💡</span>Indices<span class="co-meta">cherche d’abord !</span></div>
        ${hintsHTML(K, hintLevels(K).map(() => true))}</section>
      <section class="co co-corr"><details class="acc corr-acc" open>
        <summary><span class="co-e" aria-hidden="true">📝</span><span class="acc-t"><b>Correction détaillée</b><small>Touche pour afficher ou masquer</small></span><span class="chev" aria-hidden="true"></span></summary>
        <div class="acc-body">${figCorr(id)}${correctionHTML(K)}</div></details></section>` : ''}
    <div class="noprint openall">${!enonceOnly && K ? `<button class="btn" id="bAll">Tout afficher</button>` : ''}</div>
    <footer class="sh-foot"><span>${esc(CONFIG.NOM_SITE)} — ${esc(CONFIG.NOM_PROF)}</span><span>${esc(location.href.split('&pdf')[0])}</span></footer>`;
  // Tout est composé ouvert (largeur réelle pour MathJax), puis replié pour laisser chercher l'élève.
  await typeset($('#sheet'));
  const accs = [...document.querySelectorAll('#sheet details.acc')];
  if (q.get('pdf') !== '1') accs.forEach(d => d.open = false);
  $('#bAll') && ($('#bAll').onclick = () => { const o = accs.some(d => !d.open); accs.forEach(d => d.open = o); $('#bAll').textContent = o ? 'Tout masquer' : 'Tout afficher'; });
  window.addEventListener('beforeprint', () => accs.forEach(d => d.open = true));
  if (q.get('pdf') === '1') { toast('Choisis « Enregistrer au format PDF » dans la fenêtre qui s’ouvre.', 6000); setTimeout(makePdf, 400); }
}

const fileName = () => ((enonceOnly ? 'exercice-' : 'corrige-') + (EX?.titre || id)).normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^a-zA-Z0-9]+/g, '-').replace(/^-|-$/g, '').toLowerCase().slice(0, 60) + '.pdf';
// PDF : export natif du navigateur (vectoriel, formules nettes).
// Ordinateur : « Enregistrer au format PDF » ; iPhone : Imprimer → Partager ; Android : Imprimer → Enregistrer en PDF.
async function makePdf() {
  await anReady();
  document.title = fileName().replace(/\.pdf$/, '');   // nom proposé pour le fichier
  window.print();
}
$('#bPdf').onclick = makePdf;
$('#bShare').onclick = async () => {
  const url = location.href.split('&pdf')[0];
  try { if (navigator.share) { await navigator.share({title: document.title, url}); return; } } catch (e) { if (e?.name === 'AbortError') return; }
  try { await navigator.clipboard.writeText(url); toast('Lien copié : colle-le où tu veux.'); } catch { toast(url, 8000); }
};

load().catch(() => { $('#sheet').innerHTML = '<p>Impossible de charger l’exercice.</p>'; });

if ('serviceWorker' in navigator && location.protocol !== 'file:') navigator.serviceWorker.register('sw.js').catch(() => {});
