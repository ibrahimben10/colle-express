// Colleur virtuel : une colle de cours sur une fiche, menée par un modèle de langage (fonction Supabase « colleur »).
// L'élève répond par écrit, au micro (reconnaissance vocale du navigateur, si disponible) ou en photo de sa feuille ; bilan noté à la fin.
import { CONFIG } from './config.js';
import { api } from './api.js';
import { esc, rich, inlineC } from './format.js';
import { ic } from './icons.js';

let IDX = null;
const PHOTO_SEULE = '(réponse en photo)';
let S = null;          // séance en cours : {fiche, titre, n, tours, messages, fil, fin, busy}
const STAT = {juste: ['Juste', 'ok'], partiel: ['Incomplet', 'mid'], faux: ['À revoir', 'ko']};
const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
const MAX_PHOTOS = 2;
let PH = [];           // photos jointes à la réponse en cours (data URL JPEG réduites)

// Photo de la feuille : réduite à 1568 px de côté, JPEG, fond blanc (les PNG transparents restent lisibles).
async function reduire(file) {
  const url = URL.createObjectURL(file);
  try {
    const img = await new Promise((ok, ko) => { const i = new Image(); i.onload = () => ok(i); i.onerror = ko; i.src = url; });
    const k = Math.min(1, 1568 / Math.max(img.naturalWidth, img.naturalHeight));
    const c = document.createElement('canvas'); c.width = Math.round(img.naturalWidth * k); c.height = Math.round(img.naturalHeight * k);
    const g = c.getContext('2d'); g.fillStyle = '#fff'; g.fillRect(0, 0, c.width, c.height); g.drawImage(img, 0, 0, c.width, c.height);
    return c.toDataURL('image/jpeg', 0.82);
  } finally { URL.revokeObjectURL(url); }
}
const vignettes = (L, suppr) => L.length ? `<div class="colle-ph">${L.map((d, i) => `<figure><img src="${d}" alt="Photo ${i + 1} de la réponse">${suppr ? `<button type="button" class="colle-ph-x" data-x="${i}" aria-label="Retirer la photo ${i + 1}">${ic('x')}</button>` : ''}</figure>`).join('')}</div>` : '';

const memo = {
  get(id) { try { return JSON.parse(localStorage.getItem('ce:colle:' + id) || 'null'); } catch { return null; } },
  set(id, v) { try { localStorage.setItem('ce:colle:' + id, JSON.stringify(v)); } catch {} },
};

export async function renderColleur(el, id, typeset) {
  if (!IDX) IDX = await fetch('data/fiches/index.json').then(r => r.json()).catch(() => []);
  const f = IDX.find(x => x.id === id && x.pret);
  if (S && f && S.fiche === f.id) return draw(el, typeset);          // retour sur une séance en cours
  if (!f) return choix(el, id);
  S = null;
  return accueil(el, f, typeset);
}

function cadre(inner) {
  return `<div class="colle-page"><a class="btn ghost" href="#fiches">${ic('back')} Fiches de cours</a>${inner}</div>`;
}
const essai = `<p class="colle-essai">${ic('clock')} <span><b>Version d'essai</b> — le colleur virtuel est en test, ce n'est pas la version finale. Limité à 2 colles par jour.</span></p>`;
const avert = `<p class="small colle-avert">${ic('bulb')}<span>Colle de <b>cours</b> : définitions, lois, ordres de grandeur, interprétations. Le colleur s'appuie sur la fiche du chapitre, mais c'est une IA : il peut se tromper. En cas de doute, la fiche fait foi.</span></p>`;

function choix(el, id) {
  const groupes = {};
  IDX.filter(x => x.pret).forEach(x => (groupes[`${x.mat} · ${x.niveau}`] ??= []).push(x));
  el.innerHTML = cadre(`<header class="fiche-head"><h1>Passer une colle de cours</h1>
    <p class="small">Choisis un chapitre : le colleur t'interroge, juge chaque réponse et te donne une note et les points à revoir.</p></header>${essai}
    ${CONFIG.COLLEUR ? '' : `<div class="panel pad"><p>${ic('clock')} Le colleur virtuel sera disponible très bientôt.</p></div>`}
    <div class="panel pad colle-choix">
      <label class="fld"><span>Chapitre</span><select id="clF">${Object.entries(groupes).map(([g, L]) => `<optgroup label="${esc(g)}">${L.map(x => `<option value="${x.id}" ${x.id === id ? 'selected' : ''}>${esc(x.titre)}</option>`).join('')}</optgroup>`).join('')}</select></label>
      <button class="btn primary" id="clGo" type="button">${ic('arrow')} Continuer</button>
    </div>${avert}`);
  el.querySelector('#clGo').onclick = () => { location.hash = 'colle/' + el.querySelector('#clF').value; };
  scrollTo(0, 0);
}

function accueil(el, f, typeset) {
  const der = memo.get(f.id);
  el.innerHTML = cadre(`<header class="fiche-head"><p class="kicker">${ic('msg')} Colleur virtuel · ${esc(f.mat)} ${esc(f.niveau)}</p><h1>${esc(f.titre)}</h1>
    <p class="small">Le colleur pose une question à la fois. Répondez comme au tableau : précis, avec les hypothèses et les unités.${der ? ` Dernière colle sur ce chapitre : <b>${der.note}/20</b>.` : ''}</p></header>${essai}
    <div class="panel pad colle-choix">
      <div class="fld"><span>Nombre de questions</span><div class="seg" role="group">${[5, 8, 10].map((n, i) => `<button type="button" aria-pressed="${i === 0}" data-n="${n}">${n}</button>`).join('')}</div></div>
      <button class="btn primary" id="clStart" type="button" ${CONFIG.COLLEUR ? '' : 'disabled'}>${ic('msg')} Commencer la colle</button>
      <a class="btn ghost" href="#f/${f.id}">${ic('book')} Revoir la fiche</a>
    </div>${CONFIG.COLLEUR ? '' : `<div class="panel pad"><p>${ic('clock')} Le colleur virtuel sera disponible très bientôt.</p></div>`}${avert}`);
  let n = 5;
  el.querySelectorAll('[data-n]').forEach(b => b.onclick = () => { n = +b.dataset.n; el.querySelectorAll('[data-n]').forEach(x => x.setAttribute('aria-pressed', x === b)); });
  el.querySelector('#clStart').onclick = () => {
    S = {fiche: f.id, titre: f.titre, n, tours: 0, messages: [], fil: [], fin: null, busy: false}; PH = [];
    appel(el, typeset, 'debut');
  };
  scrollTo(0, 0);
}

async function appel(el, typeset, action) {
  S.busy = true; S.err = ''; draw(el, typeset);
  try {
    const images = action !== 'debut' && S.attente?.length ? S.attente : undefined;
    const r = await api.colleur({fiche: S.fiche, action, questions: S.n, messages: S.messages, ...(images ? {images} : {})});
    // ce que le colleur a lu sur la photo remplace la photo dans l'historique : les tours suivants gardent le contexte sans renvoyer l'image
    if (images) { const m = S.messages[S.messages.length - 1]; m.content = `${m.content === PHOTO_SEULE ? '' : m.content + '\n\n'}[Réponse manuscrite en photo, lue par le colleur] ${r.lu || '(illisible)'}`; S.attente = null; }
    if (action === 'debut' && r.restantes != null) S.restantes = r.restantes;
    if (r.appreciation || r.question) {
      const txt = [r.appreciation, r.question].filter(Boolean).join('\n\n');
      S.messages.push({role: 'assistant', content: txt});
      S.fil.push({qui: 'colleur', appreciation: r.appreciation || '', statut: r.statut, question: action === 'bilan' ? '' : (r.question || '')});
    }
    if (action === 'bilan') { S.fin = r; memo.set(S.fiche, {note: r.note, date: Date.now()}); }
  } catch (e) {
    S.err = e.message || 'Le colleur n’a pas pu répondre.';
    if (S.attente?.length) {   // échec : la réponse n'est pas comptée, l'élève peut la renvoyer telle quelle
      const m = S.messages.pop(), e2 = S.fil.pop(); S.tours--; PH = S.attente; S.attente = null; S.brouillon = m.content === PHOTO_SEULE ? '' : m.content; void e2;
    }
    if (action === 'debut' && !S.fil.length) { const f = IDX.find(x => x.id === S.fiche); S = null; accueil(el, f, typeset); el.querySelector('.colle-choix').insertAdjacentHTML('afterend', `<p class="err">${esc(e.message)}</p>`); return; }
  }
  S.busy = false; draw(el, typeset);
}

function draw(el, typeset) {
  const fil = S.fil.map(m => m.qui === 'eleve'
    ? `<div class="cb cb-e"><div class="cb-t">Vous</div>${m.texte ? rich(m.texte) : ''}${vignettes(m.photos || [])}</div>`
    : `<div class="cb cb-c"><div class="cb-t">${ic('msg')} Colleur${m.statut && STAT[m.statut] ? ` <span class="cb-s ${STAT[m.statut][1]}">${STAT[m.statut][0]}</span>` : ''}</div>
        ${m.appreciation ? `<div class="cb-app">${rich(m.appreciation)}</div>` : ''}${m.question ? `<div class="cb-q">${rich(m.question)}</div>` : ''}</div>`).join('');
  const reste = S.n - S.tours;
  const saisie = S.fin ? '' : `<div class="panel pad colle-saisie">
      <textarea id="clR" rows="4" placeholder="Votre réponse… (formules : $E = mc^2$), ou une photo de votre feuille" ${S.busy ? 'disabled' : ''}></textarea>
      ${vignettes(PH, !S.busy)}
      <div class="colle-btns">
        <button class="btn primary" id="clSend" type="button" ${S.busy ? 'disabled' : ''}>${ic('arrow')} Répondre</button>
        <label class="btn${PH.length >= MAX_PHOTOS || S.busy ? ' is-off' : ''}" id="clPhL">${ic('camera')} Photo<input type="file" id="clPh" accept="image/*" multiple class="sr" ${PH.length >= MAX_PHOTOS || S.busy ? 'disabled' : ''}></label>
        ${SR ? `<button class="btn" id="clMic" type="button" ${S.busy ? 'disabled' : ''} aria-pressed="false">${ic('mic')} Dicter</button>` : ''}
        <button class="btn ghost" id="clPass" type="button" ${S.busy ? 'disabled' : ''}>Je ne sais pas</button>
        <button class="btn ghost" id="clStop" type="button" ${S.busy || !S.tours ? 'disabled' : ''}>Terminer et voir le bilan</button>
      </div>
      <p class="small">${S.busy ? 'Le colleur réfléchit…' : `Question ${Math.min(S.tours + 1, S.n)} sur ${S.n}${reste > 1 ? '' : ' (dernière)'}`}</p></div>`;
  const bilan = S.fin ? `<section class="panel pad colle-bilan"><h2 class="colle-bilan-t">Bilan de la colle</h2>
      <p class="colle-note"><b>${S.fin.note}</b>/20</p>
      ${S.fin.points_forts?.length ? `<h3>Points forts</h3><ul>${S.fin.points_forts.map(t => `<li>${inlineC(t)}</li>`).join('')}</ul>` : ''}
      ${S.fin.a_revoir?.length ? `<h3>À revoir</h3><ul>${S.fin.a_revoir.map(t => `<li>${inlineC(t)}</li>`).join('')}</ul>` : ''}
      ${S.fin.conseil ? `<p>${inlineC(S.fin.conseil)}</p>` : ''}
      <p class="small">Note indicative, donnée par une IA (version d'essai).</p>
      <div class="colle-btns"><a class="btn primary" href="#f/${S.fiche}">${ic('book')} Revoir la fiche</a><button class="btn" id="clNew" type="button">${ic('msg')} Nouvelle colle</button></div></section>` : '';
  el.innerHTML = cadre(`<header class="fiche-head"><p class="kicker">${ic('msg')} Colleur virtuel · <span class="colle-tag">Version d'essai</span></p><h1>${esc(S.titre)}</h1>${S.restantes != null ? `<p class="small">Colles restantes aujourd'hui après celle-ci : ${S.restantes}</p>` : ''}</header>
    <div class="colle-fil" aria-live="polite">${fil}${S.busy ? '<div class="cb cb-c cb-wait"><span></span><span></span><span></span></div>' : ''}</div>
    ${S.err ? `<p class="err">${esc(S.err)}</p>` : ''}${saisie}${bilan}`);
  typeset?.(el);
  const fin = el.querySelector('.colle-fil').lastElementChild;
  fin?.scrollIntoView({block: 'nearest', behavior: 'smooth'});
  if (S.fin) { el.querySelector('#clNew').onclick = () => { const f = IDX.find(x => x.id === S.fiche); S = null; accueil(el, f, typeset); }; return; }
  const ta = el.querySelector('#clR');
  if (S.brouillon) { ta.value = S.brouillon; S.brouillon = ''; }
  if (!S.busy) ta.focus({preventScroll: true});
  const envoyer = (txt, sansPhoto) => {
    txt = txt.trim(); const photos = sansPhoto ? [] : PH;
    if ((!txt && !photos.length) || S.busy) return;
    S.messages.push({role: 'user', content: txt || PHOTO_SEULE}); S.fil.push({qui: 'eleve', texte: txt, photos}); S.tours++;
    S.attente = photos.length ? photos : null; PH = [];
    appel(el, typeset, S.tours >= S.n ? 'bilan' : 'repondre');
  };
  const redessiner = () => { const v = ta.value; draw(el, typeset); el.querySelector('#clR').value = v; };
  el.querySelector('#clPh').onchange = async e => {
    const files = [...e.target.files].filter(f => f.type.startsWith('image/')).slice(0, MAX_PHOTOS - PH.length);
    for (const f of files) { try { PH.push(await reduire(f)); } catch { S.err = 'Cette image n’a pas pu être lue.'; } }
    redessiner();
  };
  el.querySelectorAll('[data-x]').forEach(b => b.onclick = () => { PH.splice(+b.dataset.x, 1); redessiner(); });
  el.querySelector('#clSend').onclick = () => envoyer(ta.value);
  ta.onkeydown = e => { if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) envoyer(ta.value); };
  el.querySelector('#clPass').onclick = () => envoyer('Je ne sais pas.', true);
  el.querySelector('#clStop').onclick = () => { if (S.tours) appel(el, typeset, 'bilan'); };
  const mic = el.querySelector('#clMic');
  if (mic) mic.onclick = () => dicter(mic, ta);
}

let REC = null;
function dicter(btn, ta) {
  if (REC) { REC.stop(); return; }
  REC = new SR(); REC.lang = 'fr-FR'; REC.interimResults = true; REC.continuous = true;
  const base = ta.value ? ta.value.trimEnd() + ' ' : '';
  REC.onresult = e => { ta.value = base + [...e.results].map(r => r[0].transcript).join(' '); };
  REC.onend = () => { REC = null; btn.setAttribute('aria-pressed', 'false'); btn.classList.remove('on'); };
  REC.onerror = () => REC?.stop();
  btn.setAttribute('aria-pressed', 'true'); btn.classList.add('on');
  REC.start();
}
