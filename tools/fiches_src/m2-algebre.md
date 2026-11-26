---
titre: Compléments d'algèbre générale
---
## L'essentiel

En deuxième année : groupes monogènes et ordre d'un élément, idéaux et anneaux principaux ($\mathbb Z$, $\mathbb K[X]$), anneaux $\mathbb Z/n\mathbb Z$ et théorème chinois, algèbres. On structure ainsi l'arithmétique et la réduction des endomorphismes.

## Groupes

### Sous-groupe engendré, groupes monogènes

- Sous-groupe engendré par une partie $A$ : le plus petit sous-groupe contenant $A$ (intersection des sous-groupes contenant $A$).
- $\langle a\rangle = \{a^k,\ k \in \mathbb Z\}$. $G$ est **monogène** s'il est engendré par un élément, **cyclique** s'il est de plus fini.
- Les sous-groupes de $(\mathbb Z, +)$ sont les $n\mathbb Z$, $n \in \mathbb N$.

> **Théorème.** Tout groupe monogène infini est isomorphe à $(\mathbb Z, +)$ ; tout groupe cyclique d'ordre $n$ est isomorphe à $(\mathbb Z/n\mathbb Z, +)$ et à $(\mathbb U_n, \times)$. Les générateurs de $\mathbb Z/n\mathbb Z$ sont les $\bar k$ avec $k \wedge n = 1$.

### Ordre d'un élément

$a$ est d'ordre fini $d$ si $\langle a\rangle$ est fini de cardinal $d$ ; alors $d$ est le plus petit entier $\ge 1$ tel que $a^d = e$, et $a^k = e \Leftrightarrow d \mid k$.

> **Théorème de Lagrange (cas commutatif au programme).** Dans un groupe fini $G$, l'ordre de tout élément divise $|G|$ ; donc $a^{|G|} = e$.

## Anneaux et idéaux

> **Définition.** Un idéal $I$ d'un anneau commutatif $A$ est un sous-groupe de $(A, +)$ tel que $a \in A$, $x \in I \Rightarrow ax \in I$. Le noyau d'un morphisme d'anneaux est un idéal ; $aA$ est l'idéal engendré par $a$.

- Somme et intersection d'idéaux sont des idéaux. $I = A$ si et seulement si $1 \in I$.
- Divisibilité dans un anneau intègre : $a \mid b \Leftrightarrow bA \subset aA$.

> **Théorème — Anneaux principaux.** Les idéaux de $\mathbb Z$ sont les $n\mathbb Z$ ; ceux de $\mathbb K[X]$ sont les $P\,\mathbb K[X]$. Ainsi $a\mathbb Z + b\mathbb Z = (a \wedge b)\mathbb Z$ et $a\mathbb Z \cap b\mathbb Z = (a \vee b)\mathbb Z$ ; de même avec les polynômes (PGCD unitaire).

Application : l'ensemble des polynômes annulateurs d'un endomorphisme est un idéal de $\mathbb K[X]$, engendré par le **polynôme minimal**.

## L'anneau $\mathbb Z/n\mathbb Z$

- Éléments $\bar0, \dots, \overline{n-1}$ ; lois induites par celles de $\mathbb Z$.
- $\bar k$ est inversible si et seulement si $k \wedge n = 1$ ; l'inverse se trouve par Bézout.
- $\mathbb Z/n\mathbb Z$ est un corps si et seulement si $n$ est premier ; sinon il a des diviseurs de zéro.
- **Indicatrice d'Euler** $\varphi(n)$ = nombre d'inversibles = nombre d'entiers de $\{1, \dots, n\}$ premiers avec $n$. $\varphi(p) = p - 1$, $\varphi(p^k) = p^k - p^{k-1}$, $\varphi(mn) = \varphi(m)\varphi(n)$ si $m \wedge n = 1$.

> **Théorème d'Euler.** Si $a \wedge n = 1$, alors $a^{\varphi(n)} \equiv 1\ [n]$ (Lagrange dans le groupe des inversibles). Cas $n = p$ premier : petit théorème de Fermat.

> **Théorème chinois.** Si $m \wedge n = 1$, l'application $\bar x \mapsto (\dot x, \ddot x)$ est un isomorphisme d'anneaux $\mathbb Z/mn\mathbb Z \simeq \mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z$. Tout système $x \equiv a\ [m]$, $x \equiv b\ [n]$ a des solutions, uniques modulo $mn$.

Méthode : avec $um + vn = 1$, une solution est $x = bum + avn$.

## Algèbres

Une $\mathbb K$-algèbre est un anneau qui est aussi un $\mathbb K$-espace vectoriel, avec $\lambda(ab) = (\lambda a)b = a(\lambda b)$. Exemples : $\mathbb K[X]$, $M_n(\mathbb K)$, $\mathcal L(E)$, $\mathcal F(X, \mathbb K)$. $P \mapsto P(u)$ est un morphisme d'algèbres.

## Exemple corrigé

**Énoncé.** Trouver le dernier chiffre de $7^{2026}$.

**Solution.** Modulo 10 : $\varphi(10) = 4$ et $7 \wedge 10 = 1$, donc $7^4 \equiv 1\ [10]$. $2026 = 4\times506 + 2$, d'où $7^{2026} \equiv 49 \equiv 9\ [10]$ : le dernier chiffre est 9.

## Exemple corrigé (théorème chinois)

**Énoncé.** Résoudre $x \equiv 2\ [3]$ et $x \equiv 3\ [5]$.

**Solution.** $2\times3 - 5 = 1$ : $u = 2$, $v = -1$. Une solution : $x = 3\cdot2\cdot3 + 2\cdot(-1)\cdot5 = 18 - 10 = 8$. Vérification : $8 \equiv 2\ [3]$ et $8 \equiv 3\ [5]$. Solutions : $x \equiv 8\ [15]$.

## Pièges classiques

- L'ordre d'un élément divise l'ordre du groupe, il ne lui est pas égal en général.
- Dans $\mathbb Z/n\mathbb Z$ avec $n$ non premier : $\bar2\cdot\bar3 = \bar0$ dans $\mathbb Z/6\mathbb Z$.
- Le théorème chinois exige $m \wedge n = 1$.
