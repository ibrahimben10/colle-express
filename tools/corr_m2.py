
# Indices et corrigés — Maths CCMP (partie 2)
C = {}
def c(id, h1, h2, h3, corrige, reponse=""):
    C[id] = {"indices": [h1.strip(), h2.strip(), h3.strip()], "corrige": corrige.strip(), "reponse": reponse.strip()}

c("m-ccmp-15a",
r"Résous $Tu=\lambda u$ : c'est une suite géométrique indexée par $\mathbb Z$. À quelle condition est-elle bornée dans les deux sens ?",
r"Une suite croissante de sous-espaces d'un espace de dimension finie est stationnaire.",
r"Pour la 3, montre que $\ker(\tilde T-\lambda)^2=\ker(\tilde T-\lambda)$ : si $v=(T-\lambda)u$ est propre, écris $u_n$ explicitement et utilise la bornitude.",
r"""
**1.** $Tu=\lambda u\iff\forall n\in\mathbb Z,\ u_{n+1}=\lambda u_n$.
- Si $\lambda=0$ : $u_{n+1}=0$ pour tout $n$, donc $u=0$ : $0$ n'est pas valeur propre.
- Si $\lambda\ne0$ : $u_n=\lambda^nu_0$ pour tout $n\in\mathbb Z$. Cette suite est bornée en $+\infty$ ssi $|\lambda|\le1$ (ou $u_0=0$) et en $-\infty$ ssi $|\lambda|\ge1$.

Donc $\operatorname{Sp}(T)=\mathbb U=\{|\lambda|=1\}$, et le sous-espace propre associé à $\lambda$ est la droite engendrée par $(\lambda^n)_{n\in\mathbb Z}$.

**2.** Les $K_k=\ker(\tilde T-\lambda\,\mathrm{id})^k$ forment une suite croissante de sous-espaces de $E$, de dimension finie : la suite des dimensions, croissante et majorée par $\dim E$, est stationnaire, donc $(K_k)$ aussi.

**3.** $E$ est un $\mathbb C$-espace de dimension finie stable par $T$, donc (lemme des noyaux) $E=\bigoplus_i\ker(\tilde T-\lambda_i)^{m_i}$ où les $\lambda_i$ sont les valeurs propres de $\tilde T$, qui sont aussi valeurs propres de $T$ : $|\lambda_i|=1$.

Montrons $\ker(\tilde T-\lambda)^2=\ker(\tilde T-\lambda)$, ce qui entraîne par récurrence $\ker(\tilde T-\lambda)^k=\ker(\tilde T-\lambda)$. Soit $u$ avec $(T-\lambda)^2u=0$ et $v=(T-\lambda)u$. Alors $Tv=\lambda v$, donc $v_n=\lambda^nv_0$. La relation $u_{n+1}=\lambda u_n+\lambda^nv_0$ donne par récurrence
$$u_n=\lambda^n\Big(u_0+\frac{n\,v_0}{\lambda}\Big)\qquad(n\in\mathbb Z),$$
et $|u_n|=|u_0+nv_0/\lambda|$ : $u$ bornée impose $v_0=0$, donc $v=0$ et $u\in\ker(T-\lambda)$.

Ainsi $E=\bigoplus_{i=1}^r\ker(\tilde T-\lambda_i\,\mathrm{id})$ : $\tilde T$ est diagonalisable. Concrètement, $E$ est engendré par des suites $(\lambda_i^n)_n$ avec $|\lambda_i|=1$.
""", r"$\operatorname{Sp}T=\mathbb U$, vecteurs propres $(\lambda^n)_{n\in\mathbb Z}$ ; $\tilde T$ est diagonalisable.")

c("m-ccmp-15b",
r"Sens direct : si $a=\frac{x+y}2$ avec $x\ne a$, montre que $y\ne a$ et utilise la convexité de $A\setminus\{a\}$.",
r"Réciproque : par contraposée, si $A\setminus\{a\}$ n'est pas convexe, tu obtiens $x,y\ne a$ et $t\in]0,1[$ avec $a=(1-t)x+ty$.",
r"Quitte à échanger $x$ et $y$, $t\le\frac12$ : le point $y'=2a-x$ est sur le segment $[x,y]$, et $a=\frac{x+y'}2$.",
r"""
**($\Rightarrow$)** Supposons $A\setminus\{a\}$ convexe et $a=\frac12(x+y)$ avec $x,y\in A$. Si $x\ne a$, alors $y=2a-x\ne a$. Donc $x,y\in A\setminus\{a\}$ et leur milieu $a$ devrait appartenir à $A\setminus\{a\}$ : absurde. Donc $x=a$, puis $y=a$.

**($\Leftarrow$)** Par contraposée : supposons $A\setminus\{a\}$ non convexe. Il existe $x,y\in A\setminus\{a\}$ et $t\in]0,1[$ tels que $z=(1-t)x+ty\notin A\setminus\{a\}$. Comme $A$ est convexe, $z\in A$, donc $z=a$. Quitte à échanger $x$ et $y$ (et $t$ en $1-t$), on suppose $t\le\frac12$. Posons
$$y'=2a-x=x+2t(y-x).$$
Comme $2t\in]0,1]$, $y'\in[x,y]\subset A$. Alors $a=\frac12(x+y')$ avec $x\ne a$ : la propriété de droite est en défaut.

(Les notations $n,y$ de l'énoncé désignent $x,y$.)
""", r"Utiliser le symétrique $2a-x$, qui reste sur le segment $[x,y]$.")

c("m-ccmp-17a",
r"Les boules noires ne changent pas l'ordre relatif des rouges et des blanches : ne garde que les $a+c$ boules rouges et blanches.",
r"$Y=k$ signifie : dans l'ordre aléatoire des $a+c$ boules, les $k$ premières sont rouges et la $(k+1)$-ième est blanche.",
r"Pour l'espérance, écris $Y=\sum_{i=1}^a\mathbf 1_{R_i}$ où $R_i$ = « la rouge $i$ sort avant toutes les blanches ».",
r"""
On tire sans remise : l'ordre de sortie de toutes les boules est une permutation uniforme. Les boules noires n'interviennent pas : l'ordre relatif des $a$ rouges et des $c$ blanches est uniforme parmi les $\binom{a+c}{c}$ positions possibles des blanches. $Y$ est le nombre de rouges avant la première blanche.

**Loi.** $Y=k$ ($0\le k\le a$) signifie : les $k$ premières positions (parmi les $a+c$) sont rouges et la $(k+1)$-ième est blanche ; les $c-1$ autres blanches occupent alors $c-1$ des $a+c-k-1$ dernières positions :
$$P(Y=k)=\frac{\binom{a+c-k-1}{c-1}}{\binom{a+c}{c}},\qquad 0\le k\le a.$$

**Espérance.** Numérotons les rouges et posons $R_i$ : « la rouge $i$ sort avant toutes les blanches ». Parmi les $c+1$ boules {rouge $i$, blanches}, chacune a la même probabilité d'être la première : $P(R_i)=\frac1{c+1}$. Comme $Y=\sum_{i=1}^a\mathbf 1_{R_i}$,
$$E(Y)=\frac{a}{c+1}.$$
(Résultat indépendant de $b$ : les noires ne jouent aucun rôle.)
""", r"$P(Y=k)=\binom{a+c-k-1}{c-1}\big/\binom{a+c}{c}$, $E(Y)=\frac a{c+1}$.")

c("m-ccmp-17b",
r"Cherche $f$ sous la forme $f(x)=f(0)+\gamma\sqrt x+g(x)$ et choisis $\gamma$ pour que $g(x)-g(x/2)=o(\sqrt x)$.",
r"Il faut $\gamma\big(1-\frac1{\sqrt2}\big)=1$, soit $\gamma=2+\sqrt2$.",
r"Pour montrer $g(x)=o(\sqrt x)$, télescope $g(x)-g(x/2^N)=\sum_{k<N}\big(g(x/2^k)-g(x/2^{k+1})\big)$ et fais $N\to\infty$ (continuité en 0).",
r"""
Posons $\gamma=\dfrac1{1-1/\sqrt2}=\dfrac{\sqrt2}{\sqrt2-1}=2+\sqrt2$ et $g(x)=f(x)-f(0)-\gamma\sqrt x$. Alors $g$ est continue en $0$ avec $g(0)=0$, et
$$g(x)-g(x/2)=f(x)-f(x/2)-\gamma\Big(1-\frac1{\sqrt2}\Big)\sqrt x=f(x)-f(x/2)-\sqrt x=o(\sqrt x).$$

Soit $\varepsilon>0$ et $\delta>0$ tel que $|g(t)-g(t/2)|\le\varepsilon\sqrt t$ pour $0<t<\delta$. Pour $0<x<\delta$ et $N\ge1$ :
$$|g(x)-g(x/2^N)|\le\sum_{k=0}^{N-1}\varepsilon\sqrt{\frac x{2^k}}\le\varepsilon\sqrt x\sum_{k\ge0}2^{-k/2}=\gamma\,\varepsilon\sqrt x.$$
En faisant $N\to\infty$, $g(x/2^N)\to g(0)=0$ par continuité, d'où $|g(x)|\le\gamma\varepsilon\sqrt x$. Donc $g(x)=o(\sqrt x)$ et
$$f(x)=f(0)+(2+\sqrt2)\sqrt x+o(\sqrt x)\qquad(x\to0^+).$$
""", r"$f(x)=f(0)+(2+\sqrt2)\sqrt x+o(\sqrt x)$.")

c("m-ccmp-17c",
r"Si $A$ est inversible, écris $A=S^2$ avec $S=\sqrt A$ et compare $AB$ à $SBS$.",
r"$S^{-1}(AB)S=SBS$ est antisymétrique réelle : pourquoi est-elle diagonalisable sur $\mathbb C$ ?",
r"Teste le cas $A$ non inversible avec $A=\operatorname{diag}(1,0)$ et $B=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$.",
r"""
**Cas $A\in\mathcal S_n^{++}$.** Soit $S$ la racine carrée symétrique définie positive de $A$ ($A=PDP^T\Rightarrow S=P\sqrt DP^T$). Alors
$$S^{-1}(AB)S=S^{-1}S^2BS=SBS,$$
et $(SBS)^T=SB^TS=-SBS$ : $SBS$ est antisymétrique réelle. Donc $iSBS$ est hermitienne, diagonalisable (en base orthonormée) sur $\mathbb C$, et $SBS$ aussi. Ainsi $AB$, semblable à $SBS$, est diagonalisable sur $\mathbb C$, à valeurs propres imaginaires pures.

**Cas $A\in\mathcal S_n^+$ non inversible : le résultat est faux.** Avec $A=\begin{pmatrix}1&0\\0&0\end{pmatrix}\in\mathcal S_2^+$ et $B=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ :
$$AB=\begin{pmatrix}0&1\\0&0\end{pmatrix},$$
nilpotente non nulle, donc non diagonalisable.

À l'oral : énoncer le résultat pour $A\in\mathcal S_n^{++}$ et proposer ce contre-exemple montre une très bonne maîtrise. (On peut montrer que $AB$ est diagonalisable dès que $\ker(AB)=\ker\big((AB)^2\big)$.)
""", r"Vrai pour $A\in\mathcal S_n^{++}$ ($AB\sim SBS$ antisymétrique) ; faux en général (contre-exemple $2\times2$).")

c("m-ccmp-19a",
r"Commence par le lemme : une matrice de trace nulle est semblable à une matrice à diagonale nulle. Si $A$ n'est pas scalaire, il existe $x$ tel que $(x,Ax)$ soit libre.",
r"Dans une base commençant par $x,Ax$, la première colonne est $(0,1,0,\dots)^T$ : raisonne par récurrence sur le bloc inférieur, de trace nulle.",
r"Une matrice à diagonale nulle est somme d'une triangulaire supérieure stricte et d'une triangulaire inférieure stricte. Pour la 2, compare les traces de $A$ et $-A$, et teste $\operatorname{diag}(1,1,-2)$.",
r"""
**Lemme : si $\operatorname{Tr}A=0$, $A$ est semblable à une matrice à diagonale nulle.** Récurrence sur $n$ ; $n=1$ : $A=0$. Si $A$ est scalaire, $A=\lambda I_n$ avec $n\lambda=0$, donc $A=0$. Sinon il existe $x$ avec $(x,Ax)$ libre (sinon tout vecteur est propre et $A$ est scalaire). Dans une base $(x,Ax,e_3,\dots)$,
$$A\sim\begin{pmatrix}0&L\\C&A'\end{pmatrix},\quad C=(1,0,\dots,0)^T,\quad\operatorname{Tr}A'=0.$$
Par hypothèse de récurrence, $A'=QD'Q^{-1}$ avec $D'$ à diagonale nulle, et la conjugaison par $\operatorname{diag}(1,Q)$ donne une matrice à diagonale nulle.

**1.** Si $A=PMP^{-1}$ avec $M$ à diagonale nulle, $M=M_++M_-$ (parties strictement triangulaires supérieure et inférieure, nilpotentes), donc $A=PM_+P^{-1}+PM_-P^{-1}$ est somme de deux nilpotentes. (On a démontré la seconde affirmation d'abord.)

**2.** Si $A\sim-A$, alors $\operatorname{Tr}A=\operatorname{Tr}(-A)=-\operatorname{Tr}A$, donc $\operatorname{Tr}A=0$. La réciproque est **fausse** : $A=\operatorname{diag}(1,1,-2)$ est de trace nulle mais $\operatorname{Sp}(-A)=\{-1,2\}\ne\operatorname{Sp}(A)$. (Elle est vraie pour $n=2$ : $\chi_A=X^2+\det A=\chi_{-A}$.)
""", r"Trace nulle $\Rightarrow$ diagonale nulle à similitude près $\Rightarrow$ somme de deux nilpotentes.")

c("m-ccmp-19b",
r"Pour quelles valeurs de $x$ la quantité $1+tx$ reste-t-elle positive pour tout $t\ge1$ ? Étudie ensuite le comportement en $+\infty$.",
r"Le cas $x=0$ donne $\int_1^\infty\frac{dt}t$ : diverge. Pour $x>0$, l'intégrande est équivalent à $\frac1{\sqrt x\,t^{3/2}}$.",
r"Pour le calcul, pose $u=\sqrt{1+tx}$ : l'intégrale devient $\int\frac{2\,du}{u^2-1}$.",
r"""
**1. Domaine.** Si $x<0$, $1+tx<0$ pour $t>-1/x$ : l'intégrande n'est pas défini sur tout $[1,+\infty[$. Si $x=0$, $\int_1^\infty\frac{dt}t$ diverge. Si $x>0$, l'intégrande est continu, positif, équivalent en $+\infty$ à $\frac1{\sqrt x\,t^{3/2}}$ : intégrable. Donc $\mathcal D_f=]0,+\infty[$.

**2. Calcul.** Pour $x>0$, posons $u=\sqrt{1+tx}$ (changement de variable $\mathcal C^1$ strictement croissant) : $t=\frac{u^2-1}x$, $dt=\frac{2u}x\,du$, et
$$\frac{dt}{t\sqrt{1+tx}}=\frac{2u\,du/x}{\frac{u^2-1}x\,u}=\frac{2\,du}{u^2-1}=\Big(\frac1{u-1}-\frac1{u+1}\Big)du.$$
Donc
$$f(x)=\Big[\ln\frac{u-1}{u+1}\Big]_{\sqrt{1+x}}^{+\infty}=\ln\frac{\sqrt{1+x}+1}{\sqrt{1+x}-1}=2\ln\frac{1+\sqrt{1+x}}{\sqrt x}.$$
(En multipliant par la quantité conjuguée : $\frac{\sqrt{1+x}+1}{\sqrt{1+x}-1}=\frac{(\sqrt{1+x}+1)^2}x$.)

*Contrôles* : $f(x)\to+\infty$ quand $x\to0^+$ (cohérent avec la divergence en $x=0$) et $f(x)\sim\frac2{\sqrt x}$ en $+\infty$.
""", r"$\mathcal D_f=]0,+\infty[$, $f(x)=2\ln\frac{1+\sqrt{1+x}}{\sqrt x}$.")

c("m-ccmp-20a",
r"Pour $x>0$, c'est une série alternée : vérifie les hypothèses du critère spécial.",
r"Pour le caractère $\mathcal C^\infty$ sur $[a,+\infty[$, la série dérivée $k$-ième est encore alternée à partir d'un rang indépendant de $x$ : majore le reste uniformément.",
r"Pour la limite en $0^+$, écris $2g(x)=1+\sum_{n\ge1}(-1)^{n-1}\big(n^{-x}-(n+1)^{-x}\big)$ et majore cette nouvelle série alternée.",
r"""
**1.** Pour $x>0$, $(n^{-x})$ décroît vers $0$ : par le critère spécial des séries alternées, $g(x)$ est bien défini.

*Classe $\mathcal C^\infty$.* Les fonctions $u_n(x)=(-1)^{n-1}e^{-x\ln n}$ sont $\mathcal C^\infty$ avec $u_n^{(k)}(x)=(-1)^{n-1}(-\ln n)^kn^{-x}$. Fixons $a>0$ et $k\ge0$. La fonction $t\mapsto(\ln t)^kt^{-x}$ est décroissante pour $\ln t\ge k/x$, donc pour $t\ge e^{k/a}$ quel que soit $x\ge a$. Pour $N\ge e^{k/a}$, le reste de la série alternée $\sum u_n^{(k)}(x)$ vérifie
$$\Big|\sum_{n>N}u_n^{(k)}(x)\Big|\le\frac{(\ln(N+1))^k}{(N+1)^x}\le\frac{(\ln(N+1))^k}{(N+1)^a}\xrightarrow[N\to\infty]{}0,$$
uniformément sur $[a,+\infty[$. Toutes les séries dérivées convergent uniformément sur $[a,+\infty[$ : $g$ est $\mathcal C^\infty$ sur $[a,+\infty[$ pour tout $a>0$, donc sur $]0,+\infty[$.

**2.** Notons $a_n=n^{-x}$. On a $\sum_{n\ge1}(-1)^{n-1}(a_n-a_{n+1})=a_1-2a_2+2a_3-\dots=2g(x)-a_1$, donc
$$2g(x)=1+h(x),\qquad h(x)=\sum_{n\ge1}(-1)^{n-1}d_n,\quad d_n=n^{-x}-(n+1)^{-x}=x\int_n^{n+1}t^{-x-1}dt.$$
La suite $(d_n)$ est positive et décroissante (l'intégrande décroît) : par le critère spécial, $0\le h(x)\le d_1=1-2^{-x}\xrightarrow[x\to0^+]{}0$. Donc
$$\lim_{x\to0^+}g(x)=\frac12.$$
""", r"$g\in\mathcal C^\infty(]0,+\infty[)$ et $g(x)\to\frac12$ en $0^+$.")

c("m-ccmp-20b",
r"Si $\lambda$ est valeur propre de $A$, alors $P(\lambda)=0$ et $P'(\lambda)$ est valeur propre de $P'(A)$.",
r"Si $P'(A)$ est inversible, chaque valeur propre est racine **simple** de $P$ ; que dire alors du polynôme minimal de $A$ (qui divise $P$) ?",
r"Pour la réciproque, teste $A=I_n$ avec $P=(X-1)^2$. Puis examine le cas $P=\mu_A$.",
r"""
**1.** Si $AX=\lambda X$, alors $P(\lambda)X=P(A)X=0$ donc $P(\lambda)=0$, et $P'(A)X=P'(\lambda)X$ : $P'(\lambda)$ est valeur propre de $P'(A)$. Si $P'(A)$ est inversible, $P'(\lambda)\ne0$ : toute valeur propre de $A$ est racine simple de $P$.

Le polynôme minimal $\mu_A$ divise $P$ et ses racines sont exactement les valeurs propres de $A$. Chaque racine $\lambda$ de $\mu_A$ est de multiplicité $\le$ sa multiplicité dans $P$, soit $1$. Donc $\mu_A$ est scindé (on est sur $\mathbb C$) à racines simples : $A$ est diagonalisable.

**2.** La réciproque est **fausse** pour un annulateur quelconque : $A=I_n$ est diagonalisable, annulée par $P=(X-1)^2$, mais $P'(A)=2(A-I_n)=0$ n'est pas inversible.

Elle est **vraie** si $P=\mu_A$ : si $A=Q\operatorname{diag}(\lambda_i)Q^{-1}$ est diagonalisable, $\mu_A=\prod_{\lambda\in\operatorname{Sp}A}(X-\lambda)$ est à racines simples, donc $\mu_A'(\lambda)\ne0$ pour chaque valeur propre, et $\mu_A'(A)=Q\operatorname{diag}(\mu_A'(\lambda_i))Q^{-1}$ est inversible.

(L'énoncé d'origine, « $A$ diagonalisable $\iff P'(A)$ inversible », est donc vrai lorsque $P$ est à racines simples ou égal à $\mu_A$.)
""", r"$P'(A)$ inversible $\Rightarrow A$ diagonalisable ; réciproque vraie si $P=\mu_A$, fausse en général.")

c("m-ccmp-21b",
r"Si les boules se rencontrent en $x$, utilise l'inégalité triangulaire. Réciproquement, cherche un point d'intersection sur le segment $[c_1,c_2]$.",
r"Pour les boules : $\|c_1-c_2\|\le r_1+r_2$. Pour les sphères, il faut en plus éviter qu'une sphère soit « à l'intérieur » de l'autre.",
r"Pour construire un point commun aux sphères, travaille dans un plan contenant $c_1,c_2$ (c'est là que sert $n\ge2$) et cherche $x=c_1+\alpha u+\beta v$.",
r"""
Notons $d=\|c_1-c_2\|$.

**1. Boules.** Si $x\in B_f(c_1,r_1)\cap B_f(c_2,r_2)$, alors $d\le\|c_1-x\|+\|x-c_2\|\le r_1+r_2$. Réciproquement si $d\le r_1+r_2$ : si $d=0$, $c_1$ convient ; sinon le point $x=c_1+\frac{r_1}{r_1+r_2}(c_2-c_1)$ vérifie $\|x-c_1\|=\frac{r_1d}{r_1+r_2}\le r_1$ et $\|x-c_2\|=\frac{r_2d}{r_1+r_2}\le r_2$. (Si $r_1=r_2=0$, $d=0$.)

**CNS : $\|c_1-c_2\|\le r_1+r_2$.**

**2. Sphères.** Si $x\in S(c_1,r_1)\cap S(c_2,r_2)$, l'inégalité triangulaire donne $|r_1-r_2|\le d\le r_1+r_2$.

Réciproquement, supposons $|r_1-r_2|\le d\le r_1+r_2$. Si $d=0$, alors $r_1=r_2$ et les sphères sont égales (non vides). Sinon soit $u=\frac{c_2-c_1}d$ et $v$ unitaire orthogonal à $u$ (possible car $n\ge2$). On cherche $x=c_1+\alpha u+\beta v$ avec
$$\alpha^2+\beta^2=r_1^2,\qquad(\alpha-d)^2+\beta^2=r_2^2.$$
On trouve $\alpha=\frac{d^2+r_1^2-r_2^2}{2d}$, et il faut $\alpha^2\le r_1^2$, soit $|d^2+r_1^2-r_2^2|\le2dr_1$, c'est-à-dire $(d-r_1)^2\le r_2^2\le(d+r_1)^2$, équivalent à $|r_1-r_2|\le d\le r_1+r_2$. On prend alors $\beta=\sqrt{r_1^2-\alpha^2}$.

**CNS : $|r_1-r_2|\le\|c_1-c_2\|\le r_1+r_2$.**
""", r"Boules : $d\le r_1+r_2$. Sphères : $|r_1-r_2|\le d\le r_1+r_2$.")

c("m-ccmp-24b",
r"Une matrice nilpotente a toutes ses valeurs propres nulles : que vaut $\operatorname{Tr}(N^2)$ ?",
r"Que vaut $\operatorname{Tr}(S^2)$ pour $S$ symétrique réelle non nulle ? Déduis-en $F\cap\mathcal S_n(\mathbb R)=\{0\}$.",
r"Utilise $\dim F+\dim\mathcal S_n\le n^2$. Pour l'égalité, pense aux matrices triangulaires supérieures strictes.",
r"""
**Majoration.** Si $N\in F$ est nilpotente, $N^2$ l'est aussi et $\operatorname{Tr}(N^2)=0$ (somme des valeurs propres, toutes nulles). Si $S\in\mathcal S_n(\mathbb R)$ est non nulle, $\operatorname{Tr}(S^2)=\operatorname{Tr}(S^TS)=\sum_{i,j}s_{ij}^2>0$. Donc aucune matrice symétrique non nulle n'appartient à $F$ :
$$F\cap\mathcal S_n(\mathbb R)=\{0\}.$$
$F$ et $\mathcal S_n(\mathbb R)$ sont en somme directe dans $\mathcal M_n(\mathbb R)$ :
$$\dim F\le n^2-\dim\mathcal S_n(\mathbb R)=n^2-\frac{n(n+1)}2=\frac{n(n-1)}2.$$

**Égalité.** L'espace $\mathcal T_n^{++}$ des matrices triangulaires supérieures strictes est formé de matrices nilpotentes et a pour dimension $\frac{n(n-1)}2$.

*Remarque :* il n'est pas nécessaire que $F$ soit stable par produit ; seul compte que chaque élément soit nilpotent. C'est le théorème de Gerstenhaber (valable sur tout corps), dont la preuve générale est plus difficile.
""", r"$F\cap\mathcal S_n=\{0\}$ donc $\dim F\le\frac{n(n-1)}2$, égalité pour les triangulaires strictes.")

c("m-ccmp-25a",
r"Au voisinage de $0$ et de $1$, $f(t)=O(t)$ et $f(t)=O(1-t)$ : cela compense les singularités de $\cot(\pi t)$.",
r"Remarque que $\frac{1+\tan^2}{\tan^2}=\frac1{\sin^2}$, puis intègre $I_1$ par parties en écrivant $ff'=\frac12(f^2)'$. Tu dois trouver $I_1=\frac\pi2I_2$.",
r"Développe $\int_0^1\big(f'-\pi f\cot(\pi t)\big)^2dt\ge0$ et utilise $\cot^2=\frac1{\sin^2}-1$.",
r"""
**1.** Comme $f(0)=f(1)=0$ et $f\in\mathcal C^1$, on a $|f(t)|\le\|f'\|_\infty\min(t,1-t)$. Au voisinage de $0$, $|\cot(\pi t)|\sim\frac1{\pi t}$, donc $|ff'\cot(\pi t)|\le\frac{C}{\pi}$ : $I_1$ converge (de même en $1$). Ensuite $\frac{1+\tan^2(\pi t)}{\tan^2(\pi t)}=\frac1{\sin^2(\pi t)}$, donc $I_2=\int_0^1\frac{f(t)^2}{\sin^2(\pi t)}dt$, et $\frac{f^2}{\sin^2(\pi t)}$ est borné ($\sin(\pi t)\ge2\min(t,1-t)$) : $I_2$ converge.

Intégration par parties sur $[\varepsilon,1-\varepsilon]$, avec $(\cot)'=-\frac1{\sin^2}$ :
$$\int_\varepsilon^{1-\varepsilon}ff'\cot(\pi t)\,dt=\Big[\frac{f^2}2\cot(\pi t)\Big]_\varepsilon^{1-\varepsilon}+\frac\pi2\int_\varepsilon^{1-\varepsilon}\frac{f^2}{\sin^2(\pi t)}dt.$$
Le crochet tend vers $0$ ($f^2=O(t^2)$ et $\cot=O(1/t)$). Donc
$$I_1=\frac\pi2\,I_2.$$

**2.** Comme $\big(f'-\pi f\cot(\pi t)\big)^2\ge0$ est intégrable,
$$0\le\int_0^1f'^2-2\pi I_1+\pi^2\int_0^1f^2\cot^2(\pi t)=\int_0^1f'^2-\pi^2I_2+\pi^2\int_0^1f^2\Big(\frac1{\sin^2(\pi t)}-1\Big)=\int_0^1f'^2-\pi^2\int_0^1f^2.$$
D'où l'**inégalité de Wirtinger** : $\displaystyle\int_0^1f'^2\ge\pi^2\int_0^1f^2$.

**3. Égalité** $\iff f'=\pi f\cot(\pi t)$ sur $]0,1[$ (fonction continue positive d'intégrale nulle). Sur $]0,1[$, cela équivaut à $\big(f/\sin(\pi t)\big)'=0$, soit $f=\lambda\sin(\pi t)$. Réciproquement ces fonctions réalisent l'égalité ($\int\pi^2\cos^2=\pi^2\int\sin^2$).
""", r"$I_1=\frac\pi2I_2$ ; $\int_0^1f'^2\ge\pi^2\int_0^1f^2$, égalité ssi $f=\lambda\sin(\pi t)$.")

c("m-ccmp-26a",
r"Écris $\sin(2n\theta)=\operatorname{Im}\big((\cos\theta+i\sin\theta)^{2n}\big)$ avec le binôme : seuls les termes impairs en $\sin\theta$ interviennent.",
r"Les racines de $P$ sont les $\cos\frac{k\pi}{2n}$, $1\le k\le2n-1$ ; elles vont par paires opposées, et $k=n$ donne la racine $0$.",
r"Écris $P=2^{2n-1}X\prod_{k=1}^{n-1}(X^2-c_k^2)$ et calcule $P'(0)$ de deux manières (la seconde en dérivant $\frac{\sin(2n\theta)}{\sin\theta}$ en $\theta=\frac\pi2$).",
r"""
**1.** Par la formule du binôme,
$$\sin(2n\theta)=\operatorname{Im}(\cos\theta+i\sin\theta)^{2n}=\sum_{j\ \mathrm{impair}}\binom{2n}{j}(-1)^{\frac{j-1}2}\cos^{2n-j}\theta\,\sin^j\theta.$$
Chaque terme contient $\sin\theta\cdot(\sin^2\theta)^{\frac{j-1}2}=\sin\theta(1-\cos^2\theta)^{\frac{j-1}2}$ : donc $\sin(2n\theta)=\sin\theta\,P(\cos\theta)$ avec
$$P=\sum_{j\ \mathrm{impair}}\binom{2n}j(-1)^{\frac{j-1}2}X^{2n-j}(1-X^2)^{\frac{j-1}2}.$$

**2.** Chaque terme est de degré $2n-1$, avec coefficient de $X^{2n-1}$ égal à $\binom{2n}j(-1)^{\frac{j-1}2}(-1)^{\frac{j-1}2}=\binom{2n}j$. Donc $\deg P=2n-1$ et le coefficient dominant vaut $\sum_{j\ \mathrm{impair}}\binom{2n}j=2^{2n-1}$. Terme constant : $P(0)=\frac{\sin(2n\cdot\pi/2)}{\sin(\pi/2)}=\sin(n\pi)=0$.

**3.** $\sin(2n\theta)=0\iff\theta=\frac{k\pi}{2n}$. Pour $\theta_k=\frac{k\pi}{2n}$, $1\le k\le2n-1$, on a $\sin\theta_k\ne0$, donc $P(\cos\theta_k)=0$. Ces $2n-1$ réels $\cos\theta_k$ sont distincts ($\cos$ injectif sur $]0,\pi[$) : ce sont toutes les racines de $P$.

**4.** Posons $c_k=\cos\frac{k\pi}{2n}$ ; $c_{2n-k}=-c_k$ et $c_n=0$. Donc $P=2^{2n-1}X\prod_{k=1}^{n-1}(X^2-c_k^2)$ et $P'(0)=2^{2n-1}(-1)^{n-1}\prod_{k=1}^{n-1}c_k^2$.
D'autre part, en dérivant $P(\cos\theta)=\frac{\sin2n\theta}{\sin\theta}$ en $\theta=\frac\pi2$ : $-P'(0)=2n\cos(n\pi)=2n(-1)^n$, soit $P'(0)=2n(-1)^{n-1}$. D'où $\prod c_k^2=\frac{2n}{2^{2n-1}}=\frac{n}{4^{n-1}}$ et, les $c_k$ étant positifs :
$$\prod_{k=1}^{n-1}\cos\frac{k\pi}{2n}=\frac{\sqrt n}{2^{n-1}}.$$
(Vérification $n=2$ : $\cos\frac\pi4=\frac{\sqrt2}2$.)
""", r"$\deg P=2n-1$, coefficient dominant $2^{2n-1}$, $P(0)=0$ ; $\prod_{k=1}^{n-1}\cos\frac{k\pi}{2n}=\frac{\sqrt n}{2^{n-1}}$.")

c("m-ccmp-27a",
r"Ramène-toi à une variable : pour chaque $i$, étudie $\varphi_i(t)=f(a+te_i)$.",
r"$\varphi_i$ admet un minimum local en $0$, donc $\varphi_i'(0)=0$. Que dire de $\varphi_i''(0)$ ?",
r"Si $\varphi_i''(0)<0$, la formule de Taylor-Young donne $\varphi_i(t)<\varphi_i(0)$ pour $t$ petit non nul.",
r"""
Soit $i\in\{1,\dots,m\}$. Comme $\Omega$ est ouvert, $\varphi_i(t)=f(a+te_i)$ est définie et de classe $\mathcal C^2$ au voisinage de $0$, avec $\varphi_i'(0)=\partial_if(a)$ et $\varphi_i''(0)=\partial_{i}^2f(a)$.

$\varphi_i$ admet un minimum local en $0$, intérieur : $\varphi_i'(0)=0$. Par Taylor-Young,
$$\varphi_i(t)=\varphi_i(0)+\frac{\varphi_i''(0)}2t^2+o(t^2).$$
Si $\varphi_i''(0)<0$, on aurait $\varphi_i(t)<\varphi_i(0)$ pour $t\ne0$ assez petit, ce qui contredit le minimum. Donc $\partial_i^2f(a)\ge0$ pour tout $i$, et
$$\Delta f(a)=\sum_{i=1}^m\partial_i^2f(a)\ge0.$$

*Prolongement classique :* une fonction $\mathcal C^2$ vérifiant $\Delta f<0$ sur $\Omega$ n'a pas de minimum local dans $\Omega$ (principe du minimum pour les fonctions sur-harmoniques strictes).
""", r"$\partial_i^2f(a)\ge0$ pour tout $i$ (restriction aux droites), donc $\Delta f(a)\ge0$.")

c("m-ccmp-27b",
r"Une inclusion est facile : si $u(x)=\lambda x$, que vaut $p(u)(x)$ ?",
r"Pour l'autre, soit $\mu$ valeur propre de $p(u)$. Factorise $p(X)-\mu$ sur $\mathbb C$.",
r"$p(u)-\mu\,\mathrm{id}=c\prod_j(u-\alpha_j\mathrm{id})$ n'est pas injectif : l'un des facteurs ne l'est pas.",
r"""
Montrons $\operatorname{Sp}(p(u))=p(\operatorname{Sp}u)=\{p(\lambda):\lambda\in\operatorname{Sp}u\}$.

**($\supset$)** Si $u(x)=\lambda x$ avec $x\ne0$, alors $u^k(x)=\lambda^kx$ et $p(u)(x)=p(\lambda)x$ : $p(\lambda)\in\operatorname{Sp}(p(u))$.

**($\subset$)** Soit $\mu\in\operatorname{Sp}(p(u))$. Si $p$ est constant égal à $c$, $p(u)=c\,\mathrm{id}$, $\mu=c=p(\lambda)$ pour n'importe quel $\lambda\in\operatorname{Sp}u$ (non vide en dimension finie sur $\mathbb C$). Sinon, $\mathbb C$ étant algébriquement clos, $p(X)-\mu=c\prod_{j=1}^d(X-\alpha_j)$ avec $c\ne0$. Alors
$$p(u)-\mu\,\mathrm{id}=c\,(u-\alpha_1\mathrm{id})\circ\dots\circ(u-\alpha_d\mathrm{id})$$
n'est pas injectif ; une composée d'injections étant injective, l'un des $u-\alpha_j\mathrm{id}$ n'est pas injectif : $\alpha_j\in\operatorname{Sp}u$ et $p(\alpha_j)=\mu$.

*Remarque :* sur $\mathbb R$ l'inclusion $\subset$ peut tomber en défaut (rotation d'angle $\pi/2$ : $\operatorname{Sp}u=\emptyset$ mais $u^2=-\mathrm{id}$).
""", r"$\operatorname{Sp}(p(u))=p(\operatorname{Sp}u)$.")

c("m-ccmp-27c",
r"Compare les variables aléatoires $\mathbf 1_{\{X\ge a\}}$ et $\frac{h(X)}{h(a)}$.",
r"Si $X(\omega)\ge a$, la croissance de $h$ donne $h(X(\omega))\ge h(a)$ ; sinon l'indicatrice est nulle et $h>0$.",
r"Prends l'espérance (croissance de l'espérance). Pourquoi $E(h(X))$ existe-t-il ?",
r"""
Comme $X$ est bornée, disons $|X|\le M$, et $h$ croissante, $0<h(X)\le h(M)$ : $h(X)$ est bornée, donc d'espérance finie.

Montrons l'inégalité ponctuelle $\mathbf 1_{\{X\ge a\}}\le\dfrac{h(X)}{h(a)}$ :
- si $X(\omega)\ge a$ : $h(X(\omega))\ge h(a)>0$, donc $\frac{h(X(\omega))}{h(a)}\ge1$ ;
- sinon : $\mathbf 1_{\{X\ge a\}}(\omega)=0<\frac{h(X(\omega))}{h(a)}$.

Par croissance de l'espérance :
$$P(X\ge a)=E\big(\mathbf 1_{\{X\ge a\}}\big)\le\frac{E(h(X))}{h(a)}.$$

*Cas particuliers :* $h(x)=e^{tx}$ ($t>0$) donne l'inégalité de Chernoff $P(X\ge a)\le e^{-ta}E(e^{tX})$ ; avec $h(x)=x$ sur $X\ge0$ on retrouve Markov.
""", r"$\mathbf 1_{\{X\ge a\}}\le h(X)/h(a)$, puis espérance.")

c("m-ccmp-28a",
r"Développe $p^2=\frac1{n^2}\sum_i\sum_jg_ig_j$ et utilise que $g\mapsto g_ig$ est une bijection de $G$.",
r"$p$ est un projecteur. Montre que $\operatorname{Im}p=\bigcap_i\ker(g_i-\mathrm{id})$ (vecteurs fixés par tout le groupe).",
r"Pour un projecteur, $\operatorname{rg}p=\operatorname{Tr}p$.",
r"""
Notons $p=\frac1n\sum_{i=1}^ng_i$.

**1.** Pour $i$ fixé, $j\mapsto g_ig_j$ est une bijection de $G$ (translation à gauche), donc $\sum_jg_ig_j=\sum_kg_k=np$. Ainsi
$$p^2=\frac1{n^2}\sum_i\sum_jg_ig_j=\frac1{n^2}\sum_inp=p.$$
$p$ est un projecteur.

**2.** Notons $F=\bigcap_i\ker(g_i-\mathrm{id})$ (vecteurs fixes). Montrons $\operatorname{Im}p=F$.
- Si $x\in F$, $p(x)=\frac1n\sum g_i(x)=x$, donc $x\in\operatorname{Im}p$.
- Si $x=p(y)$, alors $g_k(x)=\frac1n\sum_ig_kg_i(y)=p(y)=x$ pour tout $k$ (même argument de bijection) : $x\in F$.

Pour un projecteur, $\operatorname{rg}p=\operatorname{Tr}p$ (dans une base adaptée à $E=\operatorname{Im}p\oplus\ker p$, sa matrice est $\operatorname{diag}(I_r,0)$). Donc
$$\dim\bigcap_{i=1}^n\ker(g_i-\mathrm{id}_E)=\operatorname{Tr}p=\frac1n\sum_{i=1}^n\operatorname{tr}(g_i).$$
(C'est le point de départ de la théorie des caractères : la moyenne des traces compte les vecteurs invariants.)
""", r"$p^2=p$, $\operatorname{Im}p$ = vecteurs fixes, $\dim=\operatorname{Tr}p=\frac1n\sum\operatorname{tr}g_i$.")

c("m-ccmp-28b",
r"Domine l'intégrande pour $x>0$ et montre que $f$ est dérivable sur $[a,+\infty[$ ($a>0$).",
r"$f'(x)=-\int_0^\infty\sin t\,e^{-xt}dt=-\frac1{1+x^2}$. Trouve la constante grâce à la limite en $+\infty$.",
r"Pour la question 2, il faut la continuité de $f$ en $0$ : majore uniformément le reste $\int_A^\infty\frac{\sin t}te^{-xt}dt$ pour $x\ge0$ par une intégration par parties.",
r"""
**1.** Pour $x>0$, $\big|\frac{\sin t}te^{-xt}\big|\le e^{-xt}$, intégrable : $f$ est définie. Sur $[a,+\infty[$ ($a>0$), $\big|\partial_x\big(\frac{\sin t}te^{-xt}\big)\big|=|\sin t|e^{-xt}\le e^{-at}$ : par dérivation sous l'intégrale,
$$f'(x)=-\int_0^\infty\sin t\,e^{-xt}dt=-\operatorname{Im}\int_0^\infty e^{(-x+i)t}dt=-\operatorname{Im}\frac1{x-i}=-\frac1{1+x^2}.$$
Donc $f(x)=C-\arctan x$. Comme $|f(x)|\le\int_0^\infty e^{-xt}dt=\frac1x\to0$, $C=\frac\pi2$ :
$$f(x)=\frac\pi2-\arctan x.$$

**2.** L'intégrale $\int_0^\infty\frac{\sin t}tdt$ est semi-convergente ; il faut justifier $\lim_{x\to0^+}f(x)=f(0)$. Pour $x\ge0$ et $A>0$, posons $\varphi_x(t)=\frac{e^{-xt}}t$, positive et décroissante. Par intégration par parties,
$$\int_A^\infty\sin t\,\varphi_x(t)dt=\big[-\cos t\,\varphi_x\big]_A^\infty+\int_A^\infty\cos t\,\varphi_x'(t)dt,$$
d'où $\Big|\int_A^\infty\frac{\sin t}te^{-xt}dt\Big|\le\varphi_x(A)+\int_A^\infty|\varphi_x'|=2\varphi_x(A)\le\frac2A$, **uniformément** en $x\ge0$. Ainsi $f$ est limite uniforme sur $[0,+\infty[$ des fonctions continues $x\mapsto\int_0^A\frac{\sin t}te^{-xt}dt$ : $f$ est continue en $0$, et
$$\int_0^{+\infty}\frac{\sin t}t\,dt=\lim_{x\to0^+}\Big(\frac\pi2-\arctan x\Big)=\frac\pi2.$$
""", r"$f(x)=\frac\pi2-\arctan x$ ; $\int_0^\infty\frac{\sin t}tdt=\frac\pi2$.")
