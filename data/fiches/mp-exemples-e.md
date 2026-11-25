---
titre: Exemples de champs électrostatiques
---
## L'essentiel

Quatre distributions très symétriques, traitées toutes par le théorème de Gauss : boule, fil infini, plan infini, condensateur plan. À connaître et à savoir redémontrer.

## Boule uniformément chargée

[[fig:mp-exemples-e-1]]

Boule de rayon $R$, de charge $Q$ uniforme. Symétrie sphérique : $\vec E = E(r)\,\vec u_r$. Sphère de Gauss de rayon $r$ :
$$E(r) = \frac{Q\,r}{4\pi\varepsilon_0R^3}\ (r < R),\qquad E(r) = \frac{Q}{4\pi\varepsilon_0r^2}\ (r > R).$$
À l'extérieur, tout se passe comme si la charge était concentrée au centre.

## Fil infini

[[fig:mp-exemples-e-2]]

Fil de charge linéique $\lambda$ : $\vec E = \dfrac{\lambda}{2\pi\varepsilon_0r}\,\vec u_r$ (coordonnées cylindriques). Le flux à travers les bases du cylindre est nul.

## Plan infini

[[fig:mp-exemples-e-3]]

Plan de charge surfacique $\sigma$ : $\vec E = \pm\dfrac{\sigma}{2\varepsilon_0}\,\vec u_z$ selon le côté. Le champ est **uniforme** de chaque côté et subit une discontinuité de $\sigma/\varepsilon_0$ à la traversée.

## Condensateur plan

[[fig:mp-exemples-e-4]]

Par superposition des deux plans de charges $+\sigma$ et $-\sigma$ :

> **Formule — Condensateur plan.** $E = \dfrac{\sigma}{\varepsilon_0}$ entre les armatures, nul à l'extérieur ; $U = Ee$, d'où la capacité $C = \dfrac{\varepsilon_0S}{e}$.

Énergie stockée : $\tfrac12CU^2 = \tfrac{\varepsilon_0E^2}{2}\cdot Se$, soit une densité volumique d'énergie $\dfrac{\varepsilon_0E^2}{2}$.

## Pièges classiques

- Le fil et le plan infinis sont des modèles : loin d'un fil fini, on retrouve un champ en $1/r^2$.
- Le champ d'un plan ne dépend pas de la distance au plan.
