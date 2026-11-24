// Confort au téléphone : les barres s'effacent quand on lit et reviennent dès qu'on remonte,
// elles disparaissent quand le clavier est ouvert, et un glissement depuis le bord gauche
// ramène à la liste des exercices (utile dans l'application installée, qui n'a pas de bouton retour).
const phone = () => innerWidth < 820;
const root = document.documentElement;

/* ---------- barres qui s'effacent au défilement ---------- */
function autoHide() {
  let last = scrollY, acc = 0, raf = 0;
  const set = hide => root.classList.toggle('bars-off', hide);
  addEventListener('scroll', () => {
    if (raf) return;
    raf = requestAnimationFrame(() => {
      raf = 0;
      const y = scrollY, dy = y - last; last = y;
      if (!phone()) return set(false);
      const end = y + innerHeight >= document.documentElement.scrollHeight - 40;
      if (y < 60 || end) { acc = 0; return set(false); }
      acc = Math.sign(dy) === Math.sign(acc) ? acc + dy : dy;   // on cumule dans un même sens : pas de clignotement
      if (acc > 24) set(true);
      else if (acc < -18) set(false);
    });
  }, {passive: true});
  addEventListener('hashchange', () => set(false));
}

/* ---------- clavier ouvert : on libère l'écran ---------- */
function keyboard() {
  const typing = el => el?.matches?.('textarea, input:not([type=checkbox]):not([type=radio]):not([type=range]):not([type=file]), select, [contenteditable=true]');
  addEventListener('focusin', e => { if (phone() && typing(e.target)) root.classList.add('kb'); });
  addEventListener('focusout', () => setTimeout(() => { if (!typing(document.activeElement)) root.classList.remove('kb'); }, 50));
  // le champ reste visible au-dessus du clavier
  window.visualViewport?.addEventListener('resize', () => {
    const a = document.activeElement;
    if (root.classList.contains('kb') && typing(a)) a.scrollIntoView({block: 'nearest'});
  });
}

/* ---------- glissement depuis le bord gauche : retour à la liste ---------- */
function edgeSwipe() {
  let x0 = 0, y0 = 0, t0 = 0, on = false, el = null;
  addEventListener('touchstart', e => {
    const t = e.touches[0];
    on = phone() && document.body.classList.contains('detail') && t.clientX < 28 && e.touches.length === 1;
    if (!on) return;
    x0 = t.clientX; y0 = t.clientY; t0 = performance.now(); el = document.getElementById('copy');
  }, {passive: true});
  addEventListener('touchmove', e => {
    if (!on) return;
    const t = e.touches[0], dx = t.clientX - x0, dy = Math.abs(t.clientY - y0);
    if (dy > 40 && dy > dx) { on = false; el.style.transform = ''; return; }
    if (dx > 0) { el.style.transition = 'none'; el.style.transform = `translateX(${Math.min(dx, innerWidth) * .6}px)`; el.style.opacity = 1 - Math.min(dx / innerWidth, .5); }
  }, {passive: true});
  addEventListener('touchend', e => {
    if (!on) return; on = false;
    const dx = e.changedTouches[0].clientX - x0, fast = dx > 60 && performance.now() - t0 < 300;
    el.style.transition = 'transform .22s ease, opacity .22s ease';
    if (dx > innerWidth * .35 || fast) {
      el.style.transform = `translateX(${innerWidth * .6}px)`; el.style.opacity = 0;
      setTimeout(() => { document.getElementById('bBack')?.click(); el.style.cssText = ''; }, 180);
    } else { el.style.transform = ''; el.style.opacity = ''; setTimeout(() => { el.style.transition = ''; }, 230); }
  }, {passive: true});
}

export function initTactile() {
  autoHide(); keyboard(); edgeSwipe();
}
