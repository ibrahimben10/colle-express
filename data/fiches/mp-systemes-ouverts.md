---
titre: Systèmes ouverts en régime stationnaire
---
## L'essentiel

Dans une machine industrielle, un fluide s'écoule en régime stationnaire à travers des organes (compresseur, turbine, détendeur…). On écrit les principes de la thermodynamique **par unité de masse de fluide** qui traverse l'organe.

## Système fermé fictif

[[fig:mp-systemes-ouverts-1]]

On suit un système **fermé** : le fluide contenu dans le volume de contrôle plus la masse $\delta m_e$ qui va entrer pendant $\mathrm dt$. En régime stationnaire, le débit massique $D_m$ est le même à l'entrée et à la sortie.

## Premier et second principes industriels

> **Loi — Premier principe pour un écoulement stationnaire.** $\Delta h + \Delta e_c + g\,\Delta z = w_u + q$, avec $h$ l'enthalpie massique, $w_u$ le travail utile massique (hors forces de pression) et $q$ le transfert thermique massique reçus.

> **Loi — Second principe.** $\Delta s = s_e + s_c$, avec $s_e = q/T_{\text{ext}}$ et $s_c \ge 0$.

En puissance : $D_m(\Delta h + \Delta e_c + g\Delta z) = \mathcal P_u + \mathcal P_{th}$.

## Organes usuels

[[fig:mp-systemes-ouverts-2]]

| Organe | Hypothèses usuelles | Bilan |
|---|---|---|
| compresseur, turbine | adiabatique, $\Delta e_c$ négligeable | $w_u = \Delta h$ |
| détendeur (vanne) | adiabatique, sans travail | $\Delta h = 0$ |
| tuyère | adiabatique, sans travail | $\Delta h + \Delta e_c = 0$ |
| échangeur | sans travail | $q = \Delta h$ |

## Diagramme des frigoristes

[[fig:mp-systemes-ouverts-3]]

Dans le diagramme $(\log P, h)$, les transformations isobares et isenthalpiques sont des segments : on lit directement $w_u$ et $q$ en différences d'abscisses. Efficacité d'un réfrigérateur : $e = \dfrac{q_{\text{évap}}}{w_u}$.

## Pièges classiques

- C'est l'**enthalpie**, et non l'énergie interne, qui intervient : le travail des forces de pression d'entrée et de sortie est inclus dans $h$.
- Un détendeur n'est pas réversible : il crée de l'entropie.
