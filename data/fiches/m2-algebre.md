---
titre: Compléments d'algèbre générale
---
## L'essentiel

En deuxième année : sous-groupes de $\mathbb Z$, groupes monogènes, ordre d'un élément, anneaux $\mathbb Z/n\mathbb Z$, idéaux, et anneau $\mathbb K[X]$ revu sous l'angle des idéaux.

## Groupes

- Les sous-groupes de $(\mathbb Z, +)$ sont les $n\mathbb Z$.
- Sous-groupe engendré par $a$ : $\langle a\rangle = \{a^k,\ k \in \mathbb Z\}$. Un groupe est **monogène** s'il est engendré par un élément, **cyclique** s'il est de plus fini ; tout groupe cyclique d'ordre $n$ est isomorphe à $(\mathbb Z/n\mathbb Z, +)$.
- **Ordre** de $a$ : plus petit $n \ge 1$ tel que $a^n = e$ (s'il existe) ; $a^k = e \Leftrightarrow n \mid k$.

> **Théorème de Lagrange (cas commutatif au programme).** Dans un groupe fini, l'ordre de tout élément divise l'ordre du groupe ; donc $a^{|G|} = e$.

## Anneaux et idéaux

> **Définition.** Un idéal $I$ d'un anneau commutatif $A$ est un sous-groupe additif tel que $a \in A$, $x \in I \Rightarrow ax \in I$. Le noyau d'un morphisme d'anneaux est un idéal.

Les idéaux de $\mathbb Z$ sont les $n\mathbb Z$ ; ceux de $\mathbb K[X]$ sont les $P\,\mathbb K[X]$ (anneaux principaux) : d'où le PGCD comme générateur de $I + J$.

## L'anneau $\mathbb Z/n\mathbb Z$

- $\bar k$ est inversible si et seulement si $\operatorname{pgcd}(k, n) = 1$ ; $\mathbb Z/n\mathbb Z$ est un corps si et seulement si $n$ est premier.
- **Indicatrice d'Euler** $\varphi(n)$ = nombre d'inversibles ; $\varphi(p^k) = p^k - p^{k-1}$, multiplicative.

> **Théorème d'Euler.** Si $\operatorname{pgcd}(a, n) = 1$, alors $a^{\varphi(n)} \equiv 1\ [n]$.

> **Théorème chinois.** Si $m$ et $n$ sont premiers entre eux, $\mathbb Z/mn\mathbb Z \simeq \mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z$ (isomorphisme d'anneaux).

## Exemple corrigé

**Énoncé.** Trouver le dernier chiffre de $7^{2026}$.

**Solution.** On travaille modulo 10 : $\varphi(10) = 4$ et 7 est premier avec 10, donc $7^4 \equiv 1\ [10]$. Comme $2026 = 4\times506 + 2$, $7^{2026} \equiv 7^2 = 49 \equiv 9\ [10]$ : le dernier chiffre est 9.

## Pièges classiques

- L'ordre d'un élément n'est pas l'ordre du groupe (il le divise).
- Dans $\mathbb Z/n\mathbb Z$ avec $n$ non premier, il y a des diviseurs de zéro : $\bar2\cdot\bar3 = \bar0$ dans $\mathbb Z/6\mathbb Z$.
