D = {}

D['p-th-ccs4'] = r"""
**1. Bilan sur une tranche.** On considère la tranche $[x,x+\mathrm dx]$, de section $S$, de masse volumique $\rho$ et de capacité thermique massique $c$. Entre $t$ et $t+\mathrm dt$ :
$$\underbrace{\rho cS\,\mathrm dx\,\frac{\partial T}{\partial t}\mathrm dt}_{\mathrm dU}=\underbrace{\big[j(x)-j(x+\mathrm dx)\big]S\,\mathrm dt}_{\text{conduction}}+\underbrace{qS\,\mathrm dx\,\mathrm dt}_{\text{production}}.$$
Avec $j(x)-j(x+\mathrm dx)=-\frac{\partial j}{\partial x}\mathrm dx$ et la loi de Fourier $j=-k\frac{\partial T}{\partial x}$ :
$$\rho c\frac{\partial T}{\partial t}=k\frac{\partial^2T}{\partial x^2}+q.$$

**1. Régime stationnaire.** Il suppose que les températures des faces et la production $q$ sont constantes, et qu'on attend une durée grande devant le temps de diffusion $\tau\sim\frac{(2L)^2}D$, avec $D=\frac k{\rho c}$. Alors $\frac{\partial T}{\partial t}=0$.

**2. Équation stationnaire.** $kT''(x)=-q$, donc $T'(x)=-\frac qkx+A$ et $T(x)=-\frac q{2k}x^2+Ax+B$.

**2. Conditions aux limites.** $T(L)=T(-L)=T_0$. La différence donne $2AL=0$, donc $A=0$ : le profil est symétrique et $T'(0)=0$, le flux est nul au centre. Puis $T_0=-\frac q{2k}L^2+B$, d'où
$$T(x)=T_0+\frac q{2k}\big(L^2-x^2\big).$$
C'est une parabole, avec un maximum au centre : $T_{\max}=T(0)=T_0+\frac{qL^2}{2k}$.

**3. Flux sortant en $x=+L$.**
$$j(L)=-kT'(L)=-k\Big(-\frac qkL\Big)=qL>0.$$
Il est dirigé selon $+\vec u_x$, donc sortant. En $x=-L$, $j(-L)=-qL$, dirigé selon $-\vec u_x$ : il est aussi sortant, de norme $qL$.

**3. Conservation de l'énergie.** La puissance produite par unité de surface de paroi est celle d'une colonne de section unité et de longueur $2L$ : $q\cdot2L$. La puissance sortante totale, par unité de surface, vaut $qL+qL=2qL$. Les deux sont égales : en régime stationnaire, toute l'énergie produite est évacuée par les faces. ✓ Plus précisément, le flux en $x$ vaut $j(x)=qx$ : c'est la puissance produite entre $0$ et $x$.

**Application.** Pour un élément de combustible nucléaire, $T_{\max}-T_0=\frac{qL^2}{2k}$ doit rester inférieure à une valeur admissible (fusion, tenue des matériaux) : l'épaisseur est limitée, en $L\propto\sqrt{k/q}$.
"""

D['p-th-ccmp4'] = r"""
**1. Description qualitative.** À l'interface eau/glace, l'eau est à $T_{\mathrm{fus}}$ et peut geler. Pour solidifier une épaisseur $\mathrm de$, il faut évacuer la chaleur latente correspondante. Cette énergie traverse la couche de glace par conduction, du bas (à $T_{\mathrm{fus}}$) vers le haut (à $T_c$, plus froid), puis elle est cédée à l'air. Plus la couche est épaisse, plus sa résistance thermique est grande, plus le flux évacué est faible : la croissance **ralentit**.

**2. Profil dans la glace.** En régime quasi stationnaire, la glace n'a ni source ni stockage notable, donc $\frac{\mathrm d^2T}{\mathrm dz^2}=0$ : le profil est linéaire, de $T_{\mathrm{fus}}$ (en bas) à $T_c$ (en haut). On suppose que la surface supérieure est à la température de l'air. Le flux surfacique traversant la glace vers le haut vaut
$$\varphi=\lambda_g\frac{T_{\mathrm{fus}}-T_c}{e}.$$

**2. Bilan à l'interface.** Pendant $\mathrm dt$, une épaisseur $\mathrm de$ d'eau gèle (par unité de surface, une masse $\rho_g\,\mathrm de$). Elle libère l'énergie $\rho_g\ell_{\mathrm{fus}}\,\mathrm de$, entièrement évacuée par conduction dans la glace : $\rho_g\ell_{\mathrm{fus}}\,\mathrm de=\varphi\,\mathrm dt$. Donc
$$\rho_g\ell_{\mathrm{fus}}\frac{\mathrm de}{\mathrm dt}=\lambda_g\frac{T_{\mathrm{fus}}-T_c}e.$$

**2. Intégration.** On sépare les variables : $e\,\mathrm de=K\,\mathrm dt$, avec $K=\frac{\lambda_g(T_{\mathrm{fus}}-T_c)}{\rho_g\ell_{\mathrm{fus}}}$. En intégrant de $0$ à $t$, avec $e(0)=e_0$ : $\frac{e^2-e_0^2}2=Kt$, d'où
$$e(t)=\sqrt{e_0^2+\frac{2\lambda_g(T_{\mathrm{fus}}-T_c)}{\rho_g\ell_{\mathrm{fus}}}t}.$$

**3. Allure.** Avec $e_0=0$ : $e=\sqrt{2Kt}\propto\sqrt t$. La courbe est concave, avec une pente infinie en $t=0$ : la croissance est d'abord rapide, puis de plus en plus lente. Cette loi en $\sqrt t$ est la signature d'un processus limité par la diffusion.

**3. Ordre de grandeur.** $\lambda_g\approx2{,}2\ \mathrm{W\,m^{-1}\,K^{-1}}$, $T_{\mathrm{fus}}-T_c=10$ K, $\rho_g\ell_{\mathrm{fus}}\approx917\times3{,}34\times10^5\approx3{,}1\times10^8\ \mathrm{J\,m^{-3}}$ :
$$2K\approx\frac{2\times2{,}2\times10}{3{,}1\times10^8}\approx1{,}4\times10^{-7}\ \mathrm{m^2\,s^{-1}}.$$
En un jour, $e\approx\sqrt{1{,}4\times10^{-7}\times86\,400}\approx11$ cm ; en dix jours, environ 35 cm seulement (le temps a été multiplié par 10, l'épaisseur par $\sqrt{10}$).

**3. Validité.** L'approximation quasi stationnaire suppose que la chaleur sensible de la glace est négligeable devant la chaleur latente : $c_g(T_{\mathrm{fus}}-T_c)\approx2\times10^4\ \mathrm{J\,kg^{-1}}\ll\ell_{\mathrm{fus}}=3{,}3\times10^5\ \mathrm{J\,kg^{-1}}$. ✓ On a aussi négligé la résistance thermique de l'échange glace/air (convection), qui ralentirait la croissance au début.
"""

D['p-th-ccmp15'] = r"""
**1. Loi de Fourier.**
$$\vec j_{th}=-\lambda\,\overrightarrow{\mathrm{grad}}\,T.$$
- $\vec j_{th}$ est la densité de flux thermique, en $\mathrm{W\,m^{-2}}$ ;
- $\lambda$ est la conductivité thermique, en $\mathrm{W\,m^{-1}\,K^{-1}}$ ;
- le gradient s'exprime en $\mathrm{K\,m^{-1}}$.

Le signe $-$ traduit le fait que la chaleur va du chaud vers le froid.

**2. Hypothèses.** Régime permanent (température du phoque stable) ; cylindre long ($L\gg R_e$), donc transfert radial et extrémités négligées ; pas de production de chaleur dans la graisse ; production $P$ entièrement dans le cœur.

**2. Flux à travers un cylindre.** Pour $r\in[R_i,R_e]$, considérons le volume compris entre le cœur et le cylindre de rayon $r$. En régime permanent, toute la puissance produite par le cœur traverse ce cylindre :
$$P=j(r)\cdot2\pi rL=-\lambda\frac{\mathrm dT}{\mathrm dr}2\pi rL\quad\Longrightarrow\quad\frac{\mathrm dT}{\mathrm dr}=-\frac P{2\pi\lambda rL}.$$

**3. Intégration.** De $R_i$ (où $T=T_i$) à $R_e$ (où $T=T_e$) :
$$T_e-T_i=-\frac P{2\pi\lambda L}\ln\frac{R_e}{R_i}\iff T_i-T_e=\frac P{2\pi\lambda L}\ln\Big(1+\frac{\Delta R}{R_i}\Big).$$

**3. Couche mince.** Si $\Delta R\ll R_i$, $\ln\big(1+\frac{\Delta R}{R_i}\big)\approx\frac{\Delta R}{R_i}$, d'où $T_i-T_e\approx\frac{P\,\Delta R}{2\pi\lambda LR_i}$ (mur plan de surface $2\pi R_iL$).

**3. Production métabolique.** $P=\alpha M$, avec la masse du cœur $M=\rho\pi R_i^2L$ (la graisse est négligée dans la masse). Donc
$$T_i-T_e=\frac{\alpha\rho\pi R_i^2L\,\Delta R}{2\pi\lambda LR_i}=\frac{\alpha\rho R_i\,\Delta R}{2\lambda}.$$

**3. Taille minimale.** L'écart $T_i-T_e$ que l'animal peut maintenir croît avec $R_i$ : la production croît comme le volume ($R_i^2$), et les pertes comme la surface ($R_i$). Pour maintenir $T_i-T_e=33$ K avec une couche de graisse $\Delta R$ donnée, il faut
$$R_i\ge R_{\min}=\frac{2\lambda(T_i-T_e)}{\alpha\rho\,\Delta R}.$$

**3. Application numérique.** Avec $\lambda\approx0{,}2\ \mathrm{W\,m^{-1}\,K^{-1}}$, $\alpha\approx2\ \mathrm{W\,kg^{-1}}$, $\rho\approx10^3\ \mathrm{kg\,m^{-3}}$ et $\Delta R=5$ cm :
$$R_{\min}=\frac{2\times0{,}2\times33}{2\times10^3\times0{,}05}=\frac{13{,}2}{100}\approx0{,}13\ \mathrm m.$$
Un mammifère marin doit avoir un rayon d'au moins une dizaine de centimètres (en fait davantage, car l'hypothèse $\Delta R\ll R_i$ n'est qu'à peine vérifiée ici, et la convection de l'eau augmente les pertes). Il n'existe pas de mammifère marin de la taille d'une souris.

**4. Commentaires.**
- C'est la loi d'échelle « surface/volume » : un petit animal perd relativement plus de chaleur.
- Les petits animaux des régions froides compensent par un métabolisme plus intense ($\alpha$ plus grand) ou un meilleur isolant (fourrure, plumes : $\lambda$ plus petit).
- Limites du modèle : géométrie idéalisée, conduction pure dans la graisse, circulation sanguine (que le phoque peut réguler) et échange convectif avec l'eau négligés.
"""

D['p-chim-ccs6'] = r"""
**1. Réaction.** $\mathrm{H_3O^+}+\mathrm{HO^-}\to2\,\mathrm{H_2O}$, de constante $K=\frac1{K_e}=10^{14}$ à 25 °C : elle est quasi totale.

**1. Avancement.** Les quantités initiales sont $n(\mathrm{H_3O^+})=c_0V_0$ et $n(\mathrm{HO^-})=c_0V_s$.
- Pour $V_s\le V_0$, la soude ajoutée est limitante : $\xi=c_0V_s$.
- Pour $V_s\ge V_0$, l'acide est épuisé : $\xi=c_0V_0$ (constant).

**2. Signe.** On observe $T(V_s)>T_0$ dans un calorimètre (adiabatique) : la réaction libère de l'énergie thermique, qui échauffe le contenu. Elle est **exothermique** : $\Delta_rH<0$.

**3. Bilan enthalpique.** La transformation est adiabatique et monobare, sans autre travail que celui des forces de pression : $\Delta H=Q_P=0$. $H$ étant une fonction d'état, on décompose en deux étapes fictives :
- la réaction, à $T_0$ et $P$ constantes, d'avancement $\xi$ : $\Delta H_1=\xi\,\Delta_rH$ ;
- l'échauffement de tout le contenu (solution et calorimètre) de $T_0$ à $T(V_s)$ : $\Delta H_2=\Delta H_{\mathrm{temp}}=\big(m(V_s)+m_{eq}\big)c_{\mathrm{eau}}\big(T(V_s)-T_0\big)$.

**3. Expression de $\Delta_rH$.** $\Delta H_1+\Delta H_2=0$, avec $m(V_s)=\rho(V_0+V_s)$ (solutions diluées, assimilées à de l'eau, de capacité $c_{\mathrm{eau}}$). Pour $V_s\le V_0$ :
$$\Delta_rH=-\frac{\big(\rho(V_0+V_s)+m_{eq}\big)c_{\mathrm{eau}}\,\Delta T}{c_0V_s},\qquad\Delta T=T(V_s)-T_0.$$
On suppose que la soude ajoutée est aussi à $T_0$. On attend $\Delta_rH\approx-57\ \mathrm{kJ\,mol^{-1}}$.

**3. Ordre de grandeur.** Pour $V_0=V_s=100$ mL, $c_0=1\ \mathrm{mol\,L^{-1}}$ et $m_{eq}$ négligeable : $\Delta T=\frac{0{,}1\times57\times10^3}{0{,}2\times4180}\approx6{,}8$ K, facilement mesurable.

**Remarque : titrage thermométrique.** Avant l'équivalence, chaque ajout fait réagir de l'acide et la température monte. Après l'équivalence, la soude ajoutée ne réagit plus et dilue le mélange : la température stagne ou baisse légèrement. Le maximum (le changement de pente) de $T(V_s)$ repère l'équivalence.
"""

D['p-ccs-bulle'] = r"""
**1. Masse volumique du $\mathrm{CO_2}$.** Pour un gaz parfait, $\rho_{\mathrm{CO_2}}=\frac{PM}{RT}=\frac{1{,}0\times10^5\times44\times10^{-3}}{8{,}314\times293}=\frac{4400}{2436}\approx1{,}8\ \mathrm{kg\,m^{-3}}$.

**1. Comparaison.** Pour une bulle de volume $V$ :
$$\frac{\text{poids}}{\text{poussée}}=\frac{\rho_{\mathrm{CO_2}}Vg}{\rho_cVg}=\frac{1{,}8}{1{,}0\times10^3}\approx1{,}8\times10^{-3}.$$
Le poids est environ 550 fois plus faible que la poussée d'Archimède : on le néglige.

**2. Équation du mouvement.** On applique le principe fondamental à la bulle (masse $m=\rho_{\mathrm{CO_2}}V$, $V=\frac43\pi r^3$, rayon supposé constant), dans le référentiel du verre, galiléen. Avec $\vec u_z$ vers le haut, elle subit la poussée $\rho_cVg\,\vec u_z$ et la traînée de Stokes $-6\pi\eta r\vec v$ :
$$m\frac{\mathrm d\vec v}{\mathrm dt}=\rho_cVg\,\vec u_z-6\pi\eta r\,\vec v.$$
Sur $\vec u_z$ : $\frac{\mathrm dv}{\mathrm dt}+\frac v\tau=\frac{v_{\lim}}\tau$.

**3. Vitesse limite.** En régime permanent, la poussée équilibre la traînée : $\rho_c\frac43\pi r^3g=6\pi\eta rv_{\lim}$, donc
$$v_{\lim}=\frac{2\rho_cgr^2}{9\eta}.$$

**3. Temps caractéristique.**
$$\tau=\frac m{6\pi\eta r}=\frac{\rho_{\mathrm{CO_2}}\frac43\pi r^3}{6\pi\eta r}=\frac{2\rho_{\mathrm{CO_2}}r^2}{9\eta}.$$
La solution, pour un départ au repos, est $v(t)=v_{\lim}\big(1-e^{-t/\tau}\big)$.

**3. Applications numériques** (bulle de rayon $r=0{,}25$ mm) :
$$v_{\lim}=\frac{2\times10^3\times9{,}81\times(2{,}5\times10^{-4})^2}{9\times1{,}3\times10^{-3}}=\frac{1{,}23\times10^{-3}}{1{,}17\times10^{-2}}\approx0{,}10\ \mathrm{m\,s^{-1}},$$
$$\tau=\frac{2\times1{,}8\times6{,}25\times10^{-8}}{1{,}17\times10^{-2}}\approx2\times10^{-5}\ \mathrm s.$$
Le régime transitoire est quasi instantané : la bulle monte à vitesse limite.

**3. Critique du modèle.**
- **Masse ajoutée** : en accélérant, la bulle met en mouvement du liquide, ce qui ajoute une masse effective $\frac12\rho_cV\gg m$. On obtient alors $\tau\approx\frac{\rho_cr^2}{9\eta}\approx5$ ms, toujours très court.
- **Validité de Stokes** : le nombre de Reynolds vaut $Re=\frac{\rho_cv\,2r}\eta=\frac{10^3\times0{,}1\times5\times10^{-4}}{1{,}3\times10^{-3}}\approx40$. Il n'est pas petit devant 1 : la loi de Stokes n'est qu'un ordre de grandeur. Les bulles réelles, plus petites au départ, montent à quelques cm/s.

**4. Croissance de la bulle.** Deux effets se combinent.
- **(i) Baisse de la pression hydrostatique** en remontant : $\Delta P=\rho_cgh\approx10^3\times10\times0{,}1=10^3$ Pa, soit 1 % de $P_{\mathrm{atm}}$ pour 10 cm. L'effet sur le volume ($PV=\text{cste}$) est faible.
- **(ii) Effet dominant** : le champagne est **sursaturé en $\mathrm{CO_2}$ dissous** (la bouteille était sous environ 6 bar). Le $\mathrm{CO_2}$ dissous diffuse vers la bulle, dont la quantité de gaz augmente.

Comme $v_{\lim}\propto r^2$, la bulle accélère en grossissant : les bulles s'espacent au fil de leur montée, dans un « train » de bulles.
"""

D['p-ccs-plan'] = r"""
**1.(a) Plan infini.** Pour un plan $z=0$ de charge $\sigma$ : par symétrie, $\vec E=E(z)\vec u_z$ avec $E(-z)=-E(z)$ (tout plan perpendiculaire au plan chargé est plan de symétrie, et le plan chargé lui-même aussi). On applique le théorème de Gauss sur un cylindre de section $S$ traversant le plan, de $-z$ à $z$ : $2SE(z)=\frac{\sigma S}{\varepsilon_0}$, d'où
$$\vec E=\frac\sigma{2\varepsilon_0}\vec u_z\ (z>0),\qquad\vec E=-\frac\sigma{2\varepsilon_0}\vec u_z\ (z<0).$$

**1.(b) Couche épaisse : symétries.** Invariance par translation selon $x$ et $y$, et tout plan contenant $\vec u_z$ est plan de symétrie : $\vec E=E(z)\vec u_z$. Le plan $z=0$ est aussi plan de symétrie, donc $E(-z)=-E(z)$ et $E(0)=0$.

**1.(b) Théorème de Gauss.** On prend un cylindre de section $S$, d'axe $Oz$, entre $-z$ et $z$ ($z>0$). Le flux à travers la surface latérale est nul ($\vec E\parallel\vec u_z$). Sur chaque base, il vaut $E(z)S$, car $E(-z)\cdot(-S)=E(z)S$. Donc $\Phi=2SE(z)=\frac{Q_{\mathrm{int}}}{\varepsilon_0}$.
- **$0\le z\le\frac a2$** : $Q_{\mathrm{int}}=\rho\cdot2zS$, donc $E(z)=\frac{\rho z}{\varepsilon_0}$.
- **$z\ge\frac a2$** : $Q_{\mathrm{int}}=\rho aS$, donc $E(z)=\frac{\rho a}{2\varepsilon_0}$.

Par imparité :
$$\vec E=\frac{\rho z}{\varepsilon_0}\vec u_z\quad(|z|\le\tfrac a2),\qquad\vec E=\mathrm{sgn}(z)\frac{\rho a}{2\varepsilon_0}\vec u_z\quad(|z|\ge\tfrac a2).$$

**1.(b) Allure.** $E(z)$ est affine dans la couche (de $-\frac{\rho a}{2\varepsilon_0}$ à $+\frac{\rho a}{2\varepsilon_0}$), puis constant à l'extérieur. Il est continu en $z=\pm\frac a2$ (pas de charge surfacique). À l'extérieur, on retrouve le champ d'un plan de charge surfacique $\sigma=\rho a$.

**1.(c) Potentiel.** $E=-\frac{\mathrm dV}{\mathrm dz}$ ; on choisit $V(0)=0$.
- **Dans la couche** : $V(z)=-\int_0^z\frac{\rho z'}{\varepsilon_0}\mathrm dz'=-\frac{\rho z^2}{2\varepsilon_0}$.
- **Pour $z\ge\frac a2$** : $V(z)=V\big(\frac a2\big)-\frac{\rho a}{2\varepsilon_0}\big(z-\frac a2\big)=-\frac{\rho a^2}{8\varepsilon_0}-\frac{\rho az}{2\varepsilon_0}+\frac{\rho a^2}{4\varepsilon_0}$.

Avec la parité ($V$ est pair) :
$$V(z)=-\frac{\rho a|z|}{2\varepsilon_0}+\frac{\rho a^2}{8\varepsilon_0}\quad(|z|\ge\tfrac a2).$$
L'allure (pour $\rho>0$) est un arc de parabole renversé au centre, raccordé avec la même tangente à deux demi-droites décroissantes. $V$ est de classe $C^1$.

**2.(a) Équation du mouvement.** La force vaut $F=qE(z)$, avec $z_0=\frac a4$ et une vitesse initiale nulle ; le mouvement est selon $Oz$.
- **Si $q\rho>0$** : en $z_0>0$, $F>0$, et la particule est repoussée vers l'extérieur. Elle sort de la couche en $z=\frac a2$, puis subit une force constante $\frac{q\rho a}{2\varepsilon_0}$ : mouvement uniformément accéléré, elle s'éloigne indéfiniment.
- **Si $q\rho<0$** : dans la couche, $m\ddot z=\frac{q\rho}{\varepsilon_0}z=-\frac{|q\rho|}{\varepsilon_0}z$. C'est un oscillateur harmonique de pulsation $\omega=\sqrt{\frac{|q\rho|}{m\varepsilon_0}}$. Lâchée sans vitesse en $\frac a4$, la particule oscille entre $-\frac a4$ et $\frac a4$ : $z(t)=\frac a4\cos\omega t$. Elle reste dans la couche, ce qui valide l'expression du champ utilisée.

**2.(b) Mesure de $\rho$.** Oui, si l'on connaît $\frac qm$.
- **Cas oscillant** : on mesure la période $T=\frac{2\pi}\omega$, d'où $|\rho|=\frac{4\pi^2m\varepsilon_0}{|q|T^2}$. Le sens du mouvement initial (vers le centre) donne le signe : $\rho$ est de signe opposé à $q$.
- **Cas répulsif** : la conservation de l'énergie entre $\frac a4$ et $\frac a2$ donne $\frac12mv_s^2=q\big[V\big(\frac a4\big)-V\big(\frac a2\big)\big]=\frac{q\rho}{2\varepsilon_0}\Big(\frac{a^2}4-\frac{a^2}{16}\Big)=\frac{3q\rho a^2}{32\varepsilon_0}$. La mesure de la vitesse de sortie $v_s$ donne donc $\rho$.
"""
