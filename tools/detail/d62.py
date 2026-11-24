# Conversion « 6 étapes » — lot 2 : maths CCINP (vérifications : quadrature, mpmath, sympy, tirages aléatoires).
D = {}

D['m-ccmp-15b'] = r"""**Étape 1 — Analyse de l'énoncé.** $A\subset\mathbb R^n$ est convexe et $a\in A$. Par définition, $a$ est **extrémal** si $A\setminus\{a\}$ est convexe. Il faut montrer l'équivalence avec la propriété
$$(\mathcal P)\qquad\forall x,y\in A,\quad a=\tfrac12(x+y)\Rightarrow x=y=a,$$
autrement dit : $a$ n'est le milieu d'aucun segment de $A$ non réduit à un point.

**Étape 2 — Rappels du cours.**

> **Définition — Convexité.** $C$ est convexe si, pour tous $x,y\in C$ et $t\in[0,1]$, $(1-t)x+ty\in C$. Le segment $[x,y]$ est l'ensemble de ces points.

> **Propriété — Combinaisons convexes.** Si $x,y\in C$ convexe et $s\in[0,1]$, le point $(1-s)x+sy$ appartient à $C$. En particulier, un point de la forme $(1-2t)x+2ty$ avec $2t\in[0,1]$ est dans $[x,y]$.

> **Principe — Contraposée.** Pour montrer $(\mathcal P)\Rightarrow$ « $a$ extrémal », il est équivalent de montrer « $a$ non extrémal » $\Rightarrow$ non $(\mathcal P)$.

**Étape 3 — Stratégie.** Sens direct : par l'absurde, un milieu $a$ de deux points distincts de $a$ contredirait la convexité de $A\setminus\{a\}$. Réciproque : par contraposée. Si $A\setminus\{a\}$ n'est pas convexe, $a$ est un point intérieur d'un segment $[x,y]$ de $A$, mais pas forcément le milieu. On le « recentre » en remplaçant l'extrémité $y$ par le symétrique $y'=2a-x$, qui reste sur le segment si $a$ est plus près de $x$.

**Étape 4 — Résolution détaillée.**

**4.1 Sens direct.** Supposons $A\setminus\{a\}$ convexe, et soient $x,y\in A$ avec $a=\frac12(x+y)$. Par l'absurde, supposons $x\neq a$. Alors $y=2a-x\neq a$. Donc $x,y\in A\setminus\{a\}$, qui est convexe, et leur milieu $\frac12(x+y)=a$ appartient à $A\setminus\{a\}$ : contradiction. Donc $x=a$, puis $y=2a-x=a$.

**4.2 Réciproque : un segment qui passe par $a$.** Supposons $A\setminus\{a\}$ non convexe. Il existe $x,y\in A\setminus\{a\}$ et $t\in[0,1]$ tels que $z=(1-t)x+ty\notin A\setminus\{a\}$. Comme $A$ est convexe, $z\in A$, donc $z=a$. De plus $t\neq0$ et $t\neq1$, sinon $z=x$ ou $z=y$, qui sont différents de $a$. Ainsi $t\in]0,1[$ et
$$a=(1-t)x+ty,\qquad x\neq a,\ y\neq a.$$

**4.3 Recentrage.** Quitte à échanger $x$ et $y$ (ce qui change $t$ en $1-t$), on suppose $t\le\frac12$. On pose $y'=2a-x$. Alors
$$y'=2\big((1-t)x+ty\big)-x=(1-2t)x+2t\,y,\qquad 2t\in\,]0,1].$$
Donc $y'\in[x,y]\subset A$ (combinaison convexe). Par construction, $a=\frac12(x+y')$ avec $x,y'\in A$ et $x\neq a$ : la propriété $(\mathcal P)$ est fausse.

**Étape 5 — Vérification.**

> **Vérification — Exemples.**
> - Pour le disque fermé de $\mathbb R^2$, les points extrémaux sont ceux du cercle. Un point intérieur est le milieu d'une petite corde. Un point du cercle n'est le milieu d'aucune corde : c'est la stricte convexité de la norme euclidienne.
> - Pour le carré $[0,1]^2$, seuls les 4 sommets sont extrémaux. Le milieu d'un côté est le milieu de deux sommets.

- La convexité de $A$ sert en 4.2, pour affirmer $z\in A$. Sans elle, l'énoncé n'aurait d'ailleurs pas de sens.
- Le cas $t=\frac12$ redonne directement $y'=y$ : le recentrage ne change rien quand $a$ est déjà le milieu.

**Étape 6 — Conclusion.**
$$\boxed{a\ \text{extrémal}\iff\Big(\forall x,y\in A,\ a=\tfrac12(x+y)\Rightarrow x=y=a\Big)}$$
Autrement dit, $a$ est extrémal si et seulement s'il n'est le milieu d'aucun segment non trivial de $A$.
===RÉPONSE===
Sens direct par l'absurde ; réciproque par contraposée, en remplaçant une extrémité par le symétrique $2a-x$, qui reste sur le segment."""

D['m-ccmp-19b'] = r"""**Étape 1 — Analyse de l'énoncé.** On pose $f(x)=\displaystyle\int_1^{+\infty}\frac{\mathrm dt}{t\sqrt{1+tx}}$. C'est une intégrale impropre en $+\infty$, dont l'intégrande n'est défini que si $1+tx\ge0$ pour tout $t\ge1$.
1. Il faut trouver l'ensemble des $x$ pour lesquels l'intégrale existe.
2. Il faut calculer $f(x)$ explicitement.

**Étape 2 — Rappels du cours.**

> **Théorème — Comparaison (fonctions positives).** Si $0\le h(t)\sim g(t)$ en $+\infty$, alors $\int^{+\infty}h$ et $\int^{+\infty}g$ sont de même nature. De plus, $\int_1^{+\infty}\frac{\mathrm dt}{t^\alpha}$ converge si et seulement si $\alpha>1$.

> **Théorème — Changement de variable (intégrale impropre).** Si $\varphi$ est une bijection $C^1$ strictement croissante de $[\alpha,\beta[$ sur $[a,b[$, alors $\int_a^bf(t)\,\mathrm dt$ et $\int_\alpha^\beta f(\varphi(u))\varphi'(u)\,\mathrm du$ sont de même nature et égales en cas de convergence.

> **Formule — Éléments simples.** $\dfrac2{u^2-1}=\dfrac1{u-1}-\dfrac1{u+1}$.

**Étape 3 — Stratégie.** On écarte d'abord les $x\le0$ : racine non définie, ou divergence. Pour $x>0$, un équivalent en $+\infty$ donne la convergence. Le calcul se fait en posant $u=\sqrt{1+tx}$, ce qui rend l'intégrande rationnel. On décompose en éléments simples, puis on simplifie le résultat.

**Étape 4 — Résolution détaillée.**

**4.1 Cas $x<0$.** Pour $t>-\frac1x$, on a $1+tx<0$ : l'intégrande n'est pas défini sur tout $[1,+\infty[$. Ces valeurs sont exclues.

**4.2 Cas $x=0$.** $\int_1^X\frac{\mathrm dt}t=\ln X\to+\infty$ : l'intégrale diverge.

**4.3 Cas $x>0$.** L'intégrande $h$ est continu et positif sur $[1,+\infty[$. En $+\infty$, $\sqrt{1+tx}=\sqrt{tx}\sqrt{1+\frac1{tx}}\sim\sqrt x\sqrt t$, donc $h(t)\sim\dfrac1{\sqrt x\,t^{3/2}}$. Comme $\frac32>1$, l'intégrale converge. Donc $\mathcal D_f=]0,+\infty[$.

**4.4 Changement de variable.** Pour $x>0$, $t\mapsto u=\sqrt{1+tx}$ est une bijection $C^1$ strictement croissante de $[1,+\infty[$ sur $[\sqrt{1+x},+\infty[$. On a $t=\frac{u^2-1}x$ et $\mathrm dt=\frac{2u}x\,\mathrm du$, donc
$$\frac{\mathrm dt}{t\sqrt{1+tx}}=\frac{\frac{2u}x}{\frac{u^2-1}x\,u}\,\mathrm du=\frac{2\,\mathrm du}{u^2-1}.$$

**4.5 Primitive et calcul.** Pour $u>1$, une primitive de $\frac2{u^2-1}$ est $\ln\frac{u-1}{u+1}$, qui tend vers $\ln1=0$ en $+\infty$. Donc
$$f(x)=0-\ln\frac{\sqrt{1+x}-1}{\sqrt{1+x}+1}=\ln\frac{\sqrt{1+x}+1}{\sqrt{1+x}-1}.$$

**4.6 Simplification.** Comme $(\sqrt{1+x}-1)(\sqrt{1+x}+1)=x$, on a $\frac{\sqrt{1+x}+1}{\sqrt{1+x}-1}=\frac{(1+\sqrt{1+x})^2}x$, d'où $f(x)=2\ln\dfrac{1+\sqrt{1+x}}{\sqrt x}$.

**Étape 5 — Vérification.**

> **Contrôle numérique.** Par quadrature : $f(0{,}5)=2{,}292432$, $f(2)=1{,}316958$, $f(10)=0{,}622363$. La formule donne les mêmes valeurs, à $10^{-12}$ près.

- En $0^+$ : $f(x)\sim2\ln\frac2{\sqrt x}\to+\infty$, ce qui est cohérent avec la divergence en $x=0$.
- En $+\infty$ : $f(x)\sim\frac2{\sqrt x}$. C'est cohérent avec la majoration $f(x)\le\int_1^{+\infty}\frac{\mathrm dt}{\sqrt x\,t^{3/2}}=\frac2{\sqrt x}$, obtenue avec $\sqrt{1+tx}\ge\sqrt{tx}$.
- Monotonie : $f$ est décroissante, comme attendu, car l'intégrande décroît quand $x$ augmente.

**Étape 6 — Conclusion.**
$$\boxed{\mathcal D_f=\,]0,+\infty[\qquad\text{et}\qquad\forall x>0,\ f(x)=2\ln\frac{1+\sqrt{1+x}}{\sqrt x}}$$
===RÉPONSE===
$\mathcal D_f=]0,+\infty[$ et $f(x)=2\ln\frac{1+\sqrt{1+x}}{\sqrt x}$."""

D['m-ccmp-20a'] = r"""**Étape 1 — Analyse de l'énoncé.** Pour $x>0$, on pose $g(x)=\sum_{n\ge1}u_n(x)$ avec $u_n(x)=\dfrac{(-1)^{n-1}}{n^x}$.
1. Il faut montrer que $g$ est définie et de classe $C^\infty$ sur $]0,+\infty[$. La série ne converge pas absolument pour $x\le1$ : il faudra exploiter l'alternance.
2. Il faut calculer $\lim_{x\to0^+}g(x)$. En $x=0$, la série $\sum(-1)^{n-1}$ diverge : la limite ne peut pas s'obtenir par simple continuité.

**Étape 2 — Rappels du cours.**

> **Théorème — Critère spécial des séries alternées.** Si $(a_n)$ est positive, décroissante et de limite nulle, alors $\sum(-1)^{n-1}a_n$ converge. Sa somme est comprise entre $0$ et $a_1$, et le reste vérifie $\big|\sum_{n>N}(-1)^{n-1}a_n\big|\le a_{N+1}$.

> **Théorème — Dérivation terme à terme.** Si les $u_n$ sont $C^k$ sur un intervalle $J$, si $\sum u_n^{(j)}$ converge simplement sur $J$ pour $j<k$, et si $\sum u_n^{(k)}$ converge **uniformément** sur $J$, alors $\sum u_n$ est $C^k$ sur $J$, dérivable terme à terme.

> **Propriété — Caractère local.** Une fonction de classe $C^\infty$ sur tout $[a,+\infty[$ avec $a>0$ est $C^\infty$ sur $]0,+\infty[$.

**Étape 3 — Stratégie.** Les dérivées $u_n^{(k)}$ forment encore des séries alternées. On montre que leurs termes décroissent à partir d'un rang **indépendant de $x$** sur $[a,+\infty[$. La majoration du reste donne alors la convergence uniforme. Pour la limite, on regroupe les termes deux à deux : $2g(x)=1+h(x)$, où $h$ est une autre série alternée dont le premier terme tend vers $0$.

**Étape 4 — Résolution détaillée.**

**4.1 Définition.** Pour $x>0$, $a_n=n^{-x}$ est positive, décroissante et tend vers $0$ : $g(x)$ est défini par le critère spécial.

**4.2 Dérivées des termes.** $u_n(x)=(-1)^{n-1}e^{-x\ln n}$ est $C^\infty$, et
$$u_n^{(k)}(x)=(-1)^{n-1+k}(\ln n)^kn^{-x}.$$
Chaque série dérivée est alternée, de terme $b_n(x)=(\ln n)^kn^{-x}$ en valeur absolue.

**4.3 Décroissance à partir d'un rang uniforme.** Fixons $a>0$ et $k\ge1$, et posons $\varphi(t)=(\ln t)^kt^{-x}$. Alors
$$\varphi'(t)=t^{-x-1}(\ln t)^{k-1}\big(k-x\ln t\big).$$
Pour $x\ge a$ et $t\ge e^{k/a}$, on a $x\ln t\ge k$, donc $\varphi'(t)\le0$. Ainsi, pour $n\ge N_0=\lceil e^{k/a}\rceil$, la suite $(b_n(x))$ décroît **pour tout** $x\ge a$, et elle tend vers $0$ par croissances comparées.

**4.4 Convergence uniforme.** Pour $N\ge N_0$ et $x\ge a$, le critère spécial donne
$$\Big|\sum_{n>N}u_n^{(k)}(x)\Big|\le b_{N+1}(x)\le\frac{(\ln(N+1))^k}{(N+1)^a}\xrightarrow[N\to\infty]{}0.$$
Le majorant ne dépend pas de $x$ : la convergence est uniforme sur $[a,+\infty[$, pour tout $k$. Le théorème de dérivation montre que $g$ est $C^\infty$ sur $[a,+\infty[$, donc sur $]0,+\infty[$.

**4.5 Regroupement.** Avec $a_n=n^{-x}$ et le décalage $m=n+1$ (licite, car les deux séries convergent) :
$$\sum_{n\ge1}(-1)^{n-1}(a_n-a_{n+1})=g(x)+\big(g(x)-a_1\big),\qquad\text{donc}\qquad2g(x)=1+h(x),$$
avec $h(x)=\sum_{n\ge1}(-1)^{n-1}d_n$ et $d_n=n^{-x}-(n+1)^{-x}$.

**4.6 Majoration de $h$.** On a $d_n=x\int_n^{n+1}t^{-x-1}\,\mathrm dt\ge0$, et $d_{n+1}=x\int_n^{n+1}(t+1)^{-x-1}\,\mathrm dt\le d_n$. De plus $d_n\to0$. Par le critère spécial, $0\le h(x)\le d_1=1-2^{-x}$, qui tend vers $0$ quand $x\to0^+$. Donc $g(x)=\frac{1+h(x)}2\to\frac12$.

**Étape 5 — Vérification.**

> **Contrôle numérique.** $g(1)=\ln2=0{,}693147\ldots$ (série harmonique alternée). $g(0{,}1)=0{,}5223$, $g(0{,}01)=0{,}50225$ et $g(0{,}001)=0{,}500226$ : la limite $\frac12$ est confirmée.

- Encadrement : $\frac12\le g(x)\le1-2^{-x-1}$ d'après 4.6, ce qui est compatible avec $g(1)=\ln2\in[0{,}5\,;0{,}75]$.
- La valeur $\frac12$ est la « somme d'Abel » de la série divergente $1-1+1-\cdots$. L'énoncé demande une limite, pas une valeur en $0$, qui n'existe pas.
- Le rang $N_0$ dépend de $a$ : on ne peut pas dominer uniformément sur tout $]0,+\infty[$, d'où le passage par les segments $[a,+\infty[$.

**Étape 6 — Conclusion.**
$$\boxed{g\in\mathcal C^\infty\big(]0,+\infty[\big)\qquad\text{et}\qquad\lim_{x\to0^+}g(x)=\frac12}$$
===RÉPONSE===
$g$ est $\mathcal C^\infty$ sur $]0,+\infty[$ (convergence uniforme des séries dérivées sur $[a,+\infty[$) et $g(x)\to\frac12$ quand $x\to0^+$."""

D['m-ccmp-21b'] = r"""**Étape 1 — Analyse de l'énoncé.** $E$ est euclidien de dimension $n\ge2$. On note $d=\|c_1-c_2\|$, avec des rayons $r_1,r_2\ge0$. Il faut une condition nécessaire et suffisante (CNS) pour que :
1. les boules fermées $B_f(c_1,r_1)$ et $B_f(c_2,r_2)$ se rencontrent ;
2. les sphères $S(c_1,r_1)$ et $S(c_2,r_2)$ se rencontrent.

**Étape 2 — Rappels du cours.**

> **Théorème — Inégalité triangulaire.** $\|u+v\|\le\|u\|+\|v\|$, et donc $\big|\|u\|-\|v\|\big|\le\|u-v\|$.

> **Théorème — Pythagore.** Si $u\perp v$, alors $\|\alpha u+\beta v\|^2=\alpha^2\|u\|^2+\beta^2\|v\|^2$.

> **Propriété — Dimension.** Si $\dim E\ge2$, tout vecteur unitaire $u$ admet un vecteur unitaire $v$ orthogonal (complétion en base orthonormée).

**Étape 3 — Stratégie.** Pour chaque question, la condition nécessaire découle de l'inégalité triangulaire. Pour la suffisance, on construit un point explicite :
- pour les boules, un point bien placé sur le segment $[c_1,c_2]$ ;
- pour les sphères, un point du plan $\mathrm{Vect}(u,v)$ dont on calcule les coordonnées $(\alpha,\beta)$ en résolvant deux équations. C'est là que sert l'hypothèse $n\ge2$.

**Étape 4 — Résolution détaillée.**

**4.1 Boules : condition nécessaire.** Si $x$ appartient aux deux boules, alors $d\le\|c_1-x\|+\|x-c_2\|\le r_1+r_2$.

**4.2 Boules : condition suffisante.** Supposons $d\le r_1+r_2$. Si $r_1+r_2=0$, alors $d=0$ et $c_1=c_2$ convient. Sinon, posons $x=c_1+\frac{r_1}{r_1+r_2}(c_2-c_1)$. On obtient
$$\|x-c_1\|=\frac{r_1d}{r_1+r_2}\le r_1,\qquad\|x-c_2\|=\frac{r_2d}{r_1+r_2}\le r_2,$$
car $\frac d{r_1+r_2}\le1$.

**4.3 Sphères : condition nécessaire.** Si $\|x-c_1\|=r_1$ et $\|x-c_2\|=r_2$, alors $d\le r_1+r_2$. De plus, $r_1\le\|x-c_2\|+\|c_2-c_1\|=r_2+d$ et, de même, $r_2\le r_1+d$. Donc $|r_1-r_2|\le d\le r_1+r_2$.

**4.4 Sphères : cas $d=0$.** La condition impose $r_1=r_2$ : les deux sphères sont égales, et non vides puisque $E\ne\{0\}$.

**4.5 Sphères : cas $d>0$.** Soit $u=\frac{c_2-c_1}d$, et $v$ unitaire orthogonal à $u$ (possible car $n\ge2$). On cherche $x=c_1+\alpha u+\beta v$. Comme $c_2=c_1+du$, Pythagore donne
$$\|x-c_1\|^2=\alpha^2+\beta^2,\qquad\|x-c_2\|^2=(\alpha-d)^2+\beta^2.$$
En égalant à $r_1^2$ et $r_2^2$ et en soustrayant, on obtient $2\alpha d-d^2=r_1^2-r_2^2$, soit $\alpha=\dfrac{d^2+r_1^2-r_2^2}{2d}$. Il faut ensuite $\beta^2=r_1^2-\alpha^2\ge0$, c'est-à-dire
$$|d^2+r_1^2-r_2^2|\le2dr_1\iff(d-r_1)^2\le r_2^2\le(d+r_1)^2\iff|d-r_1|\le r_2\le d+r_1.$$
Cette double inégalité équivaut à $|r_1-r_2|\le d\le r_1+r_2$. On prend alors $\beta=\sqrt{r_1^2-\alpha^2}$.

**Étape 5 — Vérification.**

> **Contrôle numérique.** Sur 2000 tirages aléatoires (centres dans $\mathbb R^3$, rayons dans $[0,2]$), dès que la condition $|r_1-r_2|\le d\le r_1+r_2$ est vérifiée, le point $x$ construit en 4.5 est bien sur les deux sphères, à $10^{-9}$ près.

- Cas d'égalité $d=r_1+r_2$ : $\beta=0$, l'intersection est un seul point, sur la droite des centres (sphères tangentes extérieurement). Même chose pour $d=|r_1-r_2|$ (tangence intérieure).
- Rôle de $n\ge2$ : dans $\mathbb R$, $S(0,1)=\{-1,1\}$ et $S(3,2)=\{1,5\}$ se rencontrent, mais $S(0,1)$ et $S(1{,}5\,;1)=\{0{,}5\,;2{,}5\}$ ne se rencontrent pas, alors que $|1-1|\le1{,}5\le2$. La condition n'est donc plus suffisante en dimension 1.

**Étape 6 — Conclusion.**
$$\boxed{\begin{aligned}&B_f(c_1,r_1)\cap B_f(c_2,r_2)\ne\emptyset\iff\|c_1-c_2\|\le r_1+r_2\\&S(c_1,r_1)\cap S(c_2,r_2)\ne\emptyset\iff|r_1-r_2|\le\|c_1-c_2\|\le r_1+r_2\quad(n\ge2)\end{aligned}}$$
===RÉPONSE===
Boules : $d\le r_1+r_2$. Sphères (en dimension $\ge2$) : $|r_1-r_2|\le d\le r_1+r_2$, avec $d=\|c_1-c_2\|$."""

D['m-ccmp-26a'] = r"""**Étape 1 — Analyse de l'énoncé.** Pour $n\in\mathbb N^*$ :
1. il faut montrer qu'il existe $P\in\mathbb R[X]$ tel que $\sin(2n\theta)=\sin\theta\,P(\cos\theta)$ pour tout $\theta$ ;
2. il faut trouver son degré, son coefficient dominant et son terme constant ;
3. il faut résoudre $\sin(2n\theta)=0$ et en déduire les racines de $P$ ;
4. il faut calculer $\prod_{k=1}^{n-1}\cos\frac{k\pi}{2n}$.

**Étape 2 — Rappels du cours.**

> **Formule — Moivre et binôme.** $(\cos\theta+i\sin\theta)^m=\cos(m\theta)+i\sin(m\theta)$ et $(a+b)^m=\sum_j\binom mja^{m-j}b^j$.

> **Formule — Sommes de binomiaux.** $\sum_{j\text{ impair}}\binom{2n}j=\frac{(1+1)^{2n}-(1-1)^{2n}}2=2^{2n-1}$.

> **Théorème — Racines d'un polynôme.** Un polynôme non nul de degré $d$ a au plus $d$ racines. S'il a $d$ racines distinctes $c_1,\dots,c_d$, il s'écrit $\lambda\prod(X-c_k)$, avec $\lambda$ son coefficient dominant.

**Étape 3 — Stratégie.** On développe $(\cos\theta+i\sin\theta)^{2n}$ et on prend la partie imaginaire. Les puissances impaires de $\sin\theta$ se factorisent par $\sin\theta$, et le reste s'exprime en $\cos\theta$ grâce à $\sin^2=1-\cos^2$. Les zéros de $\sin(2n\theta)$ donnent $2n-1$ racines distinctes, donc la factorisation complète de $P$. Pour le produit, on calcule $P'(0)$ de deux façons : par la factorisation, et en dérivant $\frac{\sin(2n\theta)}{\sin\theta}$ en $\frac\pi2$.

**Étape 4 — Résolution détaillée.**

**4.1 Existence.** La partie imaginaire de $\sum_j\binom{2n}j\cos^{2n-j}\theta\,(i\sin\theta)^j$ ne fait intervenir que les $j$ impairs, avec $i^j=i\,(-1)^{\frac{j-1}2}$. En écrivant $\sin^j\theta=\sin\theta\,(1-\cos^2\theta)^{\frac{j-1}2}$, on obtient $\sin(2n\theta)=\sin\theta\,P(\cos\theta)$ avec
$$P=\sum_{\substack{1\le j\le2n-1\\ j\text{ impair}}}\binom{2n}j(-1)^{\frac{j-1}2}X^{2n-j}(1-X^2)^{\frac{j-1}2}.$$

**4.2 Degré et coefficient dominant.** Chaque terme est de degré $(2n-j)+(j-1)=2n-1$, de coefficient dominant $\binom{2n}j(-1)^{\frac{j-1}2}(-1)^{\frac{j-1}2}=\binom{2n}j>0$. Ces coefficients ne se compensent pas, donc $\deg P=2n-1$ et le coefficient dominant vaut $\sum_{j\text{ impair}}\binom{2n}j=2^{2n-1}$.

**4.3 Terme constant.** En $\theta=\frac\pi2$ : $\sin(n\pi)=1\cdot P(0)$, donc $P(0)=0$.

**4.4 Racines.** $\sin(2n\theta)=0\iff\theta\in\frac\pi{2n}\mathbb Z$. Pour $\theta_k=\frac{k\pi}{2n}$ avec $1\le k\le2n-1$, on a $\theta_k\in]0,\pi[$, donc $\sin\theta_k\ne0$ et $P(c_k)=0$ avec $c_k=\cos\theta_k$. Les $c_k$ sont distincts, car $\cos$ est injectif sur $]0,\pi[$. Ce sont $2n-1$ racines distinctes, donc toutes les racines :
$$P=2^{2n-1}\prod_{k=1}^{2n-1}(X-c_k).$$

**4.5 Produit des cosinus.** On a $c_{2n-k}=-c_k$ et $c_n=0$, d'où $P=X\,R$ avec $R=2^{2n-1}\prod_{k=1}^{n-1}(X^2-c_k^2)$. Il vient
$$P'(0)=R(0)=2^{2n-1}(-1)^{n-1}\prod_{k=1}^{n-1}c_k^2.$$
D'autre part, $g(\theta)=P(\cos\theta)=\frac{\sin2n\theta}{\sin\theta}$ sur $]0,\pi[$, donc $g'(\theta)=-\sin\theta\,P'(\cos\theta)$, et en $\frac\pi2$ : $g'(\frac\pi2)=-P'(0)$. Par la dérivée d'un quotient, $g'(\frac\pi2)=2n\cos(n\pi)=2n(-1)^n$, donc $P'(0)=2n(-1)^{n-1}$. En égalant les deux expressions :
$$\prod_{k=1}^{n-1}c_k^2=\frac{2n}{2^{2n-1}}=\frac n{4^{n-1}}.$$
Pour $1\le k\le n-1$, $\frac{k\pi}{2n}\in]0,\frac\pi2[$, donc $c_k>0$.

**Étape 5 — Vérification.**

> **Vérification — Calcul formel.** Pour $n=2$ : $P=8X^3-4X$. Pour $n=3$ : $P=32X^5-32X^3+6X$. Les deux sont de degré $2n-1$, de coefficient dominant $2^{2n-1}$, sans terme constant, et l'identité $\sin(2n\theta)=\sin\theta\,P(\cos\theta)$ est vérifiée. De plus, $P'(0)=-4=2\cdot2\cdot(-1)^{1}$ et $P'(0)=6=2\cdot3\cdot(-1)^2$, comme prévu.

> **Contrôle numérique.** $\prod_{k=1}^{n-1}\cos\frac{k\pi}{2n}$ vaut $0{,}70711$, $0{,}43301$, $0{,}13975$ et $0{,}022097$ pour $n=2,3,5,8$. La formule $\frac{\sqrt n}{2^{n-1}}$ donne les mêmes valeurs.

- Cas $n=1$ : le produit est vide et vaut $1=\frac{\sqrt1}{2^0}$ ; $P=2X$ et $\sin2\theta=2\sin\theta\cos\theta$. Tout est cohérent.

**Étape 6 — Conclusion.**
$$\boxed{\begin{aligned}&\deg P=2n-1,\qquad\text{coefficient dominant }2^{2n-1},\qquad P(0)=0\\&P=2^{2n-1}\prod_{k=1}^{2n-1}\Big(X-\cos\frac{k\pi}{2n}\Big),\qquad\prod_{k=1}^{n-1}\cos\frac{k\pi}{2n}=\frac{\sqrt n}{2^{n-1}}\end{aligned}}$$
===RÉPONSE===
$\deg P=2n-1$, coefficient dominant $2^{2n-1}$, $P(0)=0$ ; racines $\cos\frac{k\pi}{2n}$ ($1\le k\le2n-1$) ; $\prod_{k=1}^{n-1}\cos\frac{k\pi}{2n}=\frac{\sqrt n}{2^{n-1}}$."""
