---
titre: Mouvement dans un puits de potentiel
---
## L'essentiel

Pour un système conservatif à un degré de liberté, $E_m = E_c + E_p(x)$ est constante et $E_c \geq 0$ : le mouvement n'est possible que là où $E_p(x) \leq E_m$. La lecture graphique de $E_p(x)$ donne la nature du mouvement (lié ou libre, périodique) et les positions d'équilibre sans résoudre d'équation.

## Zones accessibles

[[fig:p2-puits-1]]

> **Propriété — Points de rebroussement.** Aux points où $E_p(x) = E_m$, la vitesse s'annule et le mouvement change de sens. Entre deux tels points, le mouvement est **périodique** : état lié.

- Si la zone accessible s'étend à l'infini, le système peut s'éloigner indéfiniment : état de diffusion (libre).
- Une **barrière de potentiel** (maximum de $E_p$) ne peut être franchie que si $E_m$ est supérieure à sa hauteur (en mécanique classique).
- La vitesse en un point se lit : $\frac12m\dot x^2 = E_m - E_p(x)$.

## Positions d'équilibre

Équilibre en $x_e$ si $E_p'(x_e) = 0$ ; stable pour un minimum, instable pour un maximum. Un système écarté légèrement d'un équilibre stable oscille autour ; d'un équilibre instable, il s'en éloigne.

## Approximation harmonique

[[fig:p2-puits-2]]

Au voisinage d'un minimum $x_0$ (développement de Taylor) :
$$E_p(x) \approx E_p(x_0) + \tfrac12E_p''(x_0)\,(x - x_0)^2,$$
ce qui conduit à un oscillateur harmonique de pulsation
$$\omega_0 = \sqrt{\frac{E_p''(x_0)}{m}}.$$

> **Méthode — Petites oscillations.** Trouver $x_0$ ($E_p' = 0$), vérifier la stabilité ($E_p'' > 0$), puis lire $\omega_0$ ; ou dériver $E_m$ par rapport au temps et linéariser l'équation obtenue.

La période ne dépend pas de l'amplitude tant que l'approximation harmonique est valable ; pour de grandes amplitudes, l'anharmonicité modifie la période.

## Période d'un mouvement lié

De l'énergie : $\dot x = \pm\sqrt{\frac2m(E_m - E_p(x))}$, d'où la période $T = 2\int_{x_1}^{x_2}\frac{\mathrm dx}{\sqrt{\frac2m(E_m - E_p(x))}}$ (intégrale calculée numériquement en général).

## Portrait de phase

Dans le plan $(x, \dot x)$, les trajectoires sont les courbes $\frac12m\dot x^2 + E_p(x) = E_m$ :
- courbes fermées autour d'un minimum (mouvement périodique) ;
- trajectoires ouvertes (mouvement non borné) ;
- la **séparatrice** passe par un point d'équilibre instable et sépare les deux types.

Avec frottement, les trajectoires spiralent vers l'équilibre stable.

## Exemple : pendule simple

$E_p = mg\ell(1 - \cos\theta)$, énergie cinétique $\frac12m\ell^2\dot\theta^2$. Équilibre stable en $\theta = 0$, instable en $\theta = \pi$. Aux petits angles, $\omega_0 = \sqrt{g/\ell}$. Si $E_m < 2mg\ell$, le pendule oscille ; si $E_m > 2mg\ell$, il fait des tours complets (mouvement révolutif).

## Exemple : molécule diatomique

Le potentiel de Lennard-Jones $E_p(r) = 4\varepsilon\left[\left(\frac\sigma r\right)^{12} - \left(\frac\sigma r\right)^6\right]$ a un minimum en $r_0 = 2^{1/6}\sigma$ (longueur de liaison) ; l'énergie de liaison est $\varepsilon$. Autour de $r_0$, les petites vibrations sont harmoniques.

## Exemple corrigé

**Énoncé.** Une particule a l'énergie potentielle $E_p(x) = \dfrac{a}{x^2} - \dfrac{b}{x}$ ($a, b > 0$, $x > 0$). Position d'équilibre, stabilité, nature des mouvements ?

**Solution.**
1. $E_p'(x) = -\dfrac{2a}{x^3} + \dfrac{b}{x^2} = 0$ donne $x_e = \dfrac{2a}{b}$.
2. $E_p''(x_e) = \dfrac{b^4}{8a^3} > 0$ : minimum, équilibre **stable** ; $E_p(x_e) = -\frac{b^2}{4a}$.
3. Si $-\frac{b^2}{4a} < E_m < 0$, mouvement borné entre deux points de rebroussement ; si $E_m \ge 0$, la particule part à l'infini.
4. Petites oscillations : $\omega_0 = \sqrt{\frac{b^4}{8a^3m}}$.

## Pièges classiques

- Le « $m$ » de la formule de $\omega_0$ est le coefficient du terme cinétique ($m\ell^2$ si la variable est un angle).
- Une position d'équilibre instable n'est pas un point de rebroussement : le système peut y passer avec une vitesse non nulle.
- Ces raisonnements supposent un système **conservatif**.
