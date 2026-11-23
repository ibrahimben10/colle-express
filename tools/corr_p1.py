
# Indices et corrigés — Chimie, électromagnétisme, ondes
C = {}
def c(id, h1, h2, h3, corrige, reponse=""):
    C[id] = {"indices": [h1.strip(), h2.strip(), h3.strip()], "corrige": corrige.strip(), "reponse": reponse.strip()}

c("c-thermo-1",
r"Seul $\mathrm{O_2}$ est gazeux : exprime la constante d'équilibre $K(T)$ en fonction de la pression mesurée.",
r"$\Delta_rG^\circ(T)=-RT\ln K(T)=\Delta_rH^\circ-T\Delta_rS^\circ$ : écris cette relation aux deux températures.",
r"Soustrais les deux relations (ou utilise Van't Hoff intégrée) pour obtenir $\Delta_rH^\circ$, puis reporte pour $\Delta_rS^\circ$.",
r"""
Les solides ont une activité égale à 1 : $K(T)=\dfrac{P_{\mathrm{O_2}}}{P^\circ}$, soit $K_1=0{,}0466$ et $K_2=0{,}2961$.

Avec $\Delta_rH^\circ$ et $\Delta_rS^\circ$ indépendants de $T$ : $-RT\ln K=\Delta_rH^\circ-T\Delta_rS^\circ$, donc $\ln K=-\dfrac{\Delta_rH^\circ}{RT}+\dfrac{\Delta_rS^\circ}R$. Par différence :
$$\Delta_rH^\circ=\frac{R\ln(K_2/K_1)}{\frac1{T_1}-\frac1{T_2}}=\frac{8{,}314\times\ln(6{,}354)}{6{,}18\times10^{-5}}\approx2{,}49\times10^{5}\ \mathrm{J\,mol^{-1}}.$$
Puis $\Delta_rS^\circ=\dfrac{\Delta_rH^\circ+RT_1\ln K_1}{T_1}\approx178\ \mathrm{J\,K^{-1}\,mol^{-1}}$.

*Commentaires* : $\Delta_rH^\circ>0$ (réaction endothermique, $K$ croît avec $T$, loi de Van't Hoff) ; $\Delta_rS^\circ>0$ cohérent avec la formation d'un gaz ($\Delta n_g=+1$).
""", r"$\Delta_rH^\circ\approx+249\ \mathrm{kJ\,mol^{-1}}$, $\Delta_rS^\circ\approx+178\ \mathrm{J\,K^{-1}\,mol^{-1}}$.")

c("c-sol-2",
r"En milieu acide, les ions sulfure sont protonés en $\mathrm{H_2S}$ : écris la réaction de dissolution prépondérante.",
r"$\mathrm{CoS_{(s)}+2H^+=Co^{2+}+H_2S}$, de constante $K=\dfrac{K_s}{K_{A1}K_{A2}}$.",
r"Fais un tableau d'avancement : $[\mathrm{Co^{2+}}]=s$, $[\mathrm{H^+}]=c_0-2s$, $[\mathrm{H_2S}]=s$ (ou $c_0+s$ dans la question 2).",
r"""
**Réaction prépondérante.** En milieu acide ($\mathrm{pH}<7$), le soufre dissous est sous forme $\mathrm{H_2S}$ :
$$\mathrm{CoS_{(s)}+2H^+=Co^{2+}+H_2S},\qquad K=\frac{K_s}{K_{A1}K_{A2}}=10^{-20{,}4+20}=10^{-0{,}4}\approx0{,}40.$$

**1.** Tableau d'avancement (par litre) : $[\mathrm{Co^{2+}}]=[\mathrm{H_2S}]=s$, $[\mathrm{H^+}]=c_0-2s$. À l'équilibre :
$$\frac{s^2}{(c_0-2s)^2}=K\ \Rightarrow\ s=\frac{\sqrt K\,c_0}{1+2\sqrt K}\approx1{,}4\times10^{-2}\ \mathrm{mol\,L^{-1}}.$$
Vérification : $[\mathrm{H^+}]\approx2{,}2\times10^{-2}$, $\mathrm{pH}\approx1{,}7$ : le milieu reste bien acide ($\mathrm{H_2S}$ prédomine). (Si l'on néglige la consommation d'acide, $s\approx\sqrt Kc_0=3{,}2\times10^{-2}$, ce qui est incohérent : il faudrait $2s>c_0$.)

**2.** Avec $\mathrm{H_2S}$ initialement à $c_0$ : $[\mathrm{H_2S}]=c_0+s$ et
$$\frac{s(c_0+s)}{(c_0-2s)^2}=K\ \Rightarrow\ (1-4K)s^2+(1+4K)c_0s-Kc_0^2=0,$$
d'où $s\approx8{,}0\times10^{-3}\ \mathrm{mol\,L^{-1}}$ : la solubilité diminue (effet d'ion commun, l'équilibre est déplacé vers la gauche).
""", r"$s\approx1{,}4\times10^{-2}$ puis $8{,}0\times10^{-3}\ \mathrm{mol\,L^{-1}}$.")

c("c-redox-3",
r"Compare les potentiels : $\mathrm{MnO_4^-}$ est l'oxydant le plus fort, $\mathrm{Mn^{2+}}$ le réducteur le plus fort ; leurs domaines sont-ils disjoints ?",
r"Écris la médiamutation $\mathrm{2MnO_4^-+3Mn^{2+}+2H_2O=5MnO_2+4H^+}$ : combien d'électrons sont échangés ? $\log K=\frac{n(E_1^\circ-E_2^\circ)}{0{,}059}$.",
r"Pour $E_3^\circ$, additionne les enthalpies libres standard : $5E_3^\circ=3E_1^\circ+2E_2^\circ$. Pour la masse, détermine le réactif limitant.",
r"""
**1.** $E_1^\circ(\mathrm{MnO_4^-/MnO_2})>E_2^\circ(\mathrm{MnO_2/Mn^{2+}})$ : $\mathrm{MnO_4^-}$ (oxydant du couple 1) et $\mathrm{Mn^{2+}}$ (réducteur du couple 2) ont des domaines de prédominance disjoints ; ils réagissent selon une réaction quasi totale et ne peuvent coexister.

**2.** Demi-équations : $\mathrm{MnO_4^-+4H^++3e^-=MnO_2+2H_2O}$ et $\mathrm{MnO_2+4H^++2e^-=Mn^{2+}+2H_2O}$. Bilan (6 électrons) :
$$\mathrm{2MnO_4^-+3Mn^{2+}+2H_2O=5MnO_{2(s)}+4H^+},\qquad\log K=\frac{6(1{,}70-1{,}23)}{0{,}059}\approx47{,}8.$$
Réaction totale.

**3.** $\Delta_rG^\circ$ s'additionnent : $-5FE_3^\circ=-3FE_1^\circ-2FE_2^\circ$, donc
$$E_3^\circ(\mathrm{MnO_4^-/Mn^{2+}})=\frac{3\times1{,}70+2\times1{,}23}5=1{,}51\ \mathrm V.$$

**4.** $n(\mathrm{Mn^{2+}})=n(\mathrm{MnO_4^-})=1{,}00\times10^{-3}$ mol. Avec les proportions $3:2$, $\mathrm{Mn^{2+}}$ est limitant : $\xi=\frac{1{,}00\times10^{-3}}3$, d'où $n(\mathrm{MnO_2})=5\xi=1{,}67\times10^{-3}$ mol et, avec $M(\mathrm{MnO_2})=86{,}9\ \mathrm{g\,mol^{-1}}$ :
$$m\approx0{,}145\ \mathrm g.$$
""", r"$\log K\approx47{,}8$ ; $E_3^\circ=1{,}51$ V ; $m(\mathrm{MnO_2})\approx0{,}145$ g.")

c("c-thermo-4",
r"Seul $\mathrm{CO_2}$ est gazeux : chaque équilibre fixe la pression ($P=K_iP^\circ$). Les deux peuvent-ils coexister ?",
r"Dans un très grand volume, $P$ initiale est très faible : les deux carbonates se décomposent entièrement. Combien de moles de $\mathrm{CO_2}$ obtiens-tu ?",
r"En comprimant, $P=nRT/V$ augmente jusqu'à $0{,}20$ bar (palier tant que $\mathrm{CaO}$ se recarbonate), puis jusqu'à $0{,}40$ bar (palier pour $\mathrm{MgO}$).",
r"""
**1.** Seul $\mathrm{CO_2}$ est gazeux : l'équilibre (1) impose $P=K_1P^\circ=20$ kPa, l'équilibre (2) $P=40$ kPa ; ils ne peuvent coexister. Le volume étant très grand, la pression initiale est inférieure aux deux valeurs : les deux réactions avancent jusqu'à disparition des carbonates. **État initial : $1{,}0$ mol $\mathrm{CaO}$, $1{,}0$ mol $\mathrm{MgO}$, $5{,}0$ mol $\mathrm{CO_2}$.**

**2.** À $T=1093$ K, $RT\approx9{,}09\times10^3\ \mathrm{J\,mol^{-1}}$.
- $V>V_1$ : $P=\frac{5RT}V$ (hyperbole). $P$ atteint $20$ kPa pour $V_1=\frac{5RT}{2\times10^4}\approx2{,}27\ \mathrm{m^3}$.
- $V_1\ge V\ge V_1'$ : **palier** à $P=20$ kPa ; $\mathrm{CaO}$ se recarbonate, $n(\mathrm{CO_2})=\frac{PV}{RT}$ passe de 5 à 4 mol, atteint en $V_1'\approx1{,}82\ \mathrm{m^3}$.
- $V_1'\ge V\ge V_2$ : $P=\frac{4RT}V$ jusqu'à $40$ kPa en $V_2\approx0{,}909\ \mathrm{m^3}$.
- $V_2\ge V\ge V_2'$ : **palier** à $P=40$ kPa ($\mathrm{MgO}$ se recarbonate), jusqu'à $n=3$ mol en $V_2'\approx0{,}682\ \mathrm{m^3}$.
- $V<V_2'$ : $P=\frac{3RT}V$.

La courbe $P(V)$ est une succession d'hyperboles et de deux paliers horizontaux (« courbe en escalier »), analogue aux paliers de changement d'état.
""", r"Paliers à 20 kPa ($V$ de 2,27 à 1,82 m³) et 40 kPa (0,909 à 0,682 m³).")

c("c-thermo-6",
r"Exprime $K^\circ$ avec les fractions molaires : $K^\circ=\dfrac{x_{\mathrm{NH_3}}^2}{x_{\mathrm{N_2}}x_{\mathrm{H_2}}^3}\Big(\dfrac{P^\circ}P\Big)^2$.",
r"Écris le quotient $Q$ en fonction des quantités $a,b,c$ et de $n_{\mathrm{tot}}$ à $P$ fixée, puis étudie le signe de $\dfrac{\partial\ln Q}{\partial n_i}$ quand on ajoute un peu de l'espèce $i$.",
r"Si $Q$ devient $>K^\circ$ l'équilibre est déplacé dans le sens indirect, et inversement. Pour $\mathrm{N_2}$, le signe dépend de $x_{\mathrm{N_2}}$ comparé à $\frac12$.",
r"""
**1.** $\mathrm{N_{2(g)}+3H_{2(g)}=2NH_{3(g)}}$.

**2.(a)** Avec $N=a+b+c$ :
$$K^\circ=\frac{c^2N^2}{ab^3}\Big(\frac{P^\circ}P\Big)^2.$$
À $T$ et $P$ fixées, après un petit ajout, $Q=\frac{n_{\mathrm{NH_3}}^2N^2}{n_{\mathrm{N_2}}n_{\mathrm{H_2}}^3}\big(\frac{P^\circ}P\big)^2$, et l'on compare $Q$ à $K^\circ$ via $\frac{\partial\ln Q}{\partial n_i}$.

**(b) Ajout de $\mathrm{NH_3}$** : $\frac{\partial\ln Q}{\partial c}=\frac2c+\frac2N>0$, donc $Q>K^\circ$ : évolution dans le **sens indirect** (décomposition de $\mathrm{NH_3}$).

**(c) Ajout de $\mathrm{H_2}$** : $\frac{\partial\ln Q}{\partial b}=\frac2N-\frac3b<0$ (car $b<N$) : $Q<K^\circ$, **sens direct**.

**(d) Ajout de $\mathrm{N_2}$** : $\frac{\partial\ln Q}{\partial a}=\frac2N-\frac1a$, du signe de $2a-N$. Si $x_{\mathrm{N_2}}<\frac12$ : sens direct ; si $x_{\mathrm{N_2}}>\frac12$ : sens **indirect**. On ne peut pas conclure sans connaître la composition : ajouter un réactif peut déplacer l'équilibre dans le sens de sa formation !

**(e) Ajout d'hélium** (inerte) : $\frac{\partial\ln Q}{\partial n_{\mathrm{He}}}=\frac2N>0$ : **sens indirect**. À pression totale constante, la dilution diminue les pressions partielles, comme une baisse de pression : l'équilibre se déplace vers le plus grand nombre de moles de gaz.
""", r"$\mathrm{NH_3}$ : indirect ; $\mathrm{H_2}$ : direct ; $\mathrm{N_2}$ : dépend de $x_{\mathrm{N_2}}\lessgtr\frac12$ ; He : indirect.")

c("c-electro-3",
r"Les courbes sont des droites de Tafel ($E$ affine en $\log|j|$) : trace-les en $E$ fonction de $\log|j|$, puis en $j(E)$.",
r"Au potentiel de corrosion, il n'y a pas de courant global : $j_a=|j_c|=j_{\mathrm{cor}}$. Égale les deux expressions de $E$.",
r"La vitesse de corrosion se déduit de la loi de Faraday : épaisseur dissoute par unité de temps $v=\dfrac{j_{\mathrm{cor}}M}{2\mathcal F\mu}$.",
r"""
**1.** $j_a(E)$ croît exponentiellement au-delà de $E\approx-0{,}2$ V (oxydation du zinc, système lent), $j_c(E)$ est négatif et croît en valeur absolue quand $E$ diminue (réduction de $\mathrm H^+$ sur le zinc, très lente : forte surtension). En coordonnées $(\log|j|,E)$ : deux droites de Tafel, l'une montante, l'autre descendante.

**2.** $\mathrm{Zn=Zn^{2+}+2e^-}$ ; $\mathrm{2H^++2e^-=H_2}$ ; bilan : $\mathrm{Zn+2H^+=Zn^{2+}+H_2}$.

**3.** À $E_{\mathrm{cor}}$, $j_a=|j_c|=j_{\mathrm{cor}}$ :
$$0{,}0774\log j-0{,}1956=-0{,}0780\log j-0{,}778\ \Rightarrow\ \log j_{\mathrm{cor}}=-3{,}75,$$
$$j_{\mathrm{cor}}\approx1{,}8\times10^{-4}\ \mathrm{A\,cm^{-2}},\qquad E_{\mathrm{cor}}\approx-0{,}49\ \mathrm V.$$

**4.** Par unité de surface, $j_{\mathrm{cor}}$ dissout $\frac{j_{\mathrm{cor}}}{2\mathcal F}$ mol de zinc par seconde, soit une épaisseur
$$v=\frac{j_{\mathrm{cor}}M_{\mathrm{Zn}}}{2\mathcal F\mu_{\mathrm{Zn}}}=\frac{1{,}79\times0{,}0654}{2\times96\,490\times7140}\approx8{,}5\times10^{-11}\ \mathrm{m\,s^{-1}}$$
($j$ converti en $1{,}79\ \mathrm{A\,m^{-2}}$), soit **environ $2{,}7$ mm par an** ($\approx2700\ \mu$m/an) : corrosion rapide en milieu acide.
""", r"$j_{\mathrm{cor}}\approx1{,}8\times10^{-4}\ \mathrm{A\,cm^{-2}}$, $E_{\mathrm{cor}}\approx-0{,}49$ V, $v\approx2{,}7$ mm/an.")

c("c-electro-5",
r"Dans une pile, l'anode est le siège de l'oxydation (pôle $-$), la cathode de la réduction (pôle $+$). Les électrons circulent dans le circuit extérieur de l'anode vers la cathode.",
r"Point de fonctionnement : le courant anodique $i$ et le courant cathodique $-i$ sont égaux en valeur absolue, et $E_C-E_A=Ri$.",
r"Avec $\eta_A=\alpha_Ai$ et $\eta_C=-|\alpha_C|i$, exprime $E_C-E_A$ en fonction de la f.é.m. $e=E_{C,\mathrm{eq}}-E_{A,\mathrm{eq}}$ et de $i$.",
r"""
**1.** Anode (pôle $-$) : $\mathrm{Red_2\to Ox_2+e^-}$ ; cathode (pôle $+$) : $\mathrm{Ox_1+e^-\to Red_1}$. Le courant $i>0$ circule dans $R$ de la cathode vers l'anode ; les électrons vont de l'anode vers la cathode dans le circuit extérieur.

**2–3.** Couples rapides : courbes $i(E)$ sans palier de surtension, qui « décollent » dès les potentiels d'équilibre $E_{A,\mathrm{eq}}$ et $E_{C,\mathrm{eq}}$. Le point de fonctionnement s'obtient en cherchant $E_A$ sur la branche anodique et $E_C$ sur la branche cathodique, avec le même $|i|$ et $E_C-E_A=Ri$ ; les surtensions sont $\eta_A=E_A-E_{A,\mathrm{eq}}>0$ et $\eta_C=E_C-E_{C,\mathrm{eq}}<0$.

**4.** Trois relations : (i) $i_{\mathrm{anode}}=-i_{\mathrm{cathode}}=i$ (conservation de la charge) ; (ii) $U=E_C-E_A$ ; (iii) $U=Ri$ (loi d'Ohm).

**5.** Il manque les lois $i(E)$ de chaque électrode, c'est-à-dire les surtensions en fonction de $i$.

**6.** Avec $\eta_A=\alpha_Ai$ et $\eta_C=\alpha_Ci$ ($\alpha_C<0$) :
$$Ri=E_C-E_A=(E_{C,\mathrm{eq}}-E_{A,\mathrm{eq}})+(\alpha_C-\alpha_A)i\ \Rightarrow\ i=\frac{e}{R+\alpha_A+|\alpha_C|},$$
avec $e$ la f.é.m. à courant nul. Les surtensions jouent le rôle d'une **résistance interne** $r=\alpha_A+|\alpha_C|$ (en plus de la résistance de l'électrolyte, négligée ici).
""", r"$i=\dfrac{e}{R+\alpha_A+|\alpha_C|}$ : les surtensions agissent comme une résistance interne.")

c("c-cin-2",
r"Le volume de $\mathrm{O_2}$ dégagé est proportionnel à la quantité de $\mathrm{N_2O_5}$ ayant réagi.",
r"Pour une cinétique d'ordre 1, $[\mathrm{N_2O_5}]=[\mathrm{N_2O_5}]_0e^{-kt}$, donc $V(t)=V_\infty(1-e^{-kt})$.",
r"Isole $e^{-kt}=\frac{V_\infty-V(t)}{V_\infty}$ à $t=40$ min, puis $t_{1/2}=\frac{\ln2}k$.",
r"""
Le volume de dioxygène est proportionnel à l'avancement : $V(t)=V_\infty\big(1-\frac{[\mathrm{N_2O_5}]}{[\mathrm{N_2O_5}]_0}\big)$. Pour un ordre 1, $[\mathrm{N_2O_5}]=[\mathrm{N_2O_5}]_0e^{-kt}$, d'où
$$V(t)=V_\infty(1-e^{-kt}).$$
À $t=40$ min : $e^{-40k}=\frac{35-19}{35}=\frac{16}{35}$, donc
$$k=\frac1{40}\ln\frac{35}{16}\approx1{,}96\times10^{-2}\ \mathrm{min^{-1}}\ (3{,}3\times10^{-4}\ \mathrm{s^{-1}}),\qquad t_{1/2}=\frac{\ln2}k\approx35\ \mathrm{min}.$$
Le volume molaire n'est pas nécessaire (on ne raisonne que sur des rapports) ; il servirait à calculer la quantité initiale : $n_0(\mathrm{N_2O_5})=2\frac{V_\infty}{V_m}\approx2{,}9\times10^{-3}$ mol.
""", r"$k\approx1{,}96\times10^{-2}\ \mathrm{min^{-1}}$, $t_{1/2}\approx35$ min.")

c("c-cristallo-1",
r"Dans l'empilement hexagonal compact idéal, $c=a\sqrt{8/3}$ et les atomes sont tangents selon $a$ : $a=2r$. On peut aussi utiliser la masse volumique donnée.",
r"Cubique centré : 2 atomes par maille, tangence selon la grande diagonale : $4r=a\sqrt3$.",
r"Compacité $=\dfrac{2\cdot\frac43\pi r^3}{a^3}$ ; masse volumique $\rho=\dfrac{2M}{\mathcal N_Aa^3}$.",
r"""
**1. $\mathrm{Ti}_\alpha$ (h.c.).** Tangence dans le plan de base : $r=\frac a2=147{,}5$ pm. Empilement compact idéal : $c=a\sqrt{8/3}\approx482$ pm. En utilisant plutôt la masse volumique (maille hexagonale de volume $\frac{\sqrt3}2a^2c$ contenant 2 atomes) :
$$c=\frac{2M}{\mathcal N_A\rho\frac{\sqrt3}2a^2}\approx469\ \mathrm{pm},$$
soit $c/a\approx1{,}59$, légèrement inférieur à la valeur idéale $1{,}633$.

**2.(a) Compacité c.c.** 2 atomes par maille, tangence selon la diagonale du cube ($4r=a\sqrt3$) :
$$\mathcal C=\frac{2\cdot\frac43\pi r^3}{a^3}=\frac{\pi\sqrt3}8\approx0{,}68.$$

**(b) $\mathrm{Ti}_\beta$.** $r=\frac{a\sqrt3}4\approx144$ pm et
$$\rho=\frac{2M}{\mathcal N_Aa^3}=\frac{2\times47{,}88\times10^{-3}}{6{,}02\times10^{23}\times(332\times10^{-12})^3}\approx4{,}35\times10^3\ \mathrm{kg\,m^{-3}},$$
plus faible que pour $\mathrm{Ti}_\alpha$ (structure moins compacte : $0{,}68<0{,}74$).
""", r"$r_\alpha=147{,}5$ pm, $c\approx469$ pm ; c.c. : $\mathcal C=0{,}68$, $r_\beta\approx144$ pm, $\rho_\beta\approx4{,}35\times10^3\ \mathrm{kg\,m^{-3}}$.")

c("c-cristallo-2",
r"Dans un réseau c.f.c., où sont les sites octaédriques et tétraédriques ? Combien y en a-t-il par maille ?",
r"Tangence des atomes métalliques selon la diagonale d'une face : $a=2\sqrt2R$. Site O : $r_O=\frac a2-R$ ; site T : $r_T=\frac{a\sqrt3}4-R$.",
r"Compare $r_H=37$ pm aux rayons trouvés. Si H occupe tous les sites tétraédriques (8 par maille, 4 Zr), quelle est la formule ?",
r"""
**1.** Sites **octaédriques** : centre du cube et milieux des 12 arêtes, soit $1+12\times\frac14=4$ par maille. Sites **tétraédriques** : centres des 8 petits cubes d'arête $a/2$, soit 8 par maille.

**2.** Tangence selon la diagonale d'une face : $a\sqrt2=4R$, $a=2\sqrt2R\approx453$ pm.
- Site O : $r_O=\frac a2-R=(\sqrt2-1)R\approx0{,}414R\approx66$ pm.
- Site T : $r_T=\frac{a\sqrt3}4-R=\big(\sqrt{3/2}-1\big)R\approx0{,}225R\approx36$ pm.

**3.** $r_H=37$ pm : le site octaédrique ($66$ pm) accueille H sans déformation ; le site tétraédrique ($36$ pm) est juste un peu trop petit (légère dilatation du réseau).

**4.** En réalité H occupe **tous les sites tétraédriques** : 8 H pour 4 Zr par maille, soit **$\mathrm{ZrH_2}$** (structure de type fluorine : Zr en c.f.c., H aux centres des 8 petits cubes). La dilatation du réseau est observée expérimentalement.

**5.** Stockage de l'hydrogène (pile à combustible, véhicules) : les hydrures métalliques stockent H de façon dense et réversible, plus sûre qu'un gaz comprimé.
""", r"$r_O\approx66$ pm, $r_T\approx36$ pm ; hydrure $\mathrm{ZrH_2}$ (H dans tous les sites T).")

# ---------- Électromagnétisme ----------
c("p-em-1",
r"La charge d'une portion de hauteur $H$ est la somme d'une charge volumique et d'une charge surfacique.",
r"Symétries et invariances : $\vec E=E(r)\vec u_r$. Applique le théorème de Gauss sur un cylindre coaxial de rayon $r$ et de hauteur $H$.",
r"Pour $r>b$, la charge intérieure est nulle (question 1).",
r"""
**1.** $Q=\rho\pi b^2H+\sigma\,2\pi bH=0\ \Rightarrow\ \sigma=-\dfrac{\rho b}2$.

**2.** *Symétries* : tout plan contenant l'axe et $M$, et le plan perpendiculaire à l'axe passant par $M$, sont plans de symétrie : $\vec E(M)$ est radial. *Invariances* par rotation et translation selon $z$ : $\vec E=E(r)\vec u_r$.

*Gauss* sur un cylindre coaxial de rayon $r$, hauteur $H$ (flux nul sur les bases) : $E(r)\,2\pi rH=\dfrac{Q_{\mathrm{int}}}{\varepsilon_0}$.
- $r<b$ : $Q_{\mathrm{int}}=\rho\pi r^2H$, donc $\vec E=\dfrac{\rho r}{2\varepsilon_0}\vec u_r$.
- $r>b$ : $Q_{\mathrm{int}}=0$, donc $\vec E=\vec 0$.

On note la discontinuité en $r=b$ : $E(b^-)-E(b^+)=\frac{\rho b}{2\varepsilon_0}=-\frac\sigma{\varepsilon_0}$, conforme à la relation de passage $\Delta E_n=\sigma/\varepsilon_0$.
""", r"$\sigma=-\rho b/2$ ; $\vec E=\frac{\rho r}{2\varepsilon_0}\vec u_r$ ($r<b$), $\vec 0$ ($r>b$).")

c("p-em-2",
r"Distribution à symétrie sphérique : $\vec E=E(r)\vec u_r$. Applique Gauss sur une sphère de rayon $r$.",
r"$\rho=-\dfrac{3e}{4\pi R^3}$. À l'intérieur $E\propto r$, à l'extérieur champ d'une charge ponctuelle.",
r"Calcule l'énergie $W=\iiint\frac{\varepsilon_0E^2}2d\tau$ en sommant les contributions des deux régions.",
r"""
**1.** Symétrie sphérique : $\vec E=E(r)\vec u_r$, avec $\rho=-\frac{3e}{4\pi R^3}$. Gauss : $4\pi r^2E(r)=\frac{Q_{\mathrm{int}}}{\varepsilon_0}$.
- $r\le R$ : $Q_{\mathrm{int}}=-e\frac{r^3}{R^3}$, donc $\vec E=-\dfrac{er}{4\pi\varepsilon_0R^3}\vec u_r=\dfrac{\rho r}{3\varepsilon_0}\vec u_r$.
- $r>R$ : $\vec E=-\dfrac{e}{4\pi\varepsilon_0r^2}\vec u_r$.

**2.** $W=\iiint\frac{\varepsilon_0E^2}2d\tau$ avec $d\tau=4\pi r^2dr$ :
$$W=\frac{\varepsilon_0}2\Big(\frac e{4\pi\varepsilon_0}\Big)^2\Big[\int_0^R\frac{r^2}{R^6}4\pi r^2dr+\int_R^\infty\frac{4\pi}{r^2}dr\Big]=\frac{e^2}{8\pi\varepsilon_0}\Big(\frac1{5R}+\frac1R\Big)=\frac35\,\frac{e^2}{4\pi\varepsilon_0R}.$$

*Ordre de grandeur* : en égalant $W$ à $m_ec^2$, on obtient un « rayon classique » de l'électron de l'ordre de $10^{-15}$ m.
""", r"$W=\frac35\frac{e^2}{4\pi\varepsilon_0R}$.")

c("p-em-3",
r"$I$ est le flux de $\vec j$ à travers une section du cylindre.",
r"Étudie les symétries : tout plan contenant l'axe est plan de symétrie de la distribution, donc $\vec B$ y est perpendiculaire : $\vec B=B(r)\vec u_\theta$. Que vaut-il sur l'axe ?",
r"Théorème d'Ampère sur un cercle d'axe $Oz$ et de rayon $r$ : distingue $r<b$ et $r>b$.",
r"""
**1.** $I=\iint\vec j\cdot d\vec S=j\pi b^2$.

**2.** Tout plan contenant l'axe et $M$ est plan de symétrie des courants : $\vec B(M)$ lui est orthogonal, donc $\vec B=B\vec u_\theta$ ; par invariances, $B=B(r)$. Sur l'axe, une infinité de plans de symétrie se coupent : $\vec B$ doit être orthogonal à tous, donc $\vec B(r=0)=\vec 0$.

**3.** Ampère sur un cercle de rayon $r$ orienté par $\vec u_\theta$ : $2\pi rB(r)=\mu_0I_{\mathrm{enl}}$.
- $r<b$ : $I_{\mathrm{enl}}=j\pi r^2$, donc $\vec B=\dfrac{\mu_0jr}2\vec u_\theta$.
- $r>b$ : $\vec B=\dfrac{\mu_0jb^2}{2r}\vec u_\theta=\dfrac{\mu_0I}{2\pi r}\vec u_\theta$.

$B$ est continu en $r=b$ (pas de courant surfacique), maximal en $r=b$.
""", r"$\vec B=\frac{\mu_0jr}2\vec u_\theta$ ($r<b$), $\frac{\mu_0I}{2\pi r}\vec u_\theta$ ($r>b$).")

c("p-max-1",
r"Combine Maxwell-Gauss ($\operatorname{div}\vec E=\rho/\varepsilon_0$) et $\vec E=-\overrightarrow{\operatorname{grad}}V$ en régime statique, avec $\rho=0$.",
r"Par symétrie, $V$ ne dépend que de $r$ : $\frac1r\frac{d}{dr}\big(r\frac{dV}{dr}\big)=0$.",
r"Intègre deux fois : $V=A\ln r+B$, puis applique les conditions aux limites.",
r"""
**1.** En statique, $\vec E=-\overrightarrow{\operatorname{grad}}V$ et $\operatorname{div}\vec E=\frac\rho{\varepsilon_0}$ donnent l'équation de Poisson $\Delta V=-\frac\rho{\varepsilon_0}$, qui devient l'équation de **Laplace** $\Delta V=0$ dans une région vide de charges.

**2.** Invariances par rotation et translation : $V=V(r)$. Donc $\frac1r\frac d{dr}\big(r\frac{dV}{dr}\big)=0$, soit $r\frac{dV}{dr}=A$ et $V=A\ln r+B$. Avec $V(a)=0$ et $V(b)=U$ :
$$V(r)=U\,\frac{\ln(r/a)}{\ln(b/a)}.$$

**3.** $\vec E=-\dfrac{dV}{dr}\vec u_r=-\dfrac{U}{r\ln(b/a)}\vec u_r$ (dirigé vers l'intérieur si $U>0$).

*Prolongement* : la charge par unité de longueur du cylindre intérieur est $\lambda=-\frac{2\pi\varepsilon_0U}{\ln(b/a)}$, d'où la capacité linéique du câble coaxial $\frac{2\pi\varepsilon_0}{\ln(b/a)}$.
""", r"$V=U\frac{\ln(r/a)}{\ln(b/a)}$, $\vec E=-\frac{U}{r\ln(b/a)}\vec u_r$.")

c("p-max-2",
r"Compare la durée de propagation $\tau=L/c_0$ à la période $T$.",
r"En ordres de grandeur, $\|\partial\vec E/\partial t\|\sim E/T$ et $\|\overrightarrow{\operatorname{rot}}\vec B\|\sim B/L$ ; relie $E$ et $B$ par Maxwell-Faraday : $E/L\sim B/T$.",
r"Le courant de déplacement est négligeable devant $\overrightarrow{\operatorname{rot}}\vec B$ : que devient Maxwell-Ampère ? Quelle conséquence sur $\operatorname{div}\vec j$ ?",
r"""
**1.** $\tau=\frac L{c_0}=\frac{0{,}3}{3\times10^8}=10^{-9}$ s, et $T\ge\frac1{10^6}=10^{-6}$ s : $\tau\ll T$, l'ARQS est vérifiée.

**2.** Maxwell-Faraday : $\overrightarrow{\operatorname{rot}}\vec E=-\partial_t\vec B$, donc en ordres de grandeur $\frac EL\sim\frac BT$, soit $E\sim\frac{LB}T$. Alors
$$\frac{\|\varepsilon_0\mu_0\partial_t\vec E\|}{\|\overrightarrow{\operatorname{rot}}\vec B\|}\sim\frac{\frac1{c_0^2}\frac ET}{\frac BL}=\frac{L^2}{c_0^2T^2}=\Big(\frac\tau T\Big)^2\approx10^{-6}.$$

**3.** Dans l'ARQS (magnétique), on néglige le courant de déplacement :
$$\operatorname{div}\vec E=\frac\rho{\varepsilon_0},\quad\operatorname{div}\vec B=0,\quad\overrightarrow{\operatorname{rot}}\vec E=-\frac{\partial\vec B}{\partial t},\quad\overrightarrow{\operatorname{rot}}\vec B=\mu_0\vec j.$$
Par rapport au régime stationnaire, seule Maxwell-Faraday garde son terme temporel : c'est l'**induction**. Conséquence : $\operatorname{div}\vec j=0$ (le courant a même intensité en tout point d'une branche).

**4.** Les lois de l'électrocinétique de première année (lois des nœuds et des mailles, condensateurs, bobines, résistances) sont exactement les conséquences de ces équations : en TP (circuits de quelques dizaines de cm, fréquences $\lesssim$ MHz), on est toujours dans l'ARQS.
""", r"$\frac{\|\varepsilon_0\mu_0\partial_t\vec E\|}{\|\mathrm{rot}\,\vec B\|}\sim(L/c_0T)^2\approx10^{-6}$ : courant de déplacement négligé.")

c("p-max-3",
r"Le milieu est neutre et en régime permanent : $\vec E=E(r)\vec u_r$ vérifie $\operatorname{div}\vec E=0$, et le courant $I$ est conservé à travers tout cylindre de rayon $r$.",
r"Avec le champ magnétique, la loi de la quantité de mouvement en régime permanent donne $\vec E=\frac{\vec j}\gamma+\frac{\vec j\wedge\vec B}{n_0e}$ : projette-la sur $\vec u_r$, $\vec u_\theta$, $\vec u_z$.",
r"La composante orthoradiale impose $j_\theta=\frac{\gamma B}{n_0e}j_r$ ; reporte dans la composante radiale pour trouver la nouvelle relation $E(r)$–$j_r(r)$.",
r"""
**1–2. Sans champ magnétique.** $I=2\pi raj(r)$ est indépendant de $r$, donc $j=\frac I{2\pi ar}$ et $E=\frac j\gamma=\frac I{2\pi a\gamma r}$. Avec $U=\int_b^cE\,dr=\frac I{2\pi a\gamma}\ln\frac cb$ :
$$\vec E=\frac U{r\ln(c/b)}\vec u_r,\qquad\vec j=\gamma\vec E,\qquad I=\frac{2\pi a\gamma U}{\ln(c/b)},\qquad R_0=\frac{\ln(c/b)}{2\pi a\gamma}.$$

**3.** $m\frac{d\vec v}{dt}=-e(\vec E+\vec v\wedge\vec B)-\frac m\tau\vec v$ (frottement modélisant les collisions).

**4.** En régime permanent, $\frac m\tau\vec v=-e(\vec E+\vec v\wedge\vec B)$ ; avec $\vec v=-\frac{\vec j}{n_0e}$ et $\gamma=\frac{n_0e^2\tau}m$ :
$$\vec E=\frac{\vec j}\gamma+\frac{\vec j\wedge\vec B}{n_0e}.$$

**5.** Avec $\vec j\wedge\vec B=B(j_\theta\vec u_r-j_r\vec u_\theta)$ et $\vec E=E\vec u_r$ : selon $\vec u_z$ : $j_z=0$ ; selon $\vec u_\theta$ : $0=\frac{j_\theta}\gamma-\frac{Bj_r}{n_0e}$, d'où
$$\tan\theta_H=\frac{j_\theta}{j_r}=\frac{\gamma B}{n_0e}=\frac{e\tau}mB\quad(\text{angle de Hall}).$$

**6.** L'angle entre $\vec j$ et $\vec u_r$ est constant : les lignes de courant sont des **spirales logarithmiques**.

**7.** Selon $\vec u_r$ : $E=\frac{j_r}\gamma(1+\tan^2\theta_H)$. Le courant radial $I=2\pi raj_r$ est inchangé dans sa forme, donc $U=\frac{I\ln(c/b)}{2\pi a\gamma}(1+\tan^2\theta_H)$ :
$$R=R_0(1+\varepsilon),\qquad\varepsilon=\Big(\frac{\gamma B}{n_0e}\Big)^2=\Big(\frac{e\tau B}m\Big)^2.$$
C'est la **magnétorésistance géométrique** (effet Corbino), utilisée pour mesurer la mobilité $\frac{e\tau}m$.
""", r"$R_0=\frac{\ln(c/b)}{2\pi a\gamma}$, $\tan\theta_H=\frac{e\tau B}m$, $R=R_0(1+\varepsilon)$ avec $\varepsilon=\big(\frac{e\tau B}m\big)^2$.")

c("p-ind-2",
r"Oriente le circuit et calcule la f.é.m. induite par le flux coupé (ou la loi de Faraday) : $e=-BD\dot z$ (selon l'orientation).",
r"La force de Laplace $iD\vec u\wedge\vec B$ s'oppose au mouvement : elle vaut $-\frac{B^2D^2}R\dot z$ verticalement.",
r"Écris $m\ddot z+\big(\alpha+\frac{B^2D^2}R\big)\dot z+2kz=0$ (origine à l'équilibre) et identifie le temps d'amortissement de l'enveloppe.",
r"""
On repère la tige par sa cote $z$ (axe vertical ascendant, origine à la position d'équilibre mécanique : le poids est compensé par les ressorts).

**1. Équation électrique.** Le flux de $\vec B$ à travers le circuit varie comme $\Phi=BDz$ (à une constante près, selon l'orientation), d'où $e=-\frac{d\Phi}{dt}=-BD\dot z$ et $i=\frac eR=-\frac{BD\dot z}R$ (auto-induction négligée).

**Équation mécanique.** Force de Laplace sur la tige : $F_z=iDB=-\frac{B^2D^2}R\dot z$. Avec deux ressorts ($2k$) et le frottement :
$$m\ddot z=-2kz-\alpha\dot z-\frac{B^2D^2}R\dot z.$$

**2. Bilan de puissance.** En multipliant par $\dot z$ :
$$\frac d{dt}\Big(\frac12m\dot z^2+kz^2\Big)=-\alpha\dot z^2-Ri^2.$$
L'énergie mécanique (cinétique + élastique + pesanteur, cette dernière incluse via le choix de l'origine) diminue : dissipation par frottement et par **effet Joule** dans $R$. La puissance de la force de Laplace ($-\frac{B^2D^2}R\dot z^2$) est l'opposée de la puissance électrique fournie par la f.é.m. ($ei$) : couplage électromécanique parfait.

**3.** $\ddot z+\frac1\tau\cdot2\dot z+\omega_0^2z=0$ avec $\omega_0^2=\frac{2k}m$ : en régime pseudo-périodique, $z\propto e^{-t/\tau}\cos(\Omega t+\varphi)$ avec
$$\tau=\frac{2m}{\alpha+\frac{B^2D^2}R}.$$
Le champ magnétique renforce l'amortissement (freinage par induction).
""", r"$m\ddot z=-2kz-\big(\alpha+\frac{B^2D^2}R\big)\dot z$ ; $\tau=\frac{2m}{\alpha+B^2D^2/R}$.")

c("p-ind-3",
r"Calcule le flux du champ créé par le solénoïde à travers la bobine plate. Le solénoïde est long : quel est son champ intérieur ?",
r"$B=\mu_0\frac{10N}Di$ à l'intérieur, nul à l'extérieur. Le flux à travers $N$ spires de rayon $R$ vaut $N\,B\,\pi R^2$.",
r"Dans le cas 2, la bobine plate est plus grande que le solénoïde : le champ n'existe que sur la section $\pi R^2$ du solénoïde.",
r"""
**1.** Solénoïde long ($n=\frac{10N}D$ spires par mètre) : $B=\mu_0\frac{10N}Di$, uniforme à l'intérieur, nul à l'extérieur. La bobine plate (rayon $R<2R$) est entièrement dans la zone de champ : $\Phi=NB\pi R^2$, d'où
$$M=\frac\Phi i=\frac{10\mu_0N^2\pi R^2}D.$$

**2.** Bobine plate de rayon $2R$, solénoïde de rayon $R$ : le champ n'est non nul que sur la section du solénoïde, d'aire $\pi R^2$. Le flux est le même :
$$M=\frac{10\mu_0N^2\pi R^2}D.$$

*Vérification* par la symétrie de la mutuelle ($M_{12}=M_{21}$) : on aurait aussi pu calculer le flux du champ de la bobine plate à travers le solénoïde, beaucoup plus difficile. Le résultat ne dépend que de la plus petite des deux sections.
""", r"$M=\frac{10\mu_0N^2\pi R^2}D$ dans les deux cas.")

c("p-ondes-1",
r"Un ressort de raideur $k=\frac{ES}{dx}$ exerce une force proportionnelle à l'allongement relatif : quelle grandeur est $E$ ?",
r"Les deux ressorts reliés à la masselotte $x$ ont pour allongements $u(x+dx)-u(x)$ et $u(x)-u(x-dx)$.",
r"Développe $u(x\pm dx)$ à l'ordre 2 : la somme des forces vaut $\frac{ES}{dx}\,dx^2\,\partial_x^2u$.",
r"""
**1.** $F=k\Delta\ell=ES\frac{\Delta\ell}{dx}$ : $E=\frac{F/S}{\Delta\ell/\ell}$ est homogène à une **pression** (contrainte), en pascals. Il caractérise la raideur intrinsèque du matériau (loi de Hooke : déformation élastique réversible), d'où « module d'élasticité » (acier : $E\approx200$ GPa).

**2.** Pour la masselotte d'abscisse $x$ :
$$\mu S\,dx\,\frac{\partial^2u}{\partial t^2}(x,t)=k\big[u(x+dx)-u(x)\big]-k\big[u(x)-u(x-dx)\big].$$

**3.** $u(x\pm dx)=u\pm dx\,\partial_xu+\frac{dx^2}2\partial_x^2u+o(dx^2)$, donc le crochet vaut $dx^2\,\partial_x^2u$ et
$$\mu S\,dx\,\partial_t^2u=\frac{ES}{dx}\,dx^2\,\partial_x^2u\ \Rightarrow\ \frac{\partial^2u}{\partial x^2}-\frac1{c^2}\frac{\partial^2u}{\partial t^2}=0,\quad c=\sqrt{\frac E\mu}.$$
*A.N.* acier : $c=\sqrt{2\times10^{11}/7800}\approx5\ \mathrm{km\,s^{-1}}$ (vitesse du son dans l'acier).
""", r"$E$ en Pa ; $\partial_x^2u=\frac1{c^2}\partial_t^2u$ avec $c=\sqrt{E/\mu}$.")

c("p-ondes-2",
r"Applique la loi de la quantité de mouvement à un tronçon $dx$ en projection verticale : tension aux deux extrémités, force de rappel.",
r"La composante verticale de la tension en $x$ vaut $T_E\alpha\simeq T_E\partial_xz$ : la résultante sur le tronçon est $T_E\partial_x^2z\,dx$.",
r"Avec une onde $e^{i(\omega t-kx)}$, la relation de dispersion est $k^2=\frac{\omega^2}{c^2}-\frac1{\delta^2}$ : discute le signe de $k^2$.",
r"""
**1.** Tronçon $[x,x+dx]$, de masse $\mu dx$ ; petits angles. Verticalement :
$$\mu\,dx\,\partial_t^2z=T_E\big[\alpha(x+dx)-\alpha(x)\big]-\alpha_r\,dx\,z=T_E\,\partial_x^2z\,dx-\alpha_r\,z\,dx,$$
où $\alpha_r$ est le coefficient de rappel (noté $\alpha$ dans l'énoncé, à ne pas confondre avec l'angle). D'où
$$\frac{\partial^2z}{\partial x^2}-\frac1{c^2}\frac{\partial^2z}{\partial t^2}=\frac z{\delta^2},\qquad c=\sqrt{\frac{T_E}\mu},\quad\delta=\sqrt{\frac{T_E}{\alpha_r}}.$$
(Équation de **Klein-Gordon**.)

**2.** Avec $z=z_0e^{i(\omega t-kx)}$ : $k^2=\frac{\omega^2}{c^2}-\frac1{\delta^2}=\frac{\omega^2-\omega_c^2}{c^2}$, avec $\omega_c=\frac c\delta=\sqrt{\frac{\alpha_r}\mu}$.
- $\omega>\omega_c$ : $k$ réel, **onde progressive dispersive** ; $v_\varphi=\frac c{\sqrt{1-\omega_c^2/\omega^2}}>c$ et $v_g=c\sqrt{1-\omega_c^2/\omega^2}<c$, avec $v_\varphi v_g=c^2$.
- $\omega<\omega_c$ : $k$ imaginaire pur, **onde évanescente** (pas de propagation, amplitude en $e^{-x/\ell}$).

$\omega_c$ est une **pulsation de coupure** : le câble se comporte comme un filtre passe-haut.
""", r"Klein-Gordon ; $k^2=\frac{\omega^2-\omega_c^2}{c^2}$, propagation si $\omega>\omega_c=\sqrt{\alpha/\mu}$.")

c("p-oem-2",
r"Injecte $G=G_0e^{i(\omega t-kx)}$ : $\partial_x\to-ik$, $\partial_t\to i\omega$.",
r"Tu obtiens $k^2=k_0^2\big(1-i\frac{\omega_0}\omega\big)$ : identifie parties réelle et imaginaire de $(k'+ik'')^2$.",
r"Avec $e^{i(\omega t-kx)}=e^{i(\omega t-k'x)}e^{k''x}$ : si $k'>0$ (propagation vers $x>0$), le signe de $k''$ dit si l'amplitude croît ou décroît.",
r"""
**1.** Avec $G=G_0e^{i(\omega t-kx)}$ : $-k^2+\frac{\omega^2}{c^2}-i\frac{\omega\omega_0}{c^2}=0$.

**2.** $\dfrac{k^2}{k_0^2}=1-i\dfrac{\omega_0}\omega$.

**3.** $(k'+ik'')^2=k'^2-k''^2+2ik'k''$, donc $k'^2-k''^2=k_0^2$ et $2k'k''=-k_0^2\frac{\omega_0}\omega<0$ : **$k'k''<0$**.

**4.** $G=G_0e^{k''x}e^{i(\omega t-k'x)}$. Pour une onde se propageant vers les $x$ croissants ($k'>0$), $k''<0$ : l'amplitude décroît en $e^{-|k''|x}$, l'onde est **atténuée** (le terme en $\partial_tG$ est dissipatif). Distance caractéristique $\delta=\frac1{|k''|}$ ; pour $\omega\gg\omega_0$, $k''\approx-\frac{\omega_0}{2c}$, d'où $\delta\approx\frac{2c}{\omega_0}$.
""", r"$k^2=k_0^2(1-i\omega_0/\omega)$ ; $k'k''<0$ : onde atténuée.")

c("p-oem-3",
r"Utilise Maxwell-Faraday : $\partial_tB_y=-\partial_zE_x$ (pour $\vec E=E_x\vec u_x$, $\vec B=B_y\vec u_y$).",
r"La puissance Joule volumique est $p_J=\vec j\cdot\vec E=\gamma E^2$ ; la moyenne de $\cos^2$ vaut $\frac12$.",
r"Intègre $\langle p_J\rangle$ sur le volume $a\times a\times[0,+\infty[$ : $\int_0^\infty e^{-2z/\delta}dz=\frac\delta2$.",
r"""
**1.** Maxwell-Faraday : $\partial_tB_y=-\partial_zE_x$. Or
$$\partial_zE_x=-\frac{E_0}\delta e^{-z/\delta}\big[\cos(\omega t-z/\delta)-\sin(\omega t-z/\delta)\big]=-\frac{\sqrt2E_0}\delta e^{-z/\delta}\cos\Big(\omega t-\frac z\delta+\frac\pi4\Big).$$
En intégrant en temps (sans composante statique) :
$$B(z,t)=\frac{\sqrt2E_0}{\omega\delta}e^{-z/\delta}\sin\Big(\omega t-\frac z\delta+\frac\pi4\Big),$$
déphasé de $\frac\pi4$ par rapport à $\vec E$ (contrairement à une onde dans le vide). Ici $\delta=\sqrt{\frac2{\mu_0\gamma\omega}}$ est l'épaisseur de peau.

**2.** $p_J=\gamma E^2=\gamma E_0^2e^{-2z/\delta}\cos^2(\omega t-z/\delta)$ et $\langle p_J\rangle=\frac{\gamma E_0^2}2e^{-2z/\delta}$.

**3.** $\langle P\rangle=a^2\int_0^\infty\frac{\gamma E_0^2}2e^{-2z/\delta}dz=\frac{\gamma E_0^2a^2\delta}4$. (On vérifie qu'elle égale le flux moyen du vecteur de Poynting entrant en $z=0$.)

**4.** L'onde ne pénètre que sur quelques $\delta$ ; $\delta\propto\omega^{-1/2}$ est plus grand pour l'infrarouge que pour le visible. Le visible est surtout réfléchi par une surface métallique, tandis que l'IR (abondant dans le rayonnement solaire et bien absorbé par la peinture) dépose son énergie en volume : c'est lui qui chauffe la carrosserie.
""", r"$B=\frac{\sqrt2E_0}{\omega\delta}e^{-z/\delta}\sin(\omega t-\frac z\delta+\frac\pi4)$ ; $\langle P\rangle=\frac{\gamma E_0^2a^2\delta}4$.")

c("p-oem-4",
r"Ajoute $\rho_{\mathrm{die}}$ et $\vec j_{\mathrm{die}}$ dans Maxwell-Gauss et Maxwell-Ampère.",
r"Avec $\vec P=\varepsilon_0\chi\vec E$ et $\rho=0$, $\vec j=\vec 0$ : $\operatorname{div}\big(\varepsilon_0(1+\chi)\vec E\big)=0$ et $\overrightarrow{\operatorname{rot}}\vec B=\mu_0\varepsilon_0(1+\chi)\partial_t\vec E$.",
r"Pour la loi de Cauchy, développe $\chi(\omega)$ pour $\omega\ll\omega_0$ puis $n=\sqrt{1+\chi}$ au premier ordre, avec $\omega=\frac{2\pi c}{\lambda_0}$.",
r"""
**1.** $\operatorname{div}\vec E=\frac{\rho+\rho_{\mathrm{die}}}{\varepsilon_0}$, $\operatorname{div}\vec B=0$, $\overrightarrow{\operatorname{rot}}\vec E=-\partial_t\vec B$, $\overrightarrow{\operatorname{rot}}\vec B=\mu_0(\vec j+\vec j_{\mathrm{die}})+\mu_0\varepsilon_0\partial_t\vec E$.

**2.** $\operatorname{div}\vec j_{\mathrm{die}}+\partial_t\rho_{\mathrm{die}}=\partial_t(\operatorname{div}\vec P)-\partial_t(\operatorname{div}\vec P)=0$ : les charges et courants de polarisation se conservent ; ajoutés aux libres, la conservation globale tient toujours.

**3.** Avec $\rho=0$, $\vec j=\vec0$, $\vec P=\varepsilon_0\chi\vec E$ : $\operatorname{div}(\varepsilon_0\varepsilon_r\vec E)=0$ et $\overrightarrow{\operatorname{rot}}\vec B=\mu_0\varepsilon_0\varepsilon_r\partial_t\vec E$ : équations du vide avec $\varepsilon_0\to\varepsilon_0\varepsilon_r$, où $\varepsilon_r=1+\chi$.

**4–5.** $\overrightarrow{\operatorname{rot}}\,\overrightarrow{\operatorname{rot}}\vec E=-\Delta\vec E$ (car $\operatorname{div}\vec E=0$) donne $\Delta\vec E-\frac{\varepsilon_r}{c_0^2}\partial_t^2\vec E=\vec0$ : célérité $c=\frac{c_0}n$, $n=\sqrt{1+\chi}$.

**6.** Avec $\chi_0=\frac{n_0e^2}{\varepsilon_0\kappa}$ et $\omega\ll\omega_0$ : $\chi=\frac{\chi_0}{1-\omega^2/\omega_0^2}\approx\chi_0\big(1+\frac{\omega^2}{\omega_0^2}\big)$. Avec $A=\sqrt{1+\chi_0}$ :
$$n\approx A\Big(1+\frac{\chi_0\omega^2}{2A^2\omega_0^2}\Big)=A+\frac B{\lambda_0^2},\qquad B=\frac{\chi_0}{2A}\Big(\frac{2\pi c_0}{\omega_0}\Big)^2=\frac{2\pi^2c_0^2\chi_0}{A\,\omega_0^2}.$$
C'est la **loi de Cauchy** ($B>0$ : dispersion normale, le bleu est plus dévié que le rouge).
""", r"$\varepsilon_r=1+\chi$, $n=\sqrt{1+\chi}$ ; $n\approx A+B/\lambda_0^2$ avec $A=\sqrt{1+\chi_0}$.")

c("p-oem-5",
r"Le poids et la force magnétique ($v\ll c$) sont négligeables devant la force électrique. En régime sinusoïdal, exprime $\underline{\vec v}$ puis $\underline{\vec j}=\underline\gamma\,\underline{\vec E}$.",
r"Combine Maxwell-Faraday et Maxwell-Ampère (métal neutre) : $\underline k^2=\frac{\omega^2}{c^2}-i\mu_0\omega\underline\gamma$.",
r"Pour $\omega\tau\gg1$, $\underline n^2\approx1-\frac{\omega_p^2}{\omega^2}$ avec $\omega_p^2=\frac{n_0e^2}{\varepsilon_0m}$ : compare $\omega$ à $\omega_p$.",
r"""
**1.** Le poids ($\sim10^{-29}$ N) et la force magnétique ($evB\sim\frac vcevE$) sont négligeables devant $eE$ ; le terme $(\vec v\cdot\overrightarrow{\operatorname{grad}})\vec v$ aussi (petits déplacements).

**2.** En complexes : $i\omega m\underline{\vec v}=-e\underline{\vec E}-\frac m\tau\underline{\vec v}$, donc $\underline{\vec j}=-n_0e\underline{\vec v}=\underline\gamma\underline{\vec E}$ avec $\underline\gamma=\frac{n_0e^2\tau}{m(1+i\omega\tau)}$. Maxwell (avec $\rho=0$) donne $\Delta\underline{\vec E}=\mu_0\partial_t\underline{\vec j}+\frac1{c^2}\partial_t^2\underline{\vec E}$, d'où
$$\underline k^2=\frac{\omega^2}{c^2}-i\mu_0\omega\underline\gamma.$$

**3.** $\underline n^2=\frac{\underline k^2c^2}{\omega^2}=1-\frac{i\underline\gamma}{\varepsilon_0\omega}=1-\frac{\omega_p^2\tau}{\omega(\omega\tau-i)},\qquad\omega_p^2=\frac{n_0e^2}{\varepsilon_0m}.$

**4.** Pour $\omega\tau\gg1$ : $\underline n^2\approx1-\frac{\omega_p^2}{\omega^2}$. A.N. : $\omega_p^2\approx\frac{10^{29}\times10^{-38}}{10^{-11}\times10^{-30}}=10^{32}$, $\omega_p\approx10^{16}\ \mathrm{rad\,s^{-1}}$, soit $\lambda_p=\frac{2\pi c}{\omega_p}\approx0{,}2\ \mu$m (UV).
- $\omega<\omega_p$ (visible, IR) : $\underline n^2<0$, $\underline n$ imaginaire : onde évanescente, **réflexion totale** (éclat métallique).
- $\omega>\omega_p$ (UV lointain) : $\underline n$ réel, l'onde se propage : le métal devient **transparent**.
""", r"$\underline n^2\approx1-\omega_p^2/\omega^2$, $\omega_p\approx10^{16}$ rad/s : transparent pour $\lambda<0{,}2\ \mu$m.")

c("p-ccs-plan",
r"Utilise les symétries (tout plan contenant $M$ et parallèle à $Oz$ est plan de symétrie, ainsi que le plan $z=0$) puis le théorème de Gauss sur un cylindre d'axe parallèle à $Oz$, symétrique par rapport à $z=0$.",
r"À l'intérieur $\vec E=\frac{\rho z}{\varepsilon_0}\vec u_z$, à l'extérieur $\pm\frac{\rho a}{2\varepsilon_0}\vec u_z$ ; $V$ se déduit de $E=-\frac{dV}{dz}$.",
r"La force sur la particule est $qE(z)$ : dans la couche, si $q\rho<0$, c'est une force de rappel linéaire. Que donne sa période ?",
r"""
**1.(a)** Plan infini de charge $\sigma$ : $\vec E=\pm\frac\sigma{2\varepsilon_0}\vec u_z$ selon le côté.

**(b)** Symétries : $\vec E=E(z)\vec u_z$ avec $E(-z)=-E(z)$. Gauss sur un cylindre de section $S$ entre $-z$ et $z$ :
- $|z|\le\frac a2$ : $2SE(z)=\frac{\rho\,2zS}{\varepsilon_0}$, donc $\vec E=\dfrac{\rho z}{\varepsilon_0}\vec u_z$ ;
- $|z|\ge\frac a2$ : $\vec E=\operatorname{sgn}(z)\dfrac{\rho a}{2\varepsilon_0}\vec u_z$.

$E$ est continu, affine dans la couche, constant à l'extérieur.

**(c)** Avec $V(0)=0$ : $V=-\frac{\rho z^2}{2\varepsilon_0}$ dans la couche, $V=-\frac{\rho a|z|}{2\varepsilon_0}+\frac{\rho a^2}{8\varepsilon_0}$ à l'extérieur (parabole raccordée à deux demi-droites).

**2.(a)** Force $F=qE(z)$, particule lâchée en $z_0=\frac a4$.
- Si $q\rho>0$ : force répulsive vers l'extérieur ; la particule sort de la couche et est accélérée indéfiniment (champ uniforme à l'extérieur).
- Si $q\rho<0$ : $m\ddot z=-\frac{|q|\rho}{\varepsilon_0}z$ : **oscillations harmoniques** d'amplitude $\frac a4$ (elle reste dans la couche), de pulsation $\omega=\sqrt{\frac{|q\rho|}{m\varepsilon_0}}$.

**(b)** Oui : en mesurant la période $T$, on obtient $\rho=\frac{4\pi^2m\varepsilon_0}{|q|T^2}$ (si $q/m$ est connu). Dans le cas répulsif, la vitesse à la sortie donne aussi accès à $\rho$ par conservation de l'énergie.
""", r"$\vec E=\frac{\rho z}{\varepsilon_0}\vec u_z$ dedans ; oscillations de pulsation $\sqrt{|q\rho|/(m\varepsilon_0)}$ si $q\rho<0$.")
