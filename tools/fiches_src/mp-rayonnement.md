---
titre: Rayonnement dipolaire
---
## L'essentiel

Une charge accélérée rayonne. Le modèle de base est le **dipôle oscillant** $\vec p(t) = p_0\cos(\omega t)\,\vec u_z$, source des antennes et de la diffusion de la lumière par les molécules.

[[fig:mp-rayonnement-1]]

## Hypothèses

Taille du dipôle $d \ll \lambda \ll r$ : approximation dipolaire et **zone de rayonnement**.

## Champ rayonné

Dans la zone de rayonnement, le champ a localement la structure d'une onde plane se propageant selon $\vec u_r$ :
$$\vec E = -\frac{\mu_0\sin\theta}{4\pi r}\,\ddot p\!\left(t - \frac rc\right)\vec u_\theta,\qquad \vec B = \frac{\vec u_r\wedge\vec E}{c}.$$
L'amplitude décroît en $1/r$, et la puissance traversant une sphère est indépendante de $r$ : l'énergie part à l'infini.

## Puissance rayonnée

[[fig:mp-rayonnement-2]]

> **Propriété — Indicatrice de rayonnement.** La puissance rayonnée par unité d'angle solide varie en $\sin^2\theta$ : maximale dans le plan équatorial, nulle dans l'axe du dipôle.

Puissance totale moyenne : $\mathcal P = \dfrac{\mu_0p_0^2\omega^4}{12\pi c}$, proportionnelle à $\omega^4$.

## Applications

- **Bleu du ciel** : la diffusion de Rayleigh par les molécules d'air est plus forte pour le bleu (facteur $\omega^4$).
- Lumière diffusée polarisée à 90° du soleil.
- Antennes : une antenne émet surtout perpendiculairement à son axe.

## Exemple corrigé

**Énoncé.** Pourquoi le ciel est-il bleu, et le soleil couchant rouge ?

**Solution.**
1. Les molécules de l'air, excitées par la lumière solaire, se comportent comme des dipôles oscillants à la fréquence de l'onde.
2. Puissance diffusée proportionnelle à $\omega^4$ : le bleu (400 nm) est diffusé $(700/400)^4 \approx 9$ fois plus que le rouge (700 nm).
3. Le ciel diffuse surtout du bleu. Au coucher, la lumière traverse une grande épaisseur d'air : elle a perdu son bleu, il reste le rouge.

## Pièges classiques

- Le champ rayonné est évalué au temps retardé $t - r/c$.
- Ne pas confondre la zone de rayonnement ($r \gg \lambda$) avec la zone proche, où l'on retrouve le champ électrostatique du dipôle.
