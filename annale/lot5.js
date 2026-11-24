// Lot 5 : mécanique quantique et ondes électromagnétiques.
import { CH, svg, L, P, poly, C, Ell, Rect, hatch, hatchRect, aire, paroi, vec, axe, fl, mid, cote, it, sub, sup, q, T, tick, V, pt, ptO,
  sortant, entrant, pol, arc, Ta, graphe } from './kit.js';

const n = v => Math.round(v * 10) / 10;
const small = 13.5, sep = (x, y1, y2) => L(x, y1, x, y2, 'pt');
const onde = (x0, x1, y, k, a, ph = 0, k2 = 'obj') => poly(Array.from({length: Math.ceil((x1 - x0) / 1.5) + 1}, (_, i) => { const x = Math.min(x1, x0 + i * 1.5); return [x, y - a * Math.cos(k * x + ph)]; }), k2);

// ---------- marche de potentiel ----------
const marcheE = svg(380, 190, axe(24, 160, 370, 160) + T(370, 178, it('x'), 'end') + axe(180, 174, 180, 16) + T(172, 22, it('V'), 'end') + tick(174, 176, '0', 'end')
  + P('M24,160 L180,160 L180,96 L356,96', 'epais') + tick(186, 90, q('V', '0'), 'start') + L(24, 56, 356, 56, 'pt') + T(356, 50, it('E'), 'end')
  + vec(44, 126, 130, 126) + T(87, 118, 'électrons', 'middle', 12.5), 'Marche de potentiel');
const marcheC = (() => {
  const k1 = 2 * Math.PI / 30, k2 = k1 / Math.SQRT2;
  const a = P('M20,190 L150,190 L150,150 L250,150', 'fin') + L(150, 30, 150, 196, 'mixte') + tick(150, 210, '0')
    + onde(20, 148, 80, k1, 12) + onde(152, 250, 80, k2, 12, 0) + vec(30, 110, 90, 110) + T(60, 128, 'e' + sup('i' + q('k', '1') + it('x')), 'middle', 12.5)
    + vec(130, 46, 70, 46) + T(100, 38, it('r') + ' e' + sup('−i' + q('k', '1') + it('x')), 'middle', 12.5) + vec(170, 110, 230, 110) + T(200, 128, it('t') + ' e' + sup('i' + q('k', '2') + it('x')), 'middle', 12.5)
    + T(135, 226, '(a) ' + it('E') + ' > ' + q('V', '0') + ' : ' + q('k', '2') + ' < ' + q('k', '1'), 'middle', 12.5);
  const ke = 2 * Math.PI / 40, ka = ke / 1.6, ph = Math.atan(ka / ke);
  let ev = ''; for (let x = 400; x <= 500; x += 2) ev += (ev ? ' L' : 'M') + n(x) + ',' + n(110 - 28 * Math.cos(ph) * Math.exp(-ka * (x - 400)));
  const b = P('M290,190 L400,190 L400,60 L500,60', 'fin') + L(400, 30, 400, 196, 'mixte') + tick(400, 210, '0') + L(290, 110, 500, 110, 'fin')
    + poly(Array.from({length: 74}, (_, i) => { const x = 290 + i * 1.5; return [x, 110 - 28 * Math.cos(ke * (x - 400) + ph)]; })) + P(ev)
    + T(470, 96, 'e' + sup('−κ' + it('x')), 'middle', 12.5) + T(395, 226, '(b) ' + it('E') + ' < ' + q('V', '0') + ' : onde évanescente', 'middle', 12.5);
  return svg(520, 236, a + sep(268, 14, 214) + b, 'Marche de potentiel : ondes incidente, réfléchie, transmise');
})();

// ---------- voile solaire ----------
const voileE = svg(380, 190, C(44, 95, 26) + T(44, 140, 'Soleil', 'middle', 12.5)
  + [55, 80, 110, 135].map(y => vec(80, y, 238, y)).join('') + T(160, 44, 'φ', 'middle')
  + hatchRect(242, 26, 7, 138) + Rect(242, 26, 7, 138) + vec(249, 95, 300, 95) + V(290, 86, 'n') + T(246, 182, 'voile (surface ' + it('S') + ')', 'middle', 12.5),
  'Voile solaire face au Soleil');
const voileC = svg(420, 200, hatchRect(250, 22, 7, 150) + Rect(250, 22, 7, 150)
  + vec(70, 62, 246, 62) + T(150, 52, 'incident : (ε/' + it('c') + ')', 'middle', 12.5) + V(196, 52, 'u', '', 'start')
  + vec(246, 102, 70, 102) + T(150, 124, 'réfléchi : −(ε/' + it('c') + ')', 'middle', 12.5) + V(202, 124, 'u', '', 'start')
  + vec(260, 82, 330, 82) + T(298, 72, '2ε/' + it('c'), 'middle', 12.5) + V(330, 150, 'F', '', 'middle') + T(344, 150, ' = 2φ' + it('S') + '/' + it('c'), 'start', 12.5)
  + axe(40, 180, 80, 180) + V(94, 186, 'u', '', 'start'),
  'Voile : quantité de mouvement cédée par un photon');

// ---------- effet photoélectrique ----------
const photoC = (() => {
  const k = 26, yv = 50, ym = yv + 4.3 * k, yp = ym - 4.88 * k;
  return svg(380, 236, hatchRect(40, ym, 140, 236 - ym) + L(40, ym, 180, ym, 'epais') + T(110, ym + 18, 'zinc', 'middle', 12.5) + L(40, yv, 350, yv, 'pt') + T(350, yv - 6, 'niveau du vide', 'end', 12.5)
    + vec(110, ym, 110, yp) + T(102, (ym + yp) / 2, 'h' + it('ν'), 'end') + fl(110, yp, 180, yp, 'pt')
    + cote(220, ym, 220, yv) + T(228, (ym + yv) / 2 + 5, it('W') + ' = 4,3 eV', 'start', small) + cote(220, yv, 220, yp) + T(228, yp + 2, q('E', 'c'), 'start', small)
    + T(110, ym - 6, 'électron', 'middle', 12) , 'Effet photoélectrique : bilan d’énergie');
})();

// ---------- puits infini ----------
const puitsC = (() => {
  const x0 = 70, x1 = 290, yE = k => 212 - 17 * k * k;
  let s = paroi(x0, 24, x0, 212, 1) + paroi(x1, 24, x1, 212, -1) + L(x0, 212, x1, 212, 'epais') + tick(x0, 228, '0') + tick(x1, 228, it('L'));
  for (const k of [1, 2, 3]) s += L(x0, yE(k), x1, yE(k), 'pt') + poly(Array.from({length: 101}, (_, i) => [x0 + (x1 - x0) * i / 100, yE(k) - 13 * Math.sin(k * Math.PI * i / 100)]))
    + T(x1 + 14, yE(k) + 4, q('E', String(k)) + (k > 1 ? ' = ' + k * k + q('E', '1') : ''), 'start', small);
  return svg(380, 236, s + vec(112, yE(1), 112, yE(2) + 2) + T(104, (yE(1) + yE(2)) / 2 + 5, 'h' + it('ν'), 'end'), 'Puits infini : niveaux et fonctions d’onde');
})();

// ---------- particule sur un cercle ----------
const q1C = svg(300, 240, C(150, 118, 72) + poly(Array.from({length: 241}, (_, i) => pol(150, 118, 72 + 13 * Math.cos(3 * i * Math.PI / 120), i * 1.5)), 'ptobj')
  + pt(150, 118) + L(150, 118, 250, 118, 'pt') + L(150, 118, ...pol(150, 118, 72, 50), 'fin') + C(...pol(150, 118, 72, 50), 5) + arc(150, 118, 26, 0, 50) + Ta(150, 118, 38, 25, 'θ')
  + T(...pol(150, 118, 36, 145), it('R')) + T(150, 222, 'ψ(θ + 2π) = ψ(θ)', 'middle', small),
  'Particule sur un cercle : condition de périodicité');

// ---------- oscillateur harmonique ----------
const q3C = (() => {
  const g = graphe(44, 24, 300, 170, [-3, 3], [0, 3.6]);
  return svg(380, 224, g.axes(it('x'), it('V'), 0, 0) + g.courbe(u => u * u / 2, -2.68, 2.68) + g.hl(.5, 'pt') + g.courbe(u => .5 + 1.2 * Math.exp(-u * u / 2), -3, 3, 'ptobj')
    + T(g.X(-3), g.Y(.5) + 15, q('E', '0') + ' = ħ' + q('ω', '0') + '/2', 'start', 12.5) + pt(g.X(-1), g.Y(.5)) + pt(g.X(1), g.Y(.5)) + L(g.X(1), g.Y(.5), g.X(1), g.Y(0), 'pt') + tick(g.X(1), g.Y(0) + 15, q('x', 'c'))
    + T(g.X(.35), g.Y(1.75), q('ψ', '0'), 'start') + T(g.X(-2.2), g.Y(2.95), '½' + it('m') + q('ω', '0') + sup('2') + it('x') + sup('2'), 'end', 12.5),
    'Oscillateur harmonique : potentiel et état fondamental');
})();

// ---------- potentiel en −λ/x ----------
const q2C = (() => {
  const g = graphe(60, 22, 290, 170, [0, 8], [-2.6, .9]);
  return svg(380, 226, g.axes(it('x'), it('V'), 0, 0) + hatchRect(g.X(0) - 10, 22, 10, 170) + g.courbe(x => -1 / x, .39, 8) + g.hl(-.5, 'pt')
    + aire(`M${g.X(0)},${g.Y(-.5) - 4} H${g.X(2)} V${g.Y(-.5) + 4} H${g.X(0)} Z`) + g.courbe(x => -.5 + 1.2 * x * Math.exp(-x), 0, 8, 'ptobj')
    + pt(g.X(2), g.Y(-.5)) + tick(g.X(2) + 4, g.Y(-.5) + 16, '2/' + it('k'), 'start') + T(g.X(8), g.Y(-.5) + 16, it('E'), 'end') + T(g.X(1), g.Y(-.02), 'φ', 'middle')
    + T(g.X(5), g.Y(-1.4), 'zone accessible : 0 < ' + it('x') + ' < 2/' + it('k'), 'middle', 12) + T(g.X(1.5), g.Y(-2.2), it('V') + ' = −λ/' + it('x'), 'start', 12.5),
    'Potentiel en −λ/x : énergie et zone accessible');
})();

// ---------- atome d'hydrogène ----------
const bohrC = (() => {
  const g = graphe(270, 28, 210, 160, [0, 5], [-3, 3]);
  return svg(510, 230, C(60, 110, 6) + T(60, 115, '+', 'middle', 11) + T(60, 138, 'proton', 'middle', 12) + C(60, 110, 70, 'pt') + pt(...pol(60, 110, 70, 30), 3) + L(60, 110, ...pol(60, 110, 70, 30), 'fin')
    + T(...pol(60, 110, 36, 46), it('a')) + T(...pol(60, 110, 84, 30), 'e' + sup('−'), 'start') + T(110, 212, q('E', 'c') + ' ~ ħ' + sup('2') + '/(2' + q('m', 'e') + it('a') + sup('2') + ')', 'middle', 12.5)
    + sep(236, 14, 218) + g.axes(it('a'), it('E'), 0, 0) + g.courbe(x => 1 / (x * x), .3, 5, 'pt') + g.courbe(x => -2 / x, .3, 5, 'pt') + g.courbe(x => 1 / (x * x) - 2 / x, .3, 5)
    + pt(g.X(1), g.Y(-1)) + L(g.X(1), g.Y(0), g.X(1), g.Y(-1), 'pt') + tick(g.X(1), g.Y(0) - 6, q('a', '0')) + tick(g.X(1) + 6, g.Y(-1) + 16, '−13,6 eV', 'start')
    + T(g.X(.75), g.Y(2.6), q('E', 'c'), 'start', 12.5) + T(g.X(1.5), g.Y(-2.4), q('E', 'p'), 'start', 12.5),
    'Atome d’hydrogène : énergie estimée en fonction de la taille a');
})();

// ---------- dispersion et amortissement ----------
const oem2C = (() => {
  const kk = u => { const re = 1, im = -1 / u, m = Math.hypot(re, im), a = Math.atan2(im, re) / 2, s = Math.sqrt(m); return [u * s * Math.cos(a), u * s * Math.sin(a)]; };
  const g = graphe(44, 28, 190, 160, [0, 3], [0, 3.1]), h = graphe(300, 28, 190, 160, [0, 12], [-1.1, 1.15]);
  return svg(520, 236, g.axes('ω/' + q('ω', '0'), '') + g.courbe(u => kk(u)[0], .01, 3) + g.courbe(u => -kk(u)[1], .01, 3, 'ptobj') + g.courbe(u => u, 0, 3, 'pt')
    + T(g.X(2.3), g.Y(2.6), it('k') + '′', 'start') + T(g.X(2.3), g.Y(.78), '−' + it('k') + '″', 'start') + T(g.X(1.4), g.Y(1.9), 'ω/' + it('c'), 'end', 12)
    + T(139, 224, '(a) ' + it('k') + '′ et ' + it('k') + '″ (unités ' + q('ω', '0') + '/' + it('c') + ')', 'middle', 12.5) + sep(262, 14, 214)
    + h.axes(it('x'), it('G'), 0, 0) + h.courbe(x => Math.exp(-.22 * x), 0, 12, 'pt') + h.courbe(x => -Math.exp(-.22 * x), 0, 12, 'pt') + h.courbe(x => Math.exp(-.22 * x) * Math.cos(2.2 * x), 0, 12, 'obj', 400)
    + vec(h.X(7), h.Y(.85), h.X(10), h.Y(.85)) + T(h.X(8.5), h.Y(.85) - 8, 'propagation', 'middle', 12) + T(395, 224, '(b) onde atténuée (' + it('k') + '′' + it('k') + '″ < 0)', 'middle', 12.5),
    'Dispersion : vecteur d’onde complexe et onde atténuée');
})();

// ---------- effet Joule dans un conducteur ----------
const oem3C = svg(430, 220, L(130, 20, 130, 176, 'epais') + hatchRect(122, 20, 8, 156) + T(250, 22, 'conducteur (γ), ' + it('z') + ' ≥ 0', 'middle', small) + T(64, 40, 'vide', 'middle', small)
  + Rect(130, 70, 270, 70, 'pt') + T(390, 64, it('a') + ' × ' + it('a') + ' × ∞', 'end', 12.5)
  + [0, 1, 2, 3, 4].map(k => vec(160 + 50 * k, 120, 160 + 50 * k, 120 - 64 * Math.exp(-k * .62))).join('') + V(176, 76, 'E', '', 'start')
  + vec(56, 104, 124, 104) + T(90, 96, '⟨' + it('Π') + '⟩', 'middle') + cote(130, 156, 180, 156) + T(155, 172, 'δ')
  + axe(30, 204, 70, 204) + T(74, 209, it('z'), 'start') + axe(30, 204, 30, 168) + T(36, 170, it('x'), 'start') + sortant(30, 204, 4) + T(22, 194, it('y'), 'end')
  + T(300, 196, '⟨𝒫⟩ = γ' + q('E', '0') + sup('2') + it('a') + sup('2') + 'δ/4', 'middle', small),
  'Conducteur : pénétration de l’onde et puissance dissipée');

// ---------- ionosphère ----------
const plasmaC = svg(440, 236, P('M0,214 Q220,168 440,214') + `<path d="M0,214 Q220,168 440,214 L440,236 L0,236 Z" fill="url(#an-h)" stroke="none"/>` + T(220, 228, 'Terre', 'middle', 12.5)
  + L(0, 56, 440, 56, 'pt') + L(0, 86, 440, 86, 'pt') + T(430, 74, 'ionosphère', 'end', 12.5)
  + L(40, 200, 130, 92) + mid(40, 200, 130, 92) + L(130, 92, 220, 192) + mid(130, 92, 220, 192) + T(70, 128, it('f') + ' < ' + q('f', 'p'), 'end', small) + T(130, 108, 'réfléchie', 'middle', 12)
  + L(260, 188, 330, 14) + mid(260, 188, 330, 14) + T(316, 120, it('f') + ' > ' + q('f', 'p'), 'start', small) + T(338, 24, 'transmise', 'start', 12)
  + cote(400, 190, 400, 86) + T(394, 142, it('h'), 'end'),
  'Ionosphère : réflexion des ondes de basse fréquence');

// ---------- transparence UV ----------
const oem5C = (() => {
  const g = graphe(50, 24, 290, 170, [0, 3], [-3, 1.3]);
  return svg(380, 226, g.axes('ω', it('n') + sup('2'), 0, 0) + g.courbe(u => 1 - 1 / (u * u), .5, 3) + g.hl(1, 'pt') + tick(g.X(0) - 5, g.Y(1) + 4, '1', 'end')
    + g.vl(1, 'pt', -3, 1) + tick(g.X(1) + 6, g.Y(0) + 15, q('ω', 'p'), 'start')
    + T(g.X(.55), g.Y(-1.2), it('n') + sup('2') + ' < 0', 'end', 12.5) + T(g.X(.55), g.Y(-1.6), 'réflexion', 'end', 12.5) + T(g.X(1.9), g.Y(.45), 'transparent (UV)', 'start', 12.5),
    'Métal : carré de l’indice en fonction de ω');
})();

export const LOT5 = [
  {id: 'n-p2-marche', type: 'enonce', titre: 'Marche de potentiel', legende: 'V = 0 pour x < 0 et V = V₀ pour x > 0 ; électrons d’énergie E venant de x < 0', svg: marcheE},
  {id: 'n-p2-marche', type: 'correction', titre: 'Marche de potentiel', legende: '(a) E > V₀ : incidente et réfléchie (k₁) à gauche, transmise (k₂ < k₁, longueur d’onde plus grande) à droite. (b) E < V₀ : onde évanescente en e^(−κx), réflexion totale', svg: marcheC},
  {id: 'n-p2-voile', type: 'enonce', titre: 'Voile solaire', legende: 'Voile plane parfaitement réfléchissante, de surface S, face au Soleil (incidence normale), recevant le flux φ', svg: voileE},
  {id: 'n-p2-voile', type: 'correction', titre: 'Voile solaire', legende: 'Chaque photon arrive avec (ε/c)u et repart avec −(ε/c)u : la voile reçoit 2ε/c, d’où la force F = 2φS/c et la pression 2φ/c', svg: voileC},
  {id: 'n-p1-photo', type: 'correction', titre: 'Effet photoélectrique', legende: 'Le photon (hν ≈ 4,9 eV) fournit le travail d’extraction W = 4,3 eV ; le reste est l’énergie cinétique maximale E_c ≈ 0,58 eV', svg: photoC},
  {id: 'n-p1-puits', type: 'correction', titre: 'Électron confiné', legende: 'Puits infini [0, L] : niveaux Eₙ = n²E₁ et fonctions d’onde sin(nπx/L) ; la transition 1 → 2 absorbe un photon de 275 nm', svg: puitsC},
  {id: 'p-q-1', type: 'correction', titre: 'Particule sur un cercle', legende: 'La fonction d’onde reprend sa valeur après un tour : ψ(θ + 2π) = ψ(θ), d’où ψₙ ∝ e^(inθ) (tireté : partie réelle pour n = 3)', svg: q1C},
  {id: 'p-q-3', type: 'correction', titre: 'Oscillateur harmonique', legende: 'Potentiel V = ½mω₀²x², niveau E₀ = ħω₀/2 et fondamental gaussien ψ₀ (tireté), qui déborde au-delà des points de rebroussement classiques ±x_c', svg: q3C},
  {id: 'p-q-2', type: 'correction', titre: 'Potentiel hyperbolique', legende: 'V = −λ/x avec paroi infinie en 0 ; niveau E = −mλ²/(2ħ²) ; la zone classiquement accessible est 0 < x < 2/k ; φ = Cx e^(−kx) (tireté)', svg: q2C},
  {id: 'n-p2-bohr', type: 'correction', titre: 'Taille de l’atome d’hydrogène', legende: 'Électron confiné dans une région de taille a : E(a) = ħ²/(2mₑa²) − e²/(4πε₀a), minimale en a₀ ≈ 53 pm où E ≈ −13,6 eV', svg: bohrC},
  {id: 'p-oem-2', type: 'correction', titre: 'Dispersion et amortissement', legende: '(a) k = k′ + ik″ avec k′ > 0 et k″ < 0 ; à haute fréquence k′ → ω/c et k″ → −ω₀/(2c). (b) L’onde progresse vers x > 0 en s’atténuant', svg: oem2C},
  {id: 'p-oem-3', type: 'correction', titre: 'Effet Joule dans un conducteur', legende: 'Le vecteur de Poynting entre dans le conducteur ; E (selon u_x) décroît sur δ ; la puissance Joule moyenne dans a × a × ∞ vaut γE₀²a²δ/4', svg: oem3C},
  {id: 'n-p2-plasma', type: 'correction', titre: 'Ionosphère et ondes radio', legende: 'Les ondes de fréquence f < f_p ≈ 9 MHz sont réfléchies par l’ionosphère (liaisons lointaines) ; les plus hautes la traversent (satellites)', svg: plasmaC},
  {id: 'p-oem-5', type: 'correction', titre: 'Transparence UV des métaux', legende: 'Pour τω ≫ 1, n² ≈ 1 − ω_p²/ω² : n² < 0 sous ω_p (réflexion, le métal brille), n² > 0 au-delà (transparent dans l’UV, λ < 0,2 µm)', svg: oem5C},
];
