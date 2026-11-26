---
titre: Dimension finie et rang
---
## L'essentiel

En dimension finie, toutes les bases ont le même nombre d'éléments : la dimension. Elle permet de compter : formule de Grassmann, théorème du rang, et surtout « injective ⇔ surjective ⇔ bijective » pour un endomorphisme.

## Dimension

> **Théorème — Base incomplète.** Dans un espace engendré par une famille finie, toute famille libre peut être complétée en une base à l'aide de vecteurs d'une famille génératrice donnée. En particulier, il existe des bases.

> **Théorème — Dimension.** Toutes les bases d'un espace de dimension finie ont le même cardinal $n = \dim E$. Une famille libre a au plus $n$ éléments, une famille génératrice au moins $n$.

> **Propriété.** En dimension $n$, une famille de $n$ vecteurs est une base si et seulement si elle est libre, si et seulement si elle est génératrice.

Dimensions usuelles : $\dim\mathbb K^n = n$, $\dim\mathbb K_n[X] = n + 1$, $\dim M_{n,p}(\mathbb K) = np$, $\dim\mathcal L(E, F) = \dim E\cdot\dim F$, $\dim(E \times F) = \dim E + \dim F$. Solutions de $y'' + ay' + by = 0$ : dimension 2 ; suites récurrentes linéaires d'ordre 2 : dimension 2.

## Sous-espaces en dimension finie

- Si $F \subset E$, $\dim F \le \dim E$, avec égalité si et seulement si $F = E$.
- Tout sous-espace admet un supplémentaire.

> **Théorème — Formule de Grassmann.** $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$.

> **Propriété — Supplémentaires.** $E = F \oplus G$ si et seulement si $F \cap G = \{0\}$ et $\dim F + \dim G = \dim E$ (ou : $F + G = E$ et $\dim F + \dim G = \dim E$).

Hyperplans : noyaux des formes linéaires non nulles, de dimension $n - 1$.

## Rang

$\operatorname{rg}(x_1, \dots, x_p) = \dim\operatorname{Vect}(x_i)$ ; $\operatorname{rg}u = \dim\operatorname{Im}u$.

> **Théorème du rang.** Si $E$ est de dimension finie et $u \in \mathcal L(E, F)$ : $\dim E = \dim\ker u + \operatorname{rg}u$.

Plus précisément, tout supplémentaire de $\ker u$ est isomorphe à $\operatorname{Im}u$.

> **Théorème — Cas $\dim E = \dim F$.** Si $\dim E = \dim F$ (finie), pour $u \in \mathcal L(E, F)$ : $u$ injective $\Leftrightarrow$ $u$ surjective $\Leftrightarrow$ $u$ bijective.

Conséquences : pour un endomorphisme, il suffit de montrer l'injectivité ($\ker u = \{0\}$) pour avoir la bijectivité ; pour des matrices carrées, $AB = I$ suffit pour $B = A^{-1}$.

- $\operatorname{rg}(v \circ u) \le \min(\operatorname{rg}u, \operatorname{rg}v)$ ; composer par un isomorphisme ne change pas le rang.
- Deux espaces de dimension finie sont isomorphes si et seulement s'ils ont la même dimension.

## Exemple corrigé

**Énoncé.** Montrer que pour $a_0, \dots, a_n$ distincts, $\varphi : \mathbb R_n[X] \to \mathbb R^{n+1}$, $P \mapsto (P(a_0), \dots, P(a_n))$ est un isomorphisme.

**Solution.** $\varphi$ est linéaire. Si $\varphi(P) = 0$, $P$ (de degré $\le n$) a $n + 1$ racines distinctes, donc $P = 0$ : $\varphi$ est injective. Comme $\dim\mathbb R_n[X] = \dim\mathbb R^{n+1} = n + 1$, elle est bijective. C'est l'existence et l'unicité de l'interpolation de Lagrange.

## Exemple corrigé (Grassmann)

**Énoncé.** Deux hyperplans distincts $H_1$, $H_2$ de $E$ ($\dim E = n$) : dimension de $H_1 \cap H_2$ ?

**Solution.** $H_1 \subsetneq H_1 + H_2$, donc $\dim(H_1 + H_2) = n$. Grassmann : $\dim(H_1 \cap H_2) = (n - 1) + (n - 1) - n = n - 2$.

## Pièges classiques

- « Injective ⇔ bijective » n'est vrai qu'en dimension finie et entre espaces de **même dimension** ; la dérivation sur $\mathbb K[X]$ est surjective sans être injective.
- Le théorème du rang porte sur la dimension de l'espace de **départ**.
- Une famille de $n$ vecteurs génératrice d'un espace de dimension $n$ est automatiquement libre : ne pas refaire les deux preuves.
