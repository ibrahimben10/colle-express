---
titre: Circuit mobile dans un champ magnétique stationnaire
---
## L'essentiel

Un circuit qui se déplace dans un champ constant (cas de Lorentz) voit son flux varier : une f.é.m. apparaît, et la force de Laplace qui en résulte freine le mouvement. C'est la **conversion électromécanique** de puissance.

## Rails de Laplace en générateur

[[fig:p5-circuit-mobile-1]]

Barre de longueur $L$ glissant à la vitesse $v$ dans un champ $B$ perpendiculaire :
$$e = -\frac{\mathrm d\Phi}{\mathrm dt},\qquad |e| = BLv,\qquad i = \frac{e}{R}.$$
La force de Laplace sur la barre s'oppose à la vitesse (loi de Lenz) : c'est un **freinage**.

> **Méthode — Couplage électromécanique.** Écrire l'équation électrique (loi des mailles avec $e$) et l'équation mécanique (PFD avec la force de Laplace) ; les résoudre ensemble.

> **Propriété — Bilan de puissance.** La puissance de la force de Laplace est l'opposée de la puissance électrique fournie par la f.é.m. : $\mathcal P_{\text{Laplace}} + ei = 0$. Le couplage convertit l'énergie sans en créer.

## Alternateur

[[fig:p5-circuit-mobile-2]]

Un cadre de $N$ spires de surface $S$ tourne à $\omega$ dans un champ uniforme : $\Phi = NBS\cos\omega t$, donc $e = NBS\omega\sin\omega t$, une tension sinusoïdale.

## Applications

Freinage par courants de Foucault, alternateurs de centrales, dynamo, haut-parleur utilisé en microphone.

## Pièges classiques

- Oublier le terme de f.é.m. dans la loi des mailles, ou la force de Laplace dans le PFD : le couplage disparaît.
- Le sens de $e$ suit l'orientation du contour, comme dans toute l'induction.
