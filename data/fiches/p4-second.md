---
titre: Deuxième principe, bilans d'entropie
---
## L'essentiel

Le deuxième principe introduit l'**entropie** $S$, fonction d'état extensive, et rend compte de l'irréversibilité des transformations réelles.

> **Principe — Deuxième principe.** Pour un système fermé : $\Delta S = S_e + S_c$, avec l'entropie échangée $S_e = \sum\dfrac{Q_i}{T_i}$ ($T_i$ température de la source) et l'entropie créée $S_c \geq 0$, nulle pour une transformation réversible.

## Causes d'irréversibilité

Frottements, inhomogénéités de température ou de pression, réactions chimiques, diffusion : toutes créent de l'entropie.

## Expressions de l'entropie

| Système | $\Delta S$ |
|---|---|
| gaz parfait | $nC_{V,m}\ln\dfrac{T_f}{T_i} + nR\ln\dfrac{V_f}{V_i}$ |
| phase condensée | $C\ln\dfrac{T_f}{T_i}$ |
| changement d'état à $T$ | $\dfrac{m\,\Delta h}{T}$ |

> **Loi de Laplace.** Pour un gaz parfait subissant une transformation adiabatique **réversible** : $PV^\gamma = $ constante, $TV^{\gamma - 1} = $ constante.

## Diagramme entropique

[[fig:p4-second-1]]

Dans le diagramme $(T, S)$, une isotherme est horizontale, une adiabatique réversible (isentropique) est verticale, et l'aire sous une courbe réversible vaut le transfert thermique reçu.

## Méthode — Bilan d'entropie

1. Calculer $\Delta S$ par un chemin réversible fictif (fonction d'état).
2. Calculer $S_e$ avec la température de la **source**, pas celle du système.
3. En déduire $S_c = \Delta S - S_e \geq 0$ : son signe vérifie la cohérence.

## Pièges classiques

- Dans $S_e$, c'est la température de la frontière (du thermostat) qui intervient.
- La loi de Laplace exige une transformation adiabatique **et** réversible.
