---
titre: Équations différentielles linéaires
---
## L'essentiel

Systèmes $X' = A(t)X + B(t)$ et équations scalaires d'ordre $n$ : le théorème de Cauchy-Lipschitz linéaire garantit l'existence et l'unicité d'une solution pour toute condition initiale, et l'ensemble des solutions est un espace affine de dimension $n$. À coefficients constants, on résout par réduction de la matrice ou par l'exponentielle de matrice.

## Cadre et théorème fondamental

Équation $X' = A(t)X + B(t)$, avec $A : I \to M_n(\mathbb K)$ et $B : I \to \mathbb K^n$ continues sur un intervalle $I$. Une équation scalaire $y^{(n)} + a_{n-1}(t)y^{(n-1)} + \dots + a_0(t)y = b(t)$ s'y ramène avec $X = (y, y', \dots, y^{(n-1)})$.

> **Théorème de Cauchy-Lipschitz linéaire.** Pour tout $t_0 \in I$ et $X_0 \in \mathbb K^n$, il existe une unique solution sur $I$ telle que $X(t_0) = X_0$.

> **Théorème — Structure.** L'ensemble $S_H$ des solutions de l'équation homogène est un espace vectoriel de dimension $n$ (l'application $X \mapsto X(t_0)$ est un isomorphisme de $S_H$ sur $\mathbb K^n$). Les solutions de l'équation complète sont $X_p + S_H$.

Conséquence : une solution qui s'annule en un point (avec toutes ses dérivées utiles) est nulle ; deux solutions sont égales si elles ont la même condition initiale.

## Coefficients constants : $X' = AX + B(t)$

### Exponentielle de matrice

$e^{A} = \sum_{k\ge0}\frac{A^k}{k!}$ (série absolument convergente). Propriétés :
- si $AB = BA$, $e^{A+B} = e^Ae^B$ ; $e^A$ est inversible d'inverse $e^{-A}$ ;
- $\frac{\mathrm d}{\mathrm dt}e^{tA} = Ae^{tA} = e^{tA}A$ ;
- $e^{PDP^{-1}} = Pe^DP^{-1}$, et $e^{\operatorname{diag}(\lambda_i)} = \operatorname{diag}(e^{\lambda_i})$ ; $\det(e^A) = e^{\operatorname{tr}A}$.

> **Théorème.** Les solutions de $X' = AX$ sont les $X(t) = e^{(t-t_0)A}X_0$.

### Méthodes pratiques

- **$A$ diagonalisable** : $A = PDP^{-1}$, on pose $X = PY$ : $Y' = DY + P^{-1}B$, système découplé. Les solutions homogènes sont $\sum c_ie^{\lambda_it}V_i$ ($V_i$ vecteurs propres).
- **$A$ trigonalisable** : $A = PTP^{-1}$, système triangulaire, résolu en remontant.
- Calcul de $e^{tA}$ : par diagonalisation, ou par $A = \lambda I + N$ avec $N$ nilpotente ($e^{tA} = e^{\lambda t}\sum_k\frac{t^kN^k}{k!}$, somme finie).
- **Variation des constantes** : $X = e^{tA}C(t)$ avec $C' = e^{-tA}B(t)$.

## Équations scalaires d'ordre 2

$y'' + a(t)y' + b(t)y = c(t)$, $a$, $b$, $c$ continues sur $I$.

- $S_H$ est un plan vectoriel. Deux solutions $y_1$, $y_2$ en forment une base si et seulement si le **wronskien** $W = y_1y_2' - y_1'y_2$ ne s'annule pas (il s'annule partout ou nulle part) ; $W' = -aW$.
- **Une solution connue** $y_1$ ne s'annulant pas : poser $y = y_1z$ ; l'équation devient une équation du premier ordre en $z'$.
- **Variation des constantes** : $y = \lambda(t)y_1 + \mu(t)y_2$ avec $\lambda'y_1 + \mu'y_2 = 0$ et $\lambda'y_1' + \mu'y_2' = c$ (système de Cramer de déterminant $W$).
- **Solutions développables en série entière** : injecter $\sum a_nt^n$, obtenir une récurrence sur les coefficients, calculer le rayon.
- Coefficients constants : équation caractéristique (voir la fiche de première année).

## Recollement

Pour $\alpha(t)y' + \beta(t)y = \gamma(t)$ quand $\alpha$ s'annule en $t_0$ : résoudre sur chaque intervalle où $\alpha \ne 0$, puis chercher les solutions sur $I$ entier par **raccordement** (continuité et dérivabilité en $t_0$). L'ensemble des solutions n'est plus forcément de dimension 1.

## Exemple corrigé

**Énoncé.** Résoudre $X' = AX$ avec $A = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$.

**Solution.** Valeurs propres 1 et $-1$, vecteurs propres $\binom11$ et $\binom1{-1}$ : $A$ est diagonalisable. Les solutions sont $X(t) = \alpha e^t\binom11 + \beta e^{-t}\binom1{-1}$, $\alpha, \beta \in \mathbb R$. On a aussi $e^{tA} = \begin{pmatrix}\operatorname{ch}t & \operatorname{sh}t\\ \operatorname{sh}t & \operatorname{ch}t\end{pmatrix}$.

## Exemple corrigé (une solution connue)

**Énoncé.** Résoudre $t^2y'' - 2y = 0$ sur $]0, +\infty[$ sachant que $y_1 = t^2$ est solution.

**Solution.** On pose $y = t^2z$ : $y'' = 2z + 4tz' + t^2z''$, d'où $t^4z'' + 4t^3z' = 0$, soit $z'' = -\frac4tz'$, $z' = \frac{c}{t^4}$, $z = -\frac{c}{3t^3} + d$. Solutions : $y = \frac{\alpha}{t} + \beta t^2$.

## Pièges classiques

- Cauchy-Lipschitz exige la forme **résolue** (coefficient dominant égal à 1) et des coefficients continus sur un **intervalle**.
- $e^{A+B} = e^Ae^B$ seulement si $A$ et $B$ commutent.
- Pour une équation d'ordre 2, la condition initiale porte sur $y(t_0)$ **et** $y'(t_0)$.
