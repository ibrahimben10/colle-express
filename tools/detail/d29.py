D = {}

D['p-meca-6'] = r"""
**1. Équation du mouvement.** Dans le référentiel du laboratoire (galiléen), en négligeant le poids devant la force magnétique : $m\frac{\mathrm d\vec v}{\mathrm dt}=q\vec v\wedge\vec B$.
- $\vec B$ ne travaille pas : $\frac{\mathrm d}{\mathrm dt}\big(\frac12mv^2\big)=q(\vec v\wedge\vec B)\cdot\vec v=0$, donc $\|\vec v\|=v_0$.
- Sur $\vec u_z$ : $m\dot v_z=0$ et $v_z(0)=0$, donc le mouvement est plan, dans $(Oxy)$.

**1. Forme complexe.** Avec $\vec v\wedge\vec u_z=(v_y,-v_x,0)$, on a $\dot v_x=\omega v_y$ et $\dot v_y=-\omega v_x$. Posons $\underline w=v_x+iv_y$ : $\dot{\underline w}=\omega(v_y-iv_x)=-i\omega\underline w$, donc $\underline w=v_0e^{-i\omega t}$.

**1. Trajectoire.** En intégrant, avec $\underline z(0)=0$ :
$$\underline z=x+iy=\frac{v_0}{-i\omega}\big(e^{-i\omega t}-1\big)=-iR+iRe^{-i\omega t},\qquad R=\frac{v_0}\omega=\frac{mv_0}{qB_0}.$$
C'est un **cercle** de centre $(0,-R)$ et de rayon $R$, parcouru uniformément à la vitesse angulaire $\omega$, dans le sens horaire vu depuis $+\vec u_z$ (car $e^{-i\omega t}$).

**2. Norme de la vitesse.** Le théorème de l'énergie cinétique, avec la force magnétique qui ne travaille pas, donne
$$\frac{\mathrm d}{\mathrm dt}\Big(\frac12mv^2\Big)=-\frac m\tau v^2\iff\frac{\mathrm dv}{\mathrm dt}=-\frac v\tau\iff v(t)=v_0e^{-t/\tau}.$$

**2. Longueur de la trajectoire.** C'est l'intégrale de la vitesse scalaire :
$$L=\int_0^{+\infty}v(t)\,\mathrm dt=v_0\int_0^{+\infty}e^{-t/\tau}\,\mathrm dt=v_0\tau.$$

**3. Composantes de la vitesse.** L'équation devient $\dot{\underline w}=-i\omega\underline w-\frac1\tau\underline w=-\big(\frac1\tau+i\omega\big)\underline w$. Avec $\underline w(0)=v_0$ :
$$\underline w=v_0e^{-t/\tau}e^{-i\omega t},\qquad v_x=v_0e^{-t/\tau}\cos\omega t,\qquad v_y=-v_0e^{-t/\tau}\sin\omega t.$$
On vérifie que $|\underline w|=v_0e^{-t/\tau}$, conformément à la question 2.

**4. Point limite.** $\underline z(t)=\int_0^t\underline w$, et l'intégrale converge en $+\infty$ :
$$\underline z_\infty=v_0\int_0^{+\infty}e^{-(1/\tau+i\omega)t}\,\mathrm dt=\frac{v_0}{\frac1\tau+i\omega}=\frac{v_0\tau}{1+i\omega\tau}=\frac{v_0\tau(1-i\omega\tau)}{1+\omega^2\tau^2}.$$
$$x_\infty=\frac{v_0\tau}{1+\omega^2\tau^2},\qquad y_\infty=-\frac{v_0\omega\tau^2}{1+\omega^2\tau^2}.$$
Limites : si $\omega\tau\to0$ (pas de champ), $x_\infty\to v_0\tau=L$ en ligne droite ; si $\omega\tau\gg1$, $\underline z_\infty\to-\frac{iv_0}\omega=-iR$, le centre du cercle initial.

**5. Allure.** $\underline z_\infty-\underline z(t)=\int_t^{+\infty}\underline w=\frac{v_0e^{-t/\tau}e^{-i\omega t}}{1/\tau+i\omega}$. La distance au point limite décroît exponentiellement, et l'angle tourne uniformément : c'est une **spirale logarithmique** qui s'enroule (sens horaire) vers le point limite. En chambre à bulles, le rayon de courbure initial $\frac{mv_0}{qB_0}$ donne la quantité de mouvement (rapportée à la charge) ; le sens d'enroulement donne le signe de $q$.
"""

D['p-meca-7'] = r"""
**1. Hypothèse de non-glissement.** Si le cube ne glisse pas, il a le même mouvement que le chariot. On note $x$ l'écart à la position d'équilibre (ressort au repos). L'ensemble {chariot + cube}, de masse $M+m$, est soumis horizontalement à la seule force du ressort, $-kx$ (la table est sans frottement, et les forces cube/chariot sont intérieures). Donc
$$(M+m)\ddot x=-kx\quad\Longrightarrow\quad x=X_m\cos(\omega t+\varphi),\qquad\omega^2=\frac k{M+m}.$$

**1. Forces sur le cube.** Le cube subit son poids $-mg\vec u_z$, la réaction normale $N\vec u_z$ et la force de frottement horizontale $T\vec u_x$ exercée par le chariot.
- Verticalement : pas de mouvement, donc $N=mg$.
- Horizontalement : $T=m\ddot x=-m\omega^2x$.

**1. Valeur maximale de $|T|$.** $|T|=m\omega^2|x|$ est maximal aux élongations extrêmes ($|x|=X_m$), là où l'accélération est maximale : $|T|_{\max}=m\omega^2X_m$.

**1. Loi de Coulomb.** Le non-glissement exige $|T|\le\mu N$ à chaque instant, donc il suffit qu'il soit vérifié aux extrémités :
$$m\omega^2X_m\le\mu mg\iff X_m\le\frac{\mu g}{\omega^2}.$$

**Conclusion.**
$$X_{\max}=\frac{\mu g}{\omega^2}=\frac{\mu g(M+m)}k.$$
La masse $m$ se simplifie dans la condition, mais elle intervient dans $\omega$. Au-delà de $X_{\max}$, le cube commence à glisser aux positions extrêmes du mouvement.
"""

D['p-meca-8'] = r"""
**0. Cadre.** On travaille dans le référentiel du camion, en translation d'accélération $A\vec u_x$ (vers l'avant) : il faut ajouter la force d'inertie $-mA\vec u_x$ appliquée en $G$, et il n'y a pas de force de Coriolis. On note $x$ l'abscisse de $G$ dans ce référentiel, $\omega$ la vitesse angulaire du tonneau (rotation autour de son axe horizontal), $T$ la composante tangentielle et $N$ la composante normale de la réaction du plateau.

**1. Hypothèse de roulement sans glissement.** La vitesse du point de contact $I$ du tonneau est nulle par rapport au plateau : $v_I=\dot x\mp b\omega=0$, soit $|\dot x|=b|\omega|$.

**1. Énergie cinétique.** Par le théorème de König :
$$E_c=\frac12m\dot x^2+\frac12J\omega^2=\frac12m\dot x^2+\frac12\cdot\frac12mb^2\cdot\frac{\dot x^2}{b^2}=\frac34m\dot x^2.$$

**1. Puissance des forces.** La réaction du plateau s'applique en $I$, de vitesse nulle : puissance nulle. Le poids est vertical, et $G$ se déplace horizontalement : puissance nulle. La force d'inertie a pour puissance $-mA\dot x$. Par le théorème de la puissance cinétique :
$$\frac{\mathrm d}{\mathrm dt}\Big(\frac34m\dot x^2\Big)=\frac32m\dot x\ddot x=-mA\dot x\quad\Longrightarrow\quad\ddot x=-\frac{2A}3.$$
Le tonneau recule par rapport au camion avec l'accélération $\frac{2A}3$, moins vite que s'il glissait sans frottement (il reculerait alors avec l'accélération $A$).

**1. Calcul de la réaction.** Le théorème de la résultante cinétique s'écrit $m\ddot x=T-mA$ sur $\vec u_x$ et $0=N-mg$ sur $\vec u_z$. Donc
$$T=m\ddot x+mA=mA-\frac{2mA}3=\frac{mA}3>0,\qquad N=mg.$$
La force de frottement est dirigée vers l'avant : c'est elle qui fait tourner le tonneau.

**1. Condition de Coulomb.** Il faut $|T|\le\mu N$, soit $\frac{mA}3\le\mu mg$.
- **Roulement sans glissement** si $A\le3\mu g$.
- **Glissement** si $A>3\mu g$. Alors $T=\mu N=\mu mg$ (vers l'avant, car le tonneau glisse vers l'arrière par rapport au plateau), et $m\ddot x=\mu mg-mA$, donc $\ddot x=-(A-\mu g)$.

**2. Hypothèse géométrique.** Le tonneau, initialement immobile, a son point de contact à la distance $d$ du bord arrière du plateau (il est placé tout à l'avant). Il tombe quand son point de contact, à la verticale de $G$, atteint le bord arrière, c'est-à-dire après un recul $d$ par rapport au camion.

**2. Durée de la chute.** Le recul est uniformément accéléré, d'accélération $a_r$ : $d=\frac12a_rt_c^2$, donc $t_c^2=\frac{2d}{a_r}$.

**2. Distance parcourue par le camion.** Le camion part du repos avec l'accélération $A$ (référentiel terrestre) : $L=\frac12At_c^2=d\,\frac A{a_r}$.
- Roulement sans glissement ($a_r=\frac{2A}3$) : $L=\frac32d$, **indépendant de $A$**.
- Glissement ($a_r=A-\mu g$) : $L=\frac{dA}{A-\mu g}$, qui tend vers $d$ quand $A\to\infty$.

Les deux expressions coïncident pour $A=3\mu g$ : $\frac{3\mu g\,d}{2\mu g}=\frac32d$. ✓ Dans le référentiel terrestre, le tonneau avance pendant ce temps de $L-d=\frac d2$ dans le cas sans glissement.
"""

D['p-meca-9'] = r"""
**0. Géométrie.** Les cylindres sont en $x=-\frac D2$ (cylindre 1) et $x=+\frac D2$ (cylindre 2) ; le centre $G$ de la plaque est en $x$. Les surfaces des cylindres en contact avec la plaque se déplacent vers le milieu : à gauche avec la vitesse $+R_c\omega$ et à droite avec $-R_c\omega$, où $R_c$ est le rayon des cylindres.

**1. Réactions normales.** La plaque n'a pas de mouvement vertical : $N_1+N_2-mg=0$.

**1. Moment en $G$.** La plaque ne tourne pas : le moment résultant en $G$ est nul. Le poids s'applique en $G$, et les réactions normales ont pour bras de levier $\frac D2+x$ (contact 1, à gauche de $G$) et $\frac D2-x$ (contact 2). Les forces de frottement sont horizontales, appliquées sous la plaque, à une distance de $G$ égale à la demi-épaisseur, supposée négligeable : leur moment est négligé. D'où
$$N_1\Big(\frac D2+x\Big)=N_2\Big(\frac D2-x\Big).$$

**1. Résolution.** Avec $N_2=mg-N_1$ : $N_1\big(\frac D2+x\big)=(mg-N_1)\big(\frac D2-x\big)$, donc $N_1D=mg\big(\frac D2-x\big)$ :
$$N_1=mg\,\frac{D/2-x}D,\qquad N_2=mg\,\frac{D/2+x}D,\qquad N_1-N_2=-\frac{2mg}Dx.$$
Le cylindre le plus proche de $G$ porte la plus grande charge.

**1. Sens des frottements.** On suppose $|\dot x|<R_c\omega$ : il y a glissement aux deux contacts.
- Contact 1 : la vitesse de la plaque par rapport à la surface vaut $\dot x-R_c\omega<0$. Le frottement s'oppose à ce glissement : il vaut $+\mu_dN_1\vec u_x$.
- Contact 2 : la vitesse relative vaut $\dot x+R_c\omega>0$, donc le frottement vaut $-\mu_dN_2\vec u_x$.

Chaque cylindre tire la plaque vers le milieu.

**1. Équation du mouvement.** Le théorème de la résultante, sur $\vec u_x$, donne
$$m\ddot x=\mu_dN_1-\mu_dN_2=-\frac{2\mu_dmg}Dx\iff\ddot x+\frac{2\mu_dg}Dx=0.$$

**Conclusion.** La plaque oscille harmoniquement autour du milieu, avec la pulsation et la période
$$\Omega=\sqrt{\frac{2\mu_dg}D},\qquad T=2\pi\sqrt{\frac D{2\mu_dg}}.$$
Ce résultat est valable tant que le glissement persiste, c'est-à-dire tant que l'amplitude des vitesses $X_m\Omega$ reste inférieure à $R_c\omega$. La mesure de $T$ donne $\mu_d$. Si les cylindres tournaient dans l'autre sens, on aurait $\ddot x=+\frac{2\mu_dg}Dx$ : l'équilibre serait instable, et la plaque serait éjectée.
"""

D['p-meca-10'] = r"""
**0. Modèle.** Les rouleaux sont espacés de $2R+\varepsilon$, et le solide a une longueur $10R$. Quatre intervalles mesurent $8R+4\varepsilon<10R$ et cinq intervalles $10R+5\varepsilon>10R$ : au moment où l'avant du solide atteint le $(n+1)$-ième rouleau, le solide repose sur **4 rouleaux** qui roulent déjà sans glisser (à $\omega=\frac{V_n}R$), plus le nouveau, immobile. Le rouleau qui quitte l'arrière du solide emporte son moment cinétique sans interagir. Les axes sont fixes, et chaque rouleau ne reçoit du solide qu'une force tangentielle (les réactions des axes ont un moment nul).

**1. Méthode des percussions.** La phase de glissement est brève. Notons $\Pi_0$ la percussion tangentielle (intégrale de la force de frottement) que le solide exerce sur le nouveau rouleau, et $\Pi_k$ ($k=1,\dots,4$) celles qu'il exerce sur les anciens rouleaux, comptées positivement vers l'avant.

**1. Nouveau rouleau.** Le théorème du moment cinétique par rapport à son axe donne $J\big(\omega_f-0\big)=R\,\Pi_0$. Après la phase de glissement, il roule sans glisser : $\omega_f=\frac{V_{n+1}}R$. Donc
$$\Pi_0=\frac J{R^2}V_{n+1}=\frac m2V_{n+1}.$$

**1. Anciens rouleaux.** Ils restent en roulement sans glissement, donc leur vitesse angulaire passe de $\frac{V_n}R$ à $\frac{V_{n+1}}R$ :
$$\Pi_k=\frac m2\big(V_{n+1}-V_n\big)<0.$$
En ralentissant, ils poussent le solide vers l'avant.

**1. Solide.** Par la loi des actions réciproques, il reçoit $-\sum\Pi$ :
$$M(V_{n+1}-V_n)=-\Pi_0-\sum_{k=1}^4\Pi_k=-\frac m2V_{n+1}-2m(V_{n+1}-V_n).$$

**1. Résolution.** $(M+2m)V_{n+1}+\frac m2V_{n+1}=(M+2m)V_n$, donc
$$V_{n+1}=\frac{M+2m}{M+\frac52m}V_n=\frac{7m}{7{,}5m}V_n=\frac{14}{15}V_n.$$

**1. Résultat.** La suite est géométrique :
$$V_n=V_0\Big(\frac{14}{15}\Big)^n.$$
Le résultat ne dépend pas du coefficient de frottement : celui-ci ne fixe que la durée du glissement.

**1. Vérification par les forces.** Pendant le glissement, le nouveau rouleau reçoit la force de frottement $\mu N$ : $J\dot\omega_0=\mu NR$, soit $R\omega_0=\frac{2\mu N}mt$. Chaque ancien rouleau impose au solide une force $-\frac m2\dot V$, donc $(M+2m)\dot V=-\mu N$ et $V=V_n-\frac{\mu N}{M+2m}t$. Le glissement cesse quand $V=R\omega_0$, c'est-à-dire pour $V_n=\mu Nt_f\big(\frac1{M+2m}+\frac2m\big)$. Alors $\frac{V_{n+1}}{V_n}=\frac{2/m}{\frac1{M+2m}+\frac2m}=\frac{2(M+2m)}{m+2(M+2m)}=\frac{14m}{15m}$. ✓

**Bilan énergétique.** L'énergie cinétique du système juste avant le contact vaut $\frac12(M+2m)V_n^2$ ; juste après, elle vaut $\frac12\big(M+\frac52m\big)V_{n+1}^2$. Le rapport vaut $\frac{14}{15}<1$ : le glissement dissipe à chaque rouleau la fraction $\frac1{15}$ de l'énergie, et le solide ralentit géométriquement.

**Remarque.** Si l'on néglige l'inertie des rouleaux déjà en rotation (modèle plus grossier, où seul le nouveau rouleau intervient), on obtient $MV_n=\big(M+\frac m2\big)V_{n+1}$, soit $V_n=V_0\big(\frac{10}{11}\big)^n$.
===RÉPONSE===
$V_{n+1}=\dfrac{M+2m}{M+\frac52m}V_n$, d'où $V_n=V_0\big(\frac{14}{15}\big)^n$ (4 rouleaux déjà en rotation ; en négligeant leur inertie : $(\frac{10}{11})^n$).
"""
