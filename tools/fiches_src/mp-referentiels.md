---
titre: Changements de référentiels
---
## L'essentiel

On étudie le mouvement d'un point M dans deux référentiels : R (dit absolu) et R′ (dit relatif), en mouvement par rapport à R. Au programme, deux cas seulement : R′ en **translation** par rapport à R, ou en **rotation uniforme autour d'un axe fixe**.

[[fig:mp-referentiels-1]]

## Description du mouvement de R′

- **Translation** : les axes de R′ gardent une direction fixe dans R ; tous les points de R′ ont la même vitesse $\vec v(O')$ (translation rectiligne, circulaire…).
- **Rotation uniforme autour de $Oz$** : vecteur rotation $\vec\omega = \omega\,\vec u_z$ constant ; un point fixe de R′ décrit un cercle d'axe $Oz$.

## Composition des vitesses

> **Loi — Composition des vitesses.** $\vec v_a = \vec v_r + \vec v_e$, où $\vec v_e$ est la vitesse, dans R, du **point coïncident** (point de R′ qui coïncide avec M à l'instant $t$).

[[fig:mp-referentiels-2]]

| Mouvement de R′ | Vitesse d'entraînement $\vec v_e$ |
|---|---|
| translation | $\vec v_e = \vec v(O')$ |
| rotation uniforme autour de $Oz$ | $\vec v_e = \vec\omega\wedge\overrightarrow{HM}$ ($H$ projeté de M sur l'axe) |

## Composition des accélérations

> **Loi — Composition des accélérations.** $\vec a_a = \vec a_r + \vec a_e + \vec a_c$, avec l'accélération de Coriolis $\vec a_c = 2\vec\omega\wedge\vec v_r$.

| Mouvement de R′ | $\vec a_e$ | $\vec a_c$ |
|---|---|---|
| translation | $\vec a(O')$ | $\vec 0$ |
| rotation uniforme | $-\omega^2\,\overrightarrow{HM}$ | $2\vec\omega\wedge\vec v_r$ |

## Méthode

1. Choisir R et R′ et préciser le mouvement de R′ par rapport à R.
2. Identifier le point coïncident.
3. Écrire $\vec v_r$ dans la base de R′, puis appliquer les lois de composition.

## Exemple corrigé

**Énoncé.** Un manège tourne à $\omega = 1$ rad·s⁻¹. Un enfant marche sur un rayon, vers l'extérieur, à $v_r = 1$ m·s⁻¹ par rapport au manège. À $r = 2$ m, donner sa vitesse et son accélération dans le référentiel terrestre.

**Solution.**
1. Vitesse d'entraînement (point coïncident, cercle de rayon $r$) : $\vec v_e = r\omega\,\vec u_\theta$, de norme 2 m·s⁻¹.
2. $\vec v_a = v_r\,\vec u_r + r\omega\,\vec u_\theta$, de norme $\sqrt5 \approx 2{,}2$ m·s⁻¹.
3. $\vec a_r = \vec 0$ (marche uniforme), $\vec a_e = -r\omega^2\,\vec u_r$ (2 m·s⁻² vers l'axe), $\vec a_c = 2\vec\omega\wedge\vec v_r = 2\omega v_r\,\vec u_\theta$ (2 m·s⁻²).
4. $\vec a_a = -2\,\vec u_r + 2\,\vec u_\theta$ (en m·s⁻²).

## Pièges classiques

- $\vec v_e$ n'est pas la vitesse de O′ en rotation : c'est celle du point coïncident.
- Dérivée d'un vecteur : $\left(\dfrac{\mathrm d\vec U}{\mathrm dt}\right)_R = \left(\dfrac{\mathrm d\vec U}{\mathrm dt}\right)_{R'} + \vec\omega\wedge\vec U$.
