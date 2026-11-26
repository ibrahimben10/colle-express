---
titre: Onde dans un conducteur, réflexion
---
## L'essentiel

Dans un conducteur ohmique de conductivité $\gamma$, une onde électromagnétique de basse fréquence ne pénètre que sur une faible épaisseur, l'**épaisseur de peau** $\delta$. À la limite d'un conducteur parfait, l'onde est entièrement réfléchie.

## Effet de peau

En négligeant le courant de déplacement devant le courant de conduction, on obtient une équation de diffusion, puis
$$\underline k = \frac{1 - j}{\delta},\qquad \delta = \sqrt{\frac{2}{\mu_0\gamma\omega}}.$$

[[fig:mp-conducteur-1]]

L'onde s'atténue en $e^{-z/\delta}$ ; elle est dissipée par effet Joule.

## Ordres de grandeur

| Cuivre ($\gamma = 6\cdot10^7$ S·m⁻¹) | $\delta$ |
|---|---|
| 50 Hz | 9 mm |
| 1 MHz | 65 µm |
| 1 GHz | 2 µm |

## Réflexion sur un conducteur parfait

Dans un conducteur parfait ($\gamma\to\infty$), $\vec E = \vec 0$ et $\vec B = \vec 0$. Sous incidence normale, l'onde réfléchie a même amplitude que l'onde incidente, et le champ électrique tangentiel est nul sur la surface.

[[fig:mp-conducteur-2]]

> **Propriété — Onde stationnaire.** La superposition donne $\vec E = 2E_0\sin(kx)\sin(\omega t)\,\vec u_y$ (origine sur le métal) : **nœuds** de $\vec E$ sur le métal et tous les $\lambda/2$ ; les ventres de $\vec B$ sont aux nœuds de $\vec E$.

Le vecteur de Poynting moyen est nul : une onde stationnaire ne transporte pas d'énergie. Entre deux plans conducteurs distants de $L$, seules les ondes avec $L = n\lambda/2$ subsistent (modes propres d'une cavité).

## Exemple corrigé

**Énoncé.** Pourquoi les câbles haute tension en courant alternatif (50 Hz) sont-ils formés de plusieurs brins plutôt que d'un seul gros conducteur ? (aluminium, $\gamma = 3{,}5\cdot10^7$ S·m⁻¹)

**Solution.**
1. $\delta = \sqrt{\dfrac{2}{\mu_0\gamma\omega}} = \sqrt{\dfrac{2}{4\pi\cdot10^{-7}\times3{,}5\cdot10^7\times2\pi\cdot50}} \approx 12$ mm.
2. Le courant circule surtout dans une couche d'environ $\delta$ sous la surface : le cœur d'un conducteur de rayon bien supérieur à 12 mm serait mal utilisé.
3. Des brins de rayon inférieur à $\delta$ utilisent toute leur section : moins de pertes pour la même masse de métal.

## Pièges classiques

- Ne pas oublier les courants surfaciques induits sur le métal, qui expliquent la discontinuité de $\vec B$.
- Une onde stationnaire n'est pas une onde progressive : pas de relation $\vec B = \vec k\wedge\vec E/\omega$.
