---
titre: Fonctions usuelles
---
## L'essentiel

Connaître parfaitement les fonctions de référence (puissances, exponentielle, logarithme, trigonométriques et leurs réciproques, hyperboliques) : domaines, dérivées, limites, courbes et inégalités classiques.

## Généralités sur les fonctions réelles

- Parité, imparité (courbe symétrique par rapport à l'axe des ordonnées, à l'origine), périodicité.
- Transformations de courbe : $x \mapsto f(x) + a$ (translation verticale), $f(x + a)$ (horizontale), $f(-x)$ (symétrie), $af(x)$ (dilatation).
- Monotonie : la somme de fonctions croissantes est croissante ; la composée de deux fonctions de même monotonie est croissante.

> **Théorème — Bijection réciproque.** Si $f$ est continue et strictement monotone sur un intervalle $I$, elle réalise une bijection de $I$ sur l'intervalle $f(I)$ ; $f^{-1}$ est continue, de même monotonie, et sa courbe est symétrique de celle de $f$ par rapport à $y = x$. Si $f$ est dérivable en $a$ avec $f'(a) \ne 0$, $f^{-1}$ est dérivable en $b = f(a)$ et $(f^{-1})'(b) = \frac{1}{f'(a)}$.

## Exponentielle, logarithme, puissances

[[fig:m1-fonctions-1]]

- $\ln$ : primitive de $\frac1x$ sur $]0, +\infty[$ nulle en 1 ; $\ln(ab) = \ln a + \ln b$. $\exp$ est sa réciproque : $\exp' = \exp$, $e^{a+b} = e^ae^b$.
- Puissances réelles : $a^b = e^{b\ln a}$ pour $a > 0$ ; $x \mapsto x^\alpha$ a pour dérivée $\alpha x^{\alpha-1}$.
- Logarithme en base $a$ : $\log_a x = \frac{\ln x}{\ln a}$.

> **Théorème — Croissances comparées.** Pour $\alpha, \beta > 0$ : $\frac{(\ln x)^\beta}{x^\alpha} \to 0$ et $\frac{e^{\alpha x}}{x^\beta} \to +\infty$ en $+\infty$ ; $x^\alpha|\ln x|^\beta \to 0$ en $0^+$.

> **Propriété — Inégalités de convexité.** $e^x \ge 1 + x$ pour tout réel $x$ ; $\ln(1 + x) \le x$ pour $x > -1$ ; $\sin x \le x$ pour $x \ge 0$.

## Fonctions trigonométriques

- $\cos' = -\sin$, $\sin' = \cos$, $\tan' = 1 + \tan^2 = \frac{1}{\cos^2}$ ($\tan$ définie hors de $\frac\pi2 + \pi\mathbb Z$).
- Limite remarquable : $\frac{\sin x}{x} \to 1$ en 0 ; $|\sin x| \le |x|$.

### Fonctions réciproques

| Fonction | Définie sur | Valeurs dans | Dérivée |
|---|---|---|---|
| $\arcsin$ | $[-1, 1]$ | $[-\frac\pi2, \frac\pi2]$ | $\frac{1}{\sqrt{1 - x^2}}$ sur $]-1, 1[$ |
| $\arccos$ | $[-1, 1]$ | $[0, \pi]$ | $-\frac{1}{\sqrt{1 - x^2}}$ sur $]-1, 1[$ |
| $\arctan$ | $\mathbb R$ | $]-\frac\pi2, \frac\pi2[$ | $\frac{1}{1 + x^2}$ |

Relations : $\arcsin x + \arccos x = \frac\pi2$ ; $\arctan x + \arctan\frac1x = \frac\pi2$ pour $x > 0$ ($-\frac\pi2$ pour $x < 0$). Attention : $\arcsin(\sin x) = x$ seulement si $x \in [-\frac\pi2, \frac\pi2]$.

## Fonctions hyperboliques

$\operatorname{ch}x = \frac{e^x + e^{-x}}{2}$ (paire), $\operatorname{sh}x = \frac{e^x - e^{-x}}{2}$ (impaire), $\operatorname{th} = \frac{\operatorname{sh}}{\operatorname{ch}}$. $\operatorname{ch}' = \operatorname{sh}$, $\operatorname{sh}' = \operatorname{ch}$, $\operatorname{th}' = 1 - \operatorname{th}^2$ ; $\operatorname{ch}^2 - \operatorname{sh}^2 = 1$.

## Dérivées usuelles à connaître

$(u^\alpha)' = \alpha u'u^{\alpha-1}$ ; $(e^u)' = u'e^u$ ; $(\ln|u|)' = \frac{u'}{u}$ ; $(\arctan u)' = \frac{u'}{1 + u^2}$ ; $(f \circ g)' = g'\cdot f' \circ g$.

## Exemple corrigé

**Énoncé.** Montrer que pour $x > 0$, $\arctan x + \arctan\frac1x = \frac\pi2$.

**Solution.** Soit $g(x) = \arctan x + \arctan\frac1x$ sur $]0, +\infty[$. $g'(x) = \frac{1}{1 + x^2} - \frac{1}{x^2}\cdot\frac{1}{1 + 1/x^2} = \frac{1}{1 + x^2} - \frac{1}{x^2 + 1} = 0$. $g$ est constante sur l'intervalle, et $g(1) = 2\cdot\frac\pi4 = \frac\pi2$.

## Pièges classiques

- Une dérivée nulle donne une fonction constante **sur un intervalle** seulement.
- $\ln$ n'est défini que sur $]0, +\infty[$ : penser à $\ln|u|$ pour les primitives.
- $a^b$ n'a de sens général que pour $a > 0$.
