D = {}

D['p-th-spe3'] = r"""
**1. Changement de variable.** L'énergie volumique contenue dans une bande spectrale est la même, qu'on la repère en $\omega$ ou en $\lambda$ : $|\mathrm du|=\mathcal D(\omega)|\mathrm d\omega|=\mathcal D(\lambda)|\mathrm d\lambda|$. Avec $\omega=\frac{2\pi c}\lambda$, on a $\Big|\frac{\mathrm d\omega}{\mathrm d\lambda}\Big|=\frac{2\pi c}{\lambda^2}$. Donc
$$\mathcal D(\lambda)=\mathcal D(\omega)\frac{2\pi c}{\lambda^2}=\frac\hbar{\pi^2c^3}\Big(\frac{2\pi c}\lambda\Big)^3\frac{2\pi c}{\lambda^2}\cdot\frac1{e^{\hbar\omega/k_BT}-1}=\frac{16\pi^2\hbar c}{\lambda^5}\cdot\frac1{e^{hc/\lambda k_BT}-1}.$$
Avec $h=2\pi\hbar$, $16\pi^2\hbar c=8\pi hc$ :
$$\mathcal D(\lambda)=\frac{8\pi hc}{\lambda^5}\cdot\frac1{e^{hc/(\lambda k_BT)}-1}.$$

**2. Variable réduite.** À $T$ fixée, on pose $x=\frac{hc}{\lambda k_BT}$, donc $\frac1{\lambda^5}=\Big(\frac{k_BT}{hc}\Big)^5x^5$ et $\mathcal D=\text{cste}\times g(x)$, avec $g(x)=\frac{x^5}{e^x-1}$. Comme $x$ est une fonction décroissante de $\lambda$, le maximum de $\mathcal D(\lambda)$ correspond au maximum de $g$.

**2. Maximum.**
$$g'(x)=\frac{5x^4(e^x-1)-x^5e^x}{(e^x-1)^2}=0\iff5(e^x-1)=xe^x\iff5(1-e^{-x})=x\iff e^{-x}+0{,}2x-1=0.$$
La solution non nulle est $x_m=4{,}9651$. $g$ croît puis décroît, donc c'est bien un maximum.

**2. Loi de Wien.**
$$\lambda_{\max}T=\frac{hc}{4{,}9651\,k_B}=\frac{6{,}626\times10^{-34}\times3{,}00\times10^8}{4{,}9651\times1{,}381\times10^{-23}}\approx2{,}90\times10^{-3}\ \mathrm{m\,K}.$$
Exemples : le Soleil ($T\approx5800$ K) a $\lambda_{\max}\approx500$ nm, dans le visible ; le corps humain ($T\approx310$ K) a $\lambda_{\max}\approx9{,}4\ \mu$m, dans l'infrarouge.

**3. Dénombrement des photons.** L'énergie volumique des photons de pulsation comprise dans $[\omega,\omega+\mathrm d\omega]$ vaut $\mathrm du=\mathcal D(\omega)\,\mathrm d\omega$. Dans le volume $c\,\mathrm dt\,\mathrm dS$, l'énergie correspondante est $\mathrm du\,c\,\mathrm dt\,\mathrm dS$. Chaque photon transporte $\hbar\omega$, donc leur nombre est
$$\mathrm dN=\frac{\mathrm du\,c\,\mathrm dt\,\mathrm dS}{\hbar\omega}.$$

**4. Modèle unidimensionnel.** Les photons vont à $\pm c$ selon $\vec u_z$ avec la même probabilité (rayonnement isotrope). Parmi ceux contenus dans le cylindre de base $\mathrm dS$ et de hauteur $c\,\mathrm dt$, adjacent à la surface, seule la moitié se dirige vers l'extérieur, et tous ceux-là traversent $\mathrm dS$ pendant $\mathrm dt$. Il en sort donc $\frac{\mathrm dN}2$. En 3D, la projection des vitesses sur la normale introduit un facteur $\frac12$ supplémentaire (moyenne de $\cos\theta$ sur le demi-espace sortant), d'où $\frac{\mathrm dN}4$.

**5. Puissance émise par unité de surface.** L'énergie sortant par $\mathrm dS$ pendant $\mathrm dt$ vaut $\frac{\mathrm dN}4\hbar\omega=\frac c4\mathrm du\,\mathrm dt\,\mathrm dS$. Par unité de surface et de temps :
$$\mathrm d\mathcal P_S=\frac c4\mathcal D(\omega)\,\mathrm d\omega.$$

**5. Intégration.** On pose $x=\frac{\hbar\omega}{k_BT}$, donc $\omega=\frac{k_BT}\hbar x$ et $\mathrm d\omega=\frac{k_BT}\hbar\mathrm dx$ :
$$\mathcal P_S=\frac c4\int_0^{+\infty}\frac{\hbar\omega^3}{\pi^2c^3}\frac{\mathrm d\omega}{e^{\hbar\omega/k_BT}-1}=\frac\hbar{4\pi^2c^2}\Big(\frac{k_BT}\hbar\Big)^4\int_0^{+\infty}\frac{x^3\,\mathrm dx}{e^x-1}=\frac{k_B^4T^4}{4\pi^2c^2\hbar^3}\cdot\frac{\pi^4}{15}.$$

**5. Loi de Stefan.**
$$\mathcal P_S=\sigma T^4,\qquad\sigma=\frac{\pi^2k_B^4}{60\hbar^3c^2}\approx5{,}67\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}.$$
La puissance rayonnée croît comme $T^4$ : doubler la température multiplie le rayonnement par 16.
"""

D['p-th-spe4'] = r"""
**1. Nombre et densité de photons.** Chaque photon a l'énergie $hf$, donc
$$N=\frac U{hf},\qquad n=\frac N{a^3}=\frac U{hfa^3}.$$

**2. Photons frappant le miroir de droite.** Pendant $\mathrm dt$, un photon se dirigeant vers $+\vec u_x$ parcourt $c\,\mathrm dt$. Atteignent le miroir de droite ceux qui sont à moins de $c\,\mathrm dt$ de lui et qui vont vers la droite. Le cylindre de base $a^2$ et de longueur $c\,\mathrm dt$ contient $na^2c\,\mathrm dt$ photons, dont la moitié va vers la droite :
$$\mathrm dN=\frac12na^2c\,\mathrm dt=\frac{Uc\,\mathrm dt}{2hfa}.$$

**3. Variation de quantité de mouvement.** Un photon de fréquence $f$ a une quantité de mouvement de norme $\frac{hf}c$. La réflexion sur un miroir fixe conserve la fréquence et inverse la direction :
$$\delta\vec p=-\frac{hf}c\vec u_x-\frac{hf}c\vec u_x=-\frac{2hf}c\vec u_x.$$

**3. Force sur le miroir.** Pendant $\mathrm dt$, les photons perdent au total
$$\mathrm d\vec p=-\frac{2hf}c\vec u_x\cdot\frac{Uc\,\mathrm dt}{2hfa}=-\frac Ua\,\mathrm dt\,\vec u_x.$$
Le miroir exerce donc sur les photons la force $\frac{\mathrm d\vec p}{\mathrm dt}=-\frac Ua\vec u_x$. Par le principe des actions réciproques, les photons exercent sur le miroir la force $+\frac Ua\vec u_x$.

**3. Pression de radiation.** En divisant par l'aire $a^2$ :
$$P_r=\frac U{a\cdot a^2}=\frac U{a^3}=u.$$
Dans ce modèle 1D, la pression est égale à la densité volumique d'énergie.

**4. Cas tridimensionnel.** Les photons se répartissent également entre les trois directions de l'espace. Seule la composante normale de leur quantité de mouvement contribue à la pression, ce qui donne en moyenne un facteur $\frac13$ :
$$P=\frac{P_r}3=\frac u3.$$
C'est l'équation d'état du gaz de photons (un gaz parfait monoatomique non relativiste vérifie au contraire $P=\frac23u$).

**5. Détente adiabatique quasi statique.** Le premier principe donne $\mathrm dU=\delta Q+\delta W$, avec $\delta Q=0$ et $\delta W=-P\,\mathrm dV$ (quasi statique). Avec $U=uV=aT^4V$ et $P=\frac{aT^4}3$ (ici $a$ désigne la constante de la loi $u=aT^4$) :
$$\mathrm d(aT^4V)=4aT^3V\,\mathrm dT+aT^4\,\mathrm dV=-\frac{aT^4}3\mathrm dV.$$

**5. Intégration.** En divisant par $aT^4V$ :
$$4\frac{\mathrm dT}T+\frac{\mathrm dV}V=-\frac13\frac{\mathrm dV}V\iff\frac{\mathrm dT}T=-\frac13\frac{\mathrm dV}V\iff TV^{1/3}=\text{cste}.$$
Comme $V=\frac43\pi R^3$, $V^{1/3}\propto R$, d'où
$$RT=\text{cste}.$$
C'est l'analogue de la loi de Laplace, avec $\gamma=\frac43$ : $PV^{4/3}=\text{cste}$.

**5. Interprétation.** L'expansion de l'Univers refroidit le rayonnement en $T\propto\frac1R$. Le fond diffus cosmologique, émis à environ 3000 K (au moment où l'Univers est devenu transparent), est observé aujourd'hui à 2,7 K : l'Univers s'est dilaté d'un facteur $\frac{3000}{2{,}7}\approx1100$ depuis cette époque.
"""

D['p-th-spe5'] = r"""
**1. Relation de dispersion.** On injecte $\underline T=\underline T_ae^{i(\omega t-\underline kx)}$ dans l'équation de la chaleur. Avec $\frac{\partial}{\partial t}\to i\omega$ et $\frac{\partial^2}{\partial x^2}\to-\underline k^2$ :
$$\mu c\,i\omega+\lambda\underline k^2=0\iff\underline k^2=-i\frac{\mu c\omega}\lambda=-i\frac\omega D,\qquad D=\frac\lambda{\mu c}\ \text{(diffusivité thermique)}.$$

**2. Racines.** On écrit $-i=e^{-i\pi/2}$, donc $\underline k=\pm\sqrt{\frac\omega D}e^{-i\pi/4}=\pm\sqrt{\frac\omega D}\cdot\frac{1-i}{\sqrt2}$. La racine de partie réelle positive est
$$\underline k=\sqrt{\frac\omega{2D}}(1-i)=\frac{1-i}\delta,\qquad\delta=\sqrt{\frac{2D}\omega}=\sqrt{\frac{2\lambda}{\mu c\omega}}.$$
Ce choix correspond à une onde qui se propage vers les $x>0$ (vers l'intérieur du sol) en s'atténuant. L'autre racine donnerait une amplitude divergente en profondeur.

**3. Profondeur caractéristique.** Comme $e^{-i\underline kx}=e^{-ix/\delta}e^{-x/\delta}$, en prenant la partie réelle avec $T(0,t)=T_m+T_0\cos\omega t$ (la partie constante $T_m$ est aussi solution) :
$$T(x,t)=T_m+T_0\,e^{-x/\delta}\cos\Big(\omega t-\frac x\delta\Big).$$
C'est une onde thermique, fortement amortie : l'amplitude est divisée par $e$ sur la distance $\delta$, appelée **profondeur de pénétration** (épaisseur de peau thermique). Sa phase varie de 1 rad sur la même distance, et sa vitesse de phase vaut $v_\varphi=\omega\delta$.

**4. Diffusivité.** $D=\frac\lambda{\mu c}=\frac{0{,}500}{1000\times4200}=1{,}19\times10^{-7}\ \mathrm{m^2\,s^{-1}}$.

**4.(a) Variation journalière.** $\omega=\frac{2\pi}{86\,400}=7{,}27\times10^{-5}\ \mathrm{rad\,s^{-1}}$, donc
$$\delta=\sqrt{\frac{2\times1{,}19\times10^{-7}}{7{,}27\times10^{-5}}}=\sqrt{3{,}27\times10^{-3}}\approx5{,}7\ \mathrm{cm}.$$
L'amplitude, $10\ ^\circ$C en surface autour de $25\ ^\circ$C, vaut $10e^{-3}\approx0{,}5\ ^\circ$C à $3\delta\approx17$ cm, et $10e^{-5}\approx0{,}07\ ^\circ$C à $5\delta\approx29$ cm. Au-delà d'environ 30 cm, la température est quasi constante, égale à $25\ ^\circ$C (la moyenne journalière).

**4.(b) Variation annuelle.** $\omega=\frac{2\pi}{365\times86\,400}=1{,}99\times10^{-7}\ \mathrm{rad\,s^{-1}}$, donc
$$\delta=\sqrt{\frac{2\times1{,}19\times10^{-7}}{1{,}99\times10^{-7}}}=\sqrt{1{,}20}\approx1{,}1\ \mathrm m.$$
On a $\frac{\delta_{\mathrm{an}}}{\delta_{\mathrm{jour}}}=\sqrt{365}\approx19$. La température est quasi constante (variation inférieure à $0{,}5\ ^\circ$C) au-delà de $3\delta$ à $5\delta$, c'est-à-dire de 3 à 5 m, et elle vaut la moyenne annuelle, environ $15\ ^\circ$C.

**5. Théorie des caves.** Une cave enterrée à quelques mètres est à une température quasi constante toute l'année, égale à la moyenne annuelle (environ $15\ ^\circ$C) : elle paraît fraîche en été et tiède en hiver. Idéal pour conserver le vin. De plus, le déphasage $\frac x\delta$ vaut $\pi$ à $x=\pi\delta\approx3{,}4$ m : à cette profondeur, la faible oscillation résiduelle est en opposition de phase avec la surface (la cave est à son minimum en été). C'est l'analyse publiée par Fourier dans sa *Théorie analytique de la chaleur* (1822).
"""

D['p-th-spe6'] = r"""
**1. Bilan d'énergie.** On considère la couronne cylindrique comprise entre $r$ et $r+\mathrm dr$, de hauteur $H$. En régime permanent, son énergie interne ne varie pas, et il n'y a pas de source interne : le flux entrant à travers la surface de rayon $r$ est égal au flux sortant à travers la surface de rayon $r+\mathrm dr$,
$$\Phi(r)=\Phi(r+\mathrm dr),\qquad\Phi(r)=j(r)\cdot2\pi rH.$$
Donc $\frac{\mathrm d\Phi}{\mathrm dr}=0$ : le flux thermique total à travers un cylindre de rayon $r$ est indépendant de $r$.

**1. Équation en $T$.** Avec la loi de Fourier, $j=-\lambda\frac{\mathrm dT}{\mathrm dr}$ (transfert radial), on obtient $\Phi=-2\pi\lambda H\,r\frac{\mathrm dT}{\mathrm dr}$, et la condition $\frac{\mathrm d\Phi}{\mathrm dr}=0$ s'écrit
$$\frac{\mathrm d}{\mathrm dr}\Big(r\frac{\mathrm dT}{\mathrm dr}\Big)=0.$$
On retrouve l'équation de Laplace $\Delta T=0$ en coordonnées cylindriques.

**2. Intégration.** $r\frac{\mathrm dT}{\mathrm dr}=A$, donc $T(r)=A\ln r+B$. Les conditions aux limites $T(a_1)=T_1$ et $T(a_2)=T_2$ donnent $A=\frac{T_2-T_1}{\ln(a_2/a_1)}$ et
$$T(r)=T_1+(T_2-T_1)\frac{\ln(r/a_1)}{\ln(a_2/a_1)}.$$
Le profil est logarithmique, et non linéaire comme pour un mur plan.

**2. Densité de flux.**
$$j(r)=-\lambda\frac{\mathrm dT}{\mathrm dr}=-\lambda\frac{T_2-T_1}{r\ln(a_2/a_1)}=\frac{\lambda(T_1-T_2)}{r\ln(a_2/a_1)}.$$
Elle décroît en $\frac1r$ : le même flux se répartit sur une surface croissante.

**3. Flux total.**
$$\Phi=j(r)\cdot2\pi rH=\frac{2\pi\lambda H(T_1-T_2)}{\ln(a_2/a_1)}.$$
Il est bien indépendant de $r$, conformément au bilan de la question 1.

**3. Résistance thermique.** Par analogie avec la loi d'Ohm ($U=RI$, avec $T\leftrightarrow V$ et $\Phi\leftrightarrow I$), on définit $R_{th}=\frac{T_1-T_2}\Phi$, d'où
$$R_{th}=\frac{\ln(a_2/a_1)}{2\pi\lambda H}.$$
Elle s'exprime en $\mathrm{K\,W^{-1}}$.

**4. Limite du mur mince.** Avec $a_2=a_1+\varepsilon$, $\varepsilon\ll a_1$ : $\ln\frac{a_2}{a_1}=\ln\Big(1+\frac\varepsilon{a_1}\Big)\approx\frac\varepsilon{a_1}$. Donc
$$R_{th}\approx\frac\varepsilon{2\pi a_1H\lambda}=\frac e{\lambda S},$$
avec $e=\varepsilon$ l'épaisseur et $S=2\pi a_1H$ la surface de la paroi. On retrouve la résistance d'un mur plan : à l'échelle de son épaisseur, un mur mince est localement plan, et la courbure ne joue plus.

**Application.** C'est la formule utilisée pour calorifuger des tuyaux. Comme $R_{th}$ croît seulement en $\ln a_2$, doubler l'épaisseur d'isolant n'apporte pas un gain proportionnel.
"""
