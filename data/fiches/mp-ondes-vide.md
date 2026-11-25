---
titre: Ondes électromagnétiques dans le vide
---
## L'essentiel

Dans le vide sans charges ni courants, les équations de Maxwell conduisent à l'**équation de d'Alembert** pour chaque composante des champs : la perturbation se propage à la vitesse $c = 1/\sqrt{\mu_0\varepsilon_0}$.

$$\Delta\vec E - \frac{1}{c^2}\frac{\partial^2\vec E}{\partial t^2} = \vec 0.$$

## Onde plane progressive monochromatique

[[fig:mp-ondes-vide-1]]

$\vec E = \vec E_0\cos(\omega t - \vec k\cdot\vec r)$, avec la relation de dispersion $k = \omega/c$.

> **Propriété — Structure de l'OPPM.** L'onde est **transverse** ($\vec E$ et $\vec B$ orthogonaux à $\vec k$) et $\vec B = \dfrac{\vec k\wedge\vec E}{\omega}$ : $(\vec E, \vec B, \vec k)$ est un trièdre direct, $\|\vec B\| = \|\vec E\|/c$.

Énergie : $\langle u\rangle = \tfrac12\varepsilon_0E_0^2$ et $\langle\vec\Pi\rangle = c\langle u\rangle\,\vec u_k$ : l'énergie se propage à la vitesse $c$.

## Polarisation

[[fig:mp-ondes-vide-2]]

- **Rectiligne** : $\vec E$ garde une direction fixe.
- **Circulaire** : deux composantes de même amplitude en quadrature.
- **Elliptique** : cas général.

Un polariseur ne transmet que la composante selon sa direction : **loi de Malus** $I = I_0\cos^2\theta$.

## Notation complexe

Pour une OPPM, $\mathrm{div} \to -j\vec k\cdot$, $\overrightarrow{\mathrm{rot}} \to -j\vec k\wedge$, $\partial/\partial t \to j\omega$ (convention $e^{j(\omega t - \vec k\cdot\vec r)}$).

## Pièges classiques

- La relation $\vec B = \vec k\wedge\vec E/\omega$ n'est valable que pour une onde plane progressive (pas pour une onde stationnaire).
- La lumière naturelle n'est pas polarisée.
