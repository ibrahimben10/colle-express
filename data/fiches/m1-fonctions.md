---
titre: Fonctions usuelles
---
## L'essentiel

Il faut connaître parfaitement les fonctions usuelles : domaine, dérivée, limites, allure de la courbe, et les inégalités classiques qui en découlent.

## Exponentielle, logarithme, puissances

[[fig:m1-fonctions-1]]

| Fonction | Dérivée | Propriétés |
|---|---|---|
| $\exp$ | $\exp$ | $e^{a+b} = e^ae^b$, $\exp > 0$ |
| $\ln$ (sur $]0, +\infty[$) | $1/x$ | $\ln(ab) = \ln a + \ln b$ |
| $x \mapsto x^\alpha = e^{\alpha\ln x}$ | $\alpha x^{\alpha-1}$ | croissante si $\alpha > 0$ |

> **Propriété — Croissances comparées.** Pour $\alpha, \beta > 0$ : $\dfrac{(\ln x)^\beta}{x^\alpha} \xrightarrow[x\to+\infty]{} 0$, $\dfrac{x^\alpha}{e^{\beta x}} \xrightarrow[x\to+\infty]{} 0$ et $x^\alpha|\ln x|^\beta \xrightarrow[x\to0^+]{} 0$.

## Fonctions trigonométriques et réciproques

- $\sin' = \cos$, $\cos' = -\sin$, $\tan' = 1 + \tan^2 = \dfrac{1}{\cos^2}$.
- $\arcsin : [-1, 1] \to [-\frac\pi2, \frac\pi2]$, $\arcsin'(x) = \dfrac{1}{\sqrt{1 - x^2}}$ sur $]-1, 1[$.
- $\arccos : [-1, 1] \to [0, \pi]$, $\arccos' = -\arcsin'$ ; $\arcsin x + \arccos x = \frac\pi2$.
- $\arctan : \mathbb R \to ]-\frac\pi2, \frac\pi2[$, $\arctan'(x) = \dfrac{1}{1 + x^2}$ ; $\arctan x + \arctan\frac1x = \pm\frac\pi2$ selon le signe de $x$.

## Fonctions hyperboliques

$\operatorname{ch} x = \dfrac{e^x + e^{-x}}{2}$, $\operatorname{sh} x = \dfrac{e^x - e^{-x}}{2}$, $\operatorname{ch}^2 - \operatorname{sh}^2 = 1$, $\operatorname{ch}' = \operatorname{sh}$, $\operatorname{sh}' = \operatorname{ch}$.

## Inégalités à connaître

> **Propriété.** Pour tout réel $x$ : $e^x \ge 1 + x$ ; pour $x > -1$ : $\ln(1 + x) \le x$ ; pour $x \ge 0$ : $\sin x \le x$ ; pour $x \in [0, \frac\pi2]$ : $\sin x \ge \frac{2}{\pi}x$ (concavité).

## Méthode : étudier une fonction

1. Domaine de définition, parité, périodicité.
2. Dérivée et signe, tableau de variations.
3. Limites aux bornes, asymptotes.
4. Points particuliers, tracé.

## Exemple corrigé

**Énoncé.** Montrer que pour tout $x > 0$, $\ln x \le x - 1$.

**Solution.** Soit $g(x) = x - 1 - \ln x$ sur $]0, +\infty[$. $g'(x) = 1 - \frac1x$ est négative sur $]0, 1]$ et positive sur $[1, +\infty[$ : $g$ admet un minimum en 1, égal à $g(1) = 0$. Donc $g \ge 0$, avec égalité seulement en $x = 1$.

## Pièges classiques

- $\arcsin(\sin x) = x$ seulement pour $x \in [-\frac\pi2, \frac\pi2]$.
- $x^\alpha$ n'est défini que pour $x > 0$ si $\alpha$ n'est pas entier.
- Ne pas confondre $\ln(a + b)$ et $\ln a + \ln b$.
