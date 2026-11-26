---
titre: Optique géométrique
---
## L'essentiel

Dans l'approximation de l'optique géométrique ($\lambda$ petite devant les dimensions en jeu), la lumière suit des **rayons** rectilignes dans un milieu homogène et isotrope, et les lois de Snell-Descartes décrivent ce qui se passe à une interface. Les lentilles minces, utilisées dans les conditions de Gauss, forment des images ; on en déduit les instruments (œil, loupe, lunette, appareil photo).

## Sources et milieux

- Indice $n = \frac cv$ ; air $n \approx 1{,}000$, eau $1{,}33$, verre $1{,}5$.
- Propagation rectiligne dans un milieu homogène ; **principe du retour inverse** de la lumière ; indépendance des rayons lumineux.
- Limite : quand une ouverture n'est pas grande devant $\lambda$, la diffraction intervient.

## Lois de Snell-Descartes

[[fig:p1-optique-geo-1]]

> **Loi — Réflexion et réfraction.** Les rayons réfléchi et réfracté sont dans le plan d'incidence ; $i_1' = i_1$ et $n_1\sin i_1 = n_2\sin i_2$, angles mesurés par rapport à la **normale**.

En passant dans un milieu plus réfringent ($n_2 > n_1$), le rayon se rapproche de la normale. La dispersion ($n$ dépend de $\lambda$) explique la décomposition de la lumière par un prisme.

## Réflexion totale

[[fig:p1-optique-geo-2]]

> **Propriété — Angle limite.** Si $n_1 > n_2$, il n'y a plus de rayon réfracté pour $i_1 > i_\ell$ avec $\sin i_\ell = n_2/n_1$ : toute la lumière est réfléchie. Verre-air : $i_\ell \approx 42°$.

Application : **fibre optique** à saut d'indice (cœur $n_1$, gaine $n_2 < n_1$). Les rayons guidés sont ceux qui subissent la réflexion totale ; l'**ouverture numérique** est $\sin\theta_{\max} = \sqrt{n_1^2 - n_2^2}$ (entrée depuis l'air). Les différents trajets ont des durées différentes : dispersion intermodale, qui limite le débit.

## Formation des images

- Un système est **stigmatique** pour un couple $(A, A')$ si tous les rayons issus de $A$ passent par $A'$ ; **aplanétique** si l'image d'un objet plan perpendiculaire à l'axe est plane et perpendiculaire à l'axe. Seul le miroir plan est rigoureusement stigmatique pour tout point.
- Objet et image **réels** (rayons effectifs) ou **virtuels** (prolongements).
- **Conditions de Gauss** : rayons peu inclinés et proches de l'axe ; les systèmes centrés sont alors approximativement stigmatiques et aplanétiques.

Miroir plan : l'image est symétrique de l'objet par rapport au miroir (virtuelle pour un objet réel).

## Lentilles minces

Une lentille mince est caractérisée par son centre $O$, ses foyers objet $F$ et image $F'$ symétriques par rapport à $O$, sa distance focale $f' = \overline{OF'}$ et sa vergence $V = \frac{1}{f'}$ (en dioptries, δ). Convergente : $f' > 0$ ; divergente : $f' < 0$.

> **Formule — Conjugaison et grandissement (origine au centre).** $\dfrac{1}{\overline{OA'}} - \dfrac{1}{\overline{OA}} = \dfrac{1}{f'}$ et $\gamma = \dfrac{\overline{A'B'}}{\overline{AB}} = \dfrac{\overline{OA'}}{\overline{OA}}$.

Avec l'origine aux foyers (Newton) : $\overline{FA}\cdot\overline{F'A'} = -f'^2$ et $\gamma = -\frac{f'}{\overline{FA}} = -\frac{\overline{F'A'}}{f'}$.

[[fig:p1-optique-geo-3]]

Les trois rayons particuliers : un rayon passant par $O$ n'est pas dévié ; un rayon parallèle à l'axe émerge en passant par $F'$ ; un rayon passant par $F$ émerge parallèle à l'axe. Un rayon quelconque : utiliser un **foyer secondaire** (rayons parallèles entre eux convergent dans le plan focal image).

[[fig:p1-optique-geo-4]]

Pour une lentille **divergente**, $f' < 0$ : $F'$ est du côté de la lumière incidente, et un objet réel donne une image virtuelle, droite et réduite.

- Lentille convergente, objet réel au-delà de $F$ : image réelle renversée ; objet entre $F$ et $O$ : image virtuelle droite agrandie (**loupe**).
- Pour obtenir une image réelle d'un objet réel sur un écran à distance $D$ de l'objet, il faut $D \ge 4f'$.
- Deux lentilles minces accolées : les vergences s'ajoutent.

## Instruments

### L'œil

[[fig:p1-optique-geo-6]]

L'œil se modélise par une lentille de vergence variable (cristallin), un diaphragme (iris) et un écran fixe (rétine) : l'**accommodation** permet de voir net du punctum remotum (l'infini pour un œil normal) au punctum proximum (environ 25 cm). Pouvoir séparateur : environ $3\cdot10^{-4}$ rad (1 minute d'arc). Myopie (œil trop convergent, corrigé par une lentille divergente), hypermétropie (corrigée par une convergente), presbytie (perte d'accommodation).

### Appareil photographique

Objectif (lentille convergente) formant une image réelle sur le capteur ; la mise au point déplace l'objectif. Profondeur de champ : plage de distances nettes, d'autant plus grande que le diaphragme est fermé (nombre d'ouverture $N = f'/D$ grand).

### Lunette afocale

[[fig:p1-optique-geo-5]]

Une lunette **afocale** ($F_1' = F_2$) donne d'un objet à l'infini une image à l'infini (observation sans fatigue) ; son grossissement est $G = \alpha'/\alpha = -f_1'/f_2'$. Lunette astronomique : deux convergentes, image renversée ; lunette de Galilée : oculaire divergent, image droite.

## Exemple corrigé

**Énoncé.** Un objet de 2 cm est placé à 30 cm devant une lentille convergente de distance focale $f' = 10$ cm. Où est l'image et quelle est sa taille ?

**Solution.**
1. $\overline{OA} = -30$ cm : $\dfrac{1}{\overline{OA'}} = \dfrac{1}{10} - \dfrac{1}{30} = \dfrac{1}{15}$, donc $\overline{OA'} = 15$ cm.
2. $\gamma = \overline{OA'}/\overline{OA} = -0{,}5$.
3. L'image est réelle, renversée, de taille 1 cm.

## Exemple corrigé (fibre optique)

**Énoncé.** Fibre de cœur $n_1 = 1{,}50$ et gaine $n_2 = 1{,}48$. Angle d'acceptance dans l'air ?

**Solution.** Réflexion totale à l'interface cœur-gaine si l'angle d'incidence dépasse $i_\ell$ avec $\sin i_\ell = \frac{n_2}{n_1}$. Le rayon réfracté à l'entrée fait l'angle $\frac\pi2 - i_\ell$ avec l'axe, d'où $\sin\theta_{\max} = n_1\cos i_\ell = \sqrt{n_1^2 - n_2^2} \approx 0{,}24$ : $\theta_{\max} \approx 14°$.

## Pièges classiques

- Les distances sont **algébriques** : orienter l'axe dans le sens de la lumière.
- Une image virtuelle se construit avec les **prolongements** des rayons (en pointillés).
- La réflexion totale n'existe que du côté du milieu **le plus** réfringent.
- Pour une divergente, $F'$ est avant la lentille.
