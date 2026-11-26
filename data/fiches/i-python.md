---
titre: Programmer en Python
---
## L'essentiel

Un programme Python manipule des **valeurs** typées (`int`, `float`, `bool`, `str`, `list`, `tuple`, `dict`) désignées par des **noms** (variables). On structure le code en **fonctions**, qu'on documente et qu'on teste.

## Types et opérations

| Type | Exemple | Mutable ? |
|---|---|---|
| entier `int` | `7 // 2` vaut 3, `7 % 2` vaut 1 | non |
| flottant `float` | `7 / 2` vaut 3.5 | non |
| chaîne `str` | `"ab" + "c"`, `len(s)` | non |
| liste `list` | `[1, 2, 3]`, `L.append(4)` | **oui** |
| n-uplet `tuple` | `(1, 2)` | non |
| dictionnaire `dict` | `{"a": 1}` | **oui** |

## Références et mutabilité

[[fig:i-python-1]]

> **Propriété — Aliasing.** L'affectation `b = a` ne copie pas une liste : `a` et `b` désignent le **même objet**. Pour une copie indépendante : `b = a.copy()` ou `b = a[:]` (copie superficielle).

Une fonction qui reçoit une liste peut donc la modifier : c'est un **effet de bord**.

## Indices et tranches

[[fig:i-python-2]]

`L[i:j]` contient les éléments d'indices $i$ à $j - 1$ ; `L[-1]` est le dernier élément. `range(a, b)` parcourt $a, a+1, \dots, b-1$.

## Fonctions

```python
def moyenne(L):
    """Renvoie la moyenne d'une liste non vide de nombres."""
    assert len(L) > 0, "liste vide"
    s = 0
    for x in L:
        s = s + x
    return s / len(L)
```

- La **spécification** (docstring) dit ce que fait la fonction, pas comment.
- `assert` vérifie une **précondition** ; on écrit des tests sur des cas simples et des cas limites.
- `return` termine l'exécution de la fonction ; une fonction sans `return` renvoie `None`.

## Boucles

- `for` : nombre d'itérations connu (parcours d'une liste, d'un `range`).
- `while` : on répète tant qu'une condition est vraie ; il faut s'assurer que la boucle termine.

## Compléments utiles

- **Compréhensions de liste** : `[x**2 for x in range(10) if x % 2 == 0]` ; liste de listes : `[[0] * p for _ in range(n)]` (et non `[[0] * p] * n`).
- **N-uplets et affectation multiple** : `a, b = b, a` échange deux variables ; une fonction peut renvoyer plusieurs valeurs `return q, r`.
- **Chaînes** : non mutables ; `s.split(",")`, `",".join(L)`, `s.strip()`, `s[::-1]` (chaîne renversée).
- **Booléens** : `and` et `or` sont paresseux, `0 < i < len(L) and L[i] > 0` n'évalue `L[i]` que si l'indice est valide.
- **Portée** : une variable affectée dans une fonction est locale ; une fonction ne modifie pas une variable globale entière, mais peut modifier une liste reçue en argument.
- **Entiers** : `//` et `%` donnent quotient et reste (avec des opérandes positifs) ; `**` est la puissance ; les entiers Python ont une taille illimitée.

## Tester son code

```python
def test_indice_max():
    assert indice_max([3]) == 0                # cas limite : un seul élément
    assert indice_max([1, 5, 2]) == 1
    assert indice_max([7, 7, 1]) == 0          # égalités
    assert indice_max([-4, -2, -9]) == 1       # valeurs négatives
```
On partitionne les entrées (cas général, cas limites, égalités) et on écrit les sorties attendues **avant** d'exécuter.

## Exemple corrigé

**Énoncé.** Écrire une fonction qui renvoie l'indice du maximum d'une liste non vide.

**Solution.**
```python
def indice_max(L):
    i_max = 0
    for i in range(1, len(L)):
        if L[i] > L[i_max]:
            i_max = i
    return i_max
```
Invariant : après le tour $i$, `L[i_max]` est le maximum de `L[0:i+1]`. Complexité linéaire : $n - 1$ comparaisons.

## Pièges classiques

- Confondre `=` (affectation) et `==` (comparaison).
- Modifier une liste pendant qu'on la parcourt avec `for`.
- Tester l'égalité de deux flottants avec `==` : comparer plutôt `abs(x - y) < eps`.
- `L * 2` duplique la liste, et `[[0] * 3] * 2` crée deux références vers **la même** sous-liste.
