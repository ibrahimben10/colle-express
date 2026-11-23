D = {}

D['x-r-1'] = r"""
**1. $1$ est valeur propre.** Avec $\mathbf 1=(1,\dots,1)^{\top}$, la $i$-ème coordonnée de $A\mathbf 1$ est $\sum_ja_{ij}=1$ : $A\mathbf 1=\mathbf 1$.

**1. Le sous-espace propre réel est une droite.** Soit $X\in\mathbb R^n$ avec $AX=X$ et $i$ tel que $x_i=\max_jx_j$. Alors, puisque $a_{ij}>0$ et $x_j\le x_i$ :
$$x_i=\sum_ja_{ij}x_j\le\sum_ja_{ij}x_i=x_i.$$
Il y a donc égalité, c'est-à-dire $\sum_ja_{ij}(x_i-x_j)=0$ : une somme de termes positifs nulle, donc chaque terme est nul, et comme $a_{ij}>0$, $x_j=x_i$ pour tout $j$. Ainsi $X\in\mathbb R\mathbf 1$.

**1. Sur $\mathbb C$.** Si $X\in\mathbb C^n$ vérifie $AX=X$, comme $A$ est réelle, $A(\mathrm{Re}\,X)=\mathrm{Re}\,X$ et $A(\mathrm{Im}\,X)=\mathrm{Im}\,X$ ; les deux sont dans $\mathbb R\mathbf 1$, donc $X\in\mathbb C\mathbf 1$. Ainsi $\ker(A-I_n)=\mathbb C\mathbf 1$ est de dimension 1.

**2. Majoration du module.** Soit $\lambda\in\mathbb C$ et $X\neq0$ avec $AX=\lambda X$ ; soit $i$ tel que $|x_i|=\max_j|x_j|>0$. Par l'inégalité triangulaire :
$$|\lambda|\,|x_i|=\Big|\sum_ja_{ij}x_j\Big|\le\sum_ja_{ij}|x_j|\le\sum_ja_{ij}|x_i|=|x_i|.\qquad(\ast)$$
Donc $|\lambda|\le1$.

**2. Cas $|\lambda|=1$.** Les deux inégalités de $(\ast)$ sont alors des égalités.
- La seconde : $\sum_ja_{ij}(|x_i|-|x_j|)=0$, somme de termes positifs, et $a_{ij}>0$, donc $|x_j|=|x_i|$ pour tout $j$.
- La première, $\big|\sum_ja_{ij}x_j\big|=\sum_j|a_{ij}x_j|$ : c'est le cas d'égalité de l'inégalité triangulaire, qui impose que tous les nombres non nuls $a_{ij}x_j$ aient le même argument. Comme $a_{ij}>0$, les $x_j$ ont tous le même argument.

Même module et même argument : tous les $x_j$ sont égaux, $X=x_i\mathbf 1$, donc $AX=X$ et $\lambda=1$.

**Conclusion.** Toute valeur propre vérifie $|\lambda|\le1$, et $1$ est la seule de module 1 ; son sous-espace propre est $\mathbb C\mathbf 1$. C'est le théorème de Perron-Frobenius pour les matrices stochastiques à coefficients strictement positifs ; il entraîne la convergence d'une chaîne de Markov vers sa loi stationnaire.
"""

D['x-r-2'] = r"""
**Polynôme annulateur de $A^p$.** $A^p$ est diagonalisable : en notant $\mu_1,\dots,\mu_r$ ses valeurs propres distinctes, elle est annulée par $\prod_{k=1}^r(X-\mu_k)$. Comme $A$ est inversible, $A^p$ l'est aussi ($\det(A^p)=(\det A)^p\neq0$), donc $\mu_k\neq0$ pour tout $k$.

**Polynôme annulateur de $A$.** Posons $Q=\prod_{k=1}^r(X^p-\mu_k)$. Alors $Q(A)=\prod_k(A^p-\mu_kI_n)=0$ : $Q$ annule $A$.

**$Q$ est à racines simples.**
- Chaque facteur $X^p-\mu_k$ a des racines simples : si $z^p=\mu_k$, alors $z\neq0$ (car $\mu_k\neq0$) et la dérivée $pz^{p-1}$ ne s'annule pas en $z$. (Ses $p$ racines sont les $z_0\omega^j$, $\omega=e^{2i\pi/p}$, distinctes.)
- Deux facteurs distincts n'ont pas de racine commune : si $z^p=\mu_k$ et $z^p=\mu_l$, alors $\mu_k=\mu_l$, donc $k=l$.

Ainsi $Q$ est scindé sur $\mathbb C$, à racines simples, et annule $A$ : $A$ est diagonalisable.

**Sans inversibilité, c'est faux.** $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ vérifie $A^2=0$, qui est diagonalisable. Mais $A$ est nilpotente non nulle : si elle était diagonalisable, sa seule valeur propre étant 0, elle serait nulle. L'argument échoue parce que pour $\mu=0$, $X^p$ a la racine multiple 0.
"""

D['x-r-3'] = r"""
**Traces des puissances.** Trigonalisons $A=PTP^{-1}$ sur $\mathbb C$, $T$ triangulaire de diagonale les valeurs propres. $A^k=PT^kP^{-1}$ et $T^k$ est triangulaire de diagonale les puissances $k$-ièmes. En notant $\lambda_1,\dots,\lambda_r$ les valeurs propres **distinctes non nulles** et $m_i$ leurs multiplicités :
$$\mathrm{Tr}(A^k)=\mathrm{Tr}(T^k)=\sum_{i=1}^rm_i\lambda_i^k.$$
(S'il n'y a pas de valeur propre non nulle, $A$ est nilpotente et il n'y a rien à démontrer.)

**Raisonnement par l'absurde.** Supposons $\rho=\max_i|\lambda_i|\ge1$. Soit $J=\{i:|\lambda_i|=\rho\}$ et, pour $i\in J$, $\lambda_i=\rho z_i$ avec $|z_i|=1$ (les $z_i$ sont distincts). En divisant par $\rho^k$ :
$$\frac{\mathrm{Tr}(A^k)}{\rho^k}=\underbrace{\sum_{i\in J}m_iz_i^k}_{u_k}+\sum_{i\notin J}m_i\Big(\frac{\lambda_i}\rho\Big)^k.$$
Le membre de gauche tend vers 0 (numérateur $\to0$ et $\rho^k\ge1$). Pour $i\notin J$, $\big|\frac{\lambda_i}\rho\big|<1$, donc la seconde somme tend vers 0. Ainsi $u_k\to0$.

**Moyenne de $|u_k|^2$.** Développons $|u_k|^2=u_k\overline{u_k}$ :
$$\frac1N\sum_{k=0}^{N-1}|u_k|^2=\sum_{i,j\in J}m_im_j\,\frac1N\sum_{k=0}^{N-1}(z_i\overline{z_j})^k.$$
- Si $i=j$ : $z_i\overline{z_i}=|z_i|^2=1$ et la moyenne vaut 1.
- Si $i\neq j$ : $w=z_i\overline{z_j}$ est de module 1 et différent de 1 (car $z_i\neq z_j$), et par la somme géométrique
$$\Big|\frac1N\sum_{k=0}^{N-1}w^k\Big|=\frac{|1-w^N|}{N|1-w|}\le\frac2{N|1-w|}\xrightarrow[N\to\infty]{}0.$$

Donc $\frac1N\sum_{k<N}|u_k|^2\to\sum_{i\in J}m_i^2\ge1$.

**Contradiction.** Si $u_k\to0$, alors $|u_k|^2\to0$ et, par le lemme de Cesàro, la moyenne $\frac1N\sum_{k<N}|u_k|^2$ tend vers 0. C'est incompatible avec la limite $\sum m_i^2\ge1$.

**Conclusion.** $\rho<1$ : toutes les valeurs propres de $A$ sont de module strictement inférieur à 1 (et alors $A^k\to0$, réciproquement).
"""

D['x-r-4'] = r"""
**1. Exponentielle d'une nilpotente.** Si $N^n=0$, la série $\exp N=\sum_k\frac{N^k}{k!}$ est une somme finie : $\exp N=I_n+N'$ avec $N'=\sum_{k=1}^{n-1}\frac{N^k}{k!}=N\,R$, où $R=\sum_{k\ge1}\frac{N^{k-1}}{k!}$ commute avec $N$. Alors $N'^n=N^nR^n=0$ : $N'$ est nilpotente et $\exp N$ est unipotente.

**1. Logarithme d'une unipotente.** Pour $M$ nilpotente, posons $\log(I_n+M)=\sum_{k=1}^{n-1}\frac{(-1)^{k+1}}kM^k$ (somme finie). C'est $M$ fois un polynôme en $M$, donc une matrice nilpotente.

**1. Les deux applications sont réciproques.** Dans l'anneau des séries formelles $\mathbb Q[[x]]$, on a les identités $\exp\big(\log(1+x)\big)=1+x$ et $\log\big(1+(\exp(x)-1)\big)=x$ (la composition de séries formelles est licite car $\log(1+x)$ et $\exp(x)-1$ n'ont pas de terme constant). Si l'on remplace $x$ par une matrice nilpotente $N$, toutes les séries deviennent des sommes finies (les termes de degré $\ge n$ disparaissent), et la substitution respecte sommes et produits de polynômes en $N$ (ce sont des éléments de l'algèbre commutative $\mathbb C[N]$). On obtient
$$\exp\big(\log(I_n+M)\big)=I_n+M,\qquad\log\big(\exp N\big)=N.$$
Donc $\exp$ est une bijection de l'ensemble des matrices nilpotentes sur celui des matrices unipotentes, de réciproque $\log$.

**2. Inclusion $\exp(\mathcal M_n(\mathbb C))\subset GL_n(\mathbb C)$.** $M$ et $-M$ commutent, donc $\exp(M)\exp(-M)=\exp(0)=I_n$ : $\exp M$ est inversible.

**2. Inclusion réciproque : décomposition en blocs.** Soit $M\in GL_n(\mathbb C)$, de polynôme caractéristique $\prod_\lambda(X-\lambda)^{m_\lambda}$ (avec $\lambda\neq0$). Par le lemme des noyaux, $\mathbb C^n=\bigoplus_\lambda F_\lambda$ avec $F_\lambda=\ker(M-\lambda I)^{m_\lambda}$, sous-espaces stables par $M$. Sur $F_\lambda$, $M$ induit $\lambda\,\mathrm{id}+N_\lambda$ avec $N_\lambda$ nilpotent, soit $\lambda\big(\mathrm{id}+\frac{N_\lambda}\lambda\big)$.

**2. Logarithme de chaque bloc.** Choisissons $\mu\in\mathbb C$ avec $e^\mu=\lambda$ (possible car $\lambda\neq0$ : $\mu=\ln|\lambda|+i\arg\lambda$). Posons $L_\lambda=\mu\,\mathrm{id}+\log\big(\mathrm{id}+\frac{N_\lambda}\lambda\big)$. Les deux termes commutent, donc
$$\exp(L_\lambda)=e^\mu\exp\Big(\log\Big(\mathrm{id}+\frac{N_\lambda}\lambda\Big)\Big)=\lambda\Big(\mathrm{id}+\frac{N_\lambda}\lambda\Big)=M_{|F_\lambda}.$$

**2. Recollement.** Soit $B$ l'endomorphisme égal à $L_\lambda$ sur chaque $F_\lambda$. Dans une base adaptée à la décomposition, $B$ et $M$ sont diagonales par blocs, et l'exponentielle d'une matrice diagonale par blocs est diagonale par blocs (bloc par bloc). Donc $\exp B=M$.

**Conclusion.** $\exp(\mathcal M_n(\mathbb C))=GL_n(\mathbb C)$. Sur $\mathbb R$, c'est faux : $\det(\exp M)=e^{\mathrm{Tr}\,M}>0$, et même certaines matrices de déterminant positif ne sont pas des exponentielles réelles (par exemple $\mathrm{diag}(-1,-2)$).
"""
