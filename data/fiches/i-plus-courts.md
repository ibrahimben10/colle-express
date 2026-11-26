---
titre: Plus courts chemins
---
## L'essentiel

Dans un graphe pondéré à poids **positifs**, l'algorithme de Dijkstra calcule les distances depuis un sommet source. Sans poids, un simple parcours en largeur suffit.

## Algorithme de Dijkstra

[[fig:i-plus-courts-1]]

1. Distance provisoire 0 pour la source, $+\infty$ pour les autres.
2. Tant qu'il reste des sommets non traités : choisir le sommet non traité $u$ de plus petite distance provisoire ; il est définitivement traité.
3. Pour chaque voisin $v$ de $u$ : si $d(u) + w(u, v) < d(v)$, mettre à jour $d(v)$ (et retenir $u$ comme prédécesseur).

```python
import heapq

def dijkstra(G, s):
    """G[u] : liste de couples (v, poids). Renvoie le dictionnaire des distances."""
    dist = {s: 0}
    tas = [(0, s)]
    traites = set()
    while tas:
        d, u = heapq.heappop(tas)
        if u in traites:
            continue
        traites.add(u)
        for v, w in G[u]:
            if v not in dist or d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(tas, (dist[v], v))
    return dist
```

> **Propriété.** Avec une file de priorité (tas), la complexité est $O((n + m)\log n)$. L'algorithme est correct parce que les poids sont positifs : la distance d'un sommet traité ne peut plus diminuer.

Pour retrouver le chemin : remonter les prédécesseurs depuis l'arrivée.

## Retrouver le chemin

On mémorise pour chaque sommet son **prédécesseur** au moment de la mise à jour, puis on remonte depuis l'arrivée :
```python
def chemin(pred, s, t):
    c = [t]
    while c[-1] != s:
        c.append(pred[c[-1]])
    return c[::-1]
```

## Algorithme A*

Variante de Dijkstra guidée par une **heuristique** $h(v)$ qui estime la distance restante jusqu'à l'arrivée (par exemple la distance à vol d'oiseau sur une carte). On traite en priorité le sommet qui minimise $d(v) + h(v)$. Si $h$ ne surestime jamais la vraie distance, le chemin trouvé est optimal, et beaucoup moins de sommets sont explorés.

## File de priorité naïve

Le programme accepte une version sans tas : on cherche à chaque étape le minimum parmi les sommets non traités par un parcours. Complexité $O(n^2)$, suffisante pour des graphes denses.

## Exemple corrigé

**Énoncé.** Sur le graphe de la figure, dans quel ordre Dijkstra traite-t-il les sommets depuis A ?

**Solution.** A (0) ; on met à jour B = 4 et C = 1. On traite C (1) : B devient $\min(4, 1 + 2) = 3$, D = 9. On traite B (3) : D devient $\min(9, 3 + 5) = 8$. Puis D (8) : E = 11. Ordre : A, C, B, D, E.

## Pièges classiques

- Dijkstra est faux avec des poids négatifs.
- Ne pas confondre l'ordre de **traitement** (distances croissantes) et l'ordre de découverte.
