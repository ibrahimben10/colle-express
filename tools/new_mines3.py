# Mathématiques — distributions (hors programme, définies dans l'énoncé) et exercices mêlant calcul différentiel et probabilités.
from newlib import ex, E

DEF = r"""**Cadre.** On note $\mathcal D$ l'ensemble des fonctions $\varphi:\mathbb R\to\mathbb R$ de classe $\mathcal C^\infty$ et nulles en dehors d'un segment (fonctions test). Une **distribution** est une forme linéaire $T:\mathcal D\to\mathbb R$ telle que, pour tout $a>0$, il existe $C\ge0$ et $k\in\mathbb N$ avec $|T(\varphi)|\le C\max_{j\le k}\|\varphi^{(j)}\|_\infty$ pour toute $\varphi\in\mathcal D$ nulle hors de $[-a,a]$. Exemples : pour $f$ continue par morceaux, $T_f(\varphi)=\int_{\mathbb R}f\varphi$ ; la masse de Dirac $\delta(\varphi)=\varphi(0)$. La **dérivée** de $T$ est la distribution $T'(\varphi)=-T(\varphi')$ (pour $f$ de classe $\mathcal C^1$, une intégration par parties donne $(T_f)'=T_{f'}$)."""

def dist():
    E[-1]['enonce'] = DEF + '\n\n' + E[-1]['enonce'] + "\n\n*Pour aller plus loin : notion hors programme, entièrement définie dans l'énoncé.*"
    E[-1]['concours'] = 'Ouverture'
    E[-1]['ajout'] = '2026-11-26'

def mp():
    E[-1]['enonce'] += "\n\n*Dans l'esprit des oraux Mines-Ponts.*"
    E[-1]['concours'] = 'Mines-Ponts'
    E[-1]['ajout'] = '2026-11-26'

# ------------------------------------------------------------ D1
ex('n-dist-heaviside', 'Maths', 'Distributions', 2, 'Dérivées de Heaviside, de |x| et masse de Dirac', 25, r"""
On note $H=\mathbb 1_{[0,+\infty[}$ (fonction de Heaviside).

1. Soit $g(x)=e^{-1/x}$ pour $x>0$ et $g(x)=0$ pour $x\le0$. On admet que $g$ est de classe $\mathcal C^\infty$. Vérifier que $\varphi_0(x)=g(1-x^2)$ appartient à $\mathcal D$ et que $\varphi_0(0)\ne0$.
2. Montrer que $(T_H)'=\delta$.
3. Calculer $(T_{|x|})'$ et $(T_{|x|})''$.
4. Montrer qu'il n'existe pas de fonction $f$ continue telle que $\delta=T_f$.
""", r"""Que vaut $-\int_{\mathbb R}H\varphi'$ ? Et si $\delta=T_f$ avec $f$ continue, que se passe-t-il quand on teste contre une fonction très concentrée près de $0$ ?""",
r"""Utilise la définition $T'(\varphi)=-T(\varphi')$ et le fait que $\varphi$ est nulle hors d'un segment. Pour 4, teste contre $\varphi_\varepsilon(x)=\varphi_0(x/\varepsilon)$ et change de variable.""",
r"""$\int f(x)\varphi_0(x/\varepsilon)\,\mathrm dx=\varepsilon\int f(\varepsilon u)\varphi_0(u)\,\mathrm du\to0$, alors que $\delta(\varphi_\varepsilon)=\varphi_0(0)=e^{-1}$. Pour $|x|$, découpe l'intégrale en $0$.""",
r"""**Étape 1 — Analyse de l'énoncé.** On dérive des fonctions non dérivables (sauts, points anguleux) au sens des distributions : le saut de $H$ produit une masse de Dirac, le point anguleux de $|x|$ en produit une à l'ordre 2. On montre enfin que $\delta$ n'est pas une « vraie » fonction.

**Étape 2 — Rappels du cours.**

> **Définition — Dérivée d'une distribution.** $T'(\varphi)=-T(\varphi')$ ; c'est la formule d'intégration par parties sans terme de bord, puisque $\varphi$ est nulle hors d'un segment.

> **Propriété — Changement de variable affine.** $\int_{\mathbb R}h(x/\varepsilon)\,\mathrm dx=\varepsilon\int_{\mathbb R}h(u)\,\mathrm du$ pour $\varepsilon>0$.

> **Théorème — Continuité d'une intégrale à paramètre** sur un segment fixe, avec une fonction continue en les deux variables.

**Étape 3 — Stratégie.** Calcul direct de $-\int H\varphi'$ et $-\int|x|\varphi'$ ; pour l'impossibilité, une famille de fonctions test qui se concentrent en $0$.

**Étape 4 — Résolution détaillée.**

**4.1 Une fonction test.** $x\mapsto1-x^2$ est $\mathcal C^\infty$ et $g$ aussi, donc $\varphi_0$ est $\mathcal C^\infty$. Si $|x|\ge1$, $1-x^2\le0$ et $\varphi_0(x)=0$ : $\varphi_0\in\mathcal D$, nulle hors de $[-1,1]$, et $\varphi_0(0)=e^{-1}\ne0$.

**4.2 Heaviside.** $T_H$ est bien une distribution : $|T_H(\varphi)|\le2a\|\varphi\|_\infty$ si $\varphi$ est nulle hors de $[-a,a]$. Soit $\varphi\in\mathcal D$ nulle hors de $[-a,a]$ :
$$(T_H)'(\varphi)=-\int_0^{+\infty}\varphi'(x)\,\mathrm dx=-\big(\varphi(a)-\varphi(0)\big)=\varphi(0)=\delta(\varphi).$$

**4.3 Valeur absolue.** Avec le même $\varphi$, en coupant en $0$ et en intégrant par parties sur chaque morceau :
$$(T_{|x|})'(\varphi)=-\int_{-a}^0(-x)\varphi'(x)\,\mathrm dx-\int_0^ax\,\varphi'(x)\,\mathrm dx=-\int_{-a}^0\varphi+\int_0^a\varphi=T_{\operatorname{sgn}}(\varphi),$$
(les termes de bord s'annulent : $x\varphi(x)$ est nul en $0$ et en $\pm a$). Puis $(T_{\operatorname{sgn}})'(\varphi)=\int_{-a}^0\varphi'-\int_0^a\varphi'=\varphi(0)+\varphi(0)=2\varphi(0)$, donc $(T_{|x|})''=2\delta$.

**4.4 $\delta$ n'est pas une fonction.** Supposons $\delta=T_f$ avec $f$ continue. Pour $\varepsilon\in\,]0,1]$, $\varphi_\varepsilon(x)=\varphi_0(x/\varepsilon)\in\mathcal D$ et
$$e^{-1}=\varphi_\varepsilon(0)=\int_{\mathbb R}f(x)\varphi_0(x/\varepsilon)\,\mathrm dx=\varepsilon\int_{-1}^1f(\varepsilon u)\varphi_0(u)\,\mathrm du.$$
L'intégrale $\int_{-1}^1f(\varepsilon u)\varphi_0(u)\,\mathrm du$ est bornée par $2\max_{[-1,1]}|f|\cdot\|\varphi_0\|_\infty$, donc le membre de droite tend vers $0$ quand $\varepsilon\to0$ : contradiction.

**Étape 5 — Vérification.**

> **Vérification — Cohérence avec le calcul usuel.** Hors de $0$, $|x|'=\operatorname{sgn}(x)$ et $\operatorname{sgn}'=0$ : la dérivée au sens des distributions ajoute seulement la contribution du point singulier, ici le saut de hauteur $2$ de $\operatorname{sgn}$, d'où $2\delta$ ✓.

**Étape 6 — Conclusion.**
$$\boxed{(T_H)'=\delta,\qquad(T_{|x|})'=T_{\operatorname{sgn}},\qquad(T_{|x|})''=2\delta,\qquad\delta\ne T_f\ (f\ \text{continue})}$$""",
r"""$-\int_0^\infty\varphi'=\varphi(0)$ donc $H'=\delta$ ; $|x|'=\operatorname{sgn}$ et $\operatorname{sgn}'=2\delta$ (saut de hauteur $2$) ; tester $\delta=T_f$ contre $\varphi_0(x/\varepsilon)$ donne $e^{-1}=O(\varepsilon)$, absurde.""")
dist()

# ------------------------------------------------------------ D2
ex('n-dist-equations', 'Maths', 'Distributions', 3, 'Équations T′ = 0, T′ = δ et xT = 0', 35, r"""
Pour une distribution $T$, on note $xT$ la distribution $\varphi\mapsto T(x\varphi)$, où $x\varphi$ désigne la fonction $x\mapsto x\varphi(x)$. On fixe $\theta\in\mathcal D$ telle que $\int_{\mathbb R}\theta=1$, et $\chi\in\mathcal D$ égale à $1$ sur $[-1,1]$ (on admet leur existence).

1. Soit $\varphi\in\mathcal D$ et $\rho=\varphi-\big(\int_{\mathbb R}\varphi\big)\theta$. Montrer que $\psi(x)=\int_{-\infty}^x\rho(t)\,\mathrm dt$ définit un élément de $\mathcal D$ tel que $\psi'=\rho$.
2. En déduire que si $T'=0$, alors il existe une constante $c$ telle que $T=T_c$.
3. Déterminer toutes les distributions $T$ telles que $T'=\delta$.
4. Soit $\varphi\in\mathcal D$ et $\sigma=\varphi-\varphi(0)\chi$. Montrer que $\sigma(x)=x\,\eta(x)$ avec $\eta\in\mathcal D$ (on pourra écrire $\sigma(x)=x\int_0^1\sigma'(tx)\,\mathrm dt$).
5. En déduire les distributions $T$ telles que $xT=0$.
""", r"""Pourquoi la primitive d'une fonction test n'est-elle pas, en général, une fonction test ? Que faut-il imposer à son intégrale totale ?""",
r"""Une fonction test d'intégrale nulle est la dérivée d'une fonction test. Avec $T'=0$, $T$ s'annule sur toutes ces dérivées : il ne reste qu'une direction, celle de $\theta$. Pour 5, une fonction test nulle en $0$ est de la forme $x\eta$.""",
r"""$T(\varphi)=T(\rho)+\big(\int\varphi\big)T(\theta)$ et $T(\rho)=T(\psi')=-T'(\psi)=0$. Pour 5 : $T(\varphi)=T(x\eta)+\varphi(0)T(\chi)$.""",
r"""**Étape 1 — Analyse de l'énoncé.** On résout les « équations différentielles » les plus simples dans les distributions. La méthode est toujours la même : décomposer une fonction test en une partie « facile » (dérivée, ou multiple de $x$) et une composante le long d'une fonction fixée.

**Étape 2 — Rappels du cours.**

> **Théorème fondamental de l'analyse.** Pour $\rho$ continue, $x\mapsto\int_{-\infty}^x\rho$ est une primitive de $\rho$ (ici l'intégrale porte sur un segment, car $\rho$ est nulle hors d'un segment).

> **Théorème — Dérivation sous l'intégrale (segment).** Si $h(t,x)$ est de classe $\mathcal C^\infty$ sur $[0,1]\times\mathbb R$, alors $x\mapsto\int_0^1h(t,x)\,\mathrm dt$ est $\mathcal C^\infty$.

**Étape 3 — Stratégie.** Primitives à support compact pour $T'=0$ ; solution particulière $T_H$ pour $T'=\delta$ ; lemme de division par $x$ pour $xT=0$.

**Étape 4 — Résolution détaillée.**

**4.1 Primitive à support compact.** $\rho$ est $\mathcal C^\infty$ et nulle hors d'un segment $[-a,a]$ contenant les supports de $\varphi$ et $\theta$, et $\int\rho=\int\varphi-\int\varphi\cdot1=0$. Donc $\psi$ est $\mathcal C^\infty$, $\psi'=\rho$, $\psi(x)=0$ pour $x\le-a$ et $\psi(x)=\int_{\mathbb R}\rho=0$ pour $x\ge a$ : $\psi\in\mathcal D$.

**4.2 $T'=0$.** Par linéarité, $T(\varphi)=T(\rho)+\big(\int\varphi\big)T(\theta)$, et $T(\rho)=T(\psi')=-T'(\psi)=0$. Avec $c=T(\theta)$ : $T(\varphi)=c\int\varphi=T_c(\varphi)$.

**4.3 $T'=\delta$.** $(T_H)'=\delta$ (calcul : $-\int_0^\infty\varphi'=\varphi(0)$). Si $T'=\delta$, $(T-T_H)'=0$, donc $T=T_H+T_c=T_{H+c}$. Réciproquement ces distributions conviennent.

**4.4 Division par $x$.** $\sigma\in\mathcal D$ et $\sigma(0)=0$. Par le théorème fondamental, $\sigma(x)=\int_0^1\frac{\mathrm d}{\mathrm dt}\sigma(tx)\,\mathrm dt=x\int_0^1\sigma'(tx)\,\mathrm dt=x\,\eta(x)$. $(t,x)\mapsto\sigma'(tx)$ est $\mathcal C^\infty$, donc $\eta$ est $\mathcal C^\infty$. Si $\sigma$ est nulle hors de $[-a,a]$ avec $a\ge1$, alors pour $|x|>a$, $\eta(x)=\sigma(x)/x=0$ : $\eta\in\mathcal D$.

**4.5 $xT=0$.** Par linéarité et 4.4 :
$$T(\varphi)=T(x\eta)+\varphi(0)T(\chi)=(xT)(\eta)+\varphi(0)T(\chi)=c\,\delta(\varphi),\qquad c=T(\chi).$$
Réciproquement, $(x\delta)(\varphi)=\delta(x\varphi)=0\cdot\varphi(0)=0$. Les solutions sont les $c\,\delta$.

**Étape 5 — Vérification.**

> **Vérification — Analogie avec les fonctions.** Une fonction continue $f$ telle que $xf(x)=0$ est nulle ; dans les distributions, la masse de Dirac « vit » exactement là où $x$ s'annule, d'où les solutions non nulles $c\,\delta$ ✓.

**Étape 6 — Conclusion.**
$$\boxed{T'=0\iff T=T_c\ ;\qquad T'=\delta\iff T=T_{H+c}\ ;\qquad xT=0\iff T=c\,\delta}$$""",
r"""Une fonction test d'intégrale nulle est la dérivée d'une fonction test, donc $T'=0$ impose $T=T(\theta)\int\cdot$ ; $T'=\delta$ donne $T_{H+c}$ ; une fonction test nulle en $0$ s'écrit $x\eta$, donc $xT=0$ impose $T=T(\chi)\,\delta$.""")
dist()

# ------------------------------------------------------------ D3
ex('n-dist-convergence', 'Maths', 'Distributions', 2, 'Suites de fonctions qui convergent vers δ', 25, r"""
On dit qu'une suite de distributions $(T_n)$ converge vers $T$ si $T_n(\varphi)\to T(\varphi)$ pour toute $\varphi\in\mathcal D$.

1. Soit $\rho\in\mathcal D$, positive, nulle hors de $[-1,1]$, d'intégrale $1$, et $\rho_n(x)=n\rho(nx)$. Montrer que $T_{\rho_n}\to\delta$.
2. Montrer que $T_{f_n}\to\delta$ pour $f_n(x)=\dfrac{n}{\pi(1+n^2x^2)}$.
3. Montrer que $T_{\cos(n\,\cdot)}\to0$, bien que $\cos(nx)$ ne tende vers $0$ pour aucun réel $x$.
4. Montrer que $(T_{\rho_n})'\to\delta'$, où $\delta'(\varphi)=-\varphi'(0)$.
""", r"""Après le changement de variable $u=nx$, que devient $\int\rho_n\varphi$ ? Et que reste-t-il à comparer à $\varphi(0)$ ?""",
r"""Inégalité des accroissements finis pour 1, convergence dominée pour 2 (la fonction $\frac{1}{1+u^2}$ est intégrable), intégration par parties pour 3.""",
r"""$\big|\int\rho_n\varphi-\varphi(0)\big|=\big|\int\rho(u)\big(\varphi(u/n)-\varphi(0)\big)\,\mathrm du\big|\le\frac{\|\varphi'\|_\infty}{n}$. Pour 3, $\int\cos(nx)\varphi(x)\,\mathrm dx=-\frac1n\int\sin(nx)\varphi'(x)\,\mathrm dx$.""",
r"""**Étape 1 — Analyse de l'énoncé.** La convergence au sens des distributions est beaucoup plus faible que la convergence simple : des « pics » de plus en plus fins tendent vers $\delta$, et des oscillations rapides tendent vers $0$ par compensation.

**Étape 2 — Rappels du cours.**

> **Théorème — Convergence dominée.** Si $g_n\to g$ simplement et $|g_n|\le h$ intégrable, alors $\int g_n\to\int g$.

> **Théorème — Inégalité des accroissements finis.** $|\varphi(x)-\varphi(y)|\le\|\varphi'\|_\infty|x-y|$.

**Étape 3 — Stratégie.** Changement de variable $u=nx$ pour concentrer la masse en $0$ ; accroissements finis ou convergence dominée ; intégration par parties pour les oscillations.

**Étape 4 — Résolution détaillée.**

**4.1 Suite régularisante.** Avec $u=nx$ et $\int\rho=1$ :
$$\int_{\mathbb R}\rho_n\varphi-\varphi(0)=\int_{-1}^1\rho(u)\big(\varphi(u/n)-\varphi(0)\big)\,\mathrm du,$$
de valeur absolue au plus $\int_{-1}^1\rho(u)\|\varphi'\|_\infty\frac{|u|}n\,\mathrm du\le\frac{\|\varphi'\|_\infty}n\to0$.

**4.2 Noyau de Cauchy.** $\int f_n\varphi=\int_{\mathbb R}\frac{\varphi(u/n)}{\pi(1+u^2)}\,\mathrm du$. L'intégrande tend vers $\frac{\varphi(0)}{\pi(1+u^2)}$ et est dominée par $\frac{\|\varphi\|_\infty}{\pi(1+u^2)}$, intégrable. Par convergence dominée, la limite vaut $\frac{\varphi(0)}\pi\int\frac{\mathrm du}{1+u^2}=\varphi(0)$.

**4.3 Oscillations.** Pour $\varphi$ nulle hors de $[-a,a]$, par parties (termes de bord nuls) :
$$\int_{-a}^a\cos(nx)\varphi(x)\,\mathrm dx=-\frac1n\int_{-a}^a\sin(nx)\varphi'(x)\,\mathrm dx,$$
de valeur absolue au plus $\frac{2a\|\varphi'\|_\infty}n\to0$. Pourtant, pour $x$ fixé, $\cos(nx)$ ne tend pas vers $0$ (sinon $\cos(2nx)=2\cos^2(nx)-1$ tendrait vers $-1$).

**4.4 Dérivées.** $(T_{\rho_n})'(\varphi)=-\int\rho_n\varphi'\to-\varphi'(0)=\delta'(\varphi)$ par 4.1 appliqué à $\varphi'\in\mathcal D$.

**Étape 5 — Vérification.**

> **Vérification — Masse totale.** $\int f_n=\frac1\pi[\arctan(nx)]_{-\infty}^{+\infty}=1$ pour tout $n$ : la masse reste $1$ et se concentre en $0$, comme celle de $\delta$ ✓.

**Étape 6 — Conclusion.**
$$\boxed{T_{\rho_n}\to\delta,\qquad T_{f_n}\to\delta,\qquad T_{\cos(n\,\cdot)}\to0,\qquad(T_{\rho_n})'\to\delta'}$$""",
r"""Changement de variable $u=nx$ puis accroissements finis ($O(1/n)$) ou convergence dominée ; intégration par parties pour $\cos(nx)$ ; la dérivation passe à la limite car $T'(\varphi)=-T(\varphi')$.""")
dist()

# ------------------------------------------------------------ C1 Régression
ex('n-cdp-regression', 'Maths', 'Calcul différentiel & probabilités', 2, 'Meilleure approximation affine d’une variable aléatoire', 25, r"""
Soient $X$ et $Y$ deux variables aléatoires réelles discrètes admettant un moment d'ordre $2$, avec $V(X)>0$. Pour $(a,b)\in\mathbb R^2$, on pose $f(a,b)=E\big((Y-aX-b)^2\big)$.

1. Montrer que $f$ est une fonction polynomiale de degré au plus $2$ en $(a,b)$, et calculer son gradient.
2. Montrer que $f$ admet un unique point critique $(a^*,b^*)$, avec $a^*=\dfrac{\operatorname{Cov}(X,Y)}{V(X)}$ et $b^*=E(Y)-a^*E(X)$.
3. Montrer que $(a^*,b^*)$ est un minimum global de $f$, et que ce minimum vaut $V(Y)\big(1-r^2\big)$ où $r=\dfrac{\operatorname{Cov}(X,Y)}{\sqrt{V(X)V(Y)}}$ (si $V(Y)>0$).
4. En déduire que $|r|\le1$, avec égalité si et seulement si $Y$ est presque sûrement une fonction affine de $X$.
""", r"""Développe le carré et utilise la linéarité de l'espérance : quels coefficients apparaissent devant $a^2$, $b^2$, $ab$, $a$, $b$ ?""",
r"""Point critique : annuler les deux dérivées partielles. Pour la nature, la hessienne d'un polynôme de degré $2$ est constante, et la formule de Taylor à l'ordre $2$ est **exacte**.""",
r"""Montre que la hessienne $2\begin{pmatrix}E(X^2)&E(X)\\E(X)&1\end{pmatrix}$ est définie positive (déterminant $4V(X)$). Pour la valeur, $f(a^*,b^*)=V\big(Y-a^*X\big)$.""",
r"""**Étape 1 — Analyse de l'énoncé.** C'est la régression linéaire des moindres carrés, vue comme un problème d'optimisation d'une fonction de deux variables. Le calcul différentiel donne la droite de régression ; la valeur du minimum donne l'inégalité $|r|\le1$.

**Étape 2 — Rappels du cours.**

> **Théorème — Condition nécessaire.** En un extremum local d'une fonction différentiable sur un ouvert, le gradient est nul.

> **Théorème — Taylor à l'ordre 2.** $f(m+h)=f(m)+\langle\nabla f(m),h\rangle+\frac12{}^thH_f(m)h+o(\|h\|^2)$ ; pour un polynôme de degré $\le2$, le reste est nul.

> **Propriété — Matrice symétrique $2\times2$.** Elle est définie positive si et seulement si son déterminant et sa trace sont strictement positifs.

> **Propriété — Variance.** $V(Z)=E(Z^2)-E(Z)^2$, $V(Y-aX)=V(Y)-2a\operatorname{Cov}(X,Y)+a^2V(X)$.

**Étape 3 — Stratégie.** Développer $f$, annuler le gradient, étudier la hessienne constante, puis exprimer la valeur minimale.

**Étape 4 — Résolution détaillée.**

**4.1 Expression.** Par linéarité :
$$f(a,b)=E(Y^2)+a^2E(X^2)+b^2-2aE(XY)-2bE(Y)+2abE(X),$$
polynôme de degré $2$, de gradient
$$\nabla f(a,b)=\big(2aE(X^2)-2E(XY)+2bE(X),\ 2b-2E(Y)+2aE(X)\big).$$

**4.2 Point critique.** La seconde équation donne $b=E(Y)-aE(X)$. En reportant dans la première : $a\big(E(X^2)-E(X)^2\big)=E(XY)-E(X)E(Y)$, soit $aV(X)=\operatorname{Cov}(X,Y)$. Comme $V(X)>0$, le point critique est unique : $(a^*,b^*)$.

**4.3 Minimum global.** La hessienne est constante : $H=2\begin{pmatrix}E(X^2)&E(X)\\E(X)&1\end{pmatrix}$, de déterminant $4V(X)>0$ et de trace $>0$ : $H$ est définie positive. Comme $f$ est de degré $2$, pour tout $h\in\mathbb R^2$, $f\big((a^*,b^*)+h\big)=f(a^*,b^*)+\frac12{}^thHh\ge f(a^*,b^*)$, avec égalité seulement si $h=0$. Le minimum vaut, puisque $Y-a^*X-b^*=(Y-a^*X)-E(Y-a^*X)$ :
$$f(a^*,b^*)=V(Y-a^*X)=V(Y)-2a^*\operatorname{Cov}(X,Y)+a^{*2}V(X)=V(Y)-\frac{\operatorname{Cov}(X,Y)^2}{V(X)}=V(Y)(1-r^2).$$

**4.4 Inégalité $|r|\le1$.** $f\ge0$ donc $V(Y)(1-r^2)\ge0$, soit $|r|\le1$. Égalité $\iff f(a^*,b^*)=0\iff E\big((Y-a^*X-b^*)^2\big)=0\iff Y=a^*X+b^*$ presque sûrement. Réciproquement, si $Y=\alpha X+\beta$ p.s., alors $\operatorname{Cov}(X,Y)=\alpha V(X)$, $V(Y)=\alpha^2V(X)$ et $|r|=1$ (si $\alpha\ne0$).

**Étape 5 — Vérification.**

> **Vérification — Cas indépendant.** Si $X$ et $Y$ sont indépendantes, $\operatorname{Cov}=0$ : $a^*=0$, $b^*=E(Y)$, et le minimum vaut $V(Y)$. La meilleure prévision affine de $Y$ est sa moyenne ✓.

**Étape 6 — Conclusion.**
$$\boxed{a^*=\frac{\operatorname{Cov}(X,Y)}{V(X)},\quad b^*=E(Y)-a^*E(X),\quad\min f=V(Y)(1-r^2),\quad|r|\le1}$$""",
r"""Gradient nul : $b=E(Y)-aE(X)$ et $aV(X)=\operatorname{Cov}(X,Y)$ ; hessienne constante définie positive (déterminant $4V(X)$) et Taylor exact : minimum global $V(Y)(1-r^2)\ge0$, d'où $|r|\le1$.""")
mp()

# ------------------------------------------------------------ C2 Log-convexité
ex('n-cdp-laplace', 'Maths', 'Calcul différentiel & probabilités', 3, 'Transformée de Laplace d’un couple et convexité', 30, r"""
Soient $X$ et $Y$ deux variables aléatoires réelles prenant un nombre **fini** de valeurs. Pour $(x,y)\in\mathbb R^2$, on pose $L(x,y)=E\big(e^{xX+yY}\big)$ et $g=\ln L$.

1. Montrer que $L$ est de classe $\mathcal C^\infty$ et strictement positive, et calculer $\nabla L(0,0)$ et la hessienne de $L$ en $(0,0)$.
2. Montrer que la hessienne de $g$ en $(0,0)$ est la matrice de covariance $\Sigma=\begin{pmatrix}V(X)&\operatorname{Cov}(X,Y)\\\operatorname{Cov}(X,Y)&V(Y)\end{pmatrix}$, et que $\Sigma$ est symétrique positive.
3. Pour $(x,y)$ fixé et $(u,v)\in\mathbb R^2$, on pose $h(t)=g(x+tu,y+tv)$. Montrer que $h''(t)\ge0$ (on pourra introduire une probabilité « pondérée » par $e^{xX+yY}$).
4. En déduire que $g$ est convexe sur $\mathbb R^2$, puis que $L\big(\tfrac{m+m'}2\big)^2\le L(m)L(m')$ pour tous $m,m'\in\mathbb R^2$.
""", r"""$L$ est une somme finie d'exponentielles : comment dérive-t-on $e^{xi+yj}$ par rapport à $x$ et à $y$ ? Que deviennent ces dérivées en $(0,0)$ ?""",
r"""Dérivées partielles d'une somme finie et règle de la chaîne pour $g=\ln L$ ; une matrice $\Sigma$ est positive si ${}^tw\Sigma w\ge0$, et ici ${}^tw\Sigma w$ est une variance.""",
r"""Avec $Q(X=i,Y=j)=\frac{e^{xi+yj}P(X=i,Y=j)}{L(x,y)}$, montre que $h'(t)=E_Q(uX+vY)$ en $t=0$ et $h''(0)=V_Q(uX+vY)\ge0$ ; le point $(x,y)$ étant quelconque, cela vaut pour tout $t$.""",
r"""**Étape 1 — Analyse de l'énoncé.** La fonction génératrice des moments d'un couple a un logarithme convexe : sa hessienne est toujours une matrice de covariance. On relie ainsi calcul différentiel à deux variables et variance.

**Étape 2 — Rappels du cours.**

> **Propriété — Dérivées partielles.** Une somme finie de fonctions $\mathcal C^\infty$ est $\mathcal C^\infty$ ; $\partial_x e^{xi+yj}=ie^{xi+yj}$.

> **Propriété — Variance d'une combinaison.** $V(uX+vY)=u^2V(X)+2uv\operatorname{Cov}(X,Y)+v^2V(Y)\ge0$.

> **Propriété — Convexité.** Une fonction $\mathcal C^2$ d'une variable est convexe si et seulement si sa dérivée seconde est positive ; une fonction de plusieurs variables est convexe si et seulement si sa restriction à toute droite l'est.

**Étape 3 — Stratégie.** Dériver la somme finie ; règle de la chaîne pour $g$ ; probabilité pondérée pour transporter le calcul de $(0,0)$ à un point quelconque ; convexité le long des droites, puis exponentielle.

**Étape 4 — Résolution détaillée.**

**4.1 Régularité.** $L(x,y)=\sum_{(i,j)}p_{ij}e^{xi+yj}$ avec $p_{ij}=P(X=i,Y=j)$ (somme finie) : $L$ est $\mathcal C^\infty$ et $L>0$. On a $\partial_xL=E(Xe^{xX+yY})$, $\partial_{xx}L=E(X^2e^{xX+yY})$, $\partial_{xy}L=E(XYe^{xX+yY})$, etc. En $(0,0)$ : $\nabla L=(E(X),E(Y))$ et $H_L=\begin{pmatrix}E(X^2)&E(XY)\\E(XY)&E(Y^2)\end{pmatrix}$.

**4.2 Hessienne de $g$.** $\partial_xg=\frac{\partial_xL}{L}$, $\partial_{xy}g=\frac{\partial_{xy}L}{L}-\frac{\partial_xL\,\partial_yL}{L^2}$, etc. En $(0,0)$, $L=1$, d'où $\partial_{xx}g=E(X^2)-E(X)^2=V(X)$, $\partial_{xy}g=E(XY)-E(X)E(Y)=\operatorname{Cov}(X,Y)$, $\partial_{yy}g=V(Y)$ : $H_g(0,0)=\Sigma$. Pour $w=(u,v)$, ${}^tw\Sigma w=V(uX+vY)\ge0$ : $\Sigma$ est symétrique positive.

**4.3 Point quelconque.** Fixons $(x,y)$. Les nombres $q_{ij}=\frac{p_{ij}e^{xi+yj}}{L(x,y)}$ sont positifs de somme $1$ : ils définissent une loi $Q$ de couple $(X',Y')$. Pour $(s,t')$, $L(x+s,y+t')=L(x,y)\,L_Q(s,t')$ où $L_Q$ est la fonction analogue pour $(X',Y')$. Donc $g(x+s,y+t')=g(x,y)+g_Q(s,t')$, et par 4.2 appliqué à $(X',Y')$ : $H_g(x,y)=\Sigma_Q$, matrice de covariance de $(X',Y')$. Avec $h(t)=g(x+tu,y+tv)$, la règle de la chaîne donne $h''(0)={}^tw\,H_g(x,y)\,w=V_Q(uX'+vY')\ge0$. Le point $(x,y)$ étant arbitraire, $h''(t)\ge0$ pour tout $t$.

**4.4 Convexité et inégalité.** Toute restriction de $g$ à une droite est convexe, donc $g$ est convexe : $g\big(\frac{m+m'}2\big)\le\frac{g(m)+g(m')}2$. En prenant l'exponentielle : $L\big(\frac{m+m'}2\big)\le\sqrt{L(m)L(m')}$, d'où l'inégalité demandée.

**Étape 5 — Vérification.**

> **Vérification — Cas indépendant.** Si $X$ et $Y$ sont indépendantes, $L(x,y)=E(e^{xX})E(e^{yY})$ et $g(x,y)=g_X(x)+g_Y(y)$ : la hessienne est diagonale, $\operatorname{Cov}(X,Y)=0$ ✓. L'inégalité de 4 est aussi l'inégalité de Cauchy-Schwarz $E(e^{(Z+Z')/2})^2\le E(e^Z)E(e^{Z'})$ ✓.

**Étape 6 — Conclusion.**
$$\boxed{H_{\ln L}(0,0)=\Sigma\succeq0,\qquad\ln L\ \text{convexe sur}\ \mathbb R^2,\qquad L\big(\tfrac{m+m'}2\big)^2\le L(m)L(m')}$$""",
r"""$L$ est une somme finie d'exponentielles ; la hessienne de $\ln L$ en $0$ est la matrice de covariance, positive ; par la loi pondérée $Q\propto e^{xX+yY}P$, la hessienne en tout point est une covariance, donc $\ln L$ est convexe.""")
mp()

# ------------------------------------------------------------ C3 Entropie
ex('n-cdp-entropie', 'Maths', 'Calcul différentiel & probabilités', 3, 'Entropie maximale', 30, r"""
Pour une loi $p=(p_1,\dots,p_n)$ sur $\{1,\dots,n\}$ (avec $p_i\ge0$, $\sum p_i=1$), on définit l'**entropie** $H(p)=-\sum_{i=1}^np_i\ln p_i$ (avec la convention $0\ln0=0$).

1. Sur l'ouvert $U=\,]0,+\infty[^n$, on considère $H$ et la contrainte $C(p)=\sum p_i=1$. Montrer qu'en un extremum de $H$ sur $U\cap\{C=1\}$, le gradient de $H$ est colinéaire à celui de $C$, et en déduire le seul candidat.
2. Montrer que $\ln x\le x-1$ pour $x>0$, puis que $H(p)\le\ln n$ pour toute loi $p$, avec égalité si et seulement si $p$ est uniforme.
3. Soit $\beta\in\mathbb R$, $Z=\sum_{i=1}^ne^{-\beta i}$ et $q_i=\frac{e^{-\beta i}}Z$. Montrer que pour toute loi $p$ de même espérance que $q$ (c'est-à-dire $\sum ip_i=\sum iq_i$), on a $H(p)\le H(q)$.
""", r"""Que valent les dérivées partielles de $H$ et de $C$ ? Et pour comparer $H(p)$ à $\ln n$, quelle inégalité élémentaire sur le logarithme utiliser avec $x=\frac{1}{np_i}$ ?""",
r"""Extrema liés : en un extremum de $H$ sous la contrainte $C=1$ (avec $\nabla C\ne0$), $\nabla H=\lambda\nabla C$. Pour 2 et 3, l'inégalité de Gibbs $\sum p_i\ln\frac{q_i}{p_i}\le0$ découle de $\ln x\le x-1$.""",
r"""$-\ln p_i-1=\lambda$ pour tout $i$ force $p_i$ constant. Pour 3, écris $\sum p_i\ln\frac{q_i}{p_i}\le\sum(q_i-p_i)=0$, puis $-\sum p_i\ln q_i=\beta\sum ip_i+\ln Z$.""",
r"""**Étape 1 — Analyse de l'énoncé.** L'entropie mesure l'incertitude d'une loi. On montre que la loi la plus incertaine est l'uniforme, puis, à espérance fixée, une loi exponentielle (de Gibbs). Le calcul différentiel donne le candidat, une inégalité de convexité prouve l'optimalité globale.

**Étape 2 — Rappels du cours.**

> **Théorème — Extrema liés.** Si $f$ et $g$ sont $\mathcal C^1$ sur un ouvert, si $f$ restreinte à $\{g=0\}$ admet un extremum local en $a$ et si $\nabla g(a)\ne0$, alors $\nabla f(a)$ est colinéaire à $\nabla g(a)$.

> **Propriété — Concavité du logarithme.** $\ln x\le x-1$ pour $x>0$, avec égalité si et seulement si $x=1$.

**Étape 3 — Stratégie.** Extrema liés pour trouver le candidat ; inégalité de Gibbs pour l'optimalité globale, y compris sur le bord du simplexe ; même inégalité avec la loi de Gibbs $q$ pour la question 3.

**Étape 4 — Résolution détaillée.**

**4.1 Candidat.** Sur $U$, $\partial_iH(p)=-\ln p_i-1$ et $\nabla C=(1,\dots,1)\ne0$. En un extremum lié, il existe $\lambda$ avec $-\ln p_i-1=\lambda$ pour tout $i$ : les $p_i$ sont égaux, et $\sum p_i=1$ donne $p_i=\frac1n$. C'est le seul candidat, avec $H=\ln n$.

**4.2 Maximum global.** $f(x)=\ln x-x+1$ a pour dérivée $\frac1x-1$ : maximum en $1$, où $f(1)=0$ ; donc $\ln x\le x-1$, avec égalité seulement en $1$. Soit $p$ une loi et $I=\{i,\ p_i>0\}$. Alors
$$H(p)-\ln n=\sum_{i\in I}p_i\ln\frac{1}{np_i}\le\sum_{i\in I}p_i\Big(\frac1{np_i}-1\Big)=\frac{|I|}n-1\le0.$$
Égalité si et seulement si $|I|=n$ et $np_i=1$ pour tout $i$ : $p$ uniforme.

**4.3 Loi de Gibbs.** Soit $p$ de même espérance que $q$. Les $q_i$ sont $>0$ ; avec $I$ comme ci-dessus,
$$\sum_{i\in I}p_i\ln\frac{q_i}{p_i}\le\sum_{i\in I}(q_i-p_i)\le0,$$
donc $H(p)\le-\sum_ip_i\ln q_i=\sum_ip_i(\beta i+\ln Z)=\beta\sum ip_i+\ln Z$. Pour $p=q$, l'égalité a lieu dans les deux inégalités : $H(q)=\beta\sum iq_i+\ln Z$. Comme $\sum ip_i=\sum iq_i$, on obtient $H(p)\le H(q)$.

**Étape 5 — Vérification.**

> **Vérification — $\beta=0$.** $q$ est alors uniforme, d'espérance $\frac{n+1}2$, et l'on retrouve $H(p)\le\ln n$ ✓.

**Étape 6 — Conclusion.**
$$\boxed{H(p)\le\ln n\ (\text{égalité}\iff p\ \text{uniforme}),\qquad H(p)\le H(q)\ \text{à espérance fixée, avec}\ q_i\propto e^{-\beta i}}$$""",
r"""Extrema liés : $-\ln p_i-1=\lambda$ donne l'uniforme ; $\ln x\le x-1$ donne $H(p)\le\ln n$ (et traite le bord) ; à espérance fixée, l'inégalité de Gibbs contre $q_i\propto e^{-\beta i}$ donne $H(p)\le\beta m+\ln Z=H(q)$.""")
mp()
