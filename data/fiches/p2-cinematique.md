---
titre: Cinématique du point
---
## L'essentiel

La cinématique décrit le mouvement sans s'intéresser à ses causes. Elle demande de choisir un **référentiel** (solide de référence muni d'une horloge), un repère et une base de projection adaptée à la géométrie du mouvement.

## Position, vitesse, accélération

$$\vec v = \frac{\mathrm d\overrightarrow{OM}}{\mathrm dt},\qquad \vec a = \frac{\mathrm d\vec v}{\mathrm dt}\qquad\text{(dérivées dans le référentiel d'étude).}$$

[[fig:p2-cinematique-1]]

> **Formule — Coordonnées cartésiennes.** La base est fixe : $\vec v = \dot x\,\vec u_x + \dot y\,\vec u_y + \dot z\,\vec u_z$ et $\vec a = \ddot x\,\vec u_x + \ddot y\,\vec u_y + \ddot z\,\vec u_z$.

## Coordonnées polaires et cylindriques

[[fig:p2-cinematique-2]]

La base $(\vec u_r, \vec u_\theta)$ tourne avec le point : $\dfrac{\mathrm d\vec u_r}{\mathrm dt} = \dot\theta\,\vec u_\theta$ et $\dfrac{\mathrm d\vec u_\theta}{\mathrm dt} = -\dot\theta\,\vec u_r$.

> **Formule — Coordonnées cylindriques.** $\overrightarrow{OM} = r\,\vec u_r + z\,\vec u_z$ ; $\vec v = \dot r\,\vec u_r + r\dot\theta\,\vec u_\theta + \dot z\,\vec u_z$ ; $\vec a = (\ddot r - r\dot\theta^2)\,\vec u_r + (2\dot r\dot\theta + r\ddot\theta)\,\vec u_\theta + \ddot z\,\vec u_z$.

[[fig:p2-cinematique-3]]

[[fig:p2-cinematique-4]]

En coordonnées sphériques $(r, \theta, \varphi)$, on retient surtout le déplacement élémentaire : $\mathrm d\overrightarrow{OM} = \mathrm dr\,\vec u_r + r\,\mathrm d\theta\,\vec u_\theta + r\sin\theta\,\mathrm d\varphi\,\vec u_\varphi$.

## Mouvement circulaire

[[fig:p2-cinematique-5]]

Pour $r = R$ constant : $\vec v = R\dot\theta\,\vec u_\theta$ et $\vec a = -R\dot\theta^2\,\vec u_r + R\ddot\theta\,\vec u_\theta$. En repère de Frenet : $\vec a = \dfrac{\mathrm dv}{\mathrm dt}\,\vec T + \dfrac{v^2}{R}\,\vec N$, $\vec N$ dirigé vers le centre.

> **Propriété — Mouvement circulaire uniforme.** La vitesse a une norme constante mais l'accélération n'est pas nulle : elle est centripète, de norme $v^2/R = R\omega^2$.

## Méthode

- Choisir la base selon la symétrie : cartésienne pour un mouvement rectiligne ou parabolique, polaire pour une rotation ou une force centrale.
- Dériver les vecteurs de base mobiles : c'est l'erreur la plus fréquente.

## Exemple corrigé

**Énoncé.** Un point M décrit un cercle de rayon $R = 2$ m avec $\theta(t) = 3t^2$ (en rad, $t$ en s). Donner sa vitesse et son accélération à $t = 1$ s.

**Solution.**
1. En coordonnées polaires ($r = R$ constant) : $\vec v = R\dot\theta\,\vec u_\theta$ et $\vec a = -R\dot\theta^2\,\vec u_r + R\ddot\theta\,\vec u_\theta$.
2. $\dot\theta = 6t = 6$ rad·s⁻¹ et $\ddot\theta = 6$ rad·s⁻² à $t = 1$ s.
3. $v = 12$ m·s⁻¹ ; $a_r = -72$ m·s⁻² (centripète), $a_\theta = 12$ m·s⁻² (tangentielle). Le mouvement est circulaire **accéléré**.

## Pièges classiques

- « Uniforme » signifie norme de la vitesse constante, pas accélération nulle.
- En polaire, le terme $2\dot r\dot\theta$ (Coriolis cinématique) est souvent oublié.
