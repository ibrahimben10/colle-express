// Mise en forme des énoncés et des corrigés (partagée par le site et la page de correction).
export const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[c]));

// Gras **…**, italique *…*, sauts de ligne ; les formules $…$ sont laissées à MathJax.
// Empêche MathJax de couper une ligne avant « dx » / « dt » et au milieu d'une écriture scientifique.
const noBreakD = t => String(t ?? '')
  .replace(/\\,\s*\\mathrm\s*\{?d/g, m => '\\nobreak' + m)
  .replace(/\\times\s*10/g, '\\nobreak\\times\\nobreak 10');   // 8,85 × 10⁻¹² reste sur une ligne
export function inline(t) {
  return esc(noBreakD(t))
    .replace(/\*\*(.+?)\*\*/g, '<b>$1</b>')
    .replace(/(^|[\s(])\*([^*\n$]+?)\*(?=[\s.,:;)]|$)/g, '$1<i>$2</i>');
}
// Tableau Markdown simple : lignes « | a | b | », ligne de séparation « |---| » ignorée, première ligne en en-tête.
function table(p) {
  const rows = p.trim().split('\n').map(l => l.trim().replace(/^\||\|$/g, '').split('|').map(c => c.trim()));
  const body = rows.filter((r, i) => !(i === 1 && r.every(c => /^:?-{2,}:?$/.test(c))));
  const [head, ...rest] = body;
  return `<div class="tbl"><table><thead><tr>${head.map(c => `<th>${inline(c)}</th>`).join('')}</tr></thead><tbody>${rest.map(r => `<tr>${r.map(c => `<td>${inline(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
}
const isTable = p => { const l = p.trim().split('\n'); return l.length > 1 && l.every(x => /^\s*\|.*\|\s*$/.test(x)); };
// Paragraphe : lignes « - … » regroupées en liste à puces.
function para(p) {
  p = p.replace(/\$\$[\s\S]*?\$\$/g, m => m.replace(/\s*\n\s*/g, ' '));   // pas de <br> dans une formule centrée
  const L = p.split('\n');
  if (!L.some(l => /^\s*[-•]\s+/.test(l))) return `<p>${inline(p).replace(/\n/g, '<br>')}</p>`;
  let html = '', ul = [];
  const flush = () => { if (ul.length) html += `<ul class="bul">${ul.map(x => `<li>${inline(x)}</li>`).join('')}</ul>`; ul = []; };
  for (const l of L) { const m = l.match(/^\s*[-•]\s+(.*)$/); if (m) ul.push(m[1]); else if (ul.length && /^\s{2,}\S/.test(l)) ul[ul.length - 1] += ' ' + l.trim(); else { flush(); if (l.trim()) html += `<p>${inline(l)}</p>`; } }
  flush(); return html;
}
export const rich = t => String(t ?? '').split(/\n{2,}/).map(p => isTable(p) ? table(p) : para(p)).join('');

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
  // Un paragraphe « **Titre.** … » ouvre une étape ; les paragraphes suivants s'y rattachent.
  let html = '', open = false;
  for (const p of String(text ?? '').split(/\n{2,}/)) {
    const m = p.match(/^\*\*(.+?)\*\*\s*([\s\S]*)$/);
    if (m && m[1].length < 70) {
      let head = m[1].replace(/\s*[.:]\s*$/, '');
      if (/^\d+(\.?\([a-z]\))?$/.test(head)) head = 'Question ' + head.replace('.(', '(');
      if (open) html += '</section>';
      html += `<section class="step"><h4>${inline(head)}</h4>${m[2].trim() ? para(m[2].trim()) : ''}`; open = true;
    } else html += isTable(p) ? table(p) : para(p);
  }
  return html + (open ? '</section>' : '');
}

/* ---------- Blocs pédagogiques partagés (site et page de correction) ---------- */
// Deux niveaux d'indices : 1 = piste globale ; 2 = méthode précise (indices 2 et 3 du professeur regroupés).
export const hintLevels = K => K?.indices?.length ? [K.indices[0], K.indices.slice(1).join('\n\n')].filter(Boolean) : [];
export const HINT_LAB = ['Piste globale', 'Méthode précise'];

export function hintsHTML(K, open = []) {
  return hintLevels(K).map((h, i) => `<details class="acc hint-acc" data-h="${i}" ${open[i] ? 'open' : ''}>
    <summary><span class="hn">${i + 1}</span><span class="acc-t"><b>Indice ${i + 1}</b><small>${HINT_LAB[i]}</small></span><span class="chev" aria-hidden="true"></span></summary>
    <div class="acc-body">${rich(h)}</div></details>`).join('');
}

export function bilanHTML(K) {
  const th = K?.theoremes || [], as = K?.astuces || [];
  if (!th.length && !as.length) return '';
  return `<div class="co co-bilan"><div class="co-h"><span class="co-e" aria-hidden="true">📌</span>Bilan de l'exercice</div>
    ${th.length ? `<h5>📜 Théorèmes &amp; définitions utilisés</h5><ul class="thm">${th.map(t => `<li>${inline(t)}</li>`).join('')}</ul>` : ''}
    ${as.length ? `<h5>💡 Astuces &amp; réflexes à retenir</h5><ul class="tips">${as.map(t => `<li>${inline(t)}</li>`).join('')}</ul>` : ''}</div>`;
}

export function correctionHTML(K) {
  return `${K.reponse ? `<div class="result"><span class="lab">🎯 Résultat</span><div>${rich(K.reponse)}</div></div>` : ''}
    <div class="corrige">${fmtCorrige(K.corrige)}</div>${bilanHTML(K)}`;
}
