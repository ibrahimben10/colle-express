---
titre: Principes de la dynamique newtonienne
---
## L'essentiel

Dans un **référentiel galiléen**, les lois de Newton relient les forces au mouvement. On commence toujours par définir le système, le référentiel, puis on fait le bilan des forces avant de projeter le principe fondamental sur une base adaptée.

## Masse, quantité de mouvement, centre d'inertie

- La masse est une grandeur additive et conservée (mécanique classique).
- Quantité de mouvement d'un point : $\vec p = m\vec v$ ; d'un système : $\vec p = \sum m_i\vec v_i = m\vec v_G$, où $G$ est le **centre de masse** ($m\overrightarrow{OG} = \sum m_i\overrightarrow{OM_i}$).
- Système **isolé** : soumis à aucune force ; **pseudo-isolé** : forces qui se compensent.

## Les trois lois de Newton

> **Principe d'inertie.** Il existe des référentiels, dits galiléens, dans lesquels un point isolé est au repos ou en mouvement rectiligne uniforme. Tout référentiel en translation rectiligne uniforme par rapport à un référentiel galiléen est galiléen.

> **Principe fondamental de la dynamique.** Dans un référentiel galiléen, $\dfrac{\mathrm d\vec p}{\mathrm dt} = \sum\vec F_{\text{ext}}$ ; pour une masse constante, $m\vec a = \sum\vec F$. Pour un système : $m\vec a_G = \sum\vec F_{\text{ext}}$ (théorème du centre de masse ; les forces intérieures se compensent).

> **Principe des actions réciproques.** $\vec F_{A\to B} = -\vec F_{B\to A}$, les deux forces ayant même droite d'action.

Référentiels usuels : terrestre (galiléen pour des expériences brèves), géocentrique (pour les satellites), héliocentrique (pour les planètes).

## Forces usuelles

| Force | Expression |
|---|---|
| poids | $\vec P = m\vec g$ ($g \approx 9{,}8$ m·s⁻²) |
| gravitation | $\vec F = -\frac{Gm_1m_2}{r^2}\vec u_r$ |
| tension d'un fil | dirigée le long du fil, vers le point d'attache |
| réaction d'un support | normale $\vec R_N$ + tangentielle $\vec R_T$ (frottement) |
| force de rappel d'un ressort | $-k(\ell - \ell_0)\vec u_{\text{ext}}$ |
| frottement fluide | $-\alpha\vec v$ (faible vitesse) ou $-\beta v\vec v$ (vitesse élevée) |
| poussée d'Archimède | $-\rho_{\text{fluide}}V_{\text{immergé}}\vec g$ |
| force de Lorentz | $q(\vec E + \vec v\wedge\vec B)$ |

[[fig:p2-dynamique-1]]

Un fil idéal (inextensible, sans masse) transmet la tension ; il est tendu tant que $T > 0$. Un contact cesse quand la réaction normale s'annule.

## Exemples à connaître

### Pendule simple

[[fig:p2-dynamique-2]]

En projetant sur $\vec u_\theta$ : $\ddot\theta + \dfrac g\ell\sin\theta = 0$ ; aux petits angles, oscillateur harmonique de pulsation $\sqrt{g/\ell}$. La projection sur $\vec u_r$ donne la tension : $T = mg\cos\theta + m\ell\dot\theta^2$.

### Chute libre

[[fig:p2-dynamique-3]]

Sans frottement, avec $\vec v_0$ inclinée de $\alpha$ : $x = v_0\cos\alpha\,t$, $z = -\frac12gt^2 + v_0\sin\alpha\,t$ ; trajectoire parabolique, portée $d = \dfrac{v_0^2\sin2\alpha}{g}$ maximale pour $\alpha = 45°$, flèche $h = \dfrac{v_0^2\sin^2\alpha}{2g}$.

### Chute avec frottement fluide

$m\dot v = mg - \alpha v$ : $v(t) = v_\infty(1 - e^{-t/\tau})$ avec $\tau = \frac m\alpha$ et la **vitesse limite** $v_\infty = \frac{mg}{\alpha}$. Avec un frottement quadratique, $v_\infty = \sqrt{\frac{mg}{\beta}}$.

## Méthode

1. Système, référentiel (supposé galiléen), repère et base.
2. Bilan des forces avec un schéma.
3. PFD projeté sur des axes bien choisis (souvent liés à une contrainte : le long d'un plan, polaire pour un pendule).
4. Résolution avec les conditions initiales ; discussion (rupture de contact $N = 0$, fil détendu $T = 0$).

## Exemple corrigé

**Énoncé.** Un palet de masse $m$ glisse sans frottement sur un plan incliné d'un angle $\alpha = 30°$. Calculer son accélération et la réaction du support.

**Solution.**
1. Système : le palet ; référentiel terrestre galiléen ; forces : poids $m\vec g$ et réaction normale $\vec N$.
2. Base liée au plan : $\vec u_x$ le long de la pente (vers le bas), $\vec u_y$ normal au plan.
3. Sur $\vec u_x$, $ma = mg\sin\alpha$ ; sur $\vec u_y$, $0 = N - mg\cos\alpha$.
4. $a = g\sin\alpha \approx 4{,}9$ m·s⁻², indépendante de la masse ; $N = mg\cos\alpha$.

## Exemple corrigé (vitesse limite)

**Énoncé.** Une bille de 10 g tombe dans l'huile avec un frottement $-\alpha\vec v$, $\alpha = 0{,}05$ kg·s⁻¹ (Archimède négligé). Vitesse limite et temps caractéristique ?

**Solution.** $v_\infty = \frac{mg}{\alpha} \approx 2{,}0$ m·s⁻¹ ; $\tau = \frac m\alpha = 0{,}2$ s : la vitesse limite est atteinte à 95 % au bout de $3\tau = 0{,}6$ s.

## Pièges classiques

- La réaction normale ne vaut $mg$ que sur un support horizontal sans autre force verticale.
- Le frottement s'oppose au **glissement**, pas forcément au mouvement global.
- Le PFD ne s'applique tel quel que dans un référentiel **galiléen**.
