// Progression : points d'expérience (XP), niveaux et jalons.
// Tout est calculé à partir des statistiques publiques du profil (les mêmes partout : tableau de bord,
// profil personnel, profil vu par les autres). On récompense le travail réel, jamais les clics :
// ouvrir un exercice ou le corrigé ne rapporte rien.
import { esc } from './format.js';
import { ic } from './icons.js';

export const BAREME = [
  ['reussis', 40, 'par exercice réussi (≥ 12/20 de moyenne, au moins 2 notes de pairs)'],
  ['termines', 20, 'par réponse soumise sur l’honneur'],
  ['sansAide', 10, 'bonus si la réponse a été soumise sans indice ni corrigé'],
  ['travailles', 5, 'par exercice travaillé (indice demandé ou réponse)'],
  ['jours', 3, 'par jour actif']
];
// Les paliers reprennent l'argot des prépas : on monte d'une année… ou d'un rang.
export const PALIERS = [[0, 'Bizuth'], [150, 'Taupin'], [450, 'Carré'], [1000, 'Cube'], [2000, 'Bicarré'], [3500, 'Major']];

export const xpDe = S => BAREME.reduce((a, [k, v]) => a + v * (S[k] || 0), 0);
export function niveau(xp) {
  let i = 0; while (i + 1 < PALIERS.length && xp >= PALIERS[i + 1][0]) i++;
  const [min, nom] = PALIERS[i], nx = PALIERS[i + 1];
  return {i: i + 1, nom, min, next: nx?.[0] ?? null, nextNom: nx?.[1] ?? null, pct: nx ? (xp - min) / (nx[0] - min) : 1};
}

/* Jalons : critères publics, calculés sur les exercices réussis (liste publique du profil). */
export function jalons(p, byId, domaine) {
  const ok = (p.reussis || []).map(byId).filter(Boolean), S = p._S || {};
  const dom = d => ok.filter(e => domaine(e) === d).length;
  const alg = ok.filter(e => /algèbre linéaire|réduction|matric|espaces? vect/i.test(e.chap)).length;
  return [
    {id: 'j-premier', titre: 'Première réussite', critere: 'Un exercice validé par tes pairs', val: ok.length, cible: 1, icon: 'trophy'},
    {id: 'j-dix', titre: 'Sans filet', critere: '10 réponses soumises sans indice ni corrigé', val: S.sansAide || 0, cible: 10, icon: 'target'},
    {id: 'j-meca', titre: 'Spécialiste de mécanique', critere: '5 exercices de mécanique réussis', val: dom('Mécanique'), cible: 5, icon: 'pendulum'},
    {id: 'j-alg', titre: 'Mordu d’algèbre linéaire', critere: '5 exercices d’algèbre linéaire ou de réduction réussis', val: alg, cible: 5, icon: 'matrix'},
    {id: 'j-cent', titre: 'Centurion', critere: '100 exercices travaillés', val: S.travailles || 0, cible: 100, icon: 'book'}
  ];
}

/* Carte de niveau (tableau de bord, profil) */
export function niveauHTML(S, {self = false, compact = false} = {}) {
  const xp = xpDe(S), n = niveau(xp);
  const ring = 2 * Math.PI * 26, off = ring * (1 - n.pct);
  return `<div class="lvlcard${compact ? ' compact' : ''}">
    <svg class="lvl-ring" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="26" class="trk"/><circle cx="32" cy="32" r="26" class="arc" style="stroke-dasharray:${ring.toFixed(1)};stroke-dashoffset:${off.toFixed(1)}"/><text x="32" y="38" text-anchor="middle">${n.i}</text></svg>
    <div class="lvl-txt"><span class="k">Niveau ${n.i}</span><b>${esc(n.nom)}</b>
      <span class="small"><b class="xpn" data-n="${xp}">${xp}</b> XP${n.next ? ` · encore ${n.next - xp} pour <i>${esc(n.nextNom)}</i>` : ' · palier maximal'}</span></div>
    ${compact ? '' : `<details class="lvl-how"><summary>${self ? 'Comment gagner des XP ?' : 'Comment sont comptés les XP ?'}</summary><ul>${BAREME.map(([k, v, l]) => `<li><b>+${v}</b> ${l}</li>`).join('')}</ul>
      <p class="small">Ouvrir un énoncé ou un corrigé ne rapporte rien : seul le travail compte. Paliers : ${PALIERS.map(([m, nm]) => `${nm} (${m})`).join(' · ')}.</p></details>`}
  </div>`;
}

export function jalonsHTML(L, self) {
  const one = j => { const done = j.val >= j.cible, pct = Math.min(1, j.val / j.cible);
    return `<li class="jal ${done ? 'ok' : ''}"><span class="jal-ic">${ic(j.icon)}</span><div><b>${esc(j.titre)}</b><span class="small">${esc(j.critere)}</span>
      ${done ? '' : `<span class="jal-bar" role="img" aria-label="${Math.min(j.val, j.cible)} sur ${j.cible}"><i style="width:${(100 * pct).toFixed(0)}%"></i></span><span class="mono">${Math.min(j.val, j.cible)} / ${j.cible}</span>`}</div></li>`; };
  const ok = L.filter(j => j.val >= j.cible), ko = L.filter(j => j.val < j.cible);
  if (!self && !ok.length) return '';
  return `<ul class="jals">${ok.map(one).join('')}${self ? ko.map(one).join('') : ''}</ul>`;
}
