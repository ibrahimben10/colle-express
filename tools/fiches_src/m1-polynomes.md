---
titre: Polynômes
---
## L'essentiel

L'anneau $\mathbb K[X]$ ressemble à $\mathbb Z$ : division euclidienne, PGCD, Bézout, Gauss, décomposition en irréductibles. Les racines d'un polynôme sont liées à sa factorisation ; sur $\mathbb C$, tout polynôme est scindé.

## L'anneau $\mathbb K[X]$

- Degré : $\deg(PQ) = \deg P + \deg Q$, $\deg(P + Q) \le \max(\deg P, \deg Q)$, avec $\deg 0 = -\infty$. Coefficient dominant, polynôme unitaire.
- $\mathbb K[X]$ est intègre ; ses inversibles sont les constantes non nulles.
- Composition $P \circ Q$, dérivation formelle : $(PQ)' = P'Q + PQ'$, Leibniz.

## Divisibilité

> **Théorème — Division euclidienne.** Pour $A$ et $B \ne 0$, il existe un unique couple $(Q, R)$ avec $A = BQ + R$ et $\deg R < \deg B$.

Comme dans $\mathbb Z$ : PGCD (unitaire) par l'algorithme d'Euclide, **Bézout** ($A \wedge B = 1 \Leftrightarrow$ il existe $U$, $V$ avec $AU + BV = 1$), **Gauss**, PPCM.

## Racines

> **Propriété.** $a$ est racine de $P$ si et seulement si $(X - a) \mid P$. Le reste de la division de $P$ par $X - a$ est $P(a)$.

- Multiplicité : $a$ est racine d'ordre $m$ si $(X - a)^m \mid P$ et $(X - a)^{m+1} \nmid P$ ; caractérisation : $P(a) = P'(a) = \dots = P^{(m-1)}(a) = 0$ et $P^{(m)}(a) \ne 0$.
- Un polynôme non nul de degré $n$ a au plus $n$ racines comptées avec multiplicité. Donc un polynôme de degré $\le n$ qui a $n + 1$ racines est nul ; un polynôme qui a une infinité de racines est nul.
- **Formule de Taylor** : $P = \sum_k\frac{P^{(k)}(a)}{k!}(X - a)^k$.

### Polynômes scindés et relations coefficients-racines

$P$ est scindé s'il s'écrit $c\prod(X - x_i)$. Pour $P = a_nX^n + \dots + a_0$ scindé de racines $x_1, \dots, x_n$ : $\sigma_1 = \sum x_i = -\frac{a_{n-1}}{a_n}$, $\sigma_n = \prod x_i = (-1)^n\frac{a_0}{a_n}$, et plus généralement $\sigma_k = (-1)^k\frac{a_{n-k}}{a_n}$.

## Factorisation

> **Théorème de d'Alembert-Gauss.** Tout polynôme non constant de $\mathbb C[X]$ a au moins une racine ; donc tout polynôme de $\mathbb C[X]$ est scindé.

- **Irréductibles** de $\mathbb C[X]$ : les polynômes de degré 1.
- Irréductibles de $\mathbb R[X]$ : degré 1, et degré 2 à discriminant strictement négatif. Pour $P$ réel, si $z$ est racine, $\bar z$ aussi (même multiplicité).
- Tout polynôme se décompose de façon unique en produit d'une constante et d'irréductibles unitaires.

[[fig:m1-polynomes-1]]

Exemple : $X^n - 1 = \prod_{k=0}^{n-1}(X - e^{2ik\pi/n})$ dans $\mathbb C[X]$ ; dans $\mathbb R[X]$, on regroupe les racines conjuguées : $(X - e^{i\theta})(X - e^{-i\theta}) = X^2 - 2\cos\theta X + 1$.

## Interpolation de Lagrange

Pour $x_0, \dots, x_n$ distincts et $y_0, \dots, y_n$, il existe un unique $P$ de degré $\le n$ avec $P(x_i) = y_i$ : $P = \sum_iy_iL_i$, où $L_i = \prod_{j\ne i}\frac{X - x_j}{x_i - x_j}$.

## Fractions rationnelles (décomposition en éléments simples)

Sur $\mathbb C$ : $F = \frac PQ$ s'écrit (de façon unique) partie entière + somme de termes $\frac{a}{(X - \alpha)^k}$. Pour un pôle simple $\alpha$ : coefficient $\frac{P(\alpha)}{Q'(\alpha)}$. Utile pour primitiver et pour les sommes télescopiques.

## Exemple corrigé

**Énoncé.** Reste de la division de $X^n$ par $(X - 1)(X - 2)$.

**Solution.** $X^n = (X - 1)(X - 2)Q + aX + b$. En $X = 1$ : $a + b = 1$ ; en $X = 2$ : $2a + b = 2^n$. D'où $a = 2^n - 1$, $b = 2 - 2^n$ : $R = (2^n - 1)X + 2 - 2^n$.

## Exemple corrigé (factorisation)

**Énoncé.** Factoriser $X^4 + 1$ dans $\mathbb C[X]$ puis $\mathbb R[X]$.

**Solution.** Racines : $e^{i\pi/4}$, $e^{3i\pi/4}$ et leurs conjuguées. En regroupant : $X^4 + 1 = (X^2 - \sqrt2X + 1)(X^2 + \sqrt2X + 1)$, deux facteurs de discriminant $-2 < 0$, irréductibles sur $\mathbb R$.

## Pièges classiques

- $\deg(P + Q)$ peut être strictement inférieur au max (compensation des termes dominants).
- Sur $\mathbb R$, un polynôme sans racine réelle n'est pas forcément irréductible ($X^4 + 1$).
- Ne pas confondre le polynôme $P$ et la fonction $x \mapsto P(x)$ quand on parle de racines multiples : utiliser les dérivées.
