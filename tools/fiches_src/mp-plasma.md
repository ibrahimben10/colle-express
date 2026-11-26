---
titre: Propagation dans un plasma, dispersion
---
## L'essentiel

Un plasma (gaz ionisé, ionosphère) est un milieu **dispersif** : la vitesse de phase dépend de la fréquence. Les ondes de pulsation inférieure à la pulsation plasma ne s'y propagent pas.

## Relation de dispersion

Les électrons libres, de densité $n$, sont mis en mouvement par l'onde. On obtient :

> **Relation de dispersion d'un plasma.** $k^2 = \dfrac{\omega^2 - \omega_p^2}{c^2}$, avec la pulsation plasma $\omega_p = \sqrt{\dfrac{ne^2}{m\varepsilon_0}}$.

[[fig:mp-plasma-1]]

- $\omega > \omega_p$ : $k$ réel, propagation sans atténuation.
- $\omega < \omega_p$ : $k$ imaginaire pur, onde **évanescente** (réflexion totale) ; c'est pourquoi les ondes radio longues se réfléchissent sur l'ionosphère.

## Vitesse de phase et vitesse de groupe

[[fig:mp-plasma-2]]

> **Définitions.** Vitesse de phase $v_\varphi = \dfrac{\omega}{k}$ (vitesse des crêtes) ; vitesse de groupe $v_g = \dfrac{\mathrm d\omega}{\mathrm dk}$ (vitesse de l'enveloppe, donc de l'énergie et de l'information).

Dans le plasma, $v_\varphi > c$ mais $v_g < c$, et $v_\varphi v_g = c^2$.

## Ordres de grandeur

Ionosphère : $n \approx 10^{11}$ à $10^{12}$ m⁻³, soit $f_p = \omega_p/2\pi$ de quelques MHz.

## Exemple corrigé

**Énoncé.** L'ionosphère contient $n = 10^{12}$ électrons par m³. Une onde radio de 5 MHz s'y propage-t-elle ? Et une onde FM à 100 MHz ?

**Solution.**
1. $\omega_p = \sqrt{\dfrac{ne^2}{m\varepsilon_0}} \approx 5{,}6\cdot10^7$ rad·s⁻¹, soit $f_p \approx 9$ MHz.
2. À 5 MHz, $f < f_p$ : onde évanescente, réflexion. Ces ondes « rebondissent » sur l'ionosphère et portent loin.
3. À 100 MHz, $f \gg f_p$ : l'onde traverse l'ionosphère (d'où l'usage de fréquences élevées pour les satellites).

## Pièges classiques

- $v_\varphi > c$ ne contredit pas la relativité : aucune information ne se propage à la vitesse de phase.
- Dans un milieu dispersif, un paquet d'ondes se déforme au cours de la propagation.
