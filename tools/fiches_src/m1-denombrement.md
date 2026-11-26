---
titre: Dénombrement
---
## L'essentiel

Compter les éléments d'un ensemble fini en le décomposant (union disjointe, produit) ou en le mettant en bijection avec un ensemble connu.

## Principes

- **Union disjointe** : $|A \cup B| = |A| + |B|$ ; en général $|A \cup B| = |A| + |B| - |A \cap B|$.
- **Produit** : $|A\times B| = |A|\times|B|$.
- Si $f : A \to B$ est une bijection, $|A| = |B|$.
- $|\mathcal P(E)| = 2^n$ pour $|E| = n$.

## Formules à connaître

| On compte | Nombre |
|---|---|
| applications de $E$ ($p$ éléments) dans $F$ ($n$ éléments) | $n^p$ |
| $p$-listes d'éléments distincts (arrangements) | $\frac{n!}{(n-p)!}$ |
| permutations de $E$ ($n$ éléments) | $n!$ |
| parties à $p$ éléments (combinaisons) | $\binom np$ |

> **Méthode.** Se demander : l'ordre compte-t-il ? les répétitions sont-elles permises ? Puis choisir la formule ou découper en étapes (principe multiplicatif).

## Exemple corrigé

**Énoncé.** Combien de mains de 5 cartes (jeu de 32) contiennent exactement 2 as ?

**Solution.** On choisit 2 as parmi 4 et 3 autres cartes parmi les 28 qui ne sont pas des as : $\binom42\binom{28}3 = 6\times3276 = 19\,656$.

## Pièges classiques

- Compter deux fois le même objet en imposant un ordre qui n'existe pas (diviser par le nombre d'ordres).
- « Au moins un » : passer souvent par le complémentaire.
