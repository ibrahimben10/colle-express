---
titre: Limites et continuité
---
## L'essentiel

La continuité permet d'énoncer trois grands théorèmes : valeurs intermédiaires, bornes atteintes sur un segment, et continuité de la réciproque d'une bijection continue.

## Limites

> **Définition.** $f(x) \xrightarrow[x\to a]{} \ell$ si $\forall\varepsilon > 0,\ \exists\eta > 0,\ \forall x \in D,\ |x - a| \le \eta \Rightarrow |f(x) - \ell| \le \varepsilon$.

> **Propriété — Caractérisation séquentielle.** $f(x) \to \ell$ quand $x \to a$ si et seulement si, pour toute suite $(x_n)$ de $D$ tendant vers $a$, $f(x_n) \to \ell$. Utile pour montrer qu'une limite **n'existe pas** (deux suites donnant deux limites différentes).

## Continuité

$f$ est continue en $a$ si $f(x) \to f(a)$. Les sommes, produits, quotients (dénominateur non nul) et composées de fonctions continues sont continues.

## Théorèmes fondamentaux

[[fig:m1-continuite-1]]

> **Théorème des valeurs intermédiaires.** Si $f$ est continue sur un intervalle $I$, alors $f(I)$ est un intervalle. En particulier, si $f$ est continue sur $[a, b]$ et $f(a)f(b) \le 0$, $f$ s'annule sur $[a, b]$.

> **Théorème des bornes atteintes.** Une fonction continue sur un **segment** $[a, b]$ est bornée et atteint ses bornes : $f([a, b]) = [m, M]$.

> **Théorème de la bijection.** Si $f$ est continue et strictement monotone sur un intervalle $I$, elle réalise une bijection de $I$ sur l'intervalle $f(I)$, et sa réciproque est continue et de même monotonie.

> **Théorème de Heine.** Une fonction continue sur un segment y est uniformément continue.

## Exemple corrigé

**Énoncé.** Montrer que l'équation $x^5 + x - 1 = 0$ a une unique solution réelle.

**Solution.** $f(x) = x^5 + x - 1$ est continue et $f'(x) = 5x^4 + 1 > 0$ : $f$ est strictement croissante. $f(0) = -1 < 0$ et $f(1) = 1 > 0$ : par le TVI, $f$ s'annule sur $[0, 1]$ ; par stricte monotonie, ce zéro est unique (et il est dans $]0, 1[$).

## Pièges classiques

- Le TVI demande un **intervalle** et la continuité ; les bornes atteintes demandent un **segment** (fermé, borné).
- Le TVI donne l'existence, pas l'unicité : il faut la monotonie pour l'unicité.
- Une fonction peut avoir une limite en $a$ sans être définie en $a$.
