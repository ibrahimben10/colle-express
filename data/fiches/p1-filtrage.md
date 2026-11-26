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

## Exemple corrigé

**Énoncé.** Un signal $e(t) = 2 + 3\cos(2\pi\cdot50\,t) + \cos(2\pi\cdot5000\,t)$ (en V) entre dans un passe-bas du 1er ordre de fréquence de coupure 500 Hz. Que vaut approximativement la sortie ?

**Solution.**
1. On traite chaque composante séparément (linéarité).
2. Composante continue : $|H(0)| = 1$, elle passe : 2 V.
3. 50 Hz $\ll f_c$ : $|H| \approx 1$, déphasage faible ; la composante de 3 V passe.
4. 5000 Hz $= 10f_c$ : $|H| \approx 0{,}1$ et déphasage $\approx -\pi/2$ ; il reste 0,1 V.
5. $s(t) \approx 2 + 3\cos(2\pi\cdot50\,t) + 0{,}1\cos(2\pi\cdot5000\,t - \pi/2)$ : la composante haute fréquence est fortement atténuée.

## Pièges classiques

- Les formules ci-dessus supposent une sortie **ouverte** (aucun courant prélevé) ; une charge branchée en sortie modifie $\underline H$.
- « Intégrateur » et « dérivateur » ne sont valables que dans le domaine de fréquences correspondant à l'asymptote.
