# Rédactions « rigoureuses » (copie de concours), lot 1. Résultats vérifiés (voir tools/detail/d62.py).
R = {}

R['m-ccmp-15b'] = r"""**Sens direct.** Supposons $A\setminus\{a\}$ convexe. Soient $x,y\in A$ tels que $a=\frac12(x+y)$. Supposons par l'absurde $x\neq a$. Alors $y=2a-x\neq a$, donc $x,y\in A\setminus\{a\}$. Par convexité de $A\setminus\{a\}$, $\frac12(x+y)\in A\setminus\{a\}$, c'est-à-dire $a\neq a$ : contradiction. Ainsi $x=a$, puis $y=2a-x=a$.

**Réciproque.** Montrons la contraposée : si $A\setminus\{a\}$ n'est pas convexe, il existe $x,y\in A$ avec $a=\frac12(x+y)$ et $x\neq a$.

Par hypothèse, il existe $x,y\in A\setminus\{a\}$ et $t\in[0,1]$ tels que $z=(1-t)x+ty\notin A\setminus\{a\}$. Comme $A$ est convexe, $z\in A$, donc $z=a$. On a $t\notin\{0,1\}$, car sinon $z\in\{x,y\}$ et $z\neq a$. Donc $t\in\,]0,1[$.

Quitte à échanger $x$ et $y$ (ce qui remplace $t$ par $1-t$), on peut supposer $t\le\frac12$. Posons $y'=2a-x$. Alors
$$y'=2(1-t)x+2ty-x=(1-2t)x+2t\,y,\qquad 2t\in\,]0,1].$$
Par convexité de $A$, $y'\in A$. Enfin $a=\frac12(x+y')$ avec $x\in A$, $y'\in A$ et $x\neq a$ : la propriété n'est pas vérifiée.

**Conclusion.**
$$\boxed{a\ \text{extrémal}\iff\big(\forall x,y\in A,\ a=\tfrac12(x+y)\Rightarrow x=y=a\big)}$$"""

R['m-ccmp-19b'] = r"""**Domaine.** Notons $h_x(t)=\dfrac1{t\sqrt{1+tx}}$.
- Si $x<0$, alors $1+tx<0$ pour $t>-\frac1x$ : $h_x$ n'est pas définie sur $[1,+\infty[$ et $f(x)$ n'a pas de sens.
- Si $x=0$, alors $\int_1^X\frac{\mathrm dt}t=\ln X\xrightarrow[X\to+\infty]{}+\infty$ : l'intégrale diverge.
- Si $x>0$, $h_x$ est continue et positive sur $[1,+\infty[$, et $h_x(t)\underset{t\to+\infty}{\sim}\dfrac1{\sqrt x\,t^{3/2}}$. Par comparaison de fonctions positives à une intégrale de Riemann convergente ($\frac32>1$), l'intégrale converge.

Donc $\mathcal D_f=\,]0,+\infty[$.

**Calcul.** Soit $x>0$. L'application $\varphi:t\mapsto\sqrt{1+tx}$ est une bijection de classe $C^1$, strictement croissante, de $[1,+\infty[$ sur $[\sqrt{1+x},+\infty[$. Sa réciproque est $u\mapsto\frac{u^2-1}x$, de dérivée $\frac{2u}x$. Par le théorème de changement de variable pour les intégrales impropres :
$$f(x)=\int_{\sqrt{1+x}}^{+\infty}\frac{\frac{2u}x}{\frac{u^2-1}x\,u}\,\mathrm du=\int_{\sqrt{1+x}}^{+\infty}\frac{2\,\mathrm du}{u^2-1}.$$
Pour $u>1$, $\frac2{u^2-1}=\frac1{u-1}-\frac1{u+1}$, de primitive $G(u)=\ln\frac{u-1}{u+1}$, et $G(u)\xrightarrow[u\to+\infty]{}0$. Donc
$$f(x)=-\ln\frac{\sqrt{1+x}-1}{\sqrt{1+x}+1}=\ln\frac{\big(\sqrt{1+x}+1\big)^2}{(1+x)-1}=2\ln\frac{1+\sqrt{1+x}}{\sqrt x}.$$

**Conclusion.**
$$\boxed{\mathcal D_f=\,]0,+\infty[\quad\text{et}\quad\forall x>0,\ f(x)=2\ln\frac{1+\sqrt{1+x}}{\sqrt x}}$$"""

R['m-ccmp-20a'] = r"""**Définition.** Soit $x>0$. La suite $(n^{-x})_{n\ge1}$ est positive, décroissante et de limite nulle. Par le critère spécial des séries alternées, $\sum\frac{(-1)^{n-1}}{n^x}$ converge : $g$ est définie sur $]0,+\infty[$.

**Classe $C^\infty$.** Posons $u_n(x)=(-1)^{n-1}e^{-x\ln n}$. Chaque $u_n$ est $C^\infty$, avec $u_n^{(k)}(x)=(-1)^{n-1+k}(\ln n)^kn^{-x}$ pour tout $k\in\mathbb N$.

Soient $a>0$ et $k\in\mathbb N^*$. Posons $\varphi_x(t)=(\ln t)^kt^{-x}$ pour $t\ge1$. On a
$$\varphi_x'(t)=t^{-x-1}(\ln t)^{k-1}(k-x\ln t).$$
Soit $N_0=\lceil e^{k/a}\rceil$. Pour tout $x\ge a$ et tout $t\ge N_0$, on a $x\ln t\ge a\cdot\frac ka=k$, donc $\varphi_x'(t)\le0$. Ainsi, pour tout $x\ge a$, la suite $\big((\ln n)^kn^{-x}\big)_{n\ge N_0}$ est décroissante, et elle tend vers $0$ par croissances comparées.

Le critère spécial donne alors, pour $N\ge N_0$ et $x\ge a$ :
$$\Big|\sum_{n>N}u_n^{(k)}(x)\Big|\le(\ln(N+1))^k(N+1)^{-x}\le\frac{(\ln(N+1))^k}{(N+1)^a}\xrightarrow[N\to+\infty]{}0.$$
Le majorant est indépendant de $x$ : $\sum u_n^{(k)}$ converge uniformément sur $[a,+\infty[$, pour tout $k\ge1$. Pour $k=0$, la convergence simple a été établie.

Par le théorème de dérivation terme à terme, $g$ est $C^\infty$ sur $[a,+\infty[$. Ceci valant pour tout $a>0$, $g$ est $C^\infty$ sur $]0,+\infty[$.

**Limite en $0^+$.** Soit $x>0$ et $d_n=n^{-x}-(n+1)^{-x}$. Les séries $\sum(-1)^{n-1}n^{-x}$ et $\sum(-1)^{n-1}(n+1)^{-x}$ convergent. La seconde vaut $-(g(x)-1)$, par le changement d'indice $m=n+1$. Donc
$$h(x):=\sum_{n\ge1}(-1)^{n-1}d_n=g(x)+g(x)-1,\qquad\text{soit}\qquad g(x)=\frac{1+h(x)}2.$$
Or $d_n=x\int_n^{n+1}t^{-x-1}\,\mathrm dt\ge0$. De plus $d_{n+1}=x\int_n^{n+1}(t+1)^{-x-1}\,\mathrm dt\le d_n$, et $d_n\to0$. Par le critère spécial, $0\le h(x)\le d_1=1-2^{-x}\xrightarrow[x\to0^+]{}0$.

**Conclusion.**
$$\boxed{g\in\mathcal C^\infty\big(]0,+\infty[\big)\qquad\text{et}\qquad\lim_{x\to0^+}g(x)=\frac12}$$"""

R['m-ccmp-21b'] = r"""Notons $d=\|c_1-c_2\|$, avec $r_1,r_2\ge0$.

**1. Boules fermées.** Si $x\in B_f(c_1,r_1)\cap B_f(c_2,r_2)$, l'inégalité triangulaire donne $d\le\|c_1-x\|+\|x-c_2\|\le r_1+r_2$.

Réciproquement, supposons $d\le r_1+r_2$.
- Si $r_1+r_2=0$, alors $d=0$ et $c_1=c_2$ appartient aux deux boules.
- Sinon, posons $x=c_1+\frac{r_1}{r_1+r_2}(c_2-c_1)$. Alors $\|x-c_1\|=\frac{r_1d}{r_1+r_2}\le r_1$ et $\|x-c_2\|=\frac{r_2d}{r_1+r_2}\le r_2$.
$$\boxed{B_f(c_1,r_1)\cap B_f(c_2,r_2)\neq\emptyset\iff d\le r_1+r_2}$$

**2. Sphères ($\dim E\ge2$).** *Condition nécessaire.* Soit $x$ avec $\|x-c_1\|=r_1$ et $\|x-c_2\|=r_2$. Alors $d\le r_1+r_2$, $r_1\le r_2+d$ et $r_2\le r_1+d$, donc $|r_1-r_2|\le d\le r_1+r_2$.

*Condition suffisante.* Supposons $|r_1-r_2|\le d\le r_1+r_2$.
- Si $d=0$, alors $r_1=r_2$ et les deux sphères sont égales. Elles sont non vides, car $E\neq\{0\}$.
- Si $d>0$, posons $u=\frac{c_2-c_1}d$. Comme $\dim E\ge2$, il existe $v$ unitaire orthogonal à $u$. Posons
$$\alpha=\frac{d^2+r_1^2-r_2^2}{2d}.$$
On a $|r_1-r_2|\le d\le r_1+r_2$, soit $(d-r_1)^2\le r_2^2\le(d+r_1)^2$. Cela équivaut à $|d^2+r_1^2-r_2^2|\le2dr_1$, donc à $\alpha^2\le r_1^2$. On pose alors $\beta=\sqrt{r_1^2-\alpha^2}$ et $x=c_1+\alpha u+\beta v$. Par le théorème de Pythagore :
$$\|x-c_1\|^2=\alpha^2+\beta^2=r_1^2,\qquad\|x-c_2\|^2=(\alpha-d)^2+\beta^2=r_1^2-2\alpha d+d^2=r_2^2.$$
$$\boxed{S(c_1,r_1)\cap S(c_2,r_2)\neq\emptyset\iff|r_1-r_2|\le d\le r_1+r_2}$$"""

R['m-ccmp-26a'] = r"""**1. Existence de $P$.** Soit $\theta\in\mathbb R$. Par la formule de Moivre et le binôme,
$$\sin(2n\theta)=\operatorname{Im}\big((\cos\theta+i\sin\theta)^{2n}\big)=\sum_{\substack{1\le j\le2n-1\\ j\text{ impair}}}\binom{2n}j(-1)^{\frac{j-1}2}\cos^{2n-j}\theta\,\sin^j\theta.$$
Pour $j$ impair, $\sin^j\theta=\sin\theta\,(1-\cos^2\theta)^{\frac{j-1}2}$. Le polynôme
$$P=\sum_{\substack{1\le j\le2n-1\\ j\text{ impair}}}\binom{2n}j(-1)^{\frac{j-1}2}X^{2n-j}(1-X^2)^{\frac{j-1}2}$$
vérifie donc $\sin(2n\theta)=\sin\theta\,P(\cos\theta)$ pour tout $\theta$.

**2. Degré, coefficient dominant, terme constant.** Chaque terme est de degré $(2n-j)+(j-1)=2n-1$, de coefficient dominant $\binom{2n}j(-1)^{\frac{j-1}2}(-1)^{\frac{j-1}2}=\binom{2n}j>0$. Ces coefficients s'ajoutent sans compensation : $\deg P=2n-1$ et le coefficient dominant vaut
$$\sum_{j\text{ impair}}\binom{2n}j=\frac{(1+1)^{2n}-(1-1)^{2n}}2=2^{2n-1}.$$
En $\theta=\frac\pi2$ : $0=\sin(n\pi)=1\cdot P(0)$, donc $P(0)=0$.

**3. Racines.** $\sin(2n\theta)=0\iff\theta\in\frac\pi{2n}\mathbb Z$. Pour $1\le k\le2n-1$, posons $\theta_k=\frac{k\pi}{2n}\in\,]0,\pi[$. Alors $\sin\theta_k\neq0$, donc $P(c_k)=0$ avec $c_k=\cos\theta_k$. La fonction $\cos$ est injective sur $]0,\pi[$ : les $c_k$ sont $2n-1$ réels distincts. Comme $\deg P=2n-1$, ce sont toutes les racines, et
$$P=2^{2n-1}\prod_{k=1}^{2n-1}(X-c_k).$$

**4. Produit.** Pour $1\le k\le n-1$, $c_{2n-k}=-c_k$, et $c_n=0$. D'où $P=X\,R$ avec $R=2^{2n-1}\prod_{k=1}^{n-1}(X^2-c_k^2)$, puis
$$P'(0)=R(0)=2^{2n-1}(-1)^{n-1}\prod_{k=1}^{n-1}c_k^2.$$
D'autre part, $g:\theta\mapsto P(\cos\theta)=\frac{\sin(2n\theta)}{\sin\theta}$ est dérivable sur $]0,\pi[$, avec $g'(\theta)=-\sin\theta\,P'(\cos\theta)$. La dérivée du quotient en $\frac\pi2$ donne $g'(\frac\pi2)=2n\cos(n\pi)=2n(-1)^n$. Donc $P'(0)=-g'(\frac\pi2)=2n(-1)^{n-1}$.

En identifiant, $\prod_{k=1}^{n-1}c_k^2=\frac{2n}{2^{2n-1}}=\frac n{4^{n-1}}$. Comme $c_k>0$ pour $1\le k\le n-1$ :
$$\boxed{\begin{aligned}&\deg P=2n-1,\quad\text{coefficient dominant }2^{2n-1},\quad P(0)=0\\&\prod_{k=1}^{n-1}\cos\frac{k\pi}{2n}=\frac{\sqrt n}{2^{n-1}}\end{aligned}}$$"""
