// Schémas des fiches de cours — Physique MP : thermodynamique (systèmes ouverts, diffusion, statistique) et physique quantique.
import { svg, L, A, D, T, I, V, C, R, P, dot, sb, wallV } from './figkit.js';
import { axes, courbe, res, fil } from './fiches-kit.js';

const r2 = n => Math.round(n * 100) / 100;
const g = (u, m, s) => Math.exp(-(((u - m) / s) ** 2) / 2);

export const FIGS = {
// ---------- systèmes ouverts ----------
'mp-systemes-ouverts-1': ['Système fermé fictif : à l’instant t, il est formé du fluide contenu dans le volume de contrôle Σ et de la masse δme qui va entrer ; à t + dt, du fluide dans Σ et de la masse δms sortie. En régime stationnaire, δme = δms = Dm dt', svg(440, 200, `
  ${P('M20,60 L180,60 C230,60 250,80 300,80 L420,80')}${P('M20,150 L180,150 C230,150 250,130 300,130 L420,130')}
  ${R(70, 60, 30, 90, 'fillR')}${R(330, 80, 22, 50, 'fillA')}${L(100, 50, 100, 160, 'dash b')}${L(330, 70, 330, 140, 'dash b')}
  ${T(215, 108, 'Σ', 'b', 'middle')}${T(85, 178, 'δ' + sb(I('m'), 'e'), 'r')}${T(341, 158, 'δ' + sb(I('m'), 's'), 'b')}
  ${A(20, 105, 62, 105)}${A(360, 105, 410, 105)}${T(30, 44, 'entrée', 'nt', 'start')}${T(410, 66, 'sortie', 'nt', 'end')}`, 'Système fermé fictif')],

'mp-systemes-ouverts-2': ['Symboles des organes usuels : compresseur et turbine (échange de travail utile wu, en général adiabatiques), détendeur (isenthalpique), tuyère, échangeur thermique (échange de chaleur q)', svg(460, 200, `
  ${P('M20,60 L80,75 L80,125 L20,140 Z', 'fillA')}${A(50, 20, 50, 58, 'r')}${T(56, 34, sb(I('w'), 'u'), 'r', 'start')}${T(50, 165, 'compresseur', 'nt')}
  ${P('M110,75 L170,60 L170,140 L110,125 Z', 'fillA')}${A(140, 62, 140, 22, 'r')}${T(146, 34, sb(I('w'), 'u'), 'r', 'start')}${T(140, 165, 'turbine', 'nt')}
  ${P('M210,85 L240,100 L210,115 Z', 'fillW')}${P('M270,85 L240,100 L270,115 Z', 'fillW')}${L(195, 100, 210, 100)}${L(270, 100, 285, 100)}${T(240, 165, 'détendeur', 'nt')}
  ${P('M305,70 L345,88 L345,112 L305,130')}${T(325, 165, 'tuyère', 'nt')}
  ${R(370, 70, 70, 60, 'fillW')}${P('M370,115 L385,85 L400,115 L415,85 L430,115 L440,100', 'b')}${A(405, 22, 405, 66, 'r')}${T(411, 34, I('q'), 'r', 'start')}${T(405, 165, 'échangeur', 'nt')}
  ${A(4, 185, 456, 185, 'soft')}${T(230, 198, 'sens de l’écoulement', 'nt')}`, 'Organes')],

'mp-systemes-ouverts-3': ['Cycle d’une machine frigorifique dans le diagramme (log P, h) : compression 1→2, condensation 2→3, détente isenthalpique 3→4, évaporation 4→1 ; la cloche de saturation sépare liquide, mélange et vapeur', svg(420, 250, `
  ${axes(40, 220, 370, 0, 205, 0, I('h'), 'log ' + I('P'))}
  <path d="M80,215 C110,90 160,40 210,38 C260,40 300,110 330,215" class="s soft"/>${T(205, 30, 'point critique', 'nt', 'middle')}
  ${T(70, 120, 'liquide', 'nt', 'middle')}${T(370, 140, 'vapeur', 'nt', 'middle')}${T(205, 150, 'L + V', 'nt', 'middle')}
  ${P('M310,165 L360,80 L120,80 L120,165 Z', 'b')}${A(340, 115, 352, 94, 'b')}${A(230, 80, 200, 80, 'b')}${A(120, 120, 120, 140, 'b')}${A(200, 165, 230, 165, 'b')}
  ${[[310, 165, '1', 'start', 8, 16], [360, 80, '2', 'start', 6, -4], [120, 80, '3', 'end', -6, -4], [120, 165, '4', 'end', -6, 16]].map(([x, y, t, a, dx, dy]) => dot(x, y) + T(x + dx, y + dy, t, 'b', a)).join('')}`, 'Diagramme (P,h)')],

// ---------- diffusion thermique ----------
'mp-diffusion-1': ['Bilan d’énergie sur une tranche de section S entre x et x + dx : la variation d’énergie interne pendant dt est due à la différence entre le flux entrant en x et le flux sortant en x + dx', svg(400, 200, `
  ${P('M40,60 L360,60 M40,140 L360,140', '')}${R(160, 60, 70, 80, 'fillY')}
  ${A(100, 100, 158, 100, 'r')}${T(110, 90, I('Φ') + '(' + I('x') + ')', 'r', 'middle')}${A(232, 100, 290, 100, 'r')}${T(290, 90, I('Φ') + '(' + I('x') + ' + d' + I('x') + ')', 'r', 'middle')}
  ${L(160, 140, 160, 160, 'soft')}${L(230, 140, 230, 160, 'soft')}${T(160, 176, I('x'))}${T(230, 176, I('x') + ' + d' + I('x'))}${A(40, 190, 360, 190, 'soft')}${T(195, 108, I('S'), '', 'middle')}`, 'Bilan sur une tranche')],

'mp-diffusion-2': ['Mur composé de deux couches en régime stationnaire : profil de température affine dans chaque couche ; analogie électrique, les résistances thermiques Rth = e/(λS) s’ajoutent en série', svg(420, 240, `
  ${R(120, 20, 60, 120, 'fillY')}${R(180, 20, 100, 120, 'fillA')}${T(150, 152, sb('λ', '1'), '', 'middle')}${T(230, 152, sb('λ', '2'), '', 'middle')}
  ${P('M40,30 L120,30 L180,110 L280,130 L360,130', 'r')}${T(40, 24, sb(I('T'), '1'), 'r', 'start')}${T(360, 124, sb(I('T'), '2'), 'r', 'end')}${A(300, 80, 360, 80)}${T(330, 72, I('Φ'))}
  ${fil(40, 200, 80, 200)}${res(80, 200, 160, 200)}${fil(160, 200, 220, 200)}${res(220, 200, 300, 200)}${fil(300, 200, 360, 200)}
  ${dot(40, 200)}${dot(190, 200)}${dot(360, 200)}${T(40, 222, sb(I('T'), '1'))}${T(190, 222, sb(I('T'), 'i'))}${T(360, 222, sb(I('T'), '2'))}${T(120, 190, sb(I('R'), '1'))}${T(260, 190, sb(I('R'), '2'))}${A(330, 186, 352, 186, 'r')}`, 'Résistance thermique')],

'mp-diffusion-3': ['Conducto-convection : le flux échangé entre une paroi à Tp et un fluide à Text suit la loi de Newton Φ = h S (Tp − Text), h coefficient d’échange', svg(400, 200, `
  ${R(30, 20, 90, 160, 'fillY')}${L(120, 20, 120, 180, 'thick')}${T(75, 104, sb(I('T'), 'p'), '', 'middle')}
  ${courbe(u => 60 + 70 * Math.exp(-u / 25), 0, 250, 120, 190, 1, -1, 200, 'r')}${L(120, 130, 370, 130, 'dash soft')}${T(370, 124, sb(I('T'), 'ext'), 'r', 'end')}
  ${A(140, 40, 210, 40, 'r')}${T(220, 44, I('Φ') + ' = ' + I('hS') + '(' + sb(I('T'), 'p') + ' − ' + sb(I('T'), 'ext') + ')', 'r', 'start')}${T(250, 170, 'fluide', 'nt', 'middle')}`, 'Conducto-convection')],

// ---------- quantique ----------
'mp-quantique-1': ['Densité de probabilité de présence |ψ(x)|² : l’aire sous la courbe entre a et b est la probabilité de trouver la particule dans [a, b] ; l’aire totale vaut 1', svg(400, 200, `
  ${axes(30, 170, 360, 0, 150, 0, I('x'), '|' + I('ψ') + '|²')}
  ${P('M' + Array.from({length: 61}, (_, i) => { const u = 150 + i; return r2(30 + u) + ',' + r2(170 - 120 * (0.7 * g(u, 150, 40) + 0.45 * g(u, 250, 30))); }).join(' L') + ' L240,170 L180,170 Z', 'fillA')}
  ${courbe(u => 120 * (0.7 * g(u, 150, 40) + 0.45 * g(u, 250, 30)), 0, 350, 30, 170, 1, -1, 300, 'b')}
  ${T(180, 186, I('a'))}${T(240, 186, I('b'))}${T(210, 140, I('P'), 'b', 'middle')}`, 'Densité de probabilité')],

'mp-quantique-2': ['Inégalité de Heisenberg Δx Δp ≥ ℏ/2 : un paquet d’ondes étroit en position est large en vecteur d’onde, et inversement', svg(420, 220, `
  ${axes(20, 90, 180, 0, 70, 0, I('x'), '')}${courbe(u => 65 * g(u, 90, 12), 0, 180, 20, 90, 1, -1, 200, 'b')}
  ${axes(230, 90, 180, 0, 70, 0, I('k'), '')}${courbe(u => 65 * g(u, 90, 40), 0, 180, 230, 90, 1, -1, 200, 'r')}
  ${axes(20, 200, 180, 0, 70, 0, I('x'), '')}${courbe(u => 65 * g(u, 90, 40), 0, 180, 20, 200, 1, -1, 200, 'b')}
  ${axes(230, 200, 180, 0, 70, 0, I('k'), '')}${courbe(u => 65 * g(u, 90, 12), 0, 180, 230, 200, 1, -1, 200, 'r')}
  ${D(98, 46, 122, 46, '', 0, 0)}${T(110, 38, 'Δ' + I('x'))}${D(278, 46, 362, 46, '', 0, 0)}${T(320, 38, 'Δ' + I('k'))}
  ${D(70, 156, 150, 156, '', 0, 0)}${T(110, 148, 'Δ' + I('x'))}${D(308, 156, 332, 156, '', 0, 0)}${T(320, 148, 'Δ' + I('k'))}`, 'Heisenberg')],

'mp-libre-1': ['Paquet d’ondes d’une particule libre : |ψ|² se déplace à la vitesse de groupe et s’étale au cours du temps (aire constante)', svg(420, 190, `
  ${axes(20, 170, 390, 0, 150, 0, I('x'), '|' + I('ψ') + '|²')}
  ${[[80, 18, 'b', sb(I('t'), '0')], [200, 30, 'b dash', sb(I('t'), '1')], [320, 45, 'b soft', sb(I('t'), '2')]].map(([m, s, c, t]) => courbe(u => 140 * 18 / s * g(u, m, s), 0, 390, 20, 170, 1, -1, 300, c) + T(20 + m, r2(170 - 140 * 18 / s) - 8, t, 'b')).join('')}`, 'Étalement')],

'mp-potentiel-1': ['Marche de potentiel de hauteur V₀ : si E > V₀, onde progressive de part et d’autre (avec réflexion partielle) ; si E &lt; V₀, onde évanescente au-delà de la marche (réflexion totale)', svg(440, 220, (() => {
  const pan = (x0, Ehaut) => {
    const y0 = 190, yV = 110, yE = Ehaut ? 60 : 150, w = 200;
    let s = A(x0, y0, x0 + w, y0, 'soft') + P(`M${x0},${y0} L${x0 + 100},${y0} L${x0 + 100},${yV} L${x0 + w},${yV}`, 'thick') + L(x0, yE, x0 + w, yE, 'dash r') + T(x0 + w, yE - 26, I('E'), 'r', 'end') + T(x0 + 106, yV + 16, sb(I('V'), '0'), '', 'start');
    const ph = Ehaut ? 0 : 0.405;                  // raccord de ψ et de ψ′ en x = 0
    s += courbe(u => 16 * Math.cos((u - 100) / 6 + ph), 0, 100, x0, yE, 1, -1, 200, 'b');
    s += Ehaut ? courbe(u => 16 * Math.cos((u - 100) / 11), 100, 200, x0, yE, 1, -1, 200, 'b') : courbe(u => 16 * Math.cos(ph) * Math.exp(-(u - 100) / 14), 100, 200, x0, yE, 1, -1, 200, 'b');
    return s;
  };
  return pan(10, true) + T(110, 214, I('E') + ' > ' + sb(I('V'), '0'), 'nt', 'middle') + pan(230, false) + T(330, 214, I('E') + ' &lt; ' + sb(I('V'), '0') + ' : évanescente', 'nt', 'middle');
})(), 'Marche de potentiel')],

'mp-potentiel-2': ['Puits infini de largeur L : énergies quantifiées En = n² π²ℏ²/(2mL²) ; fonctions d’onde ψn ∝ sin(nπx/L), nulles sur les parois', svg(380, 260, `
  ${L(100, 20, 100, 240, 'thick')}${L(300, 20, 300, 240, 'thick')}${L(100, 240, 300, 240, 'thick')}${T(100, 256, '0')}${T(300, 256, I('L'))}
  ${[[1, 215], [2, 165], [3, 80]].map(([n, y]) => L(100, y, 300, y, 'dash soft') + courbe(u => 20 * Math.sin(n * Math.PI * u / 200), 0, 200, 100, y, 1, -1, 200, 'b') + T(310, y + 4, sb(I('E'), n) + (n > 1 ? ' = ' + n * n + sb(I('E'), 1) : ''), '', 'start')).join('')}`, 'Puits infini')],

'mp-potentiel-3': ['Effet tunnel : une particule d’énergie E &lt; V₀ traverse une barrière de largeur a avec une probabilité non nulle ; l’onde décroît exponentiellement dans la barrière, l’onde transmise est atténuée', svg(420, 200, `
  ${A(10, 170, 410, 170, 'soft')}${P('M10,170 L170,170 L170,60 L250,60 L250,170 L410,170', 'thick')}${R(170, 60, 80, 110, 'fillY')}
  ${L(10, 110, 410, 110, 'dash r')}${T(406, 104, I('E'), 'r', 'end')}${T(210, 54, sb(I('V'), '0'))}
  ${courbe(u => 30 * Math.cos((u - 160) / 7), 0, 160, 10, 110, 1, -1, 300, 'b')}${courbe(u => 30 * Math.cosh(0) * Math.exp(-(u - 160) / 30) * Math.cos(0), 160, 240, 10, 110, 1, -1, 100, 'b')}
  ${courbe(u => 30 * Math.exp(-80 / 30) * Math.cos((u - 240) / 7), 240, 400, 10, 110, 1, -1, 300, 'b')}
  ${D(170, 186, 250, 186, '', 0, 0)}${T(210, 180, I('a'))}`, 'Effet tunnel')],

'mp-potentiel-4': ['Puits de profondeur finie : nombre fini d’états liés ; les fonctions d’onde débordent du puits (ondes évanescentes), d’où des énergies un peu plus basses que pour le puits infini', svg(400, 230, `
  ${P('M20,40 L120,40 L120,210 L280,210 L280,40 L380,40', 'thick')}${T(26, 34, sb(I('V'), '0'), '', 'start')}
  ${[[1, 175, 1.2, 0.0386], [2, 110, 2.5, 0.0419]].map(([n, y, ka, kp]) => { const k = ka / 80, A0 = 22;
    const f = u => { const d = u - 180, ad = Math.abs(d); if (n === 1) return A0 * (ad < 80 ? Math.cos(k * d) : Math.cos(ka) * Math.exp(-kp * (ad - 80))); return A0 * (ad < 80 ? Math.sin(k * d) : Math.sign(d) * Math.sin(ka) * Math.exp(-kp * (ad - 80))); };
    return L(20, y, 380, y, 'dash soft') + courbe(f, 0, 360, 20, y, 1, -1, 300, 'b') + T(392, y + 4, sb(I('E'), n), '', 'end'); }).join('')}
`, 'Puits fini')],

// ---------- statistique ----------
'mp-statistique-1': ['Atmosphère isotherme : la densité de particules décroît exponentiellement avec l’altitude, n(z) = n₀ exp(−mgz/(kBT)), hauteur caractéristique H = kBT/(mg)', svg(380, 220, `
  ${axes(40, 200, 320, 0, 185, 0, I('n'), I('z'))}
  ${P(Array.from({length: 101}, (_, i) => { const z = i * 1.8; return (i ? 'L' : 'M') + r2(40 + 280 * Math.exp(-z / 50)) + ',' + r2(200 - z); }).join(' '), 'b')}
  ${L(40, 150, r2(40 + 280 / Math.E), 150, 'dash soft')}${L(r2(40 + 280 / Math.E), 150, r2(40 + 280 / Math.E), 200, 'dash soft')}
  ${T(34, 154, I('H'), '', 'end')}${T(r2(40 + 280 / Math.E), 214, sb(I('n'), '0') + '/e')}${T(320, 214, sb(I('n'), '0'))}`, 'Atmosphère isotherme')],

'mp-statistique-2': ['Système à deux niveaux d’écart ΔE : à basse température, seul le niveau fondamental est peuplé ; à haute température (kBT ≫ ΔE), les deux populations tendent vers 1/2', svg(400, 220, `
  ${axes(40, 190, 340, 0, 170, 0, sb(I('k'), 'B') + I('T') + '/Δ' + I('E'), I('p'))}
  ${courbe(u => 150 / (1 + Math.exp(-60 / Math.max(u, 0.01))), 0, 330, 40, 190, 1, -1, 300, 'b')}${courbe(u => 150 / (1 + Math.exp(60 / Math.max(u, 0.01))), 0, 330, 40, 190, 1, -1, 300, 'r')}
  ${L(40, 115, 380, 115, 'dash soft')}${T(34, 119, '1/2', '', 'end')}${T(34, 44, '1', '', 'end')}
  ${T(110, 52, sb(I('p'), '1') + ' (fondamental)', 'b', 'start')}${T(120, 172, sb(I('p'), '2') + ' (excité)', 'r', 'start')}${T(100, 206, '1')}${L(100, 186, 100, 194)}`, 'Deux niveaux')],
};
