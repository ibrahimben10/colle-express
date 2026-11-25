// Page d'accueil : la bibliothèque en chiffres (calculés sur les vraies données), un carrousel d'exercices
// réels et un petit laboratoire interactif (maths, physique, informatique). Aucune donnée inventée.
import { esc, fmtEnonce } from './format.js';
import { ic, chapIcon } from './icons.js';
import { FIG } from './figures.js';
import { countUp } from './vivant.js';

const LV = {1: 'CCINP', 2: 'Mines-Centrale', 3: 'X-ENS'};
const MAT = ['Maths', 'Physique', 'Chimie'];
const reduce = () => matchMedia('(prefers-reduced-motion: reduce)').matches;
const typeset = el => { if (window.MathJax?.typesetPromise) MathJax.typesetPromise([el]).catch(() => {}); else setTimeout(() => typeset(el), 500); };

/* ---------- extrait d'énoncé : on coupe hors des formules ---------- */
export function extrait(t, max = 230) {
  const p = String(t).trim().split(/\n{2,}/)[0].replace(/\n/g, ' ');
  if (p.length <= max) return p;
  let out = '', inMath = false;
  for (const part of p.split(/(\$\$?)/)) {
    if (/^\$\$?$/.test(part)) { inMath = !inMath; out += part; continue; }
    if (!inMath && out.length + part.length > max) { const cut = part.slice(0, Math.max(0, max - out.length)); out += cut.replace(/\s+\S*$/, '') + '…'; break; }
    out += part;
  }
  return out;
}

/* ---------- 1. Les chiffres ---------- */
function chiffres(E) {
  const box = document.getElementById('chiffresBox'); if (!box) return;
  const n = E.length, chap = new Set(E.map(e => e.mat + e.chap)).size, sch = E.filter(e => FIG[e.id]).length;
  const by = m => E.filter(e => e.mat === m).length, lv = k => E.filter(e => e.niveau === k).length;
  box.innerHTML = `
    <div class="ch-big"><b data-n="${n}">${n}</b><span>exercices corrigés pas à pas</span></div>
    <dl class="ch-list">
      <div><dt>chapitres</dt><dd data-n="${chap}">${chap}</dd></div>
      <div><dt>schémas tracés à la main… en SVG</dt><dd data-n="${sch}">${sch}</dd></div>
      <div><dt>niveaux de concours</dt><dd>3</dd></div>
    </dl>
    <div class="ch-bars" role="img" aria-label="${MAT.map(m => `${m} : ${by(m)}`).join(', ')}">
      ${MAT.map(m => `<div class="ch-row"><span>${m}</span><i style="--w:${(100 * by(m) / n).toFixed(1)}%" class="m-${m}"></i><b>${by(m)}</b></div>`).join('')}
    </div>
    <div class="ch-lv">${[1, 2, 3].map(k => `<span class="stamp n${k}">${LV[k]}</span><b>${lv(k)}</b>`).join('')}</div>`;
  const io = new IntersectionObserver(es => es.forEach(x => {
    if (!x.isIntersecting) return; io.disconnect(); box.classList.add('on');
    if (!reduce()) box.querySelectorAll('[data-n]').forEach(el => countUp(el, +el.dataset.n));
  }), {threshold: .3});
  io.observe(box);
}

/* ---------- 2. Le carrousel d'exercices réels ---------- */
function vitrine(E) {
  const root = document.getElementById('vitrineBox'); if (!root) return;
  const pick = {
    'Nouveautés': E.filter(e => e.ajout).sort((a, b) => (b.ajout || '').localeCompare(a.ajout || '')),
    'Maths': E.filter(e => e.mat === 'Maths'),
    'Physique': E.filter(e => e.mat === 'Physique' && FIG[e.id]).concat(E.filter(e => e.mat === 'Physique' && !FIG[e.id])),
    'Chimie': E.filter(e => e.mat === 'Chimie')
  };
  // un échantillon varié : on alterne les chapitres et les niveaux plutôt que de prendre les premiers
  const varie = L => { const seen = new Set(), a = [], b = []; L.forEach(e => (seen.has(e.chap) ? b : (seen.add(e.chap), a)).push(e)); return a.concat(b).slice(0, 9); };
  let tab = 'Nouveautés';
  const card = e => `<article class="vx-card" data-mat="${e.mat}">
      <header><span class="tile ${e.mat}">${ic(chapIcon(e.mat, e.chap))}</span><span class="vx-meta"><b>${esc(e.chap)}</b><span>${esc(e.mat)} · ${e.duree} min</span></span><span class="stamp n${e.niveau}">${LV[e.niveau]}</span></header>
      <h3>${esc(e.titre)}</h3>
      ${FIG[e.id] ? `<div class="vx-fig">${FIG[e.id].svg}</div>` : `<div class="vx-txt enonce">${fmtEnonce(extrait(e.enonce))}</div>`}
      <footer><a class="ul" href="correction.html?id=${encodeURIComponent(e.id)}&amp;enonce=1">Lire l’énoncé ${ic('arrow')}</a>${e.ajout ? '<span class="vx-new">nouveau</span>' : ''}</footer>
    </article>`;
  const draw = () => {
    const L = varie(pick[tab]);
    root.querySelector('.vx-track').innerHTML = L.map(card).join('');
    root.querySelector('.vx-track').scrollTo({left: 0});
    root.querySelectorAll('.vx-tabs button').forEach(b => b.setAttribute('aria-pressed', b.dataset.t === tab));
    typeset(root.querySelector('.vx-track')); state();
  };
  root.innerHTML = `<div class="vx-head"><div class="vx-tabs" role="group" aria-label="Choisir une rubrique">${Object.keys(pick).map(t => `<button data-t="${t}">${t}</button>`).join('')}</div>
      <div class="vx-nav"><button class="iconbtn" data-d="-1" aria-label="Exercices précédents">${ic('chev')}</button><button class="iconbtn" data-d="1" aria-label="Exercices suivants">${ic('chev')}</button></div></div>
    <div class="vx-track" tabindex="0" aria-label="Exercices de la bibliothèque (faire défiler)"></div>`;
  const tr = root.querySelector('.vx-track');
  const step = () => (tr.querySelector('.vx-card')?.offsetWidth || 300) + 16;
  const state = () => { const [p, n] = root.querySelectorAll('.vx-nav button'); p.disabled = tr.scrollLeft < 8; n.disabled = tr.scrollLeft + tr.clientWidth > tr.scrollWidth - 8; };
  root.querySelector('.vx-tabs').onclick = e => { const b = e.target.closest('button'); if (b && b.dataset.t !== tab) { tab = b.dataset.t; draw(); } };
  root.querySelector('.vx-nav').onclick = e => { const b = e.target.closest('button'); if (b) tr.scrollBy({left: step() * b.dataset.d * (innerWidth < 700 ? 1 : 2), behavior: reduce() ? 'auto' : 'smooth'}); };
  tr.addEventListener('scroll', () => requestAnimationFrame(state), {passive: true});
  tr.addEventListener('keydown', e => { if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); tr.scrollBy({left: step() * (e.key === 'ArrowRight' ? 1 : -1), behavior: 'smooth'}); } });
  draw();
}

/* ---------- 3. Le laboratoire ---------- */
const W = 600, H = 280;
function plot({xmin, xmax, ymin, ymax}, curves, extra = '') {
  const X = x => (x - xmin) / (xmax - xmin) * W, Y = y => H - (y - ymin) / (ymax - ymin) * H;
  const path = (f, n = 240) => { let d = '', pen = false; for (let i = 0; i <= n; i++) { const x = xmin + (xmax - xmin) * i / n, y = f(x);
      if (!isFinite(y) || y < ymin - 5 * (ymax - ymin) || y > ymax + 5 * (ymax - ymin)) { pen = false; continue; }
      d += (pen ? 'L' : 'M') + X(x).toFixed(1) + ' ' + Y(Math.max(ymin - (ymax - ymin), Math.min(ymax + (ymax - ymin), y))).toFixed(1); pen = true; } return d; };
  return `<svg viewBox="0 0 ${W} ${H}" class="lab-plot" role="img"><defs><clipPath id="labclip"><rect width="${W}" height="${H}"/></clipPath></defs>
    <line class="ax" x1="0" x2="${W}" y1="${Y(0)}" y2="${Y(0)}"/><line class="ax" y1="0" y2="${H}" x1="${X(0)}" x2="${X(0)}"/>
    <g clip-path="url(#labclip)">${extra.replace(/\{X:([-\d.]+)\}/g, (_, v) => X(+v).toFixed(1)).replace(/\{Y:([-\d.]+)\}/g, (_, v) => Y(+v).toFixed(1))}
    ${curves.map(c => `<path class="${c.cls}" d="${path(c.f)}"/>`).join('')}</g></svg>`;
}
const fact = n => n < 2 ? 1 : n * fact(n - 1);
const LABS = {
  maths: {
    titre: 'Taylor en direct', ex: /Taylor|développement limité/i,
    texte: n => `Le polynôme de Taylor de $\\sin$ en $0$ à l’ordre ${2 * n + 1} colle à la courbe sur un intervalle qui s’élargit avec l’ordre. Hors de cet intervalle, il s’en écarte très vite : c’est tout l’enjeu du reste.`,
    ctl: {k: 'n', min: 0, max: 7, val: 2, lab: v => `ordre ${2 * v + 1}`},
    draw(n) {
      const T = x => { let s = 0; for (let k = 0; k <= n; k++) s += (-1) ** k * x ** (2 * k + 1) / fact(2 * k + 1); return s; };
      let r = 0; for (let x = 0; x < 12; x += .01) { if (Math.abs(T(x) - Math.sin(x)) > .1) break; r = x; }
      return {svg: plot({xmin: -12, xmax: 12, ymin: -2.2, ymax: 2.2}, [{cls: 'c1', f: Math.sin}, {cls: 'c2', f: T}],
        `<rect class="zone" x="{X:${-r}}" width="${(2 * r / 24 * W).toFixed(1)}" y="0" height="${H}"/>`),
        info: `écart inférieur à 0,1 sur [−${r.toFixed(1).replace('.', ',')} ; ${r.toFixed(1).replace('.', ',')}]`};
    }
  },
  physique: {
    titre: 'Oscillateur amorti', ex: /oscillat|amorti/i,
    texte: () => `$\\ddot x+\\dfrac{\\omega_0}{Q}\\dot x+\\omega_0^2x=0$, lâché sans vitesse depuis $x_0$. Fais varier le facteur de qualité $Q$ : au-dessus de $\\tfrac12$ le régime est pseudo-périodique, en dessous il est apériodique.`,
    ctl: {k: 'Q', min: 0, max: 40, val: 30, lab: v => `Q = ${q(v).toFixed(2).replace('.', ',')}`},
    draw(v) {
      const Q = q(v), w0 = 1, l = w0 / (2 * Q), x = t => {
        if (Math.abs(Q - .5) < 1e-3) return (1 + w0 * t) * Math.exp(-w0 * t);
        if (Q > .5) { const w = w0 * Math.sqrt(1 - 1 / (4 * Q * Q)); return Math.exp(-l * t) * (Math.cos(w * t) + l / w * Math.sin(w * t)); }
        const s = w0 * Math.sqrt(1 / (4 * Q * Q) - 1), r1 = -l + s, r2 = -l - s; return (r2 * Math.exp(r1 * t) - r1 * Math.exp(r2 * t)) / (r2 - r1);
      };
      const reg = Math.abs(Q - .5) < 1e-3 ? 'critique' : Q > .5 ? 'pseudo-périodique' : 'apériodique';
      return {svg: plot({xmin: 0, xmax: 30, ymin: -1.1, ymax: 1.1}, [{cls: 'env', f: t => Q > .5 ? Math.exp(-l * t) : NaN}, {cls: 'env', f: t => Q > .5 ? -Math.exp(-l * t) : NaN}, {cls: 'c1', f: x}]),
        info: `régime ${reg}`};
    }
  },
  info: {
    titre: 'Dichotomie pas à pas', ex: /dichotom|valeurs intermédiaires/i,
    texte: () => `On cherche le zéro de $f(x)=x^2-2$ sur $[0,2]$. À chaque étape on garde la moitié où $f$ change de signe : l’intervalle est divisé par $2$, donc $n$ étapes donnent environ $0{,}3\\,n$ décimales exactes.`,
    ctl: {k: 'étapes', min: 0, max: 20, val: 3, lab: v => `${v} étape${v > 1 ? 's' : ''}`},
    draw(n) {
      let a = 0, b = 2; const f = x => x * x - 2, hist = [];
      for (let i = 0; i < n; i++) { const m = (a + b) / 2; hist.push([a, b]); if (f(a) * f(m) <= 0) b = m; else a = m; }
      // chaque étape = un segment, empilés sous l'axe : on voit l'intervalle se resserrer autour de √2
      const rows = hist.concat([[a, b]]).slice(-7), y0 = -.35, dy = .27;
      const segs = rows.map(([u, v], i) => { const y = y0 - i * dy, last = i === rows.length - 1;
        return `<line class="seg${last ? ' cur' : ''}" x1="{X:${u}}" x2="{X:${v}}" y1="{Y:${y}}" y2="{Y:${y}}"/><line class="tk" x1="{X:${u}}" x2="{X:${u}}" y1="{Y:${y + .06}}" y2="{Y:${y - .06}}"/><line class="tk" x1="{X:${v}}" x2="{X:${v}}" y1="{Y:${y + .06}}" y2="{Y:${y - .06}}"/>`; }).join('');
      return {svg: plot({xmin: -.1, xmax: 2.1, ymin: -2.2, ymax: 2.4}, [{cls: 'c1', f}],
        `<rect class="zone" x="{X:${a}}" width="${Math.max(1.5, (b - a) / 2.2 * W).toFixed(1)}" y="0" height="${H}"/>` + segs + `<line class="root" x1="{X:${Math.SQRT2}}" x2="{X:${Math.SQRT2}}" y1="0" y2="${H}"/>`),
        info: `√2 ∈ [${a.toFixed(6).replace('.', ',')} ; ${b.toFixed(6).replace('.', ',')}] · largeur ${(b - a).toExponential(1).replace('.', ',')}`};
    }
  }
};
const q = v => v <= 20 ? .05 + v * (.45 / 20) : .5 + (v - 20) * (9.5 / 20);   // curseur : fin autour de 1/2, large au-delà
function labo(E) {
  const root = document.getElementById('laboBox'); if (!root) return;
  let cur = 'maths';
  const lien = k => { const e = E.find(x => LABS[k].ex.test(x.chap + ' ' + x.titre)); return e ? `<a class="ul" href="correction.html?id=${encodeURIComponent(e.id)}&amp;enonce=1">Un exercice sur ce thème : ${esc(e.titre)} ${ic('arrow')}</a>` : ''; };
  root.innerHTML = `<div class="lab-tabs" role="tablist">${[['maths', 'Maths', 'sigma'], ['physique', 'Physique', 'wave'], ['info', 'Informatique', 'code']].map(([k, l, i]) =>
      `<button role="tab" id="lt-${k}" aria-controls="labPanel" data-k="${k}">${ic(i)}${l}</button>`).join('')}</div>
    <div class="lab-panel" id="labPanel" role="tabpanel"><div class="lab-txt"><h3></h3><p class="enonce"></p><label class="lab-ctl"><span></span><input type="range"></label><output class="mono"></output><p class="lab-link small"></p></div><div class="lab-fig"></div></div>`;
  const P = root.querySelector('.lab-panel'), inp = P.querySelector('input'), lab = P.querySelector('.lab-ctl span'), out = P.querySelector('output'), fig = P.querySelector('.lab-fig');
  const render = () => { const L = LABS[cur], v = +inp.value, r = L.draw(v); fig.innerHTML = r.svg; inp.style.setProperty('--p', (100 * (v - inp.min) / (inp.max - inp.min)) + '%'); lab.textContent = L.ctl.lab(v); out.textContent = r.info; };
  const select = k => {
    cur = k; const L = LABS[k];
    root.querySelectorAll('[role=tab]').forEach(b => { b.setAttribute('aria-selected', b.dataset.k === k); b.tabIndex = b.dataset.k === k ? 0 : -1; });
    P.setAttribute('aria-labelledby', 'lt-' + k);
    P.querySelector('h3').textContent = L.titre; P.querySelector('.enonce').innerHTML = fmtEnonce(L.texte(L.ctl.val));
    Object.assign(inp, {min: L.ctl.min, max: L.ctl.max, value: L.ctl.val, step: 1}); inp.setAttribute('aria-label', L.titre);
    P.querySelector('.lab-link').innerHTML = lien(k);
    typeset(P); render();
  };
  inp.oninput = render;
  root.querySelector('.lab-tabs').onclick = e => { const b = e.target.closest('[role=tab]'); if (b) select(b.dataset.k); };
  root.querySelector('.lab-tabs').onkeydown = e => {
    const ks = Object.keys(LABS), i = ks.indexOf(cur);
    if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { const k = ks[(i + (e.key === 'ArrowRight' ? 1 : ks.length - 1)) % ks.length]; select(k); root.querySelector('#lt-' + k).focus(); }
  };
  select('maths');
}

export async function initVitrine() {
  if (!document.getElementById('chiffresBox')) return;
  let E = [];
  try { E = await fetch('data/exercices.json').then(r => r.json()); } catch { return; }
  chiffres(E); vitrine(E); labo(E);
}
