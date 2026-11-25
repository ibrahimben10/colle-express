// Schémas des fiches de cours — Physique MPSI, partie 4 : Thermodynamique.
import { svg, L, A, D, T, I, V, C, R, P, dot, sb } from './figkit.js';
import { axes, courbe } from './fiches-kit.js';

const r2 = n => Math.round(n * 100) / 100;
const pth = pts => 'M' + pts.map(p => p.map(r2).join(',')).join(' L');
// flèche de sens au milieu d'une liste de points
const fl = (pts, c = '') => { const k = Math.floor(pts.length / 2), a = pts[k - 1], b = pts[k + 1]; return A(r2(a[0]), r2(a[1]), r2(b[0]), r2(b[1]), c); };
// cycle de Carnot ou isotherme/adiabatique dans (P, V) : P en unités arbitraires
const iso = (k, v1, v2, n = 60) => Array.from({length: n + 1}, (_, i) => { const v = v1 + (v2 - v1) * i / n; return [v, k / v]; });
const adia = (k, g, v1, v2, n = 60) => Array.from({length: n + 1}, (_, i) => { const v = v1 + (v2 - v1) * i / n; return [v, k / v ** g]; });

function machine(ox, rec) {   // schéma de principe d'une machine ditherme ; rec = récepteur (frigo/pompe)
  return `${R(ox + 40, 20, 140, 34, 'fillR', 8)}${T(ox + 110, 42, 'source chaude ' + sb(I('T'), 'c'))}
  ${C(ox + 110, 120, 34, 'fillA')}${T(ox + 110, 125, 'machine')}
  ${R(ox + 40, 186, 140, 34, 'fillA', 8)}${T(ox + 110, 208, 'source froide ' + sb(I('T'), 'f'))}
  ${rec ? A(ox + 110, 86, ox + 110, 56, 'r') + A(ox + 110, 186, ox + 110, 156, 'b') + A(ox + 10, 120, ox + 74, 120, '')
        : A(ox + 110, 56, ox + 110, 86, 'r') + A(ox + 110, 156, ox + 110, 186, 'b') + A(ox + 146, 120, ox + 210, 120, '')}
  ${T(ox + 118, 74, sb(I('Q'), 'c'), 'r', 'start')}${T(ox + 118, 176, sb(I('Q'), 'f'), 'b', 'start')}${T(rec ? ox + 30 : ox + 190, 112, '|' + I('W') + '|', '', 'middle')}`;
}

export const FIGS = {
'p4-equilibre-1': ['Diagramme (P, T) d’un corps pur : point triple, point critique ; pour l’eau, la courbe de fusion a une pente négative', svg(380, 240, (() => {
  const X0 = 40, Y0 = 210, Tt = [130, 150], Cc = [300, 50];
  const vap = Array.from({length: 41}, (_, i) => { const t = i / 40; return [Tt[0] + (Cc[0] - Tt[0]) * t, Tt[1] - (Tt[1] - Cc[1]) * (t ** 1.6)]; });
  const sub = Array.from({length: 41}, (_, i) => { const t = i / 40; return [X0 + 10 + (Tt[0] - X0 - 10) * t, Y0 - 5 - (Y0 - 5 - Tt[1]) * t ** 2.2]; });
  return `${axes(X0, Y0, 330, 0, 200, 0, I('T'), I('P'))}<path d="${pth(vap)}" class="s b"/><path d="${pth(sub)}" class="s b"/>
  ${L(Tt[0], Tt[1], Tt[0] + 22, 20, 'b')}${L(Tt[0], Tt[1], Tt[0] - 14, 20, 'r dash')}
  ${dot(...Tt)}${T(Tt[0] + 10, Tt[1] + 18, 'point triple', 'nt', 'start')}${dot(...Cc)}${T(Cc[0] - 6, Cc[1] - 10, 'point critique', 'nt', 'end')}
  ${T(80, 70, 'solide')}${T(220, 60, 'liquide')}${T(250, 170, 'vapeur')}${T(92, 30, 'eau', 'r', 'end')}`;
})(), 'Diagramme (P,T)')],

'p4-equilibre-2': ['Diagramme de Clapeyron (P, v) : courbe de saturation, isothermes et palier de changement d’état ; titre en vapeur x = LM/LV', svg(400, 250, (() => {
  const X0 = 40, Y0 = 220, cx = 150, top = 50;
  const bell = Array.from({length: 81}, (_, i) => { const u = -1 + 2 * i / 80; const x = u < 0 ? cx + 90 * u * 0.9 : cx + 200 * u; return [x, top + (Y0 - top - 10) * (u * u) ** 0.8]; });
  const yP = 150, xs = bell.filter(p => Math.abs(p[1] - yP) < 4).map(p => p[0]), xl = Math.min(...xs), xv = Math.max(...xs);
  const lq = Array.from({length: 20}, (_, i) => [xl - 22 + 22 * i / 19, yP - 60 * (1 - i / 19) ** 2]);
  const vp = Array.from({length: 40}, (_, i) => { const x = xv + (370 - xv) * i / 39; return [x, yP + (Y0 - 20 - yP) * (1 - Math.exp(-(x - xv) / 80))]; });
  const hot = Array.from({length: 60}, (_, i) => { const x = 75 + 295 * i / 59; return [x, 20 + 3000 / (x - 30)]; });
  const xm = xl + 0.62 * (xv - xl);
  return `${axes(X0, Y0, 350, 0, 205, 0, I('v'), I('P'))}<path d="${pth(bell)}" class="s b"/><path d="${pth(lq)}" class="s"/>${L(xl, yP, xv, yP)}<path d="${pth(vp)}" class="s"/>
  <path d="${pth(hot)}" class="s soft"/>${dot(cx, top)}${T(cx - 8, top - 4, 'point critique', 'nt', 'end')}
  ${dot(xl, yP)}${dot(xv, yP)}${dot(xm, yP)}${T(xl - 4, yP + 16, I('L'), '', 'end')}${T(xv + 4, yP + 16, I('V'), '', 'start')}${T(xm, yP - 8, I('M'))}
  ${T(70, 200, 'liquide', 'nt')}${T((xl + xv) / 2, yP + 34, 'liquide + vapeur', 'nt')}${T(330, 120, 'vapeur', 'nt')}${T(360, 46, I('T') + ' > ' + sb(I('T'), 'C'), 'nt', 'end')}`;
})(), 'Diagramme de Clapeyron')],

'p4-energie-1': ['Diagramme de Watt : pour une transformation quasi statique, |W| est l’aire sous la courbe ; W = −∫P dV', svg(380, 220, (() => {
  const X0 = 40, Y0 = 190, pts = iso(9000, 70, 300).map(([v, p]) => [X0 + v, Y0 - p * 0.9 + 10]);
  return `${axes(X0, Y0, 330, 0, 175, 0, I('V'), I('P'))}<path d="${pth(pts)} L${r2(pts.at(-1)[0])},${Y0} L${r2(pts[0][0])},${Y0} Z" class="fillA"/><path d="${pth(pts)}" class="s b"/>${fl(pts, 'b')}
  ${dot(...pts[0])}${dot(...pts.at(-1))}${T(pts[0][0] - 6, pts[0][1] - 4, I('A'), '', 'end')}${T(pts.at(-1)[0] + 6, pts.at(-1)[1] - 4, I('B'), '', 'start')}
  ${T(230, 182, '|' + I('W') + '| = aire', 'b')}${T(330, 40, 'détente : ' + I('W') + ' &lt; 0', 'nt', 'end')}`;
})(), 'Diagramme de Watt')],

'p4-energie-2': ['Cycle moteur (parcouru dans le sens horaire, W < 0) et cycle récepteur (sens trigonométrique, W > 0)', svg(440, 200, (() => {
  const cyc = (ox, cw) => { const c = [ox + 100, 95], pts = Array.from({length: 41}, (_, i) => { const a = 2 * Math.PI * i / 40 * (cw ? -1 : 1); return [c[0] + 70 * Math.cos(a) + 15 * Math.sin(2 * a), c[1] - 45 * Math.sin(a)]; });
    return `${axes(ox + 10, 170, 190, 0, 155, 0, I('V'), I('P'))}<path d="${pth(pts)} Z" class="s fillA"/>${A(...pts[9].map(r2), ...pts[11].map(r2), 'b')}${A(...pts[29].map(r2), ...pts[31].map(r2), 'b')}`; };
  return `${cyc(0, true)}${T(110, 190, 'moteur : ' + I('W') + ' &lt; 0', 'nt')}${cyc(220, false)}${T(330, 190, 'récepteur : ' + I('W') + ' > 0', 'nt')}`;
})(), 'Cycles')],

'p4-premier-1': ['Détente de Joule-Gay-Lussac : parois rigides et calorifugées, ouverture du robinet ; W = 0, Q = 0 donc ΔU = 0', svg(380, 190, `
  ${R(40, 40, 300, 110, 'hatch')}${R(52, 52, 276, 86, 'fillW')}${R(52, 52, 138, 86, 'fillA')}${L(190, 52, 190, 138, 'thick')}
  ${R(184, 86, 12, 18, 'fillW')}${L(184, 95, 196, 95)}${T(190, 32, 'robinet', 'nt')}${L(190, 38, 190, 84, 'dash soft')}
  ${T(121, 100, 'gaz')}${T(259, 100, 'vide')}${T(190, 176, 'parois rigides et calorifugées', 'nt')}`, 'Joule-Gay-Lussac')],

'p4-premier-2': ['Calorimètre : vase isolé (vase Dewar), couvercle, thermomètre et agitateur', svg(320, 230, `
  ${P('M70,50 L70,200 Q70,214 84,214 L236,214 Q250,214 250,200 L250,50', 'thick')}${P('M84,58 L84,192 Q84,200 92,200 L228,200 Q236,200 236,192 L236,58')}
  ${R(60, 40, 200, 12, 'fillW')}<rect x="85" y="110" width="150" height="89" class="fillA"/>${L(85, 110, 235, 110, 'b')}
  ${R(120, 10, 8, 160, 'fillW')}${C(124, 172, 7, 'fillR')}${T(132, 20, 'thermomètre', 'nt', 'start')}
  ${L(200, 6, 200, 170)}${L(184, 170, 216, 170, 'thick')}${T(208, 22, 'agitateur', 'nt', 'start')}${T(160, 150, 'eau', 'b')}`, 'Calorimètre')],

'p4-second-1': ['Cycle de Carnot dans le diagramme (T, S) : un rectangle ; l’aire est égale au travail fourni |W|', svg(380, 220, `
  ${axes(40, 190, 330, 0, 175, 0, I('S'), I('T'))}<rect x="100" y="50" width="200" height="100" class="s fillA"/>
  ${A(180, 50, 220, 50, 'r')}${A(300, 90, 300, 110, '')}${A(220, 150, 180, 150, 'b')}${A(100, 110, 100, 90, '')}
  ${L(40, 50, 100, 50, 'dash soft')}${L(40, 150, 100, 150, 'dash soft')}${T(34, 54, sb(I('T'), 'c'), '', 'end')}${T(34, 154, sb(I('T'), 'f'), '', 'end')}
  ${T(200, 42, 'isotherme ' + sb(I('T'), 'c') + ' : ' + sb(I('Q'), 'c') + ' reçu', 'nt')}${T(200, 168, 'isotherme ' + sb(I('T'), 'f'), 'nt')}${T(308, 104, 'adiabatique réversible', 'nt', 'start')}${T(200, 104, '|' + I('W') + '|', 'b')}`, 'Cycle (T,S)')],

'p4-machines-1': ['Moteur ditherme : reçoit Q_c > 0 de la source chaude, cède Q_f < 0 à la source froide, fournit W < 0', svg(260, 230, machine(10, false), 'Moteur ditherme')],

'p4-machines-2': ['Réfrigérateur ou pompe à chaleur : reçoit W > 0, prend Q_f > 0 à la source froide, cède Q_c < 0 à la source chaude', svg(260, 230, machine(30, true), 'Récepteur ditherme')],

'p4-machines-3': ['Cycle de Carnot dans le diagramme (P, V) : deux isothermes et deux adiabatiques réversibles', svg(380, 230, (() => {
  const g = 1.4, X0 = 40, Y0 = 200, sx = 1, sy = 1;
  const Tc = 16000, Tf = 10000;                      // P·V = cste sur les isothermes (unités arbitraires)
  const v1 = 40, v2 = 80, k1 = Tc * v2 ** (g - 1), v3 = (k1 / Tf) ** (1 / (g - 1)), k2 = Tc * v1 ** (g - 1), v4 = (k2 / Tf) ** (1 / (g - 1));
  const tr = q => q.map(([v, p]) => [X0 + v * 1.2, Y0 - p * 0.44]);
  const a = tr(iso(Tc, v1, v2)), b = tr(adia(k1 * v2 ** 0 * 1, g, v2, v3).map(([v, p]) => [v, Tc * v2 ** (g - 1) / v ** g])), c = tr(iso(Tf, v3, v4)), d = tr(adia(0, g, v4, v1).map(([v]) => [v, Tc * v1 ** (g - 1) / v ** g]));
  return `${axes(X0, Y0, 330, 0, 185, 0, I('V'), I('P'))}<path d="${pth(a)}" class="s r"/><path d="${pth(b)}" class="s"/><path d="${pth(c)}" class="s b"/><path d="${pth(d)}" class="s"/>
  ${fl(a, 'r')}${fl(b)}${fl(c, 'b')}${fl(d)}${['1', '2', '3', '4'].map((t, k) => { const p = [a[0], b[0], c[0], d[0]][k]; return dot(...p.map(r2)) + T(p[0] + (k > 1 ? 6 : -6), p[1] - 6, t, '', k > 1 ? 'start' : 'end'); }).join('')}
  ${T(a[30][0] + 8, a[30][1] - 6, 'isotherme ' + sb(I('T'), 'c'), 'r', 'start')}${T(c[30][0] - 6, c[30][1] + 18, 'isotherme ' + sb(I('T'), 'f'), 'b', 'end')}`;
})(), 'Cycle de Carnot')],

'p4-machines-4': ['Cycle de Beau de Rochas (moteur à essence) : compression et détente adiabatiques, combustion et échappement isochores', svg(380, 230, (() => {
  const g = 1.4, X0 = 40, Y0 = 205, V1 = 240, V2 = 60, P1 = 16;
  const P2 = P1 * (V1 / V2) ** g, P3 = P2 * 1.9, P4 = P3 * (V2 / V1) ** g;
  const tr = q => q.map(([v, p]) => [X0 + 20 + v * 1.2, Y0 - p * 0.86]);
  const c12 = tr(Array.from({length: 61}, (_, i) => { const v = V1 + (V2 - V1) * i / 60; return [v, P1 * (V1 / v) ** g]; }));
  const c34 = tr(Array.from({length: 61}, (_, i) => { const v = V2 + (V1 - V2) * i / 60; return [v, P3 * (V2 / v) ** g]; }));
  const p = (v, pp) => tr([[v, pp]])[0];
  return `${axes(X0, Y0, 330, 0, 195, 0, I('V'), I('P'))}<path d="${pth(c12)}" class="s"/><path d="${pth(c34)}" class="s"/>${L(...p(V2, P2), ...p(V2, P3), 'r')}${L(...p(V1, P4), ...p(V1, P1), 'b')}
  ${fl(c12)}${fl(c34)}${A(...p(V2, P2 * 1.35), ...p(V2, P2 * 1.6), 'r')}${A(...p(V1, P4 * 0.85), ...p(V1, P4 * 0.7), 'b')}
  ${[[V1, P1, '1', 6, 16], [V2, P2, '2', -6, 4], [V2, P3, '3', -6, 4], [V1, P4, '4', 6, 0]].map(([v, pp, t, dx, dy]) => { const q = p(v, pp); return dot(...q) + T(q[0] + dx, q[1] + dy, t, '', dx > 0 ? 'start' : 'end'); }).join('')}
  ${T(p(V2, P3)[0] + 8, p(V2, (P2 + P3) / 2)[1], 'combustion', 'r', 'start')}${T(p(V1, P4)[0] - 40, p(V1, P4)[1] - 30, 'échappement', 'b', 'middle')}
  ${L(...p(V2, 0), ...p(V2, P2), 'dash soft')}${T(p(V2, 0)[0], Y0 + 16, sb(I('V'), 'min'))}${T(p(V1, 0)[0], Y0 + 16, sb(I('V'), 'max'))}`;
})(), 'Beau de Rochas')],
};
