D = {}

D['x-a-1'] = r"""
**Heuristique (non rigoureuse, pour deviner l'inverse).** Si les séries géométriques avaient un sens :
$$(1-ba)^{-1}=\sum_{k\ge0}(ba)^k=1+\sum_{k\ge1}b(ab)^{k-1}a=1+b\Big(\sum_{j\ge0}(ab)^j\Big)a=1+b(1-ab)^{-1}a.$$
On vérifie ce candidat par un calcul exact, valable dans tout anneau (non nécessairement commutatif).

**Notations.** $c=(1-ab)^{-1}$, de sorte que $(1-ab)c=1$ et $c(1-ab)=1$, et $d=1+bca$.

**Inverse à droite.** On développe en gardant l'ordre des facteurs :
$$(1-ba)d=(1-ba)(1+bca)=1+bca-ba-babca.$$
On regroupe les termes contenant $b\cdots a$ : $bca-babca=b\,(c-abc)\,a=b\,(1-ab)c\,a=b\cdot1\cdot a=ba$. Donc
$$(1-ba)d=1+ba-ba=1.$$

**Inverse à gauche.** De même :
$$d(1-ba)=1-ba+bca-bcaba,\qquad bca-bcaba=b\,(c-cab)\,a=b\,c(1-ab)\,a=ba.$$
Donc $d(1-ba)=1$.

**Conclusion.** $1-ba$ est inversible, d'inverse $1+b(1-ab)^{-1}a$. (Il faut vérifier les deux côtés : dans un anneau non commutatif, un inverse à droite n'est pas forcément un inverse à gauche.)

**Application.** Pour $A\in\mathcal M_{n,m}(\mathbb K)$, $B\in\mathcal M_{m,n}(\mathbb K)$ et $\lambda\neq0$ : $\lambda I_n-AB=\lambda\big(I_n-\frac A\lambda B\big)$ est inversible si et seulement si $\lambda I_m-BA$ l'est (le raisonnement s'adapte aux matrices rectangulaires). Donc $AB$ et $BA$ ont les mêmes valeurs propres non nulles.
"""

D['x-ar-1'] = r"""
**Factorisation.** On cherche deux facteurs : $(2n+1)(3n+1)=6n^2+2n+3n+1=6n^2+5n+1$. (On peut aussi la trouver par le discriminant $25-24=1$, racines $-\frac12$ et $-\frac13$.)

**Principe.** Pour que $p$ divise un produit, il suffit qu'il divise l'un des facteurs. On cherche donc $n\in\mathbb N$ tel que $p\mid2n+1$ ou $p\mid3n+1$.

**Cas $p=2$.** $2n+1$ est toujours impair ; mais $3n+1$ est pair pour $n$ impair. Avec $n=1$ : $6+5+1=12\equiv0\pmod2$.

**Cas $p$ impair.** $2\wedge p=1$, donc 2 est inversible modulo $p$ et l'équation $2n+1\equiv0\pmod p$ a des solutions. Explicitement, $n=\frac{p-1}2$ est un entier naturel (car $p$ est impair) et $2n+1=p\equiv0\pmod p$. Alors
$$6n^2+5n+1=(2n+1)(3n+1)=p\Big(\frac{3(p-1)}2+1\Big)\equiv0\pmod p.$$

**Conclusion.** Pour tout premier $p$, l'entier $n=1$ (si $p=2$) ou $n=\frac{p-1}2$ (si $p$ est impair) convient. Le point clé est de factoriser : chercher une racine d'un polynôme modulo $p$ est en général difficile, mais un facteur de degré 1 à coefficient dominant inversible a toujours une racine.
"""

D['x-ar-2'] = r"""
**Cadre.** $\mathbb F_p=\mathbb Z/p\mathbb Z$ est un corps (car $p$ est premier) et $\mathbb F_p^*$ est un groupe multiplicatif commutatif d'ordre $p-1$. Par Lagrange, $x^{p-1}=1$ pour tout $x\in\mathbb F_p^*$ (petit théorème de Fermat).

**Outil : nombre de racines.** Dans un corps, un polynôme non nul de degré $d$ a au plus $d$ racines.

**1 et 2. Élément d'ordre $q^\alpha$.** Soit $q$ premier avec $q^\alpha\mid p-1$ (la question 1 est le cas $\alpha=1$). Le polynôme $X^{(p-1)/q}-1$ est de degré $\frac{p-1}q<p-1$ ; il a donc au plus $\frac{p-1}q$ racines, et ne peut pas s'annuler sur les $p-1$ éléments de $\mathbb F_p^*$. Il existe donc $x\in\mathbb F_p^*$ avec $x^{(p-1)/q}\neq1$. Posons
$$y=x^{(p-1)/q^\alpha}\quad(\text{exposant entier car }q^\alpha\mid p-1).$$
Alors $y^{q^\alpha}=x^{p-1}=1$, donc l'ordre de $y$ divise $q^\alpha$ : il vaut $q^\beta$ avec $\beta\le\alpha$. Et $y^{q^{\alpha-1}}=x^{(p-1)/q}\neq1$, donc l'ordre ne divise pas $q^{\alpha-1}$ : $\beta=\alpha$. L'élément $y$ est d'ordre exactement $q^\alpha$.

**3. Lemme : produit d'éléments d'ordres premiers entre eux.** Soient $a,b$ dans un groupe commutatif, d'ordres $m$ et $n$ avec $m\wedge n=1$. Si $(ab)^k=1$, alors $a^k=b^{-k}\in\langle a\rangle\cap\langle b\rangle$ ; ce sous-groupe a un ordre qui divise $m$ et $n$, donc vaut 1. Ainsi $a^k=b^k=1$, $m\mid k$ et $n\mid k$, donc $mn\mid k$. Comme $(ab)^{mn}=1$, l'ordre de $ab$ est exactement $mn$.

**3. Conclusion.** Décomposons $p-1=q_1^{\alpha_1}\cdots q_r^{\alpha_r}$ en facteurs premiers distincts. Par la question 2, il existe $y_i$ d'ordre $q_i^{\alpha_i}$. Les ordres sont deux à deux premiers entre eux ; par récurrence avec le lemme, $y=y_1y_2\cdots y_r$ est d'ordre $\prod q_i^{\alpha_i}=p-1=|\mathbb F_p^*|$. Donc $\mathbb F_p^*=\langle y\rangle$ est **cyclique**.

**Exemple.** Dans $\mathbb F_7^*$, les puissances de 3 sont $3,2,6,4,5,1$ : 3 est un générateur.
"""

D['x-p-1'] = r"""
**1. Dérivée logarithmique.** Sur $\mathbb C$, $P=a\prod_{i=1}^r(X-z_i)^{m_i}$ avec $z_i$ distincts, $m_i\ge1$, $a\neq0$. En dérivant le produit (règle de Leibniz) puis en divisant par $P$ :
$$\frac{P'}P=\sum_{i=1}^r\frac{m_i}{X-z_i}.$$

**1. Une racine de $P'$ qui n'est pas racine de $P$.** Soit $w$ avec $P'(w)=0$. Si $P(w)=0$, $w$ est un des $z_i$ et il est dans l'enveloppe convexe. Sinon, on évalue en $w$ :
$$0=\sum_{i=1}^r\frac{m_i}{w-z_i}=\sum_{i=1}^r\frac{m_i\,\overline{(w-z_i)}}{|w-z_i|^2},$$
en multipliant numérateur et dénominateur par le conjugué. En prenant le conjugué de cette égalité :
$$\sum_{i=1}^r\lambda_i(w-z_i)=0,\qquad\lambda_i=\frac{m_i}{|w-z_i|^2}>0.$$

**1. Barycentre.** On isole $w$ : $\big(\sum\lambda_i\big)w=\sum\lambda_iz_i$, soit
$$w=\frac{\sum_i\lambda_iz_i}{\sum_i\lambda_i}.$$
$w$ est un barycentre à coefficients strictement positifs des racines de $P$ : il appartient à leur enveloppe convexe (**théorème de Gauss-Lucas**).

**2. Réduction.** Soit $c\in\mathbb C$ ; montrons que $c\in P(H_1)$. Posons $Q=P-c$ : $Q$ n'est pas constant et $Q'=P'$.

**2. Raisonnement par l'absurde.** Supposons que $Q$ n'a aucune racine dans $H_1$ : toutes ses racines sont dans $K=\mathbb C\setminus H_1$, demi-plan fermé, qui est convexe. L'enveloppe convexe des racines de $Q$ est alors contenue dans $K$, et par la question 1, toutes les racines de $Q'=P'$ sont dans $K$. Cela contredit l'hypothèse : $P'$ a une racine dans $H_1$.

**2. Conclusion.** $Q$ a une racine $z\in H_1$, c'est-à-dire $P(z)=c$. Ceci pour tout $c$ : $P(H_1)=\mathbb C$.
"""
