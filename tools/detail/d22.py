D = {}

D['x-se-2'] = r"""
**Notation.** $A_n=a_1+\dots+a_n>0$ et $S=\sum_{n\ge1}\frac1{a_n}<+\infty$. On montre que $K=2$ convient et qu'il est optimal.

**1. Cauchy-Schwarz avec des poids.** L'idée est d'écrire $k=\sqrt{a_k}\cdot\frac k{\sqrt{a_k}}$ pour faire apparaître $A_n$ et $\frac1{a_k}$. Par l'inégalité de Cauchy-Schwarz dans $\mathbb R^n$ :
$$\Big(\sum_{k=1}^nk\Big)^2=\Big(\sum_{k=1}^n\sqrt{a_k}\cdot\frac k{\sqrt{a_k}}\Big)^2\le\Big(\sum_{k=1}^na_k\Big)\Big(\sum_{k=1}^n\frac{k^2}{a_k}\Big)=A_n\sum_{k=1}^n\frac{k^2}{a_k}.$$
Comme $\sum_{k=1}^nk=\frac{n(n+1)}2$, on obtient $\frac1{A_n}\le\frac4{n^2(n+1)^2}\sum_{k=1}^n\frac{k^2}{a_k}$, puis
$$\frac n{A_n}\le\frac4{n(n+1)^2}\sum_{k=1}^n\frac{k^2}{a_k}.$$

**2. Interversion des sommes.** Tous les termes sont positifs : on peut sommer sur $n\ge1$ puis intervertir (Fubini pour les séries à termes positifs ; le couple $(n,k)$ parcourt $k\le n$) :
$$\sum_{n\ge1}\frac n{A_n}\le\sum_{n\ge1}\sum_{k=1}^n\frac{4}{n(n+1)^2}\cdot\frac{k^2}{a_k}=\sum_{k\ge1}\frac{k^2}{a_k}\sum_{n\ge k}\frac4{n(n+1)^2}.$$

**3. Majoration de la somme intérieure par télescopage.**
$$\frac1{n^2}-\frac1{(n+1)^2}=\frac{(n+1)^2-n^2}{n^2(n+1)^2}=\frac{2n+1}{n^2(n+1)^2}\ge\frac{2n}{n^2(n+1)^2}=\frac2{n(n+1)^2}.$$
Donc $\frac4{n(n+1)^2}\le2\Big(\frac1{n^2}-\frac1{(n+1)^2}\Big)$, et en sommant (somme télescopique, le terme général tend vers 0) :
$$\sum_{n\ge k}\frac4{n(n+1)^2}\le2\sum_{n\ge k}\Big(\frac1{n^2}-\frac1{(n+1)^2}\Big)=\frac2{k^2}.$$

**4. Conclusion de la majoration.** En reportant :
$$\sum_{n\ge1}\frac n{a_1+\dots+a_n}\le\sum_{k\ge1}\frac{k^2}{a_k}\cdot\frac2{k^2}=2\sum_{k\ge1}\frac1{a_k}.$$

**5. Optimalité : la suite test.** Soit $\varepsilon\in]0,1]$ et $a_n=n^{1+\varepsilon}$. Comparaison série-intégrale ($t\mapsto t^{-1-\varepsilon}$ décroissante) :
$$\frac1\varepsilon=\int_1^{+\infty}\frac{\mathrm dt}{t^{1+\varepsilon}}\le\sum_{n\ge1}\frac1{n^{1+\varepsilon}}=:Z_\varepsilon\le1+\frac1\varepsilon.$$
Par ailleurs $t\mapsto t^{1+\varepsilon}$ est croissante, donc $A_n=\sum_{k=1}^nk^{1+\varepsilon}\le\int_1^{n+1}t^{1+\varepsilon}\,\mathrm dt\le\frac{(n+1)^{2+\varepsilon}}{2+\varepsilon}$.

**6. Minoration du membre de gauche.** Avec $n=(n+1)-1$ :
$$\frac n{A_n}\ge(2+\varepsilon)\frac n{(n+1)^{2+\varepsilon}}=(2+\varepsilon)\Big(\frac1{(n+1)^{1+\varepsilon}}-\frac1{(n+1)^{2+\varepsilon}}\Big).$$
En sommant, avec $\sum_{m\ge2}m^{-1-\varepsilon}=Z_\varepsilon-1$ et $\sum_{m\ge2}m^{-2-\varepsilon}\le\zeta(2)$ :
$$\sum_{n\ge1}\frac n{A_n}\ge(2+\varepsilon)\big(Z_\varepsilon-1-\zeta(2)\big).$$

**7. Passage à la limite.** Si $K$ convient, alors pour tout $\varepsilon$ : $K\ge(2+\varepsilon)\Big(1-\frac{1+\zeta(2)}{Z_\varepsilon}\Big)$. Quand $\varepsilon\to0^+$, $Z_\varepsilon\ge\frac1\varepsilon\to+\infty$, donc le membre de droite tend vers 2 : $K\ge2$.

**Conclusion.** La meilleure constante est $K=2$.
"""

D['x-f-1'] = r"""
**1. Mise en place.** Soit $I=[a,b]$ et $g=f-\mathrm{id}$, continue sur $I$. Un point fixe de $f$ est un zéro de $g$ ; d'après le théorème des valeurs intermédiaires (TVI), il suffit de trouver deux points où $g$ prend des valeurs de signes opposés (au sens large).

**1. Cas $f(I)\subset I$.** $f(a)\in[a,b]$ donc $g(a)=f(a)-a\ge0$ ; $f(b)\in[a,b]$ donc $g(b)=f(b)-b\le0$. Par le TVI sur $[a,b]$, $g$ s'annule.

**1. Cas $I\subset f(I)$.** $a,b\in f(I)$ : il existe $u,v\in I$ avec $f(u)=a$ et $f(v)=b$. Comme $u,v\in[a,b]$ : $g(u)=a-u\le0$ et $g(v)=b-v\ge0$. Le TVI entre $u$ et $v$ donne un zéro de $g$, donc un point fixe de $f$.

**2. L'ensemble $A$.** Soit $A=\{x\in[0,1]:f(x)\ge x\}$. $f(0)\in[0,1]$ donc $f(0)\ge0$ : $0\in A$. $A$ est non vide et majoré par 1 : il admet une borne supérieure $s\in[0,1]$.

**2. $s\le f(s)$.** Soit $x\in A$. Comme $x\le s$ et $f$ est croissante : $x\le f(x)\le f(s)$. Donc $f(s)$ majore $A$, et $s$ étant le plus petit majorant : $s\le f(s)$.

**2. $f(s)\le s$.** Appliquons $f$ (croissante) à $s\le f(s)$ : $f(s)\le f(f(s))$. Ainsi $y=f(s)\in[0,1]$ vérifie $y\le f(y)$, donc $f(s)\in A$, et $f(s)\le\sup A=s$.

**2. Conclusion.** $f(s)=s$. Aucune continuité n'a servi : seules la croissance et la borne supérieure interviennent (théorème de Knaster-Tarski).

**3. Raisonnement par l'absurde.** Supposons $f(x)\neq g(x)$ pour tout $x\in[0,1]$. La fonction $f-g$ est continue et ne s'annule pas : par le TVI, elle est de signe constant. Supposons $f>g$ (l'autre cas est symétrique).

**3. L'ensemble des points fixes de $g$.** Soit $F=\{x\in[0,1]:g(x)=x\}$. D'après la question 1 (avec $g([0,1])\subset[0,1]$), $F\neq\emptyset$. $F$ est l'image réciproque de $\{0\}$ par la fonction continue $g-\mathrm{id}$ : il est fermé, et borné, donc il admet un maximum $m$.

**3. $F$ est stable par $f$.** Pour $x\in F$ : $g(f(x))=f(g(x))=f(x)$, donc $f(x)\in F$.

**3. Contradiction.** $f(m)\in F$, donc $f(m)\le\max F=m=g(m)$. Mais $f(m)>g(m)$ par hypothèse : contradiction. (Si $f<g$, on prend $m=\min F$ : $f(m)\ge m=g(m)$, contradiction.)

**3. Conclusion.** Il existe $x\in[0,1]$ tel que $f(x)=g(x)$.
"""

D['x-f-2'] = r"""
**1. Un $\delta$ associé à $\varepsilon=1$.** Par uniforme continuité, il existe $\delta>0$ tel que pour tous $x,y\in\mathbb R$ : $|x-y|\le\delta\Rightarrow|f(x)-f(y)|\le1$.

**2. Découpage de $[0,x]$.** Soit $x\neq0$ (le cas $x=0$ est trivial). Posons $N=\big\lceil\frac{|x|}\delta\big\rceil\ge1$, de sorte que $\frac{|x|}\delta\le N<\frac{|x|}\delta+1$. Points intermédiaires : $x_k=\frac kNx$ pour $0\le k\le N$. Alors $x_0=0$, $x_N=x$ et
$$|x_{k+1}-x_k|=\frac{|x|}N\le\delta.$$

**3. Télescopage.** $f(x)-f(0)=\sum_{k=0}^{N-1}\big(f(x_{k+1})-f(x_k)\big)$, donc par l'inégalité triangulaire
$$|f(x)-f(0)|\le\sum_{k=0}^{N-1}|f(x_{k+1})-f(x_k)|\le N\cdot1<\frac{|x|}\delta+1.$$

**4. Conclusion.** $|f(x)|\le|f(0)|+|f(x)-f(0)|\le\frac1\delta|x|+1+|f(0)|$. On prend $a=\frac1\delta$ et $b=1+|f(0)|$.

**5. La réciproque est fausse.** Soit $f(x)=\sin(x^2)$. Elle vérifie $|f(x)|\le1\le|x|+1$. Montrons qu'elle n'est pas uniformément continue. Posons $x_n=\sqrt{n\pi}$ et $y_n=\sqrt{n\pi+\frac\pi2}$ (avec $n$ pair) : $f(x_n)=\sin(n\pi)=0$ et $f(y_n)=\sin\big(n\pi+\frac\pi2\big)=1$. Par la quantité conjuguée :
$$y_n-x_n=\frac{y_n^2-x_n^2}{y_n+x_n}=\frac{\pi/2}{\sqrt{n\pi+\pi/2}+\sqrt{n\pi}}\xrightarrow[n\to\infty]{}0,$$
alors que $|f(y_n)-f(x_n)|=1$ ne tend pas vers 0. Ceci contredit l'uniforme continuité (qui imposerait $|f(y_n)-f(x_n)|\le\frac12$ dès que $|y_n-x_n|\le\delta'$).

**Moralité.** Une fonction uniformément continue sur $\mathbb R$ est au plus affine à l'infini. Ainsi $x\mapsto x^2$ n'est pas uniformément continue sur $\mathbb R$, car elle n'est majorée par aucune fonction $a|x|+b$.
"""

D['x-f-3'] = r"""
**1. Hypothèse absurde.** Supposons qu'il existe $R=\frac PQ\in\mathbb R(X)$ (fraction irréductible) avec $Q$ sans racine dans $]a,b[$ et $\sin x=R(x)$ pour tout $x\in]a,b[$.

**2. Équation différentielle.** Sur $]a,b[$, $\sin''=-\sin$, et la dérivée de la fonction rationnelle associée à $R$ est la fonction associée à la fraction dérivée $R'$. Donc $R''(x)+R(x)=0$ pour tout $x\in]a,b[$. La fraction $R''+R$ s'écrit $\frac{N}{Q^3}$ avec $N\in\mathbb R[X]$. $N$ s'annule en une infinité de points (tout $]a,b[$), donc $N=0$ : $R''+R=0$ dans $\mathbb R(X)$.

**3. Degré d'une fraction.** Pour $R=\frac PQ\neq0$, on pose $\deg R=\deg P-\deg Q$ (indépendant du représentant). Montrons que si $R'\neq0$, alors $\deg R'\le\deg R-1$. Soient $p=\deg P$, $q=\deg Q$, et $\alpha,\beta$ les coefficients dominants. Alors $R'=\frac{P'Q-PQ'}{Q^2}$.
- Les termes de $P'Q$ et $PQ'$ sont de degré $\le p+q-1$, et le coefficient de $X^{p+q-1}$ dans $P'Q-PQ'$ vaut $p\alpha\beta-q\alpha\beta=(p-q)\alpha\beta$.
- Donc $\deg(P'Q-PQ')\le p+q-1$, et $\deg R'\le(p+q-1)-2q=\deg R-1$.

En itérant, si $R''\neq0$ : $\deg R''\le\deg R-2$.

**4. Contradiction.** $R\neq0$, sinon $\sin$ serait nulle sur $]a,b[$, ce qui est faux. De $R''+R=0$, on tire $R''=-R\neq0$, donc $\deg R=\deg R''\le\deg R-2$ : absurde.

**Conclusion.** La fonction sinus n'est la restriction à aucun intervalle ouvert non vide d'une fraction rationnelle.

**Remarque.** L'argument « $\sin$ a une infinité de zéros » ne suffit pas ici, car sur un petit intervalle $]a,b[$, $\sin$ n'a qu'un nombre fini de zéros. C'est l'équation différentielle qui permet de conclure localement.
"""

D['x-fo-1'] = r"""
**1. Parité.** $f$ est paire (car $(-x)^2=x^2$ sur $[-\pi,\pi]$), donc $b_n=\frac1\pi\int_{-\pi}^\pi f(x)\sin(nx)\,\mathrm dx=0$ (intégrande impaire), et
$$a_n=\frac1\pi\int_{-\pi}^\pi x^2\cos(nx)\,\mathrm dx=\frac2\pi\int_0^\pi x^2\cos(nx)\,\mathrm dx.$$

**2. $a_0$.** $a_0=\frac2\pi\int_0^\pi x^2\,\mathrm dx=\frac2\pi\cdot\frac{\pi^3}3=\frac{2\pi^2}3$.

**3. Première intégration par parties ($n\ge1$).** Avec $u=x^2$ et $v=\frac{\sin nx}n$ :
$$\int_0^\pi x^2\cos(nx)\,\mathrm dx=\Big[\frac{x^2\sin nx}n\Big]_0^\pi-\frac2n\int_0^\pi x\sin(nx)\,\mathrm dx=-\frac2n\int_0^\pi x\sin(nx)\,\mathrm dx,$$
car $\sin(n\pi)=\sin0=0$.

**4. Seconde intégration par parties.** Avec $u=x$ et $v=-\frac{\cos nx}n$, et $\cos(n\pi)=(-1)^n$ :
$$\int_0^\pi x\sin(nx)\,\mathrm dx=\Big[-\frac{x\cos nx}n\Big]_0^\pi+\frac1n\int_0^\pi\cos(nx)\,\mathrm dx=-\frac{\pi(-1)^n}n+\frac1n\Big[\frac{\sin nx}n\Big]_0^\pi=-\frac{\pi(-1)^n}n.$$

**5. Résultat.** $\int_0^\pi x^2\cos(nx)\,\mathrm dx=-\frac2n\cdot\Big(-\frac{\pi(-1)^n}n\Big)=\frac{2\pi(-1)^n}{n^2}$, donc
$$a_n=\frac2\pi\cdot\frac{2\pi(-1)^n}{n^2}=\frac{4(-1)^n}{n^2}.$$

**6. Convergence de la série de Fourier.** $f$ est $2\pi$-périodique et continue, car $f(-\pi)=f(\pi)=\pi^2$ : pas de saut au raccord. Elle est aussi $C^1$ par morceaux. Par le théorème de Dirichlet (ou la convergence normale, puisque $\sum\frac4{n^2}<\infty$), la série de Fourier converge vers $f$ en tout point :
$$x^2=\frac{a_0}2+\sum_{n\ge1}a_n\cos(nx)=\frac{\pi^2}3+4\sum_{n\ge1}\frac{(-1)^n}{n^2}\cos(nx),\qquad x\in[-\pi,\pi].$$

**7. Valeur en $x=\pi$.** $\cos(n\pi)=(-1)^n$, donc $(-1)^n\cos(n\pi)=1$ :
$$\pi^2=\frac{\pi^2}3+4\sum_{n\ge1}\frac1{n^2}\iff\sum_{n\ge1}\frac1{n^2}=\frac14\Big(\pi^2-\frac{\pi^2}3\Big)=\frac{\pi^2}6.$$
En $x=0$, on obtient de même $0=\frac{\pi^2}3+4\sum\frac{(-1)^n}{n^2}$, soit $\sum_{n\ge1}\frac{(-1)^{n+1}}{n^2}=\frac{\pi^2}{12}$.

**8. Parseval.** Pour $f$ continue par morceaux et $2\pi$-périodique : $\frac1\pi\int_{-\pi}^\pi f^2=\frac{a_0^2}2+\sum_{n\ge1}(a_n^2+b_n^2)$. Calculons chaque terme :
$$\frac1\pi\int_{-\pi}^\pi x^4\,\mathrm dx=\frac1\pi\cdot\frac{2\pi^5}5=\frac{2\pi^4}5,\qquad\frac{a_0^2}2=\frac12\cdot\frac{4\pi^4}9=\frac{2\pi^4}9,\qquad a_n^2=\frac{16}{n^4}.$$

**9. Conclusion.** $\frac{2\pi^4}5=\frac{2\pi^4}9+16\sum_{n\ge1}\frac1{n^4}$, donc
$$16\sum_{n\ge1}\frac1{n^4}=2\pi^4\Big(\frac15-\frac19\Big)=\frac{8\pi^4}{45},\qquad\sum_{n\ge1}\frac1{n^4}=\frac{\pi^4}{90}.$$
"""
