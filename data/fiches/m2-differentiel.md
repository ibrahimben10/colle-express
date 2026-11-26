---
titre: Calcul différentiel
---
## L'essentiel

Pour une fonction de plusieurs variables, la différentielle généralise la dérivée : c'est l'application linéaire qui approche $f$ au voisinage d'un point. Dérivées partielles, gradient et règle de la chaîne permettent de calculer ; la hessienne aide à classer les points critiques pour chercher les extremums.

## Dérivées selon un vecteur, dérivées partielles

$f : U \to F$ avec $U$ ouvert de $E$ (en pratique $\mathbb R^n$).

- Dérivée selon $v$ en $a$ : $D_vf(a) = \lim_{t\to0}\frac{f(a + tv) - f(a)}{t}$ (si elle existe).
- Dérivées partielles : $\partial_if(a) = D_{e_i}f(a)$ ; on dérive par rapport à une variable, les autres étant fixées.

## Différentielle

> **Définition.** $f$ est différentiable en $a$ s'il existe une application linéaire $\mathrm df(a)$ telle que $f(a + h) = f(a) + \mathrm df(a)(h) + o(\|h\|)$.

- Différentiable en $a$ implique continue en $a$ et dérivable selon tout vecteur : $D_vf(a) = \mathrm df(a)(v)$.
- Dans $\mathbb R^n$ : $\mathrm df(a)(h) = \sum_i\partial_if(a)h_i$ ; matrice **jacobienne** $J_f(a) = (\partial_jf_i(a))$ pour $f$ à valeurs dans $\mathbb R^p$.
- Les applications linéaires, bilinéaires (produit scalaire, produit matriciel) et polynomiales sont différentiables : $\mathrm du(a) = u$ pour $u$ linéaire ; $\mathrm dB(a, b)(h, k) = B(h, b) + B(a, k)$.

> **Théorème.** Si les dérivées partielles existent et sont **continues** sur $U$, alors $f$ est différentiable sur $U$ : elle est de classe $\mathcal C^1$.

## Règle de la chaîne

> **Théorème.** $\mathrm d(g \circ f)(a) = \mathrm dg(f(a)) \circ \mathrm df(a)$ ; matriciellement, $J_{g\circ f}(a) = J_g(f(a))J_f(a)$.

- Le long d'un chemin : $\frac{\mathrm d}{\mathrm dt}f(\gamma(t)) = \mathrm df(\gamma(t))(\gamma'(t)) = \sum_i\partial_if(\gamma(t))\gamma_i'(t)$.
- Changement de variables : si $g(u, v) = f(x(u, v), y(u, v))$, alors $\partial_ug = \partial_xf\,\partial_ux + \partial_yf\,\partial_uy$. Exemple : coordonnées polaires $x = r\cos\theta$, $y = r\sin\theta$.
- **Inégalité des accroissements finis** : sur un ouvert convexe, si $\|\mathrm df\| \le k$, $f$ est $k$-lipschitzienne. Si $\mathrm df = 0$ sur un ouvert connexe par arcs, $f$ est constante.

## Gradient

[[fig:m2-differentiel-1]]

Pour $f$ à valeurs réelles dans un espace euclidien : $\mathrm df(a)(h) = \langle\nabla f(a), h\rangle$ ; dans $\mathbb R^n$, $\nabla f = (\partial_1f, \dots, \partial_nf)$.

- Le gradient indique la direction de plus forte croissance ; sa norme est la pente maximale.
- Il est **orthogonal aux lignes (surfaces) de niveau** : si $\gamma$ est tracée sur $\{f = c\}$, $\langle\nabla f(\gamma(t)), \gamma'(t)\rangle = 0$.
- Plan tangent à la surface $\{f = 0\}$ en un point régulier $a$ ($\nabla f(a) \ne 0$) : $\langle\nabla f(a), x - a\rangle = 0$. Pour un graphe $z = g(x, y)$ : $z = g(a) + \partial_xg(a)(x - x_0) + \partial_yg(a)(y - y_0)$.

## Dérivées d'ordre 2

> **Théorème de Schwarz.** Si $f$ est de classe $\mathcal C^2$ sur $U$, $\partial_i\partial_jf = \partial_j\partial_if$.

Matrice **hessienne** $H_f(a) = (\partial_i\partial_jf(a))$, symétrique. Formule de Taylor-Young à l'ordre 2 : $f(a + h) = f(a) + \langle\nabla f(a), h\rangle + \frac12{}^thH_f(a)h + o(\|h\|^2)$.

Équations aux dérivées partielles simples : $\partial_xf = 0$ sur un convexe donne $f(x, y) = \varphi(y)$ ; on résout souvent par un changement de variables linéaire (par exemple $u = x + y$, $v = x - y$ pour l'équation des ondes).

## Extremums

> **Théorème — Condition nécessaire.** Si $f$ est différentiable sur un **ouvert** $U$ et admet un extremum local en $a$, alors $\nabla f(a) = 0$ : $a$ est un **point critique**.

> **Théorème — Condition d'ordre 2.** Si $f$ est $\mathcal C^2$ et $a$ est un point critique :
> - si $H_f(a) \in S_n^{++}$ (valeurs propres $> 0$), minimum local strict ;
> - si $-H_f(a) \in S_n^{++}$, maximum local strict ;
> - si $H_f(a)$ a deux valeurs propres de signes opposés, pas d'extremum (point col) ;
> - condition nécessaire : en un minimum local, $H_f(a) \in S_n^+$.

En dimension 2, avec $r = \partial_x^2f$, $s = \partial_x\partial_yf$, $t = \partial_y^2f$ : $rt - s^2 > 0$ donne un extremum (minimum si $r > 0$) ; $rt - s^2 < 0$, un col ; $rt - s^2 = 0$, on ne peut pas conclure.

> **Méthode — Extremums sur un compact.** Une fonction continue sur un compact $K$ atteint ses bornes. On cherche les points critiques à l'**intérieur**, puis on étudie $f$ sur le **bord** (paramétrage), et on compare les valeurs.

**Extremums sous contrainte** (optimisation sur $\{g = 0\}$) : en un extremum de $f$ restreinte à la surface régulière $\{g = 0\}$, $\nabla f(a)$ est colinéaire à $\nabla g(a)$ (multiplicateur de Lagrange).

## Exemple corrigé

**Énoncé.** Extremums de $f(x, y) = x^2 + xy + y^2 - 3x$ sur $\mathbb R^2$.

**Solution.** $\nabla f = (2x + y - 3,\ x + 2y) = 0$ donne $(2, -1)$. Hessienne $\begin{pmatrix}2 & 1\\ 1 & 2\end{pmatrix}$, valeurs propres 3 et 1 : minimum local, $f(2, -1) = -3$. Il est global : $f(2 + h, -1 + k) - f(2, -1) = h^2 + hk + k^2 = \left(h + \frac k2\right)^2 + \frac34k^2 \ge 0$.

## Exemple corrigé (règle de la chaîne)

**Énoncé.** Trouver les $f$ de classe $\mathcal C^1$ sur $\mathbb R^2$ telles que $\partial_xf - \partial_yf = 0$.

**Solution.** Changement de variables $u = x + y$, $v = x - y$ (bijectif linéaire) : $f(x, y) = g(x + y, x - y)$. Alors $\partial_xf = \partial_ug + \partial_vg$ et $\partial_yf = \partial_ug - \partial_vg$, d'où $2\partial_vg = 0$ : $g(u, v) = \varphi(u)$. Solutions : $f(x, y) = \varphi(x + y)$ avec $\varphi$ de classe $\mathcal C^1$.

## Pièges classiques

- L'existence des dérivées partielles n'implique ni la différentiabilité, ni même la continuité.
- $\nabla f(a) = 0$ n'est une condition nécessaire que sur un **ouvert** : sur le bord d'un domaine, un extremum peut avoir un gradient non nul.
- Un point critique n'est pas forcément un extremum (col de $x^2 - y^2$).
