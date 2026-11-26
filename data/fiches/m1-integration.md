---
titre: Intégration sur un segment
---
## L'essentiel

L'intégrale d'une fonction continue (par morceaux) sur un segment se définit à partir des fonctions en escalier. Le théorème fondamental la relie aux primitives ; les sommes de Riemann l'approchent ; la formule de Taylor avec reste intégral donne des inégalités précises.

## Construction et propriétés

- Fonctions en escalier, puis fonctions **continues par morceaux** sur $[a, b]$ (nombre fini de discontinuités, avec limites finies à gauche et à droite).
- **Linéarité**, **relation de Chasles**, **positivité** : $f \ge 0 \Rightarrow \int_a^bf \ge 0$ ($a \le b$), d'où la croissance.
- $\left|\int_a^bf\right| \le \int_a^b|f| \le (b - a)\sup|f|$.

> **Propriété — Stricte positivité.** Si $f$ est **continue**, positive sur $[a, b]$ ($a < b$) et $\int_a^bf = 0$, alors $f = 0$ sur $[a, b]$.

**Valeur moyenne** $\frac{1}{b - a}\int_a^bf$ ; inégalité de Cauchy-Schwarz $\left(\int fg\right)^2 \le \int f^2\int g^2$.

## Sommes de Riemann

[[fig:m1-integration-1]]

> **Théorème.** Si $f$ est continue par morceaux sur $[a, b]$ : $\frac{b - a}{n}\sum_{k=0}^{n-1}f\left(a + k\frac{b - a}{n}\right) \to \int_a^bf$. Si $f$ est $M$-lipschitzienne, l'erreur est au plus $\frac{M(b - a)^2}{2n}$.

Usage : calculer des limites de sommes, en reconnaissant $\frac1n\sum f(\frac kn) \to \int_0^1f$.

## Intégrale et primitive

> **Théorème fondamental.** Si $f$ est continue sur $I$ et $a \in I$, $F(x) = \int_a^xf(t)\,\mathrm dt$ est l'unique primitive de $f$ nulle en $a$ ; et pour toute primitive $G$, $\int_a^bf = G(b) - G(a)$.

Dérivée d'une intégrale à bornes variables : $\frac{\mathrm d}{\mathrm dx}\int_{u(x)}^{v(x)}f = v'(x)f(v(x)) - u'(x)f(u(x))$.

- **Intégration par parties** : $\int_a^buv' = [uv]_a^b - \int_a^bu'v$ ($u$, $v$ de classe $\mathcal C^1$).
- **Changement de variable** : $\int_{\varphi(\alpha)}^{\varphi(\beta)}f(x)\,\mathrm dx = \int_\alpha^\beta f(\varphi(t))\varphi'(t)\,\mathrm dt$ ($\varphi$ de classe $\mathcal C^1$).
- Parité : pour $f$ impaire, $\int_{-a}^af = 0$ ; paire, $2\int_0^af$. Périodicité : $\int_a^{a+T}f$ ne dépend pas de $a$.

### Primitives usuelles

$\int\frac{\mathrm dx}{x} = \ln|x|$ ; $\int\frac{\mathrm dx}{1 + x^2} = \arctan x$ ; $\int\frac{\mathrm dx}{\sqrt{1 - x^2}} = \arcsin x$ ; $\int\tan = -\ln|\cos|$ ; $\int e^{ax}\cos bx$ : prendre la partie réelle de $\int e^{(a+ib)x}$ ; fractions rationnelles : éléments simples ; $\cos^p\sin^q$ : linéarisation ou changement de variable.

## Formules de Taylor

> **Théorème — Taylor avec reste intégral.** Si $f$ est de classe $\mathcal C^{n+1}$ sur $I$ : $f(b) = \sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(b - a)^k + \int_a^b\frac{(b - t)^n}{n!}f^{(n+1)}(t)\,\mathrm dt$.

> **Théorème — Inégalité de Taylor-Lagrange.** Si $|f^{(n+1)}| \le M$ sur $I$ : $\left|f(b) - \sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(b - a)^k\right| \le \frac{M|b - a|^{n+1}}{(n + 1)!}$.

Application : $e^x = \sum\frac{x^k}{k!}$ en passant à la limite. Taylor-Young (local) est dans la fiche d'analyse asymptotique ; Taylor-Lagrange et reste intégral sont **globaux**.

## Fonctions à valeurs complexes

On intègre partie réelle et partie imaginaire. Linéarité, Chasles, $\left|\int f\right| \le \int|f|$, IPP, changement de variable et Taylor (reste intégral, inégalité) restent vrais.

## Exemple corrigé

**Énoncé.** Calculer $\lim_{n\to\infty}\sum_{k=1}^n\frac{n}{n^2 + k^2}$.

**Solution.** $\sum_{k=1}^n\frac{n}{n^2 + k^2} = \frac1n\sum_{k=1}^n\frac{1}{1 + (k/n)^2}$ : somme de Riemann de $f(x) = \frac{1}{1 + x^2}$ sur $[0, 1]$. La limite vaut $\int_0^1\frac{\mathrm dx}{1 + x^2} = \frac\pi4$.

## Exemple corrigé (IPP)

**Énoncé.** Calculer $I_n = \int_0^1x^ne^x\,\mathrm dx$ par récurrence.

**Solution.** IPP avec $u = x^n$, $v' = e^x$ : $I_n = e - nI_{n-1}$, et $I_0 = e - 1$. Par exemple $I_1 = 1$, $I_2 = e - 2$.

## Pièges classiques

- La stricte positivité exige la **continuité**.
- Dans un changement de variable, changer aussi les **bornes** et l'élément $\mathrm dx$.
- On ne peut pas intégrer une inégalité si les bornes sont dans le « mauvais » ordre sans changer le sens.
