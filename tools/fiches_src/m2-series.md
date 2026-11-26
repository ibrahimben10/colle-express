---
titre: Séries et familles sommables
---
## L'essentiel

Compléments sur les séries numériques : séries alternées, règle de d'Alembert, comparaison des restes et des sommes partielles, produit de Cauchy. Les familles sommables donnent un cadre où l'on peut réordonner et intervertir les sommes (Fubini).

## Rappels et compléments

- Séries de référence : géométriques, Riemann ($\alpha > 1$), exponentielle.
- **Comparaison logarithmique** : si $u_n, v_n > 0$ et $\frac{u_{n+1}}{u_n} \le \frac{v_{n+1}}{v_n}$ à partir d'un rang, alors $u_n = O(v_n)$.
- **Règle de d'Alembert** (termes non nuls) : $\left|\frac{u_{n+1}}{u_n}\right| \to \ell < 1$ : convergence absolue ; $\ell > 1$ : divergence grossière.
- **Séries de Bertrand** (hors programme mais classiques, à redémontrer) : $\sum\frac{1}{n^\alpha(\ln n)^\beta}$.

> **Théorème — Sommation des relations de comparaison.** Soient $u_n$ et $v_n \ge 0$.
> - Si $\sum v_n$ converge et $u_n = o(v_n)$ (resp. $O$, $\sim$), alors les **restes** vérifient $R_n(u) = o(R_n(v))$ (resp. $O$, $\sim$).
> - Si $\sum v_n$ diverge et $u_n = o(v_n)$ (resp. $O$, $\sim$), alors les **sommes partielles** vérifient $S_n(u) = o(S_n(v))$ (resp. $O$, $\sim$).

Cas particulier : théorème de Cesàro (si $u_n \to \ell$, la moyenne $\frac1n\sum_{k=1}^nu_k \to \ell$).

## Séries alternées

> **Théorème des séries alternées.** Si $(a_n)$ est **décroissante** et tend vers 0, alors $\sum(-1)^na_n$ converge ; le reste $R_n$ est du signe de son premier terme $(-1)^{n+1}a_{n+1}$ et $|R_n| \le a_{n+1}$.

Exemple : $\sum\frac{(-1)^{n-1}}{n} = \ln2$, convergente sans être absolument convergente (semi-convergence). Méthode quand le théorème ne s'applique pas directement : développement asymptotique du terme général $u_n = \frac{(-1)^n}{n^\alpha} + O(\dots)$ et séparation en série alternée plus série absolument convergente.

## Produit de Cauchy

> **Théorème.** Si $\sum a_n$ et $\sum b_n$ convergent **absolument**, la série de terme $c_n = \sum_{k=0}^na_kb_{n-k}$ converge absolument et $\sum c_n = \left(\sum a_n\right)\left(\sum b_n\right)$.

Application : $e^ae^b = e^{a+b}$ ; $\frac{1}{(1 - x)^2} = \sum(n + 1)x^n$ pour $|x| < 1$.

## Familles sommables

$I$ est un ensemble dénombrable.

> **Définition.** Pour des $u_i \ge 0$, $\sum_{i\in I}u_i = \sup_{J\text{ fini}}\sum_{i\in J}u_i \in [0, +\infty]$. Une famille complexe $(u_i)$ est **sommable** si $\sum|u_i| < +\infty$ ; sa somme ne dépend alors pas de l'ordre de sommation.

- Pour $I = \mathbb N$ : sommable si et seulement si la série converge absolument.
- Linéarité, inégalité triangulaire, croissance.

> **Théorème — Sommation par paquets.** Si $I = \bigsqcup_nI_n$ (partition) et $(u_i)$ est sommable (ou positive), alors $\sum_{i\in I}u_i = \sum_n\sum_{i\in I_n}u_i$.

> **Théorème de Fubini.** Si $(u_{p,q})$ est sommable, $\sum_{(p,q)}u_{p,q} = \sum_p\sum_qu_{p,q} = \sum_q\sum_pu_{p,q}$. Pour des termes **positifs**, l'égalité vaut toujours (dans $[0, +\infty]$) : c'est ainsi qu'on prouve la sommabilité.

Produit : si $(a_i)$ et $(b_j)$ sont sommables, $(a_ib_j)$ l'est et sa somme est le produit des sommes.

## Exemple corrigé

**Énoncé.** Calculer $\sum_{n\ge1}\sum_{k\ge n}\frac{1}{k^3}$.

**Solution.** Termes positifs : on peut intervertir. Pour $k$ fixé, $n$ va de 1 à $k$ : $\sum_{k\ge1}\frac{k}{k^3} = \sum_{k\ge1}\frac{1}{k^2} = \frac{\pi^2}{6}$.

## Exemple corrigé (développement asymptotique)

**Énoncé.** Nature de $\sum\ln\left(1 + \frac{(-1)^n}{\sqrt n}\right)$.

**Solution.** $u_n = \frac{(-1)^n}{\sqrt n} - \frac{1}{2n} + O\left(\frac{1}{n^{3/2}}\right)$. $\sum\frac{(-1)^n}{\sqrt n}$ converge (séries alternées), $\sum O(n^{-3/2})$ converge absolument, mais $\sum\frac{1}{2n}$ diverge : la série **diverge**, alors que $u_n \sim \frac{(-1)^n}{\sqrt n}$, terme d'une série convergente.

## Pièges classiques

- Les équivalents ne transmettent la nature que pour des termes de **signe constant**.
- Réordonner une série semi-convergente peut changer sa somme.
- Le théorème des séries alternées exige la **décroissance** de $(a_n)$.
