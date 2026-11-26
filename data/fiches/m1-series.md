---
titre: Séries numériques
---
## L'essentiel

Une série $\sum u_n$ converge si la suite des sommes partielles $S_n = u_0 + \dots + u_n$ a une limite. Pour les séries à termes positifs, on compare à des séries de référence (géométriques, de Riemann) ; la convergence absolue implique la convergence.

## Définitions

- Somme partielle $S_n = \sum_{k=0}^nu_k$ ; si $(S_n)$ converge, sa limite est la somme $\sum_{n=0}^{+\infty}u_n$ et le **reste** $R_n = \sum_{k>n}u_k$ tend vers 0.
- Linéarité : la somme de deux séries convergentes converge ; convergente + divergente diverge.

> **Propriété — Divergence grossière.** Si $\sum u_n$ converge, alors $u_n \to 0$. Si $u_n \not\to 0$, la série diverge grossièrement. La réciproque est fausse : $\sum\frac1n$ diverge.

**Lien suite-série** : $(a_n)$ converge si et seulement si la série télescopique $\sum(a_{n+1} - a_n)$ converge.

## Séries de référence

- **Géométrique** : $\sum q^n$ converge si et seulement si $|q| < 1$, et $\sum_{n\ge0}q^n = \frac{1}{1 - q}$.
- **Riemann** : $\sum\frac{1}{n^\alpha}$ converge si et seulement si $\alpha > 1$. Par exemple $\sum\frac{1}{n^2} = \frac{\pi^2}{6}$ ; la série harmonique diverge, avec $\sum_{k=1}^n\frac1k \sim \ln n$.
- **Exponentielle** : $\sum\frac{x^n}{n!} = e^x$ pour tout réel (ou complexe) $x$.

## Séries à termes positifs

Pour $u_n \ge 0$, $(S_n)$ est croissante : la série converge si et seulement si $(S_n)$ est majorée.

> **Théorème — Comparaison.** Soient $u_n, v_n \ge 0$.
> - Si $u_n \le v_n$ et $\sum v_n$ converge, alors $\sum u_n$ converge ; si $\sum u_n$ diverge, $\sum v_n$ aussi.
> - Si $u_n = O(v_n)$ (ou $o(v_n)$) et $\sum v_n$ converge, alors $\sum u_n$ converge.
> - Si $u_n \sim v_n$, les deux séries sont de même nature.

> **Méthode — Règle « $n^\alpha u_n$ ».** Si $n^\alpha u_n \to 0$ avec $\alpha > 1$, alors $u_n = o(\frac{1}{n^\alpha})$ et la série converge. Si $nu_n \to +\infty$, elle diverge.

**Règle de d'Alembert** : si $\frac{u_{n+1}}{u_n} \to \ell$, la série converge si $\ell < 1$, diverge si $\ell > 1$ ; on ne peut pas conclure si $\ell = 1$.

### Comparaison série-intégrale

[[fig:m1-series-1]]

> **Théorème.** Si $f$ est continue, positive et décroissante sur $[1, +\infty[$ : $\int_k^{k+1}f \le f(k) \le \int_{k-1}^kf$. La série $\sum f(n)$ converge si et seulement si $\int_1^xf$ est bornée. On en tire des encadrements des sommes partielles et des restes.

## Convergence absolue

> **Théorème.** Si $\sum|u_n|$ converge, alors $\sum u_n$ converge (série réelle ou complexe), et $\left|\sum u_n\right| \le \sum|u_n|$.

Une série convergente non absolument convergente est dite semi-convergente (exemple : $\sum\frac{(-1)^n}{n}$, voir le théorème des séries alternées en deuxième année).

## Exemple corrigé

**Énoncé.** Nature de $\sum u_n$ avec $u_n = \ln\left(1 + \frac{1}{n^2}\right)$, puis $v_n = \frac{n!}{n^n}$.

**Solution.** $u_n \ge 0$ et $u_n \sim \frac{1}{n^2}$, terme d'une série de Riemann convergente : $\sum u_n$ converge. Pour $v_n > 0$ : $\frac{v_{n+1}}{v_n} = \frac{(n+1)n^n}{(n+1)^{n+1}} = \left(1 + \frac1n\right)^{-n} \to \frac1e < 1$ : par d'Alembert, $\sum v_n$ converge.

## Exemple corrigé (série-intégrale)

**Énoncé.** Équivalent de $H_n = \sum_{k=1}^n\frac1k$.

**Solution.** $f(x) = \frac1x$ est décroissante : $\int_k^{k+1}\frac{\mathrm dx}{x} \le \frac1k \le \int_{k-1}^k\frac{\mathrm dx}{x}$ ($k \ge 2$). En sommant : $\ln(n + 1) \le H_n \le 1 + \ln n$. Donc $H_n \sim \ln n$.

## Pièges classiques

- $u_n \to 0$ ne suffit pas pour converger.
- Les critères de comparaison et d'équivalents exigent des termes de **signe constant**.
- Ne pas écrire $\sum u_n$ (la somme) avant d'avoir prouvé la convergence.
