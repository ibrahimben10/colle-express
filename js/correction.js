// Page publique d'un exercice et de son corrigé : lecture, impression, PDF, partage.
import { CONFIG } from './config.js';
import { ic, chapIcon } from './icons.js';
import { FIG } from './figures.js';
import { esc, rich, fmtEnonce, fmtCorrige } from './format.js';

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
      <svg class="crest" viewBox="0 0 48 48" aria-hidden="true"><circle class="ring" cx="24" cy="24" r="23"/><circle class="in" cx="24" cy="24" r="19.5"/><text x="24" y="33" text-anchor="middle">∮</text></svg>
      <div class="t"><b>${esc(CONFIG.NOM_SITE)}</b><small>Prépa MP · ${esc(CONFIG.NOM_PROF)}</small></div>
      <div class="lvl"><span class="stamp n${EX.niveau}">${LV[EX.niveau]}</span><br>${esc(EX.mat)} · ${esc(EX.chap)}</div>
    </header>
    <h1>${esc(EX.titre)}</h1>
    <h2 class="part">Énoncé</h2>
    <div class="enonce">${fmtEnonce(EX.enonce)}</div>
    ${fig ? `<figure class="fig">${fig.svg}<figcaption>${ic('eye')}<span>${esc(fig.legende)}</span></figcaption></figure>` : ''}
    ${!enonceOnly && K ? `
      <h2 class="part">Indices</h2>
      <ol class="hints">${K.indices.map((h, i) => `<li><span class="n">${i + 1}</span><div>${rich(h)}</div></li>`).join('')}</ol>
      <h2 class="part">Corrigé</h2>
      ${K.reponse ? `<div class="result">${ic('target')}<div><span class="lab">Résultat</span><div>${rich(K.reponse)}</div></div></div>` : ''}
      <div class="corrige">${fmtCorrige(K.corrige)}</div>` : ''}
    <footer class="sh-foot"><span>${esc(CONFIG.NOM_SITE)} — ${esc(CONFIG.NOM_PROF)}</span><span>${esc(location.href.split('&pdf')[0])}</span></footer>`;
  await typeset($('#sheet'));
  if (q.get('pdf') === '1') { toast('Choisis « Enregistrer au format PDF » dans la fenêtre qui s’ouvre.', 6000); setTimeout(makePdf, 400); }
}

const fileName = () => ((enonceOnly ? 'exercice-' : 'corrige-') + (EX?.titre || id)).normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^a-zA-Z0-9]+/g, '-').replace(/^-|-$/g, '').toLowerCase().slice(0, 60) + '.pdf';
// PDF : export natif du navigateur (vectoriel, formules nettes).
// Ordinateur : « Enregistrer au format PDF » ; iPhone : Imprimer → Partager ; Android : Imprimer → Enregistrer en PDF.
function makePdf() {
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
