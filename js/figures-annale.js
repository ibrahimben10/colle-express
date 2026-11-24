// Schémas « annale » : SVG chargés à la demande depuis annale/svg/ et insérés dans la page
// (insertion directe, pour que les traits prennent la couleur du texte en mode clair comme en sombre).
import { AN } from './figures-annale-index.js';
export { AN };
import { esc } from './format.js';
// Légendes : T_m → T<sub>m</sub>, e^(−x/δ) → e<sup>−x/δ</sup>.
export const legHTML = t => esc(t).replace(/\^\(([^()]*)\)/g, '<sup>$1</sup>').replace(/_([A-Za-z0-9θωρℓ]+)/g, '<sub>$1</sub>');

const cache = {}, pending = new Set();
const url = k => new URL(`../annale/svg/${k}.svg`, import.meta.url);
export const anSlot = (id, t) => `<span class="an-svg" data-an="${id}-${t === 'e' ? 'enonce' : 'correction'}"></span>`;

function hydrate(el) {
  if (el.dataset.ok) return; el.dataset.ok = '1';
  const k = el.dataset.an;
  const p = (cache[k] ||= fetch(url(k)).then(r => r.ok ? r.text() : '').then(t => t.replace(/^<\?xml[^>]*>\s*/, '')).then(t => t.startsWith('<svg') ? t : '').catch(() => ''));
  pending.add(p);
  p.then(t => { el.innerHTML = t; if (!t) el.remove(); }).finally(() => pending.delete(p));
}
const scan = root => root.querySelectorAll?.('.an-svg:not([data-ok])').forEach(hydrate);
// Toute figure ajoutée à la page est complétée automatiquement.
new MutationObserver(ms => { for (const m of ms) for (const nd of m.addedNodes) if (nd.nodeType === 1) { if (nd.matches('.an-svg')) hydrate(nd); else scan(nd); } })
  .observe(document.documentElement, {childList: true, subtree: true});
scan(document);
// Attend que les schémas affichés soient chargés (impression, PDF).
export const anReady = async () => { while (pending.size) await Promise.all([...pending]); };
