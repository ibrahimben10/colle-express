---
titre: Probabilités
---
## L'essentiel

En deuxième année, l'univers peut être infini : on travaille dans un espace probabilisé $(\Omega, \mathcal A, P)$ avec la $\sigma$-additivité, et avec des variables aléatoires **discrètes** (valeurs dénombrables).

## Espaces probabilisés

- $P\left(\bigcup A_n\right) = \sum P(A_n)$ pour des événements deux à deux incompatibles.
- **Continuité monotone** : si $(A_n)$ est croissante, $P\left(\bigcup A_n\right) = \lim P(A_n)$.
- Les formules des probabilités totales et de Bayes s'étendent aux systèmes complets dénombrables.

## Variables discrètes et lois usuelles

[[fig:m2-probas-1]]

| Loi | $P(X = k)$ | $E(X)$ | $V(X)$ |
|---|---|---|---|
| géométrique $\mathcal G(p)$, $k \ge 1$ | $(1 - p)^{k-1}p$ | $\frac1p$ | $\frac{1 - p}{p^2}$ |
| Poisson $\mathcal P(\lambda)$, $k \ge 0$ | $e^{-\lambda}\frac{\lambda^k}{k!}$ | $\lambda$ | $\lambda$ |

La loi géométrique est **sans mémoire** : $P(X > n + k \mid X > n) = P(X > k)$.

## Espérance et variance

$X$ admet une espérance si $\sum|x|P(X = x) < +\infty$. **Formule de transfert** : $E(f(X)) = \sum f(x)P(X = x)$ (sous réserve de convergence absolue). Covariance, $V(X + Y) = V(X) + V(Y) + 2\operatorname{Cov}(X, Y)$.

> **Inégalité de Markov.** Si $X \ge 0$ admet une espérance, $P(X \ge a) \le \frac{E(X)}{a}$ ($a > 0$). **Bienaymé-Tchebychev** : $P(|X - E(X)| \ge a) \le \frac{V(X)}{a^2}$.

> **Loi faible des grands nombres.** Si les $X_i$ sont indépendantes, de même loi, de variance finie, alors pour tout $\varepsilon > 0$, $P\left(\left|\frac{X_1 + \dots + X_n}{n} - m\right| \ge \varepsilon\right) \to 0$.

## Fonctions génératrices

$G_X(t) = E(t^X) = \sum P(X = k)t^k$ (variables à valeurs dans $\mathbb N$) : elle caractérise la loi, $E(X) = G_X'(1)$ et $G_{X+Y} = G_XG_Y$ si $X$ et $Y$ sont indépendantes.

## Exemple corrigé

**Énoncé.** $X \sim \mathcal P(\lambda)$ et $Y \sim \mathcal P(\mu)$ indépendantes. Loi de $X + Y$ ?

**Solution.** $G_X(t) = e^{\lambda(t - 1)}$, $G_Y(t) = e^{\mu(t - 1)}$. Par indépendance, $G_{X+Y}(t) = e^{(\lambda + \mu)(t - 1)}$ : c'est la fonction génératrice de $\mathcal P(\lambda + \mu)$, qui caractérise la loi. Donc $X + Y \sim \mathcal P(\lambda + \mu)$.

## Pièges classiques

- Toute variable n'admet pas d'espérance : vérifier la convergence **absolue**.
- Indépendantes deux à deux n'implique pas mutuellement indépendantes.
