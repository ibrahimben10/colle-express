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

## Exemple corrigé

**Énoncé.** Jeu de Nim simplifié : 5 allumettes, chacun retire 1 ou 2 allumettes, celui qui prend la dernière gagne. Le premier joueur a-t-il une stratégie gagnante ?

**Solution.** Une position est perdante pour celui qui joue si le nombre d'allumettes est un multiple de 3 (0, 3, 6…) : quoi qu'il fasse, l'adversaire peut revenir à un multiple de 3. Avec 5 allumettes, le premier joueur en retire 2 pour laisser 3 : il gagne.

## Pièges classiques

- Pour le joueur 2, il faut que **tous** les coups mènent dans l'attracteur, pas seulement un.
- L'heuristique n'est qu'une estimation : minimax à profondeur limitée ne garantit pas le meilleur coup.
