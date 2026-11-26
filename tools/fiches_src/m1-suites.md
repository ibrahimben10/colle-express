---
titre: Nombres réels et suites
---
## L'essentiel

Toute partie non vide et majorée de $\mathbb R$ admet une borne supérieure : c'est la propriété fondamentale de $\mathbb R$, dont découlent les théorèmes de convergence des suites monotones et adjacentes.

## Borne supérieure

> **Définition.** $M = \sup A$ est le plus petit des majorants de $A$. Caractérisation : $M$ majore $A$ et, pour tout $\varepsilon > 0$, il existe $a \in A$ avec $a > M - \varepsilon$.

## Convergence

> **Définition.** $(u_n)$ converge vers $\ell$ si : $\forall\varepsilon > 0,\ \exists N,\ \forall n \ge N,\ |u_n - \ell| \le \varepsilon$.

Toute suite convergente est bornée ; la limite est unique ; les limites passent aux opérations usuelles (sauf formes indéterminées) et aux inégalités **larges**.

> **Théorème — Encadrement (gendarmes).** Si $v_n \le u_n \le w_n$ et si $v_n$ et $w_n$ tendent vers $\ell$, alors $u_n \to \ell$.

> **Théorème — Limite monotone.** Une suite croissante et majorée converge ; croissante et non majorée, elle tend vers $+\infty$.

> **Théorème — Suites adjacentes.** Si $(u_n)$ croît, $(v_n)$ décroît et $v_n - u_n \to 0$, elles convergent vers la même limite.

> **Théorème de Bolzano-Weierstrass.** Toute suite réelle (ou complexe) bornée admet une sous-suite convergente.

## Suites usuelles

- Arithmétique : $u_n = u_0 + nr$ ; géométrique : $u_n = u_0q^n$, convergente si $|q| < 1$ (vers 0).
- Arithmético-géométrique $u_{n+1} = au_n + b$ ($a \ne 1$) : $u_n - \ell = a^n(u_0 - \ell)$ avec $\ell = \frac{b}{1 - a}$.
- Récurrente linéaire d'ordre 2 $u_{n+2} = au_{n+1} + bu_n$ : racines de $r^2 = ar + b$, comme pour les équations différentielles.

## Suites récurrentes $u_{n+1} = f(u_n)$

[[fig:m1-suites-1]]

> **Méthode.** Trouver un intervalle stable par $f$ ; si $f$ est croissante, la suite est monotone ; si elle converge et si $f$ est continue, la limite est un **point fixe** de $f$.

## Exemple corrigé

**Énoncé.** Étudier $u_0 = 0$, $u_{n+1} = \sqrt{2 + u_n}$.

**Solution.** $f(x) = \sqrt{2 + x}$ est croissante et $[0, 2]$ est stable ($f(2) = 2$). $u_1 = \sqrt2 \ge u_0$, et par récurrence $u_{n+1} \ge u_n$ (car $f$ croissante). La suite est croissante et majorée par 2 : elle converge vers un point fixe de $f$ dans $[0, 2]$, c'est-à-dire $\ell = \sqrt{2 + \ell}$, soit $\ell = 2$.

## Pièges classiques

- Les inégalités **strictes** deviennent larges à la limite.
- Ne pas « passer à la limite » avant d'avoir montré que la suite converge.
- Si $f$ est décroissante, étudier les suites extraites $(u_{2n})$ et $(u_{2n+1})$.
