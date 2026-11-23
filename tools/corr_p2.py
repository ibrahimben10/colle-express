
# Indices et corrigés — Mécanique, optique, quantique, statistique, thermodynamique
C = {}
def c(id, h1, h2, h3, corrige, reponse=""):
    C[id] = {"indices": [h1.strip(), h2.strip(), h3.strip()], "corrige": corrige.strip(), "reponse": reponse.strip()}

# ---------- Mécanique ----------
c("p-meca-1",
r"Travaille dans le référentiel du boîtier (non galiléen, en translation) : quelle force d'inertie d'entraînement apparaît ?",
r"Avec la cote du boîtier $Z(t)=H\cos\omega t$, la force d'inertie vaut $-m\ddot Z=mH\omega^2\cos\omega t$ : écris l'équation de l'oscillateur forcé pour $z$.",
r"Passe en complexes : $\underline z=\frac{H\omega^2}{\omega_0^2-\omega^2+i\omega\lambda/m}$. Étudie $|\underline z|$ quand $\omega\gg\omega_0$.",
r"""
**1.** Dans le référentiel du boîtier (translation d'accélération $\ddot Z\vec u_z$, $Z=H\cos\omega t$), la masse subit son poids, la tension du ressort, le frottement et la force d'inertie $-m\ddot Z\vec u_z$. Avec $z$ mesuré depuis l'équilibre au repos (le poids est compensé) :
$$m\ddot z+\lambda\dot z+kz=mH\omega^2\cos\omega t.$$
En complexes, avec $\omega_0^2=\frac km$ :
$$\underline z=\frac{H\omega^2}{\omega_0^2-\omega^2+i\omega\frac\lambda m},\qquad|\underline z|=\frac{H\omega^2}{\sqrt{(\omega_0^2-\omega^2)^2+\big(\frac{\lambda\omega}m\big)^2}}.$$
C'est un **filtre passe-haut** du second ordre.

**2.** Pour $\omega\gg\omega_0$ : $|\underline z|\to H$, avec $z\approx-Z$ : la masse reste quasi immobile dans le référentiel terrestre, et son déplacement relatif reproduit fidèlement le mouvement du sol. On choisit donc $\omega_0$ **faible** (ressort souple, grande masse) devant les pulsations sismiques, et un amortissement proche du critique ($Q\approx\frac1{\sqrt2}$) pour éviter la résonance.
""", r"$|\underline z|=\frac{H\omega^2}{\sqrt{(\omega_0^2-\omega^2)^2+(\lambda\omega/m)^2}}\to H$ pour $\omega\gg\omega_0$.")

c("p-meca-2",
r"La force d'inertie d'entraînement d'un référentiel en translation est $-m\vec A$.",
r"Cherche $E_p$ telle que $-\frac{dE_p}{dx}=-mA$ : $E_{p,ie}=mAx$. Pour le pendule, exprime $x$ et $z$ de la masse en fonction de $\theta$.",
r"$E_p(\theta)=-mgL\cos\theta+mAL\sin\theta$ : l'équilibre annule $E_p'(\theta)$ ; dérive l'énergie mécanique pour l'équation du mouvement.",
r"""
**1.** $\vec f_{ie}=-m\vec A=-mA\vec u_x$ (uniforme et constante).

**2.** $\vec f_{ie}=-\overrightarrow{\operatorname{grad}}E_{p,ie}$ avec $E_{p,ie}=mAx$ (référence en $x=0$) : analogue à une énergie potentielle de pesanteur « horizontale ».

**3.(a)** Masse en $x=L\sin\theta$, $z=-L\cos\theta$ ($\theta$ compté depuis la verticale descendante, positif vers $+x$) :
$$E_p(\theta)=-mgL\cos\theta+mAL\sin\theta.$$
$E_p'(\theta)=mL(g\sin\theta+A\cos\theta)=0\iff\tan\theta_{eq}=-\frac Ag$ : le pendule s'incline **vers l'arrière** (fil selon la « pesanteur apparente » $\vec g-\vec A$). L'équilibre stable correspond au minimum : $\cos\theta_{eq}=\frac g{\sqrt{g^2+A^2}}$.

**(b)** Les autres forces (tension) ne travaillent pas : $\frac12mL^2\dot\theta^2+E_p(\theta)=\mathrm{cte}$. En dérivant :
$$\ddot\theta+\frac gL\sin\theta+\frac AL\cos\theta=0.$$
Autour de $\theta_{eq}$, petites oscillations de pulsation $\omega=\sqrt{\frac{\sqrt{g^2+A^2}}L}$ (pendule dans une pesanteur apparente $g'=\sqrt{g^2+A^2}$).
""", r"$E_{p,ie}=mAx$ ; $\tan\theta_{eq}=-A/g$ ; $\ddot\theta+\frac gL\sin\theta+\frac AL\cos\theta=0$.")

c("p-meca-3",
r"Pour de petites oscillations, la tension vaut environ $mg$ et est dirigée selon $\overrightarrow{MS}$ : projette-la dans le plan horizontal.",
r"Dans le référentiel tournant, ajoute la force centrifuge $m\Omega^2r\vec u_r$ et la force de Coriolis $-2m\vec\Omega\wedge\vec v$, puis projette en coordonnées polaires.",
r"Avec $\theta=-\Omega t$, l'équation radiale devient $\ddot r=-\frac gLr$ : le pendule oscille dans un plan fixe du laboratoire. Compte les pétales par tour.",
r"""
**1.** Le fil est quasi vertical : $T_z\approx mg$, et $\vec T=-\frac T L\overrightarrow{SM}$ a pour composante horizontale $-\frac{mg}Lr\vec u_r$.

**2.** Dans le référentiel tournant (coordonnées polaires $r,\theta$ dans le plan horizontal), avec la force centrifuge $m\Omega^2r\vec u_r$ et la force de Coriolis $-2m\Omega\vec u_z\wedge(\dot r\vec u_r+r\dot\theta\vec u_\theta)=2m\Omega r\dot\theta\vec u_r-2m\Omega\dot r\vec u_\theta$ :
$$\ddot r-r\dot\theta^2=-\frac gLr+\Omega^2r+2\Omega r\dot\theta,\qquad r\ddot\theta+2\dot r\dot\theta=-2\Omega\dot r.$$

**3.** $\theta=-\Omega t$ : la seconde équation donne $-2\Omega\dot r=-2\Omega\dot r$ ✓. La première : $\ddot r-\Omega^2r=-\frac gLr+\Omega^2r-2\Omega^2r$, soit
$$\ddot r+\omega_0^2r=0,\qquad\omega_0=\sqrt{g/L}.$$
Le mouvement est celui d'un pendule oscillant dans un **plan vertical fixe du laboratoire** ($\theta=-\Omega t$ dans le référentiel tournant). $r=r_0\cos(\omega_0t)$.

**4.** Vue du plateau, la trajectoire passe par le centre à chaque demi-période et chaque aller-retour depuis le centre trace un pétale : $2\times\frac{\omega_0}{2\pi}$ pétales par seconde, et le plateau fait un tour en $\frac{2\pi}\Omega$. Une rosace **fermée à six pétales** par tour impose $\frac{2\omega_0}\Omega=6$, soit
$$\omega_0=3\Omega,\quad\text{i.e. }\frac gL=9\Omega^2.$$
""", r"$\theta=-\Omega t$ : $\ddot r+\frac gLr=0$ ; six pétales : $\sqrt{g/L}=3\Omega$.")

c("p-meca-4",
r"La force d'inertie d'entraînement est incluse dans le poids (définition du champ de pesanteur terrestre).",
r"$\vec\Omega=\Omega(0,C,S)$ dans la base (est, nord, verticale). Écris $-2m\vec\Omega\wedge\vec v$ et projette.",
r"Résous par perturbation : à l'ordre 0, $\dot z=-gt$ ; reporte dans l'équation en $x$ pour obtenir la déviation à l'ordre 1 en $\Omega$.",
r"""
**1.** La pesanteur $\vec g$ est définie dans le référentiel terrestre : elle inclut l'attraction et la force d'inertie d'entraînement (centrifuge). Il ne reste que la force de Coriolis.

**2.** Avec $\vec u_x$ vers l'est, $\vec u_y$ vers le nord, $\vec u_z$ vertical ascendant : $\vec\Omega=\Omega(0,\ C,\ S)$, avec $C=\cos\lambda$, $S=\sin\lambda$.

**3.** $\vec\Omega\wedge\vec v=\Omega\big(C\dot z-S\dot y,\ S\dot x,\ -C\dot x\big)$, donc
$$\ddot x=2\Omega(S\dot y-C\dot z),\qquad\ddot y=-2\Omega S\dot x,\qquad\ddot z=-g+2\Omega C\dot x.$$
(La base de l'énoncé est orientée différemment, d'où des signes et des rôles de $x,y$ échangés dans ses formules ; la physique est la même.)

**4–5.** Le système linéaire se résout exactement (combinaison des équations : $\ddot u+4\Omega^2u=\dots$), mais comme $\Omega t\ll1$ pendant la chute, un développement à l'ordre 1 en $\Omega$ suffit. À l'ordre 0 : $x=y=0$, $\dot z=-gt$, $z=-\frac{gt^2}2$. Reporté :
$$\ddot x\approx-2\Omega C\dot z=2\Omega Cgt\ \Rightarrow\ x(t)\approx\frac13\Omega Cg\,t^3>0,$$
et $y=O(\Omega^2)$. Le corps est dévié **vers l'est** (au nord comme au sud de l'équateur) : c'est la **déviation vers l'est**, maximale à l'équateur.

**6.** $h=400$ m : $t=\sqrt{2h/g}\approx9{,}0$ s. À la latitude de Paris ($C\approx0{,}66$) : $x\approx\frac13\times7{,}29\times10^{-5}\times0{,}66\times9{,}81\times9{,}03^3\approx0{,}12$ m. Soit **une dizaine de centimètres** (à l'équateur : environ 18 cm).
""", r"$x\approx\frac13\Omega g\cos\lambda\,t^3$ vers l'est : $\approx12$ cm pour 400 m à Paris.")

c("p-meca-5",
r"Pour de petites oscillations, $T\approx mg$ ; écris $\vec T=-\frac TL\overrightarrow{SM}$ et projette sur le plan horizontal.",
r"La force de Coriolis horizontale est $-2m\Omega\sin\lambda\,\vec u_z\wedge\vec v$ (la composante horizontale de $\vec\Omega$ donne une force verticale, compensée par $T$).",
r"Avec $\rho=x+iy$ : $\ddot\rho+2i\beta\dot\rho+\omega_0^2\rho=0$. Cherche $\rho=e^{-i\beta t}u$ et néglige $\beta^2$ devant $\omega_0^2$.",
r"""
**1.** Le fil est quasi vertical, $T\approx mg$, donc $\vec T\simeq-\frac{mg}L\overrightarrow{SM}$, de composantes horizontales $-\frac{mg}Lx$, $-\frac{mg}Ly$.

**2.** Dans le plan horizontal, la force de Coriolis s'écrit $-2m\Omega S\,\vec u_z\wedge\vec v=2m\Omega S(\dot y,-\dot x)$ (la partie liée à $\Omega C$ est verticale ou d'ordre supérieur). D'où
$$\ddot x+\omega_0^2x=2\beta\dot y,\qquad\ddot y+\omega_0^2y=-2\beta\dot x,\qquad\omega_0=\sqrt{\frac gL},\quad\beta=\Omega\sin\lambda.$$

**3.** $\omega_0=\sqrt{9{,}81/67}\approx0{,}38\ \mathrm{rad\,s^{-1}}$ (période $16{,}4$ s), $\beta=7{,}29\times10^{-5}\times\sin48{,}85^\circ\approx5{,}5\times10^{-5}\ \mathrm{rad\,s^{-1}}$ : $\beta\ll\omega_0$.

**4.** $\rho=x+iy$ vérifie $\ddot\rho+2i\beta\dot\rho+\omega_0^2\rho=0$. Avec $\rho=e^{-i\beta t}u$ : $\ddot u+(\omega_0^2+\beta^2)u=0\approx\ddot u+\omega_0^2u$. Avec les conditions initiales ($u(0)=a$, $\dot u(0)=i\beta a\approx0$) :
$$\rho(t)\approx a\cos(\omega_0t)\,e^{-i\beta t}.$$

**5.** $x=a\cos\omega_0t\cos\beta t$, $y=-a\cos\omega_0t\sin\beta t$ : allers-retours quasi rectilignes de longueur $2a$ sur une droite qui tourne lentement dans le **sens horaire** (hémisphère nord) à la vitesse angulaire $\Omega_F=\Omega\sin\lambda$.

**6.** $T_F=\frac{2\pi}{\Omega\sin\lambda}=\frac{23\ \mathrm h\,56\ \mathrm{min}}{\sin48{,}85^\circ}\approx31{,}8$ h. (Le plan ne fait un tour en un jour qu'aux pôles.)
""", r"$\rho\approx a\cos(\omega_0t)e^{-i\Omega\sin\lambda\,t}$ ; $T_F=\frac{2\pi}{\Omega\sin\lambda}\approx31{,}8$ h.")

c("p-meca-6",
r"Sans frottement, la force magnétique ne travaille pas : le mouvement est circulaire uniforme. Quel est le rayon ?",
r"Avec frottement, la puissance de la force magnétique reste nulle : $\frac{d}{dt}\big(\frac12mv^2\big)=-\frac m\tau v^2$.",
r"Pose $\underline w=v_x+iv_y$ : $\dot{\underline w}=-\big(\frac1\tau+i\omega\big)\underline w$. Intègre pour obtenir la position, puis fais $t\to\infty$.",
r"""
Notons $\omega=\frac{qB_0}m$.

**1.** $m\dot{\vec v}=q\vec v\wedge\vec B$ : $\vec B$ ne travaille pas, $\|\vec v\|=v_0$. Le mouvement est **circulaire uniforme** dans le plan $(Oxy)$, de rayon $R=\frac{v_0}\omega=\frac{mv_0}{qB_0}$, parcouru dans le sens horaire (pour $q>0$, $\vec B$ selon $+\vec u_z$), centre en $(0,-R)$.

**2.** $\frac d{dt}\big(\frac12mv^2\big)=-\frac m\tau v^2$ donc $v(t)=v_0e^{-t/\tau}$ et la longueur totale parcourue est $L=\int_0^\infty v\,dt=v_0\tau$.

**3.** Avec $\underline w=v_x+iv_y$ : $\dot{\underline w}=-i\omega\underline w-\frac1\tau\underline w$ (car $(\vec v\wedge\vec u_z)$ correspond à $-i\underline w$), d'où $\underline w=v_0e^{-(1/\tau+i\omega)t}$ :
$$v_x=v_0e^{-t/\tau}\cos\omega t,\qquad v_y=-v_0e^{-t/\tau}\sin\omega t.$$

**4.** $\underline z_\infty=\int_0^\infty\underline w\,dt=\frac{v_0}{1/\tau+i\omega}=\frac{v_0\tau(1-i\omega\tau)}{1+\omega^2\tau^2}$, soit
$$x_\infty=\frac{v_0\tau}{1+\omega^2\tau^2},\qquad y_\infty=-\frac{v_0\omega\tau^2}{1+\omega^2\tau^2}.$$

**5.** Une **spirale** (logarithmique) qui s'enroule vers ce point. En chambre à bulles, la mesure du rayon de courbure initial donne $\frac{mv_0}{q}$, et le sens d'enroulement le signe de la charge.
""", r"$v=v_0e^{-t/\tau}$, $L=v_0\tau$ ; point limite $\big(\frac{v_0\tau}{1+\omega^2\tau^2},-\frac{v_0\omega\tau^2}{1+\omega^2\tau^2}\big)$.")

c("p-meca-7",
r"Tant que le cube ne glisse pas, le système {chariot + cube} oscille comme une seule masse $M+m$.",
r"L'accélération maximale est $\omega^2X_m$ avec $\omega^2=\frac k{M+m}$. Quelle force horizontale le cube doit-il recevoir ?",
r"Le frottement statique doit fournir $m\,a$ : la loi de Coulomb impose $|ma|\le\mu mg$.",
r"""
Sans glissement, chariot et cube forment un oscillateur de masse $M+m$ : $x=X_m\cos\omega t$ avec $\omega^2=\frac k{M+m}$.

Le cube n'est soumis horizontalement qu'à la force de frottement $T$ exercée par le chariot : $T=m\ddot x$, maximale en valeur absolue aux extrémités : $|T|_{\max}=m\omega^2X_m$. Verticalement $N=mg$.

Condition de non-glissement (Coulomb) : $|T|\le\mu N$ à chaque instant, soit $m\omega^2X_m\le\mu mg$ :
$$X_m\le X_{\max}=\frac{\mu g}{\omega^2}=\frac{\mu g(M+m)}k.$$
Au-delà, le cube glisse d'abord aux positions extrêmes (là où l'accélération est maximale).
""", r"$X_{\max}=\frac{\mu g(M+m)}k$.")

c("p-meca-8",
r"Dans le référentiel du camion, le tonneau subit son poids, la réaction ($N,T$) et $-m\vec A$ en $G$. Suppose le roulement sans glissement : $\dot x_G=b\omega$.",
r"Théorème de la puissance cinétique avec $E_c=\frac34m\dot x^2$ : seule $-m\vec A$ travaille. Tu obtiens $\ddot x=-\frac{2A}3$.",
r"Calcule $T$ par le théorème de la résultante et compare à $\mu N$. Pour la chute, intègre le mouvement relatif sur la distance disponible.",
r"""
**1.** Référentiel du camion, axe $x$ vers l'avant. Supposons le roulement sans glissement : $\dot x=b\omega$, donc $E_c=\frac12m\dot x^2+\frac12\cdot\frac12mb^2\omega^2=\frac34m\dot x^2$. $N$ et $T$ ne travaillent pas (point de contact immobile), le poids non plus : seule la force d'inertie travaille :
$$\frac32m\dot x\ddot x=-mA\dot x\ \Rightarrow\ \ddot x=-\frac{2A}3.$$
Théorème de la résultante : $m\ddot x=T-mA$, donc $T=\frac{mA}3$, et $N=mg$. Condition de Coulomb $|T|\le\mu N$ :
- **roulement sans glissement** si $A\le3\mu g$ ;
- **glissement** si $A>3\mu g$ (alors $T=\mu mg$, $\ddot x=-(A-\mu g)$).

**2.** Le tonneau part au repos, à la distance $d$ de l'arrière du plateau (à $b$ près). Il recule par rapport au camion avec l'accélération $a_r$ et tombe après $t$ tel que $d=\frac12a_rt^2$. Pendant ce temps le camion parcourt $L=\frac12At^2=d\,\frac A{a_r}$ :
- sans glissement ($a_r=\frac{2A}3$) : $L=\frac32d$, **indépendant de $A$** ;
- avec glissement ($a_r=A-\mu g$) : $L=\frac{dA}{A-\mu g}$.

(En tenant compte du rayon : remplacer $d$ par $d-b$.)
""", r"Roulement sans glissement ssi $A\le3\mu g$ ; alors $L=\frac32d$.")

c("p-meca-9",
r"La plaque ne bascule pas et ne monte pas : écris l'équilibre vertical ($N_1+N_2=mg$) et l'équilibre des moments en $G$.",
r"Tu obtiens $N_1=mg\frac{D/2-x}D$ et $N_2=mg\frac{D/2+x}D$. Il y a glissement : les frottements valent $\mu_dN_1$ et $\mu_dN_2$, en sens opposés.",
r"Le théorème de la résultante horizontal donne $m\ddot x=\mu_d(N_1-N_2)$ : un oscillateur harmonique.",
r"""
Cylindres en $x=\mp\frac D2$, plaque de centre $G$ d'abscisse $x$ ; les cylindres tournent de façon que les surfaces en contact se déplacent vers le centre.

**Réactions normales.** Verticalement : $N_1+N_2=mg$. Moment en $G$ nul (pas de rotation de la plaque ; les frottements sont dans le plan de contact, de bras de levier commun négligeable devant celui des normales) : $N_1\big(\frac D2+x\big)=N_2\big(\frac D2-x\big)$. D'où
$$N_1=mg\,\frac{D/2-x}{D},\qquad N_2=mg\,\frac{D/2+x}{D}.$$

**Frottements.** Il y a glissement aux deux contacts ; la vitesse de glissement de la plaque par rapport à chaque surface est dirigée vers l'extérieur, donc les frottements sont dirigés vers le centre : $+\mu_dN_1$ (cylindre de gauche) et $-\mu_dN_2$ (cylindre de droite) :
$$m\ddot x=\mu_d(N_1-N_2)=-\frac{2\mu_dmg}Dx.$$

**Conclusion :** oscillations harmoniques de pulsation $\omega=\sqrt{\frac{2\mu_dg}D}$, de période
$$T=2\pi\sqrt{\frac D{2\mu_dg}}.$$
(Tant que le glissement persiste, i.e. $|\dot x|$ reste inférieur à la vitesse périphérique des cylindres.) Mesurer $T$ permet de mesurer $\mu_d$. Si les cylindres tournaient en sens inverse, l'équilibre serait instable.
""", r"$m\ddot x=-\frac{2\mu_dmg}Dx$, $T=2\pi\sqrt{\frac D{2\mu_dg}}$.")

c("p-meca-10",
r"Le solide repose sur 5 rouleaux : la réaction normale sur le nouveau rouleau vaut environ $\frac{Mg}5$, et pendant le glissement le frottement vaut $\mu\frac{Mg}5$.",
r"Écris la décélération du solide et l'accélération angulaire du rouleau ($J\dot\omega=TR$) pendant la phase de glissement.",
r"Le glissement cesse quand $\dot X=R\omega$ : calcule cet instant, puis $V_{n+1}$. La suite est géométrique.",
r"""
Modèle : le solide repose sur 5 rouleaux, $N=\frac{Mg}5$ par rouleau. Les anciens rouleaux roulent sans glisser (inertie de mise en rotation déjà acquise) ; seul le nouveau rouleau, initialement immobile, glisse.

**Phase de glissement** ($t=0$ : contact avec le $(n+1)$-ième rouleau). Frottement de glissement $T=\mu N=\frac{\mu Mg}5$ :
$$M\ddot X=-T\Rightarrow\dot X=V_n-\frac{\mu g}5t,\qquad J\dot\omega=TR\Rightarrow\omega=\frac{\mu MgR}{5J}t=\frac{2\mu g}Rt\quad(J=\tfrac12mR^2,\ M=5m).$$
Le glissement cesse quand $\dot X=R\omega$ : $V_n-\frac{\mu g}5t_f=2\mu gt_f$, soit $t_f=\frac{5V_n}{11\mu g}$. Alors
$$V_{n+1}=V_n-\frac{\mu g}5t_f=\frac{10}{11}V_n,\qquad V_n=V_0\Big(\frac{10}{11}\Big)^n.$$

*Vérification par les impulsions* (indépendante de $\mu$) : l'impulsion de frottement $I$ vérifie $M(V_n-V_{n+1})=I$ et $J\frac{V_{n+1}}R=IR$, d'où $(M+\frac m2)V_{n+1}=MV_n$, soit le même rapport $\frac{5}{5{,}5}=\frac{10}{11}$. À chaque rouleau, une fraction de l'énergie est dissipée par frottement : le solide finit par s'arrêter (ici en une infinité de rouleaux, la vitesse décroissant géométriquement).
""", r"$V_n=V_0\big(\frac{10}{11}\big)^n$.")

c("p-meca-ccmp2",
r"À l'équilibre, la poussée d'Archimède compense le poids. Écarte le bloc de $z$ : quelle est la force de rappel ?",
r"La force de rappel vaut $-\rho_eSgz$ et la masse $\rho_bSe$ : déduis $\omega^2=\frac{\rho_eg}{\rho_be}$, puis $\rho_b$ en fonction de $T$.",
r"Une diminution de 10 % par période correspond à un décrément logarithmique $\delta=\ln\frac1{0{,}9}$ : relie-le au facteur de qualité $Q\approx\frac\pi\delta$.",
r"""
**1.** Bloc de section $S$, d'épaisseur $e$, de masse $\rho_bSe$, eau de masse volumique $\rho_e\approx1025\ \mathrm{kg\,m^{-3}}$ (35 g de sel par litre). Si on l'enfonce de $z$ au-delà de l'équilibre, la poussée d'Archimède augmente de $\rho_eSgz$ :
$$\rho_bSe\,\ddot z=-\rho_eSg\,z\ \Rightarrow\ \omega^2=\frac{\rho_eg}{\rho_be}.$$
Donc $\rho_b=\frac{\rho_egT^2}{4\pi^2e}=\frac{1025\times9{,}81\times1^2}{4\pi^2\times0{,}30}\approx850\ \mathrm{kg\,m^{-3}}$ : **oui**, on peut la déterminer (bois dense, type chêne). On néglige la masse d'eau entraînée (masse ajoutée), ce qui surestime légèrement $\rho_b$.

**2.** L'amortissement vient de la dissipation visqueuse et surtout de l'**émission de vagues** qui emportent de l'énergie. Modèle de frottement fluide : amplitude en $e^{-t/\tau}$ avec $e^{-T/\tau}=0{,}9$, soit $\tau=\frac T{\ln(1/0{,}9)}\approx9{,}5$ s, et facteur de qualité $Q\approx\frac{\omega\tau}2=\frac\pi{\ln(1/0{,}9)}\approx30$ : amortissement faible (l'approximation $T\approx T_0$ est justifiée).
""", r"$\rho_b=\frac{\rho_egT^2}{4\pi^2e}\approx850\ \mathrm{kg\,m^{-3}}$ ; $\tau\approx9{,}5$ s, $Q\approx30$.")

c("p-meca-ccmp13",
r"Pour une orbite circulaire, la gravitation fournit l'accélération centripète ; à la surface, $GM_T=g_0R_T^2$.",
r"Pour désorbiter, on réduit la vitesse en un point de l'orbite circulaire : ce point devient l'apogée d'une ellipse dont le périgée est à $R_T+h$.",
r"Utilise la conservation du moment cinétique ($r_av_a=r_pv_p$) et de l'énergie entre apogée et périgée.",
r"""
**1.** $\frac{v_s^2}{R_T}=\frac{GM_T}{R_T^2}=g_0$, donc $v_s=\sqrt{g_0R_T}=\sqrt{10\times6{,}4\times10^6}=8{,}0\ \mathrm{km\,s^{-1}}$.

**2.** $v_1=\sqrt{\frac{GM_T}{5R_T}}=\frac{v_s}{\sqrt5}\approx3{,}6\ \mathrm{km\,s^{-1}}$.

**3.(a)** On freine brièvement le satellite en un point $A$ de l'orbite ($r_a=5R_T$) : il décrit une ellipse d'apogée $A$ et de périgée $P$ à $r_p=R_T+h\approx6{,}5\times10^6$ m (tangente à l'atmosphère).

**(b)** Conservation de $L$ : $r_av_2=r_pv_3$ ; conservation de l'énergie : $\frac12v_2^2-\frac{GM}{r_a}=\frac12v_3^2-\frac{GM}{r_p}$. On en tire
$$v_2=\sqrt{\frac{2GM\,r_p}{r_a(r_a+r_p)}}\approx2{,}1\ \mathrm{km\,s^{-1}}.$$
Il faut donc diminuer la vitesse d'environ $1{,}5\ \mathrm{km\,s^{-1}}$.

**(c)** $v_3=v_2\frac{r_a}{r_p}\approx10{,}2\ \mathrm{km\,s^{-1}}$ à l'entrée dans l'atmosphère : énorme énergie cinétique, dissipée en chaleur par frottement (destruction du satellite).
""", r"$v_s=8{,}0$, $v_1\approx3{,}6$, $v_2\approx2{,}1$, $v_3\approx10{,}2\ \mathrm{km\,s^{-1}}$.")

c("p-meca-ccs1",
r"Définition du barycentre : $M_S\,\overrightarrow{GS}+M_J\,\overrightarrow{GJ}=\vec0$.",
r"Pour $\omega$, écris la loi de la quantité de mouvement pour Jupiter (mouvement circulaire de rayon $GJ$ autour de $G$).",
r"Dans le référentiel tournant à $\omega$, un point est à l'équilibre si attractions + force centrifuge s'annulent : ce sont les points de Lagrange.",
r"""
Notons $d=SJ$.

**1.** $GS=\frac{M_J}{M_S+M_J}d\approx\frac{M_J}{M_S}d$ : si $M_J\ll M_S$, $G$ est pratiquement confondu avec le centre du Soleil (en réalité, $G$ est juste à l'extérieur du Soleil : $M_J/M_S\approx10^{-3}$ et $d\approx5{,}2$ ua donnent $GS\approx1{,}07R_S$).

**2.(a)** Jupiter décrit un cercle de rayon $\approx d$ : $M_J\omega^2d=\frac{GM_SM_J}{d^2}$, donc $\omega^2=\frac{GM_S}{d^3}$.

**(b)** Avec $T=\frac{2\pi}\omega$ : $\frac{T^2}{d^3}=\frac{4\pi^2}{GM_S}$, identique pour toutes les planètes : **troisième loi de Kepler**.

**(c)** Sans approximation, Jupiter tourne sur un cercle de rayon $GJ=\frac{M_S}{M_S+M_J}d$ : $M_J\omega^2\frac{M_Sd}{M_S+M_J}=\frac{GM_SM_J}{d^2}$, donc
$$\omega^2=\frac{G(M_S+M_J)}{d^3}.$$

**3.** Dans le référentiel tournant à $\omega$ autour de $G$, $M$ est à l'équilibre si $-\frac{GM_S}{SM^3}\overrightarrow{SM}-\frac{GM_J}{JM^3}\overrightarrow{JM}+\omega^2\overrightarrow{GM}=\vec0$. Il y a cinq solutions : trois sur la droite $SJ$ ($L_1,L_2,L_3$, instables) et deux formant des triangles équilatéraux avec $S$ et $J$ ($L_4,L_5$, stables car $M_J/M_S<0{,}04$ : on y trouve les astéroïdes « troyens »).
""", r"$\omega^2=\frac{G(M_S+M_J)}{d^3}$ ; équilibre aux points de Lagrange.")

c("p-meca-ccs3",
r"Applique Gauss gravitationnel à une sphère de rayon $r<R_T$ : quelle masse est contenue à l'intérieur ?",
r"$\vec g(r)=-g_0\frac r{R_T}\vec u_r$. Projette sur la direction du tunnel : avec $x$ l'abscisse depuis le milieu de $AB$, la composante vaut $-g_0\frac x{R_T}$.",
r"Mouvement harmonique de pulsation $\sqrt{g_0/R_T}$ : la durée $A\to B$ est une demi-période. Pour la rotation, regarde la composante des forces d'inertie le long du tunnel.",
r"""
**1.** Gauss gravitationnel : $4\pi r^2g(r)=4\pi G\,M_T\frac{r^3}{R_T^3}$, donc $\vec g(r)=-g_0\frac r{R_T}\vec u_r$ (avec $g_0=\frac{GM_T}{R_T^2}$) : champ proportionnel à la distance au centre.

**2.** Soit $H$ le milieu de $AB$ et $x$ l'abscisse de la voiture sur $AB$ depuis $H$. La composante de $m\vec g$ selon le tunnel vaut $-mg_0\frac x{R_T}$ (la composante perpendiculaire est compensée par la réaction). Sans frottement :
$$\ddot x+\frac{g_0}{R_T}x=0,\qquad\text{durée }A\to B:\ \tau=\pi\sqrt{\frac{R_T}{g_0}}\approx42\ \mathrm{min}.$$
**Remarquable** : cette durée est la même pour tous les tunnels rectilignes, quelle que soit leur longueur (c'est aussi la demi-période d'un satellite rasant).

**3.** Dans le référentiel terrestre :
- **(a)** tunnel parallèle à l'axe des pôles : la force centrifuge est perpendiculaire à l'axe, donc au tunnel ; la force de Coriolis ($\propto\vec\Omega\wedge\vec v$) est nulle car $\vec v\parallel\vec\Omega$. Mouvement inchangé.
- **(b)** tunnel dans un plan perpendiculaire à l'axe (équatorial) : la force centrifuge a une composante $m\Omega^2x$ le long du tunnel : $\omega'^2=\frac{g_0}{R_T}-\Omega^2$ (correction relative $\sim3\times10^{-3}$) ; la force de Coriolis est perpendiculaire au tunnel et presse la voiture contre une paroi.

**4.** Avec frottements, l'énergie mécanique diminue : la voiture n'atteint pas $B$ et finit par s'arrêter au milieu $H$ (oscillations amorties).
""", r"Oscillateur harmonique : durée $\pi\sqrt{R_T/g_0}\approx42$ min, quel que soit le tunnel.")

c("p-meca-ccs-ressort",
r"Écris la loi de la quantité de mouvement pour chaque masse : le ressort exerce des forces opposées $\pm K(x_2-x_1-l_0)$.",
r"Divise chaque équation par sa masse et soustrais : tu fais apparaître $\frac1{m_1}+\frac1{m_2}=\frac1\mu$.",
r"Si le centre de masse est immobile, $E_c=\frac12\mu\dot X^2$. Une molécule diatomique polaire qui vibre rayonne à la fréquence de vibration.",
r"""
**1.** $m_1\ddot x_1=K(x_2-x_1-l_0)$ et $m_2\ddot x_2=-K(x_2-x_1-l_0)$. En divisant et en soustrayant :
$$\ddot X=-K\Big(\frac1{m_1}+\frac1{m_2}\Big)(X-l_0)\ \Rightarrow\ \mu\ddot X=-K(X-l_0),\quad\mu=\frac{m_1m_2}{m_1+m_2},\quad\omega_0=\sqrt{\frac K\mu}.$$
(Et $m_1\ddot x_1+m_2\ddot x_2=0$ : le centre de masse est en mouvement rectiligne uniforme.)

**2.(a)** Dans le référentiel du centre de masse : $\dot x_1=-\frac{m_2}{m_1+m_2}\dot X$, $\dot x_2=\frac{m_1}{m_1+m_2}\dot X$, donc
$$E_p=\frac12K(X-l_0)^2,\qquad E_c=\frac12m_1\dot x_1^2+\frac12m_2\dot x_2^2=\frac12\mu\dot X^2,\qquad E_m=E_c+E_p=\mathrm{cte}.$$
Le problème à deux corps se ramène à une particule fictive de masse $\mu$.

**(b)** $X-l_0=A\cos\omega_0t$ : si les deux masses portent des charges opposées (molécule polaire), le moment dipolaire oscille à $\omega_0$ et rayonne une onde électromagnétique de fréquence $f_0=\frac{\omega_0}{2\pi}$ (typiquement **infrarouge**, $10^{13}$–$10^{14}$ Hz : spectroscopie IR des liaisons). Le milieu peut aussi transmettre une onde acoustique à cette fréquence.
""", r"$\mu\ddot X=-K(X-l_0)$, $\mu=\frac{m_1m_2}{m_1+m_2}$ ; $E_m=\frac12\mu\dot X^2+\frac12K(X-l_0)^2$.")

# ---------- Optique ----------
c("p-opt-2",
r"Avec la relation de conjugaison, la distance objet-image vaut $D=\frac{d^2}{d-f'}$ : étudie cette fonction de $d$.",
r"Une image réelle sur la plaque impose $D\ge4f'$ ; la contrainte $d\le D/2$ correspond à $|\gamma|\le1$.",
r"Pour doubler le grandissement, $L_1$ doit avoir un grandissement $\gamma_1=2$ sur l'objet virtuel $A_1$ formé par $L$ : résous $\frac1{\overline{OA'}}-\frac1{\overline{OA}}=\frac1{f_1'}$ avec $\overline{OA'}=2\overline{OA}$.",
r"""
**1.** Avec $p=\overline{OA}<0$ et $p'=\overline{OA'}=d>0$ : $\frac1d-\frac1p=\frac1{f'}$, et $D=d-p$. On obtient $D=\frac{d^2}{d-f'}$ (pour $d>f'$), minimale pour $d=2f'$, où $D=4f'$. Une image réelle exige donc $D\ge4f'$.

La condition $d\in[0,\frac D2]$ équivaut à $p'\le|p|$, soit $|\gamma|\le1$. Comme $d=\frac D2$ pour $D=4f'$ et que $d$ est la plus petite racine de $d^2-Dd+Df'=0$, on obtient :
$$D\ge4f',\qquad f'<d\le2f'.$$

**2.** $L$ donne de $AB$ une image intermédiaire $A_1B_1$ dans le plan de l'ancienne plaque. On intercale $L_1$ avant ce plan : $A_1$ est un **objet virtuel** pour $L_1$. On veut $\gamma_1=\frac{\overline{O_1A'}}{\overline{O_1A_1}}=2$. La conjugaison donne
$$\frac1{2x}-\frac1x=\frac1{f_1'}\ \Rightarrow\ x=\overline{O_1A_1}=-\frac{f_1'}2=3\ \mathrm{cm}.$$
Il faut placer $L_1$ **3 cm avant** l'ancienne position de la plaque ; l'image finale est à $\overline{O_1A'}=6$ cm, donc la plaque est **reculée de 3 cm**. Le grandissement total est doublé (l'objectif « double focale » est équivalent à une lentille de focale $2f'$ : c'est un téléconvertisseur).
""", r"$D\ge4f'$, $f'<d\le2f'$ ; $L_1$ à 3 cm avant l'ancienne plaque, plaque reculée de 3 cm.")

c("p-opt-3",
r"Un œil sans défaut n'accommode pas pour un objet à l'infini : où doit se trouver $A_1B_1$ par rapport à $L_2$ ?",
r"$A_1$ doit être au foyer objet $F_2$ de l'oculaire. Calcule $\overline{O_1A_1}$ par la conjugaison de Descartes.",
r"$\alpha'=\frac{|A_1B_1|}{f_2'}=\frac{|\gamma_1|AB}{f_2'}$ ; le grossissement est $G=\frac{\alpha'}{\alpha_{\mathrm{ref}}}$ avec $\alpha_{\mathrm{ref}}=\frac{AB}{d_m}$.",
r"""
**1.** L'image finale doit être à l'infini, donc $A_1$ (image par l'objectif) au **foyer objet de l'oculaire** : $A_1=F_2$.

**2.** Rayon issu de $B$ parallèle à l'axe : il passe par $F_1'$, puis, $B_1$ étant dans le plan focal de $L_2$, tous les rayons issus de $B_1$ émergent parallèles à $(O_2B_1)$. Le rayon passant par $O_1$ n'est pas dévié jusqu'à $B_1$.

**3.** $\frac1{\overline{O_1A_1}}=\frac1{f_1'}+\frac1{\overline{O_1A}}=2-\frac1{0{,}51}\Rightarrow\overline{O_1A_1}=25{,}5$ cm, et
$$\gamma_1=\frac{\overline{O_1A_1}}{\overline{O_1A}}=\frac{f_1'}{f_1'+\overline{O_1A}}=-50.$$

**4.** $\overline{O_1O_2}=\overline{O_1A_1}+\overline{A_1O_2}=25{,}5+2=27{,}5$ cm.

**5.** $\alpha'=\frac{|\overline{A_1B_1}|}{f_2'}=\frac{|\gamma_1|AB}{f_2'}=\frac{50\times0{,}01}{2}=0{,}25$ rad.

**6.** $\alpha_{\mathrm{ref}}=\frac{AB}{d_m}=\frac{0{,}01}{25}=4\times10^{-4}$ rad, donc
$$G=\frac{\alpha'}{\alpha_{\mathrm{ref}}}=|\gamma_1|\frac{d_m}{f_2'}=50\times12{,}5=625.$$
(Produit du grandissement de l'objectif et du grossissement commercial de l'oculaire.)
""", r"$\gamma_1=-50$, $O_1O_2=27{,}5$ cm, $\alpha'=0{,}25$ rad, $G=625$.")

c("p-opt-4",
r"Dans le triangle $C$–$M$–projection, Pythagore donne $R^2=(R-\varepsilon)^2+x^2$ : néglige $\varepsilon^2$.",
r"La différence de marche vaut l'aller-retour dans la lame d'air plus le déphasage de réflexion : $\delta=2\varepsilon+\frac{\lambda_0}2$.",
r"Franges brillantes : $\delta=p\lambda_0$ ; sombres : $\delta=(p+\frac12)\lambda_0$. Exprime le rayon $x$ correspondant.",
r"""
**1.** $R^2=(R-\varepsilon)^2+x^2$ donne $2R\varepsilon=x^2+\varepsilon^2\approx x^2$, d'où $\varepsilon\simeq\frac{x^2}{2R}$ (pour $x\ll R$).

**2.** Les deux rayons diffèrent d'un aller-retour dans la lame d'air (incidence quasi normale, indice 1) et de la réflexion sur le miroir (déphasage $\pi$) :
$$\delta=2\varepsilon+\frac{\lambda_0}2=\frac{x^2}R+\frac{\lambda_0}2.$$

**3.** $\delta$ ne dépend que de $x$ : franges **circulaires** centrées en $O$ (franges d'égale épaisseur). Au centre, $\delta=\frac{\lambda_0}2$ : **centre sombre**.
- Sombres : $\delta=(m+\frac12)\lambda_0\iff x^2=mR\lambda_0$. En comptant le centre comme première frange sombre, la $n$-ième a pour rayon $x_n=\sqrt{(n-1)\lambda_0R}$.
- Brillantes : $\delta=m\lambda_0\iff x^2=(m-\frac12)R\lambda_0$ ; la $n$-ième ($m=n\ge1$) : $x_n=\sqrt{\big(n-\frac12\big)\lambda_0R}$.

Les anneaux se resserrent ($x_n\propto\sqrt n$).

**4.** En lumière blanche : centre noir (sombre pour toutes les longueurs d'onde), entouré de quelques anneaux irisés (teintes de Newton), puis blanc d'ordre supérieur car les systèmes de franges des différentes couleurs se brouillent.
""", r"$\delta=\frac{x^2}R+\frac{\lambda_0}2$ ; anneaux sombres $x=\sqrt{m\lambda_0R}$, brillants $x=\sqrt{(m-\frac12)\lambda_0R}$.")

c("p-opt-5",
r"La lumière est observée dans une direction différente de l'incidence grâce à la diffraction par chaque fente.",
r"Différence de marche entre deux fentes consécutives : $\delta=a(\sin\alpha-\sin i)$ ; les pics correspondent aux interférences constructives de toutes les ondes.",
r"Pour le minimum de déviation, dérive $D_p(i)=i-\alpha_p(i)$ en utilisant $\cos\alpha\,d\alpha=\cos i\,di$.",
r"""
**1.** La **diffraction** par chaque fente (de largeur comparable à $\lambda_0$) envoie de la lumière dans toutes les directions ; les ondes issues des $N$ fentes interfèrent.

**2.** $\delta=a(\sin\alpha-\sin i)$ et $\varphi=\frac{2\pi}{\lambda_0}a(\sin\alpha-\sin i)$.

**3.** Somme de $N$ ondes déphasées de $\varphi$ : $I=I_0\frac{\sin^2(N\varphi/2)}{\sin^2(\varphi/2)}$, avec des pics fins d'intensité $N^2I_0$ quand $\varphi\in2\pi\mathbb Z$. **Formule des réseaux** :
$$\sin\alpha_p-\sin i=p\,\frac{\lambda_0}a,\qquad p\in\mathbb Z.$$

**4.** $i=0$ : $|\sin\alpha_p|=|p|\frac{\lambda_0}a=|p|\times0{,}207\le1$, donc $|p|\le4$ : **9 pics** ($p=-4,\dots,4$).

**5.** À $p$ fixé, $\cos\alpha_p\,d\alpha_p=\cos i\,di$, donc $\frac{dD_p}{di}=1-\frac{\cos i}{\cos\alpha_p}=0\iff\alpha_p=-i$ (la solution $\alpha_p=i$ correspond à $p=0$). Alors $-2\sin i=p\frac{\lambda_0}a$ et $D_p^*=2i$, d'où
$$\lambda_0=\frac{2a}{|p|}\sin\frac{|D_p^*|}2.$$

**6.** Chaque radiation donne son propre pic (pour $p\ne0$) à un angle différent : le réseau **disperse** la lumière (spectroscope). Le minimum de déviation se repère précisément (la déviation y est stationnaire) et la formule ne fait intervenir que $a$ (connu) et un angle mesuré au goniomètre (à la minute d'arc près), d'où une bonne précision sur $\lambda_0$.
""", r"$\sin\alpha_p-\sin i=p\lambda_0/a$ ; 9 pics ; $\lambda_0=\frac{2a}{|p|}\sin\frac{D_p^*}2$.")

c("p-opt-6",
r"En lame d'air éclairée en incidence normale, $\delta=2e$ au centre.",
r"Une frange brillante défile chaque fois que $\delta$ varie de $\lambda_0$.",
r"La lame de verre ajoute $2(n-1)h$ à la différence de marche (aller-retour) : combien de franges faut-il faire défiler pour compenser ?",
r"""
**1.** $e=0$ : $\delta=0$ en tout point, l'éclairement est uniforme et maximal : c'est le **contact optique** (« teinte plate »).

**2.** Au foyer, $\delta=2e$. Une variation $\Delta e=2\ \mu$m change $\delta$ de $4\ \mu$m : nombre de franges $N=\frac{2\Delta e}{\lambda_0}=\frac{4\times10^{-6}}{475\times10^{-9}}\approx8{,}4$, soit **8 franges brillantes**.

**3.** La lame est traversée deux fois : le chemin optique sur ce bras augmente de $2(n-1)h$. À partir du contact optique :
$$\delta=2(n-1)h=2\times0{,}50\times1{,}0\ \mathrm{mm}=1{,}0\ \mathrm{mm}.$$
Pour revenir à $\delta=0$, il faut chariotter le miroir de $\Delta e=(n-1)h=0{,}50$ mm, ce qui fait défiler $N=\frac{\delta}{\lambda_0}\approx2{,}1\times10^3$ franges. (En comptant les franges, on mesure $(n-1)h$ ; avec une source quasi monochromatique de cohérence limitée, il faut une lumière de grande longueur de cohérence.)
""", r"Contact optique ; 8 franges ; $\delta=2(n-1)h=1$ mm, environ 2100 franges.")

c("p-opt-7",
r"Pour la lentille, relation de conjugaison avec $\overline{OA}=-D$ et $\overline{OA'}=D'$ ; le grandissement transversal est $\frac{D'}{-D}$.",
r"Dans le coin d'air d'angle $\alpha$, l'épaisseur au point d'abscisse $x$ depuis l'arête vaut $\varepsilon=\alpha x$, et $\delta=2\varepsilon$.",
r"Remplace $x$ par $x'\frac{D-f'}{-f'}$, puis cherche les $x'$ tels que $\delta=p\lambda_0$.",
r"""
**1.** Conjugaison : $\frac1{D'}+\frac1D=\frac1{f'}$, soit $D'=\frac{Df'}{D-f'}$. Grandissement : $\gamma=\frac{x'}x=-\frac{D'}D=-\frac{f'}{D-f'}$ (ici $\gamma=-\frac{25}2=-12{,}5$).

**2.** $\varepsilon=x\tan\alpha\simeq\alpha x$ (franges localisées sur le coin).

**3.** $\varepsilon=-\alpha x'\frac{D-f'}{f'}$.

**4.** Incidence quasi normale : $\delta=2\varepsilon=-\frac{2\alpha(D-f')}{f'}x'$.

**5.** $I=2I_0\big(1+\cos\frac{2\pi\delta}{\lambda_0}\big)$. Franges rectilignes parallèles à l'arête, brillantes pour $x'_p=-\frac{p\lambda_0f'}{2\alpha(D-f')}$, d'interfrange
$$i=\frac{\lambda_0f'}{2\alpha(D-f')}=|\gamma|\,\frac{\lambda_0}{2\alpha}.$$

**6.** $\alpha=0{,}5'=1{,}45\times10^{-4}$ rad : interfrange sur le coin $\frac{\lambda_0}{2\alpha}\approx2{,}1$ mm, sur l'écran $i\approx12{,}5\times2{,}1\approx26$ mm. On observe des **franges rectilignes, équidistantes d'environ 2,6 cm**, parallèles à l'arête du coin, frange centrale ($\varepsilon=0$) brillante au centre de l'écran.
""", r"$\gamma=-12{,}5$ ; $\delta=2\alpha x$ ; interfrange $\approx2{,}6$ cm sur l'écran.")

c("p-opt-8",
r"Chaque bande $d\sigma$ donne un éclairement $dI=2\mathcal D(\sigma)\big[1+\cos(2\pi\sigma\delta)\big]d\sigma$ ; les bandes sont incohérentes entre elles : les éclairements s'additionnent.",
r"Avec $\delta=2e=2V_0t$ et les intégrales données, identifie l'enveloppe gaussienne $e^{-\pi^2b^2\delta^2}$.",
r"$T_0$ est la période des franges : $2\sigma_0V_0T_0=1$. $\tau$ vient de $\pi b\,2V_0\tau=1$. Le compteur de franges donne $\lambda_0$, la largeur de l'enveloppe donne $b$.",
r"""
**1.** Les composantes spectrales sont incohérentes entre elles :
$$I(t)=\int_0^\infty2\mathcal D(\sigma)\big[1+\cos(2\pi\sigma\delta)\big]d\sigma,\qquad\delta=2e=2V_0t.$$

**2.** Avec les intégrales données ($b\ll\sigma_0$, on peut intégrer sur $\mathbb R$) :
$$I(t)=2\mathcal D_0b\sqrt\pi\big[1+e^{-\pi^2b^2\delta^2}\cos(2\pi\sigma_0\delta)\big]=I_0\Big[1+e^{-(t/\tau)^2}\cos\frac{2\pi t}{T_0}\Big],$$
avec $I_0=2\sqrt\pi\,\mathcal D_0b$, $\tau=\frac1{2\pi bV_0}$, $T_0=\frac1{2\sigma_0V_0}=\frac{\lambda_0}{2V_0}$. On a bien $T_0\ll\tau$ car $b\ll\sigma_0$.

**3.** $V_0=\frac{0{,}500\ \mathrm{mm}}{15\ \mathrm{min}}\approx5{,}6\times10^{-7}\ \mathrm{m\,s^{-1}}$. Si $N=480$ franges défilent pendant la durée $\Delta t$ lue sur l'interférogramme, $\Delta\delta=2V_0\Delta t=N\lambda_0$, d'où $\lambda_0=\frac{2V_0\Delta t}N$ et $\sigma_0=\frac1{\lambda_0}$. La demi-largeur temporelle $\tau$ de l'enveloppe (lue sur le graphe) donne $b=\frac1{2\pi V_0\tau}$. On vérifie alors $b\ll\sigma_0$, i.e. $\tau\gg T_0$ (beaucoup de franges sous l'enveloppe).

*Interprétation* : l'interférogramme est la transformée de Fourier du spectre ; sa largeur est inversement proportionnelle à la largeur spectrale (longueur de cohérence $\ell_c\sim\frac1b$). C'est le principe de la spectroscopie par transformée de Fourier.
""", r"$I=I_0[1+e^{-(t/\tau)^2}\cos(2\pi t/T_0)]$, $\tau=\frac1{2\pi bV_0}$, $T_0=\frac{\lambda_0}{2V_0}$.")

c("p-opt-ccmp1",
r"Calcule $\delta=SS_2M-SS_1M$ par développement limité pour $x\ll D$ et $a\ll D$.",
r"$\delta=\frac{ax}D$ : franges rectilignes perpendiculaires à $S_1S_2$, interfrange $i=\frac{\lambda D}a$.",
r"Si la source se déplace de $y_s$ parallèlement à $S_1S_2$ (à la distance $d$ des trous), $\delta$ devient $\frac{ax}D+\frac{ay_s}d$. Brouillage quand deux points de la source donnent des systèmes décalés d'une demi-interfrange.",
r"""
**1.** Avec $S$ sur l'axe et $M$ d'abscisse $x$ sur l'écran à la distance $D$ (avec $a,x\ll D$) : $S_2M-S_1M\approx\frac{ax}D$, donc
$$\delta=\frac{ax}D,\qquad p=\frac\delta\lambda,\qquad I=2I_0\Big(1+\cos\frac{2\pi ax}{\lambda D}\Big).$$
Franges **rectilignes**, perpendiculaires à $S_1S_2$, équidistantes d'interfrange $i=\frac{\lambda D}a$ ; frange centrale brillante.

**2.** Si $S$ est déplacée de $y_s$ parallèlement à $S_1S_2$ (à la distance $d$ du plan des trous), $\delta=\frac{ax}D+\frac{ay_s}d$ : le système de franges est **translaté** de $-\frac Dd y_s$ (en sens opposé). Un déplacement perpendiculaire à $S_1S_2$ (parallèle aux franges) ne change rien.

**3.** Une source large de $\ell$ (selon $S_1S_2$) est une somme de sources ponctuelles incohérentes. Les franges disparaissent quand les systèmes extrêmes sont décalés d'une interfrange : $\frac{a\ell}d\approx\lambda$. Le calcul exact donne un contraste $\big|\operatorname{sinc}\big(\frac{\pi a\ell}{\lambda d}\big)\big|$, nul pour la première fois en $\ell=\frac{\lambda d}a$. Il faut donc
$$\ell<\frac{\lambda d}a.$$
D'où l'utilisation de sources fines (fente parallèle aux franges). C'est le principe de la mesure du diamètre apparent des étoiles (interféromètre stellaire).
""", r"$\delta=\frac{ax}D$, $i=\frac{\lambda D}a$ ; source de largeur $\ell<\frac{\lambda d}a$.")

# ---------- Quantique ----------
c("p-q-1",
r"Sur le cercle, l'abscisse curviligne est $s=R\theta$ : remplace $\frac{d^2}{dx^2}$ par $\frac1{R^2}\frac{d^2}{d\theta^2}$.",
r"La fonction d'onde doit être univaluée : $\psi(\theta+2\pi)=\psi(\theta)$.",
r"Les solutions de $\psi''=-k^2\psi$ sont des $e^{\pm ik\theta}$ : la périodicité impose $k$ entier.",
r"""
**1.** Particule libre ($V=0$), abscisse curviligne $s=R\theta$ :
$$-\frac{\hbar^2}{2mR^2}\frac{d^2\psi}{d\theta^2}=E\psi.$$
(C'est aussi le laplacien cylindrique à $r=R$ fixé, sans dépendance en $z$.)

**2.** $\theta$ et $\theta+2\pi$ désignent le même point : $\psi(\theta+2\pi)=\psi(\theta)$ (et de même pour $\psi'$).

**3.** Avec $E=\frac{\hbar^2k^2}{2mR^2}\ge0$ ($E<0$ donnerait des exponentielles réelles non périodiques), $\psi=Ae^{ik\theta}+Be^{-ik\theta}$ ; la périodicité impose $k=n\in\mathbb Z$. États stationnaires normalisés :
$$\psi_n(\theta)=\frac1{\sqrt{2\pi R}}e^{in\theta},\qquad E_n=\frac{n^2\hbar^2}{2mR^2},\quad n\in\mathbb Z.$$
Niveaux quantifiés, deux fois dégénérés pour $n\ne0$ (sens de rotation) ; le moment cinétique $L_z=n\hbar$ est quantifié (modèle de Bohr ; molécules cycliques comme le benzène).
""", r"$\psi_n=\frac{e^{in\theta}}{\sqrt{2\pi R}}$, $E_n=\frac{n^2\hbar^2}{2mR^2}$.")

c("p-q-2",
r"Calcule $\varphi''$ pour $\varphi=Cxe^{-kx}$ et reporte dans l'équation de Schrödinger.",
r"En identifiant les termes en $x$ et les termes constants, tu obtiens deux équations : $k=\frac{m\lambda}{\hbar^2}$ et $E=-\frac{\hbar^2k^2}{2m}$.",
r"Normalise avec $\int_0^\infty x^2e^{-2kx}dx=\frac{2}{(2k)^3}$ et calcule $\langle x\rangle=\int_0^\infty x|\varphi|^2dx$.",
r"""
**1.** Pour $x>0$ : $-\frac{\hbar^2}{2m}\varphi''-\frac\lambda x\varphi=E\varphi$, avec $\varphi(0)=0$ (paroi infinie).

**2.** $\varphi''=C(k^2x-2k)e^{-kx}$. En reportant et en divisant par $Ce^{-kx}$ :
$$-\frac{\hbar^2}{2m}(k^2x-2k)-\lambda=Ex.$$
Identification : $E=-\frac{\hbar^2k^2}{2m}$ et $\frac{\hbar^2k}m=\lambda$, d'où
$$k=\frac{m\lambda}{\hbar^2},\qquad E=-\frac{m\lambda^2}{2\hbar^2}.$$

**3.** $V\to-\infty$ en $0^+$ et $V\to0^-$ à l'infini ; $E<0$ : état **lié**, la particule est classiquement confinée dans $x<\frac\lambda{|E|}$. (Analogue de l'état fondamental de l'atome d'hydrogène, avec $\lambda=\frac{e^2}{4\pi\varepsilon_0}$ : $E=-13{,}6$ eV.)

**4.** $C^2\int_0^\infty x^2e^{-2kx}dx=C^2\frac{2}{(2k)^3}=1$, d'où $C=2k^{3/2}$.

**5.** $\langle x\rangle=C^2\int_0^\infty x^3e^{-2kx}dx=4k^3\cdot\frac{6}{(2k)^4}=\frac3{2k}=\frac{3\hbar^2}{2m\lambda}$.
""", r"$k=\frac{m\lambda}{\hbar^2}$, $E=-\frac{m\lambda^2}{2\hbar^2}$, $C=2k^{3/2}$, $\langle x\rangle=\frac3{2k}$.")

c("p-q-3",
r"$|\psi|^2dx$ est une probabilité (sans dimension) : quelle est la dimension de $A$ ? L'argument d'une exponentielle est sans dimension.",
r"Normalise $|A|^2\int e^{-m\omega_0x^2/\hbar}dx=1$. L'énergie se lit sur la dépendance temporelle $e^{-iEt/\hbar}$.",
r"Pour $V(x)$, reporte $\psi$ dans l'équation de Schrödinger stationnaire et isole $V$.",
r"""
**1.** $|\psi|^2$ est une densité de probabilité linéique : $[A]=\mathrm m^{-1/2}$. $\omega_0t$ est sans dimension : $[\omega_0]=\mathrm s^{-1}$ (et $\frac{m\omega_0x^2}\hbar$ est bien sans dimension).

**2.** $|A|^2\sqrt{\frac{\pi\hbar}{m\omega_0}}=1$, donc $A=\Big(\frac{m\omega_0}{\pi\hbar}\Big)^{1/4}e^{i\varphi}$ ($\varphi$ phase arbitraire).

**3.** $\psi=\varphi(x)e^{-iEt/\hbar}$ avec $\frac E\hbar=\frac{\omega_0}2$ : $E=\frac12\hbar\omega_0$.

**4.** $\varphi=Ae^{-\alpha x^2/2}$ avec $\alpha=\frac{m\omega_0}\hbar$ : $\varphi''=(\alpha^2x^2-\alpha)\varphi$. Dans $-\frac{\hbar^2}{2m}\varphi''+V\varphi=E\varphi$ :
$$V(x)=E+\frac{\hbar^2}{2m}(\alpha^2x^2-\alpha)=\frac12m\omega_0^2x^2.$$
C'est l'**oscillateur harmonique**, dont $\psi$ est l'état fondamental.

**5.** $|\psi|^2$ est paire : $\langle x\rangle=0$.

**6.** $\langle x^2\rangle=|A|^2\sqrt{\frac\pi{4\alpha^3}}=\frac1{2\alpha}=\frac\hbar{2m\omega_0}$, donc $\big\langle\frac12m\omega_0^2x^2\big\rangle=\frac14\hbar\omega_0=\frac E2$ : énergie équitablement répartie entre potentielle et cinétique (théorème du viriel).
""", r"$A=(\frac{m\omega_0}{\pi\hbar})^{1/4}$, $E=\frac{\hbar\omega_0}2$, $V=\frac12m\omega_0^2x^2$, $\langle V\rangle=\frac{\hbar\omega_0}4$.")

c("p-q-4",
r"Dans chaque zone, résous $\varphi''=-\frac{2m(E-V)}{\hbar^2}\varphi$ : oscillant si $E>V$, exponentiel si $E<V$.",
r"$\varphi$ doit rester bornée : le terme $e^{x/\delta}$ est exclu. Continuité de $\varphi$ en $0$ (paroi infinie) et de $\varphi$ et $\varphi'$ en $a$.",
r"Tu obtiens $\tan(ka)=-k\delta$ avec $k^2+\delta^{-2}=k_0^2$ ; déduis $\sin^2(ka)=\frac{k^2}{k_0^2}$ et résous graphiquement $|\sin X|=\frac X{k_0a}$.",
r"""
**1.** $V=+\infty$ pour $x<0$ : $\varphi=0$. Sur $[0,a]$, $E>V=0$ : solutions oscillantes $A_1e^{ikx}+B_1e^{-ikx}$. Pour $x>a$, $E<V_0$ : $\varphi''=\frac1{\delta^2}\varphi$, solutions $A_2e^{-x/\delta}+B_2e^{x/\delta}$.

**2.** $\varphi$ doit être normalisable : $B_2=0$.

**3.** Continuité de $\varphi$ en $0$ : $A_1+B_1=0$, donc $\varphi=2iA_1\sin kx$ sur $[0,a]$. En $a$, continuité de $\varphi$ et $\varphi'$ :
$$2iA_1\sin(ka)=A_2e^{-a/\delta},\qquad2iA_1k\cos(ka)=-\frac{A_2}\delta e^{-a/\delta}.$$

**4.** Le quotient donne $\tan(ka)=-k\delta$ (donc $\tan(ka)<0$). Comme $k^2+\frac1{\delta^2}=k_0^2$ : $\sin^2(ka)=\frac{\tan^2}{1+\tan^2}=\frac{k^2\delta^2}{1+k^2\delta^2}=\frac{k^2}{k_0^2}$, soit
$$|\sin(ka)|=\frac k{k_0},\qquad\tan(ka)<0.$$

**5.** Avec $X=ka$ : intersection de $|\sin X|$ et de la droite $\frac X{k_0a}$, sur les arches où $\tan X<0$ ($X\in]\frac\pi2,\pi[$ modulo $\pi$).
- Si $k_0a<\frac\pi2$ : la droite passe au-dessus de $|\sin X|$ dès $X=\frac\pi2$ : **aucun état lié**.
- Si $k_0a>\frac\pi2$ : nombre **fini** de solutions (à peu près $\frac{k_0a}\pi+\frac12$) : énergies quantifiées.
- Si $k_0a\gg\frac\pi2$ : les solutions tendent vers $X=n\pi$, soit $E_n=\frac{n^2\pi^2\hbar^2}{2ma^2}$ : on retrouve le **puits infini**.

Contrairement au puits fini symétrique, un puits trop étroit ou peu profond n'admet ici aucun état lié.
""", r"$\tan(ka)=-k\delta$, $|\sin ka|=k/k_0$ ; état lié ssi $k_0a>\pi/2$.")

c("p-stat-1",
r"Dipôles indépendants, discernables, à l'équilibre avec un thermostat : statistique de Boltzmann, $p\propto e^{-\varepsilon/k_BT}$.",
r"$p_\pm=\frac{e^{\pm\beta\varepsilon_0}}{2\operatorname{ch}(\beta\varepsilon_0)}$ avec $\beta=\frac1{k_BT}$.",
r"$\langle\mu\rangle=\mu_0(p_+-p_-)=\mu_0\operatorname{th}\frac{\mu_0B_0}{k_BT}$ ; développe à haute température.",
r"""
**1.** Hypothèses : particules indépendantes (interactions négligées), discernables (localisées), système en équilibre avec un thermostat à $T$ : la probabilité d'un état d'énergie $\varepsilon$ est proportionnelle à $e^{-\varepsilon/k_BT}$.

**2.** États $\pm$ d'énergies $\mp\varepsilon_0$. Avec $\beta=\frac1{k_BT}$ :
$$p_\pm=\frac{e^{\pm\beta\varepsilon_0}}{e^{\beta\varepsilon_0}+e^{-\beta\varepsilon_0}}=\frac{e^{\pm\beta\varepsilon_0}}{2\operatorname{ch}(\beta\varepsilon_0)}.$$

**3.** $\langle\varepsilon\rangle=-\varepsilon_0p_++\varepsilon_0p_-=-\varepsilon_0\operatorname{th}(\beta\varepsilon_0)$.

**4.** $\langle\mu_k\rangle=\mu_0(p_+-p_-)\vec u=\mu_0\operatorname{th}\Big(\frac{\mu_0B_0}{k_BT}\Big)\vec u$.

**5.** Pour $N$ dipôles (aimantation par unité de volume avec $n$ dipôles par m³) : $\langle\vec{\mathcal M}\rangle=n\mu_0\operatorname{th}\big(\frac{\mu_0B_0}{k_BT}\big)\vec u$.

**6.** Haute température ($\mu_0B_0\ll k_BT$) : $\operatorname{th}u\approx u$, $\langle\vec{\mathcal M}\rangle\approx\frac{n\mu_0^2}{k_BT}\vec B$ : **loi de Curie** avec $C=\frac{n\mu_0^2}{k_B}$. À basse température ou champ fort : saturation $\mathcal M\to n\mu_0$ (tous les dipôles alignés), la loi de Curie n'est plus valable.

*Modèle continu (partie B)* : on obtient la fonction de Langevin $L(u)=\coth u-\frac1u$ et $C=\frac{n\mu_0^2}{3k_B}$ (facteur $\frac13$ de moyenne angulaire).
""", r"$\langle\mu\rangle=\mu_0\operatorname{th}\frac{\mu_0B}{k_BT}$ ; Curie à haute $T$ : $C=\frac{n\mu_0^2}{k_B}$.")

c("p-stat-3",
r"Chaque maillon a 2 états : $2^N$ états au total. Avec $k$ maillons courts, $\mathcal L=N\ell+(N-2k)a$ et $\Omega(k)=\binom Nk$.",
r"Avec Stirling, $S(k)=k_B[N\ln N-k\ln k-(N-k)\ln(N-k)]$, maximale en $k=N/2$.",
r"$f=-T\frac{dS}{d\mathcal L}=-T\frac{dS/dk}{d\mathcal L/dk}$ ; exprime $k$ en fonction de $x=\frac{\mathcal L-\mathcal L_0}{Na}$.",
r"""
**1.** $2^N$ états microscopiques.

**2.(a)** $\mathcal L=k(\ell-a)+(N-k)(\ell+a)=N\ell+(N-2k)a$.

**(b)** $\Omega(k)=\binom Nk=\frac{N!}{k!(N-k)!}$.

**(c)** Stirling : $S(k)=k_B\big[N\ln N-k\ln k-(N-k)\ln(N-k)\big]$, et $\frac{dS}{dk}=k_B\ln\frac{N-k}k=0$ pour $k=\frac N2$ : longueur à vide $\mathcal L_0=N\ell$.

**3.** $d\mathcal L=-2a\,dk$, donc
$$f=-T\frac{dS}{d\mathcal L}=\frac{k_BT}{2a}\ln\frac{N-k}k.$$

**4.** Avec $x=\frac{\mathcal L-\mathcal L_0}{Na}=\frac{N-2k}N$ : $\frac{N-k}k=\frac{1+x}{1-x}$, donc $f=\frac{k_BT}a\operatorname{argth}x$, soit
$$\mathcal L=\mathcal L_0+Na\operatorname{th}\Big(\frac{af}{k_BT}\Big).$$

**5.** Pour une force $f$ donnée, posons $T_c=\frac{af}{k_B}$.
- $T\gg T_c$ : $\operatorname{th}u\approx u$, donc $f=\kappa(\mathcal L-\mathcal L_0)$ avec $\kappa=\frac{k_BT}{Na^2}$ : **loi de Hooke**, de raideur proportionnelle à $T$ (élasticité **entropique**, comme le caoutchouc qui se contracte quand on le chauffe).
- $T\ll T_c$ : $\operatorname{th}\to1$, $\mathcal L=N(\ell+a)$ : fibre totalement étirée, insensible à de petites variations de force : **figée**.
""", r"$f=\frac{k_BT}{2a}\ln\frac{N-k}k$ ; $\mathcal L=\mathcal L_0+Na\operatorname{th}\frac{af}{k_BT}$ ; Hooke avec $\kappa=\frac{k_BT}{Na^2}$.")

# ---------- Thermodynamique ----------
c("p-th-1",
r"La transformation est adiabatique et monobare (pression extérieure $P_1$) : applique le premier principe avec $W=-P_1(V_f-V_0)$.",
r"$\Delta U=nc_v(T_f-T_0)$ avec $c_v=\frac32R$ et $P_f=P_1$ : tu obtiens une équation en $T_f$.",
r"Pour l'entropie d'un gaz parfait, $\Delta S=nc_p\ln\frac{T_f}{T_0}-nR\ln\frac{P_f}{P_0}$. Compare à l'entropie échangée.",
r"""
**1.** $V_0=\frac{nRT_0}{P_0}$.

**2.** À l'équilibre mécanique final, $P_f=P_1=\frac{P_0}2$. Adiabatique, travail contre la pression extérieure constante :
$$\frac32nR(T_f-T_0)=-P_1(V_f-V_0)=-nRT_f+\frac{P_0}2\cdot\frac{nRT_0}{P_0}.$$
D'où $\frac52T_f=2T_0$ :
$$T_f=\frac45T_0,\qquad P_f=\frac{P_0}2,\qquad V_f=\frac{nRT_f}{P_f}=\frac85V_0.$$
(Une détente adiabatique réversible jusqu'à $\frac{P_0}2$ donnerait $T=2^{-2/5}T_0\approx0{,}76T_0<0{,}80T_0$ : la détente brutale refroidit moins.)

**3.** $\Delta S=nc_p\ln\frac{T_f}{T_0}-nR\ln\frac{P_f}{P_0}=nR\Big(\frac52\ln\frac45+\ln2\Big)\approx0{,}135\,nR>0.$

La transformation est adiabatique : $S_{\mathrm{éch}}=0$, donc $S_{\mathrm{créée}}=\Delta S>0$ : **irréversible**. La cause : l'hétérogénéité de pression lors de la libération brutale du piston.
""", r"$T_f=\frac45T_0$, $V_f=\frac85V_0$, $\Delta S=nR(\frac52\ln\frac45+\ln2)\approx0{,}135\,nR>0$.")

c("p-th-4",
r"Pour les étapes adiabatiques réversibles d'un gaz parfait, utilise la loi de Laplace $TP^{\frac{1-\gamma}\gamma}=\mathrm{cte}$.",
r"Le travail de la turbine compense celui du compresseur : $T_C-T_D=T_B-T_A$. Dans la tuyère, premier principe industriel : $\frac12V_E^2=c_p(T_D-T_E)$.",
r"Rendement $=\frac{\text{puissance cinétique}}{\text{puissance thermique}}=\frac{T_D-T_E}{T_C-T_B}$ ; multiplie par le débit pour les puissances.",
r"""
$c_p=\frac{\gamma R}{(\gamma-1)M}\approx1003\ \mathrm{J\,K^{-1}\,kg^{-1}}$ ; $\frac{\gamma-1}\gamma=0{,}286$.

**1.**
- $A\to B$ (Laplace) : $T_B=T_A\,5^{0{,}286}\approx459$ K, $P_B=5{,}0\times10^5$ Pa.
- $B\to C$ isobare : $P_C=5{,}0\times10^5$ Pa, $T_C=1500$ K.
- $C\to D$ : le travail fourni par la turbine égale celui reçu par le compresseur : $c_p(T_C-T_D)=c_p(T_B-T_A)$, d'où $T_D\approx1331$ K, puis (Laplace) $P_D=P_C\big(\frac{T_D}{T_C}\big)^{3{,}5}\approx3{,}3\times10^5$ Pa.
- $D\to E$ : $P_E=1{,}0\times10^5$ Pa et $T_E=T_C\,5^{-0{,}286}\approx947$ K.

**2.** Tuyère adiabatique, sans travail utile, vitesse d'entrée négligée : $\frac12V_E^2=c_p(T_D-T_E)$, d'où $V_E\approx877\ \mathrm{m\,s^{-1}}$.

**3.** $q=c_p(T_C-T_B)\approx1{,}04\times10^6\ \mathrm{J\,kg^{-1}}$. Rendement :
$$\eta=\frac{V_E^2/2}{q}=\frac{T_D-T_E}{T_C-T_B}=1-5^{-0{,}286}\approx0{,}37$$
(rendement du cycle de Brayton, fonction du seul rapport de compression). Puissance cinétique $D_m\frac{V_E^2}2\approx15$ MW ; puissance thermique $D_mq\approx42$ MW.
""", r"$T_B\approx459$ K, $T_D\approx1331$ K, $T_E\approx947$ K ; $V_E\approx877$ m/s ; $\eta\approx0{,}37$.")

c("p-th-spe1",
r"Bilan d'énergie sur la tranche $[z,z+dz]$ : variation d'énergie interne = flux conductif net + puissance Joule − pertes latérales.",
r"Puissance Joule de la tranche : $R\,i^2$ avec $R=\frac{dz}{\gamma\pi a^2}$ ; pertes latérales : $\beta(T-T_0)2\pi a\,dz$.",
r"Intègre l'EDP sur $[0,L]$ : les termes de conduction disparaissent grâce aux extrémités calorifugées ($\partial_zT=0$).",
r"""
**1.** Pour la tranche (volume $\pi a^2dz$) pendant $dt$ :
$$\mu c\pi a^2dz\,\partial_tT=\lambda\pi a^2\big[\partial_zT(z+dz)-\partial_zT(z)\big]+\frac{i^2dz}{\gamma\pi a^2}-\beta(T-T_0)2\pi a\,dz,$$
d'où l'équation de l'énoncé :
$$\mu c\pi a^2\partial_tT=\lambda\pi a^2\partial_z^2T-2\beta\pi a(T-T_0)+\frac{i^2}{\gamma\pi a^2}.$$

**2.** $T_m$ est la température moyenne du conducteur, $\theta$ son écart à l'extérieur. En intégrant sur $[0,L]$ et en divisant par $L$ : $\int_0^L\partial_z^2T=[\partial_zT]_0^L=0$ (extrémités calorifugées). Donc
$$\mu c\pi a^2\dot\theta=-2\beta\pi a\theta+\frac{i^2}{\gamma\pi a^2}\ \Rightarrow\ \tau\dot\theta+\theta=\theta_\infty,$$
$$\tau=\frac{\mu ca}{2\beta},\qquad\theta_\infty=\frac{i^2}{2\beta\gamma\pi^2a^3}.$$

**3.** Avec $T_m(0)=T_0$ : $T_m(t)=T_0+\theta_\infty\big(1-e^{-t/\tau}\big)$.

*Commentaire* : en régime permanent, la puissance Joule $\frac{i^2L}{\gamma\pi a^2}$ égale les pertes $2\beta\pi aL\theta_\infty$ ; $\theta_\infty\propto\frac{i^2}{a^3}$ : c'est pourquoi la section des câbles est dimensionnée selon l'intensité.
""", r"$\tau=\frac{\mu ca}{2\beta}$, $\theta_\infty=\frac{i^2}{2\beta\gamma\pi^2a^3}$, $T_m=T_0+\theta_\infty(1-e^{-t/\tau})$.")

c("p-th-spe2",
r"Loi de Stefan : puissance surfacique émise par un corps noir $\sigma T^4$.",
r"La Lune reçoit, sur sa section $\pi R_L^2$, la puissance solaire $\frac{P_S}{4\pi r^2}\pi R_L^2$ (distance Soleil-Lune $\approx r$).",
r"À l'équilibre, l'hémisphère éclairé ($2\pi R_L^2$) rayonne ce qu'il absorbe (on néglige l'hémisphère nocturne).",
r"""
**1.** $P_S=4\pi R_S^2\sigma T_S^4\approx4\pi(6{,}96\times10^8)^2\times5{,}67\times10^{-8}\times5778^4\approx3{,}8\times10^{26}$ W.

**2.** Distance Soleil-Lune $\approx r$ (car $r_L\ll r$). Puissance absorbée : $\frac{P_S}{4\pi r^2}\pi R_L^2$. Puissance émise par l'hémisphère éclairé (corps noir à $T_j$, $T_n\ll T_j$) : $2\pi R_L^2\sigma T_j^4$. Équilibre :
$$\frac{R_S^2\sigma T_S^4}{r^2}\pi R_L^2=2\pi R_L^2\sigma T_j^4\ \Rightarrow\ T_j=T_S\sqrt{\frac{R_S}r}\cdot2^{-1/4}\approx331\ \mathrm K\approx58\ ^\circ\mathrm C.$$
(Valeur mesurée en plein jour au point subsolaire : environ $390$ K ; le modèle d'hémisphère homogène moyenne les régions éclairées en incidence rasante. La nuit, $T_n$ chute vers $100$ K : pas d'atmosphère ni d'océan pour redistribuer la chaleur.)
""", r"$P_S\approx3{,}8\times10^{26}$ W ; $T_j=T_S\sqrt{R_S/r}\,2^{-1/4}\approx330$ K.")

c("p-th-spe3",
r"$\mathcal D(\lambda)=\mathcal D(\omega)\big|\frac{d\omega}{d\lambda}\big|$ avec $\omega=\frac{2\pi c}\lambda$.",
r"Pour Wien, dérive $\lambda^{-5}\big(e^{hc/\lambda k_BT}-1\big)^{-1}$ ; avec $x=\frac{hc}{\lambda k_BT}$, la condition devient $e^{-x}+\frac x5-1=0$.",
r"Pour Stefan, $\mathcal P_S=\frac c4\int_0^\infty\mathcal D(\omega)d\omega$ ; pose $x=\frac{\hbar\omega}{k_BT}$.",
r"""
**1.** $\Big|\frac{d\omega}{d\lambda}\Big|=\frac{2\pi c}{\lambda^2}$, donc
$$\mathcal D(\lambda)=\frac{8\pi hc}{\lambda^5}\cdot\frac1{e^{hc/(\lambda k_BT)}-1}.$$

**2.** Avec $x=\frac{hc}{\lambda k_BT}$, $\mathcal D\propto\frac{x^5}{e^x-1}$ ; le maximum vérifie $5(e^x-1)=xe^x$, soit $e^{-x}+\frac x5-1=0$, d'où $x=4{,}9651$ et
$$\lambda_{\max}T=\frac{hc}{4{,}9651\,k_B}\approx2{,}90\times10^{-3}\ \mathrm{m\,K}\quad\text{(loi de Wien)}.$$
Soleil : $\lambda_{\max}\approx500$ nm ; corps humain : $\approx10\ \mu$m.

**3.** Les photons de pulsation dans $[\omega,\omega+d\omega]$ ont l'énergie volumique $du$ et l'énergie individuelle $\hbar\omega$ ; dans le volume $c\,dt\,dS$ il y en a $dN=\frac{du\,c\,dt\,dS}{\hbar\omega}$.

**4.** Modèle 1D : la moitié se dirige vers l'extérieur et traverse $dS$ pendant $dt$ : $dN_e=\frac{dN}2$.

**5.** Avec le facteur $\frac12$ du passage au 3D : $d\mathcal E=\frac{dN}4\hbar\omega=\frac{c}4du\,dt\,dS$.

**6–7.** $d\mathcal P_S=\frac c4\mathcal D(\omega)d\omega$ et, avec $x=\frac{\hbar\omega}{k_BT}$,
$$\mathcal P_S=\frac c4\cdot\frac{\hbar}{\pi^2c^3}\Big(\frac{k_BT}\hbar\Big)^4\int_0^\infty\frac{x^3dx}{e^x-1}=\frac{\pi^2k_B^4}{60\hbar^3c^2}T^4=\sigma T^4,$$
avec $\sigma\approx5{,}67\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}$ : **loi de Stefan**. (Le facteur $\frac c4$ est exact : il provient de la moyenne $\langle\cos\theta\rangle$ sur un demi-espace.)
""", r"$\lambda_{\max}T=2{,}90\times10^{-3}$ m K ; $\mathcal P_S=\frac{\pi^2k_B^4}{60\hbar^3c^2}T^4$.")

c("p-th-spe4",
r"Un photon d'énergie $hf$ a une quantité de mouvement $\frac{hf}c$ ; pendant $dt$, frappent le miroir les photons situés à moins de $c\,dt$ et allant vers lui.",
r"Force = quantité de mouvement transférée par unité de temps ; pression = force / surface : en 1D, $P_r=\frac U{a^3}=u$.",
r"Pour l'Univers, écris $dU=-P\,dV$ avec $U=aT^4V$ et $P=\frac{aT^4}3$ : intègre.",
r"""
**1.** $N=\frac U{hf}$ ; densité $\nu=\frac N{a^3}=\frac U{hfa^3}$.

**2.** Les photons qui frappent le miroir de droite pendant $dt$ sont ceux à distance $<c\,dt$ et se dirigeant vers la droite (la moitié) : $dN=\frac12\nu a^2c\,dt=\frac{Uc\,dt}{2hfa}$.

**3–4.** $\delta\vec p=-\frac{2hf}c\vec u_x$ par photon, donc $d\vec p=-\frac{2hf}c\,dN\,\vec u_x=-\frac U a\,dt\,\vec u_x$.

**5.** $\vec f_{\mathrm{miroir\to photons}}=-\frac Ua\vec u_x$ ; par l'action-réaction, les photons poussent le miroir avec $\frac Ua$.

**6.** $P_r=\frac{U/a}{a^2}=\frac U{a^3}=u$.

**7.** En 3D, $P=\frac{P_r}3=\frac u3$ : équation d'état du gaz de photons.

**8.** Détente adiabatique quasi statique : $dU=-P\,dV$ avec $U=aT^4V$ :
$$4aT^3V\,dT+aT^4dV=-\frac{aT^4}3dV\ \Rightarrow\ \frac{dT}T=-\frac13\frac{dV}V.$$
Donc $TV^{1/3}=\mathrm{cte}$, et comme $V\propto R^3$ : **$RT=\mathrm{cte}$**. L'expansion refroidit le rayonnement : c'est l'origine du fond diffus cosmologique, émis vers $3000$ K et observé aujourd'hui à $2{,}7$ K (l'Univers s'est dilaté d'un facteur $\approx1100$ depuis).
""", r"$P=\frac u3$ ; détente adiabatique : $TV^{1/3}=\mathrm{cte}$, d'où $RT=\mathrm{cte}$.")

c("p-th-spe5",
r"Injecte $T=T_ae^{i(\omega t-kx)}$ : $\partial_t\to i\omega$, $\partial_x^2\to-k^2$.",
r"Tu obtiens $k^2=-i\frac{\mu c\omega}\lambda$ ; prends la racine de partie réelle positive : $k=\frac{1-i}\delta$.",
r"L'amplitude décroît en $e^{-x/\delta}$ avec $\delta=\sqrt{\frac{2\lambda}{\mu c\omega}}$ ; la température est quasi constante au-delà de quelques $\delta$.",
r"""
**1.** $i\omega\mu c+\lambda k^2=0$, soit $k^2=-i\frac{\mu c\omega}\lambda$.

**2.** $-i=e^{-i\pi/2}$, donc $k=\pm\sqrt{\frac{\mu c\omega}\lambda}e^{-i\pi/4}$ ; la racine de partie réelle positive est
$$k=\sqrt{\frac{\mu c\omega}{2\lambda}}(1-i)=\frac{1-i}\delta,\qquad\delta=\sqrt{\frac{2\lambda}{\mu c\omega}}=\sqrt{\frac{2D}\omega}.$$

**3.** $T(x,t)=T_m+T_0e^{-x/\delta}\cos\big(\omega t-\frac x\delta+\varphi\big)$ : onde amortie, de profondeur de pénétration $\delta$ (et de vitesse $\omega\delta$).

**4.** $D=\frac\lambda{\mu c}=1{,}19\times10^{-7}\ \mathrm{m^2\,s^{-1}}$.
- **(a)** Journalier : $T_m=25\ ^\circ$C, $T_0=10\ ^\circ$C, $\omega=\frac{2\pi}{86\,400}=7{,}3\times10^{-5}\ \mathrm{s^{-1}}$, $\delta\approx5{,}7$ cm. À $3\delta$–$5\delta$ ($\approx20$–$30$ cm), l'oscillation est réduite à 5 %–1 % : température quasi constante.
- **(b)** Annuel : $T_m=15\ ^\circ$C, $T_0=10\ ^\circ$C, $\omega=2{,}0\times10^{-7}\ \mathrm{s^{-1}}$, $\delta\approx1{,}1$ m ; température quasi constante à partir de 4–5 m.

**(c)** Une cave enterrée de quelques mètres reste à température quasi constante toute l'année, égale à la moyenne annuelle (environ $15\ ^\circ$C), avec un déphasage : à $x=\pi\delta\approx3{,}4$ m, elle est en opposition de phase (plus fraîche en été qu'en hiver par rapport à la moyenne) : c'est la « **théorie des caves** » (Fourier).
""", r"$k=\frac{1-i}\delta$, $\delta=\sqrt{2\lambda/(\mu c\omega)}$ : 5,7 cm (jour), 1,1 m (an).")

c("p-th-spe6",
r"En régime permanent, sans source, le flux à travers un cylindre de rayon $r$ et de hauteur $H$ est le même pour tout $r$.",
r"$\Phi=-\lambda\frac{dT}{dr}2\pi rH$ constant donne $r\frac{dT}{dr}=\mathrm{cte}$, d'où $T=A\ln r+B$.",
r"$R_{th}=\frac{T_1-T_2}\Phi=\frac{\ln(a_2/a_1)}{2\pi\lambda H}$ ; développe $\ln(1+\varepsilon/a_1)$ au premier ordre.",
r"""
**1.** Bilan sur la couronne $[r,r+dr]$ de hauteur $H$ en régime permanent : $\Phi(r)=\Phi(r+dr)$, avec $\Phi(r)=j(r)2\pi rH$ et $j=-\lambda\frac{dT}{dr}$ (Fourier). Donc $\frac d{dr}\big(r\frac{dT}{dr}\big)=0$.

**2.** $T(r)=T_1+(T_2-T_1)\dfrac{\ln(r/a_1)}{\ln(a_2/a_1)}$ et $j(r)=\dfrac{\lambda(T_1-T_2)}{r\ln(a_2/a_1)}$.

**3.** $\Phi=j(r)2\pi rH=\dfrac{2\pi\lambda H(T_1-T_2)}{\ln(a_2/a_1)}$, indépendant de $r$. Par analogie avec la loi d'Ohm ($T\leftrightarrow V$, $\Phi\leftrightarrow I$) :
$$R_{th}=\frac{T_1-T_2}\Phi=\frac{\ln(a_2/a_1)}{2\pi\lambda H}.$$

**4.** $a_2=a_1+\varepsilon$ : $\ln\big(1+\frac\varepsilon{a_1}\big)\approx\frac\varepsilon{a_1}$, donc $R_{th}\approx\frac\varepsilon{\lambda\,2\pi a_1H}=\frac e{\lambda S}$ : résistance d'un mur plan d'épaisseur $e=\varepsilon$ et de surface $S=2\pi a_1H$. Normal : un mur mince est localement plan.
""", r"$T=T_1+(T_2-T_1)\frac{\ln(r/a_1)}{\ln(a_2/a_1)}$, $R_{th}=\frac{\ln(a_2/a_1)}{2\pi\lambda H}\approx\frac e{\lambda S}$.")

c("p-th-ccs4",
r"Bilan sur une tranche $[x,x+dx]$ : la production volumique $q$ apparaît comme un terme source.",
r"En régime stationnaire, $kT''+q=0$ : intègre deux fois avec $T(\pm L)=T_0$.",
r"Flux sortant en $x=L$ : $\varphi=-kT'(L)$. Puissance produite par unité de surface : $q\times2L$.",
r"""
**1.** Bilan sur une tranche de section $S$ : $\rho c\,\partial_tT\,S\,dx=-\big[j(x+dx)-j(x)\big]S+qS\,dx$, avec $j=-k\partial_xT$ :
$$\rho c\,\frac{\partial T}{\partial t}=k\frac{\partial^2T}{\partial x^2}+q.$$
Régime stationnaire : conditions aux limites et production constantes, après une durée grande devant $\frac{(2L)^2}{D}$ ($D=\frac k{\rho c}$).

**2.** $kT''=-q$ et, par symétrie, $T'(0)=0$ :
$$T(x)=T_0+\frac q{2k}(L^2-x^2),\qquad T_{\max}=T(0)=T_0+\frac{qL^2}{2k}.$$

**3.** Flux surfacique sortant en $x=+L$ : $\varphi=-kT'(L)=qL$ ; de même en $x=-L$ (vers les $x$ négatifs). Puissance produite par unité de surface de paroi : $2qL=\varphi(L)+\varphi(-L)$ : **conservation de l'énergie vérifiée**.

*Application* : gaine de combustible nucléaire ; la contrainte $T_{\max}<T_{\mathrm{fusion}}$ limite l'épaisseur ($T_{\max}-T_0\propto L^2$).
""", r"$T=T_0+\frac q{2k}(L^2-x^2)$ ; flux sortant $qL$ par face, total $2qL$.")

c("p-th-ccmp4",
r"Dans la glace (mince, régime quasi stationnaire), le profil de température est linéaire entre $T_c$ et $T_{\mathrm{fus}}$.",
r"Le flux qui traverse la glace évacue la chaleur latente de l'eau qui gèle à l'interface : $\rho_g\ell_{\mathrm{fus}}\frac{de}{dt}=\lambda_g\frac{T_{\mathrm{fus}}-T_c}e$.",
r"Sépare les variables : $e\,de=\mathrm{cte}\,dt$.",
r"""
**1.** L'eau à $T_{\mathrm{fus}}$ gèle à l'interface ; la chaleur latente libérée traverse la glace par conduction jusqu'à l'air plus froid. Plus la couche est épaisse, plus elle isole : la croissance ralentit.

**2.** Régime quasi stationnaire dans la glace : profil linéaire, flux surfacique $\varphi=\lambda_g\frac{T_{\mathrm{fus}}-T_c}e$. Pendant $dt$, l'épaisseur gagne $de$ : l'énergie $\rho_g\ell_{\mathrm{fus}}\,de$ (par unité de surface) est évacuée :
$$\rho_g\ell_{\mathrm{fus}}\frac{de}{dt}=\lambda_g\frac{T_{\mathrm{fus}}-T_c}e\ \Rightarrow\ e(t)=\sqrt{e_0^2+\frac{2\lambda_g(T_{\mathrm{fus}}-T_c)}{\rho_g\ell_{\mathrm{fus}}}t}.$$

**3.** $e\propto\sqrt t$ (à partir de $e_0=0$) : croissance rapide puis de plus en plus lente, signature d'un processus diffusif. *Ordre de grandeur* : avec $\lambda_g=2{,}2$ SI, $\Delta T=10$ K, $\rho_g\ell_{\mathrm{fus}}\approx3\times10^8\ \mathrm{J\,m^{-3}}$, environ 10 cm en un jour. Validité du quasi-stationnaire : la chaleur latente domine la chaleur sensible ($c\Delta T\ll\ell_{\mathrm{fus}}$).
""", r"$e(t)=\sqrt{e_0^2+\frac{2\lambda_g(T_{\mathrm{fus}}-T_c)}{\rho_g\ell_{\mathrm{fus}}}t}\propto\sqrt t$.")

c("p-th-ccmp15",
r"Loi de Fourier : $\vec j=-\lambda\overrightarrow{\operatorname{grad}}T$ ($\vec j$ en $\mathrm{W\,m^{-2}}$, $\lambda$ en $\mathrm{W\,m^{-1}\,K^{-1}}$).",
r"En régime permanent, tout le flux $P$ produit traverse chaque cylindre de rayon $r$ dans la graisse : $P=-\lambda\frac{dT}{dr}2\pi rL$.",
r"Intègre entre $R_i$ et $R_e$ puis utilise $P=\alpha M$ avec $M\approx\rho\pi R_i^2L$ : pour maintenir $T_i-T_e$, quelle condition sur $R_i$ ?",
r"""
**1.** $\vec j=-\lambda\overrightarrow{\operatorname{grad}}T$ : $\vec j$ en $\mathrm{W\,m^{-2}}$, $\lambda$ en $\mathrm{W\,m^{-1}\,K^{-1}}$, gradient en $\mathrm{K\,m^{-1}}$.

**2.** Hypothèses : régime permanent, transfert radial (cylindre long, extrémités négligées), pas de source dans la graisse. Le flux à travers un cylindre de rayon $r\in[R_i,R_e]$ vaut la puissance produite :
$$P=-\lambda\frac{dT}{dr}2\pi rL\ \Rightarrow\ \frac{dT}{dr}=-\frac P{2\pi\lambda rL}.$$

**3.** En intégrant : $T_i-T_e=\frac P{2\pi\lambda L}\ln\frac{R_e}{R_i}\approx\frac{P\,\Delta R}{2\pi\lambda LR_i}$ pour $\Delta R\ll R_i$. Avec $P=\alpha M=\alpha\rho\pi R_i^2L$ :
$$T_i-T_e=\frac{\alpha\rho R_i\Delta R}{2\lambda}.$$
Pour une épaisseur de graisse donnée, maintenir $T_i-T_e=33$ K impose
$$R_i\ge R_{\min}=\frac{2\lambda(T_i-T_e)}{\alpha\rho\,\Delta R}.$$
Un animal trop petit perdrait trop de chaleur par rapport à sa production (rapport surface/volume trop grand) : **taille minimale** des mammifères marins. (Avec $\lambda\approx0{,}2$ SI, $\alpha\approx2\ \mathrm{W\,kg^{-1}}$, $\rho\approx10^3$, $\Delta R=5$ cm, on trouve $R_{\min}$ de l'ordre de quelques dizaines de cm.)

**4.** Approximations : cylindre homogène, conduction pure (la circulation sanguine et la convection de l'eau sont négligées), production uniforme. Cela explique aussi que les petits animaux polaires aient un métabolisme plus intense ou une fourrure épaisse.
""", r"$T_i-T_e=\frac{\alpha\rho R_i\Delta R}{2\lambda}$, d'où $R_i\ge\frac{2\lambda(T_i-T_e)}{\alpha\rho\Delta R}$.")

c("p-chim-ccs6",
r"Avant l'équivalence ($V_s<V_0$), c'est la soude versée qui est limitante : $\xi=c_0V_s$.",
r"La température augmente : signe de $\Delta_rH$ ?",
r"Le calorimètre est adiabatique et monobare : $\Delta H=0=\xi\Delta_rH+\Delta H_{\mathrm{temp}}$.",
r"""
**1.** $\mathrm{H_3O^++HO^-\to2H_2O}$, quasi totale ($K=10^{14}$). Pour $V_s\le V_0$, la soude est limitante : $\xi=c_0V_s$ ; au-delà, $\xi=c_0V_0$ (l'acide est épuisé).

**2.** On observe $T(V_s)>T_0$ : la réaction libère de la chaleur, elle est **exothermique** ($\Delta_rH<0$).

**3.** Transformation adiabatique monobare : $\Delta H=0$. On décompose en réaction à $T_0$ puis échauffement du contenu :
$$0=\xi\Delta_rH+\big(m(V_s)+m_{eq}\big)c_{\mathrm{eau}}(T(V_s)-T_0)\ \Rightarrow\ \Delta_rH=-\frac{\big(m(V_s)+m_{eq}\big)c_{\mathrm{eau}}\Delta T_{\mathrm{temp}}}{c_0V_s}\quad(V_s\le V_0),$$
avec $m(V_s)=\rho(V_0+V_s)$. Valeur attendue : $\Delta_rH\approx-57\ \mathrm{kJ\,mol^{-1}}$. Au-delà de l'équivalence, la température diminue (dilution par de la soude froide) : le maximum de $T(V_s)$ repère l'équivalence (titrage thermométrique).
""", r"$\xi=c_0V_s$ ; exothermique ; $\Delta_rH=-\frac{(m+m_{eq})c_{\mathrm{eau}}\Delta T}{c_0V_s}\approx-57\ \mathrm{kJ\,mol^{-1}}$.")

c("p-ccs-bulle",
r"Compare la masse volumique du $\mathrm{CO_2}$ (gaz parfait à 1 bar) à celle du champagne.",
r"Poids négligé, la bulle subit la poussée d'Archimède $\rho_cVg$ et le frottement de Stokes $-6\pi\eta r\vec v$.",
r"Vitesse limite : $6\pi\eta rv_{\lim}=\rho_c\frac43\pi r^3g$. La masse de la bulle est minuscule : que dire du temps caractéristique ?",
r"""
**1.** $\rho_{\mathrm{CO_2}}=\frac{PM}{RT}=\frac{10^5\times0{,}044}{8{,}314\times293}\approx1{,}8\ \mathrm{kg\,m^{-3}}\ll\rho_c=10^3\ \mathrm{kg\,m^{-3}}$ : le poids est environ 550 fois plus faible que la poussée d'Archimède.

**2.** $m\frac{d\vec v}{dt}=\rho_cV g\,\vec u_z-6\pi\eta r\vec v$, avec $m=\rho_{\mathrm{CO_2}}V$, $V=\frac43\pi r^3$.

**3.** $v_{\lim}=\frac{2\rho_cgr^2}{9\eta}$ et $\tau=\frac m{6\pi\eta r}=\frac{2\rho_{\mathrm{CO_2}}r^2}{9\eta}$. Pour $r=0{,}25$ mm : $v_{\lim}\approx0{,}10\ \mathrm{m\,s^{-1}}$ et $\tau\approx2\times10^{-5}$ s : le régime permanent est atteint quasi instantanément. (En réalité il faut ajouter la « masse ajoutée » de liquide entraîné, $\frac12\rho_cV$, ce qui donne $\tau\sim\frac{\rho_cr^2}{9\eta}\approx5$ ms, toujours très court ; et vérifier que le nombre de Reynolds est modéré pour que Stokes s'applique.)

**4.** Le volume augmente car (i) la pression hydrostatique diminue en remontant (effet faible pour quelques cm : $\rho_cgh\approx10^{-2}$ bar) et surtout (ii) le champagne est **sursaturé en $\mathrm{CO_2}$ dissous**, qui diffuse dans la bulle. Comme $v_{\lim}\propto r^2$, la bulle accélère en grossissant.
""", r"$\rho_{\mathrm{CO_2}}\approx1{,}8\ \mathrm{kg\,m^{-3}}$ ; $v_{\lim}=\frac{2\rho_cgr^2}{9\eta}$ ; croissance par diffusion du $\mathrm{CO_2}$ dissous.")
