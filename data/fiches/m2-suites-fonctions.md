---
titre: Suites et séries de fonctions
---
## L'essentiel

Une suite de fonctions peut converger simplement (point par point) ou uniformément (avec un contrôle valable partout). La convergence uniforme transmet la continuité, permet d'intervertir limite et intégrale sur un segment, et, appliquée aux dérivées, de dériver terme à terme. Pour les séries, l'outil principal est la convergence normale.

## Modes de convergence

[[fig:m2-suites-fonctions-1]]

- **Convergence simple** sur $A$ : pour tout $x \in A$, $f_n(x) \to f(x)$.
- **Convergence uniforme** sur $A$ : $\|f_n - f\|_{\infty,A} = \sup_{x\in A}|f_n(x) - f(x)| \to 0$. Uniforme implique simple.

[[fig:m2-suites-fonctions-2]]

> **Méthode.**
> 1. Trouver la limite simple $f$ (pour $x$ fixé).
> 2. Pour prouver la convergence uniforme : majorer $|f_n(x) - f(x)| \le \varepsilon_n$ avec $\varepsilon_n \to 0$ **indépendant de $x$**, ou étudier la fonction $f_n - f$ pour calculer son sup.
> 3. Pour la réfuter : trouver $x_n$ tel que $|f_n(x_n) - f(x_n)| \not\to 0$, ou utiliser un théorème (une limite discontinue de fonctions continues).
> 4. Souvent, on obtient la convergence uniforme sur $[a, +\infty[$ ou sur tout segment, mais pas sur l'intervalle entier.

## Régularité de la limite

> **Théorème — Continuité.** Si les $f_n$ sont continues sur $I$ et convergent uniformément vers $f$ sur tout segment de $I$ (ou au voisinage de chaque point), alors $f$ est continue sur $I$.

> **Théorème de la double limite.** Si $f_n \to f$ uniformément sur $A$ et si, pour chaque $n$, $f_n(x) \to \ell_n$ quand $x \to a$ (adhérent à $A$, éventuellement infini), alors $(\ell_n)$ converge vers un $\ell$ et $f(x) \to \ell$ quand $x \to a$.

> **Théorème — Intégration sur un segment.** Si les $f_n$ sont continues et convergent uniformément vers $f$ sur $[a, b]$, alors $\int_a^bf_n \to \int_a^bf$.

> **Théorème — Dérivation.** Si les $f_n$ sont de classe $\mathcal C^1$ sur $I$, si $(f_n)$ converge simplement vers $f$ et si $(f_n')$ converge uniformément sur tout segment vers $g$, alors $f$ est $\mathcal C^1$ et $f' = g$. Version $\mathcal C^k$ : convergence simple des $f_n^{(j)}$ pour $j < k$ et uniforme de $f_n^{(k)}$.

## Séries de fonctions

On applique ce qui précède aux sommes partielles $S_n = \sum_{k\le n}f_k$.

- Convergence simple, uniforme : la convergence uniforme de $\sum f_n$ équivaut à celle de la suite des restes vers 0 : $\sup|R_n| \to 0$.
- **Convergence normale** : $\sum\|f_n\|_\infty < +\infty$. Elle implique la convergence absolue en tout point et la convergence uniforme.

> **Théorèmes pour les séries.**
> - Si les $f_n$ sont continues et $\sum f_n$ converge uniformément (normalement) sur tout segment, la somme est continue.
> - **Double limite** : si $\sum f_n$ converge uniformément et $f_n(x) \to \ell_n$ en $a$, alors $\sum\ell_n$ converge et $\sum f_n(x) \to \sum\ell_n$.
> - **Intégration terme à terme sur un segment** si la convergence est uniforme.
> - **Dérivation terme à terme** si $\sum f_n$ converge simplement et $\sum f_n'$ converge uniformément sur tout segment.

> **Méthode — Séries alternées de fonctions.** Si pour chaque $x$, $\sum(-1)^na_n(x)$ vérifie le critère des séries alternées, alors $|R_n(x)| \le a_{n+1}(x)$ : la convergence est uniforme dès que $\sup_xa_{n+1}(x) \to 0$, même sans convergence normale.

## Approximation

> **Théorème de Weierstrass.** Toute fonction continue sur un segment est limite uniforme d'une suite de polynômes.

Toute fonction continue par morceaux sur un segment est limite uniforme de fonctions en escalier.

## Exemple corrigé

**Énoncé.** Étudier la convergence de $f_n(x) = \frac{x}{1 + nx^2}$ sur $\mathbb R$.

**Solution.** Limite simple : 0. $f_n$ est impaire ; sur $[0, +\infty[$, $f_n'(x) = \frac{1 - nx^2}{(1 + nx^2)^2}$ : maximum en $\frac{1}{\sqrt n}$, égal à $\frac{1}{2\sqrt n}$. Donc $\|f_n\|_\infty = \frac{1}{2\sqrt n} \to 0$ : convergence uniforme sur $\mathbb R$.

## Exemple corrigé (fonction zêta)

**Énoncé.** Montrer que $\zeta(x) = \sum_{n\ge1}\frac{1}{n^x}$ est continue sur $]1, +\infty[$ et calculer sa limite en $+\infty$.

**Solution.** Sur $[a, +\infty[$ avec $a > 1$ : $\left|\frac{1}{n^x}\right| \le \frac{1}{n^a}$, terme d'une série convergente : convergence normale, donc $\zeta$ est continue sur $[a, +\infty[$ pour tout $a > 1$, donc sur $]1, +\infty[$. Double limite (convergence normale sur $[2, +\infty[$) : $\frac{1}{n^x} \to 0$ pour $n \ge 2$ et $\to 1$ pour $n = 1$, donc $\zeta(x) \to 1$.

## Pièges classiques

- Une limite simple de fonctions continues peut être discontinue ($x^n$ sur $[0, 1]$).
- Convergence normale ⇒ uniforme, mais pas l'inverse.
- Pour dériver, c'est la suite des **dérivées** qui doit converger uniformément.
- Le sup doit être pris sur $x$ **avant** de faire tendre $n$ vers l'infini.
