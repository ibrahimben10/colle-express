// Correction en trois modes : Guidée, Détaillée, Rigoureuse.
// Le module affiche le panneau de correction d'un exercice et ses outils (« Expliquer davantage »,
// « Pourquoi cette méthode ? », « Autre méthode », « Vérifier ma réponse », copier, signaler).
// Les contenus générés par l'IA passent par la fonction Supabase « corriger », qui garde la clé API
// côté serveur, met en cache les contenus partagés et contrôle les rédactions par une relecture indépendante.
import { api, DEMO } from './api.js';
import { CONFIG } from './config.js';
const IA = () => !!CONFIG.IA && !DEMO;
import { ic } from './icons.js';
import { esc, rich, inline, fmtCorrige, correctionHTML, stepChunks, guideQuestion } from './format.js';
import { toast, busy } from './ui.js';
import { celebrate, readingProgress, stepNav } from './vivant.js';
import { figCorr } from './figures-corr.js';

const MODES = [
  {k: 'guide', t: 'Guidée', d: 'Une étape à la fois, avec des questions pour chercher toi-même.'},
  {k: 'detail', t: 'Détaillée', d: 'Toute la démarche : analyse, rappels, stratégie, calculs, vérification.'},
  {k: 'rigueur', t: 'Rigoureuse', d: 'Une rédaction de copie de concours, sans commentaire pédagogique.'},
];
export const FILIERES = ['MPSI', 'MP', 'MP*', 'PCSI', 'PC', 'PSI', 'MP2I', 'MPI', 'PTSI', 'PT', 'TSI', 'BCPST'];
const LS = {get(k, d) { try { const v = localStorage.getItem('ce:' + k); return v ? JSON.parse(v) : d; } catch { return d; } },
  set(k, v) { try { localStorage.setItem('ce:' + k, JSON.stringify(v)); } catch {} }};
export const filiere = () => FILIERES.includes(LS.get('filiere', '')) ? LS.get('filiere') : 'MP';
export const setFiliere = f => { if (FILIERES.includes(f)) LS.set('filiere', f); };
const VERIF = {conforme: ['ok', 'La relecture indépendante n’a trouvé aucune erreur.'], incertain: ['warn', 'La relecture signale des points qu’elle n’a pas pu confirmer.'],
  erreur: ['err', 'La relecture a trouvé des erreurs : lis ses remarques avant de t’y fier.'], non_relu: ['warn', 'La relecture n’a pas pu avoir lieu.']};

/*
 ctx = {ex, K, S, sol(), locked(), ensureSolution(), unlock(), record(kind), nextHint(), typeset(el), shareURL, share()}
*/
export function renderCorrection(sec, ctx) {
  const {ex, S} = ctx;
  S.cmode ||= LS.get('cmode', 'guide');
  S.gstep ||= 0; S.ia ||= {}; S.expl ||= {}; S.fold ||= {}; S.tbusy ||= {};
  sec.innerHTML = `<div class="co-h">Correction<span class="co-meta" id="corrMeta"></span></div>
    <div class="modebar">
      <div class="modesel" role="radiogroup" aria-label="Mode de correction">${MODES.map((m, i) => `<button type="button" role="radio" data-m="${m.k}" aria-checked="${S.cmode === m.k}" tabindex="${S.cmode === m.k ? 0 : -1}"><span class="mk-n">0${i + 1}</span><b>${m.t}</b></button>`).join('')}</div>
      ${IA() ? `<label class="prog"><span>Programme</span><select id="cFil" aria-label="Ta filière (adapte les contenus générés)">${FILIERES.map(f => `<option ${f === filiere() ? 'selected' : ''}>${f}</option>`).join('')}</select></label>` : ''}
    </div>
    <p class="mode-d" id="modeD"></p>
    <div id="corrBody" class="corr-body"></div>`;
  const radios = [...sec.querySelectorAll('.modesel [role=radio]')];
  const pick = k => { S.cmode = k; LS.set('cmode', k); radios.forEach(r => { const on = r.dataset.m === k; r.setAttribute('aria-checked', on); r.tabIndex = on ? 0 : -1; }); draw(true); };
  radios.forEach((r, i) => {
    r.onclick = () => pick(r.dataset.m);
    r.onkeydown = e => { const d = {ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1}[e.key]; if (!d) return; e.preventDefault(); const n = radios[(i + d + 3) % 3]; n.focus(); pick(n.dataset.m); };
  });
  sec.querySelector('#cFil') && (sec.querySelector('#cFil').onchange = e => { setFiliere(e.target.value); toast(`Programme ${e.target.value} : les prochains contenus générés en tiendront compte.`, 'ok'); });
  const body = sec.querySelector('#corrBody');
  function draw(anim) {
    sec.querySelector('#modeD').textContent = MODES.find(m => m.k === S.cmode).d;
    body.classList.toggle('anim', !!anim);
    ({guide: drawGuide, detail: drawDetail, rigueur: drawRigueur})[S.cmode](body, ctx, draw);
    ctx.typeset(body);
  }
  ctx.redraw = () => draw(false);
  draw(false);
}

/* ---------------- Mode guidé ---------------- */
function drawGuide(box, ctx, draw) {
  const {S} = ctx, sol = ctx.sol();
  const C = sol ? stepChunks(sol.corrige) : [];
  const n = Math.min(S.gstep, C.length || S.gstep);
  const done = sol && n >= C.length;
  const nxt = sol ? C[n] : null;
  if (!sol && !IA()) { box.innerHTML = `<div class="gate"><p>Cet exercice n’a pas encore de correction rédigée.</p><p class="small">Elle arrivera bientôt. En attendant, compare ta réponse avec celles de ton groupe.</p></div>`; return; }
  box.innerHTML = `
    ${n === 0 ? `<p class="guide-intro"><span class="hand">On commence par comprendre l’énoncé.</span> Essaie chaque question sur ta feuille avant de dévoiler la suite. Tu peux t’arrêter dès que tu as compris.</p>` : ''}
    ${sol && n ? figCorr(ctx.ex.id) : ''}
    ${sol && n ? `<div class="corrige guide">${fmtCorrige(C.slice(0, n).map(c => c.md).join('\n\n'))}</div>` : ''}
    ${S.busy === 'solution' ? `<p class="wait"><span class="spin"></span> Rédaction de la correction, puis relecture indépendante… cela peut prendre une minute.</p>` : done ? `
      <div class="guide-end"><p class="sep" aria-hidden="true">∴</p>
        ${sol.reponse ? `<div class="result"><span class="lab">Résultat</span><div>${rich(sol.reponse)}</div></div>` : ''}
        <p>Tu as tout dévoilé. Compare avec ta copie, puis vérifie ta propre réponse ci-dessous.</p></div>` : `
      <div class="guide-next">
        <p class="gq"><span class="mono">${sol ? `Étape ${n + 1} / ${C.length}${nxt?.title ? ` · ${esc(nxt.title)}` : ''}` : 'Étape 1'}</span>${esc(guideQuestion(nxt || {title: 'Analyse'}))}</p>
        <div class="row-b">
          <button class="btn primary" id="gNext">${ic('arrow')} Voir l’étape suivante</button>
          <button class="btn" id="gHint">${ic('bulb')} Afficher un indice</button>
        </div>
        <button class="linkbtn" id="gAll">Voir toute la correction</button>
      </div>`}
    ${verifierHTML(ctx)}`;
  box.querySelector('#gNext')?.addEventListener('click', async () => {
    if (!ctx.sol()) { S.gstep = Math.max(S.gstep, 1); ctx.record('guide'); await ctx.ensureSolution(); return; }
    if (S.gstep === 0) ctx.record('guide');
    S.gstep = Math.min(S.gstep + 1, stepChunks(ctx.sol().corrige).length);
    const fini = S.gstep >= stepChunks(ctx.sol().corrige).length;
    if (fini) { ctx.unlock(); ctx.record('solution'); }
    draw(false);
    if (fini && !S.cele) { S.cele = true; celebrate(box.querySelector('.guide-end') || box, 'Bien joué : tu as parcouru toute la correction.'); }
    const last = box.querySelectorAll('.corrige.guide > .step, .corrige.guide > *'); const el = [...box.querySelectorAll('.corrige.guide > section')].at(-1) || last[last.length - 1];
    if (el) { el.classList.add('fresh'); el.scrollIntoView({behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'nearest'}); }
  });
  box.querySelector('#gHint')?.addEventListener('click', () => ctx.nextHint());
  box.querySelector('#gAll')?.addEventListener('click', () => { const r = document.querySelector('.modesel [data-m=detail]'); r?.click(); });
  bindVerifier(box, ctx, draw);
}

/* ---------------- Porte douce : on encourage à chercher, sans interdire ---------------- */
function gate(box, ctx, draw) {
  const {S} = ctx;
  if (!ctx.locked() || S.forceOpen) return false;
  box.innerHTML = `<div class="gate"><p class="gate-t">Tu peux essayer avant de voir la solution.</p>
    <p class="small">Le mode guidé dévoile la correction une étape à la fois. Si tu préfères tout lire maintenant, c’est possible aussi.</p>
    <div class="row-b"><button class="btn primary" id="toGuide">${ic('bulb')} Passer en mode guidé</button><button class="btn" id="seeAll">${ic('eye')} Voir quand même</button></div></div>`;
  box.querySelector('#toGuide').onclick = () => document.querySelector('.modesel [data-m=guide]')?.click();
  box.querySelector('#seeAll').onclick = () => { S.forceOpen = true; ctx.unlock(); draw(true); };
  return true;
}

/* ---------------- Mode détaillé ---------------- */
function drawDetail(box, ctx, draw) {
  const {S, K, ex} = ctx;
  if (gate(box, ctx, draw)) return;
  const sol = ctx.sol();
  if (!sol && !IA()) { box.innerHTML = `<div class="gate"><p>Cet exercice n’a pas encore de correction rédigée.</p><p class="small">Elle arrivera bientôt.</p></div>`; return; }
  if (!sol) {
    box.innerHTML = S.busy === 'solution' ? `<p class="wait"><span class="spin"></span> Rédaction de la correction, puis relecture indépendante… cela peut prendre une minute.</p>`
      : `<div class="gate"><p>Cet exercice n’a pas encore de correction rédigée par l’équipe.</p><p class="small">Une correction peut être rédigée par l’IA puis contrôlée par une seconde relecture automatique. Elle restera signalée comme telle.</p>
        <button class="btn primary" id="genSol" ${DEMO ? 'disabled' : ''}>${ic('pen')} Rédiger la correction</button>${DEMO ? '<p class="small">Indisponible en mode démonstration.</p>' : ''}</div>`;
    box.querySelector('#genSol')?.addEventListener('click', () => ctx.ensureSolution());
    return;
  }
  if (!S.seenD) { S.seenD = true; ctx.record('solution'); }
  const C = stepChunks(sol.corrige);
  const strat = C.find(c => /stratégie|méthode/i.test(c.title));
  box.innerHTML = `
    <div class="ctools" role="toolbar" aria-label="Outils de la correction">
      ${strat || IA() ? `<button class="tbtn" id="tWhy" aria-expanded="${!!S.showWhy}">${ic('target')} Pourquoi cette méthode ?</button>` : ''}
      ${IA() ? `<button class="tbtn" id="tAlt" aria-expanded="${!!S.showAlt}">${ic('wave')} Autre méthode</button>` : ''}
      <button class="tbtn" id="tFold">${ic('menu')} ${Object.values(S.fold).some(Boolean) ? 'Tout déplier' : 'Tout replier'}</button>
      <button class="tbtn" id="tCopy">${ic('link')} Copier</button>
      ${K ? `<a class="tbtn" href="${esc(ctx.shareURL)}&pdf=1" target="_blank" rel="noopener">${ic('pdf')} PDF</a><button class="tbtn" id="tShare">${ic('share')} Partager</button>` : ''}
      <button class="tbtn warnb" id="tReport">${ic('x')} Signaler une erreur</button>
    </div>
    <div id="whyBox" ${S.showWhy ? '' : 'hidden'}>${S.showWhy ? whyHTML(ctx, strat) : ''}</div>
    ${figCorr(ex.id)}
    ${correctionHTML(sol)}
    ${srcHTML(ctx)}
    <div id="altBox" ${S.showAlt ? '' : 'hidden'}>${S.showAlt ? altHTML(ctx) : ''}</div>
    ${verifierHTML(ctx)}`;
  // outils par étape : replier, « Expliquer davantage »
  box.querySelectorAll('.corrige > section.step').forEach((st, i) => {
    st.dataset.i = i;
    const h = st.querySelector('h4');
    if (IA()) {
      const tb = document.createElement('span'); tb.className = 'stools';
      tb.innerHTML = `<button class="sbtn" data-x="${i}" aria-expanded="${!!S.expl[i]}">${ic('bulb')} <span>Expliquer davantage</span></button>`;
      h.append(tb);
    }
    h.tabIndex = 0; h.setAttribute('role', 'button'); h.setAttribute('aria-expanded', !S.fold[i]);
    const tog = e => { if (e?.target?.closest?.('.sbtn')) return; S.fold[i] = !S.fold[i]; st.classList.toggle('folded', S.fold[i]); h.setAttribute('aria-expanded', !S.fold[i]); };
    h.onclick = tog; h.onkeydown = e => { if (e.target === h && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); tog(); } };
    st.classList.toggle('folded', !!S.fold[i]);
    if (S.expl[i]) st.append(explBox(S.expl[i]));
  });
  box.querySelectorAll('[data-x]').forEach(b => b.onclick = e => { e.stopPropagation(); expliquer(+b.dataset.x, b, ctx, C); });
  box.querySelector('#tWhy') && (box.querySelector('#tWhy').onclick = async () => {
    S.showWhy = !S.showWhy; const w = box.querySelector('#whyBox');
    w.hidden = !S.showWhy; box.querySelector('#tWhy').setAttribute('aria-expanded', S.showWhy);
    if (!S.showWhy) return;
    if (!strat && !S.ia.pourquoi) { w.innerHTML = waitHTML('Je prépare l’explication…'); await outil('pourquoi', ctx, {}, r => { S.ia.pourquoi = r; }); }
    w.innerHTML = whyHTML(ctx, strat); ctx.typeset(w);
  });
  box.querySelector('#tAlt') && (box.querySelector('#tAlt').onclick = async () => {
    S.showAlt = !S.showAlt; const w = box.querySelector('#altBox');
    w.hidden = !S.showAlt; box.querySelector('#tAlt').setAttribute('aria-expanded', S.showAlt);
    if (!S.showAlt) return;
    if (!S.ia.autre) { w.innerHTML = waitHTML('Je cherche une autre méthode, puis je la fais relire… (jusqu’à une minute)'); await outil('autre', ctx, {}, r => { S.ia.autre = r; }); }
    w.innerHTML = altHTML(ctx); ctx.typeset(w); w.scrollIntoView({behavior: 'smooth', block: 'nearest'});
  });
  box.querySelector('#tFold').onclick = () => { const any = Object.values(S.fold).some(Boolean); C.forEach((_, i) => S.fold[i] = !any); draw(false); };
  box.querySelector('#tCopy').onclick = () => copier(`${ex.titre}\n\n${sol.corrige}${sol.reponse ? `\n\nRésultat : ${sol.reponse}` : ''}`);
  box.querySelector('#tShare')?.addEventListener('click', () => ctx.share());
  box.querySelector('#tReport').onclick = () => signaler(ctx, C, 'détaillée');
  stepNav(box); readingProgress(box);
  bindVerifier(box, ctx, draw);
}
const waitHTML = t => `<p class="wait"><span class="spin"></span> ${esc(t)}</p>`;
function whyHTML(ctx, strat) {
  if (strat) return `<aside class="callout thm why"><b class="callout-t">Pourquoi cette méthode — extrait de l’étape « ${esc(strat.title)} »</b>${rich(strat.md.replace(/^\*\*.+?\*\*\s*/, ''))}</aside>`;
  const r = ctx.S.ia.pourquoi;
  if (!r) return '';
  if (r.error) return `<p class="alert error">${esc(r.error)}</p>`;
  return `<aside class="callout thm why"><b class="callout-t">Pourquoi cette méthode</b>${rich(r.pourquoi)}${iaNote(r)}</aside>`;
}
function altHTML(ctx) {
  const r = ctx.S.ia.autre;
  if (!r) return '';
  if (r.error) return `<p class="alert error">${esc(r.error)}</p>`;
  if (r.existe === false) return `<aside class="callout note"><b class="callout-t">Autre méthode</b><p>Il n’y a pas d’autre méthode vraiment différente et raisonnable au programme pour cet exercice. ${esc(r.comparaison || '')}</p></aside>`;
  return `<section class="alt"><p class="sep" aria-hidden="true">∗</p><h4 class="alt-t">Autre méthode · ${inline(r.titre || '')}</h4>
    ${verifHTML(r)}<div class="corrige">${fmtCorrige(r.methode || '')}</div>
    ${r.comparaison ? `<aside class="callout note"><b class="callout-t">Laquelle choisir ?</b>${rich(r.comparaison)}</aside>` : ''}${iaNote(r)}</section>`;
}
function explBox(r) {
  const d = document.createElement('div'); d.className = 'expl';
  d.innerHTML = r.error ? `<p class="alert error">${esc(r.error)}</p>` : `<b class="callout-t">Cette étape mérite une explication</b>${rich(r.explication)}${iaNote(r)}`;
  return d;
}
async function expliquer(i, btn, ctx, C) {
  const {S} = ctx;
  const st = btn.closest('section.step');
  if (S.expl[i]) { delete S.expl[i]; st.querySelector('.expl')?.remove(); btn.setAttribute('aria-expanded', false); return; }
  btn.setAttribute('aria-expanded', true);
  const w = document.createElement('div'); w.className = 'expl'; w.innerHTML = waitHTML('Je détaille cette étape…'); st.append(w);
  await outil('expliquer', ctx, {etape: C[i]?.md || st.innerText}, r => { S.expl[i] = r; }, e => { S.expl[i] = {error: e}; });
  w.replaceWith(explBox(S.expl[i])); ctx.typeset(st);
}

/* ---------------- Mode rigoureux ---------------- */
function drawRigueur(box, ctx, draw) {
  const {S, K, ex} = ctx;
  if (gate(box, ctx, draw)) return;
  const sol0 = ctx.sol();
  // 1. Rédaction de concours écrite par l'équipe ; 2. à défaut, version courte tirée des étapes Résolution et Conclusion.
  const hand = sol0?.rigoureux;
  const C0 = sol0 ? stepChunks(sol0.corrige) : [];
  const res = C0.find(c => /^Résolution/i.test(c.title)), concl = C0.find(c => /^Conclusion/i.test(c.title));
  const strip = c => c ? c.md.replace(/^\*\*[^*]+\*\*\s*/, '') : '';
  const derive = !hand && res ? strip(res) + (concl ? '\n\n**Conclusion.** ' + strip(concl) : '') : '';
  if (hand || (derive && !IA())) {
    const txt = hand || derive;
    box.innerHTML = `<div class="ctools" role="toolbar" aria-label="Outils de la rédaction">
        <button class="tbtn" id="tCopy">${ic('link')} Copier</button><button class="tbtn warnb" id="tReport">${ic('x')} Signaler une erreur</button></div>
      <p class="rig-src">${hand ? `<span class="lab-ok">${ic('check')} Rédaction de concours</span> <span class="small">Écrite par l’équipe et vérifiée par calcul, comme une copie : objets définis, hypothèses vérifiées, conclusion par question.</span>`
        : `<span class="lab-warn">Version courte</span> <span class="small">Tirée de la résolution détaillée, sans les rappels ni les commentaires. La rédaction de concours complète de cet exercice arrive bientôt.</span>`}</p>
      ${figCorr(ex.id)}
      <div class="corrige rig">${fmtCorrige(txt)}</div>
      ${sol0.reponse ? `<div class="result"><span class="lab">Résultat</span><div>${rich(sol0.reponse)}</div></div>` : ''}`;
    box.querySelector('#tCopy').onclick = () => copier(`${ex.titre}\n\n${txt}`);
    box.querySelector('#tReport').onclick = () => signaler(ctx, stepChunks(txt), 'rigoureuse');
    ctx.record('solution');
    return;
  }
  if (!IA()) {
    box.innerHTML = `<div class="gate"><p class="gate-t">Pas encore de rédaction de concours pour cet exercice.</p>
      <p class="small">On les rédige une par une, en vérifiant chaque calcul. En attendant, le mode Détaillé contient la démonstration complète.</p>
      <button class="btn" id="toDet">${ic('book')} Voir la correction détaillée</button></div>`;
    box.querySelector('#toDet').onclick = () => document.querySelector('.modesel [data-m=detail]')?.click();
    return;
  }
  const r = S.ia.rigoureux;
  if (r && !r.error) {
    box.innerHTML = `<div class="ctools" role="toolbar" aria-label="Outils de la rédaction">
        <button class="tbtn" id="tCopy">${ic('link')} Copier</button><button class="tbtn warnb" id="tReport">${ic('x')} Signaler une erreur</button></div>
      ${verifHTML(r)}
      <div class="corrige rig">${fmtCorrige(r.redaction)}</div>
      ${r.reponse ? `<div class="result"><span class="lab">Résultat</span><div>${rich(r.reponse)}</div></div>` : ''}
      ${iaNote(r, K ? 'Rédaction générée par IA à partir de la correction de la plateforme.' : 'Rédaction générée par IA.')}
      ${verifierHTML(ctx)}`;
    box.querySelector('#tCopy').onclick = () => copier(`${ex.titre}\n\n${r.redaction}`);
    box.querySelector('#tReport').onclick = () => signaler(ctx, stepChunks(r.redaction), 'rigoureuse');
    bindVerifier(box, ctx, draw);
    return;
  }
  const sol = ctx.sol();
  box.innerHTML = S.tbusy.rigoureux ? waitHTML('Rédaction de la copie de concours, puis relecture indépendante… (une à deux minutes)')
    : `<div class="gate"><p class="gate-t">Une rédaction comme dans une excellente copie de concours.</p>
      <p class="small">Objets définis, hypothèses vérifiées au moment de chaque théorème, quantificateurs explicites, conclusion par question. Elle est rédigée par l’IA ${K ? 'à partir de la correction de la plateforme' : ''}, contrôlée par une seconde relecture indépendante, puis partagée avec tous les élèves : on ne la génère qu’une fois.</p>
      ${r?.error ? `<p class="alert error">${esc(r.error)}</p>` : ''}
      <button class="btn primary" id="genRig" ${DEMO ? 'disabled' : ''}>${ic('pen')} Afficher la rédaction rigoureuse</button>${DEMO ? '<p class="small">Indisponible en mode démonstration : elle nécessite la fonction « corriger » de Supabase.</p>' : ''}
      ${!sol && !K ? '<p class="small">Sans correction de référence, la rédaction sera produite directement à partir de l’énoncé.</p>' : ''}</div>`;
  box.querySelector('#genRig')?.addEventListener('click', async () => {
    S.tbusy.rigoureux = true; draw(false);
    await outil('rigoureux', ctx, {}, x => { S.ia.rigoureux = x; }, e => { S.ia.rigoureux = {error: e}; });
    S.tbusy.rigoureux = false; ctx.record('solution'); draw(true);
  });
}

/* ---------------- « Vérifier ma réponse » : analyse de la démarche de l'élève ---------------- */
function verifierHTML(ctx) {
  if (!IA()) return '';
  const {S} = ctx, a = S.analyse;
  return `<details class="verif" ${S.openV ? 'open' : ''}><summary>${ic('check')} <b>Vérifier ma réponse</b><span class="small">résultat ou démarche : on cherche ta première erreur, sans te donner la solution</span></summary>
    <div class="verif-b">
      <textarea id="vTxt" class="note" maxlength="4000" placeholder="Écris ton résultat, ou les grandes étapes de ta démarche. Formules entre $…$." aria-label="Ta réponse ou ta démarche">${esc(S.vTxt || '')}</textarea>
      <div class="row-b"><button class="btn primary" id="vGo" ${DEMO ? 'disabled' : ''}>${ic('check')} Vérifier ma réponse</button>${DEMO ? '<span class="small">Indisponible en mode démonstration.</span>' : '<span class="small">Analyse faite par l’IA à partir de la correction de référence.</span>'}</div>
      <div id="vOut">${a ? analyseHTML(a) : ''}</div></div></details>`;
}
const VERD = {juste: ['ok', 'Ta réponse est juste'], partiel: ['warn', 'C’est en partie juste'], faux: ['err', 'Il y a une erreur'], incomplet: ['warn', 'Difficile de juger avec si peu']};
const TYPE = {calcul: 'erreur de calcul', methode: 'erreur de méthode', raisonnement: 'erreur de raisonnement', redaction: 'problème de rédaction'};
function analyseHTML(a) {
  if (a.error) return `<p class="alert error">${esc(a.error)}</p>`;
  const [k, t] = VERD[a.verdict] || VERD.incomplet;
  const e = a.premiere_erreur;
  return `<div class="ana ${k}"><p class="ana-v"><b>${t}.</b> ${inline(a.resume || '')}</p>
    ${(a.points_justes || []).length ? `<p class="lab2">Ce qui est juste</p><ul class="bul">${a.points_justes.map(x => `<li>${inline(x)}</li>`).join('')}</ul>` : ''}
    ${e && e.explication ? `<p class="lab2">Première erreur · ${esc(TYPE[e.type] || 'erreur')}</p>${e.citation ? `<blockquote class="cit">${inline(e.citation)}</blockquote>` : ''}${rich(e.explication)}` : ''}
    ${a.piste ? `<p class="lab2">Pour reprendre</p>${rich(a.piste)}` : ''}
    <p class="small">Analyse automatique : elle peut se tromper. En cas de doute, demande l’avis de ton groupe.</p></div>`;
}
function bindVerifier(box, ctx) {
  const {S} = ctx;
  const d = box.querySelector('details.verif'); if (!d) return;
  d.addEventListener('toggle', () => { S.openV = d.open; });
  const t = box.querySelector('#vTxt'); t.oninput = () => { S.vTxt = t.value; };
  const go = box.querySelector('#vGo');
  go.onclick = async () => {
    const v = t.value.trim();
    if (v.length < 2) { toast('Écris d’abord ta réponse ou ta démarche.', 'error'); t.focus(); return; }
    if (S.tbusy.analyse) return;
    S.tbusy.analyse = true; const undo = busy(go, 'Analyse en cours…');
    await outil('analyse', ctx, {reponse_eleve: v}, r => { S.analyse = r; }, e => { S.analyse = {error: e}; });
    S.tbusy.analyse = false; undo();
    const o = box.querySelector('#vOut'); o.innerHTML = analyseHTML(S.analyse); ctx.typeset(o);
  };
}

/* ---------------- utilitaires ---------------- */
function verifHTML(r) {
  const v = r?.verification; if (!v) return '';
  const [k, t] = VERIF[v.statut] || VERIF.non_relu;
  return `<div class="relu ${k}"><b>${k === 'ok' ? ic('check') : ''} Relecture automatique.</b> ${t}${(v.remarques || []).length ? `<ul class="bul">${v.remarques.map(x => `<li>${inline(x)}</li>`).join('')}</ul>` : ''}</div>`;
}
function iaNote(r, extra = '') {
  return `<p class="ianote">${ic('bulb')} ${esc(extra || 'Contenu généré par IA.')} Il n’a pas été relu par un professeur : vérifie-le avec ton cours.${r?.cache ? ' <span class="mono">· déjà généré pour un autre élève</span>' : ''}</p>`;
}
function srcHTML(ctx) {
  const {K, S} = ctx;
  if (K) return `<p class="corr-src"><span class="lab-ok">${ic('check')} Correction de la plateforme</span><span class="small">Rédigée et vérifiée par calcul avant publication. Une erreur ? Signale-la.</span></p>`;
  return `<p class="corr-src"><span class="lab-warn">${ic('bulb')} Correction générée par IA</span><span class="small">${S.relu ? 'Relue par une seconde passe automatique indépendante' + (S.verif?.statut === 'corrige' ? ', qui a corrigé des erreurs du premier jet' : S.verif?.statut === 'incertain' ? ', qui signale des points incertains' : '') + '.' : 'Non relue.'} Vérifie-la avec ton cours.</span></p>
    ${S.verif?.remarques?.length && S.verif.statut !== 'conforme' ? `<details class="nprev"><summary>Remarques de la relecture</summary><ul>${S.verif.remarques.map(x => `<li>${rich(x)}</li>`).join('')}</ul></details>` : ''}`;
}
// Appel d'un outil IA, avec anti-doublon (un seul appel en cours par outil et par étape).
async function outil(mode, ctx, extra, ok, ko) {
  const {ex, K, S} = ctx;
  const key = mode + (extra.etape ? ':' + extra.etape.length : '');
  if (S.tbusy[key + '!']) return;
  S.tbusy[key + '!'] = true;
  try {
    const sol = ctx.sol();
    const reference = K ? `${K.corrige}\n\nRÉSULTAT ATTENDU : ${K.reponse}` : sol ? `${sol.corrige}${sol.reponse ? `\n\nRÉSULTAT ATTENDU : ${sol.reponse}` : ''}` : '';
    const r = await api.ia({mode, filiere: filiere(), reference,
      exercice: {id: ex.id, titre: ex.titre, mat: ex.mat, chap: ex.chap, niveau: ex.niveau, enonce: ex.enonce}, ...extra});
    ok(r);
  } catch (e) {
    const m = e?.message || 'Service indisponible, réessaie dans un instant.';
    if (ko) ko(m); else ok({error: m});
  } finally { delete S.tbusy[key + '!']; }
}
async function copier(t) {
  try { await navigator.clipboard.writeText(t); toast('Correction copiée (texte et LaTeX).', 'ok'); }
  catch { toast('Copie impossible dans ce navigateur.', 'error'); }
}
function signaler(ctx, C, mode) {
  const dlg = document.createElement('dialog'); dlg.className = 'dlg';
  dlg.innerHTML = `<form method="dialog" class="dlg-in"><header><h2>Signaler une erreur</h2><button class="iconbtn" value="x" formnovalidate aria-label="Fermer">${ic('x')}</button></header>
    <p class="small">Merci ! Chaque signalement est relu. Dis-nous où se trouve le problème et ce qui te semble faux.</p>
    <div class="fld"><label for="seW">Où ?</label><select id="seW" name="ou"><option value="">Je ne sais pas / partout</option>${C.map((c, i) => `<option>${esc((c.n ? 'Étape ' + c.n + ' — ' : '') + c.title).slice(0, 80)}</option>`).join('')}<option>Résultat final</option><option>Énoncé</option></select></div>
    <div class="fld"><label for="seD">Ce qui te semble faux</label><textarea id="seD" name="details" maxlength="420" rows="4" required placeholder="Par exemple : à la ligne 2, le facteur 2 a disparu."></textarea></div>
    <footer><button class="btn ghost" value="x" formnovalidate>Annuler</button><button class="btn primary" value="ok">Envoyer</button></footer></form>`;
  document.body.append(dlg);
  dlg.addEventListener('close', async () => {
    const f = dlg.querySelector('form');
    if (dlg.returnValue === 'ok' && f.details.value.trim()) {
      try { await api.signaler('corrige', ctx.ex.id, 'erreur', `[${mode}] ${f.ou.value ? f.ou.value + ' : ' : ''}${f.details.value.trim()}`.slice(0, 500)); toast('Signalement envoyé. Merci pour ta relecture !', 'ok'); }
      catch (x) { toast(x.message, 'error'); }
    }
    dlg.remove();
  });
  dlg.showModal();
}
