---
titre: Circuit linéaire du second ordre
---
## L'essentiel

Un circuit RLC série est un oscillateur **amorti**. Son équation se met sous une forme canonique faisant apparaître la pulsation propre $\omega_0$ et le facteur de qualité $Q$. Selon $Q$, la réponse à un échelon est pseudo-périodique, critique ou apériodique.

[[fig:p1-second-ordre-1]]

## Mise en équation

Loi des mailles $E = Ri + L\frac{\mathrm di}{\mathrm dt} + u_C$ avec $i = C\frac{\mathrm du_C}{\mathrm dt}$ :
$$\frac{\mathrm d^2u_C}{\mathrm dt^2} + \frac{\omega_0}{Q}\frac{\mathrm du_C}{\mathrm dt} + \omega_0^2u_C = \omega_0^2E,\qquad \omega_0 = \frac1{\sqrt{LC}},\quad Q = \frac1R\sqrt{\frac LC}.$$

On écrit aussi $\ddot x + 2\lambda\dot x + \omega_0^2x = \dots$ avec le coefficient d'amortissement $\lambda = \frac{\omega_0}{2Q} = \frac{R}{2L}$, ou avec $\xi = \frac{1}{2Q}$.

> **Méthode — Équation caractéristique.** $r^2 + \dfrac{\omega_0}{Q}r + \omega_0^2 = 0$, de discriminant $\Delta = \omega_0^2\left(\dfrac1{Q^2} - 4\right)$ : le signe de $\Delta$ dépend de la comparaison de $Q$ à $\tfrac12$.

## Trois régimes

[[fig:p1-second-ordre-2]]

| Régime | Condition | Forme de la solution homogène |
|---|---|---|
| pseudo-périodique | $Q > \tfrac12$ | $e^{-t/\tau}(A\cos\Omega t + B\sin\Omega t)$, $\tau = \frac{2Q}{\omega_0}$, $\Omega = \omega_0\sqrt{1 - \tfrac1{4Q^2}}$ |
| critique | $Q = \tfrac12$ | $(A + Bt)e^{-\omega_0 t}$ |
| apériodique | $Q < \tfrac12$ | $Ae^{r_1t} + Be^{r_2t}$, $r_1, r_2 < 0$ |

- Le régime critique est le retour à l'équilibre le plus rapide **sans dépassement**.
- En régime pseudo-périodique, on observe environ $Q$ oscillations visibles ; durée du transitoire de l'ordre de quelques $\tau = \frac{2Q}{\omega_0}$.
- **Décrément logarithmique** : $\delta = \ln\frac{x(t)}{x(t + T)} = \frac{T}{\tau}$ ; pour $Q \gg 1$, $\delta \approx \frac{\pi}{Q}$. Il permet de mesurer $Q$ sur un enregistrement.
- Régime apériodique très amorti ($Q \ll 1$) : une constante de temps lente $\approx \frac{1}{Q\omega_0} = RC$ domine.

## Conditions initiales

Deux conditions sont nécessaires : continuité de $u_C$ et de $i = C\,\mathrm du_C/\mathrm dt$ (continuité de l'intensité dans la bobine), donc $u_C(0^+)$ et $\dot u_C(0^+) = \frac{i(0^+)}{C}$.

## Énergie

$\mathcal E = \tfrac12 Cu_C^2 + \tfrac12 Li^2$. En régime libre, $\dfrac{\mathrm d\mathcal E}{\mathrm dt} = -Ri^2 \le 0$ : la résistance dissipe l'énergie, qui oscille entre condensateur et bobine. Sans résistance ($R = 0$, $Q \to \infty$), on retrouve l'oscillateur harmonique LC.

Interprétation de $Q$ : $Q = 2\pi\frac{\text{énergie stockée}}{\text{énergie dissipée par période}}$ (pour $Q \gg 1$).

## Analogie électromécanique

| Électrique | $q$ | $i$ | $L$ | $R$ | $\frac1C$ |
|---|---|---|---|---|---|
| Mécanique | $x$ | $v$ | $m$ | $\alpha$ (frottement) | $k$ |

Pour une masse-ressort amortie $m\ddot x + \alpha\dot x + kx = 0$ : $\omega_0 = \sqrt{k/m}$ et $Q = \frac{\sqrt{km}}{\alpha}$.

## Portrait de phase

Dans le plan $(x, \dot x)$ : spirale convergeant vers l'équilibre (pseudo-périodique), courbe sans tour (apériodique ou critique). C'est un outil de lecture des régimes, utile aussi pour les systèmes non linéaires.

## Exemple corrigé

**Énoncé.** Un circuit RLC série ($R = 100$ Ω, $L = 0{,}1$ H, $C = 1$ µF) est soumis à un échelon de tension. Quel est le régime transitoire ?

**Solution.**
1. $\omega_0 = \dfrac{1}{\sqrt{LC}} \approx 3{,}2\cdot10^3$ rad·s⁻¹ et $Q = \dfrac1R\sqrt{\dfrac LC} \approx 3{,}2$.
2. $Q > 1/2$ : régime **pseudo-périodique**.
3. $\Omega = \omega_0\sqrt{1 - \dfrac{1}{4Q^2}} \approx 0{,}99\,\omega_0$ ; on observe environ 3 oscillations visibles ; $\tau = \frac{2L}{R} = 2$ ms.

## Exemple corrigé (résistance critique)

**Énoncé.** Pour $L = 0{,}1$ H et $C = 1$ µF, quelle résistance donne le régime critique ?

**Solution.** $Q = \frac12 \Leftrightarrow R = 2\sqrt{\frac LC} = 2\sqrt{10^5} \approx 630$ Ω.

## Pièges classiques

- La pseudo-période $2\pi/\Omega$ est **plus grande** que la période propre $2\pi/\omega_0$.
- Ne pas oublier la solution particulière ($E$) avant d'appliquer les conditions initiales.
- Le régime dépend de $Q$, pas de $R$ seule : augmenter $R$ diminue $Q$.
