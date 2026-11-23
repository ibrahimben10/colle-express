D = {}

D['m-ccmp-02b'] = r"""
**Deux rappels utilisés.**
- $M$ est diagonalisable si et seulement si elle annule un polynôme scindé à racines simples.
- Si $M=QDQ^{-1}$, alors $M^k=QD^kQ^{-1}$ pour tout $k$ (les $Q^{-1}Q$ intermédiaires se simplifient), donc par linéarité $P(M)=Q\,P(D)\,Q^{-1}$ pour tout polynôme $P$.

**1. Sens direct.** Supposons $M=QDQ^{-1}$ avec $D=\mathrm{diag}(d_1,\dots,d_n)$. Soit $P\in\mathbb C[X]$ tel que $P(M)^n=0$. D'après le rappel, $P(M)=Q\,\mathrm{diag}\big(P(d_1),\dots,P(d_n)\big)\,Q^{-1}$, donc
$$P(M)^n=Q\,\mathrm{diag}\big(P(d_1)^n,\dots,P(d_n)^n\big)\,Q^{-1}=0.$$
En multipliant à gauche par $Q^{-1}$ et à droite par $Q$, on obtient $P(d_i)^n=0$, donc $P(d_i)=0$ pour tout $i$. Ainsi $\mathrm{diag}(P(d_i))=0$ et $P(M)=0$.

**1. Sens réciproque.** Supposons la propriété vraie. Sur $\mathbb C$, $\chi_M$ est scindé : $\chi_M=\prod_{i=1}^r(X-\lambda_i)^{m_i}$ avec $\lambda_1,\dots,\lambda_r$ distincts et $m_i\ge1$, $\sum m_i=n$. Posons $P=\prod_{i=1}^r(X-\lambda_i)$.

Comme $m_i\le n$ pour tout $i$, chaque facteur $(X-\lambda_i)^{m_i}$ divise $(X-\lambda_i)^n$, donc $\chi_M$ divise $P^n=\prod(X-\lambda_i)^n$ : il existe $R$ avec $P^n=R\,\chi_M$. Par le théorème de Cayley-Hamilton, $\chi_M(M)=0$, donc
$$P(M)^n=P^n(M)=R(M)\,\chi_M(M)=0.$$
L'hypothèse donne alors $P(M)=0$ : $M$ annule $P$, scindé à racines simples ($\lambda_i$ distincts). Donc $M$ est diagonalisable.

**2. Sur $\mathbb R$ : l'équivalence est fausse.** Prenons $M=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, avec $\chi_M=X^2+1$.
- $M$ n'est pas diagonalisable sur $\mathbb R$ : $\chi_M$ n'a pas de racine réelle, donc $M$ n'a aucune valeur propre réelle.
- Pourtant $M$ vérifie la propriété (avec des polynômes réels) : $\chi_M$ a deux racines distinctes $\pm i$, donc $M$ est diagonalisable dans $\mathcal M_2(\mathbb C)$. Si $P\in\mathbb R[X]\subset\mathbb C[X]$ vérifie $P(M)^2=0$, le sens direct de la question 1 (appliqué dans $\mathbb C$) donne $P(M)=0$.

**Conclusion.** Sur $\mathbb C$ l'équivalence est vraie ; sur $\mathbb R$, la propriété caractérise en fait les matrices diagonalisables **sur $\mathbb C$** (même preuve, en remarquant que $P=\prod(X-\lambda_i)$ est réel car les valeurs propres non réelles vont par paires conjuguées).
"""

D['m-ccmp-03a'] = r"""
**Préliminaire : $S$ est une matrice compagnon.** Par définition, $Se_j=e_{j+1}$ pour $1\le j\le n-1$ (coefficient 1 en position $(j+1,j)$) et $Se_n=p^me_1$. Donc $S^ke_1=e_{k+1}$ pour $k\le n-1$, puis $S^ne_1=S(S^{n-1}e_1)=Se_n=p^me_1$. Comme $S^n$ commute avec $S^{j-1}$ et $e_j=S^{j-1}e_1$ : $S^ne_j=S^{j-1}(S^ne_1)=S^{j-1}(p^me_1)=p^me_j$ pour tout $j$. Ainsi
$$S^n=p^mI_n,$$
et $S$ est inversible ($S\cdot\frac1{p^m}S^{n-1}=I_n$).

**1.** Comme $m\wedge n=1$, le théorème de Bézout fournit $(a,b)\in\mathbb Z^2$ avec $an+bm=1$. Alors, $S$ étant inversible (puissances négatives permises) et commutant avec les scalaires :
$$(p^aS^b)^n=p^{an}\,S^{bn}=p^{an}\,(S^n)^b=p^{an}\,p^{bm}\,I_n=p^{an+bm}I_n=p\,I_n.$$

**2. Réduction à une matrice entière.** Notons $U=p^aS^b$, de sorte que $U^n=pI_n$. Le polynôme $X^n-p$ annule $U$. Ses racines complexes sont les $\omega p^{1/n}$, $\omega\in\mathbb U_n$ : il est scindé à racines simples sur $\mathbb C$, donc $U$ est diagonalisable, et ses valeurs propres sont parmi ces racines. Montrons qu'elles y sont toutes : les valeurs propres de $S$ sont les racines de $\chi_S=X^n-p^m$, soit les $\zeta p^{m/n}$ ($\zeta\in\mathbb U_n$), toutes simples ; celles de $U$ sont les $p^a(\zeta p^{m/n})^b=\zeta^bp^{(an+bm)/n}=\zeta^bp^{1/n}$. Comme $b\wedge n=1$ (Bézout encore), $\zeta\mapsto\zeta^b$ est une bijection de $\mathbb U_n$ : $U$ a $n$ valeurs propres distinctes et $\chi_U=X^n-p$.

Soit $C$ la matrice compagnon de $X^n-p$ (même forme que $S$ avec $p$ à la place de $p^m$). $U$ et $C$ ont le même polynôme caractéristique $X^n-p$, à racines simples : elles sont toutes deux semblables (dans $\mathcal M_n(\mathbb C)$) à la même matrice diagonale, donc semblables entre elles : $U=PCP^{-1}$ avec $P\in GL_n(\mathbb C)$. Alors $\sum\lambda_kU^k=P\big(\sum\lambda_kC^k\big)P^{-1}$, et ces deux matrices ont le même déterminant. Il suffit donc de montrer que $Q=\sum_{k=0}^{n-1}\lambda_kC^k\in\mathcal M_n(\mathbb Z)$ a un déterminant non nul (une matrice rationnelle de déterminant non nul est dans $GL_n(\mathbb Q)$).

**2. Réduction modulo $p$.** Tous les coefficients de $C$ sont entiers ; modulo $p$, le coefficient $p$ devient 0 et $C\equiv N$, où $N$ est la matrice de décalage ($Ne_j=e_{j+1}$, $Ne_n=0$), triangulaire inférieure stricte. Donc
$$Q\equiv\lambda_0I_n+\lambda_1N+\dots+\lambda_{n-1}N^{n-1}\pmod p,$$
matrice triangulaire inférieure de diagonale $(\lambda_0,\dots,\lambda_0)$. Le déterminant est un polynôme à coefficients entiers en les coefficients de la matrice, donc il est compatible avec la réduction modulo $p$ :
$$\det Q\equiv\lambda_0^n\pmod p.$$
Comme $p$ est premier et $p\nmid\lambda_0$, $p\nmid\lambda_0^n$ (lemme d'Euclide). Donc $\det Q\ne0$, et $\sum\lambda_kU^k\in GL_n(\mathbb Q)$.

**3.** Soit $\lambda\in\mathbb Q^n\setminus\{0\}$. Multiplier tous les $\lambda_k$ par un même rationnel non nul ne change pas l'inversibilité : on peut supposer $\lambda\in\mathbb Z^n$ avec $\mathrm{pgcd}(\lambda_0,\dots,\lambda_{n-1})=1$. Si $p\nmid\lambda_0$, on conclut par la question 2. Sinon, comme le pgcd vaut 1, les $\lambda_k$ ne sont pas tous divisibles par $p$ : soit $j\ge1$ le plus petit indice tel que $p\nmid\lambda_j$. Posons $V=\sum_k\lambda_kU^k$. Avec $U^n=pI_n$ :
$$\frac1p\,V\,U^{n-j}=\sum_{k\ge j}\lambda_k\frac{U^{k+n-j}}p+\sum_{k<j}\frac{\lambda_k}p\,U^{k+n-j}=\sum_{k\ge j}\lambda_kU^{k-j}+\sum_{k<j}\frac{\lambda_k}p\,U^{k+n-j}.$$
Les exposants $k-j$ ($k\ge j$) et $k+n-j$ ($k<j$) sont tous distincts et dans $[\![0,n-1]\!]$ ; les coefficients sont entiers ($p\mid\lambda_k$ pour $k<j$) et le coefficient constant est $\lambda_j$, non divisible par $p$. Par la question 2, $\frac1pVU^{n-j}$ est inversible ; comme $U$ l'est, $V$ l'est aussi.

**4.** Vérifions d'abord que $S\in\mathbb Q[U]$ : avec $an+bm=1$, $U^m=p^{am}S^{bm}=p^{am}S^{1-an}=p^{am}S\,(S^n)^{-a}=p^{am}S\,p^{-am}=S$.

Raisonnons par l'absurde : $X^n-p^m=AB$ avec $A,B\in\mathbb Q[X]$ de degrés $\ge1$, donc $<n$. Comme $S$ est une matrice compagnon, $(I,S,\dots,S^{n-1})$ est libre (ces matrices envoient $e_1$ sur $e_1,\dots,e_n$) : un polynôme non nul de degré $<n$ n'annule pas $S$, donc $A(S)\ne0$ et $B(S)\ne0$. Or $A(S)$ et $B(S)$ sont des polynômes en $U$ (car $S=U^m$), qui se réduisent à des combinaisons $\sum_{k<n}\lambda_kU^k$ grâce à $U^n=pI_n$ ; par la question 3, elles sont inversibles. Mais $A(S)B(S)=\chi_S(S)=0$ : un produit de deux matrices inversibles serait nul, absurde.

**Conclusion.** $X^n-p^m$ est irréductible dans $\mathbb Q[X]$.
"""

D['m-ccmp-03b'] = r"""
**Notations.** Soit $g(t)=\dfrac{\sin(\ln t)}t$ sur $[1,+\infty[$, de classe $C^1$, et $w_n=g(n)-\displaystyle\int_n^{n+1}g(t)\,\mathrm dt$.

**1. Majoration de $g'$.** Par dérivée d'un quotient, avec $(\sin(\ln t))'=\frac{\cos(\ln t)}t$ :
$$g'(t)=\frac{\frac{\cos(\ln t)}t\cdot t-\sin(\ln t)}{t^2}=\frac{\cos(\ln t)-\sin(\ln t)}{t^2},\qquad\text{donc}\qquad|g'(t)|\le\frac2{t^2}.$$

**1. Majoration de $w_n$.** Comme $\int_n^{n+1}g(n)\,\mathrm dt=g(n)$ (intervalle de longueur 1) :
$$w_n=\int_n^{n+1}\big(g(n)-g(t)\big)\,\mathrm dt.$$
Pour $t\in[n,n+1]$, l'inégalité des accroissements finis donne $|g(n)-g(t)|\le\sup_{[n,n+1]}|g'|\cdot|t-n|\le\frac2{n^2}$. Donc $|w_n|\le\dfrac2{n^2}$.

**1. Conclusion.** $\sum\frac2{n^2}$ converge (Riemann), donc $\sum w_n$ converge absolument. Comme $g(n)=w_n+\int_n^{n+1}g$, les séries $\sum g(n)$ et $\sum\int_n^{n+1}g$ sont de même nature (la différence de deux séries convergentes converge, et la somme d'une convergente et d'une divergente diverge).

Remarque : on ne peut pas utiliser la comparaison série-intégrale usuelle, qui suppose $g$ monotone ; ici $g$ change de signe une infinité de fois.

**2. Sommes partielles de la série des intégrales.** Par la relation de Chasles, puis le changement de variable $u=\ln t$ ($\mathrm du=\frac{\mathrm dt}t$, $C^1$ croissant de $[1,N]$ sur $[0,\ln N]$) :
$$T_N=\sum_{n=1}^{N-1}\int_n^{n+1}\frac{\sin(\ln t)}t\,\mathrm dt=\int_1^N\frac{\sin(\ln t)}t\,\mathrm dt=\int_0^{\ln N}\sin u\,\mathrm du=1-\cos(\ln N).$$

**2. Absence de limite.** Montrons que $(T_N)$ diverge. Pour $k\in\mathbb N^*$, soit $N_k=\lfloor e^{2k\pi}\rfloor$. Comme $\ln$ est croissante et $e^{2k\pi}-1<N_k\le e^{2k\pi}$ :
$$\ln(e^{2k\pi}-1)<\ln N_k\le2k\pi,\qquad\text{et}\qquad\ln(e^{2k\pi}-1)=2k\pi+\ln(1-e^{-2k\pi})\xrightarrow[k\to\infty]{}2k\pi+0.$$
Donc $\ln N_k-2k\pi\to0$ et $\cos(\ln N_k)\to1$ : $T_{N_k}\to0$. De même avec $N'_k=\lfloor e^{(2k+1)\pi}\rfloor$ : $\cos(\ln N'_k)\to-1$, donc $T_{N'_k}\to2$. Deux sous-suites ont des limites différentes : $(T_N)$ n'a pas de limite, la série des intégrales diverge.

**Conclusion.** D'après la question 1, $\displaystyle\sum_{n\ge1}\frac{\sin(\ln n)}n$ **diverge** (ses sommes partielles oscillent, à une constante près, comme $1-\cos(\ln N)$).
"""

D['m-ccmp-04a'] = r"""
**Calcul des premiers termes (pour deviner).** $a_1=a_0^2=1$, $a_2=a_0a_1+a_1a_0=2$, $a_3=a_0a_2+a_1^2+a_2a_0=5$, $a_4=2\cdot5+2\cdot1\cdot2+\dots=14$. On reconnaît $1,1,2,5,14$ : les nombres de Catalan.

**Heuristique : la série génératrice.** Si $A(x)=\sum a_nx^n$ a un rayon $R>0$, alors pour $|x|<R$, le produit de Cauchy donne $A(x)^2=\sum_n\big(\sum_{k=0}^na_ka_{n-k}\big)x^n=\sum_na_{n+1}x^n$, d'où
$$xA(x)^2=\sum_{n\ge0}a_{n+1}x^{n+1}=A(x)-a_0=A(x)-1.$$
Pour $x\ne0$, $A$ est racine de $xA^2-A+1=0$, donc $A(x)=\frac{1\pm\sqrt{1-4x}}{2x}$. Comme $A$ est continue en 0 avec $A(0)=1$, il faut le signe $-$ (avec $+$, la fraction tend vers l'infini en 0). On évite de justifier $R>0$ a priori en raisonnant à l'envers.

**Développement de $B(x)=\dfrac{1-\sqrt{1-4x}}{2x}$.** Pour $|u|<1$, $(1+u)^{1/2}=\sum_{n\ge0}\binom{1/2}nu^n$, avec, pour $n\ge1$,
$$\binom{1/2}n=\frac{\frac12\left(\frac12-1\right)\cdots\left(\frac12-n+1\right)}{n!}=\frac{(-1)^{n-1}}{2^n\,n!}\cdot1\cdot3\cdots(2n-3).$$
Or $1\cdot3\cdots(2n-3)=\dfrac{(2n-2)!}{2\cdot4\cdots(2n-2)}=\dfrac{(2n-2)!}{2^{n-1}(n-1)!}$. Avec $u=-4x$, le terme $\binom{1/2}n(-4x)^n$ vaut donc
$$\frac{(-1)^{n-1}(-1)^n4^n}{2^n\,n!}\cdot\frac{(2n-2)!}{2^{n-1}(n-1)!}\,x^n=-\frac{2}{n}\binom{2n-2}{n-1}x^n.$$
Ainsi, pour $|x|<\frac14$, $1-\sqrt{1-4x}=\sum_{n\ge1}\frac2n\binom{2n-2}{n-1}x^n$, et en divisant par $2x$ (puis en posant $m=n-1$) :
$$B(x)=\sum_{m\ge0}\frac1{m+1}\binom{2m}{m}x^m,\qquad b_m=\frac1{m+1}\binom{2m}m,$$
de rayon $\frac14$ (prolongée par $B(0)=1=b_0$).

**$B$ vérifie l'équation et la récurrence.** Pour $0<|x|<\frac14$, posons $r=\sqrt{1-4x}$ ; alors $xB^2-B+1=\frac{(1-r)^2}{4x}-\frac{1-r}{2x}+1=\frac{(1-r)^2-2(1-r)+4x}{4x}=\frac{r^2-1+4x}{4x}=0$ car $r^2=1-4x$. Par continuité, $B=1+xB^2$ sur tout le disque. En identifiant les coefficients (produit de Cauchy dans le disque de convergence, unicité du développement) : $b_0=1$ et $b_{n+1}=\sum_{k=0}^nb_kb_{n-k}$.

**Conclusion.** $(a_n)$ et $(b_n)$ vérifient la même récurrence avec le même premier terme, donc (récurrence forte) $a_n=b_n$ pour tout $n$ :
$$a_n=\frac1{n+1}\binom{2n}n\qquad(1,1,2,5,14,42,\dots).$$
"""
