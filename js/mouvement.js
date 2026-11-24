// Mouvement : une couche d'animations posée sur l'application, sans toucher au rendu.
// Elle observe le DOM (MutationObserver) et réagit aux gestes : apparition en cascade de la liste,
// ondulation au toucher, cœur qui éclate, compteurs qui défilent, cartes qui se révèlent au défilement,
// célébration à la première réussite d'un exercice. Rien ne bouge si l'utilisateur a demandé moins d'animations.
import { celebrate } from './vivant.js';

const reduce = () => matchMedia('(prefers-reduced-motion: reduce)').matches;
const buzz = ms => { try { navigator.vibrate?.(ms); } catch {} };
const store = {get(k, d) { try { return JSON.parse(localStorage.getItem('ce:' + k)) ?? d; } catch { return d; } },
               set(k, v) { try { localStorage.setItem('ce:' + k, JSON.stringify(v)); } catch {} }};

/* ---------- liste des exercices : cascade, seulement quand son contenu change ---------- */
let sig = '', sigT = 0;
function stagger(box) {
  const items = [...box.querySelectorAll(':scope > .item')];
  const s = items.map(i => i.dataset.id).join(',');
  // même liste re-dessinée : pas de nouvelle cascade, sauf si la précédente est encore en cours
  if (s === sig && performance.now() - sigT > 700) { box.classList.add('still'); return; }
  if (s !== sig) sigT = performance.now();
  sig = s; box.classList.remove('still');
  items.forEach((it, k) => it.style.setProperty('--i', Math.min(k, 14)));
}

/* ---------- ondulation au toucher ---------- */
const RIPPLE = '.btn, .item, .bottombar a, nav.tabs a, .seg button, .favtoggle, .modesel button';
function ripple(e) {
  if (reduce() || e.button > 0) return;
  const t = e.target.closest(RIPPLE); if (!t || t.disabled) return;
  const r = t.getBoundingClientRect(), d = Math.max(r.width, r.height) * 2;
  const s = document.createElement('span'); s.className = 'rip';
  s.style.cssText = `width:${d}px;height:${d}px;left:${e.clientX - r.left - d / 2}px;top:${e.clientY - r.top - d / 2}px`;
  t.classList.add('has-rip'); t.append(s);
  setTimeout(() => s.remove(), 650);
}

/* ---------- favori : le cœur éclate ---------- */
function heart(btn) {
  btn.classList.remove('beat'); void btn.offsetWidth; btn.classList.add('beat');
  if (btn.getAttribute('aria-pressed') !== 'true') return;
  buzz(12);
  if (reduce()) return;
  const b = document.createElement('span'); b.className = 'burst'; b.setAttribute('aria-hidden', 'true');
  b.innerHTML = Array.from({length: 8}, (_, k) => `<i style="--a:${k * 45}deg"></i>`).join('');
  btn.append(b); setTimeout(() => b.remove(), 800);
}

/* ---------- compteurs du suivi : seul le nombre défile, les unités restent ---------- */
function tick(el) {
  if (el.dataset.mv) return; el.dataset.mv = 1;
  const n = el.firstChild; if (!n || n.nodeType !== 3) return;
  const m = n.textContent.match(/^(\s*)(\d+)(.*)$/s); if (!m || +m[2] === 0 || reduce()) return;
  const to = +m[2], t0 = performance.now(), d = Math.min(1200, 500 + to * 25);
  const step = t => { const k = Math.min(1, (t - t0) / d), e = 1 - Math.pow(1 - k, 3);
    n.textContent = m[1] + Math.round(to * e) + m[3]; if (k < 1) requestAnimationFrame(step); };
  n.textContent = m[1] + '0' + m[3]; requestAnimationFrame(step);
}

/* ---------- cartes qui se révèlent au défilement ---------- */
const REVEAL = '.view .panel.stat, .view .cm-card, .view .coll-cards a, .view .grid2 > .panel';
let io = null;
function reveal(el) {
  if (el.dataset.rv || reduce() || !('IntersectionObserver' in window)) return;
  el.dataset.rv = 1;
  const r = el.getBoundingClientRect();
  if (r.top < innerHeight && r.bottom > 0) return;          // déjà visible : pas de saut
  io ||= new IntersectionObserver(es => es.forEach(x => { if (x.isIntersecting) { x.target.classList.add('rv-in'); io.unobserve(x.target); } }), {rootMargin: '0px 0px -8% 0px'});
  el.classList.add('rv'); io.observe(el);
}

/* ---------- première réussite d'un exercice ---------- */
function success(el) {
  const id = (location.hash.match(/^#ex-(.+)$/) || [])[1]; if (!id) return;
  const seen = store.get('cele', []); if (seen.includes(id)) return;
  store.set('cele', [...seen, id].slice(-500));
  buzz([10, 40, 18]);
  if (!reduce()) celebrate(el, 'Exercice réussi : tes pairs t’ont donné au moins 12/20.');
}

/* ---------- l'observateur ---------- */
function scan(root) {
  if (root.nodeType !== 1) return;
  const all = sel => [...(root.matches?.(sel) ? [root] : []), ...root.querySelectorAll(sel)];
  all('#items').forEach(stagger);
  if (root.parentElement?.id === 'items') stagger(root.parentElement);
  all('.stat .big, .stat .v').forEach(tick);
  all(REVEAL).forEach(reveal);
  all('#copy .status.ok').forEach(success);
}

export function initMouvement() {
  document.documentElement.classList.add('mv');
  new MutationObserver(ms => {
    for (const m of ms) {
      if (m.target.id === 'items') { stagger(m.target); continue; }
      m.addedNodes.forEach(scan);
    }
  }).observe(document.body, {childList: true, subtree: true});
  scan(document.body);
  addEventListener('pointerdown', ripple, {passive: true});
  addEventListener('click', e => { const f = e.target.closest('#bFav'); if (f) setTimeout(() => heart(f), 0); });
  // les changements d'onglet : l'icône du nouvel onglet sautille
  addEventListener('hashchange', () => setTimeout(() => document.querySelectorAll('.bottombar a[aria-current=page] svg, nav.tabs a[aria-current=page] svg').forEach(s => {
    s.classList.remove('hop'); void s.getBoundingClientRect(); s.classList.add('hop'); }), 0));
}
