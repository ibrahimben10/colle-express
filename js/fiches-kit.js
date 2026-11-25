// Briques de dessin des fiches de cours (au-dessus de figkit) : axes, courbes, dipôles électriques.
import { L, A, T, C, R, P, dot, sb, I } from './figkit.js';

const r2 = n => Math.round(n * 100) / 100;

// Axes d'origine (ox, oy) : longueur vers la droite w, vers la gauche wl, vers le haut h, vers le bas hb.
export function axes(ox, oy, w, wl, h, hb, lx = '', ly = '') {
  let s = A(ox - wl, oy, ox + w, oy, 'soft');
  if (lx) s += T(ox + w + 2, oy + 18, lx, '', 'end');
  if (h || hb) { s += A(ox, oy + hb, ox, oy - h, 'soft'); if (ly) s += T(ox + 8, oy - h + 6, ly, '', 'start'); }
  return s;
}
// Courbe y = f(u) pour u ∈ [a, b] ; point écran (ox + sx·u, oy + sy·f(u)) — sy = −1 pour « y vers le haut ».
export function courbe(f, a, b, ox, oy, sx = 1, sy = -1, n = 200, c = '') {
  let d = '';
  for (let k = 0; k <= n; k++) {
    const u = a + (b - a) * k / n, y = f(u);
    if (!Number.isFinite(y)) continue;
    d += (d ? ' L' : 'M') + r2(ox + sx * u) + ',' + r2(oy + sy * y);
  }
  return P(d, c);
}

// ---- électrocinétique (normes françaises) ----
export const fil = (x1, y1, x2, y2) => L(x1, y1, x2, y2);
export const noeud = (x, y) => dot(x, y);
function rep(x1, y1, x2, y2) { const dx = x2 - x1, dy = y2 - y1, l = Math.hypot(dx, dy); return {l, ux: dx / l, uy: dy / l, px: -dy / l, py: dx / l}; }
// Résistance : rectangle entre les deux bornes.
export function res(x1, y1, x2, y2) {
  const {l, ux, uy, px, py} = rep(x1, y1, x2, y2), h = 8, m = Math.min(12, l * .15);
  const a = [x1 + ux * m, y1 + uy * m], b = [x2 - ux * m, y2 - uy * m];
  const pts = [[a[0] + px * h, a[1] + py * h], [b[0] + px * h, b[1] + py * h], [b[0] - px * h, b[1] - py * h], [a[0] - px * h, a[1] - py * h]];
  return L(x1, y1, a[0], a[1]) + L(b[0], b[1], x2, y2) + P('M' + pts.map(p => p.map(r2).join(',')).join(' L') + ' Z', 'fillW');
}
// Condensateur : deux armatures perpendiculaires au fil, entre les bornes (écart = longueur du segment).
export function cond(x1, y1, x2, y2) {
  const {px, py} = rep(x1, y1, x2, y2), h = 14;
  return L(x1 + px * h, y1 + py * h, x1 - px * h, y1 - py * h, 'thick') + L(x2 + px * h, y2 + py * h, x2 - px * h, y2 - py * h, 'thick');
}
// Bobine : suite de demi-boucles.
export function bobine(x1, y1, x2, y2, n = 4) {
  const {l, ux, uy, px, py} = rep(x1, y1, x2, y2), m = Math.min(10, l * .12), s = (l - 2 * m) / n, rr = s / 2;
  let d = `M${r2(x1)},${r2(y1)} L${r2(x1 + ux * m)},${r2(y1 + uy * m)}`;
  for (let k = 0; k < n; k++) { const ex = x1 + ux * (m + s * (k + 1)), ey = y1 + uy * (m + s * (k + 1)); d += ` A${r2(rr)},${r2(rr)} 0 0 ${px * 0 + 1} ${r2(ex)},${r2(ey)}`; }
  d += ` L${r2(x2)},${r2(y2)}`;
  return P(d);
}
// Source idéale de tension : cercle traversé par le fil.
export function gene(x1, y1, x2, y2) {
  const cx = (x1 + x2) / 2, cy = (y1 + y2) / 2, rr = 16;
  const {ux, uy} = rep(x1, y1, x2, y2);
  return L(x1, y1, cx - ux * rr, cy - uy * rr) + L(cx + ux * rr, cy + uy * rr, x2, y2) + C(cx, cy, rr, 'fillW') + L(cx - ux * rr, cy - uy * rr, cx + ux * rr, cy + uy * rr);
}
// Interrupteur ouvert.
export function inter(x1, y1, x2, y2) {
  const {l, ux, uy, px, py} = rep(x1, y1, x2, y2);
  return dot(x1, y1) + dot(x2, y2) + L(x1, y1, x2 - ux * 4 + px * l * .45, y2 - uy * 4 + py * l * .45);
}
// Flèche de tension (à côté du dipôle) et de courant (sur le fil), avec étiquette.
export function ten(x1, y1, x2, y2, t, sd = 1) {
  let {px, py} = rep(x1, y1, x2, y2); px *= sd; py *= sd;
  const mx = (x1 + x2) / 2, my = (y1 + y2) / 2, tx = mx + px * 14, ty = my + py * 14 + 5;
  return A(x1, y1, x2, y2, 'b') + T(r2(tx), r2(ty), t, 'b', Math.abs(px) > .5 ? (px > 0 ? 'start' : 'end') : 'middle');
}
export function cour(x1, y1, x2, y2, t) {
  const {px, py} = rep(x1, y1, x2, y2);
  return A(x1, y1, x2, y2, 'r') + T(r2((x1 + x2) / 2 - px * 12), r2((y1 + y2) / 2 - py * 12 + 4), t, 'r');
}
export const tir = (x, y, w) => L(x, y, x + w, y, 'dash soft');

// Petit diagramme de Bode asymptotique + réel (gain en dB) d'un filtre du 1er ordre ou d'un passe-bande.
export function flt(ox, oy, type) {
  const w = 200, X0 = ox, Y0 = oy + 50, sx = 50;     // log10(ω/ωc) ∈ [−2, 2] → 200 px
  const G = {bas: x => -10 * Math.log10(1 + x * x), haut: x => -10 * Math.log10(1 + 1 / (x * x)), bande: x => -10 * Math.log10(1 + 9 * (x - 1 / x) ** 2)}[type];
  const k = 1.6;
  const asym = {bas: `${L(X0, Y0, X0 + 100, Y0, 'r dash')}${L(X0 + 100, Y0, X0 + 200, Y0 + 40 * k, 'r dash')}`,
    haut: `${L(X0, Y0 + 40 * k, X0 + 100, Y0, 'r dash')}${L(X0 + 100, Y0, X0 + 200, Y0, 'r dash')}`,
    bande: `${L(X0 + 0.2 * sx, Y0 + 45.54 * k, X0 + 100, Y0 + 9.54 * k, 'r dash')}${L(X0 + 100, Y0 + 9.54 * k, X0 + 3.8 * sx, Y0 + 45.54 * k, 'r dash')}`}[type];
  return `${A(X0, Y0, X0 + w + 10, Y0, 'soft')}${A(X0, Y0 + 90, X0, oy, 'soft')}${T(X0 + 8, oy + 8, sb(I('G'), 'dB'), '', 'start')}${T(X0 + w + 10, Y0 - 6, 'log ω', '', 'end')}
    ${asym}${pathLog(G, X0, Y0, sx, k)}${L(X0 + 100, Y0 - 4, X0 + 100, Y0 + 4)}${T(X0 + 100, Y0 - 8, type === 'bande' ? sb('ω', '0') : sb('ω', 'c'))}
`;
}
function pathLog(G, X0, Y0, sx, k) {
  let d = '';
  for (let i = 0; i <= 200; i++) { const u = -2 + 4 * i / 200, y = Math.max(-56, G(10 ** u)); d += (d ? ' L' : 'M') + r2(X0 + (u + 2) * sx) + ',' + r2(Y0 - y * k); }
  return P(d, 'b');
}
