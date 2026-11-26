---
titre: Dictionnaires et hachage
---
## L'essentiel

Un **dictionnaire** associe des **valeurs** à des **clés**. En Python, `dict` est implémenté par une **table de hachage** : l'accès, l'ajout et le test d'appartenance se font en temps constant en moyenne.

```python
d = {"pomme": 3, "kiwi": 5}
d["poire"] = 2          # ajout ou modification
"kiwi" in d             # True, en O(1) en moyenne
for cle, val in d.items():
    print(cle, val)
d.get("figue", 0)       # 0 si la clé est absente
```

## Table de hachage

[[fig:i-dictionnaires-1]]

Une fonction de hachage $h$ transforme chaque clé en un indice d'alvéole. Si deux clés ont le même indice (**collision**), on les range dans la même alvéole (par exemple dans une liste).

> **Propriété.** Si $h$ répartit bien les clés et si la table est assez grande, chaque alvéole contient peu d'éléments : opérations en $O(1)$ en moyenne (pire cas $O(n)$).

Les clés doivent être **non mutables** (entiers, chaînes, n-uplets) : une liste ne peut pas être une clé.

## Usages typiques

- Compter des occurrences.
- Mémoïser les résultats d'une fonction (programmation dynamique).
- Représenter un graphe par listes d'adjacence.
- Remplacer une recherche linéaire dans une liste.

## Exemple corrigé

**Énoncé.** Compter le nombre d'occurrences de chaque mot d'une liste.

**Solution.**
```python
def occurrences(mots):
    d = {}
    for m in mots:
        d[m] = d.get(m, 0) + 1
    return d
```
Complexité $O(n)$ en moyenne, contre $O(n^2)$ si l'on recompte chaque mot dans la liste.

## Pièges classiques

- Accéder à une clé absente avec `d[k]` lève une `KeyError`.
- Modifier un dictionnaire pendant qu'on le parcourt.
- Utiliser une liste comme clé : la convertir en n-uplet.
