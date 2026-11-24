// Schémas de la correction (montrés avec la correction, jamais avec l'énoncé seul).
import { AN, anSlot, legHTML as leg } from './figures-annale.js';
import { ic } from './icons.js';
export const FIGC = Object.fromEntries(Object.entries(AN).filter(([, v]) => 'c' in v).map(([id, v]) => [id, {legende: v.c, svg: anSlot(id, 'c')}]));
// Figure affichée en tête de la correction (tous les modes, et la fiche imprimable).
export const figCorr = id => FIGC[id] ? `<figure class="fig figc">${FIGC[id].svg}<figcaption>${ic('eye')}<span><b>Schéma de la correction.</b> ${leg(FIGC[id].legende)}</span></figcaption></figure>` : '';
