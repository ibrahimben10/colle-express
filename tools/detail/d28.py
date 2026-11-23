D = {}

D['p-meca-1'] = r"""
**1. Référentiel et paramétrage.** On travaille dans le référentiel $\mathcal R'$ lié au boîtier. Il est en translation par rapport au sol galiléen, avec la position $Z(t)=H\cos\omega t$ et l'accélération $\ddot Z\vec u_z=-H\omega^2\cos(\omega t)\vec u_z$. $z$ est la cote de $M$ **par rapport au boîtier**, avec l'origine à la position d'équilibre au repos.

**1. Bilan des forces dans $\mathcal R'$.**
- Poids : $-mg\vec u_z$.
- Tension du ressort : à l'équilibre au repos, elle compense le poids ; un déplacement $z$ (relatif au boîtier, auquel le ressort est accroché) la modifie de $-kz\vec u_z$. Poids + tension $=-kz\vec u_z$.
- Frottement fluide (sur le guide, solidaire du boîtier) : $-\lambda\dot z\vec u_z$.
- Force d'inertie d'entraînement : $-m\ddot Z\vec u_z=mH\omega^2\cos(\omega t)\vec u_z$.
- Pas de force de Coriolis, car le référentiel est en translation.

**1. Équation du mouvement.**
$$m\ddot z+\lambda\dot z+kz=mH\omega^2\cos\omega t.$$

**1. Régime sinusoïdal forcé.** On pose $\omega_0^2=\frac km$ et $z=\mathrm{Re}(\underline ze^{i\omega t})$. Avec $\frac{\mathrm d}{\mathrm dt}\to i\omega$ :
$$\Big(-\omega^2+i\omega\frac\lambda m+\omega_0^2\Big)\underline z=H\omega^2\iff\underline z=\frac{H\omega^2}{\omega_0^2-\omega^2+i\frac{\lambda\omega}m}.$$
L'amplitude est le module :
$$Z_m(\omega)=|\underline z|=\frac{H\omega^2}{\sqrt{(\omega_0^2-\omega^2)^2+\big(\frac{\lambda\omega}m\big)^2}}.$$

**1. Comportements limites.**
- $\omega\ll\omega_0$ : $Z_m\approx H\frac{\omega^2}{\omega_0^2}\to0$. La masse suit le boîtier, et rien n'est mesuré.
- $\omega\gg\omega_0$ : $Z_m\to H$, et $\underline z\approx\frac{H\omega^2}{-\omega^2}=-H$.

C'est un **filtre passe-haut** du second ordre, avec une éventuelle résonance près de $\omega_0$ si l'amortissement est faible.

**2. Fonctionnement.** Pour $\omega\gg\omega_0$, $z(t)\approx-H\cos\omega t=-Z(t)$. La position absolue de $M$, $Z+z\approx0$, est quasi constante : la masse reste immobile par inertie, et le stylet relié à $M$ enregistre sur le boîtier (qui bouge avec le sol) exactement le mouvement du sol, au signe près.

**2. Conception.** Il faut que $\omega_0$ soit petit devant les pulsations sismiques (périodes de 0,1 à quelques secondes) : on utilise un ressort souple et une grande masse. On choisit un amortissement proche du critique, avec un facteur de qualité $Q=\frac{m\omega_0}\lambda\approx\frac1{\sqrt2}$, pour supprimer la résonance et obtenir une réponse plate au-delà de $\omega_0$.
"""

D['p-meca-2'] = r"""
**1. Force d'inertie d'entraînement.** Pour un référentiel en translation d'accélération $\vec A$ par rapport à un référentiel galiléen, l'accélération d'entraînement de tout point est $\vec A$. Donc
$$\vec f_{ie}=-m\vec A=-mA\,\vec u_x.$$
Cette force est uniforme et constante, comme un poids.

**2. Énergie potentielle.** On cherche $E_{p,ie}$ tel que $\vec f_{ie}=-\overrightarrow{\mathrm{grad}}\,E_{p,ie}$, soit $\frac{\partial E_{p,ie}}{\partial x}=mA$ et $\frac{\partial E_{p,ie}}{\partial y}=\frac{\partial E_{p,ie}}{\partial z}=0$. Donc
$$E_{p,ie}=mAx+\text{cste}=mAx\quad(\text{référence en }x=0).$$
Équivalent : le travail élémentaire $\delta W=\vec f_{ie}\cdot\mathrm d\vec r=-mA\,\mathrm dx=-\mathrm d(mAx)$. Elle est l'analogue d'une énergie potentielle de pesanteur, mais horizontale.

**3.(a) Position du pendule.** On repère le pendule par l'angle $\theta$ entre le fil et la verticale descendante, positif vers $+\vec u_x$ (sens de $\vec A$). Le point de suspension est pris à l'origine, et $\vec u_z$ est vertical ascendant : $x=L\sin\theta$ et $z=-L\cos\theta$.

**3.(a) Énergie potentielle totale.** Elle somme l'énergie de pesanteur, $mgz$, et celle d'entraînement, $mAx$ ; la tension du fil ne travaille pas (elle est perpendiculaire à la vitesse) :
$$E_p(\theta)=-mgL\cos\theta+mAL\sin\theta.$$

**3.(a) Équilibre.**
$$E_p'(\theta)=mL(g\sin\theta+A\cos\theta)=0\iff\tan\theta_{eq}=-\frac Ag.$$
On distingue deux solutions sur $]-\pi,\pi]$, et on regarde la dérivée seconde $E_p''(\theta)=mL(g\cos\theta-A\sin\theta)$.
- $\theta_{eq}\in\big]-\frac\pi2,0\big[$, avec $\cos\theta_{eq}=\frac g{\sqrt{g^2+A^2}}$ et $\sin\theta_{eq}=-\frac A{\sqrt{g^2+A^2}}$. Alors $E_p''=mL\sqrt{g^2+A^2}>0$ : c'est un minimum, donc l'**équilibre stable**.
- L'autre solution, $\theta_{eq}+\pi$, est un maximum : équilibre instable.

Le pendule s'incline **vers l'arrière** (côté opposé à $\vec A$), d'un angle $\arctan\frac Ag$ : le fil est aligné avec la « pesanteur apparente » $\vec g_{\mathrm{app}}=\vec g-\vec A$.

**3.(b) Conservation de l'énergie.** Dans le référentiel du train, les forces sont conservatives (poids et inertie d'entraînement) ou ne travaillent pas (tension), et il n'y a pas de Coriolis (translation). L'énergie mécanique se conserve :
$$E_m=\frac12mL^2\dot\theta^2-mgL\cos\theta+mAL\sin\theta=\text{cste}.$$

**3.(b) Équation du mouvement.** On dérive par rapport au temps :
$$mL^2\dot\theta\ddot\theta+mgL\sin\theta\,\dot\theta+mAL\cos\theta\,\dot\theta=0.$$
En simplifiant par $mL^2\dot\theta$ (le mouvement n'est pas l'équilibre) :
$$\ddot\theta+\frac gL\sin\theta+\frac AL\cos\theta=0.$$

**3.(b) Petites oscillations.** Autour de $\theta_{eq}$, posons $\theta=\theta_{eq}+\varepsilon$ ; au premier ordre, $\ddot\varepsilon+\frac{E_p''(\theta_{eq})}{mL^2}\varepsilon=0$. La pulsation vaut donc
$$\omega=\sqrt{\frac{\sqrt{g^2+A^2}}L}.$$
C'est la pulsation d'un pendule simple dans la pesanteur apparente $g'=\sqrt{g^2+A^2}$.
"""

D['p-meca-3'] = r"""
**1. Tension du fil.** Soit $S$ le point d'attache, $L$ la longueur du fil, et $M$ à la distance $r$ de la verticale de $S$. Pour de petites oscillations ($r\ll L$), le fil est quasi vertical et $M$ reste quasi à altitude constante. La projection verticale du principe fondamental donne $T\cos\alpha-mg\approx0$, avec $\alpha\approx\frac rL\ll1$, donc $T\approx mg$. La tension est dirigée de $M$ vers $S$ : $\vec T=-\frac T L\overrightarrow{SM}$. La composante horizontale de $\overrightarrow{SM}$ vaut $r\vec u_r$, d'où
$$\vec f\simeq-\frac{mg}Lr\,\vec u_r.$$

**2. Forces d'inertie.** Le référentiel du plateau tourne à $\vec\Omega=\Omega\vec u_z$ constant.
- **Entraînement (centrifuge)** : $\vec f_{ie}=m\Omega^2r\,\vec u_r$, où $r$ est la distance à l'axe. On suppose le mât sur l'axe de rotation.
- **Coriolis** : $\vec f_{ic}=-2m\vec\Omega\wedge\vec v_r$, avec $\vec v_r=\dot r\vec u_r+r\dot\theta\vec u_\theta$. Comme $\vec u_z\wedge\vec u_r=\vec u_\theta$ et $\vec u_z\wedge\vec u_\theta=-\vec u_r$, on obtient $\vec\Omega\wedge\vec v_r=\Omega(\dot r\vec u_\theta-r\dot\theta\vec u_r)$, et
$$\vec f_{ic}=2m\Omega r\dot\theta\,\vec u_r-2m\Omega\dot r\,\vec u_\theta.$$

**2. Équations du mouvement.** L'accélération en polaires est $(\ddot r-r\dot\theta^2)\vec u_r+(r\ddot\theta+2\dot r\dot\theta)\vec u_\theta$. En projetant le principe fondamental dans le référentiel tournant :
$$\ddot r-r\dot\theta^2=-\frac gLr+\Omega^2r+2\Omega r\dot\theta,\qquad r\ddot\theta+2\dot r\dot\theta=-2\Omega\dot r.$$

**3. Vérification de $\theta=-\Omega t$.** On a $\dot\theta=-\Omega$ et $\ddot\theta=0$.
- Seconde équation : $0+2\dot r(-\Omega)=-2\Omega\dot r$. ✓
- Première équation : $\ddot r-\Omega^2r=-\frac gLr+\Omega^2r-2\Omega^2r=-\frac gLr-\Omega^2r$, donc
$$\ddot r+\omega_0^2r=0,\qquad\omega_0=\sqrt{\frac gL}.$$

**3. Interprétation.** $\theta=-\Omega t$ dans le référentiel tournant signifie que la direction du mouvement est **fixe dans le référentiel du laboratoire** : le pendule oscille dans un plan vertical immobile, pendant que le plateau tourne en dessous. C'est normal, car dans le laboratoire (galiléen), aucune force ne fait tourner le plan d'oscillation.

**3. Résolution.** Si $M$ est lâché depuis $r_0$ sans vitesse dans le laboratoire, alors $r(t)=r_0\cos(\omega_0t)$. Ici $r$ est une abscisse algébrique le long de la droite d'oscillation : quand $r<0$, $M$ est de l'autre côté de l'axe.

**4. Comptage des pétales.** Vue du plateau, la droite d'oscillation tourne à la vitesse $-\Omega$. $M$ passe par le centre à chaque demi-période $\frac\pi{\omega_0}$, et chaque excursion entre deux passages au centre trace un pétale. Pendant un tour du plateau, de durée $\frac{2\pi}\Omega$, le nombre de pétales vaut
$$N=\frac{2\pi/\Omega}{\pi/\omega_0}=\frac{2\omega_0}\Omega.$$

**4. Condition.** Pour une rosace fermée à six pétales, il faut $N=6$, ce qui assure aussi la fermeture puisque $\frac{\omega_0}\Omega$ est alors entier :
$$\omega_0=3\Omega\iff\frac gL=9\Omega^2.$$
"""

D['p-meca-4'] = r"""
**1. Pas de force d'entraînement explicite.** Le poids $m\vec g$ mesuré dans le référentiel terrestre est la somme de l'attraction gravitationnelle et de la force d'inertie d'entraînement (axifuge) : $\vec g=\vec g_{\mathrm{grav}}+\Omega^2\overrightarrow{HM}$. La force d'entraînement est donc déjà incluse dans le poids. On néglige en outre la variation de $\vec g$ le long de la chute.

**2. Vecteur rotation.** $\vec\Omega$ est porté par l'axe des pôles, vers le nord. Au point $O$, de latitude $\lambda$, l'axe des pôles fait l'angle $\lambda$ avec l'horizontale dirigée vers le nord ($\vec u_y$), dans le plan méridien. Donc
$$\vec\Omega=\Omega\big(0\,\vec u_x+\cos\lambda\,\vec u_y+\sin\lambda\,\vec u_z\big)=\Omega(0,C,S).$$

**3. Force de Coriolis.** Avec $\vec v=(\dot x,\dot y,\dot z)$ :
$$\vec\Omega\wedge\vec v=\Omega\begin{pmatrix}C\dot z-S\dot y\\S\dot x-0\\0-C\dot x\end{pmatrix},\qquad-2m\vec\Omega\wedge\vec v=2m\Omega\begin{pmatrix}S\dot y-C\dot z\\-S\dot x\\C\dot x\end{pmatrix}.$$

**3. Système différentiel.**
$$\ddot x=2\Omega(S\dot y-C\dot z),\qquad\ddot y=-2\Omega S\dot x,\qquad\ddot z=-g+2\Omega C\dot x,$$
avec, à $t=0$, $x=y=z=0$ et $\dot x=\dot y=\dot z=0$.

**4. Intégration des deux dernières équations.** En intégrant de $0$ à $t$ (conditions initiales nulles) :
$$\dot y=-2\Omega Sx,\qquad\dot z=-gt+2\Omega Cx.$$

**4. Équation en $x$ seule.** En reportant dans la première équation :
$$\ddot x=2\Omega\big(-2\Omega S^2x+Cgt-2\Omega C^2x\big)=-4\Omega^2x+2\Omega Cg\,t,$$
car $S^2+C^2=1$. Donc $\ddot x+4\Omega^2x=2\Omega Cg\,t$.

**4. Résolution en $x$.** Une solution particulière affine est $x_p=\frac{2\Omega Cgt}{4\Omega^2}=\frac{Cg}{2\Omega}t$. La solution générale s'écrit $x=A\cos2\Omega t+B\sin2\Omega t+\frac{Cg}{2\Omega}t$.
- $x(0)=0$ donne $A=0$.
- $\dot x(0)=0$ donne $2\Omega B+\frac{Cg}{2\Omega}=0$, soit $B=-\frac{Cg}{4\Omega^2}$.

$$x(t)=\frac{Cg}{4\Omega^2}\big(2\Omega t-\sin2\Omega t\big).$$

**4. Résolution en $y$ et $z$.** En intégrant $\dot y=-2\Omega Sx$ et $\dot z=-gt+2\Omega Cx$, avec $\int_0^t(2\Omega t'-\sin2\Omega t')\,\mathrm dt'=\Omega t^2-\frac{1-\cos2\Omega t}{2\Omega}$ :
$$y(t)=-\frac{SCg}{2\Omega}\Big(\Omega t^2-\frac{1-\cos2\Omega t}{2\Omega}\Big),\qquad z(t)=-\frac{gt^2}2+\frac{C^2g}{2\Omega}\Big(\Omega t^2-\frac{1-\cos2\Omega t}{2\Omega}\Big).$$

**5. Développements limités.** Avec $u=2\Omega t$, $\sin u=u-\frac{u^3}6+o(u^3)$ et $1-\cos u=\frac{u^2}2-\frac{u^4}{24}+o(u^4)$ :
- $2\Omega t-\sin2\Omega t=\frac{8\Omega^3t^3}6+o(t^3)$, donc $x(t)\approx\frac{Cg}{4\Omega^2}\cdot\frac43\Omega^3t^3=\frac13\Omega g\cos\lambda\,t^3$ ;
- $\Omega t^2-\frac{1-\cos2\Omega t}{2\Omega}=\Omega t^2-\big(\Omega t^2-\frac{\Omega^3t^4}3\big)=\frac{\Omega^3t^4}3$, donc $y\approx-\frac{SCg\Omega^2t^4}6$ et $z\approx-\frac{gt^2}2+\frac{C^2g\Omega^2t^4}6$.

**5. Interprétation.** Par rapport à la chute libre $\frac{gt^2}2$, $x$ est d'ordre $\Omega t$ (premier ordre), tandis que $y$ et la correction sur $z$ sont d'ordre $(\Omega t)^2$, négligeables. $x>0$ quelle que soit l'hémisphère ($C=\cos\lambda>0$) : le corps est dévié **vers l'est**. C'est la déviation vers l'est, maximale à l'équateur et nulle aux pôles. Explication dans le référentiel géocentrique : au départ, le corps a la vitesse vers l'est du haut du puits, plus grande que celle du fond (plus proche de l'axe), donc il « prend de l'avance » vers l'est.

**6. Application numérique.** $h=400$ m, donc $t=\sqrt{\frac{2h}g}=\sqrt{\frac{800}{9{,}81}}\approx9{,}03$ s et $t^3\approx737\ \mathrm s^3$. $\Omega=\frac{2\pi}{86\,164}\approx7{,}29\times10^{-5}\ \mathrm{rad\,s^{-1}}$, et $\Omega t\approx6{,}6\times10^{-4}\ll1$ : le développement est justifié.
- À la latitude de Paris ($\lambda\approx48{,}9^\circ$, $C\approx0{,}66$) : $x\approx\frac13\times7{,}29\times10^{-5}\times9{,}81\times0{,}66\times737\approx0{,}12$ m.
- À l'équateur ($C=1$) : $x\approx0{,}18$ m.

La déviation est d'une dizaine de centimètres : petite, mais mesurable (expériences de Reich en 1831 dans un puits de mine).
"""

D['p-meca-5'] = r"""
**1. Tension du fil.** Pour de petites oscillations, le fil reste quasi vertical : l'angle avec la verticale vaut $\alpha\approx\frac{SM_{\perp}}L\ll1$, où $SM_\perp$ est la distance horizontale. La projection verticale du principe fondamental (la masse reste quasi à altitude constante, $\ddot z\approx0$) donne $T\cos\alpha\approx mg$, donc $T\approx mg$ à l'ordre 1. La tension est portée par $\overrightarrow{MS}$, de norme $L$ :
$$\vec T=-\frac TL\overrightarrow{SM}\simeq-\frac{mg}L\overrightarrow{SM}.$$
Ses composantes horizontales valent $-\frac{mg}Lx$ et $-\frac{mg}Ly$, avec l'origine sur la verticale de $S$.

**2. Force de Coriolis horizontale.** On reprend $\vec\Omega=\Omega(0,C,S)$, avec $C=\cos\lambda$ et $S=\sin\lambda$. Le mouvement est horizontal, $\vec v\approx(\dot x,\dot y,0)$, donc
$$\vec\Omega\wedge\vec v=\Omega\big(-S\dot y,\ S\dot x,\ -C\dot x\big),\qquad-2m\vec\Omega\wedge\vec v=2m\Omega\big(S\dot y,\ -S\dot x,\ C\dot x\big).$$
La composante verticale, $2m\Omega C\dot x$, est compensée par une infime variation de la tension et n'intervient pas.

**2. Équations du mouvement.** Les projections horizontales du principe fondamental, divisées par $m$, donnent
$$\ddot x+\omega_0^2x=2\beta\dot y,\qquad\ddot y+\omega_0^2y=-2\beta\dot x,\qquad\omega_0=\sqrt{\frac gL},\qquad\beta=\Omega\sin\lambda.$$

**3. Ordres de grandeur.**
- $\omega_0=\sqrt{\frac{9{,}81}{67}}=\sqrt{0{,}146}\approx0{,}383\ \mathrm{rad\,s^{-1}}$, soit une période $\frac{2\pi}{\omega_0}\approx16{,}4$ s.
- $\beta=\frac{2\pi}{86\,164}\times\sin48{,}85^\circ=7{,}29\times10^{-5}\times0{,}753\approx5{,}49\times10^{-5}\ \mathrm{rad\,s^{-1}}$.

Le rapport $\frac\beta{\omega_0}\approx1{,}4\times10^{-4}$ montre que $\beta\ll\omega_0$.

**4. Équation complexe.** On pose $\rho=x+iy$. On forme (première équation) $+\,i\times$(seconde) :
$$\ddot\rho+\omega_0^2\rho=2\beta(\dot y-i\dot x)=-2i\beta(\dot x+i\dot y)=-2i\beta\dot\rho.$$
Donc $\ddot\rho+2i\beta\dot\rho+\omega_0^2\rho=0$.

**4. Changement de fonction.** On pose $\rho=e^{-i\beta t}u$. Alors $\dot\rho=e^{-i\beta t}(\dot u-i\beta u)$ et $\ddot\rho=e^{-i\beta t}(\ddot u-2i\beta\dot u-\beta^2u)$. En substituant :
$$\ddot u-2i\beta\dot u-\beta^2u+2i\beta\dot u+2\beta^2u+\omega_0^2u=0\iff\ddot u+(\omega_0^2+\beta^2)u=0.$$

**4. Conditions initiales.** $u(0)=\rho(0)=a$ et $\dot u(0)=\dot\rho(0)+i\beta\rho(0)=i\beta a$. Avec $\omega=\sqrt{\omega_0^2+\beta^2}$ :
$$u(t)=a\cos\omega t+\frac{i\beta a}\omega\sin\omega t\approx a\cos\omega_0t,$$
car $\frac\beta\omega\approx1{,}4\times10^{-4}$ et $\omega\approx\omega_0$ (à $10^{-8}$ près en valeur relative). Donc
$$\rho(t)\approx a\cos(\omega_0t)\,e^{-i\beta t}.$$

**5. Rotation du plan d'oscillation.** En prenant parties réelle et imaginaire :
$$x(t)\approx a\cos(\omega_0t)\cos(\beta t),\qquad y(t)\approx-a\cos(\omega_0t)\sin(\beta t).$$
À chaque instant, $M$ est sur la droite passant par l'origine et faisant l'angle $-\beta t$ avec $\vec u_x$ : il oscille rapidement (période 16,4 s) le long d'une droite qui tourne lentement, à la vitesse angulaire
$$\Omega_F=\beta=\Omega\sin\lambda,$$
dans le sens **horaire** vu de dessus (angle décroissant) dans l'hémisphère nord.

**6. Période de Foucault.**
$$T_F=\frac{2\pi}{\Omega\sin\lambda}=\frac{86\,164\ \mathrm s}{\sin48{,}85^\circ}=\frac{86\,164}{0{,}753}\approx1{,}14\times10^5\ \mathrm s\approx31{,}8\ \mathrm h.$$
Le plan ne fait un tour en un jour sidéral qu'aux pôles ($\sin\lambda=1$), et ne tourne pas à l'équateur. C'est la preuve expérimentale (Foucault, 1851) de la rotation de la Terre, sans observation astronomique. (La masse $m=28$ kg n'intervient pas dans le mouvement : une grande masse sert seulement à limiter l'effet relatif des frottements.)
"""
