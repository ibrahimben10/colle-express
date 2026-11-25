# Physique — exercices d'après des planches d'oral CCINP (L'Officiel de la Taupe), une préparation aux oraux
# (type CCINP / CCS / CCMP) et les attentes du rapport de jury Centrale-Supélec 2025.
# Énoncés reformulés, indices et corrigés originaux.
from newlib import ex, E

def src(texte, concours):
    E[-1]['enonce'] += '\n\n*' + texte + '*'
    E[-1]['concours'] = concours
    E[-1]['ajout'] = '2026-11-25'

P = 'Physique'
CCINP = "D'après une planche d'oral CCINP (MP)."

# ------------------------------------------------------------------ 1. Radiateur
ex('n-pc-radiateur', P, 'Thermodynamique', 1, 'Radiateur d’un composant électronique', 15, r"""
Un radiateur de capacité thermique $C$, de température uniforme $T(t)$, reçoit d'un composant électronique une puissance thermique constante $P$. Il cède à l'air ambiant, de température constante $T_0$, la puissance $\varphi=h\,(T-T_0)$. À $t=0$, $T=T_0$.

1. Faire un bilan d'énergie pour le radiateur entre $t$ et $t+\mathrm dt$ et en déduire l'équation différentielle vérifiée par $T$. Faire apparaître une durée caractéristique $\tau$.
2. Résoudre, tracer $T(t)$ et calculer $T(\tau)-T_0$.
3. Au bout de combien de temps le radiateur atteint-il sa température finale à 1 % près (de l'écart) ?

On donne $C=2{,}0\ \mathrm{kJ\cdot K^{-1}}$, $h=10\ \mathrm{W\cdot K^{-1}}$, $P=100\ \mathrm W$.
""", r"""Premier principe pour le radiateur (solide, pas de travail) : $\mathrm dU=C\,\mathrm dT$ égale la chaleur reçue pendant $\mathrm dt$.""",
r"""La chaleur reçue vaut $P\,\mathrm dt-h(T-T_0)\,\mathrm dt$ ; tu dois trouver $\tau=C/h$.""",
r"""L'écart à la valeur finale décroît comme $e^{-t/\tau}$ : il vaut 1 % de l'écart initial quand $e^{-t/\tau}=0{,}01$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Système : le radiateur, solide de température uniforme. Il reçoit $P$ et perd une puissance conducto-convective proportionnelle à l'écart de température : on attend une relaxation exponentielle du premier ordre.

**Étape 2 — Rappels du cours.**

> **Principe — Premier principe pour une phase condensée.** $\mathrm dU=C\,\mathrm dT=\delta W+\delta Q$, avec $\delta W\approx0$ pour un solide indilatable.

> **Loi — Transfert conducto-convectif (loi de Newton).** La puissance cédée par une paroi à un fluide vaut $h\,(T-T_0)$, positive si $T>T_0$.

**Étape 3 — Stratégie.** Bilan sur $[t,t+\mathrm dt]$, équation du premier ordre à coefficients constants, solution particulière constante plus solution homogène.

**Étape 4 — Résolution détaillée.**

**4.1 Équation.** $C\,\mathrm dT=P\,\mathrm dt-h(T-T_0)\,\mathrm dt$, soit
$$\tau\frac{\mathrm dT}{\mathrm dt}+T=T_0+\frac Ph,\qquad\tau=\frac Ch=200\ \mathrm s.$$

**4.2 Solution.** Avec $T(0)=T_0$ : $T(t)=T_0+\dfrac Ph\big(1-e^{-t/\tau}\big)$. La courbe part de $T_0$ avec la pente $P/C$ et tend vers $T_\infty=T_0+P/h=T_0+10\ \mathrm K$. $T(\tau)-T_0=\frac Ph(1-e^{-1})\approx6{,}3\ \mathrm K$.

**4.3 Durée.** $T_\infty-T=\frac Ph e^{-t/\tau}$ ; on veut $e^{-t/\tau}=0{,}01$, soit $t_{1\%}=\tau\ln100\approx4{,}6\,\tau\approx9{,}2\times10^2\ \mathrm s$, environ 15 minutes.

**Étape 5 — Vérification.**

> **Vérification — Cohérence.** En régime permanent, la puissance reçue est entièrement évacuée : $P=h(T_\infty-T_0)$, soit $10\ \mathrm K$ d'écart. Unités : $C/h$ en $\mathrm{J\cdot K^{-1}}/(\mathrm{W\cdot K^{-1}})=\mathrm s$.

**Étape 6 — Conclusion.**
$$\boxed{T(t)=T_0+\frac Ph\big(1-e^{-t/\tau}\big),\quad\tau=\frac Ch=200\ \mathrm s,\quad T(\tau)-T_0\approx6{,}3\ \mathrm K,\quad t_{1\%}=\tau\ln100\approx15\ \mathrm{min}}$$""",
r"""$\tau\dot T+T=T_0+P/h$ avec $\tau=C/h=200$ s ; $T=T_0+\frac Ph(1-e^{-t/\tau})$ ; $T(\tau)-T_0\approx6{,}3$ K ; 1 % au bout de $\tau\ln100\approx920$ s.""")
src(CCINP + " Le rapport du jury Centrale-Supélec 2025 insiste : définir le système et l'intervalle de temps avant tout bilan.", 'CCINP')

# ------------------------------------------------------------------ 2. Deux condensateurs
ex('n-pc-deuxcond', P, 'Électrocinétique', 1, 'Partage de charge entre deux condensateurs', 20, r"""
Un condensateur de capacité $C_0$, chargé ($q_0=Q$), est relié à $t=0$, par l'intermédiaire d'une résistance $R$, à un condensateur de capacité $C_1$ initialement déchargé ($q_1=0$).

1. Quelle grandeur se conserve ? En déduire les charges finales $q_0(\infty)$ et $q_1(\infty)$.
2. Établir l'équation différentielle vérifiée par $q_1(t)$ et la résoudre. Tracer $q_0$ et $q_1$ sur un même graphique.
3. Calculer l'énergie dissipée dans la résistance. Dépend-elle de $R$ ?

On donne $C_0=1{,}0\ \mu\mathrm F$, $C_1=2{,}0\ \mu\mathrm F$, $Q=1{,}0\times10^{-4}\ \mathrm C$, $R=1{,}0\ \mathrm{k\Omega}$.
""", r"""Les armatures reliées entre elles forment un conducteur isolé : la charge totale $q_0+q_1$ se conserve.""",
r"""Dans l'état final, plus de courant, donc les deux tensions sont égales.""",
r"""Loi des mailles : $\frac{q_0}{C_0}=Ri+\frac{q_1}{C_1}$ avec $i=\dot q_1$ et $q_0=Q-q_1$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Circuit série fermé $C_0$–$R$–$C_1$ : la charge quitte $C_0$ pour $C_1$ jusqu'à égalité des tensions. On attend un régime transitoire du premier ordre.

**Étape 2 — Rappels du cours.**

> **Loi — Conservation de la charge.** Pour un ensemble de conducteurs isolés, la charge totale est constante.

> **Relation — Condensateur.** $u=q/C$, $i=\mathrm dq/\mathrm dt$ ; énergie stockée $\frac{q^2}{2C}$.

**Étape 3 — Stratégie.** État final par conservation et égalité des tensions ; loi des mailles ; bilan d'énergie entre états initial et final.

**Étape 4 — Résolution détaillée.**

**4.1 État final.** $q_0+q_1=Q$ et $\frac{q_0}{C_0}=\frac{q_1}{C_1}$ donnent
$$q_0(\infty)=\frac{C_0}{C_0+C_1}Q\approx3{,}3\times10^{-5}\ \mathrm C,\qquad q_1(\infty)=\frac{C_1}{C_0+C_1}Q\approx6{,}7\times10^{-5}\ \mathrm C.$$

**4.2 Évolution.** $\frac{Q-q_1}{C_0}=R\dot q_1+\frac{q_1}{C_1}$, soit $\tau\dot q_1+q_1=q_1(\infty)$ avec
$$\tau=R\,\frac{C_0C_1}{C_0+C_1}\approx0{,}67\ \mathrm{ms}.$$
Donc $q_1(t)=q_1(\infty)\big(1-e^{-t/\tau}\big)$ et $q_0(t)=Q-q_1(t)$ : $q_0$ décroît de $Q$ vers $Q/3$, $q_1$ croît de $0$ vers $2Q/3$, avec la même constante de temps.

**4.3 Énergie.** $E_i=\frac{Q^2}{2C_0}=5{,}0\ \mathrm{mJ}$ ; $E_f=\frac{Q^2}{2(C_0+C_1)}\approx1{,}7\ \mathrm{mJ}$. Énergie dissipée par effet Joule :
$$W_J=E_i-E_f=\frac{Q^2}{2C_0}\cdot\frac{C_1}{C_0+C_1}\approx3{,}3\ \mathrm{mJ},$$
indépendante de $R$ : $R$ ne fixe que la durée du transfert.

**Étape 5 — Vérification.**

> **Vérification — Calcul direct.** $i=\dot q_1=\frac{q_1(\infty)}\tau e^{-t/\tau}$ et $\int_0^\infty Ri^2\,\mathrm dt=\frac{Rq_1(\infty)^2}{2\tau}$, qui redonne $\frac{Q^2C_1}{2C_0(C_0+C_1)}$.

**Étape 6 — Conclusion.**
$$\boxed{q_1(\infty)=\tfrac{C_1}{C_0+C_1}Q,\quad\tau=R\tfrac{C_0C_1}{C_0+C_1},\quad W_J=\tfrac{Q^2}{2C_0}\tfrac{C_1}{C_0+C_1}\ \text{(indépendant de }R)}$$""",
r"""Charge conservée et tensions égales : $q_0=Q/3$, $q_1=2Q/3$ ; $\tau=RC_0C_1/(C_0+C_1)\approx0{,}67$ ms ; $W_J=\frac{Q^2}{2C_0}\frac{C_1}{C_0+C_1}\approx3{,}3$ mJ, indépendant de $R$.""")
src(CCINP, 'CCINP')

# ------------------------------------------------------------------ 3. Force centrale élastique
ex('n-pc-elastique', P, 'Mécanique', 1, 'Force centrale élastique et potentiel effectif', 20, r"""
Un point matériel $M$ de masse $m$, astreint à se déplacer dans un plan horizontal $(Oxy)$ sans frottement, est soumis à la force $\vec F=-k\,\overrightarrow{OM}$ ($k>0$). On utilise les coordonnées polaires $(r,\theta)$.

1. Montrer que le moment cinétique en $O$ se conserve, et l'exprimer à l'aide de la constante $\mathcal C=r^2\dot\theta$. Conséquences ?
2. Montrer que l'énergie mécanique se conserve et l'écrire en fonction de $r$, $\dot r$, $\mathcal C$, $m$, $k$. Définir l'énergie potentielle effective et tracer son allure.
3. Montrer que, pour $\mathcal C\neq0$, le mouvement se fait entre deux valeurs $r_1\le r\le r_2$. À quelle condition est-il circulaire ? Quelle est alors sa période ?
4. Résoudre en coordonnées cartésiennes et décrire la trajectoire.
""", r"""La force est centrale : son moment en $O$ est nul.""",
r"""$E_m=\frac12m\dot r^2+\frac{m\mathcal C^2}{2r^2}+\frac12kr^2$ ; le terme du milieu est l'énergie cinétique orthoradiale.""",
r"""En cartésiennes, $m\ddot x=-kx$ et $m\ddot y=-ky$ : deux oscillateurs de même pulsation.""",
r"""**Étape 1 — Analyse de l'énoncé.** Force centrale et conservative : deux intégrales premières (moment cinétique, énergie), qui ramènent le problème à une dimension avec un potentiel effectif.

**Étape 2 — Rappels du cours.**

> **Théorème — Moment cinétique.** $\frac{\mathrm d\vec L_O}{\mathrm dt}=\overrightarrow{OM}\wedge\vec F$ ; il est nul pour une force centrale, et le mouvement est plan avec loi des aires $r^2\dot\theta=\mathcal C$.

> **Définition — Énergie potentielle effective.** $E_{p,\mathrm{eff}}(r)=\frac{m\mathcal C^2}{2r^2}+E_p(r)$, avec $E_m=\frac12m\dot r^2+E_{p,\mathrm{eff}}(r)\ge E_{p,\mathrm{eff}}(r)$.

**Étape 3 — Stratégie.** Intégrales premières, étude graphique de $E_{p,\mathrm{eff}}$, puis résolution directe en cartésiennes.

**Étape 4 — Résolution détaillée.**

**4.1 Moment cinétique.** $\overrightarrow{OM}\wedge\vec F=-k\,\overrightarrow{OM}\wedge\overrightarrow{OM}=\vec0$ : $\vec L_O=m r^2\dot\theta\,\vec e_z=m\mathcal C\,\vec e_z$ est constant. $\theta$ est monotone (si $\mathcal C\neq0$) et l'aire balayée croît uniformément.

**4.2 Énergie.** $\vec F=-\overrightarrow{\mathrm{grad}}\big(\frac12kr^2\big)$ est conservative et la réaction du plan ne travaille pas : $E_m$ se conserve. Avec $v^2=\dot r^2+r^2\dot\theta^2=\dot r^2+\frac{\mathcal C^2}{r^2}$ :
$$E_m=\frac12m\dot r^2+\underbrace{\frac{m\mathcal C^2}{2r^2}+\frac12kr^2}_{E_{p,\mathrm{eff}}(r)}.$$
$E_{p,\mathrm{eff}}$ tend vers $+\infty$ en $0$ et en $+\infty$, avec un minimum unique en $r_0=\big(\frac{m\mathcal C^2}k\big)^{1/4}$.

**4.3 Bornes.** $\frac12m\dot r^2=E_m-E_{p,\mathrm{eff}}(r)\ge0$ impose $E_{p,\mathrm{eff}}(r)\le E_m$ : un intervalle $[r_1,r_2]$ autour de $r_0$ (état lié). Mouvement circulaire si $E_m=E_{p,\mathrm{eff}}(r_0)$, avec $r=r_0$ ; alors $m r_0\dot\theta^2=kr_0$, soit $\dot\theta=\omega_0=\sqrt{k/m}$ et $T=2\pi\sqrt{m/k}$.

**4.4 Trajectoire.** $x=A\cos(\omega_0t+\varphi)$, $y=B\cos(\omega_0t+\psi)$ : la trajectoire est une ellipse **centrée** en $O$ (et non de foyer $O$ comme pour la gravitation), parcourue en $T=2\pi\sqrt{m/k}$ quelles que soient les conditions initiales.

**Étape 5 — Vérification.**

> **Vérification — Cohérence.** Sur l'ellipse $x=a\cos\omega_0t$, $y=b\sin\omega_0t$ : $r_1=b$, $r_2=a$ (si $b<a$) et $\mathcal C=ab\,\omega_0$. On vérifie $E_{p,\mathrm{eff}}(a)=E_{p,\mathrm{eff}}(b)=\frac12k(a^2+b^2)=E_m$.

**Étape 6 — Conclusion.**
$$\boxed{E_m=\tfrac12m\dot r^2+\tfrac{m\mathcal C^2}{2r^2}+\tfrac12kr^2;\ r_1\le r\le r_2;\ \text{ellipse centrée en }O,\ T=2\pi\sqrt{m/k}}$$""",
r"""Force centrale : $r^2\dot\theta=\mathcal C$ constant ; $E_{p,\mathrm{eff}}=\frac{m\mathcal C^2}{2r^2}+\frac12kr^2$ a un minimum en $r_0=(m\mathcal C^2/k)^{1/4}$, d'où $r_1\le r\le r_2$ ; trajectoire elliptique centrée en $O$, période $2\pi\sqrt{m/k}$.""")
src(CCINP, 'CCINP')

# ------------------------------------------------------------------ 4. Identification d'un filtre
ex('n-pc-filtre-id', P, 'Électrocinétique', 2, 'Identifier un filtre RLC à partir de mesures', 25, r"""
Un quadripôle est formé de deux dipôles $D_1$ (entre l'entrée et la sortie) et $D_2$ (aux bornes de la sortie), qui contiennent à eux deux une résistance $R$, une bobine idéale $L$ et un condensateur $C$, chacun pouvant être associé en série ou en parallèle. La sortie est ouverte.

1. On applique en entrée une tension continue $E=12\ \mathrm V$ ; un ampèremètre placé dans la maille d'entrée indique $I=12\ \mathrm{mA}$. Quelles configurations sont compatibles avec cette mesure ? Que vaut $R$ ?
2. L'expérience montre que le montage est un passe-bande. Parmi les configurations restantes, laquelle est-ce ? Justifier par une étude en basses et hautes fréquences.
3. Établir la fonction de transfert sous la forme $H=\dfrac{1}{1+jQ\big(\frac\omega{\omega_0}-\frac{\omega_0}\omega\big)}$.
4. On mesure $f_0=1{,}59\ \mathrm{kHz}$ et une bande passante à $-3\ \mathrm{dB}$ de largeur $\Delta f=159\ \mathrm{Hz}$. En déduire $L$ et $C$.
""", r"""En continu, un condensateur est un interrupteur ouvert et une bobine un fil : il faut un chemin de courant passant par $R$.""",
r"""Un passe-bande RLC classique : $L$ et $C$ en série dans $D_1$, sortie aux bornes de $R$ ($D_2$).""",
r"""Pour ce passe-bande, $\omega_0=1/\sqrt{LC}$ et $\Delta\omega=\omega_0/Q=R/L$.""",
r"""**Étape 1 — Analyse de l'énoncé.** On procède par élimination : la mesure en continu fixe la place de la résistance, l'étude asymptotique fixe la nature du filtre, la fonction de transfert donne les valeurs.

**Étape 2 — Rappels du cours.**

> **Propriété — Comportements limites.** En continu (et en BF), un condensateur se comporte comme un circuit ouvert, une bobine comme un fil ; en HF, c'est l'inverse.

> **Propriété — Passe-bande du second ordre.** $H=\frac{H_0}{1+jQ(x-1/x)}$ avec $x=\omega/\omega_0$ : bande passante à $-3\ \mathrm{dB}$ de largeur $\Delta\omega=\omega_0/Q$.

**Étape 3 — Stratégie.** Élimination par la mesure continue, choix par les limites BF/HF (comme le recommande le rapport Centrale 2025), puis pont diviseur de tension (légitime : sortie ouverte, même courant dans $D_1$ et $D_2$).

**Étape 4 — Résolution détaillée.**

**4.1 Mesure continue.** La sortie étant ouverte, le même courant traverse $D_1$ puis $D_2$. En continu, $C$ est un circuit ouvert et $L$ un fil. Un courant non nul impose qu'aucun condensateur ne soit seul en série sur le trajet ; un courant fini impose que ce trajet contienne la résistance. Donc $R=E/I=1{,}0\ \mathrm{k\Omega}$, et l'on écarte toutes les configurations où $C$ coupe le trajet continu (par exemple $L$ et $C$ en série dans $D_1$, avec $R$ en $D_2$).

**4.2 Passe-bande.** Il faut une sortie nulle en BF et en HF. Avec $D_1=L$ et $C$ en série et $D_2=R$ : en BF, $C$ ouvert, $i=0$, $s=0$ ; en HF, $L$ ouverte, $s=0$ ; entre les deux, à la résonance $LC\omega^2=1$, l'impédance de $D_1$ s'annule et $s=e$. Mais en continu ce montage ne laisse passer aucun courant ! La mesure (12 mA) impose donc l'autre passe-bande : $D_1=R$ et $D_2=L\parallel C$ ($L$ et $C$ en parallèle en sortie). En continu, $L$ court-circuite la sortie : $I=E/R=12\ \mathrm{mA}$, compatible. En BF, $L$ court-circuite $D_2$ ; en HF, $C$ le court-circuite : $s\to0$ dans les deux cas.

**4.3 Fonction de transfert.** Admittance de $D_2$ : $Y=jC\omega+\frac1{jL\omega}$. Pont diviseur :
$$H=\frac{1/Y}{R+1/Y}=\frac1{1+RY}=\frac1{1+jR\big(C\omega-\frac1{L\omega}\big)}=\frac1{1+jQ\big(\frac\omega{\omega_0}-\frac{\omega_0}\omega\big)},$$
avec $\omega_0=\frac1{\sqrt{LC}}$ et $Q=RC\omega_0=R\sqrt{C/L}$.

**4.4 Valeurs.** $\Delta\omega=\frac{\omega_0}Q=\frac1{RC}$, d'où $C=\frac1{2\pi R\,\Delta f}=1{,}0\times10^{-6}\ \mathrm F$ ; puis $L=\frac1{C\omega_0^2}=\frac1{C(2\pi f_0)^2}\approx10\ \mathrm{mH}$. Facteur de qualité $Q=f_0/\Delta f=10$.

**Étape 5 — Vérification.**

> **Vérification — Ordres de grandeur.** $\frac1{2\pi\sqrt{LC}}=\frac1{2\pi\sqrt{10^{-2}\times10^{-6}}}\approx1{,}59\ \mathrm{kHz}$ et $Q=R\sqrt{C/L}=10^3\sqrt{10^{-4}}=10$ : cohérent avec les mesures.

**Étape 6 — Conclusion.**
$$\boxed{D_1=R=1{,}0\ \mathrm{k\Omega},\ D_2=L\parallel C;\quad\omega_0=\tfrac1{\sqrt{LC}},\ Q=R\sqrt{C/L};\quad C\approx1{,}0\ \mu\mathrm F,\ L\approx10\ \mathrm{mH}}$$""",
r"""En continu, 12 V / 12 mA donne $R=1$ kΩ en série et $L$ assurant le passage du courant ; le passe-bande compatible est $D_1=R$, $D_2=L\parallel C$ ; $H=1/[1+jQ(x-1/x)]$, $Q=R\sqrt{C/L}$, $\Delta\omega=1/(RC)$ : $C\approx1{,}0\ \mu$F, $L\approx10$ mH.""")
src(CCINP + " Démarche (analyse basses et hautes fréquences avant tout calcul) recommandée par le rapport du jury Centrale-Supélec 2025.", 'CCINP')

# ------------------------------------------------------------------ 5. Décollage sur un quart de cercle
ex('n-pc-decollage', P, 'Mécanique', 1, 'Glissade sur un dôme : où décolle-t-on ?', 20, r"""
Un point matériel de masse $m$ glisse sans frottement sur la face extérieure d'un quart de cercle vertical de rayon $R$ et de centre $O$ (un dôme). Sa position est repérée par l'angle $\theta$ entre la verticale ascendante et $\overrightarrow{OM}$. Il est lâché sans vitesse en $\theta_0$, avec $0<\theta_0\ll1$.

1. Justifier la conservation de l'énergie mécanique. En déduire $\dot\theta^2$ en fonction de $\theta$, tant que le contact dure.
2. Exprimer la réaction normale $N(\theta)$. En déduire l'angle $\theta_d$ de décollage. Que vaut-il pour $\theta_0\to0$ ?
3. Pour $\theta_0\ll1$, montrer que la durée avant le décollage est de l'ordre de $\sqrt{R/g}\ \ln\big(\frac{\text{cte}}{\theta_0}\big)$ : elle diverge quand $\theta_0\to0$. Interpréter.
""", r"""La réaction est normale au support, donc perpendiculaire à la vitesse : elle ne travaille pas.""",
r"""Projette le principe fondamental sur la direction radiale : $-mR\dot\theta^2=N-mg\cos\theta$.""",
r"""Au voisinage du sommet, linéarise : $\ddot\theta\approx\frac gR\theta$, dont la solution partant du repos est $\theta_0\operatorname{ch}(t\sqrt{g/R})$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Mouvement circulaire tant que le contact existe ; le contact cesse quand la réaction normale s'annule. L'énergie donne la vitesse, le principe fondamental la réaction.

**Étape 2 — Rappels du cours.**

> **Théorème — Énergie mécanique.** Si les seules forces qui travaillent sont conservatives, $E_m$ se conserve.

> **Formule — Accélération en mouvement circulaire.** $\vec a=-R\dot\theta^2\vec e_r+R\ddot\theta\,\vec e_\theta$.

**Étape 3 — Stratégie.** Énergie → $\dot\theta^2(\theta)$ ; projection radiale → $N(\theta)$ ; condition $N=0$ ; puis linéarisation pour estimer la durée.

**Étape 4 — Résolution détaillée.**

**4.1 Énergie.** Le poids est conservatif, la réaction ne travaille pas : $\frac12mR^2\dot\theta^2+mgR\cos\theta=mgR\cos\theta_0$, donc
$$\dot\theta^2=\frac{2g}R(\cos\theta_0-\cos\theta).$$

**4.2 Décollage.** Sur $\vec e_r$ (sortant) : $-mR\dot\theta^2=N-mg\cos\theta$, d'où
$$N=mg(3\cos\theta-2\cos\theta_0).$$
$N$ s'annule pour $\cos\theta_d=\frac23\cos\theta_0$. Pour $\theta_0\to0$ : $\cos\theta_d=\frac23$, $\theta_d\approx48{,}2^\circ$, inférieur à $90^\circ$ : le point quitte bien le quart de cercle.

**4.3 Durée.** Près du sommet, $\sin\theta\approx\theta$ et $mR\ddot\theta=mg\sin\theta$ donne $\ddot\theta\approx\frac gR\theta$, soit $\theta(t)\approx\theta_0\operatorname{ch}(t/\tau)$ avec $\tau=\sqrt{R/g}$. Cette approximation vaut jusqu'à des angles d'ordre 1 ; la durée pour atteindre un angle $\Theta\sim1$ vérifie $\theta_0\operatorname{ch}(t/\tau)\approx\frac{\theta_0}2e^{t/\tau}\sim\Theta$, soit $t\approx\tau\ln\frac{2\Theta}{\theta_0}$. La fin du mouvement jusqu'à $\theta_d$ ne dure qu'un temps d'ordre $\tau$. Donc $t_d\approx\sqrt{R/g}\,\ln\frac{\text{cte}}{\theta_0}$, qui diverge (lentement) quand $\theta_0\to0$ : le sommet est une position d'équilibre instable, et partir exactement du sommet sans vitesse, c'est y rester.

**Étape 5 — Vérification.**

> **Vérification — Ordre de grandeur.** Pour $R=1\ \mathrm m$ et $\theta_0=10^{-3}$ : $\tau\approx0{,}32\ \mathrm s$ et $\ln(2/10^{-3})\approx7{,}6$, soit environ 2,4 s avant de quitter la zone du sommet : on « attend » longtemps puis tout va très vite.

**Étape 6 — Conclusion.**
$$\boxed{\dot\theta^2=\tfrac{2g}R(\cos\theta_0-\cos\theta),\quad N=mg(3\cos\theta-2\cos\theta_0),\quad\cos\theta_d=\tfrac23\cos\theta_0,\quad t_d\sim\sqrt{\tfrac Rg}\ln\tfrac{\text{cte}}{\theta_0}}$$""",
r"""$\dot\theta^2=\frac{2g}R(\cos\theta_0-\cos\theta)$ ; $N=mg(3\cos\theta-2\cos\theta_0)$ ; décollage pour $\cos\theta_d=\frac23\cos\theta_0$ (48° si $\theta_0\to0$) ; durée $\sim\sqrt{R/g}\ln(\text{cte}/\theta_0)$ car le sommet est un équilibre instable.""")
src(CCINP, 'CCINP')

# ------------------------------------------------------------------ 6. Barre entre deux sources finies
ex('n-pc-barre2sources', P, 'Diffusion thermique', 2, 'Barre entre deux corps de capacités finies', 25, r"""
Une barre de longueur $L$, de section $S$, de conductivité thermique $\lambda$ et de capacité thermique négligeable, relie deux corps de capacités thermiques $C_1$ et $C_2$, de températures initiales $T_{10}>T_{20}$. L'ensemble est isolé de l'extérieur.

1. Justifier que, dans la barre, le profil de température est affine à chaque instant, et exprimer la puissance $\Phi$ qui la traverse à l'aide de la résistance thermique $R_{th}=\frac L{\lambda S}$.
2. Établir les équations d'évolution de $T_1(t)$ et $T_2(t)$, puis les résoudre. Donner la température finale et la constante de temps.
3. Calculer la variation d'entropie de l'ensemble entre $t=0$ et $t\to\infty$, et vérifier son signe.
""", r"""Capacité de la barre négligeable : elle n'accumule pas d'énergie, le flux est le même dans chaque section (régime quasi stationnaire).""",
r"""$C_1\dot T_1=-\Phi$ et $C_2\dot T_2=+\Phi$ avec $\Phi=\frac{T_1-T_2}{R_{th}}$ ; étudie la différence $\theta=T_1-T_2$.""",
r"""Pour l'entropie, chaque corps est une phase condensée : $\Delta S_i=C_i\ln\frac{T_f}{T_{i0}}$ ; la barre ne contribue pas.""",
r"""**Étape 1 — Analyse de l'énoncé.** Deux réservoirs de capacités finies échangent de la chaleur à travers une résistance thermique : l'écart de température relaxe exponentiellement, et le processus crée de l'entropie.

**Étape 2 — Rappels du cours.**

> **Définition — Résistance thermique.** En régime stationnaire, sans source, le flux $\Phi$ est uniforme et $T_1-T_2=R_{th}\Phi$ avec $R_{th}=\frac L{\lambda S}$ pour une barre (le rapport Centrale 2025 recommande cette méthode).

> **Formule — Entropie d'une phase condensée.** $\Delta S=C\ln\frac{T_f}{T_i}$.

**Étape 3 — Stratégie.** Quasi-stationnarité dans la barre ; bilans sur chaque corps ; équation sur l'écart $\theta$ ; bilan d'entropie entre états extrêmes.

**Étape 4 — Résolution détaillée.**

**4.1 Barre.** Sa capacité étant négligeable, son énergie ne varie pas : le flux entrant égale le flux sortant dans toute tranche, donc $\Phi$ est uniforme, $\frac{\mathrm d^2T}{\mathrm dx^2}=0$ et le profil est affine. $\Phi=\frac{T_1-T_2}{R_{th}}$.

**4.2 Évolution.** $C_1\dot T_1=-\Phi$, $C_2\dot T_2=\Phi$. La somme donne $C_1T_1+C_2T_2=$ cte, d'où $T_f=\frac{C_1T_{10}+C_2T_{20}}{C_1+C_2}$. Pour $\theta=T_1-T_2$ :
$$\dot\theta=-\frac{\theta}{R_{th}}\Big(\frac1{C_1}+\frac1{C_2}\Big)=-\frac\theta\tau,\qquad\tau=R_{th}\frac{C_1C_2}{C_1+C_2}.$$
Donc $\theta=(T_{10}-T_{20})e^{-t/\tau}$, puis $T_1=T_f+\frac{C_2}{C_1+C_2}\theta$ et $T_2=T_f-\frac{C_1}{C_1+C_2}\theta$.

**4.3 Entropie.** La barre revient à son état (capacité nulle) :
$$\Delta S=C_1\ln\frac{T_f}{T_{10}}+C_2\ln\frac{T_f}{T_{20}}.$$
Le système est isolé, donc $\Delta S=S_{\text{créée}}$. Par concavité du logarithme, $\ln T_f=\ln\big(\frac{C_1T_{10}+C_2T_{20}}{C_1+C_2}\big)\ge\frac{C_1\ln T_{10}+C_2\ln T_{20}}{C_1+C_2}$, d'où $\Delta S\ge0$, avec égalité seulement si $T_{10}=T_{20}$.

**Étape 5 — Vérification.**

> **Vérification — Cas limite.** Si $C_2\to\infty$ (thermostat), $T_f\to T_{20}$ et $\tau\to R_{th}C_1$ : on retrouve la relaxation d'un corps relié à un thermostat. Exemple : $C_1=C_2=C$, $T_{10}=400\ \mathrm K$, $T_{20}=200\ \mathrm K$ : $T_f=300\ \mathrm K$ et $\Delta S=C\ln\frac{300^2}{400\times200}\approx0{,}118\,C>0$.

**Étape 6 — Conclusion.**
$$\boxed{T_f=\tfrac{C_1T_{10}+C_2T_{20}}{C_1+C_2},\ \ \tau=\tfrac{L}{\lambda S}\tfrac{C_1C_2}{C_1+C_2},\ \ \Delta S=C_1\ln\tfrac{T_f}{T_{10}}+C_2\ln\tfrac{T_f}{T_{20}}>0}$$""",
r"""Profil affine, $\Phi=(T_1-T_2)/R_{th}$ ; $T_f$ barycentrique, l'écart décroît en $e^{-t/\tau}$ avec $\tau=R_{th}C_1C_2/(C_1+C_2)$ ; $\Delta S=C_1\ln\frac{T_f}{T_{10}}+C_2\ln\frac{T_f}{T_{20}}>0$ (concavité du logarithme).""")
src(CCINP, 'CCINP')

# ------------------------------------------------------------------ 7. Condensateur dont on écarte les armatures
ex('n-pc-armatures', P, 'Électrocinétique', 2, 'On écarte brusquement les armatures', 25, r"""
Un condensateur de capacité $C$, en série avec une résistance $R$, est chargé par un générateur idéal de tension $E_0$.

1. Établir la loi $i(t)$ pendant la charge, puis faire le bilan d'énergie de la charge complète.
2. Le régime permanent étant atteint, on écarte brusquement les armatures (en un temps très court devant $RC$) : la capacité passe de $C$ à $C_1<C$. Quelle grandeur est continue lors de cette opération ? Quel travail l'opérateur a-t-il fourni ?
3. On prend cet instant comme origine des temps. Déterminer $i(t)$ ensuite, et le sens du courant.
4. Faire le bilan énergétique de cette seconde phase : énergie reçue par le générateur, variation d'énergie du condensateur, énergie dissipée par effet Joule.
""", r"""Pendant l'écartement, aucun courant fini n'a le temps de transporter de la charge : $q$ est continue.""",
r"""Après l'écartement, la tension $q/C_1$ dépasse $E_0$ : le condensateur se décharge partiellement dans le générateur.""",
r"""Énergie fournie par le générateur : $E_0\,\Delta q$ ; elle est négative si la charge retourne vers lui.""",
r"""**Étape 1 — Analyse de l'énoncé.** Un circuit RC classique, puis une perturbation mécanique instantanée qui modifie la capacité à charge constante, suivie d'un nouveau régime transitoire.

**Étape 2 — Rappels du cours.**

> **Relation — Condensateur.** $q=Cu$, énergie $\frac{q^2}{2C}$ ; la charge est une fonction continue du temps (courant fini).

> **Bilan — Charge d'un condensateur.** Le générateur fournit $CE_0^2$ ; la moitié est stockée, l'autre moitié dissipée, quel que soit $R$.

**Étape 3 — Stratégie.** Équations du premier ordre ; continuité de $q$ ; bilans entre états d'équilibre.

**Étape 4 — Résolution détaillée.**

**4.1 Charge.** $i=\frac{E_0}Re^{-t/RC}$. Le générateur fournit $W_g=E_0\cdot CE_0=CE_0^2$, le condensateur stocke $\frac12CE_0^2$, la résistance dissipe $\frac12CE_0^2$.

**4.2 Écartement.** La charge reste $q_0=CE_0$. L'énergie passe de $\frac{q_0^2}{2C}$ à $\frac{q_0^2}{2C_1}$ ; il n'y a pas de dissipation pendant un temps aussi bref, donc l'opérateur fournit
$$W_{op}=\frac{C^2E_0^2}2\Big(\frac1{C_1}-\frac1C\Big)>0$$
(il faut tirer sur des armatures qui s'attirent).

**4.3 Nouveau transitoire.** Pour $t>0$ : $E_0=Ri+\frac q{C_1}$ avec $q(0)=CE_0$, donc
$$q(t)=C_1E_0+(C-C_1)E_0e^{-t/RC_1},\qquad i=\dot q=-\frac{(C-C_1)E_0}{RC_1}e^{-t/RC_1}<0.$$
Le courant circule en sens inverse de la charge : le condensateur restitue la charge $(C-C_1)E_0$ au générateur.

**4.4 Bilan de la seconde phase.** Énergie fournie par le générateur : $W_g=E_0\Delta q=-(C-C_1)E_0^2<0$ (il reçoit de l'énergie). Variation d'énergie du condensateur : $\Delta E_c=\frac12C_1E_0^2-\frac{C^2E_0^2}{2C_1}$. Effet Joule : $W_J=W_g-\Delta E_c=\frac{E_0^2(C-C_1)^2}{2C_1}>0$.

**Étape 5 — Vérification.**

> **Vérification — Calcul direct.** $\int_0^\infty Ri^2\,\mathrm dt=R\frac{(C-C_1)^2E_0^2}{R^2C_1^2}\cdot\frac{RC_1}2=\frac{(C-C_1)^2E_0^2}{2C_1}$ : identique. Et si $C_1=C$, rien ne se passe.

**Étape 6 — Conclusion.**
$$\boxed{i=-\tfrac{(C-C_1)E_0}{RC_1}e^{-t/RC_1};\quad W_{op}=\tfrac{C^2E_0^2}2\big(\tfrac1{C_1}-\tfrac1C\big);\quad W_J=\tfrac{E_0^2(C-C_1)^2}{2C_1}}$$""",
r"""Charge : $i=\frac{E_0}Re^{-t/RC}$, moitié stockée, moitié dissipée. Écartement à charge constante : $W_{op}=\frac{C^2E_0^2}2(\frac1{C_1}-\frac1C)$. Ensuite $i=-\frac{(C-C_1)E_0}{RC_1}e^{-t/RC_1}$ (retour vers le générateur), $W_g=-(C-C_1)E_0^2$, $W_J=\frac{E_0^2(C-C_1)^2}{2C_1}$.""")
src(CCINP, 'CCINP')

# ------------------------------------------------------------------ 8. Pompe à chaleur de Carnot
ex('n-pc-pac', P, 'Thermodynamique', 1, 'Pompe à chaleur : cycle de Carnot d’un gaz parfait', 20, r"""
Une pompe à chaleur fait décrire à $n$ moles de gaz parfait ($\gamma$ constant) le cycle réversible suivant, entre une source froide $T_f$ et une source chaude $T_c$ :
- compression isentropique de $(V_1,T_f)$ à $(V_2,T_c)$ ;
- compression isotherme à $T_c$ de $V_2$ à $V_3$ ;
- détente isentropique de $(V_3,T_c)$ à $(V_4,T_f)$ ;
- détente isotherme à $T_f$ de $V_4$ à $V_1$.

1. Expliquer à l'aide d'un schéma le principe d'une pompe à chaleur. Tracer le cycle en diagramme de Clapeyron $(V,P)$ et en diagramme entropique $(S,T)$, et préciser le sens de parcours.
2. Montrer que $\dfrac{V_1V_3}{V_2V_4}=1$.
3. Calculer les transferts thermiques $Q_c$ et $Q_f$, puis l'efficacité. Faire le bilan entropique du cycle.
4. Application : $T_f=275\ \mathrm K$ (sol en hiver), $T_c=318\ \mathrm K$ (eau de chauffage). Efficacité maximale ?
""", r"""Le fluide prélève de la chaleur à la source froide et en cède à la source chaude, grâce à un travail reçu.""",
r"""Loi de Laplace sur les isentropiques : $TV^{\gamma-1}=$ cte.""",
r"""Sur une isotherme d'un gaz parfait, $\Delta U=0$ donc $Q=-W=nRT\ln\frac{V_{\text{fin}}}{V_{\text{déb}}}$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Cycle de Carnot parcouru en sens récepteur : on calcule les transferts sur les isothermes, et l'on vérifie que l'efficacité vaut la limite de Carnot.

**Étape 2 — Rappels du cours.**

> **Loi — Laplace.** Pour une transformation adiabatique réversible d'un gaz parfait à $\gamma$ constant, $TV^{\gamma-1}$ est constant.

> **Principe — Second principe pour un cycle ditherme.** $\frac{Q_c}{T_c}+\frac{Q_f}{T_f}+S_{\text{créée}}=0$, avec $S_{\text{créée}}=0$ si le cycle est réversible.

**Étape 3 — Stratégie.** Laplace sur les deux isentropiques ; transferts isothermes ; premier et second principes sur le cycle.

**Étape 4 — Résolution détaillée.**

**4.1 Principe et diagrammes.** Le fluide reçoit $Q_f>0$ de la source froide, un travail $W>0$, et cède $|Q_c|=Q_f+W$ à la source chaude (le logement). En $(V,P)$, le cycle est parcouru dans le sens trigonométrique (aire = travail reçu). En $(S,T)$, c'est un rectangle : deux isothermes horizontales, deux isentropiques verticales, parcouru lui aussi dans le sens trigonométrique.

**4.2 Volumes.** $T_fV_1^{\gamma-1}=T_cV_2^{\gamma-1}$ et $T_cV_3^{\gamma-1}=T_fV_4^{\gamma-1}$. En divisant : $\big(\frac{V_1}{V_4}\big)^{\gamma-1}=\big(\frac{V_2}{V_3}\big)^{\gamma-1}$, donc $\frac{V_1V_3}{V_2V_4}=1$.

**4.3 Transferts et efficacité.** $Q_c=nRT_c\ln\frac{V_3}{V_2}<0$ (compression) ; $Q_f=nRT_f\ln\frac{V_1}{V_4}=nRT_f\ln\frac{V_2}{V_3}>0$. Donc $\frac{Q_c}{T_c}+\frac{Q_f}{T_f}=0$ : pas d'entropie créée (cycle réversible). Efficacité :
$$e=\frac{-Q_c}{W}=\frac{-Q_c}{-Q_c-Q_f}=\frac{T_c}{T_c-T_f}.$$

**4.4 Application.** $e=\frac{318}{43}\approx7{,}4$ : au mieux, 1 kWh électrique fournit 7,4 kWh de chaleur. Les pompes réelles atteignent 3 à 4.

**Étape 5 — Vérification.**

> **Vérification — Cohérence.** $e>1$ toujours, et $e\to\infty$ quand $T_c\to T_f$ : sans écart de température, il ne faut aucun travail pour « déplacer » de la chaleur.

**Étape 6 — Conclusion.**
$$\boxed{\tfrac{V_1V_3}{V_2V_4}=1,\quad\tfrac{Q_c}{T_c}+\tfrac{Q_f}{T_f}=0,\quad e=\tfrac{T_c}{T_c-T_f}\approx7{,}4}$$""",
r"""Laplace sur les isentropiques donne $V_1V_3=V_2V_4$ ; $Q_c=nRT_c\ln\frac{V_3}{V_2}$, $Q_f=nRT_f\ln\frac{V_2}{V_3}$, entropie créée nulle ; $e=\frac{T_c}{T_c-T_f}\approx7{,}4$.""")
src(CCINP + " Le rapport du jury Centrale-Supélec 2025 note que l'établissement de l'efficacité de Carnot est souvent trop laborieux.", 'CCINP')

# ------------------------------------------------------------------ 9. Étoile double et trous d'Young
ex('n-pc-etoiledouble', P, 'Optique ondulatoire', 2, 'Mesurer l’écart d’une étoile double avec des trous d’Young', 25, r"""
On observe une étoile double, formée de deux étoiles $S_1$ (sur l'axe) et $S_2$ (vue sous l'angle $\varepsilon$ faible), à travers deux trous d'Young distants de $a$ placés devant une lentille convergente de focale $f'$ ; on observe dans le plan focal image, à l'abscisse $x$. Les deux étoiles ont la même intensité et la même longueur d'onde $\lambda$.

1. Exprimer l'éclairement $\mathcal E_1(x)$ dû à $S_1$ seule, puis $\mathcal E_2(x)$ dû à $S_2$ seule.
2. Les deux étoiles peuvent-elles interférer entre elles ? En déduire l'éclairement total et le contraste $V(a)$.
3. Montrer qu'en faisant varier $a$ on peut mesurer $\varepsilon$. Pour $\lambda=550\ \mathrm{nm}$ et $\varepsilon=5{,}0\ \mu\mathrm{rad}$, pour quelle valeur de $a$ le contraste s'annule-t-il pour la première fois ?
""", r"""Pour une onde plane arrivant sous l'angle $\varepsilon$, la différence de marche entre les deux trous contient un terme $a\varepsilon$ en plus de $ax/f'$.""",
r"""Deux étoiles distinctes sont des sources incohérentes : on ajoute les éclairements, pas les amplitudes.""",
r"""Somme de deux cosinus : $\cos p+\cos q=2\cos\frac{p+q}2\cos\frac{p-q}2$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Chaque étoile donne son propre système de franges ; les deux systèmes sont décalés, et leur superposition incohérente brouille les franges pour certaines valeurs de $a$. C'est le principe de l'interféromètre stellaire de Fizeau et Michelson.

**Étape 2 — Rappels du cours.**

> **Formule — Interférences à deux ondes.** $\mathcal E=2\mathcal E_0\big(1+\cos\frac{2\pi\delta}\lambda\big)$ pour deux ondes cohérentes de même intensité.

> **Propriété — Sources incohérentes.** Les éclairements dus à des sources incohérentes s'ajoutent.

**Étape 3 — Stratégie.** Différence de marche pour chaque étoile, somme des éclairements, factorisation pour lire le contraste.

**Étape 4 — Résolution détaillée.**

**4.1 Chaque étoile.** Pour $S_1$ (sur l'axe), $\delta_1=\frac{ax}{f'}$ et $\mathcal E_1=2\mathcal E_0\big(1+\cos\frac{2\pi ax}{\lambda f'}\big)$. Pour $S_2$, l'onde plane incidente ajoute la différence de marche $a\varepsilon$ avant les trous (au signe près selon l'orientation) : $\delta_2=\frac{ax}{f'}-a\varepsilon$ et $\mathcal E_2=2\mathcal E_0\big(1+\cos\frac{2\pi(ax/f'-a\varepsilon)}\lambda\big)$.

**4.2 Total.** Les étoiles sont incohérentes :
$$\mathcal E=4\mathcal E_0\Big[1+\cos\Big(\frac{\pi a\varepsilon}\lambda\Big)\cos\Big(\frac{2\pi}\lambda\Big(\frac{ax}{f'}-\frac{a\varepsilon}2\Big)\Big)\Big],\qquad V=\Big|\cos\frac{\pi a\varepsilon}\lambda\Big|.$$

**4.3 Mesure.** Partant de $a$ petit ($V\approx1$), on écarte les trous jusqu'à la première disparition des franges : $\frac{\pi a\varepsilon}\lambda=\frac\pi2$, soit $a_1=\frac\lambda{2\varepsilon}$, ce qui donne $\varepsilon=\frac\lambda{2a_1}$. Numériquement, $a_1=\frac{550\times10^{-9}}{2\times5{,}0\times10^{-6}}=5{,}5\ \mathrm{cm}$.

**Étape 5 — Vérification.**

> **Vérification — Ordre de grandeur.** $5\ \mu\mathrm{rad}\approx1''$ d'arc, ordre de grandeur de la séparation d'étoiles doubles serrées ; une base de quelques centimètres suffit, ce qui rend la méthode pratique.

**Étape 6 — Conclusion.**
$$\boxed{V(a)=\Big|\cos\frac{\pi a\varepsilon}\lambda\Big|,\quad\text{première annulation pour }a_1=\frac\lambda{2\varepsilon}=5{,}5\ \mathrm{cm}}$$""",
r"""$\delta_2=\delta_1-a\varepsilon$ ; sources incohérentes : $\mathcal E=4\mathcal E_0[1+\cos\frac{\pi a\varepsilon}\lambda\cos(\dots)]$, $V=|\cos\frac{\pi a\varepsilon}\lambda|$ ; première annulation pour $a=\frac\lambda{2\varepsilon}=5{,}5$ cm, d'où $\varepsilon$.""")
src(CCINP, 'CCINP')
