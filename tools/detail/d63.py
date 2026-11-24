# Conversion « 6 étapes » — lot 3 : maths CCINP (vérifications numériques : numpy, sommes partielles, simulation).
D = {}

D['m-ccmp-27a'] = r"""**Étape 1 — Analyse de l'énoncé.** $\Omega\subset\mathbb R^m$ est ouvert, $f:\Omega\to\mathbb R$ est de classe $C^2$, et $f$ admet un **minimum local** en $a\in\Omega$. Il faut montrer que $\Delta f(a)=\sum_{i=1}^m\partial_i^2f(a)\ge0$.

**Étape 2 — Rappels du cours.**

> **Théorème — Dérivée d'une composée le long d'une droite.** Si $f$ est $C^k$ et $\varphi(t)=f(a+tv)$, alors $\varphi$ est $C^k$, avec $\varphi'(t)=\mathrm df_{a+tv}(v)$. En particulier, pour $v=e_i$ : $\varphi'(t)=\partial_if(a+te_i)$ et $\varphi''(t)=\partial_i^2f(a+te_i)$.

> **Théorème — Condition du premier ordre.** Si une fonction dérivable sur un intervalle ouvert admet un extremum local en un point, sa dérivée y est nulle.

> **Théorème — Taylor-Young à l'ordre 2.** Si $\varphi$ est $C^2$ au voisinage de 0, alors $\varphi(t)=\varphi(0)+\varphi'(0)t+\frac{\varphi''(0)}2t^2+o(t^2)$.

**Étape 3 — Stratégie.** On ramène le problème à une variable. Pour chaque direction $e_i$, la fonction $\varphi_i(t)=f(a+te_i)$ admet un minimum local en $0$. La formule de Taylor-Young montre alors que $\varphi_i''(0)\ge0$. Comme $\varphi_i''(0)=\partial_i^2f(a)$, il suffit de sommer sur $i$.

**Étape 4 — Résolution détaillée.**

**4.1 Restriction à une droite.** $\Omega$ est ouvert : il existe $r>0$ tel que $B(a,r)\subset\Omega$. Pour $i$ fixé et $|t|<r$, on pose $\varphi_i(t)=f(a+te_i)$. D'après le rappel, $\varphi_i$ est $C^2$ sur $]-r,r[$ et $\varphi_i''(0)=\partial_i^2f(a)$.

**4.2 Minimum de $\varphi_i$.** Il existe $\rho\in]0,r]$ tel que $f(x)\ge f(a)$ pour $\|x-a\|<\rho$. Donc $\varphi_i(t)\ge\varphi_i(0)$ pour $|t|<\rho$ : $0$ est un minimum local intérieur, d'où $\varphi_i'(0)=0$.

**4.3 Signe de $\varphi_i''(0)$.** Par Taylor-Young, avec $\varphi_i'(0)=0$ :
$$\varphi_i(t)-\varphi_i(0)=t^2\Big(\frac{\varphi_i''(0)}2+\varepsilon(t)\Big),\qquad\varepsilon(t)\xrightarrow[t\to0]{}0.$$
Supposons par l'absurde $\varphi_i''(0)<0$. Pour $t\neq0$ assez petit, la parenthèse est strictement négative, donc $\varphi_i(t)<\varphi_i(0)$, ce qui contredit le minimum. Donc $\partial_i^2f(a)\ge0$.

**4.4 Somme.** En sommant sur $i=1,\dots,m$ : $\Delta f(a)\ge0$.

**Étape 5 — Vérification.**

> **Vérification — Exemples.**
> - $f(x,y)=x^2+y^2$ a un minimum en $0$, avec $\Delta f(0)=4\ge0$.
> - $f(x,y)=x^2-y^2$ n'a pas de minimum en $0$ (point col), et l'on a $\partial_y^2f(0)=-2<0$ : c'est cohérent avec la contraposée de 4.3.
> - $f(x,y)=x^4+y^4$ a un minimum en $0$ avec $\Delta f(0)=0$ : l'inégalité est large, on ne peut pas espérer mieux.

- La réciproque est fausse : $f(x,y)=x^2-\frac12y^2$ vérifie $\Delta f(0)=1>0$ sans avoir de minimum en $0$. On a seulement une condition nécessaire.
- L'hypothèse « ouvert » sert à faire varier $t$ des deux côtés de $0$ (minimum intérieur). Au bord d'un fermé, le résultat peut tomber.

**Étape 6 — Conclusion.**
$$\boxed{f\ \text{minimum local en } a\ \Longrightarrow\ \forall i,\ \frac{\partial^2f}{\partial x_i^2}(a)\ge0\ \Longrightarrow\ \Delta f(a)\ge0}$$
Conséquence (principe du minimum) : une fonction $C^2$ telle que $\Delta f<0$ sur $\Omega$ n'a aucun minimum local dans $\Omega$.
===RÉPONSE===
Restriction aux droites $t\mapsto f(a+te_i)$ : minimum local, donc $\partial_i^2f(a)\ge0$ pour tout $i$, d'où $\Delta f(a)\ge0$."""

D['m-ccmp-27b'] = r"""**Étape 1 — Analyse de l'énoncé.** $E$ est un $\mathbb C$-espace vectoriel de dimension finie $n\ge1$, $u\in\mathcal L(E)$ et $p\in\mathbb C[X]$. Il faut déterminer $\mathrm{Sp}(p(u))$ en fonction de $\mathrm{Sp}(u)$. On s'attend à $\mathrm{Sp}(p(u))=p(\mathrm{Sp}\,u)$ : il faut prouver les deux inclusions.

**Étape 2 — Rappels du cours.**

> **Propriété — Morphisme d'évaluation.** $Q\mapsto Q(u)$ est un morphisme d'algèbres : $(QR)(u)=Q(u)\circ R(u)$ et $(Q+\lambda R)(u)=Q(u)+\lambda R(u)$.

> **Théorème — D'Alembert-Gauss.** Tout polynôme non constant de $\mathbb C[X]$ est scindé : $P=c\prod_j(X-\alpha_j)$.

> **Propriété — Spectre en dimension finie sur $\mathbb C$.** $\lambda\in\mathrm{Sp}\,u\iff u-\lambda\,\mathrm{id}$ non injectif $\iff\chi_u(\lambda)=0$. En particulier, $\mathrm{Sp}\,u\ne\emptyset$.

> **Propriété — Composée d'injections.** Une composée d'applications injectives est injective.

**Étape 3 — Stratégie.** Inclusion $\supset$ : un vecteur propre de $u$ pour $\lambda$ est vecteur propre de $p(u)$ pour $p(\lambda)$. Inclusion $\subset$ : pour $\mu\in\mathrm{Sp}(p(u))$, on factorise $p(X)-\mu$ sur $\mathbb C$. Alors $p(u)-\mu\,\mathrm{id}$ est une composée de $u-\alpha_j\mathrm{id}$, et comme elle n'est pas injective, l'un des facteurs ne l'est pas. On traite à part le cas où $p$ est constant.

**Étape 4 — Résolution détaillée.**

**4.1 Inclusion $p(\mathrm{Sp}\,u)\subset\mathrm{Sp}(p(u))$.** Soit $u(x)=\lambda x$ avec $x\neq0$. Par récurrence, $u^k(x)=\lambda^kx$. Pour $p=\sum a_kX^k$, on a donc $p(u)(x)=\sum a_k\lambda^kx=p(\lambda)x$, avec $x\neq0$.

**4.2 Inclusion réciproque, $p$ constant égal à $c$.** $p(u)=c\,\mathrm{id}$ a pour spectre $\{c\}$. Or $\mathrm{Sp}\,u\neq\emptyset$, et $c=p(\lambda)$ pour tout $\lambda\in\mathrm{Sp}\,u$.

**4.3 Inclusion réciproque, $\deg p=d\ge1$.** Soit $\mu\in\mathrm{Sp}(p(u))$. On écrit $p(X)-\mu=c\prod_{j=1}^d(X-\alpha_j)$ avec $c\neq0$. Par le morphisme d'évaluation,
$$p(u)-\mu\,\mathrm{id}=c\,(u-\alpha_1\mathrm{id})\circ\cdots\circ(u-\alpha_d\mathrm{id}).$$
Le membre de gauche n'est pas injectif, donc l'un des $u-\alpha_j\mathrm{id}$ ne l'est pas : $\alpha_j\in\mathrm{Sp}\,u$. Et $p(\alpha_j)-\mu=0$, donc $\mu=p(\alpha_j)\in p(\mathrm{Sp}\,u)$.

**Étape 5 — Vérification.**

> **Contrôle numérique.** Pour une matrice complexe aléatoire $U$ de taille 4 et $p=X^3-2X+1$, les valeurs propres de $U^3-2U+I$ coïncident, à $10^{-8}$ près, avec les $p(\lambda)$ pour $\lambda$ valeur propre de $U$.

> **Hypothèses — Rôle de $\mathbb C$.** Sur $\mathbb R$, l'inclusion $\mathrm{Sp}(p(u))\subset p(\mathrm{Sp}\,u)$ peut tomber. Pour la rotation $u$ d'angle $\frac\pi2$ du plan, $\mathrm{Sp}_{\mathbb R}u=\emptyset$, mais $u^2=-\mathrm{id}$ a pour valeur propre $-1$.

- Les **multiplicités** ne sont pas affirmées par cet énoncé, qui porte sur les ensembles. Sur $\mathbb C$, on a en fait $\chi_{p(u)}=\prod_\lambda(X-p(\lambda))^{m_\lambda}$ par trigonalisation, mais ce n'était pas demandé.

**Étape 6 — Conclusion.**
$$\boxed{\mathrm{Sp}\big(p(u)\big)=p(\mathrm{Sp}\,u)=\{p(\lambda):\lambda\in\mathrm{Sp}\,u\}\qquad(E\ \text{de dimension finie sur }\mathbb C)}$$
===RÉPONSE===
$\operatorname{Sp}(p(u))=p(\operatorname{Sp}u)$ (sur $\mathbb C$, en dimension finie)."""

D['m-ccmp-27c'] = r"""**Étape 1 — Analyse de l'énoncé.** Les données sont les suivantes :
- $X$ est une variable aléatoire discrète, réelle et **bornée** ;
- $h:\mathbb R\to\mathbb R$ est **croissante** et **strictement positive**.

Il faut montrer que $P(X\ge a)\le\dfrac{E(h(X))}{h(a)}$ pour tout réel $a$.

**Étape 2 — Rappels du cours.**

> **Propriété — Espérance d'une variable bornée.** Une variable aléatoire discrète bornée admet une espérance finie.

> **Propriété — Croissance et linéarité de l'espérance.** Si $Y\le Z$ (point par point) et si ces variables ont une espérance, alors $E(Y)\le E(Z)$. Pour une constante $c$, $E(cY)=cE(Y)$.

> **Formule — Indicatrice.** $E(\mathbf 1_A)=P(A)$.

**Étape 3 — Stratégie.** On établit une inégalité **point par point** entre l'indicatrice $\mathbf 1_{\{X\ge a\}}$ et $\frac{h(X)}{h(a)}$, en distinguant deux cas selon que $X\ge a$ ou non. Il suffit ensuite de prendre l'espérance des deux membres.

**Étape 4 — Résolution détaillée.**

**4.1 Existence des espérances.** On a $|X|\le M$, donc $0<h(X)\le h(M)$ par croissance de $h$. Ainsi $h(X)$ est bornée et admet une espérance. De même, $\mathbf 1_{\{X\ge a\}}$ est bornée et $E(\mathbf 1_{\{X\ge a\}})=P(X\ge a)$.

**4.2 Inégalité point par point.** Montrons que, pour tout $\omega$, $\mathbf 1_{\{X\ge a\}}(\omega)\le\frac{h(X(\omega))}{h(a)}$.
- Si $X(\omega)\ge a$ : $h(X(\omega))\ge h(a)>0$, donc le quotient vaut au moins $1$, qui est la valeur de l'indicatrice.
- Si $X(\omega)<a$ : l'indicatrice vaut $0$ et le quotient est strictement positif.

**4.3 Passage à l'espérance.** Par croissance et linéarité :
$$P(X\ge a)=E\big(\mathbf 1_{\{X\ge a\}}\big)\le E\Big(\frac{h(X)}{h(a)}\Big)=\frac{E(h(X))}{h(a)}.$$

**Étape 5 — Vérification.**

> **Contrôle par simulation.** Pour $X$ uniforme sur $\{-3,\dots,3\}$ et $a=2$, on a $P(X\ge2)\approx0{,}287$. Avec $h(x)=e^{0{,}7x}$, le majorant vaut environ $0{,}569$ ; avec $h(x)=x+4$ (positive là où vit $X$), il vaut environ $0{,}667$. L'inégalité est respectée dans les deux cas.

- Cas particuliers :
  - $h(x)=e^{tx}$ avec $t>0$ donne l'inégalité de Chernoff, $P(X\ge a)\le e^{-ta}E(e^{tX})$ ;
  - pour $X\ge0$, la fonction $h(x)=x$ (positive là où vit $X$) redonne l'inégalité de Markov ;
  - appliqué à $|X-E(X)|$ avec $h(x)=x^2$, l'argument donne Bienaymé-Tchebychev.
- L'hypothèse $h>0$ sert dans le cas $X<a$ et pour pouvoir diviser par $h(a)$. La croissance sert dans le cas $X\ge a$.

**Étape 6 — Conclusion.**
$$\boxed{\forall a\in\mathbb R,\qquad P(X\ge a)\le\frac{E\big(h(X)\big)}{h(a)}}$$
===RÉPONSE===
$\mathbf 1_{\{X\ge a\}}\le\frac{h(X)}{h(a)}$ point par point, puis on prend l'espérance (croissance et linéarité)."""

D['m-ccs-02'] = r"""**Étape 1 — Analyse de l'énoncé.** On étudie $S=\sum_{n\ge1}f_n$ avec $f_n(x)=\frac1n\arctan\frac xn$.
1. Il faut rappeler les théorèmes utiles.
2. Il faut montrer la convergence simple sur $\mathbb R$, puis que $S$ est $C^1$.
3. Il faut décider si la convergence est uniforme sur $\mathbb R_+$.

**Étape 2 — Rappels du cours.**

> **Théorème — Convergence normale.** Si $\sup_I|f_n|\le\alpha_n$ et si $\sum\alpha_n$ converge, alors $\sum f_n$ converge uniformément et absolument sur $I$.

> **Théorème — Dérivation terme à terme.** Si les $f_n$ sont $C^1$ sur $I$, si $\sum f_n$ converge simplement et si $\sum f_n'$ converge uniformément sur tout segment de $I$, alors $S$ est $C^1$ et $S'=\sum f_n'$.

> **Propriété — Critère de non-uniformité.** $\sum f_n$ converge uniformément sur $I$ si et seulement si $\sup_I|R_N|\to0$, où $R_N=\sum_{n>N}f_n$. Il suffit donc d'exhiber des points $x_N$ tels que $R_N(x_N)\not\to0$.

> **Formule — Majoration de l'arctangente.** $|\arctan u|\le|u|$ pour tout réel $u$ (accroissements finis, puisque $|\arctan'|\le1$).

**Étape 3 — Stratégie.** La convergence simple s'obtient par la majoration $|f_n(x)|\le\frac{|x|}{n^2}$. Les dérivées $f_n'(x)=\frac1{n^2+x^2}$ sont normalement dominées par $\frac1{n^2}$, ce qui donne $C^1$. Pour la non-uniformité, on évalue le reste $R_N$ au point mobile $x=2N$ et on le minore par $\frac\pi8$.

**Étape 4 — Résolution détaillée.**

**4.1 Convergence simple.** $|f_n(x)|\le\frac{|x|}{n^2}$, terme d'une série convergente pour $x$ fixé : la série converge absolument sur $\mathbb R$.

**4.2 Classe $C^1$.** $f_n'(x)=\frac1n\cdot\frac1n\cdot\frac1{1+x^2/n^2}=\frac1{n^2+x^2}$, donc $\sup_{\mathbb R}|f_n'|=\frac1{n^2}$. La série $\sum f_n'$ converge normalement sur $\mathbb R$. Par le théorème de dérivation, $S$ est $C^1$ et $S'(x)=\sum_{n\ge1}\frac1{n^2+x^2}$.

**4.3 Pas de convergence uniforme sur $\mathbb R_+$.** Pour $x\ge0$, tous les termes sont positifs. On minore $R_N(2N)$ par les termes $N+1\le n\le2N$. Pour ces $n$, $\frac{2N}n\ge1$, donc $\arctan\frac{2N}n\ge\frac\pi4$, et $\frac1n\ge\frac1{2N}$. D'où
$$R_N(2N)\ge N\cdot\frac1{2N}\cdot\frac\pi4=\frac\pi8.$$
Donc $\sup_{\mathbb R_+}|R_N|\ge\frac\pi8\not\to0$.

**Étape 5 — Vérification.**

> **Contrôle numérique.** En sommant les termes, $R_N(2N)\approx1{,}52$, $1{,}570$ et $1{,}574$ pour $N=10,100,1000$. On a bien $R_N(2N)\ge\frac\pi8\approx0{,}39$. En fait, $R_N(2N)$ tend vers $\int_1^{+\infty}\frac{\arctan(2/t)}t\,\mathrm dt\approx1{,}576$ (somme de Riemann).

- Sur un segment $[0,A]$, on a $|R_N(x)|\le A\sum_{n>N}\frac1{n^2}\to0$ : la convergence est uniforme sur tout segment. C'est pourquoi $S$ est bien continue, et même $C^1$.
- Autre preuve de la non-uniformité : chaque $f_n$ est bornée, mais $S(x)\ge\sum_{n\le N}f_n(x)\to\frac\pi2\sum_{n\le N}\frac1n$ quand $x\to+\infty$. Donc $S$ n'est pas bornée sur $\mathbb R_+$. Une limite uniforme de fonctions bornées serait bornée.

**Étape 6 — Conclusion.**
$$\boxed{S=\sum_{n\ge1}f_n\in\mathcal C^1(\mathbb R),\quad S'(x)=\sum_{n\ge1}\frac1{n^2+x^2}\,;\quad\text{pas de convergence uniforme sur }\mathbb R_+\ \big(R_N(2N)\ge\tfrac\pi8\big)}$$
===RÉPONSE===
$S\in\mathcal C^1(\mathbb R)$ avec $S'(x)=\sum\frac1{n^2+x^2}$ ; convergence non uniforme sur $\mathbb R_+$ car $R_N(2N)\ge\frac\pi8$."""

D['m-ccs-12'] = r"""**Étape 1 — Analyse de l'énoncé.** On note $q=1-p\in]0,1[$. Chaque élève passe l'examen jusqu'à sa réussite :
- $X_i$ est le nombre d'examens passés par l'élève $i$ ;
- les $X_i$ sont indépendantes ;
- $X=\sum_{i=1}^NX_i$.

Il faut :
1. rappeler la loi géométrique ;
2. (a) calculer $E(X)$ et $V(X)$ ; (b) calculer la fonction génératrice de $X_i$, puis la loi de $X$.

**Étape 2 — Rappels du cours.**

> **Définition — Loi géométrique.** $Y\sim\mathcal G(p)$ si $Y(\Omega)=\mathbb N^*$ et $P(Y=k)=q^{k-1}p$. C'est le rang du premier succès dans des épreuves de Bernoulli indépendantes. Elle vérifie $E(Y)=\frac1p$ et $V(Y)=\frac q{p^2}$.

> **Définition — Fonction génératrice.** $G_Y(s)=E(s^Y)=\sum_kP(Y=k)s^k$. Elle caractérise la loi : les coefficients du développement en série entière sont les probabilités.

> **Théorème — Somme de variables indépendantes.** Si $X_1,\dots,X_N$ sont indépendantes, alors $G_{X_1+\dots+X_N}=\prod G_{X_i}$, $E(\sum X_i)=\sum E(X_i)$ et $V(\sum X_i)=\sum V(X_i)$.

> **Formule — Série binomiale négative.** Pour $|u|<1$, $(1-u)^{-N}=\sum_{j\ge0}\binom{N+j-1}ju^j$ (dérivée $(N-1)$-ième de $\frac1{1-u}$).

**Étape 3 — Stratégie.** Pour l'espérance et la variance, on additionne, sans avoir besoin de la loi de $X$. Pour la loi, la fonction génératrice transforme la somme indépendante en produit. On développe $\big(\frac{ps}{1-qs}\big)^N$ en série entière et on lit les coefficients.

**Étape 4 — Résolution détaillée.**

**4.1 Loi géométrique.** On a $E(Y)=\sum_{k\ge1}kpq^{k-1}=\frac p{(1-q)^2}=\frac1p$, par la série dérivée $\sum kq^{k-1}=\frac1{(1-q)^2}$. De même $V(Y)=\frac q{p^2}$.

**4.2 Espérance et variance de $X$.** Chaque $X_i$ suit $\mathcal G(p)$ et les $X_i$ sont indépendantes. Donc
$$E(X)=\frac Np,\qquad V(X)=\sum_{i=1}^NV(X_i)=\frac{Nq}{p^2}.$$

**4.3 Fonction génératrice de $X_i$.** Pour $|s|<\frac1q$, on a $G_{X_i}(s)=\sum_{k\ge1}pq^{k-1}s^k=\dfrac{ps}{1-qs}$.

**4.4 Loi de $X$.** Par indépendance, $G_X(s)=\big(\frac{ps}{1-qs}\big)^N=p^Ns^N\sum_{j\ge0}\binom{N+j-1}j(qs)^j$. Par unicité des coefficients, avec $k=N+j$ et $\binom{k-1}{k-N}=\binom{k-1}{N-1}$, on obtient pour $k\ge N$ :
$$P(X=k)=\binom{k-1}{N-1}p^Nq^{k-N}.$$

**Étape 5 — Vérification.**

> **Contrôle numérique.** Pour $p=0{,}3$ et $N=4$, la loi trouvée a pour somme $1{,}0000$, pour espérance $13{,}333=\frac4{0{,}3}$ et pour variance $31{,}111=\frac{4\times0{,}7}{0{,}09}$, comme en 4.2.

- Cas $N=1$ : on retrouve $P(X=k)=q^{k-1}p$, la loi géométrique.
- Interprétation directe (loi de Pascal) : « $X=k$ » signifie que le $k$-ième examen est le $N$-ième succès. Parmi les $k-1$ précédents, il y a exactement $N-1$ succès, à placer de $\binom{k-1}{N-1}$ façons. Chaque configuration a pour probabilité $p^{N-1}q^{k-N}$, et le dernier succès apporte un facteur $p$.
- Valeurs possibles : $X\ge N$, puisque chaque élève passe au moins un examen. Les coefficients de $s^k$ pour $k<N$ sont bien nuls.

**Étape 6 — Conclusion.**
$$\boxed{\begin{aligned}&E(X)=\frac Np,\qquad V(X)=\frac{N(1-p)}{p^2},\qquad G_{X_i}(s)=\frac{ps}{1-(1-p)s}\\&\forall k\ge N,\quad P(X=k)=\binom{k-1}{N-1}p^N(1-p)^{k-N}\end{aligned}}$$
===RÉPONSE===
$E(X)=\frac Np$, $V(X)=\frac{Nq}{p^2}$, $G_{X_i}(s)=\frac{ps}{1-qs}$ et $P(X=k)=\binom{k-1}{N-1}p^Nq^{k-N}$ pour $k\ge N$ (loi de Pascal)."""
