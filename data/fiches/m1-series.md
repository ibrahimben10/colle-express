---
titre: Séries numériques
---
## L'essentiel

La série $\sum u_n$ converge si la suite des sommes partielles $S_n = \sum_{k=0}^nu_k$ converge. Pour les séries à termes **positifs**, on dispose de théorèmes de comparaison ; sinon, on étudie la convergence absolue.

> **Propriété — Divergence grossière.** Si $\sum u_n$ converge, alors $u_n \to 0$. La réciproque est fausse (série harmonique).

## Séries de référence

| Série | Convergence |
|---|---|
| géométrique $\sum q^n$ | ssi $|q| < 1$, somme $\frac{1}{1 - q}$ |
| de Riemann $\sum\frac{1}{n^\alpha}$ | ssi $\alpha > 1$ |
| exponentielle $\sum\frac{z^n}{n!}$ | toujours, somme $e^z$ |

## Séries à termes positifs

> **Théorème — Comparaison.** Si $0 \le u_n \le v_n$ (à partir d'un certain rang) et $\sum v_n$ converge, alors $\sum u_n$ converge. Si $u_n \sim v_n$ (termes positifs), les séries sont de même nature.

[[fig:m1-series-1]]

> **Théorème — Comparaison série-intégrale.** Si $f$ est continue, positive et décroissante sur $[1, +\infty[$, $\sum f(n)$ et $\int_1^{+\infty}f$ sont de même nature ; l'encadrement donne aussi un équivalent des sommes partielles ou des restes.

**Règle de d'Alembert** : si $\frac{u_{n+1}}{u_n} \to \ell$ ($u_n > 0$), la série converge pour $\ell < 1$ et diverge grossièrement pour $\ell > 1$.

## Convergence absolue

> **Théorème.** Si $\sum|u_n|$ converge, alors $\sum u_n$ converge (et $|\sum u_n| \le \sum|u_n|$).

## Exemple corrigé

**Énoncé.** Nature de $\sum\left(1 - \cos\frac1n\right)$ et de $\sum\frac{\ln n}{n^2}$.

**Solution.** $1 - \cos\frac1n \sim \frac{1}{2n^2}$, termes positifs, série de Riemann convergente : la première converge. Pour la seconde, $\frac{\ln n}{n^2} = o\!\left(\frac{1}{n^{3/2}}\right)$ (croissances comparées) et $\sum\frac{1}{n^{3/2}}$ converge : elle converge.

## Pièges classiques

- Les comparaisons ($\le$, $\sim$, $o$) ne valent que pour des termes de **signe constant**.
- $u_n \to 0$ ne suffit pas : $\sum\frac1n$ diverge.
- La règle de d'Alembert ne conclut pas si $\ell = 1$.
