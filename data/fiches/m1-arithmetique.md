---
titre: Arithmétique dans ℤ
---
## L'essentiel

Divisibilité, division euclidienne, PGCD et algorithme d'Euclide, théorèmes de Bézout et de Gauss, nombres premiers et décomposition, congruences. Tout repose sur la division euclidienne.

## Divisibilité et division euclidienne

$a \mid b$ s'il existe $k \in \mathbb Z$ avec $b = ka$. La divisibilité est réflexive, transitive ; si $a \mid b$ et $a \mid c$, alors $a \mid ub + vc$.

> **Théorème — Division euclidienne.** Pour $a \in \mathbb Z$ et $b \in \mathbb N^*$, il existe un unique couple $(q, r)$ avec $a = bq + r$ et $0 \le r < b$.

## PGCD et PPCM

$a \wedge b$ est le plus grand diviseur commun (pour $(a, b) \ne (0, 0)$) ; $a \vee b$ le plus petit multiple commun positif. Les diviseurs communs à $a$ et $b$ sont exactement les diviseurs de $a \wedge b$.

> **Méthode — Algorithme d'Euclide.** $a \wedge b = b \wedge r$ où $r$ est le reste de $a$ par $b$. On itère jusqu'à un reste nul : le dernier reste non nul est le PGCD. En remontant les calculs (algorithme étendu), on obtient $u$, $v$ avec $au + bv = a \wedge b$.

Propriétés : $(ka) \wedge (kb) = |k|(a \wedge b)$ ; $(a \wedge b)(a \vee b) = |ab|$.

> **Théorème de Bézout.** $a$ et $b$ sont premiers entre eux ($a \wedge b = 1$) si et seulement s'il existe $u, v \in \mathbb Z$ tels que $au + bv = 1$.

> **Théorème de Gauss.** Si $a \mid bc$ et $a \wedge b = 1$, alors $a \mid c$.

Conséquences : si $a \mid c$, $b \mid c$ et $a \wedge b = 1$, alors $ab \mid c$. Tout rationnel s'écrit de manière unique sous forme irréductible $\frac pq$ ($q > 0$, $p \wedge q = 1$).

PGCD de plusieurs entiers, entiers premiers entre eux dans leur ensemble (Bézout généralisé), à ne pas confondre avec « deux à deux premiers entre eux ».

### Équations diophantiennes $ax + by = c$

Solvable si et seulement si $d = a \wedge b$ divise $c$. On divise par $d$, on trouve une solution particulière $(x_0, y_0)$ par Euclide, et les solutions sont $x = x_0 + k\frac bd$, $y = y_0 - k\frac ad$, $k \in \mathbb Z$ (par Gauss).

## Nombres premiers

$p \ge 2$ est premier si ses seuls diviseurs positifs sont 1 et $p$. Tout entier $n \ge 2$ a un diviseur premier ; si $n$ n'est pas premier, il a un diviseur premier $\le \sqrt n$ (crible d'Ératosthène).

> **Théorème.** L'ensemble des nombres premiers est infini.

> **Théorème — Décomposition.** Tout entier $n \ge 2$ s'écrit de manière unique (à l'ordre près) $n = p_1^{\alpha_1}\cdots p_r^{\alpha_r}$ avec des $p_i$ premiers distincts et $\alpha_i \ge 1$.

Valuation $p$-adique $v_p(n)$ : $v_p(ab) = v_p(a) + v_p(b)$ ; $a \mid b \Leftrightarrow v_p(a) \le v_p(b)$ pour tout $p$ ; $v_p(a \wedge b) = \min$, $v_p(a \vee b) = \max$. Lemme d'Euclide : si $p$ premier divise $ab$, il divise $a$ ou $b$.

## Congruences

$a \equiv b\ [n]$ si $n \mid a - b$. C'est une relation d'équivalence, compatible avec $+$ et $\times$ (donc avec les puissances). On ne simplifie par $c$ que si $c \wedge n = 1$.

> **Théorème — Petit théorème de Fermat.** Si $p$ est premier, $a^p \equiv a\ [p]$ ; et si $p \nmid a$, $a^{p-1} \equiv 1\ [p]$.

Inverse modulo $n$ : $a$ est inversible modulo $n$ si et seulement si $a \wedge n = 1$ ; l'inverse est le $u$ d'une relation de Bézout $au + nv = 1$.

## Exemple corrigé

**Énoncé.** Résoudre $35x + 21y = 14$ dans $\mathbb Z^2$.

**Solution.** $35 \wedge 21 = 7$ divise 14 ; on se ramène à $5x + 3y = 2$. Solution particulière : $5\cdot1 + 3\cdot(-1) = 2$, donc $(1, -1)$. Si $(x, y)$ est solution, $5(x - 1) = -3(y + 1)$ ; par Gauss ($5 \wedge 3 = 1$), $3 \mid x - 1$ : $x = 1 + 3k$, puis $y = -1 - 5k$. Réciproquement ces couples conviennent : $S = \{(1 + 3k, -1 - 5k),\ k \in \mathbb Z\}$.

## Exemple corrigé (Fermat)

**Énoncé.** Montrer que $n^7 - n$ est divisible par 7 pour tout $n$, et calculer le reste de $3^{100}$ modulo 7.

**Solution.** Par Fermat, $n^7 \equiv n\ [7]$. Puis $3^6 \equiv 1\ [7]$ et $100 = 6\times16 + 4$, donc $3^{100} \equiv 3^4 = 81 \equiv 4\ [7]$.

## Pièges classiques

- Gauss exige $a \wedge b = 1$ ; sinon, $6 \mid 4\times3$ sans que $6 \mid 3$.
- Ne pas diviser une congruence par un entier non premier avec le module.
- Dans la résolution diophantienne, ne pas oublier la réciproque.
