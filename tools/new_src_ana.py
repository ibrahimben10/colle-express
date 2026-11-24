# Exercices d'après des sujets de concours (analyse, probabilités) : énoncés reformulés, indices et corrigés originaux.
from newlib import ex, E

def src(texte, concours):
    E[-1]['enonce'] += '\n\n*' + texte + '*'
    E[-1]['concours'] = concours

# ---------------------------------------------------------------- 1. Σ 2xⁿ/(n²−1)
ex('n-s-n-se1', 'Maths', 'Séries entières', 1, 'Somme de Σ 2xⁿ/(n² − 1)', 20, r"""
On considère la série entière $\displaystyle\sum_{n\ge2}\frac{2}{n^2-1}\,x^n$, de somme $S$.

1. Déterminer son rayon de convergence $R$.
2. Calculer $S(x)$ pour $x\in\,]-R,R[$.
3. Montrer que $S$ admet une limite en $1^-$ et la calculer. Comparer avec $\sum_{n\ge2}\frac2{n^2-1}$.
""", r"""Décompose $\frac2{n^2-1}=\frac1{n-1}-\frac1{n+1}$.""",
r"""Utilise $-\ln(1-x)=\sum_{m\ge1}\frac{x^m}m$ et réindexe chaque morceau.""",
r"""En $1^-$, $(1-x)\ln(1-x)\to0$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Le coefficient est une fraction rationnelle en $n$ ; on la décompose en éléments simples pour ramener la somme à des séries logarithmiques.

**Étape 2 — Rappels du cours.**

> **Théorème — Règle de d'Alembert.** Si $\big|\frac{a_{n+1}}{a_n}\big|\to\ell$, le rayon vaut $\frac1\ell$.

> **Développement usuel.** Pour $|x|<1$, $-\ln(1-x)=\sum_{m\ge1}\frac{x^m}m$.

**Étape 3 — Stratégie.** Avec $\frac2{n^2-1}=\frac1{n-1}-\frac1{n+1}$, la série se scinde en deux séries de rayon $1$, que l'on exprime avec $\ln(1-x)$ après réindexation.

**Étape 4 — Résolution détaillée.**

**4.1 Rayon.** $\frac{a_{n+1}}{a_n}=\frac{n^2-1}{(n+1)^2-1}\to1$ : $R=1$.

**4.2 Somme.** Pour $0<|x|<1$ :
$$\sum_{n\ge2}\frac{x^n}{n-1}=x\sum_{m\ge1}\frac{x^m}m=-x\ln(1-x),\qquad\sum_{n\ge2}\frac{x^n}{n+1}=\frac1x\sum_{m\ge3}\frac{x^m}m=\frac1x\Big(-\ln(1-x)-x-\frac{x^2}2\Big).$$
Par différence :
$$S(x)=\Big(\frac1x-x\Big)\ln(1-x)+1+\frac x2\quad(0<|x|<1),\qquad S(0)=0.$$

**4.3 Limite en $1^-$.** $\big(\frac1x-x\big)\ln(1-x)=\frac{(1+x)}x(1-x)\ln(1-x)\to0$, donc $S(x)\to1+\frac12=\frac32$. La série numérique est télescopique : $\sum_{n=2}^N\big(\frac1{n-1}-\frac1{n+1}\big)=1+\frac12-\frac1N-\frac1{N+1}\to\frac32$. Les deux valeurs coïncident, comme le prévoit le théorème d'Abel radial.

**Étape 5 — Vérification.**

> **Vérification — Numérique.** En $x=\frac12$ : la formule donne $\frac32\ln\frac12+\frac54\approx0{,}2103$, et la somme partielle $\frac23\cdot\frac14+\frac14\cdot\frac18+\frac2{15}\cdot\frac1{16}+\dots$ vaut aussi $\approx0{,}2103$.

> **Vérification — Développement en $0$.** $\big(\frac1x-x\big)\big(-x-\frac{x^2}2-\frac{x^3}3\big)+1+\frac x2=\frac23x^2+O(x^3)$, et le premier coefficient est bien $\frac2{2^2-1}=\frac23$.

**Étape 6 — Conclusion.**
$$\boxed{R=1,\qquad S(x)=\Big(\frac1x-x\Big)\ln(1-x)+1+\frac x2\ (x\neq0),\qquad\lim_{x\to1^-}S(x)=\frac32}$$""",
r"""$R=1$ ; $S(x)=(\frac1x-x)\ln(1-x)+1+\frac x2$ pour $x\neq0$ ; $S(x)\to\frac32=\sum\frac2{n^2-1}$ en $1^-$.""")
src("D'après un oral CCINP.", 'CCINP')

# ---------------------------------------------------------------- 2. arcsin x / √(1−x²)
ex('n-s-n-arcsin', 'Maths', 'Séries entières', 2, 'Développement de arcsin x / √(1 − x²)', 25, r"""
1. Développer $f:t\mapsto\frac1{\sqrt{1-t}}$ en série entière ; préciser le rayon et écrire les coefficients à l'aide de $\binom{2n}n$.
2. Soit $g(x)=\dfrac{\arcsin x}{\sqrt{1-x^2}}$ sur $]-1,1[$.
   (a) Justifier que $g$ est développable en série entière sur $]-1,1[$.
   (b) Montrer que $(1-x^2)g'(x)-xg(x)=1$.
   (c) En déduire le développement de $g$.
""", r"""$(1-t)^{-1/2}=\sum_n\binom{-1/2}n(-t)^n$ ; simplifie le produit $\frac12\cdot\frac32\cdots\frac{2n-1}2$.""",
r"""$g$ est le produit de $\arcsin$ et de $x\mapsto f(x^2)$, deux fonctions développables sur $]-1,1[$.""",
r"""Avec $g=\sum c_kx^k$ impaire, l'équation donne $(m+1)c_{m+1}=m\,c_{m-1}$.""",
r"""**Étape 1 — Analyse de l'énoncé.** On développe d'abord une puissance usuelle, puis une fonction produit dont on obtient les coefficients plus simplement par une équation différentielle que par un produit de Cauchy.

**Étape 2 — Rappels du cours.**

> **Développement usuel.** Pour $|t|<1$ et $\alpha\in\mathbb R$, $(1+t)^\alpha=\sum_n\binom\alpha nt^n$.

> **Propriété — Produit.** Le produit de deux fonctions développables en série entière sur $]-r,r[$ l'est sur $]-r,r[$.

> **Propriété — Unicité.** Si une série entière de rayon $>0$ est nulle sur un voisinage de $0$, tous ses coefficients sont nuls.

**Étape 3 — Stratégie.** Question 1 : formule du binôme généralisé. Question 2 : la fonction $g$ vérifie une équation différentielle linéaire du premier ordre ; on y injecte la série et on identifie les coefficients.

**Étape 4 — Résolution détaillée.**

**4.1 Développement de $f$.** Pour $|t|<1$,
$$\frac1{\sqrt{1-t}}=\sum_{n\ge0}\frac{\frac12\cdot\frac32\cdots\frac{2n-1}2}{n!}t^n=\sum_{n\ge0}\frac{(2n)!}{4^n(n!)^2}t^n=\sum_{n\ge0}\binom{2n}n\frac{t^n}{4^n},$$
car $1\cdot3\cdots(2n-1)=\frac{(2n)!}{2^nn!}$. Le rayon vaut $1$ (d'Alembert : le quotient tend vers $1$). Ainsi $\alpha_n=\frac1{4^n}$.

**4.2 $g$ est développable.** $\arcsin$ est développable sur $]-1,1[$ (primitive de $f(x^2)$) et $x\mapsto f(x^2)$ aussi ; leur produit $g$ l'est donc sur $]-1,1[$.

**4.3 Équation différentielle.** $g'(x)=\frac1{1-x^2}+\frac{x\arcsin x}{(1-x^2)^{3/2}}=\frac{1+x\,g(x)}{1-x^2}$, d'où $(1-x^2)g'-xg=1$.

**4.4 Coefficients.** $g$ est impaire. Avec $g=\sum c_kx^k$ :
$$\sum_kkc_kx^{k-1}-\sum_kkc_kx^{k+1}-\sum_kc_kx^{k+1}=1 .$$
Le terme constant donne $c_1=1$. Pour $m\ge1$, le coefficient de $x^m$ donne $(m+1)c_{m+1}-(m-1)c_{m-1}-c_{m-1}=0$, soit $c_{m+1}=\frac m{m+1}c_{m-1}$. D'où
$$c_{2n+1}=\prod_{j=1}^n\frac{2j}{2j+1}=\frac{4^n(n!)^2}{(2n+1)!},\qquad g(x)=\sum_{n\ge0}\frac{4^n(n!)^2}{(2n+1)!}x^{2n+1}.$$

**Étape 5 — Vérification.**

> **Vérification — Premiers termes.** $\arcsin x=x+\frac{x^3}6+\dots$ et $\frac1{\sqrt{1-x^2}}=1+\frac{x^2}2+\dots$ donnent $g=x+\big(\frac16+\frac12\big)x^3+\dots=x+\frac23x^3+\dots$ ; la formule donne $c_3=\frac{4}{6}=\frac23$.

Le rayon de la série de $g$ vaut $1$ : $\frac{c_{2n+3}}{c_{2n+1}}=\frac{2n+2}{2n+3}\to1$.

**Étape 6 — Conclusion.**
$$\boxed{\frac1{\sqrt{1-t}}=\sum_{n\ge0}\binom{2n}n\frac{t^n}{4^n},\qquad\frac{\arcsin x}{\sqrt{1-x^2}}=\sum_{n\ge0}\frac{4^n(n!)^2}{(2n+1)!}x^{2n+1}\quad(|x|<1)}$$""",
r"""$\frac1{\sqrt{1-t}}=\sum\binom{2n}n\frac{t^n}{4^n}$ ($R=1$) ; $(1-x^2)g'-xg=1$ donne $c_{2n+1}=\frac{4^n(n!)^2}{(2n+1)!}$.""")
src("D'après un oral Mines-Ponts.", 'Mines-Ponts')

# ---------------------------------------------------------------- 3. Σ n! xⁿ / n^{n+1}
ex('n-s-n-nfact', 'Maths', 'Séries entières', 2, 'La série Σ n! xⁿ / nⁿ⁺¹ et sa représentation intégrale', 30, r"""
Soit $f(x)=\displaystyle\sum_{n\ge1}\frac{n!}{n^{n+1}}x^n$.

1. Déterminer le rayon de convergence $R$, et montrer que $\displaystyle\int_0^{+\infty}t^ne^{-nt}\,dt=\frac{n!}{n^{n+1}}$.
2. Étudier la convergence de la série en $x=R$ et en $x=-R$.
3. Montrer que pour $|x|<R$ : $\displaystyle f(x)=\int_0^{+\infty}\frac{xt}{e^t-xt}\,dt$.
""", r"""Rapport $\frac{a_{n+1}}{a_n}=\big(1+\frac1n\big)^{-(n+1)}$ ; pour l'intégrale, pose $u=nt$.""",
r"""En $x=R$, utilise la formule de Stirling ; en $x=-R$, montre que $\big(1+\frac1n\big)^{n+1}$ décroît vers $e$.""",
r"""Écris $\frac{n!}{n^{n+1}}x^n=\int_0^\infty(xte^{-t})^n\,dt$ et intervertis série et intégrale ; $\max te^{-t}=\frac1e$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Les coefficients rappellent la formule de Stirling. On calcule le rayon, on étudie le bord, puis on obtient une expression intégrale de la somme.

**Étape 2 — Rappels du cours.**

> **Fonction Gamma.** $\int_0^\infty u^ne^{-u}\,du=n!$.

> **Formule de Stirling.** $n!\sim\sqrt{2\pi n}\,\big(\frac ne\big)^n$.

> **Théorème — Intégration terme à terme.** Si $u_n$ est intégrable sur $I$ et $\sum_n\int_I|u_n|<\infty$, alors $\sum u_n$ est intégrable et $\int\sum u_n=\sum\int u_n$.

> **Théorème — Séries alternées.** Si $(v_n)$ décroît vers $0$, $\sum(-1)^nv_n$ converge.

**Étape 3 — Stratégie.** D'Alembert pour $R$ ; Stirling en $x=e$ ; critère des séries alternées en $x=-e$ ; enfin intégration terme à terme de la série géométrique $\sum(xte^{-t})^n$.

**Étape 4 — Résolution détaillée.**

**4.1 Rayon et intégrale.** $\frac{a_{n+1}}{a_n}=\frac{(n+1)!\,n^{n+1}}{(n+1)^{n+2}n!}=\big(\frac n{n+1}\big)^{n+1}\to\frac1e$ : $R=e$. Avec $u=nt$ : $\int_0^\infty t^ne^{-nt}dt=\frac1{n^{n+1}}\int_0^\infty u^ne^{-u}du=\frac{n!}{n^{n+1}}$.

**4.2 En $x=e$.** Par Stirling, $\frac{n!\,e^n}{n^{n+1}}\sim\frac{\sqrt{2\pi n}}n=\sqrt{\frac{2\pi}n}$, terme d'une série divergente (Riemann, exposant $\frac12$).

**4.3 En $x=-e$.** Soit $v_n=\frac{n!\,e^n}{n^{n+1}}\to0$. Alors $\frac{v_{n+1}}{v_n}=e\big(1+\frac1n\big)^{-(n+1)}<1$, car $(n+1)\ln\big(1+\frac1n\big)>1$, qui découle de $\ln(1+u)>\frac u{1+u}$ pour $u>0$. La suite $(v_n)$ décroît vers $0$ : la série alternée converge.

**4.4 Représentation intégrale.** Pour $|x|<e$ et $t\ge0$, $|xte^{-t}|\le\frac{|x|}e<1$. Avec $u_n(t)=(xte^{-t})^n$, $\sum_n\int_0^\infty|u_n|=\sum_n\frac{n!\,|x|^n}{n^{n+1}}<\infty$ car $|x|<R$. On peut donc intervertir :
$$f(x)=\int_0^\infty\sum_{n\ge1}(xte^{-t})^n\,dt=\int_0^\infty\frac{xte^{-t}}{1-xte^{-t}}\,dt=\int_0^\infty\frac{xt}{e^t-xt}\,dt.$$

**Étape 5 — Vérification.**

> **Vérification — Numérique.** En $x=1$ : la série vaut $1+\frac2{8}+\frac6{81}+\frac{24}{1024}+\dots\approx1{,}359$, et l'intégrale $\int_0^\infty\frac t{e^t-t}dt$ donne aussi $\approx1{,}359$.

La condition $|x|<e$ est exactement celle qui empêche le dénominateur $e^t-xt$ de s'annuler : $e^t>|x|t$ pour tout $t\ge0$ si et seulement si $|x|<e$.

**Étape 6 — Conclusion.**
$$\boxed{R=e;\quad\text{divergente en }e,\ \text{convergente en }-e;\quad f(x)=\int_0^{+\infty}\frac{xt}{e^t-xt}\,dt\ \ (|x|<e)}$$""",
r"""$R=e$ ; divergence en $e$ (terme $\sim\sqrt{2\pi/n}$), convergence en $-e$ (série alternée) ; $f(x)=\int_0^\infty\frac{xt}{e^t-xt}dt$ par intégration terme à terme.""")
src("D'après un oral Centrale.", 'Centrale')

# ---------------------------------------------------------------- 4. Σ∫ ≠ ∫Σ
ex('n-s-n-interv', 'Maths', 'Intégration', 1, 'Une interversion série-intégrale interdite', 20, r"""
Sur $I=\,]0,+\infty[$, on pose $f_n(x)=e^{-nx}-2e^{-2nx}$ pour $n\ge1$.

1. Montrer que $f_n$ est intégrable sur $I$ et calculer $\int_If_n$. Que vaut $\sum_{n\ge1}\int_If_n$ ?
2. Montrer que $\sum f_n$ converge simplement sur $I$, calculer sa somme $S$, et montrer que $S$ est intégrable. Calculer $\int_IS$.
3. Expliquer pourquoi le théorème d'intégration terme à terme ne s'applique pas.
""", r"""Les deux sommes $\sum e^{-nx}$ et $\sum e^{-2nx}$ sont géométriques.""",
r"""Tu dois trouver $S(x)=\frac1{e^x+1}$.""",
r"""Calcule $\int_I|f_n|=\frac cn$ avec $c=\int_0^\infty|e^{-u}-2e^{-2u}|\,du$.""",
r"""**Étape 1 — Analyse de l'énoncé.** On construit un exemple où l'intégrale de la somme diffère de la somme des intégrales. Il faut identifier l'hypothèse du théorème qui est en défaut.

**Étape 2 — Rappels du cours.**

> **Théorème — Intégration terme à terme.** Si les $f_n$ sont intégrables sur $I$, si $\sum f_n$ converge simplement vers $S$ continue par morceaux et si $\sum_n\int_I|f_n|<\infty$, alors $S$ est intégrable et $\int_IS=\sum_n\int_If_n$.

> **Série géométrique.** Pour $|q|<1$, $\sum_{n\ge1}q^n=\frac q{1-q}$.

**Étape 3 — Stratégie.** Calcul direct des deux membres, puis calcul de $\int|f_n|$ par le changement de variable $u=nx$.

**Étape 4 — Résolution détaillée.**

**4.1 Intégrales.** $f_n$ est continue et $|f_n|\le3e^{-nx}$, intégrable. $\int_If_n=\frac1n-\frac2{2n}=0$, donc $\sum_n\int_If_n=0$.

**4.2 Somme.** Pour $x>0$, $e^{-x}<1$ :
$$S(x)=\frac{e^{-x}}{1-e^{-x}}-\frac{2e^{-2x}}{1-e^{-2x}}=\frac1{e^x-1}-\frac2{e^{2x}-1}=\frac{e^x+1-2}{e^{2x}-1}=\frac1{e^x+1}.$$
$S$ est continue, positive, majorée par $e^{-x}$ : intégrable, et
$$\int_IS=\int_0^\infty\frac{e^{-x}}{1+e^{-x}}dx=\Big[-\ln(1+e^{-x})\Big]_0^{+\infty}=\ln2 .$$

**4.3 Hypothèse en défaut.** Avec $u=nx$, $\int_I|f_n|=\frac1n\int_0^\infty|e^{-u}-2e^{-2u}|du=\frac cn$. Le signe change en $u=\ln2$ :
$$c=\int_0^{\ln2}(2e^{-2u}-e^{-u})du+\int_{\ln2}^\infty(e^{-u}-2e^{-2u})du=\frac14+\frac14=\frac12 .$$
Donc $\sum\int|f_n|=\sum\frac1{2n}=+\infty$ : l'hypothèse de sommabilité des intégrales des valeurs absolues n'est pas satisfaite.

**Étape 5 — Vérification.**

> **Vérification — Cohérence.** $\ln2\neq0$ : sans l'hypothèse $\sum\int|f_n|<\infty$, l'interversion peut effectivement échouer. On peut aussi vérifier $S(x)\to\frac12$ en $0^+$ : la somme est bornée, mais la convergence n'est pas dominée par une fonction intégrable de la forme $\sum|f_n|$.

**Étape 6 — Conclusion.**
$$\boxed{\sum_n\int_0^\infty f_n=0\neq\ln2=\int_0^\infty\sum_nf_n,\quad\text{car }\sum_n\int_0^\infty|f_n|=\sum_n\frac1{2n}=+\infty}$$""",
r"""$\int f_n=0$ mais $S=\frac1{e^x+1}$ et $\int S=\ln2$ ; $\int|f_n|=\frac1{2n}$, série divergente : le théorème d'intégration terme à terme ne s'applique pas.""")
src("D'après un oral CCINP.", 'CCINP')

# ---------------------------------------------------------------- 5. Loi conjointe (i+j)/2^{i+j+3}
ex('n-s-n-conj', 'Maths', 'Probabilités', 1, 'Une loi conjointe en (i + j)/2^(i+j+3)', 20, r"""
1. Montrer que la famille $\Big(\dfrac{i+j}{2^{i+j}}\Big)_{(i,j)\in\mathbb N^2}$ est sommable et calculer sa somme.
2. Soient $X$, $Y$ deux variables aléatoires à valeurs dans $\mathbb N$ telles que $\mathbb P(X=i,Y=j)=\dfrac{i+j}{2^{i+j+3}}$ pour tous $i,j\in\mathbb N$.
   (a) Vérifier que l'on définit bien ainsi une loi conjointe.
   (b) Déterminer la loi de $X$ et celle de $Y$.
   (c) $X$ et $Y$ sont-elles indépendantes ?
   (d) Calculer $\mathbb E(X)$.
""", r"""Famille positive : somme par paquets, en sommant d'abord en $j$.""",
r"""$\sum_{i\ge0}\frac1{2^i}=2$, $\sum_{i\ge0}\frac i{2^i}=2$ et $\sum_{i\ge0}\frac{i^2}{2^i}=6$.""",
r"""Regarde $\mathbb P(X=0,Y=0)$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Famille double positive, puis loi conjointe : on vérifie la somme $1$, on calcule les marginales, on teste l'indépendance et on calcule une espérance.

**Étape 2 — Rappels du cours.**

> **Théorème — Sommation par paquets.** Pour une famille de réels positifs, on peut sommer dans n'importe quel ordre ; la famille est sommable si et seulement si la somme obtenue est finie.

> **Séries dérivées.** Pour $|x|<1$ : $\sum x^i=\frac1{1-x}$, $\sum ix^i=\frac x{(1-x)^2}$, $\sum i^2x^i=\frac{x(1+x)}{(1-x)^3}$. En $x=\frac12$ : $2$, $2$ et $6$.

> **Propriété — Indépendance.** $X$ et $Y$ sont indépendantes si et seulement si $\mathbb P(X=i,Y=j)=\mathbb P(X=i)\mathbb P(Y=j)$ pour tous $i,j$.

**Étape 3 — Stratégie.** On sépare $\frac{i+j}{2^{i+j}}=\frac i{2^i}\cdot\frac1{2^j}+\frac1{2^i}\cdot\frac j{2^j}$, puis on somme par paquets.

**Étape 4 — Résolution détaillée.**

**4.1 Somme.** $\sum_{i,j}\frac{i+j}{2^{i+j}}=\sum_i\frac i{2^i}\sum_j\frac1{2^j}+\sum_i\frac1{2^i}\sum_j\frac j{2^j}=2\cdot2+2\cdot2=8$.

**4.2 Loi conjointe.** Les nombres $\frac{i+j}{2^{i+j+3}}$ sont positifs, de somme $\frac88=1$ : c'est une loi de probabilité sur $\mathbb N^2$.

**4.3 Marginales.** $\mathbb P(X=i)=\sum_j\frac{i+j}{2^{i+j+3}}=\frac1{2^{i+3}}(2i+2)=\frac{i+1}{2^{i+2}}$. Par symétrie de la loi, $Y$ a la même loi. Vérification : $\sum_i\frac{i+1}{2^{i+2}}=\frac14(2+2)=1$.

**4.4 Indépendance.** $\mathbb P(X=0,Y=0)=0$ mais $\mathbb P(X=0)\mathbb P(Y=0)=\frac14\cdot\frac14\neq0$ : $X$ et $Y$ ne sont pas indépendantes.

**4.5 Espérance.** $\mathbb E(X)=\sum_i\frac{i(i+1)}{2^{i+2}}=\frac14(6+2)=2$.

**Étape 5 — Vérification.**

> **Vérification — Numérique.** Les premières probabilités de $X$ sont $\frac14,\frac14,\frac3{16},\frac18,\dots$, de somme partielle croissante vers $1$ ; leur moyenne pondérée tend vers $2$.

Le défaut d'indépendance se voit aussi sur la loi conjointe : elle ne s'écrit pas comme un produit $a_ib_j$, à cause de la somme $i+j$.

**Étape 6 — Conclusion.**
$$\boxed{\sum\frac{i+j}{2^{i+j}}=8,\quad\mathbb P(X=i)=\mathbb P(Y=i)=\frac{i+1}{2^{i+2}},\quad X,Y\text{ non indépendantes},\quad\mathbb E(X)=2}$$""",
r"""Somme $8$ donc loi conjointe ; $\mathbb P(X=i)=\frac{i+1}{2^{i+2}}$ (même loi pour $Y$) ; non indépendantes car $\mathbb P(0,0)=0$ ; $\mathbb E(X)=2$.""")
src("D'après un oral CCINP.", 'CCINP')

# ---------------------------------------------------------------- 6. Binomiale → Poisson
ex('n-s-n-poisson', 'Maths', 'Probabilités', 1, 'De la loi binomiale à la loi de Poisson', 15, r"""
Soit $\lambda\in\,]0,1[$ et, pour $n\ge2$, $X_n$ une variable aléatoire de loi binomiale $\mathcal B\big(n,\frac\lambda n\big)$.

1. Pour $k\in\mathbb N$ fixé, montrer que $\dfrac{n(n-1)\cdots(n-k+1)}{n^k}\xrightarrow[n\to\infty]{}1$.
2. Déterminer $\lim_{n\to\infty}\mathbb P(X_n=k)$ pour tout $k\in\mathbb N$.
3. Application : une machine produit des pièces défectueuses avec probabilité $0{,}01$. Estimer la probabilité qu'un lot de $100$ pièces n'en contienne aucune défectueuse, et comparer à la valeur exacte.
""", r"""C'est un produit de $k$ facteurs $1-\frac jn$, avec $k$ fixé.""",
r"""Écris $\mathbb P(X_n=k)=\frac{n(n-1)\cdots(n-k+1)}{n^k}\cdot\frac{\lambda^k}{k!}\cdot\big(1-\frac\lambda n\big)^{n-k}$.""",
r"""$\big(1-\frac\lambda n\big)^n=\exp\big(n\ln(1-\frac\lambda n)\big)\to e^{-\lambda}$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Le nombre d'épreuves tend vers l'infini et la probabilité de succès vers $0$, avec une moyenne $n\cdot\frac\lambda n=\lambda$ fixe. On montre que la loi tend vers une loi de Poisson.

**Étape 2 — Rappels du cours.**

> **Loi binomiale.** $\mathbb P(X=k)=\binom nkp^k(1-p)^{n-k}$ pour $0\le k\le n$.

> **Loi de Poisson.** $\mathbb P(Y=k)=e^{-\lambda}\frac{\lambda^k}{k!}$.

> **Équivalent usuel.** $\ln(1+u)\sim u$ quand $u\to0$.

**Étape 3 — Stratégie.** On sépare $\mathbb P(X_n=k)$ en trois facteurs, dont on calcule les limites séparément, $k$ étant fixé.

**Étape 4 — Résolution détaillée.**

**4.1 Premier facteur.** $\frac{n(n-1)\cdots(n-k+1)}{n^k}=\prod_{j=0}^{k-1}\big(1-\frac jn\big)\to1$, produit d'un nombre fixé de facteurs tendant vers $1$.

**4.2 Limite.** Pour $n\ge k$ :
$$\mathbb P(X_n=k)=\frac{n(n-1)\cdots(n-k+1)}{n^k}\cdot\frac{\lambda^k}{k!}\cdot\Big(1-\frac\lambda n\Big)^{n}\cdot\Big(1-\frac\lambda n\Big)^{-k}.$$
$\big(1-\frac\lambda n\big)^n=\exp\big(n\ln(1-\frac\lambda n)\big)\to e^{-\lambda}$ et $\big(1-\frac\lambda n\big)^{-k}\to1$. Donc $\mathbb P(X_n=k)\to e^{-\lambda}\frac{\lambda^k}{k!}$.

**4.3 Application.** $n=100$, $p=0{,}01$, donc $\lambda=1$ (la limite vaut pour tout $\lambda>0$ ; la restriction $\lambda<1$ assure seulement $\frac\lambda n\le1$ dès $n\ge2$). Estimation : $e^{-1}\approx0{,}368$. Valeur exacte : $0{,}99^{100}\approx0{,}366$.

**Étape 5 — Vérification.**

> **Vérification — Somme.** $\sum_ke^{-\lambda}\frac{\lambda^k}{k!}=1$ : la limite est bien une loi de probabilité.

L'écart relatif de l'application est d'environ $0{,}5\ \%$ : l'approximation est excellente pour $n$ grand et $p$ petit.

**Étape 6 — Conclusion.**
$$\boxed{\mathbb P(X_n=k)\xrightarrow[n\to\infty]{}e^{-\lambda}\frac{\lambda^k}{k!}}$$""",
r"""Produit de trois facteurs : $\prod(1-\frac jn)\to1$, $(1-\frac\lambda n)^n\to e^{-\lambda}$ : $\mathbb P(X_n=k)\to e^{-\lambda}\frac{\lambda^k}{k!}$ ; application : $e^{-1}\approx0{,}368$ contre $0{,}99^{100}\approx0{,}366$.""")
src("D'après un oral CCINP.", 'CCINP')

# ---------------------------------------------------------------- 7. xy'' − y' − 4x³y = 0
ex('n-s-n-ed1', 'Maths', 'Équations différentielles', 2, 'Équation xy″ − y′ − 4x³y = 0 sur ℝ', 25, r"""
On considère l'équation différentielle $(E)$ : $xy''-y'-4x^3y=0$.

1. Déterminer les solutions de $(E)$ développables en série entière au voisinage de $0$.
2. Résoudre $(E)$ sur $]0,+\infty[$ et sur $]-\infty,0[$.
3. Résoudre $(E)$ sur $\mathbb R$.
""", r"""Avec $y=\sum a_nx^n$, obtiens la relation $k(k-2)a_k=4a_{k-4}$.""",
r"""Les coefficients d'indices $4p$ et $4p+2$ donnent $\mathrm{ch}(x^2)$ et $\mathrm{sh}(x^2)$.""",
r"""Sur $\mathbb R$, recolle deux solutions en $0$ en imposant que $y$ soit deux fois dérivable : regarde $\frac{y'(x)}x$.""",
r"""**Étape 1 — Analyse de l'énoncé.** L'équation est linéaire d'ordre $2$, mais le coefficient de $y''$ s'annule en $0$ : le théorème de Cauchy-Lipschitz ne s'applique que sur $]0,+\infty[$ et $]-\infty,0[$. On cherche des solutions en série entière, puis on recolle.

**Étape 2 — Rappels du cours.**

> **Théorème — Structure des solutions.** Sur un intervalle où $a$, $b$ sont continues, l'ensemble des solutions de $y''+a(x)y'+b(x)y=0$ est un plan vectoriel.

> **Développements usuels.** $\mathrm{ch}\,u=\sum\frac{u^{2p}}{(2p)!}$ et $\mathrm{sh}\,u=\sum\frac{u^{2p+1}}{(2p+1)!}$, de rayon infini.

**Étape 3 — Stratégie.** Identification des coefficients pour la question 1 ; les deux solutions trouvées forment une base sur chaque demi-droite ; sur $\mathbb R$, on étudie la dérivabilité seconde en $0$ d'une fonction recollée.

**Étape 4 — Résolution détaillée.**

**4.1 Séries entières.** Avec $y=\sum a_nx^n$ de rayon $r>0$ : $xy''-y'=\sum_nn(n-2)a_nx^{n-1}$ et $4x^3y=\sum_n4a_nx^{n+3}$. Le coefficient de $x^{k-1}$ donne
$$k(k-2)a_k=4a_{k-4}\qquad(k\ge0,\ a_j=0\text{ si }j<0).$$
$k=1$ : $a_1=0$ ; $k=3$ : $a_3=\frac43a_{-1}=0$ ; donc les $a_{\text{impair}}$ sont nuls. $a_0$ et $a_2$ sont libres ($k=0$ et $k=2$ donnent $0=0$). Pour $k=4p$ : $a_{4p}=\frac{a_{4p-4}}{2p(2p-1)}$, d'où $a_{4p}=\frac{a_0}{(2p)!}$. Pour $k=4p+2$ : $a_{4p+2}=\frac{a_{4p-2}}{(2p+1)(2p)}$, d'où $a_{4p+2}=\frac{a_2}{(2p+1)!}$. Ainsi
$$y=a_0\,\mathrm{ch}(x^2)+a_2\,\mathrm{sh}(x^2),$$
de rayon infini ; réciproquement ces fonctions sont solutions.

**4.2 Sur une demi-droite.** Sur $]0,+\infty[$, $(E)\iff y''-\frac1xy'-4x^2y=0$, linéaire à coefficients continus : les solutions forment un plan. $\mathrm{ch}(x^2)$ et $\mathrm{sh}(x^2)$ sont solutions et indépendantes : $y=A\,\mathrm{ch}(x^2)+B\,\mathrm{sh}(x^2)$. De même sur $]-\infty,0[$.

**4.3 Recollement.** Une solution sur $\mathbb R$ s'écrit $A_1\mathrm{ch}(x^2)+B_1\mathrm{sh}(x^2)$ pour $x>0$ et $A_2\mathrm{ch}(x^2)+B_2\mathrm{sh}(x^2)$ pour $x<0$. La continuité en $0$ donne $A_1=A_2$. Pour $x\neq0$, $y'(x)=2x\big(A\,\mathrm{sh}(x^2)+B_i\mathrm{ch}(x^2)\big)$, donc $y'(0)=0$ et $\frac{y'(x)-y'(0)}x\to2B_1$ en $0^+$, $2B_2$ en $0^-$. La dérivabilité de $y'$ en $0$ impose $B_1=B_2$. Réciproquement, $A\,\mathrm{ch}(x^2)+B\,\mathrm{sh}(x^2)$ est solution sur $\mathbb R$.

**Étape 5 — Vérification.**

> **Vérification — Calcul direct.** $y=\mathrm{ch}(x^2)$ : $y'=2x\,\mathrm{sh}(x^2)$, $y''=2\,\mathrm{sh}(x^2)+4x^2\mathrm{ch}(x^2)$. Alors $xy''-y'-4x^3y=2x\,\mathrm{sh}+4x^3\mathrm{ch}-2x\,\mathrm{sh}-4x^3\mathrm{ch}=0$.

L'espace des solutions sur $\mathbb R$ est encore un plan : le point singulier $0$ n'apporte ici aucune liberté supplémentaire.

**Étape 6 — Conclusion.**
$$\boxed{\mathcal S_{\mathbb R}=\{A\,\mathrm{ch}(x^2)+B\,\mathrm{sh}(x^2),\ (A,B)\in\mathbb R^2\}}$$""",
r"""Série entière : $k(k-2)a_k=4a_{k-4}$, d'où $y=A\,\mathrm{ch}(x^2)+B\,\mathrm{sh}(x^2)$ ; même plan sur chaque demi-droite ; sur $\mathbb R$, le recollement impose $A_1=A_2$, $B_1=B_2$.""")
src("D'après un oral Mines-Ponts.", 'Mines-Ponts')

# ---------------------------------------------------------------- 8. y'' − y = 1/sh x, th x
ex('n-s-n-ed2', 'Maths', 'Équations différentielles', 2, 'Variation des constantes : y″ − y = 1/sh x et th x', 25, r"""
1. Résoudre sur $]0,+\infty[$ l'équation $y''-y=\dfrac1{\mathrm{sh}\,x}$.
2. Résoudre sur $\mathbb R$ l'équation $y''-y=\mathrm{th}\,x$.
""", r"""Cherche $y=\lambda(x)\,\mathrm{sh}\,x+\mu(x)\,\mathrm{ch}\,x$ avec $\lambda'\mathrm{sh}\,x+\mu'\mathrm{ch}\,x=0$.""",
r"""Tu obtiens $\lambda'=f(x)\mathrm{ch}\,x$ et $\mu'=-f(x)\mathrm{sh}\,x$, où $f$ est le second membre.""",
r"""Pour la question 2, $\int\frac{\mathrm{sh}^2t}{\mathrm{ch}\,t}dt=\mathrm{sh}\,t-\int\frac{dt}{\mathrm{ch}\,t}$ et $\int\frac{dt}{\mathrm{ch}\,t}=2\arctan(e^t)$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Équations linéaires d'ordre $2$ à coefficients constants, avec des seconds membres non usuels : on utilise la variation des constantes.

**Étape 2 — Rappels du cours.**

> **Théorème — Équation homogène.** Les solutions de $y''-y=0$ sont $\lambda\,\mathrm{sh}\,x+\mu\,\mathrm{ch}\,x$.

> **Méthode — Variation des constantes.** Une solution particulière de $y''-y=f$ est $\lambda\,\mathrm{sh}+\mu\,\mathrm{ch}$ avec $\lambda'\mathrm{sh}+\mu'\mathrm{ch}=0$ et $\lambda'\mathrm{ch}+\mu'\mathrm{sh}=f$. Comme $\mathrm{ch}^2-\mathrm{sh}^2=1$, cela donne $\lambda'=f\,\mathrm{ch}$ et $\mu'=-f\,\mathrm{sh}$.

**Étape 3 — Stratégie.** On calcule les deux primitives, puis on ajoute la solution générale de l'équation homogène.

**Étape 4 — Résolution détaillée.**

**4.1 Second membre $\frac1{\mathrm{sh}\,x}$.** $\lambda'=\frac{\mathrm{ch}\,x}{\mathrm{sh}\,x}$, donc $\lambda=\ln(\mathrm{sh}\,x)$ sur $]0,+\infty[$ ; $\mu'=-1$, donc $\mu=-x$. Solution particulière : $y_p=\mathrm{sh}\,x\ln(\mathrm{sh}\,x)-x\,\mathrm{ch}\,x$, et
$$y=\lambda\,\mathrm{sh}\,x+\mu\,\mathrm{ch}\,x+\mathrm{sh}\,x\ln(\mathrm{sh}\,x)-x\,\mathrm{ch}\,x .$$

**4.2 Second membre $\mathrm{th}\,x$.** $\lambda'=\mathrm{th}\,x\,\mathrm{ch}\,x=\mathrm{sh}\,x$, donc $\lambda=\mathrm{ch}\,x$ ; $\mu'=-\frac{\mathrm{sh}^2x}{\mathrm{ch}\,x}=-\mathrm{ch}\,x+\frac1{\mathrm{ch}\,x}$, donc $\mu=-\mathrm{sh}\,x+2\arctan(e^x)$ (car $\frac{d}{dx}2\arctan e^x=\frac{2e^x}{1+e^{2x}}=\frac1{\mathrm{ch}\,x}$). D'où $y_p=\mathrm{ch}\,x\,\mathrm{sh}\,x-\mathrm{ch}\,x\,\mathrm{sh}\,x+2\,\mathrm{ch}\,x\arctan(e^x)=2\,\mathrm{ch}\,x\arctan(e^x)$, et
$$y=\lambda\,\mathrm{sh}\,x+\mu\,\mathrm{ch}\,x+2\,\mathrm{ch}\,x\,\arctan(e^x)\qquad\text{sur }\mathbb R .$$

**Étape 5 — Vérification.**

> **Vérification — Question 1.** $y_p'=\mathrm{ch}\,x\ln(\mathrm{sh}\,x)-x\,\mathrm{sh}\,x$ et $y_p''=\mathrm{sh}\,x\ln(\mathrm{sh}\,x)+\frac{\mathrm{ch}^2x}{\mathrm{sh}\,x}-\mathrm{sh}\,x-x\,\mathrm{ch}\,x$, donc $y_p''-y_p=\frac{\mathrm{ch}^2x-\mathrm{sh}^2x}{\mathrm{sh}\,x}=\frac1{\mathrm{sh}\,x}$.

> **Vérification — Question 2.** $y_p'=2\,\mathrm{sh}\,x\arctan(e^x)+1$ et $y_p''=2\,\mathrm{ch}\,x\arctan(e^x)+\mathrm{th}\,x$ : $y_p''-y_p=\mathrm{th}\,x$.

**Étape 6 — Conclusion.**
$$\boxed{y=\lambda\,\mathrm{sh}x+\mu\,\mathrm{ch}x+\mathrm{sh}x\ln(\mathrm{sh}x)-x\,\mathrm{ch}x\ \ (x>0);\qquad y=\lambda\,\mathrm{sh}x+\mu\,\mathrm{ch}x+2\,\mathrm{ch}x\arctan(e^x)\ \ (x\in\mathbb R)}$$""",
r"""Variation des constantes : $y_p=\mathrm{sh}x\ln(\mathrm{sh}x)-x\,\mathrm{ch}x$ pour $\frac1{\mathrm{sh}x}$, et $y_p=2\,\mathrm{ch}x\arctan(e^x)$ pour $\mathrm{th}x$, plus $\lambda\,\mathrm{sh}x+\mu\,\mathrm{ch}x$.""")
src("D'après un oral de l'École polytechnique.", 'X')

# ---------------------------------------------------------------- 9. ∂f/∂x + ∂f/∂y = 0
ex('n-s-n-transp', 'Maths', 'Calcul différentiel', 1, 'Équation de transport ∂f/∂x + ∂f/∂y = 0', 15, r"""
1. Soit $f\in\mathcal C^1(\mathbb R^2,\mathbb R)$ telle que $\dfrac{\partial f}{\partial x}+\dfrac{\partial f}{\partial y}=0$. Montrer qu'il existe $\varphi\in\mathcal C^1(\mathbb R,\mathbb R)$ telle que $f(x,y)=\varphi(x-y)$ pour tout $(x,y)$.
2. Déterminer les $f\in\mathcal C^1(\mathbb R^2,\mathbb R)$ telles que $\dfrac{\partial f}{\partial x}+\dfrac{\partial f}{\partial y}=f$.
""", r"""Change de variables : $u=x+y$, $v=x-y$, et pose $g(u,v)=f\big(\frac{u+v}2,\frac{u-v}2\big)$.""",
r"""Calcule $\frac{\partial g}{\partial u}$ par la règle de la chaîne ; une fonction de dérivée nulle sur $\mathbb R$ est constante.""",
r"""Question 2 : pose $h(x,y)=e^{-x}f(x,y)$ et applique la question 1.""",
r"""**Étape 1 — Analyse de l'énoncé.** L'opérateur $\partial_x+\partial_y$ est la dérivée selon le vecteur $(1,1)$. Une fonction annulée par cet opérateur est constante sur chaque droite de direction $(1,1)$, c'est-à-dire fonction de $x-y$.

**Étape 2 — Rappels du cours.**

> **Théorème — Règle de la chaîne.** Si $f$ est $\mathcal C^1$ et $g(u,v)=f(a(u,v),b(u,v))$, alors $\partial_ug=\partial_xf\cdot\partial_ua+\partial_yf\cdot\partial_ub$.

> **Propriété — Dérivée nulle.** Une fonction d'une variable dérivable, de dérivée nulle sur un intervalle, est constante.

**Étape 3 — Stratégie.** Le changement de variables linéaire $(u,v)=(x+y,x-y)$ redresse la direction $(1,1)$ sur l'axe des $u$ : l'équation devient $\partial_ug=0$.

**Étape 4 — Résolution détaillée.**

**4.1 Changement de variables.** Posons $g(u,v)=f\big(\frac{u+v}2,\frac{u-v}2\big)$, de classe $\mathcal C^1$. Par la règle de la chaîne,
$$\frac{\partial g}{\partial u}(u,v)=\frac12\Big(\frac{\partial f}{\partial x}+\frac{\partial f}{\partial y}\Big)\Big(\frac{u+v}2,\frac{u-v}2\Big)=0 .$$

**4.2 Conclusion de la question 1.** Pour $v$ fixé, $u\mapsto g(u,v)$ a une dérivée nulle sur $\mathbb R$ : elle est constante. Donc $g(u,v)=g(0,v)=:\varphi(v)$, avec $\varphi(v)=f\big(\frac v2,-\frac v2\big)$ de classe $\mathcal C^1$. Comme $(x,y)=\big(\frac{u+v}2,\frac{u-v}2\big)$ pour $u=x+y$, $v=x-y$ : $f(x,y)=g(x+y,x-y)=\varphi(x-y)$. Réciproquement, $\partial_x\varphi(x-y)+\partial_y\varphi(x-y)=\varphi'-\varphi'=0$.

**4.3 Question 2.** Si $\partial_xf+\partial_yf=f$, la fonction $h=e^{-x}f$ vérifie $\partial_xh+\partial_yh=e^{-x}(\partial_xf-f+\partial_yf)=0$. Donc $h(x,y)=\varphi(x-y)$ et $f(x,y)=e^x\varphi(x-y)$ ; réciproquement ces fonctions conviennent.

**Étape 5 — Vérification.**

> **Vérification — Exemples.** $f(x,y)=\sin(x-y)$ vérifie $\partial_xf+\partial_yf=\cos(x-y)-\cos(x-y)=0$. Pour la question 2, $f=e^x(x-y)^2$ : $\partial_xf=e^x(x-y)^2+2e^x(x-y)$ et $\partial_yf=-2e^x(x-y)$, de somme $f$.

On pouvait aussi écrire $f=e^y\psi(x-y)$ : c'est la même famille, avec $\psi(w)=e^{w}\varphi(w)$.

**Étape 6 — Conclusion.**
$$\boxed{\partial_xf+\partial_yf=0\iff f(x,y)=\varphi(x-y);\qquad\partial_xf+\partial_yf=f\iff f(x,y)=e^x\varphi(x-y),\ \varphi\in\mathcal C^1}$$""",
r"""Avec $u=x+y$, $v=x-y$ : $\partial_ug=0$, donc $f(x,y)=\varphi(x-y)$ ; pour la question 2, $e^{-x}f$ est solution de la première : $f=e^x\varphi(x-y)$.""")
src("D'après un oral Mines-Ponts.", 'Mines-Ponts')

# ---------------------------------------------------------------- 10. y'' − 4y = f à support compact
ex('n-s-n-ed3', 'Maths', 'Équations différentielles', 3, 'y″ − 4y = f avec f à support compact', 30, r"""
Soit $f:\mathbb R\to\mathbb R$ de classe $\mathcal C^\infty$, nulle en dehors d'un segment $[-a,a]$. On considère $(E)$ : $y''-4y=f$.

1. Une solution de $(E)$ est-elle nécessairement nulle en dehors d'un segment ?
2. Montrer que $y$ est solution de $(E)$ sur $\mathbb R$ si et seulement s'il existe $(\lambda,\mu)\in\mathbb R^2$ tel que
$$y(x)=\lambda e^{2x}+\mu e^{-2x}-\frac{e^{2x}}4\int_x^{+\infty}f(t)e^{-2t}\,dt-\frac{e^{-2x}}4\int_{-\infty}^xf(t)e^{2t}\,dt .$$
3. En déduire qu'il existe une unique solution $y_0$ de $(E)$ qui tend vers $0$ en $+\infty$ et en $-\infty$.
4. Donner une condition nécessaire et suffisante sur $f$ pour que $(E)$ admette une solution nulle en dehors d'un segment.
""", r"""Ajoute à une solution une solution de l'équation homogène, par exemple $\mathrm{ch}(2x)$.""",
r"""Dérive deux fois la fonction proposée avec $\lambda=\mu=0$ : les termes en $f$ se compensent dans $y'$.""",
r"""Pour $x>a$, $\int_x^{+\infty}f(t)e^{-2t}dt=0$ et la solution particulière vaut $-\frac{e^{-2x}}4\int_{\mathbb R}f(t)e^{2t}dt$.""",
r"""**Étape 1 — Analyse de l'énoncé.** On résout une équation linéaire d'ordre $2$ à coefficients constants dont le second membre est à support compact, et l'on étudie le comportement des solutions à l'infini.

**Étape 2 — Rappels du cours.**

> **Théorème — Structure.** Les solutions de $y''-4y=f$ sont $y_p+\lambda e^{2x}+\mu e^{-2x}$, où $y_p$ est une solution particulière.

> **Théorème — Dérivation d'une intégrale.** Si $f$ est continue, $x\mapsto\int_c^xf(t)\,dt$ est dérivable de dérivée $f(x)$.

**Étape 3 — Stratégie.** On vérifie que la formule proposée, avec $\lambda=\mu=0$, est une solution particulière ; on lit ensuite son comportement hors de $[-a,a]$, où les intégrales sont constantes.

**Étape 4 — Résolution détaillée.**

**4.1 Question 1.** Non : si $y$ est solution, $y+\mathrm{ch}(2x)$ l'est aussi, et l'une des deux n'est pas nulle hors d'un segment (leur différence tend vers $+\infty$).

**4.2 Solution particulière.** Les intégrales convergent car $f$ est nulle hors de $[-a,a]$. Notons $A(x)=\int_x^{+\infty}fe^{-2t}$, $B(x)=\int_{-\infty}^xfe^{2t}$ et $y_p=-\frac14\big(e^{2x}A+e^{-2x}B\big)$. Avec $A'=-fe^{-2x}$ et $B'=fe^{2x}$ :
$$y_p'=-\tfrac14\big(2e^{2x}A-f-2e^{-2x}B+f\big)=-\tfrac12\big(e^{2x}A-e^{-2x}B\big),$$
$$y_p''=-\tfrac12\big(2e^{2x}A-f+2e^{-2x}B-f\big)=-\big(e^{2x}A+e^{-2x}B\big)+f=4y_p+f .$$
Donc $y_p$ est solution, et par le théorème de structure les solutions sont exactement $y_p+\lambda e^{2x}+\mu e^{-2x}$.

**4.3 Comportement à l'infini.** Soient $I_+=\int_{\mathbb R}fe^{2t}$ et $I_-=\int_{\mathbb R}fe^{-2t}$. Pour $x>a$ : $A(x)=0$ et $B(x)=I_+$, donc $y_p(x)=-\frac{I_+}4e^{-2x}\to0$. Pour $x<-a$ : $B(x)=0$ et $A(x)=I_-$, donc $y_p(x)=-\frac{I_-}4e^{2x}\to0$.

**4.4 Unicité.** $y=y_p+\lambda e^{2x}+\mu e^{-2x}$ tend vers $0$ en $+\infty$ si et seulement si $\lambda=0$, et en $-\infty$ si et seulement si $\mu=0$. Donc $y_0=y_p$ est l'unique solution qui tend vers $0$ aux deux bouts.

**4.5 Support compact.** Une solution nulle hors d'un segment tend vers $0$ aux deux bouts, donc c'est $y_p$ ; et $y_p$ est nulle pour $x>a$ si et seulement si $I_+=0$, pour $x<-a$ si et seulement si $I_-=0$. Condition : $\int_{\mathbb R}f(t)e^{2t}dt=\int_{\mathbb R}f(t)e^{-2t}dt=0$.

**Étape 5 — Vérification.**

> **Vérification — Exemple.** Si $f=\psi''-4\psi$ avec $\psi$ $\mathcal C^\infty$ à support compact, alors $y=\psi$ est solution à support compact, et par intégration par parties $\int(\psi''-4\psi)e^{\pm2t}dt=\int\psi\big((e^{\pm2t})''-4e^{\pm2t}\big)dt=0$ : la condition est bien vérifiée.

**Étape 6 — Conclusion.**
$$\boxed{y_0=-\frac14\Big(e^{2x}\!\int_x^{+\infty}\!fe^{-2t}+e^{-2x}\!\int_{-\infty}^x\!fe^{2t}\Big);\quad\text{support compact}\iff\int fe^{2t}=\int fe^{-2t}=0}$$""",
r"""Non (ajouter $\mathrm{ch}\,2x$) ; la formule donne une solution particulière, qui tend vers $0$ aux deux bouts et est l'unique telle ; support compact si et seulement si $\int fe^{2t}=\int fe^{-2t}=0$.""")
src("D'après un oral de l'École polytechnique.", 'X')
