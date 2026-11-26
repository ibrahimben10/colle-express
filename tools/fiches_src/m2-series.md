---
titre: Séries et familles sommables
---
## L'essentiel

Compléments sur les séries numériques (séries alternées, produit de Cauchy, comparaison) et notion de famille sommable, qui justifie les interversions de sommes.

## Séries alternées

> **Théorème des séries alternées.** Si $(a_n)$ est décroissante et tend vers 0, alors $\sum(-1)^na_n$ converge, et le reste vérifie $|R_n| \le a_{n+1}$, avec le signe de son premier terme.

Exemple : $\sum\frac{(-1)^n}{n}$ converge (vers $-\ln2$) sans converger absolument : convergence **semi-convergente**.

## Comparaison et restes

- Pour des termes positifs : si $u_n \sim v_n$ et que les séries convergent, les **restes** sont équivalents ; si elles divergent, les **sommes partielles** sont équivalentes.
- **Règle de d'Alembert** et comparaison logarithmique pour les termes positifs.

## Produit de Cauchy

> **Théorème.** Si $\sum a_n$ et $\sum b_n$ convergent **absolument**, la série de terme $c_n = \sum_{k=0}^na_kb_{n-k}$ converge absolument et $\sum c_n = \left(\sum a_n\right)\left(\sum b_n\right)$.

Application : $e^ae^b = e^{a+b}$ à partir des séries exponentielles.

## Familles sommables

> **Définition.** Une famille $(u_i)_{i\in I}$ (avec $I$ dénombrable) est sommable si $\sum_{i\in J}|u_i|$ est bornée pour $J$ fini ; sa somme ne dépend alors pas de l'ordre.

> **Théorème de Fubini (familles).** Si $(u_{p,q})$ est sommable, $\sum_{p,q}u_{p,q} = \sum_p\sum_qu_{p,q} = \sum_q\sum_pu_{p,q}$. Pour des termes **positifs**, l'égalité vaut toujours (dans $[0, +\infty]$).

## Exemple corrigé

**Énoncé.** Calculer $\sum_{n\ge1}\sum_{k\ge n}\frac{1}{k^3}$ (familles positives).

**Solution.** Les termes sont positifs : on peut intervertir. Pour $k$ fixé, $n$ varie de 1 à $k$ : $\sum_{k\ge1}\frac{k}{k^3} = \sum\frac{1}{k^2} = \frac{\pi^2}{6}$.

## Pièges classiques

- Réordonner une série semi-convergente peut changer sa somme.
- Le théorème des séries alternées exige la **décroissance** de $(a_n)$.
