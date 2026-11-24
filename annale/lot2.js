// Lot 2 : diffusion thermique et thermodynamique.
import { CH, svg, L, P, poly, C, Ell, Rect, hatch, hatchRect, aire, paroi, vec, axe, fl, mid, cote, it, sub, sup, q, T, tick, V, pt, ptO,
  pol, arc, Ta, resistor, graphe } from './kit.js';

const n = v => Math.round(v * 10) / 10;
const ring = (cx, cy, r1, r2) => `<path d="M${cx - r2},${cy} a${r2},${r2} 0 1 0 ${2 * r2},0 a${r2},${r2} 0 1 0 ${-2 * r2},0 Z M${cx - r1},${cy} a${r1},${r1} 0 1 0 ${2 * r1},0 a${r1},${r1} 0 1 0 ${-2 * r1},0 Z" fill="url(#an-h)" fill-rule="evenodd" stroke="none"/>`;
const disque = (cx, cy, r) => `<circle cx="${cx}" cy="${cy}" r="${r}" fill="url(#an-h)" stroke="none"/>` + C(cx, cy, r);
const sep = (x, y1, y2) => L(x, y1, x, y2, 'pt');
const small = 13.5;

// ---------- ailette (énoncé) ----------
const ailetteE = svg(400, 190, paroi(60, 18, 60, 172, 1) + T(46, 100, q('T', '0'), 'end')
  + L(60, 78, 372, 78) + L(60, 112, 372, 112) + L(372, 78, 388, 78, 'pt') + L(372, 112, 388, 112, 'pt') + L(60, 95, 396, 95, 'mixte')
  + fl(150, 76, 150, 54) + fl(150, 114, 150, 136) + fl(240, 76, 240, 54) + fl(240, 114, 240, 136)
  + T(250, 58, it('h') + '(' + it('T') + ' − ' + q('T', 'e') + ')', 'start', small) + T(196, 32, 'air à ' + q('T', 'e'), 'middle', small)
  + cote(330, 95, 330, 78) + T(338, 91, it('a'), 'start')
  + axe(60, 158, 396, 158) + T(396, 176, it('x'), 'end') + L(60, 154, 60, 162, 'fin') + tick(60, 176, '0'),
  'Ailette cylindrique fixée à une paroi');

// ---------- conducteur refroidi latéralement ----------
const spe1E = svg(400, 195, hatchRect(56, 63, 12, 64) + Rect(56, 63, 12, 64) + hatchRect(332, 63, 12, 64) + Rect(332, 63, 12, 64)
  + L(68, 65, 332, 65) + L(68, 125, 332, 125) + L(18, 95, 56, 95) + L(344, 95, 382, 95) + mid(26, 95, 50, 95) + T(38, 86, it('i'))
  + L(68, 95, 332, 95, 'mixte') + fl(150, 63, 150, 40) + fl(150, 127, 150, 150) + fl(240, 63, 240, 40) + fl(240, 127, 240, 150)
  + T(250, 44, 'β(' + it('T') + ' − ' + q('T', '0') + ')', 'start', small) + T(120, 22, 'milieu extérieur à ' + q('T', '0'), 'middle', small)
  + cote(300, 95, 300, 65) + T(308, 85, it('a'), 'start') + tick(62, 145, 'calorifugé', 'middle') + tick(338, 145, 'calorifugé', 'middle')
  + axe(68, 176, 384, 176) + T(384, 192, it('z'), 'end') + L(68, 172, 68, 180, 'fin') + tick(68, 192, '0') + L(332, 172, 332, 180, 'fin') + tick(332, 192, it('L')),
  'Conducteur cylindrique parcouru par un courant');
const spe1C = (() => {
  const y = 112, r = 35, x1 = 170, x2 = 250;
  return svg(430, 250, L(30, y - r, 392, y - r) + L(30, y + r, 392, y + r) + L(20, y - r, 30, y - r, 'pt') + L(20, y + r, 30, y + r, 'pt') + L(392, y - r, 402, y - r, 'pt') + L(392, y + r, 402, y + r, 'pt')
    + L(12, y, 408, y, 'mixte') + Ell(x1, y, 10, r, 'fin') + Ell(x2, y, 10, r, 'fin')
    + vec(104, y, x1 - 4, y) + T(124, y - 8, 'Φ(' + it('z') + ')') + vec(x2 + 6, y, 322, y) + T(294, y - 8, 'Φ(' + it('z') + ' + d' + it('z') + ')')
    + T(210, y + 22, 'Joule', 'middle', 12.5)
    + vec(210, y - r - 2, 210, y - r - 30) + vec(210, y + r + 2, 210, y + r + 30)
    + T(222, y - r - 16, 'β(' + it('T') + ' − ' + q('T', '0') + ') 2π' + it('a') + ' d' + it('z'), 'start', small)
    + L(x1 - 6, y - 22, 112, 56, 'fin') + T(110, 52, 'section π' + it('a') + sup('2'), 'end')
    + axe(20, 226, 406, 226) + T(406, 244, it('z'), 'end') + L(x1, y + r, x1, 226, 'pt') + L(x2, y + r, x2, 226, 'pt') + tick(x1, 244, it('z')) + tick(x2, 244, it('z') + ' + d' + it('z')),
    'Conducteur : bilan sur la tranche [z, z + dz]');
})();

// ---------- phoque ----------
const phoqueE = svg(330, 255, C(150, 122, 95) + C(150, 122, 62) + pt(150, 122)
  + L(150, 122, ...pol(150, 122, 62, 150), 'fin') + T(...pol(150, 122, 40, 165).map((v, k) => v + (k ? -6 : 0)), q('R', 'i'))
  + L(150, 122, ...pol(150, 122, 95, 35), 'fin') + T(...pol(150, 122, 74, 46).map((v, k) => v + (k ? -4 : 6)), q('R', 'e'), 'start')
  + T(150, 136, 'cœur') + T(150, 156, it('P') + ', ' + q('T', 'i'), 'middle', small)
  + cote(150, 184, 150, 217) + T(158, 206, 'Δ' + it('R'), 'start')
  + L(...pol(150, 122, 80, -35), 262, 214, 'fin') + T(264, 226, 'graisse (λ)', 'start', small)
  + T(318, 26, 'eau à ' + q('T', 'e'), 'end', small) + T(12, 248, 'cylindre de longueur ' + it('L'), 'start', 12.5),
  'Phoque : cœur et couche de graisse');
const phoqueC = (() => {
  const c = [130, 125], Ri = 62, Re = 95, r = 79;
  let a = C(...c, Re) + C(...c, Ri) + C(...c, r, 'pt') + pt(...c) + T(c[0], c[1] + 18, 'cœur', 'middle', small);
  for (const ang of [20, 110, 200, 290]) a += vec(...pol(...c, Ri + 4, ang), ...pol(...c, Re + 26, ang));
  a += T(...pol(...c, Re + 32, 20).map((v, k) => v + (k ? 6 : 2)), 'Φ = ' + it('P'), 'start') + L(...c, ...pol(...c, r, 140), 'fin') + T(...pol(...c, r - 22, 150), it('r'));
  const y = 125, b = L(316, y, 372, y) + resistor(390, y) + L(407, y, 462, y) + pt(316, y) + pt(462, y) + mid(330, y, 356, y)
    + T(316, y + 24, q('T', 'i')) + T(462, y + 24, q('T', 'e')) + T(343, y - 10, 'Φ', 'middle') + T(390, y - 16, q('R', 'th'))
    + T(390, y + 54, q('R', 'th') + ' = ln(' + q('R', 'e') + '/' + q('R', 'i') + ')/(2πλ' + it('L') + ')', 'middle', 12.5);
  return svg(480, 255, a + sep(292, 20, 235) + b, 'Phoque : flux radial et résistance thermique');
})();

// ---------- rayon critique ----------
const isolantE = svg(330, 255, C(140, 125, 90) + disque(140, 125, 26)
  + L(140, 125, ...pol(140, 125, 90, 25), 'fin') + T(...pol(140, 125, 66, 36), q('r', '2'))
  + L(...pol(140, 125, 26, 135), 64, 40, 'fin') + T(62, 36, 'fil : ' + q('r', '1') + ', ' + q('T', '1'), 'end', small)
  + T(140, 192, 'gaine (λ)', 'middle', small) + T(320, 26, 'air : ' + q('T', 'e') + ', ' + it('h'), 'end', small)
  + [-30, 210, 250].map(a => fl(...pol(140, 125, 92, a), ...pol(140, 125, 116, a))).join(''),
  'Fil et gaine isolante');
const isolantC = (() => {
  const c = [110, 105], r1 = 18, r2 = 64;
  let a = C(...c, r2) + disque(...c, r1);
  for (const ang of [30, 120, 210, 300]) a += vec(...pol(...c, r2 + 2, ang), ...pol(...c, r2 + 30, ang));
  a += T(...pol(...c, r2 + 38, 30).map((v, k) => v + (k ? 4 : 2)), 'Φ', 'start');
  const y = 222, s = L(14, y, 38, y) + resistor(56, y) + L(73, y, 120, y) + resistor(138, y) + L(155, y, 196, y) + pt(14, y) + pt(105, y) + pt(196, y)
    + tick(14, y + 20, q('T', '1')) + tick(105, y + 20, q('T', 's')) + tick(196, y + 20, q('T', 'e')) + tick(56, y - 12, q('R', 'cond')) + tick(138, y - 12, q('R', 'conv'));
  const g = graphe(290, 28, 190, 170, [0, 82], [0, 62]), f = r => 5 * Math.log(r) + 100 / r, rc = 20;
  const b = g.axes(q('r', '2'), q('R', 'tot')) + g.courbe(f, 1.7, 80) + g.vl(rc, 'pt', 0, f(rc)) + pt(g.X(rc), g.Y(f(rc)))
    + tick(g.X(rc), g.Y(0) + 17, q('r', 'c') + ' = λ/' + it('h')) + T(g.X(52), g.Y(30), it('R') + sub('cond') + ' + ' + it('R') + sub('conv'), 'middle', 12.5);
  return svg(500, 250, a + s + sep(234, 16, 240) + b, 'Rayon critique : résistances en série');
})();

// ---------- diffusion ----------
const diffusionC = (() => {
  const y = 100, r = 30, x1 = 92, x2 = 152;
  const a = L(18, y - r, 218, y - r) + L(18, y + r, 218, y + r) + Ell(x1, y, 8, r, 'fin') + Ell(x2, y, 8, r, 'fin') + L(10, y, 226, y, 'mixte')
    + vec(34, y, x1 - 4, y) + T(54, y - 8, it('j') + '(' + it('x') + ')', 'middle', small) + vec(x2 + 5, y, 212, y) + T(184, y - 8, it('j') + '(' + it('x') + ' + d' + it('x') + ')', 'middle', small)
    + L(x1 - 4, y - 20, 60, 50, 'fin') + T(58, 46, 'section ' + it('S'), 'end', small)
    + axe(10, 176, 228, 176) + T(228, 194, it('x'), 'end') + L(x1, y + r, x1, 176, 'pt') + L(x2, y + r, x2, 176, 'pt') + tick(x1, 194, it('x')) + tick(x2, 194, it('x') + ' + d' + it('x'))
    + T(118, 224, '(a) bilan sur une tranche', 'middle', small);
  const g = graphe(276, 26, 200, 150, [-10, 10], [0, 1.1]), gs = s => x => Math.exp(-x * x / (2 * s * s)) / s;
  const b = g.axes(it('x'), it('n'), 0) + g.courbe(gs(1), -10, 10) + g.courbe(gs(2), -10, 10, 'ptobj') + g.courbe(gs(4), -10, 10, 'fin')
    + T(g.X(1.3), g.Y(.92), q('t', '1'), 'start', small) + T(g.X(2.7), g.Y(.43), '4' + q('t', '1'), 'start', small) + T(g.X(7.2), g.Y(.1), '16' + q('t', '1'), 'start', small)
    + cote(g.X(0), g.Y(gs(4)(4)), g.X(4), g.Y(gs(4)(4))) + T(g.X(4.6), g.Y(.32), '√(2' + it('Dt') + ')', 'start', 12.5)
    + T(376, 224, '(b) étalement des profils', 'middle', small);
  return svg(500, 235, a + sep(248, 14, 210) + b, 'Diffusion : bilan et profils n(x, t)');
})();

// ---------- ondes thermiques ----------
const spe5C = (() => {
  const X0 = 200, Y0 = 56, H = 186, W = 130, y = x => Y0 + x / 3 * H, tx = v => X0 + v * W;
  const cur = (f, k) => poly(Array.from({length: 161}, (_, i) => { const x = 3 * i / 160; return [tx(f(x)), y(x)]; }), k);
  return svg(400, 262, L(30, Y0, 370, Y0, 'epais') + T(200, 22, it('T') + '(0, ' + it('t') + ') = ' + q('T', 'm') + ' + ' + q('T', '0') + ' cos ω' + it('t'), 'middle', small)
    + T(36, Y0 + 44, 'sol', 'start', small) + axe(X0, Y0, X0, 252) + T(X0 + 8, 252, it('x'), 'start') + tick(X0, Y0 - 8, q('T', 'm'), 'middle')
    + cur(x => Math.exp(-x), 'pt') + cur(x => -Math.exp(-x), 'pt') + cur(x => Math.exp(-x) * Math.cos(x), 'obj') + cur(x => -Math.exp(-x) * Math.cos(x), 'ptobj')
    + L(36, y(1), 364, y(1), 'fin') + T(364, y(1) - 6, 'δ', 'end') + tick(tx(1), Y0 - 8, q('T', 'm') + ' + ' + q('T', '0'), 'middle') + tick(tx(-1), Y0 - 8, q('T', 'm') + ' − ' + q('T', '0'), 'middle')
    + T(X0 + 30, y(2.6), 'à quelques δ : ' + it('T') + ' ≈ ' + q('T', 'm'), 'start', 12.5),
    'Onde thermique dans le sol');
})();

// ---------- compression adiabatique ----------
const adiabE = svg(400, 206, L(30, 46, 336, 46, 'epais') + L(30, 134, 336, 134, 'epais') + L(30, 46, 30, 134, 'epais') + hatchRect(18, 34, 12, 112) + hatchRect(30, 34, 306, 12) + hatchRect(30, 134, 306, 12)
  + hatchRect(300, 47, 12, 86) + Rect(300, 47, 12, 86) + L(312, 90, 390, 90) + vec(386, 72, 340, 72) + T(364, 64, it('F'), 'middle')
  + Rect(57, 47, 8, 86, 'pt') + T(61, 24, 'état final', 'middle', 12.5) + T(306, 24, 'état initial', 'middle', 12.5)
  + T(180, 86, 'air', 'middle', small) + T(180, 106, q('P', '1') + ', ' + q('T', '1') + ', γ', 'middle', small)
  + cote(30, 182, 300, 182) + T(165, 198, q('V', '1')) + cote(30, 160, 57, 160) + T(66, 165, q('V', '2') + ' = ' + q('V', '1') + '/10', 'start', 13.5),
  'Compression de l’air dans un cylindre');
const adiabC = (() => {
  const g = graphe(64, 24, 290, 196, [0, 1.08], [0, 27]), ad = v => v ** -1.4, iso = v => 1 / v;
  let z = `M${n(g.X(.1))},${n(g.Y(0))}`; for (let k = 0; k <= 60; k++) { const v = .1 + .9 * k / 60; z += ` L${n(g.X(v))},${n(g.Y(ad(v)))}`; } z += ` L${n(g.X(1))},${n(g.Y(0))} Z`;
  return svg(410, 262, aire(z) + g.axes(it('V'), it('P')) + T(g.X(0) - 6, g.Y(0) + 16, it('O'), 'end') + g.courbe(ad, .1, 1) + g.courbe(iso, .1, 1, 'ptobj')
    + mid(g.X(.42), g.Y(ad(.42)), g.X(.38), g.Y(ad(.38))) + pt(g.X(1), g.Y(1)) + T(g.X(1) + 8, g.Y(1) - 6, '1', 'start')
    + pt(g.X(.1), g.Y(ad(.1))) + T(g.X(.1) + 8, g.Y(ad(.1)) + 4, '2', 'start') + pt(g.X(.1), g.Y(10)) + T(g.X(.1) + 8, g.Y(10) + 4, '2′', 'start')
    + L(g.X(.1), g.Y(ad(.1)), g.X(.1), g.Y(0), 'pt') + L(g.X(1), g.Y(1), g.X(1), g.Y(0), 'pt') + T(g.X(.1), g.Y(0) + 18, q('V', '2')) + T(g.X(1), g.Y(0) + 18, q('V', '1'))
    + T(g.X(.5), g.Y(7.4), 'adiabatique', 'start', 12.5) + T(g.X(.33), g.Y(1.2), 'isotherme', 'start', 12.5),
    'Compression : adiabatique et isotherme dans le diagramme de Watt');
})();

// ---------- réfrigérateur ----------
const frigoC = svg(450, 200, Rect(14, 66, 100, 64) + T(64, 92, 'intérieur', 'middle', small) + T(64, 114, q('T', 'F'), 'middle')
  + Rect(336, 66, 100, 64) + T(386, 92, 'cuisine', 'middle', small) + T(386, 114, q('T', 'C'), 'middle')
  + C(225, 98, 36) + T(225, 103, 'fluide', 'middle', small)
  + vec(116, 98, 186, 98) + T(150, 88, q('Q', 'F') + ' > 0', 'middle', small) + vec(264, 98, 334, 98) + T(300, 88, '−' + q('Q', 'C') + ' > 0', 'middle', small)
  + vec(225, 22, 225, 59) + T(235, 34, it('W') + ' > 0 (compresseur)', 'start', small)
  + T(225, 172, 'grandeurs reçues par le fluide sur un cycle', 'middle', 12.5),
  'Réfrigérateur : échanges du fluide sur un cycle');

// ---------- détente de Joule – Gay-Lussac ----------
function enceinte(x0, final) {
  const x = x0, y = 50, w = 190, h = 90, e = 10;
  const band = `M${x - e},${y - e} h${w + 2 * e} v${h + 2 * e} h${-w - 2 * e} Z M${x},${y} v${h} h${w} v${-h} Z`;
  let s = `<path d="${band}" fill="url(#an-h)" fill-rule="evenodd" stroke="none"/>` + Rect(x, y, w, h, 'epais');
  s += final ? L(x + w / 2, y, x + w / 2, y + 30) + L(x + w / 2, y + h - 30, x + w / 2, y + h)
    : L(x + w / 2, y, x + w / 2, y + 36) + L(x + w / 2, y + h - 36, x + w / 2, y + h) + L(x + w / 2, y + 36, x + w / 2, y + h - 36);
  const pts = final ? [[18, 22], [52, 60], [80, 30], [120, 70], [150, 26], [172, 58], [36, 74], [104, 44]] : [[16, 22], [40, 60], [64, 34], [82, 72], [28, 42], [70, 16], [52, 80], [86, 46]];
  s += pts.map(([u, v]) => pt(x + u, y + v, 2.4)).join('');
  s += final ? T(x + w / 2, y + h + 34, q('V', '2') + ' = 2' + q('V', '1') + ', ' + q('T', '2'), 'middle', small)
    : T(x + w / 4, y + h + 34, q('V', '1') + ', ' + q('T', '1'), 'middle', small) + T(x + 3 * w / 4, y + h / 2 + 5, 'vide', 'middle', small);
  return s + T(x + w / 2, y - 22, final ? '(b) vanne ouverte' : '(a) vanne fermée', 'middle', small);
}
const vdwC = svg(470, 200, enceinte(24, false) + enceinte(256, true), 'Détente de Joule – Gay-Lussac');

export const LOT2 = [
  {id: 'n-p2-ailette', type: 'enonce', titre: 'Ailette de refroidissement', legende: 'Tige de rayon a fixée en x = 0 à une paroi à T₀, dans l’air à Tₑ ; sa surface latérale cède h(T − Tₑ) par unité de surface', svg: ailetteE},
  {id: 'p-th-spe1', type: 'enonce', titre: 'Conducteur refroidi latéralement', legende: 'Conducteur de longueur L et de rayon a parcouru par i, calorifugé aux extrémités, qui cède β(T − T₀) par unité de surface latérale', svg: spe1E},
  {id: 'p-th-spe1', type: 'correction', titre: 'Conducteur refroidi latéralement', legende: 'Tranche [z, z + dz] : conduction axiale entrante et sortante, effet Joule i² dz/(γπa²) dans le volume, pertes latérales β(T − T₀)·2πa dz', svg: spe1C},
  {id: 'p-th-ccmp15', type: 'enonce', titre: 'Le phoque et sa couche de graisse', legende: 'Phoque modélisé par un cylindre de longueur L : cœur de rayon Rᵢ qui produit P, couche de graisse d’épaisseur ΔR, eau à Tₑ', svg: phoqueE},
  {id: 'p-th-ccmp15', type: 'correction', titre: 'Le phoque et sa couche de graisse', legende: 'En régime permanent, le même flux Φ = P traverse tout cylindre de rayon r de la graisse ; la graisse se comporte comme une résistance thermique entre Tᵢ et Tₑ', svg: phoqueC},
  {id: 'n-p2-isolant', type: 'enonce', titre: 'Rayon critique d’isolation', legende: 'Fil de rayon r₁ à T₁ entouré d’une gaine de conductivité λ et de rayon extérieur r₂ ; échanges conducto-convectifs (h) avec l’air à Tₑ', svg: isolantE},
  {id: 'n-p2-isolant', type: 'correction', titre: 'Rayon critique d’isolation', legende: 'Conduction dans la gaine, R_cond = ln(r₂/r₁)/(2πλL), puis convection, R_conv = 1/(2πr₂Lh), en série : la résistance totale est minimale (pertes maximales) pour r₂ = r_c = λ/h', svg: isolantC},
  {id: 'n-p2-diffusion', type: 'correction', titre: 'Diffusion d’un parfum', legende: '(a) Bilan de particules sur la tranche [x, x + dx] avec la loi de Fick j = −D ∂n/∂x. (b) Profils gaussiens à t₁, 4t₁ et 16t₁ : la largeur √(2Dt) double quand t quadruple', svg: diffusionC},
  {id: 'p-th-spe5', type: 'correction', titre: 'Ondes thermiques et caves', legende: 'Profils de température dans le sol à deux instants (trait plein et tireté), dans l’enveloppe T_m ± T₀e^(−x/δ) : l’onde s’amortit et se déphase ; à quelques δ la température est constante', svg: spe5C},
  {id: 'n-p1-adiab', type: 'enonce', titre: 'Compression dans un moteur Diesel', legende: 'Air (gaz parfait, γ = 1,4) comprimé rapidement par le piston du volume V₁ au volume V₂ = V₁/10', svg: adiabE},
  {id: 'n-p1-adiab', type: 'correction', titre: 'Compression dans un moteur Diesel', legende: 'Compression adiabatique réversible 1 → 2 (PVᵞ = cste), plus raide que l’isotherme 1 → 2′ ; le travail reçu est l’aire hachurée sous l’adiabatique (échelle : P en bar, V/V₁)', svg: adiabC},
  {id: 'n-p1-frigo', type: 'correction', titre: 'Réfrigérateur réel', legende: 'Sur un cycle, le fluide reçoit Q_F > 0 de l’intérieur et le travail W > 0, et cède −Q_C > 0 à la cuisine ; efficacité e = Q_F/W', svg: frigoC},
  {id: 'n-p2-vdw', type: 'correction', titre: 'Détente de Joule – Gay-Lussac', legende: 'Enceinte rigide et calorifugée : à l’ouverture de la vanne, le gaz occupe V₂ = 2V₁ sans travail ni chaleur reçus, donc ΔU = 0 ; pour un gaz de van der Waals, T₂ < T₁', svg: vdwC},
];
