D = {}

D['p-th-1'] = r"""
**1. Volume initial.** Par l'équation d'état des gaz parfaits :
$$V_0=\frac{nRT_0}{P_0}.$$

**2. État final mécanique.** Une fois le piston libéré, il oscille puis s'immobilise (les frottements dissipent les oscillations). À l'équilibre mécanique final, la pression du gaz équilibre l'atmosphère (piston de masse négligeable) :
$$P_f=P_1=\frac{P_0}2.$$

**2. Premier principe.** Le système {gaz} est fermé et la transformation est adiabatique ($Q=0$). Le piston, en se déplaçant, est soumis du côté extérieur à la pression constante $P_1$ : le travail reçu par le gaz est celui de la pression extérieure, $W=-P_1(V_f-V_0)$ (transformation monobare). Avec $\Delta U=nC_{v,m}(T_f-T_0)$ et $C_{v,m}=\frac R{\gamma-1}=\frac32R$ :
$$\frac32nR(T_f-T_0)=-P_1V_f+P_1V_0.$$

**2. Calcul.** $P_1V_f=P_fV_f=nRT_f$ et $P_1V_0=\frac{P_0}2\cdot\frac{nRT_0}{P_0}=\frac{nRT_0}2$. Donc, en divisant par $nR$ :
$$\frac32T_f-\frac32T_0=-T_f+\frac12T_0\iff\frac52T_f=2T_0\iff T_f=\frac45T_0.$$

**2. Résultats.**
$$P_f=\frac{P_0}2,\qquad T_f=\frac45T_0,\qquad V_f=\frac{nRT_f}{P_f}=\frac{nR\cdot\frac45T_0}{P_0/2}=\frac85V_0.$$

**2. Comparaison.** Une détente adiabatique **réversible** jusqu'à $\frac{P_0}2$ suivrait la loi de Laplace $T^\gamma P^{1-\gamma}=\text{cste}$, d'où $T=T_0\,2^{-(\gamma-1)/\gamma}=T_0\,2^{-2/5}\approx0{,}76T_0$. La détente brutale refroidit moins ($0{,}80T_0$) : le gaz fournit moins de travail, car il pousse contre $P_1$ seulement, et non contre sa propre pression.

**3. Variation d'entropie.** $S$ est une fonction d'état : on la calcule par la formule du gaz parfait, avec $C_{p,m}=\frac52R$.
$$\Delta S=nC_{p,m}\ln\frac{T_f}{T_0}-nR\ln\frac{P_f}{P_0}=nR\Big(\frac52\ln\frac45-\ln\frac12\Big)=nR\Big(\frac52\ln0{,}8+\ln2\Big).$$
Numériquement : $\frac52\ln0{,}8=-0{,}558$ et $\ln2=0{,}693$, donc
$$\Delta S\approx0{,}135\,nR>0.$$

**3. Irréversibilité.** Le second principe s'écrit $\Delta S=S_{\mathrm{éch}}+S_{\mathrm{créée}}$. La transformation est adiabatique : $S_{\mathrm{éch}}=0$. Donc $S_{\mathrm{créée}}=\Delta S\approx0{,}135\,nR>0$ : la transformation est **irréversible**. La cause est le déséquilibre mécanique initial : la pression du gaz, $P_0$, est très différente de la pression extérieure, $P_0/2$. Les oscillations du piston et les mouvements internes du gaz sont amortis par les frottements et la viscosité.
"""

D['p-th-4'] = r"""
**0. Données utiles.** On travaille par unité de masse.
$$c_p=\frac{\gamma R}{(\gamma-1)M}=\frac{1{,}4\times8{,}314}{0{,}4\times0{,}029}\approx1{,}00\times10^3\ \mathrm{J\,K^{-1}\,kg^{-1}},\qquad\frac{\gamma-1}\gamma=\frac{0{,}4}{1{,}4}=0{,}286.$$
On note $r=5^{0{,}286}\approx1{,}584$. Pour un écoulement permanent, le premier principe industriel s'écrit $\Delta h+\Delta e_c=w_u+q$ ; pour un gaz parfait, $\Delta h=c_p\Delta T$.

**1. Compression $A\to B$** (adiabatique réversible). La loi de Laplace, $TP^{(1-\gamma)/\gamma}=\text{cste}$, donne
$$T_B=T_A\Big(\frac{P_B}{P_A}\Big)^{0{,}286}=290\times1{,}584\approx459\ \mathrm K,\qquad P_B=5{,}0\times10^5\ \mathrm{Pa}.$$
Le travail utile reçu vaut $w_{AB}=c_p(T_B-T_A)\approx1{,}70\times10^5\ \mathrm{J\,kg^{-1}}$.

**1. Chauffage $B\to C$** (isobare). $P_C=P_B=5{,}0\times10^5$ Pa et $T_C=1500$ K.

**1. Turbine $C\to D$.** Le travail fourni par la turbine, $c_p(T_C-T_D)$, entraîne exactement le compresseur :
$$c_p(T_C-T_D)=c_p(T_B-T_A)\iff T_D=T_C-(T_B-T_A)=1500-169\approx1331\ \mathrm K.$$
La transformation étant adiabatique réversible :
$$P_D=P_C\Big(\frac{T_D}{T_C}\Big)^{\gamma/(\gamma-1)}=5{,}0\times10^5\times(0{,}887)^{3{,}5}\approx3{,}3\times10^5\ \mathrm{Pa}.$$

**1. Tuyère $D\to E$** (adiabatique réversible). $P_E=P_A=1{,}0\times10^5$ Pa. Comme $C\to D\to E$ est globalement isentropique, on peut appliquer Laplace entre $C$ et $E$ :
$$T_E=T_C\Big(\frac{P_E}{P_C}\Big)^{0{,}286}=\frac{1500}{1{,}584}\approx947\ \mathrm K.$$

**2. Vitesse d'éjection.** Dans la tuyère, il n'y a ni travail utile ni transfert thermique, et la vitesse d'entrée est négligée : $c_p(T_E-T_D)+\frac12V_E^2=0$. Donc
$$V_E=\sqrt{2c_p(T_D-T_E)}=\sqrt{2\times1003\times384}\approx877\ \mathrm{m\,s^{-1}}.$$

**3. Chaleur reçue.** $q=c_p(T_C-T_B)=1003\times1041\approx1{,}04\times10^6\ \mathrm{J\,kg^{-1}}$.

**3. Rendement.** L'énergie utile est l'énergie cinétique du jet :
$$\eta=\frac{V_E^2/2}q=\frac{T_D-T_E}{T_C-T_B}.$$
Avec $T_B=rT_A$, $T_E=\frac{T_C}r$ et $T_D=T_C-T_B+T_A$ :
$$T_D-T_E=(T_C-T_B)-\Big(\frac{T_C}r-\frac{T_B}r\Big)=(T_C-T_B)\Big(1-\frac1r\Big),$$
donc
$$\eta=1-\frac1r=1-5^{-0{,}286}\approx0{,}37.$$
C'est le rendement du cycle de Brayton (Joule), qui ne dépend que du rapport de compression.

**3. Puissances.**
- Puissance cinétique produite : $\mathcal P_c=D_m\frac{V_E^2}2=40\times3{,}85\times10^5\approx15$ MW.
- Puissance thermique consommée : $\mathcal P_{th}=D_mq=40\times1{,}04\times10^6\approx42$ MW.

On vérifie que $\frac{15}{42}\approx0{,}37$. ✓ La poussée vaut $D_mV_E\approx35$ kN (en négligeant la vitesse d'entrée).
"""

D['p-th-spe1'] = r"""
**1. Système.** On considère la tranche $[z,z+\mathrm dz]$ du conducteur, de volume $\pi a^2\,\mathrm dz$ et de masse $\mu\pi a^2\,\mathrm dz$. On fait un bilan d'énergie (interne) entre $t$ et $t+\mathrm dt$.

**1. Variation d'énergie interne.** $\mathrm dU=\mu c\,\pi a^2\,\mathrm dz\,\frac{\partial T}{\partial t}\mathrm dt$.

**1. Termes du bilan.**
- **Conduction axiale** (loi de Fourier, $j_{th}=-\lambda\frac{\partial T}{\partial z}$). L'énergie entrant en $z$ moins celle sortant en $z+\mathrm dz$ vaut
$$\big[j_{th}(z)-j_{th}(z+\mathrm dz)\big]\pi a^2\,\mathrm dt=\lambda\frac{\partial^2T}{\partial z^2}\pi a^2\,\mathrm dz\,\mathrm dt.$$
- **Effet Joule.** La tranche a une résistance $\mathrm dR=\frac{\mathrm dz}{\gamma\pi a^2}$ et reçoit $\mathrm dR\,i^2\,\mathrm dt=\frac{i^2\,\mathrm dz}{\gamma\pi a^2}\mathrm dt$.
- **Pertes latérales.** Sur la surface $2\pi a\,\mathrm dz$, l'énergie perdue vaut $\beta(T-T_0)2\pi a\,\mathrm dz\,\mathrm dt$ (on suppose $T$ uniforme sur une section, car le conducteur est fin).

**1. Équation.** En divisant le bilan par $\mathrm dz\,\mathrm dt$ :
$$\mu c\pi a^2\frac{\partial T}{\partial t}=\lambda\pi a^2\frac{\partial^2T}{\partial z^2}-2\beta\pi a(T-T_0)+\frac{i^2}{\gamma\pi a^2}.$$

**2. Moyenne sur la longueur.** On intègre l'équation sur $z\in[0,L]$, puis on divise par $L$. Comme $L$ est fixe, $\frac1L\int_0^L\frac{\partial T}{\partial t}\mathrm dz=\frac{\mathrm dT_m}{\mathrm dt}=\dot\theta$ (car $T_0$ est constante). De même, $\frac1L\int_0^L(T-T_0)\,\mathrm dz=\theta$.

**2. Terme de conduction.** $\int_0^L\frac{\partial^2T}{\partial z^2}\mathrm dz=\Big[\frac{\partial T}{\partial z}\Big]_0^L=0$, car les extrémités sont calorifugées (flux nul, donc $\frac{\partial T}{\partial z}=0$ en $z=0$ et $z=L$). La conduction redistribue l'énergie sans en créer ni en perdre.

**2. Équation en $\theta$.**
$$\mu c\pi a^2\dot\theta=-2\beta\pi a\,\theta+\frac{i^2}{\gamma\pi a^2}.$$
En divisant par $2\beta\pi a$ :
$$\tau\dot\theta+\theta=\theta_\infty,\qquad\tau=\frac{\mu c\pi a^2}{2\beta\pi a}=\frac{\mu ca}{2\beta},\qquad\theta_\infty=\frac{i^2}{\gamma\pi a^2\cdot2\beta\pi a}=\frac{i^2}{2\beta\gamma\pi^2a^3}.$$

**3. Résolution.** La solution générale est $\theta=\theta_\infty+Ke^{-t/\tau}$. En supposant le conducteur initialement à l'équilibre avec l'extérieur ($T_m(0)=T_0$, donc $\theta(0)=0$), on trouve $K=-\theta_\infty$ et
$$T_m(t)=T_0+\theta_\infty\big(1-e^{-t/\tau}\big).$$
La température moyenne tend exponentiellement vers $T_0+\theta_\infty$ en quelques $\tau$.

**Commentaires.**
- En régime permanent, la puissance Joule totale, $\frac{i^2L}{\gamma\pi a^2}$, est égale aux pertes latérales, $2\beta\pi aL\theta_\infty$.
- $\theta_\infty\propto\frac{i^2}{a^3}$ : doubler l'intensité multiplie l'échauffement par 4. C'est pourquoi la section des câbles électriques est dimensionnée selon l'intensité maximale (normes d'installation).
- $\tau\propto a$ : un fil fin s'échauffe vite (principe du fusible).
"""

D['p-th-spe2'] = r"""
**1. Puissance rayonnée par le Soleil.** On assimile le Soleil à un corps noir à $T_S$. La loi de Stefan donne un flux surfacique $\sigma T_S^4$, émis par la surface $4\pi R_S^2$ :
$$P_S=4\pi R_S^2\,\sigma T_S^4.$$
Applications numériques : $R_S^2=4{,}84\times10^{17}\ \mathrm{m^2}$, $T_S^4=(5778)^4\approx1{,}115\times10^{15}\ \mathrm{K^4}$, d'où
$$P_S=4\pi\times4{,}84\times10^{17}\times5{,}67\times10^{-8}\times1{,}115\times10^{15}\approx3{,}8\times10^{26}\ \mathrm W.$$

**2. Flux reçu.** La Lune est à la distance $r\approx1{,}496\times10^{11}$ m du Soleil (la distance Terre-Lune est négligeable devant $r$). La puissance solaire se répartit sur la sphère de rayon $r$, d'où un flux surfacique (constante solaire)
$$\varphi=\frac{P_S}{4\pi r^2}=\frac{R_S^2\sigma T_S^4}{r^2}\approx1{,}37\times10^3\ \mathrm{W\,m^{-2}}.$$

**2. Puissance absorbée.** La Lune intercepte le rayonnement sur sa section droite (le disque $\pi R_L^2$), et absorbe tout (puissance réfléchie négligée) : $P_{\mathrm{abs}}=\varphi\,\pi R_L^2$.

**2. Puissance émise.** L'hémisphère jour, d'aire $2\pi R_L^2$, rayonne comme un corps noir à $T_j$. L'hémisphère nuit émet $2\pi R_L^2\sigma T_n^4$, négligeable car $T_n\ll T_j$. La conduction entre les deux hémisphères est aussi négligée : chaque hémisphère est en équilibre séparément.

**2. Bilan en régime permanent.**
$$\frac{R_S^2\sigma T_S^4}{r^2}\pi R_L^2=2\pi R_L^2\sigma T_j^4\iff T_j^4=\frac{T_S^4}2\cdot\frac{R_S^2}{r^2}\iff T_j=T_S\sqrt{\frac{R_S}r}\cdot2^{-1/4}.$$
Le rayon lunaire se simplifie.

**2. Application numérique.** $\sqrt{\frac{R_S}r}=\sqrt{\frac{6{,}957\times10^8}{1{,}496\times10^{11}}}=\sqrt{4{,}65\times10^{-3}}=0{,}0682$, et $2^{-1/4}=0{,}841$. Donc
$$T_j\approx5778\times0{,}0682\times0{,}841\approx331\ \mathrm K\approx58\,^\circ\mathrm C.$$

**2. Commentaires.**
- La température mesurée au point subsolaire atteint environ 390 K. Le modèle, avec un hémisphère homogène, moyenne les régions éclairées en incidence rasante, beaucoup plus froides. Au point subsolaire seul, l'équilibre local donnerait $\sigma T^4=\varphi$, soit $T=T_S\sqrt{\frac{R_S}r}\approx394$ K, en bon accord avec la mesure.
- La nuit, $T_n$ chute vers 100 K : sans atmosphère ni océan, rien ne redistribue la chaleur, contrairement à la Terre.
"""
