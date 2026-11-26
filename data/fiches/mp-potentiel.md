---
titre: Particule quantique dans un potentiel
---
## L'essentiel

On résout l'équation de Schrödinger stationnaire dans des potentiels constants par morceaux. Dans une zone où $E > V$, la solution est oscillante ; là où $E < V$, elle est **évanescente** (exponentielle). Aux frontières, $\varphi$ et sa dérivée sont continues (si $V$ reste fini).

## Marche de potentiel

[[fig:mp-potentiel-1]]

- $E > V_0$ : réflexion **partielle**, même si la particule classique passerait toujours.
- $E < V_0$ : réflexion totale, mais onde évanescente sur une profondeur $\delta = \dfrac{1}{\kappa}$, avec $\kappa = \dfrac{\sqrt{2m(V_0 - E)}}{\hbar}$.

## Effet tunnel

[[fig:mp-potentiel-3]]

Une barrière de hauteur $V_0 > E$ et de largeur $a$ est franchie avec une probabilité de transmission
$$T \approx e^{-2\kappa a}\quad(\kappa a \gg 1).$$
Applications : radioactivité α, microscope à effet tunnel, diode tunnel.

## Puits infini

[[fig:mp-potentiel-2]]

> **Formule — Puits infini de largeur $L$.** $\varphi_n(x) = \sqrt{\dfrac 2L}\sin\left(\dfrac{n\pi x}{L}\right)$, $E_n = \dfrac{n^2\pi^2\hbar^2}{2mL^2}$, $n \ge 1$.

Énergies **quantifiées** : analogie avec les modes d'une corde vibrante. L'énergie minimale $E_1 > 0$ est l'énergie de confinement.

## Puits fini

[[fig:mp-potentiel-4]]

Nombre fini d'états liés ($E < V_0$). Les fonctions d'onde débordent du puits ; les niveaux sont un peu plus bas que pour un puits infini de même largeur.

## Exemple corrigé

**Énoncé.** Un électron est enfermé dans un puits infini de largeur $L = 1$ nm. Calculer $E_1$ et la longueur d'onde du photon émis lors de la transition $2 \to 1$.

**Solution.**
1. $E_1 = \dfrac{\pi^2\hbar^2}{2mL^2} \approx 6{,}0\cdot10^{-20}$ J $\approx 0{,}38$ eV.
2. $E_2 - E_1 = 3E_1 \approx 1{,}1$ eV.
3. $\lambda = \dfrac{hc}{E_2 - E_1} \approx 1{,}1$ µm, dans l'infrarouge proche : c'est le principe des boîtes quantiques, dont la couleur dépend de la taille.

## Pièges classiques

- Une particule quantique peut être là où elle serait classiquement interdite.
- Pas de niveau $n = 0$ dans le puits infini : la fonction d'onde serait nulle.
