# Physique — niveau Mines-Centrale (et deux exercices X-ENS)
from newlib import ex
P = 'Physique'

ex('n-p2-ailette', P, 'Diffusion thermique', 2, 'Ailette de refroidissement', 25, r"""
Une tige cylindrique en aluminium, de rayon $a$ et de grande longueur, est fixée par son extrémité $x=0$ à une paroi maintenue à $T_0$. Elle est entourée d'air à $T_e$. Sa surface latérale échange avec l'air le flux surfacique $h(T-T_e)$ (loi de Newton). On suppose le régime permanent et la température uniforme sur une section droite : $T(x)$.

On donne : $\lambda=200\ \mathrm{W\,m^{-1}\,K^{-1}}$, $a=2{,}0\ \mathrm{mm}$, $h=20\ \mathrm{W\,m^{-2}\,K^{-1}}$, $T_0-T_e=50\ \mathrm K$.

1. Par un bilan d'énergie sur une tranche $[x,x+\mathrm dx]$, établir l'équation $\dfrac{\mathrm d^2\theta}{\mathrm dx^2}=\dfrac{\theta}{\delta^2}$ avec $\theta=T-T_e$. Exprimer et calculer $\delta$.
2. Résoudre pour une tige très longue devant $\delta$.
3. Calculer le flux $\Phi$ évacué par l'ailette. Par quel facteur l'ailette multiplie-t-elle le flux évacué par la surface $\pi a^2$ de paroi qu'elle occupe ?
""",
r"Bilan sur la tranche : flux conductif entrant en $x$, sortant en $x+\mathrm dx$, et flux latéral $h\,2\pi a\,\mathrm dx\,\theta$ ; loi de Fourier $j=-\lambda\,\mathrm dT/\mathrm dx$.",
r"$\pi a^2\lambda\theta''=2\pi ah\theta$, d'où $\delta=\sqrt{\lambda a/(2h)}$ ; la solution bornée est $\theta=\theta_0e^{-x/\delta}$.",
r"Le flux évacué est celui qui entre dans la tige en $x=0$ : $\Phi=-\lambda\pi a^2\theta'(0)$ ; sans ailette, $\Phi_0=h\pi a^2\theta_0$.",
r"""
**1.** En régime permanent, pour la tranche : $\Phi(x)-\Phi(x+\mathrm dx)-h\,2\pi a\,\mathrm dx\,\theta=0$ avec $\Phi=-\lambda\pi a^2\theta'$. D'où $\lambda\pi a^2\theta''=2\pi ah\theta$, soit
$$\theta''=\frac\theta{\delta^2},\qquad\delta=\sqrt{\frac{\lambda a}{2h}}=\sqrt{\frac{200\times2\times10^{-3}}{40}}=0{,}10\ \mathrm m.$$

**2.** $\theta=Ae^{-x/\delta}+Be^{x/\delta}$ ; la température reste bornée, donc $B=0$, et $\theta(0)=\theta_0$ : $\theta(x)=\theta_0e^{-x/\delta}$. Au-delà de quelques $\delta$, la tige est à la température de l'air : une ailette plus longue que $3\delta\approx30$ cm ne sert à rien.

**3.** $\Phi=-\lambda\pi a^2\theta'(0)=\dfrac{\lambda\pi a^2\theta_0}\delta=\pi\theta_0\sqrt{2h\lambda a^3}\approx200\times\pi\times4\times10^{-6}\times50/0{,}1\approx1{,}3\ \mathrm W$. Sans ailette, la même surface évacuerait $\Phi_0=h\pi a^2\theta_0\approx1{,}3\times10^{-2}$ W. Le rapport $\dfrac\Phi{\Phi_0}=\dfrac\lambda{h\delta}=100$ : l'ailette offre une grande surface d'échange tout en conduisant bien la chaleur.
""", r"$\delta=\sqrt{\lambda a/(2h)}=10$ cm ; $\theta=\theta_0e^{-x/\delta}$ ; $\Phi\approx1{,}3$ W, 100 fois plus que sans ailette.")

ex('n-p2-isolant', P, 'Diffusion thermique', 2, 'Rayon critique d’isolation d’un fil', 20, r"""
Un fil électrique de rayon $r_1$, à la température $T_1$, est entouré d'une gaine isolante de conductivité $\lambda$, de rayon extérieur $r_2$. La surface extérieure échange avec l'air ambiant ($T_e$) selon la loi de Newton, de coefficient $h$. On se place en régime permanent.

On donne : $\lambda=0{,}20\ \mathrm{W\,m^{-1}\,K^{-1}}$ (PVC), $h=10\ \mathrm{W\,m^{-2}\,K^{-1}}$, $r_1=1{,}0\ \mathrm{mm}$.

1. Montrer que le flux thermique $\Phi$ à travers un cylindre de rayon $r$ est indépendant de $r$ et établir la résistance thermique de la gaine, pour une longueur $L$.
2. Exprimer la résistance thermique totale entre le fil et l'air.
3. Montrer que le flux perdu est maximal pour un rayon $r_2=r_c$ à exprimer et calculer. Commenter ce résultat surprenant pour l'isolation d'un fil fin.
""",
r"Sans source, en régime permanent, le flux à travers tout cylindre coaxial est le même ; loi de Fourier : $\Phi=-\lambda\,2\pi rL\,\dfrac{\mathrm dT}{\mathrm dr}$.",
r"$R_{\text{gaine}}=\dfrac{\ln(r_2/r_1)}{2\pi\lambda L}$ ; résistance de convection $R_h=\dfrac1{2\pi r_2Lh}$, en série.",
r"Étudie $R(r_2)=\dfrac1{2\pi L}\left(\dfrac{\ln(r_2/r_1)}\lambda+\dfrac1{hr_2}\right)$ : sa dérivée s'annule en $r_2=\lambda/h$.",
r"""
**1.** Bilan sur la couronne $[r,r+\mathrm dr]$ en régime permanent sans source : $\Phi(r)=\Phi(r+\mathrm dr)$. Avec $\Phi=-\lambda\,2\pi rL\,T'(r)$ constant, on intègre : $T_1-T_2=\dfrac{\Phi}{2\pi\lambda L}\ln\dfrac{r_2}{r_1}$, d'où $R_{\text{gaine}}=\dfrac{\ln(r_2/r_1)}{2\pi\lambda L}$.

**2.** Convection en surface : $\Phi=h\,2\pi r_2L(T_2-T_e)$, soit $R_h=\dfrac1{2\pi r_2hL}$. Les résistances sont en série :
$$R=\frac1{2\pi L}\left(\frac{\ln(r_2/r_1)}\lambda+\frac1{hr_2}\right).$$

**3.** $\dfrac{\mathrm dR}{\mathrm dr_2}=\dfrac1{2\pi L}\left(\dfrac1{\lambda r_2}-\dfrac1{hr_2^2}\right)$ s'annule en $r_c=\lambda/h=2{,}0\ \mathrm{cm}$, où $R$ est minimale : le flux perdu $(T_1-T_e)/R$ est maximal. Tant que $r_2<r_c$, épaissir la gaine **augmente** les pertes : l'augmentation de la surface d'échange l'emporte sur la résistance de conduction. C'est favorable pour un câble électrique, que la gaine aide à refroidir. Pour isoler un tuyau, il faut au contraire $r_1>r_c$ ou une couche très épaisse.
""", r"$R=\frac1{2\pi L}\left(\frac{\ln(r_2/r_1)}\lambda+\frac1{hr_2}\right)$ ; pertes maximales pour $r_2=\lambda/h=2$ cm.")

ex('n-p2-peau', P, 'Équations de Maxwell', 2, 'Effet de peau dans le cuivre', 25, r"""
Un conducteur ohmique de conductivité $\gamma$ occupe le demi-espace $z>0$. On étudie, dans l'approximation des régimes quasi stationnaires (courant de déplacement négligé), un champ $\vec E=E(z,t)\vec u_x$ imposé à la surface : $E(0,t)=E_0\cos\omega t$.

On donne : $\gamma=6{,}0\times10^7\ \mathrm{S\,m^{-1}}$ (cuivre), $\mu_0=4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$.

1. À partir des équations de Maxwell et de la loi d'Ohm, établir $\Delta\vec E=\mu_0\gamma\dfrac{\partial\vec E}{\partial t}$.
2. Chercher une solution sous la forme $\underline E=E_0e^{j(\omega t-\underline kz)}$. Établir la relation de dispersion et montrer que $E=E_0e^{-z/\delta}\cos(\omega t-z/\delta)$ ; exprimer $\delta$.
3. Calculer $\delta$ à $50\ \mathrm{Hz}$ et à $1\ \mathrm{MHz}$. Conséquences pratiques ?
4. Justifier l'approximation qui néglige le courant de déplacement.
""",
r"$\overrightarrow{\mathrm{rot}}\,\overrightarrow{\mathrm{rot}}\,\vec E=\overrightarrow{\mathrm{grad}}(\mathrm{div}\vec E)-\Delta\vec E$ avec $\mathrm{div}\vec E=0$ dans le conducteur, et $\overrightarrow{\mathrm{rot}}\vec B=\mu_0\gamma\vec E$.",
r"$\underline k^2=-j\mu_0\gamma\omega$, d'où $\underline k=\dfrac{1-j}\delta$ (racine choisie pour que l'onde s'atténue vers $z>0$), $\delta=\sqrt{\dfrac2{\mu_0\gamma\omega}}$.",
r"Compare $\varepsilon_0\omega$ à $\gamma$ : le rapport $\varepsilon_0\omega/\gamma$ est minuscule pour un métal.",
r"""
**1.** $\overrightarrow{\mathrm{rot}}\vec E=-\partial_t\vec B$ et, dans l'ARQS, $\overrightarrow{\mathrm{rot}}\vec B=\mu_0\vec j=\mu_0\gamma\vec E$. En prenant le rotationnel de la première, avec $\mathrm{div}\vec E=0$ (conducteur localement neutre) : $-\Delta\vec E=-\mu_0\gamma\partial_t\vec E$, soit une **équation de diffusion** $\Delta\vec E=\mu_0\gamma\,\partial_t\vec E$.

**2.** On obtient $-\underline k^2=j\mu_0\gamma\omega$, soit $\underline k^2=-j\mu_0\gamma\omega=\dfrac{2}{\delta^2}e^{-j\pi/2}$ avec $\delta=\sqrt{\dfrac2{\mu_0\gamma\omega}}$. Donc $\underline k=\pm\dfrac{1-j}\delta$. Le champ doit rester borné quand $z\to+\infty$ : $\underline k=\dfrac{1-j}\delta$, d'où
$$E(z,t)=E_0e^{-z/\delta}\cos\left(\omega t-\frac z\delta\right).$$
Le champ, et donc le courant, est confiné sur une épaisseur de l'ordre de $\delta$.

**3.** À $50$ Hz : $\delta=\sqrt{\dfrac2{4\pi\times10^{-7}\times6\times10^7\times314}}\approx9{,}2\ \mathrm{mm}$. À 1 MHz ($\delta\propto1/\sqrt f$) : $\delta\approx65\ \mathrm{\mu m}$. Les câbles très gros sont inutiles en BF au-delà de $\sim1$ cm de rayon ; en HF, le courant circule en surface, la résistance augmente. D'où les conducteurs creux, les fils divisés (fil de Litz) et l'argenture des conducteurs HF.

**4.** Le rapport du courant de déplacement au courant de conduction vaut $\varepsilon_0\omega/\gamma\approx10^{-19}\times f$ : il est négligeable jusqu'à des fréquences optiques.
""", r"$\Delta\vec E=\mu_0\gamma\partial_t\vec E$ ; $\delta=\sqrt{2/(\mu_0\gamma\omega)}$ ; 9,2 mm à 50 Hz, 65 µm à 1 MHz.")

ex('n-p2-bohr', P, 'Mécanique quantique', 2, 'Taille de l’atome d’hydrogène par Heisenberg', 15, r"""
On cherche à comprendre pourquoi l'électron de l'atome d'hydrogène ne « tombe » pas sur le proton. On modélise l'état fondamental par un électron localisé dans une région de taille $a$ autour du proton.

On donne : $\hbar=1{,}05\times10^{-34}\ \mathrm{J\,s}$, $m_e=9{,}11\times10^{-31}\ \mathrm{kg}$, $e=1{,}60\times10^{-19}\ \mathrm C$, $\dfrac1{4\pi\varepsilon_0}=9{,}0\times10^9\ \mathrm{SI}$.

1. À l'aide de l'inégalité de Heisenberg, estimer l'énergie cinétique minimale de l'électron en fonction de $a$.
2. En déduire une estimation de l'énergie totale $E(a)$. Pourquoi existe-t-il une taille d'équilibre ?
3. Minimiser $E(a)$ : exprimer et calculer $a_0$ et $E_{\min}$ en eV. Commenter.
""",
r"$\Delta x\sim a$ donne $p\sim\Delta p\sim\hbar/a$, donc $E_c\sim\dfrac{\hbar^2}{2m_ea^2}$.",
r"$E(a)=\dfrac{\hbar^2}{2m_ea^2}-\dfrac{e^2}{4\pi\varepsilon_0a}$ : un terme qui diverge en $a\to0$ et un terme attractif.",
r"$E'(a_0)=0$ donne $a_0=\dfrac{4\pi\varepsilon_0\hbar^2}{m_ee^2}$ ; reporte pour obtenir $E_{\min}=-\dfrac{e^2}{8\pi\varepsilon_0a_0}$.",
r"""
**1.** Confiné sur $\Delta x\sim a$, l'électron a $\Delta p\gtrsim\hbar/a$ ; comme $\langle p\rangle=0$, $\langle p^2\rangle\ge\Delta p^2$ et $E_c\gtrsim\dfrac{\hbar^2}{2m_ea^2}$.

**2.** $E(a)\approx\dfrac{\hbar^2}{2m_ea^2}-\dfrac{e^2}{4\pi\varepsilon_0a}$. Rapprocher l'électron du proton abaisse l'énergie potentielle en $1/a$, mais augmente le coût de confinement en $1/a^2$, qui l'emporte à courte distance : il existe un minimum.

**3.** $E'(a)=-\dfrac{\hbar^2}{m_ea^3}+\dfrac{e^2}{4\pi\varepsilon_0a^2}=0$ donne
$$a_0=\frac{4\pi\varepsilon_0\hbar^2}{m_ee^2}\approx\frac{(1{,}05\times10^{-34})^2}{9{,}11\times10^{-31}\times9\times10^9\times(1{,}6\times10^{-19})^2}\approx5{,}3\times10^{-11}\ \mathrm m.$$
Puis $E_{\min}=-\dfrac{e^2}{8\pi\varepsilon_0a_0}\approx-2{,}2\times10^{-18}\ \mathrm J\approx-13{,}6\ \mathrm{eV}$. On retrouve exactement le rayon de Bohr et l'énergie d'ionisation de l'hydrogène (la coïncidence exacte est un hasard de l'estimation, mais l'ordre de grandeur est robuste). La stabilité de la matière est un effet quantique.
""", r"$E(a)=\frac{\hbar^2}{2m_ea^2}-\frac{e^2}{4\pi\varepsilon_0a}$ ; $a_0\approx53$ pm, $E_{\min}\approx-13{,}6$ eV.")

ex('n-p2-marche', P, 'Mécanique quantique', 2, 'Marche de potentiel', 25, r"""
Un faisceau d'électrons d'énergie $E$, venant de $x<0$, rencontre une marche de potentiel : $V=0$ pour $x<0$ et $V=V_0>0$ pour $x>0$.

1. On suppose $E>V_0$. Écrire les solutions de l'équation de Schrödinger stationnaire dans chaque région (onde incidente d'amplitude 1, réfléchie $r$, transmise $t$). Écrire les conditions de raccordement en $x=0$ et en déduire $r$ et $t$.
2. Les coefficients de réflexion et de transmission en probabilité sont $R=|r|^2$ et $T=\dfrac{k_2}{k_1}|t|^2$. Vérifier $R+T=1$ et calculer $R$ pour $E=2V_0$. Comparer au comportement classique.
3. On suppose maintenant $E<V_0$. Montrer que la réflexion est totale mais que la probabilité de présence n'est pas nulle pour $x>0$. Calculer la profondeur de pénétration pour $V_0-E=1{,}0\ \mathrm{eV}$.

On donne : $\hbar=1{,}05\times10^{-34}\ \mathrm{J\,s}$, $m_e=9{,}11\times10^{-31}\ \mathrm{kg}$, $e=1{,}60\times10^{-19}\ \mathrm C$.
""",
r"$\varphi=e^{ik_1x}+re^{-ik_1x}$ pour $x<0$, $\varphi=te^{ik_2x}$ pour $x>0$, avec $k_1=\sqrt{2mE}/\hbar$, $k_2=\sqrt{2m(E-V_0)}/\hbar$. Continuité de $\varphi$ et de $\varphi'$.",
r"$1+r=t$ et $k_1(1-r)=k_2t$, d'où $r=\dfrac{k_1-k_2}{k_1+k_2}$ et $t=\dfrac{2k_1}{k_1+k_2}$.",
r"Pour $E<V_0$, $k_2=i/\delta$ avec $\delta=\hbar/\sqrt{2m(V_0-E)}$ ; alors $|r|=1$.",
r"""
**1.** Pour $x<0$ : $\varphi=e^{ik_1x}+re^{-ik_1x}$, $k_1=\dfrac{\sqrt{2mE}}\hbar$. Pour $x>0$ : $\varphi=te^{ik_2x}$, $k_2=\dfrac{\sqrt{2m(E-V_0)}}\hbar$ (pas d'onde venant de $+\infty$). Le potentiel est fini, donc $\varphi$ et $\varphi'$ sont continues : $1+r=t$ et $k_1(1-r)=k_2t$. D'où
$$r=\frac{k_1-k_2}{k_1+k_2},\qquad t=\frac{2k_1}{k_1+k_2}.$$

**2.** $R+T=\dfrac{(k_1-k_2)^2+4k_1k_2}{(k_1+k_2)^2}=1$ : conservation du courant de probabilité. Pour $E=2V_0$, $k_2=k_1/\sqrt2$ : $r=\dfrac{\sqrt2-1}{\sqrt2+1}\approx0{,}17$ et $R\approx0{,}029$. Classiquement, une particule d'énergie supérieure à la marche passe toujours ($R=0$) : la réflexion partielle est un effet ondulatoire, analogue à la réflexion de la lumière sur un dioptre.

**3.** Pour $E<V_0$ : $\varphi=te^{-x/\delta}$ avec $\delta=\dfrac\hbar{\sqrt{2m(V_0-E)}}$, ce qui revient à $k_2=i/\delta$. Alors $r=\dfrac{k_1-i/\delta}{k_1+i/\delta}$ est de module 1 : $R=1$, réflexion totale. Mais $|\varphi|^2=|t|^2e^{-2x/\delta}\neq0$ pour $x>0$ : l'électron pénètre dans la zone classiquement interdite (onde évanescente). Numériquement : $\delta=\dfrac{1{,}05\times10^{-34}}{\sqrt{2\times9{,}11\times10^{-31}\times1{,}6\times10^{-19}}}\approx0{,}20\ \mathrm{nm}$. Si la marche est remplacée par une barrière d'épaisseur comparable à $\delta$, un effet tunnel devient possible (microscope à effet tunnel).
""", r"$r=\frac{k_1-k_2}{k_1+k_2}$, $t=\frac{2k_1}{k_1+k_2}$ ; $R\approx0{,}029$ pour $E=2V_0$ ; $\delta\approx0{,}20$ nm.")

ex('n-p2-doublet', P, 'Optique ondulatoire', 2, 'Michelson et doublet du sodium', 25, r"""
Un interféromètre de Michelson réglé en lame d'air d'épaisseur $e$ est éclairé par une lampe à vapeur de sodium. On observe les anneaux à l'infini (au foyer d'une lentille).

1. Exprimer la différence de marche $\delta$ pour un rayon d'incidence $i$. Où sont localisées les franges ? Pourquoi a-t-on des anneaux ?
2. La lampe émet en réalité deux raies de même intensité, $\lambda_1=589{,}0\ \mathrm{nm}$ et $\lambda_2=589{,}6\ \mathrm{nm}$, incohérentes entre elles. Montrer que l'éclairement au centre s'écrit $\mathcal E=2\mathcal E_0\left[1+\cos\left(\dfrac{\pi\Delta\lambda\,\delta}{\lambda_m^2}\right)\cos\left(\dfrac{2\pi\delta}{\lambda_m}\right)\right]$ en approchant $\lambda_m^2\approx\lambda_1\lambda_2$.
3. On translate le miroir mobile depuis le contact optique. De quelle distance faut-il le déplacer entre deux brouillages successifs ? Combien d'anneaux défilent au centre entre deux brouillages ?
""",
r"Pour une lame d'air, les deux rayons émergents sont parallèles : $\delta=2e\cos i$ ; franges localisées à l'infini, d'égale inclinaison.",
r"Les deux raies étant incohérentes, on somme les éclairements : $\mathcal E_0\left[2+\cos\frac{2\pi\delta}{\lambda_1}+\cos\frac{2\pi\delta}{\lambda_2}\right]$, puis formule $\cos p+\cos q$.",
r"Brouillage quand le terme de contraste s'annule ; deux annulations successives correspondent à une variation de $\delta$ de $\lambda_m^2/\Delta\lambda$, avec $\delta=2e$ au centre.",
r"""
**1.** Les deux rayons issus d'un même rayon incident ressortent parallèles, séparés par une lame d'air d'épaisseur $e$ : $\delta=2e\cos i$. Les franges sont localisées à l'infini et ont même éclairement pour un même $i$ : par symétrie de révolution autour de l'axe, ce sont des **anneaux** (franges d'égale inclinaison).

**2.** Les raies sont incohérentes : les éclairements s'ajoutent.
$$\mathcal E=\mathcal E_0\left[2+\cos\frac{2\pi\delta}{\lambda_1}+\cos\frac{2\pi\delta}{\lambda_2}\right]=2\mathcal E_0\left[1+\cos\left(\pi\delta\Big(\frac1{\lambda_1}-\frac1{\lambda_2}\Big)\right)\cos\left(\pi\delta\Big(\frac1{\lambda_1}+\frac1{\lambda_2}\Big)\right)\right].$$
Avec $\dfrac1{\lambda_1}-\dfrac1{\lambda_2}=\dfrac{\Delta\lambda}{\lambda_1\lambda_2}\approx\dfrac{\Delta\lambda}{\lambda_m^2}$ et $\dfrac1{\lambda_1}+\dfrac1{\lambda_2}\approx\dfrac2{\lambda_m}$, on obtient la formule. Le premier cosinus, qui varie lentement, module le **contraste** $C=\left|\cos\frac{\pi\Delta\lambda\,\delta}{\lambda_m^2}\right|$.

**3.** Le contraste s'annule pour $\dfrac{\pi\Delta\lambda\,\delta}{\lambda_m^2}=\dfrac\pi2+p\pi$ : entre deux brouillages, $\Delta\delta=\dfrac{\lambda_m^2}{\Delta\lambda}$. Au centre, $\delta=2e$, donc $\Delta e=\dfrac{\lambda_m^2}{2\Delta\lambda}=\dfrac{(589{,}3\times10^{-9})^2}{2\times0{,}6\times10^{-9}}\approx0{,}29\ \mathrm{mm}$. Il défile alors $\dfrac{2\Delta e}{\lambda_m}=\dfrac{\lambda_m}{\Delta\lambda}\approx980$ anneaux. Inversement, la mesure de $\Delta e$ donne $\Delta\lambda$ avec précision.
""", r"$\delta=2e\cos i$ ; contraste $|\cos(\pi\Delta\lambda\,\delta/\lambda_m^2)|$ ; brouillages tous les $\Delta e=\lambda_m^2/(2\Delta\lambda)\approx0{,}29$ mm, ≈ 980 anneaux.")

ex('n-p2-reseau', P, 'Optique ondulatoire', 2, 'Réseau : recouvrement des ordres et résolution', 20, r"""
Un réseau plan par transmission comporte $n=500$ traits par millimètre. Il est éclairé sous incidence normale par de la lumière blanche ($400$ à $700\ \mathrm{nm}$).

1. Établir la relation donnant les directions $\theta_p$ des maxima principaux d'ordre $p$.
2. Quel est l'ordre maximal observable pour le rouge ($700$ nm) ? Pour le violet ($400$ nm) ?
3. Les spectres d'ordres 2 et 3 se recouvrent-ils ? Et ceux d'ordres 1 et 2 ?
4. On éclaire $N=2\,000$ traits par une lampe au sodium. Le pouvoir de résolution d'un réseau dans l'ordre $p$ vaut $pN$. Peut-on séparer le doublet ($589{,}0$ et $589{,}6$ nm) dans l'ordre 1 ?
""",
r"Deux traits voisins, distants de $a=1/n$, donnent une différence de marche $a\sin\theta$ sous incidence normale ; interférence constructive si elle vaut $p\lambda$.",
r"$|\sin\theta_p|\le1$ donne $|p|\le a/\lambda$, avec $a=2{,}0\ \mathrm{\mu m}$.",
r"Compare $\sin\theta$ pour le bord rouge d'un ordre et le bord violet de l'ordre suivant ; pour la résolution, compare $pN$ à $\lambda/\Delta\lambda$.",
r"""
**1.** Pas $a=1/n=2{,}0\ \mathrm{\mu m}$. Entre deux traits voisins, $\delta=a\sin\theta$ ; toutes les ondes diffractées sont en phase si $a\sin\theta_p=p\lambda$, $p\in\mathbb Z$.

**2.** Il faut $|p|\le a/\lambda$ : pour le rouge, $a/\lambda=2{,}86$, ordre maximal 2 ; pour le violet, $a/\lambda=5$, mais l'ordre 5 est à $\theta=90^\circ$ (rasant) : ordre 4 observable en pratique.

**3.** Ordre 2 : le rouge est à $\sin\theta=2\times0{,}7/2=0{,}70$ ; ordre 3 : le violet est à $\sin\theta=3\times0{,}4/2=0{,}60<0{,}70$ : les spectres d'ordres 2 et 3 **se recouvrent**. Ordres 1 et 2 : rouge d'ordre 1 à $0{,}35$, violet d'ordre 2 à $0{,}40$ : pas de recouvrement, le spectre d'ordre 1 est entièrement isolé.

**4.** Il faut $pN\ge\dfrac\lambda{\Delta\lambda}=\dfrac{589{,}3}{0{,}6}\approx980$. Dans l'ordre 1, $pN=2\,000>980$ : le doublet est séparé. (Avec seulement 500 traits éclairés, il faudrait passer à l'ordre 2.)
""", r"$a\sin\theta_p=p\lambda$ ; ordre max 2 (rouge) ; ordres 2 et 3 se recouvrent, pas 1 et 2 ; $pN=2000>980$ : doublet résolu.")

ex('n-p2-tige', P, 'Mécanique', 2, 'Anneau sur une tige en rotation', 25, r"""
Une tige rectiligne horizontale tourne autour d'un axe vertical $Oz$ fixe, à vitesse angulaire constante $\omega$, imposée par un moteur. Un anneau de masse $m$, assimilé à un point $M$, peut glisser sans frottement le long de la tige. À $t=0$, il est lâché sans vitesse relative à la distance $r_0$ de l'axe.

1. Dans le référentiel tournant lié à la tige, faire le bilan des forces. Établir l'équation du mouvement de $r(t)$ et la résoudre.
2. Déterminer la réaction de la tige. Quelle composante s'oppose à la force de Coriolis ?
3. La tige a pour longueur $L$. Calculer la durée au bout de laquelle l'anneau quitte la tige, pour $r_0=10\ \mathrm{cm}$, $L=1{,}0\ \mathrm m$ et $\omega=2{,}0\ \mathrm{rad\,s^{-1}}$.
4. Calculer l'énergie cinétique de l'anneau, dans le référentiel du laboratoire, quand il quitte la tige. D'où provient cette énergie ?
""",
r"Forces dans le référentiel tournant : poids, réaction (perpendiculaire à la tige, sans frottement), force d'inertie d'entraînement $m\omega^2r\vec u_r$, force de Coriolis $-2m\omega\vec u_z\wedge\dot r\vec u_r$.",
r"Projection sur la tige : $\ddot r=\omega^2r$, d'où $r=r_0\cosh\omega t$. Projection orthoradiale : $R_\theta=2m\omega\dot r$.",
r"Dans le laboratoire, $v^2=\dot r^2+r^2\omega^2$ ; le théorème de l'énergie cinétique fait intervenir la puissance de la réaction, non nulle.",
r"""
**1.** Dans le référentiel tournant (non galiléen) : poids $-mg\vec u_z$, réaction $\vec R=R_\theta\vec u_\theta+R_z\vec u_z$ (sans frottement, perpendiculaire à la tige), force d'entraînement $m\omega^2r\vec u_r$, force de Coriolis $-2m\omega\vec u_z\wedge\dot r\vec u_r=-2m\omega\dot r\vec u_\theta$. Sur $\vec u_r$ : $m\ddot r=m\omega^2r$. Avec $r(0)=r_0$, $\dot r(0)=0$ : $r(t)=r_0\cosh\omega t$.

**2.** Sur $\vec u_\theta$ : $R_\theta=2m\omega\dot r=2m\omega^2r_0\sinh\omega t$ ; sur $\vec u_z$ : $R_z=mg$. La composante $R_\theta$ compense la force de Coriolis : la tige « pousse » l'anneau pour l'entraîner en rotation.

**3.** L'anneau quitte la tige quand $\cosh\omega t=L/r_0=10$ : $t=\dfrac{\operatorname{argch}10}\omega=\dfrac{\ln(10+\sqrt{99})}{2{,}0}\approx1{,}5\ \mathrm s$.

**4.** Dans le laboratoire, $v^2=\dot r^2+r^2\omega^2=r_0^2\omega^2(\sinh^2+\cosh^2)$ ; en sortie, $\dot r=\omega\sqrt{L^2-r_0^2}$, donc $E_c=\tfrac12m\omega^2(2L^2-r_0^2)$. Elle provient du travail de la réaction $R_\theta$, dont la puissance $R_\theta\,r\omega$ est non nulle dans le laboratoire : c'est le moteur qui fournit l'énergie (couple $\Gamma=rR_\theta$). On vérifie : $\int R_\theta r\omega\,\mathrm dt=m\omega^2(L^2-r_0^2)=\Delta E_c$.
""", r"$r=r_0\cosh\omega t$ ; $R_\theta=2m\omega\dot r$ ; sortie à $t\approx1{,}5$ s ; $E_c=\frac12m\omega^2(2L^2-r_0^2)$, fournie par le moteur.")

ex('n-p2-resonance', P, 'Mécanique', 2, 'Résonance d’élongation et facteur de qualité', 25, r"""
Une masse $m$ accrochée à un ressort de raideur $k$ subit un frottement fluide $-h\dot x$ et une force excitatrice $F_0\cos\omega t$. On note $\omega_0=\sqrt{k/m}$ et $Q=\dfrac{m\omega_0}h$.

1. Établir l'amplitude complexe $\underline X$ en régime sinusoïdal forcé, puis son module $X(\omega)$.
2. Montrer qu'il y a résonance d'élongation si et seulement si $Q>1/\sqrt2$, à une pulsation $\omega_r$ à exprimer.
3. On étudie maintenant la vitesse. Montrer que la résonance de vitesse a toujours lieu en $\omega_0$ et que sa bande passante vaut $\Delta\omega=\omega_0/Q$.
4. Expérimentalement, on mesure une résonance de vitesse à $f_0=12{,}0\ \mathrm{Hz}$ et une bande passante de $0{,}40\ \mathrm{Hz}$. En déduire $Q$ et, pour $m=0{,}20\ \mathrm{kg}$, le coefficient $h$.
""",
r"En complexes : $(-m\omega^2+jh\omega+k)\underline X=F_0$.",
r"$X$ est maximal quand $D(\omega)=(\omega_0^2-\omega^2)^2+\left(\frac{\omega\omega_0}Q\right)^2$ est minimal ; étudie $D$ comme fonction de $u=\omega^2$.",
r"$\underline V=j\omega\underline X=\dfrac{F_0/h}{1+jQ\left(\frac\omega{\omega_0}-\frac{\omega_0}\omega\right)}$ : même forme qu'un passe-bande RLC.",
r"""
**1.** $\underline X=\dfrac{F_0/m}{\omega_0^2-\omega^2+j\omega\omega_0/Q}$, d'où $X(\omega)=\dfrac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2+\omega^2\omega_0^2/Q^2}}$.

**2.** Avec $u=\omega^2$ : $D(u)=(\omega_0^2-u)^2+u\omega_0^2/Q^2$, $D'(u)=-2(\omega_0^2-u)+\omega_0^2/Q^2$, nul en $u=\omega_0^2\left(1-\frac1{2Q^2}\right)$. Ce minimum est atteint pour $u>0$ si et seulement si $Q>1/\sqrt2$ : alors $\omega_r=\omega_0\sqrt{1-\frac1{2Q^2}}<\omega_0$. Sinon, $X$ décroît dès $\omega=0$ : pas de résonance.

**3.** $\underline V=j\omega\underline X=\dfrac{F_0/h}{1+jQ\left(\frac\omega{\omega_0}-\frac{\omega_0}\omega\right)}$ : module maximal $F_0/h$ en $\omega=\omega_0$, quel que soit $Q$. La bande passante à $-3$ dB vérifie $Q\left|x-\frac1x\right|=1$, d'où $\Delta\omega=\omega_0/Q$ (même calcul que pour le circuit RLC).

**4.** $Q=f_0/\Delta f=12{,}0/0{,}40=30$. Puis $h=\dfrac{m\omega_0}Q=\dfrac{0{,}20\times2\pi\times12{,}0}{30}\approx0{,}50\ \mathrm{kg\,s^{-1}}$. Comme $Q\gg1$, la résonance d'élongation est pratiquement à $\omega_0$.
""", r"$X=\frac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2+\omega^2\omega_0^2/Q^2}}$ ; résonance si $Q>1/\sqrt2$ en $\omega_0\sqrt{1-1/(2Q^2)}$ ; $Q=30$, $h\approx0{,}50$ kg/s.")

ex('n-p2-fourier', P, 'Électrocinétique', 2, 'Du créneau au triangle', 25, r"""
Un signal créneau $e(t)$ symétrique, d'amplitude $E$ (il vaut $+E$ sur une demi-période, $-E$ sur l'autre) et de fréquence $f=1{,}0\ \mathrm{kHz}$, est appliqué à l'entrée d'un filtre RC passe-bas (sortie aux bornes du condensateur, en sortie ouverte) de fréquence de coupure $f_c=50\ \mathrm{Hz}$.

On admet la décomposition $e(t)=\dfrac{4E}\pi\displaystyle\sum_{k\ge0}\dfrac{\sin\big((2k+1)\omega t\big)}{2k+1}$.

1. Comment se comporte le filtre pour toutes les composantes du créneau ? En déduire une relation approchée entre $s$ et $e$.
2. Quelle est la forme du signal de sortie ? Calculer son amplitude crête à crête par un raisonnement temporel.
3. Retrouver le résultat par l'analyse spectrale : comparer les amplitudes du fondamental et de l'harmonique 3 en sortie. Pourquoi le signal de sortie est-il « plus sinusoïdal » que l'entrée ?
""",
r"Toutes les fréquences présentes ($f$, $3f$, $5f$…) sont très supérieures à $f_c$ : $\underline H\approx\dfrac{1}{j\omega RC}$.",
r"$s\approx\dfrac1{RC}\int e\,\mathrm dt$ : pendant une demi-période, $s$ varie linéairement de $\dfrac{E}{RC}\cdot\dfrac T2$.",
r"L'harmonique de rang $n$ a une amplitude en $1/n$ en entrée, et le filtre la divise par $\sim n$ de plus : amplitude en $1/n^2$ en sortie.",
r"""
**1.** Le créneau ne contient que $f=1$ kHz et ses harmoniques impairs, tous $\gg f_c=50$ Hz. Pour eux, $\underline H=\dfrac1{1+jf/f_c}\approx\dfrac{f_c}{jf}=\dfrac1{jRC\omega}$ : le filtre est **intégrateur**, $s(t)\approx\dfrac1{RC}\int e\,\mathrm dt$ (à une constante près ; en régime permanent, $s$ est de moyenne nulle).

**2.** Sur une demi-période où $e=+E$, $s$ croît linéairement avec la pente $E/(RC)$ ; puis décroît avec la pente opposée : **signal triangulaire**. Amplitude crête à crête : $\Delta s=\dfrac E{RC}\cdot\dfrac T2=\dfrac{E\cdot2\pi f_c}{2f}=\pi\dfrac{f_c}fE\approx0{,}16\,E$.

**3.** Composante $n$ (impaire) : amplitude d'entrée $\dfrac{4E}{n\pi}$, gain $\approx\dfrac{f_c}{nf}$, donc en sortie $\dfrac{4Ef_c}{\pi n^2f}$. Le fondamental vaut $\dfrac{4f_c}{\pi f}E\approx0{,}064E$ et l'harmonique 3 est 9 fois plus faible. On retrouve la série du triangle, en $1/n^2$. Les harmoniques élevés, responsables des discontinuités du créneau, sont fortement atténués : le triangle est continu et sa série converge plus vite, il est plus proche de sa composante fondamentale.
""", r"Filtre intégrateur ; triangle d'amplitude crête à crête $\pi Ef_c/f\approx0{,}16E$ ; harmoniques en $1/n^2$.")

ex('n-p2-coax', P, 'Électrostatique', 2, 'Câble coaxial : capacité, inductance, impédance', 25, r"""
Un câble coaxial est formé d'une âme cylindrique de rayon $R_1$ et d'une gaine conductrice de rayon $R_2$, séparées par du polyéthylène de permittivité relative $\varepsilon_r$ (on remplacera $\varepsilon_0$ par $\varepsilon_0\varepsilon_r$) et de perméabilité $\mu_0$.

On donne : $R_1=0{,}50\ \mathrm{mm}$, $R_2=1{,}75\ \mathrm{mm}$, $\varepsilon_r=2{,}25$, $\varepsilon_0=8{,}85\times10^{-12}\ \mathrm{F\,m^{-1}}$, $\mu_0=4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$.

1. L'âme porte la charge linéique $\lambda$, la gaine $-\lambda$. Déterminer le champ électrique entre les conducteurs, la tension entre eux et la capacité linéique $\Gamma$.
2. L'âme est parcourue par un courant $I$ qui revient par la gaine. Déterminer le champ magnétique entre les conducteurs, l'énergie magnétique par unité de longueur et l'inductance linéique $\Lambda$.
3. Calculer $\Gamma$ et $\Lambda$. Calculer la vitesse $1/\sqrt{\Lambda\Gamma}$ des signaux et l'impédance caractéristique $Z_c=\sqrt{\Lambda/\Gamma}$.
""",
r"Symétries : $\vec E=E(r)\vec u_r$ ; théorème de Gauss sur un cylindre de rayon $r$ et de hauteur $h$.",
r"Ampère : $\vec B=\dfrac{\mu_0I}{2\pi r}\vec u_\theta$ entre les conducteurs, nul au-delà ; énergie $\int\frac{B^2}{2\mu_0}\mathrm d\tau=\frac12\Lambda I^2$.",
r"$\Gamma=\dfrac{2\pi\varepsilon_0\varepsilon_r}{\ln(R_2/R_1)}$, $\Lambda=\dfrac{\mu_0}{2\pi}\ln\dfrac{R_2}{R_1}$ ; le produit $\Lambda\Gamma=\mu_0\varepsilon_0\varepsilon_r$ ne dépend pas de la géométrie.",
r"""
**1.** Par symétrie (invariances par rotation et translation, plans de symétrie), $\vec E=E(r)\vec u_r$. Gauss : $E\,2\pi rh=\dfrac{\lambda h}{\varepsilon_0\varepsilon_r}$, donc $E=\dfrac\lambda{2\pi\varepsilon_0\varepsilon_rr}$. Tension : $U=\int_{R_1}^{R_2}E\,\mathrm dr=\dfrac\lambda{2\pi\varepsilon_0\varepsilon_r}\ln\dfrac{R_2}{R_1}$, d'où $\Gamma=\dfrac\lambda U=\dfrac{2\pi\varepsilon_0\varepsilon_r}{\ln(R_2/R_1)}$.

**2.** Ampère sur un cercle de rayon $r$ : $B=\dfrac{\mu_0I}{2\pi r}$ pour $R_1<r<R_2$, nul à l'extérieur (courant total enlacé nul). Énergie par unité de longueur : $\displaystyle\int_{R_1}^{R_2}\frac{B^2}{2\mu_0}2\pi r\,\mathrm dr=\frac{\mu_0I^2}{4\pi}\ln\frac{R_2}{R_1}=\frac12\Lambda I^2$, donc $\Lambda=\dfrac{\mu_0}{2\pi}\ln\dfrac{R_2}{R_1}$ (on néglige le champ dans l'âme).

**3.** $\ln3{,}5=1{,}25$ : $\Gamma=\dfrac{2\pi\times8{,}85\times10^{-12}\times2{,}25}{1{,}25}\approx100\ \mathrm{pF\,m^{-1}}$ et $\Lambda=2\times10^{-7}\times1{,}25\approx0{,}25\ \mathrm{\mu H\,m^{-1}}$. Vitesse : $\dfrac1{\sqrt{\Lambda\Gamma}}=\dfrac c{\sqrt{\varepsilon_r}}=2{,}0\times10^8\ \mathrm{m\,s^{-1}}$. Impédance : $Z_c=\sqrt{\Lambda/\Gamma}\approx50\ \Omega$ : c'est le câble standard des laboratoires.
""", r"$\Gamma=\frac{2\pi\varepsilon_0\varepsilon_r}{\ln(R_2/R_1)}\approx100$ pF/m ; $\Lambda=\frac{\mu_0}{2\pi}\ln\frac{R_2}{R_1}\approx0{,}25$ µH/m ; $v=2\times10^8$ m/s ; $Z_c\approx50\ \Omega$.")

ex('n-p2-serre', P, 'Rayonnement', 2, 'Modèle simple de l’effet de serre', 20, r"""
La Terre reçoit du Soleil un flux surfacique $\varphi_S=1\,361\ \mathrm{W\,m^{-2}}$ (constante solaire) et en réfléchit une fraction $A=0{,}30$ (albédo). On assimile sa surface à un corps noir à température uniforme $T_s$, en régime permanent.

On donne : $\sigma=5{,}67\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}$.

1. Sans atmosphère, écrire le bilan radiatif de la Terre et calculer $T_s$. Commenter (la température moyenne réelle est de $288\ \mathrm K$).
2. On ajoute une atmosphère modélisée par une couche mince, transparente au rayonnement solaire (visible) mais absorbant totalement l'infrarouge ; elle rayonne comme un corps noir à $T_a$, vers le haut et vers le bas. Écrire les bilans de la couche et du sol. En déduire $T_a$ et $T_s$.
3. Pourquoi le modèle surestime-t-il $T_s$ ?
""",
r"Puissance absorbée : $(1-A)\varphi_S\pi R^2$ ; puissance émise : $\sigma T_s^44\pi R^2$.",
r"Couche : elle absorbe $\sigma T_s^4$ et émet $2\sigma T_a^4$. Sol : il reçoit $\frac{(1-A)\varphi_S}4+\sigma T_a^4$ et émet $\sigma T_s^4$.",
r"Bilan global au sommet de l'atmosphère : $\sigma T_a^4=\frac{(1-A)\varphi_S}4$, d'où $T_a=255$ K, puis $T_s=2^{1/4}T_a$.",
r"""
**1.** La Terre intercepte le flux sur un disque $\pi R^2$ et rayonne par toute sa surface $4\pi R^2$ : $(1-A)\varphi_S\pi R^2=4\pi R^2\sigma T_s^4$, d'où
$$T_s=\left(\frac{(1-A)\varphi_S}{4\sigma}\right)^{1/4}\approx255\ \mathrm K\ (-18\ ^\circ\mathrm C).$$
C'est bien plus froid que la réalité : il manque l'effet de l'atmosphère.

**2.** Couche (par unité de surface) : elle absorbe $\sigma T_s^4$ et émet $\sigma T_a^4$ vers le haut et vers le bas : $\sigma T_s^4=2\sigma T_a^4$. Sol : $\dfrac{(1-A)\varphi_S}4+\sigma T_a^4=\sigma T_s^4$. En combinant : $\sigma T_a^4=\dfrac{(1-A)\varphi_S}4$, soit $T_a=255$ K (la planète vue de l'espace rayonne toujours comme à la question 1), et $T_s=2^{1/4}T_a\approx303\ \mathrm K$.

**3.** L'atmosphère réelle n'absorbe pas tout l'infrarouge (fenêtre atmosphérique vers $10\ \mathrm{\mu m}$), absorbe une partie du visible, et transporte de l'énergie par convection et évaporation. Le modèle à une couche opaque surestime donc l'effet ; il en montre néanmoins le mécanisme : l'atmosphère renvoie vers le sol une partie de son rayonnement infrarouge.
""", r"Sans atmosphère : $T_s\approx255$ K ; avec une couche absorbante : $T_a=255$ K, $T_s=2^{1/4}T_a\approx303$ K.")

ex('n-p2-dipole', P, 'Électrostatique', 2, 'Molécule d’eau près d’un ion', 20, r"""
On modélise une molécule d'eau par un dipôle électrostatique de moment $p=6{,}2\times10^{-30}\ \mathrm{C\,m}$. On donne $\dfrac1{4\pi\varepsilon_0}=9{,}0\times10^9\ \mathrm{SI}$, $e=1{,}6\times10^{-19}\ \mathrm C$, $k_B=1{,}38\times10^{-23}\ \mathrm{J\,K^{-1}}$.

1. Rappeler le potentiel créé à grande distance par un dipôle $\vec p$ et en déduire les composantes du champ en coordonnées sphériques.
2. Un dipôle rigide $\vec p$ est placé dans un champ extérieur $\vec E$. Rappeler son énergie potentielle et sa position d'équilibre stable.
3. Une molécule d'eau est à $r=0{,}30\ \mathrm{nm}$ d'un ion $\mathrm{Na^+}$ ; on la traite comme un dipôle ponctuel. Calculer l'énergie d'interaction dans la position d'équilibre stable et la comparer à $k_BT$ à $300$ K. Conclure sur la solvatation des ions.
4. La force subie par le dipôle est-elle attractive ou répulsive ? Exprimer sa norme.
""",
r"$V=\dfrac{\vec p\cdot\vec u_r}{4\pi\varepsilon_0r^2}=\dfrac{p\cos\theta}{4\pi\varepsilon_0r^2}$ et $\vec E=-\overrightarrow{\mathrm{grad}}V$.",
r"$E_p=-\vec p\cdot\vec E$ : équilibre stable pour $\vec p$ parallèle à $\vec E$ et de même sens.",
r"Le champ de l'ion est $\dfrac{e}{4\pi\varepsilon_0r^2}$ ; la force vaut $-\dfrac{\mathrm dE_p}{\mathrm dr}$ avec $E_p(r)=-\dfrac{pe}{4\pi\varepsilon_0r^2}$.",
r"""
**1.** $V=\dfrac{p\cos\theta}{4\pi\varepsilon_0r^2}$, d'où $E_r=\dfrac{2p\cos\theta}{4\pi\varepsilon_0r^3}$, $E_\theta=\dfrac{p\sin\theta}{4\pi\varepsilon_0r^3}$, $E_\varphi=0$ : le champ décroît en $1/r^3$.

**2.** $E_p=-\vec p\cdot\vec E$, minimale quand $\vec p$ est aligné avec $\vec E$ et de même sens (le couple $\vec p\wedge\vec E$ ramène vers cette position).

**3.** L'ion crée un champ radial $E=\dfrac{e}{4\pi\varepsilon_0r^2}$. Le dipôle s'oriente (oxygène, pôle négatif, vers l'ion) et $E_p=-pE=-\dfrac{9\times10^9\times6{,}2\times10^{-30}\times1{,}6\times10^{-19}}{(3{,}0\times10^{-10})^2}\approx-9{,}9\times10^{-20}\ \mathrm J\approx-0{,}62\ \mathrm{eV}$. À 300 K, $k_BT\approx4{,}1\times10^{-21}$ J $\approx0{,}026$ eV : l'interaction est 24 fois plus grande. L'agitation thermique ne désoriente pas les premières molécules d'eau : elles forment autour de l'ion une couche de solvatation stable.

**4.** $E_p(r)=-\dfrac{pe}{4\pi\varepsilon_0r^2}$ croît avec $r$ : $F_r=-\dfrac{\mathrm dE_p}{\mathrm dr}=-\dfrac{2pe}{4\pi\varepsilon_0r^3}<0$, force **attractive** en $1/r^3$. Un dipôle orienté est attiré vers les zones de champ intense.
""", r"$E_r=\frac{2p\cos\theta}{4\pi\varepsilon_0r^3}$, $E_\theta=\frac{p\sin\theta}{4\pi\varepsilon_0r^3}$ ; $E_p\approx-0{,}62$ eV $\approx24\,k_BT$ ; force attractive en $1/r^3$.")

ex('n-p2-plasma', P, 'Ondes électromagnétiques', 2, 'Ionosphère et ondes radio', 25, r"""
L'ionosphère est un plasma dilué contenant $n$ électrons libres par unité de volume (les ions, plus lourds, sont supposés immobiles). On néglige les collisions et l'action du champ magnétique de l'onde sur les électrons.

On donne : $e=1{,}6\times10^{-19}\ \mathrm C$, $m_e=9{,}1\times10^{-31}\ \mathrm{kg}$, $\varepsilon_0=8{,}85\times10^{-12}\ \mathrm{F\,m^{-1}}$, $n=1{,}0\times10^{12}\ \mathrm{m^{-3}}$.

1. Pour une onde plane progressive sinusoïdale $\underline{\vec E}=\underline{\vec E}_0e^{j(\omega t-kz)}$, montrer que la densité de courant vaut $\underline{\vec j}=-j\dfrac{ne^2}{m_e\omega}\underline{\vec E}$.
2. En déduire la relation de dispersion $k^2c^2=\omega^2-\omega_p^2$ et exprimer la pulsation plasma $\omega_p$. Calculer la fréquence $f_p$.
3. Que se passe-t-il pour $\omega<\omega_p$ ? Expliquer pourquoi les ondes radio « grandes ondes » se propagent loin autour de la Terre, alors que la communication avec les satellites utilise des fréquences de l'ordre du GHz.
4. Pour $\omega>\omega_p$, calculer les vitesses de phase et de groupe et montrer que $v_\varphi v_g=c^2$.
""",
r"PFD pour un électron : $m_e\dot{\vec v}=-e\vec E$, en complexes $\underline{\vec v}=\dfrac{-e\underline{\vec E}}{jm_e\omega}$ ; puis $\vec j=-ne\vec v$.",
r"Combine Maxwell-Faraday et Maxwell-Ampère : $-k^2\underline{\vec E}=-\dfrac{\omega^2}{c^2}\underline{\vec E}+j\mu_0\omega\underline{\vec j}$ ; $\omega_p=\sqrt{\dfrac{ne^2}{m_e\varepsilon_0}}$.",
r"Pour $\omega<\omega_p$, $k$ est imaginaire pur : onde évanescente, réflexion totale. $v_g=\mathrm d\omega/\mathrm dk$.",
r"""
**1.** $m_ej\omega\underline{\vec v}=-e\underline{\vec E}$ donc $\underline{\vec v}=\dfrac{je}{m_e\omega}\underline{\vec E}$ et $\underline{\vec j}=-ne\underline{\vec v}=-j\dfrac{ne^2}{m_e\omega}\underline{\vec E}$.

**2.** L'onde est transverse ; $\overrightarrow{\mathrm{rot}}\,\overrightarrow{\mathrm{rot}}\,\vec E=-\Delta\vec E$ donne $k^2\underline{\vec E}=\dfrac{\omega^2}{c^2}\underline{\vec E}-j\mu_0\omega\underline{\vec j}=\left(\dfrac{\omega^2}{c^2}-\dfrac{\mu_0ne^2}{m_e}\right)\underline{\vec E}$, soit
$$k^2c^2=\omega^2-\omega_p^2,\qquad\omega_p=\sqrt{\frac{ne^2}{m_e\varepsilon_0}}\approx5{,}6\times10^7\ \mathrm{rad\,s^{-1}},\quad f_p\approx9\ \mathrm{MHz}.$$

**3.** Pour $\omega<\omega_p$, $k^2<0$ : $k=-j/\delta$, onde évanescente qui ne transporte pas d'énergie en moyenne. Elle est **réfléchie** par l'ionosphère. Les ondes de quelques centaines de kHz à quelques MHz se réfléchissent entre le sol et l'ionosphère et contournent la courbure terrestre ; les ondes du GHz ($\gg f_p$) traversent l'ionosphère et atteignent les satellites.

**4.** $v_\varphi=\dfrac\omega k=\dfrac c{\sqrt{1-\omega_p^2/\omega^2}}>c$ ; en différentiant, $2kc^2\,\mathrm dk=2\omega\,\mathrm d\omega$, d'où $v_g=\dfrac{\mathrm d\omega}{\mathrm dk}=\dfrac{kc^2}\omega=c\sqrt{1-\omega_p^2/\omega^2}<c$. On a bien $v_\varphi v_g=c^2$ ; c'est $v_g$, inférieure à $c$, qui correspond à la propagation de l'énergie et de l'information.
""", r"$k^2c^2=\omega^2-\omega_p^2$, $\omega_p=\sqrt{ne^2/(m_e\varepsilon_0)}$, $f_p\approx9$ MHz ; réflexion si $\omega<\omega_p$ ; $v_\varphi v_g=c^2$.")

ex('n-p2-roulement', P, 'Mécanique', 2, 'Course de cylindres sur un plan incliné', 25, r"""
Un cylindre homogène plein (masse $m$, rayon $R$, moment d'inertie $J=\frac12mR^2$) et un cylindre creux à paroi mince (même masse, même rayon, $J=mR^2$) sont lâchés sans vitesse, côte à côte, en haut d'un plan incliné d'un angle $\alpha$ sur l'horizontale. On suppose qu'ils roulent sans glisser. On note $f$ le coefficient de frottement statique.

1. Pour un cylindre de moment d'inertie $J$, écrire la condition de roulement sans glissement et appliquer les théorèmes de la résultante et du moment cinétique (au centre de masse). En déduire l'accélération du centre.
2. Quel cylindre arrive en bas le premier ? Retrouver le résultat par un raisonnement énergétique.
3. Exprimer la réaction tangentielle. À quelle condition sur $\alpha$ le cylindre plein roule-t-il sans glisser ?
""",
r"Non-glissement : $v=R\omega$. Résultante (selon la ligne de plus grande pente) : $m\dot v=mg\sin\alpha-T$ ; moment en $G$ : $J\dot\omega=RT$.",
r"$\dot v=\dfrac{g\sin\alpha}{1+J/(mR^2)}$. Énergie : $mgh=\frac12mv^2+\frac12J\omega^2$, l'énergie cinétique de rotation « vole » une part de l'énergie disponible.",
r"$T=\dfrac{J}{R^2}\dot v$ et la réaction normale vaut $N=mg\cos\alpha$ ; loi de Coulomb : $T\le fN$.",
r"""
**1.** Non-glissement : $v=R\omega$. Selon la pente : $m\dot v=mg\sin\alpha-T$ ($T$ : réaction tangentielle, vers le haut). Moment cinétique en $G$ : $J\dot\omega=RT$, soit $T=\dfrac{J}{R^2}\dot v$. D'où
$$\dot v=\frac{g\sin\alpha}{1+\dfrac J{mR^2}}.$$
Cylindre plein : $\dot v=\frac23g\sin\alpha$ ; creux : $\dot v=\frac12g\sin\alpha$.

**2.** Le cylindre plein, plus accéléré, gagne la course, indépendamment de $m$ et $R$. Énergie (sans glissement, la réaction ne travaille pas) : $mgh=\frac12mv^2\left(1+\frac J{mR^2}\right)$. Le cylindre creux, dont la masse est loin de l'axe, stocke plus d'énergie en rotation et va donc moins vite.

**3.** $T=\dfrac J{R^2}\dot v=\dfrac{mg\sin\alpha}{3}$ pour le cylindre plein, et $N=mg\cos\alpha$. Il faut $T\le fN$, soit $\tan\alpha\le3f$. Au-delà, le cylindre glisse en roulant.
""", r"$\dot v=g\sin\alpha/(1+J/mR^2)$ : $\frac23g\sin\alpha$ (plein) > $\frac12g\sin\alpha$ (creux) ; non-glissement si $\tan\alpha\le3f$.")

ex('n-p2-beau', P, 'Thermodynamique', 2, 'Cycle de Beau de Rochas', 25, r"""
Le moteur à essence est modélisé par le cycle de Beau de Rochas, décrit par de l'air assimilé à un gaz parfait ($\gamma=1{,}4$) :
- $1\to2$ : compression adiabatique réversible de $V_1$ à $V_2=V_1/a$ ;
- $2\to3$ : combustion isochore, apport de chaleur $Q_{23}$ ;
- $3\to4$ : détente adiabatique réversible jusqu'à $V_1$ ;
- $4\to1$ : refroidissement isochore.

On donne : $a=9$, $T_1=300\ \mathrm K$, $T_3=2\,000\ \mathrm K$.

1. Représenter le cycle dans le diagramme de Watt $(P,V)$. Est-il moteur ?
2. Calculer $T_2$ et $T_4$.
3. Exprimer le rendement $\eta=-W/Q_{23}$ en fonction de $a$ et $\gamma$, et le calculer.
4. Comparer au rendement de Carnot entre $T_1$ et $T_3$. Pourquoi le rendement réel d'un moteur est-il encore plus faible ?
""",
r"Le cycle est parcouru dans le sens horaire dans le diagramme $(P,V)$ : il est moteur.",
r"Laplace : $T_2=T_1a^{\gamma-1}$ et $T_4=T_3a^{1-\gamma}$. Chaleurs isochores : $Q_{23}=C_v(T_3-T_2)$ et $Q_{41}=C_v(T_1-T_4)$.",
r"$\eta=1+\dfrac{Q_{41}}{Q_{23}}=1-\dfrac{T_4-T_1}{T_3-T_2}$ ; utilise $T_4/T_3=T_1/T_2=a^{1-\gamma}$.",
r"""
**1.** Deux adiabatiques et deux isochores ; le cycle est décrit dans le sens horaire (la détente $3\to4$ se fait à plus haute pression que la compression $1\to2$) : le travail total reçu est négatif, le cycle est **moteur**.

**2.** $T_2=T_1a^{\gamma-1}=300\times9^{0{,}4}\approx722\ \mathrm K$ et $T_4=T_3a^{1-\gamma}=2\,000/2{,}41\approx831\ \mathrm K$.

**3.** Sur le cycle, $W+Q_{23}+Q_{41}=0$, avec $Q_{23}=C_v(T_3-T_2)>0$ et $Q_{41}=C_v(T_1-T_4)<0$. D'où $\eta=1-\dfrac{T_4-T_1}{T_3-T_2}$. Comme $T_4=T_3a^{1-\gamma}$ et $T_1=T_2a^{1-\gamma}$ :
$$\eta=1-a^{1-\gamma}=1-9^{-0{,}4}\approx0{,}58.$$
Il ne dépend que du taux de compression (limité par le cliquetis, l'auto-inflammation de l'essence).

**4.** $\eta_C=1-T_1/T_3=0{,}85$. Le cycle théorique est moins bon car les échanges de chaleur se font à température variable (le gaz n'est pas en contact avec deux sources à $T_1$ et $T_3$). Le rendement réel (30 à 35 %) est plus faible encore : combustion non instantanée, pertes thermiques aux parois, frottements, pompage des gaz.
""", r"$T_2\approx722$ K, $T_4\approx831$ K ; $\eta=1-a^{1-\gamma}\approx58\ \%$ ($\eta_C=85\ \%$).")

ex('n-p2-vdw', P, 'Thermodynamique', 2, 'Détente de Joule – Gay-Lussac d’un gaz réel', 25, r"""
Une mole de dioxyde de carbone, initialement à $T_1=300\ \mathrm K$ dans un volume $V_1=1{,}0\ \mathrm L$, se détend brutalement dans le vide jusqu'au volume $V_2=2{,}0\ \mathrm L$, dans une enceinte rigide et calorifugée. On modélise le gaz par l'équation de van der Waals $\left(P+\dfrac{a}{V_m^2}\right)(V_m-b)=RT$, d'énergie interne molaire $U_m=C_vT-\dfrac a{V_m}+\text{cte}$ et d'entropie molaire $S_m=C_v\ln T+R\ln(V_m-b)+\text{cte}$.

On donne : $a=0{,}364\ \mathrm{Pa\,m^6\,mol^{-2}}$, $b=4{,}27\times10^{-5}\ \mathrm{m^3\,mol^{-1}}$, $C_v=3R$, $R=8{,}31\ \mathrm{J\,K^{-1}\,mol^{-1}}$.

1. Montrer que la détente se fait à énergie interne constante.
2. Calculer la température finale. Que donnerait le modèle du gaz parfait ?
3. Calculer l'entropie créée. Conclure.
4. Interpréter physiquement le refroidissement.
""",
r"Enceinte rigide et calorifugée, détente dans le vide : $W=0$ et $Q=0$, donc $\Delta U=0$.",
r"$C_v(T_2-T_1)=a\left(\dfrac1{V_2}-\dfrac1{V_1}\right)$, avec ici $V_m=V$ (une mole).",
r"Système isolé : $S_c=\Delta S=C_v\ln\dfrac{T_2}{T_1}+R\ln\dfrac{V_2-b}{V_1-b}$.",
r"""
**1.** L'enceinte est rigide : $W=0$ ; elle est calorifugée : $Q=0$. Premier principe : $\Delta U=0$.

**2.** $C_v(T_2-T_1)-a\left(\dfrac1{V_2}-\dfrac1{V_1}\right)=0$, soit $T_2-T_1=\dfrac a{C_v}\left(\dfrac1{V_2}-\dfrac1{V_1}\right)=\dfrac{0{,}364\times(500-1000)}{24{,}9}\approx-7{,}3\ \mathrm K$. Donc $T_2\approx292{,}7\ \mathrm K$. Pour un gaz parfait (première loi de Joule, $U$ ne dépend que de $T$), $T$ resterait égale à 300 K.

**3.** Le système est isolé, $S_c=\Delta S=3R\ln\dfrac{292{,}7}{300}+R\ln\dfrac{2{,}0\times10^{-3}-b}{1{,}0\times10^{-3}-b}\approx-0{,}61+5{,}95\approx5{,}3\ \mathrm{J\,K^{-1}}>0$ : la détente est irréversible (le gaz ne revient jamais spontanément dans le premier compartiment).

**4.** Le terme $-a/V_m$ traduit les interactions attractives entre molécules. En s'éloignant les unes des autres, les molécules gagnent de l'énergie potentielle, prise sur leur énergie cinétique d'agitation : le gaz se refroidit.
""", r"$\Delta U=0$ ; $T_2\approx292{,}7$ K ($-7{,}3$ K ; gaz parfait : 0) ; $S_c\approx5{,}3$ J/K.")

ex('n-p2-voile', P, 'Ondes électromagnétiques', 2, 'Voile solaire', 20, r"""
Une voile solaire est une très grande membrane réfléchissante propulsée par la pression de la lumière. On considère une voile plane parfaitement réfléchissante, orientée face au Soleil.

On donne : flux solaire à la distance de la Terre $\varphi_0=1\,361\ \mathrm{W\,m^{-2}}$, $c=3{,}00\times10^8\ \mathrm{m\,s^{-1}}$, champ de gravitation solaire à la distance de la Terre $g_0=5{,}9\times10^{-3}\ \mathrm{m\,s^{-2}}$.

1. Un photon d'énergie $\varepsilon$ a une quantité de mouvement $\varepsilon/c$. Montrer que la pression exercée sur la voile vaut $P=2\varphi/c$. La calculer à la distance de la Terre.
2. Une voile carrée de $100\ \mathrm m$ de côté, de masse totale $100\ \mathrm{kg}$, est à la distance de la Terre. Calculer la force et l'accélération dues à la lumière ; comparer à l'attraction solaire.
3. Montrer que le rapport de la force radiative au poids solaire est indépendant de la distance au Soleil. En déduire la masse surfacique maximale pour que la voile soit repoussée par le Soleil. Est-ce réaliste ?
""",
r"Pendant $\mathrm dt$, la surface $S$ reçoit $N=\varphi S\,\mathrm dt/\varepsilon$ photons ; chaque réflexion transfère $2\varepsilon/c$.",
r"$F=PS$ ; accélération $F/m$ ; compare à $g_0$.",
r"Le flux et la gravitation varient tous deux en $1/r^2$. Condition : $\dfrac{2\varphi_0}{c}S\ge mg_0$, soit $\sigma=m/S\le\dfrac{2\varphi_0}{cg_0}$.",
r"""
**1.** Pendant $\mathrm dt$, la voile reçoit $\varphi S\,\mathrm dt$ d'énergie, soit $\varphi S\,\mathrm dt/\varepsilon$ photons, chacun renvoyé en sens inverse : variation de quantité de mouvement $2\varepsilon/c$ par photon. Force $F=\dfrac{2\varphi S}c$ et pression $P=\dfrac{2\varphi}c=\dfrac{2\times1361}{3\times10^8}\approx9{,}1\times10^{-6}\ \mathrm{Pa}$.

**2.** $F=PS=9{,}1\times10^{-6}\times10^4\approx9{,}1\times10^{-2}\ \mathrm N$ et $a=F/m\approx9{,}1\times10^{-4}\ \mathrm{m\,s^{-2}}$, soit environ $15\ \%$ de $g_0$. La voile ne peut pas s'échapper du Soleil, mais la poussée, continue et gratuite, modifie l'orbite de façon notable sur des mois.

**3.** $\varphi=\varphi_0(r_0/r)^2$ et $g=g_0(r_0/r)^2$ : le rapport $\dfrac{2\varphi S}{cmg}$ ne dépend pas de $r$. La voile est repoussée si $\sigma=\dfrac mS<\dfrac{2\varphi_0}{cg_0}\approx1{,}5\times10^{-3}\ \mathrm{kg\,m^{-2}}=1{,}5\ \mathrm{g\,m^{-2}}$. C'est extrêmement léger : un film de quelques microns d'épaisseur, sans charge utile. Les projets réels (IKAROS) utilisent la voile pour manœuvrer, pas pour échapper au Soleil.
""", r"$P=2\varphi/c\approx9{,}1\times10^{-6}$ Pa ; $F\approx0{,}091$ N, $a\approx15\ \%$ de $g_0$ ; il faut $\sigma<1{,}5$ g/m².")

ex('n-p2-alternateur', P, 'Induction', 2, 'Alternateur élémentaire', 25, r"""
Une bobine plate de $N$ spires, de surface $S$, de résistance totale $R$ et d'inductance propre $L$, tourne à vitesse angulaire constante $\omega$ autour d'un axe de son plan, perpendiculaire à un champ magnétique uniforme et stationnaire $\vec B$. Elle est fermée sur elle-même. À $t=0$, sa normale est parallèle à $\vec B$.

1. Calculer la force électromotrice induite $e(t)$.
2. Établir l'équation électrique et déterminer l'intensité $i(t)$ en régime sinusoïdal établi (amplitude et déphasage).
3. Le moment magnétique de la bobine est $\vec{\mathcal M}=Ni\vec S$. Calculer la valeur moyenne du couple des forces de Laplace. Quel est son rôle ?
4. Faire le bilan de puissance : comparer la puissance mécanique moyenne que doit fournir l'opérateur et la puissance moyenne dissipée par effet Joule.
""",
r"$\Phi=NBS\cos\omega t$ et $e=-\dot\Phi=NBS\omega\sin\omega t$.",
r"$L\dfrac{\mathrm di}{\mathrm dt}+Ri=e$ ; en complexes, $\underline I=\dfrac{\underline e}{R+jL\omega}$.",
r"Couple $\vec\Gamma=\vec{\mathcal M}\wedge\vec B$, de projection sur l'axe $-NiSB\sin\omega t$ ; calcule $\langle i\sin\omega t\rangle$ avec le déphasage $\varphi=\arctan(L\omega/R)$.",
r"""
**1.** $\Phi=NBS\cos\omega t$, donc $e=-\dfrac{\mathrm d\Phi}{\mathrm dt}=E_m\sin\omega t$ avec $E_m=NBS\omega$.

**2.** $L\dfrac{\mathrm di}{\mathrm dt}+Ri=e$. En régime établi : $i=I_m\sin(\omega t-\varphi)$ avec $I_m=\dfrac{NBS\omega}{\sqrt{R^2+L^2\omega^2}}$ et $\tan\varphi=\dfrac{L\omega}R$.

**3.** $\vec{\mathcal M}=NiS\vec n$ et $\vec n$ fait l'angle $\omega t$ avec $\vec B$ : la projection du couple sur l'axe de rotation (dans le sens de $\omega$) vaut $\Gamma=-NiSB\sin\omega t$. Valeur moyenne : $\langle\Gamma\rangle=-NSBI_m\langle\sin(\omega t-\varphi)\sin\omega t\rangle=-\dfrac{NSBI_m\cos\varphi}2<0$. C'est un couple **résistant** : il s'oppose à la rotation (loi de Lenz).

**4.** L'opérateur doit fournir $\mathcal P_m=-\langle\Gamma\rangle\omega=\dfrac{NBS\omega I_m\cos\varphi}2=\dfrac{E_mI_m\cos\varphi}2$. Puissance Joule : $\dfrac{RI_m^2}2=\dfrac{R}2\cdot\dfrac{E_m^2}{R^2+L^2\omega^2}=\dfrac{E_mI_m}2\cdot\dfrac R{\sqrt{R^2+L^2\omega^2}}=\dfrac{E_mI_m\cos\varphi}2$. Les deux sont égales : toute la puissance mécanique est convertie en puissance électrique, puis dissipée (l'énergie magnétique stockée dans $L$ a une moyenne constante).
""", r"$e=NBS\omega\sin\omega t$ ; $I_m=\frac{NBS\omega}{\sqrt{R^2+L^2\omega^2}}$ ; couple moyen résistant ; $\mathcal P_m=\mathcal P_J=\frac12E_mI_m\cos\varphi$.")

ex('n-p2-diffusion', P, 'Diffusion thermique', 2, 'Diffusion d’un parfum dans une pièce', 20, r"""
On ouvre un flacon de parfum dans une pièce fermée, dans de l'air immobile. On étudie la diffusion des molécules de parfum, de coefficient de diffusion $D=1{,}0\times10^{-5}\ \mathrm{m^2\,s^{-1}}$, à une dimension selon $x$.

1. À partir de la loi de Fick et d'un bilan de matière, établir l'équation de diffusion $\dfrac{\partial n}{\partial t}=D\dfrac{\partial^2n}{\partial x^2}$.
2. Par une analyse en ordres de grandeur, estimer la durée nécessaire pour que le parfum diffuse sur $L=5\ \mathrm m$. Conclure sur le mécanisme réel de propagation des odeurs.
3. Vérifier que $n(x,t)=\dfrac{N_0}{\sqrt{4\pi Dt}}\exp\left(-\dfrac{x^2}{4Dt}\right)$ est solution, où $N_0$ est le nombre de molécules libérées en $x=0$ à $t=0$ (par unité de surface). Que représente la largeur $\sqrt{2Dt}$ ?
""",
r"Bilan sur une tranche $[x,x+\mathrm dx]$ de section $S$, sans création : $\partial_tn\,S\,\mathrm dx=j(x)S-j(x+\mathrm dx)S$, avec $j=-D\,\partial_xn$.",
r"Remplace dérivées par rapports d'échelles : $\dfrac n\tau\sim D\dfrac n{L^2}$, d'où $\tau\sim L^2/D$.",
r"Calcule $\partial_tn$ et $\partial_x^2n$ en écrivant $\ln n=\text{cte}-\frac12\ln t-\frac{x^2}{4Dt}$ ; la variance de la gaussienne est $2Dt$.",
r"""
**1.** Bilan de particules sur la tranche, sans source : $\dfrac{\partial n}{\partial t}S\,\mathrm dx=[j(x)-j(x+\mathrm dx)]S$, soit $\dfrac{\partial n}{\partial t}=-\dfrac{\partial j}{\partial x}$. Avec la loi de Fick $j=-D\dfrac{\partial n}{\partial x}$ : $\dfrac{\partial n}{\partial t}=D\dfrac{\partial^2n}{\partial x^2}$.

**2.** $\tau\sim\dfrac{L^2}D=\dfrac{25}{10^{-5}}=2{,}5\times10^6\ \mathrm s\approx1$ mois. Or on sent un parfum en quelques secondes ou minutes : la propagation réelle est due à la **convection** (mouvements d'air, même faibles, avec $v\sim1\ \mathrm{cm\,s^{-1}}$ : $L/v\sim10$ min). La diffusion n'est efficace qu'à petite échelle ($\tau\propto L^2$ : $1$ mm en $0{,}1$ s).

**3.** Avec $\ln n=\ln N_0-\tfrac12\ln(4\pi Dt)-\dfrac{x^2}{4Dt}$ : $\dfrac{\partial_tn}n=-\dfrac1{2t}+\dfrac{x^2}{4Dt^2}$ ; $\dfrac{\partial_xn}n=-\dfrac x{2Dt}$, d'où $\dfrac{\partial_x^2n}n=\dfrac{x^2}{4D^2t^2}-\dfrac1{2Dt}$. Donc $\partial_tn=D\partial_x^2n$. De plus $\int n\,\mathrm dx=N_0$ (conservation). C'est une gaussienne d'écart type $\sqrt{2Dt}$ : la distance typique parcourue croît comme $\sqrt t$, signature d'un mouvement aléatoire (marche au hasard), contrairement à $vt$ pour la convection.
""", r"$\partial_tn=D\partial_x^2n$ ; $\tau\sim L^2/D\approx2{,}5\times10^6$ s : c'est la convection qui transporte l'odeur ; étalement en $\sqrt{2Dt}$.")

ex('n-p3-neutron', P, 'Mécanique quantique', 3, 'Rayon d’une étoile à neutrons', 30, r"""
Une étoile à neutrons est formée de $N$ neutrons de masse $m_n$ ; sa masse est $M=Nm_n$ et son rayon $R$. On cherche à estimer $R$ par un raisonnement en ordres de grandeur, en négligeant les facteurs numériques.

On donne : $\hbar=1{,}05\times10^{-34}\ \mathrm{J\,s}$, $\mathcal G=6{,}67\times10^{-11}\ \mathrm{SI}$, $m_n=1{,}67\times10^{-27}\ \mathrm{kg}$, $M_\odot=2{,}0\times10^{30}\ \mathrm{kg}$.

1. Les neutrons sont des fermions : deux neutrons ne peuvent occuper le même état. On admet que chacun est alors confiné dans un volume de l'ordre de $R^3/N$. Estimer l'énergie cinétique d'un neutron, puis l'énergie cinétique totale $E_c(R)$.
2. Estimer l'énergie potentielle de gravitation $E_p(R)$ de l'étoile.
3. En minimisant l'énergie totale, montrer que $R\sim\dfrac{\hbar^2}{\mathcal Gm_n^3N^{1/3}}$. Calculer $R$ pour $M=1{,}4M_\odot$ (la valeur mesurée est de l'ordre de $12$ km).
4. Comment varie le rayon avec la masse ? Commenter ce comportement inhabituel.
""",
r"Chaque neutron est confiné sur $\Delta x\sim R/N^{1/3}$, donc $p\sim\hbar N^{1/3}/R$ et $\varepsilon_c\sim\dfrac{\hbar^2N^{2/3}}{m_nR^2}$.",
r"$E_p\sim-\dfrac{\mathcal GM^2}R$ (sans le facteur $3/5$). L'énergie totale a la forme $\dfrac A{R^2}-\dfrac BR$.",
r"Le minimum est en $R=2A/B$ ; avec $A=\hbar^2N^{5/3}/m_n$ et $B=\mathcal Gm_n^2N^2$, on trouve $R\sim\hbar^2/(\mathcal Gm_n^3N^{1/3})$.",
r"""
**1.** Chaque neutron dispose d'un volume $R^3/N$, soit $\Delta x\sim R/N^{1/3}$. Heisenberg : $p\sim\hbar N^{1/3}/R$, donc $\varepsilon_c\sim\dfrac{p^2}{m_n}\sim\dfrac{\hbar^2N^{2/3}}{m_nR^2}$ et $E_c\sim N\varepsilon_c=\dfrac{\hbar^2N^{5/3}}{m_nR^2}$. C'est la « pression de dégénérescence » : elle existe même à température nulle.

**2.** $E_p\sim-\dfrac{\mathcal GM^2}R=-\dfrac{\mathcal Gm_n^2N^2}R$.

**3.** $E(R)=\dfrac A{R^2}-\dfrac BR$ est minimale pour $E'(R)=-\dfrac{2A}{R^3}+\dfrac B{R^2}=0$, soit $R=\dfrac{2A}B\sim\dfrac{\hbar^2N^{5/3}}{m_n\cdot\mathcal Gm_n^2N^2}=\dfrac{\hbar^2}{\mathcal Gm_n^3N^{1/3}}$.

Numériquement : $N=\dfrac{1{,}4\times2{,}0\times10^{30}}{1{,}67\times10^{-27}}\approx1{,}7\times10^{57}$, $N^{1/3}\approx1{,}2\times10^{19}$ ; $\mathcal Gm_n^3\approx3{,}1\times10^{-91}$ SI. D'où $R\sim\dfrac{1{,}1\times10^{-68}}{3{,}1\times10^{-91}\times1{,}2\times10^{19}}\approx3\ \mathrm{km}$. L'ordre de grandeur (quelques km) est correct ; l'écart d'un facteur 4 vient des facteurs numériques négligés.

**4.** $R\propto N^{-1/3}\propto M^{-1/3}$ : **plus l'étoile est massive, plus elle est petite**, à l'inverse des objets ordinaires. Une masse plus grande comprime davantage les neutrons, ce qui augmente leur énergie de confinement. Au-delà d'une masse limite (quand les neutrons deviennent relativistes), la pression de dégénérescence ne suffit plus : l'étoile s'effondre en trou noir.
""", r"$E_c\sim\hbar^2N^{5/3}/(m_nR^2)$, $E_p\sim-\mathcal GM^2/R$ ; $R\sim\hbar^2/(\mathcal Gm_n^3N^{1/3})\approx3$ km ; $R\propto M^{-1/3}$.")
