---
titre: Structures algébriques usuelles
---
## L'essentiel

Groupes, anneaux et corps donnent un cadre commun à des objets variés ($\mathbb Z$, $\mathbb R$, matrices, permutations, polynômes). On étudie les sous-structures et les morphismes.

## Groupes

> **Définition.** $(G, \ast)$ est un groupe si la loi est associative, admet un neutre $e$, et si tout élément a un symétrique. Il est abélien si la loi est commutative.

- **Sous-groupe** $H$ : non vide, et $x, y \in H \Rightarrow x\ast y^{-1} \in H$.
- **Morphisme** $f(x\ast y) = f(x)\star f(y)$ ; son **noyau** $\ker f = f^{-1}(\{e'\})$ est un sous-groupe, et $f$ est injective si et seulement si $\ker f = \{e\}$.
- Exemples : $(\mathbb Z, +)$, $(\mathbb U, \times)$, $(\mathbb U_n, \times)$, $(GL_n(\mathbb K), \times)$, $(S_n, \circ)$.

## Anneaux et corps

> **Définition.** $(A, +, \times)$ est un anneau si $(A, +)$ est un groupe abélien, $\times$ est associative, distributive sur $+$, avec un neutre $1$. Un **corps** est un anneau commutatif où tout élément non nul est inversible.

- Anneau **intègre** : $ab = 0 \Rightarrow a = 0$ ou $b = 0$ ($\mathbb Z$, $\mathbb K[X]$ le sont ; $M_n(\mathbb K)$ non pour $n \ge 2$).
- Groupe des inversibles $A^\times$ : $\mathbb Z^\times = \{\pm1\}$, $M_n(\mathbb K)^\times = GL_n(\mathbb K)$.
- Formule du binôme et $a^n - b^n = (a - b)\sum a^kb^{n-1-k}$ valables si $a$ et $b$ **commutent**.

## Exemple corrigé

**Énoncé.** Montrer que $\mathbb U_n = \{z \in \mathbb C,\ z^n = 1\}$ est un sous-groupe de $(\mathbb C^*, \times)$.

**Solution.** $1 \in \mathbb U_n$. Si $z, w \in \mathbb U_n$ : $(zw^{-1})^n = z^n(w^n)^{-1} = 1$, donc $zw^{-1} \in \mathbb U_n$. C'est un sous-groupe (c'est aussi le noyau du morphisme $z \mapsto z^n$).

## Pièges classiques

- Vérifier que la loi est **interne** avant tout.
- Dans un anneau non commutatif, $(a + b)^2 \ne a^2 + 2ab + b^2$ en général.
- Un anneau non intègre peut avoir des diviseurs de zéro : ne pas simplifier sans précaution.
