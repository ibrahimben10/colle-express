D = {}

D['n-p2-diffusion'] = r"""
**1. Bilan de particules.** On considère la tranche $[x,x+\mathrm dx]$, de section $S$. Le nombre de molécules de parfum qu'elle contient vaut $n(x,t)S\,\mathrm dx$. Entre $t$ et $t+\mathrm dt$, il varie uniquement par les flux entrant en $x$ et sortant en $x+\mathrm dx$ (pas de réaction chimique, donc pas de source) :
$$\frac{\partial n}{\partial t}S\,\mathrm dx\,\mathrm dt=\big[j(x,t)-j(x+\mathrm dx,t)\big]S\,\mathrm dt=-\frac{\partial j}{\partial x}\mathrm dx\,S\,\mathrm dt.$$
D'où l'équation de conservation : $\frac{\partial n}{\partial t}=-\frac{\partial j}{\partial x}$.

**1. Loi de Fick.** Le flux de particules va des zones concentrées vers les zones diluées, proportionnellement au gradient : $j=-D\frac{\partial n}{\partial x}$. En substituant ($D$ uniforme) :
$$\frac{\partial n}{\partial t}=D\frac{\partial^2n}{\partial x^2}.$$

**2. Analyse en ordres de grandeur.** On remplace $\frac{\partial n}{\partial t}$ par $\frac n\tau$ et $\frac{\partial^2n}{\partial x^2}$ par $\frac n{L^2}$. L'équation donne $\frac n\tau\sim D\frac n{L^2}$, soit
$$\tau\sim\frac{L^2}D=\frac{(5)^2}{1{,}0\times10^{-5}}=2{,}5\times10^6\ \mathrm s\approx1\ \text{mois}.$$

**2. Conclusion.** On sent pourtant un parfum à l'autre bout d'une pièce en quelques minutes : la diffusion n'est pas le mécanisme dominant. Ce sont les mouvements d'air (**convection**), même très lents, qui transportent l'odeur. Pour une vitesse $v\sim1\ \mathrm{cm\,s^{-1}}$ (courants thermiques, passage d'une personne), $\frac Lv\sim500$ s, soit environ 10 min. La diffusion n'est efficace qu'à petite échelle, car $\tau\propto L^2$ : sur 1 mm, $\tau\sim0{,}1$ s.

**3. Dérivées.** Avec $n=\frac{N_0}{\sqrt{4\pi Dt}}e^{-x^2/(4Dt)}$, on dérive par la dérivée logarithmique : $\ln n=\ln N_0-\frac12\ln(4\pi Dt)-\frac{x^2}{4Dt}$.
- Dérivée temporelle : $\frac{\partial_tn}n=-\frac1{2t}+\frac{x^2}{4Dt^2}$.
- Dérivée spatiale : $\frac{\partial_xn}n=-\frac x{2Dt}$, donc $\partial_xn=-\frac x{2Dt}n$.
- Dérivée seconde : $\partial_x^2n=-\frac1{2Dt}n-\frac x{2Dt}\partial_xn=\Big(-\frac1{2Dt}+\frac{x^2}{4D^2t^2}\Big)n$.

**3. Vérification.** $D\partial_x^2n=\Big(-\frac1{2t}+\frac{x^2}{4Dt^2}\Big)n=\partial_tn$. ✓

**3. Conservation.** Avec $\int_{-\infty}^{+\infty}e^{-x^2/(4Dt)}\mathrm dx=\sqrt{4\pi Dt}$, on obtient $\int n\,\mathrm dx=N_0$ à tout instant : le nombre de molécules se conserve.

**3. Interprétation.** C'est une gaussienne de variance $\sigma^2=2Dt$ (on l'identifie à $e^{-x^2/(2\sigma^2)}$). La largeur $\sqrt{2Dt}$ est la distance typique parcourue par les molécules. Elle croît comme $\sqrt t$, alors qu'elle croîtrait comme $t$ pour un transport à vitesse constante. C'est la signature d'une **marche au hasard** : chaque molécule subit des chocs incessants qui changent sa direction (mouvement brownien). Pour aller deux fois plus loin, il faut quatre fois plus de temps.
"""

D['n-p3-neutron'] = r"""
**1. Confinement.** Le principe de Pauli interdit à deux neutrons (fermions) d'occuper le même état. Ils ne peuvent pas tous s'entasser dans l'état de plus basse énergie : chacun dispose en moyenne d'un volume $\frac{R^3}N$, de taille linéaire $\Delta x\sim\frac R{N^{1/3}}$.

**1. Énergie cinétique.** L'inégalité de Heisenberg donne $p\sim\Delta p\gtrsim\frac\hbar{\Delta x}=\frac{\hbar N^{1/3}}R$. Dans l'approximation non relativiste :
$$\varepsilon_c\sim\frac{p^2}{m_n}\sim\frac{\hbar^2N^{2/3}}{m_nR^2},\qquad E_c\sim N\varepsilon_c=\frac{\hbar^2N^{5/3}}{m_nR^2}.$$
C'est l'énergie de **dégénérescence** : elle existe même à température nulle, et elle augmente quand on comprime l'étoile ($\propto R^{-2}$). Elle se traduit par une pression qui s'oppose à l'effondrement.

**2. Énergie de gravitation.** Pour une boule homogène, $E_p=-\frac35\frac{\mathcal GM^2}R$. En ordre de grandeur :
$$E_p\sim-\frac{\mathcal GM^2}R=-\frac{\mathcal Gm_n^2N^2}R.$$

**3. Minimisation.** On écrit $E(R)=\frac A{R^2}-\frac BR$, avec $A=\frac{\hbar^2N^{5/3}}{m_n}$ et $B=\mathcal Gm_n^2N^2$. Alors
$$E'(R)=-\frac{2A}{R^3}+\frac B{R^2}=0\iff R=\frac{2A}B.$$
C'est un minimum, car $E\to+\infty$ en $0$ et $E\to0^-$ en $+\infty$. En négligeant le facteur 2 :
$$R\sim\frac{\hbar^2N^{5/3}}{m_n\cdot\mathcal Gm_n^2N^2}=\frac{\hbar^2}{\mathcal Gm_n^3N^{1/3}}.$$

**3. Application numérique.**
- $N=\frac{1{,}4\times2{,}0\times10^{30}}{1{,}67\times10^{-27}}\approx1{,}7\times10^{57}$, d'où $N^{1/3}\approx1{,}2\times10^{19}$.
- $\mathcal Gm_n^3=6{,}67\times10^{-11}\times(1{,}67\times10^{-27})^3\approx3{,}1\times10^{-91}$ SI.
- $\hbar^2\approx1{,}1\times10^{-68}$ SI.

$$R\sim\frac{1{,}1\times10^{-68}}{3{,}1\times10^{-91}\times1{,}2\times10^{19}}=\frac{1{,}1\times10^{-68}}{3{,}7\times10^{-72}}\approx3\times10^3\ \mathrm m=3\ \mathrm{km}.$$

**3. Comparaison.** L'ordre de grandeur, quelques kilomètres, est le bon : 1,4 masse solaire dans une sphère de la taille d'une ville. L'écart d'un facteur 4 avec la valeur mesurée (12 km) vient des facteurs numériques négligés : $2$, $\frac35$, $(3\pi^2)^{2/3}$ dans l'énergie de Fermi, etc. On vérifie a posteriori que $p\sim\frac{\hbar N^{1/3}}R\sim4\times10^{-19}\ \mathrm{kg\,m\,s^{-1}}$ est comparable à $m_nc=5\times10^{-19}\ \mathrm{kg\,m\,s^{-1}}$ : les neutrons sont presque relativistes, à la limite de validité du modèle.

**4. Variation avec la masse.** $R\propto N^{-1/3}\propto M^{-1/3}$ : **plus l'étoile est massive, plus elle est petite**. C'est l'inverse des objets ordinaires (planètes, étoiles classiques), dont le rayon croît avec la masse. Une masse plus grande comprime davantage la matière, et il faut confiner plus fortement les neutrons pour que leur pression de dégénérescence équilibre une gravité plus intense.

**4. Masse limite.** Quand $M$ augmente, $p$ augmente jusqu'à devenir relativiste. L'énergie cinétique varie alors comme $pc\propto\frac1R$, comme la gravitation : l'équilibre n'est plus possible au-delà d'une masse limite (environ 2 à 3 masses solaires, analogue de la masse de Chandrasekhar pour les naines blanches). L'étoile s'effondre alors en **trou noir**.
"""

D['n-c-fer'] = r"""
**1. Règles de remplissage.**
- **Klechkowski** : les sous-couches se remplissent par $n+\ell$ croissant, et à $n+\ell$ égal par $n$ croissant. On obtient l'ordre $1s,2s,2p,3s,3p,4s,3d,\dots$
- **Pauli** : au plus 2 électrons (de spins opposés) par orbitale atomique, donc au plus 2 électrons pour $s$, 6 pour $p$ et 10 pour $d$.
- **Hund** : dans une sous-couche incomplète, les électrons occupent le maximum d'orbitales avec des spins parallèles.

**1. Configuration du fer.** On place 26 électrons : $1s^2$ (2), $2s^2$ (4), $2p^6$ (10), $3s^2$ (12), $3p^6$ (18), $4s^2$ (20), $3d^6$ (26).
$$\mathrm{Fe}:1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,4s^2\,3d^6=[\mathrm{Ar}]\,4s^2\,3d^6.$$

**1. Électrons de valence.** Ce sont ceux de la couche de $n$ le plus élevé ($4s$) et ceux de la sous-couche $d$ en cours de remplissage : $4s^2\,3d^6$, soit **8 électrons de valence**.

**1. Électrons célibataires.** Les 6 électrons $3d$ se répartissent dans les 5 orbitales $d$. D'après Hund, ils en occupent d'abord 5 avec des spins parallèles, puis le 6ᵉ s'apparie : **4 électrons célibataires**. L'atome de fer est paramagnétique.

**2. Position dans la classification.**
- Période : nombre quantique principal maximal, $n=4$, donc **4ᵉ période**.
- Bloc : la dernière sous-couche remplie selon Klechkowski est $3d$, donc **bloc $d$** (métal de transition).
- Colonne : pour le bloc $d$, le numéro de colonne est le nombre d'électrons $(n)s+(n-1)d$, soit $2+6=8$, donc **colonne 8**.

**3. Ions du fer.** Lors de l'ionisation des métaux de transition, ce sont les électrons $4s$ (de $n$ le plus élevé, les plus externes) qui partent en premier, avant les électrons $3d$ :
$$\mathrm{Fe^{2+}}:[\mathrm{Ar}]\,3d^6,\qquad\mathrm{Fe^{3+}}:[\mathrm{Ar}]\,3d^5.$$
(Une erreur fréquente consiste à écrire $\mathrm{Fe^{2+}}$ en $[\mathrm{Ar}]4s^23d^4$.)

**3. Stabilité de $\mathrm{Fe^{3+}}$.** La configuration $3d^5$ correspond à une sous-couche **à moitié remplie** : 5 électrons célibataires, de spins parallèles, un par orbitale $d$. Cette configuration est symétrique (densité électronique sphérique) et maximise l'énergie d'échange stabilisante entre électrons de même spin. Elle est particulièrement stable. C'est pourquoi $\mathrm{Fe^{2+}}$ ($3d^6$) s'oxyde facilement en $\mathrm{Fe^{3+}}$ par le dioxygène de l'air (la rouille contient du fer(III)).

**4. Exception du cuivre.** Klechkowski prévoit $\mathrm{Cu}:[\mathrm{Ar}]\,4s^2\,3d^9$. La configuration réelle est
$$\mathrm{Cu}:[\mathrm{Ar}]\,4s^1\,3d^{10}.$$
Un électron $4s$ passe en $3d$ pour compléter la sous-couche $3d$, ce qui est plus stable, car les niveaux $4s$ et $3d$ sont très proches en énergie. (De même, le chrome est $[\mathrm{Ar}]\,4s^1\,3d^5$, avec deux sous-couches à moitié pleines.)
"""

D['n-c-vsepr'] = r"""
**1. Méthode.** On compte les électrons de valence, on forme les liaisons, puis on complète les octets (duet pour H) avec des doublets non liants.

**1. $\mathrm{CO_2}$.** $4+2\times6=16$ électrons, soit 8 doublets. Formule $\mathrm O{=}\mathrm C{=}\mathrm O$ : deux doubles liaisons (4 doublets liants) et deux doublets non liants sur chaque oxygène. Chaque atome respecte l'octet.

**1. $\mathrm{H_2O}$.** $6+2=8$ électrons, soit 4 doublets. O est lié aux deux H par deux liaisons simples et porte **deux doublets non liants**.

**1. $\mathrm{NH_3}$.** $5+3=8$ électrons, soit 4 doublets. N est lié aux trois H et porte **un doublet non liant**.

**1. $\mathrm{BF_3}$.** $3+3\times7=24$ électrons, soit 12 doublets. B est lié aux trois F par des liaisons simples ; chaque F porte trois doublets non liants. Le bore n'est entouré que de 6 électrons : il présente une **lacune électronique**. C'est un acide de Lewis (il accepte un doublet, par exemple celui de $\mathrm{NH_3}$ pour former $\mathrm{F_3B{-}NH_3}$).

**2. Principe VSEPR.** Les doublets de la couche de valence de l'atome central (liants $X$ et non liants $E$) se repoussent et s'éloignent au maximum. Une liaison multiple compte pour une seule direction.
- **$\mathrm{CO_2}$** : $\mathrm{AX_2E_0}$, 2 directions, molécule **linéaire**, angle de $180^\circ$.
- **$\mathrm{H_2O}$** : $\mathrm{AX_2E_2}$, 4 directions, figure de répulsion tétraédrique. Seuls les atomes comptent pour la géométrie : la molécule est **coudée**, avec un angle inférieur à $109{,}5^\circ$ (mesuré : $104{,}5^\circ$).
- **$\mathrm{NH_3}$** : $\mathrm{AX_3E_1}$, figure tétraédrique, molécule **pyramidale** à base triangulaire, angle inférieur à $109{,}5^\circ$ (mesuré : $107^\circ$).
- **$\mathrm{BF_3}$** : $\mathrm{AX_3E_0}$, 3 directions, molécule **triangulaire plane**, angles de $120^\circ$.

**3. Polarité des liaisons.** Toutes les liaisons sont polarisées, car les électronégativités diffèrent : C–O ($\Delta\chi=0{,}8$), O–H ($1{,}2$), N–H ($0{,}8$), B–F ($2{,}0$). Le moment dipolaire de la molécule est la somme vectorielle des moments de liaison.

**3. Bilan.**
- $\mathrm{CO_2}$ : les deux moments C–O sont opposés (molécule linéaire, centrosymétrique), leur somme est nulle : **apolaire**.
- $\mathrm{BF_3}$ : trois moments égaux à $120^\circ$ dans un plan, leur somme est nulle : **apolaire**.
- $\mathrm{H_2O}$ : les deux moments O–H ne sont pas alignés, la somme est non nulle, dirigée selon la bissectrice : **polaire** ($\mu=1{,}85$ D).
- $\mathrm{NH_3}$ : la somme des trois moments N–H est dirigée selon l'axe de la pyramide : **polaire** ($\mu=1{,}47$ D).

La polarité dépend donc autant de la géométrie que des liaisons.

**4. Comparaison des angles.** Un doublet non liant n'est attiré que par un seul noyau : il est plus diffus, plus proche de l'atome central, et occupe plus de place que les doublets liants. Les répulsions se classent ainsi : non liant/non liant > non liant/liant > liant/liant. L'eau, avec deux doublets non liants, resserre davantage ses liaisons O–H ($104{,}5^\circ$) que l'ammoniac, qui n'en a qu'un ($107^\circ$). Le méthane, sans doublet non liant ($\mathrm{AX_4}$), a l'angle tétraédrique parfait de $109{,}5^\circ$.
"""

D['n-c-h2o2'] = r"""
**1. Test de l'ordre 1.** Si la réaction est d'ordre 1, $v=-\frac{\mathrm d[\mathrm{H_2O_2}]}{\mathrm dt}=k[\mathrm{H_2O_2}]$. On sépare les variables et on intègre :
$$\int_{c_0}^c\frac{\mathrm dc'}{c'}=-k\int_0^t\mathrm dt'\iff\ln\frac{c_0}c=kt\iff c=c_0e^{-kt}.$$
Il suffit donc de vérifier que $\ln\frac{c_0}c$ est proportionnel à $t$.

**1. Calcul.**

| $t$ (s) | 0 | 300 | 600 | 900 | 1200 |
|---|---|---|---|---|---|
| $\ln(c_0/c)$ | 0 | 0,300 | 0,600 | 0,900 | 1,20 |
| $\frac1t\ln(c_0/c)$ ($\mathrm s^{-1}$) | — | $1{,}00\times10^{-3}$ | $1{,}00\times10^{-3}$ | $1{,}00\times10^{-3}$ | $1{,}00\times10^{-3}$ |

Les points $\big(t,\ln\frac{c_0}c\big)$ sont alignés sur une droite passant par l'origine : la loi d'ordre 1 est vérifiée. La pente donne
$$k=1{,}0\times10^{-3}\ \mathrm{s^{-1}}.$$
(Pour un ordre 2, c'est $\frac1c$ qui serait affine en $t$ ; on vérifierait que ce n'est pas le cas.)

**2. Temps de demi-réaction.** $c(t_{1/2})=\frac{c_0}2$, donc $e^{-kt_{1/2}}=\frac12$ et
$$t_{1/2}=\frac{\ln2}k=\frac{0{,}693}{1{,}0\times10^{-3}}\approx693\ \mathrm s\approx12\ \mathrm{min}.$$
Il **ne dépend pas** de $c_0$ : c'est une propriété caractéristique de l'ordre 1 (pour un ordre 2, $t_{1/2}=\frac1{kc_0}$). On vérifie : entre 0 et 600 s, $c$ passe de 0,100 à 0,0549, et à 693 s il vaudrait 0,050.

**3. Quantité de $\mathrm{H_2O_2}$ décomposée** à 600 s, dans $V=1{,}0$ L :
$$\Delta n(\mathrm{H_2O_2})=(0{,}100-0{,}0549)\times1{,}0=0{,}0451\ \mathrm{mol}.$$

**3. Quantité de $\mathrm O_2$.** D'après la stœchiométrie ($2\,\mathrm{H_2O_2}\to\mathrm O_2$), $n(\mathrm O_2)=\frac{\Delta n(\mathrm{H_2O_2})}2=0{,}0226$ mol.

**3. Volume.** Pour un gaz parfait à $T=298$ K et $P=1{,}0\times10^5$ Pa :
$$V(\mathrm O_2)=\frac{nRT}P=\frac{0{,}0226\times8{,}31\times298}{1{,}0\times10^5}\approx5{,}6\times10^{-4}\ \mathrm{m^3}=0{,}56\ \mathrm L.$$
(Le volume molaire vaut ici $\frac{RT}P=24{,}8\ \mathrm{L\,mol^{-1}}$.) On suppose que le dioxygène ne reste pas dissous dans la solution.
"""

D['n-c-arrhenius'] = r"""
**1. Loi d'Arrhenius.**
$$k(T)=A\exp\Big(-\frac{E_a}{RT}\Big),$$
où $A$ est le facteur préexponentiel, supposé indépendant de $T$, et $E_a$ l'énergie d'activation, c'est-à-dire la barrière énergétique à franchir.

**1. Rapport entre deux températures.** Les vitesses (à concentrations égales) sont dans le rapport des constantes de vitesse :
$$\frac{k_2}{k_1}=\exp\Big[\frac{E_a}R\Big(\frac1{T_1}-\frac1{T_2}\Big)\Big]\iff\ln\frac{k_2}{k_1}=\frac{E_a}R\Big(\frac1{T_1}-\frac1{T_2}\Big).$$

**1. Calcul de $E_a$.** $T_1=298$ K, $T_2=308$ K et $\frac{k_2}{k_1}=2$. On a $\frac1{T_1}-\frac1{T_2}=\frac{T_2-T_1}{T_1T_2}=\frac{10}{298\times308}=1{,}09\times10^{-4}\ \mathrm{K^{-1}}$. Donc
$$E_a=\frac{R\ln2}{\frac1{T_1}-\frac1{T_2}}=\frac{8{,}31\times0{,}693}{1{,}09\times10^{-4}}\approx5{,}3\times10^4\ \mathrm{J\,mol^{-1}}=53\ \mathrm{kJ\,mol^{-1}}.$$
C'est une valeur typique des réactions biochimiques et de nombreuses réactions organiques.

**2. Entre 25 et 60 °C.** $T_3=333$ K, $\frac1{298}-\frac1{333}=\frac{35}{298\times333}=3{,}53\times10^{-4}\ \mathrm{K^{-1}}$ et $\frac{E_a}R=\frac{53\times10^3}{8{,}31}=6{,}4\times10^3$ K. Donc
$$\ln\frac{k_{333}}{k_{298}}=6{,}4\times10^3\times3{,}53\times10^{-4}\approx2{,}24,\qquad\frac{k_{333}}{k_{298}}=e^{2{,}24}\approx9{,}4.$$
Vérification avec la règle empirique : 35 °C d'écart, c'est 3,5 fois 10 °C, d'où $2^{3{,}5}\approx11$. L'ordre de grandeur est cohérent, la règle n'étant qu'approchée (le facteur diminue un peu quand $T$ augmente).

**3. Au réfrigérateur.** $T=277$ K, $\frac1{277}-\frac1{298}=\frac{21}{277\times298}=2{,}54\times10^{-4}\ \mathrm{K^{-1}}$. Donc
$$\ln\frac{k_{298}}{k_{277}}=6{,}4\times10^3\times2{,}54\times10^{-4}\approx1{,}62,\qquad\frac{k_{298}}{k_{277}}=e^{1{,}62}\approx5.$$

**3. Interprétation.** Les réactions de dégradation (oxydation des graisses, réactions enzymatiques) et la multiplication des micro-organismes, dont le métabolisme suit une loi voisine, sont environ **5 fois plus lentes** à 4 °C qu'à 25 °C : un aliment se conserve environ 5 fois plus longtemps. Au congélateur ($-18$ °C), le ralentissement est encore beaucoup plus important, et l'eau gelée bloque en plus la croissance microbienne.
"""
