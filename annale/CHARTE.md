# Charte graphique « annale » des schémas de physique

Toutes les valeurs ci-dessous sont centralisées dans `annale/kit.js` (objet `CH`). Un schéma ne fixe jamais lui-même une épaisseur, une police ou une couleur.

## Couleur
- Monochrome : tout est tracé en `currentColor` (noir sur papier, clair en mode sombre). Aucun aplat de couleur, aucun dégradé, aucune ombre.
- Les seules « matières » sont des hachures à 45° (pas de 5 px, trait de 0,55) : parois, sol, bâti, conducteurs massifs.
- Une aire significative (travail d'un cycle, par exemple) est marquée par des hachures lâches à −45°.

## Traits
| Usage | Épaisseur | Style |
|---|---|---|
| Objets, fils, solides, courbes | 1,3 | plein |
| Parois (avec hachures) | 1,7 | plein |
| Vecteurs (forces, champs, vitesses) | 1,3 | plein, tête pleine 8,5 × 6 |
| Axes et repères | 0,9 | plein, petite tête pleine |
| Constructions, cotes, lignes de rappel | 0,7 | plein |
| Normales, positions antérieures, asymptotes | 0,7 | pointillé 4-3 |
| Axe de symétrie ou de rotation | 0,7 | mixte 9-2,5-2-2,5 |

- Sens de parcours (fil, rayon, branche de cycle) : petite tête pleine posée au milieu du trait.
- Tensions et flux : flèche fine (0,7) parallèle au dipôle ou au trajet.
- Cotes : trait fin, flèche aux deux bouts.

## Typographie
- Police : Latin Modern Roman (rendu LaTeX), puis CMU Serif, STIX Two et Times en secours.
- Corps : 15 px pour les notations, 10,5 px pour les indices et les exposants, 12,5 px pour les graduations, 13,5 px pour les rares mots.
- Grandeurs en italique, avec un indice romain s'il s'agit d'une étiquette (`u_C`, `W_g`) et italique s'il s'agit d'une variable.
- Chiffres, unités et mots en romain. Les lettres grecques restent droites.
- Vecteurs : lettre italique surmontée d'une flèche fine.

## Contenu
- Le schéma porte des notations, pas des phrases. Les explications vont dans la légende HTML, sous la figure.
- Seule exception : un ou deux mots indispensables (« générateur », « effet Joule », « (a) capacité »).
- Quand plusieurs dessins se complètent (circuit et courbe, ou capacité et inductance), ils sont séparés par un trait pointillé vertical et repérés (a), (b).
- Énoncé : données géométriques et notations de l'énoncé seulement, jamais la méthode. Correction : le même dessin, complété par les éléments de la méthode.
- Courbes calculées à partir des formules exactes ; si les valeurs réelles rendent la figure illisible, on garde l'allure et on le dit dans la légende.

## Électrocinétique (norme française)
- Résistor : rectangle 34 × 12.
- Condensateur : deux armatures épaisses de 22 px, écartées de 7 px.
- Bobine : quatre boucles.
- Générateur de tension : cercle traversé par le fil.
- Interrupteur : deux bornes creuses et une lame.
- Le fil s'arrête aux bornes des dipôles (aucun fond blanc).
- Conventions : courant par une tête sur le fil ; tensions par une flèche fine. Convention récepteur, avec la flèche de tension opposée au courant ; convention générateur pour la source.

## Format
- SVG autonome, `viewBox` de 340 à 560 px de large, sans dépendance externe.
- Identifiants partagés `an-*` (marqueurs et hachures), identiques d'un fichier à l'autre.
- Nom des fichiers : `<id-exercice>-enonce.svg` ou `<id-exercice>-correction.svg`.
