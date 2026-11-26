---
titre: Principes de la dynamique newtonienne
---
## L'essentiel

Dans un **référentiel galiléen**, les lois de Newton relient les forces au mouvement. On commence toujours par définir le système, le référentiel, puis on fait le bilan des forces.

## Les trois lois de Newton

> **Principe d'inertie.** Il existe des référentiels, dits galiléens, dans lesquels un point isolé est au repos ou en mouvement rectiligne uniforme.

> **Principe fondamental de la dynamique.** Dans un référentiel galiléen, $m\vec a = \sum\vec F$, ou plus généralement $\dfrac{\mathrm d\vec p}{\mathrm dt} = \sum\vec F$ avec $\vec p = m\vec v$.

> **Principe des actions réciproques.** $\vec F_{A\to B} = -\vec F_{B\to A}$, les deux forces ayant même droite d'action.

## Forces usuelles

| Force | Expression |
|---|---|
| poids | $\vec P = m\vec g$ |
| tension d'un fil | dirigée le long du fil, vers le point d'attache |
| réaction d'un support | normale $\vec R_N$ + tangentielle $\vec R_T$ (frottement) |
| frottement fluide | $-\alpha\vec v$ (faible vitesse) ou $-\beta v\vec v$ |
| poussée d'Archimède | $-\rho_{\text{fluide}}V\vec g$ |

[[fig:p2-dynamique-1]]

## Exemples à connaître

[[fig:p2-dynamique-2]]

Pendule simple, en projetant sur $\vec u_\theta$ : $\ddot\theta + \dfrac g\ell\sin\theta = 0$ ; aux petits angles, oscillateur harmonique de pulsation $\sqrt{g/\ell}$. La projection sur $\vec u_r$ donne la tension.

[[fig:p2-dynamique-3]]

Chute libre sans frottement avec $\vec v_0$ inclinée de $\alpha$ : trajectoire parabolique, portée $d = \dfrac{v_0^2\sin2\alpha}{g}$ maximale pour $\alpha = 45°$, flèche $h = \dfrac{v_0^2\sin^2\alpha}{2g}$.

## Méthode

1. Système, référentiel (supposé galiléen), repère.
2. Bilan des forces avec un schéma.
3. PFD projeté sur des axes bien choisis.
4. Résolution avec les conditions initiales.

## Exemple corrigé

**Énoncé.** Un palet de masse $m$ glisse sans frottement sur un plan incliné d'un angle $\alpha = 30°$. Calculer son accélération et la réaction du support.

**Solution.**
1. Système : le palet ; référentiel terrestre supposé galiléen ; forces : poids $m\vec g$ et réaction normale $\vec N$.
2. Base liée au plan : $\vec u_x$ le long de la pente (vers le bas), $\vec u_y$ normal au plan.
3. PFD projeté : sur $\vec u_x$, $ma = mg\sin\alpha$ ; sur $\vec u_y$, $0 = N - mg\cos\alpha$.
4. $a = g\sin\alpha \approx 4{,}9$ m·s⁻², indépendante de la masse ; $N = mg\cos\alpha$.

## Pièges classiques

- La réaction normale ne vaut $mg$ que sur un support horizontal sans autre force verticale.
- Le frottement s'oppose au **glissement**, pas forcément au mouvement global.
