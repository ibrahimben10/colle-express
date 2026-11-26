---
titre: Calculs algébriques
---
## L'essentiel

Manipuler les sommes et les produits avec les symboles $\sum$ et $\prod$ : changements d'indice, télescopage, sommes usuelles, coefficients binomiaux.

## Sommes usuelles

| Somme | Valeur |
|---|---|
| $\sum_{k=1}^nk$ | $\frac{n(n+1)}{2}$ |
| $\sum_{k=1}^nk^2$ | $\frac{n(n+1)(2n+1)}{6}$ |
| $\sum_{k=1}^nk^3$ | $\left(\frac{n(n+1)}{2}\right)^2$ |
| $\sum_{k=0}^nq^k$ ($q \ne 1$) | $\frac{1 - q^{n+1}}{1 - q}$ |

## Techniques

- **Changement d'indice** : $\sum_{k=1}^nu_{k-1} = \sum_{j=0}^{n-1}u_j$.
- **Télescopage** : $\sum_{k=0}^{n-1}(u_{k+1} - u_k) = u_n - u_0$. Exemple : $\frac{1}{k(k+1)} = \frac1k - \frac{1}{k+1}$.
- **Sommes doubles** : $\sum_{i,j}a_ib_j = \left(\sum_ia_i\right)\left(\sum_jb_j\right)$ ; interversion $\sum_{1\le i\le j\le n} = \sum_{j=1}^n\sum_{i=1}^j$.
- Factorisation : $a^n - b^n = (a - b)\sum_{k=0}^{n-1}a^kb^{n-1-k}$.

## Coefficients binomiaux

$\binom nk = \frac{n!}{k!(n-k)!}$ : symétrie $\binom nk = \binom n{n-k}$, **formule de Pascal** $\binom nk + \binom n{k+1} = \binom{n+1}{k+1}$.

> **Formule du binôme de Newton.** Pour $a, b$ qui commutent : $(a + b)^n = \sum_{k=0}^n\binom nka^kb^{n-k}$. En particulier $\sum_k\binom nk = 2^n$.

## Systèmes linéaires

Méthode du pivot de Gauss : opérations élémentaires sur les lignes, système échelonné, inconnues principales et paramètres.

## Exemple corrigé

**Énoncé.** Calculer $S_n = \sum_{k=1}^n\frac{1}{k(k+1)}$.

**Solution.** $\frac{1}{k(k+1)} = \frac1k - \frac{1}{k+1}$, donc par télescopage $S_n = 1 - \frac{1}{n+1} = \frac{n}{n+1}$, qui tend vers 1.

## Pièges classiques

- $\sum_{k=0}^n1 = n + 1$, pas $n$.
- Le binôme exige que $a$ et $b$ commutent (attention aux matrices).
- Bien vérifier les bornes après un changement d'indice.
