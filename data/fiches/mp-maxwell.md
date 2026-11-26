---
titre: Équations de Maxwell
---
## L'essentiel

Les quatre équations de Maxwell décrivent tous les phénomènes électromagnétiques. Elles relient les champs $\vec E$ et $\vec B$ à leurs sources : la densité de charge $\rho$ et la densité de courant $\vec j$.

> **Équations de Maxwell.**
> - Maxwell-Gauss : $\mathrm{div}\,\vec E = \dfrac{\rho}{\varepsilon_0}$
> - Maxwell-flux : $\mathrm{div}\,\vec B = 0$
> - Maxwell-Faraday : $\overrightarrow{\mathrm{rot}}\,\vec E = -\dfrac{\partial\vec B}{\partial t}$
> - Maxwell-Ampère : $\overrightarrow{\mathrm{rot}}\,\vec B = \mu_0\vec j + \mu_0\varepsilon_0\dfrac{\partial\vec E}{\partial t}$

## Formes intégrales

| Équation | Forme intégrale |
|---|---|
| Maxwell-Gauss | théorème de Gauss |
| Maxwell-flux | flux de $\vec B$ nul à travers toute surface fermée |
| Maxwell-Faraday | loi de Faraday : $e = -\dfrac{\mathrm d\Phi}{\mathrm dt}$ |
| Maxwell-Ampère | théorème d'Ampère généralisé |

## Conservation de la charge

En prenant la divergence de Maxwell-Ampère : $\dfrac{\partial\rho}{\partial t} + \mathrm{div}\,\vec j = 0$. Le terme $\varepsilon_0\dfrac{\partial\vec E}{\partial t}$ (« courant de déplacement ») est indispensable à cette cohérence.

## Relations de passage

[[fig:mp-maxwell-1]]

À la traversée d'une surface chargée ($\sigma$) et parcourue par des courants ($\vec j_s$) :
$$\vec E_2 - \vec E_1 = \frac{\sigma}{\varepsilon_0}\vec n_{12},\qquad \vec B_2 - \vec B_1 = \mu_0\,\vec j_s\wedge\vec n_{12}.$$

## Régimes particuliers

- **Statique** : on retrouve l'électrostatique et la magnétostatique, découplées.
- **ARQS magnétique** : on néglige le courant de déplacement ; valable si les dimensions sont petites devant la longueur d'onde.

## Exemple corrigé

**Énoncé.** Montrer qu'en régime variable, Maxwell-Ampère sans le terme $\varepsilon_0\partial\vec E/\partial t$ contredirait la conservation de la charge.

**Solution.**
1. Sans ce terme : $\overrightarrow{\mathrm{rot}}\,\vec B = \mu_0\vec j$. La divergence d'un rotationnel est nulle, donc $\mathrm{div}\,\vec j = 0$.
2. Or la conservation de la charge impose $\mathrm{div}\,\vec j = -\partial\rho/\partial t$, non nul pendant la charge d'un condensateur.
3. Avec le terme complet : $0 = \mu_0\,\mathrm{div}\,\vec j + \mu_0\varepsilon_0\,\partial(\mathrm{div}\,\vec E)/\partial t = \mu_0\left(\mathrm{div}\,\vec j + \partial\rho/\partial t\right)$, grâce à Maxwell-Gauss : tout est cohérent.

## Pièges classiques

- Les champs sont couplés dès qu'ils varient dans le temps.
- Bien orienter $\vec n_{12}$ du milieu 1 vers le milieu 2.
