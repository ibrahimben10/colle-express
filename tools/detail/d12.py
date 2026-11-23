D = {}

D['m-ccmp-28a'] = r"""
**Lemme : les translations sont des bijections.** Pour $g\in G$, l'application $\tau_g:G\to G$, $h\mapsto gh$, est bien à valeurs dans $G$ (stabilité par produit) et bijective, d'inverse $h\mapsto g^{-1}h$. Par conséquent, pour toute fonction $\psi$ définie sur $G$, $\sum_{h\in G}\psi(gh)=\sum_{h\in G}\psi(h)$ (réindexation par une bijection).

**1. Calcul de $p^2$.** Par bilinéarité de la composition :
$$p^2=\frac1{n^2}\Big(\sum_ig_i\Big)\Big(\sum_jg_j\Big)=\frac1{n^2}\sum_{i=1}^n\Big(\sum_{j=1}^ng_ig_j\Big).$$
Pour $i$ fixé, d'après le lemme, $\sum_jg_ig_j=\sum_jg_j=np$. Donc
$$p^2=\frac1{n^2}\sum_{i=1}^nnp=\frac1{n^2}\cdot n\cdot np=p.$$
$p$ est un projecteur.

**2. $\mathrm{Im}\,p$ est l'ensemble des vecteurs fixes.** Notons $F=\bigcap_i\ker(g_i-\mathrm{id})=\{x:g_i(x)=x\ \forall i\}$.
- Si $x\in F$ : $p(x)=\frac1n\sum_ig_i(x)=\frac1n\cdot nx=x$, donc $x\in\mathrm{Im}\,p$.
- Si $x=p(y)\in\mathrm{Im}\,p$ et $k$ fixé : $g_k(x)=\frac1n\sum_ig_kg_i(y)=\frac1n\sum_ig_i(y)=p(y)=x$, par le lemme. Donc $x\in F$.

Ainsi $\mathrm{Im}\,p=F$.

**2. Rang d'un projecteur.** Pour un projecteur, $E=\mathrm{Im}\,p\oplus\ker p$ (tout $x$ s'écrit $p(x)+(x-p(x))$, et $\mathrm{Im}\,p\cap\ker p=\{0\}$ car si $x=p(y)$ et $p(x)=0$ alors $x=p(y)=p^2(y)=p(x)=0$). Dans une base adaptée, la matrice de $p$ est $\begin{pmatrix}I_r&0\\0&0\end{pmatrix}$ avec $r=\mathrm{rg}\,p$, d'où $\mathrm{Tr}\,p=r$.

**2. Conclusion.** Par linéarité de la trace :
$$\dim\bigcap_{i=1}^n\ker(g_i-\mathrm{id}_E)=\mathrm{rg}\,p=\mathrm{Tr}\,p=\frac1n\sum_{i=1}^n\mathrm{tr}(g_i).$$
En particulier, la moyenne des traces des éléments d'un groupe fini est toujours un entier.
"""

D['m-ccmp-28b'] = r"""
**1. Définition.** Pour $x>0$ et $t>0$, $|\sin t|\le t$ donne $\big|\frac{\sin t}te^{-xt}\big|\le e^{-xt}$, intégrable sur $]0,+\infty[$ (et l'intégrande se prolonge par continuité en $0$ par la valeur 1). Donc $f$ est définie sur $]0,+\infty[$.

**1. Dérivabilité.** Soit $a>0$. Sur $[a,+\infty[\times]0,+\infty[$, $h(x,t)=\frac{\sin t}te^{-xt}$ admet la dérivée partielle $\partial_xh(x,t)=-\sin t\,e^{-xt}$, continue, et
$$|\partial_xh(x,t)|\le e^{-at},$$
intégrable et indépendante de $x\in[a,+\infty[$. Par le théorème de dérivation sous l'intégrale, $f$ est $C^1$ sur $[a,+\infty[$, donc sur $]0,+\infty[$, et $f'(x)=-\int_0^{+\infty}\sin t\,e^{-xt}\,\mathrm dt$.

**1. Calcul de $f'$.** $\sin t=\mathrm{Im}(e^{it})$, donc $\int_0^{+\infty}\sin t\,e^{-xt}\,\mathrm dt=\mathrm{Im}\int_0^{+\infty}e^{(-x+i)t}\,\mathrm dt$. Comme $|e^{(-x+i)t}|=e^{-xt}\to0$ :
$$\int_0^{+\infty}e^{(-x+i)t}\,\mathrm dt=\left[\frac{e^{(-x+i)t}}{-x+i}\right]_0^{+\infty}=\frac1{x-i}=\frac{x+i}{x^2+1}.$$
D'où $f'(x)=-\frac1{1+x^2}$ et $f(x)=C-\arctan x$ sur $]0,+\infty[$.

**1. Constante.** $|f(x)|\le\int_0^{+\infty}e^{-xt}\,\mathrm dt=\frac1x\to0$ quand $x\to+\infty$. Or $\arctan x\to\frac\pi2$, donc $C=\frac\pi2$ :
$$f(x)=\frac\pi2-\arctan x.$$

**2. Difficulté.** $\int_0^{+\infty}\frac{\sin t}t\,\mathrm dt$ n'est que semi-convergente : on ne peut pas dominer pour passer à la limite $x\to0$. On montre une convergence **uniforme** des intégrales tronquées.

**2. Majoration uniforme du reste.** Pour $x\ge0$, posons $\varphi_x(t)=\frac{e^{-xt}}t$ sur $[A,+\infty[$ ($A>0$) : positive, décroissante, de limite nulle. Par intégration par parties ($u=-\cos t$, $v=\varphi_x$) :
$$\int_A^{B}\sin t\,\varphi_x(t)\,\mathrm dt=\big[-\cos t\,\varphi_x(t)\big]_A^B+\int_A^B\cos t\,\varphi_x'(t)\,\mathrm dt.$$
Quand $B\to\infty$, le crochet tend vers $\cos A\,\varphi_x(A)$, de module $\le\varphi_x(A)$ ; et $\big|\int_A^\infty\cos t\,\varphi_x'\big|\le\int_A^\infty(-\varphi_x')=\varphi_x(A)$. Donc
$$\Big|\int_A^{+\infty}\frac{\sin t}te^{-xt}\,\mathrm dt\Big|\le2\varphi_x(A)\le\frac2A\qquad\text{pour tout }x\ge0.$$

**2. Continuité de $f$ en 0.** Posons $F_A(x)=\int_0^A\frac{\sin t}te^{-xt}\,\mathrm dt$ : intégrale sur un segment d'une fonction continue de $(x,t)$, donc continue en $x$ sur $[0,+\infty[$. La majoration précédente donne $\sup_{x\ge0}|f(x)-F_A(x)|\le\frac2A$ (en posant $f(0)=\int_0^\infty\frac{\sin t}t\,\mathrm dt$) : $F_A\to f$ uniformément quand $A\to\infty$, donc $f$ est continue sur $[0,+\infty[$, en particulier en 0.

**Conclusion.**
$$\int_0^{+\infty}\frac{\sin t}t\,\mathrm dt=f(0)=\lim_{x\to0^+}\Big(\frac\pi2-\arctan x\Big)=\frac\pi2.$$
"""

D['m-ccs-01'] = r"""
**1. Formule de l'inverse.** Pour toute matrice $M$, $M\,\mathrm{com}(M)^{\top}=\mathrm{com}(M)^{\top}M=\det(M)\,I_n$ (développement des déterminants selon les lignes et colonnes). Si $M\in GL_n(\mathbb R)$ :
$$M^{-1}=\frac1{\det M}\,\mathrm{com}(M)^{\top}.$$

**1. Continuité.** Chaque coefficient de $\mathrm{com}(M)$ est un déterminant de taille $n-1$, donc un polynôme en les coefficients de $M$ ; $\det M$ aussi, et il ne s'annule pas sur $GL_n(\mathbb R)$. Les coefficients de $M^{-1}$ sont donc des fractions rationnelles des $m_{ij}$ à dénominateur non nul : chaque coefficient est continu, et $M\mapsto M^{-1}$ est continue sur $GL_n(\mathbb R)$ (en dimension finie, la continuité s'étudie coefficient par coefficient).

**2. Élimination par blocs.** On multiplie à gauche par une matrice triangulaire par blocs de déterminant 1 :
$$\begin{pmatrix}I_k&-W^{\top}\\0&I_p\end{pmatrix}\begin{pmatrix}0_k&W^{\top}\\V&I_p\end{pmatrix}=\begin{pmatrix}0_k-W^{\top}V&W^{\top}-W^{\top}I_p\\V&I_p\end{pmatrix}=\begin{pmatrix}-W^{\top}V&0\\V&I_p\end{pmatrix}.$$
La matrice obtenue est triangulaire inférieure par blocs : son déterminant est $\det(-W^{\top}V)\det(I_p)$. Donc
$$\det M_{V,W}=\det(-W^{\top}V)=(-1)^k\det(W^{\top}V).$$
Si $W^{\top}V$ est inversible, $\det M_{V,W}\neq0$ et $M_{V,W}$ est inversible.

**3.(a) Voisinage.** L'application $\delta:W\mapsto\det(W^{\top}V)$ est polynomiale en les coefficients de $W$, donc continue sur $\mathcal M_{p,k}(\mathbb R)$. Et $\delta(V)=\det(V^{\top}V)=\det(I_k)=1\neq0$. L'ensemble $\mathcal V=\delta^{-1}(\mathbb R^*)$ est l'image réciproque d'un ouvert par une application continue : c'est un ouvert, qui contient $V$. Pour $W\in\mathcal V$, $W^{\top}V$ est inversible.

**3.(b) Dimensions.** Soit $W\in\mathcal V$.
- $V$ est injective : si $Vy=0$, alors $y=V^{\top}Vy=0$. Donc $\dim\mathrm{Im}\,V=k$.
- $k=\mathrm{rg}(W^{\top}V)\le\mathrm{rg}(W^{\top})=\mathrm{rg}\,W\le k$ (car $W$ a $k$ colonnes). Donc $\mathrm{rg}\,W=k$ et $\dim(\mathrm{Im}\,W)^{\perp}=p-k$.

**3.(b) Intersection nulle.** Soit $x\in\mathrm{Im}\,V\cap(\mathrm{Im}\,W)^{\perp}$ : $x=Vy$, et $x$ est orthogonal à toutes les colonnes de $W$, c'est-à-dire $W^{\top}x=0$. Alors $W^{\top}Vy=0$, donc $y=0$ ($W^{\top}V$ inversible) et $x=0$.

**Conclusion.** $\dim\mathrm{Im}\,V+\dim(\mathrm{Im}\,W)^{\perp}=k+(p-k)=p$ et l'intersection est nulle :
$$\mathbb R^p=\mathrm{Im}\,V\oplus(\mathrm{Im}\,W)^{\perp}\qquad\text{pour tout }W\in\mathcal V.$$
"""
