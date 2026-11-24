// Lot 3 : électrocinétique, électrostatique, équations de Maxwell, induction.
import { CH, svg, L, P, poly, C, Ell, Rect, hatch, hatchRect, aire, paroi, vec, axe, fl, mid, cote, it, sub, sup, q, T, tick, V, pt, ptO,
  sortant, entrant, pol, arc, Ta, resistor, condo, bobine, interrupteur, borne, courant, graphe, sinus } from './kit.js';

const n = v => Math.round(v * 10) / 10;
const small = 13.5, sep = (x, y1, y2) => L(x, y1, x, y2, 'pt');
const disque = (cx, cy, r) => `<circle cx="${cx}" cy="${cy}" r="${r}" fill="url(#an-h)" stroke="none"/>` + C(cx, cy, r);
const anneau = (cx, cy, r1, r2) => `<path d="M${cx - r2},${cy} a${r2},${r2} 0 1 0 ${2 * r2},0 a${r2},${r2} 0 1 0 ${-2 * r2},0 Z M${cx - r1},${cy} a${r1},${r1} 0 1 0 ${2 * r1},0 a${r1},${r1} 0 1 0 ${-2 * r1},0 Z" fill="url(#an-h)" fill-rule="evenodd" stroke="none"/>` + C(cx, cy, r1) + C(cx, cy, r2);
const lg = Math.log10;

// ---------- RLC passe-bande ----------
function rlcBande(o = 0, corr = false) {
  const xl = 50 + o, xr = 260 + o, yt = 50, yb = 170;
  return sinus(xl, 110) + L(xl, yt, xl, 98) + L(xl, 122, xl, yb) + L(xl, yt, 82 + o, yt) + bobine(102 + o, yt) + L(122 + o, yt, 158.5 + o, yt) + condo(162 + o, yt) + L(165.5 + o, yt, xr, yt)
    + L(xr, yt, xr, 93) + resistor(xr, 110, false) + L(xr, 127, xr, yb) + L(xl, yb, xr, yb)
    + fl(28 + o, 136, 28 + o, 84) + T(20 + o, 115, it('e'), 'end') + fl(282 + o, 136, 282 + o, 84) + T(290 + o, 115, it('s'), 'start')
    + (corr ? T(102 + o, 32, 'j' + it('L') + 'ω', 'middle', small) + T(162 + o, 30, '1/(j' + it('C') + 'ω)', 'middle', small) + T(244 + o, 115, it('R'), 'end') + courant(212 + o, yt, 'r')
      : T(102 + o, 32, it('L')) + T(162 + o, 32, it('C')) + T(244 + o, 115, it('R'), 'end'));
}
const bandeE = svg(320, 196, rlcBande(), 'Circuit RLC série, sortie aux bornes de R');
const bandeC = (() => {
  const Q = 10, H = x => 1 / Math.sqrt(1 + Q * Q * (x - 1 / x) ** 2), g = graphe(352, 30, 170, 150, [lg(.5), lg(2)], [0, 1.15]);
  const xm = (Math.sqrt(1 + 4 * Q * Q) - 1) / (2 * Q), xp = (Math.sqrt(1 + 4 * Q * Q) + 1) / (2 * Q), s2 = 1 / Math.SQRT2;
  return svg(550, 222, rlcBande(0, true) + sep(326, 14, 200)
    + g.axes('log ω', '|' + it('H') + '|', lg(.5)) + g.courbe(t => H(10 ** t), lg(.5), lg(2), 'obj', 400)
    + g.hl(1, 'fin', lg(.5), lg(.53)) + tick(g.X(lg(.5)) - 5, g.Y(1) + 4, '1', 'end') + g.hl(s2, 'pt', lg(.5), lg(xp)) + tick(g.X(lg(.5)) - 5, g.Y(s2) + 4, '1/√2', 'end')
    + g.vl(lg(xm), 'pt', 0, s2) + g.vl(lg(xp), 'pt', 0, s2) + g.vl(0, 'pt', 0, 1) + tick(g.X(0), g.Y(0) + 17, q('ω', '0'))
    + cote(g.X(lg(xm)), g.Y(.32), g.X(lg(xp)), g.Y(.32)) + T(g.X(lg(xp)) + 6, g.Y(.32) + 5, 'Δω = ' + q('ω', '0') + '/' + it('Q'), 'start', 12.5),
    'Passe-bande : impédances et réponse en fréquence');
})();

// ---------- RC passe-bas ----------
function rcBas(corr = false) {
  return borne(40, 50) + borne(40, 160) + L(42.6, 50, 98, 50) + resistor(115, 50) + L(132, 50, 268, 50) + L(190, 50, 190, 101.5) + condo(190, 105, false) + L(190, 108.5, 190, 160)
    + L(42.6, 160, 268, 160) + borne(270, 50) + borne(270, 160) + pt(190, 50) + pt(190, 160)
    + fl(28, 146, 28, 64) + T(20, 110, it('e'), 'end') + fl(286, 146, 286, 64) + T(294, 110, it('s'), 'start')
    + (corr ? T(115, 32, it('R'), 'middle') + T(208, 110, '1/(j' + it('C') + 'ω)', 'start', small) + courant(80, 50, 'r') + T(155, 186, it('i') + ' = 0 en sortie ouverte', 'middle', 12.5)
      : T(115, 32, it('R')) + T(210, 110, it('C'), 'start'));
}
const basE = svg(320, 196, rcBas(), 'Filtre RC, sortie aux bornes du condensateur');
const basC = (() => {
  const fc = 1592, G = f => -10 * lg(1 + (f / fc) ** 2), g = graphe(352, 26, 176, 160, [1, 5], [-40, 6]);
  return svg(556, 222, rcBas(true) + sep(326, 14, 206) + g.axes('log ' + it('f'), q('G', 'dB'), 1, 0)
    + L(g.X(1), g.Y(0), g.X(lg(fc)), g.Y(0), 'pt') + L(g.X(lg(fc)), g.Y(0), g.X(5), g.Y(-20 * (5 - lg(fc))), 'pt') + g.courbe(t => G(10 ** t), 1, 5)
    + g.vl(lg(fc), 'pt', -40, 0) + tick(g.X(lg(fc)), g.Y(-40) + 15, q('f', 'c'))
    + pt(g.X(2), g.Y(G(100))) + tick(g.X(2), g.Y(0) - 8, q('f', '1')) + pt(g.X(lg(2e4)), g.Y(G(2e4))) + tick(g.X(lg(2e4)) - 6, g.Y(G(2e4)) + 4, q('f', '2'), 'end')
    + T(g.X(4.15), g.Y(-30), '−20 dB/déc.', 'start', 12) + T(g.X(1.05), g.Y(-16), 'continu, ' + q('f', '1') + ' : transmis', 'start', 11.5) + T(g.X(1.05), g.Y(-24), q('f', '2') + ' : atténuée', 'start', 11.5),
    'Passe-bas : impédances et diagramme de Bode');
})();

// ---------- créneau et triangle ----------
const fourierC = (() => {
  const sq = t => ((t % 1) + 1) % 1 < .5 ? 1 : -1, tri = t => { const u = ((t % 1) + 1) % 1; return u < .5 ? -1 + 4 * u : 3 - 4 * u; };
  const a = graphe(40, 20, 220, 90, [0, 2.15], [-1.3, 1.3]), b = graphe(40, 168, 220, 90, [0, 2.15], [-1.3, 1.3]);
  const c = graphe(330, 20, 190, 90, [0, 8], [0, 1.2]), d = graphe(330, 168, 190, 90, [0, 8], [0, 1.2]);
  const sqd = (g) => { let s = ''; for (let k = 0; k < 4.3; k++) { const x0 = k * .5, x1 = Math.min(2.15, x0 + .5); if (x0 >= 2.15) break; const v = k % 2 ? -1 : 1; s += L(g.X(x0), g.Y(v), g.X(x1), g.Y(v)); if (x1 < 2.15) s += L(g.X(x1), g.Y(v), g.X(x1), g.Y(-v), 'fin'); } return s + L(g.X(0), g.Y(0), g.X(0), g.Y(1), 'fin'); };
  const raies = (g, f) => [1, 3, 5, 7].map(k => L(g.X(k), g.Y(0), g.X(k), g.Y(f(k)), 'epais') + tick(g.X(k), g.Y(0) + 15, String(k))).join('');
  return svg(560, 300, a.axes(it('t'), it('e'), 0, 0) + sqd(a) + tick(a.X(0) - 5, a.Y(1) + 4, it('E'), 'end') + tick(a.X(0) - 5, a.Y(-1) + 4, '−' + it('E'), 'end')
    + cote(a.X(0), a.Y(-1.22), a.X(1), a.Y(-1.22)) + tick(a.X(.5), a.Y(-1.22) + 14, it('T'))
    + b.axes(it('t'), it('s'), 0, 0) + b.courbe(tri, 0, 2.15, 'obj', 430) + tick(b.X(2.15), b.Y(1) - 4, '(échelle dilatée)', 'end')
    + L(b.X(.5), b.Y(1), b.X(.5), b.Y(0), 'pt') + tick(b.X(.5), b.Y(0) + 15, it('T') + '/2')
    + c.axes(it('n'), '|' + q('c', 'n', true) + '|', 0, 0) + raies(c, k => 1 / k) + tick(c.X(5), c.Y(.85), '∝ 1/' + it('n'), 'start')
    + d.axes(it('n'), '|' + q('c', 'n', true) + '|', 0, 0) + raies(d, k => 1 / (k * k)) + tick(d.X(4), d.Y(.85), '∝ 1/' + it('n') + sup('2'), 'start')
    + T(150, 140, '(a) créneau ' + it('e') + '(' + it('t') + ')', 'middle', 12.5) + T(150, 290, '(b) triangle ' + it('s') + '(' + it('t') + ')', 'middle', 12.5)
    + T(425, 140, '(c) spectre de ' + it('e'), 'middle', 12.5) + T(425, 290, '(d) spectre de ' + it('s'), 'middle', 12.5) + sep(296, 10, 292),
    'Créneau et triangle : signaux et spectres');
})();

// ---------- électron : boule chargée ----------
const em2C = (() => {
  const c = [120, 118], R = 80, g = graphe(290, 30, 200, 160, [0, 3], [0, 1.15]);
  return svg(530, 236, C(...c, R) + C(...c, 46, 'pt') + C(...c, 54, 'pt') + pt(...c)
    + L(...c, ...pol(...c, 46, 205), 'fin') + T(...pol(...c, 30, 215), it('r')) + L(...c, ...pol(...c, R, 40), 'fin') + T(...pol(...c, R - 16, 52), it('R'))
    + L(...pol(...c, 50, -40), 216, 206, 'fin') + T(214, 222, 'coquille [' + it('r') + ', ' + it('r') + ' + d' + it('r') + ']', 'end', 12.5)
    + T(c[0], c[1] + 66, 'ρ < 0', 'middle', small) + sep(262, 14, 226)
    + g.axes(it('r'), '‖' + it('E') + '‖') + g.courbe(r => r <= 1 ? r : 1 / (r * r), 0, 3) + g.vl(1, 'pt', 0, 1) + tick(g.X(1), g.Y(0) + 17, it('R'))
    + T(g.X(.45), g.Y(.62), '∝ ' + it('r'), 'end', 12.5) + T(g.X(1.8), g.Y(.48), '∝ 1/' + it('r') + sup('2'), 'start', 12.5),
    'Électron : coquille élémentaire et champ E(r)');
})();

// ---------- ion et dipôle ----------
const dipE = svg(380, 190, C(70, 120, 12) + T(70, 125, '+') + T(70, 158, 'ion Na' + sup('+'), 'middle', small)
  + L(82, 116, 340, 64, 'pt') + pt(250, 86) + T(244, 106, it('M'), 'end') + vec(250, 86, ...pol(250, 86, 60, 62)) + V(...pol(250, 86, 74, 64), 'p')
  + arc(250, 86, 32, 11.5, 62) + Ta(250, 86, 44, 36, 'θ') + T(160, 92, it('r'), 'middle'),
  'Molécule d’eau (dipôle p) à la distance r d’un ion');
const dipC = svg(420, 200, C(60, 120, 12) + T(60, 125, '+') + T(60, 158, 'Na' + sup('+'), 'middle', small)
  + L(72, 120, 390, 120, 'pt') + pt(250, 120) + T(250, 140, it('M'), 'middle')
  + vec(250, 120, ...pol(250, 120, 62, 50)) + V(...pol(250, 120, 76, 54), 'p') + L(250, 120, 312, 120, 'ptobj') + T(320, 112, 'équilibre', 'start', 12.5)
  + vec(330, 160, 392, 160) + V(362, 184, 'E', '', 'middle') + T(398, 164, '(ion)', 'start', 12)
  + arc(250, 120, 42, 46, 8, 'obj', true) + V(...pol(250, 120, 56, 30).map((v, k) => v + (k ? 0 : 8)), 'Γ', '', 'start')
  + vec(226, 88, 170, 88) + V(198, 80, 'F'),
  'Dipôle dans le champ de l’ion : couple de rappel et force');

// ---------- effet de peau ----------
const peauE = svg(380, 206, hatchRect(150, 20, 210, 150) + L(150, 20, 150, 170, 'epais') + T(255, 14, 'cuivre (γ)', 'middle', small) + T(80, 40, 'vide', 'middle', small)
  + vec(136, 128, 136, 62) + T(128, 96, q('E', '0') + ' cos ω' + it('t'), 'end', small)
  + axe(30, 186, 370, 186) + T(370, 202, it('z'), 'end') + L(150, 182, 150, 190, 'fin') + tick(150, 202, '0')
  + axe(40, 150, 40, 110) + T(48, 112, it('x'), 'start') + axe(40, 150, 80, 150) + T(84, 155, it('z'), 'start') + sortant(40, 150, 5) + T(28, 166, it('y'), 'end'),
  'Conducteur occupant le demi-espace z > 0');
const peauC = (() => {
  const g = graphe(290, 30, 210, 160, [0, 5], [-1.1, 1.15]), d = 46;
  let a = L(60, 26, 60, 196, 'epais') + T(150, 20, 'cuivre', 'middle', small);
  for (let k = 0; k < 5; k++) { const l = 76 * Math.exp(-k * 10 / d * 1.1); a += vec(70 + 44 * k, 150, 70 + 44 * k, 150 - l); }
  a += V(84, 70, 'j', '', 'start') + T(100, 70, ' = γ', 'start') + V(126, 70, 'E', '', 'start') + cote(60, 176, 60 + d, 176) + T(60 + d / 2, 194, 'δ')
    + axe(46, 210, 260, 210) + T(260, 226, it('z'), 'end');
  const b = g.axes(it('z'), it('E') + '/' + q('E', '0'), 0, 0) + g.courbe(z => Math.exp(-z), 0, 5, 'pt') + g.courbe(z => -Math.exp(-z), 0, 5, 'pt')
    + g.courbe(z => Math.exp(-z) * Math.cos(z), 0, 5) + g.courbe(z => Math.exp(-z) * Math.sin(z), 0, 5, 'ptobj')
    + g.vl(1, 'pt', 0, Math.exp(-1)) + tick(g.X(1), g.Y(0) + 15, 'δ') + T(g.X(1.6), g.Y(.48), 'e' + sup('−' + it('z') + '/δ'), 'start', 12.5);
  return svg(530, 236, a + sep(270, 14, 226) + b, 'Effet de peau : courants surfaciques et décroissance');
})();

// ---------- bobine plate ----------
const coilDraw = (cx, cy) => Ell(cx, cy, 20, 64) + Ell(cx + 5, cy, 20, 64, 'fin') + Ell(cx + 10, cy, 20, 64, 'fin');
const bobineE = svg(380, 200, coilDraw(170, 100) + L(30, 100, 360, 100, 'mixte')
  + [36, 164].map(y => vec(30, y, 350, y)).join('') + V(330, 28, 'B', '', 'end') + T(350, 28, '(' + it('t') + ')', 'start')
  + vec(185, 100, 250, 100) + V(240, 92, 'n') + T(120, 64, it('N') + ' spires', 'end', small) + T(120, 144, 'surface ' + it('S'), 'end', small),
  'Bobine plate dans un champ uniforme B(t)');
const bobineC = svg(420, 210, coilDraw(170, 105) + L(30, 105, 380, 105, 'mixte')
  + [38, 172].map(y => vec(30, y, 370, y)).join('') + V(340, 30, 'B', '', 'end') + T(360, 30, 'croît', 'start', 12.5)
  + vec(185, 105, 246, 105) + V(236, 97, 'n') + vec(160, 120, 100, 120) + V(118, 142, 'B', 'i', 'middle')
  + entrant(175, 41, 6) + sortant(175, 169, 6) + T(190, 56, it('i') + ' < 0', 'start', small)
  + T(300, 140, 'Φ = ' + it('NSB') + ' croît', 'middle', 12.5) + T(300, 158, it('e') + ' = −dΦ/d' + it('t') + ' < 0', 'middle', 12.5),
  'Bobine plate : sens du courant induit (loi de Lenz)');

// ---------- rails de Laplace ----------
function rails(corr) {
  const xb = 236;
  let s = L(40, 50, 360, 50, 'epais') + L(40, 150, 360, 150, 'epais') + L(40, 50, 40, 83) + resistor(40, 100, false) + L(40, 117, 40, 150) + T(24, 104, it('R'), 'end')
    + Rect(xb - 4, 42, 8, 116) + [[110, 78], [110, 122], [300, 78], [300, 122]].map(([x, y]) => sortant(x, y, 6)).join('') + V(322, 108, 'B', '', 'start')
    + cote(378, 50, 378, 150) + T(386, 104, it('ℓ'), 'start') + axe(250, 184, 290, 184) + V(304, 190, 'u', 'x', 'start') + axe(250, 184, 250, 160) + V(242, 166, 'u', 'y', 'end');
  if (!corr) return s + vec(xb + 6, 100, xb + 56, 100) + V(xb + 32, 92, 'v', '0') + cote(40, 176, xb, 176) + T((40 + xb) / 2, 194, it('x'));
  return aire(`M41,51 H${xb - 4} V149 H41 Z`) + s + vec(xb + 6, 126, xb + 56, 126) + V(xb + 32, 118, 'v')
    + mid(xb, 60, xb, 140) + mid(150, 50, 110, 50) + mid(110, 150, 150, 150) + mid(40, 140, 40, 120) + T(xb + 10, 70, it('i'), 'start')
    + vec(xb - 6, 92, xb - 62, 92) + V(xb - 36, 84, 'F', 'L') + T(140, 102, it('S') + ' = ' + it('ℓx'), 'middle', small);
}
const railsE = svg(400, 200, rails(false), 'Rails de Laplace vus de dessus');
const railsC = svg(400, 200, rails(true), 'Rails de Laplace : courant induit et force de Laplace');

// ---------- transformateur ----------
function transfo(corr) {
  const s = bobine(150, 100, false, 4, 56) + bobine(190, 100, false, 4, 56);
  const flip = s.replace(/<path d="M190/, '<path transform="translate(380,0) scale(-1,1)" d="M190');
  let o = bobine(150, 100, false, 4, 56) + `<g transform="translate(340,0) scale(-1,1)">${bobine(150, 100, false, 4, 56)}</g>`
    + L(166, 64, 166, 136, 'epais') + L(174, 64, 174, 136, 'epais')
    + L(150, 72, 150, 60) + L(150, 60, 60, 60) + L(150, 128, 150, 140) + L(150, 140, 60, 140) + sinus(60, 100) + L(60, 60, 60, 88) + L(60, 112, 60, 140)
    + L(190, 72, 190, 60) + L(190, 60, 280, 60) + L(190, 128, 190, 140) + L(190, 140, 280, 140) + L(280, 60, 280, 83) + resistor(280, 100, false) + L(280, 117, 280, 140)
    + fl(38, 126, 38, 74) + fl(222, 126, 222, 74) + courant(105, 60, 'r', '') + courant(235, 60, 'r', '')
    + T(140, 46, sb2('N', '1'), 'end') + T(200, 46, sb2('N', '2'), 'start') + T(298, 104, it('R'), 'start');
  return o + (corr ? T(30, 104, q('U', '1'), 'end') + T(214, 104, q('U', '2'), 'end') + T(105, 50, q('I', '1')) + T(235, 50, q('I', '2'))
    : T(30, 104, q('u', '1'), 'end') + T(214, 104, q('u', '2'), 'end') + T(105, 50, q('i', '1')) + T(235, 50, q('i', '2')));
}
function sb2(a, b) { return q(a, b); }
const transfoE = svg(330, 170, transfo(false), 'Transformateur alimentant une charge R');
const transfoC = svg(560, 200, transfo(true) + sep(330, 14, 186)
  + sinus(380, 100) + L(380, 60, 380, 88) + L(380, 112, 380, 140) + L(380, 60, 470, 60) + L(470, 60, 470, 83) + resistor(470, 100, false) + L(470, 117, 470, 140) + L(380, 140, 470, 140)
  + T(488, 104, it('R') + '′', 'start') + T(368, 104, q('U', '1'), 'end') + courant(425, 60, 'r', q('I', '1'))
  + T(445, 166, it('R') + '′ = ' + it('R') + '/' + it('m') + sup('2'), 'middle', small)
  + T(170, 172, it('m') + ' = ' + q('N', '2') + '/' + q('N', '1') + ' = ' + q('U', '2') + '/' + q('U', '1') + ' = ' + q('I', '1') + '/' + q('I', '2'), 'middle', small),
  'Transformateur parfait : relations et résistance ramenée au primaire');

// ---------- alternateur (vue de dessus) ----------
function alterTop(cx, cy, th, corr) {
  let s = hatchRect(cx - 150, cy - 70, 34, 140) + Rect(cx - 150, cy - 70, 34, 140) + T(cx - 133, cy + 5, 'N') + hatchRect(cx + 116, cy - 70, 34, 140) + Rect(cx + 116, cy - 70, 34, 140) + T(cx + 133, cy + 5, 'S');
  s = s.replace(/<text[^>]*>N<\/text>/, T(cx - 133, cy - 78, 'N')).replace(/<text[^>]*>S<\/text>/, T(cx + 133, cy - 78, 'S'));
  for (const y of [-50, 50]) s += vec(cx - 110, cy + y, cx + 110, cy + y);
  s += V(cx - 104, cy - 58, 'B', '', 'start') + L(...pol(cx, cy, 70, th + 90), ...pol(cx, cy, 70, th - 90), 'epais')
    + vec(cx, cy, ...pol(cx, cy, 56, th)) + V(...pol(cx, cy, 70, th + 6), 'n') + L(cx, cy, cx + 66, cy, 'pt') + arc(cx, cy, 28, 0, th) + Ta(cx, cy, 40, th / 2, 'θ')
    + sortant(cx, cy, 4) + T(cx - 8, cy + 20, 'Δ', 'end') + arc(cx, cy, 90, 200, 245, 'fin', true) + Ta(cx, cy, 102, 222, 'ω');
  return s + (corr ? T(cx, cy + 96, 'Φ = ' + it('NBS') + ' cos θ, θ = ω' + it('t'), 'middle', small) : T(cx - 70, cy - 30, 'bobine', 'middle', 12));
}
const alterE = svg(330, 210, alterTop(165, 100, 40, false), 'Alternateur : bobine tournant dans un champ uniforme (vue de dessus)');
const alterC = (() => {
  const g = graphe(350, 30, 180, 150, [0, 4 * Math.PI], [-1.2, 1.25]);
  return svg(560, 230, alterTop(165, 100, 40, true) + sep(328, 14, 216) + g.axes('ω' + it('t'), '', 0, 0) + g.courbe(Math.cos, 0, 4 * Math.PI, 'ptobj') + g.courbe(Math.sin, 0, 4 * Math.PI)
    + T(g.X(.1), g.Y(1.08), 'Φ', 'start', small) + T(g.X(Math.PI / 2), g.Y(1.08) - 4, it('e'), 'middle', small) + tick(g.X(2 * Math.PI), g.Y(0) + 15, '2π')
    + T(440, 214, it('e') + ' = −dΦ/d' + it('t') + ' = ' + it('NBS') + 'ω sin ω' + it('t'), 'middle', 12.5),
    'Alternateur : flux et force électromotrice');
})();

// ---------- câble coaxial (énoncé) ----------
const coaxE = svg(320, 250, anneau(150, 122, 86, 92) + disque(150, 122, 24) + pt(150, 122)
  + L(150, 122, ...pol(150, 122, 24, 210), 'fin') + L(...pol(150, 122, 24, 210), 40, 196, 'fin') + T(36, 210, q('R', '1'), 'start')
  + L(150, 122, ...pol(150, 122, 86, 35), 'fin') + T(...pol(150, 122, 64, 48), q('R', '2'))
  + T(150, 72, 'isolant (' + q('ε', 'r') + ')', 'middle', small) + L(...pol(150, 122, 92, 125), 60, 20, 'fin') + T(58, 18, 'gaine', 'end', small) + T(150, 164, 'âme', 'middle', small),
  'Coupe du câble coaxial');

export const LOT3 = [
  {id: 'n-p1-passebande', type: 'enonce', titre: 'Filtre passe-bande RLC', legende: 'Circuit RLC série alimenté par e(t) ; la sortie s est la tension aux bornes du résistor', svg: bandeE},
  {id: 'n-p1-passebande', type: 'correction', titre: 'Filtre passe-bande RLC', legende: 'Diviseur de tension : H = R/(R + jLω + 1/(jCω)). Le gain vaut 1 en ω₀ et la bande passante à −3 dB (|H| = 1/√2) a pour largeur Δω = ω₀/Q', svg: bandeC},
  {id: 'n-p1-passebas', type: 'enonce', titre: 'Filtre RC', legende: 'Résistor R en série, sortie s aux bornes du condensateur C, sortie ouverte', svg: basE},
  {id: 'n-p1-passebas', type: 'correction', titre: 'Filtre RC', legende: 'H = 1/(1 + jRCω) : passe-bas de coupure f_c ≈ 1,6 kHz. La composante continue et f₁ passent, f₂ = 20 kHz est atténuée d’environ 22 dB', svg: basC},
  {id: 'n-p2-fourier', type: 'correction', titre: 'Du créneau au triangle', legende: 'Pour f ≫ f_c le filtre intègre : le créneau (harmoniques impairs en 1/n) donne un triangle en phase (harmoniques en 1/n²), de crête à crête πEf_c/f', svg: fourierC},
  {id: 'p-em-2', type: 'correction', titre: 'Énergie d’un nuage électronique', legende: 'Gauss sur la sphère de rayon r ; ‖E‖ croît comme r dans la boule puis décroît en 1/r² ; W = ∫ ε₀E²/2 dτ sur des coquilles [r, r + dr]', svg: em2C},
  {id: 'n-p2-dipole', type: 'enonce', titre: 'Molécule d’eau près d’un ion', legende: 'Ion Na⁺ et molécule d’eau assimilée à un dipôle p en M, à la distance r ; θ est l’angle entre la direction de l’ion et p', svg: dipE},
  {id: 'n-p2-dipole', type: 'correction', titre: 'Molécule d’eau près d’un ion', legende: 'Le couple Γ = p ∧ E aligne p sur le champ de l’ion (équilibre stable θ = 0) ; le dipôle est alors attiré vers l’ion', svg: dipC},
  {id: 'n-p2-peau', type: 'enonce', titre: 'Effet de peau', legende: 'Conducteur de conductivité γ dans le demi-espace z > 0 ; champ E = E(z, t) u_x imposé en surface, E(0, t) = E₀ cos ωt', svg: peauE},
  {id: 'n-p2-peau', type: 'correction', titre: 'Effet de peau', legende: 'Champ et courants j = γE parallèles à la surface, d’amplitude décroissante en e^(−z/δ) avec δ = √(2/(μ₀γω)) ; à droite, deux instants dans l’enveloppe', svg: peauC},
  {id: 'n-p1-bobine', type: 'enonce', titre: 'Bobine plate', legende: 'Bobine plate de N spires et de surface S, fermée sur elle-même, dans un champ uniforme B(t) parallèle à son axe', svg: bobineE},
  {id: 'n-p1-bobine', type: 'correction', titre: 'Bobine plate', legende: 'Quand B croît, Φ croît, e = −dΦ/dt < 0 et i < 0 : le courant tourne dans le sens opposé à celui associé à n et son champ B_i s’oppose à la variation de B (loi de Lenz)', svg: bobineC},
  {id: 'n-p1-rails', type: 'enonce', titre: 'Rails de Laplace', legende: 'Barre de masse m lancée à la vitesse v₀ sur deux rails distants de ℓ fermés par R, dans un champ B vertical', svg: railsE},
  {id: 'n-p1-rails', type: 'correction', titre: 'Rails de Laplace', legende: 'Le flux Φ = Bℓx croît : le courant induit (i < 0) circule dans la barre selon −u_y et la force de Laplace F_L s’oppose à v : la barre freine', svg: railsC},
  {id: 'n-p1-transfo', type: 'enonce', titre: 'Transformateur', legende: 'Transformateur parfait (N₁ spires au primaire, N₂ au secondaire) alimenté par le secteur et chargé par R', svg: transfoE},
  {id: 'n-p1-transfo', type: 'correction', titre: 'Transformateur', legende: 'U₂/U₁ = N₂/N₁ = m et I₁/I₂ = m (puissance conservée) ; vu du primaire, la charge équivaut à R′ = R/m² ≈ 2,2 kΩ', svg: transfoC},
  {id: 'n-p2-alternateur', type: 'enonce', titre: 'Alternateur élémentaire', legende: 'Vue de dessus : la bobine (N spires, surface S) tourne à ω autour de l’axe Δ perpendiculaire à B ; θ est l’angle entre sa normale n et B', svg: alterE},
  {id: 'n-p2-alternateur', type: 'correction', titre: 'Alternateur élémentaire', legende: 'Avec θ = ωt, le flux vaut Φ = NBS cos ωt et la force électromotrice e = NBSω sin ωt, en quadrature avec le flux', svg: alterC},
  {id: 'n-p2-coax', type: 'enonce', titre: 'Câble coaxial', legende: 'Âme conductrice de rayon R₁, gaine conductrice de rayon intérieur R₂, isolant de permittivité relative εᵣ entre les deux', svg: coaxE},
];
