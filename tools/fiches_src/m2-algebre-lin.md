---
titre: Compléments d'algèbre linéaire
---
## L'essentiel

Sommes directes de plusieurs sous-espaces, matrices par blocs, et surtout polynômes d'endomorphismes : ils préparent la réduction.

## Somme directe de plusieurs sous-espaces

$F_1 + \dots + F_p$ est directe si toute décomposition $x = x_1 + \dots + x_p$ est unique, c'est-à-dire si $x_1 + \dots + x_p = 0 \Rightarrow$ tous les $x_i$ sont nuls. En dimension finie : directe $\Leftrightarrow \dim\sum F_i = \sum\dim F_i$.

Une base **adaptée** à $E = \bigoplus F_i$ (concaténation de bases des $F_i$) donne une matrice diagonale par blocs pour un endomorphisme qui laisse chaque $F_i$ stable.

## Sous-espaces stables

Si $F$ est stable par $u$ ($u(F) \subset F$), la matrice de $u$ dans une base adaptée est triangulaire par blocs. Si $u$ et $v$ **commutent**, $\ker v$ et $\operatorname{Im}v$ sont stables par $u$.

## Polynômes d'endomorphismes

Pour $P = \sum a_kX^k$, $P(u) = \sum a_ku^k$ ; $P \mapsto P(u)$ est un morphisme d'algèbres : $(PQ)(u) = P(u)\circ Q(u)$.

- Polynôme **annulateur** : $P(u) = 0$. En dimension finie, il en existe toujours (non nul).
- **Polynôme minimal** $\pi_u$ : unitaire, de plus petit degré, il engendre l'idéal des annulateurs.

> **Lemme des noyaux.** Si $P_1, \dots, P_k$ sont deux à deux premiers entre eux : $\ker(P_1\cdots P_k)(u) = \bigoplus_i\ker P_i(u)$.

## Exemple corrigé

**Énoncé.** Soit $p$ un endomorphisme tel que $p^2 = p$. Retrouver $E = \ker p \oplus \ker(p - \mathrm{id})$.

**Solution.** $X^2 - X = X(X - 1)$ annule $p$, et $X$, $X - 1$ sont premiers entre eux. Par le lemme des noyaux, $E = \ker(p^2 - p) = \ker p \oplus \ker(p - \mathrm{id})$ : on retrouve que $p$ est le projecteur sur $\operatorname{Im}p = \ker(p - \mathrm{id})$ parallèlement à $\ker p$.

## Pièges classiques

- Pour plus de deux sous-espaces, les intersections deux à deux nulles ne suffisent pas.
- $P(u)$ et $Q(u)$ commutent toujours, mais $u$ et $v$ quelconques non.
