// Schémas des fiches de cours — Physique MPSI, partie 5 : Induction ; annexe : mesures et incertitudes.
import { svg, L, A, D, T, I, V, C, R, P, dot, sb, ox, ot } from './figkit.js';
import { axes, courbe, res, gene, fil, ten, cour } from './fiches-kit.js';

const r2 = n => Math.round(n * 100) / 100;
const pth = pts => 'M' + pts.map(p => p.map(r2).join(',')).join(' L');
const mid = (pts, c = '', rev = false) => { const k = Math.floor(pts.length / 2), a = pts[k - 1], b = pts[k + 1]; return rev ? A(r2(b[0]), r2(b[1]), r2(a[0]), r2(a[1]), c) : A(r2(a[0]), r2(a[1]), r2(b[0]), r2(b[1]), c); };
// ligne de champ d'un dipôle : r = c sin²θ (θ depuis l'axe du dipôle, horizontal)
const ldip = (cx, cy, c, haut = true) => Array.from({length: 121}, (_, i) => { const t = 0.12 + (Math.PI - 0.24) * i / 120, r = c * Math.sin(t) ** 2; return [cx + r * Math.cos(t), cy - (haut ? 1 : -1) * r * Math.sin(t)]; });

export const FIGS = {
'p5-champ-b-1': ['Lignes de champ d’un aimant droit : à l’extérieur, elles sortent par le pôle nord et rentrent par le pôle sud', svg(400, 300, (() => {
  let s = '';
  [[4, 40, 30], [8, 75, 60], [11, 115, 95], [13, 160, 135]].forEach(([k, w, h]) => [1, -1].forEach(sg => {
    const y0 = 150 - sg * k, yc = 150 - sg * h;
    s += `<path d="M250,${y0} C${250 + w},${yc} ${150 - w},${yc} 150,${y0}" class="s soft"/>`;
    const ym = 150 - sg * (0.75 * h + 0.25 * k);   // sommet de la courbe de Bézier (t = ½)
    s += A(204, r2(ym), 196, r2(ym));
  }));
  return `${s}${A(254, 150, 390, 150, 'soft')}${A(10, 150, 146, 150, 'soft')}
  ${R(150, 136, 50, 28, 'fillA')}${R(200, 136, 50, 28, 'fillR')}${T(175, 155, 'S')}${T(225, 155, 'N')}`;
})(), 'Aimant droit')],

'p5-champ-b-2': ['Fil rectiligne infini parcouru par I (sortant, ⊙) : lignes de champ circulaires, sens donné par la règle de la main droite, B = μ₀I/(2πr)', svg(320, 230, `
  ${[40, 70, 100].map(r => C(160, 115, r, 'b') + A(160 + r * 0.7071 + 2, 115 - r * 0.7071 + 2, 160 + r * 0.7071 - 2, 115 - r * 0.7071 - 2, 'b')).join('')}
  ${ox(160, 115)}${T(172, 132, I('I'), '', 'start')}${dot(230.7, 44.3)}${T(244, 46, V('B'), 'b', 'start')}${L(160, 115, 230.7, 44.3, 'dash soft')}${T(206, 92, I('r'), '', 'start')}`, 'Fil rectiligne')],

'p5-champ-b-3': ['Spire circulaire (coupe dans un plan contenant l’axe) : lignes de champ et champ sur l’axe', svg(400, 240, (() => {
  let s = '';
  [[200, 60, 1], [200, 180, -1]].forEach(([x, y, sg]) => [18, 34, 52].forEach(r => { s += `<ellipse cx="${x}" cy="${y}" rx="${r}" ry="${r * 0.9}" class="s soft"/>`; }));
  return `${s}${L(200, 60, 200, 180, 'dash soft')}${ox(200, 60)}${ot(200, 180)}${T(212, 52, I('I'), '', 'start')}
  ${A(20, 120, 380, 120, 'b')}${T(384, 124, V('B'), 'b', 'start')}${A(200 - 18, 60 - 16, 200 - 26, 60 - 8, 'soft')}${A(200 - 18, 180 + 16, 200 - 26, 180 + 8, 'soft')}
  ${T(70, 112, 'axe de la spire', 'nt', 'middle')}`;
})(), 'Spire circulaire')],

'p5-champ-b-4': ['Solénoïde (coupe) : champ quasi uniforme à l’intérieur, B = μ₀ n I, très faible à l’extérieur', svg(400, 220, `
  ${[80, 120, 160, 200, 240, 280, 320].map(x => ox(x, 60) + ot(x, 160)).join('')}${T(330, 46, I('I'), '', 'start')}
  ${[85, 110, 135].map(y => A(60, y, 340, y, 'b')).join('')}${T(352, 114, V('B'), 'b', 'start')}
  <path d="M340,110 C390,110 395,24 300,24 L100,24 C5,24 10,110 60,110" class="s soft"/><path d="M340,110 C390,110 395,196 300,196 L100,196 C5,196 10,110 60,110" class="s soft"/>
  ${A(210, 24, 190, 24, 'soft')}${A(210, 196, 190, 196, 'soft')}`, 'Solénoïde')],

'p5-actions-1': ['Rails de Laplace (vue de dessus, B entrant ⊗) : la barre parcourue par I subit F = I L ∧ B', svg(420, 220, `
  ${L(60, 50, 380, 50, 'thick')}${L(60, 170, 380, 170, 'thick')}${gene(60, 50, 60, 170)}${T(36, 114, I('E'), '', 'end')}
  ${L(250, 40, 250, 180, 'thick r')}${A(238, 70, 238, 130, 'r')}${T(232, 100, I('I'), 'r', 'end')}
  ${A(250, 110, 320, 110, '')}${T(326, 114, V('F'), '', 'start')}
  ${[110, 160, 340].map(x => ot(x, 90) + ot(x, 135)).join('')}${T(112, 116, V('B'), '', 'start')}${D(200, 50, 200, 170, '', 0, 0)}${T(192, 114, I('L'), '', 'end')}`, 'Rails de Laplace')],

'p5-actions-2': ['Spire dans un champ uniforme : couple Γ = m ∧ B qui tend à aligner le moment magnétique m = I S n sur B', svg(380, 220, `
  ${[50, 100, 150].map(y => A(30, y + 10, 350, y + 10, 'soft')).join('')}${T(356, 64, V('B'), '', 'start')}
  ${L(150, 160, 230, 60, 'thick')}${dot(190, 110)}${A(190, 110, 268, 172, 'b')}${T(274, 180, V('m'), 'b', 'start')}
  <path d="M240,110 A50,50 0 0 1 229,141" class="s"/>${T(246, 134, 'θ', '', 'start')}
  <path d="M120,60 A80,80 0 0 0 110,140" class="s r"/>${A(112, 136, 110, 142, 'r')}${T(96, 100, 'Γ', 'r', 'end')}${T(200, 210, 'vue en coupe de la spire', 'nt')}`, 'Spire dans B')],

'p5-induction-1': ['Flux du champ magnétique à travers une surface orientée : Φ = ∬ B·n dS, n orienté par le sens du contour (main droite)', svg(380, 220, `
  <ellipse cx="190" cy="130" rx="120" ry="40" class="s fillA"/>${A(296, 148, 284, 154, 'r')}${T(300, 166, 'sens du contour', 'r', 'start')}
  ${A(190, 130, 190, 50, 'b')}${T(198, 56, V('n'), 'b', 'start')}${[110, 150, 230, 270].map(x => A(x - 30, 210, x + 20, 20, 'soft')).join('')}${T(300, 30, V('B'), '', 'start')}
  ${T(120, 136, I('S'), '')}`, 'Flux')],

'p5-induction-2': ['Loi de Lenz : quand le pôle nord s’approche, le courant induit crée un champ qui s’oppose à l’augmentation du flux (répulsion)', svg(420, 200, `
  ${R(30, 85, 50, 30, 'fillA')}${R(80, 85, 50, 30, 'fillR')}${T(55, 104, 'S')}${T(105, 104, 'N')}${A(70, 140, 120, 140, '')}${T(95, 160, 'mouvement', 'nt')}
  ${[90, 100, 110].map(y => A(140, y, 240, y, 'soft')).join('')}${T(190, 82, V('B') + ' aimant', 'nt')}
  <ellipse cx="290" cy="100" rx="18" ry="60" class="s thick"/>${A(282, 44, 296, 42, 'r')}${T(300, 34, sb(I('i'), 'induit'), 'r', 'start')}
  ${A(330, 100, 260, 100, 'b')}${T(338, 104, sb(V('B'), 'induit'), 'b', 'start')}`, 'Loi de Lenz')],

'p5-circuit-fixe-1': ['Deux circuits couplés : le flux du champ créé par i₁ à travers le circuit 2 vaut Φ₁→₂ = M i₁', svg(420, 200, `
  ${[0, 1, 2, 3].map(k => `<ellipse cx="${110 + k * 18}" cy="100" rx="8" ry="40" class="s"/>`).join('')}${[0, 1, 2, 3].map(k => `<ellipse cx="${270 + k * 18}" cy="100" rx="8" ry="40" class="s"/>`).join('')}
  ${[80, 100, 120].map(y => L(90, y, 350, y, 'soft')).join('')}${A(220, 100, 240, 100, 'soft')}
  ${T(137, 160, 'circuit 1 : ' + sb(I('i'), '1'), '', 'middle')}${T(297, 160, 'circuit 2', '', 'middle')}${T(220, 40, 'flux commun', 'nt')}
  ${T(210, 190, sb('Φ', '1→2') + ' = ' + I('M') + sb(I('i'), '1') + ',  ' + sb('Φ', '2→1') + ' = ' + I('M') + sb(I('i'), '2'), 'nt')}`, 'Inductance mutuelle')],

'p5-circuit-fixe-2': ['Transformateur : primaire de N₁ spires, secondaire de N₂ spires sur un même noyau ; |u₂/u₁| = N₂/N₁', svg(420, 220, `
  ${P('M130,30 H290 V190 H130 Z M155,55 H265 V165 H155 Z', 'fillA')}
  ${[0, 1, 2, 3, 4].map(k => L(118, 70 + k * 18, 166, 62 + k * 18, 'thick')).join('')}${[0, 1, 2].map(k => L(254, 80 + k * 25, 302, 72 + k * 25, 'thick')).join('')}
  ${L(118, 70, 60, 70)}${L(118, 142, 60, 142)}${L(302, 72, 360, 72)}${L(302, 122, 360, 122)}
  ${ten(50, 142, 50, 70, sb(I('u'), '1'), -1)}${ten(370, 122, 370, 72, sb(I('u'), '2'))}${T(140, 20, sb(I('N'), '1'), '', 'middle')}${T(280, 20, sb(I('N'), '2'), '', 'middle')}${T(210, 112, 'noyau', 'nt')}`, 'Transformateur')],

'p5-circuit-mobile-1': ['Rails de Laplace en générateur : la barre poussée à la vitesse v est le siège d’une f.é.m. e = −dΦ/dt ; schéma électrique équivalent', svg(460, 210, `
  ${L(40, 50, 260, 50, 'thick')}${L(40, 160, 260, 160, 'thick')}${res(40, 50, 40, 160)}${T(22, 108, I('R'), '', 'end')}
  ${L(190, 40, 190, 170, 'thick r')}${A(190, 105, 240, 105, '')}${T(246, 110, V('v'), '', 'start')}${[90, 140, 225].map(x => ot(x, 80) + ot(x, 130)).join('')}${T(92, 106, V('B'), '', 'start')}
  ${gene(370, 60, 370, 150)}${ten(394, 150, 394, 60, I('e'))}${fil(370, 60, 370, 40)}${fil(370, 40, 440, 40)}${res(440, 40, 440, 170)}${fil(440, 170, 370, 170)}${fil(370, 170, 370, 150)}
  ${T(452, 108, I('R'), '', 'start')}${T(405, 200, 'circuit équivalent', 'nt')}`, 'Rails générateurs')],

'p5-circuit-mobile-2': ['Alternateur : cadre de N spires tournant à ω autour de Δ ⟂ B ; Φ = NBS cos ωt et e = NBSω sin ωt', svg(380, 220, `
  ${[50, 100, 150].map(y => A(20, y + 10, 360, y + 10, 'soft')).join('')}${T(364, 64, V('B'), '', 'start')}
  ${L(190, 20, 190, 200, 'axis')}${T(198, 24, 'Δ', '', 'start')}
  <path d="M150,50 L230,70 L230,170 L150,150 Z" class="s fillA"/>${A(190, 110, 250, 70, 'b')}${T(256, 66, V('n'), 'b', 'start')}
  <path d="M240,110 A50,50 0 0 0 232,82" class="s"/>${T(246, 100, 'θ = ω' + I('t'), '', 'start')}<path d="M170,15 A20,8 0 1 0 210,15" class="s r"/>${A(208, 17, 211, 13, 'r')}${T(160, 14, 'ω', 'r', 'end')}`, 'Alternateur')],

'px-incertitudes-1': ['Distribution de mesures répétées : moyenne et écart-type ; l’incertitude-type sur la moyenne vaut σ/√N', svg(400, 220, (() => {
  const X0 = 40, Y0 = 190, mu = 170, sg = 45, g = x => 140 * Math.exp(-((x - mu) ** 2) / (2 * sg * sg));
  const bars = [6, 18, 44, 80, 118, 140, 122, 84, 46, 20, 7];
  return `${axes(X0, Y0, 340, 0, 175, 0, 'valeur mesurée', 'effectif')}${bars.map((h, k) => R(X0 + 40 + k * 24, Y0 - h, 24, h, 'fillA')).join('')}
  ${courbe(g, 0, 330, X0, Y0, 1, -1, 200, 'b')}${L(X0 + mu, Y0, X0 + mu, Y0 - 146, 'r')}${T(X0 + mu, Y0 - 152, 'moyenne', 'r')}
  ${D(X0 + mu - sg, Y0 - 82, X0 + mu, Y0 - 82, 'σ', X0 + mu - sg / 2, Y0 - 88)}`;
})(), 'Distribution')],

'px-incertitudes-2': ['Régression linéaire : points avec leurs barres d’incertitude et droite modèle ; les écarts doivent être compatibles avec les incertitudes', svg(400, 220, (() => {
  const X0 = 40, Y0 = 190, pts = [[30, 28], [70, 52], [110, 70], [150, 101], [190, 118], [230, 142], [270, 161], [310, 188]];
  return `${axes(X0, Y0, 340, 0, 180, 0, I('x'), I('y'))}${L(X0 + 10, Y0 - 16, X0 + 330, Y0 - 16 - 320 * 0.585, 'b')}
  ${pts.map(([x, y]) => L(X0 + x, Y0 - y - 9, X0 + x, Y0 - y + 9) + L(X0 + x - 4, Y0 - y - 9, X0 + x + 4, Y0 - y - 9) + L(X0 + x - 4, Y0 - y + 9, X0 + x + 4, Y0 - y + 9) + dot(X0 + x, Y0 - y)).join('')}
  ${T(330, 170, I('y') + ' = ' + I('a') + I('x') + ' + ' + I('b'), 'b', 'end')}`;
})(), 'Régression')],
};
