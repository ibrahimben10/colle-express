
# Indices et corrigés — Maths CCMP (partie 1)
C = {}
def c(id, h1, h2, h3, corrige, reponse=""):
    C[id] = {"indices": [h1.strip(), h2.strip(), h3.strip()], "corrige": corrige.strip(), "reponse": reponse.strip()}

c("m-ccmp-01a",
r"Pour le sens direct, montre que $x\mapsto d(x,F)$ est elle-même convexe quand $F$ est convexe.",
r"Pour la réciproque, prends $a,b\in F$ : que valent $f_{a,b}(0)$ et $f_{a,b}(1)$ ? Que dire d'une fonction convexe positive nulle aux extrémités ?",
r"Tu obtiens $d\big((1-t)a+tb,F\big)=0$, donc $(1-t)a+tb\in\overline F$. Pour conclure il faut que $F$ soit fermé : cherche un contre-exemple sinon (par exemple $F=\mathbb Q$ dans $\mathbb R$).",
r"""
**Sens direct.** Supposons $F$ convexe. Soient $x,y\in E$, $t\in[0,1]$ et $\varepsilon>0$. Il existe $u,v\in F$ avec $\|x-u\|\le d(x,F)+\varepsilon$ et $\|y-v\|\le d(y,F)+\varepsilon$. Par convexité, $(1-t)u+tv\in F$, donc
$$d\big((1-t)x+ty,F\big)\le\|(1-t)(x-u)+t(y-v)\|\le(1-t)d(x,F)+t\,d(y,F)+\varepsilon.$$
Ainsi $\delta=d(\cdot,F)$ est convexe. Comme $t\mapsto(1-t)a+tb$ est affine, $f_{a,b}=\delta\circ(\text{affine})$ est convexe.

**Réciproque.** Soient $a,b\in F$. Alors $f_{a,b}(0)=d(a,F)=0$ et $f_{a,b}(1)=0$. Une fonction convexe est sous ses cordes : $0\le f_{a,b}(t)\le(1-t)f_{a,b}(0)+tf_{a,b}(1)=0$. Donc $d\big((1-t)a+tb,F\big)=0$, c'est-à-dire $(1-t)a+tb\in\overline F$.

**Attention à l'hypothèse.** On a seulement prouvé que $\overline F$ est convexe. Si $F$ est **fermé** (cas implicite de l'énoncé), $F=\overline F$ est convexe. Sans cette hypothèse l'équivalence est fausse : pour $F=\mathbb Q\subset\mathbb R$, $d(x,\mathbb Q)=0$ pour tout $x$, donc toutes les $f_{a,b}$ sont nulles (convexes) alors que $\mathbb Q$ n'est pas convexe.

À l'oral, signaler spontanément ce point de fermeture est très apprécié.
""", r"Équivalence vraie pour $F$ fermé ; en général on obtient seulement $\overline F$ convexe.")

c("m-ccmp-01b",
r"Écris $p_n=P(X=n)$ et résous la récurrence linéaire d'ordre 1 avec second membre.",
r"Exprime $p_n$ à l'aide de $p_0$, puis utilise $\sum p_n=1$ (et $p_n\to0$) pour contraindre $\alpha$ et $\beta$.",
r"Pour l'espérance, utilise la fonction génératrice : $G(s)-p_0=\alpha sG(s)+\dfrac{\beta s}{1-\beta s}$.",
r"""
On note $p_n=P(X=n)$ et on suppose $\alpha,\beta>0$.

**1. Expression de $p_n$.** Par récurrence, $p_n=\alpha^np_0+\sum_{k=1}^n\alpha^{n-k}\beta^k$.

*Contraintes.* Tous les termes sont positifs et $\sum p_n$ converge, donc $p_n\to0$ ; or $p_n\ge\beta^n$ impose $\beta<1$, et $p_n\ge\alpha^{n-1}\beta$ impose $\alpha<1$. Ainsi $(\alpha,\beta)\in\,]0,1[^2$.

*Normalisation.* Par sommation (termes positifs, Fubini) :
$$1=\sum_n p_n=\frac{p_0}{1-\alpha}+\sum_{k\ge1}\beta^k\sum_{n\ge k}\alpha^{n-k}=\frac{p_0}{1-\alpha}+\frac{\beta}{(1-\alpha)(1-\beta)},$$
d'où $p_0=1-\alpha-\dfrac{\beta}{1-\beta}$, ce qui exige $p_0\ge0$, c'est-à-dire $\beta\le(1-\alpha)(1-\beta)$.

*Loi.* Pour $\alpha\ne\beta$ : $\sum_{k=1}^n\alpha^{n-k}\beta^k=\beta\,\dfrac{\beta^n-\alpha^n}{\beta-\alpha}$, donc
$$p_n=\alpha^np_0+\beta\,\frac{\beta^n-\alpha^n}{\beta-\alpha}.$$
(Pour $\alpha=\beta$ : $p_n=\alpha^np_0+n\alpha^n$.)

**2. Espérance.** Avec $G(s)=\sum p_ns^n$ (rayon $\ge1$), la récurrence donne $G(s)-p_0=\alpha sG(s)+\dfrac{\beta s}{1-\beta s}$, donc
$$G(s)=\frac{N(s)}{1-\alpha s},\qquad N(s)=p_0+\frac{\beta s}{1-\beta s}.$$
On a $N(1)=1-\alpha$, $N'(1)=\dfrac{\beta}{(1-\beta)^2}$. Comme $G$ est dérivable en $1$ (rayon $>1$ car $\alpha,\beta<1$) :
$$E(X)=G'(1)=\frac{N'(1)}{1-\alpha}+\frac{\alpha N(1)}{(1-\alpha)^2}=\frac{\beta}{(1-\alpha)(1-\beta)^2}+\frac{\alpha}{1-\alpha}.$$
""", r"$p_0=1-\alpha-\frac{\beta}{1-\beta}$, $E(X)=\frac{\alpha}{1-\alpha}+\frac{\beta}{(1-\alpha)(1-\beta)^2}$.")

c("m-ccmp-02a",
r"Commence par la relation simple $x f(x)=\operatorname{sh}x$ et dérive-la.",
r"En dérivant deux fois $xf=\operatorname{sh}$, tu obtiens $(xf)''=xf$ : traduis-la en une équation sur $f$.",
r"Pour résoudre, pose $z=xy$ : l'équation devient $z''=z$. Attention ensuite au raccord en $0$.",
r"""
**Équation.** Posons $z(x)=xf(x)=\operatorname{sh}x$. Alors $z''=z$, et $z''=(xf)''=xf''+2f'$. Donc $f$ vérifie
$$(E)\qquad x\,y''+2y'-x\,y=0.$$

**Résolution sur $]0,+\infty[$ ou $]-\infty,0[$.** Si $y$ est solution sur un tel intervalle $I$, $z=xy$ vérifie $z''=xy''+2y'=xy=z$, donc $z=A\operatorname{ch}x+B\operatorname{sh}x$ et
$$y=\frac{A\operatorname{ch}x+B\operatorname{sh}x}{x}.$$
Réciproquement ces fonctions sont solutions : l'espace des solutions sur $I$ est de dimension 2 (cohérent avec le théorème de Cauchy linéaire, le coefficient $x$ ne s'annulant pas).

**Solutions sur $\mathbb R$.** Soit $y$ de classe $\mathcal C^2$ sur $\mathbb R$ solution. Sur $]0,+\infty[$, $y=(A\operatorname{ch}x+B\operatorname{sh}x)/x$ ; comme $y$ est bornée au voisinage de $0^+$ et $\operatorname{ch}x/x\to+\infty$, on a $A=0$. De même à gauche : $y=B'\operatorname{sh}x/x$. La continuité en $0$ donne $B=y(0)=B'$. Donc $y=B\,\dfrac{\operatorname{sh}x}{x}$ (prolongée par $B$ en $0$), qui est bien $\mathcal C^\infty$ (série entière $\sum x^{2k}/(2k+1)!$) et solution.

**Conclusion.** Sur $\mathbb R$, l'espace des solutions est la droite $\operatorname{Vect}(f)$ : le point singulier $x=0$ fait chuter la dimension de 2 à 1.
""", r"$xy''+2y'-xy=0$ ; sur $\mathbb R$ : $y=B\,\frac{\operatorname{sh}x}{x}$.")

c("m-ccmp-02b",
r"Pour le sens direct, que dire d'une matrice diagonalisable et nilpotente ?",
r"Pour la réciproque, choisis $P=\prod(X-\lambda_i)$ sur les valeurs propres **distinctes** de $M$ et compare $P^n$ au polynôme caractéristique.",
r"Dans $\mathcal M_n(\mathbb R)$, teste la matrice de rotation $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$.",
r"""
**1. ($\Rightarrow$)** Si $M=QDQ^{-1}$ avec $D$ diagonale, alors $P(M)=QP(D)Q^{-1}$ est diagonalisable. Si $P(M)^n=0$, $P(M)$ est diagonalisable et nilpotente, donc ses valeurs propres sont nulles et $P(M)=0$.

**($\Leftarrow$)** Soient $\lambda_1,\dots,\lambda_r$ les valeurs propres distinctes de $M$, de multiplicités $m_i\le n$, et $P=\prod_{i}(X-\lambda_i)$. Alors $\chi_M=\prod(X-\lambda_i)^{m_i}$ divise $P^n$, donc par Cayley-Hamilton $P(M)^n=P^n(M)=0$. L'hypothèse donne $P(M)=0$ : $M$ annule un polynôme scindé à racines simples, elle est diagonalisable.

**2. Dans $\mathcal M_n(\mathbb R)$** (polynômes réels), l'équivalence est **fausse**. Pour $M=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ : si $P\in\mathbb R[X]$ et $P(M)^2=0$, alors $P(M)$ est nilpotente ; or $M$ est diagonalisable sur $\mathbb C$ (valeurs propres $\pm i$), donc $P(M)$ aussi, et $P(M)=0$. La propriété est vérifiée, mais $M$ n'est pas diagonalisable sur $\mathbb R$ ($\chi_M=X^2+1$ non scindé).

En fait, sur $\mathbb R$ la propriété caractérise les matrices **diagonalisables sur $\mathbb C$**.
""", r"Équivalence vraie sur $\mathbb C$ ; fausse sur $\mathbb R$ (rotation d'angle $\pi/2$).")

c("m-ccmp-03a",
r"$S$ est la matrice compagnon de $X^n-p^m$ : calcule $S^n$, puis utilise Bézout ($an+bm=1$).",
r"Pour la question 2, $U$ est semblable à la matrice compagnon $C$ de $X^n-p$, à coefficients entiers. Réduis $\sum\lambda_kC^k$ modulo $p$ : que devient $C$ ?",
r"Pour la question 3, si $p\mid\lambda_0,\dots,\lambda_{j-1}$ et $p\nmid\lambda_j$, multiplie par $U^{n-j}$ et divise par $p$ pour te ramener à la question 2. Pour la 4, montre que $\mathbb Q[S]=\mathbb Q[U]$ est un corps.",
r"""
**1.** $S$ est la matrice compagnon de $X^n-p^m$, donc $\chi_S=X^n-p^m$ et, par Cayley-Hamilton, $S^n=p^mI_n$ ; en particulier $S\in GL_n(\mathbb Q)$. Comme $m\wedge n=1$, il existe $(a,b)\in\mathbb Z^2$ avec $an+bm=1$, et
$$(p^aS^b)^n=p^{an}(S^n)^b=p^{an+bm}I_n=pI_n.$$

**2.** Notons $U=p^aS^b$. Les valeurs propres de $S$ sont les $\omega\,p^{m/n}$, $\omega\in\mathbb U_n$ (distinctes), donc celles de $U$ sont les $\omega^b p^{1/n}$ ; comme $b\wedge n=1$, $\omega\mapsto\omega^b$ permute $\mathbb U_n$ : $U$ a $n$ valeurs propres distinctes et $\chi_U=X^n-p$. Ainsi $U$ est semblable (sur $\mathbb Q$) à la matrice compagnon $C$ de $X^n-p$, à coefficients **entiers**, et $\sum\lambda_kU^k$ est semblable à $Q=\sum\lambda_kC^k\in\mathcal M_n(\mathbb Z)$.

Modulo $p$, $C\equiv N$ où $N$ est le décalage nilpotent (sous-diagonale de 1). Donc $Q\equiv\lambda_0I_n+\sum_{k\ge1}\lambda_kN^k$, matrice triangulaire de diagonale $\lambda_0$, et
$$\det Q\equiv\lambda_0^n\not\equiv0\pmod p.$$
Donc $\det Q\ne0$ : $\sum\lambda_kU^k\in GL_n(\mathbb Q)$.

**3.** Quitte à multiplier par un entier non nul, $\lambda\in\mathbb Z^n$ avec $\gcd(\lambda_0,\dots,\lambda_{n-1})=1$. Si $p\nmid\lambda_0$, c'est la question 2. Sinon soit $j\ge1$ minimal avec $p\nmid\lambda_j$ (il existe car le pgcd vaut 1). En utilisant $U^n=pI_n$ :
$$\frac1p\Big(\sum_k\lambda_kU^k\Big)U^{n-j}=\sum_{k\ge j}\lambda_kU^{k-j}+\sum_{k<j}\frac{\lambda_k}{p}U^{k+n-j}.$$
Les coefficients sont entiers (car $p\mid\lambda_k$ pour $k<j$) et le coefficient constant $\lambda_j$ n'est pas divisible par $p$ : par la question 2 cette matrice est inversible, donc $\sum\lambda_kU^k$ aussi.

**4.** $U^m=p^{am}S^{bm}=p^{am}S^{1-an}=p^{am}S\,(p^m)^{-a}=S$, donc $S\in\mathbb Q[U]$ et $\mathbb Q[S]=\mathbb Q[U]$. Par la question 3, tout élément non nul $\sum_{k<n}\lambda_kU^k$ de cette algèbre est inversible (et $\mathbb Q[U]=\{\sum_{k<n}\lambda_kU^k\}$ puisque $U^n=p$). Si $X^n-p^m=AB$ avec $1\le\deg A,\deg B<n$, alors $A(S)B(S)=\chi_S(S)=0$ avec $A(S),B(S)\ne0$ (le polynôme minimal de $S$ est de degré $n$, car $S$ est compagnon) : deux éléments inversibles de produit nul, absurde. Donc $X^n-p^m$ est irréductible dans $\mathbb Q[X]$.
""", r"$(p^aS^b)^n=pI_n$ avec $an+bm=1$ ; $\det\big(\sum\lambda_kU^k\big)\equiv\lambda_0^n\pmod p$ ; $\mathbb Q[S]$ est un corps.")

c("m-ccmp-03b",
r"Compare $u_n=\frac{\sin(\ln n)}n$ à $\int_n^{n+1}\frac{\sin(\ln t)}t\,dt$ : majore la différence avec l'inégalité des accroissements finis.",
r"Avec $g(t)=\frac{\sin(\ln t)}t$, $|g'(t)|\le\frac2{t^2}$ : la série des différences converge absolument.",
r"Calcule explicitement $\int_1^N\frac{\sin(\ln t)}t\,dt$ (pose $u=\ln t$) : cette quantité a-t-elle une limite ?",
r"""
**1.** Soit $g(t)=\dfrac{\sin(\ln t)}{t}$ sur $[1,+\infty[$. On a $g'(t)=\dfrac{\cos(\ln t)-\sin(\ln t)}{t^2}$, donc $|g'(t)|\le\dfrac2{t^2}$. Par l'inégalité des accroissements finis,
$$\Big|g(n)-\int_n^{n+1}g(t)\,dt\Big|=\Big|\int_n^{n+1}\big(g(n)-g(t)\big)dt\Big|\le\sup_{[n,n+1]}|g'|\le\frac2{n^2}.$$
La série de terme général $g(n)-\int_n^{n+1}g$ converge absolument, donc $\sum g(n)$ et $\sum\int_n^{n+1}g$ sont de même nature. (On ne peut pas utiliser la comparaison série-intégrale classique : $g$ n'est pas monotone.)

**2.** $\displaystyle\sum_{n=1}^{N-1}\int_n^{n+1}g=\int_1^N\frac{\sin(\ln t)}t\,dt=\int_0^{\ln N}\sin u\,du=1-\cos(\ln N).$

Cette quantité n'a pas de limite quand $N\to\infty$ : comme $\ln(N+1)-\ln N\to0$, la suite $(\ln N)$ passe arbitrairement près de tous les $2k\pi$ et de tous les $(2k+1)\pi$, donc $1-\cos(\ln N)$ a pour valeurs d'adhérence $0$ et $2$. La série des intégrales diverge, donc
$$\sum_{n\ge1}\frac{\sin(\ln n)}{n}\ \text{diverge}.$$
""", r"La série diverge (sommes partielles comparables à $1-\cos(\ln N)$).")

c("m-ccmp-04a",
r"Introduis la série génératrice $A(x)=\sum a_nx^n$ : quelle équation fonctionnelle la relation de récurrence impose-t-elle ?",
r"Tu dois trouver $A(x)=1+xA(x)^2$. Résous cette équation du second degré en choisissant la bonne racine (comportement en $0$).",
r"Plutôt que de justifier le rayon a priori, pars de $B(x)=\frac{1-\sqrt{1-4x}}{2x}$, développe-la en série entière, vérifie qu'elle satisfait $B=1+xB^2$ et conclus par unicité de la suite définie par récurrence.",
r"""
**Heuristique.** Si $A(x)=\sum a_nx^n$ a un rayon $>0$, le produit de Cauchy donne $\sum_n a_{n+1}x^{n+1}=x\sum_n\big(\sum_{k=0}^na_ka_{n-k}\big)x^n$, soit $A-1=xA^2$. Comme $A(0)=1$, $A(x)=\dfrac{1-\sqrt{1-4x}}{2x}$.

**Preuve rigoureuse.** Pour $|x|<\frac14$, $\sqrt{1-4x}=1-\sum_{n\ge1}\dfrac{2}{n}\dbinom{2n-2}{n-1}x^n$ (série du binôme $(1+u)^{1/2}$). Donc
$$B(x):=\frac{1-\sqrt{1-4x}}{2x}=\sum_{n\ge0}b_nx^n,\qquad b_n=\frac1{n+1}\binom{2n}{n},$$
de rayon $\frac14$. Pour $x\ne0$, $B$ est racine de $xB^2-B+1=0$ (vérification directe), relation qui s'étend en $0$ par continuité. L'identification des coefficients dans $B=1+xB^2$ (produit de Cauchy, valable dans le disque de convergence) donne $b_0=1$ et $b_{n+1}=\sum_{k=0}^nb_kb_{n-k}$. La suite $(b_n)$ vérifie la même récurrence que $(a_n)$, avec le même terme initial, donc $a_n=b_n$ pour tout $n$.

**Conclusion.** $a_n=\dfrac{1}{n+1}\dbinom{2n}{n}$ : ce sont les nombres de Catalan ($1,1,2,5,14,42,\dots$).
""", r"$a_n=\frac{1}{n+1}\binom{2n}{n}$.")

c("m-ccmp-04b",
r"Considère le morphisme de groupes $\det:G\to\mathbb C^*$. Quel est son noyau ?",
r"Le noyau est $G\cap SL_n(\mathbb C)=\{I_n\}$ : $\det$ est injectif, donc $G$ est isomorphe à $\det(G)$.",
r"Un sous-groupe fini de $\mathbb C^*$ de cardinal $N$ est contenu dans $\mathbb U_N$ (Lagrange) : conclus.",
r"""
L'application $\det:G\to\mathbb C^*$ est un morphisme de groupes de noyau $G\cap SL_n(\mathbb C)=\{I_n\}$ : elle est injective, donc $G\simeq H:=\det(G)$, sous-groupe fini de $\mathbb C^*$.

Soit $N=|H|$. Par le théorème de Lagrange, tout $z\in H$ vérifie $z^N=1$, donc $H\subset\mathbb U_N$. Comme $|\mathbb U_N|=N=|H|$, $H=\mathbb U_N=\langle e^{2i\pi/N}\rangle$ est cyclique.

Donc $G$ est cyclique (engendré par l'unique $g\in G$ tel que $\det g=e^{2i\pi/N}$).
""", r"$\det$ est injectif sur $G$, donc $G\simeq\mathbb U_N$ cyclique.")

c("m-ccmp-04c",
r"Écris $P(X+Y=n)=\sum_kP(X=k)P(Y=n-k)$ en précisant bien les valeurs possibles de $k$.",
r"Avec $P(X=k)=pq^{k-1}$ ($k\ge1$, $q=1-p$), chaque terme de la somme vaut $p^2q^{n-2}$ : il reste à compter les termes.",
r"Pour l'espérance et la variance, utilise la linéarité et l'indépendance : $E(X)=\frac1p$, $V(X)=\frac q{p^2}$.",
r"""
On note $q=1-p$ et $P(X=k)=P(Y=k)=pq^{k-1}$ pour $k\ge1$.

**1.** $X+Y$ prend ses valeurs dans $\{2,3,\dots\}$. Pour $n\ge2$, par la formule des probabilités totales et l'indépendance :
$$P(X+Y=n)=\sum_{k=1}^{n-1}P(X=k)P(Y=n-k)=\sum_{k=1}^{n-1}pq^{k-1}\,pq^{n-k-1}=(n-1)\,p^2q^{n-2}.$$
(Vérification : $\sum_{n\ge2}(n-1)p^2q^{n-2}=p^2\cdot\frac1{(1-q)^2}=1$.)

**2.** Par linéarité, $E(X+Y)=\dfrac2p$. Par indépendance, $V(X+Y)=V(X)+V(Y)=\dfrac{2q}{p^2}$.
""", r"$P(X+Y=n)=(n-1)p^2q^{n-2}$ ($n\ge2$), $E=\frac2p$, $V=\frac{2(1-p)}{p^2}$.")

c("m-ccmp-05a",
r"$P(Y=r)=\sum_{k\ge0}P(X=kp+r)$ : il faut sommer $\frac{\lambda^n}{n!}$ sur les $n\equiv r\pmod p$.",
r"Utilise le « filtre » des racines $p$-ièmes de l'unité : $\frac1p\sum_{j=0}^{p-1}\omega^{j(n-r)}$ vaut $1$ si $n\equiv r$ et $0$ sinon ($\omega=e^{2i\pi/p}$).",
r"Interverti les sommes : $\sum_n\frac{\lambda^n}{n!}\omega^{jn}=e^{\lambda\omega^j}$.",
r"""
$Y$ est à valeurs dans $\{0,\dots,p-1\}$ et $P(Y=r)=e^{-\lambda}\sum_{n\equiv r\,[p]}\dfrac{\lambda^n}{n!}$.

Soit $\omega=e^{2i\pi/p}$. Pour tout entier $m$, $\dfrac1p\sum_{j=0}^{p-1}\omega^{jm}$ vaut $1$ si $p\mid m$ et $0$ sinon (somme géométrique). Donc, en intervertissant les sommes (une somme finie et une série absolument convergente) :
$$\sum_{n\equiv r}\frac{\lambda^n}{n!}=\sum_{n\ge0}\frac{\lambda^n}{n!}\cdot\frac1p\sum_{j=0}^{p-1}\omega^{j(n-r)}=\frac1p\sum_{j=0}^{p-1}\omega^{-jr}e^{\lambda\omega^j}.$$

**Loi de $Y$ :** pour $r\in\{0,\dots,p-1\}$,
$$P(Y=r)=\frac1p\sum_{j=0}^{p-1}\omega^{-jr}\,e^{\lambda(\omega^j-1)}=\frac1p\sum_{j=0}^{p-1}e^{\lambda(\cos\frac{2\pi j}p-1)}\cos\!\Big(\lambda\sin\frac{2\pi j}p-\frac{2\pi jr}p\Big).$$

*Vérification* pour $p=2$ : $P(Y=0)=\frac12(1+e^{-2\lambda})$, $P(Y=1)=\frac12(1-e^{-2\lambda})$, ce qui redonne $e^{-\lambda}\operatorname{ch}\lambda$ et $e^{-\lambda}\operatorname{sh}\lambda$.
""", r"$P(Y=r)=\frac1p\sum_{j=0}^{p-1}\omega^{-jr}e^{\lambda(\omega^j-1)}$, $\omega=e^{2i\pi/p}$.")

c("m-ccmp-05b",
r"Que sais-tu des valeurs propres complexes d'une matrice réelle antisymétrique ?",
r"Les valeurs propres de $A$ sont $0$ et des $\pm i\theta_k$ ; celles de $\exp(xA)$ sont donc $1$ et des $e^{\pm ix\theta_k}$.",
r"Écris $f(x)$ comme produit des $(\mu+2)$ sur les valeurs propres $\mu$ de $\exp(xA)$, et minore $|e^{i\varphi}+2|$.",
r"""
$A$ est réelle antisymétrique, donc normale : elle est diagonalisable dans une base orthonormée de $\mathbb C^n$, et ses valeurs propres sont imaginaires pures (si $AX=\lambda X$, $\bar X^TAX=\lambda\|X\|^2$ est imaginaire pur). Comme $A$ est réelle, elles se regroupent en $0$ (multiplicité $n_0$) et en paires $\pm i\theta_k$, $k=1,\dots,s$ ($n_0+2s=n$).

Dans une base de diagonalisation, $\exp(xA)$ est diagonale de valeurs propres $1$ ($n_0$ fois) et $e^{\pm ix\theta_k}$. Donc
$$f(x)=\det\big(\exp(xA)+2I_n\big)=3^{n_0}\prod_{k=1}^s(e^{ix\theta_k}+2)(e^{-ix\theta_k}+2)=3^{n_0}\prod_{k=1}^s|e^{ix\theta_k}+2|^2.$$
Or $|e^{i\varphi}+2|\ge2-1=1$. Donc $f(x)\ge1$ pour tout $x$, et
$$\inf_{\mathbb R}f\ge1>0.$$
(Plus précisément $|e^{i\varphi}+2|^2=5+4\cos\varphi\in[1,9]$.)
""", r"$f(x)=3^{n_0}\prod|e^{ix\theta_k}+2|^2\ge1$.")

c("m-ccmp-06a",
r"La linéarité est immédiate. Calcule $\varphi^k(M)$.",
r"$\varphi^k(M)=A^kMA^k$. Pour la réciproque, choisis une matrice $M$ bien particulière.",
r"Si $A=PDP^{-1}$, calcule l'image de $PE_{ij}P^{-1}$ par $\varphi$.",
r"""
**1.** $\varphi$ est linéaire (distributivité du produit) de $\mathcal M_n(\mathbb R)$ dans lui-même : c'est un endomorphisme. Par récurrence, $\varphi^k(M)=A^kMA^k$.
- Si $A^k=0$, alors $\varphi^k=0$ : $\varphi$ est nilpotent.
- Si $\varphi^k=0$, alors $\varphi^k(I_n)=A^{2k}=0$ : $A$ est nilpotente.

**2.** Supposons $A=PDP^{-1}$ avec $D=\operatorname{diag}(d_1,\dots,d_n)$. Les matrices $F_{ij}=PE_{ij}P^{-1}$ forment une base de $\mathcal M_n(\mathbb R)$ (image de la base canonique par l'automorphisme $M\mapsto PMP^{-1}$), et
$$\varphi(F_{ij})=PDP^{-1}PE_{ij}P^{-1}PDP^{-1}=P\,DE_{ij}D\,P^{-1}=d_id_j\,F_{ij}.$$
On a une base de vecteurs propres : $\varphi$ est diagonalisable, de valeurs propres les produits $d_id_j$.
""", r"$\varphi^k(M)=A^kMA^k$ ; $\varphi(PE_{ij}P^{-1})=d_id_j\,PE_{ij}P^{-1}$.")

c("m-ccmp-06b",
r"$g(t)=\sum p_nt^n$ est une série entière de rayon $\ge1$ : sur $[0,1[$ elle est $\mathcal C^\infty$. Tout se joue en $t=1$.",
r"Sens ($\Leftarrow$) : si $E(X^m)<\infty$, les séries des dérivées jusqu'à l'ordre $m$ convergent normalement sur $[0,1]$.",
r"Sens ($\Rightarrow$) : $g^{(m)}(t)=\sum n(n-1)\cdots(n-m+1)p_nt^{n-m}$ est croissante sur $[0,1[$ et bornée par $g^{(m)}(1)$ ; utilise la convergence monotone (série à termes positifs).",
r"""
Notons $p_n=P(X=n)$, $g(t)=\sum_{n\ge0}p_nt^n$ (rayon $\ge1$) et $n^{\underline m}=n(n-1)\cdots(n-m+1)$.

**($\Leftarrow$)** Supposons $E(X^m)=\sum n^mp_n<\infty$. Pour $k\le m$ et $t\in[0,1]$, $|n^{\underline k}p_nt^{n-k}|\le n^mp_n$ (pour $n\ge1$) : les séries dérivées $\sum n^{\underline k}p_nt^{n-k}$ convergent normalement sur $[0,1]$. Par le théorème de dérivation terme à terme, $g\in\mathcal C^m([0,1])$, avec $g^{(m)}(1)=E\big(X^{\underline m}\big)$.

**($\Rightarrow$)** Supposons $g\in\mathcal C^m([0,1])$. Sur $[0,1[$, $g^{(m)}(t)=\sum_{n\ge m}n^{\underline m}p_nt^{n-m}$. Pour chaque $N$ et $t\in[0,1[$,
$$\sum_{n=m}^Nn^{\underline m}p_nt^{n-m}\le g^{(m)}(t)\le\sup_{[0,1]}|g^{(m)}|=:K.$$
En faisant $t\to1$ puis $N\to\infty$ : $\sum n^{\underline m}p_n\le K<\infty$. Enfin pour $n\ge2m$, $n^{\underline m}\ge(n/2)^m$, donc $n^mp_n\le2^mn^{\underline m}p_n$ et $E(X^m)<\infty$.

*Remarque :* on obtient au passage $g^{(m)}(1)=E\big(X(X-1)\cdots(X-m+1)\big)$ (moments factoriels).
""", r"Équivalence via $g^{(m)}(t)=\sum n^{\underline m}p_nt^{n-m}$ et convergence monotone.")

c("m-ccmp-07a",
r"Étudie le signe de $f'(x)=\frac{\ln x-1}{\ln^2x}$.",
r"Pour l'équivalent de $f^{-1}(n)$ : si $x=f^{-1}(y)$, alors $x=y\ln x$. Prends le logarithme pour montrer que $\ln x\sim\ln y$.",
r"Tu obtiens $\frac1{f^{-1}(n)}\sim\frac1{n\ln n}$ : série de Bertrand divergente, et sommation des équivalents pour les sommes partielles.",
r"""
**1.** $f$ est continue sur $[e,+\infty[$ et $f'(x)=\dfrac{\ln x-1}{\ln^2x}>0$ pour $x>e$ : $f$ est strictement croissante. $f(e)=e$ et $f(x)\to+\infty$. Donc $f$ réalise une bijection de $[e,+\infty[$ sur $J=[e,+\infty[$.

**2.** Notons $x_y=f^{-1}(y)\to+\infty$ quand $y\to\infty$. On a $x_y=y\ln x_y$, donc $\ln x_y=\ln y+\ln\ln x_y$, et comme $\ln\ln x_y=o(\ln x_y)$, $\ln x_y\sim\ln y$. Ainsi
$$f^{-1}(y)=y\ln x_y\sim y\ln y,\qquad\frac1{f^{-1}(n)}\sim\frac1{n\ln n}.$$
La série de Bertrand $\sum\frac1{n\ln n}$ diverge (comparaison avec $\int\frac{dt}{t\ln t}=\ln\ln t$), donc par comparaison de séries à termes positifs, $\sum_{n\ge3}\frac1{f^{-1}(n)}$ **diverge**.

**3.** Pour des séries à termes positifs divergentes, les sommes partielles sont équivalentes. Or $\sum_{k=3}^n\frac1{k\ln k}\sim\int_3^n\frac{dt}{t\ln t}\sim\ln\ln n$ (comparaison série-intégrale, $t\mapsto\frac1{t\ln t}$ décroissante). Donc
$$S_n=\sum_{k=3}^n\frac1{f^{-1}(k)}\sim\ln\ln n.$$
""", r"$f^{-1}(n)\sim n\ln n$ ; la série diverge et $S_n\sim\ln\ln n$.")

c("m-ccmp-07b",
r"$MM^T$ et $M^TM$ sont symétriques réelles : quand deux matrices symétriques réelles sont-elles orthogonalement semblables ?",
r"Il suffit qu'elles aient le même polynôme caractéristique (mêmes valeurs propres avec multiplicités), grâce au théorème spectral.",
r"Montre $\chi_{AB}=\chi_{BA}$ : facile si $A$ est inversible, puis par densité de $GL_n$.",
r"""
**Réduction du problème.** $S_1=MM^T$ et $S_2=M^TM$ sont symétriques réelles. Par le théorème spectral, $S_i=P_iD_iP_i^T$ avec $P_i\in O_n(\mathbb R)$ et $D_i$ diagonale. Si $\chi_{S_1}=\chi_{S_2}$, on peut ordonner les valeurs propres pour avoir $D_1=D_2=D$, et alors $S_2=P_2P_1^T\,S_1\,(P_2P_1^T)^T$ avec $P_2P_1^T\in O_n$ : elles sont orthosemblables.

**Lemme : $\chi_{AB}=\chi_{BA}$.** Si $A$ est inversible, $BA=A^{-1}(AB)A$, donc $\chi_{BA}=\chi_{AB}$. En général, $A_k=A+\frac1kI_n$ est inversible pour $k$ assez grand ($A$ n'a qu'un nombre fini de valeurs propres), et $\chi_{A_kB}=\chi_{BA_k}$. Les coefficients de $\chi_{XY}$ sont polynomiaux en les coefficients de $X$ : en faisant $k\to\infty$, $\chi_{AB}=\chi_{BA}$.

**Conclusion.** Avec $A=M$, $B=M^T$ : $\chi_{MM^T}=\chi_{M^TM}$, donc $MM^T$ et $M^TM$ sont orthogonalement semblables.
""", r"Même polynôme caractéristique ($\chi_{AB}=\chi_{BA}$) + théorème spectral.")

c("m-ccmp-08a",
r"Calcule d'abord le produit de **tous** les diviseurs de $n$ : associe chaque diviseur $d$ à $n/d$.",
r"Le produit de tous les diviseurs vaut $n^{\tau(n)/2}$ où $\tau(n)$ est le nombre de diviseurs. Donc $f(n)=n^{\tau(n)/2-1}$.",
r"$f(n)=n$ équivaut (pour $n\ge2$) à $\tau(n)=4$ : quels entiers ont exactement 4 diviseurs ?",
r"""
**Produit des diviseurs.** Notons $D(n)$ l'ensemble des diviseurs de $n$ et $\tau(n)=|D(n)|$. L'application $d\mapsto n/d$ est une bijection de $D(n)$, donc
$$\Big(\prod_{d\mid n}d\Big)^2=\prod_{d\mid n}d\cdot\prod_{d\mid n}\frac nd=n^{\tau(n)},\qquad\prod_{d\mid n}d=n^{\tau(n)/2}.$$
Donc $f(n)=n^{\tau(n)/2-1}$ (produit vide égal à 1 pour $n=1$).

**Résolution.** Pour $n=1$ : $f(1)=1$, solution. Pour $n\ge2$ : $f(n)=n\iff\frac{\tau(n)}2-1=1\iff\tau(n)=4$.

Si $n=\prod p_i^{a_i}$, $\tau(n)=\prod(a_i+1)=4$ impose : un seul facteur avec $a=3$, ou deux facteurs avec $a_1=a_2=1$.

**Conclusion.** $f(n)=n\iff n=1$, ou $n=p^3$ ($p$ premier), ou $n=pq$ ($p\ne q$ premiers). Exemples : $6=1\cdot2\cdot3$, $8=1\cdot2\cdot4$.
""", r"$n=1$, $n=p^3$ ou $n=pq$ ($p\ne q$ premiers).")

c("m-ccmp-08b",
r"Pour la convergence, donne un équivalent de $\ln\cos\frac x{2^n}$ quand $n\to\infty$.",
r"Pour la somme, passe au produit : $\sum\ln\cos=\ln\prod\cos$. Pense à la formule $\sin2a=2\sin a\cos a$.",
r"Montre que $\sin\frac x{2^N}\prod_{k=0}^N\cos\frac x{2^k}=\frac{\sin2x}{2^{N+1}}$ puis fais $N\to\infty$.",
r"""
**Convergence.** Pour $x\in[0,1]$, $\frac x{2^n}\to0$ et $\ln\cos u\sim-\frac{u^2}2$, donc $\ln\cos\frac x{2^n}\sim-\frac{x^2}{2\cdot4^n}$ (si $x\ne0$) : terme général de signe constant, équivalent à celui d'une série géométrique convergente. La série converge (et sa somme est nulle si $x=0$).

**Calcul** pour $x\in]0,1]$. Posons $P_N=\prod_{k=0}^N\cos\frac x{2^k}$. Avec $\sin2a=2\sin a\cos a$, par récurrence descendante :
$$P_N\sin\frac x{2^N}=\frac12P_{N-1}\sin\frac x{2^{N-1}}=\dots=\frac1{2^N}\cos x\sin x=\frac{\sin2x}{2^{N+1}}.$$
Donc $P_N=\dfrac{\sin2x}{2^{N+1}\sin(x/2^N)}\xrightarrow[N\to\infty]{}\dfrac{\sin2x}{2x}$ puisque $2^N\sin\frac x{2^N}\to x$.

Comme $2x\in]0,2]\subset]0,\pi[$, $\sin2x>0$ et par continuité du logarithme :
$$\sum_{n=0}^{\infty}\ln\cos\frac x{2^n}=\ln\frac{\sin2x}{2x}.$$
""", r"$\sum_{n\ge0}\ln\cos\frac x{2^n}=\ln\frac{\sin2x}{2x}$ (et $0$ si $x=0$).")

c("m-ccmp-09",
r"Question 1 : encadre $f$ entre son minimum $m$ et son maximum $M$, multiplie par $g\ge0$ et intègre.",
r"Question 2 : sépare l'intégrale sur $[\varepsilon,+\infty[$ en deux et fais les changements de variables $u=bt$ et $u=at$.",
r"Tu dois arriver à $ab\int_{b\varepsilon}^{a\varepsilon}\frac{\sin u}{u}\cdot\frac{du}u$ : applique la formule de la question 1.",
r"""
**1.** $f$ est continue sur le segment : elle atteint $m=\min f$ et $M=\max f$. Comme $g\ge0$, $mg\le fg\le Mg$, d'où $m\int g\le\int fg\le M\int g$.
- Si $\int g=0$, $g$ (continue, positive) est nulle et tout $c$ convient.
- Sinon $\frac{\int fg}{\int g}\in[m,M]$ et le théorème des valeurs intermédiaires fournit $c$ avec $f(c)=\frac{\int fg}{\int g}$.

**2.** Soient $a,b>0$ et $h(t)=\dfrac{a\sin bt-b\sin at}{t^2}$.

*Convergence.* En $0$ : $a\sin bt-b\sin at=a\big(bt-\frac{b^3t^3}6\big)-b\big(at-\frac{a^3t^3}6\big)+o(t^3)=\frac{ab(a^2-b^2)}6t^3+o(t^3)$, donc $h(t)\to0$ : $h$ se prolonge par continuité. En $+\infty$ : $|h(t)|\le\frac{a+b}{t^2}$, intégrable. L'intégrale converge.

*Calcul.* Pour $\varepsilon>0$, les deux intégrales $\int_\varepsilon^\infty\frac{\sin bt}{t^2}dt$ et $\int_\varepsilon^\infty\frac{\sin at}{t^2}dt$ convergent ; avec $u=bt$ et $u=at$ :
$$\int_\varepsilon^\infty h=ab\int_{b\varepsilon}^\infty\frac{\sin u}{u^2}du-ab\int_{a\varepsilon}^\infty\frac{\sin u}{u^2}du=ab\int_{b\varepsilon}^{a\varepsilon}\frac{\sin u}{u}\cdot\frac{du}{u}.$$
Par la question 1 (avec $f=\frac{\sin u}u$, $g=\frac1u>0$ sur le segment), il existe $c_\varepsilon$ entre $a\varepsilon$ et $b\varepsilon$ tel que cette quantité vaut $ab\,\frac{\sin c_\varepsilon}{c_\varepsilon}\ln\frac ab$. Quand $\varepsilon\to0$, $c_\varepsilon\to0$ et $\frac{\sin c_\varepsilon}{c_\varepsilon}\to1$ :
$$\int_0^{+\infty}\frac{a\sin bt-b\sin at}{t^2}\,dt=ab\ln\frac ab.$$
""", r"$ab\ln\frac ab$.")

c("m-ccmp-10b",
r"Pour la structure de groupe, utilise que la similitude est une relation d'équivalence compatible avec la multiplication par un scalaire.",
r"Si $cA\sim A$, que peut-on dire du spectre de $A$ ? Il est stable par multiplication par $c$.",
r"Pour $A$ nilpotente, utilise la réduction de Jordan et la conjugaison par $\operatorname{diag}(1,c,c^2,\dots)$.",
r"""
**1.** $1\in O_A$. Si $c_1,c_2\in O_A$ : $A\sim c_2A$ entraîne $c_1A\sim c_1c_2A$, et $c_1A\sim A$, donc par transitivité $c_1c_2A\sim A$. Si $cA\sim A$, en multipliant par $c^{-1}$ : $A\sim c^{-1}A$. Donc $O_A$ est un sous-groupe de $\mathbb C^*$.

**2.** *($\Leftarrow$, et question 3)* Si $A$ est nilpotente, elle est semblable à une matrice de Jordan $J$ formée de blocs $J_k$ (1 sur la sur-diagonale). Pour $c\ne0$, avec $D=\operatorname{diag}(1,c,\dots,c^{k-1})$, on vérifie $D^{-1}(cJ_k)D=J_k$ (le coefficient $(i,i+1)$ devient $c\cdot c^{i-1}/c^{i}=1$). Donc $cA\sim A$ pour tout $c\in\mathbb C^*$ : $O_A=\mathbb C^*$, infini.

*($\Rightarrow$)* Supposons $O_A$ infini. Si $cA\sim A$, alors $\operatorname{Sp}(cA)=c\operatorname{Sp}(A)=\operatorname{Sp}(A)$. Si $A$ avait une valeur propre $\lambda\ne0$, les $c\lambda$ pour $c\in O_A$ seraient une infinité de valeurs propres distinctes : absurde. Donc $\operatorname{Sp}(A)=\{0\}$ et $A$ est nilpotente (Cayley-Hamilton : $\chi_A=X^3$).

**3.** Déjà vu : $A$ nilpotente $\Rightarrow O_A=\mathbb C^*$.

*Complément :* si $A$ n'est pas nilpotente, $O_A$ est un sous-groupe fini de $\mathbb C^*$, donc un groupe $\mathbb U_d$ de racines de l'unité.
""", r"$O_A$ infini $\iff A$ nilpotente, et alors $O_A=\mathbb C^*$.")

c("m-ccmp-11a",
r"L'ensemble $K=\{X:X^TMX\le1\}$ est toujours fermé. La question est donc : quand est-il borné ?",
r"Si $M\in\mathcal S_n^{++}$, minore $X^TMX$ par $\lambda_{\min}\|X\|^2$ (théorème spectral).",
r"Si $M$ a une valeur propre $\lambda\le0$, considère les vecteurs $tV$ avec $V$ vecteur propre associé.",
r"""
$K=\{X\in\mathbb R^n:X^TMX\le1\}$ est l'image réciproque de $]-\infty,1]$ par l'application continue (polynomiale) $X\mapsto X^TMX$ : il est **fermé**. En dimension finie, $K$ est compact si et seulement s'il est borné.

**($\Rightarrow$)** Si $M\in\mathcal S_n^{++}$, par le théorème spectral, $X^TMX\ge\lambda_{\min}\|X\|^2$ avec $\lambda_{\min}>0$. Pour $X\in K$, $\|X\|^2\le1/\lambda_{\min}$ : $K$ est borné, donc compact.

**($\Leftarrow$)** Si $M\notin\mathcal S_n^{++}$, elle a une valeur propre $\lambda\le0$, de vecteur propre $V\ne0$. Pour tout $t\in\mathbb R$, $(tV)^TM(tV)=\lambda t^2\|V\|^2\le0\le1$, donc $tV\in K$ : $K$ contient une droite et n'est pas borné, donc pas compact.

(Pour $M\in\mathcal S_n^{++}$, $K$ est un ellipsoïde plein.)
""", r"$K$ fermé ; borné $\iff\lambda_{\min}(M)>0$.")

c("m-ccmp-11b",
r"Le sens ($\Leftarrow$) est simple : une limite simple de fonctions convexes est convexe.",
r"Pour ($\Rightarrow$), approche $f''\ge0$ (continue) par des polynômes grâce au théorème de Weierstrass, en t'assurant qu'ils restent positifs.",
r"Si $Q_n\to f''$ uniformément avec erreur $\varepsilon_n$, pose $R_n=Q_n+\varepsilon_n\ge0$ puis $P_n(x)=f(a)+f'(a)(x-a)+\int_a^x(x-t)R_n(t)\,dt$.",
r"""
**($\Leftarrow$)** Si $P_n\to f$ uniformément (donc simplement) avec $P_n$ convexes sur $[a,b]$, alors pour $x,y\in[a,b]$, $t\in[0,1]$ : $P_n((1-t)x+ty)\le(1-t)P_n(x)+tP_n(y)$, et le passage à la limite donne la convexité de $f$.

**($\Rightarrow$)** $f\in\mathcal C^2$ convexe, donc $f''\ge0$ continue sur $[a,b]$. Par le théorème de Weierstrass, il existe des polynômes $Q_n$ avec $\varepsilon_n=\|Q_n-f''\|_\infty\to0$. Posons $R_n=Q_n+\varepsilon_n$ : $R_n\ge f''\ge0$ et $\|R_n-f''\|_\infty\le2\varepsilon_n$.

Soit $P_n(x)=f(a)+f'(a)(x-a)+\int_a^x(x-t)R_n(t)\,dt$. C'est un polynôme, et $P_n''=R_n\ge0$ : $P_n$ est convexe sur $[a,b]$. Par la formule de Taylor avec reste intégral, $f(x)=f(a)+f'(a)(x-a)+\int_a^x(x-t)f''(t)\,dt$, donc
$$|P_n(x)-f(x)|\le\int_a^x(x-t)\,2\varepsilon_n\,dt\le(b-a)^2\varepsilon_n\xrightarrow[n\to\infty]{}0$$
uniformément sur $[a,b]$.
""", r"Approcher $f''$ par des polynômes positifs puis intégrer deux fois (Taylor reste intégral).")

c("m-ccmp-12a",
r"Écris le dénominateur sous forme canonique : $1-2t\cos x+t^2=(t-\cos x)^2+\sin^2x$.",
r"Une primitive est $\frac1{\sin x}\arctan\frac{t-\cos x}{\sin x}$. Simplifie $\frac{1-\cos x}{\sin x}$ et $\frac{\cos x}{\sin x}$ à l'aide d'angles.",
r"Pour la question 2, développe $\frac1{(1+t^2)-2t\cos x}$ en série géométrique en puissances de $\cos x$ et intègre terme à terme.",
r"""
**1.** Pour $x\in]0,\pi/2]$, $1-2t\cos x+t^2=(t-\cos x)^2+\sin^2x\ge\sin^2x>0$ : l'intégrande est continu sur $[0,1]$, l'intégrale existe. Une primitive est $\frac1{\sin x}\arctan\frac{t-\cos x}{\sin x}$, donc
$$I(x)=\frac1{\sin x}\Big(\arctan\frac{1-\cos x}{\sin x}+\arctan\frac{\cos x}{\sin x}\Big).$$
Or $\frac{1-\cos x}{\sin x}=\tan\frac x2$ et $\frac{\cos x}{\sin x}=\tan\big(\frac\pi2-x\big)$ avec $\frac x2,\frac\pi2-x\in[0,\frac\pi2[$. D'où
$$I(x)=\frac1{\sin x}\Big(\frac x2+\frac\pi2-x\Big)=\frac{\pi-x}{2\sin x}.$$

**2.** Posons $c=\cos x\in[0,1[$. Pour $t\in[0,1]$, $0\le2tc<1+t^2$ (car $2t\le1+t^2$ et $c<1$), donc
$$\frac1{1+t^2-2tc}=\sum_{k\ge0}\frac{(2t)^kc^k}{(1+t^2)^{k+1}}.$$
Les termes sont positifs : on peut intégrer terme à terme (théorème d'intégration terme à terme pour les séries de fonctions positives). Ainsi
$$\frac{\pi-x}{\sin x}=2I(x)=\sum_{k\ge0}\alpha_k\cos^kx,\qquad\alpha_k=2\int_0^1\Big(\frac{2t}{1+t^2}\Big)^k\frac{dt}{1+t^2}.$$
Comme $0\le\frac{2t}{1+t^2}\le1$, la suite $\big(\frac{2t}{1+t^2}\big)^k$ décroît en $k$ : $(\alpha_k)$ est **positive et décroissante**.

*Vérification* : $\alpha_0=2\cdot\frac\pi4=\frac\pi2$, cohérent avec $x=\frac\pi2$ (cos nul) : $\frac{\pi-\pi/2}{1}=\frac\pi2$.
""", r"$I(x)=\frac{\pi-x}{2\sin x}$ ; $\alpha_k=2\int_0^1\big(\frac{2t}{1+t^2}\big)^k\frac{dt}{1+t^2}$.")

c("m-ccmp-12b",
r"Sur $\mathbb C$, tout endomorphisme est trigonalisable : commence par là.",
r"Dans une base $(e_1,\dots,e_n)$ où la matrice $T$ est triangulaire supérieure, que devient $T$ si l'on remplace $e_i$ par $\varepsilon^ie_i$ ?",
r"Le coefficient $t_{ij}$ ($j>i$) devient $\varepsilon^{j-i}t_{ij}$ : choisis $\varepsilon$ assez petit.",
r"""
$u$ est trigonalisable sur $\mathbb C$ : il existe une base $(e_1,\dots,e_n)$ dans laquelle sa matrice $T=(t_{ij})$ est triangulaire supérieure : $u(e_j)=\sum_{i\le j}t_{ij}e_i$.

Pour $\varepsilon>0$, posons $f_i=\varepsilon^ie_i$. Alors
$$u(f_j)=\varepsilon^ju(e_j)=\sum_{i\le j}t_{ij}\varepsilon^{j}e_i=\sum_{i\le j}\varepsilon^{j-i}t_{ij}f_i.$$
Dans la base $(f_i)$, la matrice $M$ est triangulaire supérieure, de diagonale inchangée, avec $m_{ij}=\varepsilon^{j-i}t_{ij}$ pour $j>i$ (et $0$ sous la diagonale).

Soit $K=\max|t_{ij}|$. Si $K=0$ c'est fini. Sinon, avec $\varepsilon=\min(1,\alpha/K)$, pour $j>i$ : $|m_{ij}|\le\varepsilon K\le\alpha$. (Si $\alpha=0$, il faut $u$ diagonalisable : l'énoncé suppose implicitement $\alpha>0$.)
""", r"Trigonaliser puis remplacer $e_i$ par $\varepsilon^ie_i$.")

c("m-ccmp-13a",
r"Écris $A$ comme somme de deux matrices de rang 1 : $A=uv^T+vu^T$ avec $u=(a^i)_i$ et $v=(1,\dots,1)^T$.",
r"Le rang est donc au plus 2. Ensuite, $\operatorname{Im}A\subset\operatorname{Vect}(u,v)$ : étudie la restriction de $A$ à ce plan.",
r"Calcule $Au$ et $Av$ en fonction de $S_1=\sum a^i$, $S_2=\sum a^{2i}$ et $n$ ; le polynôme caractéristique est $X^{n-2}$ fois celui de la matrice $2\times2$ obtenue.",
r"""
Notons $u=(a,a^2,\dots,a^n)^T$, $v=(1,\dots,1)^T$, $S_1=\sum_{i=1}^na^i=v^Tu$ et $S_2=\sum a^{2i}=u^Tu$. Alors $A=uv^T+vu^T$.

**Rang.** Pour $n=1$, $A=(2a)$, de rang 1. Pour $n\ge2$, $u$ et $v$ sont libres ($a\ne1$). $\operatorname{Im}A\subset\operatorname{Vect}(u,v)$ et $Au=S_1u+S_2v$, $Av=nu+S_1v$. La matrice de $A$ restreinte à $P=\operatorname{Vect}(u,v)$ dans la base $(u,v)$ est $B=\begin{pmatrix}S_1&n\\S_2&S_1\end{pmatrix}$, de déterminant $S_1^2-nS_2$. Par Cauchy-Schwarz, $S_1^2=(v^Tu)^2<\|v\|^2\|u\|^2=nS_2$ (inégalité stricte car $u$ et $v$ non colinéaires). Donc $B$ est inversible, $A(P)=P$ et $\operatorname{rg}A=2$.

**Polynôme caractéristique.** $\ker A$ est de dimension $n-2$ et $\mathbb R^n=P\oplus\ker A$ ($P$ stable, $A_{|P}$ inversible). Dans une base adaptée,
$$\chi_A=X^{n-2}\chi_B=X^{n-2}\big(X^2-2S_1X+S_1^2-nS_2\big),$$
avec $S_1=\dfrac{a(a^n-1)}{a-1}$ et $S_2=\dfrac{a^2(a^{2n}-1)}{a^2-1}$.

Les deux valeurs propres non nulles sont $S_1\pm\sqrt{nS_2}$ : l'une positive, l'autre négative (car $S_1^2<nS_2$).
""", r"$\operatorname{rg}A=2$ ($n\ge2$), $\chi_A=X^{n-2}\big(X^2-2S_1X+S_1^2-nS_2\big)$.")

c("m-ccmp-13b",
r"Pour ($\Leftarrow$), utilise la concavité sous la forme $f(x+s)+f(x-s)\le2f(x)$ et intègre en $s$.",
r"Pour ($\Rightarrow$), fixe $x$ et étudie $F(r)=\int_{x-r}^{x+r}f-2rf(x)$ au voisinage de $r=0$.",
r"Calcule $F'$, $F''$, $F'''$ : $F(0)=F'(0)=F''(0)=0$ et $F'''(0)=2f''(x)$. Conclus par Taylor.",
r"""
**($\Leftarrow$)** Si $f$ est concave, pour $s\ge0$ : $f(x)=f\big(\frac{(x+s)+(x-s)}2\big)\ge\frac{f(x+s)+f(x-s)}2$. En intégrant sur $s\in[0,r]$ :
$$2rf(x)\ge\int_0^r\big(f(x+s)+f(x-s)\big)ds=\int_{x-r}^{x+r}f(t)\,dt.$$

**($\Rightarrow$)** Fixons $x$ et posons $F(r)=\int_{x-r}^{x+r}f(t)dt-2rf(x)$, de classe $\mathcal C^3$ car $f\in\mathcal C^2$. On calcule
$$F'(r)=f(x+r)+f(x-r)-2f(x),\quad F''(r)=f'(x+r)-f'(x-r),\quad F'''(r)=f''(x+r)+f''(x-r).$$
Donc $F(0)=F'(0)=F''(0)=0$ et $F'''(0)=2f''(x)$. Par Taylor-Young, $F(r)=\frac{f''(x)}3r^3+o(r^3)$. L'hypothèse $F(r)\le0$ pour $r>0$ impose $f''(x)\le0$. Ceci pour tout $x$ : $f$ est concave.

(Version convexe : $\int_{x-r}^{x+r}f\ge2rf(x)$ caractérise les fonctions convexes — inégalité d'Hermite-Hadamard.)
""", r"Taylor : $\int_{x-r}^{x+r}f-2rf(x)=\frac{f''(x)}3r^3+o(r^3)$.")

c("m-ccmp-14a",
r"Pour l'existence de $(I_n+A)^{-1}$ : les valeurs propres d'une matrice antisymétrique réelle sont imaginaires pures.",
r"Remarque que $I_n-A$ et $(I_n+A)^{-1}$ commutent, et calcule $C^TC$. Pour le déterminant, utilise $\det(M^T)=\det M$.",
r"Pour l'inversibilité de $I_n+C$, factorise par $(I_n+A)^{-1}$. Pour la surjectivité, pense à $-I_2\in SO_2$.",
r"""
**1.** Si $AX=\lambda X$ ($X\in\mathbb C^n$ non nul), $\bar X^TAX=\lambda\|X\|^2$ et ce nombre est imaginaire pur ($A^T=-A$ réelle). Donc $-1\notin\operatorname{Sp}A$ et $I_n+A$ est inversible : $C$ est bien définie.

$I_n-A$ et $I_n+A$ commutent, donc $I_n-A$ commute avec $(I_n+A)^{-1}$. Avec $A^T=-A$ :
$$C^T=(I_n-A)^T\big((I_n+A)^{-1}\big)^T=(I_n+A)(I_n-A)^{-1},$$
$$C^TC=(I_n+A)(I_n-A)^{-1}(I_n+A)^{-1}(I_n-A)=I_n$$
(tous les facteurs commutent). Donc $C\in O_n$, et $\det C=\dfrac{\det(I_n-A)}{\det(I_n+A)}=\dfrac{\det\big((I_n+A)^T\big)}{\det(I_n+A)}=1$ : $C\in SO_n$.

**2.** $I_n+C(A)=(I_n+A)^{-1}\big((I_n+A)+(I_n-A)\big)=2(I_n+A)^{-1}$ : toujours inversible.

**3.** *Injectivité* : de $I_n+C=2(I_n+A)^{-1}$ on tire $A=2(I_n+C)^{-1}-I_n$ : $A$ est déterminée par $C(A)$.

*Non surjective* : l'image est contenue dans $\{R\in SO_n:-1\notin\operatorname{Sp}R\}$. Par exemple, pour $n=2$, la rotation d'angle $\pi$, $-I_2\in SO_2$, n'est pas atteinte. (En fait l'image est exactement cet ensemble : pour un tel $R$, $A=(I_n-R)(I_n+R)^{-1}$ est antisymétrique et $C(A)=R$.)
""", r"$C$ injective, d'image $\{R\in SO_n:\ -1\notin\operatorname{Sp}R\}$ : non surjective.")

c("m-ccmp-14b",
r"Étudie l'intégrabilité en $0$ (équivalent de $e^t-1$) et en $+\infty$.",
r"Pour la continuité sur $]0,+\infty[$, travaille sur un segment $[a,b]$ et domine $t^x$ par $t^a+t^b$.",
r"Développe $\frac1{e^t-1}=\sum_{k\ge1}e^{-kt}$ et intègre terme à terme (termes positifs) ; reconnais la fonction $\Gamma$.",
r"""
**1.** Soit $x>0$. L'intégrande $h(x,t)=\frac{t^x}{e^t-1}$ est continu et positif sur $]0,+\infty[$.
- En $0$ : $e^t-1\sim t$, donc $h\sim t^{x-1}$, intégrable car $x-1>-1$.
- En $+\infty$ : $h(x,t)\le2t^xe^{-t}$ pour $t\ge1$, intégrable.

$f$ est donc définie sur $]0,+\infty[$. *Continuité* : sur $[a,b]\subset]0,+\infty[$, $t^x\le t^a$ si $t\le1$ et $t^x\le t^b$ si $t\ge1$, donc $|h(x,t)|\le\varphi(t)=\frac{t^a+t^b}{e^t-1}$, intégrable et indépendante de $x$. Par le théorème de continuité sous l'intégrale, $f$ est continue sur $[a,b]$, donc sur $]0,+\infty[$.

**2.** Pour $t>0$, $\frac1{e^t-1}=\frac{e^{-t}}{1-e^{-t}}=\sum_{k\ge1}e^{-kt}$. Les fonctions $t\mapsto t^xe^{-kt}$ sont positives et intégrables, donc (intégration terme à terme d'une série de fonctions positives)
$$f(x)=\sum_{k\ge1}\int_0^\infty t^xe^{-kt}dt=\sum_{k\ge1}\frac{\Gamma(x+1)}{k^{x+1}}=\Gamma(x+1)\,\zeta(x+1),$$
avec le changement de variable $u=kt$. Exemple : $f(1)=\Gamma(2)\zeta(2)=\frac{\pi^2}6$.
""", r"$f(x)=\sum_{k\ge1}\frac{\Gamma(x+1)}{k^{x+1}}=\Gamma(x+1)\zeta(x+1)$.")
