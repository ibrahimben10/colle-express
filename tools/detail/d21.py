D = {}

D['x-s-1'] = r"""
**1. Signe de $f(x)-x$ près de 0.** Écrivons $f(x)=x-ax^\alpha\big(1+\varepsilon(x)\big)$ avec $\varepsilon(x)\to0$ quand $x\to0^+$. Il existe $\eta\in]0,c]$ tel que $|\varepsilon(x)|\le\frac12$ et $ax^{\alpha-1}\cdot\frac32<1$ pour $0<x\le\eta$. Alors, pour $0<x\le\eta$ :
$$f(x)-x=-ax^\alpha(1+\varepsilon(x))\le-\frac a2x^\alpha<0,\qquad f(x)=x\big(1-ax^{\alpha-1}(1+\varepsilon(x))\big)\ge x\Big(1-\frac32ax^{\alpha-1}\Big)>0.$$
Donc $0<f(x)<x$ sur $]0,\eta]$.

**1. Convergence.** Soit $u_0\in]0,\eta]$. Par récurrence, $0<u_{n+1}=f(u_n)<u_n\le\eta$. La suite $(u_n)$ est décroissante et minorée par 0 : elle converge vers $\ell\in[0,\eta]$. Par continuité de $f$, $f(\ell)=\ell$ ; comme $f(x)<x$ sur $]0,\eta]$, $\ell=0$.

**2. Choix de $\beta$.** On cherche $\beta$ tel que $u_{n+1}^\beta-u_n^\beta$ ait une limite finie non nulle. Avec $u_{n+1}=u_n\big(1-au_n^{\alpha-1}+o(u_n^{\alpha-1})\big)$ et $(1+h)^\beta=1+\beta h+o(h)$ :
$$u_{n+1}^\beta=u_n^\beta\big(1-a\beta u_n^{\alpha-1}+o(u_n^{\alpha-1})\big),\qquad u_{n+1}^\beta-u_n^\beta=-a\beta\,u_n^{\beta+\alpha-1}+o\big(u_n^{\beta+\alpha-1}\big).$$
Pour obtenir une limite finie non nulle, il faut $\beta+\alpha-1=0$, soit $\beta=1-\alpha<0$. Alors
$$u_{n+1}^\beta-u_n^\beta\xrightarrow[n\to\infty]{}-a\beta=a(\alpha-1)>0.$$

**2. Lemme de Cesàro.** Si $v_{n+1}-v_n\to L$, alors $\frac{v_n}n\to L$. Avec $v_n=u_n^\beta$ : $\frac{u_n^{1-\alpha}}n\to a(\alpha-1)$, soit $u_n^{1-\alpha}\sim a(\alpha-1)n$. En élevant à la puissance $\frac1{1-\alpha}$ (les équivalents passent aux puissances fixes) :
$$u_n\sim\big(a(\alpha-1)\,n\big)^{-\frac1{\alpha-1}}.$$

**3. Exemples.**
- $\sin x=x-\frac{x^3}6+o(x^3)$ : $a=\frac16$, $\alpha=3$, $a(\alpha-1)=\frac13$, donc $u_n\sim\big(\frac n3\big)^{-1/2}=\sqrt{\frac3n}$.
- $\ln(1+x)=x-\frac{x^2}2+o(x^2)$ : $a=\frac12$, $\alpha=2$, $a(\alpha-1)=\frac12$, donc $u_n\sim\big(\frac n2\big)^{-1}=\frac2n$.
(Pour $\sin$, $f$ va de $[0,\frac\pi2]$ dans lui-même et $0<\sin x<x$ pour tout $x>0$ : la convergence vaut pour tout $u_0\in]0,\frac\pi2]$.)
"""

D['x-s-2'] = r"""
**Remarque.** Si $a_0=b_0$, les deux suites sont constantes ; on suppose $a_0\neq b_0$.

**1. Le produit est constant.** La moyenne harmonique s'écrit $b_{n+1}=\frac2{\frac1{a_n}+\frac1{b_n}}=\frac{2a_nb_n}{a_n+b_n}$. Donc
$$a_{n+1}b_{n+1}=\frac{a_n+b_n}2\cdot\frac{2a_nb_n}{a_n+b_n}=a_nb_n=\dots=a_0b_0.$$
Posons $\ell=\sqrt{a_0b_0}$. Par récurrence immédiate, $a_n>0$ et $b_n>0$.

**1. Ordre entre les suites.**
$$a_{n+1}-b_{n+1}=\frac{a_n+b_n}2-\frac{2a_nb_n}{a_n+b_n}=\frac{(a_n+b_n)^2-4a_nb_n}{2(a_n+b_n)}=\frac{(a_n-b_n)^2}{2(a_n+b_n)}>0.$$
Donc $b_n<a_n$ pour $n\ge1$.

**1. Monotonies.** Pour $n\ge1$ : $a_{n+1}-a_n=\frac{b_n-a_n}2<0$ et $\frac1{b_{n+1}}-\frac1{b_n}=\frac12\big(\frac1{a_n}-\frac1{b_n}\big)<0$, donc $b_{n+1}>b_n$. Ainsi $(a_n)_{n\ge1}$ décroît, $(b_n)_{n\ge1}$ croît, et $b_1\le b_n<a_n\le a_1$.

**1. Adjacence.** $0<a_{n+1}-b_{n+1}=\frac{(a_n-b_n)^2}{2(a_n+b_n)}\le\frac{a_n-b_n}2$ (car $a_n-b_n<a_n+b_n$). Donc $a_n-b_n\to0$ : les suites sont adjacentes, de même limite $L>0$. En passant à la limite dans $a_nb_n=\ell^2$ : $L^2=\ell^2$, donc $L=\ell=\sqrt{a_0b_0}$ (moyenne géométrique de $a_0$ et $b_0$).

**2. Récurrence sur l'erreur.** Comme $b_n=\frac{\ell^2}{a_n}$ : $a_{n+1}=\frac12\big(a_n+\frac{\ell^2}{a_n}\big)$ (méthode de Héron pour $\sqrt{\ell^2}$). Avec $e_n=a_n-\ell>0$ ($n\ge1$) :
$$e_{n+1}=\frac{a_n^2+\ell^2-2\ell a_n}{2a_n}=\frac{(a_n-\ell)^2}{2a_n}=\frac{e_n^2}{2(\ell+e_n)}.$$
En particulier $e_{n+1}\sim\frac{e_n^2}{2\ell}$ : convergence quadratique.

**2. Linéarisation par le logarithme.** Posons $\varepsilon_n=\frac{e_n}{2\ell}$. Alors $\varepsilon_{n+1}=\varepsilon_n^2\cdot\frac\ell{\ell+e_n}$, soit $\ln\varepsilon_{n+1}=2\ln\varepsilon_n-\ln\big(1+\frac{e_n}\ell\big)$. Avec $c_n=2^{-n}\ln\varepsilon_n$ :
$$c_{n+1}-c_n=-2^{-n-1}\ln\Big(1+\frac{e_n}\ell\Big).$$
$(e_n)$ est bornée, donc ce terme est un $O(2^{-n})$ : la série $\sum(c_{n+1}-c_n)$ converge, et $c_n\to K$.

**2. Équivalent.** $K=c_n-\sum_{k\ge n}2^{-k-1}\ln\big(1+\frac{e_k}\ell\big)$, donc
$$\ln\varepsilon_n-2^nK=\sum_{k\ge n}2^{n-k-1}\ln\Big(1+\frac{e_k}\ell\Big)\le\ln\Big(1+\frac{e_n}\ell\Big)\sum_{k\ge n}2^{n-k-1}=\ln\Big(1+\frac{e_n}\ell\Big)\to0$$
($e_k$ décroît). Ainsi $\varepsilon_n\sim e^{2^nK}$. Comme $\varepsilon_n\to0$, on a $K<0$ ; posons $\theta=e^K\in]0,1[$ (il dépend de $a_0,b_0$) :
$$a_n-\ell\sim2\ell\,\theta^{2^n}.$$
Le nombre de décimales exactes double environ à chaque étape.
"""

D['x-s-3'] = r"""
**Forme exponentielle des facteurs.** $1+\frac ik$ a pour module $\sqrt{1+\frac1{k^2}}$ et pour argument $\arctan\frac1k\in]0,\frac\pi4]$ (partie réelle $1>0$). Donc
$$z_n=\prod_{k=1}^n\sqrt{1+\frac1{k^2}}\,e^{i\arctan(1/k)}=r_n\,e^{i\theta_n},\quad r_n=\prod_{k=1}^n\sqrt{1+\frac1{k^2}},\quad\theta_n=\sum_{k=1}^n\arctan\frac1k.$$

**Le module converge.** $\ln r_n=\frac12\sum_{k=1}^n\ln\big(1+\frac1{k^2}\big)$ et $0\le\ln(1+\frac1{k^2})\le\frac1{k^2}$ : la série converge, donc $\ln r_n\to\ln\rho$ et $r_n\to\rho=\prod_{k\ge1}\sqrt{1+\frac1{k^2}}>1$. (Avec la formule $\frac{\sin\pi z}{\pi z}=\prod_{k\ge1}\big(1-\frac{z^2}{k^2}\big)$ en $z=i$, admise, on trouve $\rho^2=\frac{\mathrm{sh}\,\pi}\pi$.)

**L'argument diverge à petits pas.** $\arctan\frac1k\sim\frac1k$ et $\sum\frac1k$ diverge : $\theta_n\to+\infty$. De plus $(\theta_n)$ est croissante et ses pas $\theta_{n+1}-\theta_n=\arctan\frac1{n+1}\to0$.

**Tout point du cercle est valeur d'adhérence.** Soit $\varphi\in\mathbb R$. Construisons $n_1<n_2<\cdots$ avec $|\theta_{n_j}-(\varphi+2m_j\pi)|\le\frac1j$ pour des entiers $m_j$. Supposons $n_{j-1}$ construit ; soit $N>n_{j-1}$ tel que les pas soient $\le\frac1j$ à partir du rang $N$, et $m_j$ un entier tel que $\varphi+2m_j\pi>\theta_N$. Comme $\theta_n\to+\infty$, il existe un plus grand $n\ge N$ avec $\theta_n\le\varphi+2m_j\pi$ ; alors $\theta_n\le\varphi+2m_j\pi<\theta_{n+1}\le\theta_n+\frac1j$. On pose $n_j=n$. Alors $e^{i\theta_{n_j}}=e^{i(\theta_{n_j}-2m_j\pi)}\to e^{i\varphi}$, et $z_{n_j}=r_{n_j}e^{i\theta_{n_j}}\to\rho e^{i\varphi}$.

**Il n'y en a pas d'autre.** Si $z_{\psi(n)}\to w$, alors $|w|=\lim r_{\psi(n)}=\rho$.

**Conclusion.** L'ensemble des valeurs d'adhérence de $(z_n)$ est le cercle de centre 0 et de rayon $\rho=\sqrt{\dfrac{\mathrm{sh}\,\pi}\pi}\approx1{,}92$.
"""

D['x-se-1'] = r"""
**Termes positifs : regroupement par paquets.** Pour une série à termes positifs, on peut regrouper les termes en paquets consécutifs : la série converge si et seulement si la série des paquets converge, avec la même somme. On regroupe les $p_n$ selon leur nombre de chiffres $d$.

**Dénombrement.** Un entier à $d$ chiffres sans 9 a un premier chiffre dans $\{1,\dots,8\}$ (8 choix : ni 0 ni 9) et chacun des $d-1$ autres chiffres dans $\{0,\dots,8\}$ (9 choix). Il y en a donc $8\cdot9^{d-1}$.

**Majoration de chaque paquet.** Un entier à $d$ chiffres est $\ge10^{d-1}$, donc son inverse est $\le\frac1{10^{d-1}}$. La somme $S_d$ des $\frac1{p_n}$ sur les entiers à $d$ chiffres vérifie
$$S_d\le8\cdot9^{d-1}\cdot\frac1{10^{d-1}}=8\Big(\frac9{10}\Big)^{d-1}.$$

**Conclusion.** Par sommation d'une série géométrique de raison $\frac9{10}$ :
$$\sum_{n\ge1}\frac1{p_n}=\sum_{d\ge1}S_d\le8\sum_{d\ge1}\Big(\frac9{10}\Big)^{d-1}=8\cdot\frac1{1-9/10}=80.$$
La série **converge** (série de Kempner ; sa somme vaut environ $22{,}92$).

**Morale.** La série harmonique diverge, mais il suffit d'enlever les entiers contenant un 9 pour qu'elle converge : « presque tous » les grands entiers contiennent un 9. Parmi les entiers à $d$ chiffres, la proportion de ceux qui n'en contiennent pas vaut $\frac{8\cdot9^{d-1}}{9\cdot10^{d-1}}=\frac89\big(\frac9{10}\big)^{d-1}\to0$.
"""
