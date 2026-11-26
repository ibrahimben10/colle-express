---
titre: Circuit linéaire du premier ordre
---
## L'essentiel

Un circuit du premier ordre (RC ou RL) obéit à une équation différentielle linéaire d'ordre 1. Sa réponse à un échelon de tension est une évolution **exponentielle** de constante de temps $\tau$ ; le régime permanent est atteint à 99 % au bout de $5\tau$.

[[fig:p1-premier-ordre-1]]

## Régime transitoire et régime permanent

Après un changement brusque (fermeture d'un interrupteur, échelon), le circuit passe par un **régime transitoire** avant d'atteindre un **régime permanent** (ici continu). On cherche les grandeurs juste après le changement grâce aux **continuités** ($u_C$, $i_L$), et les grandeurs en régime permanent en remplaçant $C$ par un interrupteur ouvert et $L$ par un fil.

## Circuit RC série

### Équation

Loi des mailles $E = Ri + u_C$ et $i = C\,\dfrac{\mathrm du_C}{\mathrm dt}$ :
$$\tau\frac{\mathrm du_C}{\mathrm dt} + u_C = E,\qquad \tau = RC.$$

> **Méthode — Résolution.** Solution = solution particulière (régime permanent, ici $E$) + solution de l'équation homogène $Ae^{-t/\tau}$ ; la constante $A$ se fixe par la **continuité** de $u_C$ en $t = 0$.

### Charge

Condensateur initialement déchargé :
$$u_C(t) = E\left(1 - e^{-t/\tau}\right),\qquad i(t) = \frac{E}{R}e^{-t/\tau}.$$

[[fig:p1-premier-ordre-2]]

- La tangente à l'origine coupe l'asymptote $u_C = E$ à $t = \tau$ ; à cet instant $u_C = 0{,}63\,E$.
- Temps de réponse à 5 % : $3\tau$ ; à 1 % : $5\tau$.
- L'intensité **saute** de 0 à $\frac ER$ à la fermeture.

### Décharge

Si $u_C(0) = E$ et le générateur est remplacé par un fil : $u_C(t) = Ee^{-t/\tau}$ et $i(t) = -\frac ERe^{-t/\tau}$.

## Circuit RL série

[[fig:p1-premier-ordre-3]]

$$\frac LR\frac{\mathrm di}{\mathrm dt} + i = \frac{E}{R},\qquad \tau = \frac{L}{R},\qquad i(t) = \frac{E}{R}\left(1 - e^{-t/\tau}\right).$$

Ici, c'est l'intensité qui est continue ; $u_L = L\frac{\mathrm di}{\mathrm dt} = Ee^{-t/\tau}$ saute de 0 à $E$. À l'ouverture d'un circuit inductif, la continuité de $i$ provoque une surtension (étincelle) : on protège par une diode de roue libre.

## Forme générale et portrait de phase

Toute grandeur $x$ d'un circuit du premier ordre vérifie $\tau\dot x + x = x_\infty$, d'où $x(t) = x_\infty + (x(0^+) - x_\infty)e^{-t/\tau}$. Dans le plan $(x, \dot x)$, la trajectoire est un segment de droite qui aboutit au point $(x_\infty, 0)$.

## Bilan d'énergie

Multiplier la loi des mailles par $i$ : $Ei = Ri^2 + \dfrac{\mathrm d}{\mathrm dt}\left(\tfrac12Cu_C^2\right)$ (puissance fournie = puissance Joule + variation d'énergie stockée).

Pendant la charge complète, le générateur fournit $CE^2$ : la moitié est stockée dans le condensateur ($\tfrac12 CE^2$), l'autre moitié est dissipée par effet Joule, **quelle que soit** $R$.

## Méthode générale

1. Déterminer les valeurs initiales ($t = 0^+$) par continuité, et finales par le régime permanent.
2. Établir l'équation différentielle (lois de Kirchhoff + relations des dipôles), la mettre sous forme canonique et identifier $\tau$.
3. Résoudre et fixer la constante.
4. Vérifier : homogénéité ($RC$ et $L/R$ sont des temps), limites en 0 et $+\infty$.

## Exemple corrigé

**Énoncé.** Un condensateur $C = 10$ µF, initialement déchargé, est chargé à travers $R = 1$ kΩ par un échelon de tension $E = 5$ V. Donner $u_C(t)$ et le temps au bout duquel $u_C = 4{,}75$ V.

**Solution.**
1. Loi des mailles : $E = Ri + u_C$ avec $i = C\dfrac{\mathrm du_C}{\mathrm dt}$, d'où $\tau\dfrac{\mathrm du_C}{\mathrm dt} + u_C = E$, $\tau = RC = 10$ ms.
2. Solution : $u_C = E + K e^{-t/\tau}$ ; la continuité de $u_C$ donne $u_C(0) = 0$, donc $K = -E$ : $u_C(t) = E(1 - e^{-t/\tau})$.
3. $u_C = 0{,}95E$ pour $e^{-t/\tau} = 0{,}05$, soit $t = \tau\ln20 \approx 3\tau = 30$ ms : c'est le temps de réponse à 5 %.

## Exemple corrigé (circuit à deux mailles)

**Énoncé.** $E$ en série avec $R$, puis $C$ en parallèle avec une résistance $R$. Constante de temps et tension finale ?

**Solution.** Thévenin vu du condensateur : $E' = \frac E2$ et $R' = \frac R2$. Donc $\tau = \frac{RC}{2}$ et $u_C \to \frac E2$ (diviseur de tension en régime permanent).

## Pièges classiques

- L'intensité dans un circuit RC **saute** à la fermeture de l'interrupteur : seule $u_C$ est continue.
- En régime permanent continu, un condensateur se comporte comme un interrupteur ouvert, une bobine comme un fil.
- La constante se fixe sur la solution **complète**, pas sur la solution homogène.

## Ordres de grandeur

$R = 10$ kΩ et $C = 100$ nF : $\tau = 1$ ms ; $L = 10$ mH et $R = 100$ Ω : $\tau = 0{,}1$ ms.
