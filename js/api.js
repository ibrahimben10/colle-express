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
  if (map[code]) return map[code];
  if (st === 429 || /rate.?limit|too many/i.test(code + ' ' + m)) return 'rate_limit';
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
              commentaires: d.coms.filter(c => c.groupe_id === g && c.exercice_id === ex).sort((a, b) => a.created_at.localeCompare(b.created_at))}; }
    const [r, c] = await Promise.all([
      sb.from('reponses').select('*, notes(note, evaluateur_id)').eq('groupe_id', g).eq('exercice_id', ex).order('created_at'),
      sb.from('commentaires').select('*').eq('groupe_id', g).eq('exercice_id', ex).order('created_at')]);
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
  async commenter({g, ex, rid, contenu}) {
    if (DEMO) { const d = D.get(); d.coms.push({id: uid4(), groupe_id: g, exercice_id: ex, reponse_id: rid || null, user_id: 'demo', contenu, created_at: new Date().toISOString(), edited_at: null}); D.set(d); return; }
    const { error } = await sb.from('commentaires').insert({groupe_id: g, exercice_id: ex, reponse_id: rid || null, contenu}); if (error) throw new Error(errFr(error));
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
