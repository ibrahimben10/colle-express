D = {}

D['m-ccmp-08a'] = r"""
**Notations.** Pour $n\ge1$, $D(n)$ est l'ensemble des diviseurs positifs de $n$ et $\tau(n)=|D(n)|$. On a $f(n)=\dfrac{\Pi(n)}n$ avec $\Pi(n)=\prod_{d\in D(n)}d$ (on retire le diviseur $n$ lui-même).

**Étape 1 : produit de tous les diviseurs.** L'application $\sigma:d\mapsto\frac nd$ envoie $D(n)$ dans $D(n)$ (si $d\mid n$, $\frac nd$ est un entier qui divise $n$) et $\sigma\circ\sigma=\mathrm{id}$ : c'est une bijection. Réindexer un produit par une bijection ne le change pas, donc
$$\Pi(n)^2=\prod_{d\in D(n)}d\cdot\prod_{d\in D(n)}\frac nd=\prod_{d\in D(n)}\Big(d\cdot\frac nd\Big)=n^{\tau(n)}.$$
Comme $\Pi(n)>0$ : $\Pi(n)=n^{\tau(n)/2}$, puis $f(n)=n^{\tau(n)/2-1}$.

**Étape 2 : traduction de $f(n)=n$.**
- $n=1$ : $D(1)=\{1\}$, il n'y a aucun diviseur strict, le produit vide vaut 1 : $f(1)=1$. Donc $n=1$ est solution.
- $n\ge2$ : $n^{\tau(n)/2-1}=n^1$ avec $n\ge2$ équivaut à l'égalité des exposants (la fonction $x\mapsto n^x$ est injective) : $\frac{\tau(n)}2-1=1$, soit $\tau(n)=4$.

**Étape 3 : entiers ayant exactement 4 diviseurs.** Écrivons $n=p_1^{a_1}\cdots p_r^{a_r}$ (premiers distincts, $a_i\ge1$). Un diviseur s'écrit $p_1^{b_1}\cdots p_r^{b_r}$ avec $0\le b_i\le a_i$, d'où $\tau(n)=\prod_{i=1}^r(a_i+1)$. Chaque facteur $a_i+1$ est $\ge2$, donc $\prod(a_i+1)=4$ impose :
- soit $r=1$ et $a_1+1=4$ : $n=p^3$ ;
- soit $r=2$ et $a_1+1=a_2+1=2$ : $n=pq$ avec $p\neq q$ ;
- $r\ge3$ est impossible ($\prod\ge8$).

**Conclusion.** $f(n)=n$ si et seulement si $n=1$, ou $n=p^3$, ou $n=pq$ ($p,q$ premiers distincts). Vérifications : $f(8)=1\cdot2\cdot4=8$, $f(6)=1\cdot2\cdot3=6$, mais $f(12)=1\cdot2\cdot3\cdot4\cdot6=144\neq12$.
"""

D['m-ccmp-08b'] = r"""
**Le terme général est bien défini.** Pour $x\in[0,1]$ et $n\ge0$, $0\le\frac x{2^n}\le1<\frac\pi2$, donc $\cos\frac x{2^n}>0$ et le logarithme a un sens.

**Convergence.** Si $x=0$, tous les termes sont nuls. Supposons $x\in]0,1]$ et posons $u_n=\frac x{2^n}\to0$. On a $\cos u=1-\frac{u^2}2+o(u^2)$ et $\ln(1+h)\sim h$ en 0, donc
$$\ln\cos u_n\sim-\frac{u_n^2}2=-\frac{x^2}2\cdot\frac1{4^n}.$$
Les termes sont tous négatifs, et $\sum\frac1{4^n}$ est une série géométrique convergente : par comparaison de séries de signe constant, la série converge.

**Produit télescopique.** Pour $x\in]0,1]$, posons $P_N=\prod_{k=0}^N\cos\frac x{2^k}$, de sorte que $\sum_{n=0}^N\ln\cos\frac x{2^n}=\ln P_N$. La formule $\sin2a=2\sin a\cos a$ avec $a=\frac x{2^k}$ donne
$$\cos\frac x{2^k}=\frac{\sin\frac x{2^{k-1}}}{2\sin\frac x{2^k}}\qquad(k\ge0,\ \sin\tfrac x{2^k}\neq0\text{ car }0<\tfrac x{2^k}<\pi).$$
Le produit télescope :
$$P_N=\prod_{k=0}^N\frac{\sin\frac x{2^{k-1}}}{2\sin\frac x{2^k}}=\frac1{2^{N+1}}\cdot\frac{\sin(2x)}{\sin\frac x{2^N}}.$$

**Passage à la limite.** Comme $\sin u\sim u$ en 0, $2^N\sin\frac x{2^N}\sim2^N\cdot\frac x{2^N}=x$. Donc
$$P_N=\frac{\sin2x}{2\cdot2^N\sin\frac x{2^N}}\xrightarrow[N\to\infty]{}\frac{\sin2x}{2x}.$$
Comme $0<2x\le2<\pi$, $\sin2x>0$ : la limite est strictement positive, et par continuité du logarithme, $\ln P_N\to\ln\frac{\sin2x}{2x}$.

**Conclusion.** $\displaystyle\sum_{n=0}^{+\infty}\ln\cos\frac x{2^n}=\ln\frac{\sin2x}{2x}$ pour $x\in]0,1]$, et $0$ pour $x=0$ (valeur qui est aussi la limite de $\ln\frac{\sin2x}{2x}$ quand $x\to0$).
"""

D['m-ccmp-09'] = r"""
**1. Encadrement.** $f$ est continue sur le segment $[a,b]$ : elle est bornée et atteint ses bornes $m=f(x_1)=\min f$ et $M=f(x_2)=\max f$. Comme $g\ge0$, on a $mg(x)\le f(x)g(x)\le Mg(x)$ pour tout $x$, et par croissance de l'intégrale :
$$m\int_a^bg\le\int_a^bfg\le M\int_a^bg.$$

**1. Conclusion.**
- Si $\int_a^bg=0$ : $g$ est continue, positive, d'intégrale nulle, donc nulle. Alors $\int fg=0=f(c)\int g$ pour tout $c$.
- Sinon $\int g>0$ et $\mu=\frac{\int fg}{\int g}\in[m,M]=[f(x_1),f(x_2)]$. Par le théorème des valeurs intermédiaires appliqué à $f$ entre $x_1$ et $x_2$, il existe $c$ (entre $x_1$ et $x_2$, donc dans $[a,b]$) avec $f(c)=\mu$, ce qu'on voulait.

**2. Convergence en 0.** Soit $h(t)=\frac{a\sin(bt)-b\sin(at)}{t^2}$, continue sur $]0,+\infty[$. Avec $\sin u=u-\frac{u^3}6+o(u^3)$ :
$$a\sin(bt)-b\sin(at)=a\Big(bt-\frac{b^3t^3}6\Big)-b\Big(at-\frac{a^3t^3}6\Big)+o(t^3)=\frac{ab(a^2-b^2)}6t^3+o(t^3).$$
Les termes en $t$ se compensent ; donc $h(t)=\frac{ab(a^2-b^2)}6t+o(t)\to0$ : $h$ se prolonge par continuité en 0, il n'y a pas de problème en 0.

**2. Convergence en $+\infty$.** $|h(t)|\le\frac{a+b}{t^2}$, intégrable sur $[1,+\infty[$ (Riemann, exposant $2>1$). L'intégrale converge (absolument).

**2. Découpage loin de 0.** Fixons $\varepsilon>0$. Sur $[\varepsilon,+\infty[$, chacune des fonctions $\frac{\sin(bt)}{t^2}$ et $\frac{\sin(at)}{t^2}$ est intégrable (majorées par $\frac1{t^2}$), on peut donc séparer :
$$\int_\varepsilon^{+\infty}h=a\int_\varepsilon^{+\infty}\frac{\sin(bt)}{t^2}\mathrm dt-b\int_\varepsilon^{+\infty}\frac{\sin(at)}{t^2}\mathrm dt.$$
(On ne peut pas le faire sur $]0,+\infty[$ : chaque morceau diverge en 0, car $\frac{\sin(bt)}{t^2}\sim\frac bt$.)

**2. Changements de variable.** Dans la première intégrale, $u=bt$ ($t=\frac ub$, $\mathrm dt=\frac{\mathrm du}b$) :
$$a\int_\varepsilon^{+\infty}\frac{\sin(bt)}{t^2}\mathrm dt=a\int_{b\varepsilon}^{+\infty}\frac{\sin u}{u^2/b^2}\cdot\frac{\mathrm du}b=ab\int_{b\varepsilon}^{+\infty}\frac{\sin u}{u^2}\mathrm du.$$
De même, avec $u=at$, la seconde vaut $ab\int_{a\varepsilon}^{+\infty}\frac{\sin u}{u^2}\mathrm du$. Par Chasles :
$$\int_\varepsilon^{+\infty}h=ab\int_{b\varepsilon}^{a\varepsilon}\frac{\sin u}u\cdot\frac{\mathrm du}u.$$

**2. Formule de la moyenne.** Sur le segment d'extrémités $a\varepsilon$ et $b\varepsilon$, appliquons la question 1 avec $f(u)=\frac{\sin u}u$ (continue) et $g(u)=\frac1u>0$ : il existe $c_\varepsilon$ entre $a\varepsilon$ et $b\varepsilon$ tel que
$$\int_{b\varepsilon}^{a\varepsilon}\frac{\sin u}u\cdot\frac{\mathrm du}u=\frac{\sin c_\varepsilon}{c_\varepsilon}\int_{b\varepsilon}^{a\varepsilon}\frac{\mathrm du}u=\frac{\sin c_\varepsilon}{c_\varepsilon}\,\ln\frac{a\varepsilon}{b\varepsilon}=\frac{\sin c_\varepsilon}{c_\varepsilon}\ln\frac ab.$$
(Si $a>b$, les bornes sont dans l'ordre décroissant : on applique la question 1 sur $[b\varepsilon,a\varepsilon]$ et on change de signe des deux côtés ; le résultat est le même.)

**2. Limite.** Quand $\varepsilon\to0$, $c_\varepsilon\to0$ (encadré par $a\varepsilon$ et $b\varepsilon$), donc $\frac{\sin c_\varepsilon}{c_\varepsilon}\to1$. Ainsi
$$\int_0^{+\infty}\frac{a\sin(bt)-b\sin(at)}{t^2}\,\mathrm dt=\lim_{\varepsilon\to0}\int_\varepsilon^{+\infty}h=ab\ln\frac ab.$$
(Vérification : pour $a=b$ l'intégrande est nul et on trouve bien 0.)
"""

D['m-ccmp-10b'] = r"""
**1. $O_A$ est un sous-groupe de $\mathbb C^*$.** On note $\sim$ la similitude, relation d'équivalence sur $\mathcal M_3(\mathbb C)$, compatible avec la multiplication par un scalaire : si $B=PCP^{-1}$, alors $\lambda B=P(\lambda C)P^{-1}$.
- $1\in O_A$ car $A\sim A$.
- Stabilité par produit : soient $c_1,c_2\in O_A$. De $c_2A\sim A$ on tire, en multipliant par $c_1$, $c_1c_2A\sim c_1A$ ; et $c_1A\sim A$. Par transitivité, $c_1c_2A\sim A$ : $c_1c_2\in O_A$.
- Stabilité par inverse : si $cA\sim A$, en multipliant par $c^{-1}$ : $A\sim c^{-1}A$, donc $c^{-1}\in O_A$.

**2. Sens direct : $O_A$ infini $\Rightarrow$ $A$ nilpotente.** Si $cA=PAP^{-1}$, les deux matrices ont même spectre ; or le spectre de $cA$ est $c\,\mathrm{Sp}(A)$. Donc $c\,\mathrm{Sp}(A)=\mathrm{Sp}(A)$ pour tout $c\in O_A$. Supposons par l'absurde que $A$ a une valeur propre $\lambda\neq0$. Alors pour tout $c\in O_A$, $c\lambda\in\mathrm{Sp}(A)$ ; l'application $c\mapsto c\lambda$ est injective et $O_A$ est infini, donc $\mathrm{Sp}(A)$ serait infini, alors qu'il a au plus 3 éléments. Contradiction : $\mathrm{Sp}(A)=\{0\}$, donc $\chi_A=X^3$ et, par Cayley-Hamilton, $A^3=0$ : $A$ est nilpotente.

**2 et 3. Sens réciproque : $A$ nilpotente $\Rightarrow O_A=\mathbb C^*$.** Une matrice nilpotente de taille 3 est semblable à l'une des trois matrices
$$0,\qquad N_2=\begin{pmatrix}0&1&0\\0&0&0\\0&0&0\end{pmatrix},\qquad N_3=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}$$
(réduction de Jordan, ou selon le rang : 0, 1 ou 2). Soit $c\in\mathbb C^*$ et $D=\mathrm{diag}(1,c,c^2)$. Pour une matrice $N$, le coefficient $(i,j)$ de $D\,N\,D^{-1}$ vaut $d_i\,n_{ij}\,d_j^{-1}=c^{i-1}n_{ij}c^{-(j-1)}=c^{i-j}n_{ij}$. Pour $N=N_2$ ou $N_3$, les seuls coefficients non nuls sont en position $(i,i+1)$, multipliés par $c^{-1}$ ; donc
$$D\,(cN)\,D^{-1}=c\cdot c^{-1}N=N.$$
Ainsi $cN\sim N$ pour tout $c\neq0$ (et trivialement $c\cdot0=0$). Si $A=PNP^{-1}$, alors $cA=P(cN)P^{-1}\sim cN\sim N\sim A$. Donc $O_A=\mathbb C^*$, qui est infini.

**Conclusion.** $O_A$ est infini si et seulement si $A$ est nilpotente, et dans ce cas $O_A=\mathbb C^*$. (Si $A$ n'est pas nilpotente, $O_A$ est un sous-groupe fini de $\mathbb C^*$, donc de la forme $\mathbb U_d$.)
"""
