D = {}

D['p-meca-ccmp2'] = r"""
**1. Données.** Le bloc a une section $S$ (horizontale), une épaisseur $e$ et une masse $m=\rho_bSe$. L'eau de mer contient 35 g de sel par litre, d'où une masse volumique $\rho_e\approx1025\ \mathrm{kg\,m^{-3}}$ (valeur usuelle de l'eau de mer).

**1. Équilibre.** Le bloc est enfoncé d'une hauteur $h_0$ : la poussée d'Archimède compense le poids, $\rho_eSh_0g=\rho_bSeg$, donc $h_0=\frac{\rho_b}{\rho_e}e$.

**1. Équation du mouvement.** On note $z$ l'enfoncement supplémentaire, compté vers le bas, et on suppose que le bloc ne s'immerge pas totalement. La poussée devient $\rho_eS(h_0+z)g$, d'où, en projection sur la verticale descendante :
$$\rho_bSe\,\ddot z=\rho_bSeg-\rho_eS(h_0+z)g=-\rho_eSg\,z.$$
C'est un oscillateur harmonique, de pulsation
$$\omega^2=\frac{\rho_eg}{\rho_be}.$$

**1. Masse volumique du bois.** Avec $\omega=\frac{2\pi}T$ :
$$\rho_b=\frac{\rho_egT^2}{4\pi^2e}=\frac{1025\times9{,}81\times1^2}{4\pi^2\times0{,}30}=\frac{1{,}006\times10^4}{11{,}84}\approx850\ \mathrm{kg\,m^{-3}}.$$
**Oui**, on peut la déterminer : c'est un bois dense (type chêne). On vérifie que $\rho_b<\rho_e$ (il flotte), et $h_0\approx0{,}83e\approx25$ cm.

**1. Limite du modèle.** On a négligé la « masse ajoutée », c'est-à-dire l'eau mise en mouvement avec le bloc, qui augmente l'inertie effective. La période réelle est donc un peu plus longue que celle du modèle, et la valeur calculée de $\rho_b$ est légèrement surestimée.

**2. Origine de l'amortissement.** Le bloc dissipe son énergie par la viscosité de l'eau, et surtout par l'**émission de vagues** à la surface, qui emportent de l'énergie vers l'extérieur.

**2. Modélisation.** On ajoute un frottement fluide $-\alpha\dot z$ : $\ddot z+\frac2\tau\dot z+\omega_0^2z=0$. En régime pseudo-périodique faiblement amorti, $z=z_0e^{-t/\tau}\cos(\Omega t+\varphi)$. Le rapport de deux amplitudes séparées d'une période vaut $e^{-T/\tau}$ :
$$e^{-T/\tau}=0{,}90\iff\frac T\tau=\ln\frac1{0{,}90}=0{,}105\iff\tau=\frac{1\ \mathrm s}{0{,}105}\approx9{,}5\ \mathrm s.$$
$\delta=\frac T\tau=0{,}105$ est le décrément logarithmique.

**2. Facteur de qualité.** $Q=\frac{\omega_0\tau}2=\frac{\pi\tau}T=\frac\pi\delta\approx\frac{3{,}14}{0{,}105}\approx30$. L'amortissement est faible : la pseudo-période diffère de la période propre d'un facteur $\sqrt{1-\frac1{4Q^2}}\approx1-1{,}4\times10^{-4}$, ce qui justifie l'utilisation de $T=1$ s à la question 1.
"""

D['p-meca-ccmp13'] = r"""
**1. Vitesse de satellisation.** Pour un mouvement circulaire uniforme de rayon $R_T$, l'accélération est centripète, de norme $\frac{v_s^2}{R_T}$, et la seule force est l'attraction terrestre. Le principe fondamental donne
$$m\frac{v_s^2}{R_T}=\frac{GM_Tm}{R_T^2}=mg_0\quad\Longrightarrow\quad v_s=\sqrt{g_0R_T}.$$
Avec $R_T=6{,}4\times10^6$ m : $v_s=\sqrt{10\times6{,}4\times10^6}=\sqrt{6{,}4\times10^7}=8{,}0\times10^3\ \mathrm{m\,s^{-1}}$.

**2. Orbite de rayon $5R_T$.** De même, $\frac{v_1^2}{5R_T}=\frac{GM_T}{25R_T^2}$, soit $v_1^2=\frac{GM_T}{5R_T}=\frac{g_0R_T}5$, donc
$$v_1=\frac{v_s}{\sqrt5}=\frac{8{,}0}{2{,}24}\approx3{,}6\ \mathrm{km\,s^{-1}}.$$

**3.(a) Manœuvre.** On freine brièvement le satellite au point $A$ ($r_a=5R_T$), avec une poussée opposée à la vitesse, ce qui garde la vitesse tangentielle. La nouvelle trajectoire est une ellipse de foyer $O$ (centre de la Terre), d'apogée $A$, et de périgée $P$ diamétralement opposé, à $r_p=R_T+h\approx6{,}5\times10^6$ m (tangente à la haute atmosphère). Le grand axe vaut $r_a+r_p$.

**3.(b) Lois de conservation.** Entre $A$ et $P$, où la vitesse est orthogonale au rayon :
- **moment cinétique** (force centrale) : $r_av_2=r_pv_3$ ;
- **énergie mécanique** (force conservative) : $\frac12v_2^2-\frac{GM_T}{r_a}=\frac12v_3^2-\frac{GM_T}{r_p}$.

**3.(b) Calcul de $v_2$.** En reportant $v_3=v_2\frac{r_a}{r_p}$ dans l'énergie :
$$v_2^2\Big(1-\frac{r_a^2}{r_p^2}\Big)=2GM_T\Big(\frac1{r_a}-\frac1{r_p}\Big)\iff v_2^2\,\frac{(r_p-r_a)(r_p+r_a)}{r_p^2}=2GM_T\frac{r_p-r_a}{r_ar_p},$$
donc
$$v_2=\sqrt{\frac{2GM_T\,r_p}{r_a(r_a+r_p)}}.$$

**3.(b) Application numérique.** $GM_T=g_0R_T^2=10\times(6{,}4\times10^6)^2=4{,}1\times10^{14}\ \mathrm{m^3\,s^{-2}}$, $r_a=3{,}2\times10^7$ m et $r_a+r_p=3{,}85\times10^7$ m :
$$v_2=\sqrt{\frac{2\times4{,}1\times10^{14}\times6{,}5\times10^6}{3{,}2\times10^7\times3{,}85\times10^7}}=\sqrt{4{,}3\times10^6}\approx2{,}1\ \mathrm{km\,s^{-1}}.$$
Il faut donc réduire la vitesse de $\Delta v=v_1-v_2\approx1{,}5\ \mathrm{km\,s^{-1}}$.

**3.(c) Vitesse d'entrée dans l'atmosphère.**
$$v_3=v_2\frac{r_a}{r_p}=2{,}08\times\frac{3{,}2\times10^7}{6{,}5\times10^6}=2{,}08\times4{,}92\approx10{,}2\ \mathrm{km\,s^{-1}}.$$
Vérification par l'énergie : $v_3^2=v_2^2+2GM_T\big(\frac1{r_p}-\frac1{r_a}\big)=4{,}3\times10^6+8{,}2\times10^{14}\times(1{,}54-0{,}31)\times10^{-7}\approx1{,}05\times10^8$, soit $v_3\approx10{,}2\ \mathrm{km\,s^{-1}}$. ✓ Cette énorme énergie cinétique (environ $5\times10^7$ J par kg) est dissipée en chaleur par le frottement atmosphérique : le satellite se consume.
"""

D['p-meca-ccs1'] = r"""
**Notation.** $d=SJ$ (distance Soleil-Jupiter, constante), $M=M_S+M_J$.

**1. Position de $G$.** Par définition du barycentre, $M_S\overrightarrow{GS}+M_J\overrightarrow{GJ}=\vec0$. Donc $G\in[SJ]$, avec
$$GS=\frac{M_J}{M_S+M_J}d,\qquad GJ=\frac{M_S}{M_S+M_J}d.$$
Si $M_J\ll M_S$, $GS\approx\frac{M_J}{M_S}d\ll d$ : $G$ est pratiquement au centre du Soleil, qui est quasi immobile. En réalité, $\frac{M_J}{M_S}\approx9{,}5\times10^{-4}$ et $d\approx7{,}8\times10^{11}$ m donnent $GS\approx7{,}4\times10^8$ m $\approx1{,}07R_S$ : $G$ est juste à l'extérieur du Soleil, qui « danse » légèrement (méthode de détection des exoplanètes par les vitesses radiales).

**2.(a) Approximation $M_J\ll M_S$.** Le Soleil est fixe en $G$ et Jupiter décrit un cercle de rayon $d$ à la vitesse angulaire $\omega$. Le principe fondamental appliqué à Jupiter, projeté sur la normale, donne
$$M_J\omega^2d=\frac{GM_SM_J}{d^2}\quad\Longrightarrow\quad\omega^2=\frac{GM_S}{d^3}.$$

**2.(b) Troisième loi de Kepler.** Avec $T=\frac{2\pi}\omega$ : $T^2=\frac{4\pi^2}{\omega^2}=\frac{4\pi^2d^3}{GM_S}$, donc
$$\frac{T^2}{d^3}=\frac{4\pi^2}{GM_S}.$$
Ce rapport est le même pour toutes les planètes du système solaire (dans cette approximation) : c'est la troisième loi de Kepler (énoncée ici pour des orbites circulaires).

**2.(c) Sans approximation.** Dans le référentiel barycentrique (galiléen), $S$ et $J$ tournent autour de $G$ à la même vitesse angulaire $\omega$. Jupiter décrit un cercle de rayon $GJ=\frac{M_S}{M}d$, et subit toujours la force $\frac{GM_SM_J}{d^2}$ (la distance $SJ$ vaut toujours $d$) :
$$M_J\omega^2\frac{M_S}Md=\frac{GM_SM_J}{d^2}\quad\Longrightarrow\quad\omega^2=\frac{G(M_S+M_J)}{d^3}.$$
On retrouve 2(a) si $M_J\ll M_S$. La correction relative sur $T$ vaut environ $\frac{M_J}{2M_S}\approx5\times10^{-4}$.

**3. Forces dans le référentiel tournant.** Ce référentiel a pour origine $G$ et tourne à $\omega$ ; $S$ et $J$ y sont fixes. Le point $M$ (de masse $m$, sans influence sur $S$ et $J$) subit :
- les attractions de $S$ et $J$ ;
- la force d'inertie d'entraînement (centrifuge) $m\omega^2\overrightarrow{GM}$, à condition que $M$ soit dans le plan de l'orbite (sinon, il faut prendre la projection sur ce plan) ;
- la force de Coriolis, nulle à l'équilibre ($\vec v=\vec0$).

**3. Condition d'équilibre.**
$$-\frac{GM_S}{SM^3}\overrightarrow{SM}-\frac{GM_J}{JM^3}\overrightarrow{JM}+\omega^2\overrightarrow{GM}=\vec0,\qquad\omega^2=\frac{G(M_S+M_J)}{d^3}.$$

**3. Solutions : les cinq points de Lagrange.**
- Trois points $L_1$, $L_2$, $L_3$ sur la droite $(SJ)$. Ils sont obtenus en résolvant une équation scalaire, et sont **instables**.
- Deux points $L_4$, $L_5$ formant avec $S$ et $J$ des **triangles équilatéraux** de côté $d$. On le vérifie : si $SM=JM=d$, la somme des attractions vaut $-\frac G{d^3}\big(M_S\overrightarrow{SM}+M_J\overrightarrow{JM}\big)=-\frac{GM}{d^3}\overrightarrow{GM}$ par définition de $G$, ce qui compense exactement la force centrifuge $\omega^2\overrightarrow{GM}$.

$L_4$ et $L_5$ sont stables (grâce à la force de Coriolis) lorsque $\frac{M_J}{M_S}<0{,}04$, ce qui est le cas. On y observe les astéroïdes **troyens** de Jupiter.
"""

D['p-meca-ccs3'] = r"""
**1. Théorème de Gauss gravitationnel.** La Terre, homogène, a une masse volumique $\rho=\frac{M_T}{\frac43\pi R_T^3}$. Par symétrie sphérique, $\vec g=g(r)\vec u_r$. Le flux de $\vec g$ à travers la sphère de rayon $r$ vaut $-4\pi G$ fois la masse intérieure :
$$4\pi r^2g(r)=-4\pi G\,\rho\frac43\pi r^3=-4\pi G\,M_T\frac{r^3}{R_T^3}.$$
D'où, pour $r<R_T$, avec $g_0=\frac{GM_T}{R_T^2}$ :
$$\vec g(r)=-\frac{GM_T}{R_T^3}r\,\vec u_r=-g_0\frac r{R_T}\vec u_r.$$
Le champ est proportionnel à la distance au centre : $\vec g=-\frac{g_0}{R_T}\overrightarrow{OM}$.

**2. Paramétrage.** Soit $H$ le pied de la perpendiculaire abaissée de $O$ sur le tunnel (le milieu de $AB$), et $x$ l'abscisse de la voiture sur $(AB)$, comptée depuis $H$. Alors $\overrightarrow{OM}=\overrightarrow{OH}+x\vec u$, où $\vec u$ est le vecteur directeur du tunnel, avec $\overrightarrow{OH}\perp\vec u$.

**2. Projection le long du tunnel.** La force de gravité vaut $m\vec g=-\frac{mg_0}{R_T}\big(\overrightarrow{OH}+x\vec u\big)$. Sa composante selon $\vec u$ est $-\frac{mg_0}{R_T}x$. La composante perpendiculaire est compensée par la réaction des parois, sans frottement, elle-même perpendiculaire au tunnel. Le principe fondamental, projeté sur $\vec u$, donne
$$m\ddot x=-\frac{mg_0}{R_T}x\iff\ddot x+\omega_0^2x=0,\qquad\omega_0=\sqrt{\frac{g_0}{R_T}}.$$

**2. Durée du trajet.** Lâchée sans vitesse en $A$ ($x=-\frac{AB}2$), la voiture oscille et atteint $B$ ($x=+\frac{AB}2$) au bout d'une demi-période :
$$\tau=\frac\pi{\omega_0}=\pi\sqrt{\frac{R_T}{g_0}}=\pi\sqrt{\frac{6{,}4\times10^6}{9{,}8}}=\pi\times808\approx2{,}54\times10^3\ \mathrm s\approx42\ \mathrm{min}.$$

**2. Commentaire.** Cette durée ne dépend **pas** du tunnel (ni de sa longueur, ni de sa position) : le trajet Paris-Sydney (passant près du centre) dure autant que Paris-Lyon. C'est aussi la demi-période d'un satellite en orbite rasante ($2\pi\sqrt{R_T/g_0}\approx84$ min), car la projection d'un mouvement circulaire uniforme est un mouvement harmonique. La vitesse maximale, atteinte en $H$, vaut $\omega_0\frac{AB}2$.

**3. Prise en compte de la rotation terrestre.** Dans le référentiel terrestre (non galiléen, $\vec\Omega$ selon l'axe des pôles), on ajoute la force d'entraînement $m\Omega^2\overrightarrow{KM}$, où $K$ est le projeté de $M$ sur l'axe, et la force de Coriolis $-2m\vec\Omega\wedge\vec v$.

**3.(a) Tunnel parallèle à l'axe des pôles.** La force d'entraînement est perpendiculaire à l'axe, donc au tunnel : sans effet sur le mouvement. La force de Coriolis est nulle, car $\vec v\parallel\vec\Omega$. Le mouvement est inchangé : $\tau\approx42$ min.

**3.(b) Tunnel orthogonal à l'axe** (situé dans un plan perpendiculaire à l'axe, par exemple dans le plan équatorial). Le projeté de $M$ sur l'axe est fixe, et l'on peut écrire $\overrightarrow{KM}=\overrightarrow{KH'}+x\vec u$, avec $\overrightarrow{KH'}\perp\vec u$. La force d'entraînement a donc une composante $+m\Omega^2x$ le long du tunnel, d'où
$$\ddot x+\Big(\frac{g_0}{R_T}-\Omega^2\Big)x=0.$$
La pulsation diminue un peu, et la durée augmente : la correction relative vaut $\frac{\Omega^2R_T}{2g_0}\approx\frac{3{,}5\times10^{-3}}2$, soit environ $+4$ s. La force de Coriolis, perpendiculaire à $\vec v$ et à $\vec\Omega$, est perpendiculaire au tunnel : elle plaque la voiture contre une paroi, sans effet sur le mouvement en l'absence de frottement.

**4. Avec frottements.** L'énergie mécanique décroît : la voiture n'atteint pas $B$. Elle fait des oscillations amorties autour de $H$ et finit par s'immobiliser en $H$, au point le plus profond du tunnel. Il faudrait un moteur pour compenser les pertes.
"""

D['p-meca-ccs-ressort'] = r"""
**1. Équations du mouvement.** On suppose $x_1<x_2$. Le ressort a pour longueur $X=x_2-x_1$ et pour allongement $X-l_0$. S'il est allongé ($X>l_0$), il tire $m_1$ vers $+\vec u_x$ et $m_2$ vers $-\vec u_x$. Dans un référentiel galiléen, sans autre force horizontale :
$$m_1\ddot x_1=+K(x_2-x_1-l_0),\qquad m_2\ddot x_2=-K(x_2-x_1-l_0).$$

**1. Équation en $X$.** On divise chaque équation par la masse correspondante, puis on soustrait :
$$\ddot X=\ddot x_2-\ddot x_1=-K\Big(\frac1{m_2}+\frac1{m_1}\Big)(X-l_0)=-\frac K\mu(X-l_0),\qquad\frac1\mu=\frac1{m_1}+\frac1{m_2}.$$
Soit
$$\mu\ddot X=-K(X-l_0),\qquad\mu=\frac{m_1m_2}{m_1+m_2},\qquad\omega_0=\sqrt{\frac K\mu}.$$
C'est un oscillateur harmonique de masse $\mu$ (masse réduite), toujours inférieure à $m_1$ et à $m_2$. Si $m_2\to\infty$ (mur fixe), $\mu\to m_1$.

**1. Centre de masse.** En additionnant les deux équations, $m_1\ddot x_1+m_2\ddot x_2=0$ : l'accélération du centre de masse est nulle, il est en mouvement rectiligne uniforme (système isolé).

**2.(a) Vitesses dans le référentiel du centre de masse.** On a $m_1x_1+m_2x_2=\text{cste}$ (centre de masse immobile) et $x_2-x_1=X$. On en déduit $\dot x_1=-\frac{m_2}{m_1+m_2}\dot X$ et $\dot x_2=\frac{m_1}{m_1+m_2}\dot X$.

**2.(a) Énergie cinétique.**
$$E_c=\frac12m_1\dot x_1^2+\frac12m_2\dot x_2^2=\frac12\cdot\frac{m_1m_2^2+m_2m_1^2}{(m_1+m_2)^2}\dot X^2=\frac12\cdot\frac{m_1m_2}{m_1+m_2}\dot X^2=\frac12\mu\dot X^2.$$

**2.(a) Énergie potentielle et énergie mécanique.** L'énergie potentielle élastique du ressort est $E_p=\frac12K(X-l_0)^2$, d'où
$$E_m=\frac12\mu\dot X^2+\frac12K(X-l_0)^2=\text{cste}.$$
Elle est constante, car les forces intérieures sont conservatives et il n'y a pas de force extérieure. En dérivant, on retrouve $\mu\ddot X=-K(X-l_0)$. Le problème à deux corps se ramène à celui d'une particule fictive de masse $\mu$.

**2.(b) Rayonnement.** Si les deux masses portent des charges opposées $\pm q$ (modèle d'une molécule diatomique polaire, par exemple HCl), le moment dipolaire $p=qX$ oscille à la pulsation $\omega_0$. Un dipôle oscillant rayonne une onde électromagnétique de même fréquence :
$$f_0=\frac{\omega_0}{2\pi}=\frac1{2\pi}\sqrt{\frac K\mu}.$$
Pour une liaison chimique, $f_0\sim10^{13}$–$10^{14}$ Hz : c'est le domaine de l'**infrarouge**. La spectroscopie IR mesure ainsi la raideur des liaisons, et la dépendance en $\mu$ explique le décalage isotopique (H/D).
"""
