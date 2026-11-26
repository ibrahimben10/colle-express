---
titre: Séries entières
---
## L'essentiel

Une série entière $\sum a_nz^n$ converge sur un disque (son disque de convergence) et y définit une fonction très régulière : continue, et même $\mathcal C^\infty$ sur l'intervalle réel ouvert, dérivable terme à terme.

## Rayon de convergence

[[fig:m2-series-entieres-1]]

> **Définition — Lemme d'Abel.** Si $(a_nz_0^n)$ est bornée, $\sum a_nz^n$ converge absolument pour $|z| < |z_0|$. Le rayon $R$ est la borne supérieure des $r$ tels que $(a_nr^n)$ soit bornée.

Calcul : **règle de d'Alembert** appliquée à $|a_{n+1}z^{n+1}|/|a_nz^n|$ ; comparaison ($|a_n| \le |b_n| \Rightarrow R_a \ge R_b$ ; $a_n \sim b_n \Rightarrow R_a = R_b$).

Le rayon ne change pas par dérivation ou intégration terme à terme.

## Régularité

> **Théorème.** La somme $S(x) = \sum a_nx^n$ est de classe $\mathcal C^\infty$ sur $]-R, R[$, ses dérivées s'obtiennent terme à terme, et $a_n = \frac{S^{(n)}(0)}{n!}$. On peut intégrer terme à terme sur $[0, x] \subset ]-R, R[$.

## Développements usuels

| Fonction | Développement | Rayon |
|---|---|---|
| $e^x$ | $\sum\frac{x^n}{n!}$ | $+\infty$ |
| $\frac{1}{1 - x}$ | $\sum x^n$ | 1 |
| $\ln(1 + x)$ | $\sum_{n\ge1}(-1)^{n-1}\frac{x^n}{n}$ | 1 |
| $(1 + x)^\alpha$ | $\sum\frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}x^n$ | 1 (si $\alpha \notin \mathbb N$) |
| $\cos x$, $\sin x$ | $\sum\frac{(-1)^nx^{2n}}{(2n)!}$, $\sum\frac{(-1)^nx^{2n+1}}{(2n+1)!}$ | $+\infty$ |
| $\arctan x$ | $\sum\frac{(-1)^nx^{2n+1}}{2n+1}$ | 1 |

## Méthodes

- Développer une fonction : opérations sur les DSE usuels, ou trouver une équation différentielle vérifiée par la fonction et chercher une solution série entière.
- Calculer une somme : reconnaître une dérivée ou une primitive d'une série connue.

## Exemple corrigé

**Énoncé.** Calculer $\sum_{n\ge1}nx^n$ pour $|x| < 1$.

**Solution.** Sur $]-1, 1[$, en dérivant $\sum x^n = \frac{1}{1 - x}$ terme à terme : $\sum nx^{n-1} = \frac{1}{(1 - x)^2}$. Donc $\sum_{n\ge1}nx^n = \frac{x}{(1 - x)^2}$.

## Pièges classiques

- Le comportement **sur** le cercle de convergence n'est pas donné par $R$.
- La règle de d'Alembert ne s'applique pas directement s'il y a des coefficients nuls (séries lacunaires) : l'appliquer à la série en $x^2$, par exemple.
