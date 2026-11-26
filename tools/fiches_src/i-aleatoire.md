---
titre: Simulation aléatoire et Monte-Carlo
---
## L'essentiel

Le module `random` produit des nombres **pseudo-aléatoires**. On s'en sert pour simuler des expériences (lancers, marches aléatoires, files d'attente), tester des algorithmes sur des données aléatoires et estimer des grandeurs par la **méthode de Monte-Carlo**.

## Fonctions utiles

```python
import random
random.random()            # flottant uniforme dans [0, 1[
random.uniform(a, b)       # flottant uniforme dans [a, b]
random.randint(1, 6)       # entier entre 1 et 6 inclus
random.choice(L)           # élément au hasard
random.shuffle(L)          # mélange L en place
random.gauss(mu, sigma)    # loi normale
random.seed(42)            # rend la suite reproductible
```
Avec NumPy : `np.random.rand(n)`, `np.random.normal(mu, sigma, n)`.

## Méthode de Monte-Carlo

[[fig:i-aleatoire-1]]

Pour estimer une probabilité $p$, on répète $N$ fois l'expérience et on calcule la fréquence de succès $\hat p$.

```python
def estime_pi(N):
    dedans = 0
    for _ in range(N):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1:
            dedans += 1
    return 4 * dedans / N
```

> **Propriété.** L'erreur typique de Monte-Carlo est en $\dfrac{1}{\sqrt N}$ (écart-type $\sqrt{p(1-p)/N}$) : pour gagner un chiffre, il faut 100 fois plus de tirages. La méthode est lente, mais simple et utilisable en grande dimension.

## Propagation des incertitudes par Monte-Carlo

En TP de physique : on tire de nombreuses valeurs des grandeurs mesurées selon leur incertitude, on calcule le résultat pour chaque tirage, et l'écart-type des résultats donne l'incertitude-type.

```python
import numpy as np
N = 100_000
L = np.random.normal(1.00, 0.01, N)      # longueur (m)
T = np.random.normal(2.01, 0.02, N)      # période (s)
g = 4 * np.pi**2 * L / T**2
print(g.mean(), g.std(ddof=1))
```

## Exemple corrigé

**Énoncé.** Estimer la probabilité d'obtenir au moins un six en quatre lancers de dé.

**Solution.**
```python
def experience():
    return any(random.randint(1, 6) == 6 for _ in range(4))
N = 100_000
p = sum(experience() for _ in range(N)) / N
```
On trouve environ 0,518 ; la valeur exacte est $1 - (5/6)^4 \approx 0{,}5177$, l'écart est de l'ordre de $1/\sqrt N \approx 0{,}003$.

## Pièges classiques

- `random.randint(a, b)` inclut $b$, contrairement à `range`.
- Conclure avec trop peu de tirages : toujours estimer l'erreur en $1/\sqrt N$.
- Fixer la graine (`seed`) pour pouvoir reproduire un résultat lors du débogage.
