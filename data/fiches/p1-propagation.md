---
titre: Propagation d'un signal
---
## L'essentiel

Un **signal** est une grandeur physique qui transporte une information. Une **onde progressive** est la propagation d'une perturbation sans transport global de matière, avec une célérité $c$ qui dépend du milieu. Une onde sinusoïdale présente une double périodicité, temporelle et spatiale.

## Exemples de signaux et d'ondes

- Ondes mécaniques : son (surpression dans un fluide), ondes sur une corde, ondes sismiques, houle. Elles nécessitent un milieu matériel.
- Ondes électromagnétiques : lumière, ondes radio ; elles se propagent aussi dans le vide.
- Onde **transversale** (perturbation perpendiculaire à la propagation : corde) ou **longitudinale** (parallèle : son).
- Domaines du son audible : 20 Hz – 20 kHz ; ultrasons au-delà, infrasons en deçà.

[[fig:p1-propagation-1]]

## Onde progressive à une dimension

> **Définition — Onde progressive.** Une onde se propageant sans déformation dans le sens des $x$ croissants s'écrit $s(x,t) = f(t - x/c)$, ou de façon équivalente $g(x - ct)$. Dans le sens des $x$ décroissants : $f(t + x/c)$.

Le signal en $x$ reproduit, avec le **retard** $\tau = x/c$, le signal émis en $x = 0$ :
$$s(x,t) = s(0,\, t - x/c).$$

Le profil spatial à l'instant $t + \Delta t$ est celui de l'instant $t$ translaté de $c\Delta t$.

## Onde progressive sinusoïdale

$$s(x,t) = S_m\cos(\omega t - kx + \varphi),\qquad k = \frac{2\pi}{\lambda} = \frac{\omega}{c}.$$

[[fig:p1-propagation-2]]

> **Propriété — Double périodicité.** Période temporelle $T = 2\pi/\omega$, période spatiale (longueur d'onde) $\lambda = 2\pi/k$, reliées par $\lambda = cT = c/f$. Le vecteur d'onde $k$ est en rad·m⁻¹.

- Déphasage entre deux points distants de $d$ (même instant) : $\Delta\varphi = kd = 2\pi d/\lambda$ ; points en phase si $d = p\lambda$, en opposition si $d = (p + \tfrac12)\lambda$.
- Le retard et le déphasage sont liés : $\Delta\varphi = \omega\tau$.

## Célérité, dispersion, atténuation

- La célérité dépend des propriétés du milieu : pour une corde, $c = \sqrt{T/\mu}$ (tension sur masse linéique) ; pour le son dans un gaz parfait, $c = \sqrt{\gamma RT/M}$.
- Un milieu est **dispersif** si $c$ dépend de la fréquence : un signal non sinusoïdal se déforme (exemple : houle, lumière dans le verre).
- Un milieu **absorbant** atténue l'amplitude au cours de la propagation.
- L'intensité sonore se mesure en décibels : $L = 10\log\frac{I}{I_0}$ avec $I_0 = 10^{-12}$ W·m⁻² ; doubler l'intensité ajoute 3 dB.

## Diffraction

Une onde de longueur d'onde $\lambda$ qui traverse une ouverture de taille $a$ diverge avec un demi-angle $\theta \approx \frac{\lambda}{a}$ (en radians). L'effet est notable quand $a$ n'est pas grand devant $\lambda$ : on entend derrière une porte (son, $\lambda \sim 1$ m), la lumière ($\lambda \sim 0{,}5$ µm) ne diffracte que par de très petites ouvertures.

## Méthode

- Pour lire un retard sur deux enregistrements : repérer le même motif, mesurer le décalage $\tau$, puis $c = d/\tau$.
- Pour écrire l'onde : identifier le sens de propagation (signe devant $kx$), puis $\omega$, $k$, la phase avec une condition.
- Distinguer graphe $s(x)$ à $t$ fixé (période $\lambda$) et graphe $s(t)$ à $x$ fixé (période $T$).

## Exemple corrigé

**Énoncé.** Une onde progressive sinusoïdale se propage le long d'une corde à $c = 4$ m·s⁻¹ dans le sens des $x$ croissants, avec $f = 2$ Hz et une amplitude $A = 1$ cm. Écrire $y(x,t)$ et calculer le retard entre deux points distants de 1,5 m.

**Solution.**
1. $\lambda = c/f = 2$ m ; $k = 2\pi/\lambda = \pi$ rad·m⁻¹, $\omega = 2\pi f = 4\pi$ rad·s⁻¹.
2. $y(x,t) = A\cos(\omega t - kx)$, avec $A = 1$ cm.
3. Retard $\tau = d/c = 0{,}375$ s, soit un déphasage $kd = 1{,}5\pi$.

## Exemple corrigé (diffraction)

**Énoncé.** Un laser ($\lambda = 633$ nm) éclaire une fente de largeur $a = 0{,}1$ mm. Largeur de la tache centrale sur un écran à $D = 2$ m ?

**Solution.** $\theta \approx \frac{\lambda}{a} = 6{,}3\cdot10^{-3}$ rad ; largeur $2D\theta \approx 2{,}5$ cm.

## Pièges classiques

- Le profil spatial et le signal temporel sont **inversés** l'un par rapport à l'autre : le front avant de l'onde dans l'espace est le début du signal dans le temps.
- En changeant de milieu, $f$ est conservée, $\lambda$ change.
- Le milieu ne se déplace pas avec l'onde : c'est l'énergie et l'information qui se propagent.

## Ordres de grandeur

| Onde | Célérité |
|---|---|
| son dans l'air (20 °C) | 343 m·s⁻¹ |
| son dans l'eau | 1 500 m·s⁻¹ |
| son dans l'acier | 5 000 m·s⁻¹ |
| lumière dans le vide | 3,00·10⁸ m·s⁻¹ |
| houle au large | 10 à 20 m·s⁻¹ |
