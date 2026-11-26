---
titre: Algorithmes gloutons
---
## L'essentiel

Un algorithme **glouton** construit une solution pas à pas, en faisant à chaque étape le choix qui semble le meilleur sur le moment, sans jamais revenir en arrière. Il est rapide, mais pas toujours optimal.

## Sélection d'activités

[[fig:i-gloutons-1]]

Problème : choisir le plus grand nombre d'activités deux à deux compatibles (intervalles disjoints).

```python
def selection(activites):
    """activites : liste de couples (debut, fin)."""
    choix, fin_courante = [], float('-inf')
    for (d, f) in sorted(activites, key=lambda a: a[1]):  # tri par fin
        if d >= fin_courante:
            choix.append((d, f))
            fin_courante = f
    return choix
```

> **Propriété.** Trier par date de **fin** croissante donne une solution optimale (argument d'échange : la première activité qui finit laisse le plus de place aux autres). Coût : $O(n\log n)$, dominé par le tri.

## Rendu de monnaie

Rendre une somme avec le moins de pièces possible en prenant à chaque fois la plus grande pièce possible.
- Avec le système européen (1, 2, 5, 10, 20, 50…), la méthode gloutonne est optimale.
- Avec les pièces (1, 3, 4) et la somme 6 : glouton $4 + 1 + 1$ (3 pièces), alors que $3 + 3$ (2 pièces) est meilleur.

## Allocation de salles

Problème : placer des cours (intervalles) dans le moins de salles possible. Glouton : traiter les cours par date de **début** croissante et mettre chacun dans une salle déjà libérée s'il y en a une, sinon ouvrir une nouvelle salle. C'est optimal : le nombre de salles est le nombre maximal de cours simultanés.

## Démarche pour un algorithme glouton

1. Choisir un critère d'ordre (le « meilleur choix local »).
2. Écrire l'algorithme : tri ($O(n\log n)$) puis un parcours ($O(n)$).
3. Prouver l'optimalité (argument d'échange) **ou** trouver un contre-exemple.

## Exemple corrigé

**Énoncé.** Sac à dos fractionnaire : on peut prendre une fraction de chaque objet. Objets (poids, valeur) : (10, 60), (20, 100), (30, 120), capacité 50.

**Solution.** On trie par valeur massique décroissante : 6, 5, 4. On prend entièrement les deux premiers (poids 30, valeur 160), puis 20/30 du troisième (valeur 80) : **240**. Ici le glouton est optimal. Pour le sac à dos entier (objets non fractionnables), il ne l'est pas : il faut la programmation dynamique.

## Pièges classiques

- Ne pas affirmer qu'un algorithme glouton est optimal sans preuve ou sans avoir cherché un contre-exemple.
- Le critère de tri est essentiel : trier par durée ou par date de début ne marche pas pour la sélection d'activités.
