---
titre: Déterminants
---
## L'essentiel

Le déterminant est l'unique forme $n$-linéaire alternée qui vaut 1 sur la base canonique. Il caractérise l'inversibilité et mesure un volume orienté.

## Groupe symétrique

Une permutation de $\{1, \dots, n\}$ se décompose en produit de **cycles** à supports disjoints, et en produit de transpositions. Sa **signature** $\varepsilon(\sigma) = \pm1$ est un morphisme : $\varepsilon(\sigma\sigma') = \varepsilon(\sigma)\varepsilon(\sigma')$ ; un $k$-cycle a pour signature $(-1)^{k-1}$.

## Propriétés du déterminant

[[fig:m1-determinants-1]]

- $\det(AB) = \det A\det B$, $\det({}^tA) = \det A$, $\det(\lambda A) = \lambda^n\det A$.
- $A$ inversible $\Leftrightarrow \det A \ne 0$, et $\det(A^{-1}) = \frac{1}{\det A}$.
- Opérations sur les lignes ou colonnes : échanger deux colonnes change le signe ; ajouter à une colonne une combinaison des autres ne change rien.
- Matrice triangulaire : produit des coefficients diagonaux.

> **Formule — Développement selon une colonne.** $\det A = \sum_{i=1}^n(-1)^{i+j}a_{ij}\Delta_{ij}$, où $\Delta_{ij}$ est le mineur obtenu en supprimant la ligne $i$ et la colonne $j$.

## Déterminant de Vandermonde

$\det\big(x_i^{j-1}\big)_{1\le i,j\le n} = \prod_{1\le i<j\le n}(x_j - x_i)$ : non nul si et seulement si les $x_i$ sont distincts.

## Exemple corrigé

**Énoncé.** Calculer $D_n$, déterminant $n\times n$ avec des 2 sur la diagonale et des $-1$ juste au-dessus et au-dessous.

**Solution.** En développant selon la première colonne : $D_n = 2D_{n-1} - D_{n-2}$, avec $D_1 = 2$, $D_2 = 3$. La suite est arithmétique ($D_n - D_{n-1}$ constant égal à 1) : $D_n = n + 1$.

## Pièges classiques

- $\det(A + B) \ne \det A + \det B$.
- $\det(\lambda A) = \lambda^n\det A$, pas $\lambda\det A$.
- Le déterminant n'a de sens que pour une matrice carrée.
