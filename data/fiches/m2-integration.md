---
titre: Intégration sur un intervalle quelconque
---
## L'essentiel

On étend l'intégrale à des intervalles non bornés ou à des fonctions non bornées. La notion clé est l'**intégrabilité** (convergence absolue), et le théorème de convergence dominée permet d'intervertir limite et intégrale.

## Intégrales généralisées

$\int_a^{+\infty}f$ converge si $\int_a^xf$ a une limite finie quand $x \to +\infty$. $f$ est **intégrable** si $\int|f|$ converge ; l'intégrabilité implique la convergence.

[[fig:m2-integration-1]]

> **Propriété — Intégrales de référence.** $\int_1^{+\infty}\frac{\mathrm dx}{x^\alpha}$ converge ssi $\alpha > 1$ ; $\int_0^1\frac{\mathrm dx}{x^\alpha}$ converge ssi $\alpha < 1$ ; $\int_0^{+\infty}e^{-ax}\,\mathrm dx$ converge ssi $a > 0$.

> **Théorème — Comparaison (fonctions positives).** Si $0 \le f \le g$ et $g$ est intégrable, $f$ l'est ; si $f \sim g$ (positives) au voisinage de la borne, elles sont de même nature.

Intégration par parties et changement de variable ($\mathcal C^1$ strictement monotone) restent valables, en vérifiant la convergence des termes.

## Théorèmes d'interversion

> **Théorème de convergence dominée.** Si les $f_n$ sont continues par morceaux, convergent simplement vers $f$ continue par morceaux, et s'il existe $\varphi$ intégrable avec $|f_n| \le \varphi$ pour tout $n$ (domination), alors $\int_If_n \to \int_If$.

> **Théorème d'intégration terme à terme.** Si $\sum f_n$ converge simplement vers $f$ et si $\sum\int|f_n| < +\infty$, alors $f$ est intégrable et $\int f = \sum\int f_n$.

## Exemple corrigé

**Énoncé.** Calculer $\displaystyle\lim_{n\to\infty}\int_0^{+\infty}\frac{\mathrm dx}{1 + x^n}$.

**Solution.** Pour $n \ge 2$, $f_n(x) = \frac{1}{1 + x^n}$ converge simplement vers $f$ valant 1 sur $[0, 1[$, $\frac12$ en 1 et 0 sur $]1, +\infty[$ (continue par morceaux). Domination : $|f_n| \le 1$ sur $[0, 1]$ et $|f_n(x)| \le \frac{1}{x^n} \le \frac{1}{x^2}$ sur $[1, +\infty[$ ; la fonction $\varphi$ égale à 1 sur $[0, 1]$ et à $\frac{1}{x^2}$ ensuite est intégrable. Par convergence dominée, la limite vaut $\int_0^1 1\,\mathrm dx = 1$.

## Pièges classiques

- Ne pas oublier d'étudier **chaque borne** séparément.
- La domination doit être indépendante de $n$.
- $\int_0^{+\infty}\frac{\sin x}{x}\,\mathrm dx$ converge mais $\frac{\sin x}{x}$ n'est pas intégrable.
