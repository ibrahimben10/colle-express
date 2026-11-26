# Mathématiques — 10 exercices dans l'esprit des oraux Mines-Ponts (énoncés, indices et corrigés originaux).
from newlib import ex, E

SRC = "Dans l'esprit des oraux Mines-Ponts."
def mp():
    E[-1]['enonce'] += '\n\n*' + SRC + '*'
    E[-1]['concours'] = 'Mines-Ponts'
    E[-1]['ajout'] = '2026-11-26'

# ------------------------------------------------------------ 1. Racine carrée et diagonalisabilité
ex('n-mp-racine', 'Maths', 'Réduction', 2, 'Si A² est diagonalisable…', 20, r"""
Soit $A\in\mathcal M_n(\mathbb C)$ **inversible** telle que $A^2$ soit diagonalisable.

1. Montrer que $A$ est diagonalisable.
2. Le résultat subsiste-t-il sans l'hypothèse d'inversibilité ?
3. Le résultat subsiste-t-il dans $\mathcal M_n(\mathbb R)$ (diagonalisabilité sur $\mathbb R$) ?
""", r"""Quel polynôme annule $A^2$ ? Et comment en tirer un polynôme qui annule $A$ lui-même ?""",
r"""Critère : $A$ est diagonalisable si et seulement si elle annule un polynôme **scindé à racines simples**. Si $Q$ annule $A^2$, alors $Q(X^2)$ annule $A$.""",
r"""Avec $Q=\prod_i(X-\mu_i)$ ($\mu_i$ valeurs propres distinctes de $A^2$, non nulles), écris $X^2-\mu_i=(X-\alpha_i)(X+\alpha_i)$ et vérifie que les $\pm\alpha_i$ sont deux à deux distincts.""",
r"""**Étape 1 — Analyse de l'énoncé.** On remonte de $A^2$ à $A$ : un polynôme annulateur de $A^2$ fournit un polynôme annulateur de $A$. Tout l'enjeu est de garder des racines simples, et c'est là qu'intervient l'inversibilité.

**Étape 2 — Rappels du cours.**

> **Théorème — Critère de diagonalisabilité.** Une matrice est diagonalisable si et seulement si elle annule un polynôme scindé à racines simples.

> **Propriété — Racines carrées complexes.** Tout $\mu\in\mathbb C^*$ a exactement deux racines carrées, opposées et distinctes.

**Étape 3 — Stratégie.** $A^2$ diagonalisable annule $Q=\prod(X-\mu_i)$. Alors $A$ annule $Q(X^2)=\prod(X^2-\mu_i)$, que l'on factorise sur $\mathbb C$ ; il reste à vérifier que ses racines sont simples.

**Étape 4 — Résolution détaillée.**

**4.1 Un annulateur de $A$.** Soient $\mu_1,\dots,\mu_r$ les valeurs propres **distinctes** de $A^2$. Comme $A^2$ est diagonalisable, $Q=\prod_{i=1}^r(X-\mu_i)$ annule $A^2$. Comme $A$ est inversible, $A^2$ aussi, donc $\mu_i\ne0$. Le polynôme $R=Q(X^2)=\prod_{i=1}^r(X^2-\mu_i)$ vérifie $R(A)=Q(A^2)=0$.

**4.2 Factorisation.** Pour chaque $i$, choisissons $\alpha_i\in\mathbb C$ avec $\alpha_i^2=\mu_i$ : $X^2-\mu_i=(X-\alpha_i)(X+\alpha_i)$, donc $R=\prod_i(X-\alpha_i)(X+\alpha_i)$ est scindé.

**4.3 Racines simples.** $\alpha_i\ne-\alpha_i$ car $\alpha_i\ne0$. Pour $i\ne j$, $\alpha_i\ne\pm\alpha_j$ car $\alpha_i^2=\mu_i\ne\mu_j=\alpha_j^2$. Les $2r$ racines sont donc distinctes : $R$ est scindé à racines simples et $A$ est diagonalisable.

**4.4 Sans inversibilité.** $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ vérifie $A^2=0$, diagonalisable, mais $A$ est nilpotente non nulle, donc non diagonalisable. Le point qui casse : $X^2-0=X^2$ a une racine double.

**4.5 Sur $\mathbb R$.** $A=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ est inversible et $A^2=-I_2$ est diagonale, mais $\chi_A=X^2+1$ n'a pas de racine réelle : $A$ n'est pas diagonalisable sur $\mathbb R$. Le point qui casse : $-1$ n'a pas de racine carrée réelle.

**Étape 5 — Vérification.**

> **Vérification — Un cas concret.** $A=\mathrm{diag}(1,-1)$ : $A^2=I_2$ ; $R=X^2-1=(X-1)(X+1)$ annule bien $A$, avec deux racines simples.

**Étape 6 — Conclusion.**
$$\boxed{A\in GL_n(\mathbb C),\ A^2\ \text{diagonalisable}\Rightarrow A\ \text{diagonalisable}\ ;\ \text{faux sans inversibilité, faux sur }\mathbb R}$$""",
r"""$A$ annule $\prod(X^2-\mu_i)$, scindé à racines simples car les $\mu_i$ sont non nuls et distincts. Contre-exemples : une nilpotente non nulle, une rotation d'angle $\pi/2$ sur $\mathbb R$.""")
mp()

# ------------------------------------------------------------ 2. Commutant
ex('n-mp-commutant', 'Maths', 'Algèbre linéaire', 2, 'Commutant d’un endomorphisme à valeurs propres distinctes', 20, r"""
Soit $E$ un $\mathbb K$-espace vectoriel de dimension $n\ge1$ et $u\in\mathcal L(E)$ admettant $n$ valeurs propres distinctes $\lambda_1,\dots,\lambda_n$. On note $\mathcal C(u)=\{v\in\mathcal L(E),\ u\circ v=v\circ u\}$.

1. Montrer que $v\in\mathcal C(u)$ si et seulement si $v$ est diagonale dans une base de vecteurs propres de $u$.
2. En déduire $\dim\mathcal C(u)$.
3. Montrer que $\mathcal C(u)=\mathbb K[u]$, et même que tout $v\in\mathcal C(u)$ s'écrit $P(u)$ avec $\deg P\le n-1$.
""", r"""Si $v$ commute avec $u$, que fait $v$ d'un sous-espace propre de $u$ ? Quelle est la dimension de ces sous-espaces ici ?""",
r"""Les sous-espaces propres d'un endomorphisme sont stables par tout endomorphisme qui commute avec lui. Pour la question 3, pense à l'interpolation de Lagrange.""",
r"""Si $v(e_i)=a_ie_i$, cherche $P$ de degré $\le n-1$ avec $P(\lambda_i)=a_i$, puis compare $P(u)$ et $v$ sur la base $(e_i)$.""",
r"""**Étape 1 — Analyse de l'énoncé.** On décrit tous les endomorphismes qui commutent avec $u$. L'hypothèse « $n$ valeurs propres distinctes » rend $u$ diagonalisable avec des sous-espaces propres de dimension $1$.

**Étape 2 — Rappels du cours.**

> **Propriété — Stabilité.** Si $u\circ v=v\circ u$, tout sous-espace propre de $u$ est stable par $v$.

> **Théorème — Interpolation de Lagrange.** Pour $x_1,\dots,x_n$ distincts et $y_1,\dots,y_n$ quelconques, il existe un unique $P\in\mathbb K_{n-1}[X]$ tel que $P(x_i)=y_i$.

**Étape 3 — Stratégie.** Dans une base de vecteurs propres $(e_1,\dots,e_n)$, chaque droite $\mathbb Ke_i$ est stable par $v$, donc $v(e_i)$ est colinéaire à $e_i$. On identifie ainsi $\mathcal C(u)$ aux matrices diagonales, puis on reconnaît des polynômes en $u$.

**Étape 4 — Résolution détaillée.**

**4.1 Caractérisation.** Soit $(e_1,\dots,e_n)$ une base de vecteurs propres, $u(e_i)=\lambda_ie_i$ ; chaque $E_{\lambda_i}(u)=\mathbb Ke_i$ est une droite. Si $v\in\mathcal C(u)$ : $u(v(e_i))=v(u(e_i))=\lambda_iv(e_i)$, donc $v(e_i)\in E_{\lambda_i}(u)=\mathbb Ke_i$ : $v(e_i)=a_ie_i$, et la matrice de $v$ est diagonale. Réciproquement, deux matrices diagonales dans la même base commutent.

**4.2 Dimension.** L'application $v\mapsto\operatorname{Mat}_{(e_i)}(v)$ est un isomorphisme de $\mathcal C(u)$ sur l'espace des matrices diagonales : $\dim\mathcal C(u)=n$.

**4.3 Polynômes en $u$.** Tout $P(u)$ commute avec $u$, donc $\mathbb K[u]\subset\mathcal C(u)$. Soit $v\in\mathcal C(u)$, $v(e_i)=a_ie_i$. Par Lagrange, il existe $P\in\mathbb K_{n-1}[X]$ avec $P(\lambda_i)=a_i$ (les $\lambda_i$ sont distincts). Alors $P(u)(e_i)=P(\lambda_i)e_i=a_ie_i=v(e_i)$ pour tout $i$ : $P(u)=v$. Donc $\mathcal C(u)=\mathbb K[u]=\{P(u),\ \deg P\le n-1\}$.

**Étape 5 — Vérification.**

> **Vérification — Hypothèse indispensable.** Pour $u=\mathrm{Id}$ (une seule valeur propre), $\mathcal C(u)=\mathcal L(E)$ est de dimension $n^2$, alors que $\mathbb K[u]=\mathbb K\,\mathrm{Id}$ est de dimension $1$.

**Étape 6 — Conclusion.**
$$\boxed{\mathcal C(u)=\{v\ \text{diagonale dans la base propre}\}=\mathbb K_{n-1}[u],\qquad\dim\mathcal C(u)=n}$$""",
r"""$v$ commute avec $u$ ⇔ $v$ stabilise chaque droite propre ⇔ $v$ diagonale dans la base propre ; $\dim\mathcal C(u)=n$ ; par Lagrange, $v=P(u)$ avec $\deg P\le n-1$.""")
mp()

# ------------------------------------------------------------ 3. Trace et rang d'une matrice symétrique
ex('n-mp-tracerang', 'Maths', 'Algèbre euclidienne', 2, 'Trace, rang et matrice symétrique', 15, r"""
Soit $A\in\mathcal S_n(\mathbb R)$ non nulle, de rang $r$.

1. Montrer que $(\operatorname{tr}A)^2\le r\,\operatorname{tr}(A^2)$.
2. Étudier le cas d'égalité.
3. En déduire que si $A\in\mathcal S_n(\mathbb R)$ vérifie $A^2=A$, alors $\operatorname{rg}A=\operatorname{tr}A$.
""", r"""Que deviennent $\operatorname{tr}A$, $\operatorname{tr}(A^2)$ et $\operatorname{rg}A$ quand on regarde les valeurs propres de $A$ ?""",
r"""Théorème spectral : $A$ est diagonalisable en base orthonormée, et son rang est le nombre de valeurs propres non nulles (comptées avec multiplicité). Puis une inégalité célèbre sur les sommes.""",
r"""Applique l'inégalité de Cauchy-Schwarz aux vecteurs $(\lambda_1,\dots,\lambda_r)$ et $(1,\dots,1)$ de $\mathbb R^r$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Trois quantités invariantes par similitude : la trace, la trace du carré et le rang. Pour une matrice symétrique réelle, elles se lisent toutes sur les valeurs propres.

**Étape 2 — Rappels du cours.**

> **Théorème spectral.** Toute $A\in\mathcal S_n(\mathbb R)$ s'écrit $A=PD\,{}^tP$ avec $P\in O_n(\mathbb R)$ et $D$ diagonale réelle.

> **Théorème — Cauchy-Schwarz dans $\mathbb R^r$.** $\left(\sum x_iy_i\right)^2\le\sum x_i^2\sum y_i^2$, avec égalité si et seulement si les vecteurs sont colinéaires.

**Étape 3 — Stratégie.** On écrit les trois quantités avec les valeurs propres non nulles, puis Cauchy-Schwarz contre le vecteur $(1,\dots,1)$.

**Étape 4 — Résolution détaillée.**

**4.1 Lecture spectrale.** $A=PD\,{}^tP$ avec $D=\mathrm{diag}(\lambda_1,\dots,\lambda_n)$. Le rang de $A$ est celui de $D$ : quitte à réordonner, $\lambda_1,\dots,\lambda_r$ sont non nuls et les autres nuls. Comme $A^2=PD^2\,{}^tP$ :
$$\operatorname{tr}A=\sum_{i=1}^r\lambda_i,\qquad\operatorname{tr}(A^2)=\sum_{i=1}^r\lambda_i^2.$$

**4.2 Inégalité.** Cauchy-Schwarz avec $x=(\lambda_1,\dots,\lambda_r)$ et $y=(1,\dots,1)$ :
$$(\operatorname{tr}A)^2=\Big(\sum_{i=1}^r\lambda_i\cdot1\Big)^2\le\sum_{i=1}^r\lambda_i^2\cdot r=r\operatorname{tr}(A^2).$$

**4.3 Égalité.** Il y a égalité si et seulement si $(\lambda_1,\dots,\lambda_r)$ est colinéaire à $(1,\dots,1)$, c'est-à-dire si toutes les valeurs propres non nulles sont égales à un même $\lambda$ : $A=\lambda\,P\,\mathrm{diag}(I_r,0)\,{}^tP=\lambda p$, où $p$ est la matrice d'un projecteur orthogonal de rang $r$.

**4.4 Projecteurs.** Si $A^2=A$ avec $A$ symétrique non nulle, les valeurs propres vérifient $\lambda^2=\lambda$, donc les non nulles valent $1$ : $\operatorname{tr}A=r$. (Si $A=0$, $\operatorname{tr}A=\operatorname{rg}A=0$.) C'est le cas d'égalité, avec $\lambda=1$.

**Étape 5 — Vérification.**

> **Vérification — Un exemple.** $A=\mathrm{diag}(1,2,0)$ : $r=2$, $(\operatorname{tr}A)^2=9\le2\times5=10$, inégalité stricte car $1\ne2$.

**Étape 6 — Conclusion.**
$$\boxed{(\operatorname{tr}A)^2\le\operatorname{rg}(A)\operatorname{tr}(A^2),\ \text{égalité}\iff A=\lambda p\ (p\ \text{projecteur orthogonal})}$$""",
r"""Spectralement, $\operatorname{tr}A=\sum_{i\le r}\lambda_i$ et $\operatorname{tr}A^2=\sum_{i\le r}\lambda_i^2$ ; Cauchy-Schwarz contre $(1,\dots,1)$. Égalité ssi les valeurs propres non nulles sont égales : $A=\lambda p$.""")
mp()

# ------------------------------------------------------------ 4. Deux lois géométriques
ex('n-mp-geom', 'Maths', 'Probabilités', 1, 'Duel de lois géométriques', 15, r"""
Soient $X$ et $Y$ deux variables aléatoires indépendantes de même loi géométrique $\mathcal G(p)$, $p\in\,]0,1[$, et $q=1-p$.

1. Calculer $P(X>k)$ pour $k\in\mathbb N$.
2. Déterminer la loi de $Z=\min(X,Y)$.
3. Calculer $P(X=Y)$, puis $P(X<Y)$.
""", r"""Que signifie l'événement $(X>k)$ en termes d'épreuves de Bernoulli ? Et $(\min(X,Y)>k)$ en fonction de $X$ et de $Y$ ?""",
r"""$(\min(X,Y)>k)=(X>k)\cap(Y>k)$, et l'indépendance transforme l'intersection en produit. Pour $(X=Y)$, utilise la formule des probabilités totales sur la valeur commune.""",
r"""$P(X=Y)=\sum_{k\ge1}P(X=k)P(Y=k)$ est une série géométrique ; pour $P(X<Y)$, la symétrie entre $X$ et $Y$ suffit.""",
r"""**Étape 1 — Analyse de l'énoncé.** $X$ et $Y$ jouent des rôles symétriques ; on exploite la fonction de survie $k\mapsto P(X>k)$, bien adaptée au minimum.

**Étape 2 — Rappels du cours.**

> **Définition — Loi géométrique.** $X\sim\mathcal G(p)$ si $X(\Omega)=\mathbb N^*$ et $P(X=k)=q^{k-1}p$ : rang du premier succès dans une suite d'épreuves de Bernoulli indépendantes de paramètre $p$.

> **Propriété — Caractérisation par la survie.** Pour $Z$ à valeurs dans $\mathbb N^*$, $P(Z=k)=P(Z>k-1)-P(Z>k)$ : la survie détermine la loi.

**Étape 3 — Stratégie.** Survie de $X$, puis survie de $Z$ par indépendance ; $P(X=Y)$ par probabilités totales ; $P(X<Y)$ par symétrie.

**Étape 4 — Résolution détaillée.**

**4.1 Survie.** $(X>k)$ signifie que les $k$ premières épreuves sont des échecs : $P(X>k)=q^k$. (Ou : $\sum_{j>k}q^{j-1}p=q^k$.)

**4.2 Minimum.** $(Z>k)=(X>k)\cap(Y>k)$, donc par indépendance $P(Z>k)=q^{2k}=(q^2)^k$. C'est la survie d'une loi géométrique de paramètre $1-q^2$ : $Z\sim\mathcal G(1-q^2)=\mathcal G\big(p(2-p)\big)$.

**4.3 Égalité.** Les événements $(X=k)$, $k\ge1$, forment un système complet :
$$P(X=Y)=\sum_{k\ge1}P(X=k,Y=k)=\sum_{k\ge1}p^2q^{2(k-1)}=\frac{p^2}{1-q^2}=\frac{p}{2-p}.$$

**4.4 Ordre strict.** $(X<Y)$, $(X=Y)$, $(X>Y)$ forment un système complet, et $P(X<Y)=P(Y<X)$ car $(X,Y)$ et $(Y,X)$ ont même loi. Donc
$$P(X<Y)=\frac{1-P(X=Y)}2=\frac{1-p}{2-p}.$$

**Étape 5 — Vérification.**

> **Vérification — Cas limites.** Pour $p\to1$, $X=Y=1$ presque sûrement : $P(X=Y)\to1$ ✓. Pour $p=\frac12$ : $P(X=Y)=\frac13$ et $P(X<Y)=\frac13$, la somme des trois probabilités vaut bien $1$.

**Étape 6 — Conclusion.**
$$\boxed{Z\sim\mathcal G\big(p(2-p)\big),\quad P(X=Y)=\frac p{2-p},\quad P(X<Y)=\frac{1-p}{2-p}}$$""",
r"""$P(X>k)=q^k$ ; $P(\min>k)=q^{2k}$ donc $\min(X,Y)\sim\mathcal G(1-q^2)$ ; $P(X=Y)=\frac{p}{2-p}$ et, par symétrie, $P(X<Y)=\frac{1-p}{2-p}$.""")
mp()

# ------------------------------------------------------------ 5. Involutions
ex('n-mp-involutions', 'Maths', 'Séries entières', 2, 'Nombre d’involutions et série génératrice', 25, r"""
Pour $n\in\mathbb N$, on note $a_n$ le nombre d'involutions de $\{1,\dots,n\}$ (permutations $\sigma$ telles que $\sigma\circ\sigma=\mathrm{id}$), avec $a_0=1$.

1. Montrer que $a_{n+1}=a_n+n\,a_{n-1}$ pour $n\ge1$.
2. Montrer que la série entière $S(x)=\sum_{n\ge0}\frac{a_n}{n!}x^n$ a un rayon de convergence $R\ge1$.
3. Montrer que $S'(x)=(1+x)S(x)$ sur $]-1,1[$ et en déduire $S$.
4. En déduire que $R=+\infty$ et une expression de $a_n$ sous forme de somme.
""", r"""Dans une involution de $\{1,\dots,n+1\}$, que peut devenir l'élément $n+1$ ?""",
r"""Dénombrement par disjonction de cas pour la récurrence ; majoration $a_n\le n!$ pour le rayon ; dérivation terme à terme d'une série entière sur l'intervalle ouvert de convergence.""",
r"""Écris $S'(x)=\sum\frac{a_{n+1}}{n!}x^n$, remplace $a_{n+1}$ par la récurrence, reconnais $S$ et $xS$. Puis développe $e^{x}e^{x^2/2}$ par produit de Cauchy.""",
r"""**Étape 1 — Analyse de l'énoncé.** Une suite définie combinatoirement, une récurrence, puis une série génératrice exponentielle qui vérifie une équation différentielle simple.

**Étape 2 — Rappels du cours.**

> **Théorème — Dérivation terme à terme.** Sur $]-R,R[$, la somme d'une série entière est $\mathcal C^\infty$ et se dérive terme à terme.

> **Théorème — Produit de Cauchy.** Le produit de deux séries entières de rayons $\ge\rho$ est une série entière de rayon $\ge\rho$, de coefficients $c_n=\sum_ka_kb_{n-k}$.

> **Propriété — Unicité.** Deux séries entières égales au voisinage de $0$ ont les mêmes coefficients.

**Étape 3 — Stratégie.** Récurrence par le sort de $n+1$ ; rayon par comparaison ; équation $S'=(1+x)S$ résolue ; identification des coefficients avec ceux de $e^{x+x^2/2}$.

**Étape 4 — Résolution détaillée.**

**4.1 Récurrence.** Soit $\sigma$ une involution de $\{1,\dots,n+1\}$. Ou bien $\sigma(n+1)=n+1$, et $\sigma$ induit une involution de $\{1,\dots,n\}$ : $a_n$ possibilités. Ou bien $\sigma(n+1)=j\le n$, et alors $\sigma(j)=n+1$ ; il y a $n$ choix de $j$, et $\sigma$ induit une involution des $n-1$ éléments restants : $n\,a_{n-1}$ possibilités. D'où $a_{n+1}=a_n+n\,a_{n-1}$.

**4.2 Rayon.** Une involution est une permutation : $0<a_n\le n!$, donc $\frac{a_n}{n!}\le1$ et la série $\sum\frac{a_n}{n!}x^n$ converge absolument pour $|x|<1$ : $R\ge1$.

**4.3 Équation différentielle.** Sur $]-1,1[$ :
$$S'(x)=\sum_{n\ge0}\frac{a_{n+1}}{n!}x^n=\sum_{n\ge0}\frac{a_n}{n!}x^n+\sum_{n\ge1}\frac{n\,a_{n-1}}{n!}x^n=S(x)+x\sum_{n\ge1}\frac{a_{n-1}}{(n-1)!}x^{n-1}=(1+x)S(x).$$
(Pour $n=0$, $a_1=1=a_0$ est cohérent avec la convention $n\,a_{n-1}=0$.) Avec $S(0)=a_0=1$, la solution est $S(x)=e^{x+x^2/2}$.

**4.4 Rayon infini et formule.** $e^x=\sum\frac{x^j}{j!}$ et $e^{x^2/2}=\sum\frac{x^{2k}}{2^kk!}$ ont un rayon infini, donc leur produit de Cauchy aussi :
$$e^{x+x^2/2}=\sum_{n\ge0}\Big(\sum_{0\le k\le n/2}\frac{1}{(n-2k)!\,2^k\,k!}\Big)x^n.$$
Cette série coïncide avec $S$ sur $]-1,1[$ ; par unicité des coefficients,
$$a_n=\sum_{0\le k\le n/2}\frac{n!}{(n-2k)!\,2^k\,k!},$$
et $R=+\infty$ puisque les deux séries ont les mêmes coefficients.

**Étape 5 — Vérification.**

> **Vérification — Petites valeurs.** $a_1=1$, $a_2=2$ (identité, transposition), $a_3=a_2+2a_1=4$ (identité et trois transpositions). La formule : $a_3=\frac{6}{6}+\frac{6}{1\cdot2\cdot1}=1+3=4$ ✓.

**Étape 6 — Conclusion.**
$$\boxed{\sum_{n\ge0}\frac{a_n}{n!}x^n=e^{x+x^2/2}\ (R=+\infty),\qquad a_n=\sum_{k\le n/2}\frac{n!}{(n-2k)!\,2^kk!}}$$""",
r"""Le sort de $n+1$ donne $a_{n+1}=a_n+na_{n-1}$ ; $a_n\le n!$ donne $R\ge1$ ; $S'=(1+x)S$ et $S(0)=1$ donnent $S=e^{x+x^2/2}$, d'où $R=+\infty$ et $a_n=\sum_k\frac{n!}{(n-2k)!2^kk!}$.""")
mp()

# ------------------------------------------------------------ 6. Intégrale à paramètre
ex('n-mp-logint', 'Maths', 'Intégrales à paramètre', 2, 'Une intégrale qui donne un logarithme', 20, r"""
Pour $x\in\mathbb R$, on pose $F(x)=\displaystyle\int_0^{+\infty}e^{-t}\,\frac{1-\cos(xt)}{t}\,\mathrm dt$.

1. Montrer que $F$ est définie sur $\mathbb R$.
2. Montrer que $F$ est de classe $\mathcal C^1$ sur $\mathbb R$ et calculer $F'$.
3. En déduire $F(x)$ pour tout réel $x$, puis la valeur de $\displaystyle\int_0^{+\infty}e^{-t}\,\frac{1-\cos t}{t}\,\mathrm dt$.
""", r"""Comment se comporte l'intégrande en $0$ et en $+\infty$ ? Et que gagne-t-on à dériver par rapport à $x$ ?""",
r"""Théorème de dérivation sous l'intégrale : il faut une domination de $\frac{\partial}{\partial x}$ par une fonction intégrable **indépendante de $x$**.""",
r"""$\frac{\partial}{\partial x}\Big(e^{-t}\frac{1-\cos(xt)}{t}\Big)=e^{-t}\sin(xt)$, majorée par $e^{-t}$. Calcule $\int_0^{+\infty}e^{-t}\sin(xt)\,\mathrm dt$ comme partie imaginaire de $\int_0^{+\infty}e^{(-1+ix)t}\,\mathrm dt$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Une intégrale généralisée à paramètre : on justifie l'existence, on dérive sous le signe somme (ce qui fait disparaître le $\frac1t$ gênant), puis on intègre en $x$.

**Étape 2 — Rappels du cours.**

> **Théorème — Dérivation sous l'intégrale.** Si $f(x,t)$ est intégrable en $t$ pour tout $x$, si $\frac{\partial f}{\partial x}$ existe, est continue en $x$ et continue par morceaux en $t$, et si $\big|\frac{\partial f}{\partial x}(x,t)\big|\le\varphi(t)$ avec $\varphi$ intégrable indépendante de $x$, alors $F$ est $\mathcal C^1$ et $F'(x)=\int\frac{\partial f}{\partial x}(x,t)\,\mathrm dt$.

> **Propriété — Intégrale de référence.** Pour $\operatorname{Re}a<0$, $\int_0^{+\infty}e^{at}\,\mathrm dt=-\frac1a$.

**Étape 3 — Stratégie.** Existence par comparaison aux deux bornes ; dérivation avec la domination par $e^{-t}$ ; calcul de $F'$ par l'exponentielle complexe ; intégration avec $F(0)=0$.

**Étape 4 — Résolution détaillée.**

**4.1 Existence.** Soit $x\in\mathbb R$ ; $g(t)=e^{-t}\frac{1-\cos(xt)}{t}$ est continue sur $]0,+\infty[$. En $0$ : $1-\cos(xt)\sim\frac{x^2t^2}2$ (ou est nul si $x=0$), donc $g(t)\to0$ : $g$ se prolonge par continuité. En $+\infty$ : $0\le g(t)\le2e^{-t}$ pour $t\ge1$, intégrable. Donc $F(x)$ existe.

**4.2 Dérivation.** $f(x,t)=e^{-t}\frac{1-\cos(xt)}{t}$ admet $\frac{\partial f}{\partial x}(x,t)=e^{-t}\sin(xt)$, continue en $x$ et en $t$, avec $|e^{-t}\sin(xt)|\le e^{-t}$, intégrable sur $]0,+\infty[$ et indépendante de $x$. Donc $F$ est $\mathcal C^1$ sur $\mathbb R$ et
$$F'(x)=\int_0^{+\infty}e^{-t}\sin(xt)\,\mathrm dt=\operatorname{Im}\int_0^{+\infty}e^{(-1+ix)t}\,\mathrm dt=\operatorname{Im}\frac{1}{1-ix}=\operatorname{Im}\frac{1+ix}{1+x^2}=\frac{x}{1+x^2}.$$

**4.3 Intégration.** $F(0)=0$ (intégrande nul), donc $F(x)=\int_0^x\frac{s}{1+s^2}\,\mathrm ds=\frac12\ln(1+x^2)$. En particulier, pour $x=1$ :
$$\int_0^{+\infty}e^{-t}\frac{1-\cos t}{t}\,\mathrm dt=\frac{\ln2}{2}.$$

**Étape 5 — Vérification.**

> **Vérification — Parité et comportement en 0.** $F$ est paire (l'intégrande l'est en $x$) ✓ ; pour $x\to0$, $F(x)\sim\frac{x^2}{2}$ et $\int_0^{+\infty}e^{-t}\frac{x^2t^2/2}{t}\,\mathrm dt=\frac{x^2}2\int_0^{+\infty}te^{-t}\,\mathrm dt=\frac{x^2}{2}$ ✓.

**Étape 6 — Conclusion.**
$$\boxed{F(x)=\tfrac12\ln(1+x^2)\quad\text{et}\quad\int_0^{+\infty}e^{-t}\frac{1-\cos t}{t}\,\mathrm dt=\frac{\ln 2}{2}}$$""",
r"""Existence par comparaison ; domination de $e^{-t}\sin(xt)$ par $e^{-t}$ : $F'(x)=\frac{x}{1+x^2}$ ; avec $F(0)=0$, $F(x)=\frac12\ln(1+x^2)$, et la valeur en $1$ vaut $\frac{\ln2}2$.""")
mp()

# ------------------------------------------------------------ 7. Sinus de racines
ex('n-mp-sinrac', 'Maths', 'Séries', 1, 'Nature de séries en sin(π√…)', 15, r"""
Déterminer la nature des séries de termes généraux
$$u_n=\sin\big(\pi\sqrt{n^2+1}\big)\qquad\text{et}\qquad v_n=\sin\big(\pi\sqrt{n^2+n}\big)\qquad(n\ge1).$$
La première est-elle absolument convergente ?
""", r"""$\sqrt{n^2+1}$ est très proche d'un entier. Que vaut $\sin(\pi n+h)$ ?""",
r"""Développement asymptotique de $\sqrt{n^2+1}=n\sqrt{1+\frac1{n^2}}$, puis $\sin(\pi n+h)=(-1)^n\sin h$. Pour conclure : critère des séries alternées et comparaison.""",
r"""Écris $u_n=(-1)^n\frac{\pi}{2n}+O\big(\frac1{n^3}\big)$ et sépare en deux séries. Pour $v_n$, développe $\sqrt{n^2+n}=n+\frac12-\frac1{8n}+O\big(\frac1{n^2}\big)$ et regarde si $v_n\to0$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Les termes ne sont pas de signe constant : les critères de comparaison ne s'appliquent pas directement. Un développement asymptotique sépare une partie alternée et un reste absolument convergent.

**Étape 2 — Rappels du cours.**

> **Théorème — Séries alternées.** Si $(a_n)$ décroît vers $0$, $\sum(-1)^na_n$ converge.

> **Propriété — Somme de séries.** La somme d'une série convergente et d'une série absolument convergente converge ; une série dont le terme ne tend pas vers $0$ diverge grossièrement.

**Étape 3 — Stratégie.** Développer la racine, factoriser $\pi n$ dans le sinus pour faire apparaître $(-1)^n$, puis conclure terme à terme.

**Étape 4 — Résolution détaillée.**

**4.1 Développement de $u_n$.** $\sqrt{n^2+1}=n\Big(1+\frac1{2n^2}+O\big(\frac1{n^4}\big)\Big)=n+\frac1{2n}+O\big(\frac1{n^3}\big)$. Donc
$$u_n=\sin\Big(\pi n+\frac{\pi}{2n}+O\big(\tfrac1{n^3}\big)\Big)=(-1)^n\sin\Big(\frac{\pi}{2n}+O\big(\tfrac1{n^3}\big)\Big)=(-1)^n\frac{\pi}{2n}+O\big(\tfrac1{n^3}\big).$$

**4.2 Nature de $\sum u_n$.** $\sum(-1)^n\frac{\pi}{2n}$ converge (séries alternées, $\frac{\pi}{2n}$ décroît vers $0$) et $\sum O\big(\frac1{n^3}\big)$ converge absolument (Riemann). Donc $\sum u_n$ converge.

**4.3 Convergence absolue.** $|u_n|\sim\frac{\pi}{2n}$, terme positif d'une série divergente : $\sum|u_n|$ diverge. La série est **semi-convergente**.

**4.4 Développement de $v_n$.** $\sqrt{n^2+n}=n\sqrt{1+\frac1n}=n\Big(1+\frac1{2n}-\frac1{8n^2}+O\big(\tfrac1{n^3}\big)\Big)=n+\frac12-\frac1{8n}+O\big(\tfrac1{n^2}\big)$, donc
$$v_n=(-1)^n\sin\Big(\frac\pi2-\frac{\pi}{8n}+O\big(\tfrac1{n^2}\big)\Big)=(-1)^n\cos\Big(\frac{\pi}{8n}+O\big(\tfrac1{n^2}\big)\Big).$$
$|v_n|\to1$ : $\sum v_n$ **diverge grossièrement**.

**Étape 5 — Vérification.**

> **Vérification — Numérique.** $n=10$ : $\sqrt{101}\approx10{,}0499$, $\sin(\pi\times10{,}0499)\approx\sin(0{,}1567)\approx0{,}156$, et $\frac{\pi}{20}\approx0{,}157$ ✓.

**Étape 6 — Conclusion.**
$$\boxed{\sum u_n\ \text{semi-convergente},\qquad\sum v_n\ \text{grossièrement divergente}}$$""",
r"""$u_n=(-1)^n\frac{\pi}{2n}+O(n^{-3})$ : série alternée plus série absolument convergente, donc convergente, mais pas absolument ($|u_n|\sim\frac{\pi}{2n}$). $|v_n|\to1$ : divergence grossière.""")
mp()

# ------------------------------------------------------------ 8. Polynômes positifs
ex('n-mp-deuxcarres', 'Maths', 'Polynômes', 2, 'Polynôme positif et somme de deux carrés', 20, r"""
Soit $P\in\mathbb R[X]$ tel que $P(x)\ge0$ pour tout réel $x$.

1. Montrer que les racines réelles de $P$ sont de multiplicité paire, et que si $P\ne0$ son coefficient dominant est positif.
2. Montrer qu'il existe $A,B\in\mathbb R[X]$ tels que $P=A^2+B^2$.
3. Écrire explicitement $X^4+1$ sous cette forme.
""", r"""Que se passe-t-il pour le signe de $P$ au voisinage d'une racine réelle de multiplicité impaire ? Et dans $\mathbb C$, comment s'écrit $A^2+B^2$ ?""",
r"""Factorisation dans $\mathbb C[X]$ : les racines non réelles d'un polynôme réel vont par paires conjuguées. Et $A^2+B^2=(A+iB)(A-iB)$.""",
r"""Construis $Q\in\mathbb C[X]$ qui prend la moitié de chaque racine réelle et une racine dans chaque paire conjuguée, de sorte que $P=Q\,\overline Q$ ; puis pose $A=\operatorname{Re}Q$, $B=\operatorname{Im}Q$ (coefficient par coefficient).""",
r"""**Étape 1 — Analyse de l'énoncé.** On caractérise les polynômes réels positifs : ce sont exactement les sommes de deux carrés. La clé est d'écrire $P=Q\overline Q$ avec $Q$ complexe.

**Étape 2 — Rappels du cours.**

> **Théorème — Factorisation.** Tout $P\in\mathbb C[X]$ non nul est scindé ; si $P\in\mathbb R[X]$, ses racines non réelles vont par paires conjuguées de même multiplicité.

> **Propriété — Conjugué.** Pour $Q\in\mathbb C[X]$, on note $\overline Q$ le polynôme aux coefficients conjugués ; pour $x$ réel, $\overline Q(x)=\overline{Q(x)}$, et $\overline{QR}=\overline Q\,\overline R$.

**Étape 3 — Stratégie.** Signe près des racines réelles ⇒ multiplicités paires ; on « coupe en deux » la factorisation de $P$ pour obtenir $Q$ avec $P=Q\overline Q$, puis $Q=A+iB$.

**Étape 4 — Résolution détaillée.**

**4.1 Multiplicités paires.** Si $P=0$, prendre $A=B=0$. Sinon, soit $x_0$ racine réelle de multiplicité $m$ : $P=(X-x_0)^mR$ avec $R(x_0)\ne0$. Par continuité, $R$ garde un signe constant près de $x_0$ ; si $m$ était impair, $(x-x_0)^m$ changerait de signe en $x_0$, donc $P$ aussi, ce qui contredit $P\ge0$. Ainsi $m$ est pair.

**4.2 Factorisation.** Dans $\mathbb C[X]$ :
$$P=c\prod_k(X-x_k)^{2m_k}\prod_j\big((X-z_j)(X-\overline{z_j})\big)^{n_j},$$
avec $x_k$ réels, $z_j\notin\mathbb R$. $P$ est de degré pair, et $P(x)\sim cx^{\deg P}$ en $+\infty$ avec $P\ge0$, donc $c>0$.

**4.3 Construction de $Q$.** Posons $Q=\sqrt c\prod_k(X-x_k)^{m_k}\prod_j(X-z_j)^{n_j}\in\mathbb C[X]$. Alors $\overline Q=\sqrt c\prod_k(X-x_k)^{m_k}\prod_j(X-\overline{z_j})^{n_j}$, et $Q\overline Q=P$.

**4.4 Deux carrés.** Écrivons $Q=A+iB$ avec $A,B\in\mathbb R[X]$ (parties réelle et imaginaire des coefficients). Alors $\overline Q=A-iB$ et
$$P=Q\overline Q=(A+iB)(A-iB)=A^2+B^2.$$

**4.5 Exemple.** Les racines de $X^4+1$ sont $e^{\pm i\pi/4}$ et $e^{\pm3i\pi/4}$. On peut aussi conclure directement : $X^4+1=(X^2-1)^2+2X^2=(X^2-1)^2+(\sqrt2X)^2$.

**Étape 5 — Vérification.**

> **Vérification — Développement.** $(X^2-1)^2+(\sqrt2X)^2=X^4-2X^2+1+2X^2=X^4+1$ ✓.

**Étape 6 — Conclusion.**
$$\boxed{P\ge0\ \text{sur}\ \mathbb R\iff P=A^2+B^2,\ A,B\in\mathbb R[X];\qquad X^4+1=(X^2-1)^2+(\sqrt2\,X)^2}$$""",
r"""Racines réelles de multiplicité paire et coefficient dominant positif ; $P=Q\overline Q$ avec $Q=\sqrt c\prod(X-x_k)^{m_k}\prod(X-z_j)^{n_j}$ ; $Q=A+iB$ donne $P=A^2+B^2$. $X^4+1=(X^2-1)^2+2X^2$.""")
mp()

# ------------------------------------------------------------ 9. Équation à coefficient singulier
ex('n-mp-sinc', 'Maths', 'Équations différentielles', 2, 'Équation xy″ + 2y′ + xy = 0', 25, r"""
On considère l'équation différentielle $(E)\ :\ x\,y''+2y'+x\,y=0$.

1. Déterminer les solutions de $(E)$ développables en série entière au voisinage de $0$.
2. Résoudre $(E)$ sur $]0,+\infty[$ (on pourra poser $z(x)=x\,y(x)$).
3. Déterminer les solutions de $(E)$ de classe $\mathcal C^2$ sur $\mathbb R$. L'ensemble obtenu est-il un plan vectoriel ?
""", r"""Si $y=\sum a_nx^n$, quelle relation lie les coefficients ? Et que donne la dérivée seconde de $z=xy$ ?""",
r"""Identification des coefficients d'une série entière ; puis, sur $]0,+\infty[$, le changement de fonction $z=xy$ transforme $(E)$ en une équation à coefficients constants.""",
r"""$(xy)''=xy''+2y'$, donc $(E)$ devient $z''+z=0$. Pour la question 3, une solution sur $\mathbb R$ doit rester bornée près de $0$ : regarde le terme en $\frac{\cos x}{x}$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Le coefficient de $y''$ s'annule en $0$ : le théorème de Cauchy-Lipschitz ne s'applique que sur $]0,+\infty[$ et $]-\infty,0[$, et l'ensemble des solutions sur $\mathbb R$ peut ne pas être un plan.

**Étape 2 — Rappels du cours.**

> **Théorème — Cauchy-Lipschitz linéaire.** Sur un intervalle où l'équation se met sous forme résolue $y''+a(x)y'+b(x)y=0$ avec $a,b$ continues, les solutions forment un plan vectoriel.

> **Propriété — Unicité des coefficients.** Si $\sum c_nx^n=0$ sur un voisinage de $0$, tous les $c_n$ sont nuls.

**Étape 3 — Stratégie.** Méthode des séries entières en $0$ ; changement de fonction $z=xy$ sur $]0,+\infty[$ ; raccordement en $0$.

**Étape 4 — Résolution détaillée.**

**4.1 Séries entières.** Avec $y=\sum a_nx^n$ de rayon $R>0$ :
$$xy''+2y'=\sum_{n\ge1}\big(n(n-1)+2n\big)a_nx^{n-1}=\sum_{n\ge1}n(n+1)a_nx^{n-1},\qquad xy=\sum_{n\ge2}a_{n-2}x^{n-1}.$$
Par unicité : $2a_1=0$ et $n(n+1)a_n+a_{n-2}=0$ pour $n\ge2$. Donc $a_{2k+1}=0$ et $a_{2k}=\frac{(-1)^ka_0}{(2k+1)!}$ (récurrence). La série $\sum\frac{(-1)^k}{(2k+1)!}x^{2k}$ a un rayon infini et vaut $\frac{\sin x}{x}$ pour $x\ne0$. Les solutions développables sont $y=a_0\,\varphi$, où $\varphi(x)=\frac{\sin x}{x}$, $\varphi(0)=1$.

**4.2 Sur $]0,+\infty[$.** Posons $z=xy$ : $z''=xy''+2y'$, donc $(E)\iff z''+z=0\iff z=\alpha\cos x+\beta\sin x$. Les solutions sont
$$y(x)=\frac{\alpha\cos x+\beta\sin x}{x},\qquad\alpha,\beta\in\mathbb R,$$
un plan, comme le prévoit Cauchy-Lipschitz (forme résolue $y''+\frac2xy'+y=0$). De même sur $]-\infty,0[$, avec des constantes $\alpha',\beta'$.

**4.3 Raccordement.** Soit $y$ solution de classe $\mathcal C^2$ sur $\mathbb R$. Sur $]0,+\infty[$, $y=\frac{\alpha\cos x+\beta\sin x}{x}$ doit avoir une limite finie en $0^+$ ; comme $\frac{\beta\sin x}{x}\to\beta$, il faut $\frac{\alpha\cos x}{x}$ borné, donc $\alpha=0$. De même $\alpha'=0$. Alors $y=\beta\varphi$ sur $]0,+\infty[$ et $\beta'\varphi$ sur $]-\infty,0[$ ; la continuité en $0$ impose $\beta=\beta'=y(0)$. Réciproquement, $\beta\varphi$ est $\mathcal C^\infty$ sur $\mathbb R$ (série entière de rayon infini) et vérifie $(E)$ partout (4.1).

**Étape 5 — Vérification.**

> **Vérification — Dimension.** Sur $\mathbb R$, les solutions forment la **droite** $\mathbb R\varphi$, et non un plan : c'est possible car le coefficient de $y''$ s'annule en $0$, ce qui fait sortir du cadre de Cauchy-Lipschitz.

**Étape 6 — Conclusion.**
$$\boxed{\text{sur }]0,+\infty[\ :\ y=\frac{\alpha\cos x+\beta\sin x}{x}\ ;\quad\text{sur }\mathbb R\ :\ y=\beta\,\frac{\sin x}{x}\ (\text{prolongée par }\beta\text{ en }0)}$$""",
r"""Séries entières : $a_{2k}=\frac{(-1)^ka_0}{(2k+1)!}$, d'où $\frac{\sin x}{x}$ ; avec $z=xy$, $z''+z=0$ et $y=\frac{\alpha\cos x+\beta\sin x}{x}$ ; sur $\mathbb R$, seule la droite $\mathbb R\frac{\sin x}{x}$ convient.""")
mp()

# ------------------------------------------------------------ 10. χ_AB = χ_BA par densité
ex('n-mp-chiab', 'Maths', 'Topologie matricielle', 2, 'χ_AB = χ_BA par densité', 20, r"""
Soient $A,B\in\mathcal M_n(\mathbb C)$.

1. Montrer que $GL_n(\mathbb C)$ est dense dans $\mathcal M_n(\mathbb C)$.
2. Montrer que si $A$ est inversible, $AB$ et $BA$ sont semblables.
3. En déduire que $\chi_{AB}=\chi_{BA}$ pour toutes matrices $A,B$.
4. $AB$ et $BA$ sont-elles toujours semblables ?
""", r"""Pour combien de valeurs de $\lambda$ la matrice $A-\lambda I_n$ n'est-elle pas inversible ?""",
r"""Une matrice n'a qu'un nombre fini de valeurs propres ; deux fonctions continues égales sur une partie dense sont égales. Les coefficients de $\chi_M$ sont polynomiaux en ceux de $M$.""",
r"""Utilise $A_p=A-\frac1pI_n$, inversible pour $p$ assez grand, et $A_pB=A_p(BA_p)A_p^{-1}$ ; puis fais tendre $p$ vers l'infini dans $\chi_{A_pB}(x)=\chi_{BA_p}(x)$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Le résultat est facile quand $A$ est inversible ; la densité de $GL_n$ et la continuité du polynôme caractéristique l'étendent à toutes les matrices.

**Étape 2 — Rappels du cours.**

> **Propriété — Valeurs propres.** Une matrice $A\in\mathcal M_n(\mathbb C)$ a au plus $n$ valeurs propres ; $A-\lambda I_n$ est inversible si et seulement si $\lambda\notin\operatorname{Sp}(A)$.

> **Propriété — Prolongement des identités.** Deux applications continues égales sur une partie dense sont égales. Les coefficients de $\chi_M$ sont des polynômes en les coefficients de $M$, donc continus.

**Étape 3 — Stratégie.** Approcher $A$ par $A_p=A-\frac1pI_n$ inversible, utiliser la similitude $A_pB\sim BA_p$, puis passer à la limite.

**Étape 4 — Résolution détaillée.**

**4.1 Densité.** $\operatorname{Sp}(A)$ est fini, donc pour $p$ assez grand $\frac1p\notin\operatorname{Sp}(A)$ et $A_p=A-\frac1pI_n\in GL_n(\mathbb C)$. Comme $A_p\to A$, tout $A$ est limite de matrices inversibles.

**4.2 Cas inversible.** Si $A$ est inversible : $AB=A(BA)A^{-1}$, donc $AB$ et $BA$ sont semblables et $\chi_{AB}=\chi_{BA}$.

**4.3 Cas général.** Fixons $x\in\mathbb C$. L'application $M\mapsto\chi_{MB}(x)-\chi_{BM}(x)=\det(xI_n-MB)-\det(xI_n-BM)$ est polynomiale en les coefficients de $M$, donc continue. Elle est nulle sur $GL_n(\mathbb C)$ (4.2), partie dense (4.1), donc nulle partout : $\chi_{AB}(x)=\chi_{BA}(x)$ pour tout $x$, et $\chi_{AB}=\chi_{BA}$.

**4.4 Pas de similitude en général.** $A=\begin{pmatrix}1&0\\0&0\end{pmatrix}$, $B=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ : $AB=\begin{pmatrix}0&1\\0&0\end{pmatrix}\ne0$ et $BA=0$. Une matrice semblable à la matrice nulle est nulle : $AB$ et $BA$ ne sont pas semblables, bien qu'elles aient le même polynôme caractéristique $X^2$.

**Étape 5 — Vérification.**

> **Vérification — Conséquences.** En identifiant les coefficients : $\operatorname{tr}(AB)=\operatorname{tr}(BA)$ et $\det(AB)=\det(BA)$, deux résultats connus ✓.

**Étape 6 — Conclusion.**
$$\boxed{\forall A,B\in\mathcal M_n(\mathbb C),\ \chi_{AB}=\chi_{BA},\ \text{mais }AB\ \text{et}\ BA\ \text{ne sont pas toujours semblables}}$$""",
r"""$A-\frac1pI_n$ est inversible pour $p$ grand : $GL_n$ est dense ; $AB=A(BA)A^{-1}$ si $A$ inversible ; continuité de $M\mapsto\chi_{MB}(x)-\chi_{BM}(x)$ ; contre-exemple à la similitude avec $AB\ne0=BA$.""")
mp()
