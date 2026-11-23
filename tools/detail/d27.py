D = {}

D['p-ondes-2'] = r"""
**Notation.** Pour éviter toute confusion, on note $\alpha_r$ le coefficient de rappel des suspentes (le $\alpha$ de l'énoncé) et $\beta(x,t)$ l'angle du câble avec l'horizontale.

**1. Système et hypothèses.** On étudie le tronçon $[x,x+\mathrm dx]$, de masse $\mu\,\mathrm dx$, avec de petits mouvements transversaux ($|\beta|\ll1$, $\beta\approx\tan\beta=\frac{\partial z}{\partial x}$). Le poids est compensé à l'équilibre par les suspentes ; on ne garde que les écarts à l'équilibre.

**1. Projection horizontale.** Les forces de tension sont $-T(x)\vec u(x)$ à gauche et $T(x+\mathrm dx)\vec u(x+\mathrm dx)$ à droite, où $\vec u$ est le vecteur tangent. Sur $\vec u_x$ (pas de mouvement horizontal) : $T(x+\mathrm dx)\cos\beta(x+\mathrm dx)-T(x)\cos\beta(x)=0$. À l'ordre 1 en $\beta$, $\cos\beta\approx1$, donc la tension est uniforme : $T=T_E$.

**1. Projection verticale.**
$$\mu\,\mathrm dx\,\frac{\partial^2z}{\partial t^2}=T_E\sin\beta(x+\mathrm dx)-T_E\sin\beta(x)-\alpha_r\,\mathrm dx\,z.$$
Avec $\sin\beta\approx\frac{\partial z}{\partial x}$, on a $T_E\Big[\frac{\partial z}{\partial x}(x+\mathrm dx)-\frac{\partial z}{\partial x}(x)\Big]=T_E\frac{\partial^2z}{\partial x^2}\mathrm dx$. Donc
$$\mu\frac{\partial^2z}{\partial t^2}=T_E\frac{\partial^2z}{\partial x^2}-\alpha_rz.$$

**1. Forme demandée.** En divisant par $T_E$ :
$$\frac{\partial^2z}{\partial x^2}-\frac1{c^2}\frac{\partial^2z}{\partial t^2}=\frac z{\delta^2},\qquad c=\sqrt{\frac{T_E}\mu},\qquad\delta=\sqrt{\frac{T_E}{\alpha_r}}.$$
C'est l'**équation de Klein-Gordon**. $c$ est une vitesse, et $\delta$ une longueur (car $\alpha_r$ est une force par unité de longueur et par mètre de déplacement, en $\mathrm{N\,m^{-2}}$).

**2. Relation de dispersion.** On cherche $z=z_0e^{i(\omega t-kx)}$. Alors $\frac{\partial^2z}{\partial x^2}=-k^2z$ et $\frac{\partial^2z}{\partial t^2}=-\omega^2z$, donc
$$-k^2+\frac{\omega^2}{c^2}=\frac1{\delta^2}\iff k^2=\frac{\omega^2-\omega_c^2}{c^2},\qquad\omega_c=\frac c\delta=\sqrt{\frac{\alpha_r}\mu}.$$

**2. Cas $\omega>\omega_c$ : propagation dispersive.** $k=\pm\frac1c\sqrt{\omega^2-\omega_c^2}$ est réel : l'onde se propage sans atténuation, mais $k$ n'est pas proportionnel à $\omega$, donc le milieu est **dispersif**.
- Vitesse de phase : $v_\varphi=\frac\omega k=\frac c{\sqrt{1-\omega_c^2/\omega^2}}>c$.
- Vitesse de groupe : en différentiant $c^2k^2=\omega^2-\omega_c^2$, on obtient $c^2k\,\mathrm dk=\omega\,\mathrm d\omega$, donc $v_g=\frac{\mathrm d\omega}{\mathrm dk}=\frac{c^2k}\omega=c\sqrt{1-\frac{\omega_c^2}{\omega^2}}<c$.

On remarque que $v_\varphi v_g=c^2$.

**2. Cas $\omega<\omega_c$ : onde évanescente.** $k^2<0$, donc $k=\pm\frac i\ell$ avec $\ell=\frac c{\sqrt{\omega_c^2-\omega^2}}$. La solution physique (bornée) est $z=z_0e^{-x/\ell}\cos(\omega t)$ : c'est une onde stationnaire d'amplitude décroissante, qui ne propage pas d'énergie en moyenne.

**2. Bilan.** $\omega_c$ est une **pulsation de coupure** : le câble se comporte comme un filtre passe-haut. Les suspentes, qui rappellent chaque point vers l'équilibre, empêchent la propagation des vibrations lentes.
"""

D['p-oem-2'] = r"""
**1. Relation de dispersion.** On injecte la forme complexe $\underline G=G_0e^{i(\omega t-\underline kx)}$, pour laquelle $\frac{\partial}{\partial x}\to-i\underline k$ et $\frac{\partial}{\partial t}\to i\omega$. On a donc $\frac{\partial^2\underline G}{\partial x^2}=-\underline k^2\underline G$, $\frac{\partial^2\underline G}{\partial t^2}=-\omega^2\underline G$ et $\frac{\partial\underline G}{\partial t}=i\omega\underline G$. L'équation devient
$$-\underline k^2+\frac{\omega^2}{c^2}-i\frac{\omega_0\omega}{c^2}=0\iff\underline k^2=\frac{\omega^2}{c^2}-i\frac{\omega_0\omega}{c^2}.$$

**2. Forme réduite.** On divise par $k_0^2=\frac{\omega^2}{c^2}$ :
$$\frac{\underline k^2}{k_0^2}=1-i\frac{\omega_0}\omega.$$

**3. Signe de $k'k''$.** Avec $\underline k=k'+ik''$ ($k',k''$ réels) :
$$\underline k^2=k'^2-k''^2+2ik'k''.$$
On identifie les parties réelles et imaginaires avec $k_0^2\big(1-i\frac{\omega_0}\omega\big)$ :
$$k'^2-k''^2=k_0^2,\qquad2k'k''=-k_0^2\frac{\omega_0}\omega<0.$$
Donc $k'k''<0$ : $k'$ et $k''$ sont de signes opposés.

**4. Forme réelle de l'onde.** $e^{-i\underline kx}=e^{-ik'x}e^{k''x}$, donc
$$G(x,t)=G_0\,e^{k''x}\cos(\omega t-k'x).$$
L'onde se propage dans le sens du signe de $k'$, avec une amplitude en $e^{k''x}$.

**4. Conclusion.** Pour une onde se propageant vers les $x$ croissants, $k'>0$, donc $k''<0$ et l'amplitude décroît en $e^{-|k''|x}$ dans le sens de propagation. Inversement, si $k'<0$, alors $k''>0$ et l'amplitude décroît vers les $x$ décroissants. Dans tous les cas, l'onde est **atténuée** : le terme en $\frac{\partial G}{\partial t}$ (dérivée d'ordre impair en temps) traduit une dissipation, comme un frottement fluide.

**4. Distance d'atténuation.** Elle vaut $\delta=\frac1{|k''|}$. Pour $\omega\gg\omega_0$ (faible amortissement), au premier ordre $\underline k\approx k_0\big(1-\frac{i\omega_0}{2\omega}\big)$, donc $k''\approx-\frac{k_0\omega_0}{2\omega}=-\frac{\omega_0}{2c}$ et
$$\delta\approx\frac{2c}{\omega_0}.$$
"""

D['p-oem-3'] = r"""
**1. Maxwell-Faraday.** Avec $\vec E=E_x(z,t)\vec u_x$ : $\overrightarrow{\mathrm{rot}}\,\vec E=\frac{\partial E_x}{\partial z}\vec u_y$. L'équation $\overrightarrow{\mathrm{rot}}\,\vec E=-\frac{\partial\vec B}{\partial t}$ donne, sur $\vec u_y$ :
$$\frac{\partial B}{\partial t}=-\frac{\partial E_x}{\partial z}.$$

**1. Dérivée spatiale.** Notons $u=\omega t-\frac z\delta$. Par la règle du produit (et $\frac{\partial}{\partial z}\cos u=\frac1\delta\sin u$) :
$$\frac{\partial E_x}{\partial z}=-\frac{E_0}\delta e^{-z/\delta}\cos u+\frac{E_0}\delta e^{-z/\delta}\sin u=-\frac{E_0}\delta e^{-z/\delta}(\cos u-\sin u).$$
Avec $\cos u-\sin u=\sqrt2\cos\big(u+\frac\pi4\big)$ :
$$\frac{\partial B}{\partial t}=\frac{\sqrt2E_0}\delta e^{-z/\delta}\cos\Big(\omega t-\frac z\delta+\frac\pi4\Big).$$

**1. Intégration en temps.** Sans composante statique (l'onde est purement sinusoïdale), on obtient
$$B(z,t)=\frac{\sqrt2E_0}{\omega\delta}e^{-z/\delta}\sin\Big(\omega t-\frac z\delta+\frac\pi4\Big).$$
$\vec B$ est déphasé de $\frac\pi4$ par rapport à $\vec E$, alors que dans le vide ils sont en phase. Le rapport des amplitudes vaut $\frac{\sqrt2}{\omega\delta}$ et non $\frac1c$. Ici, $\delta=\sqrt{\frac2{\mu_0\gamma\omega}}$ est l'épaisseur de peau.

**2. Puissance volumique Joule.** Avec la loi d'Ohm locale $\vec j=\gamma\vec E$, $p_J=\vec j\cdot\vec E=\gamma E^2$, donc
$$p_J(z,t)=\gamma E_0^2e^{-2z/\delta}\cos^2\Big(\omega t-\frac z\delta\Big).$$
Comme $\langle\cos^2\rangle=\frac12$ :
$$\langle p_J\rangle=\frac{\gamma E_0^2}2e^{-2z/\delta}.$$

**3. Intégration sur $V$.** Le volume élémentaire est $\mathrm d\tau=a^2\,\mathrm dz$ (le champ ne dépend pas de $x$, $y$) :
$$\langle P\rangle=\int_0^{+\infty}\frac{\gamma E_0^2}2e^{-2z/\delta}a^2\,\mathrm dz=\frac{\gamma E_0^2a^2}2\Big[-\frac\delta2e^{-2z/\delta}\Big]_0^{+\infty}=\frac{\gamma E_0^2a^2\delta}4.$$

**3. Vérification énergétique.** Le vecteur de Poynting en $z=0$ vaut $\Pi_z=\frac{E_xB}{\mu_0}=\frac{\sqrt2E_0^2}{\mu_0\omega\delta}\cos(\omega t)\sin\big(\omega t+\frac\pi4\big)$. Or $\langle\cos u\sin(u+\frac\pi4)\rangle=\frac12\sin\frac\pi4=\frac{\sqrt2}4$, donc
$$\langle\Pi_z(0)\rangle=\frac{E_0^2}{2\mu_0\omega\delta}=\frac{\gamma E_0^2\delta}4,$$
car $\frac1{\mu_0\omega}=\frac{\gamma\delta^2}2$. Le flux entrant, $a^2\langle\Pi_z(0)\rangle$, est égal à $\langle P\rangle$ : toute l'énergie qui entre est dissipée par effet Joule. ✓

**4. Interprétation.** L'onde ne pénètre que sur quelques $\delta$, et $\delta\propto\omega^{-1/2}$ est plus grand aux basses fréquences. Dans le visible, une surface métallique réfléchit l'essentiel du rayonnement (pouvoir réflecteur proche de 1), et seule une fraction infime pénètre. L'infrarouge, qui représente environ la moitié de la puissance solaire, est fortement absorbé par la peinture et dépose son énergie sous forme thermique. C'est donc lui qui chauffe principalement la carrosserie.
"""

D['p-oem-4'] = r"""
**1. Équations de Maxwell.** Les charges et courants de polarisation s'ajoutent aux charges et courants libres ($\rho$, $\vec j$) :
$$\mathrm{div}\,\vec E=\frac{\rho+\rho_{\mathrm{die}}}{\varepsilon_0},\qquad\mathrm{div}\,\vec B=0,\qquad\overrightarrow{\mathrm{rot}}\,\vec E=-\frac{\partial\vec B}{\partial t},\qquad\overrightarrow{\mathrm{rot}}\,\vec B=\mu_0\big(\vec j+\vec j_{\mathrm{die}}\big)+\mu_0\varepsilon_0\frac{\partial\vec E}{\partial t}.$$

**2. Conservation de la charge de polarisation.** Les dérivées par rapport à $t$ et à l'espace commutent, donc
$$\mathrm{div}\,\vec j_{\mathrm{die}}+\frac{\partial\rho_{\mathrm{die}}}{\partial t}=\mathrm{div}\frac{\partial\vec P}{\partial t}-\frac{\partial}{\partial t}\mathrm{div}\,\vec P=0.$$
Les charges liées se conservent d'elles-mêmes. On vérifie aussi la conservation globale : en prenant la divergence de Maxwell-Ampère ($\mathrm{div}\,\overrightarrow{\mathrm{rot}}=0$), puis en utilisant Maxwell-Gauss, on obtient $\mathrm{div}(\vec j+\vec j_{\mathrm{die}})+\frac{\partial(\rho+\rho_{\mathrm{die}})}{\partial t}=0$, et donc $\mathrm{div}\,\vec j+\frac{\partial\rho}{\partial t}=0$.

**3. Milieu neutre et isolant.** On a $\rho=0$ et $\vec j=\vec0$. Avec $\vec P=\varepsilon_0\chi\vec E$ ($\chi$ uniforme) :
- Maxwell-Gauss : $\varepsilon_0\,\mathrm{div}\,\vec E=-\mathrm{div}\,\vec P=-\varepsilon_0\chi\,\mathrm{div}\,\vec E$, donc $\varepsilon_0(1+\chi)\,\mathrm{div}\,\vec E=0$ ;
- Maxwell-Ampère : $\overrightarrow{\mathrm{rot}}\,\vec B=\mu_0\varepsilon_0\chi\frac{\partial\vec E}{\partial t}+\mu_0\varepsilon_0\frac{\partial\vec E}{\partial t}=\mu_0\varepsilon_0(1+\chi)\frac{\partial\vec E}{\partial t}$.

Ce sont les équations du vide, avec $\varepsilon_0$ remplacé par $\varepsilon_0\varepsilon_r$, où
$$\varepsilon_r=1+\chi.$$

**4. Équation de propagation.** On calcule $\overrightarrow{\mathrm{rot}}(\overrightarrow{\mathrm{rot}}\,\vec E)$ de deux façons.
- Formule d'analyse vectorielle : $\overrightarrow{\mathrm{rot}}\,\overrightarrow{\mathrm{rot}}\,\vec E=\overrightarrow{\mathrm{grad}}(\mathrm{div}\,\vec E)-\Delta\vec E=-\Delta\vec E$, car $\mathrm{div}\,\vec E=0$.
- Maxwell : $\overrightarrow{\mathrm{rot}}\,\overrightarrow{\mathrm{rot}}\,\vec E=-\frac{\partial}{\partial t}\overrightarrow{\mathrm{rot}}\,\vec B=-\mu_0\varepsilon_0\varepsilon_r\frac{\partial^2\vec E}{\partial t^2}$.

D'où l'équation de d'Alembert :
$$\Delta\vec E-\frac{\varepsilon_r}{c_0^2}\frac{\partial^2\vec E}{\partial t^2}=\vec0,\qquad c=\frac{c_0}{\sqrt{\varepsilon_r}}=\frac{c_0}n,\qquad n=\sqrt{1+\chi}.$$

**5. Développement de $\chi$.** Posons $\chi_0=\frac{n_0e^2}{\varepsilon_0\kappa}$ et $\omega_0^2=\frac\kappa{m_e}$, de sorte que $\frac{m_e\omega^2}\kappa=\frac{\omega^2}{\omega_0^2}$ et $\chi=\frac{\chi_0}{1-\omega^2/\omega_0^2}$. Pour $\omega\ll\omega_0$, avec $\frac1{1-\varepsilon}\approx1+\varepsilon$ :
$$\chi\approx\chi_0\Big(1+\frac{\omega^2}{\omega_0^2}\Big).$$

**5. Développement de $n$.** On pose $A=\sqrt{1+\chi_0}$ :
$$n=\sqrt{1+\chi_0+\chi_0\frac{\omega^2}{\omega_0^2}}=A\sqrt{1+\frac{\chi_0\omega^2}{A^2\omega_0^2}}\approx A\Big(1+\frac{\chi_0\omega^2}{2A^2\omega_0^2}\Big)=A+\frac{\chi_0\omega^2}{2A\omega_0^2}.$$

**5. Loi de Cauchy.** Avec $\omega=\frac{2\pi c_0}{\lambda_0}$ ($\lambda_0$ : longueur d'onde dans le vide), $\omega^2=\frac{4\pi^2c_0^2}{\lambda_0^2}$, donc
$$n\approx A+\frac B{\lambda_0^2},\qquad A=\sqrt{1+\chi_0},\qquad B=\frac{2\pi^2c_0^2\chi_0}{A\,\omega_0^2}>0.$$
C'est la loi empirique de Cauchy. Comme $B>0$, l'indice augmente quand $\lambda_0$ diminue (dispersion normale) : le bleu est plus dévié que le rouge par un prisme. L'hypothèse $\omega\ll\omega_0$ revient à supposer que les résonances du matériau sont dans l'UV, comme pour le verre.
"""

D['p-oem-5'] = r"""
**1. Justification du modèle.** On a négligé :
- **le poids**, $mg\sim10^{-29}$ N, devant $eE$ (même pour $E\sim1\ \mathrm{V\,m^{-1}}$, $eE\sim10^{-19}$ N) ;
- **la force magnétique** $e\vec v\wedge\vec B$ : pour une onde, $B\sim\frac Ec$, donc $\frac{evB}{eE}\sim\frac vc\ll1$ (électrons non relativistes) ;
- **le terme convectif** $(\vec v\cdot\overrightarrow{\mathrm{grad}})\vec v$ dans l'accélération : les déplacements des électrons sont petits devant la longueur d'onde.

Le terme $-\frac m\tau\vec v$ modélise les collisions (modèle de Drude). Le métal étant neutre ($\rho=0$), il n'y a pas de force de rappel électrostatique.

**2. Conductivité complexe.** En régime sinusoïdal, $\frac{\mathrm d}{\mathrm dt}\to i\omega$ :
$$i\omega m\underline{\vec v}=-e\underline{\vec E}-\frac m\tau\underline{\vec v}\iff\underline{\vec v}=-\frac{e\tau}{m(1+i\omega\tau)}\underline{\vec E}.$$
D'où $\underline{\vec j}=-n_0e\underline{\vec v}=\underline\gamma\,\underline{\vec E}$, avec
$$\underline\gamma=\frac{n_0e^2\tau}{m(1+i\omega\tau)}.$$

**2. Équation de propagation.** Comme $\rho=0$, $\mathrm{div}\,\vec E=0$. On calcule $\overrightarrow{\mathrm{rot}}\,\overrightarrow{\mathrm{rot}}\,\vec E$ de deux façons :
$$-\Delta\vec E=-\frac{\partial}{\partial t}\overrightarrow{\mathrm{rot}}\,\vec B=-\mu_0\frac{\partial\vec j}{\partial t}-\frac1{c^2}\frac{\partial^2\vec E}{\partial t^2}.$$

**2. Relation de dispersion.** Avec $\underline{\vec E}=\vec E_0e^{i(\omega t-\underline kx)}$ : $\Delta\to-\underline k^2$ et $\frac{\partial}{\partial t}\to i\omega$. Donc $-\underline k^2=i\omega\mu_0\underline\gamma-\frac{\omega^2}{c^2}$, soit
$$\underline k^2=\frac{\omega^2}{c^2}-i\mu_0\omega\underline\gamma.$$

**3. Indice complexe.** Par définition, $\underline n=\frac{\underline kc}\omega$. Avec $\mu_0c^2=\frac1{\varepsilon_0}$ :
$$\underline n^2=1-\frac{i\underline\gamma}{\varepsilon_0\omega}=1-\frac{i\,n_0e^2\tau}{\varepsilon_0m\,\omega(1+i\omega\tau)}.$$
On pose $\omega_p^2=\frac{n_0e^2}{\varepsilon_0m}$ (pulsation plasma) et on utilise $1+i\omega\tau=i(\omega\tau-i)$ :
$$\underline n^2=1-\frac{\omega_p^2\tau}{\omega(\omega\tau-i)}.$$

**4. Cas $\omega\tau\gg1$.** On a $\omega\tau-i\approx\omega\tau$ : les collisions sont négligeables, et
$$\underline n^2\approx1-\frac{\omega_p^2}{\omega^2}\quad(\text{réel}).$$

**4. Ordre de grandeur.**
$$\omega_p^2=\frac{n_0e^2}{\varepsilon_0m}\approx\frac{10^{29}\times(10^{-19})^2}{10^{-11}\times10^{-30}}=\frac{10^{-9}}{10^{-41}}=10^{32}\ \mathrm{s^{-2}},\qquad\omega_p\approx10^{16}\ \mathrm{rad\,s^{-1}}.$$
La longueur d'onde associée est $\lambda_p=\frac{2\pi c}{\omega_p}\approx\frac{6\times3\times10^8}{10^{16}}\approx2\times10^{-7}$ m $=0{,}2\ \mu$m : c'est le domaine ultraviolet. ($\tau\sim10^{-14}$ s, donc $\omega\tau\gg1$ est bien vérifié au voisinage de $\omega_p$.)

**4. Discussion.**
- **$\omega<\omega_p$** (radio, IR, visible) : $\underline n^2<0$, donc $\underline n$ et $\underline k$ sont imaginaires purs. L'onde est évanescente (amplitude en $e^{-x/\delta}$), ne transporte pas d'énergie en moyenne dans le métal, et est réfléchie : c'est l'éclat métallique.
- **$\omega>\omega_p$** (UV lointain) : $\underline n$ est réel, compris entre 0 et 1, et l'onde se propage sans atténuation.

Le métal devient **transparent dans l'UV**, pour $\lambda<\lambda_p\approx0{,}2\ \mu$m : c'est la transparence UV des métaux alcalins, observée expérimentalement.
"""
