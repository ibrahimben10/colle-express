// Schémas de correction (1/2) : exercices dont l'énoncé a aussi un schéma.
import { svg, L, A, D, T, I, V, C, R, P, dot, spring, ground, wallV, lens, ox, ot, sb } from './figkit.js';
import { res, cap, coil, gen, arc, rot, E, pol, wav, plot } from './figkit2.js';

const f1 = v => (Math.round(v * 10) / 10).toFixed(1);
const lg = Math.log10;

// Arc en angles « écran » (degrés, y vers le bas).
const arcS = (cx, cy, r, s1, s2, c = '') => {
  const p = s => [cx + r * Math.cos(s * Math.PI / 180), cy + r * Math.sin(s * Math.PI / 180)];
  const [x1, y1] = p(s1), [x2, y2] = p(s2);
  return `<path d="M${f1(x1)},${f1(y1)} A${r},${r} 0 0 ${s2 > s1 ? 1 : 0} ${f1(x2)},${f1(y2)}" class="s ${c}"/>`;
};
const TS = (cx, cy, r, s, t, c = '') => T(f1(cx + r * Math.cos(s * Math.PI / 180)), f1(cy + r * Math.sin(s * Math.PI / 180) + 5), t, c);
const st = (p, s, l) => [p[0] + l * Math.cos(s * Math.PI / 180), p[1] + l * Math.sin(s * Math.PI / 180)];

// Prisme au minimum de déviation (A = 60°, n = 1,5) : trajet symétrique et déviation Dm.
function prismeMin() {
  const rad = Math.PI / 180, n = 1.5, Ad = 60, r = Ad / 2, i = Math.asin(n * Math.sin(r * rad)) / rad, Dm = 2 * i - Ad;
  const S = [180, 34], len = 170, Lb = [S[0] - len / 2, S[1] + len * Math.cos(30 * rad)], Rb = [S[0] + len / 2, Lb[1]];
  const Ip = [S[0] - 100 * Math.sin(30 * rad), S[1] + 100 * Math.cos(30 * rad)], J = [S[0] + 100 * Math.sin(30 * rad), Ip[1]];
  const sIn = 30 - i, sOut = -30 + i;
  const I0 = st(Ip, sIn + 180, 120), J1 = st(J, sOut, 120), Iext = st(Ip, sIn, 150);
  // point de rencontre K de l'incident prolongé et de l'émergent prolongé (sur l'axe de symétrie)
  const K = [S[0], Ip[1] + (S[0] - Ip[0]) * Math.tan(sIn * rad)];
  return svg(360, 230, `
    ${P(`M${S} L${Lb} L${Rb} Z`, 'fillA thick')}${L(S[0], 14, S[0], 220, 'axis')}
    ${L(...st(Ip, 210, 40), ...st(Ip, 30, 40), 'dash soft')}${L(...st(J, -30, 40), ...st(J, 150, 40), 'dash soft')}
    ${A(...I0, ...Ip, 'r')}${L(...Ip, ...J, 'thick r')}${A(...J, ...J1, 'r')}${L(...Ip, ...Iext, 'dash')}
    ${arcS(...K, 60, sOut, sIn)}${TS(...K, 86, (sIn + sOut) / 2 - 4, sb(I('D'), 'm'), 'r')}
    ${arcS(...Ip, 26, sIn + 180, 210)}${TS(...Ip, 40, (sIn + 390) / 2, I('i'))}${arcS(...J, 26, -30, sOut)}${TS(...J, 40, (sOut - 30) / 2, I('i'))}
    ${arcS(...Ip, 24, 0, 30)}${TS(...Ip, 36, 15, I('r'))}${arcS(...J, 24, 150, 180)}${TS(...J, 36, 165, I('r'))}
    ${T(180, 210, 'rayon intérieur parallèle à la base', 'soft')}`, 'Minimum de déviation');
}

// Lunette afocale (échelle non respectée : f′₁ = 200 px, f′₂ = 60 px).
function lunetteRays() {
  const y0 = 90, x1 = 40, xF = 240, x2 = 300, ta = Math.tan(6 * Math.PI / 180), yi = y0 + (xF - x1) * ta;
  let body = '';
  for (const h of [-36, 0, 36]) {
    const yL1 = y0 + h, yL2 = yi + (yi - yL1) * (x2 - xF) / (xF - x1), sl = (y0 - yi) / (x2 - xF);
    body += A(0, yL1 - x1 * ta, x1 - 1, yL1, 'r') + L(x1, yL1, x2, yL2, 'r') + A(x2, yL2, 352, yL2 + sl * 52, 'r');
  }
  return svg(360, 190, `${L(0, y0, 360, y0, 'axis')}${body}${lens(x1, y0, 100)}${lens(x2, y0, 96)}
    ${L(xF, y0, xF, yi, 'thick b')}${dot(xF, yi, 'b')}${T(xF - 4, yi + 20, 'image intermédiaire', 'b', 'end')}
    ${T(x1, 30, sb(I('L'), '1'))}${T(x2, 34, sb(I('L'), '2'))}${dot(xF, y0)}${T(xF + 4, y0 - 8, sb(I('F'), '1') + '′ = ' + sb(I('F'), '2'), '', 'end')}
    ${T(14, 60, 'α', 'r')}${T(346, 60, 'α′', 'r', 'end')}${T(180, 182, '(échelle non respectée)', 'soft')}`, 'Lunette : tracé des rayons');
}

// Projecteur : construction de l'image (échelle non respectée).
function projRays() {
  return svg(360, 200, `${L(10, 130, 350, 130, 'axis')}${lens(110, 130, 76)}
    ${A(60, 130, 60, 154, 'b')}${T(52, 166, I('B'), 'b', 'end')}${T(56, 124, I('A'), '', 'end')}
    ${L(60, 154, 110, 154, 'r')}${L(110, 154, 310, 34, 'r')}${L(60, 154, 310, 34, 'r')}
    ${A(310, 130, 310, 36, 'b')}${T(318, 40, I('B') + '′', 'b', 'start')}${T(318, 146, I('A') + '′', '', 'start')}
    ${dot(70, 130)}${T(74, 146, I('F'), '', 'start')}${dot(150, 130)}${T(154, 146, I('F') + '′', '', 'start')}${dot(110, 130)}${T(102, 146, I('O'), '', 'end')}
    ${T(180, 190, 'diapositive retournée → image à l’endroit, γ < 0', 'soft')}`, 'Projecteur : construction');
}

export const FC1 = {
'n-p2-ailette': {legende: 'Bilan sur la tranche [x, x + dx] : Φ(x) = Φ(x + dx) + h(T − Tₑ)2πa dx ; en dessous, θ = T − Tₑ décroît en e^(−x/δ)', svg: (() => {
  const p = plot(60, 132, 250, 76, [0, 4], [0, 1.08]);
  return svg(360, 236, `
  ${R(40, 40, 290, 30, 'fillA')}${R(160, 40, 50, 30, 'fillR')}${L(40, 55, 340, 55, 'axis')}
  ${A(118, 55, 158, 55, 'r')}${A(212, 55, 252, 55, 'r')}${T(124, 32, 'Φ(' + I('x') + ')', 'r')}${T(248, 32, 'Φ(' + I('x') + ' + d' + I('x') + ')', 'r')}
  ${wav(185, 36, 0, -24)}${wav(185, 74, 0, 22)}${T(200, 108, I('h') + 'θ · 2π' + I('a') + ' d' + I('x'), 'r', 'start')}
  ${L(160, 72, 160, 80)}${L(210, 72, 210, 80)}${T(150, 92, I('x'), '', 'end')}
  ${p.axes(I('x'), 'θ')}${p.f(t => Math.exp(-t), 0, 4)}${L(p.X(0), p.Y(1), p.X(1), p.Y(0), 'dash b')}
  ${T(p.X(1), p.Y(0) + 16, 'δ', 'b')}${T(p.X(0) - 6, p.Y(1) + 4, sb('θ', '0'), '', 'end')}`, 'Bilan sur une tranche d’ailette');
})()},
'p-th-spe1': {legende: 'Tranche [z, z + dz] : conduction axiale (entrée − sortie), effet Joule dans la tranche, pertes latérales β(T − T₀)·2πa dz', svg: svg(360, 210, `
  ${R(40, 60, 280, 60, 'fillA')}${R(150, 60, 60, 60, 'fillR')}${L(30, 90, 340, 90, 'axis')}
  ${A(106, 90, 148, 90, 'r')}${A(212, 90, 254, 90, 'r')}${T(110, 48, sb(I('j'), 'th') + '(' + I('z') + ')·π' + I('a') + '²', 'r')}${T(256, 48, sb(I('j'), 'th') + '(' + I('z') + ' + d' + I('z') + ')·π' + I('a') + '²', 'r')}
  ${T(180, 112, 'Joule', 'soft')}${wav(180, 56, 0, -24)}${wav(180, 124, 0, 24)}
  ${T(180, 166, 'β(' + I('T') + ' − ' + sb(I('T'), '0') + ')·2π' + I('a') + ' d' + I('z'), 'r')}
  ${A(40, 190, 340, 190)}${T(343, 194, I('z'), '', 'start')}${L(150, 185, 150, 195)}${L(210, 185, 210, 195)}${T(150, 206, I('z'))}${T(214, 206, I('z') + ' + d' + I('z'))}`,
  'Bilan sur une tranche de conducteur')},
'p-th-ccmp15': {legende: 'Le flux Φ = P traverse tout cylindre de rayon r ∈ [Rᵢ, Rₑ] (régime permanent, pas de source dans la graisse)', svg: svg(320, 240, `
  ${C(150, 120, 92, 'fillY')}${C(150, 120, 62, 'fillR')}${C(150, 120, 77, 'dash b')}${dot(150, 120)}
  ${[20, 110, 200, 290].map(a => A(...pol(150, 120, 66, a), ...pol(150, 120, 106, a), 'r')).join('')}
  ${A(150, 120, ...pol(150, 120, 77, 135), 'b')}${T(122, 106, I('r'), 'b', 'end')}${T(150, 136, sb(I('T'), 'i') + ' en ' + sb(I('R'), 'i'))}
  ${T(...pol(150, 120, 112, 30).map(f1), 'Φ = ' + I('P'), 'r', 'start')}${T(300, 226, sb(I('T'), 'e') + ' en ' + sb(I('R'), 'e'), 'b', 'end')}`,
  'Flux radial dans la graisse')},
'n-p2-isolant': {legende: 'Flux perdu Φ en fonction du rayon extérieur r₂ (r₁ = 1 mm) : maximum pour r₂ = r_c = λ/h = 20 mm', svg: (() => {
  const g = r => 1 / (5 * Math.log(r) + 100 / r), gm = g(20), p = plot(50, 30, 270, 130, [0, 80], [0, 1.1]);
  return svg(360, 200, `${p.axes(sb(I('r'), '2') + ' (mm)', 'Φ / ' + sb('Φ', 'max'))}${p.f(r => g(r) / gm, 1, 80)}
    ${p.vline(20)}${dot(p.X(20), p.Y(1), 'r')}${T(p.X(20) + 6, p.Y(1) - 8, sb(I('r'), 'c') + ' = λ/' + I('h'), 'r', 'start')}
    ${dot(p.X(1), p.Y(g(1) / gm))}${T(p.X(1) + 8, p.Y(g(1) / gm) + 4, 'fil nu', 'soft', 'start')}${T(p.X(20), p.Y(0) + 16, '20')}${T(p.X(80), p.Y(0) + 16, '80')}
    ${T(250, 196, 'gaine fine : elle augmente les pertes', 'soft')}`, 'Rayon critique');
})()},
'n-p1-rc': {legende: 'Charge : u_C = E(1 − e^(−t/τ)) et i = (E/R) e^(−t/τ) ; la tangente à l’origine coupe E en t = τ ; 99 % en 4,6 τ', svg: (() => {
  const p = plot(50, 24, 270, 140, [0, 5.2], [0, 1.1]);
  return svg(360, 200, `${p.axes(I('t') + '/τ', '')}${p.hline(1)}${T(p.X(0) - 6, p.Y(1) + 4, I('E'), '', 'end')}
    ${p.f(t => 1 - Math.exp(-t), 0, 5.2)}${p.f(t => Math.exp(-t), 0, 5.2, 'thick b')}${L(p.X(0), p.Y(0), p.X(1), p.Y(1), 'dash')}
    ${p.vline(1)}${T(p.X(1), p.Y(0) + 16, 'τ')}${dot(p.X(4.6), p.Y(.99), 'r')}${T(p.X(4.6), p.Y(0) + 16, '4,6τ')}
    ${T(p.X(2.6), p.Y(.93) + 4, sb(I('u'), 'C'), 'r')}${T(p.X(2.2), p.Y(.2), I('Ri'), 'b')}`, 'Charge du condensateur');
})()},
'n-p1-passebande': {legende: 'Gain en décibels du passe-bande (Q = 10) : maximum 0 dB en f₀, bande passante à −3 dB de largeur Δf = f₀/Q', svg: (() => {
  const Q = 10, G = x => -10 * lg(1 + Q * Q * (x - 1 / x) ** 2), p = plot(50, 20, 280, 150, [lg(.5), lg(2)], [-30, 3]);
  const xm = (Math.sqrt(1 + 4 * Q * Q) - 1) / (2 * Q), xp = (Math.sqrt(1 + 4 * Q * Q) + 1) / (2 * Q);
  return svg(360, 210, `${p.axes('log ' + I('f'), sb(I('G'), 'dB'), lg(.5), 0)}${p.f(t => G(10 ** t), lg(.5), lg(2))}
    ${p.hline(-3)}${T(p.X(lg(2)) + 4, p.Y(-3) + 4, '−3 dB', 'soft', 'start')}${p.vline(lg(xm))}${p.vline(lg(xp))}
    ${D(p.X(lg(xm)), p.Y(-12), p.X(lg(xp)), p.Y(-12), '', 0, 0)}${T(p.X(lg(xp)) + 8, p.Y(-12) + 4, 'Δ' + I('f') + ' = ' + sb(I('f'), '0') + '/' + I('Q'), 'b', 'start')}
    ${T(p.X(0), p.Y(-30) + 16, sb(I('f'), '0'))}${T(p.X(lg(.5)) + 12, p.Y(-30) + 16, sb(I('f'), '0') + '/2')}${T(p.X(lg(2)), p.Y(-30) + 16, '2' + sb(I('f'), '0'))}`, 'Diagramme de Bode du passe-bande');
})()},
'n-p1-passebas': {legende: 'Bode en gain du passe-bas (f_c ≈ 1,6 kHz) : asymptotes 0 dB puis −20 dB/décade ; f₁ = 100 Hz passe, f₂ = 20 kHz est atténuée d’environ 22 dB', svg: (() => {
  const fc = 1 / (2 * Math.PI * 1e-4), G = f => -10 * lg(1 + (f / fc) ** 2), p = plot(50, 20, 280, 150, [1, 5], [-42, 6]);
  return svg(360, 210, `${p.axes('log ' + I('f'), sb(I('G'), 'dB'), 1, 0)}
    ${L(p.X(1), p.Y(0), p.X(lg(fc)), p.Y(0), 'dash b')}${L(p.X(lg(fc)), p.Y(0), p.X(5), p.Y(-20 * (5 - lg(fc))), 'dash b')}${p.f(t => G(10 ** t), 1, 5)}
    ${p.vline(lg(fc))}${T(p.X(lg(fc)), p.Y(-42) + 16, sb(I('f'), 'c'))}${T(p.X(lg(fc)) + 40, p.Y(-30), '−20 dB/déc', 'b')}
    ${dot(p.X(2), p.Y(G(100)))}${T(p.X(2), p.Y(G(100)) - 10, sb(I('f'), '1'))}${dot(p.X(lg(2e4)), p.Y(G(2e4)))}${T(p.X(lg(2e4)) + 8, p.Y(G(2e4)) - 6, sb(I('f'), '2') + ' : −22 dB', '', 'start')}
    ${T(p.X(1), p.Y(-42) + 16, '10 Hz')}${T(p.X(5), p.Y(-42) + 16, '100 kHz')}`, 'Diagramme de Bode du passe-bas');
})()},
'n-p1-rlc': {legende: 'Régime pseudo-périodique (Q = 5) : q(t) oscille dans l’enveloppe ±q₀e^(−t/τ) ; pseudo-période T ≈ 0,63 ms, rapport de deux maxima e^(−0,63) ≈ 0,53', svg: (() => {
  const al = 1000, W = Math.sqrt(1e8 - al * al), Tp = 2 * Math.PI / W * 1e3, q = t => Math.exp(-al * t / 1e3) * (Math.cos(W * t / 1e3) + al / W * Math.sin(W * t / 1e3));
  const p = plot(40, 26, 290, 150, [0, 3.2], [-1.05, 1.1]);
  return svg(360, 210, `${p.axes(I('t') + ' (ms)', I('q') + '/' + sb(I('q'), '0'))}${p.f(t => Math.exp(-al * t / 1e3), 0, 3.2, 'dash b')}${p.f(t => -Math.exp(-al * t / 1e3), 0, 3.2, 'dash b')}
    ${p.f(q, 0, 3.2, 'thick r', 300)}${dot(p.X(Tp), p.Y(q(Tp)))}${dot(p.X(2 * Tp), p.Y(q(2 * Tp)))}
    ${D(p.X(Tp), p.Y(1), p.X(2 * Tp), p.Y(1), I('T'), (p.X(Tp) + p.X(2 * Tp)) / 2, p.Y(1) - 6)}${T(p.X(3), p.Y(.25), 'enveloppe', 'b', 'end')}`, 'Régime libre du RLC');
})()},
'n-p2-coax': {legende: 'Lignes de champ : E radial (de l’âme vers la gaine), B orthoradial ; le cylindre de Gauss et le contour d’Ampère ont le rayon r', svg: svg(300, 240, `
  ${C(150, 115, 96, 'fillB')}${C(150, 115, 88, 'fillA')}${C(150, 115, 26, 'fillB')}${dot(150, 115)}
  ${[0, 45, 90, 135, 180, 225, 270, 315].map(a => A(...pol(150, 115, 30, a + 22), ...pol(150, 115, 84, a + 22), 'r')).join('')}
  ${C(150, 115, 58, 'dash b')}${[60, 180, 300].map(a => rot(150, 115, 58, a, a + 28, 'b')).join('')}
  ${T(150, 112, '⊙ ' + I('I'))}${T(294, 24, V('E') + ' radial', 'r', 'end')}${T(294, 232, V('B') + ' orthoradial', 'b', 'end')}${T(150, 50, I('r'), 'b')}`, 'Câble coaxial : lignes de champ')},
'n-p2-dipole': {legende: 'Équilibre stable : p aligné sur le champ de l’ion (θ = 0) ; la force sur le dipôle est dirigée vers l’ion (attractive)', svg: svg(360, 170, `
  ${C(70, 90, 13, 'fillR')}${T(70, 95, '+', 'r')}${T(70, 126, 'Na⁺', 'r')}${L(83, 90, 340, 90, 'dash soft')}
  ${C(250, 90, 16, 'fillW')}${A(226, 90, 280, 90, 'b')}${T(272, 80, V('p'), 'b')}${A(250, 120, 310, 120, 'r')}${T(302, 140, V('E') + ' de l’ion', 'r', 'end')}
  ${A(240, 58, 180, 58)}${T(210, 48, V('F') + ' (attraction)')}${D(70, 156, 250, 156, I('r'), 160, 150)}`, 'Dipôle à l’équilibre')},
'n-p2-peau': {legende: 'Dans le cuivre, E décroît comme e^(−z/δ) et se déphase avec z ; deux instants (trait plein, pointillé) dans l’enveloppe ±E₀e^(−z/δ)', svg: (() => {
  const p = plot(40, 20, 290, 160, [0, 5], [-1.05, 1.1]);
  return svg(360, 210, `${p.axes(I('z'), I('E') + '/' + sb(I('E'), '0'))}${p.f(z => Math.exp(-z), 0, 5, 'dash b')}${p.f(z => -Math.exp(-z), 0, 5, 'dash b')}
    ${p.f(z => Math.exp(-z) * Math.cos(z), 0, 5)}${p.f(z => Math.exp(-z) * Math.sin(z), 0, 5, 'dash r')}
    ${p.vline(1)}${T(p.X(1), p.Y(-1.05) + 16, 'δ')}${dot(p.X(1), p.Y(Math.exp(-1)), 'b')}${T(p.X(1) + 6, p.Y(Math.exp(-1)) - 6, '1/e', 'b', 'start')}`, 'Effet de peau');
})()},
'n-p1-bobine': {legende: 'Quand B croît, e < 0 et i < 0 : le courant tourne dans le sens opposé à celui associé à n, et son champ propre s’oppose à B (loi de Lenz)', svg: svg(320, 200, `
  ${[0, 5, 10].map(d => E(150 + d, 100, 16, 62, d ? '' : 'fillA')).join('')}${L(30, 100, 300, 100, 'axis')}
  ${[40, 170].map(y => A(30, y, 290, y, 'b')).join('')}${T(290, 28, V('B') + ' croît', 'b', 'end')}
  ${A(176, 100, 230, 100)}${T(226, 92, V('n'))}${A(140, 112, 86, 112, 'r')}${T(96, 130, sb(V('B'), 'induit'), 'r')}
  ${ot(155, 38)}${ox(155, 162)}${T(176, 30, I('i') + ' < 0', 'r', 'start')}`, 'Loi de Lenz')},
'n-p1-rails': {legende: 'Pour v > 0 : i < 0, le courant circule dans la barre selon −u_y ; la force de Laplace i ℓ u_y ∧ B est opposée à v et freine la barre', svg: svg(360, 200, `
  ${L(40, 50, 340, 50, 'thick')}${L(40, 150, 340, 150, 'thick')}${L(40, 50, 40, 82)}${res(40, 100, false)}${L(40, 118, 40, 150)}${T(24, 104, I('R'), '', 'end')}
  ${R(226, 42, 8, 116, 'fillR', 2)}${A(240, 120, 290, 120)}${T(266, 112, V('v'))}${A(220, 80, 166, 80, 'b')}${T(190, 70, sb(V('F'), 'L'), 'b')}
  ${A(230, 70, 230, 132, 'r')}${A(140, 50, 180, 50, 'r')}${A(180, 150, 120, 150, 'r')}${A(40, 140, 40, 124, 'r')}${T(250, 160, I('i'), 'r')}
  ${ox(300, 80)}${T(300, 106, V('B'), 'b')}${A(300, 176, 330, 176)}${T(334, 180, sb(V('u'), 'x'), '', 'start')}${A(300, 176, 300, 160)}${T(286, 166, sb(V('u'), 'y'), '', 'end')}`, 'Courant induit et force de Laplace')},
'n-p1-transfo': {legende: 'Vu du primaire, le secondaire chargé par R équivaut à R′ = R/m² = R(N₁/N₂)² ≈ 2,2 kΩ', svg: svg(380, 170, `
  ${coil(110, 85, false, 4, 48)}${coil(150, 85, false, 4, 48)}${L(126, 55, 126, 115, 'thick')}${L(134, 55, 134, 115, 'thick')}
  ${L(40, 61, 110, 61)}${L(40, 109, 110, 109)}${L(150, 61, 210, 61)}${L(150, 109, 210, 109)}${L(210, 61, 210, 67)}${res(210, 85, false)}${L(210, 103, 210, 109)}
  ${C(40, 61, 4, 'fillW')}${C(40, 109, 4, 'fillW')}${A(28, 104, 28, 66, 'b')}${T(20, 90, sb(I('u'), '1'), 'b', 'end')}${T(228, 90, I('R'), '', 'start')}
  ${T(110, 40, sb(I('N'), '1'))}${T(150, 40, sb(I('N'), '2'))}${T(262, 90, '⟺', '')}
  ${L(300, 61, 340, 61)}${L(300, 109, 340, 109)}${L(340, 61, 340, 67)}${res(340, 85, false)}${L(340, 103, 340, 109)}${C(300, 61, 4, 'fillW')}${C(300, 109, 4, 'fillW')}
  ${A(290, 104, 290, 66, 'b')}${T(358, 90, I('R') + '′', '', 'start')}${T(190, 150, 'm = ' + sb(I('N'), '2') + '/' + sb(I('N'), '1') + ' ≈ 0,052', 'soft')}`, 'Résistance ramenée au primaire')},
'n-p2-alternateur': {legende: 'Flux Φ = NBS cos ωt et f.é.m. e = NBSω sin ωt (en quadrature) ; le courant i est en retard sur e (tan φ = Lω/R)', svg: (() => {
  const p = plot(40, 24, 290, 150, [0, 4 * Math.PI], [-1.15, 1.2]), ph = .7;
  return svg(360, 210, `${p.axes('ω' + I('t'), '')}${p.f(Math.cos, 0, 4 * Math.PI, 'thick b')}${p.f(Math.sin, 0, 4 * Math.PI)}${p.f(t => .6 * Math.sin(t - ph), 0, 4 * Math.PI, 'dash r')}
    ${T(p.X(.15), p.Y(1) - 8, 'Φ', 'b', 'start')}${T(p.X(Math.PI / 2), p.Y(1) - 8, I('e'), 'r')}${T(p.X(Math.PI / 2 + ph) + 8, p.Y(.6) + 18, I('i'), 'r', 'start')}
    ${T(p.X(2 * Math.PI), p.Y(-1.15) + 16, '2π')}${T(p.X(4 * Math.PI), p.Y(-1.15) + 16, '4π')}`, 'Flux et force électromotrice');
})()},
'p-meca-ccs-ressort': {legende: 'Ressort allongé (X > l₀) : il tire m₁ vers +u_x et m₂ vers −u_x avec des forces opposées de norme K(X − l₀)', svg: svg(360, 150, `
  ${A(20, 112, 345, 112)}${T(348, 116, I('x'), '', 'start')}
  ${R(70, 62, 36, 36, 'fillA', 3)}${T(88, 85, sb(I('m'), '1'))}${spring(106, 80, 246, 80, 11, 8)}${R(246, 62, 36, 36, 'fillA', 3)}${T(264, 85, sb(I('m'), '2'))}
  ${A(88, 50, 138, 50, 'r')}${T(114, 40, '+' + I('K') + '(' + I('X') + ' − ' + sb(I('l'), '0') + ')', 'r')}${A(264, 50, 214, 50, 'r')}${T(238, 40, '−' + I('K') + '(' + I('X') + ' − ' + sb(I('l'), '0') + ')', 'r')}
  ${D(88, 132, 264, 132, I('X') + ' = ' + sb(I('x'), '2') + ' − ' + sb(I('x'), '1'), 176, 146)}`, 'Forces du ressort')},
'n-p1-pendule': {legende: 'À l’angle θ : base polaire (u_r, u_θ), tension T dirigée vers O, poids mg vertical', svg: (() => {
  const O = [150, 30], th = 35, M = st(O, 90 - th, 150), ur = st(M, 90 - th, 38), ut = st(M, -th, 38);
  return svg(320, 250, `${ground(80, 30, 140, true)}${dot(...O)}${T(140, 46, I('O'), '', 'end')}${L(150, 30, 150, 210, 'axis')}
    ${L(...O, ...M, 'thick')}${C(...M, 9, 'fillR')}${arcS(...O, 50, 90 - th, 90)}${TS(...O, 64, 90 - th / 2, 'θ')}
    ${A(...M, ...ur)}${T(ur[0] + 6, ur[1] + 12, sb(V('u'), 'r'), '', 'start')}${A(...M, ...ut)}${T(ut[0] + 6, ut[1], sb(V('u'), 'θ'), '', 'start')}
    ${A(...M, ...st(M, 270 - th, 62), 'b')}${T(...st(M, 270 - th, 74).map(f1), V('T'), 'b')}${A(...M, M[0], M[1] + 66, 'r')}${T(M[0] - 8, M[1] + 60, I('m') + V('g'), 'r', 'end')}`, 'Forces sur le pendule');
})()},
'n-p2-tige': {legende: 'Vue de dessus dans le référentiel de la tige : force axifuge selon u_r, Coriolis −2mωṙ u_θ compensée par R_θ (poids et R_z, verticaux, non représentés)', svg: svg(340, 200, `
  ${L(90, 110, 330, 110, 'thick')}${ox(90, 110)}${T(80, 130, I('O') + ', ' + V('ω'), '', 'end')}${rot(90, 110, 30, 200, 330)}
  ${E(230, 110, 6, 12, 'fillR')}${A(238, 110, 300, 110, 'r')}${T(296, 98, I('m') + 'ω²' + I('r'), 'r')}
  ${A(230, 118, 230, 172, 'r')}${T(238, 166, '−2' + I('m') + 'ω' + I('ṙ'), 'r', 'start')}${A(230, 102, 230, 46, 'b')}${T(238, 54, sb(I('R'), 'θ'), 'b', 'start')}
  ${A(280, 180, 316, 180)}${T(320, 184, sb(V('u'), 'r'), '', 'start')}${A(280, 180, 280, 146)}${T(272, 152, sb(V('u'), 'θ'), '', 'end')}${D(90, 82, 230, 82, I('r'), 160, 76)}`, 'Forces dans le référentiel tournant')},
'n-p2-roulement': {legende: 'Forces sur un cylindre : poids mg en G, réaction normale N et frottement T (vers le haut de la pente) au contact I ; v = Rω', svg: (() => {
  const O = [20, 50], B = [340, 200], len = Math.hypot(B[0] - O[0], B[1] - O[1]), u = [(B[0] - O[0]) / len, (B[1] - O[1]) / len], n = [u[1], -u[0]], Rr = 38;
  const al = Math.atan2(B[1] - O[1], B[0] - O[0]) * 180 / Math.PI, Ip = [O[0] + 150 * u[0], O[1] + 150 * u[1]], G = [Ip[0] + Rr * n[0], Ip[1] + Rr * n[1]];
  return svg(360, 220, `${P(`M${O} L${B} L20,200 Z`, 'fillW')}${ground(10, 200, 340)}${C(...G, Rr, 'fillA')}${dot(...G)}${dot(...Ip)}
    ${T(G[0] - 8, G[1] - 6, I('G'), '', 'end')}${T(Ip[0] - 6, Ip[1] + 16, I('I'), '', 'end')}
    ${A(...G, G[0], G[1] + 70, 'r')}${T(G[0] + 6, G[1] + 66, I('m') + V('g'), 'r', 'start')}
    ${A(...Ip, Ip[0] + 70 * n[0], Ip[1] + 70 * n[1], 'b')}${T(Ip[0] + 80 * n[0] - 16, Ip[1] + 80 * n[1] + 4, V('N'), 'b')}
    ${A(...Ip, Ip[0] - 46 * u[0], Ip[1] - 46 * u[1], 'b')}${T(Ip[0] - 58 * u[0], Ip[1] - 58 * u[1] + 14, V('T'), 'b')}
    ${A(G[0] + 44 * u[0], G[1] + 44 * u[1], G[0] + 96 * u[0], G[1] + 96 * u[1])}${T(G[0] + 96 * u[0] + 4, G[1] + 96 * u[1] - 10, V('v'))}
    ${rot(...G, 24, 200, 100)}${T(G[0] - 30, G[1] - 14, 'ω')}${arcS(340, 200, 50, 180, 180 + al)}${TS(340, 200, 64, 180 + al / 2, 'α')}`, 'Forces sur le cylindre');
})()},
'p-meca-3': {legende: 'Vue de dessus (référentiel du plateau) : rappel du fil −(mg/L) r u_r, force centrifuge mΩ² r u_r, Coriolis −2mΩ u_z ∧ v′, perpendiculaire à la vitesse relative v′', svg: (() => {
  const O = [110, 140], M = st(O, -30, 130), ur = st(M, -30, 40), ut = st(M, -120, 40);
  return svg(340, 230, `${ox(...O)}${T(O[0] - 10, O[1] + 20, I('O') + ', ' + V('Ω'), '', 'end')}${L(...O, ...M, 'dash soft')}${arcS(...O, 40, -30, 0)}${TS(...O, 54, -15, 'θ')}${L(...O, O[0] + 60, O[1], 'dash soft')}
    ${C(...M, 7, 'fillR')}${T(M[0] + 2, M[1] + 24, I('M'), '', 'start')}
    ${A(...M, ...st(M, 150, 70), 'b')}${T(...st(M, 150, 84).map(f1), V('f'), 'b')}${A(...M, ...st(M, -30, 26), 'r')}${T(...st(M, -30, 40).map(f1), I('m') + 'Ω²' + I('r'), 'r')}
    ${A(...M, ...st(M, 210, 48), 'dash')}${T(...st(M, 210, 62).map(f1), V('v') + '′')}${A(...M, ...st(M, 300, 56), 'r')}${T(...st(M, 300, 70).map(f1), sb(V('f'), 'ic'), 'r')}`, 'Forces dans le plan horizontal');
})()},
'n-p2-marche': {legende: 'E > V₀ : onde incidente et réfléchie (k₁) à gauche, onde transmise (k₂ < k₁, longueur d’onde plus grande) à droite. E < V₀ : onde évanescente en e^(−κx)', svg: (() => {
  const k1 = 2 * Math.PI / 36, k2 = k1 / Math.SQRT2;
  const w = (x0, x1, y, k, a) => { let d = ''; for (let x = x0; x <= x1; x += 1.5) d += (d ? ' L' : 'M') + f1(x) + ',' + f1(y - a * Math.sin(k * (x - 170))); return P(d, 'r'); };
  const ke = 2 * Math.PI / 60, ka = ke / 2, ph = Math.atan(ka / ke);
  let ev = '', ev2 = ''; for (let x = 170; x <= 320; x += 2) ev += (ev ? ' L' : 'M') + f1(x) + ',' + f1(200 - 20 * Math.cos(ph) * Math.exp(-ka * (x - 170)));
  for (let x = 30; x <= 170; x += 1.5) ev2 += (ev2 ? ' L' : 'M') + f1(x) + ',' + f1(200 - 20 * Math.cos(ke * (x - 170) + ph));
  return svg(360, 240, `${T(14, 22, I('E') + ' > ' + sb(I('V'), '0'), 'soft', 'start')}${L(30, 100, 170, 100)}${L(170, 100, 170, 70)}${L(170, 70, 330, 70)}${L(170, 20, 170, 222, 'axis')}
    ${w(30, 168, 56, k1, 14)}${w(172, 330, 38, k2, 14)}${A(60, 92, 120, 92, 'b')}${T(90, 84, 'incidente + réfléchie', 'b')}${A(220, 62, 290, 62, 'b')}${T(254, 92, 'transmise', 'b')}
    ${T(90, 120, sb(I('k'), '1'))}${T(254, 108, sb(I('k'), '2') + ' < ' + sb(I('k'), '1'))}
    ${T(14, 142, I('E') + ' < ' + sb(I('V'), '0'), 'soft', 'start')}${L(30, 200, 330, 200, 'soft')}${P(ev2, 'r')}${P(ev, 'r')}${T(250, 182, 'e^(−κ' + I('x') + ')', 'r')}${T(100, 236, 'onde stationnaire, réflexion totale', 'soft')}`, 'Ondes de part et d’autre de la marche');
})()},
'n-p2-voile': {legende: 'Chaque photon arrive avec ε/c et repart avec −ε/c : la voile reçoit 2ε/c ; d’où la pression P = 2φ/c', svg: svg(340, 180, `
  ${R(242, 20, 7, 140, 'fillB')}${A(60, 60, 236, 60, 'r')}${T(150, 50, '+ε/' + I('c'), 'r')}${A(236, 100, 60, 100, 'r')}${T(150, 90, '−ε/' + I('c') + ' (réfléchi)', 'r')}
  ${A(252, 80, 318, 80, 'b')}${T(290, 70, '+2ε/' + I('c'), 'b')}${T(286, 132, V('F') + ' = 2φ' + I('S') + '/' + I('c'), 'b')}${T(36, 160, 'Soleil →', 'soft', 'start')}`, 'Quantité de mouvement transférée')},
'n-p1-ultrasons': {legende: 'Amplitude du signal reçu le long de la droite : maxima où δ = ax/D = pλ, séparés de l’interfrange i = λD/a ≈ 17 cm', svg: (() => {
  const i0 = .17, p = plot(30, 30, 300, 120, [-.42, .42], [0, 1.15]);
  return svg(360, 200, `${p.axes(I('x') + ' (m)', 'amplitude', 0, 0)}${p.f(x => Math.abs(Math.cos(Math.PI * x / i0)), -.42, .42, 'thick r', 300)}
    ${[-2, -1, 0, 1, 2].map(k => T(p.X(k * i0), p.Y(1) - 8, I('p') + ' = ' + k, 'soft')).join('')}
    ${D(p.X(0), p.Y(0) + 24, p.X(i0), p.Y(0) + 24, I('i'), p.X(i0 / 2), p.Y(0) + 42)}`, 'Maxima d’amplitude');
})()},
'n-p1-lunette': {legende: 'Un faisceau parallèle incliné de α converge dans le plan focal F′₁ = F₂ (image intermédiaire renversée) puis ressort parallèle, incliné de α′ : G = α′/α = −f′₁/f′₂', svg: lunetteRays()},
'n-p1-prisme': {legende: 'Au minimum de déviation, le trajet est symétrique : i = i′, r = r′ = A/2 et Dm = 2i − A ≈ 37°', svg: prismeMin()},
'n-p1-projecteur': {legende: 'Construction de l’image : rayon parallèle à l’axe (ressort par F′) et rayon passant par O ; l’image est renversée et agrandie', svg: projRays()},
'n-p1-fente': {legende: 'Éclairement sur l’écran : tache centrale entre les premières annulations X = ±λD/a, de largeur ℓ = 2λD/a', svg: (() => {
  const p = plot(30, 24, 300, 130, [-3.3, 3.3], [0, 1.1]), s = u => u === 0 ? 1 : (Math.sin(Math.PI * u) / (Math.PI * u)) ** 2;
  return svg(360, 200, `${p.axes(I('X'), I('I') + '/' + sb(I('I'), '0'), 0, 0)}${p.f(s, -3.3, 3.3, 'thick r', 400)}
    ${T(p.X(-1), p.Y(0) + 16, '−λ' + I('D') + '/' + I('a'))}${T(p.X(1), p.Y(0) + 16, 'λ' + I('D') + '/' + I('a'))}
    ${D(p.X(-1), p.Y(0) + 30, p.X(1), p.Y(0) + 30, I('ℓ'), p.X(0) + 14, p.Y(0) + 44)}`, 'Figure de diffraction');
})()},
'p-stat-3': {legende: 'Longueur à l’équilibre : 𝓛 = 𝓛₀ + Na th(af/k_BT) ; loi de Hooke (pente à l’origine) pour af ≪ k_BT, saturation à 𝓛₀ ± Na', svg: (() => {
  const p = plot(40, 24, 290, 150, [-3, 3], [-1.25, 1.25]);
  return svg(360, 200, `${p.axes(I('f'), '𝓛', 0, 0)}${p.hline(1)}${p.hline(-1)}${p.f(Math.tanh, -3, 3)}${L(p.X(-1.15), p.Y(-1.15), p.X(1.15), p.Y(1.15), 'dash b')}
    ${T(p.X(-3), p.Y(1) - 6, sb('𝓛', '0') + ' + ' + I('Na'), 'soft', 'start')}${T(p.X(3), p.Y(-1) + 16, sb('𝓛', '0') + ' − ' + I('Na'), 'soft', 'end')}
    ${T(p.X(0) - 6, p.Y(0) + 16, sb('𝓛', '0'), '', 'end')}${T(p.X(1.2) + 4, p.Y(1.2) + 18, 'Hooke', 'b', 'start')}`, 'Élasticité entropique');
})()},
'n-p1-adiab': {legende: 'Compression de V₁ à V₁/10 : l’adiabatique réversible (PVᵞ = cste) monte plus haut que l’isotherme ; le travail reçu est l’aire sous la courbe', svg: (() => {
  const p = plot(50, 20, 270, 150, [0, 1.05], [0, 27]);
  const ad = v => v ** -1.4, iso = v => 1 / v;
  let area = `M${f1(p.X(.1))},${f1(p.Y(0))}`; for (let k = 0; k <= 60; k++) { const v = .1 + .9 * k / 60; area += ` L${f1(p.X(v))},${f1(p.Y(ad(v)))}`; } area += ` L${f1(p.X(1))},${f1(p.Y(0))} Z`;
  return svg(360, 210, `<path d="${area}" class="fillR" style="stroke:none"/>${p.axes(I('V') + '/' + sb(I('V'), '1'), I('P') + ' (bar)')}${p.f(ad, .1, 1)}${p.f(iso, .1, 1, 'thick b')}
    ${dot(p.X(1), p.Y(1))}${T(p.X(1) + 6, p.Y(1) - 6, '1', '', 'start')}${dot(p.X(.1), p.Y(ad(.1)), 'r')}${T(p.X(.1) + 8, p.Y(ad(.1)) + 4, '2 : 25 bar, 736 K', 'r', 'start')}
    ${dot(p.X(.1), p.Y(10))}${T(p.X(.1) + 8, p.Y(10) + 4, 'isotherme : 10 bar', 'b', 'start')}${T(p.X(.1), p.Y(0) + 16, '0,1')}${T(p.X(1), p.Y(0) + 16, '1')}`, 'Compression adiabatique et isotherme');
})()},
};
