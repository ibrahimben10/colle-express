---
titre: Analyse asymptotique
---
## L'essentiel

Comparer des fonctions ou des suites au voisinage d'un point ($o$, $O$, $\sim$) et approcher une fonction par un polynôme (développements limités). C'est l'outil principal pour lever les formes indéterminées et étudier les courbes et les séries.

## Relations de comparaison

Au voisinage de $a$ (ou pour les suites, quand $n \to +\infty$) :

- $f = o(g)$ : $f = \varepsilon g$ avec $\varepsilon \to 0$ ; si $g$ ne s'annule pas, $\frac fg \to 0$.
- $f = O(g)$ : $f = \beta g$ avec $\beta$ bornée.
- $f \sim g$ : $f - g = o(g)$ ; si $g$ ne s'annule pas, $\frac fg \to 1$.

> **Propriété — Règles sur les équivalents.**
> - $\sim$ est compatible avec le **produit**, le **quotient** et les **puissances** fixes.
> - Il n'est **pas** compatible avec la somme ni avec la composition par une fonction en général ($e^{f}$ et $e^{g}$).
> - Si $f \sim g$ et $g \to \ell$, alors $f \to \ell$ ; deux fonctions équivalentes ont le même signe au voisinage.

### Équivalents usuels en 0

$\sin x \sim x$, $\tan x \sim x$, $\ln(1 + x) \sim x$, $e^x - 1 \sim x$, $1 - \cos x \sim \frac{x^2}{2}$, $(1 + x)^\alpha - 1 \sim \alpha x$, $\arctan x \sim x$, $\operatorname{sh}x \sim x$.

Un polynôme est équivalent en $\pm\infty$ à son terme de plus haut degré, en 0 à son terme de plus bas degré.

> **Théorème — Formule de Stirling.** $n! \sim \sqrt{2\pi n}\left(\frac ne\right)^n$.

## Développements limités

> **Définition.** $f$ admet un DL à l'ordre $n$ en $a$ s'il existe des réels $c_0, \dots, c_n$ tels que $f(a + h) = c_0 + c_1h + \dots + c_nh^n + o(h^n)$. La partie polynomiale est unique.

> **Théorème de Taylor-Young.** Si $f$ est de classe $\mathcal C^n$ au voisinage de $a$ : $f(a + h) = \sum_{k=0}^n\frac{f^{(k)}(a)}{k!}h^k + o(h^n)$.

[[fig:m1-asymptotique-1]]

### Développements usuels en 0

- $e^x = 1 + x + \frac{x^2}{2} + \dots + \frac{x^n}{n!} + o(x^n)$
- $\frac{1}{1 - x} = 1 + x + x^2 + \dots + x^n + o(x^n)$ ; $\frac{1}{1 + x} = 1 - x + x^2 - \dots + (-1)^nx^n + o(x^n)$
- $\ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots + (-1)^{n-1}\frac{x^n}{n} + o(x^n)$
- $(1 + x)^\alpha = 1 + \alpha x + \frac{\alpha(\alpha - 1)}{2}x^2 + \dots + \binom\alpha nx^n + o(x^n)$
- $\cos x = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \dots + (-1)^p\frac{x^{2p}}{(2p)!} + o(x^{2p+1})$
- $\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - \dots + (-1)^p\frac{x^{2p+1}}{(2p+1)!} + o(x^{2p+2})$
- $\tan x = x + \frac{x^3}{3} + \frac{2x^5}{15} + o(x^6)$ ; $\arctan x = x - \frac{x^3}{3} + \frac{x^5}{5} + o(x^6)$
- $\operatorname{ch}x = 1 + \frac{x^2}{2} + \frac{x^4}{24} + o(x^5)$ ; $\operatorname{sh}x = x + \frac{x^3}{6} + o(x^4)$
- $\sqrt{1 + x} = 1 + \frac x2 - \frac{x^2}{8} + o(x^2)$

### Opérations

- **Somme** et **produit** : on tronque au plus petit ordre commun.
- **Composition** $g(f(x))$ avec $f(x) \to 0$ : remplacer dans le DL de $g$ et tronquer.
- **Inverse** : se ramener à $\frac{1}{1 - u}$ avec $u \to 0$.
- **Primitivation** : si $f(x) = \sum c_kx^k + o(x^n)$ et $F' = f$, alors $F(x) = F(0) + \sum\frac{c_k}{k+1}x^{k+1} + o(x^{n+1})$. (On ne dérive pas un DL sans justification.)
- DL en $a \ne 0$ : poser $x = a + h$ ; en $+\infty$ : poser $h = \frac1x$.

## Applications

- **Limites** : un DL ou un équivalent lève les formes indéterminées.
- **Position par rapport à la tangente** : si $f(a + h) = f(a) + f'(a)h + c_kh^k + o(h^k)$ avec $c_k \ne 0$, la position est donnée par le signe de $c_kh^k$ ; $k$ impair : point d'inflexion.
- **Extremums** : si $f'(a) = 0$ et $f''(a) > 0$, minimum local.
- **Asymptotes** : $f(x) = ax + b + \frac cx + o(\frac1x)$ en $+\infty$ donne l'asymptote $y = ax + b$ et la position (signe de $\frac cx$).
- Développements asymptotiques de suites, par exemple de la solution $x_n$ d'une équation dépendant de $n$.

## Exemple corrigé

**Énoncé.** Calculer $\lim_{x\to0}\frac{e^x - 1 - \sin x}{x^2}$.

**Solution.** $e^x = 1 + x + \frac{x^2}{2} + o(x^2)$ et $\sin x = x + o(x^2)$. Le numérateur vaut $\frac{x^2}{2} + o(x^2)$ : la limite est $\frac12$.

## Exemple corrigé (asymptote)

**Énoncé.** Étudier $f(x) = \sqrt{x^2 + x}$ en $+\infty$.

**Solution.** $f(x) = x\sqrt{1 + \frac1x} = x\left(1 + \frac{1}{2x} - \frac{1}{8x^2} + o(\frac{1}{x^2})\right) = x + \frac12 - \frac{1}{8x} + o(\frac1x)$. Asymptote $y = x + \frac12$, et la courbe est en dessous (terme $-\frac{1}{8x} < 0$).

## Pièges classiques

- On n'additionne pas des équivalents : $x + x^2 \sim x$ et $-x \sim -x$, mais la somme n'est pas équivalente à 0.
- Ne jamais écrire $f \sim 0$ (sauf si $f$ est nulle au voisinage).
- $e^{u} \sim e^{v}$ exige $u - v \to 0$, pas seulement $u \sim v$.
- Dans une composition, vérifier que la fonction intérieure tend vers 0 et garder assez de termes.
