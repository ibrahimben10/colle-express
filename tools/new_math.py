# Mathématiques — exercices d'oraux récents (CCINP, Mines-Télécom, Mines-Ponts), corrigés rédigés
from newlib import ex
M = 'Maths'

ex('n-m-max', M, 'Probabilités', 1, 'Maximum de tirages avec remise', 20, r"""
Une urne contient $N$ boules numérotées de $1$ à $N$. On effectue $n$ tirages avec remise et on note $X_i$ le numéro obtenu au $i$-ème tirage. On pose $M_n=\max(X_1,\dots,X_n)$.

1. Calculer $P(M_n\le k)$ pour $k\in[\![0,N]\!]$ et en déduire la loi de $M_n$.
2. Montrer que $E(M_n)=\displaystyle\sum_{i=0}^{N-1}P(M_n>i)$. Déterminer la limite de $E(M_n)$ quand $n\to+\infty$ et l'interpréter.
3. Montrer que $E\big(M_n(M_n-1)\big)=\displaystyle\sum_{i=0}^{N-1}2i\,P(M_n>i)$.
4. En déduire la limite de $V(M_n)$ quand $n\to+\infty$. Interpréter.
""",
r"$(M_n\le k)=\bigcap_i(X_i\le k)$ et les tirages sont indépendants.",
r"Écris $M_n=\sum_{i=0}^{N-1}\mathbf 1_{M_n>i}$ (pour $M_n$ à valeurs dans $[\![1,N]\!]$) et prends l'espérance.",
r"De même, $M_n(M_n-1)=\sum_{i=0}^{M_n-1}2i=\sum_{i=0}^{N-1}2i\,\mathbf 1_{M_n>i}$.",
r"""
**1.** Par indépendance, $P(M_n\le k)=\prod_iP(X_i\le k)=\left(\dfrac kN\right)^n$. Donc, pour $k\in[\![1,N]\!]$ : $P(M_n=k)=P(M_n\le k)-P(M_n\le k-1)=\dfrac{k^n-(k-1)^n}{N^n}$.

**2.** Pour $m\in[\![1,N]\!]$, $m=\sum_{i=0}^{N-1}\mathbf 1_{i<m}$. Donc $M_n=\sum_{i=0}^{N-1}\mathbf 1_{(M_n>i)}$ et, par linéarité, $E(M_n)=\sum_{i=0}^{N-1}P(M_n>i)=\sum_{i=0}^{N-1}\left(1-\left(\frac iN\right)^n\right)$. Pour $i<N$, $(i/N)^n\to0$ : $E(M_n)\to N$. Avec beaucoup de tirages, on finit presque sûrement par tirer la boule $N$.

**3.** Pour $m\in[\![1,N]\!]$ : $\sum_{i=0}^{m-1}2i=m(m-1)$. Donc $M_n(M_n-1)=\sum_{i=0}^{N-1}2i\,\mathbf 1_{(M_n>i)}$ et on prend l'espérance.

**4.** $E(M_n(M_n-1))\to\sum_{i=0}^{N-1}2i=N(N-1)$, donc $V(M_n)=E(M_n(M_n-1))+E(M_n)-E(M_n)^2\to N(N-1)+N-N^2=0$. La loi de $M_n$ se concentre sur la valeur $N$ : $M_n$ converge vers la constante $N$.
""", r"$P(M_n=k)=\frac{k^n-(k-1)^n}{N^n}$ ; $E(M_n)\to N$, $V(M_n)\to0$.")

ex('n-m-euler', M, 'Équations différentielles', 1, 'Une équation d’Euler', 15, r"""
On considère, sur $]0,+\infty[$, l'équation $(E):\ t^2y''+4ty'+2y=0$.

1. Trouver les solutions de la forme $t\mapsto t^r$, $r\in\mathbb R$. En déduire l'ensemble des solutions de $(E)$.
2. Calculer la dérivée seconde de $z(t)=t^2y(t)$. Retrouver le résultat précédent.
3. Résoudre $(E'):\ t^2y''+4ty'+2y=e^t$.
""",
r"$t^r$ est solution si et seulement si $r(r-1)+4r+2=0$.",
r"$(t^2y)''=t^2y''+4ty'+2y$ : l'équation devient $z''=0$ (ou $z''=e^t$).",
r"Pour $(E')$ : $z''=e^t$ s'intègre deux fois directement.",
r"""
**1.** $t^r$ est solution ssi $r(r-1)+4r+2=r^2+3r+2=0$, soit $r=-1$ ou $r=-2$. L'équation, linéaire d'ordre 2 à coefficient dominant $t^2$ qui ne s'annule pas sur $]0,+\infty[$, a un espace de solutions de dimension 2. Les fonctions $t\mapsto1/t$ et $t\mapsto1/t^2$ sont libres, donc $S=\left\{t\mapsto\dfrac at+\dfrac b{t^2},\ (a,b)\in\mathbb R^2\right\}$.

**2.** $z'=2ty+t^2y'$ et $z''=2y+4ty'+t^2y''$. Ainsi $(E)\iff z''=0\iff z=at+b\iff y=\dfrac{at+b}{t^2}$ : même résultat.

**3.** $(E')\iff z''=e^t\iff z=e^t+at+b$, donc $y(t)=\dfrac{e^t+at+b}{t^2}$, $(a,b)\in\mathbb R^2$. (La méthode de variation des constantes donne le même résultat, plus laborieusement.)
""", r"$y=\frac at+\frac b{t^2}$ ; pour $(E')$ : $y=\frac{e^t+at+b}{t^2}$.")

ex('n-m-abb', M, 'Algèbre euclidienne', 1, 'Une matrice symétrique 3×3', 15, r"""
Soient $(a,b)\in\mathbb R^2$ avec $b\neq0$, et $A=\begin{pmatrix}a&b&b\\b&a&b\\b&b&a\end{pmatrix}$.

1. Déterminer le rang de $A-(a-b)I_3$. En déduire les valeurs propres de $A$ et les sous-espaces propres.
2. Déterminer une matrice orthogonale $P$ et une matrice diagonale $D$ telles que $A=PDP^{\top}$.
3. On suppose $a=3$ et $b=2$. Montrer que $(X,Y)\mapsto X^{\top}AY$ est un produit scalaire sur $\mathcal M_{3,1}(\mathbb R)$.
""",
r"$A-(a-b)I_3=bJ$ où $J$ est la matrice dont tous les coefficients valent 1.",
r"$a-b$ est valeur propre d'ordre au moins 2 ; la trace donne la troisième, avec le vecteur propre $(1,1,1)^\top$.",
r"Une forme bilinéaire symétrique $X^\top AY$ est définie positive ssi toutes les valeurs propres de $A$ sont strictement positives.",
r"""
**1.** $A-(a-b)I_3=bJ$ avec $J$ de rang 1 ($b\neq0$) : $\dim E_{a-b}=2$, avec $E_{a-b}=\{x+y+z=0\}$. La trace vaut $3a=2(a-b)+\lambda$, d'où $\lambda=a+2b$, de vecteur propre $(1,1,1)^\top$ (somme des coefficients de chaque ligne). Comme $b\neq0$, $a+2b\neq a-b$.

**2.** $A$ est symétrique réelle : ses sous-espaces propres sont orthogonaux. On prend une base orthonormée adaptée :
$$P=\begin{pmatrix}\frac1{\sqrt3}&\frac1{\sqrt2}&\frac1{\sqrt6}\\\frac1{\sqrt3}&-\frac1{\sqrt2}&\frac1{\sqrt6}\\\frac1{\sqrt3}&0&-\frac2{\sqrt6}\end{pmatrix},\qquad D=\mathrm{diag}(a+2b,a-b,a-b).$$
$P$ est orthogonale, donc $P^{-1}=P^\top$ et $A=PDP^\top$.

**3.** $(X,Y)\mapsto X^\top AY$ est bilinéaire et symétrique ($A^\top=A$). Avec $X'=P^\top X$ : $X^\top AX=X'^\top DX'=7x_1'^2+x_2'^2+x_3'^2\ge0$, avec égalité ssi $X'=0$ ssi $X=0$. C'est un produit scalaire.
""", r"Valeurs propres $a-b$ (double, plan $x+y+z=0$) et $a+2b$ (droite $(1,1,1)$) ; pour $a=3$, $b=2$ : 7 et 1 > 0, produit scalaire.")

ex('n-m-antisym', M, 'Algèbre euclidienne', 1, 'Endomorphisme antisymétrique : rang pair', 20, r"""
Soit $E$ un espace euclidien et $u\in\mathcal L(E)$ tel que $\langle u(x),x\rangle=0$ pour tout $x\in E$.

1. Montrer que $\langle u(y),z\rangle=-\langle y,u(z)\rangle$ pour tous $y,z\in E$.
2. Montrer que $\mathrm{Ker}\,u$ et $\mathrm{Im}\,u$ sont supplémentaires orthogonaux.
3. On note $v$ l'endomorphisme induit par $u$ sur $\mathrm{Im}\,u$. Montrer que $v$ n'a aucune valeur propre réelle.
4. Quels sont les polynômes réels qui ne s'annulent pas sur $\mathbb R$ ? En déduire que le rang de $u$ est pair.
""",
r"Développe $\langle u(y+z),y+z\rangle=0$.",
r"$y\in\mathrm{Ker}\,u\iff\forall z,\ \langle u(y),z\rangle=0\iff\forall z,\ \langle y,u(z)\rangle=0$ : donc $\mathrm{Ker}\,u=(\mathrm{Im}\,u)^\perp$.",
r"$v$ est injectif car $\mathrm{Ker}\,u\cap\mathrm{Im}\,u=\{0\}$ ; si $v(x)=\lambda x$ avec $x\neq0$, calcule $\langle v(x),x\rangle$.",
r"""
**1.** $0=\langle u(y+z),y+z\rangle=\langle u(y),y\rangle+\langle u(y),z\rangle+\langle u(z),y\rangle+\langle u(z),z\rangle=\langle u(y),z\rangle+\langle u(z),y\rangle$.

**2.** $y\in\mathrm{Ker}\,u\iff\forall z,\ \langle u(y),z\rangle=0\iff\forall z,\ \langle y,u(z)\rangle=0\iff y\in(\mathrm{Im}\,u)^\perp$. Donc $\mathrm{Ker}\,u=(\mathrm{Im}\,u)^\perp$ et $E=\mathrm{Im}\,u\oplus^\perp\mathrm{Ker}\,u$.

**3.** $\mathrm{Im}\,u$ est stable par $u$ ; $\mathrm{Ker}\,v=\mathrm{Ker}\,u\cap\mathrm{Im}\,u=\{0\}$, donc $v$ est un automorphisme de $\mathrm{Im}\,u$. Si $v(x)=\lambda x$ avec $x\neq0$ et $\lambda\in\mathbb R$ : $0=\langle v(x),x\rangle=\lambda\|x\|^2$, donc $\lambda=0$, ce qui contredit l'injectivité. $v$ n'a pas de valeur propre réelle.

**4.** Un polynôme réel de degré impair a une racine réelle (théorème des valeurs intermédiaires, limites $\pm\infty$ opposées). Les polynômes sans racine réelle sont donc de degré pair (par exemple les produits de trinômes de discriminant négatif, à constante près). $\chi_v$ n'a pas de racine réelle par 3, donc $\deg\chi_v=\dim\mathrm{Im}\,u=\mathrm{rg}\,u$ est pair.
""", r"$\mathrm{Ker}\,u=(\mathrm{Im}\,u)^\perp$ ; $v$ sans valeur propre réelle ; $\chi_v$ sans racine réelle, donc $\mathrm{rg}\,u$ pair.")

ex('n-m-phiX1', M, 'Réduction', 1, 'L’endomorphisme P ↦ (X−1)P′', 10, r"""
Soit $n\in\mathbb N^*$ et $\varphi:\mathbb R_n[X]\to\mathbb R[X]$ définie par $\varphi(P)=(X-1)P'$.

1. Montrer que $\varphi$ est un endomorphisme de $\mathbb R_n[X]$.
2. Déterminer ses valeurs propres et ses sous-espaces propres. $\varphi$ est-il diagonalisable ?
""",
r"Linéarité immédiate ; $\deg\big((X-1)P'\big)\le\deg P$.",
r"Travaille dans la base $\big((X-1)^k\big)_{0\le k\le n}$ (formule de Taylor en 1).",
r"$\varphi\big((X-1)^k\big)=k(X-1)^k$.",
r"""
**1.** $\varphi$ est linéaire (la dérivation l'est). Si $\deg P\le n$, alors $\deg P'\le n-1$ et $\deg\varphi(P)\le n$ : $\varphi$ est un endomorphisme de $\mathbb R_n[X]$.

**2.** $\big((X-1)^k\big)_{0\le k\le n}$ est une base de $\mathbb R_n[X]$ (polynômes de degrés échelonnés) et $\varphi\big((X-1)^k\big)=(X-1)\cdot k(X-1)^{k-1}=k(X-1)^k$. La matrice de $\varphi$ dans cette base est $\mathrm{diag}(0,1,\dots,n)$. Valeurs propres : $0,1,\dots,n$, toutes simples, de sous-espaces propres $E_k=\mathrm{Vect}\big((X-1)^k\big)$. $\varphi$ est diagonalisable ($n+1$ valeurs propres distinctes en dimension $n+1$).
""", r"Valeurs propres $0,1,\dots,n$, $E_k=\mathrm{Vect}((X-1)^k)$ ; diagonalisable.")

ex('n-m-ln1t', M, 'Séries entières', 1, 'Intégrale de ln(1+t)/t', 15, r"""
On admet que $\displaystyle\sum_{n=1}^{+\infty}\frac1{n^2}=\frac{\pi^2}6$.

1. Rappeler le développement en série entière de $t\mapsto\ln(1+t)$ et son rayon de convergence.
2. Justifier l'existence de $I=\displaystyle\int_0^1\frac{\ln(1+t)}t\,\mathrm dt$ et la calculer.
""",
r"$\ln(1+t)=\sum_{n\ge1}\dfrac{(-1)^{n+1}t^n}n$ pour $|t|<1$, rayon 1.",
r"Pour $t\in]0,1]$, $\dfrac{\ln(1+t)}t=\sum_{n\ge1}\dfrac{(-1)^{n+1}t^{n-1}}n$ : série alternée dont tu peux majorer le reste uniformément.",
r"Après intégration terme à terme : $I=\sum\dfrac{(-1)^{n+1}}{n^2}$, puis sépare termes pairs et impairs.",
r"""
**1.** $\ln(1+t)=\displaystyle\sum_{n=1}^{+\infty}\frac{(-1)^{n+1}}nt^n$, rayon de convergence 1 (l'égalité vaut aussi en $t=1$).

**2.** $\dfrac{\ln(1+t)}t\to1$ en $0$ : la fonction se prolonge par continuité sur $[0,1]$, l'intégrale existe. Pour $t\in[0,1]$, $f_n(t)=\dfrac{(-1)^{n+1}t^{n-1}}n$ définit une série alternée ($|f_n(t)|$ décroît vers 0) : le reste vérifie $|R_N(t)|\le\dfrac{t^N}{N+1}\le\dfrac1{N+1}$. La convergence est uniforme sur $[0,1]$ (segment) : on peut intégrer terme à terme.
$$I=\sum_{n=1}^{+\infty}\frac{(-1)^{n+1}}{n^2}=\sum_{n\ge1}\frac1{n^2}-2\sum_{n\ge1}\frac1{(2n)^2}=\frac{\pi^2}6-\frac12\cdot\frac{\pi^2}6=\frac{\pi^2}{12}.$$
""", r"$I=\sum_{n\ge1}\frac{(-1)^{n+1}}{n^2}=\frac{\pi^2}{12}$.")

ex('n-m-wallis', M, 'Séries', 1, 'Série alternée et produit de Wallis', 15, r"""
On admet la formule de Wallis : $\displaystyle\prod_{k=1}^{N}\frac{4k^2}{4k^2-1}\xrightarrow[N\to+\infty]{}\frac\pi2$.

1. Étudier la convergence de la série $\displaystyle\sum_{n\ge1}(-1)^n\ln\left(1+\frac1n\right)$.
2. Calculer sa somme.
""",
r"Critère spécial des séries alternées : $\ln(1+1/n)$ décroît vers 0.",
r"Calcule la somme partielle $S_{2N}$ en regroupant les termes d'indices $2k-1$ et $2k$.",
r"$-\ln\dfrac{2k}{2k-1}+\ln\dfrac{2k+1}{2k}=\ln\dfrac{(2k-1)(2k+1)}{4k^2}$.",
r"""
**1.** $u_n=\ln(1+1/n)$ est positive, décroissante et tend vers 0 : par le critère spécial des séries alternées, $\sum(-1)^nu_n$ converge. (Elle ne converge pas absolument : $u_n\sim1/n$.)

**2.** La série converge, donc sa somme est la limite de $S_{2N}$. En regroupant :
$$S_{2N}=\sum_{k=1}^N\left[-\ln\frac{2k}{2k-1}+\ln\frac{2k+1}{2k}\right]=\sum_{k=1}^N\ln\frac{(2k-1)(2k+1)}{4k^2}=-\ln\prod_{k=1}^N\frac{4k^2}{4k^2-1}.$$
Par la formule de Wallis, $S_{2N}\to-\ln\dfrac\pi2$ : la somme vaut $\ln\dfrac2\pi$.
""", r"Converge (série alternée) ; somme $=\ln(2/\pi)$.")

ex('n-m-arctanx2', M, 'Intégration', 1, 'Intégrale de Arctan(x)/x² sur [1,+∞[', 10, r"""
Justifier l'existence et calculer $\displaystyle I=\int_1^{+\infty}\frac{\mathrm{Arctan}\,x}{x^2}\,\mathrm dx$.
""",
r"$0\le\dfrac{\mathrm{Arctan}\,x}{x^2}\le\dfrac\pi{2x^2}$, intégrable en $+\infty$.",
r"Intégration par parties avec $u=\mathrm{Arctan}\,x$ et $v=-1/x$, sur $[1,A]$ puis $A\to+\infty$.",
r"$\dfrac1{x(1+x^2)}=\dfrac1x-\dfrac x{1+x^2}$.",
r"""
**Existence.** La fonction est continue et positive sur $[1,+\infty[$, majorée par $\dfrac\pi{2x^2}$, intégrable en $+\infty$ (Riemann) : $I$ converge.

**Calcul.** Sur $[1,A]$, par parties :
$$\int_1^A\frac{\mathrm{Arctan}\,x}{x^2}\mathrm dx=\left[-\frac{\mathrm{Arctan}\,x}x\right]_1^A+\int_1^A\frac{\mathrm dx}{x(1+x^2)}.$$
Avec $\dfrac1{x(1+x^2)}=\dfrac1x-\dfrac x{1+x^2}$ : $\displaystyle\int_1^A\frac{\mathrm dx}{x(1+x^2)}=\left[\ln x-\tfrac12\ln(1+x^2)\right]_1^A=\ln\frac A{\sqrt{1+A^2}}+\frac12\ln2$. Quand $A\to+\infty$ : $\ln\frac A{\sqrt{1+A^2}}\to0$ et $-\frac{\mathrm{Arctan}\,A}A\to0$. Donc
$$I=\frac\pi4+\frac{\ln2}2.$$
""", r"$I=\frac\pi4+\frac{\ln2}2$.")

ex('n-m-symk', M, 'Réduction', 1, 'Matrice symétrique dont une puissance vaut l’identité', 10, r"""
Soit $A\in\mathcal S_n(\mathbb R)$ telle qu'il existe $k\in\mathbb N^*$ avec $A^k=I_n$. Montrer que $A^2=I_n$. Le résultat subsiste-t-il pour une matrice réelle non symétrique ?
""",
r"Théorème spectral : $A=PDP^\top$ avec $P$ orthogonale et $D$ diagonale réelle.",
r"$A^k=I_n$ donne $D^k=I_n$ : chaque valeur propre réelle $\lambda$ vérifie $\lambda^k=1$.",
r"Pour le cas non symétrique, pense à une rotation d'angle $2\pi/3$ du plan.",
r"""
Par le théorème spectral, $A=PDP^\top$ avec $P\in O_n(\mathbb R)$ et $D=\mathrm{diag}(\lambda_1,\dots,\lambda_n)$ réelle. $A^k=PD^kP^\top=I_n$ donne $D^k=I_n$, soit $\lambda_i^k=1$ avec $\lambda_i\in\mathbb R$ : $\lambda_i=\pm1$. Donc $D^2=I_n$ et $A^2=PD^2P^\top=I_n$.

Sans symétrie, c'est faux : la rotation $R=\begin{pmatrix}\cos\frac{2\pi}3&-\sin\frac{2\pi}3\\\sin\frac{2\pi}3&\cos\frac{2\pi}3\end{pmatrix}$ vérifie $R^3=I_2$ mais $R^2\neq I_2$ (ses valeurs propres sont $j$ et $\bar j$, non réelles).
""", r"Valeurs propres réelles avec $\lambda^k=1$, donc $\pm1$ : $A^2=I_n$ ; faux sans symétrie (rotation d'angle $2\pi/3$).")

ex('n-m-chth', M, 'Séries', 1, 'Une suite définie par une puissance', 15, r"""
Pour $n\in\mathbb N^*$, on pose $u_n=\left(\mathrm{ch}\frac1n-1\right)^{\mathrm{th}(1/n)}$.

1. Montrer que $(u_n)$ converge et déterminer sa limite $\ell$.
2. Déterminer la nature de la série de terme général $u_n-\ell$.
""",
r"Écris $u_n=\exp\big(\mathrm{th}(1/n)\ln(\mathrm{ch}(1/n)-1)\big)$ et utilise $\mathrm{ch}\,x-1\sim x^2/2$, $\mathrm{th}\,x\sim x$.",
r"L'exposant est équivalent à $-\dfrac{2\ln n}n$, qui tend vers 0.",
r"$e^{v_n}-1\sim v_n$ quand $v_n\to0$ ; compare $\dfrac{\ln n}n$ à $\dfrac1n$.",
r"""
**1.** $u_n=e^{v_n}$ avec $v_n=\mathrm{th}\frac1n\cdot\ln\left(\mathrm{ch}\frac1n-1\right)$. Comme $\mathrm{ch}\frac1n-1=\frac1{2n^2}(1+o(1))$, $\ln\left(\mathrm{ch}\frac1n-1\right)=-2\ln n-\ln2+o(1)\sim-2\ln n$. Et $\mathrm{th}\frac1n\sim\frac1n$. Donc $v_n\sim-\dfrac{2\ln n}n\to0$ et $u_n\to\ell=1$.

**2.** $u_n-1=e^{v_n}-1\sim v_n\sim-\dfrac{2\ln n}n$. Les termes sont négatifs à partir d'un certain rang et $\dfrac{2\ln n}n\ge\dfrac1n$ pour $n\ge2$ : par comparaison de séries à termes de signe constant, $\sum(u_n-1)$ **diverge**.
""", r"$\ell=1$ ; $u_n-1\sim-\frac{2\ln n}n$ : la série diverge.")

ex('n-m-extrema', M, 'Calcul différentiel', 2, 'Extrema de x⁴ + y⁴ − 2(x − y)²', 20, r"""
Déterminer les extrema locaux et globaux de $f(x,y)=x^4+y^4-2(x-y)^2$ sur $\mathbb R^2$.
""",
r"Points critiques : $\partial_xf=4x^3-4(x-y)=0$ et $\partial_yf=4y^3+4(x-y)=0$ ; additionne les deux équations.",
r"On trouve $y=-x$ puis $x^3=2x$ : trois points critiques. $f$ tend vers $+\infty$ à l'infini, elle atteint donc un minimum global.",
r"En $(0,0)$, compare $f(x,x)$ et $f(x,0)$ pour $x$ petit.",
r"""
**Points critiques.** En additionnant $4x^3-4(x-y)=0$ et $4y^3+4(x-y)=0$ : $x^3+y^3=0$, donc $y=-x$. Alors $4x^3-8x=0$ : $x\in\{0,\sqrt2,-\sqrt2\}$. Points critiques : $(0,0)$, $(\sqrt2,-\sqrt2)$, $(-\sqrt2,\sqrt2)$.

**Minimum global.** $(x-y)^2\le2(x^2+y^2)$, donc $f(x,y)\ge x^4+y^4-4(x^2+y^2)\xrightarrow[\|(x,y)\|\to\infty]{}+\infty$. $f$ est continue et coercive : elle atteint un minimum global, en un point critique (ouvert $\mathbb R^2$). $f(\pm\sqrt2,\mp\sqrt2)=4+4-2\times8=-8$ et $f(0,0)=0$ : le minimum global vaut $-8$, atteint en $(\sqrt2,-\sqrt2)$ et $(-\sqrt2,\sqrt2)$.

**En $(0,0)$.** $f(x,x)=2x^4>0$ et $f(x,0)=x^4-2x^2<0$ pour $0<|x|<\sqrt2$ : $f$ prend des valeurs des deux signes près de $(0,0)$, qui est un **point col**, pas un extremum. Pas de maximum (local ou global).
""", r"Minimum global $-8$ en $(\sqrt2,-\sqrt2)$ et $(-\sqrt2,\sqrt2)$ ; $(0,0)$ est un point col ; pas de maximum.")

ex('n-m-In', M, 'Séries entières', 2, 'Intégrales de (eᵗ − 1)ⁿ et série entière', 25, r"""
Pour $n\in\mathbb N$, on pose $I_n=\displaystyle\int_0^{\ln2}(e^t-1)^n\,\mathrm dt$.

1. Montrer que $I_n=\displaystyle\int_0^1\frac{u^n}{1+u}\,\mathrm du$ et en déduire une relation entre $I_n$ et $I_{n-1}$.
2. Trouver un équivalent de $I_n$.
3. Déterminer le rayon de convergence $R$ de $\sum I_nx^n$.
4. Calculer $\displaystyle\sum_{n=0}^{+\infty}I_nx^n$ pour $x\in]-R,R[$.
""",
r"Changement de variable $u=e^t-1$, $\mathrm du=(1+u)\mathrm dt$. Puis $I_n+I_{n-1}=\int_0^1u^{n-1}\mathrm du$.",
r"$(I_n)$ est décroissante : encadre $2I_n$ entre $I_n+I_{n+1}$ et $I_n+I_{n-1}$.",
r"Pour la somme, intervertis série et intégrale : $\sum(xu)^n=\dfrac1{1-xu}$, puis décompose $\dfrac1{(1+u)(1-xu)}$ en éléments simples.",
r"""
**1.** Avec $u=e^t-1$ ($C^1$, croissant de $[0,\ln2]$ sur $[0,1]$), $\mathrm dt=\frac{\mathrm du}{1+u}$ : $I_n=\int_0^1\frac{u^n}{1+u}\mathrm du$. Alors $I_n+I_{n-1}=\int_0^1u^{n-1}\mathrm du=\dfrac1n$ pour $n\ge1$.

**2.** Pour $u\in[0,1]$, $u^{n+1}\le u^n$ : $(I_n)$ décroît. Donc $\dfrac1{n+1}=I_{n+1}+I_n\le2I_n\le I_n+I_{n-1}=\dfrac1n$, d'où $I_n\sim\dfrac1{2n}$.

**3.** $I_nx^n\sim\frac{x^n}{2n}$ : même rayon que $\sum x^n/n$, soit $R=1$.

**4.** Pour $|x|<1$ et $u\in[0,1]$ : $\sum|xu|^n/(1+u)\le\sum|x|^n$, convergence normale sur $[0,1]$, on intègre terme à terme :
$$\sum_{n\ge0}I_nx^n=\int_0^1\frac{\mathrm du}{(1+u)(1-xu)}=\frac1{1+x}\int_0^1\left(\frac1{1+u}+\frac x{1-xu}\right)\mathrm du=\frac{\ln2-\ln(1-x)}{1+x}.$$
(Vérification en $x=0$ : $I_0=\ln2$.)
""", r"$I_n+I_{n-1}=\frac1n$ ; $I_n\sim\frac1{2n}$ ; $R=1$ ; $\sum I_nx^n=\frac{\ln2-\ln(1-x)}{1+x}$.")

ex('n-m-double', M, 'Séries', 2, 'Une somme double rationnelle', 25, r"""
Montrer que la somme double $\displaystyle S=\sum_{n=1}^{+\infty}\sum_{m=1}^{+\infty}\frac1{m^2n+mn^2+2mn}$ est finie et la calculer.

*Indication possible :* écrire $\dfrac1{m+n+2}$ comme une intégrale.
""",
r"$m^2n+mn^2+2mn=mn(m+n+2)$ et $\dfrac1{m+n+2}=\displaystyle\int_0^1x^{m+n+1}\mathrm dx$.",
r"Tout est positif : on peut intervertir sommes et intégrale (théorème de Fubini-Tonelli). $\sum_{m\ge1}\frac{x^m}m=-\ln(1-x)$.",
r"$S=\int_0^1x\ln^2(1-x)\,\mathrm dx$ ; pose $y=1-x$ et utilise $\int_0^1y^a\ln^2y\,\mathrm dy=\dfrac2{(a+1)^3}$.",
r"""
**Réécriture.** $m^2n+mn^2+2mn=mn(m+n+2)$ et $\dfrac1{m+n+2}=\int_0^1x^{m+n+1}\mathrm dx$. Tous les termes sont positifs : on peut intervertir les sommes et l'intégrale (Fubini-Tonelli), la valeur commune étant finie ou $+\infty$.
$$S=\int_0^1x\left(\sum_{m\ge1}\frac{x^m}m\right)\left(\sum_{n\ge1}\frac{x^n}n\right)\mathrm dx=\int_0^1x\ln^2(1-x)\,\mathrm dx.$$

**Calcul.** Avec $y=1-x$ : $S=\int_0^1(1-y)\ln^2y\,\mathrm dy$. Par deux intégrations par parties, $\int_0^1y^a\ln^2y\,\mathrm dy=\dfrac2{(a+1)^3}$ (convergentes car $y^a\ln^2y$ est intégrable en 0). Donc
$$S=2-\frac28=\frac74.$$
""", r"$S=\int_0^1x\ln^2(1-x)\,\mathrm dx=\frac74$.")

ex('n-m-blocs', M, 'Réduction', 2, 'Diagonalisabilité d’une matrice par blocs', 25, r"""
Soient $A,B\in\mathcal M_n(\mathbb C)$ telles que $AB=BA$, et $M=\begin{pmatrix}A&B\\0&A\end{pmatrix}\in\mathcal M_{2n}(\mathbb C)$.

1. Montrer que pour tout polynôme $P\in\mathbb C[X]$, $P(M)=\begin{pmatrix}P(A)&P'(A)B\\0&P(A)\end{pmatrix}$.
2. Trouver une condition nécessaire et suffisante sur $A$ et $B$ pour que $M$ soit diagonalisable.
""",
r"Vérifie la formule pour $P=X^k$ par récurrence (c'est là que $AB=BA$ sert), puis par linéarité.",
r"$M$ est diagonalisable ssi elle annule un polynôme scindé à racines simples. Si $P(M)=0$, alors $P(A)=0$ et $P'(A)B=0$.",
r"Si $A$ est diagonalisable de polynôme minimal $\pi$ à racines simples, $\pi'(A)$ est inversible : ses valeurs propres sont les $\pi'(\lambda)\neq0$.",
r"""
**1.** Pour $P=X^k$, récurrence : $M^{k+1}=\begin{pmatrix}A^k&kA^{k-1}B\\0&A^k\end{pmatrix}\begin{pmatrix}A&B\\0&A\end{pmatrix}=\begin{pmatrix}A^{k+1}&A^kB+kA^{k-1}BA\\0&A^{k+1}\end{pmatrix}$ et $kA^{k-1}BA=kA^kB$ car $AB=BA$. On conclut par linéarité.

**2.** Montrons que $M$ est diagonalisable ssi **$A$ est diagonalisable et $B=0$**.

Si $A$ est diagonalisable et $B=0$, $M=\mathrm{diag}(A,A)$ est diagonalisable.

Réciproquement, si $M$ est diagonalisable, soit $P$ scindé à racines simples tel que $P(M)=0$. Alors $P(A)=0$ (donc $A$ est diagonalisable) et $P'(A)B=0$. Le polynôme minimal $\pi$ de $A$ divise $P$ ; toute valeur propre $\lambda$ de $A$ est racine simple de $P$, donc $P'(\lambda)\neq0$. Comme $A$ est diagonalisable, $P'(A)$ l'est aussi (même base), de valeurs propres $P'(\lambda)\neq0$ : $P'(A)$ est inversible. Donc $B=0$.
""", r"$P(M)=\begin{pmatrix}P(A)&P'(A)B\\0&P(A)\end{pmatrix}$ ; $M$ diagonalisable ssi $A$ diagonalisable et $B=0$.")

ex('n-m-pieces', M, 'Probabilités', 2, 'L’intrus à pile ou face', 15, r"""
Soit $n\ge3$. $n$ personnes lancent chacune une pièce équilibrée, indépendamment.

1. Quelle est la probabilité $p_n$ qu'une personne exactement obtienne un résultat différent de toutes les autres ?
2. On répète l'expérience jusqu'à ce que cela se produise pour la première fois, et on note $X$ le nombre d'expériences effectuées. Donner la loi, l'espérance et la variance de $X$.
3. Pourquoi a-t-on supposé $n\ge3$ ?
""",
r"Il y a $2^n$ issues équiprobables. Une issue favorable est déterminée par la personne isolée et par son résultat.",
r"$p_n=\dfrac{2n}{2^n}$ ; $X$ est le temps d'attente du premier succès d'épreuves de Bernoulli indépendantes.",
r"Pour $n=2$, que signifie « différent de toutes les autres » ?",
r"""
**1.** $2^n$ issues équiprobables. Une issue favorable : une personne (n choix) obtient un résultat (2 choix) et toutes les autres le résultat opposé. Pour $n\ge3$, ces $2n$ issues sont distinctes (la personne isolée est l'unique minoritaire). Donc $p_n=\dfrac{2n}{2^n}=\dfrac n{2^{n-1}}$.

**2.** Les expériences sont indépendantes, de même probabilité de succès $p_n$ : $X$ suit la loi géométrique $\mathcal G(p_n)$, $P(X=k)=(1-p_n)^{k-1}p_n$. Donc $E(X)=\dfrac1{p_n}=\dfrac{2^{n-1}}n$ et $V(X)=\dfrac{1-p_n}{p_n^2}$.

**3.** Pour $n=2$, dès que les deux résultats diffèrent, chaque personne est « différente de l'autre » : l'issue (pile, face) serait comptée deux fois, et la formule donnerait $p_2=1$, ce qui est faux ($p_2=1/2$).
""", r"$p_n=\frac n{2^{n-1}}$ ; $X\sim\mathcal G(p_n)$, $E(X)=\frac{2^{n-1}}n$, $V(X)=\frac{1-p_n}{p_n^2}$.")

ex('n-m-Jn', M, 'Intégration', 2, 'Intégrales de 1/(1+x³)ⁿ⁺¹', 25, r"""
Pour $n\in\mathbb N$, on pose $J_n=\displaystyle\int_0^{+\infty}\frac{\mathrm dx}{(1+x^3)^{n+1}}$.

1. Justifier l'existence de $J_n$.
2. Calculer $J_0$.
3. Établir une relation entre $J_{n+1}$ et $J_n$.
4. Montrer qu'il existe $A>0$ tel que $J_n\sim\dfrac A{\sqrt[3]n}$.
""",
r"$\dfrac1{(1+x^3)^{n+1}}\le\dfrac1{1+x^3}\sim\dfrac1{x^3}$ en $+\infty$.",
r"$\dfrac1{1+x^3}=\dfrac{1/3}{1+x}-\dfrac16\cdot\dfrac{2x-1}{x^2-x+1}+\dfrac12\cdot\dfrac1{x^2-x+1}$. Pour la relation, intègre $J_n$ par parties avec $u=(1+x^3)^{-(n+1)}$, $v=x$.",
r"$J_{n+1}=\dfrac{3n+2}{3n+3}J_n$ ; étudie $\ln J_n=\ln J_0+\sum_{k<n}\ln\left(1-\frac1{3k+3}\right)$ et compare à $-\frac13\ln n$.",
r"""
**1.** Continue et positive sur $[0,+\infty[$, majorée par $\frac1{1+x^3}\sim\frac1{x^3}$ intégrable en $+\infty$ : $J_n$ existe.

**2.** Avec la décomposition de l'indice, une primitive est $\dfrac16\ln\dfrac{(1+x)^2}{x^2-x+1}+\dfrac1{\sqrt3}\mathrm{Arctan}\dfrac{2x-1}{\sqrt3}$. Le logarithme tend vers 0 en $+\infty$ et vaut 0 en 0, donc $J_0=\dfrac1{\sqrt3}\left(\dfrac\pi2+\dfrac\pi6\right)=\dfrac{2\pi}{3\sqrt3}$.

**3.** Par parties (le crochet $\frac x{(1+x^3)^{n+1}}$ est nul en 0 et tend vers 0 en $+\infty$) :
$$J_n=3(n+1)\int_0^{+\infty}\frac{x^3}{(1+x^3)^{n+2}}\mathrm dx=3(n+1)(J_n-J_{n+1}),$$
d'où $J_{n+1}=\dfrac{3n+2}{3n+3}J_n$.

**4.** $\ln J_n=\ln J_0+\sum_{k=0}^{n-1}\ln\left(1-\dfrac1{3(k+1)}\right)$, et $\ln\left(1-\frac1{3(k+1)}\right)=-\frac1{3(k+1)}+O\left(\frac1{k^2}\right)$. Comme $\sum_{k=1}^n\frac1k=\ln n+\gamma+o(1)$ et que la série des $O(1/k^2)$ converge, $\ln J_n=-\frac13\ln n+C+o(1)$. Donc $J_n\sim\dfrac{e^C}{\sqrt[3]n}$ : $A=e^C>0$.
""", r"$J_0=\frac{2\pi}{3\sqrt3}$ ; $J_{n+1}=\frac{3n+2}{3n+3}J_n$ ; $J_n\sim A/\sqrt[3]n$.")

ex('n-m-sintx', M, 'Intégrales à paramètre', 2, 'Intégrale de sin(tx)/(t(1+t²))', 20, r"""
Soit $F(x)=\displaystyle\int_0^{+\infty}\frac{\sin(tx)}{t(1+t^2)}\,\mathrm dt$. On admet que $\displaystyle\int_0^{+\infty}\frac{\cos(tx)}{1+t^2}\,\mathrm dt=\frac\pi2e^{-|x|}$ pour tout réel $x$.

1. Montrer que $F$ est définie et de classe $C^1$ sur $\mathbb R$, et calculer $F'$.
2. En déduire une expression de $F$ à l'aide des fonctions usuelles.
3. $F$ est-elle de classe $C^2$ sur $\mathbb R$ ?
""",
r"$|\sin(tx)|\le|tx|$ et $|\sin(tx)|\le1$ : l'intégrande est intégrable en 0 et en $+\infty$.",
r"Dérivée de l'intégrande par rapport à $x$ : $\dfrac{\cos(tx)}{1+t^2}$, dominée par $\dfrac1{1+t^2}$ indépendamment de $x$.",
r"$F(0)=0$, donc $F(x)=\int_0^xF'$ ; regarde les dérivées à droite et à gauche de $F'$ en 0.",
r"""
**1.** Pour $t>0$ : $\left|\frac{\sin(tx)}{t(1+t^2)}\right|\le\min\left(\frac{|x|}{1+t^2},\frac1{t(1+t^2)}\right)$ : intégrable, $F$ est définie. La dérivée partielle $\frac{\cos(tx)}{1+t^2}$ est continue et dominée par $\frac1{1+t^2}$, intégrable sur $]0,+\infty[$ indépendamment de $x$ : par le théorème de dérivation sous l'intégrale, $F$ est $C^1$ et $F'(x)=\displaystyle\int_0^{+\infty}\frac{\cos(tx)}{1+t^2}\mathrm dt=\frac\pi2e^{-|x|}$.

**2.** $F(0)=0$, donc pour $x\ge0$ : $F(x)=\dfrac\pi2\left(1-e^{-x}\right)$. $F$ est impaire : $F(x)=\dfrac\pi2\,\mathrm{sgn}(x)\left(1-e^{-|x|}\right)$.

**3.** $F'(x)=\frac\pi2e^{-|x|}$ a pour dérivée à droite $-\frac\pi2$ et à gauche $+\frac\pi2$ en 0 : $F'$ n'est pas dérivable en 0, et $F$ n'est pas $C^2$ sur $\mathbb R$ (elle l'est sur $\mathbb R^*$). On ne peut d'ailleurs pas dériver deux fois sous l'intégrale : $\frac{t\sin(tx)}{1+t^2}$ n'est pas intégrable sur $]0,+\infty[$.
""", r"$F'(x)=\frac\pi2e^{-|x|}$ ; $F(x)=\frac\pi2\,\mathrm{sgn}(x)(1-e^{-|x|})$ ; $C^1$ mais pas $C^2$ en 0.")

ex('n-m-arctantx', M, 'Intégrales à paramètre', 2, 'Intégrale de Arctan(tx)/(t(1+t²))', 25, r"""
Soit $F(x)=\displaystyle\int_0^{+\infty}\frac{\mathrm{Arctan}(tx)}{t(1+t^2)}\,\mathrm dt$.

1. Déterminer le domaine de définition de $F$.
2. Montrer que $F$ est de classe $C^1$ sur $\mathbb R$ et calculer $F'(x)$.
3. En déduire $F(x)$.
4. En déduire la valeur de $\displaystyle\int_0^{+\infty}\left(\frac{\mathrm{Arctan}\,t}t\right)^2\mathrm dt$.
""",
r"$|\mathrm{Arctan}(tx)|\le\min(|tx|,\pi/2)$ : intégrable en 0 et en $+\infty$ pour tout $x$.",
r"$\partial_x$ de l'intégrande : $\dfrac1{(1+t^2x^2)(1+t^2)}\le\dfrac1{1+t^2}$. Pour $x^2\neq1$, décompose en éléments simples en $t^2$.",
r"Pour la dernière intégrale, intègre par parties $\dfrac{\mathrm{Arctan}^2t}{t^2}$ avec $v=-1/t$ : elle vaut $2F(1)$.",
r"""
**1.** $\left|\frac{\mathrm{Arctan}(tx)}{t(1+t^2)}\right|\le\min\left(\frac{|x|}{1+t^2},\frac\pi{2t^3}\right)$ : intégrable sur $]0,+\infty[$ pour tout $x$. $D=\mathbb R$.

**2.** $\partial_x\frac{\mathrm{Arctan}(tx)}{t(1+t^2)}=\frac1{(1+t^2x^2)(1+t^2)}$, continue et dominée par $\frac1{1+t^2}$ : $F$ est $C^1$ et $F'(x)=\int_0^{+\infty}\frac{\mathrm dt}{(1+t^2x^2)(1+t^2)}$. Pour $x^2\neq1$ : $\frac1{(1+x^2t^2)(1+t^2)}=\frac1{1-x^2}\left(\frac1{1+t^2}-\frac{x^2}{1+x^2t^2}\right)$, d'où $F'(x)=\frac1{1-x^2}\left(\frac\pi2-|x|\frac\pi2\right)=\dfrac\pi{2(1+|x|)}$, formule prolongée en $x=\pm1$ par continuité de $F'$.

**3.** $F(0)=0$ et $F$ est impaire : $F(x)=\dfrac\pi2\,\mathrm{sgn}(x)\ln(1+|x|)$.

**4.** Par parties sur $[\varepsilon,A]$ : $\int\frac{\mathrm{Arctan}^2t}{t^2}\mathrm dt=\left[-\frac{\mathrm{Arctan}^2t}t\right]+\int\frac{2\,\mathrm{Arctan}\,t}{t(1+t^2)}\mathrm dt$. Le crochet tend vers 0 aux deux bornes ($\mathrm{Arctan}^2t/t\sim t$ en 0). Donc l'intégrale vaut $2F(1)=\pi\ln2$.
""", r"$D=\mathbb R$ ; $F'(x)=\frac\pi{2(1+|x|)}$ ; $F(x)=\frac\pi2\,\mathrm{sgn}(x)\ln(1+|x|)$ ; $\int_0^\infty(\mathrm{Arctan}\,t/t)^2=\pi\ln2$.")

ex('n-m-geodiff', M, 'Probabilités', 2, 'Écart entre deux lois géométriques', 25, r"""
Soient $X_1$ et $X_2$ indépendantes, de loi géométrique $\mathcal G(p)$ sur $\mathbb N^*$, $p\in]0,1[$, $q=1-p$. On pose $Y=|X_1-X_2|$.

1. Calculer $P(Y=0)$. Montrer que $P(X_1-X_2=n)=\dfrac{pq^n}{1+q}$ pour tout $n\in\mathbb N$. En déduire la loi de $Y$.
2. Montrer que $Y$ admet une espérance et la calculer.
3. Montrer que $E\big((X_1-X_2)^2\big)=2V(X_1)$. En déduire que $Y$ admet une variance et la calculer.
""",
r"$P(X_1-X_2=n)=\sum_{k\ge1}P(X_2=k)P(X_1=k+n)$ : série géométrique de raison $q^2$.",
r"Par symétrie, $P(X_1-X_2=-n)=P(X_1-X_2=n)$ : $P(Y=n)=\dfrac{2pq^n}{1+q}$ pour $n\ge1$. Utilise $\sum nq^n=\dfrac q{(1-q)^2}$.",
r"$E((X_1-X_2)^2)=E(X_1^2)+E(X_2^2)-2E(X_1)E(X_2)$ ; et $Y^2=(X_1-X_2)^2$.",
r"""
**1.** Par indépendance, pour $n\ge0$ : $P(X_1-X_2=n)=\sum_{k\ge1}pq^{k-1}\,pq^{k+n-1}=p^2q^n\sum_{k\ge1}q^{2(k-1)}=\dfrac{p^2q^n}{1-q^2}=\dfrac{pq^n}{1+q}$. En particulier $P(Y=0)=\dfrac p{1+q}$. Par symétrie des rôles, $P(X_1-X_2=-n)=P(X_1-X_2=n)$, donc $P(Y=n)=\dfrac{2pq^n}{1+q}$ pour $n\ge1$.

**2.** $\sum nP(Y=n)=\dfrac{2p}{1+q}\sum_{n\ge1}nq^n=\dfrac{2p}{1+q}\cdot\dfrac q{p^2}$ converge : $E(Y)=\dfrac{2q}{p(1+q)}$.

**3.** $X_1,X_2$ ont un moment d'ordre 2 et sont indépendantes : $E((X_1-X_2)^2)=2E(X_1^2)-2E(X_1)^2=2V(X_1)=\dfrac{2q}{p^2}$. Or $Y^2=(X_1-X_2)^2$, donc $Y$ admet un moment d'ordre 2 et
$$V(Y)=\frac{2q}{p^2}-\frac{4q^2}{p^2(1+q)^2}=\frac{2q(1+q^2)}{p^2(1+q)^2}.$$
""", r"$P(Y=0)=\frac p{1+q}$, $P(Y=n)=\frac{2pq^n}{1+q}$ ; $E(Y)=\frac{2q}{p(1+q)}$ ; $V(Y)=\frac{2q(1+q^2)}{p^2(1+q)^2}$.")

ex('n-m-kerf2', M, 'Algèbre linéaire', 2, 'Noyau de f² et noyau de f', 20, r"""
Soit $E\neq\{0\}$ un espace vectoriel de dimension finie et $f\in\mathcal L(E)$.

1. Montrer que $\dim\mathrm{Ker}\,f^2\le2\dim\mathrm{Ker}\,f$.
2. Montrer l'équivalence des propriétés :
(i) $\dim\mathrm{Ker}\,f^2=2\dim\mathrm{Ker}\,f$ ;
(ii) $\mathrm{Ker}\,f\subset\mathrm{Im}\,f$ ;
(iii) $f(\mathrm{Ker}\,f^2)=\mathrm{Ker}\,f$.
""",
r"Applique le théorème du rang à la restriction $g$ de $f$ à $\mathrm{Ker}\,f^2$.",
r"$\mathrm{Ker}\,g=\mathrm{Ker}\,f$ et $\mathrm{Im}\,g=f(\mathrm{Ker}\,f^2)\subset\mathrm{Ker}\,f$.",
r"(i)⇔(iii) par les dimensions ; (iii)⇒(ii) est immédiat ; pour (ii)⇒(iii), écris $y\in\mathrm{Ker}\,f$ sous la forme $y=f(x)$.",
r"""
**1.** Soit $g:\mathrm{Ker}\,f^2\to E$, $x\mapsto f(x)$. $\mathrm{Ker}\,g=\mathrm{Ker}\,f\cap\mathrm{Ker}\,f^2=\mathrm{Ker}\,f$ et $\mathrm{Im}\,g=f(\mathrm{Ker}\,f^2)\subset\mathrm{Ker}\,f$ (si $f^2(x)=0$, $f(f(x))=0$). Théorème du rang : $\dim\mathrm{Ker}\,f^2=\dim\mathrm{Ker}\,f+\dim f(\mathrm{Ker}\,f^2)\le2\dim\mathrm{Ker}\,f$.

**2.** (i)⇔(iii) : par la formule précédente, (i) équivaut à $\dim f(\mathrm{Ker}\,f^2)=\dim\mathrm{Ker}\,f$, donc (inclusion et égalité des dimensions) à $f(\mathrm{Ker}\,f^2)=\mathrm{Ker}\,f$.

(iii)⇒(ii) : $\mathrm{Ker}\,f=f(\mathrm{Ker}\,f^2)\subset\mathrm{Im}\,f$.

(ii)⇒(iii) : soit $y\in\mathrm{Ker}\,f$. Par (ii), $y=f(x)$ ; alors $f^2(x)=f(y)=0$, donc $x\in\mathrm{Ker}\,f^2$ et $y\in f(\mathrm{Ker}\,f^2)$. L'autre inclusion a été vue en 1.
""", r"Théorème du rang sur $f_{|\mathrm{Ker}f^2}$ : $\dim\mathrm{Ker}f^2=\dim\mathrm{Ker}f+\dim f(\mathrm{Ker}f^2)$ ; (i)⇔(iii)⇔(ii).")
