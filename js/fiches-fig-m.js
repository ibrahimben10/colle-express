// Schémas des fiches de cours — Mathématiques MPSI et MP.
import { svg, L, A, D, T, I, C, R, P, dot, sb } from './figkit.js';
import { axes, courbe } from './fiches-kit.js';

const r2 = n => Math.round(n * 100) / 100;
const rad = d => d * Math.PI / 180;
const pol = (x, y, r, deg) => [r2(x + r * Math.cos(rad(deg))), r2(y - r * Math.sin(rad(deg)))];
const arc = (x, y, r, d1, d2, c = 'soft') => { const [a, b] = pol(x, y, r, d1), [e, f] = pol(x, y, r, d2); return P(`M${a},${b} A${r},${r} 0 ${Math.abs(d2 - d1) > 180 ? 1 : 0} ${d2 > d1 ? 0 : 1} ${e},${f}`, c); };
const sup = (b, s) => `${b}<tspan baseline-shift="super" font-size="10">${s}</tspan>`;
const pts = (f, a, b, n, X, Y) => Array.from({length: n + 1}, (_, i) => { const x = a + (b - a) * i / n; return [X(x), Y(f(x))]; });
const chemin = (p, c = 'b') => P('M' + p.map(q => q.map(r2).join(',')).join(' L'), c);
// repère mathématique : origine (ox, oy), échelle s (pixels par unité)
const rep = (ox, oy, s) => [x => r2(ox + x * s), y => r2(oy - y * s)];

// patates pour les applications
const patate = (cx, cy, rx, ry) => `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" class="s fillA"/>`;
const sagittal = (x0, fl, nE, nF, titre) => {
  const E = Array.from({length: nE}, (_, i) => [x0 + 30, 50 + i * 30]), F = Array.from({length: nF}, (_, i) => [x0 + 110, 50 + i * 30]);
  return patate(x0 + 30, 80, 22, 58) + patate(x0 + 110, 80, 22, 58) + E.map(([x, y]) => dot(x, y)).join('') + F.map(([x, y]) => dot(x, y)).join('')
    + fl.map(([i, j]) => A(E[i][0] + 4, E[i][1], F[j][0] - 5, F[j][1], 'b')).join('') + T(x0 + 70, 168, titre, 'nt') + T(x0 + 30, 16, I('E')) + T(x0 + 110, 16, I('F'));
};

export const FIGS = {
'm1-logique-1': ['Injection : deux éléments distincts ont des images distinctes. Surjection : tout élément de l’ensemble d’arrivée a au moins un antécédent. Bijection : les deux à la fois (exactement un antécédent)', svg(460, 180,
  sagittal(10, [[0, 0], [1, 2], [2, 3]], 3, 4, 'injective, non surjective') + sagittal(160, [[0, 0], [1, 1], [2, 1], [3, 2]], 4, 3, 'surjective, non injective') + sagittal(310, [[0, 1], [1, 2], [2, 0]], 3, 3, 'bijective'), 'Applications')],

'm1-complexes-1': ['Forme exponentielle : le point M d’affixe z = r e^{iθ} est à la distance r = |z| de l’origine, et θ est un argument de z ; z̄ est le symétrique de z par rapport à l’axe réel', svg(380, 280, (() => {
  const [X, Y] = rep(150, 150, 90);
  return A(30, 150, 350, 150, 'soft') + A(150, 270, 150, 20, 'soft') + T(354, 154, 'Re', 'nt', 'start') + T(156, 22, 'Im', 'nt', 'start') + C(150, 150, 90, 'dash soft')
    + L(150, 150, ...pol(150, 150, 120, 35), 'b') + dot(...pol(150, 150, 120, 35)) + T(...pol(150, 150, 132, 38), I('z')) + arc(150, 150, 34, 0, 35, 'r') + T(...pol(150, 150, 46, 17), I('θ'), 'r')
    + T(...pol(150, 150, 66, 50), I('r'), 'b') + L(...pol(150, 150, 120, 35), r2(pol(150, 150, 120, 35)[0]), 150, 'dash soft') + L(...pol(150, 150, 120, -35), r2(pol(150, 150, 120, -35)[0]), 150, 'dash soft')
    + dot(...pol(150, 150, 120, -35)) + T(...pol(150, 150, 134, -38), 'z̄') + T(X(1) + 4, 166, '1', '', 'start') + T(156, Y(1) - 4, I('i'), '', 'start') + T(199, 168, I('r') + ' cos ' + I('θ'), 'nt');
})(), 'Forme exponentielle')],

'm1-fonctions-1': ['L’exponentielle et le logarithme népérien sont réciproques l’une de l’autre : leurs courbes sont symétriques par rapport à la droite y = x', svg(360, 300, (() => {
  const [X, Y] = rep(140, 180, 40);
  return A(20, 180, 350, 180, 'soft') + A(140, 296, 140, 10, 'soft') + L(X(-2.5), Y(-2.5), X(4.2), Y(4.2), 'dash soft') + T(X(4.2), Y(4.2) + 14, I('y') + ' = ' + I('x'), 'nt', 'end')
    + chemin(pts(Math.exp, -3, 1.45, 80, X, Y), 'b') + chemin(pts(Math.log, 0.06, 5.2, 120, X, Y), 'r') + T(X(1.3), Y(4) - 2, 'exp', 'b', 'end') + T(X(5), Y(1.6) - 10, 'ln', 'r', 'end')
    + dot(X(0), Y(1)) + dot(X(1), Y(0)) + T(X(0) - 6, Y(1) + 4, '1', '', 'end') + T(X(1), Y(0) + 16, '1');
})(), 'exp et ln')],

'm1-suites-1': ['Suite récurrente u_{n+1} = f(u_n) : on reporte u_n sur l’axe des abscisses grâce à la droite y = x. Ici f est croissante : la suite est monotone et converge vers le point fixe ℓ', svg(360, 300, (() => {
  const f = x => 1 + 0.5 * x, [X, Y] = rep(40, 270, 60);
  let s = A(30, 270, 350, 270, 'soft') + A(40, 285, 40, 10, 'soft') + L(X(0), Y(0), X(4.8), Y(4.8), 'dash soft') + chemin(pts(f, 0, 4.8, 10, X, Y), 'b') + T(X(4.8), Y(f(4.8)) - 6, I('f'), 'b', 'end');
  let u = 0.3; const v = [u];
  for (let k = 0; k < 5; k++) { const w = f(u); s += L(X(u), Y(k ? u : 0), X(u), Y(w), 'r') + L(X(u), Y(w), X(w), Y(w), 'r'); u = w; v.push(u); }
  return s + v.slice(0, 3).map((x, k) => L(X(x), 266, X(x), 274) + T(X(x), 288, sb(I('u'), String(k)))).join('') + dot(X(2), Y(2)) + T(X(2) + 8, Y(2) + 16, 'ℓ', '', 'start');
})(), 'Suite récurrente')],

'm1-continuite-1': ['Théorème des valeurs intermédiaires : si f est continue sur [a, b], elle prend toute valeur y comprise entre f(a) et f(b) (en au moins un point c)', svg(380, 250, (() => {
  const f = x => 0.8 + 0.35 * x + 0.9 * Math.sin(1.4 * x), [X, Y] = rep(40, 220, 60);
  return axes(40, 220, 330, 0, 205, 0, I('x'), '') + chemin(pts(f, 0.3, 5, 120, X, Y), 'b') + L(X(0.3), 220, X(0.3), Y(f(0.3)), 'dash soft') + L(X(5), 220, X(5), Y(f(5)), 'dash soft')
    + T(X(0.3), 236, I('a')) + T(X(5), 236, I('b')) + L(40, Y(1.9), 360, Y(1.9), 'r') + T(36, Y(1.9) + 4, I('y'), 'r', 'end')
    + dot(X(0.82), Y(1.9), 'r') + L(X(0.82), Y(1.9), X(0.82), 220, 'dash soft') + T(X(0.82), 236, I('c'), 'r');
})(), 'TVI')],

'm1-derivabilite-1': ['Théorème des accroissements finis : si f est continue sur [a, b] et dérivable sur ]a, b[, il existe c ∈ ]a, b[ où la tangente est parallèle à la corde : f(b) − f(a) = f′(c)(b − a)', svg(380, 250, (() => {
  const f = x => 0.5 + 0.9 * x - 0.12 * x * x + 0.3 * Math.sin(2 * x), [X, Y] = rep(40, 220, 55);
  const a = 0.4, b = 5, p = (f(b) - f(a)) / (b - a);
  let c = 0, best = 9; for (let x = a; x < b; x += 0.001) { const d = Math.abs((f(x + 1e-5) - f(x)) / 1e-5 - p); if (d < best && x > 1.5) { best = d; c = x; } }
  const t = x => f(c) + p * (x - c);
  return axes(40, 220, 330, 0, 205, 0, I('x'), '') + chemin(pts(f, 0.2, 5.4, 120, X, Y), 'b') + L(X(a), Y(f(a)), X(b), Y(f(b)), 'r') + dot(X(a), Y(f(a))) + dot(X(b), Y(f(b)))
    + L(X(c - 1.6), Y(t(c - 1.6)), X(c + 1.6), Y(t(c + 1.6)), 'r dash') + dot(X(c), Y(f(c)), 'r') + L(X(c), Y(f(c)), X(c), 220, 'dash soft') + T(X(a), 236, I('a')) + T(X(b), 236, I('b')) + T(X(c), 236, I('c'), 'r');
})(), 'Accroissements finis')],

'm1-derivabilite-2': ['Fonction convexe : la courbe est au-dessous de ses cordes et au-dessus de ses tangentes ; pour f deux fois dérivable, f convexe ⇔ f″ ≥ 0', svg(380, 250, (() => {
  const f = x => 0.25 * (x - 2.6) ** 2 + 0.5, [X, Y] = rep(40, 220, 55);
  return axes(40, 220, 330, 0, 205, 0, I('x'), '') + chemin(pts(f, 0, 5.6, 120, X, Y), 'b') + L(X(0.8), Y(f(0.8)), X(4.8), Y(f(4.8)), 'r') + dot(X(0.8), Y(f(0.8))) + dot(X(4.8), Y(f(4.8)))
    + L(X(3.6 - 1.8), Y(f(3.6) + 0.5 * (3.6 - 2.6) * -1.8), X(3.6 + 1.7), Y(f(3.6) + 0.5 * (3.6 - 2.6) * 1.7), 'b dash') + dot(X(3.6), Y(f(3.6)), 'b') + T(X(4.8) + 6, Y(f(4.8)), 'corde', 'r', 'start') + T(X(5.3), Y(f(3.6) + 0.5 * 1.7) + 18, 'tangente', 'b', 'end');
})(), 'Convexité')],

'm1-asymptotique-1': ['Développement limité de sin en 0 : les polynômes de Taylor x, x − x³/6, x − x³/6 + x⁵/120 approchent de mieux en mieux la fonction au voisinage de 0', svg(400, 260, (() => {
  const [X, Y] = rep(200, 130, 45);
  return A(20, 130, 390, 130, 'soft') + A(200, 250, 200, 10, 'soft') + chemin(pts(Math.sin, -4, 4, 160, X, Y), 'b thick')
    + chemin(pts(x => x, -2.4, 2.4, 2, X, Y), 'soft') + chemin(pts(x => x - x ** 3 / 6, -3.3, 3.3, 80, X, Y), 'r dash') + chemin(pts(x => x - x ** 3 / 6 + x ** 5 / 120, -3.9, 3.9, 80, X, Y), 'r')
    + T(X(3.9), Y(1.8), sup('ordre ', '') + '5', 'r', 'end') + T(X(3.2), Y(-2.9), 'ordre 3', 'r', 'end') + T(X(2.3), Y(2.6), 'ordre 1', 'nt', 'end') + T(X(-3.6), Y(0.9), 'sin', 'b', 'middle');
})(), 'Développements limités')],

'm1-polynomes-1': ['Les racines n-ièmes de l’unité ω_k = e^{2ikπ/n} (ici n = 6) sont les sommets d’un polygone régulier inscrit dans le cercle unité ; leur somme est nulle pour n ≥ 2', svg(320, 280, (() => {
  let s = A(20, 140, 300, 140, 'soft') + A(160, 270, 160, 10, 'soft') + C(160, 140, 100, 'dash soft');
  const v = Array.from({length: 6}, (_, k) => pol(160, 140, 100, k * 60));
  s += P('M' + v.map(p => p.join(',')).join(' L') + 'Z', 'b fillA') + v.map((p, k) => dot(...p) + T(...pol(160, 140, 118, k * 60).map((q, i) => i ? q + 5 : q), sb('ω', String(k)))).join('');
  return s + arc(160, 140, 30, 0, 60, 'r') + T(...pol(160, 140, 46, 28), '2π/6', 'r');
})(), 'Racines de l’unité')],

'm1-ev-1': ['Si E = F ⊕ G, tout vecteur x s’écrit de façon unique x = x_F + x_G ; la projection sur F parallèlement à G associe x_F à x (p ∘ p = p)', svg(380, 240, (() => {
  const O = [170, 166], f = [330, -80], g = [90, -210], at = (v, t) => [r2(O[0] + v[0] * t), r2(O[1] + v[1] * t)];
  const xF = at(f, 0.4), xG = at(g, 0.45), x = [r2(xF[0] + xG[0] - O[0]), r2(xF[1] + xG[1] - O[1])];
  return L(...at(f, -0.42), ...at(f, 0.58), 'b thick') + T(...at(f, 0.56).map((v, i) => i ? v - 10 : v), I('F'), 'b', 'end') + L(...at(g, -0.3), ...at(g, 0.68), 'r thick') + T(...at(g, 0.68).map((v, i) => i ? v + 6 : v + 6), I('G'), 'r', 'start')
    + A(...O, ...x) + T(x[0] + 6, x[1] - 2, I('x'), '', 'start') + A(...O, ...xF, 'b') + T(xF[0] + 4, xF[1] + 18, sb(I('x'), I('F')), 'b', 'start') + A(...O, ...xG, 'r') + T(xG[0] - 8, xG[1], sb(I('x'), I('G')), 'r', 'end')
    + L(...xF, ...x, 'dash soft') + L(...xG, ...x, 'dash soft') + dot(...O) + T(O[0] - 8, O[1] + 14, '0', '', 'end');
})(), 'Projection')],

'm1-determinants-1': ['En dimension 2, |det(u, v)| est l’aire du parallélogramme construit sur u et v ; le signe indique l’orientation (positif si on tourne de u vers v dans le sens direct)', svg(360, 230, (() => {
  const O = [60, 190], u = [200, -30], v = [70, -130];
  return P(`M${O.join(',')} L${O[0] + u[0]},${O[1] + u[1]} L${O[0] + u[0] + v[0]},${O[1] + u[1] + v[1]} L${O[0] + v[0]},${O[1] + v[1]} Z`, 'fillA') + A(...O, O[0] + u[0], O[1] + u[1], 'b') + A(...O, O[0] + v[0], O[1] + v[1], 'r')
    + T(O[0] + u[0] / 2, O[1] + u[1] / 2 + 18, I('u'), 'b') + T(O[0] + v[0] / 2 - 12, O[1] + v[1] / 2, I('v'), 'r', 'end') + T(O[0] + (u[0] + v[0]) / 2, O[1] + (u[1] + v[1]) / 2 + 6, 'aire = |det(' + I('u') + ', ' + I('v') + ')|', '', 'middle')
    + arc(...O, 38, 8.5, 61.7, 'soft');
})(), 'Déterminant et aire')],

'm1-prehilbertiens-1': ['Projection orthogonale sur un sous-espace F de dimension finie : p(x) est l’unique vecteur de F tel que x − p(x) ⊥ F ; c’est le point de F le plus proche de x, d(x, F) = ‖x − p(x)‖', svg(380, 240, `
  <path d="M30,200 L250,200 L350,130 L130,130 Z" class="s fillA"/>${T(60, 190, I('F'), 'b', 'start')}
  ${dot(150, 175)}${T(140, 190, '0', '', 'end')}${A(150, 175, 250, 40)}${T(256, 38, I('x'), '', 'start')}${A(150, 175, 250, 165, 'b')}${T(256, 172, I('p') + '(' + I('x') + ')', 'b', 'start')}
  ${L(250, 40, 250, 165, 'r')}${P('M250,152 L240,150 L240,163', 'soft')}${T(258, 105, I('x') + ' − ' + I('p') + '(' + I('x') + ')', 'r', 'start')}`, 'Projection orthogonale')],

'm1-integration-1': ['Sommes de Riemann : pour f continue sur [a, b], (b − a)/n · Σ f(a + k(b − a)/n) tend vers ∫ₐᵇ f quand n → +∞', svg(400, 240, (() => {
  const f = x => 1.2 + 0.8 * Math.sin(x) + 0.15 * x, [X, Y] = rep(40, 210, 55);
  let s = axes(40, 210, 350, 0, 195, 0, I('x'), '');
  for (let k = 0; k < 8; k++) { const x = 0.5 + k * 0.6; s += R(X(x), Y(f(x)), r2(0.6 * 55), r2(f(x) * 55), 'fillA b'); }
  return s + chemin(pts(f, 0.2, 5.6, 120, X, Y), 'r') + T(X(0.5), 226, I('a')) + T(X(5.3), 226, I('b'));
})(), 'Sommes de Riemann')],

'm1-series-1': ['Comparaison série-intégrale : pour f continue, positive et décroissante, ∫ₖᵏ⁺¹ f ≤ f(k) ≤ ∫ₖ₋₁ᵏ f ; la série Σ f(n) et l’intégrale ∫₁^{+∞} f sont de même nature', svg(400, 240, (() => {
  const f = x => 3.2 / x, [X, Y] = rep(40, 210, 50);
  let s = axes(40, 210, 350, 0, 195, 0, I('x'), '');
  for (let k = 1; k <= 6; k++) s += R(X(k), Y(f(k)), 50, r2(f(k) * 50), 'fillA b');
  return s + chemin(pts(f, 0.85, 6.9, 120, X, Y), 'r') + [1, 2, 3, 4, 5, 6, 7].map(k => T(X(k), 226, String(k))).join('') + T(X(1.5) + 30, Y(f(1)) - 4, I('f'), 'r', 'start');
})(), 'Série et intégrale')],

'm1-probas-1': ['Arbre de probabilités : formule des probabilités totales P(B) = P(A)P_A(B) + P(Ā)P_Ā(B), puis formule de Bayes P_B(A) = P(A)P_A(B)/P(B)', svg(420, 230, `
  ${dot(40, 115)}${L(40, 115, 170, 55)}${L(40, 115, 170, 175)}${T(100, 72, I('P') + '(' + I('A') + ')', 'nt', 'end')}${T(100, 168, I('P') + '(Ā)', 'nt', 'end')}
  ${T(182, 60, I('A'), '', 'start')}${T(182, 180, 'Ā', '', 'start')}
  ${L(200, 55, 320, 25)}${L(200, 55, 320, 85)}${L(200, 175, 320, 145)}${L(200, 175, 320, 205)}
  ${T(332, 30, I('B'), 'b', 'start')}${T(332, 90, 'B̄', '', 'start')}${T(332, 150, I('B'), 'b', 'start')}${T(332, 210, 'B̄', '', 'start')}
  ${T(258, 30, sb(I('P'), I('A')) + '(' + I('B') + ')', 'nt', 'end')}${T(258, 150, sb(I('P'), 'Ā') + '(' + I('B') + ')', 'nt', 'end')}`, 'Arbre')],

// ---------- MP ----------
'm2-reduction-1': ['Si u est diagonalisable, il existe une base de vecteurs propres : u multiplie chacun par sa valeur propre (ici u(e₁) = 2e₁ et u(e₂) = ½e₂, en gras) ; dans cette base, la matrice de u est diagonale', svg(400, 240, (() => {
  const O = [170, 150], e1 = [80, -24], e2 = [-30, -70];
  const tr = ([a, b], k) => [r2(O[0] + a * k), r2(O[1] + b * k)];
  return L(...tr(e1, -1.6), ...tr(e1, 2.6), 'dash soft') + L(...tr(e2, -1.2), ...tr(e2, 1.8), 'dash soft')
    + A(...O, ...tr(e1, 2), 'b thick') + A(...O, ...tr(e1, 1), 'b') + T(tr(e1, 0.55)[0], tr(e1, 0.55)[1] + 20, sb(I('e'), '1'), 'b') + T(tr(e1, 2)[0] + 4, tr(e1, 2)[1] - 10, '2' + sb(I('e'), '1'), 'b', 'start')
    + A(...O, ...tr(e2, 1), 'r') + A(...O, ...tr(e2, 0.5), 'r thick') + T(tr(e2, 1)[0] - 8, tr(e2, 1)[1], sb(I('e'), '2'), 'r', 'end') + T(tr(e2, 0.5)[0] + 10, tr(e2, 0.5)[1] + 2, '½' + sb(I('e'), '2'), 'r', 'start') + dot(...O);
})(), 'Vecteurs propres')],

'm2-euclidiens-1': ['Théorème spectral : une matrice symétrique réelle est diagonalisable dans une base orthonormée. Ici la courbe d’équation ᵗX S X = 1 est une ellipse dont les axes sont dirigés par les vecteurs propres orthogonaux de S', svg(380, 260, `
  ${A(20, 130, 360, 130, 'soft')}${A(190, 250, 190, 10, 'soft')}
  <ellipse cx="190" cy="130" rx="130" ry="60" transform="rotate(-30 190 130)" class="s b fillA"/>
  ${A(190, 130, ...pol(190, 130, 130, 30), 'r')}${A(190, 130, ...pol(190, 130, 60, 120), 'r')}${T(...pol(190, 130, 146, 30), sb(I('v'), '1'), 'r')}${T(...pol(190, 130, 76, 120), sb(I('v'), '2'), 'r')}
  ${P(`M${pol(190, 130, 14, 30).join(',')} L${pol(190, 130, 19.8, 75).join(',')} L${pol(190, 130, 14, 120).join(',')}`, 'soft')}`, 'Théorème spectral')],

'm2-topologie-1': ['Boules unités fermées de ℝ² pour les normes ‖·‖₁ (losange), ‖·‖₂ (disque) et ‖·‖∞ (carré) ; en dimension finie toutes les normes sont équivalentes : ‖x‖∞ ≤ ‖x‖₂ ≤ ‖x‖₁ ≤ 2‖x‖∞', svg(320, 300, `
  ${A(20, 150, 300, 150, 'soft')}${A(160, 290, 160, 10, 'soft')}
  ${R(60, 50, 200, 200, 'r')}${C(160, 150, 100, 'b')}${P('M160,50 L260,150 L160,250 L60,150 Z', 'thick')}
  ${T(266, 44, '‖·‖∞', 'r', 'start')}${T(...pol(160, 150, 106, 50), '‖·‖₂', 'b', 'start')}${T(118, 104, '‖·‖₁', '', 'end')}${T(268, 166, '1', '', 'start')}${T(166, 44, '1', '', 'start')}`, 'Boules unités')],

'm2-suites-fonctions-1': ['fₙ(x) = xⁿ sur [0, 1] converge simplement vers la fonction nulle sur [0, 1[ et valant 1 en 1 : la limite n’est pas continue, la convergence n’est donc pas uniforme', svg(380, 250, (() => {
  const [X, Y] = rep(50, 210, 280 / 1.05);
  let s = axes(50, 210, 320, 0, 195, 0, I('x'), '');
  [1, 2, 4, 8, 16, 40].forEach((n, k) => { s += chemin(pts(x => x ** n, 0, 1, 120, X, x => r2(210 - x * 180)), k === 5 ? 'r' : 'b'); });
  return s + L(50, 30, X(1), 30, 'dash soft') + L(X(1), 30, X(1), 210, 'dash soft') + T(X(1), 226, '1') + T(44, 34, '1', '', 'end') + T(X(0.55), 196, 'limite : 0', 'nt') + dot(X(1), 30, 'r') + T(X(0.92), 60, sb(I('f'), I('n')), 'b', 'end');
})(), 'Convergence simple')],

'm2-suites-fonctions-2': ['Convergence uniforme : à partir d’un certain rang, le graphe de fₙ reste dans la bande de largeur ε autour du graphe de f, sur tout l’intervalle : sup |fₙ − f| → 0', svg(380, 240, (() => {
  const f = x => 1.5 + 0.6 * Math.sin(1.2 * x), [X, Y] = rep(40, 210, 55);
  return axes(40, 210, 330, 0, 195, 0, I('x'), '') + chemin(pts(x => f(x) + 0.35, 0, 5.8, 120, X, Y), 'r dash') + chemin(pts(x => f(x) - 0.35, 0, 5.8, 120, X, Y), 'r dash')
    + chemin(pts(f, 0, 5.8, 120, X, Y), 'r') + chemin(pts(x => f(x) + 0.22 * Math.sin(5 * x), 0, 5.8, 200, X, Y), 'b') + T(X(5.8), Y(f(5.8) + 0.35) - 6, I('f') + ' + ' + I('ε'), 'r', 'end') + T(X(1.1), Y(f(1.1) + 0.65), sb(I('f'), I('n')), 'b');
})(), 'Convergence uniforme')],

'm2-series-entieres-1': ['Rayon de convergence R : Σ aₙzⁿ converge absolument pour |z| &lt; R et diverge grossièrement pour |z| > R ; sur le cercle |z| = R, tout peut arriver', svg(320, 280, `
  ${A(20, 140, 300, 140, 'soft')}${A(160, 270, 160, 10, 'soft')}
  ${C(160, 140, 95, 'b fillA')}${L(160, 140, ...pol(160, 140, 95, 30), 'b')}${T(...pol(160, 140, 56, 42), I('R'), 'b')}
  ${T(160, 175, 'convergence', 'b')}${T(160, 191, 'absolue', 'b')}${T(270, 40, 'divergence', 'r', 'end')}${T(270, 56, 'grossière', 'r', 'end')}${T(260, 250, '|' + I('z') + '| = ' + I('R') + ' : ?', 'nt', 'end')}`, 'Disque de convergence')],

'm2-integration-1': ['Intégrales de Riemann : ∫₀¹ dx/x^α converge si et seulement si α &lt; 1 ; ∫₁^{+∞} dx/x^α converge si et seulement si α > 1 (ici α = 1/2 et α = 2)', svg(400, 250, (() => {
  const [X, Y] = rep(50, 220, 60);
  return axes(50, 220, 340, 0, 205, 0, I('x'), '') + chemin(pts(x => 1 / Math.sqrt(x), 0.075, 5.6, 200, X, Y), 'b') + chemin(pts(x => 1 / (x * x), 0.29, 5.6, 200, X, Y), 'r')
    + L(X(1), 216, X(1), 224) + T(X(1), 238, '1') + T(X(5.4), Y(1 / Math.sqrt(5.4)) - 8, '1/√' + I('x'), 'b', 'end') + T(X(0.6), Y(3), '1/' + I('x') + '²', 'r', 'start')
    + T(X(3.3), Y(2.8), 'en 0 : converge pour 1/√' + I('x'), 'nt') + T(X(3.3), Y(2.5), 'en +∞ : converge pour 1/' + I('x') + '²', 'nt');
})(), 'Intégrales de Riemann')],

'm2-probas-1': ['Lois usuelles : géométrique 𝒢(p), P(X = k) = (1 − p)^{k−1} p pour k ≥ 1 (rang du premier succès) ; Poisson 𝒫(λ), P(X = k) = e^{−λ} λᵏ/k! (ici p = 0,3 et λ = 3)', svg(440, 220, (() => {
  let s = axes(20, 190, 190, 0, 170, 0, I('k'), '') + axes(240, 190, 190, 0, 170, 0, I('k'), '');
  for (let k = 1; k <= 9; k++) { const p = 0.7 ** (k - 1) * 0.3; s += R(20 + k * 19 - 6, r2(190 - p * 480), 12, r2(p * 480), 'fillA b'); }
  let f = 1; for (let k = 0; k <= 9; k++) { if (k) f *= k; const p = Math.exp(-3) * 3 ** k / f; s += R(240 + k * 19 + 6, r2(190 - p * 480), 12, r2(p * 480), 'fillR r'); }
  return s + T(115, 30, 'géométrique', 'b') + T(335, 30, 'Poisson', 'r') + [1, 5, 9].map(k => T(20 + k * 19, 206, String(k), 'nt')).join('') + [0, 3, 6, 9].map(k => T(240 + k * 19 + 12, 206, String(k), 'nt')).join('');
})(), 'Lois usuelles')],

'm2-differentiel-1': ['Lignes de niveau de f(x, y) = x² + 2y² (ellipses) : en chaque point, le gradient est orthogonal à la ligne de niveau et dirigé vers les valeurs croissantes de f', svg(380, 260, (() => {
  let s = A(20, 130, 360, 130, 'soft') + A(190, 250, 190, 10, 'soft');
  [0.5, 1, 1.5, 2].forEach(c => { s += `<ellipse cx="190" cy="130" rx="${r2(70 * c)}" ry="${r2(70 * c / Math.SQRT2)}" class="s b"/>`; });
  const t = rad(40), x = Math.cos(t) * 105, y = Math.sin(t) * 105 / Math.SQRT2, gx = 2 * x, gy = 4 * y, n = Math.hypot(gx, gy);
  const P0 = [r2(190 + x), r2(130 - y)];
  return s + dot(...P0, 'r') + A(...P0, r2(P0[0] + gx / n * 55), r2(P0[1] - gy / n * 55), 'r') + T(r2(P0[0] + gx / n * 62), r2(P0[1] - gy / n * 62), '∇' + I('f'), 'r', 'start')
    + L(r2(P0[0] - gy / n * 40), r2(P0[1] - gx / n * 40), r2(P0[0] + gy / n * 40), r2(P0[1] + gx / n * 40), 'dash soft') + T(330, 245, I('f') + ' = cste', 'b', 'end');
})(), 'Gradient')],
};
