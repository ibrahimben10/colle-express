---
titre: Équations différentielles : méthode d'Euler
---
## L'essentiel

Pour une équation différentielle $y'(t) = F(t, y(t))$ avec $y(t_0) = y_0$, on calcule des valeurs approchées $y_k \approx y(t_k)$ aux instants $t_k = t_0 + kh$. La **méthode d'Euler explicite** remplace la dérivée par un taux d'accroissement.

## Méthode d'Euler explicite

[[fig:i-edo-1]]

$$y_{k+1} = y_k + h\,F(t_k, y_k).$$

```python
def euler(F, t0, y0, tf, n):
    h = (tf - t0) / n
    t, y = [t0], [y0]
    for k in range(n):
        y.append(y[k] + h * F(t[k], y[k]))
        t.append(t[k] + h)
    return t, y
```

> **Propriété.** L'erreur globale est en $O(h)$ (méthode d'ordre 1) : diviser le pas par 10 divise l'erreur par 10 environ, mais multiplie le temps de calcul par 10.

## Équation d'ordre 2 : vectorisation

On se ramène à un système d'ordre 1 sur le vecteur $Y = (y, y')$. Pour l'oscillateur $\ddot x + \omega_0^2x = 0$ :
$$\frac{\mathrm d}{\mathrm dt}\begin{pmatrix}x\\ v\end{pmatrix} = \begin{pmatrix}v\\ -\omega_0^2x\end{pmatrix}.$$

```python
import numpy as np
def F(t, Y):
    x, v = Y
    return np.array([v, -w0**2 * x])

def euler_vect(F, t0, Y0, tf, n):
    h = (tf - t0) / n
    T = np.linspace(t0, tf, n + 1)
    Y = np.zeros((n + 1, len(Y0)))
    Y[0] = Y0
    for k in range(n):
        Y[k + 1] = Y[k] + h * F(T[k], Y[k])
    return T, Y
```
Avec Euler explicite, l'énergie de l'oscillateur **augmente** artificiellement à chaque pas : l'amplitude croît. Pour un oscillateur, il faut un pas très petit devant la période (ou une meilleure méthode).

## Stabilité

Pour $y' = -\dfrac{y}{\tau}$ : $y_{k+1} = \left(1 - \dfrac h\tau\right)y_k$. La suite oscille et diverge si $h > 2\tau$ : le pas doit être petit devant les temps caractéristiques du problème.

**Euler implicite** : $y_{k+1} = y_k + hF(t_{k+1}, y_{k+1})$, plus stable, mais demande de résoudre une équation à chaque pas.

## Avec SciPy

```python
from scipy.integrate import solve_ivp
sol = solve_ivp(F, (0, 10), [1, 0], max_step=0.01)
plt.plot(sol.t, sol.y[0])
# ou : from scipy.integrate import odeint ; Y = odeint(G, Y0, t) avec G(Y, t)
```
Attention : `odeint` attend `G(Y, t)`, `solve_ivp` attend `F(t, Y)`.

## Exemple corrigé

**Énoncé.** Appliquer Euler à $y' = y$, $y(0) = 1$, sur $[0, 1]$ avec $n$ pas. Que trouve-t-on pour $y(1)$ ?

**Solution.** $y_{k+1} = (1 + h)y_k$ avec $h = 1/n$, donc $y_n = \left(1 + \dfrac1n\right)^n$. Pour $n = 10$ : 2,594 ; $n = 100$ : 2,705 ; la valeur exacte est $e \approx 2{,}718$. L'erreur est à peu près divisée par 10 quand $n$ est multiplié par 10 : ordre 1.

## Pièges classiques

- Mettre à jour $t$ et $y$ dans le mauvais ordre : utiliser $t_k$ (et non $t_{k+1}$) dans $F$ pour Euler explicite.
- Pour un système, calculer toutes les nouvelles composantes à partir des **anciennes** valeurs.
- Choisir un pas trop grand : solution instable ou fausse.
