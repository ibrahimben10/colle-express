D = {}

D['n-c-vitinit'] = r"""
**1. Principe.** À l'instant initial, les concentrations sont connues ($[\mathrm{NO}]_0$, $[\mathrm{O_2}]_0$), et $v_0=k[\mathrm{NO}]_0^\alpha[\mathrm{O_2}]_0^\beta$. En comparant deux expériences où une seule concentration change, on isole un ordre partiel.

**1. Ordre $\alpha$.** Entre les expériences 1 et 2, $[\mathrm O_2]_0$ est fixée et $[\mathrm{NO}]_0$ double :
$$\frac{v_{0,2}}{v_{0,1}}=\Big(\frac{0{,}020}{0{,}010}\Big)^\alpha=2^\alpha=\frac{1{,}0\times10^{-4}}{2{,}5\times10^{-5}}=4\quad\Longrightarrow\quad\alpha=2.$$

**1. Ordre $\beta$.** Entre les expériences 1 et 3, $[\mathrm{NO}]_0$ est fixée et $[\mathrm O_2]_0$ double :
$$2^\beta=\frac{5{,}0\times10^{-5}}{2{,}5\times10^{-5}}=2\quad\Longrightarrow\quad\beta=1.$$
L'ordre global vaut $\alpha+\beta=3$.

**1. Constante de vitesse.** Avec l'expérience 1 :
$$k=\frac{v_0}{[\mathrm{NO}]_0^2[\mathrm O_2]_0}=\frac{2{,}5\times10^{-5}}{(0{,}010)^2\times0{,}010}=\frac{2{,}5\times10^{-5}}{1{,}0\times10^{-6}}=25.$$
Unité : $\frac{\mathrm{mol\,L^{-1}\,s^{-1}}}{(\mathrm{mol\,L^{-1}})^3}=\mathrm{L^2\,mol^{-2}\,s^{-1}}$. Donc $k=25\ \mathrm{L^2\,mol^{-2}\,s^{-1}}$. On vérifie avec les expériences 2 et 3 : $25\times(0{,}02)^2\times0{,}01=1{,}0\times10^{-4}$ ✓ et $25\times(0{,}01)^2\times0{,}02=5{,}0\times10^{-5}$ ✓.

**2. Acte élémentaire ?** Pour un acte élémentaire, les ordres partiels sont égaux aux coefficients stœchiométriques (loi de Van't Hoff). C'est le cas ici ($\alpha=2$, $\beta=1$) : la loi est **compatible** avec un acte élémentaire trimoléculaire. Mais la rencontre simultanée de trois molécules est un événement très improbable.

**2. Mécanisme plausible.** On propose plutôt deux étapes :
- un pré-équilibre rapide : $2\,\mathrm{NO}\rightleftharpoons\mathrm{N_2O_2}$, de constante $K$, d'où $[\mathrm{N_2O_2}]=K[\mathrm{NO}]^2$ ;
- une étape lente : $\mathrm{N_2O_2}+\mathrm O_2\to2\,\mathrm{NO_2}$, de constante $k_2$.

L'étape lente impose la vitesse : $v=k_2[\mathrm{N_2O_2}][\mathrm O_2]=k_2K[\mathrm{NO}]^2[\mathrm O_2]$. C'est la même loi, avec $k=k_2K$.

**2. Conclusion.** Une loi de vitesse ne prouve pas un mécanisme : elle peut seulement en exclure certains. (Ce mécanisme explique aussi que $k$ diminue quand $T$ augmente pour cette réaction : le pré-équilibre exothermique se déplace vers la gauche.)

**3. Dégénérescence de l'ordre.** On travaille avec un large excès de NO : $[\mathrm{NO}]_0\gg[\mathrm O_2]_0$, par exemple 100 fois plus. Au cours de la réaction, $[\mathrm{NO}]\approx[\mathrm{NO}]_0$ reste quasi constante, et
$$v\approx k_{\mathrm{app}}[\mathrm O_2]^\beta,\qquad k_{\mathrm{app}}=k[\mathrm{NO}]_0^2.$$
On suit $[\mathrm O_2](t)$ (par la pression, ou par l'absorbance de $\mathrm{NO_2}$, qui est coloré) et on teste les lois intégrées : si $\ln[\mathrm O_2]$ est affine en $t$, alors $\beta=1$, et la pente donne $k_{\mathrm{app}}$.
"""

D['n-c-ethanoique'] = r"""
**1. Réaction de titrage.** L'acide le plus fort ($\mathrm{CH_3COOH}$) réagit avec la base la plus forte ($\mathrm{HO^-}$) :
$$\mathrm{CH_3COOH+HO^-\to CH_3COO^-+H_2O}.$$

**1. Constante.** On écrit $K=\frac{[\mathrm{CH_3COO^-}]}{[\mathrm{CH_3COOH}][\mathrm{HO^-}]}$, puis on multiplie numérateur et dénominateur par $[\mathrm{H_3O^+}]$ :
$$K=\frac{K_a}{K_e}=10^{-4{,}76+14{,}0}=10^{9{,}24}\gg1.$$
La réaction est quasi totale et rapide : elle convient pour un titrage.

**2. pH initial.** L'acide éthanoïque est faible ; on suppose qu'il se dissocie peu ($[\mathrm{CH_3COOH}]\approx c_a$) et que l'autoprotolyse de l'eau est négligeable ($[\mathrm{CH_3COO^-}]\approx[\mathrm{H_3O^+}]=h$). La constante d'acidité donne
$$K_a=\frac{h^2}{c_a}\iff h=\sqrt{K_ac_a}\iff\mathrm{pH}=\frac12(\mathrm pK_a-\log c_a)=\frac12(4{,}76+1{,}00)=2{,}88.$$

**2. Vérifications.**
- $h=10^{-2{,}88}=1{,}3\times10^{-3}$ et $\frac h{c_a}=1{,}3\,\%\ll1$ : l'acide est bien peu dissocié. On peut aussi dire que $\mathrm{pH}<\mathrm pK_a-1$.
- $\mathrm{pH}<6{,}5$ : $[\mathrm{HO^-}]\ll h$, et l'autoprotolyse est négligeable.

**3. Volume équivalent.** À l'équivalence, les réactifs ont été introduits dans les proportions stœchiométriques : $c_aV_a=c_bV_{eq}$, donc
$$V_{eq}=\frac{c_aV_a}{c_b}=\frac{0{,}100\times20{,}0}{0{,}100}=20{,}0\ \mathrm{mL}.$$

**3. Demi-équivalence.** Pour $V_b=\frac{V_{eq}}2$, la moitié de l'acide a été transformée en base conjuguée : $[\mathrm{CH_3COOH}]=[\mathrm{CH_3COO^-}]$. La relation $\mathrm{pH}=\mathrm pK_a+\log\frac{[\mathrm{CH_3COO^-}]}{[\mathrm{CH_3COOH}]}$ donne
$$\mathrm{pH}=\mathrm pK_a=4{,}76.$$
C'est une méthode classique de détermination d'un $\mathrm pK_a$.

**4. Composition à l'équivalence.** Toute la quantité d'acide est devenue $\mathrm{CH_3COO^-}$, dans le volume $V_a+V_{eq}=40{,}0$ mL :
$$c=\frac{c_aV_a}{V_a+V_{eq}}=\frac{2{,}00\times10^{-3}}{40{,}0\times10^{-3}}=0{,}050\ \mathrm{mol\,L^{-1}}.$$
C'est une solution de base faible, avec $\mathrm pK_b=\mathrm pK_e-\mathrm pK_a=9{,}24$.

**4. pH à l'équivalence.** Par le même raisonnement qu'en 2 (base peu protonée) :
$$\mathrm{pOH}=\frac12(\mathrm pK_b-\log c)=\frac12(9{,}24+1{,}30)=5{,}27,\qquad\mathrm{pH}=14{,}0-5{,}27\approx8{,}73.$$
Vérification : $\mathrm{pH}>\mathrm pK_a+1$, donc la base est bien très majoritaire. ✓

**4. Choix de l'indicateur.** Le pH à l'équivalence est basique, à cause de la base conjuguée. L'indicateur doit virer dans le saut de pH, autour de 8,7 : c'est la **phénolphtaléine** (zone 8,2–10,0), qui passe d'incolore à rose. L'hélianthine virerait bien trop tôt (pH de 3,1 à 4,4, avant même la demi-équivalence), et le BBT virerait légèrement avant l'équivalence.
"""

D['n-c-tampon'] = r"""
**1. pH initial.** La solution contient le couple $\mathrm{CH_3COOH/CH_3COO^-}$ en quantités égales (0,10 mol de chaque dans 1,0 L). Les réactions de l'acide et de la base avec l'eau modifient très peu ces concentrations, car l'acide faible est en présence de sa base conjuguée. La relation d'Henderson donne
$$\mathrm{pH}=\mathrm pK_a+\log\frac{[\mathrm{CH_3COO^-}]}{[\mathrm{CH_3COOH}]}=4{,}76+\log1=4{,}76.$$

**2. Réaction de l'acide fort.** $\mathrm{H_3O^+}$ (acide fort) réagit sur la base la plus forte présente :
$$\mathrm{CH_3COO^-}+\mathrm{H_3O^+}\to\mathrm{CH_3COOH}+\mathrm{H_2O},\qquad K=\frac1{K_a}=10^{4{,}76}.$$
La réaction est quasi totale. $\mathrm{H_3O^+}$ ($0{,}010$ mol) est en défaut et entièrement consommé.

**2. Bilan de matière.**

| | $\mathrm{CH_3COO^-}$ | $\mathrm{H_3O^+}$ | $\mathrm{CH_3COOH}$ |
|---|---|---|---|
| avant | 0,10 | 0,010 | 0,10 |
| après | 0,090 | $\approx0$ | 0,110 |

**2. Nouveau pH.**
$$\mathrm{pH}=4{,}76+\log\frac{0{,}090}{0{,}110}=4{,}76-0{,}087\approx4{,}67.$$
Le pH n'a diminué que de 0,09 unité.

**3. Dans l'eau pure.** $0{,}010$ mol d'acide fort dans 1,0 L donne $[\mathrm{H_3O^+}]=0{,}010\ \mathrm{mol\,L^{-1}}$, soit $\mathrm{pH}=2{,}0$. Le pH passe de 7,0 à 2,0 : une chute de 5 unités.

**3. Rôle d'une solution tampon.** Le mélange d'un acide faible et de sa base conjuguée, en concentrations voisines et notables, **modère fortement les variations de pH** lors d'ajouts modérés d'acide ou de base, ainsi que lors d'une dilution (le rapport des concentrations ne change pas). La base du couple « absorbe » les $\mathrm{H_3O^+}$ ajoutés, et l'acide les $\mathrm{HO^-}$. Le pouvoir tampon est maximal quand $\mathrm{pH}=\mathrm pK_a$ (mélange équimolaire), et d'autant plus grand que les concentrations sont élevées. Applications : le sang est tamponné à pH 7,4 par le couple $\mathrm{CO_2/HCO_3^-}$ ; les solutions d'étalonnage des pH-mètres sont des tampons.
"""

D['n-c-agcl'] = r"""
**1. Équilibre de dissolution.** $\mathrm{AgCl_{(s)}}=\mathrm{Ag^+}+\mathrm{Cl^-}$, de constante $K_s=[\mathrm{Ag^+}][\mathrm{Cl^-}]=10^{-9{,}75}\approx1{,}8\times10^{-10}$ (à saturation, en présence du solide).

**1. Solubilité dans l'eau pure.** Dissoudre $s$ mol/L de solide libère $s$ mol/L de chaque ion : $[\mathrm{Ag^+}]=[\mathrm{Cl^-}]=s$. Donc $K_s=s^2$ et
$$s=\sqrt{K_s}=10^{-4{,}875}\approx1{,}3\times10^{-5}\ \mathrm{mol\,L^{-1}}.$$

**1. Solubilité massique.** $s_m=sM=1{,}33\times10^{-5}\times143{,}3\approx1{,}9\times10^{-3}\ \mathrm{g\,L^{-1}}=1{,}9\ \mathrm{mg\,L^{-1}}$. Le chlorure d'argent est très peu soluble (précipité blanc caractéristique des ions chlorure).

**2. Solution de NaCl.** Les ions $\mathrm{Cl^-}$ sont déjà présents à $0{,}10\ \mathrm{mol\,L^{-1}}$. Si $s'$ est la nouvelle solubilité, $[\mathrm{Ag^+}]=s'$ et $[\mathrm{Cl^-}]=0{,}10+s'\approx0{,}10$ (en supposant $s'\ll0{,}10$). Donc
$$s'=\frac{K_s}{0{,}10}=\frac{1{,}8\times10^{-10}}{0{,}10}=1{,}8\times10^{-9}\ \mathrm{mol\,L^{-1}}.$$
L'hypothèse est largement vérifiée.

**2. Effet observé.** La solubilité est divisée par environ $7\times10^3$ : c'est l'**effet d'ion commun**. L'ion $\mathrm{Cl^-}$, déjà présent, déplace l'équilibre de dissolution vers la gauche (loi de modération). On l'utilise pour précipiter quantitativement les ions $\mathrm{Ag^+}$ avec un excès de chlorure.

**3. Concentrations après mélange.** Le volume double (10 + 10 mL) : chaque concentration est divisée par 2. On a donc $[\mathrm{Ag^+}]_0=[\mathrm{Cl^-}]_0=5{,}0\times10^{-5}\ \mathrm{mol\,L^{-1}}$.

**3. Critère de précipitation.** On compare le quotient de réaction $Q=[\mathrm{Ag^+}]_0[\mathrm{Cl^-}]_0$ à $K_s$.
- Cas 1 : $Q=(5{,}0\times10^{-5})^2=2{,}5\times10^{-9}>K_s=1{,}8\times10^{-10}$ : la solution est sursaturée, et il se forme un **précipité**.
- Cas 2 (solutions dix fois plus diluées) : $Q=(5{,}0\times10^{-6})^2=2{,}5\times10^{-11}<K_s$. Le solide ne peut pas exister : il n'y a **pas de précipité**, et la solution reste limpide.

L'existence d'un précipité n'est pas acquise d'avance : elle dépend des concentrations.
"""

D['n-c-mgoh2'] = r"""
**1. Équilibre de dissolution.** $\mathrm{Mg(OH)_{2(s)}}=\mathrm{Mg^{2+}}+2\,\mathrm{HO^-}$, de constante $K_s=[\mathrm{Mg^{2+}}][\mathrm{HO^-}]^2=10^{-11{,}2}=6{,}3\times10^{-12}$.

**1. Solubilité dans l'eau pure.** Dissoudre $s$ mol/L donne $[\mathrm{Mg^{2+}}]=s$ et $[\mathrm{HO^-}]=2s$, en négligeant les $\mathrm{HO^-}$ de l'autoprotolyse. Donc $K_s=s(2s)^2=4s^3$ et
$$s=\Big(\frac{K_s}4\Big)^{1/3}=\Big(\frac{6{,}3\times10^{-12}}4\Big)^{1/3}=(1{,}6\times10^{-12})^{1/3}\approx1{,}2\times10^{-4}\ \mathrm{mol\,L^{-1}}.$$

**1. pH de la solution saturée.** $[\mathrm{HO^-}]=2s\approx2{,}3\times10^{-4}\ \mathrm{mol\,L^{-1}}$, donc $\mathrm{pOH}=3{,}6$ et $\mathrm{pH}=14{,}0-3{,}6\approx10{,}4$. On a bien $[\mathrm{HO^-}]\gg10^{-7}$, ce qui justifie l'approximation.

**2. Début de précipitation.** Tant que $Q=[\mathrm{Mg^{2+}}][\mathrm{HO^-}]^2<K_s$, il n'y a pas de solide. Le précipité apparaît quand $Q=K_s$, avec $[\mathrm{Mg^{2+}}]=1{,}0\times10^{-2}$ (encore inchangée) :
$$[\mathrm{HO^-}]=\sqrt{\frac{K_s}{[\mathrm{Mg^{2+}}]}}=\sqrt{\frac{10^{-11{,}2}}{10^{-2}}}=10^{-4{,}6}\ \mathrm{mol\,L^{-1}},$$
soit $\mathrm{pOH}=4{,}6$ et $\mathrm{pH}=9{,}4$. En dessous de pH 9,4, les ions $\mathrm{Mg^{2+}}$ restent en solution.

**3. Solubilité en fonction du pH.** En présence du solide, l'équilibre est réalisé : $s=[\mathrm{Mg^{2+}}]=\frac{K_s}{[\mathrm{HO^-}]^2}$. Avec $[\mathrm{HO^-}]=\frac{K_e}{[\mathrm{H_3O^+}]}$, on a $\log[\mathrm{HO^-}]=\mathrm{pH}-\mathrm pK_e$, d'où
$$\log s=\log K_s-2\log[\mathrm{HO^-}]=-\mathrm pK_s-2(\mathrm{pH}-\mathrm pK_e)=2\mathrm pK_e-\mathrm pK_s-2\,\mathrm{pH}=16{,}8-2\,\mathrm{pH}.$$

**3. Allure.** C'est une droite de pente $-2$ dans le plan $(\mathrm{pH},\log s)$. Par exemple, $s=1$ mol/L à pH 8,4, et $s=10^{-4{,}6}$ mol/L à pH 10,7. En milieu acide, la solubilité devient très grande : le solide se dissout entièrement (la droite n'a de sens que tant que le solide existe). En milieu basique, elle devient très faible.

**4. Lait de magnésie.** L'estomac contient un acide fort (HCl, pH de l'ordre de 1 à 2). À ce pH, la solubilité de $\mathrm{Mg(OH)_2}$ est énorme. La réaction
$$\mathrm{Mg(OH)_{2(s)}}+2\,\mathrm{H_3O^+}\to\mathrm{Mg^{2+}}+4\,\mathrm{H_2O},\qquad K=\frac{K_s}{K_e^2}=10^{-11{,}2+28}=10^{16{,}8},$$
est totale : le solide neutralise l'excès d'acide (brûlures d'estomac). Avantage : étant peu soluble, il ne rend pas le milieu fortement basique (pH limité vers 10 dans la suspension) et n'agit qu'au contact de l'acide. C'est un antiacide doux, contrairement à une base forte soluble comme la soude.
"""

D['n-c-nacl'] = r"""
**1. Ions chlorure.** Ils occupent les nœuds du réseau CFC : 8 sommets, chacun partagé entre 8 mailles, et 6 centres de faces, chacun partagé entre 2 mailles.
$$N(\mathrm{Cl^-})=8\times\frac18+6\times\frac12=4.$$

**1. Ions sodium.** Ils occupent tous les sites octaédriques : le centre du cube (1, propre à la maille) et les milieux des 12 arêtes (chacun partagé entre 4 mailles).
$$N(\mathrm{Na^+})=1+12\times\frac14=4.$$

**1. Électroneutralité.** 4 $\mathrm{Na^+}$ et 4 $\mathrm{Cl^-}$ par maille : la charge totale est nulle, et la maille contient **4 motifs NaCl**.

**2. Coordinence de $\mathrm{Na^+}$.** Un ion au centre du cube a pour plus proches voisins les 6 $\mathrm{Cl^-}$ des centres des faces, à la distance $\frac a2$, formant un octaèdre régulier : coordinence $\mathrm{Na^+/Cl^-}=6$.

**2. Coordinence de $\mathrm{Cl^-}$.** Les deux sous-réseaux sont des CFC identiques, décalés de $\frac a2$ le long d'une arête. Les rôles sont symétriques : chaque $\mathrm{Cl^-}$ est entouré de 6 $\mathrm{Na^+}$. C'est une structure de coordinence [6,6].

**3. Masse volumique.** La maille contient 4 motifs, de masse $\frac{4M}{N_A}$, dans un volume $a^3$ :
$$\rho=\frac{4M}{N_Aa^3}=\frac{4\times58{,}4\times10^{-3}}{6{,}02\times10^{23}\times(564\times10^{-12})^3}=\frac{0{,}234}{6{,}02\times10^{23}\times1{,}79\times10^{-28}}\approx2{,}16\times10^3\ \mathrm{kg\,m^{-3}}.$$
Valeur tabulée : 2,16 g/cm³. ✓

**4. Rayon de $\mathrm{Na^+}$.** Le long d'une arête se succèdent $\mathrm{Cl^-}$ (sommet), $\mathrm{Na^+}$ (milieu) et $\mathrm{Cl^-}$ (sommet). Le contact cation-anion donne $r_++r_-=\frac a2$, donc
$$r_+=\frac a2-r_-=282-181=101\ \mathrm{pm}.$$

**4. Non-contact des anions.** Les $\mathrm{Cl^-}$ les plus proches sont un sommet et un centre de face voisin, à la distance d'une demi-diagonale de face : $\frac{a\sqrt2}2=\frac{564\times1{,}414}2=399$ pm. Comme $399>2r_-=362$ pm, les anions ne se touchent pas. Leur répulsion mutuelle est évitée, et ce sont les contacts cation-anion, attractifs, qui assurent la cohésion.

**4. Rapport des rayons.** $\frac{r_+}{r_-}=\frac{101}{181}=0{,}56$.
- **Limite inférieure** : les anions se touchent si $\frac{a\sqrt2}2=2r_-$, avec $a=2(r_++r_-)$, c'est-à-dire si $\frac{r_+}{r_-}=\sqrt2-1=0{,}414$. En dessous, le cation « flotte » dans le site octaédrique, et la structure est instable.
- **Limite supérieure** : au-delà de $\sqrt3-1=0{,}732$, un cation plus gros peut s'entourer de 8 anions (structure de type CsCl, coordinence [8,8]), plus favorable.

On a $0{,}414<0{,}56<0{,}732$ : la structure NaCl est cohérente.

**5. Compacité.** C'est le volume occupé par les ions sur le volume de la maille :
$$C=\frac{4\times\frac43\pi\big(r_+^3+r_-^3\big)}{a^3}=\frac{16{,}76\times\big(1{,}03\times10^6+5{,}93\times10^6\big)}{(564)^3}=\frac{1{,}17\times10^8}{1{,}79\times10^8}\approx0{,}65$$
(rayons en pm). C'est moins que 0,74 (empilement compact de sphères égales), car les ions ont des tailles différentes et les anions ne sont pas en contact.
"""
