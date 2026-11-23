D = {}

D['n-p2-plasma'] = r"""
**1. Mouvement d'un électron.** Un électron est soumis à la force électrique $-e\vec E$. On néglige la force magnétique ($evB\sim\frac vceE\ll eE$), le poids et les collisions. Le principe fondamental en régime sinusoïdal ($\frac{\mathrm d}{\mathrm dt}\to j\omega$) donne
$$m_ej\omega\underline{\vec v}=-e\underline{\vec E}\iff\underline{\vec v}=-\frac e{jm_e\omega}\underline{\vec E}=\frac{je}{m_e\omega}\underline{\vec E}.$$

**1. Densité de courant.** Les ions, immobiles, ne contribuent pas. Donc
$$\underline{\vec j}=-ne\underline{\vec v}=-j\frac{ne^2}{m_e\omega}\underline{\vec E}.$$
Le courant est en quadrature avec $\vec E$ : en moyenne, aucune puissance n'est cédée aux électrons, et il n'y a pas d'absorption (pas de collisions).

**2. Équation de propagation.** Le plasma est globalement neutre et l'onde est transverse : $\mathrm{div}\,\vec E=0$. On calcule $\overrightarrow{\mathrm{rot}}\,\overrightarrow{\mathrm{rot}}\,\vec E$ de deux façons :
$$-\Delta\vec E=-\frac{\partial}{\partial t}\overrightarrow{\mathrm{rot}}\,\vec B=-\mu_0\frac{\partial\vec j}{\partial t}-\frac1{c^2}\frac{\partial^2\vec E}{\partial t^2}.$$

**2. Relation de dispersion.** En complexes, $\Delta\to-k^2$ et $\frac{\partial}{\partial t}\to j\omega$ :
$$k^2\underline{\vec E}=\frac{\omega^2}{c^2}\underline{\vec E}-j\omega\mu_0\underline{\vec j}=\frac{\omega^2}{c^2}\underline{\vec E}-j\omega\mu_0\Big(-j\frac{ne^2}{m_e\omega}\Big)\underline{\vec E}=\Big(\frac{\omega^2}{c^2}-\frac{\mu_0ne^2}{m_e}\Big)\underline{\vec E}.$$
On multiplie par $c^2$, avec $\mu_0c^2=\frac1{\varepsilon_0}$ :
$$k^2c^2=\omega^2-\omega_p^2,\qquad\omega_p=\sqrt{\frac{ne^2}{m_e\varepsilon_0}}.$$

**2. Application numérique.**
$$\omega_p=\sqrt{\frac{1{,}0\times10^{12}\times(1{,}6\times10^{-19})^2}{9{,}1\times10^{-31}\times8{,}85\times10^{-12}}}=\sqrt{3{,}2\times10^{15}}\approx5{,}6\times10^7\ \mathrm{rad\,s^{-1}},\qquad f_p=\frac{\omega_p}{2\pi}\approx9\ \mathrm{MHz}.$$

**3. Cas $\omega<\omega_p$.** On a $k^2<0$, donc $k=\pm\frac j\delta$ avec $\delta=\frac c{\sqrt{\omega_p^2-\omega^2}}$. La solution physique est $\vec E=\vec E_0e^{-z/\delta}\cos\omega t$ : c'est une **onde évanescente**, non propagative, qui ne transporte pas d'énergie en moyenne ($\vec E$ et $\vec B$ en quadrature). L'onde incidente est totalement **réfléchie** par l'ionosphère.

**3. Applications.**
- Les ondes de fréquence inférieure à $f_p$ (grandes ondes, ondes moyennes, ondes courtes jusqu'à environ 10 MHz) se réfléchissent sur l'ionosphère, puis sur le sol, etc. Elles contournent ainsi la courbure terrestre et portent à des milliers de kilomètres.
- Les ondes du GHz ($f\gg f_p$) traversent l'ionosphère presque sans être affectées : elles conviennent pour communiquer avec les satellites (GPS, télévision).

**4. Vitesse de phase.**
$$v_\varphi=\frac\omega k=\frac{\omega c}{\sqrt{\omega^2-\omega_p^2}}=\frac c{\sqrt{1-\omega_p^2/\omega^2}}>c.$$

**4. Vitesse de groupe.** On différentie $k^2c^2=\omega^2-\omega_p^2$ : $2kc^2\,\mathrm dk=2\omega\,\mathrm d\omega$, donc
$$v_g=\frac{\mathrm d\omega}{\mathrm dk}=\frac{kc^2}\omega=c\sqrt{1-\frac{\omega_p^2}{\omega^2}}<c.$$

**4. Produit.** $v_\varphi v_g=\frac\omega k\cdot\frac{kc^2}\omega=c^2$. La vitesse de phase supérieure à $c$ ne contredit pas la relativité : c'est la vitesse de groupe, inférieure à $c$, qui correspond à la propagation de l'énergie et de l'information. Le plasma est dispersif : un paquet d'ondes s'y déforme.
"""

D['n-p2-roulement'] = r"""
**1. Notations.** On note $x$ l'abscisse du centre $G$ le long de la pente (vers le bas), $v=\dot x$, et $\omega$ la vitesse angulaire du cylindre, positive dans le sens qui correspond à un roulement vers le bas. Les forces sont le poids $m\vec g$, la réaction normale $N$ et la réaction tangentielle $T$ (frottement), supposée dirigée vers le haut de la pente.

**1. Roulement sans glissement.** La vitesse du point de contact $I$ est nulle : $\vec v_I=\vec v_G+\vec\omega\wedge\overrightarrow{GI}=\vec0$, ce qui donne $v=R\omega$.

**1. Théorème de la résultante.** On projette sur la pente et sur sa normale :
$$m\dot v=mg\sin\alpha-T,\qquad0=N-mg\cos\alpha.$$

**1. Théorème du moment cinétique en $G$.** Seule $T$ a un moment non nul par rapport à l'axe passant par $G$ (le poids s'applique en $G$, et $N$ passe par $G$) :
$$J\dot\omega=RT\quad\Longrightarrow\quad T=\frac J{R^2}\dot v,$$
en utilisant $\dot\omega=\frac{\dot v}R$.

**1. Accélération.** En reportant dans le théorème de la résultante : $m\dot v=mg\sin\alpha-\frac J{R^2}\dot v$, donc
$$\dot v=\frac{g\sin\alpha}{1+\frac J{mR^2}}.$$
- Cylindre plein, $\frac J{mR^2}=\frac12$ : $\dot v=\frac23g\sin\alpha$.
- Cylindre creux, $\frac J{mR^2}=1$ : $\dot v=\frac12g\sin\alpha$.

**2. Vainqueur.** Les deux mouvements sont uniformément accélérés à partir du repos. Le cylindre **plein**, plus accéléré, arrive premier, quelles que soient sa masse et son rayon : seule compte la répartition de la masse, à travers $\frac J{mR^2}$.

**2. Raisonnement énergétique.** Sans glissement, le point d'application de la réaction a une vitesse nulle : la réaction ne travaille pas, et l'énergie mécanique se conserve. Après une descente de hauteur $h$, par le théorème de König :
$$mgh=\frac12mv^2+\frac12J\omega^2=\frac12mv^2\Big(1+\frac J{mR^2}\Big)\quad\Longrightarrow\quad v^2=\frac{2gh}{1+J/(mR^2)}.$$
Le cylindre creux, dont toute la masse est loin de l'axe, stocke une plus grande part de l'énergie sous forme de rotation : il lui en reste moins pour la translation, et il va moins vite à toute hauteur.

**3. Réaction tangentielle (cylindre plein).**
$$T=\frac J{R^2}\dot v=\frac m2\cdot\frac23g\sin\alpha=\frac{mg\sin\alpha}3,\qquad N=mg\cos\alpha.$$

**3. Condition de non-glissement.** Selon la loi de Coulomb, il n'y a pas de glissement tant que $|T|\le fN$ :
$$\frac{mg\sin\alpha}3\le fmg\cos\alpha\iff\tan\alpha\le3f.$$
Au-delà, le cylindre glisse en roulant : $T=fN$, et l'accélération devient $g(\sin\alpha-f\cos\alpha)$, avec $\dot\omega=\frac{2fg\cos\alpha}R<\frac{\dot v}R$. Pour le cylindre creux, la condition est $\tan\alpha\le2f$ : il glisse plus facilement.
"""

D['n-p2-beau'] = r"""
**1. Diagramme de Watt.** Le cycle comporte deux adiabatiques ($1\to2$ et $3\to4$), plus pentues que des isothermes, et deux isochores (segments verticaux $2\to3$ et $4\to1$). Partant de $1$ ($V_1$, basse pression), on monte le long de l'adiabatique jusqu'à $2$ ($V_2$), puis verticalement jusqu'à $3$ (combustion). On redescend le long de l'adiabatique de détente jusqu'à $4$ ($V_1$), puis verticalement jusqu'à $1$.

**1. Caractère moteur.** La détente $3\to4$ se fait à plus haute pression que la compression $1\to2$ : le cycle est parcouru dans le sens horaire. Le travail reçu sur le cycle, $W=-\oint P\,\mathrm dV$, est l'opposé de l'aire du cycle : $W<0$. Le gaz fournit du travail, et le cycle est **moteur**.

**2. Température $T_2$.** Adiabatique réversible d'un gaz parfait, loi de Laplace $TV^{\gamma-1}=\text{cste}$ :
$$T_2=T_1\Big(\frac{V_1}{V_2}\Big)^{\gamma-1}=T_1a^{\gamma-1}=300\times9^{0{,}4}=300\times2{,}41\approx722\ \mathrm K.$$

**2. Température $T_4$.**
$$T_4=T_3\Big(\frac{V_3}{V_4}\Big)^{\gamma-1}=T_3\Big(\frac{V_2}{V_1}\Big)^{\gamma-1}=\frac{T_3}{a^{\gamma-1}}=\frac{2000}{2{,}41}\approx831\ \mathrm K.$$

**3. Transferts thermiques.** Sur les adiabatiques, $Q=0$. Sur les isochores, $W=0$ et $Q=\Delta U=C_v\Delta T$ :
$$Q_{23}=C_v(T_3-T_2)>0\ (\text{reçu}),\qquad Q_{41}=C_v(T_1-T_4)<0\ (\text{cédé}).$$

**3. Rendement.** Premier principe sur un cycle : $W+Q_{23}+Q_{41}=0$, donc
$$\eta=\frac{-W}{Q_{23}}=\frac{Q_{23}+Q_{41}}{Q_{23}}=1-\frac{T_4-T_1}{T_3-T_2}.$$

**3. Simplification.** D'après la question 2, $T_4=T_3a^{1-\gamma}$ et $T_1=T_2a^{1-\gamma}$, donc $T_4-T_1=a^{1-\gamma}(T_3-T_2)$ et
$$\eta=1-a^{1-\gamma}=1-9^{-0{,}4}=1-\frac1{2{,}41}\approx0{,}58.$$
Le rendement ne dépend que du rapport volumétrique $a$ (et de $\gamma$). Il croît avec $a$, mais $a$ est limité, vers 10 pour l'essence, par le cliquetis (auto-inflammation prématurée du mélange). Vérification avec les températures : $1-\frac{831-300}{2000-722}=1-\frac{531}{1278}\approx0{,}58$. ✓

**4. Comparaison avec Carnot.** Entre les températures extrêmes, $\eta_C=1-\frac{T_1}{T_3}=1-\frac{300}{2000}=0{,}85>0{,}58$. Le cycle de Beau de Rochas, même réversible pour le gaz, échange de la chaleur à température variable (sur les isochores) et non avec deux thermostats aux températures extrêmes. Les transferts avec les sources réelles sont irréversibles, d'où un rendement inférieur à celui de Carnot.

**4. Rendement réel.** Il est de l'ordre de 30 à 35 %, encore plus faible, à cause de :
- la combustion non instantanée (le cycle réel est arrondi) ;
- les pertes thermiques aux parois (les compressions et détentes ne sont pas adiabatiques) ;
- les frottements mécaniques ;
- le travail de pompage (admission et échappement) ;
- le gaz réel ($\gamma$ diminue à haute température), et la combustion incomplète.
"""

D['n-p2-vdw'] = r"""
**1. Premier principe.** Le système est le gaz (le vide ne contient rien). L'enceinte est rigide : le gaz ne reçoit aucun travail des parois, et il se détend dans le vide sans pousser de piston, donc $W=0$. Elle est calorifugée, donc $Q=0$. Le premier principe donne
$$\Delta U=W+Q=0.$$
C'est une détente de Joule et Gay-Lussac, isoénergétique.

**2. Température finale.** Pour une mole, $V_m=V$. Avec $U_m=C_vT-\frac a{V_m}+\text{cste}$, la condition $\Delta U=0$ s'écrit
$$C_v(T_2-T_1)-a\Big(\frac1{V_2}-\frac1{V_1}\Big)=0\iff T_2-T_1=\frac a{C_v}\Big(\frac1{V_2}-\frac1{V_1}\Big).$$

**2. Application numérique.** $C_v=3R=24{,}9\ \mathrm{J\,K^{-1}\,mol^{-1}}$, $\frac1{V_2}=500\ \mathrm{m^{-3}}$ et $\frac1{V_1}=1000\ \mathrm{m^{-3}}$ :
$$T_2-T_1=\frac{0{,}364\times(500-1000)}{24{,}9}=\frac{-182}{24{,}9}\approx-7{,}3\ \mathrm K,\qquad T_2\approx292{,}7\ \mathrm K.$$

**2. Gaz parfait.** Selon la première loi de Joule, $U$ ne dépend que de $T$. $\Delta U=0$ impose donc $T_2=T_1=300$ K : pas de variation de température. L'écart mesure l'effet des interactions.

**3. Entropie créée.** Le système est isolé : $S_{\mathrm{éch}}=0$, donc $S_c=\Delta S$. Avec l'expression donnée :
$$\Delta S=C_v\ln\frac{T_2}{T_1}+R\ln\frac{V_2-b}{V_1-b}.$$
- Premier terme : $24{,}9\times\ln\frac{292{,}7}{300}=24{,}9\times(-0{,}0246)\approx-0{,}61\ \mathrm{J\,K^{-1}}$.
- Second terme : $8{,}31\times\ln\frac{2{,}0\times10^{-3}-4{,}27\times10^{-5}}{1{,}0\times10^{-3}-4{,}27\times10^{-5}}=8{,}31\times\ln\frac{1{,}957}{0{,}957}=8{,}31\times0{,}715\approx5{,}94\ \mathrm{J\,K^{-1}}$.

$$S_c\approx5{,}3\ \mathrm{J\,K^{-1}}>0.$$

**3. Conclusion.** La détente est **irréversible** : le gaz ne revient jamais spontanément dans le premier compartiment. Pour un gaz parfait, on aurait $S_c=R\ln2\approx5{,}76\ \mathrm{J\,K^{-1}}$, peu différent.

**4. Interprétation microscopique.** Le terme $-\frac a{V_m}$ représente l'énergie potentielle d'interaction attractive entre molécules (forces de van der Waals), négative et d'autant plus grande en valeur absolue que les molécules sont proches. Pendant la détente, la distance moyenne entre molécules augmente : leur énergie potentielle croît (devient moins négative). L'énergie totale étant conservée, cette augmentation est prélevée sur l'énergie cinétique d'agitation thermique : la température baisse. Ce refroidissement est faible, mais il est à la base (via la détente de Joule-Thomson, plus pratique) de la liquéfaction des gaz.
"""

D['n-p2-voile'] = r"""
**1. Photons reçus.** Pendant $\mathrm dt$, la voile de surface $S$, face au Soleil, reçoit l'énergie $\varphi S\,\mathrm dt$. Avec des photons d'énergie $\varepsilon$, cela représente $\mathrm dN=\frac{\varphi S\,\mathrm dt}\varepsilon$ photons. (Le résultat ne dépend pas de $\varepsilon$ : on peut raisonner sur un spectre quelconque.)

**1. Quantité de mouvement transférée.** Chaque photon arrive avec la quantité de mouvement $\frac\varepsilon c\vec u$ (où $\vec u$ s'éloigne du Soleil) et repart, après réflexion parfaite sous incidence normale, avec $-\frac\varepsilon c\vec u$. Sa variation vaut $-\frac{2\varepsilon}c\vec u$. Par conservation de la quantité de mouvement, la voile reçoit $+\frac{2\varepsilon}c\vec u$ par photon.

**1. Force et pression.**
$$\vec F=\frac{\mathrm dN}{\mathrm dt}\cdot\frac{2\varepsilon}c\vec u=\frac{2\varphi S}c\vec u,\qquad P=\frac FS=\frac{2\varphi}c.$$
À la distance de la Terre :
$$P=\frac{2\times1361}{3{,}00\times10^8}\approx9{,}1\times10^{-6}\ \mathrm{Pa}.$$
C'est environ $10^{-10}$ fois la pression atmosphérique. (Pour une surface absorbante, le facteur 2 disparaît.)

**2. Force et accélération.** $S=(100)^2=10^4\ \mathrm{m^2}$, donc $F=PS=9{,}1\times10^{-6}\times10^4\approx9{,}1\times10^{-2}$ N (le poids d'environ 9 g sur Terre). L'accélération vaut
$$a=\frac Fm=\frac{9{,}1\times10^{-2}}{100}\approx9{,}1\times10^{-4}\ \mathrm{m\,s^{-2}}.$$

**2. Comparaison.** $\frac a{g_0}=\frac{9{,}1\times10^{-4}}{5{,}9\times10^{-3}}\approx0{,}15$. La poussée radiative ne compense que 15 % de l'attraction solaire : la voile ne peut pas s'échapper. Mais cette poussée est continue et sans consommation de carburant. Sur un an ($3\times10^7$ s), elle produit un changement de vitesse de l'ordre de $\Delta v\sim a\,t\sim3\times10^4\ \mathrm{m\,s^{-1}}$, ce qui modifie fortement l'orbite.

**3. Dépendance en distance.** Le flux solaire et le champ de gravitation décroissent tous deux en $\frac1{r^2}$ : $\varphi=\varphi_0\big(\frac{r_0}r\big)^2$ et $g=g_0\big(\frac{r_0}r\big)^2$. Leur rapport,
$$\frac{F_{\mathrm{rad}}}{mg}=\frac{2\varphi S}{cmg}=\frac{2\varphi_0}{cg_0}\cdot\frac Sm,$$
ne dépend pas de $r$. Ce n'est qu'une question de masse surfacique.

**3. Masse surfacique maximale.** La voile est repoussée (accélération nette dirigée vers l'extérieur) si $\frac{F_{\mathrm{rad}}}{mg}>1$, c'est-à-dire si
$$\sigma=\frac mS<\frac{2\varphi_0}{cg_0}=\frac{2\times1361}{3{,}00\times10^8\times5{,}9\times10^{-3}}\approx1{,}5\times10^{-3}\ \mathrm{kg\,m^{-2}}=1{,}5\ \mathrm{g\,m^{-2}}.$$

**3. Réalisme.** Un film de Mylar aluminisé de $1\ \mu$m d'épaisseur (masse volumique de l'ordre de $1400\ \mathrm{kg\,m^{-3}}$) pèse déjà $1{,}4\ \mathrm{g\,m^{-2}}$, sans structure ni charge utile. Échapper au Soleil par la seule lumière est donc hors de portée des technologies actuelles. Ici, $\sigma=\frac{100}{10^4}=10\ \mathrm{g\,m^{-2}}$. Les missions réelles (IKAROS, 2010 ; LightSail) utilisent la voile pour manœuvrer et modifier lentement leur orbite, en orientant la voile pour obtenir une composante tangentielle de la force.
"""

D['n-p2-alternateur'] = r"""
**1. Flux.** Le champ est uniforme. À l'instant $t$, la normale $\vec n$ de la bobine fait l'angle $\theta=\omega t$ avec $\vec B$ (elle est parallèle à $\vec B$ à $t=0$). Le flux à travers les $N$ spires vaut
$$\Phi_{\mathrm{ext}}=NBS\cos\omega t.$$

**1. F.é.m. induite.** Loi de Faraday :
$$e(t)=-\frac{\mathrm d\Phi_{\mathrm{ext}}}{\mathrm dt}=NBS\omega\sin\omega t=E_m\sin\omega t,\qquad E_m=NBS\omega.$$
Elle est sinusoïdale, de pulsation égale à la vitesse de rotation : c'est le principe de l'alternateur.

**2. Équation électrique.** La bobine fermée sur elle-même se comporte comme la f.é.m. $e$, en série avec $R$ et l'inductance propre $L$ (qui ajoute la f.é.m. d'auto-induction $-L\frac{\mathrm di}{\mathrm dt}$) :
$$L\frac{\mathrm di}{\mathrm dt}+Ri=e(t)=E_m\sin\omega t.$$

**2. Régime établi.** En complexes, $\underline I=\frac{\underline E}{R+jL\omega}$. Donc $i=I_m\sin(\omega t-\varphi)$, avec
$$I_m=\frac{NBS\omega}{\sqrt{R^2+L^2\omega^2}},\qquad\tan\varphi=\frac{L\omega}R,\quad\varphi\in\Big[0,\frac\pi2\Big[.$$
Le courant est en retard sur la f.é.m., à cause de l'inductance.

**3. Couple de Laplace.** Le moment magnétique vaut $\vec{\mathcal M}=NiS\vec n$, et le couple $\vec\Gamma=\vec{\mathcal M}\wedge\vec B$. On note $\vec u$ le vecteur unitaire de l'axe de rotation, orienté de sorte que $\theta=\omega t$ croisse ; $\vec n$ tourne de $\vec B/B$ vers une direction $\vec c\perp\vec B$. Alors $\vec n\wedge\vec B=-B\sin\omega t\,\vec u$, et la projection du couple sur l'axe vaut
$$\Gamma=-NiSB\sin\omega t.$$

**3. Valeur moyenne.**
$$\langle\Gamma\rangle=-NSBI_m\big\langle\sin(\omega t-\varphi)\sin\omega t\big\rangle=-NSBI_m\cdot\frac{\cos\varphi}2,$$
car $\sin(\omega t-\varphi)\sin\omega t=\frac12\big[\cos\varphi-\cos(2\omega t-\varphi)\big]$. On a $\langle\Gamma\rangle<0$ : c'est un couple **résistant**, qui s'oppose à la rotation. C'est la loi de Lenz : le courant induit freine le mouvement qui lui a donné naissance.

**4. Puissance mécanique.** Pour maintenir $\omega$ constante, l'opérateur doit exercer un couple $-\Gamma$ ; sa puissance moyenne vaut
$$\mathcal P_m=-\langle\Gamma\rangle\omega=\frac{NBS\omega I_m\cos\varphi}2=\frac{E_mI_m\cos\varphi}2.$$

**4. Puissance Joule.** Avec $\cos\varphi=\frac R{\sqrt{R^2+L^2\omega^2}}$ :
$$\mathcal P_J=\langle Ri^2\rangle=\frac{RI_m^2}2=\frac{R}2\cdot\frac{E_m^2}{R^2+L^2\omega^2}=\frac{E_m}2\cdot\frac{E_m}{\sqrt{R^2+L^2\omega^2}}\cdot\frac R{\sqrt{R^2+L^2\omega^2}}=\frac{E_mI_m\cos\varphi}2.$$

**4. Bilan.** $\mathcal P_m=\mathcal P_J$ : toute la puissance mécanique fournie est convertie en puissance électrique, puis dissipée par effet Joule. L'énergie magnétique $\frac12Li^2$ est périodique, donc de variation moyenne nulle sur une période, et n'intervient pas en moyenne. C'est le couplage électromécanique parfait : $\Gamma\omega+ei=0$ à chaque instant. Dans un vrai alternateur, la bobine débite dans une charge utile, au lieu d'être en court-circuit.
"""
