// Petits composants d'interface partagés : notifications (toasts), thème clair/sombre,
// apparition au défilement, état « chargement » des boutons.

const $ = s => document.querySelector(s);

/* ---------- notifications ---------- */
export function toast(msg, kind = 'info', ms = 3800) {
  let box = $('#toasts');
  if (!box) { box = document.createElement('div'); box.id = 'toasts'; box.className = 'toasts'; box.setAttribute('aria-live', 'polite'); document.body.append(box); }
  const t = document.createElement('div');
  t.className = 'toast ' + kind; t.setAttribute('role', kind === 'error' ? 'alert' : 'status');
  t.textContent = msg;
  box.append(t);
  requestAnimationFrame(() => t.classList.add('in'));
  setTimeout(() => { t.classList.remove('in'); setTimeout(() => t.remove(), 300); }, ms);
}

/* ---------- thème ---------- */
const THEME_KEY = 'ce:theme';
const sysDark = () => matchMedia('(prefers-color-scheme: dark)').matches;
export const themeActuel = () => document.documentElement.dataset.theme || (sysDark() ? 'dark' : 'light');
function appliquer(t) {
  if (t) document.documentElement.dataset.theme = t; else delete document.documentElement.dataset.theme;
  syncTheme();
}
export function syncTheme() {
  const dark = themeActuel() === 'dark';
  document.querySelector('meta[name=theme-color]')?.setAttribute('content', dark ? '#0B1022' : '#1C2B78');
  document.querySelectorAll('[data-theme-toggle]').forEach(b => {
    b.setAttribute('aria-pressed', dark);
    b.setAttribute('aria-label', dark ? 'Passer en mode clair' : 'Passer en mode sombre');
    b.title = b.getAttribute('aria-label');
  });
}
export function initTheme() {
  let t = null; try { t = localStorage.getItem(THEME_KEY); } catch {}
  appliquer(t === 'light' || t === 'dark' ? t : null);
  document.addEventListener('click', e => {
    const b = e.target.closest('[data-theme-toggle]'); if (!b) return;
    const next = themeActuel() === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem(THEME_KEY, next); } catch {}
    // transition douce entre les thèmes (fondu croisé si le navigateur le permet)
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) appliquer(next);
    else if (document.startViewTransition) document.startViewTransition(() => appliquer(next));
    else { document.documentElement.classList.add('theme-anim'); appliquer(next); setTimeout(() => document.documentElement.classList.remove('theme-anim'), 450); }
  });
}
export const THEME_ICON = '<svg class="ic th-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/></svg><svg class="ic th-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';

/* ---------- apparition au défilement ---------- */
export function reveal(root = document) {
  const els = root.querySelectorAll('.reveal:not(.shown)');
  if (!('IntersectionObserver' in window) || matchMedia('(prefers-reduced-motion: reduce)').matches) { els.forEach(e => e.classList.add('shown')); return; }
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('shown'); io.unobserve(e.target); } }), {rootMargin: '0px 0px -8% 0px'});
  els.forEach(e => io.observe(e));
}

/* ---------- bouton en cours d'envoi ---------- */
// Désactive le bouton et affiche un indicateur ; renvoie une fonction qui restaure l'état.
export function busy(btn, label) {
  if (!btn) return () => {};
  const html = btn.innerHTML;
  btn.disabled = true; btn.setAttribute('aria-busy', 'true');
  btn.innerHTML = `<span class="spin" aria-hidden="true"></span><span>${label || btn.textContent.trim()}</span>`;
  return () => { btn.disabled = false; btn.removeAttribute('aria-busy'); btn.innerHTML = html; };
}
