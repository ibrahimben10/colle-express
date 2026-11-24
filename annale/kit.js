// Charte « annale » : outils de dessin SVG sobres, monochromes (couleur du texte courant).
// Toutes les valeurs de la charte sont ici, et seulement ici.

export const CH = {
  font: "'Latin Modern Roman','LM Roman 10','CMU Serif','STIX Two Text','Times New Roman',serif",
  fs: 15,          // texte et notations
  fsSub: 10.5,     // indices et exposants
  fsTick: 12.5,    // graduations
  wObj: 1.3,       // objets, fils, solides, courbes
  wVec: 1.3,       // vecteurs (forces, champs, vitesses)
  wAxe: 0.9,       // axes et repères
  wFin: 0.7,       // constructions, cotes, normales, lignes de rappel
  wHatch: 0.55,    // hachures
  dash: '4 3',     // pointillés (construction, normales, positions antérieures)
  mixte: '9 2.5 2 2.5', // trait mixte (axe de symétrie, axe de rotation)
};

const n = v => (Math.round(v * 10) / 10).toString();
const stroke = (w, extra = '') => `fill="none" stroke="currentColor" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"${extra}`;

// ---------- racine ----------
export function svg(w, h, body, title) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" width="${w}" height="${h}" role="img" aria-label="${title}" font-family="${CH.font}" font-size="${CH.fs}" fill="currentColor">
<title>${title}</title>
<defs>
<marker id="an-v" viewBox="0 0 10 7" refX="9.2" refY="3.5" markerWidth="8.5" markerHeight="6" markerUnits="userSpaceOnUse" orient="auto-start-reverse"><path d="M0,0 L10,3.5 L0,7 L2.2,3.5 Z" fill="currentColor"/></marker>
<marker id="an-c" viewBox="0 0 10 7" refX="9.6" refY="3.5" markerWidth="6.5" markerHeight="4.5" markerUnits="userSpaceOnUse" orient="auto-start-reverse"><path d="M0,0 L10,3.5 L0,7 Z" fill="currentColor"/></marker>
<pattern id="an-h" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" stroke="currentColor" stroke-width="${CH.wHatch}"/></pattern>
<pattern id="an-h2" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><line x1="0" y1="0" x2="0" y2="9" stroke="currentColor" stroke-width="0.45"/></pattern>
</defs>
${body}
</svg>`;
}

// ---------- traits ----------
export const L = (x1, y1, x2, y2, k = 'obj') => `<line x1="${n(x1)}" y1="${n(y1)}" x2="${n(x2)}" y2="${n(y2)}" ${style(k)}/>`;
export const P = (d, k = 'obj', extra = '') => `<path d="${d}" ${style(k)}${extra}/>`;
export const poly = (pts, k = 'obj', close = false) => P('M' + pts.map(p => n(p[0]) + ',' + n(p[1])).join(' L') + (close ? ' Z' : ''), k);
export const C = (x, y, r, k = 'obj') => `<circle cx="${n(x)}" cy="${n(y)}" r="${n(r)}" ${style(k)}/>`;
export const Ell = (x, y, rx, ry, k = 'obj') => `<ellipse cx="${n(x)}" cy="${n(y)}" rx="${n(rx)}" ry="${n(ry)}" ${style(k)}/>`;
export const Rect = (x, y, w, h, k = 'obj') => `<rect x="${n(x)}" y="${n(y)}" width="${n(w)}" height="${n(h)}" ${style(k)}/>`;
function style(k) {
  return ({
    obj: stroke(CH.wObj), epais: stroke(1.7), fin: stroke(CH.wFin), axe: stroke(CH.wAxe),
    pt: stroke(CH.wFin, ` stroke-dasharray="${CH.dash}"`), ptobj: stroke(CH.wObj, ` stroke-dasharray="${CH.dash}"`),
    mixte: stroke(CH.wFin, ` stroke-dasharray="${CH.mixte}"`),
  })[k] || stroke(CH.wObj);
}
// Zone hachurée (paroi, sol, bâti, conducteur massif) : contour facultatif.
export const hatch = (d, contour = false) => `<path d="${d}" fill="url(#an-h)" stroke="none"/>` + (contour ? P(d, 'obj') : '');
export const hatchRect = (x, y, w, h) => hatch(`M${n(x)},${n(y)} h${n(w)} v${n(h)} h${n(-w)} Z`);
// Aire (travail d'un cycle…) : hachure lâche.
export const aire = d => `<path d="${d}" fill="url(#an-h2)" stroke="none"/>`;
// Paroi : trait épais + hachures du côté « matière » (dx, dy = direction de la matière).
export function paroi(x1, y1, x2, y2, side = 1, e = 8) {
  const dx = x2 - x1, dy = y2 - y1, l = Math.hypot(dx, dy), nx = -dy / l * e * side, ny = dx / l * e * side;
  return hatch(`M${n(x1)},${n(y1)} L${n(x2)},${n(y2)} L${n(x2 + nx)},${n(y2 + ny)} L${n(x1 + nx)},${n(y1 + ny)} Z`) + L(x1, y1, x2, y2, 'epais');
}

// ---------- flèches ----------
export const vec = (x1, y1, x2, y2) => `<line x1="${n(x1)}" y1="${n(y1)}" x2="${n(x2)}" y2="${n(y2)}" ${stroke(CH.wVec)} marker-end="url(#an-v)"/>`;
export const axe = (x1, y1, x2, y2) => `<line x1="${n(x1)}" y1="${n(y1)}" x2="${n(x2)}" y2="${n(y2)}" ${stroke(CH.wAxe)} marker-end="url(#an-c)"/>`;
// Flèche fine (tension, flux, rayon lumineux orienté, sens de parcours) : tête au point d'arrivée.
export const fl = (x1, y1, x2, y2, k = 'fin') => `<line x1="${n(x1)}" y1="${n(y1)}" x2="${n(x2)}" y2="${n(y2)}" ${style(k)} marker-end="url(#an-c)"/>`;
// Tête de flèche seule au milieu d'un segment (sens de parcours sur un fil, un rayon, une branche de cycle).
export function mid(x1, y1, x2, y2, t = .55) {
  const a = Math.atan2(y2 - y1, x2 - x1), x = x1 + (x2 - x1) * t, y = y1 + (y2 - y1) * t, c = Math.cos(a), s = Math.sin(a);
  const p = (u, v) => n(x + u * c - v * s) + ',' + n(y + u * s + v * c);
  return `<path d="M${p(4.5, 0)} L${p(-4, 3.2)} L${p(-4, -3.2)} Z" fill="currentColor"/>`;
}
// Cote : trait fin, flèches aux deux bouts, lignes de rappel facultatives.
export const cote = (x1, y1, x2, y2) => `<line x1="${n(x1)}" y1="${n(y1)}" x2="${n(x2)}" y2="${n(y2)}" ${stroke(CH.wFin)} marker-start="url(#an-c)" marker-end="url(#an-c)"/>`;

// ---------- texte ----------
export const it = s => `<tspan font-style="italic">${s}</tspan>`;
export const rm = s => `<tspan font-style="normal">${s}</tspan>`;
// indice : romain par défaut (étiquette), italique si c'est une variable
// (décalage par dy puis retour à la ligne de base : rendu identique dans tous les navigateurs)
export const sub = (s, ital = false) => `<tspan dy="3.6" font-size="${CH.fsSub}"${ital ? ' font-style="italic"' : ''}>${s}</tspan><tspan dy="-3.6">\u200b</tspan>`;
export const sup = s => `<tspan dy="-6" font-size="${CH.fsSub}">${s}</tspan><tspan dy="6">\u200b</tspan>`;
// grandeur : lettre italique + indice éventuel
export const q = (s, i = '', ital = false) => it(s) + (i ? sub(i, ital) : '');
export const T = (x, y, content, anchor = 'middle', size = 0) => `<text x="${n(x)}" y="${n(y)}" text-anchor="${anchor}"${size ? ` font-size="${size}"` : ''}>${content}</text>`;
export const tick = (x, y, s, anchor = 'middle') => T(x, y, s, anchor, CH.fsTick);
// Vecteur : lettre italique surmontée d'une flèche (largeur estimée).
export function V(x, y, s, i = '', anchor = 'middle') {
  const w = s.length * CH.fs * .52, x0 = anchor === 'middle' ? x - w / 2 : anchor === 'end' ? x - w - (i ? 7 : 0) : x;
  return T(x, y, q(s, i), anchor) + `<line x1="${n(x0 + 1)}" y1="${n(y - 13.5)}" x2="${n(x0 + w + 2)}" y2="${n(y - 13.5)}" ${stroke(.75)} marker-end="url(#an-c)"/>`;
}
// Repère local (u_x, u_y…) ou nom de point.
export const pt = (x, y, r = 2.2) => `<circle cx="${n(x)}" cy="${n(y)}" r="${r}" fill="currentColor"/>`;
export const ptO = (x, y, r = 2.6) => `<circle cx="${n(x)}" cy="${n(y)}" r="${r}" ${stroke(CH.wObj)}/>`;
export const sortant = (x, y, r = 6) => C(x, y, r, 'obj') + pt(x, y, 1.6);                // ⊙
export const entrant = (x, y, r = 6) => C(x, y, r, 'obj') + L(x - r * .7, y - r * .7, x + r * .7, y + r * .7) + L(x - r * .7, y + r * .7, x + r * .7, y - r * .7); // ⊗

// ---------- angles (degrés, sens trigonométrique, y vers le haut) ----------
export const pol = (x, y, r, a) => [x + r * Math.cos(a * Math.PI / 180), y - r * Math.sin(a * Math.PI / 180)];
export function arc(x, y, r, a1, a2, k = 'fin', head = false) {
  const [x1, y1] = pol(x, y, r, a1), [x2, y2] = pol(x, y, r, a2);
  return `<path d="M${n(x1)},${n(y1)} A${r},${r} 0 ${Math.abs(a2 - a1) > 180 ? 1 : 0} ${a2 > a1 ? 0 : 1} ${n(x2)},${n(y2)}" ${style(k)}${head ? ' marker-end="url(#an-c)"' : ''}/>`;
}
export const Ta = (x, y, r, a, s) => { const [u, v] = pol(x, y, r, a); return T(u, v + 5, s); };

// ---------- composants de circuit (norme française) ----------
// Chaque composant occupe [a, b] sur un fil horizontal (h) ou vertical ; le fil s'arrête aux bornes.
export function resistor(x, y, h = true, l = 34, e = 12) {
  return h ? Rect(x - l / 2, y - e / 2, l, e) : Rect(x - e / 2, y - l / 2, e, l);
}
export function condo(x, y, h = true, g = 7, p = 22) {
  return h ? L(x - g / 2, y - p / 2, x - g / 2, y + p / 2, 'epais') + L(x + g / 2, y - p / 2, x + g / 2, y + p / 2, 'epais')
    : L(x - p / 2, y - g / 2, x + p / 2, y - g / 2, 'epais') + L(x - p / 2, y + g / 2, x + p / 2, y + g / 2, 'epais');
}
export function bobine(x, y, h = true, nb = 4, l = 40) {
  const s = l / nb; let d = h ? `M${n(x - l / 2)},${n(y)}` : `M${n(x)},${n(y - l / 2)}`;
  for (let k = 0; k < nb; k++) d += h ? ` a${n(s / 2)},${n(s / 2)} 0 0 1 ${n(s)},0` : ` a${n(s / 2)},${n(s / 2)} 0 0 1 0,${n(s)}`;
  return P(d);
}
export const generateur = (x, y, h = false, r = 12) => C(x, y, r) + (h ? L(x - r, y, x + r, y) : L(x, y - r, x, y + r));
export function interrupteur(x1, y1, x2, y2) {          // ouvert
  const h = y1 === y2;
  return ptO(x1, y1, 2.2) + ptO(x2, y2, 2.2) + (h ? L(x1 + 2, y1 - 1, x2 - 2, y1 - 12) : L(x1 - 1, y1 + 2, x1 - 12, y2 - 2));
}
export const borne = (x, y) => ptO(x, y, 2.6);
// Courant : petite flèche pleine sur le fil + nom.
export const courant = (x, y, dir, s = it('i'), dx = 0, dy = -9) => {
  const d = {r: [1, 0], l: [-1, 0], u: [0, -1], d: [0, 1]}[dir];
  return mid(x - d[0] * 6, y - d[1] * 6, x + d[0] * 6, y + d[1] * 6, .6) + T(x + dx, y + dy, s);
};

// ---------- graphes ----------
export function graphe(x, y, w, h, xr, yr) {
  const X = v => x + (v - xr[0]) / (xr[1] - xr[0]) * w, Y = v => y + h - (v - yr[0]) / (yr[1] - yr[0]) * h;
  const courbe = (f, a, b, k = 'obj', N = 200) => {
    let d = '', on = false;
    for (let i = 0; i <= N; i++) {
      const t = a + (b - a) * i / N, v = f(t);
      if (!isFinite(v) || v < yr[0] || v > yr[1]) { on = false; continue; }
      d += (on ? ' L' : ' M') + n(X(t)) + ',' + n(Y(v)); on = true;
    }
    return P(d.trim(), k);
  };
  const axes = (xl, yl, x0 = xr[0], y0 = 0) => axe(x - 6, Y(y0), x + w + 12, Y(y0)) + T(x + w + 12, Y(y0) + 17, xl, 'end') +
    axe(X(x0), y + h + 6, X(x0), y - 12) + T(X(x0) - 6, y - 4, yl, 'end');
  const vl = (v, k = 'pt', y0 = 0, y1 = null) => L(X(v), Y(y0), X(v), y1 === null ? y : Y(y1), k);
  const hl = (v, k = 'pt', x0 = null, x1 = null) => L(x0 === null ? x : X(x0), Y(v), x1 === null ? x + w : X(x1), Y(v), k);
  return {X, Y, courbe, axes, vl, hl};
}
