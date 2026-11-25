---
titre: Circuits électriques dans l'ARQS
---
## L'essentiel

Dans l'**approximation des régimes quasi stationnaires** (ARQS), le courant a la même valeur en tout point d'une branche à un instant donné. Elle est valable si la taille du circuit est petite devant $c\,T$, où $T$ est la durée caractéristique des variations.

## Courant, tension, puissance

- Intensité : $i = \dfrac{\mathrm dq}{\mathrm dt}$ (en A), algébrique selon le sens choisi.
- Tension : $u_{AB} = V_A - V_B$ (en V), représentée par une flèche pointant vers $A$.

[[fig:p1-arqs-1]]

> **Définition — Conventions.** En convention **récepteur**, $u$ et $i$ sont fléchés en sens opposés et $P = ui$ est la puissance reçue. En convention **générateur**, ils sont dans le même sens et $P = ui$ est la puissance fournie.

## Lois de Kirchhoff

[[fig:p1-arqs-2]]

> **Loi des nœuds.** La somme des intensités qui arrivent à un nœud est égale à la somme de celles qui en partent.

> **Loi des mailles.** Le long d'une maille parcourue dans un sens choisi, la somme algébrique des tensions est nulle (signe + pour une flèche dans le sens de parcours).

## Dipôles usuels (convention récepteur)

| Dipôle | Relation | Énergie stockée |
|---|---|---|
| résistance $R$ | $u = Ri$ | aucune (dissipe $Ri^2$) |
| condensateur $C$ | $i = C\,\dfrac{\mathrm du}{\mathrm dt}$ | $\tfrac12 Cu^2$ |
| bobine $L$ | $u = L\,\dfrac{\mathrm di}{\mathrm dt}$ | $\tfrac12 Li^2$ |
| générateur réel | $u = E - ri$ (convention générateur) | |

> **Propriété — Continuité.** La tension aux bornes d'un condensateur et l'intensité dans une bobine sont des fonctions **continues** du temps.

## Associations et diviseurs

[[fig:p1-arqs-3]]

Résistances en série : $R = R_1 + R_2$ ; en parallèle : $\dfrac1R = \dfrac1{R_1} + \dfrac1{R_2}$.

Diviseur de tension : $U_2 = \dfrac{R_2}{R_1 + R_2}U$. Diviseur de courant : $I_2 = \dfrac{R_1}{R_1 + R_2}I$ (c'est l'**autre** résistance au numérateur).

## Pièges classiques

- Le diviseur de tension suppose que les deux résistances sont parcourues par le **même** courant (pas de dérivation entre elles).
- Toujours préciser la convention avant d'écrire $u = Ri$ : en convention générateur, $u = -Ri$.
