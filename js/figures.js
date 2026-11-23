// Schémas SVG des énoncés de physique-chimie (dessinés à la main, thème clair/sombre via CSS).
// Chaque entrée : id d'exercice -> {svg, legende}

const DEFS = `<defs>
<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1L10,5L0,9z" class="fh"/></marker>
<marker id="ahr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1L10,5L0,9z" class="fh r"/></marker>
<marker id="ahb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1L10,5L0,9z" class="fh b"/></marker>
<pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="7" class="ht"/></pattern>
</defs>`;
const svg = (w, h, body, t) => `<svg viewBox="0 0 ${w} ${h}" role="img" aria-label="${t}" class="fig-svg">${DEFS}${body}</svg>`;
const L = (x1, y1, x2, y2, c = '') => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" class="s ${c}"/>`;
const A = (x1, y1, x2, y2, c = '') => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" class="s ${c}" marker-end="url(#${c.includes('r') && !c.includes('ro') ? 'ahr' : c.includes('b') ? 'ahb' : 'ah'})"/>`;
const D = (x1, y1, x2, y2, t, tx, ty) => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" class="s dim" marker-start="url(#ah)" marker-end="url(#ah)"/>${T(tx ?? (x1 + x2) / 2, ty ?? (y1 + y2) / 2 - 6, t)}`;
const T = (x, y, t, c = '', a = 'middle') => `<text x="${x}" y="${y}" class="lb ${c}" text-anchor="${a}">${t}</text>`;
const I = s => `<tspan class="it">${s}</tspan>`;           // variable en italique
const V = s => `<tspan class="it">${s}</tspan><tspan class="vec" dx="-${s.length * 6.5}" dy="-9">→</tspan><tspan dy="9"> </tspan>`;
const C = (x, y, r, c = '') => `<circle cx="${x}" cy="${y}" r="${r}" class="s ${c}"/>`;
const R = (x, y, w, h, c = '', rx = 0) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx}" class="s ${c}"/>`;
const P = (d, c = '') => `<path d="${d}" class="s ${c}"/>`;
const dot = (x, y, c = '') => `<circle cx="${x}" cy="${y}" r="3.2" class="pt ${c}"/>`;
function spring(x1, y1, x2, y2, n = 9, a = 7) {
  const dx = x2 - x1, dy = y2 - y1, l = Math.hypot(dx, dy), ux = dx / l, uy = dy / l, px = -uy, py = ux;
  const e = Math.min(10, l * .12); let d = `M${x1},${y1} L${x1 + ux * e},${y1 + uy * e}`;
  for (let i = 0; i < n; i++) { const t = e + (l - 2 * e) * (i + .5) / n, s = i % 2 ? -a : a; d += ` L${x1 + ux * t + px * s},${y1 + uy * t + py * s}`; }
  d += ` L${x2 - ux * e},${y2 - uy * e} L${x2},${y2}`;
  return `<path d="${d}" class="s spring"/>`;
}
const ground = (x, y, w, up = false) => `<rect x="${x}" y="${up ? y - 9 : y}" width="${w}" height="9" class="hatch"/>${L(x, y, x + w, y)}`;
const wallV = (x, y, h, left = true) => `<rect x="${left ? x - 9 : x}" y="${y}" width="9" height="${h}" class="hatch"/>${L(x, y, x, y + h)}`;
const lens = (x, y, h, conv = true) => {
  const k = 7, t = y - h / 2, b = y + h / 2;
  return L(x, t, x, b, 'thick') + (conv
    ? P(`M${x - k},${t + k} L${x},${t} L${x + k},${t + k} M${x - k},${b - k} L${x},${b} L${x + k},${b - k}`, 'thick')
    : P(`M${x - k},${t - k} L${x},${t} L${x + k},${t - k} M${x - k},${b + k} L${x},${b} L${x + k},${b + k}`, 'thick'));
};
const axe = (x1, x2, y) => L(x1, y, x2, y, 'axis');
const ox = (x, y) => C(x, y, 6) + C(x, y, 1.6, 'fill');        // vecteur sortant ⊙
const ot = (x, y) => C(x, y, 6) + L(x - 4, y - 4, x + 4, y + 4) + L(x - 4, y + 4, x + 4, y - 4); // entrant ⊗

export const FIG = {
'p-em-1': {legende: 'Cylindre infini chargé en volume (ρ) et en surface (σ)', svg: svg(360, 200, `
  <ellipse cx="90" cy="100" rx="22" ry="62" class="s fillA"/>${R(90, 38, 180, 124, 'fillA')}<ellipse cx="270" cy="100" rx="22" ry="62" class="s fillA"/>
  ${L(90, 38, 270, 38, 'thick r')}${L(90, 162, 270, 162, 'thick r')}
  ${L(40, 100, 330, 100, 'axis')}${T(338, 104, I('z'), '', 'start')}
  ${T(180, 92, 'ρ > 0')}${T(180, 30, 'σ < 0', 'r')}
  ${D(300, 100, 300, 38, I('b'), 312, 72)}${dot(230, 60)}${T(238, 58, I('M'), '', 'start')}${A(230, 100, 230, 64, 'b')}${T(220, 86, I('r'), 'b')}`,
  'Cylindre chargé')},
'p-em-3': {legende: 'Cylindre parcouru par une densité de courant uniforme et contour d’Ampère', svg: svg(360, 210, `
  ${R(150, 20, 60, 170, 'fillA')}${A(180, 175, 180, 40, 'r')}${T(196, 60, V('j'), 'r', 'start')}
  <ellipse cx="180" cy="110" rx="110" ry="26" class="s dash b"/>${A(274, 124, 262, 128, 'b')}${T(296, 112, 'contour', 'b', 'start')}${T(296, 128, 'd’Ampère', 'b', 'start')}
  ${D(150, 198, 210, 198, '2' + I('b'), 180, 194)}${dot(290, 110)}${T(298, 100, I('M'), '', 'start')}${A(290, 110, 290, 80, 'r')}${T(300, 82, V('B'), 'r', 'start')}`,
  'Cylindre parcouru par un courant')},
'p-max-1': {legende: 'Deux cylindres coaxiaux aux potentiels 0 et U (coupe transversale)', svg: svg(320, 220, `
  ${C(160, 110, 92, 'fillA')}${C(160, 110, 40, 'fillB')}${dot(160, 110)}${T(166, 124, I('O'), '', 'start')}
  ${A(160, 110, 189, 82)}${T(190, 98, I('a'), '', 'start')}${A(160, 110, 225, 175)}${T(205, 160, I('b'), '', 'start')}
  ${T(160, 94, I('V') + ' = 0')}${T(250, 200, I('V') + ' = ' + I('U'), 'r', 'start')}${T(252, 70, 'vide', 'soft', 'start')}`,
  'Cylindres coaxiaux')},
'p-max-3': {legende: 'Disque de Corbino : courant radial, champ magnétique axial', svg: svg(340, 240, `
  ${C(160, 110, 95, 'fillA')}${C(160, 110, 35, 'fillW')}
  ${[0, 60, 120, 180, 240, 300].map(a => { const r = Math.PI * a / 180; return A(160 + 42 * Math.cos(r), 110 + 42 * Math.sin(r), 160 + 85 * Math.cos(r), 110 + 85 * Math.sin(r), 'r'); }).join('')}
  ${ox(160, 110)}${T(176, 106, V('B'), 'b', 'start')}${T(118, 74, I('b'), '', 'middle')}${T(258, 46, I('c'), '', 'start')}
  ${T(300, 196, V('j') + ' radial', 'r', 'end')}${T(160, 232, I('U') + ' = ' + I('V') + '(' + I('b') + ') − ' + I('V') + '(' + I('c') + ')')}`,
  'Disque de Corbino')},
'p-ind-2': {legende: 'Tige mobile sur des rails verticaux, retenue par deux ressorts, circuit fermé par R', svg: svg(340, 240, `
  ${ground(60, 22, 220, true)}${L(90, 22, 90, 220, 'thick')}${L(250, 22, 250, 220, 'thick')}
  ${spring(120, 22, 120, 120, 8, 7)}${spring(220, 22, 220, 120, 8, 7)}
  ${R(84, 118, 172, 10, 'fillR', 2)}${T(276, 128, 'tige (' + I('m') + ')', '', 'start')}
  ${R(150, 196, 40, 14, 'fillW')}${L(90, 203, 150, 203)}${L(190, 203, 250, 203)}${T(170, 230, I('R'))}
  ${[[60, 70], [60, 160], [300, 70], [300, 160]].map(([x, y]) => ot(x, y)).join('')}${T(300, 100, V('B'), 'b')}
  ${A(170, 150, 170, 180)}${T(180, 172, V('g'), '', 'start')}${A(40, 200, 40, 160)}${T(30, 156, I('z'))}${T(170, 112, 'largeur ' + I('D'), 'soft')}`,
  'Tige sur rails verticaux')},
'p-ind-3': {legende: 'Bobine plate (N spires, rayon R) au centre d’un solénoïde (10N spires, rayon 2R)', svg: svg(360, 190, `
  ${Array.from({length: 13}, (_, i) => `<ellipse cx="${60 + i * 20}" cy="95" rx="8" ry="58" class="s ${i % 2 ? '' : 'soft'}"/>`).join('')}
  ${L(60, 37, 300, 37)}${L(60, 153, 300, 153)}<ellipse cx="180" cy="95" rx="5" ry="29" class="s thick r"/>
  ${L(20, 95, 345, 95, 'axis')}${D(60, 172, 300, 172, I('D'), 180, 168)}${D(320, 37, 320, 95, '2' + I('R'), 334, 70)}
  ${T(196, 74, I('R'), 'r', 'start')}${T(180, 20, 'solénoïde, 10' + I('N') + ' spires')}`,
  'Solénoïde et spire plate')},
'p-ondes-1': {legende: 'Modèle de la tige : masselottes reliées par des ressorts', svg: svg(360, 140, `
  ${axe(10, 350, 100)}${T(352, 104, I('x'), '', 'start')}
  ${[50, 130, 210, 290].map((x, i) => R(x - 12, 52, 24, 24, i === 2 ? 'fillR' : 'fillA', 3)).join('')}
  ${[[62, 118], [142, 198], [222, 278]].map(([a, b]) => spring(a, 64, b, 64, 7, 6)).join('')}
  ${T(130, 44, I('x') + ' − ' + I('dx'))}${T(210, 44, I('x'))}${T(290, 44, I('x') + ' + ' + I('dx'))}
  ${A(210, 92, 236, 92, 'r')}${T(226, 118, I('u') + '(' + I('x') + ',' + I('t') + ')', 'r')}${T(170, 16, 'raideur ' + I('k') + ' = ' + I('ES') + '/' + I('dx') + ' — masse ' + I('μS dx'), 'soft')}`,
  'Chaîne masses-ressorts')},
'p-ondes-2': {legende: 'Câble tendu soutenu par des suspensions caténaires (force de rappel −α dx z)', svg: svg(360, 170, `
  ${L(10, 20, 350, 20, 'thick')}${[50, 110, 170, 230, 290].map(x => spring(x, 20, x, 82 + 14 * Math.sin(x / 40), 5, 5)).join('')}
  ${P('M10,90 C60,70 110,110 170,92 S290,74 350,94', 'thick r')}${axe(10, 350, 130)}${T(352, 134, I('x'), '', 'start')}
  ${A(330, 150, 330, 100)}${T(338, 110, I('z'), '', 'start')}${A(20, 90, 2, 90)}${A(340, 94, 358, 94)}${T(36, 108, I('T') + '<tspan baseline-shift="sub" font-size="10">E</tspan>', '', 'start')}`,
  'Caténaire')},
'p-meca-1': {legende: 'Sismographe : boîtier lié au sol, ressort et amortisseur', svg: svg(300, 250, `
  ${R(70, 20, 160, 190, 'fillW', 4)}${ground(30, 210, 240)}
  ${spring(150, 20, 150, 110, 8, 9)}${R(125, 110, 50, 34, 'fillR', 4)}${T(150, 132, I('m'))}
  ${L(150, 144, 150, 165)}${R(138, 165, 24, 30, '')}${L(142, 180, 158, 180, 'thick')}${L(150, 180, 150, 210)}${T(176, 186, 'λ', '', 'start')}
  ${T(178, 66, I('k') + ', ' + I('ℓ') + '<tspan baseline-shift="sub" font-size="10">0</tspan>', '', 'start')}
  ${A(255, 160, 255, 70)}${T(262, 76, I('z'), '', 'start')}${dot(255, 127)}${T(262, 131, I('O'), '', 'start')}
  ${A(40, 120, 40, 80, 'b')}${A(40, 120, 40, 160, 'b')}${T(30, 76, I('H') + ' cos ' + I('ωt'), 'b', 'start')}`,
  'Sismographe')},
'p-meca-2': {legende: 'Pendule simple accroché au plafond d’un train d’accélération A', svg: svg(320, 210, `
  ${R(20, 20, 280, 160, 'fillW', 6)}${ground(30, 30, 260, true)}${C(80, 196, 12)}${C(240, 196, 12)}
  ${dot(160, 30)}${T(168, 46, I('O'), '', 'start')}${L(160, 30, 112, 126, 'thick')}${C(112, 126, 11, 'fillR')}${T(96, 152, I('M'))}
  ${L(160, 30, 160, 140, 'axis')}<path d="M160,80 A50,50 0 0 1 138,74" class="s r"/>${T(140, 98, 'θ', 'r')}
  ${A(250, 110, 300, 110, 'r')}${T(276, 100, V('A'), 'r')}${A(112, 126, 112, 166)}${T(120, 166, V('g'), '', 'start')}${T(140, 70, I('L'), '', 'end')}`,
  'Pendule dans un train')},
'p-meca-4': {legende: 'Repère local à la latitude λ : x vers l’est, y vers le nord, z vertical', svg: svg(340, 240, `
  ${C(130, 130, 90, 'fillA')}${L(130, 22, 130, 238, 'axis')}${A(130, 40, 130, 18, 'b')}${T(140, 22, V('Ω'), 'b', 'start')}
  <ellipse cx="130" cy="130" rx="90" ry="18" class="s soft dash"/>${L(130, 130, 207, 84, 'dash')}
  <path d="M175,130 A45,45 0 0 0 169,107" class="s r"/>${T(182, 122, 'λ', 'r', 'start')}
  ${dot(207, 84)}${A(207, 84, 250, 58)}${T(256, 56, I('z'), '', 'start')}${A(207, 84, 181, 42)}${T(186, 38, I('y') + ' (nord)', '', 'start')}${A(207, 84, 240, 110)}${T(246, 120, I('x') + ' (est)', '', 'start')}
  ${T(130, 232, 'axe des pôles', 'soft')}`,
  'Latitude et repère local')},
'p-meca-5': {legende: 'Pendule de Foucault : fil de longueur L accroché en S, petites oscillations', svg: svg(320, 230, `
  ${ground(110, 22, 100, true)}${dot(160, 22)}${T(170, 34, I('S'), '', 'start')}${L(160, 22, 196, 170, 'thick')}${C(196, 170, 11, 'fillR')}${T(210, 156, I('M'), '', 'start')}
  ${L(160, 22, 160, 200, 'axis')}${T(150, 110, I('L'), '', 'end')}${dot(160, 200)}${T(150, 214, I('O'), '', 'end')}
  <ellipse cx="160" cy="200" rx="110" ry="16" class="s soft dash"/>${A(160, 200, 270, 200)}${T(276, 204, I('x') + ' est', '', 'start')}${A(160, 200, 216, 184)}${T(222, 182, I('y') + ' nord', '', 'start')}${A(40, 190, 40, 150)}${T(48, 154, I('z'), '', 'start')}`,
  'Pendule de Foucault')},
'p-meca-6': {legende: 'Particule chargée entrant dans un champ magnétique uniforme sortant du plan', svg: svg(340, 210, `
  ${R(120, 15, 205, 180, 'fillA', 4)}${Array.from({length: 12}, (_, i) => ox(145 + (i % 4) * 50, 45 + Math.floor(i / 4) * 60)).join('')}
  ${T(310, 32, V('B'), 'b', 'end')}${dot(120, 135, 'r')}${A(40, 135, 116, 135, 'r')}${T(60, 126, V('v') + '<tspan baseline-shift="sub" font-size="10">0</tspan>', 'r')}
  ${P('M120,135 C170,135 196,108 196,72 C196,44 176,32 160,36 C146,40 140,58 152,70 C160,78 172,72 170,62', 'r dash')}
  ${A(20, 190, 60, 190)}${T(64, 194, I('x'), '', 'start')}${A(20, 190, 20, 150)}${T(14, 146, I('y'), '', 'end')}`,
  'Chambre à bulles')},
'p-meca-7': {legende: 'Cube posé sur un chariot relié à un ressort, sans frottement sur la table', svg: svg(340, 170, `
  ${ground(20, 140, 310)}${wallV(30, 40, 100)}${spring(30, 100, 110, 100, 9, 8)}${R(110, 80, 150, 46, 'fillW', 4)}${C(135, 132, 8)}${C(235, 132, 8)}
  ${R(165, 50, 34, 30, 'fillR', 3)}${T(182, 70, I('m'))}${T(185, 108, I('M'))}${T(70, 84, I('k'))}${T(182, 40, 'μ', 'r')}${A(270, 60, 320, 60)}${T(326, 64, I('x'), '', 'start')}`,
  'Rodéo horizontal')},
'p-meca-8': {legende: 'Tonneau posé sur le plateau d’un camion qui accélère', svg: svg(340, 200, `
  ${R(30, 110, 260, 22, 'fillW', 3)}${R(250, 70, 70, 62, 'fillW', 6)}${C(80, 150, 16)}${C(280, 150, 16)}${ground(10, 166, 320)}
  ${C(130, 82, 28, 'fillR')}${C(130, 82, 3, 'fill')}${T(130, 46, 'tonneau')}${T(166, 86, I('b'), '', 'start')}${L(130, 82, 158, 82, 'dash')}
  ${A(260, 40, 320, 40, 'r')}${T(290, 30, V('a') + ' = ' + I('A') + ' ' + V('u') + '<tspan baseline-shift="sub" font-size="10">x</tspan>', 'r')}${D(30, 100, 250, 100, I('d'), 190, 96)}`,
  'Tonneau sur un camion')},
'p-meca-9': {legende: 'Machine de Timochenko : plaque posée sur deux cylindres tournant en sens opposés', svg: svg(340, 190, `
  ${R(60, 70, 220, 14, 'fillR', 2)}${dot(170, 77)}${T(170, 62, I('G'))}${C(100, 112, 26, 'fillA')}${C(240, 112, 26, 'fillA')}
  <path d="M84,96 A22,22 0 0 1 116,96" class="s b" marker-end="url(#ahb)"/><path d="M256,96 A22,22 0 0 0 224,96" class="s b" marker-end="url(#ahb)"/>
  ${T(100, 160, I('ω'), 'b')}${T(240, 160, I('ω'), 'b')}${dot(100, 86)}${dot(240, 86)}${T(92, 64, I('I') + '<tspan baseline-shift="sub" font-size="10">1</tspan>')}${T(248, 64, I('I') + '<tspan baseline-shift="sub" font-size="10">2</tspan>')}
  ${D(100, 178, 240, 178, I('D'), 170, 174)}${A(170, 40, 210, 40)}${T(216, 44, I('x'), '', 'start')}`,
  'Machine de Timochenko')},
'p-meca-10': {legende: 'Solide de longueur 10R glissant sur une suite de rouleaux identiques', svg: svg(360, 150, `
  ${Array.from({length: 7}, (_, i) => C(40 + i * 46, 100, 22, 'fillA') + dot(40 + i * 46, 100)).join('')}
  ${R(70, 56, 190, 22, 'fillR', 2)}${T(165, 72, I('M') + ' = 5' + I('m'))}${A(270, 50, 320, 50, 'r')}${T(296, 40, V('V') + '<tspan baseline-shift="sub" font-size="10">n</tspan>', 'r')}
  ${D(70, 40, 260, 40, '10' + I('R'), 165, 36)}${T(40, 140, I('R') + ', ' + I('m'))}`,
  'Tapis à rouleaux')},
'p-meca-ccs3': {legende: 'Tunnel rectiligne AB à travers une Terre homogène', svg: svg(300, 240, `
  ${C(150, 120, 100, 'fillA')}${dot(150, 120)}${T(158, 134, I('O'), '', 'start')}${L(62, 72, 238, 72, 'thick r')}${dot(62, 72)}${dot(238, 72)}
  ${T(52, 66, I('A'), '', 'end')}${T(248, 66, I('B'), '', 'start')}${dot(190, 72, 'r')}${T(194, 64, I('M'), 'r', 'start')}${L(150, 120, 190, 72, 'dash')}${T(160, 92, I('r'), '', 'end')}
  ${L(150, 120, 150, 72, 'dash')}${A(150, 120, 245, 145)}${T(206, 150, I('R') + '<tspan baseline-shift="sub" font-size="10">T</tspan>')}`,
  'Tunnel à travers la Terre')},
'p-meca-ccs1': {legende: 'Soleil et Jupiter en rotation uniforme autour de leur centre de masse G', svg: svg(360, 160, `
  ${C(90, 80, 34, 'fillY')}${T(90, 136, 'Soleil')}${C(300, 80, 14, 'fillR')}${T(300, 120, 'Jupiter')}${L(90, 80, 300, 80, 'dash')}
  ${dot(112, 80, 'r')}${T(112, 62, I('G'), 'r')}<path d="M210,40 A100,100 0 0 1 240,62" class="s b" marker-end="url(#ahb)"/>${T(232, 40, I('ω'), 'b', 'start')}`,
  'Système Soleil-Jupiter')},
'p-meca-ccmp2': {legende: 'Parallélépipède de bois flottant, d’épaisseur e', svg: svg(320, 170, `
  ${R(10, 80, 300, 80, 'fillB')}${L(10, 80, 310, 80, 'b')}${R(110, 50, 100, 60, 'fillW', 2)}${D(230, 50, 230, 110, I('e'), 244, 84)}
  ${A(160, 30, 160, 10)}${A(160, 30, 160, 48)}${T(170, 26, 'oscillations', '', 'start')}${T(30, 100, 'eau de mer', 'b', 'start')}`,
  'Bouchon flottant')},
'p-opt-2': {legende: 'Objectif L formant l’image de AB sur la plaque, à la distance D de l’objet', svg: svg(360, 170, `
  ${axe(10, 350, 100)}${A(40, 100, 40, 62, 'r')}${T(40, 116, I('A'))}${T(30, 60, I('B'), '', 'end')}${lens(180, 100, 110)}${T(180, 34, I('L') + ' (' + I('f') + "′)")}
  ${L(320, 40, 320, 150, 'thick b')}${T(330, 46, 'plaque', 'b', 'start')}${D(40, 160, 320, 160, I('D'), 180, 156)}${D(180, 136, 320, 136, I('d'), 250, 132)}
  ${L(40, 62, 180, 62, 'ray')}${L(180, 62, 320, 132, 'ray')}${L(40, 62, 320, 132, 'ray')}`,
  'Objectif photographique')},
'p-opt-3': {legende: 'Microscope : objectif L₁ (f′₁ = 0,5 cm) et oculaire L₂ (f′₂ = 2 cm)', svg: svg(360, 170, `
  ${axe(10, 350, 96)}${A(60, 96, 60, 74, 'r')}${T(60, 112, I('A'))}${T(52, 72, I('B'), '', 'end')}${lens(90, 96, 80)}${T(90, 44, I('L') + '<tspan baseline-shift="sub" font-size="10">1</tspan>')}
  ${lens(280, 96, 100)}${T(280, 34, I('L') + '<tspan baseline-shift="sub" font-size="10">2</tspan>')}${dot(90, 96)}${dot(280, 96)}${T(96, 112, I('O') + '<tspan baseline-shift="sub" font-size="10">1</tspan>', '', 'start')}${T(286, 112, I('O') + '<tspan baseline-shift="sub" font-size="10">2</tspan>', '', 'start')}
  <path d="M330,80 q14,16 0,32" class="s"/>${T(344, 100, 'œil', '', 'start')}${A(230, 96, 230, 150, 'b')}${T(236, 150, I('A') + '<tspan baseline-shift="sub" font-size="10">1</tspan>' + I('B') + '<tspan baseline-shift="sub" font-size="10">1</tspan>', 'b', 'start')}`,
  'Microscope')},
'p-opt-4': {legende: 'Lentille plan-convexe (rayon R) posée sur un miroir plan : lame d’air d’épaisseur ε(x)', svg: svg(360, 200, `
  ${R(30, 160, 300, 12, 'fillB')}${T(40, 192, 'miroir plan', 'b', 'start')}${P('M40,60 L320,60 L320,110 Q180,190 40,110 Z', 'fillA')}${dot(180, 150)}${T(180, 186, I('O'))}
  ${L(180, 20, 180, 160, 'axis')}${D(250, 136, 250, 160, 'ε', 264, 152)}${L(250, 60, 250, 136, 'dash')}${D(180, 46, 250, 46, I('x'), 215, 42)}
  ${A(110, 10, 110, 58, 'r')}${A(140, 10, 140, 58, 'r')}${T(100, 20, 'λ<tspan baseline-shift="sub" font-size="10">0</tspan>', 'r', 'end')}`,
  'Anneaux de Newton')},
'p-opt-5': {legende: 'Réseau de pas a éclairé sous l’incidence i, observé dans la direction α', svg: svg(340, 210, `
  ${L(170, 20, 170, 190, 'thick')}${Array.from({length: 9}, (_, i) => L(164, 30 + i * 19, 176, 30 + i * 19)).join('')}${D(190, 68, 190, 87, I('a'), 202, 82)}
  ${A(40, 50, 166, 100, 'r')}${A(40, 70, 166, 120, 'r')}${L(20, 105, 320, 105, 'axis')}<path d="M110,105 A60,60 0 0 1 115,82" class="s r"/>${T(100, 96, I('i'), 'r', 'end')}
  ${A(174, 105, 300, 160, 'b')}${A(174, 125, 300, 180, 'b')}<path d="M230,105 A56,56 0 0 1 225,129" class="s b"/>${T(240, 124, 'α', 'b', 'start')}`,
  'Réseau plan')},
'p-opt-6': {legende: 'Interféromètre de Michelson réglé en lame d’air', svg: svg(340, 240, `
  ${L(120, 70, 200, 150, 'thick b')}${T(212, 152, 'séparatrice', 'b', 'start')}${R(250, 100, 8, 40, 'fillB')}${T(270, 124, I('M') + '<tspan baseline-shift="sub" font-size="10">2</tspan>', '', 'start')}
  ${R(140, 18, 40, 8, 'fillB')}${T(194, 24, I('M') + '<tspan baseline-shift="sub" font-size="10">1</tspan>', '', 'start')}${C(30, 110, 9, 'fillY')}${T(30, 140, 'source')}
  ${A(42, 110, 156, 110, 'r')}${L(160, 110, 248, 110, 'r')}${L(160, 110, 160, 28, 'r')}${A(160, 110, 160, 200, 'r')}${lens(160, 200, 40)}${dot(160, 226)}${T(172, 230, 'capteur', '', 'start')}
  ${L(250, 100, 250, 140, 'dash')}${D(254, 84, 264, 84, I('e'), 266, 78)}`,
  'Michelson')},
'p-opt-7': {legende: 'Michelson en coin d’air (angle α) : franges d’égale épaisseur projetées sur un écran', svg: svg(340, 200, `
  ${L(60, 150, 260, 150, 'thick b')}${L(60, 150, 260, 120, 'thick r')}<path d="M120,150 A60,60 0 0 0 119,141" class="s"/>${T(132, 144, 'α', '', 'start')}
  ${T(270, 154, I('M') + '<tspan baseline-shift="sub" font-size="10">1</tspan>′', 'b', 'start')}${T(270, 120, I('M') + '<tspan baseline-shift="sub" font-size="10">2</tspan>', 'r', 'start')}
  ${dot(200, 150)}${T(200, 168, I('P'))}${D(200, 150, 200, 129, 'ε', 214, 142)}${dot(60, 150)}${T(56, 168, I('A'))}${lens(160, 70, 50)}${T(176, 60, I('f') + '′', '', 'start')}`,
  'Coin d’air')},
'p-opt-ccmp1': {legende: 'Trous d’Young : source S, trous S₁ et S₂ distants de a, écran à la distance D', svg: svg(360, 190, `
  ${dot(30, 95, 'r')}${T(30, 116, I('S'))}${L(120, 20, 120, 170, 'thick')}${dot(120, 75)}${dot(120, 115)}${T(110, 70, I('S') + '<tspan baseline-shift="sub" font-size="10">1</tspan>', '', 'end')}${T(110, 130, I('S') + '<tspan baseline-shift="sub" font-size="10">2</tspan>', '', 'end')}
  ${L(30, 95, 120, 75, 'ray')}${L(30, 95, 120, 115, 'ray')}${L(320, 20, 320, 170, 'thick b')}${dot(320, 60)}${T(330, 64, I('M'), '', 'start')}${L(120, 75, 320, 60, 'ray')}${L(120, 115, 320, 60, 'ray')}
  ${D(140, 75, 140, 115, I('a'), 152, 100)}${D(120, 182, 320, 182, I('D'), 220, 178)}${A(330, 95, 330, 40)}${T(340, 44, I('x'), '', 'start')}`,
  'Trous d’Young')},
'p-th-1': {legende: 'Gaz parfait dans un cylindre calorifugé fermé par un piston bloqué ; atmosphère à P₀/2', svg: svg(340, 170, `
  ${P('M30,40 L230,40 M30,130 L230,130 M30,40 L30,130', 'thick')}${R(30, 40, 150, 90, 'fillA')}${R(180, 40, 16, 90, 'fillW', 2)}
  ${T(105, 82, I('n') + ' mol')}${T(105, 102, I('T') + '<tspan baseline-shift="sub" font-size="10">0</tspan>, ' + I('P') + '<tspan baseline-shift="sub" font-size="10">0</tspan>')}
  ${T(280, 90, I('P') + '<tspan baseline-shift="sub" font-size="10">1</tspan> = ' + I('P') + '<tspan baseline-shift="sub" font-size="10">0</tspan>/2', 'b')}${L(188, 30, 188, 140, 'r')}${T(188, 156, 'cale', 'r')}`,
  'Détente sous piston')},
'p-th-spe6': {legende: 'Mur cylindrique de rayons a₁ et a₂ (coupe), parois à T₁ et T₂', svg: svg(300, 220, `
  ${C(150, 110, 95, 'fillA')}${C(150, 110, 60, 'fillW')}${dot(150, 110)}${A(150, 110, 192, 68)}${T(176, 100, I('a') + '<tspan baseline-shift="sub" font-size="10">1</tspan>', '', 'start')}
  ${A(150, 110, 82, 178)}${T(102, 150, I('a') + '<tspan baseline-shift="sub" font-size="10">2</tspan>', '', 'end')}${T(150, 128, I('T') + '<tspan baseline-shift="sub" font-size="10">1</tspan>')}${T(268, 30, I('T') + '<tspan baseline-shift="sub" font-size="10">2</tspan>', 'b')}
  ${A(225, 110, 255, 110, 'r')}${T(258, 100, V('j') + '<tspan baseline-shift="sub" font-size="10">th</tspan>', 'r', 'start')}`,
  'Mur cylindrique')},
'p-th-ccs4': {legende: 'Paroi d’épaisseur 2L produisant une puissance volumique q, faces à T₀', svg: svg(320, 170, `
  ${R(110, 20, 100, 130, 'fillR')}${T(160, 88, I('q'))}${L(20, 150, 300, 150, 'axis')}${T(304, 154, I('x'), '', 'start')}
  ${T(110, 166, '−' + I('L'))}${T(210, 166, '+' + I('L'))}${T(160, 166, '0')}${T(80, 40, I('T') + '<tspan baseline-shift="sub" font-size="10">0</tspan>', 'b')}${T(240, 40, I('T') + '<tspan baseline-shift="sub" font-size="10">0</tspan>', 'b')}
  ${A(210, 70, 260, 70, 'r')}${A(110, 70, 60, 70, 'r')}`,
  'Paroi avec production de chaleur')},
'p-th-ccmp4': {legende: 'Couche de glace d’épaisseur e(t) entre l’air à T_c et l’eau à T_fus', svg: svg(320, 180, `
  ${R(10, 20, 300, 50, 'fillW')}${T(30, 50, 'air, ' + I('T') + '<tspan baseline-shift="sub" font-size="10">c</tspan>', '', 'start')}${R(10, 70, 300, 40, 'fillI')}${T(30, 96, 'glace', 'b', 'start')}
  ${R(10, 110, 300, 60, 'fillB')}${T(30, 146, 'eau liquide, ' + I('T') + '<tspan baseline-shift="sub" font-size="10">fus</tspan>', 'b', 'start')}${D(260, 70, 260, 110, I('e') + '(' + I('t') + ')', 286, 94)}${A(200, 104, 200, 124, 'r')}`,
  'Croissance de la glace')},
'p-q-4': {legende: 'Puits de potentiel semi-infini : V = +∞ pour x < 0, 0 sur [0, a], V₀ au-delà', svg: svg(340, 190, `
  ${A(40, 160, 330, 160)}${T(334, 164, I('x'), '', 'start')}${A(60, 175, 60, 14)}${T(66, 18, I('V'), '', 'start')}
  ${P('M60,20 L60,160 L170,160 L170,70 L320,70', 'thick r')}${R(40, 20, 20, 140, 'hatch')}${T(60, 176, '0')}${T(170, 176, I('a'))}${T(176, 64, I('V') + '<tspan baseline-shift="sub" font-size="10">0</tspan>', 'r', 'start')}
  ${L(60, 110, 320, 110, 'dash b')}${T(326, 114, I('E'), 'b', 'start')}`,
  'Puits semi-infini')},
'p-ccs-plan': {legende: 'Couche infinie chargée uniformément, d’épaisseur a', svg: svg(320, 170, `
  ${R(20, 60, 280, 50, 'fillA')}${T(160, 90, 'ρ')}${A(160, 160, 160, 14)}${T(168, 18, I('z'), '', 'start')}${L(20, 85, 300, 85, 'axis')}
  ${T(310, 64, I('a') + '/2', '', 'end')}${T(310, 120, '−' + I('a') + '/2', '', 'end')}${dot(160, 72, 'r')}${T(150, 72, I('q'), 'r', 'end')}`,
  'Plan épais chargé')},
'p-ccs-bulle': {legende: 'Bulle de CO₂ remontant dans le champagne', svg: svg(220, 220, `
  ${P('M60,20 L60,200 Q60,210 70,210 L150,210 Q160,210 160,200 L160,20', 'thick')}${R(62, 40, 96, 168, 'fillY')}
  ${C(110, 150, 6, 'fillW')}${C(104, 110, 8, 'fillW')}${C(114, 66, 10, 'fillW')}${A(130, 150, 130, 110, 'r')}${T(136, 130, V('v'), 'r', 'start')}${T(110, 196, 'ρ<tspan baseline-shift="sub" font-size="10">c</tspan>, η')}`,
  'Bulle de champagne')},
'p-th-4': {legende: 'Turboréacteur : compresseur, chambre de combustion, turbine, tuyère', svg: svg(360, 140, `
  ${[['A', 20], ['B', 100], ['C', 180], ['D', 260], ['E', 330]].map(([n, x]) => dot(x, 70) + T(x, 100, I(n))).join('')}
  ${R(34, 50, 52, 40, 'fillA', 6)}${T(60, 40, 'compr.')}${R(114, 50, 52, 40, 'fillR', 6)}${T(140, 40, 'combustion', 'r')}${R(194, 50, 52, 40, 'fillA', 6)}${T(220, 40, 'turbine')}
  ${P('M274,52 L318,62 L318,78 L274,88 Z', 'fillW')}${T(296, 40, 'tuyère')}${A(20, 70, 32, 70)}${A(320, 70, 350, 70, 'r')}${T(340, 120, I('V') + '<tspan baseline-shift="sub" font-size="10">E</tspan>', 'r')}
  ${P('M220,92 Q140,130 60,92', 'dash b')}${T(140, 128, 'travail transmis', 'b')}`,
  'Turboréacteur')},
'c-cristallo-2': {legende: 'Maille cubique à faces centrées : sites octaédriques (O) et tétraédriques (T)', svg: svg(260, 230, `
  ${R(50, 70, 130, 130)}${P('M50,70 L100,30 L230,30 L180,70 M230,30 L230,160 L180,200', '')}${P('M50,200 L100,160 L230,160 M100,30 L100,160', 'dash soft')}
  ${[[50, 70], [180, 70], [50, 200], [180, 200], [100, 30], [230, 30], [230, 160], [100, 160], [115, 135], [140, 50], [205, 115], [75, 115], [165, 95], [155, 180]].map(([x, y]) => C(x, y, 7, 'fillA')).join('')}
  ${C(140, 115, 6, 'fillR')}${T(150, 112, 'O', 'r', 'start')}${C(82, 92, 4, 'fillY')}${T(76, 90, 'T', '', 'end')}`,
  'Maille CFC')},
};
export const hasFig = id => !!FIG[id];
