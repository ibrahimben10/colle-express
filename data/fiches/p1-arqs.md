---
titre: Circuits électriques dans l'ARQS
---
## L'essentiel

Dans l'**approximation des régimes quasi stationnaires** (ARQS), le courant a la même valeur en tout point d'une branche à un instant donné. On décrit alors un circuit avec deux lois (nœuds et mailles) et les relations courant-tension de chaque dipôle.

## Charge, courant, tension

- La charge électrique est quantifiée ($q = ne$, $e = 1{,}6\cdot10^{-19}$ C) et conservée.
- Intensité : $i = \dfrac{\mathrm dq}{\mathrm dt}$ (en A), débit de charge à travers une section, algébrique selon le sens choisi.
- Potentiel électrique $V$ défini à une constante près (on fixe une **masse**) ; tension $u_{AB} = V_A - V_B$ (en V), représentée par une flèche pointant vers $A$.

> **Propriété — Validité de l'ARQS.** Le signal se propage à une vitesse proche de $c$ ; l'ARQS est valable si la taille $L$ du circuit vérifie $L \ll cT$ (ou $L \ll \lambda$), où $T$ est la durée caractéristique des variations. Pour $f = 50$ Hz, $\lambda = 6000$ km : toujours valable au laboratoire ; pour $f = 1$ GHz, $\lambda = 30$ cm : elle ne l'est plus.

## Conventions et puissance

[[fig:p1-arqs-1]]

> **Définition — Conventions.** En convention **récepteur**, $u$ et $i$ sont fléchés en sens opposés et $P = ui$ est la puissance **reçue**. En convention **générateur**, ils sont dans le même sens et $P = ui$ est la puissance **fournie**.

Un dipôle est récepteur s'il reçoit effectivement de l'énergie ($P_{\text{reçue}} > 0$), générateur sinon. Énergie reçue entre $t_1$ et $t_2$ : $W = \int_{t_1}^{t_2}u\,i\,\mathrm dt$.

## Lois de Kirchhoff

[[fig:p1-arqs-2]]

> **Loi des nœuds.** La somme des intensités qui arrivent à un nœud est égale à la somme de celles qui en partent (conservation de la charge dans l'ARQS).

> **Loi des mailles.** Le long d'une maille parcourue dans un sens choisi, la somme algébrique des tensions est nulle (signe + pour une flèche dans le sens de parcours).

Dipôles en **série** : même courant ; en **parallèle** (dérivation) : même tension.

## Dipôles usuels

### Relations (convention récepteur)

| Dipôle | Relation | Énergie |
|---|---|---|
| résistance $R$ | $u = Ri$ (loi d'Ohm) | dissipe $P = Ri^2 = \frac{u^2}{R}$ |
| condensateur $C$ | $i = C\,\dfrac{\mathrm du}{\mathrm dt}$ | stocke $\tfrac12 Cu^2$ |
| bobine $L$ | $u = L\,\dfrac{\mathrm di}{\mathrm dt}$ | stocke $\tfrac12 Li^2$ |
| interrupteur fermé / fil | $u = 0$ | |
| interrupteur ouvert | $i = 0$ | |

> **Propriété — Continuité.** La tension aux bornes d'un condensateur et l'intensité dans une bobine sont des fonctions **continues** du temps (sinon l'énergie stockée varierait instantanément, ce qui demanderait une puissance infinie).

En régime **continu permanent** : un condensateur se comporte comme un interrupteur ouvert ($i = 0$), une bobine comme un fil ($u = 0$).

### Sources

- Source idéale de tension : $u = E$ quel que soit $i$ ; source idéale de courant : $i = \eta$ quel que soit $u$.
- **Modèle de Thévenin** d'un générateur réel : source $E$ en série avec une résistance interne $r$ : $u = E - ri$ (convention générateur).
- Modèle de Norton : source de courant $\eta$ en parallèle avec $r$ ; équivalence avec $E = r\eta$.

### Caractéristique et point de fonctionnement

La caractéristique $i = f(u)$ d'un dipôle est linéaire pour $R$, affine pour un générateur réel. Quand on branche un générateur sur un récepteur, le **point de fonctionnement** est l'intersection de leurs caractéristiques (tracées dans la même convention).

## Associations et diviseurs

[[fig:p1-arqs-3]]

- Résistances en série : $R = R_1 + R_2$ ; en parallèle : $\dfrac1R = \dfrac1{R_1} + \dfrac1{R_2}$ (conductances $G = \frac1R$ qui s'ajoutent).
- Condensateurs : capacités qui s'ajoutent en **parallèle** ; bobines : inductances qui s'ajoutent en **série**.
- **Diviseur de tension** : $U_2 = \dfrac{R_2}{R_1 + R_2}U$. **Diviseur de courant** : $I_2 = \dfrac{R_1}{R_1 + R_2}I$ (c'est l'**autre** résistance au numérateur).

### Résistances d'entrée et de sortie

Un appareil de mesure perturbe le circuit : un voltmètre doit avoir une grande résistance d'entrée (en parallèle), un ampèremètre une faible résistance (en série). Un oscilloscope a typiquement $R_e = 1$ MΩ ; un GBF a une résistance de sortie de 50 Ω.

## Méthode

1. Flécher toutes les intensités et tensions, préciser les conventions.
2. Simplifier par associations (série, parallèle) quand c'est possible.
3. Écrire les lois des nœuds et des mailles, puis les relations des dipôles.
4. Vérifier : homogénéité, cas limites ($R \to 0$, $R \to \infty$), bilan de puissance (puissance fournie = puissance reçue).

## Exemple corrigé

**Énoncé.** Un générateur de f.é.m. $E = 12$ V alimente deux résistances $R_1 = 2$ kΩ et $R_2 = 4$ kΩ montées en série. Calculer l'intensité et la tension aux bornes de $R_2$.

**Solution.**
1. Loi des mailles : $E = R_1I + R_2I$, donc $I = \dfrac{E}{R_1 + R_2} = 2$ mA.
2. Pont diviseur de tension : $U_2 = E\,\dfrac{R_2}{R_1 + R_2} = 8$ V.
3. Vérification : $U_1 = 4$ V et $U_1 + U_2 = E$. Puissance fournie : $EI = 24$ mW, entièrement dissipée par effet Joule.

## Exemple corrigé (générateur réel)

**Énoncé.** Une pile ($E = 4{,}5$ V, $r = 1{,}5$ Ω) alimente une résistance $R$. Pour quelle valeur de $R$ la puissance reçue est-elle maximale ?

**Solution.** $I = \dfrac{E}{R + r}$ et $P = RI^2 = \dfrac{RE^2}{(R + r)^2}$. $\dfrac{\mathrm dP}{\mathrm dR} = E^2\dfrac{r - R}{(R + r)^3}$ s'annule pour $R = r$ : $P_{\max} = \dfrac{E^2}{4r} \approx 3{,}4$ W (adaptation d'impédance).

## Pièges classiques

- Le diviseur de tension suppose que les deux résistances sont parcourues par le **même** courant (pas de dérivation entre elles).
- Toujours préciser la convention avant d'écrire $u = Ri$ : en convention générateur, $u = -Ri$.
- Ne pas confondre potentiel (défini à une constante près) et tension.

## Ordres de grandeur

Courants de quelques mA en électronique, de quelques A dans un appareil ménager ; tensions de 5 à 15 V en TP ; $R$ de 10 Ω à 1 MΩ ; $C$ de 1 nF à 1 mF ; $L$ de 1 mH à 1 H.
