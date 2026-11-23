// Mise en forme des énoncés et des corrigés (partagée par le site et la page de correction).
export const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[c]));

// Gras **…**, italique *…*, sauts de ligne ; les formules $…$ sont laissées à MathJax.
export function inline(t) {
  return esc(t)
    .replace(/\*\*(.+?)\*\*/g, '<b>$1</b>')
    .replace(/(^|[\s(])\*([^*\n$]+?)\*(?=[\s.,:;)]|$)/g, '$1<i>$2</i>');
}
export const rich = t => String(t ?? '').split(/\n{2,}/).map(p => `<p>${inline(p).replace(/\n/g, '<br>')}</p>`).join('');

// Énoncé : texte d'introduction, « Données » encadrées, questions numérotées et sous-questions (a), (b)…
export function fmtEnonce(text) {
  const lines = String(text ?? '').split('\n');
  const intro = [], qs = [];
  let cur = null;
  for (const raw of lines) {
    const l = raw.replace(/\s+$/, '');
    const q = l.match(/^\s*(\d+)\.\s+(.*)$/);
    const sub = l.match(/^\s*\(?([a-h])[).]\s+(.*)$/);
    if (q) { cur = {n: q[1], head: [q[2]], subs: []}; qs.push(cur); continue; }
    if (cur && sub) { cur.subs.push({k: sub[1], t: [sub[2]]}); continue; }
    if (cur) {
      if (!l.trim()) { (cur.subs.length ? cur.subs.at(-1).t : cur.head).push(''); continue; }
      (cur.subs.length ? cur.subs.at(-1).t : cur.head).push(l.trim());
    } else intro.push(l);
  }
  const block = arr => rich(arr.join('\n').replace(/\n{3,}/g, '\n\n').trim());
  let html = '';
  const introTxt = intro.join('\n').trim();
  if (introTxt) {
    html += introTxt.split(/\n{2,}/).map(p => /^(On donne|Données|Donnée)\b/i.test(p.trim())
      ? `<div class="donnees"><span class="dlab">Données</span>${rich(p.replace(/^(On donne|Données|Donnée)\s*:?\s*/i, ''))}</div>`
      : rich(p)).join('');
  }
  if (qs.length) {
    html += `<ol class="qs">${qs.map(q => `<li><span class="qn">${q.n}</span><div class="qb">${block(q.head)}${q.subs.length
      ? `<ol class="subs">${q.subs.map(s => `<li><span class="sk">${s.k}</span><div>${block(s.t)}</div></li>`).join('')}</ol>` : ''}</div></li>`).join('')}</ol>`;
  }
  return html;
}

// Corrigé : chaque paragraphe qui commence par **1.**, **2.(a)**, **Conclusion.** devient une étape titrée.
export function fmtCorrige(text) {
  return String(text ?? '').split(/\n{2,}/).map(p => {
    const m = p.match(/^\*\*(.+?)\*\*\s*([\s\S]*)$/);
    if (m && m[1].length < 60) {
      const head = m[1].replace(/\s*[.:]\s*$/, '');
      return `<section class="step"><h4>${inline(head)}</h4>${m[2].trim() ? `<p>${inline(m[2]).replace(/\n/g, '<br>')}</p>` : ''}</section>`;
    }
    return `<p>${inline(p).replace(/\n/g, '<br>')}</p>`;
  }).join('');
}
