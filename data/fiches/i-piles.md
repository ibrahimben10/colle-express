---
titre: Piles et files
---
## L'essentiel

Une **pile** et une **file** stockent des éléments en attente de traitement. Elles ne diffèrent que par l'ordre de sortie : dernier entré, premier sorti pour la pile ; premier entré, premier sorti pour la file.

[[fig:i-piles-1]]

## Pile (LIFO)

Opérations en temps constant avec une liste Python, le sommet étant la fin de la liste :

```python
p = []
p.append(3)    # empiler
x = p.pop()    # dépiler (erreur si la pile est vide)
vide = (p == [])
```

Usages : pile d'appels récursifs, parcours en profondeur, vérification du parenthésage, évaluation d'expressions.

## File (FIFO)

`L.pop(0)` coûte un temps proportionnel à la longueur : on utilise plutôt `collections.deque`.

```python
from collections import deque
f = deque()
f.append(3)      # enfiler
x = f.popleft()  # défiler, en temps constant
```

Usages : parcours en largeur, simulation de files d'attente.

## Exemple corrigé

**Énoncé.** Vérifier qu'une chaîne formée de `(` et `)` est bien parenthésée.

**Solution.**
```python
def bien_parenthesee(s):
    p = []
    for c in s:
        if c == '(':
            p.append(c)
        elif p == []:
            return False      # fermante sans ouvrante
        else:
            p.pop()
    return p == []            # toutes les ouvrantes sont fermées
```
Complexité linéaire. (Pour un seul type de parenthèse, un compteur suffirait ; la pile se généralise à `()[]{}`.)

## Pièges classiques

- Dépiler une pile vide lève une erreur : tester avant.
- `L.pop(0)` sur une grande liste est lent.
