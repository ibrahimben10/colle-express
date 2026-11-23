D = {}

D['m-ccs-02'] = r"""
**1. Rappels.**
- *Continuité* : si les $f_n$ sont continues sur un intervalle $I$ et si $\sum f_n$ converge uniformément sur $I$ (ou sur tout segment de $I$), la somme est continue sur $I$.
- *Convergence normale* : si $\sup_I|f_n|\le\alpha_n$ avec $\sum\alpha_n$ convergente, alors $\sum f_n$ converge uniformément (et absolument) sur $I$.
- *Dérivation* : si les $f_n$ sont $C^1$ sur $I$, si $\sum f_n$ converge simplement sur $I$ et si $\sum f_n'$ converge uniformément sur tout segment de $I$, alors $S=\sum f_n$ est $C^1$ et $S'=\sum f_n'$.

**2. Convergence simple.** Pour tout réel $u$, $|\arctan u|\le|u|$ (accroissements finis : $|\arctan'|=\frac1{1+u^2}\le1$ et $\arctan0=0$). Donc
$$|f_n(x)|=\frac1n\Big|\arctan\frac xn\Big|\le\frac1n\cdot\frac{|x|}n=\frac{|x|}{n^2}.$$
Pour $x$ fixé, $\sum\frac{|x|}{n^2}$ converge (Riemann) : $\sum f_n(x)$ converge absolument, donc la série converge simplement sur $\mathbb R$.

**2. Dérivées.** $f_n$ est $C^1$ et, avec $(\arctan u)'=\frac1{1+u^2}$ et la dérivée de $\frac xn$ égale à $\frac1n$ :
$$f_n'(x)=\frac1n\cdot\frac1n\cdot\frac1{1+\frac{x^2}{n^2}}=\frac1{n^2+x^2}.$$
Donc $\sup_{\mathbb R}|f_n'|=\frac1{n^2}$, terme général d'une série convergente : $\sum f_n'$ converge normalement, donc uniformément, sur $\mathbb R$.

**2. Conclusion.** Par le théorème de dérivation, $S$ est $C^1$ sur $\mathbb R$ et $S'(x)=\sum_{n\ge1}\frac1{n^2+x^2}$.

**3. Pas de convergence uniforme sur $\mathbb R_+$.** Notons $R_N(x)=\sum_{n>N}f_n(x)$. Pour $x\ge0$, tous les termes sont positifs, donc on minore en ne gardant que $N+1\le n\le2N$. Pour $x=2N$ et un tel $n$ : $\frac{2N}n\ge1$, donc $\arctan\frac{2N}n\ge\arctan1=\frac\pi4$, et $\frac1n\ge\frac1{2N}$. Il y a $N$ termes, donc
$$R_N(2N)\ge\sum_{n=N+1}^{2N}\frac1{2N}\cdot\frac\pi4=N\cdot\frac1{2N}\cdot\frac\pi4=\frac\pi8.$$
Ainsi $\sup_{\mathbb R_+}|R_N|\ge\frac\pi8$ ne tend pas vers 0 : la convergence n'est **pas** uniforme sur $\mathbb R_+$.

**Compléments.** Sur $[0,A]$, $|R_N(x)|\le A\sum_{n>N}\frac1{n^2}\to0$ : la convergence est uniforme sur tout segment. Et $S(x)\to+\infty$ quand $x\to+\infty$ (pour tout $N$, $S(x)\ge\sum_{n\le N}f_n(x)\to\frac\pi2\sum_{n\le N}\frac1n$), alors que chaque $f_n$ est bornée : c'est une autre preuve de la non-uniformité.
"""

D['m-ccs-03'] = r"""
**1. Énoncé.** Soit $(Y_k)_{k\ge1}$ une suite de variables aléatoires indépendantes, de même loi, admettant une variance $\sigma^2$ ; on note $m=E(Y_1)$ et $\overline Y_n=\frac1n\sum_{k=1}^nY_k$. Alors pour tout $\varepsilon>0$, $P\big(|\overline Y_n-m|\ge\varepsilon\big)\xrightarrow[n\to\infty]{}0$.

**1. Démonstration.** Par linéarité, $E(\overline Y_n)=\frac1n\cdot nm=m$. Par indépendance (les covariances sont nulles), $V\big(\sum Y_k\big)=\sum V(Y_k)=n\sigma^2$, donc $V(\overline Y_n)=\frac1{n^2}\cdot n\sigma^2=\frac{\sigma^2}n$. L'inégalité de Bienaymé-Tchebychev donne
$$P\big(|\overline Y_n-m|\ge\varepsilon\big)\le\frac{V(\overline Y_n)}{\varepsilon^2}=\frac{\sigma^2}{n\varepsilon^2}\xrightarrow[n\to\infty]{}0.$$

**2. Relation entre les $X_k$ et les $U_k$.** $X_k$ est le reste de $S_k$ modulo 10. Comme $S_k=S_{k-1}+U_k$ : $X_0=U_0$ et $X_k\equiv X_{k-1}+U_k\pmod{10}$.

**2. Une bijection.** Notons $D=\{0,\dots,9\}$ et définissons $\Phi:D^{n+1}\to D^{n+1}$ par $\Phi(u_0,\dots,u_n)=(x_0,\dots,x_n)$ avec $x_k=(u_0+\dots+u_k)\bmod10$. Elle est bijective : connaissant $(x_0,\dots,x_n)$, on retrouve $u_0=x_0$ et $u_k=(x_k-x_{k-1})\bmod10$ (l'unique élément de $D$ congru à $x_k-x_{k-1}$). Une application d'un ensemble fini dans lui-même qui admet un inverse est une bijection.

**2. Loi jointe.** Les $U_k$ sont indépendantes et uniformes, donc pour tout $(u_0,\dots,u_n)\in D^{n+1}$ :
$$P(U_0=u_0,\dots,U_n=u_n)=\prod_{k=0}^n\frac1{10}=10^{-(n+1)}.$$
Pour $(x_0,\dots,x_n)\in D^{n+1}$, l'événement $(X_0=x_0,\dots,X_n=x_n)$ est égal à $\big((U_0,\dots,U_n)=\Phi^{-1}(x_0,\dots,x_n)\big)$, donc
$$P(X_0=x_0,\dots,X_n=x_n)=10^{-(n+1)}.$$

**2. Conclusion.** En sommant sur toutes les valeurs des autres coordonnées, $P(X_k=x)=10^n\cdot10^{-(n+1)}=\frac1{10}$ : chaque $X_k$ suit la loi **uniforme sur $\{0,\dots,9\}$**. Et la loi jointe est le produit des lois marginales : $P(X_0=x_0,\dots,X_n=x_n)=\prod_k\frac1{10}=\prod_kP(X_k=x_k)$. Les $X_0,\dots,X_n$ sont donc **mutuellement indépendantes**, pour tout $n$.

**Commentaire.** C'est surprenant, car $X_n$ et $X_{n+1}$ dépendent des mêmes $U_0,\dots,U_n$ ; l'indépendance vient de ce que l'incrément uniforme $U_{n+1}$ « efface » toute information modulo 10.
"""

D['m-ccs-05'] = r"""
On suppose $A$ et $B$ non nuls et non tous deux constants (sinon il n'y a rien à démontrer).

**1. Degré d'une somme.** Si $A=\sum a_kX^k$ et $B=\sum b_kX^k$, alors $A+B=\sum(a_k+b_k)X^k$ et tous les coefficients d'indice $k>\max(\deg A,\deg B)$ sont nuls : $\deg(A+B)\le\max(\deg A,\deg B)$. L'inégalité est stricte quand les termes dominants se compensent : $A=X$, $B=1-X$, $A+B=1$.

**2.(a) Une racine n'appartient qu'à un seul des trois polynômes.** Si $z$ était racine de $A$ et de $B$, elle le serait de $C=A+B$ ; si elle était racine de $A$ et de $C$, elle le serait de $B=C-A$ ; etc. C'est exclu par hypothèse. Donc une racine $z$ de $ABC$ de multiplicité $n$ est racine d'**exactement un** des trois polynômes, avec multiplicité $n$.

**2.(a) Trois écritures de $W$.** Avec $C'=A'+B'$ :
$$AC'-CA'=A(A'+B')-(A+B)A'=AB'-BA'=W,\qquad CB'-BC'=(A+B)B'-B(A'+B')=AB'-BA'=W.$$

**2.(a) Multiplicité dans $W$.** Supposons $(X-z)^n\mid A$ (cas où $z$ est racine de $A$). Alors $(X-z)^{n-1}$ divise $A$ et $A'$ (si $A=(X-z)^nQ$, $A'=(X-z)^{n-1}\big(nQ+(X-z)Q'\big)$), donc divise $W=AB'-BA'$. Si $z$ est racine de $B$, on utilise la même écriture ; si $z$ est racine de $C$, on utilise $W=CB'-BC'$. Dans tous les cas, $z$ est racine de $W$ de multiplicité au moins $n-1$.

**2.(b) $W$ n'est pas nul.** Si $W=0$, alors sur un intervalle où $B$ ne s'annule pas, $\big(\frac AB\big)'=\frac{A'B-AB'}{B^2}=-\frac W{B^2}=0$, donc $A=\lambda B$ (égalité de polynômes vraie sur un intervalle, donc partout). Toute racine de $B$ serait racine de $A$ : par hypothèse, $B$ n'a pas de racine, donc $B$ est constant, puis $A$ aussi : exclu.

**2.(b) Minoration de $\mu$.** Notons $Z$ l'ensemble des racines distinctes de $ABC$ ($|Z|=\mu$) et $m_z$ la multiplicité de $z$ dans $ABC$. Les polynômes $(X-z)^{m_z-1}$, $z\in Z$, sont premiers entre eux deux à deux et divisent $W\neq0$, donc leur produit divise $W$ :
$$\sum_{z\in Z}(m_z-1)\le\deg W.$$
Or $\sum_zm_z=\deg(ABC)=\deg A+\deg B+\deg C$ (sur $\mathbb C$, tout polynôme est scindé). Donc $\deg A+\deg B+\deg C-\mu\le\deg W$, soit
$$\mu\ge\deg A+\deg B+\deg C-\deg W.$$

**2.(c) Conclusion.** $\deg(AB')\le\deg A+\deg B-1$ et $\deg(BA')\le\deg A+\deg B-1$, donc $\deg W\le\deg A+\deg B-1$. En reportant : $\mu\ge\deg C+1$. Avec $W=AC'-CA'$ (donc $\deg W\le\deg A+\deg C-1$) on obtient $\mu\ge\deg B+1$, et avec $W=CB'-BC'$ on obtient $\mu\ge\deg A+1$. Ainsi
$$\mu>\max(\deg A,\deg B,\deg C).$$
C'est le **théorème de Mason–Stothers**. Application : si $f^n+g^n=h^n$ avec $f,g,h$ polynômes premiers entre eux non tous constants, alors $\mu\le\deg f+\deg g+\deg h$ et $n\max(\deg)<\mu$ imposent $n\le2$ : il n'y a pas de « Fermat polynomial » pour $n\ge3$.
"""
