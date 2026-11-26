---
titre: Récursivité
---
## L'essentiel

Une fonction **récursive** s'appelle elle-même sur une instance plus petite du problème. Elle doit avoir un **cas de base** atteint au bout d'un nombre fini d'appels.

```python
def fact(n):
    if n == 0:          # cas de base
        return 1
    return n * fact(n - 1)
```

## Pile d'appels

[[fig:i-recursivite-2]]

Chaque appel en attente occupe de la place dans la **pile d'appels**. Python limite sa profondeur (environ 1000 par défaut) : une récursion trop profonde provoque une `RecursionError`.

## Terminaison et correction

> **Méthode — Récurrence.** On prouve la terminaison avec une quantité entière qui décroît strictement à chaque appel (ici $n$), et la correction par récurrence sur cette quantité.

## Complexité

On écrit une relation de récurrence sur le coût $C(n)$ :

| Relation | Exemple | Complexité |
|---|---|---|
| $C(n) = C(n-1) + O(1)$ | factorielle | $O(n)$ |
| $C(n) = C(n/2) + O(1)$ | dichotomie récursive, exponentiation rapide | $O(\log n)$ |
| $C(n) = 2C(n/2) + O(n)$ | tri fusion | $O(n\log n)$ |
| $C(n) = C(n-1) + C(n-2) + O(1)$ | Fibonacci naïf | exponentielle |

## Appels redondants

[[fig:i-recursivite-1]]

La version naïve de Fibonacci recalcule de nombreuses fois les mêmes valeurs. Remède : la **mémoïsation** (voir programmation dynamique).

## Exemple corrigé

**Énoncé.** Écrire l'exponentiation rapide $x^n$ et donner sa complexité.

**Solution.**
```python
def puissance(x, n):
    if n == 0:
        return 1
    y = puissance(x, n // 2)
    return y * y if n % 2 == 0 else x * y * y
```
On utilise $x^n = (x^{n/2})^2$ (ou $x\,(x^{\lfloor n/2\rfloor})^2$ si $n$ est impair) : $n$ est divisé par 2 à chaque appel, donc $O(\log n)$ multiplications au lieu de $n$.

## Pièges classiques

- Oublier le cas de base, ou un cas de base jamais atteint (par exemple pour $n$ négatif).
- Écrire `puissance(x, n // 2) * puissance(x, n // 2)` : deux appels au lieu d'un, on perd tout le gain.
