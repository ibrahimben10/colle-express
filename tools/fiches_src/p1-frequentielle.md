---
titre: Analyse fréquentielle d'un système linéaire
---
## L'essentiel

Tout signal périodique se décompose en une somme de sinusoïdes (série de Fourier). Un système linéaire traite chaque composante séparément, selon sa **fonction de transfert** $\underline H(j\omega)$.

## Spectre d'un signal périodique

$$s(t) = A_0 + \sum_{n\geq1}A_n\cos(n\omega t + \varphi_n).$$
$A_0$ est la valeur moyenne ; la composante de rang $n$ est l'harmonique $n$, de fréquence $nf$.

[[fig:p1-frequentielle-1]]

Un créneau impair d'amplitude $E$ ne contient que des harmoniques **impaires**, d'amplitudes $\dfrac{4E}{n\pi}$ : elles décroissent en $1/n$. Plus un signal a des variations brutales, plus son spectre est riche en hautes fréquences.

## Fonction de transfert et Bode

> **Définition — Gain et phase.** $\underline H = \underline s/\underline e$ ; gain en décibels $G_{\text{dB}} = 20\log|\underline H|$ ; phase $\varphi = \arg\underline H$.

[[fig:p1-frequentielle-2]]

Le diagramme de Bode trace $G_{\text{dB}}$ et $\varphi$ en fonction de $\log\omega$. On le construit à partir des **asymptotes** (pentes multiples de 20 dB par décade) puis on place les points remarquables : la coupure à $-3$ dB correspond à $|\underline H| = H_{\max}/\sqrt2$.

## Méthode

1. Écrire $\underline H$ sous forme canonique (diviseur de tension, impédances).
2. Étudier les comportements limites $\omega \to 0$ et $\omega \to \infty$ : ils donnent les asymptotes.
3. Pour un signal d'entrée donné, multiplier chaque raie par $|\underline H(n\omega)|$ et la déphaser de $\arg\underline H(n\omega)$.

## Exemple corrigé

**Énoncé.** Pour le filtre RC (sortie aux bornes de C), avec $R = 10$ kΩ et $C = 10$ nF, donner la fonction de transfert, la pulsation de coupure et le gain en dB à $f = 16$ kHz.

**Solution.**
1. Pont diviseur : $\underline H = \dfrac{1}{1 + jRC\omega}$, passe-bas du 1er ordre.
2. $\omega_c = 1/(RC) = 10^4$ rad·s⁻¹, soit $f_c \approx 1{,}6$ kHz.
3. À $f = 10f_c$ : $|\underline H| \approx 1/10$, $G_{dB} \approx -20$ dB (une décade au-dessus de $f_c$, l'asymptote descend de 20 dB).

## Pièges classiques

- $20\log$ pour une amplitude, $10\log$ pour une puissance.
- Une décade correspond à une fréquence multipliée par 10, une octave par 2 (−6 dB/octave = −20 dB/décade).
