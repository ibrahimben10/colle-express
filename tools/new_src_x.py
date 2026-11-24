# Exercices d'après les oraux de l'X 2019 (MP) : énoncés reformulés, indices et corrigés originaux.
from newlib import ex, E

def src(texte, concours):
    E[-1]['enonce'] += '\n\n*' + texte + '*'
    E[-1]['concours'] = concours

X19 = "D'après un oral de l'École polytechnique (MP, 2019)."

# ---------------------------------------------------------------- 1. Kronecker
ex('n-s-x-kron', 'Maths', 'Polynômes', 3, 'Racines de module au plus 1 d’un polynôme entier', 30, r"""
Soit $P\in\mathbb Z[X]$ unitaire de degré $d\ge1$, dont toutes les racines complexes $\lambda_1,\dots,\lambda_d$ (comptées avec multiplicité) vérifient $|\lambda_k|\le1$. Pour $n\in\mathbb N$, on pose $s_n=\sum_{k=1}^d\lambda_k^n$.

1. Montrer que $s_n\in\mathbb Z$ pour tout $n$, puis que la suite $(s_n)$ est périodique à partir d'un certain rang.
2. En déduire que chaque $\lambda_k$ est nul ou est une racine de l'unité.
""", r"""Écris la relation de récurrence linéaire que vérifie $(s_n)$ grâce aux coefficients de $P$, avec $s_0=d$.""",
r"""Les $s_n$ sont des entiers bornés par $d$ : le $d$-uplet $(s_n,\dots,s_{n+d-1})$ ne prend qu'un nombre fini de valeurs.""",
r"""Compare deux écritures de la fraction rationnelle $\sum_n s_nt^n$ : $\sum_k\frac1{1-\lambda_kt}$ et une fraction de dénominateur $1-t^p$.""",
r"""**Étape 1 — Analyse de l'énoncé.** $P=X^d+c_{d-1}X^{d-1}+\dots+c_0$ est à coefficients entiers et toutes ses racines sont dans le disque unité fermé. On étudie les sommes de Newton $s_n=\sum_k\lambda_k^n$ : il faut voir qu'elles sont entières et finalement périodiques, puis en tirer que les racines non nulles sont des racines de l'unité (théorème de Kronecker).

**Étape 2 — Rappels du cours.**

> **Propriété — Récurrence des sommes de Newton.** Si $P(\lambda_k)=0$, alors $\lambda_k^nP(\lambda_k)=0$, donc en sommant sur $k$ : $s_{n+d}+c_{d-1}s_{n+d-1}+\dots+c_0s_n=0$ pour tout $n\ge0$.

> **Propriété — Relations coefficients-racines.** $s_1=-c_{d-1}\in\mathbb Z$, et plus généralement les $s_n$ s'expriment avec les coefficients de $P$.

> **Théorème — Décomposition en éléments simples.** La décomposition d'une fraction rationnelle en éléments simples est unique : une fraction $\sum_\mu\frac{m_\mu}{1-\mu t}$, avec des $\mu$ non nuls distincts et des $m_\mu\neq0$, a exactement pour pôles les $\frac1\mu$.

**Étape 3 — Stratégie.** La récurrence à coefficients entiers et les valeurs initiales entières donnent $s_n\in\mathbb Z$. Comme $|s_n|\le d$, un argument de tiroirs sur les blocs de $d$ termes consécutifs donne la périodicité. Pour conclure, on lit les pôles de la série génératrice $\sum s_nt^n$ de deux façons.

**Étape 4 — Résolution détaillée.**

**4.1 Entiers.** $s_0=d$. Pour $1\le n\le d-1$, les identités de Newton $s_n+c_{d-1}s_{n-1}+\dots+c_{d-n+1}s_1+n\,c_{d-n}=0$ montrent par récurrence que $s_n\in\mathbb Z$. Ensuite, la récurrence $s_{n+d}=-(c_{d-1}s_{n+d-1}+\dots+c_0s_n)$ à coefficients entiers propage le caractère entier à tous les $n$.

**4.2 Bornes et périodicité.** $|s_n|\le\sum_k|\lambda_k|^n\le d$. Le vecteur $V_n=(s_n,\dots,s_{n+d-1})$ appartient donc à l'ensemble fini $\{-d,\dots,d\}^d$. Il existe $a<b$ avec $V_a=V_b$. La récurrence d'ordre $d$ détermine la suite à partir de $V_a$ comme à partir de $V_b$, donc $s_{n+p}=s_n$ pour tout $n\ge a$, avec $p=b-a\ge1$.

**4.3 Série génératrice.** Pour $|t|$ petit, $\sum_{n\ge0}s_nt^n=\sum_k\sum_n(\lambda_kt)^n=\sum_\mu\frac{m_\mu}{1-\mu t}$, où $\mu$ parcourt les racines distinctes et $m_\mu$ est leur multiplicité. D'autre part, avec la périodicité :
$$\sum_{n\ge0}s_nt^n=Q(t)+\frac{t^a\,(s_a+s_{a+1}t+\dots+s_{a+p-1}t^{p-1})}{1-t^p},\qquad Q\in\mathbb Z[t].$$
Deux fractions rationnelles égales au voisinage de $0$ sont égales.

**4.4 Pôles.** Le terme $\frac{m_0}{1-0\cdot t}=m_0$ (si $0$ est racine) n'a pas de pôle. Pour $\mu\neq0$, $\frac1\mu$ est un pôle de la première écriture (pôles distincts, coefficients $m_\mu\neq0$, pas de compensation). Les pôles de la seconde écriture sont parmi les $t$ tels que $t^p=1$. Donc $\mu^{-p}=1$, soit $\mu^p=1$ : $\mu$ est une racine de l'unité.

**Étape 5 — Vérification.**

> **Vérification — Exemples.**
> - $P=X^2-X+1$ : racines $e^{\pm i\pi/3}$, $s_n=2\cos\frac{n\pi}3$ est périodique de période $6$, et les racines sont des racines sixièmes de l'unité.
> - L'hypothèse « coefficients entiers » est indispensable : $X-\frac12$ a une racine de module $\le1$ qui n'est pas une racine de l'unité, et $s_n=2^{-n}$ n'est pas entier.

**Étape 6 — Conclusion.**
$$\boxed{\text{Toute racine d'un polynôme unitaire de }\mathbb Z[X]\text{ dont les racines sont de module}\le1\text{ est nulle ou racine de l'unité.}}$$""",
r"""$s_n\in\mathbb Z$, $|s_n|\le d$, donc $(s_n)$ est périodique à partir d'un rang ; la série génératrice $\sum_k\frac1{1-\lambda_kt}$ n'a de pôles qu'aux racines $p$-ièmes de l'unité, d'où $\lambda_k=0$ ou $\lambda_k^p=1$.""")
src(X19, 'X')

# ---------------------------------------------------------------- 2. Newton
ex('n-s-x-newton', 'Maths', 'Polynômes', 3, 'Inégalités de Newton pour un polynôme scindé sur ℝ', 25, r"""
Soit $P=\sum_{k=0}^na_kX^k\in\mathbb R[X]$ de degré $n\ge2$, dont toutes les racines sont réelles.

1. Montrer que $QQ''\le Q'^2$ sur $\mathbb R$ pour tout polynôme $Q$ non constant scindé sur $\mathbb R$.
2. En déduire que $a_{k-1}a_{k+1}\le a_k^2$ pour tout $k\in[\![1,n-1]\!]$.
""", r"""Hors des racines, calcule la dérivée de $\frac{Q'}Q=\sum_i\frac1{X-r_i}$.""",
r"""Les dérivées successives d'un polynôme scindé sur $\mathbb R$ sont scindées sur $\mathbb R$ (théorème de Rolle).""",
r"""Applique la question 1 à $Q=P^{(k-1)}$ au point $0$, en utilisant $a_j=\frac{P^{(j)}(0)}{j!}$.""",
r"""**Étape 1 — Analyse de l'énoncé.** $P$ est réel et scindé sur $\mathbb R$. On veut la log-concavité des coefficients : $a_{k-1}a_{k+1}\le a_k^2$. Les coefficients sont des dérivées en $0$, ce qui suggère une inégalité ponctuelle sur $Q,Q',Q''$.

**Étape 2 — Rappels du cours.**

> **Propriété — Dérivée logarithmique.** Si $Q=c\prod_{i=1}^m(X-r_i)$, alors, hors des racines, $\dfrac{Q'}Q=\sum_{i=1}^m\dfrac1{X-r_i}$.

> **Théorème — Rolle pour les polynômes.** Si $Q$ de degré $m\ge1$ est scindé sur $\mathbb R$, alors $Q'$ est scindé sur $\mathbb R$ : entre deux racines consécutives de $Q$ il y a une racine de $Q'$, et une racine de multiplicité $\alpha$ de $Q$ l'est à l'ordre $\alpha-1$ de $Q'$.

> **Formule de Taylor.** $a_j=\dfrac{P^{(j)}(0)}{j!}$.

**Étape 3 — Stratégie.** On dérive la dérivée logarithmique pour obtenir $QQ''-Q'^2=-Q^2\sum\frac1{(X-r_i)^2}\le0$. On applique ce résultat à $Q=P^{(k-1)}$, scindé par Rolle, au point $0$.

**Étape 4 — Résolution détaillée.**

**4.1 Inégalité ponctuelle.** Hors des racines de $Q$ :
$$\Big(\frac{Q'}Q\Big)'=\frac{Q''Q-Q'^2}{Q^2}=-\sum_{i=1}^m\frac1{(x-r_i)^2}<0,$$
donc $Q(x)Q''(x)<Q'(x)^2$. En une racine $x$ de $Q$ : $Q(x)Q''(x)=0\le Q'(x)^2$. Ainsi $QQ''\le Q'^2$ sur $\mathbb R$.

**4.2 Polynôme auxiliaire.** Soit $k\in[\![1,n-1]\!]$ et $Q=P^{(k-1)}$, de degré $n-k+1\ge2$. Par Rolle appliqué $k-1$ fois, $Q$ est scindé sur $\mathbb R$. De plus :
$$Q(0)=(k-1)!\,a_{k-1},\qquad Q'(0)=k!\,a_k,\qquad Q''(0)=(k+1)!\,a_{k+1}.$$

**4.3 Conclusion.** La question 1 en $0$ donne $(k-1)!\,(k+1)!\,a_{k-1}a_{k+1}\le(k!)^2a_k^2$, soit
$$a_{k-1}a_{k+1}\le\frac{k}{k+1}\,a_k^2\le a_k^2 .$$

**Étape 5 — Vérification.**

> **Vérification — Exemples.**
> - $P=(1+X)^n$ : $a_k=\binom nk$ et $\binom n{k-1}\binom n{k+1}\le\binom nk^2$, inégalité classique.
> - L'hypothèse « scindé sur $\mathbb R$ » est nécessaire : $P=1+X^2$ donne $a_0a_2=1>a_1^2=0$.

On a même obtenu l'inégalité plus forte $a_{k-1}a_{k+1}\le\frac k{k+1}a_k^2$.

**Étape 6 — Conclusion.**
$$\boxed{\forall k\in[\![1,n-1]\!],\quad a_{k-1}a_{k+1}\le\frac k{k+1}a_k^2\le a_k^2}$$""",
r"""$QQ''-Q'^2=-Q^2\sum\frac1{(X-r_i)^2}\le0$, appliqué à $Q=P^{(k-1)}$ en $0$ : $a_{k-1}a_{k+1}\le\frac k{k+1}a_k^2$.""")
src(X19, 'X')

# ---------------------------------------------------------------- 3. Fekete
ex('n-s-x-fekete', 'Maths', 'Suites', 3, 'Suites sous-additives (lemme de Fekete)', 20, r"""
Soit $(x_n)_{n\ge1}$ une suite réelle **sous-additive** : $x_{n+m}\le x_n+x_m$ pour tous $n,m\ge1$. On pose $\ell=\inf_{n\ge1}\frac{x_n}n\in[-\infty,+\infty[$.

1. On suppose $x_n\ge0$ pour tout $n$. Montrer que $\frac{x_n}n\to\ell$.
2. Montrer que la conclusion subsiste sans hypothèse de signe, la limite pouvant valoir $-\infty$.
3. Application : si $u_n>0$ et $u_{n+m}\le u_nu_m$, montrer que $u_n^{1/n}$ converge.
""", r"""Fixe $q\ge1$ et écris la division euclidienne $n=aq+r$ avec $0\le r<q$.""",
r"""La sous-additivité donne $x_n\le a\,x_q+x_r$ (avec la convention $x_0=0$ quand $r=0$).""",
r"""Montre $\limsup\frac{x_n}n\le\frac{x_q}q$ pour tout $q$, puis passe à la borne inférieure.""",
r"""**Étape 1 — Analyse de l'énoncé.** La sous-additivité est l'inégalité triangulaire « dans le temps ». On veut montrer que la moyenne $\frac{x_n}n$ converge, et vers sa borne inférieure.

**Étape 2 — Rappels du cours.**

> **Propriété — Limites supérieure et inférieure.** Une suite réelle converge vers $\ell$ (finie ou $-\infty$) si et seulement si $\limsup u_n\le\ell\le\liminf u_n$.

> **Propriété — Borne inférieure.** Si $u_n\ge\ell$ pour tout $n$, alors $\liminf u_n\ge\ell$.

**Étape 3 — Stratégie.** La minoration $\frac{x_n}n\ge\ell$ est gratuite. Pour la majoration, on découpe $n$ en blocs de longueur $q$ fixée : $\frac{x_n}n$ est au plus $\frac{x_q}q$ plus un reste qui tend vers $0$. On fait ensuite varier $q$.

**Étape 4 — Résolution détaillée.**

**4.1 Découpage.** Fixons $q\ge1$. Pour $n\ge q$, $n=aq+r$ avec $a\ge1$ et $0\le r<q$. Une récurrence sur $a$ donne $x_{aq}\le a\,x_q$, puis, si $r\ge1$, $x_n\le x_{aq}+x_r$. En notant $M_q=\max(0,x_1,\dots,x_{q-1})$ :
$$x_n\le a\,x_q+M_q .$$

**4.2 Passage à la limite (question 1 et 2).** On divise par $n$ : $\frac{x_n}n\le\frac{aq}n\cdot\frac{x_q}q+\frac{M_q}n$. Quand $n\to\infty$ ($q$ fixé), $\frac{aq}n\to1$ et $\frac{M_q}n\to0$. Donc
$$\limsup_{n\to\infty}\frac{x_n}n\le\frac{x_q}q\quad\text{pour tout }q\ge1,\qquad\text{d'où}\quad\limsup\frac{x_n}n\le\ell .$$
Comme $\frac{x_n}n\ge\ell$ pour tout $n$, $\liminf\frac{x_n}n\ge\ell$. Donc $\frac{x_n}n\to\ell$. Le signe de $x_n$ n'a pas servi : si $\ell=-\infty$, la majoration montre que $\frac{x_n}n\to-\infty$ ; si $x_n\ge0$, $\ell\ge0$ est fini.

**4.3 Application.** $x_n=\ln u_n$ est sous-additive, donc $\frac{\ln u_n}n\to\ell\in[-\infty,+\infty[$ et $u_n^{1/n}=e^{x_n/n}\to e^\ell$ (avec $e^{-\infty}=0$).

**Étape 5 — Vérification.**

> **Vérification — Exemples.**
> - $x_n=\sqrt n$ est sous-additive : $\frac{x_n}n\to0=\inf\frac{\sqrt n}n$.
> - Pour une matrice $A$ et une norme d'algèbre, $u_n=\|A^n\|$ vérifie $u_{n+m}\le u_nu_m$ : $\|A^n\|^{1/n}$ converge (vers le rayon spectral, résultat de Gelfand).

**Étape 6 — Conclusion.**
$$\boxed{\frac{x_n}n\xrightarrow[n\to\infty]{}\inf_{k\ge1}\frac{x_k}k}$$""",
r"""Avec $n=aq+r$ : $x_n\le ax_q+M_q$, d'où $\limsup\frac{x_n}n\le\frac{x_q}q$ pour tout $q$ ; avec $\frac{x_n}n\ge\ell$, la limite est $\ell=\inf\frac{x_n}n$.""")
src(X19, 'X')

# ---------------------------------------------------------------- 4. Idéaux maximaux
ex('n-s-x-ideaux', 'Maths', 'Anneaux', 3, 'Idéaux maximaux de C([0,1])', 25, r"""
On note $A=\mathcal C([0,1],\mathbb R)$, anneau commutatif pour les opérations usuelles. Pour $a\in[0,1]$, on pose $M_a=\{f\in A,\ f(a)=0\}$.

1. Montrer que $M_a$ est un idéal maximal de $A$ (un idéal $I\neq A$ tel que le seul idéal contenant strictement $I$ soit $A$).
2. Soit $I$ un idéal de $A$ distinct de $A$. Montrer qu'il existe $a\in[0,1]$ tel que $I\subset M_a$.
3. En déduire tous les idéaux maximaux de $A$.
""", r"""Pour la question 1, si $J\supsetneq M_a$ contient $f$ avec $f(a)\neq0$, écris $f(a)\cdot1=f-(f-f(a))$.""",
r"""Raisonne par l'absurde : pour chaque $a$, une fonction $f_a\in I$ ne s'annule pas sur un voisinage ouvert de $a$.""",
r"""Par compacité, un nombre fini de ces voisinages recouvre $[0,1]$ ; la fonction $\sum f_{a_i}^2\in I$ ne s'annule pas.""",
r"""**Étape 1 — Analyse de l'énoncé.** On cherche tous les idéaux maximaux de l'anneau des fonctions continues sur $[0,1]$. On montre qu'ils sont exactement les $M_a$, idéaux des fonctions nulles en un point.

**Étape 2 — Rappels du cours.**

> **Propriété — Idéal et unité.** Un idéal qui contient un inversible, en particulier $1$, est l'anneau entier.

> **Théorème — Borel-Lebesgue.** $[0,1]$ est compact : de tout recouvrement de $[0,1]$ par des ouverts, on peut extraire un sous-recouvrement fini.

> **Propriété — Inverse d'une fonction continue.** Si $g\in A$ ne s'annule pas, $\frac1g\in A$ : $g$ est inversible dans $A$.

**Étape 3 — Stratégie.** La question 1 est algébrique. La question 2 est le cœur : si aucun point n'annule tout $I$, on fabrique par compacité une fonction de $I$ qui ne s'annule jamais, donc inversible, et $I=A$.

**Étape 4 — Résolution détaillée.**

**4.1 $M_a$ est maximal.** $M_a$ est le noyau du morphisme d'anneaux $f\mapsto f(a)$, donc un idéal, et $M_a\neq A$ car $1\notin M_a$. Soit $J$ un idéal avec $M_a\subsetneq J$, et $f\in J\setminus M_a$, donc $f(a)\neq0$. La fonction $f-f(a)$ s'annule en $a$, donc appartient à $M_a\subset J$. Alors $f(a)\cdot1=f-(f-f(a))\in J$, puis $1=\frac1{f(a)}\cdot f(a)\in J$ : $J=A$.

**4.2 Tout idéal propre est dans un $M_a$.** Par l'absurde, supposons que pour tout $a\in[0,1]$ il existe $f_a\in I$ avec $f_a(a)\neq0$. Par continuité, $f_a$ ne s'annule pas sur un ouvert $V_a\ni a$ de $[0,1]$. Par compacité, $[0,1]=V_{a_1}\cup\dots\cup V_{a_n}$. On pose
$$g=f_{a_1}^2+\dots+f_{a_n}^2\in I\qquad(\text{car }f_{a_i}\cdot f_{a_i}\in I).$$
Tout $x$ est dans un $V_{a_i}$, donc $g(x)\ge f_{a_i}(x)^2>0$. Ainsi $g$ est inversible dans $A$ et $1=g\cdot\frac1g\in I$ : $I=A$, contradiction.

**4.3 Conclusion.** Si $I$ est maximal, $I\neq A$, donc $I\subset M_a$ pour un $a$ ; par maximalité de $I$ et comme $M_a\neq A$, $I=M_a$. Réciproquement, chaque $M_a$ est maximal.

**Étape 5 — Vérification.**

> **Vérification — Cas limites.**
> - Les $M_a$ sont deux à deux distincts : pour $a\neq b$, $x\mapsto x-a$ est dans $M_a$ mais pas dans $M_b$.
> - La compacité est essentielle : sur $]0,1]$, l'idéal des fonctions continues qui s'annulent au voisinage de $0$ n'est contenu dans aucun $M_a$.

**Étape 6 — Conclusion.**
$$\boxed{\text{Les idéaux maximaux de }\mathcal C([0,1],\mathbb R)\text{ sont les }M_a=\{f,\ f(a)=0\},\ a\in[0,1].}$$""",
r"""Maximaux : exactement les $M_a=\{f:f(a)=0\}$. Sinon, par compacité, $\sum f_{a_i}^2\in I$ ne s'annule pas et $I=A$.""")
src(X19, 'X')

# ---------------------------------------------------------------- 5. Famille commutative
ex('n-s-x-comm', 'Maths', 'Réduction', 3, 'Famille commutative : tous polynômes en un seul endomorphisme', 25, r"""
Soient $E$ un $\mathbb C$-espace vectoriel de dimension finie $n$ et $\mathcal F\subset\mathcal L(E)$ une famille (éventuellement infinie) d'endomorphismes diagonalisables qui commutent deux à deux.

1. Montrer qu'il existe une base de $E$ dans laquelle tous les éléments de $\mathcal F$ sont diagonaux.
2. Montrer qu'il existe $g\in\mathcal L(E)$ tel que tout $f\in\mathcal F$ soit un polynôme en $g$.
""", r"""Une famille finie de diagonalisables qui commutent est codiagonalisable ; ramène-toi à une base finie de $\mathrm{Vect}(\mathcal F)$.""",
r"""Dans la base commune, regroupe les vecteurs selon la liste de leurs valeurs propres $(\lambda_1(e_i),\dots,\lambda_r(e_i))$.""",
r"""Prends $g$ diagonal avec une valeur propre distincte par groupe, puis utilise l'interpolation de Lagrange.""",
r"""**Étape 1 — Analyse de l'énoncé.** La famille peut être infinie, mais elle vit dans $\mathcal L(E)$, de dimension finie. On veut un seul endomorphisme $g$ dont tous les $f$ soient des polynômes.

**Étape 2 — Rappels du cours.**

> **Théorème — Codiagonalisation.** Une famille finie d'endomorphismes diagonalisables qui commutent deux à deux est diagonalisable dans une base commune. (Les sous-espaces propres de l'un sont stables par les autres, et l'on raisonne par récurrence sur la dimension.)

> **Théorème — Interpolation de Lagrange.** Si $c_1,\dots,c_s$ sont distincts, pour toutes valeurs $\mu_1,\dots,\mu_s$ il existe $L\in\mathbb C[X]$ avec $L(c_t)=\mu_t$.

**Étape 3 — Stratégie.** On extrait une base $f_1,\dots,f_r$ de $\mathrm{Vect}(\mathcal F)$, formée d'éléments de $\mathcal F$, et on les codiagonalise : tout $f\in\mathcal F$, combinaison des $f_j$, est diagonal dans la même base. On construit $g$ diagonal dont les valeurs propres séparent les « profils » des vecteurs de base, puis on interpole.

**Étape 4 — Résolution détaillée.**

**4.1 Base commune.** $\mathrm{Vect}(\mathcal F)$ est de dimension finie ; on en extrait une base $f_1,\dots,f_r\in\mathcal F$. Ils commutent et sont diagonalisables : il existe une base $(e_1,\dots,e_n)$ avec $f_j(e_i)=\lambda_{j,i}e_i$. Tout $f\in\mathcal F$ s'écrit $f=\sum_j\alpha_jf_j$, donc $f(e_i)=\big(\sum_j\alpha_j\lambda_{j,i}\big)e_i$ : $f$ est diagonal dans cette base.

**4.2 Profils.** Au vecteur $e_i$ on associe son profil $\pi_i=(\lambda_{1,i},\dots,\lambda_{r,i})\in\mathbb C^r$. Soient $C_1,\dots,C_s$ les classes de vecteurs de même profil. Pour $f=\sum\alpha_jf_j$, la valeur propre de $f$ sur $e_i$ ne dépend que du profil : elle vaut un $\mu_t(f)$ constant sur $C_t$.

**4.3 Construction de $g$.** On choisit des complexes distincts $c_1,\dots,c_s$ et $g$ diagonal dans la base $(e_i)$ avec $g(e_i)=c_te_i$ si $e_i\in C_t$. Pour $f\in\mathcal F$, soit $L_f$ le polynôme de Lagrange avec $L_f(c_t)=\mu_t(f)$. Alors $L_f(g)(e_i)=L_f(c_t)e_i=\mu_t(f)e_i=f(e_i)$ pour $e_i\in C_t$ : $L_f(g)=f$.

**Étape 5 — Vérification.**

> **Vérification — Exemples.**
> - Si $\mathcal F=\{f\}$, on peut prendre $g=f$ : chaque profil est une valeur propre.
> - L'hypothèse de commutation est nécessaire : des polynômes en $g$ commutent toujours entre eux.

On peut choisir $c_t$ entiers, par exemple $c_t=t$.

**Étape 6 — Conclusion.**
$$\boxed{\exists\,g\in\mathcal L(E),\ \forall f\in\mathcal F,\ \exists L_f\in\mathbb C[X],\ f=L_f(g)}$$""",
r"""Codiagonaliser une base $f_1,\dots,f_r$ de $\mathrm{Vect}\,\mathcal F$, prendre $g$ diagonal séparant les profils de valeurs propres, puis $f=L_f(g)$ par interpolation de Lagrange.""")
src(X19, 'X')

# ---------------------------------------------------------------- 6. Unipotentes
ex('n-s-x-unip', 'Maths', 'Réduction', 3, 'Matrices unipotentes et racine carrée rationnelle', 25, r"""
Soit $A\in\mathcal M_n(\mathbb C)$.

1. Montrer l'équivalence : (i) toutes les valeurs propres de $A$ valent $1$ ; (ii) $A=I_n+N$ avec $N^n=0$.
2. On suppose de plus $A\in\mathcal M_n(\mathbb Q)$ et (i). Montrer qu'il existe $B\in\mathcal M_n(\mathbb Q)$ telle que $B^2=A$.
""", r"""(i)⇒(ii) : polynôme caractéristique de $N=A-I_n$ et théorème de Cayley-Hamilton.""",
r"""Pense au développement $(1+x)^{1/2}=\sum_k\binom{1/2}kx^k$ : ses coefficients sont rationnels.""",
r"""Tronque la série à l'ordre $n-1$ : le carré du polynôme obtenu vaut $1+X$ modulo $X^n$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Une matrice dont toutes les valeurs propres valent $1$ est dite unipotente. On veut la caractériser, puis extraire une racine carrée à coefficients rationnels, ce qui interdit d'utiliser une réduction sur $\mathbb C$.

**Étape 2 — Rappels du cours.**

> **Théorème — Cayley-Hamilton.** $\chi_N(N)=0$.

> **Propriété — Nilpotence et spectre.** $N$ est nilpotente si et seulement si sa seule valeur propre complexe est $0$, c'est-à-dire $\chi_N=X^n$.

> **Développement en série entière.** Pour $|x|<1$, $\sqrt{1+x}=\sum_{k\ge0}c_kx^k$ avec $c_k=\binom{1/2}k=\frac{\frac12(\frac12-1)\cdots(\frac12-k+1)}{k!}\in\mathbb Q$, et $\big(\sum c_kx^k\big)^2=1+x$.

**Étape 3 — Stratégie.** Question 1 : on traduit sur $N=A-I_n$. Question 2 : on remplace $x$ par $N$ dans la série de $\sqrt{1+x}$ ; comme $N^n=0$, la série devient un polynôme à coefficients rationnels.

**Étape 4 — Résolution détaillée.**

**4.1 (i)⇒(ii).** $\chi_A=(X-1)^n$ donc $\chi_N(X)=\chi_A(X+1)=X^n$, et $N^n=0$ par Cayley-Hamilton.

**4.2 (ii)⇒(i).** Si $Ax=\lambda x$ avec $x\neq0$, alors $Nx=(\lambda-1)x$, puis $0=N^nx=(\lambda-1)^nx$, donc $\lambda=1$.

**4.3 Identité polynomiale.** Soit $T=\sum_{k=0}^{n-1}c_kX^k\in\mathbb Q[X]$. Le coefficient de $X^m$ dans $T^2$, pour $m\le n-1$, ne fait intervenir que les $c_k$ avec $k\le m$ : c'est le même que dans le carré de la série, donc celui de $1+X$. Ainsi $T^2=1+X+X^nR$ avec $R\in\mathbb Q[X]$.

**4.4 Racine carrée.** $N=A-I_n\in\mathcal M_n(\mathbb Q)$ et $N^n=0$. On pose $B=T(N)\in\mathcal M_n(\mathbb Q)$. Alors $B^2=T^2(N)=I_n+N+N^nR(N)=I_n+N=A$.

**Étape 5 — Vérification.**

> **Vérification — Exemple.** $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ : $N^2=0$, $B=I_2+\frac12N=\begin{pmatrix}1&\frac12\\0&1\end{pmatrix}$ et $B^2=I_2+N+\frac14N^2=A$.

Sans l'hypothèse (i), il n'y a pas toujours de racine rationnelle : $A=2$ ($n=1$) n'est le carré d'aucun rationnel.

**Étape 6 — Conclusion.**
$$\boxed{A=I_n+N,\ N^n=0,\qquad B=\sum_{k=0}^{n-1}\binom{1/2}k N^k\in\mathcal M_n(\mathbb Q),\quad B^2=A}$$""",
r"""(i)⇔(ii) par Cayley-Hamilton ; $B=\sum_{k<n}\binom{1/2}kN^k$ est rationnelle et $B^2=A$ car $T^2\equiv1+X\pmod{X^n}$.""")
src(X19, 'X')

# ---------------------------------------------------------------- 7. Traces bornées
ex('n-s-x-traces', 'Maths', 'Réduction', 3, 'Traces des puissances bornées', 25, r"""
Soit $u$ un endomorphisme d'un $\mathbb C$-espace vectoriel $V$ de dimension $d\ge1$. On suppose qu'il existe $C\ge0$ tel que $|\mathrm{Tr}(u^n)|\le C$ pour tout $n\in\mathbb N$.

1. On note $\lambda_1,\dots,\lambda_d$ les valeurs propres de $u$ (avec multiplicité). Montrer que la série entière $S(t)=\sum_{n\ge0}\mathrm{Tr}(u^n)t^n$ a un rayon au moins $1$, et que $S(t)=\sum_k\frac1{1-\lambda_kt}$ pour $|t|$ petit.
2. En déduire que $|\lambda_k|\le1$ pour tout $k$, puis que $|\mathrm{Tr}(u^n)|\le d$ pour tout $n$.
""", r"""$\mathrm{Tr}(u^n)=\sum_k\lambda_k^n$ : écris $S(t)$ comme une somme de séries géométriques.""",
r"""Si une valeur propre $\mu$ de module maximal vérifie $|\mu|>1$, regarde $S$ sur le rayon $t=\frac s\mu$, $s\to1^-$.""",
r"""La somme d'une série entière est continue, donc bornée près de $\frac1\mu$, qui est dans le disque de convergence.""",
r"""**Étape 1 — Analyse de l'énoncé.** Les traces des puissances sont les sommes de Newton des valeurs propres. La seule hypothèse est qu'elles restent bornées ; on veut en déduire la borne universelle $d$.

**Étape 2 — Rappels du cours.**

> **Propriété — Trigonalisation.** Sur $\mathbb C$, $u$ est trigonalisable et $\mathrm{Tr}(u^n)=\sum_{k=1}^d\lambda_k^n$.

> **Propriété — Rayon de convergence.** Si $(a_n)$ est bornée, le rayon de $\sum a_nt^n$ est au moins $1$, et la somme est continue sur le disque ouvert de convergence.

**Étape 3 — Stratégie.** On identifie $S$ à une fraction rationnelle près de $0$. Une valeur propre de module $>1$ produirait un pôle à l'intérieur du disque unité, où $S$ est pourtant continue : contradiction.

**Étape 4 — Résolution détaillée.**

**4.1 Série génératrice.** $|\mathrm{Tr}(u^n)|\le C$ donne un rayon $R\ge1$. Pour $|t|<\frac1\rho$, où $\rho=\max|\lambda_k|$ (et pour tout $t$ si $\rho=0$) :
$$S(t)=\sum_n\sum_k\lambda_k^nt^n=\sum_k\frac1{1-\lambda_kt}=\sum_\mu\frac{m_\mu}{1-\mu t},$$
$\mu$ parcourant les valeurs propres distinctes et $m_\mu\ge1$ leurs multiplicités.

**4.2 Pas de valeur propre de module $>1$.** Supposons $\rho>1$ et soit $\mu_0$ avec $|\mu_0|=\rho$. Pour $s\in[0,1[$, $t_s=\frac s{\mu_0}$ vérifie $|t_s|<\frac1\rho$, donc
$$S(t_s)=\frac{m_{\mu_0}}{1-s}+\sum_{\mu\neq\mu_0}\frac{m_\mu}{1-\mu s/\mu_0}.$$
Quand $s\to1^-$, le premier terme tend vers $+\infty$ et les autres ont une limite finie ($1-\frac\mu{\mu_0}\neq0$). Donc $|S(t_s)|\to+\infty$. Mais $|t_s|\to\frac1\rho<1\le R$ : le point $\frac1{\mu_0}$ est dans le disque ouvert de convergence, où $S$ est continue, donc bornée au voisinage de $\frac1{\mu_0}$. Contradiction : $\rho\le1$.

**4.3 Borne.** $|\mathrm{Tr}(u^n)|=\big|\sum_k\lambda_k^n\big|\le\sum_k|\lambda_k|^n\le d$.

**Étape 5 — Vérification.**

> **Vérification — Exemples.**
> - Une rotation du plan : valeurs propres $e^{\pm i\theta}$, $\mathrm{Tr}(u^n)=2\cos(n\theta)$, bien majoré par $d=2$.
> - $u=\mathrm{diag}(2)$ : $\mathrm{Tr}(u^n)=2^n$ n'est pas bornée, ce qui est cohérent.
> - La borne $d$ est atteinte pour $u=\mathrm{Id}$.

**Étape 6 — Conclusion.**
$$\boxed{\sup_n|\mathrm{Tr}(u^n)|<\infty\ \Longrightarrow\ \forall k,\ |\lambda_k|\le1\ \Longrightarrow\ \forall n,\ |\mathrm{Tr}(u^n)|\le\dim V}$$""",
r"""$S(t)=\sum_k\frac1{1-\lambda_kt}$ a un rayon $\ge1$ ; une valeur propre de module $>1$ donnerait un pôle dans le disque unité. Donc $|\lambda_k|\le1$ et $|\mathrm{Tr}\,u^n|\le d$.""")
src(X19, 'X')

# ---------------------------------------------------------------- 8. Hoeffding
ex('n-s-x-hoeff', 'Maths', 'Probabilités', 3, 'Inégalité de Hoeffding', 30, r"""
1. Soit $X$ une variable aléatoire réelle centrée, à valeurs dans $[a,b]$. Montrer que pour tout $t\in\mathbb R$ :
$$\mathbb E\big(e^{tX}\big)\le\exp\Big(\frac{t^2(b-a)^2}8\Big).$$
2. Soient $X_1,\dots,X_n$ indépendantes, $X_i$ à valeurs dans $[a_i,b_i]$, et $S_n=X_1+\dots+X_n$. Montrer que pour tout $s>0$ :
$$\mathbb P\big(S_n-\mathbb E(S_n)\ge s\big)\le\exp\Big(-\frac{2s^2}{\sum_i(b_i-a_i)^2}\Big).$$
""", r"""Par convexité de $x\mapsto e^{tx}$ sur $[a,b]$ : $e^{tx}\le\frac{b-x}{b-a}e^{ta}+\frac{x-a}{b-a}e^{tb}$.""",
r"""Avec $p=\frac{-a}{b-a}$ et $u=t(b-a)$, le majorant s'écrit $e^{\varphi(u)}$ avec $\varphi(u)=-pu+\ln(1-p+pe^u)$ ; montre $\varphi''\le\frac14$.""",
r"""Question 2 : Markov appliquée à $e^{\lambda(S_n-\mathbb E S_n)}$, indépendance, puis choix optimal de $\lambda>0$.""",
r"""**Étape 1 — Analyse de l'énoncé.** On veut une majoration de la transformée de Laplace d'une variable bornée centrée (lemme de Hoeffding), puis une inégalité de concentration exponentielle pour une somme indépendante.

**Étape 2 — Rappels du cours.**

> **Propriété — Convexité.** Une fonction convexe est sous ses cordes : pour $x\in[a,b]$, $f(x)\le\frac{b-x}{b-a}f(a)+\frac{x-a}{b-a}f(b)$.

> **Théorème — Inégalité de Markov.** Si $Y\ge0$ et $c>0$, $\mathbb P(Y\ge c)\le\frac{\mathbb E(Y)}c$.

> **Propriété — Indépendance.** Si $X_1,\dots,X_n$ sont indépendantes, $\mathbb E\big(\prod g_i(X_i)\big)=\prod\mathbb E\big(g_i(X_i)\big)$.

> **Théorème — Taylor-Lagrange.** $\varphi(u)=\varphi(0)+u\varphi'(0)+\frac{u^2}2\varphi''(c)$ pour un $c$ entre $0$ et $u$.

**Étape 3 — Stratégie.** Question 1 : on majore $e^{tX}$ par sa corde, on prend l'espérance, puis on étudie le logarithme du majorant comme une fonction de $u=t(b-a)$. Question 2 : méthode de Chernoff.

**Étape 4 — Résolution détaillée.**

**4.1 Corde.** Si $a=b$, $X=0$ et l'inégalité est claire. Sinon, comme $\mathbb E X=0$ et $a\le X\le b$, on a $a\le0\le b$. En prenant l'espérance de l'inégalité de convexité :
$$\mathbb E(e^{tX})\le\frac{b\,e^{ta}-a\,e^{tb}}{b-a}=e^{ta}\big(1-p+pe^{u}\big),\qquad p=\frac{-a}{b-a}\in[0,1],\ u=t(b-a).$$
Comme $ta=-pu$, ce majorant vaut $e^{\varphi(u)}$ avec $\varphi(u)=-pu+\ln(1-p+pe^u)$.

**4.2 Étude de $\varphi$.** $\varphi(0)=0$ ; $\varphi'(u)=-p+\frac{pe^u}{1-p+pe^u}$, donc $\varphi'(0)=0$ ; en posant $q=\frac{pe^u}{1-p+pe^u}\in[0,1]$, $\varphi''(u)=q(1-q)\le\frac14$. Par Taylor-Lagrange, $\varphi(u)\le\frac{u^2}8=\frac{t^2(b-a)^2}8$.

**4.3 Chernoff.** Soit $\lambda>0$ et $Y_i=X_i-\mathbb E X_i$, centrée et à valeurs dans un intervalle de longueur $b_i-a_i$. Par Markov, puis indépendance et 4.2 :
$$\mathbb P(S_n-\mathbb ES_n\ge s)\le e^{-\lambda s}\,\mathbb E\big(e^{\lambda\sum Y_i}\big)=e^{-\lambda s}\prod_i\mathbb E(e^{\lambda Y_i})\le\exp\Big(-\lambda s+\frac{\lambda^2}8\sum_i(b_i-a_i)^2\Big).$$

**4.4 Optimisation.** Le trinôme en $\lambda$ est minimal pour $\lambda=\frac{4s}{\sum(b_i-a_i)^2}$, où il vaut $-\frac{2s^2}{\sum(b_i-a_i)^2}$.

**Étape 5 — Vérification.**

> **Vérification — Ordre de grandeur.** Pour $100$ lancers d'une pièce équilibrée ($X_i\in\{0,1\}$), $\mathbb P(S_{100}\ge60)\le e^{-2\cdot100/100}=e^{-2}\approx0{,}135$. La valeur exacte est environ $0{,}028$ : la borne est correcte, sans être fine.

Par symétrie (appliquée à $-X_i$), $\mathbb P(|S_n-\mathbb ES_n|\ge s)\le2\exp\big(-\frac{2s^2}{\sum(b_i-a_i)^2}\big)$.

**Étape 6 — Conclusion.**
$$\boxed{\mathbb E(e^{tX})\le e^{t^2(b-a)^2/8},\qquad\mathbb P\big(S_n-\mathbb ES_n\ge s\big)\le e^{-2s^2/\sum_i(b_i-a_i)^2}}$$""",
r"""Corde de $e^{tx}$ puis $\varphi''\le\frac14$ : $\mathbb E(e^{tX})\le e^{t^2(b-a)^2/8}$ ; Markov + indépendance + $\lambda=\frac{4s}{\sum(b_i-a_i)^2}$.""")
src(X19, 'X')

# ---------------------------------------------------------------- 9. Dérangements
ex('n-s-x-derang', 'Maths', 'Probabilités', 3, 'Dérangements : nombre et somme des signatures', 25, r"""
Un dérangement de $[\![1,n]\!]$ ($n\ge1$) est une permutation sans point fixe. On note $D(n)$ leur nombre.

1. Montrer que $D(n)=n!\sum_{k=0}^n\frac{(-1)^k}{k!}$, puis que $D(n)$ est l'entier le plus proche de $\frac{n!}e$.
2. On note $S(n)=\sum_{\sigma}\varepsilon(\sigma)$, la somme portant sur les dérangements. Calculer $S(n)$.
3. Combien de permutations de $[\![1,n]\!]$ ont exactement $m$ points fixes ? Quelle est la limite de la proportion correspondante quand $n\to\infty$ ?
""", r"""Formule du crible avec $A_i=\{\sigma,\ \sigma(i)=i\}$ : $|A_{i_1}\cap\dots\cap A_{i_k}|=(n-k)!$.""",
r"""Développe le déterminant de $J_n-I_n$ ($J_n$ : matrice remplie de $1$) par la formule de Leibniz.""",
r"""Choisis les $m$ points fixes, puis un dérangement des $n-m$ autres.""",
r"""**Étape 1 — Analyse de l'énoncé.** On compte les permutations sans point fixe, on estime ce nombre, puis on calcule la somme de leurs signatures et on dénombre les permutations à $m$ points fixes.

**Étape 2 — Rappels du cours.**

> **Théorème — Formule du crible.** $\big|\bigcup_iA_i\big|=\sum_{k\ge1}(-1)^{k+1}\sum_{i_1<\dots<i_k}|A_{i_1}\cap\dots\cap A_{i_k}|$.

> **Théorème — Formule de Leibniz.** $\det M=\sum_{\sigma\in\mathfrak S_n}\varepsilon(\sigma)\prod_{j=1}^nm_{\sigma(j),j}$.

> **Propriété — Séries alternées.** Si $(u_k)$ décroît vers $0$, le reste $\sum_{k>n}(-1)^ku_k$ est de valeur absolue $<u_{n+1}$.

**Étape 3 — Stratégie.** Crible pour $D(n)$ ; reste d'une série alternée pour l'approximation de $\frac{n!}e$. Pour $S(n)$, on reconnaît un déterminant : seuls les dérangements contribuent si la diagonale est nulle.

**Étape 4 — Résolution détaillée.**

**4.1 Crible.** Les permutations ayant au moins un point fixe forment $\bigcup A_i$, et une intersection de $k$ ensembles $A_i$ compte $(n-k)!$ permutations. Donc
$$D(n)=n!-\sum_{k=1}^n(-1)^{k+1}\binom nk(n-k)!=n!\sum_{k=0}^n\frac{(-1)^k}{k!}.$$

**4.2 Entier le plus proche.** $\frac{n!}e=n!\sum_{k\ge0}\frac{(-1)^k}{k!}$, donc $\big|\frac{n!}e-D(n)\big|=n!\,\big|\sum_{k>n}\frac{(-1)^k}{k!}\big|<\frac{n!}{(n+1)!}=\frac1{n+1}\le\frac12$. $D(n)$ est l'entier le plus proche de $\frac{n!}e$.

**4.3 Somme des signatures.** Soit $M=J_n-I_n$ (zéros sur la diagonale, $1$ ailleurs). Dans la formule de Leibniz, $\prod_jm_{\sigma(j),j}$ vaut $1$ si $\sigma$ est un dérangement, $0$ sinon. Donc $S(n)=\det(J_n-I_n)$. Or $J_n$ est de rang $1$ et de trace $n$ : ses valeurs propres sont $n$ (simple) et $0$ (d'ordre $n-1$), et $J_n$ est diagonalisable (symétrique réelle). Celles de $J_n-I_n$ sont $n-1$ et $-1$ (d'ordre $n-1$) :
$$S(n)=(-1)^{n-1}(n-1).$$

**4.4 Points fixes.** Choisir les $m$ points fixes ($\binom nm$ façons), puis un dérangement des $n-m$ autres : $\binom nmD(n-m)$ permutations (avec $D(0)=1$). La proportion vaut $\frac{D(n-m)}{m!\,(n-m)!}\to\frac{1}{m!\,e}$.

**Étape 5 — Vérification.**

> **Vérification — Petites valeurs.**
> - $n=2$ : un seul dérangement, la transposition, de signature $-1$ : $S(2)=-1=(-1)^1\cdot1$.
> - $n=3$ : deux $3$-cycles, de signature $+1$ : $S(3)=2$ ; $D(3)=2$ et $\frac{6}e\approx2{,}21$.
> - $n=4$ : $D(4)=9$ et $\frac{24}e\approx8{,}83$.

Les proportions limites $\frac1{m!\,e}$ forment la loi de Poisson de paramètre $1$.

**Étape 6 — Conclusion.**
$$\boxed{D(n)=\Big\lfloor\frac{n!}e\Big\rceil,\qquad S(n)=(-1)^{n-1}(n-1),\qquad\#\{\text{exactement }m\text{ points fixes}\}=\binom nmD(n-m)}$$""",
r"""$D(n)=n!\sum_{k\le n}\frac{(-1)^k}{k!}$, à moins de $\frac1{n+1}$ de $\frac{n!}e$ ; $S(n)=\det(J_n-I_n)=(-1)^{n-1}(n-1)$ ; $\binom nmD(n-m)$ permutations à $m$ points fixes.""")
src(X19, 'X')

# ---------------------------------------------------------------- 10. n | Σ k^n
ex('n-s-x-sompuis', 'Maths', 'Arithmétique', 3, 'Quand n divise-t-il 1ⁿ + 2ⁿ + … + (n−1)ⁿ ?', 20, r"""
1. Soit $p$ un nombre premier. Montrer que $p$ divise $1^{p-1}+2^{p-1}+\dots+(p-1)^{p-1}+1$.
2. Déterminer tous les entiers $n\ge1$ tels que $n$ divise $1^n+2^n+\dots+(n-1)^n$.
""", r"""Question 1 : petit théorème de Fermat.""",
r"""Si $n$ est impair, regroupe les termes $k^n$ et $(n-k)^n$.""",
r"""Si $n=2^am$ avec $a\ge1$ et $m$ impair, calcule la somme modulo $2^a$ : pour $k$ impair, $k^{2^{a-1}}\equiv1\pmod{2^a}$.""",
r"""**Étape 1 — Analyse de l'énoncé.** On étudie la divisibilité de sommes de puissances par l'exposant lui-même. Le cas premier est une application directe de Fermat ; le cas général sépare les $n$ impairs et les $n$ pairs.

**Étape 2 — Rappels du cours.**

> **Théorème — Petit théorème de Fermat.** Si $p$ est premier et $p\nmid k$, alors $k^{p-1}\equiv1\pmod p$.

> **Théorème — Euler.** Si $k\wedge N=1$, $k^{\varphi(N)}\equiv1\pmod N$ ; pour $N=2^a$, $\varphi(2^a)=2^{a-1}$.

**Étape 3 — Stratégie.** Pour $n$ impair, $k\mapsto n-k$ apparie les termes deux à deux en sommes nulles modulo $n$. Pour $n$ pair, on regarde la somme modulo la plus grande puissance de $2$ qui divise $n$ : les termes pairs disparaissent, les impairs valent $1$, et leur nombre n'est pas divisible par $2^a$.

**Étape 4 — Résolution détaillée.**

**4.1 Cas premier.** Les $p-1$ termes $k^{p-1}$ ($1\le k\le p-1$) valent $1$ modulo $p$ : la somme vaut $(p-1)+1=p\equiv0\pmod p$.

**4.2 $n$ impair.** Pour $1\le k\le n-1$, $(n-k)^n\equiv(-k)^n=-k^n\pmod n$. Comme $n$ est impair, $k\neq n-k$ et les termes se regroupent par paires de somme nulle modulo $n$ : $n$ divise la somme. (Pour $n=1$, la somme est vide, égale à $0$.)

**4.3 $n$ pair.** Écrivons $n=2^am$ avec $a\ge1$ et $m$ impair, et raisonnons modulo $2^a$.
- Si $k=2j$ est pair, $k^n=2^nj^n$ et $n\ge2^a>a$, donc $k^n\equiv0\pmod{2^a}$.
- Si $k$ est impair, $k^{2^{a-1}}\equiv1\pmod{2^a}$ (Euler) et $2^{a-1}\mid n$, donc $k^n\equiv1\pmod{2^a}$.

Il y a $\frac n2=2^{a-1}m$ entiers impairs dans $[\![1,n-1]\!]$, donc la somme est congrue à $2^{a-1}m\pmod{2^a}$. Comme $m$ est impair, ce n'est pas $0$ : $2^a$, donc $n$, ne divise pas la somme.

**Étape 5 — Vérification.**

> **Vérification — Petites valeurs.**
> - $n=3$ : $1+8=9$, divisible par $3$.
> - $n=4$ : $1+16+81=98$, non divisible par $4$ ($98\equiv2$, et la formule donne $2^{a-1}m=2$).
> - $n=5$ : $1+32+243+1024=1300=5\times260$.

**Étape 6 — Conclusion.**
$$\boxed{n\mid1^n+2^n+\dots+(n-1)^n\iff n\text{ est impair}}$$""",
r"""Fermat pour $p$ premier ; $n$ impair : appariement $k\leftrightarrow n-k$ ; $n=2^am$ pair : somme $\equiv2^{a-1}m\not\equiv0\pmod{2^a}$. Réponse : les $n$ impairs.""")
src(X19, 'X')
