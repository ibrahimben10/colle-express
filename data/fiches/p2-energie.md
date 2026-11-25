---
titre: Aspects énergétiques de la dynamique du point
---
## L'essentiel

L'approche énergétique donne une équation scalaire, souvent plus rapide que le PFD quand on cherche une vitesse en fonction d'une position, ou les positions d'équilibre.

## Puissance et travail

[[fig:p2-energie-1]]

$$\mathcal P = \vec F\cdot\vec v,\qquad \delta W = \vec F\cdot\mathrm d\vec l,\qquad W_{A\to B} = \int_A^B\vec F\cdot\mathrm d\vec l.$$
Une force perpendiculaire au déplacement (réaction normale sans frottement, force magnétique) ne travaille pas.

## Théorèmes énergétiques

> **Théorème de l'énergie cinétique.** Dans un référentiel galiléen, $\Delta E_c = \sum W$ ; sous forme instantanée, $\dfrac{\mathrm dE_c}{\mathrm dt} = \sum\mathcal P$.

> **Définition — Force conservative.** Son travail ne dépend pas du chemin suivi : $\delta W = -\mathrm dE_p$.

| Force | Énergie potentielle |
|---|---|
| poids ($z$ vers le haut) | $mgz$ |
| ressort | $\tfrac12 k(\ell - \ell_0)^2$ |
| gravitation | $-\dfrac{Gm_1m_2}{r}$ |
| électrostatique | $qV$ |

> **Théorème de l'énergie mécanique.** $\Delta E_m = W_{\text{non conservatives}}$ ; en l'absence de forces non conservatives qui travaillent, $E_m$ se conserve.

## Équilibre et stabilité

[[fig:p2-energie-2]]

Pour un mouvement à un degré de liberté : équilibre si $\dfrac{\mathrm dE_p}{\mathrm dx} = 0$ ; stable si c'est un minimum ($E_p'' > 0$), instable si c'est un maximum.

## Pièges classiques

- Le TEC fait intervenir **toutes** les forces, le théorème de l'énergie mécanique seulement les non conservatives.
- Les frottements font décroître $E_m$ : $W < 0$.
