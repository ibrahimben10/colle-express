---
titre: Systèmes linéaires : pivot de Gauss
---
## L'essentiel

Résoudre $AX = B$ (avec $A$ inversible de taille $n$) par la **méthode du pivot de Gauss** : on transforme le système en un système **triangulaire** par opérations élémentaires sur les lignes, puis on le résout par **remontée**.

[[fig:i-systemes-1]]

## Opérations élémentaires

Elles ne changent pas les solutions :
- échanger deux lignes $L_i \leftrightarrow L_j$ ;
- multiplier une ligne par un réel non nul ;
- ajouter à une ligne un multiple d'une autre : $L_i \leftarrow L_i - \lambda L_j$.

## Algorithme

```python
def gauss(A, B):
    """Résout A X = B. A : liste de listes n × n inversible, B : liste. Modifie des copies."""
    n = len(A)
    M = [A[i][:] + [B[i]] for i in range(n)]       # matrice augmentée
    for j in range(n):
        # pivot partiel : ligne de plus grand |coefficient| dans la colonne j
        p = max(range(j, n), key=lambda i: abs(M[i][j]))
        M[j], M[p] = M[p], M[j]
        for i in range(j + 1, n):
            c = M[i][j] / M[j][j]
            for k in range(j, n + 1):
                M[i][k] -= c * M[j][k]
    X = [0] * n
    for i in range(n - 1, -1, -1):                  # remontée
        s = sum(M[i][k] * X[k] for k in range(i + 1, n))
        X[i] = (M[i][n] - s) / M[i][i]
    return X
```

> **Propriété.** Coût : environ $\dfrac{2n^3}{3}$ opérations, soit $O(n^3)$ ; la remontée coûte $O(n^2)$.

Le **pivot partiel** (choisir le plus grand pivot en valeur absolue) évite de diviser par un nombre nul ou très petit, ce qui amplifierait les erreurs d'arrondi.

## Avec NumPy

```python
import numpy as np
X = np.linalg.solve(A, B)        # bien plus rapide et plus sûr
```
Inverser la matrice (`np.linalg.inv(A) @ B`) est plus coûteux et moins précis que `solve`.

## Exemple corrigé

**Énoncé.** Résoudre $\begin{cases}x + y + z = 6\\ 2x + 3y + z = 11\\ x - y + 2z = 5\end{cases}$.

**Solution.** $L_2 \leftarrow L_2 - 2L_1$ : $y - z = -1$. $L_3 \leftarrow L_3 - L_1$ : $-2y + z = -1$. $L_3 \leftarrow L_3 + 2L_2$ : $-z = -3$. Remontée : $z = 3$, $y = 2$, $x = 1$.

## Pièges classiques

- Oublier d'appliquer les opérations au second membre.
- Tester un pivot avec `== 0` : avec des flottants, un pivot « presque nul » pose déjà problème.
- Modifier la matrice passée en argument sans le vouloir : travailler sur une copie.
