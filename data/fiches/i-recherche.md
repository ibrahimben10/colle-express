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

## Autres algorithmes du programme

- **Maximum et deuxième maximum** en un seul parcours : on garde `m1 >= m2` et on les met à jour à chaque élément ; $O(n)$.
- **Recherche d'un mot dans un texte** (algorithme naïf) : pour chaque position $i$ du texte, on compare le motif caractère par caractère ; $O(nm)$ pour un texte de longueur $n$ et un motif de longueur $m$.

```python
def cherche(motif, texte):
    n, m = len(texte), len(motif)
    for i in range(n - m + 1):
        j = 0
        while j < m and texte[i + j] == motif[j]:
            j += 1
        if j == m:
            return i
    return -1
```
- **Deux valeurs les plus proches** dans un tableau : deux boucles imbriquées ($O(n^2)$), ou bien trier puis comparer les voisins ($O(n\log n)$).
- **Version récursive** de la dichotomie : même complexité $O(\log n)$, mais on évite de recopier les tranches (passer `g` et `d` en paramètres).

## Exemple corrigé

**Énoncé.** Combien d'itérations de dichotomie faut-il pour encadrer $\sqrt2$ à $10^{-6}$ près, en partant de $[1, 2]$ ?

**Solution.** Il faut $\dfrac{1}{2^k} \le 10^{-6}$, soit $k \ge 6\log_210 \approx 19{,}9$ : **20 itérations**.

## Pièges classiques

- Écrire `g < d` au lieu de `g <= d` : on oublie le cas d'un intervalle à un élément.
- Mettre `g = m` au lieu de `g = m + 1` : la boucle peut ne pas terminer.
- La dichotomie n'a de sens que sur une liste **triée**.
