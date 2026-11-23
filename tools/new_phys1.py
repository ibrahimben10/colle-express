# Physique — niveau CCINP (programme MPSI / MP, exercices courts)
from newlib import ex
P = 'Physique'

ex('n-p1-rc', P, 'Électrocinétique', 1, "Charge d'un condensateur : bilan d'énergie", 15, r"""
Un générateur idéal de tension $E$ charge, à travers un résistor $R$, un condensateur de capacité $C$ initialement déchargé. On ferme l'interrupteur à $t=0$.

On donne : $E=10\ \mathrm V$, $R=1{,}0\ \mathrm{k\Omega}$, $C=100\ \mathrm{\mu F}$.

1. Établir l'équation différentielle vérifiée par la tension $u_C(t)$ aux bornes du condensateur, puis la résoudre.
2. Calculer la constante de temps $\tau$ et la durée au bout de laquelle le condensateur est chargé à $99\ \%$.
3. Calculer l'énergie fournie par le générateur, l'énergie stockée dans le condensateur et l'énergie dissipée par effet Joule pendant toute la charge.
4. Le rendement de la charge dépend-il de $R$ ? Commenter.
""",
r"Loi des mailles : $E=Ri+u_C$ avec $i=C\,\dfrac{\mathrm du_C}{\mathrm dt}$.",
r"Solution : $u_C=E\left(1-e^{-t/\tau}\right)$ ; résous $e^{-t/\tau}=0{,}01$.",
r"Énergie du générateur : $\int_0^\infty Ei\,\mathrm dt=E\,q_{\text{finale}}=CE^2$ ; celle du condensateur : $\tfrac12CE^2$.",
r"""
**1.** Loi des mailles avec $i=C\dot u_C$ : $RC\,\dfrac{\mathrm du_C}{\mathrm dt}+u_C=E$. Avec $u_C(0)=0$ (continuité de la tension aux bornes d'un condensateur) :
$$u_C(t)=E\left(1-e^{-t/\tau}\right),\qquad \tau=RC.$$

**2.** $\tau=RC=10^3\times10^{-4}=0{,}10\ \mathrm s$. On veut $e^{-t/\tau}=0{,}01$, soit $t_{99}=\tau\ln100\approx4{,}6\,\tau\approx0{,}46\ \mathrm s$.

**3.** Le générateur fournit $W_g=\int_0^\infty Ei\,\mathrm dt=E\,q_\infty=CE^2=10\ \mathrm{mJ}$. Le condensateur stocke $W_C=\tfrac12CE^2=5{,}0\ \mathrm{mJ}$. Le reste est dissipé : $W_J=W_g-W_C=\tfrac12CE^2=5{,}0\ \mathrm{mJ}$ (on le retrouve en calculant $\int_0^\infty Ri^2\,\mathrm dt$ avec $i=\frac ER e^{-t/\tau}$ : $\frac{E^2}R\cdot\frac\tau2=\frac12CE^2$).

**4.** Le rendement vaut $W_C/W_g=50\ \%$ quelle que soit $R$ : $R$ ne fixe que la durée de la charge. Même avec $R\to0$, la moitié de l'énergie est perdue (rayonnement, résistance des fils). Pour faire mieux, il faut charger progressivement (tension d'alimentation en rampe).
""", r"$u_C=E(1-e^{-t/RC})$ ; $\tau=0{,}10$ s ; $W_g=10$ mJ, $W_C=W_J=5{,}0$ mJ ; rendement 50 %.")

ex('n-p1-rlc', P, 'Électrocinétique', 1, 'Régime libre du circuit RLC série', 15, r"""
Un condensateur chargé sous $U_0$ se décharge à $t=0$ dans une bobine idéale d'inductance $L$ en série avec un résistor $R$.

On donne : $L=10\ \mathrm{mH}$, $C=1{,}0\ \mathrm{\mu F}$, $R=20\ \Omega$.

1. Établir l'équation différentielle vérifiée par la charge $q(t)$ du condensateur et la mettre sous forme canonique en faisant apparaître $\omega_0$ et le facteur de qualité $Q$.
2. Calculer $\omega_0$ et $Q$. Quel est le régime ?
3. Calculer la pseudo-période $T$ et le rapport des amplitudes de deux maxima successifs de $q$.
4. Quelle valeur $R_c$ faudrait-il pour obtenir le régime critique ?
""",
r"Loi des mailles : $L\ddot q+R\dot q+\dfrac qC=0$ ; compare avec $\ddot q+\dfrac{\omega_0}Q\dot q+\omega_0^2q=0$.",
r"$\omega_0=1/\sqrt{LC}$ et $Q=\dfrac1R\sqrt{\dfrac LC}$. Régime pseudo-périodique si $Q>1/2$.",
r"$q(t)=e^{-\omega_0t/(2Q)}\left(A\cos\Omega t+B\sin\Omega t\right)$ avec $\Omega=\omega_0\sqrt{1-\frac1{4Q^2}}$ : entre deux maxima, l'exponentielle est multipliée par $e^{-\omega_0T/(2Q)}$.",
r"""
**1.** $u_L+u_R+u_C=0$ avec $i=\dot q$ : $L\ddot q+R\dot q+q/C=0$, soit
$$\ddot q+\frac{\omega_0}Q\dot q+\omega_0^2q=0,\qquad\omega_0=\frac1{\sqrt{LC}},\quad Q=\frac{L\omega_0}R=\frac1R\sqrt{\frac LC}.$$

**2.** $\omega_0=1/\sqrt{10^{-2}\times10^{-6}}=1{,}0\times10^4\ \mathrm{rad\,s^{-1}}$ ($f_0\approx1{,}6$ kHz) et $Q=\frac1{20}\sqrt{10^4}=5{,}0$. Comme $Q>1/2$, le discriminant est négatif : régime **pseudo-périodique**.

**3.** $\Omega=\omega_0\sqrt{1-\frac1{4Q^2}}=\omega_0\sqrt{0{,}99}$, donc $T=\dfrac{2\pi}\Omega\approx6{,}3\times10^{-4}\ \mathrm s$ (très proche de $T_0$). Le rapport de deux maxima successifs vaut $e^{-\omega_0T/(2Q)}=e^{-\pi/(Q\sqrt{1-1/(4Q^2)})}\approx e^{-0{,}63}\approx0{,}53$ : le décrément logarithmique est $\delta\approx\pi/Q\approx0{,}63$. On observe environ $Q\approx5$ oscillations nettes.

**4.** Régime critique : $Q=1/2$, soit $R_c=2\sqrt{L/C}=2\times100=200\ \Omega$.
""", r"$\omega_0=1{,}0\times10^4$ rad/s, $Q=5$ ; $T\approx0{,}63$ ms ; rapport $\approx0{,}53$ ; $R_c=200\ \Omega$.")

ex('n-p1-passebas', P, 'Électrocinétique', 1, 'Filtre RC et signal composite', 20, r"""
Un filtre est formé d'un résistor $R$ en série avec un condensateur $C$ ; la sortie $s$ est la tension aux bornes du condensateur, en sortie ouverte.

On donne : $R=1{,}0\ \mathrm{k\Omega}$, $C=100\ \mathrm{nF}$.

1. Établir la fonction de transfert $\underline H=\underline s/\underline e$. Nature du filtre, fréquence de coupure $f_c$.
2. Tracer l'allure du diagramme de Bode en gain (asymptotes). Quel comportement le filtre a-t-il pour $f\gg f_c$ ?
3. L'entrée est $e(t)=2{,}0+1{,}0\cos(2\pi f_1t)+1{,}0\cos(2\pi f_2t)$ (en volts) avec $f_1=100\ \mathrm{Hz}$ et $f_2=20\ \mathrm{kHz}$. Donner $s(t)$.
""",
r"Pont diviseur de tension en complexes : $\underline H=\dfrac{1/(jC\omega)}{R+1/(jC\omega)}$.",
r"$\underline H=\dfrac1{1+jf/f_c}$ avec $f_c=\dfrac1{2\pi RC}$ ; pour $f\gg f_c$, $\underline H\approx\dfrac{f_c}{jf}$.",
r"Linéarité : traite chaque composante séparément ; gain $|\underline H|$ et déphasage $-\arctan(f/f_c)$ à chaque fréquence, la composante continue passe avec $H(0)=1$.",
r"""
**1.** Pont diviseur : $\underline H=\dfrac1{1+jRC\omega}=\dfrac1{1+jf/f_c}$ avec $f_c=\dfrac1{2\pi RC}=\dfrac1{2\pi\times10^{-4}}\approx1{,}6\ \mathrm{kHz}$. Filtre **passe-bas du premier ordre** ($H\to1$ en BF, $H\to0$ en HF).

**2.** $G_{dB}=-10\log\left(1+(f/f_c)^2\right)$ : asymptote horizontale $0$ dB pour $f\ll f_c$, asymptote de pente $-20$ dB/décade pour $f\gg f_c$, les deux se coupant en $f_c$ (gain réel $-3$ dB). Pour $f\gg f_c$, $\underline H\approx\frac1{jRC\omega}$ : le filtre est **intégrateur**, $s\approx\frac1{RC}\int e\,\mathrm dt$.

**3.** Par linéarité :
- composante continue : $H(0)=1$, elle passe : $2{,}0$ V ;
- $f_1=100$ Hz : $f_1/f_c=0{,}063$, $|H|=0{,}998$, $\varphi=-3{,}6^\circ$ ;
- $f_2=20$ kHz : $f_2/f_c=12{,}6$, $|H|=1/\sqrt{1+158}\approx0{,}079$, $\varphi=-\arctan12{,}6\approx-85^\circ$.

$$s(t)\approx2{,}0+1{,}0\cos(2\pi f_1t-0{,}063)+0{,}079\cos(2\pi f_2t-1{,}49)\ \ (\mathrm V).$$
Le filtre élimine pratiquement la composante haute fréquence : c'est le principe du lissage d'une tension « bruitée ».
""", r"$f_c=1{,}6$ kHz ; $s\approx2{,}0+1{,}0\cos(2\pi f_1t)+0{,}079\cos(2\pi f_2t-85^\circ)$.")

ex('n-p1-passebande', P, 'Électrocinétique', 1, 'Filtre passe-bande RLC', 20, r"""
Un circuit RLC série est alimenté par une tension sinusoïdale $e(t)$ de pulsation $\omega$ ; la sortie est la tension $s$ aux bornes du résistor.

On donne : $L=0{,}10\ \mathrm H$, $C=0{,}10\ \mathrm{\mu F}$, $R=100\ \Omega$.

1. Montrer que $\underline H=\dfrac{1}{1+jQ\left(x-\frac1x\right)}$ avec $x=\omega/\omega_0$ ; exprimer $\omega_0$ et $Q$.
2. Calculer $f_0$ et $Q$.
3. Déterminer la bande passante à $-3$ dB et calculer sa largeur $\Delta f$.
4. Que valent le gain et le déphasage à la résonance ? Interpréter physiquement.
""",
r"Pont diviseur : $\underline H=\dfrac R{R+jL\omega+\frac1{jC\omega}}$ ; divise par $R$.",
r"$\dfrac{L\omega}R=Q\dfrac\omega{\omega_0}$ et $\dfrac1{RC\omega}=Q\dfrac{\omega_0}\omega$ avec $Q=\dfrac{L\omega_0}R$.",
r"$|\underline H|=1/\sqrt2\iff Q\left|x-\frac1x\right|=1$ : les deux racines positives vérifient $x_2-x_1=1/Q$.",
r"""
**1.** $\underline H=\dfrac R{R+j\left(L\omega-\frac1{C\omega}\right)}=\dfrac1{1+j\left(\frac{L\omega}R-\frac1{RC\omega}\right)}$. Avec $\omega_0=1/\sqrt{LC}$ et $Q=\dfrac{L\omega_0}R=\dfrac1{RC\omega_0}$, on obtient bien $\underline H=\dfrac1{1+jQ(x-1/x)}$.

**2.** $\omega_0=1/\sqrt{10^{-1}\times10^{-7}}=1{,}0\times10^4\ \mathrm{rad\,s^{-1}}$, soit $f_0\approx1{,}6$ kHz ; $Q=\dfrac1R\sqrt{\dfrac LC}=\dfrac{1000}{100}=10$.

**3.** $|\underline H|=1/\sqrt2$ pour $Q(x-1/x)=\pm1$, i.e. $x^2\mp x/Q-1=0$. Les racines positives sont $x_{1,2}=\mp\frac1{2Q}+\sqrt{1+\frac1{4Q^2}}$, d'où $x_2-x_1=1/Q$ : $\Delta\omega=\omega_0/Q$ et $\Delta f=f_0/Q\approx160\ \mathrm{Hz}$.

**4.** En $x=1$ : $\underline H=1$, gain $0$ dB et déphasage nul. Les impédances de $L$ et $C$ se compensent ($jL\omega_0+\frac1{jC\omega_0}=0$) : le circuit se comporte comme $R$ seule, le courant est maximal et en phase avec $e$. Plus $Q$ est grand, plus le filtre est sélectif.
""", r"$f_0\approx1{,}6$ kHz, $Q=10$, $\Delta f=f_0/Q\approx160$ Hz ; à la résonance $H=1$.")

ex('n-p1-corde', P, 'Ondes mécaniques', 1, 'Corde de guitare', 15, r"""
La corde la plus grave d'une guitare, de longueur vibrante $L=65\ \mathrm{cm}$ et de masse linéique $\mu=5{,}0\ \mathrm{g\,m^{-1}}$, est fixée à ses deux extrémités. Elle émet un mi grave de fréquence fondamentale $f_1=82\ \mathrm{Hz}$.

On rappelle que la célérité des ondes transversales sur une corde de tension $T$ est $c=\sqrt{T/\mu}$.

1. Déterminer les fréquences propres de la corde. En déduire $c$ puis la tension $T$.
2. Où faut-il appuyer (frette) pour obtenir le la de fréquence $110\ \mathrm{Hz}$ sur cette corde ?
3. On pince la corde exactement en son milieu. Quels harmoniques sont absents du son ? Justifier.
""",
r"Modes propres : la corde contient un nombre entier de demi-longueurs d'onde, $L=n\lambda_n/2$.",
r"$f_n=n\dfrac c{2L}$ donc $c=2Lf_1$ ; puis $T=\mu c^2$. Pour la frette, la longueur vibrante $\ell$ vérifie $f=c/(2\ell)$.",
r"Un pincement au milieu donne une déformation initiale symétrique par rapport au milieu : les modes qui y ont un nœud ne sont pas excités.",
r"""
**1.** Avec deux extrémités fixes, $\sin(k_nL)=0$ : $L=n\dfrac{\lambda_n}2$, d'où $f_n=n\dfrac c{2L}=nf_1$. Donc $c=2Lf_1=2\times0{,}65\times82\approx107\ \mathrm{m\,s^{-1}}$ et
$$T=\mu c^2=5{,}0\times10^{-3}\times107^2\approx57\ \mathrm N.$$

**2.** La célérité ne change pas : $\ell=\dfrac c{2f}=\dfrac{107}{220}\approx0{,}48\ \mathrm m$. On appuie à $L-\ell\approx17\ \mathrm{cm}$ du sillet (c'est la 5ᵉ frette : $\ell/L=82/110=2^{-5/12}$).

**3.** Le mode $n$ a pour profil $\sin(n\pi x/L)$ ; en $x=L/2$ il vaut $\sin(n\pi/2)$, nul pour $n$ pair. La déformation initiale, symétrique par rapport au milieu, ne se décompose que sur les modes symétriques ($n$ impair) : les **harmoniques pairs sont absents**. Le son est plus « creux » qu'en pinçant près du chevalet.
""", r"$f_n=nf_1$ ; $c\approx107$ m/s, $T\approx57$ N ; frette à 17 cm ; harmoniques pairs absents.")

ex('n-p1-ultrasons', P, 'Ondes mécaniques', 1, 'Interférences de deux émetteurs ultrasonores', 15, r"""
Deux émetteurs ultrasonores $S_1$ et $S_2$, distants de $a=5{,}0\ \mathrm{cm}$, émettent en phase une onde sinusoïdale de fréquence $f=40\ \mathrm{kHz}$. Un récepteur se déplace sur une droite parallèle à $S_1S_2$, à la distance $D=1{,}0\ \mathrm m$.

On donne : célérité du son dans l'air $c=340\ \mathrm{m\,s^{-1}}$.

1. Calculer la longueur d'onde.
2. Exprimer la différence de marche $\delta$ en un point d'abscisse $x$ de la droite (avec $|x|\ll D$). En déduire la position des maxima d'amplitude et l'interfrange.
3. Dans combien de directions (sans hypothèse $|x|\ll D$) observe-t-on un maximum d'amplitude ?
""",
r"$\lambda=c/f$.",
r"Comme pour les trous d'Young : $\delta=S_2M-S_1M\approx\dfrac{ax}D$. Maximum si $\delta=p\lambda$, $p\in\mathbb Z$.",
r"Dans la direction $\theta$, $\delta=a\sin\theta$ : les maxima vérifient $|p|\lambda\le a$, compte les entiers $p$.",
r"""
**1.** $\lambda=c/f=340/(4{,}0\times10^4)=8{,}5\ \mathrm{mm}$.

**2.** Avec $S_{1,2}$ en $y=\mp a/2$ : $S_2M-S_1M\approx\dfrac{ax}D$ (développement au premier ordre). Les ondes arrivent en phase si $\delta=p\lambda$ : maxima en $x_p=p\dfrac{\lambda D}a$, et l'interfrange vaut $i=\dfrac{\lambda D}a=\dfrac{8{,}5\times10^{-3}\times1{,}0}{5{,}0\times10^{-2}}\approx17\ \mathrm{cm}$.

**3.** Loin des sources, dans la direction $\theta$ : $\delta=a\sin\theta$. Un maximum demande $\sin\theta=p\lambda/a$, possible si $|p|\le a/\lambda=5{,}9$ : $p\in\{-5,\dots,5\}$, soit **11 directions** de maximum.
""", r"$\lambda=8{,}5$ mm ; $\delta\approx ax/D$, $i=\lambda D/a\approx17$ cm ; 11 directions.")

ex('n-p1-fente', P, 'Optique ondulatoire', 1, "Diffraction par une fente : mesurer une largeur", 10, r"""
Un laser hélium-néon ($\lambda=633\ \mathrm{nm}$) éclaire une fente fine de largeur $a$. On observe la figure de diffraction sur un écran à $D=2{,}0\ \mathrm m$.

1. Rappeler la relation donnant le demi-angle $\theta$ de la tache centrale. Exprimer sa largeur $\ell$ sur l'écran.
2. Pour $a=0{,}10\ \mathrm{mm}$, calculer $\ell$.
3. Avec une autre fente, on mesure $\ell=1{,}3\ \mathrm{cm}$. Que vaut sa largeur ?
4. Pourquoi n'observe-t-on aucune diffraction notable de la lumière par une fenêtre ?
""",
r"La première annulation de l'éclairement a lieu pour $\sin\theta=\lambda/a$.",
r"Petits angles : $\ell=2D\tan\theta\approx\dfrac{2\lambda D}a$.",
r"Compare $\lambda/a$ pour $a\sim1$ m : l'ouverture angulaire est de l'ordre de $10^{-7}$ rad.",
r"""
**1.** La tache centrale est limitée par les premières annulations : $\sin\theta=\lambda/a$, soit $\theta\approx\lambda/a$ pour $a\gg\lambda$. Sur l'écran : $\ell\approx2D\theta=\dfrac{2\lambda D}a$.

**2.** $\ell=\dfrac{2\times633\times10^{-9}\times2{,}0}{1{,}0\times10^{-4}}\approx2{,}5\ \mathrm{cm}$.

**3.** $a=\dfrac{2\lambda D}\ell=\dfrac{2{,}53\times10^{-6}}{1{,}3\times10^{-2}}\approx0{,}19\ \mathrm{mm}$ (deux fois plus large que la première : tache deux fois plus étroite).

**4.** Pour $a\sim1$ m, $\theta\sim\lambda/a\sim6\times10^{-7}$ rad : l'élargissement est imperceptible. La diffraction n'est notable que pour des ouvertures de quelques centaines de longueurs d'onde au plus ; c'est ce qui justifie l'approximation de l'optique géométrique.
""", r"$\ell=2\lambda D/a\approx2{,}5$ cm ; $a\approx0{,}19$ mm.")

ex('n-p1-projecteur', P, 'Optique géométrique', 1, 'Projecteur de diapositives', 15, r"""
Un projecteur utilise une lentille mince convergente de distance focale $f'=10\ \mathrm{cm}$. On veut former, sur un écran placé à $3{,}0\ \mathrm m$ de la lentille, l'image nette d'une diapositive de format $24\times36\ \mathrm{mm}$.

1. À quelle distance de la lentille faut-il placer la diapositive ? Dans quel sens ?
2. Calculer le grandissement et les dimensions de l'image.
3. Montrer qu'une lentille convergente ne peut donner d'un objet réel une image réelle que si la distance objet-écran est au moins $4f'$.
""",
r"Relation de conjugaison de Descartes : $\dfrac1{\overline{OA'}}-\dfrac1{\overline{OA}}=\dfrac1{f'}$ avec $\overline{OA'}=+3{,}0$ m.",
r"Grandissement $\gamma=\overline{OA'}/\overline{OA}$ ; le signe dit si l'image est renversée.",
r"Pose $D=\overline{OA'}-\overline{OA}$ et $p=\overline{OA}<0$ : obtiens une équation du second degré en $p$ et écris que son discriminant est positif.",
r"""
**1.** $\dfrac1{\overline{OA}}=\dfrac1{\overline{OA'}}-\dfrac1{f'}=\dfrac1{3{,}0}-\dfrac1{0{,}10}\approx-9{,}67\ \mathrm{m^{-1}}$, donc $\overline{OA}\approx-10{,}3\ \mathrm{cm}$ : la diapositive est juste en avant du foyer objet. L'image étant renversée, on place la diapositive **à l'envers** pour que l'image soit droite.

**2.** $\gamma=\dfrac{\overline{OA'}}{\overline{OA}}=\dfrac{3{,}0}{-0{,}103}\approx-29$. Image de $0{,}70\times1{,}04\ \mathrm m$.

**3.** Avec $p=\overline{OA}<0$ et $p'=p+D$ : $\dfrac1{p+D}-\dfrac1p=\dfrac1{f'}$, soit $p^2+Dp+Df'=0$. Il faut un discriminant positif : $D^2-4Df'\ge0$, donc $D\ge4f'$. Pour $D=4f'$, $p=-2f'$ : c'est la configuration objet-image la plus courte, avec $\gamma=-1$.
""", r"$\overline{OA}\approx-10{,}3$ cm ; $\gamma\approx-29$, image $0{,}70\times1{,}04$ m ; $D\ge4f'$.")

ex('n-p1-lunette', P, 'Optique géométrique', 1, 'Lunette astronomique', 20, r"""
Une lunette astronomique afocale est formée d'un objectif $L_1$ (focale $f'_1=1{,}0\ \mathrm m$, diamètre $D_1=10\ \mathrm{cm}$) et d'un oculaire $L_2$ (focale $f'_2=5{,}0\ \mathrm{cm}$).

1. Pourquoi la lunette doit-elle être afocale pour un observateur à l'œil normal ? Quelle est sa longueur ?
2. Établir l'expression du grossissement $G=\alpha'/\alpha$ et le calculer. La Lune a un diamètre apparent de $0{,}50^\circ$ : sous quel angle la voit-on dans la lunette ?
3. Le cercle oculaire est l'image de la monture de l'objectif par l'oculaire. Déterminer sa position et son diamètre. Pourquoi y placer l'œil ?
""",
r"L'œil normal observe sans fatigue une image à l'infini ; l'objet aussi est à l'infini. Le foyer image de $L_1$ doit donc coïncider avec le foyer objet de $L_2$.",
r"Un rayon passant par le foyer commun : $\tan\alpha=\dfrac{\overline{A'B'}}{f'_1}$ et $\tan\alpha'=-\dfrac{\overline{A'B'}}{f'_2}$ (attention aux signes).",
r"Conjugue $O_1$ par $L_2$ avec $\overline{O_2O_1}=-(f'_1+f'_2)$ ; le grandissement donne le diamètre.",
r"""
**1.** L'objet est à l'infini et l'œil normal veut une image à l'infini : le système doit être afocal, donc $F'_1=F_2$. Longueur : $O_1O_2=f'_1+f'_2=1{,}05\ \mathrm m$.

**2.** L'image intermédiaire $A'B'$ se forme dans le plan focal commun. $\alpha\approx\overline{A'B'}/f'_1$ et l'oculaire en donne une image à l'infini sous $\alpha'\approx-\overline{A'B'}/f'_2$, d'où
$$G=\frac{\alpha'}\alpha=-\frac{f'_1}{f'_2}=-20.$$
La Lune est vue sous $20\times0{,}50^\circ=10^\circ$ (image renversée, sans gêne en astronomie).

**3.** Conjugaison par $L_2$ avec $\overline{O_2O_1}=-1{,}05\ \mathrm m$ : $\dfrac1{\overline{O_2C}}=\dfrac1{0{,}05}-\dfrac1{1{,}05}=19{,}05\ \mathrm{m^{-1}}$, soit $\overline{O_2C}\approx5{,}25\ \mathrm{cm}$, juste après le foyer image de l'oculaire. Grandissement $\overline{O_2C}/\overline{O_2O_1}=-0{,}05$ : diamètre $10\times0{,}05=0{,}50\ \mathrm{cm}$. Tous les rayons entrés dans l'objectif passent par ce disque : l'œil (pupille $\sim5$ mm) y reçoit toute la lumière collectée et voit le champ le plus large.
""", r"Longueur 1,05 m ; $G=-f'_1/f'_2=-20$, Lune vue sous $10^\circ$ ; cercle oculaire à 5,25 cm, diamètre 5 mm.")

ex('n-p1-prisme', P, 'Optique géométrique', 1, 'Minimum de déviation du prisme', 20, r"""
Un prisme d'angle au sommet $A=60^\circ$, d'indice $n=1{,}50$, est placé dans l'air. Un rayon monochromatique entre par une face sous l'incidence $i$ et ressort par l'autre sous l'angle $i'$ ; on note $r$ et $r'$ les angles de réfraction intérieurs.

1. Établir les relations $\sin i=n\sin r$, $\sin i'=n\sin r'$, $r+r'=A$ et $D=i+i'-A$.
2. On admet que la déviation est minimale quand le trajet est symétrique ($i=i'$). Exprimer $n$ en fonction de $A$ et de la déviation minimale $D_m$, puis calculer $D_m$.
3. À quelle condition sur $A$ un rayon peut-il émerger du prisme ?
""",
r"Le triangle formé par les deux normales et l'arête donne $r+r'=A$ ; la déviation est la somme des déviations à chaque face, $(i-r)+(i'-r')$.",
r"Au minimum : $r=r'=A/2$ et $i=(A+D_m)/2$, d'où $n=\dfrac{\sin\frac{A+D_m}2}{\sin\frac A2}$.",
r"Il faut $r'\le\arcsin(1/n)$ (pas de réflexion totale) avec $r\le\arcsin(1/n)$ aussi : donc $A=r+r'\le2\arcsin(1/n)$.",
r"""
**1.** Lois de Descartes sur chaque face : $\sin i=n\sin r$ et $n\sin r'=\sin i'$. Les normales aux faces font entre elles l'angle $\pi-A$ ; dans le triangle qu'elles forment avec le rayon intérieur, $r+r'+(\pi-A)=\pi$, donc $r+r'=A$. La déviation totale est $D=(i-r)+(i'-r')=i+i'-A$.

**2.** Au minimum, $r=r'=A/2$ et $i=i'=(A+D_m)/2$, d'où $n=\dfrac{\sin\frac{A+D_m}2}{\sin\frac A2}$. Numériquement : $\sin\frac{A+D_m}2=1{,}50\times\sin30^\circ=0{,}75$, donc $\frac{A+D_m}2=48{,}6^\circ$ et $D_m\approx37{,}2^\circ$. Cette méthode permet de mesurer précisément un indice (et sa variation avec $\lambda$).

**3.** Il faut $r'\le\ell=\arcsin(1/n)=41{,}8^\circ$ ; comme $r\le\ell$ aussi (réfraction à l'entrée), $A=r+r'\le2\ell=83{,}6^\circ$. Pour $A=60^\circ$, il faut de plus $r\ge A-\ell=18{,}2^\circ$, soit $i\ge\arcsin(1{,}5\sin18{,}2^\circ)\approx27{,}9^\circ$.
""", r"$D=i+i'-A$ ; $D_m\approx37{,}2^\circ$ ; émergence possible si $A\le2\arcsin(1/n)=83{,}6^\circ$.")

ex('n-p1-photo', P, 'Mécanique quantique', 1, 'Effet photoélectrique sur le zinc', 15, r"""
Le travail d'extraction du zinc vaut $W=4{,}3\ \mathrm{eV}$.

On donne : $h=6{,}63\times10^{-34}\ \mathrm{J\,s}$, $c=3{,}00\times10^8\ \mathrm{m\,s^{-1}}$, $e=1{,}60\times10^{-19}\ \mathrm C$, $m_e=9{,}11\times10^{-31}\ \mathrm{kg}$ ; on pourra utiliser $hc\approx1240\ \mathrm{eV\,nm}$.

1. Calculer la longueur d'onde seuil $\lambda_0$. Dans quel domaine se situe-t-elle ?
2. On éclaire la plaque par une lampe à vapeur de mercure ($\lambda=254\ \mathrm{nm}$). Calculer l'énergie cinétique maximale des électrons émis, leur vitesse maximale et le potentiel d'arrêt.
3. Une lampe de bureau très puissante, de lumière visible, ne produit aucun effet. Pourquoi ce fait contredit-il la théorie ondulatoire classique ?
""",
r"Un photon d'énergie $h\nu$ peut arracher un électron si $h\nu\ge W$ : $\lambda_0=hc/W$.",
r"Bilan d'Einstein : $E_{c,\max}=\dfrac{hc}\lambda-W$, puis $v=\sqrt{2E_c/m_e}$ ; le potentiel d'arrêt vérifie $eU_0=E_{c,\max}$.",
r"Classiquement, l'énergie reçue augmente avec l'intensité, quelle que soit la fréquence. Ici, chaque photon visible a une énergie inférieure à $W$.",
r"""
**1.** $\lambda_0=\dfrac{hc}W=\dfrac{1240}{4{,}3}\approx288\ \mathrm{nm}$ : **ultraviolet**.

**2.** $E_{c,\max}=\dfrac{1240}{254}-4{,}3=4{,}88-4{,}3\approx0{,}58\ \mathrm{eV}=9{,}3\times10^{-20}\ \mathrm J$. Vitesse : $v=\sqrt{2E_c/m_e}\approx4{,}5\times10^5\ \mathrm{m\,s^{-1}}$. Potentiel d'arrêt : $U_0=E_{c,\max}/e\approx0{,}58\ \mathrm V$.

**3.** Un photon visible ($\lambda>400$ nm) transporte au plus $3{,}1$ eV $<W$ : aucun électron n'est arraché, quel que soit le nombre de photons (l'intensité ne change que leur nombre). Dans le modèle ondulatoire classique, une onde assez intense finirait par fournir l'énergie nécessaire : l'existence d'un seuil en fréquence, indépendant de l'intensité, impose la quantification de l'énergie lumineuse.
""", r"$\lambda_0\approx288$ nm (UV) ; $E_c\approx0{,}58$ eV, $v\approx4{,}5\times10^5$ m/s, $U_0\approx0{,}58$ V.")

ex('n-p1-debroglie', P, 'Mécanique quantique', 1, 'Longueurs d’onde de de Broglie', 10, r"""
On donne : $h=6{,}63\times10^{-34}\ \mathrm{J\,s}$, $m_e=9{,}11\times10^{-31}\ \mathrm{kg}$, $m_n=1{,}67\times10^{-27}\ \mathrm{kg}$, $e=1{,}60\times10^{-19}\ \mathrm C$, $k_B=1{,}38\times10^{-23}\ \mathrm{J\,K^{-1}}$.

1. Calculer la longueur d'onde de de Broglie d'un électron accéléré sans vitesse initiale sous une tension $U=100\ \mathrm V$. Pourquoi peut-on l'utiliser pour étudier un cristal ?
2. Même question pour un neutron « thermique » d'énergie cinétique $k_BT$ à $T=300\ \mathrm K$.
3. Calculer la longueur d'onde d'une balle de tennis de $58\ \mathrm g$ lancée à $50\ \mathrm{m\,s^{-1}}$. Conclure.
""",
r"$\lambda=h/p$ ; l'énergie cinétique acquise est $eU$, donc $p=\sqrt{2m_eeU}$ (cas non relativiste).",
r"Pour le neutron : $p=\sqrt{2m_nk_BT}$.",
r"Compare chaque $\lambda$ à la taille des obstacles rencontrés : $0{,}1$–$0{,}5$ nm pour les distances interatomiques.",
r"""
**1.** $\lambda=\dfrac h{\sqrt{2m_eeU}}=\dfrac{6{,}63\times10^{-34}}{\sqrt{2\times9{,}11\times10^{-31}\times1{,}60\times10^{-17}}}\approx1{,}2\times10^{-10}\ \mathrm m$. C'est l'ordre des distances interatomiques : un cristal se comporte comme un réseau et diffracte les électrons (expérience de Davisson et Germer). $eU=100$ eV $\ll m_ec^2=511$ keV justifie le calcul non relativiste.

**2.** $\lambda=\dfrac h{\sqrt{2m_nk_BT}}=\dfrac{6{,}63\times10^{-34}}{\sqrt{2\times1{,}67\times10^{-27}\times4{,}14\times10^{-21}}}\approx1{,}8\times10^{-10}\ \mathrm m$ : même ordre de grandeur, d'où la diffraction de neutrons (sensible aux noyaux et au magnétisme).

**3.** $\lambda=\dfrac h{mv}=\dfrac{6{,}63\times10^{-34}}{2{,}9}\approx2\times10^{-34}\ \mathrm m$ : sans commune mesure avec toute taille physique. Les effets ondulatoires sont inobservables pour les objets macroscopiques.
""", r"Électron : $0{,}12$ nm ; neutron thermique : $0{,}18$ nm ; balle : $2\times10^{-34}$ m.")

ex('n-p1-puits', P, 'Mécanique quantique', 1, 'Électron confiné dans une molécule', 20, r"""
On modélise un électron délocalisé le long d'une chaîne moléculaire par une particule libre de masse $m_e$ confinée sur un segment $[0,L]$ par des parois infiniment hautes.

On donne : $L=0{,}50\ \mathrm{nm}$, $h=6{,}63\times10^{-34}\ \mathrm{J\,s}$, $m_e=9{,}11\times10^{-31}\ \mathrm{kg}$, $hc\approx1240\ \mathrm{eV\,nm}$.

1. Écrire l'équation de Schrödinger stationnaire dans le puits et les conditions aux limites. En déduire les fonctions d'onde normalisées et les énergies $E_n$.
2. Calculer $E_1$ en eV.
3. Quelle est la longueur d'onde du photon absorbé lors de la transition $1\to2$ ?
4. Retrouver l'ordre de grandeur de $E_1$ par l'inégalité de Heisenberg spatiale.
""",
r"Dans le puits : $-\dfrac{\hbar^2}{2m}\varphi''=E\varphi$, avec $\varphi(0)=\varphi(L)=0$ (continuité de la fonction d'onde).",
r"$\varphi_n=\sqrt{2/L}\sin(n\pi x/L)$ et $E_n=\dfrac{n^2h^2}{8mL^2}$.",
r"Transition $1\to2$ : $\Delta E=3E_1=hc/\lambda$. Pour Heisenberg : $\Delta x\sim L$, $\Delta p\gtrsim\hbar/L$, $E\sim\Delta p^2/(2m)$.",
r"""
**1.** Dans le puits, $\varphi''+k^2\varphi=0$ avec $k=\sqrt{2mE}/\hbar$, et $\varphi(0)=\varphi(L)=0$. Donc $\varphi=A\sin kx$ avec $kL=n\pi$ ($n\ge1$). Normalisation : $A=\sqrt{2/L}$. Énergies :
$$E_n=\frac{\hbar^2k_n^2}{2m}=\frac{n^2h^2}{8mL^2}.$$
L'énergie est quantifiée et le niveau fondamental n'est pas nul.

**2.** $E_1=\dfrac{(6{,}63\times10^{-34})^2}{8\times9{,}11\times10^{-31}\times(5{,}0\times10^{-10})^2}\approx2{,}4\times10^{-19}\ \mathrm J\approx1{,}5\ \mathrm{eV}$.

**3.** $\Delta E=E_2-E_1=3E_1\approx4{,}5$ eV, donc $\lambda=hc/\Delta E\approx275\ \mathrm{nm}$ (UV). Pour une chaîne plus longue, $\lambda\propto L^2$ augmente : les longues chaînes conjuguées (carotène) absorbent dans le visible et sont colorées.

**4.** $\Delta x\sim L$ donne $p\sim\Delta p\gtrsim\hbar/L$, d'où $E\sim\dfrac{\hbar^2}{2mL^2}\approx0{,}15$ eV. On retrouve l'ordre de grandeur (le facteur $\pi^2$ manque, ce qui est normal pour une estimation).
""", r"$E_n=n^2h^2/(8mL^2)$ ; $E_1\approx1{,}5$ eV ; $\lambda_{1\to2}\approx275$ nm.")

ex('n-p1-chute', P, 'Mécanique', 1, 'Chute avec frottements', 15, r"""
1. Une bille de masse $m=2{,}0\ \mathrm g$ tombe sans vitesse initiale dans un fluide qui exerce une force $-\alpha\vec v$ (on néglige la poussée d'Archimède), avec $\alpha=1{,}0\times10^{-2}\ \mathrm{kg\,s^{-1}}$.
(a) Établir et résoudre l'équation du mouvement. Faire apparaître une vitesse limite $v_\ell$ et un temps caractéristique $\tau$.
(b) Au bout de combien de temps la bille atteint-elle $95\ \%$ de $v_\ell$ ?
2. Un parachutiste de masse $m=80\ \mathrm{kg}$ (équipement compris) en chute libre subit une force de norme $kv^2$. Sa vitesse limite, bras écartés, est de $55\ \mathrm{m\,s^{-1}}$.
(a) Calculer $k$.
(b) Parachute ouvert, la vitesse limite tombe à $5{,}0\ \mathrm{m\,s^{-1}}$. De quel facteur $k$ a-t-il été multiplié ?

On prendra $g=9{,}8\ \mathrm{m\,s^{-2}}$.
""",
r"PFD projeté sur la verticale descendante : $m\dot v=mg-\alpha v$.",
r"$v(t)=v_\ell\left(1-e^{-t/\tau}\right)$ avec $\tau=m/\alpha$ et $v_\ell=mg/\alpha$ ; pour 95 % : $t=\tau\ln20\approx3\tau$.",
r"À la vitesse limite, la force de frottement compense le poids : $kv_\ell^2=mg$.",
r"""
**1.(a)** $m\dot v=mg-\alpha v$, soit $\dot v+v/\tau=g$ avec $\tau=m/\alpha$. Avec $v(0)=0$ :
$$v(t)=v_\ell\left(1-e^{-t/\tau}\right),\qquad v_\ell=\frac{mg}\alpha.$$
$\tau=0{,}20\ \mathrm s$ et $v_\ell=2{,}0\times10^{-3}\times9{,}8/10^{-2}\approx2{,}0\ \mathrm{m\,s^{-1}}$.

**1.(b)** $e^{-t/\tau}=0{,}05$ donne $t=\tau\ln20\approx3{,}0\,\tau\approx0{,}60\ \mathrm s$.

**2.(a)** Régime limite : $kv_\ell^2=mg$, donc $k=\dfrac{80\times9{,}8}{55^2}\approx0{,}26\ \mathrm{kg\,m^{-1}}$.

**2.(b)** $k\propto1/v_\ell^2$ : il est multiplié par $(55/5{,}0)^2\approx120$, ce qui correspond à une surface frontale bien plus grande (le coefficient $k=\frac12\rho C_xS$ croît avec $S$).
""", r"$v=v_\ell(1-e^{-t/\tau})$, $\tau=0{,}20$ s, $v_\ell=2{,}0$ m/s, 95 % en 0,60 s ; $k\approx0{,}26$ kg/m, facteur ≈ 120.")

ex('n-p1-geostat', P, 'Mécanique', 1, 'Satellite géostationnaire', 15, r"""
Un satellite de masse $m$ décrit une orbite circulaire dans le plan équatorial terrestre.

On donne : $\mathcal GM_T=3{,}99\times10^{14}\ \mathrm{m^3\,s^{-2}}$, $R_T=6{,}37\times10^3\ \mathrm{km}$, jour sidéral $T_s=86\,164\ \mathrm s$.

1. Montrer que le mouvement circulaire est uniforme et relier la vitesse $v$ au rayon $r$. En déduire la troisième loi de Kepler.
2. Un satellite géostationnaire reste à la verticale d'un même point de la Terre. Quelle doit être sa période ? Calculer son rayon, son altitude et sa vitesse.
3. Exprimer l'énergie mécanique du satellite sur une orbite circulaire. Quelle énergie minimale faut-il fournir à un satellite de $1{,}0$ tonne pour le faire passer d'une orbite basse ($r_1=R_T+300\ \mathrm{km}$) à l'orbite géostationnaire ?
""",
r"Dans la base de Frenet, l'accélération tangentielle est nulle (force centrale radiale) et $\dfrac{v^2}r=\dfrac{\mathcal GM_T}{r^2}$.",
r"$T=2\pi r/v$ donne $\dfrac{T^2}{r^3}=\dfrac{4\pi^2}{\mathcal GM_T}$ ; la période géostationnaire est le jour sidéral.",
r"Sur une orbite circulaire, $E_c=-E_p/2$, donc $E_m=-\dfrac{\mathcal GM_Tm}{2r}$.",
r"""
**1.** La force est radiale : $m\dot v=0$, le mouvement est uniforme, et $m\dfrac{v^2}r=\dfrac{\mathcal GM_Tm}{r^2}$, soit $v=\sqrt{\mathcal GM_T/r}$. Avec $T=2\pi r/v$ : $\dfrac{T^2}{r^3}=\dfrac{4\pi^2}{\mathcal GM_T}$.

**2.** Le satellite doit tourner avec la Terre dans le référentiel géocentrique : $T=T_s$. Donc
$$r=\left(\frac{\mathcal GM_TT_s^2}{4\pi^2}\right)^{1/3}\approx4{,}22\times10^7\ \mathrm m,$$
altitude $h\approx35\,800\ \mathrm{km}$, vitesse $v=2\pi r/T_s\approx3{,}07\ \mathrm{km\,s^{-1}}$.

**3.** $E_m=\tfrac12mv^2-\dfrac{\mathcal GM_Tm}r=-\dfrac{\mathcal GM_Tm}{2r}$. Énergie minimale à fournir :
$$\Delta E=\frac{\mathcal GM_Tm}2\left(\frac1{r_1}-\frac1{r_2}\right)=\frac{3{,}99\times10^{14}\times10^3}2\left(\frac1{6{,}67\times10^6}-\frac1{4{,}22\times10^7}\right)\approx2{,}5\times10^{10}\ \mathrm J.$$
""", r"$T^2/r^3=4\pi^2/(\mathcal GM_T)$ ; $r\approx42\,200$ km, $h\approx35\,800$ km, $v\approx3{,}07$ km/s ; $\Delta E\approx2{,}5\times10^{10}$ J.")

ex('n-p1-pendule', P, 'Mécanique', 1, 'Pendule simple lâché de haut', 15, r"""
Un pendule simple est formé d'une masse ponctuelle $m$ suspendue à un fil inextensible, de masse négligeable, de longueur $L=1{,}0\ \mathrm m$. On le lâche sans vitesse depuis l'angle $\theta_0=60^\circ$. On néglige les frottements et on prend $g=9{,}8\ \mathrm{m\,s^{-2}}$.

1. Calculer la vitesse de la masse au point le plus bas.
2. Calculer la tension du fil en ce point. Comparer au poids.
3. Établir l'équation du mouvement. Pour de petites oscillations, calculer la période. Le résultat s'applique-t-il ici ?
4. Quelle vitesse minimale faut-il communiquer à la masse au point le plus bas pour qu'elle fasse un tour complet, fil tendu ?
""",
r"Conservation de l'énergie mécanique : la tension ne travaille pas (perpendiculaire au mouvement).",
r"Projection du PFD sur la normale (vers le point de suspension) : $T-mg\cos\theta=mv^2/L$.",
r"Pour le tour complet, le fil doit rester tendu en haut : $T\ge0$ au sommet donne $v_{\text{haut}}^2\ge gL$ ; conserve l'énergie entre le bas et le haut.",
r"""
**1.** $\tfrac12mv^2=mgL(1-\cos\theta_0)$, d'où $v=\sqrt{2gL(1-\cos\theta_0)}=\sqrt{gL}\approx3{,}1\ \mathrm{m\,s^{-1}}$.

**2.** En bas, $T-mg=mv^2/L$, soit $T=mg+2mg(1-\cos\theta_0)=mg(3-2\cos\theta_0)=2mg$ : le fil supporte le double du poids.

**3.** Projection tangentielle : $L\ddot\theta=-g\sin\theta$. Pour $\theta$ petit, $\ddot\theta+\frac gL\theta=0$ et $T_0=2\pi\sqrt{L/g}\approx2{,}0\ \mathrm s$. Pour $\theta_0=60^\circ$, l'approximation $\sin\theta\approx\theta$ n'est plus valable : la période réelle est plus grande d'environ $7\ \%$ (formule de Borda : $T\approx T_0(1+\theta_0^2/16)$).

**4.** Au sommet ($\theta=\pi$) : $T+mg=mv_h^2/L$ et il faut $T\ge0$, donc $v_h^2\ge gL$. Énergie : $v_b^2=v_h^2+4gL\ge5gL$, d'où $v_b\ge\sqrt{5gL}\approx7{,}0\ \mathrm{m\,s^{-1}}$.
""", r"$v=\sqrt{gL}\approx3{,}1$ m/s ; $T=2mg$ ; $T_0\approx2{,}0$ s (non applicable à 60°) ; $v_b\ge\sqrt{5gL}\approx7{,}0$ m/s.")

ex('n-p1-rails', P, 'Induction', 1, 'Freinage sur les rails de Laplace', 20, r"""
Une barre conductrice de masse $m$ glisse sans frottement sur deux rails horizontaux parallèles distants de $\ell$, reliés à une extrémité par un résistor $R$ (les autres résistances et l'auto-induction sont négligées). L'ensemble baigne dans un champ magnétique uniforme vertical $\vec B$. À $t=0$, on lance la barre avec la vitesse $v_0$ le long des rails.

On donne : $m=20\ \mathrm g$, $\ell=10\ \mathrm{cm}$, $B=0{,}50\ \mathrm T$, $R=0{,}10\ \Omega$, $v_0=1{,}0\ \mathrm{m\,s^{-1}}$.

1. Exprimer la force électromotrice induite et l'intensité du courant en fonction de la vitesse $v$ de la barre.
2. Exprimer la force de Laplace et montrer qu'elle freine la barre. En déduire $v(t)$.
3. Calculer la distance totale parcourue.
4. Faire un bilan énergétique entre $t=0$ et $t\to\infty$.
""",
r"Le flux de $\vec B$ à travers le circuit est $\Phi=B\ell x$ ; loi de Faraday $e=-\mathrm d\Phi/\mathrm dt$ (avec une orientation cohérente).",
r"$i=-\dfrac{B\ell v}R$ (orientation choisie) et $\vec F=i\,\ell\,\vec u\wedge\vec B=-\dfrac{B^2\ell^2}Rv\,\vec u_x$ : $m\dot v=-\dfrac{B^2\ell^2}Rv$.",
r"$v=v_0e^{-t/\tau}$ avec $\tau=\dfrac{mR}{B^2\ell^2}$ ; la distance totale est $\int_0^\infty v\,\mathrm dt=v_0\tau$.",
r"""
**1.** Le circuit (rails, barre, résistor) délimite une surface $\ell x$ : $\Phi=B\ell x$, donc $e=-B\ell v$ et $i=e/R=-\dfrac{B\ell v}R$ (avec le circuit orienté de sorte que la normale soit $\vec B/B$).

**2.** La barre est parcourue par $i$ sur la longueur $\ell$ : $\vec F=i\ell\,\vec u_y\wedge B\vec u_z=-\dfrac{B^2\ell^2v}R\vec u_x$, opposée à la vitesse (loi de Lenz). PFD : $m\dot v=-\dfrac{B^2\ell^2}Rv$, d'où
$$v(t)=v_0e^{-t/\tau},\qquad\tau=\frac{mR}{B^2\ell^2}=\frac{0{,}02\times0{,}1}{0{,}25\times0{,}01}=0{,}80\ \mathrm s.$$

**3.** $d=\int_0^\infty v\,\mathrm dt=v_0\tau=0{,}80\ \mathrm m$.

**4.** L'énergie dissipée par effet Joule vaut $\int_0^\infty Ri^2\,\mathrm dt=\dfrac{B^2\ell^2v_0^2}R\cdot\dfrac\tau2=\tfrac12mv_0^2=10\ \mathrm{mJ}$ : toute l'énergie cinétique initiale est convertie en chaleur. La force de Laplace (puissance $-\frac{B^2\ell^2v^2}R$) et la fém (puissance $ei$) se compensent exactement : couplage électromécanique parfait.
""", r"$e=-B\ell v$ ; $v=v_0e^{-t/\tau}$, $\tau=mR/(B^2\ell^2)=0{,}80$ s ; $d=0{,}80$ m ; $W_J=\frac12mv_0^2=10$ mJ.")

ex('n-p1-transfo', P, 'Induction', 1, 'Transformateur et adaptation', 15, r"""
Un transformateur parfait comporte $N_1$ spires au primaire et $N_2$ au secondaire, enroulées sur un même circuit magnétique fermé. Le primaire est alimenté par le secteur ($230\ \mathrm V$ efficaces, $50\ \mathrm{Hz}$) ; le secondaire doit délivrer $12\ \mathrm V$ efficaces.

1. En admettant que le flux magnétique est le même à travers chaque spire, établir la relation entre les tensions $u_1$ et $u_2$. Calculer le rapport $N_2/N_1$.
2. Le transformateur parfait ne stocke ni ne dissipe d'énergie. En déduire la relation entre les intensités efficaces.
3. Le secondaire alimente un résistor $R=6{,}0\ \Omega$. Calculer les intensités au secondaire et au primaire. Quelle résistance $R'$ le générateur « voit-il » ?
4. Pourquoi transporte-t-on l'électricité sous très haute tension ?
""",
r"Loi de Faraday pour chaque bobinage : $u_k=N_k\dfrac{\mathrm d\varphi}{\mathrm dt}$ (convention récepteur au primaire, générateur au secondaire).",
r"Conservation de la puissance instantanée : $u_1i_1=u_2i_2$, d'où $I_1/I_2=N_2/N_1$.",
r"$R'=U_1/I_1=(N_1/N_2)^2R$. Pour la ligne : pertes $rI^2$ à puissance $UI$ fixée.",
r"""
**1.** Le même flux $\varphi$ traverse chaque spire : $u_1=N_1\dot\varphi$ et $u_2=N_2\dot\varphi$, donc $\dfrac{u_2}{u_1}=\dfrac{N_2}{N_1}=m$. Ici $m=12/230\approx0{,}052$ ($N_1/N_2\approx19$).

**2.** Pas de stockage ni de pertes : $u_1i_1=u_2i_2$, donc $\dfrac{I_1}{I_2}=\dfrac{N_2}{N_1}=m$ : le côté basse tension porte le fort courant.

**3.** $I_2=12/6{,}0=2{,}0\ \mathrm A$ et $I_1=mI_2\approx0{,}10\ \mathrm A$. Résistance vue du primaire : $R'=\dfrac{U_1}{I_1}=\dfrac{R}{m^2}\approx2{,}2\ \mathrm{k\Omega}$. Le transformateur permet donc d'adapter une impédance.

**4.** Pour une puissance $P=UI$ transportée, les pertes en ligne valent $rI^2=rP^2/U^2$ : multiplier $U$ par 100 divise les pertes par $10^4$. Les transformateurs élèvent la tension au départ (400 kV) et l'abaissent à l'arrivée.
""", r"$U_2/U_1=N_2/N_1\approx0{,}052$ ; $I_2=2{,}0$ A, $I_1\approx0{,}10$ A ; $R'=R(N_1/N_2)^2\approx2{,}2$ kΩ.")

ex('n-p1-adiab', P, 'Thermodynamique', 1, 'Compression rapide de l’air dans un moteur Diesel', 15, r"""
Dans un cylindre de moteur Diesel, on comprime rapidement de l'air, assimilé à un gaz parfait de coefficient $\gamma=1{,}4$, depuis $P_1=1{,}0\ \mathrm{bar}$ et $T_1=293\ \mathrm K$, jusqu'à un volume dix fois plus petit. On considère la transformation adiabatique et réversible.

On donne : $R=8{,}31\ \mathrm{J\,K^{-1}\,mol^{-1}}$.

1. Pourquoi peut-on supposer la transformation adiabatique ?
2. Calculer la température $T_2$ et la pression $P_2$ en fin de compression.
3. Calculer le travail reçu par mole d'air. Le comparer à celui d'une compression isotherme réversible de même rapport.
4. Le gazole s'enflamme spontanément vers $550\ \mathrm K$. Commenter.
""",
r"La compression dure quelques millisecondes : les transferts thermiques à travers les parois n'ont pas le temps de se faire.",
r"Lois de Laplace : $TV^{\gamma-1}=\text{cte}$ et $PV^\gamma=\text{cte}$.",
r"Premier principe pour une adiabatique : $W=\Delta U=\dfrac R{\gamma-1}(T_2-T_1)$ par mole ; en isotherme : $W=RT_1\ln(V_1/V_2)$.",
r"""
**1.** La compression est très rapide devant le temps caractéristique de diffusion thermique à travers les parois : $Q\approx0$.

**2.** Lois de Laplace avec $V_1/V_2=10$ : $T_2=T_1\cdot10^{\gamma-1}=293\times2{,}51\approx736\ \mathrm K$ et $P_2=P_1\cdot10^\gamma\approx25\ \mathrm{bar}$.

**3.** $W=\Delta U=\dfrac R{\gamma-1}(T_2-T_1)=20{,}8\times443\approx9{,}2\ \mathrm{kJ\,mol^{-1}}$. En isotherme réversible : $W=RT_1\ln10\approx5{,}6\ \mathrm{kJ\,mol^{-1}}$. La compression adiabatique coûte plus de travail, car le gaz s'échauffe et sa pression croît plus vite.

**4.** $T_2\approx740\ \mathrm K>550\ \mathrm K$ : le gazole injecté en fin de compression s'enflamme spontanément, sans bougie. C'est le principe de l'allumage par compression du moteur Diesel.
""", r"$T_2\approx736$ K, $P_2\approx25$ bar ; $W\approx9{,}2$ kJ/mol (isotherme : 5,6 kJ/mol).")

ex('n-p1-frigo', P, 'Thermodynamique', 1, 'Réfrigérateur réel', 20, r"""
Un réfrigérateur maintient son intérieur à $T_F=278\ \mathrm K$ dans une cuisine à $T_C=298\ \mathrm K$. Le fluide frigorigène décrit des cycles ; son compresseur reçoit une puissance électrique $\mathcal P=100\ \mathrm W$.

1. Définir l'efficacité $e$ du réfrigérateur. Établir son expression maximale $e_C$ à l'aide des deux principes et la calculer.
2. L'efficacité réelle vaut $e=3{,}0$. Combien de temps faut-il pour transformer en glace $1{,}0\ \mathrm{kg}$ d'eau déjà à $0\ ^\circ\mathrm C$ placé dans le congélateur ?
3. Calculer l'entropie créée par joule électrique consommé dans le cas réel.

On donne : enthalpie de fusion de la glace $\ell_f=334\ \mathrm{kJ\,kg^{-1}}$. Pour la question 2, on suppose que l'efficacité reste égale à $3{,}0$.
""",
r"$e=Q_F/W$ ; sur un cycle : $W+Q_F+Q_C=0$ et $\dfrac{Q_F}{T_F}+\dfrac{Q_C}{T_C}\le0$.",
r"Au mieux $e_C=\dfrac{T_F}{T_C-T_F}$. Il faut extraire $Q=m\ell_f$ à la puissance $e\mathcal P$.",
r"$S_c=-\left(\dfrac{Q_F}{T_F}+\dfrac{Q_C}{T_C}\right)$ avec $Q_F=e\,W$ et $Q_C=-(1+e)W$, pour $W=1$ J.",
r"""
**1.** $e=\dfrac{Q_F}W$ (chaleur extraite de la source froide sur travail reçu). Premier principe : $W+Q_F+Q_C=0$ ; second principe (Clausius) : $\dfrac{Q_F}{T_F}+\dfrac{Q_C}{T_C}\le0$. En éliminant $Q_C$ : $Q_F\left(\frac1{T_F}-\frac1{T_C}\right)\le\frac W{T_C}$, d'où
$$e\le e_C=\frac{T_F}{T_C-T_F}=\frac{278}{20}\approx14.$$

**2.** Il faut extraire $Q=m\ell_f=334\ \mathrm{kJ}$ à la puissance $e\mathcal P=300\ \mathrm W$ : $\Delta t=334\times10^3/300\approx1{,}1\times10^3\ \mathrm s\approx19\ \mathrm{min}$.

**3.** Pour $W=1$ J : $Q_F=3{,}0$ J et $Q_C=-4{,}0$ J. $S_c=-\dfrac{3{,}0}{278}+\dfrac{4{,}0}{298}\approx2{,}6\times10^{-3}\ \mathrm{J\,K^{-1}}$. Elle est strictement positive : les irréversibilités (écarts de température dans les échangeurs, détente du fluide) expliquent l'écart entre $e$ et $e_C$.
""", r"$e_C=T_F/(T_C-T_F)\approx14$ ; $\approx19$ min ; $S_c\approx2{,}6\times10^{-3}$ J/K par joule.")

ex('n-p1-glacon', P, 'Thermodynamique', 1, 'Glaçon dans un verre d’eau', 20, r"""
Dans un calorimètre parfaitement isolé, de capacité thermique négligeable, on place $m_e=200\ \mathrm g$ d'eau à $25\ ^\circ\mathrm C$, puis un glaçon de $m_g=50\ \mathrm g$ sorti du congélateur à $-10\ ^\circ\mathrm C$. La pression reste égale à $1$ bar.

On donne : $c_{\text{eau}}=4{,}18\ \mathrm{kJ\,kg^{-1}\,K^{-1}}$, $c_{\text{glace}}=2{,}1\ \mathrm{kJ\,kg^{-1}\,K^{-1}}$, $\ell_f=334\ \mathrm{kJ\,kg^{-1}}$ à $0\ ^\circ\mathrm C$.

1. Montrer que tout le glaçon fond.
2. Déterminer la température finale.
3. Calculer la variation d'entropie du système. Conclure.
""",
r"Compare l'énergie nécessaire pour amener la glace à $0\ ^\circ$C et la fondre à celle que libère l'eau en se refroidissant jusqu'à $0\ ^\circ$C.",
r"Bilan enthalpique (système isolé, isobare) : $\Delta H=0$, en découpant en étapes fictives.",
r"Pour chaque étape : $mc\ln(T_f/T_i)$, et $m\ell_f/T_0$ pour la fusion. Travaille en kelvins.",
r"""
**1.** Pour amener la glace à $0\ ^\circ$C puis la fondre : $0{,}05\times2{,}1\times10+0{,}05\times334\approx1{,}05+16{,}7=17{,}8\ \mathrm{kJ}$. L'eau libère au plus $0{,}2\times4{,}18\times25=20{,}9$ kJ en descendant à $0\ ^\circ$C : c'est suffisant, tout fond.

**2.** $\Delta H=0$ : $m_gc_g(0-(-10))+m_g\ell_f+m_gc_e\theta_f+m_ec_e(\theta_f-25)=0$, soit $(m_g+m_e)c_e\theta_f=20{,}9-17{,}8=3{,}1$ kJ, et $\theta_f=\dfrac{3{,}15}{0{,}25\times4{,}18}\approx3{,}0\ ^\circ\mathrm C$.

**3.** Avec $T_0=273$ K et $T_f=276$ K :
- glace de $263$ à $273$ K : $0{,}105\ln\frac{273}{263}\approx+3{,}9\ \mathrm{J\,K^{-1}}$ ;
- fusion : $16\,700/273\approx+61{,}1\ \mathrm{J\,K^{-1}}$ ;
- eau de fonte de $273$ à $276$ K : $209\ln\frac{276}{273}\approx+2{,}3\ \mathrm{J\,K^{-1}}$ ;
- eau chaude de $298$ à $276$ K : $836\ln\frac{276}{298}\approx-64{,}1\ \mathrm{J\,K^{-1}}$.

$\Delta S\approx+3{,}3\ \mathrm{J\,K^{-1}}>0$. Le système étant isolé, $\Delta S=S_c>0$ : la transformation est irréversible, comme tout échange de chaleur sous un écart fini de température.
""", r"Tout fond ; $\theta_f\approx3{,}0\ ^\circ$C ; $\Delta S\approx+3{,}3$ J/K (irréversible).")

ex('n-p1-atmo', P, 'Mécanique des fluides', 1, 'Atmosphère isotherme et ballon d’hélium', 20, r"""
On modélise l'atmosphère comme un gaz parfait de masse molaire $M=29\ \mathrm{g\,mol^{-1}}$ à température uniforme $T=288\ \mathrm K$, en équilibre dans le champ de pesanteur uniforme $g=9{,}8\ \mathrm{m\,s^{-2}}$. Au sol, $P_0=1{,}0\ \mathrm{bar}$.

On donne : $R=8{,}31\ \mathrm{J\,K^{-1}\,mol^{-1}}$, $M_{\mathrm{He}}=4{,}0\ \mathrm{g\,mol^{-1}}$.

1. Établir la loi $P(z)$ et faire apparaître une hauteur caractéristique $H$ ; la calculer.
2. Estimer la pression au sommet de l'Everest ($8\,850\ \mathrm m$).
3. Montrer que l'on peut considérer la pression comme uniforme dans une salle de classe ; donner l'écart relatif sur $100\ \mathrm m$.
4. Un ballon contient $10\ \mathrm{m^3}$ d'hélium à la pression et à la température de l'air ambiant au sol. Quelle masse totale (enveloppe et charge) peut-il soulever ?
""",
r"Statique des fluides : $\dfrac{\mathrm dP}{\mathrm dz}=-\rho g$ avec $\rho=\dfrac{PM}{RT}$.",
r"$P=P_0e^{-z/H}$ avec $H=\dfrac{RT}{Mg}$. Pour $z\ll H$ : $\Delta P/P\approx z/H$.",
r"Poussée d'Archimède : $\rho_{\text{air}}Vg$ ; il faut qu'elle dépasse le poids de l'hélium plus celui de la charge.",
r"""
**1.** $\dfrac{\mathrm dP}{\mathrm dz}=-\dfrac{Mg}{RT}P$, d'où $P(z)=P_0e^{-z/H}$ avec $H=\dfrac{RT}{Mg}=\dfrac{8{,}31\times288}{0{,}029\times9{,}8}\approx8{,}4\ \mathrm{km}$.

**2.** $P=P_0e^{-8850/8400}\approx0{,}35\ \mathrm{bar}$ (la valeur réelle, $\approx0{,}33$ bar, est un peu plus faible car l'air est plus froid en altitude).

**3.** Pour $z\ll H$, $P\approx P_0(1-z/H)$ : l'écart relatif sur 100 m est $100/8400\approx1{,}2\ \%$ ; sur 3 m, il vaut $4\times10^{-4}$ : la pression est uniforme à l'échelle d'une salle.

**4.** $\rho_{\text{air}}=\dfrac{P_0M}{RT}\approx1{,}21\ \mathrm{kg\,m^{-3}}$ et $\rho_{\mathrm{He}}=\dfrac{P_0M_{\mathrm{He}}}{RT}\approx0{,}17\ \mathrm{kg\,m^{-3}}$. La masse maximale soulevée vaut $(\rho_{\text{air}}-\rho_{\mathrm{He}})V\approx10\ \mathrm{kg}$.
""", r"$P=P_0e^{-z/H}$, $H=RT/(Mg)\approx8{,}4$ km ; Everest ≈ 0,35 bar ; 1,2 % sur 100 m ; ≈ 10 kg.")

ex('n-p1-bobine', P, 'Induction', 1, 'Bobine plate dans un champ alternatif', 10, r"""
Une bobine plate de $N=100$ spires, de surface $S=20\ \mathrm{cm^2}$ et de résistance $r=2{,}0\ \Omega$, est fermée sur elle-même. Elle est placée dans un champ magnétique uniforme, parallèle à son axe, $B(t)=B_0\sin\omega t$, avec $B_0=50\ \mathrm{mT}$ et $f=50\ \mathrm{Hz}$. On néglige l'auto-induction.

1. Calculer la force électromotrice induite $e(t)$ et sa valeur maximale.
2. En déduire l'intensité $i(t)$ et la puissance moyenne dissipée.
3. Donner le sens du courant lorsque $B$ croît et l'interpréter avec la loi de Lenz.
""",
r"Flux à travers les $N$ spires : $\Phi=NSB(t)$, et $e=-\mathrm d\Phi/\mathrm dt$.",
r"$i=e/r$ ; puissance moyenne : $\langle ri^2\rangle=\dfrac{rI_{\max}^2}2$.",
r"Le courant induit crée un champ propre qui s'oppose à la variation du flux.",
r"""
**1.** $\Phi=NSB_0\sin\omega t$, donc $e=-NSB_0\omega\cos\omega t$ et $e_{\max}=NSB_0\omega=100\times2{,}0\times10^{-3}\times0{,}05\times314\approx3{,}1\ \mathrm V$.

**2.** $i=e/r$, d'amplitude $I_{\max}\approx1{,}6\ \mathrm A$. Puissance moyenne : $\dfrac{e_{\max}^2}{2r}\approx2{,}5\ \mathrm W$.

**3.** Quand $B$ croît, $e<0$ : le courant circule dans le sens négatif (relativement à l'orientation de la normale le long de $\vec B$). Il crée un champ propre opposé à $\vec B$ au centre de la bobine, qui tend à limiter l'augmentation du flux : c'est la loi de Lenz. L'hypothèse d'auto-induction négligeable demande $L\omega\ll r$.
""", r"$e_{\max}=NSB_0\omega\approx3{,}1$ V ; $I_{\max}\approx1{,}6$ A ; $\langle\mathcal P\rangle\approx2{,}5$ W.")
