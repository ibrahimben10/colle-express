---
titre: Dimension finie
---
## L'essentiel

En dimension finie, toutes les bases ont le même cardinal, la dimension. Le théorème du rang relie les dimensions du noyau et de l'image, et une application linéaire entre espaces de même dimension est bijective dès qu'elle est injective (ou surjective).

## Bases et dimension

> **Théorème de la base incomplète.** Toute famille libre de $E$ peut être complétée en une base ; de toute famille génératrice, on peut extraire une base.

- Dans $E$ de dimension $n$ : une famille libre a au plus $n$ vecteurs, une famille génératrice au moins $n$ ; une famille de $n$ vecteurs est une base si et seulement si elle est libre, si et seulement si elle est génératrice.
- Sous-espace $F \subset E$ : $\dim F \le \dim E$, avec égalité si et seulement si $F = E$.
- **Formule de Grassmann** : $\dim(F + G) = \dim F + \dim G - \dim(F \cap G)$.

## Rang

> **Théorème du rang.** Pour $u \in \mathcal L(E, F)$ avec $E$ de dimension finie : $\dim E = \dim\ker u + \operatorname{rg}u$.

> **Corollaire.** Si $\dim E = \dim F$ (finie), alors $u$ injective $\Leftrightarrow$ $u$ surjective $\Leftrightarrow$ $u$ bijective.

Le rang d'une famille de vecteurs est la dimension de l'espace qu'elle engendre ; le rang d'une matrice est celui de ses colonnes (égal à celui de ses lignes).

## Exemple corrigé

**Énoncé.** Soit $u : \mathbb R_n[X] \to \mathbb R_n[X]$, $P \mapsto P + P'$. Montrer que $u$ est bijective.

**Solution.** $u$ est linéaire. Si $u(P) = 0$ avec $P \ne 0$, alors $P = -P'$, ce qui est impossible car $\deg P' < \deg P$. Donc $\ker u = \{0\}$ : $u$ est injective, et c'est un endomorphisme d'un espace de dimension finie, donc bijective.

## Pièges classiques

- Le corollaire « injective ⇔ bijective » exige la **même dimension finie** au départ et à l'arrivée.
- Le théorème du rang ne dit pas que $E = \ker u \oplus \operatorname{Im}u$ (faux en général).
