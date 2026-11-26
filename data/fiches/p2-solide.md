---
titre: Cinématique du solide
---
## L'essentiel

Un **solide** est un système dont les distances entre points restent constantes. Au programme, deux mouvements : la **translation** (tous les points ont la même vitesse) et la **rotation autour d'un axe fixe** (tous les points ont la même vitesse angulaire). On sait alors décrire la vitesse de n'importe quel point.

[[fig:p2-solide-1]]

## Translation

> **Définition — Translation.** Tout segment du solide garde une direction fixe. Tous les points ont alors, à chaque instant, le **même** vecteur vitesse (et la même accélération).

- **Translation rectiligne** : les trajectoires sont des droites parallèles (ascenseur).
- **Translation circulaire** : les trajectoires sont des cercles de même rayon mais de centres différents (nacelle de grande roue, bielle d'une locomotive).
- Le mouvement d'un solide en translation se ramène à celui d'un seul de ses points (par exemple $G$).

## Rotation autour d'un axe fixe

Chaque point $M$ décrit un cercle centré sur l'axe $\Delta$, de rayon $r$ égal à sa distance à l'axe. Tous les points ont la même vitesse angulaire $\omega = \dot\theta$, où $\theta$ est l'angle dont a tourné le solide.

> **Formule — Vitesse d'un point.** $v = r\omega$, la vitesse est orthoradiale ; vectoriellement $\vec v = \vec\omega \wedge \overrightarrow{HM}$, $H$ projeté de $M$ sur l'axe, $\vec\omega = \dot\theta\,\vec u_\Delta$ (vecteur rotation).

- Accélération d'un point : $\vec a = -r\omega^2\vec u_r + r\dot\omega\,\vec u_\theta$ (centripète si $\omega$ est constante).
- Unités : $\omega$ en rad·s⁻¹ ; fréquence de rotation $N$ en tours par seconde ou par minute : $\omega = 2\pi N$.
- Points de l'axe : immobiles.

## Le vecteur rotation (notion)

Pour un solide en rotation autour d'un axe fixe passant par $O$ : $\vec v_M = \vec\omega\wedge\overrightarrow{OM}$ pour tout point $O$ de l'axe. On en déduit la relation entre les vitesses de deux points $A$ et $B$ du solide : $\vec v_B = \vec v_A + \vec\omega\wedge\overrightarrow{AB}$.

## Situations à reconnaître

- Une **roue qui roule sans glisser** n'est ni en translation ni en rotation autour d'un axe fixe : son point de contact avec le sol a une vitesse nulle, le centre avance à $v = R\omega$ ; le point haut a une vitesse $2R\omega$.
- Engrenages et courroies : la vitesse est la même au point de contact, donc $R_1\omega_1 = R_2\omega_2$ (rapport de transmission).
- Une porte, une hélice, un rotor : rotation autour d'un axe fixe.

## Méthode

- Pour un solide en rotation, raisonner sur un seul paramètre angulaire $\theta(t)$ : c'est un système à un degré de liberté.
- Pour une translation, étudier le mouvement d'un point représentatif.
- Vérifier le type de mouvement en regardant un segment du solide : garde-t-il sa direction (translation) ? un axe reste-t-il immobile (rotation) ?

## Exemple corrigé

**Énoncé.** Un disque tourne autour de son axe fixe à 1200 tours par minute. Quelle est la vitesse d'un point situé à 10 cm de l'axe ?

**Solution.**
1. $\omega = 1200\times\dfrac{2\pi}{60} \approx 126$ rad·s⁻¹.
2. $v = r\omega = 0{,}10\times126 \approx 12{,}6$ m·s⁻¹.
3. Accélération (centripète) : $r\omega^2 \approx 1{,}6\cdot10^3$ m·s⁻², environ 160 $g$.

## Exemple corrigé (engrenage)

**Énoncé.** Un pignon de rayon 2 cm entraîne une roue de rayon 8 cm. Le pignon tourne à 600 tr/min ; vitesse de la roue ?

**Solution.** Égalité des vitesses au contact : $R_1\omega_1 = R_2\omega_2$, d'où $\omega_2 = \omega_1\frac{R_1}{R_2}$ : 150 tr/min (en sens inverse).

## Pièges classiques

- Translation circulaire et rotation : dans les deux cas les points décrivent des cercles, mais en translation les cercles ont des centres différents et les vitesses sont toutes égales.
- $\omega$ en rad·s⁻¹, la fréquence de rotation $N$ en tours par seconde : $\omega = 2\pi N$.
- La vitesse d'un point d'un solide en rotation dépend de sa distance à l'axe ; la vitesse angulaire non.
