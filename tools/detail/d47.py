D = {}

D['n-c-electrolyse'] = r"""
**1. Cathode.** C'est l'électrode où a lieu la réduction, reliée au pôle $-$ du générateur. L'eau y est réduite en dihydrogène ; en milieu basique, on équilibre avec $\mathrm{HO^-}$ :
$$2\,\mathrm{H_2O}+2\,e^-\to\mathrm{H_2}+2\,\mathrm{HO^-}.$$

**1. Anode.** C'est l'électrode où a lieu l'oxydation, reliée au pôle $+$. Les ions hydroxyde y sont oxydés en dioxygène :
$$4\,\mathrm{HO^-}\to\mathrm O_2+2\,\mathrm{H_2O}+4\,e^-.$$

**1. Bilan.** On multiplie la première demi-équation par 2 (4 électrons échangés) et on additionne. $4\,\mathrm{HO^-}$ et $2\,\mathrm{H_2O}$ se simplifient :
$$2\,\mathrm{H_2O}\to2\,\mathrm{H_2}+\mathrm O_2.$$
Cette réaction n'est pas spontanée : le générateur doit la forcer.

**2. Tension minimale théorique.** Il faut imposer à l'anode un potentiel au moins égal à celui du couple $\mathrm{O_2/H_2O}$, et à la cathode un potentiel au plus égal à celui du couple $\mathrm{H_2O/H_2}$ :
$$U_{\min}=E(\mathrm{O_2/H_2O})-E(\mathrm{H_2O/H_2})=(1{,}23-0{,}06\,\mathrm{pH})-(0-0{,}06\,\mathrm{pH})=1{,}23\ \mathrm V.$$
L'écart ne dépend pas du pH (sous 1 bar). C'est la tension thermodynamique, $U_{\min}=\frac{\Delta_rG^\circ}{nF}$.

**2. Tension réelle.** Les couples de l'eau sont lents, surtout $\mathrm{O_2/H_2O}$ : les courbes intensité-potentiel ne « décollent » qu'avec des surtensions. Pour obtenir un courant $I$ notable, il faut imposer à l'anode $E_a=1{,}23+\eta_a$ ($\eta_a>0$) et à la cathode $E_c=0+\eta_c$ ($\eta_c<0$), avec des surtensions qui croissent avec $I$. Il faut aussi vaincre la résistance de l'électrolyte et des connexions (chute ohmique $RI$). Donc
$$U=1{,}23+\eta_a+|\eta_c|+RI\approx1{,}8\ \mathrm V\ \text{en fonctionnement industriel}.$$
Le nickel est choisi comme matériau d'électrode pour ses surtensions relativement faibles et sa résistance en milieu basique.

**3. Charge par mole de $\mathrm{H_2}$.** La formation d'une mole de $\mathrm{H_2}$ consomme 2 mol d'électrons, soit $Q=2F$. L'énergie électrique correspondante vaut
$$W_1=QU=2FU=2\times96\,500\times1{,}8\approx3{,}5\times10^5\ \mathrm{J\,mol^{-1}}.$$

**3. Pour 1 kg.** $n=\frac{1000}{2{,}0}=500$ mol, donc
$$W=500\times3{,}47\times10^5\approx1{,}7\times10^8\ \mathrm J=\frac{1{,}7\times10^8}{3{,}6\times10^6}\approx48\ \mathrm{kWh}.$$

**4. Énergie récupérable.** La combustion de 500 mol de $\mathrm{H_2}$ libère $500\times286=1{,}43\times10^5$ kJ $=1{,}43\times10^8$ J, soit environ 40 kWh.

**4. Rendement.**
$$\eta=\frac{40}{48}\approx0{,}82.$$
C'est le rendement de l'étape d'électrolyse : 18 % de l'énergie électrique est perdue sous forme de chaleur, à cause des surtensions et de l'effet Joule. Si l'on reconvertit ensuite l'hydrogène en électricité dans une pile à combustible (rendement de l'ordre de 50 %), le rendement global « électricité → électricité » tombe à environ 40 %. Sans compter la compression ou la liquéfaction pour le stockage, qui coûtent encore 10 à 30 %. L'hydrogène est un vecteur d'énergie, pas une source.
"""

D['n-c-aeqs'] = r"""
**1. Étape cinétiquement déterminante.** L'étape lente impose la vitesse globale. $\mathrm{NO_2}$ n'est formé que par l'étape 2, avec 2 molécules par acte. Avec la vitesse de réaction $v=\frac12\frac{\mathrm d[\mathrm{NO_2}]}{\mathrm dt}$ :
$$v=k_2[\mathrm{N_2O_2}][\mathrm O_2].$$

**1. Pré-équilibre.** L'étape 1 est rapide dans les deux sens et reste à l'équilibre à chaque instant. L'étape 2, lente, ne consomme pas assez vite $\mathrm{N_2O_2}$ pour le perturber. D'où
$$K=\frac{[\mathrm{N_2O_2}]}{[\mathrm{NO}]^2}\quad\Longrightarrow\quad[\mathrm{N_2O_2}]=K[\mathrm{NO}]^2.$$

**1. Loi de vitesse.**
$$v=k_2K[\mathrm{NO}]^2[\mathrm O_2].$$
On retrouve la loi expérimentale, avec $k=k_2K$ : ordre 2 par rapport à NO et ordre 1 par rapport à $\mathrm O_2$.

**2. AEQS.** $\mathrm{N_2O_2}$ est un intermédiaire réactionnel très réactif, en concentration faible et quasi constante : $\frac{\mathrm d[\mathrm{N_2O_2}]}{\mathrm dt}\approx0$. Il est formé par l'étape 1 (vitesse $k_1[\mathrm{NO}]^2$) et consommé par l'étape $-1$ (vitesse $k_{-1}[\mathrm{N_2O_2}]$) et par l'étape 2 (vitesse $k_2[\mathrm{N_2O_2}][\mathrm O_2]$) :
$$k_1[\mathrm{NO}]^2-k_{-1}[\mathrm{N_2O_2}]-k_2[\mathrm{N_2O_2}][\mathrm O_2]=0\quad\Longrightarrow\quad[\mathrm{N_2O_2}]=\frac{k_1[\mathrm{NO}]^2}{k_{-1}+k_2[\mathrm O_2]}.$$

**2. Vitesse.**
$$v=k_2[\mathrm{N_2O_2}][\mathrm O_2]=\frac{k_1k_2[\mathrm{NO}]^2[\mathrm O_2]}{k_{-1}+k_2[\mathrm O_2]}.$$
Cette loi n'a pas d'ordre global en général.

**2. Condition.** Si $k_{-1}\gg k_2[\mathrm O_2]$ (l'intermédiaire se redissocie bien plus souvent qu'il ne réagit avec $\mathrm O_2$, ce qui est l'hypothèse « étape 2 lente »), le dénominateur se réduit à $k_{-1}$ :
$$v\approx\frac{k_1}{k_{-1}}k_2[\mathrm{NO}]^2[\mathrm O_2]=Kk_2[\mathrm{NO}]^2[\mathrm O_2],$$
car à l'équilibre $k_1[\mathrm{NO}]^2=k_{-1}[\mathrm{N_2O_2}]$, donc $K=\frac{k_1}{k_{-1}}$. On retrouve le résultat de la question 1 : le pré-équilibre rapide est un cas particulier de l'AEQS.

**3. Dépendance en température.** On écrit $\ln k=\ln k_2+\ln K$, puis on dérive :
- loi d'Arrhenius : $\frac{\mathrm d\ln k_2}{\mathrm dT}=\frac{E_{a,2}}{RT^2}$, avec $E_{a,2}>0$ ;
- loi de Van't Hoff : $\frac{\mathrm d\ln K}{\mathrm dT}=\frac{\Delta_rH_1^\circ}{RT^2}$.

$$\frac{\mathrm d\ln k}{\mathrm dT}=\frac{E_{a,2}+\Delta_rH_1^\circ}{RT^2}=\frac{E_{a,\mathrm{app}}}{RT^2},\qquad E_{a,\mathrm{app}}=E_{a,2}+\Delta_rH_1^\circ.$$

**3. Conclusion.** La dimérisation $2\,\mathrm{NO}\to\mathrm{N_2O_2}$ forme une liaison : elle est exothermique, $\Delta_rH_1^\circ<0$. Si $|\Delta_rH_1^\circ|>E_{a,2}$, l'énergie d'activation apparente est **négative**, et $k$ diminue quand $T$ augmente. Physiquement, chauffer accélère l'étape 2, mais déplace le pré-équilibre exothermique vers NO : la concentration de l'intermédiaire $\mathrm{N_2O_2}$ chute plus vite que $k_2$ n'augmente. Ce comportement, inexplicable pour un acte élémentaire (dont $E_a>0$), est un argument en faveur du mécanisme en deux étapes.
"""

D['n-m-max'] = r"""
**1. Événement $(M_n\le k)$.** Le maximum est inférieur ou égal à $k$ si et seulement si tous les tirages le sont : $(M_n\le k)=\bigcap_{i=1}^n(X_i\le k)$. Les tirages, avec remise, sont indépendants, et chaque $X_i$ suit la loi uniforme sur $[\![1,N]\!]$, donc $P(X_i\le k)=\frac kN$. D'où
$$P(M_n\le k)=\prod_{i=1}^nP(X_i\le k)=\Big(\frac kN\Big)^n,\qquad k\in[\![0,N]\!].$$

**1. Loi de $M_n$.** $M_n$ prend ses valeurs dans $[\![1,N]\!]$. Pour $k$ dans cet intervalle, $(M_n=k)=(M_n\le k)\setminus(M_n\le k-1)$, avec $(M_n\le k-1)\subset(M_n\le k)$. Donc
$$P(M_n=k)=\Big(\frac kN\Big)^n-\Big(\frac{k-1}N\Big)^n=\frac{k^n-(k-1)^n}{N^n}.$$
Vérification : la somme sur $k$ est télescopique et vaut $\frac{N^n-0}{N^n}=1$. ✓

**2. Écriture de $M_n$ comme somme d'indicatrices.** Pour tout entier $m\in[\![1,N]\!]$, il y a exactement $m$ entiers $i\in[\![0,N-1]\!]$ tels que $i<m$ (ce sont $0,1,\dots,m-1$). Donc $m=\sum_{i=0}^{N-1}\mathbf 1_{i<m}$, et en appliquant à $m=M_n(\omega)$ :
$$M_n=\sum_{i=0}^{N-1}\mathbf 1_{(M_n>i)}.$$

**2. Espérance.** Par linéarité, avec $E(\mathbf 1_A)=P(A)$ :
$$E(M_n)=\sum_{i=0}^{N-1}P(M_n>i)=\sum_{i=0}^{N-1}\Big(1-\Big(\frac iN\Big)^n\Big)=N-\sum_{i=0}^{N-1}\Big(\frac iN\Big)^n.$$

**2. Limite.** Pour $0\le i\le N-1$, $0\le\frac iN<1$, donc $\big(\frac iN\big)^n\to0$. La somme est finie, avec $N$ termes, donc $E(M_n)\to N$.

**2. Interprétation.** Avec beaucoup de tirages, on finit presque sûrement par tirer la boule $N$ : $P(M_n=N)=1-\big(\frac{N-1}N\big)^n\to1$.

**3. Identité.** Pour $m\in[\![1,N]\!]$ :
$$\sum_{i=0}^{N-1}2i\,\mathbf 1_{i<m}=\sum_{i=0}^{m-1}2i=2\cdot\frac{(m-1)m}2=m(m-1).$$
Donc $M_n(M_n-1)=\sum_{i=0}^{N-1}2i\,\mathbf 1_{(M_n>i)}$, et par linéarité de l'espérance :
$$E\big(M_n(M_n-1)\big)=\sum_{i=0}^{N-1}2i\,P(M_n>i).$$

**4. Limite de la variance.** $P(M_n>i)\to1$ pour tout $i\le N-1$, donc
$$E\big(M_n(M_n-1)\big)\to\sum_{i=0}^{N-1}2i=N(N-1).$$
Avec $V(M_n)=E(M_n^2)-E(M_n)^2=E\big(M_n(M_n-1)\big)+E(M_n)-E(M_n)^2$ :
$$V(M_n)\to N(N-1)+N-N^2=0.$$

**4. Interprétation.** La variance mesure la dispersion autour de la moyenne. Elle tend vers 0 et l'espérance vers $N$ : la loi de $M_n$ se concentre sur la valeur $N$. Par l'inégalité de Bienaymé-Tchebychev, $M_n$ converge en probabilité vers la constante $N$ (et ici on a même $P(M_n=N)\to1$).
"""

D['n-m-euler'] = r"""
**1. Recherche de solutions puissances.** Pour $y(t)=t^r$ sur $]0,+\infty[$ : $y'=rt^{r-1}$ et $y''=r(r-1)t^{r-2}$. Donc
$$t^2y''+4ty'+2y=\big[r(r-1)+4r+2\big]t^r=(r^2+3r+2)\,t^r.$$
Comme $t^r\neq0$, $t^r$ est solution si et seulement si $r^2+3r+2=0$, soit $(r+1)(r+2)=0$, c'est-à-dire $r=-1$ ou $r=-2$.

**1. Ensemble des solutions.** Sur $]0,+\infty[$, le coefficient de $y''$, $t^2$, ne s'annule pas. En divisant par $t^2$, on obtient une équation linéaire homogène d'ordre 2 à coefficients continus, normalisée : par le théorème de Cauchy linéaire, l'ensemble $S$ des solutions est un espace vectoriel de dimension 2. Les fonctions $f_1:t\mapsto\frac1t$ et $f_2:t\mapsto\frac1{t^2}$ sont solutions et forment une famille libre. En effet, si $\frac at+\frac b{t^2}=0$ pour tout $t>0$, alors en multipliant par $t^2$, $at+b=0$ pour tout $t$, donc $a=b=0$. Ainsi
$$S=\Big\{t\mapsto\frac at+\frac b{t^2},\ (a,b)\in\mathbb R^2\Big\}.$$

**2. Changement de fonction.** Avec $z=t^2y$ :
$$z'=2ty+t^2y',\qquad z''=2y+2ty'+2ty'+t^2y''=t^2y''+4ty'+2y.$$
L'équation $(E)$ s'écrit donc simplement $z''=0$.

**2. Résolution.** $z''=0$ sur l'intervalle $]0,+\infty[$ équivaut à $z(t)=at+b$, donc
$$y(t)=\frac{z(t)}{t^2}=\frac{at+b}{t^2}=\frac at+\frac b{t^2}.$$
On retrouve le résultat, sans avoir eu besoin de deviner la forme des solutions ni d'invoquer le théorème de dimension.

**3. Équation avec second membre.** Le même calcul donne $(E')\iff z''=e^t$. En intégrant deux fois sur l'intervalle : $z'=e^t+a$, puis $z=e^t+at+b$, avec $(a,b)\in\mathbb R^2$. D'où
$$y(t)=\frac{e^t+at+b}{t^2},\qquad(a,b)\in\mathbb R^2.$$
On reconnaît la structure habituelle : une solution particulière, $\frac{e^t}{t^2}$, plus la solution générale de l'équation homogène. Vérification de la solution particulière : avec $z=e^t$, on a bien $z''=e^t$. ✓ La méthode de variation des constantes donnerait le même résultat, plus laborieusement.
"""

D['n-m-abb'] = r"""
**1. Rang de $A-(a-b)I_3$.**
$$A-(a-b)I_3=\begin{pmatrix}b&b&b\\b&b&b\\b&b&b\end{pmatrix}=bJ,$$
où $J$ est la matrice dont tous les coefficients valent 1. Ses trois colonnes sont égales et non nulles ($b\neq0$) : elle est de rang 1.

**1. Valeur propre $a-b$.** Par le théorème du rang, $\dim\mathrm{Ker}\big(A-(a-b)I_3\big)=3-1=2$. Donc $a-b$ est valeur propre, et son sous-espace propre est
$$E_{a-b}=\mathrm{Ker}(bJ)=\{(x,y,z)^\top:\ x+y+z=0\},$$
qui est un plan.

**1. Troisième valeur propre.** Chaque ligne de $A$ a pour somme $a+2b$, donc $A\begin{pmatrix}1\\1\\1\end{pmatrix}=(a+2b)\begin{pmatrix}1\\1\\1\end{pmatrix}$ : $a+2b$ est valeur propre, de vecteur propre $(1,1,1)^\top$. On peut aussi utiliser la trace : $\mathrm{tr}\,A=3a=2(a-b)+\lambda_3$, donc $\lambda_3=a+2b$. Comme $b\neq0$, $a+2b\neq a-b$. Les valeurs propres sont donc $a-b$ (double) et $a+2b$ (simple), et
$$E_{a+2b}=\mathrm{Vect}\big((1,1,1)^\top\big).$$
$A$ est diagonalisable, ce qui est cohérent avec le fait qu'elle est symétrique réelle.

**2. Orthogonalité.** $A$ est symétrique réelle : par le théorème spectral, ses sous-espaces propres sont orthogonaux. On le vérifie : $(1,1,1)$ est normal au plan $x+y+z=0$.

**2. Base orthonormée adaptée.**
- Pour $E_{a+2b}$ : $u_1=\frac1{\sqrt3}(1,1,1)^\top$.
- Pour $E_{a-b}$, on prend une base orthonormée du plan : $u_2=\frac1{\sqrt2}(1,-1,0)^\top$, puis un vecteur du plan orthogonal à $u_2$, $(1,1,-2)$, normalisé en $u_3=\frac1{\sqrt6}(1,1,-2)^\top$.

On vérifie : $u_2$ et $u_3$ ont des coordonnées de somme nulle, et $u_2\cdot u_3=\frac{1-1+0}{\sqrt{12}}=0$.

**2. Diagonalisation.**
$$P=\begin{pmatrix}\frac1{\sqrt3}&\frac1{\sqrt2}&\frac1{\sqrt6}\\\frac1{\sqrt3}&-\frac1{\sqrt2}&\frac1{\sqrt6}\\\frac1{\sqrt3}&0&-\frac2{\sqrt6}\end{pmatrix},\qquad D=\mathrm{diag}(a+2b,\,a-b,\,a-b).$$
Les colonnes de $P$ forment une base orthonormée : $P$ est orthogonale, $P^{-1}=P^\top$, et $A=PDP^\top$.

**3. Forme bilinéaire.** Soit $\varphi(X,Y)=X^\top AY$. Elle est bilinéaire (par bilinéarité du produit matriciel) et symétrique : $\varphi(Y,X)=Y^\top AX=(Y^\top AX)^\top=X^\top A^\top Y=X^\top AY$, car $A^\top=A$ et qu'un réel est égal à sa transposée.

**3. Positivité et définition.** Pour $a=3$ et $b=2$, les valeurs propres sont $a+2b=7$ et $a-b=1$. Avec $X'=P^\top X=(x_1',x_2',x_3')^\top$ :
$$\varphi(X,X)=X^\top PDP^\top X=X'^\top DX'=7x_1'^2+x_2'^2+x_3'^2\ge0.$$
L'égalité $\varphi(X,X)=0$ impose $x_1'=x_2'=x_3'=0$, donc $X'=0$ et $X=PX'=0$. $\varphi$ est définie positive : c'est un **produit scalaire**. Plus généralement, $X^\top AY$ est un produit scalaire si et seulement si $A$ est symétrique à valeurs propres strictement positives.
"""

D['n-m-antisym'] = r"""
**1. Polarisation.** On applique l'hypothèse à $x=y+z$ et on développe par bilinéarité du produit scalaire :
$$0=\langle u(y+z),y+z\rangle=\underbrace{\langle u(y),y\rangle}_{0}+\langle u(y),z\rangle+\langle u(z),y\rangle+\underbrace{\langle u(z),z\rangle}_{0}.$$
Donc $\langle u(y),z\rangle=-\langle u(z),y\rangle=-\langle y,u(z)\rangle$, par symétrie du produit scalaire. On dit que $u$ est antisymétrique ($u^*=-u$) ; sa matrice dans une base orthonormée est antisymétrique.

**2. $\mathrm{Ker}\,u=(\mathrm{Im}\,u)^\perp$.** Pour $y\in E$, on a les équivalences
$$y\in\mathrm{Ker}\,u\iff u(y)=0\iff\forall z\in E,\ \langle u(y),z\rangle=0\iff\forall z\in E,\ \langle y,u(z)\rangle=0\iff y\in(\mathrm{Im}\,u)^\perp.$$
La deuxième équivalence vient de ce qu'un vecteur orthogonal à tous les vecteurs est nul ; la troisième de la question 1.

**2. Conclusion.** En dimension finie, $E=\mathrm{Im}\,u\oplus(\mathrm{Im}\,u)^\perp$, donc $E=\mathrm{Im}\,u\overset{\perp}{\oplus}\mathrm{Ker}\,u$. Le noyau et l'image sont supplémentaires orthogonaux.

**3. L'endomorphisme induit.** $\mathrm{Im}\,u$ est stable par $u$ (puisque $u(\mathrm{Im}\,u)\subset\mathrm{Im}\,u$), donc $v$ est bien défini. Son noyau vaut $\mathrm{Ker}\,v=\mathrm{Ker}\,u\cap\mathrm{Im}\,u=\{0\}$, d'après la question 2 (supplémentaires). Ainsi $v$ est injectif, donc bijectif en dimension finie : c'est un automorphisme de $\mathrm{Im}\,u$.

**3. Pas de valeur propre réelle.** Supposons $v(x)=\lambda x$ avec $x\in\mathrm{Im}\,u$ non nul et $\lambda\in\mathbb R$. Alors
$$0=\langle u(x),x\rangle=\langle\lambda x,x\rangle=\lambda\|x\|^2,$$
donc $\lambda=0$, car $\|x\|\neq0$. Mais alors $v(x)=0$ avec $x\neq0$, ce qui contredit l'injectivité. Donc $v$ n'a **aucune valeur propre réelle**. (On suppose $\mathrm{Im}\,u\neq\{0\}$ ; si $u=0$, le rang vaut 0, qui est pair.)

**4. Polynômes réels sans racine réelle.** Un polynôme réel $P$ de degré impair a une racine réelle. En effet, son coefficient dominant impose des limites de signes opposés en $\pm\infty$, et le théorème des valeurs intermédiaires s'applique à la fonction continue $P$. Les polynômes réels qui ne s'annulent pas sur $\mathbb R$ sont donc de degré pair : constantes non nulles, et produits de trinômes $X^2+pX+q$ de discriminant négatif (par décomposition en facteurs irréductibles sur $\mathbb R$).

**4. Parité du rang.** Les valeurs propres réelles de $v$ sont exactement les racines réelles de son polynôme caractéristique $\chi_v$. D'après 3, $\chi_v$ n'a aucune racine réelle, donc son degré est pair. Or $\deg\chi_v=\dim\mathrm{Im}\,u=\mathrm{rg}\,u$. Donc
$$\mathrm{rg}\,u\ \text{est pair}.$$
Conséquence : en dimension impaire, un endomorphisme antisymétrique n'est jamais inversible. On retrouve que $\det A=0$ pour toute matrice antisymétrique d'ordre impair, puisque $\det A=\det A^\top=\det(-A)=(-1)^n\det A$.
"""
