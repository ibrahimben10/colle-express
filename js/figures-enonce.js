// Schémas d'énoncé ajoutés (exercices de physique, priorité haute du relevé des schémas).
import { svg, L, A, D, T, I, V, C, R, P, dot, spring, ground, wallV, lens, ox, ot, sb } from './figkit.js';
import { res, cap, coil, gen, sw, arc, rot, E, pol, wav } from './figkit2.js';

// Arc en angles « écran » (degrés, y vers le bas, sens horaire croissant).
const arcS = (cx, cy, r, s1, s2, c = '') => {
  const p = s => [cx + r * Math.cos(s * Math.PI / 180), cy + r * Math.sin(s * Math.PI / 180)];
  const [x1, y1] = p(s1), [x2, y2] = p(s2);
  return `<path d="M${x1.toFixed(1)},${y1.toFixed(1)} A${r},${r} 0 0 ${s2 > s1 ? 1 : 0} ${x2.toFixed(1)},${y2.toFixed(1)}" class="s ${c}"/>`;
};
const ptS = (cx, cy, r, s) => [cx + r * Math.cos(s * Math.PI / 180), cy + r * Math.sin(s * Math.PI / 180)];
const TS = (cx, cy, r, s, t, c = '') => { const [x, y] = ptS(cx, cy, r, s); return T(x.toFixed(1), (y + 5).toFixed(1), t, c); };

// Prisme : trajet calculé pour A = 60°, n = 1,5, i = 50°.
function prisme() {
  const rad = Math.PI / 180, n = 1.5, Ad = 60, i = 50;
  const r = Math.asin(Math.sin(i * rad) / n) / rad, rp = Ad - r, ip = Math.asin(n * Math.sin(rp * rad)) / rad;
  const S = [180, 30], len = 170;
  const Lb = [S[0] - len * Math.sin(30 * rad), S[1] + len * Math.cos(30 * rad)], Rb = [S[0] + len * Math.sin(30 * rad), Lb[1]];
  const Ip = [S[0] - 118 * Math.sin(30 * rad), S[1] + 118 * Math.cos(30 * rad)];
  const sIn = 30 - i, sInt = 30 - r;                      // directions écran du rayon incident et du rayon intérieur
  const u = [Math.cos(sInt * rad), Math.sin(sInt * rad)];
  // intersection avec la face de droite : S + t·(sin30, cos30)
  const f = [Math.sin(30 * rad), Math.cos(30 * rad)];
  const det = u[0] * (-f[1]) - u[1] * (-f[0]);
  const t1 = ((S[0] - Ip[0]) * (-f[1]) - (S[1] - Ip[1]) * (-f[0])) / det;
  const J = [Ip[0] + t1 * u[0], Ip[1] + t1 * u[1]];
  const sOut = -30 + ip;
  const st = (p, s, l) => [p[0] + l * Math.cos(s * rad), p[1] + l * Math.sin(s * rad)];
  const I0 = st(Ip, sIn + 180, 112), J1 = st(J, sOut, 105);
  const nI1 = st(Ip, 210, 44), nI2 = st(Ip, 30, 44), nJ1 = st(J, -30, 44), nJ2 = st(J, 150, 44);
  return svg(360, 220, `
    ${P(`M${S} L${Lb} L${Rb} Z`, 'fillA thick')}${L(...nI1, ...nI2, 'dash soft')}${L(...nJ1, ...nJ2, 'dash soft')}
    ${A(...I0, ...Ip, 'r')}${L(...Ip, ...J, 'thick r')}${A(...J, ...J1, 'r')}
    ${arcS(...S, 26, 60, 120)}${TS(...S, 40, 90, I('A'))}
    ${arcS(...Ip, 28, sIn + 180 - 360 + 360, 210)}${TS(...Ip, 42, (sIn + 180 + 210) / 2, I('i'))}
    ${arcS(...Ip, 30, sInt, 30)}${TS(...Ip, 44, (sInt + 30) / 2, I('r'))}
    ${arcS(...J, 30, 150, sInt + 180)}${TS(...J, 44, (150 + sInt + 180) / 2, I('r') + '′')}
    ${arcS(...J, 28, -30, sOut)}${TS(...J, 42, (sOut - 30) / 2, I('i') + '′')}
    ${T(180, 170, I('n') + ' = 1,50', 'soft')}`, 'Prisme et rayon lumineux');
}

// Cylindres roulant sur un plan incliné.
function plan() {
  const O = [30, 60], B = [330, 190], len = Math.hypot(B[0] - O[0], B[1] - O[1]);
  const u = [(B[0] - O[0]) / len, (B[1] - O[1]) / len], n = [u[1], -u[0]], Rr = 22;
  const al = Math.atan2(B[1] - O[1], B[0] - O[0]) * 180 / Math.PI;
  const at = s => [O[0] + s * u[0], O[1] + s * u[1]], ce = s => { const p = at(s); return [p[0] + Rr * n[0], p[1] + Rr * n[1]]; };
  const c1 = ce(80), c2 = ce(185), p1 = at(80);
  return svg(360, 220, `
    ${P(`M${O} L${B} L30,190 Z`, 'fillW')}${ground(20, 190, 330)}
    ${C(...c1, Rr, 'fillA')}${dot(...c1)}${L(...c1, ...p1, 'dim')}${T(c1[0] - 14, c1[1] - 2, I('R'), '', 'end')}
    ${C(...c2, Rr, 'thick')}${C(...c2, Rr - 3)}${dot(...c2)}
    ${T(c1[0] + 4, c1[1] - 30, 'plein', 'soft')}${T(c2[0] + 6, c2[1] - 30, 'creux', 'soft')}
    ${arcS(330, 190, 52, 180, 180 + al)}${TS(330, 190, 66, 180 + al / 2, 'α')}
    ${A(325, 30, 325, 80)}${T(333, 64, V('g'), '', 'start')}`, 'Cylindres sur un plan incliné');
}

// Chaîne de maillons courts et longs.
function chaine() {
  const seq = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1], ls = 24, ll = 38; let x = 30, body = '', firstS = null, firstL = null;
  for (const k of seq) { const w = k ? ll : ls; body += R(x, 66, w, 16, k ? 'fillA' : 'fillR', 8); if (k && firstL === null) firstL = x + w / 2; if (!k && firstS === null) firstS = x + w / 2; x += w; }
  return svg(400, 150, `${wallV(30, 44, 60)}${body}${A(x, 74, x + 44, 74, 'r')}${T(x + 30, 64, V('f'), 'r')}
    ${T(firstL, 56, I('ℓ') + ' + ' + I('a'), 'soft')}${T(firstS, 104, I('ℓ') + ' − ' + I('a'), 'soft')}
    ${D(30, 124, x, 124, '𝓛', (30 + x) / 2, 142)}`, 'Fibre : chaîne de maillons');
}

export const FIG2 = {
'n-p2-ailette': {legende: 'Ailette : tige de rayon a fixée en x = 0 à une paroi à T₀, entourée d’air à Tₑ', svg: svg(360, 170, `
  ${wallV(40, 20, 120)}${T(26, 160, sb(I('T'), '0'))}
  ${R(40, 60, 290, 30, 'fillA')}${L(330, 60, 340, 60, 'dash')}${L(330, 90, 340, 90, 'dash')}${L(40, 75, 350, 75, 'axis')}
  ${[100, 170, 240].map(x => wav(x, 56, 0, -30) + wav(x + 30, 94, 0, 22)).join('')}${T(300, 30, I('h') + '(' + I('T') + ' − ' + sb(I('T'), 'e') + ')', 'r')}
  ${A(52, 75, 52, 62)}${T(58, 72, I('a'), '', 'start')}
  ${A(40, 140, 345, 140)}${T(348, 144, I('x'), '', 'start')}${T(40, 156, '0')}${T(200, 160, 'air à ' + sb(I('T'), 'e'), 'b')}`,
  'Ailette de refroidissement')},
'p-th-spe1': {legende: 'Conducteur cylindrique parcouru par i, extrémités calorifugées, pertes latérales vers le milieu à T₀', svg: svg(360, 190, `
  ${R(60, 48, 240, 64, 'fillA')}${E(60, 80, 10, 32, 'fillB')}${E(300, 80, 10, 32, 'fillA')}
  ${L(20, 80, 50, 80, 'thick')}${L(310, 80, 340, 80, 'thick')}${A(110, 80, 190, 80, 'r')}${T(150, 72, I('i'), 'r')}
  ${[100, 170, 240].map(x => wav(x, 44, 0, -26) + wav(x + 30, 116, 0, 24)).join('')}${T(330, 28, 'β(' + I('T') + ' − ' + sb(I('T'), '0') + ')', 'r', 'end')}
  ${D(316, 80, 316, 48, I('a'), 330, 70)}${T(60, 136, 'calorifugé', 'soft')}${T(300, 136, 'calorifugé', 'soft')}
  ${A(60, 168, 340, 168)}${T(343, 172, I('z'), '', 'start')}${T(60, 184, '0')}${T(300, 184, I('L'))}${L(60, 163, 60, 173)}${L(300, 163, 300, 173)}
  ${T(30, 28, 'milieu à ' + sb(I('T'), '0'), 'b', 'start')}`,
  'Conducteur refroidi')},
'p-th-ccmp15': {legende: 'Coupe du phoque : cœur de rayon Rᵢ qui produit P, couche de graisse d’épaisseur ΔR, eau à Tₑ', svg: svg(320, 240, `
  ${C(150, 120, 92, 'fillY')}${C(150, 120, 62, 'fillR')}${dot(150, 120)}
  ${A(150, 120, ...pol(150, 120, 62, 145))}${T(120, 128, sb(I('R'), 'i'), '', 'end')}${A(150, 120, ...pol(150, 120, 92, 30))}${T(206, 104, sb(I('R'), 'e'), '', 'start')}
  ${T(150, 152, 'cœur : ' + I('P') + ', ' + sb(I('T'), 'i'))}${T(150, 200, 'graisse, λ')}${T(300, 30, 'eau, ' + sb(I('T'), 'e'), 'b', 'end')}
  ${D(...pol(150, 120, 62, -60), ...pol(150, 120, 92, -60), 'Δ' + I('R'), 214, 214)}`,
  'Phoque')},
'n-p2-isolant': {legende: 'Fil de rayon r₁ à T₁ et gaine isolante de rayon extérieur r₂ dans l’air à Tₑ', svg: svg(320, 240, `
  ${C(140, 120, 84, 'fillY')}${C(140, 120, 24, 'fillR')}${dot(140, 120)}
  ${A(140, 120, ...pol(140, 120, 24, 135))}${T(112, 100, sb(I('r'), '1'), '', 'end')}${A(140, 120, ...pol(140, 120, 84, 20))}${T(196, 106, sb(I('r'), '2'), '', 'start')}
  ${T(140, 142, sb(I('T'), '1'))}${T(140, 190, 'gaine, λ')}
  ${[-35, 200, 250].map(a => { const [x1, y1] = pol(140, 120, 88, a), [x2, y2] = pol(140, 120, 116, a); return wav(x1.toFixed(1), y1.toFixed(1), x2 - x1, y2 - y1); }).join('')}
  ${T(305, 40, 'air : ' + sb(I('T'), 'e') + ', ' + I('h'), 'b', 'end')}`,
  'Fil gainé')},
'n-p1-rc': {legende: 'Charge de C par le générateur E à travers R ; l’interrupteur K est fermé à t = 0', svg: svg(340, 200, `
  ${gen(50, 100)}${L(50, 40, 50, 86)}${L(50, 114, 50, 160)}${L(50, 40, 90, 40)}${sw(90, 40, 120, 40)}${L(120, 40, 152, 40)}${res(170, 40)}${L(188, 40, 290, 40)}
  ${L(290, 40, 290, 95)}${cap(290, 100, false)}${L(290, 105, 290, 160)}${L(50, 160, 290, 160)}
  ${A(26, 128, 26, 72, 'b')}${T(18, 104, I('E'), 'b', 'end')}${T(105, 22, I('K'))}${T(170, 24, I('R'))}${T(312, 104, I('C'), '', 'start')}
  ${A(206, 40, 240, 40, 'r')}${T(223, 32, I('i'), 'r')}${A(188, 60, 152, 60, 'b')}${T(170, 76, sb(I('u'), 'R'), 'b')}
  ${A(268, 126, 268, 74, 'b')}${T(260, 104, sb(I('u'), 'C'), 'b', 'end')}`,
  'Circuit RC')},
'n-p1-passebande': {legende: 'Circuit RLC série alimenté par e(t) ; la sortie s est prise aux bornes de R', svg: svg(360, 200, `
  ${gen(50, 100)}${L(50, 40, 50, 86)}${L(50, 114, 50, 160)}${L(50, 40, 110, 40)}${coil(130, 40)}${L(150, 40, 205, 40)}${cap(210, 40)}${L(215, 40, 300, 40)}
  ${L(300, 40, 300, 82)}${res(300, 100, false)}${L(300, 118, 300, 160)}${L(50, 160, 300, 160)}
  ${T(130, 22, I('L'))}${T(210, 22, I('C'))}${T(284, 104, I('R'), '', 'end')}
  ${A(26, 128, 26, 72, 'b')}${T(18, 104, I('e') + '(' + I('t') + ')', 'b', 'end')}${A(324, 128, 324, 72, 'b')}${T(334, 104, I('s'), 'b', 'start')}`,
  'Filtre RLC')},
'n-p1-passebas': {legende: 'Filtre RC : R en série, sortie s aux bornes de C, sortie ouverte', svg: svg(340, 190, `
  ${L(44, 50, 102, 50)}${res(120, 50)}${L(138, 50, 280, 50)}${L(200, 50, 200, 95)}${cap(200, 100, false)}${L(200, 105, 200, 150)}${L(44, 150, 280, 150)}
  ${dot(200, 50)}${dot(200, 150)}${C(44, 50, 4, 'fillW')}${C(44, 150, 4, 'fillW')}${C(280, 50, 4, 'fillW')}${C(280, 150, 4, 'fillW')}
  ${T(120, 34, I('R'))}${T(220, 104, I('C'), '', 'start')}
  ${A(30, 138, 30, 62, 'b')}${T(22, 104, I('e'), 'b', 'end')}${A(296, 138, 296, 62, 'b')}${T(306, 104, I('s'), 'b', 'start')}`,
  'Filtre RC')},
'n-p1-rlc': {legende: 'Condensateur chargé sous U₀ qui se décharge dans L et R à la fermeture de K (t = 0)', svg: svg(340, 210, `
  ${L(60, 40, 60, 100)}${cap(60, 105, false)}${L(60, 110, 60, 170)}${L(60, 40, 100, 40)}${sw(100, 40, 130, 40)}${L(130, 40, 170, 40)}${coil(190, 40)}${L(210, 40, 280, 40)}
  ${L(280, 40, 280, 87)}${res(280, 105, false)}${L(280, 123, 280, 170)}${L(60, 170, 280, 170)}
  ${T(78, 98, '+' + I('q'), 'r', 'start')}${T(78, 124, '−' + I('q'), 'b', 'start')}${T(40, 110, I('C'), '', 'end')}
  ${T(115, 22, I('K') + ' (' + I('t') + ' = 0)')}${T(190, 22, I('L'))}${T(300, 110, I('R'), '', 'start')}
  ${A(226, 40, 260, 40, 'r')}${T(243, 32, I('i'), 'r')}${T(170, 198, sb(I('u'), 'C') + '(0) = ' + sb(I('U'), '0'), 'soft')}`,
  'Circuit RLC libre')},
'n-p2-coax': {legende: 'Coupe du câble coaxial : âme de rayon R₁, gaine de rayon R₂, polyéthylène (εᵣ) entre les deux', svg: svg(300, 240, `
  ${C(150, 115, 96, 'fillB')}${C(150, 115, 88, 'fillA')}${C(150, 115, 26, 'fillB')}${dot(150, 115)}
  ${A(150, 115, ...pol(150, 115, 26, 40))}${T(178, 92, sb(I('R'), '1'), '', 'start')}${A(150, 115, ...pol(150, 115, 88, -35))}${T(206, 150, sb(I('R'), '2'), '', 'start')}
  ${T(150, 64, 'polyéthylène, ' + sb('ε', 'r'))}${T(150, 150, 'âme')}${T(285, 30, 'gaine', '', 'end')}`,
  'Câble coaxial')},
'n-p2-dipole': {legende: 'Ion Na⁺ en O et molécule d’eau (dipôle p) en M, à la distance r ; θ est l’angle entre u_r et p', svg: svg(360, 200, `
  ${C(70, 130, 13, 'fillR')}${T(70, 135, '+', 'r')}${T(70, 166, 'Na⁺', 'r')}
  ${L(70, 130, 330, 72, 'dash soft')}${dot(250, 90)}${T(246, 112, I('M'), '', 'end')}
  ${A(250, 90, ...pol(250, 90, 58, 55), 'b')}${T(...pol(250, 90, 70, 58).map(v => v.toFixed(1)), V('p'), 'b')}
  ${A(250, 90, ...pol(250, 90, 40, 12.5))}${T(296, 98, sb(V('u'), 'r'), '', 'start')}
  ${arc(250, 90, 28, 12.5, 55)}${T(...pol(250, 90, 38, 34).map(v => v.toFixed(1)), 'θ')}${T(160, 100, I('r'))}`,
  'Ion et dipôle')},
'n-p2-peau': {legende: 'Conducteur ohmique (γ) occupant z > 0 ; champ E = E(z,t) u_x imposé en surface', svg: svg(340, 200, `
  ${R(150, 20, 180, 140, 'fillA')}${L(150, 20, 150, 160, 'thick')}${T(240, 46, 'conducteur, γ')}${T(80, 46, 'vide', 'soft')}
  ${A(162, 120, 162, 56, 'r')}${T(170, 78, sb(I('E'), '0') + ' cos ω' + I('t'), 'r', 'start')}
  ${A(40, 180, 330, 180)}${T(333, 184, I('z'), '', 'start')}${L(150, 175, 150, 185)}${T(150, 196, '0')}
  ${A(50, 150, 90, 150)}${T(94, 154, I('z'), '', 'start')}${A(50, 150, 50, 110)}${T(56, 112, I('x'), '', 'start')}${ox(50, 150)}${T(40, 160, I('y'), '', 'end')}`,
  'Effet de peau')},
'n-p1-bobine': {legende: 'Bobine plate (N spires, surface S) fermée sur elle-même, dans B(t) parallèle à son axe', svg: svg(320, 200, `
  ${[0, 5, 10].map(d => E(150 + d, 100, 16, 62, d ? '' : 'fillA')).join('')}${L(30, 100, 300, 100, 'axis')}
  ${[40, 170].map(y => A(30, y, 290, y, 'b')).join('')}${T(290, 28, V('B') + '(' + I('t') + ')', 'b', 'end')}
  ${A(176, 100, 236, 100, 'r')}${T(232, 92, V('n'), 'r')}${T(110, 60, I('N') + ' spires', '', 'end')}${T(110, 146, 'surface ' + I('S'), '', 'end')}`,
  'Bobine plate')},
'n-p1-rails': {legende: 'Rails de Laplace vus de dessus : barre mobile à l’abscisse x, résistor R, champ B vertical', svg: svg(360, 200, `
  ${L(40, 50, 340, 50, 'thick')}${L(40, 150, 340, 150, 'thick')}${L(40, 50, 40, 82)}${res(40, 100, false)}${L(40, 118, 40, 150)}${T(24, 104, I('R'), '', 'end')}
  ${R(226, 42, 8, 116, 'fillR', 2)}${A(240, 100, 290, 100, 'r')}${T(266, 92, V('v'), 'r')}${T(230, 34, 'barre (' + I('m') + ')')}
  ${[[110, 76], [110, 124], [170, 100], [300, 72], [300, 128]].map(([x, y]) => ox(x, y)).join('')}${T(170, 126, V('B'), 'b')}
  ${D(325, 50, 325, 150, I('ℓ'), 340, 104)}${D(40, 178, 230, 178, I('x'), 135, 172)}`,
  'Rails de Laplace')},
'n-p1-transfo': {legende: 'Transformateur parfait : N₁ spires au primaire, N₂ au secondaire, sur un même circuit magnétique fermé', svg: svg(380, 200, `
  ${R(110, 30, 140, 140, 'fillA', 4)}${R(140, 60, 80, 80, 'fillW', 2)}
  ${[74, 88, 102, 116].map(y => R(102, y, 46, 7, 'fillW', 3)).join('')}${[78, 94, 110].map(y => R(212, y, 46, 7, 'fillW', 3)).join('')}
  ${L(40, 74, 102, 74)}${L(40, 123, 102, 123)}${C(40, 74, 4, 'fillW')}${C(40, 123, 4, 'fillW')}
  ${L(258, 78, 320, 78)}${L(258, 117, 320, 117)}${L(320, 78, 320, 80)}${res(320, 98, false)}${L(320, 116, 320, 117)}
  ${A(28, 116, 28, 80, 'b')}${T(20, 102, sb(I('u'), '1'), 'b', 'end')}${A(54, 74, 84, 74, 'r')}${T(69, 66, sb(I('i'), '1'), 'r')}
  ${A(346, 112, 346, 84, 'b')}${T(354, 102, sb(I('u'), '2'), 'b', 'start')}${A(266, 78, 296, 78, 'r')}${T(281, 70, sb(I('i'), '2'), 'r')}${T(304, 102, I('R'), '', 'end')}
  ${T(125, 22, sb(I('N'), '1'))}${T(235, 22, sb(I('N'), '2'))}`,
  'Transformateur')},
'n-p2-alternateur': {legende: 'Vue de dessus : la bobine tourne autour de l’axe Δ (perpendiculaire à la figure) ; sa normale n fait l’angle θ = ωt avec B', svg: svg(320, 230, `
  ${[30, 200].map(y => A(20, y, 300, y, 'b')).join('')}${T(296, 24, V('B'), 'b', 'end')}
  ${L(...pol(160, 115, 72, 130), ...pol(160, 115, 72, -50), 'thick')}${T(...pol(160, 115, 86, 130).map(v => v.toFixed(1)), 'bobine', 'soft')}
  ${A(160, 115, ...pol(160, 115, 66, 40), 'r')}${T(...pol(160, 115, 80, 40).map(v => v.toFixed(1)), V('n'), 'r')}
  ${L(160, 115, 250, 115, 'dash soft')}${arc(160, 115, 34, 0, 40)}${T(...pol(160, 115, 46, 20).map(v => v.toFixed(1)), 'θ')}
  ${ox(160, 115)}${T(148, 140, 'Δ', '', 'end')}${rot(160, 115, 92, 195, 245)}${T(...pol(160, 115, 104, 222).map(v => v.toFixed(1)), 'ω')}`,
  'Alternateur')},
'p-meca-ccs-ressort': {legende: 'Deux masses m₁ et m₂ reliées par un ressort (K, l₀), mobiles sur l’axe Ox', svg: svg(360, 140, `
  ${A(20, 105, 345, 105)}${T(348, 109, I('x'), '', 'start')}${L(30, 100, 30, 110)}${T(30, 126, I('O'))}
  ${R(80, 62, 36, 36, 'fillA', 3)}${T(98, 85, sb(I('m'), '1'))}${spring(116, 80, 236, 80, 9, 8)}${R(236, 62, 36, 36, 'fillA', 3)}${T(254, 85, sb(I('m'), '2'))}
  ${L(98, 98, 98, 105, 'dash soft')}${L(254, 98, 254, 105, 'dash soft')}${T(98, 126, sb(I('x'), '1'))}${T(254, 126, sb(I('x'), '2'))}
  ${T(176, 56, I('K') + ', ' + sb(I('l'), '0'))}`,
  'Deux masses et un ressort')},
'n-p1-pendule': {legende: 'Pendule simple de longueur L lâché sans vitesse depuis θ₀ = 60°', svg: svg(320, 240, `
  ${ground(80, 24, 140, true)}${dot(150, 24)}${T(140, 40, I('O'), '', 'end')}${L(150, 24, 150, 200, 'axis')}
  ${arc(150, 24, 140, -150, -30, 'dash soft')}${L(150, 24, ...pol(150, 24, 140, -30), 'thick')}${C(...pol(150, 24, 140, -30), 10, 'fillR')}
  ${T(...pol(150, 24, 140, -30).map((v, k) => (v + (k ? 30 : 0)).toFixed(1)), I('m'))}
  ${arc(150, 24, 46, -90, -30)}${T(...pol(150, 24, 60, -62).map(v => v.toFixed(1)), sb('θ', '0'))}${T(...pol(150, 24, 76, -24).map(v => v.toFixed(1)), I('L'))}
  ${dot(150, 164)}${T(158, 182, 'point bas', 'soft', 'start')}${A(44, 120, 44, 170)}${T(52, 160, V('g'), '', 'start')}`,
  'Pendule simple')},
'n-p2-tige': {legende: 'Tige horizontale tournant à ω autour de Oz ; anneau M libre de glisser, lâché à r₀', svg: svg(340, 230, `
  ${A(170, 205, 170, 18)}${T(178, 24, I('z'), '', 'start')}${R(152, 196, 36, 16, 'fillW', 3)}${T(170, 226, 'moteur', 'soft')}
  ${L(170, 120, 330, 120, 'thick')}${dot(170, 120)}${T(162, 136, I('O'), '', 'end')}${E(250, 120, 6, 13, 'fillR')}${T(262, 146, I('M') + ' (' + I('m') + ')', '', 'start')}
  ${D(170, 96, 250, 96, I('r'), 210, 90)}
  <path d="M146,52 A26,8 0 1 0 194,52" class="s" marker-end="url(#ah)"/>${T(204, 50, 'ω', '', 'start')}
  ${D(170, 182, 330, 182, I('L'), 250, 198)}`,
  'Anneau sur une tige')},
'n-p2-roulement': {legende: 'Cylindre plein et cylindre creux (même m, même R) lâchés en haut d’un plan incliné d’angle α', svg: plan()},
'p-meca-3': {legende: 'Pendule accroché en S au sommet d’un mât fixé sur un plateau tournant à Ω autour de la verticale de S', svg: svg(320, 240, `
  ${E(160, 196, 124, 26, 'fillA')}${L(160, 16, 160, 222, 'axis')}
  ${L(240, 196, 240, 44, 'thick')}${L(240, 44, 160, 44, 'thick')}${dot(160, 44)}${T(152, 40, I('S'), '', 'end')}
  ${L(160, 44, 182, 156)}${C(182, 156, 8, 'fillR')}${T(196, 162, I('M'), '', 'start')}${T(178, 102, I('L'), '', 'start')}
  <path d="M138,24 A22,6 0 1 0 182,24" class="s" marker-end="url(#ah)"/>${T(190, 22, V('Ω'), '', 'start')}${T(254, 120, 'mât', 'soft', 'start')}${T(60, 232, 'plateau', 'soft')}`,
  'Pendule sur plateau tournant')},
'n-p2-marche': {legende: 'Marche de potentiel : V = 0 pour x < 0, V = V₀ pour x > 0 ; électrons d’énergie E venant de x < 0', svg: svg(340, 190, `
  ${A(30, 160, 330, 160)}${T(333, 164, I('x'), '', 'start')}${A(170, 176, 170, 16)}${T(178, 22, I('V'), '', 'start')}${T(162, 176, '0', '', 'end')}
  ${P('M30,160 L170,160 L170,92 L320,92', 'thick r')}${T(300, 84, sb(I('V'), '0'), 'r')}
  ${L(30, 56, 320, 56, 'dash b')}${T(320, 50, I('E'), 'b', 'end')}${A(50, 128, 130, 128, 'b')}${T(90, 120, 'électrons', 'soft')}`,
  'Marche de potentiel')},
'n-p2-voile': {legende: 'Voile plane parfaitement réfléchissante, face au Soleil, recevant le flux φ', svg: svg(340, 190, `
  ${C(42, 95, 26, 'fillY')}${T(42, 140, 'Soleil', 'soft')}
  ${[55, 80, 110, 135].map(y => A(76, y, 238, y, 'r')).join('')}${T(150, 42, 'φ', 'r')}
  ${R(242, 30, 7, 130, 'fillB')}${A(249, 95, 300, 95, 'b')}${T(294, 86, V('n'), 'b')}${T(246, 178, 'voile', 'soft')}`,
  'Voile solaire')},
'n-p1-ultrasons': {legende: 'Émetteurs S₁ et S₂ distants de a ; récepteur M sur une droite parallèle à S₁S₂, à la distance D', svg: svg(340, 230, `
  ${dot(60, 140)}${T(50, 144, sb(I('S'), '1'), '', 'end')}${dot(60, 90)}${T(50, 94, sb(I('S'), '2'), '', 'end')}
  ${L(300, 14, 300, 206, 'thick')}${dot(300, 60, 'r')}${T(310, 64, I('M'), 'r', 'start')}
  ${L(60, 140, 300, 60, 'dash')}${L(60, 90, 300, 60, 'dash')}${L(60, 115, 300, 115, 'axis')}${dot(300, 115)}${T(310, 120, '0', '', 'start')}
  ${A(318, 115, 318, 64)}${T(324, 94, I('x'), '', 'start')}${D(30, 90, 30, 140, I('a'), 22, 120)}${D(60, 220, 300, 220, I('D'), 180, 214)}`,
  'Deux émetteurs')},
'n-p1-lunette': {legende: 'Lunette afocale : objectif L₁ (f′₁), oculaire L₂ (f′₂), avec F′₁ = F₂', svg: svg(360, 180, `
  ${L(10, 90, 350, 90, 'axis')}${lens(60, 90, 116)}${lens(300, 90, 52)}${T(60, 22, sb(I('L'), '1'))}${T(300, 54, sb(I('L'), '2'))}
  ${dot(280, 90)}${T(270, 80, sb(I('F'), '1') + '′ = ' + sb(I('F'), '2'), '', 'end')}
  ${D(60, 154, 280, 154, sb(I('f'), '1') + '′', 170, 148)}${D(280, 130, 300, 130, '', 0, 0)}${T(312, 134, sb(I('f'), '2') + '′', '', 'start')}`,
  'Lunette afocale')},
'n-p1-prisme': {legende: 'Prisme d’angle A et d’indice n : incidence i, réfractions r et r′, émergence i′', svg: prisme()},
'n-p1-projecteur': {legende: 'Projecteur : diapositive près du foyer objet F, lentille convergente (f′), écran à 3,0 m', svg: svg(360, 190, `
  ${L(10, 100, 350, 100, 'axis')}${lens(100, 100, 110)}${T(100, 34, I('L'))}
  ${R(64, 78, 6, 44, 'fillY')}${T(56, 66, 'diapositive', 'soft')}${dot(74, 100)}${T(80, 116, I('F'), '', 'start')}${dot(126, 100)}${T(126, 116, I('F') + '′')}
  ${R(330, 24, 8, 152, 'hatch')}${L(330, 24, 330, 176, 'thick')}${T(330, 16, 'écran', 'soft')}
  ${D(100, 168, 330, 168, '3,0 m', 215, 162)}${T(215, 92, '(échelle non respectée)', 'soft')}`,
  'Projecteur')},
'n-p1-fente': {legende: 'Laser (λ) éclairant une fente de largeur a ; figure de diffraction sur un écran à la distance D', svg: svg(380, 210, `
  ${R(10, 88, 50, 24, 'fillW', 3)}${T(35, 82, 'laser', 'soft')}${A(60, 100, 122, 100, 'r')}${T(92, 92, 'λ', 'r')}
  ${L(130, 18, 130, 93, 'thick')}${L(130, 107, 130, 182, 'thick')}${T(122, 126, I('a'), '', 'end')}
  ${L(130, 100, 330, 100, 'axis')}${L(130, 100, 330, 68, 'dash')}${L(130, 100, 330, 132, 'dash')}${arc(130, 100, 100, 0, 9.1)}${T(240, 97, 'θ')}
  ${R(330, 18, 8, 164, 'hatch')}${L(330, 18, 330, 182, 'thick')}${R(324, 68, 6, 64, 'fillR')}
  ${D(352, 68, 352, 132, I('ℓ'), 366, 104)}${D(130, 198, 330, 198, I('D'), 230, 192)}`,
  'Diffraction par une fente')},
'p-stat-3': {legende: 'Fibre tendue par f : chaîne de N maillons, chacun court (ℓ − a) ou long (ℓ + a)', svg: chaine()},
'n-p1-adiab': {legende: 'Cylindre de moteur Diesel : l’air est comprimé rapidement du volume V₁ au volume V₂ = V₁/10', svg: svg(340, 190, `
  ${L(40, 50, 300, 50, 'thick')}${L(40, 140, 300, 140, 'thick')}${L(40, 50, 40, 140, 'thick')}${R(41, 51, 168, 88, 'fillA')}
  ${T(124, 90, 'air (gaz parfait)')}${T(124, 112, sb(I('P'), '1') + ', ' + sb(I('T'), '1') + ', γ = 1,4', 'soft')}
  ${R(209, 47, 16, 96, 'fillW', 2)}${L(225, 95, 325, 95, 'thick')}${A(318, 74, 268, 74, 'r')}${T(292, 66, 'compression', 'r')}
  ${D(40, 166, 209, 166, sb(I('V'), '1') + ' → ' + sb(I('V'), '2') + ' = ' + sb(I('V'), '1') + '/10', 124, 160)}`,
  'Compression dans un cylindre')},
};
