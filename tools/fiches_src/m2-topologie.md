---
titre: Espaces vectoriels normés
---
## L'essentiel

Une norme permet de parler de distance, de limite et de continuité dans un espace vectoriel. En dimension finie, toutes les normes sont équivalentes et les fermés bornés sont compacts.

## Normes

> **Définition.** Une norme vérifie : $\|x\| = 0 \Rightarrow x = 0$ ; $\|\lambda x\| = |\lambda|\|x\|$ ; $\|x + y\| \le \|x\| + \|y\|$.

[[fig:m2-topologie-1]]

Sur $\mathbb K^n$ : $\|x\|_1 = \sum|x_i|$, $\|x\|_2 = \sqrt{\sum|x_i|^2}$, $\|x\|_\infty = \max|x_i|$. Sur $\mathcal C([a, b])$ : $\|f\|_\infty$, $\|f\|_1$, $\|f\|_2$.

Normes **équivalentes** : $\alpha N_1 \le N_2 \le \beta N_1$ ; elles définissent les mêmes suites convergentes.

## Topologie

- **Ouvert** : contient une boule autour de chacun de ses points. **Fermé** : complémentaire d'un ouvert ; caractérisation séquentielle : $F$ fermé si toute suite de $F$ qui converge a sa limite dans $F$.
- Intérieur, adhérence, densité ($A$ dense si $\bar A = E$, par exemple $\mathbb Q$ dans $\mathbb R$, $GL_n$ dans $M_n$).
- $f$ continue : l'image réciproque d'un ouvert (d'un fermé) est un ouvert (un fermé). Utile : $\{x,\ f(x) = 0\}$ est fermé.

## Compacité et dimension finie

> **Théorème.** En dimension finie, toutes les normes sont équivalentes, et les compacts sont les fermés bornés.

> **Théorème.** Une fonction continue sur un compact, à valeurs réelles, est bornée et atteint ses bornes.

Les applications linéaires sont continues en dimension finie ; en général, $u$ linéaire est continue si et seulement s'il existe $k$ avec $\|u(x)\| \le k\|x\|$.

## Exemple corrigé

**Énoncé.** Montrer que $GL_n(\mathbb R)$ est un ouvert de $M_n(\mathbb R)$.

**Solution.** $\det$ est polynomiale en les coefficients, donc continue sur $M_n(\mathbb R)$ (dimension finie). $GL_n(\mathbb R) = \det^{-1}(\mathbb R^*)$ est l'image réciproque de l'ouvert $\mathbb R^*$ par une application continue : c'est un ouvert.

## Pièges classiques

- En dimension infinie, les normes ne sont pas toutes équivalentes, et un fermé borné n'est pas forcément compact.
- Un ensemble peut n'être ni ouvert ni fermé.
