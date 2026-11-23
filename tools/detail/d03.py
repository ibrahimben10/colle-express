D = {}

D['m-ccmp-04b'] = r"""
**Étape 1 : le déterminant est un morphisme injectif sur $G$.** L'application $\varphi:G\to\mathbb C^*$, $M\mapsto\det M$, est bien définie (une matrice inversible a un déterminant non nul) et c'est un morphisme de groupes : $\det(MN)=\det M\det N$. Son noyau est
$$\ker\varphi=\{M\in G:\det M=1\}=G\cap SL_n(\mathbb C)=\{I_n\}.$$
Un morphisme de noyau trivial est injectif : si $\det M=\det N$, alors $\det(MN^{-1})=1$, donc $MN^{-1}=I_n$ et $M=N$. Ainsi $\varphi$ réalise un isomorphisme de $G$ sur $H=\varphi(G)$, sous-groupe fini de $\mathbb C^*$ de cardinal $N=|G|$.

**Étape 2 : $H$ est le groupe $\mathbb U_N$.** Soit $z\in H$. Par le théorème de Lagrange, l'ordre de $z$ divise $N$, donc $z^N=1$ : $z\in\mathbb U_N=\{w\in\mathbb C:w^N=1\}$. Ainsi $H\subset\mathbb U_N$. Or $\mathbb U_N$ a exactement $N$ éléments (les $e^{2ik\pi/N}$, $0\le k<N$, racines distinctes de $X^N-1$) et $|H|=N$ : l'inclusion est une égalité, $H=\mathbb U_N$.

**Étape 3 : conclusion.** $\mathbb U_N$ est cyclique, engendré par $\omega=e^{2i\pi/N}$ (ses puissances $\omega^k$, $0\le k<N$, sont les $N$ éléments). Un groupe isomorphe à un groupe cyclique est cyclique : si $g\in G$ est l'unique élément tel que $\det g=\omega$, alors $\varphi(g^k)=\omega^k$ parcourt $H$, donc (injectivité) les $g^k$ parcourent $G$.

**Conclusion.** $G$ est cyclique d'ordre $N$, engendré par l'élément de déterminant $e^{2i\pi/N}$.
"""

D['m-ccmp-04c'] = r"""
**Données.** On note $q=1-p\in\,]0,1[$. Pour $k\ge1$, $P(X=k)=P(Y=k)=pq^{k-1}$, et $E(X)=\frac1p$, $V(X)=\frac q{p^2}$.

**1. Valeurs prises.** $X$ et $Y$ sont à valeurs dans $\mathbb N^*$, donc $X+Y$ est à valeurs dans $\{2,3,4,\dots\}$.

**1. Formule des probabilités totales.** Soit $n\ge2$. Les événements $(X=k)$, $k\ge1$, forment un système complet. L'événement $(X+Y=n)\cap(X=k)$ est égal à $(X=k)\cap(Y=n-k)$ ; il est vide si $n-k<1$, c'est-à-dire $k>n-1$. Donc
$$P(X+Y=n)=\sum_{k=1}^{n-1}P\big((X=k)\cap(Y=n-k)\big)=\sum_{k=1}^{n-1}P(X=k)\,P(Y=n-k)\quad\text{(indépendance)}.$$

**1. Calcul.** Chaque terme vaut
$$pq^{k-1}\cdot pq^{(n-k)-1}=p^2q^{k-1+n-k-1}=p^2q^{n-2},$$
indépendant de $k$. Il y a $n-1$ termes ($k=1,\dots,n-1$), donc
$$P(X+Y=n)=(n-1)\,p^2q^{n-2}\qquad(n\ge2).$$

**1. Vérification.** Avec $\sum_{m\ge1}mq^{m-1}=\frac1{(1-q)^2}$ (dérivée de la série géométrique), en posant $m=n-1$ : $\sum_{n\ge2}(n-1)p^2q^{n-2}=p^2\cdot\frac1{(1-q)^2}=\frac{p^2}{p^2}=1$. C'est bien une loi de probabilité (loi de Pascal : rang du deuxième succès).

**2. Espérance.** Par linéarité (pas besoin d'indépendance) : $E(X+Y)=E(X)+E(Y)=\dfrac2p$.

**2. Variance.** $X$ et $Y$ sont indépendantes, donc $\mathrm{Cov}(X,Y)=0$ et
$$V(X+Y)=V(X)+V(Y)+2\,\mathrm{Cov}(X,Y)=\frac{2q}{p^2}=\frac{2(1-p)}{p^2}.$$
"""

D['m-ccmp-05a'] = r"""
**Valeurs de $Y$.** Le reste de la division de $X$ par $p$ est dans $\{0,\dots,p-1\}$, et pour un tel $r$ :
$$(Y=r)=\bigcup_{k\ge0}(X=kp+r)\quad\text{(réunion disjointe)},\qquad P(Y=r)=e^{-\lambda}\sum_{n\equiv r\,[p]}\frac{\lambda^n}{n!}.$$

**Le filtre des racines de l'unité.** Soit $\omega=e^{2i\pi/p}$ et $m\in\mathbb Z$. On calcule $S_m=\frac1p\sum_{j=0}^{p-1}(\omega^m)^j$.
- Si $p\mid m$, $\omega^m=1$ et $S_m=\frac1p\cdot p=1$.
- Sinon $\omega^m\neq1$ et, par la somme géométrique, $S_m=\frac1p\cdot\frac{1-(\omega^m)^p}{1-\omega^m}=\frac1p\cdot\frac{1-(\omega^p)^m}{1-\omega^m}=0$ car $\omega^p=1$.

Ainsi $\mathbf 1_{n\equiv r\,[p]}=\frac1p\sum_{j=0}^{p-1}\omega^{j(n-r)}$ pour tout $n\in\mathbb N$.

**Calcul de la somme.** On remplace l'indicatrice et on intervertit une somme finie (sur $j$) et une série absolument convergente (sur $n$) :
$$\sum_{n\equiv r}\frac{\lambda^n}{n!}=\sum_{n\ge0}\frac{\lambda^n}{n!}\cdot\frac1p\sum_{j=0}^{p-1}\omega^{j(n-r)}=\frac1p\sum_{j=0}^{p-1}\omega^{-jr}\sum_{n\ge0}\frac{(\lambda\omega^j)^n}{n!}=\frac1p\sum_{j=0}^{p-1}\omega^{-jr}e^{\lambda\omega^j}.$$

**Loi de $Y$.** En multipliant par $e^{-\lambda}$, pour $r\in\{0,\dots,p-1\}$ :
$$P(Y=r)=\frac1p\sum_{j=0}^{p-1}\omega^{-jr}\,e^{\lambda(\omega^j-1)}.$$
Forme réelle : avec $\omega^j=\cos\frac{2\pi j}p+i\sin\frac{2\pi j}p$, on a $\omega^{-jr}e^{\lambda(\omega^j-1)}=e^{\lambda(\cos\frac{2\pi j}p-1)}e^{i(\lambda\sin\frac{2\pi j}p-\frac{2\pi jr}p)}$. La somme est réelle (c'est une probabilité ; les termes $j$ et $p-j$ sont conjugués), donc on peut ne garder que les parties réelles :
$$P(Y=r)=\frac1p\sum_{j=0}^{p-1}e^{\lambda(\cos\frac{2\pi j}p-1)}\cos\Big(\lambda\sin\frac{2\pi j}p-\frac{2\pi jr}p\Big).$$

**Vérifications.**
- $\sum_rP(Y=r)=\frac1p\sum_je^{\lambda(\omega^j-1)}\sum_r\omega^{-jr}$ ; la somme sur $r$ vaut $p$ si $j=0$ et $0$ sinon : on trouve $e^0=1$. ✓
- Pour $p=2$ ($\omega=-1$) : $P(Y=0)=\frac12(1+e^{-2\lambda})=e^{-\lambda}\operatorname{ch}\lambda$ et $P(Y=1)=\frac12(1-e^{-2\lambda})=e^{-\lambda}\operatorname{sh}\lambda$, ce qui correspond bien aux termes pairs et impairs de l'exponentielle. ✓
"""

D['m-ccmp-05b'] = r"""
**Étape 1 : valeurs propres de $A$.** Soit $\lambda\in\mathbb C$ valeur propre de $A$ et $X\in\mathbb C^n\setminus\{0\}$ avec $AX=\lambda X$. Posons $s=\overline X^{\top}AX$. D'une part $s=\lambda\overline X^{\top}X=\lambda\|X\|^2$. D'autre part, $s$ est un nombre (matrice $1\times1$), égal à sa transposée ; avec $A^{\top}=-A$ et $A$ réelle :
$$\overline s=X^{\top}A\overline X=(X^{\top}A\overline X)^{\top}=\overline X^{\top}A^{\top}X=-\overline X^{\top}AX=-s.$$
Donc $s$ est imaginaire pur, et $\lambda=s/\|X\|^2$ aussi. Comme $A$ est réelle, $\chi_A\in\mathbb R[X]$ : ses racines non réelles vont par paires conjuguées $\pm i\theta$ avec la même multiplicité. Le spectre de $A$ (avec multiplicités) est donc formé de $0$ ($n_0$ fois) et de couples $i\theta_k,-i\theta_k$ ($k=1,\dots,s$, $\theta_k>0$), avec $n_0+2s=n$.

**Étape 2 : valeurs propres de $\exp(xA)+2I_n$.** Trigonalisons $A$ sur $\mathbb C$ : $A=PTP^{-1}$ avec $T$ triangulaire supérieure de diagonale $(\mu_1,\dots,\mu_n)$ (les valeurs propres ci-dessus). Les puissances $T^m$ sont triangulaires de diagonale $(\mu_i^m)$, donc $\exp(xT)=\sum\frac{x^mT^m}{m!}$ est triangulaire de diagonale $(e^{x\mu_i})$, et
$$\exp(xA)+2I_n=P\big(\exp(xT)+2I_n\big)P^{-1},$$
où $\exp(xT)+2I_n$ est triangulaire de diagonale $(e^{x\mu_i}+2)$.

**Étape 3 : calcul de $f$.** Le déterminant d'une matrice triangulaire est le produit de ses coefficients diagonaux, et il est invariant par similitude :
$$f(x)=\prod_{i=1}^n\big(e^{x\mu_i}+2\big)=(e^0+2)^{n_0}\prod_{k=1}^s\big(e^{ix\theta_k}+2\big)\big(e^{-ix\theta_k}+2\big)=3^{n_0}\prod_{k=1}^s\big|e^{ix\theta_k}+2\big|^2,$$
car $e^{-i\varphi}+2=\overline{e^{i\varphi}+2}$ et $z\overline z=|z|^2$.

**Étape 4 : minoration.** Pour $\varphi\in\mathbb R$, l'inégalité triangulaire donne $|e^{i\varphi}+2|\ge|2|-|e^{i\varphi}|=2-1=1$. Plus précisément,
$$|e^{i\varphi}+2|^2=(\cos\varphi+2)^2+\sin^2\varphi=5+4\cos\varphi\in[1,9].$$
Donc chaque facteur est $\ge1$ et $f(x)\ge3^{n_0}\ge1$ pour tout $x\in\mathbb R$.

**Conclusion.** $\displaystyle\inf_{x\in\mathbb R}f(x)\ge1>0$. (L'infimum vaut exactement $3^{n_0}$ si l'on peut rendre tous les $\cos(x\theta_k)$ proches de $-1$ simultanément, ce qui n'est pas toujours possible ; seule la minoration est demandée.)
===RÉPONSE===
$f(x)=3^{n_0}\prod_k|e^{ix\theta_k}+2|^2$ avec $|e^{i\varphi}+2|^2=5+4\cos\varphi\ge1$ : $\inf f\ge1>0$.
"""
