# Exercices d'après des sujets de concours (algèbre) : énoncés reformulés, indices et corrigés originaux.
from newlib import ex, E

def src(texte, concours):
    E[-1]['enonce'] += '\n\n*' + texte + '*'
    E[-1]['concours'] = concours

# ---------------------------------------------------------------- 1. Exposant d'un groupe abélien
ex('n-s-a-expo', 'Maths', 'Groupes', 3, 'Exposant d’un groupe abélien fini', 25, r"""
Soit $G$ un groupe abélien fini, noté multiplicativement.

1. Soient $a,b\in G$ d'ordres $m$ et $n$ premiers entre eux. Montrer que $ab$ est d'ordre $mn$. Que dire de l'ordre de $ab$ en général ? Montrer qu'il existe toujours un élément d'ordre $\mathrm{ppcm}(m,n)$.
2. Soit $r$ le ppcm des ordres des éléments de $G$. Montrer qu'il existe un élément d'ordre $r$.
3. Le résultat subsiste-t-il si $G$ n'est pas abélien ?
4. Soit $K$ un corps. Montrer que tout sous-groupe fini de $(K^*,\times)$ est cyclique.
""", r"""Si $(ab)^k=1$, alors $a^k=b^{-k}$ appartient à $\langle a\rangle\cap\langle b\rangle$.""",
r"""Pour le cas général, décompose $\mathrm{ppcm}(m,n)=m'n'$ avec $m'\mid m$, $n'\mid n$ et $m'\wedge n'=1$, à l'aide des facteurs premiers.""",
r"""Question 4 : tous les éléments sont racines de $X^r-1$, qui a au plus $r$ racines dans un corps.""",
r"""**Étape 1 — Analyse de l'énoncé.** On étudie l'ordre d'un produit dans un groupe abélien, puis l'exposant $r$ du groupe (ppcm des ordres). La conséquence classique est la cyclicité des sous-groupes finis du groupe multiplicatif d'un corps.

**Étape 2 — Rappels du cours.**

> **Propriété — Ordre.** Si $a$ est d'ordre $m$, alors $a^k=1\iff m\mid k$, et $a^d$ est d'ordre $\frac m{d}$ si $d\mid m$.

> **Théorème — Lagrange.** L'ordre d'un élément divise le cardinal du groupe.

> **Propriété — Racines d'un polynôme.** Dans un corps, un polynôme non nul de degré $r$ a au plus $r$ racines.

**Étape 3 — Stratégie.** Ordres premiers entre eux : l'intersection $\langle a\rangle\cap\langle b\rangle$ est triviale. Cas général : on ne garde de $a$ et de $b$ que les facteurs premiers où chacun « domine ». Pour l'exposant : un élément d'ordre maximal a un ordre multiple de tous les autres. Pour le corps : compter les racines de $X^r-1$.

**Étape 4 — Résolution détaillée.**

**4.1 Ordres premiers entre eux.** $(ab)^{mn}=(a^m)^n(b^n)^m=1$ car $G$ est abélien. Si $(ab)^k=1$, alors $c=a^k=b^{-k}$ ; l'ordre de $c$ divise $m$ et $n$, donc vaut $1$. Ainsi $a^k=b^k=1$, $m\mid k$, $n\mid k$, donc $mn\mid k$. L'ordre de $ab$ est $mn$.

**4.2 Cas général.** L'ordre de $ab$ divise $\mathrm{ppcm}(m,n)$ mais peut être plus petit (pour $b=a^{-1}$, il vaut $1$). Posons $m'=\prod p^{v_p(m)}$ sur les premiers $p$ avec $v_p(m)\ge v_p(n)$, et $n'=\prod p^{v_p(n)}$ sur les autres. Alors $m'\mid m$, $n'\mid n$, $m'\wedge n'=1$ et $m'n'=\mathrm{ppcm}(m,n)$. Les éléments $a^{m/m'}$ et $b^{n/n'}$ sont d'ordres $m'$ et $n'$, et leur produit est d'ordre $m'n'$ d'après 4.1.

**4.3 Exposant.** Soit $g$ d'ordre maximal $N$. Pour tout $h$ d'ordre $k$, 4.2 fournit un élément d'ordre $\mathrm{ppcm}(N,k)\ge N$, donc égal à $N$ : $k\mid N$. Ainsi $r=N$ est atteint.

**4.4 Non abélien.** Dans $\mathfrak S_3$, les ordres sont $1,2,3$, donc $r=6$, mais aucun élément n'est d'ordre $6$ (sinon $\mathfrak S_3$ serait cyclique, donc abélien).

**4.5 Corps.** Soit $G\subset K^*$ fini de cardinal $N$ et d'exposant $r$. Par Lagrange, $r\mid N$. Tous les éléments de $G$ sont racines de $X^r-1$, qui a au plus $r$ racines : $N\le r$. Donc $r=N$, et un élément d'ordre $r=N$ engendre $G$.

**Étape 5 — Vérification.**

> **Vérification — Exemples.**
> - $(\mathbb Z/7\mathbb Z)^*$ est cyclique, engendré par $3$ : $3^1,\dots,3^6$ valent $3,2,6,4,5,1$.
> - Les racines $n$-ièmes de l'unité de $\mathbb C$ forment le groupe cyclique engendré par $e^{2i\pi/n}$.

**Étape 6 — Conclusion.**
$$\boxed{m\wedge n=1\Rightarrow\mathrm{ord}(ab)=mn;\quad\exists\,g,\ \mathrm{ord}(g)=\mathrm{ppcm\ des\ ordres};\quad G\subset K^*\text{ fini}\Rightarrow G\text{ cyclique}}$$""",
r"""Ordres premiers entre eux : $\langle a\rangle\cap\langle b\rangle=\{1\}$ donne $\mathrm{ord}(ab)=mn$ ; l'exposant est atteint ; faux pour $\mathfrak S_3$ ; dans un corps, $|G|\le r$ donc $G$ est cyclique.""")
src("D'après un oral de l'École polytechnique.", 'X')

# ---------------------------------------------------------------- 2. (Z/2^nZ)*
ex('n-s-a-deuxn', 'Maths', 'Arithmétique', 2, 'Le groupe des inversibles de ℤ/2ⁿℤ', 20, r"""
Soit $a$ un entier impair.

1. Montrer que $a^{2^{n-2}}\equiv1\pmod{2^n}$ pour tout entier $n\ge3$.
2. En déduire les entiers $n\ge1$ pour lesquels le groupe $(\mathbb Z/2^n\mathbb Z)^*$ est cyclique.
""", r"""Récurrence sur $n$ : pour $n=3$, $a^2=4k(k+1)+1$.""",
r"""Si $a^{2^{n-2}}=1+2^nm$, élève au carré.""",
r"""$(\mathbb Z/2^n\mathbb Z)^*$ a $2^{n-1}$ éléments ; compare avec l'ordre maximal d'un élément.""",
r"""**Étape 1 — Analyse de l'énoncé.** On montre une congruence pour les impairs, puis on l'utilise pour majorer l'ordre des éléments de $(\mathbb Z/2^n\mathbb Z)^*$, ce qui décide de sa cyclicité.

**Étape 2 — Rappels du cours.**

> **Propriété — Inversibles de $\mathbb Z/N\mathbb Z$.** $\bar a$ est inversible si et seulement si $a\wedge N=1$ ; il y en a $\varphi(N)$, et $\varphi(2^n)=2^{n-1}$.

> **Propriété — Groupe cyclique.** Un groupe fini de cardinal $N$ est cyclique si et seulement s'il possède un élément d'ordre $N$.

**Étape 3 — Stratégie.** Une récurrence simple fournit la congruence. Pour $n\ge3$, tout élément a alors un ordre qui divise $2^{n-2}$, strictement plus petit que le cardinal $2^{n-1}$ : le groupe n'est pas cyclique. Les petits cas se traitent à la main.

**Étape 4 — Résolution détaillée.**

**4.1 Initialisation ($n=3$).** $a=2k+1$ : $a^2=4k^2+4k+1=4k(k+1)+1$, et $k(k+1)$ est pair, donc $a^2\equiv1\pmod8$.

**4.2 Hérédité.** Si $a^{2^{n-2}}=1+2^nm$ avec $m\in\mathbb Z$, alors
$$a^{2^{n-1}}=(1+2^nm)^2=1+2^{n+1}m+2^{2n}m^2\equiv1\pmod{2^{n+1}}.$$

**4.3 Non-cyclicité pour $n\ge3$.** Le groupe $(\mathbb Z/2^n\mathbb Z)^*$ a $2^{n-1}$ éléments, et d'après 1 l'ordre de chacun divise $2^{n-2}<2^{n-1}$. Aucun élément n'est d'ordre $2^{n-1}$ : le groupe n'est pas cyclique.

**4.4 Petits cas.** $n=1$ : $\{\bar1\}$, cyclique. $n=2$ : $\{\bar1,\bar3\}$, d'ordre $2$, cyclique.

**Étape 5 — Vérification.**

> **Vérification — $n=3$.** $(\mathbb Z/8\mathbb Z)^*=\{1,3,5,7\}$ et $3^2=9\equiv1$, $5^2=25\equiv1$, $7^2=49\equiv1$ : tous les éléments non triviaux sont d'ordre $2$. C'est le groupe de Klein, non cyclique.

La puissance $2^{n-2}$ est optimale : $5$ est d'ordre exactement $2^{n-2}$ modulo $2^n$.

**Étape 6 — Conclusion.**
$$\boxed{(\mathbb Z/2^n\mathbb Z)^*\text{ est cyclique}\iff n\in\{1,2\}}$$""",
r"""Récurrence : $a^{2^{n-2}}\equiv1\pmod{2^n}$ ; pour $n\ge3$ l'ordre de tout élément divise $2^{n-2}<2^{n-1}$ : cyclique seulement pour $n=1,2$.""")
src("D'après un oral Mines-Ponts.", 'Mines-Ponts')

# ---------------------------------------------------------------- 3. Groupe de Heisenberg
ex('n-s-a-heis', 'Maths', 'Groupes', 2, 'Matrices unitriangulaires sur ℤ/pℤ', 20, r"""
Soit $p\ge3$ un nombre premier et $K=\mathbb Z/p\mathbb Z$. Pour $(a,b,c)\in K^3$, on pose
$$M(a,b,c)=\begin{pmatrix}1&a&b\\0&1&c\\0&0&1\end{pmatrix},\qquad G=\{M(a,b,c),\ (a,b,c)\in K^3\}.$$

1. Montrer que $G$ est un sous-groupe de $GL_3(K)$, non commutatif. Quel est son cardinal ?
2. Déterminer l'ordre de chaque élément de $G$.
3. Que se passe-t-il pour $p=2$ ?
""", r"""Calcule le produit $M(a,b,c)M(a',b',c')$ et l'inverse de $M(a,b,c)$.""",
r"""Écris $M=I_3+N$ avec $N$ triangulaire supérieure stricte, donc $N^3=0$, et développe $M^p$ par le binôme.""",
r"""Pour $p=2$, calcule le carré de $M(1,0,1)$.""",
r"""**Étape 1 — Analyse de l'énoncé.** $G$ est l'ensemble des matrices unitriangulaires supérieures $3\times3$ sur le corps à $p$ éléments. On vérifie la structure de groupe, on compte, puis on calcule les ordres.

**Étape 2 — Rappels du cours.**

> **Propriété — Sous-groupe.** $H\subset G$ est un sous-groupe s'il contient le neutre et est stable par produit et inverse.

> **Formule du binôme.** Si $I$ et $N$ commutent, $(I+N)^p=\sum_{k=0}^p\binom pkN^k$.

> **Propriété — $\binom pk$.** Pour $p$ premier et $1\le k\le p-1$, $p\mid\binom pk$.

**Étape 3 — Stratégie.** Calcul direct pour la structure. Pour les ordres, $N^3=0$ réduit le binôme à trois termes, tous multiples de $p$ sauf le premier quand $p\ge3$.

**Étape 4 — Résolution détaillée.**

**4.1 Groupe.** $M(0,0,0)=I_3$, et
$$M(a,b,c)\,M(a',b',c')=M(a+a',\ b+b'+ac',\ c+c'),\qquad M(a,b,c)^{-1}=M(-a,\ ac-b,\ -c).$$
$G$ est un sous-groupe de $GL_3(K)$, de cardinal $p^3$ (l'application $(a,b,c)\mapsto M(a,b,c)$ est injective). Il n'est pas commutatif : $M(1,0,0)M(0,0,1)=M(1,1,1)$ mais $M(0,0,1)M(1,0,0)=M(1,0,1)$.

**4.2 Ordres.** $M=I_3+N$ avec $N=\begin{pmatrix}0&a&b\\0&0&c\\0&0&0\end{pmatrix}$, donc $N^3=0$. Par le binôme :
$$M^p=I_3+pN+\frac{p(p-1)}2N^2 .$$
Dans $K$, $p=0$ ; et comme $p$ est impair, $\frac{p-1}2$ est entier, donc $\frac{p(p-1)}2\equiv0\pmod p$. Ainsi $M^p=I_3$. L'ordre de $M$ divise $p$ premier : il vaut $1$ si $M=I_3$ et $p$ sinon.

**4.3 Cas $p=2$.** $M(1,0,1)^2=M(0,1,0)\neq I_3$ : cet élément est d'ordre $4$. Le terme $\frac{p(p-1)}2N^2=N^2$ ne s'annule plus.

**Étape 5 — Vérification.**

> **Vérification — Cohérence.** Par Lagrange, l'ordre de chaque élément divise $|G|=p^3$ : les ordres $1$ et $p$ conviennent. Pour $p=2$, $|G|=8$ et l'ordre $4$ est aussi compatible.

**Étape 6 — Conclusion.**
$$\boxed{|G|=p^3,\ G\text{ non abélien},\ \forall M\neq I_3,\ \mathrm{ord}(M)=p\ \ (p\ge3)}$$""",
r"""$M(a,b,c)M(a',b',c')=M(a+a',b+b'+ac',c+c')$, $|G|=p^3$ ; $M^p=I_3+pN+\frac{p(p-1)}2N^2=I_3$ : ordre $p$ (sauf $I_3$). Pour $p=2$, un élément d'ordre $4$.""")
src("D'après un oral Mines-Ponts.", 'Mines-Ponts')

# ---------------------------------------------------------------- 4. P(X²) = P(X)P(X+1)
ex('n-s-a-pxx', 'Maths', 'Polynômes', 2, 'Équation P(X²) = P(X)P(X+1)', 25, r"""
On cherche les polynômes $P\in\mathbb C[X]$ non nuls tels que $P(X^2)=P(X)\,P(X+1)$.

1. Montrer qu'un tel $P$ est unitaire.
2. Montrer que si $\lambda$ est racine de $P$, alors $\lambda^2$ et $(\lambda-1)^2$ le sont aussi.
3. En déduire que toute racine $\lambda$ vérifie : $\lambda=0$ ou $|\lambda|=1$, et $\lambda=1$ ou $|\lambda-1|=1$.
4. Déterminer les complexes $z$ tels que $|z|=|z-1|=1$, et montrer qu'ils ne sont pas racines.
5. Déterminer tous les polynômes solutions.
""", r"""Pour $(\lambda-1)^2$, évalue la relation en $X=\lambda-1$.""",
r"""Si $\lambda\neq0$ et $|\lambda|\neq1$, les racines $\lambda^{2^k}$ ont des modules deux à deux distincts.""",
r"""Les points $e^{\pm i\pi/3}$ : regarde si leurs carrés vérifient les conditions de la question 3. Puis cherche $P=X^a(X-1)^b$.""",
r"""**Étape 1 — Analyse de l'énoncé.** On résout une équation fonctionnelle polynomiale en étudiant l'ensemble $Z$ des racines : il est fini et stable par deux transformations, ce qui le contraint fortement.

**Étape 2 — Rappels du cours.**

> **Propriété — Coefficient dominant.** Le coefficient dominant d'un produit est le produit des coefficients dominants.

> **Propriété — Nombre de racines.** Un polynôme non nul a un nombre fini de racines.

> **Propriété — Factorisation.** Un polynôme unitaire de $\mathbb C[X]$ est le produit des $(X-\lambda)^{m_\lambda}$ sur ses racines.

**Étape 3 — Stratégie.** On montre que $Z\subset\{0,1\}$ grâce aux deux stabilités et à un argument de modules, puis on identifie les exposants en comparant les deux membres.

**Étape 4 — Résolution détaillée.**

**4.1 Unitaire.** Si $c$ est le coefficient dominant et $n$ le degré, les deux membres sont de degré $2n$, de coefficients dominants $c$ et $c^2$. Donc $c=c^2$, et $c=1$ car $c\neq0$.

**4.2 Stabilités.** Si $P(\lambda)=0$ : en $X=\lambda$, $P(\lambda^2)=P(\lambda)P(\lambda+1)=0$. En $X=\lambda-1$, $P\big((\lambda-1)^2\big)=P(\lambda-1)P(\lambda)=0$.

**4.3 Modules.** Si $\lambda\in Z$ avec $\lambda\neq0$ et $|\lambda|\neq1$, les $\lambda^{2^k}\in Z$ ont des modules $|\lambda|^{2^k}$ deux à deux distincts : $Z$ serait infini. Donc $\lambda=0$ ou $|\lambda|=1$. En appliquant ceci à $(\lambda-1)^2\in Z$ : $(\lambda-1)^2=0$ ou $|\lambda-1|^2=1$, c'est-à-dire $\lambda=1$ ou $|\lambda-1|=1$.

**4.4 Points critiques.** $|z|=|z-1|=1$ : $z$ est à distance $1$ de $0$ et de $1$, donc $z=\frac12\pm i\frac{\sqrt3}2=e^{\pm i\pi/3}$. Si $z=e^{i\pi/3}\in Z$, alors $z^2=e^{2i\pi/3}\in Z$, avec $z^2\neq1$ et $|z^2-1|=\sqrt3\neq1$ : contradiction avec 4.3. Même raisonnement pour $e^{-i\pi/3}$.

**4.5 Racines possibles.** Une racine $\lambda\notin\{0,1\}$ vérifierait $|\lambda|=|\lambda-1|=1$, ce qui est exclu. Donc $P=X^a(X-1)^b$ avec $a,b\in\mathbb N$. Alors
$$P(X^2)=X^{2a}(X-1)^b(X+1)^b,\qquad P(X)P(X+1)=X^a(X-1)^b(X+1)^aX^b .$$
L'égalité impose $2a=a+b$, soit $a=b$, et la réciproque est claire.

**Étape 5 — Vérification.**

> **Vérification — $n=1$.** $P=X^2-X$ : $P(X^2)=X^4-X^2$ et $P(X)P(X+1)=X(X-1)(X+1)X=X^2(X^2-1)$. L'égalité est vérifiée.

Le polynôme $X^2-X+1$, de racines $e^{\pm i\pi/3}$, n'est pas solution : $(X^2-X+1)(X^2+X+1)=X^4+X^2+1\neq X^4-X^2+1$.

**Étape 6 — Conclusion.**
$$\boxed{P(X^2)=P(X)P(X+1),\ P\neq0\iff P=(X^2-X)^n,\ n\in\mathbb N}$$""",
r"""Les racines sont dans $\{0,1\}$ (stabilité par $\lambda\mapsto\lambda^2$ et $\lambda\mapsto(\lambda-1)^2$, $e^{\pm i\pi/3}$ exclus) : $P=(X^2-X)^n$, $n\in\mathbb N$.""")
src("D'après un oral Mines-Ponts.", 'Mines-Ponts')

# ---------------------------------------------------------------- 5. P(U) ⊂ U
ex('n-s-a-pu', 'Maths', 'Polynômes', 2, 'Polynômes qui laissent stable le cercle unité', 20, r"""
On note $\mathbb U=\{z\in\mathbb C,\ |z|=1\}$. Pour $P=\sum_{k=0}^na_kX^k\in\mathbb C[X]$ de degré $n$, on pose $P^*=X^n\overline P\big(\tfrac1X\big)=\sum_{k=0}^n\overline{a_{n-k}}X^k$.

1. Montrer que si $P(\mathbb U)\subset\mathbb U$, alors $P(z)P^*(z)=z^n$ pour tout $z\in\mathbb U$.
2. En déduire tous les polynômes $P$ tels que $P(\mathbb U)\subset\mathbb U$.
3. Lesquels vérifient $P(\mathbb U)=\mathbb U$ ?
""", r"""Pour $z\in\mathbb U$, $\bar z=\frac1z$, donc $\overline{P(z)}=\overline P\big(\frac1z\big)$.""",
r"""L'égalité $P(z)P^*(z)=z^n$ a lieu en une infinité de points : c'est une égalité de polynômes.""",
r"""Les diviseurs de $X^n$ dans $\mathbb C[X]$ sont les $cX^m$.""",
r"""**Étape 1 — Analyse de l'énoncé.** On cherche les polynômes de module $1$ sur tout le cercle unité. L'idée est de traduire $|P(z)|^2=1$ en une identité polynomiale grâce au polynôme réciproque $P^*$.

**Étape 2 — Rappels du cours.**

> **Propriété — Conjugué sur le cercle.** Si $|z|=1$, $\bar z=\frac1z$, et $\overline{P(z)}=\overline P(\bar z)$, où $\overline P$ a les coefficients conjugués.

> **Propriété — Rigidité.** Deux polynômes qui coïncident en une infinité de points sont égaux.

**Étape 3 — Stratégie.** On écrit $1=P(z)\overline{P(z)}$ sur $\mathbb U$, on chasse les dénominateurs par $z^n$, on obtient $PP^*=X^n$, puis on lit les diviseurs de $X^n$.

**Étape 4 — Résolution détaillée.**

**4.1 Identité sur le cercle.** $P(\mathbb U)\subset\mathbb U$ impose $P\neq0$. Pour $z\in\mathbb U$ : $1=|P(z)|^2=P(z)\overline P\big(\frac1z\big)$. En multipliant par $z^n$ : $z^n=P(z)\,z^n\overline P\big(\frac1z\big)=P(z)P^*(z)$.

**4.2 Identité polynomiale.** $PP^*-X^n$ s'annule sur $\mathbb U$, infini, donc $PP^*=X^n$. Ainsi $P$ divise $X^n$ : $P=cX^m$ avec $c\neq0$ ; comme $\deg P=n$, $m=n$. Enfin $|P(1)|=|c|=1$.

**4.3 Réciproque.** Pour $|c|=1$ et $z\in\mathbb U$, $|cz^n|=1$ : $P=cX^n$ convient.

**4.4 Surjectivité.** Si $n\ge1$, $z\mapsto cz^n$ est surjective de $\mathbb U$ sur $\mathbb U$ (tout $w=e^{i\theta}$ est atteint en $z=e^{i(\theta-\arg c)/n}$). Si $n=0$, l'image est le point $\{c\}$.

**Étape 5 — Vérification.**

> **Vérification — Contre-exemples.**
> - $P=\frac{1+X}2$ envoie $\mathbb U$ dans le disque fermé mais pas dans $\mathbb U$ : $P(-1)=0$.
> - Les fractions rationnelles $\frac{X-a}{1-\bar aX}$ ($|a|<1$) laissent $\mathbb U$ stable sans être des monômes : le résultat est propre aux polynômes.

**Étape 6 — Conclusion.**
$$\boxed{P(\mathbb U)\subset\mathbb U\iff P=cX^n,\ |c|=1;\qquad P(\mathbb U)=\mathbb U\iff P=cX^n,\ |c|=1,\ n\ge1}$$""",
r"""Sur $\mathbb U$, $PP^*=X^n$, donc $P\mid X^n$ : $P=cX^n$ avec $|c|=1$ ; surjectif sur $\mathbb U$ si et seulement si $n\ge1$.""")
src("D'après un oral Mines-Ponts.", 'Mines-Ponts')

# ---------------------------------------------------------------- 6. P'² − PP''
ex('n-s-a-pprime', 'Maths', 'Polynômes', 2, 'P′² − PP″ n’a pas de racine réelle', 15, r"""
Soit $P\in\mathbb C[X]$ de degré $n\ge2$ dont toutes les racines sont réelles et simples. Montrer que le polynôme $Q=P'^2-PP''$ n'a aucune racine réelle.
""", r"""Écris $P=\lambda\prod_k(X-a_k)$ et calcule la dérivée de $\frac{P'}P$.""",
r"""Hors des racines de $P$, $Q=P^2\sum_k\frac1{(X-a_k)^2}$.""",
r"""Aux racines $a_k$, $Q(a_k)=P'(a_k)^2$ : utilise la simplicité.""",
r"""**Étape 1 — Analyse de l'énoncé.** $P$ a $n$ racines réelles distinctes $a_1,\dots,a_n$ et un coefficient dominant $\lambda\in\mathbb C^*$. On veut $Q(x)\neq0$ pour tout réel $x$.

**Étape 2 — Rappels du cours.**

> **Propriété — Dérivée logarithmique.** Si $P=\lambda\prod(X-a_k)$, alors hors des racines $\dfrac{P'}P=\sum_k\dfrac1{X-a_k}$.

> **Propriété — Racine simple.** $a$ est racine simple de $P$ si et seulement si $P(a)=0$ et $P'(a)\neq0$.

**Étape 3 — Stratégie.** On distingue les réels qui sont racines de $P$ et les autres. Pour les seconds, la dérivée logarithmique donne une expression de $Q$ comme produit de termes non nuls.

**Étape 4 — Résolution détaillée.**

**4.1 Hors des racines.** En dérivant $\frac{P'}P$ :
$$\frac{P''P-P'^2}{P^2}=-\sum_k\frac1{(X-a_k)^2},\qquad\text{donc}\qquad Q=P^2\sum_{k=1}^n\frac1{(X-a_k)^2}.$$
Pour $x$ réel non racine : $P(x)^2=\lambda^2\prod_k(x-a_k)^2\neq0$ et $\sum_k\frac1{(x-a_k)^2}>0$. Donc $Q(x)\neq0$ (et $|Q(x)|=|\lambda|^2\prod(x-a_k)^2\sum\frac1{(x-a_k)^2}>0$).

**4.2 En une racine.** $Q(a_k)=P'(a_k)^2-0=P'(a_k)^2\neq0$, car $a_k$ est simple.

**Étape 5 — Vérification.**

> **Vérification — Exemples.**
> - $P=X^2-1$ : $Q=4X^2-2(X^2-1)=2X^2+2$, sans racine réelle.
> - Avec une racine double, $P=X^2$ : $Q=4X^2-2X^2=2X^2$ s'annule en $0$. L'hypothèse de simplicité est nécessaire.

**Étape 6 — Conclusion.**
$$\boxed{Q=P'^2-PP''=P^2\sum_k\frac1{(X-a_k)^2}\ \text{hors des racines, et}\ Q(a_k)=P'(a_k)^2\neq0:\ Q\text{ n'a pas de racine réelle}}$$""",
r"""$Q=P^2\sum\frac1{(X-a_k)^2}\neq0$ hors des racines, et $Q(a_k)=P'(a_k)^2\neq0$ (racines simples).""")
src("D'après un oral Centrale.", 'Centrale')

# ---------------------------------------------------------------- 7. Quotient de polynômes cyclotomiques
ex('n-s-a-quot', 'Maths', 'Polynômes', 2, 'Un quotient à coefficients entiers', 20, r"""
Soient $p,q\ge1$ deux entiers premiers entre eux. On pose $A=(1-X^p)(1-X^q)$ et $B=(1-X^{pq})(1-X)$.

1. Montrer que $A$ divise $B$ dans $\mathbb C[X]$, puis que le quotient $Q=\frac BA$ est à coefficients entiers.
2. Calculer $\deg Q$, $Q(0)$ et $Q(1)$.
""", r"""Compare les racines (avec multiplicités) de $A$ et de $B$ : ce sont des racines de l'unité.""",
r"""Une racine commune à $X^p-1$ et $X^q-1$ est une racine $d$-ième de l'unité avec $d=p\wedge q=1$.""",
r"""Pour $Q(1)$, écris $Q=\frac{1-X^{pq}}{1-X^p}\cdot\frac{1-X}{1-X^q}$ et reconnais deux sommes géométriques.""",
r"""**Étape 1 — Analyse de l'énoncé.** $A$ et $B$ sont des produits de polynômes $1-X^k$, dont les racines sont des racines de l'unité. On compare les multiplicités, puis on passe de $\mathbb C[X]$ à $\mathbb Z[X]$.

**Étape 2 — Rappels du cours.**

> **Propriété — Racines de $X^k-1$.** $X^k-1$ a pour racines les $k$ racines $k$-ièmes de l'unité, toutes simples. Une racine commune à $X^p-1$ et $X^q-1$ est une racine de $X^{p\wedge q}-1$.

> **Propriété — Division euclidienne.** Si $A\in\mathbb Z[X]$ a un coefficient dominant égal à $\pm1$, la division euclidienne de $B\in\mathbb Z[X]$ par $A$ se fait dans $\mathbb Z[X]$, et le quotient est le même que dans $\mathbb C[X]$.

**Étape 3 — Stratégie.** Chaque racine de $A$ est racine de $B$ avec une multiplicité au moins égale : $A\mid B$. L'unicité de la division euclidienne donne un quotient entier. On évalue ensuite $Q$ via des sommes géométriques.

**Étape 4 — Résolution détaillée.**

**4.1 Racines de $A$.** Les racines de $1-X^p$ et de $1-X^q$ sont simples. Une racine commune vérifie $z^p=z^q=1$, donc $z^{p\wedge q}=z=1$. Ainsi $1$ est racine double de $A$, et les autres racines de $A$ (racines $p$-ièmes ou $q$-ièmes de l'unité différentes de $1$) sont simples.

**4.2 Racines de $B$.** Les racines $p$-ièmes et $q$-ièmes de l'unité sont des racines $pq$-ièmes, donc racines de $1-X^{pq}$. Le nombre $1$ est racine de $1-X^{pq}$ et de $1-X$ : il est double pour $B$. Toutes les racines de $A$ sont donc racines de $B$ avec au moins la même multiplicité : $A\mid B$ dans $\mathbb C[X]$.

**4.3 Coefficients entiers.** Le coefficient dominant de $A$ est $(-1)(-1)=1$. La division euclidienne de $B$ par $A$ dans $\mathbb Z[X]$ donne $B=AQ_1+R_1$ ; par unicité dans $\mathbb C[X]$, $R_1=0$ et $Q=Q_1\in\mathbb Z[X]$.

**4.4 Valeurs.** $\deg Q=pq+1-p-q=(p-1)(q-1)$ et $Q(0)=\frac{B(0)}{A(0)}=1$. Comme fractions rationnelles,
$$Q=\big(1+X^p+\dots+X^{p(q-1)}\big)\cdot\frac1{1+X+\dots+X^{q-1}},$$
donc $Q(1)=q\cdot\frac1q=1$.

**Étape 5 — Vérification.**

> **Vérification — $p=2$, $q=3$.** $Q=\frac{(1-X^6)(1-X)}{(1-X^2)(1-X^3)}=X^2-X+1$ : degré $(2-1)(3-1)=2$, $Q(0)=Q(1)=1$.

Sans l'hypothèse $p\wedge q=1$ (par exemple $p=q=2$), $1$ et $-1$ seraient racines doubles de $A$ et la divisibilité tomberait.

**Étape 6 — Conclusion.**
$$\boxed{Q=\frac{(1-X^{pq})(1-X)}{(1-X^p)(1-X^q)}\in\mathbb Z[X],\quad\deg Q=(p-1)(q-1),\quad Q(0)=Q(1)=1}$$""",
r"""Racines de $A$ toutes racines de $B$ (seul $1$ est double), $A$ unitaire donc $Q\in\mathbb Z[X]$ ; $\deg Q=(p-1)(q-1)$, $Q(0)=Q(1)=1$.""")
src("D'après un oral Centrale.", 'Centrale')

# ---------------------------------------------------------------- 8. Mesure de Mahler
ex('n-s-a-mahler', 'Maths', 'Polynômes', 2, 'Coefficients et mesure de Mahler', 20, r"""
Soit $P=\sum_{k=0}^na_kX^k\in\mathbb C[X]$ unitaire de degré $n$, de racines $\lambda_1,\dots,\lambda_n$ (avec multiplicité). On pose $M(P)=\prod_{k=1}^n\max(1,|\lambda_k|)$.

1. Montrer que $|a_k|\le\binom nk M(P)$ pour tout $k\in[\![0,n]\!]$.
2. En déduire que $\sum_{k=0}^n|a_k|\le2^nM(P)$. Cas d'égalité pour un exemple simple ?
""", r"""Relations coefficients-racines : $a_{n-j}=(-1)^j\sigma_j(\lambda_1,\dots,\lambda_n)$.""",
r"""Majore chaque produit $\prod_{i\in I}|\lambda_i|$ par $\prod_{i\in I}\max(1,|\lambda_i|)$, puis par $M(P)$.""",
r"""$\sum_k\binom nk=2^n$ ; essaie $P=(X+1)^n$.""",
r"""**Étape 1 — Analyse de l'énoncé.** $M(P)$ est la mesure de Mahler : produit des modules des racines extérieures au disque unité. On veut borner les coefficients par $M(P)$.

**Étape 2 — Rappels du cours.**

> **Propriété — Relations coefficients-racines.** Pour $P$ unitaire, $a_{n-j}=(-1)^j\sigma_j$, où $\sigma_j=\sum_{|I|=j}\prod_{i\in I}\lambda_i$, la somme portant sur les parties $I\subset[\![1,n]\!]$ à $j$ éléments.

> **Propriété — Coefficients binomiaux.** Il y a $\binom nj$ parties à $j$ éléments, et $\sum_j\binom nj=2^n$.

**Étape 3 — Stratégie.** On majore $|\sigma_j|$ par l'inégalité triangulaire, puis chaque produit partiel par le produit complet des $\max(1,|\lambda_i|)$, qui sont tous $\ge1$.

**Étape 4 — Résolution détaillée.**

**4.1 Majoration de $\sigma_j$.** Pour $|I|=j$ :
$$\prod_{i\in I}|\lambda_i|\le\prod_{i\in I}\max(1,|\lambda_i|)\le\prod_{i=1}^n\max(1,|\lambda_i|)=M(P),$$
la seconde inégalité car les facteurs ajoutés sont $\ge1$. Donc $|\sigma_j|\le\binom njM(P)$.

**4.2 Coefficients.** $|a_{n-j}|=|\sigma_j|\le\binom njM(P)$. Avec $k=n-j$ et $\binom n{n-k}=\binom nk$ : $|a_k|\le\binom nkM(P)$.

**4.3 Somme.** $\sum_k|a_k|\le M(P)\sum_k\binom nk=2^nM(P)$.

**Étape 5 — Vérification.**

> **Vérification — Égalité.** $P=(X+1)^n$ : toutes les racines valent $-1$, donc $M(P)=1$, et $\sum_k\binom nk=2^n$. Les deux inégalités sont des égalités.

Pour $P=X^n-1$, $M(P)=1$ et $\sum|a_k|=2\le2^n$.

**Étape 6 — Conclusion.**
$$\boxed{|a_k|\le\binom nkM(P),\qquad\sum_{k=0}^n|a_k|\le2^nM(P),\ \text{égalité pour }(X+1)^n}$$""",
r"""$|a_{n-j}|=|\sigma_j|\le\binom njM(P)$ car chaque produit partiel de $\max(1,|\lambda_i|)$ est $\le M(P)$ ; en sommant, $\sum|a_k|\le2^nM(P)$, égalité pour $(X+1)^n$.""")
src("D'après un oral Centrale.", 'Centrale')

# ---------------------------------------------------------------- 9. Racines cinquièmes
ex('n-s-a-cinq', 'Maths', 'Polynômes', 3, 'Dimension de l’espace engendré par les racines cinquièmes', 20, r"""
Soit $\omega=e^{2i\pi/5}$. On considère $\mathbb C$ comme un $\mathbb Q$-espace vectoriel et $F=\mathrm{Vect}_{\mathbb Q}(1,\omega,\omega^2,\omega^3,\omega^4)$.

1. Montrer que $\dim_{\mathbb Q}F\le4$.
2. Montrer que $\Phi=X^4+X^3+X^2+X+1$ est irréductible dans $\mathbb Q[X]$. On pourra utiliser $c=\omega+\omega^4=2\cos\frac{2\pi}5$.
3. En déduire $\dim_{\mathbb Q}F$.
""", r"""$1+\omega+\omega^2+\omega^3+\omega^4=\frac{\omega^5-1}{\omega-1}=0$.""",
r"""$\Phi$ n'a pas de racine réelle. Un facteur de degré $2$ à coefficients réels a pour racines deux racines conjuguées : $\{\omega,\omega^4\}$ ou $\{\omega^2,\omega^3\}$.""",
r"""En divisant $\Phi(\omega)=0$ par $\omega^2$, montre que $c^2+c-1=0$, donc $c\notin\mathbb Q$.""",
r"""**Étape 1 — Analyse de l'énoncé.** On cherche la dimension sur $\mathbb Q$ du sous-espace engendré par les racines cinquièmes de l'unité. Une relation est évidente ; il faut montrer qu'il n'y en a pas d'autre, ce qui revient à l'irréductibilité de $\Phi$.

**Étape 2 — Rappels du cours.**

> **Propriété — Polynômes réels.** Les racines non réelles d'un polynôme à coefficients réels sont deux à deux conjuguées.

> **Propriété — Polynôme minimal.** Si $\omega$ est racine d'un polynôme irréductible $\Phi\in\mathbb Q[X]$ de degré $d$, aucun polynôme non nul de $\mathbb Q[X]$ de degré $<d$ ne s'annule en $\omega$ ; sinon son pgcd avec $\Phi$ serait un facteur strict de $\Phi$.

**Étape 3 — Stratégie.** La relation $1+\omega+\dots+\omega^4=0$ donne $\dim F\le4$. Pour l'égalité, on montre que $1,\omega,\omega^2,\omega^3$ sont libres, via l'irréductibilité de $\Phi$, établie en examinant les factorisations possibles.

**Étape 4 — Résolution détaillée.**

**4.1 Majoration.** $\omega\neq1$ et $\omega^5=1$, donc $\Phi(\omega)=\frac{\omega^5-1}{\omega-1}=0$ : $\omega^4=-(1+\omega+\omega^2+\omega^3)$, et $F=\mathrm{Vect}(1,\omega,\omega^2,\omega^3)$, de dimension $\le4$.

**4.2 La valeur $c$.** En divisant $\Phi(\omega)=0$ par $\omega^2$ : $(\omega^2+\omega^{-2})+(\omega+\omega^{-1})+1=0$. Avec $c=\omega+\omega^{-1}=\omega+\omega^4$, on a $\omega^2+\omega^{-2}=c^2-2$, donc $c^2+c-1=0$ et $c=\frac{-1+\sqrt5}2$ (car $c=2\cos\frac{2\pi}5>0$). Ainsi $c\notin\mathbb Q$.

**4.3 Irréductibilité.** Les racines de $\Phi$ sont $\omega,\omega^2,\omega^3,\omega^4$, aucune réelle : $\Phi$ n'a pas de facteur de degré $1$ (ni de degré $3$, qui en laisserait un de degré $1$). Une factorisation $\Phi=AB$ dans $\mathbb Q[X]$ avec $A$, $B$ unitaires de degré $2$ aurait des facteurs réels, dont les racines sont conjuguées deux à deux : $A=(X-\omega)(X-\omega^4)=X^2-cX+1$ ou $A=(X-\omega^2)(X-\omega^3)$, dont le coefficient de $X$ est $-(\omega^2+\omega^3)=1+c\notin\mathbb Q$. Dans les deux cas, $A\notin\mathbb Q[X]$ : contradiction.

**4.4 Liberté.** Une relation $q_0+q_1\omega+q_2\omega^2+q_3\omega^3=0$ à coefficients rationnels non tous nuls donnerait un polynôme non nul de degré $\le3$ annulant $\omega$, ce qui est exclu par 4.3. Donc $\dim F=4$.

**Étape 5 — Vérification.**

> **Vérification — Numérique.** $c=2\cos72^\circ\approx0{,}618=\frac{\sqrt5-1}2$, et $c^2+c-1\approx0{,}382+0{,}618-1=0$.

Plus généralement, pour $p$ premier, les racines $p$-ièmes de l'unité engendrent un $\mathbb Q$-espace de dimension $p-1$.

**Étape 6 — Conclusion.**
$$\boxed{\dim_{\mathbb Q}\mathrm{Vect}(1,\omega,\omega^2,\omega^3,\omega^4)=4}$$""",
r"""Une relation $\sum\omega^k=0$ ; $\Phi=X^4+X^3+X^2+X+1$ est irréductible sur $\mathbb Q$ car $2\cos\frac{2\pi}5=\frac{\sqrt5-1}2\notin\mathbb Q$ ; donc $1,\omega,\omega^2,\omega^3$ sont libres : dimension $4$.""")
src("D'après un oral de l'École polytechnique.", 'X')

# ---------------------------------------------------------------- 10. p + q = Id
ex('n-s-a-proj', 'Maths', 'Algèbre linéaire', 1, 'p + q = Id et rangs : deux projecteurs', 15, r"""
Soit $E$ un espace vectoriel de dimension finie $n$ et $p,q\in\mathcal L(E)$ tels que $p+q=\mathrm{Id}_E$ et $\mathrm{rg}(p)+\mathrm{rg}(q)\le n$.

1. Montrer que $E=\mathrm{Im}\,p\oplus\mathrm{Im}\,q$.
2. Montrer que $p\circ q=q\circ p=0$.
3. En déduire que $p$ et $q$ sont des projecteurs.
""", r"""Pour $x\in E$, $x=p(x)+q(x)$ : la somme $\mathrm{Im}\,p+\mathrm{Im}\,q$ vaut $E$.""",
r"""Compare les dimensions : $n\le\mathrm{rg}\,p+\mathrm{rg}\,q\le n$.""",
r"""$p\circ q=p-p^2=q\circ p$ a son image dans $\mathrm{Im}\,p\cap\mathrm{Im}\,q$.""",
r"""**Étape 1 — Analyse de l'énoncé.** $p$ et $q$ décomposent l'identité, et la somme de leurs rangs est au plus la dimension. On veut montrer que ce sont les projecteurs associés à une décomposition de $E$.

**Étape 2 — Rappels du cours.**

> **Propriété — Somme directe.** Si $E=F+G$ et $\dim F+\dim G\le\dim E$, alors $E=F\oplus G$ (et l'inégalité est une égalité), car $\dim(F+G)=\dim F+\dim G-\dim(F\cap G)$.

> **Définition — Projecteur.** $p$ est un projecteur si $p\circ p=p$.

**Étape 3 — Stratégie.** On obtient la somme directe par un argument de dimension. Ensuite $p\circ q$ et $q\circ p$ valent tous deux $p-p^2$, et leur image tombe dans l'intersection nulle.

**Étape 4 — Résolution détaillée.**

**4.1 Somme directe.** Tout $x$ s'écrit $x=p(x)+q(x)$, donc $E=\mathrm{Im}\,p+\mathrm{Im}\,q$. Alors $n=\dim(\mathrm{Im}\,p+\mathrm{Im}\,q)=\mathrm{rg}\,p+\mathrm{rg}\,q-\dim(\mathrm{Im}\,p\cap\mathrm{Im}\,q)\le n-\dim(\mathrm{Im}\,p\cap\mathrm{Im}\,q)$. Donc $\mathrm{Im}\,p\cap\mathrm{Im}\,q=\{0\}$ et $E=\mathrm{Im}\,p\oplus\mathrm{Im}\,q$.

**4.2 Produits nuls.** $q=\mathrm{Id}-p$ donne $p\circ q=p-p^2=q\circ p$. Pour $x\in E$, $p(q(x))\in\mathrm{Im}\,p$ et $q(p(x))\in\mathrm{Im}\,q$ ; ces deux vecteurs sont égaux, donc dans l'intersection : ils sont nuls. Ainsi $p\circ q=q\circ p=0$.

**4.3 Projecteurs.** $p-p^2=p\circ q=0$ donne $p^2=p$. De même $q^2=q-q\circ p=q$.

**Étape 5 — Vérification.**

> **Vérification — Contre-exemple sans l'hypothèse de rang.** Dans $\mathbb R^2$, $p=2\,\mathrm{Id}$ et $q=-\mathrm{Id}$ vérifient $p+q=\mathrm{Id}$ mais $\mathrm{rg}\,p+\mathrm{rg}\,q=4>2$, et $p^2=4\,\mathrm{Id}\neq p$.

**Étape 6 — Conclusion.**
$$\boxed{E=\mathrm{Im}\,p\oplus\mathrm{Im}\,q,\quad p\circ q=q\circ p=0,\quad p^2=p,\ q^2=q}$$""",
r"""$E=\mathrm{Im}\,p+\mathrm{Im}\,q$ et les rangs donnent une somme directe ; $p\circ q=p-p^2=q\circ p$ est à valeurs dans l'intersection, donc nul : $p^2=p$, $q^2=q$.""")
src("D'après un oral CCINP.", 'CCINP')
