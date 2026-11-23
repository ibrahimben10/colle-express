# Colle express — Prépa MP

Site de colles courtes de maths et de physique-chimie pour la prépa MP, par **BEN YAKHLEF IBRAHIM**.

- 151 exercices d’oraux classés en 3 niveaux : **CCINP**, **Mines-Centrale**, **X-ENS**
- 36 schémas dessinés pour les énoncés de physique-chimie
- Pour **chaque** exercice : 3 indices gradués et un corrigé complet et détaillé (`data/corriges.json`)
- Comptes élèves (e-mail + mot de passe) protégés par un **code de classe**
- L’élève photographie sa copie : l’IA (Claude) valide les étapes, pointe la première erreur et donne **un indice gradué** — le corrigé n’est accessible qu’après 2 copies ou une réussite
- **Suivi** de chaque élève par chapitre, historique, exercices conseillés
- **Tableau de bord** du professeur : élèves connectés **en temps réel**, fil d’activité, progression de chaque élève, message et sélection d’exercices pour la classe, ajout d’exercices (y compris par photo)

Le site est **statique** (hébergé gratuitement par GitHub Pages). Les comptes, le suivi et le temps réel passent par **Supabase** (gratuit), et la correction par l’**API Claude** d’Anthropic (payante, à l’usage).

---

## Mise en ligne pas à pas (≈ 30 minutes)

### Étape 1 — Publier le site sur GitHub Pages

1. Sur GitHub, ouvre le dépôt `colle-express` → **Settings** → **Pages**.
2. *Source* : **Deploy from a branch** ; *Branch* : **main**, dossier **/ (root)** → **Save**.
3. Après 1 à 2 minutes, le site est en ligne à l’adresse :
   **https://ibrahimben10.github.io/colle-express/**

À ce stade il fonctionne en **mode démonstration** (bandeau orange) : tout est navigable, mais rien n’est partagé entre élèves et la correction IA est désactivée.

### Étape 2 — Créer la base de données (Supabase)

1. Crée un compte sur **https://supabase.com** puis **New project** (région : *West EU (Paris)* ou *Frankfurt*). Note le mot de passe de la base quelque part.
2. Dans le projet : menu **SQL Editor** → **New query** → colle **tout** le contenu du fichier [`supabase/schema.sql`](supabase/schema.sql) → **Run**. Tu dois voir « Success ».
3. Menu **Authentication** → **URL Configuration** :
   - *Site URL* : `https://ibrahimben10.github.io/colle-express/`
   - *Redirect URLs* : ajoute la même adresse.
4. (Conseillé) **Authentication** → **Sign In / Providers** → **Email** : tu peux laisser « Confirm email » activé (l’élève confirme son adresse) ou le désactiver pour aller plus vite en classe.

### Étape 3 — Relier le site à Supabase

1. Dans Supabase : **Project Settings** → **API** (ou **Data API**). Copie :
   - **Project URL** (ex. `https://abcdxyz.supabase.co`)
   - la clé **anon public** (longue chaîne qui commence par `eyJ…`). *Ne copie jamais la clé `service_role`.*
2. Sur GitHub, ouvre le fichier **`js/config.js`** → icône crayon (Edit) → remplis :
   ```js
   SUPABASE_URL: 'https://abcdxyz.supabase.co',
   SUPABASE_ANON_KEY: 'eyJ...',
   ```
   → **Commit changes**. Le site se met à jour en 1 à 2 minutes.

### Étape 4 — Activer la correction par l’IA

1. Crée une clé API sur **https://console.anthropic.com** → *API Keys* → **Create Key** (ajoute un peu de crédit dans *Billing* ; une correction de copie coûte de l’ordre de quelques centimes).
2. Dans Supabase : **Edge Functions** → **Deploy a new function** → **Via Editor** :
   - Nom de la fonction : **`corriger`** (exactement)
   - Remplace le code par le contenu de [`supabase/functions/corriger/index.ts`](supabase/functions/corriger/index.ts) → **Deploy**.
3. **Edge Functions** → **Secrets** (ou *Project Settings → Edge Functions*) → ajoute :
   - `ANTHROPIC_API_KEY` = ta clé `sk-ant-…`
   - (facultatif) `LIMITE_JOUR` = nombre max. de demandes IA par élève et par jour (40 par défaut)
   - (facultatif) `CLAUDE_MODEL` = modèle utilisé (`claude-sonnet-5-5` par défaut)

> Alternative en ligne de commande : `npx supabase login`, `npx supabase link --project-ref <ref>`, `npx supabase functions deploy corriger`, `npx supabase secrets set ANTHROPIC_API_KEY=sk-ant-...`

### Étape 5 — Devenir professeur

1. Va sur le site → **Créer un compte** avec ton e-mail. Code de classe par défaut : **`MP2026`**.
2. Dans Supabase → **SQL Editor**, exécute (avec ton adresse) :
   ```sql
   update public.profiles set role = 'prof'
   where id = (select id from auth.users where email = 'ton.email@exemple.fr');
   ```
3. Déconnecte-toi / reconnecte-toi : l’onglet **Tableau de bord** apparaît.
4. Dans le tableau de bord, en bas : **change le code de la classe** (sinon n’importe qui connaissant `MP2026` pourrait s’inscrire).

### Étape 6 — Partager avec les élèves

Donne-leur simplement :
- l’adresse : **https://ibrahimben10.github.io/colle-express/**
- le **code de la classe**

Chaque élève crée son compte (nom, e-mail, mot de passe, niveau visé) et retrouve son suivi sur tous ses appareils. Le site s’utilise aussi bien sur téléphone (photo de la copie directement depuis l’appareil photo).

---

## Modifier le site

| Je veux… | Fichier |
|---|---|
| Changer mon nom, le titre | `js/config.js` (`NOM_PROF`, `NOM_SITE`) |
| Ajouter des exercices | Tableau de bord → *Ajouter un exercice* (ou `data/exercices.json`) |
| Ajouter / modifier un schéma | `js/figures.js` (clé = identifiant de l’exercice) |
| Modifier un indice ou un corrigé | `data/corriges.json` (clé = identifiant de l’exercice ; sources lisibles dans `tools/corr_*.py`) |
| Couleurs, polices | `css/style.css` |
| Consignes données à l’IA | `supabase/functions/corriger/index.ts` (puis redéployer la fonction) |

Format d’un exercice dans `data/exercices.json` :
```json
{"id":"p-meca-1","mat":"Physique","chap":"Mécanique","niveau":1,"concours":"CCINP/CCS",
 "titre":"Sismographe","enonce":"Texte avec formules LaTeX entre $...$","duree":20}
```
`niveau` : 1 = CCINP, 2 = Mines-Centrale, 3 = X-ENS.

## Sécurité et coûts

- Les indices préparés et les corrigés s’affichent sans appel à l’IA (gratuit, instantané). Le corrigé n’apparaît dans l’interface qu’après 2 copies corrigées, une réussite ou les 3 indices ; mais le fichier `data/corriges.json` est public : un élève curieux peut le lire directement.

- Les règles de sécurité (RLS) de Supabase empêchent un élève de lire le suivi des autres ; seul le professeur voit toute la classe.
- La clé Anthropic reste côté serveur (Edge Function) : elle n’apparaît jamais dans le site.
- Chaque élève est limité à `LIMITE_JOUR` demandes IA par jour. Surveille ta consommation sur console.anthropic.com (tu peux y fixer une limite de dépense mensuelle).
- Les corrections sont générées par IA : elles peuvent se tromper, encourage les élèves à vérifier avec leur cours.

## Modifier la présentation « À propos »

Le texte de présentation, le parcours et le contact se trouvent dans `js/config.js`, rubrique `PRESENTATION`. Modifie-les directement sur GitHub (icône crayon), puis « Commit changes » : le site est mis à jour en une minute.

## Partager un corrigé en PDF

Chaque exercice a une page publique `correction.html?id=…` (énoncé, schéma, indices, corrigé), lisible sans compte. Le bouton « PDF / Imprimer » ouvre l’export du navigateur : « Enregistrer au format PDF » sur ordinateur et Android, « Imprimer » puis « Partager » sur iPhone.

## Recevoir les sujets d'oraux envoyés par les élèves

L'onglet « À propos » contient un formulaire « Enrichir la plateforme » : l'élève joint un PDF, qui arrive en pièce jointe dans la boîte `ENVOI_EMAIL` (réglée dans `js/config.js`), via le service gratuit FormSubmit.

**Au tout premier envoi**, FormSubmit envoie à cette adresse un e-mail « Activate Form » : il faut cliquer sur le bouton d'activation, sinon les envois suivants ne sont pas transmis. Fais toi-même un premier envoi test juste après la mise en ligne.

## Photo de profil

Chaque élève peut ajouter une photo (onglet « Mon suivi » ou clic sur son avatar en haut). Elle est recadrée et compressée sur l'appareil (160 × 160 px), puis enregistrée avec son suivi : aucune configuration supplémentaire n'est nécessaire.

## Ajouter des exercices en lot

Les exercices ajoutés en lot sont écrits dans `tools/new_*.py` (énoncé, 3 indices, corrigé). Pour régénérer les fichiers de données : `python3 tools/build_new.py`.
