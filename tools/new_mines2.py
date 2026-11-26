# Mathématiques — 6 exercices difficiles et élégants (probabilités, réduction, topologie), énoncés et corrigés originaux.
from newlib import ex, E

def mp():
    E[-1]['enonce'] += "\n\n*Dans l'esprit des oraux Mines-Ponts.*"
    E[-1]['concours'] = 'Mines-Ponts'
    E[-1]['ajout'] = '2026-11-26'

# ------------------------------------------------------------ P1. Urne de Pólya
ex('n-mp-polya', 'Maths', 'Probabilités', 3, 'L’urne de Pólya devient uniforme', 25, r"""
Une urne contient initialement une boule rouge et une boule bleue. À chaque étape, on tire une boule au hasard, on la remet, et on ajoute une boule **de la même couleur**. On note $R_n$ le nombre de boules rouges après $n$ tirages (il y a alors $n+2$ boules).

1. Montrer que $R_n$ suit la loi uniforme sur $\{1,\dots,n+1\}$.
2. Montrer que, pour tout $n$, la probabilité que le $(n+1)$-ième tirage donne une boule rouge vaut $\frac12$.
3. On pose $Y_n=\frac{R_n}{n+2}$ (proportion de rouges). Montrer que $P(Y_n\le x)\to x$ pour tout $x\in[0,1]$.
""", r"""Calcule les lois de $R_1$ et $R_2$ à la main : que remarques-tu ? Comment passer de la loi de $R_n$ à celle de $R_{n+1}$ ?""",
r"""Formule des probabilités totales avec le système complet $(R_n=j)_j$ : seuls deux états de $R_n$ peuvent mener à $R_{n+1}=k$.""",
r"""$P(R_{n+1}=k)=P(R_n=k-1)\frac{k-1}{n+2}+P(R_n=k)\frac{n+2-k}{n+2}$ ; par récurrence, remplace les deux probabilités par $\frac1{n+1}$. Pour 2, conditionne par $R_n$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Un modèle où « les riches s'enrichissent » : chaque tirage renforce la couleur tirée. Le résultat surprenant est que la composition de l'urne est **uniforme**, et que chaque tirage reste équilibré.

**Étape 2 — Rappels du cours.**

> **Théorème — Probabilités totales.** Si $(B_j)$ est un système complet d'événements, $P(A)=\sum_jP(B_j)\,P_{B_j}(A)$.

> **Définition — Loi uniforme.** $X$ suit la loi uniforme sur un ensemble fini $F$ si $P(X=x)=\frac1{|F|}$ pour tout $x\in F$.

**Étape 3 — Stratégie.** Récurrence sur $n$ par probabilités totales ; puis conditionnement par $R_n$ pour la couleur du tirage suivant ; enfin un simple comptage pour la loi de la proportion.

**Étape 4 — Résolution détaillée.**

**4.1 Loi de $R_n$.** $R_0=1$ : uniforme sur $\{1\}$. Supposons $R_n$ uniforme sur $\{1,\dots,n+1\}$. Si $R_n=j$, le tirage suivant est rouge avec probabilité $\frac j{n+2}$, et alors $R_{n+1}=j+1$ ; sinon $R_{n+1}=j$. Pour $k\in\{1,\dots,n+2\}$, par probabilités totales :
$$P(R_{n+1}=k)=P(R_n=k-1)\,\frac{k-1}{n+2}+P(R_n=k)\,\frac{n+2-k}{n+2}.$$
Pour $2\le k\le n+1$, les deux probabilités valent $\frac1{n+1}$ : $P(R_{n+1}=k)=\frac{(k-1)+(n+2-k)}{(n+1)(n+2)}=\frac1{n+2}$. Pour $k=1$, le premier terme est nul ($R_n\ge1$) et le second vaut $\frac{1}{n+1}\cdot\frac{n+1}{n+2}=\frac1{n+2}$. Pour $k=n+2$, le second terme est nul et le premier vaut $\frac1{n+1}\cdot\frac{n+1}{n+2}=\frac1{n+2}$. Donc $R_{n+1}$ est uniforme sur $\{1,\dots,n+2\}$.

**4.2 Tirage équilibré.** Notons $A$ l'événement « le $(n+1)$-ième tirage est rouge ». Par probabilités totales :
$$P(A)=\sum_{j=1}^{n+1}\frac1{n+1}\cdot\frac j{n+2}=\frac1{(n+1)(n+2)}\cdot\frac{(n+1)(n+2)}2=\frac12.$$

**4.3 Loi limite de la proportion.** Pour $x\in[0,1]$, $P(Y_n\le x)=P\big(R_n\le x(n+2)\big)=\frac{\min\big(n+1,\lfloor x(n+2)\rfloor\big)}{n+1}$, car $R_n$ est uniforme sur $\{1,\dots,n+1\}$. Comme $\lfloor x(n+2)\rfloor=x(n+2)+O(1)$, ce rapport tend vers $x$ (pour $x=1$, il vaut $1$).

**Étape 5 — Vérification.**

> **Vérification — $n=1$ et $n=2$.** $R_1\in\{1,2\}$ avec probabilités $\frac12,\frac12$ ✓. $P(R_2=1)=\frac12\cdot\frac23=\frac13$, $P(R_2=3)=\frac12\cdot\frac23=\frac13$, donc $P(R_2=2)=\frac13$ ✓.

**Étape 6 — Conclusion.**
$$\boxed{R_n\sim\mathcal U(\{1,\dots,n+1\}),\qquad P(\text{tirage }n+1\text{ rouge})=\tfrac12,\qquad P(Y_n\le x)\to x}$$""",
r"""Récurrence par probabilités totales : $P(R_{n+1}=k)=\frac{1}{n+1}\cdot\frac{(k-1)+(n+2-k)}{n+2}=\frac1{n+2}$ ; chaque tirage est rouge avec probabilité $\frac12$ ; la proportion suit asymptotiquement la loi uniforme sur $[0,1]$.""")
mp()

# ------------------------------------------------------------ P2. Matrice aléatoire inversible
ex('n-mp-glnp', 'Maths', 'Probabilités', 3, 'Une matrice au hasard est-elle inversible ?', 30, r"""
Soit $p$ un nombre premier et $n\ge1$. On choisit une matrice $M$ uniformément au hasard dans $\mathcal M_n(\mathbb Z/p\mathbb Z)$ (les $n^2$ coefficients sont indépendants et uniformes).

1. Montrer que $P(M\in GL_n(\mathbb Z/p\mathbb Z))=\prod_{j=1}^n\big(1-p^{-j}\big)$.
2. Montrer que cette probabilité admet une limite $L_p>0$ quand $n\to+\infty$.
3. Montrer que $L_2\ge\frac14$ et que $L_p\ge1-\frac1{p-1}$ pour $p\ge3$. Que vaut $\lim_{p\to+\infty}L_p$ ?
""", r"""Une matrice est inversible si et seulement si ses colonnes forment une base. Combien de choix pour la première colonne, puis pour la deuxième ?""",
r"""Dénombrement colonne par colonne : la colonne $k+1$ doit éviter le sous-espace engendré par les $k$ premières, qui a $p^k$ éléments. Pour la limite, passe au logarithme et compare $\ln(1-x)$ à $-x$.""",
r"""Pour la minoration, utilise $\prod(1-a_j)\ge1-\sum a_j$ (pour $a_j\in[0,1]$), en isolant éventuellement le premier facteur.""",
r"""**Étape 1 — Analyse de l'énoncé.** On mélange algèbre linéaire sur le corps $\mathbb Z/p\mathbb Z$, dénombrement et produits infinis. Le résultat frappant : même pour des matrices immenses, la probabilité d'être inversible ne tend pas vers $0$.

**Étape 2 — Rappels du cours.**

> **Propriété — Corps $\mathbb Z/p\mathbb Z$.** Pour $p$ premier, $\mathbb Z/p\mathbb Z$ est un corps ; un sous-espace de dimension $k$ de $(\mathbb Z/p\mathbb Z)^n$ a $p^k$ éléments.

> **Propriété — Inversibilité.** $M\in\mathcal M_n(\mathbb K)$ est inversible si et seulement si ses colonnes forment une base de $\mathbb K^n$.

> **Propriété — Inégalité de Weierstrass.** Pour $a_1,\dots,a_N\in[0,1]$, $\prod(1-a_j)\ge1-\sum a_j$ (récurrence).

**Étape 3 — Stratégie.** Compter $GL_n(\mathbb Z/p\mathbb Z)$ colonne par colonne, diviser par $p^{n^2}$ ; suite décroissante minorée, puis logarithme pour la stricte positivité ; inégalité de Weierstrass pour les minorations.

**Étape 4 — Résolution détaillée.**

**4.1 Dénombrement.** Les colonnes $C_1,\dots,C_n$ forment une base si et seulement si, pour tout $k$, $C_{k+1}\notin\operatorname{Vect}(C_1,\dots,C_k)$ (et $C_1\ne0$). Si $C_1,\dots,C_k$ sont libres, leur span a $p^k$ éléments, donc il reste $p^n-p^k$ choix pour $C_{k+1}$. Ainsi
$$|GL_n(\mathbb Z/p\mathbb Z)|=\prod_{k=0}^{n-1}(p^n-p^k),\qquad P_n=\frac{|GL_n|}{p^{n^2}}=\prod_{k=0}^{n-1}\big(1-p^{k-n}\big)=\prod_{j=1}^n\big(1-p^{-j}\big).$$

**4.2 Limite strictement positive.** $P_{n+1}=P_n(1-p^{-(n+1)})\le P_n$ : la suite décroît et est positive, donc converge vers $L_p\ge0$. De plus $\ln P_n=\sum_{j=1}^n\ln(1-p^{-j})$ ; comme $\ln(1-p^{-j})\sim-p^{-j}$ et que $\sum p^{-j}$ converge, la série $\sum\ln(1-p^{-j})$ converge (termes de signe constant) vers un réel $\ell$. Donc $L_p=e^\ell>0$.

**4.3 Minorations.** Pour $p\ge3$, Weierstrass donne $P_n\ge1-\sum_{j\ge1}p^{-j}=1-\frac1{p-1}$, donc $L_p\ge1-\frac1{p-1}$. Pour $p=2$, cette borne est nulle ; on isole le premier facteur : $P_n=\frac12\prod_{j=2}^n(1-2^{-j})\ge\frac12\Big(1-\sum_{j\ge2}2^{-j}\Big)=\frac12\cdot\frac12=\frac14$. Enfin $1-\frac1{p-1}\le L_p\le1$ donne $L_p\to1$ quand $p\to+\infty$.

**Étape 5 — Vérification.**

> **Vérification — $n=1$ et $n=2$, $p=2$.** $n=1$ : seule la matrice $(1)$ est inversible, $P_1=\frac12=1-2^{-1}$ ✓. $n=2$ : $|GL_2(\mathbb Z/2\mathbb Z)|=(4-1)(4-2)=6$ sur $16$ matrices, et $(1-\frac12)(1-\frac14)=\frac38=\frac6{16}$ ✓. Numériquement $L_2\approx0{,}289$.

**Étape 6 — Conclusion.**
$$\boxed{P\big(M\in GL_n(\mathbb Z/p\mathbb Z)\big)=\prod_{j=1}^n(1-p^{-j})\xrightarrow[n\to\infty]{}L_p>0,\qquad L_2\ge\tfrac14,\quad L_p\xrightarrow[p\to\infty]{}1}$$""",
r"""Colonne par colonne : $|GL_n|=\prod_{k<n}(p^n-p^k)$, d'où $P_n=\prod_{j\le n}(1-p^{-j})$ ; suite décroissante dont le logarithme est une série convergente : $L_p>0$ ; Weierstrass : $L_2\ge\frac14$, $L_p\ge1-\frac1{p-1}\to1$.""")
mp()

# ------------------------------------------------------------ R1. Trace nulle et commutateurs
ex('n-mp-commutateur', 'Maths', 'Réduction', 3, 'Toute matrice de trace nulle est un commutateur', 35, r"""
Soit $\mathbb K=\mathbb R$ ou $\mathbb C$ et $n\ge1$.

1. Montrer qu'il n'existe pas de matrices $X,Y\in\mathcal M_n(\mathbb K)$ telles que $XY-YX=I_n$.
2. Soit $u\in\mathcal L(\mathbb K^n)$ qui n'est pas une homothétie. Montrer qu'il existe $x$ tel que $(x,u(x))$ soit libre.
3. Montrer que toute matrice $A$ de trace nulle est semblable à une matrice de diagonale nulle.
4. Soit $D=\mathrm{diag}(1,2,\dots,n)$. Montrer que toute matrice $C$ de diagonale nulle s'écrit $C=DB-BD$.
5. En déduire : $\operatorname{tr}A=0\iff$ il existe $X,Y$ telles que $A=XY-YX$.
""", r"""Quelle quantité est nulle pour tout commutateur $XY-YX$, mais pas pour $I_n$ ? Et si tout vecteur est propre pour $u$, que peut-on dire de $u$ ?""",
r"""Pour 3, récurrence sur $n$ : construis une base commençant par $x,u(x)$ ; dans cette base, le coefficient $(1,1)$ est nul, et le bloc restant est encore de trace nulle.""",
r"""Pour 4, calcule $(DB-BD)_{ij}=(i-j)\,b_{ij}$ et choisis $b_{ij}$. Pour 5, si $A=PCP^{-1}$, conjugue $D$ et $B$ par $P$.""",
r"""**Étape 1 — Analyse de l'énoncé.** La trace d'un commutateur est nulle ; le résultat remarquable est la réciproque : la trace est la **seule** obstruction. On procède en deux temps : rendre la diagonale nulle par similitude, puis écrire une matrice de diagonale nulle comme commutateur explicite.

**Étape 2 — Rappels du cours.**

> **Propriété — Trace.** $\operatorname{tr}(XY)=\operatorname{tr}(YX)$, donc $\operatorname{tr}(XY-YX)=0$ ; la trace est invariante par similitude.

> **Propriété — Homothéties.** Si tout vecteur non nul est vecteur propre de $u$, alors $u$ est une homothétie.

> **Théorème — Base incomplète.** Toute famille libre se complète en une base.

**Étape 3 — Stratégie.** Trace pour 1 ; contraposée pour 2 ; récurrence par blocs pour 3 ; calcul coefficient par coefficient pour 4 ; conjugaison pour 5.

**Étape 4 — Résolution détaillée.**

**4.1 Pas de commutateur égal à $I_n$.** $\operatorname{tr}(XY-YX)=0\ne n=\operatorname{tr}I_n$.

**4.2 Un vecteur non propre.** Si pour tout $x$ la famille $(x,u(x))$ était liée, tout $x\ne0$ serait vecteur propre, et $u$ serait une homothétie (rappel). Contraposée : il existe $x$ avec $(x,u(x))$ libre.

**4.3 Diagonale nulle.** Récurrence sur $n$. Pour $n=1$, $A=(0)$. Soit $n\ge2$ et $A$ de trace nulle, d'endomorphisme $u$. Si $u=\lambda\,\mathrm{Id}$, alors $n\lambda=0$, donc $A=0$, de diagonale nulle. Sinon, prenons $x$ comme en 4.2 et complétons $(x,u(x))$ en une base $(x,u(x),e_3,\dots,e_n)$. Comme $u(x)$ est le deuxième vecteur de base, la première colonne de la matrice est $(0,1,0,\dots,0)$ :
$$A\sim A'=\begin{pmatrix}0&L\\c&A_1\end{pmatrix},\qquad\operatorname{tr}A_1=\operatorname{tr}A'=0.$$
Par hypothèse de récurrence, $A_1=QB_1Q^{-1}$ avec $B_1$ de diagonale nulle. Avec $R=\begin{pmatrix}1&0\\0&Q\end{pmatrix}$ : $R^{-1}A'R=\begin{pmatrix}0&LQ\\Q^{-1}c&B_1\end{pmatrix}$, de diagonale nulle.

**4.4 Commutateur explicite.** Pour $B=(b_{ij})$ : $(DB)_{ij}=i\,b_{ij}$ et $(BD)_{ij}=j\,b_{ij}$, donc $(DB-BD)_{ij}=(i-j)\,b_{ij}$. Si $C$ est de diagonale nulle, posons $b_{ij}=\frac{c_{ij}}{i-j}$ pour $i\ne j$ et $b_{ii}=0$ : alors $DB-BD=C$ (les coefficients diagonaux valent $0=c_{ii}$).

**4.5 Conclusion.** Si $\operatorname{tr}A=0$, alors $A=PCP^{-1}$ avec $C$ de diagonale nulle, $C=DB-BD$, donc
$$A=(PDP^{-1})(PBP^{-1})-(PBP^{-1})(PDP^{-1})=XY-YX.$$
La réciproque est 4.1.

**Étape 5 — Vérification.**

> **Vérification — $n=2$.** $A=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ : avec $x=e_1+e_2$, $u(x)=e_1-e_2$, libre avec $x$. Dans la base $(x,u(x))$, $u(u(x))=x$ : la matrice est $\begin{pmatrix}0&1\\1&0\end{pmatrix}$, de diagonale nulle, et $\begin{pmatrix}0&1\\1&0\end{pmatrix}=DB-BD$ avec $D=\mathrm{diag}(1,2)$, $B=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ ✓.

**Étape 6 — Conclusion.**
$$\boxed{\operatorname{tr}A=0\iff\exists\,X,Y\in\mathcal M_n(\mathbb K),\ A=XY-YX\quad(\text{et }XY-YX\ne I_n)}$$""",
r"""Trace d'un commutateur nulle, donc $XY-YX\ne I_n$ ; un vecteur non propre donne une base où le coefficient $(1,1)$ est nul, d'où par récurrence une diagonale nulle ; $(DB-BD)_{ij}=(i-j)b_{ij}$ fournit $B$ ; on conjugue.""")
mp()

# ------------------------------------------------------------ R2. Nilpotence et traces
ex('n-mp-nilptr', 'Maths', 'Réduction', 3, 'Nilpotence lue sur les traces', 25, r"""
Soit $A\in\mathcal M_n(\mathbb C)$.

1. Montrer que $A$ est nilpotente si et seulement si $\operatorname{tr}(A^k)=0$ pour tout $k\in\{1,\dots,n\}$.
2. Soient $A,B\in\mathcal M_n(\mathbb C)$ telles que $AB-BA=A$. Montrer que $A^kB-BA^k=kA^k$ pour tout $k\ge1$.
3. En déduire que $A$ est nilpotente.
""", r"""Si $A$ est trigonalisée, que valent les traces de ses puissances en fonction des valeurs propres ? Et si $A$ n'est pas nilpotente, combien a-t-elle de valeurs propres non nulles distinctes ?""",
r"""Les valeurs propres non nulles distinctes $\mu_1,\dots,\mu_r$, avec multiplicités $m_i\ge1$, vérifient un système linéaire en les $m_i$ : sa matrice est de type Vandermonde.""",
r"""$\det(\mu_i^k)_{1\le k,i\le r}=\mu_1\cdots\mu_r\prod_{i<j}(\mu_j-\mu_i)\ne0$ force $m_i=0$. Pour 2, récurrence : $A^{k+1}B-BA^{k+1}=A(A^kB-BA^k)+(AB-BA)A^k$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Les traces des puissances déterminent les valeurs propres « avec multiplicité » : si elles sont toutes nulles, il ne reste que $0$. Application élégante : une relation de commutation force la nilpotence.

**Étape 2 — Rappels du cours.**

> **Théorème — Trigonalisation.** $A=PTP^{-1}$ avec $T$ triangulaire de diagonale $\lambda_1,\dots,\lambda_n$ (valeurs propres avec multiplicité) ; alors $\operatorname{tr}(A^k)=\sum_i\lambda_i^k$.

> **Propriété — Nilpotence.** $A\in\mathcal M_n(\mathbb C)$ est nilpotente si et seulement si $0$ est sa seule valeur propre.

> **Propriété — Vandermonde.** $\det(x_i^{j-1})=\prod_{i<j}(x_j-x_i)$, non nul si les $x_i$ sont distincts.

**Étape 3 — Stratégie.** Sens direct par trigonalisation ; réciproque par l'absurde et un système de Vandermonde ; récurrence pour la relation de commutation ; trace d'un commutateur nulle.

**Étape 4 — Résolution détaillée.**

**4.1 Sens direct.** Si $A$ est nilpotente, ses valeurs propres sont nulles ; $A^k$ est semblable à $T^k$, triangulaire de diagonale nulle : $\operatorname{tr}(A^k)=0$.

**4.2 Réciproque.** Supposons $\operatorname{tr}(A^k)=0$ pour $1\le k\le n$ et $A$ non nilpotente. Soient $\mu_1,\dots,\mu_r$ ($1\le r\le n$) ses valeurs propres non nulles distinctes, de multiplicités $m_1,\dots,m_r\ge1$. Pour $1\le k\le r$ :
$$0=\operatorname{tr}(A^k)=\sum_{i=1}^rm_i\mu_i^k.$$
Le vecteur $(m_1,\dots,m_r)$ est donc dans le noyau de la matrice $V=(\mu_i^k)_{1\le k,i\le r}$. Or, en factorisant $\mu_i$ dans chaque colonne, $\det V=\mu_1\cdots\mu_r\prod_{i<j}(\mu_j-\mu_i)\ne0$ (Vandermonde, $\mu_i$ non nuls et distincts). Donc $m_i=0$ pour tout $i$, contradiction. $A$ est nilpotente.

**4.3 Relation de commutation.** Pour $k=1$, c'est l'hypothèse. Si $A^kB-BA^k=kA^k$, alors
$$A^{k+1}B-BA^{k+1}=A(A^kB-BA^k)+(AB-BA)A^k=kA^{k+1}+A^{k+1}=(k+1)A^{k+1}.$$

**4.4 Nilpotence.** Par 4.3, $k\,\operatorname{tr}(A^k)=\operatorname{tr}(A^kB-BA^k)=0$, donc $\operatorname{tr}(A^k)=0$ pour tout $k\ge1$. Par 4.2, $A$ est nilpotente.

**Étape 5 — Vérification.**

> **Vérification — Un exemple.** $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ et $B=\mathrm{diag}(0,1)$ : $AB=\begin{pmatrix}0&1\\0&0\end{pmatrix}=A$ et $BA=0$, donc $AB-BA=A$ ✓, et $A$ est bien nilpotente.

**Étape 6 — Conclusion.**
$$\boxed{A\ \text{nilpotente}\iff\forall k\in\{1,\dots,n\},\ \operatorname{tr}(A^k)=0\ ;\qquad AB-BA=A\Rightarrow A\ \text{nilpotente}}$$""",
r"""$\operatorname{tr}(A^k)=\sum m_i\mu_i^k$ ; si les traces sont nulles, le système de Vandermonde force $m_i=0$ : seule la valeur propre $0$ subsiste. $AB-BA=A$ donne $A^kB-BA^k=kA^k$, donc $\operatorname{tr}(A^k)=0$ et $A$ nilpotente.""")
mp()

# ------------------------------------------------------------ T1. Connexité de GL_n
ex('n-mp-glconnexe', 'Maths', 'Topologie & convexité', 3, 'GL_n(ℂ) est connexe par arcs, GL_n(ℝ) non', 30, r"""
1. Montrer que $GL_n(\mathbb R)$ n'est pas connexe par arcs ($n\ge1$).
2. Soient $A,B\in GL_n(\mathbb C)$. Montrer que $P(z)=\det\big((1-z)A+zB\big)$ est un polynôme en $z$ non nul, et en déduire qu'il existe un chemin continu $\gamma:[0,1]\to\mathbb C$ de $0$ à $1$ qui évite ses racines.
3. En déduire que $GL_n(\mathbb C)$ est connexe par arcs.
4. Montrer que toute application continue $f:GL_n(\mathbb C)\to\mathbb Z$ est constante. Est-ce vrai pour $GL_n(\mathbb R)$ ?
""", r"""Quelle fonction continue sur $GL_n(\mathbb R)$ prend des valeurs positives et négatives sans jamais s'annuler ?""",
r"""L'image continue d'un connexe par arcs est connexe par arcs, et dans $\mathbb R$ ce sont les intervalles. Dans $\mathbb C$, au contraire, enlever un nombre fini de points ne déconnecte rien.""",
r"""Considère la famille d'arcs $\gamma_s(t)=t+i\,s\,t(1-t)$, $s\in\mathbb R$ : deux arcs distincts ne se coupent qu'en $0$ et $1$. Combien d'arcs peuvent rencontrer une racine donnée ?""",
r"""**Étape 1 — Analyse de l'énoncé.** Le déterminant sépare $GL_n(\mathbb R)$ en deux morceaux (signe), mais dans $\mathbb C$ il n'y a pas de « signe » : l'ensemble des valeurs interdites est fini, et on le contourne.

**Étape 2 — Rappels du cours.**

> **Propriété — Image d'un connexe par arcs.** L'image d'une partie connexe par arcs par une application continue est connexe par arcs ; les parties connexes par arcs de $\mathbb R$ sont les intervalles.

> **Propriété — Racines.** Un polynôme non nul n'a qu'un nombre fini de racines.

> **Propriété — Continuité.** $M\mapsto\det M$ est continue (polynomiale en les coefficients).

**Étape 3 — Stratégie.** Signe du déterminant pour $\mathbb R$ ; pour $\mathbb C$, segment « tordu » entre $A$ et $B$ le long d'un chemin qui évite les racines de $P$ ; enfin image de $f$ connexe par arcs dans $\mathbb Z$.

**Étape 4 — Résolution détaillée.**

**4.1 Cas réel.** $\det:GL_n(\mathbb R)\to\mathbb R^*$ est continue et surjective ($\det\mathrm{diag}(a,1,\dots,1)=a$). Si $GL_n(\mathbb R)$ était connexe par arcs, $\mathbb R^*$ le serait, donc serait un intervalle : faux, car il contient $-1$ et $1$ mais pas $0$.

**4.2 Le polynôme $P$.** Développer le déterminant montre que $P$ est polynomial en $z$ (de degré $\le n$), et $P(0)=\det A\ne0$, $P(1)=\det B\ne0$ : $P$ est non nul, avec un ensemble fini $Z$ de racines, ne contenant ni $0$ ni $1$.

**4.3 Un chemin qui évite $Z$.** Pour $s\in\mathbb R$, $\gamma_s(t)=t+i\,s\,t(1-t)$ va continûment de $0$ à $1$. Si $\gamma_s(t)=\gamma_{s'}(t')$, les parties réelles donnent $t=t'$, puis $s\,t(1-t)=s'\,t(1-t)$ ; pour $t\in\,]0,1[$, $s=s'$. Ainsi chaque point $z\in Z$ (qui n'est ni $0$ ni $1$) appartient à au plus un arc $\gamma_s$. $Z$ étant fini, il existe $s$ tel que $\gamma_s$ évite $Z$.

**4.4 Connexité de $GL_n(\mathbb C)$.** Avec ce $s$, $\Gamma(t)=(1-\gamma_s(t))A+\gamma_s(t)B$ est continue, $\Gamma(0)=A$, $\Gamma(1)=B$, et $\det\Gamma(t)=P(\gamma_s(t))\ne0$ : $\Gamma$ est un chemin dans $GL_n(\mathbb C)$. Donc $GL_n(\mathbb C)$ est connexe par arcs.

**4.5 Fonctions à valeurs entières.** $f(GL_n(\mathbb C))$ est une partie connexe par arcs de $\mathbb R$ contenue dans $\mathbb Z$ : un intervalle d'entiers, donc un singleton. Pour $GL_n(\mathbb R)$, c'est faux : $f(M)=\operatorname{sgn}(\det M)$ est continue (localement constante) et prend les valeurs $\pm1$.

**Étape 5 — Vérification.**

> **Vérification — $n=1$.** $GL_1(\mathbb C)=\mathbb C^*$ : on relie deux points en contournant $0$ ✓ ; $GL_1(\mathbb R)=\mathbb R^*$ : deux demi-droites disjointes ✓.

**Étape 6 — Conclusion.**
$$\boxed{GL_n(\mathbb R)\ \text{n'est pas connexe par arcs},\qquad GL_n(\mathbb C)\ \text{est connexe par arcs}}$$""",
r"""$\det$ envoie $GL_n(\mathbb R)$ sur $\mathbb R^*$, non connexe ; dans $\mathbb C$, $P(z)=\det((1-z)A+zB)$ n'a qu'un nombre fini de racines, évitées par un arc $t+ist(1-t)$ bien choisi : $GL_n(\mathbb C)$ est connexe par arcs.""")
mp()

# ------------------------------------------------------------ T2. Sous-groupes de R
ex('n-mp-sgR', 'Maths', 'Topologie & convexité', 2, 'Sous-groupes de ℝ et densité de {cos n}', 25, r"""
Soit $G$ un sous-groupe de $(\mathbb R,+)$ non réduit à $\{0\}$, et $a=\inf\big(G\cap\,]0,+\infty[\big)$.

1. Montrer que si $a>0$, alors $a\in G$ et $G=a\mathbb Z$.
2. Montrer que si $a=0$, alors $G$ est dense dans $\mathbb R$.
3. En déduire que $\mathbb Z+\sqrt2\,\mathbb Z$ est dense dans $\mathbb R$.
4. Montrer que $\{\cos n,\ n\in\mathbb N\}$ est dense dans $[-1,1]$.
""", r"""Si $a>0$ n'était pas atteint, on trouverait deux éléments de $G$ très proches dans $]a,2a[$. Que dire de leur différence ?""",
r"""Caractérisation de la borne inférieure et division euclidienne « réelle » : pour $x\in G$, écris $x=ka+r$ avec $k=\lfloor x/a\rfloor$. Si $a=0$, les multiples d'un petit élément de $G$ quadrillent $\mathbb R$.""",
r"""Pour 3, montre que $\mathbb Z+\sqrt2\mathbb Z$ n'est pas de la forme $a\mathbb Z$ (irrationalité). Pour 4, applique le même raisonnement à $\mathbb Z+2\pi\mathbb Z$ et utilise la périodicité et la parité de $\cos$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Classification complète des sous-groupes de $\mathbb R$ : discrets ($a\mathbb Z$) ou denses. On en tire des résultats de densité spectaculaires.

**Étape 2 — Rappels du cours.**

> **Propriété — Borne inférieure.** $a=\inf A$ si et seulement si $a$ minore $A$ et, pour tout $\varepsilon>0$, il existe $x\in A$ avec $x<a+\varepsilon$.

> **Propriété — Densité.** $D$ est dense dans $\mathbb R$ si tout intervalle ouvert non vide rencontre $D$. L'image d'une partie dense par une application continue surjective est dense dans l'image.

**Étape 3 — Stratégie.** Cas $a>0$ par l'absurde puis division euclidienne ; cas $a=0$ par les multiples d'un petit élément ; irrationalité de $\sqrt2$ et de $\pi$ pour exclure le cas discret.

**Étape 4 — Résolution détaillée.**

**4.1 Cas $a>0$.** Si $a\notin G$, il existe $x\in G$ avec $a<x<2a$, puis $y\in G$ avec $a<y<x$. Alors $x-y\in G$ et $0<x-y<a$ : contradiction avec la définition de $a$. Donc $a\in G$ et $a\mathbb Z\subset G$. Pour $x\in G$, posons $k=\lfloor x/a\rfloor$ et $r=x-ka\in[0,a[$ ; $r\in G$, donc $r=0$ (sinon $0<r<a$). Ainsi $G=a\mathbb Z$.

**4.2 Cas $a=0$.** Soit $]\alpha,\beta[$ un intervalle, $\varepsilon=\beta-\alpha>0$. Il existe $g\in G$ avec $0<g<\varepsilon$. Avec $k=\lfloor\alpha/g\rfloor+1$, on a $\alpha<kg\le\alpha+g<\beta$, et $kg\in G$. Donc $G$ est dense.

**4.3 $\mathbb Z+\sqrt2\mathbb Z$.** C'est un sous-groupe non nul. S'il valait $a\mathbb Z$ avec $a>0$, on aurait $1=pa$ et $\sqrt2=qa$ avec $p,q$ entiers non nuls, donc $\sqrt2=\frac qp\in\mathbb Q$ : absurde. Donc $a=0$ et il est dense.

**4.4 $\{\cos n\}$.** De même, $\mathbb Z+2\pi\mathbb Z$ est dense ($\pi$ irrationnel). Soit $x\in[-1,1]$, $x=\cos\theta$. Il existe $n_k+2\pi m_k\to\theta$ ($n_k,m_k\in\mathbb Z$), donc $\cos n_k=\cos(n_k+2\pi m_k)\to\cos\theta=x$ par continuité. Par parité, $\cos n_k=\cos|n_k|$ avec $|n_k|\in\mathbb N$ : $x$ est limite de termes de $\{\cos n,\ n\in\mathbb N\}$.

**Étape 5 — Vérification.**

> **Vérification — Le cas discret existe.** $G=\mathbb Z+\frac12\mathbb Z=\frac12\mathbb Z$ : $a=\frac12$ est atteint ✓. Le cas dense : $\mathbb Q$, avec $a=0$ ✓.

**Étape 6 — Conclusion.**
$$\boxed{G=a\mathbb Z\ (a>0)\ \text{ou}\ G\ \text{dense}\ ;\quad\mathbb Z+\sqrt2\mathbb Z\ \text{dense}\ ;\quad\overline{\{\cos n\}}=[-1,1]}$$""",
r"""Si $a>0$, il est atteint (sinon une différence serait dans $]0,a[$) et la division euclidienne donne $G=a\mathbb Z$ ; si $a=0$, les multiples d'un petit élément sont partout ; l'irrationalité de $\sqrt2$ et $\pi$ exclut le cas discret.""")
mp()
