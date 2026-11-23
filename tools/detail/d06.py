D = {}

D['m-ccmp-11a'] = r"""
**Notations.** $q(X)=X^{\top}MX$ et $K=\{X\in\mathbb R^n:q(X)\le1\}$.

**Étape 1 : $K$ est fermé.** $q$ est une fonction polynomiale des coordonnées de $X$ ($q(X)=\sum_{i,j}m_{ij}x_ix_j$), donc continue. $K=q^{-1}\big(]-\infty,1]\big)$ est l'image réciproque d'un fermé par une application continue : c'est un fermé. En dimension finie, un fermé est compact si et seulement s'il est borné (Borel-Lebesgue / Bolzano-Weierstrass). Tout se ramène donc à : **$K$ est-il borné ?**

**Étape 2 : écriture spectrale de $q$.** Par le théorème spectral, $M=PDP^{\top}$ avec $P\in O_n(\mathbb R)$ et $D=\mathrm{diag}(\lambda_1,\dots,\lambda_n)$. En posant $Y=P^{\top}X$ (qui vérifie $\|Y\|=\|X\|$ car $P^{\top}$ est orthogonale) :
$$q(X)=X^{\top}PDP^{\top}X=Y^{\top}DY=\sum_{i=1}^n\lambda_iy_i^2.$$

**Sens direct : $M\in\mathcal S_n^{++}\Rightarrow K$ compact.** Si $M\in\mathcal S_n^{++}$, toutes les valeurs propres sont strictement positives ; soit $\lambda_{\min}>0$ la plus petite. Alors
$$q(X)=\sum\lambda_iy_i^2\ge\lambda_{\min}\sum y_i^2=\lambda_{\min}\|X\|^2.$$
Pour $X\in K$ : $\lambda_{\min}\|X\|^2\le q(X)\le1$, donc $\|X\|\le\frac1{\sqrt{\lambda_{\min}}}$. $K$ est borné, et fermé : il est compact.

**Sens réciproque, par contraposée.** Supposons $M\notin\mathcal S_n^{++}$ : $M$ a une valeur propre $\lambda\le0$, associée à un vecteur propre $V\neq0$. Pour tout $t\in\mathbb R$ :
$$q(tV)=t^2\,V^{\top}MV=t^2\lambda\|V\|^2\le0\le1,$$
donc $tV\in K$. Ainsi $K$ contient toute la droite $\mathbb RV$ : $\|tV\|=|t|\,\|V\|\to+\infty$, $K$ n'est pas borné, donc pas compact.

**Conclusion.** $K$ est compact si et seulement si $M\in\mathcal S_n^{++}(\mathbb R)$. (C'est alors un ellipsoïde plein, d'axes les vecteurs propres et de demi-axes $1/\sqrt{\lambda_i}$.)
"""

D['m-ccmp-11b'] = r"""
**Sens réciproque : une limite de fonctions convexes est convexe.** Supposons $P_n\to f$ uniformément, donc simplement, sur $[a,b]$, avec $P_n$ convexe sur $[a,b]$. Soient $x,y\in[a,b]$ et $t\in[0,1]$ ; pour tout $n$ :
$$P_n\big((1-t)x+ty\big)\le(1-t)P_n(x)+tP_n(y).$$
En faisant $n\to\infty$ (convergence simple aux trois points concernés, inégalité large conservée) : $f\big((1-t)x+ty\big)\le(1-t)f(x)+tf(y)$. Donc $f$ est convexe. (Ce sens n'utilise pas la régularité de $f$.)

**Sens direct, étape 1 : approcher $f''$ par des polynômes positifs.** $f$ est $C^2$ et convexe, donc $f''\ge0$ sur $[a,b]$, et $f''$ est continue. Par le théorème de Weierstrass, il existe des polynômes $Q_n$ avec $\varepsilon_n=\|Q_n-f''\|_\infty\to0$. Posons $R_n=Q_n+\varepsilon_n$ (polynôme). Pour tout $x\in[a,b]$ :
$$R_n(x)=f''(x)+\big(Q_n(x)-f''(x)\big)+\varepsilon_n\ge f''(x)-\varepsilon_n+\varepsilon_n=f''(x)\ge0,$$
et $|R_n(x)-f''(x)|\le|Q_n(x)-f''(x)|+\varepsilon_n\le2\varepsilon_n$.

**Sens direct, étape 2 : intégrer deux fois.** Posons
$$P_n(x)=f(a)+f'(a)(x-a)+\int_a^x(x-t)R_n(t)\,\mathrm dt.$$
En développant $(x-t)R_n(t)$, $\int_a^x(x-t)R_n(t)\,\mathrm dt=x\int_a^xR_n-\int_a^xtR_n(t)\,\mathrm dt$ est un polynôme en $x$ : $P_n$ est un polynôme. En dérivant (dérivée d'une intégrale de borne variable) : $P_n'(x)=f'(a)+\int_a^xR_n$, puis $P_n''=R_n\ge0$. Donc $P_n$ est convexe sur $[a,b]$.

**Sens direct, étape 3 : convergence uniforme.** La formule de Taylor avec reste intégral à l'ordre 1 donne, pour $f\in C^2$ :
$$f(x)=f(a)+f'(a)(x-a)+\int_a^x(x-t)f''(t)\,\mathrm dt.$$
Par différence, pour $x\in[a,b]$ (avec $x-t\ge0$ sur $[a,x]$) :
$$|P_n(x)-f(x)|=\left|\int_a^x(x-t)\big(R_n(t)-f''(t)\big)\mathrm dt\right|\le2\varepsilon_n\int_a^x(x-t)\,\mathrm dt=\varepsilon_n(x-a)^2\le\varepsilon_n(b-a)^2.$$
Le majorant ne dépend pas de $x$ et tend vers 0 : $P_n\to f$ uniformément sur $[a,b]$.

**Conclusion.** $f$ est convexe si et seulement si elle est limite uniforme sur $[a,b]$ de polynômes convexes sur $[a,b]$.
"""

D['m-ccmp-12a'] = r"""
**1. Existence.** Soit $x\in]0,\frac\pi2]$. On complète le carré :
$$1-2t\cos x+t^2=(t-\cos x)^2+1-\cos^2x=(t-\cos x)^2+\sin^2x\ge\sin^2x>0.$$
Le dénominateur ne s'annule pas sur $[0,1]$ : l'intégrande est continu sur ce segment, l'intégrale $I(x)$ existe.

**1. Primitive.** On utilise $\int\frac{\mathrm dt}{(t-\alpha)^2+\beta^2}=\frac1\beta\arctan\frac{t-\alpha}\beta$ (pour $\beta>0$ ; dérivée : $\frac1\beta\cdot\frac{1/\beta}{1+(t-\alpha)^2/\beta^2}=\frac1{(t-\alpha)^2+\beta^2}$). Avec $\alpha=\cos x$ et $\beta=\sin x>0$ :
$$I(x)=\frac1{\sin x}\left[\arctan\frac{t-\cos x}{\sin x}\right]_0^1=\frac1{\sin x}\left(\arctan\frac{1-\cos x}{\sin x}+\arctan\frac{\cos x}{\sin x}\right),$$
en utilisant l'imparité de $\arctan$ pour la borne $t=0$.

**1. Simplification.** Avec $1-\cos x=2\sin^2\frac x2$ et $\sin x=2\sin\frac x2\cos\frac x2$ : $\frac{1-\cos x}{\sin x}=\tan\frac x2$, et $\frac x2\in]0,\frac\pi4]\subset]-\frac\pi2,\frac\pi2[$, donc $\arctan\big(\tan\frac x2\big)=\frac x2$. De même $\frac{\cos x}{\sin x}=\tan\big(\frac\pi2-x\big)$ avec $\frac\pi2-x\in[0,\frac\pi2[$, donc $\arctan\frac{\cos x}{\sin x}=\frac\pi2-x$. Ainsi
$$I(x)=\frac1{\sin x}\left(\frac x2+\frac\pi2-x\right)=\frac{\pi-x}{2\sin x}.$$

**2. Développement en série.** Posons $c=\cos x\in[0,1[$ et, pour $t\in[0,1]$, $q(t)=\frac{2tc}{1+t^2}$. Comme $2t\le1+t^2$ (équivaut à $(1-t)^2\ge0$) et $0\le c<1$, on a $0\le q(t)\le c<1$. On factorise et on développe la série géométrique :
$$\frac1{1+t^2-2tc}=\frac1{1+t^2}\cdot\frac1{1-q(t)}=\sum_{k\ge0}\frac{q(t)^k}{1+t^2}=\sum_{k\ge0}c^k\,\frac{(2t)^k}{(1+t^2)^{k+1}}.$$

**2. Intégration terme à terme.** Les fonctions $t\mapsto c^k\frac{(2t)^k}{(1+t^2)^{k+1}}$ sont continues et positives sur $[0,1]$, et leur somme est continue : le théorème d'intégration terme à terme pour les séries de fonctions positives donne
$$I(x)=\sum_{k\ge0}c^k\int_0^1\frac{(2t)^k}{(1+t^2)^{k+1}}\,\mathrm dt.$$
(On peut aussi invoquer la convergence normale : le terme général est majoré par $c^k$ sur $[0,1]$.)

**2. Conclusion.** En multipliant par 2 et en utilisant la question 1 :
$$\frac{\pi-x}{\sin x}=2I(x)=\sum_{k\ge0}\alpha_k\cos^kx,\qquad\alpha_k=2\int_0^1\Big(\frac{2t}{1+t^2}\Big)^k\frac{\mathrm dt}{1+t^2}.$$
Pour $t\in[0,1]$, $0\le\frac{2t}{1+t^2}\le1$, donc $\big(\frac{2t}{1+t^2}\big)^{k+1}\le\big(\frac{2t}{1+t^2}\big)^k$ : par croissance de l'intégrale, $0\le\alpha_{k+1}\le\alpha_k$. La suite $(\alpha_k)$ est **positive et décroissante**.

**Vérification.** $\alpha_0=2\int_0^1\frac{\mathrm dt}{1+t^2}=2\cdot\frac\pi4=\frac\pi2$ ; pour $x=\frac\pi2$, $\cos x=0$ et la formule donne $\alpha_0=\frac{\pi-\pi/2}{1}=\frac\pi2$. ✓
"""

D['m-ccmp-12b'] = r"""
**Étape 1 : trigonalisation.** Sur $\mathbb C$, le polynôme caractéristique de $u$ est scindé, donc $u$ est trigonalisable : il existe une base $(e_1,\dots,e_n)$ dans laquelle la matrice $T=(t_{ij})$ de $u$ est triangulaire supérieure, c'est-à-dire
$$u(e_j)=\sum_{i=1}^jt_{ij}e_i\qquad(1\le j\le n).$$

**Étape 2 : changement d'échelle.** Pour $\varepsilon>0$, posons $f_i=\varepsilon^ie_i$. C'est encore une base (on multiplie chaque vecteur par un scalaire non nul). On calcule, par linéarité de $u$ et en écrivant $e_i=\varepsilon^{-i}f_i$ :
$$u(f_j)=\varepsilon^ju(e_j)=\sum_{i=1}^jt_{ij}\,\varepsilon^je_i=\sum_{i=1}^jt_{ij}\,\varepsilon^{j}\varepsilon^{-i}f_i=\sum_{i=1}^j\varepsilon^{j-i}t_{ij}\,f_i.$$
Dans la base $(f_i)$, la matrice $M=(m_{ij})$ de $u$ est donc triangulaire supérieure avec
$$m_{ii}=t_{ii},\qquad m_{ij}=\varepsilon^{j-i}t_{ij}\ (j>i),\qquad m_{ij}=0\ (j<i).$$

**Étape 3 : choix de $\varepsilon$.** Soit $K=\max_{i<j}|t_{ij}|$. Si $K=0$, la matrice $T$ est déjà diagonale et convient. Sinon, prenons $\varepsilon=\min\left(1,\frac\alpha K\right)\in]0,1]$. Pour $j>i$, on a $j-i\ge1$ et $\varepsilon\le1$, donc $\varepsilon^{j-i}\le\varepsilon$, et
$$|m_{ij}|=\varepsilon^{j-i}|t_{ij}|\le\varepsilon K\le\frac\alpha K\cdot K=\alpha.$$
Sous la diagonale, $m_{ij}=0\le\alpha$.

**Conclusion.** Dans la base $(\varepsilon e_1,\varepsilon^2e_2,\dots,\varepsilon^ne_n)$, tous les coefficients non diagonaux de la matrice de $u$ sont de module au plus $\alpha$. (Conséquence classique : les matrices diagonalisables sont denses dans $\mathcal M_n(\mathbb C)$, en perturbant ensuite la diagonale pour rendre les valeurs propres distinctes.)
"""
