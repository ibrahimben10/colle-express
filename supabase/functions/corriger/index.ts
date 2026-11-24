// Supabase Edge Function « corriger » : correction de copie, indice, corrigé, import d'énoncé.
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
  if (!["indice", "solution", "import"].includes(mode)) return json({ error: "Mode inconnu." }, 400);
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
    return (out.content ?? []).filter((c: any) => c.type === "text").map((c: any) => c.text).join("\n");
  };
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
