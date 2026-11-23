D = {}

D['c-electro-3'] = r"""
**1. Allure des courbes $i(E)$.**
- **Oxydation du zinc** ($j_a>0$) : d'après le modèle, $\log j_a=\frac{E+0{,}1956}{0{,}0774}$, donc $j_a$ croît exponentiellement avec $E$. Le système est lent : il faut une surtension pour obtenir un courant notable.
- **Réduction de $\mathrm{H^+}$ sur le zinc** ($j_c<0$) : $\log|j_c|=-\frac{E+0{,}778}{0{,}0780}$, donc $|j_c|$ croît exponentiellement quand $E$ diminue. La surtension cathodique de $\mathrm{H^+/H_2}$ sur le zinc est importante (système très lent).

En coordonnées $(\log|j|,E)$, on obtient deux **droites de Tafel**, l'une croissante (anodique) et l'autre décroissante (cathodique). Elles se coupent au point de corrosion.

**2. Demi-équations et bilan.**
$$\text{anode : }\mathrm{Zn}=\mathrm{Zn^{2+}}+2\,e^-,\qquad\text{cathode : }2\,\mathrm H^++2\,e^-=\mathrm{H_{2(g)}},$$
$$\text{bilan : }\mathrm{Zn_{(s)}}+2\,\mathrm H^+\to\mathrm{Zn^{2+}}+\mathrm{H_{2(g)}}.$$

**3. Condition de corrosion.** La plaque n'est reliée à aucun circuit extérieur : le courant total est nul. Les électrons produits à l'anode sont consommés à la cathode, donc $I_a=|I_c|$. Les surfaces étant égales, $j_a=|j_c|=j_{\mathrm{cor}}$, au même potentiel $E_{\mathrm{cor}}$ (potentiel mixte).

**3. Résolution.** Posons $x=\log j_{\mathrm{cor}}$ et égalons les deux expressions de $E$ :
$$0{,}0774\,x-0{,}1956=-0{,}0780\,x-0{,}778\iff(0{,}0774+0{,}0780)\,x=-0{,}778+0{,}1956\iff0{,}1554\,x=-0{,}5824,$$
donc $x=-3{,}748$ et
$$j_{\mathrm{cor}}=10^{-3{,}748}\approx1{,}79\times10^{-4}\ \mathrm{A\,cm^{-2}}.$$
En reportant dans la loi anodique : $E_{\mathrm{cor}}=0{,}0774\times(-3{,}748)-0{,}1956=-0{,}290-0{,}196\approx-0{,}49$ V. (Vérification par la loi cathodique : $-0{,}0780\times(-3{,}748)-0{,}778=0{,}292-0{,}778=-0{,}49$ V. ✓)

**4. Définition de la vitesse de corrosion.** C'est l'épaisseur de métal perdue par unité de temps, notée $v=\frac{\mathrm de}{\mathrm dt}$.

**4. Bilan de matière.** Sur une surface $S$, pendant $\mathrm dt$, la charge $j_{\mathrm{cor}}S\,\mathrm dt$ traverse l'interface anodique. Chaque atome de Zn oxydé libère 2 électrons, donc
$$\mathrm dn_{\mathrm{Zn}}=\frac{j_{\mathrm{cor}}S\,\mathrm dt}{2\mathcal F}.$$
Cette quantité correspond à un volume $\frac{M\,\mathrm dn}{\mu}=S\,\mathrm de$. D'où
$$v=\frac{\mathrm de}{\mathrm dt}=\frac{j_{\mathrm{cor}}M_{\mathrm{Zn}}}{2\mathcal F\mu_{\mathrm{Zn}}}.$$

**4. Application numérique (unités SI).** $j_{\mathrm{cor}}=1{,}79\times10^{-4}\ \mathrm{A\,cm^{-2}}=1{,}79\ \mathrm{A\,m^{-2}}$ (car $1\ \mathrm{m^2}=10^4\ \mathrm{cm^2}$) et $M=65{,}4\times10^{-3}\ \mathrm{kg\,mol^{-1}}$ :
$$v=\frac{1{,}79\times65{,}4\times10^{-3}}{2\times96\,490\times7140}=\frac{0{,}117}{1{,}378\times10^9}\approx8{,}5\times10^{-11}\ \mathrm{m\,s^{-1}}.$$
Une année dure $365{,}25\times24\times3600\approx3{,}16\times10^7$ s, donc
$$v\approx8{,}5\times10^{-11}\times3{,}16\times10^7\approx2{,}7\times10^{-3}\ \mathrm{m/an}\approx2700\ \mu\mathrm m/\mathrm{an}.$$
C'est une corrosion rapide (près de 3 mm par an), typique d'un métal réducteur en milieu acide.
"""

D['c-electro-5'] = r"""
**1. Identification des électrodes.** La réaction spontanée est $\mathrm{Ox_1}+\mathrm{Red_2}\to\mathrm{Red_1}+\mathrm{Ox_2}$.
- **Anode** (siège de l'oxydation, pôle $-$) : $\mathrm{Red_2}\to\mathrm{Ox_2}+e^-$, au potentiel $E_A$.
- **Cathode** (siège de la réduction, pôle $+$) : $\mathrm{Ox_1}+e^-\to\mathrm{Red_1}$, au potentiel $E_C$.

**1. Sens des courants.** Les électrons sont produits à l'anode et consommés à la cathode : dans le circuit extérieur, ils vont de l'anode vers la cathode à travers $R$. Le courant $i>0$ circule en sens inverse : dans $R$, de la cathode (pôle $+$) vers l'anode (pôle $-$). Dans la pile, la charge est transportée par les ions (pont salin ou électrolyte).

**2. Courbes intensité-potentiel.** Pour un couple rapide, la courbe $i(E)$ passe par le potentiel d'équilibre de Nernst sans palier de courant nul : un faible écart au potentiel d'équilibre suffit à produire un courant notable.
- Couple 2 (anode) : branche d'oxydation ($i>0$) pour $E>E_{A,\mathrm{eq}}=E_{\mathrm{Nernst}}(\mathrm{Ox_2/Red_2})$.
- Couple 1 (cathode) : branche de réduction ($i<0$) pour $E<E_{C,\mathrm{eq}}=E_{\mathrm{Nernst}}(\mathrm{Ox_1/Red_1})$.

On a $E_{C,\mathrm{eq}}>E_{A,\mathrm{eq}}$ : c'est ce qui rend la réaction spontanée. La f.é.m. à courant nul vaut $e=E_{C,\mathrm{eq}}-E_{A,\mathrm{eq}}>0$.

**3. Point de fonctionnement.** On trace l'horizontale d'ordonnée $+i$ sur la branche anodique, ce qui donne $E_A$, et celle d'ordonnée $-i$ sur la branche cathodique, ce qui donne $E_C$. On ajuste $i$ pour que l'écart $E_C-E_A$ soit égal à $Ri$. Les surtensions sont :
$$\eta_A=E_A-E_{A,\mathrm{eq}}>0,\qquad\eta_C=E_C-E_{C,\mathrm{eq}}<0.$$
La tension aux bornes, $U=E_C-E_A=e+\eta_C-\eta_A$, est donc inférieure à $e$ : les deux surtensions « mangent » une partie de la f.é.m.

**4. Les trois relations vérifiées.**
- (i) **Conservation de la charge** : le courant d'oxydation à l'anode est égal, en valeur absolue, au courant de réduction à la cathode : $i_A=-i_C=i$.
- (ii) **Tension aux bornes** : $U=E_C-E_A$ (résistance de l'électrolyte négligée).
- (iii) **Loi d'Ohm** dans le résistor : $U=Ri$.

**4. Relation manquante.** Ces trois relations ne suffisent pas à déterminer les inconnues $i$, $E_A$, $E_C$ et $U$. Il manque les **lois cinétiques** de chaque électrode, c'est-à-dire les courbes $i(E)$, ou de façon équivalente les surtensions $\eta_A(i)$ et $\eta_C(i)$.

**5. Modèle linéaire.** Avec $\eta_A=\alpha_Ai$ ($\alpha_A>0$) et $\eta_C=\alpha_Ci$ ($\alpha_C<0$) :
$$E_A=E_{A,\mathrm{eq}}+\alpha_Ai,\qquad E_C=E_{C,\mathrm{eq}}+\alpha_Ci.$$
En combinant (ii) et (iii) :
$$Ri=E_C-E_A=(E_{C,\mathrm{eq}}-E_{A,\mathrm{eq}})+(\alpha_C-\alpha_A)i=e-(\alpha_A+|\alpha_C|)\,i.$$
D'où
$$i=\frac e{R+\alpha_A+|\alpha_C|},\qquad U=Ri=\frac{Re}{R+\alpha_A+|\alpha_C|}.$$

**5. Interprétation.** La pile se comporte comme un générateur de Thévenin de f.é.m. $e$ et de **résistance interne** $r=\alpha_A+|\alpha_C|$, due aux surtensions (à laquelle s'ajouterait la résistance de l'électrolyte). Plus les couples sont rapides, plus $r$ est faible et plus la pile peut débiter.
"""

D['c-cin-2'] = r"""
**1. Lien entre volume de $\mathrm{O_2}$ et avancement.** Soit $n_0$ la quantité initiale de $\mathrm{N_2O_5}$ et $x(t)$ l'avancement. D'après $\mathrm{N_2O_5}\to\mathrm{N_2O_4}+\frac12\mathrm{O_2}$ :
$$n_{\mathrm{N_2O_5}}(t)=n_0-x(t),\qquad n_{\mathrm{O_2}}(t)=\frac{x(t)}2.$$
Le dioxygène recueilli (gaz parfait, à $V_m$ fixé) occupe $V(t)=\frac{x(t)}2V_m$. La réaction étant totale, $x_\infty=n_0$ et $V_\infty=\frac{n_0}2V_m$. Donc
$$\frac{V(t)}{V_\infty}=\frac{x(t)}{n_0}=1-\frac{[\mathrm{N_2O_5}](t)}{[\mathrm{N_2O_5}]_0}.$$

**2. Loi cinétique d'ordre 1.** $v=-\frac{\mathrm d[\mathrm{N_2O_5}]}{\mathrm dt}=k[\mathrm{N_2O_5}]$. En séparant les variables puis en intégrant de $0$ à $t$ :
$$\int_{[\mathrm{N_2O_5}]_0}^{[\mathrm{N_2O_5}]}\frac{\mathrm dc}c=-k\int_0^t\mathrm dt'\iff\ln\frac{[\mathrm{N_2O_5}]}{[\mathrm{N_2O_5}]_0}=-kt\iff[\mathrm{N_2O_5}]=[\mathrm{N_2O_5}]_0\,e^{-kt}.$$

**3. Loi $V(t)$.** En combinant 1 et 2 :
$$V(t)=V_\infty\big(1-e^{-kt}\big)\iff e^{-kt}=\frac{V_\infty-V(t)}{V_\infty}.$$

**4. Calcul de $k$.** À $t=40$ min, $V=19$ mL, et $V_\infty=35$ mL :
$$e^{-40k}=\frac{35-19}{35}=\frac{16}{35}\iff k=\frac1{40}\ln\frac{35}{16}=\frac{\ln2{,}1875}{40}=\frac{0{,}7828}{40}\approx1{,}96\times10^{-2}\ \mathrm{min^{-1}}.$$
En $\mathrm s^{-1}$ : $k=\frac{1{,}96\times10^{-2}}{60}\approx3{,}3\times10^{-4}\ \mathrm{s^{-1}}$.

**5. Temps de demi-réaction.** À $t_{1/2}$, $[\mathrm{N_2O_5}]=\frac{[\mathrm{N_2O_5}]_0}2$, soit $e^{-kt_{1/2}}=\frac12$ :
$$t_{1/2}=\frac{\ln2}k=\frac{0{,}693}{1{,}96\times10^{-2}}\approx35\ \mathrm{min}.$$
Pour un ordre 1, $t_{1/2}$ ne dépend pas de la concentration initiale. Contrôle : à $t=t_{1/2}\approx35$ min, on attend $V=\frac{V_\infty}2=17{,}5$ mL, et à 40 min on mesure 19 mL : c'est cohérent.

**6. Rôle de $V_m$.** Il n'est pas nécessaire pour $k$, qui ne fait intervenir que le rapport $V/V_\infty$. Il permet en revanche de calculer la quantité initiale :
$$n_0=\frac{2V_\infty}{V_m}=\frac{2\times35\times10^{-3}}{24{,}5}\approx2{,}9\times10^{-3}\ \mathrm{mol}.$$
"""

D['c-cristallo-1'] = r"""
**1. Rayon atomique de $\mathrm{Ti}_\alpha$.** Dans un plan compact (base hexagonale), chaque atome est tangent à ses 6 voisins, distants de $a$. Donc $2r=a$, soit
$$r_\alpha=\frac a2=\frac{295}2=147{,}5\ \mathrm{pm}.$$

**1. Paramètre $c$ idéal.** Un atome du plan intermédiaire (B) repose sur un triangle équilatéral de 3 atomes du plan A : ces 4 atomes forment un tétraèdre régulier d'arête $a$, de hauteur $h=a\sqrt{\frac23}$. La maille contient deux demi-hauteurs de tétraèdre (A, puis B, puis A), donc
$$c=2h=2a\sqrt{\tfrac23}=a\sqrt{\tfrac83}\approx1{,}633\,a=1{,}633\times295\approx482\ \mathrm{pm}.$$

**1. Contrôle par la masse volumique.** La maille hexagonale (prisme à base losange d'angle $120^\circ$) a pour volume $V=a^2\sin120^\circ\cdot c=\frac{\sqrt3}2a^2c$ et contient $8\times\frac18+1=2$ atomes. Donc $\rho=\frac{2M}{\mathcal N_A\frac{\sqrt3}2a^2c}$, d'où
$$c=\frac{2M}{\mathcal N_A\,\rho\,\frac{\sqrt3}2a^2}=\frac{2\times47{,}88\times10^{-3}}{6{,}022\times10^{23}\times4503\times0{,}866\times(295\times10^{-12})^2}=\frac{9{,}58\times10^{-2}}{2{,}04\times10^{8}}\approx4{,}69\times10^{-10}\ \mathrm m.$$
On trouve $c\approx469$ pm, soit $c/a\approx1{,}59$, un peu inférieur à la valeur idéale $1{,}633$ : le titane réel est un hexagonal légèrement « écrasé ».

**2.(a) Compacité du cubique centré.**
- **Population** : 8 sommets comptant chacun pour $\frac18$, plus 1 atome central, soit $Z=2$.
- **Tangence** : les atomes se touchent le long de la grande diagonale du cube (sommet, centre, sommet opposé), de longueur $a\sqrt3=4r$, donc $r=\frac{a\sqrt3}4$.
- **Compacité** :
$$\mathcal C=\frac{Z\cdot\frac43\pi r^3}{a^3}=\frac{2\cdot\frac43\pi\big(\frac{a\sqrt3}4\big)^3}{a^3}=\frac83\pi\cdot\frac{3\sqrt3}{64}=\frac{\pi\sqrt3}8\approx0{,}68.$$

**2.(b) Rayon de $\mathrm{Ti}_\beta$.**
$$r_\beta=\frac{a\sqrt3}4=\frac{332\times1{,}732}4\approx144\ \mathrm{pm}.$$
Il est légèrement inférieur à $r_\alpha$ : le rayon métallique dépend un peu de la coordinence (8 en c.c. contre 12 en h.c.).

**2.(b) Masse volumique de $\mathrm{Ti}_\beta$.** $a^3=(332\times10^{-12})^3=3{,}66\times10^{-29}\ \mathrm{m^3}$, donc
$$\rho_\beta=\frac{2M}{\mathcal N_Aa^3}=\frac{2\times47{,}88\times10^{-3}}{6{,}022\times10^{23}\times3{,}66\times10^{-29}}=\frac{9{,}58\times10^{-2}}{2{,}20\times10^{-5}}\approx4{,}35\times10^3\ \mathrm{kg\,m^{-3}}.$$
Elle est plus faible que celle de $\mathrm{Ti}_\alpha$ ($4503\ \mathrm{kg\,m^{-3}}$), conformément à une compacité plus faible ($0{,}68<0{,}74$).
"""

D['c-cristallo-2'] = r"""
**1. Sites octaédriques (O).** Ils sont situés au centre du cube et aux milieux des 12 arêtes. Chaque site d'arête est partagé entre 4 mailles. Nombre par maille : $1+12\times\frac14=4$. Chacun est entouré de 6 atomes Zr formant un octaèdre régulier.

**1. Sites tétraédriques (T).** Ils sont situés aux centres des 8 petits cubes d'arête $\frac a2$ (aux points $(\frac14,\frac14,\frac14)$ et équivalents), entièrement inclus dans la maille : 8 par maille. Chacun est entouré de 4 atomes Zr formant un tétraèdre régulier.

**1. Bilan.** Pour 4 Zr par maille ($8\times\frac18+6\times\frac12=4$), on compte 4 sites O (1 par Zr) et 8 sites T (2 par Zr).

**2. Paramètre de maille.** Dans le c.f.c., les atomes sont tangents le long de la diagonale d'une face, de longueur $a\sqrt2=4R$. Donc $a=2\sqrt2R=2\times1{,}414\times160\approx453$ pm.

**2. Rayon du site octaédrique.** Le long d'une arête, entre deux sommets, se trouve un site O au milieu. La distance centre du site–centre de Zr vaut $\frac a2$. Le site est tangent aux Zr si $r_O+R=\frac a2$ :
$$r_O=\frac a2-R=\sqrt2R-R=(\sqrt2-1)R\approx0{,}414\times160\approx66\ \mathrm{pm}.$$

**2. Rayon du site tétraédrique.** Le site au centre d'un petit cube d'arête $\frac a2$ est à la distance d'une demi-diagonale de ce petit cube du sommet occupé : $\frac12\cdot\frac a2\sqrt3=\frac{a\sqrt3}4$. Donc
$$r_T=\frac{a\sqrt3}4-R=\frac{2\sqrt2R\sqrt3}4-R=\Big(\sqrt{\tfrac32}-1\Big)R\approx0{,}225\times160\approx36\ \mathrm{pm}.$$

**3. Compatibilité avec l'hydrogène.** $r_{\mathrm H}=0{,}037$ nm $=37$ pm.
- Site O : $r_{\mathrm H}=37<66$ pm, l'hydrogène s'y loge sans déformer le réseau.
- Site T : $r_{\mathrm H}=37>36$ pm, l'hydrogène est très légèrement trop gros et doit écarter un peu les atomes de Zr.

Le critère géométrique simple désigne donc les **sites octaédriques**.

**4. Occupation réelle.** En fait, H occupe tous les **sites tétraédriques** (l'autre type), avec une légère dilatation de la maille. Les liaisons Zr–H, en partie covalentes, rendent le modèle de sphères dures insuffisant.

**4. Maille et formule.** Zr occupe les sommets et centres des faces ; H occupe les 8 centres des petits cubes d'arête $\frac a2$ (structure de type fluorine $\mathrm{CaF_2}$). Par maille : 4 Zr et 8 H, d'où la formule
$$\mathrm{ZrH_2}.$$
Chaque H est entouré de 4 Zr (tétraèdre), et chaque Zr de 8 H (cube).

**5. Application énergétique.** Le **stockage de l'hydrogène** : les hydrures métalliques absorbent $\mathrm{H_2}$ de façon réversible (il est libéré par chauffage ou baisse de pression), à une densité volumique d'hydrogène supérieure à celle du gaz comprimé et en toute sécurité. Applications : alimentation des piles à combustible et véhicules à hydrogène. (Les hydrures de zirconium servent aussi de modérateur de neutrons dans certains réacteurs nucléaires.)
"""
