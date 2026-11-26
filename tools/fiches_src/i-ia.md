---
titre: Algorithmes pour l'intelligence artificielle
---
## L'essentiel

Deux algorithmes d'apprentissage au programme : les **k plus proches voisins** (apprentissage supervisé : on dispose d'exemples étiquetés) et les **k-moyennes** (apprentissage non supervisé : on cherche des groupes).

## Distance

Les données sont des vecteurs de $\mathbb R^d$ ; on utilise en général la distance euclidienne $d(x, y) = \sqrt{\sum_k(x_k - y_k)^2}$. Il faut souvent **normaliser** les attributs pour qu'ils aient des échelles comparables.

## k plus proches voisins

[[fig:i-ia-1]]

Pour classer un nouveau point : calculer sa distance à tous les exemples, garder les $k$ plus proches, renvoyer la classe **majoritaire**.

```python
def knn(exemples, x, k):
    """exemples : liste de couples (point, classe)."""
    proches = sorted(exemples, key=lambda e: distance(e[0], x))[:k]
    compte = {}
    for _, c in proches:
        compte[c] = compte.get(c, 0) + 1
    return max(compte, key=compte.get)
```

Coût par prédiction : $O(n\log n)$ avec un tri (ou $O(nd)$ pour les distances). On évalue la qualité sur un jeu de **test** séparé, avec une **matrice de confusion**. Le choix de $k$ est un compromis : $k$ trop petit est sensible au bruit, $k$ trop grand mélange les classes.

## k-moyennes

[[fig:i-ia-2]]

1. Choisir $k$ centres initiaux (par exemple $k$ points au hasard).
2. **Affecter** chaque point au centre le plus proche.
3. **Recalculer** chaque centre comme la moyenne (barycentre) de son groupe.
4. Recommencer jusqu'à ce que les groupes ne changent plus.

> **Propriété.** L'inertie (somme des carrés des distances aux centres) diminue à chaque étape, donc l'algorithme termine ; mais le résultat dépend de l'initialisation (minimum local).

## Exemple corrigé

**Énoncé.** Points de $\mathbb R$ : 1, 2, 3, 10, 11, 12 ; $k = 2$ ; centres initiaux 1 et 2. Dérouler les k-moyennes.

**Solution.**
1. Affectation : {1} au centre 1 ; {2, 3, 10, 11, 12} au centre 2. Nouveaux centres : 1 et 7,6.
2. Affectation : {1, 2, 3} (plus proches de 1) et {10, 11, 12}. Centres : 2 et 11.
3. Plus de changement : groupes {1, 2, 3} et {10, 11, 12}.

## Pièges classiques

- Ne pas normaliser des attributs d'unités différentes (une taille en m et une masse en g).
- Confondre $k$ (nombre de voisins) dans kNN et $k$ (nombre de groupes) dans les k-moyennes.
