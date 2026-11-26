---
titre: Filtrage linéaire
---
## L'essentiel

Un filtre laisse passer certaines fréquences et en atténue d'autres. On le caractérise par son type (passe-bas, passe-haut, passe-bande, coupe-bande), son ordre et sa ou ses fréquences de coupure. Connaissant le spectre d'un signal, on prévoit la sortie composante par composante.

## Prévoir le type de filtre

Remplacer les composants par leur comportement limite : à basse fréquence, $C$ est un interrupteur ouvert et $L$ un fil ; à haute fréquence, $C$ est un fil et $L$ un interrupteur ouvert. On lit alors si la sortie est nulle ou égale à l'entrée aux deux extrémités.

## Passe-bas du premier ordre (RC)

[[fig:p1-filtrage-1]]

$$\underline H = \frac{1}{1 + j\dfrac{\omega}{\omega_c}},\qquad \omega_c = \frac1{RC}.$$

- Gain : 0 dB aux basses fréquences, pente $-20$ dB/décade au-delà de $\omega_c$ ; $-3$ dB et $\varphi = -45°$ en $\omega_c$.
- Phase de $0$ à $-90°$.
- Aux hautes fréquences ($\omega \gg \omega_c$), $\underline H \approx \frac{\omega_c}{j\omega}$ : il se comporte en **intégrateur** ($s \approx \omega_c\int e$).
- Usage : extraire la valeur moyenne, lisser, filtre anti-repliement.

## Passe-haut du premier ordre (RC)

[[fig:p1-filtrage-2]]

$$\underline H = \frac{j\dfrac{\omega}{\omega_c}}{1 + j\dfrac{\omega}{\omega_c}}.$$

- Pente $+20$ dB/décade aux basses fréquences, 0 dB au-delà de $\omega_c$ ; phase de $+90°$ à $0$.
- Aux basses fréquences, il se comporte en **dérivateur** ($s \approx \frac{1}{\omega_c}\frac{\mathrm de}{\mathrm dt}$) ; il supprime la composante continue (mode AC de l'oscilloscope).

## Filtres du second ordre

### Passe-bande (RLC, sortie sur R)

[[fig:p1-filtrage-3]]

$$\underline H = \frac{1}{1 + jQ\left(x - \dfrac1x\right)},\qquad x = \frac{\omega}{\omega_0}.$$

Gain maximal 1 (0 dB) en $\omega_0$, asymptotes $\pm20$ dB/décade, bande passante $\Delta\omega = \omega_0/Q$ : plus $Q$ est grand, plus le filtre est sélectif. Phase de $+90°$ à $-90°$, nulle en $\omega_0$.

### Passe-bas (RLC, sortie sur C)

$\underline H = \dfrac{1}{1 - x^2 + j\frac xQ}$ : 0 dB à basse fréquence, $-40$ dB/décade à haute fréquence, résonance (surtension) si $Q > \frac{1}{\sqrt2}$ ; en $\omega_0$, $|\underline H| = Q$ et $\varphi = -90°$. Le choix $Q = \frac{1}{\sqrt2}$ donne la réponse la plus plate (Butterworth).

Un filtre d'ordre $n$ a des asymptotes de pente $\pm20n$ dB/décade : un ordre élevé est plus sélectif.

## Action sur un signal

[[fig:p1-filtrage-4]]

> **Méthode — Filtrer un signal périodique.** Décomposer le signal en série de Fourier, appliquer $\underline H$ à chaque harmonique (module et phase), puis recomposer. Un passe-bas de coupure bien inférieure à la fréquence du signal ne garde que la valeur moyenne ; un passe-bande étroit centré sur un harmonique l'isole.

Cas usuels : un créneau dans un intégrateur donne un triangle ; un triangle dans un dérivateur donne un créneau.

## Associations et impédances

- **Filtres en cascade** : $\underline H = \underline H_1\underline H_2$ (gains en dB qui s'ajoutent) **seulement si** le second ne charge pas le premier (impédance d'entrée du second très grande devant l'impédance de sortie du premier).
- Impédance d'entrée $\underline Z_e = \frac{\underline e}{\underline i_e}$ ; impédance de sortie : celle du modèle de Thévenin vu de la sortie.

## Exemple corrigé

**Énoncé.** Un signal $e(t) = 2 + 3\cos(2\pi\cdot50\,t) + \cos(2\pi\cdot5000\,t)$ (en V) entre dans un passe-bas du 1er ordre de fréquence de coupure 500 Hz. Que vaut approximativement la sortie ?

**Solution.**
1. On traite chaque composante séparément (linéarité).
2. Composante continue : $|H(0)| = 1$, elle passe : 2 V.
3. 50 Hz $\ll f_c$ : $|H| \approx 1$, déphasage faible ($-6°$).
4. 5000 Hz $= 10f_c$ : $|H| \approx 0{,}1$ et déphasage $\approx -\pi/2$ ; il reste 0,1 V.
5. $s(t) \approx 2 + 3\cos(2\pi\cdot50\,t) + 0{,}1\cos(2\pi\cdot5000\,t - \pi/2)$.

## Exemple corrigé (choix d'un filtre)

**Énoncé.** On veut garder la composante continue d'un signal créneau de 1 kHz en atténuant le fondamental d'un facteur 100. Quelle fréquence de coupure pour un passe-bas d'ordre 1 ?

**Solution.** Au-delà de $f_c$, $|H| \approx \frac{f_c}{f}$ ; on veut $\frac{f_c}{1000} = 0{,}01$, soit $f_c = 10$ Hz (par exemple $R = 16$ kΩ et $C = 1$ µF).

## Pièges classiques

- Les formules supposent une sortie **ouverte** (aucun courant prélevé) ; une charge branchée en sortie modifie $\underline H$.
- « Intégrateur » et « dérivateur » ne sont valables que dans le domaine de fréquences de l'asymptote correspondante.
- Gains en dB qui s'ajoutent : seulement pour des filtres en cascade **non chargés**.
