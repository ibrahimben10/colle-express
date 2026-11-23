# Bilans — maths, Centrale (m-ccs) et X-ENS (x-*)
from bilan_lib import *
B = {}

B['m-ccs-01'] = ([
  r"**Formule de la comatrice.** $M^{-1}=\frac1{\det M}\,\mathrm{com}(M)^{\top}$ : les coefficients de $M^{-1}$ sont des fractions rationnelles des coefficients de $M$, donc $M\mapsto M^{-1}$ est continue sur $GL_n$.",
  r"**Déterminant par blocs (complément de Schur).** Si $D$ est inversible, $\det\begin{pmatrix}A&B\\C&D\end{pmatrix}=\det D\,\det(A-BD^{-1}C)$.", RANG],
  [r"Continuité d'une application matricielle : l'écrire avec des polynômes et des quotients de déterminants.",
   r"Pour un déterminant par blocs avec un bloc identité, éliminer par opérations sur les blocs (complément de Schur).",
   r"$\mathrm{Im}\,V\oplus(\mathrm{Im}\,W)^\perp=\mathbb R^n$ se traduit par l'inversibilité de $W^{\top}V$."])
B['m-ccs-02'] = ([CV_NORM,
  r"**Inégalité $|\arctan u|\le|u|$.** Elle découle de l'inégalité des accroissements finis ($|\arctan'|\le1$)."],
  [r"Majorer le terme général par une quantité indépendante de $x$ sur un segment (convergence normale locale).",
   r"Dériver terme à terme quand la série des dérivées converge normalement : ici $\frac1{n^2+x^2}\le\frac1{n^2}$.",
   r"Non-uniformité : évaluer le reste en un point qui dépend de $N$ (ici $x=2N$)."])
B['m-ccs-03'] = ([BT,
  r"**Loi faible des grands nombres.** Si les $X_k$ sont i.i.d. de variance finie, $P\left(\left|\frac{S_n}n-E(X_1)\right|\ge\varepsilon\right)\le\frac{V(X_1)}{n\varepsilon^2}\to0$.",
  r"**Image d'une loi uniforme par une bijection.** Si $U$ est uniforme sur un ensemble fini et $\varphi$ une bijection, $\varphi(U)$ est uniforme."],
  [r"Pour démontrer l'indépendance, exhiber une bijection entre les vecteurs $(U_0,\dots,U_n)$ et $(X_0,\dots,X_n)$.",
   r"Travailler modulo 10 : $X_k\equiv X_{k-1}+U_k$.",
   r"Uniforme + bijection = uniforme : la loi jointe est uniforme, donc produit de lois uniformes."])
B['m-ccs-05'] = ([
  r"**Multiplicité d'une racine.** Si $(X-z)^m$ divise $P$, alors $(X-z)^{m-1}$ divise $P'$.",
  r"**Degré.** $\deg(AB'-BA')\le\deg A+\deg B-1$ ; il est nul ssi $A$ et $B$ sont proportionnels."],
  [r"Introduire le wronskien $W=AB'-BA'$, identique pour les trois couples de $(A,B,C=A+B)$.",
   r"Compter les racines avec multiplicité : chaque racine multiple de $ABC$ est racine de $W$ avec multiplicité diminuée de 1.",
   r"Comparer le degré de $W$ à la somme des multiplicités moins le nombre de racines distinctes."])
B['m-ccs-06'] = ([RAYON, DSE,
  r"**Produit et inverse de séries entières.** Si $f(0)\neq0$, $1/f$ est développable en série entière au voisinage de 0 ; son rayon est au moins la distance de 0 au plus proche zéro complexe de $f$."],
  [r"Écrire $\frac1f=\sum_k(1-f)^k$ quand $|1-f|<1$ et justifier le réarrangement (convergence absolue).",
   r"Le rayon de $1/f$ est limité par les zéros complexes de $f$ : ici $e^x=1$, soit $x=2i\pi$.",
   r"Coefficients via $f\cdot\frac1f=1$ : relation de récurrence (nombres de Bernoulli)."])
B['m-ccs-07'] = ([IPP,
  r"**Méthode de l'énergie.** Si $E(t)=\int w^2\ge0$ vérifie $E'\le0$ et $E(0)=0$, alors $E\equiv0$, donc $w=0$.",
  r"**Séparation des variables.** Chercher $u(x,t)=f(x)g(t)$ : on obtient $\sin\frac{k\pi x}L\,e^{-k^2\pi^2t/L^2}$, puis on superpose."],
  [r"Unicité d'une solution d'EDP linéaire : étudier l'énergie de la différence de deux solutions.",
   r"Intégration par parties avec les conditions aux bords pour obtenir $E'(t)=-2\int(\partial_xw)^2\le0$.",
   r"Existence : séparation des variables et série de Fourier en sinus de la condition initiale."])
B['m-ccs-10'] = ([RAYON, EDL2,
  r"**Développement de $\arcsin$.** $\frac1{\sqrt{1-x^2}}=\sum\binom{2n}n\frac{x^{2n}}{4^n}$ ($R=1$), puis intégration."],
  [r"Pour identifier une série entière, chercher une équation différentielle vérifiée par sa somme.",
   r"$y=\arcsin^2x$ vérifie $(1-x^2)y''-xy'=2$ : comparer les coefficients.",
   r"Au bord du disque, conclure par le théorème de convergence radiale d'Abel ou la convergence normale."])
B['m-ccs-11'] = ([DOM_DERIV,
  r"**Unicité.** Deux solutions de $y''+y=\frac1x$ diffèrent d'une solution de $y''+y=0$, de la forme $A\cos x+B\sin x$ ; si leur différence tend vers 0 en $+\infty$, elle est nulle."],
  [r"Pour montrer que deux fonctions sont égales, montrer qu'elles vérifient la même équation différentielle et ont le même comportement à l'infini.",
   r"Dériver deux fois sous l'intégrale ; obtenir $f''+f=\frac1x$ par intégration de $e^{-xt}$.",
   r"Une combinaison $A\cos x+B\sin x$ qui tend vers 0 est nulle."])
B['m-ccs-12'] = ([GEOM, SOMME_IND,
  r"**Loi de Pascal.** Le rang du $N$-ième succès suit $P(X=k)=\binom{k-1}{N-1}p^Nq^{k-N}$ ($k\ge N$)."],
  [r"Décomposer un temps d'attente total en somme de temps d'attente géométriques indépendants.",
   r"Espérance et variance par linéarité et indépendance, sans calculer la loi.",
   r"Pour la loi : le $k$-ième essai est un succès et il y a exactement $N-1$ succès parmi les $k-1$ précédents."])
B['m-ccs-14'] = ([
  r"**Carrés modulo 3.** Un carré est congru à 0 ou 1 modulo 3.",
  r"**Descente infinie.** Une solution entière non nulle en fournit une strictement plus petite : impossible, il n'y a pas de solution non nulle.", SPECTRAL],
  [r"Pour une équation diophantienne homogène, raisonner modulo un nombre premier bien choisi et faire une descente infinie.",
   r"Une matrice symétrique rationnelle a un polynôme caractéristique rationnel : traduire « $M^2=\alpha I$ » en conditions sur ses coefficients.",
   r"Chercher des exemples simples ($\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ pour $\sqrt2$)."])
B['m-ccs-15'] = ([
  r"**Relation d'Euler.** Si $f$ est homogène de degré $\alpha$ : $\sum x_i\partial_if=\alpha f$ ; en dérivant, $Hx=(\alpha-1)\nabla f$.",
  r"**Matrice hessienne.** $H=(\partial_{ij}f)$, symétrique pour $f$ de classe $C^2$ (Schwarz)."],
  [r"Passer au logarithme pour dériver un produit de puissances.",
   r"Homogénéité de degré 1 : $Hx=0$, donc $x\in\ker H$ et $\mathrm{rg}\,H\le n-1$.",
   r"Écrire $H=f\,(ww^{\top}-\mathrm{diag}(\cdot))$ (diagonale + rang 1) pour trouver exactement le rang."])
B['m-ccs-mi8'] = ([RAYON,
  r"**Série génératrice et récurrence de convolution.** Si $a_{n+2}=a_{n+1}+\sum_ka_ka_{n-k}$, la série $G=\sum a_nx^n$ vérifie une équation du second degré."],
  [r"Dénombrement de configurations récursives : décomposer selon ce que fait le premier point.",
   r"Traduire la décomposition en équation sur la série génératrice.",
   r"Le rayon est donné par le plus petit zéro du discriminant : ici $1-2x-3x^2=0$, soit $x=\frac13$."])
B['x-g-1'] = ([LAGRANGE,
  r"**Ordre d'un produit.** Si $x,y$ commutent, sont d'ordres $p,q$ premiers entre eux, alors $xy$ est d'ordre $pq$.",
  r"**Lemme de Cauchy (cas abélien).** Si un premier $p$ divise l'ordre d'un groupe abélien fini, il existe un élément d'ordre $p$."],
  [r"Lister les ordres possibles par Lagrange.",
   r"Si $x$ est d'ordre $pq$, alors $x^q$ est d'ordre $p$ : on fabrique des éléments d'ordre premier par puissances.",
   r"Groupe abélien où tout élément vérifie $x^p=e$ : c'est un $\mathbb Z/p\mathbb Z$-espace vectoriel, donc de cardinal $p^k$."])
B['x-g-2'] = ([LAGRANGE,
  r"**Groupe d'exposant 2.** Si $x^2=e$ pour tout $x$, le groupe est abélien ($xy=(xy)^{-1}=y^{-1}x^{-1}=yx$) et c'est un $\mathbb F_2$-espace vectoriel : son cardinal est une puissance de 2."],
  [r"Raisonner par l'absurde sur les ordres possibles (1, 2, $p$, $2p$).",
   r"Un élément d'ordre $2p$ donne un élément d'ordre $p$ en l'élevant au carré.",
   r"Si tout élément est d'ordre $\le2$, le groupe est un espace vectoriel sur $\mathbb F_2$."])
B['x-a-1'] = ([
  r"**Inverse dans un anneau.** Il suffit d'exhiber $y$ avec $xy=yx=1$ ; vérifier les deux produits si l'anneau n'est pas commutatif."],
  [r"Deviner l'inverse avec les séries géométriques formelles, puis vérifier par un calcul algébrique honnête.",
   r"$(1-ba)^{-1}=1+b(1-ab)^{-1}a$ : développer $(1-ba)(1+bca)$ avec $c=(1-ab)^{-1}$.",
   r"Conséquence : $AB$ et $BA$ ont les mêmes valeurs propres non nulles."])
B['x-ar-1'] = ([
  r"**Lemme d'Euclide.** Si un premier $p$ divise $ab$, il divise $a$ ou $b$.",
  r"**Inverse modulo $p$.** Si $p\nmid a$, $a$ est inversible modulo $p$."],
  [r"Factoriser le polynôme avant de chercher une racine modulo $p$.",
   r"Il suffit qu'un facteur soit nul modulo $p$ : $2n+1\equiv0$ a une solution pour $p$ impair.",
   r"Traiter $p=2$ à part."])
B['x-ar-2'] = ([RACINES, LAGRANGE,
  r"**Ordre d'un produit.** Si $x,y$ commutent et ont des ordres premiers entre eux $a$ et $b$, $xy$ est d'ordre $ab$."],
  [r"Pour chaque facteur $q^\alpha$ de $p-1$, trouver un élément d'ordre exactement $q^\alpha$.",
   r"Un polynôme de degré $d$ a au plus $d$ racines dans un corps : cela fournit un $x$ avec $x^{(p-1)/q}\neq1$.",
   r"Multiplier ces éléments d'ordres premiers entre eux pour obtenir un générateur."])
B['x-p-1'] = ([
  r"**Dérivée logarithmique.** Si $P=c\prod(X-z_i)^{m_i}$, alors $\frac{P'}P=\sum\frac{m_i}{X-z_i}$.",
  r"**Barycentre.** Un barycentre à coefficients positifs de points est dans leur enveloppe convexe."],
  [r"Écrire $\frac{P'}P$ en éléments simples et évaluer en une racine de $P'$.",
   r"Multiplier par le conjugué : $\frac1{w-z}=\frac{\overline{w-z}}{|w-z|^2}$ fait apparaître des poids positifs.",
   r"Interprétation : les racines de $P'$ sont dans l'enveloppe convexe des racines de $P$."])
B['x-al-1'] = ([RANG,
  r"**Rang d'une composée.** $\mathrm{rg}(ab)=\mathrm{rg}\,b-\dim(\ker a\cap\mathrm{Im}\,b)$ ; $\mathrm{rg}(ab)\le\min(\mathrm{rg}\,a,\mathrm{rg}\,b)$."],
  [r"Appliquer le théorème du rang à la restriction de $a$ à $\mathrm{Im}\,b$.",
   r"$\mathrm{Im}(a+b)\subset\mathrm{Im}\,a+\mathrm{Im}\,b$ et $a=(a+b)-b$ donnent les deux inégalités.",
   r"Cas d'égalité : traduire en somme directe des images (et des noyaux)."])
B['x-al-2'] = ([
  r"**Multilinéarité du déterminant.** $\det$ est linéaire par rapport à chaque ligne ; développer une ligne combinaison convexe des vecteurs de base donne une moyenne de déterminants de matrices à lignes canoniques.",
  r"**Valeurs propres d'une matrice stochastique.** Toute valeur propre vérifie $|\lambda|\le1$ (regarder la coordonnée de module maximal)."],
  [r"Pour majorer un déterminant, le voir comme produit des valeurs propres ou par multilinéarité.",
   r"Une ligne stochastique est une combinaison convexe des vecteurs de la base canonique.",
   r"Cas d'égalité : seuls les termes « permutations » contribuent."])
B['x-al-3'] = ([
  r"**Comatrice.** $A\,\mathrm{com}(A)^{\top}=\det(A)\,I_n$ ; donc $\tilde A=\det(A)A^{-1}$ si $A$ est inversible.",
  r"**Densité de $GL_n(\mathbb C)$.** Toute matrice est limite de matrices inversibles ; les coefficients du polynôme caractéristique dépendent continûment de la matrice."],
  [r"Cas inversible d'abord, puis densité et continuité.",
   r"Valeurs propres de $A^{-1}$ : les inverses ; celles de $\det(A)A^{-1}$ : $\prod_{j\neq i}\lambda_j$.",
   r"Réflexe : une identité polynomiale vraie sur $GL_n$ est vraie partout."])
B['x-al-4'] = ([
  r"**Multilinéarité alternée.** $\det(C_1,\dots,C_n)$ est multilinéaire alterné : un déterminant avec deux colonnes égales est nul.",
  r"**Rang d'un produit.** $\mathrm{rg}(AB)\le\min(\mathrm{rg}\,A,\mathrm{rg}\,B)$."],
  [r"Écrire chaque colonne de $AB$ comme combinaison des colonnes de $A$ et développer par multilinéarité.",
   r"Ne garder que les familles d'indices distincts (sinon déterminant nul), puis regrouper par ensemble d'indices.",
   r"Si $n>m$, le rang de $AB$ est au plus $m<n$ : déterminant nul."])
B['x-r-1'] = ([
  r"**Matrice stochastique.** Si $a_{ij}\ge0$ et $\sum_ja_{ij}=1$, alors $A\mathbf 1=\mathbf 1$ et toute valeur propre vérifie $|\lambda|\le1$.",
  r"**Cas d'égalité de l'inégalité triangulaire.** $\left|\sum a_jz_j\right|=\sum a_j|z_j|$ (avec $a_j>0$) impose aux $z_j$ un même argument."],
  [r"Regarder la coordonnée de module (ou de partie réelle) maximal d'un vecteur propre.",
   r"Les coefficients strictement positifs forcent les égalités : toutes les coordonnées sont égales.",
   r"Conséquence classique : $A^k$ converge vers un projecteur de rang 1 (chaînes de Markov)."])
B['x-r-2'] = ([DIAG_POLY,
  r"**Racines de $X^p-\mu$.** Pour $\mu\neq0$ dans $\mathbb C$, $X^p-\mu$ a $p$ racines distinctes ; les polynômes $X^p-\mu_k$ ($\mu_k$ distincts) sont premiers entre eux."],
  [r"Transformer un polynôme annulateur de $A^p$ en un polynôme annulateur de $A$ : $Q(X^p)$.",
   r"Vérifier que ce polynôme est à racines simples : c'est là que sert $\mu_k\neq0$ (inversibilité).",
   r"Contre-exemple quand $A^p$ n'est pas inversible : une matrice nilpotente non nulle."])
B['x-r-3'] = ([TRIGO,
  r"**Moyenne de Cesàro.** Si $u_k\to0$, alors $\frac1N\sum_{k<N}|u_k|^2\to0$.",
  r"**Somme d'exponentielles.** Pour des $\theta_i$ distincts de module 1, $\frac1N\sum_{k<N}\left|\sum m_i\theta_i^k\right|^2\to\sum m_i^2$."],
  [r"Écrire $\mathrm{Tr}(A^k)=\sum m_i\lambda_i^k$ et isoler les valeurs propres de module maximal.",
   r"Moyenner le module au carré pour tuer les termes croisés (les $\theta_i\bar\theta_j$ avec $i\neq j$ ont une moyenne nulle).",
   r"Raisonner par l'absurde avec $\rho=\max|\lambda_i|\ge1$."])
B['x-r-4'] = ([
  r"**Exponentielle d'une nilpotente.** Si $N^n=0$, $\exp N=\sum_{k<n}\frac{N^k}{k!}$ est unipotente ($I+$ nilpotente).",
  r"**Identités formelles.** $\exp(\log(1+x))=1+x$ et $\log(\exp x)=x$ dans les séries formelles ; elles s'appliquent aux matrices nilpotentes (sommes finies)."],
  [r"Pour inverser $\exp$ sur les unipotentes, utiliser la série du logarithme, finie.",
   r"Transporter des identités de séries formelles à des matrices nilpotentes : toutes les sommes sont finies.",
   r"Surjectivité sur $GL_n(\mathbb C)$ : décomposition de Dunford et logarithme sur chaque sous-espace caractéristique."])
B['x-r-5'] = ([
  r"**Matrice d'ordre fini.** Si $M^k=I$, $M$ est annulée par $X^k-1$, scindé à racines simples sur $\mathbb C$ : diagonalisable à valeurs propres racines de l'unité.",
  r"**Relations coefficients-racines.** Les coefficients de $\chi_M$ sont les fonctions symétriques élémentaires des valeurs propres ; si celles-ci sont de module 1, le coefficient de degré $n-k$ est borné par $\binom nk$."],
  [r"Polynôme caractéristique à coefficients entiers et bornés : il n'y a qu'un nombre fini de possibilités.",
   r"Donc les valeurs propres possibles sont en nombre fini, et l'ordre est borné (PPCM des ordres).",
   r"Réflexe : entier + borné = nombre fini de cas."])
B['x-an-1'] = ([CHGT, IPP],
  [r"Faire un dessin : l'aire sous $f$ et l'aire « à gauche » de $f$ remplissent un rectangle.",
   r"Changement de variable $t=f(u)$ dans $\int f^{-1}$, puis intégration par parties.",
   r"Pour l'inégalité, distinguer $b\le f(a)$ et $b\ge f(a)$ et comparer les aires."])
B['x-an-2'] = ([IPP,
  r"**Intégrales de Wallis.** $I_n=\int_0^{\pi/2}\sin^nt\,\mathrm dt$ : $I_{n+2}=\frac{n+1}{n+2}I_n$, $(n+1)I_{n+1}I_n=\frac\pi2$, $I_n\sim\sqrt{\frac\pi{2n}}$."],
  [r"Relation de récurrence par parties, puis invariant $(n+1)I_nI_{n+1}$.",
   r"Encadrer $I_{n+1}\le I_n\le I_{n-1}$ (décroissance) pour obtenir $I_n\sim I_{n+1}$.",
   r"Réflexe : $I_n^2\sim\frac\pi{2n}$, d'où la divergence de $\sum I_n^2$."])
B['x-an-3'] = ([
  r"**Théorème de Dini.** Une suite croissante de fonctions continues qui converge simplement vers une fonction continue sur un segment converge uniformément.",
  r"**Compacité (Bolzano-Weierstrass).** Toute suite d'un segment admet une sous-suite convergente."],
  [r"Prouver Dini par l'absurde avec une suite de points et une sous-suite convergente.",
   r"Pour $p_{n+1}=p_n+\frac12(x-p_n^2)$, montrer par récurrence $0\le p_n\le\sqrt x$ et la croissance.",
   r"Conclure par Dini : la limite $\sqrt x$ est continue."])
B['x-s-1'] = ([
  r"**Suites récurrentes $u_{n+1}=f(u_n)$.** Si $f(x)<x$ près de $0^+$ et $f$ est continue, la suite décroît vers un point fixe, ici 0.",
  r"**Lemme de Cesàro.** Si $v_{n+1}-v_n\to\ell$, alors $\frac{v_n}n\to\ell$."],
  [r"Méthode générale : trouver $\beta$ tel que $u_{n+1}^\beta-u_n^\beta$ ait une limite finie non nulle, puis Cesàro.",
   r"Pour $u_{n+1}=u_n-au_n^\alpha+\dots$, prendre $\beta=1-\alpha$.",
   r"Exemples à connaître : $\sin$ donne $\sqrt{3/n}$, $\ln(1+x)$ donne $2/n$."])
B['x-s-2'] = ([
  r"**Suites adjacentes.** Une suite croissante et une suite décroissante dont la différence tend vers 0 convergent vers la même limite.",
  r"**Inégalité arithmético-harmonique.** $\frac{a+b}2\ge\frac{2ab}{a+b}$ pour $a,b>0$."],
  [r"Chercher un invariant : ici le produit $a_nb_n$ est constant.",
   r"Montrer l'adjacence avec l'inégalité entre moyennes.",
   r"Vitesse : $a_{n+1}-\ell=\frac{(a_n-\ell)^2}{2a_n}$, convergence quadratique (méthode de Newton pour $\sqrt{\cdot}$)."])
B['x-s-3'] = ([
  r"**Produit infini.** $\prod(1+a_k)$ avec $a_k\ge0$ converge ssi $\sum a_k$ converge.",
  r"**Valeurs d'adhérence et densité.** Si $\theta_n\to+\infty$ avec $\theta_{n+1}-\theta_n\to0$, l'ensemble des $e^{i\theta_n}$ est dense dans le cercle."],
  [r"Séparer module et argument d'un produit de nombres complexes.",
   r"L'argument diverge mais à pas de plus en plus petits : toutes les directions sont valeurs d'adhérence.",
   r"$\prod(1+\frac1{k^2})=\frac{\mathrm{sh}\,\pi}\pi$ (produit eulérien du sinus)."])
B['x-se-1'] = ([COMP,
  r"**Série géométrique.** $\sum_{d\ge1}9\left(\frac9{10}\right)^{d-1}=90$."],
  [r"Regrouper les termes par paquets (nombre de chiffres) et majorer chaque paquet.",
   r"Compter les entiers à $d$ chiffres sans 9 : $8\times9^{d-1}$.",
   r"Une série de termes positifs dont les paquets forment une série convergente converge."])
B['x-se-2'] = ([CS, TONELLI],
  [r"Minorer une somme partielle par Cauchy-Schwarz en insérant les bons poids ($\sqrt{a_k}$, $\frac k{\sqrt{a_k}}$).",
   r"Sommer en $n$ puis intervertir les sommes (termes positifs), et majorer $\sum_{n\ge k}\frac1{n(n+1)^2}$.",
   r"Optimalité : tester une famille $a_n=n^{1+\varepsilon}$ et faire $\varepsilon\to0$."])
B['x-f-1'] = ([TVI,
  r"**Borne supérieure.** Toute partie non vide majorée de $\mathbb R$ admet une borne supérieure."],
  [r"Point fixe d'une fonction continue de $[0,1]$ dans lui-même : TVI appliqué à $f(x)-x$.",
   r"Sans continuité mais avec croissance : considérer $\sup\{x:f(x)\ge x\}$.",
   r"Pour deux fonctions qui commutent, montrer qu'un ensemble de points fixes est stable."])
B['x-f-2'] = ([
  r"**Uniforme continuité.** $\forall\varepsilon>0,\ \exists\delta>0,\ |x-y|\le\delta\Rightarrow|f(x)-f(y)|\le\varepsilon$."],
  [r"Fixer $\varepsilon=1$ et relier 0 à $x$ par $\lceil|x|/\delta\rceil$ pas de longueur $\le\delta$.",
   r"On obtient une majoration affine : $|f(x)|\le\frac{|x|}\delta+1+|f(0)|$.",
   r"Réciproque fausse : $\sin(x^2)$ est bornée mais pas uniformément continue."])
B['x-f-3'] = ([RACINES,
  r"**Dérivée d'une fraction rationnelle.** Si $R=P/Q$ est non polynomiale, $R''$ a un degré (au sens $\deg P-\deg Q$) strictement inférieur à celui de $R$."],
  [r"Si $\sin=R$ sur un intervalle, $R$ vérifie $R''+R=0$ sur cet intervalle, donc partout (infinité de points).",
   r"Comparer les degrés ou les pôles de $R$ et de $R''$.",
   r"Réflexe : une égalité de fractions rationnelles sur un ensemble infini est une égalité de fractions."])
B['x-fo-1'] = ([DIRICHLET_F, IPP],
  [r"Fonction paire : seuls les coefficients $a_n$ (cosinus) sont à calculer.",
   r"Deux intégrations par parties pour $\int x^2\cos(nx)$.",
   r"Évaluer en $x=\pi$ (Dirichlet) pour $\sum\frac1{n^2}$, puis Parseval pour $\sum\frac1{n^4}$."])
