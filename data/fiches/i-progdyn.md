---
titre: Programmation dynamique
---
## L'essentiel

La programmation dynamique résout un problème en combinant les solutions de **sous-problèmes qui se chevauchent**, en calculant chacun **une seule fois**. Elle s'applique aux problèmes d'optimisation qui ont une sous-structure optimale.

## Méthode

1. Définir les sous-problèmes, par exemple $T[i][c]$.
2. Écrire la **relation de récurrence** et les cas de base.
3. Calculer : soit de haut en bas avec **mémoïsation** (récursif et dictionnaire), soit de bas en haut en remplissant un **tableau**.
4. Reconstruire la solution optimale si on la demande (en remontant le tableau).

## Mémoïsation

[[fig:i-progdyn-1]]

```python
memo = {}
def fib(n):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
```
On passe d'un coût exponentiel à $O(n)$.

## Le sac à dos

[[fig:i-progdyn-2]]

Objets de poids $p_i$ et de valeurs $v_i$, capacité $C$. $T[i][c]$ = meilleure valeur avec les $i$ premiers objets et la capacité $c$ :
$$T[i][c] = \max\big(T[i-1][c],\ T[i-1][c - p_i] + v_i\big)\quad\text{(second terme si } p_i \le c).$$

```python
def sac_a_dos(objets, C):
    n = len(objets)
    T = [[0] * (C + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        p, v = objets[i - 1]
        for c in range(C + 1):
            T[i][c] = T[i - 1][c]
            if p <= c:
                T[i][c] = max(T[i][c], T[i - 1][c - p] + v)
    return T[n][C]
```
Complexité $O(nC)$.

## Exemple corrigé

**Énoncé.** Rendu de monnaie avec les pièces (1, 3, 4) : nombre minimal de pièces pour 6.

**Solution.** $N(0) = 0$ et $N(s) = 1 + \min_{p \le s}N(s - p)$. On calcule $N(1..6) = 1, 2, 1, 1, 2, 2$ ; par exemple $N(6) = 1 + \min(N(5), N(3), N(2)) = 1 + 1 = 2$ (soit $3 + 3$). L'algorithme glouton donnait 3 pièces.

## Pièges classiques

- `[[0] * (C + 1)] * (n + 1)` crée des lignes **partagées** : utiliser une compréhension de liste.
- Bien choisir l'ordre de remplissage : chaque case ne doit dépendre que de cases déjà calculées.
