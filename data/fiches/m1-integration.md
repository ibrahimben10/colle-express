---
titre: Intégration sur un segment
---
## L'essentiel

L'intégrale d'une fonction continue (ou continue par morceaux) sur un segment est la limite des sommes de Riemann. Le théorème fondamental relie intégrale et primitive.

## Propriétés

[[fig:m1-integration-1]]

- **Linéarité**, **relation de Chasles**, **positivité** : si $f \ge 0$ et $a \le b$, alors $\int_a^bf \ge 0$ ; croissance de l'intégrale.
- $\left|\int_a^bf\right| \le \int_a^b|f|$ ($a \le b$).

> **Propriété — Stricte positivité.** Si $f$ est **continue**, positive sur $[a, b]$ ($a < b$) et $\int_a^bf = 0$, alors $f$ est nulle sur $[a, b]$.

> **Théorème — Sommes de Riemann.** Si $f$ est continue sur $[a, b]$ : $\dfrac{b - a}{n}\displaystyle\sum_{k=0}^{n-1}f\!\left(a + k\frac{b - a}{n}\right) \xrightarrow[n\to+\infty]{} \int_a^bf$.

## Théorème fondamental

> **Théorème fondamental de l'analyse.** Si $f$ est continue sur un intervalle $I$ et $a \in I$, $F(x) = \int_a^xf(t)\,\mathrm dt$ est l'unique primitive de $f$ qui s'annule en $a$ ; elle est de classe $\mathcal C^1$ et $F' = f$.

## Techniques de calcul

- **Intégration par parties** ($u$, $v$ de classe $\mathcal C^1$) : $\int_a^bu'v = [uv]_a^b - \int_a^buv'$.
- **Changement de variable** ($\varphi$ de classe $\mathcal C^1$) : $\int_{\varphi(\alpha)}^{\varphi(\beta)}f(x)\,\mathrm dx = \int_\alpha^\beta f(\varphi(t))\varphi'(t)\,\mathrm dt$.
- Fractions rationnelles : décomposition en éléments simples.

> **Formule de Taylor avec reste intégral.** Pour $f$ de classe $\mathcal C^{n+1}$ : $f(b) = \sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(b - a)^k + \int_a^b\frac{(b - t)^n}{n!}f^{(n+1)}(t)\,\mathrm dt$ ; d'où l'inégalité de Taylor-Lagrange.

## Exemple corrigé

**Énoncé.** Calculer $\displaystyle\lim_{n\to\infty}\sum_{k=1}^n\frac{n}{n^2 + k^2}$.

**Solution.** $\displaystyle\sum_{k=1}^n\frac{n}{n^2 + k^2} = \frac1n\sum_{k=1}^n\frac{1}{1 + (k/n)^2}$ : c'est une somme de Riemann de $x \mapsto \frac{1}{1 + x^2}$ sur $[0, 1]$ (avec les points de droite). La limite vaut $\int_0^1\frac{\mathrm dx}{1 + x^2} = \arctan 1 = \frac\pi4$.

## Pièges classiques

- Positivité et croissance de l'intégrale supposent les bornes dans le **bon ordre**.
- Dans un changement de variable, changer aussi les bornes et le $\mathrm dx$.
- Une primitive n'existe a priori que pour une fonction continue sur un **intervalle**.
