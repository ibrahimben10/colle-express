---
titre: Particule chargée dans un champ électrique ou magnétique
---
## L'essentiel

Une particule de charge $q$ subit la **force de Lorentz** $\vec F = q(\vec E + \vec v\wedge\vec B)$. Le poids est en général négligeable devant cette force. Un champ électrique accélère ou dévie la particule ; un champ magnétique ne modifie que la direction de sa vitesse.

## Force de Lorentz

- Charge élémentaire $e = 1{,}6\cdot10^{-19}$ C ; électron $m_e = 9{,}1\cdot10^{-31}$ kg, proton $m_p = 1{,}67\cdot10^{-27}$ kg.
- Ordre de grandeur : pour un électron dans $E = 10^4$ V·m⁻¹, $eE \approx 10^{-15}$ N, contre $m_eg \approx 10^{-29}$ N pour le poids.
- Puissance : $\mathcal P = q\vec E\cdot\vec v$ (la partie magnétique ne travaille pas).
- Énergie potentielle électrique : $E_p = qV$ ; l'électron-volt : $1$ eV $= 1{,}6\cdot10^{-19}$ J.

## Champ électrique uniforme

[[fig:p2-charge-1]]

Le mouvement est analogue à une chute libre avec $\vec g$ remplacé par $q\vec E/m$ : mouvement rectiligne uniformément accéléré si $\vec v_0$ est colinéaire à $\vec E$, trajectoire **parabolique** sinon.

> **Propriété — Accélération sous une tension $U$.** La force électrique dérive de l'énergie potentielle $qV$ : $\tfrac12mv^2 - \tfrac12mv_0^2 = q(V_A - V_B) = qU$.

Entre deux plaques planes distantes de $d$ sous la tension $U$ : $E = \frac Ud$, dirigé vers les potentiels décroissants. **Déviation** d'un faisceau : en sortie d'un condensateur de longueur $L$, l'électron a été dévié d'un angle $\tan\alpha = \frac{eEL}{mv_0^2}$ (principe de l'oscilloscope analogique).

## Champ magnétique uniforme

> **Propriété — La force magnétique ne travaille pas.** $\vec F\cdot\vec v = 0$ : la norme de la vitesse (et l'énergie cinétique) est constante.

[[fig:p2-charge-2]]

Si $\vec v_0 \perp \vec B$, le mouvement est **circulaire uniforme** de rayon et de pulsation
$$R = \frac{mv_0}{|q|B},\qquad \omega_c = \frac{|q|B}{m}\ \text{(pulsation cyclotron)}.$$

Démonstration : le mouvement est plan (pas de force selon $\vec B$) ; force de norme constante $|q|vB$ perpendiculaire à $\vec v$ ; PFD en base de Frenet : $m\frac{v^2}{R} = |q|vB$. Le sens de rotation dépend du signe de $q$ ; la période $T = \frac{2\pi m}{|q|B}$ ne dépend pas de la vitesse.

[[fig:p2-charge-3]]

Si $\vec v_0$ a une composante $v_\parallel$ selon $\vec B$, elle est conservée : la trajectoire est une **hélice** de rayon $\frac{mv_\perp}{|q|B}$ et de pas $v_\parallel T$.

## Applications

- **Spectromètre de masse** : des ions accélérés sous la même tension $U$ ont $R = \frac1B\sqrt{\frac{2mU}{q}}$ : on sépare les isotopes.
- **Cyclotron** : deux « dés » où règne $\vec B$, séparés par un intervalle où un champ électrique alternatif à la fréquence cyclotron accélère les particules à chaque demi-tour ; le rayon augmente à chaque passage.
- **Filtre de Wien** : $\vec E \perp \vec B$, seules les particules de vitesse $v = \frac EB$ passent sans déviation.
- Aurores polaires : particules guidées en hélice le long du champ terrestre.

## Méthode

1. Vérifier que le poids est négligeable.
2. Champ électrique seul : PFD (comme une chute libre) ou théorème de l'énergie cinétique pour une vitesse.
3. Champ magnétique seul : $v$ constante ; mouvement circulaire si $\vec v_0 \perp \vec B$ ; sens de rotation par la règle de la main droite appliquée à $q\vec v\wedge\vec B$.
4. Équations couplées en cartésiennes : poser $\underline u = \dot x + i\dot y$ pour les résoudre.

## Exemple corrigé

**Énoncé.** Un électron, de vitesse initiale négligeable, est accéléré sous $U = 1$ kV, puis entre dans un champ $B = 1$ mT perpendiculaire à sa vitesse. Vitesse et rayon ?

**Solution.**
1. $\tfrac12mv^2 = eU$, donc $v = \sqrt{2eU/m} \approx 1{,}9\cdot10^7$ m·s⁻¹ (non relativiste : $v < 0{,}1c$).
2. Mouvement circulaire uniforme de rayon $R = \dfrac{mv}{eB} \approx 11$ cm.

## Exemple corrigé (isotopes)

**Énoncé.** Des ions ³⁵Cl⁻ et ³⁷Cl⁻ sont accélérés sous la même tension puis décrivent un demi-cercle dans $\vec B$. Rapport des rayons ?

**Solution.** $R \propto \sqrt m$ : $\frac{R_{37}}{R_{35}} = \sqrt{\frac{37}{35}} \approx 1{,}028$ ; les points d'impact sont séparés de $2(R_{37} - R_{35})$.

## Pièges classiques

- Le sens de la force pour un électron ($q = -e$) est opposé à $\vec E$.
- Produit vectoriel : vérifier le sens de $\vec v\wedge\vec B$ par la règle de la main droite, puis tenir compte du signe de $q$.
- Le rayon dépend de la vitesse, la période non.
