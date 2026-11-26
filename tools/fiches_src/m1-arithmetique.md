---
titre: Arithmétique dans ℤ
---
## L'essentiel

Divisibilité, division euclidienne, PGCD et nombres premiers : tout repose sur l'algorithme d'Euclide et sur la relation de Bézout.

## Division euclidienne et PGCD

> **Théorème — Division euclidienne.** Pour $a \in \mathbb Z$ et $b \ge 1$, il existe un unique couple $(q, r)$ tel que $a = bq + r$ et $0 \le r < b$.

**Algorithme d'Euclide** : $\operatorname{pgcd}(a, b) = \operatorname{pgcd}(b, r)$ ; le dernier reste non nul est le PGCD.

> **Théorème de Bézout.** $a$ et $b$ sont premiers entre eux si et seulement s'il existe $u, v \in \mathbb Z$ tels que $au + bv = 1$. Plus généralement, il existe $u, v$ avec $au + bv = \operatorname{pgcd}(a, b)$ (algorithme d'Euclide étendu).

> **Lemme de Gauss.** Si $a \mid bc$ et $\operatorname{pgcd}(a, b) = 1$, alors $a \mid c$.

$\operatorname{pgcd}(a, b) \times \operatorname{ppcm}(a, b) = |ab|$.

## Nombres premiers

- Il existe une infinité de nombres premiers.
- **Décomposition** : tout entier $n \ge 2$ s'écrit de façon unique (à l'ordre près) comme produit de nombres premiers.
- Si $p$ premier divise $ab$, alors $p \mid a$ ou $p \mid b$.

## Congruences

$a \equiv b\ [n]$ si $n \mid a - b$ ; compatible avec $+$ et $\times$.

> **Petit théorème de Fermat.** Si $p$ est premier et $p \nmid a$, alors $a^{p-1} \equiv 1\ [p]$ ; pour tout $a$, $a^p \equiv a\ [p]$.

## Exemple corrigé

**Énoncé.** Résoudre dans $\mathbb Z^2$ l'équation $7x + 5y = 1$.

**Solution.** Solution particulière : $7\times(-2) + 5\times3 = 1$. Si $(x, y)$ est solution, $7(x + 2) = -5(y - 3)$ ; 7 divise $5(y - 3)$ et est premier avec 5, donc par Gauss $7 \mid y - 3$ : $y = 3 + 7k$, puis $x = -2 - 5k$. Réciproquement ces couples conviennent : $\{(-2 - 5k, 3 + 7k),\ k \in \mathbb Z\}$.

## Pièges classiques

- On ne simplifie une congruence par $c$ que si $c$ est premier avec le module.
- Bien faire la réciproque dans les équations diophantiennes.
