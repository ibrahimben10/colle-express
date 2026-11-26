---
titre: Dipôle magnétique
---
## L'essentiel

Une boucle de courant de petite taille, vue de loin, est un **dipôle magnétique**, caractérisé par son moment $\vec m = I\,S\,\vec n$ (en A·m²). Les aimants et les atomes se modélisent de la même façon.

## Champ créé

[[fig:mp-dipole-m-1]]

Loin de la spire ($r \gg$ sa taille), le champ a la même forme que celui d'un dipôle électrostatique, en remplaçant $\dfrac{\vec p}{\varepsilon_0}$ par $\mu_0\vec m$ :
$$B_r = \frac{\mu_0}{4\pi}\frac{2m\cos\theta}{r^3},\qquad B_\theta = \frac{\mu_0}{4\pi}\frac{m\sin\theta}{r^3}.$$

## Actions subies

[[fig:mp-dipole-m-2]]

> **Propriété — Dipôle dans un champ uniforme.** Résultante nulle, couple $\vec\Gamma = \vec m\wedge\vec B$, énergie potentielle $E_p = -\vec m\cdot\vec B$.

La boussole s'oriente selon le champ local (équilibre stable pour $\vec m$ dans le sens de $\vec B$). Dans un champ non uniforme, un aimant aligné est attiré vers les zones de champ fort.

## Ordres de grandeur

| Objet | $m$ |
|---|---|
| magnéton de Bohr (électron) | $9{,}3\cdot10^{-24}$ A·m² |
| aimant usuel | 1 A·m² |
| Terre | $8\cdot10^{22}$ A·m² |

## Exemple corrigé

**Énoncé.** Une boussole (moment $m = 0{,}1$ A·m²) est soumise à la composante horizontale du champ terrestre, $B_h = 2\cdot10^{-5}$ T. Calculer le couple qui la ramène lorsqu'elle est écartée de 90°, et la période des petites oscillations (moment d'inertie $J = 10^{-7}$ kg·m²).

**Solution.**
1. $\Gamma = mB_h\sin\theta$, maximal à 90° : $2\cdot10^{-6}$ N·m.
2. Petits angles : $J\ddot\theta = -mB_h\theta$, d'où $\omega_0 = \sqrt{\dfrac{mB_h}{J}} \approx 4{,}5$ rad·s⁻¹.
3. $T_0 = 2\pi/\omega_0 \approx 1{,}4$ s. Mesurer cette période permet de mesurer $B_h$.

## Pièges classiques

- Le sens de $\vec n$ est lié au sens du courant par la règle de la main droite.
- Le pôle nord géographique de la Terre est un pôle sud magnétique.
