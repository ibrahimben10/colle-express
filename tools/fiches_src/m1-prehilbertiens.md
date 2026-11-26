---
titre: Espaces préhilbertiens réels
---
## L'essentiel

Un produit scalaire permet de parler de longueur, d'angle et d'orthogonalité. Les bases orthonormées simplifient les calculs, et la projection orthogonale donne la meilleure approximation dans un sous-espace.

## Produit scalaire

> **Définition.** Un produit scalaire sur un $\mathbb R$-espace vectoriel est une forme bilinéaire, symétrique, positive ($\langle x, x\rangle \ge 0$) et définie ($\langle x, x\rangle = 0 \Rightarrow x = 0$).

Exemples : $\langle X, Y\rangle = {}^tXY$ sur $\mathbb R^n$ ; $\langle f, g\rangle = \int_a^bfg$ sur $\mathcal C([a, b])$ ; $\langle A, B\rangle = \operatorname{tr}({}^tAB)$.

> **Inégalité de Cauchy-Schwarz.** $|\langle x, y\rangle| \le \|x\|\,\|y\|$, avec égalité si et seulement si $x$ et $y$ sont colinéaires.

Identité de polarisation, théorème de Pythagore ($x \perp y \Rightarrow \|x + y\|^2 = \|x\|^2 + \|y\|^2$).

## Bases orthonormées

Dans une base orthonormée $(e_i)$ : $x = \sum\langle x, e_i\rangle e_i$ et $\|x\|^2 = \sum\langle x, e_i\rangle^2$.

**Procédé de Gram-Schmidt** : d'une famille libre, on construit une famille orthonormée engendrant les mêmes sous-espaces successifs.

## Projection orthogonale

[[fig:m1-prehilbertiens-1]]

> **Théorème.** Si $F$ est de dimension finie, $E = F \oplus F^\perp$. Le projeté orthogonal vaut $p_F(x) = \sum_i\langle x, e_i\rangle e_i$ pour une base orthonormée $(e_i)$ de $F$, et $d(x, F) = \|x - p_F(x)\| = \min_{y\in F}\|x - y\|$.

## Exemple corrigé

**Énoncé.** Déterminer $\displaystyle\min_{a, b\in\mathbb R}\int_0^1(x^2 - ax - b)^2\,\mathrm dx$.

**Solution.** C'est $d(x^2, F)^2$ avec $F = \operatorname{Vect}(1, x)$ pour $\langle f, g\rangle = \int_0^1fg$. Le projeté $ax + b$ vérifie $\langle x^2 - ax - b, 1\rangle = 0$ et $\langle x^2 - ax - b, x\rangle = 0$, soit $\frac13 = \frac a2 + b$ et $\frac14 = \frac a3 + \frac b2$ ; d'où $a = 1$, $b = -\frac16$. Le minimum vaut $\langle x^2 - x + \frac16, x^2\rangle = \frac15 - \frac14 + \frac1{18} = \frac{1}{180}$.

## Pièges classiques

- Ne pas oublier « définie » en vérifiant un produit scalaire.
- La formule du projeté exige une base **orthonormée** de $F$.
