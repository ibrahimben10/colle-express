---
titre: Intégrales à paramètre
---
## L'essentiel

Étudier $F(x) = \int_If(x, t)\,\mathrm dt$ : continuité et dérivabilité s'obtiennent par des théorèmes de domination, qui exigent une majoration **indépendante du paramètre**.

> **Théorème — Continuité.** Si $f$ est continue par rapport à $x$, continue par morceaux par rapport à $t$, et s'il existe $\varphi$ intégrable sur $I$ telle que $|f(x, t)| \le \varphi(t)$ pour tous $x \in A$, $t \in I$, alors $F$ est continue sur $A$.

> **Théorème — Dérivation (Leibniz).** Si de plus $\frac{\partial f}{\partial x}$ existe, est continue en $x$ et dominée par $\psi$ intégrable, alors $F$ est $\mathcal C^1$ et $F'(x) = \int_I\frac{\partial f}{\partial x}(x, t)\,\mathrm dt$.

Version locale : la domination sur tout segment $[a, b] \subset A$ suffit pour conclure sur $A$.

## La fonction Gamma

$\Gamma(x) = \int_0^{+\infty}t^{x-1}e^{-t}\,\mathrm dt$ est définie et $\mathcal C^\infty$ sur $]0, +\infty[$ ; $\Gamma(x + 1) = x\Gamma(x)$, $\Gamma(n + 1) = n!$, $\Gamma(\frac12) = \sqrt\pi$.

## Méthode

1. Vérifier que $F(x)$ est définie (intégrabilité pour chaque $x$).
2. Trouver une domination indépendante de $x$ (éventuellement sur des segments).
3. Appliquer le théorème ; souvent, $F$ vérifie ensuite une équation différentielle simple.

## Exemple corrigé

**Énoncé.** Calculer $F(x) = \int_0^{+\infty}e^{-t^2}\cos(xt)\,\mathrm dt$.

**Solution.** $|\partial_x f| = |te^{-t^2}\sin(xt)| \le te^{-t^2}$, intégrable : $F$ est $\mathcal C^1$ et $F'(x) = -\int_0^{+\infty}te^{-t^2}\sin(xt)\,\mathrm dt$. Une intégration par parties donne $F'(x) = -\frac x2F(x)$. Donc $F(x) = F(0)e^{-x^2/4}$ avec $F(0) = \frac{\sqrt\pi}{2}$ : $F(x) = \frac{\sqrt\pi}{2}e^{-x^2/4}$.

## Pièges classiques

- Une domination qui dépend de $x$ ne vaut rien.
- Ne pas oublier de justifier que l'intégrale définissant $F$ existe.
