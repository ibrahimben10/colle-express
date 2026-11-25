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
export function presentationPage(u = {}) {
  const tel = (P.telephone || '').replace(/[^+\d]/g, '');
  const contact = (P.email || P.telephone) ? `<div class="about-contact">
      ${P.email ? `<a class="btn" href="mailto:${esc(P.email)}">${ic('msg')}<span>${esc(P.email)}</span></a>` : ''}
      ${P.telephone ? `<a class="btn" href="tel:${esc(tel)}">${ic('phone')}<span>${esc(P.telephone)}</span></a>` : ''}
    </div>` : '';
  return `
  <div class="about">
    <div class="about-card panel">
      <div class="about-id">
        <span class="avatar-xl">${esc(initials(CONFIG.NOM_PROF))}</span>
        <div><h2>${esc(CONFIG.NOM_PROF)}</h2><p class="about-acc">${ic('cap')} ${esc(P.accroche || '')}</p></div>
      </div>
      ${(P.texte || []).map(t => `<p>${esc(t)}</p>`).join('')}
      ${contact ? `<h3 class="sec" style="margin-top:18px">${ic('msg')} Me contacter</h3>${contact}` : ''}
    </div>
    ${envoiForm(u)}
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

// Formulaire d'envoi de sujets d'oraux : le PDF arrive en pièce jointe dans la boîte de CONFIG.ENVOI_EMAIL (service FormSubmit).
function envoiForm(u) {
  const dest = CONFIG.ENVOI_EMAIL || P.email;
  if (!dest) return '';
  return `<section class="panel envoi" id="envoi">
    <h3 class="sec">${ic('upload')} Enrichir la plateforme</h3>
    ${u.merci ? `<div class="ok">${ic('check')} Merci ! Ton sujet a bien été envoyé, il sera ajouté après relecture.</div>` : ''}
    <p class="small">Tu as passé un oral, ou tu as des sujets d'oraux en PDF ? Envoie-les ici : ils arrivent directement dans ma boîte e-mail et je les ajoute au site avec indices et corrigé.</p>
    <form action="https://formsubmit.co/${esc(dest)}" method="POST" enctype="multipart/form-data">
      <input type="hidden" name="_subject" value="Colle express : nouveau sujet d'oral">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_next" value="">
      <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
      <div class="row">
        <label class="field">Ton nom<input name="nom" required maxlength="80" value="${esc(u.nom || '')}"></label>
        <label class="field">Ton e-mail<input type="email" name="email" required value="${esc(u.email || '')}"></label>
      </div>
      <div class="row">
        <label class="field">Concours<select name="concours"><option>CCINP</option><option>Mines-Télécom</option><option>Mines-Ponts</option><option>Centrale-Supélec</option><option>X-ENS</option><option>Autre / plusieurs</option></select></label>
        <label class="field">Matière<select name="matiere"><option>Maths</option><option>Physique</option><option>Chimie</option><option>Informatique</option><option>Plusieurs</option></select></label>
      </div>
      <label class="field">Fichier PDF (10 Mo max.)<input type="file" name="attachment" accept="application/pdf,.pdf" required></label>
      <label class="field">Message (année, remarques…)<textarea name="message" rows="3" maxlength="2000"></textarea></label>
      <div class="err"></div>
      <button class="btn primary" type="submit">${ic('upload')} Envoyer le sujet</button>
    </form>
  </section>`;
}
