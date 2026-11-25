---
titre: Thermodynamique statistique
---
## L'essentiel

Pour un système en équilibre avec un thermostat à la température $T$, la probabilité d'occuper un état d'énergie $E$ est proportionnelle au **facteur de Boltzmann** $e^{-E/(k_BT)}$.

> **Loi de Boltzmann.** $p_i = \dfrac{1}{Z}e^{-E_i/(k_BT)}$, avec la fonction de partition $Z = \sum_i e^{-E_i/(k_BT)}$.

L'énergie thermique $k_BT$ sert d'échelle : un état d'énergie très supérieure à $k_BT$ au-dessus du fondamental est quasiment vide.

## Atmosphère isotherme

[[fig:mp-statistique-1]]

L'énergie potentielle d'une molécule est $mgz$ :
$$n(z) = n_0\,e^{-z/H},\qquad H = \frac{k_BT}{mg}\approx 8\ \text{km pour l'air à 290 K}.$$
On retrouve le résultat de la statique des fluides pour un gaz parfait isotherme.

## Système à deux niveaux

[[fig:mp-statistique-2]]

Niveaux d'énergie $0$ et $\Delta E$ :
$$p_2 = \frac{1}{1 + e^{\Delta E/(k_BT)}}.$$
Basse température : tout est dans le fondamental. Haute température : les populations tendent vers 1/2, sans jamais s'inverser à l'équilibre.

## Énergie moyenne et capacité thermique

$\langle E\rangle = \sum_ip_iE_i$, et $C = \dfrac{\mathrm d\langle E\rangle}{\mathrm dT}$.

> **Théorème d'équipartition.** À l'équilibre, chaque terme quadratique indépendant de l'énergie contribue pour $\tfrac12k_BT$ à l'énergie moyenne.

Gaz parfait monoatomique : $U = \tfrac32Nk_BT$ ; diatomique (à température ambiante) : $\tfrac52Nk_BT$ ; solide (loi de Dulong et Petit) : $C_m = 3R$.

## Pièges classiques

- L'équipartition ne s'applique qu'aux degrés de liberté « dégelés » ($k_BT$ grand devant l'écart entre niveaux).
- $p_i$ concerne un **état** ; si un niveau est dégénéré, multiplier par sa dégénérescence.
