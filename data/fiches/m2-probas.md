---
titre: Probabilités
---
## L'essentiel

En deuxième année, l'univers peut être infini : un espace probabilisé $(\Omega, \mathcal A, P)$ avec une tribu et la $\sigma$-additivité. On étudie les variables aléatoires **discrètes** (valeurs dénombrables), les lois géométrique et de Poisson, l'espérance, la variance, les fonctions génératrices et la loi faible des grands nombres.

## Espaces probabilisés

- **Tribu** $\mathcal A$ : contient $\Omega$, stable par complémentaire et par réunion (et intersection) **dénombrable**.
- **Probabilité** : $P(\Omega) = 1$ et $\sigma$-additivité : $P\left(\bigcup A_n\right) = \sum P(A_n)$ pour des $A_n$ deux à deux incompatibles.
- Sur un ensemble dénombrable, une probabilité est donnée par une famille $(p_\omega)$ positive de somme 1.
- **Continuité monotone** : si $(A_n)$ est croissante, $P\left(\bigcup A_n\right) = \lim P(A_n)$ ; si décroissante, $P\left(\bigcap A_n\right) = \lim P(A_n)$.
- **Sous-additivité** : $P\left(\bigcup A_n\right) \le \sum P(A_n)$. Événement presque sûr, négligeable.
- Probabilités conditionnelles, probabilités composées, **probabilités totales** et **Bayes** pour un système complet dénombrable ; indépendance (mutuelle) d'une suite d'événements.

## Variables aléatoires discrètes

$X : \Omega \to E$ avec $X(\Omega)$ dénombrable et $\{X = x\} \in \mathcal A$. Loi : $(P(X = x))_{x\in X(\Omega)}$. Pour une fonction $f$, $f(X)$ est une variable discrète.

### Lois usuelles

[[fig:m2-probas-1]]

| Loi | $P(X = k)$ |
|---|---|
| Bernoulli $\mathcal B(p)$ | $P(X = 1) = p$, $P(X = 0) = 1 - p$ |
| binomiale $\mathcal B(n, p)$ | $\binom nkp^k(1 - p)^{n-k}$, $0 \le k \le n$ |
| géométrique $\mathcal G(p)$ | $(1 - p)^{k-1}p$, $k \ge 1$ |
| Poisson $\mathcal P(\lambda)$ | $e^{-\lambda}\frac{\lambda^k}{k!}$, $k \ge 0$ |

| Loi | $E(X)$ | $V(X)$ | $G_X(t)$ |
|---|---|---|---|
| $\mathcal B(p)$ | $p$ | $p(1 - p)$ | $1 - p + pt$ |
| $\mathcal B(n, p)$ | $np$ | $np(1 - p)$ | $(1 - p + pt)^n$ |
| $\mathcal G(p)$ | $\frac1p$ | $\frac{1 - p}{p^2}$ | $\frac{pt}{1 - (1 - p)t}$ |
| $\mathcal P(\lambda)$ | $\lambda$ | $\lambda$ | $e^{\lambda(t - 1)}$ |

- La géométrique est le rang du premier succès dans une suite d'épreuves de Bernoulli indépendantes ; elle est **sans mémoire** : $P(X > n + k \mid X > n) = P(X > k)$, et c'est la seule loi sur $\mathbb N^*$ qui le soit.
- **Approximation** : si $np_n \to \lambda$, $P(X_n = k) \to e^{-\lambda}\frac{\lambda^k}{k!}$ pour $X_n \sim \mathcal B(n, p_n)$.

## Couples, indépendance

Loi conjointe, lois marginales ($P(X = x) = \sum_yP(X = x, Y = y)$), lois conditionnelles. Indépendance de $X$ et $Y$ : $P(X \in A, Y \in B) = P(X \in A)P(Y \in B)$. Lemme des coalitions : des fonctions de paquets disjoints de variables indépendantes sont indépendantes.

Loi d'une somme : $P(X + Y = n) = \sum_kP(X = k)P(Y = n - k)$ si $X$ et $Y$ sont indépendantes (à valeurs entières).

## Espérance et variance

- $X$ (réelle) admet une espérance si $\sum|x|P(X = x) < +\infty$ (famille sommable) ; $E(X) = \sum xP(X = x)$. Linéarité, positivité, croissance.
- **Formule de transfert** : $f(X)$ admet une espérance si et seulement si $\sum|f(x)|P(X = x) < +\infty$, et alors $E(f(X)) = \sum f(x)P(X = x)$.
- Pour $X$ à valeurs dans $\mathbb N$ : $E(X) = \sum_{n\ge1}P(X \ge n)$.
- Si $X$ et $Y$ sont indépendantes et admettent une espérance, $E(XY) = E(X)E(Y)$.
- Moment d'ordre 2 : si $E(X^2)$ existe, $E(X)$ existe ; $V(X) = E(X^2) - E(X)^2$, $V(aX + b) = a^2V(X)$. Cauchy-Schwarz : $E(XY)^2 \le E(X^2)E(Y^2)$.
- Covariance, $V\left(\sum X_i\right) = \sum V(X_i) + 2\sum_{i<j}\operatorname{Cov}(X_i, X_j)$ ; coefficient de corrélation dans $[-1, 1]$.

> **Inégalités.** Markov : $P(X \ge a) \le \frac{E(X)}{a}$ ($X \ge 0$, $a > 0$). Bienaymé-Tchebychev : $P(|X - E(X)| \ge a) \le \frac{V(X)}{a^2}$.

> **Loi faible des grands nombres.** Si $(X_n)$ est une suite de variables indépendantes, de même loi, admettant une variance, d'espérance $m$, alors pour tout $\varepsilon > 0$ : $P\left(\left|\frac{X_1 + \dots + X_n}{n} - m\right| \ge \varepsilon\right) \le \frac{V(X_1)}{n\varepsilon^2} \to 0$.

## Fonctions génératrices

Pour $X$ à valeurs dans $\mathbb N$ : $G_X(t) = E(t^X) = \sum P(X = n)t^n$, série entière de rayon $\ge 1$, convergeant normalement sur $[-1, 1]$.

- $G_X$ **caractérise** la loi : $P(X = n) = \frac{G_X^{(n)}(0)}{n!}$.
- $X$ admet une espérance si et seulement si $G_X$ est dérivable en 1, et $E(X) = G_X'(1)$ ; $V(X) = G_X''(1) + G_X'(1) - G_X'(1)^2$ (si $G_X$ est deux fois dérivable en 1).
- Si $X$ et $Y$ sont indépendantes, $G_{X+Y} = G_XG_Y$.

## Exemple corrigé

**Énoncé.** $X \sim \mathcal P(\lambda)$ et $Y \sim \mathcal P(\mu)$ indépendantes. Loi de $X + Y$ ?

**Solution.** $G_{X+Y}(t) = G_X(t)G_Y(t) = e^{\lambda(t-1)}e^{\mu(t-1)} = e^{(\lambda+\mu)(t-1)}$ : c'est la fonction génératrice de $\mathcal P(\lambda + \mu)$, qui caractérise la loi. Donc $X + Y \sim \mathcal P(\lambda + \mu)$.

## Exemple corrigé (géométrique)

**Énoncé.** On lance un dé équilibré jusqu'à obtenir un 6. Espérance du nombre de lancers ? Probabilité qu'il en faille plus de 10 ?

**Solution.** $N \sim \mathcal G(\frac16)$ : $E(N) = 6$. $P(N > 10) = \left(\frac56\right)^{10}$ (dix échecs de suite) $\approx 0{,}16$.

## Pièges classiques

- Une variable discrète n'a pas toujours d'espérance : vérifier la convergence **absolue**.
- Indépendantes deux à deux n'implique pas mutuellement indépendantes.
- Covariance nulle n'implique pas indépendance.
- Préciser si la loi géométrique commence à 1 (premier succès) ou à 0 (nombre d'échecs).
