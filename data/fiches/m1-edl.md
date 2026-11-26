---
titre: Équations différentielles linéaires
---
## L'essentiel

Une équation différentielle linéaire se résout en deux temps : solutions de l'équation homogène, puis une solution particulière. Toute solution est la somme des deux.

> **Théorème — Structure des solutions.** Si $y_p$ est une solution de $(E)$, les solutions de $(E)$ sont exactement les $y_p + y_h$, où $y_h$ parcourt l'ensemble des solutions de l'équation homogène $(H)$.

## Ordre 1 : $y' + a(x)y = b(x)$

Avec $a$, $b$ continues sur un intervalle $I$ et $A$ une primitive de $a$ :
- solutions de $(H)$ : $y = \lambda e^{-A(x)}$, $\lambda \in \mathbb K$ ;
- solution particulière : **variation de la constante**, on cherche $y = \lambda(x)e^{-A(x)}$, d'où $\lambda'(x) = b(x)e^{A(x)}$.

> **Théorème de Cauchy-Lipschitz linéaire (ordre 1).** Pour tout $x_0 \in I$ et tout $y_0$, il existe une unique solution sur $I$ telle que $y(x_0) = y_0$.

## Ordre 2 à coefficients constants : $ay'' + by' + cy = f(x)$

Équation caractéristique $ar^2 + br + c = 0$, de discriminant $\Delta$.

| Cas (solutions réelles) | Solutions de $(H)$ |
|---|---|
| $\Delta > 0$, racines $r_1 \ne r_2$ | $\lambda e^{r_1x} + \mu e^{r_2x}$ |
| $\Delta = 0$, racine double $r$ | $(\lambda x + \mu)e^{rx}$ |
| $\Delta < 0$, racines $\alpha \pm i\beta$ | $e^{\alpha x}(\lambda\cos\beta x + \mu\sin\beta x)$ |

Second membre $f(x) = P(x)e^{mx}$ ($P$ polynôme) : on cherche une solution $Q(x)e^{mx}$, avec $\deg Q = \deg P$ si $m$ n'est pas racine, en multipliant par $x$ (racine simple) ou $x^2$ (racine double). Pour $\cos(\omega x)$ ou $\sin(\omega x)$ : passer par $e^{i\omega x}$ et prendre la partie réelle ou imaginaire. **Principe de superposition** pour une somme de seconds membres.

## Exemple corrigé

**Énoncé.** Résoudre $y'' - 3y' + 2y = e^x$ avec $y(0) = 0$, $y'(0) = 0$.

**Solution.**
1. $r^2 - 3r + 2 = 0$ : racines 1 et 2, donc $y_h = \lambda e^x + \mu e^{2x}$.
2. 1 est racine simple : on cherche $y_p = axe^x$. On trouve $y_p'' - 3y_p' + 2y_p = -ae^x$, donc $a = -1$.
3. $y = \lambda e^x + \mu e^{2x} - xe^x$ ; $y(0) = \lambda + \mu = 0$ et $y'(0) = \lambda + 2\mu - 1 = 0$, d'où $\mu = 1$, $\lambda = -1$ : $y = e^{2x} - (1 + x)e^x$.

## Pièges classiques

- Résoudre sur un **intervalle** où le coefficient de $y'$ (ou de $y''$) ne s'annule pas ; sinon, étudier le raccordement.
- Ne pas oublier le facteur $x$ quand le second membre est solution de l'équation homogène (résonance).
- Les constantes se déterminent sur la solution **générale**, pas sur $y_h$ seule.
