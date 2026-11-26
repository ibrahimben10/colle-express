---
titre: NumPy et tracés
---
## L'essentiel

NumPy fournit des **tableaux** de nombres de même type, sur lesquels les opérations s'appliquent coefficient par coefficient, sans boucle Python : c'est beaucoup plus rapide. Il sert dans toutes les méthodes numériques et en TP de physique.

## Créer un tableau

```python
import numpy as np
a = np.array([1.0, 2.0, 3.0])
t = np.linspace(0, 1, 101)       # 101 valeurs régulières de 0 à 1 (inclus)
u = np.arange(0, 1, 0.1)         # de 0 à 1 exclu, pas 0,1
z = np.zeros((3, 4))             # matrice nulle 3 × 4
I = np.eye(3)                    # identité
```

## Indices et formes

[[fig:i-numpy-1]]

- `A.shape` donne les dimensions ; `A[i, j]`, `A[i, :]` (ligne), `A[:, j]` (colonne), `A[1:3, ::2]`.
- Une tranche est une **vue** : la modifier modifie `A`. Utiliser `A.copy()` pour une copie.

## Calcul vectorisé

```python
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x) * np.exp(-x / 3)   # appliqué à chaque coefficient
y.max(), y.mean(), y.sum()
A @ B                             # produit matriciel (A * B : produit terme à terme)
np.linalg.solve(A, b)             # résout A X = b
np.linalg.det(A), np.linalg.inv(A)
```

## Tracer une courbe

```python
import matplotlib.pyplot as plt
plt.plot(x, y, label="amortie")
plt.plot(x, np.sin(x), "--", label="sin")
plt.xlabel("x"); plt.ylabel("y"); plt.legend(); plt.grid()
plt.show()
```
Autres tracés : `plt.scatter` (nuage de points), `plt.hist` (histogramme), `plt.errorbar` (barres d'incertitude).

## Bibliothèque SciPy (utile en TP et à l'oral)

| Besoin | Fonction |
|---|---|
| zéro d'une fonction | `scipy.optimize.brentq(f, a, b)`, `fsolve(f, x0)` |
| intégrale | `scipy.integrate.quad(f, a, b)` |
| équation différentielle | `scipy.integrate.solve_ivp`, `odeint` |
| régression | `np.polyfit(x, y, 1)` (droite des moindres carrés) |

## Exemple corrigé

**Énoncé.** Régression linéaire de mesures `x` et `y`.

**Solution.**
```python
a, b = np.polyfit(x, y, 1)       # y ≈ a x + b
residus = y - (a * x + b)
plt.plot(x, y, "o"); plt.plot(x, a * x + b); plt.show()
```
On vérifie visuellement l'alignement et l'absence de tendance dans les résidus.

## Pièges classiques

- `A * B` n'est pas le produit matriciel : utiliser `A @ B` ou `np.dot`.
- `np.arange` avec un pas flottant peut donner une valeur de plus ou de moins : préférer `np.linspace`.
- Les tableaux d'entiers ont une taille fixe et peuvent déborder.
