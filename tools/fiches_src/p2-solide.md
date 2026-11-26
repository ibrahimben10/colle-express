---
titre: Cinématique du solide
---
## L'essentiel

Un **solide** est un système dont les distances entre points restent constantes. Au programme, deux mouvements : la **translation** et la **rotation autour d'un axe fixe**.

[[fig:p2-solide-1]]

## Translation

> **Définition — Translation.** Tout segment du solide garde une direction fixe. Tous les points ont alors, à chaque instant, le **même** vecteur vitesse (et la même accélération).

La translation peut être rectiligne ou circulaire (une nacelle de grande roue est en translation circulaire : ses points décrivent des cercles de même rayon mais de centres différents).

## Rotation autour d'un axe fixe

Chaque point $M$ décrit un cercle centré sur l'axe $\Delta$, de rayon $r$ égal à sa distance à l'axe. Tous les points ont la même vitesse angulaire $\omega = \dot\theta$.

> **Formule — Vitesse d'un point.** $v = r\omega$, la vitesse est orthoradiale ; vectoriellement $\vec v = \vec\omega \wedge \overrightarrow{HM}$, $H$ projeté de $M$ sur l'axe.

## Méthode

- Pour un solide en rotation, raisonner sur un seul paramètre angulaire $\theta(t)$.
- Une roue qui roule sans glisser n'est ni en translation ni en rotation autour d'un axe fixe : son point de contact a une vitesse nulle.

## Exemple corrigé

**Énoncé.** Un disque tourne autour de son axe fixe à 1200 tours par minute. Quelle est la vitesse d'un point situé à 10 cm de l'axe ?

**Solution.**
1. Vitesse angulaire : $\omega = 1200\times\dfrac{2\pi}{60} \approx 126$ rad·s⁻¹.
2. Chaque point décrit un cercle centré sur l'axe : $v = r\omega = 0{,}10\times126 \approx 12{,}6$ m·s⁻¹.
3. Tous les points ont la même $\omega$, mais leur vitesse est proportionnelle à la distance à l'axe.

## Pièges classiques

- Translation circulaire et rotation : dans les deux cas les points décrivent des cercles, mais en translation les cercles ont des centres différents et les vitesses sont toutes égales.
- $\omega$ en rad·s⁻¹, la fréquence de rotation $N$ en tours par seconde : $\omega = 2\pi N$.
