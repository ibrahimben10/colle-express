---
titre: Complexité, terminaison, correction
---
## L'essentiel

Analyser un algorithme, c'est prouver qu'il **termine**, qu'il est **correct** (il renvoie ce que dit sa spécification) et estimer sa **complexité** (son coût en fonction de la taille $n$ de l'entrée).

## Terminaison

> **Méthode — Variant de boucle.** Exhiber une quantité entière positive qui décroît strictement à chaque tour de boucle `while` : la boucle s'arrête.

Exemple : dans l'algorithme d'Euclide, le second argument est un entier positif qui décroît strictement.

## Correction

> **Méthode — Invariant de boucle.** Une propriété vraie avant la boucle et conservée par chaque itération. À la sortie, combinée à la condition d'arrêt, elle donne le résultat.

Exemple : pour le calcul de la somme d'une liste, « `s` contient la somme des $i$ premiers éléments ».

## Complexité

On compte les opérations élémentaires dans le **pire cas** (parfois en moyenne), et on donne un ordre de grandeur $O(\cdot)$.

[[fig:i-complexite-1]]

| Complexité | Exemple | $n = 10^6$ |
|---|---|---|
| $O(\log n)$ | recherche dichotomique | 20 opérations |
| $O(n)$ | parcours d'une liste | $10^6$ |
| $O(n\log n)$ | tri fusion | $2\cdot10^7$ |
| $O(n^2)$ | tri par insertion, deux boucles imbriquées | $10^{12}$ (trop lent) |
| $O(2^n)$ | énumérer toutes les parties | impossible |

Ordre de grandeur : un ordinateur fait environ $10^8$ à $10^9$ opérations simples par seconde (beaucoup moins en Python).

## Exemple corrigé

**Énoncé.** Complexité de :
```python
def doublons(L):
    n = len(L)
    for i in range(n):
        for j in range(i + 1, n):
            if L[i] == L[j]:
                return True
    return False
```

**Solution.** Dans le pire cas (pas de doublon), le nombre de comparaisons est $\sum_{i=0}^{n-1}(n - 1 - i) = \dfrac{n(n-1)}{2}$ : complexité **quadratique** $O(n^2)$. En triant d'abord la liste ($O(n\log n)$), puis en comparant les voisins ($O(n)$), on passe à $O(n\log n)$.

## Pièges classiques

- Oublier le coût caché des opérations : `x in L` et `L.pop(0)` sont linéaires, `x in d` (dictionnaire) est en temps constant en moyenne.
- Un invariant doit être vrai **avant** la première itération.
