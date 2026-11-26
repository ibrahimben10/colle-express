---
titre: Déterminants
---
## L'essentiel

Le déterminant est un nombre attaché à une matrice carrée (ou à une famille de $n$ vecteurs, ou à un endomorphisme) qui est non nul si et seulement si la matrice est inversible. Il se calcule par opérations sur les lignes et colonnes ou par développement.

## Groupe symétrique

$S_n$ : permutations de $\{1, \dots, n\}$. Toute permutation se décompose en produit de cycles à supports disjoints, et en produit de transpositions. La **signature** $\varepsilon$ est l'unique morphisme $S_n \to \{-1, 1\}$ valant $-1$ sur les transpositions ; un $p$-cycle a pour signature $(-1)^{p-1}$.

## Formes multilinéaires alternées

> **Théorème — Définition du déterminant.** Dans un espace de dimension $n$ muni d'une base $\mathcal B$, il existe une unique forme $n$-linéaire alternée $\det_{\mathcal B}$ valant 1 sur $\mathcal B$. Pour une matrice : $\det A = \sum_{\sigma\in S_n}\varepsilon(\sigma)a_{\sigma(1)1}\cdots a_{\sigma(n)n}$.

- Alternée : si deux vecteurs sont égaux, le déterminant est nul ; échanger deux vecteurs change le signe.
- Une famille de $n$ vecteurs est une base si et seulement si son déterminant est non nul.

## Propriétés

> **Propriété.**
> - $\det(AB) = \det A\det B$ ; $A$ est inversible si et seulement si $\det A \ne 0$, et alors $\det(A^{-1}) = \frac{1}{\det A}$.
> - $\det({}^tA) = \det A$ : tout ce qui vaut pour les colonnes vaut pour les lignes.
> - $\det(\lambda A) = \lambda^n\det A$.
> - Deux matrices semblables ont le même déterminant ; on définit ainsi $\det u$ pour un endomorphisme, avec $\det(v \circ u) = \det v\det u$.

## Calcul

- **Opérations** : ajouter à une colonne une combinaison des autres ne change rien ; échanger deux colonnes multiplie par $-1$ ; multiplier une colonne par $\lambda$ multiplie par $\lambda$.
- **Triangulaire** : produit des coefficients diagonaux. Triangulaire par blocs : produit des déterminants des blocs diagonaux.
- $2\times2$ : $ad - bc$ ; $3\times3$ : règle de Sarrus.

> **Théorème — Développement selon une ligne ou une colonne.** $\det A = \sum_{i=1}^n(-1)^{i+j}a_{ij}\Delta_{ij}$ (colonne $j$), où $\Delta_{ij}$ est le mineur obtenu en supprimant la ligne $i$ et la colonne $j$.

Comatrice : $A\,{}^t\operatorname{Com}(A) = {}^t\operatorname{Com}(A)A = \det(A)I_n$, d'où $A^{-1} = \frac{1}{\det A}{}^t\operatorname{Com}(A)$.

> **Propriété — Déterminant de Vandermonde.** $\det\left(x_i^{j-1}\right)_{1\le i,j\le n} = \prod_{1\le i<j\le n}(x_j - x_i)$ : non nul si et seulement si les $x_i$ sont distincts.

## Interprétation géométrique

[[fig:m1-determinants-1]]

En dimension 2, $|\det(u, v)|$ est l'aire du parallélogramme construit sur $u$ et $v$ ; en dimension 3, $|\det(u, v, w)|$ est le volume du parallélépipède. Le signe donne l'orientation.

## Exemple corrigé

**Énoncé.** Calculer $D = \begin{vmatrix}a & b & b\\ b & a & b\\ b & b & a\end{vmatrix}$.

**Solution.** On ajoute les colonnes 2 et 3 à la première : chaque ligne commence par $a + 2b$. On factorise : $D = (a + 2b)\begin{vmatrix}1 & b & b\\ 1 & a & b\\ 1 & b & a\end{vmatrix}$. On retranche la ligne 1 aux autres : $D = (a + 2b)\begin{vmatrix}1 & b & b\\ 0 & a - b & 0\\ 0 & 0 & a - b\end{vmatrix} = (a + 2b)(a - b)^2$.

## Exemple corrigé (récurrence)

**Énoncé.** $D_n$ est le déterminant tridiagonal $n\times n$ avec 2 sur la diagonale et $-1$ juste au-dessus et au-dessous. Calculer $D_n$.

**Solution.** En développant selon la première ligne : $D_n = 2D_{n-1} - D_{n-2}$, avec $D_1 = 2$, $D_2 = 3$. Équation caractéristique $(r - 1)^2 = 0$ : $D_n = \alpha + \beta n$, d'où $D_n = n + 1$.

## Pièges classiques

- $\det(A + B) \ne \det A + \det B$.
- $\det(\lambda A) = \lambda^n\det A$, pas $\lambda\det A$.
- Le déterminant n'est défini que pour les matrices **carrées**.
