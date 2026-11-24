// node annale/export.mjs : écrit les SVG autonomes du lot dans annale/svg/ et une planche HTML.
import { writeFileSync, mkdirSync } from 'fs';
import { LOT1 } from './lot1.js';
mkdirSync(new URL('./svg/', import.meta.url), {recursive: true});
const cards = [];
for (const f of LOT1) {
  const name = `${f.id}-${f.type}.svg`;
  writeFileSync(new URL('./svg/' + name, import.meta.url), '<?xml version="1.0" encoding="UTF-8"?>\n' + f.svg + '\n');
  cards.push(`<figure><div class="sv">${f.svg}</div><figcaption><b>${f.titre}</b> · ${f.type === 'enonce' ? 'énoncé' : 'correction'} <code>${name}</code></figcaption></figure>`);
}
writeFileSync(new URL('./planche.html', import.meta.url), `<!doctype html><html lang="fr"><meta charset="utf-8"><title>Lot test charte annale</title>
<style>body{margin:24px;font:14px 'Latin Modern Roman',serif;color:#111;background:#fff}h1{font-size:20px;margin:0 0 16px}
.g{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}figure{margin:0;border:1px solid #ccc;padding:12px;break-inside:avoid}
.sv svg{max-width:100%;height:auto;display:block;margin:auto}figcaption{margin-top:6px;font-size:13px;color:#444}code{font-size:11px}
.dark{background:#151A19;color:#E9EEEA}.dark figure{border-color:#334}.dark figcaption{color:#aab}</style>
<body><h1>Colle express — lot test de la charte « annale » (10 schémas)</h1><div class="g">${cards.join('')}</div></body></html>`);
console.log(LOT1.length, 'fichiers');
