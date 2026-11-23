D = {}

D['m-ccmp-06a'] = r"""
**1. $\varphi$ est un endomorphisme.** Pour $M,N\in\mathcal M_n(\mathbb R)$ et $\lambda\in\mathbb R$, par distributivité du produit matriciel :
$$\varphi(\lambda M+N)=A(\lambda M+N)A=\lambda\,AMA+ANA=\lambda\varphi(M)+\varphi(N),$$
et $\varphi(M)\in\mathcal M_n(\mathbb R)$. C'est donc un endomorphisme de $\mathcal M_n(\mathbb R)$.

**1. Puissances de $\varphi$.** Montrons par récurrence que $\varphi^k(M)=A^kMA^k$ pour tout $k\ge0$ : c'est vrai pour $k=0$ ($\varphi^0=\mathrm{id}$, $A^0=I_n$) ; si c'est vrai au rang $k$, alors $\varphi^{k+1}(M)=\varphi(A^kMA^k)=A\,A^kMA^k\,A=A^{k+1}MA^{k+1}$.

**1. Équivalence des nilpotences.**
- Si $A$ est nilpotente, $A^k=0$ pour un $k\ge1$ ; alors $\varphi^k(M)=0\cdot M\cdot0=0$ pour tout $M$ : $\varphi^k=0$, $\varphi$ est nilpotent.
- Si $\varphi$ est nilpotent, $\varphi^k=0$ pour un $k$ ; en l'appliquant à $M=I_n$ : $0=\varphi^k(I_n)=A^kI_nA^k=A^{2k}$. Donc $A$ est nilpotente.

**2. Une base adaptée.** Supposons $A=PDP^{-1}$ avec $P\in GL_n(\mathbb R)$ et $D=\mathrm{diag}(d_1,\dots,d_n)$. L'application $\psi:M\mapsto PMP^{-1}$ est un automorphisme de $\mathcal M_n(\mathbb R)$ (linéaire, d'inverse $M\mapsto P^{-1}MP$). Elle envoie la base canonique $(E_{ij})$ sur une base : les $F_{ij}=PE_{ij}P^{-1}$, $1\le i,j\le n$, forment une base de $\mathcal M_n(\mathbb R)$.

**2. Les $F_{ij}$ sont propres.** On calcule, en simplifiant $P^{-1}P=I_n$ :
$$\varphi(F_{ij})=PDP^{-1}\cdot PE_{ij}P^{-1}\cdot PDP^{-1}=P\,(DE_{ij}D)\,P^{-1}.$$
Or $DE_{ij}$ multiplie la ligne $i$ de $E_{ij}$ par $d_i$ et $E_{ij}D$ multiplie sa colonne $j$ par $d_j$ ; comme $E_{ij}$ n'a qu'un coefficient non nul, en position $(i,j)$ : $DE_{ij}D=d_id_jE_{ij}$. Donc
$$\varphi(F_{ij})=d_id_j\,F_{ij}.$$

**Conclusion.** $(F_{ij})$ est une base de vecteurs propres de $\varphi$ : $\varphi$ est diagonalisable, ses valeurs propres sont les produits $d_id_j$ ($1\le i,j\le n$).
"""

D['m-ccmp-06b'] = r"""
**Notations.** $p_n=P(X=n)$, $g(t)=\sum_{n\ge0}p_nt^n$ pour $t\in[0,1]$ (la série converge en $t=1$ car $\sum p_n=1$, donc son rayon est $\ge1$), et $n^{\underline k}=n(n-1)\cdots(n-k+1)$ (nul si $n<k$). Sur $[0,1[$, intérieur du disque de convergence, $g$ est $C^\infty$ et
$$g^{(k)}(t)=\sum_{n\ge k}n^{\underline k}p_nt^{n-k}.$$

**Sens réciproque : $E(X^m)<\infty\Rightarrow g\in C^m([0,1])$.** Soit $k\in[\![0,m]\!]$. Pour $n\ge1$ et $t\in[0,1]$ : $0\le n^{\underline k}p_nt^{n-k}\le n^kp_n\le n^mp_n$ (car $n^{\underline k}\le n^k$ et $t^{n-k}\le1$). La série $\sum n^mp_n=E(X^m)$ converge, donc les séries $\sum_nn^{\underline k}p_nt^{n-k}$ convergent **normalement** sur $[0,1]$ pour $k=0,\dots,m$. Par le théorème de dérivation terme à terme (appliqué $m$ fois), $g$ est de classe $C^m$ sur $[0,1]$, et en particulier $g^{(m)}(1)=\sum n^{\underline m}p_n=E\big(X^{\underline m}\big)$.

**Sens direct : $g\in C^m([0,1])\Rightarrow E(X^m)<\infty$.** La fonction $g^{(m)}$ est continue sur le segment $[0,1]$, donc bornée : soit $K=\sup_{[0,1]}|g^{(m)}|$. Pour $N\ge m$ et $t\in[0,1[$, tous les termes de la série de $g^{(m)}(t)$ étant positifs,
$$\sum_{n=m}^Nn^{\underline m}p_nt^{n-m}\le g^{(m)}(t)\le K.$$
Le membre de gauche est un polynôme en $t$ : on fait $t\to1^-$ et on obtient $\sum_{n=m}^Nn^{\underline m}p_n\le K$. Ces sommes partielles de termes positifs sont majorées, donc $\sum_nn^{\underline m}p_n<\infty$.

**Passage de $n^{\underline m}$ à $n^m$.** Pour $n\ge2m$ et $0\le i\le m-1$ : $n-i\ge n-m\ge\frac n2$. Donc $n^{\underline m}\ge\left(\frac n2\right)^m$, soit $n^mp_n\le2^m\,n^{\underline m}p_n$. Par comparaison de séries à termes positifs, $\sum_{n\ge2m}n^mp_n$ converge, et donc $E(X^m)=\sum n^mp_n<\infty$ (les premiers termes sont en nombre fini).

**Conclusion.** $g\in C^m([0,1])\iff E(X^m)<+\infty$, et alors $g^{(m)}(1)=E\big(X(X-1)\cdots(X-m+1)\big)$ (moment factoriel d'ordre $m$).
"""

D['m-ccmp-07a'] = r"""
**1. Variations de $f$.** $f$ est dérivable sur $[e,+\infty[$ et
$$f'(x)=\frac{1\cdot\ln x-x\cdot\frac1x}{\ln^2x}=\frac{\ln x-1}{\ln^2x}.$$
Pour $x>e$, $\ln x>1$ donc $f'(x)>0$ ($f'(e)=0$ en un seul point) : $f$ est continue et strictement croissante sur $[e,+\infty[$. De plus $f(e)=\frac e1=e$ et $f(x)=\frac x{\ln x}\to+\infty$ (croissances comparées). Par le théorème de la bijection, $f$ réalise une bijection de $[e,+\infty[$ sur $J=[e,+\infty[$, de réciproque continue et strictement croissante, avec $f^{-1}(y)\to+\infty$ quand $y\to+\infty$.

**2. Équation vérifiée par $x_y=f^{-1}(y)$.** Pour $y\ge e$, $x_y$ est défini par $\frac{x_y}{\ln x_y}=y$, soit
$$x_y=y\ln x_y.\qquad(\ast)$$

**2. Équivalent de $\ln x_y$.** En prenant le logarithme de $(\ast)$ : $\ln x_y=\ln y+\ln(\ln x_y)$. Quand $y\to\infty$, $x_y\to\infty$ et $\frac{\ln(\ln x_y)}{\ln x_y}\to0$ (croissances comparées, avec $u=\ln x_y\to\infty$). Donc
$$\frac{\ln y}{\ln x_y}=1-\frac{\ln\ln x_y}{\ln x_y}\to1,\qquad\text{c'est-à-dire}\qquad\ln x_y\sim\ln y.$$

**2. Équivalent de $f^{-1}(y)$ et nature de la série.** Par $(\ast)$ : $f^{-1}(y)=y\ln x_y\sim y\ln y$. Donc, pour $n\ge3$,
$$\frac1{f^{-1}(n)}\sim\frac1{n\ln n}>0.$$
La série $\sum\frac1{n\ln n}$ diverge : la fonction $t\mapsto\frac1{t\ln t}$ est positive et décroissante sur $[3,+\infty[$, et $\int_3^X\frac{\mathrm dt}{t\ln t}=\ln\ln X-\ln\ln3\to+\infty$ (primitive $\ln(\ln t)$). Par comparaison de séries à termes positifs équivalents, $\sum_{n\ge3}\frac1{f^{-1}(n)}$ **diverge**.

**3. Équivalent des sommes partielles.** Pour des séries à termes positifs divergentes dont les termes sont équivalents, les sommes partielles sont équivalentes. Il suffit donc d'estimer $\sum_{k=3}^n\frac1{k\ln k}$. Comme $h(t)=\frac1{t\ln t}$ est décroissante, pour $k\ge4$ : $\int_k^{k+1}h\le h(k)\le\int_{k-1}^kh$. En sommant :
$$\int_4^{n+1}h\le\sum_{k=4}^nh(k)\le\int_3^nh,\qquad\text{soit}\qquad\ln\ln(n+1)-\ln\ln4\le\sum_{k=4}^n\frac1{k\ln k}\le\ln\ln n-\ln\ln3.$$
Les deux bornes sont équivalentes à $\ln\ln n$, donc $\sum_{k=3}^n\frac1{k\ln k}\sim\ln\ln n$.

**Conclusion.** $S_n=\displaystyle\sum_{k=3}^n\frac1{f^{-1}(k)}\sim\ln\ln n$ : la série diverge, mais extrêmement lentement.
"""

D['m-ccmp-07b'] = r"""
**Objectif.** Trouver $Q\in O_n(\mathbb R)$ telle que $M^{\top}M=Q\,(MM^{\top})\,Q^{\top}$.

**Étape 1 : les deux matrices sont symétriques.** $(MM^{\top})^{\top}=(M^{\top})^{\top}M^{\top}=MM^{\top}$ et de même $(M^{\top}M)^{\top}=M^{\top}M$.

**Étape 2 : réduction au polynôme caractéristique.** Notons $S_1=MM^{\top}$, $S_2=M^{\top}M$. Par le théorème spectral, $S_i=P_iD_iP_i^{\top}$ avec $P_i\in O_n(\mathbb R)$ et $D_i$ diagonale réelle, dont les coefficients diagonaux sont les valeurs propres de $S_i$ comptées avec multiplicité. Si $\chi_{S_1}=\chi_{S_2}$, les deux matrices ont les mêmes valeurs propres avec les mêmes multiplicités ; quitte à permuter les colonnes de $P_2$ (ce qui la laisse orthogonale), on peut ordonner les valeurs propres de la même façon : $D_1=D_2=D$. Alors $D=P_1^{\top}S_1P_1$ et
$$S_2=P_2DP_2^{\top}=P_2P_1^{\top}\,S_1\,P_1P_2^{\top}=Q\,S_1\,Q^{\top},\qquad Q=P_2P_1^{\top}\in O_n(\mathbb R)$$
(produit de matrices orthogonales). Il reste à prouver $\chi_{MM^{\top}}=\chi_{M^{\top}M}$.

**Étape 3 : lemme $\chi_{AB}=\chi_{BA}$, cas $A$ inversible.** Si $A$ est inversible, $BA=A^{-1}(AB)A$ : les deux matrices sont semblables, donc ont le même polynôme caractéristique.

**Étape 4 : cas général, par densité.** $A$ n'a qu'un nombre fini de valeurs propres, donc pour $k$ assez grand, $-\frac1k$ n'en est pas une et $A_k=A+\frac1kI_n$ est inversible. Par l'étape 3, $\chi_{A_kB}(x)=\chi_{BA_k}(x)$ pour tout réel $x$. Or $\chi_{A_kB}(x)=\det(xI_n-A_kB)$ est un polynôme en les coefficients de $A_k$, donc une fonction continue de $\frac1k$. En faisant $k\to\infty$ (avec $A_k\to A$) : $\chi_{AB}(x)=\chi_{BA}(x)$ pour tout $x$.

**Conclusion.** Avec $A=M$ et $B=M^{\top}$ : $\chi_{MM^{\top}}=\chi_{M^{\top}M}$. Par l'étape 2, $MM^{\top}$ et $M^{\top}M$ sont orthogonalement semblables.
"""
