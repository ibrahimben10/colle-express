// Lot 6 : ondes mécaniques, optique, physique statistique, rayonnement.
import { CH, svg, L, P, poly, C, Ell, Rect, hatch, hatchRect, aire, paroi, vec, axe, fl, mid, cote, it, sub, sup, q, T, tick, V, pt, ptO,
  sortant, entrant, pol, arc, Ta, graphe } from './kit.js';

const n = v => Math.round(v * 10) / 10;
const small = 13.5, sep = (x, y1, y2) => L(x, y1, x, y2, 'pt');
const rad = Math.PI / 180;
const st = (p, s, l) => [p[0] + l * Math.cos(s * rad), p[1] + l * Math.sin(s * rad)];
const aS = (p, r, s1, s2) => { const [x1, y1] = st(p, s1, r), [x2, y2] = st(p, s2, r); return `<path d="M${n(x1)},${n(y1)} A${r},${r} 0 0 ${s2 > s1 ? 1 : 0} ${n(x2)},${n(y2)}" fill="none" stroke="currentColor" stroke-width="${CH.wFin}"/>`; };
// Lentille mince convergente (double flèche) ou divergente.
const lentille = (x, y, h) => L(x, y - h / 2, x, y + h / 2) + `<path d="M${x - 5},${y - h / 2 + 7} L${x},${y - h / 2} L${x + 5},${y - h / 2 + 7} M${x - 5},${y + h / 2 - 7} L${x},${y + h / 2} L${x + 5},${y + h / 2 - 7}" fill="none" stroke="currentColor" stroke-width="${CH.wObj}"/>`;
const ecran = (x, y1, y2) => hatchRect(x, y1, 7, y2 - y1) + L(x, y1, x, y2, 'epais');

// ---------- interférences ultrasonores ----------
const ultraE = svg(380, 232, pt(60, 140) + T(50, 145, q('S', '1'), 'end') + pt(60, 90) + T(50, 95, q('S', '2'), 'end') + L(320, 14, 320, 208, 'epais')
  + pt(320, 60) + T(330, 64, it('M'), 'start') + L(60, 140, 320, 60, 'pt') + L(60, 90, 320, 60, 'pt') + T(170, 96, q('d', '1'), 'middle', small) + T(196, 70, q('d', '2'), 'middle', small)
  + L(60, 115, 320, 115, 'mixte') + pt(320, 115) + tick(330, 120, '0', 'start') + axe(344, 115, 344, 62) + T(352, 74, it('x'), 'start')
  + cote(34, 90, 34, 140) + T(26, 120, it('a'), 'end') + cote(60, 222, 320, 222) + T(190, 216, it('D')), 'Deux émetteurs et une droite de mesure');
const ultraC = (() => {
  const S1 = [40, 150], S2 = [40, 100], M = [240, 40], u = [M[0] - S1[0], M[1] - S1[1]], l = Math.hypot(...u), e = [u[0] / l, u[1] / l];
  const d2 = Math.hypot(M[0] - S2[0], M[1] - S2[1]), H = [M[0] - d2 * e[0], M[1] - d2 * e[1]];
  const a = pt(...S1) + T(30, 155, q('S', '1'), 'end') + pt(...S2) + T(30, 105, q('S', '2'), 'end') + pt(...M) + T(248, 44, it('M'), 'start') + L(240, 14, 240, 200, 'epais')
    + L(...S1, ...M, 'fin') + L(...S2, ...M, 'fin') + L(...S2, ...H, 'pt') + L(...S1, ...H, 'epais') + T(H[0] - 2, H[1] + 22, 'δ', 'middle') + T(H[0] + 8, H[1] - 6, it('H'), 'start')
    + T(140, 220, '(a) δ = ' + q('S', '1') + it('M') + ' − ' + q('S', '2') + it('M') + ' ≈ ' + it('ax') + '/' + it('D'), 'middle', 12.5);
  const i0 = .17, g = graphe(300, 30, 200, 150, [-.42, .42], [0, 1.15]);
  const b = g.axes(it('x'), 'amplitude', 0, 0) + g.courbe(x => Math.abs(Math.cos(Math.PI * x / i0)), -.42, .42, 'obj', 300)
    + [-2, -1, 0, 1, 2].map(k => tick(g.X(k * i0), g.Y(1) - 6, String(k))).join('')
    + cote(g.X(0), g.Y(0) + 14, g.X(i0), g.Y(0) + 14) + T(g.X(i0) + 6, g.Y(0) + 18, it('i'), 'start', 12.5)
    + T(400, 220, '(b) maxima (' + it('p') + ') : δ = ' + it('p') + 'λ', 'middle', 12.5);
  return svg(520, 230, a + sep(272, 14, 206) + b, 'Interférences : différence de marche et maxima');
})();

// ---------- lunette ----------
const lunetteE = svg(420, 180, L(10, 90, 410, 90, 'mixte') + lentille(60, 90, 116) + lentille(300, 90, 70) + T(60, 24, q('L', '1')) + T(300, 48, q('L', '2'))
  + pt(240, 90) + T(236, 108, q('F', '1') + '′ = ' + q('F', '2'), 'end', small) + pt(360, 90) + T(360, 108, q('F', '2') + '′', 'middle', small)
  + cote(60, 150, 240, 150) + T(150, 166, q('f', '1') + '′') + cote(240, 150, 300, 150) + T(270, 166, q('f', '2') + '′')
  + vec(10, 46, 58, 51) + vec(10, 98, 58, 103) + T(16, 38, 'α', 'start') + T(412, 24, '(échelle non respectée)', 'end', 12),
  'Lunette afocale : objectif, oculaire et foyers');
const lunetteC = (() => {
  const y0 = 90, x1 = 40, xF = 240, x2 = 300, ta = Math.tan(6 * rad), yi = y0 + (xF - x1) * ta;
  let b = '';
  for (const h of [-36, 0, 36]) {
    const yL1 = y0 + h, yL2 = yi + (yi - yL1) * (x2 - xF) / (xF - x1), sl = (y0 - yi) / (x2 - xF);
    b += L(0, yL1 - x1 * ta, x1, yL1) + mid(0, yL1 - x1 * ta, x1, yL1, .5) + L(x1, yL1, x2, yL2) + L(x2, yL2, 380, yL2 + sl * 80) + mid(x2, yL2, 380, yL2 + sl * 80, .5);
  }
  return svg(400, 196, L(0, y0, 400, y0, 'mixte') + b + lentille(x1, y0, 100) + lentille(x2, y0, 96) + L(xF, y0, xF, yi, 'epais') + pt(xF, yi)
    + T(x1, 30, q('L', '1')) + T(x2, 34, q('L', '2')) + T(xF - 4, y0 - 8, q('F', '1') + '′ = ' + q('F', '2'), 'end', 12.5) + T(xF + 6, yi + 18, it('A') + '′' + it('B') + '′', 'start', 12.5)
    + T(14, 58, 'α') + T(392, 48, 'α′', 'end') + T(200, 188, 'image intermédiaire dans le plan focal commun (échelle non respectée)', 'middle', 12),
    'Lunette afocale : marche d’un faisceau parallèle');
})();

// ---------- prisme (énoncé) ----------
const prismeE = (() => {
  const nI = 1.5, Ad = 60, i = 50, r = Math.asin(Math.sin(i * rad) / nI) / rad, rp = Ad - r, ip = Math.asin(nI * Math.sin(rp * rad)) / rad;
  const S = [200, 30], len = 176, Lb = [S[0] - len / 2, S[1] + len * Math.cos(30 * rad)], Rb = [S[0] + len / 2, Lb[1]];
  const I = [S[0] - 118 * Math.sin(30 * rad), S[1] + 118 * Math.cos(30 * rad)], sIn = 30 - i, sInt = 30 - r, u = [Math.cos(sInt * rad), Math.sin(sInt * rad)], f = [Math.sin(30 * rad), Math.cos(30 * rad)];
  const det = u[0] * (-f[1]) - u[1] * (-f[0]), t1 = ((S[0] - I[0]) * (-f[1]) - (S[1] - I[1]) * (-f[0])) / det, J = [I[0] + t1 * u[0], I[1] + t1 * u[1]], sOut = -30 + ip;
  const I0 = st(I, sIn + 180, 120), J1 = st(J, sOut, 120), lab = (p, rr, s, t) => { const [x, y] = st(p, s, rr); return T(x, y + 5, t); };
  return svg(400, 230, poly([S, Lb, Rb], 'obj', true) + L(...st(I, 210, 44), ...st(I, 30, 40), 'pt') + L(...st(J, -30, 44), ...st(J, 150, 40), 'pt')
    + L(...I0, ...I) + mid(...I0, ...I) + L(...I, ...J) + mid(...I, ...J) + L(...J, ...J1) + mid(...J, ...J1)
    + aS(S, 24, 60, 120) + lab(S, 38, 90, it('A')) + aS(I, 30, sIn + 180, 210) + lab(I, 44, (sIn + 390) / 2, it('i')) + aS(I, 26, sInt, 30) + lab(I, 40, (sInt + 30) / 2, it('r'))
    + aS(J, 26, 150, sInt + 180) + lab(J, 40, (150 + sInt + 180) / 2, it('r') + '′') + aS(J, 30, -30, sOut) + lab(J, 44, (sOut - 30) / 2, it('i') + '′')
    + T(I[0] - 6, I[1] - 10, it('I'), 'end') + T(J[0] + 6, J[1] - 10, it('J'), 'start') + T(200, 168, it('n'), 'middle'), 'Prisme : angles d’incidence, de réfraction et d’émergence');
})();

// ---------- projecteur ----------
const projE = svg(420, 180, L(10, 100, 410, 100, 'mixte') + C(36, 100, 13) + L(27, 91, 45, 109, 'fin') + L(27, 109, 45, 91, 'fin') + T(36, 134, 'lampe', 'middle', 12)
  + Rect(84, 78, 5, 44) + T(86, 70, 'diapositive', 'middle', 12) + lentille(130, 100, 100) + T(130, 40, it('L') + ' (' + it('f') + '′)')
  + pt(160, 100) + T(160, 116, it('F') + '′', 'middle', small) + pt(100, 100) + T(102, 116, it('F'), 'middle', small)
  + L(220, 92, 226, 108, 'fin') + L(226, 92, 232, 108, 'fin') + ecran(380, 24, 176) + T(383, 18, 'écran', 'middle', 12) + cote(130, 160, 380, 160) + T(255, 154, '3,0 m'),
  'Projecteur : lampe, diapositive, lentille, écran');
const projC = svg(420, 216, L(10, 130, 410, 130, 'mixte') + lentille(110, 130, 80)
  + vec(60, 130, 60, 154) + T(52, 166, it('B'), 'end') + T(56, 122, it('A'), 'end')
  + L(60, 154, 110, 154) + mid(60, 154, 110, 154) + L(110, 154, 310, 34) + mid(110, 154, 310, 34, .7) + L(60, 154, 310, 34) + mid(60, 154, 310, 34, .7)
  + ecran(310, 20, 190) + vec(304, 130, 304, 36) + T(298, 60, it('B') + '′', 'end') + T(298, 146, it('A') + '′', 'end')
  + pt(70, 130) + T(70, 146, it('F'), 'middle', small) + pt(150, 130) + T(150, 146, it('F') + '′', 'middle', small) + pt(110, 130) + T(118, 146, it('O'), 'start')
  + T(372, 64, '1/' + it('OA') + '′ − 1/' + it('OA'), 'middle', 12.5) + T(372, 82, '= 1/' + it('f') + '′', 'middle', 12.5) + T(372, 112, 'γ = ' + it('OA') + '′/' + it('OA'), 'middle', 12.5)
  + T(200, 208, '(échelle non respectée)', 'middle', 12), 'Projecteur : construction de l’image');

// ---------- diffraction par une fente ----------
const fenteE = svg(400, 212, Rect(10, 88, 50, 24) + T(35, 82, 'laser', 'middle', 12) + vec(60, 100, 124, 100) + T(92, 92, 'λ')
  + L(132, 16, 132, 93, 'epais') + L(132, 107, 132, 184, 'epais') + hatchRect(124, 16, 8, 77) + hatchRect(124, 107, 8, 77) + T(144, 128, it('a'), 'start')
  + L(132, 100, 340, 100, 'mixte') + ecran(340, 16, 184) + cote(132, 200, 340, 200) + T(236, 194, it('D')), 'Fente de largeur a éclairée par un laser');
const fenteC = (() => {
  const a = L(30, 16, 30, 93, 'epais') + L(30, 107, 30, 184, 'epais') + L(30, 100, 230, 100, 'mixte') + L(30, 100, 230, 64, 'fin') + L(30, 100, 230, 136, 'fin') + ecran(230, 16, 184)
    + aS([30, 100], 120, 0, -10.2) + T(160, 92, 'θ', 'start') + cote(252, 64, 252, 136) + T(258, 104, it('ℓ'), 'start')
    + T(130, 214, '(a) sin θ = λ/' + it('a') + ', ℓ ≈ 2λ' + it('D') + '/' + it('a'), 'middle', 12.5);
  const g = graphe(300, 30, 200, 150, [-3.3, 3.3], [0, 1.12]), s = u => u === 0 ? 1 : (Math.sin(Math.PI * u) / (Math.PI * u)) ** 2;
  const b = g.axes(it('X'), it('I'), 0, 0) + g.courbe(s, -3.3, 3.3, 'obj', 400) + tick(g.X(-1), g.Y(0) + 15, '−λ' + it('D') + '/' + it('a')) + tick(g.X(1), g.Y(0) + 15, 'λ' + it('D') + '/' + it('a'))
    + T(400, 214, '(b) éclairement sur l’écran', 'middle', 12.5);
  return svg(520, 226, a + sep(276, 14, 200) + b, 'Diffraction par une fente : premiers minima et tache centrale');
})();

// ---------- corde ----------
const cordeC = (() => {
  const y = x => 120 - 46 * Math.sin(Math.PI * (x - 20) / 220), x1 = 90, x2 = 140;
  const tg = x => { const h = .5; return Math.atan2(y(x + h) - y(x - h), 2 * h); };
  const a = poly(Array.from({length: 111}, (_, i) => [20 + 2 * i, y(20 + 2 * i)])) + L(10, 120, 250, 120, 'mixte') + pt(20, 120) + pt(240, 120)
    + vec(x1, y(x1), x1 - 52 * Math.cos(tg(x1)), y(x1) - 52 * Math.sin(tg(x1))) + V(x1 - 58, y(x1) + 4, 'T', '', 'end')
    + vec(x2, y(x2), x2 + 52 * Math.cos(tg(x2)), y(x2) + 52 * Math.sin(tg(x2))) + V(x2 + 50, y(x2) - 6, 'T', '′', 'start')
    + L(x1, y(x1), x1, 120, 'pt') + L(x2, y(x2), x2, 120, 'pt') + tick(x1, 138, it('x')) + tick(x2, 138, it('x') + ' + d' + it('x')) + T(x1 + 6, (y(x1) + 120) / 2 + 4, it('y'), 'start', 12.5)
    + T(130, 214, '(a) élément de corde', 'middle', 12.5);
  const x0 = 290, x3 = 500, row = (k, yy) => poly(Array.from({length: 101}, (_, i) => [x0 + (x3 - x0) * i / 100, yy - 14 * Math.sin(k * Math.PI * i / 100)])) + poly(Array.from({length: 101}, (_, i) => [x0 + (x3 - x0) * i / 100, yy + 14 * Math.sin(k * Math.PI * i / 100)]), 'pt')
    + Array.from({length: k + 1}, (_, j) => pt(x0 + j * (x3 - x0) / k, yy)).join('') + T(x3 + 10, yy + 4, it('n') + ' = ' + k, 'start', 12.5);
  const b = row(1, 40) + row(2, 100) + row(3, 160) + T(400, 214, '(b) modes propres, ' + q('f', 'n', true) + ' = ' + it('n') + q('f', '1'), 'middle', 12.5);
  return svg(550, 226, a + sep(266, 14, 200) + b, 'Corde : élément dx et modes propres');
})();

// ---------- doublet du sodium ----------
const doubletC = (() => {
  const a = graphe(40, 26, 200, 150, [0, 2.2], [0, 2.15]), b = graphe(300, 26, 200, 150, [0, 2.2], [0, 1.15]);
  return svg(530, 226, a.axes('δ', 'ℰ', 0, 0) + a.courbe(d => 1 + Math.cos(Math.PI * d) * Math.cos(2 * Math.PI * 14 * d), 0, 2.2, 'fin', 900)
    + a.courbe(d => 1 + Math.abs(Math.cos(Math.PI * d)), 0, 2.2, 'pt') + a.courbe(d => 1 - Math.abs(Math.cos(Math.PI * d)), 0, 2.2, 'pt')
    + T(140, 214, '(a) éclairement au centre (franges schématiques)', 'middle', 12) + sep(266, 14, 200)
    + b.axes('δ', it('V'), 0, 0) + b.courbe(d => Math.abs(Math.cos(Math.PI * d)), 0, 2.2) + tick(b.X(.5), b.Y(0) + 15, 'λ' + q('', 'm') + sup('2') + '/(2Δλ)') + tick(b.X(1.5), b.Y(0) + 15, '3λ' + q('', 'm') + sup('2') + '/(2Δλ)')
    + T(400, 214, '(b) contraste |cos(πΔλδ/λ' + q('', 'm') + sup('2') + ')|', 'middle', 12), 'Doublet du sodium : battements et contraste');
})();

// ---------- réseau ----------
const reseauC = (() => {
  let a = ''; for (let y = 30; y <= 170; y += 8) a += L(70, y, 70, y + 4, 'epais');
  a += [60, 90, 120].map(y => vec(14, y, 66, y)).join('') + L(70, 100, 230, 100, 'mixte');
  for (const [p, ang] of [[1, 17], [2, 36], [-1, -17], [-2, -36]]) { const e = st([70, 100], -ang, 150); a += vec(72, 100, ...e) + T(e[0] + 6, e[1] + 4, it('p') + ' = ' + p, 'start', 12); }
  a += T(240, 104, it('p') + ' = 0', 'start', 12) + aS([70, 100], 90, -17, 0) + T(168, 88, q('θ', '1'), 'start', 12) + T(130, 214, '(a) ' + it('a') + ' sin ' + q('θ', 'p', true) + ' = ' + it('p') + 'λ', 'middle', 12.5);
  const X0 = 320, W = 190, sx = v => X0 + v * W;
  let b = '';
  for (const [p, y] of [[1, 40], [2, 80], [3, 120]]) { const lo = p * .2, hi = Math.min(p * .35, 1); b += Rect(sx(lo), y, sx(hi) - sx(lo), 16) + `<rect x="${n(sx(lo))}" y="${y}" width="${n(sx(hi) - sx(lo))}" height="16" fill="url(#an-h2)"/>` + tick(X0 - 8, y + 12, it('p') + ' = ' + p, 'end'); }
  b += Rect(sx(.6), 32, sx(.7) - sx(.6), 108, 'pt') + tick(sx(.65), 26, 'recouvrement') + axe(X0, 160, X0 + W + 14, 160) + T(X0 + W + 14, 178, 'sin θ', 'end')
    + [0, .5, 1].map(v => L(sx(v), 156, sx(v), 164, 'fin') + tick(sx(v), 178, String(v).replace('.', ','))).join('') + T(415, 214, '(b) spectres 400–700 nm, ' + it('a') + ' = 2 µm', 'middle', 12.5);
  return svg(540, 226, a + sep(282, 14, 200) + b, 'Réseau : ordres et recouvrement des spectres');
})();

// ---------- profil gaussien ----------
const opt8C = (() => {
  const a = graphe(40, 30, 190, 150, [-3, 3], [0, 1.15]), w = Math.sqrt(Math.log(2));
  const b = graphe(300, 30, 200, 150, [0, 2.6], [0, 2.15]);
  return svg(530, 226, a.axes('σ', '𝒟', 0, 0) + a.courbe(x => Math.exp(-x * x), -3, 3) + a.hl(.5, 'pt', -w, w) + cote(a.X(-1), a.Y(Math.exp(-1)), a.X(1), a.Y(Math.exp(-1)))
    + T(a.X(1.1), a.Y(Math.exp(-1)) + 4, '2' + it('b'), 'start', 12.5) + tick(a.X(0), a.Y(0) + 15, q('σ', '0')) + T(a.X(1.1), a.Y(.62), '½', 'start', 12)
    + T(135, 214, '(a) densité spectrale autour de ' + q('σ', '0'), 'middle', 12.5) + sep(262, 14, 200)
    + b.axes(it('t'), it('I'), 0, 0) + b.courbe(t => 1 + Math.exp(-t * t) * Math.cos(2 * Math.PI * 7 * t), 0, 2.6, 'fin', 800) + b.courbe(t => 1 + Math.exp(-t * t), 0, 2.6, 'pt') + b.courbe(t => 1 - Math.exp(-t * t), 0, 2.6, 'pt')
    + b.vl(1, 'pt', 0, 2) + tick(b.X(1), b.Y(0) + 15, 'τ') + cote(b.X(2 / 7), b.Y(2.08), b.X(3 / 7), b.Y(2.08)) + tick(b.X(3 / 7) + 6, b.Y(2.08) + 4, q('T', '0'), 'start')
    + T(400, 214, '(b) interférogramme ' + it('I') + '(' + it('t') + ')', 'middle', 12.5), 'Profil gaussien : spectre et interférogramme');
})();

// ---------- paramagnétisme ----------
const stat1C = (() => {
  const g = graphe(300, 30, 190, 150, [0, 3], [0, 1.15]);
  return svg(520, 220, L(40, 60, 190, 60, 'epais') + L(40, 150, 190, 150, 'epais') + T(196, 64, '+' + q('ε', '0'), 'start') + T(196, 154, '−' + q('ε', '0'), 'start')
    + vec(115, 54, 115, 28) + T(125, 40, q('p', '−'), 'start', 12.5) + [80, 115, 150].map(x => vec(x, 156, x, 182)).join('') + T(160, 178, q('p', '+'), 'start', 12.5)
    + cote(232, 60, 232, 150) + T(238, 110, 'Δε = 2' + q('ε', '0'), 'start', 12) + vec(20, 80, 20, 130) + V(28, 116, 'B', '', 'start')
    + T(120, 210, 'μ ∥ ' + it('B') + ' : niveau bas, plus peuplé', 'middle', 12) + sep(282, 14, 200)
    + g.axes(q('μ', '0') + it('B') + '/' + q('k', 'B') + it('T'), '⟨μ⟩/' + q('μ', '0')) + g.hl(1, 'pt') + g.courbe(Math.tanh, 0, 3) + L(g.X(0), g.Y(0), g.X(1.05), g.Y(1.05), 'fin') + T(g.X(.95), g.Y(.45), 'Curie', 'start', 12),
    'Paramagnétisme : deux niveaux et aimantation moyenne');
})();

// ---------- élasticité entropique ----------
function chaine(x0, y, seq) {
  let x = x0, s = paroi(x0, y - 26, x0, y + 26, 1);
  for (const k of seq) { const w = k ? 40 : 24; s += Rect(x, y - 7, w, 14) + pt(x + w, y, 2); x += w; }
  return [s, x];
}
const seq = [1, 0, 1, 1, 0, 1, 0, 0, 1];
const stat3E = (() => {
  const [s, x] = chaine(30, 70, seq);
  return svg(400, 150, s + vec(x, 70, x + 46, 70) + V(x + 30, 60, 'f') + T(50, 52, it('ℓ') + ' + ' + it('a'), 'middle', 12.5) + T(82, 98, it('ℓ') + ' − ' + it('a'), 'middle', 12.5)
    + cote(30, 124, x, 124) + T((30 + x) / 2, 142, '𝓛'), 'Fibre : chaîne de maillons courts ou longs');
})();
const stat3C = (() => {
  const [s, x] = chaine(20, 70, seq), g = graphe(310, 26, 190, 150, [-3, 3], [-1.25, 1.25]);
  return svg(530, 222, s + vec(x, 70, x + 40, 70) + V(x + 26, 60, 'f') + cote(20, 110, x, 110) + T((20 + x) / 2, 128, '𝓛') + T(140, 160, 'les maillons longs sont favorisés', 'middle', 12) + T(140, 178, 'quand ' + it('f') + ' > 0', 'middle', 12)
    + sep(280, 14, 200) + g.axes(it('f'), '𝓛 − ' + q('𝓛', '0'), 0, 0) + g.hl(1, 'pt') + g.hl(-1, 'pt') + g.courbe(Math.tanh, -3, 3) + L(g.X(-1.1), g.Y(-1.1), g.X(1.1), g.Y(1.1), 'fin')
    + tick(g.X(-3), g.Y(1) - 5, it('Na'), 'start') + tick(g.X(3), g.Y(-1) + 15, '−' + it('Na'), 'end') + T(g.X(.9), g.Y(.35), 'Hooke', 'start', 12),
    'Fibre : traction et allongement');
})();

// ---------- effet de serre ----------
const serreC = svg(440, 230, hatchRect(0, 196, 440, 34) + L(0, 196, 440, 196, 'epais') + T(430, 190, 'sol, ' + q('T', 's'), 'end', small)
  + L(0, 90, 440, 90) + L(0, 108, 440, 108) + T(430, 84, 'atmosphère, ' + q('T', 'a'), 'end', small)
  + vec(60, 20, 60, 192) + T(68, 40, '(1 − ' + it('A') + ')' + q('φ', 'S') + '/4', 'start', 12.5) + T(68, 150, 'visible', 'start', 12)
  + vec(160, 194, 160, 110) + T(168, 160, 'σ' + q('T', 's') + sup('4'), 'start', small) + vec(240, 88, 240, 18) + T(248, 40, 'σ' + q('T', 'a') + sup('4'), 'start', small)
  + vec(300, 110, 300, 192) + T(308, 160, 'σ' + q('T', 'a') + sup('4'), 'start', small) + T(160, 124, 'infrarouge', 'start', 12),
  'Effet de serre : bilan radiatif à une couche');

// ---------- Planck, Wien, Stefan ----------
const spe3C = (() => {
  const Dn = Tk => l => l ** -5 / (Math.exp(14388 / (l * Tk)) - 1), ref = Dn(6000)(2898 / 6000), g = graphe(40, 26, 210, 150, [0, 2.5], [0, 1.1]);
  const h = graphe(320, 26, 180, 150, [0, 1.3], [0, 1.25]);
  let loc = ''; for (let Tk = 3600; Tk <= 6200; Tk += 50) loc += (loc ? ' L' : 'M') + n(g.X(2898 / Tk)) + ',' + n(g.Y(Dn(Tk)(2898 / Tk) / ref));
  return svg(540, 226, g.axes('λ', '𝒟') + [[6000, 'obj'], [5000, 'ptobj'], [4000, 'fin']].map(([Tk, k]) => g.courbe(l => Dn(Tk)(l) / ref, .1, 2.5, k)).join('') + P(loc, 'pt')
    + T(g.X(.62), g.Y(1.02), '6 000 K', 'start', 12) + T(g.X(.72), g.Y(.44), '5 000 K', 'start', 12) + T(g.X(.95), g.Y(.2), '4 000 K', 'start', 12)
    + T(145, 214, '(a) Wien : ' + q('λ', 'max') + it('T') + ' = cste', 'middle', 12.5) + sep(282, 14, 200)
    + h.axes(it('T'), q('𝒫', 'S')) + h.courbe(t => t ** 4, 0, 1.3) + T(h.X(.75), h.Y(.75), '∝ ' + it('T') + sup('4'), 'end', 12.5) + T(410, 214, '(b) Stefan : ' + q('𝒫', 'S') + ' = σ' + it('T') + sup('4'), 'middle', 12.5),
    'Corps noir : déplacement du maximum et loi de Stefan');
})();

// ---------- gaz de photons ----------
const spe4C = svg(460, 220, L(60, 30, 60, 170, 'epais') + hatchRect(50, 30, 10, 140) + L(260, 30, 260, 170, 'epais') + hatchRect(260, 30, 10, 140) + L(300, 30, 300, 170, 'ptobj')
  + `<rect x="214" y="31" width="46" height="138" fill="url(#an-h2)"/>` + cote(214, 186, 260, 186) + T(237, 202, it('c') + ' d' + it('t'), 'middle', 12.5)
  + [[90, 60, 1], [150, 90, -1], [110, 130, 1], [180, 150, -1], [222, 70, 1], [230, 120, 1], [200, 50, -1]].map(([x, y, s]) => vec(x, y, x + s * 26, y)).join('')
  + vec(276, 100, 326, 100) + T(330, 92, '2' + it('hf') + '/' + it('c'), 'start', 12.5) + fl(270, 186, 300, 186) + T(306, 190, 'd' + it('a') + ' (détente)', 'start', 12.5)
  + cote(60, 16, 260, 16) + T(160, 12, it('a')) + axe(380, 140, 420, 140) + V(430, 146, 'u', 'x', 'start'),
  'Gaz de photons : pression de radiation et détente');

export const LOT6 = [
  {id: 'n-p1-ultrasons', type: 'enonce', titre: 'Interférences ultrasonores', legende: 'Émetteurs S₁ et S₂ distants de a ; récepteur M sur une droite parallèle à S₁S₂, à la distance D, repéré par x ; d₁ = S₁M, d₂ = S₂M', svg: ultraE},
  {id: 'n-p1-ultrasons', type: 'correction', titre: 'Interférences ultrasonores', legende: '(a) La différence de marche δ = S₁M − S₂M ≈ ax/D. (b) Maxima d’amplitude pour δ = pλ, séparés de i = λD/a ≈ 17 cm', svg: ultraC},
  {id: 'n-p1-lunette', type: 'enonce', titre: 'Lunette astronomique', legende: 'Objectif L₁ (f′₁) et oculaire L₂ (f′₂) sur le même axe, avec F′₁ = F₂ ; objet à l’infini vu sous l’angle α', svg: lunetteE},
  {id: 'n-p1-lunette', type: 'correction', titre: 'Lunette astronomique', legende: 'Un faisceau incliné de α converge en A′B′ dans le plan focal commun, puis ressort parallèle, incliné de α′ : G = α′/α = −f′₁/f′₂', svg: lunetteC},
  {id: 'n-p1-prisme', type: 'enonce', titre: 'Prisme', legende: 'Prisme d’angle A et d’indice n : incidence i en I, réfractions r et r′, émergence i′ en J (normales en pointillé)', svg: prismeE},
  {id: 'n-p1-projecteur', type: 'enonce', titre: 'Projecteur de diapositives', legende: 'Lampe, diapositive au voisinage du foyer F, lentille convergente de focale f′, écran à 3,0 m de la lentille', svg: projE},
  {id: 'n-p1-projecteur', type: 'correction', titre: 'Projecteur de diapositives', legende: 'Rayon parallèle à l’axe (ressort par F′) et rayon par O : l’image est renversée et agrandie, d’où la diapositive placée à l’envers ; conjugaison de Descartes et γ = OA′/OA', svg: projC},
  {id: 'n-p1-fente', type: 'enonce', titre: 'Diffraction par une fente', legende: 'Laser de longueur d’onde λ éclairant une fente de largeur a ; écran à la distance D', svg: fenteE},
  {id: 'n-p1-fente', type: 'correction', titre: 'Diffraction par une fente', legende: '(a) Premiers minima dans les directions sin θ = λ/a ; tache centrale de largeur ℓ ≈ 2λD/a. (b) Éclairement en sinc²', svg: fenteC},
  {id: 'n-p1-corde', type: 'correction', titre: 'Corde de guitare', legende: '(a) Élément [x, x + dx] soumis aux tensions de ses voisins, tangentes à la corde. (b) Modes propres fₙ = nf₁, nœuds aux extrémités et tous les L/n', svg: cordeC},
  {id: 'n-p2-doublet', type: 'correction', titre: 'Michelson et doublet du sodium', legende: '(a) Franges modulées par le battement des deux raies. (b) Contraste |cos(πΔλδ/λ²ₘ)|, nul pour δ = λ²ₘ/(2Δλ) : brouillage', svg: doubletC},
  {id: 'n-p2-reseau', type: 'correction', titre: 'Réseau', legende: '(a) Maxima principaux dans les directions a sin θ_p = pλ. (b) Sur l’échelle sin θ, les spectres d’ordres 2 et 3 se recouvrent (0,6 à 0,7), pas ceux d’ordres 1 et 2', svg: reseauC},
  {id: 'p-opt-8', type: 'correction', titre: 'Profil spectral gaussien', legende: '(a) Densité spectrale gaussienne de centre σ₀ et de largeur caractéristique b. (b) Franges de période T₀ = λ₀/(2V₀) sous une enveloppe gaussienne de durée τ = 1/(2πbV₀)', svg: opt8C},
  {id: 'p-stat-1', type: 'correction', titre: 'Paramagnétisme à deux niveaux', legende: 'Niveaux −ε₀ (moment parallèle à B, plus peuplé) et +ε₀ ; ⟨μ⟩ = μ₀ th(μ₀B/k_BT), linéaire à haute température (loi de Curie)', svg: stat1C},
  {id: 'p-stat-3', type: 'enonce', titre: 'Élasticité entropique', legende: 'Fibre de N maillons, chacun court (ℓ − a) ou long (ℓ + a), de longueur totale 𝓛, tirée par la force f', svg: stat3E},
  {id: 'p-stat-3', type: 'correction', titre: 'Élasticité entropique', legende: 'La traction favorise les maillons longs : 𝓛 = 𝓛₀ + Na th(af/k_BT), loi de Hooke aux faibles forces et saturation à 𝓛₀ ± Na', svg: stat3C},
  {id: 'n-p2-serre', type: 'correction', titre: 'Effet de serre', legende: 'Le visible traverse l’atmosphère ; elle absorbe l’infrarouge du sol et rayonne σT_a⁴ vers l’espace et vers le sol, d’où T_s = 2^(1/4)T_a ≈ 303 K', svg: serreC},
  {id: 'p-th-spe3', type: 'correction', titre: 'De Planck à Wien et Stefan', legende: '(a) Densité spectrale à 4 000, 5 000 et 6 000 K ; le maximum se déplace selon λ_max T = 2,90 × 10⁻³ m K. (b) Puissance surfacique émise en T⁴', svg: spe3C},
  {id: 'p-th-spe4', type: 'correction', titre: 'Gaz de photons', legende: 'Modèle 1D : les photons qui frappent le miroir pendant dt sont dans la tranche c dt ; chacun lui cède 2hf/c, d’où P = u/3 ; lors d’une détente lente (da), TV^(1/3) reste constant', svg: spe4C},
];
