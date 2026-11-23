D = {}

D['p-q-1'] = r"""
**1. Analogie avec le cas rectiligne.** Pour une particule libre sur une droite, d'abscisse $s$, l'équation de Schrödinger stationnaire s'écrit $-\frac{\hbar^2}{2m}\frac{\mathrm d^2\psi}{\mathrm ds^2}=E\psi$. Sur le cercle, l'abscisse curviligne est $s=R\theta$, donc $\frac{\mathrm d}{\mathrm ds}=\frac1R\frac{\mathrm d}{\mathrm d\theta}$ et
$$-\frac{\hbar^2}{2mR^2}\frac{\mathrm d^2\psi}{\mathrm d\theta^2}=E\psi.$$
On retrouve aussi cette équation à partir du laplacien en coordonnées cylindriques à $r=R$ fixé, sans dépendance en $z$. Le facteur $mR^2$ est le moment d'inertie $J$ : l'énergie cinétique classique vaut $\frac{L_z^2}{2J}$.

**2. Condition aux limites.** $\theta$ et $\theta+2\pi$ repèrent le même point physique, et la fonction d'onde doit être univoque (une seule amplitude de probabilité en chaque point) :
$$\psi(\theta+2\pi)=\psi(\theta)\quad\text{pour tout }\theta,$$
ce qui implique aussi la périodicité de $\psi'$ (continuité de la dérivée en tout point du cercle).

**3. Signe de $E$.** On écrit l'équation sous la forme $\psi''=-\frac{2mR^2E}{\hbar^2}\psi$.
- Si $E<0$ : $\psi''=K^2\psi$ avec $K>0$, d'où $\psi=Ae^{K\theta}+Be^{-K\theta}$. La périodicité impose $A=B=0$, car une combinaison non nulle de ces exponentielles réelles n'est pas $2\pi$-périodique.
- Si $E=0$ : $\psi=A+B\theta$, périodique si et seulement si $B=0$ : $\psi$ est constante, ce qui est admissible.
- Si $E>0$ : on pose $E=\frac{\hbar^2k^2}{2mR^2}$ avec $k>0$, d'où $\psi=Ae^{ik\theta}+Be^{-ik\theta}$.

**3. Quantification.** La périodicité de chacune des exponentielles $e^{\pm ik\theta}$ (elles sont linéairement indépendantes) impose $e^{2i\pi k}=1$, soit $k\in\mathbb N^*$. Avec le cas $E=0$ ($k=0$), les états stationnaires sont les $e^{in\theta}$, $n\in\mathbb Z$.

**3. Normalisation.** La densité de probabilité est linéique, par unité de longueur d'arc : $\int_0^{2\pi}|\psi|^2R\,\mathrm d\theta=1$. Pour $\psi_n=Ce^{in\theta}$, on obtient $2\pi R|C|^2=1$.

**3. Résultats.**
$$\psi_n(\theta)=\frac1{\sqrt{2\pi R}}e^{in\theta},\qquad E_n=\frac{n^2\hbar^2}{2mR^2},\qquad n\in\mathbb Z.$$

**3. Commentaires.**
- Les niveaux sont quantifiés. Ils sont deux fois dégénérés pour $n\neq0$ ($\pm n$ correspond aux deux sens de rotation), et l'état fondamental $n=0$ est non dégénéré, d'énergie nulle.
- $\psi_n$ est état propre du moment cinétique, $\hat L_z=-i\hbar\frac{\partial}{\partial\theta}$, de valeur propre $n\hbar$ : le moment cinétique est quantifié, comme dans le modèle de Bohr.
- La densité $|\psi_n|^2=\frac1{2\pi R}$ est uniforme sur le cercle. Ce modèle s'applique aux électrons $\pi$ des molécules cycliques, comme le benzène.
"""

D['p-q-2'] = r"""
**1. Équation de Schrödinger.** Pour $x\le0$, $V=+\infty$ : la particule ne peut pas s'y trouver, $\varphi=0$. Pour $x>0$ :
$$-\frac{\hbar^2}{2m}\varphi''(x)-\frac\lambda x\varphi(x)=E\varphi(x),$$
avec la condition de raccordement $\varphi(0)=0$ (continuité de $\varphi$ à la paroi infinie).

**2. Dérivées de la fonction d'essai.** $\varphi=Cxe^{-kx}$ vérifie $\varphi(0)=0$.
$$\varphi'=C(1-kx)e^{-kx},\qquad\varphi''=C\big[-k-k(1-kx)\big]e^{-kx}=C(k^2x-2k)e^{-kx}.$$

**2. Report.** En divisant l'équation par $Ce^{-kx}$ :
$$-\frac{\hbar^2}{2m}(k^2x-2k)-\lambda=Ex\iff\Big(-\frac{\hbar^2k^2}{2m}-E\Big)x+\Big(\frac{\hbar^2k}m-\lambda\Big)=0\quad\forall x>0.$$
Un polynôme du premier degré nul sur $]0,+\infty[$ a des coefficients nuls :
$$E=-\frac{\hbar^2k^2}{2m},\qquad k=\frac{m\lambda}{\hbar^2},\qquad\text{donc}\qquad E=-\frac{m\lambda^2}{2\hbar^2}.$$
On a bien $k>0$ (si $\lambda>0$), ce qui assure la normalisabilité.

**3. Allure.** $V(x)=-\frac\lambda x$ tend vers $-\infty$ en $0^+$ et vers $0^-$ en $+\infty$ ; il est infini pour $x\le0$. $E<0$ est une droite horizontale qui coupe la courbe de $V$ en $x_c=\frac\lambda{|E|}=\frac{2\hbar^2}{m\lambda}=\frac2k$. C'est un **état lié** : classiquement, la particule serait confinée dans $]0,x_c]$ ; quantiquement, $\varphi$ déborde de façon évanescente au-delà de $x_c$. Analogie : avec $\lambda=\frac{e^2}{4\pi\varepsilon_0}$, on retrouve la partie radiale ($u=r\psi$) de l'état fondamental de l'atome d'hydrogène, avec $E=-13{,}6$ eV et $\frac1k=a_0$, le rayon de Bohr.

**4. Normalisation.** Avec la formule donnée ($n=2$, $\alpha=2k$) :
$$1=\int_0^{+\infty}C^2x^2e^{-2kx}\,\mathrm dx=C^2\frac{2!}{(2k)^3}=\frac{C^2}{4k^3}\quad\Longrightarrow\quad C=2k^{3/2}.$$

**5. Position moyenne.** Avec $n=3$ et $\alpha=2k$ :
$$\langle x\rangle=\int_0^{+\infty}x|\varphi|^2\,\mathrm dx=4k^3\int_0^{+\infty}x^3e^{-2kx}\,\mathrm dx=4k^3\cdot\frac{3!}{(2k)^4}=\frac{24k^3}{16k^4}=\frac3{2k}=\frac{3\hbar^2}{2m\lambda}.$$
Comparaison : $|\varphi|^2\propto x^2e^{-2kx}$ est maximale en $x=\frac1k$, et $\langle x\rangle=\frac{1{,}5}k$ est plus grand, car la distribution est dissymétrique (queue vers les grands $x$). Les deux sont inférieurs au point de rebroussement classique $\frac2k$.
"""

D['p-q-3'] = r"""
**1. Dimension de $A$.** $|\psi|^2\,\mathrm dx$ est une probabilité, sans dimension : $|\psi|^2$ s'exprime en $\mathrm m^{-1}$. L'exponentielle est sans dimension, donc $[A]=\mathrm m^{-1/2}$.

**1. Dimension de $\omega_0$.** L'argument $\frac{\omega_0}2t$ de l'exponentielle est sans dimension, donc $[\omega_0]=\mathrm s^{-1}$ : c'est une pulsation. Vérification : $\frac{m\omega_0x^2}\hbar$ a pour unité $\frac{\mathrm{kg\,s^{-1}\,m^2}}{\mathrm{J\,s}}=\frac{\mathrm{kg\,m^2\,s^{-1}}}{\mathrm{kg\,m^2\,s^{-1}}}$, sans dimension. ✓

**2. Normalisation.** On pose $\alpha=\frac{m\omega_0}\hbar$. Alors $|\psi|^2=|A|^2e^{-\alpha x^2}$ (le facteur de phase temporel a pour module 1), et
$$\int_{-\infty}^{+\infty}|\psi|^2\,\mathrm dx=|A|^2\sqrt{\frac\pi\alpha}=1\quad\Longrightarrow\quad A=\Big(\frac{m\omega_0}{\pi\hbar}\Big)^{1/4}e^{i\varphi_0},$$
où la phase $\varphi_0$ est arbitraire (sans effet physique).

**3. Énergie.** $\psi$ est de la forme $\phi(x)e^{-iEt/\hbar}$ : c'est un état stationnaire. Par identification, $\frac E\hbar=\frac{\omega_0}2$, donc
$$E=\frac12\hbar\omega_0.$$

**4. Potentiel.** $\phi(x)=Ae^{-\alpha x^2/2}$ a pour dérivées $\phi'=-\alpha x\phi$ et $\phi''=-\alpha\phi+\alpha^2x^2\phi=(\alpha^2x^2-\alpha)\phi$. L'équation stationnaire $-\frac{\hbar^2}{2m}\phi''+V\phi=E\phi$ donne
$$V(x)=E+\frac{\hbar^2}{2m}\frac{\phi''}\phi=\frac{\hbar\omega_0}2+\frac{\hbar^2\alpha^2}{2m}x^2-\frac{\hbar^2\alpha}{2m}.$$
Or $\frac{\hbar^2\alpha}{2m}=\frac{\hbar\omega_0}2$ et $\frac{\hbar^2\alpha^2}{2m}=\frac{m\omega_0^2}2$, donc
$$V(x)=\frac12m\omega_0^2x^2.$$
C'est le potentiel de l'**oscillateur harmonique**, et $\psi$ en est l'état fondamental.

**5. Position moyenne.** $\langle x\rangle=\int x|\psi|^2\,\mathrm dx$. L'intégrande est impaire, car $|\psi|^2$ est paire, donc $\langle x\rangle=0$. La particule est en moyenne au fond du puits.

**6. Énergie potentielle moyenne.**
$$\langle x^2\rangle=|A|^2\int x^2e^{-\alpha x^2}\,\mathrm dx=\sqrt{\frac\alpha\pi}\cdot\sqrt{\frac\pi{4\alpha^3}}=\frac1{2\alpha}=\frac\hbar{2m\omega_0},$$
donc
$$\Big\langle\frac12m\omega_0^2x^2\Big\rangle=\frac12m\omega_0^2\cdot\frac\hbar{2m\omega_0}=\frac14\hbar\omega_0=\frac E2.$$
L'énergie potentielle moyenne est la moitié de l'énergie totale, donc l'énergie cinétique moyenne aussi vaut $\frac E2$ : c'est le théorème du viriel pour un potentiel quadratique. De plus, $\Delta x=\sqrt{\frac\hbar{2m\omega_0}}$ et $\Delta p=\sqrt{\frac{m\hbar\omega_0}2}$ donnent $\Delta x\Delta p=\frac\hbar2$ : l'état fondamental réalise l'égalité dans l'inégalité de Heisenberg.
"""

D['p-q-4'] = r"""
**1. Zone $x<0$.** $V=+\infty$ : la particule ne peut pas s'y trouver, donc $\varphi=0$.

**1. Zone $0\le x\le a$.** $V=0<E$ : l'équation $-\frac{\hbar^2}{2m}\varphi''=E\varphi$ s'écrit $\varphi''=-k^2\varphi$, d'où des solutions oscillantes $\varphi=A_1e^{ikx}+B_1e^{-ikx}$.

**1. Zone $x>a$.** $V=V_0>E$ : $\varphi''=\frac{2m(V_0-E)}{\hbar^2}\varphi=\frac1{\delta^2}\varphi$, d'où $\varphi=A_2e^{-x/\delta}+B_2e^{x/\delta}$. C'est une zone classiquement interdite, où l'onde est évanescente.

**2. Normalisabilité.** Un état lié doit vérifier $\int|\varphi|^2<\infty$. Le terme $B_2e^{x/\delta}$ diverge quand $x\to+\infty$, donc $B_2=0$.

**3. Raccordement en $x=0$.** $\varphi$ est continue. La dérivée n'est pas imposée à cause du saut infini de potentiel. Donc $A_1+B_1=0$, et sur $[0,a]$ :
$$\varphi=A_1(e^{ikx}-e^{-ikx})=A\sin(kx),\qquad A=2iA_1.$$

**3. Raccordement en $x=a$.** Le saut de potentiel est fini : $\varphi$ et $\varphi'$ sont continues.
$$A\sin(ka)=A_2e^{-a/\delta},\qquad Ak\cos(ka)=-\frac{A_2}\delta e^{-a/\delta}.$$

**4. Équation aux énergies.** En divisant la seconde équation par la première (on a $\sin(ka)\neq0$, sinon $A_2=0$ et alors $\cos(ka)=0$, ce qui est impossible simultanément) :
$$k\cot(ka)=-\frac1\delta\iff\tan(ka)=-k\delta<0.$$

**4. Élimination de $\delta$.** Par définition, $k^2+\frac1{\delta^2}=\frac{2mE}{\hbar^2}+\frac{2m(V_0-E)}{\hbar^2}=k_0^2$. Avec $\sin^2=\frac{\tan^2}{1+\tan^2}$ :
$$\sin^2(ka)=\frac{k^2\delta^2}{1+k^2\delta^2}=\frac{k^2}{\frac1{\delta^2}+k^2}=\frac{k^2}{k_0^2}.$$
Donc
$$|\sin(ka)|=\frac k{k_0}\quad\text{avec}\quad\tan(ka)<0.$$

**5. Résolution graphique.** On pose $X=ka>0$. On cherche les intersections de la courbe $|\sin X|$ avec la droite $X\mapsto\frac X{k_0a}$ (de pente $\frac1{k_0a}$, issue de l'origine), restreintes aux arches où $\tan X<0$, c'est-à-dire $X\in\big]\big(n-\frac12\big)\pi,n\pi\big[$ pour $n\ge1$. Il faut aussi $k<k_0$, soit $X<k_0a$.

**5. Discussion.**
- **$k_0a<\frac\pi2$** : sur $\big]0,\frac\pi2\big]$, $\tan X>0$ (zone exclue). Pour $X>\frac\pi2$, la droite vaut $\frac X{k_0a}>1\ge|\sin X|$ : il n'y a **aucune solution**, donc **aucun état lié**. Le puits est trop étroit ou trop peu profond ; on peut le traduire par $V_0<\frac{\pi^2\hbar^2}{8ma^2}$.
- **$k_0a>\frac\pi2$** : la droite coupe $|\sin X|$ sur la première arche décroissante $\big]\frac\pi2,\pi\big[$, puis sur les suivantes tant que $\frac X{k_0a}<1$. Le nombre d'états liés est **fini**, environ $\frac{k_0a}\pi+\frac12$ (partie entière), et les énergies sont quantifiées.
- **$k_0a\gg\frac\pi2$** : la droite est presque horizontale et proche de 0, donc les premières solutions vérifient $\sin X\approx0$ avec $X$ juste en dessous de $n\pi$. On obtient $k\approx\frac{n\pi}a$ et
$$E_n\approx\frac{n^2\pi^2\hbar^2}{2ma^2},$$
les niveaux du **puits infini** de largeur $a$. Physiquement, $\delta\to0$ : l'onde ne pénètre plus dans la barrière.

**Remarque.** Contrairement au puits fini symétrique, qui a toujours au moins un état lié, la paroi infinie impose ici $\varphi(0)=0$. C'est comme ne garder que les états impairs d'un puits symétrique de largeur $2a$.
"""

D['p-stat-1'] = r"""
**1. Hypothèses de la statistique de Boltzmann.**
- Les dipôles sont **indépendants** : on néglige leurs interactions mutuelles, et l'énergie totale est la somme des énergies individuelles.
- Ils sont **discernables** : localisés aux nœuds d'un réseau cristallin.
- Le système est en **équilibre thermique** avec un thermostat à la température $T$.

Alors la probabilité qu'un dipôle soit dans un état d'énergie $\varepsilon$ est proportionnelle au facteur de Boltzmann $e^{-\varepsilon/k_BT}$.

**2. Énergies des deux états.** L'état $+$ ($\vec\mu=+\mu_0\vec u$, parallèle à $\vec B$) a pour énergie $\varepsilon_+=-\mu_0B_0=-\varepsilon_0$. L'état $-$ (antiparallèle) a pour énergie $\varepsilon_-=+\varepsilon_0$.

**2. Probabilités.** Avec $\beta=\frac1{k_BT}$ et la fonction de partition $z=e^{\beta\varepsilon_0}+e^{-\beta\varepsilon_0}=2\,\mathrm{ch}(\beta\varepsilon_0)$ :
$$p_+=\frac{e^{\beta\varepsilon_0}}{2\,\mathrm{ch}(\beta\varepsilon_0)},\qquad p_-=\frac{e^{-\beta\varepsilon_0}}{2\,\mathrm{ch}(\beta\varepsilon_0)}.$$
$p_+>p_-$ : l'état aligné sur le champ, d'énergie la plus basse, est le plus peuplé.

**3. Énergie moyenne.**
$$\langle\varepsilon\rangle=\varepsilon_+p_++\varepsilon_-p_-=-\varepsilon_0(p_+-p_-)=-\varepsilon_0\frac{e^{\beta\varepsilon_0}-e^{-\beta\varepsilon_0}}{e^{\beta\varepsilon_0}+e^{-\beta\varepsilon_0}}=-\varepsilon_0\,\mathrm{th}(\beta\varepsilon_0).$$
(On peut aussi l'obtenir par $\langle\varepsilon\rangle=-\frac{\partial\ln z}{\partial\beta}$.)

**3. Moment moyen.** Il est porté par $\vec u$ :
$$\langle\vec\mu\rangle=\mu_0(p_+-p_-)\vec u=\mu_0\,\mathrm{th}\Big(\frac{\mu_0B_0}{k_BT}\Big)\vec u.$$
On vérifie que $\langle\varepsilon\rangle=-\langle\vec\mu\rangle\cdot\vec B$. ✓

**4. Aimantation.** Les dipôles sont indépendants : les moments moyens s'additionnent. Pour un volume $V$ contenant $N$ dipôles, de densité $n=\frac NV$, l'aimantation (moment par unité de volume) vaut
$$\langle\vec{\mathcal M}\rangle=n\mu_0\,\mathrm{th}\Big(\frac{\mu_0B_0}{k_BT}\Big)\vec u.$$

**4. Haute température** ($k_BT\gg\mu_0B_0$). L'agitation thermique domine et $\mathrm{th}\,u\approx u$ : $\langle\mathcal M\rangle\approx\frac{n\mu_0^2B_0}{k_BT}$. L'aimantation est faible et proportionnelle à $\frac BT$.

**4. Basse température ou champ fort** ($k_BT\ll\mu_0B_0$). On a $\mathrm{th}\to1$ et $\langle\mathcal M\rangle\to n\mu_0$ : c'est la **saturation**, tous les dipôles sont alignés.

**5. Loi de Curie.** Dans le domaine de haute température, on obtient
$$\langle\vec{\mathcal M}\rangle=\frac{n\mu_0^2}{k_B}\cdot\frac{\vec B}T,\qquad C=\frac{n\mu_0^2}{k_B}.$$
La loi de Curie est vérifiée dans ce domaine (le cas usuel : pour $\mu_0\sim\mu_B\approx10^{-23}\ \mathrm{J\,T^{-1}}$ et $B=1$ T, $\frac{\mu_0B}{k_B}\approx0{,}7$ K). Elle cesse de l'être à très basse température, où apparaît la saturation.

**Remarque.** Pour des dipôles classiques orientables dans toutes les directions, on obtient la fonction de Langevin $\mathcal L(u)=\coth u-\frac1u\approx\frac u3$, d'où $C=\frac{n\mu_0^2}{3k_B}$. Le facteur $\frac13$ provient de la moyenne angulaire.
"""

D['p-stat-3'] = r"""
**1. Dénombrement.** Chacun des $N$ maillons peut être court ou long, indépendamment des autres : il y a $2^N$ états microscopiques.

**2.(a) Longueur.** Avec $k$ maillons courts et $N-k$ longs :
$$\mathcal L=k(\ell-a)+(N-k)(\ell+a)=N\ell+(N-2k)a.$$

**2.(b) Nombre de micro-états.** C'est le nombre de façons de choisir les $k$ maillons courts parmi $N$ :
$$\Omega(k)=\binom Nk=\frac{N!}{k!\,(N-k)!}.$$

**2.(c) Entropie.** $S(k)=k_B\ln\Omega(k)$. La formule de Stirling, $\ln n!\approx n\ln n-n$, s'applique ($N$, $k$, $N-k\gg1$) ; les termes en $-n$ se compensent, car $-N+k+(N-k)=0$ :
$$S(k)=k_B\big[N\ln N-k\ln k-(N-k)\ln(N-k)\big].$$

**2.(c) Équilibre à $f=0$.** Tous les micro-états ont même énergie : l'état d'équilibre maximise $S$ (on peut aussi dire $\Omega$).
$$\frac{\mathrm dS}{\mathrm dk}=k_B\big[-\ln k-1+\ln(N-k)+1\big]=k_B\ln\frac{N-k}k=0\iff k=\frac N2.$$
$S$ est concave en $k$, donc c'est bien un maximum. La longueur à vide vaut
$$\mathcal L_0=N\ell.$$
Autant de maillons sont courts que longs : la fibre a sa longueur « moyenne ».

**3. Force.** $\mathcal L=N\ell+(N-2k)a$ donne $\mathrm d\mathcal L=-2a\,\mathrm dk$. Avec $f\,\mathrm d\mathcal L=-T\,\mathrm dS$ :
$$f=-T\frac{\mathrm dS}{\mathrm d\mathcal L}=-T\frac{\mathrm dS}{\mathrm dk}\cdot\frac{\mathrm dk}{\mathrm d\mathcal L}=-T\cdot k_B\ln\frac{N-k}k\cdot\Big(-\frac1{2a}\Big)=\frac{k_BT}{2a}\ln\frac{N-k}k.$$
Si la fibre est étirée ($\mathcal L>\mathcal L_0$, donc $k<\frac N2$), alors $f>0$ : il faut tirer pour la maintenir étirée. Cette force est d'origine purement **entropique**, car l'énergie ne dépend pas de $k$.

**4. Expression en fonction de $\mathcal L$.** Posons $x=\frac{\mathcal L-\mathcal L_0}{Na}=\frac{N-2k}N\in[-1,1]$. Alors $k=\frac N2(1-x)$ et $N-k=\frac N2(1+x)$, donc $\frac{N-k}k=\frac{1+x}{1-x}$. Avec $\frac12\ln\frac{1+x}{1-x}=\mathrm{argth}\,x$ :
$$f=\frac{k_BT}a\,\mathrm{argth}\,x\iff x=\mathrm{th}\Big(\frac{af}{k_BT}\Big)\iff\mathcal L=\mathcal L_0+Na\,\mathrm{th}\Big(\frac{af}{k_BT}\Big).$$

**5. Température caractéristique.** Pour une force $f$ donnée, on pose $T_c=\frac{af}{k_B}$, de sorte que $\mathcal L=\mathcal L_0+Na\,\mathrm{th}\frac{T_c}T$.

**5. Cas $T\gg T_c$.** $\mathrm{th}\,u\approx u$, donc $\mathcal L-\mathcal L_0\approx\frac{Na^2}{k_BT}f$, soit
$$f=\kappa(\mathcal L-\mathcal L_0),\qquad\kappa=\frac{k_BT}{Na^2}.$$
C'est la **loi de Hooke**, avec une raideur proportionnelle à $T$ : élasticité entropique. Un élastique en caoutchouc tendu (à force constante) se **contracte** quand on le chauffe, contrairement à un métal.

**5. Cas $T\ll T_c$.** $\mathrm{th}\frac{T_c}T\to1$ et $\mathcal L\to\mathcal L_0+Na=N(\ell+a)$ : tous les maillons sont longs, et la fibre est totalement étirée. Une petite variation de $f$ ne change pas $\mathcal L$ : la fibre est **figée**, et il n'y a plus d'élasticité.
"""
