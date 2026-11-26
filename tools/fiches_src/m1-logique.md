---
titre: Logique, ensembles, applications
---
## L'essentiel

Ce chapitre fixe le langage de toutes les mathématiques : assertions et quantificateurs, méthodes de raisonnement (récurrence, absurde, analyse-synthèse), ensembles, applications, relations. On l'utilise ensuite dans chaque démonstration.

## Logique

### Connecteurs

- Négation $\neg P$, conjonction $P \wedge Q$ (« et »), disjonction $P \vee Q$ (« ou » inclusif).
- **Implication** $P \Rightarrow Q$ : elle est fausse seulement si $P$ est vraie et $Q$ fausse ; elle équivaut à $\neg P \vee Q$.
- **Équivalence** $P \Leftrightarrow Q$ : $(P \Rightarrow Q) \wedge (Q \Rightarrow P)$.
- **Contraposée** : $P \Rightarrow Q$ équivaut à $\neg Q \Rightarrow \neg P$. La **réciproque** $Q \Rightarrow P$ n'est pas équivalente.
- Lois de De Morgan : $\neg(P \wedge Q) \Leftrightarrow \neg P \vee \neg Q$ et $\neg(P \vee Q) \Leftrightarrow \neg P \wedge \neg Q$.
- Négation d'une implication : $\neg(P \Rightarrow Q) \Leftrightarrow P \wedge \neg Q$.

### Quantificateurs

- $\forall x \in E,\ P(x)$ ; $\exists x \in E,\ P(x)$ ; $\exists!$ pour « il existe un unique ».
- Négation : on échange $\forall$ et $\exists$ et on nie la propriété : $\neg(\forall x,\ P(x)) \Leftrightarrow \exists x,\ \neg P(x)$.
- L'**ordre** des quantificateurs de nature différente compte : $\forall x\ \exists y$ (le $y$ dépend de $x$) n'est pas $\exists y\ \forall x$ (un même $y$ pour tous).

> **Méthode — Nier une définition.** « $f$ est bornée » : $\exists M,\ \forall x,\ |f(x)| \le M$. Négation : $\forall M,\ \exists x,\ |f(x)| > M$.

## Raisonnements

- **Direct** : on suppose $P$, on déduit $Q$.
- **Par contraposée** : on suppose $\neg Q$, on déduit $\neg P$.
- **Par l'absurde** : on suppose le contraire de ce qu'on veut et on aboutit à une contradiction (exemple : $\sqrt2$ est irrationnel).
- **Disjonction de cas**.
- **Analyse-synthèse** : pour trouver toutes les solutions d'un problème, l'analyse suppose une solution et en tire des conditions nécessaires (souvent une forme unique), la synthèse vérifie que ces candidats conviennent. Typique pour « toute fonction s'écrit de façon unique comme somme d'une paire et d'une impaire ».
- **Contre-exemple** : pour réfuter un « pour tout ».

> **Théorème — Récurrence.** Si $P(n_0)$ est vraie et si $P(n) \Rightarrow P(n + 1)$ pour tout $n \ge n_0$, alors $P(n)$ est vraie pour tout $n \ge n_0$.

Variantes : **récurrence double** (initialiser deux rangs, $P(n) \wedge P(n + 1) \Rightarrow P(n + 2)$) et **récurrence forte** (supposer $P(n_0), \dots, P(n)$ pour montrer $P(n + 1)$). Toute partie non vide de $\mathbb N$ a un plus petit élément.

## Ensembles

- Appartenance $x \in A$, inclusion $A \subset B$ ($\forall x,\ x \in A \Rightarrow x \in B$), égalité par double inclusion.
- Opérations : $A \cap B$, $A \cup B$, $A \setminus B$, complémentaire $\bar A$ (dans $E$), produit cartésien $A \times B$, ensemble des parties $\mathcal P(E)$.
- Distributivité : $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ et l'inverse ; De Morgan : $\overline{A \cup B} = \bar A \cap \bar B$, $\overline{A \cap B} = \bar A \cup \bar B$.
- Réunion et intersection d'une famille $(A_i)_{i \in I}$. **Partition** : parties non vides, deux à deux disjointes, de réunion $E$.
- Fonction indicatrice $\mathbb 1_A$ : $\mathbb 1_{A\cap B} = \mathbb 1_A\mathbb 1_B$, $\mathbb 1_{\bar A} = 1 - \mathbb 1_A$.

## Applications

### Vocabulaire

Une application $f : E \to F$ associe à chaque $x$ un unique $f(x)$. Image directe $f(A) = \{f(x),\ x \in A\}$, image réciproque $f^{-1}(B) = \{x \in E,\ f(x) \in B\}$ (définie même si $f$ n'est pas bijective). Restriction, prolongement, composée $g \circ f$ (associative, non commutative).

### Injections, surjections, bijections

[[fig:m1-logique-1]]

> **Définition.** $f$ est **injective** si $f(x) = f(x') \Rightarrow x = x'$ ; **surjective** si tout $y \in F$ a au moins un antécédent ; **bijective** si tout $y$ a exactement un antécédent.

> **Propriété.**
> - La composée de deux injections (surjections, bijections) en est une.
> - Si $g \circ f$ est injective, $f$ est injective ; si $g \circ f$ est surjective, $g$ est surjective.
> - $f$ est bijective si et seulement s'il existe $g$ avec $g \circ f = \mathrm{id}_E$ et $f \circ g = \mathrm{id}_F$ ; alors $g = f^{-1}$, et $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$.

> **Méthode.** Injectivité : partir de $f(x) = f(x')$. Surjectivité : prendre $y$ et **construire** un antécédent. Bijectivité : résoudre $f(x) = y$ et trouver une unique solution, ce qui donne $f^{-1}$.

Pour $E$ et $F$ finis de même cardinal : injective $\Leftrightarrow$ surjective $\Leftrightarrow$ bijective.

## Relations binaires

- **Relation d'équivalence** : réflexive, symétrique, transitive. Classes d'équivalence ; elles forment une partition. Exemple : congruence modulo $n$.
- **Relation d'ordre** : réflexive, antisymétrique, transitive. Ordre **total** si deux éléments sont toujours comparables ($\le$ sur $\mathbb R$) ; sinon partiel (inclusion, divisibilité sur $\mathbb N$).
- Majorant, minorant, plus grand élément, borne supérieure (plus petit des majorants).

## Exemple corrigé

**Énoncé.** Soit $f : \mathbb R \to \mathbb R$, $f(x) = \frac{2x}{1 + x^2}$. Est-elle injective ? surjective ? Déterminer $f(\mathbb R)$.

**Solution.** $f(2) = \frac45 = f(\frac12)$ : $f$ n'est pas injective. Pour $y$ donné, $f(x) = y \Leftrightarrow yx^2 - 2x + y = 0$. Si $y = 0$, $x = 0$. Sinon, il y a une solution réelle si et seulement si le discriminant $4 - 4y^2 \ge 0$, soit $|y| \le 1$. Donc $f(\mathbb R) = [-1, 1]$ et $f$ n'est pas surjective (2 n'a pas d'antécédent). Sa restriction $[-1, 1] \to [-1, 1]$ est bijective (elle est strictement croissante et continue).

## Exemple corrigé (analyse-synthèse)

**Énoncé.** Montrer que toute $f : \mathbb R \to \mathbb R$ s'écrit de manière unique $f = p + i$ avec $p$ paire et $i$ impaire.

**Solution.** *Analyse* : si $f = p + i$, alors $f(-x) = p(x) - i(x)$, d'où $p(x) = \frac{f(x) + f(-x)}{2}$ et $i(x) = \frac{f(x) - f(-x)}{2}$ : unicité. *Synthèse* : ces deux fonctions sont paire et impaire et leur somme vaut $f$ : existence.

## Pièges classiques

- La négation de « $\forall x,\ P(x) \Rightarrow Q(x)$ » est « $\exists x,\ P(x) \wedge \neg Q(x)$ ».
- La notation $f^{-1}(B)$ ne suppose pas que $f$ soit bijective.
- Une récurrence sans initialisation ne prouve rien ; dans une récurrence double, initialiser **deux** rangs.
- Confondre contraposée (équivalente) et réciproque (pas équivalente).
