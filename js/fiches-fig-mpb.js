// Schémas des fiches de cours — Physique MP : électromagnétisme.
import { svg, L, A, D, T, I, V, C, R, P, dot, sb, ox, ot } from './figkit.js';
import { axes, courbe } from './fiches-kit.js';

const r2 = n => Math.round(n * 100) / 100;
const rad = d => d * Math.PI / 180;
const pol = (x, y, r, deg) => [r2(x + r * Math.cos(rad(deg))), r2(y - r * Math.sin(rad(deg)))];
const arc = (x, y, r, d1, d2, c = 'soft') => { const [a, b] = pol(x, y, r, d1), [e, f] = pol(x, y, r, d2); return P(`M${a},${b} A${r},${r} 0 ${Math.abs(d2 - d1) > 180 ? 1 : 0} ${d2 > d1 ? 0 : 1} ${e},${f}`, c); };
const pth = pts => 'M' + pts.map(p => p.map(r2).join(',')).join(' L');
const chg = (x, y, s, c = '') => C(x, y, 9, 'fillW ' + c) + T(x, y + 5, s, c);
// ligne de champ d’un dipôle d’axe horizontal : r = c sin²θ
const ldip = (cx, cy, c, haut, t0 = 0.12) => Array.from({length: 121}, (_, i) => { const t = t0 + (Math.PI - 2 * t0) * i / 120, r = c * Math.sin(t) ** 2; return [cx + r * Math.cos(t), cy - (haut ? 1 : -1) * r * Math.sin(t)]; });
const mid = (pts, c = '') => { const k = Math.floor(pts.length / 2); return A(r2(pts[k - 2][0]), r2(pts[k - 2][1]), r2(pts[k + 2][0]), r2(pts[k + 2][1]), c); };
const dipole = (cx, cy, cs, cl = 'soft', rev = false) => cs.map(c => [true, false].map(h => { const p = ldip(cx, cy, c, h); const q = rev ? p.slice().reverse() : p; return `<path d="${pth(p)}" class="s ${cl}"/>` + mid(q, cl); }).join('')).join('');

export const FIGS = {
// ---------- champ électrostatique ----------
'mp-electrostatique-1': ['Principe de Curie : en un point d’un plan de symétrie de la distribution, E est contenu dans ce plan ; en un point d’un plan d’antisymétrie, E lui est orthogonal', svg(440, 220, `
  ${L(110, 15, 110, 195, 'dash b')}${chg(60, 110, '+')}${chg(160, 110, '+')}${dot(110, 70)}${T(102, 66, I('M'), '', 'end')}
  ${A(110, 70, 110, 20, 'r')}${T(118, 30, V('E'), 'r', 'start')}${T(110, 212, 'plan de symétrie', 'nt', 'middle')}
  ${L(220, 10, 220, 210, 'dash soft')}
  ${L(330, 15, 330, 195, 'dash b')}${chg(280, 110, '+')}${chg(380, 110, '−')}${dot(330, 70)}${T(322, 62, I('M'), '', 'end')}
  ${A(330, 70, 390, 70, 'r')}${T(394, 66, V('E'), 'r', 'start')}${T(330, 212, 'plan d’antisymétrie', 'nt', 'middle')}`, 'Symétries')],

'mp-electrostatique-2': ['Théorème de Gauss : le flux de E sortant d’une surface fermée S vaut Q_int/ε₀ ; seules comptent les charges intérieures (ici q₁ et q₂, pas q₃)', svg(400, 220, `
  <path d="M90,110 C90,40 200,25 260,50 C330,80 320,170 240,185 C160,200 90,170 90,110 Z" class="s b fillA"/>
  ${dot(160, 100)}${T(168, 96, sb(I('q'), '1'), '', 'start')}${dot(230, 130)}${T(238, 126, sb(I('q'), '2'), '', 'start')}${dot(350, 90)}${T(358, 86, sb(I('q'), '3'), '', 'start')}
  ${A(290, 68, 316, 50, 'r')}${A(112, 172, 92, 190, 'r')}${A(240, 185, 244, 213, 'r')}${T(320, 46, sb(V('n'), 'ext'), 'r', 'start')}${T(76, 64, I('S'), 'b', 'middle')}
  ${T(20, 212, '∯ ' + V('E') + '·d' + V('S') + ' = ' + sb(I('Q'), 'int') + '/' + sb(I('ε'), '0'), '', 'start')}`, 'Théorème de Gauss')],

// ---------- exemples ----------
'mp-exemples-e-1': ['Boule de rayon R uniformément chargée : par symétrie sphérique, E est radial ; le théorème de Gauss sur une sphère de rayon r donne E ∝ r à l’intérieur, E ∝ 1/r² à l’extérieur', svg(440, 220, `
  ${C(100, 110, 50, 'fillR')}${C(100, 110, 80, 'dash b')}${dot(100, 110)}${L(100, 110, ...pol(100, 110, 50, 200), 'soft')}${T(...pol(100, 110, 30, 214), I('R'))}
  ${[30, 100, 170, 260, 330].map(a => A(...pol(100, 110, 80, a), ...pol(100, 110, 104, a), 'r')).join('')}${T(...pol(100, 110, 90, 140), I('r'), 'b')}
  ${axes(240, 190, 190, 0, 160, 0, I('r'), I('E'))}
  ${courbe(u => u < 50 ? 2.4 * u : 120 * 2500 / (u * u), 0, 180, 240, 190, 1, -1, 200, 'b')}
  ${L(290, 70, 290, 194, 'dash soft')}${T(290, 206, I('R'))}${T(330, 60, '∝ 1/' + I('r') + '²', 'nt', 'start')}`, 'Boule chargée')],

'mp-exemples-e-2': ['Fil infini de charge linéique λ : E radial (perpendiculaire au fil), même norme à distance r ; le cylindre de Gauss de rayon r et de hauteur h donne E = λ/(2πε₀r)', svg(380, 230, `
  ${L(150, 10, 150, 220, 'thick r')}${T(158, 22, I('λ'), 'r', 'start')}
  <ellipse cx="150" cy="60" rx="60" ry="14" class="s b"/><ellipse cx="150" cy="170" rx="60" ry="14" class="s b dash"/>${L(90, 60, 90, 170, 'b')}${L(210, 60, 210, 170, 'b')}
  ${[90, 125].map(y => A(210, y, 260, y, 'r') + A(90, y, 40, y, 'r')).join('')}${T(264, 95, V('E'), 'r', 'start')}
  ${D(150, 115, 210, 115, '', 0, 0)}${T(180, 108, I('r'))}${D(230, 60, 230, 170, '', 0, 0)}${T(238, 140, I('h'), '', 'start')}`, 'Fil infini')],

'mp-exemples-e-3': ['Plan infini de charge surfacique σ : E perpendiculaire au plan, de sens opposés de part et d’autre ; le cylindre de Gauss qui traverse le plan donne E = σ/(2ε₀)', svg(400, 230, `
  <path d="M40,140 L150,90 L360,90 L250,140 Z" class="s fillR"/>${T(330, 130, I('σ'), 'r', 'start')}
  <ellipse cx="200" cy="55" rx="34" ry="10" class="s b"/><ellipse cx="200" cy="175" rx="34" ry="10" class="s b"/>${L(166, 55, 166, 175, 'b')}${L(234, 55, 234, 175, 'b')}
  ${A(200, 55, 200, 10, 'r')}${A(200, 175, 200, 220, 'r')}${T(208, 22, V('E'), 'r', 'start')}${T(208, 214, V('E'), 'r', 'start')}
  ${T(60, 40, I('E') + ' = ' + I('σ') + '/(2' + sb(I('ε'), '0') + ')', '', 'start')}`, 'Plan infini')],

'mp-exemples-e-4': ['Condensateur plan (armatures de surface S distantes de e, e ≪ dimensions) : champ uniforme E = σ/ε₀ entre les armatures, nul à l’extérieur ; capacité C = ε₀S/e', svg(400, 210, `
  ${L(60, 50, 340, 50, 'thick')}${L(60, 160, 340, 160, 'thick')}
  ${[80, 120, 160, 200, 240, 280, 320].map(x => T(x, 42, '+', 'r') + T(x, 178, '−', 'b')).join('')}
  ${[90, 150, 210, 270, 330].map(x => A(x - 10, 58, x - 10, 152, 'r')).join('')}${T(126, 110, V('E'), 'r', 'end')}
  ${D(370, 50, 370, 160, '', 0, 0)}${T(378, 110, I('e'), '', 'start')}${T(30, 54, '+' + I('Q'), '', 'end')}${T(30, 164, '−' + I('Q'), '', 'end')}`, 'Condensateur plan')],

// ---------- dipôle électrostatique ----------
'mp-dipole-e-1': ['Dipôle électrostatique p (vu de loin) : lignes de champ (trait plein) et équipotentielles (pointillés), orthogonales entre elles', svg(400, 260, (() => {
  const cx = 200, cy = 130;
  let s = dipole(cx, cy, [60, 110, 170], 'soft');
  [26, 42, 62].forEach(k => [1, -1].forEach(sg => { const pts = Array.from({length: 81}, (_, i) => { const t = -Math.PI / 2 + 0.02 + (Math.PI - 0.04) * i / 80, r = k * Math.sqrt(Math.cos(t)); return [cx + sg * r * Math.cos(t), cy - r * Math.sin(t)]; }); s += `<path d="${pth(pts)}" class="s b dash"/>`; }));
  return s + A(cx - 14, cy, cx + 14, cy, 'thick') + T(cx, cy + 22, V('p')) + T(cx + 80, cy - 20, sb(I('V'), '&gt; 0'), 'b', 'middle') + T(cx - 80, cy - 20, sb(I('V'), '&lt; 0'), 'b', 'middle');
})(), 'Dipôle')],

'mp-dipole-e-2': ['Dipôle rigide dans un champ uniforme : forces opposées qE et −qE (résultante nulle), couple Γ = p ∧ E qui tend à aligner p sur E ; énergie Ep = −p·E', svg(400, 220, `
  ${[40, 80, 140, 180].map(y => A(20, y, 380, y, 'soft')).join('')}${T(384, 30, V('E'), '', 'end')}
  ${(() => { const [x1, y1] = pol(200, 110, 50, 215), [x2, y2] = pol(200, 110, 50, 35); return L(x1, y1, x2, y2) + chg(x2, y2, '+', 'r') + chg(x1, y1, '−', 'b') + A(x2 + 9, y2, x2 + 60, y2, 'r') + T(x2 + 64, y2 + 4, I('q') + V('E'), 'r', 'start') + A(x1 - 9, y1, x1 - 60, y1, 'b') + T(x1 - 64, y1 + 4, '−' + I('q') + V('E'), 'b', 'end'); })()}
  ${L(200, 110, 300, 110, 'dash soft')}${arc(200, 110, 40, 0, 35, 'b')}${T(...pol(200, 110, 52, 17), I('θ'), 'b')}${T(200, 210, V('Γ') + ' = ' + V('p') + ' ∧ ' + V('E') + ' : rappel vers ' + I('θ') + ' = 0', '', 'middle')}`, 'Dipôle dans un champ')],

// ---------- magnétostatique ----------
'mp-magnetostatique-1': ['Théorème d’Ampère pour un fil infini : B est orthoradial ; sur un cercle de rayon r orienté, la circulation 2πrB vaut μ₀I, d’où B = μ₀I/(2πr)', svg(320, 220, `
  ${C(160, 110, 75, 'dash b')}${ox(160, 110)}${T(160, 136, I('I'), '', 'middle')}
  ${A(...pol(160, 110, 75, 80), ...pol(160, 110, 75, 100), 'b')}${T(...pol(160, 110, 92, 95), '(' + I('C') + ')', 'b')}
  ${dot(...pol(160, 110, 75, -20))}${A(...pol(160, 110, 75, -20), ...pol(...pol(160, 110, 75, -20), 50, 70), 'r')}
  ${T(254, 92, V('B'), 'r', 'start')}${L(160, 110, ...pol(160, 110, 75, -20), 'soft')}${T(...pol(160, 110, 40, -34), I('r'))}`, 'Ampère, fil')],

'mp-magnetostatique-2': ['Solénoïde infini (n spires par mètre) : B est axial, nul à l’extérieur ; le contour rectangulaire dont un côté de longueur ℓ est à l’intérieur donne Bℓ = μ₀nℓI, soit B = μ₀nI', svg(400, 240, `
  ${[60, 100, 140, 180, 220, 260, 300, 340].map(x => ox(x, 50) + ot(x, 170)).join('')}${T(360, 40, I('I'), '', 'start')}
  ${[78, 102].map(y => A(40, y, 360, y, 'r')).join('')}${T(366, 82, V('B'), 'r', 'start')}
  ${R(140, 130, 120, 80, 'b dash')}${A(200, 130, 230, 130, 'b')}${T(128, 128, I('A'), 'b', 'end')}${T(272, 128, I('B'), 'b', 'start')}${T(272, 222, I('C'), 'b', 'start')}${T(128, 222, I('D'), 'b', 'end')}
  ${D(140, 118, 260, 118, '', 0, 0)}${T(170, 124, I('ℓ'))}`, 'Solénoïde, Ampère')],

'mp-magnetostatique-3': ['Câble coaxial (âme de rayon R₁ parcourue par I, gaine entre R₂ et R₃ parcourue par −I) : contours d’Ampère circulaires et profil B(r)', svg(440, 230, `
  ${C(100, 115, 85, 'fillA')}${C(100, 115, 70, 'fillW')}${C(100, 115, 28, 'fillR')}${ox(100, 115)}
  ${[0, 90, 180, 270].map(a => ot(...pol(100, 115, 77.5, a + 45))).join('')}
  ${[18, 50, 78, 100].map(r => C(100, 115, r, 'dash b')).join('')}
  ${L(100, 115, ...pol(100, 115, 28, 30), 'soft')}${T(...pol(100, 115, 34, 52), sb(I('R'), '1'), '', 'start')}
  ${axes(240, 200, 190, 0, 170, 0, I('r'), I('B'))}
  ${courbe(u => u < 30 ? 4.5 * u : u < 75 ? 135 * 30 / u : u < 91 ? 54 * 75 / u * (91 * 91 - u * u) / (91 * 91 - 75 * 75) : 0, 0, 180, 240, 200, 1, -1, 300, 'b')}
  ${[[30, 'R₁'], [75, 'R₂'], [91, 'R₃']].map(([u, t]) => L(240 + u, 196, 240 + u, 204) + T(240 + u, 218, I(t[0]) + t.slice(1))).join('')}`, 'Câble coaxial')],

'mp-magnetostatique-4': ['Nappe plane de courant surfacique js (sortant) : B est parallèle au plan, perpendiculaire à js, de sens opposés de part et d’autre, de norme μ₀js/2', svg(400, 200, `
  ${L(20, 100, 380, 100, 'thick')}${[50, 100, 150, 200, 250, 300, 350].map(x => ox(x, 100)).join('')}${T(384, 92, sb(V('j'), 's'), '', 'end')}
  ${[90, 200, 310].map(x => A(x + 30, 50, x - 30, 50, 'r') + A(x - 30, 150, x + 30, 150, 'r')).join('')}${T(206, 40, V('B'), 'r', 'middle')}${T(206, 176, V('B'), 'r', 'middle')}`, 'Nappe de courant')],

// ---------- dipôle magnétique ----------
'mp-dipole-m-1': ['Une spire de courant vue de loin est un dipôle magnétique de moment m = I S n : ses lignes de champ ont la même forme que celles du dipôle électrostatique (loin de la source)', svg(400, 260, `
  ${dipole(200, 130, [60, 110, 170], 'soft')}
  <ellipse cx="200" cy="130" rx="7" ry="22" class="s thick"/>${A(200, 130, 236, 130, 'b')}${T(240, 124, V('m'), 'b', 'start')}${T(186, 100, I('I'), '', 'end')}`, 'Spire et dipôle')],

'mp-dipole-m-2': ['Aiguille aimantée (moment m) dans un champ B uniforme : couple Γ = m ∧ B qui ramène m vers B (position d’équilibre stable)', svg(360, 200, `
  ${[40, 160].map(y => A(20, y, 340, y, 'soft')).join('')}${T(344, 36, V('B'), '', 'end')}
  ${(() => { const [a, b] = pol(180, 100, 60, 40), [c, d] = pol(180, 100, 60, 220), [e, f] = pol(180, 100, 9, 130), [g, h] = pol(180, 100, 9, 310); return P(`M${a},${b} L${e},${f} L${c},${d} L${g},${h} Z`, 'fillW') + P(`M${a},${b} L${e},${f} L180,100 L${g},${h} Z`, 'fillR'); })()}
  ${dot(180, 100)}${A(180, 100, ...pol(180, 100, 40, 40), 'b')}${T(...pol(180, 100, 50, 52), V('m'), 'b')}
  ${L(180, 100, 270, 100, 'dash soft')}${arc(180, 100, 34, 0, 40, 'b')}${arc(180, 100, 80, 32, 8, 'r')}${A(...pol(180, 100, 80, 12), ...pol(180, 100, 80, 6), 'r')}${T(...pol(180, 100, 94, 22), V('Γ'), 'r')}`, 'Boussole')],

// ---------- Maxwell ----------
'mp-maxwell-1': ['Relations de passage à une interface portant σ et js : E₂ − E₁ = (σ/ε₀) n₁₂ (composante tangentielle continue) ; B₂ − B₁ = μ₀ js ∧ n₁₂ (composante normale continue)', svg(420, 210, `
  <path d="M20,110 C120,100 300,120 400,105" class="s thick"/>${T(400, 40, '(2)', 'nt', 'end')}${T(400, 190, '(1)', 'nt', 'end')}
  ${dot(200, 110)}${A(200, 110, 200, 50, 'b')}${T(208, 56, sb(V('n'), '12'), 'b', 'start')}${T(60, 96, I('σ') + ', ' + sb(V('j'), 's'), 'r', 'middle')}
  ${A(290, 113, 340, 60, 'r')}${T(346, 58, sb(V('E'), '2'), 'r', 'start')}${A(290, 113, 340, 170, 'r')}${T(346, 176, sb(V('E'), '1'), 'r', 'start')}
  ${T(120, 160, sb(V('E'), '2') + ' − ' + sb(V('E'), '1') + ' = ' + I('σ') + '/' + sb(I('ε'), '0') + ' ' + sb(V('n'), '12'), '', 'middle')}`, 'Relations de passage')],

// ---------- énergie EM ----------
'mp-energie-em-1': ['Fil cylindrique résistif parcouru par I : E est axial, B orthoradial ; le vecteur de Poynting Π = E ∧ B/μ₀ est radial et entrant : l’énergie dissipée par effet Joule entre par la surface latérale', svg(420, 200, `
  ${R(60, 70, 300, 60, 'fillA')}<ellipse cx="60" cy="100" rx="10" ry="30" class="s fillW"/><ellipse cx="360" cy="100" rx="10" ry="30" class="s"/>
  ${A(100, 100, 180, 100, 'r')}${T(140, 92, V('E'), 'r')}${A(230, 100, 300, 100)}${T(266, 92, I('I'))}
  ${ox(200, 40)}${ot(200, 160)}${T(212, 44, V('B'), 'b', 'start')}${T(212, 166, V('B'), 'b', 'start')}
  ${A(300, 20, 300, 64, 'r')}${A(300, 180, 300, 136, 'r')}${T(308, 34, V('Π'), 'r', 'start')}${T(308, 176, V('Π'), 'r', 'start')}`, 'Poynting')],

'mp-energie-em-2': ['Bilan d’énergie sur un volume V fixe délimité par S : la diminution de l’énergie électromagnétique est due au flux sortant de Π et au travail cédé aux charges (j·E)', svg(400, 220, `
  <path d="M90,110 C90,40 200,25 260,50 C330,80 320,170 240,185 C160,200 90,170 90,110 Z" class="s fillA"/>
  ${A(290, 68, 330, 40, 'r')}${A(318, 130, 366, 140, 'r')}${A(112, 172, 82, 196, 'r')}${A(110, 70, 76, 48, 'r')}${T(340, 34, V('Π'), 'r', 'start')}
  ${T(200, 100, I('u') + ' = ' + sb(I('ε'), '0') + I('E') + '²/2 + ' + I('B') + '²/(2' + sb(I('μ'), '0') + ')', '', 'middle')}${T(200, 124, V('j') + '·' + V('E'), 'b', 'middle')}${T(250, 172, I('V'), 'nt', 'middle')}${T(320, 186, I('S'), '', 'middle')}`, 'Bilan local')],

// ---------- ondes dans le vide ----------
'mp-ondes-vide-1': ['Onde plane progressive monochromatique dans le vide : E, B et k forment un trièdre direct, E et B sont en phase, B = k ∧ E/ω, ‖B‖ = ‖E‖/c', svg(440, 220, `
  ${A(30, 120, 420, 120, 'soft')}${T(424, 124, I('z'), '', 'start')}
  ${courbe(u => 70 * Math.sin(u / 40), 0, 360, 40, 120, 1, -1, 300, 'r')}
  ${P(Array.from({length: 121}, (_, i) => { const u = i * 3, v = 45 * Math.sin(u / 40); return (i ? 'L' : 'M') + r2(40 + u - 0.8 * v) + ',' + r2(120 + 0.6 * v); }).join(' '), 'b')}
  ${[20, 60, 100].map(k => { const u = k * 3 * 0 + (k === 20 ? 63 : k === 60 ? 188 : 314), v = 70 * Math.sin(u / 40), w = 45 * Math.sin(u / 40); return A(40 + u, 120, 40 + u, r2(120 - v), 'r') + A(40 + u, 120, r2(40 + u - 0.8 * w), r2(120 + 0.6 * w), 'b'); }).join('')}
  ${T(103, 44, V('E'), 'r', 'middle')}${T(56, 178, V('B'), 'b', 'middle')}${A(360, 190, 410, 190)}${T(414, 194, V('k'), '', 'start')}`, 'OPPM')],

'mp-ondes-vide-2': ['États de polarisation : trajectoire de l’extrémité de E dans un plan d’onde (rectiligne, circulaire, elliptique)', svg(440, 170, `
  ${[70, 220, 370].map(x => A(x - 55, 85, x + 55, 85, 'soft') + A(x, 145, x, 25, 'soft') + T(x + 55, 100, sb(I('E'), I('x')), '', 'end') + T(x + 6, 30, sb(I('E'), I('y')), '', 'start')).join('')}
  ${L(40, 115, 100, 55, 'r thick')}${C(220, 85, 42, 'r')}${A(...pol(220, 85, 42, 30), ...pol(220, 85, 42, 45), 'r')}
  <ellipse cx="370" cy="85" rx="48" ry="24" class="s r" transform="rotate(-25 370 85)"/>${A(...pol(370, 85, 40, 60), ...pol(370, 85, 36, 80), 'r')}
  ${T(70, 165, 'rectiligne', 'nt')}${T(220, 165, 'circulaire', 'nt')}${T(370, 165, 'elliptique', 'nt')}`, 'Polarisations')],

// ---------- plasma ----------
'mp-plasma-1': ['Relation de dispersion d’un plasma : ω² = ωp² + c²k² ; pas de propagation pour ω &lt; ωp (onde évanescente) ; asymptote ω = ck aux hautes fréquences', svg(400, 230, `
  ${R(40, 140, 350, 70, 'fillY')}${T(300, 190, 'ω &lt; ' + sb('ω', 'p') + ' : évanescente', 'nt', 'middle')}
  ${axes(40, 210, 350, 0, 195, 0, I('k'), I('ω'))}${L(36, 140, 390, 140, 'dash soft')}${T(32, 144, sb('ω', 'p'), '', 'end')}
  ${courbe(u => Math.sqrt(70 * 70 + u * u), 0, 180, 40, 210, 1, -1, 200, 'b')}${L(40, 210, 220, 30, 'dash soft')}${T(226, 36, 'ω = ' + I('ck'), 'nt', 'start')}`, 'Plasma')],

'mp-plasma-2': ['Paquet d’ondes dans un milieu dispersif : l’enveloppe se déplace à la vitesse de groupe vg = dω/dk, la porteuse (crêtes) à la vitesse de phase vφ = ω/k', svg(420, 190, `
  ${A(20, 100, 410, 100, 'soft')}
  ${courbe(u => 70 * Math.exp(-(((u - 200) / 70) ** 2)), 0, 390, 20, 100, 1, -1, 300, 'r dash')}${courbe(u => -70 * Math.exp(-(((u - 200) / 70) ** 2)), 0, 390, 20, 100, 1, -1, 300, 'r dash')}
  ${courbe(u => 70 * Math.exp(-(((u - 200) / 70) ** 2)) * Math.cos((u - 200) / 9), 0, 390, 20, 100, 1, -1, 600, 'b')}
  ${A(220, 20, 280, 20, 'r')}${T(286, 24, sb(I('v'), 'g'), 'r', 'start')}${A(220, 180, 300, 180, 'b')}${T(306, 184, sb(I('v'), 'φ'), 'b', 'start')}`, 'Paquet d’ondes')],

// ---------- conducteur ----------
'mp-conducteur-1': ['Effet de peau : dans un bon conducteur, l’amplitude du champ décroît en exp(−z/δ), avec δ = √(2/(μ₀γω)) l’épaisseur de peau', svg(420, 200, `
  ${R(140, 20, 270, 160, 'fillA')}${T(380, 40, 'métal', 'nt', 'end')}${A(20, 100, 410, 100, 'soft')}${T(414, 116, I('z'), '', 'end')}
  ${courbe(u => 60 * Math.cos(u / 12), -120, 0, 140, 100, 1, -1, 200, 'b')}
  ${courbe(u => 60 * Math.exp(-u / 45) * Math.cos(u / 12), 0, 260, 140, 100, 1, -1, 400, 'b')}
  ${courbe(u => 60 * Math.exp(-u / 45), 0, 260, 140, 100, 1, -1, 200, 'r dash')}${courbe(u => -60 * Math.exp(-u / 45), 0, 260, 140, 100, 1, -1, 200, 'r dash')}
  ${L(185, 96, 185, 104)}${D(140, 170, 185, 170, '', 0, 0)}${T(162, 164, I('δ'))}${T(150, 112, '0', '', 'start')}`, 'Effet de peau')],

'mp-conducteur-2': ['Réflexion d’une OPPM sous incidence normale sur un métal parfait : l’onde réfléchie s’ajoute à l’onde incidente pour donner une onde stationnaire ; nœuds de E sur le métal et tous les λ/2', svg(420, 200, `
  ${R(350, 20, 50, 160, 'fillA')}${L(350, 20, 350, 180, 'thick')}${T(375, 104, 'métal', 'nt', 'middle')}${A(20, 100, 345, 100, 'soft')}
  ${courbe(u => 70 * Math.sin((350 - u) / 40), 20, 350, 0, 100, 1, -1, 300, 'b')}${courbe(u => -70 * Math.sin((350 - u) / 40), 20, 350, 0, 100, 1, -1, 300, 'b dash')}
  ${[0, 1, 2].map(k => dot(r2(350 - k * 40 * Math.PI), 100, 'r')).join('')}${D(r2(350 - 40 * Math.PI), 186, 350, 186, '', 0, 0)}${T(r2(350 - 20 * Math.PI), 180, I('λ') + '/2')}
  ${A(40, 20, 100, 20)}${T(70, 14, 'incidente', 'nt')}${A(160, 20, 100, 20, 'soft')}${T(180, 14, 'réfléchie', 'nt', 'start')}`, 'Onde stationnaire')],

// ---------- rayonnement ----------
'mp-rayonnement-1': ['Dipôle oscillant p(t) = p₀ cos(ωt) u_z : on étudie le champ en M, repéré en coordonnées sphériques (r, θ), dans la zone de rayonnement d ≪ λ ≪ r', svg(400, 240, `
  ${A(120, 200, 120, 20, 'soft')}${T(128, 28, I('z'), '', 'start')}${A(120, 140, 120, 100, 'thick b')}${T(108, 116, V('p'), 'b', 'end')}${dot(120, 140)}${T(112, 156, I('O'), '', 'end')}
  ${L(120, 140, ...pol(120, 140, 200, 40), 'dash soft')}${(() => { const [x, y] = pol(120, 140, 200, 40); return dot(x, y) + T(x + 8, y + 16, I('M'), '', 'start') + A(x, y, ...pol(x, y, 50, 40)) + T(...pol(x, y, 62, 40), sb(V('u'), I('r'))) + A(x, y, ...pol(x, y, 50, -50), 'r') + T(...pol(x, y, 62, -50), sb(V('u'), 'θ'), 'r'); })()}
  ${arc(120, 140, 50, 90, 40, 'b')}${T(...pol(120, 140, 62, 66), I('θ'), 'b')}${T(...pol(120, 140, 110, 48), I('r'))}
  ${T(290, 225, I('d') + ' ≪ ' + I('λ') + ' ≪ ' + I('r'), '', 'middle')}`, 'Dipôle oscillant')],

'mp-rayonnement-2': ['Indicatrice de rayonnement du dipôle oscillant : la puissance rayonnée par unité d’angle solide varie en sin²θ ; elle est maximale dans le plan équatorial et nulle selon l’axe du dipôle', svg(360, 240, `
  ${L(180, 10, 180, 230, 'axis')}${A(180, 135, 180, 105, 'thick b')}${T(170, 140, V('p'), 'b', 'end')}
  ${P(Array.from({length: 361}, (_, i) => { const t = rad(i), r = 120 * Math.sin(t) ** 2; return (i ? 'L' : 'M') + r2(180 + r * Math.sin(t)) + ',' + r2(120 - r * Math.cos(t)); }).join(' ') + ' Z', 'r fillR')}
  ${L(180, 120, ...pol(180, 120, 120 * Math.sin(rad(50)) ** 2, 40), 'soft')}${arc(180, 120, 30, 90, 40, 'b')}${T(...pol(180, 120, 42, 65), I('θ'), 'b')}
  ${T(300, 30, '∝ sin²' + I('θ'), 'r', 'middle')}`, 'Indicatrice')],
};
