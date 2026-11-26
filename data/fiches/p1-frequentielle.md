---
titre: Analyse fréquentielle d'un système linéaire
---
## L'essentiel

Tout signal périodique se décompose en une somme de sinusoïdes (série de Fourier). Un système linéaire traite chaque composante séparément, selon sa **fonction de transfert** $\underline H(j\omega)$ ; le diagramme de Bode résume ce comportement.

## Spectre d'un signal périodique

$$s(t) = A_0 + \sum_{n\geq1}A_n\cos(n\omega t + \varphi_n).$$

- $A_0$ est la **valeur moyenne** $\langle s\rangle = \frac1T\int_0^Ts(t)\,\mathrm dt$ ; la composante $n = 1$ est le **fondamental**, celle de rang $n$ l'harmonique $n$, de fréquence $nf$.
- Le **spectre** représente $A_n$ en fonction de $nf$ (raies).
- Valeur efficace : $S_{\text{eff}}^2 = \langle s^2\rangle = A_0^2 + \sum\frac{A_n^2}{2}$ (formule de Parseval).

[[fig:p1-frequentielle-1]]

| Signal (amplitude $E$, impair ou pair) | Harmoniques | Amplitudes |
|---|---|---|
| sinusoïde | fondamental seul | $E$ |
| créneau | rangs impairs | $\frac{4E}{n\pi}$ (en $\frac1n$) |
| triangle | rangs impairs | $\frac{8E}{n^2\pi^2}$ (en $\frac{1}{n^2}$) |

Plus un signal a des variations brutales, plus son spectre est riche en hautes fréquences ; un signal plus « lisse » a des harmoniques qui décroissent plus vite. Un signal non périodique a un spectre continu ; la largeur spectrale $\Delta f$ et la durée $\Delta t$ vérifient $\Delta f\,\Delta t \sim 1$.

## Système linéaire

Un système est linéaire si sa réponse à $a e_1 + b e_2$ est $a s_1 + b s_2$ ; il est régi par une équation différentielle linéaire à coefficients constants. En régime sinusoïdal établi, la sortie a la **même fréquence** que l'entrée. Un système non linéaire (diode, saturation) crée des harmoniques absentes de l'entrée.

## Fonction de transfert et Bode

> **Définition — Gain et phase.** $\underline H(j\omega) = \underline s/\underline e$ ; gain $G = |\underline H|$, gain en décibels $G_{\text{dB}} = 20\log|\underline H|$ ; phase $\varphi = \arg\underline H$ (avance de la sortie sur l'entrée).

[[fig:p1-frequentielle-2]]

Le diagramme de Bode trace $G_{\text{dB}}$ et $\varphi$ en fonction de $\log\omega$ (ou $\log f$).

- On le construit à partir des **asymptotes** : pentes multiples de 20 dB par décade (un facteur $(j\omega)^n$ donne $20n$ dB/décade).
- La coupure à $-3$ dB correspond à $|\underline H| = H_{\max}/\sqrt2$ ; la **bande passante** est l'intervalle où $G_{\text{dB}} \ge G_{\max} - 3$ dB.
- Lien avec l'équation différentielle : remplacer $j\omega$ par $\frac{\mathrm d}{\mathrm dt}$. Par exemple $\underline H = \frac{1}{1 + j\omega\tau}$ correspond à $\tau\dot s + s = e$.

### Formes canoniques

| Type | $\underline H$ |
|---|---|
| passe-bas d'ordre 1 | $\frac{H_0}{1 + j\frac{\omega}{\omega_c}}$ |
| passe-haut d'ordre 1 | $H_0\frac{j\frac{\omega}{\omega_c}}{1 + j\frac{\omega}{\omega_c}}$ |
| passe-bas d'ordre 2 | $\frac{H_0}{1 - x^2 + j\frac xQ}$ |
| passe-bande d'ordre 2 | $\frac{H_0}{1 + jQ\left(x - \frac1x\right)}$ |

## Méthode

1. Écrire $\underline H$ sous forme canonique (diviseur de tension, impédances).
2. Étudier les comportements limites $\omega \to 0$ et $\omega \to \infty$ : ils donnent les asymptotes et le type de filtre (on peut le prévoir en remplaçant $C$ et $L$ par fils ou interrupteurs ouverts).
3. Pour un signal d'entrée donné, multiplier chaque raie par $|\underline H(n\omega)|$ et la déphaser de $\arg\underline H(n\omega)$ (linéarité).

## Exemple corrigé

**Énoncé.** Pour le filtre RC (sortie aux bornes de C), avec $R = 10$ kΩ et $C = 10$ nF, donner la fonction de transfert, la pulsation de coupure et le gain en dB à $f = 16$ kHz.

**Solution.**
1. Pont diviseur : $\underline H = \dfrac{1}{1 + jRC\omega}$, passe-bas du 1er ordre.
2. $\omega_c = 1/(RC) = 10^4$ rad·s⁻¹, soit $f_c \approx 1{,}6$ kHz.
3. À $f = 10f_c$ : $|\underline H| \approx 1/10$, $G_{dB} \approx -20$ dB, $\varphi \approx -84°$.

## Exemple corrigé (valeur efficace)

**Énoncé.** Valeur efficace de $s(t) = 2 + 3\cos(\omega t)$ ?

**Solution.** $S_{\text{eff}}^2 = 2^2 + \frac{3^2}{2} = 8{,}5$, donc $S_{\text{eff}} \approx 2{,}9$ V (et non $\sqrt{2^2 + 3^2}$).

## Pièges classiques

- $20\log$ pour une amplitude, $10\log$ pour une puissance.
- Une décade correspond à une fréquence multipliée par 10, une octave par 2 (−6 dB/octave = −20 dB/décade).
- Le gain maximal n'est pas toujours 0 dB.
