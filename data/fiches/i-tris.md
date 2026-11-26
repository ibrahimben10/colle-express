---
titre: Algorithmes de tri
---
## L'essentiel

Trier une liste permet ensuite des recherches rapides et de nombreux traitements. Les tris simples (insertion, sélection) sont quadratiques ; les tris « diviser pour régner » (fusion, rapide) atteignent $O(n\log n)$.

## Tri par insertion

[[fig:i-tris-1]]

```python
def tri_insertion(T):
    for i in range(1, len(T)):
        x = T[i]
        j = i
        while j > 0 and T[j - 1] > x:
            T[j] = T[j - 1]    # décalage vers la droite
            j = j - 1
        T[j] = x
```

Invariant : au début du tour $i$, `T[0:i]` est trié. Pire cas (liste triée à l'envers) : $O(n^2)$ ; meilleur cas (déjà triée) : $O(n)$. Tri **en place**.

## Tri fusion

[[fig:i-tris-2]]

```python
def fusion(A, B):
    R, i, j = [], 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            R.append(A[i]); i += 1
        else:
            R.append(B[j]); j += 1
    return R + A[i:] + B[j:]

def tri_fusion(T):
    if len(T) <= 1:
        return T
    m = len(T) // 2
    return fusion(tri_fusion(T[:m]), tri_fusion(T[m:]))
```

La fusion de deux listes triées coûte $O(n)$ ; il y a environ $\log_2n$ niveaux : $O(n\log n)$ dans tous les cas.

## Tri rapide

On choisit un **pivot**, on partitionne en « plus petits » et « plus grands », puis on trie récursivement. $O(n\log n)$ en moyenne, $O(n^2)$ dans le pire cas.

## Comparaison

| Tri | Pire cas | En place |
|---|---|---|
| insertion, sélection | $O(n^2)$ | oui |
| fusion | $O(n\log n)$ | non |
| rapide | $O(n^2)$ (moyenne $O(n\log n)$) | oui |

`sorted(L)` et `L.sort()` de Python sont en $O(n\log n)$.

## Exemple corrigé

**Énoncé.** Combien de comparaisons fait le tri par insertion sur `[5, 4, 3, 2, 1]` ?

**Solution.** Chaque nouvel élément est plus petit que tous ceux déjà triés : il est comparé à tous. Total $1 + 2 + 3 + 4 = 10 = \dfrac{n(n-1)}{2}$ : c'est le pire cas.

## Pièges classiques

- `L.sort()` trie en place et renvoie `None` ; `sorted(L)` renvoie une nouvelle liste.
- Oublier le cas de base dans un tri récursif.
