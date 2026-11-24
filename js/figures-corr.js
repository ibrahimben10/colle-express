// Schémas de la correction (montrés avec la correction, jamais avec l'énoncé seul).
import { FC1 } from './figc1.js';
import { FC2 } from './figc2.js';
import { ic } from './icons.js';
import { esc } from './format.js';
export const FIGC = {...FC1, ...FC2};
// Indices et exposants des légendes : T_m → T<sub>m</sub>, e^(−x/δ) → e<sup>−x/δ</sup>.
const leg = t => esc(t).replace(/\^\(([^()]*)\)/g, '<sup>$1</sup>').replace(/_([A-Za-z0-9θωρℓ]+)/g, '<sub>$1</sub>');
// Figure affichée en tête de la correction (tous les modes, et la fiche imprimable).
export const figCorr = id => FIGC[id] ? `<figure class="fig figc">${FIGC[id].svg}<figcaption>${ic('eye')}<span><b>Schéma de la correction.</b> ${leg(FIGC[id].legende)}</span></figcaption></figure>` : '';
