// Couche de données : Supabase en production, navigateur (localStorage) en mode démonstration.
import { CONFIG } from './config.js';
import { emailValide, motDePasseErreur } from './validation.js';

export const DEMO = !CONFIG.SUPABASE_URL || !CONFIG.SUPABASE_ANON_KEY;
const ls = { get(k, d) { try { const v = localStorage.getItem('ce:' + k); return v ? JSON.parse(v) : d; } catch { return d; } },
             set(k, v) { try { localStorage.setItem('ce:' + k, JSON.stringify(v)); } catch {} } };

let sb = null, channel = null;
const listeners = { auth: [], presence: [], activity: [], classe: [], config: [], banque: [], groupe: [] };
const emit = (k, v) => listeners[k].forEach(f => f(v));
const uid4 = () => (crypto.randomUUID ? crypto.randomUUID() : 'x' + Date.now() + Math.random().toString(16).slice(2));
const dataToBlob = d => { const [h, b] = d.split(','); const bin = atob(b); const u = new Uint8Array(bin.length); for (let i = 0; i < bin.length; i++) u[i] = bin.charCodeAt(i); return new Blob([u], {type: h.slice(5).split(';')[0]}); };
const errFr = e => { const m = e?.message || String(e);
  if (/duplicate key.*reponses/.test(m)) return 'Tu as déjà soumis une réponse à cet exercice dans ce groupe.';
  if (/row-level security/.test(m)) return 'Action non autorisée (rôle ou appartenance au groupe).';
  return m; };
// Mode démonstration : tout est conservé dans le navigateur.
const D = { get: () => ls.get('demo-g', {groupes: [], membres: [], reponses: [], notes: [], coms: []}), set(v) { ls.set('demo-g', v); emit('groupe'); } };
export const on = (k, f) => listeners[k].push(f);

/* ---------- profil en mode démonstration (calculé à partir des données locales) ---------- */
function demoProfil(ref, apercu, A) {
  const p = ls.get('demo-profil', {username: 'demo', public: false, matieres: []}), sv = ls.get('demo-suivi', {}), act = ls.get('demo-activite', []);
  if (ref && ref !== 'demo' && ref !== p.username) return null;
  const d = D.get(), mes = d.reponses.filter(r => r.user_id === 'demo');
  const uniq = a => [...new Set(a)];
  const jours = {};
  act.filter(a => a.kind === 'indice' || a.kind === 'reponse').forEach(a => (jours[a.jour] ||= new Set()).add(a.exercice_id));
  mes.forEach(r => (jours[r.created_at.slice(0, 10)] ||= new Set()).add(r.exercice_id));
  const vis = k => !apercu || p['vis_' + k] !== false;
  const o = {id: 'demo', username: p.username || 'demo', nom: A.profile.full_name, photo: sv.photo || '', bio: p.bio || '', etablissement: p.etablissement || '', filiere: p.filiere || '',
    annee: p.annee || null, matieres: p.matieres || [], objectif: p.objectif || '', liens: {github: p.lien_github || '', linkedin: p.lien_linkedin || '', site: p.lien_site || ''},
    public: !!p.public, self: !apercu, admin: true, role: 'admin', membre_depuis: new Date(sv.cree || Date.now()).toISOString(), contributions: ls.get('demo-contrib', 0) || 0};
  if (!apercu) o.vis = {stats: p.vis_stats !== false, activite: p.vis_activite !== false, parcours: p.vis_parcours !== false, favoris: p.vis_favoris !== false, commentaires: p.vis_commentaires !== false, etoiles: p.vis_etoiles !== false};
  if (vis('stats') || vis('parcours')) Object.assign(o, {
    vus: uniq(act.filter(a => a.kind === 'vu').map(a => a.exercice_id)),
    travailles: uniq(act.filter(a => a.kind === 'indice' || a.kind === 'reponse').map(a => a.exercice_id).concat(mes.map(r => r.exercice_id))),
    termines: uniq(mes.map(r => r.exercice_id)), sans_aide: uniq(mes.filter(r => !r.aide_consultee).map(r => r.exercice_id)),
    reussis: uniq(mes.filter(r => { const n = d.notes.filter(x => x.reponse_id === r.id); return n.length >= 2 && n.reduce((a, x) => a + x.note, 0) / n.length >= 6; }).map(r => r.exercice_id))});
  if (vis('activite')) o.jours = Object.entries(jours).map(([j, s]) => ({j, ids: [...s]})).sort((a, b) => a.j.localeCompare(b.j));
  if (vis('favoris')) o.favoris = Array.isArray(sv.fav) ? sv.fav : [];
  if (vis('commentaires')) o.commentaires = d.coms.filter(c => c.user_id === 'demo' && c.public).map(c => ({id: c.id, ex: c.exercice_id, contenu: c.contenu, d: c.created_at})).reverse();
  if (vis('etoiles')) o.etoiles = {n: 0, moy: null, mienne: null, peut_noter: false};
  return o;
}

/* ---------- erreurs d'authentification ---------- */
export class AuthFail extends Error {
  constructor(code, detail = '') { super(detail || code); this.code = code; this.detail = detail; }
}
// Adresse de retour des liens d'e-mail : la page d'accueil du site (à déclarer dans Supabase > Auth > URL Configuration).
const redirectURL = () => new URL('index.html', location.href.split('#')[0]).href;
// Une exception réseau (hors connexion, DNS…) devient une erreur classée « serveur ».
const safe = async f => { try { return await f(); } catch (e) { return {data: {}, error: e || {}}; } };
function classer(e, map = {}) {
  const code = e.code || e.name || '', st = e.status || 0, m = String(e.message || '');
  // Trace minimale pour le diagnostic (code et statut, jamais l'adresse ni le mot de passe).
  try { console.warn('[auth]', code || '-', st, m.slice(0, 120)); } catch {}
  if (map[code]) return map[code];
  if (st === 429 || /rate.?limit|too many/i.test(code + ' ' + m)) return 'rate_limit';
  if (/error sending|smtp|sending .*email/i.test(code + ' ' + m)) return 'email_send';
  if (/email_address_invalid|validation_failed/.test(code) || /invalid format|validate email|email address .* invalid/i.test(m)) return 'invalid_email';
  if (/Invalid login credentials/i.test(m)) return map.invalid_credentials || 'invalid_credentials';
  if (/Email not confirmed/i.test(m)) return map.email_not_confirmed || 'email_not_confirmed';
  if (/should be different/i.test(m)) return map.same_password || 'same_password';
  if (/Auth session missing/i.test(m)) return map.AuthSessionMissingError || 'link_invalid';
  if (/already registered/i.test(m)) return map.user_already_exists || 'signup_refused';
  if (/Password should/i.test(m)) return map.weak_password || 'weak_password';
  return 'server';
}

export const api = {
  user: null,      // {id, email}
  profile: null,   // {id, full_name, role, niveau}

  recovery: false,  // vrai quand l'utilisateur arrive par un lien de réinitialisation valide
  linkError: '',    // code d'erreur d'un lien d'e-mail expiré ou invalide

  async init() {
    if (DEMO) {
      const p = ls.get('demo-profile', null);
      if (p) { this.user = {id: p.id, email: 'demo@local'}; this.profile = p; }
      return;
    }
    // Lien reçu par e-mail : on lit l'URL AVANT que supabase-js ne la consomme,
    // pour ne jamais rater l'arrivée d'un lien de réinitialisation (ni un lien expiré).
    const h = new URLSearchParams(location.hash.slice(1)), q = new URLSearchParams(location.search);
    const err = h.get('error_code') || q.get('error_code') || h.get('error') || q.get('error');
    if (err) {
      this.linkError = 'email_link';   // lien de confirmation ou de réinitialisation expiré / déjà utilisé
      history.replaceState(null, '', location.pathname);
    }
    if (h.get('type') === 'recovery' || q.get('type') === 'recovery') this.recovery = true;

    const { createClient } = await import('https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/+esm');
    sb = createClient(CONFIG.SUPABASE_URL, CONFIG.SUPABASE_ANON_KEY);
    // Abonnement immédiat (avant getSession) : l'événement PASSWORD_RECOVERY est émis pendant l'initialisation.
    sb.auth.onAuthStateChange((ev, session) => setTimeout(async () => {
      if (ev === 'PASSWORD_RECOVERY') { this.recovery = true; if (session && session.user.id !== this.user?.id) await this._load(session.user); emit('auth', 'recovery'); return; }
      if (ev === 'SIGNED_IN' && this._ready && session && session.user.id !== this.user?.id) { await this._load(session.user); if (!this.recovery) emit('auth', 'in'); }
      if (ev === 'SIGNED_OUT') { this.user = null; this.profile = null; emit('auth', 'out'); }
    }, 0));
    const { data } = await sb.auth.getSession();
    if (data.session && !this.user) await this._load(data.session.user);
    if (this.recovery && !data.session) { this.recovery = false; this.linkError ||= 'link_invalid'; }
    if (location.hash.includes('access_token') || location.hash.includes('type=')) history.replaceState(null, '', location.pathname + '#exercices');
    this._ready = true;
  },
  async _load(u) {
    this.user = {id: u.id, email: u.email};
    const { data } = await sb.from('profiles').select('id, full_name, role, niveau').eq('id', u.id).single();
    this.profile = data || {id: u.id, full_name: u.user_metadata?.full_name || '', role: 'eleve', niveau: 1};
    sb.from('profiles').update({last_seen: new Date().toISOString()}).eq('id', u.id).then(() => {});
  },
  get isProf() { return this.profile?.role === 'prof'; },

  /* ---------- authentification ---------- */
  // Chaque échec est converti en AuthFail(code) ; les messages affichés sont choisis par l'interface
  // et ne révèlent jamais si un compte existe, ni le détail technique de l'erreur.
  async signIn(email, password) {
    if (!emailValide(email)) throw new AuthFail('invalid_email');
    if (!password) throw new AuthFail('missing_password');
    if (DEMO) return this._demo(email.split('@')[0] || 'Démo');
    const { error } = await safe(() => sb.auth.signInWithPassword({email: email.trim(), password}));
    if (error) throw new AuthFail(classer(error, {invalid_credentials: 'invalid_credentials', email_not_confirmed: 'email_not_confirmed'}));
  },
  async signUp({name, email, password, code, niveau}) {
    if (!emailValide(email)) throw new AuthFail('invalid_email');
    const pe = motDePasseErreur(password); if (pe) throw new AuthFail('weak_password', pe);
    if (DEMO) return this._demo(name, niveau);
    const { data, error } = await safe(() => sb.auth.signUp({email: email.trim(), password, options: {data: {full_name: name, code, niveau}, emailRedirectTo: redirectURL()}}));
    if (error) throw new AuthFail(/Database error|code de classe/i.test(error.message || '') ? 'bad_class_code' : classer(error, {weak_password: 'weak_password', user_already_exists: 'signup_refused', email_exists: 'signup_refused'}));
    return data.session ? 'in' : 'confirm';
  },
  async _demo(name, niveau = 1) {
    this.profile = {id: 'demo', full_name: name, role: 'prof', niveau: +niveau};
    this.user = {id: 'demo', email: 'demo@local'};
    ls.set('demo-profile', this.profile);
    emit('auth', 'in');
    return 'in';
  },
  /** Demande de lien de réinitialisation. Ne se résout QUE si Supabase a accepté la demande. */
  async resetPassword(email) {
    if (!emailValide(email)) throw new AuthFail('invalid_email');
    if (DEMO) throw new AuthFail('demo');
    const { error } = await safe(() => sb.auth.resetPasswordForEmail(email.trim(), {redirectTo: redirectURL()}));
    if (error) throw new AuthFail(classer(error));
    return true;
  },
  /** Renvoie l'e-mail de confirmation d'inscription. Ne se résout que si Supabase accepte. */
  async resendConfirmation(email) {
    if (!emailValide(email)) throw new AuthFail('invalid_email');
    if (DEMO) throw new AuthFail('demo');
    const { error } = await safe(() => sb.auth.resend({type: 'signup', email: email.trim(), options: {emailRedirectTo: redirectURL()}}));
    if (error) throw new AuthFail(classer(error));
    return true;
  },
  async updatePassword(password) {
    const pe = motDePasseErreur(password); if (pe) throw new AuthFail('weak_password', pe);
    if (DEMO) throw new AuthFail('demo');
    const { error } = await safe(() => sb.auth.updateUser({password}));
    if (error) throw new AuthFail(classer(error, {same_password: 'same_password', weak_password: 'weak_password', session_not_found: 'link_invalid', AuthSessionMissingError: 'link_invalid'}));
    this.recovery = false;
  },
  async signOut() {
    if (DEMO) { localStorage.removeItem('ce:demo-profile'); this.user = null; this.profile = null; emit('auth', 'out'); return; }
    await sb.auth.signOut();
  },

  /* ---------- profils ---------- */
  // Profil éditable de l'utilisateur connecté (ligne de la table "profils")
  async monProfil() {
    if (DEMO) return ls.get('demo-profil', {user_id: 'demo', username: 'demo', bio: '', etablissement: '', filiere: '', annee: null, matieres: [], objectif: '',
      lien_github: '', lien_linkedin: '', lien_site: '', public: false, vis_stats: true, vis_activite: true, vis_parcours: true, vis_favoris: true, vis_commentaires: true, vis_etoiles: true});
    const { data, error } = await sb.from('profils').select('*').eq('user_id', this.user.id).maybeSingle();
    if (error) throw new Error(errFr(error));
    return data;
  },
  async majProfil(champs) {
    if (DEMO) { ls.set('demo-profil', {...await this.monProfil(), ...champs}); return; }
    const { error } = await sb.from('profils').update(champs).eq('user_id', this.user.id);
    if (error) {
      if (error.code === '23505') throw new Error('Cet identifiant est déjà pris : choisis-en un autre.');
      if (error.code === '23514') throw new Error(/username/.test(error.message) ? 'Identifiant invalide : 3 à 20 caractères, lettres minuscules, chiffres ou _.' : /lien/.test(error.message) ? 'Lien invalide : utilise l’adresse complète, commençant par https://.' : 'Une valeur est invalide ou trop longue.');
      throw new Error(errFr(error));
    }
  },
  // Lecture d'un profil (confidentialité appliquée par le serveur). apercu = « voir comme les autres »
  async profilPublic(ref, apercu = false) {
    if (DEMO) return demoProfil(ref, apercu, this);
    const { data, error } = await sb.rpc('profil_public', {p_ref: String(ref || ''), p_apercu: !!apercu});
    if (error) throw new Error(errFr(error));
    return data;
  },
  async cartes(ids) {   // nom, identifiant et photo d'auteurs (commentaires publics)
    const u = [...new Set(ids.filter(Boolean))]; if (!u.length) return [];
    if (DEMO) return u.map(id => ({id, nom: id === 'demo' ? this.profile.full_name : 'Membre', username: id === 'demo' ? 'demo' : '', photo: ''}));
    const { data } = await sb.rpc('cartes_auteurs', {p_ids: u.slice(0, 200)});
    return data || [];
  },
  // Activité réelle : un enregistrement par exercice, type et jour (doublons ignorés)
  _vus: new Set(),
  track(exId, kind) {
    const k = exId + '|' + kind + '|' + new Date().toDateString();
    if (!this.user || !exId || this._vus.has(k)) return;
    this._vus.add(k);
    if (DEMO) { const a = ls.get('demo-activite', []); a.push({exercice_id: exId, kind, jour: new Date().toISOString().slice(0, 10)}); ls.set('demo-activite', a.slice(-3000)); return; }
    sb.from('activite').upsert({exercice_id: exId, kind}, {onConflict: 'user_id,exercice_id,kind,jour', ignoreDuplicates: true}).then(() => {}, () => {});
  },
  async etoile(cible, note) {   // étoiles 1..5 ; null = retirer sa note
    if (DEMO) throw new Error('Les étoiles nécessitent Supabase.');
    const r = note == null ? await sb.from('etoiles').delete().eq('cible_id', cible).eq('auteur_id', this.user.id)
      : await sb.from('etoiles').upsert({cible_id: cible, auteur_id: this.user.id, note}, {onConflict: 'cible_id,auteur_id'});
    if (r.error) throw new Error(/row-level/.test(r.error.message) ? 'Ce profil n’accepte pas les étoiles.' : errFr(r.error));
  },
  async etoilesModeration(cible) {
    if (DEMO) return [];
    const { data } = await sb.rpc('etoiles_moderation', {p_cible: cible}); return data || [];
  },
  async retirerEtoile(cible, auteur) {
    const { error } = await sb.from('etoiles').delete().eq('cible_id', cible).eq('auteur_id', auteur); if (error) throw new Error(errFr(error));
  },
  async contribution(titre) {   // enregistre le FAIT qu'un PDF a été envoyé (le fichier part par e-mail)
    if (DEMO) { ls.set('demo-contrib', (ls.get('demo-contrib', 0) || 0) + 1); return; }
    await sb.from('contributions').insert({titre: String(titre || '').slice(0, 120)});
  },

  /* ---------- suivi ---------- */
  async loadSuivi() {
    if (DEMO) return ls.get('demo-suivi', {});
    const { data } = await sb.from('suivi').select('data').eq('user_id', this.user.id).maybeSingle();
    return data?.data || {};
  },
  _w: Promise.resolve(),
  saveSuivi(d) {
    if (DEMO) { ls.set('demo-suivi', d); return Promise.resolve(); }
    const body = JSON.parse(JSON.stringify(d));
    this._w = this._w.then(() => sb.from('suivi').upsert({user_id: this.user.id, data: body, updated_at: new Date().toISOString()})).catch(() => {});
    return this._w;
  },
  async setMyLevel(n) {
    this.profile.niveau = n;
    if (DEMO) { ls.set('demo-profile', this.profile); return; }
    await sb.from('profiles').update({niveau: n}).eq('id', this.user.id);
  },

  /* ---------- classe (prof) ---------- */
  async classe() {
    if (DEMO) return [{id: 'demo', full_name: this.profile.full_name, niveau: this.profile.niveau, role: 'prof', last_seen: new Date().toISOString(), data: ls.get('demo-suivi', {})}];
    const [{ data: ps }, { data: ss }] = await Promise.all([
      sb.from('profiles').select('id, full_name, role, niveau, last_seen, created_at'),
      sb.from('suivi').select('user_id, data, updated_at')]);
    const m = Object.fromEntries((ss || []).map(s => [s.user_id, s]));
    return (ps || []).map(p => ({...p, data: m[p.id]?.data || {}, updated_at: m[p.id]?.updated_at}));
  },
  async setLevel(uid, n) {
    if (DEMO) return this.setMyLevel(n);
    const { error } = await sb.from('profiles').update({niveau: n}).eq('id', uid);
    if (error) throw error;
  },

  /* ---------- configuration de classe ---------- */
  async config() {
    if (DEMO) return ls.get('demo-config', {message: '', sel: {}});
    const { data } = await sb.from('classe_config').select('message, sel').eq('id', 1).maybeSingle();
    return data || {message: '', sel: {}};
  },
  async saveConfig(c) {
    if (DEMO) { ls.set('demo-config', c); emit('config'); return; }
    const { error } = await sb.from('classe_config').update({message: c.message, sel: c.sel, updated_at: new Date().toISOString()}).eq('id', 1);
    if (error) throw error;
  },
  async getCode() {
    if (DEMO) return 'MP2026';
    const { data } = await sb.from('classe_secret').select('code_inscription').eq('id', 1).maybeSingle();
    return data?.code_inscription || '';
  },
  async setCode(code) {
    if (DEMO) return;
    const { error } = await sb.from('classe_secret').update({code_inscription: code}).eq('id', 1);
    if (error) throw error;
  },

  /* ---------- banque d'exercices ajoutés ---------- */
  async banque() {
    if (DEMO) return ls.get('demo-banque', []);
    const { data } = await sb.from('banque').select('*').order('created_at', {ascending: false});
    return data || [];
  },
  async addBanque(e) {
    if (DEMO) { const b = ls.get('demo-banque', []); b.unshift({...e, id: 'b' + Date.now()}); ls.set('demo-banque', b); emit('banque'); return; }
    const { error } = await sb.from('banque').insert({...e, created_by: this.user.id});
    if (error) throw error;
  },
  async delBanque(id) {
    if (DEMO) { ls.set('demo-banque', ls.get('demo-banque', []).filter(x => x.id !== id)); emit('banque'); return; }
    const { error } = await sb.from('banque').delete().eq('id', id);
    if (error) throw error;
  },


  /* ---------- groupes ---------- */
  async groupes() {
    if (DEMO) { const d = D.get(); return d.groupes.map(g => ({...g, role: d.membres.find(m => m.groupe_id === g.id && m.user_id === 'demo')?.role || null, n: d.membres.filter(m => m.groupe_id === g.id).length})); }
    const [{ data: gs, error }, { data: ms }] = await Promise.all([
      sb.from('groupes').select('id, nom, description, code, created_at').order('created_at'),
      sb.from('groupe_membres').select('groupe_id, user_id, role')]);
    if (error) throw new Error(errFr(error));
    return (gs || []).map(g => ({...g, role: (ms || []).find(m => m.groupe_id === g.id && m.user_id === this.user.id)?.role || null, n: (ms || []).filter(m => m.groupe_id === g.id).length}));
  },
  async membres(g) {
    if (DEMO) { const d = D.get(); return d.membres.filter(m => m.groupe_id === g).map(m => ({...m, full_name: m.user_id === 'demo' ? this.profile.full_name : m.full_name})); }
    const { data: ms, error } = await sb.from('groupe_membres').select('user_id, role, joined_at').eq('groupe_id', g).order('joined_at');
    if (error) throw new Error(errFr(error));
    const ids = (ms || []).map(m => m.user_id);
    const { data: ps } = ids.length ? await sb.from('profiles').select('id, full_name').in('id', ids) : {data: []};
    const nm = Object.fromEntries((ps || []).map(p => [p.id, p.full_name]));
    return (ms || []).map(m => ({...m, full_name: nm[m.user_id] || 'Membre'}));
  },
  async _rpc(f, args) { const { data, error } = await sb.rpc(f, args); if (error) throw new Error(errFr(error)); return data; },
  async creerGroupe(nom, description = '') {
    if (DEMO) { const d = D.get(), id = uid4(); d.groupes.push({id, nom, description, code: Math.random().toString(36).slice(2, 8).toUpperCase(), created_at: new Date().toISOString()});
      d.membres.push({groupe_id: id, user_id: 'demo', role: 'responsable', joined_at: new Date().toISOString()}); D.set(d); return id; }
    return this._rpc('creer_groupe', {p_nom: nom, p_description: description});
  },
  async rejoindre(code) {
    if (DEMO) { const d = D.get(), g = d.groupes.find(x => x.code === code.trim().toUpperCase()); if (!g) throw new Error('Code de groupe inconnu'); if (!d.membres.some(m => m.groupe_id === g.id && m.user_id === 'demo')) d.membres.push({groupe_id: g.id, user_id: 'demo', role: 'membre', joined_at: new Date().toISOString()}); D.set(d); return g.id; }
    return this._rpc('rejoindre_groupe', {p_code: code});
  },
  async quitter(g) {
    if (DEMO) { const d = D.get(); d.membres = d.membres.filter(m => !(m.groupe_id === g && m.user_id === 'demo')); if (!d.membres.some(m => m.groupe_id === g)) d.groupes = d.groupes.filter(x => x.id !== g); D.set(d); return; }
    return this._rpc('quitter_groupe', {g});
  },
  async definirRole(g, u, r) {
    if (DEMO) { const d = D.get(), m = d.membres.find(m => m.groupe_id === g && m.user_id === u); if (m) m.role = r;
      if (!d.membres.some(m => m.groupe_id === g && m.role === 'responsable')) { m.role = 'responsable'; throw new Error('Le groupe doit garder au moins un responsable'); } D.set(d); return; }
    return this._rpc('definir_role', {g, u, r});
  },
  async exclure(g, u) {
    if (DEMO) { const d = D.get(); d.membres = d.membres.filter(m => !(m.groupe_id === g && m.user_id === u)); D.set(d); return; }
    return this._rpc('exclure_membre', {g, u});
  },
  async regenererCode(g) {
    if (DEMO) { const d = D.get(), x = d.groupes.find(x => x.id === g); x.code = Math.random().toString(36).slice(2, 8).toUpperCase(); D.set(d); return x.code; }
    return this._rpc('regenerer_code', {g});
  },
  async majGroupe(g, champs) {
    if (DEMO) { const d = D.get(); Object.assign(d.groupes.find(x => x.id === g), champs); D.set(d); return; }
    const { error } = await sb.from('groupes').update(champs).eq('id', g); if (error) throw new Error(errFr(error));
  },
  async supprimerGroupe(g) {
    if (DEMO) { const d = D.get(); d.groupes = d.groupes.filter(x => x.id !== g); d.membres = d.membres.filter(m => m.groupe_id !== g); d.reponses = d.reponses.filter(r => r.groupe_id !== g); d.coms = d.coms.filter(c => c.groupe_id !== g); D.set(d); return; }
    const { error } = await sb.from('groupes').delete().eq('id', g); if (error) throw new Error(errFr(error));
  },

  /* ---------- réponses sur l'honneur, notes, commentaires ---------- */
  async fil(g, ex) {
    if (DEMO) { const d = D.get();
      return {reponses: d.reponses.filter(r => r.groupe_id === g && r.exercice_id === ex).map(r => ({...r, notes: d.notes.filter(n => n.reponse_id === r.id)})),
              commentaires: d.coms.filter(c => (c.groupe_id === g || c.public) && c.exercice_id === ex).sort((a, b) => a.created_at.localeCompare(b.created_at))}; }
    const [r, c] = await Promise.all([
      sb.from('reponses').select('*, notes(note, evaluateur_id)').eq('groupe_id', g).eq('exercice_id', ex).order('created_at'),
      sb.from('commentaires').select('*').eq('exercice_id', ex).or(`groupe_id.eq.${g},public.eq.true`).order('created_at').limit(300)]);
    if (r.error) throw new Error(errFr(r.error));
    return {reponses: r.data || [], commentaires: c.data || []};
  },
  async recentes(g) {   // dernières réponses d'un groupe (page Groupes)
    if (DEMO) { const d = D.get(); return d.reponses.filter(r => r.groupe_id === g).map(r => ({...r, notes: d.notes.filter(n => n.reponse_id === r.id)})).sort((a, b) => b.created_at.localeCompare(a.created_at)).slice(0, 30); }
    const { data } = await sb.from('reponses').select('id, exercice_id, user_id, created_at, aide_consultee, notes(note)').eq('groupe_id', g).order('created_at', {ascending: false}).limit(30);
    return data || [];
  },
  async mesReponses() {
    if (DEMO) { const d = D.get(); return d.reponses.filter(r => r.user_id === 'demo').map(r => ({...r, notes: d.notes.filter(n => n.reponse_id === r.id)})); }
    const { data } = await sb.from('reponses').select('id, groupe_id, exercice_id, created_at, notes(note)').eq('user_id', this.user.id);
    return data || [];
  },
  async soumettre({g, ex, contenu, images, engagementTexte, aide}) {
    const base = {groupe_id: g, exercice_id: ex, contenu, engagement: true, engagement_texte: engagementTexte, aide_consultee: !!aide};
    if (DEMO) { const d = D.get();
      if (d.reponses.some(r => r.groupe_id === g && r.exercice_id === ex && r.user_id === 'demo')) throw new Error(errFr('duplicate key reponses'));
      d.reponses.push({...base, id: uid4(), user_id: 'demo', photos: images.slice(0, 4), created_at: new Date().toISOString()}); D.set(d); return; }
    const photos = [];
    try {
      for (const im of images.slice(0, 4)) {
        const path = `${g}/${this.user.id}/${uid4()}.jpg`;
        const { error } = await sb.storage.from('reponses').upload(path, dataToBlob(im), {contentType: 'image/jpeg'});
        if (error) throw new Error('Envoi d’une photo impossible : ' + error.message);
        photos.push(path);
      }
      const { error } = await sb.from('reponses').insert({...base, photos});
      if (error) throw new Error(errFr(error));
    } catch (e) { if (photos.length) sb.storage.from('reponses').remove(photos).catch(() => {}); throw e; }
  },
  async supprimerReponse(r) {
    if (DEMO) { const d = D.get(); d.reponses = d.reponses.filter(x => x.id !== r.id); d.notes = d.notes.filter(n => n.reponse_id !== r.id); d.coms = d.coms.filter(c => c.reponse_id !== r.id); D.set(d); return; }
    const { error } = await sb.from('reponses').delete().eq('id', r.id); if (error) throw new Error(errFr(error));
    if (r.photos?.length) sb.storage.from('reponses').remove(r.photos).catch(() => {});
  },
  async noter(rid, note) {   // note entière de 0 à 10, ou null pour retirer sa note
    if (DEMO) { const d = D.get(); d.notes = d.notes.filter(n => !(n.reponse_id === rid && n.evaluateur_id === 'demo')); if (note != null) d.notes.push({reponse_id: rid, evaluateur_id: 'demo', note}); D.set(d); return; }
    const q = note == null ? sb.from('notes').delete().eq('reponse_id', rid).eq('evaluateur_id', this.user.id)
      : sb.from('notes').upsert({reponse_id: rid, evaluateur_id: this.user.id, note, updated_at: new Date().toISOString()});
    const { error } = await q; if (error) throw new Error(errFr(error));
  },
  async commenter({g, ex, rid, contenu, pub = false}) {
    const publique = !!pub && !rid;   // une réponse à une réponse privée reste dans le groupe
    if (DEMO) { const d = D.get(); d.coms.push({id: uid4(), groupe_id: g, exercice_id: ex, reponse_id: rid || null, user_id: 'demo', contenu, public: publique, created_at: new Date().toISOString(), edited_at: null}); D.set(d); return; }
    const { error } = await sb.from('commentaires').insert({groupe_id: g, exercice_id: ex, reponse_id: rid || null, contenu, public: publique}); if (error) throw new Error(errFr(error));
  },
  async modifierCommentaire(id, contenu) {
    if (DEMO) { const d = D.get(), c = d.coms.find(c => c.id === id); c.contenu = contenu; c.edited_at = new Date().toISOString(); D.set(d); return; }
    const { error } = await sb.from('commentaires').update({contenu}).eq('id', id); if (error) throw new Error(errFr(error));
  },
  async supprimerCommentaire(id) {
    if (DEMO) { const d = D.get(); d.coms = d.coms.filter(c => c.id !== id); D.set(d); return; }
    const { error } = await sb.from('commentaires').delete().eq('id', id); if (error) throw new Error(errFr(error));
  },
  _urls: {},
  async photoURLs(paths) {   // URL signées (1 h) pour les photos privées
    const todo = paths.filter(p => !p.startsWith('data:') && !this._urls[p]);
    if (todo.length && !DEMO) { const { data } = await sb.storage.from('reponses').createSignedUrls(todo, 3600); (data || []).forEach(x => { if (x.signedUrl) this._urls[x.path] = x.signedUrl; }); }
    return Object.fromEntries(paths.map(p => [p, p.startsWith('data:') ? p : this._urls[p] || '']));
  },

  /* ---------- IA ---------- */
  async ia(body) {
    if (DEMO) throw new Error('La correction par l’IA est désactivée en mode démonstration.');
    const { data, error } = await sb.functions.invoke('corriger', {body});
    if (error) {
      let msg = 'La correction n’a pas pu aboutir.';
      try { const j = await error.context.json(); if (j?.error) msg = j.error; } catch {}
      throw new Error(msg);
    }
    if (data?.error) throw new Error(data.error);
    return data;
  },

  /* ---------- temps réel ---------- */
  live(state) {
    if (DEMO || !this.user) return;
    if (channel) { channel.track(state).catch(() => {}); return; }
    channel = sb.channel('classe-live', {config: {presence: {key: this.user.id}, broadcast: {self: false}}});
    channel.on('presence', {event: 'sync'}, () => emit('presence', channel.presenceState()))
      .on('broadcast', {event: 'activite'}, ({payload}) => emit('activity', payload));
    if (this.isProf) {
      channel.on('postgres_changes', {event: '*', schema: 'public', table: 'suivi'}, () => emit('classe'))
             .on('postgres_changes', {event: '*', schema: 'public', table: 'profiles'}, () => emit('classe'));
    }
    for (const t of ['reponses', 'notes', 'commentaires', 'groupe_membres'])
      channel.on('postgres_changes', {event: '*', schema: 'public', table: t}, p => emit('groupe', {t, p}));
    channel.on('postgres_changes', {event: '*', schema: 'public', table: 'classe_config'}, () => emit('config'))
           .on('postgres_changes', {event: '*', schema: 'public', table: 'banque'}, () => emit('banque'));
    channel.subscribe(st => { if (st === 'SUBSCRIBED') channel.track(state).catch(() => {}); });
  },
  activity(p) { if (channel) channel.send({type: 'broadcast', event: 'activite', payload: p}).catch(() => {}); },
  stopLive() { if (channel) { sb.removeChannel(channel); channel = null; } },
};
