// Interface d'authentification : connexion, inscription, mot de passe oublié, nouveau mot de passe.
// Règles : validation avant tout appel réseau, un seul envoi à la fois, confirmation affichée
// uniquement après acceptation par le serveur, messages neutres (aucune énumération de comptes).
import { api, AuthFail, DEMO } from './api.js';
import { emailValide, motDePasseErreur, force, PW_MIN } from './validation.js';
import { busy, toast, reveal } from './ui.js';

const $ = s => document.querySelector(s);

export const MSG = {
  invalid_email: 'Veuillez saisir une adresse email valide.',
  missing_password: 'Saisissez votre mot de passe.',
  missing_name: 'Indiquez votre prénom et votre nom.',
  missing_code: 'Saisissez le code de classe qui vous a été communiqué.',
  mismatch: 'Les deux mots de passe ne sont pas identiques.',
  invalid_credentials: 'Adresse e-mail ou mot de passe incorrect.',
  email_not_confirmed: 'Confirmez d’abord votre adresse grâce à l’e-mail reçu à l’inscription.',
  rate_limit: 'Trop de demandes en peu de temps. Patientez quelques minutes avant de réessayer.',
  server: 'Impossible de traiter votre demande pour le moment. Veuillez réessayer ultérieurement.',
  email_send: 'L’e-mail n’a pas pu être envoyé pour le moment (problème d’envoi côté serveur). Réessayez plus tard ; si cela persiste, prévenez l’administrateur du site.',
  demo: 'Mode démonstration : aucun e-mail ne peut être envoyé tant que Supabase n’est pas configuré.',
  bad_class_code: 'Code de classe invalide. Vérifiez-le auprès de la personne qui vous l’a donné.',
  signup_refused: 'Impossible de créer un compte avec cette adresse. Si vous avez déjà un compte, connectez-vous ou réinitialisez votre mot de passe.',
  weak_password: `Le mot de passe doit contenir au moins ${PW_MIN} caractères, dont une lettre et un chiffre.`,
  same_password: 'Le nouveau mot de passe doit être différent de l’ancien.',
  link_invalid: 'Ce lien de réinitialisation est invalide ou a déjà été utilisé. Demandez un nouveau lien ci-dessous.',
  link_expired: 'Ce lien de réinitialisation a expiré. Demandez un nouveau lien ci-dessous.',
  email_link: 'Ce lien a expiré ou a déjà été utilisé (il ne fonctionne qu’une fois). Si vous veniez de confirmer votre adresse, connectez-vous simplement ; sinon, utilisez « Mot de passe oublié ? ».',
  confirm_sent: 'E-mail de confirmation renvoyé. Ouvrez le lien qu’il contient (pensez aux spams), puis connectez-vous.',
  reset_sent: 'Si un compte est associé à cette adresse, vous recevrez un lien de réinitialisation.',
  signup_confirm: 'Compte presque prêt : ouvrez l’e-mail de confirmation que nous venons de vous envoyer, puis connectez-vous.',
};
const HEAD = {
  in: ['Bon retour !', 'Connectez-vous pour retrouver vos exercices, vos groupes et votre suivi.'],
  up: ['Créer votre compte', 'Gratuit. Il vous faut seulement le code de classe qui vous a été communiqué.'],
  forgot: ['Mot de passe oublié', 'Indiquez votre adresse : vous recevrez un lien sécurisé, temporaire et utilisable une seule fois.'],
  new: ['Nouveau mot de passe', `Choisissez un mot de passe d’au moins ${PW_MIN} caractères, avec au moins une lettre et un chiffre.`],
};

/* ---------- limitation des tentatives (complément des limites serveur de Supabase) ---------- */
const LOCK_KEY = 'ce:auth-lock', RESET_KEY = 'ce:reset-at', RESET_WAIT = 60;
const rd = (k, d) => { try { return JSON.parse(localStorage.getItem(k)) ?? d; } catch { return d; } };
const wr = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} };
const lockLeft = () => Math.max(0, Math.ceil(((rd(LOCK_KEY, {}).until || 0) - Date.now()) / 1000));
function noteFail() {
  const l = rd(LOCK_KEY, {fails: 0, level: 0});
  l.fails = (l.fails || 0) + 1;
  if (l.fails >= 5) { l.until = Date.now() + 30000 * 2 ** Math.min(l.level || 0, 5); l.level = (l.level || 0) + 1; l.fails = 0; }
  wr(LOCK_KEY, l);
}
const resetLeft = () => Math.max(0, RESET_WAIT - Math.floor((Date.now() - (rd(RESET_KEY, 0) || 0)) / 1000));

/* ---------- affichage ---------- */
let mode = 'in', onDone = () => {};
function setAlert(kind, text) {
  const a = $('#authAlert');
  if (!text) { a.hidden = true; a.textContent = ''; return; }
  a.hidden = false; a.className = 'alert ' + kind;
  a.setAttribute('role', kind === 'error' ? 'alert' : 'status');
  a.innerHTML = `<span class="alert-ic" aria-hidden="true">${kind === 'error' ? '!' : kind === 'ok' ? '✓' : 'i'}</span><span></span>`;
  a.lastChild.textContent = text;
}
function fieldErr(input, text) {
  const p = document.getElementById(input.id + 'E');
  input.setAttribute('aria-invalid', text ? 'true' : 'false');
  input.closest('.fld')?.classList.toggle('bad', !!text);
  if (p) p.textContent = text || '';
}
function clearErrs(form) { form.querySelectorAll('input, select').forEach(i => fieldErr(i, '')); }

export function showAuth(m = 'in', {alert, kind = 'error'} = {}) {
  mode = m;
  $('#app').hidden = true; $('#auth').hidden = false;
  document.body.classList.add('on-landing');
  for (const [k, id] of [['in', 'fIn'], ['up', 'fUp'], ['forgot', 'fForgot'], ['new', 'fNew']]) $('#' + id).hidden = k !== m;
  const tabs = m === 'in' || m === 'up';
  $('#atabs').hidden = !tabs;
  $('#tIn').setAttribute('aria-selected', m === 'in'); $('#tUp').setAttribute('aria-selected', m === 'up');
  $('#authTitle').textContent = HEAD[m][0]; $('#authSub').textContent = HEAD[m][1];
  setAlert(kind, alert || '');
  if (m === 'forgot') { const v = $('#inMail').value.trim(); if (v && !$('#fgMail').value) $('#fgMail').value = v; tickReset(); }
  if (m === 'in') tickLock();
  reveal();
}
function go(m, focus = true) {
  showAuth(m);
  if (!focus) return;
  const card = $('#authBox');
  if (card.getBoundingClientRect().top < 0 || card.getBoundingClientRect().top > innerHeight * .6) card.scrollIntoView({behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start'});
  setTimeout(() => $(`#${{in: 'fIn', up: 'fUp', forgot: 'fForgot', new: 'fNew'}[m]} input`)?.focus({preventScroll: true}), 250);
}

// Compte à rebours du bouton « Envoyer le lien » après une demande acceptée.
let resetTimer = 0;
function tickReset() {
  clearTimeout(resetTimer);
  const b = $('#fgBtn'), s = resetLeft();
  if (b.getAttribute('aria-busy')) return;
  if (s > 0) { b.disabled = true; b.querySelector('.bl').textContent = `Renvoyer dans ${s} s`; resetTimer = setTimeout(tickReset, 1000); }
  else { b.disabled = false; b.querySelector('.bl').textContent = rd(RESET_KEY, 0) ? 'Renvoyer le lien' : 'Envoyer le lien'; }
}
let lockTimer = 0;
function tickLock() {
  clearTimeout(lockTimer);
  const b = $('#inBtn'), s = lockLeft();
  if (b.getAttribute('aria-busy')) return;
  if (s > 0) { b.disabled = true; b.querySelector('.bl').textContent = `Réessayer dans ${s} s`; lockTimer = setTimeout(tickLock, 1000); }
  else { b.disabled = false; b.querySelector('.bl').textContent = 'Se connecter'; }
}

/* ---------- un seul envoi à la fois ---------- */
function guard(form, fn) {
  let inflight = false;
  form.addEventListener('submit', async e => {
    e.preventDefault();
    if (inflight) return;
    inflight = true;
    try { await fn(e); } finally { inflight = false; }
  });
}
const err = x => (x instanceof AuthFail ? x.code : 'server');

export function initAuth({ onSignedIn }) {
  onDone = onSignedIn;
  // Boutons « afficher / masquer le mot de passe »
  document.querySelectorAll('.pw').forEach(w => {
    const i = w.querySelector('input'), b = w.querySelector('.eye');
    b.onclick = () => { const show = i.type === 'password'; i.type = show ? 'text' : 'password'; b.setAttribute('aria-pressed', show); b.setAttribute('aria-label', show ? 'Masquer le mot de passe' : 'Afficher le mot de passe'); i.focus(); };
  });
  document.addEventListener('click', e => { const t = e.target.closest('[data-auth]'); if (t) { e.preventDefault(); go(t.dataset.auth); } });
  $('#tIn').onclick = () => go('in', false); $('#tUp').onclick = () => go('up', false);
  // Les erreurs disparaissent dès que l'on corrige le champ.
  document.querySelectorAll('#auth form input').forEach(i => i.addEventListener('input', () => fieldErr(i, '')));
  $('#upPass').addEventListener('input', () => meter($('#upPass').value, '#upMeter'));
  $('#newPass').addEventListener('input', () => meter($('#newPass').value, '#newMeter'));

  /* Connexion */
  guard($('#fIn'), async () => {
    const f = $('#fIn'), mail = $('#inMail'), pass = $('#inPass');
    clearErrs(f); setAlert();
    let ok = true;
    if (!emailValide(mail.value)) { fieldErr(mail, MSG.invalid_email); ok = false; }
    if (!pass.value) { fieldErr(pass, MSG.missing_password); ok = false; }
    if (!ok) { f.querySelector('[aria-invalid=true]').focus(); return; }
    if (lockLeft()) return tickLock();
    const done = busy($('#inBtn'), 'Connexion…');
    try { await api.signIn(mail.value, pass.value); wr(LOCK_KEY, {fails: 0, level: 0}); done(); }
    catch (x) {
      done();
      const c = err(x);
      if (c === 'invalid_credentials') noteFail();
      if (c === 'invalid_email') fieldErr(mail, MSG.invalid_email); else setAlert('error', MSG[c] || MSG.server);
      if (c === 'email_not_confirmed') offerResend(mail.value);
      tickLock();
    }
  });

  /* Inscription */
  guard($('#fUp'), async () => {
    const f = $('#fUp'), name = $('#upName'), mail = $('#upMail'), pass = $('#upPass'), code = $('#upCode');
    clearErrs(f); setAlert();
    const checks = [[name, name.value.trim().length >= 2 ? '' : MSG.missing_name], [mail, emailValide(mail.value) ? '' : MSG.invalid_email],
      [pass, motDePasseErreur(pass.value)], [code, code.value.trim() ? '' : MSG.missing_code]];
    checks.forEach(([i, m]) => fieldErr(i, m));
    const bad = checks.find(c => c[1]); if (bad) { bad[0].focus(); return; }
    const done = busy($('#upBtn'), 'Création du compte…');
    try {
      const r = await api.signUp({name: name.value.trim(), email: mail.value, password: pass.value, code: code.value.trim(), niveau: +$('#upLvl').value});
      done();
      if (r === 'confirm') { setAlert('ok', MSG.signup_confirm); f.reset(); meter('', '#upMeter'); }
    } catch (x) {
      done();
      const c = err(x);
      if (c === 'invalid_email') fieldErr(mail, MSG.invalid_email);
      else if (c === 'weak_password') fieldErr(pass, x.detail || MSG.weak_password);
      else if (c === 'bad_class_code') fieldErr(code, MSG.bad_class_code);
      else setAlert('error', MSG[c] || MSG.server);
    }
  });

  /* Mot de passe oublié */
  guard($('#fForgot'), async () => {
    const f = $('#fForgot'), mail = $('#fgMail');
    clearErrs(f); setAlert();
    // Cas 1 : format invalide → aucune requête.
    if (!emailValide(mail.value)) { fieldErr(mail, MSG.invalid_email); mail.focus(); return; }
    if (resetLeft()) return tickReset();
    const done = busy($('#fgBtn'), 'Envoi en cours…');
    try {
      await api.resetPassword(mail.value);        // Cas 2 : ne se résout que si le serveur accepte
      wr(RESET_KEY, Date.now());
      done(); setAlert('ok', MSG.reset_sent);
    } catch (x) {
      done();
      const c = err(x);                             // Cas 3 : jamais de confirmation en cas d'erreur
      if (c === 'invalid_email') { fieldErr(mail, MSG.invalid_email); mail.focus(); }
      else setAlert('error', MSG[c] || MSG.server);
    }
    tickReset();
  });

  /* Nouveau mot de passe (arrivée par le lien de l'e-mail) */
  guard($('#fNew'), async () => {
    const f = $('#fNew'), p1 = $('#newPass'), p2 = $('#newPass2');
    clearErrs(f); setAlert();
    const e1 = motDePasseErreur(p1.value);
    if (e1) { fieldErr(p1, e1); p1.focus(); return; }
    if (p1.value !== p2.value) { fieldErr(p2, MSG.mismatch); p2.focus(); return; }
    const done = busy($('#newBtn'), 'Enregistrement…');
    try {
      await api.updatePassword(p1.value);
      done(); f.reset(); meter('', '#newMeter');
      toast('Mot de passe mis à jour. Bienvenue !', 'ok');
      onDone();
    } catch (x) {
      done();
      const c = err(x);
      if (c === 'weak_password') fieldErr(p1, x.detail || MSG.weak_password);
      else if (c === 'same_password') fieldErr(p1, MSG.same_password);
      else if (c === 'link_invalid' || c === 'link_expired') showAuth('forgot', {alert: MSG[c]});
      else setAlert('error', MSG[c] || MSG.server);
    }
  });
  if (DEMO) $('#fgDemo').hidden = false;
}

// Bouton « Renvoyer l'e-mail de confirmation » sous l'alerte (connexion refusée : adresse non confirmée).
let resending = false;
function offerResend(email) {
  const a = $('#authAlert'), b = document.createElement('button');
  b.type = 'button'; b.className = 'alink'; b.id = 'resendBtn'; b.textContent = 'Renvoyer l’e-mail de confirmation';
  a.lastChild.append(document.createElement('br'), b);
  b.onclick = async () => {
    if (resending) return;
    const wait = Math.max(0, 60 - Math.floor((Date.now() - (rd('ce:confirm-at', 0) || 0)) / 1000));
    if (wait) { b.textContent = `Patientez ${wait} s avant un nouvel envoi`; return; }
    resending = true; const done = busy(b, 'Envoi…');
    try { await api.resendConfirmation(email); wr('ce:confirm-at', Date.now()); done(); setAlert('ok', MSG.confirm_sent); }
    catch (x) { done(); setAlert('error', MSG[err(x)] || MSG.server); }
    resending = false;
  };
}

function meter(pw, sel) {
  const m = $(sel); if (!m) return;
  const f = pw ? Math.max(1, force(pw)) : 0;
  m.dataset.f = f;
  m.querySelector('span').textContent = pw ? ['', 'Faible', 'Moyen', 'Bon', 'Excellent'][f] : '';
}
