// Supabase Edge Function « corriger » : indice, corrigé, import d'énoncé, et les outils des trois modes de correction
// (rédaction rigoureuse, autre méthode, « expliquer davantage », « pourquoi cette méthode », analyse de la réponse de l'élève).
// Secrets à définir dans Supabase : ANTHROPIC_API_KEY (obligatoire), CLAUDE_MODEL (facultatif), LIMITE_JOUR (facultatif)
import { createClient } from "npm:@supabase/supabase-js@2";

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const MODEL = Deno.env.get("CLAUDE_MODEL") ?? "claude-sonnet-5-5";
const LIMITE = Number(Deno.env.get("LIMITE_JOUR") ?? "40");
const LV: Record<number, string> = { 1: "CCINP", 2: "Mines-Centrale", 3: "X-ENS" };
const json = (b: unknown, status = 200) => new Response(JSON.stringify(b), { status, headers: { ...CORS, "Content-Type": "application/json" } });
const clip = (s: unknown, n: number) => String(s ?? "").slice(0, n);

function regles(ex: any, hint: number) {
  return `Tu es examinateur de colle en classe préparatoire MP (niveau visé : ${LV[ex.niveau] ?? "MP"}). Matière : ${ex.mat}, chapitre : ${ex.chap}.
Règles impératives :
- Ne donne JAMAIS la solution complète ni le résultat final tant que l'élève ne l'a pas obtenu lui-même.
- Indices gradués : niveau 1 = piste globale (idée clé, concept de départ) ; niveau 2 = méthode précise (étape intermédiaire, outil ou théorème à employer). Donne UN seul indice, au niveau ${hint}.
- Exige la rigueur de l'oral : hypothèses des théorèmes, justifications, quantificateurs ; en physique : système, référentiel, bilan des forces, homogénéité, unités, ordres de grandeur.
- Français, phrases courtes, bienveillant mais exigeant. Toute formule en LaTeX entre $...$.
- Garde des étapes ("points") stables d'un retour à l'autre, formulées sans révéler les résultats.`;
}

// Exigences communes au corrigé et à sa relecture (format « 6 étapes » affiché par le site).
const REGLES_CORRIGE = `FORMAT OBLIGATOIRE du champ "corrige" (Markdown + LaTeX), six étapes dans cet ordre, chacune ouverte par une ligne en gras exactement de la forme :
**Étape 1 — Analyse de l'énoncé.** données, hypothèses, ce qu'il faut démontrer ou calculer (question par question).
**Étape 2 — Rappels du cours.** chaque théorème, définition ou propriété utilisé, dans un encadré : un paragraphe commençant par « > **Théorème — Nom.** » (ou Définition, Propriété, Loi, Formule) avec l'énoncé précis ET ses hypothèses.
**Étape 3 — Stratégie.** la méthode choisie et pourquoi elle est adaptée.
**Étape 4 — Résolution détaillée.** sous-parties « **4.1 Titre.** », « **4.2 Titre.** »… ; chaque égalité, inégalité ou transformation est justifiée (« car », « d'après », hypothèse vérifiée) ; aucune étape sautée ; calculs intermédiaires écrits.
**Étape 5 — Vérification.** au moins deux contrôles parmi : cas particulier, cas limite, recalcul par une autre voie, homogénéité et unités, signes, ordre de grandeur, rôle de chaque hypothèse (contre-exemple si on la retire). Un contrôle peut être mis en encadré « > **Vérification — …** ».
**Étape 6 — Conclusion.** résultat final dans $$\\boxed{…}$$.
RIGUEUR :
- Mathématiques : quantificateurs explicites, implications et équivalences correctes, hypothèses de chaque théorème vérifiées au moment de l'appliquer (continuité, intégrabilité, convergence, dimension finie…), cas d'égalité et cas limites traités.
- Physique et chimie : système, référentiel, lois utilisées et leurs conditions de validité, conventions de signe, approximations annoncées et justifiées (« > **Hypothèses — …** »), homogénéité vérifiée, applications numériques avec unités et un nombre raisonnable de chiffres significatifs.
- Informatique : spécification, invariant de boucle démontré (initialisation, conservation, terminaison), complexité justifiée.
- Ne présente jamais une intuition comme une preuve. Si une étape ne peut pas être établie avec certitude, écris-le dans un encadré « > **Point non démontré — …** » au lieu d'inventer une justification.
- Toute formule en LaTeX ($…$, $$…$$ pour les formules centrées, environnement aligned pour aligner plusieurs lignes). Pas de titre général.
CHAMPS : "reponse" = résultats finaux en une ou deux lignes ; "theoremes" = 1 à 4 éléments « **Nom.** énoncé avec hypothèses » ; "astuces" = 2 ou 3 réflexes (« Penser à … quand … »).`;

// Relecture indépendante : un second appel, qui n'a pas rédigé le corrigé, le contrôle et le corrige.
function promptRelecture(ex: any, brouillon: string) {
  return `Tu es un examinateur exigeant de concours (CCINP, Mines-Ponts, CentraleSupélec, X-ENS). Un collègue a rédigé le corrigé ci-dessous. Tu ne l'as pas écrit : relis-le de façon critique et INDÉPENDANTE.
1. Refais toi-même chaque calcul (signes, facteurs, bornes, unités) et chaque raisonnement ; vérifie les hypothèses de chaque théorème au moment où il est appliqué ; repère tout saut logique ou toute justification fausse ou absente.
2. Corrige toutes les erreurs et complète les justifications manquantes. Garde le format imposé ci-dessous.
3. Si un point reste douteux après ta relecture, signale-le dans un encadré « > **Point non démontré — …** » plutôt que de le masquer.

${REGLES_CORRIGE}

ÉNONCÉ :
${clip(ex.enonce, 6000)}

CORRIGÉ À RELIRE (JSON) :
${clip(brouillon, 24000)}

Réponds UNIQUEMENT avec un objet JSON valide : {"corrige":"…","reponse":"…","theoremes":["…"],"astuces":["…"],"verification":{"statut":"conforme|corrige|incertain","remarques":["erreurs trouvées et corrections faites, ou points incertains"]}}`;
}

function prompt(mode: string, b: any) {
  const ex = b.exercice ?? {};
  const hint = Math.max(1, Math.min(2, Number(b.hint) || 1));
  const hist = clip(b.historique, 4000) || "(aucun)";
  const ref = clip(b.reference, 9000);
  // Indices préparés : niveau 1 = piste globale ; niveau 2 = méthode précise (les indices 2 et 3 du professeur, regroupés).
  const ip = Array.isArray(b.indices) ? b.indices.map((t: unknown) => clip(t, 600)) : [];
  const ind = ip.length ? [`Niveau 1 (piste globale) : ${ip[0]}`, ip.length > 1 ? `Niveau 2 (méthode précise) : ${ip.slice(1).join(" ")}` : ""].filter(Boolean).join("\n") : "";
  const base = `${regles(ex, hint)}\n\nÉNONCÉ :\n${clip(ex.enonce, 6000)}` +
    (ref ? `\n\nCORRIGÉ DE RÉFÉRENCE DU PROFESSEUR (confidentiel : sers-t'en pour juger la copie, ne le recopie jamais et ne révèle pas les résultats) :\n${ref}` : "") +
    (ind ? `\n\nINDICES PRÉPARÉS PAR LE PROFESSEUR (reprends de préférence celui du niveau demandé, adapté à la copie) :\n${ind}` : "") +
    `\n\nRETOURS PRÉCÉDENTS :\n${hist}`;
  const note = b.note ? ` (message de l'élève : « ${clip(b.note, 600)} »)` : "";
  if (mode === "copie") return `${base}

TÂCHE : les photos jointes sont la copie manuscrite de l'élève${note}. Lis-la, vérifie chaque étape, situe la première erreur ou le premier manque. Si la photo est illisible ou hors sujet : verdict "illisible".
Réponds UNIQUEMENT avec un objet JSON valide :
{"verdict":"juste|partiel|faux|illisible","score":<entier 0-100>,"resume":"une phrase","points":[{"etape":"…","statut":"ok|erreur|manquant","note":"…"}],"retour":"2 à 4 phrases","indice":"indice de niveau ${hint}, vide si juste","question":"question d'examinateur"}`;
  if (mode === "indice") return `${base}

TÂCHE : l'élève bloque${note} et n'a pas envoyé de copie. Donne un indice de niveau ${hint} et une question qui le fait avancer.
Réponds UNIQUEMENT avec un objet JSON valide :
{"verdict":"bloque","score":null,"resume":"","points":[],"retour":"une phrase de méthode","indice":"…","question":"…"}`;
  if (mode === "solution") return `Tu es professeur en classe préparatoire MP et tu rédiges le corrigé de référence de l'exercice ci-dessous, au niveau ${LV[ex.niveau] ?? "MP"} (matière : ${ex.mat ?? "?"}, chapitre : ${ex.chap ?? "?"}).

${REGLES_CORRIGE}

ÉNONCÉ :
${clip(ex.enonce, 6000)}

Réponds UNIQUEMENT avec un objet JSON valide : {"corrige":"…","reponse":"…","theoremes":["…"],"astuces":["…"]}`;
  // import
  return `Retranscris fidèlement l'énoncé d'exercice de la photo (pas la solution). Formules en LaTeX entre $...$ ($$...$$ en display), questions numérotées "1.", "2." sur des lignes séparées. Classe-le pour une prépa MP.
Réponds UNIQUEMENT avec un objet JSON valide : {"titre":"…","mat":"Maths|Physique|Chimie","chap":"…","niveau":1|2|3,"duree":20,"enonce":"…"}`;
}


// ---------- Outils des trois modes de correction ----------
const FILIERES = ["MPSI", "MP", "MP*", "PCSI", "PC", "PSI", "MP2I", "MPI", "PTSI", "PT", "TSI", "BCPST"];
function contexte(b: any) {
  const ex = b.exercice ?? {};
  const fil = FILIERES.includes(String(b.filiere)) ? String(b.filiere) : "MP";
  const ref = clip(b.reference, 12000);
  return {
    ex, fil,
    tete: `Tu es professeur de classe préparatoire (filière ${fil}). Exercice de ${ex.mat ?? "?"}, chapitre ${ex.chap ?? "?"}, niveau ${LV[ex.niveau] ?? "MP"}.
PROGRAMME : reste dans le programme officiel de la filière ${fil}. Si un outil hors programme est indispensable, annonce-le dans un encadré « > **Attention — hors programme.** » et justifie son emploi.
HONNÊTETÉ : n'invente jamais un théorème, une hypothèse, une source ou un résultat. Si l'énoncé est ambigu ou incomplet, dis-le explicitement. Si tu ne peux pas établir un point avec certitude, écris-le dans un encadré « > **Point non démontré — …** ».
Toute formule en LaTeX ($…$, $$…$$ ; environnement aligned pour aligner des calculs). Français, phrases claires. Jamais « il est évident que » ou « on trouve facilement » quand une justification est nécessaire.

ÉNONCÉ :
${clip(ex.enonce, 6000)}` + (ref ? `\n\nCORRIGÉ DE RÉFÉRENCE (vérifié par l'équipe ; appuie-toi sur ses résultats et ne les modifie que si tu y trouves une erreur certaine, que tu signales alors) :\n${ref}` : ""),
  };
}

function promptOutil(mode: string, b: any) {
  const { tete } = contexte(b);
  if (mode === "rigoureux") return `${tete}

TÂCHE : rédige la solution comme une EXCELLENTE COPIE DE CONCOURS (CCINP, CentraleSupélec, Mines-Ponts, X-ENS).
- Une section par question, ouverte par une ligne en gras « **1.** », « **2.(a)** »… (ou « **Solution.** » s'il n'y a qu'une question).
- Définis les objets introduits et annonce les notations. Quantificateurs explicites (« Soit $\\varepsilon>0$. Il existe… »).
- Pour chaque théorème : nomme-le et vérifie ses hypothèses AU MOMENT où tu l'appliques.
- Démontre toute implication non triviale ; distingue condition nécessaire et condition suffisante ; traite les cas particuliers et les cas limites.
- Physique et chimie : système, référentiel, lois et leurs conditions de validité, conventions de signe, homogénéité, application numérique avec unités.
- Informatique : spécification, invariant de boucle (initialisation, conservation), terminaison, complexité.
- Chaque question se termine par une phrase de conclusion explicite ; le résultat principal est encadré par $$\\boxed{…}$$.
- Style concis de copie : pas de rappels de cours séparés, pas de commentaires pédagogiques.
Réponds UNIQUEMENT avec un objet JSON valide : {"redaction":"…","reponse":"résultats finaux en une ou deux lignes"}`;
  if (mode === "autre") return `${tete}

TÂCHE : propose une MÉTHODE DE RÉSOLUTION RÉELLEMENT DIFFÉRENTE de celle du corrigé de référence (autre outil, autre point de vue ; pas une simple reformulation). Rédige-la complètement et rigoureusement, avec des sous-parties « **1. Titre.** », « **2. Titre.** »…, et le résultat final dans $$\\boxed{…}$$, qui doit coïncider avec celui de la référence.
S'il n'existe pas d'autre méthode raisonnable au programme, dis-le simplement (existe = false) au lieu d'en inventer une.
Réponds UNIQUEMENT avec un objet JSON valide : {"existe":true,"titre":"nom court de la méthode","methode":"…","comparaison":"2 ou 3 phrases : avantages, limites, quand préférer chaque méthode"}`;
  if (mode === "expliquer") return `${tete}

ÉTAPE DU CORRIGÉ QUE L'ÉLÈVE VEUT MIEUX COMPRENDRE :
${clip(b.etape, 5000)}
${b.question ? `\nQUESTION DE L'ÉLÈVE : « ${clip(b.question, 500)} »\n` : ""}
TÂCHE : explique cette étape plus lentement, pour un élève de prépa qui bloque : chaque transformation ou calcul intermédiaire, pourquoi il est légitime (quelle hypothèse, quel théorème), et l'idée qui guide l'étape. Ne traite pas les étapes suivantes. Si tu vois une erreur dans l'étape, signale-la clairement au lieu de la justifier.
Réponds UNIQUEMENT avec un objet JSON valide : {"explication":"…"}`;
  if (mode === "pourquoi") return `${tete}

TÂCHE : explique POURQUOI la méthode employée dans le corrigé de référence est adaptée : quels indices de l'énoncé y conduisent, quelles autres pistes viendraient à l'esprit et pourquoi elles sont moins efficaces, et le réflexe à retenir. 6 à 10 phrases, sans refaire la résolution.
Réponds UNIQUEMENT avec un objet JSON valide : {"pourquoi":"…"}`;
  // analyse de la réponse de l'élève
  return `${tete}

RÉPONSE OU DÉMARCHE DE L'ÉLÈVE :
${clip(b.reponse_eleve, 4000)}

TÂCHE : analyse cette réponse SANS donner la solution complète ni recopier le corrigé.
- Si elle est juste : dis-le, puis signale ce qui manque éventuellement en rigueur ou en justification.
- Sinon : identifie précisément la PREMIÈRE erreur (cite le passage), classe-la (calcul, méthode, raisonnement, rédaction), explique pourquoi la démarche devient incorrecte à cet endroit, et donne une piste pour reprendre à partir de là.
- Si la réponse est trop courte ou illisible pour juger, dis-le (verdict "incomplet") et demande ce qu'il faudrait préciser.
- Ne sois jamais plus affirmatif que ce que tu peux vérifier.
Réponds UNIQUEMENT avec un objet JSON valide : {"verdict":"juste|partiel|faux|incomplet","resume":"une phrase","points_justes":["…"],"premiere_erreur":{"citation":"…","type":"calcul|methode|raisonnement|redaction","explication":"…"},"piste":"…"} (premiere_erreur = null si aucune erreur).`;
}

// Relecture indépendante courte : un second appel contrôle le contenu produit et renvoie un verdict, sans le réécrire.
function promptControle(b: any, contenu: string) {
  const { tete } = contexte(b);
  return `${tete}

Un collègue a rédigé le texte ci-dessous. Tu ne l'as pas écrit. Contrôle-le de façon INDÉPENDANTE : refais chaque calcul (signes, facteurs, bornes, unités), vérifie les hypothèses de chaque théorème appliqué et la logique de chaque implication, compare les résultats à la référence s'il y en a une.

TEXTE À CONTRÔLER :
${clip(contenu, 20000)}

Réponds UNIQUEMENT avec un objet JSON valide : {"statut":"conforme|incertain|erreur","remarques":["chaque problème précis trouvé, ou point que tu n'as pas pu vérifier"]}`;
}
const OUTILS: Record<string, { max: number; controle: boolean; cache: boolean }> = {
  rigoureux: { max: 7000, controle: true, cache: true },
  autre: { max: 5000, controle: true, cache: true },
  expliquer: { max: 2500, controle: false, cache: true },
  pourquoi: { max: 1500, controle: false, cache: true },
  analyse: { max: 1800, controle: false, cache: false },
};
async function empreinte(mode: string, b: any) {
  const ex = b.exercice ?? {};
  const txt = JSON.stringify([mode, MODEL, String(ex.enonce ?? ""), String(b.reference ?? ""), String(b.filiere ?? ""), String(b.etape ?? ""), String(b.question ?? "")]);
  const h = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(txt));
  return [...new Uint8Array(h)].map((x) => x.toString(16).padStart(2, "0")).join("");
}

function parse(t: string) {
  const a = t.indexOf("{"), b = t.lastIndexOf("}");
  if (a < 0 || b < a) throw new Error("Réponse illisible");
  return JSON.parse(t.slice(a, b + 1));
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  if (req.method !== "POST") return json({ error: "Méthode non autorisée" }, 405);
  const key = Deno.env.get("ANTHROPIC_API_KEY");
  if (!key) return json({ error: "Clé ANTHROPIC_API_KEY absente côté serveur." }, 500);

  const auth = req.headers.get("Authorization") ?? "";
  const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const { data: u } = await admin.auth.getUser(auth.replace("Bearer ", ""));
  if (!u?.user) return json({ error: "Connexion requise." }, 401);
  const uid = u.user.id;
  const { data: prof } = await admin.from("profiles").select("role").eq("id", uid).single();
  const isProf = prof?.role === "prof";

  let body: any;
  try { body = await req.json(); } catch { return json({ error: "Requête invalide." }, 400); }
  const mode = String(body.mode);
  // L'évaluation automatique des copies est remplacée par la soumission sur l'honneur et la notation entre pairs.
  if (mode === "copie") return json({ error: "La correction automatique des copies est désactivée : soumets ta réponse à ton groupe." }, 410);
  const outil = Object.hasOwn(OUTILS, mode) ? OUTILS[mode] : undefined;
  if (!outil && !["indice", "solution", "import"].includes(mode)) return json({ error: "Mode inconnu." }, 400);
  if (mode === "analyse" && !String(body.reponse_eleve ?? "").trim()) return json({ error: "Écris d'abord ta réponse ou ta démarche." }, 400);
  if (outil && !String(body.exercice?.enonce ?? "").trim()) return json({ error: "Énoncé manquant." }, 400);

  // Contenus partagés déjà générés : renvoyés sans nouvel appel à l'IA (ni décompte du quota).
  let cle = "";
  if (outil?.cache) {
    cle = await empreinte(mode, body);
    const { data: c } = await admin.from("corrections_ia").select("contenu").eq("cle", cle).maybeSingle();
    if (c?.contenu) return json({ ...c.contenu, cache: true });
  }
  if (mode === "import" && !isProf) return json({ error: "Réservé au professeur." }, 403);

  if (!isProf) {
    const depuis = new Date(); depuis.setHours(0, 0, 0, 0);
    const { count } = await admin.from("ia_usage").select("id", { count: "exact", head: true }).eq("user_id", uid).gte("created_at", depuis.toISOString());
    if ((count ?? 0) >= LIMITE) return json({ error: `Limite de ${LIMITE} demandes par jour atteinte. Reviens demain !` }, 429);
  }

  const images: string[] = Array.isArray(body.images) ? body.images.slice(0, 4) : [];
  if ((mode === "copie" || mode === "import") && !images.length) return json({ error: "Aucune image reçue." }, 400);
  const content: any[] = images.map((d) => ({ type: "image", source: { type: "base64", media_type: "image/jpeg", data: String(d).replace(/^data:image\/\w+;base64,/, "") } }));
  content.push({ type: "text", text: prompt(mode, body) });

  const appel = async (contenu: any[], max: number) => {
    const r = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: { "x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json" },
      body: JSON.stringify({ model: MODEL, max_tokens: max, messages: [{ role: "user", content: contenu }] }),
    });
    if (!r.ok) throw new Error((await r.text()).slice(0, 300));
    const out = await r.json();
    if (out.stop_reason === "max_tokens") throw new Error("Réponse tronquée");
    return (out.content ?? []).filter((c: any) => c.type === "text").map((c: any) => c.text).join("\n");
  };

  if (outil) {
    let res: any;
    try { res = parse(await appel([{ type: "text", text: promptOutil(mode, body) }], outil.max)); }
    catch (e) {
      const trop = String(e).includes("tronquée");
      return json({ error: trop ? "La réponse était trop longue et a été coupée : réessaie, ou utilise le mode détaillé." : "Le service de correction n'a pas pu répondre. Réessaie dans un instant." }, 502);
    }
    await admin.from("ia_usage").insert({ user_id: uid, mode });
    const texte = mode === "rigoureux" ? res.redaction : mode === "autre" ? res.methode : mode === "expliquer" ? res.explication : mode === "pourquoi" ? res.pourquoi : "ok";
    if (!texte || typeof texte !== "string") { if (!(mode === "autre" && res.existe === false)) return json({ error: "Réponse de l'IA incomplète, réessaie." }, 502); }
    if (outil.controle && texte && !(mode === "autre" && res.existe === false)) {
      try {
        const v = parse(await appel([{ type: "text", text: promptControle(body, texte) }], 1500));
        res.verification = { statut: ["conforme", "incertain", "erreur"].includes(v.statut) ? v.statut : "incertain", remarques: Array.isArray(v.remarques) ? v.remarques.slice(0, 8).map(String) : [] };
      } catch { res.verification = { statut: "non_relu", remarques: [] }; }
    }
    // On ne met en cache que ce qui n'a pas été jugé faux par la relecture : une nouvelle demande pourra faire mieux.
    if (cle && res.verification?.statut !== "erreur" && res.verification?.statut !== "non_relu") {
      await admin.from("corrections_ia").upsert({ cle, exercice_id: clip(body.exercice?.id || "?", 80), type: mode, contenu: res }, { onConflict: "cle", ignoreDuplicates: true });
    }
    return json(res);
  }
  let text: string;
  try { text = await appel(content, mode === "solution" ? 8000 : 1500); }
  catch (e) { return json({ error: "Le service de correction a refusé la demande.", detail: String(e).slice(0, 300) }, 502); }
  await admin.from("ia_usage").insert({ user_id: uid, mode });
  if (mode === "solution") {
    // Contrôle qualité : seconde passe de relecture critique avant tout affichage.
    let brouillon: any;
    try { brouillon = parse(text); } catch { brouillon = { corrige: text }; }
    try {
      const relu = parse(await appel([{ type: "text", text: promptRelecture(body.exercice ?? {}, JSON.stringify(brouillon)) }], 10000));
      if (relu?.corrige) return json({ ...relu, relu: true });
    } catch { /* relecture indisponible : on renvoie le brouillon, signalé comme non relu */ }
    return json({ ...brouillon, relu: false });
  }
  try { return json(parse(text)); }
  catch { return json({ error: "Réponse de l'IA illisible, réessaie." }, 502); }
});
