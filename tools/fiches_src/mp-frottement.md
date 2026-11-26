---
titre: Lois du frottement solide
---
## L'essentiel

Un solide en contact avec un autre subit une réaction $\vec R = \vec N + \vec T$ : composante normale $\vec N$ et composante tangentielle $\vec T$ (frottement). Les lois de Coulomb relient $T$ et $N$ par le coefficient de frottement $f$.

## Lois de Coulomb

[[fig:mp-frottement-1]]

> **Loi — Lois de Coulomb.**
> - Sans glissement (adhérence) : $\|\vec T\| \le f\,\|\vec N\|$.
> - Avec glissement : $\|\vec T\| = f\,\|\vec N\|$, et $\vec T$ est opposée à la vitesse de glissement.

Le **cône de frottement** a pour demi-angle $\varphi$ avec $\tan\varphi = f$ : sans glissement, $\vec R$ est dans le cône ; avec glissement, elle est sur son bord. On prend souvent les coefficients statique et dynamique égaux.

## Exemple : solide sur un plan incliné

[[fig:mp-frottement-2]]

Le solide posé sans vitesse reste immobile si $\tan\alpha \le f$ ; sinon, il glisse avec l'accélération $a = g(\sin\alpha - f\cos\alpha)$.

## Méthode

1. Faire une **hypothèse** (adhérence ou glissement, avec le sens du glissement).
2. Résoudre avec la loi correspondante.
3. **Vérifier** la cohérence : $\|\vec T\| \le f\|\vec N\|$ pour l'adhérence ; vitesse de glissement de même sens que celui supposé pour le glissement. Sinon, changer d'hypothèse.

## Aspect énergétique

La puissance des actions de contact est négative ou nulle : $\mathcal P = \vec T\cdot\vec v_g \le 0$. Elle est nulle en l'absence de glissement.

## Ordres de grandeur

| Contact | $f$ |
|---|---|
| acier sur acier | 0,2 |
| pneu sur route sèche | 0,8 |
| bois sur bois | 0,3 à 0,5 |

## Exemple corrigé

**Énoncé.** On pose un bloc sur un plan dont on augmente lentement l'inclinaison. Il commence à glisser pour $\alpha_0 = 25°$. En déduire $f$, puis l'accélération pour $\alpha = 35°$.

**Solution.**
1. Juste avant le glissement, la réaction est sur le bord du cône : $\tan\alpha_0 = f$, donc $f \approx 0{,}47$.
2. Pour $\alpha = 35°$, hypothèse glissement vers le bas : $N = mg\cos\alpha$ et $T = fN$, opposée au mouvement.
3. PFD le long de la pente : $a = g(\sin\alpha - f\cos\alpha) \approx 9{,}8\,(0{,}574 - 0{,}38) \approx 1{,}9$ m·s⁻².
4. Vérification : $a > 0$, cohérent avec un glissement vers le bas (on suppose ici $f$ dynamique égal à $f$ statique).

## Pièges classiques

- La composante $N$ n'est pas toujours égale au poids : la déterminer avec le PFD.
- En adhérence, $T$ est inconnue (ce n'est pas $fN$).
