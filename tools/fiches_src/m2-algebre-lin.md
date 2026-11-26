---
titre: Compléments d'algèbre linéaire
---
## L'essentiel

Sommes directes de plusieurs sous-espaces, matrices par blocs, sous-espaces stables, polynômes d'endomorphismes et lemme des noyaux : ce sont les outils qui préparent la réduction. S'y ajoutent dualité élémentaire, trace et matrices semblables.

## Produits et sommes de sous-espaces

- Produit d'espaces : $\dim(E_1\times\dots\times E_p) = \sum\dim E_i$.
- $F_1 + \dots + F_p$ est **directe** si toute décomposition $x = x_1 + \dots + x_p$ ($x_i \in F_i$) est unique, c'est-à-dire si $x_1 + \dots + x_p = 0 \Rightarrow$ tous les $x_i$ sont nuls.

> **Propriété.** En dimension finie, la somme est directe si et seulement si $\dim\sum F_i = \sum\dim F_i$. Une base adaptée (concaténation de bases des $F_i$) est une base de $E = \bigoplus F_i$.

Une application linéaire sur $\bigoplus F_i$ est déterminée par ses restrictions aux $F_i$.

## Matrices par blocs

Produit par blocs (tailles compatibles). Déterminant d'une matrice triangulaire par blocs : produit des déterminants des blocs diagonaux. Si $E = F_1 \oplus \dots \oplus F_p$ et chaque $F_i$ est stable par $u$, la matrice dans une base adaptée est diagonale par blocs.

## Sous-espaces stables

$F$ est stable par $u$ si $u(F) \subset F$ ; $u$ induit alors un endomorphisme $u_F$. Dans une base adaptée à $F$, la matrice est triangulaire supérieure par blocs.

> **Propriété.** Si $u$ et $v$ commutent, $\ker v$ et $\operatorname{Im}v$ sont stables par $u$ ; en particulier les $\ker P(u)$, $\operatorname{Im}P(u)$ et les sous-espaces propres de $v$.

Une droite $\operatorname{Vect}(x)$ est stable si et seulement si $x$ est un vecteur propre.

## Polynômes d'endomorphismes et de matrices

Pour $P = \sum a_kX^k$, $P(u) = \sum a_ku^k$ (avec $u^0 = \mathrm{id}$). $P \mapsto P(u)$ est un morphisme d'algèbres : $(PQ)(u) = P(u) \circ Q(u)$ ; donc $P(u)$ et $Q(u)$ commutent.

- $P$ est **annulateur** si $P(u) = 0$ ; ils forment un idéal de $\mathbb K[X]$. En dimension finie $n$, il existe un annulateur non nul (car $\dim\mathcal L(E) = n^2$).
- **Polynôme minimal** $\pi_u$ : générateur unitaire de cet idéal. $\mathbb K[u] = \{P(u)\}$ est une algèbre de dimension $\deg\pi_u$.
- Si $P(u) = 0$ et $u(x) = \lambda x$, alors $P(\lambda) = 0$ : les valeurs propres sont racines de tout annulateur.
- Calcul : si $P$ annule $u$ et $X^k = PQ + R$ (division euclidienne), alors $u^k = R(u)$. Inversibilité : si $P(0) \ne 0$, on en déduit $u^{-1}$ comme polynôme en $u$.

> **Théorème — Lemme des noyaux.** Si $P_1, \dots, P_k$ sont deux à deux premiers entre eux et $P = P_1\cdots P_k$ : $\ker P(u) = \bigoplus_{i=1}^k\ker P_i(u)$. Si de plus $P(u) = 0$, alors $E = \bigoplus\ker P_i(u)$.

## Trace, matrices semblables

- $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ ; deux matrices semblables ont même trace, même rang, même déterminant, même polynôme caractéristique ; ce sont des **invariants de similitude**.
- La trace d'un projecteur est égale à son rang.

## Formes linéaires et hyperplans

Une forme linéaire non nulle a pour noyau un hyperplan ; deux formes ont le même noyau si et seulement si elles sont proportionnelles. En dimension finie, un hyperplan a une équation $a_1x_1 + \dots + a_nx_n = 0$.

## Exemple corrigé

**Énoncé.** Soit $p$ tel que $p^2 = p$. Retrouver $E = \ker p \oplus \ker(p - \mathrm{id})$.

**Solution.** $X^2 - X = X(X - 1)$ annule $p$, avec $X$ et $X - 1$ premiers entre eux. Lemme des noyaux : $E = \ker p \oplus \ker(p - \mathrm{id})$, et $\ker(p - \mathrm{id}) = \operatorname{Im}p$.

## Exemple corrigé (inverse par annulateur)

**Énoncé.** $A^2 - 5A + 6I = 0$. Montrer que $A$ est inversible et donner $A^{-1}$.

**Solution.** $A(5I - A) = 6I$, donc $A\cdot\frac{5I - A}{6} = I$ : $A$ est inversible et $A^{-1} = \frac{5I - A}{6}$.

## Pièges classiques

- Pour trois sous-espaces ou plus, les intersections deux à deux nulles ne suffisent pas pour une somme directe.
- $u$ et $v$ quelconques ne commutent pas : $\ker v$ n'est pas stable par $u$ en général.
- Une valeur propre est racine de tout annulateur, mais une racine d'un annulateur n'est pas forcément valeur propre.
