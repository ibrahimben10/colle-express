D = {}

D['x-al-1'] = r"""
**1. Majoration.** Pour tout $x$, $(a+b)(x)=a(x)+b(x)\in\mathrm{Im}\,a+\mathrm{Im}\,b$. Donc $\mathrm{Im}(a+b)\subset\mathrm{Im}\,a+\mathrm{Im}\,b$ et, par la formule de Grassmann,
$$\mathrm{rg}(a+b)\le\dim(\mathrm{Im}\,a+\mathrm{Im}\,b)=\mathrm{rg}\,a+\mathrm{rg}\,b-\dim(\mathrm{Im}\,a\cap\mathrm{Im}\,b)\le\mathrm{rg}\,a+\mathrm{rg}\,b.$$

**1. Minoration.** On applique la majoration à $a=(a+b)+(-b)$, avec $\mathrm{rg}(-b)=\mathrm{rg}\,b$ : $\mathrm{rg}\,a\le\mathrm{rg}(a+b)+\mathrm{rg}\,b$. De même $\mathrm{rg}\,b\le\mathrm{rg}(a+b)+\mathrm{rg}\,a$. Donc
$$|\mathrm{rg}\,a-\mathrm{rg}\,b|\le\mathrm{rg}(a+b)\le\mathrm{rg}\,a+\mathrm{rg}\,b.$$

**2. Sens réciproque.** Supposons $\mathrm{Im}\,a\cap\mathrm{Im}\,b=\{0\}$ et $\ker a+\ker b=E$. Soit $y=a(x)\in\mathrm{Im}\,a$. Écrivons $x=k_a+k_b$ avec $k_a\in\ker a$, $k_b\in\ker b$. Alors
$$y=a(k_a)+a(k_b)=a(k_b)=a(k_b)+b(k_b)=(a+b)(k_b)\in\mathrm{Im}(a+b).$$
De même $\mathrm{Im}\,b\subset\mathrm{Im}(a+b)$. Donc $\mathrm{Im}\,a+\mathrm{Im}\,b\subset\mathrm{Im}(a+b)$, et avec l'inclusion de la question 1, il y a égalité. La somme étant directe : $\mathrm{rg}(a+b)=\mathrm{rg}\,a+\mathrm{rg}\,b$.

**2. Sens direct.** Supposons $\mathrm{rg}(a+b)=\mathrm{rg}\,a+\mathrm{rg}\,b$. La chaîne d'inégalités de la question 1 est alors une chaîne d'égalités, donc $\dim(\mathrm{Im}\,a\cap\mathrm{Im}\,b)=0$ : $\mathrm{Im}\,a\cap\mathrm{Im}\,b=\{0\}$.
- Noyau de $a+b$ : si $(a+b)(x)=0$, alors $a(x)=-b(x)=b(-x)\in\mathrm{Im}\,a\cap\mathrm{Im}\,b=\{0\}$, donc $x\in\ker a\cap\ker b$. L'inclusion inverse est évidente : $\ker(a+b)=\ker a\cap\ker b$.
- Par le théorème du rang : $\dim(\ker a\cap\ker b)=n-\mathrm{rg}(a+b)=n-\mathrm{rg}\,a-\mathrm{rg}\,b$.
- Par Grassmann :
$$\dim(\ker a+\ker b)=(n-\mathrm{rg}\,a)+(n-\mathrm{rg}\,b)-(n-\mathrm{rg}\,a-\mathrm{rg}\,b)=n.$$
Donc $\ker a+\ker b=E$.

**3. Majoration.** $\mathrm{Im}(ab)=a(b(E))\subset a(E)$ : $\mathrm{rg}(ab)\le\mathrm{rg}\,a$. Et $\mathrm{Im}(ab)=a(\mathrm{Im}\,b)$ est l'image de $\mathrm{Im}\,b$ par une application linéaire : sa dimension est au plus $\dim\mathrm{Im}\,b=\mathrm{rg}\,b$.

**3. Minoration (inégalité de Sylvester).** Soit $c$ la restriction de $a$ à $\mathrm{Im}\,b$. Son image est $a(\mathrm{Im}\,b)=\mathrm{Im}(ab)$ et son noyau est $\ker a\cap\mathrm{Im}\,b$. Le théorème du rang appliqué à $c$ donne
$$\mathrm{rg}(ab)=\mathrm{rg}\,b-\dim(\ker a\cap\mathrm{Im}\,b)\ge\mathrm{rg}\,b-\dim\ker a=\mathrm{rg}\,b-(n-\mathrm{rg}\,a).$$

**Conclusion.** $\mathrm{rg}\,a+\mathrm{rg}\,b-n\le\mathrm{rg}(ab)\le\min(\mathrm{rg}\,a,\mathrm{rg}\,b)$.
"""

D['x-al-2'] = r"""
**1. Développement par multilinéarité.** La ligne $i$ de $M$ s'écrit $L_i=\sum_{j=1}^nm_{ij}\varepsilon_j$, où $\varepsilon_j$ est la $j$-ième ligne de la base canonique. Le déterminant est linéaire par rapport à chaque ligne ; en développant les $n$ lignes :
$$\det M=\sum_{\sigma}\Big(\prod_{i=1}^nm_{i\sigma(i)}\Big)\det\big(\varepsilon_{\sigma(1)},\dots,\varepsilon_{\sigma(n)}\big),$$
la somme portant sur **toutes** les applications $\sigma:[\![1,n]\!]\to[\![1,n]\!]$. Si $\sigma$ n'est pas injective, deux lignes sont égales et le déterminant est nul ; si $\sigma$ est une permutation, il vaut $\varepsilon(\sigma)$. On retrouve la formule $\det M=\sum_{\sigma\in S_n}\varepsilon(\sigma)\prod_im_{i\sigma(i)}$.

**1. Majoration.** Par l'inégalité triangulaire, puis en ajoutant les termes positifs des applications non injectives :
$$|\det M|\le\sum_{\sigma\in S_n}\prod_im_{i\sigma(i)}\le\sum_{\text{toutes }\sigma}\prod_im_{i\sigma(i)}=\prod_{i=1}^n\Big(\sum_{j=1}^nm_{ij}\Big)=1.$$
(L'égalité du milieu est le développement du produit de $n$ sommes : on choisit un terme dans chaque facteur.)

**1. Autre méthode par les valeurs propres.** Si $MX=\lambda X$ avec $X\neq0$ et $|x_i|=\max_j|x_j|>0$, alors $|\lambda||x_i|=\big|\sum_jm_{ij}x_j\big|\le\sum_jm_{ij}|x_j|\le|x_i|$, donc $|\lambda|\le1$, et $|\det M|=\prod|\lambda_k|\le1$.

**2. Les applications non injectives ont un produit nul.** Si $|\det M|=1$, toutes les inégalités ci-dessus sont des égalités ; en particulier, pour toute $\sigma$ non injective, $\prod_im_{i\sigma(i)}=0$.

**2. Chaque ligne a un seul coefficient non nul.** Par l'absurde, supposons que la ligne $i_0$ a deux coefficients strictement positifs, en colonnes $j\neq k$. Chaque ligne a au moins un coefficient $>0$ (somme 1) : choisissons $c_r$ avec $m_{rc_r}>0$ pour $r\neq i_0$, et $c_{i_0}=j$. L'application $r\mapsto c_r$ a un produit $\prod_rm_{rc_r}>0$, donc elle est injective, donc c'est une permutation. Il existe alors $r'\neq i_0$ avec $c_{r'}=k$. En remplaçant $c_{i_0}=j$ par $k$, on obtient une application non injective ($k$ atteint deux fois) de produit encore $>0$ : contradiction.

**2. Conclusion.** Chaque ligne contient un seul coefficient non nul, qui vaut 1 (somme de la ligne). Si deux lignes avaient leur 1 dans la même colonne, deux lignes seraient égales et $\det M=0$. Les positions des 1 définissent donc une permutation : $M$ est une **matrice de permutation**, de déterminant $\pm1$. Réciproquement, une matrice de permutation est stochastique et $|\det M|=1$.
"""

D['x-al-3'] = r"""
**Notations.** $\lambda_1,\dots,\lambda_n$ sont les valeurs propres de $A$ comptées avec multiplicité ($\chi_A=\prod(X-\lambda_i)$), et $\mu_i=\prod_{j\neq i}\lambda_j$. On va montrer que $\chi_{\tilde A}=\prod_{i=1}^n(X-\mu_i)$ pour toute $A$.

**Cas $A$ inversible.** La relation $A\,{}^t\mathrm{com}(A)=\det(A)I_n$ donne $\tilde A=\det(A)\,A^{-1}$. Les valeurs propres de $A^{-1}$ sont les $\frac1{\lambda_i}$ (avec multiplicités : trigonaliser $A=PTP^{-1}$, alors $A^{-1}=PT^{-1}P^{-1}$ et $T^{-1}$ est triangulaire de diagonale $\frac1{\lambda_i}$). Donc celles de $\tilde A$ sont
$$\det(A)\cdot\frac1{\lambda_i}=\frac{\lambda_1\cdots\lambda_n}{\lambda_i}=\prod_{j\neq i}\lambda_j=\mu_i.$$

**Cas général : continuité.** Considérons $Q_A=\prod_i(X-\mu_i)$. Ses coefficients sont des polynômes symétriques en $\lambda_1,\dots,\lambda_n$ ; par le théorème des polynômes symétriques, ce sont des polynômes en les fonctions symétriques élémentaires des $\lambda_i$, c'est-à-dire (au signe près) en les coefficients de $\chi_A$, eux-mêmes polynomiaux en les coefficients de $A$. Donc $A\mapsto Q_A$ est continue. De même, les coefficients de $\tilde A$ sont des mineurs de $A$ (polynomiaux), donc $A\mapsto\chi_{\tilde A}$ est continue.

**Densité.** $GL_n(\mathbb C)$ est dense dans $\mathcal M_n(\mathbb C)$ : $A+\frac1kI_n$ est inversible pour $k$ assez grand (seulement un nombre fini de $-\frac1k$ peuvent être valeurs propres de $A$). Les deux applications continues $A\mapsto\chi_{\tilde A}$ et $A\mapsto Q_A$ coïncident sur $GL_n(\mathbb C)$ ; en passant à la limite, elles coïncident partout.

**Conclusion.** Pour toute $A$, $\mathrm{Sp}(\tilde A)=\{\mu_i\}=\big\{\prod_{j\neq i}\lambda_j\big\}$ (avec multiplicités).

**Lecture selon le rang.**
- $\mathrm{rg}\,A=n$ : $\mathrm{Sp}\,\tilde A=\big\{\frac{\det A}{\lambda_i}\big\}$, toutes non nulles.
- $\mathrm{rg}\,A=n-1$ : $0$ est valeur propre. Si elle est simple ($\lambda_1=0$, les autres non nulles), alors $\mu_1=\lambda_2\cdots\lambda_n\neq0$ et $\mu_i=0$ pour $i\ge2$ : spectre $\{0\ (n-1\text{ fois}),\ \lambda_2\cdots\lambda_n\}$. Si 0 est au moins double, tous les $\mu_i$ sont nuls et $\tilde A$ est nilpotente (non nulle, car $\tilde A$ est de rang 1 dans ce cas).
- $\mathrm{rg}\,A\le n-2$ : tous les mineurs d'ordre $n-1$ sont nuls, donc $\tilde A=0$ (cohérent : au moins deux $\lambda_j$ sont nuls, tous les $\mu_i$ le sont).
"""

D['x-al-4'] = r"""
**1. Cas $n>m$.** Le rang d'un produit est au plus le rang de chaque facteur : $\mathrm{rg}\,C\le\mathrm{rg}\,A\le m$ ($A$ a $m$ colonnes). Comme $m<n$, $C\in\mathcal M_n(K)$ n'est pas de rang maximal, donc $\det C=0$.

**2. Colonnes de $C$.** Notons $A_1,\dots,A_m$ les colonnes de $A$. Par définition du produit, la $j$-ième colonne de $C=AB$ est
$$C_j=\sum_{k=1}^mB_{kj}A_k.$$

**2. Développement par multilinéarité.** Le déterminant est linéaire par rapport à chaque colonne ; en développant les $n$ colonnes, on choisit pour chaque $j$ un indice $\kappa(j)\in[\![1,m]\!]$ :
$$\det C=\sum_{\kappa:[\![1,n]\!]\to[\![1,m]\!]}\Big(\prod_{j=1}^nB_{\kappa(j)j}\Big)\det\big(A_{\kappa(1)},\dots,A_{\kappa(n)}\big).$$

**2. Seules les injections comptent.** Si $\kappa$ n'est pas injective, deux colonnes du déterminant sont égales : il est nul (forme alternée).

**2. Regroupement par ensemble d'indices.** Une injection $\kappa$ a pour image un ensemble $\{k_1<\dots<k_n\}$, et s'écrit de façon unique $\kappa(j)=k_{\sigma(j)}$ avec $\sigma\in S_n$. Permuter les colonnes multiplie le déterminant par la signature :
$$\det\big(A_{k_{\sigma(1)}},\dots,A_{k_{\sigma(n)}}\big)=\varepsilon(\sigma)\det\big(A_{k_1},\dots,A_{k_n}\big)=\varepsilon(\sigma)\,A\binom{1\cdots n}{k_1\cdots k_n}.$$

**2. Reconnaissance du second mineur.** Pour $k_1<\dots<k_n$ fixés :
$$\sum_{\sigma\in S_n}\varepsilon(\sigma)\prod_{j=1}^nB_{k_{\sigma(j)}j}=\det\big(B_{k_ij}\big)_{1\le i,j\le n}=B\binom{k_1\cdots k_n}{1\cdots n},$$
par la formule du déterminant (somme sur les permutations) appliquée à la sous-matrice de $B$ formée des lignes $k_1,\dots,k_n$.

**Conclusion.**
$$\det(AB)=\sum_{1\le k_1<\dots<k_n\le m}A\binom{1\cdots n}{k_1\cdots k_n}B\binom{k_1\cdots k_n}{1\cdots n}.$$
Pour $n=m$, il n'y a qu'un terme et on retrouve $\det(AB)=\det A\det B$.

**Application.** Pour $A$ réelle et $B=A^{\top}$ : $\det(AA^{\top})=\sum\big(A\binom{1\cdots n}{k}\big)^2\ge0$. Pour $n=2$, $m=3$, $A$ de lignes $u,v$ : $\|u\|^2\|v\|^2-(u\cdot v)^2=\|u\wedge v\|^2$ (identité de Lagrange).
"""
