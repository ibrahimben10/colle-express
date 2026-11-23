D = {}

D['m-ccmp-20b'] = r"""
**1. Les valeurs propres sont racines simples de $P$.** Soit $\lambda$ une valeur propre de $A$ et $X\neq0$ avec $AX=\lambda X$. Par récurrence $A^kX=\lambda^kX$, donc par linéarité $Q(A)X=Q(\lambda)X$ pour tout polynôme $Q$.
- Avec $Q=P$ : $0=P(A)X=P(\lambda)X$, et $X\neq0$, donc $P(\lambda)=0$.
- Avec $Q=P'$ : $P'(A)X=P'(\lambda)X$. Si $P'(\lambda)=0$, alors $X\in\ker P'(A)$, ce qui contredit l'inversibilité de $P'(A)$. Donc $P'(\lambda)\neq0$.

$\lambda$ est racine de $P$ sans être racine de $P'$ : c'est une racine **simple** de $P$.

**1. Conclusion par le polynôme minimal.** Le polynôme minimal $\mu_A$ divise tout polynôme annulateur, donc $\mu_A\mid P$ ; ses racines sont exactement les valeurs propres de $A$. Si $\lambda$ était racine double de $\mu_A$, $(X-\lambda)^2$ diviserait $\mu_A$ donc $P$, et $\lambda$ serait racine au moins double de $P$ : contradiction. Sur $\mathbb C$, $\mu_A$ est scindé ; il est donc scindé à racines simples, et $A$ est diagonalisable.

**2. La réciproque est fausse pour un annulateur quelconque.** $A=I_n$ est diagonalisable et annulée par $P=(X-1)^2$. Mais $P'=2(X-1)$ et $P'(A)=2(I_n-I_n)=0$, qui n'est pas inversible.

**2. Elle est vraie pour $P=\mu_A$.** Si $A$ est diagonalisable, $A=Q\,\mathrm{diag}(\lambda_1,\dots,\lambda_n)\,Q^{-1}$ et $\mu_A=\prod_{\lambda\in\mathrm{Sp}\,A}(X-\lambda)$ (valeurs propres distinctes), à racines simples. Chaque valeur propre $\lambda_i$ est racine simple de $\mu_A$, donc $\mu_A'(\lambda_i)\neq0$. Alors
$$\mu_A'(A)=Q\,\mathrm{diag}\big(\mu_A'(\lambda_1),\dots,\mu_A'(\lambda_n)\big)\,Q^{-1}$$
a un déterminant $\prod\mu_A'(\lambda_i)\neq0$ : il est inversible.

**Bilan.** $P'(A)$ inversible $\Rightarrow$ $A$ diagonalisable, pour tout annulateur $P$. La réciproque est vraie si $P=\mu_A$ (ou plus généralement si $P$ est à racines simples), fausse en général.
"""

D['m-ccmp-21b'] = r"""
**Notation.** $d=\|c_1-c_2\|$.

**1. Condition nécessaire.** Si $x$ est dans les deux boules : $\|x-c_1\|\le r_1$ et $\|x-c_2\|\le r_2$, donc par l'inégalité triangulaire $d\le\|c_1-x\|+\|x-c_2\|\le r_1+r_2$.

**1. Condition suffisante.** Supposons $d\le r_1+r_2$.
- Si $r_1+r_2=0$ : alors $d=0$, $c_1=c_2$ et ce point est dans les deux boules.
- Sinon, posons $x=c_1+\frac{r_1}{r_1+r_2}(c_2-c_1)$, point du segment $[c_1,c_2]$. On calcule
$$\|x-c_1\|=\frac{r_1}{r_1+r_2}d\le r_1,\qquad\|x-c_2\|=\Big\|\Big(\frac{r_1}{r_1+r_2}-1\Big)(c_2-c_1)\Big\|=\frac{r_2}{r_1+r_2}d\le r_2,$$
en utilisant $\frac d{r_1+r_2}\le1$. Donc $x$ est dans les deux boules.

**CNS pour les boules : $d\le r_1+r_2$.**

**2. Condition nécessaire.** Si $\|x-c_1\|=r_1$ et $\|x-c_2\|=r_2$ : $d\le r_1+r_2$ (inégalité triangulaire), et $r_1=\|x-c_1\|\le\|x-c_2\|+\|c_2-c_1\|=r_2+d$, de même $r_2\le r_1+d$. Donc $|r_1-r_2|\le d\le r_1+r_2$.

**2. Condition suffisante, cas $d=0$.** Alors $|r_1-r_2|\le0$ impose $r_1=r_2$ : les deux sphères sont égales, et non vides (car $n\ge1$).

**2. Condition suffisante, cas $d>0$.** Posons $u=\frac{c_2-c_1}d$ (unitaire) et choisissons $v$ unitaire orthogonal à $u$ (possible car $\dim E\ge2$). On cherche $x=c_1+\alpha u+\beta v$. Par Pythagore ($u\perp v$), et avec $c_2=c_1+du$ :
$$\|x-c_1\|^2=\alpha^2+\beta^2,\qquad\|x-c_2\|^2=(\alpha-d)^2+\beta^2.$$
On veut $\alpha^2+\beta^2=r_1^2$ et $(\alpha-d)^2+\beta^2=r_2^2$. En soustrayant : $\alpha^2-(\alpha-d)^2=r_1^2-r_2^2$, soit $2\alpha d-d^2=r_1^2-r_2^2$ :
$$\alpha=\frac{d^2+r_1^2-r_2^2}{2d}.$$
Il reste à trouver $\beta$ réel avec $\beta^2=r_1^2-\alpha^2$ : c'est possible si et seulement si $\alpha^2\le r_1^2$, c'est-à-dire $|d^2+r_1^2-r_2^2|\le2dr_1$, soit
$$-2dr_1\le d^2+r_1^2-r_2^2\le2dr_1\iff(d-r_1)^2\le r_2^2\le(d+r_1)^2\iff|d-r_1|\le r_2\le d+r_1.$$
Or $|d-r_1|\le r_2$ équivaut à ($d\le r_1+r_2$ et $r_1-r_2\le d$), et $r_2\le d+r_1$ équivaut à $r_2-r_1\le d$. L'ensemble équivaut donc exactement à l'hypothèse $|r_1-r_2|\le d\le r_1+r_2$. On prend alors $\beta=\sqrt{r_1^2-\alpha^2}$, et $x$ est sur les deux sphères.

**CNS pour les sphères : $|r_1-r_2|\le d\le r_1+r_2$.** (En dimension 1, l'argument échoue : deux « sphères » de $\mathbb R$ sont des paires de points, et la condition n'est plus suffisante.)
"""

D['m-ccmp-24b'] = r"""
**Étape 1 : trace du carré d'une nilpotente.** Soit $N\in F$. $N$ est nilpotente, donc $N^2$ aussi ; sur $\mathbb C$, $N^2$ est trigonalisable avec des valeurs propres toutes nulles (si $N^2X=\lambda X$ et $N^{2k}=0$, alors $\lambda^kX=0$, donc $\lambda=0$). La trace étant la somme des valeurs propres : $\mathrm{Tr}(N^2)=0$.

**Étape 2 : trace du carré d'une symétrique.** Soit $S\in\mathcal S_n(\mathbb R)$. Comme $S^{\top}=S$ :
$$\mathrm{Tr}(S^2)=\mathrm{Tr}(S^{\top}S)=\sum_{j}(S^{\top}S)_{jj}=\sum_j\sum_is_{ij}^2,$$
qui est strictement positif si $S\neq0$.

**Étape 3 : $F\cap\mathcal S_n(\mathbb R)=\{0\}$.** Une matrice $S$ dans l'intersection vérifie $\mathrm{Tr}(S^2)=0$ (étape 1) et, si $S\neq0$, $\mathrm{Tr}(S^2)>0$ (étape 2). Donc $S=0$.

**Étape 4 : dimension.** $F$ et $\mathcal S_n(\mathbb R)$ sont en somme directe dans $\mathcal M_n(\mathbb R)$ :
$$\dim F+\dim\mathcal S_n(\mathbb R)=\dim\big(F\oplus\mathcal S_n(\mathbb R)\big)\le n^2.$$
Une matrice symétrique est déterminée par ses coefficients sur et au-dessus de la diagonale : $\dim\mathcal S_n(\mathbb R)=n+\frac{n(n-1)}2=\frac{n(n+1)}2$. Donc
$$\dim F\le n^2-\frac{n(n+1)}2=\frac{n(n-1)}2.$$

**Cas d'égalité.** Soit $\mathcal T$ l'ensemble des matrices triangulaires supérieures strictes. C'est un sous-espace de dimension $\frac{n(n-1)}2$ (coefficients libres strictement au-dessus de la diagonale). Ses éléments sont nilpotents : si $T\in\mathcal T$, $Te_1=0$ et $Te_j\in\mathrm{Vect}(e_1,\dots,e_{j-1})$, donc par récurrence $T^je_j=0$ et $T^n=0$. L'égalité est atteinte.

**Remarque.** $F$ n'est pas supposé stable par produit : seule la nilpotence de chaque élément compte. C'est le théorème de Gerstenhaber, vrai sur tout corps ; l'astuce de la trace utilise ici le corps $\mathbb R$.
"""

D['m-ccmp-25a'] = r"""
**1. Contrôle de $f$ aux bords.** Pour $f\in E$ et $t\in[0,1]$, l'inégalité des accroissements finis donne $|f(t)|=|f(t)-f(0)|\le\|f'\|_\infty\,t$ et $|f(t)|=|f(t)-f(1)|\le\|f'\|_\infty(1-t)$. Donc
$$|f(t)|\le M\min(t,1-t),\qquad M=\|f'\|_\infty.$$

**1. Contrôle du sinus.** La fonction $\sin$ est concave sur $[0,\pi]$, donc au-dessus de ses cordes : pour $t\in[0,\frac12]$, $\sin(\pi t)\ge2t$ (corde entre $0$ et $\frac\pi2$), et par symétrie $\sin(\pi t)\ge2\min(t,1-t)$ sur $[0,1]$.

**1. Existence de $I_2$.** Par l'identité $1+\tan^2=\frac1{\cos^2}$, on a $\frac{1+\tan^2(\pi t)}{\tan^2(\pi t)}=\frac{1/\cos^2}{\sin^2/\cos^2}=\frac1{\sin^2(\pi t)}$. Donc $I_2=\int_0^1\frac{f(t)^2}{\sin^2(\pi t)}\mathrm dt$ et, sur $]0,1[$,
$$0\le\frac{f(t)^2}{\sin^2(\pi t)}\le\frac{M^2\min(t,1-t)^2}{4\min(t,1-t)^2}=\frac{M^2}4.$$
L'intégrande est continu et borné sur $]0,1[$ : $I_2$ converge.

**1. Existence de $I_1$.** $|\cot(\pi t)|=\frac{|\cos(\pi t)|}{\sin(\pi t)}\le\frac1{2\min(t,1-t)}$, donc $|f(t)f'(t)\cot(\pi t)|\le M\cdot M\min(t,1-t)\cdot\frac1{2\min(t,1-t)}=\frac{M^2}2$ : intégrande borné, $I_1$ converge.

**1. Comparaison par intégration par parties.** Sur $[\varepsilon,1-\varepsilon]$, avec $u=\frac{f^2}2$ ($u'=ff'$) et $v=\cot(\pi t)$ ($v'=-\frac\pi{\sin^2(\pi t)}$) :
$$\int_\varepsilon^{1-\varepsilon}ff'\cot(\pi t)\,\mathrm dt=\Big[\frac{f^2}2\cot(\pi t)\Big]_\varepsilon^{1-\varepsilon}+\frac\pi2\int_\varepsilon^{1-\varepsilon}\frac{f^2}{\sin^2(\pi t)}\,\mathrm dt.$$
Le crochet tend vers 0 : $\big|\frac{f(\varepsilon)^2}2\cot(\pi\varepsilon)\big|\le\frac{M^2\varepsilon^2}2\cdot\frac1{2\varepsilon}\to0$ (de même en $1-\varepsilon$). En faisant $\varepsilon\to0$ :
$$I_1=\frac\pi2\,I_2.$$

**2. Développement d'un carré.** La fonction $\big(f'-\pi f\cot(\pi t)\big)^2$ est continue, positive, et intégrable (somme de termes intégrables : $f'^2$, $ff'\cot$ et $f^2\cot^2\le\frac{f^2}{\sin^2}$). En développant :
$$0\le\int_0^1\big(f'-\pi f\cot(\pi t)\big)^2=\int_0^1f'^2-2\pi I_1+\pi^2\int_0^1f^2\cot^2(\pi t)\,\mathrm dt.$$
Avec $\cot^2=\frac1{\sin^2}-1$ : $\int_0^1f^2\cot^2(\pi t)=I_2-\int_0^1f^2$. Et $2\pi I_1=\pi^2I_2$. Donc
$$0\le\int_0^1f'^2-\pi^2I_2+\pi^2I_2-\pi^2\int_0^1f^2=\int_0^1f'^2-\pi^2\int_0^1f^2.$$
C'est l'**inégalité de Wirtinger** : $\int_0^1f'^2\ge\pi^2\int_0^1f^2$.

**3. Cas d'égalité.** Il y a égalité si et seulement si $\int_0^1\big(f'-\pi f\cot(\pi t)\big)^2=0$, c'est-à-dire (fonction continue positive d'intégrale nulle sur $]0,1[$) $f'(t)=\pi\cot(\pi t)f(t)$ pour tout $t\in]0,1[$. Sur $]0,1[$, $\sin(\pi t)>0$ et
$$\Big(\frac{f(t)}{\sin(\pi t)}\Big)'=\frac{f'(t)\sin(\pi t)-\pi\cos(\pi t)f(t)}{\sin^2(\pi t)}=\frac{f'(t)-\pi\cot(\pi t)f(t)}{\sin(\pi t)}=0.$$
Donc $f=\lambda\sin(\pi t)$ sur $]0,1[$, puis sur $[0,1]$ par continuité. Réciproquement, pour $f=\lambda\sin(\pi t)$ : $\int_0^1f'^2=\lambda^2\pi^2\int_0^1\cos^2(\pi t)=\frac{\lambda^2\pi^2}2=\pi^2\int_0^1f^2$. ✓

**Conclusion.** Égalité si et seulement si $f=\lambda\sin(\pi t)$, $\lambda\in\mathbb R$.
"""
