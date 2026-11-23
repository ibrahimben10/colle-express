D = {}

D['n-p1-rc'] = r"""
**1. Loi des mailles.** En convention récepteur pour $R$ et $C$, avec $i$ le courant de charge : $E=u_R+u_C=Ri+u_C$. Pour le condensateur, $q=Cu_C$ et $i=\frac{\mathrm dq}{\mathrm dt}=C\frac{\mathrm du_C}{\mathrm dt}$. D'où
$$RC\frac{\mathrm du_C}{\mathrm dt}+u_C=E.$$

**1. Résolution.** La solution générale est la somme de la solution de l'équation homogène, $Ae^{-t/\tau}$ avec $\tau=RC$, et d'une solution particulière constante, $E$ : $u_C=E+Ae^{-t/\tau}$. La tension aux bornes d'un condensateur est continue (l'énergie $\frac12Cu_C^2$ ne peut pas varier instantanément), donc $u_C(0^+)=u_C(0^-)=0$, ce qui donne $A=-E$ :
$$u_C(t)=E\big(1-e^{-t/\tau}\big),\qquad i(t)=C\frac{\mathrm du_C}{\mathrm dt}=\frac ERe^{-t/\tau}.$$

**2. Constante de temps.** $\tau=RC=1{,}0\times10^3\times100\times10^{-6}=0{,}10$ s.

**2. Charge à 99 %.** On veut $u_C=0{,}99E$, soit $e^{-t/\tau}=0{,}01$ :
$$t_{99}=\tau\ln100\approx4{,}6\,\tau\approx0{,}46\ \mathrm s.$$
On retient qu'au bout de $5\tau$, le régime permanent est atteint à moins de 1 % près.

**3. Énergie fournie par le générateur.**
$$W_g=\int_0^{+\infty}Ei\,\mathrm dt=E\int_0^{+\infty}i\,\mathrm dt=E\,q_\infty=E\cdot CE=CE^2=10^{-4}\times100=10\ \mathrm{mJ}.$$

**3. Énergie stockée.** $W_C=\frac12Cu_C(\infty)^2=\frac12CE^2=5{,}0$ mJ.

**3. Énergie dissipée par effet Joule.**
$$W_J=\int_0^{+\infty}Ri^2\,\mathrm dt=\frac{E^2}R\int_0^{+\infty}e^{-2t/\tau}\,\mathrm dt=\frac{E^2}R\cdot\frac\tau2=\frac12CE^2=5{,}0\ \mathrm{mJ}.$$
Vérification : $W_g=W_C+W_J$ (conservation de l'énergie). ✓

**4. Rendement.** $\eta=\frac{W_C}{W_g}=\frac12$, **indépendant de $R$**. $R$ ne fixe que la durée de la charge (par $\tau$) : une petite résistance donne un courant plus intense mais plus bref, et la dissipation $\int Ri^2$ reste la même. Même pour $R\to0$, la moitié de l'énergie est perdue (résistance des fils, rayonnement). Pour améliorer le rendement, il faut charger sous une tension croissant progressivement : l'écart $E-u_C$, cause des pertes, reste alors petit.
"""

D['n-p1-rlc'] = r"""
**1. Loi des mailles.** Circuit série en régime libre, en convention récepteur : $u_L+u_R+u_C=0$, avec $i=\frac{\mathrm dq}{\mathrm dt}$, $u_L=L\frac{\mathrm di}{\mathrm dt}$, $u_R=Ri$ et $u_C=\frac qC$. D'où
$$L\ddot q+R\dot q+\frac qC=0.$$

**1. Forme canonique.** On divise par $L$ et on identifie avec $\ddot q+\frac{\omega_0}Q\dot q+\omega_0^2q=0$ :
$$\omega_0^2=\frac1{LC},\qquad\frac{\omega_0}Q=\frac RL\iff Q=\frac{L\omega_0}R=\frac1R\sqrt{\frac LC}.$$

**2. Valeurs numériques.**
$$\omega_0=\frac1{\sqrt{10\times10^{-3}\times1{,}0\times10^{-6}}}=\frac1{10^{-4}}=1{,}0\times10^4\ \mathrm{rad\,s^{-1}},\qquad f_0=\frac{\omega_0}{2\pi}\approx1{,}6\ \mathrm{kHz},$$
$$Q=\frac1{20}\sqrt{\frac{10^{-2}}{10^{-6}}}=\frac{100}{20}=5{,}0.$$

**2. Régime.** L'équation caractéristique $r^2+\frac{\omega_0}Qr+\omega_0^2=0$ a pour discriminant $\Delta=\omega_0^2\big(\frac1{Q^2}-4\big)$. Comme $Q=5>\frac12$, $\Delta<0$ : le régime est **pseudo-périodique**.

**3. Pseudo-période.** Les racines sont $r=-\frac{\omega_0}{2Q}\pm i\Omega$, avec
$$\Omega=\omega_0\sqrt{1-\frac1{4Q^2}}=\omega_0\sqrt{0{,}99}\approx0{,}995\,\omega_0,\qquad T=\frac{2\pi}\Omega\approx6{,}3\times10^{-4}\ \mathrm s.$$
$T$ est très proche de la période propre $T_0=0{,}628$ ms.

**3. Décroissance.** $q(t)=Ae^{-\omega_0t/(2Q)}\cos(\Omega t+\varphi)$. Deux maxima successifs sont séparés de $T$, et leur rapport vaut
$$\frac{q(t+T)}{q(t)}=e^{-\omega_0T/(2Q)}=\exp\Big(-\frac\pi{Q\sqrt{1-1/(4Q^2)}}\Big)=e^{-0{,}63}\approx0{,}53.$$
Le décrément logarithmique vaut $\delta=\frac{\omega_0T}{2Q}\approx\frac\pi Q\approx0{,}63$. On observe environ $Q\approx5$ oscillations nettes avant que l'amplitude devienne négligeable.

**4. Régime critique.** Il correspond à $\Delta=0$, soit $Q=\frac12$ :
$$R_c=2\sqrt{\frac LC}=2\sqrt{\frac{10^{-2}}{10^{-6}}}=2\times100=200\ \Omega.$$
C'est le régime qui ramène le plus vite à l'équilibre sans oscillation.
"""

D['n-p1-passebas'] = r"""
**1. Fonction de transfert.** Sortie ouverte : le même courant traverse $R$ et $C$, ce qui forme un pont diviseur de tension d'impédances $Z_R=R$ et $Z_C=\frac1{jC\omega}$ :
$$\underline H=\frac{\underline s}{\underline e}=\frac{Z_C}{Z_R+Z_C}=\frac{1/(jC\omega)}{R+1/(jC\omega)}=\frac1{1+jRC\omega}=\frac1{1+jf/f_c},\qquad f_c=\frac1{2\pi RC}.$$

**1. Nature.** En basses fréquences, $\underline H\to1$ (le condensateur est un interrupteur ouvert). En hautes fréquences, $\underline H\to0$ (le condensateur est un fil). C'est un **passe-bas du premier ordre**.

**1. Fréquence de coupure.** $RC=10^3\times10^{-7}=10^{-4}$ s, donc $f_c=\frac1{2\pi\times10^{-4}}\approx1{,}6$ kHz. En $f=f_c$, $|\underline H|=\frac1{\sqrt2}$.

**2. Diagramme de Bode en gain.** $G_{dB}=20\log|\underline H|=-10\log\big(1+(f/f_c)^2\big)$.
- $f\ll f_c$ : $G_{dB}\approx0$, asymptote horizontale.
- $f\gg f_c$ : $G_{dB}\approx-20\log\frac f{f_c}$, droite de pente $-20$ dB par décade.

Les deux asymptotes se coupent en $f_c$, où la courbe réelle passe à $-3$ dB.

**2. Comportement en hautes fréquences.** $\underline H\approx\frac1{jRC\omega}$, c'est-à-dire $\underline s\approx\frac{\underline e}{jRC\omega}$. Diviser par $j\omega$ revient à intégrer : $s(t)\approx\frac1{RC}\int e\,\mathrm dt$. Le filtre est **intégrateur** pour $f\gg f_c$.

**3. Principe.** Le filtre est linéaire : la réponse à une somme est la somme des réponses. Chaque composante sinusoïdale est multipliée par $|\underline H(f)|$ et déphasée de $\varphi=\arg\underline H=-\arctan\frac f{f_c}$.

**3. Composante continue** ($f=0$) : $\underline H(0)=1$, elle passe intégralement : $2{,}0$ V.

**3. Composante à $f_1=100$ Hz.** $\frac{f_1}{f_c}=0{,}063$, donc $|\underline H|=\frac1{\sqrt{1+0{,}004}}\approx0{,}998$ et $\varphi=-\arctan0{,}063\approx-0{,}063$ rad ($-3{,}6^\circ$). Elle passe quasiment intacte.

**3. Composante à $f_2=20$ kHz.** $\frac{f_2}{f_c}=12{,}6$, donc $|\underline H|=\frac1{\sqrt{1+158}}\approx0{,}079$ et $\varphi=-\arctan12{,}6\approx-1{,}49$ rad ($-85^\circ$). Elle est atténuée d'un facteur 12,6, soit $-22$ dB.

**3. Résultat.**
$$s(t)\approx2{,}0+1{,}0\cos(2\pi f_1t-0{,}063)+0{,}079\cos(2\pi f_2t-1{,}49)\quad(\mathrm V).$$
Le filtre élimine pratiquement la composante haute fréquence (le « bruit ») sans altérer le signal utile basse fréquence : c'est le principe du lissage.
"""

D['n-p1-passebande'] = r"""
**1. Fonction de transfert.** Pont diviseur : la sortie est prise aux bornes de $R$, en série avec $L$ et $C$.
$$\underline H=\frac R{R+jL\omega+\frac1{jC\omega}}=\frac R{R+j\big(L\omega-\frac1{C\omega}\big)}=\frac1{1+j\big(\frac{L\omega}R-\frac1{RC\omega}\big)}.$$

**1. Forme canonique.** On pose $\omega_0=\frac1{\sqrt{LC}}$ et $x=\frac\omega{\omega_0}$. Alors $\frac{L\omega}R=\frac{L\omega_0}Rx$ et $\frac1{RC\omega}=\frac1{RC\omega_0}\cdot\frac1x$. Or $\frac{L\omega_0}R=\frac1R\sqrt{\frac LC}=\frac1{RC\omega_0}$ : on note $Q$ cette quantité commune. D'où
$$\underline H=\frac1{1+jQ\big(x-\frac1x\big)},\qquad\omega_0=\frac1{\sqrt{LC}},\qquad Q=\frac1R\sqrt{\frac LC}.$$

**2. Valeurs numériques.** $\omega_0=\frac1{\sqrt{0{,}10\times10^{-7}}}=\frac1{10^{-4}}=1{,}0\times10^4\ \mathrm{rad\,s^{-1}}$, $f_0\approx1{,}6$ kHz ; $Q=\frac1{100}\sqrt{\frac{0{,}10}{10^{-7}}}=\frac{1000}{100}=10$.

**3. Coupure à $-3$ dB.** $|\underline H|=\frac1{\sqrt2}$ équivaut à $Q^2\big(x-\frac1x\big)^2=1$, soit $Q\big(x-\frac1x\big)=\pm1$. En multipliant par $\frac xQ$ : $x^2\mp\frac xQ-1=0$.

**3. Résolution.** Les racines positives sont
$$x_1=-\frac1{2Q}+\sqrt{1+\frac1{4Q^2}},\qquad x_2=+\frac1{2Q}+\sqrt{1+\frac1{4Q^2}}.$$
Leur différence vaut $x_2-x_1=\frac1Q$, et leur produit $x_1x_2=1$ (les deux pulsations sont symétriques en échelle logarithmique autour de $\omega_0$). Donc
$$\Delta\omega=\frac{\omega_0}Q,\qquad\Delta f=\frac{f_0}Q=\frac{1590}{10}\approx160\ \mathrm{Hz}.$$
La bande passante s'étend d'environ 1,51 kHz à 1,67 kHz.

**4. À la résonance** ($x=1$). $x-\frac1x=0$, donc $\underline H=1$ : le gain vaut $0$ dB (maximal) et le déphasage est nul.

**4. Interprétation.** À $\omega_0$, les impédances de la bobine et du condensateur se compensent exactement : $jL\omega_0+\frac1{jC\omega_0}=j\big(L\omega_0-\frac1{C\omega_0}\big)=0$. Le circuit se comporte comme la seule résistance $R$ : le courant est maximal ($\frac ER$) et en phase avec $e$, et toute la tension d'entrée se retrouve aux bornes de $R$. En revanche, les tensions aux bornes de $L$ et de $C$ valent $Q$ fois l'entrée (surtension). Plus $Q$ est grand, plus le filtre est sélectif ($\Delta f$ petit).
"""

D['n-p1-corde'] = r"""
**1. Modes propres.** La corde vérifie l'équation de d'Alembert. On cherche des ondes stationnaires $y(x,t)=A\sin(kx+\phi)\cos(\omega t+\psi)$ avec $\omega=kc$. Les conditions aux limites sont :
- $y(0,t)=0$ pour tout $t$, d'où $\sin\phi=0$ : on prend $\phi=0$ ;
- $y(L,t)=0$, d'où $\sin(kL)=0$ et $k_nL=n\pi$, $n\in\mathbb N^*$.

Donc $\lambda_n=\frac{2L}n$ (la longueur est un nombre entier de demi-longueurs d'onde) et
$$f_n=\frac c{\lambda_n}=n\frac c{2L}=nf_1.$$

**1. Célérité et tension.** $f_1=\frac c{2L}$, donc $c=2Lf_1=2\times0{,}65\times82\approx107\ \mathrm{m\,s^{-1}}$. Avec $c=\sqrt{T/\mu}$ :
$$T=\mu c^2=5{,}0\times10^{-3}\times(107)^2\approx57\ \mathrm N.$$
Cela correspond à une masse d'environ 6 kg suspendue à la corde.

**2. Frette pour le la.** En appuyant sur une frette, on réduit la longueur vibrante à $\ell$, sans changer la tension ni la masse linéique : $c$ est inchangée. Le fondamental vaut alors $f=\frac c{2\ell}$, d'où
$$\ell=\frac c{2f}=\frac{107}{2\times110}\approx0{,}485\ \mathrm m.$$
On appuie donc à $L-\ell\approx65-48{,}5\approx17$ cm du sillet (côté tête). On remarque que $\frac\ell L=\frac{82}{110}\approx0{,}75\approx2^{-5/12}$ : la quarte (5 demi-tons) correspond à la 5ᵉ frette.

**3. Pincement au milieu.** La déformation initiale (triangle de sommet en $\frac L2$) est symétrique par rapport au milieu. On la décompose sur les modes propres $\sin\frac{n\pi x}L$ (série de Fourier).
- Pour $n$ impair, $\sin\frac{n\pi x}L$ est symétrique par rapport à $\frac L2$.
- Pour $n$ pair, il est antisymétrique, et nul en $\frac L2$ : un nœud au milieu.

Une fonction symétrique a des coefficients nuls sur les modes antisymétriques. Les **harmoniques pairs** ($2f_1$, $4f_1$, …) sont donc **absents** du son.

**3. Remarque.** On peut aussi dire qu'on ne peut pas exciter un mode en un de ses nœuds. Le timbre est alors plus « creux », plus doux. En pinçant près du chevalet, on excite au contraire beaucoup d'harmoniques élevés : le son est brillant.
"""

D['n-p1-ultrasons'] = r"""
**1. Longueur d'onde.**
$$\lambda=\frac cf=\frac{340}{4{,}0\times10^4}=8{,}5\times10^{-3}\ \mathrm m=8{,}5\ \mathrm{mm}.$$

**2. Géométrie.** On place les sources en $S_{1,2}=\big(\mp\frac a2,0\big)$, et le récepteur en $M=(x,D)$, sur une droite parallèle à $S_1S_2$, à la distance $D$.
$$S_1M=\sqrt{D^2+\Big(x+\frac a2\Big)^2}\approx D+\frac{(x+a/2)^2}{2D},\qquad S_2M\approx D+\frac{(x-a/2)^2}{2D},$$
à condition que $|x|,a\ll D$.

**2. Différence de marche.**
$$\delta=S_1M-S_2M\approx\frac{(x+a/2)^2-(x-a/2)^2}{2D}=\frac{2ax}{2D}=\frac{ax}D.$$

**2. Maxima.** Les sources émettent en phase : les ondes arrivent en phase en $M$ si $\delta=p\lambda$, $p\in\mathbb Z$. L'amplitude y est maximale, égale à la somme des amplitudes. Donc
$$x_p=p\frac{\lambda D}a,\qquad i=\frac{\lambda D}a=\frac{8{,}5\times10^{-3}\times1{,}0}{5{,}0\times10^{-2}}=0{,}17\ \mathrm m=17\ \mathrm{cm}.$$
La condition $|x|\ll D$ n'est valable que pour les premiers maxima ($p=0,\pm1$).

**3. Directions des maxima.** Loin des sources ($D\gg a$), dans la direction faisant l'angle $\theta$ avec la médiatrice de $S_1S_2$, les rayons sont quasi parallèles et $\delta=a\sin\theta$, sans hypothèse de petit angle.

**3. Comptage.** Un maximum exige $a\sin\theta=p\lambda$, soit $\sin\theta=\frac{p\lambda}a$. Il faut $|\sin\theta|\le1$, donc $|p|\le\frac a\lambda=\frac{50}{8{,}5}=5{,}9$, soit $p\in\{-5,\dots,5\}$. On observe un maximum dans **11 directions** (dans un demi-plan devant les émetteurs). Le maximum d'ordre 5 est à $\theta_5=\arcsin(0{,}85)\approx58^\circ$.
"""
