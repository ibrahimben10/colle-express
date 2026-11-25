---
titre: Circuit linéaire du second ordre
---
## L'essentiel

Un circuit RLC série est un oscillateur **amorti**. Selon le facteur de qualité $Q$, la réponse à un échelon est pseudo-périodique, critique ou apériodique.

[[fig:p1-second-ordre-1]]

## Forme canonique

$$\frac{\mathrm d^2u_C}{\mathrm dt^2} + \frac{\omega_0}{Q}\frac{\mathrm du_C}{\mathrm dt} + \omega_0^2u_C = \omega_0^2E,\qquad \omega_0 = \frac1{\sqrt{LC}},\quad Q = \frac1R\sqrt{\frac LC}.$$

> **Méthode — Équation caractéristique.** $r^2 + \dfrac{\omega_0}{Q}r + \omega_0^2 = 0$, de discriminant $\Delta = \omega_0^2\left(\dfrac1{Q^2} - 4\right)$ : le signe de $\Delta$ dépend de la comparaison de $Q$ à $\tfrac12$.

## Trois régimes

[[fig:p1-second-ordre-2]]

| Régime | Condition | Forme de la solution homogène |
|---|---|---|
| pseudo-périodique | $Q > \tfrac12$ | $e^{-t/\tau}(A\cos\Omega t + B\sin\Omega t)$, $\Omega = \omega_0\sqrt{1 - \tfrac1{4Q^2}}$ |
| critique | $Q = \tfrac12$ | $(A + Bt)e^{-\omega_0 t}$ |
| apériodique | $Q < \tfrac12$ | $Ae^{r_1t} + Be^{r_2t}$, $r_1, r_2 < 0$ |

Le régime critique est le retour à l'équilibre le plus rapide **sans dépassement**. En régime pseudo-périodique, on observe environ $Q$ oscillations visibles.

## Conditions initiales

Deux conditions sont nécessaires : continuité de $u_C$ et de $i = C\,\mathrm du_C/\mathrm dt$ (continuité de l'intensité dans la bobine).

## Énergie

$E = \tfrac12 Cu_C^2 + \tfrac12 Li^2$ décroît : $\dfrac{\mathrm dE}{\mathrm dt} = -Ri^2$ en régime libre.

## Pièges classiques

- La pseudo-période $2\pi/\Omega$ est **plus grande** que la période propre $2\pi/\omega_0$.
- Ne pas oublier la solution particulière ($E$) avant d'appliquer les conditions initiales.
