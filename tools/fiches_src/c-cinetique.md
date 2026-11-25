---
titre: Cinétique chimique
---
## L'essentiel

La cinétique étudie la vitesse des réactions. Pour une réaction d'ordre simple, la vitesse dépend des concentrations par une loi de puissance et de la température par la loi d'Arrhenius.

> **Définition — Vitesse volumique.** $v = \dfrac{1}{V}\dfrac{\mathrm d\xi}{\mathrm dt} = \dfrac{1}{\nu_i}\dfrac{\mathrm d[A_i]}{\mathrm dt}$ à volume constant.

Si la réaction admet un ordre : $v = k[A]^\alpha[B]^\beta$, d'ordre global $\alpha + \beta$.

## Lois de vitesse intégrées (réaction A → produits)

| Ordre | Loi | Temps de demi-réaction |
|---|---|---|
| 0 | $[A] = [A]_0 - kt$ | $\dfrac{[A]_0}{2k}$ |
| 1 | $\ln[A] = \ln[A]_0 - kt$ | $\dfrac{\ln2}{k}$, indépendant de $[A]_0$ |
| 2 | $\dfrac{1}{[A]} = \dfrac{1}{[A]_0} + kt$ | $\dfrac{1}{k[A]_0}$ |

[[fig:c-cinetique-1]]

## Méthodes

- **Méthode intégrale** : tracer la grandeur qui doit être affine en $t$ et vérifier par régression linéaire.
- **Dégénérescence de l'ordre** : un réactif en large excès garde une concentration quasi constante.
- **Méthode différentielle**, **temps de demi-réaction** pour plusieurs $[A]_0$.

## Loi d'Arrhenius

[[fig:c-cinetique-2]]

> **Loi d'Arrhenius.** $k = A\,e^{-E_a/(RT)}$ : $\ln k$ est une fonction affine de $1/T$, de pente $-E_a/R$.

[[fig:c-cinetique-3]]

L'énergie d'activation $E_a$ est la barrière à franchir. Un catalyseur abaisse cette barrière sans modifier l'état final.

## Pièges classiques

- Ordre et coefficients stœchiométriques ne coïncident que pour un acte élémentaire.
- Penser aux coefficients stœchiométriques dans la définition de $v$.
