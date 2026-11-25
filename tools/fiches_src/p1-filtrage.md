---
titre: Filtrage linéaire
---
## L'essentiel

Un filtre laisse passer certaines fréquences et en atténue d'autres. On le caractérise par son type (passe-bas, passe-haut, passe-bande), son ordre et sa ou ses fréquences de coupure.

## Passe-bas du premier ordre (RC)

[[fig:p1-filtrage-1]]

$$\underline H = \frac{1}{1 + j\dfrac{\omega}{\omega_c}},\qquad \omega_c = \frac1{RC}.$$
Gain : 0 dB aux basses fréquences, pente $-20$ dB/décade au-delà de $\omega_c$, $-3$ dB et $\varphi = -45°$ en $\omega_c$. Aux hautes fréquences, il se comporte en **intégrateur**.

## Passe-haut du premier ordre (RC)

[[fig:p1-filtrage-2]]

$$\underline H = \frac{j\dfrac{\omega}{\omega_c}}{1 + j\dfrac{\omega}{\omega_c}}.$$
Pente $+20$ dB/décade aux basses fréquences, où il se comporte en **dérivateur** ; il supprime la composante continue.

## Passe-bande du second ordre (RLC, sortie sur R)

[[fig:p1-filtrage-3]]

$$\underline H = \frac{1}{1 + jQ\left(x - \dfrac1x\right)},\qquad x = \frac{\omega}{\omega_0}.$$
Gain maximal 1 (0 dB) en $\omega_0$, bande passante $\Delta\omega = \omega_0/Q$ : plus $Q$ est grand, plus le filtre est sélectif.

## Action sur un signal

[[fig:p1-filtrage-4]]

> **Méthode — Filtrer un signal périodique.** Décomposer le signal en série de Fourier, appliquer $\underline H$ à chaque harmonique, puis recomposer. Un passe-bas de coupure bien inférieure à la fréquence du signal ne garde que la valeur moyenne.

## Pièges classiques

- Les formules ci-dessus supposent une sortie **ouverte** (aucun courant prélevé) ; une charge branchée en sortie modifie $\underline H$.
- « Intégrateur » et « dérivateur » ne sont valables que dans le domaine de fréquences correspondant à l'asymptote.
