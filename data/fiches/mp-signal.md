---
titre: Signaux périodiques, filtrage
---
## L'essentiel

Un signal périodique de fréquence $f$ se décompose en une somme de sinusoïdes de fréquences $nf$ (série de Fourier). Un filtre linéaire agit sur chaque harmonique séparément, à travers sa fonction de transfert.

## Décomposition de Fourier

$$s(t) = a_0 + \sum_{n\ge1}A_n\cos(2\pi nft + \varphi_n),$$
où $a_0$ est la valeur moyenne. Le **spectre** représente $A_n$ en fonction de $nf$. Un créneau ne contient que des harmoniques impairs, d'amplitudes en $1/n$ ; un triangle, en $1/n^2$.

> **Propriété — Action d'un filtre.** Chaque harmonique de pulsation $\omega_n$ est multiplié par $|H(j\omega_n)|$ et déphasé de $\arg H(j\omega_n)$.

## Gabarit d'un filtre

[[fig:mp-signal-1]]

Le gabarit traduit un cahier des charges : gain minimal dans la bande passante, gain maximal dans la bande coupée. On choisit ensuite l'ordre et la fréquence de coupure du filtre.

## Caractère intégrateur ou dérivateur

[[fig:mp-signal-2]]

- Un passe-bas du 1er ordre est **intégrateur** pour $f \gg f_c$ : un créneau donne un triangle.
- Un passe-haut du 1er ordre est **dérivateur** pour $f \ll f_c$ : le créneau donne des pics aux fronts.
- Pour garder la seule valeur moyenne : passe-bas avec $f_c \ll f$.

## Puissance et valeur efficace

$S_{\text{eff}}^2 = a_0^2 + \sum_n \dfrac{A_n^2}{2}$ (formule de Parseval).

## Exemple corrigé

**Énoncé.** Un créneau de fréquence 1 kHz, de valeur moyenne nulle et d'amplitude $E$, a pour harmoniques $\dfrac{4E}{n\pi}$ aux rangs $n$ impairs. On veut extraire le fondamental avec un passe-bande très sélectif centré sur 1 kHz. Quelle amplitude obtient-on ?

**Solution.**
1. Le filtre laisse passer la seule composante à 1 kHz (rang 1) et coupe les rangs 3, 5…
2. Amplitude du fondamental : $\dfrac{4E}{\pi} \approx 1{,}27E$, plus grande que l'amplitude du créneau.
3. On obtient une sinusoïde à 1 kHz : un créneau filtré est une manière simple de fabriquer une sinusoïde.

## Pièges classiques

- Un filtre non linéaire (diode, saturation) crée de nouvelles fréquences ; un filtre linéaire, jamais.
- Pour savoir si un harmonique passe, comparer sa fréquence $nf$ (et non $f$) à $f_c$.
