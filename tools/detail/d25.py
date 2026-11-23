D = {}

D['p-em-1'] = r"""
**1. Charge d'une portion de hauteur $H$.** Volume du cylindre plein : $\pi b^2H$, donc charge volumique totale $\rho\pi b^2H$. Surface latérale : $2\pi bH$, donc charge surfacique totale $\sigma\,2\pi bH$. La neutralité impose
$$\rho\pi b^2H+\sigma\,2\pi bH=0\iff\sigma=-\frac{\rho b}2.$$
On a bien $\sigma<0$ puisque $\rho>0$.

**2. Symétries.** En coordonnées cylindriques $(r,\theta,z)$, soit $M$ un point quelconque.
- Le plan $(M,\vec u_r,\vec u_z)$ (contenant l'axe et $M$) est plan de symétrie de la distribution.
- Le plan $(M,\vec u_r,\vec u_\theta)$ (perpendiculaire à l'axe) l'est aussi, car le cylindre est infini.

$\vec E(M)$, vecteur polaire, appartient à ces deux plans : il est porté par leur intersection, c'est-à-dire $\vec E(M)=E\,\vec u_r$.

**2. Invariances.** La distribution est invariante par rotation d'angle $\theta$ et par translation selon $z$ : $E$ ne dépend que de $r$. Donc $\vec E=E(r)\,\vec u_r$.

**2. Surface de Gauss.** On prend un cylindre fermé coaxial de rayon $r$ et de hauteur $H$.
- Sur les bases, $\vec E\perp\mathrm d\vec S$ : flux nul.
- Sur la surface latérale, $\vec E\cdot\mathrm d\vec S=E(r)\,\mathrm dS$ avec $E(r)$ constant.

Donc $\Phi=E(r)\cdot2\pi rH$, et le théorème de Gauss s'écrit
$$E(r)\cdot2\pi rH=\frac{Q_{\mathrm{int}}}{\varepsilon_0}.$$

**2. Cas $r<b$.** Seule la charge volumique du cylindre de rayon $r$ est intérieure : $Q_{\mathrm{int}}=\rho\pi r^2H$. Donc
$$E(r)=\frac{\rho\pi r^2H}{2\pi rH\varepsilon_0}=\frac{\rho r}{2\varepsilon_0},\qquad\vec E=\frac{\rho r}{2\varepsilon_0}\vec u_r.$$

**2. Cas $r>b$.** Toute la charge de la portion est intérieure : $Q_{\mathrm{int}}=0$ (question 1). Donc $\vec E=\vec0$.

**2. Vérification par la relation de passage.** En $r=b$, $E$ passe de $E(b^-)=\frac{\rho b}{2\varepsilon_0}$ à $E(b^+)=0$, soit $E(b^+)-E(b^-)=-\frac{\rho b}{2\varepsilon_0}=\frac\sigma{\varepsilon_0}$. C'est bien la relation $\vec E_2-\vec E_1=\frac\sigma{\varepsilon_0}\vec n_{1\to2}$, avec $\vec n_{1\to2}=\vec u_r$. ✓
"""

D['p-em-2'] = r"""
**1. Charge volumique.** La charge $-e$ est répartie uniformément dans la boule de volume $\frac43\pi R^3$ : $\rho=-\frac{3e}{4\pi R^3}$.

**1. Symétries et invariances.** Tout plan contenant $O$ et $M$ est plan de symétrie : $\vec E(M)$ est radial. La distribution est invariante par toute rotation autour de $O$ : $\vec E=E(r)\,\vec u_r$.

**1. Théorème de Gauss.** On prend une sphère de centre $O$ et de rayon $r$ : $\vec E\cdot\mathrm d\vec S=E(r)\,\mathrm dS$, donc $\Phi=4\pi r^2E(r)=\frac{Q_{\mathrm{int}}}{\varepsilon_0}$.
- **$r\le R$** : $Q_{\mathrm{int}}=\rho\cdot\frac43\pi r^3=-e\frac{r^3}{R^3}$, d'où
$$\vec E=-\frac{e\,r}{4\pi\varepsilon_0R^3}\vec u_r=\frac{\rho r}{3\varepsilon_0}\vec u_r.$$
- **$r>R$** : $Q_{\mathrm{int}}=-e$, d'où $\vec E=-\frac e{4\pi\varepsilon_0r^2}\vec u_r$ (champ d'une charge ponctuelle).

$E$ est continu en $r=R$ (pas de charge surfacique) : les deux expressions donnent $-\frac e{4\pi\varepsilon_0R^2}$. ✓

**2. Densité d'énergie.** L'énergie électrostatique est localisée dans le champ, avec la densité $w=\frac{\varepsilon_0E^2}2$. En symétrie sphérique, on découpe l'espace en coquilles de volume $\mathrm d\tau=4\pi r^2\,\mathrm dr$ :
$$W=\int_0^{+\infty}\frac{\varepsilon_0E(r)^2}2\,4\pi r^2\,\mathrm dr.$$
Posons $k=\frac e{4\pi\varepsilon_0}$, de sorte que $E^2=\frac{k^2r^2}{R^6}$ à l'intérieur et $E^2=\frac{k^2}{r^4}$ à l'extérieur.

**2. Contribution intérieure.**
$$W_{\mathrm{int}}=2\pi\varepsilon_0k^2\int_0^R\frac{r^2}{R^6}r^2\,\mathrm dr=2\pi\varepsilon_0k^2\cdot\frac{R^5}{5R^6}=\frac{2\pi\varepsilon_0k^2}{5R}.$$

**2. Contribution extérieure.**
$$W_{\mathrm{ext}}=2\pi\varepsilon_0k^2\int_R^{+\infty}\frac{r^2}{r^4}\,\mathrm dr=2\pi\varepsilon_0k^2\Big[-\frac1r\Big]_R^{+\infty}=\frac{2\pi\varepsilon_0k^2}R.$$

**2. Total.** $W=2\pi\varepsilon_0k^2\cdot\frac6{5R}$. Avec $2\pi\varepsilon_0k^2=\frac{e^2}{8\pi\varepsilon_0}$ :
$$W=\frac{e^2}{8\pi\varepsilon_0}\cdot\frac6{5R}=\frac35\,\frac{e^2}{4\pi\varepsilon_0R}.$$
L'extérieur porte $\frac56$ de l'énergie. Quand $R\to0$, $W\to+\infty$ : une charge ponctuelle a une énergie propre infinie.

**2. Ordre de grandeur.** En posant $W=m_ec^2$ :
$$R=\frac35\cdot\frac{e^2}{4\pi\varepsilon_0m_ec^2}=\frac35\times2{,}8\times10^{-15}\approx1{,}7\times10^{-15}\ \mathrm m.$$
C'est l'ordre de grandeur du « rayon classique de l'électron » (le modèle n'a pas de sens physique en dessous : il faut la mécanique quantique).
"""

D['p-em-3'] = r"""
**1. Intensité.** L'intensité est le flux de $\vec j$ à travers une section droite : $\vec j=j\vec u_z$ est uniforme et $\mathrm d\vec S=\mathrm dS\,\vec u_z$, donc
$$I=\iint_{\text{section}}\vec j\cdot\mathrm d\vec S=j\cdot\pi b^2.$$

**2. Symétries.** Soit $M$ à distance $r$ de l'axe. Le plan $(M,\vec u_r,\vec u_z)$ contient l'axe : c'est un plan de symétrie de la distribution de courants. $\vec B$ est un pseudo-vecteur, donc $\vec B(M)$ est **orthogonal** à ce plan : $\vec B(M)=B\,\vec u_\theta$.

**2. Invariances.** Invariance par rotation autour de $(Oz)$ et par translation selon $z$ : $B=B(r)$. Ainsi $\vec B=B(r)\,\vec u_\theta$.

**2. Sur l'axe.** En un point de l'axe, **tous** les plans contenant l'axe sont plans de symétrie. $\vec B$ devrait être orthogonal à chacun d'eux ; or aucun vecteur non nul n'est orthogonal à deux plans distincts sécants selon $(Oz)$. Donc $\vec B(r=0)=\vec0$.

**3. Contour d'Ampère.** On prend le cercle $\mathcal C$ de rayon $r$, d'axe $(Oz)$, orienté par $\vec u_\theta$ (donc la surface qu'il délimite est orientée par $\vec u_z$). Sur ce cercle, $\vec B\cdot\mathrm d\vec\ell=B(r)\,r\,\mathrm d\theta$, donc
$$\oint_{\mathcal C}\vec B\cdot\mathrm d\vec\ell=2\pi r\,B(r)=\mu_0I_{\mathrm{enl}}.$$

**3. Cas $r<b$.** Le courant enlacé traverse le disque de rayon $r$ : $I_{\mathrm{enl}}=j\pi r^2$. Donc
$$B(r)=\frac{\mu_0j\pi r^2}{2\pi r}=\frac{\mu_0jr}2,\qquad\vec B=\frac{\mu_0jr}2\vec u_\theta.$$
On retrouve $\vec B(0)=\vec0$. ✓

**3. Cas $r\ge b$.** Tout le courant est enlacé : $I_{\mathrm{enl}}=I=j\pi b^2$. Donc
$$\vec B=\frac{\mu_0I}{2\pi r}\vec u_\theta=\frac{\mu_0jb^2}{2r}\vec u_\theta.$$
C'est le champ d'un fil infini.

**3. Commentaires.** En $r=b$, les deux expressions valent $\frac{\mu_0jb}2$ : $B$ est continu (il n'y a pas de courant surfacique). $B$ croît linéairement jusqu'à $r=b$, où il est maximal, puis décroît en $\frac1r$. Le sens de $\vec B$ suit la règle de la main droite autour de $\vec j$.
"""

D['p-max-1'] = r"""
**1. Équations de base.** En régime statique, l'équation de Maxwell-Faraday donne $\overrightarrow{\mathrm{rot}}\,\vec E=\vec0$, donc $\vec E$ dérive d'un potentiel : $\vec E=-\overrightarrow{\mathrm{grad}}\,V$. L'équation de Maxwell-Gauss s'écrit $\mathrm{div}\,\vec E=\frac\rho{\varepsilon_0}$.

**1. Combinaison.** Comme $\mathrm{div}(\overrightarrow{\mathrm{grad}}\,V)=\Delta V$ :
$$\mathrm{div}\big(-\overrightarrow{\mathrm{grad}}\,V\big)=\frac\rho{\varepsilon_0}\iff\Delta V+\frac\rho{\varepsilon_0}=0\quad\text{(équation de Poisson).}$$
Dans une région vide de charges ($\rho=0$), on obtient l'**équation de Laplace** : $\Delta V=0$.

**2. Réduction à une variable.** Le système est invariant par rotation autour de l'axe (pas de dépendance en $\theta$) et par translation selon $z$ (cylindres infinis) : $V=V(r)$. Les dérivées en $\theta$ et $z$ sont nulles, et l'équation de Laplace devient
$$\frac1r\frac{\mathrm d}{\mathrm dr}\Big(r\frac{\mathrm dV}{\mathrm dr}\Big)=0.$$

**2. Intégration.** On multiplie par $r\neq0$ : $\frac{\mathrm d}{\mathrm dr}\big(r\frac{\mathrm dV}{\mathrm dr}\big)=0$, donc $r\frac{\mathrm dV}{\mathrm dr}=A$ (constante). Puis $\frac{\mathrm dV}{\mathrm dr}=\frac Ar$, donc
$$V(r)=A\ln r+B.$$

**2. Conditions aux limites.**
- $V(a)=0$ : $A\ln a+B=0$, donc $B=-A\ln a$ et $V(r)=A\ln\frac ra$.
- $V(b)=U$ : $A\ln\frac ba=U$, donc $A=\frac U{\ln(b/a)}$.

$$V(r)=U\,\frac{\ln(r/a)}{\ln(b/a)}\qquad(a\le r\le b).$$
Vérification : $V(a)=U\frac{\ln1}{\ln(b/a)}=0$ et $V(b)=U$. ✓

**3. Champ électrique.** En cylindriques, pour $V=V(r)$ : $\overrightarrow{\mathrm{grad}}\,V=\frac{\mathrm dV}{\mathrm dr}\vec u_r$. Avec $\frac{\mathrm d}{\mathrm dr}\ln\frac ra=\frac1r$ :
$$\vec E=-\frac{\mathrm dV}{\mathrm dr}\vec u_r=-\frac U{r\ln(b/a)}\vec u_r.$$
Si $U>0$, $\vec E$ est dirigé vers l'axe, c'est-à-dire des hauts potentiels ($r=b$) vers les bas potentiels ($r=a$). Sa norme décroît en $\frac1r$ : le champ est le plus intense près du conducteur intérieur.

**Prolongement : capacité linéique.** Par le théorème de Gauss sur un cylindre de rayon $r\in]a,b[$ et de hauteur $H$ : $E(r)\,2\pi rH=\frac{\lambda H}{\varepsilon_0}$, où $\lambda$ est la charge linéique de l'armature intérieure. Donc $\lambda=2\pi\varepsilon_0rE(r)=-\frac{2\pi\varepsilon_0U}{\ln(b/a)}$. L'armature intérieure (au potentiel 0) porte $\lambda$, l'extérieure (au potentiel $U$) porte $-\lambda=\Gamma U$, d'où la capacité linéique du câble coaxial :
$$\Gamma=\frac{2\pi\varepsilon_0}{\ln(b/a)}.$$
"""
