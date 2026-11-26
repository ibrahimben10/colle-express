---
titre: Intégration sur un intervalle quelconque
---
## L'essentiel

On étend l'intégrale à des intervalles non bornés ou à des fonctions non bornées aux bornes. La notion clé est l'**intégrabilité** (convergence absolue). Le théorème de convergence dominée et l'intégration terme à terme permettent d'intervertir limite (ou somme) et intégrale.

## Intégrales généralisées

- Sur $[a, b[$ ($b$ fini ou $+\infty$) : $\int_a^bf$ **converge** si $\int_a^xf$ a une limite finie quand $x \to b$. Sur $]a, b[$, on coupe en un point $c$ et on étudie chaque borne séparément.
- Si $f$ est continue sur $[a, b]$ avec $b$ fini, l'intégrale « faussement impropre » converge (prolongement par continuité).
- Linéarité, Chasles, positivité, croissance pour les intégrales convergentes.

### Intégrales de référence

[[fig:m2-integration-1]]

> **Propriété.**
> - $\int_1^{+\infty}\frac{\mathrm dx}{x^\alpha}$ converge si et seulement si $\alpha > 1$ ;
> - $\int_0^1\frac{\mathrm dx}{x^\alpha}$ converge si et seulement si $\alpha < 1$ ;
> - $\int_0^{+\infty}e^{-ax}\,\mathrm dx$ converge si et seulement si $a > 0$ ;
> - $\int_0^1\ln x\,\mathrm dx = -1$ converge.

## Intégrabilité

> **Définition.** $f$ continue par morceaux sur $I$ est **intégrable** si $\int_I|f|$ converge. L'intégrabilité implique la convergence, et $\left|\int_If\right| \le \int_I|f|$.

> **Théorème — Comparaison (fonctions positives ou en module).** Au voisinage de la borne étudiée :
> - si $|f| \le g$ et $g$ intégrable, $f$ est intégrable ;
> - si $f = O(g)$ ou $o(g)$ avec $g$ intégrable, $f$ est intégrable ;
> - si $f \sim g$ et $g \ge 0$, $f$ et $g$ sont de même nature.

> **Méthode.** Pour $\int_0^{+\infty}$ : en $+\infty$, comparer à $\frac{1}{x^2}$ (montrer $x^2f(x) \to 0$) ; en $0$, comparer à $\frac{1}{x^\alpha}$ avec $\alpha < 1$.

Une intégrale peut converger sans que la fonction soit intégrable : $\int_1^{+\infty}\frac{\sin x}{x}\,\mathrm dx$ converge (intégration par parties), mais $\frac{\sin x}{x}$ n'est pas intégrable.

## Calcul

- **Intégration par parties** : $\int_a^buv' = [uv]_a^b - \int_a^bu'v$, valable si deux des trois termes convergent (limites du crochet aux bornes).
- **Changement de variable** $\varphi$ de classe $\mathcal C^1$, **strictement monotone** et bijective : les intégrales $\int f(\varphi(t))\varphi'(t)\,\mathrm dt$ et $\int f(x)\,\mathrm dx$ sont de même nature et égales.
- Intégrale de Gauss : $\int_{-\infty}^{+\infty}e^{-x^2}\,\mathrm dx = \sqrt\pi$.

## Comparaison série-intégrale

Si $f$ est continue, positive, décroissante sur $[a, +\infty[$, alors $\sum f(n)$ et $\int_a^{+\infty}f$ sont de même nature, avec encadrement des restes.

## Théorèmes d'interversion

> **Théorème de convergence dominée.** Soit $(f_n)$ continues par morceaux sur $I$, convergeant simplement vers $f$ continue par morceaux. S'il existe $\varphi$ **intégrable** sur $I$ avec $|f_n(x)| \le \varphi(x)$ pour tout $n$ et tout $x$ (domination), alors les $f_n$ et $f$ sont intégrables et $\int_If_n \to \int_If$.

Version continue : pour une famille $f_\lambda$ avec $\lambda \to \lambda_0$, par caractérisation séquentielle.

> **Théorème d'intégration terme à terme.** Si les $f_n$ sont intégrables, si $\sum f_n$ converge simplement vers $f$ continue par morceaux, et si $\sum\int_I|f_n| < +\infty$, alors $f$ est intégrable et $\int_If = \sum_n\int_If_n$.

Cas **positif** : si les $f_n \ge 0$, $\int\sum f_n = \sum\int f_n$ dans $[0, +\infty]$ (sans autre hypothèse). Si $\sum\int|f_n|$ diverge, essayer la convergence dominée sur les sommes partielles (séries alternées).

## Exemple corrigé

**Énoncé.** Calculer $\lim_{n\to\infty}\int_0^{+\infty}\frac{\mathrm dx}{1 + x^n}$.

**Solution.** Pour $n \ge 2$, $f_n(x) = \frac{1}{1 + x^n}$ converge simplement vers $f$ valant 1 sur $[0, 1[$, $\frac12$ en 1, 0 sur $]1, +\infty[$. Domination : $f_n \le 1$ sur $[0, 1]$ et $f_n(x) \le \frac{1}{x^n} \le \frac{1}{x^2}$ sur $[1, +\infty[$ ; $\varphi$ (1 sur $[0, 1]$, $\frac{1}{x^2}$ ensuite) est intégrable. Par convergence dominée, la limite est $\int_0^1 1\,\mathrm dx = 1$.

## Exemple corrigé (terme à terme)

**Énoncé.** Montrer que $\int_0^1\frac{\ln x}{1 - x}\,\mathrm dx = -\frac{\pi^2}{6}$.

**Solution.** Sur $]0, 1[$, $\frac{-\ln x}{1 - x} = \sum_{n\ge0}(-\ln x)x^n$, termes positifs. $\int_0^1(-\ln x)x^n\,\mathrm dx = \frac{1}{(n + 1)^2}$ (IPP). Par intégration terme à terme de fonctions positives, $\int_0^1\frac{-\ln x}{1 - x}\,\mathrm dx = \sum\frac{1}{(n + 1)^2} = \frac{\pi^2}{6}$.

## Pièges classiques

- Étudier **chaque borne** séparément ; ne pas écrire $\int_{-\infty}^{+\infty}$ comme une limite symétrique $\int_{-A}^A$.
- La domination doit être **indépendante de $n$**.
- Pour l'IPP, vérifier l'existence des limites du crochet.
