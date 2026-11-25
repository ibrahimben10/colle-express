# Physique (suite) — planches d'oral CCINP, préparation aux oraux (type CCS/CCMP/X), rapport Centrale-Supélec 2025.
from newlib import ex, E

def src(texte, concours):
    E[-1]['enonce'] += '\n\n*' + texte + '*'
    E[-1]['concours'] = concours
    E[-1]['ajout'] = '2026-11-25'

P = 'Physique'
CCINP = "D'après une planche d'oral CCINP (MP)."
PREP = "D'après un exercice de préparation aux oraux MP (type {})."
CENTRALE = "Thème signalé par le rapport du jury Centrale-Supélec 2025 (épreuve orale de physique-chimie) : {}."

# ------------------------------------------------------------------ 10. Deux OPPH symétriques
ex('n-pc-deuxopph', P, 'Ondes électromagnétiques', 2, 'Deux ondes planes symétriques : une onde guidée', 30, r"""
Dans le vide, on superpose les deux ondes $\underline{\vec B}_1=B_0\,e^{i(\omega t-\vec k_1\cdot\vec r)}\vec e_z$ et $\underline{\vec B}_2=B_0\,e^{i(\omega t-\vec k_2\cdot\vec r)}\vec e_z$, avec $\|\vec k_1\|=\|\vec k_2\|=k_0=\frac\omega c=\frac{2\pi}{\lambda_0}$, les vecteurs $\vec k_1$ et $\vec k_2$ étant dans le plan $(Oxy)$ et faisant les angles $+\alpha$ et $-\alpha$ avec $\vec e_x$.

1. Déterminer le champ magnétique résultant. Caractériser l'onde obtenue : direction de propagation, vitesse de phase, longueur d'onde selon $Ox$, amplitude. Est-ce une onde plane ?
2. Calculer le champ électrique associé (en réel).
3. Calculer la moyenne temporelle du vecteur de Poynting, puis la vitesse de propagation de l'énergie. Comparer à la vitesse de phase et commenter.
""", r"""Écris $\vec k_{1,2}=k_0(\cos\alpha,\pm\sin\alpha,0)$ et factorise $e^{i(\omega t-k_0x\cos\alpha)}$.""",
r"""Maxwell-Ampère dans le vide : $\frac{\partial\vec E}{\partial t}=c^2\,\overrightarrow{\mathrm{rot}}\,\vec B$, soit en complexe $\underline{\vec E}=\frac{c^2}{i\omega}\overrightarrow{\mathrm{rot}}\,\underline{\vec B}$.""",
r"""Les grandeurs énergétiques se calculent en réel. Pour la vitesse de l'énergie, divise la puissance moyenne traversant une section par l'énergie moyenne par unité de longueur (moyennes sur $y$ aussi).""",
r"""**Étape 1 — Analyse de l'énoncé.** La superposition de deux ondes planes symétriques donne une onde qui progresse selon $Ox$ et qui est stationnaire selon $Oy$ : c'est la structure du champ dans un guide d'ondes.

**Étape 2 — Rappels du cours.**

> **Équation — Maxwell-Ampère dans le vide.** $\overrightarrow{\mathrm{rot}}\,\vec B=\frac1{c^2}\frac{\partial\vec E}{\partial t}$.

> **Définition — Vecteur de Poynting.** $\vec\Pi=\frac{\vec E\wedge\vec B}{\mu_0}$ ; densité d'énergie $u=\frac{\varepsilon_0E^2}2+\frac{B^2}{2\mu_0}$. Ces grandeurs sont quadratiques : on repasse en réel avant de les calculer (rappel du rapport Centrale 2025).

**Étape 3 — Stratégie.** Somme des complexes, rotationnel, puis moyennes temporelles et spatiales.

**Étape 4 — Résolution détaillée.**

**4.1 Champ résultant.** $\vec k_{1,2}\cdot\vec r=k_0(x\cos\alpha\pm y\sin\alpha)$, donc
$$\underline{\vec B}=2B_0\cos(k_0y\sin\alpha)\,e^{i(\omega t-k_0x\cos\alpha)}\,\vec e_z.$$
Propagation selon $+\vec e_x$ avec $k_x=k_0\cos\alpha$ : vitesse de phase $v_\varphi=\frac c{\cos\alpha}>c$, longueur d'onde selon $Ox$ : $\lambda_x=\frac{\lambda_0}{\cos\alpha}$. L'amplitude $2B_0|\cos(k_0y\sin\alpha)|$ dépend de $y$ (nœuds en $k_0y\sin\alpha=\frac\pi2+p\pi$) : l'onde n'est pas plane, c'est une onde progressive selon $x$ et stationnaire selon $y$.

**4.2 Champ électrique.** $\overrightarrow{\mathrm{rot}}(\underline B\vec e_z)=(\partial_y\underline B,-\partial_x\underline B,0)$ et $\underline{\vec E}=\frac{c^2}{i\omega}\overrightarrow{\mathrm{rot}}\,\underline{\vec B}$. Avec $c^2k_0/\omega=c$, en réel, en notant $\phi=\omega t-k_0x\cos\alpha$ :
$$E_x=-2cB_0\sin\alpha\,\sin(k_0y\sin\alpha)\sin\phi,\qquad E_y=2cB_0\cos\alpha\,\cos(k_0y\sin\alpha)\cos\phi,$$
et $B_z=2B_0\cos(k_0y\sin\alpha)\cos\phi$. $\vec E$ a une composante selon la direction de propagation : ce n'est pas la structure d'une onde plane.

**4.3 Énergie.** $\Pi_x=\frac{E_yB_z}{\mu_0}$ et $\Pi_y=-\frac{E_xB_z}{\mu_0}$. En moyenne temporelle, $\langle\sin\phi\cos\phi\rangle=0$ donc $\langle\Pi_y\rangle=0$, et
$$\langle\Pi_x\rangle=\frac{2cB_0^2\cos\alpha}{\mu_0}\cos^2(k_0y\sin\alpha).$$
En moyennant aussi sur $y$ : $\overline{\langle\Pi_x\rangle}=\frac{cB_0^2\cos\alpha}{\mu_0}$ et $\overline{\langle u\rangle}=\frac{B_0^2}{2\mu_0}+\frac{B_0^2}{2\mu_0}=\frac{B_0^2}{\mu_0}$. La vitesse de l'énergie vaut $v_e=\frac{\overline{\langle\Pi_x\rangle}}{\overline{\langle u\rangle}}=c\cos\alpha<c$.

**Étape 5 — Vérification.**

> **Vérification — Interprétation.** $v_\varphi v_e=c^2$. Chaque onde plane transporte l'énergie à $c$ dans sa propre direction, qui fait l'angle $\alpha$ avec $Ox$ : la projection donne $c\cos\alpha$. Pour $\alpha=0$, on retrouve une onde plane avec $v_\varphi=v_e=c$.

**Étape 6 — Conclusion.**
$$\boxed{\underline{\vec B}=2B_0\cos(k_0y\sin\alpha)e^{i(\omega t-k_0x\cos\alpha)}\vec e_z,\quad v_\varphi=\tfrac c{\cos\alpha},\quad v_e=c\cos\alpha,\quad v_\varphi v_e=c^2}$$""",
r"""$\underline B=2B_0\cos(k_0y\sin\alpha)e^{i(\omega t-k_0x\cos\alpha)}$ : progressive selon $x$ ($v_\varphi=c/\cos\alpha$, $\lambda_x=\lambda_0/\cos\alpha$), stationnaire selon $y$ ; $E_x$, $E_y$ par Maxwell-Ampère ; $\langle\Pi_y\rangle=0$, vitesse de l'énergie $c\cos\alpha$.""")
src(CCINP, 'CCINP')

# ------------------------------------------------------------------ 11. Spire sur l'axe
ex('n-pc-spire', P, 'Magnétostatique', 1, 'Champ d’une spire sur son axe', 15, r"""
Une spire circulaire de centre $O$, de rayon $R$, d'axe $(Ox)$, est parcourue par un courant $I$. On repère un point $M$ de l'axe par son abscisse $x$.

1. Par des arguments de symétrie, déterminer la direction de $\vec B(M)$.
2. À l'aide de la loi de Biot et Savart, exprimer $B(x)$ sous forme d'intégrale, puis la calculer.
3. Donner les expressions approchées pour $x\ll R$ et pour $x\gg R$. Commenter le second résultat à l'aide du moment magnétique de la spire.
""", r"""Tout plan contenant l'axe est un plan d'antisymétrie de la distribution de courants.""",
r"""Seule la composante axiale de $\mathrm d\vec B$ subsiste ; elle vaut $\mathrm dB\cdot\frac R{\sqrt{R^2+x^2}}$.""",
r"""Pour $x\gg R$, compare au champ d'un dipôle magnétique de moment $m=I\pi R^2$ sur son axe : $\frac{\mu_0m}{2\pi x^3}$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Calcul classique par Biot et Savart, simplifié par la symétrie : toutes les contributions ont la même norme et la même composante axiale.

**Étape 2 — Rappels du cours.**

> **Loi — Biot et Savart.** $\mathrm d\vec B(M)=\frac{\mu_0}{4\pi}\frac{I\,\mathrm d\vec\ell\wedge\overrightarrow{PM}}{PM^3}$.

> **Propriété — Symétries.** $\vec B$ appartient aux plans d'antisymétrie des courants et est orthogonal à leurs plans de symétrie.

**Étape 3 — Stratégie.** Direction par symétrie, puis somme des composantes axiales.

**Étape 4 — Résolution détaillée.**

**4.1 Direction.** Tout plan contenant $(Ox)$ est un plan d'antisymétrie : $\vec B(M)$ appartient à tous ces plans, donc à leur intersection : $\vec B=B(x)\vec e_x$.

**4.2 Calcul.** Pour $P$ sur la spire, $PM=\sqrt{R^2+x^2}$ et $\mathrm d\vec\ell\perp\overrightarrow{PM}$, d'où $\|\mathrm d\vec B\|=\frac{\mu_0I\,\mathrm d\ell}{4\pi(R^2+x^2)}$ ; sa composante axiale est multipliée par $\sin\psi=\frac R{\sqrt{R^2+x^2}}$. Donc
$$B(x)=\oint\frac{\mu_0I R\,\mathrm d\ell}{4\pi(R^2+x^2)^{3/2}}=\frac{\mu_0IR^2}{2(R^2+x^2)^{3/2}}.$$

**4.3 Limites.** Pour $x\ll R$ : $B\approx\frac{\mu_0I}{2R}$, le champ au centre. Pour $x\gg R$ : $B\approx\frac{\mu_0IR^2}{2|x|^3}=\frac{\mu_0m}{2\pi|x|^3}$ avec $m=I\pi R^2$ : c'est le champ d'un dipôle magnétique sur son axe, qui décroît en $1/x^3$.

**Étape 5 — Vérification.**

> **Vérification — Ordre de grandeur.** Pour $I=1\ \mathrm A$ et $R=5\ \mathrm{cm}$ : $B(0)=\frac{4\pi\times10^{-7}}{0{,}1}\approx1{,}3\times10^{-5}\ \mathrm T$, du même ordre que le champ terrestre.

**Étape 6 — Conclusion.**
$$\boxed{\vec B=\frac{\mu_0IR^2}{2(R^2+x^2)^{3/2}}\vec e_x;\quad B(0)=\frac{\mu_0I}{2R};\quad B\underset{x\gg R}\sim\frac{\mu_0m}{2\pi|x|^3},\ m=I\pi R^2}$$""",
r"""Par symétrie $\vec B=B\vec e_x$ ; Biot et Savart : $B=\frac{\mu_0IR^2}{2(R^2+x^2)^{3/2}}$ ; $\frac{\mu_0I}{2R}$ au centre ; champ dipolaire $\frac{\mu_0m}{2\pi x^3}$ loin, avec $m=I\pi R^2$.""")
src(CCINP, 'CCINP')

# ------------------------------------------------------------------ 12. Trois fils au carré
ex('n-pc-troisfils', P, 'Magnétostatique', 1, 'Trois fils aux sommets d’un carré', 15, r"""
Dans un plan $\Pi$, on considère un carré $PQRS$ de côté $a$ (sommets dans cet ordre). Trois fils rectilignes infinis, perpendiculaires à $\Pi$, passent par $P$, $S$ et $Q$ et sont parcourus par des courants $I_1$, $I_2$, $I_3$ (comptés positivement dans le même sens, vers l'avant de $\Pi$).

1. Rappeler le champ créé par un fil infini.
2. Trouver une relation entre $I_1$, $I_2$, $I_3$ pour que le champ magnétique soit nul au quatrième sommet $R$.
3. On ajoute en $R$ un quatrième fil parcouru par $I'$. Quelle force par unité de longueur subit-il ?
""", r"""Le champ d'un fil est orthoradial, de norme $\frac{\mu_0I}{2\pi r}$.""",
r"""Place le carré dans un repère : $P(0,0)$, $Q(0,a)$, $R(a,a)$, $S(a,0)$, et calcule chaque contribution en $R$.""",
r"""La force de Laplace par unité de longueur sur le fil en $R$ vaut $I'\vec e_z\wedge\vec B(R)$, où $\vec B(R)$ est le champ des autres fils.""",
r"""**Étape 1 — Analyse de l'énoncé.** Superposition de trois champs orthoradiaux ; on annule les deux composantes du champ total en $R$, puis on en tire la force.

**Étape 2 — Rappels du cours.**

> **Formule — Fil infini.** $\vec B=\frac{\mu_0I}{2\pi r}\vec e_\theta$, avec $\vec e_\theta=\vec e_z\wedge\vec e_r$.

> **Loi — Force de Laplace.** $\mathrm d\vec F=I\,\mathrm d\vec\ell\wedge\vec B$.

**Étape 3 — Stratégie.** Coordonnées, contributions en $R$, deux équations.

**Étape 4 — Résolution détaillée.**

**4.1 Contributions.** Fil en $Q$ : $\vec e_r=\vec e_x$, $r=a$ : $\vec B_Q=\frac{\mu_0I_3}{2\pi a}\vec e_y$. Fil en $S$ : $\vec e_r=\vec e_y$, $r=a$ : $\vec B_S=-\frac{\mu_0I_2}{2\pi a}\vec e_x$. Fil en $P$ : $\vec e_r=\frac{\vec e_x+\vec e_y}{\sqrt2}$, $r=a\sqrt2$, $\vec e_\theta=\frac{-\vec e_x+\vec e_y}{\sqrt2}$ : $\vec B_P=\frac{\mu_0I_1}{4\pi a}(-\vec e_x+\vec e_y)$.

**4.2 Champ nul.** Selon $x$ : $-\frac{I_2}2-\frac{I_1}4=0$ ; selon $y$ : $\frac{I_3}2+\frac{I_1}4=0$. Donc
$$I_2=I_3=-\frac{I_1}2.$$
Les fils voisins de $R$ portent chacun la moitié du courant du fil opposé, en sens contraire.

**4.3 Force.** Le champ des trois fils est nul en $R$ : le quatrième fil ne subit **aucune** force, quel que soit $I'$.

**Étape 5 — Vérification.**

> **Vérification — Symétrie.** Avec $I_2=I_3$, la configuration est symétrique par rapport à la diagonale $PR$ ; le champ en $R$ est alors porté par la direction orthogonale à $PR$ : une seule équation scalaire suffit, ce qui explique que la condition se réduise à $I_2=I_3=-I_1/2$.

**Étape 6 — Conclusion.**
$$\boxed{I_2=I_3=-\tfrac{I_1}2\quad\Rightarrow\quad\vec B(R)=\vec 0\ \text{et force nulle sur le fil en }R}$$""",
r"""$\vec B_Q=\frac{\mu_0I_3}{2\pi a}\vec e_y$, $\vec B_S=-\frac{\mu_0I_2}{2\pi a}\vec e_x$, $\vec B_P=\frac{\mu_0I_1}{4\pi a}(-\vec e_x+\vec e_y)$ ; champ nul si $I_2=I_3=-I_1/2$ ; le fil ajouté en $R$ ne subit alors aucune force.""")
src(CCINP, 'CCINP')

# ------------------------------------------------------------------ 13. Cylindre retenu par un ressort
ex('n-pc-cylressort', P, 'Mécanique', 2, 'Cylindre roulant retenu par un ressort', 25, r"""
Un cylindre homogène de masse $M$, de rayon $R$ (moment d'inertie $J=\frac12MR^2$ par rapport à son axe), roule sans glisser sur un plan incliné d'un angle $\alpha$. Son axe est relié, vers le haut de la pente, à un ressort de raideur $k$ et de longueur à vide $\ell_0$, parallèle à la pente. On note $x$ l'écart (compté vers le bas de la pente) de la longueur du ressort à sa longueur d'équilibre $\ell_e$, et $\varphi$ l'angle de rotation du cylindre. Le coefficient de frottement est $f$.

1. Écrire la condition de roulement sans glissement reliant $\dot x$ et $\dot\varphi$.
2. À l'aide des théorèmes de la résultante dynamique et du moment cinétique, établir l'équation différentielle vérifiée par $x$. Exprimer $\ell_e$.
3. Le cylindre est lâché sans vitesse avec $x(0)=X_0$. Donner $x(t)$, puis la condition sur $f$ pour que le roulement sans glissement soit toujours assuré.
4. Retrouver l'équation du mouvement par une méthode énergétique.
""", r"""Vitesse du point de contact nulle : $\dot x=R\dot\varphi$ avec une orientation convenable de $\varphi$.""",
r"""Introduis la composante tangentielle $T$ de la réaction ; le moment cinétique en $G$ donne $J\ddot\varphi=-RT$.""",
r"""L'énergie cinétique vaut $\frac12M\dot x^2+\frac12J\dot\varphi^2=\frac34M\dot x^2$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Un oscillateur dont l'inertie inclut la rotation : on attend $\omega^2=\frac{k}{M_{\text{eff}}}$ avec $M_{\text{eff}}=\frac32M$. Le frottement statique est nécessaire et doit rester dans le cône de Coulomb.

**Étape 2 — Rappels du cours.**

> **Théorèmes — Solide en mouvement plan.** $M\vec a_G=\sum\vec F$ et $J\ddot\varphi=\sum\mathcal M_G$.

> **Loi — Frottement de Coulomb.** Sans glissement, $|T|\le f|N|$ (le rapport Centrale 2025 rappelle d'orienter correctement la composante de frottement).

**Étape 3 — Stratégie.** Projections sur la pente et sur la normale, moment en $G$, élimination de $T$ ; puis vérification de la condition de non-glissement sur tout le mouvement.

**Étape 4 — Résolution détaillée.**

**4.1 Roulement.** Vitesse du point de contact $I$ : $\vec v_I=\vec v_G+\vec\omega\wedge\overrightarrow{GI}=\vec 0$, soit $\dot x=R\dot\varphi$ en orientant $\varphi$ dans le sens du roulement vers le bas.

**4.2 Équation.** Sur la pente (vers le bas) : $M\ddot x=Mg\sin\alpha-k(\ell_e-\ell_0+x)+T$. À l'équilibre ($T=0$) : $\ell_e=\ell_0+\frac{Mg\sin\alpha}k$. Moment en $G$ : $J\ddot\varphi=-RT$, donc $T=-\frac J{R^2}\ddot x=-\frac12M\ddot x$. D'où
$$\frac32M\ddot x+kx=0,\qquad\omega=\sqrt{\frac{2k}{3M}}.$$

**4.3 Mouvement et frottement.** $x=X_0\cos\omega t$. Normale : $N=Mg\cos\alpha$. $|T|=\frac12M\omega^2|x|\le\frac12M\omega^2X_0=\frac{kX_0}3$. Il faut donc $\frac{kX_0}3\le fMg\cos\alpha$, soit
$$f\ge\frac{kX_0}{3Mg\cos\alpha}.$$

**4.4 Énergie.** Les actions de contact ne travaillent pas (roulement sans glissement). $E_m=\frac34M\dot x^2+\frac12k(\ell_e-\ell_0+x)^2-Mgx\sin\alpha$ est constante ; en dérivant et en utilisant $k(\ell_e-\ell_0)=Mg\sin\alpha$ : $\dot x\big(\frac32M\ddot x+kx\big)=0$.

**Étape 5 — Vérification.**

> **Vérification — Cas limites.** Sans rotation ($J=0$), on retrouverait $\omega=\sqrt{k/M}$ : la rotation alourdit l'oscillateur d'un facteur $\frac32$. Pour $\alpha\to\frac\pi2$, $N\to0$ : impossible de rouler sans glisser, comme l'indique la condition sur $f$.

**Étape 6 — Conclusion.**
$$\boxed{\tfrac32M\ddot x+kx=0,\ \omega=\sqrt{\tfrac{2k}{3M}},\ \ell_e=\ell_0+\tfrac{Mg\sin\alpha}k,\ f\ge\tfrac{kX_0}{3Mg\cos\alpha}}$$""",
r"""$\dot x=R\dot\varphi$ ; $T=-\frac12M\ddot x$ donne $\frac32M\ddot x+kx=0$, $\omega=\sqrt{2k/3M}$, $\ell_e=\ell_0+Mg\sin\alpha/k$ ; non-glissement si $f\ge\frac{kX_0}{3Mg\cos\alpha}$ ; même équation par conservation de l'énergie.""")
src(CCINP + " Remarque du rapport du jury Centrale-Supélec 2025 sur l'orientation du frottement.", 'CCINP')

# ------------------------------------------------------------------ 14. Paramagnétisme de Langevin
ex('n-pc-langevin', P, 'Physique statistique', 3, 'Paramagnétisme de Langevin et loi de Curie', 30, r"""
Un matériau contient $n$ moments magnétiques par unité de volume, indépendants, de norme $\mu$, à l'équilibre à la température $T$ dans un champ $\vec B=B\vec e_z$. L'énergie d'un moment est $\varepsilon=-\vec\mu\cdot\vec B$. On cherche l'aimantation $M$ (moment moyen par unité de volume) et l'on compare à la loi de Curie $M=\frac{C_{\text{Curie}}}TB$.

1. **Modèle à deux niveaux.** Le moment ne peut valoir que $\pm\mu\vec e_z$. Calculer $\langle\mu_z\rangle$ par la loi de Boltzmann, puis $M$ à haute température.
2. **Modèle de Langevin.** Le moment peut prendre toutes les orientations ; la probabilité qu'il fasse un angle compris entre $\theta$ et $\theta+\mathrm d\theta$ avec $\vec e_z$ est proportionnelle à $e^{\beta\mu B\cos\theta}\sin\theta\,\mathrm d\theta$, avec $\beta=\frac1{k_BT}$. Justifier le facteur $\sin\theta$, puis montrer que $\langle\mu_z\rangle=\mu\,\mathcal L(\beta\mu B)$ avec $\mathcal L(y)=\coth y-\frac1y$.
3. Étudier $\mathcal L$ pour $y\ll1$ et $y\gg1$. En déduire la constante de Curie dans chaque modèle, et comparer.
4. Application : $\mu=\mu_B=9{,}27\times10^{-24}\ \mathrm{J\cdot T^{-1}}$, $B=1\ \mathrm T$, $T=300\ \mathrm K$. Quel régime ?
""", r"""Deux niveaux d'énergie $\mp\mu B$ : $\langle\mu_z\rangle=\mu\tanh(\beta\mu B)$.""",
r"""L'angle solide entre les cônes d'angles $\theta$ et $\theta+\mathrm d\theta$ vaut $2\pi\sin\theta\,\mathrm d\theta$ ; pose $u=\cos\theta$ pour intégrer.""",
r"""$\coth y=\frac1y+\frac y3+O(y^3)$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Les moments sont indépendants : la statistique de Boltzmann s'applique à chacun. On compare un modèle discret et un modèle continu ; tous deux donnent une loi de Curie à haute température, avec des constantes différentes.

**Étape 2 — Rappels du cours.**

> **Loi — Boltzmann.** Pour un système en équilibre avec un thermostat, la probabilité d'un état d'énergie $\varepsilon$ est proportionnelle à $e^{-\varepsilon/k_BT}$.

> **Formule — Angle solide.** L'élément d'angle solide en coordonnées sphériques vaut $\sin\theta\,\mathrm d\theta\,\mathrm d\phi$.

**Étape 3 — Stratégie.** Somme sur deux états, puis intégrale sur les orientations avec le changement $u=\cos\theta$ ; développements limités.

**Étape 4 — Résolution détaillée.**

**4.1 Deux niveaux.** $p_\pm\propto e^{\pm\beta\mu B}$, donc $\langle\mu_z\rangle=\mu\frac{e^{y}-e^{-y}}{e^y+e^{-y}}=\mu\tanh y$ avec $y=\beta\mu B$. Pour $y\ll1$ : $M=n\langle\mu_z\rangle\approx\frac{n\mu^2}{k_BT}B$, soit $C_{\text{Curie}}^{(2)}=\frac{n\mu^2}{k_B}$.

**4.2 Langevin.** Les orientations sont uniformément réparties en angle solide en l'absence de champ ; celles d'angle entre $\theta$ et $\theta+\mathrm d\theta$ occupent $2\pi\sin\theta\,\mathrm d\theta$, d'où le facteur $\sin\theta$. Avec $u=\cos\theta$ :
$$\langle\cos\theta\rangle=\frac{\int_{-1}^1ue^{yu}\,\mathrm du}{\int_{-1}^1e^{yu}\,\mathrm du}=\frac{\mathrm d}{\mathrm dy}\ln\Big(\frac{2\operatorname{sh}y}y\Big)=\coth y-\frac1y=\mathcal L(y).$$

**4.3 Limites.** Pour $y\ll1$ : $\mathcal L(y)\approx\frac y3$, d'où $M\approx\frac{n\mu^2}{3k_BT}B$ et $C_{\text{Curie}}^{(L)}=\frac{n\mu^2}{3k_B}$, trois fois plus petite que pour deux niveaux (seule une composante sur trois s'aligne en moyenne). Pour $y\gg1$ : $\mathcal L\to1$ : saturation, tous les moments sont alignés, $M\to n\mu$.

**4.4 Application.** $y=\frac{9{,}27\times10^{-24}\times1}{1{,}38\times10^{-23}\times300}\approx2{,}2\times10^{-3}\ll1$ : régime linéaire, loi de Curie bien vérifiée. La saturation demanderait des températures de l'ordre du kelvin et des champs de plusieurs teslas.

**Étape 5 — Vérification.**

> **Vérification — Cohérence.** $0\le\mathcal L(y)<1$ et $\tanh y<1$ : le moment moyen ne dépasse jamais $\mu$. Les deux modèles coïncident à forte aimantation (saturation) et diffèrent d'un facteur 3 à haute température.

**Étape 6 — Conclusion.**
$$\boxed{\langle\mu_z\rangle=\mu\tanh(\beta\mu B)\ \text{ou}\ \mu\,\mathcal L(\beta\mu B);\quad C^{(2)}=\tfrac{n\mu^2}{k_B},\ C^{(L)}=\tfrac{n\mu^2}{3k_B};\quad y\approx2\times10^{-3}\ \text{(régime de Curie)}}$$""",
r"""Deux niveaux : $\mu\tanh(\beta\mu B)$, $C=n\mu^2/k_B$. Langevin : poids $e^{y\cos\theta}\sin\theta$, $\langle\mu_z\rangle=\mu(\coth y-1/y)$, $C=n\mu^2/(3k_B)$ ; saturation pour $y\gg1$ ; ici $y\approx2{,}2\times10^{-3}$ : régime de Curie.""")
src(PREP.format('CCS / CCMP'), 'Centrale')

# ------------------------------------------------------------------ 15. Repliement de spectre
ex('n-pc-shannon', P, 'Électrocinétique', 1, 'Échantillonnage et repliement de spectre', 15, r"""
On échantillonne un signal à la fréquence $f_e$.

1. Énoncer le critère de Nyquist-Shannon. Que se passe-t-il s'il n'est pas respecté ?
2. Un signal sinusoïdal de fréquence $f=3{,}0\ \mathrm{kHz}$ est échantillonné à $f_e=4{,}0\ \mathrm{kHz}$. Quelle fréquence apparente lit-on sur le spectre calculé, qui s'étend de $0$ à $f_e/2$ ?
3. Une roue de vélo comporte une valve, qui tourne à 50 tours par seconde. Elle est filmée à 48 images par seconde, puis à 52 images par seconde. Que voit-on ?
4. Pour numériser de la musique (fréquences audibles jusqu'à $20\ \mathrm{kHz}$), on échantillonne à $44{,}1\ \mathrm{kHz}$. Pourquoi faut-il placer un filtre analogique avant l'échantillonneur ? Quelles caractéristiques doit-il avoir ?
""", r"""Le spectre d'un signal échantillonné est périodisé de période $f_e$ : une fréquence $f$ apparaît aussi en $|f-kf_e|$ pour tout entier $k$.""",
r"""Cherche l'entier $k$ qui ramène $f-kf_e$ dans l'intervalle $[-f_e/2,f_e/2]$.""",
r"""Une fréquence apparente négative signifie une rotation apparente en sens inverse.""",
r"""**Étape 1 — Analyse de l'énoncé.** L'échantillonnage confond les fréquences qui diffèrent d'un multiple de $f_e$. Le critère de Shannon évite cette ambiguïté ; le stroboscope en donne une illustration visuelle.

**Étape 2 — Rappels du cours.**

> **Théorème — Nyquist-Shannon.** Un signal de fréquence maximale $f_{\max}$ est correctement représenté par ses échantillons si $f_e>2f_{\max}$.

> **Propriété — Repliement.** Les échantillons de $\cos(2\pi ft)$ et de $\cos(2\pi(f-kf_e)t)$ sont identiques pour tout entier $k$.

**Étape 3 — Stratégie.** Ramener chaque fréquence dans $[-f_e/2,f_e/2]$ par translation d'un multiple de $f_e$ ; le rapport Centrale 2025 insiste sur ce lien entre condition de Shannon et repliement.

**Étape 4 — Résolution détaillée.**

**4.1 Critère.** $f_e>2f_{\max}$. Sinon, les composantes de fréquence supérieure à $f_e/2$ se replient : elles apparaissent à de fausses fréquences, et rien dans les échantillons ne permet de les distinguer des vraies.

**4.2 Sinusoïde.** $3{,}0-4{,}0=-1{,}0\ \mathrm{kHz}$ : on lit un pic à $1{,}0\ \mathrm{kHz}$ (un cosinus de fréquence $-1$ kHz est le même que de fréquence $+1$ kHz).

**4.3 Roue.** À 48 images/s : $50-48=2$ : la valve semble tourner lentement, à 2 tr/s, dans le bon sens. À 52 images/s : $50-52=-2$ : elle semble tourner à 2 tr/s en sens inverse (effet « roue de diligence »).

**4.4 Audio.** $44{,}1\ \mathrm{kHz}>2\times20\ \mathrm{kHz}$, mais un son contient aussi des composantes inaudibles au-delà de $22{,}05\ \mathrm{kHz}$, qui se replieraient dans la bande audible (une composante à 30 kHz apparaîtrait à 14,1 kHz). On place donc un filtre passe-bas anti-repliement : il doit transmettre jusqu'à 20 kHz et atténuer fortement au-delà de 22,05 kHz, d'où un filtre d'ordre élevé (transition raide).

**Étape 5 — Vérification.**

> **Vérification — Cohérence.** Une fréquence apparente est toujours comprise entre $0$ et $f_e/2$ ; ici $1{,}0\ \mathrm{kHz}\le2{,}0\ \mathrm{kHz}$ et $2\ \mathrm{tr/s}\le24\ \mathrm{tr/s}$.

**Étape 6 — Conclusion.**
$$\boxed{f_e>2f_{\max};\quad 3\ \mathrm{kHz}\to1\ \mathrm{kHz};\quad\text{roue : }+2\ \mathrm{tr/s}\text{ puis }-2\ \mathrm{tr/s};\quad\text{filtre anti-repliement avant l'échantillonneur}}$$""",
r"""Shannon : $f_e>2f_{\max}$ ; $f$ apparaît en $|f-kf_e|\le f_e/2$ : 3 kHz → 1 kHz ; roue : 2 tr/s dans le bon sens à 48 im/s, à l'envers à 52 im/s ; passe-bas raide coupant au-delà de 22 kHz avant l'échantillonnage.""")
src(CENTRALE.format('condition de Nyquist-Shannon et repliement de spectre'), 'Centrale')

# ------------------------------------------------------------------ 16. Miroirs de Fresnel
ex('n-pc-fresnel', P, 'Optique ondulatoire', 2, 'Miroirs de Fresnel', 25, r"""
Deux miroirs plans $M_1$ et $M_2$ ont une arête commune $(Oz)$ et font entre eux un angle $\pi-\alpha$, avec $\alpha=0{,}080\ \mathrm{mrad}$. Une source ponctuelle monochromatique $S$, de longueur d'onde $\lambda_0=576{,}9\ \mathrm{nm}$, est placée à la distance $OS=R=80\ \mathrm{cm}$ de l'arête. On observe sur un écran parallèle à l'arête, perpendiculaire au plan médiateur des images $S_1$ et $S_2$ de $S$ par les miroirs, à la distance $d=1{,}20\ \mathrm m$ de $O$.

1. Faire une figure. Montrer que $S_1$ et $S_2$ sont sur le cercle de centre $O$ et de rayon $R$, et que $S_1S_2\approx2R\alpha$.
2. En déduire l'éclairement $\mathcal E(x)$ sur l'écran ($x$ repère un point de l'écran à partir du plan médiateur de $S_1S_2$) et l'interfrange. Application numérique.
3. La source est maintenant blanche. Décrire la figure observée.
""", r"""Une image par un miroir plan est le symétrique de l'objet : elle est à la même distance de tout point du miroir, en particulier de l'arête $O$.""",
r"""L'angle $S_1OS_2$ vaut le double de l'angle entre les normales aux miroirs, soit $2\alpha$.""",
r"""On est ramené à deux sources ponctuelles cohérentes distantes de $a=2R\alpha$, à la distance $D\approx R+d$ de l'écran : $i=\frac{\lambda_0D}a$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Dispositif à division du front d'onde : les deux miroirs donnent deux images cohérentes de la même source, très proches. On se ramène aux trous d'Young.

**Étape 2 — Rappels du cours.**

> **Propriété — Miroir plan.** L'image d'un point est son symétrique par rapport au plan du miroir.

> **Formule — Deux sources ponctuelles.** Pour deux sources cohérentes distantes de $a$, à la distance $D\gg a$ d'un écran parallèle à leur médiatrice, $\delta\approx\frac{ax}D$ et $i=\frac{\lambda_0D}a$.

**Étape 3 — Stratégie.** Géométrie des images, puis formule des deux sources.

**Étape 4 — Résolution détaillée.**

**4.1 Sources secondaires.** $OS_1=OS_2=OS=R$ (symétries par rapport à des plans contenant $O$). La composée des deux symétries est une rotation d'axe $Oz$ d'angle double de l'angle entre les miroirs : l'angle $\widehat{S_1OS_2}=2\alpha$. D'où $S_1S_2=2R\sin\alpha\approx2R\alpha=0{,}128\ \mathrm{mm}$.

**4.2 Éclairement.** Les sources $S_1$, $S_2$ sont cohérentes (images de la même source). Leur distance à l'écran vaut $D=R\cos\alpha+d\approx R+d=2{,}00\ \mathrm m$. Avec $a=2R\alpha$ :
$$\mathcal E(x)=2\mathcal E_0\Big[1+\cos\Big(\frac{2\pi}{\lambda_0}\frac{2R\alpha\,x}{R+d}\Big)\Big],\qquad i=\frac{\lambda_0(R+d)}{2R\alpha}=\frac{576{,}9\times10^{-9}\times2{,}00}{2\times0{,}80\times0{,}080\times10^{-3}}\approx9{,}0\ \mathrm{mm}.$$
Les franges sont rectilignes, parallèles à l'arête, et n'existent que dans la zone de l'écran éclairée par les deux faisceaux réfléchis.

**4.3 Lumière blanche.** La frange centrale ($x=0$, $\delta=0$) est blanche pour toutes les longueurs d'onde ; de part et d'autre apparaissent quelques franges irisées (l'interfrange est proportionnel à $\lambda_0$), puis, dès que $\delta$ dépasse quelques micromètres, un blanc d'ordre supérieur où les couleurs se brouillent.

**Étape 5 — Vérification.**

> **Vérification — Ordre de grandeur.** $i\approx9\ \mathrm{mm}$ est facile à observer ; c'est grâce à l'angle très petit entre les miroirs. Avec $\alpha=1^\circ$, on aurait $i\approx40\ \mu\mathrm m$, invisible à l'œil nu.

**Étape 6 — Conclusion.**
$$\boxed{S_1S_2=2R\alpha,\quad\mathcal E=2\mathcal E_0\Big[1+\cos\frac{4\pi R\alpha x}{\lambda_0(R+d)}\Big],\quad i=\frac{\lambda_0(R+d)}{2R\alpha}\approx9{,}0\ \mathrm{mm}}$$""",
r"""Images $S_1$, $S_2$ sur le cercle de rayon $R$, $\widehat{S_1OS_2}=2\alpha$, donc $a=2R\alpha$ ; deux sources cohérentes à $D\approx R+d$ : $i=\frac{\lambda_0(R+d)}{2R\alpha}\approx9{,}0$ mm ; en lumière blanche, frange centrale blanche, quelques franges irisées, puis blanc d'ordre supérieur.""")
src(PREP.format('CCINP / CCS'), 'CCINP')

# ------------------------------------------------------------------ 17. Interférences à trois ondes
ex('n-pc-troisondes', P, 'Optique ondulatoire', 3, 'Interférences à trois ondes', 30, r"""
Trois fentes fines, parallèles et équidistantes (pas $a$), sont éclairées en incidence normale par une onde plane monochromatique de longueur d'onde $\lambda$. On observe à l'infini dans la direction $\theta$ et l'on note $\varphi=\frac{2\pi a\sin\theta}\lambda$ le déphasage entre deux fentes voisines. On néglige la diffraction par chaque fente.

1. Les trois ondes ont la même amplitude. Montrer que l'intensité vaut $I(\varphi)=I_0(1+2\cos\varphi)^2$. Étudier ses maxima principaux, ses zéros et ses maxima secondaires, et tracer l'allure.
2. Comparer avec deux fentes ($I=2I_0(1+\cos\varphi)$ pour la même amplitude par fente) : position et largeur des maxima principaux.
3. On place devant la fente centrale un filtre qui multiplie son amplitude par $\beta>0$. Exprimer l'intensité et le contraste $V=\frac{I_{\max}-I_{\min}}{I_{\max}+I_{\min}}$ en fonction de $\beta$.
4. Généraliser la question 1 à $N$ fentes et justifier qu'un réseau sépare d'autant mieux deux longueurs d'onde que $N$ est grand.
""", r"""Somme des amplitudes complexes : $A(1+e^{i\varphi}+e^{2i\varphi})=Ae^{i\varphi}(e^{-i\varphi}+1+e^{i\varphi})$.""",
r"""Avec la fente centrale d'amplitude $\beta$ : amplitude $Ae^{i\varphi}(\beta+2\cos\varphi)$ ; distingue $\beta\le2$ et $\beta>2$ pour le minimum.""",
r"""Pour $N$ fentes, somme géométrique : $\big|\frac{\sin(N\varphi/2)}{\sin(\varphi/2)}\big|^2$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Interférences à plus de deux ondes : on somme les amplitudes complexes. Les maxima principaux restent aux mêmes positions qu'avec deux ondes, mais deviennent plus fins : c'est le principe du réseau.

**Étape 2 — Rappels du cours.**

> **Principe — Superposition cohérente.** Les amplitudes complexes s'ajoutent ; l'intensité est proportionnelle au carré du module de l'amplitude totale.

> **Formule — Somme géométrique.** $\sum_{p=0}^{N-1}e^{ip\varphi}=e^{i(N-1)\varphi/2}\frac{\sin(N\varphi/2)}{\sin(\varphi/2)}$.

**Étape 3 — Stratégie.** Factoriser par le terme central, étudier la fonction obtenue, puis généraliser.

**Étape 4 — Résolution détaillée.**

**4.1 Trois ondes.** $\underline A=A(1+e^{i\varphi}+e^{2i\varphi})=Ae^{i\varphi}(1+2\cos\varphi)$, donc $I=I_0(1+2\cos\varphi)^2$ avec $I_0\propto|A|^2$. Maxima principaux : $\varphi=2m\pi$, $I=9I_0$. Zéros : $\cos\varphi=-\frac12$, soit $\varphi=\pm\frac{2\pi}3$ modulo $2\pi$. Maximum secondaire : $\varphi=\pi$, $I=I_0$, neuf fois plus faible.

**4.2 Comparaison.** Avec deux fentes, maxima en $\varphi=2m\pi$ aussi, d'intensité $4I_0$, et premiers zéros en $\varphi=\pm\pi$. Avec trois, les premiers zéros sont en $\pm\frac{2\pi}3$ : les pics principaux sont plus étroits (demi-largeur $\frac{2\pi}3$ au lieu de $\pi$) et plus intenses.

**4.3 Fente centrale filtrée.** $\underline A=Ae^{i\varphi}(\beta+2\cos\varphi)$, $I=I_0(\beta+2\cos\varphi)^2$ avec $I_{\max}=I_0(\beta+2)^2$. Si $\beta\le2$, $\beta+2\cos\varphi$ s'annule : $I_{\min}=0$ et $V=1$. Si $\beta>2$, $I_{\min}=I_0(\beta-2)^2$ et
$$V=\frac{(\beta+2)^2-(\beta-2)^2}{(\beta+2)^2+(\beta-2)^2}=\frac{4\beta}{\beta^2+4}.$$

**4.4 N fentes.** $I=I_0\Big(\frac{\sin(N\varphi/2)}{\sin(\varphi/2)}\Big)^2$ : maxima principaux $N^2I_0$ en $\varphi=2m\pi$, premiers zéros en $\varphi=2m\pi\pm\frac{2\pi}N$. La largeur angulaire d'un pic est en $\frac1N$ : deux longueurs d'onde voisines donnent des pics décalés qui se séparent dès que le décalage dépasse cette largeur, d'où un pouvoir de résolution $\frac\lambda{\Delta\lambda}=mN$ proportionnel à $N$.

**Étape 5 — Vérification.**

> **Vérification — Cas particuliers.** Pour $N=3$, la formule générale donne $\big(\frac{\sin(3\varphi/2)}{\sin(\varphi/2)}\big)^2=(1+2\cos\varphi)^2$ (identité $\sin3u=\sin u\,(1+2\cos2u)$). Pour $\beta=1$, $V=1$ ; pour $\beta\to\infty$ (fente centrale dominante), $V\to0$ : il n'y a plus qu'une onde.

**Étape 6 — Conclusion.**
$$\boxed{I=I_0(1+2\cos\varphi)^2;\quad V=1\ (\beta\le2),\ V=\tfrac{4\beta}{\beta^2+4}\ (\beta>2);\quad I_N=I_0\Big(\tfrac{\sin(N\varphi/2)}{\sin(\varphi/2)}\Big)^2}$$""",
r"""$\underline A=Ae^{i\varphi}(1+2\cos\varphi)$ : maxima $9I_0$ en $2m\pi$, zéros en $\pm\frac{2\pi}3$, secondaires $I_0$ en $\pi$ ; pics plus fins qu'à deux ondes ; filtre : $V=1$ si $\beta\le2$, $\frac{4\beta}{\beta^2+4}$ sinon ; $N$ fentes : largeur en $1/N$, pouvoir de résolution $mN$.""")
src(PREP.format('CCMP / X / ENS'), 'X')

# ------------------------------------------------------------------ 18. Ciel bleu
ex('n-pc-cielbleu', P, 'Rayonnement', 2, 'Pourquoi le ciel est-il bleu ?', 25, r"""
On modélise un électron d'une molécule de l'air par un oscillateur : $m\ddot{\vec r}=-m\omega_0^2\vec r-e\vec E$, où $\vec E=E_0\cos(\omega t)\,\vec e_x$ est le champ de l'onde solaire. On néglige l'amortissement. La pulsation propre $\omega_0$ correspond à une longueur d'onde dans l'ultraviolet ($\lambda_0\approx100\ \mathrm{nm}$).

1. Déterminer le dipôle induit $\vec p(t)=-e\vec r(t)$ en régime forcé. Le simplifier pour la lumière visible.
2. On admet qu'un dipôle oscillant $p_0\cos\omega t$ rayonne la puissance moyenne $\mathcal P=\frac{\mu_0p_0^2\omega^4}{12\pi c}$. Justifier l'approximation dipolaire, puis montrer que la puissance diffusée varie en $\frac1{\lambda^4}$.
3. Calculer le rapport des puissances diffusées pour le bleu ($450\ \mathrm{nm}$) et le rouge ($700\ \mathrm{nm}$). Expliquer la couleur du ciel, et celle du Soleil couchant.
4. La lumière diffusée à $90^\circ$ de la direction du Soleil est-elle polarisée ? Justifier.
""", r"""En régime forcé sinusoïdal, $\vec r=\frac{-e\vec E}{m(\omega_0^2-\omega^2)}$.""",
r"""Dans le visible, $\omega\ll\omega_0$ : l'amplitude du dipôle ne dépend presque pas de $\omega$, donc $\mathcal P\propto\omega^4$.""",
r"""Un dipôle ne rayonne pas dans la direction de son axe ; le champ rayonné est dans le plan contenant l'axe du dipôle et la direction d'observation.""",
r"""**Étape 1 — Analyse de l'énoncé.** Modèle de l'électron élastiquement lié : le champ de l'onde fait osciller le dipôle, qui rayonne. La dépendance en $\omega^4$ du rayonnement explique la diffusion préférentielle du bleu (diffusion Rayleigh).

**Étape 2 — Rappels du cours.**

> **Modèle — Électron élastiquement lié.** Force de rappel $-m\omega_0^2\vec r$, force électrique $-e\vec E$ ; la force magnétique est négligeable ($v\ll c$).

> **Formule — Rayonnement dipolaire.** Puissance moyenne rayonnée $\frac{\mu_0p_0^2\omega^4}{12\pi c}$ ; le champ rayonné à grande distance est nul dans l'axe du dipôle et maximal dans le plan perpendiculaire.

**Étape 3 — Stratégie.** Régime forcé, limite $\omega\ll\omega_0$, puis rapport des puissances ; enfin géométrie du rayonnement pour la polarisation (le rapport Centrale 2025 insiste sur le sens physique de ce modèle et de l'approximation dipolaire).

**Étape 4 — Résolution détaillée.**

**4.1 Dipôle.** En régime forcé : $\vec r=-\frac{e\vec E}{m(\omega_0^2-\omega^2)}$, donc $\vec p=\frac{e^2}{m(\omega_0^2-\omega^2)}\vec E$. Dans le visible ($\lambda\ge400\ \mathrm{nm}\gg\lambda_0$), $\omega\ll\omega_0$ et $\vec p\approx\frac{e^2}{m\omega_0^2}\vec E$, indépendant de $\omega$.

**4.2 Loi en $1/\lambda^4$.** Approximation dipolaire : la molécule (taille $\sim0{,}1\ \mathrm{nm}$) est très petite devant $\lambda$, et l'on observe à grande distance. Alors $\mathcal P=\frac{\mu_0}{12\pi c}\Big(\frac{e^2E_0}{m\omega_0^2}\Big)^2\omega^4\propto\omega^4\propto\frac1{\lambda^4}$.

**4.3 Couleurs.** $\frac{\mathcal P_{\text{bleu}}}{\mathcal P_{\text{rouge}}}=\Big(\frac{700}{450}\Big)^4\approx5{,}9$. La lumière diffusée vers nous par l'atmosphère, hors de la direction du Soleil, est donc dominée par le bleu (le violet, encore plus diffusé, est moins présent dans le spectre solaire et l'œil y est moins sensible). Au coucher, la lumière directe traverse une grande épaisseur d'air : elle a perdu une grande partie de son bleu, et le Soleil paraît rouge orangé.

**4.4 Polarisation.** Le champ solaire est transverse : il est perpendiculaire à la direction du Soleil, donc les dipôles oscillent dans ce plan. Pour une observation à $90^\circ$, la composante du dipôle dirigée vers l'observateur ne rayonne pas vers lui ; seule rayonne la composante perpendiculaire à la fois à la direction du Soleil et à la ligne de visée : la lumière reçue est polarisée rectilignement.

**Étape 5 — Vérification.**

> **Vérification — Domaine de validité.** Si $\omega$ approchait $\omega_0$ (ultraviolet), le dénominateur $\omega_0^2-\omega^2$ ne serait plus négligeable et l'amortissement interviendrait : la loi en $\omega^4$ ne vaut que loin de la résonance, ce qui est bien le cas dans le visible.

**Étape 6 — Conclusion.**
$$\boxed{\vec p\approx\frac{e^2}{m\omega_0^2}\vec E,\quad\mathcal P\propto\frac1{\lambda^4},\quad\frac{\mathcal P_{450}}{\mathcal P_{700}}\approx5{,}9;\ \text{lumière diffusée à }90^\circ\text{ polarisée}}$$""",
r"""$\vec p=\frac{e^2}{m(\omega_0^2-\omega^2)}\vec E\approx\frac{e^2}{m\omega_0^2}\vec E$ dans le visible ; $\mathcal P\propto\omega^4\propto\lambda^{-4}$ ; le bleu est diffusé $(700/450)^4\approx5{,}9$ fois plus que le rouge ; à $90^\circ$, la lumière diffusée est polarisée rectilignement.""")
src(CENTRALE.format('rayonnement dipolaire et modèle de l’électron élastiquement lié'), 'Centrale')
