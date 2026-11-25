// Animations et composants vivants : mot tournant, compteurs, fond scientifique, carrousel,
// célébration, progression de lecture, navigation entre étapes, mode concentration, bannière de profil.
// Tout est en CSS + IntersectionObserver + rAF ; rien ne tourne quand l'élément est hors écran
// ou quand l'utilisateur a demandé moins d'animations.
const reduce = () => matchMedia('(prefers-reduced-motion: reduce)').matches;
const onScreen = (el, cb, opt = {threshold: .15}) => {
  if (!('IntersectionObserver' in window)) { cb(true); return; }
  new IntersectionObserver(es => es.forEach(e => cb(e.isIntersecting)), opt).observe(el);
};

/* ---------- mot tournant ---------- */
export function rotator(root = document) {
  const r = root.querySelector('.rot'); if (!r) return;
  const words = [...r.children]; let i = 0, t = 0, visible = true;
  words[0].classList.add('on');
  onScreen(r, v => { visible = v; });
  if (reduce()) return;
  t = setInterval(() => {
    if (!visible || document.hidden) return;
    words[i].classList.replace('on', 'off');
    const prev = words[i]; setTimeout(() => prev.classList.remove('off'), 500);
    i = (i + 1) % words.length; words[i].classList.add('on');
  }, 2200);
  return () => clearInterval(t);
}

/* ---------- compteurs ---------- */
export function countUp(el, to) {
  to = +to; if (!Number.isFinite(to)) return;
  el.dataset.count = to;
  if (reduce()) { el.textContent = to.toLocaleString('fr-FR'); return; }
  let done = false;
  onScreen(el, v => {
    if (!v || done) return; done = true;
    const t0 = performance.now(), d = 1100;
    const step = t => { const k = Math.min(1, (t - t0) / d), e = 1 - Math.pow(1 - k, 3); el.textContent = Math.round(to * e).toLocaleString('fr-FR'); if (k < 1) requestAnimationFrame(step); };
    requestAnimationFrame(step);
  });
}

/* ---------- fond scientifique : pause hors écran + léger parallaxe ---------- */
export function heroBackground() {
  const svg = document.querySelector('.hero-sci'); if (!svg) return;
  let vis = true;
  onScreen(svg, v => { vis = v; svg.classList.toggle('paused', !v); }, {threshold: 0});
  if (reduce()) return;
  let raf = 0;
  addEventListener('scroll', () => {
    if (!vis || raf) return;
    raf = requestAnimationFrame(() => { raf = 0; svg.style.transform = `translate3d(0, ${Math.min(scrollY, 900) * .18}px, 0)`; });
  }, {passive: true});
}

/* ---------- carrousel ---------- */
export function carousel(root) {
  if (!root) return;
  const track = root.querySelector('.car-track'), slides = [...track.children];
  const dots = root.querySelector('.car-dots'), bar = root.querySelector('.car-bar'), play = root.querySelector('[data-car=play]');
  const DUR = 7000;
  let i = 0, paused = reduce(), hold = false, visible = false, timer = 0, idle = 0;
  dots.innerHTML = slides.map((s, k) => `<button type="button" role="tab" aria-label="Diapositive ${k + 1} : ${s.querySelector('h3').textContent}"></button>`).join('');
  const dotBtns = [...dots.children];
  root.style.setProperty('--dur', DUR + 'ms');
  const mark = k => {
    i = k;
    slides.forEach((s, j) => { s.classList.toggle('on', j === k); s.setAttribute('aria-hidden', j !== k); s.inert = j !== k; });
    dotBtns.forEach((d, j) => d.setAttribute('aria-selected', j === k));
    bar.classList.remove('run'); void bar.offsetWidth; if (!paused && !hold && visible) bar.classList.add('run');
  };
  const go = (k, smooth = true) => {
    k = (k + slides.length) % slides.length;
    track.scrollTo({left: slides[k].offsetLeft - track.offsetLeft, behavior: smooth && !reduce() ? 'smooth' : 'auto'});
    mark(k); schedule();
  };
  const schedule = () => {
    clearTimeout(timer);
    if (paused || hold || !visible) { bar.classList.remove('run'); return; }
    bar.classList.remove('run'); void bar.offsetWidth; bar.classList.add('run');
    timer = setTimeout(() => go(i + 1), DUR);
  };
  const setPaused = p => { paused = p; play.setAttribute('aria-pressed', p); play.textContent = p ? '▶' : '❚❚';
    play.setAttribute('aria-label', p ? 'Reprendre le défilement' : 'Mettre en pause le défilement'); root.classList.toggle('is-paused', p); schedule(); };
  // l'utilisateur interagit : on suspend, puis on reprend après un moment de calme
  const interact = () => { hold = true; schedule(); clearTimeout(idle); idle = setTimeout(() => { hold = false; schedule(); }, 9000); };
  root.addEventListener('pointerenter', () => { hold = true; schedule(); });
  root.addEventListener('pointerleave', () => { hold = false; schedule(); });
  root.addEventListener('focusin', () => { hold = true; schedule(); });
  root.addEventListener('focusout', e => { if (!root.contains(e.relatedTarget)) { hold = false; schedule(); } });
  track.addEventListener('pointerdown', interact, {passive: true});
  track.addEventListener('wheel', interact, {passive: true});
  // défilement tactile : la diapositive la plus visible devient l'active
  let st = 0;
  track.addEventListener('scroll', () => { clearTimeout(st); st = setTimeout(() => {
    const k = Math.round((track.scrollLeft) / track.clientWidth); if (k !== i && slides[k]) { mark(k); schedule(); } }, 90); }, {passive: true});
  track.addEventListener('keydown', e => { if (e.key === 'ArrowRight') { e.preventDefault(); interact(); go(i + 1); } if (e.key === 'ArrowLeft') { e.preventDefault(); interact(); go(i - 1); } });
  root.querySelector('[data-car=prev]').onclick = () => { interact(); go(i - 1); };
  root.querySelector('[data-car=next]').onclick = () => { interact(); go(i + 1); };
  dotBtns.forEach((d, k) => d.onclick = () => { interact(); go(k); });
  play.onclick = () => setPaused(!paused);
  onScreen(root, v => { visible = v; schedule(); }, {threshold: .35});
  document.addEventListener('visibilitychange', () => schedule());
  setPaused(paused); mark(0);
}

/* ---------- célébration discrète ---------- */
export function celebrate(anchor, msg) {
  const el = document.createElement('div'); el.className = 'celebrate'; el.setAttribute('aria-hidden', 'true');
  el.innerHTML = '<svg viewBox="0 0 52 52"><circle cx="26" cy="26" r="23"/><path d="M15 27 l8 8 l15 -17"/></svg>' + '<i></i>'.repeat(8);
  (anchor || document.body).append(el);
  setTimeout(() => el.remove(), 1600);
  if (msg) import('./ui.js').then(m => m.toast(msg, 'ok'));
}

/* ---------- progression de lecture d'une section (une seule barre, un seul écouteur) ---------- */
let RP = null, rpBar = null, rpRaf = 0;
function rpUpdate() {
  rpRaf = 0; if (!rpBar) return;
  if (!RP || !RP.isConnected || !RP.offsetHeight) { rpBar.classList.remove('on'); return; }
  const r = RP.getBoundingClientRect(), h = r.height - innerHeight * .6;
  const p = h > 0 ? Math.min(1, Math.max(0, -r.top / h)) : (r.top < innerHeight ? 1 : 0);
  rpBar.classList.toggle('on', r.top < innerHeight * .5 && r.bottom > 0);
  rpBar.firstChild.style.transform = `scaleX(${p})`;
}
export function readingProgress(section) {
  RP = section;
  if (!rpBar) {
    rpBar = document.createElement('div'); rpBar.className = 'read-prog'; rpBar.innerHTML = '<i></i>'; rpBar.setAttribute('aria-hidden', 'true'); document.body.append(rpBar);
    addEventListener('scroll', () => { if (!rpRaf) rpRaf = requestAnimationFrame(rpUpdate); }, {passive: true});
  }
  rpUpdate();
}

/* ---------- navigation entre les étapes d'une correction ---------- */
export function stepNav(box) {
  const steps = [...box.querySelectorAll('.corrige > section.step')]; if (steps.length < 3) return;
  const nav = document.createElement('nav'); nav.className = 'stepnav'; nav.setAttribute('aria-label', 'Étapes de la correction');
  nav.innerHTML = steps.map((s, k) => { const h = s.querySelector('h4')?.cloneNode(true); h?.querySelectorAll('.en,.sr,.stools').forEach(x => x.remove()); const t = (h?.textContent || '').trim();
    return `<a href="#" data-k="${k}" title="${t.replace(/"/g, '&quot;')}"><b>${k + 1}</b><span>${t}</span></a>`; }).join('');
  box.querySelector('.corrige').before(nav);
  const links = [...nav.children];
  nav.onclick = e => { const a = e.target.closest('a'); if (!a) return; e.preventDefault(); steps[+a.dataset.k].scrollIntoView({behavior: reduce() ? 'auto' : 'smooth', block: 'start'}); };
  if (!('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) links.forEach((l, k) => l.classList.toggle('cur', steps[k] === e.target)); }), {rootMargin: '-30% 0px -60% 0px'});
  steps.forEach(s => io.observe(s));
}

/* ---------- bannière de profil : un tracé scientifique propre à chaque membre ---------- */
// Bannière de profil : un motif scientifique tracé à partir de l'identifiant (stable d'une visite à l'autre).
// choix = « motif:couleur » choisi par l'élève ; vide = onde amortie terracotta.
export const BANNIERES = {motifs: [['onde', 'Onde amortie'], ['lissajous', 'Courbe de Lissajous'], ['champ', 'Lignes de champ'], ['grille', 'Papier millimétré']],
  couleurs: [['terra', 'Terracotta'], ['vert', 'Vert académique'], ['encre', 'Encre'], ['ambre', 'Ambre']]};
export function bannerSVG(seed = '', choix = '') {
  let h = 2166136261; for (const c of String(seed)) h = Math.imul(h ^ c.charCodeAt(0), 16777619);
  const rnd = () => ((h = Math.imul(h ^ (h >>> 15), 2246822507) ^ Math.imul(h ^ (h >>> 13), 3266489909)) >>> 0) / 4294967296;
  const [m0, c0] = String(choix).split(':'), motif = BANNIERES.motifs.some(x => x[0] === m0) ? m0 : 'onde', coul = BANNIERES.couleurs.some(x => x[0] === c0) ? c0 : 'terra';
  const a = 18 + rnd() * 26, f = 1.5 + rnd() * 3, ph = rnd() * 6.28, d = .3 + rnd() * .7;
  const poly = (fn, n = 240) => Array.from({length: n + 1}, (_, k) => { const [x, y] = fn(k / n); return `${x.toFixed(1)},${y.toFixed(1)}`; }).join(' ');
  let body = '';
  if (motif === 'onde') {
    body = `<polyline points="${poly(t => [1200 * t, 70 + a * Math.exp(-d * t * 2) * Math.sin(f * 6.28 * t + ph)], 60)}" class="b1"/>
      <polyline points="${poly(t => [1200 * t, 70 + a * .55 * Math.cos(f * 4.1 * t + ph)], 60)}" class="b2"/>`;
  } else if (motif === 'lissajous') {
    const p = 3 + Math.floor(rnd() * 3), q = p + 1 + Math.floor(rnd() * 2);
    body = `<polyline points="${poly(t => [600 + 540 * Math.sin(p * 6.2832 * t + ph), 70 + 52 * Math.sin(q * 6.2832 * t)], 600)}" class="b1"/>`;
  } else if (motif === 'champ') {
    // lignes de champ d'un dipôle : familles de courbes y = k·sin(πx/L)^2 (vue schématique)
    body = Array.from({length: 7}, (_, i) => { const k = (i - 3) * 22 + (rnd() - .5) * 6;
      return `<polyline points="${poly(t => [1200 * t, 70 + k * Math.sin(Math.PI * t) ** (1.4 + rnd() * .2)], 80)}" class="${i === 3 ? 'b1' : 'b2'}"/>`; }).join('');
  } else {
    const x0 = 200 + rnd() * 800;
    body = Array.from({length: 25}, (_, i) => `<line x1="${i * 50}" x2="${i * 50}" y1="0" y2="140" class="b0 g"/>`).join('') + Array.from({length: 4}, (_, i) => `<line x1="0" x2="1200" y1="${i * 35 + 17}" y2="${i * 35 + 17}" class="b0 g"/>`).join('')
      + `<polyline points="${poly(t => [1200 * t, 125 - 110 * ((1200 * t - x0) / 700) ** 2], 120)}" class="b1"/><line x1="${x0 - 300}" x2="${x0 + 300}" y1="125" y2="125" class="b2"/>`;
  }
  return `<svg class="pf-banner bn-${coul}" viewBox="0 0 1200 140" preserveAspectRatio="none" aria-hidden="true">${motif === 'grille' ? '' : '<line x1="0" y1="70" x2="1200" y2="70" class="b0"/>'}${body}</svg>`;
}
