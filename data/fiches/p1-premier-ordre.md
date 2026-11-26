---
titre: Circuit linéaire du premier ordre
---
## L'essentiel

Un circuit du premier ordre (RC ou RL) répond à un échelon de tension par une évolution **exponentielle** de constante de temps $\tau$. Le régime permanent est atteint à 99 % au bout de $5\tau$.

[[fig:p1-premier-ordre-1]]

## Circuit RC série

Loi des mailles et $i = C\,\mathrm du_C/\mathrm dt$ :
$$\tau\frac{\mathrm du_C}{\mathrm dt} + u_C = E,\qquad \tau = RC.$$

> **Méthode — Résolution.** Solution = solution particulière (régime permanent, ici $E$) + solution de l'équation homogène $Ae^{-t/\tau}$ ; la constante $A$ se fixe par la **continuité** de $u_C$.

Charge d'un condensateur initialement déchargé :
$$u_C(t) = E\left(1 - e^{-t/\tau}\right),\qquad i(t) = \frac{E}{R}e^{-t/\tau}.$$

[[fig:p1-premier-ordre-2]]

La tangente à l'origine coupe l'asymptote à $t = \tau$ ; à cet instant $u_C = 0{,}63\,E$.

## Circuit RL série

[[fig:p1-premier-ordre-3]]

$$\tau\frac{\mathrm di}{\mathrm dt} + i = \frac{E}{R},\qquad \tau = \frac{L}{R},\qquad i(t) = \frac{E}{R}\left(1 - e^{-t/\tau}\right).$$
Ici, c'est l'intensité qui est continue.

## Bilan d'énergie

Pendant la charge complète, le générateur fournit $CE^2$ : la moitié est stockée dans le condensateur ($\tfrac12 CE^2$), l'autre moitié est dissipée par effet Joule, **quelle que soit** $R$.

## Exemple corrigé

**Énoncé.** Un condensateur $C = 10$ µF, initialement déchargé, est chargé à travers $R = 1$ kΩ par un échelon de tension $E = 5$ V. Donner $u_C(t)$ et le temps au bout duquel $u_C = 4{,}75$ V.

**Solution.**
1. Loi des mailles : $E = Ri + u_C$ avec $i = C\dfrac{\mathrm du_C}{\mathrm dt}$, d'où $\tau\dfrac{\mathrm du_C}{\mathrm dt} + u_C = E$, $\tau = RC = 10$ ms.
2. Solution : $u_C = E + K e^{-t/\tau}$ ; la continuité de $u_C$ donne $u_C(0) = 0$, donc $K = -E$ : $u_C(t) = E(1 - e^{-t/\tau})$.
3. $u_C = 0{,}95E$ pour $e^{-t/\tau} = 0{,}05$, soit $t = \tau\ln20 \approx 3\tau = 30$ ms : c'est le « temps de réponse à 5 % ».

## Pièges classiques

- L'intensité dans un circuit RC **saute** à la fermeture de l'interrupteur : seule $u_C$ est continue.
- En régime permanent continu, un condensateur se comporte comme un interrupteur ouvert, une bobine comme un fil.
- Vérifier l'homogénéité : $RC$ et $L/R$ sont des temps.

## Ordres de grandeur

$R = 10$ kΩ et $C = 100$ nF : $\tau = 1$ ms.
