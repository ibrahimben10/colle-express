---
titre: Propagation d'un signal
---
## L'essentiel

Un **signal** est une grandeur physique qui transporte une information. Une **onde progressive** est la propagation d'une perturbation sans transport global de matière, avec une célérité $c$.

[[fig:p1-propagation-1]]

## Onde progressive à une dimension

> **Définition — Onde progressive.** Une onde se propageant sans déformation dans le sens des $x$ croissants s'écrit $s(x,t) = f(t - x/c)$, ou de façon équivalente $g(x - ct)$. Dans le sens des $x$ décroissants : $f(t + x/c)$.

Le signal en $x$ reproduit, avec le **retard** $\tau = x/c$, le signal émis en $x = 0$ :
$$s(x,t) = s(0,\, t - x/c).$$

## Onde progressive sinusoïdale

$$s(x,t) = S_m\cos(\omega t - kx + \varphi),\qquad k = \frac{2\pi}{\lambda} = \frac{\omega}{c}.$$

[[fig:p1-propagation-2]]

> **Propriété — Double périodicité.** Période temporelle $T = 2\pi/\omega$, période spatiale (longueur d'onde) $\lambda = 2\pi/k$, reliées par $\lambda = cT = c/f$.

## Méthode

- Pour lire un retard sur deux enregistrements : repérer le même motif, mesurer le décalage $\tau$, puis $c = d/\tau$.
- Déphasage entre deux points distants de $d$ : $\Delta\varphi = kd = 2\pi d/\lambda$ ; points en phase si $d = p\lambda$, en opposition si $d = (p + \tfrac12)\lambda$.

## Exemple corrigé

**Énoncé.** Une onde progressive sinusoïdale se propage le long d'une corde à $c = 4$ m·s⁻¹ dans le sens des $x$ croissants, avec une fréquence $f = 2$ Hz et une amplitude $A = 1$ cm. Écrire $y(x,t)$ et calculer le retard entre deux points distants de 1,5 m.

**Solution.**
1. Longueur d'onde : $\lambda = c/f = 2$ m ; $k = 2\pi/\lambda = \pi$ rad·m⁻¹, $\omega = 2\pi f = 4\pi$ rad·s⁻¹.
2. Propagation vers les $x$ croissants : $y(x,t) = A\cos(\omega t - kx)$, avec $A = 1$ cm.
3. Le point le plus éloigné reproduit le mouvement de l'autre avec le retard $\tau = d/c = 0{,}375$ s, soit un déphasage $k\,d = 1{,}5\pi$.

## Pièges classiques

- Le profil spatial et le signal temporel sont **inversés** l'un par rapport à l'autre : le front avant de l'onde dans l'espace est le début du signal dans le temps.
- La célérité dépend du milieu, la fréquence est fixée par la source : en changeant de milieu, $f$ est conservée, $\lambda$ change.

## Ordres de grandeur

| Onde | Célérité |
|---|---|
| son dans l'air (20 °C) | 343 m·s⁻¹ |
| son dans l'eau | 1 500 m·s⁻¹ |
| lumière dans le vide | 3,00·10⁸ m·s⁻¹ |
| houle au large | 10 à 20 m·s⁻¹ |
