
# Indices et corrigés — Maths Centrale + X-ENS
C = {}
def c(id, h1, h2, h3, corrige, reponse=""):
    C[id] = {"indices": [h1.strip(), h2.strip(), h3.strip()], "corrige": corrige.strip(), "reponse": reponse.strip()}

c("m-ccs-01",
r"$M^{-1}=\frac1{\det M}\operatorname{com}(M)^T$ : les coefficients sont des fractions rationnelles des coefficients de $M$.",
r"Pour une matrice par blocs $\begin{pmatrix}0&W^T\\V&I_p\end{pmatrix}$, utilise le complément de Schur (élimination par blocs).",
r"Pour 3(b), compte les dimensions : $\operatorname{rg}V=k$, $\dim(\operatorname{Im}W)^\perp=p-k$, et montre que l'intersection est nulle.",
r"""
**1.** $M\,\operatorname{com}(M)^T=\det(M)I_n$, donc $M^{-1}=\frac1{\det M}\operatorname{com}(M)^T$ sur $GL_n(\mathbb R)$. Chaque coefficient de $M^{-1}$ est un quotient de polynômes en les coefficients de $M$, à dénominateur $\det M$ non nul : $M\mapsto M^{-1}$ est continue.

**2.** Les tailles des blocs recueillis sont incompatibles ; une version cohérente (et classique) est $M_{V,W}=\begin{pmatrix}0_k&W^T\\V&I_p\end{pmatrix}\in\mathcal M_{k+p}(\mathbb R)$. Par élimination de Gauss par blocs,
$$\begin{pmatrix}I_k&-W^T\\0&I_p\end{pmatrix}\begin{pmatrix}0_k&W^T\\V&I_p\end{pmatrix}=\begin{pmatrix}-W^TV&0\\V&I_p\end{pmatrix},$$
donc $\det M_{V,W}=\det(-W^TV)=(-1)^k\det(W^TV)$ : si $W^TV$ est inversible, $M_{V,W}$ l'est.

**3.(a)** $\delta:W\mapsto\det(W^TV)$ est continue (polynomiale) et $\delta(V)=\det(V^TV)=\det I_k=1$. Donc $\mathcal V=\delta^{-1}(\mathbb R^*)$ est un ouvert contenant $V$, sur lequel $W^TV$ est inversible.

**(b)** Soit $W\in\mathcal V$. Comme $V^TV=I_k$, $V$ est injective : $\dim\operatorname{Im}V=k$. Comme $W^TV$ est inversible, $\operatorname{rg}W\ge\operatorname{rg}(W^TV)=k$, donc $\operatorname{rg}W=k$ et $\dim(\operatorname{Im}W)^\perp=p-k$. Si $x=Vy\in(\operatorname{Im}W)^\perp$, alors $W^Tx=W^TVy=0$, d'où $y=0$ et $x=0$. Les dimensions s'ajoutant à $p$, on obtient
$$\mathbb R^p=\operatorname{Im}V\oplus(\operatorname{Im}W)^\perp.$$
""", r"$\det M_{V,W}=\pm\det(W^TV)$ ; $\operatorname{Im}V\oplus(\operatorname{Im}W)^\perp=\mathbb R^p$ près de $V$.")

c("m-ccs-02",
r"Majore $|f_n(x)|$ par $\frac{|x|}{n^2}$ (inégalité $|\arctan u|\le|u|$).",
r"Calcule $f_n'(x)=\frac1{n^2+x^2}$ : la série des dérivées converge normalement sur $\mathbb R$.",
r"Pour la convergence uniforme sur $\mathbb R_+$, minore le reste $R_N(x)$ en $x=2N$ en ne gardant que les termes $N<n\le2N$.",
r"""
**1.** *Convergence uniforme et continuité de la somme* : si $\sum f_n$ converge uniformément sur un intervalle et les $f_n$ sont continues, la somme est continue. *Dérivation* : si $\sum f_n$ converge simplement, les $f_n$ sont $\mathcal C^1$ et $\sum f_n'$ converge uniformément sur tout segment, alors $\sum f_n$ est $\mathcal C^1$ et $\big(\sum f_n\big)'=\sum f_n'$.

**2.** $|f_n(x)|\le\frac1n\cdot\frac{|x|}n=\frac{|x|}{n^2}$ : convergence simple (absolue) sur $\mathbb R$. De plus $f_n'(x)=\frac1n\cdot\frac{1/n}{1+x^2/n^2}=\frac1{n^2+x^2}\le\frac1{n^2}$ : convergence normale de $\sum f_n'$ sur $\mathbb R$. La somme $S$ est donc de classe $\mathcal C^1$ sur $\mathbb R$, avec $S'(x)=\sum\frac1{n^2+x^2}$.

**3.** Non. Pour $x\ge0$ tous les termes sont positifs, donc
$$R_N(2N)=\sum_{n>N}\frac1n\arctan\frac{2N}n\ge\sum_{n=N+1}^{2N}\frac1n\arctan1\ge N\cdot\frac1{2N}\cdot\frac\pi4=\frac\pi8.$$
Ainsi $\sup_{\mathbb R_+}|R_N|\ge\frac\pi8\not\to0$ : pas de convergence uniforme sur $\mathbb R_+$. (Elle est uniforme sur tout $[0,A]$ : $|R_N(x)|\le A\sum_{n>N}\frac1{n^2}$. Et $S(x)\to+\infty$ quand $x\to+\infty$, alors que chaque somme partielle est bornée.)
""", r"$S\in\mathcal C^1(\mathbb R)$ ; convergence non uniforme sur $\mathbb R_+$ ($R_N(2N)\ge\pi/8$).")

c("m-ccs-03",
r"La loi faible des grands nombres découle de l'inégalité de Bienaymé-Tchebychev appliquée à $S_n/n$.",
r"Écris $X_k\equiv X_{k-1}+U_k\pmod{10}$ : l'application $(U_0,\dots,U_n)\mapsto(X_0,\dots,X_n)$ est une bijection de $\{0,\dots,9\}^{n+1}$.",
r"Une bijection transporte la loi uniforme sur la loi uniforme ; la loi uniforme sur un produit est le produit des lois uniformes.",
r"""
**1. Loi faible.** Soit $(Y_k)$ i.i.d. de variance finie $\sigma^2$, d'espérance $m$, et $\bar Y_n=\frac1n\sum_{k=1}^nY_k$. Par linéarité et indépendance, $E(\bar Y_n)=m$ et $V(\bar Y_n)=\frac{\sigma^2}n$. Par Bienaymé-Tchebychev, pour $\varepsilon>0$,
$$P(|\bar Y_n-m|\ge\varepsilon)\le\frac{\sigma^2}{n\varepsilon^2}\xrightarrow[n\to\infty]{}0.$$

**2.** On a $X_0=U_0$ et $X_k\equiv X_{k-1}+U_k\pmod{10}$. L'application
$$\Phi:(u_0,\dots,u_n)\mapsto(x_0,\dots,x_n),\quad x_k=(u_0+\dots+u_k)\bmod10$$
est une bijection de $\{0,\dots,9\}^{n+1}$, de réciproque $u_0=x_0$, $u_k=(x_k-x_{k-1})\bmod10$. Comme $(U_0,\dots,U_n)$ est uniforme sur cet ensemble (indépendance), pour tout $(x_0,\dots,x_n)$ :
$$P(X_0=x_0,\dots,X_n=x_n)=P\big((U_0,\dots,U_n)=\Phi^{-1}(x)\big)=10^{-(n+1)}.$$
Donc $(X_0,\dots,X_n)$ est uniforme sur $\{0,\dots,9\}^{n+1}$ : les $X_k$ sont **indépendantes**, toutes de **loi uniforme sur $\{0,\dots,9\}$**.

*Commentaire :* c'est surprenant car $X_n$ et $X_{n+1}$ sont construites à partir des mêmes $U_k$ ; l'indépendance vient de l'uniformité de l'incrément.
""", r"Les $X_n$ sont i.i.d. de loi uniforme sur $\{0,\dots,9\}$.")

c("m-ccs-05",
r"Remarque que si $z$ est racine de deux des polynômes $A,B,C=A+B$, il l'est du troisième : chaque racine de $ABC$ est racine d'un seul d'entre eux.",
r"$W=AB'-BA'=AC'-CA'=CB'-BC'$. Si $(X-z)^n$ divise $A$, il divise $A$ et $(X-z)^{n-1}$ divise $A'$.",
r"Le produit $\prod(X-z)^{m_z-1}$ divise $W$ ; compare les degrés, puis majore $\deg W\le\deg A+\deg B-1$.",
r"""
On suppose $A,B$ non tous deux constants (sinon tout est trivial).

**1.** $\deg(A+B)\le\max(\deg A,\deg B)$ (les termes de degré supérieur ne peuvent que se compenser). Inégalité stricte : $A=X$, $B=1-X$, $A+B=1$.

**2.(a)** Si $z$ est racine de deux des trois polynômes, il l'est du troisième (car $C=A+B$), ce qui est exclu. Donc une racine $z$ de $ABC$ de multiplicité $n$ est racine d'exactement un des trois, avec multiplicité $n$. Or
$$W=AB'-BA'=AC'-CA'=CB'-BC'$$
(par exemple $AC'-CA'=A(A'+B')-(A+B)A'=AB'-BA'$). Si $(X-z)^n\mid A$, alors $(X-z)^{n-1}$ divise $A$ et $A'$, donc $W=AB'-BA'$. Idem pour $B$ ou $C$ avec l'écriture adaptée.

**(b)** $W\ne0$ : sinon $(A/B)'=0$ donne $A=\lambda B$, et $A,B$ auraient leurs racines en commun, donc seraient constants. Les $(X-z)^{m_z-1}$ ($z$ racine de $ABC$ de multiplicité $m_z$) sont premiers entre eux et divisent $W$, donc leur produit aussi :
$$\sum_z(m_z-1)=\deg A+\deg B+\deg C-\mu\le\deg W.$$

**(c)** $\deg W=\deg(AB'-BA')\le\deg A+\deg B-1$. Donc $\mu\ge\deg C+1$. Avec les écritures $W=AC'-CA'$ et $W=CB'-BC'$ : $\mu\ge\deg B+1$ et $\mu\ge\deg A+1$. Ainsi
$$\mu>\max(\deg A,\deg B,\deg C).$$
C'est le **théorème de Mason–Stothers** (analogue polynomial de la conjecture $abc$). Application : $X^n+Y^n=Z^n$ n'a pas de solution polynomiale non triviale pour $n\ge3$.
""", r"$\mu\ge\deg A+\deg B+\deg C-\deg W$, d'où $\mu>\max(\deg A,\deg B,\deg C)$.")

c("m-ccs-06",
r"Écris $f$ comme somme de série entière : $f(x)=\sum_{n\ge0}\frac{x^n}{(n+1)!}$.",
r"$f(0)=1\ne0$. Pour $|x|<1$, $|f(x)-1|\le e-2<1$ : écris $\frac1f=\sum_k(1-f)^k$ et justifie la sommation.",
r"Pour $R\le2\pi$ : si $g$ était développable sur un disque de rayon $>2\pi$, que se passerait-il au point $z=2i\pi$ ?",
r"""
**1.** $f$ est DSE en $0$ s'il existe $r>0$ et $(a_n)$ avec $f(x)=\sum a_nx^n$ sur $]-r,r[$. Exemple : $e^x=\sum\frac{x^n}{n!}$ sur $\mathbb R$.

**2.** $\frac{e^x-1}x\to1$ en $0$ : on prolonge par $f(0)=1$.

**3.** Pour tout $x$, $f(x)=\sum_{n\ge0}\frac{x^n}{(n+1)!}$ (rayon infini, valable aussi en $0$). Donc $f$ est $\mathcal C^\infty$ sur $\mathbb R$ et $f^{(n)}(0)=\frac{n!}{(n+1)!}=\frac1{n+1}$.

*$g=1/f$ est DSE avec $R\ge1$.* Écrivons $f=1-h$ avec $h(z)=-\sum_{n\ge1}\frac{z^n}{(n+1)!}$. Pour $|z|\le r<1$ : $\sum_{n\ge1}\frac{r^n}{(n+1)!}\le\sum_{n\ge1}\frac1{(n+1)!}=e-2<1$. Alors $\frac1f=\sum_{k\ge0}h^k$, et la famille double obtenue en développant chaque $h^k$ est sommable (majorée par $\sum_k(e-2)^k$ après passage aux modules). Par sommation par paquets, $g(z)=\sum_mb_mz^m$ pour $|z|<1$ : $g$ est DSE de rayon $R\ge1$.

**4.** Raisonnons sur $\mathbb C$ : $e^z-1=zf(z)$ pour tout $z$. Si $R>2\pi$, la série $G(z)=\sum b_mz^m$ est continue sur le disque ouvert de rayon $R$ et $G(z)f(z)=1$ (produit de Cauchy, identité vraie sur $]-1,1[$ donc sur le disque par unicité du développement). En $z=2i\pi$ : $f(2i\pi)=\frac{e^{2i\pi}-1}{2i\pi}=0$, donc $1=G(2i\pi)\cdot0$ : contradiction. Donc $R\le2\pi$.

(En fait $R=2\pi$ : $g(x)=\frac x{e^x-1}=\sum B_n\frac{x^n}{n!}$, les $B_n$ étant les nombres de Bernoulli.)
""", r"$f^{(n)}(0)=\frac1{n+1}$ ; $1\le R\le2\pi$ (en fait $R=2\pi$).")

c("m-ccs-07",
r"Pour l'unicité, considère la différence $w$ de deux solutions et étudie $E(t)=\int_0^Lw(x,t)^2dx$.",
r"$E'(t)=2\int_0^Lw\,\partial_tw=2\int_0^Lw\,\partial_x^2w$ : intègre par parties avec les conditions aux bords.",
r"Pour les solutions séparées, $\frac{\varphi''}\varphi=\frac{\psi'}\psi$ est une constante $-\lambda$ ; les conditions $\varphi(0)=\varphi(L)=0$ imposent $\lambda=(k\pi/L)^2$.",
r"""
**1.** Si $f_n\to f$ uniformément sur $[a,b]$ (les $f_n$ continues), alors $\int_a^bf_n\to\int_a^bf$ : en effet $f$ est continue et $\big|\int f_n-\int f\big|\le(b-a)\|f_n-f\|_\infty\to0$.

**2. Unicité.** Soit $w=u_1-u_2$ : $\partial_tw=\partial_x^2w$, $w(0,t)=w(L,t)=0$, $w(x,0)=0$. Posons $E(t)=\int_0^Lw^2dx$ ($w$ est $\mathcal C^2$ sur le compact : dérivation sous l'intégrale licite). Alors
$$E'(t)=2\int_0^Lw\,\partial_x^2w\,dx=2\big[w\,\partial_xw\big]_0^L-2\int_0^L(\partial_xw)^2dx=-2\int_0^L(\partial_xw)^2\le0.$$
$E$ est décroissante, positive, avec $E(0)=0$ : $E\equiv0$, donc $w\equiv0$ par continuité.

**3.(a)** Si $u=\varphi(x)\psi(t)$ est non nulle et solution : $\varphi\psi'=\varphi''\psi$, donc $\frac{\varphi''(x)}{\varphi(x)}=\frac{\psi'(t)}{\psi(t)}=-\lambda$ constante (là où ils ne s'annulent pas). Alors $\varphi''+\lambda\varphi=0$ avec $\varphi(0)=\varphi(L)=0$ :
- $\lambda\le0$ : seule la solution nulle ;
- $\lambda>0$ : $\varphi=\sin(\sqrt\lambda x)$ avec $\sqrt\lambda L=k\pi$.

Donc $u_k(x,t)=e^{-k^2\pi^2t/L^2}\sin\frac{k\pi x}L$ ($k\ge1$), à une constante près.

**(b)** Si $f(x)=\sum_{k\ge1}b_k\sin\frac{k\pi x}L$ avec $b_k=\frac2L\int_0^Lf(x)\sin\frac{k\pi x}Ldx$ (et par exemple $\sum|b_k|<\infty$), on propose
$$u(x,t)=\sum_{k\ge1}b_k\,e^{-k^2\pi^2t/L^2}\sin\frac{k\pi x}L.$$
Pour $t\ge t_0>0$, les facteurs $e^{-k^2\pi^2t/L^2}$ assurent la convergence normale de toutes les séries dérivées : $u$ est solution, et l'unicité montre que c'est **la** solution.
""", r"$u(x,t)=\sum b_ke^{-k^2\pi^2t/L^2}\sin\frac{k\pi x}L$ ; unicité par l'énergie $E(t)=\int w^2$.")

c("m-ccs-10",
r"Règle de d'Alembert : calcule $\frac{\binom{2n}n}{\binom{2n+2}{n+1}}$.",
r"Pour le rayon, applique d'Alembert au terme $\frac{2^{2n-1}}{n^2\binom{2n}n}x^{2n}$ : le rapport tend vers $x^2$.",
r"Montre que $y=\arcsin^2$ vérifie $(1-x^2)y''-xy'=2$, avec $y(0)=y'(0)=0$, et que $S$ vérifie la même équation (récurrence sur les coefficients).",
r"""
**1.** *D'Alembert* : si $u_n>0$ et $\frac{u_{n+1}}{u_n}\to\ell<1$, $\sum u_n$ converge (et diverge si $\ell>1$). Ici $\frac{\binom{2n}n}{\binom{2n+2}{n+1}}=\frac{(n+1)^2}{(2n+2)(2n+1)}\to\frac14$, donc pour $u_n=\frac1{n^p\binom{2n}n}$ : $\frac{u_{n+1}}{u_n}\to\frac14<1$. $A_p$ est bien défini pour tout $p$.

**2.** Avec $c_n=\frac{2^{2n-1}}{n^2\binom{2n}n}$ : $\frac{c_{n+1}}{c_n}=4\frac{n^2}{(n+1)^2}\cdot\frac{(n+1)^2}{(2n+2)(2n+1)}=\frac{4n^2}{(2n+2)(2n+1)}\to1$. Pour $x\ne0$, $\big|\frac{c_{n+1}x^{2n+2}}{c_nx^{2n}}\big|\to x^2$ : convergence si $|x|<1$, divergence si $|x|>1$. **Rayon $1$.**

En $x=\pm1$ : par Stirling, $\binom{2n}n\sim\frac{4^n}{\sqrt{\pi n}}$, donc $c_n\sim\frac{\sqrt\pi}{2n^{3/2}}$ : convergence normale sur $[-1,1]$, $S$ y est continue.

**3.** Soit $y=\arcsin^2$ sur $]-1,1[$ : $y'=\frac{2\arcsin x}{\sqrt{1-x^2}}$, donc $\sqrt{1-x^2}\,y'=2\arcsin x$ ; en dérivant : $\sqrt{1-x^2}\,y''-\frac{x}{\sqrt{1-x^2}}y'=\frac2{\sqrt{1-x^2}}$, soit
$$(1-x^2)y''-xy'=2,\qquad y(0)=y'(0)=0.$$
Pour $S=\sum_{n\ge1}c_nx^{2n}$, on calcule $(1-x^2)S''-xS'=\sum_n\big[(2n+2)(2n+1)c_{n+1}-(2n)^2c_n\big]x^{2n}+2c_1$, avec $c_1=1$ ; et la relation $\frac{c_{n+1}}{c_n}=\frac{4n^2}{(2n+2)(2n+1)}$ annule tous les crochets. Donc $S$ vérifie le même problème de Cauchy sur $]-1,1[$ (équation linéaire résolue en $y''$, coefficients continus) : $S=\arcsin^2$ sur $]-1,1[$, et sur $[-1,1]$ par continuité.

*Application* : $x=1$ donne $\sum_{n\ge1}\frac{2^{2n-1}}{n^2\binom{2n}n}=\frac{\pi^2}4$, soit $A_2=\sum\frac1{n^2\binom{2n}n}=\frac{\pi^2}{18}$.
""", r"Rayon 1 ; $S(x)=\arcsin^2x$ sur $[-1,1]$ ; en $x=1$ : $A_2=\pi^2/18$.")

c("m-ccs-11",
r"Calcule $f''+f$ en dérivant deux fois sous l'intégrale (pour $x>0$).",
r"Pour $g$, pose $u=x+t$ pour écrire $g(x)=\cos x\int_x^\infty\frac{\sin u}udu-\sin x\int_x^\infty\frac{\cos u}udu$, puis calcule $g''+g$.",
r"$h=f-g$ vérifie $h''+h=0$ : $h=\alpha\cos+\beta\sin$. Montre que $f$ et $g$ tendent vers $0$ en $+\infty$.",
r"""
**1.** *Convergence dominée* : si $f_n\to f$ simplement (presque partout) sur $I$ et $|f_n|\le\varphi$ intégrable, alors $f$ est intégrable et $\int_If_n\to\int_If$.

**2.** $\big|\frac{e^{-xt}}{1+t^2}\big|\le\frac1{1+t^2}$, intégrable sur $\mathbb R_+$ : $f$ est définie (et continue) sur $\mathbb R_+$.

**3.** *$f$* : continuité sur $\mathbb R_+$ par domination ci-dessus. Sur $[a,+\infty[$ ($a>0$), $\big|\partial_x^k\frac{e^{-xt}}{1+t^2}\big|\le\frac{t^ke^{-at}}{1+t^2}$ intégrable : $f$ est $\mathcal C^2$ sur $\mathbb R_+^*$ et
$$f''(x)+f(x)=\int_0^\infty\frac{(t^2+1)e^{-xt}}{1+t^2}dt=\int_0^\infty e^{-xt}dt=\frac1x.$$
*$g$* : avec $u=x+t$, $g(x)=\int_x^\infty\frac{\sin(u-x)}u\,du=\cos x\,\mathrm{Si}^*(x)-\sin x\,\mathrm{Ci}^*(x)$ où $\mathrm{Si}^*(x)=\int_x^\infty\frac{\sin u}udu$ et $\mathrm{Ci}^*(x)=\int_x^\infty\frac{\cos u}udu$ (convergentes, dérivées $-\frac{\sin x}x$ et $-\frac{\cos x}x$). Donc $g$ est $\mathcal C^2$ sur $\mathbb R_+^*$ et un calcul direct donne
$$g'(x)=-\sin x\,\mathrm{Si}^*-\cos x\,\mathrm{Ci}^*,\qquad g''(x)=-g(x)+\frac1x.$$
(La continuité de $g$ en $0$ vient de $g(x)=\cos x\,\mathrm{Si}^*(x)-\sin x\,\mathrm{Ci}^*(x)$, avec $\sin x\,\mathrm{Ci}^*(x)\sim-x\ln x\to0$.)

**4.** $h=f-g$ vérifie $h''+h=0$ sur $\mathbb R_+^*$, donc $h=\alpha\cos x+\beta\sin x$. Or $0\le f(x)\le\int_0^\infty e^{-xt}dt=\frac1x\to0$, et par intégration par parties $g(x)=\frac1x-\int_0^\infty\frac{\cos t}{(x+t)^2}dt$, d'où $|g(x)|\le\frac2x\to0$. Donc $h\to0$ en $+\infty$, ce qui impose $\alpha=\beta=0$. Ainsi $f=g$ sur $\mathbb R_+^*$, et en $0$ par continuité : $f(0)=\frac\pi2=g(0)=\int_0^\infty\frac{\sin t}tdt$.
""", r"$f$ et $g$ vérifient $y''+y=\frac1x$ et tendent vers $0$ : $f=g$.")

c("m-ccs-12",
r"$X_i$ suit une loi géométrique de paramètre $p$ : $E(X_i)=\frac1p$, $V(X_i)=\frac{1-p}{p^2}$.",
r"Les $X_i$ sont indépendantes : additionne espérances et variances.",
r"La fonction génératrice de $X$ est $\Big(\frac{ps}{1-qs}\Big)^N$ ; développe $(1-qs)^{-N}$ en série entière.",
r"""
Notons $q=1-p$.

**1.** $X_i\sim\mathcal G(p)$ : $P(X_i=k)=pq^{k-1}$ ($k\ge1$) — rang du premier succès — et $E(X_i)=\frac1p$.

**2.(a)** Les $X_i$ sont indépendantes de même loi :
$$E(X)=\frac Np,\qquad V(X)=N\frac q{p^2}.$$
**(b)** $G_{X_i}(s)=\sum_{k\ge1}pq^{k-1}s^k=\frac{ps}{1-qs}$ pour $|s|<\frac1q$. Par indépendance, $G_X=\prod G_{X_i}=\frac{p^Ns^N}{(1-qs)^N}$. Or $(1-u)^{-N}=\sum_{j\ge0}\binom{N+j-1}{j}u^j$, donc
$$G_X(s)=\sum_{j\ge0}\binom{N+j-1}{j}p^Nq^js^{N+j},\qquad P(X=k)=\binom{k-1}{N-1}p^Nq^{k-N}\quad(k\ge N).$$
C'est la **loi de Pascal** (binomiale négative) : $X$ est le rang du $N$-ième succès. Interprétation directe : les $k-1$ premiers essais contiennent $N-1$ succès et le $k$-ième est un succès.
""", r"$E(X)=\frac Np$, $V(X)=\frac{Nq}{p^2}$, $P(X=k)=\binom{k-1}{N-1}p^Nq^{k-N}$.")

c("m-ccs-14",
r"Pour 2(a), raisonne modulo 3 : quels sont les carrés modulo 3 ? Fais une descente infinie.",
r"Une matrice $M\in\mathcal S_2(\mathbb Q)$ a un polynôme caractéristique $X^2-tX+d$ à coefficients rationnels. Si $\sqrt2$ est racine, quelle est l'autre ?",
r"Il faut $t=0$ et $d=-2$ (resp. $-3$) : $M=\begin{pmatrix}a&b\\b&-a\end{pmatrix}$ avec $a^2+b^2=2$ (resp. $3$). Réduis au même dénominateur et utilise 2(a).",
r"""
**1.(a)** Le spectre est l'ensemble des racines de $\chi_M$ (dans le corps où l'on travaille) : $\lambda\in\operatorname{Sp}M\iff M-\lambda I$ non inversible $\iff\chi_M(\lambda)=0$.

**(b)** Écrire $p=\frac{a'}{c'}$, $q=\frac{b'}{c''}$, réduire au même dénominateur $c=c'c''$ puis diviser $a,b,c$ par leur pgcd.

**2.(a)** Les carrés modulo 3 sont $0$ et $1$. Si $x^2+y^2\equiv0\pmod3$, alors $x\equiv y\equiv0$. Supposons $(x,y,z)\ne0$ solution avec $|z|$ minimal (ou $\max(|x|,|y|,|z|)$ minimal). $3\mid x^2+y^2$ donne $x=3x'$, $y=3y'$, puis $9(x'^2+y'^2)=3z^2$, donc $3\mid z^2$, $z=3z'$ et $(x',y',z')$ est une solution plus petite : contradiction. **Seule solution : $(0,0,0)$.**

**(b)** Oui : $M=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ vérifie $\chi_M=X^2-2$, $\operatorname{Sp}M=\{\pm\sqrt2\}$.

**(c)** Non. Si $\sqrt3\in\operatorname{Sp}M$ avec $\chi_M=X^2-tX+d\in\mathbb Q[X]$, alors $3-t\sqrt3+d=0$ ; $\sqrt3\notin\mathbb Q$ impose $t=0$ et $d=-3$. Donc $M=\begin{pmatrix}p&q\\q&-p\end{pmatrix}$ avec $-p^2-q^2=-3$. Par 1(b), $p=\frac ac$, $q=\frac bc$ avec $a,b,c$ premiers entre eux dans leur ensemble, et $a^2+b^2=3c^2$, ce qui contredit 2(a) (car $c\ne0$).

**3.(a)** Soit $k\ge1$ entier. Par le théorème des quatre carrés de Lagrange, $k=a^2+b^2+c^2+d^2$. Soit $A\in\mathcal M_4(\mathbb Z)$ la matrice de la multiplication à gauche par le quaternion $a+bi+cj+dk$ : $AA^T=A^TA=kI_4$. Alors $N_k=\begin{pmatrix}0&A\\A^T&0\end{pmatrix}\in\mathcal S_8(\mathbb Q)$ vérifie $N_k^2=kI_8$. On pose, dans $(\mathbb Q^8)^{\otimes d}$ (taille $n=8^d$), $M_k=I\otimes\dots\otimes N_k\otimes\dots\otimes I$ ($N_k$ en $k$-ième position) : ces matrices sont symétriques, commutent deux à deux (elles agissent sur des facteurs différents) et $M_k^2=kI_n$.

**(b)** Écrivons $q_i=\frac{r_i}{s_i}=\frac{r_is_i}{s_i^2}$ avec $r_is_i\in\mathbb N^*$. Avec la construction précédente appliquée aux entiers $k_i=r_is_i$, les matrices $\frac1{s_i}M_{k_i}$ conviennent.
""", r"$x^2+y^2=3z^2\Rightarrow x=y=z=0$ ; $\sqrt2$ oui ($\begin{pmatrix}1&1\\1&-1\end{pmatrix}$), $\sqrt3$ non.")

c("m-ccs-15",
r"Passe au logarithme : $\ln f=\sum w_i\ln x_i$ avec $w_i=\alpha_i/\alpha$, $\sum w_i=1$.",
r"Calcule $\partial_if=f\frac{w_i}{x_i}$ et $\partial_{ij}f=f\Big(\frac{w_iw_j}{x_ix_j}-\delta_{ij}\frac{w_i}{x_i^2}\Big)$.",
r"Écris $H=fD^{-1}(ww^T-\operatorname{diag}(w))D^{-1}$ avec $D=\operatorname{diag}(x_i)$, et calcule le rang de $\operatorname{diag}(w)-ww^T=\operatorname{diag}(w)(I-\mathbf 1w^T)$.",
r"""
**1.** Sur $(\mathbb R_+^*)^n$, $f=\exp\big(\sum w_i\ln x_i\big)$ avec $w_i=\frac{\alpha_i}\alpha>0$, $\sum w_i=1$ : composée de fonctions $\mathcal C^\infty$, donc $\mathcal C^2$.

**2.** $\partial_if=f\frac{w_i}{x_i}$, puis
$$\partial_j\partial_if=f\frac{w_iw_j}{x_ix_j}-\delta_{ij}f\frac{w_i}{x_i^2}.$$
Avec $D=\operatorname{diag}(x_1,\dots,x_n)$ et $w=(w_i)$ :
$$H=f\,D^{-1}\big(ww^T-\operatorname{diag}(w)\big)D^{-1}.$$
$D^{-1}$ est inversible et $f>0$, donc $\operatorname{rg}H=\operatorname{rg}\big(\operatorname{diag}(w)-ww^T\big)$. Or, avec $\mathbf 1=(1,\dots,1)^T$,
$$\operatorname{diag}(w)-ww^T=\operatorname{diag}(w)\big(I_n-\mathbf 1w^T\big),$$
et $\operatorname{diag}(w)$ est inversible. $P=\mathbf 1w^T$ vérifie $P^2=\mathbf 1(w^T\mathbf 1)w^T=P$ : c'est un projecteur de rang 1, donc $I_n-P$ est un projecteur de rang $n-1$.

**Conclusion :** $\operatorname{rg}H=n-1$ (pour $n\ge1$).

*Interprétation :* $f$ est positivement homogène de degré 1, donc (Euler) $H(x)\,x=0$ : $x\in\ker H$. De plus $f$ est concave (moyenne géométrique pondérée), $H$ est négative, de noyau exactement $\mathbb Rx$.
""", r"$\operatorname{rg}H=n-1$ (noyau $\mathbb Rx$, par homogénéité).")

c("m-ccs-mi8",
r"Pour $M_5$, dessine les cas : le point 1 est libre, ou relié à un autre point qui sépare le cercle en deux arcs.",
r"Cette même décomposition donne la récurrence : si le point 1 est relié au point $k+2$, les $k$ points entre eux et les $n-1-k$ points restants sont indépendants.",
r"La récurrence se traduit par $G=1+xG+x^2G^2$ ; résous et identifie le rayon grâce à la singularité de $\sqrt{1-2x-3x^2}$.",
r"""
**2. Récurrence.** Considérons $n+1$ points numérotés sur le cercle. Soit le point $1$ n'est relié à aucun autre : il reste $M_n$ configurations. Soit il est relié au point $k+2$ ($0\le k\le n-1$) : aucune corde ne peut traverser cette corde, donc les $k$ points situés entre $1$ et $k+2$ et les $n-1-k$ points de l'autre côté forment des configurations indépendantes. D'où
$$M_{n+1}=M_n+\sum_{k=0}^{n-1}M_kM_{n-1-k}.$$

**1.** $M_0=M_1=1$, $M_2=2$, $M_3=4$, $M_4=9$, et $M_5=M_4+(M_0M_3+M_1M_2+M_2M_1+M_3M_0)=9+(4+2+2+4)=21$.

**3.** Numériquement $M_n\le3^n$ (vérification informatique), donc $R\ge\frac13$.

**4.** Pour $|x|<\frac13$, en multipliant la récurrence par $x^{n+1}$ et en sommant (produit de Cauchy) :
$$G(x)-1=x\,G(x)+x^2G(x)^2.$$

**5.** Pour $x\ne0$, $x^2G^2+(x-1)G+1=0$, de discriminant $(1-x)^2-4x^2=1-2x-3x^2=(1-3x)(1+x)$. Comme $G(0)=1$, on choisit la racine bornée en $0$ :
$$G(x)=\frac{1-x-\sqrt{(1-3x)(1+x)}}{2x^2}.$$
La singularité en $x=\frac13$ (racine carrée non dérivable) montre que $R=\frac13$ exactement. Ce sont les **nombres de Motzkin** ; on montre que $M_n\sim c\,\frac{3^n}{n^{3/2}}$.
""", r"$M_5=21$ ; $G(x)=\frac{1-x-\sqrt{1-2x-3x^2}}{2x^2}$, $R=\frac13$.")

# ======================== X-ENS ========================

c("x-g-1",
r"Un élément de $G$ a pour ordre $1$, $p$, $q$ ou $pq$. Il suffit de trouver un élément d'ordre $p$ et un d'ordre $q$.",
r"Si aucun élément n'est d'ordre $q$ ni $pq$, alors $x^p=e$ pour tout $x$ : $G$ est un $\mathbb Z/p\mathbb Z$-espace vectoriel. Quel est alors son cardinal ?",
r"Dans un groupe abélien, si $a$ et $b$ sont d'ordres premiers entre eux, l'ordre de $ab$ est le produit des ordres.",
r"""
Les ordres possibles d'un élément divisent $pq$ : $1,p,q,pq$. S'il existe un élément d'ordre $pq$, $G$ est cyclique. Supposons le contraire.

**Existence d'un élément d'ordre $q$.** Sinon, tout élément vérifie $x^p=e$. $G$ (noté additivement) est alors un $\mathbb Z/p\mathbb Z$-espace vectoriel de dimension finie $d$, donc $|G|=p^d$, ce qui contredit $q\mid|G|$. De même il existe un élément $b$ d'ordre $p$.

**Produit.** Soit $a$ d'ordre $q$ et $b$ d'ordre $p$. Comme $G$ est abélien, $(ab)^k=a^kb^k$. Si $(ab)^k=e$, alors $a^k=b^{-k}\in\langle a\rangle\cap\langle b\rangle=\{e\}$ (intersection de sous-groupes d'ordres premiers entre eux), donc $q\mid k$ et $p\mid k$, soit $pq\mid k$. Ainsi $ab$ est d'ordre $pq=|G|$ : $G$ est cyclique (contradiction avec l'hypothèse provisoire, qui était donc impossible).

**Conclusion :** $G\simeq\mathbb Z/pq\mathbb Z\simeq\mathbb Z/p\mathbb Z\times\mathbb Z/q\mathbb Z$ (lemme chinois).
""", r"Éléments d'ordres $p$ et $q$ existent ; leur produit est d'ordre $pq$.")

c("x-g-2",
r"Les ordres possibles sont $1,2,p,2p$. S'il existe un élément d'ordre $2p$, que dire de son carré ?",
r"Si aucun élément n'est d'ordre $p$ ni $2p$, tout élément vérifie $x^2=e$. Montre qu'alors $G$ est abélien.",
r"Un groupe abélien où $x^2=e$ pour tout $x$ est un $\mathbb F_2$-espace vectoriel : son cardinal est une puissance de 2.",
r"""
Les ordres possibles divisent $2p$ : $1,2,p,2p$.
- Si $x$ est d'ordre $2p$, alors $x^2$ est d'ordre $p$.
- Sinon, supposons qu'aucun élément ne soit d'ordre $p$. Alors $x^2=e$ pour tout $x$. Le groupe est abélien : $xy=(xy)^{-1}=y^{-1}x^{-1}=yx$. C'est un $\mathbb Z/2\mathbb Z$-espace vectoriel, donc $|G|=2^d$, et $2p=2^d$ impose $p=2$.

Pour $p=2$ ($|G|=4$), on cherche un élément d'ordre $2$ : les éléments $\ne e$ sont d'ordre $2$ ou $4$, et si $x$ est d'ordre $4$, $x^2$ est d'ordre $2$.

Dans tous les cas, $G$ contient un élément d'ordre $p$.

(C'est un cas particulier du **lemme de Cauchy** : si $p$ premier divise $|G|$, $G$ a un élément d'ordre $p$. Exemples : $\mathbb Z/2p\mathbb Z$ et le groupe diédral $D_p$.)
""", r"Sinon $x^2=e$ pour tout $x$, et $|G|$ serait une puissance de 2.")

c("x-a-1",
r"Pense à la série géométrique formelle : $(1-ba)^{-1}=\sum(ba)^k=1+b\Big(\sum(ab)^k\Big)a$.",
r"Cela suggère le candidat $1+b(1-ab)^{-1}a$.",
r"Vérifie par calcul direct que $(1-ba)\big(1+b(1-ab)^{-1}a\big)=1$, et de même à droite.",
r"""
*Heuristique* : formellement $(1-ba)^{-1}=\sum_k(ba)^k=1+b\big(\sum_k(ab)^k\big)a=1+b(1-ab)^{-1}a$.

Posons $c=(1-ab)^{-1}$ et $d=1+bca$. Alors
$$(1-ba)d=1-ba+bca-babca=1-ba+b(1-ab)ca=1-ba+ba=1,$$
car $(1-ab)c=1$. De même
$$d(1-ba)=1-ba+bca-bcaba=1-ba+bc(1-ab)a=1-ba+ba=1,$$
car $c(1-ab)=1$. Donc $1-ba$ est inversible, d'inverse $1+b(1-ab)^{-1}a$.

*Conséquence en algèbre linéaire* : pour $A\in\mathcal M_{n,m}$, $B\in\mathcal M_{m,n}$ et $\lambda\ne0$, $AB$ et $BA$ ont les mêmes valeurs propres non nulles (appliquer à $a=A/\lambda$, $b=B$).
""", r"$(1-ba)^{-1}=1+b(1-ab)^{-1}a$.")

c("x-ar-1",
r"Factorise $6n^2+5n+1$.",
r"$6n^2+5n+1=(2n+1)(3n+1)$. Il suffit qu'un des facteurs soit divisible par $p$.",
r"Pour $p\ne2$, $2$ est inversible modulo $p$ : résous $2n+1\equiv0$. Traite $p=2$ à part.",
r"""
On a $6n^2+5n+1=(2n+1)(3n+1)$.

- **$p=2$** : $n=1$ donne $3\cdot4=12\equiv0\pmod2$.
- **$p$ impair** : $2$ est inversible modulo $p$ ; soit $n\in\{0,\dots,p-1\}$ tel que $n\equiv-2^{-1}\pmod p$, par exemple $n=\frac{p-1}2$. Alors $2n+1=p\equiv0$, donc $p\mid6n^2+5n+1$.

Ainsi pour tout premier $p$, $6n^2+5n+1\equiv0\pmod p$ a une solution entière naturelle.

*Remarque :* l'énoncé est trivial grâce à la factorisation ; le piège à l'oral est de partir sur le discriminant ($25-24=1$, carré parfait !), ce qui mène d'ailleurs au même résultat.
""", r"$(2n+1)(3n+1)$ : $n=\frac{p-1}2$ si $p$ impair, $n=1$ si $p=2$.")

c("x-ar-2",
r"Dans le corps $\mathbb Z/p\mathbb Z$, un polynôme de degré $d$ a au plus $d$ racines.",
r"$X^{(p-1)/q}-1$ a au plus $\frac{p-1}q<p-1$ racines : il existe $x$ avec $x^{(p-1)/q}\ne1$. Considère $y=x^{(p-1)/q^\alpha}$.",
r"Décompose $p-1=\prod q_i^{\alpha_i}$ ; le produit d'éléments d'ordres $q_i^{\alpha_i}$ (premiers entre eux, groupe commutatif) a pour ordre $p-1$.",
r"""
$\mathbb F_p=\mathbb Z/p\mathbb Z$ est un corps et $\mathbb F_p^*$ est d'ordre $p-1$ : $x^{p-1}=1$ pour tout $x\in\mathbb F_p^*$.

**1–2.** Soit $q$ premier, $q^\alpha\mid p-1$. Le polynôme $X^{(p-1)/q}-1$ a au plus $\frac{p-1}q<p-1$ racines dans le corps $\mathbb F_p$ : il existe $x\in\mathbb F_p^*$ avec $x^{(p-1)/q}\ne1$. Posons $y=x^{(p-1)/q^\alpha}$. Alors
$$y^{q^\alpha}=x^{p-1}=1,\qquad y^{q^{\alpha-1}}=x^{(p-1)/q}\ne1.$$
L'ordre de $y$ divise $q^\alpha$ sans diviser $q^{\alpha-1}$ : il vaut $q^\alpha$. (La question 1 est le cas $\alpha=1$.)

**3.** Écrivons $p-1=\prod_{i=1}^rq_i^{\alpha_i}$ et choisissons $y_i$ d'ordre $q_i^{\alpha_i}$. Dans un groupe commutatif, si $a,b$ sont d'ordres $m,n$ premiers entre eux, $ab$ est d'ordre $mn$ (si $(ab)^k=1$, $a^k=b^{-k}\in\langle a\rangle\cap\langle b\rangle=\{1\}$). Par récurrence, $y=y_1\cdots y_r$ est d'ordre $p-1$ : $\mathbb F_p^*=\langle y\rangle$ est **cyclique**.

(Exemple : $3$ engendre $\mathbb F_7^*$ : $3,2,6,4,5,1$.)
""", r"$\mathbb F_p^*$ est cyclique (éléments d'ordre $q^\alpha$ puis produit).")

c("x-p-1",
r"Écris $\frac{P'}{P}=\sum_i\frac{m_i}{X-z_i}$ (décomposition en éléments simples).",
r"Si $w$ est racine de $P'$ mais pas de $P$ : $\sum\frac{m_i}{w-z_i}=0$. Multiplie numérateur et dénominateur par les conjugués.",
r"Pour la question 2, applique la question 1 à $P-c$ : si toutes ses racines étaient dans le demi-plan fermé complémentaire de $H_1$, les racines de $P'$ y seraient aussi.",
r"""
**1.** Écrivons $P=a\prod_{i=1}^r(X-z_i)^{m_i}$. Alors $\frac{P'}P=\sum_i\frac{m_i}{X-z_i}$. Soit $w$ une racine de $P'$. Si $P(w)=0$, $w$ est l'un des $z_i$. Sinon
$$0=\sum_i\frac{m_i}{w-z_i}=\sum_i\frac{m_i(\bar w-\bar z_i)}{|w-z_i|^2}.$$
En conjuguant : $\sum_i\lambda_i(w-z_i)=0$ avec $\lambda_i=\frac{m_i}{|w-z_i|^2}>0$, d'où
$$w=\frac{\sum\lambda_iz_i}{\sum\lambda_i},$$
barycentre à coefficients positifs des $z_i$ : $w$ est dans l'enveloppe convexe des racines de $P$ (**théorème de Gauss-Lucas**).

**2.** Soit $c\in\mathbb C$ et $Q=P-c$ (non constant, $Q'=P'$). Soit $K=\mathbb C\setminus H_1$, demi-plan fermé, convexe. Si toutes les racines de $Q$ étaient dans $K$, leur enveloppe convexe y serait aussi, et par la question 1 toutes les racines de $Q'=P'$ aussi : contradiction avec l'existence d'une racine de $P'$ dans $H_1$. Donc $Q$ a une racine $z\in H_1$, i.e. $P(z)=c$. Ainsi $P(H_1)=\mathbb C$.
""", r"Les racines de $P'$ sont des barycentres à poids positifs des racines de $P$.")

c("x-al-1",
r"$\operatorname{Im}(a+b)\subset\operatorname{Im}a+\operatorname{Im}b$ ; pour l'autre sens, écris $a=(a+b)+(-b)$.",
r"Pour l'équivalence, si $\operatorname{rg}(a+b)=\operatorname{rg}a+\operatorname{rg}b$, montre $\operatorname{Im}a\cap\operatorname{Im}b=\{0\}$ puis $\ker(a+b)=\ker a\cap\ker b$ et compte les dimensions.",
r"Pour Sylvester, applique le théorème du rang à la restriction de $a$ à $\operatorname{Im}b$.",
r"""
**1.** $\operatorname{Im}(a+b)\subset\operatorname{Im}a+\operatorname{Im}b$, donc $\operatorname{rg}(a+b)\le\operatorname{rg}a+\operatorname{rg}b$. Avec $a=(a+b)+(-b)$ : $\operatorname{rg}a\le\operatorname{rg}(a+b)+\operatorname{rg}b$, et symétriquement : $\operatorname{rg}(a+b)\ge|\operatorname{rg}a-\operatorname{rg}b|$.

**2. ($\Leftarrow$)** Supposons $\operatorname{Im}a\cap\operatorname{Im}b=\{0\}$ et $\ker a+\ker b=E$. Soit $y=a(x)$ ; écrivons $x=k_a+k_b$ ($k_a\in\ker a$, $k_b\in\ker b$) : $y=a(k_b)=(a+b)(k_b)\in\operatorname{Im}(a+b)$. De même $\operatorname{Im}b\subset\operatorname{Im}(a+b)$. Donc $\operatorname{Im}(a+b)=\operatorname{Im}a\oplus\operatorname{Im}b$ et les rangs s'ajoutent.

**($\Rightarrow$)** $\operatorname{rg}a+\operatorname{rg}b=\operatorname{rg}(a+b)\le\dim(\operatorname{Im}a+\operatorname{Im}b)\le\operatorname{rg}a+\operatorname{rg}b$ : égalités, donc $\operatorname{Im}a\cap\operatorname{Im}b=\{0\}$. Alors $(a+b)(x)=0\Rightarrow a(x)=-b(x)\in\operatorname{Im}a\cap\operatorname{Im}b$, d'où $\ker(a+b)=\ker a\cap\ker b$, de dimension $n-\operatorname{rg}a-\operatorname{rg}b$. Par Grassmann,
$$\dim(\ker a+\ker b)=(n-\operatorname{rg}a)+(n-\operatorname{rg}b)-(n-\operatorname{rg}a-\operatorname{rg}b)=n.$$

**3.** $\operatorname{Im}(ab)\subset\operatorname{Im}a$ et $\operatorname{Im}(ab)=a(\operatorname{Im}b)$ de dimension $\le\operatorname{rg}b$ : $\operatorname{rg}(ab)\le\min(\operatorname{rg}a,\operatorname{rg}b)$. Par le théorème du rang appliqué à $a_{|\operatorname{Im}b}$ :
$$\operatorname{rg}(ab)=\operatorname{rg}b-\dim(\ker a\cap\operatorname{Im}b)\ge\operatorname{rg}b-\dim\ker a=\operatorname{rg}a+\operatorname{rg}b-n.$$
""", r"$\operatorname{rg}a+\operatorname{rg}b-n\le\operatorname{rg}(ab)\le\min(\operatorname{rg}a,\operatorname{rg}b)$.")

c("x-al-2",
r"Première méthode : montre que toute valeur propre $\lambda$ vérifie $|\lambda|\le1$ en regardant la coordonnée de module maximal d'un vecteur propre.",
r"Pour le cas d'égalité, développe $\det M$ par multilinéarité selon les lignes : chaque ligne est combinaison convexe des $e_j^T$.",
r"$|\det M|\le\sum_{\sigma\in S_n}\prod m_{i\sigma(i)}\le\sum_{\text{toutes } \sigma}\prod m_{i\sigma(i)}=1$ : l'égalité impose que les applications non injectives donnent des produits nuls.",
r"""
**1.** Par multilinéarité selon les lignes, avec $L_i=\sum_jm_{ij}e_j^T$ :
$$\det M=\sum_{\sigma:[\![1,n]\!]\to[\![1,n]\!]}\Big(\prod_im_{i\sigma(i)}\Big)\det(e_{\sigma(1)},\dots,e_{\sigma(n)})=\sum_{\sigma\in S_n}\varepsilon(\sigma)\prod_im_{i\sigma(i)},$$
les applications non injectives donnant un déterminant nul. Donc
$$|\det M|\le\sum_{\sigma\in S_n}\prod_im_{i\sigma(i)}\le\sum_{\text{toutes }\sigma}\prod_im_{i\sigma(i)}=\prod_{i=1}^n\Big(\sum_jm_{ij}\Big)=1.$$
(Autre méthode : si $MX=\lambda X$ et $|x_i|=\max|x_j|$, alors $|\lambda||x_i|\le\sum_jm_{ij}|x_j|\le|x_i|$, donc $|\lambda|\le1$ et $|\det M|=\prod|\lambda|\le1$.)

**2. Égalité.** Si $|\det M|=1$, la seconde inégalité est une égalité : pour toute application **non injective** $\sigma$, $\prod_im_{i\sigma(i)}=0$. Supposons qu'une ligne $i$ ait deux coefficients $>0$, en colonnes $j\ne k$. Choisissons dans chaque ligne $r$ une colonne $c_r$ de coefficient $>0$, avec $c_i=j$. Si $r\mapsto c_r$ n'est pas injective, contradiction. Sinon c'est une permutation, et $k=c_{r'}$ pour un $r'\ne i$ : en remplaçant $c_i$ par $k$, on obtient une application non injective de produit $>0$ : contradiction. Donc chaque ligne a un seul coefficient non nul, égal à 1, et les positions forment une permutation (sinon $\det M=0$).

**Conclusion :** $|\det M|=1\iff M$ est une **matrice de permutation**.
""", r"$|\det M|\le1$, avec égalité ssi $M$ est une matrice de permutation.")

c("x-al-3",
r"Commence par $A$ inversible : $\tilde A=\det(A)A^{-1}$.",
r"Si $A$ a pour valeurs propres $\lambda_1,\dots,\lambda_n$ (inversible), $\tilde A$ a pour valeurs propres $\frac{\det A}{\lambda_i}=\prod_{j\ne i}\lambda_j$.",
r"Étends par densité : le polynôme caractéristique de $\tilde A$ dépend continûment de $A$ et $\prod_i\big(X-\prod_{j\ne i}\lambda_j\big)$ est un polynôme symétrique en les $\lambda_i$.",
r"""
Notons $\lambda_1,\dots,\lambda_n$ les valeurs propres de $A$ (avec multiplicité). **Résultat :** les valeurs propres de $\tilde A$ sont les $\mu_i=\prod_{j\ne i}\lambda_j$, $1\le i\le n$.

**Cas $A$ inversible.** $A\tilde A=\det(A)I_n$, donc $\tilde A=\det(A)A^{-1}$, de valeurs propres $\frac{\det A}{\lambda_i}=\prod_{j\ne i}\lambda_j$.

**Cas général (densité).** Les coefficients de $Q_A=\prod_i(X-\mu_i)$ sont des polynômes symétriques en $\lambda_1,\dots,\lambda_n$, donc des polynômes en les coefficients de $\chi_A$, donc en les coefficients de $A$ : $A\mapsto Q_A$ est continue. De même $A\mapsto\chi_{\tilde A}$ est continue (les coefficients de $\tilde A$ sont des mineurs). Les deux coïncident sur $GL_n(\mathbb C)$, dense : $\chi_{\tilde A}=Q_A$ pour toute $A$.

**Lecture selon le rang.**
- $\operatorname{rg}A=n$ : $\operatorname{Sp}\tilde A=\{\det A/\lambda_i\}$.
- $\operatorname{rg}A=n-1$ : $\tilde A$ est de rang 1 ; ses valeurs propres sont $0$ (multiplicité $n-1$) et $\operatorname{Tr}\tilde A=\prod_{\lambda_j\ne0}\lambda_j$ si $0$ est valeur propre simple, et $0$ sinon (alors $\tilde A$ est nilpotente).
- $\operatorname{rg}A\le n-2$ : $\tilde A=0$.
""", r"$\operatorname{Sp}\tilde A=\big\{\prod_{j\ne i}\lambda_j,\ 1\le i\le n\big\}$.")

c("x-al-4",
r"Si $n>m$, compare le rang de $C=AB$ à $m$.",
r"Écris les colonnes de $C$ : $C_j=\sum_kB_{kj}A_k$ ($A_k$ colonnes de $A$), et développe $\det C$ par multilinéarité.",
r"Regroupe les termes selon l'ensemble d'indices $\{k_1<\dots<k_n\}$ atteint ; la somme sur les permutations reconstitue un mineur de $B$.",
r"""
**$n>m$** : $\operatorname{rg}C\le\operatorname{rg}A\le m<n$, donc $\det C=0$.

**$n\le m$.** Notons $A_1,\dots,A_m$ les colonnes de $A$. La $j$-ième colonne de $C$ est $C_j=\sum_{k=1}^mB_{kj}A_k$. Par multilinéarité du déterminant :
$$\det C=\sum_{\kappa:[\![1,n]\!]\to[\![1,m]\!]}\Big(\prod_{j=1}^nB_{\kappa(j)j}\Big)\det\big(A_{\kappa(1)},\dots,A_{\kappa(n)}\big).$$
Les $\kappa$ non injectives donnent un déterminant nul. Une $\kappa$ injective s'écrit de façon unique $\kappa(j)=k_{\sigma(j)}$ avec $k_1<\dots<k_n$ et $\sigma\in S_n$, et $\det(A_{\kappa(1)},\dots)=\varepsilon(\sigma)\det(A_{k_1},\dots,A_{k_n})$. Donc
$$\det C=\sum_{k_1<\dots<k_n}\det(A_{k_1},\dots,A_{k_n})\sum_{\sigma\in S_n}\varepsilon(\sigma)\prod_jB_{k_{\sigma(j)}j}=\sum_{k_1<\dots<k_n}A\binom{1\cdots n}{k_1\cdots k_n}B\binom{k_1\cdots k_n}{1\cdots n}.$$

*Application classique* : avec $B=A^T$ réelle, $\det(AA^T)=\sum(\text{mineurs maximaux de }A)^2\ge0$ (identité de Lagrange pour $n=2$, $m=3$ : $\|u\|^2\|v\|^2-(u\cdot v)^2=\|u\wedge v\|^2$).
""", r"$\det(AB)=\sum_{k_1<\dots<k_n}A\binom{1\cdots n}{k}\,B\binom{k}{1\cdots n}$, nul si $n>m$.")

c("x-r-1",
r"$A\mathbf 1=\mathbf 1$ pour $\mathbf 1=(1,\dots,1)^T$. Pour la dimension du noyau, prends $X$ réel avec $AX=X$ et regarde une coordonnée maximale.",
r"$x_i=\sum_ja_{ij}x_j\le x_i$ avec égalité seulement si tous les $x_j$ sont égaux à $x_i$ (car $a_{ij}>0$).",
r"Si $|\lambda|=1$, reprends l'argument avec les modules : le cas d'égalité dans l'inégalité triangulaire impose des $x_j$ égaux.",
r"""
**1.** $A\mathbf 1=\mathbf 1$ (sommes de lignes égales à 1) : $1\in\operatorname{Sp}A$. Soit $X\in\mathbb R^n$ avec $AX=X$ et $i$ tel que $x_i=\max_jx_j$. Alors
$$x_i=\sum_ja_{ij}x_j\le\sum_ja_{ij}x_i=x_i,$$
avec égalité seulement si $x_j=x_i$ pour tout $j$ (car tous les $a_{ij}>0$). Donc $X\in\mathbb R\mathbf 1$. Pour $X$ complexe, $A$ étant réelle, $\operatorname{Re}X$ et $\operatorname{Im}X$ sont aussi fixes : $\ker(A-I_n)=\mathbb C\mathbf 1$, de dimension 1.

**2.** Soit $AX=\lambda X$, $X\ne0$, et $i$ tel que $|x_i|=\max_j|x_j|$. Alors
$$|\lambda||x_i|=\Big|\sum_ja_{ij}x_j\Big|\le\sum_ja_{ij}|x_j|\le|x_i|,$$
donc $|\lambda|\le1$. Si $|\lambda|=1$, toutes les inégalités sont des égalités : $|x_j|=|x_i|$ pour tout $j$ (car $a_{ij}>0$), et l'égalité dans l'inégalité triangulaire impose que les $a_{ij}x_j$ soient positivement liés, donc tous les $x_j$ ont même argument : $x_j=x_i$ pour tout $j$. Alors $X\in\mathbb C\mathbf 1$ et $\lambda=1$.

(C'est le cas particulier « matrices stochastiques » du **théorème de Perron-Frobenius** ; il implique que $A^k\to\mathbf 1\pi^T$ : convergence d'une chaîne de Markov vers sa loi stationnaire.)
""", r"$\ker(A-I)=\mathbb C\mathbf 1$ ; $|\lambda|\le1$ et $|\lambda|=1\Rightarrow\lambda=1$.")

c("x-r-2",
r"$A^p$ diagonalisable inversible est annulée par $\prod_k(X-\mu_k)$ avec des $\mu_k$ distincts et **non nuls**.",
r"Alors $A$ est annulée par $\prod_k(X^p-\mu_k)$. Ce polynôme est-il à racines simples ?",
r"Pour le cas non inversible, cherche une matrice nilpotente non nulle.",
r"""
$A^p$ est diagonalisable : elle est annulée par $\prod_{k=1}^r(X-\mu_k)$, $\mu_k$ distincts. Comme $A$ est inversible, $A^p$ aussi et les $\mu_k\ne0$. Donc $A$ est annulée par
$$Q=\prod_{k=1}^r(X^p-\mu_k).$$
- Pour $\mu\ne0$, $X^p-\mu$ a $p$ racines distinctes (une racine $z$ vérifie $z\ne0$, donc $pz^{p-1}\ne0$ : racine simple).
- Pour $\mu_k\ne\mu_l$, $X^p-\mu_k$ et $X^p-\mu_l$ n'ont pas de racine commune ($z^p$ ne peut valoir deux valeurs).

$Q$ est scindé sur $\mathbb C$ à racines simples et annule $A$ : $A$ est diagonalisable.

**Sans inversibilité, c'est faux** : $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ vérifie $A^2=0$ (diagonalisable) sans être diagonalisable. Le problème vient de $\mu=0$ : $X^p$ a une racine multiple.
""", r"$A$ annulée par $\prod(X^p-\mu_k)$, à racines simples car $\mu_k\ne0$ ; contre-exemple nilpotent sinon.")

c("x-r-3",
r"$\operatorname{Tr}(A^k)=\sum_im_i\lambda_i^k$ (valeurs propres distinctes $\lambda_i$, multiplicités $m_i$).",
r"Raisonne par l'absurde avec $\rho=\max|\lambda_i|\ge1$ : divise par $\rho^k$ et ne garde que les valeurs propres de module $\rho$.",
r"Montre qu'une suite $u_k=\sum_jc_jz_j^k$ ($z_j$ distincts de module 1, $c_j\ne0$) ne tend pas vers 0 : calcule la moyenne de Cesàro de $|u_k|^2$.",
r"""
Soient $\lambda_1,\dots,\lambda_r$ les valeurs propres distinctes non nulles de $A$, de multiplicités $m_i$ : $\operatorname{Tr}(A^k)=\sum_im_i\lambda_i^k$ (trigonalisation).

Supposons $\rho=\max|\lambda_i|\ge1$ et notons $J=\{i:|\lambda_i|=\rho\}$, $\lambda_i=\rho z_i$ ($|z_i|=1$, distincts). Alors
$$\frac{\operatorname{Tr}(A^k)}{\rho^k}=\underbrace{\sum_{i\in J}m_iz_i^k}_{u_k}+\sum_{i\notin J}m_i\Big(\frac{\lambda_i}\rho\Big)^k.$$
Le membre de gauche tend vers $0$ (car $\rho\ge1$) et la seconde somme aussi : donc $u_k\to0$.

**Lemme :** $u_k\not\to0$. En effet
$$\frac1N\sum_{k=0}^{N-1}|u_k|^2=\sum_{i,j\in J}m_im_j\frac1N\sum_{k=0}^{N-1}(z_i\bar z_j)^k.$$
Pour $i=j$ la moyenne vaut 1 ; pour $i\ne j$, $w=z_i\bar z_j\ne1$ est de module 1 et $\big|\frac1N\sum_kw^k\big|=\frac{|1-w^N|}{N|1-w|}\le\frac2{N|1-w|}\to0$. Donc la moyenne tend vers $\sum_{i\in J}m_i^2>0$, ce qui contredit $u_k\to0$ (Cesàro).

**Conclusion :** toutes les valeurs propres de $A$ sont de module $<1$ (et réciproquement, on aurait alors $A^k\to0$).
""", r"Moyenne de Cesàro de $|u_k|^2$ $\to\sum m_i^2>0$ : contradiction si $\rho\ge1$.")

c("x-r-4",
r"$\exp(N)$ est une somme finie si $N$ est nilpotente. Pour l'inverse, pense à $\log(I+M)=\sum_{k=1}^{n-1}\frac{(-1)^{k+1}}kM^k$.",
r"Les identités $\exp(\log(1+x))=1+x$ et $\log(\exp x)=x$ entre séries formelles se transportent aux matrices nilpotentes (toutes les sommes sont finies).",
r"Pour la question 2 : $\det(\exp M)=e^{\operatorname{Tr}M}\ne0$. Réciproquement, décompose $M\in GL_n(\mathbb C)$ sur ses sous-espaces caractéristiques : $M=\lambda(I+N/\lambda)$ sur chaque bloc.",
r"""
**1.** Si $N^n=0$, $\exp N=\sum_{k<n}\frac{N^k}{k!}=I+N'$ avec $N'=N\big(\sum_{k\ge1}\frac{N^{k-1}}{k!}\big)$ nilpotente (produit de matrices qui commutent, dont une nilpotente) : $\exp N$ est unipotente. Pour $M$ nilpotente, posons $\log(I+M)=\sum_{k=1}^{n-1}\frac{(-1)^{k+1}}kM^k$, nilpotente.

Dans l'anneau des séries formelles $\mathbb Q[[x]]$, on a $\exp(\log(1+x))=1+x$ et $\log(\exp(x)-1+1)=x$ (sans terme constant, la composition est licite). En substituant à $x$ une matrice nilpotente (toutes les séries deviennent des sommes finies, et la substitution respecte sommes, produits et compositions), on obtient $\exp(\log(I+M))=I+M$ et $\log(\exp N)=N$. Donc $\exp$ est une **bijection** des nilpotentes sur les unipotentes, de réciproque $\log$.

**2.** **$\exp(\mathcal M_n(\mathbb C))=GL_n(\mathbb C)$.**
- $\subset$ : $\exp(M)\exp(-M)=I_n$.
- $\supset$ : soit $M\in GL_n(\mathbb C)$. Par le lemme des noyaux, $\mathbb C^n=\bigoplus_\lambda\ker(M-\lambda I)^{m_\lambda}$, sous-espaces stables, et sur chacun $M=\lambda I+N_\lambda=\lambda(I+N_\lambda/\lambda)$ avec $N_\lambda$ nilpotente et $\lambda\ne0$. Choisissons $\mu\in\mathbb C$ avec $e^\mu=\lambda$ et $L_\lambda=\log(I+N_\lambda/\lambda)$. Comme $\mu I$ et $L_\lambda$ commutent : $\exp(\mu I+L_\lambda)=e^\mu(I+N_\lambda/\lambda)=M$ sur ce bloc. En recollant les blocs, $M=\exp(B)$.

*Remarque :* sur $\mathbb R$, $\exp(\mathcal M_n(\mathbb R))\ne GL_n(\mathbb R)$ ($\det>0$, et même $\operatorname{diag}(-1,-2)\notin\exp(\mathcal M_2(\mathbb R))$).
""", r"$\exp$ : nilpotentes $\leftrightarrow$ unipotentes ; $\exp(\mathcal M_n(\mathbb C))=GL_n(\mathbb C)$.")

c("x-r-5",
r"Une matrice $M$ d'ordre fini est diagonalisable sur $\mathbb C$, à valeurs propres racines de l'unité.",
r"$\chi_M$ est à coefficients entiers et toutes ses racines sont de module 1 : majore ses coefficients.",
r"Il n'y a donc qu'un nombre fini de polynômes caractéristiques possibles, donc un nombre fini de racines de l'unité possibles : prends le ppcm de leurs ordres.",
r"""
Soit $M\in GL_n(\mathbb Z)$ avec $M^m=I_n$. $M$ est annulée par $X^m-1$, à racines simples : $M$ est diagonalisable sur $\mathbb C$, de valeurs propres des racines de l'unité.

**Nombre fini de polynômes caractéristiques.** $\chi_M=X^n-\sigma_1X^{n-1}+\dots+(-1)^n\sigma_n$, où $\sigma_k$ est la $k$-ième fonction symétrique élémentaire des valeurs propres. Comme celles-ci sont de module 1, $|\sigma_k|\le\binom nk$. Les coefficients sont **entiers** et bornés : il n'y a qu'un nombre fini de polynômes caractéristiques possibles, donc un ensemble fini $\mathcal R$ de racines de l'unité pouvant apparaître comme valeurs propres.

**Conclusion.** Soit $r$ le ppcm des ordres des éléments de $\mathcal R$ (il ne dépend que de $n$). Pour toute $M$ d'ordre fini, $M=PDP^{-1}$ avec $D$ diagonale à coefficients dans $\mathcal R$, donc $D^r=I_n$ et $M^r=I_n$.

*Précision* (hors programme) : une racine primitive $d$-ième de l'unité est de degré $\varphi(d)$ sur $\mathbb Q$, donc les ordres possibles vérifient $\varphi(d)\le n$ ; pour $n=2$, les ordres possibles sont $1,2,3,4,6$ et $r=12$.
""", r"Coefficients de $\chi_M$ entiers et bornés $\Rightarrow$ nombre fini de valeurs propres possibles ; $r$ = ppcm des ordres.")

c("x-an-1",
r"Dans $\int_0^{f(a)}f^{-1}(t)\,dt$, pose $t=f(u)$ et intègre par parties.",
r"Pour l'inégalité, distingue $b\le f(a)$ et $b\ge f(a)$ ; dans le premier cas, pose $c=f^{-1}(b)\le a$ et minore $\int_c^af$.",
r"Pour $f$ seulement continue, montre directement que $F(c)=\int_0^cf+\int_0^{f(c)}f^{-1}-cf(c)$ a une dérivée nulle en encadrant $F(c+h)-F(c)$.",
r"""
**1. Identité.** Avec $t=f(u)$ ($f$ est une bijection $\mathcal C^1$ croissante de $\mathbb R_+$ sur $\mathbb R_+$) :
$$\int_0^{f(a)}f^{-1}(t)dt=\int_0^auf'(u)du=af(a)-\int_0^af(u)du.$$

**Inégalité de Young.** Soit $b>0$ et $c=f^{-1}(b)$.
- Si $c\le a$ : sur $[c,a]$, $f\ge f(c)=b$, donc $\int_c^af\ge(a-c)b$ ; avec l'identité en $c$ : $\int_0^af+\int_0^bf^{-1}\ge\big(cb-\int_0^cf\big)+\int_0^cf+(a-c)b=ab$.
- Si $c>a$ : sur $[f(a),b]$, $f^{-1}\ge a$, donc $\int_0^af+\int_0^bf^{-1}\ge af(a)+a(b-f(a))=ab$.

Égalité ssi $b=f(a)$. (Exemple : $f(t)=t^{p-1}$ donne $ab\le\frac{a^p}p+\frac{b^q}q$ avec $\frac1p+\frac1q=1$.)

**2. $f$ continue strictement croissante.** Soit $F(c)=\int_0^cf+\int_0^{f(c)}f^{-1}-cf(c)$ et $\Delta=f(c+h)-f(c)$ ($h>0$). Par croissance :
$$hf(c)\le\int_c^{c+h}f\le hf(c+h),\qquad c\Delta\le\int_{f(c)}^{f(c+h)}f^{-1}\le(c+h)\Delta.$$
On en déduit $|F(c+h)-F(c)|\le h\Delta=o(h)$ (continuité de $f$) ; de même à gauche. Donc $F'=0$, $F(0)=0$ : $F\equiv0$. L'identité vaut toujours, et la preuve de l'inégalité ci-dessus n'utilise que l'identité et la monotonie.
""", r"$\int_0^af+\int_0^{f(a)}f^{-1}=af(a)$ et $ab\le\int_0^af+\int_0^bf^{-1}$.")

c("x-an-2",
r"Une intégration par parties donne $I_{n+2}=\frac{n+1}{n+2}I_n$.",
r"Montre que $(n+1)I_{n+1}I_n$ est constant, égal à $\frac\pi2$.",
r"$(I_n)$ décroît, donc $\frac{n+1}{n+2}=\frac{I_{n+2}}{I_n}\le\frac{I_{n+1}}{I_n}\le1$ : $I_{n+1}\sim I_n$.",
r"""
**Relation de récurrence.** Par parties ($u=\cos^{n+1}$, $v'=\cos$) : $I_{n+2}=(n+1)\int_0^{\pi/2}\cos^n\sin^2=(n+1)(I_n-I_{n+2})$, d'où $I_{n+2}=\frac{n+1}{n+2}I_n$.

**Invariant.** $u_n=(n+1)I_{n+1}I_n$ vérifie $u_{n+1}=(n+2)I_{n+2}I_{n+1}=(n+1)I_nI_{n+1}=u_n$, donc $u_n=u_0=I_1I_0=\frac\pi2$.

**Équivalent.** $I_n>0$ décroît ($\cos^{n+1}\le\cos^n$ sur $[0,\pi/2]$), donc
$$\frac{n+1}{n+2}=\frac{I_{n+2}}{I_n}\le\frac{I_{n+1}}{I_n}\le1,$$
et $I_{n+1}\sim I_n$. Alors $\frac\pi2=(n+1)I_{n+1}I_n\sim nI_n^2$, d'où
$$I_n\sim\sqrt{\frac\pi{2n}}.$$

**Série.** $I_n^2\sim\frac\pi{2n}$ : par comparaison avec la série harmonique (termes positifs), $\sum I_n^2$ **diverge**.
""", r"$I_n\sim\sqrt{\frac\pi{2n}}$ ; $\sum I_n^2$ diverge.")

c("x-an-3",
r"Pour Dini, raisonne par l'absurde : s'il existe $\varepsilon$ et $x_n$ avec $f(x_n)-f_n(x_n)\ge\varepsilon$, extrais une sous-suite convergente (compacité).",
r"Pour 2, utilise la continuité uniforme de $f$ et une subdivision $t_0<\dots<t_p$ ; encadre $f_n(x)$ entre $f_n(t_k)$ et $f_n(t_{k+1})$.",
r"Pour 3, montre par récurrence $0\le p_n(x)\le p_{n+1}(x)\le\sqrt x$ à l'aide de $\sqrt x-p_{n+1}=(\sqrt x-p_n)\big(1-\frac{\sqrt x+p_n}2\big)$.",
r"""
**1. (Dini)** $g_n=f-f_n$ est continue, positive, décroissante en $n$, $g_n\to0$ simplement. Si la convergence n'était pas uniforme, il existerait $\varepsilon>0$ et $x_n$ avec $g_n(x_n)\ge\varepsilon$ pour une infinité de $n$ ; par Bolzano-Weierstrass, quitte à extraire, $x_{\varphi(n)}\to x$. Pour $m$ fixé et $\varphi(n)\ge m$ : $g_m(x_{\varphi(n)})\ge g_{\varphi(n)}(x_{\varphi(n)})\ge\varepsilon$, donc par continuité $g_m(x)\ge\varepsilon$ pour tout $m$ : contradiction avec $g_m(x)\to0$.

**2.** $f$ est croissante (limite de fonctions croissantes) et continue sur le segment, donc uniformément continue. Soit $\varepsilon>0$ et $a=t_0<\dots<t_p=b$ avec $f(t_{k+1})-f(t_k)\le\varepsilon$. Pour $n\ge N$, $|f_n(t_k)-f(t_k)|\le\varepsilon$ pour tout $k$. Si $x\in[t_k,t_{k+1}]$ :
$$f_n(x)\le f_n(t_{k+1})\le f(t_{k+1})+\varepsilon\le f(x)+2\varepsilon,\qquad f_n(x)\ge f_n(t_k)\ge f(t_k)-\varepsilon\ge f(x)-2\varepsilon.$$
D'où $\|f_n-f\|_\infty\le2\varepsilon$ : convergence uniforme.

**3.** On a $\sqrt x-p_{n+1}=(\sqrt x-p_n)\big(1-\frac{\sqrt x+p_n}2\big)$. Si $0\le p_n\le\sqrt x\le1$, le facteur est dans $[0,1]$, donc $0\le\sqrt x-p_{n+1}\le\sqrt x-p_n$ ; et $p_{n+1}-p_n=\frac{x-p_n^2}2\ge0$. Par récurrence ($p_0=0$) : $0\le p_n\le p_{n+1}\le\sqrt x$. La suite converge vers $\ell$ avec $\ell=\ell+\frac{x-\ell^2}2$, soit $\ell=\sqrt x$. Les $p_n$ sont des polynômes (continus), croissants en $n$, de limite continue : par Dini, **$p_n\to\sqrt{\cdot}$ uniformément sur $[0,1]$**.

(Utile pour prouver Weierstrass : $|t|=\sqrt{t^2}$ est limite uniforme de polynômes sur $[-1,1]$.)
""", r"Dini (compacité) ; $p_n\nearrow\sqrt x$ uniformément sur $[0,1]$.")

c("x-s-1",
r"Au voisinage de $0^+$, $f(x)<x$ : montre que la suite est décroissante, minorée par $0$, et identifie sa limite.",
r"Cherche $\beta$ tel que $u_{n+1}^\beta-u_n^\beta$ ait une limite finie non nulle : essaie $\beta=1-\alpha$.",
r"Avec $\beta=1-\alpha<0$, $u_{n+1}^{\beta}-u_n^{\beta}\to a(\alpha-1)$ : conclus par Cesàro.",
r"""
**1.** Comme $f(x)=x-ax^\alpha+o(x^\alpha)$ avec $a>0$, il existe $\eta>0$ tel que $0\le f(x)<x$ sur $]0,\eta]$. Si $0<u_0\le\eta$, par récurrence $0\le u_{n+1}<u_n\le\eta$ (si $u_n=0$ la suite est stationnaire nulle) : $(u_n)$ décroît, est minorée, converge vers $\ell\in[0,\eta]$ avec $f(\ell)=\ell$ (continuité), donc $\ell=0$.

**2.** Posons $\beta=1-\alpha<0$. Comme $u_n\to0^+$ :
$$u_{n+1}^\beta=u_n^\beta\big(1-au_n^{\alpha-1}+o(u_n^{\alpha-1})\big)^\beta=u_n^\beta\big(1-a\beta u_n^{\alpha-1}+o(u_n^{\alpha-1})\big),$$
donc $u_{n+1}^\beta-u_n^\beta=-a\beta+o(1)\to a(\alpha-1)>0$. Par le théorème de Cesàro, $\frac{u_n^\beta}n\to a(\alpha-1)$, soit
$$u_n\sim\big(a(\alpha-1)\,n\big)^{-\frac1{\alpha-1}}.$$

**3.** $\sin x=x-\frac{x^3}6+o(x^3)$ : $a=\frac16$, $\alpha=3$, donc $u_n\sim\sqrt{\frac3n}$.
$\ln(1+x)=x-\frac{x^2}2+o(x^2)$ : $a=\frac12$, $\alpha=2$, donc $u_n\sim\frac2n$.
""", r"$u_n\sim\big(a(\alpha-1)n\big)^{-1/(\alpha-1)}$ ; $\sin$ : $\sqrt{3/n}$ ; $\ln(1+x)$ : $2/n$.")

c("x-s-2",
r"Calcule $a_{n+1}b_{n+1}$ : que remarques-tu ?",
r"Le produit est constant ; avec $a_n\ge b_n$ (moyennes arithmétique et harmonique), les suites sont adjacentes et convergent vers $\ell=\sqrt{a_0b_0}$.",
r"Comme $b_n=\ell^2/a_n$, la suite $(a_n)$ est la méthode de Héron : $a_{n+1}-\ell=\frac{(a_n-\ell)^2}{2a_n}$. Convergence quadratique.",
r"""
**1.** La moyenne harmonique de $a,b>0$ est $\frac{2ab}{a+b}$, donc
$$a_{n+1}b_{n+1}=\frac{a_n+b_n}2\cdot\frac{2a_nb_n}{a_n+b_n}=a_nb_n=a_0b_0=:\ell^2.$$
De plus $a_{n+1}-b_{n+1}=\frac{(a_n-b_n)^2}{2(a_n+b_n)}\ge0$ : pour $n\ge1$, $b_n\le a_n$, donc $a_{n+1}\le a_n$ et $b_{n+1}\ge b_n$. Les suites sont monotones, bornées, et $a_{n+1}-b_{n+1}\le\frac{a_n-b_n}2$ : elles sont adjacentes, de limite commune $\ell$ avec $\ell^2=a_0b_0$, soit $\ell=\sqrt{a_0b_0}$ (moyenne géométrique).

**2.** Comme $b_n=\ell^2/a_n$ : $a_{n+1}=\frac12\big(a_n+\frac{\ell^2}{a_n}\big)$ (**méthode de Héron**), et $e_n=a_n-\ell\ge0$ ($n\ge1$) vérifie
$$e_{n+1}=\frac{e_n^2}{2a_n}=\frac{e_n^2}{2(\ell+e_n)}.$$
Donc $e_{n+1}\sim\frac{e_n^2}{2\ell}$ (convergence quadratique). Plus précisément, avec $\varepsilon_n=\frac{e_n}{2\ell}$ : $\varepsilon_{n+1}=\varepsilon_n^2\,\frac\ell{\ell+e_n}$. En posant $c_n=2^{-n}\ln\varepsilon_n$, on a $c_{n+1}-c_n=-2^{-n-1}\ln\big(1+\frac{e_n}\ell\big)$, terme d'une série convergente : $c_n\to K<0$, et $\ln\varepsilon_n-2^nK=\sum_{k\ge n}2^{n-k-1}\ln\big(1+\frac{e_k}\ell\big)\to0$. Avec $\theta=e^K\in]0,1[$ (qui dépend de $a_0,b_0$) :
$$a_n-\ell\sim2\ell\,\theta^{2^n}.$$
Le nombre de décimales exactes double à chaque étape.
""", r"$\ell=\sqrt{a_0b_0}$ ; $a_{n+1}-\ell=\frac{(a_n-\ell)^2}{2a_n}$, d'où $a_n-\ell\sim2\ell\,\theta^{2^n}$.")

c("x-s-3",
r"Étudie séparément le module et l'argument de $z_n$.",
r"$|z_n|^2=\prod_{k\le n}\big(1+\frac1{k^2}\big)$ converge ; un argument de $z_n$ est $\theta_n=\sum_{k\le n}\arctan\frac1k$.",
r"$\theta_n\to+\infty$ avec des pas $\arctan\frac1n\to0$ : la suite $\theta_n$ « passe près » de tout réel modulo $2\pi$.",
r"""
**Module.** $|z_n|^2=\prod_{k=1}^n\big(1+\frac1{k^2}\big)$ ; comme $\sum\ln(1+\frac1{k^2})$ converge, $|z_n|\to\rho=\prod_{k\ge1}\sqrt{1+1/k^2}\in]1,+\infty[$. (On peut montrer, via le produit eulérien du sinus, que $\rho^2=\frac{\operatorname{sh}\pi}\pi$.)

**Argument.** $\arg(1+\frac ik)=\arctan\frac1k$, donc $z_n=|z_n|e^{i\theta_n}$ avec $\theta_n=\sum_{k=1}^n\arctan\frac1k$. Comme $\arctan\frac1k\sim\frac1k$, $\theta_n\to+\infty$, et les pas $\theta_{n+1}-\theta_n\to0$.

**Valeurs d'adhérence.** Soit $\varphi\in\mathbb R$ et $\varepsilon>0$. Pour $n\ge N$, les pas sont $<\varepsilon$ ; comme $\theta_n\to+\infty$, pour tout $m$ assez grand il existe $n\ge N$ avec $|\theta_n-(\varphi+2m\pi)|<\varepsilon$. On construit ainsi une suite extraite avec $e^{i\theta_{n_j}}\to e^{i\varphi}$, et $z_{n_j}\to\rho e^{i\varphi}$. Réciproquement, toute valeur d'adhérence est de module $\rho$.

**Conclusion :** l'ensemble des valeurs d'adhérence est le **cercle de centre 0 et de rayon $\rho=\sqrt{\operatorname{sh}\pi/\pi}$**.
""", r"Le cercle de rayon $\rho=\prod\sqrt{1+1/k^2}=\sqrt{\operatorname{sh}\pi/\pi}$.")

c("x-se-1",
r"Regroupe les entiers selon leur nombre de chiffres $d$.",
r"Combien y a-t-il d'entiers à $d$ chiffres sans 9 ? Chacun est $\ge10^{d-1}$.",
r"Il y a $8\cdot9^{d-1}$ tels entiers : majore la contribution du bloc $d$ par $8\big(\frac9{10}\big)^{d-1}$.",
r"""
Les termes sont positifs : on peut regrouper par paquets. Un entier à $d$ chiffres sans 9 a son premier chiffre dans $\{1,\dots,8\}$ et les autres dans $\{0,\dots,8\}$ : il y en a $8\cdot9^{d-1}$, tous $\ge10^{d-1}$. La contribution des entiers à $d$ chiffres est donc au plus
$$\frac{8\cdot9^{d-1}}{10^{d-1}}=8\Big(\frac9{10}\Big)^{d-1}.$$
Par sommation par paquets (termes positifs) :
$$\sum_{n\ge1}\frac1{p_n}\le\sum_{d\ge1}8\Big(\frac9{10}\Big)^{d-1}=80.$$
La série **converge** (série de Kempner ; sa somme vaut environ $22{,}92$).

*Morale :* « presque tous » les grands entiers contiennent un 9 : parmi les entiers à $d$ chiffres, la proportion de ceux sans 9 vaut $\frac{8\cdot9^{d-1}}{9\cdot10^{d-1}}\to0$.
""", r"Converge, somme $\le80$ (en fait $\approx22{,}92$).")

c("x-se-2",
r"Notons $A_n=a_1+\dots+a_n$. Minore $A_n$ grâce à Cauchy-Schwarz appliqué à $\sum_{k\le n}k=\sum k\sqrt{1/a_k}\cdot\sqrt{a_k}$.",
r"Tu obtiens $\frac n{A_n}\le\frac4{n(n+1)^2}\sum_{k\le n}\frac{k^2}{a_k}$ ; somme en $n$ et intervertis (termes positifs).",
r"Majore $\sum_{n\ge k}\frac4{n(n+1)^2}\le\frac2{k^2}$ via $\frac1{n(n+1)^2}\le\frac12\Big(\frac1{n^2}-\frac1{(n+1)^2}\Big)$. Pour l'optimalité, teste $a_n=n^{1+\varepsilon}$.",
r"""
Notons $A_n=\sum_{k\le n}a_k$.

**Majoration.** Par Cauchy-Schwarz :
$$\Big(\frac{n(n+1)}2\Big)^2=\Big(\sum_{k=1}^n\sqrt{a_k}\cdot\frac k{\sqrt{a_k}}\Big)^2\le A_n\sum_{k=1}^n\frac{k^2}{a_k},$$
donc $\frac n{A_n}\le\frac4{n(n+1)^2}\sum_{k=1}^n\frac{k^2}{a_k}$. En sommant et en intervertissant (termes positifs) :
$$\sum_{n\ge1}\frac n{A_n}\le\sum_{k\ge1}\frac{k^2}{a_k}\sum_{n\ge k}\frac4{n(n+1)^2}.$$
Or $\frac1{n^2}-\frac1{(n+1)^2}=\frac{2n+1}{n^2(n+1)^2}\ge\frac2{n(n+1)^2}$, donc $\sum_{n\ge k}\frac4{n(n+1)^2}\le2\sum_{n\ge k}\Big(\frac1{n^2}-\frac1{(n+1)^2}\Big)=\frac2{k^2}$. Ainsi
$$\sum_{n\ge1}\frac n{a_1+\dots+a_n}\le2\sum_{n\ge1}\frac1{a_n}.$$

**Optimalité de $K=2$.** Pour $a_n=n^{1+\varepsilon}$ : $\sum\frac1{a_n}\sim\frac1\varepsilon$ et $A_n\sim\frac{n^{2+\varepsilon}}{2+\varepsilon}$, donc $\sum\frac n{A_n}\sim\frac{2+\varepsilon}\varepsilon$ quand $\varepsilon\to0$. Le rapport tend vers $2$ : aucune constante $<2$ ne convient.

**Meilleure constante : $K=2$.**
""", r"$K=2$ convient (Cauchy-Schwarz) et est optimale ($a_n=n^{1+\varepsilon}$).")

c("x-f-1",
r"Pour 1, applique le théorème des valeurs intermédiaires à $g(x)=f(x)-x$.",
r"Pour 2 (sans continuité !), considère $s=\sup\{x\in[0,1]:f(x)\ge x\}$.",
r"Pour 3, par l'absurde $f>g$ partout. Montre que $f$ envoie l'ensemble des points fixes de $g$ dans lui-même et regarde son maximum.",
r"""
**1.** Soit $I=[a,b]$ et $g=f-\mathrm{id}$, continue.
- Si $f(I)\subset I$ : $g(a)=f(a)-a\ge0$ et $g(b)\le0$.
- Si $I\subset f(I)$ : il existe $u,v\in I$ avec $f(u)=a$ et $f(v)=b$ ; alors $g(u)=a-u\le0$ et $g(v)=b-v\ge0$.

Dans les deux cas, le TVI donne un zéro de $g$ : un point fixe.

**2.** Soit $A=\{x\in[0,1]:f(x)\ge x\}\ni0$ et $s=\sup A$. Pour $x\in A$ : $x\le f(x)\le f(s)$ (croissance, $x\le s$), donc $s\le f(s)$. Alors $f(s)\le f(f(s))$, donc $f(s)\in A$ et $f(s)\le s$. Ainsi $f(s)=s$.

**3.** Supposons $f(x)\ne g(x)$ pour tout $x$ ; par le TVI, $f-g$ est de signe constant, disons $f>g$. Soit $F=\{x:g(x)=x\}$, non vide (question 1) et fermé, donc compact : soit $m=\max F$. Pour $x\in F$, $g(f(x))=f(g(x))=f(x)$, donc $f(x)\in F$. En particulier $f(m)\in F$, d'où $f(m)\le m=g(m)$ : contradiction avec $f(m)>g(m)$. (Si $f<g$, on raisonne avec $\min F$.)

Donc il existe $x$ tel que $f(x)=g(x)$.
""", r"TVI ; $\sup\{f(x)\ge x\}$ ; $\max\operatorname{Fix}(g)$ stable par $f$.")

c("x-f-2",
r"Utilise la définition de l'uniforme continuité avec $\varepsilon=1$ : il existe $\delta>0$ tel que $|x-y|\le\delta\Rightarrow|f(x)-f(y)|\le1$.",
r"Relie $0$ à $x$ par des pas de longueur $\le\delta$ : combien en faut-il ?",
r"Pour la réciproque, cherche une fonction bornée mais pas uniformément continue (oscillations de plus en plus rapides).",
r"""
**Majoration.** Soit $\delta>0$ tel que $|x-y|\le\delta\Rightarrow|f(x)-f(y)|\le1$. Pour $x\in\mathbb R$, soit $N=\lceil|x|/\delta\rceil$ et $x_k=\frac kNx$ ($0\le k\le N$) : $|x_{k+1}-x_k|=\frac{|x|}N\le\delta$. Par télescopage,
$$|f(x)-f(0)|\le\sum_{k=0}^{N-1}|f(x_{k+1})-f(x_k)|\le N\le\frac{|x|}\delta+1.$$
Donc $|f(x)|\le a|x|+b$ avec $a=\frac1\delta$ et $b=1+|f(0)|$.

**La réciproque est fausse.** $f(x)=\sin(x^2)$ est bornée (donc vérifie l'inégalité avec $a=b=1$) mais n'est pas uniformément continue : avec $x_n=\sqrt{n\pi}$ et $y_n=\sqrt{n\pi+\pi/2}$, $|x_n-y_n|=\frac{\pi/2}{\sqrt{n\pi+\pi/2}+\sqrt{n\pi}}\to0$ alors que $|f(x_n)-f(y_n)|=1$.

*Moralité* : une fonction uniformément continue est « au plus affine » à l'infini ; ainsi $x\mapsto x^2$ n'est pas uniformément continue sur $\mathbb R$.
""", r"$|f(x)|\le\frac{|x|}\delta+1+|f(0)|$ ; réciproque fausse ($\sin x^2$).")

c("x-f-3",
r"Si $\sin=R$ sur $]a,b[$ avec $R$ fraction rationnelle, quelle équation différentielle simple $R$ vérifie-t-elle ?",
r"$R''+R=0$ sur $]a,b[$, donc comme fractions rationnelles (égalité en une infinité de points).",
r"Compare les degrés : $\deg R'\le\deg R-1$, donc $\deg R''\le\deg R-2$.",
r"""
Supposons $\sin x=R(x)$ sur $]a,b[$ avec $R=P/Q$ fraction rationnelle. Alors $R''+R=0$ sur $]a,b[$. La fraction $R''+R$ s'annule en une infinité de points : c'est la fraction nulle.

**Degrés.** Pour une fraction non nulle, $\deg(P/Q)=\deg P-\deg Q$. Si $R=P/Q$ avec $\deg P=p$, $\deg Q=q$ :
$$R'=\frac{P'Q-PQ'}{Q^2},\qquad\deg(P'Q-PQ')\le p+q-1,$$
(le coefficient de $X^{p+q-1}$ vaut $(p-q)$ fois le produit des coefficients dominants, éventuellement nul). Donc $\deg R'\le\deg R-1$ (ou $R'=0$), et $\deg R''\le\deg R-2$.

Si $R\ne0$, l'égalité $R=-R''$ donne $\deg R\le\deg R-2$ : absurde. Donc $R=0$, et $\sin$ serait nulle sur $]a,b[$ : absurde.

**Conclusion :** $\sin$ n'est la restriction à aucun intervalle ouvert non vide d'une fraction rationnelle. (Autre argument : $\sin$ a une infinité de zéros, mais on ne les voit que sur $\mathbb R$ tout entier, pas sur $]a,b[$ ; d'où l'intérêt de l'équation différentielle.)
""", r"$R''+R=0$ impossible pour une fraction non nulle (le degré baisse de 2).")

c("x-fo-1",
r"$f$ est paire : seuls les $a_n$ sont non nuls. Calcule $a_n=\frac2\pi\int_0^\pi x^2\cos(nx)\,dx$ par deux intégrations par parties.",
r"$f$ est continue et $\mathcal C^1$ par morceaux (et $f(-\pi)=f(\pi)$) : le théorème de Dirichlet donne l'égalité en tout point. Évalue en $x=\pi$.",
r"Pour $\zeta(4)$, applique la formule de Parseval.",
r"""
**Coefficients.** $f$ est paire, donc $b_n=0$. $a_0=\frac1\pi\int_{-\pi}^\pi x^2dx=\frac{2\pi^2}3$. Pour $n\ge1$, deux intégrations par parties donnent
$$a_n=\frac2\pi\int_0^\pi x^2\cos(nx)\,dx=\frac{4(-1)^n}{n^2}.$$

**Somme en un point.** $f$ est continue ($f(-\pi)=f(\pi)$), $2\pi$-périodique et $\mathcal C^1$ par morceaux : sa série de Fourier converge (normalement) vers $f$ :
$$x^2=\frac{\pi^2}3+4\sum_{n\ge1}\frac{(-1)^n}{n^2}\cos(nx),\qquad x\in[-\pi,\pi].$$
En $x=\pi$ : $\pi^2=\frac{\pi^2}3+4\sum\frac1{n^2}$, d'où $\displaystyle\sum_{n\ge1}\frac1{n^2}=\frac{\pi^2}6$. (En $x=0$ : $\sum\frac{(-1)^{n+1}}{n^2}=\frac{\pi^2}{12}$.)

**Parseval.** $\frac1\pi\int_{-\pi}^\pi f^2=\frac{a_0^2}2+\sum_{n\ge1}(a_n^2+b_n^2)$ :
$$\frac1\pi\cdot\frac{2\pi^5}5=\frac{2\pi^4}9+16\sum_{n\ge1}\frac1{n^4},$$
donc $16\zeta(4)=\frac{2\pi^4}5-\frac{2\pi^4}9=\frac{8\pi^4}{45}$ et
$$\sum_{n\ge1}\frac1{n^4}=\frac{\pi^4}{90}.$$
""", r"$\sum\frac1{n^2}=\frac{\pi^2}6$, $\sum\frac1{n^4}=\frac{\pi^4}{90}$.")
