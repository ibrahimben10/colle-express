// Présentation de l'auteur du site (page de connexion, onglet « À propos »).
import { CONFIG } from './config.js';
import { ic } from './icons.js';
import { esc } from './format.js';

const P = CONFIG.PRESENTATION || {};
const initials = n => P.initiales || n.split(/\s+/).filter(Boolean).slice(0, 2).map(w => w[0]).join('').toUpperCase();

// Version courte, sur le tableau noir de la page d'accueil.
export function presentationCourte() {
  if (!P.accroche) return '';
  return `<div class="about-mini"><span class="avatar-xl">${esc(initials(CONFIG.NOM_PROF))}</span>
    <div><b>${esc(CONFIG.NOM_PROF)}</b><span>${esc(P.accroche)}</span></div></div>`;
}

// Page complète.
export function presentationPage() {
  const link = P.contact ? (P.contact.includes('@') && !P.contact.startsWith('http') ? 'mailto:' + P.contact : P.contact) : '';
  return `
  <div class="about">
    <div class="about-card panel">
      <div class="about-id">
        <span class="avatar-xl">${esc(initials(CONFIG.NOM_PROF))}</span>
        <div><h2>${esc(CONFIG.NOM_PROF)}</h2><p class="about-acc">${ic('cap')} ${esc(P.accroche || '')}</p></div>
      </div>
      ${(P.texte || []).map(t => `<p>${esc(t)}</p>`).join('')}
      ${link ? `<a class="btn" href="${esc(link)}" target="_blank" rel="noopener">${ic('msg')} Me contacter</a>` : ''}
    </div>
    <div class="about-side">
      <h3 class="sec">${ic('clock')} Mon parcours</h3>
      <ol class="timeline panel">${(P.parcours || []).map(e => `
        <li><span class="tl-ic">${ic(e.ic || 'star')}</span>
          <div><span class="tl-q">${esc(e.quand || '')}</span><b>${esc(e.quoi || '')}</b>${e.ou ? `<small>${esc(e.ou)}</small>` : ''}</div></li>`).join('')}
      </ol>
      ${(P.pourquoi || []).length ? `<h3 class="sec">${ic('target')} Ce que tu trouveras ici</h3>
      <ul class="about-list panel">${P.pourquoi.map(t => `<li>${ic('check')}<span>${esc(t)}</span></li>`).join('')}</ul>` : ''}
    </div>
  </div>`;
}
