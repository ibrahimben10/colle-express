---
titre: Introduction à la mécanique quantique
---
## L'essentiel

À l'échelle microscopique, une particule est décrite par une **fonction d'onde** $\psi(x, t)$, à valeurs complexes. Elle ne donne que des probabilités : on ne peut prévoir que la statistique des résultats de mesure.

## Interprétation probabiliste

[[fig:mp-quantique-1]]

> **Définition — Densité de probabilité.** $|\psi(x,t)|^2\,\mathrm dx$ est la probabilité de trouver la particule entre $x$ et $x + \mathrm dx$. Normalisation : $\displaystyle\int_{-\infty}^{+\infty}|\psi|^2\,\mathrm dx = 1$.

## Équation de Schrödinger

$$i\hbar\frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2} + V(x)\,\psi.$$

Pour un **état stationnaire**, $\psi(x,t) = \varphi(x)\,e^{-iEt/\hbar}$ : la densité de probabilité ne dépend pas du temps, et $\varphi$ vérifie l'équation de Schrödinger indépendante du temps.

## Dualité onde-particule

Relations de de Broglie : $p = \hbar k = \dfrac{h}{\lambda}$ et $E = \hbar\omega$.

## Inégalité de Heisenberg

[[fig:mp-quantique-2]]

> **Inégalité de Heisenberg.** $\Delta x\,\Delta p_x \ge \dfrac{\hbar}{2}$.

On ne peut pas localiser une particule en position et en impulsion à la fois. Cela permet d'estimer des ordres de grandeur (énergie de confinement, taille de l'atome).

## Ordres de grandeur

Constante de Planck réduite $\hbar = 1{,}05\cdot10^{-34}$ J·s. Électron de 1 eV : $\lambda \approx 1$ nm.

## Pièges classiques

- $\psi$ n'est pas mesurable ; seul $|\psi|^2$ a un sens physique.
- Heisenberg n'est pas une imprécision des appareils, mais une propriété de l'état.
