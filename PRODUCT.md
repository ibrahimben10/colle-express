# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Élèves de classes préparatoires scientifiques (MPSI puis MP) qui préparent les colles (interrogations orales hebdomadaires) et les oraux de concours (CCINP, Mines-Centrale, X-ENS). Ils travaillent autant au téléphone (le soir, dans les transports, entre deux cours) qu'à l'ordinateur (séances de travail avec feuille et stylo). Audience secondaire : enseignants (rôle « prof ») qui suivent des groupes d'élèves.

## Product Purpose

Faire travailler comme en colle : des exercices courts et ciblés de type oral, des indices progressifs plutôt que la solution toute faite, un corrigé détaillé une fois qu'on a vraiment cherché. Le succès : l'élève cherche par lui-même et progresse ; la solution n'arrive qu'après l'effort.

## Positioning

Une méthode d'oral, pas une banque de corrigés : indices gradués (piste globale, méthode précise), correction guidée étape par étape, fiches de cours détaillées accessibles pendant l'exercice, colleur virtuel qui interroge et note, groupes et suivi pour les profs. Créé par un ancien élève de MPSI/MP.

## Operating Context

- Parcours principal : choisir une filière (CCINP, Mines-CS, X-ENS), une matière (Maths, Physique, Chimie, Info) et un chapitre ; ouvrir un exercice ; chercher sur papier ; demander des indices ; soumettre sa réponse ; lire la correction (guidée, détaillée, rigueur).
- Fiches de cours (125) avec schémas scientifiques et formules, ouvertes en pleine page ou en panneau pendant un exercice.
- Colleur virtuel (IA, version d'essai, 2 colles par jour).
- Groupes avec code, discussion, réponses du groupe, suivi par le prof ; profils publics, communauté, carnet, collections, XP et niveaux.

## Capabilities and Constraints

- Site statique en JavaScript natif (modules ES), sans framework ni étape de compilation ; CSS unique (`css/style.css`).
- Données et authentification Supabase ; fonction Edge `colleur` ; déploiement GitHub Pages et Cloudflare Workers ; service worker hors ligne.
- Formules rendues par MathJax ; schémas en SVG générés par code (modules `js/fiches-fig-*.js`, `js/figures*.js`) qui utilisent les variables de couleur du thème.
- Modes clair et sombre ; aucune dépendance supplémentaire souhaitée.

## Brand Commitments

- Le nom « Colle Express » est conservé. Le logo actuel (toque) et tout le reste de l'identité visuelle peuvent changer.
- Voix : tutoiement, direct, bienveillant, exigeant sur le travail personnel.

## Evidence on Hand

Exercices réels (`data/exercices.json`), annales, 125 fiches de cours (`data/fiches/`), page À propos du créateur. Aucun témoignage, chiffre d'audience ou classement à inventer : l'annuaire n'affiche pas de classement par choix.

## Product Principles

- Chercher avant de lire : l'interface retient la solution, elle ne la pousse pas.
- La formule et le schéma d'abord : rien ne doit gêner la lecture des mathématiques.
- Aussi bon au téléphone qu'à l'ordinateur.
- Aucun classement public ni pression sociale ; la progression est personnelle.

## Accessibility & Inclusion

Contraste AA minimum, navigation clavier, respect de `prefers-reduced-motion`, textes en français.
