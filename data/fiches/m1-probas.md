---
titre: Probabilités sur un univers fini
---
## L'essentiel

Sur un univers fini, une probabilité est une fonction additive de masse totale 1. Les probabilités conditionnelles, la formule des probabilités totales et celle de Bayes permettent de raisonner étape par étape ; les variables aléatoires résument une expérience par des nombres.

## Probabilités conditionnelles

$P_B(A) = \frac{P(A \cap B)}{P(B)}$ si $P(B) > 0$.

[[fig:m1-probas-1]]

> **Formule des probabilités totales.** Si $(A_i)$ est un système complet d'événements : $P(B) = \sum_iP(A_i)P_{A_i}(B)$.

> **Formule de Bayes.** $P_B(A_j) = \dfrac{P(A_j)P_{A_j}(B)}{\sum_iP(A_i)P_{A_i}(B)}$.

**Formule des probabilités composées** : $P(A_1 \cap \dots \cap A_n) = P(A_1)P_{A_1}(A_2)\cdots P_{A_1\cap\dots\cap A_{n-1}}(A_n)$.

$A$ et $B$ sont **indépendants** si $P(A \cap B) = P(A)P(B)$.

## Variables aléatoires

- **Espérance** $E(X) = \sum_xxP(X = x)$, linéaire ; **variance** $V(X) = E(X^2) - E(X)^2$, $V(aX + b) = a^2V(X)$.
- Si $X$ et $Y$ sont indépendantes : $E(XY) = E(X)E(Y)$ et $V(X + Y) = V(X) + V(Y)$.

| Loi | $P(X = k)$ | $E$ | $V$ |
|---|---|---|---|
| Bernoulli $\mathcal B(p)$ | $P(X = 1) = p$ | $p$ | $p(1 - p)$ |
| binomiale $\mathcal B(n, p)$ | $\binom nkp^k(1 - p)^{n-k}$ | $np$ | $np(1 - p)$ |
| uniforme sur $\{1, \dots, n\}$ | $\frac1n$ | $\frac{n+1}{2}$ | $\frac{n^2 - 1}{12}$ |

> **Inégalité de Bienaymé-Tchebychev.** $P(|X - E(X)| \ge a) \le \dfrac{V(X)}{a^2}$ pour $a > 0$.

## Exemple corrigé

**Énoncé.** Un test détecte une maladie (prévalence 1 %) avec une sensibilité de 99 % et 2 % de faux positifs. Le test est positif : probabilité d'être malade ?

**Solution.** $P(+) = 0{,}01\times0{,}99 + 0{,}99\times0{,}02 = 0{,}0297$. Par Bayes, $P_+(M) = \frac{0{,}0099}{0{,}0297} = \frac13$ : seulement une chance sur trois, car la maladie est rare.

## Pièges classiques

- Ne pas confondre $P_B(A)$ et $P_A(B)$.
- Incompatibles n'est pas indépendants.
- $V(X + Y) = V(X) + V(Y)$ demande l'indépendance (ou au moins la non-corrélation).
