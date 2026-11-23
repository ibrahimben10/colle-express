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
- Indices gradués : niveau 1 = piste générale ; niveau 2 = méthode ou théorème précis ; niveau 3 = étape concrète. Donne UN seul indice, au niveau ${hint}.
- Exige la rigueur de l'oral : hypothèses des théorèmes, justifications, quantificateurs ; en physique : système, référentiel, bilan des forces, homogénéité, unités, ordres de grandeur.
- Français, phrases courtes, bienveillant mais exigeant. Toute formule en LaTeX entre $...$.
- Garde des étapes ("points") stables d'un retour à l'autre, formulées sans révéler les résultats.`;
}

function prompt(mode: string, b: any) {
  const ex = b.exercice ?? {};
  const hint = Math.max(1, Math.min(3, Number(b.hint) || 1));
  const hist = clip(b.historique, 4000) || "(aucun)";
  const ref = clip(b.reference, 9000);
  const ind = Array.isArray(b.indices) ? b.indices.slice(0, 3).map((t: unknown, i: number) => `Niveau ${i + 1} : ${clip(t, 600)}`).join("\n") : "";
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
  if (mode === "solution") return `Tu es professeur en classe préparatoire MP. Rédige un corrigé complet, rigoureux et concis de l'exercice suivant, comme attendu à l'oral (${LV[ex.niveau] ?? "MP"}). Structure par questions, justifie les théorèmes, termine par une remarque de méthode. Formules en LaTeX entre $...$. Pas de titre.

ÉNONCÉ :
${clip(ex.enonce, 6000)}

Réponds UNIQUEMENT avec un objet JSON valide : {"corrige":"…"}`;
  // import
  return `Retranscris fidèlement l'énoncé d'exercice de la photo (pas la solution). Formules en LaTeX entre $...$ ($$...$$ en display), questions numérotées "1.", "2." sur des lignes séparées. Classe-le pour une prépa MP.
Réponds UNIQUEMENT avec un objet JSON valide : {"titre":"…","mat":"Maths|Physique|Chimie","chap":"…","niveau":1|2|3,"duree":20,"enonce":"…","source":"…"}`;
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
  if (!["copie", "indice", "solution", "import"].includes(mode)) return json({ error: "Mode inconnu." }, 400);
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

  const r = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: { "x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json" },
    body: JSON.stringify({ model: MODEL, max_tokens: mode === "solution" ? 3000 : 1500, messages: [{ role: "user", content }] }),
  });
  if (!r.ok) return json({ error: "Le service de correction a refusé la demande.", detail: (await r.text()).slice(0, 300) }, 502);
  const out = await r.json();
  const text = (out.content ?? []).filter((c: any) => c.type === "text").map((c: any) => c.text).join("\n");
  await admin.from("ia_usage").insert({ user_id: uid, mode });
  try { return json(parse(text)); }
  catch { return mode === "solution" ? json({ corrige: text }) : json({ error: "Réponse de l'IA illisible, réessaie." }, 502); }
});
