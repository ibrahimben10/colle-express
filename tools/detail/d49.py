D = {}

D['n-m-extrema'] = r"""
**1. Points critiques.** $f$ est polynomiale, donc de classe $C^\infty$ sur l'ouvert $\mathbb R^2$. Ses dérivées partielles valent
$$\frac{\partial f}{\partial x}=4x^3-4(x-y),\qquad\frac{\partial f}{\partial y}=4y^3+4(x-y).$$
Un point critique annule les deux. En les additionnant : $4(x^3+y^3)=0$, donc $y^3=-x^3$, et $y=-x$ (la fonction cube est injective sur $\mathbb R$). En reportant dans la première équation : $4x^3-4(2x)=0$, soit $4x(x^2-2)=0$, d'où $x\in\{0,\sqrt2,-\sqrt2\}$.

Les points critiques sont $(0,0)$, $(\sqrt2,-\sqrt2)$ et $(-\sqrt2,\sqrt2)$.

**2. Existence d'un minimum global.** On a $(x-y)^2\le2(x^2+y^2)$ (car $2xy\ge-(x^2+y^2)$) et $x^4+y^4\ge\frac{(x^2+y^2)^2}2$ (Cauchy-Schwarz). Avec $r^2=x^2+y^2$ :
$$f(x,y)\ge\frac{r^4}2-4r^2\xrightarrow[r\to+\infty]{}+\infty.$$
$f$ est donc coercive. Il existe $\rho$ tel que $f>0=f(0,0)$ hors du disque fermé $\overline D(0,\rho)$. Sur ce compact, $f$ continue atteint son minimum, qui est le minimum global de $f$ sur $\mathbb R^2$. Ce minimum est atteint en un point intérieur (l'ouvert $\mathbb R^2$), donc en un point critique.

**3. Valeurs aux points critiques.**
- $f(0,0)=0$.
- $f(\sqrt2,-\sqrt2)=4+4-2(2\sqrt2)^2=8-16=-8$, et de même $f(-\sqrt2,\sqrt2)=-8$ (car $f(-x,-y)=f(x,y)$).

Le minimum global vaut $-8$, atteint en $(\sqrt2,-\sqrt2)$ et $(-\sqrt2,\sqrt2)$. Ce sont aussi des minima locaux.

**4. Nature de $(0,0)$.** On étudie $f$ sur deux droites passant par l'origine.
- Sur $y=x$ : $f(x,x)=2x^4>0$ pour $x\neq0$.
- Sur $y=0$ : $f(x,0)=x^4-2x^2=x^2(x^2-2)<0$ pour $0<|x|<\sqrt2$.

Dans tout voisinage de $(0,0)$, $f$ prend des valeurs strictement supérieures et strictement inférieures à $f(0,0)=0$ : ce n'est ni un minimum ni un maximum local, mais un **point col** (point selle).

**5. Pas de maximum.** $f\to+\infty$ à l'infini, donc il n'y a pas de maximum global. Un maximum local serait un point critique, et aucun ne convient. Il n'y a donc **aucun maximum**.

**Remarque.** La hessienne en $(0,0)$ vaut $\begin{pmatrix}-4&4\\4&-4\end{pmatrix}$, de déterminant nul : le critère du second ordre ne conclut pas, d'où l'étude directe sur des droites.
"""

D['n-m-In'] = r"""
**1. Changement de variable.** $u=e^t-1$ est de classe $C^1$ et strictement croissante de $[0,\ln2]$ sur $[0,1]$, avec $\mathrm du=e^t\,\mathrm dt=(1+u)\,\mathrm dt$. Donc
$$I_n=\int_0^{\ln2}(e^t-1)^n\,\mathrm dt=\int_0^1\frac{u^n}{1+u}\,\mathrm du.$$

**1. Relation de récurrence.** Pour $n\ge1$ :
$$I_n+I_{n-1}=\int_0^1\frac{u^n+u^{n-1}}{1+u}\,\mathrm du=\int_0^1\frac{u^{n-1}(u+1)}{1+u}\,\mathrm du=\int_0^1u^{n-1}\,\mathrm du=\frac1n.$$
Avec $I_0=\ln2$, cela détermine tous les $I_n$ ; par exemple $I_1=1-\ln2$.

**2. Monotonie.** Pour $u\in[0,1]$, $u^{n+1}\le u^n$, donc $I_{n+1}\le I_n$ : la suite $(I_n)$ est décroissante. Elle est aussi positive.

**2. Encadrement.** Avec la décroissance et la relation de récurrence :
$$\frac1{n+1}=I_{n+1}+I_n\le2I_n\le I_n+I_{n-1}=\frac1n.$$
Donc $\frac1{2(n+1)}\le I_n\le\frac1{2n}$. Comme $\frac{n}{n+1}\to1$, on obtient par encadrement $2nI_n\to1$, soit
$$I_n\sim\frac1{2n}.$$

**3. Rayon de convergence.** $|I_nx^n|\sim\frac{|x|^n}{2n}$. Deux séries entières dont les coefficients sont équivalents ont le même rayon, donc $R$ est le rayon de $\sum\frac{x^n}n$ : $R=1$ (règle de d'Alembert).

**4. Interversion.** Soit $x\in]-1,1[$. Pour $u\in[0,1]$ :
$$\sum_{n\ge0}\frac{(xu)^n}{1+u}=\frac1{(1+u)(1-xu)},\qquad\Big|\frac{(xu)^n}{1+u}\Big|\le|x|^n.$$
$\sum|x|^n$ converge : la série de fonctions converge normalement, donc uniformément, sur le segment $[0,1]$. On peut intégrer terme à terme :
$$\sum_{n=0}^{+\infty}I_nx^n=\int_0^1\frac{\mathrm du}{(1+u)(1-xu)}.$$

**4. Décomposition en éléments simples** (en $u$, pour $x\neq-1$) :
$$\frac1{(1+u)(1-xu)}=\frac1{1+x}\Big(\frac1{1+u}+\frac x{1-xu}\Big).$$
Vérification : $\frac{(1-xu)+x(1+u)}{(1+u)(1-xu)}=\frac{1+x}{(1+u)(1-xu)}$. ✓

**4. Intégration.** $\int_0^1\frac{\mathrm du}{1+u}=\ln2$, et $\int_0^1\frac{x\,\mathrm du}{1-xu}=\big[-\ln(1-xu)\big]_0^1=-\ln(1-x)$. Donc
$$\sum_{n=0}^{+\infty}I_nx^n=\frac{\ln2-\ln(1-x)}{1+x},\qquad x\in]-1,1[.$$
Vérification en $x=0$ : on retrouve $I_0=\ln2$. ✓ Le développement en série entière du membre de droite redonne aussi la relation $I_n+I_{n-1}=\frac1n$.
"""

D['n-m-double'] = r"""
**1. Factorisation.** $m^2n+mn^2+2mn=mn(m+n+2)$, donc le terme général vaut $\frac1{mn(m+n+2)}>0$.

**2. Écriture intégrale.** Pour un entier $k\ge0$, $\int_0^1x^k\,\mathrm dx=\frac1{k+1}$. Avec $k=m+n+1$ :
$$\frac1{m+n+2}=\int_0^1x^{m+n+1}\,\mathrm dx,\qquad\text{donc}\qquad\frac1{mn(m+n+2)}=\int_0^1x\cdot\frac{x^m}m\cdot\frac{x^n}n\,\mathrm dx.$$

**3. Interversion.** Tous les termes sont positifs. Le théorème de Fubini-Tonelli (pour les séries doubles et l'intégration terme à terme de séries de fonctions positives) permet d'intervertir les sommes et l'intégrale, l'égalité ayant lieu dans $[0,+\infty]$ :
$$S=\int_0^1x\Big(\sum_{m\ge1}\frac{x^m}m\Big)\Big(\sum_{n\ge1}\frac{x^n}n\Big)\mathrm dx.$$

**3. Sommes intérieures.** Pour $x\in[0,1[$, $\sum_{m\ge1}\frac{x^m}m=-\ln(1-x)$. Donc
$$S=\int_0^1x\ln^2(1-x)\,\mathrm dx.$$
Il reste à vérifier que cette intégrale est finie : la finitude de $S$ en découlera.

**4. Changement de variable.** Avec $y=1-x$ :
$$S=\int_0^1(1-y)\ln^2y\,\mathrm dy=\int_0^1\ln^2y\,\mathrm dy-\int_0^1y\ln^2y\,\mathrm dy.$$

**4. Intégrale de référence.** Pour $a\ge0$, notons $J_a=\int_0^1y^a\ln^2y\,\mathrm dy$. Elle converge, car $y^a\ln^2y=o\big(y^{-1/2}\big)$ en $0$ (croissances comparées). Une intégration par parties sur $[\varepsilon,1]$, avec $u=\ln^2y$ et $v'=y^a$, donne
$$J_a=\Big[\frac{y^{a+1}}{a+1}\ln^2y\Big]_0^1-\frac2{a+1}\int_0^1y^a\ln y\,\mathrm dy.$$
Le crochet est nul (il tend vers 0 en $0^+$). Une seconde intégration par parties donne $\int_0^1y^a\ln y\,\mathrm dy=-\frac1{(a+1)^2}$. Donc
$$J_a=\frac2{(a+1)^3}.$$
(On peut aussi poser $y=e^{-s}$ et utiliser $\int_0^\infty s^2e^{-(a+1)s}\,\mathrm ds=\frac{2}{(a+1)^3}$.)

**5. Conclusion.** $J_0=2$ et $J_1=\frac28=\frac14$, donc
$$S=J_0-J_1=2-\frac14=\frac74.$$
La somme est finie et vaut $\frac74$.
"""

D['n-m-blocs'] = r"""
**1. Cas des monômes.** Montrons par récurrence que $M^k=\begin{pmatrix}A^k&kA^{k-1}B\\0&A^k\end{pmatrix}$ pour $k\ge1$ (et $M^0=I_{2n}$). Le cas $k=1$ est immédiat. Si c'est vrai au rang $k$, le produit par blocs donne
$$M^{k+1}=\begin{pmatrix}A^k&kA^{k-1}B\\0&A^k\end{pmatrix}\begin{pmatrix}A&B\\0&A\end{pmatrix}=\begin{pmatrix}A^{k+1}&A^kB+kA^{k-1}BA\\0&A^{k+1}\end{pmatrix}.$$
Comme $AB=BA$, $A^{k-1}BA=A^kB$, et le bloc en haut à droite vaut $(k+1)A^kB$. ✓

**1. Cas général.** Pour $P=\sum a_kX^k$, par linéarité :
$$P(M)=\sum_ka_kM^k=\begin{pmatrix}\sum a_kA^k&\sum ka_kA^{k-1}B\\0&\sum a_kA^k\end{pmatrix}=\begin{pmatrix}P(A)&P'(A)B\\0&P(A)\end{pmatrix}.$$

**2. Énoncé.** Montrons que $M$ est diagonalisable si et seulement si **$A$ est diagonalisable et $B=0$**.

**2. Sens réciproque.** Si $B=0$ et $A=QDQ^{-1}$, alors $M=\mathrm{diag}(A,A)=\mathrm{diag}(Q,Q)\,\mathrm{diag}(D,D)\,\mathrm{diag}(Q,Q)^{-1}$ est diagonalisable.

**2. Sens direct : critère utilisé.** Sur $\mathbb C$, une matrice est diagonalisable si et seulement si elle est annulée par un polynôme scindé à racines simples.

**2. Sens direct : conséquences.** Soit $P$ scindé à racines simples tel que $P(M)=0$. D'après la question 1 :
- le bloc diagonal donne $P(A)=0$, donc $A$ est diagonalisable ;
- le bloc en haut à droite donne $P'(A)B=0$.

**2. $P'(A)$ est inversible.** $A$ est diagonalisable, $A=QDQ^{-1}$ avec $D=\mathrm{diag}(\lambda_i)$, donc $P'(A)=Q\,\mathrm{diag}\big(P'(\lambda_i)\big)Q^{-1}$. Chaque valeur propre $\lambda_i$ de $A$ est racine de $P$ (car $P(A)=0$ donne $P(\lambda_i)=0$). Les racines de $P$ sont simples, donc $P'(\lambda_i)\neq0$. Ainsi $P'(A)$ est inversible.

**2. Conclusion.** De $P'(A)B=0$, on déduit $B=P'(A)^{-1}\cdot0=0$.

**Exemple.** Pour $n=1$, $A=(a)$ et $B=(b)$ : $M=\begin{pmatrix}a&b\\0&a\end{pmatrix}$ a une seule valeur propre $a$, et elle est diagonalisable si et seulement si $M=aI_2$, c'est-à-dire $b=0$. C'est le cas le plus simple de ce résultat (bloc de Jordan).
"""

D['n-m-pieces'] = r"""
**1. Univers.** Chaque personne obtient pile ou face, de façon indépendante et équiprobable. L'univers est $\{P,F\}^n$, de cardinal $2^n$, muni de la probabilité uniforme.

**1. Issues favorables.** L'événement « exactement une personne a un résultat différent de toutes les autres » signifie qu'une personne obtient un résultat, et les $n-1$ autres le résultat opposé. Pour décrire une telle issue, on choisit :
- la personne isolée : $n$ choix ;
- son résultat (pile ou face) : 2 choix, les autres ayant alors le résultat opposé.

**1. Distinction des issues.** Pour $n\ge3$, l'intrus est l'unique personne minoritaire ($1<n-1$), donc ces $2n$ issues sont deux à deux distinctes et il n'y en a pas d'autre. Par équiprobabilité :
$$p_n=\frac{2n}{2^n}=\frac n{2^{n-1}}.$$
Par exemple $p_3=\frac34$, $p_4=\frac12$, $p_5=\frac5{16}$.

**2. Loi de $X$.** Les expériences successives sont indépendantes et ont chacune la probabilité de succès $p_n$. $X$ est le rang du premier succès : $X$ suit la loi géométrique $\mathcal G(p_n)$. En effet, $(X=k)$ signifie $k-1$ échecs puis un succès, donc, par indépendance,
$$P(X=k)=(1-p_n)^{k-1}p_n,\qquad k\in\mathbb N^*.$$

**2. Espérance et variance.** Ce sont les résultats classiques pour la loi géométrique :
$$E(X)=\frac1{p_n}=\frac{2^{n-1}}n,\qquad V(X)=\frac{1-p_n}{p_n^2}.$$
Par exemple, pour $n=3$, $E(X)=\frac43$. Pour $n=10$, $E(X)=\frac{512}{10}\approx51$ : avec beaucoup de joueurs, il faut en moyenne beaucoup de lancers pour départager. Le nombre moyen croît exponentiellement avec $n$.

**3. Rôle de $n\ge3$.** Pour $n=2$, si les deux résultats diffèrent, chacun des deux joueurs a un résultat différent de « toutes les autres » (c'est-à-dire de l'autre). Il y a alors deux intrus, et l'événement « exactement une personne » n'est jamais réalisé ($p_2=0$). La formule $\frac{2n}{2^n}=1$ serait fausse, car chaque issue « résultats différents » serait comptée deux fois, l'intrus n'étant pas unique. Pour $n\ge3$, l'intrus, s'il existe, est l'unique minoritaire, et le dénombrement est correct. C'est pourquoi ce jeu sert à désigner une personne dans un groupe d'au moins trois.
"""
