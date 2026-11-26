---
titre: Régime sinusoïdal forcé
---
## L'essentiel

Un circuit linéaire alimenté par une source sinusoïdale atteint, après le régime transitoire, un régime où toutes les grandeurs sont sinusoïdales **à la fréquence de la source**. Les amplitudes complexes et les impédances transforment les équations différentielles en équations algébriques ; on étudie ensuite les résonances.

## Signaux sinusoïdaux

$u(t) = U_m\cos(\omega t + \varphi)$ : amplitude $U_m$, pulsation $\omega = 2\pi f$, phase à l'origine $\varphi$. Valeur efficace $U_{\text{eff}} = \frac{U_m}{\sqrt2}$ (c'est la valeur affichée par un voltmètre en mode AC).

Déphasage de $u_2$ par rapport à $u_1$ : $\Delta\varphi = \varphi_2 - \varphi_1$ ; mesuré sur un oscillogramme par $\Delta\varphi = 2\pi\frac{\Delta t}{T}$ (avance si $u_2$ atteint son maximum avant $u_1$). En phase, en quadrature ($\pm\frac\pi2$), en opposition ($\pi$).

## Représentation complexe

À $u(t) = U_m\cos(\omega t + \varphi)$ on associe $\underline u = U_me^{j(\omega t + \varphi)} = \underline U_me^{j\omega t}$, avec l'amplitude complexe $\underline U_m = U_me^{j\varphi}$ ; $u = \operatorname{Re}\underline u$. Dériver revient à multiplier par $j\omega$, intégrer à diviser par $j\omega$.

> **Définition — Impédances.** $\underline Z = \frac{\underline U_m}{\underline I_m}$ (convention récepteur) : $\underline Z_R = R$, $\underline Z_C = \dfrac1{jC\omega}$, $\underline Z_L = jL\omega$. Elles s'associent comme des résistances (série : somme ; parallèle : somme des admittances $\underline Y = \frac{1}{\underline Z}$). Les lois de Kirchhoff, diviseurs de tension et de courant s'écrivent en complexes.

- $|\underline Z|$ est le rapport des amplitudes ; $\arg\underline Z$ est l'avance de $u$ sur $i$.
- Comportements limites : à basse fréquence, $C$ est un interrupteur ouvert et $L$ un fil ; à haute fréquence, l'inverse.

[[fig:p1-sinusoidal-1]]

Dans le diagramme de Fresnel du RLC série, $\vec U_L$ est en avance de $\pi/2$ sur $\vec I$, $\vec U_C$ en retard de $\pi/2$ ; $\varphi$ est l'avance de $u$ sur $i$.

## Résonance en intensité (RLC série)

$\underline Z = R + j\left(L\omega - \frac{1}{C\omega}\right)$, d'où
$$I_m = \frac{E_m}{\sqrt{R^2 + \left(L\omega - \frac1{C\omega}\right)^2}} = \frac{E_m/R}{\sqrt{1 + Q^2\left(x - \frac1x\right)^2}},\qquad x = \frac{\omega}{\omega_0}.$$

[[fig:p1-sinusoidal-2]]

> **Propriété — Résonance en intensité.** Elle a lieu **toujours** en $\omega = \omega_0 = \frac{1}{\sqrt{LC}}$, où $I_m = E_m/R$ et $u$, $i$ sont en phase. La bande passante à $-3$ dB (où $I_m = I_{\max}/\sqrt2$) vaut $\Delta\omega = \omega_2 - \omega_1 = \omega_0/Q$ : plus $Q$ est grand, plus la résonance est aiguë.

Déphasage : $\varphi_i - \varphi_e = -\arctan\left(Q\left(x - \frac1x\right)\right)$, de $+\frac\pi2$ à $-\frac\pi2$, nul à la résonance.

## Résonance en tension aux bornes de C

[[fig:p1-sinusoidal-3]]

$$\frac{U_{Cm}}{E_m} = \frac1{\sqrt{\left(1 - x^2\right)^2 + \left(\frac xQ\right)^2}}.$$

Il n'y a résonance que si $Q > 1/\sqrt2$, en $x_r = \sqrt{1 - \frac1{2Q^2}} < 1$ ; pour $Q \gg 1$, la surtension en $\omega_0$ vaut $Q\,E_m$. À basse fréquence $U_C \to E_m$, à haute fréquence $U_C \to 0$.

## Analogie mécanique

Oscillateur masse-ressort amorti forcé par $F_m\cos\omega t$ : l'**élongation** joue le rôle de $u_C$ (résonance seulement si $Q > \frac{1}{\sqrt2}$), la **vitesse** celui de $i$ (résonance toujours en $\omega_0$).

## Puissance

- Puissance instantanée $p = ui$ ; puissance moyenne reçue par un dipôle : $P = U_{\text{eff}}I_{\text{eff}}\cos\varphi = \frac12\operatorname{Re}(\underline U_m\underline I_m^*)$ ; $\cos\varphi$ est le **facteur de puissance**.
- Une résistance reçoit $RI_{\text{eff}}^2$ ; un condensateur ou une bobine idéaux reçoivent une puissance moyenne **nulle**.
- Au RLC série, la puissance moyenne reçue est maximale à la résonance en intensité.

## Méthode

1. Passer en complexes (impédances), utiliser lois de Kirchhoff, diviseurs, associations.
2. Mettre le résultat sous forme canonique faisant apparaître $\omega_0$ et $Q$.
3. Module pour l'amplitude, argument pour la phase ; ne revenir en réel qu'à la fin.

## Exemple corrigé

**Énoncé.** Un dipôle RC série ($R = 1$ kΩ, $C = 1$ µF) est alimenté par $e(t) = 10\cos(1000t)$ (en V). Calculer l'amplitude du courant et son déphasage par rapport à $e$.

**Solution.**
1. $\underline Z = R + \dfrac{1}{jC\omega} = 1000 - 1000j$ (en Ω).
2. $|\underline Z| = 1000\sqrt2 \approx 1{,}41$ kΩ, d'où $I_m = E_m/|\underline Z| \approx 7{,}1$ mA.
3. $\arg\underline I = -\arg\underline Z = +\pi/4$ : le courant est **en avance** de $\pi/4$ sur la tension (comportement capacitif). Puissance moyenne : $\frac12RI_m^2 \approx 25$ mW.

## Exemple corrigé (bande passante)

**Énoncé.** RLC série avec $L = 10$ mH, $C = 100$ nF, $R = 10$ Ω. Fréquence de résonance et bande passante ?

**Solution.** $\omega_0 = \frac{1}{\sqrt{LC}} = 3{,}2\cdot10^4$ rad·s⁻¹, $f_0 \approx 5{,}0$ kHz. $Q = \frac1R\sqrt{\frac LC} \approx 32$. $\Delta f = \frac{f_0}{Q} \approx 160$ Hz : résonance très sélective.

## Pièges classiques

- On ne prend la partie réelle qu'à la fin ; on n'additionne pas des amplitudes réelles de signaux déphasés.
- Ne pas confondre les deux résonances : en intensité toujours en $\omega_0$, en tension seulement pour $Q > 1/\sqrt2$.
- La notation complexe n'est valable qu'en **régime établi** et pour des systèmes linéaires.
