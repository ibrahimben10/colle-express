---
titre: Machines thermiques
---
## L'essentiel

Une machine ditherme fonctionne en cycle entre une source chaude $T_c$ et une source froide $T_f$. Les deux principes, appliqués sur un cycle, limitent son efficacité.

> **Propriété — Bilans sur un cycle.** $W + Q_c + Q_f = 0$ (premier principe) et $\dfrac{Q_c}{T_c} + \dfrac{Q_f}{T_f} \leq 0$ (inégalité de Clausius), avec égalité pour un cycle réversible.

## Moteur

[[fig:p4-machines-1]]

Le moteur reçoit $Q_c > 0$, cède $Q_f < 0$ et fournit du travail ($W < 0$).

> **Théorème de Carnot (moteur).** $\eta = \dfrac{-W}{Q_c} \leq \eta_C = 1 - \dfrac{T_f}{T_c}$.

## Réfrigérateur et pompe à chaleur

[[fig:p4-machines-2]]

Ils reçoivent du travail ($W > 0$) pour transférer de l'énergie de la source froide vers la source chaude.

| Machine | Efficacité | Maximum (Carnot) |
|---|---|---|
| réfrigérateur | $e = \dfrac{Q_f}{W}$ | $\dfrac{T_f}{T_c - T_f}$ |
| pompe à chaleur | $e = \dfrac{-Q_c}{W}$ | $\dfrac{T_c}{T_c - T_f}$ |

L'efficacité d'une pompe à chaleur est supérieure à 1 : elle chauffe mieux qu'une résistance.

## Cycles modèles

[[fig:p4-machines-3]]

Le cycle de Carnot (deux isothermes, deux adiabatiques réversibles) atteint l'efficacité maximale.

[[fig:p4-machines-4]]

Le cycle de Beau de Rochas modélise le moteur à essence : rendement $\eta = 1 - a^{1 - \gamma}$, où $a = V_{\max}/V_{\min}$ est le taux de compression.

## Exemple corrigé

**Énoncé.** Un moteur ditherme fonctionne entre une source chaude à 600 K et une source froide à 300 K. Il fournit 1 kJ de travail par cycle et reçoit 3 kJ de la source chaude. Calculer son rendement et le comparer au rendement de Carnot.

**Solution.**
1. Rendement : $\eta = \dfrac{-W}{Q_c} = \dfrac13 \approx 33$ %.
2. Rendement de Carnot : $\eta_C = 1 - \dfrac{T_f}{T_c} = 50$ %.
3. $\eta < \eta_C$ : la machine est possible mais irréversible. Chaleur rejetée : $Q_f = -(Q_c + W) = -2$ kJ.

## Pièges classiques

- Les températures sont en kelvins dans les formules de Carnot.
- Un moteur monotherme est impossible (énoncé de Kelvin) : il faut deux sources.
- L'efficacité d'un récepteur se définit avec la grandeur **utile** (ce qu'on veut) divisée par la grandeur **coûteuse** ($W$).
