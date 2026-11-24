// Outils de dessin des schémas SVG (thème clair/sombre via CSS).

export const DEFS = `<defs>
<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1L10,5L0,9z" class="fh"/></marker>
<marker id="ahr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1L10,5L0,9z" class="fh r"/></marker>
<marker id="ahb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1L10,5L0,9z" class="fh b"/></marker>
<pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="7" class="ht"/></pattern>
</defs>`;
export const svg = (w, h, body, t) => `<svg viewBox="0 0 ${w} ${h}" role="img" aria-label="${t}" class="fig-svg">${DEFS}${body}</svg>`;
export const L = (x1, y1, x2, y2, c = '') => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" class="s ${c}"/>`;
export const A = (x1, y1, x2, y2, c = '') => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" class="s ${c}" marker-end="url(#${c.includes('r') && !c.includes('ro') ? 'ahr' : c.includes('b') ? 'ahb' : 'ah'})"/>`;
export const D = (x1, y1, x2, y2, t, tx, ty) => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" class="s dim" marker-start="url(#ah)" marker-end="url(#ah)"/>${T(tx ?? (x1 + x2) / 2, ty ?? (y1 + y2) / 2 - 6, t)}`;
export const T = (x, y, t, c = '', a = 'middle') => `<text x="${x}" y="${y}" class="lb ${c}" text-anchor="${a}">${t}</text>`;
export const I = s => `<tspan class="it">${s}</tspan>`;           // variable en italique
export const V = s => `<tspan class="it">${s}</tspan><tspan class="vec" dx="-${s.length * 6.5}" dy="-9">→</tspan><tspan dy="9"> </tspan>`;
export const C = (x, y, r, c = '') => `<circle cx="${x}" cy="${y}" r="${r}" class="s ${c}"/>`;
export const R = (x, y, w, h, c = '', rx = 0) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx}" class="s ${c}"/>`;
export const P = (d, c = '') => `<path d="${d}" class="s ${c}"/>`;
export const dot = (x, y, c = '') => `<circle cx="${x}" cy="${y}" r="3.2" class="pt ${c}"/>`;
export function spring(x1, y1, x2, y2, n = 9, a = 7) {
  const dx = x2 - x1, dy = y2 - y1, l = Math.hypot(dx, dy), ux = dx / l, uy = dy / l, px = -uy, py = ux;
  const e = Math.min(10, l * .12); let d = `M${x1},${y1} L${x1 + ux * e},${y1 + uy * e}`;
  for (let i = 0; i < n; i++) { const t = e + (l - 2 * e) * (i + .5) / n, s = i % 2 ? -a : a; d += ` L${x1 + ux * t + px * s},${y1 + uy * t + py * s}`; }
  d += ` L${x2 - ux * e},${y2 - uy * e} L${x2},${y2}`;
  return `<path d="${d}" class="s spring"/>`;
}
export const ground = (x, y, w, up = false) => `<rect x="${x}" y="${up ? y - 9 : y}" width="${w}" height="9" class="hatch"/>${L(x, y, x + w, y)}`;
export const wallV = (x, y, h, left = true) => `<rect x="${left ? x - 9 : x}" y="${y}" width="9" height="${h}" class="hatch"/>${L(x, y, x, y + h)}`;
export const lens = (x, y, h, conv = true) => {
  const k = 7, t = y - h / 2, b = y + h / 2;
  return L(x, t, x, b, 'thick') + (conv
    ? P(`M${x - k},${t + k} L${x},${t} L${x + k},${t + k} M${x - k},${b - k} L${x},${b} L${x + k},${b - k}`, 'thick')
    : P(`M${x - k},${t - k} L${x},${t} L${x + k},${t - k} M${x - k},${b + k} L${x},${b} L${x + k},${b + k}`, 'thick'));
};
export const axe = (x1, x2, y) => L(x1, y, x2, y, 'axis');
export const ox = (x, y) => C(x, y, 6) + C(x, y, 1.6, 'fill');        // vecteur sortant ⊙
export const ot = (x, y) => C(x, y, 6) + L(x - 4, y - 4, x + 4, y + 4) + L(x - 4, y + 4, x + 4, y - 4); // entrant ⊗

export const sb = (b, s) => `${b}<tspan baseline-shift="sub" font-size="10">${s}</tspan>`; // indice
