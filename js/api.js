// Couche de données : Supabase en production, navigateur (localStorage) en mode démonstration.
import { CONFIG } from './config.js';

export const DEMO = !CONFIG.SUPABASE_URL || !CONFIG.SUPABASE_ANON_KEY;
const ls = { get(k, d) { try { const v = localStorage.getItem('ce:' + k); return v ? JSON.parse(v) : d; } catch { return d; } },
             set(k, v) { try { localStorage.setItem('ce:' + k, JSON.stringify(v)); } catch {} } };

let sb = null, channel = null;
const listeners = { auth: [], presence: [], activity: [], classe: [], config: [], banque: [] };
const emit = (k, v) => listeners[k].forEach(f => f(v));
export const on = (k, f) => listeners[k].push(f);

export const api = {
  user: null,      // {id, email}
  profile: null,   // {id, full_name, role, niveau}

  async init() {
    if (DEMO) {
      const p = ls.get('demo-profile', null);
      if (p) { this.user = {id: p.id, email: 'demo@local'}; this.profile = p; }
      return;
    }
    const { createClient } = await import('https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/+esm');
    sb = createClient(CONFIG.SUPABASE_URL, CONFIG.SUPABASE_ANON_KEY);
    const { data } = await sb.auth.getSession();
    if (data.session) await this._load(data.session.user);
    sb.auth.onAuthStateChange(async (ev, session) => {
      if (ev === 'PASSWORD_RECOVERY') { emit('auth', 'recovery'); return; }
      if (ev === 'SIGNED_IN' && session && session.user.id !== this.user?.id) { await this._load(session.user); emit('auth', 'in'); }
      if (ev === 'SIGNED_OUT') { this.user = null; this.profile = null; emit('auth', 'out'); }
    });
  },
  async _load(u) {
    this.user = {id: u.id, email: u.email};
    const { data } = await sb.from('profiles').select('id, full_name, role, niveau').eq('id', u.id).single();
    this.profile = data || {id: u.id, full_name: u.user_metadata?.full_name || '', role: 'eleve', niveau: 1};
    sb.from('profiles').update({last_seen: new Date().toISOString()}).eq('id', u.id).then(() => {});
  },
  get isProf() { return this.profile?.role === 'prof'; },

  async signIn(email, password) {
    if (DEMO) return this._demo(email.split('@')[0] || 'Démo');
    const { error } = await sb.auth.signInWithPassword({email, password});
    if (error) throw new Error(error.message.includes('Invalid') ? 'E-mail ou mot de passe incorrect.' : error.message.includes('confirm') ? 'Confirme d’abord ton adresse (e-mail reçu).' : error.message);
  },
  async signUp({name, email, password, code, niveau}) {
    if (DEMO) return this._demo(name, niveau);
    const { data, error } = await sb.auth.signUp({email, password, options: {data: {full_name: name, code, niveau}, emailRedirectTo: location.origin + location.pathname}});
    if (error) throw new Error(/Database error|code/i.test(error.message) ? 'Code de classe invalide.' : error.message);
    return data.session ? 'in' : 'confirm';
  },
  async _demo(name, niveau = 1) {
    this.profile = {id: 'demo', full_name: name, role: 'prof', niveau: +niveau};
    this.user = {id: 'demo', email: 'demo@local'};
    ls.set('demo-profile', this.profile);
    emit('auth', 'in');
    return 'in';
  },
  async resetPassword(email) {
    if (DEMO) return;
    const { error } = await sb.auth.resetPasswordForEmail(email, {redirectTo: location.origin + location.pathname});
    if (error) throw new Error(error.message);
  },
  async updatePassword(password) {
    const { error } = await sb.auth.updateUser({password});
    if (error) throw new Error(error.message);
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
    channel.on('postgres_changes', {event: '*', schema: 'public', table: 'classe_config'}, () => emit('config'))
           .on('postgres_changes', {event: '*', schema: 'public', table: 'banque'}, () => emit('banque'));
    channel.subscribe(st => { if (st === 'SUBSCRIBED') channel.track(state).catch(() => {}); });
  },
  activity(p) { if (channel) channel.send({type: 'broadcast', event: 'activite', payload: p}).catch(() => {}); },
  stopLive() { if (channel) { sb.removeChannel(channel); channel = null; } },
};
