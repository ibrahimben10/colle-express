---
titre: Logique, ensembles, applications
---
## L'essentiel

Rédiger une preuve demande de maîtriser les connecteurs, les quantificateurs et les types de raisonnement. Les applications sont caractérisées par trois propriétés : injectivité, surjectivité, bijectivité.

## Logique et raisonnements

- Négation : $\lnot(\forall x, P(x)) \equiv \exists x, \lnot P(x)$ ; $\lnot(P \Rightarrow Q) \equiv P \land \lnot Q$.
- **Contraposée** : $P \Rightarrow Q$ équivaut à $\lnot Q \Rightarrow \lnot P$ (la réciproque $Q \Rightarrow P$ n'est pas équivalente).
- Raisonnement par l'**absurde**, par **analyse-synthèse** (existence et unicité), par **récurrence** (simple, double, forte).

> **Méthode — Récurrence.** Énoncer précisément $\mathcal P(n)$, prouver l'initialisation, puis montrer que $\mathcal P(n) \Rightarrow \mathcal P(n+1)$ pour tout $n$.

## Ensembles

Inclusion, union, intersection, complémentaire, produit cartésien, ensemble des parties $\mathcal P(E)$. Lois de De Morgan : $\overline{A \cup B} = \bar A \cap \bar B$.

## Applications

[[fig:m1-logique-1]]

> **Définitions.** $f : E \to F$ est **injective** si $f(x) = f(y) \Rightarrow x = y$ ; **surjective** si tout $y \in F$ a un antécédent ; **bijective** si elle est les deux, c'est-à-dire si tout $y$ a un unique antécédent.

- La composée de deux injections (surjections, bijections) en est une.
- $f$ est bijective si et seulement s'il existe $g$ avec $g\circ f = \mathrm{id}_E$ et $f\circ g = \mathrm{id}_F$ ; alors $g = f^{-1}$.
- Image directe $f(A)$, image réciproque $f^{-1}(B)$ (définie même si $f$ n'est pas bijective).

## Relations

Relation d'**équivalence** (réflexive, symétrique, transitive) : classes d'équivalence, qui partitionnent l'ensemble. Relation d'**ordre** (réflexive, antisymétrique, transitive).

## Exemple corrigé

**Énoncé.** Soit $f : E \to F$ et $g : F \to G$. Montrer que si $g\circ f$ est injective, alors $f$ est injective.

**Solution.** Soient $x, y \in E$ avec $f(x) = f(y)$. Alors $g(f(x)) = g(f(y))$, et comme $g\circ f$ est injective, $x = y$. Donc $f$ est injective ($g$ ne l'est pas forcément).

## Pièges classiques

- L'ordre des quantificateurs compte : $\forall x\,\exists y$ n'est pas $\exists y\,\forall x$.
- $f^{-1}(B)$ (image réciproque) existe toujours ; $f^{-1}$ (réciproque) seulement si $f$ est bijective.
- Pour une récurrence forte, l'hypothèse porte sur tous les rangs $\le n$.
