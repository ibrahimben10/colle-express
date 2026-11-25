---
titre: Champ magnétostatique
---
## L'essentiel

Des courants permanents créent un champ magnétique $\vec B$. On le calcule avec les **symétries** puis le **théorème d'Ampère**. Le flux de $\vec B$ est conservatif : $\mathrm{div}\,\vec B = 0$.

## Symétries

> **Propriété.** En un point d'un plan de symétrie des courants, $\vec B$ est **orthogonal** à ce plan ; en un point d'un plan d'antisymétrie, $\vec B$ est **contenu** dans ce plan.

C'est l'inverse du cas électrostatique : $\vec B$ est un pseudo-vecteur.

## Théorème d'Ampère

> **Théorème d'Ampère.** Pour tout contour fermé orienté $\mathcal C$ : $\displaystyle\oint_{\mathcal C}\vec B\cdot\mathrm d\vec\ell = \mu_0\,I_{\text{enlacé}}$, les courants étant comptés positivement s'ils traversent la surface dans le sens donné par l'orientation du contour (règle de la main droite).

Forme locale : $\overrightarrow{\mathrm{rot}}\,\vec B = \mu_0\vec j$.

## Exemples à connaître

[[fig:mp-magnetostatique-1]]

Fil infini : $\vec B = \dfrac{\mu_0I}{2\pi r}\,\vec u_\theta$.

[[fig:mp-magnetostatique-2]]

Solénoïde infini : $\vec B = \mu_0nI\,\vec u_z$ à l'intérieur, nul à l'extérieur.

[[fig:mp-magnetostatique-3]]

Câble coaxial : $B$ croît linéairement dans l'âme, décroît en $1/r$ entre les conducteurs, s'annule à l'extérieur (courant total enlacé nul).

[[fig:mp-magnetostatique-4]]

Nappe de courant $\vec j_s$ : $\|\vec B\| = \dfrac{\mu_0j_s}{2}$, parallèle au plan, de sens opposés de part et d'autre.

## Méthode

1. Symétries : direction de $\vec B$ ; invariances : variables.
2. Choisir un contour d'Ampère où $\vec B$ est tangent (de norme constante) ou orthogonal.
3. Calculer la circulation et le courant enlacé.

## Pièges classiques

- Ne pas confondre les règles de symétrie de $\vec E$ et de $\vec B$.
- Le courant enlacé dépend de l'orientation du contour : fixer celle-ci d'abord.
