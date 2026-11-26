---
titre: Calcul différentiel
---
## L'essentiel

Pour une fonction de plusieurs variables, la différentielle généralise la dérivée : c'est l'application linéaire qui approche $f$ au voisinage d'un point. Les dérivées partielles et le gradient permettent de la calculer et de chercher les extremums.

## Différentielle et dérivées partielles

> **Définition.** $f$ est différentiable en $a$ s'il existe une application linéaire $\mathrm df(a)$ telle que $f(a + h) = f(a) + \mathrm df(a)(h) + o(\|h\|)$.

- Dérivée selon un vecteur $v$ : $D_vf(a) = \mathrm df(a)(v)$ ; dérivées partielles $\partial_if(a) = \mathrm df(a)(e_i)$.
- $f$ est de classe $\mathcal C^1$ si ses dérivées partielles existent et sont continues ; alors $f$ est différentiable et $\mathrm df(a)(h) = \sum_i\partial_if(a)h_i$.
- **Règle de la chaîne** : $\frac{\mathrm d}{\mathrm dt}f(x(t), y(t)) = \partial_xf\,x'(t) + \partial_yf\,y'(t)$.

## Gradient

[[fig:m2-differentiel-1]]

$\mathrm df(a)(h) = \langle\nabla f(a), h\rangle$. Le gradient est orthogonal aux lignes de niveau et indique la direction de plus forte croissance.

## Extremums

> **Théorème — Condition nécessaire.** Si $f$ (différentiable sur un **ouvert**) a un extremum local en $a$, alors $\nabla f(a) = 0$ : $a$ est un point critique.

> **Théorème de Schwarz.** Si $f$ est $\mathcal C^2$, $\partial_i\partial_jf = \partial_j\partial_if$.

Étude d'un point critique : matrice **hessienne** $H$ (symétrique) ; si $H$ est définie positive, minimum local ; définie négative, maximum local ; valeurs propres de signes opposés, point col.

Sur un compact (fermé borné), une fonction continue atteint ses extremums : les chercher parmi les points critiques intérieurs et sur le bord.

## Exemple corrigé

**Énoncé.** Extremums de $f(x, y) = x^2 + xy + y^2 - 3x$ sur $\mathbb R^2$.

**Solution.** $\nabla f = (2x + y - 3,\ x + 2y) = 0$ donne $(x, y) = (2, -1)$. La hessienne $\begin{pmatrix}2 & 1\\ 1 & 2\end{pmatrix}$ a pour valeurs propres 3 et 1, positives : minimum local, égal à $f(2, -1) = -3$. C'est un minimum global car $f(2 + h, -1 + k) - f(2, -1) = h^2 + hk + k^2 \ge 0$.

## Pièges classiques

- L'existence des dérivées partielles n'implique pas la continuité.
- La condition $\nabla f = 0$ ne vaut que sur un **ouvert** : sur un bord, un extremum peut avoir un gradient non nul.
