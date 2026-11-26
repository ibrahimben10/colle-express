---
titre: Équations différentielles linéaires
---
## L'essentiel

Systèmes $X' = A(t)X + B(t)$ et équations scalaires d'ordre 2 à coefficients non constants : le théorème de Cauchy-Lipschitz linéaire garantit l'existence et l'unicité, et l'ensemble des solutions a une structure d'espace affine de dimension $n$.

> **Théorème de Cauchy-Lipschitz linéaire.** Si $A$ et $B$ sont continues sur un intervalle $I$, pour tout $t_0 \in I$ et $X_0$, il existe une unique solution sur $I$ telle que $X(t_0) = X_0$. Les solutions de l'équation homogène forment un espace vectoriel de dimension $n$.

## Systèmes à coefficients constants

$X' = AX$ : les solutions sont $X(t) = e^{tA}X_0$, avec $e^{tA} = \sum\frac{t^kA^k}{k!}$. Si $A = PDP^{-1}$ est diagonalisable, on pose $X = PY$ : $Y' = DY$ se résout composante par composante.

## Ordre 2 : $y'' + a(t)y' + b(t)y = c(t)$

- Les solutions de l'équation homogène forment un plan vectoriel ; deux solutions $y_1$, $y_2$ en forment une base si leur **wronskien** $W = y_1y_2' - y_1'y_2$ ne s'annule pas.
- Si l'on connaît une solution $y_1$ qui ne s'annule pas, on cherche $y = y_1z$ : l'équation en $z'$ est d'ordre 1.
- **Variation des constantes** : $y = \lambda(t)y_1 + \mu(t)y_2$ avec $\lambda'y_1 + \mu'y_2 = 0$ et $\lambda'y_1' + \mu'y_2' = c$.
- Recherche de solutions **développables en série entière**.

## Exemple corrigé

**Énoncé.** Résoudre $X' = AX$ avec $A = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$.

**Solution.** $A$ est diagonalisable : valeurs propres 1 et $-1$, vecteurs propres $\binom11$ et $\binom1{-1}$. Les solutions sont $X(t) = \alpha e^t\binom11 + \beta e^{-t}\binom1{-1}$, $\alpha, \beta \in \mathbb R$.

## Pièges classiques

- Cauchy-Lipschitz exige la forme **résolue** (coefficient de $y''$ égal à 1) sur un intervalle où les coefficients sont continus.
- $e^{A+B} = e^Ae^B$ seulement si $A$ et $B$ commutent.
