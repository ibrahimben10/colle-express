D = {}

D['n-p2-isolant'] = r"""
**1. Bilan sur une couronne.** On considère la couronne de gaine comprise entre $r$ et $r+\mathrm dr$, de longueur $L$. En régime permanent, sans source dans l'isolant, l'énergie qui entre en $r$ ressort en $r+\mathrm dr$ : $\Phi(r)=\Phi(r+\mathrm dr)$. Le flux $\Phi$ à travers un cylindre coaxial est donc indépendant de $r$.

**1. Loi de Fourier.** Le transfert est radial : $\Phi=j(r)\cdot2\pi rL=-\lambda\frac{\mathrm dT}{\mathrm dr}2\pi rL$, donc $\frac{\mathrm dT}{\mathrm dr}=-\frac\Phi{2\pi\lambda Lr}$. En intégrant de $r_1$ (température $T_1$) à $r_2$ (température $T_2$ de la surface extérieure) :
$$T_1-T_2=\frac\Phi{2\pi\lambda L}\ln\frac{r_2}{r_1}\quad\Longrightarrow\quad R_{\mathrm{gaine}}=\frac{T_1-T_2}\Phi=\frac{\ln(r_2/r_1)}{2\pi\lambda L}.$$

**2. Résistance conducto-convective.** À la surface extérieure, d'aire $2\pi r_2L$, la loi de Newton donne $\Phi=h\cdot2\pi r_2L\,(T_2-T_e)$, d'où $R_h=\frac{T_2-T_e}\Phi=\frac1{2\pi hr_2L}$.

**2. Association en série.** Le même flux traverse la gaine puis l'interface gaine/air : les résistances s'ajoutent.
$$R=R_{\mathrm{gaine}}+R_h=\frac1{2\pi L}\Big(\frac{\ln(r_2/r_1)}\lambda+\frac1{hr_2}\Big).$$

**3. Étude de $R(r_2)$.**
$$\frac{\mathrm dR}{\mathrm dr_2}=\frac1{2\pi L}\Big(\frac1{\lambda r_2}-\frac1{hr_2^2}\Big)=\frac1{2\pi Lr_2^2}\Big(\frac{r_2}\lambda-\frac1h\Big).$$
Cette dérivée est négative pour $r_2<\frac\lambda h$ et positive au-delà : $R$ passe par un **minimum** en
$$r_c=\frac\lambda h=\frac{0{,}20}{10}=2{,}0\times10^{-2}\ \mathrm m=2{,}0\ \mathrm{cm}.$$

**3. Conséquence.** Le flux perdu, $\Phi=\frac{T_1-T_e}R$, est **maximal** pour $r_2=r_c$. Pour un fil fin ($r_1=1$ mm $<r_c$), ajouter de l'isolant jusqu'à $r_c$ **augmente** les pertes thermiques ! La résistance de conduction croît lentement (en $\ln r_2$), alors que la résistance de convection diminue vite (en $\frac1{r_2}$), car la surface d'échange augmente.

**3. Commentaire.** Pour un câble électrique, c'est favorable : la gaine isole électriquement tout en aidant à évacuer la chaleur produite par effet Joule. Pour calorifuger un tuyau chaud, l'isolant n'est efficace que si le rayon du tuyau dépasse déjà $r_c$, ou si la couche est assez épaisse pour que $R(r_2)>R(r_1)$.
"""

D['n-p2-peau'] = r"""
**1. Équations de base.** Dans le conducteur :
- Maxwell-Faraday : $\overrightarrow{\mathrm{rot}}\,\vec E=-\frac{\partial\vec B}{\partial t}$ ;
- Maxwell-Ampère dans l'ARQS (courant de déplacement négligé), avec la loi d'Ohm locale $\vec j=\gamma\vec E$ : $\overrightarrow{\mathrm{rot}}\,\vec B=\mu_0\vec j=\mu_0\gamma\vec E$ ;
- Maxwell-Gauss : le conducteur reste localement neutre, $\rho=0$, donc $\mathrm{div}\,\vec E=0$.

**1. Combinaison.** On prend le rotationnel de Maxwell-Faraday et on utilise $\overrightarrow{\mathrm{rot}}\,\overrightarrow{\mathrm{rot}}\,\vec E=\overrightarrow{\mathrm{grad}}(\mathrm{div}\,\vec E)-\Delta\vec E=-\Delta\vec E$ :
$$-\Delta\vec E=-\frac{\partial}{\partial t}\overrightarrow{\mathrm{rot}}\,\vec B=-\mu_0\gamma\frac{\partial\vec E}{\partial t}\quad\Longrightarrow\quad\Delta\vec E=\mu_0\gamma\frac{\partial\vec E}{\partial t}.$$
C'est une **équation de diffusion** (comme l'équation de la chaleur), et non une équation de propagation.

**2. Relation de dispersion.** Avec $\underline E=E_0e^{j(\omega t-\underline kz)}$ : $\Delta\to-\underline k^2$ et $\frac{\partial}{\partial t}\to j\omega$. Donc
$$-\underline k^2=j\mu_0\gamma\omega\iff\underline k^2=-j\mu_0\gamma\omega.$$

**2. Racines.** On pose $\delta=\sqrt{\frac2{\mu_0\gamma\omega}}$, de sorte que $\mu_0\gamma\omega=\frac2{\delta^2}$ et $\underline k^2=-\frac{2j}{\delta^2}$. Or $(1-j)^2=1-2j-1=-2j$, donc
$$\underline k=\pm\frac{1-j}\delta.$$

**2. Choix physique.** Avec $\underline k=\varepsilon\frac{1-j}\delta$ ($\varepsilon=\pm1$), on a $e^{-j\underline kz}=e^{-j\varepsilon z/\delta}e^{-\varepsilon z/\delta}$. Le champ doit rester borné quand $z\to+\infty$, donc $\varepsilon=+1$. En prenant la partie réelle :
$$E(z,t)=E_0e^{-z/\delta}\cos\Big(\omega t-\frac z\delta\Big).$$
Le champ, et donc le courant $\gamma\vec E$, s'atténue sur l'épaisseur $\delta$ : c'est l'**épaisseur de peau**.

**3. À 50 Hz.**
$$\delta=\sqrt{\frac2{4\pi\times10^{-7}\times6{,}0\times10^7\times2\pi\times50}}=\sqrt{\frac2{2{,}37\times10^4}}=\sqrt{8{,}4\times10^{-5}}\approx9{,}2\ \mathrm{mm}.$$

**3. À 1 MHz.** $\delta\propto\frac1{\sqrt f}$, et la fréquence est multipliée par $2\times10^4$, donc $\delta$ est divisé par $\sqrt{2\times10^4}\approx141$ : $\delta\approx65\ \mu$m.

**3. Conséquences pratiques.**
- À 50 Hz, il est inutile d'utiliser des conducteurs massifs de rayon supérieur à environ 1 cm : le cœur ne porterait presque pas de courant. Les lignes à haute tension utilisent des câbles torsadés, avec une âme en acier pour la résistance mécanique.
- En haute fréquence, le courant circule en surface : la résistance effective augmente (section utile $\sim2\pi r\delta$). D'où les conducteurs creux, le fil de Litz (brins isolés et entrelacés), et l'argenture des conducteurs HF (seule la surface compte).
- Le blindage électromagnétique repose sur le même phénomène : quelques $\delta$ de métal arrêtent les champs HF.

**4. Justification de l'ARQS.** En régime sinusoïdal, le courant de déplacement vaut $\varepsilon_0\frac{\partial\vec E}{\partial t}$, d'amplitude $\varepsilon_0\omega E$, et le courant de conduction vaut $\gamma E$. Leur rapport est
$$\frac{\varepsilon_0\omega}\gamma=\frac{8{,}85\times10^{-12}\times2\pi f}{6{,}0\times10^7}\approx10^{-18}\,f\ (f\ \text{en Hz}).$$
Il reste négligeable jusqu'à $f\sim10^{17}$ Hz. En pratique, c'est le modèle de conduction (loi d'Ohm statique) qui cesse d'être valable avant, vers $10^{13}$ Hz (infrarouge).
"""

D['n-p2-bohr'] = r"""
**1. Énergie cinétique minimale.** L'électron est confiné dans une région de taille $a$ : $\Delta x\sim a$. L'inégalité de Heisenberg, $\Delta x\Delta p\gtrsim\hbar$, donne $\Delta p\gtrsim\frac\hbar a$. Par symétrie, l'impulsion moyenne est nulle ($\langle p\rangle=0$), donc $\langle p^2\rangle=\Delta p^2+\langle p\rangle^2=\Delta p^2$ et
$$\langle E_c\rangle=\frac{\langle p^2\rangle}{2m_e}\gtrsim\frac{\hbar^2}{2m_ea^2}.$$
Plus on confine l'électron, plus son énergie cinétique est grande : c'est l'énergie de confinement.

**2. Énergie totale.** L'énergie potentielle électrostatique de l'électron à une distance typique $a$ du proton vaut $-\frac{e^2}{4\pi\varepsilon_0a}$. En prenant l'énergie cinétique à sa valeur minimale :
$$E(a)\approx\frac{\hbar^2}{2m_ea^2}-\frac{e^2}{4\pi\varepsilon_0a}.$$

**2. Existence d'un équilibre.**
- Pour $a\to0$, le terme cinétique en $+\frac1{a^2}$ l'emporte : $E\to+\infty$.
- Pour $a\to+\infty$, $E\to0^-$ (le terme coulombien en $-\frac1a$ domine).

$E(a)$ passe donc par un minimum négatif. En se rapprochant du proton, l'électron gagne de l'énergie potentielle, mais il paie un prix de confinement qui croît plus vite : il ne peut pas « tomber » sur le proton. La stabilité de l'atome est un effet quantique, inexplicable classiquement.

**3. Minimisation.**
$$E'(a)=-\frac{\hbar^2}{m_ea^3}+\frac{e^2}{4\pi\varepsilon_0a^2}=0\iff a=a_0=\frac{4\pi\varepsilon_0\hbar^2}{m_ee^2}.$$

**3. Application numérique.**
$$a_0=\frac{(1{,}05\times10^{-34})^2}{9{,}11\times10^{-31}\times9{,}0\times10^9\times(1{,}60\times10^{-19})^2}=\frac{1{,}10\times10^{-68}}{2{,}10\times10^{-58}}\approx5{,}3\times10^{-11}\ \mathrm m=53\ \mathrm{pm}.$$

**3. Énergie minimale.** En $a_0$, $\frac{\hbar^2}{m_ea_0^2}=\frac{e^2}{4\pi\varepsilon_0a_0}$, donc le terme cinétique vaut la moitié de l'énergie potentielle, en valeur absolue (théorème du viriel) :
$$E_{\min}=\frac12\cdot\frac{e^2}{4\pi\varepsilon_0a_0}-\frac{e^2}{4\pi\varepsilon_0a_0}=-\frac{e^2}{8\pi\varepsilon_0a_0}=-\frac{9{,}0\times10^9\times(1{,}6\times10^{-19})^2}{2\times5{,}3\times10^{-11}}\approx-2{,}2\times10^{-18}\ \mathrm J\approx-13{,}6\ \mathrm{eV}.$$

**3. Commentaire.** On retrouve exactement le rayon de Bohr et l'énergie de l'état fondamental de l'hydrogène (l'énergie d'ionisation vaut $13{,}6$ eV). L'accord parfait est en partie fortuit, car le choix $\Delta x\Delta p\sim\hbar$ est arbitraire à un facteur près. Mais l'ordre de grandeur est robuste, et ce raisonnement explique la taille des atomes (environ $10^{-10}$ m).
"""

D['n-p2-marche'] = r"""
**1. Région $x<0$.** $V=0$ et $E>0$ : l'équation $\varphi''=-k_1^2\varphi$, avec $k_1=\frac{\sqrt{2m_eE}}\hbar$, a pour solutions $e^{\pm ik_1x}$. On a une onde incidente (vers $+x$) d'amplitude 1 et une onde réfléchie d'amplitude $r$ :
$$\varphi(x)=e^{ik_1x}+re^{-ik_1x}.$$

**1. Région $x>0$.** $V=V_0<E$ : $\varphi''=-k_2^2\varphi$, avec $k_2=\frac{\sqrt{2m_e(E-V_0)}}\hbar$. Rien ne vient de $+\infty$, donc il n'y a qu'une onde transmise :
$$\varphi(x)=te^{ik_2x}.$$

**1. Raccordement.** Le potentiel a une discontinuité finie : $\varphi$ et $\varphi'$ sont continues en $x=0$ (en intégrant l'équation de Schrödinger sur $[-\varepsilon,\varepsilon]$, le saut de $\varphi'$ tend vers 0).
$$1+r=t,\qquad ik_1(1-r)=ik_2t.$$

**1. Résolution.** On reporte $t=1+r$ : $k_1-k_1r=k_2+k_2r$, donc
$$r=\frac{k_1-k_2}{k_1+k_2},\qquad t=1+r=\frac{2k_1}{k_1+k_2}.$$

**2. Conservation de la probabilité.**
$$R+T=\frac{(k_1-k_2)^2}{(k_1+k_2)^2}+\frac{k_2}{k_1}\cdot\frac{4k_1^2}{(k_1+k_2)^2}=\frac{k_1^2-2k_1k_2+k_2^2+4k_1k_2}{(k_1+k_2)^2}=\frac{(k_1+k_2)^2}{(k_1+k_2)^2}=1.$$
Le facteur $\frac{k_2}{k_1}$ dans $T$ vient du fait que le courant de probabilité est proportionnel à la vitesse $\frac{\hbar k}m$ : les particules transmises vont moins vite.

**2. Cas $E=2V_0$.** $\frac{k_2}{k_1}=\sqrt{\frac{E-V_0}E}=\frac1{\sqrt2}$, donc
$$r=\frac{1-1/\sqrt2}{1+1/\sqrt2}=\frac{\sqrt2-1}{\sqrt2+1}\approx0{,}17,\qquad R=r^2\approx0{,}029.$$
Environ 3 % des électrons sont réfléchis.

**2. Comparaison classique.** Une particule classique d'énergie $E>V_0$ franchit toujours la marche, en ralentissant ($R=0$). La réflexion partielle est un effet purement **ondulatoire**, analogue à la réflexion partielle de la lumière sur un dioptre (ou d'une onde sur une corde dont la masse linéique change).

**3. Cas $E<V_0$.** Pour $x>0$, $\varphi''=\frac1{\delta^2}\varphi$, avec $\delta=\frac\hbar{\sqrt{2m_e(V_0-E)}}$. La solution bornée est $\varphi=te^{-x/\delta}$. Les formules précédentes restent valables en remplaçant $k_2$ par $\frac i\delta$ (car $e^{ik_2x}=e^{-x/\delta}$).

**3. Réflexion totale.** $r=\frac{k_1-i/\delta}{k_1+i/\delta}$ est le quotient de deux complexes conjugués, donc $|r|=1$ et $R=1$ : toutes les particules finissent par être réfléchies, et le courant de probabilité transmis est nul (onde évanescente).

**3. Pénétration.** Pourtant, $|\varphi|^2=|t|^2e^{-2x/\delta}\neq0$ pour $x>0$ : l'électron a une probabilité non nulle de se trouver dans la zone classiquement interdite, sur une profondeur de l'ordre de $\delta$.

**3. Application numérique.** $V_0-E=1{,}0$ eV $=1{,}6\times10^{-19}$ J :
$$\delta=\frac{1{,}05\times10^{-34}}{\sqrt{2\times9{,}11\times10^{-31}\times1{,}6\times10^{-19}}}=\frac{1{,}05\times10^{-34}}{5{,}4\times10^{-25}}\approx1{,}9\times10^{-10}\ \mathrm m\approx0{,}2\ \mathrm{nm}.$$

**3. Conséquence.** Si la marche est remplacée par une barrière d'épaisseur comparable à $\delta$ (quelques angströms), l'onde évanescente atteint l'autre côté et une fraction des électrons traverse : c'est l'**effet tunnel**, exploité par le microscope à effet tunnel (STM). Le courant y varie exponentiellement avec la distance pointe-surface, ce qui donne une résolution atomique.
"""

D['n-p2-doublet'] = r"""
**1. Différence de marche.** En lame d'air, le Michelson est équivalent à deux miroirs parallèles distants de $e$ ($M_1'$, image de $M_1$ par la séparatrice, et $M_2$). Un rayon incident sous l'angle $i$ donne deux rayons émergents parallèles. Le calcul classique de la lame à faces parallèles (indice 1) donne
$$\delta=2e\cos i.$$

**1. Localisation et forme.** Les deux rayons qui interfèrent sont parallèles : ils se rencontrent à l'infini, et les franges sont localisées à l'infini. On les observe dans le plan focal d'une lentille. $\delta$ ne dépend que de $i$ : tous les rayons de même inclinaison donnent le même éclairement. Par symétrie de révolution autour de l'axe de la lentille, les points d'égale inclinaison forment des cercles : ce sont des **anneaux** (franges d'égale inclinaison). Au centre ($i=0$), $\delta=2e$ est maximal.

**2. Superposition incohérente.** Les deux raies sont incohérentes entre elles : leurs éclairements s'ajoutent. Chacune, d'éclairement $\mathcal E_0$ par voie, donne $2\mathcal E_0\big(1+\cos\frac{2\pi\delta}\lambda\big)$, d'où (au facteur près)
$$\mathcal E=\mathcal E_0\Big[2+\cos\frac{2\pi\delta}{\lambda_1}+\cos\frac{2\pi\delta}{\lambda_2}\Big].$$

**2. Transformation en produit.** Avec $\cos p+\cos q=2\cos\frac{p-q}2\cos\frac{p+q}2$ :
$$\mathcal E=2\mathcal E_0\Big[1+\cos\Big(\pi\delta\Big(\frac1{\lambda_1}-\frac1{\lambda_2}\Big)\Big)\cos\Big(\pi\delta\Big(\frac1{\lambda_1}+\frac1{\lambda_2}\Big)\Big)\Big].$$

**2. Approximations.** $\frac1{\lambda_1}-\frac1{\lambda_2}=\frac{\lambda_2-\lambda_1}{\lambda_1\lambda_2}\approx\frac{\Delta\lambda}{\lambda_m^2}$ et $\frac1{\lambda_1}+\frac1{\lambda_2}\approx\frac2{\lambda_m}$, avec $\lambda_m=589{,}3$ nm. D'où la formule demandée :
$$\mathcal E=2\mathcal E_0\Big[1+\cos\Big(\frac{\pi\Delta\lambda\,\delta}{\lambda_m^2}\Big)\cos\Big(\frac{2\pi\delta}{\lambda_m}\Big)\Big].$$

**2. Interprétation.** Le second cosinus varie vite (période $\lambda_m$ en $\delta$) : ce sont les franges. Le premier varie lentement (période $\frac{2\lambda_m^2}{\Delta\lambda}$) : il module le **contraste**, $C=\big|\cos\frac{\pi\Delta\lambda\,\delta}{\lambda_m^2}\big|$. Ce sont des battements entre les deux systèmes de franges.

**3. Brouillages.** Le contraste s'annule pour $\frac{\pi\Delta\lambda\,\delta}{\lambda_m^2}=\frac\pi2+p\pi$. Les annulations successives sont séparées de $\Delta\delta=\frac{\lambda_m^2}{\Delta\lambda}$. Au centre, $\delta=2e$, donc le miroir doit être déplacé de
$$\Delta e=\frac{\lambda_m^2}{2\Delta\lambda}=\frac{(589{,}3\times10^{-9})^2}{2\times0{,}6\times10^{-9}}=\frac{3{,}47\times10^{-13}}{1{,}2\times10^{-9}}\approx2{,}9\times10^{-4}\ \mathrm m=0{,}29\ \mathrm{mm}.$$
Le premier brouillage a lieu à $e=\frac{\Delta e}2\approx0{,}14$ mm du contact optique.

**3. Nombre d'anneaux.** Un anneau défile au centre chaque fois que $\delta=2e$ varie de $\lambda_m$. Entre deux brouillages :
$$N=\frac{2\Delta e}{\lambda_m}=\frac{\lambda_m}{\Delta\lambda}=\frac{589{,}3}{0{,}6}\approx980\ \text{anneaux}.$$

**3. Application.** Inversement, en mesurant la distance entre deux brouillages (au micromètre près, sur le vernier du chariot), on obtient $\Delta\lambda=\frac{\lambda_m^2}{2\Delta e}$ avec une bonne précision. C'est une mesure classique de l'écart du doublet jaune du sodium.
"""

D['n-p2-reseau'] = r"""
**1. Pas du réseau.** Avec $n=500$ traits par mm : $a=\frac1n=\frac{1\ \mathrm{mm}}{500}=2{,}0\ \mu$m.

**1. Condition d'interférences constructives.** Sous incidence normale, deux rayons diffractés dans la direction $\theta$ par des traits voisins ont la différence de marche $\delta=a\sin\theta$. Les $N$ ondes sont toutes en phase (maximum principal) si $\delta$ est un multiple de $\lambda$ :
$$a\sin\theta_p=p\lambda,\qquad p\in\mathbb Z.$$

**2. Ordre maximal.** Il faut $|\sin\theta_p|\le1$, soit $|p|\le\frac a\lambda$.
- **Rouge** ($700$ nm) : $\frac a\lambda=\frac{2000}{700}=2{,}86$, donc l'ordre maximal est 2.
- **Violet** ($400$ nm) : $\frac a\lambda=\frac{2000}{400}=5$. L'ordre 5 correspond à $\sin\theta=1$, soit $\theta=90^\circ$ (lumière rasante, inobservable). En pratique, l'ordre maximal est 4.

**3. Ordres 2 et 3.**
- Extrémité rouge de l'ordre 2 : $\sin\theta=\frac{2\times0{,}70}{2{,}0}=0{,}70$.
- Extrémité violette de l'ordre 3 : $\sin\theta=\frac{3\times0{,}40}{2{,}0}=0{,}60$.

Comme $0{,}60<0{,}70$, le début du spectre d'ordre 3 empiète sur la fin du spectre d'ordre 2 : ils **se recouvrent**. Par exemple, le rouge à 600 nm d'ordre 2 et le violet à 400 nm d'ordre 3 sont au même angle. C'est un phénomène général, puisque $p\lambda_{\max}>(p+1)\lambda_{\min}$ dès que $\frac{p+1}p<\frac{700}{400}=1{,}75$, soit $p\ge2$.

**3. Ordres 1 et 2.**
- Extrémité rouge de l'ordre 1 : $\sin\theta=\frac{0{,}70}{2{,}0}=0{,}35$.
- Extrémité violette de l'ordre 2 : $\sin\theta=\frac{2\times0{,}40}{2{,}0}=0{,}40$.

Comme $0{,}35<0{,}40$, il n'y a **pas de recouvrement** : le spectre d'ordre 1 est entièrement isolé. C'est pourquoi on travaille de préférence dans l'ordre 1 en lumière blanche.

**4. Critère de résolution.** On sépare deux raies de longueurs d'onde $\lambda$ et $\lambda+\Delta\lambda$ si le pouvoir de résolution $pN$ est au moins égal à $\frac\lambda{\Delta\lambda}$. Pour le doublet du sodium :
$$\frac\lambda{\Delta\lambda}=\frac{589{,}3}{0{,}6}\approx980.$$

**4. Conclusion.** Dans l'ordre 1, avec $N=2000$ traits éclairés : $pN=2000>980$. Le doublet est **résolu**. Avec seulement 500 traits éclairés (faisceau étroit), il faudrait passer à l'ordre 2 ($pN=1000$, juste suffisant). Le pouvoir de résolution est lié à la finesse des pics, dont la largeur angulaire est proportionnelle à $\frac1N$ : il faut éclairer beaucoup de traits.
"""
