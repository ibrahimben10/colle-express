// Schémas des fiches de cours — Physique MPSI, parties 2 et 3 : Mécanique.
import { svg, L, A, D, T, I, V, C, R, P, dot, spring, ground, wallV, sb, ox, ot } from './figkit.js';
import { axes, courbe } from './fiches-kit.js';

const r2 = n => Math.round(n * 100) / 100;
const arc = (cx, cy, r, a1, a2, c = '') => {     // angles en degrés, sens trigonométrique écran (y vers le haut)
  const p = a => [r2(cx + r * Math.cos(a * Math.PI / 180)), r2(cy - r * Math.sin(a * Math.PI / 180))];
  const [x1, y1] = p(a1), [x2, y2] = p(a2), big = Math.abs(a2 - a1) > 180 ? 1 : 0, sw = a2 > a1 ? 0 : 1;
  return `<path d="M${x1},${y1} A${r},${r} 0 ${big} ${sw} ${x2},${y2}" class="s ${c}"/>`;
};
// projection oblique simple pour les trièdres : x vers le bas-gauche, y vers la droite, z vers le haut
const prj = (ox0, oy0) => (x, y, z) => [r2(ox0 + y - 0.5 * x), r2(oy0 - z + 0.35 * x)];

export const FIGS = {
// ---------------- Cinématique
'p2-cinematique-1': ['Base cartésienne (u_x, u_y, u_z), fixe : OM = x u_x + y u_y + z u_z', svg(360, 230, (() => {
  const p = prj(150, 150), O = p(0, 0, 0), M = p(80, 120, 90), Hm = p(80, 120, 0);
  const ax = (q, t) => { const e = p(...q); return A(O[0], O[1], e[0], e[1], 'soft') + T(e[0] + (q[1] ? 10 : -8), e[1] + (q[0] ? 12 : 0), t); };
  return `${ax([150, 0, 0], I('x'))}${ax([0, 180, 0], I('y'))}${ax([0, 0, 130], I('z'))}
  ${A(O[0], O[1], M[0], M[1], 'b')}${dot(...M)}${T(M[0] + 8, M[1] - 6, I('M'), '', 'start')}${T(O[0] - 8, O[1] + 6, I('O'), '', 'end')}
  ${L(M[0], M[1], Hm[0], Hm[1], 'dash soft')}${L(Hm[0], Hm[1], ...p(80, 0, 0), 'dash soft')}${L(Hm[0], Hm[1], ...p(0, 120, 0), 'dash soft')}
  ${A(O[0], O[1], ...p(0, 32, 0), 'r')}${A(O[0], O[1], ...p(0, 0, 32), 'r')}${A(O[0], O[1], ...p(40, 0, 0), 'r')}
  ${T(...p(0, 34, -12), sb(V('u'), I('y')), 'r', 'start')}${T(...p(0, 6, 36), sb(V('u'), I('z')), 'r', 'start')}${T(...p(44, -14, 0), sb(V('u'), I('x')), 'r', 'end')}`;
})(), 'Base cartésienne')],

'p2-cinematique-2': ['Base polaire (u_r, u_θ), liée au point M : OM = r u_r', svg(360, 230, (() => {
  const Ox = 70, Oy = 190, r = 170, t = 38 * Math.PI / 180, Mx = Ox + r * Math.cos(t), My = Oy - r * Math.sin(t);
  const ur = [Math.cos(t), -Math.sin(t)], ut = [-Math.sin(t), -Math.cos(t)];
  return `${A(Ox - 10, Oy, 340, Oy, 'soft')}${T(340, Oy + 18, I('x'), '', 'end')}${A(Ox, Oy + 10, Ox, 20, 'soft')}${T(Ox + 8, 26, I('y'), '', 'start')}
  ${L(Ox, Oy, Mx, My, 'b')}${dot(Mx, My)}${T(Mx + 6, My - 10, I('M'), '', 'start')}${T(Ox - 8, Oy + 14, I('O'), '', 'end')}${T((Ox + Mx) / 2 - 4, (Oy + My) / 2 - 8, I('r'), 'b', 'end')}
  ${arc(Ox, Oy, 46, 0, 38)}${T(Ox + 54, Oy - 14, 'θ', '', 'start')}
  ${A(Mx, My, Mx + 50 * ur[0], My + 50 * ur[1], 'r')}${T(Mx + 56 * ur[0] + 4, My + 56 * ur[1], sb(V('u'), I('r')), 'r', 'start')}
  ${A(Mx, My, Mx + 50 * ut[0], My + 50 * ut[1], 'r')}${T(Mx + 56 * ut[0] - 4, My + 56 * ut[1], sb(V('u'), 'θ'), 'r', 'end')}`;
})(), 'Base polaire')],

'p2-cinematique-3': ['Base cylindrique (u_r, u_θ, u_z) : OM = r u_r + z u_z, H projeté de M dans le plan (Oxy)', svg(380, 240, (() => {
  const p = prj(150, 175), O = p(0, 0, 0), th = 50 * Math.PI / 180, rr = 140, zz = 110;
  const c = Math.cos(th), sn = Math.sin(th), Hq = [rr * c, rr * sn, 0], Mq = [rr * c, rr * sn, zz];
  const H = p(...Hq), M = p(...Mq), vec = (q, d, k = 45) => p(q[0] + k * d[0], q[1] + k * d[1], q[2] + k * d[2]);
  const er = [c, sn, 0], et = [-sn, c, 0], ez = [0, 0, 1];
  const fl = (d, lab, dx, dy) => { const e = vec(Mq, d); return A(...M, ...e, 'r') + T(e[0] + dx, e[1] + dy, lab, 'r', 'middle'); };
  return `${A(...O, ...p(150, 0, 0), 'soft')}${T(...p(162, -6, 0), I('x'))}${A(...O, ...p(0, 210, 0), 'soft')}${T(...p(0, 220, 0), I('y'))}${A(...O, ...p(0, 0, 160), 'soft')}${T(...p(0, 10, 165), I('z'))}
  ${L(...O, ...H, 'dash soft')}${L(...H, ...M, 'dash soft')}${L(...O, ...M, 'b')}${dot(...M)}${dot(...H)}${T(M[0] - 10, M[1] - 6, I('M'), '', 'end')}${T(H[0] + 8, H[1] + 14, I('H'), '', 'start')}
  ${T((O[0] + H[0]) / 2 - 4, (O[1] + H[1]) / 2 + 16, I('r'))}${T(H[0] - 8, (H[1] + M[1]) / 2 + 20, I('z'), '', 'end')}${T(...p(34, 22, 0), 'θ')}
  ${fl(er, sb(V('u'), I('r')), 12, 4)}${fl(et, sb(V('u'), 'θ'), 14, -4)}${fl(ez, sb(V('u'), I('z')), 16, 0)}`;
})(), 'Base cylindrique')],

'p2-cinematique-4': ['Base sphérique (u_r, u_θ, u_φ) : θ angle depuis Oz, φ angle dans le plan (Oxy) depuis Ox', svg(380, 250, (() => {
  const p = prj(150, 185), O = p(0, 0, 0), R0 = 160, th = 48 * Math.PI / 180, ph = 55 * Math.PI / 180;
  const er = [Math.sin(th) * Math.cos(ph), Math.sin(th) * Math.sin(ph), Math.cos(th)], et = [Math.cos(th) * Math.cos(ph), Math.cos(th) * Math.sin(ph), -Math.sin(th)], ep = [-Math.sin(ph), Math.cos(ph), 0];
  const Mq = er.map(v => R0 * v), Hq = [Mq[0], Mq[1], 0], M = p(...Mq), H = p(...Hq), vec = (d, k = 45) => p(Mq[0] + k * d[0], Mq[1] + k * d[1], Mq[2] + k * d[2]);
  const fl = (d, lab, dx, dy) => { const e = vec(d); return A(...M, ...e, 'r') + T(e[0] + dx, e[1] + dy, lab, 'r', 'middle'); };
  return `${A(...O, ...p(150, 0, 0), 'soft')}${T(...p(162, -6, 0), I('x'))}${A(...O, ...p(0, 200, 0), 'soft')}${T(...p(0, 210, 0), I('y'))}${A(...O, ...p(0, 0, 175), 'soft')}${T(...p(0, 10, 180), I('z'))}
  ${L(...O, ...M, 'b')}${L(...M, ...H, 'dash soft')}${L(...O, ...H, 'dash soft')}${dot(...M)}${T(M[0] - 10, M[1] - 8, I('M'), '', 'end')}${T((O[0] + M[0]) / 2 - 8, (O[1] + M[1]) / 2, I('r'), 'b', 'end')}
  ${T(...p(0, 14, 48), 'θ')}${T(...p(30, 26, 0), 'φ')}
  ${fl(er, sb(V('u'), I('r')), 12, 4)}${fl(et, sb(V('u'), 'θ'), 14, 8)}${fl(ep, sb(V('u'), 'φ'), 14, -4)}`;
})(), 'Base sphérique')],

'p2-cinematique-5': ['Mouvement circulaire de rayon R : vitesse tangente, accélération = tangentielle dv/dt + normale v²/R vers le centre', svg(360, 240, `
  ${C(160, 125, 95)}${dot(160, 125)}${T(150, 140, I('O'), '', 'end')}
  ${L(160, 125, 227, 58, 'dash soft')}${T(186, 84, I('R'), '', 'end')}${dot(227, 58)}${T(234, 52, I('M'), '', 'start')}
  ${A(227, 58, 287, 118, 'b')}${T(292, 124, V('v'), 'b', 'start')}
  ${A(227, 58, 197, 88, 'r')}${T(200, 108, sb(V('a'), I('n')), 'r', 'end')}${A(227, 58, 257, 88, 'r dash')}${T(262, 82, sb(V('a'), I('t')), 'r', 'start')}
  ${T(330, 200, sb(I('a'), I('n')) + ' = ' + I('v') + '²/' + I('R'), 'nt', 'end')}${T(330, 218, sb(I('a'), I('t')) + ' = d' + I('v') + '/d' + I('t'), 'nt', 'end')}`, 'Mouvement circulaire')],

'p2-solide-1': ['Solide en translation (tous les points ont la même vitesse) et en rotation autour d’un axe fixe (v = rω)', svg(440, 210, `
  ${R(40, 60, 110, 80, 'fillA')}${[[55, 75], [130, 80], [70, 125], [135, 128]].map(([x, y]) => dot(x, y) + A(x, y, x + 42, y - 22, 'b')).join('')}${T(95, 180, 'translation', 'nt')}
  ${C(320, 100, 70, 'fillA')}${ox(320, 100)}${T(320, 186, 'rotation autour de Δ', 'nt')}${T(332, 92, 'Δ', '', 'start')}
  ${dot(355, 100)}${A(355, 100, 355, 70, 'b')}${dot(385, 100)}${A(385, 100, 385, 40, 'b')}${dot(320, 135)}${A(320, 135, 345, 135, 'b')}
  ${L(320, 100, 385, 100, 'dash soft')}${T(372, 116, I('r'), '', 'middle')}${T(392, 50, I('v') + ' = ' + I('r') + 'ω', 'b', 'start')}`, 'Translation et rotation')],

// ---------------- Dynamique
'p2-dynamique-1': ['Solide glissant vers le bas d’un plan incliné : poids, réaction normale, frottement opposé au glissement (vers le haut de la pente)', svg(400, 230, (() => {
  const a = 28 * Math.PI / 180, c = Math.cos(a), s = Math.sin(a), X0 = 30, Y0 = 200, Lp = 340;
  const at = (u, v) => [r2(X0 + u * c - v * s), r2(Y0 - u * s - v * c)];   // u le long de la pente, v selon la normale
  const G = at(190, 25), q = (u, v) => at(190 + u, 25 + v);
  const blk = [at(160, 0), at(220, 0), at(220, 50), at(160, 50)];
  return `${P(`M${X0},${Y0} L${X0 + Lp * c},${Y0} L${X0 + Lp * c},${r2(Y0 - Lp * s)} Z`, 'fillW')}${ground(X0, Y0, Lp * c + 10)}
  ${P('M' + blk.map(p => p.join(',')).join(' L') + ' Z', 'fillA')}${dot(...G)}${T(G[0] - 6, G[1] + 4, I('G'), '', 'end')}
  ${A(...G, G[0], G[1] + 75, 'r')}${T(G[0] + 6, G[1] + 72, V('P'), 'r', 'start')}
  ${A(...at(190, 0), ...at(190, 75), 'b')}${T(...at(184, 80), sb(V('R'), 'N'), 'b', 'end')}
  ${A(...at(220, 4), ...at(270, 4), 'b')}${T(...at(268, -14), sb(V('R'), 'T'), 'b', 'middle')}
  <path d="M${X0 + 50},${Y0} A50,50 0 0 0 ${r2(X0 + 50 * c)},${r2(Y0 - 50 * s)}" class="s"/>${T(X0 + 58, Y0 - 8, 'α', '', 'start')}`;
})(), 'Plan incliné')],

'p2-dynamique-2': ['Pendule simple : tension du fil vers O, poids, base polaire (u_r vers l’extérieur, u_θ dans le sens de θ)', svg(340, 250, (() => {
  const Ox = 170, Oy = 30, l = 160, t = 30 * Math.PI / 180, Mx = Ox + l * Math.sin(t), My = Oy + l * Math.cos(t);
  return `${R(110, 18, 120, 12, 'hatch')}${L(110, 30, 230, 30)}${dot(Ox, Oy)}${T(Ox - 8, Oy + 16, I('O'), '', 'end')}
  ${L(Ox, Oy, Ox, Oy + l + 20, 'axis')}${L(Ox, Oy, Mx, My)}${C(Mx, My, 10, 'fillA')}${T(Ox + 0.5 * l * Math.sin(t) + 10, Oy + 0.5 * l * Math.cos(t), 'ℓ', '', 'start')}
  <path d="M${Ox},${Oy + 50} A50,50 0 0 0 ${r2(Ox + 50 * Math.sin(t))},${r2(Oy + 50 * Math.cos(t))}" class="s"/>${T(Ox + 12, Oy + 68, 'θ', '', 'start')}
  ${A(Mx, My, Mx - 55 * Math.sin(t), My - 55 * Math.cos(t), 'b')}${T(Mx - 60 * Math.sin(t) - 6, My - 60 * Math.cos(t), V('T'), 'b', 'end')}
  ${A(Mx, My, Mx, My + 60, 'r')}${T(Mx + 6, My + 62, V('P'), 'r', 'start')}
  ${A(Mx, My, Mx + 40 * Math.sin(t), My + 40 * Math.cos(t), 'soft')}${T(Mx + 44 * Math.sin(t) + 6, My + 44 * Math.cos(t) + 6, sb(V('u'), I('r')), '', 'start')}
  ${A(Mx, My, Mx + 40 * Math.cos(t), My - 40 * Math.sin(t), 'soft')}${T(Mx + 44 * Math.cos(t) + 6, My - 44 * Math.sin(t), sb(V('u'), 'θ'), '', 'start')}`;
})(), 'Pendule simple')],

'p2-dynamique-3': ['Chute libre avec vitesse initiale : trajectoire parabolique, portée et flèche', svg(400, 220, (() => {
  const X0 = 40, Y0 = 190, v = 1, a = 50 * Math.PI / 180, Lp = 300, H = Lp / 4 * Math.tan(a);   // y = x tanα − x²·tanα/L
  return `${ground(X0 - 10, Y0, 350)}${A(X0, Y0, X0, 20, 'soft')}${T(X0 + 8, 26, I('z'), '', 'start')}${A(X0, Y0, 380, Y0, 'soft')}${T(380, Y0 + 18, I('x'), '', 'end')}
  ${courbe(x => x * Math.tan(a) - x * x * Math.tan(a) / Lp, 0, Lp, X0, Y0, 1, -1, 120, 'b')}
  ${A(X0, Y0, X0 + 55 * Math.cos(a), Y0 - 55 * Math.sin(a), 'r')}${T(X0 + 58 * Math.cos(a) + 4, Y0 - 58 * Math.sin(a), sb(V('v'), '0'), 'r', 'start')}
  <path d="M${X0 + 30},${Y0} A30,30 0 0 0 ${r2(X0 + 30 * Math.cos(a))},${r2(Y0 - 30 * Math.sin(a))}" class="s"/>${T(X0 + 36, Y0 - 10, 'α', '', 'start')}
  ${L(X0 + Lp / 2, Y0, X0 + Lp / 2, Y0 - H, 'dash soft')}${T(X0 + Lp / 2 + 6, Y0 - H / 2, 'flèche ' + I('h'), 'nt', 'start')}${D(X0, Y0 + 14, X0 + Lp, Y0 + 14, '', 0, 0)}${T(X0 + Lp / 2, Y0 + 28, 'portée ' + I('d'), 'nt')}
  ${A(330, 40, 330, 80, 'soft')}${T(336, 66, V('g'), '', 'start')}`;
})(), 'Projectile')],

'p2-energie-1': ['Travail d’une force le long d’un chemin : δW = F·dl, puis somme de A à B', svg(380, 200, `
  <path d="M40,160 C120,40 220,190 340,60" class="s b"/>${dot(40, 160)}${dot(340, 60)}${T(34, 176, I('A'), '', 'end')}${T(348, 56, I('B'), '', 'start')}
  ${dot(176, 116)}${T(170, 132, I('M'), '', 'end')}${A(176, 116, 214, 124, '')}${T(218, 136, 'd' + V('l'), '', 'start')}
  ${A(176, 116, 230, 70, 'r')}${T(234, 66, V('F'), 'r', 'start')}<path d="M200,121 A26,26 0 0 0 196,99" class="s"/>${T(206, 108, 'α', '', 'start')}
  ${T(330, 180, 'δ' + I('W') + ' = ' + I('F') + ' d' + I('l') + ' cos α', 'nt', 'end')}`, 'Travail')],

'p2-energie-2': ['Énergie potentielle Ep(x) : un minimum est une position d’équilibre stable, un maximum une position instable', svg(400, 220, (() => {
  const X0 = 40, Y0 = 190, f = x => 70 + 45 * Math.sin((x - 20) / 60) + 0.0012 * (x - 160) ** 2;
  const xs = 20 + 60 * (Math.PI * 1.5), xi = 20 + 60 * (Math.PI * 0.5);
  return `${axes(X0, Y0, 340, 10, 170, 0, I('x'), sb(I('E'), 'p'))}${courbe(f, 0, 330, X0, Y0, 1, -1, 300, 'b')}
  ${dot(X0 + xs - 6, Y0 - f(xs - 6))}${T(X0 + xs - 6, Y0 - f(xs - 6) + 20, 'stable')}${dot(X0 + xi + 7, Y0 - f(xi + 7))}${T(X0 + xi + 7, Y0 - f(xi + 7) - 12, 'instable')}
  ${T(330, 30, 'à l’équilibre : d' + sb(I('E'), 'p') + '/d' + I('x') + ' = 0', 'nt', 'end')}`;
})(), 'Énergie potentielle')],

'p2-puits-1': ['Puits de potentiel : le mouvement est confiné entre les points de rebroussement x₁ et x₂ où Ep = Em', svg(400, 220, (() => {
  const X0 = 40, Y0 = 190, f = x => 150 - 120 * Math.exp(-((x - 140) ** 2) / 4200) + (x > 140 ? 0 : 0);
  const Em = 95, xs = []; for (let x = 0; x < 330; x += 0.5) if ((f(x) - Em) * (f(x + 0.5) - Em) < 0) xs.push(x);
  return `${axes(X0, Y0, 340, 10, 170, 0, I('x'), sb(I('E'), 'p'))}<rect x="${X0 + xs[0]}" y="${Y0 - Em}" width="${xs[1] - xs[0]}" height="${Em}" class="fillA"/>
  ${courbe(f, 0, 330, X0, Y0, 1, -1, 300, 'b')}${L(X0, Y0 - Em, X0 + 330, Y0 - Em, 'r')}${T(X0 + 334, Y0 - Em + 4, sb(I('E'), 'm'), 'r', 'start')}
  ${xs.map((x, k) => L(X0 + x, Y0 - Em, X0 + x, Y0, 'dash soft') + T(X0 + x, Y0 + 16, sb(I('x'), String(k + 1)))).join('')}
  ${T(X0 + (xs[0] + xs[1]) / 2, Y0 - 20, 'zone accessible', 'nt')}${T(X0 + 300, Y0 - 160, 'état lié', 'nt', 'end')}`;
})(), 'Puits de potentiel')],

'p2-puits-2': ['Approximation harmonique : au voisinage d’un minimum, Ep ≈ Ep(x₀) + ½ k(x − x₀)² avec k = Ep″(x₀)', svg(400, 220, (() => {
  const X0 = 40, Y0 = 190, x0 = 150, f = x => 40 + 2000 / (x - 20) + 0.004 * (x - 20) ** 2 - 0;
  // minimum numérique
  let xm = 60, fm = f(60); for (let x = 60; x < 330; x += 0.1) if (f(x) < fm) { fm = f(x); xm = x; }
  const h = 0.01, k = (f(xm + h) - 2 * f(xm) + f(xm - h)) / (h * h);
  return `${axes(X0, Y0, 340, 10, 170, 0, I('x'), sb(I('E'), 'p'))}${courbe(f, 40, 330, X0, Y0, 1, -1, 300, 'b')}
  ${courbe(x => fm + 0.5 * k * (x - xm) ** 2, xm - 55, xm + 55, X0, Y0, 1, -1, 80, 'r dash')}${dot(X0 + xm, Y0 - fm)}
  ${L(X0 + xm, Y0 - fm, X0 + xm, Y0, 'dash soft')}${T(X0 + xm, Y0 + 16, sb(I('x'), '0'))}${T(X0 + xm + 60, Y0 - fm - 40, 'parabole osculatrice', 'r', 'start')}`;
})(), 'Approximation harmonique')],

'p2-charge-1': ['Électron entrant entre deux plaques chargées : force −eE vers la plaque positive, trajectoire parabolique', svg(400, 210, `
  ${R(80, 40, 220, 8, 'fill')}${R(80, 162, 220, 8, 'fill')}${T(70, 50, '+', '', 'end')}${T(70, 172, '−', '', 'end')}
  ${[120, 180, 240].map(x => A(x, 56, x, 150, 'soft')).join('')}${T(258, 110, V('E'), '', 'start')}
  ${A(20, 105, 70, 105, 'r')}${T(30, 96, sb(V('v'), '0'), 'r', 'start')}${dot(80, 105)}
  ${courbe(x => 0.0011 * x * x, 0, 220, 80, 105, 1, -1, 80, 'b')}${L(300, 105 - 0.0011 * 220 * 220, 380, 105 - 0.0011 * 220 * 220 - 0.484 * 80, 'b dash')}
  ${T(150, 100, 'e⁻', 'b')}${A(190, 92, 190, 66, 'r')}${T(196, 72, V('F') + ' = −' + I('e') + V('E'), 'r', 'start')}`, 'Déviation électrostatique')],

'p2-charge-2': ['Charge q > 0 dans un champ B uniforme sortant (⊙) : mouvement circulaire uniforme de rayon R = mv/(|q|B), sens horaire', svg(360, 240, `
  ${[[40, 40], [320, 40], [40, 200], [320, 200], [60, 120], [300, 120]].map(([x, y]) => ox(x, y)).join('')}${T(330, 30, V('B'), '', 'start')}
  ${C(180, 120, 80, 'b')}${dot(180, 120)}${T(172, 134, I('C'), '', 'end')}${dot(180, 40)}${T(180, 30, I('q') + ' > 0')}
  ${A(180, 40, 240, 40, 'r')}${T(246, 44, V('v'), 'r', 'start')}${A(180, 40, 180, 80, '')}${T(186, 70, V('F'), '', 'start')}
  ${A(255, 84, 248, 96, 'b')}${L(180, 120, 237, 63, 'dash soft')}${T(214, 104, I('R'), '', 'start')}`, 'Mouvement cyclotron')],

'p2-charge-3': ['Vitesse initiale oblique par rapport à B : hélice d’axe parallèle à B, de pas constant', svg(400, 200, (() => {
  let d = ''; for (let k = 0; k <= 400; k++) { const t = k / 400 * 6 * Math.PI; const x = 50 + 260 * k / 400 + 26 * Math.sin(t), y = 100 - 45 * Math.cos(t); d += (d ? ' L' : 'M') + r2(x) + ',' + r2(y); }
  return `${A(30, 100, 380, 100, 'axis')}${A(310, 170, 370, 170, '')}${T(376, 174, V('B'), '', 'start')}<path d="${d}" class="s b"/>
  ${D(50 + 260 / 3, 34, 50 + 520 / 3, 34, 'pas ' + I('p'), 50 + 130, 26)}${T(30, 186, 'translation uniforme selon ' + V('B') + ' et rotation autour', 'nt', 'start')}`;
})(), 'Hélice')],

// ---------------- Moment cinétique, solide
'p3-moment-1': ['Moment d’une force par rapport à un axe Δ : M_Δ = ±F d, d bras de levier (distance de l’axe à la droite d’action)', svg(360, 220, (() => {
  const O = [110, 150], M = [230, 110], u = [0.95, 0.31], t = (O[0] - M[0]) * u[0] + (O[1] - M[1]) * u[1], H = [M[0] + t * u[0], M[1] + t * u[1]];
  return `${C(...O, 6)}${C(...O, 1.6, 'fill')}${T(O[0] - 10, O[1] + 20, 'Δ', '', 'end')}${T(O[0] + 8, O[1] + 20, I('O'), '', 'start')}
  ${L(M[0] - 200 * u[0], M[1] - 200 * u[1], M[0] + 120 * u[0], M[1] + 120 * u[1], 'dash soft')}${dot(...M)}${T(M[0] - 2, M[1] - 10, I('M'))}
  ${A(...M, M[0] + 80 * u[0], M[1] + 80 * u[1], 'r')}${T(M[0] + 86 * u[0], M[1] + 86 * u[1] + 16, V('F'), 'r')}
  ${L(...O, ...H, 'b')}${T((O[0] + H[0]) / 2 + 8, (O[1] + H[1]) / 2 + 4, I('d'), 'b', 'start')}
  ${P(`M${r2(H[0] + 8 * u[0])},${r2(H[1] + 8 * u[1])} l${r2(-8 * u[1])},${r2(8 * u[0])} l${r2(-8 * u[0])},${r2(-8 * u[1])}`, 'soft')}
  ${T(250, 205, 'droite d’action de ' + V('F'), 'nt')}`;
})(), 'Moment d’une force')],

'p3-moment-2': ['Pendule pesant : solide mobile autour de l’axe horizontal Δ passant par O, G à la distance a', svg(320, 250, (() => {
  const Ox = 160, Oy = 40, a = 120, t = 25 * Math.PI / 180, Gx = Ox + a * Math.sin(t), Gy = Oy + a * Math.cos(t);
  const pts = [[-18, -14], [18, -14], [36, a + 34], [-30, a + 40]].map(([u, v]) => [r2(Ox + u * Math.cos(t) + v * Math.sin(t)), r2(Oy - u * Math.sin(t) + v * Math.cos(t))]);
  return `${P('M' + pts.map(p => p.join(',')).join(' L') + ' Z', 'fillA')}${C(Ox, Oy, 6, 'fillW')}${C(Ox, Oy, 1.6, 'fill')}${T(Ox - 10, Oy - 8, I('O') + ', Δ', '', 'end')}
  ${L(Ox, Oy, Ox, Oy + 190, 'axis')}${L(Ox, Oy, Gx, Gy, 'dash')}${dot(Gx, Gy)}${T(Gx + 8, Gy - 2, I('G'), '', 'start')}${T(Ox + 0.5 * a * Math.sin(t) + 8, Oy + 0.5 * a * Math.cos(t), I('a'), '', 'start')}
  <path d="M${Ox},${Oy + 60} A60,60 0 0 0 ${r2(Ox + 60 * Math.sin(t))},${r2(Oy + 60 * Math.cos(t))}" class="s"/>${T(Ox + 8, Oy + 78, 'θ', '', 'start')}
  ${A(Gx, Gy, Gx, Gy + 60, 'r')}${T(Gx + 6, Gy + 58, V('P') + ' = ' + I('m') + V('g'), 'r', 'start')}`;
})(), 'Pendule pesant')],

'p3-moment-3': ['Couple de forces : deux forces opposées de droites d’action distantes de d ; résultante nulle, moment Γ = F d', svg(360, 200, `
  ${L(60, 100, 300, 100, 'thick')}${dot(180, 100)}${T(180, 120, I('O'))}
  ${A(80, 100, 80, 40, 'r')}${T(86, 46, V('F'), 'r', 'start')}${A(280, 100, 280, 160, 'r')}${T(286, 158, '−' + V('F'), 'r', 'start')}
  ${D(80, 180, 280, 180, I('d'), 180, 176)}${L(80, 100, 80, 186, 'dash soft')}${L(280, 160, 280, 186, 'dash soft')}
  <path d="M150,60 A40,40 0 0 1 210,60" class="s b"/>${A(208, 61, 214, 66, 'b')}${T(180, 46, 'Γ', 'b')}`, 'Couple')],

'p3-central-1': ['Loi des aires : le rayon vecteur balaie des aires égales pendant des durées égales (C = r²θ̇ constante)', svg(380, 240, (() => {
  const a = 140, e = 0.6, b = a * Math.sqrt(1 - e * e), cx = 180, cy = 118, Fx = cx + a * e;
  const pt = E => [r2(cx + a * Math.cos(E)), r2(cy - b * Math.sin(E))];   // E mesuré depuis le périastre (à droite, côté du foyer)
  const sect = (E1, E2) => { let d = `M${Fx},${cy}`; for (let k = 0; k <= 30; k++) { const p = pt(E1 + (E2 - E1) * k / 30); d += ` L${p[0]},${p[1]}`; } return d + ' Z'; };
  // aires égales : l'aire balayée depuis le périgée vaut (ab/2)(E − e sin E)
  const M = E => E - e * Math.sin(E), inv = m => { let E = m; for (let i = 0; i < 30; i++) E -= (E - e * Math.sin(E) - m) / (1 - e * Math.cos(E)); return E; };
  const E1 = -0.45, E2 = inv(M(E1) + 0.7), E3 = Math.PI - 0.3, E4 = inv(M(E3) + 0.7);
  return `<ellipse cx="${cx}" cy="${cy}" rx="${a}" ry="${r2(b)}" class="s"/><path d="${sect(E1, E2)}" class="s fillA"/><path d="${sect(E3, E4)}" class="s fillA"/>
  ${C(Fx, cy, 7, 'fill')}${T(Fx, cy + b + 22, 'foyer : centre attracteur', 'nt')}${L(Fx, cy + 10, Fx, cy + b + 8, 'dash soft')}${T(...pt((E1 + E2) / 2).map((v, i) => i ? v - 8 : v + 14), 'Δ' + I('t'), '', 'start')}${T(...pt((E3 + E4) / 2).map((v, i) => i ? v - 6 : v - 12), 'Δ' + I('t'), '', 'end')}`;
})(), 'Loi des aires')],

'p3-central-2': ['Énergie potentielle effective Ep,eff(r) = mC²/(2r²) − k/r : état lié si Em < 0 (entre r_min et r_max), état de diffusion si Em ≥ 0', svg(400, 240, (() => {
  const X0 = 40, Y0 = 120, f = r => 288000 / (r * r) - 9600 / r, g = r => Math.min(105, f(r));
  const roots = E => { const xs = []; for (let r = 15; r < 330; r += 0.25) if ((f(r) - E) * (f(r + 0.25) - E) < 0) xs.push(r); return xs; };
  const E1 = -40, E2 = 40, r1 = roots(E1), r3 = roots(E2);
  return `${axes(X0, Y0, 330, 10, 110, 100, I('r'), sb(I('E'), 'p,eff'))}${courbe(g, 18, 320, X0, Y0, 1, -1, 400, 'b')}
  ${L(X0, Y0 - E1, X0 + 320, Y0 - E1, 'r')}${T(X0 + 318, Y0 - E1 + 18, sb(I('E'), 'm') + ' &lt; 0 : état lié', 'r', 'end')}
  ${r1.map((r, k) => L(X0 + r, Y0 - E1, X0 + r, Y0, 'dash soft') + T(X0 + r + (k ? 4 : -4), Y0 - 6, sb(I('r'), k ? 'max' : 'min'), '', k ? 'start' : 'end')).join('')}
  ${L(X0 + r3[0], Y0 - E2, X0 + 320, Y0 - E2, '')}${T(X0 + 318, Y0 - E2 - 6, sb(I('E'), 'm') + ' > 0 : diffusion', '', 'end')}${L(X0 + r3[0], Y0 - E2, X0 + r3[0], Y0, 'dash soft')}
  ${dot(X0 + 60, Y0 + 80)}${T(X0 + 70, Y0 + 96, 'minimum : orbite circulaire', 'nt', 'start')}`;
})(), 'Énergie potentielle effective')],

'p3-central-3': ['Trajectoires coniques de foyer O : ellipse (Em < 0), parabole (Em = 0), hyperbole (Em > 0)', svg(400, 240, (() => {
  const Fx = 230, Fy = 120, rp = 40, sc = 1;
  const con = (e, c) => { let d = ''; const tmax = e < 1 ? Math.PI : Math.acos(-1 / e) - 0.06; for (let k = 0; k <= 200; k++) { const t = -tmax + 2 * tmax * k / 200, r = rp * (1 + e) / (1 + e * Math.cos(t)); const x = Fx + r * Math.cos(t), y = Fy - r * Math.sin(t); if (x < 5 || x > 395 || y < 5 || y > 235) { d += ''; continue; } d += (d && !d.endsWith('|') ? ' L' : ' M') + r2(x) + ',' + r2(y); } return `<path d="${d.trim().replace(/^L/, 'M')}" class="s ${c}"/>`; };
  const a = rp / (1 - 0.6), Ax = Fx - a * (1 + 0.6);
  return `${con(0.6, 'b')}${con(1, '')}${con(1.8, 'r')}${C(Fx, Fy, 6, 'fill')}${T(Fx + 4, Fy + 20, I('O'), '', 'start')}
  ${dot(Fx + rp, Fy)}${T(Fx + rp + 6, Fy - 6, 'périgée', 'nt', 'start')}${dot(Ax, Fy)}${T(Ax - 4, Fy - 8, 'apogée', 'nt', 'end')}${L(Ax, Fy, Fx + rp, Fy, 'dash soft')}${T((Ax + Fx + rp) / 2, Fy + 16, '2' + I('a'))}
  ${T(60, 40, 'ellipse', 'b', 'start')}${T(310, 30, 'parabole', '', 'start')}${T(330, 70, 'hyperbole', 'r', 'start')}`;
})(), 'Coniques')],

'p3-central-4': ['Satellite géostationnaire : orbite circulaire dans le plan équatorial, période égale au jour sidéral, altitude ≈ 36 000 km', svg(380, 230, `
  ${C(190, 120, 40, 'fillA')}<ellipse cx="190" cy="120" rx="40" ry="10" class="s soft"/>${L(190, 60, 190, 180, 'axis')}<path d="M175,62 A15,6 0 1 0 205,62" class="s"/>${A(204, 63, 206, 60)}
  <ellipse cx="190" cy="120" rx="165" ry="42" class="s b"/>${dot(355, 120)}${R(348, 112, 14, 16, 'fillW')}${T(340, 150, 'satellite', 'nt', 'end')}
  ${A(355, 120, 352, 85, 'b')}${T(366, 92, V('v'), 'b', 'start')}${T(150, 120, 'Terre', 'nt', 'end')}${T(200, 56, 'axe des pôles', 'nt', 'start')}
  ${D(190, 205, 355, 205, '', 0, 0)}${T(272, 222, I('r') + ' ≈ 42 000 km', '', 'middle')}`, 'Satellite géostationnaire')],
};
