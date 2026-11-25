// Schémas des fiches de cours — Physique MP : mécanique, électronique, optique ondulatoire.
import { svg, L, A, D, T, I, V, C, R, P, dot, sb, ox, ot, ground, lens } from './figkit.js';
import { axes, courbe } from './fiches-kit.js';

const r2 = n => Math.round(n * 100) / 100;
const rad = d => d * Math.PI / 180;
const pol = (x, y, r, deg) => [r2(x + r * Math.cos(rad(deg))), r2(y - r * Math.sin(rad(deg)))]; // angle compté vers le haut
const arc = (x, y, r, d1, d2, c = 'soft') => { const [a, b] = pol(x, y, r, d1), [e, f] = pol(x, y, r, d2); return P(`M${a},${b} A${r},${r} 0 0 ${d2 > d1 ? 0 : 1} ${e},${f}`, c); };
const repere = (x, y, l, lx, ly, c = 'soft') => A(x, y, x + l, y, c) + A(x, y, x, y - l, c) + T(x + l + 4, y + 5, lx, '', 'start') + T(x + 4, y - l - 4, ly, '', 'start');

export const FIGS = {
// ---------- changements de référentiels ----------
'mp-referentiels-1': ['Deux mouvements de R′ par rapport à R : translation (axes de R′ parallèles à ceux de R, O′ en mouvement) et rotation uniforme autour d’un axe fixe Oz, à la vitesse angulaire ω', svg(440, 230, `
  ${repere(30, 190, 70, I('x'), I('y'))}${T(26, 206, I('O'), '', 'middle')}${T(70, 150, '(R)', 'nt', 'middle')}
  ${A(30, 190, 130, 110, 'b')}${T(74, 142, '', '', 'middle')}
  ${repere(130, 110, 60, I('x′'), I('y′'), '')}${T(138, 102, I('O′'), '', 'start')}${T(165, 80, '(R′)', 'nt', 'middle')}
  ${A(150, 140, 195, 140, 'r')}${T(198, 144, V('v') + sb('', 'O′'), 'r', 'start')}
  ${T(120, 222, 'translation', 'nt', 'middle')}
  ${L(250, 10, 250, 222, 'dash soft')}
  ${A(330, 140, 420, 140, 'soft')}${A(330, 140, 330, 50, 'soft')}${T(424, 145, I('x'), '', 'start')}${T(336, 48, I('y'), '', 'start')}
  ${A(330, 140, ...pol(330, 140, 85, 30))}${A(330, 140, ...pol(330, 140, 85, 120))}${T(...pol(330, 140, 98, 30), I('x′'))}${T(...pol(330, 140, 96, 122), I('y′'))}
  ${arc(330, 140, 40, 0, 30, 'b')}${T(...pol(330, 140, 52, 14), I('θ'), 'b')}${ox(330, 140)}${T(316, 160, I('O'), '', 'middle')}
  ${T(380, 186, V('ω') + ' = ' + I('θ̇') + ' ' + V('u') + sb('', I('z')), 'b', 'middle')}${T(345, 222, 'rotation (vue de dessus)', 'nt', 'middle')}`, 'Référentiels')],

'mp-referentiels-2': ['Composition des vitesses : la vitesse absolue (dans R) est la somme de la vitesse relative (dans R′) et de la vitesse d’entraînement, vitesse du point coïncident', svg(400, 230, `
  ${repere(30, 200, 60, I('x'), I('y'))}${T(70, 186, '(R)', 'nt', 'start')}
  <path d="M120,200 C160,150 200,120 300,110" class="s soft dash"/>${T(250, 136, 'trajectoire dans R′', 'nt', 'start')}
  ${dot(171.84, 149.6)}${T(164, 162, I('M'), '', 'end')}
  ${A(171.84, 149.6, 237.84, 104.4, 'b')}${T(244, 104, sb(V('v'), 'r'), 'b', 'start')}
  ${A(171.84, 149.6, 194.84, 64.6, 'r')}${T(186, 58, sb(V('v'), 'e'), 'r', 'end')}
  ${L(237.84, 104.4, 260.84, 19.4, 'dash soft')}${L(194.84, 64.6, 260.84, 19.4, 'dash soft')}
  ${A(171.84, 149.6, 260.84, 19.4, 'thick')}${T(268, 24, sb(V('v'), 'a'), '', 'start')}
  ${T(200, 222, sb(V('v'), 'a') + ' = ' + sb(V('v'), 'r') + ' + ' + sb(V('v'), 'e'), '', 'middle')}`, 'Composition des vitesses')],

// ---------- référentiel non galiléen ----------
'mp-non-galileen-1': ['Manège en rotation uniforme : dans le référentiel du manège, un point M à la distance r de l’axe subit la force d’inertie d’entraînement (centrifuge), dirigée de H vers M', svg(400, 230, `
  ${L(150, 20, 150, 210, 'axis')}${A(150, 60, 150, 22, 'b')}${T(158, 32, V('ω'), 'b', 'start')}${T(140, 205, '(Δ)', 'nt', 'end')}
  <ellipse cx="150" cy="150" rx="130" ry="30" class="s fillA"/>
  ${dot(150, 150)}${T(142, 145, I('H'), '', 'end')}${L(150, 150, 250, 150, 'dash soft')}${T(200, 166, I('r'), '', 'middle')}
  ${dot(250, 150)}${T(250, 140, I('M'), '', 'middle')}
  ${A(250, 150, 330, 150, 'r')}${T(334, 144, sb(V('F'), 'ie'), 'r', 'start')}
  ${T(300, 200, sb(V('F'), 'ie') + ' = ' + I('mω') + '² ' + V('HM'), 'r', 'middle')}`, 'Force centrifuge')],

'mp-non-galileen-2': ['Force de Coriolis −2m Ω ∧ v : un corps lâché sans vitesse est dévié vers l’est (déviation exagérée) ; dans l’hémisphère nord, un mouvement horizontal est dévié vers sa droite', svg(440, 240, `
  ${ground(20, 200, 180)}${R(40, 40, 24, 160, 'fillW')}${dot(70, 50)}
  ${L(70, 50, 70, 200, 'dash soft')}<path d="M70,50 C71,120 76,170 84,198" class="s b"/>${dot(84, 198)}
  ${A(110, 120, 170, 120)}${T(174, 125, 'est', 'nt', 'start')}${T(110, 222, 'chute libre', 'nt', 'middle')}
  ${L(220, 10, 220, 230, 'dash soft')}
  ${C(330, 120, 90, 'fillA')}${ox(330, 120)}${T(330, 145, V('Ω'), 'b', 'middle')}${T(330, 225, 'hémisphère nord vu du pôle', 'nt', 'middle')}
  ${dot(280, 70)}${A(280, 70, 340, 40, 'b')}${T(346, 38, V('v'), 'b', 'start')}
  ${A(280, 70, 303, 116, 'r')}${T(296, 116, sb(V('F'), 'ic'), 'r', 'end')}
  ${arc(330, 120, 104, 60, 90, 'soft')}${A(...pol(330, 120, 104, 88), ...pol(330, 120, 104, 96), 'soft')}`, 'Coriolis')],

'mp-non-galileen-3': ['Pendule dans un véhicule d’accélération a : à l’équilibre relatif, le fil s’aligne sur la pesanteur apparente g − a et s’incline vers l’arrière, tan α = a/g', svg(400, 240, `
  ${R(40, 30, 320, 170, 'fillW')}${ground(20, 214, 360)}${C(90, 207, 7)}${C(310, 207, 7)}
  ${A(250, 60, 330, 60, 'r')}${T(334, 64, V('a'), 'r', 'start')}
  ${dot(200, 30)}${L(200, 30, 200, 160, 'dash soft')}${L(200, 30, ...pol(200, 30, 130, 270 - 25.6))}
  ${C(...pol(200, 30, 130, 270 - 25.6), 8, 'fillA')}${arc(200, 30, 50, 270 - 25.6, 270, 'b')}${T(190, 100, I('α'), 'b', 'middle')}
  ${(() => { const [x, y] = pol(200, 30, 130, 270 - 25.6); return A(x, y, x, y + 45) + T(x + 6, y + 44, I('m') + V('g'), '', 'start') + A(x, y, r2(x - 21.5), y, 'r') + T(x - 26, y - 4, '−' + I('m') + V('a'), 'r', 'end') + A(x, y, r2(x - 21.5), r2(y + 45), 'b') + T(x - 26, y + 40, I('m') + sb(V('g'), 'app'), 'b', 'end'); })()}`, 'Pendule dans un véhicule')],

'mp-non-galileen-4': ['Poids et pesanteur : le poids est la somme de l’attraction gravitationnelle (vers le centre) et de la force d’inertie d’entraînement (perpendiculaire à l’axe, exagérée ici) ; il dépend de la latitude λ', svg(400, 250, `
  ${C(170, 125, 95, 'fillA')}${L(170, 10, 170, 240, 'axis')}${A(170, 40, 170, 12, 'b')}${T(178, 22, V('Ω'), 'b', 'start')}
  ${L(170, 125, 290, 125, 'dash soft')}${L(170, 125, ...pol(170, 125, 95, 40))}${arc(170, 125, 26, 0, 40, 'b')}${T(...pol(170, 125, 36, 14), I('λ'), 'b')}
  ${(() => { const [x, y] = pol(170, 125, 95, 40); return dot(x, y) + T(x + 2, y - 8, I('M'), '', 'start') + L(170, y, x, y, 'dash soft') + T(170 - 6, y + 4, I('H'), '', 'end')
    + A(x, y, ...pol(x, y, 50, 220)) + T(pol(x, y, 50, 220)[0] - 6, pol(x, y, 50, 220)[1] + 4, sb(V('F'), 'g'), '', 'end') + A(x, y, x + 22, y, 'r') + T(x + 26, y + 5, sb(V('F'), 'ie'), 'r', 'start')
    + A(x, y, r2(pol(x, y, 50, 220)[0] + 22), pol(x, y, 50, 220)[1], 'thick') + T(r2(pol(x, y, 50, 220)[0] + 28), pol(x, y, 50, 220)[1] + 12, I('m') + V('g'), '', 'start'); })()}
  ${T(296, 129, 'équateur', 'nt', 'start')}`, 'Poids et pesanteur')],

// ---------- frottement ----------
'mp-frottement-1': ['Lois de Coulomb : la réaction R = N + T reste dans le cône de frottement d’angle φ (tan φ = f) tant qu’il n’y a pas de glissement ; elle est sur le bord du cône en cas de glissement', svg(400, 230, `
  ${ground(40, 180, 320)}${R(150, 120, 100, 60, 'fillA')}${dot(200, 180)}${T(196, 198, I('I'), '', 'end')}
  ${L(200, 180, ...pol(200, 180, 160, 90 + 31), 'dash soft')}${L(200, 180, ...pol(200, 180, 160, 90 - 31), 'dash soft')}
  ${A(200, 180, 200, 60, 'b')}${T(206, 58, V('N'), 'b', 'start')}${A(200, 180, 150, 180, 'r')}${T(146, 172, V('T'), 'r', 'end')}
  ${A(200, 180, 150, 60)}${T(144, 56, V('R'), '', 'end')}${L(150, 60, 200, 60, 'dash soft')}${L(150, 60, 150, 180, 'dash soft')}
  ${arc(200, 180, 70, 90, 121, 'b')}${T(...pol(200, 180, 84, 106), I('φ'), 'b')}
  ${T(320, 80, 'tan ' + I('φ') + ' = ' + I('f'), '', 'middle')}${T(320, 100, 'cône de frottement', 'nt', 'middle')}`, 'Cône de frottement')],

'mp-frottement-2': ['Solide posé sur un plan incliné d’angle α : il reste immobile si tan α ≤ f (la réaction équilibre le poids) ; il glisse si tan α > f, la réaction étant alors sur le bord du cône', svg(440, 220, (() => {
  const pan = (x0, al, ok) => {
    const y0 = 190, Lp = 180, [x1, y1] = pol(x0, y0, Lp, al), u = [Math.cos(rad(al)), -Math.sin(rad(al))], n = [-Math.sin(rad(al)), -Math.cos(rad(al))];
    const cx = x0 + u[0] * 100 + n[0] * 16, cy = y0 + u[1] * 100 + n[1] * 16, bx = x0 + u[0] * 100, by = y0 + u[1] * 100;
    const blk = [[-20, 0], [20, 0], [20, 32], [-20, 32]].map(([a, b]) => [r2(x0 + u[0] * (100 + a) + n[0] * b), r2(y0 + u[1] * (100 + a) + n[1] * b)]);
    let s = L(x0, y0, x0 + Lp + 20, y0) + L(x0, y0, x1, y1) + P('M' + blk.map(p => p.join(',')).join(' L') + 'Z', 'fillA') + arc(x0, y0, 40, 0, al, 'b') + T(...pol(x0, y0, 52, al / 2), I('α'), 'b');
    s += A(r2(cx), r2(cy), r2(cx), r2(cy + 60)) + T(r2(cx + 6), r2(cy + 60), V('P'), '', 'start');
    const phi = 25;                               // f = tan 25°
    if (ok) s += A(r2(bx), r2(by), r2(bx), r2(by - 60), 'b') + T(r2(bx - 6), r2(by - 56), V('R'), 'b', 'end');
    else { const d = 90 + al - phi; s += A(r2(bx), r2(by), ...pol(bx, by, 58, d), 'b') + T(...pol(bx, by, 70, d), V('R'), 'b') + A(r2(bx + u[0] * 30 + n[0] * 50), r2(by + u[1] * 30 + n[1] * 50), r2(bx - u[0] * 10 + n[0] * 50), r2(by - u[1] * 10 + n[1] * 50), 'r'); }
    s += L(r2(bx), r2(by), ...pol(bx, by, 70, 90 + al + phi), 'dash soft') + L(r2(bx), r2(by), ...pol(bx, by, 70, 90 + al - phi), 'dash soft');
    return s;
  };
  return pan(20, 18, true) + T(110, 215, 'tan ' + I('α') + ' &lt; ' + I('f') + ' : adhérence', 'nt', 'middle') + pan(230, 38, false) + T(330, 215, 'tan ' + I('α') + ' > ' + I('f') + ' : glissement', 'nt', 'middle');
})(), 'Plan incliné')],

// ---------- signaux périodiques, filtrage ----------
'mp-signal-1': ['Gabarit d’un filtre passe-bas : la courbe de gain doit éviter les zones interdites (gain trop faible dans la bande passante, trop fort dans la bande coupée)', svg(420, 230, `
  ${axes(50, 50, 350, 0, 30, 170, '', sb(I('G'), 'dB'))}${T(404, 44, 'log ' + I('f'), '', 'end')}
  ${R(50, 62, 150, 150, 'fillR')}${L(50, 62, 200, 62, 'r')}${L(200, 62, 200, 212, 'r')}${R(260, 50, 130, 70, 'fillR')}${L(260, 120, 390, 120, 'r')}${L(260, 50, 260, 120, 'r')}
  ${courbe(u => -(u < 150 ? 2 + 6 * (u / 150) ** 4 : Math.min(160, 8 + (u - 150) * 1.3)), 0, 340, 50, 50, 1, -1, 200, 'b')}
  ${L(200, 50, 200, 216, 'dash soft')}${L(260, 50, 260, 216, 'dash soft')}${T(200, 226, sb(I('f'), '1'))}${T(260, 226, sb(I('f'), '2'))}
  ${T(36, 66, '−' + sb(I('G'), '1'), '', 'end')}${T(36, 124, '−' + sb(I('G'), '2'), '', 'end')}${L(44, 120, 56, 120)}${L(44, 62, 56, 62)}
  ${T(150, 40, 'bande passante', 'nt', 'middle')}${T(318, 40, 'bande coupée', 'nt', 'middle')}`, 'Gabarit')],

'mp-signal-2': ['Filtrage d’un créneau de fréquence f : un passe-bas avec f ≫ fc intègre (triangle) ; un passe-haut avec f ≪ fc dérive (pics aux fronts)', svg(420, 260, (() => {
  const T0 = 105, X0 = 95;
  const sq = (y, h) => { let d = `M${X0},${y - h}`; for (let k = 0; k < 3; k++) { const x = X0 + k * T0; d += ` L${x + T0 / 2},${y - h} L${x + T0 / 2},${y + h} L${x + T0},${y + h} L${x + T0},${y - h}`; } return P(d); };
  const tri = (y, h) => { let d = `M${X0},${y + h}`; for (let k = 0; k < 3; k++) { const x = X0 + k * T0; d += ` L${x + T0 / 2},${y - h} L${x + T0},${y + h}`; } return P(d, 'b'); };
  const der = (y, h) => { let d = `M${X0},${y}`; for (let k = 0; k <= 5; k++) { const x = X0 + k * T0 / 2, sg = k % 2 ? -1 : 1; d += ` L${x},${y - sg * h} ` + Array.from({length: 12}, (_, i) => `L${r2(x + i * 3)},${r2(y - sg * h * Math.exp(-i * 3 / 7))}`).join(' ') + ` L${Math.min(x + T0 / 2, X0 + 3 * T0)},${y}`; } return P(d, 'b'); };
  return `${L(X0, 45, X0 + 3 * T0 + 5, 45, 'dash soft')}${sq(45, 22)}${T(X0 - 10, 50, 'entrée', 'nt', 'end')}
  ${L(X0, 130, X0 + 3 * T0 + 5, 130, 'dash soft')}${tri(130, 22)}${T(X0 - 10, 126, 'passe-bas', 'nt', 'end')}${T(X0 - 10, 142, I('f') + ' ≫ ' + sb(I('f'), 'c'), 'nt', 'end')}
  ${L(X0, 215, X0 + 3 * T0 + 5, 215, 'dash soft')}${der(215, 30)}${T(X0 - 10, 211, 'passe-haut', 'nt', 'end')}${T(X0 - 10, 227, I('f') + ' ≪ ' + sb(I('f'), 'c'), 'nt', 'end')}`;
})(), 'Filtrage d’un créneau')],

// ---------- électronique numérique ----------
'mp-numerique-1': ['Échantillonnage : le signal continu s(t) est relevé tous les Te (période d’échantillonnage), fe = 1/Te', svg(420, 210, `
  ${axes(30, 110, 380, 0, 90, 90, I('t'), I('s'))}
  ${courbe(u => 60 * Math.sin(u / 40) + 20 * Math.sin(u / 13), 0, 370, 30, 110, 1, -1, 300, 'soft')}
  ${Array.from({length: 15}, (_, k) => { const u = k * 25, y = r2(110 - (60 * Math.sin(u / 40) + 20 * Math.sin(u / 13))); return L(30 + u, 110, 30 + u, y, 'b') + dot(30 + u, y, ''); }).join('')}
  ${D(80, 196, 105, 196, '', 0, 0)}${T(92, 190, sb(I('T'), 'e'))}`, 'Échantillonnage')],

'mp-numerique-2': ['Spectre du signal échantillonné : le spectre est répété autour des multiples de fe. Si fe > 2 fmax (critère de Shannon), les motifs sont séparés ; sinon ils se recouvrent (repliement)', svg(440, 250, (() => {
  const row = (y, fe, fm) => { const sx = 1; let s = axes(30, y, 400, 0, 70, 0, I('f'), ''); for (let k = 0; k < 4; k++) { const c = 30 + k * fe; s += P(`M${r2(c - fm)},${y} L${c},${y - 55} L${r2(c + fm)},${y}`, k ? 'b dash' : 'b') + (k ? L(c, y - 3, c, y + 3) + T(c, y + 16, (k > 1 ? k : '') + sb(I('f'), 'e')) : ''); } return s; };
  return row(90, 120, 45) + T(330, 20, sb(I('f'), 'e') + ' > 2 ' + sb(I('f'), 'max'), '', 'middle') + T(75, 104, sb(I('f'), 'max')) + row(215, 70, 50) + T(330, 145, sb(I('f'), 'e') + ' &lt; 2 ' + sb(I('f'), 'max') + ' : repliement', 'r', 'middle') + R(50, 190, 30, 25, 'fillR');
})(), 'Repliement de spectre')],

'mp-numerique-3': ['Quantification par un convertisseur analogique-numérique : la valeur est arrondie au multiple le plus proche du pas q (signal en escalier)', svg(400, 220, `
  ${axes(40, 200, 340, 0, 180, 0, I('t'), I('u'))}
  ${[1, 2, 3, 4, 5, 6, 7].map(k => L(36, 200 - k * 24, 380, 200 - k * 24, 'dash soft')).join('')}
  ${courbe(u => 80 + 70 * Math.sin(u / 50), 0, 330, 40, 200, 1, -1, 200, 'soft')}
  ${(() => { let d = ''; for (let u = 0; u <= 330; u += 15) { const v = Math.round((80 + 70 * Math.sin(u / 50)) / 24) * 24; d += (d ? ` L${40 + u},${200 - v}` : `M${40 + u},${200 - v}`) + ` L${Math.min(40 + u + 15, 370)},${200 - v}`; } return P(d, 'b'); })()}
  ${D(24, 176, 24, 152, '', 0, 0)}${T(18, 168, I('q'), '', 'end')}`, 'Quantification')],

// ---------- ondes lumineuses ----------
'mp-ondes-lumineuses-1': ['Théorème de Malus : les surfaces d’onde (Σ₁, Σ₂) sont orthogonales aux rayons ; le chemin optique entre deux surfaces d’onde est le même le long de tous les rayons', svg(400, 250, `
  ${dot(40, 115)}${T(34, 119, I('S'), '', 'end')}
  ${[-22, -11, 0, 11, 22].map(a => A(40, 115, ...pol(40, 115, 320, a), 'ray')).join('')}
  ${arc(40, 115, 130, -26, 26, 'b')}${arc(40, 115, 260, -26, 26, 'b')}
  ${T(...pol(40, 115, 140, 26), sb('Σ', '1'), 'b')}${T(...pol(40, 115, 270, 26), sb('Σ', '2'), 'b')}
  ${dot(...pol(40, 115, 130, 11))}${dot(...pol(40, 115, 260, 11))}${T(...pol(40, 115, 122, 16), I('A'))}${T(...pol(40, 115, 252, 15), I('B'))}
  ${T(200, 244, '(' + I('AB') + ') identique pour tous les rayons', 'nt', 'middle')}`, 'Malus')],

'mp-ondes-lumineuses-2': ['Modèle des trains d’onde : la source émet des trains de durée moyenne τc, de phases aléatoires ; longueur de cohérence ℓc = c τc', svg(420, 170, `
  ${axes(20, 80, 390, 0, 60, 60, I('t'), '')}
  ${courbe(u => (u < 170 ? 1 : 0) * 45 * Math.sin(u / 6), 0, 168, 20, 80, 1, -1, 300, 'b')}
  ${courbe(u => 45 * Math.sin(u / 6 + 2.1), 172, 360, 20, 80, 1, -1, 300, 'r')}
  ${L(190, 20, 190, 140, 'dash soft')}${D(20, 150, 190, 150, '', 0, 0)}${T(105, 166, sb(I('τ'), 'c'))}
  ${T(300, 18, 'saut de phase aléatoire', 'nt', 'middle')}`, 'Train d’onde')],

'mp-interferences-1': ['Intensité de deux ondes cohérentes en fonction de la différence de marche δ : I = I₁ + I₂ + 2√(I₁I₂) cos(2πδ/λ), entre Imin et Imax ; contraste C = (Imax − Imin)/(Imax + Imin)', svg(420, 200, `
  ${axes(40, 170, 370, 0, 160, 0, I('δ'), I('I'))}
  ${courbe(u => 85 + 55 * Math.cos(2 * Math.PI * (u - 30) / 120), 0, 360, 40, 170, 1, -1, 300, 'b')}
  ${L(40, 30, 400, 30, 'dash soft')}${L(40, 140, 400, 140, 'dash soft')}${T(34, 34, sb(I('I'), 'max'), '', 'end')}${T(34, 144, sb(I('I'), 'min'), '', 'end')}
  ${D(70, 20, 190, 20, '', 0, 0)}${T(130, 14, I('λ'))}`, 'I(δ)')],

// ---------- trous d’Young ----------
'mp-young-1': ['Trous d’Young : la source S éclaire deux trous S₁ et S₂ distants de a ; on observe sur un écran à la distance D ≫ a, au point M d’abscisse x', svg(420, 220, `
  ${dot(30, 110)}${T(24, 114, I('S'), '', 'end')}${L(120, 20, 120, 200, 'thick')}${R(116, 84, 8, 8, 'fillW')}${R(116, 128, 8, 8, 'fillW')}
  ${L(30, 110, 120, 88, 'ray')}${L(30, 110, 120, 132, 'ray')}${T(112, 82, sb(I('S'), '1'), '', 'end')}${T(112, 148, sb(I('S'), '2'), '', 'end')}
  ${L(380, 20, 380, 200, 'thick')}${L(120, 110, 380, 110, 'axis')}${dot(380, 50)}${T(386, 44, I('M'), '', 'start')}
  ${A(120, 88, 380, 50, 'ray')}${A(120, 132, 380, 50, 'ray')}
  ${D(100, 88, 100, 132, '', 0, 0)}${T(94, 114, I('a'), '', 'end')}${D(120, 196, 380, 196, '', 0, 0)}${T(250, 190, I('D'))}
  ${D(400, 110, 400, 50, '', 0, 0)}${T(406, 84, I('x'), '', 'start')}${T(388, 124, I('O'), '', 'start')}`, 'Trous d’Young')],

'mp-young-2': ['Différence de marche : pour D ≫ a et x, les rayons vers M sont presque parallèles, d’angle θ ≈ x/D ; δ = S₂M − S₁M = S₂H ≈ a sin θ ≈ ax/D', svg(400, 220, `
  ${L(80, 20, 80, 200, 'thick')}${dot(80, 70)}${dot(80, 150)}${T(72, 74, sb(I('S'), '1'), '', 'end')}${T(72, 154, sb(I('S'), '2'), '', 'end')}
  ${L(80, 110, 380, 110, 'axis')}
  ${A(80, 70, ...pol(80, 70, 300, 20), 'ray')}${A(80, 150, ...pol(80, 150, 320, 20), 'ray')}
  ${(() => { const s20 = Math.sin(rad(20)), c20 = Math.cos(rad(20)), hx = 80 + 80 * s20 * c20, hy = 150 - 80 * s20 * s20; return L(80, 70, r2(hx), r2(hy), 'dash soft') + dot(r2(hx), r2(hy)) + T(r2(hx + 4), r2(hy + 16), I('H'), '', 'start') + L(80, 150, r2(hx), r2(hy), 'thick r') + T(r2((80 + hx) / 2 + 6), r2((150 + hy) / 2 + 14), I('δ'), 'r', 'start'); })()}
  ${arc(80, 110, 70, 0, 20, 'b')}${T(...pol(80, 110, 82, 10), I('θ'), 'b')}${L(80, 110, ...pol(80, 110, 200, 20), 'dash soft')}
  ${D(56, 70, 56, 150, '', 0, 0)}${T(50, 114, I('a'), '', 'end')}
  ${T(290, 200, I('δ') + ' ≈ ' + I('a') + ' sin ' + I('θ') + ' ≈ ' + I('ax') + '/' + I('D'), '', 'middle')}`, 'Différence de marche')],

'mp-young-3': ['Figure d’interférences : franges rectilignes équidistantes, perpendiculaires à S₁S₂, d’interfrange i = λD/a', svg(420, 220, `
  ${Array.from({length: 80}, (_, k) => { const x = 30 + k * 4.5, v = (1 + Math.cos(2 * Math.PI * (x - 210) / 72)) / 2; return `<rect x="${r2(x)}" y="15" width="4.6" height="90" class="fillB" style="opacity:${r2(v)}"/>`; }).join('')}
  ${axes(30, 200, 380, 0, 80, 0, I('x'), I('I'))}${courbe(u => 35 + 35 * Math.cos(2 * Math.PI * (u - 180) / 72), 0, 360, 30, 200, 1, -1, 300, 'b')}
  ${L(210, 110, 210, 204, 'dash soft')}${L(282, 110, 282, 204, 'dash soft')}${D(210, 118, 282, 118, '', 0, 0)}${T(246, 134, I('i'))}${T(210, 214, '0')}`, 'Franges')],

// ---------- Michelson ----------
'mp-michelson-1': ['Interféromètre de Michelson : la séparatrice partage le faisceau vers les miroirs M₁ et M₂ ; la compensatrice (parallèle à la séparatrice) égalise les traversées de verre ; les deux ondes se recombinent vers l’écran', svg(420, 260, `
  ${dot(30, 120)}${T(24, 124, I('S'), '', 'end')}${lens(80, 120, 60)}
  ${L(80, 120, 200, 120, 'ray')}${L(200, 120, 330, 120, 'ray')}${L(200, 120, 200, 30, 'ray')}${L(200, 120, 200, 230, 'ray')}
  ${A(240, 120, 270, 120, 'ray')}${A(200, 70, 200, 50, 'ray')}${A(200, 170, 200, 200, 'ray')}
  ${L(178, 142, 222, 98, 'thick b')}${L(192, 156, 236, 112, 'thick soft')}${T(240, 92, 'séparatrice', 'nt', 'start')}${T(244, 146, 'compensatrice', 'nt', 'start')}
  ${L(340, 90, 340, 150, 'thick')}${T(352, 124, sb(I('M'), '2'), '', 'start')}${L(170, 22, 230, 22, 'thick')}${T(236, 26, sb(I('M'), '1'), '', 'start')}${A(150, 22, 150, 46, 'soft')}${T(144, 40, 'translation', 'nt', 'end')}
  ${L(160, 240, 240, 240, 'thick soft')}${T(250, 244, 'écran (ou lentille + écran)', 'nt', 'start')}`, 'Michelson')],

'mp-michelson-2': ['Lame d’air (M₁ et M₂′ parallèles, épaisseur e) : deux rayons réfléchis parallèles, δ = 2e cos i ; interférences localisées à l’infini, anneaux concentriques', svg(420, 220, `
  ${L(30, 70, 280, 70, 'thick')}${L(30, 130, 280, 130, 'thick')}${T(286, 74, sb(I('M'), '1'), '', 'start')}${T(286, 134, I('M') + '′' + sb('', '2'), '', 'start')}
  ${D(40, 70, 40, 130, '', 0, 0)}${T(48, 104, I('e'), '', 'start')}
  ${(() => { const i = 30, t = Math.tan(rad(i)); const a = [100, 70], b = [100 + 60 * t, 130], c = [100 + 120 * t, 70]; return A(100 - 70 * t, 0, ...a, 'ray') + L(...a, ...b.map(r2), 'ray') + L(...b.map(r2), ...c.map(r2), 'ray') + A(...a, r2(a[0] + 70 * t), 0, 'ray') + A(...c.map(r2), r2(c[0] + 70 * t), 0, 'ray') + L(100, 10, 100, 150, 'dash soft') + arc(100, 70, 30, 90, 90 - 30, 'b') + T(...pol(100, 70, 40, 74), I('i'), 'b'); })()}
  ${[10, 20, 28, 34, 40].map(r => C(370, 100, r, 'b')).join('')}${T(370, 160, 'anneaux à l’infini', 'nt', 'middle')}
  ${T(160, 200, I('δ') + ' = 2' + I('e') + ' cos ' + I('i'), '', 'middle')}`, 'Lame d’air')],

'mp-michelson-3': ['Coin d’air (M₁ et M₂′ font un petit angle α) : sous incidence quasi normale, franges rectilignes parallèles à l’arête, localisées au voisinage des miroirs, d’interfrange λ/(2α)', svg(420, 200, `
  ${L(30, 150, 280, 150, 'thick')}${L(30, 150, 280, 90, 'thick')}${T(286, 154, I('M') + '′' + sb('', '2'), '', 'start')}${T(286, 94, sb(I('M'), '1'), '', 'start')}
  ${arc(30, 150, 50, 0, 13.5, 'b')}${T(...pol(30, 150, 62, 6), I('α'), 'b')}${T(30, 170, 'arête', 'nt', 'middle')}
  ${[120, 180, 240].map(x => A(x, 20, x, 145, 'ray')).join('')}
  ${Array.from({length: 10}, (_, k) => R(320 + k * 9, 40, 4.5, 110, 'fillB')).join('')}${T(362, 172, 'franges ∥ arête', 'nt', 'middle')}`, 'Coin d’air')],

// ---------- N ondes ----------
'mp-n-ondes-1': ['Réseau par transmission de pas a : entre deux traits voisins, différence de marche δ = a (sin θ − sin θi) ; maxima principaux pour a (sin θ − sin θi) = pλ', svg(420, 240, `
  ${L(200, 15, 200, 225, 'thick')}${[60, 100, 140, 180].map(y => R(197, y - 3, 6, 6, 'fillW')).join('')}
  ${[60, 100, 140, 180].map(y => A(...pol(200, y, 160, 180 + 25).map((v, i) => i ? r2(v) : v), 200, y, 'ray') + A(200, y, ...pol(200, y, 170, 18), 'ray')).join('')}
  ${L(200, 140, 380, 140, 'axis')}${L(200, 140, 20, 140, 'axis')}
  ${arc(200, 140, 60, 0, 18, 'b')}${T(...pol(200, 140, 74, 9), I('θ'), 'b')}${arc(200, 140, 60, 180, 180 + 25, 'b')}${T(...pol(200, 140, 74, 192), sb(I('θ'), 'i'), 'b')}
  ${D(220, 100, 220, 140, '', 0, 0)}${T(226, 124, I('a'), '', 'start')}`, 'Réseau')],

'mp-n-ondes-2': ['Intensité de N ondes de même amplitude déphasées de φ : maxima principaux pour φ = 2pπ, de largeur en 1/N ; pour N grand, des pics très fins (intensités normalisées)', svg(420, 220, `
  ${axes(30, 190, 380, 0, 170, 0, I('φ'), I('I') + '/' + sb(I('I'), 'max'))}
  ${courbe(u => { const f = (u - 180) / 70 * Math.PI; return 150 * Math.cos(f / 2) ** 2; }, 0, 370, 30, 190, 1, -1, 400, 'soft dash')}
  ${courbe(u => { const f = (u - 180) / 70 * Math.PI, N = 8, d = Math.sin(f / 2); return Math.abs(d) < 1e-6 ? 150 : 150 * (Math.sin(N * f / 2) / (N * d)) ** 2; }, 0, 370, 30, 190, 1, -1, 800, 'b')}
  ${[70, 210, 350].map((x, k) => T(x, 204, ['−2π', '0', '2π'][k])).join('')}
  ${T(300, 60, I('N') + ' = 8', 'b', 'middle')}${T(300, 80, I('N') + ' = 2', 'nt', 'middle')}`, 'N ondes')],
};
