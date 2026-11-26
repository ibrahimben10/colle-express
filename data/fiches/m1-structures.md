---
titre: Structures algébriques usuelles
---
## L'essentiel

Groupes, anneaux, corps : des ensembles munis de lois qui vérifient des règles précises. Reconnaître une structure permet d'utiliser d'un coup tous les résultats généraux (inverse, puissances, morphismes, noyau).

## Lois de composition interne

Une loi $*$ sur $E$ associe à $(x, y)$ un élément $x * y$ de $E$. Elle peut être associative, commutative, avoir un élément **neutre** $e$ (unique s'il existe) ; $x$ est **symétrisable** s'il existe $x'$ avec $x * x' = x' * x = e$ (unique si $*$ est associative). Symétrique d'un produit : $(x * y)^{-1} = y^{-1} * x^{-1}$.

Une partie $A$ est **stable** si $x, y \in A \Rightarrow x * y \in A$.

## Groupes

> **Définition.** $(G, *)$ est un groupe si la loi est associative, admet un neutre, et si tout élément est symétrisable. Abélien si la loi est commutative.

Exemples : $(\mathbb Z, +)$, $(\mathbb R^*, \times)$, $(\mathbb U, \times)$ (complexes de module 1), $(\mathbb U_n, \times)$, $(S_n, \circ)$ (permutations), $(GL_n(\mathbb K), \times)$, l'ensemble des bijections d'un ensemble.

Règles de calcul : simplification ($ax = ay \Rightarrow x = y$), puissances $x^n$ pour $n \in \mathbb Z$ avec $x^{m+n} = x^mx^n$ ; $(xy)^n = x^ny^n$ seulement si $x$ et $y$ commutent.

### Sous-groupes

> **Propriété — Caractérisation.** $H \subset G$ est un sous-groupe si et seulement si $H$ contient le neutre et, pour tous $x, y \in H$, $xy^{-1} \in H$.

L'intersection de sous-groupes est un sous-groupe (la réunion non, en général). Les sous-groupes de $(\mathbb Z, +)$ sont les $n\mathbb Z$.

### Morphismes de groupes

$f : G \to G'$ est un morphisme si $f(xy) = f(x)f(y)$. Alors $f(e) = e'$ et $f(x^{-1}) = f(x)^{-1}$.

> **Propriété.** $\ker f = f^{-1}(\{e'\})$ et $\operatorname{Im}f$ sont des sous-groupes ; $f$ est injectif si et seulement si $\ker f = \{e\}$.

Exemples : $\exp : (\mathbb R, +) \to (\mathbb R_+^*, \times)$ (isomorphisme), $\det : GL_n \to \mathbb K^*$, $\theta \mapsto e^{i\theta}$ de $(\mathbb R, +)$ dans $(\mathbb U, \times)$ (noyau $2\pi\mathbb Z$), signature $S_n \to \{\pm1\}$.

## Anneaux et corps

> **Définition.** $(A, +, \times)$ est un anneau si $(A, +)$ est un groupe abélien, si $\times$ est associative, a un neutre $1_A$, et est distributive sur $+$. Un **corps** est un anneau commutatif non nul où tout élément non nul est inversible.

Exemples : $\mathbb Z$, $\mathbb K[X]$, $M_n(\mathbb K)$ (non commutatif), $\mathcal F(\mathbb R, \mathbb R)$ ; corps : $\mathbb Q$, $\mathbb R$, $\mathbb C$.

- $0 \times a = 0$ ; $(-a)b = -(ab)$.
- **Binôme de Newton** et factorisation de $a^n - b^n$ pour $a$, $b$ qui **commutent**.
- **Diviseurs de zéro** : $ab = 0$ avec $a, b \ne 0$ (exemple : matrices). Un anneau commutatif sans diviseur de zéro est **intègre** ($\mathbb Z$, $\mathbb K[X]$).
- Groupe des inversibles $A^\times$ : $\mathbb Z^\times = \{\pm1\}$, $M_n(\mathbb K)^\times = GL_n(\mathbb K)$.
- Sous-anneau : contient $1_A$, stable par différence et produit. Morphisme d'anneaux : conserve $+$, $\times$ et $1$.

## Exemple corrigé

**Énoncé.** Montrer que $\mathbb U_n = \{z \in \mathbb C,\ z^n = 1\}$ est un sous-groupe de $(\mathbb C^*, \times)$.

**Solution.** $1 \in \mathbb U_n$. Si $z, w \in \mathbb U_n$, alors $w \ne 0$ et $(zw^{-1})^n = \frac{z^n}{w^n} = 1$, donc $zw^{-1} \in \mathbb U_n$. C'est un sous-groupe (on peut aussi le voir comme noyau du morphisme $z \mapsto z^n$).

## Exemple corrigé (anneau)

**Énoncé.** Dans un anneau, $a$ est **nilpotent** si $a^p = 0$ pour un $p$. Montrer que $1 - a$ est alors inversible.

**Solution.** $1$ et $a$ commutent : $(1 - a)(1 + a + \dots + a^{p-1}) = 1 - a^p = 1$, et de même dans l'autre sens. Donc $(1 - a)^{-1} = \sum_{k=0}^{p-1}a^k$.

## Pièges classiques

- Pour un sous-groupe, ne pas oublier qu'il est **non vide** (contient le neutre).
- Dans un anneau non commutatif, $(a + b)^2 = a^2 + ab + ba + b^2$.
- Un anneau peut avoir des diviseurs de zéro : $AB = 0$ n'implique pas $A = 0$ ou $B = 0$.
