---
titre: Suites et séries de fonctions
---
## L'essentiel

Une suite de fonctions peut converger simplement (point par point) ou uniformément (avec la même vitesse partout). Seule la convergence uniforme transmet en général la continuité et permet d'intervertir limite et intégrale sur un segment.

## Modes de convergence

[[fig:m2-suites-fonctions-1]]

- **Simple** : pour tout $x$, $f_n(x) \to f(x)$.
- **Uniforme** : $\|f_n - f\|_\infty = \sup_x|f_n(x) - f(x)| \to 0$.

[[fig:m2-suites-fonctions-2]]

> **Méthode.** Pour montrer la convergence uniforme, majorer $|f_n(x) - f(x)|$ par $\varepsilon_n \to 0$ indépendant de $x$ ; pour la réfuter, trouver $x_n$ avec $|f_n(x_n) - f(x_n)| \not\to 0$.

## Théorèmes de régularité

> **Théorème — Continuité.** Si les $f_n$ sont continues et convergent uniformément vers $f$ (sur tout segment de $I$), alors $f$ est continue.

> **Théorème — Intégration.** Si les $f_n$ sont continues et convergent uniformément sur $[a, b]$, alors $\int_a^bf_n \to \int_a^bf$.

> **Théorème — Dérivation.** Si les $f_n$ sont $\mathcal C^1$, si $(f_n)$ converge simplement et si $(f_n')$ converge uniformément (sur tout segment) vers $g$, alors $f$ est $\mathcal C^1$ et $f' = g$.

## Séries de fonctions

Mêmes énoncés pour $\sum f_n$ avec les sommes partielles. Outil principal : la **convergence normale**, $\sum\|f_n\|_\infty < +\infty$, qui implique la convergence uniforme.

> **Théorème de la double limite.** Si $\sum f_n$ converge uniformément et $f_n(x) \to \ell_n$ en $a$, alors $\sum\ell_n$ converge et $\sum f_n(x) \to \sum\ell_n$.

## Approximation

> **Théorème de Weierstrass.** Toute fonction continue sur un segment est limite uniforme d'une suite de polynômes.

## Exemple corrigé

**Énoncé.** Étudier la convergence de $f_n(x) = \frac{x}{1 + nx^2}$ sur $\mathbb R$.

**Solution.** Simplement vers 0. On étudie $f_n$ : maximum de $|f_n|$ atteint en $x = \frac{1}{\sqrt n}$, égal à $\frac{1}{2\sqrt n} \to 0$. Donc $\|f_n\|_\infty \to 0$ : convergence uniforme sur $\mathbb R$.

## Pièges classiques

- Une limite simple de fonctions continues peut être discontinue ($x^n$ sur $[0, 1]$).
- Convergence normale ⇒ uniforme, mais la réciproque est fausse.
