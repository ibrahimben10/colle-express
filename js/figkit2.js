// Outils complémentaires : composants de circuits, angles, flèches légendées.
import { L, A, T, C, R, P } from './figkit.js';

// Résistor centré en (x, y), horizontal ou vertical.
export const res = (x, y, h = true, l = 36) => h ? R(x - l / 2, y - 7, l, 14, 'fillW') : R(x - 7, y - l / 2, 14, l, 'fillW');
// Condensateur : deux armatures perpendiculaires au fil.
export const cap = (x, y, h = true) => h
  ? `<rect x="${x - 5}" y="${y - 14}" width="10" height="28" class="fillW" style="stroke:none"/>` + L(x - 5, y - 13, x - 5, y + 13, 'thick') + L(x + 5, y - 13, x + 5, y + 13, 'thick')
  : `<rect x="${x - 14}" y="${y - 5}" width="28" height="10" class="fillW" style="stroke:none"/>` + L(x - 13, y - 5, x + 13, y - 5, 'thick') + L(x - 13, y + 5, x + 13, y + 5, 'thick');
// Bobine : boucles le long du fil.
export function coil(x, y, h = true, n = 4, w = 40) {
  const s = w / n, x0 = h ? x - w / 2 : x, y0 = h ? y : y - w / 2;
  let d = `M${x0},${y0}`;
  for (let i = 0; i < n; i++) d += h ? ` a${s / 2},${s / 2} 0 0 1 ${s},0` : ` a${s / 2},${s / 2} 0 0 1 0,${s}`;
  return (h ? `<rect x="${x0}" y="${y - 2}" width="${w}" height="4" class="fillW" style="stroke:none"/>` : `<rect x="${x - 2}" y="${y0}" width="4" height="${w}" class="fillW" style="stroke:none"/>`) + P(d, 'thick');
}
// Générateur de tension idéal (cercle traversé par le fil).
export const gen = (x, y, h = false) => C(x, y, 14, 'fillW') + (h ? L(x - 14, y, x + 14, y) : L(x, y - 14, x, y + 14));
// Interrupteur ouvert entre (x1, y) et (x2, y) (horizontal) ou vertical.
export const sw = (x1, y1, x2, y2) => {
  const h = y1 === y2;
  return `<circle cx="${x1}" cy="${y1}" r="2.6" class="pt"/><circle cx="${x2}" cy="${y2}" r="2.6" class="pt"/>` +
    (h ? L(x1, y1, x2 - 3, y1 - 13, 'thick') : L(x1, y1, x1 - 13, y2 - 3, 'thick'));
};
// Arc d'angle de centre (cx, cy), rayon r, de a1 à a2 (degrés, sens trigo, y vers le haut).
export function arc(cx, cy, r, a1, a2, c = '') {
  const p = a => [cx + r * Math.cos(a * Math.PI / 180), cy - r * Math.sin(a * Math.PI / 180)];
  const [x1, y1] = p(a1), [x2, y2] = p(a2), big = Math.abs(a2 - a1) > 180 ? 1 : 0, sweep = a2 > a1 ? 0 : 1;
  return `<path d="M${x1.toFixed(1)},${y1.toFixed(1)} A${r},${r} 0 ${big} ${sweep} ${x2.toFixed(1)},${y2.toFixed(1)}" class="s ${c}"/>`;
}
// Arc fléché (rotation).
export function rot(cx, cy, r, a1, a2, c = '') {
  const p = a => [cx + r * Math.cos(a * Math.PI / 180), cy - r * Math.sin(a * Math.PI / 180)];
  const [x1, y1] = p(a1), [x2, y2] = p(a2), big = Math.abs(a2 - a1) > 180 ? 1 : 0, sweep = a2 > a1 ? 0 : 1;
  const m = c.includes('r') ? 'ahr' : c.includes('b') ? 'ahb' : 'ah';
  return `<path d="M${x1.toFixed(1)},${y1.toFixed(1)} A${r},${r} 0 ${big} ${sweep} ${x2.toFixed(1)},${y2.toFixed(1)}" class="s ${c}" marker-end="url(#${m})"/>`;
}
// Ellipse.
export const E = (cx, cy, rx, ry, c = '') => `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" class="s ${c}"/>`;
// Point (x, y) à la distance r dans la direction a (degrés, y vers le haut).
export const pol = (x, y, r, a) => [x + r * Math.cos(a * Math.PI / 180), y - r * Math.sin(a * Math.PI / 180)];
// Courbe à partir d'une fonction : x de x0 à x1 (coordonnées écran).
export function curve(f, x0, x1, c = 'thick r', n = 80) {
  let d = '';
  for (let i = 0; i <= n; i++) { const x = x0 + (x1 - x0) * i / n, y = f(x); d += (i ? ' L' : 'M') + x.toFixed(1) + ',' + y.toFixed(1); }
  return P(d, c);
}
// Flèches de flux ondulées (pertes vers l'extérieur).
export const wav = (x, y, dx, dy, c = 'r') => {
  const l = Math.hypot(dx, dy), ux = dx / l, uy = dy / l, px = -uy * 3, py = ux * 3;
  const m = c.includes('r') ? 'ahr' : c.includes('b') ? 'ahb' : 'ah';
  return `<path d="M${x},${y} q${ux * l / 4 + px},${uy * l / 4 + py} ${ux * l / 2},${uy * l / 2} t${ux * l / 2},${uy * l / 2}" class="s ${c}" marker-end="url(#${m})"/>`;
};
export const lab = (x, y, t, c = '', a = 'middle') => T(x, y, t, c, a);
export { L, A };
// Repère de tracé : (x, y) coin haut-gauche, w × h en pixels, xr / yr intervalles de données.
export function plot(x, y, w, h, xr, yr) {
  const X = v => x + (v - xr[0]) / (xr[1] - xr[0]) * w, Y = v => y + h - (v - yr[0]) / (yr[1] - yr[0]) * h;
  const f = (fn, a, b, c = 'thick r', n = 160) => {
    let d = '', pen = false;
    for (let i = 0; i <= n; i++) { const t = a + (b - a) * i / n, v = fn(t); if (!isFinite(v) || v < yr[0] - (yr[1] - yr[0]) * .02 || v > yr[1] + (yr[1] - yr[0]) * .02) { pen = false; continue; } d += (pen ? ' L' : ' M') + X(t).toFixed(1) + ',' + Y(v).toFixed(1); pen = true; }
    return P(d.trim(), c);
  };
  // Axes : abscisse à la hauteur y = y0, ordonnée à x = x0 (en données).
  const axes = (xl, yl, x0 = xr[0], y0 = Math.max(yr[0], Math.min(0, yr[1]))) =>
    A(x - 4, Y(y0), x + w + 10, Y(y0)) + T(x + w + 10, Y(y0) - 8, xl, '', 'end') +
    A(X(x0), y + h + 4, X(x0), y - 10) + T(X(x0) + 6, y - 4, yl, '', 'start');
  const vline = (v, c = 'dash soft') => L(X(v), y, X(v), y + h, c), hline = (v, c = 'dash soft') => L(x, Y(v), x + w, Y(v), c);
  return {X, Y, f, axes, vline, hline};
}
