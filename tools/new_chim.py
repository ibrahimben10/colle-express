# Chimie — programme MPSI / MP
from newlib import ex
K = 'Chimie'

ex('n-c-fer', K, 'Atomistique', 1, 'Configuration électronique du fer et de ses ions', 10, r"""
Le fer a pour numéro atomique $Z=26$.

1. Donner la configuration électronique du fer dans son état fondamental, en précisant les règles utilisées. Identifier les électrons de valence.
2. En déduire la position du fer dans la classification (période, colonne, bloc).
3. Donner les configurations des ions $\mathrm{Fe^{2+}}$ et $\mathrm{Fe^{3+}}$. Proposer une explication à la stabilité particulière de $\mathrm{Fe^{3+}}$.
4. Le cuivre ($Z=29$) fait exception à la règle de Klechkowski. Quelle est sa configuration réelle ?
""",
r"Règle de Klechkowski (remplissage par $n+\ell$ croissant), principe de Pauli, règle de Hund.",
r"Les électrons de valence sont ceux de la couche de $n$ le plus élevé et des sous-couches en cours de remplissage : ici $4s$ et $3d$.",
r"Les ions des métaux de transition perdent d'abord les électrons $4s$. Une sous-couche $3d$ à moitié remplie est particulièrement stable.",
r"""
**1.** Klechkowski (ordre $1s,2s,2p,3s,3p,4s,3d$), avec au plus 2 électrons par orbitale (Pauli) : $\mathrm{Fe}:1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,4s^2\,3d^6$, soit $[\mathrm{Ar}]\,4s^2\,3d^6$. Électrons de valence : $4s^2\,3d^6$, soit 8. D'après la règle de Hund, les 6 électrons $3d$ occupent les 5 orbitales avec un maximum de spins parallèles : 4 électrons célibataires (fer paramagnétique à l'état atomique).

**2.** $n_{\max}=4$ : 4ᵉ période. Le remplissage se termine par la sous-couche $3d$ : bloc $d$. Avec 8 électrons de valence : 8ᵉ colonne.

**3.** On retire d'abord les électrons $4s$ : $\mathrm{Fe^{2+}}:[\mathrm{Ar}]\,3d^6$ et $\mathrm{Fe^{3+}}:[\mathrm{Ar}]\,3d^5$. La sous-couche $3d^5$ est à moitié pleine, avec 5 électrons célibataires de spins parallèles : configuration symétrique, à énergie d'échange favorable. C'est pourquoi $\mathrm{Fe^{2+}}$ s'oxyde facilement à l'air en $\mathrm{Fe^{3+}}$.

**4.** Klechkowski prévoit $[\mathrm{Ar}]\,4s^2\,3d^9$, mais la configuration réelle est $[\mathrm{Ar}]\,4s^1\,3d^{10}$ : la sous-couche $3d$ pleine est plus stable.
""", r"Fe : $[\mathrm{Ar}]4s^23d^6$, 4ᵉ période, colonne 8, bloc $d$ ; $\mathrm{Fe^{2+}}:[\mathrm{Ar}]3d^6$, $\mathrm{Fe^{3+}}:[\mathrm{Ar}]3d^5$ ; Cu : $[\mathrm{Ar}]4s^13d^{10}$.")

ex('n-c-vsepr', K, 'Structure des molécules', 1, 'Lewis, VSEPR et polarité', 15, r"""
On étudie les molécules $\mathrm{CO_2}$, $\mathrm{H_2O}$, $\mathrm{NH_3}$ et $\mathrm{BF_3}$.

On donne les numéros atomiques : H (1), B (5), C (6), N (7), O (8), F (9), et les électronégativités de Pauling : H 2,2 ; B 2,0 ; C 2,6 ; N 3,0 ; O 3,4 ; F 4,0.

1. Écrire la représentation de Lewis de chaque molécule.
2. Prévoir leur géométrie par la méthode VSEPR (type $\mathrm{AX}_n\mathrm{E}_m$) et donner un ordre de grandeur des angles de liaison.
3. Lesquelles sont polaires ? Justifier.
4. Pourquoi l'angle $\widehat{\mathrm{HOH}}$ ($104{,}5^\circ$) est-il inférieur à l'angle $\widehat{\mathrm{HNH}}$ ($107^\circ$) ?
""",
r"Compte les électrons de valence : C 4, O 6, N 5, B 3, F 7, H 1. Le bore est une exception à l'octet (lacune électronique).",
r"$\mathrm{CO_2}$ : $\mathrm{AX_2}$ ; $\mathrm{H_2O}$ : $\mathrm{AX_2E_2}$ ; $\mathrm{NH_3}$ : $\mathrm{AX_3E}$ ; $\mathrm{BF_3}$ : $\mathrm{AX_3}$.",
r"Une molécule est polaire si la somme vectorielle des moments dipolaires de liaison est non nulle ; les doublets non liants occupent plus de place que les doublets liants.",
r"""
**1.** $\mathrm{O{=}C{=}O}$ avec deux doublets non liants sur chaque O (16 électrons) ; $\mathrm{H_2O}$ : O lié à deux H, avec deux doublets non liants ; $\mathrm{NH_3}$ : N lié à trois H, avec un doublet non liant ; $\mathrm{BF_3}$ : B lié à trois F (chacun avec trois doublets non liants), le bore n'a que 6 électrons autour de lui (**lacune électronique**, acide de Lewis).

**2.**
- $\mathrm{CO_2}$, $\mathrm{AX_2}$ : linéaire, $180^\circ$ ;
- $\mathrm{H_2O}$, $\mathrm{AX_2E_2}$ : figure de répulsion tétraédrique, molécule coudée, angle $<109^\circ$ ;
- $\mathrm{NH_3}$, $\mathrm{AX_3E}$ : pyramide à base triangulaire, angle $<109^\circ$ ;
- $\mathrm{BF_3}$, $\mathrm{AX_3}$ : triangulaire plane, $120^\circ$.

**3.** Les liaisons sont toutes polarisées (différences d'électronégativité). Dans $\mathrm{CO_2}$ (linéaire) et $\mathrm{BF_3}$ (triangle équilatéral), les moments de liaison se compensent par symétrie : **apolaires**. $\mathrm{H_2O}$ et $\mathrm{NH_3}$ sont **polaires** (moment dirigé vers O ou N, du côté des doublets non liants).

**4.** Les doublets non liants, attirés par un seul noyau, sont plus volumineux et repoussent davantage les doublets liants. L'eau en a deux, l'ammoniac un seul : les liaisons O–H sont plus resserrées.
""", r"$\mathrm{CO_2}$ linéaire, apolaire ; $\mathrm{H_2O}$ coudée, polaire ; $\mathrm{NH_3}$ pyramidale, polaire ; $\mathrm{BF_3}$ plane, apolaire.")

ex('n-c-h2o2', K, 'Cinétique', 1, 'Décomposition de l’eau oxygénée', 15, r"""
On suit la décomposition $\mathrm{2\,H_2O_2\to2\,H_2O+O_2}$ catalysée, à température constante, dans $V=1{,}0\ \mathrm L$ de solution. On mesure la concentration en $\mathrm{H_2O_2}$ :

| $t$ (s) | 0 | 300 | 600 | 900 | 1200 |
|---|---|---|---|---|---|
| $[\mathrm{H_2O_2}]$ (mol L⁻¹) | 0,100 | 0,0741 | 0,0549 | 0,0407 | 0,0301 |

1. Montrer que ces résultats sont compatibles avec une loi de vitesse d'ordre 1 par rapport à $\mathrm{H_2O_2}$. Déterminer la constante de vitesse $k$.
2. Calculer le temps de demi-réaction. Dépend-il de la concentration initiale ?
3. Quel volume de dioxygène a-t-on recueilli à $t=600$ s, à $25\ ^\circ\mathrm C$ et sous $1$ bar ?

On donne : $R=8{,}31\ \mathrm{J\,K^{-1}\,mol^{-1}}$.
""",
r"Pour un ordre 1, $\ln[\mathrm{H_2O_2}]$ est une fonction affine du temps : calcule $\ln(c_0/c)$ pour chaque date.",
r"$\ln\dfrac{c_0}c=kt$ ; $t_{1/2}=\dfrac{\ln2}k$.",
r"Une mole de $\mathrm{O_2}$ se forme pour deux moles de $\mathrm{H_2O_2}$ décomposées ; volume molaire $RT/P$.",
r"""
**1.** $\ln(c_0/c)$ vaut $0$ ; $0{,}300$ ; $0{,}600$ ; $0{,}900$ ; $1{,}20$ : il est proportionnel à $t$, ce qui caractérise l'ordre 1 ($\frac{\mathrm dc}{\mathrm dt}=-kc$ donne $c=c_0e^{-kt}$). La pente donne $k=1{,}0\times10^{-3}\ \mathrm{s^{-1}}$.

**2.** $t_{1/2}=\dfrac{\ln2}k\approx693\ \mathrm s\approx12$ min, indépendant de $c_0$ : c'est caractéristique de l'ordre 1.

**3.** À $600$ s : $n(\mathrm{H_2O_2})$ décomposé $=(0{,}100-0{,}0549)\times1{,}0=0{,}0451$ mol, donc $n(\mathrm{O_2})=0{,}0226$ mol. Volume : $V=\dfrac{nRT}P=\dfrac{0{,}0226\times8{,}31\times298}{10^5}\approx5{,}6\times10^{-4}\ \mathrm{m^3}=0{,}56\ \mathrm L$.
""", r"Ordre 1, $k=1{,}0\times10^{-3}$ s⁻¹ ; $t_{1/2}\approx693$ s ; $V(\mathrm{O_2})\approx0{,}56$ L.")

ex('n-c-arrhenius', K, 'Cinétique', 1, 'Loi d’Arrhenius et conservation des aliments', 10, r"""
Une règle empirique affirme que la vitesse de nombreuses réactions double quand la température passe de $25\ ^\circ\mathrm C$ à $35\ ^\circ\mathrm C$.

On donne : $R=8{,}31\ \mathrm{J\,K^{-1}\,mol^{-1}}$.

1. Rappeler la loi d'Arrhenius. En déduire l'énergie d'activation correspondant à cette règle.
2. Par quel facteur la vitesse est-elle multipliée entre $25\ ^\circ\mathrm C$ et $60\ ^\circ\mathrm C$ ?
3. Pourquoi conserve-t-on les aliments au réfrigérateur ($4\ ^\circ\mathrm C$) ? Estimer le facteur de ralentissement des réactions de dégradation par rapport à $25\ ^\circ\mathrm C$, en supposant la même énergie d'activation.
""",
r"$k=A\exp\left(-\dfrac{E_a}{RT}\right)$ ; écris le rapport $k_2/k_1$.",
r"$\ln\dfrac{k_2}{k_1}=\dfrac{E_a}R\left(\dfrac1{T_1}-\dfrac1{T_2}\right)$, avec $T$ en kelvins.",
r"Applique la même relation entre $277$ K et $298$ K.",
r"""
**1.** $k(T)=A\exp\left(-\dfrac{E_a}{RT}\right)$, donc $\ln\dfrac{k_2}{k_1}=\dfrac{E_a}R\left(\dfrac1{T_1}-\dfrac1{T_2}\right)$. Avec $k_2/k_1=2$, $T_1=298$ K, $T_2=308$ K :
$$E_a=\frac{R\ln2}{\frac1{298}-\frac1{308}}=\frac{8{,}31\times0{,}693}{1{,}09\times10^{-4}}\approx53\ \mathrm{kJ\,mol^{-1}}.$$

**2.** $\ln\dfrac{k_{333}}{k_{298}}=\dfrac{53\times10^3}{8{,}31}\left(\dfrac1{298}-\dfrac1{333}\right)\approx2{,}24$ : facteur $\approx9{,}4$.

**3.** $\ln\dfrac{k_{298}}{k_{277}}=6\,370\times\left(\dfrac1{277}-\dfrac1{298}\right)\approx1{,}62$ : les réactions (et la croissance microbienne, qui suit une loi voisine) sont environ **5 fois plus lentes** au réfrigérateur.
""", r"$E_a\approx53$ kJ/mol ; facteur ≈ 9,4 entre 25 et 60 °C ; ≈ 5 fois plus lent à 4 °C.")

ex('n-c-vitinit', K, 'Cinétique', 1, 'Méthode des vitesses initiales', 15, r"""
On étudie la réaction $\mathrm{2\,NO+O_2\to2\,NO_2}$ en phase gazeuse, à température constante. On suppose une loi de vitesse de la forme $v=k[\mathrm{NO}]^\alpha[\mathrm{O_2}]^\beta$. On mesure la vitesse initiale pour différentes concentrations initiales :

| Expérience | $[\mathrm{NO}]_0$ (mol L⁻¹) | $[\mathrm{O_2}]_0$ (mol L⁻¹) | $v_0$ (mol L⁻¹ s⁻¹) |
|---|---|---|---|
| 1 | 0,010 | 0,010 | $2{,}5\times10^{-5}$ |
| 2 | 0,020 | 0,010 | $1{,}0\times10^{-4}$ |
| 3 | 0,010 | 0,020 | $5{,}0\times10^{-5}$ |

1. Déterminer les ordres partiels $\alpha$ et $\beta$, puis la constante $k$ (avec son unité).
2. La réaction peut-elle être un acte élémentaire ? Commenter.
3. Proposer une autre méthode expérimentale pour déterminer $\beta$ seul.
""",
r"Compare deux expériences où une seule concentration change : le rapport des vitesses vaut $2^\alpha$ ou $2^\beta$.",
r"$\alpha=2$, $\beta=1$ ; $k=\dfrac{v_0}{[\mathrm{NO}]_0^2[\mathrm{O_2}]_0}$, en $\mathrm{L^2\,mol^{-2}\,s^{-1}}$.",
r"Méthode de la dégénérescence de l'ordre : un grand excès de NO rend $[\mathrm{NO}]$ quasi constante.",
r"""
**1.** Expériences 1 et 2 : $[\mathrm{NO}]_0$ double et $v_0$ est multipliée par 4 : $2^\alpha=4$, $\alpha=2$. Expériences 1 et 3 : $[\mathrm{O_2}]_0$ double et $v_0$ double : $\beta=1$. Puis
$$k=\frac{2{,}5\times10^{-5}}{(0{,}010)^2\times0{,}010}=25\ \mathrm{L^2\,mol^{-2}\,s^{-1}}.$$

**2.** Les ordres coïncident avec les coefficients stœchiométriques, ce qui est compatible avec un acte élémentaire trimoléculaire. Mais la rencontre simultanée de trois molécules est très improbable : on admet plutôt un mécanisme en deux étapes (pré-équilibre rapide $\mathrm{2\,NO\rightleftharpoons N_2O_2}$, puis $\mathrm{N_2O_2+O_2\to2\,NO_2}$) qui conduit à la même loi de vitesse. La loi de vitesse ne prouve pas le mécanisme.

**3.** Dégénérescence de l'ordre : avec $[\mathrm{NO}]_0\gg[\mathrm{O_2}]_0$, $v\approx k_{\text{app}}[\mathrm{O_2}]^\beta$ avec $k_{\text{app}}=k[\mathrm{NO}]_0^2$. On suit $[\mathrm{O_2}](t)$ et on teste $\ln[\mathrm{O_2}]$ affine en $t$ (ordre 1).
""", r"$\alpha=2$, $\beta=1$, $k=25\ \mathrm{L^2\,mol^{-2}\,s^{-1}}$.")

ex('n-c-ethanoique', K, 'Acide-base', 1, 'Titrage de l’acide éthanoïque', 20, r"""
On titre $V_a=20{,}0\ \mathrm{mL}$ d'une solution d'acide éthanoïque $\mathrm{CH_3COOH}$ de concentration $c_a=0{,}100\ \mathrm{mol\,L^{-1}}$ par une solution d'hydroxyde de sodium de concentration $c_b=0{,}100\ \mathrm{mol\,L^{-1}}$.

On donne : $\mathrm{p}K_a(\mathrm{CH_3COOH/CH_3COO^-})=4{,}76$, $\mathrm{p}K_e=14{,}0$.

1. Écrire la réaction de titrage et calculer sa constante. Conclure.
2. Calculer le pH initial de la solution d'acide (en justifiant les approximations).
3. Calculer le volume équivalent et le pH à la demi-équivalence.
4. Calculer le pH à l'équivalence. Quel indicateur coloré choisir parmi l'hélianthine (zone de virage 3,1–4,4), le bleu de bromothymol (6,0–7,6) et la phénolphtaléine (8,2–10,0) ?
""",
r"$\mathrm{CH_3COOH+HO^-\to CH_3COO^-+H_2O}$, $K=\dfrac{K_a}{K_e}$.",
r"Acide faible peu dissocié : $\mathrm{pH}=\frac12(\mathrm pK_a-\log c_a)$ ; vérifie ensuite que la dissociation est faible. À la demi-équivalence, $[\mathrm{CH_3COOH}]=[\mathrm{CH_3COO^-}]$.",
r"À l'équivalence, la solution contient la base faible $\mathrm{CH_3COO^-}$ à $c=0{,}050$ mol/L : $\mathrm{pOH}=\frac12(\mathrm pK_b-\log c)$.",
r"""
**1.** $\mathrm{CH_3COOH+HO^-\to CH_3COO^-+H_2O}$, $K=\dfrac{K_a}{K_e}=10^{14-4{,}76}=10^{9{,}24}$ : réaction quasi totale, adaptée à un titrage.

**2.** L'acide est faible : on suppose sa dissociation faible et l'autoprotolyse de l'eau négligeable. $K_a=\dfrac{h^2}{c_a}$, d'où $\mathrm{pH}=\frac12(\mathrm pK_a-\log c_a)=\frac12(4{,}76+1)=2{,}88$. Vérification : $h/c_a=1{,}3\times10^{-3}/0{,}1=1{,}3\ \%\ll1$ ✓, et $\mathrm{pH}<6{,}5$ ✓.

**3.** $V_{eq}=\dfrac{c_aV_a}{c_b}=20{,}0\ \mathrm{mL}$. À $V_{eq}/2$, la moitié de l'acide est transformée : $[\mathrm{CH_3COOH}]=[\mathrm{CH_3COO^-}]$ et $\mathrm{pH}=\mathrm pK_a=4{,}76$.

**4.** À l'équivalence : $\mathrm{CH_3COO^-}$ à $c=\dfrac{c_aV_a}{V_a+V_{eq}}=0{,}050\ \mathrm{mol\,L^{-1}}$, base faible de $\mathrm pK_b=9{,}24$. $\mathrm{pOH}=\frac12(9{,}24-\log0{,}050)=\frac12(9{,}24+1{,}30)=5{,}27$, donc $\mathrm{pH}\approx8{,}73$. On choisit la **phénolphtaléine**, dont la zone de virage contient ce pH.
""", r"$K=10^{9{,}24}$ ; pH initial 2,88 ; $V_{eq}=20{,}0$ mL, pH 4,76 à la demi-équivalence ; pH ≈ 8,73 à l'équivalence : phénolphtaléine.")

ex('n-c-tampon', K, 'Acide-base', 1, 'Solution tampon', 10, r"""
On prépare $1{,}0\ \mathrm L$ de solution contenant $0{,}10$ mol d'acide éthanoïque et $0{,}10$ mol d'éthanoate de sodium ($\mathrm pK_a=4{,}76$).

1. Quel est le pH de cette solution ?
2. On ajoute $0{,}010$ mol d'acide chlorhydrique (sans variation de volume). Calculer le nouveau pH.
3. Comparer avec l'ajout de la même quantité d'acide chlorhydrique dans $1{,}0$ L d'eau pure. Conclure sur le rôle d'une solution tampon.
""",
r"Relation de Henderson : $\mathrm{pH}=\mathrm pK_a+\log\dfrac{[\mathrm A^-]}{[\mathrm{AH}]}$.",
r"Les ions $\mathrm{H_3O^+}$ ajoutés réagissent totalement avec la base : $\mathrm{CH_3COO^-+H_3O^+\to CH_3COOH+H_2O}$.",
r"Dans l'eau pure, l'acide fort est totalement dissocié : $[\mathrm{H_3O^+}]=0{,}010$ mol/L.",
r"""
**1.** $[\mathrm{CH_3COO^-}]=[\mathrm{CH_3COOH}]$, donc $\mathrm{pH}=\mathrm pK_a=4{,}76$.

**2.** $\mathrm{CH_3COO^-+H_3O^+\to CH_3COOH+H_2O}$ est quasi totale ($K=10^{4{,}76}$). Il reste $0{,}09$ mol de base et il y a $0{,}11$ mol d'acide : $\mathrm{pH}=4{,}76+\log\dfrac{0{,}09}{0{,}11}\approx4{,}67$.

**3.** Dans l'eau pure, $\mathrm{pH}=-\log0{,}010=2{,}0$ : une chute de 5 unités, contre $0{,}09$ unité ici. Une solution tampon (mélange équimolaire d'un acide faible et de sa base conjuguée) modère fortement les variations de pH lors d'ajouts modérés d'acide ou de base ; son pouvoir tampon est maximal à $\mathrm{pH}=\mathrm pK_a$.
""", r"pH 4,76 → 4,67 après ajout (eau pure : 7 → 2,0).")

ex('n-c-agcl', K, 'Solubilité', 1, 'Solubilité du chlorure d’argent', 15, r"""
On donne : $\mathrm pK_s(\mathrm{AgCl})=9{,}75$ à $25\ ^\circ\mathrm C$, $M(\mathrm{AgCl})=143{,}3\ \mathrm{g\,mol^{-1}}$.

1. Calculer la solubilité $s$ du chlorure d'argent dans l'eau pure, en $\mathrm{mol\,L^{-1}}$ puis en $\mathrm{mg\,L^{-1}}$.
2. Calculer sa solubilité dans une solution de chlorure de sodium à $0{,}10\ \mathrm{mol\,L^{-1}}$. Nommer l'effet observé.
3. On mélange $10\ \mathrm{mL}$ de nitrate d'argent à $1{,}0\times10^{-4}\ \mathrm{mol\,L^{-1}}$ et $10\ \mathrm{mL}$ de chlorure de sodium à $1{,}0\times10^{-4}\ \mathrm{mol\,L^{-1}}$. Observe-t-on un précipité ? Et si les deux solutions sont dix fois plus diluées ?
""",
r"$\mathrm{AgCl(s)\rightleftharpoons Ag^++Cl^-}$ : dans l'eau pure, $[\mathrm{Ag^+}]=[\mathrm{Cl^-}]=s$ et $K_s=s^2$.",
r"Avec $[\mathrm{Cl^-}]\approx0{,}10$ mol/L imposé par NaCl, $s'=K_s/0{,}10$.",
r"Calcule le quotient $Q=[\mathrm{Ag^+}][\mathrm{Cl^-}]$ juste après le mélange (dilution par 2) et compare à $K_s$.",
r"""
**1.** $K_s=s^2$, donc $s=10^{-9{,}75/2}\approx1{,}3\times10^{-5}\ \mathrm{mol\,L^{-1}}$, soit $1{,}9\ \mathrm{mg\,L^{-1}}$ : AgCl est très peu soluble.

**2.** $s'=[\mathrm{Ag^+}]=\dfrac{K_s}{[\mathrm{Cl^-}]}=\dfrac{1{,}8\times10^{-10}}{0{,}10}=1{,}8\times10^{-9}\ \mathrm{mol\,L^{-1}}$ (on vérifie $s'\ll0{,}10$). La solubilité est divisée par environ $10^4$ : **effet d'ion commun**.

**3.** Après mélange, chaque ion est à $5{,}0\times10^{-5}$ mol/L : $Q=2{,}5\times10^{-9}>K_s=1{,}8\times10^{-10}$ : il y a précipitation. Avec des solutions dix fois plus diluées : $Q=2{,}5\times10^{-11}<K_s$ : pas de précipité, la solution reste limpide.
""", r"$s\approx1{,}3\times10^{-5}$ mol/L (1,9 mg/L) ; $s'\approx1{,}8\times10^{-9}$ mol/L (ion commun) ; précipité dans le 1er cas, pas dans le 2nd.")

ex('n-c-mgoh2', K, 'Solubilité', 2, 'Hydroxyde de magnésium et pH', 20, r"""
On donne : $\mathrm pK_s(\mathrm{Mg(OH)_2})=11{,}2$, $\mathrm pK_e=14{,}0$.

1. Calculer la solubilité de l'hydroxyde de magnésium dans l'eau pure et le pH de la solution saturée.
2. Une solution contient des ions $\mathrm{Mg^{2+}}$ à $1{,}0\times10^{-2}\ \mathrm{mol\,L^{-1}}$. On ajoute progressivement une base forte (sans variation de volume). À quel pH apparaît le précipité ?
3. Exprimer $\log s$ en fonction du pH lorsque le solide est présent et tracer l'allure du graphe.
4. Le « lait de magnésie », suspension de $\mathrm{Mg(OH)_2}$, est un antiacide gastrique. Expliquer.
""",
r"$\mathrm{Mg(OH)_2(s)\rightleftharpoons Mg^{2+}+2\,HO^-}$ : dans l'eau pure, $[\mathrm{Mg^{2+}}]=s$, $[\mathrm{HO^-}]=2s$, $K_s=4s^3$.",
r"Début de précipitation : $[\mathrm{Mg^{2+}}][\mathrm{HO^-}]^2=K_s$ avec $[\mathrm{Mg^{2+}}]=10^{-2}$.",
r"$s=[\mathrm{Mg^{2+}}]=\dfrac{K_s}{[\mathrm{HO^-}]^2}=\dfrac{K_sh^2}{K_e^2}$, d'où $\log s=2\mathrm pK_e-\mathrm pK_s-2\,\mathrm{pH}$.",
r"""
**1.** $s=\left(\dfrac{K_s}4\right)^{1/3}=\left(\dfrac{6{,}3\times10^{-12}}4\right)^{1/3}\approx1{,}2\times10^{-4}\ \mathrm{mol\,L^{-1}}$. Alors $[\mathrm{HO^-}]=2s\approx2{,}3\times10^{-4}$, $\mathrm{pOH}\approx3{,}6$ et $\mathrm{pH}\approx10{,}4$.

**2.** Le précipité apparaît quand $[\mathrm{HO^-}]=\sqrt{K_s/10^{-2}}=10^{-4{,}6}$, soit $\mathrm{pH}=14-4{,}6=9{,}4$.

**3.** En présence du solide : $s=[\mathrm{Mg^{2+}}]=\dfrac{K_s}{[\mathrm{HO^-}]^2}$, d'où $\log s=2\mathrm pK_e-\mathrm pK_s-2\,\mathrm{pH}=16{,}8-2\,\mathrm{pH}$ : droite de pente $-2$. La solubilité est énorme en milieu acide (le solide disparaît totalement) et devient faible en milieu basique.

**4.** Dans l'estomac (pH $\approx2$), $\mathrm{Mg(OH)_2+2\,H_3O^+\to Mg^{2+}+4\,H_2O}$ est très favorable : le solide neutralise l'excès d'acide. Peu soluble dans l'eau, il ne rend pas le milieu fortement basique avant d'être ingéré.
""", r"$s\approx1{,}2\times10^{-4}$ mol/L, pH 10,4 ; précipitation à pH 9,4 ; $\log s=16{,}8-2\,\mathrm{pH}$.")

ex('n-c-nacl', K, 'Cristallographie', 1, 'Structure du chlorure de sodium', 20, r"""
Le chlorure de sodium cristallise dans une structure où les ions $\mathrm{Cl^-}$ forment un réseau cubique à faces centrées, les ions $\mathrm{Na^+}$ occupant tous les sites octaédriques. Le paramètre de maille vaut $a=564\ \mathrm{pm}$.

On donne : $M(\mathrm{NaCl})=58{,}4\ \mathrm{g\,mol^{-1}}$, $N_A=6{,}02\times10^{23}\ \mathrm{mol^{-1}}$, $r(\mathrm{Cl^-})=181\ \mathrm{pm}$.

1. Dénombrer les ions de chaque type par maille. Vérifier l'électroneutralité.
2. Donner la coordinence de chaque ion.
3. Calculer la masse volumique du cristal.
4. Les ions de signes opposés sont tangents le long d'une arête. En déduire le rayon de $\mathrm{Na^+}$. Vérifier que les anions ne sont pas en contact entre eux, et que le rapport $r_+/r_-$ est compatible avec cette structure.
5. Calculer la compacité.
""",
r"CFC : 8 sommets ($\times\frac18$) et 6 faces ($\times\frac12$). Sites octaédriques : centre du cube et milieux des 12 arêtes ($\times\frac14$).",
r"$\rho=\dfrac{4M}{N_Aa^3}$ ; contact cation-anion selon l'arête : $r_++r_-=a/2$.",
r"Les anions sont les plus proches selon la diagonale d'une face : il faut $2r_-\le a\sqrt2/2$. Structure NaCl stable pour $\sqrt2-1\le r_+/r_-\le\sqrt3-1$.",
r"""
**1.** $\mathrm{Cl^-}$ : $8\times\frac18+6\times\frac12=4$. $\mathrm{Na^+}$ : $1+12\times\frac14=4$. Quatre motifs NaCl par maille, électroneutralité vérifiée.

**2.** Chaque $\mathrm{Na^+}$ est au centre d'un octaèdre de $\mathrm{Cl^-}$ : coordinence 6. Par symétrie de la structure (les deux sous-réseaux sont CFC, décalés de $a/2$), $\mathrm{Cl^-}$ est aussi de coordinence 6 : structure [6,6].

**3.** $\rho=\dfrac{4M}{N_Aa^3}=\dfrac{4\times58{,}4\times10^{-3}}{6{,}02\times10^{23}\times(564\times10^{-12})^3}\approx2{,}16\times10^3\ \mathrm{kg\,m^{-3}}$.

**4.** $r_+=\dfrac a2-r_-=282-181=101\ \mathrm{pm}$. Distance anion-anion la plus courte : $\dfrac{a\sqrt2}2=399\ \mathrm{pm}>2r_-=362\ \mathrm{pm}$ : pas de contact, l'empilement des anions n'est pas compact (la répulsion anion-anion est évitée). $r_+/r_-=0{,}56$, compris entre $\sqrt2-1=0{,}414$ (le cation doit être assez gros pour écarter les anions) et $\sqrt3-1=0{,}732$ (au-delà, la structure CsCl, de coordinence 8, est préférée) : cohérent.

**5.** $C=\dfrac{4\times\frac43\pi(r_+^3+r_-^3)}{a^3}=\dfrac{16{,}76\times(1{,}03\times10^6+5{,}93\times10^6)}{1{,}79\times10^8}\approx0{,}65$.
""", r"4 NaCl par maille ; coordinence [6,6] ; $\rho\approx2{,}16$ g/cm³ ; $r(\mathrm{Na^+})=101$ pm ; compacité ≈ 0,65.")

ex('n-c-daniell', K, 'Oxydoréduction', 1, 'Pile Daniell', 15, r"""
Une pile Daniell est formée d'une électrode de zinc plongeant dans une solution de sulfate de zinc à $1{,}0\ \mathrm{mol\,L^{-1}}$ et d'une électrode de cuivre dans une solution de sulfate de cuivre(II) à $0{,}10\ \mathrm{mol\,L^{-1}}$, reliées par un pont salin.

On donne : $E^\circ(\mathrm{Cu^{2+}/Cu})=0{,}34\ \mathrm V$, $E^\circ(\mathrm{Zn^{2+}/Zn})=-0{,}76\ \mathrm V$, $\frac{RT}F\ln10\approx0{,}06\ \mathrm V$, $F=96\,500\ \mathrm{C\,mol^{-1}}$, $M(\mathrm{Zn})=65{,}4\ \mathrm{g\,mol^{-1}}$.

1. Calculer le potentiel de chaque électrode. Identifier l'anode et la cathode et écrire la réaction de fonctionnement.
2. Calculer la force électromotrice de la pile et la constante d'équilibre de la réaction.
3. Rôle du pont salin ?
4. L'électrode de zinc pèse $10\ \mathrm g$ (le cuivre(II) est en excès). Quelle quantité d'électricité la pile peut-elle débiter au maximum ? L'exprimer en $\mathrm{A\,h}$.
""",
r"Nernst : $E=E^\circ+\dfrac{0{,}06}2\log[\mathrm{M^{2+}}]$ pour un couple $\mathrm{M^{2+}/M}$.",
r"Le pôle + (cathode, réduction) est l'électrode de plus haut potentiel. $\log K=\dfrac{2(E^\circ_1-E^\circ_2)}{0{,}06}$.",
r"Chaque atome de zinc oxydé libère 2 électrons : $Q=2n(\mathrm{Zn})F$.",
r"""
**1.** $E_{\mathrm{Cu}}=0{,}34+0{,}03\log0{,}10=0{,}31\ \mathrm V$ ; $E_{\mathrm{Zn}}=-0{,}76\ \mathrm V$. Le cuivre est le pôle + (cathode : $\mathrm{Cu^{2+}+2e^-\to Cu}$), le zinc le pôle − (anode : $\mathrm{Zn\to Zn^{2+}+2e^-}$). Réaction : $\mathrm{Zn+Cu^{2+}\to Zn^{2+}+Cu}$.

**2.** $e=E_+-E_-=1{,}07\ \mathrm V$. $\log K=\dfrac{2\times1{,}10}{0{,}06}\approx37$ : réaction quasi totale, la pile ne s'arrête qu'à l'épuisement d'un réactif.

**3.** Le pont salin ferme le circuit électrique en assurant la conduction par migration d'ions, et maintient l'électroneutralité de chaque compartiment, sans mélanger les solutions.

**4.** $n(\mathrm{Zn})=10/65{,}4=0{,}153$ mol, donc $Q=2nF\approx2{,}95\times10^4\ \mathrm C$, soit $Q/3600\approx8{,}2\ \mathrm{A\,h}$.
""", r"$E_+=0{,}31$ V (Cu), $E_-=-0{,}76$ V (Zn) ; $e=1{,}07$ V, $K\approx10^{37}$ ; $Q\approx8{,}2$ A·h.")

ex('n-c-permanganate', K, 'Oxydoréduction', 1, 'Dosage des ions fer(II) par le permanganate', 15, r"""
On dose $V_0=10{,}0\ \mathrm{mL}$ d'une solution d'ions $\mathrm{Fe^{2+}}$, acidifiée par de l'acide sulfurique, par une solution de permanganate de potassium à $c=2{,}00\times10^{-2}\ \mathrm{mol\,L^{-1}}$. L'équivalence est repérée pour $V_e=12{,}5\ \mathrm{mL}$.

On donne : $E^\circ(\mathrm{MnO_4^-/Mn^{2+}})=1{,}51\ \mathrm V$, $E^\circ(\mathrm{Fe^{3+}/Fe^{2+}})=0{,}77\ \mathrm V$.

1. Écrire les demi-équations, puis l'équation de la réaction de dosage. Calculer sa constante d'équilibre.
2. Comment repère-t-on l'équivalence sans indicateur ?
3. Calculer la concentration en ions $\mathrm{Fe^{2+}}$.
4. Quel est le potentiel de la solution à la demi-équivalence ?
""",
r"$\mathrm{MnO_4^-+8\,H^++5\,e^-\to Mn^{2+}+4\,H_2O}$ et $\mathrm{Fe^{2+}\to Fe^{3+}+e^-}$.",
r"$\log K=\dfrac{5(E^\circ_1-E^\circ_2)}{0{,}06}$ ; à l'équivalence, $n(\mathrm{Fe^{2+}})=5\,n(\mathrm{MnO_4^-})$.",
r"À la demi-équivalence, la moitié des ions fer(II) est oxydée : $[\mathrm{Fe^{3+}}]=[\mathrm{Fe^{2+}}]$.",
r"""
**1.** $\mathrm{MnO_4^-+8\,H^++5\,e^-\to Mn^{2+}+4\,H_2O}$ et $\mathrm{Fe^{2+}\to Fe^{3+}+e^-}$, d'où
$$\mathrm{MnO_4^-+5\,Fe^{2+}+8\,H^+\to Mn^{2+}+5\,Fe^{3+}+4\,H_2O},\qquad\log K=\frac{5(1{,}51-0{,}77)}{0{,}06}\approx62.$$
Réaction quasi totale et rapide : adaptée au dosage.

**2.** Avant l'équivalence, $\mathrm{MnO_4^-}$ (violet) est consommé et la solution reste pratiquement incolore. Après l'équivalence, il persiste : la première goutte en excès donne une teinte rose persistante. Le permanganate est son propre indicateur.

**3.** $n(\mathrm{Fe^{2+}})=5cV_e=5\times2{,}00\times10^{-2}\times12{,}5\times10^{-3}=1{,}25\times10^{-3}$ mol, d'où $[\mathrm{Fe^{2+}}]=0{,}125\ \mathrm{mol\,L^{-1}}$.

**4.** À la demi-équivalence, $[\mathrm{Fe^{3+}}]=[\mathrm{Fe^{2+}}]$ et, le permanganate étant entièrement consommé, le potentiel est fixé par le couple du fer : $E=E^\circ(\mathrm{Fe^{3+}/Fe^{2+}})=0{,}77\ \mathrm V$.
""", r"$\mathrm{MnO_4^-+5Fe^{2+}+8H^+\to Mn^{2+}+5Fe^{3+}+4H_2O}$, $K\approx10^{62}$ ; $[\mathrm{Fe^{2+}}]=0{,}125$ mol/L ; $E=0{,}77$ V.")

ex('n-c-conducti', K, 'Acide-base', 1, 'Titrage conductimétrique', 15, r"""
On titre $V_a=100\ \mathrm{mL}$ d'acide chlorhydrique à $c_a=1{,}0\times10^{-2}\ \mathrm{mol\,L^{-1}}$ par une solution concentrée d'hydroxyde de sodium (la dilution est négligeable). On suit la conductivité $\sigma$ de la solution.

On donne les conductivités molaires ioniques, en $\mathrm{mS\,m^2\,mol^{-1}}$ : $\lambda(\mathrm{H_3O^+})=35{,}0$ ; $\lambda(\mathrm{HO^-})=19{,}8$ ; $\lambda(\mathrm{Na^+})=5{,}0$ ; $\lambda(\mathrm{Cl^-})=7{,}6$.

1. Rappeler la loi de Kohlrausch. Calculer la conductivité initiale.
2. Écrire la réaction de titrage. Justifier qualitativement l'allure de la courbe $\sigma=f(V)$ avant et après l'équivalence.
3. Calculer la conductivité à l'équivalence.
4. Pourquoi l'ion oxonium a-t-il une conductivité molaire si élevée ?
""",
r"$\sigma=\sum_i\lambda_ic_i$, avec les concentrations en $\mathrm{mol\,m^{-3}}$.",
r"Avant l'équivalence, chaque $\mathrm{H_3O^+}$ consommé est remplacé par un $\mathrm{Na^+}$ ; après, on ajoute $\mathrm{Na^+}$ et $\mathrm{HO^-}$.",
r"À l'équivalence, il ne reste que $\mathrm{Na^+}$ et $\mathrm{Cl^-}$ à $10\ \mathrm{mol\,m^{-3}}$ chacun.",
r"""
**1.** Kohlrausch : $\sigma=\sum_i\lambda_ic_i$. Initialement, $[\mathrm{H_3O^+}]=[\mathrm{Cl^-}]=10\ \mathrm{mol\,m^{-3}}$ : $\sigma_0=10\times(35{,}0+7{,}6)\times10^{-3}=0{,}426\ \mathrm{S\,m^{-1}}$.

**2.** $\mathrm{H_3O^++HO^-\to2\,H_2O}$. Avant l'équivalence : on remplace $\mathrm{H_3O^+}$ ($\lambda=35{,}0$) par $\mathrm{Na^+}$ ($\lambda=5{,}0$) : $\sigma$ **décroît** linéairement (pente $\propto5{,}0-35{,}0$). Après : on ajoute $\mathrm{Na^+}$ et $\mathrm{HO^-}$ : $\sigma$ **croît** linéairement (pente $\propto5{,}0+19{,}8$). L'équivalence est au point anguleux, à l'intersection de deux droites.

**3.** $\sigma_{eq}=10\times(5{,}0+7{,}6)\times10^{-3}=0{,}126\ \mathrm{S\,m^{-1}}$.

**4.** $\mathrm{H_3O^+}$ ne se déplace pas seulement par migration : un proton passe d'une molécule d'eau à la voisine par réarrangement des liaisons hydrogène (mécanisme de Grotthuss). La charge se propage sans déplacement global de matière, beaucoup plus vite. Même chose pour $\mathrm{HO^-}$.
""", r"$\sigma_0=0{,}426$ S/m ; décroissance puis croissance linéaires ; $\sigma_{eq}=0{,}126$ S/m.")

ex('n-c-epH', K, 'Oxydoréduction', 2, 'Diagramme potentiel-pH du fer', 25, r"""
On trace le diagramme potentiel-pH simplifié du fer, pour les espèces $\mathrm{Fe(s)}$, $\mathrm{Fe^{2+}}$, $\mathrm{Fe^{3+}}$, $\mathrm{Fe(OH)_2(s)}$ et $\mathrm{Fe(OH)_3(s)}$, avec une concentration de tracé $c=1{,}0\times10^{-2}\ \mathrm{mol\,L^{-1}}$ pour chaque espèce dissoute.

On donne : $E^\circ(\mathrm{Fe^{3+}/Fe^{2+}})=0{,}77\ \mathrm V$, $E^\circ(\mathrm{Fe^{2+}/Fe})=-0{,}44\ \mathrm V$, $\mathrm pK_s(\mathrm{Fe(OH)_3})=38$, $\mathrm pK_s(\mathrm{Fe(OH)_2})=15$, $\mathrm pK_e=14$, $\frac{RT}F\ln10\approx0{,}06\ \mathrm V$.

1. Déterminer les pH d'apparition des précipités $\mathrm{Fe(OH)_3}$ et $\mathrm{Fe(OH)_2}$.
2. Établir les équations des frontières $\mathrm{Fe^{3+}/Fe^{2+}}$, $\mathrm{Fe(OH)_3/Fe^{2+}}$ et $\mathrm{Fe(OH)_3/Fe(OH)_2}$. Vérifier la continuité aux points anguleux.
3. Établir la frontière $\mathrm{Fe^{2+}/Fe}$.
4. Superposer le diagramme de l'eau ($E=1{,}23-0{,}06\,\mathrm{pH}$ et $E=-0{,}06\,\mathrm{pH}$). Le fer est-il stable dans l'eau ? Que se passe-t-il en présence de dioxygène dissous ?
""",
r"Apparition de $\mathrm{Fe(OH)_3}$ : $[\mathrm{Fe^{3+}}][\mathrm{HO^-}]^3=K_s$ avec $[\mathrm{Fe^{3+}}]=c$.",
r"Pour $\mathrm{Fe(OH)_3/Fe^{2+}}$, exprime $[\mathrm{Fe^{3+}}]=K_s/[\mathrm{HO^-}]^3$ dans la formule de Nernst du couple $\mathrm{Fe^{3+}/Fe^{2+}}$.",
r"Le domaine du fer métallique est disjoint de celui de l'eau : le fer est oxydé par l'eau (lentement) et surtout par $\mathrm{O_2}$.",
r"""
**1.** $\mathrm{Fe(OH)_3}$ : $[\mathrm{HO^-}]^3=10^{-38}/10^{-2}=10^{-36}$, d'où $[\mathrm{HO^-}]=10^{-12}$ et $\mathrm{pH}=2{,}0$. $\mathrm{Fe(OH)_2}$ : $[\mathrm{HO^-}]^2=10^{-15}/10^{-2}=10^{-13}$, d'où $\mathrm{pH}=7{,}5$.

**2.**
- $\mathrm{Fe^{3+}/Fe^{2+}}$ (pH < 2) : $E=0{,}77+0{,}06\log\frac{[\mathrm{Fe^{3+}}]}{[\mathrm{Fe^{2+}}]}=0{,}77\ \mathrm V$ (horizontale).
- $\mathrm{Fe(OH)_3/Fe^{2+}}$ ($2<\mathrm{pH}<7{,}5$) : $[\mathrm{Fe^{3+}}]=\dfrac{K_s}{[\mathrm{HO^-}]^3}=10^{-38}\times10^{3(14-\mathrm{pH})}=10^{4-3\mathrm{pH}}$, d'où $E=0{,}77+0{,}06(4-3\,\mathrm{pH}+2)=1{,}13-0{,}18\,\mathrm{pH}$. En pH 2 : $0{,}77$ V ✓.
- $\mathrm{Fe(OH)_3/Fe(OH)_2}$ (pH > 7,5) : $[\mathrm{Fe^{2+}}]=10^{-15}\times10^{2(14-\mathrm{pH})}=10^{13-2\mathrm{pH}}$, d'où $E=0{,}77+0{,}06(4-3\,\mathrm{pH}-13+2\,\mathrm{pH})=0{,}23-0{,}06\,\mathrm{pH}$. En pH 7,5 : $-0{,}22$ V des deux côtés ✓.

**3.** $\mathrm{Fe^{2+}/Fe}$ : $E=-0{,}44+0{,}03\log10^{-2}=-0{,}50\ \mathrm V$ pour pH < 7,5 (puis $\mathrm{Fe(OH)_2/Fe}$, de pente $-0{,}06$).

**4.** Le domaine de Fe est entièrement sous la droite $E=-0{,}06\,\mathrm{pH}$ du couple $\mathrm{H_2O/H_2}$ : le fer est thermodynamiquement oxydé par l'eau (en $\mathrm{Fe^{2+}}$ avec dégagement de $\mathrm{H_2}$, en milieu acide surtout ; la réaction est lente en milieu neutre). En présence de $\mathrm{O_2}$, l'oxydation va jusqu'au fer(III) : formation de $\mathrm{Fe(OH)_3}$, la rouille. C'est la corrosion du fer.
""", r"Précipités à pH 2,0 et 7,5 ; frontières $E=0{,}77$, $E=1{,}13-0{,}18\,\mathrm{pH}$, $E=0{,}23-0{,}06\,\mathrm{pH}$, $E=-0{,}50$ V ; le fer est corrodé.")

ex('n-c-flamme', K, 'Thermochimie', 2, 'Température de flamme du méthane', 20, r"""
On brûle du méthane dans la quantité d'air stœchiométrique (air : $\frac15$ de $\mathrm{O_2}$, $\frac45$ de $\mathrm{N_2}$), sous $1$ bar. Les réactifs sont initialement à $298$ K ; l'eau formée est gazeuse.

On donne les enthalpies standard de formation à $298$ K ($\mathrm{kJ\,mol^{-1}}$) : $\mathrm{CH_4(g)}$ : $-74{,}8$ ; $\mathrm{CO_2(g)}$ : $-393{,}5$ ; $\mathrm{H_2O(g)}$ : $-241{,}8$. Capacités thermiques molaires (supposées constantes, $\mathrm{J\,K^{-1}\,mol^{-1}}$) : $\mathrm{CO_2}$ : 37 ; $\mathrm{H_2O(g)}$ : 34 ; $\mathrm{N_2}$ : 29.

1. Écrire l'équation de combustion et calculer l'enthalpie standard de réaction.
2. Faire l'inventaire des espèces en fin de réaction pour une mole de méthane.
3. La combustion est rapide et supposée adiabatique. Calculer la température de flamme.
4. La température mesurée est d'environ $2\,200$ K. Proposer deux explications.
""",
r"$\mathrm{CH_4+2\,O_2\to CO_2+2\,H_2O}$ ; loi de Hess : $\Delta_rH^\circ=\sum\nu_i\Delta_fH^\circ_i$.",
r"Deux moles de $\mathrm{O_2}$ s'accompagnent de 8 moles de $\mathrm{N_2}$, qui ne réagissent pas mais doivent être chauffées.",
r"Chemin fictif : réaction à 298 K, puis échauffement des produits ; $\Delta H=0$ donne $\Delta_rH^\circ+\left(\sum C_p\right)(T_f-298)=0$.",
r"""
**1.** $\mathrm{CH_4+2\,O_2\to CO_2+2\,H_2O}$ : $\Delta_rH^\circ=-393{,}5+2\times(-241{,}8)-(-74{,}8)=-802{,}3\ \mathrm{kJ\,mol^{-1}}$.

**2.** Pour 1 mol de $\mathrm{CH_4}$ : 1 mol de $\mathrm{CO_2}$, 2 mol de $\mathrm{H_2O}$ et 8 mol de $\mathrm{N_2}$ (spectateur).

**3.** La transformation est isobare et adiabatique : $\Delta H=0$. Chemin fictif : réaction totale à 298 K, puis échauffement des produits : $\Delta_rH^\circ+(37+2\times34+8\times29)(T_f-298)=0$. Avec $\sum C_p=337\ \mathrm{J\,K^{-1}}$ : $T_f=298+\dfrac{802\,300}{337}\approx2\,680\ \mathrm K$.

**4.** La combustion n'est pas parfaitement adiabatique (pertes par rayonnement) ; à haute température, les produits se dissocient partiellement ($\mathrm{CO_2\to CO+\tfrac12O_2}$, $\mathrm{H_2O\to H+OH}$…), réactions endothermiques. Enfin, les $C_p$ augmentent avec $T$. Remarque : sans l'azote de l'air (combustion dans $\mathrm{O_2}$ pur), $\sum C_p=105$ et la flamme serait bien plus chaude, d'où l'usage du chalumeau oxy-gaz.
""", r"$\Delta_rH^\circ=-802$ kJ/mol ; produits : 1 CO₂, 2 H₂O, 8 N₂ ; $T_f\approx2\,680$ K.")

ex('n-c-ellingham', K, 'Thermochimie', 2, 'Élaboration du zinc : diagramme d’Ellingham', 20, r"""
On considère, dans l'approximation d'Ellingham, les deux couples suivants (réactions écrites pour une mole de $\mathrm{O_2}$, $T$ en kelvins) :
- $\mathrm{2\,C(s)+O_2(g)\to2\,CO(g)}$ : $\Delta_rG^\circ_1=-221-0{,}179\,T\ \ (\mathrm{kJ\,mol^{-1}})$ ;
- $\mathrm{2\,Zn+O_2(g)\to2\,ZnO(s)}$ : $\Delta_rG^\circ_2=-696+0{,}201\,T\ \ (\mathrm{kJ\,mol^{-1}})$, valable tant que le zinc est condensé.

1. Interpréter les signes des pentes à l'aide de l'entropie standard de réaction.
2. Écrire la réduction de l'oxyde de zinc par le carbone et exprimer $\Delta_rG^\circ(T)$. À partir de quelle température est-elle thermodynamiquement favorable ?
3. Le zinc bout à $1\,180$ K sous $1$ bar. Comment évolue la pente de $\Delta_rG^\circ_2$ au-delà ? Quelle conséquence sur la température d'inversion ?
4. Pourquoi récupère-t-on le zinc à l'état de vapeur dans le haut-fourneau, et que faut-il faire pour l'obtenir solide ?
""",
r"La pente de $\Delta_rG^\circ(T)$ vaut $-\Delta_rS^\circ$ ; elle est dominée par la variation du nombre de moles de gaz.",
r"$\mathrm{2\,ZnO+2\,C\to2\,Zn+2\,CO}$ : $\Delta_rG^\circ=\Delta_rG^\circ_1-\Delta_rG^\circ_2$.",
r"Au-delà de l'ébullition, le zinc gazeux est un réactif gazeux de la réaction 2 : $\Delta_rS^\circ_2$ devient plus négatif et la pente augmente.",
r"""
**1.** $\Delta_rG^\circ=\Delta_rH^\circ-T\Delta_rS^\circ$ : la pente vaut $-\Delta_rS^\circ$. Réaction 1 : $\Delta n_g=+1$, $\Delta_rS^\circ>0$, pente négative ($-0{,}179$). Réaction 2 : $\Delta n_g=-1$, $\Delta_rS^\circ<0$, pente positive ($+0{,}201$).

**2.** $\mathrm{2\,ZnO+2\,C\to2\,Zn+2\,CO}$, $\Delta_rG^\circ=\Delta_rG^\circ_1-\Delta_rG^\circ_2=475-0{,}380\,T$. Favorable ($\Delta_rG^\circ<0$) pour $T>1\,250$ K : au-delà, la droite du carbone passe sous celle du zinc.

**3.** Au-delà de $1\,180$ K, le zinc est gazeux : la réaction 2 consomme 3 moles de gaz au lieu d'une, $\Delta_rS^\circ_2$ diminue fortement et la pente de $\Delta_rG^\circ_2$ augmente (point anguleux). Les droites se coupent donc à une température plus basse que $1\,250$ K, mais supérieure à $1\,180$ K (vers $1\,200$ K).

**4.** À la température de réduction, le zinc est produit à l'état gazeux et quitte le four avec CO. Il faut le condenser rapidement (pluie de plomb liquide) pour éviter qu'il soit réoxydé par $\mathrm{CO_2}$ en se refroidissant (la réaction inverse redevient favorable à basse température).
""", r"Pentes $-\Delta_rS^\circ$ ; $\Delta_rG^\circ=475-0{,}380\,T$, favorable au-delà de ≈ 1 250 K ; inversion abaissée vers 1 200 K quand Zn est gazeux.")

ex('n-c-electrolyse', K, 'Électrochimie', 2, 'Électrolyse de l’eau et coût de l’hydrogène', 20, r"""
On produit du dihydrogène par électrolyse de l'eau en milieu basique, entre deux électrodes de nickel.

On donne : $E^\circ(\mathrm{O_2/H_2O})=1{,}23\ \mathrm V$, $E^\circ(\mathrm{H_2O/H_2})=0\ \mathrm V$, $F=96\,500\ \mathrm{C\,mol^{-1}}$, $M(\mathrm{H_2})=2{,}0\ \mathrm{g\,mol^{-1}}$, enthalpie de combustion de $\mathrm{H_2}$ (eau liquide) : $286\ \mathrm{kJ\,mol^{-1}}$.

1. Écrire les réactions aux électrodes (en milieu basique) et le bilan. Identifier anode et cathode.
2. Quelle est la tension minimale théorique à appliquer ? Expliquer pourquoi la tension réelle vaut environ $1{,}8$ V, à l'aide de l'allure des courbes intensité-potentiel.
3. Calculer l'énergie électrique nécessaire pour produire $1$ kg de $\mathrm{H_2}$ sous $1{,}8$ V, en kWh.
4. Calculer le rendement énergétique de la filière (énergie récupérable par combustion de l'hydrogène / énergie électrique).
""",
r"Cathode (réduction) : $\mathrm{2\,H_2O+2e^-\to H_2+2\,HO^-}$ ; anode (oxydation) : $\mathrm{4\,HO^-\to O_2+2\,H_2O+4e^-}$.",
r"La différence de potentiel thermodynamique est $1{,}23$ V, indépendante du pH ; s'y ajoutent les surtensions anodique et cathodique et la chute ohmique $RI$.",
r"Une mole de $\mathrm{H_2}$ demande $2F$ ; énergie $W=2FU$ par mole, puis 500 mol par kg.",
r"""
**1.** Cathode (réduction, pôle −) : $\mathrm{2\,H_2O+2e^-\to H_2+2\,HO^-}$. Anode (oxydation, pôle +) : $\mathrm{4\,HO^-\to O_2+2\,H_2O+4e^-}$. Bilan : $\mathrm{2\,H_2O\to2\,H_2+O_2}$.

**2.** Il faut au minimum $U=E(\mathrm{O_2/H_2O})-E(\mathrm{H_2O/H_2})=1{,}23\ \mathrm V$ (les deux potentiels varient de $-0{,}06\,\mathrm{pH}$ : l'écart ne dépend pas du pH). Les couples de l'eau sont lents : les courbes intensité-potentiel ne décollent qu'avec des **surtensions** (anodique $\eta_a>0$, cathodique $\eta_c<0$), croissantes avec le courant. S'y ajoute la chute ohmique dans l'électrolyte : $U=1{,}23+\eta_a-\eta_c+RI\approx1{,}8$ V en fonctionnement.

**3.** Par mole de $\mathrm{H_2}$ : $W=2FU=2\times96\,500\times1{,}8\approx3{,}5\times10^5\ \mathrm J$. Pour 1 kg (500 mol) : $1{,}7\times10^8$ J, soit $\approx48\ \mathrm{kWh}$.

**4.** La combustion de 1 kg restitue $500\times286\ \mathrm{kJ}=1{,}43\times10^8\ \mathrm J\approx40\ \mathrm{kWh}$. Rendement : $40/48\approx0{,}82$ pour l'électrolyse seule. La reconversion en électricité (pile à combustible, rendement $\sim50\ \%$) ramène le rendement global à environ $40\ \%$.
""", r"$U_{\min}=1{,}23$ V ; ≈ 48 kWh/kg de H₂ sous 1,8 V ; rendement de l'électrolyse ≈ 82 %.")

ex('n-c-aeqs', K, 'Cinétique', 2, 'Mécanisme avec pré-équilibre et énergie d’activation négative', 25, r"""
On propose pour la réaction $\mathrm{2\,NO+O_2\to2\,NO_2}$ le mécanisme suivant :
- $\mathrm{2\,NO\rightleftharpoons N_2O_2}$ : équilibre rapide, de constante $K$ (constantes de vitesse $k_1$ et $k_{-1}$) ;
- $\mathrm{N_2O_2+O_2\to2\,NO_2}$ : étape lente, de constante $k_2$.

1. Exprimer la vitesse de formation de $\mathrm{NO_2}$ en utilisant l'hypothèse de pré-équilibre rapide. Retrouver la loi de vitesse expérimentale $v=k[\mathrm{NO}]^2[\mathrm{O_2}]$.
2. Retrouver ce résultat par l'approximation des états quasi stationnaires appliquée à $\mathrm{N_2O_2}$, en précisant la condition sur les constantes.
3. Expérimentalement, la vitesse de cette réaction diminue quand la température augmente. Montrer que le mécanisme l'explique si la première étape est exothermique.
""",
r"Pré-équilibre : $[\mathrm{N_2O_2}]=K[\mathrm{NO}]^2$, puis $v=\frac12\frac{\mathrm d[\mathrm{NO_2}]}{\mathrm dt}=k_2[\mathrm{N_2O_2}][\mathrm{O_2}]$.",
r"AEQS : $\frac{\mathrm d[\mathrm{N_2O_2}]}{\mathrm dt}=k_1[\mathrm{NO}]^2-k_{-1}[\mathrm{N_2O_2}]-k_2[\mathrm{N_2O_2}][\mathrm{O_2}]\approx0$, puis $k_{-1}\gg k_2[\mathrm{O_2}]$.",
r"$k=k_2K$ : $E_{a,\text{app}}=E_{a,2}+\Delta_rH^\circ_1$ (Van't Hoff pour $K$). Elle est négative si $\Delta_rH^\circ_1<-E_{a,2}$.",
r"""
**1.** L'étape lente impose la vitesse : $v=k_2[\mathrm{N_2O_2}][\mathrm{O_2}]$. Le pré-équilibre rapide donne $[\mathrm{N_2O_2}]=K[\mathrm{NO}]^2$, donc $v=k_2K[\mathrm{NO}]^2[\mathrm{O_2}]$ : $k=k_2K$.

**2.** AEQS : $k_1[\mathrm{NO}]^2=(k_{-1}+k_2[\mathrm{O_2}])[\mathrm{N_2O_2}]$, d'où $v=\dfrac{k_1k_2[\mathrm{NO}]^2[\mathrm{O_2}]}{k_{-1}+k_2[\mathrm{O_2}]}$. Si $k_{-1}\gg k_2[\mathrm{O_2}]$ (l'intermédiaire revient en arrière bien plus souvent qu'il ne réagit), $v\approx\dfrac{k_1}{k_{-1}}k_2[\mathrm{NO}]^2[\mathrm{O_2}]$ avec $K=k_1/k_{-1}$ : même résultat.

**3.** $\dfrac{\mathrm d\ln k}{\mathrm dT}=\dfrac{\mathrm d\ln k_2}{\mathrm dT}+\dfrac{\mathrm d\ln K}{\mathrm dT}=\dfrac{E_{a,2}+\Delta_rH^\circ_1}{RT^2}$ (Arrhenius et Van't Hoff). L'énergie d'activation apparente $E_{a,2}+\Delta_rH^\circ_1$ est négative si la dimérisation est suffisamment exothermique : quand $T$ augmente, le pré-équilibre est déplacé vers $\mathrm{NO}$ et la concentration de l'intermédiaire chute plus vite que $k_2$ n'augmente. La vitesse diminue.
""", r"$v=k_2K[\mathrm{NO}]^2[\mathrm{O_2}]$ ; AEQS si $k_{-1}\gg k_2[\mathrm{O_2}]$ ; $E_{a,\text{app}}=E_{a,2}+\Delta_rH^\circ_1<0$.")
