D = {}

D['p-opt-6'] = r"""
**0. Rappel.** En lame d'air d'épaisseur $e$, un rayon d'incidence $i$ donne une différence de marche $\delta=2e\cos i$. Au foyer de la lentille de sortie, qui reçoit les rayons parallèles à l'axe ($i=0$), $\delta=2e$.

**1. Cas $e=0$.** On a $\delta=0$ pour toute incidence : toutes les ondes interfèrent constructivement et l'éclairement est uniforme et maximal dans tout le champ. C'est le réglage au **contact optique** (« teinte plate ») : les miroirs $M_1'$ (image de $M_1$ par la séparatrice) et $M_2$ sont confondus. C'est le point de départ de tous les réglages.

**2. Défilement des franges.** L'éclairement au capteur vaut $I=2I_0\big(1+\cos\frac{2\pi\delta}{\lambda_0}\big)=2I_0\big(1+\cos\frac{4\pi e}{\lambda_0}\big)$. Une frange brillante défile chaque fois que $\delta$ augmente de $\lambda_0$, c'est-à-dire chaque fois que $e$ augmente de $\frac{\lambda_0}2$. Donc
$$N=\frac{\Delta\delta}{\lambda_0}=\frac{2\Delta e}{\lambda_0}=\frac{2\times2\times10^{-6}}{475\times10^{-9}}=\frac{4\times10^{-6}}{4{,}75\times10^{-7}}\approx8{,}4.$$
On voit défiler **8 franges brillantes** (plus une fraction de frange).

**3. Effet de la lame de verre.** Sur le bras où elle est placée, la lumière traverse la lame deux fois (aller et retour) sous incidence normale. Au lieu de parcourir $2h$ dans l'air (chemin optique $2h$), elle parcourt $2h$ dans le verre (chemin optique $2nh$). Le chemin optique de ce bras augmente donc de $2(n-1)h$. Si le Michelson était au contact optique, la différence de marche au capteur devient
$$\delta=2(n-1)h=2\times0{,}50\times1{,}0\ \mathrm{mm}=1{,}0\ \mathrm{mm}.$$

**3. Retour à $\delta=0$.** On translate le miroir de l'autre bras pour allonger ce bras de $\Delta e=(n-1)h=0{,}50$ mm. La différence de marche varie alors de $2\Delta e=1{,}0$ mm, et il défile
$$N=\frac{2(n-1)h}{\lambda_0}=\frac{1{,}0\times10^{-3}}{475\times10^{-9}}\approx2{,}1\times10^3\ \text{franges}.$$

**3. Remarques.** Compter ces franges permet de mesurer $(n-1)h$, donc $n$ si $h$ est connu. En pratique, avec une source de longueur de cohérence inférieure au millimètre, les franges disparaissent dès que $|\delta|$ dépasse cette longueur. On repère alors $\delta=0$ en lumière blanche (frange achromatique), ce qui demande de tenir compte de la dispersion du verre ($n$ dépend de $\lambda$).
"""

D['p-opt-7'] = r"""
**1. Conjugaison.** La lentille forme sur l'écran (à la distance $D'$ derrière elle) l'image de $M_1'$ (à la distance $D$ devant elle). La formule de Descartes, avec $\overline{OA}=-D$ et $\overline{OA'}=D'$, s'écrit $\frac1{D'}+\frac1D=\frac1{f'}$, donc
$$D'=\frac{Df'}{D-f'}.$$

**1. Grandissement.**
$$\gamma=\frac{x'}x=\frac{\overline{OA'}}{\overline{OA}}=-\frac{D'}D=-\frac{f'}{D-f'}.$$
Application numérique : $\gamma=-\frac{25}{27-25}=-12{,}5$. L'image est renversée et agrandie 12,5 fois, et $D'=\frac{27\times25}2=337{,}5$ cm.

**2. Épaisseur du coin d'air.** Avec un angle $\frac\pi2+\alpha$ entre les miroirs, $M_1'$ et $M_2$ forment un coin d'air d'angle $\alpha$. Son arête passe par $A$. Au point $P$ de $M_1'$ tel que $\overline{AP}=x$ (compté perpendiculairement à l'arête) :
$$\varepsilon(x)=x\tan\alpha\simeq\alpha x.$$
Les franges sont localisées au voisinage du coin : c'est pourquoi on fait l'image de $M_1'$ sur l'écran.

**3. Expression en fonction de $x'$.** $x=\frac{x'}\gamma=-\frac{D-f'}{f'}x'$, donc
$$\varepsilon=-\alpha\frac{D-f'}{f'}x'.$$

**4. Différence de marche.** Sous éclairage quasi normal, $\delta\simeq2\varepsilon$ (aller-retour dans le coin, $\cos i\approx1$) :
$$\delta(x')=-\frac{2\alpha(D-f')}{f'}x'.$$

**4. Éclairement.** Pour deux ondes de même intensité $I_0$ :
$$I(x')=2I_0\Big[1+\cos\Big(\frac{2\pi\delta}{\lambda_0}\Big)\Big]=2I_0\Big[1+\cos\Big(\frac{4\pi\alpha(D-f')}{\lambda_0f'}x'\Big)\Big].$$

**4. Franges brillantes.** $\delta=p\lambda_0$, $p\in\mathbb Z$, donne
$$x'_p=-\frac{p\lambda_0f'}{2\alpha(D-f')}.$$
Ce sont des droites parallèles à l'arête (franges d'égale épaisseur), équidistantes, avec l'interfrange
$$i'=\frac{\lambda_0f'}{2\alpha(D-f')}=|\gamma|\,\frac{\lambda_0}{2\alpha}.$$
L'interfrange sur le coin, $\frac{\lambda_0}{2\alpha}$, est simplement agrandi par la lentille.

**5. Application numérique.** $\alpha=0{,}5'=\frac{0{,}5}{60}\times\frac\pi{180}=1{,}45\times10^{-4}$ rad.
- Sur le coin : $\frac{\lambda_0}{2\alpha}=\frac{6{,}0\times10^{-7}}{2{,}91\times10^{-4}}\approx2{,}1$ mm.
- Sur l'écran : $i'=12{,}5\times2{,}1\approx26$ mm.

On observe des **franges rectilignes, parallèles à l'image de l'arête, équidistantes d'environ 2,6 cm**. La frange passant par l'image de l'arête ($\varepsilon=0$, donc $\delta=0$) est brillante. En lumière blanche, seule cette frange centrale et quelques franges voisines irisées seraient visibles.
"""

D['p-opt-8'] = r"""
**1. Superposition incohérente.** Deux composantes spectrales de nombres d'onde différents n'interfèrent pas entre elles (en moyenne temporelle) : les éclairements s'ajoutent. La bande $[\sigma,\sigma+\mathrm d\sigma]$ porte l'éclairement $\mathcal D(\sigma)\,\mathrm d\sigma$, et elle donne au centre ($i=0$) $\mathrm dI=2\mathcal D(\sigma)\big[1+\cos(2\pi\sigma\delta)\big]\mathrm d\sigma$, avec $\delta=2e$. Comme $e(t)=V_0t$ :
$$I(t)=\int_0^{+\infty}2\mathcal D(\sigma)\big[1+\cos(2\pi\sigma\delta)\big]\,\mathrm d\sigma,\qquad\delta=2V_0t.$$

**2. Terme constant.** Comme $b\ll\sigma_0$, la gaussienne est négligeable pour $\sigma\le0$ : on peut intégrer sur $\mathbb R$. Avec $y=\frac{\sigma-\sigma_0}b$ :
$$\int_0^{+\infty}2\mathcal D(\sigma)\,\mathrm d\sigma\simeq2\mathcal D_0b\int_{-\infty}^{+\infty}e^{-y^2}\,\mathrm dy=2\sqrt\pi\,\mathcal D_0b.$$

**2. Terme d'interférences.** Avec l'intégrale fournie :
$$\int2\mathcal D(\sigma)\cos(2\pi\sigma\delta)\,\mathrm d\sigma\simeq2\mathcal D_0b\sqrt\pi\,e^{-\pi^2b^2\delta^2}\cos(2\pi\sigma_0\delta).$$

**2. Identification.** En remplaçant $\delta=2V_0t$ :
$$I(t)=I_0\Big[1+e^{-(2\pi bV_0t)^2}\cos(4\pi\sigma_0V_0t)\Big]=I_0\Big[1+e^{-(t/\tau)^2}\cos\frac{2\pi t}{T_0}\Big],$$
avec
$$I_0=2\sqrt\pi\,\mathcal D_0b,\qquad\tau=\frac1{2\pi bV_0},\qquad T_0=\frac1{2\sigma_0V_0}=\frac{\lambda_0}{2V_0}.$$
On a $\frac\tau{T_0}=\frac{\sigma_0}{\pi b}\gg1$ : de nombreuses franges (période $T_0$) apparaissent sous l'enveloppe gaussienne de largeur $\tau$. Le contraste $e^{-(t/\tau)^2}$ décroît quand $|t|$ augmente : c'est l'effet de la largeur spectrale (cohérence temporelle limitée).

**3. Vitesse du miroir.** Une vis au pas de 0,500 mm, faisant un tour en $15\ \mathrm{min}=900$ s, donne
$$V_0=\frac{0{,}500\times10^{-3}}{900}\approx5{,}6\times10^{-7}\ \mathrm{m\,s^{-1}}.$$

**3. Détermination de $\lambda_0$ et $\sigma_0$.** Sur l'enregistrement $I(t)$, on mesure la durée $\Delta t$ pendant laquelle défilent les $N=480$ franges comptées. On a $N=\frac{\Delta t}{T_0}$, donc $T_0=\frac{\Delta t}N$ et
$$\lambda_0=2V_0T_0=\frac{2V_0\Delta t}N,\qquad\sigma_0=\frac1{\lambda_0}.$$
Autrement dit, le miroir s'est déplacé de $V_0\Delta t=N\frac{\lambda_0}2$.

**3. Détermination de $b$.** On mesure sur l'enregistrement la demi-largeur $\tau$ de l'enveloppe (à $\frac1e$ du contraste maximal), d'où $b=\frac1{2\pi V_0\tau}$.

**3. Vérification de $b\ll\sigma_0$.** Si les 480 franges sont celles que l'on voit sous l'enveloppe, entre $-\tau$ et $+\tau$ environ, alors $N\approx\frac{2\tau}{T_0}=\frac{2\sigma_0}{\pi b}$, d'où
$$\frac b{\sigma_0}\approx\frac2{\pi N}=\frac2{\pi\times480}\approx1{,}3\times10^{-3}\ll1.$$
L'hypothèse est largement vérifiée, et la source est quasi monochromatique.

**Interprétation.** Le terme d'interférences de $I(\delta)$ est la transformée de Fourier (en cosinus) du spectre : un spectre de largeur $b$ donne un interférogramme de largeur $\sim\frac1b$ en $\delta$. C'est la longueur de cohérence $\ell_c\sim\frac1{\pi b}$. C'est le principe de la spectroscopie par transformée de Fourier.
"""

D['p-opt-ccmp1'] = r"""
**1. Géométrie.** On note $S_1$ et $S_2$ les trous, distants de $a$, symétriques par rapport à l'axe $Oz$ ; $S$ est sur l'axe, et l'écran est à la distance $D$ des trous. Un point $M$ de l'écran a pour coordonnées $(x,y)$, l'axe $x$ étant parallèle à $S_1S_2$, avec $S_{1,2}=(\mp\frac a2,0,0)$.

**1. Calcul des chemins.**
$$S_2M=\sqrt{D^2+\Big(x-\frac a2\Big)^2+y^2},\qquad S_1M=\sqrt{D^2+\Big(x+\frac a2\Big)^2+y^2}.$$
Pour $a,|x|,|y|\ll D$, au premier ordre : $S_iM\approx D+\frac{(x\pm a/2)^2+y^2}{2D}$. Donc
$$\delta=S_1M-S_2M\approx\frac{(x+a/2)^2-(x-a/2)^2}{2D}=\frac{ax}D.$$
Comme $S$ est sur l'axe, $SS_1=SS_2$ : il n'y a pas de différence de marche avant les trous.

**1. Ordre et éclairement.** L'ordre d'interférence vaut $p=\frac\delta\lambda=\frac{ax}{\lambda D}$, et
$$I(x)=2I_0\Big[1+\cos\Big(\frac{2\pi ax}{\lambda D}\Big)\Big].$$

**1. Nature des franges.** $I$ ne dépend que de $x$ : les franges sont des **droites perpendiculaires à $S_1S_2$**, équidistantes, d'interfrange $i=\frac{\lambda D}a$. La frange centrale ($x=0$, $p=0$) est brillante. (Rigoureusement, les surfaces d'égale différence de marche sont des hyperboloïdes de foyers $S_1$ et $S_2$, dont l'intersection avec l'écran, loin des trous, est quasi rectiligne.)

**2. Source déplacée.** On déplace $S$ de $y_s$ parallèlement à $S_1S_2$, à la distance $d$ du plan des trous. Par le même calcul, $SS_2-SS_1\approx\frac{ay_s}d$ : une différence de marche apparaît en amont des trous. Au total,
$$\delta=\frac{ax}D+\frac{ay_s}d.$$
La frange d'ordre 0 passe en $x_0=-\frac Ddy_s$ : le système de franges est **translaté en bloc**, d'une quantité $\frac Dd|y_s|$, en sens opposé au déplacement de la source. L'interfrange ne change pas.

**2. Direction sensible.** Un déplacement de $S$ perpendiculaire à $S_1S_2$ (parallèle aux franges) laisse $SS_1=SS_2$ au premier ordre : il ne change rien. Seuls les déplacements **parallèles à $S_1S_2$** modifient la figure.

**3. Source étendue.** Une source de largeur $\ell$ (selon la direction de $S_1S_2$) est une juxtaposition de sources ponctuelles **incohérentes** entre elles : leurs éclairements s'ajoutent. Chacune donne un système de franges décalé. Le décalage entre les systèmes extrêmes vaut $\frac Dd\ell$.

**3. Critère semi-quantitatif.** Les franges se brouillent quand ce décalage atteint une interfrange : $\frac Dd\ell\approx\frac{\lambda D}a$, soit $\ell\approx\frac{\lambda d}a$.

**3. Calcul exact.** Avec une source uniforme, on intègre sur $y_s\in[-\frac\ell2,\frac\ell2]$ :
$$I(x)\propto\int_{-\ell/2}^{\ell/2}\Big[1+\cos\Big(\frac{2\pi a}\lambda\Big(\frac xD+\frac{y_s}d\Big)\Big)\Big]\mathrm dy_s=\ell\Big[1+\mathrm{sinc}\Big(\frac{\pi a\ell}{\lambda d}\Big)\cos\Big(\frac{2\pi ax}{\lambda D}\Big)\Big].$$
Le contraste vaut $C=\big|\mathrm{sinc}\big(\frac{\pi a\ell}{\lambda d}\big)\big|$. Il s'annule pour la première fois en $\ell=\frac{\lambda d}a$.

**3. Conclusion.** Pour conserver des interférences bien contrastées, il faut
$$\ell<\frac{\lambda d}a.$$
On utilise une fente fine parallèle aux franges, qui laisse passer plus de lumière sans brouiller. Réciproquement, la disparition des franges quand on écarte les trous permet de mesurer la taille angulaire $\frac\ell d$ d'une source : c'est l'interféromètre stellaire de Michelson, qui mesure le diamètre apparent des étoiles.
"""
