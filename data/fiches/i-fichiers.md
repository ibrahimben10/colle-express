---
titre: Fichiers, modules et données
---
## L'essentiel

Un programme lit souvent ses données dans un **fichier texte** (mesures, tableau CSV), les traite, puis les écrit ou les représente graphiquement. Python fournit `open` pour les fichiers et de nombreux **modules** (`math`, `random`, `matplotlib`, `numpy`).

## Importer un module

```python
import math                 # math.sqrt(2), math.pi
from math import sqrt, pi   # sqrt(2), pi
import numpy as np          # np.array(...)
import matplotlib.pyplot as plt
```

Aucune connaissance d'un module particulier n'est exigible : l'énoncé rappelle les fonctions utiles. Il faut savoir lire leur documentation.

## Lire un fichier

[[fig:i-fichiers-1]]

```python
f = open("mesures.csv", "r")      # "r" : lecture
lignes = f.readlines()            # liste de chaînes, avec "\n" à la fin
f.close()

t, x = [], []
for ligne in lignes[1:]:          # on saute l'en-tête
    champs = ligne.strip().split(";")
    t.append(float(champs[0]))
    x.append(float(champs[1]))
```

- `f.read()` : tout le fichier en une chaîne ; `f.readline()` : la ligne suivante.
- `with open(...) as f:` ferme le fichier automatiquement.

## Écrire un fichier

```python
f = open("resultats.txt", "w")    # "w" : écrase ; "a" : ajoute à la fin
for ti, xi in zip(t, x):
    f.write(f"{ti};{xi}\n")       # write n'ajoute pas de saut de ligne
f.close()
```

## Statistiques et graphiques

```python
moy = sum(x) / len(x)
var = sum((xi - moy) ** 2 for xi in x) / len(x)

plt.plot(t, x, "o-", label="mesures")
plt.xlabel("t (s)"); plt.ylabel("x (m)"); plt.legend(); plt.grid()
plt.show()

plt.hist(x, bins=20)              # histogramme
```

## Exemple corrigé

**Énoncé.** Un fichier contient une note par ligne. Écrire une fonction qui renvoie la moyenne et le nombre de notes supérieures ou égales à 10.

**Solution.**
```python
def bilan(nom):
    with open(nom) as f:
        notes = [float(l) for l in f.readlines() if l.strip() != ""]
    moy = sum(notes) / len(notes)
    recus = len([n for n in notes if n >= 10])
    return moy, recus
```
On ignore les lignes vides ; la lecture est en $O(n)$.

## Pièges classiques

- Oublier de convertir : `"12" + "3"` vaut `"123"`, il faut `float` ou `int`.
- Oublier `strip()` : le `"\n"` final reste collé au dernier champ.
- Ouvrir en `"w"` un fichier qu'on voulait lire : il est effacé.
