---
titre: Cinématique du point
---
## L'essentiel

La cinématique décrit le mouvement sans s'intéresser à ses causes. Elle demande de choisir un **référentiel** (solide de référence muni d'une horloge), un repère et une base de projection adaptée à la géométrie du mouvement. On exprime ensuite position, vitesse et accélération dans cette base.

## Référentiel, repère, temps

- Le mouvement est **relatif** : il dépend du référentiel (un passager est immobile dans le train, en mouvement par rapport au sol).
- En mécanique classique, le temps est absolu (le même dans tous les référentiels) et les longueurs aussi.
- Repère d'espace : une origine $O$ et une base orthonormée directe.

## Position, vitesse, accélération

$$\vec v = \frac{\mathrm d\overrightarrow{OM}}{\mathrm dt},\qquad \vec a = \frac{\mathrm d\vec v}{\mathrm dt}\qquad\text{(dérivées dans le référentiel d'étude).}$$

Le vecteur vitesse est **tangent** à la trajectoire. Unités : m·s⁻¹ et m·s⁻². Le déplacement élémentaire $\mathrm d\overrightarrow{OM}$ permet aussi d'obtenir longueurs, surfaces et volumes élémentaires.

[[fig:p2-cinematique-1]]

> **Formule — Coordonnées cartésiennes.** La base est fixe : $\vec v = \dot x\,\vec u_x + \dot y\,\vec u_y + \dot z\,\vec u_z$ et $\vec a = \ddot x\,\vec u_x + \ddot y\,\vec u_y + \ddot z\,\vec u_z$ ; $\mathrm d\overrightarrow{OM} = \mathrm dx\,\vec u_x + \mathrm dy\,\vec u_y + \mathrm dz\,\vec u_z$.

### Mouvements simples

- **Rectiligne uniforme** : $\vec v$ constant. **Rectiligne uniformément accéléré** : $\vec a$ constante, $x = \frac12at^2 + v_0t + x_0$, et $v^2 - v_0^2 = 2a(x - x_0)$.
- **Mouvement à accélération constante** (chute libre) : trajectoire parabolique dans le plan contenant $\vec a$ et $\vec v_0$.

## Coordonnées polaires et cylindriques

[[fig:p2-cinematique-2]]

La base $(\vec u_r, \vec u_\theta)$ tourne avec le point : $\dfrac{\mathrm d\vec u_r}{\mathrm dt} = \dot\theta\,\vec u_\theta$ et $\dfrac{\mathrm d\vec u_\theta}{\mathrm dt} = -\dot\theta\,\vec u_r$.

> **Formule — Coordonnées cylindriques.** $\overrightarrow{OM} = r\,\vec u_r + z\,\vec u_z$ ; $\vec v = \dot r\,\vec u_r + r\dot\theta\,\vec u_\theta + \dot z\,\vec u_z$ ; $\vec a = (\ddot r - r\dot\theta^2)\,\vec u_r + (2\dot r\dot\theta + r\ddot\theta)\,\vec u_\theta + \ddot z\,\vec u_z$.

[[fig:p2-cinematique-3]]

Déplacement élémentaire : $\mathrm d\overrightarrow{OM} = \mathrm dr\,\vec u_r + r\,\mathrm d\theta\,\vec u_\theta + \mathrm dz\,\vec u_z$ ; volume élémentaire $r\,\mathrm dr\,\mathrm d\theta\,\mathrm dz$. Lien avec les cartésiennes : $x = r\cos\theta$, $y = r\sin\theta$.

## Coordonnées sphériques

[[fig:p2-cinematique-4]]

$(r, \theta, \varphi)$ avec $\theta \in [0, \pi]$ (colatitude depuis $Oz$) et $\varphi \in [0, 2\pi[$ (longitude). On retient surtout le déplacement élémentaire $\mathrm d\overrightarrow{OM} = \mathrm dr\,\vec u_r + r\,\mathrm d\theta\,\vec u_\theta + r\sin\theta\,\mathrm d\varphi\,\vec u_\varphi$ et le volume élémentaire $r^2\sin\theta\,\mathrm dr\,\mathrm d\theta\,\mathrm d\varphi$ (surface d'une sphère $4\pi R^2$, volume $\frac43\pi R^3$).

## Mouvement circulaire

[[fig:p2-cinematique-5]]

Pour $r = R$ constant : $\vec v = R\dot\theta\,\vec u_\theta$ et $\vec a = -R\dot\theta^2\,\vec u_r + R\ddot\theta\,\vec u_\theta$. En repère de Frenet : $\vec a = \dfrac{\mathrm dv}{\mathrm dt}\,\vec T + \dfrac{v^2}{R}\,\vec N$, $\vec N$ dirigé vers le centre de courbure.

> **Propriété — Mouvement circulaire uniforme.** La vitesse a une norme constante mais l'accélération n'est pas nulle : elle est centripète, de norme $v^2/R = R\omega^2$. Période $T = \frac{2\pi}{\omega}$.

Plus généralement, pour une trajectoire courbe de rayon de courbure $R_c$, l'accélération normale vaut $\frac{v^2}{R_c}$.

## Méthode

- Choisir la base selon la symétrie : cartésienne pour un mouvement rectiligne ou parabolique, polaire pour une rotation ou une force centrale, cylindrique pour une hélice.
- Dériver les vecteurs de base mobiles : c'est l'erreur la plus fréquente.
- Pour obtenir la trajectoire, éliminer le temps entre les équations horaires.
- Le mouvement est accéléré si $\vec v\cdot\vec a > 0$, décéléré si $\vec v\cdot\vec a < 0$.

## Exemple corrigé

**Énoncé.** Un point M décrit un cercle de rayon $R = 2$ m avec $\theta(t) = 3t^2$ (en rad, $t$ en s). Donner sa vitesse et son accélération à $t = 1$ s.

**Solution.**
1. $\vec v = R\dot\theta\,\vec u_\theta$ et $\vec a = -R\dot\theta^2\,\vec u_r + R\ddot\theta\,\vec u_\theta$.
2. $\dot\theta = 6$ rad·s⁻¹ et $\ddot\theta = 6$ rad·s⁻² à $t = 1$ s.
3. $v = 12$ m·s⁻¹ ; $a_r = -72$ m·s⁻² (centripète), $a_\theta = 12$ m·s⁻² (tangentielle). Le mouvement est circulaire **accéléré**.

## Exemple corrigé (spirale)

**Énoncé.** $r = r_0e^{\omega t}$ et $\theta = \omega t$. Vitesse et accélération ?

**Solution.** $\dot r = \omega r$, $\dot\theta = \omega$ : $\vec v = \omega r(\vec u_r + \vec u_\theta)$, de norme $\sqrt2\omega r$. $\ddot r - r\dot\theta^2 = \omega^2r - \omega^2r = 0$ et $2\dot r\dot\theta + r\ddot\theta = 2\omega^2r$ : $\vec a = 2\omega^2r\,\vec u_\theta$.

## Pièges classiques

- « Uniforme » signifie norme de la vitesse constante, pas accélération nulle.
- En polaire, le terme $2\dot r\dot\theta$ est souvent oublié.
- En sphériques, $\theta$ est mesuré depuis l'axe $Oz$, pas depuis le plan équatorial.
