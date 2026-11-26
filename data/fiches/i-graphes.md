---
titre: Graphes : représentations et parcours
---
## L'essentiel

Un graphe $G = (S, A)$ est formé de **sommets** et d'**arêtes** (ou d'**arcs** s'il est orienté). Il modélise des réseaux : routes, relations, dépendances, états d'un jeu.

## Vocabulaire

Voisins, degré, chemin, cycle, graphe connexe, graphe pondéré (poids sur les arêtes). Pour un graphe non orienté : $\sum_s\deg(s) = 2|A|$.

## Représentations

[[fig:i-graphes-1]]

On note $n$ le nombre de sommets et $m$ le nombre d'arêtes.

| Représentation | Mémoire | Tester si $i$–$j$ est une arête | Parcourir les voisins de $i$ |
|---|---|---|---|
| matrice d'adjacence | $O(n^2)$ | $O(1)$ | $O(n)$ |
| listes d'adjacence (dictionnaire) | $O(n + m)$ | $O(\deg i)$ | $O(\deg i)$ |

## Parcours

[[fig:i-graphes-2]]

```python
from collections import deque

def largeur(G, s):
    """Distances depuis s, en nombre d'arêtes (G : listes d'adjacence)."""
    dist = {s: 0}
    f = deque([s])
    while f:
        u = f.popleft()
        for v in G[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                f.append(v)
    return dist

def profondeur(G, s, vus=None):
    if vus is None:
        vus = set()
    vus.add(s)
    for v in G[s]:
        if v not in vus:
            profondeur(G, v, vus)
    return vus
```

> **Propriété.** Chaque sommet est visité une fois et chaque arête examinée au plus deux fois : $O(n + m)$ avec des listes d'adjacence. Le parcours en largeur donne les plus courts chemins **en nombre d'arêtes**.

Applications : connexité, composantes connexes, détection de cycle, labyrinthes.

## Détecter un cycle

- **Graphe non orienté** : pendant un parcours en profondeur, rencontrer un voisin déjà visité qui n'est pas le sommet dont on vient signale un cycle.
- **Graphe orienté** : on marque les sommets « en cours de visite » ; retomber sur un sommet en cours de visite signale un cycle.

## Parcours avec une pile

Le parcours en profondeur peut s'écrire sans récursivité, en remplaçant la file du parcours en largeur par une **pile**. C'est le seul changement entre les deux parcours.

```python
def profondeur_iter(G, s):
    vus, p = set(), [s]
    while p:
        u = p.pop()
        if u not in vus:
            vus.add(u)
            for v in G[u]:
                if v not in vus:
                    p.append(v)
    return vus
```

## Graphe pondéré en Python

Listes d'adjacence avec poids : `G = {"A": [("B", 4), ("C", 1)], ...}` ; matrice d'adjacence avec `inf` (ou `None`) pour l'absence d'arête.

## Exemple corrigé

**Énoncé.** Comment tester si un graphe non orienté est connexe ?

**Solution.** On lance un parcours (largeur ou profondeur) depuis un sommet quelconque : le graphe est connexe si et seulement si tous les sommets ont été visités, c'est-à-dire `len(largeur(G, s)) == len(G)`. Coût $O(n + m)$.

## Pièges classiques

- Oublier de marquer les sommets visités : boucle infinie dès qu'il y a un cycle.
- Marquer un sommet au moment où on le **défile** plutôt que quand on l'**enfile** : un sommet peut être ajouté plusieurs fois à la file.
