---
titre: Force centrale, champs newtoniens
---
## L'essentiel

Une force est **centrale** si sa droite d'action passe toujours par un point fixe $O$. Le moment cinétique en $O$ est alors conservé : le mouvement est **plan** et vérifie la loi des aires.

## Conséquences de la conservation du moment cinétique

> **Propriété — Constante des aires.** $\vec L_O$ constant : le mouvement a lieu dans le plan perpendiculaire à $\vec L_O$, et $C = r^2\dot\theta$ est constante.

[[fig:p3-central-1]]

La vitesse aréolaire $\dfrac{\mathrm dA}{\mathrm dt} = \dfrac C2$ est constante : c'est la deuxième loi de Kepler.

## Énergie potentielle effective

$$E_m = \tfrac12m\dot r^2 + \underbrace{\frac{mC^2}{2r^2} + E_p(r)}_{E_{p,\text{eff}}(r)}.$$

[[fig:p3-central-2]]

Pour un champ newtonien attractif ($E_p = -k/r$) : état lié si $E_m < 0$ ($r$ entre $r_{\min}$ et $r_{\max}$), état de diffusion si $E_m \geq 0$.

## Trajectoires

[[fig:p3-central-3]]

> **Propriété — Coniques.** Dans un champ newtonien attractif, la trajectoire est une conique de foyer $O$ : ellipse ($E_m < 0$, cercle en cas particulier), parabole ($E_m = 0$), hyperbole ($E_m > 0$).

Orbite circulaire de rayon $r$ : $v = \sqrt{GM/r}$, $E_m = -\dfrac{GMm}{2r}$. Pour une ellipse de demi-grand axe $a$ : $E_m = -\dfrac{GMm}{2a}$.

> **Loi — Troisième loi de Kepler.** $\dfrac{T^2}{a^3} = \dfrac{4\pi^2}{GM}$.

## Applications

[[fig:p3-central-4]]

Satellite géostationnaire : orbite circulaire équatoriale, période d'un jour sidéral (86 164 s), rayon d'environ 42 000 km soit une altitude de 36 000 km. Vitesse de libération depuis la surface : $v_\ell = \sqrt{2GM/R}$ (11,2 km/s pour la Terre).

## Pièges classiques

- La loi des aires ne dit pas que la vitesse est constante : elle est maximale au périgée.
- Dans $T^2/a^3$, $a$ est le demi-grand axe et non la distance moyenne au hasard.
