D = {}

D['n-m-phiX1'] = r"""
**1. Linéarité.** Pour $P,Q\in\mathbb R_n[X]$ et $\lambda\in\mathbb R$, la dérivation est linéaire, donc
$$\varphi(\lambda P+Q)=(X-1)(\lambda P'+Q')=\lambda(X-1)P'+(X-1)Q'=\lambda\varphi(P)+\varphi(Q).$$

**1. Stabilité.** Si $\deg P\le n$, alors $\deg P'\le n-1$ (ou $P'=0$), donc $\deg\big((X-1)P'\big)\le1+(n-1)=n$. Ainsi $\varphi(P)\in\mathbb R_n[X]$, et $\varphi$ est un endomorphisme de $\mathbb R_n[X]$.

**2. Base adaptée.** La famille $\big((X-1)^k\big)_{0\le k\le n}$ est une base de $\mathbb R_n[X]$ : elle contient $n+1$ polynômes de degrés échelonnés $0,1,\dots,n$, donc elle est libre, et $\dim\mathbb R_n[X]=n+1$. (C'est la base de Taylor en 1.)

**2. Image des vecteurs de base.** Pour $k\ge1$, $\big((X-1)^k\big)'=k(X-1)^{k-1}$, donc
$$\varphi\big((X-1)^k\big)=(X-1)\cdot k(X-1)^{k-1}=k(X-1)^k.$$
Pour $k=0$, $\varphi(1)=0=0\cdot1$. Chaque $(X-1)^k$ est donc un vecteur propre, associé à la valeur propre $k$.

**2. Matrice.** Dans cette base, $\mathrm{Mat}(\varphi)=\mathrm{diag}(0,1,2,\dots,n)$.

**2. Conclusion.** $\varphi$ est **diagonalisable**, puisqu'il existe une base de vecteurs propres. Ses valeurs propres sont $0,1,\dots,n$, soit $n+1$ valeurs distinctes en dimension $n+1$ : chacune est simple, et
$$E_k=\mathrm{Ker}(\varphi-k\,\mathrm{id})=\mathrm{Vect}\big((X-1)^k\big),\qquad k\in[\![0,n]\!].$$
En particulier, $\mathrm{Ker}\,\varphi=\mathbb R_0[X]$ (les constantes).

**Variante sans deviner la base.** On résout $\varphi(P)=\lambda P$ avec $P$ de degré $d$ et de coefficient dominant $a\ne0$. Le coefficient de $X^d$ dans $(X-1)P'$ vaut $da$, donc $\lambda=d$. Ensuite, $(X-1)P'=dP$ est une équation différentielle dont les solutions polynomiales sont les $c(X-1)^d$.
"""

D['n-m-ln1t'] = r"""
**1. Développement de $\ln(1+t)$.** Pour $|t|<1$, $\frac1{1+t}=\sum_{n\ge0}(-1)^nt^n$ (série géométrique). En intégrant terme à terme sur $[0,t]$ (une série entière s'intègre terme à terme sur l'intervalle ouvert de convergence) :
$$\ln(1+t)=\sum_{n=0}^{+\infty}\frac{(-1)^nt^{n+1}}{n+1}=\sum_{n=1}^{+\infty}\frac{(-1)^{n+1}}nt^n.$$
Le rayon de convergence vaut 1 (règle de d'Alembert : $\frac{1/(n+1)}{1/n}\to1$). En $t=1$, la série converge (série alternée) et l'égalité est encore vraie (théorème d'Abel), d'où $\ln2=\sum\frac{(-1)^{n+1}}n$.

**2. Existence de l'intégrale.** $f(t)=\frac{\ln(1+t)}t$ est continue sur $]0,1]$. En $0$, $\ln(1+t)\sim t$, donc $f(t)\to1$ : $f$ se prolonge par continuité en $0$, et l'intégrale sur le segment $[0,1]$ existe. Ce n'est pas une vraie intégrale impropre.

**2. Développement de l'intégrande.** Pour $t\in]0,1]$, en divisant par $t$ :
$$f(t)=\sum_{n=1}^{+\infty}f_n(t),\qquad f_n(t)=\frac{(-1)^{n+1}t^{n-1}}n,$$
et l'égalité vaut aussi en $t=0$ (les deux membres valent 1).

**2. Convergence uniforme.** Pour $t\in[0,1]$ fixé, $\big(\frac{t^{n-1}}n\big)_n$ est positive, décroissante et tend vers 0 : la série $\sum f_n(t)$ est alternée. Le critère spécial donne une majoration du reste :
$$|R_N(t)|=\Big|\sum_{n>N}f_n(t)\Big|\le|f_{N+1}(t)|=\frac{t^N}{N+1}\le\frac1{N+1}.$$
Cette majoration est indépendante de $t$, donc $\sup_{[0,1]}|R_N|\to0$ : la convergence est uniforme sur le segment $[0,1]$.

**2. Intégration terme à terme.** Elle est licite (convergence uniforme sur un segment) :
$$I=\sum_{n=1}^{+\infty}\int_0^1\frac{(-1)^{n+1}t^{n-1}}n\,\mathrm dt=\sum_{n=1}^{+\infty}\frac{(-1)^{n+1}}n\cdot\frac1n=\sum_{n=1}^{+\infty}\frac{(-1)^{n+1}}{n^2}.$$

**2. Calcul de la somme.** On sépare les termes pairs et impairs (les séries convergent absolument) :
$$\sum_{n\ge1}\frac{(-1)^{n+1}}{n^2}=\sum_{n\ge1}\frac1{n^2}-2\sum_{p\ge1}\frac1{(2p)^2}=\frac{\pi^2}6-\frac24\cdot\frac{\pi^2}6=\frac{\pi^2}6\cdot\frac12.$$
En effet, on soustrait deux fois les termes pairs : une fois pour les retirer, une fois pour les compter négativement. D'où
$$I=\frac{\pi^2}{12}.$$
"""

D['n-m-wallis'] = r"""
**1. Signe et monotonie.** $u_n=\ln\big(1+\frac1n\big)>0$. La suite $\big(1+\frac1n\big)$ est décroissante et $\ln$ est croissante, donc $(u_n)$ est décroissante. Enfin, $u_n\to\ln1=0$.

**1. Critère spécial.** La série $\sum(-1)^nu_n$ vérifie les hypothèses du critère spécial des séries alternées : elle **converge**.

**1. Convergence absolue.** $u_n\sim\frac1n$ et $\sum\frac1n$ diverge, donc, par comparaison de séries à termes positifs, $\sum u_n$ diverge. La série est **semi-convergente**.

**2. Méthode.** La série converge, donc sa somme $S$ est la limite des sommes partielles $S_m$, et en particulier de la sous-suite $(S_{2N})$. On regroupe les termes deux par deux : celui d'indice $2k-1$ (signe $-$) et celui d'indice $2k$ (signe $+$).
$$(-1)^{2k-1}\ln\Big(1+\frac1{2k-1}\Big)+(-1)^{2k}\ln\Big(1+\frac1{2k}\Big)=-\ln\frac{2k}{2k-1}+\ln\frac{2k+1}{2k}=\ln\frac{(2k-1)(2k+1)}{(2k)^2}.$$

**2. Somme partielle.**
$$S_{2N}=\sum_{k=1}^N\ln\frac{4k^2-1}{4k^2}=\ln\prod_{k=1}^N\frac{4k^2-1}{4k^2}=-\ln\prod_{k=1}^N\frac{4k^2}{4k^2-1}.$$

**2. Passage à la limite.** Par la formule de Wallis, le produit tend vers $\frac\pi2$, et $\ln$ est continue en $\frac\pi2$ :
$$S=\lim_{N\to\infty}S_{2N}=-\ln\frac\pi2=\ln\frac2\pi\approx-0{,}452.$$

**Remarque.** Le regroupement des termes est licite ici parce qu'on sait déjà que la série converge (question 1). Pour une série divergente, $S_{2N}$ pourrait converger sans que la série converge, comme pour $\sum(-1)^n$.
"""

D['n-m-arctanx2'] = r"""
**1. Existence.** $f(x)=\frac{\mathrm{Arctan}\,x}{x^2}$ est continue sur $[1,+\infty[$ et positive. Comme $0\le\mathrm{Arctan}\,x\le\frac\pi2$, on a $0\le f(x)\le\frac\pi{2x^2}$. La fonction $x\mapsto\frac1{x^2}$ est intégrable sur $[1,+\infty[$ (intégrale de Riemann, exposant $2>1$). Par comparaison de fonctions positives, $f$ est intégrable et $I$ converge.

**2. Intégration par parties sur $[1,A]$.** On pose $u=\mathrm{Arctan}\,x$, $u'=\frac1{1+x^2}$, $v'=\frac1{x^2}$ et $v=-\frac1x$ (toutes de classe $C^1$ sur le segment) :
$$\int_1^A\frac{\mathrm{Arctan}\,x}{x^2}\mathrm dx=\Big[-\frac{\mathrm{Arctan}\,x}x\Big]_1^A+\int_1^A\frac{\mathrm dx}{x(1+x^2)}.$$
On travaille sur un segment, puis on fait tendre $A$ vers $+\infty$ : c'est plus sûr que de faire l'intégration par parties directement sur l'intervalle infini.

**2. Décomposition en éléments simples.** $\frac1{x(1+x^2)}=\frac ax+\frac{bx+c}{1+x^2}$. En multipliant par $x$ et en faisant $x=0$, on obtient $a=1$. Ensuite, $1=(1+x^2)+(bx+c)x$ donne $b=-1$ et $c=0$. Donc
$$\frac1{x(1+x^2)}=\frac1x-\frac x{1+x^2}.$$

**2. Calcul de l'intégrale rationnelle.**
$$\int_1^A\frac{\mathrm dx}{x(1+x^2)}=\Big[\ln x-\frac12\ln(1+x^2)\Big]_1^A=\ln\frac A{\sqrt{1+A^2}}-\Big(0-\frac12\ln2\Big)=\ln\frac A{\sqrt{1+A^2}}+\frac{\ln2}2.$$

**2. Terme tout intégré.**
$$\Big[-\frac{\mathrm{Arctan}\,x}x\Big]_1^A=-\frac{\mathrm{Arctan}\,A}A+\mathrm{Arctan}\,1=-\frac{\mathrm{Arctan}\,A}A+\frac\pi4.$$

**2. Passage à la limite.** Quand $A\to+\infty$ :
- $\frac{\mathrm{Arctan}\,A}A\to0$, car le numérateur est borné ;
- $\frac A{\sqrt{1+A^2}}=\frac1{\sqrt{1+1/A^2}}\to1$, donc son logarithme tend vers 0.

D'où
$$I=\frac\pi4+\frac{\ln2}2\approx0{,}785+0{,}347=1{,}132.$$
Contrôle : $I\le\frac\pi2\int_1^\infty\frac{\mathrm dx}{x^2}=\frac\pi2\approx1{,}57$, et $I\ge\frac\pi4\int_1^\infty\frac{\mathrm dx}{x^2}=0{,}785$ (car $\mathrm{Arctan}\,x\ge\frac\pi4$ sur $[1,+\infty[$). ✓
"""

D['n-m-symk'] = r"""
**1. Théorème spectral.** $A$ est symétrique réelle : il existe $P\in O_n(\mathbb R)$ (donc $P^{-1}=P^\top$) et $D=\mathrm{diag}(\lambda_1,\dots,\lambda_n)$ à coefficients **réels** telles que $A=PDP^\top$.

**2. Puissances.** Par récurrence, $A^k=PD^kP^\top$, car les facteurs $P^\top P=I_n$ se simplifient : $A^2=PDP^\top PDP^\top=PD^2P^\top$, etc. Donc
$$A^k=I_n\iff PD^kP^\top=I_n\iff D^k=P^\top I_nP=I_n.$$

**3. Valeurs propres.** $D^k=\mathrm{diag}(\lambda_1^k,\dots,\lambda_n^k)=I_n$ donne $\lambda_i^k=1$ pour tout $i$. Un réel $\lambda$ tel que $\lambda^k=1$ vérifie $|\lambda|^k=1$, donc $|\lambda|=1$ et $\lambda=\pm1$ (si $k$ est impair, nécessairement $\lambda=1$).

**4. Conclusion.** $\lambda_i^2=1$ pour tout $i$, donc $D^2=I_n$ et
$$A^2=PD^2P^\top=PP^\top=I_n.$$
Interprétation : $A$ est une **symétrie orthogonale**, par rapport à $E_1(A)$, parallèlement à $E_{-1}(A)=E_1(A)^\perp$. Si $k$ est impair, on a même $A=I_n$.

**5. Contre-exemple sans symétrie.** Soit $R$ la matrice de la rotation d'angle $\frac{2\pi}3$ :
$$R=\begin{pmatrix}\cos\frac{2\pi}3&-\sin\frac{2\pi}3\\\sin\frac{2\pi}3&\cos\frac{2\pi}3\end{pmatrix}=\begin{pmatrix}-\frac12&-\frac{\sqrt3}2\\\frac{\sqrt3}2&-\frac12\end{pmatrix}.$$
$R^3$ est la rotation d'angle $2\pi$, donc $R^3=I_2$. Mais $R^2$ est la rotation d'angle $\frac{4\pi}3$, qui n'est pas l'identité. Le raisonnement échoue car les valeurs propres de $R$, $j=e^{2i\pi/3}$ et $\bar j$, ne sont pas réelles : ce sont des racines cubiques de l'unité différentes de $\pm1$. La symétrie de $A$ sert précisément à garantir des valeurs propres réelles et la diagonalisabilité.
"""

D['n-m-chth'] = r"""
**1. Forme exponentielle.** Pour $n\ge1$, $\mathrm{ch}\frac1n>1$, donc $\mathrm{ch}\frac1n-1>0$ et $u_n$ est bien défini :
$$u_n=e^{v_n},\qquad v_n=\mathrm{th}\Big(\frac1n\Big)\ln\Big(\mathrm{ch}\frac1n-1\Big).$$

**1. Équivalent de $\mathrm{ch}\frac1n-1$.** Avec $\mathrm{ch}\,x=1+\frac{x^2}2+o(x^2)$ en $0$ :
$$\mathrm{ch}\frac1n-1=\frac1{2n^2}\big(1+\varepsilon_n\big),\qquad\varepsilon_n\to0.$$

**1. Logarithme.**
$$\ln\Big(\mathrm{ch}\frac1n-1\Big)=-2\ln n-\ln2+\ln(1+\varepsilon_n)=-2\ln n+O(1)\sim-2\ln n.$$
On ne peut pas passer directement l'équivalent au logarithme ; on développe d'abord, puis on garde le terme dominant.

**1. Limite.** $\mathrm{th}\frac1n\sim\frac1n$, donc
$$v_n\sim\frac1n\cdot(-2\ln n)=-\frac{2\ln n}n\xrightarrow[n\to\infty]{}0$$
par croissances comparées. Par continuité de l'exponentielle, $u_n\to e^0=1$, donc $\ell=1$. C'est une forme indéterminée « $0^0$ ».

**2. Équivalent de $u_n-\ell$.** $v_n\to0$ et $e^x-1\sim x$ en $0$, donc
$$u_n-1=e^{v_n}-1\sim v_n\sim-\frac{2\ln n}n.$$

**2. Nature de la série.** $u_n-1$ est équivalent à une suite négative : il est négatif à partir d'un certain rang. On peut donc appliquer les théorèmes de comparaison à $\sum(1-u_n)$, à termes positifs à partir de ce rang, avec $1-u_n\sim\frac{2\ln n}n$.

**2. Comparaison.** Pour $n\ge3$, $\ln n\ge1$, donc $\frac{2\ln n}n\ge\frac2n$. La série harmonique diverge, donc $\sum\frac{2\ln n}n$ diverge (par comparaison), puis $\sum(1-u_n)$ diverge (par équivalence de termes positifs). Ainsi
$$\sum(u_n-\ell)\ \text{diverge}.$$
C'est une série de Bertrand, $\sum\frac{\ln n}{n^\alpha}$, avec $\alpha=1$ : elle diverge.
"""
