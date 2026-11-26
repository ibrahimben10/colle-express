---
titre: Jeux et stratégies
---
## L'essentiel

Un jeu à deux joueurs, à information complète et sans hasard, se modélise par un **graphe** dont les sommets sont les positions. On cherche les positions **gagnantes** et une **stratégie** gagnante, ou, si le graphe est trop grand, une bonne décision avec l'algorithme **minimax** et une heuristique.

## Graphe de jeu et attracteur

[[fig:i-jeux-2]]

Le graphe est **biparti** : les positions où joue le joueur 1 alternent avec celles où joue le joueur 2.

> **Définition — Attracteur.** L'attracteur du joueur 1 vers les positions gagnantes $G$ se construit par itérations : on part de $G$, puis on ajoute
> - toute position du joueur 1 qui a **au moins un** successeur dans l'ensemble ;
> - toute position du joueur 2 dont **tous** les successeurs sont dans l'ensemble.
>
> On s'arrête quand l'ensemble ne change plus : depuis ces positions, le joueur 1 peut forcer la victoire.

## Algorithme minimax

[[fig:i-jeux-1]]

```python
def minimax(position, profondeur, joueur_max):
    if profondeur == 0 or terminale(position):
        return heuristique(position)
    valeurs = [minimax(p, profondeur - 1, not joueur_max) for p in coups(position)]
    return max(valeurs) if joueur_max else min(valeurs)
```

On explore l'arbre des coups jusqu'à une profondeur donnée. Les feuilles sont évaluées par une **heuristique** (estimation de l'intérêt de la position), puis les valeurs remontent : maximum pour le joueur, minimum pour l'adversaire.

Coût : $O(b^p)$ pour un facteur de branchement $b$ et une profondeur $p$.

## Stratégie

Une **stratégie** dit, pour chaque position d'un joueur, quel coup jouer. Une stratégie **sans mémoire** ne dépend que de la position actuelle. Dans un jeu d'accessibilité, si une position est dans l'attracteur, la stratégie « aller vers un successeur de l'attracteur ajouté plus tôt » est gagnante et sans mémoire.

## Calcul de l'attracteur

```python
def attracteur(G, joueur1, gagnantes):
    """G : successeurs ; joueur1 : ensemble des positions du joueur 1."""
    A = set(gagnantes)
    change = True
    while change:
        change = False
        for s in G:
            if s not in A:
                if (s in joueur1 and any(t in A for t in G[s])) or \
                   (s not in joueur1 and G[s] and all(t in A for t in G[s])):
                    A.add(s); change = True
    return A
```

## Heuristique

Pour un jeu réel (échecs, puissance 4), on ne peut pas explorer tout l'arbre. L'**heuristique** donne une note à une position non terminale (avantage matériel, alignements…). L'élagage alpha-bêta, qui accélère minimax, est hors programme.

## Exemple corrigé

**Énoncé.** Jeu de Nim simplifié : 5 allumettes, chacun retire 1 ou 2 allumettes, celui qui prend la dernière gagne. Le premier joueur a-t-il une stratégie gagnante ?

**Solution.** Une position est perdante pour celui qui joue si le nombre d'allumettes est un multiple de 3 (0, 3, 6…) : quoi qu'il fasse, l'adversaire peut revenir à un multiple de 3. Avec 5 allumettes, le premier joueur en retire 2 pour laisser 3 : il gagne.

## Pièges classiques

- Pour le joueur 2, il faut que **tous** les coups mènent dans l'attracteur, pas seulement un.
- L'heuristique n'est qu'une estimation : minimax à profondeur limitée ne garantit pas le meilleur coup.
