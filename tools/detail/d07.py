D = {}

D['m-ccmp-13a'] = r"""
**Notations.** $u=(a,a^2,\dots,a^n)^{\top}$, $v=(1,\dots,1)^{\top}$, $S_1=\sum_{i=1}^na^i=v^{\top}u$, $S_2=\sum_{i=1}^na^{2i}=u^{\top}u$, et $v^{\top}v=n$.

**Écriture de $A$.** Le coefficient $(i,j)$ de $uv^{\top}$ est $u_iv_j=a^i$ et celui de $vu^{\top}$ est $v_iu_j=a^j$. Donc
$$A=uv^{\top}+vu^{\top}.$$

**Cas $n=1$.** $A=(2a)$, de rang 1, $\chi_A=X-2a$.

**Rang pour $n\ge2$.** Pour tout $x\in\mathbb R^n$, $Ax=u\,(v^{\top}x)+v\,(u^{\top}x)$ (les parenthèses sont des scalaires) : $\mathrm{Im}\,A\subset P=\mathrm{Vect}(u,v)$. Les vecteurs $u$ et $v$ sont libres : sinon $u=\lambda v$ donnerait $a=a^2=\lambda$, impossible car $a\neq0,1$. Calculons l'action de $A$ sur $P$ :
$$Au=u\,(v^{\top}u)+v\,(u^{\top}u)=S_1u+S_2v,\qquad Av=u\,(v^{\top}v)+v\,(u^{\top}v)=n\,u+S_1v.$$
Dans la base $(u,v)$ de $P$, l'endomorphisme induit a pour matrice $B=\begin{pmatrix}S_1&n\\S_2&S_1\end{pmatrix}$, de déterminant $S_1^2-nS_2$.

**$B$ est inversible.** Par Cauchy-Schwarz, $S_1^2=(v^{\top}u)^2\le\|v\|^2\|u\|^2=nS_2$, avec égalité seulement si $u$ et $v$ sont colinéaires, ce qui n'est pas le cas. Donc $S_1^2-nS_2<0$, $B$ est inversible, $A(P)=P$ et $\mathrm{rg}\,A=\dim P=2$.

**Noyau.** Comme $(u,v)$ est libre, $Ax=0\iff v^{\top}x=0$ et $u^{\top}x=0$ : $\ker A=P^{\perp}$, de dimension $n-2$, et $\mathbb R^n=P\oplus\ker A$.

**Polynôme caractéristique.** Dans une base formée de $(u,v)$ complétée par une base de $\ker A$, la matrice de $A$ est diagonale par blocs $\begin{pmatrix}B&0\\0&0_{n-2}\end{pmatrix}$. Donc
$$\chi_A=\chi_B\cdot X^{n-2},\qquad\chi_B=X^2-\mathrm{Tr}(B)X+\det B=X^2-2S_1X+S_1^2-nS_2.$$

**Valeurs explicites.** Par les sommes géométriques ($a\neq1$) :
$$S_1=a\,\frac{a^n-1}{a-1},\qquad S_2=a^2\,\frac{a^{2n}-1}{a^2-1}.$$
Les valeurs propres non nulles sont $S_1\pm\sqrt{nS_2}$ (discriminant réduit $S_1^2-(S_1^2-nS_2)=nS_2>0$) ; leur produit $S_1^2-nS_2$ est négatif : l'une est positive, l'autre négative.
===RÉPONSE===
$\mathrm{rg}\,A=2$ pour $n\ge2$ ; $\chi_A=X^{n-2}\big(X^2-2S_1X+S_1^2-nS_2\big)$ avec $S_1=\sum a^i$, $S_2=\sum a^{2i}$.
"""

D['m-ccmp-13b'] = r"""
**Sens réciproque : $f$ concave $\Rightarrow$ l'inégalité.** Fixons $x\in\mathbb R$, $r\ge0$ et $s\in[0,r]$. Le point $x$ est le milieu de $x-s$ et $x+s$ ; par concavité (avec le coefficient $\frac12$) :
$$f(x)=f\Big(\tfrac12(x+s)+\tfrac12(x-s)\Big)\ge\tfrac12f(x+s)+\tfrac12f(x-s).$$
On intègre cette inégalité en $s$ sur $[0,r]$ :
$$2rf(x)\ge\int_0^rf(x+s)\,\mathrm ds+\int_0^rf(x-s)\,\mathrm ds=\int_x^{x+r}f(t)\,\mathrm dt+\int_{x-r}^xf(t)\,\mathrm dt=\int_{x-r}^{x+r}f(t)\,\mathrm dt,$$
avec les changements de variable $t=x+s$ et $t=x-s$.

**Sens direct, étape 1 : la fonction auxiliaire.** Fixons $x$ et posons, pour $r\ge0$,
$$F(r)=\int_{x-r}^{x+r}f(t)\,\mathrm dt-2rf(x).$$
L'hypothèse dit $F(r)\le0$ pour tout $r\ge0$. Avec une primitive $\Phi$ de $f$, $F(r)=\Phi(x+r)-\Phi(x-r)-2rf(x)$ ; donc $F$ est dérivable et
$$F'(r)=f(x+r)+f(x-r)-2f(x).$$
Comme $f$ est $C^2$, $F'$ l'est aussi, donc $F$ est $C^3$, avec
$$F''(r)=f'(x+r)-f'(x-r),\qquad F'''(r)=f''(x+r)+f''(x-r).$$

**Sens direct, étape 2 : Taylor en 0.** $F(0)=0$, $F'(0)=f(x)+f(x)-2f(x)=0$, $F''(0)=f'(x)-f'(x)=0$, $F'''(0)=2f''(x)$. La formule de Taylor-Young à l'ordre 3 en $0$ donne
$$F(r)=\frac{F'''(0)}6r^3+o(r^3)=\frac{f''(x)}3r^3+o(r^3)\qquad(r\to0^+).$$

**Sens direct, étape 3 : signe.** Si on avait $f''(x)>0$, alors $\frac{F(r)}{r^3}\to\frac{f''(x)}3>0$, donc $F(r)>0$ pour $r>0$ assez petit, ce qui contredit l'hypothèse. Donc $f''(x)\le0$. Ceci vaut pour tout $x$ : $f''\le0$ sur $\mathbb R$, et $f$ (de classe $C^2$) est concave.

**Conclusion.** L'inégalité $\int_{x-r}^{x+r}f\le2rf(x)$ pour tous $x,r$ caractérise les fonctions concaves. (Pour les fonctions convexes, l'inégalité est renversée : c'est l'inégalité d'Hermite-Hadamard.)
"""

D['m-ccmp-14a'] = r"""
**1. $I_n+A$ est inversible.** Soit $\lambda\in\mathbb C$ une valeur propre de $A$, $X\in\mathbb C^n\setminus\{0\}$ avec $AX=\lambda X$, et $s=\overline X^{\top}AX=\lambda\|X\|^2$. Comme $s$ est un scalaire, $s=s^{\top}=X^{\top}A^{\top}\overline X=-X^{\top}A\overline X=-\overline{s}$ ($A$ réelle). Donc $s$, et $\lambda$, sont imaginaires purs. En particulier $-1$ n'est pas valeur propre de $A$ : $I_n+A$ est inversible et $C(A)$ est bien défini.

**1. Commutations.** $(I_n+A)(I_n-A)=I_n-A^2=(I_n-A)(I_n+A)$. En multipliant cette égalité à gauche et à droite par $(I_n+A)^{-1}$ :
$$(I_n-A)(I_n+A)^{-1}=(I_n+A)^{-1}(I_n-A).$$
De même ($-1$ et $1$ ne sont pas valeurs propres), $I_n-A$ est inversible, et $(I_n+A)^{-1}$, $(I_n-A)^{-1}$ commutent (inverses de matrices qui commutent).

**1. $C(A)$ est orthogonale.** Notons $C=C(A)$. Avec $A^{\top}=-A$ et $(M^{-1})^{\top}=(M^{\top})^{-1}$ :
$$C^{\top}=(I_n-A)^{\top}\big((I_n+A)^{-1}\big)^{\top}=(I_n+A)\,(I_n-A)^{-1}.$$
Donc, en faisant commuter les deux inverses :
$$C^{\top}C=(I_n+A)(I_n-A)^{-1}(I_n+A)^{-1}(I_n-A)=(I_n+A)(I_n+A)^{-1}(I_n-A)^{-1}(I_n-A)=I_n.$$

**1. $\det C=1$.** $\det(I_n-A)=\det\big((I_n-A)^{\top}\big)=\det(I_n+A)$, donc $\det C=\frac{\det(I_n-A)}{\det(I_n+A)}=1$. Ainsi $C\in SO_n(\mathbb R)$.

**2. $I_n+C$ est toujours inversible.** En factorisant par $(I_n+A)^{-1}$ à gauche :
$$I_n+C=(I_n+A)^{-1}\big[(I_n+A)+(I_n-A)\big]=2(I_n+A)^{-1},$$
inversible. Autrement dit, $-1$ n'est jamais valeur propre de $C(A)$.

**3. Injectivité.** De $I_n+C(A)=2(I_n+A)^{-1}$ on tire $I_n+A=2\big(I_n+C(A)\big)^{-1}$, soit $A=2\big(I_n+C(A)\big)^{-1}-I_n$ : $A$ est déterminée par $C(A)$, donc $C$ est injective.

**3. Non-surjectivité.** Par la question 2, l'image ne contient aucune matrice ayant $-1$ pour valeur propre. Pour $n=2$, $-I_2\in SO_2(\mathbb R)$ (rotation d'angle $\pi$, $\det=1$) n'est donc pas atteinte : $C$ n'est pas surjective sur $SO_n$ (même raisonnement pour $n\ge2$ avec $\mathrm{diag}(-1,-1,1,\dots,1)$).

**3. Description exacte de l'image.** Soit $R\in SO_n$ sans valeur propre $-1$, et $A=(I_n-R)(I_n+R)^{-1}$.
- $A$ est antisymétrique : avec $R^{\top}=R^{-1}$, $I_n+R^{-1}=R^{-1}(I_n+R)$ et $I_n-R^{-1}=R^{-1}(R-I_n)$, d'où $A^{\top}=(I_n+R^{\top})^{-1}(I_n-R^{\top})=(I_n+R)^{-1}R\,R^{-1}(R-I_n)=-(I_n+R)^{-1}(I_n-R)=-A$ (les facteurs commutent).
- $C(A)=R$ : $I_n+A=2(I_n+R)^{-1}$ et $I_n-A=2R(I_n+R)^{-1}$, donc $C(A)=\frac12(I_n+R)\cdot2R(I_n+R)^{-1}=R$.

**Conclusion.** $C$ est une bijection de $\mathcal A_n(\mathbb R)$ sur $\{R\in SO_n(\mathbb R):-1\notin\mathrm{Sp}\,R\}$ : injective, non surjective.
"""

D['m-ccmp-14b'] = r"""
**1. Existence.** Soit $x>0$ et $h(x,t)=\frac{t^x}{e^t-1}$, continue et positive sur $]0,+\infty[$.
- En $0^+$ : $e^t-1\sim t$, donc $h(x,t)\sim t^{x-1}=\frac1{t^{1-x}}$ avec $1-x<1$ : intégrable en 0 (Riemann).
- En $+\infty$ : pour $t\ge1$, $e^t\ge e>2$ donc $e^t-1\ge\frac{e^t}2$, et $h(x,t)\le2t^xe^{-t}$. Or $t^2\cdot t^xe^{-t}\to0$ (croissances comparées), donc $t^xe^{-t}=o(1/t^2)$, intégrable en $+\infty$.

Ainsi $f(x)$ est bien définie pour tout $x>0$.

**1. Continuité par domination sur un segment.** Soit $[a,b]\subset]0,+\infty[$ et $x\in[a,b]$. Pour $0<t\le1$, $t^x\le t^a$ ($t\mapsto$ exposant décroissant quand $t\le1$) ; pour $t\ge1$, $t^x\le t^b$. Donc
$$0\le h(x,t)\le\varphi(t)=\frac{t^a+t^b}{e^t-1},$$
et $\varphi$ est intégrable sur $]0,+\infty[$ (c'est $h(a,\cdot)+h(b,\cdot)$, intégrables par l'étape précédente). Comme $x\mapsto h(x,t)$ est continue, le théorème de continuité sous l'intégrale donne : $f$ est continue sur $[a,b]$. Tout point de $]0,+\infty[$ est intérieur à un tel segment, donc $f$ est continue sur $]0,+\infty[$.

**2. Développement de l'intégrande.** Pour $t>0$, $0<e^{-t}<1$, donc par la série géométrique :
$$\frac1{e^t-1}=\frac{e^{-t}}{1-e^{-t}}=\sum_{k\ge1}e^{-kt},\qquad h(x,t)=\sum_{k\ge1}t^xe^{-kt}.$$

**2. Intégration terme à terme.** Les fonctions $t\mapsto t^xe^{-kt}$ sont positives et continues sur $]0,+\infty[$ ; pour des séries de fonctions positives, on peut intervertir somme et intégrale :
$$f(x)=\sum_{k\ge1}\int_0^{+\infty}t^xe^{-kt}\,\mathrm dt.$$

**2. Calcul de chaque terme.** Changement de variable $u=kt$ ($t=\frac uk$, $\mathrm dt=\frac{\mathrm du}k$, bijection croissante de $]0,+\infty[$) :
$$\int_0^{+\infty}t^xe^{-kt}\,\mathrm dt=\int_0^{+\infty}\frac{u^x}{k^x}e^{-u}\frac{\mathrm du}k=\frac1{k^{x+1}}\int_0^{+\infty}u^xe^{-u}\,\mathrm du=\frac{\Gamma(x+1)}{k^{x+1}}.$$

**Conclusion.** Pour $x>0$ (donc $x+1>1$, la série de Riemann converge) :
$$f(x)=\sum_{k\ge1}\frac{\Gamma(x+1)}{k^{x+1}}=\Gamma(x+1)\,\zeta(x+1).$$
Exemple : $f(1)=\Gamma(2)\zeta(2)=1\cdot\frac{\pi^2}6$ ; et $f(3)=3!\,\zeta(4)=\frac{\pi^4}{15}$ (intégrale de la loi de Planck).
"""
