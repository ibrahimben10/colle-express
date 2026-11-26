---
titre: Régime sinusoïdal forcé
---
## L'essentiel

Un circuit linéaire alimenté par une source sinusoïdale atteint, après le régime transitoire, un régime où toutes les grandeurs sont sinusoïdales **à la fréquence de la source**. Les amplitudes complexes transforment les équations différentielles en équations algébriques.

## Représentation complexe

À $u(t) = U_m\cos(\omega t + \varphi)$ on associe $\underline u = U_me^{j(\omega t + \varphi)}$ ; dériver revient à multiplier par $j\omega$.

> **Définition — Impédances.** $\underline Z_R = R$, $\underline Z_C = \dfrac1{jC\omega}$, $\underline Z_L = jL\omega$. Elles s'associent comme des résistances.

[[fig:p1-sinusoidal-1]]

Dans le diagramme de Fresnel du RLC série, $\vec U_L$ est en avance de $\pi/2$ sur $\vec I$, $\vec U_C$ en retard de $\pi/2$ ; $\varphi$ est l'avance de $u$ sur $i$.

## Résonance en intensité (RLC série)

$$I_m = \frac{E_m}{\sqrt{R^2 + \left(L\omega - \frac1{C\omega}\right)^2}}.$$

[[fig:p1-sinusoidal-2]]

> **Propriété — Résonance en intensité.** Elle a lieu **toujours** en $\omega = \omega_0$, où $I_m = E_m/R$ et $u$, $i$ sont en phase. La bande passante à $-3$ dB vaut $\Delta\omega = \omega_0/Q$.

## Résonance en tension aux bornes de C

[[fig:p1-sinusoidal-3]]

$$\frac{U_{Cm}}{E_m} = \frac1{\sqrt{\left(1 - x^2\right)^2 + \left(\frac xQ\right)^2}},\qquad x = \frac{\omega}{\omega_0}.$$
Il n'y a résonance que si $Q > 1/\sqrt2$, en $x_r = \sqrt{1 - \frac1{2Q^2}} < 1$.

## Puissance

Puissance moyenne reçue par un dipôle : $P = U_{\text{eff}}I_{\text{eff}}\cos\varphi$, avec $U_{\text{eff}} = U_m/\sqrt2$. Seules les résistances consomment de la puissance en moyenne.

## Exemple corrigé

**Énoncé.** Un dipôle RC série ($R = 1$ kΩ, $C = 1$ µF) est alimenté par $e(t) = 10\cos(1000t)$ (en V). Calculer l'amplitude du courant et son déphasage par rapport à $e$.

**Solution.**
1. Impédance complexe : $\underline Z = R + \dfrac{1}{jC\omega} = 1000 - 1000j$ (en Ω).
2. $|\underline Z| = 1000\sqrt2 \approx 1{,}41$ kΩ, d'où $I_m = E_m/|\underline Z| \approx 7{,}1$ mA.
3. $\arg\underline I = -\arg\underline Z = +\pi/4$ : le courant est **en avance** de $\pi/4$ sur la tension (comportement capacitif).

## Pièges classiques

- On ne prend la partie réelle qu'à la fin ; on n'additionne pas des amplitudes réelles de signaux déphasés.
- Ne pas confondre les deux résonances : en intensité toujours en $\omega_0$, en tension seulement pour $Q > 1/\sqrt2$.
