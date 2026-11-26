---
titre: Particule chargée dans un champ électrique ou magnétique
---
## L'essentiel

Une particule de charge $q$ subit la **force de Lorentz** $\vec F = q(\vec E + \vec v\wedge\vec B)$. Le poids est en général négligeable devant cette force.

## Champ électrique uniforme

[[fig:p2-charge-1]]

Le mouvement est analogue à une chute libre avec $\vec g$ remplacé par $q\vec E/m$ : trajectoire **parabolique** si $\vec v_0$ n'est pas colinéaire à $\vec E$.

> **Propriété — Accélération sous une tension $U$.** La force électrique dérive de l'énergie potentielle $qV$ : $\tfrac12mv^2 - \tfrac12mv_0^2 = q(V_A - V_B) = qU$.

## Champ magnétique uniforme

> **Propriété — La force magnétique ne travaille pas.** $\vec F\cdot\vec v = 0$ : la norme de la vitesse est constante.

[[fig:p2-charge-2]]

Si $\vec v_0 \perp \vec B$, le mouvement est **circulaire uniforme** de rayon et de pulsation
$$R = \frac{mv_0}{|q|B},\qquad \omega_c = \frac{|q|B}{m}.$$
Le sens de rotation dépend du signe de $q$ ; la période ne dépend pas de la vitesse (principe du cyclotron).

[[fig:p2-charge-3]]

Si $\vec v_0$ a une composante selon $\vec B$, elle est conservée : la trajectoire est une **hélice**.

## Applications

Spectromètre de masse (séparer des ions de $m/q$ différents par leur rayon), cyclotron, déflexion d'un faisceau d'électrons.

## Exemple corrigé

**Énoncé.** Un électron, d'énergie cinétique initiale négligeable, est accéléré sous une tension $U = 1$ kV, puis entre dans un champ magnétique uniforme $B = 1$ mT perpendiculaire à sa vitesse. Calculer sa vitesse et le rayon de sa trajectoire.

**Solution.**
1. Théorème de l'énergie cinétique : $\tfrac12mv^2 = eU$, donc $v = \sqrt{2eU/m} \approx 1{,}9\cdot10^7$ m·s⁻¹ (non relativiste).
2. Dans $\vec B$, la force de Lorentz ne travaille pas : mouvement circulaire uniforme de rayon $R = \dfrac{mv}{eB}$.
3. $R = \dfrac{9{,}1\cdot10^{-31}\times1{,}9\cdot10^7}{1{,}6\cdot10^{-19}\times10^{-3}} \approx 11$ cm.

## Pièges classiques

- Le sens de la force pour un électron ($q = -e$) est opposé à $\vec E$.
- Le produit vectoriel : vérifier le sens de $\vec v\wedge\vec B$ par la règle de la main droite.
