---
titre: Séries entières
---
## L'essentiel

Une série entière $\sum a_nz^n$ converge sur un disque ouvert (son disque de convergence) et diverge à l'extérieur. Sur l'intervalle réel ouvert, sa somme est $\mathcal C^\infty$ et se dérive terme à terme. Les développements usuels et les équations différentielles permettent de développer les fonctions et de calculer des sommes.

## Rayon de convergence

[[fig:m2-series-entieres-1]]

> **Théorème — Lemme d'Abel.** Si $(a_nz_0^n)$ est bornée, alors $\sum a_nz^n$ converge absolument pour $|z| < |z_0|$.

> **Définition.** Le rayon de convergence est $R = \sup\{r \ge 0,\ (a_nr^n)\ \text{bornée}\} \in [0, +\infty]$. Pour $|z| < R$, la série converge absolument ; pour $|z| > R$, elle diverge grossièrement. Sur le cercle $|z| = R$, tout peut arriver.

### Calcul du rayon

- **D'Alembert** : appliquer la règle à $\sum|a_nz^n|$ ; si $\left|\frac{a_{n+1}}{a_n}\right| \to \ell$, alors $R = \frac1\ell$.
- **Comparaison** : si $|a_n| \le |b_n|$, $R_a \ge R_b$ ; si $a_n = O(b_n)$, $R_a \ge R_b$ ; si $a_n \sim b_n$, $R_a = R_b$.
- Si la série converge en $z_0$, $R \ge |z_0|$ ; si elle diverge en $z_0$, $R \le |z_0|$ ; si elle converge sans converger absolument en $z_0$, $R = |z_0|$.
- $\sum a_nz^n$ et $\sum na_nz^n$ ont le même rayon (donc aussi les séries dérivée et primitive).
- Somme : $R_{a+b} \ge \min(R_a, R_b)$, avec égalité si $R_a \ne R_b$ ; produit de Cauchy : rayon $\ge \min(R_a, R_b)$.

## Régularité de la somme

> **Théorème.** La série entière converge normalement sur tout disque fermé $|z| \le r < R$ ; sa somme est continue sur le disque ouvert.

> **Théorème — Variable réelle.** $S(x) = \sum a_nx^n$ est de classe $\mathcal C^\infty$ sur $]-R, R[$, ses dérivées s'obtiennent terme à terme, et $a_n = \frac{S^{(n)}(0)}{n!}$. On intègre terme à terme : $\int_0^xS = \sum\frac{a_n}{n+1}x^{n+1}$.

Unicité : si $\sum a_nx^n = \sum b_nx^n$ au voisinage de 0, alors $a_n = b_n$ pour tout $n$.

## Fonctions développables en série entière

$f$ est DSE en 0 s'il existe $\sum a_nx^n$ de rayon $R > 0$ égale à $f$ sur $]-r, r[$. Alors $f$ est $\mathcal C^\infty$ et $a_n = \frac{f^{(n)}(0)}{n!}$ (série de Taylor). Attention : une fonction $\mathcal C^\infty$ n'est pas toujours DSE ($e^{-1/x^2}$ prolongée par 0).

### Développements usuels

| Fonction | Développement | Rayon |
|---|---|---|
| $e^x$ | $\sum\frac{x^n}{n!}$ | $+\infty$ |
| $\operatorname{ch}x$, $\operatorname{sh}x$ | $\sum\frac{x^{2n}}{(2n)!}$, $\sum\frac{x^{2n+1}}{(2n+1)!}$ | $+\infty$ |
| $\cos x$, $\sin x$ | $\sum\frac{(-1)^nx^{2n}}{(2n)!}$, $\sum\frac{(-1)^nx^{2n+1}}{(2n+1)!}$ | $+\infty$ |
| $\frac{1}{1 - x}$ | $\sum x^n$ | 1 |
| $\ln(1 + x)$ | $\sum_{n\ge1}(-1)^{n-1}\frac{x^n}{n}$ | 1 |
| $-\ln(1 - x)$ | $\sum_{n\ge1}\frac{x^n}{n}$ | 1 |
| $(1 + x)^\alpha$ | $\sum\frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}x^n$ | 1 (si $\alpha \notin \mathbb N$) |
| $\arctan x$ | $\sum\frac{(-1)^nx^{2n+1}}{2n+1}$ | 1 |

Exponentielle complexe : $e^z = \sum\frac{z^n}{n!}$ pour tout $z \in \mathbb C$.

> **Méthode — Développer une fonction.**
> - Opérations sur les DSE connus (somme, produit, primitive, dérivée, $x \mapsto ax$ ou $x^2$) ; décomposition en éléments simples pour une fraction rationnelle.
> - Trouver une **équation différentielle** linéaire vérifiée par $f$, chercher une solution $\sum a_nx^n$ (relation de récurrence sur les $a_n$), calculer le rayon, puis conclure par unicité (Cauchy-Lipschitz).

> **Méthode — Calculer une somme $\sum a_nx^n$.** Reconnaître une dérivée ou une primitive d'une série connue ($\sum nx^n$, $\sum\frac{x^n}{n}$) ; décomposer une fraction rationnelle en $n$ ; utiliser $\sum\frac{x^n}{n!}$ pour $\frac{P(n)}{n!}$.

## Exemple corrigé

**Énoncé.** Rayon et somme de $\sum_{n\ge1}nx^n$.

**Solution.** D'Alembert : $\frac{n+1}{n} \to 1$, $R = 1$. Sur $]-1, 1[$, en dérivant $\sum x^n = \frac{1}{1 - x}$ : $\sum nx^{n-1} = \frac{1}{(1 - x)^2}$, donc $\sum_{n\ge1}nx^n = \frac{x}{(1 - x)^2}$.

## Exemple corrigé (équation différentielle)

**Énoncé.** Développer $f(x) = \frac{\arcsin x}{\sqrt{1 - x^2}}$ en série entière.

**Solution.** $f$ vérifie $(1 - x^2)f' - xf = 1$, $f(0) = 0$, et $f$ est impaire. On cherche $\sum a_{2n+1}x^{2n+1}$ : la relation donne $a_1 = 1$ et $(2n + 1)a_{2n+1} = 2n\,a_{2n-1}$, d'où $a_{2n+1} = \frac{2^{2n}(n!)^2}{(2n + 1)!}$. Rayon : $\frac{a_{2n+1}}{a_{2n-1}} \to 1$, $R = 1$. Par unicité de la solution du problème de Cauchy sur $]-1, 1[$, $f(x) = \sum_n\frac{2^{2n}(n!)^2}{(2n+1)!}x^{2n+1}$.

## Pièges classiques

- $R$ ne dit rien sur la convergence **sur** le cercle.
- D'Alembert ne s'applique pas tel quel avec des coefficients nuls (série lacunaire $\sum a_nx^{2n}$) : l'appliquer à $|a_nx^{2n}|$.
- Dériver terme à terme n'est justifié que sur l'intervalle **ouvert** $]-R, R[$.
