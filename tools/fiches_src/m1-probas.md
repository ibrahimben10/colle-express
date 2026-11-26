---
titre: Probabilités sur un univers fini
---
## L'essentiel

Sur un univers fini, une probabilité attribue un poids à chaque événement. Probabilités conditionnelles, indépendance, formules des probabilités totales et de Bayes permettent de calculer ; les variables aléatoires, leur espérance et leur variance résument une expérience.

## Espaces probabilisés finis

- Univers $\Omega$ fini, événements = parties de $\Omega$. Une probabilité vérifie $P(\Omega) = 1$ et $P(A \cup B) = P(A) + P(B)$ si $A \cap B = \emptyset$.
- $P(\bar A) = 1 - P(A)$, $P(A \cup B) = P(A) + P(B) - P(A \cap B)$, $A \subset B \Rightarrow P(A) \le P(B)$.
- Une probabilité est déterminée par les $P(\{\omega\})$. **Équiprobabilité** : $P(A) = \frac{\operatorname{Card}A}{\operatorname{Card}\Omega}$.

## Conditionnement

$P_B(A) = P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ (si $P(B) > 0$) : c'est une probabilité.

> **Théorème — Probabilités composées.** $P(A_1 \cap \dots \cap A_n) = P(A_1)P_{A_1}(A_2)\cdots P_{A_1\cap\dots\cap A_{n-1}}(A_n)$.

> **Théorème — Probabilités totales.** Si $(A_i)$ est un système complet d'événements (partition de $\Omega$) : $P(B) = \sum_iP(A_i)P_{A_i}(B)$.

> **Théorème — Formule de Bayes.** $P_B(A_j) = \frac{P(A_j)P_{A_j}(B)}{\sum_iP(A_i)P_{A_i}(B)}$.

[[fig:m1-probas-1]]

## Indépendance

$A$ et $B$ sont indépendants si $P(A \cap B) = P(A)P(B)$. Des événements $A_1, \dots, A_n$ sont **mutuellement** indépendants si $P\left(\bigcap_{i\in J}A_i\right) = \prod_{i\in J}P(A_i)$ pour toute partie $J$. Si $A$ et $B$ sont indépendants, $A$ et $\bar B$ aussi.

## Variables aléatoires

$X : \Omega \to E$ ; sa **loi** est la donnée des $P(X = x)$. Pour $f$ une fonction, $f(X)$ est une variable aléatoire.

### Lois usuelles

| Loi | Valeurs | $P(X = k)$ | $E(X)$ | $V(X)$ |
|---|---|---|---|---|
| uniforme sur $\{1, \dots, n\}$ | $1, \dots, n$ | $\frac1n$ | $\frac{n+1}{2}$ | $\frac{n^2-1}{12}$ |
| Bernoulli $\mathcal B(p)$ | 0, 1 | $P(X = 1) = p$ | $p$ | $p(1 - p)$ |
| binomiale $\mathcal B(n, p)$ | $0, \dots, n$ | $\binom nkp^k(1 - p)^{n-k}$ | $np$ | $np(1 - p)$ |

La binomiale compte le nombre de succès dans $n$ épreuves de Bernoulli indépendantes de même paramètre.

## Couples et indépendance de variables

Loi conjointe $P(X = x, Y = y)$, lois marginales par sommation. $X$ et $Y$ sont indépendantes si $P(X = x, Y = y) = P(X = x)P(Y = y)$ pour tous $x$, $y$ ; alors $f(X)$ et $g(Y)$ le sont aussi.

## Espérance et variance

- $E(X) = \sum_xxP(X = x)$ ; linéarité ; positivité ; **formule de transfert** $E(f(X)) = \sum_xf(x)P(X = x)$.
- Si $X$ et $Y$ sont indépendantes, $E(XY) = E(X)E(Y)$.
- $V(X) = E((X - E(X))^2) = E(X^2) - E(X)^2$ ; $V(aX + b) = a^2V(X)$ ; écart type $\sigma = \sqrt{V}$.
- Covariance $\operatorname{Cov}(X, Y) = E(XY) - E(X)E(Y)$ ; $V(X + Y) = V(X) + V(Y) + 2\operatorname{Cov}(X, Y)$ ; si $X$ et $Y$ sont indépendantes, la covariance est nulle.

> **Inégalités.** Markov : $P(X \ge a) \le \frac{E(X)}{a}$ pour $X \ge 0$, $a > 0$. Bienaymé-Tchebychev : $P(|X - E(X)| \ge a) \le \frac{V(X)}{a^2}$.

## Exemple corrigé

**Énoncé.** Un test détecte une maladie (prévalence 1 %) avec 99 % de sensibilité et 2 % de faux positifs. Test positif : probabilité d'être malade ?

**Solution.** $M$ : malade, $T$ : test positif. Probabilités totales : $P(T) = 0{,}01\times0{,}99 + 0{,}99\times0{,}02 = 0{,}0297$. Bayes : $P_T(M) = \frac{0{,}0099}{0{,}0297} = \frac13$.

## Exemple corrigé (binomiale)

**Énoncé.** On lance 10 fois une pièce équilibrée. Probabilité d'au moins un pile ? Espérance et variance du nombre de piles ?

**Solution.** $X \sim \mathcal B(10, \frac12)$. $P(X \ge 1) = 1 - P(X = 0) = 1 - \frac{1}{1024}$. $E(X) = 5$, $V(X) = 2{,}5$.

## Pièges classiques

- Incompatibles ($A \cap B = \emptyset$) n'est pas indépendants.
- Indépendants deux à deux ne donne pas mutuellement indépendants.
- $V(X + Y) = V(X) + V(Y)$ exige une covariance nulle (par exemple l'indépendance).
