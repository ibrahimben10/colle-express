# Design — Colle Express « Copie double »

## Idée

L'élève cherche sur sa copie à grands carreaux, au stylo bleu ; le correcteur répond en rouge, dans la marge.

## Couleurs (jetons dans `css/style.css`, couche « COPIE DOUBLE v4 »)

| Rôle | Clair | Sombre |
|---|---|---|
| Bureau (fond) `--desk` | #EEF1F7 | #0B1022 |
| Feuille `--card` | #FFFFFF | #141A2E |
| Encre `--ink` | #1B2030 | #E9ECF5 |
| Encre douce `--soft` | #555C70 | #A6AEC6 |
| Couverture (barres) `--couv` | #1C2B78 | #0E1530 |
| Stylo bleu (actions, liens) `--bic` | #2340C2 | #8FA6FF |
| Stylo rouge (indices, correction, erreurs) `--rouge` | #CF2433 | #FF6F78 |
| Marge `--marge` | #EFA3AE | #7A3442 |
| Quadrillage `--seyes` / `--seyes-fort` | #E3EAF6 / #CFDBF0 | #19223B / #222D4D |
| Intercalaires maths / physique / chimie / info | #5B3FC0 / #B0500A / #0B7C80 / #2B7A35 | #B3A1FF / #FFA25C / #5ED3D6 / #6BD77A |

Contraste vérifié ≥ 4,5:1 pour tous les textes.

## Typographie

- Titres (h1, h2, titres de fiche) : Latin Modern Roman 400, auto-hébergée, accordée aux formules MathJax.
- Interface et texte : police système (SF Pro, sinon Inter auto-hébergée).
- Annotations au stylo rouge : Caveat, rare.

## Composants

- Barres haute et basse : couleur de couverture, onglet actif souligné d'un trait rouge tracé à la main (révélé par `clip-path`).
- Mot-symbole : « Colle *Express* » en Latin Modern, souligné au stylo rouge.
- Copie d'exercice : quadrillage Seyès (10 px / 40 px) et marge rouge, coins de feuille ; supprimé en `prefers-contrast: more`.
- Matières : intercalaires (onglet coloré en haut du bouton).
- Fiches : cartes-feuilles avec un filet de marge.
- Boutons : rectangles (rayon 8 px), pression à `scale(.97)`.
- Métadonnées sous le titre, jamais de surtitre au-dessus.

## Mouvement

Fondus et légères montées de 6 px en 220 ms `cubic-bezier(.23,1,.32,1)` ; tiroir de fiche en 300 ms `cubic-bezier(.32,.72,0,1)` ; aucun rebond ni ondulation. `prefers-reduced-motion` : opacité seule.
