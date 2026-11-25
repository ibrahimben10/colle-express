// Défis du jour et de la semaine : choisis de façon déterministe (les mêmes pour tous ce jour-là),
// validés uniquement par du travail enregistré dans le suivi (synchronisé avec le compte) :
// exercice coché « fait » ou réponse soumise. Ouvrir un énoncé ne suffit jamais.
import { esc } from './format.js';
import { ic } from './icons.js';

const pad = n => String(n).padStart(2, '0');
const jour = t => { const d = new Date(t); return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`; };
function lundi(t = Date.now()) { const d = new Date(t); d.setHours(0, 0, 0, 0); d.setDate(d.getDate() - ((d.getDay() + 6) % 7)); return d.getTime(); }
const hash = s => { let h = 2166136261; for (const c of String(s)) h = Math.imul(h ^ c.charCodeAt(0), 16777619); return h >>> 0; };
const choisir = (pool, n, graine) => { const L = [...pool], out = []; let h = hash(graine); while (out.length < n && L.length) { out.push(L.splice(h % L.length, 1)[0]); h = hash(h + 'x'); } return out; };

/* Ce qui a été fait, et quand : coché « fait » (df) ou réponse soumise (journal). */
function travaux(S) {
  const L = [];
  for (const [id, v] of Object.entries(S.ex || {})) if (v.fin && v.df) L.push({id, d: v.df, i: v.i || 0, k: 'fait'});
  for (const j of S.journal || []) if (j.k === 'reponse' && j.d) L.push({id: j.id, d: j.d, i: S.ex?.[j.id]?.i || 0, k: 'reponse'});
  return L;
}

export function defis({S, byId, pick, lvl}) {
  const T = travaux(S), today = jour(Date.now()), w0 = lundi();
  const auj = T.filter(x => jour(x.d) === today), sem = T.filter(x => x.d >= w0);
  const ids = L => [...new Set(L.map(x => x.id))];
  const chapsAvant = new Set(T.filter(x => jour(x.d) !== today).map(x => byId(x.id)?.chap).filter(Boolean));
  const D = [
    {id: 'jour', titre: 'L’exercice du jour', detail: pick ? pick.titre : '—', open: pick?.id, cible: 1, val: pick && auj.some(x => x.id === pick.id) ? 1 : 0},
    {id: 'sans', titre: 'Sans filet', detail: 'Un exercice fait aujourd’hui sans aucun indice', cible: 1, val: auj.some(x => x.i === 0) ? 1 : 0},
    {id: 'neuf', titre: 'Terre inconnue', detail: 'Un exercice d’un chapitre jamais travaillé', cible: 1, val: auj.some(x => !chapsAvant.has(byId(x.id)?.chap)) ? 1 : 0}
  ];
  const W = [
    {id: 'cinq', titre: 'Cinq colles', detail: '5 exercices faits cette semaine', cible: 5, val: ids(sem).length},
    {id: 'chap', titre: 'Tour d’horizon', detail: '3 chapitres différents cette semaine', cible: 3, val: new Set(ids(sem).map(i => byId(i)?.chap).filter(Boolean)).size},
    {id: 'rep', titre: 'Au tableau', detail: 'Soumettre une réponse à ton groupe', cible: 1, val: ids(sem.filter(x => x.k === 'reponse')).length},
    {id: 'haut', titre: 'Viser plus haut', detail: `2 exercices d’un niveau au-dessus du tien`, cible: 2, val: ids(sem).filter(i => (byId(i)?.niveau || 0) > lvl).length, si: lvl < 3},
    {id: 'mix', titre: 'Les deux faces', detail: 'Un exercice de maths et un de physique-chimie', cible: 2, val: (ids(sem).some(i => byId(i)?.mat === 'Maths') ? 1 : 0) + (ids(sem).some(i => byId(i) && byId(i).mat !== 'Maths') ? 1 : 0)}
  ].filter(x => x.si !== false);
  return {jour: choisir(D, 2, today), semaine: choisir(W, 3, 'S' + jour(w0)), cle: today, cleS: jour(w0)};
}

export function defisHTML(R, {compact = false} = {}) {
  const one = d => { const ok = d.val >= d.cible, v = Math.min(d.val, d.cible);
    return `<li class="df ${ok ? 'ok' : ''}" data-df="${d.id}"><span class="df-ck" aria-hidden="true">${ok ? ic('check') : ''}</span>
      <div><b>${esc(d.titre)}</b>${d.open && !ok ? `<button class="linkbtn df-go" data-open="${esc(d.open)}">${esc(d.detail)}</button>` : `<span class="small">${esc(d.detail)}</span>`}</div>
      <span class="df-n mono" aria-label="${v} sur ${d.cible}">${d.cible > 1 ? `${v}/${d.cible}` : ok ? 'fait' : ''}</span>${d.cible > 1 ? `<span class="df-bar"><i style="width:${(100 * v / d.cible).toFixed(0)}%"></i></span>` : ''}</li>`; };
  const fin = new Date(lundi() + 7 * 864e5 - 1);
  return `<div class="dfs${compact ? ' compact' : ''}">
    <div><h4>${ic('target')} Aujourd’hui</h4><ul>${R.jour.map(one).join('')}</ul></div>
    <div><h4>${ic('chart')} Cette semaine <span class="small">jusqu’au ${fin.toLocaleDateString('fr-FR', {weekday: 'long', day: 'numeric'})}</span></h4><ul>${R.semaine.map(one).join('')}</ul></div>
  </div>`;
}

/* Défis nouvellement réussis depuis la dernière visite (pour une petite célébration, une seule fois). */
export function nouveaux(R, store) {
  const vus = new Set(store.get('defis-ok', [])), neufs = [];
  for (const d of [...R.jour.map(x => ({...x, k: R.cle + ':' + x.id})), ...R.semaine.map(x => ({...x, k: R.cleS + ':' + x.id}))])
    if (d.val >= d.cible && !vus.has(d.k)) { neufs.push(d); vus.add(d.k); }
  store.set('defis-ok', [...vus].slice(-60));
  return neufs;
}
