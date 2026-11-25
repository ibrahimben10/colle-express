# Colle express — Prépa MP

Site de colles courtes de maths et de physique-chimie pour la prépa MP, par **BEN YAKHLEF IBRAHIM**.

- 151 exercices d’oraux classés en 3 niveaux : **CCINP**, **Mines-Centrale**, **X-ENS**
- 36 schémas dessinés pour les énoncés de physique-chimie
- Pour **chaque** exercice : 3 indices gradués et un corrigé complet et détaillé (`data/corriges.json`)
- Comptes élèves (e-mail + mot de passe) protégés par un **code de classe**
- **Groupes d’étudiants** avec rôles (responsable, modérateur, membre) : on rejoint un groupe avec son code d’invitation
- **Réponse sur l’honneur** : l’élève coche un engagement sur l’honneur puis soumet sa réponse (texte LaTeX et/ou photos) ; elle devient **immédiatement visible** par les membres de son groupe et n’est plus modifiable
- **Notation par les pairs de 0 à 10** et **fil de discussion** sous chaque exercice (commentaires liés ou non à une réponse)
- Le corrigé s’ouvre après l’envoi de sa réponse ou les deux indices ; consulter le corrigé ou les autres réponses avant d’envoyer la sienne ajoute la mention « aide consultée »
- **Suivi** de chaque élève par chapitre, historique, exercices conseillés
- **Tableau de bord** du professeur : élèves connectés **en temps réel**, fil d’activité, progression de chaque élève, message et sélection d’exercices pour la classe, ajout d’exercices (y compris par photo)

Le site est **statique** (hébergé gratuitement par GitHub Pages). Les comptes, le suivi et le temps réel passent par **Supabase** (gratuit), et l’**API Claude** d’Anthropic (facultative, payante à l’usage) sert seulement aux indices et corrigés des exercices ajoutés par le professeur et à l’import d’énoncés par photo. La correction automatique des copies est désactivée.

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
   - *Redirect URLs* : ajoute `https://ibrahimben10.github.io/colle-express/**` (le `**` autorise `index.html` : c'est là que pointent les liens de confirmation et de réinitialisation).
4. **Indispensable pour les e-mails (mot de passe oublié, confirmation)** : **Authentication** → **Emails** → **SMTP Settings** → active *Custom SMTP* (Brevo, Resend… ont une offre gratuite). Sans cela, Supabase n'envoie les e-mails qu'aux membres de ton équipe Supabase, 2 par heure au plus : les élèves ne recevraient rien. Puis **Authentication** → **Rate Limits** pour régler le nombre d'e-mails par heure.
5. **Authentication** → **Sign In / Providers** → **Email** : mets *Minimum password length* à **8** (comme le site) et laisse *Email OTP Expiration* à 3600 s (lien valable 1 h, à usage unique).
6. (Conseillé) **Authentication** → **Sign In / Providers** → **Email** : tu peux laisser « Confirm email » activé (l’élève confirme son adresse) ou le désactiver pour aller plus vite en classe.

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

### Étape 4 (facultative) — Activer l’IA pour les exercices ajoutés

Sans cette étape, tout fonctionne (groupes, réponses, notes, discussion, indices et corrigés des exercices fournis) ; seuls les exercices que tu ajoutes toi-même n’ont pas d’indice ni de corrigé automatique.

1. Crée une clé API sur **https://console.anthropic.com** → *API Keys* → **Create Key** (ajoute un peu de crédit dans *Billing* ; un corrigé coûte quelques centimes).
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

- Les indices préparés et les corrigés s’affichent sans appel à l’IA (gratuit, instantané). Le corrigé n’apparaît dans l’interface qu’après l’envoi de sa réponse ou les indices ; mais le fichier `data/corriges.json` est public : un élève curieux peut le lire directement.

- Les règles de sécurité (RLS) de Supabase empêchent un élève de lire le suivi des autres ; seul le professeur voit toute la classe.
- La clé Anthropic reste côté serveur (Edge Function) : elle n’apparaît jamais dans le site.
- Chaque élève est limité à `LIMITE_JOUR` demandes IA par jour. Surveille ta consommation sur console.anthropic.com (tu peux y fixer une limite de dépense mensuelle).
- Les corrections sont générées par IA : elles peuvent se tromper, encourage les élèves à vérifier avec leur cours.

## Profils personnels (`#u/identifiant`)

**À faire une fois** : recolle **tout** `supabase/schema.sql` dans *SQL Editor* → *Run*. Le script peut être relancé sans risque. Il crée un profil pour chaque compte existant, avec un identifiant tiré du nom (`chloe_martin`), et reprend l'historique **réel** : réponses déjà soumises et journal de suivi.

- **Confidentialité** : chaque profil est **privé par défaut**. Rendu public, il n'est visible que des **membres connectés**, jamais d'Internet. Statistiques, carte d'activité, parcours, favoris, commentaires publics et étoiles se masquent un par un. L'e-mail n'est jamais affiché. « Voir comme les autres » montre exactement ce que voient les autres membres.
- **Comptage** : *consulté* = énoncé ouvert ; *travaillé* = indice demandé ou réponse soumise ; *terminé* = réponse soumise sur l'honneur ; *réussi* = au moins 2 notes de camarades avec une moyenne ≥ 12/20 ; *sans aide* = soumis sans indice ni corrigé. Ouvrir le corrigé n'est jamais une réussite. Le navigateur ne peut ni antidater une activité ni écrire pour un autre élève.
- **Étoiles (1 à 5)** : une note par membre et par profil, impossible de se noter soi-même ou de noter un profil privé. Les auteurs restent anonymes : un élève ne voit que ses propres notes. La moyenne n'apparaît qu'à partir de 3 notes. L'administrateur voit qui a noté et peut supprimer une note abusive (« Modération des étoiles » sur le profil).
- **Commentaires** : sous chaque exercice, l'auteur choisit *Groupe* (privé) ou *Public* (tous les membres + son profil). Une réponse à la réponse d'un camarade reste dans le groupe. La visibilité ne peut plus changer après publication.
- **Contributions** : l'envoi d'un sujet PDF part toujours vers l'adresse fixe `ENVOI_EMAIL` de `js/config.js`, que les élèves ne peuvent pas modifier. Le profil affiche seulement le nombre de sujets envoyés.

## Carnet, objectifs, collections et badges

Recolle **tout** `supabase/schema.sql` après chaque mise à jour, comme pour les profils.

- **Carnet de progression** (onglet *Carnet*, ou bouton *Carnet* sur un exercice) : exercices difficiles, à refaire, erreurs fréquentes, théorèmes à revoir, démonstrations, notes de révision, et « Ce que j'ai appris ». **Privé** : même l'administrateur ne lit que les notes publiées volontairement sur le profil.
- **Objectifs** : 4 types (exercices travaillés, chapitres abordés, exercices du carnet refaits, réponses sans aide), avec domaine facultatif et date de fin (6 mois au plus). La progression est **calculée par le serveur** sur l'activité réelle : rien ne se coche à la main. Un objectif peut être affiché sur le profil. Une période terminée affiche un bilan neutre, sans message culpabilisant.
- **Collections** (bouton *Collection* sur un exercice) : ordre modifiable, partage avec les membres (`#c/…`) si le profil est public.
- **Badges** : Premier pas, Régularité (7 jours d'affilée), Explorateur (5 chapitres), Polyvalent (3 domaines), Autonome (10 réponses sans aide), Reconnu par ses pairs (5 réussites), Persévérant (5 exercices refaits), Passionné (15 exercices d'un domaine), Contributeur. Ils sont recalculés par le serveur à chaque affichage et ne peuvent pas être attribués depuis le site. Les autres membres ne voient que les badges obtenus.
- Les métadonnées des exercices (matière, chapitre) sont copiées dans la base pour ces calculs. Après avoir ajouté des exercices dans `data/exercices.json`, lance `python3 tools/build_meta.py`, puis recolle `schema.sql`.

## Format des corrigés (« 6 étapes »)

Les corrigés suivent progressivement un format unique : **1. Analyse de l'énoncé · 2. Rappels du cours · 3. Stratégie · 4. Résolution détaillée · 5. Vérification · 6. Conclusion encadrée**.

- Dans `tools/detail/d*.py`, un corrigé s'écrit en Markdown + LaTeX :
  - « `**Étape 3 — Stratégie.**` » ouvre une étape ;
  - « `**4.2 Titre.**` » ouvre une sous-partie ;
  - un paragraphe commençant par « `> **Théorème — Nom.**` » devient un encadré (Théorème / Définition / Hypothèses / Attention / Vérification / Point non démontré).
- `python3 tools/build_detail.py` reconstruit `data/corriges.json`.
- Pilote : `tools/detail/d60.py` (6 exercices). Les autres corrigés gardent l'ancien format question par question jusqu'à leur conversion.
- **Corrigés générés par l'IA** (exercices ajoutés par photo) : la fonction `corriger` rédige au format 6 étapes, puis un **second appel indépendant relit** le corrigé (recalculs, hypothèses, sauts logiques) et le corrige. Le site affiche « relue par une seconde passe automatique » et les remarques de relecture. Après modification, **redéploie la fonction** : Supabase → *Edge Functions* → `corriger` → coller `supabase/functions/corriger/index.ts` → *Deploy*. Chaque corrigé IA compte pour deux appels à l'API Claude.

## Connexion, inscription et mot de passe oublié

- Tout est géré par **Supabase Auth** : les mots de passe sont hachés (bcrypt) côté serveur, jamais stockés en clair, et les liens de réinitialisation sont signés, temporaires et à usage unique.
- Le site vérifie le format de l'adresse **avant** tout envoi (`js/validation.js`) ; Supabase refait la vérification côté serveur.
- « Mot de passe oublié » n'affiche la confirmation — neutre : « Si un compte est associé à cette adresse… » — qu'après acceptation par Supabase. Une erreur technique affiche un message d'erreur, jamais une fausse confirmation. En mode démonstration, aucun envoi n'est simulé.
- Anti-abus : un seul envoi à la fois, 60 s entre deux demandes de lien, connexion bloquée 30 s (puis 1 min, 2 min…) après 5 échecs. Ces limites du navigateur complètent celles du serveur (Authentication → Rate Limits).
- Lien expiré ou déjà utilisé : l'élève est ramené au formulaire « Mot de passe oublié » avec un message clair.
- Code : `js/auth.js` (interface), `js/api.js` (appels Supabase et classement des erreurs), `js/validation.js` (règles).

## Modifier la présentation « À propos »

Le texte de présentation, le parcours et le contact se trouvent dans `js/config.js`, rubrique `PRESENTATION`. Modifie-les directement sur GitHub (icône crayon), puis « Commit changes » : le site est mis à jour en une minute.

## Partager un corrigé en PDF

Chaque exercice a une page publique `correction.html?id=…` (énoncé, schéma, indices, corrigé), lisible sans compte. Le bouton « PDF / Imprimer » ouvre l’export du navigateur : « Enregistrer au format PDF » sur ordinateur et Android, « Imprimer » puis « Partager » sur iPhone.

## Recevoir les sujets d'oraux envoyés par les élèves

L'onglet « À propos » contient un formulaire « Enrichir la plateforme » : l'élève joint un PDF, qui arrive en pièce jointe dans la boîte `ENVOI_EMAIL` (réglée dans `js/config.js`), via le service gratuit FormSubmit.

**Au tout premier envoi**, FormSubmit envoie à cette adresse un e-mail « Activate Form » : il faut cliquer sur le bouton d'activation, sinon les envois suivants ne sont pas transmis. Fais toi-même un premier envoi test juste après la mise en ligne.

## Photo de profil

Chaque élève peut ajouter une photo (onglet « Mon suivi » ou clic sur son avatar en haut). Elle est recadrée et compressée sur l'appareil (160 × 160 px), puis enregistrée avec son suivi : aucune configuration supplémentaire n'est nécessaire.

## Groupes, réponses et notation par les pairs

**Mise à jour d’une installation existante** : réexécute tout le fichier [`supabase/schema.sql`](supabase/schema.sql) dans *SQL Editor* (il est sans risque de le relancer : il ne supprime aucune donnée). Il crée les tables `groupes`, `groupe_membres`, `reponses`, `notes`, `commentaires`, le stockage privé `reponses` pour les photos, ainsi que toutes les règles de sécurité.

| Rôle | Droits |
|---|---|
| Responsable | renomme le groupe, voit et renouvelle le code d’invitation, attribue les rôles, exclut des membres, modère, supprime le groupe (il reste toujours au moins un responsable) |
| Modérateur | voit le code d’invitation, supprime réponses et messages, exclut des membres simples |
| Membre | soumet ses réponses sur l’honneur, note celles des autres de 0 à 10, commente |
| Professeur | voit et modère tous les groupes de la classe |

Règles garanties par la base (et non seulement par l’interface) :
- une réponse exige l’engagement sur l’honneur, une seule réponse par élève, exercice et groupe, et elle n’est pas modifiable ;
- seuls les membres du groupe voient les réponses, les notes, les photos et la discussion ;
- on ne peut pas noter sa propre réponse ; les notes sont des entiers de 0 à 10, modifiables ou retirables par leur auteur ;
- un commentaire ne peut être modifié que par son auteur, et supprimé par lui ou par un modérateur.

Dans le suivi, un exercice est marqué **réussi** quand la réponse a reçu au moins 2 notes et une moyenne d’au moins 12/20.

## Application installable (téléphone et ordinateur)

Le site est une **application web installable** (PWA) : `manifest.webmanifest`, icônes dans `icons/`, et `sw.js` qui garde en mémoire l’interface, les énoncés, les indices et les corrigés (consultables hors connexion ; les données des comptes ne sont jamais mises en cache).
- **Android / Chrome / Edge** : bouton « Installer » en haut du site, ou menu ⋮ → *Installer l’application*.
- **iPhone / iPad** : dans Safari, *Partager* → *Sur l’écran d’accueil*.
- Pour la publier sur le **Google Play Store** : https://www.pwabuilder.com → saisir l’adresse du site → *Package for stores* → *Android*, puis déposer le fichier `.aab` dans la Play Console. Pour l’App Store, PWABuilder fournit aussi un projet iOS, à compiler avec Xcode sur un Mac.

Après une modification du site, incrémente `VERSION` dans `sw.js` pour forcer le renouvellement du cache hors connexion.

## Ajouter des exercices en lot

Les exercices ajoutés en lot sont écrits dans `tools/new_*.py` (énoncé, 3 indices, corrigé). Pour régénérer les fichiers de données : `python3 tools/build_new.py`, puis `python3 tools/build_bilan.py` (qui découpe aussi les corrigés en un fichier par exercice dans `data/corr/`, le seul format lu par le site).

## Structure pédagogique de chaque exercice

- **Énoncé** (encadré bleu), **Ma réponse** : engagement sur l’honneur puis envoi au groupe (texte et/ou photos).
- **Indices** (encadré orange, fermés par défaut) : Indice 1 = piste globale, Indice 2 = méthode précise.
- **Correction détaillée** (encadré vert, accordéon) : déverrouillée après l’envoi de sa réponse ou les deux indices ; elle se termine par le **Bilan** (encadré violet) : 📜 théorèmes & définitions utilisés, 💡 astuces & réflexes à retenir.

Les bilans sont rédigés dans `tools/bilan_*.py` (énoncés de référence communs dans `tools/bilan_lib.py`). Pour les exercices ajoutés par le professeur depuis le site, l'IA produit le même format (corrigé, résultat, théorèmes, astuces).

Les formules sont rendues par MathJax 4 (police New Computer Modern, identique à LaTeX), avec retour à la ligne automatique des formules trop longues sur téléphone.

## Correction en trois modes

Sous chaque exercice, la section « Correction » propose trois lectures :

- **Guidée** : la correction se dévoile une étape à la fois. Avant chaque étape, une question invite l'élève à la chercher (« Quelle méthode envisages-tu ? »). Les boutons « Voir l'étape suivante » et « Afficher un indice » font avancer, « Voir toute la correction » passe au mode détaillé.
- **Détaillée** : la correction en 6 étapes, avec les outils « Pourquoi cette méthode ? » (extrait de l'étape Stratégie, ou explication générée), « Autre méthode », « Expliquer davantage » sur chaque étape, replier/déplier, copier, PDF, partager, « Signaler une erreur ».
- **Rigoureuse** : une rédaction de type copie de concours, générée par l'IA à partir de la correction de la plateforme, contrôlée par une relecture indépendante, puis mise en cache et partagée.

Le bouton « Vérifier ma réponse » analyse le résultat ou la démarche de l'élève : il trouve la première erreur (calcul, méthode, raisonnement, rédaction) et propose une piste, sans donner la solution.

Tant que l'élève n'a ni soumis sa réponse ni consulté les indices, les modes détaillé et rigoureux affichent d'abord une invitation à chercher, avec un bouton « Voir quand même ».

Le sélecteur « Programme » (MPSI, MP, PC, PSI…) est transmis à l'IA pour qu'elle reste dans le programme de la filière.

**Côté Supabase, deux actions sont nécessaires :**

1. Relancer `supabase/schema.sql` dans l'éditeur SQL. Il crée la table `corrections_ia` (le cache des contenus générés, accessible uniquement par la fonction) et autorise les signalements d'erreurs dans les corrections.
2. Redéployer la fonction `corriger` (Edge Functions → `corriger` → coller le nouveau `index.ts` → Deploy). Elle gère les nouveaux modes `rigoureux`, `autre`, `expliquer`, `pourquoi` et `analyse`.

Les contenus partagés sont mis en cache par une empreinte SHA-256 de toutes leurs entrées : une deuxième demande identique ne coûte rien et ne compte pas dans la limite quotidienne. Une réponse coupée par la limite de longueur est refusée au lieu d'être affichée tronquée. Un contenu que la relecture juge faux n'est pas mis en cache. Les signalements d'erreurs arrivent dans la file de modération du tableau de bord.

### Interrupteur de l'IA

Toutes les fonctions qui ont besoin de la clé Anthropic sont masquées tant que `IA: false` dans `js/config.js` :
- indices et corrigés générés ;
- « Expliquer davantage », « Autre méthode » et « Vérifier ma réponse » ;
- choix du programme ;
- import d'énoncé par photo.

Une fois le secret `ANTHROPIC_API_KEY` enregistré dans Supabase, passe `IA: true` pour les réactiver.

### Rédactions rigoureuses écrites à la main

Le mode Rigoureux affiche d'abord la rédaction de concours écrite par l'équipe. Elle se trouve dans `tools/rig/r*.py`, sous la forme d'un dictionnaire `R = {id: texte}`, et `python3 tools/build_detail.py` la copie dans le champ `rigoureux` de `data/corriges.json`.

À défaut, il affiche une « version courte » : les étapes Résolution et Conclusion de la correction en 6 étapes. Si l'exercice n'a ni l'une ni l'autre, un message invite à lire le mode Détaillé.

## Identité visuelle

Le site suit une direction « carnet de colle » : papier chaud, encre, vert académique `#235347`, terracotta `#D97952`, et la ligne de marge comme signature. Les polices sont auto-hébergées dans `fonts/` (licence OFL) : Fraunces pour les titres, Source Sans 3 pour le texte, JetBrains Mono pour les repères, Caveat pour les annotations. Les couleurs et les polices sont réglées par les variables en tête de `css/style.css`. Le mode sombre (graphite, ivoire, sauge, cuivre) suit automatiquement le système ou le bouton lune/soleil. Toutes les paires texte/fond passent le niveau AA du WCAG.

## Schémas de physique
- Charte graphique « annale » : `annale/CHARTE.md` ; toutes les épaisseurs, polices et marqueurs sont dans `annale/kit.js`.
- Les schémas sont décrits dans `annale/lot1.js` à `annale/lot6.js` (énoncé et correction, avec leur légende).
- `node annale/export.mjs` régénère les fichiers `annale/svg/<id>-enonce.svg` et `<id>-correction.svg`, la planche de relecture `annale/planche.html` et l'index `js/figures-annale-index.js`.
- Le site charge chaque SVG à la demande (`js/figures-annale.js`) et l'insère dans la page : les traits prennent la couleur du texte, en clair comme en sombre. La police Latin Modern est servie depuis `fonts/`.
- Le schéma de correction s'affiche en tête de la correction (Détaillée, Rigoureuse, Guidée après la première étape, fiche PDF), jamais avec l'énoncé seul.
- Les schémas d'énoncé plus anciens restent dans `js/figures.js` pour les exercices qui n'ont pas de version annale.

## Vitesse

- Les corrigés sont chargés un par un (`data/corr/<id>.json`), à l'ouverture de l'exercice ; `data/corriges.json` sert seulement aux outils et n'est pas publié.
- MathJax se télécharge après l'affichage de la page (ou dès l'ouverture d'un exercice).
- Le service worker sert l'application depuis le cache : **à chaque mise en ligne, incrémenter `VERSION` dans `sw.js`**. Les visiteurs reçoivent la nouvelle version automatiquement (rechargement discret, jamais pendant la saisie d'un texte).
- `_headers` règle la durée de cache côté Cloudflare (polices et images 30 jours, données 1 heure).

## Refonte 2026-11 (branche `refonte`)

- **Jetons de design** centralisés en tête de `css/style.css` (espacements `--s1…--s8`, rayons, tailles de texte, élévations `--e1…--e3`, couleurs de matières et de niveaux, durées d'animation).
- **Accueil** (`js/vitrine.js`) : « Le labo » (Taylor, oscillateur amorti, dichotomie, calculés en direct), « La bibliothèque » (chiffres calculés sur `data/exercices.json`, carrousel d'exercices réels avec commandes manuelles).
- **Bibliothèque** : recherche sans accents et multi-mots, accueil « Reprendre / Pour toi / Consultés récemment / Nouveautés », bouton « Marquer comme fait » (suivi personnel, distinct de « terminé » et « réussi »), navigation précédent / suivant (et touches ← →).
- **Progression** (`js/xp.js`) : XP et niveaux (Bizuth → Major) calculés sur les statistiques publiques du profil, jalons, rythme par semaine et par mois. Aucune modification de la base.
- Champ facultatif `ajout` (date) dans `data/exercices.json` pour la rubrique « Nouveautés ».
- **Étape 2** : affichage des exercices en grille (ordinateur), défis du jour et de la semaine (`js/defis.js`, validés seulement par des exercices cochés « fait » ou des réponses soumises), bannière de profil personnalisable (4 motifs × 4 couleurs ; migration `supabase/banniere.sql`, sans risque, à lancer une fois).
- **Informatique** : 26 exercices originaux (chapitres du cours d'informatique MP de D. Rupprecht : Python, complexité et preuves, piles et récursivité, tris, graphes, programmation dynamique, apprentissage, jeux, flottants), dans `tools/new_info_1.py` et `tools/new_info_2.py`. Tout le code est exécuté et vérifié par `python3 tools/test_info.py` (à relancer après toute modification). Blocs ```` ```python ```` et `code en ligne` pris en charge par `js/format.js`. Migration `supabase/informatique.sql` (matière autorisée pour les exercices du professeur + liste des exercices pour les statistiques).
- **Physique (2026-11-25)** : 18 exercices d'après des planches d'oral CCINP, une préparation aux oraux (type CCS / CCMP / X) et les attentes du rapport Centrale-Supélec 2025 (`tools/new_phys_src1.py`, `tools/new_phys_src2.py`, bilans `tools/bilan_pc.py`).
