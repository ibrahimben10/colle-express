---
titre: Dérivabilité
---
## L'essentiel

La dérivée mesure la variation locale d'une fonction. Le théorème de Rolle et celui des accroissements finis relient la dérivée aux variations globales ; la convexité se lit sur la dérivée seconde.

## Dérivée

$f$ est dérivable en $a$ si $\dfrac{f(x) - f(a)}{x - a}$ a une limite finie $f'(a)$ ; la tangente a pour équation $y = f(a) + f'(a)(x - a)$. Dérivable implique continue (la réciproque est fausse : $|x|$ en 0).

Formules : $(fg)' = f'g + fg'$, $(f\circ g)' = g'\times f'\circ g$, $(f^{-1})' = \dfrac{1}{f'\circ f^{-1}}$ là où $f'$ ne s'annule pas ; formule de **Leibniz** $(fg)^{(n)} = \sum_k\binom nk f^{(k)}g^{(n-k)}$.

## Théorèmes de Rolle et des accroissements finis

[[fig:m1-derivabilite-1]]

> **Théorème de Rolle.** Si $f$ est continue sur $[a, b]$, dérivable sur $]a, b[$ et $f(a) = f(b)$, il existe $c \in ]a, b[$ tel que $f'(c) = 0$.

> **Théorème des accroissements finis.** Sous les mêmes hypothèses sans $f(a) = f(b)$ : il existe $c \in ]a, b[$ tel que $f(b) - f(a) = f'(c)(b - a)$.

> **Inégalité des accroissements finis.** Si $|f'| \le k$ sur $I$, alors $|f(x) - f(y)| \le k|x - y|$ ($f$ est $k$-lipschitzienne).

Conséquences : $f' \ge 0$ sur un intervalle $\Rightarrow$ $f$ croissante ; **théorème de la limite de la dérivée** : si $f$ est continue en $a$ et $f'(x) \to \ell$ quand $x \to a$, alors $f$ est dérivable en $a$ et $f'(a) = \ell$.

## Convexité

[[fig:m1-derivabilite-2]]

> **Définition.** $f$ est convexe sur $I$ si $f(\lambda x + (1 - \lambda)y) \le \lambda f(x) + (1 - \lambda)f(y)$ pour tous $x, y \in I$, $\lambda \in [0, 1]$ : la courbe est sous ses cordes.

Si $f$ est dérivable : convexe $\Leftrightarrow$ $f'$ croissante $\Leftrightarrow$ la courbe est au-dessus de ses tangentes. Si $f$ est deux fois dérivable : convexe $\Leftrightarrow$ $f'' \ge 0$. **Inégalité de Jensen** : $f\left(\sum\lambda_ix_i\right) \le \sum\lambda_if(x_i)$ ($\lambda_i \ge 0$, $\sum\lambda_i = 1$).

## Exemple corrigé

**Énoncé.** Montrer que pour $0 < x < y$ : $\dfrac{y - x}{y} < \ln y - \ln x < \dfrac{y - x}{x}$.

**Solution.** $\ln$ est continue sur $[x, y]$ et dérivable : par les accroissements finis, il existe $c \in ]x, y[$ avec $\ln y - \ln x = \dfrac{y - x}{c}$. Comme $x < c < y$, on a $\dfrac1y < \dfrac1c < \dfrac1x$, d'où l'encadrement.

## Pièges classiques

- Le $c$ des accroissements finis est **dans l'intervalle ouvert** et n'est pas explicite.
- Rolle ne s'applique pas aux fonctions à valeurs complexes ; l'inégalité des accroissements finis, si.
- $f'(a) = 0$ n'implique pas un extremum ($x^3$ en 0).
