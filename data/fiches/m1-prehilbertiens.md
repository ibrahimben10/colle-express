---
titre: Espaces préhilbertiens réels
---
## L'essentiel

Un produit scalaire permet de parler de longueurs, d'angles et d'orthogonalité dans un espace vectoriel. Les bases orthonormées simplifient les calculs ; la projection orthogonale donne le meilleur approximant (la distance à un sous-espace).

## Produit scalaire

> **Définition.** Un produit scalaire sur un $\mathbb R$-espace $E$ est une forme bilinéaire, symétrique, **définie positive** : $\langle x, x\rangle \ge 0$, avec égalité seulement si $x = 0$. Norme associée : $\|x\| = \sqrt{\langle x, x\rangle}$.

Exemples : produit canonique de $\mathbb R^n$ ($\sum x_iy_i = {}^tXY$) ; $\langle f, g\rangle = \int_a^bfg$ sur $\mathcal C([a, b], \mathbb R)$ ; $\langle A, B\rangle = \operatorname{tr}({}^tAB)$ sur $M_n(\mathbb R)$.

- Identités : $\|x + y\|^2 = \|x\|^2 + 2\langle x, y\rangle + \|y\|^2$ ; **polarisation** $\langle x, y\rangle = \frac14(\|x + y\|^2 - \|x - y\|^2)$ ; parallélogramme $\|x + y\|^2 + \|x - y\|^2 = 2\|x\|^2 + 2\|y\|^2$.

> **Théorème — Inégalité de Cauchy-Schwarz.** $|\langle x, y\rangle| \le \|x\|\|y\|$, avec égalité si et seulement si $x$ et $y$ sont colinéaires.

Conséquence : inégalité triangulaire $\|x + y\| \le \|x\| + \|y\|$. Exemple : $\left(\int fg\right)^2 \le \int f^2\int g^2$.

## Orthogonalité

- $x \perp y$ si $\langle x, y\rangle = 0$. **Pythagore** : $x \perp y \Leftrightarrow \|x + y\|^2 = \|x\|^2 + \|y\|^2$.
- Orthogonal d'une partie : $A^\perp = \{x,\ \forall a \in A,\ \langle x, a\rangle = 0\}$, sous-espace vectoriel.
- Une famille orthogonale de vecteurs non nuls est libre.

## Bases orthonormées

> **Théorème — Gram-Schmidt.** À partir d'une famille libre $(e_1, \dots, e_p)$, on construit une famille orthonormée $(\varepsilon_1, \dots, \varepsilon_p)$ telle que $\operatorname{Vect}(\varepsilon_1, \dots, \varepsilon_k) = \operatorname{Vect}(e_1, \dots, e_k)$ pour tout $k$ : $\varepsilon_k$ est le normalisé de $e_k - \sum_{i<k}\langle e_k, \varepsilon_i\rangle\varepsilon_i$.

Tout espace euclidien (de dimension finie) a une base orthonormée. Dans une base orthonormée $(\varepsilon_i)$ :
$x = \sum\langle x, \varepsilon_i\rangle\varepsilon_i$, $\langle x, y\rangle = \sum x_iy_i$, $\|x\|^2 = \sum x_i^2$.

## Projection orthogonale

> **Théorème.** Si $F$ est de dimension finie, $E = F \oplus F^\perp$ ; et $(F^\perp)^\perp = F$ en dimension finie. En dimension $n$, $\dim F^\perp = n - \dim F$.

[[fig:m1-prehilbertiens-1]]

> **Propriété — Calcul et distance.** Si $(\varepsilon_1, \dots, \varepsilon_p)$ est une base orthonormée de $F$, le projeté orthogonal de $x$ est $p_F(x) = \sum_{i=1}^p\langle x, \varepsilon_i\rangle\varepsilon_i$. C'est l'unique $y \in F$ tel que $x - y \perp F$, et c'est le point de $F$ le plus proche de $x$ : $d(x, F) = \|x - p_F(x)\|$, avec $\|x\|^2 = \|p_F(x)\|^2 + d(x, F)^2$.

**Inégalité de Bessel** : $\sum\langle x, \varepsilon_i\rangle^2 \le \|x\|^2$.

- Distance à un hyperplan $H = n^\perp$ : $d(x, H) = \frac{|\langle x, n\rangle|}{\|n\|}$.
- Méthode sans base orthonormée : écrire $p_F(x) = \sum\lambda_ie_i$ et imposer $\langle x - p_F(x), e_j\rangle = 0$ pour tout $j$ (système linéaire).

## Exemple corrigé

**Énoncé.** Calculer $\min_{a,b\in\mathbb R}\int_0^1(x^2 - ax - b)^2\,\mathrm dx$.

**Solution.** C'est $d(x^2, F)^2$ avec $F = \mathbb R_1[X]$ pour $\langle f, g\rangle = \int_0^1fg$. Le projeté $p = aX + b$ vérifie $\langle X^2 - p, 1\rangle = 0$ et $\langle X^2 - p, X\rangle = 0$ : $\frac13 - \frac a2 - b = 0$ et $\frac14 - \frac a3 - \frac b2 = 0$, d'où $a = 1$, $b = -\frac16$. Le minimum vaut $\|X^2\|^2 - \langle X^2, p\rangle$ (Pythagore, car $X^2 - p \perp p$) $= \frac15 - \left(\frac14 - \frac1{18}\right) = \frac{1}{180}$.

## Pièges classiques

- Une famille orthogonale contenant 0 n'est pas libre.
- La formule $p_F(x) = \sum\langle x, \varepsilon_i\rangle\varepsilon_i$ exige une base **orthonormée**.
- En dimension infinie, on peut avoir $F \oplus F^\perp \ne E$.
