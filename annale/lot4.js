// Lot 4 : mécanique.
import { CH, svg, L, P, poly, C, Ell, Rect, hatch, hatchRect, aire, paroi, vec, axe, fl, mid, cote, it, sub, sup, q, T, tick, V, pt, ptO,
  sortant, entrant, pol, arc, Ta, graphe } from './kit.js';

const n = v => Math.round(v * 10) / 10;
const small = 13.5, sep = (x, y1, y2) => L(x, y1, x, y2, 'pt');
const disqueH = (cx, cy, r) => `<circle cx="${n(cx)}" cy="${n(cy)}" r="${r}" fill="url(#an-h)" stroke="none"/>` + C(cx, cy, r);
// Ressort en zigzag entre (x1, y) et (x2, y).
function ressort(x1, x2, y, nb = 10, a = 8) {
  const l = x2 - x1, s = l / (nb + 2); let d = `M${x1},${y} h${s}`;
  for (let k = 0; k < nb; k++) d += ` l${s / 2},${k % 2 ? a : -a} l${s / 2},${k % 2 ? -a : a}`;
  return P(d + ` h${s}`);
}

// ---------- deux masses et un ressort ----------
function masses(corr) {
  let s = axe(16, 120, 386, 120) + T(386, 138, it('x'), 'end') + L(30, 115, 30, 125, 'fin') + T(30, 138, it('O'))
    + Rect(80, 72, 40, 40) + T(100, 97, q('m', '1')) + ressort(120, 250, 92) + Rect(250, 72, 40, 40) + T(270, 97, q('m', '2'))
    + L(100, 112, 100, 120, 'pt') + L(270, 112, 270, 120, 'pt') + tick(100, 138, q('x', '1')) + tick(270, 138, q('x', '2'));
  if (!corr) return s + T(185, 70, it('K') + ', ' + q('l', '0'), 'middle', small);
  return s + vec(120, 60, 166, 60) + T(143, 50, it('K') + '(' + it('X') + ' − ' + q('l', '0') + ')', 'middle', 12.5)
    + vec(250, 60, 204, 60) + T(227, 50, '−' + it('K') + '(' + it('X') + ' − ' + q('l', '0') + ')', 'middle', 12.5)
    + cote(100, 158, 270, 158) + T(185, 176, it('X') + ' = ' + q('x', '2') + ' − ' + q('x', '1'), 'middle', small);
}
const ressortE = svg(400, 150, masses(false), 'Deux masses reliées par un ressort');
const ressortC = svg(400, 186, masses(true), 'Deux masses : forces exercées par le ressort');

// ---------- pendule (énoncé) ----------
const penduleE = (() => {
  const O = [150, 36], Lp = 160, A0 = pol(...O, Lp, -30);
  return svg(330, 240, paroi(90, 36, 210, 36, -1) + pt(...O) + T(O[0] - 8, O[1] + 16, it('O'), 'end') + L(O[0], O[1], O[0], 222, 'mixte')
    + L(...O, ...A0) + C(...A0, 6) + pt(...A0, 1.8) + T(A0[0] + 10, A0[1] + 4, it('m'), 'start')
    + arc(...O, 48, -90, -30) + Ta(...O, 62, -60, q('θ', '0')) + T((O[0] + A0[0]) / 2 + 8, (O[1] + A0[1]) / 2 - 4, it('L'), 'start')
    + arc(...O, Lp, -90, -30, 'pt') + pt(O[0], O[1] + Lp) + vec(40, 120, 40, 172) + V(48, 160, 'g', '', 'start'), 'Pendule simple lâché depuis θ₀');
})();

// ---------- anneau sur une tige ----------
const tigeE = svg(380, 230, axe(170, 206, 170, 20) + T(178, 26, it('z'), 'start') + hatchRect(150, 200, 40, 16) + Rect(150, 200, 40, 16)
  + L(170, 120, 340, 120, 'epais') + pt(170, 120) + T(162, 138, it('O'), 'end') + Ell(250, 120, 6, 13) + T(262, 144, it('M'), 'start')
  + cote(170, 96, 250, 96) + T(210, 90, it('r')) + cote(170, 168, 340, 168) + T(255, 186, it('L'))
  + `<path d="M146,52 A26,8 0 1 0 194,52" fill="none" stroke="currentColor" stroke-width="${CH.wFin}" marker-end="url(#an-c)"/>` + T(204, 50, 'ω', 'start'),
  'Anneau sur une tige horizontale en rotation');
const tigeC = svg(400, 230, L(90, 115, 360, 115, 'epais') + sortant(90, 115, 6) + T(82, 140, it('O') + ', ' + q('ω', ''), 'end') + arc(90, 115, 30, 200, 320, 'fin', true)
  + Ell(240, 115, 6, 12) + pt(240, 115, 1.8) + T(232, 140, it('M'), 'end')
  + vec(248, 115, 316, 115) + T(300, 104, it('m') + 'ω' + sup('2') + it('r'), 'middle', small)
  + vec(240, 126, 240, 186) + T(248, 176, '−2' + it('m') + 'ω' + it('ṙ'), 'start', small) + vec(240, 104, 240, 46) + V(250, 58, 'R', 'θ', 'start')
  + cote(90, 86, 232, 86) + T(160, 80, it('r')) + axe(320, 206, 356, 206) + V(362, 212, 'u', 'r', 'start') + axe(320, 206, 320, 172) + V(328, 178, 'u', 'θ', 'start'),
  'Anneau : forces dans le référentiel tournant (vue de dessus)');

// ---------- cylindres sur un plan incliné ----------
function plan(O, B, base) {
  return poly([O, B, [O[0], B[1]]], 'obj', true) + hatchRect(O[0] - 6, B[1], B[0] - O[0] + 12, 8) + L(O[0] - 6, B[1], B[0] + 6, B[1]);
}
const geomPlan = (O, B) => { const l = Math.hypot(B[0] - O[0], B[1] - O[1]), u = [(B[0] - O[0]) / l, (B[1] - O[1]) / l], nn = [u[1], -u[0]], al = Math.atan2(B[1] - O[1], B[0] - O[0]) * 180 / Math.PI; return {u, nn, al}; };
const roulE = (() => {
  const O = [30, 54], B = [350, 196], {u, nn, al} = geomPlan(O, B), Rr = 24, at = s => [O[0] + s * u[0] + Rr * nn[0], O[1] + s * u[1] + Rr * nn[1]];
  const c1 = at(70), c2 = at(170);
  return svg(380, 222, plan(O, B) + disqueH(...c1, Rr) + pt(...c1, 1.8) + C(...c2, Rr, 'epais') + pt(...c2, 1.8)
    + T(c1[0], c1[1] - 32, 'plein', 'middle', 12.5) + T(c2[0], c2[1] - 32, 'creux', 'middle', 12.5) + L(...c2, ...pol(...c2, Rr, 120), 'fin') + T(...pol(...c2, 12, 150).map((v, k) => v + (k ? -4 : -6)), it('R'), 'end')
    + `<path d="M${B[0] - 54},${B[1]} A54,54 0 0 0 ${n(B[0] - 54 * Math.cos(al * Math.PI / 180))},${n(B[1] - 54 * Math.sin(al * Math.PI / 180))}" fill="none" stroke="currentColor" stroke-width="${CH.wFin}"/>`
    + T(B[0] - 70, B[1] - 8, 'α', 'middle') + vec(330, 30, 330, 80) + V(338, 68, 'g', '', 'start'), 'Cylindres plein et creux sur un plan incliné');
})();
const roulC = (() => {
  const O = [24, 46], B = [356, 210], {u, nn, al} = geomPlan(O, B), Rr = 40, s0 = 160, I = [O[0] + s0 * u[0], O[1] + s0 * u[1]], G = [I[0] + Rr * nn[0], I[1] + Rr * nn[1]];
  return svg(380, 240, plan(O, B) + C(...G, Rr) + pt(...G) + pt(...I) + T(G[0] - 8, G[1] - 6, it('G'), 'end') + T(I[0] - 4, I[1] + 18, it('I'), 'end')
    + vec(...G, G[0], G[1] + 74) + V(G[0] + 8, G[1] + 70, 'P', '', 'start') + vec(...I, I[0] + 92 * nn[0], I[1] + 92 * nn[1]) + V(I[0] + 100 * nn[0] - 12, I[1] + 100 * nn[1], 'N', '', 'end')
    + vec(...I, I[0] - 52 * u[0], I[1] - 52 * u[1]) + V(I[0] - 62 * u[0], I[1] - 62 * u[1] + 18, 'T', '', 'middle')
    + vec(G[0] + 46 * u[0] + 18 * nn[0], G[1] + 46 * u[1] + 18 * nn[1], G[0] + 96 * u[0] + 18 * nn[0], G[1] + 96 * u[1] + 18 * nn[1]) + V(G[0] + 96 * u[0] + 18 * nn[0] + 6, G[1] + 96 * u[1] + 18 * nn[1] - 4, 'v', '', 'start')
    + arc(...G, 24, 160, 60, 'fin', true) + Ta(...G, 34, 175, 'ω')
    + `<path d="M${B[0] - 54},${B[1]} A54,54 0 0 0 ${n(B[0] - 54 * Math.cos(al * Math.PI / 180))},${n(B[1] - 54 * Math.sin(al * Math.PI / 180))}" fill="none" stroke="currentColor" stroke-width="${CH.wFin}"/>`
    + T(B[0] - 70, B[1] - 8, 'α'), 'Cylindre roulant : forces et sens de rotation');
})();

// ---------- pendule sur un plateau tournant ----------
const meca3E = svg(330, 250, Ell(160, 198, 126, 26) + L(160, 14, 160, 234, 'mixte') + L(244, 198, 244, 46, 'epais') + L(244, 46, 160, 46, 'epais')
  + pt(160, 46) + T(152, 42, it('S'), 'end') + L(160, 46, 184, 156) + C(184, 156, 6) + pt(184, 156, 1.8) + T(196, 162, it('M'), 'start') + T(178, 104, it('L'), 'start')
  + `<path d="M136,26 A24,7 0 1 0 184,26" fill="none" stroke="currentColor" stroke-width="${CH.wFin}" marker-end="url(#an-c)"/>` + V(196, 26, 'Ω', '', 'start')
  + T(258, 120, 'mât', 'start', 12.5) + T(60, 240, 'plateau', 'middle', 12.5),
  'Pendule fixé au sommet d’un mât sur un plateau tournant');
const meca3C = (() => {
  const O = [110, 150], M = pol(...O, 140, 32), st = (a, l) => pol(...M, l, a);
  return svg(400, 250, sortant(...O, 6) + T(O[0] - 10, O[1] + 22, it('O') + ', ' + 'Ω', 'end') + L(...O, ...M, 'pt') + L(...O, O[0] + 70, O[1], 'pt') + arc(...O, 44, 0, 32) + Ta(...O, 58, 16, 'θ')
    + C(...M, 6) + pt(...M, 1.8) + T(M[0] - 6, M[1] - 12, it('M'), 'end')
    + vec(...M, ...st(212, 74)) + V(...st(212, 90), 'f') + vec(...M, ...st(32, 30)) + T(...st(32, 48), it('m') + 'Ω' + sup('2') + it('r'), 'start', small)
    + fl(...M, ...st(150, 50), 'ptobj') + V(...st(150, 64), 'v', '′') + vec(...M, ...st(60, 52)) + V(...st(62, 68), 'f', 'ic', 'start')
    + T(200, 240, it('f') + ' = −' + it('mgr') + '/' + it('L') + ' (rappel du fil)', 'middle', 12.5),
    'Pendule : forces dans le plan horizontal (référentiel du plateau)');
})();

// ---------- chute avec frottement ----------
const chuteC = (() => {
  const g = graphe(200, 30, 210, 150, [0, 5], [0, 1.15]);
  return svg(450, 222, C(80, 110, 14) + vec(80, 126, 80, 188) + V(90, 180, 'P', '', 'start') + vec(80, 94, 80, 44) + T(90, 56, '−α', 'start') + V(108, 56, 'v', '', 'start') + vec(120, 90, 120, 140) + V(128, 128, 'v', '', 'start') + axe(30, 60, 30, 200) + V(22, 196, 'u', 'z', 'end') + sep(170, 14, 210)
    + g.axes(it('t'), it('v')) + g.hl(1, 'pt') + tick(g.X(0) - 5, g.Y(1) + 4, q('v', 'ℓ'), 'end') + g.courbe(t => 1 - Math.exp(-t), 0, 5) + L(g.X(0), g.Y(0), g.X(1), g.Y(1), 'fin')
    + g.vl(1, 'pt', 0, 1) + tick(g.X(1), g.Y(0) + 15, 'τ') + g.vl(3, 'pt', 0, .95) + pt(g.X(3), g.Y(.95)) + tick(g.X(3), g.Y(0) + 15, '3τ'),
    'Chute avec frottement linéaire : forces et vitesse');
})();

// ---------- satellite géostationnaire ----------
const geoC = (() => {
  const c = [150, 145], RT = 18, r = RT * 42200 / 6370, M = pol(...c, r, 35);
  return svg(320, 290, C(...c, r, 'pt') + C(...c, RT) + sortant(...c, 4) + arc(...c, 30, 200, 300, 'fin', true) + Ta(...c, 42, 252, 'Ω' + sub('T'))
    + C(...M, 5) + vec(...M, ...pol(...M, 58, 125)) + V(...pol(...M, 72, 128), 'v') + vec(...M, ...pol(...M, 44, 215)) + V(...pol(...M, 58, 230), 'F')
    + L(...c, ...pol(...c, r, 160), 'fin') + T(...pol(...c, r / 2, 168), it('r')) + T(c[0] + 24, c[1] + 30, q('R', 'T'), 'start')
    + T(160, 284, 'plan équatorial, vu du pôle Nord', 'middle', 12.5), 'Orbite géostationnaire');
})();

// ---------- désorbitation ----------
const ccmp13C = (() => {
  const c = [200, 120], RT = 18, rp = RT * 6470 / 6370, ra = 5 * RT, a = (ra + rp) / 2, cx = c[0] - ra + a, cc = c[0] - cx, b = Math.sqrt(a * a - cc * cc);
  const A = [c[0] - ra, c[1]], Pp = [c[0] + rp, c[1]];
  return svg(360, 250, C(...c, ra, 'pt') + C(...c, rp + 3, 'fin') + C(...c, RT) + `<path d="M${A[0]},${A[1]} A${n(a)},${n(b)} 0 0 0 ${n(Pp[0])},${Pp[1]}" fill="none" stroke="currentColor" stroke-width="${CH.wObj}"/>`
    + mid(cx - 10, c[1] + b, cx + 10, c[1] + b) + pt(...A) + pt(...Pp)
    + vec(...A, A[0], A[1] + 66) + V(A[0] - 8, A[1] + 60, 'v', '1', 'end') + vec(A[0] + 10, A[1], A[0] + 10, A[1] + 36) + V(A[0] + 18, A[1] + 34, 'v', '2', 'start')
    + vec(...Pp, Pp[0], Pp[1] - 82) + V(Pp[0] + 8, Pp[1] - 70, 'v', '3', 'start')
    + T(A[0] - 8, A[1] - 10, 'manœuvre', 'end', 12)
    + L(...c, ...pol(...c, ra, 120), 'fin') + T(...pol(...c, ra / 2 + 8, 128), '5' + q('R', 'T')) + T(c[0] + 26, c[1] + 40, 'atmosphère', 'start', 12),
    'Désorbitation : orbite circulaire et demi-ellipse de transfert');
})();

// ---------- atmosphère isotherme ----------
const atmoC = (() => {
  const a = Rect(40, 70, 110, 50) + vec(95, 186, 95, 122) + T(103, 172, it('P') + '(' + it('z') + ')' + it('S'), 'start', 12.5) + vec(95, 30, 95, 68) + T(103, 40, it('P') + '(' + it('z') + ' + d' + it('z') + ')' + it('S'), 'start', 12.5)
    + vec(60, 95, 60, 135) + T(52, 140, it('dm g'), 'end', 12.5) + axe(20, 200, 20, 30) + T(28, 32, it('z'), 'start') + T(95, 214, '(a) tranche d’air', 'middle', 12.5);
  const b = C(250, 90, 32) + L(250, 122, 250, 146) + Rect(240, 146, 20, 12) + vec(250, 56, 250, 20) + V(260, 30, 'Π', 'A', 'start') + vec(250, 160, 250, 196) + V(260, 192, 'P', '', 'start')
    + T(250, 214, '(b) ballon', 'middle', 12.5);
  const g = graphe(360, 30, 170, 160, [0, 1.12], [0, 3]);
  let cur = ''; for (let k = 0; k <= 80; k++) { const z = 3 * k / 80; cur += (k ? ' L' : 'M') + n(g.X(Math.exp(-z))) + ',' + n(g.Y(z)); }
  const c = g.axes(it('P'), it('z')) + P(cur) + L(g.X(0), g.Y(1), g.X(Math.exp(-1)), g.Y(1), 'pt') + L(g.X(Math.exp(-1)), g.Y(1), g.X(Math.exp(-1)), g.Y(0), 'pt')
    + tick(g.X(0) - 5, g.Y(1) + 4, it('H'), 'end') + tick(g.X(Math.exp(-1)), g.Y(0) + 15, q('P', '0') + '/e') + tick(g.X(1), g.Y(0) + 15, q('P', '0')) + T(445, 226, '(c) ' + it('P') + ' = ' + q('P', '0') + 'e' + sup('−' + it('z') + '/' + it('H')), 'middle', 12.5);
  return svg(560, 236, a + sep(185, 14, 220) + b + sep(318, 14, 220) + c, 'Atmosphère isotherme : équilibre d’une tranche, ballon, P(z)');
})();

export const LOT4 = [
  {id: 'n-p1-chute', type: 'correction', titre: 'Chute avec frottements', legende: 'Forces sur la bille : poids P et frottement −αv ; la vitesse tend vers v_ℓ = mg/α avec τ = m/α (95 % en 3τ)', svg: chuteC},
  {id: 'p-meca-ccs-ressort', type: 'enonce', titre: 'Deux masses et un ressort', legende: 'Deux masses m₁ et m₂ reliées par un ressort (K, l₀), mobiles sur l’axe Ox, d’abscisses x₁ et x₂', svg: ressortE},
  {id: 'p-meca-ccs-ressort', type: 'correction', titre: 'Deux masses et un ressort', legende: 'Ressort allongé (X > l₀) : il tire m₁ vers +u_x et m₂ vers −u_x avec des forces opposées ; X = x₂ − x₁ vérifie μẌ = −K(X − l₀)', svg: ressortC},
  {id: 'n-p1-pendule', type: 'enonce', titre: 'Pendule simple', legende: 'Masse m suspendue à un fil de longueur L, lâchée sans vitesse depuis l’angle θ₀ = 60°', svg: penduleE},
  {id: 'n-p1-geostat', type: 'correction', titre: 'Satellite géostationnaire', legende: 'Orbite circulaire dans le plan équatorial, à l’échelle : r ≈ 42 200 km ≈ 6,6 R_T ; le satellite tourne dans le même sens que la Terre, avec la période d’un jour sidéral', svg: geoC},
  {id: 'n-p2-tige', type: 'enonce', titre: 'Anneau sur une tige en rotation', legende: 'Tige horizontale de longueur L tournant à ω autour de Oz ; l’anneau M, à la distance r de l’axe, glisse sans frottement', svg: tigeE},
  {id: 'n-p2-tige', type: 'correction', titre: 'Anneau sur une tige en rotation', legende: 'Vue de dessus, dans le référentiel de la tige : force d’inertie d’entraînement mω²r u_r, Coriolis −2mωṙ u_θ compensée par R_θ ; poids et R_z, verticaux, ne sont pas représentés', svg: tigeC},
  {id: 'n-p2-roulement', type: 'enonce', titre: 'Course de cylindres', legende: 'Cylindre plein et cylindre creux de même masse m et de même rayon R, lâchés côte à côte sur un plan incliné d’angle α', svg: roulE},
  {id: 'n-p2-roulement', type: 'correction', titre: 'Course de cylindres', legende: 'Forces sur un cylindre : poids P en G, réaction normale N et frottement T (vers le haut de la pente) au contact I ; roulement sans glissement v = Rω', svg: roulC},
  {id: 'p-meca-3', type: 'enonce', titre: 'Oscillations en étoile', legende: 'Pendule de longueur L accroché en S au sommet d’un mât, sur un plateau tournant à Ω autour de la verticale de S', svg: meca3E},
  {id: 'p-meca-3', type: 'correction', titre: 'Oscillations en étoile', legende: 'Dans le plan horizontal (référentiel du plateau) : rappel du fil f = −(mg/L) r u_r, force centrifuge mΩ²r u_r, Coriolis f_ic = −2mΩ u_z ∧ v′, perpendiculaire à la vitesse relative', svg: meca3C},
  {id: 'p-meca-ccmp13', type: 'correction', titre: 'Satellisation et désorbitation', legende: 'Freinage bref sur l’orbite de rayon 5R_T (v₁ → v₂) : le satellite suit une demi-ellipse d’apogée 5R_T et de périgée R_T + 100 km, où il arrive à v₃', svg: ccmp13C},
  {id: 'n-p1-atmo', type: 'correction', titre: 'Atmosphère isotherme', legende: '(a) Équilibre d’une tranche : dP = −ρg dz. (b) Ballon : poussée d’Archimède et poids. (c) P décroît en e^(−z/H), H = RT/(Mg) ≈ 8,4 km', svg: atmoC},
];
