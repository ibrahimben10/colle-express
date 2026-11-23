D = {}

D['n-p2-tige'] = r"""
**1. Référentiel et base.** On travaille dans le référentiel $\mathcal R'$ lié à la tige, en rotation uniforme à $\vec\omega=\omega\vec u_z$ par rapport au laboratoire (galiléen). On utilise la base cylindrique $(\vec u_r,\vec u_\theta,\vec u_z)$ liée à la tige ($\vec u_r$ selon la tige). Dans $\mathcal R'$, $M$ ne se déplace que le long de la tige : $\overrightarrow{OM}=r\vec u_r$, $\vec v'=\dot r\vec u_r$ et $\vec a'=\ddot r\vec u_r$.

**1. Bilan des forces dans $\mathcal R'$.**
- Poids : $-mg\vec u_z$.
- Réaction de la tige : sans frottement, elle est perpendiculaire à la tige, $\vec R=R_\theta\vec u_\theta+R_z\vec u_z$.
- Force d'inertie d'entraînement (axifuge) : $m\omega^2r\vec u_r$.
- Force de Coriolis : $-2m\vec\omega\wedge\vec v'=-2m\omega\dot r\,\vec u_z\wedge\vec u_r=-2m\omega\dot r\,\vec u_\theta$.

**1. Équation du mouvement.** La projection du principe fondamental sur $\vec u_r$ donne, puisque seule la force axifuge a une composante radiale :
$$m\ddot r=m\omega^2r\iff\ddot r-\omega^2r=0.$$

**1. Résolution.** La solution générale est $r=A\cosh\omega t+B\sinh\omega t$. Avec $r(0)=r_0$ (donc $A=r_0$) et $\dot r(0)=0$ (donc $B=0$) :
$$r(t)=r_0\cosh\omega t.$$
L'anneau s'éloigne de l'axe de plus en plus vite (croissance exponentielle).

**2. Réaction.** On projette le principe fondamental sur les autres axes.
- Sur $\vec u_\theta$ : $0=R_\theta-2m\omega\dot r$, donc $R_\theta=2m\omega\dot r=2m\omega^2r_0\sinh\omega t$.
- Sur $\vec u_z$ : $0=R_z-mg$, donc $R_z=mg$.

C'est la composante $R_\theta$ (orthoradiale, horizontale) qui compense la force de Coriolis. Vu du laboratoire, la tige doit pousser l'anneau latéralement pour lui donner une vitesse orthoradiale $r\omega$ croissante, à mesure que $r$ augmente.

**3. Sortie de la tige.** L'anneau quitte la tige quand $r=L$, c'est-à-dire $\cosh\omega t_s=\frac L{r_0}=10$ :
$$t_s=\frac{\mathrm{argch}\,10}\omega=\frac{\ln\big(10+\sqrt{99}\big)}{2{,}0}=\frac{\ln19{,}95}{2{,}0}\approx\frac{3{,}0}{2{,}0}=1{,}5\ \mathrm s.$$

**4. Vitesse dans le laboratoire.** $\vec v=\vec v'+\vec\omega\wedge\overrightarrow{OM}=\dot r\vec u_r+r\omega\vec u_\theta$, donc $v^2=\dot r^2+r^2\omega^2$. À la sortie, $\dot r=r_0\omega\sinh\omega t_s=\omega\sqrt{r_0^2\cosh^2\omega t_s-r_0^2}=\omega\sqrt{L^2-r_0^2}$. Donc
$$E_c=\frac12m\big[\omega^2(L^2-r_0^2)+L^2\omega^2\big]=\frac12m\omega^2\big(2L^2-r_0^2\big).$$

**4. Origine de l'énergie.** Dans le laboratoire, le poids et $R_z$ ne travaillent pas (mouvement horizontal). En revanche, $R_\theta$ a une puissance non nulle : $\mathcal P=R_\theta\cdot r\omega=2m\omega^2r\dot r$. Son travail vaut
$$W=\int_0^{t_s}2m\omega^2r\dot r\,\mathrm dt=m\omega^2\big[r^2\big]_{r_0}^L=m\omega^2(L^2-r_0^2),$$
et l'on vérifie que $\Delta E_c=\frac12m\omega^2(2L^2-r_0^2)-\frac12m\omega^2r_0^2=m\omega^2(L^2-r_0^2)=W$. ✓ Cette énergie est fournie par le **moteur**, qui exerce sur la tige le couple $\Gamma=rR_\theta$ nécessaire pour maintenir $\omega$ constante malgré l'anneau.
"""

D['n-p2-resonance'] = r"""
**1. Équation du mouvement.** Le principe fondamental, projeté sur l'axe du ressort (avec $x$ compté depuis l'équilibre), donne $m\ddot x=-kx-h\dot x+F_0\cos\omega t$. En divisant par $m$, avec $\frac km=\omega_0^2$ et $\frac hm=\frac{\omega_0}Q$ :
$$\ddot x+\frac{\omega_0}Q\dot x+\omega_0^2x=\frac{F_0}m\cos\omega t.$$

**1. Amplitude complexe.** En régime sinusoïdal forcé, on pose $x=\mathrm{Re}(\underline Xe^{j\omega t})$, avec $\frac{\mathrm d}{\mathrm dt}\to j\omega$ :
$$\Big(\omega_0^2-\omega^2+j\frac{\omega\omega_0}Q\Big)\underline X=\frac{F_0}m\iff\underline X=\frac{F_0/m}{\omega_0^2-\omega^2+j\omega\omega_0/Q},$$
$$X(\omega)=|\underline X|=\frac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2+\omega^2\omega_0^2/Q^2}}.$$

**2. Étude du dénominateur.** $X$ est maximale quand $D=(\omega_0^2-\omega^2)^2+\frac{\omega^2\omega_0^2}{Q^2}$ est minimal. On pose $u=\omega^2\ge0$ :
$$D(u)=(\omega_0^2-u)^2+\frac{u\omega_0^2}{Q^2},\qquad D'(u)=-2(\omega_0^2-u)+\frac{\omega_0^2}{Q^2}.$$
$D'$ s'annule en $u^*=\omega_0^2\big(1-\frac1{2Q^2}\big)$, et $D$ est une parabole convexe en $u$.

**2. Condition de résonance.**
- Si $Q>\frac1{\sqrt2}$, alors $u^*>0$ : $D$ décroît puis croît sur $[0,+\infty[$, et $X$ passe par un maximum en
$$\omega_r=\omega_0\sqrt{1-\frac1{2Q^2}}<\omega_0.$$
- Si $Q\le\frac1{\sqrt2}$, alors $u^*\le0$ : $D$ est croissante sur $[0,+\infty[$, et $X$ décroît dès $\omega=0$. Il n'y a pas de résonance.

**3. Vitesse.** $\underline V=j\omega\underline X$. On divise numérateur et dénominateur par $j\omega\frac{\omega_0}Q$, et on utilise $\frac{F_0}m\cdot\frac Q{\omega_0}=\frac{F_0}h$ :
$$\underline V=\frac{j\omega F_0/m}{\omega_0^2-\omega^2+j\omega\omega_0/Q}=\frac{F_0/h}{1+jQ\big(\frac\omega{\omega_0}-\frac{\omega_0}\omega\big)}.$$
Le module, $V=\frac{F_0/h}{\sqrt{1+Q^2(x-1/x)^2}}$ avec $x=\frac\omega{\omega_0}$, est maximal quand $x-\frac1x=0$, soit en $\omega=\omega_0$, **quel que soit $Q$**. Il vaut alors $V_{\max}=\frac{F_0}h$ : la force excitatrice est exactement compensée par le frottement.

**3. Bande passante.** $V=\frac{V_{\max}}{\sqrt2}$ équivaut à $Q\big|x-\frac1x\big|=1$, soit $x^2\mp\frac xQ-1=0$. Les racines positives sont $x_\pm=\pm\frac1{2Q}+\sqrt{1+\frac1{4Q^2}}$, et leur différence vaut $\frac1Q$ :
$$\Delta\omega=\frac{\omega_0}Q.$$
C'est le même calcul que pour l'intensité dans un circuit RLC série (analogie électromécanique).

**4. Facteur de qualité.**
$$Q=\frac{\omega_0}{\Delta\omega}=\frac{f_0}{\Delta f}=\frac{12{,}0}{0{,}40}=30.$$

**4. Coefficient de frottement.**
$$h=\frac{m\omega_0}Q=\frac{0{,}20\times2\pi\times12{,}0}{30}=\frac{15{,}1}{30}\approx0{,}50\ \mathrm{kg\,s^{-1}}.$$
Avec $Q=30\gg1$, la résonance d'élongation est à $\omega_r=\omega_0\sqrt{1-\frac1{1800}}$, pratiquement confondue avec $\omega_0$. On peut aussi déduire $k=m\omega_0^2\approx1{,}1\times10^3\ \mathrm{N\,m^{-1}}$.
"""

D['n-p2-fourier'] = r"""
**1. Spectre du créneau.** D'après la décomposition donnée, le créneau ne contient que la fréquence $f=1{,}0$ kHz et ses harmoniques impairs, $(2k+1)f$. Il n'a pas de composante continue (il est de moyenne nulle). Toutes ses composantes vérifient $nf\ge f=20f_c$.

**1. Comportement du filtre.** Pour $f'\gg f_c$ :
$$\underline H=\frac1{1+jf'/f_c}\approx\frac{f_c}{jf'}=\frac1{jRC\omega'}.$$
L'erreur relative sur le module est inférieure à $\frac12\big(\frac{f_c}{f'}\big)^2\approx10^{-3}$. Diviser par $j\omega$ revient à intégrer : pour chaque composante, et donc pour le signal entier par linéarité,
$$s(t)\approx\frac1{RC}\int e(t)\,\mathrm dt+\text{cste}.$$
Le filtre est **intégrateur**. En régime permanent, $s$ est de moyenne nulle, comme $e$ (car $\underline H(0)=1$ et la moyenne de $e$ est nulle).

**2. Forme temporelle.** Sur une demi-période où $e=+E$, $\frac{\mathrm ds}{\mathrm dt}=\frac E{RC}$ : $s$ croît linéairement. Sur la demi-période suivante, $e=-E$ et $s$ décroît avec la pente opposée. Le signal de sortie est **triangulaire**, symétrique et de moyenne nulle.

**2. Amplitude crête à crête.** Pendant une demi-période $\frac T2=\frac1{2f}$, $s$ varie de
$$\Delta s=\frac E{RC}\cdot\frac T2=\frac{E\cdot2\pi f_c}{2f}=\pi\frac{f_c}fE=\pi\times\frac{50}{1000}E\approx0{,}16\,E,$$
car $\frac1{RC}=2\pi f_c$. Le triangle est donc très atténué : la sortie est faible devant l'entrée.

**3. Analyse spectrale.** La composante de rang $n$ (impair) a en entrée l'amplitude $\frac{4E}{n\pi}$. Le gain vaut $|\underline H(nf)|\approx\frac{f_c}{nf}$, et le déphasage est de $-\frac\pi2$ (chaque $\sin$ devient $-\cos$). En sortie :
$$S_n\approx\frac{4E}{n\pi}\cdot\frac{f_c}{nf}=\frac{4Ef_c}{\pi f}\cdot\frac1{n^2}.$$
- Fondamental ($n=1$) : $S_1=\frac{4\times0{,}05}\pi E\approx0{,}064\,E$.
- Harmonique 3 : $S_3=\frac{S_1}9\approx0{,}0071\,E$.

**3. Cohérence avec le temporel.** Un triangle d'amplitude crête $A$ a pour décomposition $\frac{8A}{\pi^2}\sum\frac{\cos((2k+1)\omega t)}{(2k+1)^2}$ (au signe près). Avec $A=\frac{\Delta s}2=\frac{\pi f_c}{2f}E$ : $\frac{8A}{\pi^2}=\frac{4f_cE}{\pi f}=S_1$. ✓

**3. Signal « plus sinusoïdal ».** En entrée, l'harmonique 3 vaut $\frac13$ du fondamental ; en sortie, il ne vaut plus que $\frac19$. Les harmoniques décroissent en $\frac1{n^2}$ au lieu de $\frac1n$. Les harmoniques élevés sont responsables des discontinuités (fronts raides) du créneau. Le triangle est continu, sa série converge plus vite, et il est mieux approché par son seul fondamental. Plus généralement, l'intégration (filtrage passe-bas) régularise un signal.
"""

D['n-p2-coax'] = r"""
**1. Symétries.** Le câble est supposé infini. La distribution de charges est invariante par rotation autour de l'axe et par translation selon l'axe, donc $E$ ne dépend que de $r$. Les plans contenant l'axe et les plans perpendiculaires à l'axe sont plans de symétrie, donc $\vec E$ est radial : $\vec E=E(r)\vec u_r$.

**1. Théorème de Gauss.** On prend un cylindre coaxial de rayon $r\in]R_1,R_2[$ et de hauteur $h$ ; le flux est nul à travers les bases. La charge intérieure est celle de l'âme, $\lambda h$. Dans le diélectrique, on remplace $\varepsilon_0$ par $\varepsilon_0\varepsilon_r$ :
$$E(r)\cdot2\pi rh=\frac{\lambda h}{\varepsilon_0\varepsilon_r}\quad\Longrightarrow\quad E(r)=\frac\lambda{2\pi\varepsilon_0\varepsilon_rr}.$$

**1. Tension et capacité.** $U=V(R_1)-V(R_2)=\int_{R_1}^{R_2}E(r)\,\mathrm dr=\frac\lambda{2\pi\varepsilon_0\varepsilon_r}\ln\frac{R_2}{R_1}$. La capacité linéique est définie par $\lambda=\Gamma U$ :
$$\Gamma=\frac{2\pi\varepsilon_0\varepsilon_r}{\ln(R_2/R_1)}.$$

**2. Champ magnétique.** Par symétrie, tout plan contenant l'axe est plan de symétrie des courants. $\vec B$, pseudo-vecteur, est orthogonal à ces plans : $\vec B=B(r)\vec u_\theta$. Le théorème d'Ampère sur un cercle coaxial de rayon $r$ donne $2\pi rB(r)=\mu_0I_{\mathrm{enl}}$.
- Pour $R_1<r<R_2$ : $I_{\mathrm{enl}}=I$ (l'âme), donc $B=\frac{\mu_0I}{2\pi r}$.
- Pour $r>R_2$ : $I_{\mathrm{enl}}=I-I=0$, donc $B=0$. Le câble ne rayonne pas de champ magnétique à l'extérieur : c'est l'intérêt du blindage coaxial.

**2. Énergie magnétique linéique.** La densité d'énergie vaut $\frac{B^2}{2\mu_0}$ ; on intègre sur une couronne de longueur unité, de volume $2\pi r\,\mathrm dr$ :
$$\mathcal E_m=\int_{R_1}^{R_2}\frac1{2\mu_0}\Big(\frac{\mu_0I}{2\pi r}\Big)^22\pi r\,\mathrm dr=\frac{\mu_0I^2}{4\pi}\int_{R_1}^{R_2}\frac{\mathrm dr}r=\frac{\mu_0I^2}{4\pi}\ln\frac{R_2}{R_1}.$$
On néglige le champ à l'intérieur de l'âme : en haute fréquence, le courant y est en surface (effet de peau).

**2. Inductance linéique.** Par définition, $\mathcal E_m=\frac12\Lambda I^2$, donc
$$\Lambda=\frac{\mu_0}{2\pi}\ln\frac{R_2}{R_1}.$$

**3. Applications numériques.** $\frac{R_2}{R_1}=3{,}5$, d'où $\ln3{,}5=1{,}25$.
$$\Gamma=\frac{2\pi\times8{,}85\times10^{-12}\times2{,}25}{1{,}25}\approx1{,}0\times10^{-10}\ \mathrm{F\,m^{-1}}=100\ \mathrm{pF\,m^{-1}},$$
$$\Lambda=\frac{4\pi\times10^{-7}}{2\pi}\times1{,}25=2{,}5\times10^{-7}\ \mathrm{H\,m^{-1}}=0{,}25\ \mu\mathrm H\,\mathrm m^{-1}.$$

**3. Vitesse des signaux.** Le produit $\Lambda\Gamma=\mu_0\varepsilon_0\varepsilon_r=\frac{\varepsilon_r}{c^2}$ ne dépend pas de la géométrie :
$$v=\frac1{\sqrt{\Lambda\Gamma}}=\frac c{\sqrt{\varepsilon_r}}=\frac{3{,}0\times10^8}{1{,}5}=2{,}0\times10^8\ \mathrm{m\,s^{-1}}.$$
Un signal parcourt donc 20 cm par nanoseconde dans le câble.

**3. Impédance caractéristique.**
$$Z_c=\sqrt{\frac\Lambda\Gamma}=\sqrt{\frac{2{,}5\times10^{-7}}{1{,}0\times10^{-10}}}=\sqrt{2500}=50\ \Omega.$$
C'est l'impédance standard des câbles BNC de laboratoire. Une charge de $50\ \Omega$ en bout de câble évite les réflexions (adaptation d'impédance).
"""

D['n-p2-serre'] = r"""
**1. Puissance absorbée.** La Terre reçoit le flux solaire sur sa section droite, le disque $\pi R^2$ (et non sur la sphère entière). Elle en réfléchit la fraction $A$, donc elle absorbe $\mathcal P_a=(1-A)\varphi_S\pi R^2$.

**1. Puissance émise.** Corps noir à $T_s$ sur toute sa surface (la rotation rapide uniformise la température) : $\mathcal P_e=4\pi R^2\sigma T_s^4$.

**1. Équilibre radiatif.** $\mathcal P_a=\mathcal P_e$, donc
$$T_s=\Big(\frac{(1-A)\varphi_S}{4\sigma}\Big)^{1/4}=\Big(\frac{0{,}70\times1361}{4\times5{,}67\times10^{-8}}\Big)^{1/4}=\big(4{,}20\times10^9\big)^{1/4}\approx255\ \mathrm K.$$
Le facteur 4 est le rapport de la surface émettrice à la section réceptrice.

**1. Commentaire.** On trouve environ $-18\ ^\circ$C, alors que la température moyenne réelle est de $288$ K ($15\ ^\circ$C). L'écart de 33 K est dû à l'atmosphère : c'est l'effet de serre naturel, sans lequel la Terre serait gelée.

**2. Hypothèses du modèle.** Couche transparente au visible : tout le flux solaire non réfléchi atteint le sol. Opaque à l'infrarouge : elle absorbe tout le rayonnement thermique du sol, à $T_s\approx300$ K, donc $\lambda_{\max}\approx10\ \mu$m. Elle rayonne $\sigma T_a^4$ par chacune de ses deux faces. On raisonne en flux moyens par unité de surface terrestre, avec $\varphi=\frac{(1-A)\varphi_S}4\approx238\ \mathrm{W\,m^{-2}}$.

**2. Bilan de la couche.** Elle reçoit $\sigma T_s^4$ (du sol) et émet $2\sigma T_a^4$ (vers le haut et vers le bas) :
$$\sigma T_s^4=2\sigma T_a^4.$$

**2. Bilan du sol.** Il reçoit le Soleil, $\varphi$, et le rayonnement de la couche vers le bas, $\sigma T_a^4$ ; il émet $\sigma T_s^4$ :
$$\varphi+\sigma T_a^4=\sigma T_s^4.$$

**2. Résolution.** En reportant $\sigma T_s^4=2\sigma T_a^4$ : $\varphi+\sigma T_a^4=2\sigma T_a^4$, donc $\sigma T_a^4=\varphi$, d'où
$$T_a=\Big(\frac\varphi\sigma\Big)^{1/4}=255\ \mathrm K,\qquad T_s=2^{1/4}T_a\approx1{,}19\times255\approx303\ \mathrm K.$$

**2. Interprétation.** Vue de l'espace, la planète rayonne toujours $\varphi$ à 255 K, comme à la question 1 : c'est le bilan global. Mais cette émission vient désormais de l'atmosphère. Le sol reçoit en plus le rayonnement de retour de la couche : il reçoit $2\varphi$ au lieu de $\varphi$, et doit être plus chaud pour l'évacuer.

**3. Surestimation.** On trouve 303 K au lieu de 288 K, car :
- l'atmosphère n'absorbe pas tout l'infrarouge : il existe une « fenêtre atmosphérique » entre 8 et 13 µm, par laquelle le sol rayonne directement vers l'espace ;
- elle absorbe une partie du rayonnement solaire (ozone, vapeur d'eau) ;
- le sol perd aussi de l'énergie par convection et par évaporation (chaleur latente), et pas seulement par rayonnement ;
- l'atmosphère n'est pas une couche isotherme : sa température décroît avec l'altitude.

Le modèle met néanmoins en évidence le mécanisme : en renvoyant vers le sol une partie de l'infrarouge, l'atmosphère le réchauffe. Augmenter la concentration de gaz absorbant l'infrarouge ($\mathrm{CO_2}$, $\mathrm{CH_4}$) renforce cet effet.
"""

D['n-p2-dipole'] = r"""
**1. Potentiel dipolaire.** À grande distance ($r\gg$ taille du dipôle), en coordonnées sphériques d'axe $\vec p$ :
$$V(r,\theta)=\frac{\vec p\cdot\vec u_r}{4\pi\varepsilon_0r^2}=\frac{p\cos\theta}{4\pi\varepsilon_0r^2}.$$

**1. Champ.** $\vec E=-\overrightarrow{\mathrm{grad}}\,V$, avec $\overrightarrow{\mathrm{grad}}=\frac{\partial}{\partial r}\vec u_r+\frac1r\frac{\partial}{\partial\theta}\vec u_\theta+\frac1{r\sin\theta}\frac{\partial}{\partial\varphi}\vec u_\varphi$ :
$$E_r=-\frac{\partial V}{\partial r}=\frac{2p\cos\theta}{4\pi\varepsilon_0r^3},\qquad E_\theta=-\frac1r\frac{\partial V}{\partial\theta}=\frac{p\sin\theta}{4\pi\varepsilon_0r^3},\qquad E_\varphi=0.$$
Le champ décroît en $\frac1{r^3}$, plus vite que celui d'une charge, car les deux charges opposées se compensent presque.

**2. Énergie potentielle.** Pour un dipôle rigide (charges $\pm q$ en $A$ et $B$, avec $\vec p=q\overrightarrow{AB}$) dans un champ extérieur, $E_p=qV(B)-qV(A)\approx q\,\overrightarrow{AB}\cdot\overrightarrow{\mathrm{grad}}\,V$, d'où
$$E_p=-\vec p\cdot\vec E.$$

**2. Équilibre stable.** $E_p=-pE\cos\alpha$, où $\alpha$ est l'angle entre $\vec p$ et $\vec E$. Elle est minimale pour $\alpha=0$ : $\vec p$ est aligné sur $\vec E$, dans le même sens. Le couple $\vec\Gamma=\vec p\wedge\vec E$ ramène le dipôle vers cette position. La position $\alpha=\pi$ est un équilibre instable.

**3. Champ de l'ion.** $\mathrm{Na^+}$ (charge $e$) crée en $M$ un champ radial $E=\frac e{4\pi\varepsilon_0r^2}$, dirigé de l'ion vers la molécule.

**3. Orientation.** À l'équilibre, $\vec p$ est dans le sens de $\vec E$, c'est-à-dire qu'il s'éloigne de l'ion. $\vec p$ allant du pôle négatif au pôle positif, c'est l'atome d'oxygène (pôle $-$) qui est tourné vers le cation.

**3. Énergie d'interaction.**
$$E_p=-pE=-\frac{pe}{4\pi\varepsilon_0r^2}=-\frac{9{,}0\times10^9\times6{,}2\times10^{-30}\times1{,}6\times10^{-19}}{(3{,}0\times10^{-10})^2}=-\frac{8{,}9\times10^{-39}}{9{,}0\times10^{-20}}\approx-9{,}9\times10^{-20}\ \mathrm J,$$
soit $-0{,}62$ eV.

**3. Comparaison.** À 300 K, $k_BT=1{,}38\times10^{-23}\times300=4{,}1\times10^{-21}$ J $\approx0{,}026$ eV. Donc $\frac{|E_p|}{k_BT}\approx24$.

**3. Solvatation.** L'agitation thermique ne peut pas désorienter les molécules d'eau les plus proches : elles restent fixées et orientées autour de l'ion, formant une **couche de solvatation** (environ 6 molécules pour $\mathrm{Na^+}$). L'énergie libérée explique la grande solubilité des sels ioniques dans l'eau, solvant très polaire. Le modèle du dipôle ponctuel est grossier à 0,3 nm (la molécule mesure environ 0,1 nm), mais l'ordre de grandeur est correct.

**4. Force.** Le dipôle reste orienté selon le champ ; son énergie dépend de sa distance à l'ion :
$$E_p(r)=-\frac{pe}{4\pi\varepsilon_0r^2},\qquad F_r=-\frac{\mathrm dE_p}{\mathrm dr}=-\frac{2pe}{4\pi\varepsilon_0r^3}<0.$$
La force est **attractive**, de norme $\frac{2pe}{4\pi\varepsilon_0r^3}$, et décroît en $\frac1{r^3}$. Un dipôle aligné sur le champ est attiré vers les régions de champ intense. Sur le dipôle orienté, la charge la plus proche (attirée) subit un champ plus fort que la plus éloignée (repoussée).
"""
