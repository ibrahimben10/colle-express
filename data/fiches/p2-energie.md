---
titre: Aspects énergétiques de la dynamique du point
---
## L'essentiel

L'approche énergétique donne une équation scalaire, souvent plus rapide que le PFD quand on cherche une vitesse en fonction d'une position, ou les positions d'équilibre et leur stabilité. Elle repose sur la puissance, le travail et les énergies cinétique, potentielle et mécanique.

## Puissance et travail

[[fig:p2-energie-1]]

$$\mathcal P = \vec F\cdot\vec v,\qquad \delta W = \vec F\cdot\mathrm d\vec l,\qquad W_{A\to B} = \int_A^B\vec F\cdot\mathrm d\vec l.$$

- Une force perpendiculaire au déplacement (réaction normale sans frottement, tension d'un pendule, force magnétique) ne travaille pas.
- Travail **moteur** ($W > 0$) ou **résistant** ($W < 0$). Unités : J et W.
- Force constante : $W = \vec F\cdot\overrightarrow{AB}$. Travail du poids : $W = mg(z_A - z_B)$, indépendant du chemin.
- Frottement de norme constante $f$ sur une longueur $L$ : $W = -fL$ (dépend du chemin).

## Énergie cinétique

$E_c = \frac12mv^2$.

> **Théorème de l'énergie cinétique.** Dans un référentiel galiléen, $\Delta E_c = \sum W$ (toutes les forces) ; sous forme instantanée, $\dfrac{\mathrm dE_c}{\mathrm dt} = \sum\mathcal P$.

## Forces conservatives et énergie potentielle

> **Définition — Force conservative.** Son travail ne dépend pas du chemin suivi : $\delta W = -\mathrm dE_p$, soit $\vec F = -\overrightarrow{\operatorname{grad}}E_p$ ; à une dimension, $F = -\frac{\mathrm dE_p}{\mathrm dx}$.

| Force | Énergie potentielle |
|---|---|
| poids ($z$ vers le haut) | $mgz$ |
| ressort | $\tfrac12 k(\ell - \ell_0)^2$ |
| gravitation | $-\dfrac{Gm_1m_2}{r}$ |
| électrostatique (charge $q$) | $qV$ |
| force centrale en $\frac{k}{r^2}$ | $\frac kr$ |

L'énergie potentielle est définie à une constante près ; seules ses variations comptent.

## Énergie mécanique

> **Théorème de l'énergie mécanique.** $E_m = E_c + E_p$ ; $\Delta E_m = W_{\text{non conservatives}}$, ou $\frac{\mathrm dE_m}{\mathrm dt} = \mathcal P_{\text{nc}}$. En l'absence de forces non conservatives qui travaillent, $E_m$ se conserve : le système est conservatif.

Les frottements font décroître $E_m$ (l'énergie est dissipée en énergie interne, chaleur).

## Équilibre et stabilité

[[fig:p2-energie-2]]

Pour un mouvement conservatif à un degré de liberté $x$ :

- équilibre si $\dfrac{\mathrm dE_p}{\mathrm dx}(x_e) = 0$ (la force est nulle) ;
- stable si c'est un minimum ($E_p''(x_e) > 0$), instable si c'est un maximum ($E_p''(x_e) < 0$) ;
- au voisinage d'un équilibre stable, petites oscillations de pulsation $\omega_0 = \sqrt{E_p''(x_e)/m}$.

Lecture graphique : le mouvement est possible là où $E_p(x) \le E_m$ (voir la fiche sur les puits de potentiel).

## Méthode

- Si la question porte sur une **vitesse en un point**, ou si les forces inconnues ne travaillent pas, préférer l'énergie au PFD.
- Pour obtenir l'équation du mouvement d'un système conservatif à un degré de liberté : écrire $E_m$ et dériver par rapport au temps (diviser par $\dot x \ne 0$).
- Pour une réaction ou une tension, il faut le PFD (l'énergie ne les donne pas).

## Exemple corrigé

**Énoncé.** Une bille est lâchée sans vitesse d'une hauteur $h = 1{,}25$ m. Avec quelle vitesse touche-t-elle le sol (frottements négligés) ?

**Solution.**
1. Seul le poids travaille ; il est conservatif : l'énergie mécanique se conserve.
2. $0 + mgh = \tfrac12mv^2 + 0$.
3. $v = \sqrt{2gh} \approx 5$ m·s⁻¹, sans résoudre le mouvement.

## Exemple corrigé (looping)

**Énoncé.** Un chariot lâché d'une hauteur $h$ sans vitesse parcourt sans frottement un looping de rayon $R$. Hauteur minimale pour qu'il ne décolle pas au sommet ?

**Solution.** Au sommet (hauteur $2R$), l'énergie donne $v^2 = 2g(h - 2R)$. Le PFD radial au sommet : $m\frac{v^2}{R} = mg + N$, avec $N \ge 0$, soit $v^2 \ge gR$. D'où $2g(h - 2R) \ge gR$ : $h \ge \frac52R$.

## Pièges classiques

- Le TEC fait intervenir **toutes** les forces, le théorème de l'énergie mécanique seulement les non conservatives.
- Les frottements font décroître $E_m$ : $W < 0$.
- Ne pas compter une force à la fois dans $E_p$ et dans le travail.
