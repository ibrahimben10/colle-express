D = {}

D['n-p1-puits'] = r"""
**1. Équation de Schrödinger.** Dans le puits ($0<x<L$), $V=0$ :
$$-\frac{\hbar^2}{2m_e}\varphi''=E\varphi\iff\varphi''+k^2\varphi=0,\qquad k=\frac{\sqrt{2m_eE}}\hbar.$$
Hors du puits, $V=+\infty$ : la particule ne peut pas s'y trouver, donc $\varphi=0$. La continuité de $\varphi$ impose $\varphi(0)=\varphi(L)=0$.

**1. Solutions.** (On vérifie que $E\le0$ ne donne que la solution nulle.) La solution générale est $\varphi=A\sin kx+B\cos kx$.
- $\varphi(0)=0$ donne $B=0$.
- $\varphi(L)=0$ donne $A\sin kL=0$. Comme $A\neq0$ (sinon $\varphi\equiv0$), $\sin kL=0$, soit $k_n=\frac{n\pi}L$, $n\in\mathbb N^*$.

**1. Normalisation.**
$$\int_0^LA^2\sin^2\frac{n\pi x}L\,\mathrm dx=A^2\frac L2=1\quad\Longrightarrow\quad\varphi_n(x)=\sqrt{\frac2L}\sin\frac{n\pi x}L.$$

**1. Énergies.** Avec $\hbar=\frac h{2\pi}$ :
$$E_n=\frac{\hbar^2k_n^2}{2m_e}=\frac{\hbar^2\pi^2n^2}{2m_eL^2}=\frac{n^2h^2}{8m_eL^2}.$$
L'énergie est quantifiée (une onde stationnaire doit « tenir » dans le puits : $L=n\frac{\lambda_n}2$), et le niveau fondamental n'est pas nul ($n\ge1$) : c'est l'énergie de confinement.

**2. Application numérique.**
$$E_1=\frac{(6{,}63\times10^{-34})^2}{8\times9{,}11\times10^{-31}\times(5{,}0\times10^{-10})^2}=\frac{4{,}40\times10^{-67}}{1{,}82\times10^{-48}}\approx2{,}4\times10^{-19}\ \mathrm J\approx1{,}5\ \mathrm{eV}.$$

**3. Transition $1\to2$.** $\Delta E=E_2-E_1=(4-1)E_1=3E_1\approx4{,}5$ eV. Le photon absorbé a la longueur d'onde
$$\lambda=\frac{hc}{\Delta E}=\frac{1240}{4{,}5}\approx275\ \mathrm{nm},$$
dans l'ultraviolet.

**3. Remarque.** $\Delta E\propto\frac1{L^2}$, donc $\lambda\propto L^2$ : pour une chaîne plus longue, $\lambda$ augmente. Les longues chaînes conjuguées (carotène, environ 2 nm) absorbent dans le visible : elles sont colorées.

**4. Estimation par Heisenberg.** L'électron est localisé dans le puits : $\Delta x\sim L$. L'inégalité de Heisenberg donne $\Delta p\gtrsim\frac\hbar L$. Comme $\langle p\rangle=0$ (pas de direction privilégiée), $\langle p^2\rangle=\Delta p^2$, d'où
$$E\sim\frac{\Delta p^2}{2m_e}\gtrsim\frac{\hbar^2}{2m_eL^2}=\frac{(1{,}055\times10^{-34})^2}{2\times9{,}11\times10^{-31}\times2{,}5\times10^{-19}}\approx2{,}4\times10^{-20}\ \mathrm J\approx0{,}15\ \mathrm{eV}.$$
On obtient un ordre de grandeur correct, inférieur d'un facteur $\pi^2\approx10$ à la valeur exacte, ce qui est normal pour une estimation. Le confinement impose une énergie cinétique minimale.
"""

D['n-p1-chute'] = r"""
**1.(a) Bilan des forces.** Axe vertical descendant $\vec u_z$. La bille subit son poids $mg\vec u_z$ et le frottement $-\alpha\vec v$ ; la poussée d'Archimède est négligée. Le mouvement est vertical (vitesse initiale nulle), et le principe fondamental, projeté sur $\vec u_z$, donne
$$m\frac{\mathrm dv}{\mathrm dt}=mg-\alpha v\iff\frac{\mathrm dv}{\mathrm dt}+\frac v\tau=g,\qquad\tau=\frac m\alpha.$$

**1.(a) Résolution.** Solution particulière constante : $v_\ell=g\tau=\frac{mg}\alpha$ (vitesse pour laquelle le frottement équilibre le poids). La solution générale est $v=v_\ell+Ae^{-t/\tau}$, et $v(0)=0$ donne $A=-v_\ell$ :
$$v(t)=v_\ell\big(1-e^{-t/\tau}\big),\qquad v_\ell=\frac{mg}\alpha.$$

**1.(a) Valeurs.** $\tau=\frac{2{,}0\times10^{-3}}{1{,}0\times10^{-2}}=0{,}20$ s et $v_\ell=\frac{2{,}0\times10^{-3}\times9{,}8}{1{,}0\times10^{-2}}\approx2{,}0\ \mathrm{m\,s^{-1}}$.

**1.(b) Durée pour 95 %.** $v=0{,}95v_\ell$ équivaut à $e^{-t/\tau}=0{,}05$, donc
$$t_{95}=\tau\ln20\approx3{,}0\,\tau\approx0{,}60\ \mathrm s.$$
En pratique, au-delà de quelques $\tau$, la bille tombe à vitesse constante $v_\ell$.

**2.(a) Vitesse limite du parachutiste.** Au régime limite, l'accélération est nulle et le frottement équilibre le poids : $kv_\ell^2=mg$. Donc
$$k=\frac{mg}{v_\ell^2}=\frac{80\times9{,}8}{55^2}=\frac{784}{3025}\approx0{,}26\ \mathrm{kg\,m^{-1}}.$$
Vérification d'unité : $kv^2$ en $\mathrm{kg\,m^{-1}\times m^2\,s^{-2}}=\mathrm N$. ✓

**2.(b) Parachute ouvert.** Le poids ne change pas, donc $k'v_\ell'^2=kv_\ell^2$, et
$$\frac{k'}k=\Big(\frac{v_\ell}{v_\ell'}\Big)^2=\Big(\frac{55}{5{,}0}\Big)^2=121\approx120.$$
Interprétation : $k=\frac12\rho C_xS$ ($\rho$ masse volumique de l'air, $C_x$ coefficient de traînée, $S$ surface frontale). Le parachute multiplie surtout la surface frontale, d'environ $0{,}7\ \mathrm{m^2}$ pour le corps à plusieurs dizaines de $\mathrm{m^2}$, et augmente aussi le $C_x$. L'arrivée à $5\ \mathrm{m\,s^{-1}}$ équivaut à un saut d'environ 1,3 m de haut.
"""

D['n-p1-geostat'] = r"""
**1. Mouvement uniforme.** Dans le référentiel géocentrique (galiléen), la seule force est l'attraction terrestre, centrale (dirigée vers $O$). Pour un mouvement circulaire de rayon $r$, l'accélération vaut $\vec a=\frac{\mathrm dv}{\mathrm dt}\vec u_\theta-\frac{v^2}r\vec u_r$. La projection du principe fondamental sur $\vec u_\theta$ donne $m\frac{\mathrm dv}{\mathrm dt}=0$ : le mouvement est **uniforme**.

**1. Vitesse.** Projection sur $\vec u_r$ :
$$m\frac{v^2}r=\frac{\mathcal GM_Tm}{r^2}\quad\Longrightarrow\quad v=\sqrt{\frac{\mathcal GM_T}r}.$$
Plus le satellite est haut, plus il est lent.

**1. Troisième loi de Kepler.** La période vaut $T=\frac{2\pi r}v=2\pi\sqrt{\frac{r^3}{\mathcal GM_T}}$, d'où
$$\frac{T^2}{r^3}=\frac{4\pi^2}{\mathcal GM_T}.$$

**2. Période.** Pour rester à la verticale d'un point de la Terre, le satellite doit tourner dans le même sens et à la même vitesse angulaire que la Terre dans le référentiel géocentrique. Sa période est donc le **jour sidéral**, $T_s=86\,164$ s (et non 86 400 s, qui correspond au jour solaire). Il doit aussi être dans le plan équatorial : le plan de l'orbite contient $O$, et le satellite ne peut rester au-dessus d'un même parallèle que si c'est l'équateur.

**2. Rayon.**
$$r=\Big(\frac{\mathcal GM_TT_s^2}{4\pi^2}\Big)^{1/3}=\Big(\frac{3{,}99\times10^{14}\times(86\,164)^2}{39{,}5}\Big)^{1/3}=\big(7{,}50\times10^{22}\big)^{1/3}\approx4{,}22\times10^7\ \mathrm m.$$

**2. Altitude et vitesse.** $h=r-R_T\approx42\,200-6\,370\approx35\,800$ km, et
$$v=\frac{2\pi r}{T_s}=\frac{2\pi\times4{,}22\times10^7}{86\,164}\approx3{,}07\times10^3\ \mathrm{m\,s^{-1}}.$$

**3. Énergie mécanique.** On a $E_c=\frac12mv^2=\frac{\mathcal GM_Tm}{2r}$ (question 1) et $E_p=-\frac{\mathcal GM_Tm}r$, donc
$$E_m=E_c+E_p=-\frac{\mathcal GM_Tm}{2r}=-E_c.$$
$E_m<0$ (état lié) et croît avec $r$ : monter coûte de l'énergie, même si la vitesse diminue.

**3. Énergie à fournir.** $r_1=6370+300=6670$ km et $r_2=42\,200$ km :
$$\Delta E=E_m(r_2)-E_m(r_1)=\frac{\mathcal GM_Tm}2\Big(\frac1{r_1}-\frac1{r_2}\Big)=\frac{3{,}99\times10^{14}\times10^3}2\big(1{,}499\times10^{-7}-0{,}237\times10^{-7}\big)\approx2{,}5\times10^{10}\ \mathrm J.$$
C'est le minimum théorique, soit environ 25 GJ par tonne. En pratique, il faut bien davantage, car le carburant doit aussi accélérer sa propre masse.
"""

D['n-p1-pendule'] = r"""
**1. Conservation de l'énergie.** La tension du fil est perpendiculaire à la vitesse (trajectoire circulaire) : elle ne travaille pas. Le poids est conservatif et il n'y a pas de frottement : l'énergie mécanique se conserve. On prend l'origine de l'énergie potentielle au point le plus bas. La hauteur de départ vaut $h=L(1-\cos\theta_0)$, d'où
$$\frac12mv^2=mgL(1-\cos\theta_0)\quad\Longrightarrow\quad v=\sqrt{2gL(1-\cos\theta_0)}.$$
Avec $\cos60^\circ=\frac12$ : $v=\sqrt{gL}=\sqrt{9{,}8\times1{,}0}\approx3{,}1\ \mathrm{m\,s^{-1}}$.

**2. Tension au point bas.** En ce point, le mouvement est circulaire de rayon $L$, et l'accélération normale vaut $\frac{v^2}L$, dirigée vers le point de suspension (vers le haut). Le principe fondamental, projeté sur la verticale ascendante, donne
$$T-mg=m\frac{v^2}L.$$
Avec $v^2=2gL(1-\cos\theta_0)$ :
$$T=mg+2mg(1-\cos\theta_0)=mg(3-2\cos\theta_0)=mg(3-1)=2mg.$$
Le fil supporte **le double du poids** : la tension doit fournir, en plus de l'opposé du poids, la force centripète.

**3. Équation du mouvement.** On projette le principe fondamental sur $\vec u_\theta$ (tangente) ; la tension, radiale, n'intervient pas. L'accélération tangentielle vaut $L\ddot\theta$, d'où
$$mL\ddot\theta=-mg\sin\theta\iff\ddot\theta+\frac gL\sin\theta=0.$$

**3. Petites oscillations.** Pour $|\theta|\ll1$, $\sin\theta\approx\theta$ : on obtient $\ddot\theta+\omega_0^2\theta=0$, avec $\omega_0=\sqrt{\frac gL}$, d'où
$$T_0=2\pi\sqrt{\frac Lg}=2\pi\sqrt{\frac{1{,}0}{9{,}8}}\approx2{,}0\ \mathrm s.$$

**3. Validité.** $\theta_0=60^\circ=1{,}05$ rad n'est pas petit : $\sin\theta_0=0{,}866$ alors que $\theta_0=1{,}047$, soit 20 % d'écart. L'oscillateur n'est plus harmonique (non-isochronisme). La formule de Borda, $T\approx T_0\big(1+\frac{\theta_0^2}{16}\big)=T_0(1+0{,}069)$, montre que la période réelle est plus grande d'environ 7 %, soit environ 2,15 s.

**4. Condition au sommet.** Pour que la masse fasse un tour complet fil tendu, il faut $T\ge0$ en tout point, et la condition la plus contraignante est au sommet ($\theta=\pi$). Là, la tension et le poids sont tous deux dirigés vers le centre :
$$T+mg=m\frac{v_h^2}L,\qquad T\ge0\iff v_h^2\ge gL.$$

**4. Vitesse minimale en bas.** La conservation de l'énergie entre le bas et le sommet (dénivelé $2L$) donne $v_b^2=v_h^2+4gL$. Donc
$$v_b^2\ge5gL\iff v_b\ge\sqrt{5gL}=\sqrt{49}=7{,}0\ \mathrm{m\,s^{-1}}.$$
Si $\sqrt{2gL}<v_b<\sqrt{5gL}$, le fil se détend avant le sommet, et la masse décrit une parabole.
"""

D['n-p1-rails'] = r"""
**0. Paramétrage.** Les rails sont selon $\vec u_x$, la barre est parallèle à $\vec u_y$ (abscisse $x$, vitesse $v=\dot x$), et $\vec B=B\vec u_z$. Le circuit (résistor, rails, barre) délimite un rectangle d'aire $\ell x$, qui croît quand la barre s'éloigne du résistor. On oriente le circuit de sorte que sa normale soit $+\vec u_z$ ; le sens positif de $i$ dans la barre est alors $+\vec u_y$.

**1. Flux et f.é.m.** Le flux à travers le circuit vaut $\Phi=B\ell x$. Par la loi de Faraday :
$$e=-\frac{\mathrm d\Phi}{\mathrm dt}=-B\ell v.$$

**1. Intensité.** Sans auto-induction, la seule résistance est $R$, et $Ri=e$, donc
$$i=-\frac{B\ell v}R.$$
Pour $v>0$, on a $i<0$ : le courant circule en sens opposé à l'orientation choisie, ce qui crée un champ propre qui s'oppose à l'augmentation du flux (loi de Lenz).

**2. Force de Laplace.** Sur la barre de longueur $\ell$, parcourue par $i$ selon $\vec u_y$ :
$$\vec F=i\ell\,\vec u_y\wedge B\vec u_z=i\ell B\,\vec u_x=-\frac{B^2\ell^2v}R\vec u_x.$$
Elle est opposée à la vitesse : c'est une force de **freinage**, de type frottement fluide, conforme à la loi de Lenz.

**2. Équation du mouvement.** Horizontalement, la seule force est la force de Laplace (pas de frottement ; poids et réaction se compensent verticalement) :
$$m\frac{\mathrm dv}{\mathrm dt}=-\frac{B^2\ell^2}Rv\iff\frac{\mathrm dv}{\mathrm dt}+\frac v\tau=0,\qquad\tau=\frac{mR}{B^2\ell^2}.$$
Donc $v(t)=v_0e^{-t/\tau}$, avec
$$\tau=\frac{0{,}020\times0{,}10}{(0{,}50)^2\times(0{,}10)^2}=\frac{2{,}0\times10^{-3}}{2{,}5\times10^{-3}}=0{,}80\ \mathrm s.$$

**3. Distance parcourue.**
$$d=\int_0^{+\infty}v\,\mathrm dt=v_0\int_0^{+\infty}e^{-t/\tau}\,\mathrm dt=v_0\tau=1{,}0\times0{,}80=0{,}80\ \mathrm m.$$
La vitesse tend vers 0 sans s'annuler, mais la distance totale reste finie.

**4. Bilan énergétique.** L'énergie dissipée par effet Joule vaut
$$W_J=\int_0^{+\infty}Ri^2\,\mathrm dt=\frac{B^2\ell^2}R\int_0^{+\infty}v_0^2e^{-2t/\tau}\,\mathrm dt=\frac{B^2\ell^2v_0^2}R\cdot\frac\tau2=\frac12mv_0^2=\frac12\times0{,}020\times1{,}0^2=10\ \mathrm{mJ}.$$
Toute l'énergie cinétique initiale est convertie en énergie thermique dans le résistor.

**4. Couplage électromécanique.** À chaque instant, la puissance de la force de Laplace, $Fv=-\frac{B^2\ell^2v^2}R$, est exactement l'opposée de la puissance fournie par la f.é.m., $ei=\frac{B^2\ell^2v^2}R=Ri^2$. L'énergie mécanique perdue est intégralement transformée en énergie électrique, puis dissipée. C'est le principe du frein électromagnétique (ralentisseurs de poids lourds).
"""

D['n-p1-transfo'] = r"""
**1. Loi de Faraday.** Le flux $\varphi$ du champ magnétique à travers une spire est le même pour toutes les spires (circuit magnétique fermé, sans fuite). Les enroulements ont une résistance négligeable ; en convention récepteur au primaire et générateur au secondaire, avec des sens d'enroulement adaptés :
$$u_1=N_1\frac{\mathrm d\varphi}{\mathrm dt},\qquad u_2=N_2\frac{\mathrm d\varphi}{\mathrm dt}\quad\Longrightarrow\quad\frac{u_2}{u_1}=\frac{N_2}{N_1}=m.$$
$m$ est le rapport de transformation.

**1. Application numérique.** Les valeurs efficaces sont dans le même rapport :
$$m=\frac{12}{230}\approx0{,}052,\qquad\frac{N_1}{N_2}\approx19.$$
C'est un transformateur abaisseur de tension.

**2. Conservation de la puissance.** Le transformateur parfait ne stocke ni ne dissipe d'énergie : la puissance reçue au primaire est intégralement fournie au secondaire, $u_1i_1=u_2i_2$ à chaque instant. Donc
$$\frac{i_1}{i_2}=\frac{u_2}{u_1}=m\quad\Longrightarrow\quad I_1=mI_2.$$
Le côté basse tension porte le fort courant, et le côté haute tension le faible courant.

**3. Courants.** Au secondaire, $I_2=\frac{U_2}R=\frac{12}{6{,}0}=2{,}0$ A. Au primaire, $I_1=mI_2=0{,}052\times2{,}0\approx0{,}10$ A. Vérification : $P=U_2I_2=24$ W et $U_1I_1=230\times0{,}104\approx24$ W. ✓

**3. Résistance vue du primaire.** Le générateur voit la résistance
$$R'=\frac{U_1}{I_1}=\frac{U_2/m}{mI_2}=\frac R{m^2}=6{,}0\times\Big(\frac{230}{12}\Big)^2\approx2{,}2\ \mathrm{k\Omega}.$$
Le transformateur multiplie les impédances par $\frac1{m^2}$ : c'est un **adaptateur d'impédance**, utilisé par exemple pour obtenir le transfert maximal de puissance vers un haut-parleur.

**4. Transport sous haute tension.** Pour transporter une puissance $P=UI$ dans une ligne de résistance $r$, les pertes par effet Joule valent
$$P_J=rI^2=r\frac{P^2}{U^2}.$$
À puissance donnée, multiplier $U$ par 100 divise le courant par 100, et les pertes par $10^4$. Les transformateurs (qui ne fonctionnent qu'en régime variable, d'où le courant alternatif) élèvent la tension au départ des centrales, jusqu'à 400 kV, puis l'abaissent par étapes jusqu'à 230 V chez l'usager.
"""
