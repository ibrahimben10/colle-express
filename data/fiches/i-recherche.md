---
titre: Recherche et dichotomie
---
## L'essentiel

Chercher un élément dans une liste quelconque demande de tout parcourir ($O(n)$). Si la liste est **triée**, la recherche dichotomique divise l'intervalle de recherche par deux à chaque étape : $O(\log n)$.

## Recherche séquentielle

```python
def appartient(x, L):
    for y in L:
        if y == x:
            return True
    return False
```

## Recherche dichotomique

[[fig:i-recherche-1]]

```python
def dicho(x, T):
    """T trié par ordre croissant. Renvoie un indice de x dans T, ou None."""
    g, d = 0, len(T) - 1
    while g <= d:
        m = (g + d) // 2
        if T[m] == x:
            return m
        elif T[m] < x:
            g = m + 1
        else:
            d = m - 1
    return None
```

> **Propriété.** Invariant : si $x$ est dans $T$, il est dans `T[g:d+1]`. Variant : $d - g$ décroît strictement. Le nombre de tours est au plus $\lfloor\log_2 n\rfloor + 1$.

Pour $n = 10^6$ : au plus 20 comparaisons au lieu d'un million.

## Variante : recherche d'un zéro

La même idée donne la **méthode de dichotomie** pour résoudre $f(x) = 0$ avec $f$ continue changeant de signe sur $[a, b]$ : après $k$ étapes, l'intervalle a pour largeur $(b - a)/2^k$.

## Exemple corrigé

**Énoncé.** Combien d'itérations de dichotomie faut-il pour encadrer $\sqrt2$ à $10^{-6}$ près, en partant de $[1, 2]$ ?

**Solution.** Il faut $\dfrac{1}{2^k} \le 10^{-6}$, soit $k \ge 6\log_210 \approx 19{,}9$ : **20 itérations**.

## Pièges classiques

- Écrire `g < d` au lieu de `g <= d` : on oublie le cas d'un intervalle à un élément.
- Mettre `g = m` au lieu de `g = m + 1` : la boucle peut ne pas terminer.
- La dichotomie n'a de sens que sur une liste **triée**.
