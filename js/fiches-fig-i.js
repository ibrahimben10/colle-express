// Schémas des fiches de cours — Informatique (tronc commun MPSI et MP).
import { svg, L, A, D, T, I, C, R, P, dot, sb } from './figkit.js';
import { axes, courbe } from './fiches-kit.js';

const r2 = n => Math.round(n * 100) / 100;
const sup = (b, s) => `${b}<tspan baseline-shift="super" font-size="10">${s}</tspan>`;
// rangée de cases : valeurs, classes facultatives par case
const cases = (x, y, vals, w = 34, h = 30, cl = []) => vals.map((v, i) => R(x + i * w, y, w, h, cl[i] || 'fillW') + T(x + i * w + w / 2, y + h / 2 + 5, String(v))).join('');
const noeud = (x, y, t, c = 'fillW', r = 15) => C(x, y, r, c) + T(x, y + 5, t);
const arete = (x1, y1, x2, y2, r = 15, c = '', fl = false) => { const d = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / d, uy = (y2 - y1) / d; return (fl ? A : L)(r2(x1 + ux * r), r2(y1 + uy * r), r2(x2 - ux * r), r2(y2 - uy * r), c); };

export const FIGS = {
// ---------- Python ----------
'i-python-1': ['Après b = a, les deux noms désignent la même liste : modifier b[0] modifie aussi a. Avec c = a.copy() (ou a[:]), on obtient une liste indépendante', svg(440, 210, `
  ${T(40, 46, 'a', '', 'end')}${T(40, 96, 'b', '', 'end')}${T(40, 166, 'c', '', 'end')}
  ${A(48, 42, 150, 62, 'b')}${A(48, 92, 150, 76)}${A(48, 162, 150, 162)}
  ${cases(152, 54, [9, 2, 3])}${T(290, 74, '← b[0] = 9 modifie aussi a', 'r', 'start')}
  ${cases(152, 147, [1, 2, 3])}${T(290, 167, 'copie indépendante', 'nt', 'start')}
  ${T(152, 38, 'une seule liste en mémoire', 'nt', 'start')}`, 'Références')],

'i-python-2': ['Indices d’une liste de longueur n : de 0 à n − 1, ou de −n à −1 depuis la fin ; la tranche L[2:5] contient les éléments d’indices 2, 3 et 4 (borne de droite exclue)', svg(430, 170, `
  ${cases(84, 60, ['a', 'b', 'c', 'd', 'e', 'f', 'g'], 46, 34, [, , 'fillA', 'fillA', 'fillA'])}
  ${[0, 1, 2, 3, 4, 5, 6].map(i => T(107 + i * 46, 50, String(i), 'b')).join('')}${[-7, -6, -5, -4, -3, -2, -1].map((v, i) => T(107 + i * 46, 116, '−' + -v, 'r')).join('')}
  ${T(74, 50, 'indice', 'nt', 'end')}${T(74, 116, 'négatif', 'nt', 'end')}
  ${L(176, 136, 176, 148)}${L(314, 136, 314, 148)}${L(176, 148, 314, 148)}${T(245, 164, 'L[2:5]', 'b')}`, 'Tranches')],

// ---------- nombres ----------
'i-nombres-1': ['Entiers signés sur 3 bits en complément à deux : de −4 à 3 ; ajouter 1 à 3 (011) donne 100, soit −4 : c’est le dépassement de capacité', svg(360, 310, (() => {
  const v = ['000', '001', '010', '011', '100', '101', '110', '111'], n = [0, 1, 2, 3, -4, -3, -2, -1], cx = 180, cy = 150;
  let s = C(cx, cy, 90, 'soft');
  v.forEach((b, k) => { const a = Math.PI / 2 - k * Math.PI / 4, x = r2(cx + 90 * Math.cos(a)), y = r2(cy - 90 * Math.sin(a)); s += C(x, y, 20, n[k] < 0 ? 'fillR' : 'fillA') + T(x, y + 5, String(n[k]).replace('-', '−')) + T(r2(cx + 130 * Math.cos(a)), r2(cy + 4 - 130 * Math.sin(a)), b, 'nt'); });
  const [x3, y3] = [r2(cx + 90 * Math.cos(-Math.PI / 4)), r2(cy + 90 * Math.sin(Math.PI / 4))];
  return s + P(`M${r2(x3 - 12)},${r2(y3 + 16)} A90,90 0 0 1 ${cx + 22},${cy + 88}`, 'r thick') + A(cx + 30, cy + 86, cx + 22, cy + 88, 'r') + T(cx, cy + 5, 'sens +1', 'nt') + T(cx, 300, '011 + 001 = 100 : 3 + 1 « = » −4', 'r');
})(), 'Complément à deux')],

'i-nombres-2': ['Flottant double précision (IEEE 754) : 1 bit de signe s, 11 bits d’exposant e, 52 bits de mantisse m ; x = (−1)^s × 1,m × 2^(e − 1023)', svg(440, 150, `
  ${R(20, 50, 24, 40, 'fillR')}${R(44, 50, 110, 40, 'fillY')}${R(154, 50, 266, 40, 'fillA')}
  ${T(32, 75, 's')}${T(99, 75, 'exposant')}${T(287, 75, 'mantisse')}
  ${T(32, 110, '1', 'nt')}${T(99, 110, '11 bits', 'nt')}${T(287, 110, '52 bits', 'nt')}${T(220, 32, '64 bits', 'nt')}
  ${T(220, 140, I('x') + ' = (−1)' + sup('', I('s')) + ' × 1,' + I('m') + ' × 2' + sup('', I('e') + ' − 1023'), '')}`, 'Flottants')],

// ---------- piles et files ----------
'i-piles-1': ['Pile (LIFO) : on empile et on dépile au sommet, le dernier entré sort le premier. File (FIFO) : on enfile à un bout et on défile à l’autre, le premier entré sort le premier', svg(440, 220, `
  ${P('M60,40 L60,190 L140,190 L140,40')}${cases(64, 152, [1], 72, 34)}${cases(64, 118, [2], 72, 34)}${cases(64, 84, [3], 72, 34, ['fillA'])}
  ${A(170, 30, 140, 70, 'b')}${A(130, 70, 100, 30, 'r')}${T(180, 28, 'empiler', 'b', 'start')}${T(94, 24, 'dépiler', 'r', 'end')}${T(100, 212, 'pile', 'nt')}
  ${L(220, 90, 420, 90)}${L(220, 140, 420, 140)}${cases(260, 98, [1, 2, 3], 46, 34, ['fillA'])}
  ${A(430, 115, 400, 115, 'b')}${A(250, 115, 210, 115, 'r')}${T(420, 80, 'enfiler', 'b', 'end')}${T(222, 80, 'défiler', 'r', 'start')}${T(320, 212, 'file', 'nt')}`, 'Pile et file')],

// ---------- complexité ----------
'i-complexite-1': ['Croissance comparée des complexités usuelles : log n ≪ n ≪ n log n ≪ n² ≪ 2ⁿ', svg(420, 240, `
  ${axes(40, 210, 340, 0, 195, 0, I('n'), 'temps')}
  ${courbe(u => 6 * Math.log2(1 + u / 33), 0, 330, 40, 210, 1, -1, 200, 'soft')}
  ${courbe(u => 6 * u / 33, 0, 330, 40, 210, 1, -1, 200, 'b')}
  ${courbe(u => 6 * (u / 33) * Math.log2(1 + u / 33), 0, 303, 40, 210, 1, -1, 200, 'b dash')}
  ${courbe(u => 6 * (u / 33) ** 2, 0, 183, 40, 210, 1, -1, 200, 'r')}
  ${courbe(u => 6 * 2 ** (u / 33), 0, 163, 40, 210, 1, -1, 300, 'r dash')}
  ${T(374, 182, 'log ' + I('n'), 'nt', 'end')}${T(374, 140, I('n'), 'b', 'end')}${T(348, 38, I('n') + ' log ' + I('n'), 'b', 'start')}${T(228, 34, I('n') + '²', 'r', 'start')}${T(196, 34, '2' + sup('', I('n')), 'r', 'end')}`, 'Complexités')],

// ---------- dichotomie ----------
'i-recherche-1': ['Recherche dichotomique de 23 dans un tableau trié : on compare à l’élément du milieu et on garde la moitié qui peut le contenir ; au plus ⌈log₂(n + 1)⌉ comparaisons', svg(440, 220, (() => {
  const t = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91], st = [[0, 9, 4], [5, 9, 7], [5, 6, 5]];
  return st.map(([g, d, m], k) => { const y = 30 + k * 62; return cases(60, y, t, 34, 30, t.map((_, i) => i === m ? (k === 2 ? 'fillA' : 'fillY') : (i < g || i > d ? 'fillG' : 'fillW'))) + T(50, y + 20, `${k + 1}`, 'nt', 'end') + T(60 + m * 34 + 17, y + 46, k === 2 ? 'trouvé' : `t[${m}] = ${t[m]} ${t[m] < 23 ? '&lt;' : '>'} 23`, k === 2 ? 'b' : 'nt'); }).join('');
})(), 'Dichotomie')],

// ---------- tris ----------
'i-tris-1': ['Tri par insertion : à chaque étape, l’élément suivant (en rouge) est inséré à sa place dans la partie déjà triée (en bleu)', svg(360, 240, (() => {
  const et = [[5, 2, 4, 6, 1], [2, 5, 4, 6, 1], [2, 4, 5, 6, 1], [2, 4, 5, 6, 1], [1, 2, 4, 5, 6]];
  return et.map((t, k) => cases(90, 14 + k * 44, t, 40, 32, t.map((_, i) => i <= k ? (i === [-1, 0, 1, 3, 0][k] ? 'fillR' : 'fillA') : 'fillW')) + T(80, 35 + k * 44, k ? `étape ${k}` : 'départ', 'nt', 'end')).join('');
})(), 'Tri par insertion')],

'i-tris-2': ['Tri fusion : on coupe le tableau en deux moitiés, on les trie récursivement puis on fusionne deux listes triées ; complexité O(n log n)', svg(440, 280, (() => {
  const lv = [[[38, 27, 43, 3]], [[38, 27], [43, 3]], [[38], [27], [43], [3]], [[27, 38], [3, 43]], [[3, 27, 38, 43]]];
  let s = '';
  lv.forEach((row, k) => { const y = 14 + k * 54, n = row.length, W = 400 / n; row.forEach((t, j) => { const w = t.length * 30, x = 20 + j * W + (W - w) / 2; s += cases(x, y, t, 30, 28, t.map(() => k >= 3 ? 'fillA' : 'fillW')); }); });
  return s + T(430, 98, 'découpage', 'nt', 'end') + T(430, 206, 'fusion', 'b', 'end');
})(), 'Tri fusion')],

// ---------- récursivité ----------
'i-recursivite-1': ['Arbre des appels de fib(4) avec la définition récursive naïve : fib(2) est calculé deux fois, fib(1) trois fois ; le nombre d’appels croît exponentiellement', svg(440, 230, (() => {
  const N = [['4', 220, 30], ['3', 120, 90], ['2', 320, 90], ['2', 60, 150], ['1', 180, 150], ['1', 280, 150], ['0', 360, 150], ['1', 30, 210], ['0', 90, 210]];
  const E = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8]];
  return E.map(([a, b]) => arete(N[a][1], N[a][2], N[b][1], N[b][2], 17)).join('') + N.map(([t, x, y], i) => C(x, y, 17, (t === '2') ? 'fillR' : 'fillW') + T(x, y + 5, 'f(' + t + ')')).join('');
})(), 'Arbre des appels')],

'i-recursivite-2': ['Pile d’appels de fact(3) : chaque appel attend le résultat du suivant ; le cas de base fact(0) = 1 arrête la récursion, puis les résultats remontent', svg(440, 200, `
  ${[['fact(3)', 3], ['fact(2)', 2], ['fact(1)', 1], ['fact(0)', 0]].map(([t, k], i) => R(40 + i * 0, 150 - i * 36, 120, 32, i === 3 ? 'fillA' : 'fillW') + T(100, 171 - i * 36, t)).join('')}
  ${T(100, 196, 'empilement des appels', 'nt')}
  ${[['fact(0) = 1', 0], ['fact(1) = 1 × 1 = 1', 1], ['fact(2) = 2 × 1 = 2', 2], ['fact(3) = 3 × 2 = 6', 3]].map(([t], i) => T(220, 50 + i * 36, t, i === 3 ? 'b' : '', 'start')).join('')}
  ${A(190, 150, 190, 46, 'b')}${T(196, 196, 'retours', 'nt', 'start')}`, 'Pile d’appels')],

// ---------- gloutons ----------
'i-gloutons-1': ['Sélection d’activités : on trie par date de fin croissante et on prend chaque activité compatible avec les précédentes ; ce choix glouton est optimal', svg(440, 220, (() => {
  const act = [[1, 4, 1], [3, 5, 0], [0, 6, 0], [5, 7, 1], [3, 9, 0], [6, 10, 0], [8, 11, 1], [8, 12, 0], [12, 14, 1]];
  const X = t => 30 + t * 27;
  return act.map(([a, b, ok], k) => R(X(a), 10 + k * 20, X(b) - X(a), 14, ok ? 'fillA b' : 'fillW')).join('') + A(30, 200, 420, 200) + [0, 2, 4, 6, 8, 10, 12, 14].map(t => L(X(t), 196, X(t), 204) + T(X(t), 216, String(t), 'nt')).join('') + T(424, 196, I('t'), '', 'end');
})(), 'Sélection d’activités')],

// ---------- graphes ----------
'i-graphes-1': ['Un même graphe non orienté sous trois formes : dessin, matrice d’adjacence (M[i][j] = 1 si i et j sont voisins) et listes d’adjacence (dictionnaire des voisins)', svg(460, 200, (() => {
  const S = [[60, 50], [150, 50], [60, 150], [150, 150]], E = [[0, 1], [0, 2], [1, 2], [2, 3]];
  const M = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]];
  let s = E.map(([a, b]) => arete(...S[a], ...S[b])).join('') + S.map(([x, y], i) => noeud(x, y, String(i))).join('');
  s += M.map((r, i) => cases(200, 30 + i * 30, r, 28, 30, r.map(v => v ? 'fillA' : 'fillW'))).join('') + [0, 1, 2, 3].map(i => T(214 + i * 28, 22, String(i), 'nt') + T(192, 50 + i * 30, String(i), 'nt', 'end')).join('');
  s += ['0 : [1, 2]', '1 : [0, 2]', '2 : [0, 1, 3]', '3 : [2]'].map((t, i) => T(340, 50 + i * 30, t, '', 'start')).join('');
  return s + T(105, 190, 'graphe', 'nt') + T(256, 190, 'matrice', 'nt') + T(380, 190, 'listes', 'nt');
})(), 'Représentations')],

'i-graphes-2': ['Parcours depuis le sommet 0 : en largeur (BFS, file), les sommets sont visités par distance croissante ; en profondeur (DFS, pile ou récursivité), on suit un chemin le plus loin possible avant de revenir', svg(460, 210, (() => {
  const S = [[70, 30], [30, 100], [110, 100], [30, 170], [80, 170], [150, 170]], E = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]];
  const g = (dx, ord, c) => E.map(([a, b]) => arete(S[a][0] + dx, S[a][1], S[b][0] + dx, S[b][1])).join('') + S.map(([x, y], i) => C(x + dx, y, 15, c) + T(x + dx, y + 5, String(i)) + T(x + dx + 20, y - 10, String(ord[i]), 'r', 'start')).join('');
  return g(20, [1, 2, 3, 4, 5, 6], 'fillA') + T(110, 206, 'largeur : 0 1 2 3 4 5', 'nt') + g(260, [1, 2, 5, 3, 4, 6], 'fillY') + T(350, 206, 'profondeur : 0 1 3 4 2 5', 'nt');
})(), 'Parcours')],

'i-plus-courts-1': ['Algorithme de Dijkstra depuis A (poids positifs) : on traite à chaque étape le sommet non traité de plus petite distance provisoire, puis on met à jour ses voisins ; distances finales en rouge', svg(440, 220, (() => {
  const S = {A: [50, 110], B: [170, 40], C: [170, 180], D: [300, 110], E: [400, 110]}, W = [['A', 'B', 4], ['A', 'C', 1], ['C', 'B', 2], ['B', 'D', 5], ['C', 'D', 8], ['D', 'E', 3]];
  const d = {A: 0, B: 3, C: 1, D: 8, E: 11}, arbre = ['A-C', 'C-B', 'B-D', 'D-E'];
  return W.map(([a, b, w]) => { const t = arbre.includes(a + '-' + b); return arete(...S[a], ...S[b], 18, t ? 'b thick' : '') + T(r2((S[a][0] + S[b][0]) / 2 + 8), r2((S[a][1] + S[b][1]) / 2 - 6), String(w), 'nt'); }).join('')
    + Object.entries(S).map(([k, [x, y]]) => noeud(x, y, k, 'fillA', 18) + T(x, y + (y > 150 ? 34 : -26), String(d[k]), 'r')).join('');
})(), 'Dijkstra')],

// ---------- SQL ----------
'i-sql-1': ['Schéma relationnel : chaque table a une clé primaire (soulignée) ; la clé étrangère id_classe de Eleve fait référence à la clé primaire de Classe', svg(440, 200, `
  ${R(30, 30, 160, 30, 'fillA')}${T(110, 50, 'Eleve')}${R(30, 60, 160, 100, 'fillW')}
  ${T(44, 84, '<tspan text-decoration="underline">id</tspan>', '', 'start')}${T(44, 106, 'nom', '', 'start')}${T(44, 128, 'note', '', 'start')}${T(44, 150, 'id_classe', 'b', 'start')}
  ${R(270, 30, 140, 30, 'fillA')}${T(340, 50, 'Classe')}${R(270, 60, 140, 56, 'fillW')}${T(284, 84, '<tspan text-decoration="underline">id</tspan>', '', 'start')}${T(284, 106, 'nom', '', 'start')}
  ${P('M190,146 C230,146 230,80 268,80', 'b')}${A(250, 80, 268, 80, 'b')}${T(230, 180, 'clé étrangère → clé primaire', 'nt')}`, 'Schéma relationnel')],

'i-sql-2': ['Jointure : SELECT e.nom, c.nom FROM Eleve AS e JOIN Classe AS c ON e.id_classe = c.id associe chaque élève à la ligne de sa classe', svg(460, 220, `
  ${T(100, 18, 'Eleve', 'nt')}${cases(20, 24, ['nom', 'id_classe'], 80, 26, ['fillA', 'fillA'])}${cases(20, 50, ['Ali', 1], 80, 26)}${cases(20, 76, ['Lina', 2], 80, 26)}${cases(20, 102, ['Sami', 1], 80, 26)}
  ${T(330, 18, 'Classe', 'nt')}${cases(270, 24, ['id', 'nom'], 60, 26, ['fillA', 'fillA'])}${cases(270, 50, [1, 'MP'], 60, 26)}${cases(270, 76, [2, 'MPSI'], 60, 26)}
  ${L(180, 63, 268, 63, 'b dash')}${L(180, 115, 268, 63, 'b dash')}${L(180, 89, 268, 89, 'r dash')}
  ${T(230, 152, 'résultat', 'nt')}${cases(150, 158, ['Ali', 'MP'], 80, 20)}${cases(150, 178, ['Lina', 'MPSI'], 80, 20)}${cases(150, 198, ['Sami', 'MP'], 80, 20)}`, 'Jointure')],

// ---------- dictionnaires ----------
'i-dictionnaires-1': ['Table de hachage : la fonction de hachage associe à chaque clé une alvéole ; deux clés peuvent tomber dans la même (collision), on les range alors dans une liste. Accès en temps constant en moyenne', svg(440, 230, `
  ${['"pomme"', '"kiwi"', '"poire"', '"figue"'].map((k, i) => R(20, 20 + i * 50, 90, 32, 'fillY') + T(65, 41 + i * 50, k)).join('')}
  ${R(165, 60, 50, 120, 'fillW')}${T(190, 125, I('h'))}${T(190, 200, 'hachage', 'nt')}
  ${[0, 1, 2, 3, 4].map(i => R(270, 20 + i * 40, 40, 40, 'fillW') + T(262, 44 + i * 40, String(i), 'nt', 'end')).join('')}
  ${[[0, 1], [1, 3], [2, 1], [3, 4]].map(([k, a]) => L(110, 36 + k * 50, 165, 120, 'soft') + A(215, 120, 270, 40 + a * 40, k === 2 ? 'r' : '')).join('')}
  ${dot(290, 80)}${A(296, 80, 318, 80)}${R(318, 66, 60, 28, 'fillY')}${T(348, 85, 'pomme')}${A(378, 80, 388, 80)}${R(388, 66, 50, 28, 'fillR')}${T(413, 85, 'poire')}
  ${T(380, 116, 'collision', 'r')}${dot(290, 160)}${A(296, 160, 318, 160)}${R(318, 146, 60, 28, 'fillY')}${T(348, 165, 'kiwi')}${dot(290, 200)}${A(296, 200, 318, 200)}${R(318, 186, 60, 28, 'fillY')}${T(348, 205, 'figue')}`, 'Table de hachage')],

// ---------- programmation dynamique ----------
'i-progdyn-1': ['Mémoïsation : dans l’arbre des appels de fib(5), les sous-problèmes grisés ont déjà été calculés ; en stockant les résultats (dictionnaire), on fait un seul calcul par sous-problème, soit O(n) au lieu d’un coût exponentiel', svg(440, 220, (() => {
  const N = [['5', 220, 25, 0], ['4', 120, 80, 0], ['3', 320, 80, 1], ['3', 60, 135, 0], ['2', 180, 135, 1], ['2', 30, 190, 0], ['1', 90, 190, 0]];
  const E = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 5], [3, 6]];
  return E.map(([a, b]) => arete(N[a][1], N[a][2], N[b][1], N[b][2], 17)).join('') + N.map(([t, x, y, m]) => C(x, y, 17, m ? 'fillG' : 'fillA') + T(x, y + 5, 'f(' + t + ')')).join('') + T(330, 140, 'déjà en mémoire', 'nt') + T(330, 156, ': lecture directe', 'nt');
})(), 'Mémoïsation')],

'i-progdyn-2': ['Sac à dos (capacité 5 ; objets (poids, valeur) : (2, 3), (3, 4), (4, 5)) : T[i][c] = meilleure valeur avec les i premiers objets et la capacité c ; chaque case se déduit de deux cases de la ligne précédente', svg(440, 220, (() => {
  const T0 = [[0, 0, 0, 0, 0, 0], [0, 0, 3, 3, 3, 3], [0, 0, 3, 4, 4, 7], [0, 0, 3, 4, 5, 7]];
  let s = T0.map((r, i) => cases(110, 40 + i * 34, r, 46, 34, r.map((_, c) => i === 3 && c === 5 ? 'fillA' : i === 2 && (c === 5 || c === 1) ? 'fillY' : 'fillW'))).join('');
  s += [0, 1, 2, 3, 4, 5].map(c => T(133 + c * 46, 32, String(c), 'nt')).join('') + ['aucun', '+ (2, 3)', '+ (3, 4)', '+ (4, 5)'].map((t, i) => T(100, 62 + i * 34, t, 'nt', 'end')).join('');
  return s + T(248, 12, 'capacité ' + I('c'), 'nt') + A(363, 125, 363, 142, 'r') + A(179, 125, 350, 148, 'r') + T(270, 200, 'max(sans l’objet, avec l’objet) = max(7, 0 + 5) = 7', 'r');
})(), 'Sac à dos')],

// ---------- IA ----------
'i-ia-1': ['k plus proches voisins (k = 3) : le point à classer (étoile) prend la classe majoritaire parmi ses 3 voisins les plus proches (ici 2 bleus contre 1 rouge)', svg(380, 240, (() => {
  const Bl = [[80, 60], [110, 100], [60, 130], [150, 140], [200, 110], [120, 180]], Ro = [[260, 60], [300, 100], [240, 170], [320, 160], [190, 175], [280, 200]];
  return C(178, 140, 42, 'dash soft') + Bl.map(([x, y]) => C(x, y, 7, 'fillB b')).join('') + Ro.map(([x, y]) => R(x - 6, y - 6, 12, 12, 'fillR r')).join('') + P('M178,128 L182,137 L192,138 L184,144 L187,154 L178,148 L169,154 L172,144 L164,138 L174,137 Z', 'fill') + T(178, 230, 'nouveau point → classe bleue', 'nt');
})(), 'kNN')],

'i-ia-2': ['Algorithme des k-moyennes (k = 2) : on affecte chaque point au centre le plus proche, puis on remplace chaque centre par la moyenne de son groupe ; on répète jusqu’à stabilité', svg(400, 220, (() => {
  const G1 = [[70, 70], [100, 50], [90, 110], [130, 80], [60, 130]], G2 = [[260, 140], [300, 120], [280, 180], [330, 160], [240, 100]];
  const m = g => g.reduce((a, p) => [a[0] + p[0] / g.length, a[1] + p[1] / g.length], [0, 0]).map(r2);
  const c1 = m(G1), c2 = m(G2);
  return G1.map(p => L(...p, ...c1, 'soft') + C(...p, 7, 'fillB b')).join('') + G2.map(p => L(...p, ...c2, 'soft') + R(p[0] - 6, p[1] - 6, 12, 12, 'fillR r')).join('')
    + [c1, c2].map(([x, y], i) => L(x - 9, y - 9, x + 9, y + 9, 'thick') + L(x - 9, y + 9, x + 9, y - 9, 'thick')).join('') + L(200, 10, 176, 180, 'dash soft') + T(200, 214, '× : centres (moyennes des groupes)', 'nt');
})(), 'k-moyennes')],

// ---------- jeux ----------
'i-jeux-1': ['Arbre minimax : aux nœuds MAX, le joueur choisit la plus grande valeur, aux nœuds MIN l’adversaire choisit la plus petite ; les valeurs remontent des feuilles vers la racine', svg(440, 220, (() => {
  const F = [3, 12, 8, 2, 4, 6, 14, 5, 2], mins = [3, 2, 2];
  let s = T(14, 34, 'MAX', 'b', 'start') + T(14, 104, 'MIN', 'r', 'start');
  mins.forEach((v, i) => { const x = 90 + i * 130; s += arete(220, 30, x, 100, 18) + [0, 1, 2].map(j => { const fx = x - 40 + j * 40, fv = F[i * 3 + j]; return arete(x, 100, fx, 180, 16) + R(fx - 15, 166, 30, 28, 'fillW') + T(fx, 185, String(fv)); }).join('') + C(x, 100, 18, 'fillR') + T(x, 105, String(v)); });
  return s + C(220, 30, 18, 'fillA') + T(220, 35, '3') + T(220, 214, 'valeur de la racine : max(3, 2, 2) = 3', 'nt');
})(), 'Minimax')],

'i-jeux-2': ['Graphe de jeu : les positions du joueur 1 (cercles) et du joueur 2 (carrés) alternent ; l’attracteur du joueur 1 (en bleu) est l’ensemble des positions d’où il peut forcer l’arrivée dans une position gagnante G', svg(440, 200, (() => {
  const S = [[50, 100, 'c', 1], [150, 50, 'r', 1], [150, 150, 'r', 0], [260, 50, 'c', 1], [260, 150, 'c', 0], [370, 100, 'G', 1]];
  const E = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 2], [2, 0]];
  return E.map(([a, b]) => arete(S[a][0], S[a][1], S[b][0], S[b][1], 18, 'soft', true)).join('') + S.map(([x, y, t, at]) => t === 'r' ? R(x - 16, y - 16, 32, 32, at ? 'fillA b' : 'fillW') : C(x, y, 17, t === 'G' ? 'fillA b thick' : at ? 'fillA b' : 'fillW') + (t === 'G' ? T(x, y + 5, 'G') : '')).join('') + T(220, 194, 'en bleu : attracteur du joueur 1', 'nt');
})(), 'Attracteur')],

// ---------- fichiers ----------
'i-fichiers-1': ['Lecture d’un fichier de données : open puis readlines donne la liste des lignes ; on retire le saut de ligne (strip), on découpe avec split(";") et on convertit les champs', svg(460, 200, `
  ${R(20, 30, 130, 120, 'fillW')}${T(85, 22, 'mesures.csv', 'nt')}${['t;x', '0;1.2', '1;1.9', '2;3.1'].map((l, i) => T(32, 56 + i * 26, l, '', 'start')).join('')}
  ${A(156, 90, 196, 90, 'b')}${T(176, 172, 'readlines', 'b')}${L(176, 96, 176, 160, 'dash soft')}
  ${['"t;x\\n"', '"0;1.2\\n"', '"1;1.9\\n"', '"2;3.1\\n"'].map((l, i) => R(200, 30 + i * 30, 90, 26, 'fillY') + T(245, 48 + i * 30, l)).join('')}
  ${A(296, 105, 336, 105, 'b')}${T(316, 172, 'split', 'b')}${L(316, 111, 316, 160, 'dash soft')}
  ${[['0', '1.2'], ['1', '1.9'], ['2', '3.1']].map((r, i) => cases(340, 60 + i * 30, r, 50, 26, ['fillA', 'fillA'])).join('')}${T(390, 48, 'données', 'nt')}
  ${T(230, 196, 'la 1ʳᵉ ligne (en-tête) est ignorée ; float() convertit les champs', 'nt')}`, 'Lecture d’un fichier')],

// ---------- images ----------
'i-images-1': ['Une image est une matrice de pixels : img[i][j] est le pixel de la ligne i et de la colonne j ; en niveaux de gris c’est un entier de 0 (noir) à 255 (blanc), en couleur un triplet (R, V, B)', svg(440, 220, (() => {
  const g = [[0, 60, 120, 180], [60, 120, 180, 240], [120, 180, 240, 255]];
  let s = g.map((r, i) => r.map((v, j) => `<rect x="${60 + j * 50}" y="${40 + i * 50}" width="50" height="50" style="fill:rgb(${v},${v},${v})" class="s"/>` + (v < 130 ? T(85 + j * 50, 70 + i * 50, String(v)).replace('<text', '<text style="fill:#fff"') : T(85 + j * 50, 70 + i * 50, String(v)))).join('')).join('');
  s += [0, 1, 2, 3].map(j => T(85 + j * 50, 32, String(j), 'nt')).join('') + [0, 1, 2].map(i => T(50, 70 + i * 50, String(i), 'nt', 'end')).join('') + T(160, 16, 'colonne ' + I('j'), 'nt') + T(24, 120, I('i'), 'nt');
  s += R(310, 90, 50, 50, 'fillW') + `<rect x="310" y="90" width="50" height="50" style="fill:rgb(230,120,40)" class="s"/>` + T(335, 160, '(230, 120, 40)', 'nt') + T(335, 80, 'pixel couleur', 'nt');
  return s + T(160, 210, 'img[1][2] = 180', 'b');
})(), 'Image et pixels')],

'i-images-2': ['Convolution par un noyau 3 × 3 : la nouvelle valeur d’un pixel est la somme des pixels voisins pondérés par les coefficients du noyau (ici un flou, moyenne des 9 voisins) ; un noyau de différences détecte les contours', svg(460, 210, `
  ${[0, 1, 2, 3, 4].map(i => [0, 1, 2, 3, 4].map(j => R(20 + j * 30, 30 + i * 30, 30, 30, i >= 1 && i <= 3 && j >= 1 && j <= 3 ? 'fillA' : 'fillW')).join('')).join('')}${R(80, 90, 30, 30, 'fillB b thick')}
  ${T(170, 116, '∗', '')}
  ${[0, 1, 2].map(i => [0, 1, 2].map(j => R(190 + j * 34, 56 + i * 34, 34, 34, 'fillY') + T(207 + j * 34, 78 + i * 34, '1')).join('')).join('')}${T(241, 46, '1/9 ×', 'nt')}
  ${T(310, 110, '→', '')}${[0, 1, 2, 3, 4].map(i => [0, 1, 2, 3, 4].map(j => R(330 + j * 24, 50 + i * 24, 24, 24, i === 2 && j === 2 ? 'fillB b' : 'fillW')).join('')).join('')}
  ${T(95, 196, 'voisinage du pixel', 'nt')}${T(240, 196, 'noyau (flou)', 'nt')}${T(390, 196, 'nouvelle image', 'nt')}`, 'Convolution')],

// ---------- zéros ----------
'i-zeros-1': ['Méthode de dichotomie pour f(x) = 0 : f(a) et f(b) de signes opposés ; on garde la moitié de [a, b] où le signe change ; la largeur est divisée par 2 à chaque étape', svg(420, 230, `
  ${axes(30, 130, 380, 0, 110, 90, I('x'), '')}
  ${courbe(u => 0.0035 * (u - 190) ** 2 * Math.sign(u - 190) * 0.9 + 0.35 * (u - 190), 10, 370, 30, 130, 1, -1, 300, 'b')}
  ${[[40, 360, 0], [40, 200, 1], [120, 200, 2], [160, 200, 3]].map(([a, b, k]) => L(30 + a, 160 + k * 18, 30 + b, 160 + k * 18, k === 3 ? 'r thick' : '') + L(30 + a, 155 + k * 18, 30 + a, 165 + k * 18) + L(30 + b, 155 + k * 18, 30 + b, 165 + k * 18)).join('')}
  ${dot(220, 130, 'r')}${T(226, 124, 'α', 'r', 'start')}${T(70, 154, I('a'), '', 'middle')}${T(390, 154, I('b'), '', 'middle')}`, 'Dichotomie')],

'i-zeros-2': ['Méthode de Newton : on remplace la courbe par sa tangente en xₙ ; l’intersection avec l’axe donne xₙ₊₁ = xₙ − f(xₙ)/f′(xₙ). Convergence très rapide près de la racine si f′(α) ≠ 0', svg(420, 230, (() => {
  const f = x => 0.012 * x * x - 1.2, fp = x => 0.024 * x, X = x => r2(30 + x * 10), Y = y => r2(190 - y * 18);   // racine α = 10
  let s = axes(30, 190, 380, 0, 175, 0, I('x'), '') + courbe(u => (0.012 * (u / 10) ** 2 - 1.2) * 18, 0, 290, 30, 190, 1, -1, 300, 'b');
  let x = 26; const pts = [];
  for (let k = 0; k < 3; k++) { const xn = x - f(x) / fp(x); s += L(X(x), 190, X(x), Y(f(x)), 'dash soft') + dot(X(x), Y(f(x))) + L(X(x), Y(f(x)), X(xn), 190, 'r'); pts.push([x, k]); x = xn; }
  return s + pts.map(([x, k]) => T(X(x), 206, sb(I('x'), String(k)), '')).join('') + dot(X(10), 190, 'r') + T(X(10) - 4, 182, 'α', 'r', 'end');
})(), 'Newton')],

// ---------- intégration ----------
'i-integration-1': ['Méthode des rectangles à gauche : l’intégrale est approchée par la somme des aires h × f(xₖ), avec h = (b − a)/n ; erreur en O(h) (en O(1/n))', svg(420, 220, `
  ${axes(30, 190, 380, 0, 175, 0, I('x'), '')}
  ${[0, 1, 2, 3, 4, 5].map(k => { const u = 30 + k * 50, v = 40 + 90 * Math.sin((u + 20) / 110); return R(30 + u, r2(190 - v), 50, r2(v), 'fillA b'); }).join('')}
  ${courbe(u => 40 + 90 * Math.sin((u + 20) / 110), 20, 340, 30, 190, 1, -1, 200, 'r')}
  ${T(60, 206, I('a'))}${T(360, 206, I('b'))}${D(110, 200, 160, 200, '', 0, 0)}${T(135, 214, I('h'))}`, 'Rectangles')],

'i-integration-2': ['Méthode des trapèzes : on relie les points (xₖ, f(xₖ)) par des segments ; l’intégrale est approchée par la somme des aires des trapèzes, h (f(xₖ) + f(xₖ₊₁))/2 ; erreur en O(h²)', svg(420, 220, `
  ${axes(30, 190, 380, 0, 175, 0, I('x'), '')}
  ${[0, 1, 2, 3, 4, 5].map(k => { const u = 30 + k * 50, f = w => 40 + 90 * Math.sin((w + 20) / 110), v1 = f(u), v2 = f(u + 50); return P(`M${30 + u},190 L${30 + u},${r2(190 - v1)} L${80 + u},${r2(190 - v2)} L${80 + u},190 Z`, 'fillA b'); }).join('')}
  ${courbe(u => 40 + 90 * Math.sin((u + 20) / 110), 20, 340, 30, 190, 1, -1, 200, 'r')}
  ${T(60, 206, I('a'))}${T(360, 206, I('b'))}`, 'Trapèzes')],

// ---------- EDO ----------
'i-edo-1': ['Méthode d’Euler explicite pour y′ = F(t, y) : on avance pas à pas le long de la tangente, yₖ₊₁ = yₖ + h F(tₖ, yₖ) ; la solution approchée (points rouges) s’écarte peu à peu de la solution exacte (bleue) ; l’erreur diminue avec h', svg(420, 230, (() => {
  const X = t => r2(40 + t * 140), Y = y => r2(200 - y * 14);
  let s = axes(40, 200, 360, 0, 185, 0, I('t'), I('y')) + courbe(u => Math.exp(u / 140) * 14, 0, 350, 40, 200, 1, -1, 300, 'b');
  let t = 0, y = 1; const h = 0.5;
  for (let k = 0; k < 5; k++) { const y2 = y + h * y; s += L(X(t), Y(y), X(t + h), Y(y2), 'r') + dot(X(t), Y(y), 'r'); t += h; y = y2; }
  return s + dot(X(t), Y(y), 'r') + T(372, 40, 'exacte', 'b', 'end') + T(400, 116, 'Euler', 'r', 'end') + D(X(0), 214, X(0.5), 214, '', 0, 0) + T(X(0.25), 228, I('h'));
})(), 'Euler')],

// ---------- systèmes ----------
'i-systemes-1': ['Pivot de Gauss : par opérations sur les lignes Lᵢ ← Lᵢ − (aᵢⱼ/aⱼⱼ) Lⱼ, on annule les coefficients sous la diagonale (système triangulaire), puis on remonte pour trouver les inconnues ; coût O(n³)', svg(460, 170, (() => {
  const M1 = [['2', '1', '−1', '8'], ['−3', '−1', '2', '−11'], ['−2', '1', '2', '−3']], M2 = [['2', '1', '−1', '8'], ['0', '1/2', '1/2', '1'], ['0', '0', '−1', '1']];
  const mat = (x, M) => M.map((r, i) => r.map((v, j) => T(x + j * 38, 50 + i * 30, v, j === 3 ? 'b' : (i > j && x > 200 ? 'r' : ''))).join('')).join('') + L(x - 16, 30, x - 16, 120) + L(x + 140, 30, x + 140, 120) + L(x + 98, 32, x + 98, 118, 'soft');
  return mat(40, M1) + T(225, 80, '→', '') + mat(280, M2) + T(110, 156, 'système de départ', 'nt') + T(350, 156, 'triangulaire : z = −1, y = 3, x = 2', 'nt');
})(), 'Pivot de Gauss')],

// ---------- numpy ----------
'i-numpy-1': ['Tableau NumPy à deux dimensions : A[i, j] désigne un coefficient, A[1, :] une ligne, A[:, 2] une colonne ; A.shape vaut (3, 4) ; les opérations (A + 1, 2 * A, np.sin(A)) s’appliquent à tous les coefficients', svg(440, 200, `
  ${[0, 1, 2].map(i => cases(110, 40 + i * 36, [0, 1, 2, 3].map(j => 4 * i + j), 48, 36, [0, 1, 2, 3].map(j => i === 1 ? 'fillA' : j === 2 ? 'fillY' : 'fillW'))).join('')}
  ${[0, 1, 2, 3].map(j => T(134 + j * 48, 32, String(j), 'nt')).join('')}${[0, 1, 2].map(i => T(100, 63 + i * 36, String(i), 'nt', 'end')).join('')}
  ${T(330, 80, 'A[1, :] = [4 5 6 7]', 'b', 'start')}${T(330, 110, 'A[:, 2] = [2 6 10]', 'nt', 'start')}${T(206, 170, 'A = np.arange(12).reshape(3, 4)', '')}`, 'NumPy')],

// ---------- aléatoire ----------
'i-aleatoire-1': ['Méthode de Monte-Carlo : on tire N points au hasard dans le carré [0, 1]² ; la proportion de points dans le quart de disque tend vers π/4 ; l’erreur décroît en 1/√N', svg(300, 270, (() => {
  let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  let s = R(40, 20, 220, 220, 'fillW') + P('M40,240 L40,20 A220,220 0 0 1 260,240 Z', 'fillA');
  for (let k = 0; k < 160; k++) { const x = rnd(), y = rnd(), dans = x * x + y * y <= 1; s += dans ? C(r2(40 + 220 * x), r2(240 - 220 * y), 2.6, 'fillB b') : R(r2(40 + 220 * x - 2.4), r2(240 - 220 * y - 2.4), 4.8, 4.8, 'fillR r'); }
  return s + T(40, 256, '0') + T(260, 256, '1') + T(30, 24, '1', '', 'end') + T(150, 268, '4 × (points bleus)/N ≈ π', 'nt');
})(), 'Monte-Carlo')],
};
