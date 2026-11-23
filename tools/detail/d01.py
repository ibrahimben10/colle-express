D = {}

D['m-ccmp-01a'] = r"""
**Notations.** Pour $x\in E$, on note $\delta(x)=d(x,F)=\inf_{y\in F}\|x-y\|$, et pour $t\in[0,1]$, $g(t)=(1-t)a+tb$, de sorte que $f_{a,b}=\delta\circ g$.

**Rappel : distance nulle et adhérence.** $\delta(x)=0$ si et seulement si $x\in\overline F$.
- Si $\delta(x)=0$ : pour tout $n\ge1$, par définition de la borne inférieure, il existe $y_n\in F$ avec $\|x-y_n\|<\frac1n$. Donc $y_n\to x$ et $x\in\overline F$.
- Si $x\in\overline F$ : il existe $(y_n)\in F^{\mathbb N}$ avec $y_n\to x$, et $0\le\delta(x)\le\|x-y_n\|\to0$.

**Sens direct, étape 1 : $\delta$ est convexe si $F$ l'est.** Soient $x,y\in E$, $\lambda\in[0,1]$ et $\varepsilon>0$. Par définition de la borne inférieure, il existe $u\in F$ et $v\in F$ tels que
$$\|x-u\|\le\delta(x)+\varepsilon\qquad\text{et}\qquad\|y-v\|\le\delta(y)+\varepsilon.$$
$F$ étant convexe, $w=(1-\lambda)u+\lambda v\in F$. Donc, par définition de $\delta$ puis par l'inégalité triangulaire et l'homogénéité de la norme ($1-\lambda\ge0$, $\lambda\ge0$) :
$$\begin{aligned}\delta\big((1-\lambda)x+\lambda y\big)&\le\big\|(1-\lambda)x+\lambda y-w\big\|=\big\|(1-\lambda)(x-u)+\lambda(y-v)\big\|\\&\le(1-\lambda)\|x-u\|+\lambda\|y-v\|\\&\le(1-\lambda)\delta(x)+\lambda\delta(y)+\varepsilon.\end{aligned}$$
Ceci vaut pour tout $\varepsilon>0$ ; en faisant $\varepsilon\to0$ : $\delta\big((1-\lambda)x+\lambda y\big)\le(1-\lambda)\delta(x)+\lambda\delta(y)$. Ainsi $\delta$ est convexe.

**Sens direct, étape 2 : composition par une application affine.** Soient $s,t,\lambda\in[0,1]$. On calcule
$$g\big((1-\lambda)s+\lambda t\big)=\big(1-(1-\lambda)s-\lambda t\big)a+\big((1-\lambda)s+\lambda t\big)b.$$
En écrivant $1=(1-\lambda)+\lambda$, le coefficient de $a$ vaut $(1-\lambda)(1-s)+\lambda(1-t)$, donc
$$g\big((1-\lambda)s+\lambda t\big)=(1-\lambda)\big[(1-s)a+sb\big]+\lambda\big[(1-t)a+tb\big]=(1-\lambda)g(s)+\lambda g(t).$$
Par convexité de $\delta$ :
$$f_{a,b}\big((1-\lambda)s+\lambda t\big)=\delta\big((1-\lambda)g(s)+\lambda g(t)\big)\le(1-\lambda)f_{a,b}(s)+\lambda f_{a,b}(t).$$
Toutes les $f_{a,b}$ sont donc convexes.

**Réciproque.** On suppose toutes les $f_{a,b}$ convexes. Soient $a,b\in F$ et $t\in[0,1]$. Comme $a\in F$, $f_{a,b}(0)=\delta(a)=0$ ; de même $f_{a,b}(1)=\delta(b)=0$. La convexité appliquée entre $0$ et $1$ donne
$$0\le f_{a,b}(t)=f_{a,b}\big((1-t)\cdot0+t\cdot1\big)\le(1-t)f_{a,b}(0)+tf_{a,b}(1)=0.$$
Donc $\delta\big((1-t)a+tb\big)=0$, c'est-à-dire, d'après le rappel, $(1-t)a+tb\in\overline F$.

**Rôle de la fermeture.** On a seulement montré : $[a,b]\subset\overline F$ pour tous $a,b\in F$.
- Si $F$ est **fermé**, $\overline F=F$, donc $[a,b]\subset F$ : $F$ est convexe, et l'équivalence est démontrée.
- Sans cette hypothèse, l'équivalence est fausse. Contre-exemple : $E=\mathbb R$, $F=\mathbb Q$. Comme $\mathbb Q$ est dense, $\delta(x)=0$ pour tout $x$, donc toutes les $f_{a,b}$ sont nulles, donc convexes ; pourtant $\mathbb Q$ n'est pas convexe ($[0,2]\not\subset\mathbb Q$ car $\sqrt2\notin\mathbb Q$).

**Conclusion.** Pour $F$ fermé : $F$ convexe $\iff$ toutes les $f_{a,b}$ sont convexes. En général, la condition sur les $f_{a,b}$ équivaut à la convexité de $\overline F$ (le sens direct s'applique à $\overline F$, qui a la même fonction distance que $F$).
===RÉPONSE===
Équivalence vraie pour $F$ fermé ; en général, la condition équivaut à « $\overline F$ convexe » (contre-exemple : $F=\mathbb Q$).
"""

D['m-ccmp-01b'] = r"""
On note $p_n=P(X=n)$ pour $n\in\mathbb N$, de sorte que $p_{n+1}=\alpha p_n+\beta^{n+1}$, avec $\alpha>0$ et $\beta>0$.

**1. Expression de $p_n$ en fonction de $p_0$.** Montrons par récurrence que, pour tout $n\ge0$,
$$p_n=\alpha^np_0+\sum_{k=1}^{n}\alpha^{n-k}\beta^k\qquad(\text{somme vide nulle pour }n=0).$$
- Pour $n=0$, c'est $p_0=p_0$.
- Si c'est vrai au rang $n$ : $p_{n+1}=\alpha p_n+\beta^{n+1}=\alpha^{n+1}p_0+\sum_{k=1}^n\alpha^{n+1-k}\beta^k+\beta^{n+1}=\alpha^{n+1}p_0+\sum_{k=1}^{n+1}\alpha^{n+1-k}\beta^k$.

**1. Les paramètres sont dans $]0,1[$.** Comme $(p_n)$ est une loi de probabilité, $\sum p_n=1$ converge, donc $p_n\to0$.
- Tous les termes de la relation étant positifs, $p_{n}=\alpha p_{n-1}+\beta^{n}\ge\beta^n$ pour $n\ge1$. Si $\beta\ge1$, alors $p_n\ge1$ ne tend pas vers 0 : contradiction. Donc $\beta<1$.
- De même $p_1=\alpha p_0+\beta\ge\beta$, puis par récurrence $p_n\ge\alpha^{n-1}p_1\ge\alpha^{n-1}\beta$ (car $p_{n}\ge\alpha p_{n-1}$). Si $\alpha\ge1$, alors $p_n\ge\beta>0$ ne tend pas vers 0 : contradiction. Donc $\alpha<1$.

Ainsi $(\alpha,\beta)\in\,]0,1[^2$.

**1. Calcul de $p_0$ (normalisation).** On somme l'expression de $p_n$ ; tous les termes sont positifs, on peut donc intervertir les sommes :
$$\sum_{n\ge0}\sum_{k=1}^n\alpha^{n-k}\beta^k=\sum_{k\ge1}\beta^k\sum_{n\ge k}\alpha^{n-k}=\sum_{k\ge1}\beta^k\cdot\frac1{1-\alpha}=\frac{\beta}{(1-\alpha)(1-\beta)}.$$
Avec $\sum_n\alpha^np_0=\frac{p_0}{1-\alpha}$, la condition $\sum p_n=1$ s'écrit
$$\frac{p_0}{1-\alpha}+\frac{\beta}{(1-\alpha)(1-\beta)}=1\iff p_0=1-\alpha-\frac{\beta}{1-\beta}.$$
Il faut de plus $p_0\ge0$, c'est-à-dire $\beta\le(1-\alpha)(1-\beta)$ ; sous cette condition, tous les $p_n$ sont positifs et de somme 1 : c'est bien une loi.

**1. Forme explicite.** Si $\alpha\neq\beta$, la somme est géométrique de raison $\beta/\alpha$ :
$$\sum_{k=1}^n\alpha^{n-k}\beta^k=\alpha^n\sum_{k=1}^n\Big(\frac\beta\alpha\Big)^k=\alpha^n\cdot\frac\beta\alpha\cdot\frac{1-(\beta/\alpha)^n}{1-\beta/\alpha}=\beta\,\frac{\beta^n-\alpha^n}{\beta-\alpha}.$$
Donc $p_n=\alpha^np_0+\beta\dfrac{\beta^n-\alpha^n}{\beta-\alpha}$. Si $\alpha=\beta$, chaque terme vaut $\alpha^n$ et $p_n=\alpha^np_0+n\alpha^n$.

**2. Fonction génératrice.** Soit $G(s)=\sum_{n\ge0}p_ns^n$. D'après la forme explicite, $0\le p_n\le C\,n\,\mu^n$ avec $\mu=\max(\alpha,\beta)<1$ : le rayon de convergence est au moins $1/\mu>1$, donc $G$ est dérivable en $1$ et $E(X)=G'(1)$.

On multiplie la relation par $s^{n+1}$ et on somme sur $n\ge0$ (pour $|s|<1$) :
$$\sum_{n\ge0}p_{n+1}s^{n+1}=\alpha s\sum_{n\ge0}p_ns^n+\sum_{n\ge0}(\beta s)^{n+1}\iff G(s)-p_0=\alpha sG(s)+\frac{\beta s}{1-\beta s}.$$
D'où $G(s)=\dfrac{N(s)}{1-\alpha s}$ avec $N(s)=p_0+\dfrac{\beta s}{1-\beta s}$.

**2. Dérivation en 1.** On a $N(1)=p_0+\frac\beta{1-\beta}=1-\alpha$ et $N'(s)=\dfrac{\beta(1-\beta s)+\beta s\cdot\beta}{(1-\beta s)^2}=\dfrac{\beta}{(1-\beta s)^2}$, donc $N'(1)=\dfrac\beta{(1-\beta)^2}$. Par la dérivée d'un quotient :
$$G'(s)=\frac{N'(s)(1-\alpha s)+\alpha N(s)}{(1-\alpha s)^2}\quad\Longrightarrow\quad G'(1)=\frac{N'(1)}{1-\alpha}+\frac{\alpha N(1)}{(1-\alpha)^2}=\frac{\beta}{(1-\alpha)(1-\beta)^2}+\frac{\alpha}{1-\alpha}.$$

**Conclusion.** $E(X)=\dfrac{\alpha}{1-\alpha}+\dfrac{\beta}{(1-\alpha)(1-\beta)^2}$.
===RÉPONSE===
$(\alpha,\beta)\in]0,1[^2$, $p_0=1-\alpha-\frac{\beta}{1-\beta}$, $p_n=\alpha^np_0+\beta\frac{\beta^n-\alpha^n}{\beta-\alpha}$ ; $E(X)=\frac{\alpha}{1-\alpha}+\frac{\beta}{(1-\alpha)(1-\beta)^2}$.
"""

D['m-ccmp-02a'] = r"""
**Recherche de l'équation.** Pour $x\neq0$, posons $z(x)=xf(x)=\operatorname{sh}x$. D'une part $z''=\operatorname{sh}''=\operatorname{sh}=z$. D'autre part, en dérivant le produit :
$$z'=f+xf',\qquad z''=f'+f'+xf''=xf''+2f'.$$
L'égalité $z''=z$ s'écrit donc $xf''+2f'=xf$ : $f$ est solution de
$$(E)\qquad xy''+2y'-xy=0.$$

**Résolution sur $I=]0,+\infty[$ (ou $]-\infty,0[$).** Sur $I$, $x\neq0$ : $(E)$ équivaut à $y''+\frac2xy'-y=0$, équation linéaire à coefficients continus ; son espace de solutions est un plan vectoriel (théorème de Cauchy linéaire).

Soit $y$ deux fois dérivable sur $I$ et $z=xy$. Le même calcul qu'au-dessus donne $z''=xy''+2y'$, donc
$$y\text{ solution de }(E)\iff xy''+2y'=xy\iff z''=z\iff z=A\operatorname{ch}x+B\operatorname{sh}x\ \ (A,B\in\mathbb R).$$
Les solutions sur $I$ sont donc les $y=\dfrac{A\operatorname{ch}x+B\operatorname{sh}x}x$ ; c'est bien un plan, engendré par $\frac{\operatorname{ch}x}x$ et $\frac{\operatorname{sh}x}x$.

**Solutions sur $\mathbb R$ : condition nécessaire.** Soit $y$ de classe $C^2$ sur $\mathbb R$, solution de $(E)$. Sa restriction à $]0,+\infty[$ s'écrit $y=\frac{A\operatorname{ch}x+B\operatorname{sh}x}x$. Alors $xy(x)=A\operatorname{ch}x+B\operatorname{sh}x\to A$ quand $x\to0^+$ ; mais $y$ est continue en 0, donc $xy(x)\to0\cdot y(0)=0$. D'où $A=0$. De même sur $]-\infty,0[$ : $y=\frac{A'\operatorname{ch}x+B'\operatorname{sh}x}x$ avec $A'=0$.

Comme $\frac{\operatorname{sh}x}x\to1$ en 0, la continuité en 0 donne $B=\lim_{0^+}y=y(0)=\lim_{0^-}y=B'$. Donc $y(x)=B\dfrac{\operatorname{sh}x}x$ pour $x\neq0$ et $y(0)=B$.

**Solutions sur $\mathbb R$ : réciproque.** Soit $f$ prolongée par $f(0)=1$. Pour tout $x\in\mathbb R$, $\operatorname{sh}x=\sum_{k\ge0}\frac{x^{2k+1}}{(2k+1)!}$, donc $f(x)=\sum_{k\ge0}\frac{x^{2k}}{(2k+1)!}$ (vrai aussi en 0) : somme d'une série entière de rayon infini, $f$ est $C^\infty$ sur $\mathbb R$. Elle vérifie $(E)$ sur $\mathbb R^*$, et les deux membres de $(E)$ sont continus sur $\mathbb R$ : par passage à la limite en 0, $(E)$ est vraie aussi en 0.

**Conclusion.** Sur $]0,+\infty[$ et $]-\infty,0[$, les solutions forment un plan : $y=\frac{A\operatorname{ch}x+B\operatorname{sh}x}x$. Sur $\mathbb R$, elles forment une droite : $y=B\frac{\operatorname{sh}x}x$. Le point $x=0$, où le coefficient de $y''$ s'annule, fait chuter la dimension de 2 à 1.
"""
