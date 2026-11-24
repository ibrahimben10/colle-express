# Conversion « 6 étapes » — lot 1 : maths CCINP (calculs revérifiés : sympy / numpy / quadrature).
D = {}

D['m-ccmp-02a'] = r"""**Étape 1 — Analyse de l'énoncé.** On pose $f(x)=\dfrac{\operatorname{sh}x}x$, défini pour $x\neq0$ et prolongeable par continuité en $0$ par $f(0)=1$.
1. On cherche une équation différentielle **linéaire d'ordre 2 à coefficients polynomiaux** dont $f$ est solution.
2. On la résout complètement : d'abord sur les intervalles où le coefficient de $y''$ ne s'annule pas, puis sur $\mathbb R$, en étudiant le raccord en $0$.

**Étape 2 — Rappels du cours.**

> **Théorème — Cauchy-Lipschitz linéaire.** Si $a,b,c$ sont continues sur un intervalle $I$, l'ensemble des solutions de $y''+a(x)y'+b(x)y=c(x)$ sur $I$ est non vide. Pour $c=0$, c'est un plan vectoriel, et une solution est déterminée par $(y(x_0),y'(x_0))$.

> **Formule — Équation $z''=z$.** Ses solutions sur un intervalle sont les $z=A\operatorname{ch}x+B\operatorname{sh}x$, avec $(A,B)\in\mathbb R^2$.

> **Propriété — Séries entières.** La somme d'une série entière de rayon $R>0$ est de classe $C^\infty$ sur $]-R,R[$. En particulier $\operatorname{sh}x=\sum_{k\ge0}\frac{x^{2k+1}}{(2k+1)!}$ pour tout $x\in\mathbb R$.

> **Attention — Point singulier.** En $x=0$, le coefficient de $y''$ s'annule. Le théorème de Cauchy-Lipschitz ne s'applique pas sur un intervalle contenant $0$ : la dimension de l'espace des solutions peut y changer.

**Étape 3 — Stratégie.** La fonction $z=xf=\operatorname{sh}$ vérifie $z''=z$. En dérivant $z=xy$, on traduit cette relation en une équation sur $y$. Le même changement d'inconnue $z=xy$ résout l'équation sur $]0,+\infty[$ et $]-\infty,0[$. Sur $\mathbb R$, on cherche les solutions qui se recollent en $0$ : on en déduit des conditions nécessaires, puis on vérifie la réciproque.

**Étape 4 — Résolution détaillée.**

**4.1 Une équation vérifiée par $f$.** Pour $x\neq0$, posons $z(x)=xf(x)=\operatorname{sh}x$. D'une part $z''=\operatorname{sh}=z$. D'autre part, par dérivation d'un produit :
$$z'=f+xf',\qquad z''=2f'+xf''.$$
L'égalité $z''=z$ s'écrit donc $xf''+2f'=xf$ : $f$ est solution sur $\mathbb R^*$ de
$$(E)\qquad xy''+2y'-xy=0.$$

**4.2 Résolution sur $I=]0,+\infty[$ ou $I=]-\infty,0[$.** Sur $I$, $(E)$ équivaut à $y''+\frac2xy'-y=0$, à coefficients continus : son espace de solutions est un plan. Pour $y$ deux fois dérivable sur $I$ et $z=xy$, le calcul de 4.1 donne $z''=xy''+2y'$, donc
$$y\text{ solution de }(E)\iff z''=z\iff z=A\operatorname{ch}x+B\operatorname{sh}x\iff y=\frac{A\operatorname{ch}x+B\operatorname{sh}x}x,\quad(A,B)\in\mathbb R^2.$$

**4.3 Sur $\mathbb R$ : conditions nécessaires.** Soit $y$ de classe $C^2$ sur $\mathbb R$, solution de $(E)$. Sur $]0,+\infty[$, $y=\frac{A\operatorname{ch}x+B\operatorname{sh}x}x$, donc $xy(x)=A\operatorname{ch}x+B\operatorname{sh}x\xrightarrow[x\to0^+]{}A$. Or $y$ est continue en $0$, donc $xy(x)\to0\cdot y(0)=0$, et $A=0$. De même, sur $]-\infty,0[$, $y=\frac{A'\operatorname{ch}x+B'\operatorname{sh}x}x$ avec $A'=0$. Comme $\frac{\operatorname{sh}x}x\to1$ en $0$, la continuité de $y$ en $0$ impose $B=y(0)=B'$. Ainsi $y=B\,f$ (avec $f(0)=1$).

**4.4 Réciproque.** Pour tout $x\in\mathbb R$, $f(x)=\sum_{k\ge0}\frac{x^{2k}}{(2k+1)!}$ (vrai aussi en $0$). C'est la somme d'une série entière de rayon infini, donc $f$ est $C^\infty$ sur $\mathbb R$. Elle vérifie $(E)$ sur $\mathbb R^*$. Le membre de gauche de $(E)$, évalué en $f$, est continu sur $\mathbb R$ et nul sur $\mathbb R^*$ : il est nul en $0$ par continuité. Donc toutes les fonctions $Bf$ sont solutions sur $\mathbb R$.

**Étape 5 — Vérification.**

> **Vérification — Calcul formel.** En reportant $\frac{\operatorname{sh}x}x$ et $\frac{\operatorname{ch}x}x$ dans $xy''+2y'-xy$, on obtient bien $0$ dans les deux cas.

- En $0$, $(E)$ donne $2y'(0)=0$. Or $f$ est paire, donc $f'(0)=0$ : c'est cohérent.
- La solution $\frac{\operatorname{ch}x}x$ tend vers $\pm\infty$ en $0$ : il est normal qu'elle disparaisse sur $\mathbb R$.
- Dimension : un plan sur chaque demi-droite, mais seulement une droite sur $\mathbb R$. C'est l'effet attendu du point singulier $x=0$ (encadré Attention).

**Étape 6 — Conclusion.**
$$\boxed{\begin{aligned}&(E):\ xy''+2y'-xy=0\\&\text{sur }]0,+\infty[\text{ ou }]-\infty,0[:\ y=\frac{A\operatorname{ch}x+B\operatorname{sh}x}x\\&\text{sur }\mathbb R:\ y=B\,\frac{\operatorname{sh}x}x\ (\text{prolongée par } y(0)=B)\end{aligned}}$$
===RÉPONSE===
$xy''+2y'-xy=0$ ; sur chaque demi-droite $y=\frac{A\operatorname{ch}x+B\operatorname{sh}x}x$ ; sur $\mathbb R$ : $y=B\,\frac{\operatorname{sh}x}{x}$."""

D['m-ccmp-06a'] = r"""**Étape 1 — Analyse de l'énoncé.** Soit $A\in\mathcal M_n(\mathbb R)$ et $\varphi:M\mapsto AMA$ sur $\mathcal M_n(\mathbb R)$, espace de dimension $n^2$.
1. Il faut vérifier que $\varphi$ est linéaire, puis montrer l'équivalence : $A$ nilpotente $\iff$ $\varphi$ nilpotent.
2. Il faut montrer que si $A$ est diagonalisable, alors $\varphi$ l'est aussi.

**Étape 2 — Rappels du cours.**

> **Définition — Nilpotence.** Un endomorphisme $u$ (ou une matrice) est nilpotent s'il existe $k\ge1$ tel que $u^k=0$.

> **Définition — Diagonalisabilité.** Un endomorphisme d'un espace de dimension finie est diagonalisable s'il existe une base formée de vecteurs propres.

> **Propriété — Base canonique et conjugaison.** Les $E_{ij}$ (un seul coefficient non nul, égal à 1, en position $(i,j)$) forment une base de $\mathcal M_n(\mathbb R)$. Pour $P\in GL_n(\mathbb R)$, $M\mapsto PMP^{-1}$ est un automorphisme, donc il transforme une base en base.

> **Formule — Produits par une matrice diagonale.** Si $D=\mathrm{diag}(d_1,\dots,d_n)$, alors $DE_{ij}=d_iE_{ij}$ et $E_{ij}D=d_jE_{ij}$.

**Étape 3 — Stratégie.** Question 1 : on calcule les puissances de $\varphi$, $\varphi^k(M)=A^kMA^k$, ce qui transfère la nilpotence dans les deux sens (en testant sur $M=I_n$ pour le sens réciproque). Question 2 : on construit explicitement une base de vecteurs propres de $\varphi$, en transportant la base canonique par la matrice de passage qui diagonalise $A$.

**Étape 4 — Résolution détaillée.**

**4.1 $\varphi$ est un endomorphisme.** Pour $M,N\in\mathcal M_n(\mathbb R)$ et $\lambda\in\mathbb R$, par distributivité du produit matriciel :
$$\varphi(\lambda M+N)=A(\lambda M+N)A=\lambda AMA+ANA=\lambda\varphi(M)+\varphi(N),$$
et $\varphi(M)\in\mathcal M_n(\mathbb R)$.

**4.2 Puissances de $\varphi$.** Par récurrence sur $k\ge0$ : $\varphi^0(M)=M=A^0MA^0$ et, si $\varphi^k(M)=A^kMA^k$, alors
$$\varphi^{k+1}(M)=A(A^kMA^k)A=A^{k+1}MA^{k+1}.$$

**4.3 Équivalence des nilpotences.**
- Si $A^k=0$ avec $k\ge1$, alors $\varphi^k(M)=0$ pour tout $M$, donc $\varphi^k=0$.
- Si $\varphi^k=0$ avec $k\ge1$, alors $0=\varphi^k(I_n)=A^kA^k=A^{2k}$, donc $A$ est nilpotente.

**4.4 Base adaptée (question 2).** Soit $A=PDP^{-1}$ avec $P\in GL_n(\mathbb R)$ et $D=\mathrm{diag}(d_1,\dots,d_n)$. Les matrices $F_{ij}=PE_{ij}P^{-1}$, $1\le i,j\le n$, forment une base de $\mathcal M_n(\mathbb R)$ (image de la base canonique par un automorphisme).

**4.5 Ce sont des vecteurs propres.** Comme $P^{-1}P=I_n$ :
$$\varphi(F_{ij})=PDP^{-1}\,PE_{ij}P^{-1}\,PDP^{-1}=P\,(DE_{ij}D)\,P^{-1}=d_id_j\,PE_{ij}P^{-1}=d_id_j\,F_{ij}.$$
Les $F_{ij}$ sont non nuls (images d'éléments non nuls par un automorphisme) : ce sont des vecteurs propres, de valeurs propres $d_id_j$.

**Étape 5 — Vérification.**

> **Vérification — Spectre sur un exemple.** Pour une matrice $A$ semblable à $\mathrm{diag}(1,2,-3)$, la matrice de $\varphi$ (de taille $9$) a pour valeurs propres $-6,-6,-3,-3,1,2,2,4,9$. Ce sont exactement les produits $d_id_j$, comptés avec multiplicité.

- Cas $A=I_n$ : $\varphi=\mathrm{id}$, valeur propre $1$ de multiplicité $n^2$, et les $d_id_j$ valent tous $1$ : cohérent.
- Exemple pour la question 1 : avec $A=E_{12}=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, nilpotente, on a $\varphi(E_{21})=E_{12}E_{21}E_{12}=E_{12}\neq0$ mais $\varphi^2(M)=A^2MA^2=0$ : $\varphi$ est nilpotent non nul, donc non diagonalisable. Cela confirme que l'hypothèse « $A$ diagonalisable » ne peut pas être supprimée en question 2.

**Étape 6 — Conclusion.**
$$\boxed{\begin{aligned}&\varphi^k(M)=A^kMA^k,\ \text{ donc } A \text{ nilpotente}\iff\varphi \text{ nilpotent}\\&A=PDP^{-1}\ \Rightarrow\ \varphi(PE_{ij}P^{-1})=d_id_j\,PE_{ij}P^{-1}:\ \varphi \text{ est diagonalisable, de valeurs propres } d_id_j\end{aligned}}$$
===RÉPONSE===
$\varphi^k(M)=A^kMA^k$ (d'où l'équivalence des nilpotences) ; si $A=PDP^{-1}$, les $PE_{ij}P^{-1}$ sont propres pour $\varphi$ (valeurs propres $d_id_j$) : $\varphi$ est diagonalisable."""

D['m-ccmp-08b'] = r"""**Étape 1 — Analyse de l'énoncé.** Soit $x\in[0,1]$ fixé. Il faut :
- vérifier que le terme général $\ln\big(\cos\frac x{2^n}\big)$ est défini ;
- montrer que la série converge ;
- calculer sa somme.

Le cas $x=0$ (tous les termes nuls) sera traité à part.

**Étape 2 — Rappels du cours.**

> **Théorème — Comparaison des séries de signe constant.** Si $u_n\le0$, $v_n\le0$ et $u_n\sim v_n$, alors $\sum u_n$ et $\sum v_n$ sont de même nature.

> **Formule — Équivalents usuels en 0.** $1-\cos u\sim\frac{u^2}2$, $\ln(1+h)\sim h$ et $\sin u\sim u$.

> **Formule — Duplication.** $\sin2a=2\sin a\cos a$ pour tout réel $a$.

> **Propriété — Somme et produit.** $\sum_{n=0}^N\ln a_n=\ln\prod_{n=0}^Na_n$ pour $a_n>0$. Si le produit tend vers $\ell>0$, la série converge vers $\ln\ell$ (continuité de $\ln$).

**Étape 3 — Stratégie.** La convergence se montre par un équivalent du terme général. Pour la somme, on passe au produit $P_N=\prod\cos\frac x{2^k}$, qui **télescope** grâce à la formule de duplication écrite sous la forme $\cos a=\frac{\sin2a}{2\sin a}$. On prend ensuite la limite.

**Étape 4 — Résolution détaillée.**

**4.1 Définition du terme général.** Pour $n\ge0$, $0\le\frac x{2^n}\le1<\frac\pi2$, donc $\cos\frac x{2^n}>0$ et le logarithme est défini.

**4.2 Convergence.** Si $x=0$, tous les termes sont nuls. Soit $x\in]0,1]$ et $u_n=\frac x{2^n}\to0$. Comme $\cos u_n-1\to0$ :
$$\ln\cos u_n=\ln\big(1+(\cos u_n-1)\big)\sim\cos u_n-1\sim-\frac{u_n^2}2=-\frac{x^2}2\cdot\frac1{4^n}.$$
Les termes sont négatifs ($\cos u_n\le1$), et $\sum\frac1{4^n}$ est géométrique de raison $\frac14<1$, donc convergente. Par comparaison, la série converge.

**4.3 Produit télescopique.** Pour $k\ge0$, $0<\frac x{2^k}<\pi$, donc $\sin\frac x{2^k}\neq0$. La duplication avec $a=\frac x{2^k}$ donne
$$\cos\frac x{2^k}=\frac{\sin\frac x{2^{k-1}}}{2\sin\frac x{2^k}}.$$
Pour $N\ge0$, en multipliant de $k=0$ à $N$, les sinus intermédiaires se simplifient :
$$P_N=\prod_{k=0}^N\cos\frac x{2^k}=\frac1{2^{N+1}}\cdot\frac{\sin2x}{\sin\frac x{2^N}}=\frac{\sin2x}{2\cdot2^N\sin\frac x{2^N}}.$$

**4.4 Limite.** Comme $\sin u\sim u$ en 0, $2^N\sin\frac x{2^N}\sim2^N\cdot\frac x{2^N}=x$, donc $P_N\to\frac{\sin2x}{2x}$. Or $0<2x\le2<\pi$, donc $\sin2x>0$ : la limite est strictement positive, et
$$\sum_{n=0}^N\ln\cos\frac x{2^n}=\ln P_N\xrightarrow[N\to\infty]{}\ln\frac{\sin2x}{2x}.$$

**Étape 5 — Vérification.**

> **Contrôle numérique.** Pour $x=0{,}3$, la somme des 60 premiers termes vaut $-0{,}0607369\ldots$ et $\ln\frac{\sin0{,}6}{0{,}6}=-0{,}0607369\ldots$. Pour $x=1$ : $-0{,}7882302\ldots$ dans les deux cas.

- Cas limite : $\ln\frac{\sin2x}{2x}\to\ln1=0$ quand $x\to0$, ce qui raccorde la formule au cas $x=0$.
- Signe : la somme est négative, comme chaque terme. On a bien $\frac{\sin2x}{2x}<1$.
- Hypothèse $x\le1$ : elle garantit $\cos x>0$, donc le premier terme est défini, et $\sin2x>0$. Pour $x$ proche de $\frac\pi2$, $\cos x\to0$ et le premier terme tend vers $-\infty$.

**Étape 6 — Conclusion.**
$$\boxed{\forall x\in\,]0,1],\quad\sum_{n=0}^{+\infty}\ln\Big(\cos\frac x{2^n}\Big)=\ln\frac{\sin2x}{2x}\qquad(\text{et }0\text{ pour }x=0)}$$
===RÉPONSE===
La série converge et $\sum_{n\ge0}\ln\cos\frac x{2^n}=\ln\frac{\sin2x}{2x}$ (et $0$ si $x=0$)."""

D['m-ccmp-13a'] = r"""**Étape 1 — Analyse de l'énoncé.** On se donne $a>0$ avec $a\neq1$, et $A=(a^i+a^j)_{1\le i,j\le n}$, matrice **symétrique réelle**. Il faut calculer son rang et son polynôme caractéristique $\chi_A=\det(XI_n-A)$.

**Étape 2 — Rappels du cours.**

> **Propriété — Matrices de rang 1.** Pour des colonnes $u,v\in\mathbb R^n$, la matrice $uv^\top$ a pour coefficient $(i,j)$ le produit $u_iv_j$, et $(uv^\top)x=u\,(v^\top x)$.

> **Théorème — Inégalité de Cauchy-Schwarz.** $(v^\top u)^2\le(v^\top v)(u^\top u)$, avec égalité si et seulement si $u$ et $v$ sont colinéaires.

> **Propriété — Matrice diagonale par blocs.** Si $\mathbb R^n=F\oplus G$ avec $F,G$ stables par $A$, alors $\chi_A=\chi_{A_F}\,\chi_{A_G}$.

**Étape 3 — Stratégie.** On écrit $A$ comme somme de deux matrices de rang 1. Son image est alors contenue dans un plan $P=\mathrm{Vect}(u,v)$. On calcule l'endomorphisme induit sur $P$, on montre qu'il est inversible (Cauchy-Schwarz), on identifie le noyau, et on lit $\chi_A$ dans une base adaptée à $\mathbb R^n=P\oplus\ker A$.

**Étape 4 — Résolution détaillée.**

**4.1 Écriture de $A$.** Soit $u=(a,a^2,\dots,a^n)^\top$ et $v=(1,\dots,1)^\top$. On note $S_1=\sum_{i=1}^na^i=v^\top u$, $S_2=\sum_{i=1}^na^{2i}=u^\top u$, et $v^\top v=n$. Les coefficients $(i,j)$ de $uv^\top$ et $vu^\top$ sont $a^i$ et $a^j$, donc
$$A=uv^\top+vu^\top.$$

**4.2 Cas $n=1$.** $A=(2a)$, de rang 1, et $\chi_A=X-2a$. On suppose ensuite $n\ge2$.

**4.3 Image et plan $P$.** Pour $x\in\mathbb R^n$, $Ax=u\,(v^\top x)+v\,(u^\top x)\in P=\mathrm{Vect}(u,v)$. De plus $u$ et $v$ sont libres : si $u=\lambda v$, alors $a=\lambda=a^2$, ce qui impose $a\in\{0,1\}$, exclu. Sur $P$ :
$$Au=S_1u+S_2v,\qquad Av=n\,u+S_1v,\qquad\text{matrice } B=\begin{pmatrix}S_1&n\\S_2&S_1\end{pmatrix}\text{ dans la base }(u,v).$$

**4.4 $B$ est inversible.** On a $\det B=S_1^2-nS_2=(v^\top u)^2-(v^\top v)(u^\top u)<0$, d'après Cauchy-Schwarz avec inégalité stricte car $(u,v)$ est libre. Donc $A(P)=P$ et $\mathrm{rg}\,A=2$.

**4.5 Noyau.** Comme $(u,v)$ est libre, $Ax=0\iff v^\top x=0\text{ et }u^\top x=0$, donc $\ker A=P^\perp$, de dimension $n-2$, et $\mathbb R^n=P\oplus\ker A$.

**4.6 Polynôme caractéristique.** Dans une base formée de $(u,v)$ complétée par une base de $\ker A$, la matrice de $A$ est $\begin{pmatrix}B&0\\0&0_{n-2}\end{pmatrix}$. Donc
$$\chi_A=X^{n-2}\,\chi_B,\qquad\chi_B=X^2-\mathrm{tr}(B)X+\det B=X^2-2S_1X+S_1^2-nS_2.$$
Les sommes géométriques ($a\neq1$) donnent $S_1=a\frac{a^n-1}{a-1}$ et $S_2=a^2\frac{a^{2n}-1}{a^2-1}$. Les valeurs propres non nulles sont $S_1\pm\sqrt{nS_2}$.

**Étape 5 — Vérification.**

> **Contrôle numérique.** Pour $a=2$ et $n=4$ : la matrice a pour rang $2$ et pour valeurs propres $0$ (double), $-6{,}8782$ et $66{,}8782$. La formule donne $S_1=30$, $S_2=340$ et $S_1\pm\sqrt{1360}=30\pm36{,}878$ : identique.

- Trace : $\mathrm{tr}A=\sum_i2a^i=2S_1$, égale à la somme des valeurs propres, $(S_1+\sqrt{nS_2})+(S_1-\sqrt{nS_2})$.
- $A$ est symétrique réelle, donc diagonalisable à valeurs propres réelles. C'est cohérent avec le discriminant $4nS_2>0$.
- Les deux valeurs propres non nulles sont de signes opposés, puisque leur produit vaut $S_1^2-nS_2<0$.

**Étape 6 — Conclusion.**
$$\boxed{\begin{aligned}&n\ge2:\quad\mathrm{rg}\,A=2,\qquad\chi_A=X^{n-2}\big(X^2-2S_1X+S_1^2-nS_2\big)\\&S_1=a\,\frac{a^n-1}{a-1},\qquad S_2=a^2\,\frac{a^{2n}-1}{a^2-1}\qquad(n=1:\ \mathrm{rg}A=1,\ \chi_A=X-2a)\end{aligned}}$$
===RÉPONSE===
$\mathrm{rg}\,A=2$ pour $n\ge2$ ; $\chi_A=X^{n-2}\big(X^2-2S_1X+S_1^2-nS_2\big)$ avec $S_1=\sum a^i$, $S_2=\sum a^{2i}$ ; valeurs propres non nulles $S_1\pm\sqrt{nS_2}$."""

D['m-ccmp-14b'] = r"""**Étape 1 — Analyse de l'énoncé.** On étudie $f(x)=\displaystyle\int_0^{+\infty}\frac{t^x}{e^t-1}\,\mathrm dt$ pour $x>0$.
1. Il faut montrer l'existence de l'intégrale (impropre aux deux bornes), puis la continuité de $f$ sur $]0,+\infty[$.
2. Il faut écrire $f(x)$ comme somme d'une série de fonctions.

**Étape 2 — Rappels du cours.**

> **Théorème — Intégrales de Riemann et comparaison.** $\int_0^1\frac{\mathrm dt}{t^\alpha}$ converge si et seulement si $\alpha<1$. Si $0\le h\le g$ (ou $h=O(g)$) au voisinage d'une borne et $g$ y est intégrable, $h$ l'est aussi.

> **Théorème — Continuité sous l'intégrale.** Si $x\mapsto h(x,t)$ est continue, $t\mapsto h(x,t)$ continue par morceaux, et $|h(x,t)|\le\varphi(t)$ pour tout $x\in J$ avec $\varphi$ intégrable (hypothèse de **domination**), alors $x\mapsto\int h(x,t)\,\mathrm dt$ est continue sur $J$.

> **Théorème — Intégration terme à terme (fonctions positives).** Si les $g_k$ sont continues par morceaux, positives et intégrables, et si $\sum g_k$ converge simplement vers une fonction continue par morceaux, alors $\int\sum g_k=\sum\int g_k$ (dans $[0,+\infty]$).

> **Définition — Fonction Gamma.** $\Gamma(s)=\int_0^{+\infty}u^{s-1}e^{-u}\,\mathrm du$ pour $s>0$.

**Étape 3 — Stratégie.** L'existence s'obtient par des équivalents aux deux bornes. La continuité s'obtient par domination sur chaque segment $[a,b]\subset]0,+\infty[$ ; on ne peut pas dominer sur tout $]0,+\infty[$ à la fois. Pour la question 2, on développe $\frac1{e^t-1}$ en série géométrique, puis on intègre terme à terme (termes positifs) et on reconnaît $\Gamma$ par le changement de variable $u=kt$.

**Étape 4 — Résolution détaillée.**

**4.1 Existence.** Soit $x>0$ et $h(x,t)=\frac{t^x}{e^t-1}$, continue et positive sur $]0,+\infty[$.
- En $0^+$ : $e^t-1\sim t$, donc $h(x,t)\sim t^{x-1}=\frac1{t^{1-x}}$ avec $1-x<1$. C'est intégrable.
- En $+\infty$ : pour $t\ge1$, $e^t-1\ge\frac{e^t}2$, donc $h(x,t)\le2t^xe^{-t}$. Comme $t^{x+2}e^{-t}\to0$ (croissances comparées), $t^xe^{-t}=o\big(\frac1{t^2}\big)$, qui est intégrable.

**4.2 Continuité.** Soit $[a,b]\subset]0,+\infty[$ et $x\in[a,b]$. Pour $0<t\le1$, $t^x\le t^a$ ; pour $t\ge1$, $t^x\le t^b$. Donc
$$0\le h(x,t)\le\varphi(t)=h(a,t)+h(b,t),$$
qui est intégrable d'après 4.1. Comme $x\mapsto h(x,t)$ est continue, $f$ est continue sur $[a,b]$. Tout point de $]0,+\infty[$ est dans un tel segment, donc $f$ est continue sur $]0,+\infty[$.

**4.3 Développement en série.** Pour $t>0$, $0<e^{-t}<1$, d'où
$$\frac1{e^t-1}=\frac{e^{-t}}{1-e^{-t}}=\sum_{k\ge1}e^{-kt},\qquad h(x,t)=\sum_{k\ge1}t^xe^{-kt}.$$

**4.4 Interversion.** Les fonctions $g_k(t)=t^xe^{-kt}$ sont continues, positives et intégrables sur $]0,+\infty[$, et leur somme $h(x,\cdot)$ est continue. Par le théorème pour les fonctions positives :
$$f(x)=\sum_{k\ge1}\int_0^{+\infty}t^xe^{-kt}\,\mathrm dt.$$

**4.5 Calcul de chaque terme.** Le changement de variable $u=kt$, bijection $C^1$ croissante de $]0,+\infty[$ sur lui-même, donne
$$\int_0^{+\infty}t^xe^{-kt}\,\mathrm dt=\frac1{k^{x+1}}\int_0^{+\infty}u^xe^{-u}\,\mathrm du=\frac{\Gamma(x+1)}{k^{x+1}}.$$
Comme $x+1>1$, la série $\sum k^{-(x+1)}$ converge et vaut $\zeta(x+1)$.

**Étape 5 — Vérification.**

> **Contrôle numérique.** Par quadrature : $f(1)=1{,}6449341$, égal à $\Gamma(2)\zeta(2)=\frac{\pi^2}6$. De même $f(3)=6{,}4939394$, égal à $\Gamma(4)\zeta(4)=6\cdot\frac{\pi^4}{90}=\frac{\pi^4}{15}$.

- Cas limite $x\to0^+$ : $\zeta(x+1)\to+\infty$, et l'intégrande se comporte comme $\frac1t$ en $0$. On comprend pourquoi $x=0$ est exclu.
- La domination n'est valable que sur des segments : pour $x\to+\infty$, $f(x)\sim\Gamma(x+1)$ n'est pas bornée. Aucune domination globale n'était donc possible.

**Étape 6 — Conclusion.**
$$\boxed{\forall x>0,\quad f(x)=\sum_{k=1}^{+\infty}\frac{\Gamma(x+1)}{k^{x+1}}=\Gamma(x+1)\,\zeta(x+1)\qquad(\text{par ex. } f(1)=\tfrac{\pi^2}6,\ f(3)=\tfrac{\pi^4}{15})}$$
===RÉPONSE===
$f$ est définie et continue sur $]0,+\infty[$ et $f(x)=\sum_{k\ge1}\frac{\Gamma(x+1)}{k^{x+1}}=\Gamma(x+1)\zeta(x+1)$."""
