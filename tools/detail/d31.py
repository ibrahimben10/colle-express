D = {}

D['p-opt-2'] = r"""
**1. Relation de conjugaison.** On note $O$ le centre de $L$, $p=\overline{OA}<0$ (objet réel) et $p'=\overline{OA'}=d>0$ (image réelle sur la plaque). La formule de Descartes s'écrit $\frac1{p'}-\frac1p=\frac1{f'}$. La distance objet-plaque vaut $D=d-p=d+|p|$, donc $p=d-D$ et
$$\frac1d+\frac1{D-d}=\frac1{f'}\iff\frac D{d(D-d)}=\frac1{f'}\iff d^2-Dd+Df'=0.$$

**1. Condition d'existence.** Cette équation du second degré en $d$ a des racines réelles si et seulement si son discriminant est positif : $\Delta=D^2-4Df'=D(D-4f')\ge0$, soit
$$D\ge4f'.$$
C'est la condition classique : la distance objet-image réelle d'une lentille convergente est au moins $4f'$.

**1. Domaine de $d$.** Les racines sont $d_\pm=\frac{D\pm\sqrt{D^2-4Df'}}2$. La contrainte $d\le\frac D2$ sélectionne $d_-$. Étudions-la en fonction de $D$ :
- pour $D=4f'$ : $d_-=\frac D2=2f'$ ;
- quand $D\to+\infty$ : $d_-=\frac D2\Big(1-\sqrt{1-\frac{4f'}D}\Big)\approx\frac D2\cdot\frac{2f'}D=f'$ (objet à l'infini, image dans le plan focal).

$d_-$ décroît de $2f'$ à $f'$ quand $D$ croît. Donc
$$D\ge4f',\qquad f'<d\le2f'.$$
Remarque : $d\le\frac D2$ équivaut à $d\le|p|$, c'est-à-dire $|\gamma|=\frac d{|p|}\le1$ : l'image est plus petite que l'objet (configuration d'un appareil photo).

**2. Principe.** $L$ ne bouge pas : elle donne toujours de $AB$ l'image $A_1B_1$, dans le plan de l'ancienne plaque. On intercale $L_1$ (centre $O_1$) entre $L$ et ce plan. Les rayons convergeant vers $A_1$ sont interceptés avant : $A_1$ est un **objet virtuel** pour $L_1$, avec $x=\overline{O_1A_1}>0$. $L_1$ en donne l'image finale $A'$, sur la nouvelle plaque.

**2. Grandissement.** Le grandissement total est $\gamma=\gamma_L\cdot\gamma_1$, où $\gamma_L$ est inchangé. Pour doubler $\gamma$, il faut $\gamma_1=\frac{\overline{O_1A'}}{\overline{O_1A_1}}=2$, donc $\overline{O_1A'}=2x$.

**2. Conjugaison par $L_1$.**
$$\frac1{\overline{O_1A'}}-\frac1{\overline{O_1A_1}}=\frac1{f_1'}\iff\frac1{2x}-\frac1x=\frac1{f_1'}\iff-\frac1{2x}=\frac1{f_1'}\iff x=-\frac{f_1'}2=3\ \mathrm{cm}.$$
$x>0$ est bien compatible avec un objet virtuel, et $\overline{O_1A'}=2x=6$ cm $>0$ : l'image finale est réelle et peut être recueillie sur la plaque.

**2. Conclusion.** On place $L_1$ **3 cm avant** l'ancienne position de la plaque (côté objectif). L'image finale est à 6 cm de $L_1$, c'est-à-dire 3 cm au-delà de l'ancienne position : la plaque est **reculée de 3 cm**. Ce dispositif (objectif convergent + divergent) est un **doubleur de focale** (téléconvertisseur) : il double la taille de l'image, comme un objectif de focale double, pour un encombrement modeste.
"""

D['p-opt-3'] = r"""
**1. Réglage à l'infini.** Un œil sans défaut qui n'accommode pas voit nettement les objets à l'infini (son punctum remotum est à l'infini). L'image finale $A'B'$ doit donc être à l'infini, et l'image intermédiaire $A_1B_1$, objet pour l'oculaire, doit être dans le plan focal objet de l'oculaire :
$$AB\xrightarrow{L_1}A_1B_1\xrightarrow{L_2}A'B'\ (\infty),\qquad A_1=F_2.$$

**2. Construction de deux rayons issus de $B$.**
- Le rayon issu de $B$ parallèle à l'axe émerge de $L_1$ en passant par $F_1'$, et atteint $B_1$.
- Le rayon issu de $B$ passant par $O_1$ n'est pas dévié, et atteint aussi $B_1$.

$B_1$ est dans le plan focal objet de $L_2$ : tous les rayons issus de $B_1$ émergent de $L_2$ parallèles entre eux, et parallèles au rayon $(B_1O_2)$, qui n'est pas dévié. Les deux rayons sortent donc parallèles à $(O_2B_1)$, sous l'angle $\alpha'$ avec l'axe.

**3. Position de $A_1$.** Formule de Descartes pour $L_1$, avec $\overline{O_1A}=-0{,}51$ cm :
$$\frac1{\overline{O_1A_1}}=\frac1{f_1'}+\frac1{\overline{O_1A}}=\frac1{0{,}5}-\frac1{0{,}51}=\frac{0{,}51-0{,}5}{0{,}5\times0{,}51}=\frac{0{,}01}{0{,}255}\ \mathrm{cm^{-1}},$$
donc $\overline{O_1A_1}=25{,}5$ cm.

**3. Grandissement.**
$$\gamma_1=\frac{\overline{O_1A_1}}{\overline{O_1A}}=\frac{25{,}5}{-0{,}51}=-50.$$
L'image intermédiaire est réelle, renversée et agrandie 50 fois. Formule générale : $\gamma_1=\frac{f_1'}{f_1'+\overline{O_1A}}$, car $\overline{O_1A_1}=\frac{f_1'\overline{O_1A}}{f_1'+\overline{O_1A}}$.

**4. Encombrement.** $A_1=F_2$, donc $\overline{A_1O_2}=\overline{F_2O_2}=f_2'=2$ cm. Par la relation de Chasles :
$$\overline{O_1O_2}=\overline{O_1A_1}+\overline{A_1O_2}=25{,}5+2=27{,}5\ \mathrm{cm}.$$

**5. Diamètre angulaire de l'image.** $|\overline{A_1B_1}|=|\gamma_1|\cdot AB=50\times0{,}01=0{,}5$ cm. Vu depuis $O_2$, à la distance $f_2'$ (rayon non dévié $B_1O_2$), dans l'approximation des petits angles :
$$\alpha'=\frac{|\overline{A_1B_1}|}{f_2'}=\frac{|\gamma_1|\,AB}{f_2'}=\frac{0{,}5}{2}=0{,}25\ \mathrm{rad}.$$

**6. Angle de référence.** À l'œil nu, l'objet est vu au mieux à la distance minimale de vision distincte $d_m=25$ cm :
$$\alpha_{\mathrm{ref}}=\frac{AB}{d_m}=\frac{0{,}01}{25}=4\times10^{-4}\ \mathrm{rad}.$$

**6. Grossissement.**
$$G=\frac{\alpha'}{\alpha_{\mathrm{ref}}}=\frac{0{,}25}{4\times10^{-4}}=625=|\gamma_1|\cdot\frac{d_m}{f_2'}=50\times12{,}5.$$
Le grossissement est le produit du grandissement de l'objectif ($\times50$) et du grossissement commercial de l'oculaire ($\frac{d_m}{f_2'}=12{,}5$), notations usuelles gravées sur les composants.
"""

D['p-opt-4'] = r"""
**1. Géométrie.** Soit $C$ le centre de la face sphérique, situé sur l'axe à la distance $R$ au-dessus de $O$. Un point de la face sphérique à distance $x$ de l'axe est à la hauteur $\varepsilon$ au-dessus du miroir. Dans le triangle rectangle formé par $C$, ce point et sa projection sur l'axe, le théorème de Pythagore donne
$$R^2=(R-\varepsilon)^2+x^2\iff2R\varepsilon-\varepsilon^2=x^2.$$
Comme $\varepsilon\ll R$ (car $x\ll R$), $\varepsilon^2\ll2R\varepsilon$, donc
$$\varepsilon\simeq\frac{x^2}{2R}.$$

**2. Rayons qui interfèrent.** En incidence normale, la lumière traverse la lentille. Une partie se réfléchit sur la face sphérique (dioptre verre → air, sans déphasage supplémentaire), et une autre traverse la lame d'air et se réfléchit sur le miroir (déphasage de $\pi$, soit $\frac{\lambda_0}2$). Les deux faisceaux interfèrent au voisinage de la face sphérique : on observe des franges d'égale épaisseur, localisées sur la lame.

**2. Différence de marche.** Le second rayon parcourt en plus un aller-retour dans l'air (indice 1) d'épaisseur $\varepsilon$ : $2\varepsilon$. Les rayons restent quasi normaux, car la face est peu inclinée pour $x\ll R$. D'où
$$\delta=2\varepsilon+\frac{\lambda_0}2=\frac{x^2}R+\frac{\lambda_0}2.$$

**3. Forme des franges.** $\delta$ ne dépend que de $x$, la distance à l'axe : les lignes d'égale intensité sont des **cercles** centrés en $O$.

**3. Centre.** En $x=0$, $\delta=\frac{\lambda_0}2$ : interférence destructive, le **centre est sombre**.

**3. Anneaux sombres.** $\delta=\big(m+\frac12\big)\lambda_0$, $m\in\mathbb N$, donne $\frac{x^2}R=m\lambda_0$, soit $x=\sqrt{m\lambda_0R}$. En comptant le centre comme premier anneau sombre ($m=0$), le $n$-ième anneau sombre a pour rayon
$$r_n^{\mathrm{sombre}}=\sqrt{(n-1)\lambda_0R}.$$

**3. Anneaux brillants.** $\delta=m\lambda_0$, $m\ge1$, donne $\frac{x^2}R=\big(m-\frac12\big)\lambda_0$. Le $n$-ième anneau brillant ($m=n$) a pour rayon
$$r_n^{\mathrm{brillant}}=\sqrt{\Big(n-\frac12\Big)\lambda_0R}.$$

**3. Remarque.** Les rayons croissent comme $\sqrt n$ : les anneaux se resserrent en s'éloignant du centre. La mesure des rayons permet de déterminer $R$ (ou $\lambda_0$) : par exemple, $r_{n+k}^2-r_n^2=k\lambda_0R$ ne dépend pas de l'origine du comptage.

**4. Lumière blanche.** Au centre, $\delta=\frac{\lambda_0}2$ pour toutes les longueurs d'onde : le centre est **noir**. Près du centre, les rayons des anneaux dépendent de $\lambda_0$ ($r\propto\sqrt{\lambda_0}$) : les anneaux des différentes couleurs sont décalés, et l'on voit quelques anneaux **irisés** (teintes de Newton). Plus loin, $\delta$ devient grand devant la longueur de cohérence : les systèmes se brouillent complètement, et l'on observe du **blanc d'ordre supérieur** (un spectroscope y révélerait un spectre cannelé).
"""

D['p-opt-5'] = r"""
**1. Phénomène.** C'est la **diffraction**. Chaque fente, de largeur comparable à $\lambda_0$, se comporte comme une source secondaire qui diffracte la lumière dans un large cône (principe de Huygens-Fresnel). Les $N$ ondes diffractées, cohérentes car issues de la même onde incidente, **interfèrent** dans chaque direction $\alpha$.

**2. Différence de marche.** On considère deux rayons parallèles passant par deux fentes consécutives, distantes de $a$.
- **À l'arrivée**, le rayon passant par la fente suivante a une avance de chemin $a\sin i$ avant le réseau (onde plane incidente, plans d'onde perpendiculaires aux rayons).
- **À la sortie**, il a un retard $a\sin\alpha$ après le réseau (direction d'observation à l'infini).

D'où, avec les angles orientés dans le même sens :
$$\delta=a(\sin\alpha-\sin i),\qquad\varphi=\frac{2\pi}{\lambda_0}\delta=\frac{2\pi a}{\lambda_0}(\sin\alpha-\sin i).$$

**3. Somme des $N$ ondes.** Les amplitudes forment une suite géométrique de raison $e^{i\varphi}$ :
$$\underline s=s_0\sum_{k=0}^{N-1}e^{ik\varphi}=s_0\frac{1-e^{iN\varphi}}{1-e^{i\varphi}},\qquad I=|\underline s|^2=I_0\frac{\sin^2(N\varphi/2)}{\sin^2(\varphi/2)}.$$
$I$ est maximale, égale à $N^2I_0$, quand $\varphi\in2\pi\mathbb Z$ (toutes les ondes en phase). Ailleurs, elle est très faible pour $N$ grand : on obtient des pics fins, de largeur angulaire de l'ordre de $\frac{2\pi}N$ en $\varphi$.

**3. Formule des réseaux.** $\varphi=2\pi p$ s'écrit
$$\sin\alpha_p-\sin i=p\,\frac{\lambda_0}a,\qquad p\in\mathbb Z\ (\text{ordre}).$$

**4. Nombre de pics.** Pour $i=0$, $\sin\alpha_p=p\frac{\lambda_0}a=p\times\frac{0{,}620}{3{,}0}=0{,}207\,p$. Il faut $|\sin\alpha_p|\le1$, soit $|p|\le\frac1{0{,}207}=4{,}84$, donc $|p|\le4$. On observe **9 pics** ($p=-4,\dots,4$), symétriques par rapport à l'ordre 0 ($\alpha_0=0$, lumière non déviée). Le pic d'ordre 4 est à $\alpha_4=\arcsin(0{,}827)\approx56^\circ$.

**5. Déviation en fonction de $i$.** À $p$ fixé, on différentie la formule des réseaux : $\cos\alpha_p\,\mathrm d\alpha_p=\cos i\,\mathrm di$. Donc
$$\frac{\mathrm dD_p}{\mathrm di}=1-\frac{\mathrm d\alpha_p}{\mathrm di}=1-\frac{\cos i}{\cos\alpha_p}.$$

**5. Extremum.** Il est atteint quand $\cos\alpha_p=\cos i$, soit $\alpha_p=\pm i$. La solution $\alpha_p=i$ donne $\sin\alpha_p-\sin i=0$, c'est-à-dire $p=0$ (déviation nulle). Pour $p\neq0$, il reste $\alpha_p=-i$ : la situation est symétrique, les rayons incident et diffracté étant symétriques par rapport à la normale. On vérifie qu'il s'agit d'un minimum de $|D_p|$ (la dérivée change de signe). Alors $D_p^*=i-(-i)=2i$ et la formule des réseaux donne $-2\sin i=p\frac{\lambda_0}a$, d'où
$$\lambda_0=\frac{2a}{|p|}\Big|\sin\frac{D_p^*}2\Big|.$$

**6. Précision du spectroscope.**
- Pour $p\neq0$, $\alpha_p$ dépend de $\lambda_0$ : le réseau **disperse** la lumière, et chaque raie donne son propre pic.
- Les pics sont **très fins** pour $N$ grand ($N\sim10^4$) : le pouvoir de résolution vaut $\frac\lambda{\Delta\lambda}=|p|N$.
- Au minimum de déviation, $D_p$ est stationnaire : une petite erreur de réglage sur $i$ n'affecte pas la mesure au premier ordre, et ce minimum se repère facilement au goniomètre.
- La formule ne fait intervenir que $a$ (connu avec précision) et un angle mesuré à la minute d'arc près.

On obtient $\lambda_0$ avec une précision relative de l'ordre de $10^{-4}$.
"""
