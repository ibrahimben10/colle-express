D = {}

D['n-m-Jn'] = r"""
**1. Existence.** $f_n(x)=\frac1{(1+x^3)^{n+1}}$ est continue et positive sur $[0,+\infty[$. Comme $1+x^3\ge1$, on a $0\le f_n(x)\le\frac1{1+x^3}$, et $\frac1{1+x^3}\sim\frac1{x^3}$ en $+\infty$. La fonction $x\mapsto\frac1{x^3}$ est intégrable au voisinage de $+\infty$ (Riemann, exposant $3>1$). Par comparaison de fonctions positives, $f_n$ est intégrable sur $[0,+\infty[$, et $J_n$ existe.

**2. Décomposition en éléments simples.** $1+x^3=(1+x)(x^2-x+1)$, où le second facteur est irréductible sur $\mathbb R$. On cherche $\frac1{1+x^3}=\frac a{1+x}+\frac{bx+c}{x^2-x+1}$. En multipliant par $1+x$ puis en faisant $x=-1$, on obtient $a=\frac13$. Ensuite, $1=\frac13(x^2-x+1)+(bx+c)(1+x)$ donne $b=-\frac13$ (coefficient de $x^2$) et $c=\frac23$ (constante). On réécrit
$$\frac{-\frac13x+\frac23}{x^2-x+1}=-\frac16\cdot\frac{2x-1}{x^2-x+1}+\frac12\cdot\frac1{\big(x-\frac12\big)^2+\frac34}.$$

**2. Primitive.**
$$G(x)=\frac13\ln(1+x)-\frac16\ln(x^2-x+1)+\frac1{\sqrt3}\mathrm{Arctan}\frac{2x-1}{\sqrt3}=\frac16\ln\frac{(1+x)^2}{x^2-x+1}+\frac1{\sqrt3}\mathrm{Arctan}\frac{2x-1}{\sqrt3}.$$

**2. Valeur de $J_0$.** En $+\infty$, $\frac{(1+x)^2}{x^2-x+1}\to1$, donc le logarithme tend vers 0, et $\mathrm{Arctan}\to\frac\pi2$. En $0$, le logarithme vaut $\ln1=0$ et $\mathrm{Arctan}\big(-\frac1{\sqrt3}\big)=-\frac\pi6$. Donc
$$J_0=\frac1{\sqrt3}\Big(\frac\pi2+\frac\pi6\Big)=\frac{2\pi}{3\sqrt3}\approx1{,}209.$$

**3. Intégration par parties.** Sur $[0,A]$, avec $u=\frac1{(1+x^3)^{n+1}}$, $u'=-\frac{3(n+1)x^2}{(1+x^3)^{n+2}}$, $v'=1$ et $v=x$ :
$$\int_0^A\frac{\mathrm dx}{(1+x^3)^{n+1}}=\Big[\frac x{(1+x^3)^{n+1}}\Big]_0^A+3(n+1)\int_0^A\frac{x^3}{(1+x^3)^{n+2}}\mathrm dx.$$
Le crochet est nul en 0 et tend vers 0 quand $A\to\infty$ (il se comporte comme $A^{-3n-2}$). Toutes les intégrales convergent.

**3. Relation.** $\frac{x^3}{(1+x^3)^{n+2}}=\frac{(1+x^3)-1}{(1+x^3)^{n+2}}=\frac1{(1+x^3)^{n+1}}-\frac1{(1+x^3)^{n+2}}$, donc
$$J_n=3(n+1)(J_n-J_{n+1})\iff3(n+1)J_{n+1}=(3n+2)J_n\iff J_{n+1}=\frac{3n+2}{3n+3}J_n.$$

**4. Passage au logarithme.** Par récurrence, $J_n=J_0\prod_{k=0}^{n-1}\frac{3k+2}{3k+3}=J_0\prod_{k=1}^n\Big(1-\frac1{3k}\Big)$. Comme $J_n>0$ :
$$\ln J_n=\ln J_0+\sum_{k=1}^n\ln\Big(1-\frac1{3k}\Big).$$

**4. Développement.** $\ln\big(1-\frac1{3k}\big)=-\frac1{3k}+w_k$, avec $w_k=O\big(\frac1{k^2}\big)$, donc $\sum w_k$ converge absolument, vers une somme $W$. Avec $\sum_{k=1}^n\frac1k=\ln n+\gamma+o(1)$ :
$$\ln J_n=\ln J_0-\frac13\ln n-\frac\gamma3+W+o(1)=-\frac13\ln n+C+o(1),\qquad C=\ln J_0-\frac\gamma3+W.$$

**4. Conclusion.** En prenant l'exponentielle, $J_n=n^{-1/3}e^{C+o(1)}$, donc
$$J_n\sim\frac A{\sqrt[3]n},\qquad A=e^C>0.$$
(On peut montrer, avec la fonction $\Gamma$, que $A=\frac13\Gamma\big(\frac13\big)\approx0{,}893$.)
"""

D['n-m-sintx'] = r"""
**1. Définition.** On pose $g(x,t)=\frac{\sin(tx)}{t(1+t^2)}$ pour $t>0$. Elle est continue en $t$, et :
- en $0^+$, $|\sin(tx)|\le|tx|$ donne $|g(x,t)|\le\frac{|x|}{1+t^2}\le|x|$ : $g$ est bornée (et même prolongeable par continuité en $t=0$, par $x$) ;
- en $+\infty$, $|g(x,t)|\le\frac1{t(1+t^2)}\le\frac1{t^3}$, intégrable.

Donc $t\mapsto g(x,t)$ est intégrable sur $]0,+\infty[$ pour tout $x$ : $F$ est définie sur $\mathbb R$.

**1. Hypothèses du théorème de dérivation sous l'intégrale.**
- Pour tout $t>0$, $x\mapsto g(x,t)$ est $C^1$, avec $\frac{\partial g}{\partial x}(x,t)=\frac{t\cos(tx)}{t(1+t^2)}=\frac{\cos(tx)}{1+t^2}$.
- $\frac{\partial g}{\partial x}$ est continue en $x$ et continue par morceaux en $t$.
- Domination : $\Big|\frac{\partial g}{\partial x}(x,t)\Big|\le\frac1{1+t^2}=\varphi(t)$, intégrable sur $]0,+\infty[$ et indépendante de $x$.
- $g(x,\cdot)$ est intégrable (vu plus haut).

**1. Conclusion.** $F$ est de classe $C^1$ sur $\mathbb R$, et, avec le résultat admis,
$$F'(x)=\int_0^{+\infty}\frac{\cos(tx)}{1+t^2}\mathrm dt=\frac\pi2e^{-|x|}.$$

**2. Intégration.** $F(0)=\int_0^\infty0\,\mathrm dt=0$. Pour $x\ge0$ :
$$F(x)=F(0)+\int_0^xF'(s)\,\mathrm ds=\frac\pi2\int_0^xe^{-s}\,\mathrm ds=\frac\pi2\big(1-e^{-x}\big).$$

**2. Imparité.** $\sin(-tx)=-\sin(tx)$, donc $F(-x)=-F(x)$ : $F$ est impaire. Ainsi
$$F(x)=\frac\pi2\,\mathrm{sgn}(x)\big(1-e^{-|x|}\big).$$
On vérifie que $F(x)\to\frac\pi2$ quand $x\to+\infty$, ce qui est cohérent avec $\int_0^\infty\frac{\sin(tx)}t\mathrm dt=\frac\pi2$ (intégrale de Dirichlet), le facteur $\frac1{1+t^2}$ valant environ 1 près de $t=0$.

**3. Régularité $C^2$.** $F'(x)=\frac\pi2e^{-|x|}$ est dérivable sur $\mathbb R^*$, mais en 0 :
- dérivée à droite : $\frac{\mathrm d}{\mathrm dx}\big(\frac\pi2e^{-x}\big)\big|_{0}=-\frac\pi2$ ;
- dérivée à gauche : $\frac{\mathrm d}{\mathrm dx}\big(\frac\pi2e^{x}\big)\big|_{0}=+\frac\pi2$.

$F'$ n'est pas dérivable en 0 : $F$ n'est **pas** de classe $C^2$ sur $\mathbb R$ (elle l'est sur $\mathbb R^*$, et même $C^\infty$).

**3. Cohérence.** Une seconde dérivation sous l'intégrale ferait apparaître $-\frac{t\sin(tx)}{1+t^2}$, qui n'est pas intégrable sur $]0,+\infty[$ (elle se comporte comme $\frac{\sin(tx)}t$, non absolument intégrable) : il n'y a pas de domination possible, et le théorème ne s'applique pas.
"""

D['n-m-arctantx'] = r"""
**1. Domaine.** Soit $h(x,t)=\frac{\mathrm{Arctan}(tx)}{t(1+t^2)}$ pour $t>0$, continue en $t$.
- En $0^+$ : $|\mathrm{Arctan}\,u|\le|u|$ donne $|h(x,t)|\le\frac{|x|}{1+t^2}$, qui est borné.
- En $+\infty$ : $|\mathrm{Arctan}|\le\frac\pi2$ donne $|h(x,t)|\le\frac\pi{2t(1+t^2)}\le\frac\pi{2t^3}$, intégrable.

Donc $h(x,\cdot)$ est intégrable sur $]0,+\infty[$ pour tout réel $x$ : $D=\mathbb R$.

**2. Dérivée partielle.** Pour $t>0$ fixé, $x\mapsto h(x,t)$ est $C^1$, et
$$\frac{\partial h}{\partial x}(x,t)=\frac1{t(1+t^2)}\cdot\frac t{1+t^2x^2}=\frac1{(1+t^2x^2)(1+t^2)}.$$
Elle est continue, et dominée par $\frac1{1+t^2}$, intégrable sur $]0,+\infty[$ et indépendante de $x$. Par le théorème de dérivation sous l'intégrale, $F$ est $C^1$ sur $\mathbb R$ et
$$F'(x)=\int_0^{+\infty}\frac{\mathrm dt}{(1+t^2x^2)(1+t^2)}.$$

**2. Calcul pour $x^2\neq1$.** Décomposition en éléments simples en la variable $t^2$ :
$$\frac1{(1+x^2t^2)(1+t^2)}=\frac1{1-x^2}\Big(\frac1{1+t^2}-\frac{x^2}{1+x^2t^2}\Big).$$
Vérification : $\frac{(1+x^2t^2)-x^2(1+t^2)}{(\dots)(\dots)}=\frac{1-x^2}{(\dots)(\dots)}$. ✓

**2. Intégrales élémentaires.** $\int_0^\infty\frac{\mathrm dt}{1+t^2}=\frac\pi2$, et pour $x\neq0$, en posant $s=|x|t$, $\int_0^\infty\frac{x^2\,\mathrm dt}{1+x^2t^2}=|x|\int_0^\infty\frac{\mathrm ds}{1+s^2}=|x|\frac\pi2$. Donc
$$F'(x)=\frac1{1-x^2}\cdot\frac\pi2\big(1-|x|\big)=\frac\pi2\cdot\frac{1-|x|}{(1-|x|)(1+|x|)}=\frac\pi{2(1+|x|)}.$$
La formule est vraie aussi pour $x=0$ ($F'(0)=\frac\pi2$), et pour $x=\pm1$ par continuité de $F'$.

**3. Intégration.** $F(0)=0$ et $F$ est impaire (car $\mathrm{Arctan}$ l'est). Pour $x\ge0$ :
$$F(x)=\int_0^x\frac\pi{2(1+s)}\mathrm ds=\frac\pi2\ln(1+x),\qquad\text{donc}\qquad F(x)=\frac\pi2\,\mathrm{sgn}(x)\ln(1+|x|).$$

**4. Intégration par parties.** Sur $[\varepsilon,A]$, avec $u=\mathrm{Arctan}^2t$, $u'=\frac{2\,\mathrm{Arctan}\,t}{1+t^2}$, $v'=\frac1{t^2}$ et $v=-\frac1t$ :
$$\int_\varepsilon^A\frac{\mathrm{Arctan}^2t}{t^2}\mathrm dt=\Big[-\frac{\mathrm{Arctan}^2t}t\Big]_\varepsilon^A+2\int_\varepsilon^A\frac{\mathrm{Arctan}\,t}{t(1+t^2)}\mathrm dt.$$

**4. Limites du crochet.** En $0^+$, $\frac{\mathrm{Arctan}^2t}t\sim\frac{t^2}t=t\to0$. En $+\infty$, $\frac{\mathrm{Arctan}^2t}t\le\frac{\pi^2}{4t}\to0$. Le crochet tend donc vers 0, et les deux intégrales convergent.

**4. Conclusion.**
$$\int_0^{+\infty}\Big(\frac{\mathrm{Arctan}\,t}t\Big)^2\mathrm dt=2\int_0^{+\infty}\frac{\mathrm{Arctan}\,t}{t(1+t^2)}\mathrm dt=2F(1)=2\cdot\frac\pi2\ln2=\pi\ln2\approx2{,}18.$$
"""

D['n-m-geodiff'] = r"""
**1. Loi de $X_1-X_2$.** Soit $n\in\mathbb N$. On décompose selon la valeur de $X_2$ (système complet d'événements $(X_2=k)_{k\ge1}$) ; l'événement $(X_1-X_2=n)$ est l'union disjointe des $(X_2=k)\cap(X_1=k+n)$. Par indépendance :
$$P(X_1-X_2=n)=\sum_{k=1}^{+\infty}P(X_2=k)P(X_1=k+n)=\sum_{k=1}^{+\infty}pq^{k-1}\cdot pq^{k+n-1}=p^2q^n\sum_{k=1}^{+\infty}q^{2(k-1)}.$$

**1. Série géométrique.** La raison est $q^2<1$, donc $\sum_{k\ge1}q^{2(k-1)}=\frac1{1-q^2}$. Avec $1-q^2=(1-q)(1+q)=p(1+q)$ :
$$P(X_1-X_2=n)=\frac{p^2q^n}{p(1+q)}=\frac{pq^n}{1+q}.$$

**1. Loi de $Y$.**
- $n=0$ : $P(Y=0)=P(X_1=X_2)=\frac p{1+q}$.
- $n\ge1$ : $(Y=n)=(X_1-X_2=n)\cup(X_1-X_2=-n)$, réunion disjointe. Les variables $X_1$ et $X_2$ jouent des rôles symétriques (indépendantes, de même loi), donc $X_1-X_2$ et $X_2-X_1$ ont la même loi, et $P(X_1-X_2=-n)=P(X_1-X_2=n)$. D'où
$$P(Y=n)=\frac{2pq^n}{1+q},\qquad n\ge1.$$

**1. Vérification.** $\frac p{1+q}+\frac{2p}{1+q}\cdot\frac q{1-q}=\frac p{1+q}+\frac{2q}{1+q}=\frac{p+2q}{1+q}=\frac{1+q}{1+q}=1$. ✓

**2. Espérance.** $Y\ge0$, et l'on vérifie la convergence de $\sum nP(Y=n)$. On utilise $\sum_{n\ge1}nq^{n-1}=\frac1{(1-q)^2}=\frac1{p^2}$ (dérivée de la série géométrique, pour $|q|<1$), donc $\sum_{n\ge1}nq^n=\frac q{p^2}$, et
$$E(Y)=\sum_{n\ge1}n\frac{2pq^n}{1+q}=\frac{2p}{1+q}\cdot\frac q{p^2}=\frac{2q}{p(1+q)}.$$

**3. Moment d'ordre 2 de $X_1-X_2$.** $X_1$ et $X_2$ ont un moment d'ordre 2 (loi géométrique), donc $X_1-X_2$ aussi. On développe, en utilisant $E(X_1X_2)=E(X_1)E(X_2)$ (indépendance) et le fait qu'elles ont même loi :
$$E\big((X_1-X_2)^2\big)=E(X_1^2)-2E(X_1)E(X_2)+E(X_2^2)=2E(X_1^2)-2E(X_1)^2=2V(X_1).$$
Avec $V(X_1)=\frac q{p^2}$, on obtient $E\big((X_1-X_2)^2\big)=\frac{2q}{p^2}$.

**3. Variance de $Y$.** $Y^2=(X_1-X_2)^2$ admet une espérance, donc $Y$ admet une variance, et par la formule de König-Huygens :
$$V(Y)=E(Y^2)-E(Y)^2=\frac{2q}{p^2}-\frac{4q^2}{p^2(1+q)^2}=\frac{2q(1+q)^2-4q^2}{p^2(1+q)^2}=\frac{2q(1+q^2)}{p^2(1+q)^2},$$
car $(1+q)^2-2q=1+q^2$.
"""

D['n-m-kerf2'] = r"""
**1. Application restreinte.** On considère $g:\mathrm{Ker}\,f^2\to E$, $x\mapsto f(x)$, linéaire.
- **Noyau** : $\mathrm{Ker}\,g=\mathrm{Ker}\,f\cap\mathrm{Ker}\,f^2=\mathrm{Ker}\,f$, car $\mathrm{Ker}\,f\subset\mathrm{Ker}\,f^2$ (si $f(x)=0$, alors $f^2(x)=f(0)=0$).
- **Image** : $\mathrm{Im}\,g=f(\mathrm{Ker}\,f^2)$. Elle est contenue dans $\mathrm{Ker}\,f$, car si $f^2(x)=0$, alors $f\big(f(x)\big)=0$, donc $f(x)\in\mathrm{Ker}\,f$.

**1. Théorème du rang.** Appliqué à $g$, défini sur l'espace de dimension finie $\mathrm{Ker}\,f^2$ :
$$\dim\mathrm{Ker}\,f^2=\dim\mathrm{Ker}\,g+\mathrm{rg}\,g=\dim\mathrm{Ker}\,f+\dim f(\mathrm{Ker}\,f^2).\qquad(\star)$$
Comme $f(\mathrm{Ker}\,f^2)\subset\mathrm{Ker}\,f$, $\dim f(\mathrm{Ker}\,f^2)\le\dim\mathrm{Ker}\,f$, et donc
$$\dim\mathrm{Ker}\,f^2\le2\dim\mathrm{Ker}\,f.$$

**2. (i) ⇔ (iii).** D'après $(\star)$, (i) équivaut à $\dim f(\mathrm{Ker}\,f^2)=\dim\mathrm{Ker}\,f$. Or $f(\mathrm{Ker}\,f^2)$ est un sous-espace de $\mathrm{Ker}\,f$. Un sous-espace de même dimension (finie) que l'espace qui le contient lui est égal, donc (i) équivaut à $f(\mathrm{Ker}\,f^2)=\mathrm{Ker}\,f$, c'est-à-dire (iii).

**2. (iii) ⇒ (ii).** $\mathrm{Ker}\,f=f(\mathrm{Ker}\,f^2)\subset f(E)=\mathrm{Im}\,f$.

**2. (ii) ⇒ (iii).** On a déjà $f(\mathrm{Ker}\,f^2)\subset\mathrm{Ker}\,f$ (question 1). Réciproquement, soit $y\in\mathrm{Ker}\,f$. Par (ii), $y\in\mathrm{Im}\,f$ : il existe $x\in E$ tel que $y=f(x)$. Alors $f^2(x)=f(y)=0$, donc $x\in\mathrm{Ker}\,f^2$, et $y=f(x)\in f(\mathrm{Ker}\,f^2)$. D'où l'égalité (iii).

**Conclusion.** (i) ⇔ (iii) ⇔ (ii).

**Exemple.** Pour la dérivation $D$ sur $\mathbb R_n[X]$ ($n\ge1$) : $\mathrm{Ker}\,D=\mathbb R_0[X]\subset\mathrm{Im}\,D=\mathbb R_{n-1}[X]$, et l'on a bien $\dim\mathrm{Ker}\,D^2=2=2\dim\mathrm{Ker}\,D$. À l'inverse, pour un projecteur $p$ non nul et différent de l'identité, $\mathrm{Ker}\,p^2=\mathrm{Ker}\,p$ et $\mathrm{Ker}\,p\cap\mathrm{Im}\,p=\{0\}$ : (ii) est fausse dès que $\mathrm{Ker}\,p\neq\{0\}$.
"""
