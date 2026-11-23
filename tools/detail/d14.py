D = {}

D['m-ccs-06'] = r"""
**1. Définition.** Une fonction $\varphi$ est développable en série entière (DSE) en 0 s'il existe $r>0$ et une suite $(a_n)$ tels que $\varphi(x)=\sum_{n\ge0}a_nx^n$ pour tout $x\in]-r,r[$. Exemple : $e^x=\sum_{n\ge0}\frac{x^n}{n!}$ pour tout $x\in\mathbb R$.

**2. Prolongement.** $e^x-1\sim x$ en 0, donc $f(x)\to1$ : on pose $f(0)=1$.

**3. Développement de $f$.** Pour $x\neq0$ :
$$f(x)=\frac1x\Big(\sum_{n\ge0}\frac{x^n}{n!}-1\Big)=\frac1x\sum_{n\ge1}\frac{x^n}{n!}=\sum_{n\ge1}\frac{x^{n-1}}{n!}=\sum_{n\ge0}\frac{x^n}{(n+1)!},$$
et cette formule donne aussi $f(0)=1$. Le rayon est infini (d'Alembert : $\frac{(n+1)!}{(n+2)!}\to0$). La somme d'une série entière est $C^\infty$ sur son intervalle de convergence et $a_n=\frac{f^{(n)}(0)}{n!}$ : donc $f$ est $C^\infty$ sur $\mathbb R$ et
$$f^{(n)}(0)=n!\cdot\frac1{(n+1)!}=\frac1{n+1}.$$

**4. Écriture $f=1-h$.** On travaille sur $\mathbb C$ (même formule) : $f(z)=1-h(z)$ avec $h(z)=-\sum_{n\ge1}\frac{z^n}{(n+1)!}$. Pour $|z|\le r<1$ :
$$|h(z)|\le\sum_{n\ge1}\frac{|z|^n}{(n+1)!}\le\sum_{n\ge1}\frac1{(n+1)!}=e-2<1.$$
Donc $f(z)\neq0$ et $g(z)=\frac1{f(z)}=\frac1{1-h(z)}=\sum_{k\ge0}h(z)^k$ (série géométrique).

**4. Réarrangement en série entière.** Développons chaque $h^k$ en série entière (produit de Cauchy) : $h(z)^k=\sum_mc_{k,m}z^m$. En majorant les coefficients par leurs modules, $\sum_m|c_{k,m}|r^m\le\big(\sum_{n\ge1}\frac{r^n}{(n+1)!}\big)^k\le(e-2)^k$. La famille double $(c_{k,m}z^m)_{k,m}$ est donc sommable pour $|z|\le r$ (somme des modules $\le\sum_k(e-2)^k=\frac1{3-e}$). On peut sommer par paquets dans l'autre ordre :
$$g(z)=\sum_{m\ge0}\Big(\sum_{k\ge0}c_{k,m}\Big)z^m=\sum_mb_mz^m\qquad(|z|\le r).$$
Ceci vaut pour tout $r<1$ : $g$ est DSE, avec un rayon $R\ge1$.

**5. Majoration du rayon.** Supposons $R>2\pi$ et notons $G(z)=\sum b_mz^m$ sur le disque ouvert $D(0,R)$. Le produit de Cauchy $G\cdot f$ est une série entière de rayon $\ge R$ ; sur $]-1,1[$ elle vaut $g\cdot f=1$, donc tous ses coefficients sont ceux de la constante 1 (unicité du développement) : $G(z)f(z)=1$ pour tout $z\in D(0,R)$. Mais $2i\pi\in D(0,R)$ et
$$f(2i\pi)=\frac{e^{2i\pi}-1}{2i\pi}=0,$$
donc $1=G(2i\pi)\cdot0=0$ : contradiction. Ainsi $1\le R\le2\pi$.

**Complément.** En fait $R=2\pi$ (les zéros de $f$ les plus proches de 0 sont $\pm2i\pi$), et $g(x)=\frac x{e^x-1}=\sum_nB_n\frac{x^n}{n!}$ définit les nombres de Bernoulli ($B_0=1$, $B_1=-\frac12$, $B_2=\frac16$).
"""

D['m-ccs-07'] = r"""
**1. Énoncé.** Si $(f_n)$ est une suite de fonctions continues sur le segment $[a,b]$ qui converge uniformément vers $f$, alors $f$ est continue et $\int_a^bf_n\to\int_a^bf$.

**1. Démonstration.** $f$ est continue comme limite uniforme de fonctions continues (théorème du cours), donc intégrable sur $[a,b]$. Par linéarité et croissance de l'intégrale :
$$\Big|\int_a^bf_n-\int_a^bf\Big|=\Big|\int_a^b(f_n-f)\Big|\le\int_a^b|f_n-f|\le(b-a)\,\|f_n-f\|_\infty\xrightarrow[n\to\infty]{}0.$$

**2. Unicité : réduction.** Soient $u_1,u_2$ deux solutions et $w=u_1-u_2$. Par linéarité, $\partial_tw=\partial_x^2w$, $w(0,t)=w(L,t)=0$ et $w(x,0)=0$. Il suffit de montrer $w=0$.

**2. Énergie.** Posons $E(t)=\int_0^Lw(x,t)^2\,\mathrm dx$. La fonction $(x,t)\mapsto w^2$ est $C^1$ sur le compact $[0,L]\times[0,T]$, donc $\partial_t(w^2)=2w\,\partial_tw$ est continue et bornée : on peut dériver sous l'intégrale. Avec l'équation $\partial_tw=\partial_x^2w$ :
$$E'(t)=\int_0^L2w\,\partial_tw\,\mathrm dx=2\int_0^Lw\,\partial_x^2w\,\mathrm dx.$$

**2. Intégration par parties en $x$.** Avec $u=w$ et $v'=\partial_x^2w$ :
$$\int_0^Lw\,\partial_x^2w\,\mathrm dx=\big[w\,\partial_xw\big]_{x=0}^{x=L}-\int_0^L(\partial_xw)^2\,\mathrm dx=-\int_0^L(\partial_xw)^2\,\mathrm dx,$$
car $w(0,t)=w(L,t)=0$. Donc $E'(t)=-2\int_0^L(\partial_xw)^2\le0$.

**2. Conclusion.** $E$ est décroissante, positive, et $E(0)=\int_0^Lw(x,0)^2=0$. Donc $0\le E(t)\le E(0)=0$ : $E\equiv0$. Pour chaque $t$, $x\mapsto w(x,t)^2$ est continue, positive, d'intégrale nulle : elle est nulle. Ainsi $w=0$ et la solution est unique.

**3.(a) Séparation des variables.** Soit $u=\varphi(x)\psi(t)$ non nulle. L'équation donne $\varphi(x)\psi'(t)=\varphi''(x)\psi(t)$. En un point où $\varphi(x)\psi(t)\neq0$, $\frac{\varphi''(x)}{\varphi(x)}=\frac{\psi'(t)}{\psi(t)}$ : le membre de gauche ne dépend que de $x$, celui de droite que de $t$, ils sont donc égaux à une même constante $-\lambda$. Ainsi $\psi'=-\lambda\psi$ (donc $\psi(t)=\psi(0)e^{-\lambda t}$) et $\varphi''+\lambda\varphi=0$, avec $\varphi(0)=\varphi(L)=0$ (conditions aux limites, $\psi\not\equiv0$).
- $\lambda<0$ : $\varphi=a\,\mathrm{ch}(\sqrt{-\lambda}x)+b\,\mathrm{sh}(\sqrt{-\lambda}x)$ ; $\varphi(0)=0$ donne $a=0$, puis $\varphi(L)=b\,\mathrm{sh}(\sqrt{-\lambda}L)=0$ donne $b=0$.
- $\lambda=0$ : $\varphi=ax+b$, et $\varphi(0)=\varphi(L)=0$ donne $a=b=0$.
- $\lambda>0$ : $\varphi=a\cos(\sqrt\lambda x)+b\sin(\sqrt\lambda x)$ ; $\varphi(0)=0$ donne $a=0$ ; $\varphi(L)=b\sin(\sqrt\lambda L)=0$ avec $b\neq0$ impose $\sqrt\lambda L=k\pi$, $k\in\mathbb N^*$.

Les solutions à variables séparées sont donc, à une constante près, $u_k(x,t)=e^{-k^2\pi^2t/L^2}\sin\frac{k\pi x}L$, $k\ge1$.

**3.(b) Superposition.** Si $f(x)=\sum_{k\ge1}b_k\sin\frac{k\pi x}L$ avec $\sum|b_k|<\infty$, on propose
$$u(x,t)=\sum_{k\ge1}b_k\,e^{-k^2\pi^2t/L^2}\sin\frac{k\pi x}L.$$
- La série converge normalement sur $[0,L]\times[0,T]$ ($|{\rm terme}|\le|b_k|$) : $u$ est continue et $u(x,0)=f(x)$, $u(0,t)=u(L,t)=0$.
- Pour $t\ge t_0>0$, les dérivées terme à terme sont majorées par $|b_k|\big(\frac{k\pi}L\big)^2e^{-k^2\pi^2t_0/L^2}$, terme d'une série convergente : on peut dériver terme à terme, et chaque terme vérifie l'équation, donc $u$ aussi.

Par la question 2, c'est l'unique solution. Les modes élevés s'éteignent très vite (facteur $e^{-k^2\pi^2t/L^2}$) : la chaleur lisse instantanément le profil initial.
"""

D['m-ccs-10'] = r"""
**1. Règle de d'Alembert.** Si $u_n>0$ et $\frac{u_{n+1}}{u_n}\to\ell$, la série $\sum u_n$ converge si $\ell<1$ et diverge grossièrement si $\ell>1$.

**1. Rapport des coefficients binomiaux.** $\binom{2n+2}{n+1}=\frac{(2n+2)!}{(n+1)!^2}=\frac{(2n+2)(2n+1)}{(n+1)^2}\binom{2n}n$, donc
$$\frac{\binom{2n}n}{\binom{2n+2}{n+1}}=\frac{(n+1)^2}{(2n+2)(2n+1)}\xrightarrow[n\to\infty]{}\frac14.$$
Avec $u_n=\frac1{n^p\binom{2n}n}$ : $\frac{u_{n+1}}{u_n}=\big(\frac n{n+1}\big)^p\frac{\binom{2n}n}{\binom{2n+2}{n+1}}\to\frac14<1$. Donc $A_p$ converge pour tout $p\in\mathbb N$.

**2. Rayon.** Posons $c_n=\frac{2^{2n-1}}{n^2\binom{2n}n}$. Alors
$$\frac{c_{n+1}}{c_n}=4\cdot\frac{n^2}{(n+1)^2}\cdot\frac{(n+1)^2}{(2n+2)(2n+1)}=\frac{4n^2}{(2n+2)(2n+1)}\xrightarrow[n\to\infty]{}1.$$
Pour $x\neq0$, le rapport des termes consécutifs de $\sum c_nx^{2n}$ vaut $\frac{c_{n+1}}{c_n}x^2\to x^2$ : convergence si $|x|<1$, divergence si $|x|>1$. Le rayon vaut **1**.

**2. Bord.** Par Stirling, $\binom{2n}n\sim\frac{4^n}{\sqrt{\pi n}}$, donc $c_n\sim\frac{4^n/2}{n^2\cdot4^n/\sqrt{\pi n}}=\frac{\sqrt\pi}{2n^{3/2}}$, terme d'une série convergente. Pour $|x|\le1$, $|c_nx^{2n}|\le c_n$ : convergence normale sur $[-1,1]$, et $S$ est continue sur $[-1,1]$.

**3. Équation vérifiée par $\arcsin^2$.** Soit $y=\arcsin^2$ sur $]-1,1[$. $y'=\frac{2\arcsin x}{\sqrt{1-x^2}}$, soit $\sqrt{1-x^2}\,y'=2\arcsin x$. En dérivant :
$$\sqrt{1-x^2}\,y''-\frac x{\sqrt{1-x^2}}\,y'=\frac2{\sqrt{1-x^2}}\quad\Longrightarrow\quad(1-x^2)y''-xy'=2,$$
avec $y(0)=0$ et $y'(0)=0$.

**3. Équation vérifiée par $S$.** Sur $]-1,1[$, $S=\sum_{n\ge1}c_nx^{2n}$, $S'=\sum2nc_nx^{2n-1}$, $S''=\sum2n(2n-1)c_nx^{2n-2}$. Alors
$$(1-x^2)S''-xS'=\sum_{n\ge1}2n(2n-1)c_nx^{2n-2}-\sum_{n\ge1}\big[2n(2n-1)+2n\big]c_nx^{2n}.$$
Dans la première somme, on pose $n=m+1$ : $\sum_{m\ge0}(2m+2)(2m+1)c_{m+1}x^{2m}$. Le terme $m=0$ vaut $2c_1=2\cdot\frac{2}{1\cdot2}=2$. Pour $m\ge1$, le coefficient de $x^{2m}$ est $(2m+2)(2m+1)c_{m+1}-(2m)^2c_m=0$, d'après le rapport calculé en 2. Donc $(1-x^2)S''-xS'=2$, avec $S(0)=0$ et $S'(0)=0$.

**3. Conclusion.** Sur $]-1,1[$, l'équation $y''=\frac{xy'+2}{1-x^2}$ est linéaire à coefficients continus : le problème de Cauchy en 0 a une unique solution. Donc $S=\arcsin^2$ sur $]-1,1[$, et sur $[-1,1]$ par continuité des deux membres.

**Application.** En $x=\frac12$ : $\arcsin^2\frac12=\frac{\pi^2}{36}$ et $c_n\frac1{4^n}=\frac1{2n^2\binom{2n}n}$, d'où
$$A_2=\sum_{n\ge1}\frac1{n^2\binom{2n}n}=2\cdot\frac{\pi^2}{36}=\frac{\pi^2}{18}.$$
En $x=1$ : $\sum_{n\ge1}\frac{2^{2n-1}}{n^2\binom{2n}n}=\arcsin^21=\frac{\pi^2}4$.
===RÉPONSE===
Rayon 1 ; $S(x)=\arcsin^2x$ sur $[-1,1]$ ; en $x=\frac12$ : $A_2=\sum\frac1{n^2\binom{2n}n}=\frac{\pi^2}{18}$.
"""
