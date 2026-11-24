// Schémas de correction (2/2) : exercices sans schéma d'énoncé.
import { svg, L, A, D, T, I, V, C, R, P, dot, ground, wallV, ox, ot, sb } from './figkit.js';
import { arc, rot, E, pol, wav, plot } from './figkit2.js';

const f1 = v => (Math.round(v * 10) / 10).toFixed(1);
const path = pts => P(pts.map((p, i) => (i ? 'L' : 'M') + f1(p[0]) + ',' + f1(p[1])).join(' '), '');
const pathC = (pts, c) => P(pts.map((p, i) => (i ? 'L' : 'M') + f1(p[0]) + ',' + f1(p[1])).join(' '), c);
const rng = (a, b, n) => Array.from({length: n + 1}, (_, i) => a + (b - a) * i / n);

export const FC2 = {
'n-p2-diffusion': {legende: 'Profils n(x, t) à trois instants t₁, 4t₁ et 16t₁ : le pic s’abaisse et s’étale en √(2Dt) (la largeur double quand t quadruple)', svg: (() => {
  const p = plot(30, 20, 300, 140, [-10, 10], [0, 1.08]), g = s => x => Math.exp(-x * x / (2 * s * s)) / s;
  return svg(360, 200, `${p.axes(I('x'), I('n'), 0, 0)}${p.f(g(1), -10, 10)}${p.f(g(2), -10, 10, 'thick b')}${p.f(g(4), -10, 10, 'dash')}
    ${T(p.X(1.2), p.Y(.9), sb(I('t'), '1'), 'r', 'start')}${T(p.X(2.6), p.Y(.42), '4' + sb(I('t'), '1'), 'b', 'start')}${T(p.X(6), p.Y(.2), '16' + sb(I('t'), '1'), '', 'start')}
    ${D(p.X(0), p.Y(g(4)(4)), p.X(4), p.Y(g(4)(4)), '', 0, 0)}${T(p.X(4) + 8, p.Y(g(4)(4)) + 4, '√(2' + I('Dt') + ')', '', 'start')}`, 'Étalement par diffusion');
})()},
'p-th-spe5': {legende: 'Température en profondeur : oscillation autour de T_m, amortie en e^(−x/δ) et retardée ; deux instants dans l’enveloppe T_m ± T₀e^(−x/δ)', svg: (() => {
  // profondeur vers le bas : x ∈ [0, 4δ] sur 150 px ; T horizontal, T_m au centre
  const X0 = 180, Y0 = 30, H = 156, Wd = 120, y = x => Y0 + x / 3 * H, tx = v => X0 + v * Wd;
  const cur = (fn, c) => pathC(rng(0, 3, 120).map(x => [tx(fn(x)), y(x)]), c);
  return svg(360, 220, `${L(30, Y0, 330, Y0, 'thick')}${R(30, Y0 - 10, 300, 10, 'fillY')}${T(36, Y0 - 14, 'surface', 'soft', 'start')}
    ${A(X0, Y0, X0, 196)}${T(X0 + 6, 200, I('x') + ' (profondeur)', '', 'start')}
    ${cur(x => Math.exp(-x), 'dash b')}${cur(x => -Math.exp(-x), 'dash b')}${cur(x => Math.exp(-x) * Math.cos(x), 'thick r')}${cur(x => Math.exp(-x) * Math.cos(x - Math.PI), 'dash r')}
    ${L(30, y(1), 330, y(1), 'dash soft')}${T(330, y(1) - 4, 'δ', '', 'end')}${T(tx(1), Y0 + 16, sb(I('T'), 'm') + ' + ' + sb(I('T'), '0'), 'soft', 'end')}${T(tx(-1), Y0 + 16, sb(I('T'), 'm') + ' − ' + sb(I('T'), '0'), 'soft', 'start')}
    ${T(X0 + 30, y(2.6), sb(I('T'), 'm') + ' : cave', 'b', 'start')}`, 'Onde thermique dans le sol');
})()},
'n-p2-fourier': {legende: 'Pour f ≫ f_c, le filtre intègre : s = (1/τ)∫e dt. Le créneau donne un triangle en phase (s croît quand e = +E), de crête à crête πEf_c/f ≈ 0,16E', svg: (() => {
  const sq = t => (t % 1) < .5 ? 1 : -1, tri = t => { const u = t % 1; return u < .5 ? -1 + 4 * u : 3 - 4 * u; };
  const pe = plot(40, 14, 290, 70, [0, 2.2], [-1.2, 1.2]), ps = plot(40, 116, 290, 70, [0, 2.2], [-1.2, 1.2]);
  return svg(360, 210, `${pe.axes(I('t'), I('e'), 0, 0)}${pe.f(sq, 0, 2.2, 'thick b', 600)}${T(pe.X(0) - 6, pe.Y(1) + 4, I('E'), 'b', 'end')}
    ${ps.axes(I('t'), I('s'), 0, 0)}${ps.f(tri, 0, 2.2)}${T(ps.X(2.2), ps.Y(1) - 4, '(échelle dilatée)', 'soft', 'end')}
    ${D(ps.X(2.12), ps.Y(1), ps.X(2.12), ps.Y(-1), '', 0, 0)}${T(ps.X(2.12) - 6, ps.Y(-.55), '0,16' + I('E'), 'r', 'end')}`, 'Créneau et triangle');
})()},
'p-em-2': {legende: 'Boule de rayon R chargée uniformément ; à droite, ‖E‖ croît linéairement jusqu’à R puis décroît en 1/r² (le champ est dirigé vers le centre, charge négative)', svg: (() => {
  const p = plot(190, 30, 150, 130, [0, 3], [0, 1.15]);
  return svg(370, 200, `${C(90, 100, 64, 'fillA')}${C(90, 100, 40, 'dash r')}${C(90, 100, 46, 'dash r')}${dot(90, 100)}
    ${A(90, 100, ...pol(90, 100, 40, 200))}${T(66, 122, I('r'), '', 'end')}${A(90, 100, ...pol(90, 100, 64, 40))}${T(140, 70, I('R'), '', 'start')}${T(90, 186, 'coquille [' + I('r') + ', ' + I('r') + ' + d' + I('r') + ']', 'r')}
    ${p.axes(I('r'), '‖' + I('E') + '‖')}${p.f(r => r <= 1 ? r : 1 / (r * r), 0, 3)}${p.vline(1)}${T(p.X(1), p.Y(0) + 16, I('R'))}`, 'Électron modélisé par une boule chargée');
})()},
'n-p1-chute': {legende: 'Forces sur la bille : poids mg et frottement −αv ; la vitesse tend vers v_ℓ = mg/α avec le temps caractéristique τ = m/α (95 % en 3τ)', svg: (() => {
  const p = plot(150, 24, 180, 140, [0, 5], [0, 1.12]);
  return svg(370, 200, `${C(70, 100, 14, 'fillR')}${A(70, 116, 70, 172, 'r')}${T(78, 166, I('m') + V('g'), 'r', 'start')}${A(70, 84, 70, 40, 'b')}${T(78, 48, '−α' + V('v'), 'b', 'start')}${A(40, 80, 40, 130)}${T(32, 110, V('v'), '', 'end')}
    ${p.axes(I('t'), I('v'))}${p.hline(1)}${T(p.X(0) - 6, p.Y(1) + 4, sb(I('v'), 'ℓ'), '', 'end')}${p.f(t => 1 - Math.exp(-t), 0, 5)}${L(p.X(0), p.Y(0), p.X(1), p.Y(1), 'dash b')}
    ${p.vline(1)}${T(p.X(1), p.Y(0) + 16, 'τ')}${dot(p.X(3), p.Y(.95), 'r')}${T(p.X(3), p.Y(0) + 16, '3τ')}`, 'Chute avec frottement linéaire');
})()},
'n-p1-geostat': {legende: 'Orbite géostationnaire à l’échelle : r ≈ 42 200 km ≈ 6,6 R_T ; vitesse tangentielle v ≈ 3,07 km/s, force de gravitation vers le centre', svg: (() => {
  const c = [150, 140], RT = 18, r = RT * 42200 / 6370, M = pol(...c, r, 40);
  return svg(320, 280, `${C(...c, r, 'dash soft')}${C(...c, RT, 'fillB')}${T(c[0], c[1] + 5, 'Terre', '')}${C(...M, 7, 'fillR')}
    ${A(...M, ...pol(M[0], M[1], 58, 130), 'r')}${T(...pol(M[0], M[1], 72, 132).map(f1), V('v'), 'r')}${A(...M, ...pol(M[0], M[1], 44, 220), 'b')}${T(...pol(M[0], M[1], 58, 236).map(f1), V('F'), 'b')}
    ${L(...c, ...pol(...c, r, 200), 'dim')}${T(...pol(...c, r / 2, 208).map(f1), I('r'))}${T(c[0] + 26, c[1] + 26, sb(I('R'), 'T'), '', 'start')}`, 'Orbite géostationnaire');
})()},
'n-p2-resonance': {legende: 'Amplitude X(ω)/X(0) pour Q = 0,5, 1 et 3 : pic à ω_r = ω₀√(1 − 1/(2Q²)) < ω₀, qui n’existe que si Q > 1/√2', svg: (() => {
  const p = plot(40, 20, 290, 150, [0, 2.4], [0, 3.4]), X = Q => u => 1 / Math.sqrt((1 - u * u) ** 2 + u * u / (Q * Q)), ur = Math.sqrt(1 - 1 / 18);
  return svg(360, 210, `${p.axes('ω/' + sb('ω', '0'), I('X') + '/' + I('X') + '(0)')}${p.f(X(.5), 0, 2.4, 'thick b')}${p.f(X(1), 0, 2.4, 'dash')}${p.f(X(3), 0, 2.4)}
    ${p.vline(1)}${T(p.X(1) + 8, p.Y(0) + 16, '1', '', 'start')}${L(p.X(ur), p.Y(0), p.X(ur), p.Y(X(3)(ur)), 'dash r')}${T(p.X(ur) - 4, p.Y(0) + 16, sb('ω', 'r'), 'r', 'end')}
    ${T(p.X(1.1), p.Y(3.05), I('Q') + ' = 3', 'r', 'start')}${T(p.X(1.2), p.Y(1.05), I('Q') + ' = 1', '', 'start')}${T(p.X(.4), p.Y(.62), I('Q') + ' = 0,5', 'b', 'end')}`, 'Résonance d’élongation');
})()},
'p-meca-ccmp13': {legende: 'Désorbitation : freinage bref sur l’orbite de rayon 5R_T ; le satellite suit une demi-ellipse d’apogée 5R_T et de périgée R_T + 100 km', svg: (() => {
  const c = [190, 115], RT = 18, rp = RT * 6470 / 6370, ra = 5 * RT, a = (ra + rp) / 2, cx = c[0] - ra + a, cc = c[0] - cx, b = Math.sqrt(a * a - cc * cc);
  return svg(330, 230, `${C(...c, ra, 'dash soft')}<ellipse cx="${f1(cx)}" cy="${c[1]}" rx="${f1(a)}" ry="${f1(b)}" class="s r"/>${C(...c, rp + 1.5, 'fillY')}${C(...c, RT, 'fillB')}
    ${dot(c[0] - ra, c[1])}${A(c[0] - ra, c[1], c[0] - ra, c[1] + 52)}${T(c[0] - ra - 8, c[1] + 50, sb(I('v'), '1'), '', 'end')}${A(c[0] - ra + 6, c[1], c[0] - ra + 6, c[1] + 28, 'r')}${T(c[0] - ra + 14, c[1] + 30, sb(I('v'), '2'), 'r', 'start')}
    ${dot(c[0] + rp, c[1], 'r')}${A(c[0] + rp, c[1], c[0] + rp, c[1] - 74, 'r')}${T(c[0] + rp + 8, c[1] - 64, sb(I('v'), '3'), 'r', 'start')}
    ${T(c[0] - ra + 40, c[1] - 94, '5' + sb(I('R'), 'T'), 'soft')}${T(c[0] + 2, c[1] + 40, 'atmosphère', 'soft', 'start')}`, 'Désorbitation');
})()},
'n-p1-atmo': {legende: 'Ballon : poussée d’Archimède vers le haut, poids vers le bas. À droite, P(z) = P₀e^(−z/H) avec H = RT/(Mg) ≈ 8,4 km', svg: (() => {
  const X0 = 190, Y0 = 176, w = 140, h = 150, px = v => X0 + v / 1.1 * w, pz = z => Y0 - z / 3 * h;
  return svg(370, 200, `${C(80, 80, 34, 'fillY')}${L(80, 114, 80, 140)}${R(70, 140, 20, 14, 'fillW', 2)}${A(80, 46, 80, 14, 'b')}${T(88, 24, sb(V('Π'), 'A'), 'b', 'start')}${A(80, 156, 80, 190, 'r')}${T(88, 186, I('m') + V('g'), 'r', 'start')}
    ${A(X0 - 4, Y0, X0 + w + 12, Y0)}${T(X0 + w + 14, Y0 + 4, I('P'), '', 'start')}${A(X0, Y0 + 4, X0, Y0 - h - 12)}${T(X0 + 6, Y0 - h - 8, I('z'), '', 'start')}
    ${pathC(rng(0, 3, 80).map(z => [px(Math.exp(-z)), pz(z)]), 'thick r')}${L(X0, pz(1), px(Math.exp(-1)), pz(1), 'dash soft')}${L(px(Math.exp(-1)), pz(1), px(Math.exp(-1)), Y0, 'dash soft')}
    ${T(X0 - 6, pz(1) + 4, I('H'), '', 'end')}${T(px(Math.exp(-1)), Y0 + 16, sb(I('P'), '0') + '/e')}${T(px(1), Y0 + 16, sb(I('P'), '0'))}`, 'Atmosphère isotherme');
})()},
'n-p1-photo': {legende: 'Bilan d’énergie : le photon (hν ≈ 4,9 eV) arrache un électron (W = 4,3 eV) ; le reste, E_c ≈ 0,58 eV, est l’énergie cinétique maximale', svg: (() => {
  const k = 22, yv = 50, ym = yv + 4.3 * k, yp = ym - 4.88 * k;
  return svg(340, 220, `${R(40, ym, 140, 210 - ym, 'fillA')}${T(110, ym + 30, 'zinc', 'soft')}${L(40, yv, 320, yv, 'dash')}${T(44, yv - 6, 'niveau du vide', 'soft', 'start')}
    ${L(40, ym, 180, ym, 'thick')}${A(110, ym, 110, yp, 'r')}${T(102, (ym + yp) / 2, 'hν = 4,88 eV', 'r', 'end')}
    ${D(210, ym, 210, yv, I('W') + ' = 4,3 eV', 222, (ym + yv) / 2)}${A(110, yp, 180, yp, 'r')}${D(196, yv, 196, yp, '', 0, 0)}${T(222, yp + 2, sb(I('E'), 'c') + ' = 0,58 eV', 'r', 'start')}`, 'Effet photoélectrique');
})()},
'n-p1-puits': {legende: 'Puits infini [0, L] : niveaux Eₙ = n²E₁ (E₁ ≈ 1,5 eV) et fonctions d’onde sin(nπx/L) ; la transition 1 → 2 absorbe un photon de 275 nm', svg: (() => {
  const x0 = 70, x1 = 290, yE = n => 206 - 16 * n * n;
  const psi = n => pathC(rng(0, 1, 100).map(u => [x0 + u * (x1 - x0), yE(n) - 13 * Math.sin(n * Math.PI * u)]), 'r');
  return svg(360, 220, `${wallV(x0, 30, 180)}${wallV(x1, 30, 180, false)}${L(x0, 210, x1, 210, 'thick')}
    ${[1, 2, 3].map(n => L(x0, yE(n), x1, yE(n), 'dash soft') + psi(n) + T(x1 + 16, yE(n) + 4, sb(I('E'), n) + (n > 1 ? ' = ' + n * n + sb(I('E'), '1') : ''), '', 'start')).join('')}
    ${A(110, yE(1), 110, yE(2) + 2, 'b')}${T(100, (yE(1) + yE(2)) / 2 + 4, 'hν', 'b', 'end')}${T(x0, 226, '0')}${T(x1, 226, I('L'))}`, 'Électron dans un puits');
})()},
'p-q-1': {legende: 'Particule sur un cercle : ψ doit reprendre la même valeur après un tour, ψ(θ + 2π) = ψ(θ), d’où ψₙ ∝ e^(inθ) (ici la partie réelle pour n = 3)', svg: svg(300, 230, `
  ${C(150, 115, 72, 'dash soft')}${pathC(rng(0, 2 * Math.PI, 200).map(t => pol(150, 115, 72 + 14 * Math.cos(3 * t), t * 180 / Math.PI)), 'thick r')}
  ${dot(150, 115)}${L(150, 115, 250, 115, 'axis')}${L(150, 115, ...pol(150, 115, 72, 50))}${C(...pol(150, 115, 72, 50), 6, 'fillB')}${arc(150, 115, 28, 0, 50)}${T(...pol(150, 115, 40, 25).map(f1), 'θ')}
  ${T(...pol(150, 115, 36, 140).map(f1), I('R'))}${T(150, 218, 'Re ψ₃(θ) ∝ cos 3θ', 'r')}`, 'Particule sur un cercle')},
'p-q-3': {legende: 'Puits harmonique V = ½mω₀²x² ; niveau fondamental E₀ = ħω₀/2 et fonction d’onde gaussienne (points de rebroussement classiques en V = E₀)', svg: (() => {
  const p = plot(40, 20, 280, 160, [-3, 3], [0, 3.6]);
  return svg(360, 210, `${p.axes(I('x') + '/' + sb(I('x'), '0'), I('V'), 0, 0)}${p.f(u => u * u / 2, -3, 3)}${p.hline(.5, 'dash b')}${p.f(u => .5 + 1.1 * Math.exp(-u * u / 2), -3, 3, 'thick b')}
    ${T(p.X(3) - 4, p.Y(.5) - 6, sb(I('E'), '0') + ' = ħ' + sb('ω', '0') + '/2', 'b', 'end')}${dot(p.X(-1), p.Y(.5))}${dot(p.X(1), p.Y(.5))}${T(p.X(1.6), p.Y(1.6) - 30, 'ψ₀', 'b', 'start')}`, 'Oscillateur harmonique quantique');
})()},
'p-q-2': {legende: 'V(x) = −λ/x pour x > 0 (paroi infinie en 0) ; niveau E = −mλ²/(2ħ²) et φ = Cx e^(−kx), maximale en 1/k ; ⟨x⟩ = 3/(2k)', svg: (() => {
  const p = plot(40, 20, 290, 170, [0, 8], [-2.6, .9]);
  return svg(370, 220, `${p.axes(I('x') + ' (unités 1/' + I('k') + ')', I('V'))}${R(p.X(0) - 10, 20, 10, 170, 'hatch')}${p.f(x => -1 / x, .38, 8)}
    ${p.hline(-.5, 'dash b')}${p.f(x => -.5 + 1.6 * x * Math.exp(-x), 0, 8, 'thick b')}${T(p.X(8), p.Y(-.5) + 16, I('E'), 'b', 'end')}
    ${dot(p.X(2), p.Y(-.5))}${T(p.X(2), p.Y(-.5) + 16, 'rebroussement', 'soft')}${p.vline(1.5)}${T(p.X(1.5), p.Y(.9) - 2, '⟨' + I('x') + '⟩')}${T(p.X(1), p.Y(.2), 'φ', 'b')}`, 'Potentiel en −1/x');
})()},
'n-p2-bohr': {legende: 'Énergie estimée E(a) = ħ²/(2mₑa²) − e²/(4πε₀a) : le terme cinétique empêche l’effondrement ; minimum en a₀ ≈ 53 pm, E ≈ −13,6 eV', svg: (() => {
  const p = plot(40, 20, 290, 170, [0, 5], [-3, 3]);
  return svg(360, 220, `${p.axes(I('a') + '/' + sb(I('a'), '0'), I('E') + '/13,6 eV', 0, 0)}${p.f(x => 1 / (x * x), .3, 5, 'dash b')}${p.f(x => -2 / x, .3, 5, 'dash')}${p.f(x => 1 / (x * x) - 2 / x, .3, 5)}
    ${dot(p.X(1), p.Y(-1), 'r')}${L(p.X(1), p.Y(0), p.X(1), p.Y(-1), 'dash soft')}${T(p.X(1) + 8, p.Y(-1) + 16, '(' + sb(I('a'), '0') + ', −13,6 eV)', 'r', 'start')}
    ${T(p.X(.7), p.Y(2.6), 'cinétique', 'b', 'start')}${T(p.X(1.4), p.Y(-2.4), 'potentielle', '', 'start')}`, 'Énergie de l’atome d’hydrogène');
})()},
'p-oem-2': {legende: 'k′k″ < 0 : pour une onde qui progresse vers x > 0 (k′ > 0), l’amplitude décroît avec x : l’onde est atténuée', svg: (() => {
  const p = plot(40, 20, 290, 140, [0, 12], [-1.1, 1.1]);
  return svg(360, 190, `${p.axes(I('x'), I('G'), 0, 0)}${p.f(x => Math.exp(-.22 * x), 0, 12, 'dash b')}${p.f(x => -Math.exp(-.22 * x), 0, 12, 'dash b')}${p.f(x => Math.exp(-.22 * x) * Math.cos(2.2 * x), 0, 12, 'thick r', 400)}
    ${A(p.X(7), p.Y(.9), p.X(10), p.Y(.9))}${T(p.X(8.5), p.Y(.9) - 8, 'propagation')}${T(p.X(3), p.Y(.62), 'e^(' + I('k') + '″' + I('x') + ')', 'b', 'start')}`, 'Onde atténuée');
})()},
'p-oem-3': {legende: 'L’onde pénètre dans le conducteur (vecteur de Poynting selon u_z) ; E décroît en e^(−z/δ) ; la puissance Joule moyenne dans le volume a × a × ∞ vaut γE₀²a²δ/4', svg: svg(360, 200, `
  ${R(120, 20, 220, 150, 'fillA')}${L(120, 20, 120, 170, 'thick')}${T(230, 40, 'conducteur, γ')}${T(60, 40, 'vide', 'soft')}
  ${[0, 1, 2, 3, 4].map(k => { const l = 60 * Math.exp(-k * .55); return A(140 + 44 * k, 130, 140 + 44 * k, 130 - l, 'r'); }).join('')}${T(150, 64, V('E'), 'r', 'start')}
  ${A(40, 100, 116, 100, 'b')}${T(76, 90, '⟨' + V('Π') + '⟩', 'b')}${D(120, 150, 164, 150, 'δ', 142, 166)}
  ${A(30, 186, 70, 186)}${T(74, 190, I('z'), '', 'start')}${A(30, 186, 30, 150)}${T(36, 152, I('x'), '', 'start')}${ox(30, 186)}`, 'Pénétration et effet Joule')},
'n-p2-plasma': {legende: 'L’ionosphère réfléchit les ondes de fréquence f < f_p ≈ 9 MHz (propagation à grande distance) et laisse passer les ondes plus hautes (satellites)', svg: svg(360, 210, `
  ${P('M0,200 Q180,160 360,200', 'fillB')}${T(180, 196, 'Terre', '')}${R(0, 40, 360, 34, 'fillA')}${T(350, 60, 'ionosphère', 'soft', 'end')}
  ${A(40, 178, 120, 76, 'r')}${A(120, 76, 200, 176, 'r')}${T(52, 140, I('f') + ' < ' + sb(I('f'), 'p'), 'r', 'start')}${T(128, 104, 'réfléchie', 'r')}
  ${A(240, 172, 290, 14, 'b')}${T(276, 104, I('f') + ' > ' + sb(I('f'), 'p'), 'b', 'start')}${T(296, 24, 'transmise', 'b', 'start')}`, 'Ionosphère et ondes radio')},
'p-oem-5': {legende: 'Pour τω ≫ 1 : n² ≈ 1 − ω_p²/ω². Sous ω_p (n² < 0) l’onde est réfléchie, le métal brille ; au-delà (UV, λ < 0,2 µm) il devient transparent', svg: (() => {
  const p = plot(40, 20, 290, 160, [0, 3], [-3, 1.2]);
  return svg(360, 210, `${p.axes('ω/' + sb('ω', 'p'), I('n') + '²', 0, 0)}${p.f(u => 1 - 1 / (u * u), .5, 3)}${p.hline(1)}${p.vline(1)}${T(p.X(1), p.Y(-3) + 16, '1')}
    ${T(p.X(.55), p.Y(-.6), 'réflexion', 'b', 'start')}${T(p.X(1.6), p.Y(.4), 'transparent (UV)', 'r', 'start')}`, 'Indice d’un métal');
})()},
'n-p1-corde': {legende: 'Modes propres de la corde fixée : fₙ = n f₁, nœuds (N) aux extrémités et tous les L/n. Pincée au milieu, la corde n’excite pas les modes pairs (nœud au milieu)', svg: (() => {
  const x0 = 40, x1 = 300, row = (n, y) => { const env = s => pathC(rng(0, 1, 100).map(u => [x0 + u * (x1 - x0), y - s * 14 * Math.sin(n * Math.PI * u)]), s > 0 ? 'thick r' : 'dash r'); return env(1) + env(-1) + Array.from({length: n + 1}, (_, k) => dot(x0 + k * (x1 - x0) / n, y)).join('') + T(x1 + 14, y + 4, I('n') + ' = ' + n, '', 'start'); };
  return svg(360, 200, `${row(1, 40)}${row(2, 100)}${row(3, 160)}${T(x0 + (x1 - x0) / 2, 116, 'N', 'soft')}${T(x0, 192, '0')}${T(x1, 192, I('L'))}`, 'Modes propres d’une corde');
})()},
'n-p2-doublet': {legende: 'Éclairement au centre en fonction de δ : franges modulées par le contraste |cos(πΔλδ/λ²ₘ)| ; brouillage pour δ = λ²ₘ/(2Δλ) (nombre de franges réduit pour la lisibilité)', svg: (() => {
  const p = plot(40, 20, 290, 150, [0, 2.2], [0, 2.15]);
  return svg(360, 200, `${p.axes('δ', 'ℰ/' + sb('ℰ', '0'), 0, 0)}${p.f(d => 1 + Math.cos(Math.PI * d) * Math.cos(2 * Math.PI * 14 * d), 0, 2.2, 'r', 900)}
    ${p.f(d => 1 + Math.abs(Math.cos(Math.PI * d)), 0, 2.2, 'dash b')}${p.f(d => 1 - Math.abs(Math.cos(Math.PI * d)), 0, 2.2, 'dash b')}
    ${T(p.X(.5), p.Y(0) + 16, 'λ²ₘ/(2Δλ)')}${T(p.X(1.5), p.Y(0) + 16, '3λ²ₘ/(2Δλ)')}${T(p.X(.5), p.Y(2.15) - 2, 'brouillage', 'b')}`, 'Battement du doublet');
})()},
'n-p2-reseau': {legende: 'Spectres du réseau (a = 2,0 µm) sur l’échelle sin θ = pλ/a : les ordres 2 et 3 se recouvrent (0,6 à 0,7), pas les ordres 1 et 2 ; l’ordre 3 est coupé au-delà de 667 nm', svg: (() => {
  const X0 = 50, W = 280, sx = v => X0 + v * W, bar = (p, y) => { const a = p * .2, b = Math.min(p * .35, 1); return `<rect x="${f1(sx(a))}" y="${y}" width="${f1(sx(b) - sx(a))}" height="18" fill="url(#spec)"/>` + T(X0 - 8, y + 14, 'ordre ' + p, '', 'end'); };
  return svg(360, 190, `<defs><linearGradient id="spec"><stop offset="0" stop-color="#7a3fc0"/><stop offset=".3" stop-color="#2f6fd0"/><stop offset=".5" stop-color="#2aa14a"/><stop offset=".7" stop-color="#e0c22a"/><stop offset="1" stop-color="#c8372d"/></linearGradient></defs>
    ${bar(1, 30)}${bar(2, 70)}${bar(3, 110)}${R(sx(.6), 22, sx(.7) - sx(.6), 112, 'dash b')}${T(sx(.65), 18, 'recouvrement', 'b')}
    ${A(X0, 150, X0 + W + 12, 150)}${T(X0 + W + 14, 154, 'sin θ', '', 'start')}${[0, .2, .4, .6, .8, 1].map(v => L(sx(v), 146, sx(v), 154) + T(sx(v), 170, String(v).replace('.', ','))).join('')}`, 'Ordres du réseau');
})()},
'p-opt-8': {legende: 'Intensité au centre : franges de période T₀ = λ₀/(2V₀) sous une enveloppe gaussienne exp[−(t/τ)²], avec τ = 1/(2πbV₀)', svg: (() => {
  const p = plot(40, 20, 290, 150, [0, 2.6], [0, 2.15]);
  return svg(360, 200, `${p.axes(I('t'), I('I') + '/' + sb(I('I'), '0'), 0, 0)}${p.f(t => 1 + Math.exp(-t * t) * Math.cos(2 * Math.PI * t * 7), 0, 2.6, 'r', 800)}
    ${p.f(t => 1 + Math.exp(-t * t), 0, 2.6, 'dash b')}${p.f(t => 1 - Math.exp(-t * t), 0, 2.6, 'dash b')}${p.vline(1)}${T(p.X(1), p.Y(0) + 16, 'τ')}
    ${D(p.X(2 / 7), p.Y(2.08), p.X(3 / 7), p.Y(2.08), '', 0, 0)}${T(p.X(3 / 7) + 6, p.Y(2.08) + 4, sb(I('T'), '0'), '', 'start')}`, 'Interférogramme d’un profil gaussien');
})()},
'p-stat-1': {legende: 'Deux niveaux : moment parallèle à B (énergie −μ₀B₀, plus peuplé) ou antiparallèle (+μ₀B₀). À droite, ⟨μ⟩/μ₀ = th(μ₀B/k_BT), linéaire à haute température (loi de Curie)', svg: (() => {
  const p = plot(210, 30, 130, 130, [0, 3], [0, 1.1]);
  return svg(380, 200, `${L(30, 60, 150, 60, 'thick')}${L(30, 140, 150, 140, 'thick')}${T(156, 64, '+' + sb('μ', '0') + sb(I('B'), '0'), '', 'start')}${T(156, 144, '−' + sb('μ', '0') + sb(I('B'), '0'), '', 'start')}
    ${A(90, 52, 90, 30, 'r')}${T(100, 40, sb(I('p'), '−'), 'r', 'start')}${[60, 90, 120].map(x => A(x, 154, x, 176, 'b')).join('')}${T(30, 184, sb(I('p'), '+') + ' > ' + sb(I('p'), '−'), 'b', 'start')}
    ${A(18, 110, 18, 160)}${T(12, 108, V('B'), '', 'middle')}
    ${p.axes(sb('μ', '0') + I('B') + '/' + sb(I('k'), 'B') + I('T'), '⟨μ⟩/' + sb('μ', '0'))}${p.hline(1)}${p.f(Math.tanh, 0, 3)}${L(p.X(0), p.Y(0), p.X(1.05), p.Y(1.05), 'dash b')}${T(p.X(.9), p.Y(.5), 'Curie', 'b', 'start')}`, 'Paramagnétisme à deux niveaux');
})()},
'n-p2-serre': {legende: 'Bilan avec une couche atmosphérique absorbant l’infrarouge : l’atmosphère rayonne σT_a⁴ vers l’espace et vers le sol ; le sol reçoit le solaire et ce rayonnement, d’où T_s = 2^(1/4)T_a ≈ 303 K', svg: svg(360, 220, `
  ${R(0, 190, 360, 30, 'fillY')}${T(340, 210, 'sol, ' + sb(I('T'), 's'), '', 'end')}${R(0, 90, 360, 18, 'fillA')}${T(340, 104, 'atmosphère, ' + sb(I('T'), 'a'), '', 'end')}
  ${A(50, 20, 50, 186, 'r')}${T(58, 40, '(1 − ' + I('A') + ')' + sb('φ', 'S') + '/4', 'r', 'start')}
  ${A(150, 188, 150, 110, 'b')}${T(158, 156, 'σ' + sb(I('T'), 's') + '⁴', 'b', 'start')}${A(230, 92, 230, 20, 'b')}${T(238, 40, 'σ' + sb(I('T'), 'a') + '⁴', 'b', 'start')}${A(270, 110, 270, 186, 'b')}${T(278, 156, 'σ' + sb(I('T'), 'a') + '⁴', 'b', 'start')}
  ${T(110, 66, 'visible : traverse', 'soft')}`, 'Effet de serre à une couche')},
'p-th-spe3': {legende: 'Densité spectrale 𝒟(λ) du corps noir à 4 000, 5 000 et 6 000 K : le maximum se déplace selon λ_max T = 2,90 × 10⁻³ m·K (pointillés) et l’aire croît en T⁴', svg: (() => {
  const Dn = T => l => l ** -5 / (Math.exp(14388 / (l * T)) - 1), ref = Dn(6000)(2898 / 6000), p = plot(40, 20, 290, 160, [0, 2.5], [0, 1.1]);
  const locus = rng(3600, 6200, 40).map(T => [p.X(2898 / T), p.Y(Dn(T)(2898 / T) / ref)]);
  return svg(360, 210, `${p.axes('λ (µm)', '𝒟')}${[[6000, 'thick r'], [5000, 'thick b'], [4000, 'thick']].map(([T, c]) => p.f(l => Dn(T)(l) / ref, .1, 2.5, c)).join('')}${pathC(locus, 'dash')}
    ${T(p.X(.62), p.Y(1.02), '6 000 K', 'r', 'start')}${T(p.X(.7), p.Y(.45), '5 000 K', 'b', 'start')}${T(p.X(.9), p.Y(.2), '4 000 K', '', 'start')}
    ${[0.5, 1, 1.5, 2].map(v => T(p.X(v), p.Y(0) + 16, String(v).replace('.', ','))).join('')}`, 'Loi de Planck');
})()},
'p-th-spe4': {legende: 'Modèle 1D : les photons vont selon ±u_x ; ceux qui frappent le miroir de droite pendant dt sont dans la tranche de largeur c dt ; chacun lui cède 2hf/c', svg: svg(360, 200, `
  ${R(60, 30, 200, 140, 'fillW')}${L(60, 30, 60, 170, 'thick')}${L(260, 30, 260, 170, 'thick')}${R(262, 30, 8, 140, 'hatch')}${R(48, 30, 10, 140, 'hatch')}
  ${R(214, 31, 44, 138, 'fillY')}${D(214, 182, 260, 182, I('c') + ' d' + I('t'), 237, 196)}
  ${[[90, 60, 1], [150, 90, -1], [110, 130, 1], [180, 150, -1], [226, 70, 1], [234, 120, 1], [200, 50, -1]].map(([x, y, s]) => A(x, y, x + s * 26, y, s > 0 ? 'r' : 'b')).join('')}
  ${A(274, 100, 320, 100)}${T(300, 90, '2' + I('hf') + '/' + I('c'))}${D(60, 16, 260, 16, I('a'), 160, 12)}`, 'Photons dans une cavité')},
'n-p1-frigo': {legende: 'Réfrigérateur : le fluide reçoit Q_F > 0 de l’intérieur (T_F) et le travail W > 0, et cède de la chaleur à la cuisine (Q_C < 0)', svg: svg(360, 180, `
  ${R(10, 60, 90, 60, 'fillA', 6)}${T(55, 86, 'intérieur')}${T(55, 106, sb(I('T'), 'F') + ' = 278 K')}${R(260, 60, 90, 60, 'fillR', 6)}${T(305, 86, 'cuisine')}${T(305, 106, sb(I('T'), 'C') + ' = 298 K')}
  ${C(180, 90, 32, 'fillW')}${T(180, 95, 'fluide')}${A(102, 90, 146, 90, 'b')}${T(124, 80, sb(I('Q'), 'F') + ' > 0', 'b')}${A(214, 90, 258, 90, 'r')}${T(236, 80, '|' + sb(I('Q'), 'C') + '|', 'r')}
  ${A(180, 16, 180, 56)}${T(188, 30, I('W') + ' > 0 (compresseur)', '', 'start')}${T(180, 158, I('e') + ' = ' + sb(I('Q'), 'F') + '/' + I('W'), 'soft')}`, 'Machine frigorifique')},
'n-p2-beau': {legende: 'Cycle de Beau de Rochas dans le diagramme (P, V) : parcouru dans le sens horaire, il est moteur (W < 0)', svg: (() => {
  const g = 1.4, a = 9, P2 = a ** g, P3 = P2 * 2000 / (300 * a ** (g - 1)), P4 = P3 / a ** g, p = plot(50, 18, 270, 160, [0, 10], [0, 64]);
  const ad = (Pr, v) => Pr * (1 / v) ** g;  // P sur l'adiabatique passant par (1, Pr)
  const mid = (fn, v1, v2) => { const m = (v1 + v2) / 2; return A(p.X(m + (v1 > v2 ? .2 : -.2)), p.Y(fn(m + (v1 > v2 ? .2 : -.2))), p.X(m), p.Y(fn(m)), 'r'); };
  return svg(360, 210, `${p.axes(I('V'), I('P'))}${p.f(v => ad(P2, v), 1, 9)}${p.f(v => ad(P3, v), 1, 9)}${L(p.X(1), p.Y(P2), p.X(1), p.Y(P3), 'thick r')}${L(p.X(9), p.Y(1), p.X(9), p.Y(P4), 'thick r')}
    ${mid(v => ad(P2, v), 9, 1)}${mid(v => ad(P3, v), 1, 9)}${A(p.X(1), p.Y(35), p.X(1), p.Y(42), 'r')}${A(p.X(9), p.Y(2.4), p.X(9), p.Y(1.6), 'r')}
    ${[[9, 1, '1'], [1, P2, '2'], [1, P3, '3'], [9, P4, '4']].map(([v, P, n]) => dot(p.X(v), p.Y(P)) + T(p.X(v) + (v > 5 ? 8 : -8), p.Y(P) + (n === '1' ? 16 : n === '4' ? -6 : 4), n, '', v > 5 ? 'start' : 'end')).join('')}
    ${T(p.X(1), p.Y(0) + 16, sb(I('V'), '2'))}${T(p.X(9), p.Y(0) + 16, sb(I('V'), '1'))}${T(p.X(3.6), p.Y(24), 'moteur', 'soft')}`, 'Cycle de Beau de Rochas');
})()},
'n-p2-vdw': {legende: 'Détente de Joule – Gay-Lussac : enceinte rigide et calorifugée ; à l’ouverture de la vanne, le gaz passe de V₁ = 1,0 L à V₂ = 2,0 L sans travail ni chaleur (ΔU = 0)', svg: svg(360, 170, `
  ${R(30, 40, 300, 90, 'hatch')}${R(40, 50, 140, 70, 'fillA')}${R(180, 50, 140, 70, 'fillW')}${L(180, 50, 180, 74, 'thick')}${L(180, 96, 180, 120, 'thick')}${C(180, 85, 7, 'fillW')}${L(175, 80, 185, 90)}
  ${[[60, 64], [90, 100], [120, 70], [150, 104], [74, 86], [140, 60], [106, 90], [160, 82]].map(([x, y]) => C(x, y, 3, 'fillB')).join('')}${T(110, 146, sb(I('V'), '1') + ' : gaz, ' + sb(I('T'), '1'))}${T(250, 90, 'vide', 'soft')}
  ${T(180, 24, 'vanne', 'soft')}${D(40, 160, 320, 160, sb(I('V'), '2') + ' = 2' + sb(I('V'), '1'), 252, 156)}`, 'Détente de Joule – Gay-Lussac')},
};
