D = {}

D['n-c-daniell'] = r"""
**1. Potentiel de l'électrode de cuivre.** Couple $\mathrm{Cu^{2+}}+2e^-=\mathrm{Cu}$, avec $n=2$ électrons ; le cuivre solide a une activité égale à 1. Formule de Nernst :
$$E_{\mathrm{Cu}}=E^\circ(\mathrm{Cu^{2+}/Cu})+\frac{0{,}06}2\log[\mathrm{Cu^{2+}}]=0{,}34+0{,}03\log0{,}10=0{,}34-0{,}03=0{,}31\ \mathrm V.$$

**1. Potentiel de l'électrode de zinc.**
$$E_{\mathrm{Zn}}=E^\circ(\mathrm{Zn^{2+}/Zn})+0{,}03\log[\mathrm{Zn^{2+}}]=-0{,}76+0{,}03\log1{,}0=-0{,}76\ \mathrm V.$$

**1. Polarité.** L'électrode de plus haut potentiel est le pôle $+$ : c'est le cuivre. Le courant sort par le pôle $+$ dans le circuit extérieur, et les électrons arrivent à l'électrode de cuivre, où ils sont consommés.
- **Cathode** (réduction, pôle $+$) : $\mathrm{Cu^{2+}}+2e^-\to\mathrm{Cu}$.
- **Anode** (oxydation, pôle $-$) : $\mathrm{Zn}\to\mathrm{Zn^{2+}}+2e^-$.

**1. Réaction de fonctionnement.** En sommant les demi-équations :
$$\mathrm{Zn}+\mathrm{Cu^{2+}}\to\mathrm{Zn^{2+}}+\mathrm{Cu}.$$

**2. Force électromotrice.** À courant nul :
$$e=E_+-E_-=0{,}31-(-0{,}76)=1{,}07\ \mathrm V.$$

**2. Constante d'équilibre.** À l'équilibre, la pile est « usée » : $e=0$, donc les deux potentiels sont égaux :
$$0{,}34+0{,}03\log[\mathrm{Cu^{2+}}]_{eq}=-0{,}76+0{,}03\log[\mathrm{Zn^{2+}}]_{eq}\iff\log\frac{[\mathrm{Zn^{2+}}]_{eq}}{[\mathrm{Cu^{2+}}]_{eq}}=\frac{0{,}34+0{,}76}{0{,}03}.$$
$$\log K=\frac{2\times(0{,}34-(-0{,}76))}{0{,}06}=\frac{2{,}20}{0{,}06}\approx37,\qquad K\approx10^{37}.$$
La réaction est quasi totale : la pile fonctionne jusqu'à l'épuisement d'un réactif.

**3. Pont salin.** Il contient un électrolyte inerte (par exemple $\mathrm{K^+,NO_3^-}$) gélifié. Il ferme le circuit : à l'intérieur de la pile, le courant est assuré par la migration des ions. Il maintient aussi l'électroneutralité de chaque compartiment. Sans lui, le compartiment du zinc s'enrichirait en charges positives ($\mathrm{Zn^{2+}}$ produits) et celui du cuivre en charges négatives ($\mathrm{SO_4^{2-}}$ dont le $\mathrm{Cu^{2+}}$ est consommé), ce qui bloquerait la réaction. Enfin, il évite le mélange des solutions : $\mathrm{Cu^{2+}}$ réagirait directement sur le zinc, sans courant utile.

**4. Quantité de zinc.** $n(\mathrm{Zn})=\frac{10}{65{,}4}=0{,}153$ mol. C'est le réactif limitant, puisque le cuivre(II) est en excès.

**4. Charge maximale.** Chaque atome de zinc oxydé libère 2 électrons, soit $2F$ coulombs par mole :
$$Q_{\max}=2n(\mathrm{Zn})F=2\times0{,}153\times96\,500\approx2{,}95\times10^4\ \mathrm C.$$
Avec $1\ \mathrm{A\,h}=3600$ C :
$$Q_{\max}=\frac{2{,}95\times10^4}{3600}\approx8{,}2\ \mathrm{A\,h}.$$
La pile peut par exemple débiter 100 mA pendant 82 h.
"""

D['n-c-permanganate'] = r"""
**1. Demi-équations.**
- Réduction du permanganate (en milieu acide) : on équilibre Mn, puis O avec $\mathrm{H_2O}$, puis H avec $\mathrm{H^+}$, puis les charges avec $e^-$ :
$$\mathrm{MnO_4^-}+8\,\mathrm{H^+}+5\,e^-\to\mathrm{Mn^{2+}}+4\,\mathrm{H_2O}.$$
- Oxydation du fer(II) : $\mathrm{Fe^{2+}}\to\mathrm{Fe^{3+}}+e^-$.

**1. Équation de dosage.** On multiplie la seconde par 5 pour égaliser les électrons échangés, puis on additionne :
$$\mathrm{MnO_4^-}+5\,\mathrm{Fe^{2+}}+8\,\mathrm{H^+}\to\mathrm{Mn^{2+}}+5\,\mathrm{Fe^{3+}}+4\,\mathrm{H_2O}.$$

**1. Constante d'équilibre.** Pour une réaction échangeant $n=5$ électrons :
$$\log K=\frac{n\big(E^\circ_{\mathrm{ox}}-E^\circ_{\mathrm{red}}\big)}{0{,}06}=\frac{5\times(1{,}51-0{,}77)}{0{,}06}=\frac{3{,}70}{0{,}06}\approx62,\qquad K\approx10^{62}.$$
La réaction est quasi totale, et rapide en milieu acide : elle convient pour un dosage. L'acide sulfurique fournit les $\mathrm{H^+}$ nécessaires. On n'utilise pas HCl, car $\mathrm{Cl^-}$ serait oxydé par $\mathrm{MnO_4^-}$.

**2. Repérage de l'équivalence.** Les ions $\mathrm{MnO_4^-}$ sont violets ; les ions $\mathrm{Mn^{2+}}$, $\mathrm{Fe^{2+}}$ et $\mathrm{Fe^{3+}}$ dilués sont presque incolores (légèrement jaunes pour $\mathrm{Fe^{3+}}$).
- Avant l'équivalence, chaque goutte de permanganate versée est immédiatement réduite par $\mathrm{Fe^{2+}}$, et la solution ne se colore pas.
- À l'équivalence, $\mathrm{Fe^{2+}}$ est épuisé : la première goutte en excès donne une teinte rose-violette persistante.

Le permanganate est son propre indicateur de fin de réaction.

**3. Concentration en fer(II).** À l'équivalence, les réactifs ont été introduits dans les proportions stœchiométriques : $\frac{n(\mathrm{Fe^{2+}})}5=n(\mathrm{MnO_4^-})_{\text{versé}}$. Donc
$$n(\mathrm{Fe^{2+}})=5cV_e=5\times2{,}00\times10^{-2}\times12{,}5\times10^{-3}=1{,}25\times10^{-3}\ \mathrm{mol},$$
$$[\mathrm{Fe^{2+}}]=\frac{n(\mathrm{Fe^{2+}})}{V_0}=\frac{1{,}25\times10^{-3}}{10{,}0\times10^{-3}}=0{,}125\ \mathrm{mol\,L^{-1}}.$$

**4. Potentiel à la demi-équivalence.** À $V=\frac{V_e}2$, la moitié de $\mathrm{Fe^{2+}}$ a été oxydée : $[\mathrm{Fe^{3+}}]=[\mathrm{Fe^{2+}}]$. Le permanganate versé a été entièrement consommé : sa concentration est infime, et le potentiel de la solution (commun à tous les couples, à l'équilibre) se calcule par le couple du fer :
$$E=E^\circ(\mathrm{Fe^{3+}/Fe^{2+}})+0{,}06\log\frac{[\mathrm{Fe^{3+}}]}{[\mathrm{Fe^{2+}}]}=0{,}77+0{,}06\log1=0{,}77\ \mathrm V.$$
Comme le pH à la demi-équivalence en titrage acido-basique, cette mesure donne directement le potentiel standard du couple titré.
"""

D['n-c-conducti'] = r"""
**1. Loi de Kohlrausch.** Pour une solution diluée, la conductivité est la somme des contributions des ions :
$$\sigma=\sum_i\lambda_ic_i,$$
avec $\lambda_i$ en $\mathrm{S\,m^2\,mol^{-1}}$, $c_i$ en $\mathrm{mol\,m^{-3}}$ et $\sigma$ en $\mathrm{S\,m^{-1}}$. (Pour des ions multichargés, on utilise des conductivités molaires adaptées.)

**1. Conductivité initiale.** HCl est un acide fort, totalement dissocié : $[\mathrm{H_3O^+}]=[\mathrm{Cl^-}]=1{,}0\times10^{-2}\ \mathrm{mol\,L^{-1}}=10\ \mathrm{mol\,m^{-3}}$ (attention à la conversion : $1\ \mathrm{mol\,L^{-1}}=10^3\ \mathrm{mol\,m^{-3}}$).
$$\sigma_0=10\times(35{,}0+7{,}6)\times10^{-3}=0{,}426\ \mathrm{S\,m^{-1}}.$$

**2. Réaction de titrage.** $\mathrm{H_3O^+}+\mathrm{HO^-}\to2\,\mathrm{H_2O}$, de constante $\frac1{K_e}=10^{14}$ : elle est totale. L'équivalence correspond à $n(\mathrm{HO^-})_{\text{versé}}=c_aV_a=1{,}0\times10^{-3}$ mol.

**2. Avant l'équivalence.** Chaque $\mathrm{HO^-}$ ajouté détruit un $\mathrm{H_3O^+}$, et l'ion $\mathrm{Na^+}$ qui l'accompagne reste en solution. Au total, on **remplace** un $\mathrm{H_3O^+}$ ($\lambda=35{,}0$) par un $\mathrm{Na^+}$ ($\lambda=5{,}0$). $[\mathrm{Cl^-}]$ ne change pas, car la dilution est négligeable. $\sigma$ **décroît** linéairement avec la quantité versée, avec une pente proportionnelle à $5{,}0-35{,}0=-30{,}0$.

**2. Après l'équivalence.** Il n'y a plus de $\mathrm{H_3O^+}$ : les ions $\mathrm{Na^+}$ et $\mathrm{HO^-}$ s'accumulent. $\sigma$ **croît** linéairement, avec une pente proportionnelle à $5{,}0+19{,}8=24{,}8$.

**2. Allure.** On obtient deux segments de droite (un « V » dissymétrique), et l'équivalence se lit au point anguleux, à l'intersection des deux droites. La méthode ne demande pas de mesure précise au voisinage de l'équivalence : on trace les droites à partir de points éloignés.

**3. À l'équivalence.** La solution ne contient que $\mathrm{Na^+}$ et $\mathrm{Cl^-}$, chacun à $10\ \mathrm{mol\,m^{-3}}$ ($\mathrm{H_3O^+}$ et $\mathrm{HO^-}$ sont à $10^{-7}$ mol/L, négligeables) :
$$\sigma_{eq}=10\times(5{,}0+7{,}6)\times10^{-3}=0{,}126\ \mathrm{S\,m^{-1}}.$$
C'est le minimum de la courbe.

**4. Mobilité exceptionnelle de $\mathrm{H_3O^+}$.** Les ions ordinaires migrent en se frayant un chemin entre les molécules d'eau. $\mathrm{H_3O^+}$ dispose d'un mécanisme supplémentaire : un proton passe de $\mathrm{H_3O^+}$ à une molécule d'eau voisine, liée par liaison hydrogène, qui devient $\mathrm{H_3O^+}$, et ainsi de suite (**mécanisme de Grotthuss**). La charge se propage par un relais de protons le long du réseau de liaisons hydrogène, sans déplacement global de matière, ce qui est beaucoup plus rapide. Le même mécanisme, par transfert d'un proton en sens inverse, explique la conductivité élevée de $\mathrm{HO^-}$ (19,8 contre 5 à 8 pour les ions ordinaires).
"""

D['n-c-epH'] = r"""
**1. Précipitation de $\mathrm{Fe(OH)_3}$.** Le solide apparaît quand $[\mathrm{Fe^{3+}}][\mathrm{HO^-}]^3=K_s$, avec $[\mathrm{Fe^{3+}}]=c=10^{-2}$ :
$$[\mathrm{HO^-}]^3=\frac{10^{-38}}{10^{-2}}=10^{-36}\iff[\mathrm{HO^-}]=10^{-12}\iff\mathrm{pH}=14-12=2{,}0.$$

**1. Précipitation de $\mathrm{Fe(OH)_2}$.**
$$[\mathrm{HO^-}]^2=\frac{10^{-15}}{10^{-2}}=10^{-13}\iff[\mathrm{HO^-}]=10^{-6{,}5}\iff\mathrm{pH}=7{,}5.$$
Le fer(III) précipite en milieu bien plus acide que le fer(II).

**2. Convention.** Sur une frontière entre deux espèces dissoutes, elles ont la même concentration ; sur une frontière solide/dissous, l'espèce dissoute est à $c=10^{-2}$.

**2. Frontière $\mathrm{Fe^{3+}/Fe^{2+}}$** ($\mathrm{pH}<2$), avec $\mathrm{Fe^{3+}}+e^-=\mathrm{Fe^{2+}}$ :
$$E=0{,}77+0{,}06\log\frac{[\mathrm{Fe^{3+}}]}{[\mathrm{Fe^{2+}}]}=0{,}77\ \mathrm V\quad(\text{horizontale}).$$

**2. Frontière $\mathrm{Fe(OH)_3/Fe^{2+}}$** ($2<\mathrm{pH}<7{,}5$). En présence du solide, $[\mathrm{Fe^{3+}}]=\frac{K_s}{[\mathrm{HO^-}]^3}$, et $[\mathrm{HO^-}]=10^{\mathrm{pH}-14}$, donc $[\mathrm{Fe^{3+}}]=10^{-38}\times10^{3(14-\mathrm{pH})}=10^{4-3\mathrm{pH}}$. Avec $[\mathrm{Fe^{2+}}]=10^{-2}$ :
$$E=0{,}77+0{,}06\log\frac{10^{4-3\mathrm{pH}}}{10^{-2}}=0{,}77+0{,}06(6-3\,\mathrm{pH})=1{,}13-0{,}18\,\mathrm{pH}.$$
Continuité en $\mathrm{pH}=2$ : $1{,}13-0{,}36=0{,}77$ V. ✓

**2. Frontière $\mathrm{Fe(OH)_3/Fe(OH)_2}$** ($\mathrm{pH}>7{,}5$). Les deux solides imposent $[\mathrm{Fe^{3+}}]=10^{4-3\mathrm{pH}}$ et $[\mathrm{Fe^{2+}}]=\frac{10^{-15}}{[\mathrm{HO^-}]^2}=10^{-15}\times10^{2(14-\mathrm{pH})}=10^{13-2\mathrm{pH}}$, donc
$$E=0{,}77+0{,}06\big[(4-3\,\mathrm{pH})-(13-2\,\mathrm{pH})\big]=0{,}77+0{,}06(-9-\mathrm{pH})=0{,}23-0{,}06\,\mathrm{pH}.$$
Continuité en $\mathrm{pH}=7{,}5$ : $1{,}13-0{,}18\times7{,}5=-0{,}22$ V et $0{,}23-0{,}45=-0{,}22$ V. ✓

**3. Frontière $\mathrm{Fe^{2+}/Fe}$** ($\mathrm{pH}<7{,}5$), avec $\mathrm{Fe^{2+}}+2e^-=\mathrm{Fe}$ et $[\mathrm{Fe^{2+}}]=10^{-2}$ :
$$E=-0{,}44+0{,}03\log10^{-2}=-0{,}50\ \mathrm V\quad(\text{horizontale}).$$
Au-delà de pH 7,5 (frontière $\mathrm{Fe(OH)_2/Fe}$), $[\mathrm{Fe^{2+}}]=10^{13-2\mathrm{pH}}$, d'où $E=-0{,}44+0{,}03(13-2\,\mathrm{pH})=-0{,}05-0{,}06\,\mathrm{pH}$. Continuité en 7,5 : $-0{,}50$ V. ✓

**3. Domaines.** De haut en bas : $\mathrm{Fe^{3+}}$ (en haut à gauche) et $\mathrm{Fe(OH)_3}$ (en haut à droite) ; $\mathrm{Fe^{2+}}$ (au milieu, pour $\mathrm{pH}<7{,}5$) et $\mathrm{Fe(OH)_2}$ (pour $\mathrm{pH}>7{,}5$) ; enfin Fe, en bas.

**4. Stabilité du fer dans l'eau.** La frontière inférieure de l'eau, $E=-0{,}06\,\mathrm{pH}$ (couple $\mathrm{H^+/H_2}$), est au-dessus des frontières du fer : $-0{,}50<-0{,}06\,\mathrm{pH}$ pour $\mathrm{pH}<8{,}3$, et $-0{,}05-0{,}06\,\mathrm{pH}<-0{,}06\,\mathrm{pH}$ toujours. Les domaines de Fe et de $\mathrm{H_2O}$ sont disjoints : le fer est **thermodynamiquement oxydé par l'eau**,
$$\mathrm{Fe}+2\,\mathrm{H^+}\to\mathrm{Fe^{2+}}+\mathrm{H_2}\quad(\text{milieu acide}).$$
En milieu neutre, cette réaction est très lente (blocage cinétique).

**4. En présence de dioxygène.** $\mathrm O_2$ (frontière $E=1{,}23-0{,}06\,\mathrm{pH}$, bien au-dessus) oxyde le fer jusqu'au degré +III. En milieu neutre, il se forme $\mathrm{Fe(OH)_3}$ (ou des oxyhydroxydes), qui est la **rouille** :
$$4\,\mathrm{Fe}+3\,\mathrm O_2+6\,\mathrm{H_2O}\to4\,\mathrm{Fe(OH)_3}.$$
C'est la corrosion humide du fer. La rouille, poreuse, ne protège pas le métal sous-jacent, contrairement à l'alumine sur l'aluminium.
"""

D['n-c-flamme'] = r"""
**1. Équation de combustion.** On équilibre C, puis H, puis O :
$$\mathrm{CH_4(g)}+2\,\mathrm{O_2(g)}\to\mathrm{CO_2(g)}+2\,\mathrm{H_2O(g)}.$$

**1. Enthalpie standard de réaction.** Loi de Hess ; $\Delta_fH^\circ(\mathrm{O_2})=0$ (corps simple dans son état standard) :
$$\Delta_rH^\circ=\Delta_fH^\circ(\mathrm{CO_2})+2\Delta_fH^\circ(\mathrm{H_2O})-\Delta_fH^\circ(\mathrm{CH_4})=-393{,}5-483{,}6+74{,}8=-802{,}3\ \mathrm{kJ\,mol^{-1}}.$$
La réaction est très exothermique (pouvoir calorifique inférieur, l'eau étant gazeuse).

**2. Bilan de matière** pour 1 mol de $\mathrm{CH_4}$. Il faut 2 mol de $\mathrm{O_2}$, apportées par l'air, qui contient $\frac15$ de $\mathrm O_2$ : il faut 10 mol d'air, soit 2 mol de $\mathrm O_2$ et 8 mol de $\mathrm N_2$. En fin de réaction, totale et stœchiométrique :

| espèce | $\mathrm{CO_2}$ | $\mathrm{H_2O(g)}$ | $\mathrm{N_2}$ | $\mathrm{CH_4}$, $\mathrm{O_2}$ |
|---|---|---|---|---|
| quantité (mol) | 1 | 2 | 8 | 0 |

$\mathrm N_2$ ne réagit pas, mais il doit être chauffé.

**3. Bilan enthalpique.** La transformation est isobare et adiabatique (combustion rapide) : $\Delta H=Q_P=0$. $H$ étant une fonction d'état, on utilise un chemin fictif en deux étapes :
- **(a)** la réaction totale à 298 K : $\Delta H_a=\xi\Delta_rH^\circ=-802{,}3$ kJ (pour $\xi=1$ mol) ;
- **(b)** l'échauffement des produits (et de $\mathrm N_2$) de 298 K à $T_f$ : $\Delta H_b=\Big(\sum n_iC_{p,i}\Big)(T_f-298)$.

**3. Capacité thermique des produits.**
$$\sum n_iC_{p,i}=1\times37+2\times34+8\times29=37+68+232=337\ \mathrm{J\,K^{-1}}.$$
L'azote représente plus des deux tiers de la capacité thermique.

**3. Température de flamme.** $\Delta H_a+\Delta H_b=0$, donc
$$T_f=298+\frac{802\,300}{337}=298+2381\approx2\,680\ \mathrm K.$$

**4. Pourquoi la flamme réelle est-elle plus froide (environ 2200 K) ?**
- **Pertes thermiques** : la flamme n'est pas adiabatique, elle rayonne beaucoup à haute température, et elle échange par convection avec l'air environnant.
- **Dissociation des produits** : à haute température, les équilibres $\mathrm{CO_2}\rightleftharpoons\mathrm{CO}+\frac12\mathrm O_2$ et $\mathrm{H_2O}\rightleftharpoons\mathrm H+\mathrm{OH}$ (ou $\mathrm{H_2}+\frac12\mathrm O_2$) se déplacent vers la droite. Ces réactions sont endothermiques, elles absorbent une partie de l'énergie, et la combustion est incomplète.
- Les capacités thermiques augmentent avec $T$ (excitation des vibrations moléculaires) : il faut plus d'énergie par kelvin.

**Remarque.** Dans du dioxygène pur, il n'y a pas d'azote à chauffer : $\sum C_p=105\ \mathrm{J\,K^{-1}}$, et la température calculée serait beaucoup plus élevée (limitée en pratique par la dissociation, vers 3000 K). C'est le principe du chalumeau oxyacétylénique utilisé en soudure.
"""

D['n-c-ellingham'] = r"""
**1. Interprétation des pentes.** Dans l'approximation d'Ellingham, $\Delta_rH^\circ$ et $\Delta_rS^\circ$ sont indépendants de $T$, donc $\Delta_rG^\circ(T)=\Delta_rH^\circ-T\Delta_rS^\circ$ est affine en $T$, de pente $-\Delta_rS^\circ$. Le signe de $\Delta_rS^\circ$ est gouverné par la variation de la quantité de gaz $\Delta n_g$ (les gaz ont des entropies molaires bien plus grandes que les solides).
- **Réaction 1** ($2\,\mathrm C+\mathrm O_2\to2\,\mathrm{CO}$) : $\Delta n_g=2-1=+1>0$, donc $\Delta_rS^\circ>0$ ($+179\ \mathrm{J\,K^{-1}\,mol^{-1}}$) et la pente est **négative**. La droite descend : le carbone devient de plus en plus réducteur quand $T$ augmente.
- **Réaction 2** ($2\,\mathrm{Zn}+\mathrm O_2\to2\,\mathrm{ZnO}$, zinc condensé) : $\Delta n_g=0-1=-1<0$, donc $\Delta_rS^\circ<0$ ($-201\ \mathrm{J\,K^{-1}\,mol^{-1}}$) et la pente est **positive**. C'est le cas général des oxydes métalliques.

**2. Réaction de réduction.** On fait (1) $-$ (2) :
$$2\,\mathrm{ZnO}+2\,\mathrm C\to2\,\mathrm{Zn}+2\,\mathrm{CO},$$
$$\Delta_rG^\circ=\Delta_rG^\circ_1-\Delta_rG^\circ_2=(-221-0{,}179\,T)-(-696+0{,}201\,T)=475-0{,}380\,T\quad(\mathrm{kJ\,mol^{-1}}).$$

**2. Température d'inversion.** La réaction est thermodynamiquement favorable ($K>1$) si $\Delta_rG^\circ<0$, soit
$$T>T_i=\frac{475}{0{,}380}=1\,250\ \mathrm K.$$
Graphiquement, au-delà de $T_i$, la droite du couple $\mathrm{CO/C}$ passe sous celle du couple $\mathrm{ZnO/Zn}$ : le réducteur du couple inférieur (C) réduit l'oxydant du couple supérieur (ZnO).

**3. Ébullition du zinc.** Mais $T_i=1250$ K dépasse la température d'ébullition du zinc (1180 K) : l'expression de $\Delta_rG^\circ_2$ n'est plus valable dans ce domaine. Au-delà de 1180 K, la réaction 2 s'écrit $2\,\mathrm{Zn(g)}+\mathrm O_2\to2\,\mathrm{ZnO(s)}$, avec $\Delta n_g=-3$. Son entropie de réaction diminue de $2\Delta_{\mathrm{vap}}S^\circ(\mathrm{Zn})$ : $\Delta_rS^\circ_2$ devient encore plus négatif, et la **pente augmente** (point anguleux sur la droite d'Ellingham, à 1180 K). La droite (2) monte donc plus vite au-delà de 1180 K.

**3. Conséquence.** À 1180 K, $\Delta_rG^\circ$ (réduction) $=475-0{,}380\times1180\approx+27$ kJ/mol, encore positif. Au-delà, il décroît plus vite qu'avant : il s'annule donc **avant** 1250 K. Avec $\Delta_{\mathrm{vap}}H^\circ(\mathrm{Zn})\approx115\ \mathrm{kJ\,mol^{-1}}$, on a $\Delta_{\mathrm{vap}}S^\circ\approx\frac{115}{1180}\approx0{,}097\ \mathrm{kJ\,K^{-1}\,mol^{-1}}$ : la pente de $\Delta_rG^\circ$ passe à $-0{,}380-2\times0{,}097\approx-0{,}575$, et $\Delta_rG^\circ=0$ vers $1180+\frac{27}{0{,}575}\approx1230$ K. La température d'inversion est abaissée, entre 1180 et 1250 K.

**4. Récupération du zinc.** À la température de réduction (vers 1300 K dans le four), le zinc est produit à l'état **gazeux** : il quitte le four avec le monoxyde de carbone. C'est d'ailleurs favorable : l'élimination du produit gazeux déplace l'équilibre.

**4. Condensation.** En se refroidissant, le mélange $\mathrm{Zn(g)}+\mathrm{CO}$ (et un peu de $\mathrm{CO_2}$) repasse sous la température d'inversion : la réaction inverse, la réoxydation du zinc en ZnO, redevient favorable. Il faut donc **refroidir brutalement** la vapeur pour la condenser plus vite qu'elle ne se réoxyde. Dans le procédé Imperial Smelting, on la condense sur une pluie de plomb liquide, qui absorbe le zinc ; on le sépare ensuite par refroidissement.
===RÉPONSE===
Pentes $=-\Delta_rS^\circ$ (signe de $-\Delta n_g$) ; $\Delta_rG^\circ=475-0{,}380\,T$, favorable au-delà de $1\,250$ K ; avec Zn gazeux (> 1 180 K), la pente augmente et l'inversion est abaissée (≈ 1 230 K).
"""
