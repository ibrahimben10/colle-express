D = {}

D['m-ccmp-15a'] = r"""
**1. Équation aux éléments propres.** Soit $\lambda\in\mathbb C$ et $u\in B$. On a $Tu=\lambda u\iff u_{n+1}=\lambda u_n$ pour tout $n\in\mathbb Z$.
- Si $\lambda=0$ : $u_{n+1}=0$ pour tout $n\in\mathbb Z$, donc $u_m=0$ pour tout $m$ (prendre $n=m-1$) : $u=0$. $0$ n'est pas valeur propre.
- Si $\lambda\neq0$ : la relation se lit dans les deux sens ($u_n=\lambda^{-1}u_{n+1}$), donc par récurrence vers $+\infty$ et vers $-\infty$ : $u_n=\lambda^nu_0$ pour tout $n\in\mathbb Z$.

**1. Condition de bornitude.** Pour $u_0\neq0$, $|u_n|=|\lambda|^n|u_0|$.
- Si $|\lambda|>1$ : $|u_n|\to+\infty$ quand $n\to+\infty$, non bornée.
- Si $|\lambda|<1$ : $|u_{-n}|=|\lambda|^{-n}|u_0|\to+\infty$ quand $n\to+\infty$, non bornée.
- Si $|\lambda|=1$ : $|u_n|=|u_0|$, bornée.

Donc $\mathrm{Sp}(T)=\mathbb U=\{\lambda\in\mathbb C:|\lambda|=1\}$, et pour $\lambda\in\mathbb U$, $\ker(T-\lambda\,\mathrm{id})=\mathrm{Vect}\big((\lambda^n)_{n\in\mathbb Z}\big)$.

**2. Suite des noyaux itérés.** Notons $K_k=\ker(\tilde T-\lambda\,\mathrm{id})^k$. Si $(\tilde T-\lambda)^kx=0$ alors $(\tilde T-\lambda)^{k+1}x=(\tilde T-\lambda)(0)=0$ : $K_k\subset K_{k+1}$. La suite $(\dim K_k)$ est donc une suite croissante d'entiers majorée par $\dim E$ : elle est stationnaire à partir d'un rang $k_0$. Deux sous-espaces emboîtés de même dimension finie sont égaux, donc $K_k=K_{k_0}$ pour $k\ge k_0$.

**3. Valeurs propres de $\tilde T$.** $E$ est un $\mathbb C$-espace de dimension finie, donc $\chi_{\tilde T}$ est scindé : $\chi_{\tilde T}=\prod_{i=1}^r(X-\lambda_i)^{m_i}$ avec $\lambda_i$ distinctes. Par le lemme des noyaux (les $(X-\lambda_i)^{m_i}$ sont premiers entre eux deux à deux) et Cayley-Hamilton :
$$E=\bigoplus_{i=1}^r\ker(\tilde T-\lambda_i\,\mathrm{id})^{m_i}.$$
Un vecteur propre de $\tilde T$ est un vecteur propre de $T$ : chaque $\lambda_i$ est dans $\mathbb U$, donc $|\lambda_i|=1$ et $\lambda_i\neq0$.

**3. Clé : $\ker(\tilde T-\lambda)^2=\ker(\tilde T-\lambda)$ pour $|\lambda|=1$.** L'inclusion $\supset$ est vue en 2. Soit $u\in E$ avec $(T-\lambda)^2u=0$ ; posons $v=(T-\lambda)u$. Alors $(T-\lambda)v=0$, donc par la question 1, $v_n=\lambda^nv_0$. La relation $v=Tu-\lambda u$ s'écrit $u_{n+1}=\lambda u_n+\lambda^nv_0$. Posons $w_n=\frac{u_n}{\lambda^n}$ ; en divisant par $\lambda^{n+1}$ :
$$w_{n+1}=w_n+\frac{v_0}\lambda\qquad(n\in\mathbb Z).$$
$(w_n)$ est arithmétique (dans les deux sens) : $w_n=w_0+n\frac{v_0}\lambda$ pour tout $n\in\mathbb Z$. Comme $|\lambda|=1$, $|u_n|=|w_n|=\big|u_0+n\frac{v_0}\lambda\big|$. Si $v_0\neq0$, $|u_n|\to+\infty$ : contradiction avec $u\in B$. Donc $v_0=0$, $v=0$ et $u\in\ker(T-\lambda)$.

**3. Récurrence.** Supposons $\ker(\tilde T-\lambda)^k=\ker(\tilde T-\lambda)$. Si $(\tilde T-\lambda)^{k+1}x=0$, alors $(\tilde T-\lambda)^k\big((\tilde T-\lambda)x\big)=0$, donc $(\tilde T-\lambda)x\in\ker(\tilde T-\lambda)$, soit $x\in\ker(\tilde T-\lambda)^2=\ker(\tilde T-\lambda)$. Ainsi tous les noyaux itérés sont égaux au sous-espace propre (la suite de la question 2 est stationnaire dès le rang 1).

**Conclusion.** $E=\bigoplus_{i=1}^r\ker(\tilde T-\lambda_i\,\mathrm{id})$ : $\tilde T$ est diagonalisable, et $E$ est engendré par des suites $(\lambda_i^n)_{n\in\mathbb Z}$ avec $|\lambda_i|=1$.
"""

D['m-ccmp-15b'] = r"""
**Sens direct.** Supposons $A\setminus\{a\}$ convexe, et soient $x,y\in A$ avec $a=\frac12(x+y)$. Raisonnons par l'absurde en supposant $x\neq a$.
- Alors $y=2a-x$, et $y=a\iff x=a$ ; donc $y\neq a$.
- Ainsi $x$ et $y$ appartiennent à $A\setminus\{a\}$, qui est convexe : leur milieu $\frac12(x+y)$ appartient à $A\setminus\{a\}$.
- Or ce milieu vaut $a$ : contradiction.

Donc $x=a$, puis $y=2a-x=a$.

**Sens réciproque, par contraposée.** Supposons $A\setminus\{a\}$ non convexe : il existe $x,y\in A\setminus\{a\}$ et $t\in]0,1[$ tels que $z=(1-t)x+ty\notin A\setminus\{a\}$. Or $A$ est convexe et $x,y\in A$, donc $z\in A$ ; c'est donc que $z=a$ :
$$a=(1-t)x+ty,\qquad x\neq a,\ y\neq a.$$

**Construction d'un « milieu ».** Quitte à échanger les rôles de $x$ et $y$ (ce qui remplace $t$ par $1-t$), on peut supposer $t\le\frac12$. Posons $y'=2a-x$. On calcule :
$$y'=2\big((1-t)x+ty\big)-x=(1-2t)x+2t\,y.$$
Comme $2t\in]0,1]$, $y'$ est une combinaison convexe de $x$ et $y$ : $y'\in[x,y]\subset A$. Par construction $a=\frac12(x+y')$, avec $x\in A$, $y'\in A$ et $x\neq a$. La propriété « $a=\frac12(x+y)\Rightarrow x=y=a$ » est donc fausse.

**Conclusion.** $a$ est extrémal si et seulement s'il n'est le milieu d'aucun segment de $A$ non réduit à un point.
"""

D['m-ccmp-17a'] = r"""
**Modélisation.** On peut imaginer qu'on tire toutes les boules : l'ordre de sortie est une permutation uniforme des $a+b+c$ boules. Le nombre $Y$ de rouges sorties avant la première blanche ne dépend que de l'**ordre relatif** des $a$ rouges et des $c$ blanches ; les noires, intercalées n'importe où, ne changent rien.

**Uniformité de l'ordre relatif.** Restreinte aux $a+c$ boules rouges et blanches, la permutation induite est encore uniforme (chaque ordre relatif provient du même nombre de permutations totales). En ne distinguant pas les boules d'une même couleur, l'ensemble $\Pi$ des positions occupées par les $c$ blanches parmi les $a+c$ places est uniforme sur les $\binom{a+c}c$ parties à $c$ éléments.

**Loi de $Y$.** Soit $k\in[\![0,a]\!]$. On a $Y=k$ si et seulement si les places $1,\dots,k$ sont rouges et la place $k+1$ est blanche, c'est-à-dire : $k+1\in\Pi$ et $\Pi\subset\{k+1,\dots,a+c\}$. Les $c-1$ autres blanches occupent alors $c-1$ places parmi les $a+c-(k+1)$ places $k+2,\dots,a+c$ :
$$P(Y=k)=\frac{\binom{a+c-k-1}{c-1}}{\binom{a+c}c},\qquad0\le k\le a.$$
Vérification : $\sum_{k=0}^a\binom{a+c-k-1}{c-1}=\sum_{j=c-1}^{a+c-1}\binom j{c-1}=\binom{a+c}c$ (formule de la crosse de hockey), donc les probabilités somment à 1.

**Espérance par indicatrices.** Numérotons les rouges $1,\dots,a$ et notons $R_i$ l'événement « la rouge $i$ sort avant toutes les blanches ». Alors $Y=\sum_{i=1}^a\mathbf 1_{R_i}$. Parmi les $c+1$ boules {rouge $i$ et les $c$ blanches}, l'ordre relatif est uniforme, donc chacune a la même probabilité $\frac1{c+1}$ de sortir la première : $P(R_i)=\frac1{c+1}$. Par linéarité de l'espérance (sans indépendance) :
$$E(Y)=\sum_{i=1}^aP(R_i)=\frac a{c+1}.$$

**Remarque.** Le résultat ne dépend pas de $b$ ; pour $c=1$, $Y$ est uniforme sur $[\![0,a]\!]$ (la blanche est à une position uniforme) et $E(Y)=\frac a2$. ✓
"""

D['m-ccmp-17b'] = r"""
**Idée.** Si $f(x)\approx f(0)+\gamma\sqrt x$, alors $f(x)-f(x/2)\approx\gamma\big(\sqrt x-\sqrt{x/2}\big)=\gamma\big(1-\frac1{\sqrt2}\big)\sqrt x$. Pour retrouver $\sqrt x$, il faut $\gamma\big(1-\frac1{\sqrt2}\big)=1$.

**Calcul de $\gamma$.** $\gamma=\dfrac1{1-1/\sqrt2}=\dfrac{\sqrt2}{\sqrt2-1}=\dfrac{\sqrt2(\sqrt2+1)}{(\sqrt2-1)(\sqrt2+1)}=\dfrac{2+\sqrt2}{1}=2+\sqrt2$.

**Fonction reste.** Posons $g(x)=f(x)-f(0)-\gamma\sqrt x$ pour $x\ge0$. $g$ est continue en 0 avec $g(0)=0$, et
$$g(x)-g\Big(\frac x2\Big)=f(x)-f\Big(\frac x2\Big)-\gamma\Big(\sqrt x-\frac{\sqrt x}{\sqrt2}\Big)=f(x)-f\Big(\frac x2\Big)-\sqrt x.$$
Par hypothèse $f(x)-f(x/2)=\sqrt x+o(\sqrt x)$, donc $g(x)-g(x/2)=o(\sqrt x)$.

**Traduction quantifiée.** Soit $\varepsilon>0$ : il existe $\delta>0$ tel que $|g(t)-g(t/2)|\le\varepsilon\sqrt t$ pour $0<t<\delta$.

**Télescopage.** Soit $0<x<\delta$ et $N\ge1$. Les points $\frac x{2^k}$ ($0\le k<N$) sont dans $]0,\delta[$, donc
$$\big|g(x)-g\big(\tfrac x{2^N}\big)\big|=\Big|\sum_{k=0}^{N-1}\Big(g\big(\tfrac x{2^k}\big)-g\big(\tfrac x{2^{k+1}}\big)\Big)\Big|\le\sum_{k=0}^{N-1}\varepsilon\sqrt{\frac x{2^k}}\le\varepsilon\sqrt x\sum_{k\ge0}\Big(\frac1{\sqrt2}\Big)^k=\gamma\,\varepsilon\sqrt x.$$

**Passage à la limite.** Quand $N\to\infty$, $\frac x{2^N}\to0$ et, par continuité de $g$ en 0, $g\big(\frac x{2^N}\big)\to g(0)=0$. D'où $|g(x)|\le\gamma\varepsilon\sqrt x$ pour tout $x\in]0,\delta[$. Ceci pour tout $\varepsilon>0$ : $g(x)=o(\sqrt x)$.

**Conclusion.**
$$f(x)=f(0)+(2+\sqrt2)\sqrt x+o(\sqrt x)\qquad(x\to0^+).$$
La continuité en 0 est indispensable : elle permet de « remonter » la relation jusqu'en 0.
"""
