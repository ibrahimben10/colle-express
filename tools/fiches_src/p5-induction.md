---
titre: Lois de l'induction
---
## L'essentiel

Une variation du flux magnétique à travers un circuit fait apparaître une **force électromotrice** induite. Le sens des effets induits s'oppose à la cause qui leur donne naissance.

## Flux magnétique

[[fig:p5-induction-1]]

$$\Phi = \iint_S\vec B\cdot\vec n\,\mathrm dS\quad(\text{en webers}),$$
où $\vec n$ est orienté par le sens choisi pour le contour (règle de la main droite). Dans un champ uniforme et pour un circuit plan : $\Phi = BS\cos\theta$.

## Loi de Faraday

> **Loi de Faraday.** $e = -\dfrac{\mathrm d\Phi}{\mathrm dt}$, la f.é.m. étant orientée dans le sens du contour (convention générateur).

Le circuit se modélise par un générateur de f.é.m. $e$ en série avec sa résistance.

## Loi de Lenz

[[fig:p5-induction-2]]

> **Loi de Lenz.** Les effets de l'induction s'opposent aux causes qui les ont produits : le courant induit crée un champ qui tend à compenser la variation du flux.

C'est une loi de **modération**, qui permet de prévoir qualitativement le sens du courant ou de la force induite.

## Auto-induction

Le flux propre d'un circuit est proportionnel à son courant : $\Phi_p = Li$, $L$ inductance propre (en henrys). La f.é.m. auto-induite vaut $e = -L\dfrac{\mathrm di}{\mathrm dt}$ : on retrouve la loi de la bobine. Énergie magnétique : $\tfrac12Li^2$.

## Exemple corrigé

**Énoncé.** Une bobine plate de 100 spires de surface 20 cm² est placée dans un champ uniforme perpendiculaire à son plan, qui croît linéairement de 0 à 0,1 T en 0,2 s. Calculer la f.é.m. induite.

**Solution.**
1. Flux total : $\Phi = NBS$ (normale orientée selon $\vec B$).
2. $e = -\dfrac{\mathrm d\Phi}{\mathrm dt} = -NS\dfrac{\mathrm dB}{\mathrm dt} = -100\times20\cdot10^{-4}\times0{,}5 = -0{,}1$ V.
3. Le signe moins traduit la loi de Lenz : le courant induit crée un champ opposé à l'augmentation de $B$.

## Pièges classiques

- Le signe de $e$ dépend de l'orientation choisie : fixer le sens du contour **avant** de calculer le flux.
- Pas de variation de flux, pas d'induction, même dans un champ intense.
