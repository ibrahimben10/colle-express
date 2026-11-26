---
titre: Circuit fixe dans un champ magnétique variable
---
## L'essentiel

Un circuit fixe plongé dans un champ variable (cas de Neumann) est le siège d'une f.é.m. induite. Deux circuits proches se couplent par leur inductance mutuelle : c'est le principe du transformateur.

## Inductance mutuelle

[[fig:p5-circuit-fixe-1]]

> **Définition — Inductance mutuelle.** Le flux du champ créé par le circuit 1 à travers le circuit 2 est $\Phi_{1\to2} = Mi_1$, et réciproquement $\Phi_{2\to1} = Mi_2$ avec le **même** coefficient $M$.

Équations électriques des deux circuits couplés (convention récepteur) :
$$u_1 = R_1i_1 + L_1\frac{\mathrm di_1}{\mathrm dt} + M\frac{\mathrm di_2}{\mathrm dt},\qquad u_2 = R_2i_2 + L_2\frac{\mathrm di_2}{\mathrm dt} + M\frac{\mathrm di_1}{\mathrm dt}.$$

Énergie magnétique : $\tfrac12L_1i_1^2 + \tfrac12L_2i_2^2 + Mi_1i_2$.

## Transformateur

[[fig:p5-circuit-fixe-2]]

Le noyau de fer canalise le flux, commun aux deux enroulements. Pour un transformateur idéal :
$$\left|\frac{u_2}{u_1}\right| = \frac{N_2}{N_1}.$$
Il élève ou abaisse une tension **alternative** ; il ne fonctionne pas en continu.

## Applications

Transport de l'énergie électrique à haute tension (moins de pertes Joule), plaques à induction, chargeurs sans fil.

## Exemple corrigé

**Énoncé.** Un transformateur idéal a $N_1 = 500$ spires au primaire et $N_2 = 25$ au secondaire. On applique 230 V efficaces au primaire. Quelle tension obtient-on, et quel courant primaire si le secondaire débite 2 A ?

**Solution.**
1. Rapport de transformation : $m = N_2/N_1 = 0{,}05$, donc $U_2 = mU_1 = 11{,}5$ V.
2. Transformateur idéal : pas de pertes, $U_1I_1 = U_2I_2$, d'où $I_1 = mI_2 = 0{,}1$ A.
3. On abaisse la tension et on élève le courant dans le même rapport.

## Pièges classiques

- Le signe de $M$ dépend des orientations choisies pour les deux circuits.
- En régime continu, aucune f.é.m. n'est induite : le transformateur ne transmet rien.
