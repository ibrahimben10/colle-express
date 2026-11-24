// Lot test n° 1 : dix schémas pour fixer la charte « annale ».
import { CH, svg, L, P, poly, C, Ell, Rect, hatch, aire, paroi, vec, axe, fl, mid, cote, it, rm, sub, sup, q, T, tick, V, pt, ptO, sortant, entrant,
  pol, arc, Ta, resistor, condo, bobine, generateur, interrupteur, borne, courant, graphe } from './kit.js';

const n = v => Math.round(v * 10) / 10;

// ---------- circuits RC ----------
function circuitRC(withCorr) {
  const xl = 60, xr = 300, yt = 50, yb = 170;
  return generateur(xl, 110) + L(xl, yt, xl, 98) + L(xl, 122, xl, yb)
    + L(xl, yt, 110, yt) + interrupteur(110, yt, 140, yt) + L(142, yt, 168, yt) + resistor(185, yt) + L(202, yt, xr, yt)
    + L(xr, yt, xr, 106.5) + condo(xr, 110, false) + L(xr, 113.5, xr, yb) + L(xl, yb, xr, yb)
    + fl(38, 136, 38, 84) + T(30, 115, it('E'), 'end') + T(125, 32, it('K')) + T(185, 34, it('R'))
    + courant(245, yt, 'r', it('i'), 0, -9)
    + fl(278, 142, 278, 78) + T(270, 115, q('u', 'C'), 'end')
    + (withCorr ? fl(203, 66, 167, 66) + T(185, 86, q('u', 'R')) + T(316, 102, '+' + it('q'), 'start') + T(316, 130, '−' + it('q'), 'start')
      : T(322, 115, it('C'), 'start'));
}
const rcE = svg(360, 200, circuitRC(false), 'Circuit RC série');
const rcC = (() => {
  const cx1 = 392, cx2 = 500, f = 13.5, CE2 = it('C') + it('E') + sup('2'), half = '½';
  return svg(560, 200, circuitRC(true)
    + T(446, 40, 'générateur', 'middle', f) + T(446, 58, q('W', 'g') + ' = ' + CE2, 'middle', f)
    + L(446, 66, 446, 88) + fl(446, 88, cx1, 118) + fl(446, 88, cx2, 118)
    + T(cx1, 136, 'effet Joule', 'middle', f) + T(cx1, 154, q('W', 'J') + ' = ' + half + CE2, 'middle', f)
    + T(cx2, 136, 'condensateur', 'middle', f) + T(cx2, 154, q('W', 'C') + ' = ' + half + CE2, 'middle', f)
    + L(340, 22, 340, 176, 'pt'), 'Circuit RC : conventions et bilan d’énergie');
})();

// ---------- circuits RLC ----------
function circuitRLC(corr) {
  const xl = 60, xr = 280, yt = corr ? 60 : 50, yb = corr ? 180 : 170, ym = (yt + yb) / 2;
  let s = L(xl, yt, xl, yb) + L(xl, yt, 95, yt)
    + (corr ? borne(95, yt) + L(97, yt, 123, yt) + borne(125, yt) : interrupteur(95, yt, 125, yt))
    + L(127, yt, 160, yt) + bobine(180, yt) + L(200, yt, xr, yt)
    + L(xr, yt, xr, ym - 3.5) + condo(xr, ym, false) + L(xr, ym + 3.5, xr, yb)
    + L(xl, yb, 148, yb) + resistor(165, yb) + L(182, yb, xr, yb);
  if (!corr) return s + T(110, 32, it('K') + ' (' + it('t') + ' = 0)') + T(180, 34, it('L')) + T(165, 194, it('R'))
    + T(298, ym + 5, it('C'), 'start') + T(262, ym - 6, '+' + q('q', '0'), 'end') + T(170, ym + 5, q('u', 'C') + '(0) = ' + q('U', '0'), 'middle', 13.5);
  return s + T(110, yt - 10, it('K'), 'middle') + T(180, yt + 22, it('L'))
    + courant(240, yt, 'r', it('i'), 0, -9)
    + fl(200, yt - 14, 160, yt - 14) + T(180, yt - 22, q('u', 'L'))
    + fl(262, yb - 30, 262, yt + 30) + T(254, ym + 5, q('u', 'C'), 'end') + T(296, ym - 8, '+' + it('q'), 'start') + T(296, ym + 20, it('C'), 'start')
    + fl(148, yb + 16, 182, yb + 16) + T(165, yb + 34, q('u', 'R'));
}
const rlcE = svg(340, 205, circuitRLC(false), 'Circuit RLC série en régime libre');
const rlcC = (() => {
  const g = graphe(350, 46, 150, 130, [0, 3.3], [-1.1, 1.4]), al = 1, W = Math.sqrt(100 - 1), Tp = 2 * Math.PI / W * 1;
  const qq = t => Math.exp(-al * t) * (Math.cos(W * t) + al / W * Math.sin(W * t));
  // t en unités de 1/α (ici ω₀ = 10α, Q = 5)
  return svg(540, 225, circuitRLC(true) + g.axes(it('t'), it('q'))
    + g.courbe(t => Math.exp(-al * t), 0, 3.3, 'pt') + g.courbe(t => -Math.exp(-al * t), 0, 3.3, 'pt') + g.courbe(qq, 0, 3.3, 'obj', 500)
    + tick(g.X(0) - 6, g.Y(1) + 4, q('q', '0'), 'end') + L(g.X(0) - 3, g.Y(1), g.X(0) + 3, g.Y(1), 'fin')
    + L(g.X(Tp), g.Y(qq(Tp)), g.X(Tp), g.Y(-1.05), 'pt') + L(g.X(2 * Tp), g.Y(qq(2 * Tp)), g.X(2 * Tp), g.Y(-1.05), 'pt')
    + cote(g.X(Tp), g.Y(-1), g.X(2 * Tp), g.Y(-1)) + T((g.X(Tp) + g.X(2 * Tp)) / 2, g.Y(-1) + 18, it('T'))
    + L(330, 22, 330, 205, 'pt'), 'Circuit RLC libre : conventions et allure de q(t)');
})();

// ---------- cycle de Beau de Rochas (allure, a = 4 pour la lisibilité) ----------
const beauC = (() => {
  const g = graphe(64, 26, 270, 196, [0, 4.7], [0, 17]), ga = 1.4, a = 4, P2 = a ** ga, P3 = 2.2 * P2, P4 = P3 / a ** ga;
  const f2 = v => P2 * v ** -ga, f3 = v => P3 * v ** -ga, at = (f, v) => [g.X(v), g.Y(f(v))];
  let zone = `M${g.X(1)},${g.Y(P2)}`; for (let k = 0; k <= 60; k++) { const v = 1 + 3 * k / 60; zone += ` L${n(g.X(v))},${n(g.Y(f2(v)))}`; }
  zone += ` L${g.X(4)},${g.Y(P4)}`; for (let k = 60; k >= 0; k--) { const v = 1 + 3 * k / 60; zone += ` L${n(g.X(v))},${n(g.Y(f3(v)))}`; } zone += ' Z';
  return svg(400, 262, aire(zone) + g.axes(it('V'), it('P')) + T(g.X(0) - 6, g.Y(0) + 16, it('O'), 'end')
    + g.courbe(f2, 1, 4) + g.courbe(f3, 1, 4) + L(g.X(1), g.Y(P2), g.X(1), g.Y(P3)) + L(g.X(4), g.Y(1), g.X(4), g.Y(P4))
    + mid(...at(f2, 2.55), ...at(f2, 2.45)) + mid(...at(f3, 2.0), ...at(f3, 2.1)) + mid(g.X(1), g.Y(P2), g.X(1), g.Y(P3)) + mid(g.X(4), g.Y(P4), g.X(4), g.Y(1))
    + [[4, 1, '1', 10, 16], [1, P2, '2', -10, 5], [1, P3, '3', -10, 5], [4, P4, '4', -10, -4]].map(([v, p, s, dx, dy]) => pt(g.X(v), g.Y(p)) + T(g.X(v) + dx, g.Y(p) + dy, s, dx > 0 ? 'start' : 'end')).join('')
    + L(g.X(1), g.Y(P2), g.X(1), g.Y(0), 'pt') + L(g.X(4), g.Y(1), g.X(4), g.Y(0), 'pt') + T(g.X(1), g.Y(0) + 18, q('V', '2')) + T(g.X(4), g.Y(0) + 18, q('V', '1'))
    + fl(g.X(1) - 46, g.Y(11), g.X(1) - 4, g.Y(11)) + T(g.X(1) - 26, g.Y(11) - 8, q('Q', '23'))
    + fl(g.X(4) + 4, g.Y(1.6), g.X(4) + 44, g.Y(1.6)) + T(g.X(4) + 26, g.Y(1.6) - 9, q('Q', '41'))
    + T(g.X(2.75), g.Y(2.55), it('W') + ' < 0', 'middle', 13.5), 'Cycle de Beau de Rochas dans le diagramme de Watt');
})();

// ---------- ailette : bilan sur une tranche ----------
const ailetteC = (() => {
  const y = 112, r = 34, x1 = 170, x2 = 250;
  return svg(420, 250, L(30, y - r, 390, y - r) + L(30, y + r, 390, y + r) + L(22, y - r, 30, y - r, 'pt') + L(22, y + r, 30, y + r, 'pt') + L(390, y - r, 398, y - r, 'pt') + L(390, y + r, 398, y + r, 'pt')
    + L(14, y, 404, y, 'mixte')
    + Ell(x1, y, 10, r, 'fin') + Ell(x2, y, 10, r, 'fin')
    + vec(106, y, x1 - 4, y) + T(124, y - 8, 'Φ(' + it('x') + ')') + vec(x2 + 6, y, 318, y) + T(292, y - 8, 'Φ(' + it('x') + ' + d' + it('x') + ')')
    + vec(210, y - r - 2, 210, y - r - 32) + vec(210, y + r + 2, 210, y + r + 32)
    + T(222, y - r - 18, it('h') + 'θ · 2π' + it('a') + ' d' + it('x'), 'start')
    + L(x1 - 6, y - 22, 112, 56, 'fin') + T(110, 52, 'section π' + it('a') + sup('2'), 'end')
    + cote(352, y, 352, y - r) + T(360, y - 13, it('a'), 'start')
    + T(330, y + r + 26, 'θ = ' + it('T') + ' − ' + q('T', 'e'), 'middle', 14)
    + axe(20, 226, 404, 226) + T(404, 244, it('x'), 'end')
    + L(x1, y + r, x1, 226, 'pt') + L(x2, y + r, x2, 226, 'pt') + tick(x1, 244, it('x')) + tick(x2, 244, it('x') + ' + d' + it('x')),
    'Ailette : bilan d’énergie sur la tranche [x, x + dx]');
})();

// ---------- câble coaxial : Gauss et Ampère ----------
function coupe(cx, cy, R1, R2, e) {
  const ring = `M${cx - R2 - e},${cy} a${R2 + e},${R2 + e} 0 1 0 ${2 * (R2 + e)},0 a${R2 + e},${R2 + e} 0 1 0 ${-2 * (R2 + e)},0 Z M${cx - R2},${cy} a${R2},${R2} 0 1 0 ${2 * R2},0 a${R2},${R2} 0 1 0 ${-2 * R2},0 Z`;
  return `<path d="${ring}" fill="url(#an-h)" fill-rule="evenodd" stroke="none"/>` + C(cx, cy, R2) + C(cx, cy, R2 + e)
    + `<circle cx="${cx}" cy="${cy}" r="${R1}" fill="url(#an-h)" stroke="none"/>` + C(cx, cy, R1);
}
const coaxC = (() => {
  const R1 = 22, R2 = 84, e = 6, A = [120, 120], B = [370, 120], r = 54;
  let a = coupe(...A, R1, R2, e) + C(...A, r, 'pt');
  for (const ang of [20, 80, 140, 200, 260, 320]) a += vec(...pol(...A, R1 + 4, ang), ...pol(...A, R2 - 6, ang));
  a += T(...pol(...A, r + 2, 52).map((v, k) => v + (k ? -6 : 6)), it('r'), 'start')
    + L(...pol(...A, R1, 235), A[0] - 74, 212, 'fin') + T(A[0] - 76, 226, '+' + it('Q') + ' (sur ' + it('ℓ') + ')', 'start', 13.5)
    + V(...pol(...A, R2 - 16, 20).map((v, k) => v + (k ? 18 : 4)), 'E', '', 'start');
  let b = coupe(...B, R1, R2, e) + C(...B, r, 'pt') + arc(...B, r, 60, 95, 'obj', true) + sortant(...B, 6);
  for (const ang of [0, 90, 180, 270]) { const [x, y] = pol(...B, r, ang), [tx, ty] = [Math.cos((ang + 90) * Math.PI / 180), -Math.sin((ang + 90) * Math.PI / 180)]; b += vec(x, y, x + 26 * tx, y + 26 * ty); }
  b += V(B[0] + r + 8, B[1] - 26, 'B', '', 'start') + T(B[0] + 12, B[1] + 20, it('I'), 'start')
    + L(...pol(...B, R2 + 3, 235), B[0] - 70, 214, 'fin') + T(B[0] - 72, 226, '−' + it('I') + ' (retour)', 'end', 13.5);
  return svg(500, 262, a + b
    + L(...pol(...A, R1, 150), 24, 34, 'fin') + T(22, 30, q('R', '1'), 'start') + L(...pol(...A, R2, 130), 52, 22, 'fin') + T(54, 18, q('R', '2'), 'start')
    + T(A[0], 254, '(a) capacité : cylindre de Gauss', 'middle', 13.5) + T(B[0], 254, '(b) inductance : contour d’Ampère', 'middle', 13.5)
    + L(245, 16, 245, 236, 'pt'), 'Câble coaxial : théorèmes de Gauss et d’Ampère');
})();

// ---------- pendule : forces et énergie potentielle ----------
const penduleC = (() => {
  const O = [170, 40], Lp = 170, th = 30, M = pol(...O, Lp, -90 + th), A0 = pol(...O, Lp, -30), B = [O[0], O[1] + Lp];
  const ur = [Math.sin(th * Math.PI / 180), Math.cos(th * Math.PI / 180)], ut = [ur[1], -ur[0]];
  return svg(390, 290, paroi(110, 40, 230, 40, -1) + pt(...O) + T(O[0] - 8, O[1] + 16, it('O'), 'end')
    + L(O[0], O[1], O[0], 238, 'mixte') + arc(...O, Lp, -90, -30, 'pt') + L(...O, ...A0, 'pt') + ptO(...A0, 3.5) + T(A0[0] + 8, A0[1] - 6, it('A'), 'start')
    + L(...O, ...M) + C(...M, 6) + pt(...M, 1.8) + T(M[0] - 12, M[1] + 16, it('M'), 'end')
    + arc(...O, 42, -90, -90 + th) + Ta(...O, 56, -90 + th / 2, 'θ') + arc(...O, 70, -90 + th, -30, 'fin') + Ta(...O, 86, -45, q('θ', '0'))
    + vec(...M, M[0], M[1] + 62) + V(M[0] + 10, M[1] + 60, 'P', '', 'start')
    + vec(...M, M[0] - 30 * ur[0] * 1.8, M[1] - 30 * ur[1] * 1.8) + V(M[0] - 58, M[1] - 40, 'T', '', 'middle')
    + fl(...M, M[0] + 30 * ur[0], M[1] + 30 * ur[1], 'obj') + V(M[0] + 30 * ur[0] + 8, M[1] + 30 * ur[1] + 12, 'u', 'r', 'start')
    + fl(...M, M[0] + 30 * ut[0], M[1] + 30 * ut[1], 'obj') + V(M[0] + 30 * ut[0] + 6, M[1] + 30 * ut[1] - 2, 'u', 'θ', 'start')
    + pt(...B) + T(B[0] - 8, B[1] + 16, it('B'), 'end') + L(100, B[1], 372, B[1], 'pt') + T(104, B[1] - 6, q('E', 'p') + ' = 0', 'start', 13.5)
    + L(A0[0], A0[1], 372, A0[1], 'pt') + cote(362, A0[1], 362, B[1]) + T(356, (A0[1] + B[1]) / 2 + 5, it('h'), 'end')
    + T(200, 282, it('h') + ' = ' + it('L') + '(1 − cos ' + q('θ', '0') + ')', 'middle', 14) + T((O[0] + M[0]) / 2 - 10, (O[1] + M[1]) / 2 + 4, it('L'), 'end'),
    'Pendule simple : forces et énergie potentielle');
})();

// ---------- prisme au minimum de déviation ----------
const prismeC = (() => {
  const rad = Math.PI / 180, nI = 1.5, Ad = 60, rr = Ad / 2, i = Math.asin(nI * Math.sin(rr * rad)) / rad;
  const st = (p, s, l) => [p[0] + l * Math.cos(s * rad), p[1] + l * Math.sin(s * rad)];
  const S = [200, 34], len = 176, Lb = [S[0] - len / 2, S[1] + len * Math.cos(30 * rad)], Rb = [S[0] + len / 2, Lb[1]];
  const I = [S[0] - 100 * Math.sin(30 * rad), S[1] + 100 * Math.cos(30 * rad)], J = [S[0] + 100 * Math.sin(30 * rad), I[1]];
  const sIn = 30 - i, sOut = -30 + i, I0 = st(I, sIn + 180, 130), J1 = st(J, sOut, 130), K = [S[0], I[1] + (S[0] - I[0]) * Math.tan(sIn * rad)];
  const aS = (p, r, s1, s2) => { const [x1, y1] = st(p, s1, r), [x2, y2] = st(p, s2, r); return `<path d="M${n(x1)},${n(y1)} A${r},${r} 0 0 ${s2 > s1 ? 1 : 0} ${n(x2)},${n(y2)}" fill="none" stroke="currentColor" stroke-width="${CH.wFin}"/>`; };
  const tS = (p, r, s, t) => { const [x, y] = st(p, s, r); return T(x, y + 5, t); };
  return svg(400, 240, poly([S, Lb, Rb], 'obj', true)
    + L(...st(I, 210, 44), ...st(I, 30, 40), 'pt') + L(...st(J, -30, 44), ...st(J, 150, 40), 'pt') + L(S[0], 18, S[0], 226, 'mixte')
    + L(...I0, ...I) + mid(...I0, ...I) + L(...I, ...J) + mid(...I, ...J) + L(...J, ...J1) + mid(...J, ...J1) + L(...I, ...st(I, sIn, 160), 'pt')
    + aS(S, 26, 60, 120) + tS(S, 40, 90, it('A'))
    + aS(I, 30, sIn + 180, 210) + tS(I, 44, (sIn + 390) / 2, it('i')) + aS(I, 24, 0, 30) + tS(I, 37, 15, it('r'))
    + aS(J, 24, 150, 180) + tS(J, 37, 165, it('r') + '′') + aS(J, 30, -30, sOut) + tS(J, 44, (sOut - 30) / 2, it('i') + '′')
    + aS(K, 112, sOut, sIn) + tS(K, 128, (sIn + sOut) / 2, q('D', 'm'))
    + T(I[0] - 6, I[1] - 12, it('I'), 'end') + T(J[0] + 6, J[1] - 12, it('J'), 'start') + T(S[0], 168, it('n'), 'middle'),
    'Prisme au minimum de déviation');
})();

// ---------- résonances d'élongation et de vitesse ----------
const resoC = (() => {
  const X = Q => u => 1 / Math.sqrt((1 - u * u) ** 2 + u * u / (Q * Q)), Q = 3, ur = Math.sqrt(1 - 1 / (2 * Q * Q));
  const a = graphe(44, 30, 190, 160, [0, 2.3], [0, 3.4]), b = graphe(318, 30, 180, 160, [0, 2.3], [0, 1.15]);
  const Vn = u => u * X(Q)(u) / Q, um = (Math.sqrt(1 + 4 * Q * Q) - 1) / (2 * Q), up = (Math.sqrt(1 + 4 * Q * Q) + 1) / (2 * Q), s2 = 1 / Math.SQRT2;
  return svg(520, 250,
    a.axes('ω', it('X')) + a.courbe(X(Q), 0, 2.3) + a.courbe(X(.5), 0, 2.3, 'ptobj')
    + a.vl(ur, 'pt', 0, X(Q)(ur)) + tick(a.X(ur) - 4, a.Y(0) + 17, q('ω', 'r'), 'end') + a.vl(1, 'fin', 0, .12) + tick(a.X(1) + 4, a.Y(0) + 17, q('ω', '0'), 'start')
    + T(a.X(1.12), a.Y(3.0), it('Q') + ' = 3', 'start', 13.5) + T(a.X(1.55), a.Y(.62), it('Q') + ' = 0,5', 'start', 13.5)
    + T(139, 236, '(a) élongation : pic en ' + q('ω', 'r') + ' < ' + q('ω', '0'), 'middle', 13.5)
    + b.axes('ω', it('V') + '/' + q('V', 'max')) + b.courbe(Vn, 0, 2.3) + b.hl(s2, 'pt', 0, up) + b.hl(1, 'fin', 0, .06)
    + tick(b.X(0) - 5, b.Y(s2) + 4, '1/√2', 'end') + tick(b.X(0) - 5, b.Y(1) + 4, '1', 'end')
    + b.vl(um, 'pt', 0, s2) + b.vl(up, 'pt', 0, s2) + b.vl(1, 'pt', 0, 1) + tick(b.X(1), b.Y(0) + 17, q('ω', '0'))
    + cote(b.X(um), b.Y(.2), b.X(up), b.Y(.2)) + T(b.X(up) + 30, b.Y(.2) + 5, 'Δω = ' + q('ω', '0') + '/' + it('Q'), 'start', 13.5)
    + T(395, 236, '(b) vitesse : pic en ' + q('ω', '0'), 'middle', 13.5) + L(262, 14, 262, 220, 'pt'),
    'Résonance d’élongation et résonance de vitesse');
})();

export const LOT1 = [
  {id: 'n-p1-rc', type: 'enonce', titre: 'Charge d’un condensateur', svg: rcE},
  {id: 'n-p1-rc', type: 'correction', titre: 'Charge d’un condensateur', svg: rcC},
  {id: 'n-p1-rlc', type: 'enonce', titre: 'Régime libre du RLC série', svg: rlcE},
  {id: 'n-p1-rlc', type: 'correction', titre: 'Régime libre du RLC série', svg: rlcC},
  {id: 'n-p2-beau', type: 'correction', titre: 'Cycle de Beau de Rochas', svg: beauC},
  {id: 'n-p2-ailette', type: 'correction', titre: 'Ailette de refroidissement', svg: ailetteC},
  {id: 'n-p2-coax', type: 'correction', titre: 'Câble coaxial', svg: coaxC},
  {id: 'n-p1-pendule', type: 'correction', titre: 'Pendule simple', svg: penduleC},
  {id: 'n-p1-prisme', type: 'correction', titre: 'Minimum de déviation du prisme', svg: prismeC},
  {id: 'n-p2-resonance', type: 'correction', titre: 'Résonance d’élongation et Q', svg: resoC},
];
