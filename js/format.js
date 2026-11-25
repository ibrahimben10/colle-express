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
const rich0 = t => String(t ?? '').split(/\n{2,}/).map(p => isTable(p) ? table(p) : para(p)).join('');

// Énoncé : texte d'introduction, « Données » encadrées, questions numérotées et sous-questions (a), (b)…
function fmtEnonce0(text) {
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
  const block = arr => rich0(arr.join('\n').replace(/\n{3,}/g, '\n\n').trim());
  let html = '';
  const introTxt = intro.join('\n').trim();
  if (introTxt) {
    html += introTxt.split(/\n{2,}/).map(p => /^(On donne|Données|Donnée)\b/i.test(p.trim())
      ? `<div class="donnees"><span class="dlab">Données</span>${rich0(p.replace(/^(On donne|Données|Donnée)\s*:?\s*/i, ''))}</div>`
      : rich0(p)).join('');
  }
  if (qs.length) {
    html += `<ol class="qs">${qs.map(q => `<li><span class="qn">${q.n}</span><div class="qb">${block(q.head)}${q.subs.length
      ? `<ol class="subs">${q.subs.map(s => `<li><span class="sk">${s.k}</span><div>${block(s.t)}</div></li>`).join('')}</ol>` : ''}</div></li>`).join('')}</ol>`;
  }
  return html;
}

// Corrigé : chaque paragraphe qui commence par **1.**, **2.(a)**, **Conclusion.** devient une étape titrée.
function fmtCorrige0(text) {
  // Un paragraphe « **Titre.** … » ouvre une étape ; les paragraphes suivants s'y rattachent.
  // Format « 6 étapes » : « **Étape 3 — Stratégie.** » ouvre une grande étape numérotée,
  // « **4.2 Titre.** » une sous-partie, et un paragraphe commençant par « > » un encadré
  // (Théorème, Définition, Hypothèses, Attention, Vérification, Point non démontré…).
  let html = '', open = false;
  for (const p of String(text ?? '').split(/\n{2,}/)) {
    if (/^>\s?/.test(p)) { html += callout(p.replace(/^>\s?/gm, '')); continue; }
    const m = p.match(/^\*\*(.+?)\*\*\s*([\s\S]*)$/);
    if (m && m[1].length < 90) {
      let head = m[1].replace(/\s*[.:]\s*$/, '');
      const sub = head.match(/^(\d+\.\d+)\s+(.+)$/);
      if (sub && open) { html += `<h5 class="sub"><span>${sub[1]}</span> ${inline(sub[2])}</h5>${m[2].trim() ? para(m[2].trim()) : ''}`; continue; }
      const et = head.match(/^Étape\s+(\d)\s*[—–-]\s*(.+)$/);
      if (open) html += '</section>';
      if (et) html += `<section class="step etape e${et[1]}"><h4><span class="en" aria-hidden="true">${et[1]}</span><span class="sr">Étape ${et[1]} : </span>${inline(et[2])}</h4>${m[2].trim() ? para(m[2].trim()) : ''}`;
      else {
        if (/^\d+(\.?\([a-z]\))?$/.test(head)) head = 'Question ' + head.replace('.(', '(');
        html += `<section class="step"><h4>${inline(head)}</h4>${m[2].trim() ? para(m[2].trim()) : ''}`;
      }
      open = true;
    } else html += isTable(p) ? table(p) : para(p);
  }
  return html + (open ? '</section>' : '');
}
/* ---------- Code (informatique) : blocs ```python … ``` et `code en ligne` ---------- */
// Les blocs sont mis de côté avant toute mise en forme (ils peuvent contenir des lignes vides, des « 1. »,
// des « * » ou des « $ »), puis remis à la fin, colorés. MathJax ignore <pre> et <code>.
const KW = new Set('False None True and as assert break class continue def del elif else except finally for from global if import in is lambda nonlocal not or pass raise return try while with yield'.split(' '));
const BI = new Set('print len range int float str list dict set tuple min max sum abs sorted enumerate zip map bool round open isinstance reversed any all divmod type'.split(' '));
const TOK = /(#[^\n]*)|("""[\s\S]*?"""|'''[\s\S]*?'''|"(?:\\.|[^"\\\n])*"|'(?:\\.|[^'\\\n])*')|(\b\d+(?:\.\d+)?(?:e[-+]?\d+)?\b)|([A-Za-z_]\w*)|(\s+)|([\s\S])/g;
const KW_SQL = new Set('SELECT FROM WHERE AND OR NOT AS JOIN ON INNER LEFT GROUP BY HAVING ORDER ASC DESC LIMIT OFFSET DISTINCT IN IS NULL LIKE BETWEEN UNION INTERSECT EXCEPT EXISTS'.split(' '));
const FN_SQL = new Set('COUNT SUM AVG MIN MAX ROUND'.split(' '));
const TOK_SQL = /(--[^\n]*)|('(?:''|[^'])*')|(\b\d+(?:\.\d+)?\b)|([A-Za-z_]\w*)|(\s+)|([\s\S])/g;
function colorierSQL(code) {
  let out = '';
  for (const m of code.matchAll(TOK_SQL)) {
    const [t, com, str, num, id] = m;
    if (com) out += `<span class="c-com">${esc(t)}</span>`;
    else if (str) out += `<span class="c-str">${esc(t)}</span>`;
    else if (num) out += `<span class="c-num">${t}</span>`;
    else if (id) { const u = id.toUpperCase(); out += KW_SQL.has(u) ? `<span class="c-kw">${id}</span>` : FN_SQL.has(u) ? `<span class="c-bi">${id}</span>` : id; }
    else out += esc(t);
  }
  return out;
}
function coloriser(code, lang) {
  if (lang === 'sql') return colorierSQL(code);
  let out = '', prev = '';
  for (const m of code.matchAll(TOK)) {
    const [t, com, str, num, id, sp] = m;
    if (com) out += `<span class="c-com">${esc(t)}</span>`;
    else if (str) out += `<span class="c-str">${esc(t)}</span>`;
    else if (num) out += `<span class="c-num">${t}</span>`;
    else if (id) out += KW.has(id) ? `<span class="c-kw">${id}</span>` : prev === 'def' ? `<span class="c-fn">${id}</span>` : BI.has(id) ? `<span class="c-bi">${id}</span>` : id;
    else out += esc(t);
    if (!sp && !com) prev = id || t;
  }
  return out;
}
const codeHTML = b => `<div class="codeblk"><pre class="code" data-lang="${esc(b.lang || 'python')}"><code>${b.lang === 'text' ? esc(b.code) : coloriser(b.code, b.lang)}</code></pre><button class="cp" type="button" aria-label="Copier le code">Copier</button></div>`;
function protect(text) {
  const B = [];
  let t = String(text ?? '').replace(/```([a-z]*)[ \t]*\n([\s\S]*?)\n[ \t]*```/g, (_, lang, code) => `\n\n\uE000B${B.push({lang, code}) - 1}\uE001\n\n`);
  t = t.replace(/`([^`\n]+)`/g, (_, c) => `\uE000I${B.push({inl: c}) - 1}\uE001`);
  return [t.replace(/\n{3,}/g, '\n\n').replace(/^\n+/, ''), B];
}
function restore(html, B) {
  if (!B.length) return html;
  return html.replace(/<p>\s*\uE000B(\d+)\uE001\s*<\/p>/g, (m, i) => B[i] ? codeHTML(B[i]) : m)
    .replace(/\uE000([BI])(\d+)\uE001/g, (m, k, i) => !B[i] ? m : k === 'B' ? codeHTML(B[i]) : `<code>${esc(B[i].inl)}</code>`);
}
const avecCode = f => t => { const [x, B] = protect(t); return restore(f(x), B); };
export const rich = avecCode(rich0);
export const fmtEnonce = avecCode(fmtEnonce0);
export const fmtCorrige = avecCode(fmtCorrige0);
export const inlineC = avecCode(inline);
// bouton « Copier » des blocs de code (une seule écoute pour toute la page)
if (typeof document !== 'undefined' && !window.__cpCode) {
  window.__cpCode = true;
  document.addEventListener('click', e => {
    const b = e.target.closest?.('.codeblk .cp'); if (!b) return;
    const txt = b.previousElementSibling?.innerText || '';
    navigator.clipboard?.writeText(txt).then(() => { b.textContent = 'Copié'; setTimeout(() => b.textContent = 'Copier', 1500); }).catch(() => {});
  });
}

// Encadré : le premier mot en gras fixe le style (théorème, mise en garde, vérification, réserve).
export function callout(p) {
  const m = p.match(/^\*\*(.+?)\*\*\s*([\s\S]*)$/), t = (m ? m[1] : '').toLowerCase();
  const k = /^(théorème|propriété|définition|lemme|rappel|formule|loi|principe|relation|corollaire)/.test(t) ? 'thm'
    : /^(hypothèse|attention|piège|condition)/.test(t) ? 'warn' : /^(vérification|contrôle|cohérence)/.test(t) ? 'chk'
    : /^(point non démontré|réserve|limite)/.test(t) ? 'doubt' : 'note';
  return `<aside class="callout ${k}">${m ? `<b class="callout-t">${inline(m[1].replace(/\s*[.:]\s*$/, ''))}</b>${m[2].trim() ? para(m[2].trim()) : ''}` : para(p)}</aside>`;
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
  return `<div class="co co-bilan"><div class="co-h">Bilan de l'exercice</div>
    ${th.length ? `<h5>Théorèmes &amp; définitions utilisés</h5><ul class="thm">${th.map(t => `<li>${inlineC(t)}</li>`).join('')}</ul>` : ''}
    ${as.length ? `<h5>Réflexes à retenir</h5><ul class="tips">${as.map(t => `<li>${inlineC(t)}</li>`).join('')}</ul>` : ''}</div>`;
}

export function correctionHTML(K) {
  return `${K.reponse ? `<div class="result"><span class="lab">Résultat</span><div>${rich(K.reponse)}</div></div>` : ''}
    <div class="corrige">${fmtCorrige(K.corrige)}</div>${bilanHTML(K)}`;
}

/* ---------- Découpage d'un corrigé en étapes (mode guidé, outils par étape) ---------- */
// Même règle que fmtCorrige : un paragraphe « **Titre.** … » ouvre une étape, sauf les sous-parties « **4.2 …** ».
export function stepChunks(text) {
  const out = [], [t0, B] = protect(text);   // un bloc de code n'est jamais coupé entre deux étapes
  const back = x => x.replace(/\uE000([BI])(\d+)\uE001/g, (m, k, i) => !B[i] ? m : k === 'B' ? '```' + (B[i].lang || '') + '\n' + B[i].code + '\n```' : '`' + B[i].inl + '`');
  for (const p0 of t0.split(/\n{2,}/)) {
    const p = back(p0);
    const m = !/^>/.test(p) && p.match(/^\*\*(.+?)\*\*/);
    const head = m && m[1].length < 90 ? m[1].replace(/\s*[.:]\s*$/, '') : '';
    if (head && !/^\d+\.\d+\s/.test(head)) {
      const et = head.match(/^Étape\s+(\d)\s*[—–-]\s*(.+)$/);
      out.push({title: et ? et[2] : /^\d+(\.?\([a-z]\))?$/.test(head) ? 'Question ' + head.replace('.(', '(') : head, n: et ? +et[1] : null, md: p});
    } else if (out.length) out.at(-1).md += '\n\n' + p;
    else out.push({title: 'Mise en place', n: null, md: p});
  }
  return out;
}
// Question posée à l'élève avant de dévoiler une étape : elle l'invite à la chercher lui-même.
export function guideQuestion(c) {
  const t = (c?.title || '').toLowerCase();
  if (/analyse/.test(t)) return 'Avant de lire : qu’est-ce qui est donné, et qu’est-ce qu’on te demande exactement ? Écris-le en une ligne.';
  if (/rappel|cours/.test(t)) return 'Quels théorèmes ou définitions pourraient servir ici ? Note-les avec leurs hypothèses.';
  if (/stratégie|méthode|idée/.test(t)) return 'Quelle méthode envisages-tu ? Essaie de la formuler en une phrase avant de comparer.';
  if (/résolution|calcul/.test(t)) return 'Mène le calcul sur ta feuille, au moins jusqu’au premier résultat intermédiaire.';
  if (/vérification|contrôle/.test(t)) return 'Comment pourrais-tu contrôler ton résultat ? Un cas particulier, une limite, l’homogénéité…';
  if (/conclusion/.test(t)) return 'Écris ta conclusion avant de la comparer à celle du corrigé.';
  return 'Cherche cette partie sur ta feuille, puis dévoile-la pour comparer.';
}
