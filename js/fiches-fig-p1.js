// Schémas des fiches de cours — Physique MPSI, partie 1 : Signaux.
// Dessinés avec figkit (thème clair/sombre par CSS). Clé : <fiche>-<n>.
import { svg, L, A, D, T, I, V, C, R, P, dot, spring, ground, wallV, lens, sb } from './figkit.js';
import { axes, courbe, res, cond, bobine, gene, inter, fil, noeud, ten, cour, tir, flt } from './fiches-kit.js';

const f2 = n => +n.toFixed(2);

export const FIGS = {

// ---------------- Oscillateur harmonique
'p1-oscillateur-1': ['Oscillateur masse-ressort horizontal : x est l’écart à la position d’équilibre', svg(380, 190, `
  ${wallV(40, 40, 90)}${ground(40, 130, 300)}
  ${spring(40, 95, 190, 95, 11, 9)}${R(190, 70, 60, 60, 'fillA')}${T(220, 106, I('m'))}${T(115, 72, I('k'))}
  ${L(190, 145, 190, 175, 'dash soft')}${L(160, 145, 160, 175, 'dash soft')}${T(160, 188, I('O'), 'nt')}
  ${A(160, 160, 190, 160, 'b')}${T(176, 154, I('x'), 'b')}
  ${A(250, 162, 340, 162)}${T(350, 166, I('x'), '', 'start')}${A(250, 100, 300, 100, 'r')}${T(306, 104, V('F'), 'r', 'start')}${T(340, 40, I('F') + ' = −' + I('k') + I('x'), 'r', 'end')}`, 'Masse-ressort')],

'p1-oscillateur-2': ['Élongation x(t) = Xm cos(ω₀t + φ) : amplitude, période, phase à l’origine', svg(400, 210, (() => {
  const X0 = 50, Y0 = 105, sx = 320 / (2.4 * 2 * Math.PI), Am = 60, ph = -Math.PI / 3;
  const c = courbe(t => Am * Math.cos(t + ph), 0, 2.4 * 2 * Math.PI, X0, Y0, sx, 1, 300);
  const tmax1 = -ph, tmax2 = tmax1 + 2 * Math.PI;
  return `${axes(X0, Y0, 330, 10, 80, 80, I('t'), I('x'))}${c}
  ${L(X0, Y0 - Am, X0 + 320, Y0 - Am, 'dash soft')}${T(X0 - 6, Y0 - Am + 4, sb(I('X'), 'm'), '', 'end')}
  ${L(X0, Y0 + Am, X0 + 320, Y0 + Am, 'dash soft')}${T(X0 - 6, Y0 + Am + 4, '−' + sb(I('X'), 'm'), '', 'end')}
  ${D(X0 + tmax1 * sx, Y0 - Am - 14, X0 + tmax2 * sx, Y0 - Am - 14, I('T') + ' = 2π/' + sb('ω', '0'))}
  ${dot(X0, Y0 - Am * Math.cos(ph))}${T(X0 - 8, Y0 - Am * Math.cos(ph) + 4, I('x') + '(0)', '', 'end')}`;
})(), 'Graphe x(t)')],

'p1-oscillateur-3': ['Portrait de phase : une ellipse parcourue dans le sens horaire', svg(360, 220, `
  ${axes(180, 110, 150, 150, 95, 95, I('x'), 'ẋ')}
  <ellipse cx="180" cy="110" rx="110" ry="70" class="s b"/>
  ${A(240, 52, 252, 56, 'b')}${A(130, 170, 118, 166, 'b')}
  ${T(296, 126, sb(I('X'), 'm'), '', 'start')}${T(186, 34, sb('ω', '0') + sb(I('X'), 'm'), '', 'start')}
  `, 'Portrait de phase')],

// ---------------- Propagation
'p1-propagation-1': ['Onde progressive : le profil se translate de cΔt pendant Δt', svg(400, 190, (() => {
  const g = x => 55 * Math.exp(-((x - 0) ** 2) / 900);
  const X0 = 40, Y0 = 140;
  return `${axes(X0, Y0, 340, 20, 110, 0, I('x'), I('s'))}
  ${courbe(x => g(x - 110), 0, 340, X0, Y0, 1, -1, 200)}${courbe(x => g(x - 230), 0, 340, X0, Y0, 1, -1, 200, 'b')}
  ${T(150, 70, I('t'))}${T(270, 70, I('t') + ' + Δ' + I('t'), 'b')}
  ${D(150, 165, 270, 165, I('c') + 'Δ' + I('t'), 210, 182)}${A(300, 110, 360, 110, 'r')}${T(366, 114, V('c'), 'r', 'start')}`;
})(), 'Onde progressive')],

'p1-propagation-2': ['Double périodicité : période spatiale λ et période temporelle T, liées par λ = cT', svg(440, 190, (() => {
  const s = (ox, lab, per, labp) => `${axes(ox, 95, 170, 10, 60, 60, lab, I('s'))}${courbe(u => 40 * Math.sin(2 * Math.PI * u / per), 0, 165, ox, 95, 1, -1, 160)}
    ${D(ox + per / 4, 40, ox + per / 4 + per, 40, labp)}`;
  return `${s(30, I('x'), 70, 'λ')}${T(110, 180, 'à ' + I('t') + ' fixé', 'nt')}${s(250, I('t'), 70, I('T'))}${T(330, 180, 'à ' + I('x') + ' fixé', 'nt')}`;
})(), 'Double périodicité')],

// ---------------- Superposition
'p1-superposition-1': ['Deux sources synchrones : en M, la différence de marche δ = d₂ − d₁ fixe le type d’interférence', svg(400, 240, (() => {
  let arcs = '';
  for (let k = 1; k <= 6; k++) arcs += `<circle cx="70" cy="80" r="${k * 28}" class="s soft"/><circle cx="70" cy="140" r="${k * 28}" class="s soft dash"/>`;
  return `<clipPath id="cl1"><rect x="40" y="5" width="300" height="190"/></clipPath><g clip-path="url(#cl1)">${arcs}</g>
  ${dot(70, 80)}${dot(70, 140)}${T(56, 84, sb(I('S'), '1'), '', 'end')}${T(56, 144, sb(I('S'), '2'), '', 'end')}
  ${L(70, 80, 320, 110, 'b')}${L(70, 140, 320, 110, 'r')}${dot(320, 110)}${T(330, 114, I('M'), '', 'start')}
  ${T(200, 86, sb(I('d'), '1'), 'b')}${T(200, 140, sb(I('d'), '2'), 'r')}
  ${T(200, 214, 'δ = ' + I('p') + 'λ : amplitude maximale', 'nt')}${T(200, 232, 'δ = (' + I('p') + ' + ½)λ : amplitude minimale', 'nt')}${T(330, 30, 'crêtes de ' + sb(I('S'), '1'), 'nt', 'end')}`;
})(), 'Interférences')],

'p1-superposition-2': ['Modes propres d’une corde fixée à ses deux extrémités : L = nλₙ/2', svg(380, 240, (() => {
  let s = '';
  [1, 2, 3].forEach((n, k) => {
    const y = 45 + k * 72, Lx = 280, X0 = 60;
    s += `${wallV(X0, y - 22, 44)}${wallV(X0 + Lx, y - 22, 44, false)}${T(30, y + 5, I('n') + ' = ' + n, '', 'middle')}`;
    s += courbe(x => 20 * Math.sin(n * Math.PI * x / Lx), 0, Lx, X0, y, 1, -1, 120, 'b');
    s += courbe(x => -20 * Math.sin(n * Math.PI * x / Lx), 0, Lx, X0, y, 1, -1, 120, 'b dash');
    for (let j = 0; j <= n; j++) s += dot(X0 + j * Lx / n, y, 'r');
    if (n === 3) { s += T(X0 + Lx / 3, y + 30, 'nœud', 'nt'); s += A(X0 + Lx / 3, y + 19, X0 + Lx / 3, y + 6, 'soft'); s += T(X0 + Lx / 6 + 36, y - 22, 'ventre', 'nt', 'start'); }
  });
  return s;
})(), 'Ondes stationnaires')],

'p1-superposition-3': ['Battements : somme de deux sinusoïdes de fréquences voisines, enveloppe de période 1/|f₁ − f₂|', svg(400, 200, (() => {
  const X0 = 40, Y0 = 100, w1 = 2 * Math.PI * 22, w2 = 2 * Math.PI * 20, sx = 330;
  const s = t => 30 * (Math.cos(w1 * t) + Math.cos(w2 * t));
  const env = t => 60 * Math.abs(Math.cos((w1 - w2) * t / 2));
  return `${axes(X0, Y0, 340, 10, 80, 80, I('t'), I('s'))}${courbe(u => s(u / sx), 0, sx, X0, Y0, 1, -1, 900)}
  ${courbe(u => env(u / sx), 0, sx, X0, Y0, 1, -1, 200, 'b dash')}${courbe(u => -env(u / sx), 0, sx, X0, Y0, 1, -1, 200, 'b dash')}
  ${D(X0 + sx * 0.25, 185, X0 + sx * 0.75, 185, sb(I('T'), 'b') + ' = 1/|' + sb(I('f'), '1') + ' − ' + sb(I('f'), '2') + '|', X0 + sx * 0.5, 180)}`;
})(), 'Battements')],

// ---------------- Onde lumineuse
'p1-onde-lumineuse-1': ['Spectre électromagnétique (échelle logarithmique) : le visible n’occupe que 400 à 800 nm', svg(420, 200, (() => {
  const X = l => 20 + (Math.log10(l) + 12) * 380 / 13;          // λ de 1 pm à 10 m
  const zones = [['γ', 1e-12, 1e-11], ['X', 1e-11, 1e-8], ['UV', 1e-8, 4e-7], ['IR', 8e-7, 1e-3], ['micro-ondes', 1e-3, 1], ['radio', 1, 10]];
  let s = R(20, 40, 380, 30);
  zones.forEach(([t, a, b]) => { s += L(X(b), 40, X(b), 70, 'soft'); s += T((X(a) + X(b)) / 2, 32, t, 'nt'); });
  s += `<rect x="${X(4e-7)}" y="40" width="${X(8e-7) - X(4e-7)}" height="30" fill="url(#vis)"/>`;
  [['1 pm', 1e-12], ['1 nm', 1e-9], ['1 µm', 1e-6], ['1 mm', 1e-3], ['1 m', 1]].forEach(([t, l]) => { s += L(X(l), 70, X(l), 76, 'soft') + T(X(l), 90, t, 'nt'); });
  return `<defs><linearGradient id="vis" x1="0" x2="1"><stop offset="0" stop-color="#7b2ff7"/><stop offset=".2" stop-color="#2b5cff"/><stop offset=".4" stop-color="#1fbf5f"/><stop offset=".6" stop-color="#f2d21b"/><stop offset=".8" stop-color="#ff8a1f"/><stop offset="1" stop-color="#e0262b"/></linearGradient></defs>
  ${s}${A(20, 104, 400, 104, 'soft')}${T(404, 108, 'λ', '', 'start')}
  ${L(X(4e-7), 70, 60, 140, 'dash soft')}${L(X(8e-7), 70, 360, 140, 'dash soft')}
  <rect x="60" y="140" width="300" height="26" fill="url(#vis)"/>${T(60, 184, '400 nm')}${T(210, 184, 'violet → rouge', 'nt')}${T(360, 184, '800 nm')}`;
})(), 'Spectre électromagnétique')],

'p1-onde-lumineuse-2': ['Diffraction par une fente de largeur a : demi-angle θ ≈ λ/a', svg(470, 215, `
  ${A(10, 105, 60, 105, 'r')}${L(10, 95, 110, 95, 'ray')}${L(10, 115, 110, 115, 'ray')}${T(20, 86, 'laser', 'nt', 'start')}
  ${R(108, 20, 6, 77, 'fill')}${R(108, 113, 6, 77, 'fill')}${D(126, 97, 126, 113, I('a'), 140, 108)}
  <path d="M114,97 L380,40 L380,170 L114,113 Z" class="s fillY" stroke="none"/>
  ${L(114, 105, 380, 105, 'axis')}${L(114, 97, 380, 40, 'ray')}${L(114, 113, 380, 170, 'ray')}
  <path d="M230,105 A116,116 0 0 0 227,80" class="s b"/>${T(240, 92, 'θ', 'b', 'start')}
  ${L(380, 15, 380, 195, 'thick')}${T(392, 20, 'écran', 'nt', 'start')}
  ${D(398, 40, 398, 170, '', 0, 0)}${T(406, 110, '≈ 2λ' + I('D') + '/' + I('a'), '', 'start')}${D(114, 200, 380, 200, I('D'))}`, 'Diffraction')],

// ---------------- Optique géométrique
'p1-optique-geo-1': ['Lois de Snell-Descartes : réflexion i₁′ = i₁ et réfraction n₁ sin i₁ = n₂ sin i₂ (ici n₂ > n₁)', svg(380, 230, `
  <rect x="20" y="115" width="340" height="100" class="fillA"/>${L(20, 115, 360, 115, 'thick')}${L(190, 15, 190, 215, 'axis')}
  ${T(30, 106, sb(I('n'), '1'), '', 'start')}${T(30, 136, sb(I('n'), '2'), '', 'start')}
  ${A(90, 25, 190, 115, 'r')}${A(190, 115, 290, 25, 'r')}${A(190, 115, 240, 210, 'r')}
  <path d="M190,70 A45,45 0 0 0 158,83" class="s"/>${T(172, 64, sb(I('i'), '1'), '', 'middle')}
  <path d="M190,70 A45,45 0 0 1 222,83" class="s"/>${T(210, 64, sb(I('i'), '1') + '′', '', 'middle')}
  <path d="M190,165 A50,50 0 0 0 213,159" class="s"/>${T(206, 180, sb(I('i'), '2'), '', 'start')}
  ${T(70, 40, 'incident', 'nt', 'end')}${T(300, 40, 'réfléchi', 'nt', 'start')}${T(250, 205, 'réfracté', 'nt', 'start')}`, 'Snell-Descartes')],

'p1-optique-geo-2': ['Réflexion totale : dans le milieu le plus réfringent (n₁ > n₂), au-delà de l’angle limite sin iℓ = n₂/n₁', svg(400, 230, `
  <rect x="20" y="115" width="360" height="100" class="fillA"/>${L(20, 115, 380, 115, 'thick')}
  ${T(30, 106, sb(I('n'), '2'), '', 'start')}${T(30, 136, sb(I('n'), '1') + ' > ' + sb(I('n'), '2'), '', 'start')}
  ${L(200, 20, 200, 215, 'axis')}
  ${A(150, 210, 200, 115, 'b')}${A(200, 115, 245, 30, 'b')}
  ${A(110, 205, 200, 115, 'r')}${A(200, 115, 370, 113, 'r')}
  ${A(60, 175, 200, 115, '')}${A(200, 115, 340, 175, '')}
  <path d="M200,165 A50,50 0 0 1 165,150" class="s r"/>${T(176, 172, sb(I('i'), 'ℓ'), 'r', 'middle')}
  ${T(250, 40, 'réfracté', 'b', 'start')}${T(372, 104, 'rasant', 'r', 'end')}${T(345, 192, 'réflexion totale', '', 'end')}`, 'Réflexion totale')],

'p1-optique-geo-3': ['Lentille convergente : construction de l’image A′B′ avec les trois rayons particuliers', svg(420, 220, (() => {
  const O = 210, Y = 110, f = 60, xA = 90, hB = 45;
  const OA = xA - O, OAp = 1 / (1 / f + 1 / OA), xAp = O + OAp, hBp = hB * OAp / OA;
  const yB = Y - hB, yBp = Y - hBp;
  return `${L(15, Y, 405, Y, 'axis')}${lens(O, Y, 150, true)}
  ${dot(O - f, Y)}${dot(O + f, Y)}${T(O - f, Y + 18, I('F'))}${T(O + f, Y + 18, I('F') + '′')}${T(O + 8, Y + 16, I('O'), '', 'start')}
  ${A(xA, Y, xA, yB, 'b')}${T(xA, Y + 18, I('A'))}${T(xA - 4, yB - 6, I('B'))}
  ${A(xAp, Y, xAp, yBp, 'b')}${T(xAp, Y - 8, I('A') + '′')}${T(xAp + 6, yBp + 14, I('B') + '′', '', 'start')}
  ${L(xA, yB, O, yB, 'ray')}${A(O, yB, xAp, yBp, 'ray')}
  ${A(xA, yB, xAp, yBp, 'ray')}
  ${L(xA, yB, O, yB + (Y - yB) * (O - xA) / ((O - f) - xA), 'ray')}${A(O, yB + (Y - yB) * (O - xA) / ((O - f) - xA), xAp + 40, yB + (Y - yB) * (O - xA) / ((O - f) - xA), 'ray')}`;
})(), 'Lentille convergente')],

'p1-optique-geo-4': ['Lentille divergente : image virtuelle, droite et réduite d’un objet réel (F′ est du côté de la lumière incidente)', svg(420, 220, (() => {
  const O = 250, Y = 120, f = -70, xA = 120, hB = 60;
  const OA = xA - O, OAp = 1 / (1 / f + 1 / OA), xAp = O + OAp, hBp = hB * OAp / OA;
  const yB = Y - hB, yBp = Y - hBp, xFp = O + f, xF = O - f;
  const slope = (yB - Y) / (O - xFp);   // rayon émergent semblant venir de F'
  return `${L(15, Y, 405, Y, 'axis')}${lens(O, Y, 150, false)}
  ${dot(xFp, Y)}${dot(xF, Y)}${T(xFp, Y + 18, I('F') + '′')}${T(xF, Y + 18, I('F'))}${T(O + 8, Y + 16, I('O'), '', 'start')}
  ${A(xA, Y, xA, yB, 'b')}${T(xA, Y + 18, I('A'))}${T(xA - 4, yB - 6, I('B'))}
  ${A(xAp, Y, xAp, yBp, 'b dash')}${T(xAp - 2, Y + 18, I('A') + '′')}${T(xAp - 6, yBp - 6, I('B') + '′', '', 'end')}
  ${L(xA, yB, O, yB, 'ray')}${A(O, yB, 400, yB + slope * (400 - O), 'ray')}${L(xFp, Y, O, yB, 'ray dash')}
  ${A(xA, yB, 400, yB + (Y - yB) * (400 - xA) / (O - xA), 'ray')}
  ${L(xA, yB, O, yB + (Y - yB) * (O - xA) / (xF - xA), 'ray')}${A(O, yBp, 400, yBp, 'ray')}${L(xAp, yBp, O, yBp, 'ray dash')}`;
})(), 'Lentille divergente')],

'p1-optique-geo-5': ['Lunette afocale (F′₁ = F₂) : un faisceau parallèle d’inclinaison α ressort parallèle avec l’inclinaison α′', svg(440, 220, (() => {
  const Y = 110, x1 = 50, f1 = 220, f2 = 70, x2 = x1 + f1 + f2, a = 0.12;
  const yF = Y + f1 * a;                    // image intermédiaire dans le plan focal
  const ap = (yF - Y) / f2;                 // pente émergente (rayon passant par O2)
  const pts = [-30, 0, 30].map(h => { const y1 = Y + h; const y2 = yF + (yF - y1) * f2 / f1; return {y1, y2}; });
  let s = `${L(10, Y, 430, Y, 'axis')}${lens(x1, Y, 120, true)}${lens(x2, Y, 90, true)}
  ${dot(x1 + f1, Y)}${T(x1 + f1, Y - 8, sb(I('F'), '1') + '′ = ' + sb(I('F'), '2'))}${T(x1, 40, sb(I('L'), '1'))}${T(x2, 55, sb(I('L'), '2'))}`;
  pts.forEach(({y1, y2}) => { s += A(x1 - 45, y1 - 45 * a, x1, y1, 'ray') + L(x1, y1, x1 + f1, yF, 'ray') + L(x1 + f1, yF, x2, y2, 'ray') + A(x2, y2, x2 + 60, y2 - 60 * ap, 'ray'); });
  s += `${T(x1 - 50, Y - 40, 'α', '', 'end')}${T(x2 + 66, Y - 24, 'α′', '', 'start')}`;
  return s + T(220, 210, 'grossissement ' + I('G') + ' = α′/α = −' + sb(I('f'), '1') + '′/' + sb(I('f'), '2') + '′', 'soft');
})(), 'Lunette afocale')],

'p1-optique-geo-6': ['Modèle réduit de l’œil : lentille (cristallin), diaphragme (iris), écran (rétine) à distance fixe', svg(400, 200, `
  ${L(20, 100, 380, 100, 'axis')}${lens(170, 100, 110, true)}
  ${R(165, 28, 10, 14, 'fill')}${R(165, 158, 10, 14, 'fill')}${T(170, 22, 'iris', 'nt')}
  ${L(320, 30, 320, 170, 'thick')}${T(330, 36, 'rétine', 'nt', 'start')}${T(170, 190, 'cristallin', 'nt')}
  ${[-40, 0, 40].map(h => A(30, 100 + h, 170, 100 + h, 'ray') + A(170, 100 + h, 320, 100, 'ray')).join('')}
  ${D(170, 140, 320, 140, I('d') + ' ≈ 17 mm', 245, 134)}${T(60, 60, 'objet à l’infini', 'nt')}`, 'Œil')],

// ---------------- Quantique
'p1-quantique-1': ['Fentes d’Young électron par électron : impacts aléatoires, puis franges quand leur nombre grandit', svg(440, 200, (() => {
  let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const tire = () => { for (;;) { const x = rnd() * 2 - 1, y = rnd(); const s = Math.PI * 3 * x; const p = Math.cos(Math.PI * 4 * x) ** 2 * (s === 0 ? 1 : (Math.sin(s) / s) ** 2); if (y < p) return x; } };
  const pan = (ox, n, lab) => { let s = R(ox, 30, 120, 130, 'fillW'); for (let i = 0; i < n; i++) s += `<circle cx="${f2(ox + 60 + 58 * tire())}" cy="${f2(34 + 122 * rnd())}" r="1.1" class="pt"/>`; return s + T(ox + 60, 180, lab, 'soft'); };
  return pan(15, 12, '10 impacts') + pan(160, 200, '200 impacts') + pan(305, 2500, '2 500 impacts');
})(), 'Fentes d’Young électrons')],

'p1-quantique-2': ['Niveaux d’énergie quantifiés : un photon est absorbé ou émis si hν = Eₙ − Eₚ', svg(380, 210, `
  ${[[30, 'E₁'], [100, 'E₂'], [140, 'E₃'], [160, 'E₄']].map(([y, t]) => L(60, 200 - y, 300, 200 - y) + T(310, 205 - y, I(t[0]) + t.slice(1), '', 'start')).join('')}
  ${A(120, 170, 120, 62, 'b')}${T(112, 110, 'absorption', 'b', 'end')}
  ${A(230, 100, 230, 168, 'r')}${T(240, 140, 'émission', 'r', 'start')}
  <path d="M60,40 q6,-8 12,0 t12,0 t12,0 t12,0 t12,0" class="s b"/>${A(120, 40, 135, 40, 'b')}${T(66, 28, 'h' + I('ν'), 'b', 'start')}
  <path d="M240,180 q6,-8 12,0 t12,0 t12,0 t12,0 t12,0" class="s r"/>${A(300, 180, 315, 180, 'r')}`, 'Niveaux d’énergie')],

// ---------------- Électrocinétique
'p1-arqs-1': ['Conventions : récepteur (flèches de u et i opposées), générateur (même sens)', svg(420, 160, `
  ${fil(20, 70, 70, 70)}${res(70, 70, 140, 70)}${fil(140, 70, 190, 70)}${cour(30, 70, 60, 70, I('i'))}${ten(140, 95, 70, 95, I('u'))}${T(105, 140, 'convention récepteur', 'nt')}
  ${fil(230, 70, 280, 70)}${res(280, 70, 350, 70)}${fil(350, 70, 400, 70)}${cour(240, 70, 270, 70, I('i'))}${ten(280, 95, 350, 95, I('u'))}${T(315, 140, 'convention générateur', 'nt')}`, 'Conventions')],

'p1-arqs-2': ['Lois de Kirchhoff : loi des nœuds (i₁ + i₂ = i₃) et loi des mailles (u₁ + u₂ − u₃ = 0)', svg(430, 228, `
  ${fil(30, 50, 100, 100)}${fil(30, 150, 100, 100)}${fil(100, 100, 180, 100)}${noeud(100, 100)}
  ${cour(45, 61, 70, 79, sb(I('i'), '1'))}${cour(45, 139, 70, 121, sb(I('i'), '2'))}${cour(130, 100, 160, 100, sb(I('i'), '3'))}${T(100, 190, 'nœud', 'nt')}
  ${res(240, 40, 330, 40)}${res(380, 60, 380, 150)}${res(330, 170, 240, 170)}${fil(330, 40, 380, 40)}${fil(380, 40, 380, 60)}${fil(380, 150, 380, 170)}${fil(380, 170, 330, 170)}${fil(240, 170, 220, 170)}${fil(220, 170, 220, 40)}${fil(220, 40, 240, 40)}
  ${ten(240, 22, 330, 22, sb(I('u'), '1'))}${ten(398, 60, 398, 150, sb(I('u'), '2'))}${ten(240, 192, 330, 192, sb(I('u'), '3'))}
  <path d="M285,80 A25,25 0 1 1 276,128" class="s soft"/>${A(279, 127, 272, 124, 'soft')}${T(300, 109, 'sens de', 'nt')}${T(300, 123, 'parcours', 'nt')}`, 'Kirchhoff')],

'p1-arqs-3': ['Diviseur de tension (série) et diviseur de courant (parallèle)', svg(440, 200, `
  ${fil(30, 40, 60, 40)}${res(60, 40, 120, 40)}${res(120, 40, 180, 40)}${fil(180, 40, 200, 40)}
  ${T(90, 28, sb(I('R'), '1'))}${T(150, 28, sb(I('R'), '2'))}${ten(200, 75, 30, 75, I('U'))}${ten(180, 22, 120, 22, sb(I('U'), '2'))}
  ${T(115, 120, sb(I('U'), '2') + ' = ' + sb(I('R'), '2') + I('U') + '/(' + sb(I('R'), '1') + ' + ' + sb(I('R'), '2') + ')', 'nt')}
  ${fil(250, 100, 290, 100)}${noeud(290, 100)}${fil(290, 100, 290, 60)}${fil(290, 100, 290, 140)}${fil(290, 60, 320, 60)}${fil(290, 140, 320, 140)}
  ${res(320, 60, 380, 60)}${res(320, 140, 380, 140)}${fil(380, 60, 400, 60)}${fil(380, 140, 400, 140)}${fil(400, 60, 400, 140)}${noeud(400, 100)}${fil(400, 100, 430, 100)}
  ${cour(255, 100, 280, 100, I('I'))}${cour(292, 140, 316, 140, '')}${T(304, 158, sb(I('I'), '2'), 'r')}${T(350, 48, sb(I('R'), '1'))}${T(350, 128, sb(I('R'), '2'))}
  ${T(345, 185, sb(I('I'), '2') + ' = ' + sb(I('R'), '1') + I('I') + '/(' + sb(I('R'), '1') + ' + ' + sb(I('R'), '2') + ')', 'nt')}`, 'Diviseurs')],

'p1-premier-ordre-1': ['Circuit RC série soumis à un échelon de tension E (interrupteur fermé à t = 0)', svg(400, 200, `
  ${gene(60, 70, 60, 150)}${ten(30, 150, 30, 70, I('E'), -1)}${fil(60, 70, 60, 40)}${fil(60, 40, 110, 40)}${inter(110, 40, 160, 40)}${T(135, 26, I('K'))}
  ${fil(160, 40, 190, 40)}${res(190, 40, 260, 40)}${T(225, 28, I('R'))}${fil(260, 40, 320, 40)}${fil(320, 40, 320, 95)}${cond(320, 95, 320, 115)}${fil(320, 115, 320, 170)}${fil(320, 170, 60, 170)}${fil(60, 170, 60, 150)}
  ${T(336, 108, I('C'), '', 'start')}${ten(350, 160, 350, 50, sb(I('u'), 'C'))}${cour(270, 40, 300, 40, I('i'))}`, 'Circuit RC')],

'p1-premier-ordre-2': ['Charge du condensateur : u_C(t) = E(1 − e^(−t/τ)), τ = RC ; 63 % de E à t = τ', svg(400, 210, (() => {
  const X0 = 50, Y0 = 170, sx = 60, E = 120;
  return `${axes(X0, Y0, 330, 10, 150, 0, I('t'), sb(I('u'), 'C'))}${courbe(u => E * (1 - Math.exp(-u / sx)), 0, 320, X0, Y0, 1, -1, 200, 'b')}
  ${L(X0, Y0 - E, X0 + 330, Y0 - E, 'dash soft')}${T(X0 - 6, Y0 - E + 4, I('E'), '', 'end')}
  ${L(X0, Y0, X0 + sx * 1.2, Y0 - E * 1.2, 'r')}${L(X0 + sx, Y0, X0 + sx, Y0 - E, 'dash soft')}${T(X0 + sx, Y0 + 16, 'τ')}
  ${L(X0, Y0 - 0.632 * E, X0 + sx, Y0 - 0.632 * E, 'dash soft')}${T(X0 - 6, Y0 - 0.632 * E + 4, '0,63' + I('E'), '', 'end')}
  ${L(X0 + 5 * sx, Y0, X0 + 5 * sx, Y0 - E, 'dash soft')}${T(X0 + 5 * sx, Y0 + 16, '5τ')}${T(X0 + 5 * sx - 4, Y0 - E - 8, '99 %', 'nt', 'end')}${T(X0 + 70, 40, 'tangente à l’origine', 'r', 'start')}`;
})(), 'Charge RC')],

'p1-premier-ordre-3': ['Circuit RL série : le courant s’établit avec la constante de temps τ = L/R', svg(400, 200, `
  ${gene(60, 70, 60, 150)}${ten(30, 150, 30, 70, I('E'), -1)}${fil(60, 70, 60, 40)}${fil(60, 40, 110, 40)}${inter(110, 40, 160, 40)}${T(135, 26, I('K'))}
  ${fil(160, 40, 190, 40)}${res(190, 40, 260, 40)}${T(225, 28, I('R'))}${fil(260, 40, 320, 40)}${bobine(320, 40, 320, 170)}${fil(320, 170, 60, 170)}${fil(60, 170, 60, 150)}
  ${T(340, 108, I('L'), '', 'start')}${ten(360, 160, 360, 50, sb(I('u'), 'L'))}${cour(270, 40, 300, 40, I('i'))}`, 'Circuit RL')],

'p1-second-ordre-1': ['Circuit RLC série alimenté par un échelon de tension', svg(420, 200, `
  ${gene(50, 70, 50, 150)}${ten(22, 150, 22, 70, I('E'), -1)}${fil(50, 70, 50, 40)}${fil(50, 40, 80, 40)}${inter(80, 40, 120, 40)}
  ${res(120, 40, 180, 40)}${T(150, 28, I('R'))}${bobine(190, 40, 280, 40)}${fil(180, 40, 190, 40)}${T(235, 26, I('L'))}${fil(280, 40, 340, 40)}
  ${fil(340, 40, 340, 95)}${cond(340, 95, 340, 115)}${fil(340, 115, 340, 170)}${fil(340, 170, 50, 170)}${fil(50, 170, 50, 150)}
  ${T(356, 108, I('C'), '', 'start')}${ten(372, 160, 372, 50, sb(I('u'), 'C'))}${cour(290, 40, 320, 40, I('i'))}`, 'Circuit RLC')],

'p1-second-ordre-2': ['Réponse indicielle : régimes pseudo-périodique (Q > ½), critique (Q = ½) et apériodique (Q < ½)', svg(400, 220, (() => {
  const X0 = 50, Y0 = 180, sx = 26, E = 100;   // ω₀ = 1 rad par unité, sx pixels par unité de ω₀t
  const rep = Q => t => {
    const a = 1 / (2 * Q);
    if (Math.abs(a - 1) < 1e-9) return 1 - (1 + t) * Math.exp(-t);
    if (a < 1) { const w = Math.sqrt(1 - a * a); return 1 - Math.exp(-a * t) * (Math.cos(w * t) + a / w * Math.sin(w * t)); }
    const r = Math.sqrt(a * a - 1), r1 = -a + r, r2 = -a - r; return 1 - (r2 * Math.exp(r1 * t) - r1 * Math.exp(r2 * t)) / (r2 - r1);
  };
  return `${axes(X0, Y0, 330, 10, 170, 0, sb('ω', '0') + I('t'), sb(I('u'), 'C'))}${L(X0, Y0 - E, X0 + 330, Y0 - E, 'dash soft')}${T(X0 - 6, Y0 - E + 4, I('E'), '', 'end')}
  ${courbe(u => E * rep(3)(u / sx), 0, 320, X0, Y0, 1, -1, 300)}${courbe(u => E * rep(0.5)(u / sx), 0, 320, X0, Y0, 1, -1, 200, 'b')}${courbe(u => E * rep(0.2)(u / sx), 0, 320, X0, Y0, 1, -1, 200, 'r')}
  ${T(150, 40, 'pseudo-périodique (' + I('Q') + ' = 3)', '', 'start')}${T(370, 72, 'critique', 'b', 'end')}${T(250, 125, 'apériodique', 'r', 'start')}`;
})(), 'Trois régimes')],

'p1-sinusoidal-1': ['Représentation de Fresnel du RLC série : U = U_R + U_L + U_C, déphasage φ de u sur i', svg(360, 230, `
  ${A(40, 130, 330, 130, 'axis')}${T(332, 124, 'axe de ' + I('i'), 'nt', 'end')}
  ${A(60, 130, 200, 130, 'b')}${T(130, 150, sb(I('U'), 'R'), 'b')}
  ${A(200, 130, 200, 30, 'r')}${T(212, 70, sb(I('U'), 'L'), 'r', 'start')}
  ${A(200, 30, 200, 75, '')}${T(186, 56, sb(I('U'), 'C'), '', 'end')}
  ${A(60, 130, 200, 75, 'thick')}${T(120, 92, I('U'), '', 'end')}
  <path d="M110,130 A50,50 0 0 0 106,112" class="s"/>${T(118, 122, 'φ', '', 'start')}`, 'Fresnel')],

'p1-sinusoidal-2': ['Résonance en intensité du RLC série : maximum en ω₀ quel que soit Q, bande passante Δω = ω₀/Q', svg(400, 220, (() => {
  const X0 = 40, Y0 = 180, sx = 120, H = 150;
  const g = Q => x => x <= 0 ? 0 : 1 / Math.sqrt(1 + Q * Q * (x - 1 / x) ** 2);
  const x1 = Q => (-1 / Q + Math.sqrt(1 / Q / Q + 4)) / 2, xc = Q => (1 / Q + Math.sqrt(1 / Q / Q + 4)) / 2;
  return `${axes(X0, Y0, 340, 10, 170, 0, 'ω/' + sb('ω', '0'), I('I') + '/' + sb(I('I'), 'max'))}
  ${[[0.7, 'soft'], [2, ''], [6, 'b']].map(([Q, c]) => courbe(u => H * g(Q)(u / sx), 0.5, 330, X0, Y0, 1, -1, 400, c)).join('')}
  ${L(X0 + sx, Y0, X0 + sx, Y0 - H, 'dash soft')}${T(X0 + sx, Y0 + 16, '1')}${L(X0, Y0 - H, X0 + 330, Y0 - H, 'dash soft')}${T(X0 - 6, Y0 - H + 4, '1', '', 'end')}
  ${L(X0, Y0 - H / Math.SQRT2, X0 + 330, Y0 - H / Math.SQRT2, 'dash soft')}${T(X0 - 6, Y0 - H / Math.SQRT2 + 4, '1/√2', '', 'end')}
  ${D(X0 + sx * x1(6), Y0 - H / Math.SQRT2 + 12, X0 + sx * xc(6), Y0 - H / Math.SQRT2 + 12, '', 0, 0)}${T(X0 + sx * xc(6) + 6, Y0 - H / Math.SQRT2 + 24, 'Δω', 'b', 'start')}
  ${T(300, 60, I('Q') + ' = 6', 'b')}${T(300, 120, I('Q') + ' = 2')}${T(300, 150, I('Q') + ' = 0,7', 'nt')}`;
})(), 'Résonance en intensité')],

'p1-sinusoidal-3': ['Tension aux bornes de C : résonance seulement si Q > 1/√2, à une pulsation inférieure à ω₀', svg(400, 220, (() => {
  const X0 = 40, Y0 = 180, sx = 120, H = 40;
  const g = Q => x => 1 / Math.sqrt((1 - x * x) ** 2 + (x / Q) ** 2);
  return `${axes(X0, Y0, 340, 10, 170, 0, 'ω/' + sb('ω', '0'), sb(I('U'), 'C') + '/' + I('E'))}
  ${[[0.4, 'soft'], [0.707, 'r'], [1.5, ''], [3, 'b']].map(([Q, c]) => courbe(u => Math.min(165, H * g(Q)(u / sx)), 0, 330, X0, Y0, 1, -1, 400, c)).join('')}
  ${L(X0, Y0 - H, X0 + 330, Y0 - H, 'dash soft')}${T(X0 - 6, Y0 - H + 4, '1', '', 'end')}${L(X0 + sx, Y0, X0 + sx, 20, 'dash soft')}${T(X0 + sx, Y0 + 16, '1')}
  ${T(X0 + sx * 0.97 + 10, 24, I('Q') + ' = 3', 'b', 'start')}${T(250, 70, I('Q') + ' = 1,5', '', 'start')}${T(80, 128, I('Q') + ' = 1/√2', 'r', 'start')}${T(70, 162, I('Q') + ' = 0,4', 'nt', 'start')}`;
})(), 'Résonance en tension')],

'p1-frequentielle-1': ['Spectre d’un créneau impair : harmoniques impaires d’amplitudes 4E/(nπ)', svg(420, 210, (() => {
  const X0 = 190, Y0 = 170, sx = 20, H = 120;
  let s = `${axes(X0, Y0, 220, 10, 150, 0, I('f') + '/' + sb(I('f'), '1'), '')}`;
  [1, 3, 5, 7, 9].forEach(n => { s += L(X0 + n * sx, Y0, X0 + n * sx, Y0 - H / n, 'thick b') + T(X0 + n * sx, Y0 + 16, String(n)); });
  s += T(X0 + sx + 8, Y0 - H + 4, '4' + I('E') + '/π', 'b', 'start');
  s += `${axes(30, 100, 140, 10, 50, 50, I('t'), '')}${P('M30,60 H60 V140 H90 V60 H120 V140 H150 V60', 'r')}${T(26, 64, I('E'), 'r', 'end')}`;
  return s;
})(), 'Spectre du créneau')],

'p1-frequentielle-2': ['Diagramme de Bode d’un passe-bas du premier ordre : gain, phase et asymptotes', svg(420, 260, (() => {
  const X0 = 60, sx = 80, Yg = 30, Yp = 170;          // log10(x) de −2 à +2
  const gdB = x => -10 * Math.log10(1 + x * x), ph = x => -Math.atan(x) * 180 / Math.PI;
  const px = u => X0 + (u + 2) * sx;
  return `${axes(X0, Yg, 330, 10, 14, 110, 'log(ω/' + sb('ω', 'c') + ')', sb(I('G'), 'dB'))}
  ${courbe(u => -2.2 * gdB(10 ** u), -2, 2, X0 + 2 * sx, Yg, sx, 1, 200)}${L(X0, Yg, px(0), Yg, 'r dash')}${L(px(0), Yg, px(2), Yg + 2.2 * 40, 'r dash')}
  ${T(px(1.3), Yg + 70, '−20 dB/décade', 'r', 'start')}${dot(px(0), Yg + 2.2 * 3.01)}${T(px(0) - 8, Yg + 24, '−3 dB', '', 'end')}
  ${axes(X0, Yp, 330, 10, 14, 90, '', 'φ')}${courbe(u => -0.8 * ph(10 ** u), -2, 2, X0 + 2 * sx, Yp, sx, 1, 200, 'b')}
  ${L(X0, Yp + 72, X0 + 330, Yp + 72, 'dash soft')}${T(X0 - 6, Yp + 76, '−90°', '', 'end')}${T(X0 - 6, Yp + 4, '0', '', 'end')}${dot(px(0), Yp + 36, 'r')}${T(px(0) + 6, Yp + 32, '−45°', '', 'start')}
  ${L(px(0), Yg, px(0), Yp + 72, 'dash soft')}${T(px(0), Yp + 90, sb('ω', 'c'))}`;
})(), 'Bode')],

'p1-filtrage-1': ['Passe-bas RC : H = 1/(1 + jω/ω_c), ω_c = 1/RC', svg(460, 200, `
  ${fil(20, 50, 50, 50)}${res(50, 50, 110, 50)}${T(80, 38, I('R'))}${fil(110, 50, 150, 50)}${noeud(150, 50)}${fil(150, 50, 190, 50)}
  ${fil(150, 50, 150, 85)}${cond(150, 85, 150, 105)}${fil(150, 105, 150, 140)}${T(166, 100, I('C'), '', 'start')}${fil(20, 140, 190, 140)}
  ${ten(20, 130, 20, 60, sb(I('v'), 'e'))}${ten(190, 130, 190, 60, sb(I('v'), 's'))}
  ${flt(240, 40, 'bas')}`, 'Passe-bas RC')],

'p1-filtrage-2': ['Passe-haut RC : H = jω/ω_c / (1 + jω/ω_c), ω_c = 1/RC', svg(460, 200, `
  ${fil(20, 50, 60, 50)}${cond(60, 50, 80, 50)}${T(70, 34, I('C'))}${fil(80, 50, 150, 50)}${noeud(150, 50)}${fil(150, 50, 190, 50)}
  ${fil(150, 50, 150, 65)}${res(150, 65, 150, 125)}${fil(150, 125, 150, 140)}${T(166, 100, I('R'), '', 'start')}${fil(20, 140, 190, 140)}
  ${ten(20, 130, 20, 60, sb(I('v'), 'e'))}${ten(190, 130, 190, 60, sb(I('v'), 's'))}
  ${flt(240, 40, 'haut')}`, 'Passe-haut RC')],

'p1-filtrage-3': ['Passe-bande RLC (sortie aux bornes de R) : gain maximal 0 dB en ω₀, bande passante ω₀/Q', svg(470, 200, `
  ${fil(10, 50, 20, 50)}${bobine(20, 50, 80, 50)}${T(50, 34, I('L'))}${fil(80, 50, 90, 50)}${cond(90, 50, 110, 50)}${T(100, 34, I('C'))}${fil(110, 50, 150, 50)}${noeud(150, 50)}${fil(150, 50, 190, 50)}
  ${fil(150, 50, 150, 65)}${res(150, 65, 150, 125)}${fil(150, 125, 150, 140)}${T(166, 100, I('R'), '', 'start')}${fil(10, 140, 190, 140)}
  ${ten(10, 130, 10, 60, sb(I('v'), 'e'))}${ten(190, 130, 190, 60, sb(I('v'), 's'))}
  ${flt(240, 40, 'bande')}`, 'Passe-bande RLC')],

'p1-filtrage-4': ['Effet d’un passe-bas sur un spectre : les composantes au-delà de la coupure sont atténuées', svg(440, 180, (() => {
  const pan = (ox, title, hs, extra = '') => `${axes(ox, 140, 120, 6, 110, 0, I('f'), '')}${hs.map((h, k) => L(ox + 12 + k * 18, 140, ox + 12 + k * 18, 140 - h, 'thick b')).join('')}${extra}${T(ox + 60, 170, title, 'nt')}`;
  const ent = [90, 30, 18, 13, 10, 8];
  const H = k => 1 / Math.sqrt(1 + ((1 + 2 * k) / 2.5) ** 2);
  return pan(15, 'entrée', ent) + `${axes(160, 140, 120, 6, 110, 0, I('f'), '')}${courbe(u => 100 * H((u - 12) / 18), 0, 118, 160, 140, 1, -1, 120, 'r')}${T(220, 170, 'gain du filtre', 'nt')}`
    + pan(305, 'sortie', ent.map((h, k) => h * H(k)));
})(), 'Effet d’un filtre')],
};
