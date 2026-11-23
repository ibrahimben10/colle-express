D = {}

D['x-r-5'] = r"""
**Étape 1 : $M$ est diagonalisable à valeurs propres racines de l'unité.** Soit $M\in GL_n(\mathbb Z)$ avec $M^m=I_n$. Le polynôme $X^m-1$ annule $M$ ; ses racines $e^{2ik\pi/m}$ sont distinctes : il est scindé à racines simples sur $\mathbb C$. Donc $M$ est diagonalisable dans $\mathcal M_n(\mathbb C)$, et ses valeurs propres $\lambda_1,\dots,\lambda_n$ vérifient $\lambda_i^m=1$ : ce sont des racines de l'unité, de module 1.

**Étape 2 : coefficients du polynôme caractéristique.** $\chi_M=\prod_{i=1}^n(X-\lambda_i)=X^n-\sigma_1X^{n-1}+\sigma_2X^{n-2}-\dots+(-1)^n\sigma_n$, où $\sigma_k=\sum_{i_1<\dots<i_k}\lambda_{i_1}\cdots\lambda_{i_k}$. Chaque terme est de module 1, et il y a $\binom nk$ termes : $|\sigma_k|\le\binom nk$.

**Étape 3 : finitude.** $M$ est à coefficients entiers, donc $\chi_M=\det(XI_n-M)\in\mathbb Z[X]$ : les $\sigma_k$ sont des **entiers** de valeur absolue au plus $\binom nk$. Il n'y a donc qu'un nombre fini de polynômes caractéristiques possibles (au plus $\prod_k(2\binom nk+1)$), chacun ayant au plus $n$ racines. L'ensemble $\mathcal R$ des valeurs propres possibles (pour toutes les $M\in GL_n(\mathbb Z)$ d'ordre fini) est donc **fini**, et ne dépend que de $n$.

**Étape 4 : choix de $r$.** Chaque élément de $\mathcal R$ est une racine de l'unité, d'un certain ordre $d$. Soit $r$ le ppcm de ces ordres : $z^r=1$ pour tout $z\in\mathcal R$.

**Conclusion.** Pour $M$ d'ordre fini, $M=PDP^{-1}$ avec $D=\mathrm{diag}(\lambda_i)$, $\lambda_i\in\mathcal R$. Alors $D^r=\mathrm{diag}(\lambda_i^r)=I_n$ et $M^r=PD^rP^{-1}=I_n$.

**Précision.** Pour $n=2$, $\chi_M=X^2-tX\pm1$ avec $|t|\le2$, et l'on trouve que les ordres possibles sont $1,2,3,4,6$ : on peut prendre $r=12$.
"""

D['x-an-1'] = r"""
**1. Propriétés de $f$.** $f$ est continue, strictement croissante ($f'>0$), avec $f(0)=0$ et $f(x)\to+\infty$ : par le théorème de la bijection, $f$ réalise une bijection de $\mathbb R_+$ sur $\mathbb R_+$, et $f^{-1}$ est continue et strictement croissante.

**1. Identité.** Dans $\int_0^{f(a)}f^{-1}(t)\,\mathrm dt$, posons $t=f(u)$ : $u\mapsto f(u)$ est $C^1$ et croissante de $[0,a]$ sur $[0,f(a)]$, et $f^{-1}(f(u))=u$. Donc
$$\int_0^{f(a)}f^{-1}(t)\,\mathrm dt=\int_0^au\,f'(u)\,\mathrm du=\big[uf(u)\big]_0^a-\int_0^af(u)\,\mathrm du=af(a)-\int_0^af,$$
par intégration par parties. D'où $\int_0^af+\int_0^{f(a)}f^{-1}=af(a)$. (Interprétation : les deux aires remplissent le rectangle $[0,a]\times[0,f(a)]$.)

**1. Inégalité de Young.** Soient $a,b>0$ et $c=f^{-1}(b)$, de sorte que $f(c)=b$.
- **Cas $c\le a$.** Sur $[c,a]$, $f\ge f(c)=b$, donc $\int_c^af\ge(a-c)b$. Par l'identité appliquée en $c$ : $\int_0^bf^{-1}=\int_0^{f(c)}f^{-1}=cb-\int_0^cf$. Ainsi
$$\int_0^af+\int_0^bf^{-1}=\int_0^cf+\int_c^af+cb-\int_0^cf\ge(a-c)b+cb=ab.$$
- **Cas $c>a$**, c'est-à-dire $b>f(a)$. Sur $[f(a),b]$, $f^{-1}\ge f^{-1}(f(a))=a$, donc $\int_{f(a)}^bf^{-1}\ge a(b-f(a))$. Avec l'identité en $a$ :
$$\int_0^af+\int_0^bf^{-1}=\Big(\int_0^af+\int_0^{f(a)}f^{-1}\Big)+\int_{f(a)}^bf^{-1}\ge af(a)+a(b-f(a))=ab.$$
L'égalité a lieu si et seulement si $b=f(a)$. Exemple : $f(t)=t^{p-1}$ ($p>1$) donne $ab\le\frac{a^p}p+\frac{b^q}q$ avec $\frac1p+\frac1q=1$.

**2. Cas $f$ seulement continue.** Posons $F(c)=\int_0^cf+\int_0^{f(c)}f^{-1}-cf(c)$ pour $c\ge0$, et montrons $F\equiv0$. Soient $c\ge0$, $h>0$ et $\Delta=f(c+h)-f(c)>0$. Par croissance de $f$ sur $[c,c+h]$ et de $f^{-1}$ sur $[f(c),f(c+h)]$ :
$$hf(c)\le\int_c^{c+h}f\le hf(c+h)=hf(c)+h\Delta,\qquad c\Delta\le\int_{f(c)}^{f(c+h)}f^{-1}\le(c+h)\Delta.$$
Par ailleurs $(c+h)f(c+h)-cf(c)=(c+h)\Delta+hf(c)$. En faisant la différence :
$$F(c+h)-F(c)=\int_c^{c+h}f+\int_{f(c)}^{f(c+h)}f^{-1}-(c+h)\Delta-hf(c)\in\big[-h\Delta,\ h\Delta\big].$$
Comme $f$ est continue, $\Delta\to0$ quand $h\to0$ : $\frac{F(c+h)-F(c)}h\to0$. Le même calcul vaut à gauche. Donc $F$ est dérivable de dérivée nulle, et $F(0)=0$ : $F\equiv0$. L'identité est vraie, et la preuve de l'inégalité de la question 1 n'utilisait que l'identité et la monotonie : elle reste valable.
"""

D['x-an-2'] = r"""
**Relation de récurrence.** Pour $n\ge0$, écrivons $\cos^{n+2}=\cos^{n+1}\cdot\cos$ et intégrons par parties avec $u=\cos^{n+1}t$ ($u'=-(n+1)\cos^nt\sin t$) et $v=\sin t$ :
$$I_{n+2}=\big[\cos^{n+1}t\,\sin t\big]_0^{\pi/2}+(n+1)\int_0^{\pi/2}\cos^nt\,\sin^2t\,\mathrm dt.$$
Le crochet est nul ($\cos\frac\pi2=0$, $\sin0=0$). Avec $\sin^2=1-\cos^2$ : $I_{n+2}=(n+1)(I_n-I_{n+2})$, soit
$$I_{n+2}=\frac{n+1}{n+2}\,I_n.$$
Valeurs initiales : $I_0=\frac\pi2$, $I_1=\int_0^{\pi/2}\cos t\,\mathrm dt=1$.

**Un invariant.** Posons $u_n=(n+1)I_{n+1}I_n$. Alors
$$u_{n+1}=(n+2)I_{n+2}I_{n+1}=(n+2)\cdot\frac{n+1}{n+2}I_n\cdot I_{n+1}=(n+1)I_nI_{n+1}=u_n.$$
Donc $u_n=u_0=1\cdot I_1I_0=\frac\pi2$ pour tout $n$.

**$I_{n+1}\sim I_n$.** Sur $[0,\frac\pi2]$, $0\le\cos t\le1$, donc $\cos^{n+1}t\le\cos^nt$ et $(I_n)$ est décroissante ; elle est strictement positive (intégrale d'une fonction continue positive non nulle). Donc $I_{n+2}\le I_{n+1}\le I_n$, et en divisant par $I_n>0$ :
$$\frac{n+1}{n+2}=\frac{I_{n+2}}{I_n}\le\frac{I_{n+1}}{I_n}\le1.$$
Par encadrement, $\frac{I_{n+1}}{I_n}\to1$ : $I_{n+1}\sim I_n$.

**Équivalent.** $\frac\pi2=(n+1)I_{n+1}I_n\sim n\,I_n\cdot I_n=nI_n^2$. Donc $I_n^2\sim\frac\pi{2n}$, et comme $I_n>0$ :
$$I_n\sim\sqrt{\frac\pi{2n}}.$$

**Nature de $\sum I_n^2$.** $I_n^2\sim\frac\pi{2n}$, terme positif équivalent à celui de la série harmonique, divergente : par comparaison, $\sum I_n^2$ **diverge**. (En revanche $\sum I_n^3$ converge, car $I_n^3\sim\big(\frac\pi2\big)^{3/2}n^{-3/2}$.)
"""

D['x-an-3'] = r"""
**1. Réduction.** Posons $g_n=f-f_n$ : continue sur $[a,b]$, positive (une suite croissante qui converge est majorée par sa limite), décroissante en $n$, et $g_n\to0$ simplement. Il faut montrer $\|g_n\|_\infty\to0$. Comme $(\|g_n\|_\infty)$ est décroissante, il suffit de l'exclure de rester $\ge\varepsilon$.

**1. Raisonnement par l'absurde.** Supposons qu'il existe $\varepsilon>0$ tel que $\|g_n\|_\infty\ge\varepsilon$ pour tout $n$ ; $g_n$ est continue sur le segment, donc atteint son maximum : il existe $x_n\in[a,b]$ avec $g_n(x_n)\ge\varepsilon$. Par Bolzano-Weierstrass, une sous-suite $x_{\varphi(n)}$ converge vers un $x\in[a,b]$.

**1. Contradiction.** Fixons $m$. Pour $n$ assez grand, $\varphi(n)\ge m$, et par décroissance en l'indice : $g_m(x_{\varphi(n)})\ge g_{\varphi(n)}(x_{\varphi(n)})\ge\varepsilon$. Par continuité de $g_m$, en faisant $n\to\infty$ : $g_m(x)\ge\varepsilon$. Ceci pour tout $m$, ce qui contredit $g_m(x)\to0$. La convergence est donc uniforme (théorème de Dini).

**2. Propriétés de $f$.** Une limite simple de fonctions croissantes est croissante (les inégalités larges passent à la limite). $f$ est aussi continue sur le segment $[a,b]$, donc uniformément continue (Heine).

**2. Subdivision.** Soit $\varepsilon>0$. Par uniforme continuité, il existe une subdivision $a=t_0<t_1<\dots<t_p=b$ telle que $f(t_{k+1})-f(t_k)\le\varepsilon$ pour tout $k$. Par convergence simple en ces $p+1$ points (en nombre fini), il existe $N$ tel que pour $n\ge N$ et tout $k$ : $|f_n(t_k)-f(t_k)|\le\varepsilon$.

**2. Encadrement.** Soit $n\ge N$ et $x\in[t_k,t_{k+1}]$. Par croissance de $f_n$ puis de $f$ :
$$f_n(x)\le f_n(t_{k+1})\le f(t_{k+1})+\varepsilon\le f(t_k)+2\varepsilon\le f(x)+2\varepsilon,$$
$$f_n(x)\ge f_n(t_k)\ge f(t_k)-\varepsilon\ge f(t_{k+1})-2\varepsilon\ge f(x)-2\varepsilon.$$
Donc $\|f_n-f\|_\infty\le2\varepsilon$ pour $n\ge N$ : convergence uniforme (second théorème de Dini).

**3. Encadrement par récurrence.** Fixons $x\in[0,1]$ et notons $s=\sqrt x\in[0,1]$. On calcule
$$s-p_{n+1}=s-p_n-\frac{s^2-p_n^2}2=(s-p_n)\Big(1-\frac{s+p_n}2\Big).$$
Supposons $0\le p_n\le s$. Alors $0\le\frac{s+p_n}2\le s\le1$, donc le facteur $1-\frac{s+p_n}2\in[0,1]$, et $0\le s-p_{n+1}\le s-p_n$. De plus $p_{n+1}-p_n=\frac{s^2-p_n^2}2\ge0$. Comme $p_0=0\le s$, par récurrence : $0\le p_n\le p_{n+1}\le\sqrt x$ pour tout $n$.

**3. Limite simple.** La suite $(p_n(x))$ est croissante et majorée par $\sqrt x$ : elle converge vers $\ell\in[0,\sqrt x]$. En passant à la limite dans la relation : $\ell=\ell+\frac{x-\ell^2}2$, donc $\ell^2=x$ et $\ell=\sqrt x$.

**3. Conclusion.** Les $p_n$ sont des polynômes (par récurrence), donc continus ; la suite est croissante en $n$ et converge simplement vers $\sqrt{\cdot}$, continue sur $[0,1]$. Par la question 1 (Dini), $p_n\to\sqrt{\cdot}$ uniformément sur $[0,1]$. Application : $|t|=\sqrt{t^2}=\lim p_n(t^2)$ uniformément sur $[-1,1]$, étape clé d'une preuve du théorème de Weierstrass.
"""
