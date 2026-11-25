---
titre: Superposition de deux signaux sinusoïdaux
---
## L'essentiel

Deux signaux sinusoïdaux de **même fréquence** s'ajoutent en un signal sinusoïdal de même fréquence dont l'amplitude dépend de leur **déphasage**. C'est le principe des interférences et des ondes stationnaires. Deux fréquences voisines donnent des battements.

## Somme de deux sinusoïdes de même pulsation

Pour $s_1 = A_1\cos(\omega t + \varphi_1)$ et $s_2 = A_2\cos(\omega t + \varphi_2)$, avec $\Delta\varphi = \varphi_2 - \varphi_1$ :
$$A^2 = A_1^2 + A_2^2 + 2A_1A_2\cos\Delta\varphi.$$

> **Propriété — Interférences.** Amplitude maximale $A_1 + A_2$ si $\Delta\varphi = 2p\pi$ (constructives), minimale $|A_1 - A_2|$ si $\Delta\varphi = (2p+1)\pi$ (destructives).

[[fig:p1-superposition-1]]

Pour deux sources synchrones en phase, en un point $M$ : $\Delta\varphi = \dfrac{2\pi}{\lambda}\,\delta$ avec $\delta = S_2M - S_1M$ la **différence de marche**.

## Ondes stationnaires

La superposition de deux ondes progressives de même amplitude se propageant en sens inverses donne
$$s(x,t) = 2A\cos(kx + \alpha)\cos(\omega t + \beta) :$$
les dépendances en $x$ et en $t$ sont **séparées**. Les nœuds (amplitude nulle) sont distants de $\lambda/2$, les ventres aussi.

[[fig:p1-superposition-2]]

> **Propriété — Modes propres d'une corde fixée en $x = 0$ et $x = L$.** Les extrémités sont des nœuds, donc $L = n\dfrac{\lambda_n}{2}$ et $f_n = n\dfrac{c}{2L}$, $n \in \mathbb N^*$.

## Battements

[[fig:p1-superposition-3]]

$\cos\omega_1 t + \cos\omega_2 t = 2\cos\!\left(\dfrac{\omega_1 - \omega_2}{2}t\right)\cos\!\left(\dfrac{\omega_1 + \omega_2}{2}t\right)$ : une oscillation rapide modulée par une enveloppe lente, de période $T_b = 1/|f_1 - f_2|$.

## Pièges classiques

- Il faut des sources **cohérentes** (même fréquence, déphasage constant) pour observer des interférences stables.
- La période des battements est $1/|f_1 - f_2|$, et non $2/|f_1 - f_2|$ : l'enveloppe s'annule deux fois par période de son cosinus.
- Dans une onde stationnaire, deux points entre deux nœuds consécutifs vibrent **en phase** ; de part et d'autre d'un nœud, en opposition.
