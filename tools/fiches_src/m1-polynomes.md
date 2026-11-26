---
titre: Polynômes
---
## L'essentiel

L'anneau $\mathbb K[X]$ ressemble à $\mathbb Z$ : division euclidienne, PGCD, factorisation en irréductibles. Les racines d'un polynôme sont liées à sa factorisation et à ses coefficients.

## Degré et division euclidienne

$\deg(PQ) = \deg P + \deg Q$ ; $\deg(P + Q) \le \max(\deg P, \deg Q)$.

> **Théorème — Division euclidienne.** Pour $A$, $B \ne 0$, il existe un unique couple $(Q, R)$ avec $A = BQ + R$ et $\deg R < \deg B$.

## Racines

- $a$ est racine de $P$ si et seulement si $(X - a) \mid P$.
- Racine d'ordre $m$ : $P(a) = P'(a) = \dots = P^{(m-1)}(a) = 0$ et $P^{(m)}(a) \ne 0$.
- Un polynôme non nul de degré $n$ a au plus $n$ racines (comptées avec multiplicité) : un polynôme qui a une infinité de racines est nul.

[[fig:m1-polynomes-1]]

> **Théorème de d'Alembert-Gauss.** Tout polynôme non constant de $\mathbb C[X]$ a au moins une racine ; il est donc scindé sur $\mathbb C$.

- Irréductibles de $\mathbb C[X]$ : degré 1. De $\mathbb R[X]$ : degré 1 et degré 2 à discriminant négatif.
- **Relations coefficients-racines** : pour $P = a_n\prod(X - x_i)$, $\sum x_i = -\frac{a_{n-1}}{a_n}$ et $\prod x_i = (-1)^n\frac{a_0}{a_n}$.

## Interpolation de Lagrange

Pour $n + 1$ points d'abscisses distinctes, il existe un unique polynôme de degré $\le n$ qui y passe : $P = \sum_iy_iL_i$, avec $L_i = \prod_{j\ne i}\frac{X - x_j}{x_i - x_j}$.

## Fractions rationnelles

Décomposition en éléments simples (partie entière + termes $\frac{a}{(X - \alpha)^k}$ sur $\mathbb C$) ; pour un pôle simple $\alpha$ de $\frac{P}{Q}$, le coefficient vaut $\frac{P(\alpha)}{Q'(\alpha)}$.

## Exemple corrigé

**Énoncé.** Factoriser $X^4 + 1$ dans $\mathbb C[X]$ puis $\mathbb R[X]$.

**Solution.** Les racines sont les $z$ avec $z^4 = -1 = e^{i\pi}$ : $e^{i\pi/4}, e^{3i\pi/4}$ et leurs conjugués. En regroupant les racines conjuguées : $X^4 + 1 = (X^2 - \sqrt2X + 1)(X^2 + \sqrt2X + 1)$ dans $\mathbb R[X]$.

## Pièges classiques

- Le degré du polynôme nul est $-\infty$.
- Sur $\mathbb R$, un polynôme peut n'avoir aucune racine sans être irréductible ($X^4 + 1$).
