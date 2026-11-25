---
titre: Mouvement dans un puits de potentiel
---
## L'essentiel

Pour un système conservatif à un degré de liberté, $E_m = E_c + E_p(x)$ est constante et $E_c \geq 0$ : le mouvement n'est possible que là où $E_p(x) \leq E_m$. La lecture graphique de $E_p(x)$ donne la nature du mouvement sans résoudre d'équation.

## Zones accessibles

[[fig:p2-puits-1]]

> **Propriété — Points de rebroussement.** Aux points où $E_p(x) = E_m$, la vitesse s'annule et le mouvement change de sens. Entre deux tels points, le mouvement est **périodique** : état lié.

Si la zone accessible s'étend à l'infini, le système peut s'éloigner indéfiniment : état de diffusion.

## Approximation harmonique

[[fig:p2-puits-2]]

Au voisinage d'un minimum $x_0$ :
$$E_p(x) \approx E_p(x_0) + \tfrac12E_p''(x_0)\,(x - x_0)^2,$$
ce qui conduit à un oscillateur harmonique de pulsation
$$\omega_0 = \sqrt{\frac{E_p''(x_0)}{m}}.$$

> **Méthode — Petites oscillations.** Trouver $x_0$ ($E_p' = 0$), vérifier la stabilité ($E_p'' > 0$), puis lire $\omega_0$ ; ou dériver $E_m$ par rapport au temps et linéariser.

## Exemple : pendule simple

$E_p = mg\ell(1 - \cos\theta)$, $E_p'' (0)= mg\ell$, moment d'inertie $m\ell^2$ : $\omega_0 = \sqrt{g/\ell}$. Pour de grandes amplitudes, la période augmente : l'isochronisme est perdu.

## Pièges classiques

- Le « $m$ » de la formule de $\omega_0$ est à remplacer par le coefficient du terme cinétique ($m\ell^2$ si la variable est un angle).
- Une position d'équilibre instable n'est pas un point de rebroussement : le système peut y passer avec une vitesse non nulle.
