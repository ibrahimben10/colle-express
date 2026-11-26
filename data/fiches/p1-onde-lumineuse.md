---
titre: Onde lumineuse
---
## L'essentiel

La lumière est une onde électromagnétique. Dans un milieu transparent d'indice $n$, elle se propage à la vitesse $v = c/n$. Le visible s'étend de 400 nm (violet) à 800 nm (rouge) environ. Les sources se distinguent par leur spectre, et la diffraction marque la limite de l'optique géométrique.

[[fig:p1-onde-lumineuse-1]]

## Le spectre électromagnétique

Des ondes radio (longueurs d'onde métriques et plus) aux rayons gamma ($< 10^{-11}$ m), en passant par les micro-ondes, l'infrarouge, le visible, l'ultraviolet et les rayons X. Toutes se propagent dans le vide à $c = 3{,}00\cdot10^8$ m·s⁻¹ ; $\lambda = \frac cf$ et l'énergie d'un photon vaut $h\nu$.

## Indice et longueur d'onde

> **Définition — Indice optique.** $n = c/v \geq 1$. Dans un milieu d'indice $n$, la fréquence est inchangée et la longueur d'onde devient $\lambda = \lambda_0/n$.

- Un milieu est **dispersif** si $n$ dépend de $\lambda$ ; la loi de Cauchy en donne une approximation : $n(\lambda) = A + B/\lambda^2$ ($B > 0$ : le bleu est plus dévié que le rouge).
- **Chemin optique** le long d'un trajet de longueur $\ell$ dans un milieu d'indice $n$ : $L = n\ell$ ; c'est la distance qu'aurait parcourue la lumière dans le vide pendant la même durée. La durée vaut $\frac{L}{c}$.

## Sources de lumière

- Spectre **continu** : corps chaud (lampe à incandescence, Soleil) ; le maximum d'émission vérifie la loi de Wien $\lambda_{\max}T \approx 2{,}9\cdot10^{-3}$ m·K.
- Spectre **de raies** : lampe spectrale (vapeur de mercure, sodium : doublet jaune à 589 nm) ; chaque raie correspond à une transition entre niveaux d'énergie.
- **Laser** : quasi monochromatique, directif, cohérent, de grande puissance surfacique (sécurité : ne jamais viser l'œil).
- **Modèle du train d'onde** : une source émet des trains d'onde de durée finie $\tau_c$ (temps de cohérence) ; la largeur spectrale vérifie $\Delta\nu\,\tau_c \approx 1$ ; longueur de cohérence $\ell_c = c\tau_c$ (quelques µm pour la lumière blanche, quelques mm à cm pour une lampe spectrale, plusieurs mètres pour un laser).

## Détecteurs

Les détecteurs (œil, photodiode, capteur CCD) sont sensibles à la puissance moyenne reçue, c'est-à-dire à l'**intensité** (éclairement), proportionnelle au carré moyen de l'amplitude de l'onde. Leur temps de réponse (ms pour l'œil, ns pour une photodiode) est très grand devant la période lumineuse ($\sim10^{-15}$ s).

## Diffraction

[[fig:p1-onde-lumineuse-2]]

> **Propriété — Diffraction par une ouverture de taille $a$.** Le faisceau s'élargit d'un demi-angle $\theta \approx \lambda/a$ (en radians), significatif dès que $a$ n'est plus grand devant $\lambda$.

- Sur un écran à la distance $D$, la tache centrale a une largeur $\ell \approx 2\lambda D/a$ : plus la fente est étroite, plus la tache est large.
- Ouverture circulaire de diamètre $d$ : $\sin\theta \approx 1{,}22\frac{\lambda}{d}$ (tache d'Airy) ; c'est ce qui limite la résolution des télescopes et microscopes.
- Une fente fine diffracte perpendiculairement à sa grande dimension.

## Exemple corrigé

**Énoncé.** Une lumière de longueur d'onde $\lambda_0 = 600$ nm dans le vide passe dans un verre d'indice $n = 1{,}5$. Que deviennent sa fréquence, sa vitesse et sa longueur d'onde ?

**Solution.**
1. La fréquence est fixée par la source : $\nu = c/\lambda_0 = 5{,}0\cdot10^{14}$ Hz.
2. $v = c/n = 2{,}0\cdot10^8$ m·s⁻¹.
3. $\lambda = \lambda_0/n = 400$ nm. La couleur perçue est liée à la fréquence, pas à $\lambda$ dans le milieu.

## Exemple corrigé (mesure par diffraction)

**Énoncé.** Un laser de 633 nm éclaire un cheveu ; sur un écran à 2,0 m, la tache centrale mesure 3,2 cm. Diamètre du cheveu ?

**Solution.** Un fil diffracte comme une fente de même largeur : $\ell = \frac{2\lambda D}{a}$, d'où $a = \frac{2\lambda D}{\ell} \approx 79$ µm.

## Pièges classiques

- $\theta \approx \lambda/a$ est un **demi**-angle ; la largeur angulaire totale de la tache centrale vaut $2\lambda/a$.
- La diffraction n'est pas propre à la lumière : elle concerne toutes les ondes (son, houle, électrons).
- Un détecteur ne mesure pas l'amplitude instantanée mais une intensité moyenne.

## Ordres de grandeur

Laser rouge $\lambda = 633$ nm, fente $a = 0{,}1$ mm, écran à $D = 2$ m : $\theta \approx 6\cdot10^{-3}$ rad et $\ell \approx 2{,}5$ cm. Période lumineuse : $2\cdot10^{-15}$ s.
