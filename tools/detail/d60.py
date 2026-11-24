# Pilote « 6 étapes » : analyse, rappels, stratégie, résolution, vérification, conclusion.
# Calculs revérifiés par script (sympy / numérique) avant publication.
D = {}

D['m-ccmp-04c'] = r"""**Étape 1 — Analyse de l'énoncé.** On dispose de deux variables aléatoires $X$ et $Y$ :
- **indépendantes** ;
- de même loi géométrique $\mathcal G(p)$ avec $p\in\,]0,1[$ : $X(\Omega)=Y(\Omega)=\mathbb N^*$ et, en notant $q=1-p\in\,]0,1[$, $P(X=k)=P(Y=k)=pq^{k-1}$ pour $k\ge1$.

On cherche la loi de $S=X+Y$ (ensemble des valeurs prises et probabilités), puis $E(S)$ et $V(S)$.

**Étape 2 — Rappels du cours.**

> **Théorème — Formule des probabilités totales.** Si $(A_k)_{k\in I}$ est un système complet d'événements ($I$ fini ou dénombrable), alors pour tout événement $B$ : $P(B)=\sum_{k\in I}P(B\cap A_k)$.

> **Définition — Indépendance.** $X$ et $Y$ sont indépendantes si $P\big((X=i)\cap(Y=j)\big)=P(X=i)\,P(Y=j)$ pour tous $i,j$.

> **Propriété — Moments d'une somme.** L'espérance est linéaire. Si $X$ et $Y$ admettent un moment d'ordre 2 et sont indépendantes, alors $\mathrm{Cov}(X,Y)=0$ et $V(X+Y)=V(X)+V(Y)$. Pour $X\sim\mathcal G(p)$ : $E(X)=\frac1p$ et $V(X)=\frac q{p^2}$.

> **Formule — Séries entières dérivées.** Pour $|x|<1$ : $\displaystyle\sum_{m\ge1}mx^{m-1}=\frac1{(1-x)^2}$ et $\displaystyle\sum_{m\ge2}m(m-1)x^{m-2}=\frac2{(1-x)^3}$ (dérivation terme à terme de $\sum x^m$ sur son disque ouvert de convergence).

**Étape 3 — Stratégie.** Pour la loi de $S$, on découpe l'événement $(S=n)$ selon la valeur prise par $X$ (formule des probabilités totales), puis on factorise chaque terme grâce à l'indépendance : c'est un produit de convolution. Pour l'espérance et la variance, inutile d'utiliser la loi de $S$ : la linéarité et l'indépendance suffisent. On contrôlera ensuite le résultat en recalculant $E(S)$ à partir de la loi trouvée.

**Étape 4 — Résolution détaillée.**

**4.1 Valeurs prises par $S$.** $X$ et $Y$ prennent leurs valeurs dans $\mathbb N^*$, donc $S$ prend ses valeurs dans $\{2,3,4,\dots\}$. On verra que $P(S=n)>0$ pour tout $n\ge2$, donc $S(\Omega)=[\![2,+\infty[\![$.

**4.2 Loi de $S$.** Soit $n\ge2$. La famille $(X=k)_{k\ge1}$ est un système complet d'événements. Pour $k\ge1$,
$$(S=n)\cap(X=k)=(X=k)\cap(Y=n-k).$$
Si $k\ge n$, alors $n-k\le0$ n'est pas une valeur de $Y$ et cet événement est vide. Par la formule des probabilités totales, puis par indépendance :
$$P(S=n)=\sum_{k=1}^{n-1}P\big((X=k)\cap(Y=n-k)\big)=\sum_{k=1}^{n-1}P(X=k)\,P(Y=n-k).$$
Chaque terme vaut
$$pq^{k-1}\cdot pq^{(n-k)-1}=p^2q^{n-2},$$
qui ne dépend pas de $k$. La somme comporte $n-1$ termes, d'où
$$P(S=n)=(n-1)\,p^2q^{n-2}.$$

**4.3 Espérance.** $X$ et $Y$ admettent une espérance, égale à $\frac1p$. Par linéarité (l'indépendance n'est pas nécessaire ici) :
$$E(S)=E(X)+E(Y)=\frac2p.$$

**4.4 Variance.** $X$ et $Y$ admettent un moment d'ordre 2, de variance $\frac q{p^2}$, et sont indépendantes, donc $\mathrm{Cov}(X,Y)=0$ et
$$V(S)=V(X)+V(Y)+2\,\mathrm{Cov}(X,Y)=\frac{2q}{p^2}.$$

**Étape 5 — Vérification.**

> **Vérification — C'est bien une loi de probabilité.** Avec $m=n-1$ : $\displaystyle\sum_{n\ge2}(n-1)p^2q^{n-2}=p^2\sum_{m\ge1}mq^{m-1}=\frac{p^2}{(1-q)^2}=1$.

> **Vérification — Espérance recalculée à partir de la loi.** $\displaystyle E(S)=\sum_{n\ge2}n(n-1)p^2q^{n-2}=p^2\cdot\frac2{(1-q)^3}=\frac2p$ : on retrouve le résultat de 4.3.

- Cas particulier $n=2$ : $P(S=2)=P(X=1)P(Y=1)=p^2$, conforme à la formule.
- Cas limite $p\to1$ : chaque variable vaut 1 presque sûrement, donc $S=2$ ; la formule donne $E(S)\to2$ et $V(S)\to0$. Cohérent.
- Interprétation : $S$ est le rang du deuxième succès dans une suite d'épreuves de Bernoulli indépendantes de paramètre $p$ (loi de Pascal). Il faut en moyenne $\frac1p$ épreuves par succès, donc $\frac2p$ pour deux succès.

**Étape 6 — Conclusion.**
$$\boxed{\begin{aligned}&\forall n\ge2,\quad P(X+Y=n)=(n-1)\,p^2(1-p)^{n-2}\\&E(X+Y)=\frac2p,\qquad V(X+Y)=\frac{2(1-p)}{p^2}\end{aligned}}$$
===RÉPONSE===
$P(X+Y=n)=(n-1)p^2(1-p)^{n-2}$ pour $n\ge2$ ; $E(X+Y)=\frac2p$ ; $V(X+Y)=\frac{2(1-p)}{p^2}$."""

D['m-ccmp-03b'] = r"""**Étape 1 — Analyse de l'énoncé.** On pose $g(t)=\dfrac{\sin(\ln t)}t$ pour $t\ge1$, $u_n=g(n)$ et $v_n=\displaystyle\int_n^{n+1}g(t)\,\mathrm dt$.
1. On doit montrer que $\sum u_n$ et $\sum v_n$ sont de même nature : elles convergent toutes les deux ou divergent toutes les deux.
2. On doit en déduire la nature de $\sum u_n$, donc étudier $\sum v_n$, dont les sommes partielles se calculent explicitement.

**Étape 2 — Rappels du cours.**

> **Théorème — Inégalité des accroissements finis.** Si $g$ est de classe $C^1$ sur un intervalle $I$ et $|g'|\le M$ sur $I$, alors $|g(a)-g(b)|\le M|a-b|$ pour tous $a,b\in I$.

> **Théorème — Séries de Riemann et convergence absolue.** $\sum\frac1{n^2}$ converge. Si $|w_n|\le c_n$ et si $\sum c_n$ converge, alors $\sum w_n$ converge absolument, donc converge.

> **Propriété — Opérations sur les séries.** La somme de deux séries convergentes converge. La somme d'une série convergente et d'une série divergente diverge.

> **Théorème — Changement de variable.** Si $\varphi$ est $C^1$ sur $[a,b]$ et $f$ continue sur $\varphi([a,b])$, alors $\int_{\varphi(a)}^{\varphi(b)}f(t)\,\mathrm dt=\int_a^bf(\varphi(u))\varphi'(u)\,\mathrm du$.

> **Attention — Hypothèse de monotonie.** La comparaison série-intégrale « classique » ($\sum g(n)$ et $\int g$ de même nature) suppose $g$ **positive et décroissante**. Ici $g$ change de signe une infinité de fois : ce théorème ne s'applique pas.

**Étape 3 — Stratégie.** On contrôle l'écart $w_n=u_n-v_n$ à l'aide de $g'$ (inégalité des accroissements finis) au lieu de la monotonie. Si $\sum w_n$ converge absolument, alors $\sum u_n$ et $\sum v_n$ ont même nature. Ensuite, la relation de Chasles et le changement de variable $t=e^u$ donnent les sommes partielles de $\sum v_n$ sous forme exacte. On montre qu'elles n'ont pas de limite en exhibant deux suites extraites de limites différentes.

**Étape 4 — Résolution détaillée.**

**4.1 Majoration de $g'$.** $g$ est de classe $C^1$ sur $[1,+\infty[$ (quotient de fonctions $C^1$, dénominateur non nul). Comme $(\sin(\ln t))'=\frac{\cos(\ln t)}t$ :
$$g'(t)=\frac{\cos(\ln t)-\sin(\ln t)}{t^2},\qquad\text{donc}\qquad|g'(t)|\le\frac{|\cos(\ln t)|+|\sin(\ln t)|}{t^2}\le\frac2{t^2}.$$

**4.2 Majoration de $w_n$.** L'intervalle $[n,n+1]$ est de longueur 1, donc $u_n=g(n)=\int_n^{n+1}g(n)\,\mathrm dt$ et
$$w_n=u_n-v_n=\int_n^{n+1}\big(g(n)-g(t)\big)\,\mathrm dt.$$
Pour $t\in[n,n+1]$, l'inégalité des accroissements finis sur $[n,t]$, avec $|g'|\le\frac2{n^2}$ sur $[n,n+1]$, donne $|g(n)-g(t)|\le\frac2{n^2}(t-n)\le\frac2{n^2}$. Par croissance de l'intégrale, $|w_n|\le\dfrac2{n^2}$.

**4.3 Même nature.** $\sum\frac2{n^2}$ converge, donc $\sum w_n$ converge absolument, donc converge. Comme $u_n=v_n+w_n$ et $v_n=u_n-w_n$ :
- si $\sum v_n$ converge, $\sum u_n$ converge (somme de deux séries convergentes) ;
- si $\sum v_n$ diverge, $\sum u_n$ diverge (somme d'une divergente et d'une convergente).

Les deux séries sont donc de même nature, ce qui répond à la question 1.

**4.4 Sommes partielles de $\sum v_n$.** Pour $N\ge2$, par la relation de Chasles :
$$T_N=\sum_{n=1}^{N-1}v_n=\int_1^N\frac{\sin(\ln t)}t\,\mathrm dt.$$
Avec $\varphi(u)=e^u$, de classe $C^1$ de $[0,\ln N]$ sur $[1,N]$ et $\varphi'(u)=e^u$, on a $g(e^u)e^u=\sin u$, donc
$$T_N=\int_0^{\ln N}\sin u\,\mathrm du=1-\cos(\ln N).$$

**4.5 $(T_N)$ n'a pas de limite.** Pour $k\ge1$, posons $N_k=\lfloor e^{2k\pi}\rfloor$. Alors $N_k\le e^{2k\pi}<N_k+1$, d'où
$$0\le2k\pi-\ln N_k<\ln(N_k+1)-\ln N_k=\ln\Big(1+\frac1{N_k}\Big)\xrightarrow[k\to\infty]{}0.$$
Par $2\pi$-périodicité et continuité de $\cos$ : $\cos(\ln N_k)=\cos(\ln N_k-2k\pi)\to\cos0=1$, donc $T_{N_k}\to0$.

De même, avec $N'_k=\lfloor e^{(2k+1)\pi}\rfloor$ : $\cos(\ln N'_k)=-\cos\big(\ln N'_k-(2k+1)\pi\big)\to-1$, donc $T_{N'_k}\to2$.

$(N_k)$ et $(N'_k)$ sont strictement croissantes et tendent vers $+\infty$ : ce sont des suites extraites de $(T_N)$. Elles ont des limites différentes, donc $(T_N)$ n'a pas de limite et $\sum v_n$ diverge.

**Étape 5 — Vérification.**

> **Hypothèses — Vérifiées.** L'inégalité des accroissements finis est appliquée à une fonction $C^1$ sur un intervalle. Le changement de variable porte sur une fonction $C^1$ avec un intégrande continu. On n'a jamais utilisé la monotonie de $g$, qui est fausse.

> **Contrôle numérique.** D'après 4.3 et 4.4, $\sum_{n=1}^N u_n-T_N=\sum_{n=1}^{N-1}w_n+u_N$ converge (car $u_N\to0$), donc $\sum_{n\le N}\frac{\sin(\ln n)}n-\big(1-\cos(\ln N)\big)$ doit tendre vers une constante. Le calcul donne environ $-0{,}0729$, $-0{,}0731$, $-0{,}0732$, $-0{,}0732$ pour $N=10^3,10^4,10^5,10^6$, alors que les sommes partielles elles-mêmes valent environ $0{,}12$, $1{,}90$, $0{,}43$, $0{,}61$ : elles oscillent sans converger, comme prévu.

- L'oscillation est très lente : il faut multiplier $N$ par $e^{2\pi}\approx535$ pour faire un tour complet. C'est pourquoi un calcul numérique naïf pourrait faire croire à une convergence.

**Étape 6 — Conclusion.** Les séries $\sum\frac{\sin(\ln n)}n$ et $\sum\int_n^{n+1}\frac{\sin(\ln t)}t\,\mathrm dt$ sont de même nature, et
$$\boxed{\sum_{n\ge1}\frac{\sin(\ln n)}{n}\ \text{diverge}}$$
Ses sommes partielles valent $1-\cos(\ln N)$ à une suite convergente près : elles oscillent entre $0$ et $2$ environ, sans limite.
===RÉPONSE===
Les deux séries sont de même nature ; $\sum\frac{\sin(\ln n)}n$ **diverge** (sommes partielles égales à $1-\cos(\ln N)$ plus une suite convergente)."""

D['m-ccmp-04b'] = r"""**Étape 1 — Analyse de l'énoncé.** Les données sont les suivantes :
- $G$ est un sous-groupe **fini** de $GL_n(\mathbb C)$, de cardinal noté $N$ ;
- $G\cap SL_n(\mathbb C)=\{I_n\}$ : la seule matrice de $G$ de déterminant 1 est l'identité.

Il faut montrer que $G$ est **cyclique**, c'est-à-dire engendré par un seul élément.

**Étape 2 — Rappels du cours.**

> **Propriété — Morphisme déterminant.** $\det:GL_n(\mathbb C)\to\mathbb C^*$ est un morphisme de groupes ($\det(AB)=\det A\det B$), de noyau $SL_n(\mathbb C)$.

> **Théorème — Noyau et injectivité.** Un morphisme de groupes est injectif si et seulement si son noyau est réduit à l'élément neutre. Il induit alors un isomorphisme sur son image, qui est un sous-groupe du groupe d'arrivée.

> **Théorème — Lagrange.** Dans un groupe fini de cardinal $N$, l'ordre de tout élément divise $N$. En particulier $x^N=e$ pour tout élément $x$.

> **Propriété — Racines de l'unité.** $\mathbb U_N=\{z\in\mathbb C:z^N=1\}$ compte exactement $N$ éléments, les $e^{2ik\pi/N}$ pour $0\le k\le N-1$. C'est un groupe cyclique engendré par $\omega=e^{2i\pi/N}$.

**Étape 3 — Stratégie.** Le déterminant transporte $G$ dans $\mathbb C^*$, où les sous-groupes finis sont bien connus. L'hypothèse $G\cap SL_n(\mathbb C)=\{I_n\}$ signifie exactement que ce transport est injectif. On identifie donc $G$ à un sous-groupe fini de $\mathbb C^*$, on montre que c'est $\mathbb U_N$, et on revient à $G$ par l'isomorphisme.

**Étape 4 — Résolution détaillée.**

**4.1 Le déterminant est injectif sur $G$.** Soit $\varphi:G\to\mathbb C^*$, $M\mapsto\det M$, restriction à $G$ d'un morphisme de groupes : c'est un morphisme. Son noyau est
$$\ker\varphi=\{M\in G:\det M=1\}=G\cap SL_n(\mathbb C)=\{I_n\}.$$
Donc $\varphi$ est injectif. Directement : si $\det M=\det M'$, alors $\det(MM'^{-1})=1$ avec $MM'^{-1}\in G$, donc $MM'^{-1}=I_n$ et $M=M'$.

**4.2 L'image est un sous-groupe de cardinal $N$.** $H=\varphi(G)$ est un sous-groupe de $\mathbb C^*$ (image d'un groupe par un morphisme), et $\varphi$ réalise une bijection de $G$ sur $H$, donc $|H|=N$.

**4.3 $H=\mathbb U_N$.** Soit $z\in H$. Par le théorème de Lagrange dans le groupe $H$ de cardinal $N$, $z^N=1$, donc $z\in\mathbb U_N$. Ainsi $H\subset\mathbb U_N$, et les deux ensembles ont le même cardinal fini $N$ : $H=\mathbb U_N$.

**4.4 Retour à $G$.** Soit $g=\varphi^{-1}(\omega)$, l'unique élément de $G$ de déterminant $\omega=e^{2i\pi/N}$. Pour tout $M\in G$, $\varphi(M)\in\mathbb U_N$ s'écrit $\omega^k=\varphi(g^k)$ avec $k\in[\![0,N-1]\!]$. Par injectivité, $M=g^k$. Donc $G=\{g^k:0\le k\le N-1\}=\langle g\rangle$.

**Étape 5 — Vérification.**

> **Hypothèses — Rôle de chacune.** La **finitude** sert dans le théorème de Lagrange. Sans elle, le résultat est faux : le sous-groupe infini $\{2^a3^b:a,b\in\mathbb Z\}$ de $GL_1(\mathbb C)=\mathbb C^*$ rencontre $SL_1(\mathbb C)=\{1\}$ seulement en $1$, mais il est isomorphe à $\mathbb Z^2$ (unicité de la décomposition en facteurs premiers), qui n'est pas cyclique. L'hypothèse $G\cap SL_n=\{I_n\}$ sert à l'injectivité. Sans elle aussi, le résultat est faux : $\{\mathrm{diag}(\pm1,\pm1)\}\subset GL_2(\mathbb C)$ est fini et non cyclique (tous ses éléments sont d'ordre au plus 2, pour un cardinal 4), et il contient $\mathrm{diag}(-1,-1)\in SL_2$.

- Cas $n=1$ : $SL_1(\mathbb C)=\{1\}$, l'hypothèse est automatique et l'on retrouve le résultat classique « tout sous-groupe fini de $\mathbb C^*$ est cyclique ».
- Le générateur trouvé est d'ordre $N$ : $g^N=I_n$ car $\varphi(g^N)=\omega^N=1$, et $g^k\ne I_n$ pour $0<k<N$ car $\omega^k\ne1$.

**Étape 6 — Conclusion.**
$$\boxed{\begin{aligned}&G\ \text{est cyclique d'ordre } N=|G|,\\&\text{engendré par l'unique } g\in G \text{ tel que } \det g=e^{2i\pi/N},\\&\text{et } \det:G\to\mathbb U_N \text{ est un isomorphisme.}\end{aligned}}$$
===RÉPONSE===
$\det$ est injectif sur $G$ (son noyau est $G\cap SL_n=\{I_n\}$), donc $G\simeq\det(G)=\mathbb U_N$ : $G$ est cyclique."""

D['p-em-1'] = r"""**Étape 1 — Analyse de l'énoncé.** La distribution de charges est la suivante :
- un cylindre infini d'axe $(Oz)$, de rayon $b$ ;
- une charge volumique uniforme $\rho>0$ (en $\mathrm{C\,m^{-3}}$) dans le volume ;
- une charge surfacique uniforme $\sigma<0$ (en $\mathrm{C\,m^{-2}}$) sur la surface latérale $r=b$.

On cherche :
1. la relation entre $\sigma$, $\rho$ et $b$ traduisant la neutralité de toute portion de hauteur $H$ ;
2. le champ $\vec E(M)$ en un point à la distance $r$ de l'axe.

On se place en électrostatique, dans le vide ($\varepsilon_0$). Le cylindre « infini » idéalise un cylindre très long, observé loin de ses extrémités.

**Étape 2 — Rappels du cours.**

> **Théorème — Gauss.** Pour toute surface fermée $\Sigma$, $\displaystyle\oint_\Sigma\vec E\cdot\mathrm d\vec S=\frac{Q_{\mathrm{int}}}{\varepsilon_0}$, avec $\mathrm d\vec S$ orienté vers l'extérieur.

> **Principe — Curie (symétries).** Le champ électrique est un vecteur polaire : en un point d'un plan de symétrie de la distribution, $\vec E$ appartient à ce plan.

> **Propriété — Invariances.** Si la distribution est invariante par une translation ou une rotation, les composantes de $\vec E$ (dans une base adaptée) ne dépendent pas de la coordonnée correspondante.

> **Relation — Passage à la traversée d'une surface chargée.** $\vec E_2-\vec E_1=\dfrac\sigma{\varepsilon_0}\vec n_{1\to2}$.

**Étape 3 — Stratégie.** Question 1 : on écrit la charge totale d'une portion de hauteur $H$ (volume + surface) et on l'annule. Question 2 : la distribution est très symétrique. On détermine la direction de $\vec E$ par les plans de symétrie, puis ses dépendances par les invariances. Le théorème de Gauss, appliqué à un cylindre coaxial bien choisi, donne alors la norme. On distingue $r<b$ et $r>b$, et on contrôle le résultat par la relation de passage en $r=b$.

**Étape 4 — Résolution détaillée.**

**4.1 Neutralité.** Pour une portion de hauteur $H$, le volume vaut $\pi b^2H$ et l'aire latérale $2\pi bH$, d'où une charge totale $Q=\rho\,\pi b^2H+\sigma\,2\pi bH$. On a donc
$$Q=0\iff\sigma=-\frac{\rho b}2,$$
qui est bien négatif puisque $\rho>0$.

**4.2 Direction du champ.** En coordonnées cylindriques $(r,\theta,z)$, soit $M$ hors de l'axe.
- Le plan $(M,\vec u_r,\vec u_z)$, qui contient l'axe et $M$, est plan de symétrie de la distribution.
- Le plan $(M,\vec u_r,\vec u_\theta)$, perpendiculaire à l'axe, l'est aussi, car le cylindre est infini.

D'après le principe de Curie, $\vec E(M)$ appartient à l'intersection de ces deux plans : $\vec E(M)=E\,\vec u_r$.

**4.3 Variables.** La distribution est invariante par rotation autour de $(Oz)$ et par translation selon $(Oz)$ : $E$ ne dépend ni de $\theta$ ni de $z$. Donc $\vec E=E(r)\,\vec u_r$.

**4.4 Flux à travers un cylindre de Gauss.** On prend pour $\Sigma$ le cylindre fermé coaxial de rayon $r\ne b$ et de hauteur $H$.
- Sur les deux bases, $\mathrm d\vec S=\pm\mathrm dS\,\vec u_z\perp\vec E$ : le flux est nul.
- Sur la surface latérale, $\mathrm d\vec S=\mathrm dS\,\vec u_r$ et $E(r)$ est constant : le flux vaut $E(r)\cdot2\pi rH$.

Le théorème de Gauss donne donc $E(r)\cdot2\pi rH=\dfrac{Q_{\mathrm{int}}}{\varepsilon_0}$.

**4.5 Cas $r<b$.** Seule la charge volumique contenue dans le cylindre de rayon $r$ est intérieure : $Q_{\mathrm{int}}=\rho\pi r^2H$. Donc
$$E(r)=\frac{\rho\pi r^2H}{2\pi rH\,\varepsilon_0}=\frac{\rho r}{2\varepsilon_0}.$$

**4.6 Cas $r>b$.** $\Sigma$ contient toute la portion de hauteur $H$, charges volumique et surfacique comprises : $Q_{\mathrm{int}}=0$ d'après 4.1. Donc $E(r)=0$.

**Étape 5 — Vérification.**

> **Vérification — Relation de passage en $r=b$.** $E(b^+)-E(b^-)=0-\frac{\rho b}{2\varepsilon_0}=-\frac{\rho b}{2\varepsilon_0}=\frac\sigma{\varepsilon_0}$ avec $\vec n_{1\to2}=\vec u_r$ : conforme.

- Homogénéité : $\frac{\rho r}{\varepsilon_0}$ s'exprime en $\frac{\mathrm{C\,m^{-3}\cdot m}}{\mathrm{C\,V^{-1}\,m^{-1}}}=\mathrm{V\,m^{-1}}$. C'est bien un champ électrique.
- Sur l'axe ($r\to0$), $E\to0$ : c'est imposé par la symétrie, car tout plan contenant l'axe est plan de symétrie.
- Signe : pour $r<b$, le champ est radial sortant, ce qui est cohérent avec une charge intérieure positive.
- À l'extérieur, le champ est nul, comme celui d'un fil de charge linéique totale nulle.

> **Limite — Modèle surfacique.** Le champ n'est pas défini en $r=b$ exactement : c'est une conséquence du modèle de charge surfacique, d'épaisseur nulle, et non une réalité physique.

**Étape 6 — Conclusion.**
$$\boxed{\begin{aligned}&\sigma=-\frac{\rho b}2\\&\vec E(M)=\frac{\rho\,r}{2\varepsilon_0}\,\vec u_r\ \text{ si } r<b,\qquad \vec E(M)=\vec 0\ \text{ si } r>b\end{aligned}}$$
===RÉPONSE===
$\sigma=-\frac{\rho b}2$ ; $\vec E=\frac{\rho r}{2\varepsilon_0}\vec u_r$ pour $r<b$ et $\vec E=\vec0$ pour $r>b$."""

D['p-meca-4'] = r"""**Étape 1 — Analyse de l'énoncé.** Un point matériel $M$ de masse $m$ est lâché sans vitesse en $O$, à la latitude $\lambda$, dans un puits vertical. On l'étudie dans le **référentiel terrestre**, en rotation uniforme à $\Omega=\frac{2\pi}{86\,164}\ \mathrm{rad\,s^{-1}}$ (jour sidéral) par rapport au référentiel géocentrique, supposé galiléen.

Les axes sont $x$ vers l'est, $y$ vers le nord et $z$ vers le haut. On note $C=\cos\lambda$ et $S=\sin\lambda$.

Les forces sont le poids $m\vec g=-mg\,\vec u_z$ et la force de Coriolis $-2m\vec\Omega\wedge\vec v$.

> **Hypothèses — Du modèle.** On néglige les frottements de l'air et la variation de $\vec g$ avec l'altitude et la position, dont l'effet est de l'ordre de $h/R_T\approx6\times10^{-5}$ pour $h=400$ m. La chute est assez courte pour que $\vec\Omega$ garde la même expression dans la base locale.

**Étape 2 — Rappels du cours.**

> **Principe — Dynamique en référentiel non galiléen.** $m\vec a_{\mathcal R}=\sum\vec F+\vec f_{ie}+\vec f_{ic}$, avec $\vec f_{ie}=m\Omega^2\overrightarrow{HM}$ pour une rotation uniforme ($H$ projeté de $M$ sur l'axe) et $\vec f_{ic}=-2m\vec\Omega\wedge\vec v_{\mathcal R}$.

> **Définition — Poids.** Le poids mesuré au laboratoire est $m\vec g=m\vec{\mathcal G}+m\Omega^2\overrightarrow{HM}$ : il inclut l'attraction gravitationnelle **et** la force d'inertie d'entraînement.

> **Formule — Équation linéaire d'ordre 2.** Les solutions de $\ddot x+\omega^2x=at$ sont $x=A\cos\omega t+B\sin\omega t+\frac a{\omega^2}t$.

> **Formule — Développements limités en 0.** $\sin u=u-\frac{u^3}6+o(u^3)$ et $1-\cos u=\frac{u^2}2-\frac{u^4}{24}+o(u^4)$.

**Étape 3 — Stratégie.** On exprime $\vec\Omega$ dans la base locale, puis la force de Coriolis. Le principe fondamental de la dynamique donne trois équations couplées. Les deux dernières s'intègrent une fois grâce aux conditions initiales nulles, ce qui découple une équation en $x$ seul, linéaire à coefficients constants. On en déduit $x$, puis $y$ et $z$ par intégration. Enfin, on développe en puissances de $\Omega t\ll1$ pour dégager l'effet dominant.

**Étape 4 — Résolution détaillée.**

**4.1 Force d'inertie d'entraînement (question 1).** D'après le rappel sur le poids, la force d'inertie d'entraînement est déjà comprise dans $m\vec g$. L'écrire en plus la compterait deux fois. Seule la force de Coriolis reste à ajouter.

**4.2 Vecteur rotation (question 2).** $\vec\Omega$ est parallèle à l'axe des pôles, orienté du sud vers le nord. Dans le plan méridien de $O$, cet axe fait l'angle $\lambda$ avec l'horizontale dirigée vers le nord. Il n'a pas de composante est-ouest. Donc
$$\vec\Omega=\Omega\,(0,\ C,\ S).$$

**4.3 Équations du mouvement (question 3).** Avec $\vec v=(\dot x,\dot y,\dot z)$ :
$$\vec\Omega\wedge\vec v=\Omega\begin{pmatrix}C\dot z-S\dot y\\ S\dot x\\ -C\dot x\end{pmatrix},\qquad -2\vec\Omega\wedge\vec v=2\Omega\begin{pmatrix}S\dot y-C\dot z\\ -S\dot x\\ C\dot x\end{pmatrix}.$$
Le principe fondamental de la dynamique, divisé par $m$, donne
$$\begin{cases}\ddot x=2\Omega(S\dot y-C\dot z)\\ \ddot y=-2\Omega S\,\dot x\\ \ddot z=-g+2\Omega C\,\dot x\end{cases}$$
avec $x=y=z=0$ et $\dot x=\dot y=\dot z=0$ à $t=0$.

**4.4 Découplage (question 4).** On intègre les deux dernières équations entre $0$ et $t$ (conditions initiales nulles) :
$$\dot y=-2\Omega S\,x,\qquad\dot z=-gt+2\Omega C\,x.$$
On reporte dans la première, en utilisant $S^2+C^2=1$ :
$$\ddot x=2\Omega\big(-2\Omega S^2x+Cgt-2\Omega C^2x\big)\iff\ddot x+4\Omega^2x=2\Omega Cg\,t.$$

**4.5 Solution exacte.** La solution particulière affine est $\frac{2\Omega Cg}{4\Omega^2}t=\frac{Cg}{2\Omega}t$, donc $x=A\cos2\Omega t+B\sin2\Omega t+\frac{Cg}{2\Omega}t$.
- $x(0)=0$ donne $A=0$.
- $\dot x(0)=0$ donne $2\Omega B+\frac{Cg}{2\Omega}=0$, soit $B=-\frac{Cg}{4\Omega^2}$.

On obtient
$$x(t)=\frac{Cg}{4\Omega^2}\big(2\Omega t-\sin2\Omega t\big).$$
Avec $F(t)=\int_0^t\big(2\Omega s-\sin2\Omega s\big)\mathrm ds=\Omega t^2-\frac{1-\cos2\Omega t}{2\Omega}$, l'intégration de $\dot y$ et de $\dot z$ donne
$$y(t)=-\frac{SCg}{2\Omega}F(t),\qquad z(t)=-\frac{gt^2}2+\frac{C^2g}{2\Omega}F(t).$$

**4.6 Développements limités (question 5).** Avec $u=2\Omega t$ :
- $2\Omega t-\sin2\Omega t=\frac{(2\Omega t)^3}6+o(t^3)=\frac43\Omega^3t^3+o(t^3)$ ;
- $F(t)=\Omega t^2-\frac{1}{2\Omega}\Big(2\Omega^2t^2-\frac{2}{3}\Omega^4t^4\Big)+o(t^4)=\frac{\Omega^3t^4}3+o(t^4)$.

À l'ordre 3 en $\Omega t$ :
$$x(t)=\frac13\,\Omega g\cos\lambda\;t^3,\qquad y(t)=0,\qquad z(t)=-\frac{gt^2}2.$$
Les termes suivants, $y\approx-\frac{SCg\Omega^2t^4}6$ et la correction $\frac{C^2g\Omega^2t^4}6$ sur $z$, sont d'ordre 4.

**4.7 Pourquoi « déviation vers l'est ».** $x(t)>0$ dans les deux hémisphères, car $\cos\lambda>0$ pour $\lambda\in\,]-\frac\pi2,\frac\pi2[$. La déviation dominante est horizontale, vers l'est. Elle est d'ordre 1 en $\Omega t$ relativement à la chute $\frac{gt^2}2$. Elle est maximale à l'équateur et nulle aux pôles.

Interprétation dans le référentiel géocentrique : le point de départ, plus loin de l'axe de rotation que le fond du puits, a une vitesse vers l'est plus grande. Le corps conserve cette vitesse pendant la chute et « prend de l'avance » vers l'est.

**4.8 Application numérique (question 6).** Pour $h=400$ m : $t=\sqrt{2h/g}=\sqrt{800/9{,}81}\approx9{,}03$ s, et $t^3\approx736\ \mathrm{s^3}$.
- $\Omega\approx7{,}29\times10^{-5}\ \mathrm{rad\,s^{-1}}$, donc $\Omega t\approx6{,}6\times10^{-4}\ll1$ : le développement est justifié.
- À Paris ($\lambda\approx48{,}9^\circ$, $C\approx0{,}658$) : $x\approx\frac13\times7{,}29\times10^{-5}\times9{,}81\times0{,}658\times736\approx0{,}116$ m.
- À l'équateur : $x\approx0{,}176$ m.

**Étape 5 — Vérification.**

> **Vérification — Solution exacte.** Les expressions de $x,y,z$ ont été réinjectées dans le système de 4.3 par calcul formel : les trois équations et les six conditions initiales sont satisfaites.

- Homogénéité : $\Omega g t^3$ s'exprime en $\mathrm{s^{-1}\cdot m\,s^{-2}\cdot s^3}=\mathrm m$.
- Limite $\Omega\to0$ : $x\to0$, $y\to0$ et $z\to-\frac{gt^2}2$, c'est-à-dire la chute libre.
- Ordres de grandeur des effets négligés pour 400 m : $|y|\approx3\times10^{-5}$ m et la correction de $z$ vaut environ $2{,}5\times10^{-5}$ m, bien plus petits que les 12 cm de déviation. Le temps de chute n'est pas modifié de façon mesurable.

> **Limite — Validité du modèle.** Dans un vrai puits, la résistance de l'air diminue la vitesse et donc la déviation. Les expériences historiques de chute dans des puits de mine ont mesuré des déviations de quelques centimètres, compatibles avec ce modèle.

**Étape 6 — Conclusion.** Le corps est dévié vers l'est, et à l'ordre 3 en $\Omega t$ :
$$\boxed{\begin{aligned}x(t)&=\frac{Cg}{4\Omega^2}\big(2\Omega t-\sin2\Omega t\big)\approx\frac13\,\Omega g\cos\lambda\;t^3\ \text{(vers l'est)}\\x&\approx12\ \text{cm pour une chute de }400\ \text{m à Paris}\end{aligned}}$$
===RÉPONSE===
$x(t)=\frac{g\cos\lambda}{4\Omega^2}(2\Omega t-\sin2\Omega t)\approx\frac13\Omega g\cos\lambda\,t^3$ vers l'est ; environ 12 cm pour 400 m à Paris (18 cm à l'équateur)."""

D['c-thermo-1'] = r"""**Étape 1 — Analyse de l'énoncé.** La réaction étudiée est
$$4\,\mathrm{CuO_{(s)}}=2\,\mathrm{Cu_2O_{(s)}}+\mathrm{O_{2(g)}}.$$
On connaît la pression de dioxygène **à l'équilibre**, les deux solides étant présents, à deux températures :
- $T_1=1223$ K, $P_1=4660$ Pa ;
- $T_2=1323$ K, $P_2=29\,610$ Pa.

On suppose $\Delta_rH^\circ$ et $\Delta_rS^\circ$ indépendants de $T$ (approximation d'Ellingham). On cherche ces deux grandeurs.

**Étape 2 — Rappels du cours.**

> **Définition — Activités.** Un solide pur seul dans sa phase a une activité égale à 1. Un gaz parfait a pour activité $a=\frac P{P^\circ}$, avec $P^\circ=1\ \mathrm{bar}=10^5$ Pa.

> **Loi — Action des masses.** À l'équilibre, $\prod_ia_i^{\nu_i}=K^\circ(T)$, avec $\nu_i>0$ pour les produits.

> **Relation — Enthalpie libre standard.** $\Delta_rG^\circ(T)=-RT\ln K^\circ(T)$ et $\Delta_rG^\circ(T)=\Delta_rH^\circ-T\Delta_rS^\circ$.

> **Loi — Van 't Hoff.** $\dfrac{\mathrm d\ln K^\circ}{\mathrm dT}=\dfrac{\Delta_rH^\circ}{RT^2}$.

**Étape 3 — Stratégie.** La loi d'action des masses relie directement $K^\circ$ à la pression mesurée. En combinant les deux expressions de $\Delta_rG^\circ$, on obtient $\ln K^\circ=-\frac{\Delta_rH^\circ}{RT}+\frac{\Delta_rS^\circ}R$, une relation affine en $\frac1T$. Deux mesures déterminent les deux inconnues : la différence élimine $\Delta_rS^\circ$, puis on reporte.

**Étape 4 — Résolution détaillée.**

**4.1 Constante d'équilibre.** Les solides purs ont une activité de 1, donc
$$K^\circ(T)=\frac{a_{\mathrm{Cu_2O}}^2\,a_{\mathrm{O_2}}}{a_{\mathrm{CuO}}^4}=\frac{P_{\mathrm{O_2,eq}}}{P^\circ},\qquad K_1=\frac{4660}{10^5}=0{,}0466,\qquad K_2=\frac{29\,610}{10^5}=0{,}2961.$$

**4.2 Relation affine.** En égalant $-RT\ln K^\circ$ et $\Delta_rH^\circ-T\Delta_rS^\circ$ :
$$\ln K^\circ(T)=-\frac{\Delta_rH^\circ}{RT}+\frac{\Delta_rS^\circ}R.$$

**4.3 Enthalpie standard.** On écrit la relation de 4.2 en $T_2$ et en $T_1$, puis on soustrait :
$$\ln\frac{K_2}{K_1}=\frac{\Delta_rH^\circ}R\Big(\frac1{T_1}-\frac1{T_2}\Big)\iff\Delta_rH^\circ=\frac{R\ln(K_2/K_1)}{\frac1{T_1}-\frac1{T_2}}.$$
Les grandeurs intermédiaires valent :
- $\frac{K_2}{K_1}=6{,}354$, donc $\ln\frac{K_2}{K_1}=1{,}849$ ;
- $\frac1{T_1}-\frac1{T_2}=\frac{T_2-T_1}{T_1T_2}=\frac{100}{1\,618\,029}=6{,}180\times10^{-5}\ \mathrm{K^{-1}}$.

D'où
$$\Delta_rH^\circ=\frac{8{,}314\times1{,}849}{6{,}180\times10^{-5}}\approx2{,}487\times10^5\ \mathrm{J\,mol^{-1}}.$$

**4.4 Entropie standard.** On isole $\Delta_rS^\circ$ dans la relation de 4.2 écrite en $T_1$ : $\Delta_rS^\circ=\dfrac{\Delta_rH^\circ+RT_1\ln K_1}{T_1}$.
- $\ln K_1=-3{,}066$ et $RT_1=1{,}017\times10^4\ \mathrm{J\,mol^{-1}}$, donc $RT_1\ln K_1=-3{,}118\times10^4\ \mathrm{J\,mol^{-1}}$.

$$\Delta_rS^\circ=\frac{2{,}487\times10^5-3{,}118\times10^4}{1223}\approx178\ \mathrm{J\,K^{-1}\,mol^{-1}}.$$

**Étape 5 — Vérification.**

> **Vérification — Seconde mesure.** On recalcule $\ln K_2$ avec les valeurs trouvées : $-\frac{2{,}487\times10^5}{8{,}314\times1323}+\frac{177{,}9}{8{,}314}=-22{,}61+21{,}40=-1{,}217$, et $\ln(0{,}2961)=-1{,}217$. Les deux valeurs concordent.

- Signe de $\Delta_rH^\circ$ : il est positif, la réaction est endothermique. D'après la loi de Van 't Hoff, $K^\circ$ croît avec $T$, et c'est bien le cas expérimentalement ($K_2>K_1$).
- Signe et ordre de grandeur de $\Delta_rS^\circ$ : il est positif, car il se forme une mole de gaz à partir de solides ($\Delta_r\nu_{\mathrm{gaz}}=+1$). Sa valeur est proche de l'entropie molaire standard de $\mathrm O_2$ (environ $205\ \mathrm{J\,K^{-1}\,mol^{-1}}$), ce qui est attendu.
- Cohérence : la température d'inversion, où $K^\circ=1$, vaut $T_i=\frac{\Delta_rH^\circ}{\Delta_rS^\circ}\approx1398$ K. Elle est supérieure à $T_1$ et $T_2$, ce qui est cohérent avec $K_1,K_2<1$.

> **Limite — Précision.** Les résultats dépendent de l'approximation d'Ellingham et de deux mesures seulement, prises à 100 K d'écart. On les donne à 3 chiffres significatifs, pas davantage.

**Étape 6 — Conclusion.**
$$\boxed{\begin{aligned}\Delta_rH^\circ&\approx+249\ \mathrm{kJ\,mol^{-1}}\\\Delta_rS^\circ&\approx+178\ \mathrm{J\,K^{-1}\,mol^{-1}}\end{aligned}}$$
===RÉPONSE===
$\Delta_rH^\circ\approx+249\ \mathrm{kJ\,mol^{-1}}$ (réaction endothermique) et $\Delta_rS^\circ\approx+178\ \mathrm{J\,K^{-1}\,mol^{-1}}$."""
