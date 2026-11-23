D = {}

D['n-p1-fente'] = r"""
**1. Position des premières annulations.** On découpe la fente en deux moitiés. Dans la direction $\theta$ telle que $a\sin\theta=\lambda$, chaque point de la première moitié a un correspondant dans la seconde (décalé de $\frac a2$) avec une différence de marche $\frac a2\sin\theta=\frac\lambda2$ : les ondes s'annulent deux à deux et l'intensité est nulle. La tache centrale est donc limitée par
$$\sin\theta=\frac\lambda a,\qquad\theta\approx\frac\lambda a\quad(a\gg\lambda).$$

**1. Largeur sur l'écran.** Pour de petits angles, la tache centrale s'étend de $-D\theta$ à $+D\theta$ sur l'écran (à la distance $D\gg a$) :
$$\ell\approx2D\tan\theta\approx\frac{2\lambda D}a.$$

**2. Application numérique.**
$$\ell=\frac{2\times633\times10^{-9}\times2{,}0}{1{,}0\times10^{-4}}=\frac{2{,}53\times10^{-6}}{10^{-4}}\approx2{,}5\times10^{-2}\ \mathrm m=2{,}5\ \mathrm{cm}.$$
On a bien $\theta\approx6{,}3\times10^{-3}$ rad $\ll1$.

**3. Mesure d'une largeur.** On inverse la relation :
$$a=\frac{2\lambda D}\ell=\frac{2{,}53\times10^{-6}}{1{,}3\times10^{-2}}\approx1{,}9\times10^{-4}\ \mathrm m=0{,}19\ \mathrm{mm}.$$
La fente est environ deux fois plus large que la première, et la tache environ deux fois plus étroite : $\ell\propto\frac1a$. Cette méthode permet de mesurer l'épaisseur d'un cheveu (théorème de Babinet : un obstacle donne la même figure qu'une fente de même largeur).

**4. Cas d'une fenêtre.** Pour $a\sim1$ m, $\theta\sim\frac\lambda a\sim6\times10^{-7}$ rad. L'élargissement sur un mur à quelques mètres est inférieur au micromètre : imperceptible. La diffraction n'est notable que pour des ouvertures de quelques dizaines à quelques centaines de longueurs d'onde au plus. Dans tous les autres cas, la lumière se propage en ligne droite : c'est le domaine de validité de l'optique géométrique.
"""

D['n-p1-projecteur'] = r"""
**1. Relation de conjugaison.** L'écran est à $\overline{OA'}=+3{,}0$ m (image réelle). La formule de Descartes, $\frac1{\overline{OA'}}-\frac1{\overline{OA}}=\frac1{f'}$, donne
$$\frac1{\overline{OA}}=\frac1{\overline{OA'}}-\frac1{f'}=\frac1{3{,}0}-\frac1{0{,}10}=0{,}333-10=-9{,}67\ \mathrm{m^{-1}},$$
donc $\overline{OA}\approx-0{,}103$ m $=-10{,}3$ cm.

**1. Interprétation.** La diapositive est placée juste avant le foyer objet ($-10$ cm), à 3 mm de lui : pour une image lointaine, l'objet est presque au foyer.

**1. Sens.** Une lentille convergente donne d'un objet réel une image réelle **renversée**, comme on va le vérifier. Pour que l'image soit à l'endroit sur l'écran, on place la diapositive à l'envers (tête en bas, et inversée gauche-droite).

**2. Grandissement.**
$$\gamma=\frac{\overline{OA'}}{\overline{OA}}=\frac{3{,}0}{-0{,}1034}\approx-29.$$
L'image est renversée et agrandie 29 fois.

**2. Dimensions de l'image.** $24\ \mathrm{mm}\times29\approx0{,}70$ m et $36\ \mathrm{mm}\times29\approx1{,}04$ m, d'où une image d'environ $0{,}70\times1{,}04\ \mathrm m$.

**3. Condition $D\ge4f'$.** Soit $D$ la distance objet-écran. Avec $p=\overline{OA}<0$ (objet réel) et $p'=\overline{OA'}=p+D>0$ (image réelle sur l'écran) :
$$\frac1{p+D}-\frac1p=\frac1{f'}\iff\frac{-D}{p(p+D)}=\frac1{f'}\iff p^2+Dp+Df'=0.$$
Cette équation du second degré en $p$ a des solutions réelles si et seulement si son discriminant est positif :
$$\Delta=D^2-4Df'=D(D-4f')\ge0\iff D\ge4f'.$$

**3. Commentaire.** Pour $D>4f'$, il y a deux positions de la lentille qui donnent une image nette (les deux racines, dont le produit vaut $Df'$). Pour $D=4f'$, il y a une racine double $p=-\frac D2=-2f'$, avec $p'=2f'$ et $\gamma=-1$ : c'est la configuration objet-image réelle la plus courte. Ici, $D=3{,}10\ \mathrm m\gg4f'=0{,}40$ m.
"""

D['n-p1-lunette'] = r"""
**1. Afocalité.** L'objet (un astre) est à l'infini. L'œil normal observe sans fatigue, sans accommoder, une image à l'infini. Le système doit donc transformer un faisceau parallèle en un faisceau parallèle : il est **afocal**. Pour deux lentilles, cela impose que le foyer image de l'objectif coïncide avec le foyer objet de l'oculaire : $F_1'=F_2$.

**1. Longueur.**
$$\overline{O_1O_2}=\overline{O_1F_1'}+\overline{F_2O_2}=f_1'+f_2'=1{,}00+0{,}05=1{,}05\ \mathrm m.$$

**2. Image intermédiaire.** Un astre vu sous l'angle $\alpha$ a, par l'objectif, une image $A'B'$ dans le plan focal image $F_1'$. Le rayon passant par $O_1$ n'est pas dévié, d'où (petits angles) $\overline{A'B'}\approx f_1'\alpha$, avec $\alpha$ orienté.

**2. Image finale.** $A'B'$ est dans le plan focal objet de l'oculaire, qui en donne une image à l'infini. Le rayon $B'O_2$ n'est pas dévié : l'angle de sortie vaut $\alpha'\approx-\frac{\overline{A'B'}}{f_2'}$. Le signe $-$ vient de l'orientation : $B'$ est de l'autre côté de l'axe.

**2. Grossissement.**
$$G=\frac{\alpha'}\alpha=-\frac{f_1'\alpha/f_2'}\alpha=-\frac{f_1'}{f_2'}=-\frac{1{,}00}{0{,}05}=-20.$$
Le signe $-$ signifie que l'image est renversée, ce qui ne gêne pas en astronomie.

**2. Application à la Lune.** $|\alpha'|=20\times0{,}50^\circ=10^\circ$ : la Lune paraît vingt fois plus grande.

**3. Cercle oculaire : position.** C'est l'image de la monture de l'objectif (centre $O_1$) par l'oculaire. Avec $\overline{O_2O_1}=-1{,}05$ m :
$$\frac1{\overline{O_2C}}=\frac1{f_2'}+\frac1{\overline{O_2O_1}}=\frac1{0{,}05}-\frac1{1{,}05}=20-0{,}952=19{,}05\ \mathrm{m^{-1}},$$
donc $\overline{O_2C}\approx5{,}25$ cm. Le cercle oculaire est réel, situé juste après le foyer image de l'oculaire (à 2,5 mm de lui).

**3. Cercle oculaire : diamètre.** Le grandissement vaut $\gamma=\frac{\overline{O_2C}}{\overline{O_2O_1}}=\frac{0{,}0525}{-1{,}05}=-0{,}050$, donc le diamètre est $d=|\gamma|D_1=0{,}050\times10\ \mathrm{cm}=0{,}50$ cm $=5$ mm. On vérifie que $\frac{D_1}d=20=|G|$ : c'est une propriété générale des systèmes afocaux.

**3. Intérêt.** Tous les rayons entrés par l'objectif (quelle que soit leur inclinaison) passent par le cercle oculaire, qui est l'image de la monture. En y plaçant la pupille de l'œil (environ 5 mm la nuit, soit justement le diamètre du cercle oculaire), on recueille toute la lumière collectée et on voit le champ le plus large.
"""

D['n-p1-prisme'] = r"""
**1. Lois de Descartes.** À l'entrée (air → verre), sur la première face : $\sin i=n\sin r$. À la sortie (verre → air), sur la seconde face : $n\sin r'=\sin i'$. Les angles sont mesurés par rapport aux normales aux faces.

**1. Relation $r+r'=A$.** Les normales aux deux faces se coupent en un point $N$ et font entre elles l'angle $\pi-A$ (dans le quadrilatère formé par le sommet, les deux points d'incidence et $N$, les deux angles aux points d'incidence sont droits). Le rayon intérieur forme avec les deux normales un triangle dont les angles valent $r$, $r'$ et $\pi-A$. La somme des angles d'un triangle valant $\pi$ :
$$r+r'+(\pi-A)=\pi\iff r+r'=A.$$

**1. Déviation.** Le rayon est dévié de $i-r$ à l'entrée, puis de $i'-r'$ à la sortie, dans le même sens (vers la base). La déviation totale vaut
$$D=(i-r)+(i'-r')=i+i'-(r+r')=i+i'-A.$$

**2. Minimum de déviation.** Au minimum, le trajet est symétrique : $i=i'$, donc $r=r'$. Avec $r+r'=A$, on obtient $r=\frac A2$, puis $D_m=2i-A$, soit $i=\frac{A+D_m}2$. La relation $\sin i=n\sin r$ donne
$$n=\frac{\sin\frac{A+D_m}2}{\sin\frac A2}.$$

**2. Application numérique.** $\sin\frac{A+D_m}2=n\sin\frac A2=1{,}50\times\sin30^\circ=0{,}75$, donc $\frac{A+D_m}2=\arcsin0{,}75=48{,}6^\circ$ et
$$D_m=2\times48{,}6^\circ-60^\circ\approx37{,}2^\circ.$$
Intérêt : $D_m$ se repère facilement au goniomètre (la déviation y est stationnaire), et sa mesure donne $n$ avec précision, ainsi que sa dépendance en $\lambda$ (dispersion).

**3. Angle limite.** Le rayon ne peut émerger que si $\sin i'=n\sin r'\le1$, c'est-à-dire $r'\le\ell=\arcsin\frac1n=\arcsin0{,}667=41{,}8^\circ$. Sinon, il subit une réflexion totale sur la seconde face.

**3. Condition sur $A$.** À l'entrée, $\sin r=\frac{\sin i}n\le\frac1n$, donc $r\le\ell$ (au mieux en incidence rasante). Avec $r+r'=A$ et $r,r'\le\ell$ :
$$A\le2\ell=2\arcsin\frac1n=83{,}6^\circ.$$
Si $A>83{,}6^\circ$, aucun rayon n'émerge.

**3. Cas $A=60^\circ$.** L'émergence est possible, mais il faut $r'=A-r\le\ell$, soit $r\ge A-\ell=18{,}2^\circ$, donc
$$i\ge\arcsin\big(1{,}50\times\sin18{,}2^\circ\big)=\arcsin(0{,}468)\approx27{,}9^\circ.$$
"""

D['n-p1-photo'] = r"""
**1. Seuil photoélectrique.** Un photon de longueur d'onde $\lambda$ a l'énergie $E=\frac{hc}\lambda$. Il arrache un électron si $E\ge W$, d'où la longueur d'onde seuil (la plus grande qui convient) :
$$\lambda_0=\frac{hc}W=\frac{1240\ \mathrm{eV\,nm}}{4{,}3\ \mathrm{eV}}\approx288\ \mathrm{nm}.$$
C'est dans l'**ultraviolet** ($\lambda<400$ nm).

**2. Énergie du photon.** $E=\frac{1240}{254}\approx4{,}88$ eV $>W$ : l'effet photoélectrique a lieu.

**2. Énergie cinétique maximale.** L'électron le moins lié reçoit l'énergie du photon, en dépense $W$ pour sortir du métal, et garde le reste (relation d'Einstein) :
$$E_{c,\max}=\frac{hc}\lambda-W=4{,}88-4{,}3\approx0{,}58\ \mathrm{eV}=0{,}58\times1{,}60\times10^{-19}\approx9{,}3\times10^{-20}\ \mathrm J.$$

**2. Vitesse maximale.** $E_c\ll m_ec^2=511$ keV : le calcul non relativiste convient.
$$v_{\max}=\sqrt{\frac{2E_{c,\max}}{m_e}}=\sqrt{\frac{2\times9{,}3\times10^{-20}}{9{,}11\times10^{-31}}}=\sqrt{2{,}04\times10^{11}}\approx4{,}5\times10^5\ \mathrm{m\,s^{-1}}.$$

**2. Potentiel d'arrêt.** C'est la tension $U_0$ à appliquer pour que même les électrons les plus rapides n'atteignent pas l'anode. Par le théorème de l'énergie cinétique, $eU_0=E_{c,\max}$, donc
$$U_0=\frac{E_{c,\max}}e\approx0{,}58\ \mathrm V.$$

**3. Lampe visible.** Un photon visible ($\lambda>400$ nm) transporte au plus $\frac{1240}{400}=3{,}1$ eV $<W=4{,}3$ eV : aucun photon n'a assez d'énergie pour arracher un électron. Augmenter la puissance de la lampe augmente le nombre de photons, mais pas l'énergie de chacun. L'absorption de plusieurs photons par un même électron est extrêmement improbable aux intensités usuelles.

**3. Contradiction avec la théorie classique.** Dans le modèle ondulatoire classique, l'énergie de l'onde est répartie continûment et proportionnelle à l'intensité : une onde assez intense, ou appliquée assez longtemps, devrait finir par fournir l'énergie $W$, quelle que soit sa fréquence. L'existence d'un seuil en fréquence, indépendant de l'intensité, et l'émission instantanée au-dessus du seuil imposent que la lumière échange son énergie par **quanta** $h\nu$ : ce sont les photons (Einstein, 1905).
"""

D['n-p1-debroglie'] = r"""
**0. Relation de de Broglie.** $\lambda=\frac hp$. Dans le cadre non relativiste, $E_c=\frac{p^2}{2m}$, donc $p=\sqrt{2mE_c}$ et $\lambda=\frac h{\sqrt{2mE_c}}$.

**1. Électron accéléré.** Par le théorème de l'énergie cinétique (partant du repos), $E_c=eU=100$ eV $=1{,}60\times10^{-17}$ J. Comme $eU\ll m_ec^2=511$ keV, l'approche non relativiste est justifiée.
$$\lambda=\frac h{\sqrt{2m_eeU}}=\frac{6{,}63\times10^{-34}}{\sqrt{2\times9{,}11\times10^{-31}\times1{,}60\times10^{-17}}}=\frac{6{,}63\times10^{-34}}{5{,}40\times10^{-24}}\approx1{,}2\times10^{-10}\ \mathrm m.$$

**1. Intérêt pour un cristal.** $\lambda\approx0{,}12$ nm est de l'ordre des distances interatomiques ($0{,}1$ à $0{,}5$ nm). Un cristal, réseau périodique d'atomes, se comporte comme un réseau de diffraction pour ces ondes : on observe des figures de diffraction électronique (Davisson et Germer, 1927), qui révèlent la structure du cristal.

**2. Neutron thermique.** $E_c=k_BT=1{,}38\times10^{-23}\times300=4{,}14\times10^{-21}$ J (environ 26 meV).
$$\lambda=\frac h{\sqrt{2m_nk_BT}}=\frac{6{,}63\times10^{-34}}{\sqrt{2\times1{,}67\times10^{-27}\times4{,}14\times10^{-21}}}=\frac{6{,}63\times10^{-34}}{3{,}72\times10^{-24}}\approx1{,}8\times10^{-10}\ \mathrm m.$$
On retrouve le même ordre de grandeur : les neutrons thermiques sont diffractés par les cristaux. Comme ils sont neutres, ils pénètrent profondément ; ils interagissent avec les noyaux (et non avec les électrons) et sont sensibles au magnétisme, ce qui complète la diffraction des rayons X.

**3. Balle de tennis.**
$$\lambda=\frac h{mv}=\frac{6{,}63\times10^{-34}}{0{,}058\times50}=\frac{6{,}63\times10^{-34}}{2{,}9}\approx2\times10^{-34}\ \mathrm m.$$
C'est $10^{19}$ fois plus petit qu'un noyau atomique : aucune ouverture ni aucun obstacle ne permet d'observer une diffraction.

**Conclusion.** Les effets ondulatoires de la matière ne sont observables que pour des particules de très faible quantité de mouvement (électrons, neutrons, atomes froids). Pour les objets macroscopiques, $\lambda$ est infime, et la mécanique classique s'applique parfaitement.
"""
