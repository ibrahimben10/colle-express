D = {}

D['m-ccs-11'] = r"""
**1. Convergence dominée.** Soit $(\varphi_n)$ une suite de fonctions continues par morceaux sur un intervalle $I$, convergeant simplement vers une fonction $\varphi$ continue par morceaux. S'il existe $\psi$ intégrable sur $I$ telle que $|\varphi_n|\le\psi$ pour tout $n$, alors $\varphi$ est intégrable et $\int_I\varphi_n\to\int_I\varphi$.

**2. $f$ est définie.** Pour $x\ge0$ et $t\ge0$ : $0\le\frac{e^{-xt}}{1+t^2}\le\frac1{1+t^2}$, intégrable sur $\mathbb R_+$ (intégrale $\frac\pi2$). Donc $f(x)$ existe, et $f(0)=\frac\pi2$.

**3. Régularité de $f$.** La domination précédente, indépendante de $x$, donne la continuité de $f$ sur $\mathbb R_+$. Pour $a>0$ et $x\ge a$, les dérivées partielles $\partial_x^k\frac{e^{-xt}}{1+t^2}=\frac{(-t)^ke^{-xt}}{1+t^2}$ ($k=1,2$) sont continues et dominées par $\frac{t^ke^{-at}}{1+t^2}\le t^ke^{-at}$, intégrable. Donc $f$ est $C^2$ sur $[a,+\infty[$ pour tout $a>0$, c'est-à-dire sur $\mathbb R_+^*$, et
$$f''(x)+f(x)=\int_0^{+\infty}\frac{t^2e^{-xt}+e^{-xt}}{1+t^2}\,\mathrm dt=\int_0^{+\infty}e^{-xt}\,\mathrm dt=\frac1x.$$

**3. Écriture de $g$.** Pour $x>0$, avec $u=x+t$ et $\sin(u-x)=\sin u\cos x-\cos u\sin x$ :
$$g(x)=\int_x^{+\infty}\frac{\sin(u-x)}u\,\mathrm du=\cos x\,\sigma(x)-\sin x\,\gamma(x),\quad\sigma(x)=\int_x^{+\infty}\frac{\sin u}u\mathrm du,\ \gamma(x)=\int_x^{+\infty}\frac{\cos u}u\mathrm du.$$
Ces intégrales convergent en $+\infty$ (intégration par parties : $\int_x^A\frac{\sin u}u=\big[-\frac{\cos u}u\big]_x^A-\int_x^A\frac{\cos u}{u^2}$, et la dernière intégrale converge absolument ; de même pour $\gamma$). Comme fonctions de la borne inférieure, $\sigma'(x)=-\frac{\sin x}x$ et $\gamma'(x)=-\frac{\cos x}x$ : $\sigma,\gamma$ sont $C^\infty$ sur $\mathbb R_+^*$, donc $g$ aussi.

**3. Équation vérifiée par $g$.** En dérivant le produit :
$$g'(x)=-\sin x\,\sigma(x)+\cos x\Big(-\frac{\sin x}x\Big)-\cos x\,\gamma(x)-\sin x\Big(-\frac{\cos x}x\Big)=-\sin x\,\sigma(x)-\cos x\,\gamma(x),$$
$$g''(x)=-\cos x\,\sigma(x)+\frac{\sin^2x}x+\sin x\,\gamma(x)+\frac{\cos^2x}x=-g(x)+\frac1x.$$
Ainsi $f$ et $g$ vérifient la même équation $y''+y=\frac1x$ sur $\mathbb R_+^*$.

**3. Continuité de $g$ en 0.** $\sigma$ est continue sur $\mathbb R_+$ (car $\frac{\sin u}u$ se prolonge par continuité en 0) et $\sigma(0)=\int_0^\infty\frac{\sin u}u$. Pour $\gamma$ : $\gamma(x)=\int_x^1\frac{\cos u}u\,\mathrm du+\gamma(1)$ et $\big|\int_x^1\frac{\cos u}u\big|\le-\ln x$, donc $|\sin x\,\gamma(x)|\le x(|\ln x|+|\gamma(1)|)\to0$. Ainsi $g(x)\to\sigma(0)=g(0)$ : $g$ est continue en 0.

**4. Différence.** $h=f-g$ vérifie $h''+h=0$ sur $\mathbb R_+^*$, donc $h(x)=\alpha\cos x+\beta\sin x$.

**4. Comportement en $+\infty$.** $0\le f(x)\le\int_0^\infty e^{-xt}\mathrm dt=\frac1x$. Pour $g$, par parties :
$$g(x)=\Big[-\frac{\cos t}{x+t}\Big]_0^{+\infty}-\int_0^{+\infty}\frac{\cos t}{(x+t)^2}\mathrm dt=\frac1x-\int_0^{+\infty}\frac{\cos t}{(x+t)^2}\mathrm dt,\qquad|g(x)|\le\frac1x+\int_0^{\infty}\frac{\mathrm dt}{(x+t)^2}=\frac2x.$$
Donc $h(x)\to0$ en $+\infty$. Or $h(2k\pi)=\alpha$ et $h(2k\pi+\frac\pi2)=\beta$ pour tout $k$ : en faisant $k\to\infty$, $\alpha=\beta=0$.

**Conclusion.** $f=g$ sur $\mathbb R_+^*$, et en 0 par continuité. En particulier $\int_0^{+\infty}\frac{\sin t}t\,\mathrm dt=g(0)=f(0)=\frac\pi2$.
"""

D['m-ccs-12'] = r"""
On note $q=1-p\in]0,1[$.

**1. Loi géométrique.** $Y\sim\mathcal G(p)$ si $Y(\Omega)=\mathbb N^*$ et $P(Y=k)=q^{k-1}p$ : c'est le rang du premier succès dans une suite d'épreuves de Bernoulli indépendantes de paramètre $p$ ($k-1$ échecs puis un succès). Son espérance : avec $\sum_{k\ge1}kq^{k-1}=\frac1{(1-q)^2}$ (dérivée de la série géométrique),
$$E(Y)=\sum_{k\ge1}kpq^{k-1}=\frac p{(1-q)^2}=\frac1p.$$
De même $V(Y)=\frac q{p^2}$.

**2.(a) Espérance et variance.** Chaque $X_i$ suit $\mathcal G(p)$, et les $X_i$ sont indépendantes (les élèves passent leurs examens indépendamment). Par linéarité :
$$E(X)=\sum_{i=1}^NE(X_i)=\frac Np.$$
Par indépendance, les covariances sont nulles :
$$V(X)=\sum_{i=1}^NV(X_i)=\frac{Nq}{p^2}.$$

**2.(b) Fonction génératrice de $X_i$.** Pour $|s|<\frac1q$, la série géométrique de raison $qs$ converge et
$$G_{X_i}(s)=\sum_{k\ge1}pq^{k-1}s^k=ps\sum_{k\ge1}(qs)^{k-1}=\frac{ps}{1-qs}.$$

**2.(b) Fonction génératrice de $X$.** Pour des variables indépendantes, $G_{X_1+\dots+X_N}=\prod G_{X_i}$ (car $s^{X_1+\dots+X_N}=\prod s^{X_i}$ et l'espérance d'un produit de variables indépendantes est le produit des espérances). Donc
$$G_X(s)=\Big(\frac{ps}{1-qs}\Big)^N=p^Ns^N(1-qs)^{-N}.$$

**2.(b) Développement.** Pour $|u|<1$, $(1-u)^{-N}=\sum_{j\ge0}\binom{N+j-1}{j}u^j$ (dériver $N-1$ fois $\frac1{1-u}=\sum u^j$ : $\frac{(N-1)!}{(1-u)^N}=\sum_j(j+1)\cdots(j+N-1)u^j$). Avec $u=qs$ :
$$G_X(s)=\sum_{j\ge0}\binom{N+j-1}{j}p^Nq^j\,s^{N+j}.$$
Par unicité des coefficients, en posant $k=N+j$ et avec $\binom{k-1}{k-N}=\binom{k-1}{N-1}$ :
$$P(X=k)=\binom{k-1}{N-1}p^Nq^{k-N}\qquad(k\ge N).$$

**Interprétation.** C'est la loi de Pascal : $X$ a la loi du rang du $N$-ième succès dans une suite d'épreuves indépendantes. On le retrouve directement : $X=k$ signifie que le $k$-ième essai est un succès et que les $k-1$ précédents contiennent exactement $N-1$ succès, d'où $\binom{k-1}{N-1}p^{N-1}q^{k-N}\cdot p$.
"""

D['m-ccs-14'] = r"""
**1.(a) Spectre et polynôme caractéristique.** Pour $\lambda$ dans le corps de travail ($\mathbb R$ ou $\mathbb C$) :
$$\lambda\in\mathrm{Sp}(M)\iff\ker(M-\lambda I)\neq\{0\}\iff M-\lambda I\text{ non inversible}\iff\det(\lambda I-M)=0\iff\chi_M(\lambda)=0.$$

**1.(b) Dénominateur commun.** Écrivons $p=\frac{a'}{c'}$ et $q=\frac{b'}{c''}$ avec $c',c''\in\mathbb N^*$. Avec $c_0=c'c''$ : $p=\frac{a'c''}{c_0}$, $q=\frac{b'c'}{c_0}$. Soit $\delta=\mathrm{pgcd}(a'c'',b'c',c_0)\ge1$ ; on pose $a=\frac{a'c''}\delta$, $b=\frac{b'c'}\delta$, $c=\frac{c_0}\delta$. Alors $p=\frac ac$, $q=\frac bc$ et $\mathrm{pgcd}(a,b,c)=1$.

**2.(a) Les carrés modulo 3.** Pour $x\in\mathbb Z$, $x\equiv0,1,2\pmod3$ donne $x^2\equiv0,1,1$. Donc $x^2+y^2\equiv0\pmod3$ si et seulement si $x\equiv y\equiv0\pmod3$ (les autres sommes valent 1 ou 2).

**2.(a) Descente infinie.** Supposons qu'il existe une solution non nulle, et choisissons-en une, $(x,y,z)$, avec $|x|+|y|+|z|>0$ minimal. Comme $x^2+y^2=3z^2\equiv0\pmod3$, on a $x=3x_1$, $y=3y_1$. Alors $9(x_1^2+y_1^2)=3z^2$, soit $z^2=3(x_1^2+y_1^2)$ : $3\mid z^2$, donc $3\mid z$ (3 premier), $z=3z_1$. En reportant : $9x_1^2+9y_1^2=27z_1^2$, soit $x_1^2+y_1^2=3z_1^2$. $(x_1,y_1,z_1)$ est une solution non nulle avec $|x_1|+|y_1|+|z_1|=\frac13(|x|+|y|+|z|)$, strictement plus petite : contradiction. **La seule solution est $(0,0,0)$.**

**2.(b) $\sqrt2$ : oui.** $M=\begin{pmatrix}1&1\\1&-1\end{pmatrix}\in\mathcal S_2(\mathbb Q)$ a pour polynôme caractéristique $\chi_M=X^2-\mathrm{Tr}(M)X+\det M=X^2-0\cdot X-2=X^2-2$. D'après 1(a), $\mathrm{Sp}(M)=\{\sqrt2,-\sqrt2\}$.

**2.(c) $\sqrt3$ : non.** Soit $M=\begin{pmatrix}p&q\\q&r\end{pmatrix}\in\mathcal S_2(\mathbb Q)$ et $\chi_M=X^2-tX+d$ avec $t=p+r$, $d=pr-q^2$ rationnels. Si $\chi_M(\sqrt3)=0$ : $3-t\sqrt3+d=0$, soit $t\sqrt3=3+d$. Si $t\neq0$, $\sqrt3=\frac{3+d}t\in\mathbb Q$, faux. Donc $t=0$ et $d=-3$. Alors $r=-p$ et $d=-p^2-q^2=-3$ : $p^2+q^2=3$.

Par 1(b), $p=\frac ac$, $q=\frac bc$ avec $a,b,c\in\mathbb Z$, $c\neq0$, premiers entre eux dans leur ensemble. En multipliant par $c^2$ : $a^2+b^2=3c^2$. Par 2(a), $a=b=c=0$, ce qui contredit $c\neq0$.

**Conclusion.** Aucune matrice symétrique rationnelle $2\times2$ n'admet $\sqrt3$ pour valeur propre, alors que $\sqrt2$ est possible : la différence vient de ce que $2=1^2+1^2$ est somme de deux carrés de rationnels, et pas $3$.
===RÉPONSE===
$x^2+y^2=3z^2\Rightarrow x=y=z=0$ ; $\sqrt2$ : oui avec $\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ ; $\sqrt3$ : non (il faudrait $p^2+q^2=3$ dans $\mathbb Q$).
"""
