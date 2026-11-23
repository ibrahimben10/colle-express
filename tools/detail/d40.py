D = {}

D['n-p1-adiab'] = r"""
**1. Hypothèse adiabatique.** La compression dure une fraction de tour moteur, soit quelques millisecondes. Les transferts thermiques à travers les parois, par diffusion, sont beaucoup plus lents : le temps caractéristique de diffusion dans le gaz sur quelques centimètres est de l'ordre de la seconde. Pendant la compression, le gaz n'a pas le temps d'échanger de chaleur : $Q\approx0$. Si l'on suppose en plus l'absence de frottements et de turbulences, la transformation est aussi réversible.

**2. Température finale.** La loi de Laplace en variables $(T,V)$, $TV^{\gamma-1}=\text{cste}$, donne, avec $\frac{V_1}{V_2}=10$ :
$$T_2=T_1\Big(\frac{V_1}{V_2}\Big)^{\gamma-1}=293\times10^{0{,}4}=293\times2{,}51\approx736\ \mathrm K.$$

**2. Pression finale.** La loi $PV^\gamma=\text{cste}$ donne
$$P_2=P_1\Big(\frac{V_1}{V_2}\Big)^\gamma=1{,}0\times10^{1{,}4}\approx25\ \mathrm{bar}.$$
Vérification par l'équation d'état : $\frac{P_2}{P_1}=\frac{T_2}{T_1}\cdot\frac{V_1}{V_2}=2{,}51\times10=25$. ✓

**3. Travail adiabatique.** Le premier principe avec $Q=0$ donne $W=\Delta U=nC_{v,m}(T_2-T_1)$, avec $C_{v,m}=\frac R{\gamma-1}=\frac{8{,}31}{0{,}4}=20{,}8\ \mathrm{J\,K^{-1}\,mol^{-1}}$. Par mole :
$$W_{ad}=20{,}8\times(736-293)=20{,}8\times443\approx9{,}2\ \mathrm{kJ\,mol^{-1}}.$$

**3. Travail isotherme.** À température constante $T_1$, réversible :
$$W_{iso}=-\int_{V_1}^{V_2}P\,\mathrm dV=-RT_1\int_{V_1}^{V_2}\frac{\mathrm dV}V=RT_1\ln\frac{V_1}{V_2}=8{,}31\times293\times\ln10\approx5{,}6\ \mathrm{kJ\,mol^{-1}}.$$

**3. Comparaison.** $W_{ad}>W_{iso}$. En adiabatique, le gaz s'échauffe, sa pression croît plus vite ($PV^\gamma$ au lieu de $PV$), et il résiste davantage à la compression. Dans le diagramme $(P,V)$, l'adiabatique est plus pentue que l'isotherme : l'aire sous la courbe, donc le travail, est plus grande.

**4. Allumage.** $T_2\approx740$ K dépasse largement la température d'auto-inflammation du gazole (550 K). Le carburant, injecté en fin de compression, s'enflamme spontanément, sans bougie : c'est le principe de l'**allumage par compression** du moteur Diesel. Les vrais moteurs ont des rapports volumétriques de 15 à 20, ce qui donne une marge supplémentaire au démarrage à froid. Le modèle réversible surestime légèrement $T_2$, car il y a des pertes thermiques.
"""

D['n-p1-frigo'] = r"""
**1. Définition de l'efficacité.** Pour un réfrigérateur, l'effet utile est la chaleur $Q_F>0$ extraite de la source froide (l'intérieur), et le coût est le travail électrique $W>0$ reçu :
$$e=\frac{Q_F}W.$$

**1. Premier principe sur un cycle.** $\Delta U=0$, donc $W+Q_F+Q_C=0$. $Q_C<0$ est la chaleur cédée à la cuisine.

**1. Second principe sur un cycle.** $\Delta S=0$ : l'entropie échangée est négative ou nulle. On obtient l'inégalité de Clausius :
$$\frac{Q_F}{T_F}+\frac{Q_C}{T_C}\le0.$$

**1. Efficacité maximale.** On remplace $Q_C=-W-Q_F$ :
$$\frac{Q_F}{T_F}-\frac{W+Q_F}{T_C}\le0\iff Q_F\Big(\frac1{T_F}-\frac1{T_C}\Big)\le\frac W{T_C}\iff Q_F\frac{T_C-T_F}{T_F}\le W.$$
D'où
$$e\le e_C=\frac{T_F}{T_C-T_F}=\frac{278}{298-278}=\frac{278}{20}\approx14.$$
L'égalité correspond au cycle réversible de Carnot.

**2. Puissance frigorifique.** Avec $e=3{,}0$, la chaleur extraite par unité de temps vaut $\mathcal P_F=e\mathcal P=3{,}0\times100=300$ W.

**2. Durée.** Pour solidifier $m=1{,}0$ kg d'eau à $0\ ^\circ$C, il faut lui retirer $Q=m\ell_f=334$ kJ. Donc
$$\Delta t=\frac Q{\mathcal P_F}=\frac{334\times10^3}{300}\approx1{,}1\times10^3\ \mathrm s\approx19\ \mathrm{min}.$$
En réalité, le congélateur est plus froid que $T_F=278$ K, donc $e$ est plus faible.

**3. Bilan pour $W=1$ J.** $Q_F=eW=3{,}0$ J, et le premier principe donne $Q_C=-(W+Q_F)=-4{,}0$ J.

**3. Entropie créée.** Sur un cycle, $\Delta S=0=S_{\mathrm{éch}}+S_c$, donc
$$S_c=-\Big(\frac{Q_F}{T_F}+\frac{Q_C}{T_C}\Big)=-\frac{3{,}0}{278}+\frac{4{,}0}{298}=-0{,}0108+0{,}0134\approx2{,}6\times10^{-3}\ \mathrm{J\,K^{-1}}.$$

**3. Interprétation.** $S_c>0$ : le fonctionnement est irréversible. Les causes sont les écarts de température finis entre le fluide et les sources dans les échangeurs, la détente irréversible dans le détendeur et les frottements dans le compresseur. C'est ce qui explique que $e=3$ soit très inférieur à $e_C\approx14$.
"""

D['n-p1-glacon'] = r"""
**1. Énergie nécessaire pour fondre tout le glaçon.**
- Réchauffer la glace de $-10\ ^\circ$C à $0\ ^\circ$C : $m_gc_g\times10=0{,}050\times2{,}1\times10=1{,}05$ kJ.
- La fondre à $0\ ^\circ$C : $m_g\ell_f=0{,}050\times334=16{,}7$ kJ.

Il faut au total $17{,}8$ kJ.

**1. Énergie disponible.** L'eau peut céder, en refroidissant de $25\ ^\circ$C à $0\ ^\circ$C, au plus $m_ec_e\times25=0{,}200\times4{,}18\times25=20{,}9$ kJ.

**1. Conclusion.** $20{,}9>17{,}8$ : il y a assez d'énergie pour fondre tout le glaçon, et l'état final est entièrement liquide, à une température $\theta_f>0\ ^\circ$C.

**2. Bilan enthalpique.** Le calorimètre est isolé et la transformation est monobare : $\Delta H=Q=0$. On somme les variations d'enthalpie de chaque partie :
$$\underbrace{m_gc_g\big(0-(-10)\big)}_{1{,}05\ \mathrm{kJ}}+\underbrace{m_g\ell_f}_{16{,}7\ \mathrm{kJ}}+\underbrace{m_gc_e(\theta_f-0)}_{\text{eau de fonte}}+\underbrace{m_ec_e(\theta_f-25)}_{\text{eau chaude}}=0.$$

**2. Résolution.** $(m_g+m_e)c_e\theta_f=m_ec_e\times25-17{,}8=20{,}9-17{,}8=3{,}1$ kJ (plus précisément $3{,}15$ kJ), donc
$$\theta_f=\frac{3{,}15}{0{,}250\times4{,}18}\approx3{,}0\ ^\circ\mathrm C.$$

**3. Variation d'entropie.** $S$ est une fonction d'état : on additionne les variations de chaque étape. Pour un corps condensé, $\Delta S=mc\ln\frac{T_f}{T_i}$ ; pour un changement d'état à $T$ fixe, $\Delta S=\frac{m\ell}T$. Avec $T_0=273$ K et $T_f=276$ K :
- glace de 263 à 273 K : $0{,}050\times2100\times\ln\frac{273}{263}=105\times0{,}0373\approx+3{,}9\ \mathrm{J\,K^{-1}}$ ;
- fusion à 273 K : $\frac{16\,700}{273}\approx+61{,}2\ \mathrm{J\,K^{-1}}$ ;
- eau de fonte de 273 à 276 K : $0{,}050\times4180\times\ln\frac{276}{273}=209\times0{,}0109\approx+2{,}3\ \mathrm{J\,K^{-1}}$ ;
- eau chaude de 298 à 276 K : $0{,}200\times4180\times\ln\frac{276}{298}=836\times(-0{,}0767)\approx-64{,}1\ \mathrm{J\,K^{-1}}$.

$$\Delta S\approx3{,}9+61{,}2+2{,}3-64{,}1\approx+3{,}3\ \mathrm{J\,K^{-1}}.$$

**3. Conclusion.** Le système est isolé : $S_{\mathrm{éch}}=0$, donc $S_c=\Delta S\approx+3{,}3\ \mathrm{J\,K^{-1}}>0$. La transformation est **irréversible**, comme tout transfert thermique entre corps de températures différentes. Le glaçon gagne plus d'entropie que l'eau chaude n'en perd : la même énergie, reçue à basse température, fait croître davantage l'entropie ($\mathrm dS=\frac{\delta Q}T$).
"""

D['n-p1-atmo'] = r"""
**1. Statique des fluides.** On oriente $Oz$ vers le haut. La relation fondamentale de la statique s'écrit $\frac{\mathrm dP}{\mathrm dz}=-\rho g$. Pour l'air, gaz parfait, $\rho=\frac{PM}{RT}$, donc
$$\frac{\mathrm dP}{\mathrm dz}=-\frac{Mg}{RT}P.$$

**1. Intégration.** $T$ est uniforme : on sépare les variables, $\frac{\mathrm dP}P=-\frac{\mathrm dz}H$, et on intègre depuis le sol :
$$P(z)=P_0e^{-z/H},\qquad H=\frac{RT}{Mg}=\frac{8{,}31\times288}{0{,}029\times9{,}8}=\frac{2393}{0{,}284}\approx8{,}4\ \mathrm{km}.$$
$H$ est la hauteur sur laquelle la pression est divisée par $e$.

**2. Pression au sommet de l'Everest.**
$$P=P_0e^{-8850/8400}=1{,}0\times e^{-1{,}05}\approx0{,}35\ \mathrm{bar}.$$
La valeur réelle, environ 0,33 bar, est un peu plus faible : la température décroît avec l'altitude (environ $-6{,}5$ K/km), donc l'air est plus dense en altitude que dans le modèle isotherme et la pression chute plus vite. Avec un tiers de la pression au sol, il y a aussi un tiers de l'oxygène.

**3. Petites hauteurs.** Pour $z\ll H$, $e^{-z/H}\approx1-\frac zH$, d'où $\frac{|\Delta P|}{P_0}\approx\frac zH$.
- Sur 100 m : $\frac{100}{8400}\approx1{,}2\ \%$.
- Sur une salle de 3 m : $\frac3{8400}\approx4\times10^{-4}$, soit 40 Pa.

La pression est uniforme à l'échelle d'une salle : c'est l'approximation usuelle pour les gaz.

**4. Masses volumiques au sol.**
$$\rho_{\mathrm{air}}=\frac{P_0M}{RT}=\frac{10^5\times0{,}029}{8{,}31\times288}\approx1{,}21\ \mathrm{kg\,m^{-3}},\qquad\rho_{\mathrm{He}}=\frac{P_0M_{\mathrm{He}}}{RT}=\frac{10^5\times0{,}004}{2393}\approx0{,}17\ \mathrm{kg\,m^{-3}}.$$

**4. Condition de décollage.** Le ballon est soumis à son poids (hélium + enveloppe + charge $m$) et à la poussée d'Archimède $\rho_{\mathrm{air}}Vg$. Il peut décoller si $\rho_{\mathrm{air}}Vg\ge(\rho_{\mathrm{He}}V+m)g$, soit
$$m\le(\rho_{\mathrm{air}}-\rho_{\mathrm{He}})V=(1{,}21-0{,}17)\times10\approx10\ \mathrm{kg}.$$
C'est environ 1 kg par $\mathrm m^3$ d'hélium, ce qui explique la taille des ballons-sondes.
"""

D['n-p1-bobine'] = r"""
**1. Flux.** Le champ est uniforme et parallèle à l'axe de la bobine. On oriente la normale aux spires selon $\vec B$ (pour $B>0$). Chaque spire est traversée par le flux $SB$, et les $N$ spires sont en série :
$$\Phi(t)=NSB(t)=NSB_0\sin\omega t.$$

**1. F.é.m. induite.** Loi de Faraday :
$$e(t)=-\frac{\mathrm d\Phi}{\mathrm dt}=-NSB_0\omega\cos\omega t.$$
Son amplitude, avec $\omega=2\pi f=314\ \mathrm{rad\,s^{-1}}$ et $S=20\times10^{-4}\ \mathrm{m^2}$, vaut
$$e_{\max}=NSB_0\omega=100\times2{,}0\times10^{-3}\times0{,}050\times314\approx3{,}1\ \mathrm V.$$

**2. Intensité.** L'auto-induction est négligée : le circuit équivaut à la f.é.m. $e$ en série avec $r$, fermé sur lui-même, donc $ri=e$ et
$$i(t)=-\frac{NSB_0\omega}r\cos\omega t,\qquad I_{\max}=\frac{3{,}14}{2{,}0}\approx1{,}6\ \mathrm A.$$

**2. Puissance moyenne.** $\mathcal P(t)=ri^2=\frac{e^2}r$, et $\langle\cos^2\rangle=\frac12$, donc
$$\langle\mathcal P\rangle=\frac{e_{\max}^2}{2r}=\frac{(3{,}14)^2}{4{,}0}\approx2{,}5\ \mathrm W.$$
Cette énergie est fournie par la source du champ $B$ et dissipée en chaleur dans la bobine.

**3. Sens du courant.** Quand $B$ croît ($\cos\omega t>0$, par exemple autour de $t=0$), $e<0$, donc $i<0$. Le courant circule dans le sens **opposé** à celui qu'associe la règle de la main droite à la normale orientée selon $\vec B$.

**3. Loi de Lenz.** Ce courant crée, au centre de la bobine, un champ propre opposé à $\vec B$, qui tend à limiter l'augmentation du flux. Les effets de l'induction s'opposent aux causes qui leur ont donné naissance.

**3. Validité.** Négliger l'auto-induction suppose $L\omega\ll r$. Pour une bobine plate de 100 spires de 2,5 cm de rayon, $L$ est de l'ordre du millihenry, et $L\omega$ est de l'ordre de $0{,}3\ \Omega$ : l'hypothèse est raisonnable, mais pas parfaite.
"""

D['n-p2-ailette'] = r"""
**1. Bilan d'énergie sur une tranche.** On considère la tranche $[x,x+\mathrm dx]$, de section $\pi a^2$ et de surface latérale $2\pi a\,\mathrm dx$. En régime permanent, l'énergie qui entre par conduction en $x$ est égale à celle qui sort par conduction en $x+\mathrm dx$, plus celle cédée à l'air par la surface latérale :
$$\Phi(x)=\Phi(x+\mathrm dx)+h(T-T_e)\,2\pi a\,\mathrm dx.$$

**1. Loi de Fourier.** $\Phi(x)=-\lambda\pi a^2\frac{\mathrm dT}{\mathrm dx}=-\lambda\pi a^2\theta'$, avec $\theta=T-T_e$ (et $T_e$ constant). Donc $\Phi(x)-\Phi(x+\mathrm dx)=-\Phi'(x)\,\mathrm dx=\lambda\pi a^2\theta''\,\mathrm dx$, et le bilan s'écrit
$$\lambda\pi a^2\theta''=2\pi ah\,\theta\iff\theta''=\frac\theta{\delta^2},\qquad\delta=\sqrt{\frac{\lambda a}{2h}}.$$

**1. Application numérique.**
$$\delta=\sqrt{\frac{200\times2{,}0\times10^{-3}}{2\times20}}=\sqrt{\frac{0{,}40}{40}}=\sqrt{0{,}010}=0{,}10\ \mathrm m.$$

**2. Solution générale.** $\theta(x)=Ae^{-x/\delta}+Be^{x/\delta}$.

**2. Conditions aux limites.** La tige est très longue devant $\delta$ : la température doit rester bornée (et tendre vers $T_e$ au loin), donc $B=0$. En $x=0$, $\theta(0)=T_0-T_e=\theta_0$, donc $A=\theta_0$ :
$$\theta(x)=\theta_0\,e^{-x/\delta}.$$

**2. Conséquence.** Au-delà de $3\delta\approx30$ cm, $\theta<5\ \%\,\theta_0$ : l'extrémité est pratiquement à la température de l'air et n'échange plus rien. Une ailette plus longue serait inutile.

**3. Flux évacué.** Tout le flux qui entre dans l'ailette en $x=0$ est finalement cédé à l'air :
$$\Phi=-\lambda\pi a^2\theta'(0)=\lambda\pi a^2\frac{\theta_0}\delta=\frac{200\times\pi\times(2{,}0\times10^{-3})^2\times50}{0{,}10}=\frac{200\times1{,}26\times10^{-5}\times50}{0{,}10}\approx1{,}3\ \mathrm W.$$
Vérification : $\int_0^\infty h\theta\,2\pi a\,\mathrm dx=2\pi ah\theta_0\delta=2\pi\times2\times10^{-3}\times20\times50\times0{,}1\approx1{,}3$ W. ✓

**3. Sans ailette.** La surface de paroi $\pi a^2$ évacuerait $\Phi_0=h\pi a^2\theta_0=20\times1{,}26\times10^{-5}\times50\approx1{,}3\times10^{-2}$ W.

**3. Gain.**
$$\frac\Phi{\Phi_0}=\frac{\lambda/\delta}h=\frac\lambda{h\delta}=\frac{200}{20\times0{,}10}=100.$$
L'ailette multiplie le flux évacué par 100 : elle offre une grande surface d'échange ($2\pi a\delta$ efficace) tout en conduisant bien la chaleur (aluminium). C'est le principe des radiateurs de processeurs. Elle n'est efficace que si $\frac\lambda{h\delta}\gg1$, c'est-à-dire pour un bon conducteur thermique.
"""
