# Mathématiques — 20 exercices de niveau CCINP (énoncés, indices et corrigés originaux).
from newlib import ex, E

def cc():
    E[-1]['enonce'] += "\n\n*Dans l'esprit des oraux CCINP.*"
    E[-1]['concours'] = 'CCINP'
    E[-1]['ajout'] = '2026-11-26'

def C(analyse, rappels, strategie, resolution, verif, conclusion):
    return ("**Étape 1 — Analyse de l'énoncé.** " + analyse + "\n\n**Étape 2 — Rappels du cours.**\n\n" + rappels +
            "\n\n**Étape 3 — Stratégie.** " + strategie + "\n\n**Étape 4 — Résolution détaillée.**\n\n" + resolution +
            "\n\n**Étape 5 — Vérification.**\n\n" + verif + "\n\n**Étape 6 — Conclusion.**\n$$\\boxed{" + conclusion + "}$$")

# 1 ---------------------------------------------------------------- Séries de Bertrand
ex('n-cc-bertrand', 'Maths', 'Séries', 1, 'Séries de Bertrand par comparaison série-intégrale', 15, r"""
1. Montrer que la série $\sum_{n\ge2}\frac{1}{n\ln n}$ diverge.
2. Montrer que la série $\sum_{n\ge2}\frac{1}{n(\ln n)^2}$ converge.
""", r"""Les termes sont positifs et décroissants : à quelle intégrale peut-on comparer la série ?""",
r"""Comparaison série-intégrale pour $f$ continue, positive, décroissante sur $[2,+\infty[$ : $\sum f(n)$ et $\int_2^{+\infty}f$ sont de même nature.""",
r"""Une primitive de $\frac{1}{t\ln t}$ est $\ln(\ln t)$, et une primitive de $\frac{1}{t(\ln t)^2}$ est $-\frac{1}{\ln t}$.""",
C(r"Deux séries à termes positifs qui ne relèvent ni de Riemann ni de d'Alembert : la comparaison avec une intégrale conclut.",
r"""> **Théorème — Comparaison série-intégrale.** Si $f$ est continue, positive et décroissante sur $[a,+\infty[$, alors $\sum f(n)$ converge si et seulement si $\int_a^{+\infty}f$ converge.""",
r"Vérifier la décroissance, puis calculer les intégrales grâce aux primitives.",
r"""**4.1 Hypothèses.** $f(t)=\frac{1}{t\ln t}$ et $g(t)=\frac{1}{t(\ln t)^2}$ sont continues, positives et décroissantes sur $[2,+\infty[$ (dénominateurs positifs et croissants).

**4.2 Première série.** $\int_2^Xf=\ln(\ln X)-\ln(\ln2)\to+\infty$ : l'intégrale diverge, donc $\sum\frac1{n\ln n}$ diverge.

**4.3 Seconde série.** $\int_2^Xg=\frac1{\ln2}-\frac1{\ln X}\to\frac1{\ln2}$ : l'intégrale converge, donc $\sum\frac1{n(\ln n)^2}$ converge.""",
r"""> **Vérification — Ordre de grandeur.** $\sum_{k=2}^n\frac1{k\ln k}\approx\ln\ln n$ diverge extrêmement lentement : $\ln\ln(10^{10})\approx3{,}1$. Le critère de Riemann ne s'applique pas, car $\frac1{n\ln n}$ est entre $\frac1n$ et $\frac1{n^\alpha}$ pour tout $\alpha<1$.""",
r"\sum\frac1{n\ln n}\ \text{diverge},\qquad\sum\frac1{n(\ln n)^2}\ \text{converge}"),
r"""Comparaison série-intégrale : $\int_2^X\frac{\mathrm dt}{t\ln t}=\ln\ln X-\ln\ln2\to+\infty$ (divergence) et $\int_2^X\frac{\mathrm dt}{t(\ln t)^2}\to\frac1{\ln2}$ (convergence).""")
cc()

# 2 ---------------------------------------------------------------- Télescopage
ex('n-cc-telescope', 'Maths', 'Séries', 1, 'Une somme calculée par télescopage', 15, r"""
1. Déterminer un réel $a$ tel que $\dfrac{1}{n(n+1)(n+2)}=a\Big(\dfrac1{n(n+1)}-\dfrac1{(n+1)(n+2)}\Big)$ pour tout $n\ge1$.
2. En déduire la convergence et la somme de $\sum_{n\ge1}\dfrac{1}{n(n+1)(n+2)}$.
""", r"""Que vaut la différence $\frac1{n(n+1)}-\frac1{(n+1)(n+2)}$ une fois réduite au même dénominateur ?""",
r"""Une somme de différences $u_n-u_{n+1}$ se télescope : $\sum_{n=1}^N(u_n-u_{n+1})=u_1-u_{N+1}$.""",
r"""$\frac1{n(n+1)}-\frac1{(n+1)(n+2)}=\frac{2}{n(n+1)(n+2)}$, donc $a=\frac12$.""",
C(r"Une série à termes positifs dont le terme général se décompose en différence de deux termes consécutifs d'une même suite.",
r"""> **Propriété — Télescopage.** $\sum_{n=1}^N(u_n-u_{n+1})=u_1-u_{N+1}$ ; si $u_n\to0$, la série converge et sa somme vaut $u_1$.""",
r"Réduire au même dénominateur, puis télescoper.",
r"""**4.1 Décomposition.** $\frac1{n(n+1)}-\frac1{(n+1)(n+2)}=\frac{(n+2)-n}{n(n+1)(n+2)}=\frac2{n(n+1)(n+2)}$, d'où $a=\frac12$.

**4.2 Somme partielle.** Avec $u_n=\frac1{n(n+1)}$ : $S_N=\frac12\sum_{n=1}^N(u_n-u_{n+1})=\frac12\Big(\frac12-\frac1{(N+1)(N+2)}\Big)$.

**4.3 Limite.** $S_N\to\frac14$ : la série converge et sa somme vaut $\frac14$.""",
r"""> **Vérification — Premiers termes.** $\frac16+\frac1{24}+\frac1{60}+\frac1{120}\approx0{,}233$, déjà proche de $0{,}25$ ✓.""",
r"\sum_{n\ge1}\frac1{n(n+1)(n+2)}=\frac14"),
r"""$\frac1{n(n+1)(n+2)}=\frac12\Big(\frac1{n(n+1)}-\frac1{(n+1)(n+2)}\Big)$ ; par télescopage $S_N=\frac14-\frac1{2(N+1)(N+2)}\to\frac14$.""")
cc()

# 3 ---------------------------------------------------------------- Somme d'une série entière
ex('n-cc-se-somme', 'Maths', 'Séries entières', 1, 'Rayon et somme de Σ (n+1)xⁿ/n!', 15, r"""
Déterminer le rayon de convergence et la somme de la série entière $\displaystyle\sum_{n\ge0}\frac{n+1}{n!}x^n$.
""", r"""Peut-on séparer $\frac{n+1}{n!}$ en deux morceaux faisant apparaître des séries connues ?""",
r"""Règle de d'Alembert pour le rayon ; pour la somme, reconnaître la série de l'exponentielle et $\frac{n}{n!}=\frac1{(n-1)!}$.""",
r"""$\sum\frac{n}{n!}x^n=x\sum_{n\ge1}\frac{x^{n-1}}{(n-1)!}=xe^x$.""",
C(r"Une série entière dont le coefficient est un polynôme en $n$ divisé par $n!$ : on se ramène à l'exponentielle.",
r"""> **Propriété — Exponentielle.** $e^x=\sum_{n\ge0}\frac{x^n}{n!}$, de rayon $+\infty$.

> **Théorème — Règle de d'Alembert.** Si $\left|\frac{a_{n+1}}{a_n}\right|\to\ell$, le rayon vaut $\frac1\ell$ ($+\infty$ si $\ell=0$).""",
r"Rayon par d'Alembert, somme par découpage.",
r"""**4.1 Rayon.** $\frac{a_{n+1}}{a_n}=\frac{n+2}{(n+1)!}\cdot\frac{n!}{n+1}=\frac{n+2}{(n+1)^2}\to0$ : $R=+\infty$.

**4.2 Somme.** Pour tout réel $x$ : $\sum_{n\ge0}\frac{n+1}{n!}x^n=\sum_{n\ge1}\frac{x^n}{(n-1)!}+\sum_{n\ge0}\frac{x^n}{n!}=xe^x+e^x$.""",
r"""> **Vérification — En $x=0$ et par dérivation.** En $0$ : $a_0=1$ et $(x+1)e^x=1$ ✓. On remarque aussi que $(x+1)e^x=(xe^x)'$ et que $xe^x=\sum\frac{x^{n+1}}{n!}$ se dérive en $\sum\frac{(n+1)x^n}{n!}$ ✓.""",
r"R=+\infty,\qquad\sum_{n\ge0}\frac{n+1}{n!}x^n=(x+1)e^x"),
r"""D'Alembert : $\frac{n+2}{(n+1)^2}\to0$, $R=+\infty$ ; $\sum\frac{n+1}{n!}x^n=xe^x+e^x=(x+1)e^x$.""")
cc()

# 4 ---------------------------------------------------------------- DSE de ln(1+x+x²)
ex('n-cc-se-ln', 'Maths', 'Séries entières', 1, 'Développement de ln(1 + x + x²)', 20, r"""
1. Montrer que $1+x+x^2=\dfrac{1-x^3}{1-x}$ pour $x\ne1$.
2. En déduire le développement en série entière de $f(x)=\ln(1+x+x^2)$ au voisinage de $0$, et son rayon de convergence.
""", r"""Quelle identité remarquable relie $1-x^3$ et $1-x$ ? Et quel développement usuel connais-tu pour $\ln(1-u)$ ?""",
r"""$\ln(1-u)=-\sum_{n\ge1}\frac{u^n}{n}$ pour $|u|<1$ ; appliquer avec $u=x$ et $u=x^3$.""",
r"""Les coefficients valent $\frac1n$ si $3\nmid n$ et $\frac1n-\frac3n=-\frac2n$ si $3\mid n$ ; pour le rayon, compare à $\sum\frac{x^n}{n}$.""",
C(r"On transforme un logarithme de trinôme en différence de logarithmes usuels.",
r"""> **Propriété — Développement usuel.** Pour $|u|<1$, $\ln(1-u)=-\sum_{n\ge1}\frac{u^n}n$.

> **Propriété — Rayon et équivalents.** Si $|a_n|\sim|b_n|$ (ou $c_1|b_n|\le|a_n|\le c_2|b_n|$), les séries $\sum a_nx^n$ et $\sum b_nx^n$ ont le même rayon.""",
r"Factoriser, passer au logarithme sur $]-1,1[$, regrouper les coefficients.",
r"""**4.1 Identité.** $(1-x)(1+x+x^2)=1-x^3$.

**4.2 Développement.** Pour $|x|<1$, $1-x>0$ et $1-x^3>0$, donc
$$f(x)=\ln(1-x^3)-\ln(1-x)=\sum_{n\ge1}\frac{x^n}n-\sum_{k\ge1}\frac{x^{3k}}k.$$
Comme $\frac{x^{3k}}k=\frac{3x^{3k}}{3k}$, le coefficient $a_n$ de $x^n$ vaut $\frac1n$ si $3\nmid n$ et $-\frac2n$ si $3\mid n$.

**4.3 Rayon.** $\frac1n\le|a_n|\le\frac2n$ : même rayon que $\sum\frac{x^n}n$, soit $R=1$.""",
r"""> **Vérification — Ordre 3.** $f(x)=x+\frac{x^2}2-\frac{2x^3}3+o(x^3)$. Directement : $\ln(1+u)$ avec $u=x+x^2$ donne $u-\frac{u^2}2+\frac{u^3}3=x+x^2-\frac{x^2+2x^3}2+\frac{x^3}3+o(x^3)=x+\frac{x^2}2-\frac{2x^3}3+o(x^3)$ ✓.""",
r"\ln(1+x+x^2)=\sum_{n\ge1}a_nx^n,\quad a_n=\tfrac1n\ (3\nmid n),\ a_n=-\tfrac2n\ (3\mid n),\quad R=1"),
r"""$1+x+x^2=\frac{1-x^3}{1-x}$, donc $f=\ln(1-x^3)-\ln(1-x)$ ; $a_n=\frac1n$ sauf $a_{3k}=-\frac{2}{3k}$ ; $R=1$.""")
cc()

# 5 ---------------------------------------------------------------- Intégrales de Wallis généralisées
ex('n-cc-wallis', 'Maths', 'Intégration', 1, 'Les intégrales ∫ dx/(1+x²)ⁿ', 20, r"""
Pour $n\ge1$, on pose $I_n=\displaystyle\int_0^{+\infty}\frac{\mathrm dx}{(1+x^2)^n}$.

1. Justifier l'existence de $I_n$ et calculer $I_1$.
2. Montrer que $I_n=2n\,(I_n-I_{n+1})$, puis que $I_{n+1}=\dfrac{2n-1}{2n}I_n$.
3. En déduire $I_2$ et $I_3$.
""", r"""Comment se comporte l'intégrande en $+\infty$ ? Et quelle intégration par parties fait apparaître $(1+x^2)^{-n-1}$ ?""",
r"""Intégration par parties avec $u=(1+x^2)^{-n}$ et $v'=1$ ; puis écrire $x^2=(1+x^2)-1$.""",
r"""$I_n=\big[x(1+x^2)^{-n}\big]_0^{+\infty}+2n\int_0^{+\infty}\frac{x^2}{(1+x^2)^{n+1}}\,\mathrm dx$, et $\frac{x^2}{(1+x^2)^{n+1}}=\frac1{(1+x^2)^n}-\frac1{(1+x^2)^{n+1}}$.""",
C(r"Une famille d'intégrales généralisées reliées par une relation de récurrence obtenue par intégration par parties.",
r"""> **Propriété — Intégrale de Riemann.** $\int_1^{+\infty}\frac{\mathrm dx}{x^\alpha}$ converge si et seulement si $\alpha>1$.

> **Théorème — Intégration par parties généralisée.** Valable si le crochet a des limites finies aux bornes ; les deux intégrales sont alors de même nature.""",
r"Existence par comparaison, intégration par parties, récurrence.",
r"""**4.1 Existence.** L'intégrande est continue sur $[0,+\infty[$ et $\frac1{(1+x^2)^n}\le\frac1{x^2}$ pour $x\ge1$ : $I_n$ converge. $I_1=[\arctan x]_0^{+\infty}=\frac\pi2$.

**4.2 Relation.** Avec $u=(1+x^2)^{-n}$, $u'=-2nx(1+x^2)^{-n-1}$, $v=x$ : le crochet $\frac{x}{(1+x^2)^n}$ est nul en $0$ et tend vers $0$ en $+\infty$. Donc
$$I_n=2n\int_0^{+\infty}\frac{x^2}{(1+x^2)^{n+1}}\,\mathrm dx=2n\,(I_n-I_{n+1}),$$
car $x^2=(1+x^2)-1$. D'où $2nI_{n+1}=(2n-1)I_n$.

**4.3 Valeurs.** $I_2=\frac12I_1=\frac\pi4$, $I_3=\frac34I_2=\frac{3\pi}{16}$.""",
r"""> **Vérification — $I_2$ directement.** Avec $x=\tan\theta$ : $I_2=\int_0^{\pi/2}\cos^2\theta\,\mathrm d\theta=\frac\pi4$ ✓.""",
r"I_1=\frac\pi2,\quad I_{n+1}=\frac{2n-1}{2n}I_n,\quad I_2=\frac\pi4,\quad I_3=\frac{3\pi}{16}"),
r"""Convergence par comparaison à $\frac1{x^2}$ ; IPP : $I_n=2n(I_n-I_{n+1})$, d'où $I_{n+1}=\frac{2n-1}{2n}I_n$, $I_2=\frac\pi4$, $I_3=\frac{3\pi}{16}$.""")
cc()

# 6 ---------------------------------------------------------------- Convergence dominée
ex('n-cc-cvd', 'Maths', 'Intégration', 1, 'Limite de ∫₀ⁿ (1 − x/n)ⁿ dx', 15, r"""
1. Montrer que $\ln(1-u)\le-u$ pour $u\in[0,1[$.
2. Pour $n\ge1$, on pose $f_n(x)=\big(1-\frac xn\big)^n$ si $0\le x\le n$, et $f_n(x)=0$ si $x>n$. Montrer que $0\le f_n(x)\le e^{-x}$.
3. En déduire $\displaystyle\lim_{n\to+\infty}\int_0^n\Big(1-\frac xn\Big)^n\mathrm dx$, puis retrouver ce résultat par un calcul direct.
""", r"""Vers quoi tend $\big(1-\frac xn\big)^n$ pour $x$ fixé ? Et par quelle fonction intégrable peut-on la majorer ?""",
r"""Théorème de convergence dominée sur $[0,+\infty[$ : limite simple, plus domination par une fonction intégrable indépendante de $n$.""",
r"""$f_n(x)=\exp\big(n\ln(1-\frac xn)\big)\le e^{-x}$ grâce à la question 1, et $\int_0^ne^{\cdots}$ se calcule aussi directement : $\int_0^n\big(1-\frac xn\big)^n\mathrm dx=\frac{n}{n+1}$.""",
C(r"Une limite d'intégrales sur des intervalles qui grandissent : on se ramène à $[0,+\infty[$ avec une indicatrice, puis convergence dominée.",
r"""> **Théorème — Convergence dominée.** Si $f_n\to f$ simplement sur $I$ (fonctions continues par morceaux) et $|f_n|\le\varphi$ intégrable, alors $\int_If_n\to\int_If$.

> **Propriété — Concavité du logarithme.** $\ln(1+t)\le t$ pour $t>-1$.""",
r"Majoration par le logarithme, limite simple, convergence dominée.",
r"""**4.1 Inégalité.** $\ln(1+t)\le t$ avec $t=-u$.

**4.2 Domination.** Pour $0\le x<n$, $f_n(x)=\exp\big(n\ln(1-\frac xn)\big)\le\exp(-x)$ ; pour $x=n$ ou $x>n$, $f_n(x)=0\le e^{-x}$.

**4.3 Limite simple.** Pour $x$ fixé et $n>x$ : $n\ln(1-\frac xn)\to-x$, donc $f_n(x)\to e^{-x}$.

**4.4 Conclusion.** $e^{-x}$ est intégrable sur $[0,+\infty[$ : par convergence dominée, $\int_0^nf_n=\int_0^{+\infty}f_n\to\int_0^{+\infty}e^{-x}\,\mathrm dx=1$.

**4.5 Calcul direct.** Avec $u=1-\frac xn$ : $\int_0^n\big(1-\frac xn\big)^n\mathrm dx=n\int_0^1u^n\,\mathrm du=\frac n{n+1}\to1$ ✓.""",
r"""> **Vérification — $n=1$.** $\int_0^1(1-x)\,\mathrm dx=\frac12=\frac1{1+1}$ ✓.""",
r"\lim_{n\to\infty}\int_0^n\Big(1-\frac xn\Big)^n\mathrm dx=1"),
r"""$f_n\le e^{-x}$ par $\ln(1-u)\le-u$, et $f_n\to e^{-x}$ : par convergence dominée la limite vaut $\int_0^\infty e^{-x}=1$ (calcul direct : $\frac{n}{n+1}$).""")
cc()

# 7 ---------------------------------------------------------------- Intégrale à paramètre et ED
ex('n-cc-param', 'Maths', 'Intégrales à paramètre', 1, 'Une intégrale à paramètre solution de y″ + y = 1/x', 25, r"""
Pour $x\ge0$, on pose $F(x)=\displaystyle\int_0^{+\infty}\frac{e^{-xt}}{1+t^2}\,\mathrm dt$.

1. Montrer que $F$ est définie et continue sur $[0,+\infty[$, et calculer $F(0)$.
2. Montrer que $F$ est de classe $\mathcal C^2$ sur $]0,+\infty[$ et que $F''(x)+F(x)=\dfrac1x$.
3. Déterminer $\lim_{x\to+\infty}F(x)$.
""", r"""Quelle majoration de l'intégrande ne dépend pas de $x\ge0$ ? Et que donne la dérivation de $e^{-xt}$ par rapport à $x$ ?""",
r"""Théorèmes de continuité et de dérivation sous l'intégrale avec domination ; pour $F''$, la domination n'est possible que sur $[a,+\infty[$ avec $a>0$.""",
r"""Sur $[a,+\infty[$ : $\frac{t^2e^{-xt}}{1+t^2}\le e^{-at}$. Puis $F''+F=\int_0^{+\infty}e^{-xt}\,\mathrm dt$. Pour la limite, $0\le F(x)\le\int_0^{+\infty}e^{-xt}\,\mathrm dt$.""",
C(r"Une transformée de Laplace : on étudie sa régularité par domination, puis on montre qu'elle vérifie une équation différentielle.",
r"""> **Théorème — Continuité sous l'intégrale.** Domination $|f(x,t)|\le\varphi(t)$ intégrable, indépendante de $x$.

> **Théorème — Dérivation sous l'intégrale.** Domination de $\partial_x^kf$ ; la domination sur tout segment (ou tout $[a,+\infty[$) de l'intervalle suffit.""",
r"Domination globale pour la continuité, domination locale pour la dérivabilité, calcul de $F''+F$.",
r"""**4.1 Continuité.** $f(x,t)=\frac{e^{-xt}}{1+t^2}$ est continue, et pour $x\ge0$ : $|f(x,t)|\le\frac1{1+t^2}$, intégrable sur $[0,+\infty[$. Donc $F$ est définie et continue sur $[0,+\infty[$, et $F(0)=\int_0^{+\infty}\frac{\mathrm dt}{1+t^2}=\frac\pi2$.

**4.2 Classe $\mathcal C^2$.** $\partial_xf=-\frac{te^{-xt}}{1+t^2}$ et $\partial_x^2f=\frac{t^2e^{-xt}}{1+t^2}$. Pour $x\ge a>0$ : $|\partial_xf|\le e^{-at}$ et $|\partial_x^2f|\le e^{-at}$, intégrables. Donc $F$ est $\mathcal C^2$ sur $[a,+\infty[$ pour tout $a>0$, donc sur $]0,+\infty[$, et
$$F''(x)+F(x)=\int_0^{+\infty}\frac{(t^2+1)e^{-xt}}{1+t^2}\,\mathrm dt=\int_0^{+\infty}e^{-xt}\,\mathrm dt=\frac1x.$$

**4.3 Limite.** $0\le F(x)\le\int_0^{+\infty}e^{-xt}\,\mathrm dt=\frac1x\to0$.""",
r"""> **Vérification — Cohérence.** $F$ est décroissante ($F'\le0$), part de $\frac\pi2$ et tend vers $0$ ; pour $x$ grand, $F(x)\approx\frac1x$ (la masse se concentre près de $t=0$ où $\frac1{1+t^2}\approx1$) ✓.""",
r"F(0)=\frac\pi2,\qquad F''+F=\frac1x\ \text{sur}\ ]0,+\infty[,\qquad\lim_{+\infty}F=0"),
r"""Domination par $\frac1{1+t^2}$ : $F$ continue, $F(0)=\frac\pi2$ ; domination par $e^{-at}$ sur $[a,+\infty[$ : $F$ est $\mathcal C^2$ et $F''+F=\int_0^\infty e^{-xt}\,\mathrm dt=\frac1x$ ; $0\le F\le\frac1x$.""")
cc()

# 8 ---------------------------------------------------------------- ED ordre 1
ex('n-cc-ed1', 'Maths', 'Équations différentielles', 1, 'Équation (1 + x²)y′ + xy = 1', 15, r"""
Résoudre sur $\mathbb R$ l'équation différentielle $(1+x^2)\,y'+x\,y=1$, puis déterminer la solution telle que $y(0)=2$.
""", r"""Peut-on diviser par $1+x^2$ ? Quelle est alors la forme des solutions de l'équation homogène ?""",
r"""Équation linéaire d'ordre 1 : solution générale = solutions homogènes + une solution particulière, obtenue par variation de la constante.""",
r"""Homogène : $y=\frac{C}{\sqrt{1+x^2}}$. Variation : $C'(x)=\frac1{\sqrt{1+x^2}}$, dont une primitive est $\ln\big(x+\sqrt{1+x^2}\big)$.""",
C(r"Équation linéaire d'ordre 1 à coefficients non constants ; le coefficient de $y'$ ne s'annule pas, donc on travaille sur tout $\mathbb R$.",
r"""> **Théorème — Équations d'ordre 1.** Les solutions de $y'+a(x)y=0$ sont $Ce^{-A(x)}$ ($A$ primitive de $a$) ; la variation de la constante fournit une solution particulière.

> **Propriété — Primitive.** $\big(\ln(x+\sqrt{1+x^2})\big)'=\frac1{\sqrt{1+x^2}}$.""",
r"Normaliser, résoudre l'homogène, faire varier la constante, puis imposer $y(0)=2$.",
r"""**4.1 Forme normale.** $1+x^2>0$ : $y'+\frac{x}{1+x^2}y=\frac1{1+x^2}$.

**4.2 Homogène.** $A(x)=\frac12\ln(1+x^2)$, donc $y_h=\frac{C}{\sqrt{1+x^2}}$.

**4.3 Variation de la constante.** $y=\frac{C(x)}{\sqrt{1+x^2}}$ donne $\frac{C'(x)}{\sqrt{1+x^2}}=\frac1{1+x^2}$, soit $C'(x)=\frac1{\sqrt{1+x^2}}$ et $C(x)=\ln\big(x+\sqrt{1+x^2}\big)+K$.

**4.4 Solutions.** $y(x)=\dfrac{\ln\big(x+\sqrt{1+x^2}\big)+K}{\sqrt{1+x^2}}$, $K\in\mathbb R$. Avec $y(0)=K=2$ : $y(x)=\dfrac{\ln\big(x+\sqrt{1+x^2}\big)+2}{\sqrt{1+x^2}}$.""",
r"""> **Vérification — Par le produit.** L'équation s'écrit $\big(\sqrt{1+x^2}\,y\big)'=\frac1{\sqrt{1+x^2}}$ (on vérifie que $(\sqrt{1+x^2}\,y)'=\frac{(1+x^2)y'+xy}{\sqrt{1+x^2}}$) ✓.""",
r"y(x)=\frac{\ln\big(x+\sqrt{1+x^2}\big)+K}{\sqrt{1+x^2}},\qquad y(0)=2\iff K=2"),
r"""Homogène $\frac{C}{\sqrt{1+x^2}}$ ; variation : $C'=\frac1{\sqrt{1+x^2}}$, $C=\ln(x+\sqrt{1+x^2})+K$ ; $y(0)=2$ donne $K=2$.""")
cc()

# 9 ---------------------------------------------------------------- ED ordre 2 résonance
ex('n-cc-ed2', 'Maths', 'Équations différentielles', 1, 'Équation y″ − 2y′ + y = eˣ', 15, r"""
Résoudre sur $\mathbb R$ l'équation $y''-2y'+y=e^x$, puis trouver la solution vérifiant $y(0)=0$ et $y'(0)=1$.
""", r"""Quelle est l'équation caractéristique, et quelle est la particularité de sa racine par rapport au second membre ?""",
r"""Second membre $e^{mx}$ avec $m$ racine **double** : chercher une solution particulière de la forme $\alpha x^2e^x$.""",
r"""Avec $y=\alpha x^2e^x$ : $y''-2y'+y=2\alpha e^x$, donc $\alpha=\frac12$.""",
C(r"Équation linéaire d'ordre 2 à coefficients constants avec un second membre en résonance double.",
r"""> **Théorème — Équation homogène.** Si $1$ est racine double de $r^2-2r+1$, les solutions sont $(\lambda x+\mu)e^x$.

> **Méthode — Second membre $e^{mx}$.** Chercher $Q(x)e^{mx}$ avec $\deg Q=0$, $1$ ou $2$ selon que $m$ n'est pas racine, racine simple ou racine double.""",
r"Homogène, solution particulière, conditions initiales.",
r"""**4.1 Homogène.** $r^2-2r+1=(r-1)^2$ : $y_h=(\lambda x+\mu)e^x$.

**4.2 Particulière.** $y_p=\alpha x^2e^x$ : $y_p'=\alpha(2x+x^2)e^x$, $y_p''=\alpha(2+4x+x^2)e^x$, donc $y_p''-2y_p'+y_p=\alpha(2+4x+x^2-4x-2x^2+x^2)e^x=2\alpha e^x$, et $\alpha=\frac12$.

**4.3 Solutions.** $y=\big(\frac{x^2}2+\lambda x+\mu\big)e^x$. $y(0)=\mu=0$ ; $y'(0)=\lambda+\mu=1$, donc $\lambda=1$ : $y=\big(\frac{x^2}2+x\big)e^x$.""",
r"""> **Vérification — Méthode du changement de fonction.** Avec $y=ze^x$, l'équation devient $z''=1$, donc $z=\frac{x^2}2+\lambda x+\mu$ ✓.""",
r"y=\Big(\frac{x^2}2+\lambda x+\mu\Big)e^x,\qquad y=\Big(\frac{x^2}2+x\Big)e^x"),
r"""Racine double $1$ : homogène $(\lambda x+\mu)e^x$, particulière $\frac{x^2}2e^x$ ; conditions initiales : $y=\big(\frac{x^2}2+x\big)e^x$.""")
cc()

# 10 ---------------------------------------------------------------- Réduction 3x3
ex('n-cc-red3', 'Maths', 'Réduction', 1, 'Diagonaliser et puissances de J − I', 20, r"""
Soit $A=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}$ et $J$ la matrice $3\times3$ dont tous les coefficients valent $1$.

1. Calculer $J^2$ et exprimer $A$ en fonction de $J$ et $I_3$.
2. Déterminer les valeurs propres et les sous-espaces propres de $A$. $A$ est-elle diagonalisable ?
3. Calculer $A^n$ pour $n\in\mathbb N$.
""", r"""Que vaut $J^2$ ? Quel polynôme annule alors $J$, et donc $A$ ?""",
r"""$J^2=3J$, et $A=J-I_3$. Un polynôme annulateur scindé à racines simples donne la diagonalisabilité ; le binôme de Newton s'applique car $J$ et $I_3$ commutent.""",
r"""Valeurs propres de $J$ : $3$ et $0$, donc celles de $A$ : $2$ et $-1$. $A^n=(-1)^nI_3+\frac{2^n-(-1)^n}{3}J$.""",
C(r"Une matrice symétrique très structurée : l'écrire à l'aide de $J$ simplifie tout.",
r"""> **Théorème — Critère.** Une matrice est diagonalisable si et seulement si elle annule un polynôme scindé à racines simples.

> **Théorème — Binôme de Newton.** $(M+N)^n=\sum\binom nkM^kN^{n-k}$ si $M$ et $N$ commutent.""",
r"Utiliser $J^2=3J$, en déduire un annulateur de $A$, puis le binôme.",
r"""**4.1 $J$.** $J^2=3J$ et $A=J-I_3$.

**4.2 Éléments propres.** $J^2-3J=0$ : $J$ annule $X(X-3)$, donc $A=J-I_3$ annule $(X+1)(X-2)$, scindé à racines simples : $A$ est diagonalisable, de valeurs propres dans $\{-1,2\}$. $E_2(A)=\ker(J-3I)=\operatorname{Vect}\big((1,1,1)\big)$ ; $E_{-1}(A)=\ker J=\{x+y+z=0\}$, de dimension $2$.

**4.3 Puissances.** Pour $k\ge1$, $J^k=3^{k-1}J$. Par le binôme ($J$ et $-I_3$ commutent) :
$$A^n=(-1)^nI_3+\sum_{k=1}^n\binom nk3^{k-1}(-1)^{n-k}J=(-1)^nI_3+\frac{(3-1)^n-(-1)^n}{3}J.$$""",
r"""> **Vérification — $n=1$ et $n=2$.** $n=1$ : $-I_3+J=A$ ✓. $n=2$ : $I_3+J$, et directement $A^2=\begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix}$ ✓.""",
r"\operatorname{Sp}(A)=\{2,-1\},\quad\dim E_{-1}=2,\quad A^n=(-1)^nI_3+\frac{2^n-(-1)^n}3J"),
r"""$A=J-I_3$ avec $J^2=3J$ : $A$ annule $(X+1)(X-2)$, diagonalisable, $E_2=\operatorname{Vect}(1,1,1)$, $E_{-1}=\{x+y+z=0\}$ ; binôme : $A^n=(-1)^nI_3+\frac{2^n-(-1)^n}{3}J$.""")
cc()

# 11 ---------------------------------------------------------------- Matrice J en dimension n
ex('n-cc-matJ', 'Maths', 'Réduction', 1, 'La matrice dont tous les coefficients valent 1', 15, r"""
Soit $n\ge2$ et $J\in\mathcal M_n(\mathbb R)$ la matrice dont tous les coefficients valent $1$.

1. Calculer $J^2$ et le rang de $J$.
2. Montrer que $J$ est diagonalisable, et donner ses valeurs propres avec leurs multiplicités.
3. En déduire le polynôme caractéristique et le déterminant de $J+\lambda I_n$ pour $\lambda\in\mathbb R$.
""", r"""Que valent les colonnes de $J$ ? Et que vaut $J$ appliquée au vecteur $(1,\dots,1)$ ?""",
r"""$J^2=nJ$ fournit un polynôme annulateur scindé à racines simples ; le rang donne la dimension du noyau.""",
r"""$J$ est semblable à $\mathrm{diag}(n,0,\dots,0)$, donc $J+\lambda I_n$ est semblable à $\mathrm{diag}(n+\lambda,\lambda,\dots,\lambda)$.""",
C(r"Une matrice de rang $1$ : son spectre se lit sur la trace et le rang.",
r"""> **Théorème — Critère.** Annulateur scindé à racines simples ⇔ diagonalisable.

> **Théorème du rang.** $\dim\ker J=n-\operatorname{rg}J$.""",
r"Annulateur, rang, puis translation du spectre.",
r"""**4.1 Calculs.** Chaque coefficient de $J^2$ vaut $\sum_{k=1}^n1\cdot1=n$, donc $J^2=nJ$. Toutes les colonnes sont égales et non nulles : $\operatorname{rg}J=1$.

**4.2 Diagonalisation.** $J$ annule $X(X-n)$, scindé à racines simples ($n\ne0$) : $J$ est diagonalisable, de valeurs propres dans $\{0,n\}$. $\dim\ker J=n-1$ : $0$ est de multiplicité $n-1$. La trace vaut $n$, donc $n$ est valeur propre simple, de vecteur propre $(1,\dots,1)$.

**4.3 Conséquences.** $\chi_J=X^{n-1}(X-n)$. $J+\lambda I_n$ est semblable à $\mathrm{diag}(n+\lambda,\lambda,\dots,\lambda)$, donc $\det(J+\lambda I_n)=(n+\lambda)\lambda^{n-1}$.""",
r"""> **Vérification — $n=2$, $\lambda=1$.** $\det\begin{pmatrix}2&1\\1&2\end{pmatrix}=3=(2+1)\cdot1$ ✓.""",
r"J^2=nJ,\quad\operatorname{Sp}(J)=\{0\ (n-1\ \text{fois}),\ n\},\quad\det(J+\lambda I_n)=(n+\lambda)\lambda^{n-1}"),
r"""$J^2=nJ$, $\operatorname{rg}J=1$ : diagonalisable, $0$ de multiplicité $n-1$ et $n$ simple ; $\det(J+\lambda I_n)=(n+\lambda)\lambda^{n-1}$.""")
cc()

# 12 ---------------------------------------------------------------- Non diagonalisable 2x2
ex('n-cc-red2', 'Maths', 'Réduction', 1, 'Une matrice non diagonalisable et ses puissances', 15, r"""
Soit $A=\begin{pmatrix}1&1\\-1&3\end{pmatrix}$.

1. Calculer le polynôme caractéristique de $A$. $A$ est-elle diagonalisable ?
2. On pose $N=A-2I_2$. Calculer $N^2$.
3. En déduire $A^n$ pour $n\in\mathbb N$.
""", r"""Combien $A$ a-t-elle de valeurs propres ? Si elle était diagonalisable avec une seule valeur propre, à quoi serait-elle égale ?""",
r"""Une matrice diagonalisable de spectre $\{\lambda\}$ est égale à $\lambda I_n$. Pour les puissances, binôme de Newton avec une matrice nilpotente.""",
r"""$N^2=0$, donc $A^n=(2I_2+N)^n=2^nI_2+n2^{n-1}N$.""",
C(r"Une matrice $2\times2$ à valeur propre double, non diagonalisable : on l'écrit comme scalaire plus nilpotente.",
r"""> **Propriété — Valeur propre unique.** Si $A$ est diagonalisable et $\operatorname{Sp}(A)=\{\lambda\}$, alors $A=\lambda I_n$.

> **Théorème — Binôme de Newton** pour des matrices qui commutent.""",
r"Polynôme caractéristique, nilpotence de $A-2I_2$, binôme.",
r"""**4.1 Spectre.** $\chi_A=X^2-\operatorname{tr}(A)X+\det A=X^2-4X+4=(X-2)^2$. Si $A$ était diagonalisable, elle vaudrait $2I_2$ : ce n'est pas le cas. $A$ n'est pas diagonalisable.

**4.2 Nilpotence.** $N=\begin{pmatrix}-1&1\\-1&1\end{pmatrix}$ et $N^2=\begin{pmatrix}1-1&-1+1\\1-1&-1+1\end{pmatrix}=0$.

**4.3 Puissances.** $2I_2$ et $N$ commutent, et $N^k=0$ pour $k\ge2$ :
$$A^n=2^nI_2+n2^{n-1}N=2^{n-1}\begin{pmatrix}2-n&n\\-n&2+n\end{pmatrix}.$$""",
r"""> **Vérification — $n=1$.** $2^0\begin{pmatrix}1&1\\-1&3\end{pmatrix}=A$ ✓ ; $n=2$ : $A^2=\begin{pmatrix}0&4\\-4&8\end{pmatrix}$ et $2\begin{pmatrix}0&2\\-2&4\end{pmatrix}$ ✓.""",
r"\chi_A=(X-2)^2,\ A\ \text{non diagonalisable},\quad A^n=2^{n-1}\begin{pmatrix}2-n&n\\-n&2+n\end{pmatrix}"),
r"""$\chi_A=(X-2)^2$ et $A\ne2I_2$ : non diagonalisable ; $N=A-2I_2$ vérifie $N^2=0$, d'où $A^n=2^nI_2+n2^{n-1}N$.""")
cc()

# 13 ---------------------------------------------------------------- Gram-Schmidt
ex('n-cc-gram', 'Maths', 'Algèbre euclidienne', 1, 'Gram-Schmidt sur ℝ₂[X] et distance de X³', 20, r"""
Sur $\mathbb R[X]$, on pose $\langle P,Q\rangle=\displaystyle\int_{-1}^1P(t)Q(t)\,\mathrm dt$.

1. Montrer que c'est un produit scalaire.
2. Orthonormaliser la base $(1,X,X^2)$ de $\mathbb R_2[X]$ par le procédé de Gram-Schmidt.
3. Calculer la distance de $X^3$ à $\mathbb R_2[X]$.
""", r"""Quelles intégrales sont nulles par imparité ? Cela simplifie beaucoup l'orthonormalisation.""",
r"""Gram-Schmidt : $\varepsilon_k$ est le normalisé de $e_k-\sum_{i<k}\langle e_k,\varepsilon_i\rangle\varepsilon_i$. Distance : $d^2=\|X^3\|^2-\|p(X^3)\|^2$ où $p$ est le projeté orthogonal.""",
r"""$\langle X^3,1\rangle=\langle X^3,X^2\rangle=0$ par imparité : le projeté de $X^3$ est $\frac{\langle X^3,X\rangle}{\|X\|^2}X=\frac35X$.""",
C(r"Un produit scalaire intégral sur un intervalle symétrique : l'imparité annule de nombreux produits scalaires.",
r"""> **Théorème — Gram-Schmidt.** D'une famille libre on tire une famille orthonormée engendrant les mêmes sous-espaces successifs.

> **Propriété — Distance.** $d(x,F)^2=\|x\|^2-\|p_F(x)\|^2$, avec $p_F(x)=\sum\langle x,\varepsilon_i\rangle\varepsilon_i$ en base orthonormée.""",
r"Vérifier les axiomes, orthonormaliser, projeter.",
r"""**4.1 Produit scalaire.** Bilinéaire, symétrique, positif ; si $\int_{-1}^1P^2=0$, alors $P^2$ (continue, positive) est nulle sur $[-1,1]$, donc $P$ a une infinité de racines et $P=0$.

**4.2 Orthonormalisation.** $\|1\|^2=2$ : $\varepsilon_0=\frac1{\sqrt2}$. $\langle X,1\rangle=0$ et $\|X\|^2=\frac23$ : $\varepsilon_1=\sqrt{\frac32}\,X$. $\langle X^2,\varepsilon_1\rangle=0$ et $\langle X^2,1\rangle=\frac23$, donc $X^2-\frac{\langle X^2,1\rangle}{\|1\|^2}=X^2-\frac13$, de norme au carré $\int_{-1}^1\big(t^4-\frac{2t^2}3+\frac19\big)\mathrm dt=\frac25-\frac49+\frac29=\frac8{45}$ : $\varepsilon_2=\sqrt{\frac{45}8}\big(X^2-\frac13\big)$.

**4.3 Distance.** Par imparité, seul $\langle X^3,\varepsilon_1\rangle$ est non nul : $\langle X^3,X\rangle=\frac25$, donc $p(X^3)=\frac{2/5}{2/3}X=\frac35X$. Alors $d^2=\|X^3\|^2-\|\tfrac35X\|^2=\frac27-\frac9{25}\cdot\frac23=\frac27-\frac6{25}=\frac8{175}$.""",
r"""> **Vérification — Orthogonalité.** $\big\langle X^3-\tfrac35X,X\big\rangle=\frac25-\frac35\cdot\frac23=0$ ✓.""",
r"\Big(\tfrac1{\sqrt2},\ \sqrt{\tfrac32}X,\ \sqrt{\tfrac{45}8}\big(X^2-\tfrac13\big)\Big),\qquad d\big(X^3,\mathbb R_2[X]\big)=\sqrt{\tfrac8{175}}"),
r"""Imparité : $\varepsilon_0=\frac1{\sqrt2}$, $\varepsilon_1=\sqrt{3/2}\,X$, $\varepsilon_2=\sqrt{45/8}(X^2-\frac13)$ ; projeté de $X^3$ : $\frac35X$ ; $d^2=\frac27-\frac6{25}=\frac8{175}$.""")
cc()

# 14 ---------------------------------------------------------------- Projection orthogonale dans R3
ex('n-cc-proj', 'Maths', 'Algèbre euclidienne', 1, 'Projection et symétrie orthogonales sur un plan de ℝ³', 15, r"""
Dans $\mathbb R^3$ euclidien canonique, soit le plan $P:\ x+y+z=0$.

1. Déterminer la matrice $M$ (dans la base canonique) de la projection orthogonale sur $P$.
2. En déduire la matrice $S$ de la symétrie orthogonale par rapport à $P$, et vérifier que $S$ est symétrique et orthogonale.
3. Calculer la distance du point $(1,2,3)$ au plan $P$.
""", r"""Quel est un vecteur normal à $P$ ? Comment s'écrit la projection d'un vecteur sur la droite qu'il engendre ?""",
r"""$p_P(x)=x-\langle x,n\rangle n$ avec $n$ unitaire normal ; $s=2p_P-\mathrm{Id}$ ; distance à un plan : $\frac{|\langle x,n\rangle|}{\|n\|}$ avec $n$ quelconque.""",
r"""Avec $n=\frac1{\sqrt3}(1,1,1)$ : $M=I_3-\frac13J$ où $J$ a tous ses coefficients égaux à $1$, puis $S=I_3-\frac23J$.""",
C(r"Projection orthogonale sur un hyperplan donné par une équation : on passe par le vecteur normal.",
r"""> **Propriété — Projection sur un hyperplan.** Si $n$ est unitaire et $H=n^\perp$, $p_H(x)=x-\langle x,n\rangle n$, et $d(x,H)=|\langle x,n\rangle|$.

> **Propriété — Symétrie orthogonale.** $s=2p-\mathrm{Id}$ ; sa matrice en base orthonormée est symétrique et orthogonale.""",
r"Vecteur normal unitaire, projection, symétrie, distance.",
r"""**4.1 Projection.** $n=\frac1{\sqrt3}(1,1,1)$ est unitaire et normal à $P$. La matrice de $x\mapsto\langle x,n\rangle n$ est $n\,{}^tn=\frac13J$. Donc $M=I_3-\frac13J=\frac13\begin{pmatrix}2&-1&-1\\-1&2&-1\\-1&-1&2\end{pmatrix}$.

**4.2 Symétrie.** $S=2M-I_3=I_3-\frac23J=\frac13\begin{pmatrix}1&-2&-2\\-2&1&-2\\-2&-2&1\end{pmatrix}$. ${}^tS=S$, et $S^2=I_3-\frac43J+\frac49J^2=I_3-\frac43J+\frac43J=I_3$ (car $J^2=3J$) : $S\,{}^tS=I_3$.

**4.3 Distance.** $d=|\langle(1,2,3),n\rangle|=\frac{6}{\sqrt3}=2\sqrt3$.""",
r"""> **Vérification — Images.** $M(1,1,1)=0$ (vecteur normal) ✓ ; $M(1,-1,0)=(1,-1,0)$ (vecteur du plan) ✓.""",
r"M=I_3-\tfrac13J,\qquad S=I_3-\tfrac23J,\qquad d\big((1,2,3),P\big)=2\sqrt3"),
r"""$n=\frac{1}{\sqrt3}(1,1,1)$ : $M=I_3-\frac13J$, $S=2M-I_3=I_3-\frac23J$ (symétrique, $S^2=I_3$) ; distance $\frac{6}{\sqrt3}=2\sqrt3$.""")
cc()

# 15 ---------------------------------------------------------------- Dé jusqu'au 6
ex('n-cc-de6', 'Maths', 'Probabilités', 1, 'Lancer un dé jusqu’au premier 6', 15, r"""
On lance un dé équilibré jusqu'à obtenir un $6$. On note $N$ le nombre de lancers effectués.

1. Reconnaître la loi de $N$ ; donner $E(N)$ et $V(N)$.
2. Calculer la probabilité que $N$ soit pair.
3. Calculer $P(N>10)$ et $P(N>15\mid N>5)$.
""", r"""Que signifie $(N=k)$ en termes de lancers ? Et $(N>k)$ ?""",
r"""$N$ suit une loi géométrique ; pour 2, somme d'une série géométrique sur les indices pairs ; pour 3, absence de mémoire.""",
r"""$P(N\text{ pair})=\sum_{k\ge1}\big(\tfrac56\big)^{2k-1}\tfrac16$ ; $P(N>k)=\big(\tfrac56\big)^k$.""",
C(r"Temps d'attente du premier succès : la loi géométrique et ses propriétés.",
r"""> **Définition — Loi géométrique $\mathcal G(p)$.** $P(N=k)=(1-p)^{k-1}p$ pour $k\ge1$ ; $E(N)=\frac1p$, $V(N)=\frac{1-p}{p^2}$ ; $P(N>k)=(1-p)^k$.

> **Propriété — Absence de mémoire.** $P(N>n+k\mid N>n)=P(N>k)$.""",
r"Reconnaître la loi, sommer sur les pairs, utiliser la survie.",
r"""**4.1 Loi.** $(N=k)$ : $k-1$ échecs puis un succès, lancers indépendants : $N\sim\mathcal G(\frac16)$, $E(N)=6$, $V(N)=\frac{5/6}{1/36}=30$.

**4.2 Parité.** Avec $q=\frac56$ : $P(N\text{ pair})=\sum_{k\ge1}q^{2k-1}p=\frac{pq}{1-q^2}=\frac{q}{1+q}=\frac{5/6}{11/6}=\frac5{11}$.

**4.3 Survie.** $P(N>10)=\big(\frac56\big)^{10}\approx0{,}16$. Par absence de mémoire, $P(N>15\mid N>5)=P(N>10)=\big(\frac56\big)^{10}$.""",
r"""> **Vérification — Parité.** $P(N\text{ impair})=\sum q^{2k-2}p=\frac{p}{1-q^2}=\frac1{1+q}=\frac6{11}$, et $\frac5{11}+\frac6{11}=1$ ✓.""",
r"N\sim\mathcal G(\tfrac16),\ E(N)=6,\ V(N)=30,\quad P(N\ \text{pair})=\tfrac5{11},\quad P(N>15\mid N>5)=\big(\tfrac56\big)^{10}"),
r"""$N\sim\mathcal G(\frac16)$ : $E=6$, $V=30$ ; $P(N$ pair$)=\frac{q}{1+q}=\frac5{11}$ ; $P(N>10)=(\frac56)^{10}$, égale à $P(N>15\mid N>5)$ par absence de mémoire.""")
cc()

# 16 ---------------------------------------------------------------- Poisson
ex('n-cc-poisson', 'Maths', 'Probabilités', 1, 'Espérance de 1/(1+X) pour une loi de Poisson', 15, r"""
Soit $X\sim\mathcal P(\lambda)$ avec $\lambda>0$.

1. Rappeler $E(X)$ et $V(X)$, en les retrouvant à l'aide de $E\big(X(X-1)\big)$.
2. Montrer que $\frac1{1+X}$ admet une espérance et la calculer.
3. Calculer la probabilité que $X$ soit pair.
""", r"""Dans $\sum\frac{1}{k+1}\cdot\frac{\lambda^k}{k!}$, peut-on faire apparaître $(k+1)!$ ?""",
r"""Formule de transfert ; pour la parité, utiliser $\frac{1+(-1)^k}2$ et les sommes $\sum\frac{\lambda^k}{k!}$, $\sum\frac{(-\lambda)^k}{k!}$.""",
r"""$\frac{1}{k+1}\cdot\frac{\lambda^k}{k!}=\frac1\lambda\cdot\frac{\lambda^{k+1}}{(k+1)!}$ ; $P(X\text{ pair})=\frac{1+e^{-2\lambda}}2$.""",
C(r"Calculs d'espérances pour une loi de Poisson : on reconnaît chaque fois la série de l'exponentielle.",
r"""> **Définition — Loi de Poisson.** $P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}$, $k\in\mathbb N$ ; $E(X)=V(X)=\lambda$.

> **Théorème — Formule de transfert.** $E(f(X))=\sum f(k)P(X=k)$ sous réserve de convergence absolue.""",
r"Transfert, décalage d'indice, parité par $\frac{1+(-1)^k}2$.",
r"""**4.1 Moments.** $E(X)=\sum_{k\ge1}e^{-\lambda}\frac{\lambda^k}{(k-1)!}=\lambda$ ; $E(X(X-1))=\sum_{k\ge2}e^{-\lambda}\frac{\lambda^k}{(k-2)!}=\lambda^2$, d'où $E(X^2)=\lambda^2+\lambda$ et $V(X)=\lambda$.

**4.2 Espérance de $\frac1{1+X}$.** $0\le\frac1{1+X}\le1$ : l'espérance existe, et
$$E\Big(\frac1{1+X}\Big)=\sum_{k\ge0}\frac{e^{-\lambda}}{k+1}\cdot\frac{\lambda^k}{k!}=\frac{e^{-\lambda}}\lambda\sum_{k\ge0}\frac{\lambda^{k+1}}{(k+1)!}=\frac{e^{-\lambda}}\lambda(e^\lambda-1)=\frac{1-e^{-\lambda}}\lambda.$$

**4.3 Parité.** $P(X\text{ pair})=\sum_ke^{-\lambda}\frac{\lambda^k}{k!}\cdot\frac{1+(-1)^k}2=\frac{e^{-\lambda}}2(e^\lambda+e^{-\lambda})=\frac{1+e^{-2\lambda}}2$.""",
r"""> **Vérification — Petites valeurs de $\lambda$.** Pour $\lambda\to0$, $X=0$ presque sûrement : $E\big(\frac1{1+X}\big)\to1$ et $\frac{1-e^{-\lambda}}\lambda\to1$ ✓ ; $P(X$ pair$)\to1$ ✓.""",
r"E(X)=V(X)=\lambda,\qquad E\Big(\frac1{1+X}\Big)=\frac{1-e^{-\lambda}}\lambda,\qquad P(X\ \text{pair})=\frac{1+e^{-2\lambda}}2"),
r"""$E(X(X-1))=\lambda^2$ donne $V(X)=\lambda$ ; $E(\frac1{1+X})=\frac{e^{-\lambda}}{\lambda}(e^\lambda-1)$ ; $P(X$ pair$)=\frac{1+e^{-2\lambda}}{2}$.""")
cc()

# 17 ---------------------------------------------------------------- Binomiale et Tchebychev
ex('n-cc-binom', 'Maths', 'Probabilités', 1, 'Somme de binomiales et sondage', 20, r"""
1. Soient $X\sim\mathcal B(n,p)$ et $Y\sim\mathcal B(m,p)$ indépendantes. À l'aide des fonctions génératrices, déterminer la loi de $X+Y$.
2. On sonde $n$ personnes ; chacune répond « oui » avec probabilité $p$, indépendamment. Soit $F_n=\frac{S_n}n$ la fréquence de « oui ». Montrer que $P(|F_n-p|\ge\varepsilon)\le\dfrac1{4n\varepsilon^2}$.
3. Combien de personnes faut-il sonder pour que la fréquence soit à moins de $0{,}01$ de $p$ avec une probabilité au moins $0{,}95$ ?
""", r"""Que vaut $G_X(t)=E(t^X)$ pour une loi binomiale ? Et comment se comporte la fonction génératrice d'une somme de variables indépendantes ?""",
r"""$G_{X+Y}=G_XG_Y$ par indépendance, et la fonction génératrice caractérise la loi. Pour 2 : inégalité de Bienaymé-Tchebychev, et $p(1-p)\le\frac14$.""",
r"""$G_X(t)=(1-p+pt)^n$ ; $V(F_n)=\frac{p(1-p)}n$ ; pour 3, on veut $\frac1{4n(0{,}01)^2}\le0{,}05$.""",
C(r"Stabilité de la loi binomiale par somme indépendante, puis estimation d'une proportion par Bienaymé-Tchebychev.",
r"""> **Propriété — Fonction génératrice.** $G_X(t)=E(t^X)$ caractérise la loi ; si $X$ et $Y$ sont indépendantes, $G_{X+Y}=G_XG_Y$.

> **Théorème — Bienaymé-Tchebychev.** $P(|Z-E(Z)|\ge\varepsilon)\le\frac{V(Z)}{\varepsilon^2}$.""",
r"Produit des fonctions génératrices, puis variance de la fréquence.",
r"""**4.1 Somme.** $G_X(t)=\sum\binom nkp^k(1-p)^{n-k}t^k=(1-p+pt)^n$ ; de même $G_Y(t)=(1-p+pt)^m$. Par indépendance, $G_{X+Y}(t)=(1-p+pt)^{n+m}$ : $X+Y\sim\mathcal B(n+m,p)$.

**4.2 Sondage.** $S_n\sim\mathcal B(n,p)$, donc $E(F_n)=p$ et $V(F_n)=\frac{p(1-p)}n\le\frac1{4n}$ (car $p(1-p)\le\frac14$). Par Bienaymé-Tchebychev : $P(|F_n-p|\ge\varepsilon)\le\frac{1}{4n\varepsilon^2}$.

**4.3 Taille.** Il suffit que $\frac1{4n\cdot10^{-4}}\le0{,}05$, soit $n\ge\frac{10^4}{4\times0{,}05}=50\,000$.""",
r"""> **Vérification — Ordre de grandeur.** Les instituts sondent environ $1\,000$ personnes pour une précision de $3$ points : Tchebychev est une majoration grossière, mais elle ne suppose rien sur $p$ ✓.""",
r"X+Y\sim\mathcal B(n+m,p),\qquad P(|F_n-p|\ge\varepsilon)\le\frac{1}{4n\varepsilon^2},\qquad n\ge50\,000"),
r"""$G_{X+Y}=(1-p+pt)^{n+m}$, donc $X+Y\sim\mathcal B(n+m,p)$ ; $V(F_n)\le\frac1{4n}$ et Tchebychev ; $n\ge50\,000$ suffit.""")
cc()

# 18 ---------------------------------------------------------------- Polynôme et somme des carrés
ex('n-cc-poly', 'Maths', 'Polynômes', 1, 'P(X+1) − P(X) = X² et somme des carrés', 15, r"""
1. Montrer qu'il existe un unique polynôme $P\in\mathbb R[X]$ tel que $P(X+1)-P(X)=X^2$ et $P(0)=0$, et le déterminer.
2. En déduire une expression de $\sum_{k=0}^nk^2$.
""", r"""Si $\deg P=d\ge1$, quel est le degré de $P(X+1)-P(X)$ ? Quel degré doit donc avoir $P$ ?""",
r"""Le terme dominant de $P(X+1)-P(X)$ est $d\,a_dX^{d-1}$. Identifier ensuite les coefficients ; pour la somme, télescoper.""",
r"""$P=\frac{X^3}3-\frac{X^2}2+\frac X6$, et $\sum_{k=0}^nk^2=\sum_{k=0}^n\big(P(k+1)-P(k)\big)=P(n+1)$.""",
C(r"Une équation fonctionnelle polynomiale, outil classique pour calculer des sommes de puissances.",
r"""> **Propriété — Degré de la différence.** Si $\deg P=d\ge1$ et de coefficient dominant $a_d$, alors $P(X+1)-P(X)$ est de degré $d-1$, de coefficient dominant $da_d$.

> **Propriété — Télescopage.** $\sum_{k=0}^n\big(u_{k+1}-u_k\big)=u_{n+1}-u_0$.""",
r"Degré, identification, puis télescopage.",
r"""**4.1 Degré.** Il faut $\deg P=3$. Écrivons $P=aX^3+bX^2+cX$ (car $P(0)=0$). Alors $P(X+1)-P(X)=a(3X^2+3X+1)+b(2X+1)+c=3aX^2+(3a+2b)X+(a+b+c)$.

**4.2 Identification.** $3a=1$, $3a+2b=0$, $a+b+c=0$ : $a=\frac13$, $b=-\frac12$, $c=\frac16$. Solution unique : $P=\frac{X^3}3-\frac{X^2}2+\frac X6=\frac{X(X-1)(2X-1)}6$.

**4.3 Somme.** $\sum_{k=0}^nk^2=\sum_{k=0}^n\big(P(k+1)-P(k)\big)=P(n+1)-P(0)=\frac{n(n+1)(2n+1)}6$.""",
r"""> **Vérification — $n=2$.** $0+1+4=5$ et $\frac{2\cdot3\cdot5}6=5$ ✓.""",
r"P=\frac{X(X-1)(2X-1)}6,\qquad\sum_{k=0}^nk^2=\frac{n(n+1)(2n+1)}6"),
r"""Degré $3$, identification : $P=\frac{X^3}{3}-\frac{X^2}{2}+\frac{X}{6}$ ; télescopage : $\sum_{k=0}^n k^2=P(n+1)=\frac{n(n+1)(2n+1)}6$.""")
cc()

# 19 ---------------------------------------------------------------- Série de fonctions
ex('n-cc-sdf', 'Maths', 'Séries de fonctions', 1, 'Étude de f(x) = Σ 1/(n² + x²)', 20, r"""
Pour $x\in\mathbb R$, on pose $f(x)=\displaystyle\sum_{n\ge1}\frac{1}{n^2+x^2}$.

1. Montrer que $f$ est définie et continue sur $\mathbb R$, et donner $f(0)$.
2. Montrer que $f$ est de classe $\mathcal C^1$ sur $\mathbb R$ et étudier ses variations.
3. Déterminer $\lim_{x\to+\infty}f(x)$.
""", r"""Quelle majoration de $\frac1{n^2+x^2}$ ne dépend pas de $x$ ? Et pour la dérivée $\frac{-2x}{(n^2+x^2)^2}$ ?""",
r"""Convergence normale sur $\mathbb R$ pour la continuité et pour la dérivabilité terme à terme. Pour majorer la dérivée, utiliser $n^2+x^2\ge2n|x|$.""",
r"""$\frac{2|x|}{(n^2+x^2)^2}\le\frac{2|x|}{2n|x|(n^2+x^2)}\le\frac1{n^3}$. Pour la limite, théorème de la double limite (chaque terme tend vers $0$).""",
C(r"Une série de fonctions dont on étudie la régularité et le comportement à l'infini par convergence normale.",
r"""> **Théorème — Convergence normale.** Si $\sum\|f_n\|_\infty<+\infty$, la série converge uniformément ; la somme de fonctions continues est continue.

> **Théorème — Dérivation terme à terme.** Si $\sum f_n$ converge simplement et $\sum f_n'$ uniformément, la somme est $\mathcal C^1$.

> **Théorème — Double limite.** Avec convergence uniforme, on peut intervertir limite et somme.""",
r"Normes infinies, dérivées, double limite.",
r"""**4.1 Continuité.** $0<\frac1{n^2+x^2}\le\frac1{n^2}$ : convergence normale sur $\mathbb R$, $f$ est continue, et $f(0)=\sum\frac1{n^2}=\frac{\pi^2}6$.

**4.2 Classe $\mathcal C^1$.** $f_n'(x)=\frac{-2x}{(n^2+x^2)^2}$. Pour $x\ne0$, $n^2+x^2\ge2n|x|$, d'où $|f_n'(x)|\le\frac{2|x|}{2n|x|(n^2+x^2)}=\frac1{n(n^2+x^2)}\le\frac1{n^3}$ (et $f_n'(0)=0$). Convergence normale de $\sum f_n'$ : $f$ est $\mathcal C^1$ et $f'(x)=\sum\frac{-2x}{(n^2+x^2)^2}$, du signe de $-x$. $f$ est paire, croissante sur $]-\infty,0]$ et décroissante sur $[0,+\infty[$, de maximum $\frac{\pi^2}6$.

**4.3 Limite.** Chaque terme tend vers $0$ en $+\infty$ et la convergence est uniforme : par double limite, $f(x)\to0$.""",
r"""> **Vérification — Ordre de grandeur.** Par comparaison série-intégrale, $f(x)\approx\int_0^{+\infty}\frac{\mathrm dt}{t^2+x^2}=\frac{\pi}{2x}$ pour $x$ grand, qui tend bien vers $0$ ✓.""",
r"f\in\mathcal C^1(\mathbb R),\quad f(0)=\frac{\pi^2}6,\quad f\ \text{paire, décroissante sur}\ [0,+\infty[,\quad\lim_{+\infty}f=0"),
r"""$\frac1{n^2+x^2}\le\frac1{n^2}$ : continuité, $f(0)=\frac{\pi^2}{6}$ ; $|f_n'|\le\frac1{n^3}$ via $n^2+x^2\ge2n|x|$ : $\mathcal C^1$, décroissante sur $[0,\infty[$ ; double limite : $f\to0$.""")
cc()

# 20 ---------------------------------------------------------------- Norme sur R_n[X]
ex('n-cc-norme', 'Maths', 'Topologie & convexité', 1, 'Une norme sur ℝₙ[X] par les valeurs aux entiers', 15, r"""
Pour $P\in\mathbb R_n[X]$, on pose $N(P)=\sum_{k=0}^n|P(k)|$.

1. Montrer que $N$ est une norme sur $\mathbb R_n[X]$.
2. $N$ est-elle une norme sur $\mathbb R_{n+1}[X]$ ?
3. Montrer qu'il existe $C>0$ tel que $\Big|\displaystyle\int_0^1P(t)\,\mathrm dt\Big|\le C\,N(P)$ pour tout $P\in\mathbb R_n[X]$.
""", r"""Quel axiome de la norme pose vraiment question ? Combien de racines peut avoir un polynôme non nul de degré $\le n$ ?""",
r"""Séparation : un polynôme de degré $\le n$ qui s'annule en $n+1$ points est nul. Pour 3 : en dimension finie, toute forme linéaire est continue pour toute norme.""",
r"""Contre-exemple pour 2 : $\prod_{k=0}^n(X-k)$. Pour 3, $P\mapsto\int_0^1P$ est linéaire sur un espace de dimension finie.""",
C(r"Construire une norme à partir de valeurs ponctuelles, et utiliser l'équivalence des normes en dimension finie.",
r"""> **Définition — Norme.** Séparation, homogénéité, inégalité triangulaire.

> **Théorème — Dimension finie.** Toutes les normes sont équivalentes et toute application linéaire est continue : $|\ell(x)|\le C\|x\|$.""",
r"Vérifier les axiomes, trouver le contre-exemple, appliquer le théorème de dimension finie.",
r"""**4.1 Norme.** Homogénéité et inégalité triangulaire viennent de celles de la valeur absolue. Si $N(P)=0$, alors $P(0)=\dots=P(n)=0$ : $P$, de degré $\le n$, a $n+1$ racines distinctes, donc $P=0$.

**4.2 Sur $\mathbb R_{n+1}[X]$.** $Q=\prod_{k=0}^n(X-k)$ est non nul, de degré $n+1$, et $N(Q)=0$ : la séparation échoue, $N$ n'est pas une norme.

**4.3 Continuité.** $\ell:P\mapsto\int_0^1P$ est linéaire sur l'espace de dimension finie $\mathbb R_n[X]$, donc continue pour la norme $N$ : il existe $C>0$ avec $|\ell(P)|\le C\,N(P)$.""",
r"""> **Vérification — $n=0$.** $N(P)=|P(0)|$ pour $P$ constant, et $\int_0^1P=P(0)$ : $C=1$ convient ✓.""",
r"N\ \text{norme sur}\ \mathbb R_n[X],\ \text{pas sur}\ \mathbb R_{n+1}[X],\qquad\Big|\int_0^1P\Big|\le C\,N(P)"),
r"""Séparation : $n+1$ racines pour un polynôme de degré $\le n$ ; contre-exemple $\prod_{k=0}^n(X-k)$ ; en dimension finie, toute forme linéaire est continue.""")
cc()
