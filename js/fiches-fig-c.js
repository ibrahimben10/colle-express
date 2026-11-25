// Schémas des fiches de cours — Chimie MPSI.
import { svg, L, A, D, T, I, V, C, R, P, dot, sb } from './figkit.js';
import { axes, courbe, res, fil } from './fiches-kit.js';

const r2 = n => Math.round(n * 100) / 100;
const rad = d => d * Math.PI / 180;
const pol = (x, y, r, deg) => [r2(x + r * Math.cos(rad(deg))), r2(y - r * Math.sin(rad(deg)))];
const sup = (b, s) => `${b}<tspan baseline-shift="super" font-size="10">${s}</tspan>`;
// perspective cavalière : (x, y, z) ∈ [0,1]³ → écran
const pj = (ox, oy, s) => (x, y, z) => [r2(ox + s * x + 0.42 * s * y), r2(oy - s * z - 0.3 * s * y)];
const cube = (p, c = '') => {
  const E = [[[0, 0, 0], [1, 0, 0]], [[0, 0, 0], [0, 0, 1]], [[1, 0, 0], [1, 0, 1]], [[0, 0, 1], [1, 0, 1]], [[0, 1, 1], [1, 1, 1]], [[1, 1, 0], [1, 1, 1]], [[0, 0, 1], [0, 1, 1]], [[1, 0, 1], [1, 1, 1]], [[1, 0, 0], [1, 1, 0]]];
  const H = [[[0, 0, 0], [0, 1, 0]], [[0, 1, 0], [1, 1, 0]], [[0, 1, 0], [0, 1, 1]]];   // arêtes cachées
  return E.map(([a, b]) => L(...p(...a), ...p(...b), c)).join('') + H.map(([a, b]) => L(...p(...a), ...p(...b), 'dash soft')).join('');
};
const at = (p, q, r, c = 'fillA') => C(...p(...q), r, c);
const corners = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0], [0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]];
const faces = [[0.5, 0.5, 0], [0.5, 0.5, 1], [0.5, 0, 0.5], [0.5, 1, 0.5], [0, 0.5, 0.5], [1, 0.5, 0.5]];
const depth = q => -q[1];      // les atomes du fond d’abord
const atoms = (p, list, r, c) => list.slice().sort((a, b) => depth(a) - depth(b) || 0).map(q => at(p, q, r, c)).join('');
const eau = (x, y, deg, s = 1) => { const [h1x, h1y] = pol(x, y, 15 * s, deg + 52), [h2x, h2y] = pol(x, y, 15 * s, deg - 52); return L(x, y, h1x, h1y) + L(x, y, h2x, h2y) + C(h1x, h1y, 5 * s, 'fillW') + C(h2x, h2y, 5 * s, 'fillW') + C(x, y, 8 * s, 'fillR'); };

export const FIGS = {
// ---------- transformation de la matière ----------
'c-matiere-1': ['Diagramme (P, T) d’un corps pur : trois domaines séparés par les courbes d’équilibre, point triple T et point critique C. Pour l’eau, la frontière solide-liquide a une pente négative', svg(440, 220, (() => {
  const pan = (x0, eau) => `${axes(x0, 190, 190, 0, 175, 0, I('T'), I('P'))}
    <path d="M${x0 + 20},180 C${x0 + 50},170 ${x0 + 70},150 ${x0 + 80},130" class="s"/><path d="M${x0 + 80},130 C${x0 + 110},110 ${x0 + 140},80 ${x0 + 165},55" class="s"/>
    <path d="M${x0 + 80},130 L${x0 + (eau ? 68 : 100)},20" class="s"/>${dot(x0 + 80, 130)}${dot(x0 + 165, 55)}${T(x0 + 90, 142, I('T'), '', 'start')}${T(x0 + 170, 52, I('C'), '', 'start')}
    ${T(x0 + 35, 80, 'solide', 'nt')}${T(x0 + 130, 60, 'liquide', 'nt')}${T(x0 + 140, 160, 'gaz', 'nt')}`;
  return pan(20, false) + T(115, 214, 'cas général', 'nt') + pan(240, true) + T(335, 214, 'eau', 'nt');
})(), 'Diagramme (P,T)')],

// ---------- classification ----------
'c-classification-1': ['Classification périodique simplifiée : blocs s, p, d et f ; familles des alcalins (colonne 1), des halogènes (17) et des gaz nobles (18)', svg(440, 270, (() => {
  const w = 22, h = 20, x0 = 20, y0 = 20; let s = '';
  const cell = (col, row, c) => R(x0 + (col - 1) * w, y0 + (row - 1) * h, w, h, c);
  for (let row = 1; row <= 7; row++) for (let col = 1; col <= 18; col++) {
    const ok = row === 1 ? (col === 1 || col === 18) : row <= 3 ? (col <= 2 || col >= 13) : true;
    if (!ok) continue;
    const c = col <= 2 ? 'fillR' : col >= 13 ? 'fillA' : 'fillY';
    s += cell(col, row, row === 1 && col === 18 ? 'fillA' : c);
  }
  for (let col = 3; col <= 16; col++) for (const row of [8.8, 9.8]) s += R(x0 + (col - 1) * w, y0 + (row - 1) * h, w, h, 'fillI');
  s += R(x0, y0 + 20, w, 6 * h, 'r thick') + R(x0 + 16 * w, y0 + 20, w, 6 * h, 'b thick') + R(x0 + 17 * w, y0, w, 7 * h, 'thick');
  return s + T(x0 + 22, y0 + 7 * h + 14, 'bloc s', 'nt', 'middle') + T(x0 + 7.5 * w, y0 + 7 * h + 14, 'bloc d', 'nt', 'middle') + T(x0 + 15.5 * w, y0 + 7 * h + 14, 'bloc p', 'nt', 'middle') + T(x0 + 16.2 * w, y0 + 9 * h + 4, 'bloc f', 'nt', 'start')
    + T(x0 + 11, y0 - 6, 'H', '', 'middle') + T(x0 + 17.5 * w, y0 - 6, 'He', '', 'middle') + T(x0 + 34, y0 + 5 * h + 10, '', '') ;
})() + T(20, 262, 'alcalins : colonne 1', 'r', 'start') + T(170, 262, 'halogènes : 17', 'b', 'start') + T(290, 262, 'gaz nobles : 18', '', 'start'), 'Tableau périodique')],

'c-classification-2': ['Évolution des propriétés : l’électronégativité augmente vers la droite et vers le haut ; le rayon atomique augmente vers la gauche et vers le bas', svg(420, 220, `
  ${R(60, 40, 300, 140, 'fillA')}${T(210, 30, 'tableau périodique', 'nt')}
  ${A(80, 120, 330, 120, 'b')}${A(330, 170, 330, 60, 'b')}${T(200, 112, 'électronégativité', 'b')}
  ${A(340, 80, 90, 80, 'r')}${A(90, 50, 90, 160, 'r')}${T(220, 72, 'rayon atomique', 'r')}`, 'Évolution des propriétés')],

'c-classification-3': ['Niveaux d’énergie de l’atome d’hydrogène, En = −13,6/n² eV : les transitions vers n = 1 forment la série de Lyman (UV), celles vers n = 2 la série de Balmer (visible)', svg(400, 256, (() => {
  const y = n => r2(30 + 200 / (n * n));
  let s = [1, 2, 3, 4, 5].map(n => L(60, y(n), 340, y(n)) + (n < 4 ? T(350, y(n) + 4, I('n') + ' = ' + n, '', 'start') : '') + (n < 4 ? T(54, y(n) + 4, (-13.6 / (n * n)).toFixed(2).replace('.', ','), '', 'end') : '')).join('');
  s += L(60, 30, 340, 30, 'dash soft') + T(350, 34, I('n') + ' = ∞', '', 'start') + T(54, 34, '0', '', 'end');
  s += [2, 3, 4].map((n, k) => A(100 + k * 30, y(n), 100 + k * 30, y(1), 'b')).join('') + [3, 4, 5].map((n, k) => A(230 + k * 30, y(n), 230 + k * 30, y(2), 'r')).join('');
  return s + T(130, 248, 'Lyman (UV)', 'b') + T(260, y(2) + 18, 'Balmer (visible)', 'r') + T(20, 18, I('E') + ' (eV)', '', 'start');
})(), 'Niveaux de H')],

// ---------- Lewis ----------
'c-lewis-1': ['Géométries VSEPR : AX₂ linéaire, AX₃ triangulaire, AX₄ tétraédrique, AX₅ bipyramide trigonale, AX₆ octaédrique ; avec doublets non liants : AX₃E pyramidale, AX₂E₂ coudée (trait épais : vers l’avant, pointillés : vers l’arrière)', svg(460, 260, (() => {
  const X = (x, y) => C(x, y, 6, 'fillW');
  const wedge = (x, y, x2, y2) => { const dx = x2 - x, dy = y2 - y, l = Math.hypot(dx, dy), px = -dy / l * 5, py = dx / l * 5; return P(`M${x},${y} L${r2(x2 + px)},${r2(y2 + py)} L${r2(x2 - px)},${r2(y2 - py)} Z`, 'fill'); };
  const lp = (x, y, deg) => { const [a, b] = pol(x, y, 22, deg); return `<ellipse cx="${a}" cy="${b}" rx="9" ry="5" transform="rotate(${-deg} ${a} ${b})" class="s soft"/>`; };
  const A0 = (x, y) => C(x, y, 9, 'fillR') + T(x, y + 4, 'A', '', 'middle');
  let s = '';
  s += L(20, 70, 100, 70) + X(20, 70) + X(100, 70) + A0(60, 70) + T(60, 120, sb('AX', '2'), 'nt');
  s += [90, 210, 330].map(d => L(160, 70, ...pol(160, 70, 38, d)) + X(...pol(160, 70, 38, d))).join('') + A0(160, 70) + T(160, 120, sb('AX', '3'), 'nt');
  s += L(260, 70, 260, 32) + X(260, 32) + L(260, 70, 228, 92) + X(228, 92) + wedge(260, 70, 290, 96) + X(290, 96) + L(260, 70, 282, 84, 'dash') + X(282, 84) + A0(260, 70) + T(260, 120, sb('AX', '4'), 'nt');
  s += L(380, 70, 380, 30) + X(380, 30) + L(380, 70, 380, 110) + X(380, 110) + L(380, 70, 345, 78) + X(345, 78) + wedge(380, 70, 410, 86) + X(410, 86) + L(380, 70, 408, 60, 'dash') + X(408, 60) + A0(380, 70) + T(430, 120, sb('AX', '5'), 'nt', 'end');
  s += L(90, 190, 90, 150) + X(90, 150) + L(90, 190, 90, 230) + X(90, 230) + L(90, 190, 52, 190) + X(52, 190) + L(90, 190, 128, 190) + X(128, 190) + wedge(90, 190, 108, 208) + X(108, 208) + L(90, 190, 72, 172, 'dash') + X(72, 172) + A0(90, 190) + T(90, 252, sb('AX', '6'), 'nt');
  s += lp(230, 180, 90) + L(230, 180, 198, 202) + X(198, 202) + wedge(230, 180, 258, 206) + X(258, 206) + L(230, 180, 236, 214, 'dash') + X(236, 214) + A0(230, 180) + T(230, 252, sb('AX', '3') + 'E pyramidale', 'nt');
  s += lp(370, 180, 60) + lp(370, 180, 120) + L(370, 180, 340, 210) + X(340, 210) + L(370, 180, 400, 210) + X(400, 210) + A0(370, 180) + T(370, 252, sb('AX', '2') + sb('E', '2') + ' coudée', 'nt');
  return s;
})(), 'VSEPR')],

'c-lewis-2': ['Moment dipolaire (orienté de la charge partielle négative vers la positive) : dans H₂O coudée, les moments de liaison s’additionnent (molécule polaire) ; dans CO₂ linéaire, ils se compensent (molécule apolaire)', svg(440, 200, `
  ${C(110, 70, 14, 'fillR')}${T(110, 75, 'O')}${L(100, 80, 60, 130)}${L(120, 80, 160, 130)}${C(55, 136, 11, 'fillW')}${C(165, 136, 11, 'fillW')}${T(55, 141, 'H')}${T(165, 141, 'H')}
  ${A(96, 94, 72, 124, 'b')}${A(124, 94, 148, 124, 'b')}${A(110, 92, 110, 150, 'r thick')}${T(118, 166, V('p'), 'r', 'start')}${T(80, 66, '2δ−', 'nt', 'end')}${T(40, 160, 'δ+', 'nt')}
  ${T(110, 192, 'polaire', 'nt')}
  ${C(250, 110, 14, 'fillR')}${C(320, 110, 12, 'fillW')}${C(390, 110, 14, 'fillR')}${T(250, 115, 'O')}${T(320, 115, 'C')}${T(390, 115, 'O')}
  ${L(264, 106, 308, 106)}${L(264, 114, 308, 114)}${L(332, 106, 376, 106)}${L(332, 114, 376, 114)}
  ${A(262, 80, 300, 80, 'b')}${A(378, 80, 340, 80, 'b')}${T(320, 150, V('p') + ' = ' + V('0'), '', 'middle')}${T(320, 192, 'apolaire', 'nt')}`, 'Moment dipolaire')],

// ---------- cinétique ----------
'c-cinetique-1': ['Méthode intégrale : on trace la grandeur qui doit varier linéairement avec t selon l’ordre supposé — [A] (ordre 0), ln[A] (ordre 1), 1/[A] (ordre 2)', svg(440, 170, `
  ${axes(20, 140, 120, 0, 120, 0, I('t'), '[A]')}${L(20, 40, 125, 130, 'b')}${T(80, 165, 'ordre 0', 'nt')}
  ${axes(165, 140, 120, 0, 120, 0, I('t'), 'ln[A]')}${L(165, 40, 280, 125, 'b')}${T(225, 165, 'ordre 1', 'nt')}
  ${axes(310, 140, 120, 0, 120, 0, I('t'), '1/[A]')}${L(310, 120, 420, 40, 'b')}${T(370, 165, 'ordre 2', 'nt')}`, 'Méthode intégrale')],

'c-cinetique-2': ['Loi d’Arrhenius k = A exp(−Ea/(RT)) : ln k est une fonction affine de 1/T, de pente −Ea/R', svg(380, 200, `
  ${axes(40, 180, 320, 0, 165, 0, '1/' + I('T'), 'ln ' + I('k'))}${L(60, 40, 340, 160, 'b')}
  ${[90, 150, 210, 270].map(x => dot(x, r2(40 + (x - 60) * 120 / 280), '')).join('')}
  ${L(150, 78.57, 250, 78.57, 'dash soft')}${L(250, 78.57, 250, 121.43, 'dash soft')}${T(260, 104, 'pente −' + sb(I('E'), 'a') + '/' + I('R'), 'b', 'start')}`, 'Arrhenius')],

'c-cinetique-3': ['Profil énergétique d’un acte élémentaire : le système passe par un état de transition (‡) ; l’énergie d’activation Ea est la hauteur de la barrière', svg(400, 220, `
  ${axes(40, 200, 340, 0, 185, 0, 'coordonnée de réaction', I('E'))}
  <path d="M50,130 C110,130 130,50 190,50 C250,50 270,160 360,160" class="s b"/>
  ${L(50, 130, 130, 130, 'dash soft')}${D(110, 130, 110, 50, '', 0, 0)}${T(104, 94, sb(I('E'), 'a'), '', 'end')}${L(110, 50, 190, 50, 'dash soft')}
  ${T(190, 40, '‡', '', 'middle')}${T(70, 122, 'réactifs', 'nt')}${T(330, 152, 'produits', 'nt')}`, 'Profil énergétique')],

// ---------- intermoléculaire ----------
'c-intermoleculaire-1': ['Liaison hydrogène entre deux molécules d’eau : un H lié à un O (donneur) interagit avec un doublet non liant d’un autre O (accepteur) ; les trois atomes sont presque alignés', svg(420, 180, `
  ${L(110, 90, 150, 90)}${L(110, 90, ...pol(110, 90, 40, 104.5))}${C(150, 90, 8, 'fillW')}${C(...pol(110, 90, 40, 104.5), 8, 'fillW')}${C(110, 90, 13, 'fillR')}${T(110, 95, 'O')}${T(150, 94, 'H')}${T(...pol(110, 90, 40, 104.5).map((v, i) => i ? v + 4 : v), 'H')}
  ${L(158, 90, 247, 90, 'dash r thick')}
  ${L(260, 90, ...pol(260, 90, 40, 52))}${L(260, 90, ...pol(260, 90, 40, -52))}${C(...pol(260, 90, 40, 52), 8, 'fillW')}${C(...pol(260, 90, 40, -52), 8, 'fillW')}${C(260, 90, 13, 'fillR')}${T(260, 95, 'O')}
  ${T(110, 150, 'donneur', 'nt')}${T(260, 150, 'accepteur', 'nt')}${T(203, 80, 'liaison H', 'r')}${D(150, 115, 260, 115, '', 0, 0)}${T(205, 132, '≈ 0,28 nm (O···O)', 'nt')}
`, 'Liaison hydrogène')],

'c-intermoleculaire-2': ['Solvatation d’un cation par l’eau : les molécules d’eau s’orientent, l’atome d’oxygène (porteur de la charge partielle négative) tourné vers le cation', svg(320, 280, `
  ${C(160, 140, 20, 'fillA b')}${T(160, 146, sup('Na', '+'))}
  ${[0, 60, 120, 180, 240, 300].map(d => { const [x, y] = pol(160, 140, 62, d); return eau(x, y, d, 1.5); }).join('')}`, 'Solvatation')],

// ---------- cristal ----------
'c-cristal-1': ['Maille cubique à faces centrées (CFC) : atomes aux sommets et aux centres des faces, 4 atomes par maille ; contact le long de la diagonale d’une face, a√2 = 4r ; compacité 0,74', svg(320, 260, (() => {
  const p = pj(60, 220, 160);
  return cube(p) + L(...p(0, 0, 0), ...p(1, 0, 1), 'r') + atoms(p, [...corners, ...faces], 13, 'fillA') + T(...p(0.5, 0, -0.12), I('a')) + T(...p(0.62, 0, 0.42), I('a') + '√2 = 4' + I('r'), 'r', 'start');
})(), 'CFC')],

'c-cristal-2': ['Maille cubique centrée : atomes aux sommets et au centre, 2 atomes par maille ; contact le long de la grande diagonale, a√3 = 4r ; compacité 0,68', svg(320, 260, (() => {
  const p = pj(60, 220, 160);
  return cube(p) + L(...p(0, 0, 0), ...p(1, 1, 1), 'r') + atoms(p, [...corners, [0.5, 0.5, 0.5]], 13, 'fillA') + T(...p(0.5, 0, -0.12), I('a')) + T(...p(0.62, 0.5, 0.42), I('a') + '√3 = 4' + I('r'), 'r', 'start');
})(), 'CC')],

'c-cristal-3': ['Empilement hexagonal compact ABAB… : couches compactes, la couche B est placée au-dessus des creux de la couche A, puis la couche suivante à l’aplomb de A', svg(440, 230, (() => {
  const lay = (cx, cy, c, n) => Array.from({length: n}, (_, i) => Array.from({length: n}, (_, j) => [cx + i * 24 + j * 12, cy + j * 20.8])).flat().map(([x, y]) => C(x, y, 12, c)).join('');
  let s = lay(40, 60, 'fillA', 4) + lay(52, 66.9, 'fillR', 4) .replace(/<circle/g, '<circle style="opacity:.85"');
  s += T(100, 170, 'A (bleu) puis B (rouge)', 'nt');
  const sx = 330, y = [190, 125, 60];
  s += [0, 1, 2].map(k => `<ellipse cx="${sx}" cy="${y[k]}" rx="70" ry="18" class="s soft"/>` + T(sx + 84, y[k] + 4, ['A', 'B', 'A'][k], k === 1 ? 'r' : 'b', 'start')).join('');
  s += [0, 2].map(k => [-50, -25, 25, 50, 0].map(dx => C(sx + dx, y[k] + (Math.abs(dx) === 25 ? (dx > 0 ? -10 : 10) : 0), 8, 'fillA')).join('')).join('');
  s += [-22, 0, 22].map((dx, i) => C(sx + dx, y[1] + [6, -8, 6][i], 8, 'fillR')).join('');
  return s;
})(), 'Hexagonal compact')],

'c-cristal-4': ['Sites interstitiels de la maille CFC : 4 sites octaédriques (centre de la maille et milieux des arêtes) et 8 sites tétraédriques (centres des 8 petits cubes d’arête a/2)', svg(320, 260, (() => {
  const p = pj(60, 220, 160);
  const oct = [[0.5, 0.5, 0.5], [0.5, 0, 0], [0.5, 1, 0], [0.5, 0, 1], [0.5, 1, 1], [0, 0.5, 0], [1, 0.5, 0], [0, 0.5, 1], [1, 0.5, 1], [0, 0, 0.5], [1, 0, 0.5], [0, 1, 0.5], [1, 1, 0.5]];
  const tet = [0.25, 0.75].flatMap(x => [0.25, 0.75].flatMap(y => [0.25, 0.75].map(z => [x, y, z])));
  return cube(p) + atoms(p, [...corners, ...faces], 8, 'fillW') + oct.map(q => { const [x, y] = p(...q); return R(x - 5, y - 5, 10, 10, 'fillR r'); }).join('') + tet.map(q => { const [x, y] = p(...q); return P(`M${x},${y - 6} L${x + 6},${y + 5} L${x - 6},${y + 5} Z`, 'fillB b'); }).join('')
    + R(20, 236, 10, 10, 'fillR r') + T(36, 245, 'site octaédrique', 'nt', 'start') + P('M180,235 L186,246 L174,246 Z', 'fillB b') + T(192, 245, 'site tétraédrique', 'nt', 'start');
})(), 'Sites interstitiels')],

'c-cristal-5': ['Structures ioniques : NaCl (ions Cl⁻ en CFC, Na⁺ dans tous les sites octaédriques, coordinence 6) et CsCl (Cl⁻ aux sommets, Cs⁺ au centre, coordinence 8)', svg(460, 275, (() => {
  const p = pj(30, 200, 130), q = pj(290, 190, 110);
  const g = [0, 0.5, 1].flatMap(x => [0, 0.5, 1].flatMap(y => [0, 0.5, 1].map(z => [x, y, z])));
  const nacl = g.sort((a, b) => b[1] - a[1]).map(t => { const cl = (Math.round(2 * (t[0] + t[1] + t[2])) % 2) === 0; return at(p, t, cl ? 12 : 7, cl ? 'fillB' : 'fillR'); }).join('');
  return cube(p) + nacl + T(120, 236, 'NaCl', 'nt') + cube(q) + atoms(q, corners, 11, 'fillB') + at(q, [0.5, 0.5, 0.5], 12, 'fillR') + T(370, 236, 'CsCl', 'nt')
    + C(150, 260, 8, 'fillB') + T(162, 264, sup('Cl', '−'), '', 'start') + C(250, 260, 6, 'fillR') + T(262, 264, 'cation', 'nt', 'start');
})(), 'NaCl et CsCl')],

'c-cristal-6': ['Blende ZnS : ions S²⁻ en CFC, Zn²⁺ dans la moitié des sites tétraédriques (un sur deux, en quinconce). Le diamant a la même structure, tous les atomes étant des atomes de carbone', svg(320, 260, (() => {
  const p = pj(60, 220, 160);
  const tet = [[0.25, 0.25, 0.25], [0.75, 0.75, 0.25], [0.75, 0.25, 0.75], [0.25, 0.75, 0.75]];
  const bonds = tet.flatMap(t => [...corners, ...faces].filter(q => Math.abs(q[0] - t[0]) + Math.abs(q[1] - t[1]) + Math.abs(q[2] - t[2]) < 0.8).map(q => L(...p(...t), ...p(...q), 'soft'))).join('');
  return cube(p) + bonds + atoms(p, [...corners, ...faces], 11, 'fillB') + atoms(p, tet, 8, 'fillR') + C(20, 26, 8, 'fillB') + T(32, 30, sup('S', '2−'), '', 'start') + C(20, 48, 6, 'fillR') + T(32, 52, sup('Zn', '2+'), '', 'start');
})(), 'Blende')],

// ---------- acide-base ----------
'c-acide-base-1': ['Diagramme de prédominance d’un couple HA/A⁻ : HA prédomine pour pH &lt; pKa, A⁻ pour pH > pKa', svg(400, 110, `
  ${A(20, 60, 380, 60)}${T(384, 64, 'pH', '', 'start')}${L(200, 50, 200, 70, 'thick')}${T(200, 90, 'p' + sb(I('K'), 'a'))}
  ${T(110, 48, 'HA prédomine', 'r')}${T(290, 48, sup('A', '−') + ' prédomine', 'b')}`, 'Prédominance')],

'c-acide-base-2': ['Titrage pH-métrique d’un acide faible par une base forte : à la demi-équivalence, pH = pKa ; saut de pH à l’équivalence (volume Ve), repéré par le maximum de dpH/dV', svg(400, 240, `
  ${axes(40, 220, 340, 0, 205, 0, I('V'), 'pH')}
  ${courbe(u => { const v = u / 300 * 2, x = Math.min(v, 0.9999); if (v < 0.999) return 15 * (4.8 + Math.log10(Math.max(x, 0.02) / (1 - x))); return 15 * (13 - 1 / (1 + 30 * (v - 1))); }, 6, 300, 40, 220, 1, -1, 400, 'b')}
  ${L(190, 216, 190, 30, 'dash soft')}${T(190, 234, sb(I('V'), 'e'))}${L(115, 216, 115, 148, 'dash soft')}${L(36, 148, 115, 148, 'dash soft')}${T(115, 234, sb(I('V'), 'e') + '/2')}${T(34, 152, 'p' + sb(I('K'), 'a'), '', 'end')}${dot(190, 120)}${T(198, 120, 'équivalence', 'nt', 'start')}`, 'Titrage pH-métrique')],

'c-acide-base-3': ['Titrage conductimétrique (acide fort par la soude) : la conductivité varie par segments de droite ; l’équivalence correspond à la rupture de pente (H₃O⁺ très conducteur remplacé par Na⁺, puis excès de HO⁻)', svg(380, 220, `
  ${axes(40, 200, 320, 0, 185, 0, I('V'), I('σ'))}${L(40, 40, 180, 160, 'b')}${L(180, 160, 340, 70, 'b')}
  ${L(180, 160, 180, 204, 'dash soft')}${T(180, 216, sb(I('V'), 'e'))}${dot(180, 160)}`, 'Titrage conductimétrique')],

// ---------- solubilité ----------
'c-solubilite-1': ['Diagramme d’existence du précipité AgCl quand on ajoute des ions Cl⁻ à une solution de Ag⁺ (concentration c) : le précipité existe pour pCl &lt; pKs − pc', svg(400, 110, `
  ${A(20, 60, 380, 60)}${T(384, 64, 'pCl', '', 'start')}${L(220, 48, 220, 72, 'thick')}${T(220, 92, 'p' + sb(I('K'), 's') + ' − p' + I('c'))}
  ${R(20, 52, 200, 16, 'fillR')}${T(120, 40, 'AgCl(s) existe', 'r')}${T(300, 40, 'pas de précipité', 'nt')}`, 'Diagramme d’existence')],

'c-solubilite-2': ['Solubilité d’un hydroxyde amphotère (exemple Zn(OH)₂) en fonction du pH : log s décroît (pente −2, Zn²⁺) puis croît (pente +2, [Zn(OH)₄]²⁻) ; solubilité minimale aux pH intermédiaires', svg(420, 230, `
  ${axes(40, 200, 350, 0, 185, 0, 'pH', 'log ' + I('s'))}${L(36, 30, 44, 30)}${T(32, 34, '0', '', 'end')}${T(32, 204, '−10', '', 'end')}
  ${courbe(u => { const pH = u / 24, ls = Math.min(0, Math.log10(10 ** (11.5 - 2 * pH) + 10 ** (-29 + 2 * pH))); return (ls + 10) * 17; }, 96, 340, 40, 200, 1, -1, 400, 'b')}
  ${[6, 10].map(v => L(40 + v * 24, 196, 40 + v * 24, 204) + T(40 + v * 24, 218, String(v))).join('')}
  ${T(196, 130, 'pente −2', 'nt', 'end')}${T(196, 148, sup('Zn', '2+'), 'nt', 'end')}${T(330, 170, 'pente +2', 'nt', 'start')}${T(330, 188, sup('[Zn(OH)₄]', '2−'), 'nt', 'start')}${T(282, 196, 'Zn(OH)₂(s)', 'nt')}
`, 'Solubilité et pH')],

// ---------- redox ----------
'c-redox-1': ['Pile Daniell : l’électrode de zinc (anode, pôle −) s’oxyde, les électrons circulent dans le circuit extérieur vers l’électrode de cuivre (cathode, pôle +) où Cu²⁺ est réduit ; le pont salin ferme le circuit', svg(440, 250, `
  ${P('M40,120 L40,230 L170,230 L170,120', '')}${R(42, 150, 126, 78, 'fillA')}${P('M270,120 L270,230 L400,230 L400,120', '')}${R(272, 150, 126, 78, 'fillY')}
  ${R(95, 80, 14, 120, 'fillW')}${R(330, 80, 14, 120, 'fillR')}${T(102, 216, sup('Zn', '2+'), '', 'middle')}${T(337, 216, sup('Cu', '2+'), '', 'middle')}
  ${P('M140,190 L140,100 L300,100 L300,190', 'thick soft')}${T(220, 92, 'pont salin', 'nt')}
  ${L(102, 80, 102, 40)}${L(337, 80, 337, 40)}${L(102, 40, 180, 40)}${res(180, 40, 260, 40)}${L(260, 40, 337, 40)}
  ${A(130, 28, 170, 28, 'b')}${T(150, 20, sup('e', '−'), 'b')}${A(310, 52, 280, 52, 'r')}${T(296, 68, I('i'), 'r')}
  ${T(80, 110, 'Zn', '', 'end')}${T(360, 110, 'Cu', '', 'start')}${T(80, 70, '−', '', 'end')}${T(360, 70, '+', '', 'start')}${T(102, 246, 'anode', 'nt')}${T(337, 246, 'cathode', 'nt')}`, 'Pile Daniell')],

'c-redox-2': ['Échelle des potentiels standard : la réaction spontanée (quantitative si les E° sont suffisamment écartés) a lieu entre l’oxydant le plus fort et le réducteur le plus fort (règle du gamma)', svg(380, 256, (() => {
  const C0 = [['Cu²⁺', 'Cu', 0.34], ['2 H⁺', 'H₂', 0], ['Fe²⁺', 'Fe', -0.44], ['Zn²⁺', 'Zn', -0.76]];
  const y = e => r2(120 - e * 120);
  return A(190, 225, 190, 40) + T(184, 46, I('E') + '° (V)', '', 'end') + C0.map(([o, r, e]) => L(184, y(e), 196, y(e)) + T(170, y(e) + 4, o, 'r', 'end') + T(210, y(e) + 4, r, 'b', 'start') + T(300, y(e) + 4, e.toFixed(2).replace('.', ','), 'nt', 'end')).join('')
    + T(120, 22, 'oxydants', 'r') + T(260, 22, 'réducteurs', 'b') + A(150, y(0.34) + 8, 222, y(-0.76) - 10, 'soft') + T(190, 246, 'réaction : oxydant le plus fort + réducteur le plus fort', 'nt');
})(), 'Échelle des potentiels')],

// ---------- E-pH ----------
'c-e-ph-1': ['Diagramme E-pH de l’eau (pressions de 1 bar) : O₂/H₂O, E = 1,23 − 0,06 pH ; H₂O/H₂, E = −0,06 pH ; l’eau est stable entre les deux droites', svg(420, 260, (() => {
  const X = pH => r2(50 + pH * 23), Y = E => r2(130 - E * 80);
  return axes(50, Y(0), 350, 0, 115, 125, 'pH', I('E') + ' (V)') + L(X(0), Y(1.23), X(14), Y(1.23 - 0.84), 'b') + L(X(0), Y(0), X(14), Y(-0.84), 'b')
    + T(X(9), Y(0.95), sb('O', '2'), 'b') + T(X(5), Y(0.2), sb('H', '2') + 'O', '', 'middle') + T(X(4), Y(-0.6), sb('H', '2'), 'b') + T(X(0) - 6, Y(1.23) + 4, '1,23', '', 'end') + T(X(14), Y(0) + 16, '14', '', 'middle');
})(), 'E-pH de l’eau')],

'c-e-ph-2': ['Diagramme E-pH simplifié du fer (concentration de tracé 10⁻² mol·L⁻¹) : domaines de Fe(s), Fe²⁺, Fe³⁺, Fe(OH)₂(s), Fe(OH)₃(s) ; droites de l’eau en pointillés', svg(420, 260, (() => {
  const X = pH => r2(50 + pH * 24), Y = E => r2(130 - E * 90);
  let s = axes(50, Y(0), 350, 0, 120, 120, 'pH', I('E') + ' (V)');
  s += P(`M${X(0)},${Y(0.77)} L${X(2)},${Y(0.77)} L${X(2)},${Y(1.15)}`) + P(`M${X(2)},${Y(0.77)} L${X(7.5)},${Y(-0.22)} L${X(14)},${Y(-0.61)}`) + L(X(7.5), Y(-0.22), X(7.5), Y(-0.5));
  s += P(`M${X(0)},${Y(-0.5)} L${X(7.5)},${Y(-0.5)} L${X(14)},${Y(-0.89)}`);
  s += L(X(0), Y(1.23), X(14), Y(0.39), 'dash soft') + L(X(0), Y(0), X(14), Y(-0.84), 'dash soft');
  return s + T(X(0.9), Y(0.95), sup('Fe', '3+'), 'b') + T(X(3), Y(0.3), sup('Fe', '2+'), 'b') + T(X(9.5), Y(0.4), 'Fe(OH)' + sb('', '3'), 'b') + T(X(11), Y(-0.6), 'Fe(OH)' + sb('', '2'), 'b') + T(X(5), Y(-0.9), 'Fe', 'b') + T(X(2), Y(0) + 16, '2') + T(X(7.5), Y(0) + 16, '7,5');
})(), 'E-pH du fer')],

'c-e-ph-3': ['Superposition de deux diagrammes E-pH : si les domaines de l’oxydant Ox₁ et du réducteur Red₂ sont disjoints, ils réagissent ; une espèce dont le domaine recoupe celui de l’autre est stable en sa présence', svg(400, 230, `
  ${axes(40, 210, 340, 0, 195, 0, 'pH', I('E'))}
  ${L(40, 60, 370, 110, 'r')}${L(40, 150, 370, 190, 'b')}
  ${T(120, 50, sb('Ox', '1'), 'r')}${T(120, 92, sb('Red', '1'), 'r')}${T(120, 150, sb('Ox', '2'), 'b')}${T(120, 182, sb('Red', '2'), 'b')}
  ${D(220, 87, 220, 172, '', 0, 0)}${T(228, 128, 'domaines disjoints :', 'nt', 'start')}${T(228, 146, sb('Ox', '1') + ' + ' + sb('Red', '2') + ' réagissent', 'nt', 'start')}`, 'Superposition')],
};
