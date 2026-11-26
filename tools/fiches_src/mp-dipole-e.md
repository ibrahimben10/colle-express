---
titre: Dipôle électrostatique
---
## L'essentiel

Un dipôle est formé de deux charges opposées $-q$ (en N) et $+q$ (en P), très proches. Il est caractérisé par son **moment dipolaire** $\vec p = q\,\overrightarrow{NP}$ (en C·m). On l'étudie à grande distance.

## Potentiel et champ créés

Dans l'approximation dipolaire ($r \gg NP$), en coordonnées sphériques d'axe $\vec p$ :
$$V = \frac{p\cos\theta}{4\pi\varepsilon_0r^2},\qquad E_r = \frac{2p\cos\theta}{4\pi\varepsilon_0r^3},\qquad E_\theta = \frac{p\sin\theta}{4\pi\varepsilon_0r^3}.$$

[[fig:mp-dipole-e-1]]

Le potentiel décroît en $1/r^2$ et le champ en $1/r^3$ : plus vite que pour une charge seule.

## Dipôle dans un champ extérieur

[[fig:mp-dipole-e-2]]

> **Propriété — Actions sur un dipôle rigide.** Dans un champ uniforme : résultante nulle, couple $\vec\Gamma = \vec p\wedge\vec E$. Énergie potentielle $E_p = -\vec p\cdot\vec E$.

- Équilibre **stable** pour $\vec p$ colinéaire à $\vec E$ et de même sens ; instable en sens opposé.
- Dans un champ non uniforme, la résultante $\vec F = (\vec p\cdot\overrightarrow{\mathrm{grad}})\vec E$ attire le dipôle aligné vers les zones de champ intense.

## Applications

Molécules polaires (eau : $p \approx 6\cdot10^{-30}$ C·m), solvatation des ions, forces de Van der Waals, électrisation d'un morceau de papier par un objet frotté.

## Exemple corrigé

**Énoncé.** Une molécule d'eau ($p = 6{,}2\cdot10^{-30}$ C·m) est placée dans un champ uniforme $E = 10^6$ V·m⁻¹. Calculer le couple maximal et comparer l'énergie d'orientation à $k_BT$ à 300 K.

**Solution.**
1. Couple maximal (pour $\vec p \perp \vec E$) : $\Gamma = pE = 6{,}2\cdot10^{-24}$ N·m.
2. Écart d'énergie entre les orientations extrêmes : $2pE \approx 1{,}2\cdot10^{-23}$ J.
3. $k_BT \approx 4{,}1\cdot10^{-21}$ J, plus de 300 fois plus grand : l'agitation thermique empêche l'alignement complet, seule une faible orientation moyenne subsiste.

## Pièges classiques

- $\vec p$ va de la charge **négative** vers la charge **positive**.
- Les formules ne valent que loin du dipôle.
