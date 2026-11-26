---
titre: Images et matrices
---
## L'essentiel

Une image numérique est une **matrice** de pixels. On la représente par une liste de listes (ou un tableau NumPy) : `img[i][j]` est le pixel de la ligne $i$ (de haut en bas) et de la colonne $j$ (de gauche à droite).

[[fig:i-images-1]]

- Niveaux de gris : un entier de 0 (noir) à 255 (blanc), codé sur un octet.
- Couleur : un triplet $(R, V, B)$ de trois entiers entre 0 et 255.

```python
n, p = len(img), len(img[0])      # nombre de lignes et de colonnes
nouvelle = [[0] * p for _ in range(n)]
```

## Transformations géométriques

| Transformation | Nouveau pixel |
|---|---|
| symétrie gauche-droite | `nouv[i][j] = img[i][p - 1 - j]` |
| rotation d'un quart de tour (sens horaire) | `nouv[j][n - 1 - i] = img[i][j]` (image $p \times n$) |
| réduction d'un facteur 2 | `nouv[i][j] = img[2*i][2*j]` (ou la moyenne des 4 pixels) |
| agrandissement d'un facteur 2 | `nouv[i][j] = img[i // 2][j // 2]` |
| négatif | `nouv[i][j] = 255 - img[i][j]` |

## Convolution

[[fig:i-images-2]]

Chaque pixel est remplacé par une combinaison de ses voisins, pondérée par un **noyau** $K$ de taille $3 \times 3$ :
$$\text{nouv}[i][j] = \sum_{a=-1}^{1}\sum_{b=-1}^{1}K[a+1][b+1]\ \text{img}[i+a][j+b].$$

- **Flou** : tous les coefficients valent $1/9$ (moyenne).
- **Détection de contours** : par exemple $\begin{pmatrix}0 & -1 & 0\\ -1 & 4 & -1\\ 0 & -1 & 0\end{pmatrix}$ ; le résultat est grand là où l'intensité varie brusquement.

```python
def convolution(img, K):
    n, p = len(img), len(img[0])
    res = [[0] * p for _ in range(n)]
    for i in range(1, n - 1):            # on laisse le bord à 0
        for j in range(1, p - 1):
            s = 0
            for a in range(3):
                for b in range(3):
                    s += K[a][b] * img[i + a - 1][j + b - 1]
            res[i][j] = min(255, max(0, round(s)))
    return res
```
Coût $O(np)$ pour un noyau de taille fixe.

## Exemple corrigé

**Énoncé.** Convertir une image couleur en niveaux de gris.

**Solution.** On remplace chaque triplet par une moyenne pondérée, par exemple $0{,}299R + 0{,}587V + 0{,}114B$ (l'œil est plus sensible au vert) :
```python
gris = [[round(0.299*r + 0.587*v + 0.114*b) for (r, v, b) in ligne] for ligne in img]
```

## Pièges classiques

- Confondre ligne et colonne : `img[i][j]` est à la ligne $i$, donc à l'ordonnée.
- Écrire dans l'image qu'on est en train de lire : créer une nouvelle matrice.
- Avec NumPy, les pixels sont souvent de type `uint8` : `200 + 100` déborde et donne 44.
