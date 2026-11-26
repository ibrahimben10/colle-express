---
titre: Analyse asymptotique
---
## L'essentiel

Comparer des fonctions ou des suites au voisinage d'un point : relations de domination ($O$), de négligeabilité ($o$) et d'équivalence ($\sim$), et développements limités, outils de base pour lever les indéterminations.

## Relations de comparaison

- $f = o(g)$ : $f/g \to 0$ ; $f = O(g)$ : $f/g$ bornée ; $f \sim g$ : $f/g \to 1$ (si $g$ ne s'annule pas au voisinage).
- $f \sim g \Leftrightarrow f = g + o(g)$.
- Les équivalents se **multiplient**, se **divisent**, s'élèvent à une puissance fixe ; ils ne s'**additionnent** pas et ne se composent pas en général.

## Développements limités

[[fig:m1-asymptotique-1]]

> **Théorème de Taylor-Young.** Si $f$ est de classe $\mathcal C^n$ au voisinage de $a$ : $f(x) = \sum_{k=0}^n\dfrac{f^{(k)}(a)}{k!}(x - a)^k + o\big((x - a)^n\big)$.

DL usuels en 0 :

| Fonction | Développement |
|---|---|
| $e^x$ | $1 + x + \frac{x^2}{2} + \dots + \frac{x^n}{n!} + o(x^n)$ |
| $\ln(1 + x)$ | $x - \frac{x^2}{2} + \frac{x^3}{3} - \dots + (-1)^{n-1}\frac{x^n}{n} + o(x^n)$ |
| $(1 + x)^\alpha$ | $1 + \alpha x + \frac{\alpha(\alpha - 1)}{2}x^2 + o(x^2)$ |
| $\sin x$ | $x - \frac{x^3}{6} + \frac{x^5}{120} + o(x^6)$ |
| $\cos x$ | $1 - \frac{x^2}{2} + \frac{x^4}{24} + o(x^5)$ |
| $\frac{1}{1 - x}$ | $1 + x + x^2 + \dots + x^n + o(x^n)$ |
| $\arctan x$ | $x - \frac{x^3}{3} + \frac{x^5}{5} + o(x^6)$ |

Opérations : somme, produit (tronquer au bon ordre), composée ($u \to 0$), quotient via $\frac{1}{1 - u}$, primitivation terme à terme.

## Méthode

1. Chercher un équivalent simple pour lever une forme indéterminée.
2. Si les équivalents se compensent (différence), passer aux DL, à un ordre suffisant.
3. Applications : limites, position d'une courbe par rapport à sa tangente ou à une asymptote.

## Exemple corrigé

**Énoncé.** Calculer $\displaystyle\lim_{x\to0}\frac{e^x - 1 - \sin x}{x^2}$.

**Solution.** $e^x = 1 + x + \frac{x^2}{2} + o(x^2)$ et $\sin x = x + o(x^2)$. Donc $e^x - 1 - \sin x = \frac{x^2}{2} + o(x^2)$, et la limite vaut $\frac12$.

## Pièges classiques

- Ne jamais additionner des équivalents : $x + x^2 \sim x$ et $-x \sim -x$, mais la somme vaut $x^2$, pas 0.
- $f \sim g$ n'implique pas $e^f \sim e^g$.
- Écrire un DL toujours avec son reste $o(\cdot)$.
