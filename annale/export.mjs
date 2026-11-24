// node annale/export.mjs [lot…] : écrit les SVG autonomes dans annale/svg/ et une planche HTML par appel.
import { writeFileSync, mkdirSync } from 'fs';
const want = process.argv.slice(2);
const mods = {1: './lot1.js', 2: './lot2.js', 3: './lot3.js', 4: './lot4.js', 5: './lot5.js', 6: './lot6.js'};
mkdirSync(new URL('./svg/', import.meta.url), {recursive: true});
const cards = []; let nb = 0;
for (const [k, m] of Object.entries(mods)) {
  let lot; try { lot = Object.values(await import(m))[0]; } catch (e) { if (e.code === 'ERR_MODULE_NOT_FOUND') continue; throw e; }
  for (const f of lot) {
    const name = `${f.id}-${f.type}.svg`; nb++;
    if (/NaN|undefined/.test(f.svg)) console.log('ATTENTION', name);
    writeFileSync(new URL('./svg/' + name, import.meta.url), '<?xml version="1.0" encoding="UTF-8"?>\n' + f.svg + '\n');
    if (!want.length || want.includes(k)) cards.push(`<figure><div class="sv">${f.svg}</div><figcaption><b>${f.titre}</b> · ${f.type === 'enonce' ? 'énoncé' : 'correction'} <code>${name}</code>${f.legende ? '<br>' + f.legende : ''}</figcaption></figure>`);
  }
}
writeFileSync(new URL('./planche.html', import.meta.url), `<!doctype html><html lang="fr"><meta charset="utf-8"><title>Schémas annale</title>
<style>body{margin:24px;font:14px 'Latin Modern Roman',serif;color:#111;background:#fff}
.g{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}figure{margin:0;border:1px solid #ccc;padding:12px;break-inside:avoid}
.sv svg{max-width:100%;height:auto;display:block;margin:auto}figcaption{margin-top:6px;font-size:13px;color:#444}code{font-size:11px}
.dark{background:#151A19;color:#E9EEEA}.dark figure{border-color:#334}.dark figcaption{color:#aab}</style>
<body><div class="g">${cards.join('')}</div></body></html>`);
console.log(nb, 'fichiers,', cards.length, 'sur la planche');

// Index pour le site : légendes des schémas disponibles (les SVG sont chargés à la demande).
{
  const idx = {};
  for (const m of Object.values(mods)) {
    let lot; try { lot = Object.values(await import(m))[0]; } catch { continue; }
    for (const f of lot) { (idx[f.id] ||= {})[f.type === 'enonce' ? 'e' : 'c'] = f.legende || ''; }
  }
  const body = `// Généré par annale/export.mjs : ne pas modifier à la main.
// Schémas « annale » : id d'exercice -> {e: légende de l'énoncé, c: légende de la correction}.
export const AN = ${JSON.stringify(idx, null, 0).replace(/\},"/g, '},\n"')};
`;
  writeFileSync(new URL('../js/figures-annale-index.js', import.meta.url), body);
  console.log(Object.keys(idx).length, 'exercices indexés');
}
