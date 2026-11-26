---
titre: Intégrales à paramètre
---
## L'essentiel

On étudie $F(x) = \int_If(x, t)\,\mathrm dt$ comme une fonction de $x$. Continuité et dérivabilité s'obtiennent par des théorèmes de **domination**, qui exigent une majoration de $|f|$ (ou de $|\partial_xf|$) par une fonction intégrable **indépendante de $x$**, au moins localement.

## Théorèmes

$A$ est un intervalle (ou une partie d'un espace normé pour la continuité), $I$ un intervalle.

> **Théorème — Continuité.** Si $f : A \times I \to \mathbb K$ vérifie : pour tout $t$, $x \mapsto f(x, t)$ est continue ; pour tout $x$, $t \mapsto f(x, t)$ est continue par morceaux ; et il existe $\varphi$ intégrable sur $I$ avec $|f(x, t)| \le \varphi(t)$ pour tous $x \in A$, $t \in I$ ; alors $F$ est définie et continue sur $A$.

> **Théorème — Dérivation (Leibniz).** Si de plus $\frac{\partial f}{\partial x}$ existe, est continue en $x$ et continue par morceaux en $t$, et si $\left|\frac{\partial f}{\partial x}(x, t)\right| \le \psi(t)$ avec $\psi$ intégrable (indépendante de $x$), alors $F$ est de classe $\mathcal C^1$ et $F'(x) = \int_I\frac{\partial f}{\partial x}(x, t)\,\mathrm dt$.

Version $\mathcal C^k$ : domination de chaque $\partial_x^jf$ ($j \le k$), ou simple intégrabilité pour $j < k$ et domination pour $j = k$.

> **Méthode — Domination locale.** Si la domination n'est possible que sur chaque segment $[a, b] \subset A$ (ou sur $[a, +\infty[$ pour tout $a > 0$), on conclut sur chacun, donc sur $A$ entier, la continuité et la dérivabilité étant des propriétés locales.

### Limites aux bornes

Utiliser la **convergence dominée** (avec une suite $x_n \to x_0$) ou un encadrement direct de $F(x)$.

## La fonction Gamma

$\Gamma(x) = \int_0^{+\infty}t^{x-1}e^{-t}\,\mathrm dt$.

- Définie sur $]0, +\infty[$ : en 0, $t^{x-1}e^{-t} \sim t^{x-1}$, intégrable si $x > 0$ ; en $+\infty$, $o(\frac{1}{t^2})$.
- $\mathcal C^\infty$ sur $]0, +\infty[$ (domination sur $[a, b]$ par $t^{a-1}|\ln t|^ke^{-t}$ pour $t \le 1$ et $t^{b-1}|\ln t|^ke^{-t}$ pour $t \ge 1$), avec $\Gamma^{(k)}(x) = \int_0^{+\infty}(\ln t)^kt^{x-1}e^{-t}\,\mathrm dt$.
- $\Gamma(x + 1) = x\Gamma(x)$ (IPP) ; $\Gamma(n + 1) = n!$ ; $\Gamma(\frac12) = \sqrt\pi$ ; $\Gamma$ est log-convexe, $\Gamma(x) \sim \frac1x$ en $0^+$.

## Méthode générale

1. Montrer que $F(x)$ est définie (intégrabilité de $t \mapsto f(x, t)$ pour chaque $x$).
2. Continuité : domination de $|f|$ indépendante de $x$ (localement).
3. Dérivation : domination de $|\partial_xf|$ ; écrire $F'$.
4. Exploiter : souvent $F$ vérifie une équation différentielle simple (après IPP), ou $F'$ se calcule explicitement ; puis calculer une valeur particulière ou une limite pour fixer la constante.

## Exemple corrigé

**Énoncé.** Calculer $F(x) = \int_0^{+\infty}e^{-t^2}\cos(xt)\,\mathrm dt$.

**Solution.** $|e^{-t^2}\cos(xt)| \le e^{-t^2}$ intégrable : $F$ est définie et continue. $|\partial_xf| = |te^{-t^2}\sin(xt)| \le te^{-t^2}$, intégrable : $F$ est $\mathcal C^1$ et $F'(x) = -\int_0^{+\infty}te^{-t^2}\sin(xt)\,\mathrm dt$. IPP avec $u = \sin(xt)$, $v' = -te^{-t^2}$, $v = \frac12e^{-t^2}$ : $F'(x) = \left[\frac12e^{-t^2}\sin(xt)\right]_0^{+\infty} - \frac x2\int_0^{+\infty}e^{-t^2}\cos(xt)\,\mathrm dt = -\frac x2F(x)$. Donc $F(x) = F(0)e^{-x^2/4} = \frac{\sqrt\pi}{2}e^{-x^2/4}$.

## Exemple corrigé (transformée de Laplace)

**Énoncé.** $F(x) = \int_0^{+\infty}\frac{e^{-xt}}{1 + t^2}\,\mathrm dt$ pour $x \ge 0$ : continuité et limite en $+\infty$.

**Solution.** $\left|\frac{e^{-xt}}{1 + t^2}\right| \le \frac{1}{1 + t^2}$, intégrable sur $[0, +\infty[$ et indépendante de $x \ge 0$ : $F$ est continue sur $[0, +\infty[$. Pour $x_n \to +\infty$, l'intégrande tend vers 0 pour $t > 0$, avec la même domination : $F(x) \to 0$ par convergence dominée. (On peut aussi majorer $0 \le F(x) \le \int_0^{+\infty}e^{-xt}\,\mathrm dt = \frac1x$.)

## Pièges classiques

- Une majoration qui dépend de $x$ n'est pas une domination.
- Ne pas oublier de justifier que l'intégrale définissant $F$ existe.
- La continuité de $\partial_xf$ en $x$ fait partie des hypothèses.
