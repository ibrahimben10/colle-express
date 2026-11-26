---
titre: Limites et continuité
---
## L'essentiel

La continuité traduit l'absence de « saut ». Sur un intervalle, elle donne le théorème des valeurs intermédiaires ; sur un segment, le théorème des bornes atteintes. Ces deux résultats servent constamment à prouver l'existence de solutions.

## Limites

> **Définition.** $f$ (définie au voisinage de $a$) tend vers $\ell$ en $a$ si : $\forall\varepsilon > 0,\ \exists\eta > 0,\ \forall x \in D,\ |x - a| \le \eta \Rightarrow |f(x) - \ell| \le \varepsilon$. On adapte aux cas infinis (voisinages $[A, +\infty[$).

- Unicité de la limite ; limite à gauche, à droite.
- Opérations sur les limites et composition : si $f \to b$ en $a$ et $g \to \ell$ en $b$, alors $g \circ f \to \ell$ en $a$.
- Passage à la limite dans les inégalités larges ; théorème d'encadrement.

> **Théorème — Caractérisation séquentielle.** $f \to \ell$ en $a$ si et seulement si, pour toute suite $(x_n)$ de $D$ qui tend vers $a$, $f(x_n) \to \ell$.

Usage : pour montrer qu'une fonction **n'a pas** de limite, trouver deux suites $x_n \to a$ et $y_n \to a$ avec $f(x_n)$ et $f(y_n)$ de limites différentes (exemple : $\sin\frac1x$ en 0).

> **Théorème — Limite monotone.** Une fonction monotone sur $]a, b[$ admet en tout point des limites à gauche et à droite finies ; en $b$, elle a une limite (finie si elle est bornée).

## Continuité

$f$ est continue en $a$ si $f(x) \to f(a)$. Elle est continue sur $I$ si elle l'est en tout point. Sommes, produits, quotients, composées de fonctions continues sont continues.

**Prolongement par continuité** : si $f$ est définie sur $I \setminus \{a\}$ et a une limite finie $\ell$ en $a$, on la prolonge en posant $f(a) = \ell$ (exemple : $\frac{\sin x}{x}$ en 0).

## Théorèmes fondamentaux

[[fig:m1-continuite-1]]

> **Théorème des valeurs intermédiaires.** Si $f$ est continue sur un intervalle $I$ et si $a, b \in I$, toute valeur comprise entre $f(a)$ et $f(b)$ est atteinte entre $a$ et $b$. Autrement dit, l'image d'un intervalle par une fonction continue est un intervalle.

Corollaire : si $f$ est continue sur $[a, b]$ et $f(a)f(b) \le 0$, elle s'annule sur $[a, b]$. Base de la **dichotomie**.

> **Théorème des bornes atteintes.** Une fonction continue sur un **segment** $[a, b]$ est bornée et atteint ses bornes : $f([a, b]) = [m, M]$.

> **Théorème de la bijection.** Une fonction continue et strictement monotone sur un intervalle $I$ est une bijection de $I$ sur l'intervalle $f(I)$, et sa réciproque est continue et de même monotonie.

Réciproquement, une fonction continue et injective sur un intervalle est strictement monotone.

### Continuité uniforme et lipschitzianité

- $f$ est **$k$-lipschitzienne** si $|f(x) - f(y)| \le k|x - y|$ ; elle est alors continue.
- $f$ est **uniformément continue** si $\forall\varepsilon,\ \exists\eta,\ \forall x, y,\ |x - y| \le \eta \Rightarrow |f(x) - f(y)| \le \varepsilon$ (le même $\eta$ pour tous les points).

> **Théorème de Heine.** Une fonction continue sur un segment y est uniformément continue.

## Fonctions à valeurs complexes

$f$ est continue si et seulement si $\operatorname{Re}f$ et $\operatorname{Im}f$ le sont. Le théorème des valeurs intermédiaires ne s'applique **pas** aux fonctions complexes.

## Exemple corrigé

**Énoncé.** Montrer que l'équation $x^5 + x - 1 = 0$ a une unique solution réelle, et qu'elle est dans $]0, 1[$.

**Solution.** $f(x) = x^5 + x - 1$ est continue et strictement croissante sur $\mathbb R$ (somme de fonctions strictement croissantes). $f(0) = -1 < 0$ et $f(1) = 1 > 0$. Par le théorème des valeurs intermédiaires, $f$ s'annule sur $]0, 1[$ ; par stricte monotonie, ce zéro est unique sur $\mathbb R$.

## Exemple corrigé (point fixe)

**Énoncé.** $f : [0, 1] \to [0, 1]$ continue. Montrer que $f$ a un point fixe.

**Solution.** $g(x) = f(x) - x$ est continue, $g(0) = f(0) \ge 0$ et $g(1) = f(1) - 1 \le 0$. Par le TVI, $g$ s'annule : il existe $c$ avec $f(c) = c$.

## Pièges classiques

- Le TVI exige un **intervalle** et la **continuité** : $\frac1x$ sur $[-1, 1] \setminus \{0\}$ change de signe sans s'annuler.
- Le théorème des bornes atteintes exige un **segment** (fermé et borné) : $\frac1x$ sur $]0, 1]$ n'est pas bornée.
- La continuité en chaque point ne suffit pas pour la continuité uniforme sur un intervalle non borné ($x^2$ sur $\mathbb R$).
