// Collections d'exercices : choix depuis un exercice, page partageable (#c/identifiant), gestion.
import { api } from './api.js';
import { ic } from './icons.js';
import { esc } from './format.js';
import { toast } from './ui.js';

let D = {};   // byId, LV
export const initBiblio = deps => { D = deps; };
const plural = (n, s, p = s + 's') => `${n} ${n > 1 ? p : s}`;

/* ---------- ranger un exercice dans des collections ---------- */
export async function openCollectionsPicker(exId) {
  const ex = D.byId(exId);
  const dlg = document.createElement('dialog'); dlg.className = 'dlg';
  dlg.innerHTML = `<div class="dlg-in"><header><h2>Ranger dans une collection</h2><button class="iconbtn" data-close aria-label="Fermer">${ic('x')}</button></header>
    <p class="small">${esc(ex?.titre || '')}</p><div id="clList" class="cl-list"><span class="skel skel-card"></span></div>
    <form class="cl-new" id="clNew"><label class="sr" for="clT">Nouvelle collection</label><input id="clT" maxlength="80" placeholder="Nouvelle collection, ex. : Classiques d’analyse"><button class="btn" type="submit">${ic('plus')} Créer</button></form>
    <footer><a class="btn ghost" href="#profil" data-close>Gérer mes collections</a><button class="btn primary" data-close>Terminé</button></footer></div>`;
  document.body.append(dlg);
  const list = dlg.querySelector('#clList');
  let C = [];
  const draw = () => {
    list.innerHTML = C.length ? C.map(c => `<label class="cl-item"><input type="checkbox" data-c="${esc(c.id)}" ${c.items.includes(exId) ? 'checked' : ''}>
      <span><b>${esc(c.titre)}</b><span class="small">${plural(c.items.length, 'exercice')} · ${c.public ? 'publique' : 'privée'}</span></span></label>`).join('')
      : '<p class="pf-emptyline">Aucune collection : crée la première ci-dessous.</p>';
  };
  try { C = await api.mesCollections(); draw(); } catch (x) { list.innerHTML = `<p class="err">${esc(x.message)}</p>`; }
  list.addEventListener('change', async e => {
    const cb = e.target.closest('[data-c]'); if (!cb) return;
    const c = C.find(x => x.id === cb.dataset.c); cb.disabled = true;
    try { await api.collectionItem(c.id, exId, cb.checked, c.items.length); c.items = cb.checked ? [...c.items, exId] : c.items.filter(x => x !== exId); draw(); toast(cb.checked ? `Ajouté à « ${c.titre} ».` : `Retiré de « ${c.titre} ».`, 'ok'); }
    catch (x) { cb.checked = !cb.checked; cb.disabled = false; toast(x.message, 'error'); }
  });
  dlg.querySelector('#clNew').onsubmit = async e => {
    e.preventDefault(); const t = dlg.querySelector('#clT').value.trim(); if (!t) return;
    try { const c = await api.creerCollection({titre: t}); await api.collectionItem(c.id, exId, true, 0); c.items = [exId]; C.push(c); dlg.querySelector('#clT').value = ''; draw(); toast(`Collection « ${t} » créée.`, 'ok'); }
    catch (x) { toast(x.message, 'error'); }
  };
  dlg.addEventListener('click', e => { if (e.target.closest('[data-close]') || e.target === dlg) dlg.close(); });
  dlg.addEventListener('close', () => dlg.remove());
  dlg.showModal();
}

/* ---------- page d'une collection ---------- */
export async function renderCollection(el, id) {
  el.innerHTML = `<div class="panel"><span class="skel skel-h"></span><span class="skel skel-card"></span></div>`;
  const c = await api.collectionPublique(id);
  if (!c) { el.innerHTML = `<div class="panel pf-missing"><h2>Collection introuvable</h2><a class="btn" href="#exercices">Retour aux exercices</a></div>`; return; }
  if (c.prive) { el.innerHTML = `<div class="panel pf-missing"><h2>Collection privée</h2><p class="small">Son auteur ne l’a pas partagée.</p><a class="btn" href="#exercices">Retour aux exercices</a></div>`; return; }
  const items = c.items.map(D.byId).filter(Boolean);
  el.innerHTML = `<article class="pf coll" style="--h:210">
    <header class="coll-head">
      <p class="pf-kicker">Collection · ${plural(items.length, 'exercice')} · ${c.public ? 'partagée avec les membres' : 'privée'}</p>
      ${c.self ? `<input class="coll-t" id="coT" maxlength="80" value="${esc(c.titre)}" aria-label="Titre de la collection">` : `<h1>${esc(c.titre)}</h1>`}
      <p class="small">par <a class="who" href="#u/${esc(c.auteur.username || c.auteur.id)}">${esc(c.auteur.nom)}</a></p>
      ${c.self ? `<textarea class="coll-d" id="coD" maxlength="300" rows="2" placeholder="Une description (facultatif)">${esc(c.description || '')}</textarea>` : c.description ? `<p class="pf-bio">${esc(c.description)}</p>` : ''}
      <div class="pf-bar" style="padding:12px 0 0">
        ${c.self ? `<label class="mini-tg"><input type="checkbox" id="coPub" ${c.public ? 'checked' : ''}> Partager avec les membres <span class="small">(si ton profil est public)</span></label>` : ''}
        <button class="btn ghost" id="coShare">${ic('link')} Copier le lien</button>
        ${c.self ? `<button class="btn ghost danger" id="coDel">${ic('trash')} Supprimer</button>` : ''}
      </div></header>
    <ol class="fav-list coll-list" id="coList">${items.map((e, i) => `<li data-id="${esc(e.id)}"><a href="#ex-${esc(e.id)}"><span class="fav-n">${String(i + 1).padStart(2, '0')}</span>
      <span class="fav-t"><b>${esc(e.titre)}</b><span class="small">${esc(e.mat)} · ${esc(e.chap)}</span></span><span class="stamp n${e.niveau}">${esc(D.LV[e.niveau] || '')}</span></a>
      ${c.self ? `<span class="coll-ord"><button class="iconbtn" data-up="${i}" aria-label="Monter" ${i ? '' : 'disabled'}>↑</button><button class="iconbtn" data-down="${i}" aria-label="Descendre" ${i < items.length - 1 ? '' : 'disabled'}>↓</button><button class="iconbtn" data-rm="${esc(e.id)}" aria-label="Retirer">${ic('x')}</button></span>` : ''}</li>`).join('')
      || `<li class="pf-emptyline" style="padding:16px">Collection vide. Sur un exercice, le bouton « Collection » permet d’en ajouter.</li>`}</ol>
  </article>`;
  el.querySelector('#coShare').onclick = async () => { const url = location.href.split('#')[0] + '#c/' + c.id; try { await navigator.clipboard.writeText(url); toast('Lien copié. Il s’ouvre pour les membres connectés si la collection est partagée.', 'ok'); } catch { prompt('Copie ce lien :', url); } };
  if (!c.self) return;
  const save = async champs => { try { await api.majCollection(c.id, champs); toast('Enregistré.', 'ok'); } catch (x) { toast(x.message, 'error'); } };
  el.querySelector('#coT').onchange = e => { const t = e.target.value.trim(); if (t) save({titre: t}); };
  el.querySelector('#coD').onchange = e => save({description: e.target.value.trim()});
  el.querySelector('#coPub').onchange = e => save({public: e.target.checked});
  el.querySelector('#coDel').onclick = async () => { if (!confirm(`Supprimer la collection « ${c.titre} » ? Les exercices eux-mêmes ne sont pas supprimés.`)) return;
    try { await api.supprimerCollection(c.id); toast('Collection supprimée.', 'ok'); location.hash = '#profil'; } catch (x) { toast(x.message, 'error'); } };
  el.querySelector('#coList').onclick = async e => {
    const b = e.target.closest('button'); if (!b) return; e.preventDefault();
    let ids = items.map(x => x.id);
    if (b.dataset.rm) { await api.collectionItem(c.id, b.dataset.rm, false); return renderCollection(el, id); }
    const i = +(b.dataset.up ?? b.dataset.down), j = b.dataset.up != null ? i - 1 : i + 1;
    [ids[i], ids[j]] = [ids[j], ids[i]];
    try { await api.ordonnerCollection(c.id, ids); renderCollection(el, id); } catch (x) { toast(x.message, 'error'); }
  };
}

/* ---------- section « Collections » du profil ---------- */
export function collectionsHTML(L, self) {
  if (!L?.length) return self ? `<p class="pf-emptyline">Aucune collection. Crée-en une pour regrouper tes exercices : « Classiques d’analyse », « À refaire avant les concours »…</p>` : '';
  return `<ul class="coll-cards">${L.map(c => `<li><a href="#c/${esc(c.id)}"><span class="coll-ic">${ic('book')}</span><span><b>${esc(c.titre)}</b>
    <span class="small">${plural(c.n, 'exercice')}${self ? ` · ${c.public ? 'partagée' : 'privée'}` : ''}</span>${c.description ? `<span class="small coll-desc">${esc(c.description)}</span>` : ''}</span></a></li>`).join('')}</ul>`;
}
export async function nouvelleCollection() {
  const t = prompt('Nom de la nouvelle collection :', ''); if (!t || !t.trim()) return null;
  try { const c = await api.creerCollection({titre: t.trim()}); toast('Collection créée.', 'ok'); return c; } catch (x) { toast(x.message, 'error'); return null; }
}
