---
titre: Dénombrement
---
## L'essentiel

Compter les éléments d'un ensemble fini : cardinal d'une réunion, d'un produit, nombre de listes, d'arrangements, de parties. Le dénombrement est la base des probabilités sur un univers fini.

## Ensembles finis

- $\operatorname{Card}(A \cup B) = \operatorname{Card}A + \operatorname{Card}B - \operatorname{Card}(A \cap B)$ ; pour une réunion **disjointe**, on additionne (principe additif).
- $\operatorname{Card}(\bar A) = \operatorname{Card}E - \operatorname{Card}A$ ; $\operatorname{Card}(A \times B) = \operatorname{Card}A\cdot\operatorname{Card}B$ (principe multiplicatif).
- Si $A \subset B$, $\operatorname{Card}A \le \operatorname{Card}B$, avec égalité si et seulement si $A = B$.
- S'il existe une bijection entre $A$ et $B$, ils ont le même cardinal (principe de bijection) ; une injection $A \to B$ donne $\operatorname{Card}A \le \operatorname{Card}B$ (principe des tiroirs).
- $\operatorname{Card}\mathcal P(E) = 2^n$ ; nombre d'applications de $E$ ($p$ éléments) dans $F$ ($n$ éléments) : $n^p$.

## Listes et combinaisons

| On choisit $p$ éléments parmi $n$… | Nombre |
|---|---|
| ordonnés, avec répétition ($p$-listes) | $n^p$ |
| ordonnés, sans répétition (arrangements) | $\frac{n!}{(n - p)!}$ |
| tous, dans un ordre (permutations) | $n!$ |
| sans ordre, sans répétition (parties) | $\binom np$ |

- Nombre d'injections d'un ensemble à $p$ éléments dans un ensemble à $n$ éléments : $\frac{n!}{(n - p)!}$ ; de bijections entre deux ensembles à $n$ éléments : $n!$.
- **Anagrammes** d'un mot de $n$ lettres où les lettres se répètent $k_1, \dots, k_r$ fois : $\frac{n!}{k_1!\cdots k_r!}$.

## Coefficients binomiaux

$\binom np$ est le nombre de parties à $p$ éléments. Démonstrations combinatoires :

- $\binom np = \binom n{n-p}$ : choisir une partie ou son complémentaire.
- Pascal $\binom np = \binom{n-1}{p-1} + \binom{n-1}p$ : selon que la partie contient un élément fixé ou non.
- $\sum_p\binom np = 2^n$ : on compte toutes les parties.
- **Vandermonde** : $\sum_k\binom ak\binom b{n-k} = \binom{a+b}n$.

## Méthode

1. Décrire précisément un résultat (une liste ? une partie ? avec ou sans ordre ?).
2. Découper en choix successifs (principe multiplicatif) ou en cas disjoints (additif).
3. Utiliser le complémentaire pour « au moins un ».
4. Vérifier qu'on ne compte pas deux fois le même objet (diviser par le nombre d'ordres si on a ordonné par erreur).

## Exemple corrigé

**Énoncé.** On tire simultanément 5 cartes d'un jeu de 32. Combien de mains contiennent exactement 2 as ? au moins un as ?

**Solution.** Le nombre de mains est $\binom{32}5$. Exactement 2 as : choisir 2 as parmi 4 et 3 cartes parmi les 28 autres : $\binom42\binom{28}3 = 6\times3276 = 19656$. Au moins un as : complémentaire des mains sans as : $\binom{32}5 - \binom{28}5 = 201376 - 98280 = 103096$.

## Exemple corrigé (bijection)

**Énoncé.** Combien de chemins sur un quadrillage vont de $(0, 0)$ à $(p, q)$ par pas $(1, 0)$ ou $(0, 1)$ ?

**Solution.** Un chemin est une suite de $p + q$ pas dont $p$ horizontaux ; il est déterminé par les positions des pas horizontaux : $\binom{p+q}p$ chemins.

## Pièges classiques

- Tirages simultanés : pas d'ordre ($\binom np$) ; tirages successifs sans remise : ordre (arrangements).
- « Au moins un » se traite presque toujours par le complémentaire.
- Ne pas additionner des cas qui se recoupent.
