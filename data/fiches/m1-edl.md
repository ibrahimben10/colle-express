---
titre: Équations différentielles linéaires
---
## L'essentiel

Une équation différentielle linéaire se résout en deux temps : on résout l'équation **homogène** (sans second membre), puis on cherche une **solution particulière**. La solution générale est la somme des deux ; une condition initiale fixe la constante.

## Primitives et calcul intégral (rappels utiles)

- Toute fonction continue sur un intervalle admet des primitives, qui diffèrent d'une constante ; $x \mapsto \int_a^xf$ est la primitive nulle en $a$.
- Intégration par parties : $\int_a^buv' = [uv]_a^b - \int_a^bu'v$ ($u$, $v$ de classe $\mathcal C^1$).
- Changement de variable : $\int_{\varphi(a)}^{\varphi(b)}f(t)\,\mathrm dt = \int_a^bf(\varphi(x))\varphi'(x)\,\mathrm dx$ ($\varphi$ de classe $\mathcal C^1$).
- Primitives de $\frac{1}{x^2 + a^2}$ : $\frac1a\arctan\frac xa$ ; de $\frac{1}{ax^2 + bx + c}$ : mise sous forme canonique ou décomposition en éléments simples.

## Équations du premier ordre : $y' + a(x)y = b(x)$

$a$ et $b$ continues sur un intervalle $I$.

> **Théorème.** Si $A$ est une primitive de $a$ sur $I$, les solutions de l'équation homogène $y' + a(x)y = 0$ sont les $x \mapsto \lambda e^{-A(x)}$, $\lambda \in \mathbb K$. Les solutions de l'équation complète sont $y = y_p + \lambda e^{-A}$, où $y_p$ est une solution particulière.

> **Méthode — Variation de la constante.** On cherche $y_p = \lambda(x)e^{-A(x)}$ : l'équation devient $\lambda'(x)e^{-A(x)} = b(x)$, d'où $\lambda$ par intégration.

> **Théorème — Problème de Cauchy.** Pour tout $x_0 \in I$ et $y_0 \in \mathbb K$, il existe une unique solution vérifiant $y(x_0) = y_0$.

**Principe de superposition** : si $y_1$ est solution avec le second membre $b_1$ et $y_2$ avec $b_2$, alors $y_1 + y_2$ est solution avec $b_1 + b_2$.

### Seconds membres usuels (coefficient $a$ constant)

- $b$ polynôme : chercher $y_p$ polynôme de même degré (degré + 1 si $a = 0$).
- $b(x) = Ce^{\mu x}$ : chercher $y_p = ke^{\mu x}$ si $\mu \ne -a$, $y_p = kxe^{\mu x}$ sinon.
- $b(x) = C\cos(\omega x)$ : passer en complexe avec $e^{i\omega x}$ et prendre la partie réelle.

## Équations du second ordre à coefficients constants

$y'' + ay' + by = f(x)$, avec $a, b$ constants.

> **Théorème — Équation homogène.** On résout l'équation caractéristique $r^2 + ar + b = 0$, de discriminant $\Delta$.
> - $\Delta > 0$, racines réelles $r_1 \ne r_2$ : $y = \lambda e^{r_1x} + \mu e^{r_2x}$.
> - $\Delta = 0$, racine double $r$ : $y = (\lambda x + \mu)e^{rx}$.
> - $\Delta < 0$, racines $\alpha \pm i\beta$ : $y = e^{\alpha x}(\lambda\cos\beta x + \mu\sin\beta x)$ (solutions réelles).
>
> Dans $\mathbb C$, avec deux racines distinctes, $y = \lambda e^{r_1x} + \mu e^{r_2x}$ avec $\lambda, \mu \in \mathbb C$.

### Solution particulière pour $f(x) = Pe^{mx}$ ($P$ polynôme, $m \in \mathbb C$)

Chercher $y_p = Q(x)e^{mx}$ avec $Q$ polynôme de degré $\deg P$ si $m$ n'est pas racine, $\deg P + 1$ si $m$ est racine simple, $\deg P + 2$ si $m$ est racine double. Pour un second membre en $\cos(\omega x)$ ou $\sin(\omega x)$, prendre la partie réelle ou imaginaire du cas $m = i\omega$.

> **Théorème — Problème de Cauchy.** Pour $x_0$, $y_0$, $y_0'$ donnés, il existe une unique solution telle que $y(x_0) = y_0$ et $y'(x_0) = y_0'$. L'ensemble des solutions de l'équation homogène est un plan vectoriel.

## Lien avec la physique

$y'' + \frac{\omega_0}{Q}y' + \omega_0^2y = 0$ : régime apériodique ($Q < \frac12$), critique ($Q = \frac12$), pseudo-périodique ($Q > \frac12$) selon le signe du discriminant.

## Exemple corrigé

**Énoncé.** Résoudre $y'' - 3y' + 2y = e^x$ avec $y(0) = 0$, $y'(0) = 0$.

**Solution.** $r^2 - 3r + 2 = (r - 1)(r - 2)$ : solutions homogènes $\lambda e^x + \mu e^{2x}$. Le second membre $e^x$ correspond à $m = 1$, racine simple : on cherche $y_p = kxe^x$. $y_p' = k(x + 1)e^x$, $y_p'' = k(x + 2)e^x$, d'où $k(x + 2) - 3k(x + 1) + 2kx = -k = 1$, $k = -1$. Donc $y = -xe^x + \lambda e^x + \mu e^{2x}$. $y(0) = \lambda + \mu = 0$ et $y'(0) = -1 + \lambda + 2\mu = 0$ : $\mu = 1$, $\lambda = -1$. Solution : $y = e^{2x} - (x + 1)e^x$.

## Exemple corrigé (variation de la constante)

**Énoncé.** Résoudre $xy' - y = x^2$ sur $]0, +\infty[$.

**Solution.** Forme normalisée : $y' - \frac yx = x$. Homogène : $A(x) = -\ln x$, solutions $\lambda x$. On pose $y = \lambda(x)x$ : $\lambda'x = x$, $\lambda = x + c$. Solutions : $y = x^2 + cx$.

## Pièges classiques

- Mettre l'équation sous forme **normalisée** (coefficient de $y'$ égal à 1) et travailler sur un intervalle où il ne s'annule pas.
- Les conditions initiales s'appliquent à la solution **générale**, pas à la solution homogène.
- Pour un second membre résonant ($m$ racine), multiplier par $x$ (ou $x^2$).
