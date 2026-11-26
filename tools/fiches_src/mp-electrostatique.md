---
titre: Champ électrostatique
---
## L'essentiel

Une distribution de charges immobiles crée un champ électrostatique $\vec E$, qui dérive d'un potentiel : $\vec E = -\overrightarrow{\mathrm{grad}}\,V$. Pour le calculer, on exploite d'abord les **symétries** et **invariances**, puis le **théorème de Gauss**.

## Loi de Coulomb

Le champ créé en M par une charge ponctuelle $q$ placée en P :
$$\vec E(M) = \frac{q}{4\pi\varepsilon_0}\frac{\vec u_{PM}}{PM^2},\qquad V(M) = \frac{q}{4\pi\varepsilon_0\,PM}.$$
Le champ d'une distribution est la somme des champs élémentaires (principe de superposition).

## Symétries et invariances

[[fig:mp-electrostatique-1]]

> **Principe de Curie.** En un point d'un plan de symétrie de la distribution, $\vec E$ appartient à ce plan. En un point d'un plan d'antisymétrie, $\vec E$ est orthogonal à ce plan.

Les **invariances** (par translation, par rotation) réduisent le nombre de variables dont dépend la norme du champ.

## Théorème de Gauss

[[fig:mp-electrostatique-2]]

> **Théorème de Gauss.** Pour toute surface fermée $S$ : $\displaystyle\oint_S\vec E\cdot\mathrm d\vec S = \frac{Q_{\text{int}}}{\varepsilon_0}$.

Forme locale : $\mathrm{div}\,\vec E = \dfrac{\rho}{\varepsilon_0}$ ; avec le potentiel, équation de Poisson $\Delta V = -\dfrac{\rho}{\varepsilon_0}$.

## Méthode

1. Symétries : direction de $\vec E$.
2. Invariances : variables dont dépend $E$.
3. Choisir une surface de Gauss fermée, sur laquelle $\vec E$ est soit normal (de norme constante), soit tangent.
4. Calculer le flux et la charge intérieure.

## Propriétés

- Les lignes de champ partent des charges positives et vont vers les charges négatives ; elles sont orthogonales aux équipotentielles.
- $\vec E$ est dirigé vers les potentiels décroissants.
- Énergie d'une charge $q$ dans le potentiel $V$ : $E_p = qV$.

## Exemple corrigé

**Énoncé.** Une sphère creuse de rayon $R$ porte une charge $Q$ uniformément répartie en surface. Calculer le champ partout.

**Solution.**
1. Symétrie sphérique : tous les plans contenant O et M sont plans de symétrie, donc $\vec E = E(r)\,\vec u_r$.
2. Surface de Gauss : sphère de rayon $r$ ; flux $4\pi r^2E(r)$.
3. $r < R$ : $Q_{\text{int}} = 0$, donc $\vec E = \vec 0$ à l'intérieur.
4. $r > R$ : $E = \dfrac{Q}{4\pi\varepsilon_0r^2}$. Le champ est discontinu en $r = R$, de $\sigma/\varepsilon_0$.

## Pièges classiques

- Le principe de Curie concerne les **causes** (la distribution), pas le champ lui-même.
- La surface de Gauss doit être **fermée** et passer par le point où l'on cherche le champ.
