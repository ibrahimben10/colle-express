D = {}

D['m-ccmp-17c'] = r"""
**Attention.** L'énoncé est faux pour $A\in\mathcal S_n^+$ non inversible (contre-exemple à la fin). On démontre le résultat pour $A\in\mathcal S_n^{++}(\mathbb R)$.

**Étape 1 : racine carrée de $A$.** Par le théorème spectral, $A=PDP^{\top}$ avec $P\in O_n(\mathbb R)$, $D=\mathrm{diag}(d_1,\dots,d_n)$ et $d_i>0$. Posons $S=P\,\mathrm{diag}(\sqrt{d_1},\dots,\sqrt{d_n})\,P^{\top}$. Alors $S^{\top}=S$, $S^2=P\,\mathrm{diag}(d_i)\,P^{\top}=A$ (car $P^{\top}P=I_n$), et $S$ est inversible (valeurs propres $\sqrt{d_i}>0$).

**Étape 2 : $AB$ est semblable à une matrice antisymétrique.**
$$S^{-1}(AB)S=S^{-1}S^2BS=SBS,\qquad(SBS)^{\top}=S^{\top}B^{\top}S^{\top}=S(-B)S=-SBS.$$
Il suffit donc de montrer qu'une matrice $K$ réelle antisymétrique est diagonalisable sur $\mathbb C$.

**Étape 3 : valeurs propres de $K$.** Pour $u,v\in\mathbb C^n$, notons $\langle u,v\rangle=\overline u^{\top}v$ (produit scalaire hermitien, avec $\langle u,u\rangle=\|u\|^2>0$ si $u\neq0$). Comme $K$ est réelle et $K^{\top}=-K$ :
$$\langle Ku,v\rangle=\overline u^{\top}K^{\top}v=-\langle u,Kv\rangle.$$
Si $Ku=\lambda u$ avec $u\neq0$ : $\overline\lambda\|u\|^2=\langle Ku,u\rangle=-\langle u,Ku\rangle=-\lambda\|u\|^2$, donc $\overline\lambda=-\lambda$ : $\lambda$ est imaginaire pur.

**Étape 4 : les noyaux itérés sont égaux aux sous-espaces propres.** Soit $\lambda$ valeur propre et $x$ tel que $(K-\lambda I)^2x=0$. Posons $y=(K-\lambda I)x$, de sorte que $Ky=\lambda y$. Alors
$$\|y\|^2=\langle(K-\lambda I)x,y\rangle=\langle Kx,y\rangle-\overline\lambda\langle x,y\rangle=-\langle x,Ky\rangle-\overline\lambda\langle x,y\rangle=-(\lambda+\overline\lambda)\langle x,y\rangle=0.$$
Donc $y=0$ : $\ker(K-\lambda I)^2=\ker(K-\lambda I)$, et par récurrence $\ker(K-\lambda I)^m=\ker(K-\lambda I)$ pour tout $m\ge1$.

**Étape 5 : conclusion.** Sur $\mathbb C$, $\chi_K=\prod(X-\lambda_i)^{m_i}$ et, par Cayley-Hamilton et le lemme des noyaux, $\mathbb C^n=\bigoplus\ker(K-\lambda_iI)^{m_i}=\bigoplus\ker(K-\lambda_iI)$ : $K$ est diagonalisable sur $\mathbb C$. Ainsi $AB$, semblable à $K=SBS$, est diagonalisable dans $\mathcal M_n(\mathbb C)$, à valeurs propres imaginaires pures.

**Contre-exemple pour $A$ seulement positive.** $A=\begin{pmatrix}1&0\\0&0\end{pmatrix}\in\mathcal S_2^+$, $B=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\in\mathcal A_2$ :
$$AB=\begin{pmatrix}1&0\\0&0\end{pmatrix}\begin{pmatrix}0&1\\-1&0\end{pmatrix}=\begin{pmatrix}0&1\\0&0\end{pmatrix}.$$
Elle est nilpotente ($(AB)^2=0$) et non nulle : si elle était diagonalisable, sa seule valeur propre étant 0, elle serait nulle. Elle n'est donc pas diagonalisable.
===RÉPONSE===
Vrai pour $A\in\mathcal S_n^{++}$ : $AB\sim SBS$ antisymétrique réelle, diagonalisable sur $\mathbb C$. Faux pour $A\in\mathcal S_n^+$ (contre-exemple $2\times2$).
"""

D['m-ccmp-19a'] = r"""
On démontre d'abord le résultat de similitude (lemme), dont la décomposition en nilpotentes découle immédiatement.

**Lemme préliminaire : un endomorphisme non scalaire a un vecteur non propre.** Si tout vecteur non nul $x$ est propre ($Ax=a_xx$), alors $A$ est une homothétie : pour $x,y$ libres, $A(x+y)=a_{x+y}(x+y)$ et $A(x+y)=a_xx+a_yy$ donnent, par liberté, $a_x=a_{x+y}=a_y$ ; et si $y=\mu x$, $a_y=a_x$ directement. Donc si $A$ n'est pas scalaire, il existe $x$ tel que $(x,Ax)$ soit libre.

**Lemme : si $\mathrm{Tr}\,A=0$, $A$ est semblable à une matrice à diagonale nulle.** Récurrence sur $n$.
- $n=1$ : $A=(\mathrm{Tr}\,A)=(0)$.
- Hérédité : soit $A$ de taille $n\ge2$ et de trace nulle. Si $A=\lambda I_n$, alors $n\lambda=0$, donc $A=0$, qui convient. Sinon, prenons $x$ avec $(x,Ax)$ libre et complétons en une base $\mathcal B=(x,Ax,e_3,\dots,e_n)$. La première colonne de la matrice de $A$ dans $\mathcal B$ est formée des coordonnées de $Ax$, soit $(0,1,0,\dots,0)^{\top}$ :
$$A\sim M=\begin{pmatrix}0&L\\C&A'\end{pmatrix},\qquad C=(1,0,\dots,0)^{\top},\quad A'\in\mathcal M_{n-1}(\mathbb R).$$
La trace est invariante par similitude : $\mathrm{Tr}\,A'=\mathrm{Tr}\,M-0=0$. Par hypothèse de récurrence, $A'=QD'Q^{-1}$ avec $D'$ à diagonale nulle. Avec $R=\begin{pmatrix}1&0\\0&Q\end{pmatrix}$ :
$$R^{-1}MR=\begin{pmatrix}0&LQ\\Q^{-1}C&Q^{-1}A'Q\end{pmatrix}=\begin{pmatrix}0&LQ\\Q^{-1}C&D'\end{pmatrix},$$
matrice à diagonale nulle, semblable à $A$.

**1. Somme de deux nilpotentes.** Écrivons $A=PNP^{-1}$ avec $N$ à diagonale nulle, et $N=N_++N_-$ où $N_+$ (resp. $N_-$) garde les coefficients strictement au-dessus (resp. au-dessous) de la diagonale. Une matrice triangulaire stricte est nilpotente (ses puissances successives « montent » d'une diagonale : $N_+^n=0$). Donc
$$A=PN_+P^{-1}+PN_-P^{-1}$$
est somme de deux matrices nilpotentes (une conjuguée de nilpotente est nilpotente : $(PN_+P^{-1})^n=PN_+^nP^{-1}=0$). Réciproquement, une somme de deux nilpotentes a une trace nulle (trace d'une nilpotente nulle, linéarité) : les trois propriétés sont équivalentes.

**2. $A\sim-A\Rightarrow\mathrm{Tr}\,A=0$.** Deux matrices semblables ont la même trace : $\mathrm{Tr}\,A=\mathrm{Tr}(-A)=-\mathrm{Tr}\,A$, d'où $\mathrm{Tr}\,A=0$.

**2. La réciproque est fausse.** $A=\mathrm{diag}(1,1,-2)$ a une trace nulle, mais $\mathrm{Sp}(A)=\{1,-2\}$ et $\mathrm{Sp}(-A)=\{-1,2\}$ : les spectres diffèrent, donc $A\not\sim-A$. (Pour $n=2$ en revanche, $\mathrm{Tr}\,A=0$ donne $\chi_A=X^2+\det A=\chi_{-A}$, et la réciproque est vraie pour les matrices diagonalisables ; pour $A$ nilpotente non nulle, $A\sim-A$ aussi.)
"""

D['m-ccmp-19b'] = r"""
**1. Le cas $x<0$.** Pour $t>-\frac1x$, $1+tx<0$ : la racine n'est pas définie sur tout $[1,+\infty[$. Ces $x$ sont exclus.

**1. Le cas $x=0$.** L'intégrale devient $\int_1^{+\infty}\frac{\mathrm dt}t=\lim_{X\to\infty}\ln X=+\infty$ : divergente.

**1. Le cas $x>0$.** L'intégrande $h(t)=\frac1{t\sqrt{1+tx}}$ est continu et positif sur $[1,+\infty[$. En $+\infty$ : $\sqrt{1+tx}=\sqrt{tx}\sqrt{1+\frac1{tx}}\sim\sqrt x\,\sqrt t$, donc
$$h(t)\sim\frac1{\sqrt x\,t^{3/2}},$$
intégrable en $+\infty$ (Riemann, $\frac32>1$). Par comparaison de fonctions positives, $f(x)$ converge. Ainsi $\mathcal D_f=]0,+\infty[$.

**2. Changement de variable.** Fixons $x>0$ et posons $u=\sqrt{1+tx}$ : $t\mapsto u$ est $C^1$ et strictement croissante de $[1,+\infty[$ sur $[\sqrt{1+x},+\infty[$. On a $u^2=1+tx$, donc
$$t=\frac{u^2-1}x,\qquad\mathrm dt=\frac{2u}x\,\mathrm du,\qquad\frac{\mathrm dt}{t\sqrt{1+tx}}=\frac{\frac{2u}x\,\mathrm du}{\frac{u^2-1}x\cdot u}=\frac{2\,\mathrm du}{u^2-1}.$$

**2. Éléments simples.** $\frac2{u^2-1}=\frac2{(u-1)(u+1)}=\frac1{u-1}-\frac1{u+1}$ (vérification : $\frac{(u+1)-(u-1)}{(u-1)(u+1)}=\frac2{u^2-1}$). Une primitive est $\ln(u-1)-\ln(u+1)=\ln\frac{u-1}{u+1}$ pour $u>1$.

**2. Calcul.** $\frac{u-1}{u+1}\to1$ quand $u\to+\infty$, donc $\ln\frac{u-1}{u+1}\to0$, et
$$f(x)=\left[\ln\frac{u-1}{u+1}\right]_{\sqrt{1+x}}^{+\infty}=0-\ln\frac{\sqrt{1+x}-1}{\sqrt{1+x}+1}=\ln\frac{\sqrt{1+x}+1}{\sqrt{1+x}-1}.$$
En multipliant numérateur et dénominateur par $\sqrt{1+x}+1$, avec $(\sqrt{1+x}-1)(\sqrt{1+x}+1)=x$ :
$$\frac{\sqrt{1+x}+1}{\sqrt{1+x}-1}=\frac{(1+\sqrt{1+x})^2}x,\qquad\text{donc}\qquad f(x)=2\ln\frac{1+\sqrt{1+x}}{\sqrt x}.$$

**Contrôles.** Quand $x\to0^+$, $f(x)\sim2\ln\frac2{\sqrt x}\to+\infty$, cohérent avec la divergence en $x=0$. Quand $x\to+\infty$, $\frac{1+\sqrt{1+x}}{\sqrt x}=1+\frac1{\sqrt x}+O(\frac1x)$, donc $f(x)\sim\frac2{\sqrt x}$, cohérent avec $f(x)\le\int_1^\infty\frac{\mathrm dt}{t^{3/2}\sqrt x}=\frac2{\sqrt x}$.
"""

D['m-ccmp-20a'] = r"""
**1. Définition.** Soit $x>0$. La suite $a_n=n^{-x}$ est positive, décroissante et tend vers 0. Par le critère spécial des séries alternées, $\sum(-1)^{n-1}a_n$ converge : $g(x)$ est défini.

**1. Dérivées des termes.** $u_n(x)=(-1)^{n-1}n^{-x}=(-1)^{n-1}e^{-x\ln n}$ est $C^\infty$ et $u_n^{(k)}(x)=(-1)^{n-1}(-\ln n)^k\,n^{-x}=(-1)^{n-1+k}(\ln n)^kn^{-x}$. Chaque série dérivée est donc alternée, de terme en valeur absolue $b_n(x)=(\ln n)^kn^{-x}$.

**1. Décroissance à partir d'un rang uniforme.** Fixons $a>0$ et $k\ge0$. Étudions $\varphi(t)=(\ln t)^kt^{-x}$ pour $t\ge1$ :
$$\varphi'(t)=t^{-x-1}(\ln t)^{k-1}\big(k-x\ln t\big)\quad(k\ge1).$$
Pour $x\ge a$ et $\ln t\ge\frac ka$, on a $x\ln t\ge k$, donc $\varphi'(t)\le0$. Ainsi, pour $n\ge N_0=\lceil e^{k/a}\rceil$, la suite $(b_n(x))_{n\ge N_0}$ est décroissante pour **tout** $x\ge a$, et elle tend vers 0 (croissances comparées).

**1. Convergence uniforme.** Pour $N\ge N_0$ et $x\ge a$, le critère spécial majore le reste par le premier terme négligé :
$$\Big|\sum_{n>N}u_n^{(k)}(x)\Big|\le b_{N+1}(x)=\frac{(\ln(N+1))^k}{(N+1)^x}\le\frac{(\ln(N+1))^k}{(N+1)^a}\xrightarrow[N\to\infty]{}0.$$
Le majorant ne dépend pas de $x$ : chaque série dérivée converge uniformément sur $[a,+\infty[$. Par le théorème de dérivation terme à terme (appliqué à tous les ordres), $g$ est $C^\infty$ sur $[a,+\infty[$ ; comme $a>0$ est arbitraire, $g$ est $C^\infty$ sur $]0,+\infty[$.

**2. Transformation de la série.** On écrit, avec $a_n=n^{-x}$ :
$$\sum_{n\ge1}(-1)^{n-1}(a_n-a_{n+1})=\sum_{n\ge1}(-1)^{n-1}a_n-\sum_{n\ge1}(-1)^{n-1}a_{n+1}=g(x)+\sum_{m\ge2}(-1)^{m-1}a_m=g(x)+\big(g(x)-a_1\big),$$
où l'on a posé $m=n+1$ (et $(-1)^{n-1}=-(-1)^{m-1}$). Les deux séries convergent, la manipulation est licite. Avec $a_1=1$ :
$$2g(x)=1+h(x),\qquad h(x)=\sum_{n\ge1}(-1)^{n-1}d_n,\quad d_n=n^{-x}-(n+1)^{-x}.$$

**2. Majoration de $h$.** $d_n=\big[-t^{-x}\big]_n^{n+1}=x\int_n^{n+1}t^{-x-1}\,\mathrm dt\ge0$, et avec $t\mapsto t+1$ : $d_{n+1}=x\int_n^{n+1}(t+1)^{-x-1}\mathrm dt\le d_n$. La suite $(d_n)$ est positive, décroissante, de limite nulle : par le critère spécial, $h(x)$ est compris entre 0 et son premier terme :
$$0\le h(x)\le d_1=1-2^{-x}\xrightarrow[x\to0^+]{}0.$$

**Conclusion.** $h(x)\to0$, donc $g(x)=\frac{1+h(x)}2\to\dfrac12$ quand $x\to0^+$ (alors que la série $\sum(-1)^{n-1}$ diverge : c'est la « somme d'Abel » $\frac12$).
"""
