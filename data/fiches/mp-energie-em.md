---
titre: Énergie du champ électromagnétique
---
## L'essentiel

Le champ électromagnétique transporte de l'énergie. On définit une densité volumique d'énergie $u$ et un vecteur densité de courant d'énergie, le **vecteur de Poynting** $\vec\Pi$.

> **Définitions.** $u = \dfrac{\varepsilon_0E^2}{2} + \dfrac{B^2}{2\mu_0}$ (J·m⁻³) et $\vec\Pi = \dfrac{\vec E\wedge\vec B}{\mu_0}$ (W·m⁻²).

## Bilan d'énergie

[[fig:mp-energie-em-2]]

> **Identité de Poynting.** $\dfrac{\partial u}{\partial t} + \mathrm{div}\,\vec\Pi = -\vec j\cdot\vec E$.

Forme intégrale sur un volume fixe $V$ délimité par $S$ :
$$\frac{\mathrm d}{\mathrm dt}\iiint_Vu\,\mathrm d\tau = -\oint_S\vec\Pi\cdot\mathrm d\vec S - \iiint_V\vec j\cdot\vec E\,\mathrm d\tau.$$
$\vec j\cdot\vec E$ est la puissance volumique cédée par le champ aux porteurs de charge.

## Exemple : fil résistif

[[fig:mp-energie-em-1]]

Dans un conducteur ohmique ($\vec j = \gamma\vec E$), $\vec j\cdot\vec E = \dfrac{j^2}{\gamma}$ : c'est l'effet Joule. Le flux de $\vec\Pi$ entrant par la surface latérale vaut exactement $RI^2$ : l'énergie arrive par le champ, autour du fil.

## Ordres de grandeur

Éclairement solaire au sol : $\langle\Pi\rangle \approx 1$ kW·m⁻². Laser de TP (1 mW sur 1 mm²) : 1 kW·m⁻².

## Pièges classiques

- $\vec\Pi$ se calcule avec les champs **réels** : passer aux notations réelles avant de faire un produit.
- Pour une onde, on s'intéresse en général à la moyenne temporelle $\langle\Pi\rangle$.
