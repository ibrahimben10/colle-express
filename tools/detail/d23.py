D = {}

D['c-thermo-1'] = r"""
**1. Expression de la constante d'équilibre.** Les solides purs ($\mathrm{CuO}$, $\mathrm{Cu_2O}$) ont une activité égale à 1 ; le gaz, supposé parfait, a pour activité $\frac{P_{\mathrm{O_2}}}{P^\circ}$. La loi d'action des masses donne donc
$$K(T)=\frac{a_{\mathrm{Cu_2O}}^2\,a_{\mathrm{O_2}}}{a_{\mathrm{CuO}}^4}=\frac{P_{\mathrm{O_2,eq}}}{P^\circ}.$$
Avec $P^\circ=10^5$ Pa :
$$K_1=\frac{4660}{10^5}=0{,}0466,\qquad K_2=\frac{29\,610}{10^5}=0{,}2961.$$

**2. Relation entre $K$ et les grandeurs standard.** On a $\Delta_rG^\circ(T)=-RT\ln K(T)$ et, dans l'approximation d'Ellingham, $\Delta_rG^\circ(T)=\Delta_rH^\circ-T\Delta_rS^\circ$. Donc
$$\ln K(T)=-\frac{\Delta_rH^\circ}{RT}+\frac{\Delta_rS^\circ}R.$$

**3. Calcul de $\Delta_rH^\circ$.** Écrivons cette relation en $T_1$ et $T_2$, puis soustrayons : le terme $\frac{\Delta_rS^\circ}R$ s'élimine.
$$\ln K_2-\ln K_1=\frac{\Delta_rH^\circ}R\Big(\frac1{T_1}-\frac1{T_2}\Big)\quad\Longrightarrow\quad\Delta_rH^\circ=\frac{R\ln(K_2/K_1)}{\frac1{T_1}-\frac1{T_2}}.$$
Applications numériques :
- $\frac{K_2}{K_1}=\frac{29\,610}{4660}=6{,}354$, donc $\ln(6{,}354)=1{,}849$ ;
- $\frac1{T_1}-\frac1{T_2}=\frac{T_2-T_1}{T_1T_2}=\frac{100}{1223\times1323}=\frac{100}{1\,618\,029}=6{,}180\times10^{-5}\ \mathrm{K^{-1}}$.

D'où
$$\Delta_rH^\circ=\frac{8{,}314\times1{,}849}{6{,}180\times10^{-5}}=\frac{15{,}37}{6{,}180\times10^{-5}}\approx2{,}49\times10^5\ \mathrm{J\,mol^{-1}}=+249\ \mathrm{kJ\,mol^{-1}}.$$

**4. Calcul de $\Delta_rS^\circ$.** On utilise la relation en $T_1$ : $\Delta_rS^\circ=\frac{\Delta_rH^\circ+RT_1\ln K_1}{T_1}$.
- $\ln K_1=\ln(0{,}0466)=-3{,}066$ ;
- $RT_1=8{,}314\times1223=1{,}017\times10^4\ \mathrm{J\,mol^{-1}}$, donc $RT_1\ln K_1=-3{,}118\times10^4\ \mathrm{J\,mol^{-1}}$.

$$\Delta_rS^\circ=\frac{2{,}488\times10^5-3{,}118\times10^4}{1223}=\frac{2{,}176\times10^5}{1223}\approx178\ \mathrm{J\,K^{-1}\,mol^{-1}}.$$
Vérification en $T_2$ : $-\frac{2{,}488\times10^5}{8{,}314\times1323}+\frac{178}{8{,}314}=-22{,}62+21{,}41=-1{,}21$, et $\ln K_2=\ln(0{,}2961)=-1{,}217$. ✓

**5. Commentaires.**
- $\Delta_rH^\circ>0$ : la réaction est endothermique. D'après la loi de Van't Hoff, $\frac{\mathrm d\ln K}{\mathrm dT}=\frac{\Delta_rH^\circ}{RT^2}>0$ : $K$ croît avec $T$, ce que confirment les mesures ($K_2>K_1$).
- $\Delta_rS^\circ>0$ : cohérent avec la formation d'un gaz à partir de solides ($\Delta n_{\mathrm{gaz}}=+1$), ce qui augmente le désordre.
"""

D['c-sol-2'] = r"""
**1. Réaction prépondérante.** En milieu acide ($\mathrm{pH}<\mathrm pK_{A1}=7$), le soufre dissous est sous forme $\mathrm{H_2S}$ : les ions $\mathrm{S^{2-}}$ libérés par la dissolution captent deux protons. La réaction de dissolution s'écrit donc
$$\mathrm{CoS_{(s)}}+2\,\mathrm{H^+}=\mathrm{Co^{2+}}+\mathrm{H_2S}.$$

**2. Calcul de sa constante.** Multiplions et divisons par $[\mathrm{S^{2-}}]$ et $[\mathrm{HS^-}]$ (concentrations en $\mathrm{mol\,L^{-1}}$, $c^\circ=1$) :
$$K=\frac{[\mathrm{Co^{2+}}][\mathrm{H_2S}]}{[\mathrm{H^+}]^2}=[\mathrm{Co^{2+}}][\mathrm{S^{2-}}]\cdot\frac{[\mathrm{HS^-}]}{[\mathrm{H^+}][\mathrm{S^{2-}}]}\cdot\frac{[\mathrm{H_2S}]}{[\mathrm{H^+}][\mathrm{HS^-}]}=\frac{K_s}{K_{A2}K_{A1}}.$$
Numériquement : $K=\frac{10^{-20{,}4}}{10^{-13{,}0}\times10^{-7{,}0}}=10^{-0{,}4}\approx0{,}398$, et $\sqrt K=10^{-0{,}2}\approx0{,}631$.

**3. Tableau d'avancement dans l'acide seul** (par litre, $s$ = solubilité) :

| | $\mathrm{H^+}$ | $\mathrm{Co^{2+}}$ | $\mathrm{H_2S}$ |
|---|---|---|---|
| initial | $c_0$ | $0$ | $0$ |
| équilibre | $c_0-2s$ | $s$ | $s$ |

**4. Résolution.** La loi d'action des masses donne
$$\frac{s^2}{(c_0-2s)^2}=K\iff\frac s{c_0-2s}=\sqrt K\iff s(1+2\sqrt K)=\sqrt K\,c_0,$$
en prenant la racine positive (toutes les quantités sont positives). Donc
$$s=\frac{\sqrt K\,c_0}{1+2\sqrt K}=\frac{0{,}631\times0{,}05}{1+1{,}262}=\frac{3{,}155\times10^{-2}}{2{,}262}\approx1{,}4\times10^{-2}\ \mathrm{mol\,L^{-1}}.$$

**5. Vérification de l'hypothèse.** $[\mathrm{H^+}]=c_0-2s=0{,}05-0{,}0279=2{,}2\times10^{-2}\ \mathrm{mol\,L^{-1}}$, soit $\mathrm{pH}=1{,}7<7$ : $\mathrm{H_2S}$ prédomine bien, et $[\mathrm{S^{2-}}]$ et $[\mathrm{HS^-}]$ sont négligeables. Remarque : si l'on avait négligé la consommation d'acide ($[\mathrm{H^+}]\approx c_0$), on aurait trouvé $s=\sqrt Kc_0=3{,}2\times10^{-2}$, ce qui consommerait $2s=6{,}3\times10^{-2}>c_0$ : c'est absurde, et la consommation d'acide doit être prise en compte.

**6. Mélange avec $\mathrm{H_2S}$ à $c_0$.** La même réaction a lieu, mais $\mathrm{H_2S}$ est initialement présent : $[\mathrm{H^+}]=c_0-2s$, $[\mathrm{Co^{2+}}]=s$, $[\mathrm{H_2S}]=c_0+s$. ($\mathrm{H_2S}$, acide faible de $\mathrm pK_A=7$, ne se dissocie quasiment pas en milieu acide fort.) La loi d'action des masses donne
$$\frac{s(c_0+s)}{(c_0-2s)^2}=K\iff s^2+c_0s=K(c_0^2-4c_0s+4s^2)\iff(1-4K)s^2+(1+4K)c_0s-Kc_0^2=0.$$

**7. Résolution numérique.** Posons $s=yc_0$ : $(1-4K)y^2+(1+4K)y-K=0$, avec $1-4K=-0{,}592$ et $1+4K=2{,}592$. Soit $0{,}592\,y^2-2{,}592\,y+0{,}398=0$ :
$$y=\frac{2{,}592\pm\sqrt{2{,}592^2-4\times0{,}592\times0{,}398}}{2\times0{,}592}=\frac{2{,}592\pm\sqrt{5{,}777}}{1{,}184}=\frac{2{,}592\pm2{,}404}{1{,}184}.$$
La racine $y\approx4{,}2$ est exclue (il faut $s<\frac{c_0}2$, c'est-à-dire $y<0{,}5$). Donc $y=\frac{0{,}188}{1{,}184}\approx0{,}159$ et
$$s\approx0{,}159\times0{,}05\approx8{,}0\times10^{-3}\ \mathrm{mol\,L^{-1}}.$$

**8. Interprétation.** La solubilité est divisée par environ 1,7 : $\mathrm{H_2S}$ étant un produit de la dissolution, sa présence initiale déplace l'équilibre vers la gauche (effet d'ion commun, loi de modération).
"""

D['c-redox-3'] = r"""
**1. Règle du gamma.** Classons les couples sur une échelle de potentiels : $E_1^\circ(\mathrm{MnO_4^-/MnO_2})=1{,}70$ V $>E_2^\circ(\mathrm{MnO_2/Mn^{2+}})=1{,}23$ V. L'oxydant le plus fort, $\mathrm{MnO_4^-}$ (du couple au potentiel le plus élevé), réagit sur le réducteur le plus fort, $\mathrm{Mn^{2+}}$ (du couple au potentiel le plus bas). Leurs domaines de prédominance sont disjoints : ils réagissent (réaction quasi totale, voir 2) et ne peuvent pas coexister. Le produit commun, $\mathrm{MnO_2}$, est l'espèce stable : c'est une **médiamutation**.

**2. Demi-équations à $\mathrm{pH}=0$** (équilibrées en O avec $\mathrm{H_2O}$, en H avec $\mathrm{H^+}$, en charges avec $e^-$) :
$$\mathrm{MnO_4^-}+4\,\mathrm{H^+}+3\,e^-=\mathrm{MnO_{2(s)}}+2\,\mathrm{H_2O}\qquad(1)$$
$$\mathrm{MnO_{2(s)}}+4\,\mathrm{H^+}+2\,e^-=\mathrm{Mn^{2+}}+2\,\mathrm{H_2O}\qquad(2)$$

**3. Bilan.** Pour échanger 6 électrons, on fait $2\times(1)$ dans le sens direct, plus $3\times(2)$ dans le sens inverse :
$$2\,\mathrm{MnO_4^-}+8\,\mathrm{H^+}+6\,e^-\to2\,\mathrm{MnO_2}+4\,\mathrm{H_2O}$$
$$3\,\mathrm{Mn^{2+}}+6\,\mathrm{H_2O}\to3\,\mathrm{MnO_2}+12\,\mathrm{H^+}+6\,e^-$$
Après simplification ($8\,\mathrm{H^+}$ d'un côté, $12$ de l'autre ; $4\,\mathrm{H_2O}$ d'un côté, $6$ de l'autre) :
$$2\,\mathrm{MnO_4^-}+3\,\mathrm{Mn^{2+}}+2\,\mathrm{H_2O}=5\,\mathrm{MnO_{2(s)}}+4\,\mathrm{H^+}.$$

**4. Constante d'équilibre.** À l'équilibre, les potentiels des deux couples sont égaux. Pour une réaction échangeant $n$ électrons, à 298 K, $\log K=\frac{n(E^\circ_{\mathrm{ox}}-E^\circ_{\mathrm{red}})}{0{,}059}$, d'où
$$\log K=\frac{6\times(1{,}70-1{,}23)}{0{,}059}=\frac{2{,}82}{0{,}059}\approx47{,}8,\qquad K\approx10^{47{,}8}.$$
La réaction est quantitative.

**5. Potentiel du couple $\mathrm{MnO_4^-/Mn^{2+}}$.** Les potentiels ne s'additionnent pas, mais les enthalpies libres standard si : $\Delta_rG^\circ=-nFE^\circ$. Or la demi-équation (3), $\mathrm{MnO_4^-}+8\,\mathrm{H^+}+5\,e^-=\mathrm{Mn^{2+}}+4\,\mathrm{H_2O}$, est la somme de (1) et (2). Donc
$$-5FE_3^\circ=-3FE_1^\circ-2FE_2^\circ\quad\Longrightarrow\quad E_3^\circ=\frac{3E_1^\circ+2E_2^\circ}5=\frac{3\times1{,}70+2\times1{,}23}5=\frac{5{,}10+2{,}46}5=1{,}51\ \mathrm V.$$

**6. Quantités initiales.** $n(\mathrm{Mn^{2+}})=c\,V_1=0{,}100\times10{,}0\times10^{-3}=1{,}00\times10^{-3}$ mol, et de même $n(\mathrm{MnO_4^-})=1{,}00\times10^{-3}$ mol.

**7. Réactif limitant.** La réaction étant totale, on compare les rapports $\frac{n_i}{\nu_i}$ : $\frac{1{,}00\times10^{-3}}2=5{,}0\times10^{-4}$ pour $\mathrm{MnO_4^-}$, et $\frac{1{,}00\times10^{-3}}3=3{,}33\times10^{-4}$ pour $\mathrm{Mn^{2+}}$. $\mathrm{Mn^{2+}}$ est limitant et $\xi_{\max}=3{,}33\times10^{-4}$ mol.

**8. Masse de $\mathrm{MnO_2}$.** $n(\mathrm{MnO_2})=5\,\xi_{\max}=1{,}67\times10^{-3}$ mol. Avec $M(\mathrm{MnO_2})=54{,}9+2\times16{,}0=86{,}9\ \mathrm{g\,mol^{-1}}$ :
$$m=1{,}67\times10^{-3}\times86{,}9\approx0{,}145\ \mathrm g.$$
Il reste $1{,}00\times10^{-3}-2\xi_{\max}=3{,}3\times10^{-4}$ mol de $\mathrm{MnO_4^-}$ en excès (la solution reste violette).
"""

D['c-thermo-4'] = r"""
**1. Conditions d'équilibre.** Pour chaque réaction, les solides ont une activité égale à 1, donc à l'équilibre $K_i=\frac{P_{\mathrm{CO_2}}}{P^\circ}$, où $P_{\mathrm{CO_2}}=P$ est la pression totale ($\mathrm{CO_2}$ est le seul gaz). L'équilibre (1) impose $P=K_1P^\circ=20$ kPa et l'équilibre (2) impose $P=K_2P^\circ=40$ kPa : les deux équilibres ne peuvent pas être réalisés simultanément (système monovariant pour chacun).

**2. Sens d'évolution initial.** Le volume étant très grand, avec $5$ mol de gaz au plus, $P=\frac{nRT}V$ est très faible : $Q_i=\frac P{P^\circ}<K_1<K_2$. Les deux réactions évoluent dans le sens direct (décomposition). Elles ne peuvent pas atteindre l'équilibre, car $P$ resterait trop faible : elles sont totales jusqu'à la disparition des carbonates (rupture d'équilibre).

**3. Composition.** Chaque mole de carbonate libère une mole de $\mathrm{CO_2}$ : on obtient $1{,}0$ mol de $\mathrm{CaO}$, $1{,}0$ mol de $\mathrm{MgO}$ et $3{,}0+1{,}0+1{,}0=5{,}0$ mol de $\mathrm{CO_2}$.

**4. Données numériques.** $T=820+273=1093$ K, $RT=8{,}314\times1093\approx9{,}09\times10^3\ \mathrm{J\,mol^{-1}}$.

**5. Première branche : $P=\frac{5RT}V$.** Tant que $P<20$ kPa, aucune recarbonatation n'est possible : $n(\mathrm{CO_2})=5$ mol et $P=\frac{5RT}V$ (hyperbole). $P$ atteint $20$ kPa pour
$$V_1=\frac{5RT}{2{,}0\times10^4}=\frac{4{,}54\times10^4}{2{,}0\times10^4}\approx2{,}27\ \mathrm{m^3}.$$

**6. Premier palier à 20 kPa.** Si l'on continue à comprimer, $P$ ne peut dépasser $K_1P^\circ$ tant que $\mathrm{CaO}$ est présent : $\mathrm{CaO}+\mathrm{CO_2}\to\mathrm{CaCO_3}$ consomme du gaz et maintient $P=20$ kPa. On a alors $n(\mathrm{CO_2})=\frac{PV}{RT}$, qui décroît de 5 à 4 mol quand le mol de $\mathrm{CaO}$ est entièrement recarbonaté, c'est-à-dire pour
$$V_1'=\frac{4RT}{2{,}0\times10^4}\approx1{,}82\ \mathrm{m^3}.$$
(À 20 kPa $<K_2P^\circ$, $\mathrm{MgO}$ ne se recarbonate pas.)

**7. Deuxième branche : $P=\frac{4RT}V$.** Plus de $\mathrm{CaO}$ : $n(\mathrm{CO_2})=4$ mol et $P$ croît jusqu'à $40$ kPa en
$$V_2=\frac{4RT}{4{,}0\times10^4}\approx0{,}909\ \mathrm{m^3}.$$

**8. Second palier à 40 kPa.** $\mathrm{MgO}$ se recarbonate à $P=40$ kPa jusqu'à épuisement, donc jusqu'à $n(\mathrm{CO_2})=3$ mol :
$$V_2'=\frac{3RT}{4{,}0\times10^4}\approx0{,}682\ \mathrm{m^3}.$$

**9. Dernière branche.** Pour $V<V_2'$, il ne reste que les deux carbonates et $3$ mol de $\mathrm{CO_2}$ : $P=\frac{3RT}V$.

**10. Allure de la courbe.**

| $V$ ($\mathrm{m^3}$) | $>2{,}27$ | $2{,}27\to1{,}82$ | $1{,}82\to0{,}909$ | $0{,}909\to0{,}682$ | $<0{,}682$ |
|---|---|---|---|---|---|
| $P$ | $5RT/V$ | $20$ kPa | $4RT/V$ | $40$ kPa | $3RT/V$ |
| solides | $\mathrm{CaO,MgO}$ | $\mathrm{CaO,CaCO_3,MgO}$ | $\mathrm{CaCO_3,MgO}$ | $\mathrm{CaCO_3,MgO,MgCO_3}$ | $\mathrm{CaCO_3,MgCO_3}$ |

La courbe $P(V)$ est formée de trois arcs d'hyperbole reliés par deux paliers horizontaux, comme les paliers de changement d'état sur une isotherme d'Andrews.
"""

D['c-thermo-6'] = r"""
**1. Équation.** $\mathrm{N_{2(g)}}+3\,\mathrm{H_{2(g)}}=2\,\mathrm{NH_{3(g)}}$ ; $\Delta n_{\mathrm{gaz}}=2-4=-2$.

**2.(a) Quotient de réaction.** Notons $N=a+b+c$ la quantité totale de gaz et $P$ la pression totale. Pour un mélange idéal de gaz parfaits, $P_i=x_iP=\frac{n_i}NP$, donc
$$Q=\frac{(P_{\mathrm{NH_3}}/P^\circ)^2}{(P_{\mathrm{N_2}}/P^\circ)(P_{\mathrm{H_2}}/P^\circ)^3}=\frac{x_{\mathrm{NH_3}}^2}{x_{\mathrm{N_2}}x_{\mathrm{H_2}}^3}\Big(\frac{P^\circ}P\Big)^2=\frac{c^2/N^2}{(a/N)(b/N)^3}\Big(\frac{P^\circ}P\Big)^2=\frac{c^2N^2}{ab^3}\Big(\frac{P^\circ}P\Big)^2.$$
À l'équilibre, $Q=K^\circ(T)$ : c'est la relation entre $a$, $b$ et $c$ (à $T$ et $P$ données).

**Méthode pour (b) à (e).** Juste après l'ajout d'une petite quantité $\mathrm dn_i$ (à $T$ et $P$ fixées), $Q$ varie de $\mathrm dQ$ avec $\mathrm d\ln Q=\frac{\partial\ln Q}{\partial n_i}\,\mathrm dn_i$. Si $Q$ devient $>K^\circ$, le système évolue dans le sens indirect ; si $Q<K^\circ$, dans le sens direct. On utilise
$$\ln Q=2\ln c+2\ln N-\ln a-3\ln b+\text{cste},\qquad N=a+b+c(+n_{\mathrm{He}}),$$
en n'oubliant pas que $N$ dépend aussi de $n_i$ : $\frac{\partial\ln N}{\partial n_i}=\frac1N$.

**(b) Ajout de $\mathrm{NH_3}$.** $\frac{\partial\ln Q}{\partial c}=\frac2c+\frac2N>0$. $Q$ augmente et devient $>K^\circ$ : évolution dans le **sens indirect** (décomposition de $\mathrm{NH_3}$), conforme à la loi de modération.

**(c) Ajout de $\mathrm{H_2}$.** $\frac{\partial\ln Q}{\partial b}=\frac2N-\frac3b$. Comme $b<N$, $\frac3b>\frac3N>\frac2N$ : la dérivée est négative. $Q<K^\circ$ : évolution dans le **sens direct**.

**(d) Ajout de $\mathrm{N_2}$.**
$$\frac{\partial\ln Q}{\partial a}=\frac2N-\frac1a=\frac{2a-N}{aN},$$
du signe de $2a-N$, c'est-à-dire de $x_{\mathrm{N_2}}-\frac12$.
- Si $x_{\mathrm{N_2}}<\frac12$ : $Q$ diminue, **sens direct**.
- Si $x_{\mathrm{N_2}}>\frac12$ : $Q$ augmente, **sens indirect**. Ajouter un réactif fait alors consommer… ce réactif à l'envers !

On ne peut donc pas conclure sans connaître la composition. Explication : à $P$ constante, ajouter $\mathrm{N_2}$ dilue aussi $\mathrm{H_2}$, qui intervient à la puissance 3.

**(e) Ajout d'hélium (inerte).** $\mathrm{He}$ n'apparaît que dans $N$ : $\frac{\partial\ln Q}{\partial n_{\mathrm{He}}}=\frac2N>0$. $Q>K^\circ$ : **sens indirect**. À pression totale constante, l'ajout d'un gaz inerte diminue toutes les pressions partielles, comme une baisse de pression ; l'équilibre se déplace vers le côté ayant le plus de moles de gaz (ici les réactifs). (À volume constant, en revanche, les pressions partielles ne changent pas et l'hélium n'a aucun effet.)
"""
