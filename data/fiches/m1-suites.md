---
titre: Nombres réels et suites
---
## L'essentiel

Toute partie non vide et majorée de $\mathbb R$ admet une borne supérieure : c'est la propriété fondamentale de $\mathbb R$. Elle donne les grands théorèmes de convergence (limite monotone, suites adjacentes, Bolzano-Weierstrass).

## Nombres réels

### Borne supérieure

> **Définition.** $M = \sup A$ est le plus petit des majorants de $A$. Caractérisation : $M$ majore $A$ et, pour tout $\varepsilon > 0$, il existe $a \in A$ avec $a > M - \varepsilon$. De même pour $\inf$.

> **Théorème — Propriété de la borne supérieure.** Toute partie de $\mathbb R$ non vide et majorée admet une borne supérieure.

Si $A$ a un plus grand élément, c'est sa borne supérieure ; la réciproque est fausse ($\sup[0, 1[ = 1 \notin [0, 1[$).

### Propriétés de $\mathbb R$

- $\mathbb R$ est **archimédien** : pour $x > 0$ et $y$ réel, il existe $n$ avec $nx > y$.
- $\mathbb Q$ et $\mathbb R \setminus \mathbb Q$ sont **denses** : tout intervalle ouvert non vide contient un rationnel et un irrationnel.
- Approximations décimales : $\frac{\lfloor10^nx\rfloor}{10^n} \le x < \frac{\lfloor10^nx\rfloor + 1}{10^n}$.
- Intervalles : parties $I$ telles que $a, b \in I$, $a \le c \le b \Rightarrow c \in I$.

## Limite d'une suite

> **Définition.** $(u_n)$ converge vers $\ell$ si : $\forall\varepsilon > 0,\ \exists N,\ \forall n \ge N,\ |u_n - \ell| \le \varepsilon$. Elle tend vers $+\infty$ si : $\forall A,\ \exists N,\ \forall n \ge N,\ u_n \ge A$.

- La limite est **unique** ; une suite convergente est **bornée**.
- Opérations : somme, produit, quotient (limite du dénominateur non nulle). Formes indéterminées : $\infty - \infty$, $0\times\infty$, $\frac00$, $\frac\infty\infty$, $1^\infty$.
- Passage à la limite dans les inégalités **larges** : si $u_n \le v_n$ et que les deux convergent, $\lim u_n \le \lim v_n$.
- Une suite bornée multipliée par une suite qui tend vers 0 tend vers 0.

> **Théorème — Encadrement (gendarmes).** Si $v_n \le u_n \le w_n$ et si $v_n$, $w_n$ tendent vers $\ell$, alors $u_n \to \ell$. **Minoration** : si $u_n \ge v_n$ et $v_n \to +\infty$, alors $u_n \to +\infty$.

## Théorèmes d'existence de limite

> **Théorème — Limite monotone.** Une suite croissante et majorée converge vers $\sup u_n$ ; croissante et non majorée, elle tend vers $+\infty$.

> **Théorème — Suites adjacentes.** Si $(u_n)$ croît, $(v_n)$ décroît et $v_n - u_n \to 0$, elles convergent vers une même limite $\ell$, et $u_n \le \ell \le v_n$.

### Suites extraites

$(u_{\varphi(n)})$ avec $\varphi$ strictement croissante. Si $u_n \to \ell$, toute suite extraite tend vers $\ell$. Si $(u_{2n})$ et $(u_{2n+1})$ tendent vers $\ell$, alors $u_n \to \ell$. Pour montrer la divergence : trouver deux suites extraites de limites différentes.

> **Théorème de Bolzano-Weierstrass.** Toute suite réelle (ou complexe) bornée admet une suite extraite convergente.

Suites complexes : $u_n \to \ell$ si et seulement si $\operatorname{Re}u_n \to \operatorname{Re}\ell$ et $\operatorname{Im}u_n \to \operatorname{Im}\ell$.

## Suites usuelles

- Arithmétique : $u_n = u_0 + nr$ ; géométrique : $u_n = u_0q^n$, qui tend vers 0 si $|q| < 1$, diverge si $|q| > 1$ (ou $q = -1$).
- Arithmético-géométrique $u_{n+1} = au_n + b$ ($a \ne 1$) : avec $\ell = \frac{b}{1 - a}$ (point fixe), $u_n - \ell = a^n(u_0 - \ell)$.
- Récurrente linéaire d'ordre 2 $u_{n+2} = au_{n+1} + bu_n$ : racines de $r^2 = ar + b$. Deux racines distinctes : $u_n = \lambda r_1^n + \mu r_2^n$ ; racine double : $u_n = (\lambda + \mu n)r^n$ ; racines complexes conjuguées $\rho e^{\pm i\theta}$ (suite réelle) : $u_n = \rho^n(\lambda\cos n\theta + \mu\sin n\theta)$.

## Suites récurrentes $u_{n+1} = f(u_n)$

[[fig:m1-suites-1]]

> **Méthode.**
> 1. Trouver un intervalle $I$ **stable** par $f$ ($f(I) \subset I$) contenant $u_0$ : la suite est bien définie.
> 2. Si $f$ est croissante sur $I$, la suite est monotone (comparer $u_0$ et $u_1$) ; si $f$ est décroissante, étudier $(u_{2n})$ et $(u_{2n+1})$, qui sont monotones.
> 3. Si la suite converge vers $\ell \in I$ et si $f$ est continue, alors $f(\ell) = \ell$ : $\ell$ est un **point fixe**.
> 4. Étudier le signe de $f(x) - x$ aide à conclure.

## Comparaison des suites (aperçu)

$u_n = o(v_n)$, $u_n = O(v_n)$, $u_n \sim v_n$ : voir la fiche d'analyse asymptotique. Croissances comparées : $(\ln n)^\alpha \ll n^\beta \ll q^n \ll n!$ ($q > 1$).

## Exemple corrigé

**Énoncé.** Étudier $u_0 = 0$, $u_{n+1} = \sqrt{2 + u_n}$.

**Solution.** $f(x) = \sqrt{2 + x}$ est croissante et $[0, 2]$ est stable ($f(0) = \sqrt2$, $f(2) = 2$). $u_1 = \sqrt2 \ge u_0$ et, $f$ étant croissante, une récurrence donne $u_{n+1} \ge u_n$. La suite est croissante, majorée par 2 : elle converge vers un point fixe de $f$ dans $[0, 2]$ : $\ell = \sqrt{2 + \ell}$, $\ell^2 - \ell - 2 = 0$, $\ell = 2$.

## Exemple corrigé (suites adjacentes)

**Énoncé.** $u_n = \sum_{k=0}^n\frac{1}{k!}$ et $v_n = u_n + \frac{1}{n\cdot n!}$. Montrer qu'elles sont adjacentes.

**Solution.** $u_{n+1} - u_n = \frac{1}{(n+1)!} > 0$. $v_{n+1} - v_n = \frac{1}{(n+1)!} + \frac{1}{(n+1)(n+1)!} - \frac{1}{n\cdot n!} = \frac{n(n+2) - (n+1)^2}{n(n+1)(n+1)!} < 0$. Et $v_n - u_n \to 0$. Elles convergent vers la même limite (qui est $e$).

## Pièges classiques

- Les inégalités **strictes** deviennent larges à la limite.
- Ne pas « passer à la limite » dans une relation avant d'avoir prouvé la convergence.
- Une suite bornée ne converge pas forcément : $(-1)^n$.
- Croissante et majorée par $M$ ne veut pas dire que la limite vaut $M$.
