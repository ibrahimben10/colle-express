D = {}

D['p-max-2'] = r"""
**1. Critère de l'ARQS.** L'approximation des régimes quasi stationnaires consiste à négliger les retards de propagation. Elle est valable si la durée de propagation $\tau$ à travers le circuit est très petite devant la période $T$ des signaux.
- $\tau=\frac L{c_0}=\frac{0{,}30}{3{,}0\times10^8}=1{,}0\times10^{-9}$ s.
- La fréquence maximale est $f=1$ MHz, donc $T\ge\frac1f=1{,}0\times10^{-6}$ s.

$\frac\tau T\le10^{-3}\ll1$ : l'ARQS est vérifiée. De façon équivalente, la longueur d'onde $\lambda=\frac{c_0}f=300$ m est très grande devant $L=0{,}3$ m.

**2. Ordre de grandeur de $E$.** L'équation de Maxwell-Faraday, $\overrightarrow{\mathrm{rot}}\,\vec E=-\frac{\partial\vec B}{\partial t}$, s'écrit en ordres de grandeur (dérivées spatiales $\sim\frac1L$, dérivées temporelles $\sim\frac1T$) :
$$\frac EL\sim\frac BT\quad\Longrightarrow\quad E\sim\frac{LB}T.$$

**2. Calcul du rapport.** Avec $\varepsilon_0\mu_0=\frac1{c_0^2}$ :
$$\Big\|\varepsilon_0\mu_0\frac{\partial\vec E}{\partial t}\Big\|\sim\frac1{c_0^2}\cdot\frac ET\sim\frac{LB}{c_0^2T^2},\qquad\big\|\overrightarrow{\mathrm{rot}}\,\vec B\big\|\sim\frac BL.$$
D'où
$$\frac{\|\varepsilon_0\mu_0\,\partial\vec E/\partial t\|}{\|\overrightarrow{\mathrm{rot}}\,\vec B\|}\sim\frac{LB}{c_0^2T^2}\cdot\frac LB=\frac{L^2}{c_0^2T^2}=\Big(\frac\tau T\Big)^2\le10^{-6}.$$

**3. Équations de Maxwell dans l'ARQS.** Le terme $\varepsilon_0\mu_0\frac{\partial\vec E}{\partial t}$ (courant de déplacement) est négligeable dans Maxwell-Ampère. Il reste :
$$\mathrm{div}\,\vec E=\frac\rho{\varepsilon_0},\qquad\mathrm{div}\,\vec B=0,\qquad\overrightarrow{\mathrm{rot}}\,\vec E=-\frac{\partial\vec B}{\partial t},\qquad\overrightarrow{\mathrm{rot}}\,\vec B=\mu_0\vec j.$$

**3. Comparaison avec le régime stationnaire.** En régime stationnaire, on a les mêmes équations, sauf $\overrightarrow{\mathrm{rot}}\,\vec E=\vec0$. La seule différence est donc le terme $-\frac{\partial\vec B}{\partial t}$ de Maxwell-Faraday, responsable de l'**induction**. Le champ $\vec B$ se calcule à chaque instant comme en magnétostatique (Biot et Savart, Ampère), à partir des courants à cet instant.

**3. Conséquence.** En prenant la divergence de $\overrightarrow{\mathrm{rot}}\,\vec B=\mu_0\vec j$ : $\mathrm{div}\,\vec j=0$ (car $\mathrm{div}\,\overrightarrow{\mathrm{rot}}=0$). Le flux de $\vec j$ est conservatif : l'intensité est la même en tout point d'une branche, et la loi des nœuds est valable.

**4. Lien avec l'électricité de première année.** Les lois de l'électrocinétique de première année sont des conséquences de ces équations :
- la loi des nœuds découle de $\mathrm{div}\,\vec j=0$ ;
- la loi des mailles découle de la circulation de $\vec E$, avec la f.é.m. d'induction pour les bobines ($u=L\frac{\mathrm di}{\mathrm dt}$) ;
- les relations des condensateurs et des résistances en découlent aussi.

Elles ne valent que dans l'ARQS, toujours vérifiée en TP (circuits de quelques dizaines de centimètres, fréquences $\lesssim$ MHz). Pour des lignes longues ou des hautes fréquences (câbles, antennes), il faut tenir compte de la propagation.
"""

D['p-max-3'] = r"""
**1. Conservation du courant.** En régime permanent, $\mathrm{div}\,\vec j=0$ : le flux de $\vec j$ à travers tout cylindre de rayon $r\in[b,c]$ et de hauteur $a$ est le même. Avec $\vec j=j(r)\vec u_r$, la surface latérale vaut $2\pi ra$, donc
$$I=j(r)\cdot2\pi ra\quad\Longrightarrow\quad j(r)=\frac I{2\pi ar}.$$

**1. Loi d'Ohm locale.** $\vec E=\frac{\vec j}\gamma$, donc $E(r)=\frac I{2\pi a\gamma r}$.

**1. Lien avec $U$.** $\vec E=-\overrightarrow{\mathrm{grad}}\,V$, donc $U=V(b)-V(c)=\int_b^cE(r)\,\mathrm dr$. D'où
$$U=\frac I{2\pi a\gamma}\int_b^c\frac{\mathrm dr}r=\frac I{2\pi a\gamma}\ln\frac cb.$$

**1. Résultats.**
$$I=\frac{2\pi a\gamma U}{\ln(c/b)},\qquad\vec E=\frac U{r\ln(c/b)}\vec u_r,\qquad\vec j=\frac{\gamma U}{r\ln(c/b)}\vec u_r.$$

**2. Résistance radiale.**
$$R_0=\frac UI=\frac{\ln(c/b)}{2\pi a\gamma}.$$
(On retrouve aussi ce résultat en sommant des résistances de coquilles en série : $\mathrm dR=\frac{\mathrm dr}{\gamma\cdot2\pi ra}$.)

**3. Équation du mouvement d'un électron.** Un électron de charge $-e$ subit la force de Lorentz et une force de frottement modélisant les collisions :
$$m\frac{\mathrm d\vec v}{\mathrm dt}=-e\big(\vec E+\vec v\wedge\vec B\big)-\frac m\tau\vec v.$$

**4. Régime permanent.** On a $\frac{\mathrm d\vec v}{\mathrm dt}=\vec0$, donc $\frac m\tau\vec v=-e(\vec E+\vec v\wedge\vec B)$, soit
$$\vec E=-\frac m{e\tau}\vec v-\vec v\wedge\vec B.$$
La densité de courant est $\vec j=-n_0e\vec v$, donc $\vec v=-\frac{\vec j}{n_0e}$. En substituant, puis avec $\frac m{n_0e^2\tau}=\frac1\gamma$ :
$$\vec E=\frac m{n_0e^2\tau}\vec j+\frac{\vec j\wedge\vec B}{n_0e}=\frac{\vec j}\gamma+\frac{\vec j\wedge\vec B}{n_0e}.$$

**5. Produit vectoriel en base cylindrique.** Écrivons $\vec j=j_r\vec u_r+j_\theta\vec u_\theta+j_z\vec u_z$. Avec $\vec u_r\wedge\vec u_z=-\vec u_\theta$, $\vec u_\theta\wedge\vec u_z=\vec u_r$ et $\vec u_z\wedge\vec u_z=\vec0$ :
$$\vec j\wedge\vec B=B\big(j_\theta\vec u_r-j_r\vec u_\theta\big).$$

**5. Projections.** Le champ électrique reste radial : par symétrie de révolution, $V=V(r)$, donc $E_\theta=-\frac1r\frac{\partial V}{\partial\theta}=0$, et $E_z=0$ (les faces du disque sont isolées).
- Sur $\vec u_z$ : $0=\frac{j_z}\gamma$, donc $j_z=0$.
- Sur $\vec u_\theta$ : $0=\frac{j_\theta}\gamma-\frac{Bj_r}{n_0e}$, donc $j_\theta=\frac{\gamma B}{n_0e}j_r$.

L'angle de Hall $\theta_H=(\vec u_r,\vec j)$ vérifie donc
$$\tan\theta_H=\frac{j_\theta}{j_r}=\frac{\gamma B}{n_0e}=\frac{e\tau B}m=\mu_eB,$$
où $\mu_e=\frac{e\tau}m$ est la mobilité électronique. L'angle est indépendant de $r$.

**6. Lignes de courant.** Le long d'une ligne de courant, $\frac{r\,\mathrm d\theta}{\mathrm dr}=\frac{j_\theta}{j_r}=\tan\theta_H$, soit $\frac{\mathrm dr}r=\frac{\mathrm d\theta}{\tan\theta_H}$. Donc $r=r_0\exp\big(\frac{\theta-\theta_0}{\tan\theta_H}\big)$ : ce sont des **spirales logarithmiques**, qui coupent chaque rayon sous l'angle constant $\theta_H$.

**7. Projection radiale.**
$$E=\frac{j_r}\gamma+\frac{Bj_\theta}{n_0e}=\frac{j_r}\gamma+\frac{B}{n_0e}\cdot\frac{\gamma B}{n_0e}j_r=\frac{j_r}\gamma\big(1+\tan^2\theta_H\big).$$

**7. Nouvelle résistance.** Le courant $I$ qui traverse un cylindre de rayon $r$ n'est dû qu'à $j_r$ : $I=2\pi ra\,j_r$. Donc $E=\frac I{2\pi a\gamma r}(1+\tan^2\theta_H)$ et, en intégrant de $b$ à $c$ :
$$U=\frac{I\ln(c/b)}{2\pi a\gamma}(1+\tan^2\theta_H)=R_0I(1+\tan^2\theta_H).$$
Ainsi $R=R_0(1+\varepsilon)$ avec
$$\varepsilon=\tan^2\theta_H=\Big(\frac{e\tau B}m\Big)^2.$$

**7. Interprétation.** Les électrons, déviés par $\vec B$, parcourent un chemin plus long (les spirales) : la résistance augmente. C'est la **magnétorésistance géométrique** (effet Corbino). Dans cette géométrie, aucune charge ne s'accumule sur un bord pour compenser la déviation (contrairement à l'effet Hall dans un barreau). La mesure de $\varepsilon(B)$ donne la mobilité $\frac{e\tau}m$.
"""

D['p-ind-2'] = r"""
**0. Paramétrage.** On note $z$ la cote de la tige (axe vertical ascendant), avec l'origine à la position d'équilibre mécanique en l'absence de courant : les ressorts compensent alors le poids. Les deux ressorts sont équivalents à un seul ressort de raideur $2k$, et la force totale de rappel autour de l'équilibre vaut $-2kz\,\vec u_z$. Le champ $\vec B$ est normal au plan du circuit, et l'on oriente le circuit de sorte que la normale associée soit $\vec B/B$.

**1. Flux et f.é.m.** La surface du circuit délimitée par la tige varie de $D\,\mathrm dz$ quand la tige monte de $\mathrm dz$. Avec l'orientation choisie (pour fixer les idées, aire croissante quand $z$ croît), $\Phi(t)=BDz+\text{cste}$. Par la loi de Faraday :
$$e=-\frac{\mathrm d\Phi}{\mathrm dt}=-BD\dot z.$$

**1. Équation électrique.** Sans auto-induction, le circuit se réduit à la f.é.m. $e$ en série avec $R$ (convention générateur) :
$$Ri=e=-BD\dot z\quad\Longrightarrow\quad i=-\frac{BD}R\dot z.$$

**1. Force de Laplace.** Sur la tige, de longueur $D$ parcourue par $i$, $\vec F=i\,\vec D\wedge\vec B$. Avec l'orientation cohérente, $F_z=iDB$ (le signe est fixé par la loi de Lenz : la force s'oppose au mouvement). En reportant $i$ :
$$F_z=iDB=-\frac{B^2D^2}R\dot z.$$

**1. Équation mécanique.** Le principe fondamental de la dynamique, projeté sur $\vec u_z$ (poids et tension d'équilibre se compensent), donne
$$m\ddot z=-2kz-\alpha\dot z+iDB=-2kz-\Big(\alpha+\frac{B^2D^2}R\Big)\dot z.$$

**2. Équation de puissance mécanique.** On multiplie l'équation mécanique par $\dot z$ :
$$m\dot z\ddot z+2kz\dot z=-\alpha\dot z^2+iDB\dot z\iff\frac{\mathrm d}{\mathrm dt}\Big(\frac12m\dot z^2+kz^2\Big)=-\alpha\dot z^2+\mathcal P_L,$$
où $\mathcal P_L=iDB\dot z$ est la puissance de la force de Laplace.

**2. Équation de puissance électrique.** On multiplie l'équation électrique par $i$ : $Ri^2=ei=-BD\dot zi$. Donc $ei=-\mathcal P_L$ : la puissance fournie par la f.é.m. d'induction est exactement l'opposée de la puissance de la force de Laplace (couplage électromécanique parfait).

**2. Bilan.** En combinant les deux équations :
$$\frac{\mathrm d}{\mathrm dt}\Big(\underbrace{\frac12m\dot z^2}_{\text{cinétique}}+\underbrace{kz^2}_{\text{élastique + pesanteur}}\Big)=-\underbrace{\alpha\dot z^2}_{\text{frottement}}-\underbrace{Ri^2}_{\text{effet Joule}}\le0.$$
Le terme $kz^2$ regroupe l'énergie potentielle élastique et celle de pesanteur, grâce au choix de l'origine à l'équilibre. L'énergie mécanique est convertie en énergie électrique par induction, puis dissipée par effet Joule dans $R$ ; une autre partie est dissipée par les frottements.

**3. Forme canonique.** En divisant par $m$ :
$$\ddot z+\frac2\tau\dot z+\omega_0^2z=0,\qquad\omega_0=\sqrt{\frac{2k}m},\qquad\frac2\tau=\frac1m\Big(\alpha+\frac{B^2D^2}R\Big).$$

**3. Régime pseudo-périodique.** Si $\frac1\tau<\omega_0$, l'équation caractéristique $r^2+\frac2\tau r+\omega_0^2=0$ a pour racines $r=-\frac1\tau\pm i\Omega$, avec $\Omega=\sqrt{\omega_0^2-\frac1{\tau^2}}$. Donc $z(t)=Ae^{-t/\tau}\cos(\Omega t+\varphi)$, et le temps caractéristique d'amortissement est
$$\tau=\frac{2m}{\alpha+\frac{B^2D^2}R}.$$
Le champ magnétique raccourcit $\tau$ : c'est le principe du freinage par courants induits.
"""

D['p-ind-3'] = r"""
**1. Champ du solénoïde.** On suppose le solénoïde long ($D\gg2R$) ; on néglige les effets de bord, et la bobine plate est au centre. Le solénoïde compte $n=\frac{10N}D$ spires par mètre. Par le théorème d'Ampère, le champ est uniforme à l'intérieur et nul à l'extérieur :
$$\vec B=\mu_0\frac{10N}Di\,\vec u_z\quad(r<2R),\qquad\vec B=\vec0\quad(r>2R).$$

**1. Flux à travers la bobine plate.** Chacune des $N$ spires de rayon $R$ est un disque d'aire $\pi R^2$, entièrement inclus dans la section du solénoïde ($R<2R$). Le champ y est uniforme et parallèle à la normale :
$$\Phi_{\text{sol}\to\text{bob}}=N\cdot B\cdot\pi R^2=N\cdot\mu_0\frac{10N}Di\cdot\pi R^2.$$

**1. Mutuelle inductance.** Par définition, $\Phi_{\text{sol}\to\text{bob}}=Mi$, donc
$$M=\frac{10\,\mu_0N^2\pi R^2}D.$$

**2. Bobine plate de rayon $2R$, solénoïde de rayon $R$.** Le champ du solénoïde est toujours $B=\mu_0\frac{10N}Di$, mais il n'est non nul que pour $r<R$. Le flux à travers une spire de rayon $2R$ se limite donc au disque central de rayon $R$ (le champ est nul sur la couronne $R<r<2R$) :
$$\Phi=N\cdot B\cdot\pi R^2\quad\Longrightarrow\quad M=\frac{10\,\mu_0N^2\pi R^2}D.$$
On obtient la même valeur : seule compte la section du solénoïde à travers laquelle passe le champ, c'est-à-dire la plus petite des deux sections.

**Remarque.** Le théorème de Neumann assure $M_{12}=M_{21}$. Pour obtenir $M$, on calcule donc le flux le plus simple : celui du champ du solénoïde (uniforme) à travers la bobine plate. Le calcul inverse (le champ de la bobine plate, non uniforme, à travers les $10N$ spires du solénoïde) serait bien plus difficile, mais donnerait le même résultat.
"""

D['p-ondes-1'] = r"""
**1. Dimension de $E$.** La tension d'un ressort allongé de $\Delta\ell$ vaut $F=k\Delta\ell=\frac{ES}{\mathrm dx}\Delta\ell$, donc
$$E=\frac{F/S}{\Delta\ell/\mathrm dx}.$$
$\frac{\Delta\ell}{\mathrm dx}$ (allongement relatif) est sans dimension, donc $E$ est homogène à une force par unité de surface, c'est-à-dire à une **pression** (contrainte). Il s'exprime en pascals ($\mathrm{N\,m^{-2}}$).

**1. Nom.** La loi de Hooke $\frac FS=E\frac{\Delta\ell}\ell$ relie la contrainte à la déformation relative, dans le domaine élastique (déformation réversible). $E$ mesure la raideur intrinsèque du matériau, indépendamment de la géométrie de la tige : c'est le « module d'élasticité » (ou module d'Young). Ordres de grandeur : acier $E\approx2\times10^{11}$ Pa, caoutchouc $\approx10^6$ Pa.

**2. Forces sur la masselotte d'abscisse $x$.** Elle est reliée à deux ressorts.
- **Ressort de droite**, entre $x$ et $x+\mathrm dx$ : son allongement vaut $u(x+\mathrm dx,t)-u(x,t)$, sa tension tire la masselotte vers la droite, d'où une force $k\big[u(x+\mathrm dx)-u(x)\big]$ selon $\vec u_x$.
- **Ressort de gauche**, entre $x-\mathrm dx$ et $x$ : son allongement vaut $u(x)-u(x-\mathrm dx)$, sa tension tire la masselotte vers la gauche, d'où une force $-k\big[u(x)-u(x-\mathrm dx)\big]$.

**2. Loi de la quantité de mouvement.** Sur $\vec u_x$, pour la masse $\mu S\,\mathrm dx$ :
$$\mu S\,\mathrm dx\,\frac{\partial^2u}{\partial t^2}(x,t)=k\big[u(x+\mathrm dx,t)-u(x,t)\big]-k\big[u(x,t)-u(x-\mathrm dx,t)\big].$$

**3. Développements de Taylor à l'ordre 2.**
$$u(x\pm\mathrm dx,t)=u(x,t)\pm\mathrm dx\,\frac{\partial u}{\partial x}+\frac{\mathrm dx^2}2\frac{\partial^2u}{\partial x^2}+o(\mathrm dx^2).$$
Donc
$$u(x+\mathrm dx)-2u(x)+u(x-\mathrm dx)=\mathrm dx^2\frac{\partial^2u}{\partial x^2}+o(\mathrm dx^2).$$
Les termes d'ordre 1 se compensent : il faut bien aller jusqu'à l'ordre 2.

**3. Équation de d'Alembert.** Avec $k=\frac{ES}{\mathrm dx}$ :
$$\mu S\,\mathrm dx\,\frac{\partial^2u}{\partial t^2}=\frac{ES}{\mathrm dx}\cdot\mathrm dx^2\frac{\partial^2u}{\partial x^2}=ES\,\mathrm dx\,\frac{\partial^2u}{\partial x^2}.$$
En divisant par $\mu S\,\mathrm dx$ :
$$\frac{\partial^2u}{\partial x^2}-\frac1{c^2}\frac{\partial^2u}{\partial t^2}=0,\qquad c=\sqrt{\frac E\mu}.$$
Vérification dimensionnelle : $\frac E\mu$ est en $\frac{\mathrm{Pa}}{\mathrm{kg\,m^{-3}}}=\frac{\mathrm{kg\,m^{-1}\,s^{-2}}}{\mathrm{kg\,m^{-3}}}=\mathrm{m^2\,s^{-2}}$. ✓

**3. Application numérique (acier).** $c=\sqrt{\frac{2\times10^{11}}{7800}}=\sqrt{2{,}6\times10^7}\approx5\times10^3\ \mathrm{m\,s^{-1}}$. C'est bien la vitesse du son dans l'acier, environ 15 fois celle dans l'air.
"""
