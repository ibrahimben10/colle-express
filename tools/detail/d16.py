D = {}

D['m-ccs-15'] = r"""
**Notations.** $w_i=\frac{\alpha_i}\alpha>0$, de sorte que $\sum_iw_i=1$, et $f(x)=\prod_ix_i^{w_i}$.

**1. Régularité.** Sur l'ouvert $(\mathbb R_+^*)^n$, $f(x)=\exp\big(\sum_{i=1}^nw_i\ln x_i\big)$. Chaque $x\mapsto\ln x_i$ est $C^\infty$, la somme aussi, et $\exp$ est $C^\infty$ : par composition, $f$ est $C^\infty$, a fortiori $C^2$.

**2. Dérivées premières.** $\ln f=\sum_kw_k\ln x_k$, donc $\frac{\partial_if}f=\frac{w_i}{x_i}$, soit
$$\partial_if=f\,\frac{w_i}{x_i}.$$

**2. Dérivées secondes.** On dérive ce produit par rapport à $x_j$ ; $\frac{w_i}{x_i}$ ne dépend de $x_j$ que si $j=i$ (dérivée $-\frac{w_i}{x_i^2}$) :
$$\partial_j\partial_if=(\partial_jf)\frac{w_i}{x_i}+f\,\partial_j\Big(\frac{w_i}{x_i}\Big)=f\,\frac{w_iw_j}{x_ix_j}-\delta_{ij}\,f\,\frac{w_i}{x_i^2}=\frac f{x_ix_j}\big(w_iw_j-\delta_{ij}w_i\big).$$

**2. Écriture matricielle.** Avec $D=\mathrm{diag}(x_1,\dots,x_n)$ et $w=(w_1,\dots,w_n)^{\top}$, le coefficient $(i,j)$ de $D^{-1}MD^{-1}$ est $\frac{m_{ij}}{x_ix_j}$. Donc
$$H=f\,D^{-1}\big(ww^{\top}-\mathrm{diag}(w)\big)D^{-1}.$$
Comme $f>0$ et $D^{-1}$ est inversible, multiplier par des matrices inversibles ne change pas le rang : $\mathrm{rg}\,H=\mathrm{rg}\big(\mathrm{diag}(w)-ww^{\top}\big)$.

**2. Factorisation.** Avec $\mathbf 1=(1,\dots,1)^{\top}$, on a $\mathrm{diag}(w)\mathbf 1=w$, donc
$$\mathrm{diag}(w)-ww^{\top}=\mathrm{diag}(w)\big(I_n-\mathbf 1w^{\top}\big),$$
et $\mathrm{diag}(w)$ est inversible ($w_i>0$). Il reste à calculer le rang de $I_n-P$ avec $P=\mathbf 1w^{\top}$.

**2. $P$ est un projecteur de rang 1.** $P^2=\mathbf 1(w^{\top}\mathbf 1)w^{\top}=\big(\sum w_i\big)\mathbf 1w^{\top}=P$, et $P\neq0$ est de rang 1 (toutes ses colonnes sont proportionnelles à $\mathbf 1$). Alors $I_n-P$ est aussi un projecteur ($(I-P)^2=I-2P+P^2=I-P$), et le rang d'un projecteur est égal à sa trace :
$$\mathrm{rg}(I_n-P)=\mathrm{Tr}(I_n)-\mathrm{Tr}(P)=n-w^{\top}\mathbf 1=n-1.$$

**Conclusion.** $\mathrm{rg}\,H(x)=n-1$ en tout point. Interprétation : $f$ est homogène de degré 1 ($f(\lambda x)=\lambda f(x)$), donc $\nabla f(\lambda x)=\nabla f(x)$ ; en dérivant en $\lambda=1$ : $H(x)x=0$. Le noyau est exactement $\mathbb Rx$ (dimension $n-\mathrm{rg}\,H=1$).
"""

D['m-ccs-mi8'] = r"""
**Valeurs initiales.** $M_0=1$ (configuration vide), $M_1=1$, $M_2=2$ (aucune corde, ou la corde entre les deux points).

**2. Décomposition selon le point 1.** On numérote $n+1$ points $1,\dots,n+1$ dans l'ordre du cercle. Deux cas disjoints :
- le point 1 n'est relié à aucun autre : les $n$ autres points forment une configuration quelconque, $M_n$ possibilités ;
- le point 1 est relié au point $k+2$, avec $0\le k\le n-1$. Aucune corde ne peut traverser la corde $\{1,k+2\}$ ni toucher ses extrémités : les $k$ points $2,\dots,k+1$ forment une configuration entre eux ($M_k$ possibilités), et les $n-1-k$ points $k+3,\dots,n+1$ une configuration entre eux ($M_{n-1-k}$ possibilités), indépendamment.

En sommant : $M_{n+1}=M_n+\sum_{k=0}^{n-1}M_kM_{n-1-k}$.

**1. Calcul de $M_5$.** $M_3=M_2+(M_0M_1+M_1M_0)=2+2=4$, $M_4=M_3+(M_0M_2+M_1^2+M_2M_0)=4+5=9$ (comme annoncé), puis
$$M_5=M_4+(M_0M_3+M_1M_2+M_2M_1+M_3M_0)=9+(4+2+2+4)=21.$$

**3. Majoration $M_n\le3^n$ par un codage.** À une configuration, associons le mot de longueur $n$ dont la $i$-ème lettre vaut $L$ si le point $i$ est libre, $O$ s'il est relié à un point d'indice plus grand, $F$ s'il est relié à un point d'indice plus petit. Ce codage est injectif : comme les cordes ne se croisent pas, chaque $F$ est relié au dernier $O$ encore « ouvert » avant lui (comme une parenthèse fermante avec son ouvrante), ce qui permet de reconstruire toutes les cordes. Il y a $3^n$ mots, donc $M_n\le3^n$. Ainsi, pour $|x|<\frac13$, $|M_nx^n|\le(3|x|)^n$ : la série converge, et $R\ge\frac13$.

**4. Équation fonctionnelle.** Pour $|x|<\frac13$, multiplions la récurrence par $x^{n+1}$ et sommons sur $n\ge0$ :
$$\sum_{n\ge0}M_{n+1}x^{n+1}=x\sum_{n\ge0}M_nx^n+x\sum_{n\ge1}\Big(\sum_{k=0}^{n-1}M_kM_{n-1-k}\Big)x^n.$$
Le membre de gauche vaut $G(x)-1$. Dans le dernier terme, posons $m=n-1$ : $\sum_{m\ge0}\big(\sum_{k=0}^mM_kM_{m-k}\big)x^{m+1}=x\,G(x)^2$ (produit de Cauchy, licite à l'intérieur du disque de convergence). Donc
$$G(x)=1+xG(x)+x^2G(x)^2.$$

**4. Résolution.** Pour $x\neq0$, $G$ est racine de $x^2Y^2+(x-1)Y+1=0$, de discriminant $(1-x)^2-4x^2=1-2x-3x^2=(1-3x)(1+x)$, positif pour $|x|<\frac13$. Donc $G(x)=\frac{1-x\pm\sqrt{(1-3x)(1+x)}}{2x^2}$. Quand $x\to0$, $1-x+\sqrt{\cdots}\to2$ et la fraction avec $+$ tend vers l'infini ; or $G$ est continue en 0 avec $G(0)=1$. Comme le signe ne peut changer sans que les deux racines se rejoignent (discriminant non nul), c'est le signe $-$ :
$$G(x)=\frac{1-x-\sqrt{1-2x-3x^2}}{2x^2}.$$
Vérification : $\sqrt{1-2x-3x^2}=1-x-2x^2-2x^3+O(x^4)$, d'où $G(x)=1+x+2x^2+\dots$ ✓.

**Rayon exact.** Si l'on avait $R>\frac13$, $G$ serait dérivable en $\frac13$, donc $G'$ bornée au voisinage de $\frac13$ ; mais la dérivée de $\sqrt{(1-3x)(1+x)}$ tend vers l'infini quand $x\to\frac13^-$. Donc $R=\frac13$. Ce sont les nombres de Motzkin $1,1,2,4,9,21,51,\dots$
"""

D['x-g-1'] = r"""
**Ordres possibles.** Par le théorème de Lagrange, l'ordre de tout élément divise $|G|=pq$ : il vaut $1$, $p$, $q$ ou $pq$. Si un élément est d'ordre $pq$, il engendre $G$, qui est cyclique. On montre qu'un tel élément existe toujours.

**Lemme.** Si tout $x\in G$ vérifie $x^p=e$, alors $|G|$ est une puissance de $p$. En effet, notons $G$ additivement. Pour $\bar k\in\mathbb Z/p\mathbb Z$ et $x\in G$, posons $\bar k\cdot x=kx$ : c'est bien défini car $px=0$ (deux représentants de $\bar k$ diffèrent d'un multiple de $p$). Comme $G$ est abélien, on vérifie les axiomes : $\bar k\cdot(x+y)=kx+ky$, $(\bar k+\bar l)\cdot x=kx+lx$, $\bar k\cdot(\bar l\cdot x)=(kl)x$, $\bar1\cdot x=x$. Ainsi $G$ est un $\mathbb Z/p\mathbb Z$-espace vectoriel ; il est fini, donc de dimension finie $d$, et $|G|=p^d$.

**Existence d'un élément d'ordre $q$ ou $pq$.** Sinon, tous les éléments sont d'ordre 1 ou $p$, donc $x^p=e$ pour tout $x$, et $|G|=p^d$ d'après le lemme. Mais $q$ divise $|G|=pq$ et $q$ est un premier différent de $p$ : impossible. Si l'élément trouvé est d'ordre $pq$, c'est terminé. Sinon on dispose de $a$ d'ordre $q$.

**Existence d'un élément d'ordre $p$.** Même raisonnement en échangeant $p$ et $q$ : on obtient $b$ d'ordre $p$ (ou directement un élément d'ordre $pq$).

**L'élément $ab$ est d'ordre $pq$.** Comme $G$ est abélien, $(ab)^k=a^kb^k$. Supposons $(ab)^k=e$. Alors $a^k=b^{-k}$ appartient à $\langle a\rangle\cap\langle b\rangle$. Ce sous-groupe est contenu dans $\langle a\rangle$ (d'ordre $q$) et dans $\langle b\rangle$ (d'ordre $p$) : son ordre divise $p$ et $q$, donc vaut 1. Ainsi $a^k=e$ et $b^k=e$, donc $q\mid k$ et $p\mid k$, et comme $p\wedge q=1$, $pq\mid k$. Réciproquement $(ab)^{pq}=(a^q)^p(b^p)^q=e$. Donc $ab$ est d'ordre exactement $pq$.

**Conclusion.** $G=\langle ab\rangle$ est cyclique : $G\simeq\mathbb Z/pq\mathbb Z\simeq\mathbb Z/p\mathbb Z\times\mathbb Z/q\mathbb Z$ (lemme chinois).
"""

D['x-g-2'] = r"""
**Ordres possibles.** Par Lagrange, l'ordre de tout élément divise $2p$ : il vaut $1$, $2$, $p$ ou $2p$.

**Cas où il existe un élément d'ordre $2p$.** Si $x$ est d'ordre $2p$, alors $(x^2)^p=x^{2p}=e$ et, pour $1\le k<p$, $(x^2)^k=x^{2k}\neq e$ car $0<2k<2p$. Donc $x^2$ est d'ordre exactement $p$.

**Cas où il n'existe aucun élément d'ordre $p$ (raisonnement par l'absurde).** Alors il n'en existe pas non plus d'ordre $2p$ (cas précédent), donc tout élément est d'ordre 1 ou 2 : $x^2=e$, soit $x^{-1}=x$, pour tout $x$.
- $G$ est alors abélien : pour $x,y\in G$, $xy=(xy)^{-1}=y^{-1}x^{-1}=yx$.
- Noté additivement, $G$ vérifie $2x=0$ pour tout $x$ : c'est un espace vectoriel sur $\mathbb Z/2\mathbb Z$ (même vérification que pour $\mathbb Z/p\mathbb Z$), fini donc de dimension finie $d$, et $|G|=2^d$.

On obtient $2p=2^d$, soit $p=2^{d-1}$ ; $p$ étant premier, $p=2$.

**Le cas $p=2$.** Ici $|G|=4$ et on cherche un élément d'ordre $p=2$. Soit $x\neq e$ : son ordre est 2 ou 4. S'il vaut 2, c'est fini ; s'il vaut 4, $x^2$ est d'ordre 2.

**Conclusion.** Dans tous les cas, $G$ contient un élément d'ordre $p$. C'est un cas particulier du lemme de Cauchy (si un premier $p$ divise $|G|$, $G$ a un élément d'ordre $p$). Exemples : $\mathbb Z/2p\mathbb Z$ (élément $\bar2$) et le groupe diédral $D_p$ des isométries du polygone régulier à $p$ côtés (rotation d'angle $\frac{2\pi}p$).
"""
