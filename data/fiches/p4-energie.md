---
titre: Énergie échangée au cours d'une transformation
---
## L'essentiel

Un système échange de l'énergie avec l'extérieur sous deux formes : le **travail** $W$ (lié à un déplacement macroscopique, par exemple des forces de pression) et le **transfert thermique** $Q$. Par convention, ils sont comptés **positivement quand le système les reçoit**.

## Travail des forces de pression

$$\delta W = -P_{\text{ext}}\,\mathrm dV,\qquad W = -\int P_{\text{ext}}\,\mathrm dV.$$

> **Définition — Transformation quasi statique.** Suite continue d'états d'équilibre ; on peut alors remplacer $P_{\text{ext}}$ par $P$.

[[fig:p4-energie-1]]

Dans le diagramme de Watt $(P, V)$, $|W|$ est l'aire sous la courbe ; une détente ($\mathrm dV > 0$) donne $W < 0$.

| Transformation (gaz parfait, quasi statique) | Travail reçu |
|---|---|
| isochore | $W = 0$ |
| isobare | $W = -P(V_f - V_i)$ |
| isotherme | $W = -nRT\ln\dfrac{V_f}{V_i}$ |
| monobare ($P_{\text{ext}}$ fixée) | $W = -P_{\text{ext}}(V_f - V_i)$ |

## Cycles

[[fig:p4-energie-2]]

Sur un cycle, $|W|$ est l'aire du cycle : parcouru dans le sens horaire, il est **moteur** ($W < 0$) ; dans le sens trigonométrique, **récepteur** ($W > 0$).

## Transferts thermiques

Trois modes : conduction (de proche en proche), convection (mouvement du fluide), rayonnement. Une transformation **adiabatique** se fait sans transfert thermique ($Q = 0$) ; un **thermostat** garde une température fixe quel que soit $Q$.

## Exemple corrigé

**Énoncé.** On chauffe 2 kg d'eau liquide de 20 °C à 100 °C, puis on la vaporise entièrement. Quelle énergie faut-il ? ($c = 4{,}18$ kJ·kg⁻¹·K⁻¹, $\ell_v = 2{,}26$ MJ·kg⁻¹.)

**Solution.**
1. Échauffement du liquide : $Q_1 = mc\Delta T = 2\times4{,}18\times80 \approx 669$ kJ.
2. Vaporisation à 100 °C : $Q_2 = m\ell_v = 4{,}52$ MJ.
3. Total $\approx 5{,}2$ MJ : le changement d'état coûte presque sept fois plus que l'échauffement.

## Pièges classiques

- $W$ et $Q$ dépendent du chemin suivi : on n'écrit pas $\Delta W$ ni $\Delta Q$.
- Le signe : $W > 0$ quand le gaz est comprimé.
