D = {}

D['m-ccmp-26a'] = r"""
**1. Existence de $P$.** Par la formule de Moivre et le binôme de Newton :
$$\cos(2n\theta)+i\sin(2n\theta)=(\cos\theta+i\sin\theta)^{2n}=\sum_{j=0}^{2n}\binom{2n}j\cos^{2n-j}\theta\;i^j\sin^j\theta.$$
On prend la partie imaginaire : seuls les $j$ impairs donnent un $i^j$ imaginaire, avec $i^j=i\cdot(i^2)^{\frac{j-1}2}=i\,(-1)^{\frac{j-1}2}$. Donc
$$\sin(2n\theta)=\sum_{j\text{ impair}}\binom{2n}j(-1)^{\frac{j-1}2}\cos^{2n-j}\theta\,\sin^j\theta.$$
Pour $j$ impair, $\sin^j\theta=\sin\theta\,(\sin^2\theta)^{\frac{j-1}2}=\sin\theta\,(1-\cos^2\theta)^{\frac{j-1}2}$. En factorisant $\sin\theta$, on obtient $\sin(2n\theta)=\sin\theta\,P(\cos\theta)$ avec
$$P=\sum_{j\text{ impair},\,1\le j\le2n-1}\binom{2n}j(-1)^{\frac{j-1}2}X^{2n-j}(1-X^2)^{\frac{j-1}2}.$$

**2. Degré et coefficient dominant.** Le terme d'indice $j$ est de degré $(2n-j)+(j-1)=2n-1$, et son coefficient de $X^{2n-1}$ vaut $\binom{2n}j(-1)^{\frac{j-1}2}\cdot(-1)^{\frac{j-1}2}=\binom{2n}j$ (le coefficient dominant de $(1-X^2)^m$ est $(-1)^m$). Tous ces coefficients sont positifs, donc ne se compensent pas : $\deg P=2n-1$ et le coefficient dominant est
$$\sum_{j\text{ impair}}\binom{2n}j=\frac{(1+1)^{2n}-(1-1)^{2n}}2=2^{2n-1}.$$

**2. Terme constant.** Avec $\theta=\frac\pi2$ ($\cos\theta=0$, $\sin\theta=1$) : $\sin(n\pi)=1\cdot P(0)$, donc $P(0)=0$.

**3. Racines.** $\sin(2n\theta)=0\iff2n\theta\in\pi\mathbb Z\iff\theta=\frac{k\pi}{2n}$, $k\in\mathbb Z$. Pour $\theta_k=\frac{k\pi}{2n}$ avec $1\le k\le2n-1$, on a $\theta_k\in]0,\pi[$, donc $\sin\theta_k\neq0$ et $P(\cos\theta_k)=0$. Les réels $c_k=\cos\theta_k$ sont deux à deux distincts ($\cos$ est injectif sur $]0,\pi[$). On a trouvé $2n-1$ racines distinctes d'un polynôme de degré $2n-1$ : ce sont toutes ses racines, et
$$P=2^{2n-1}\prod_{k=1}^{2n-1}(X-c_k).$$

**4. Regroupement des racines.** $c_{2n-k}=\cos\big(\pi-\frac{k\pi}{2n}\big)=-c_k$ et $c_n=\cos\frac\pi2=0$. En regroupant $k$ et $2n-k$ pour $1\le k\le n-1$ :
$$P=2^{2n-1}X\prod_{k=1}^{n-1}(X-c_k)(X+c_k)=X\,R(X),\qquad R=2^{2n-1}\prod_{k=1}^{n-1}(X^2-c_k^2).$$
Donc $P'=R+XR'$ et $P'(0)=R(0)=2^{2n-1}\prod_{k=1}^{n-1}(-c_k^2)=2^{2n-1}(-1)^{n-1}\prod_{k=1}^{n-1}c_k^2$.

**4. Autre calcul de $P'(0)$.** Sur $]0,\pi[$, $g(\theta)=P(\cos\theta)=\frac{\sin(2n\theta)}{\sin\theta}$. D'une part, $g'(\theta)=-\sin\theta\,P'(\cos\theta)$, donc $g'(\frac\pi2)=-P'(0)$. D'autre part, par la dérivée d'un quotient :
$$g'(\theta)=\frac{2n\cos(2n\theta)\sin\theta-\sin(2n\theta)\cos\theta}{\sin^2\theta},\qquad g'\Big(\frac\pi2\Big)=2n\cos(n\pi)=2n(-1)^n.$$
Donc $P'(0)=-2n(-1)^n=2n(-1)^{n-1}$.

**4. Conclusion.** En égalant : $2^{2n-1}(-1)^{n-1}\prod c_k^2=2n(-1)^{n-1}$, d'où $\prod_{k=1}^{n-1}c_k^2=\frac{2n}{2^{2n-1}}=\frac n{4^{n-1}}$. Pour $1\le k\le n-1$, $\frac{k\pi}{2n}\in]0,\frac\pi2[$ donc $c_k>0$, et
$$\prod_{k=1}^{n-1}\cos\frac{k\pi}{2n}=\frac{\sqrt n}{2^{n-1}}.$$
Vérifications : $n=2$ donne $\cos\frac\pi4=\frac{\sqrt2}2$ ✓ ; $n=3$ donne $\cos\frac\pi6\cos\frac\pi3=\frac{\sqrt3}2\cdot\frac12=\frac{\sqrt3}4$ ✓.
"""

D['m-ccmp-27a'] = r"""
**Étape 1 : restriction à une droite.** Fixons $i\in\{1,\dots,m\}$. $\Omega$ est ouvert, donc il contient une boule $B(a,r)$ ; pour $|t|<r$, $a+te_i\in\Omega$. On pose $\varphi_i(t)=f(a+te_i)$ sur $]-r,r[$. Par la règle de dérivation d'une composée (la dérivée de $t\mapsto a+te_i$ est $e_i$) :
$$\varphi_i'(t)=\frac{\partial f}{\partial x_i}(a+te_i),\qquad\varphi_i''(t)=\frac{\partial^2f}{\partial x_i^2}(a+te_i).$$
$\varphi_i$ est donc $C^2$, avec $\varphi_i''(0)=\partial_i^2f(a)$.

**Étape 2 : minimum de $\varphi_i$.** $f$ a un minimum local en $a$ : il existe $\rho\in]0,r]$ tel que $f(x)\ge f(a)$ pour $\|x-a\|<\rho$. En particulier $\varphi_i(t)\ge\varphi_i(0)$ pour $|t|<\rho$ : $\varphi_i$ a un minimum local en 0, point intérieur, donc $\varphi_i'(0)=0$.

**Étape 3 : signe de la dérivée seconde.** Par Taylor-Young à l'ordre 2 :
$$\varphi_i(t)-\varphi_i(0)=\frac{\varphi_i''(0)}2t^2+o(t^2)=t^2\Big(\frac{\varphi_i''(0)}2+\varepsilon(t)\Big),\qquad\varepsilon(t)\xrightarrow[t\to0]{}0.$$
Si l'on avait $\varphi_i''(0)<0$, pour $t\neq0$ assez petit on aurait $\frac{\varphi_i''(0)}2+\varepsilon(t)<0$, donc $\varphi_i(t)<\varphi_i(0)$ : contradiction avec le minimum. Donc $\partial_i^2f(a)=\varphi_i''(0)\ge0$.

**Conclusion.** Ceci vaut pour chaque $i$, donc
$$\Delta f(a)=\sum_{i=1}^m\frac{\partial^2f}{\partial x_i^2}(a)\ge0.$$
Conséquence (principe du minimum) : une fonction $C^2$ telle que $\Delta f<0$ sur $\Omega$ n'atteint jamais de minimum local dans $\Omega$.
"""

D['m-ccmp-27b'] = r"""
**Énoncé visé.** $\mathrm{Sp}\big(p(u)\big)=p(\mathrm{Sp}\,u)=\{p(\lambda):\lambda\in\mathrm{Sp}\,u\}$.

**Inclusion $p(\mathrm{Sp}\,u)\subset\mathrm{Sp}(p(u))$.** Soit $\lambda\in\mathrm{Sp}\,u$ et $x\neq0$ avec $u(x)=\lambda x$. Par récurrence, $u^k(x)=u^{k-1}(\lambda x)=\lambda u^{k-1}(x)=\dots=\lambda^kx$. Si $p=\sum_ka_kX^k$, par linéarité :
$$p(u)(x)=\sum_ka_ku^k(x)=\sum_ka_k\lambda^kx=p(\lambda)\,x.$$
Comme $x\neq0$, $p(\lambda)$ est valeur propre de $p(u)$.

**Inclusion réciproque : cas $p$ constant.** Si $p=c$, $p(u)=c\,\mathrm{id}$ a pour seule valeur propre $c$. Sur $\mathbb C$ et en dimension finie non nulle, $\chi_u$ a au moins une racine : $\mathrm{Sp}\,u\neq\emptyset$, et pour $\lambda\in\mathrm{Sp}\,u$, $c=p(\lambda)$.

**Inclusion réciproque : cas $\deg p=d\ge1$.** Soit $\mu\in\mathrm{Sp}(p(u))$. Le polynôme $p(X)-\mu$ est de degré $d\ge1$ ; $\mathbb C$ étant algébriquement clos :
$$p(X)-\mu=c\prod_{j=1}^d(X-\alpha_j),\qquad c\neq0.$$
L'application $Q\mapsto Q(u)$ étant un morphisme d'algèbres (elle transforme produits en composées) :
$$p(u)-\mu\,\mathrm{id}=c\,(u-\alpha_1\mathrm{id})\circ(u-\alpha_2\mathrm{id})\circ\cdots\circ(u-\alpha_d\mathrm{id}).$$
Le membre de gauche n'est pas injectif ($\mu$ est valeur propre). Une composée d'applications injectives est injective ; donc l'un au moins des $u-\alpha_j\mathrm{id}$ n'est pas injectif : $\alpha_j\in\mathrm{Sp}\,u$. Et $p(\alpha_j)-\mu=c\prod_k(\alpha_j-\alpha_k)=0$ (le facteur $k=j$ est nul), soit $\mu=p(\alpha_j)\in p(\mathrm{Sp}\,u)$.

**Remarque.** Sur $\mathbb R$, l'inclusion $\subset$ peut être fausse : pour la rotation $u$ d'angle $\frac\pi2$ du plan, $\mathrm{Sp}\,u=\emptyset$, mais $u^2=-\mathrm{id}$ a pour valeur propre $-1$ (avec $p=X^2$).
"""

D['m-ccmp-27c'] = r"""
**Étape 1 : $h(X)$ a une espérance.** $X$ est bornée : $|X|\le M$. Comme $h$ est croissante et positive, $0<h(X)\le h(M)$ : $h(X)$ est une variable discrète bornée, donc d'espérance finie. De même $\mathbf 1_{\{X\ge a\}}$ est bornée et $E\big(\mathbf 1_{\{X\ge a\}}\big)=P(X\ge a)$.

**Étape 2 : inégalité point par point.** Montrons que pour tout $\omega$ :
$$\mathbf 1_{\{X\ge a\}}(\omega)\le\frac{h(X(\omega))}{h(a)}.$$
- Si $X(\omega)\ge a$ : par croissance de $h$, $h(X(\omega))\ge h(a)$, et comme $h(a)>0$, $\frac{h(X(\omega))}{h(a)}\ge1=\mathbf 1_{\{X\ge a\}}(\omega)$.
- Si $X(\omega)<a$ : $\mathbf 1_{\{X\ge a\}}(\omega)=0$ et $\frac{h(X(\omega))}{h(a)}>0$ car $h>0$.

**Étape 3 : passage à l'espérance.** L'espérance est croissante (si $Y\le Z$, $E(Y)\le E(Z)$) et linéaire ($h(a)$ est une constante) :
$$P(X\ge a)=E\big(\mathbf 1_{\{X\ge a\}}\big)\le E\Big(\frac{h(X)}{h(a)}\Big)=\frac{E(h(X))}{h(a)}.$$

**Cas particuliers.**
- $h(x)=e^{tx}$ ($t>0$) : inégalité de Chernoff, $P(X\ge a)\le e^{-ta}E(e^{tX})$, qu'on optimise ensuite en $t$.
- Pour $X\ge0$ et $a>0$, le même argument avec $h(x)=x$ (positive là où vit $X$) redonne l'inégalité de Markov $P(X\ge a)\le\frac{E(X)}a$ ; avec $h(x)=x^2$ appliquée à $|X-E(X)|$, on obtient Bienaymé-Tchebychev.
"""
