# Bilans — maths, oraux CCINP / Mines (série m-ccmp)
from bilan_lib import *
B = {}

B['m-ccmp-01a'] = ([
  r"**Distance à une partie.** $d(x,F)=\inf_{y\in F}\|x-y\|$ ; $d(x,F)=0\iff x\in\overline F$.",
  r"**Fonction convexe.** $f((1-t)a+tb)\le(1-t)f(a)+tf(b)$ ; une fonction convexe positive nulle en $a$ et en $b$ est nulle sur $[a,b]$."],
  [r"Pour montrer qu'un ensemble est convexe, se ramener à une fonction d'une variable sur le segment $[a,b]$.",
   r"Penser au rôle de la fermeture : « distance nulle » donne seulement l'adhérence. Chercher un contre-exemple avec un ensemble non fermé.",
   r"Réflexe : $x\mapsto d(x,F)$ est 1-lipschitzienne, et convexe quand $F$ est convexe."])
B['m-ccmp-01b'] = ([
  r"**Suites arithmético-géométriques.** $u_{n+1}=au_n+b$ ($a\ne1$) : $u_n-\ell=a^n(u_0-\ell)$ avec $\ell=\frac b{1-a}$.", GENER,
  r"**Loi de probabilité.** $(p_n)$ est une loi sur $\mathbb N$ ssi $p_n\ge0$ et $\sum p_n=1$."],
  [r"Une relation de récurrence sur $P(X=n)$ se traduit en équation sur la fonction génératrice $G$ : on multiplie par $s^n$ et on somme.",
   r"Toujours exploiter les contraintes $p_n\ge0$, $\sum p_n=1$ : elles fixent les paramètres.",
   r"Espérance : dériver $G$ en $s=1$ plutôt que sommer $\sum np_n$ à la main."])
B['m-ccmp-02a'] = ([EDL2,
  r"**Solutions sur $\mathbb R$ et raccord.** Une solution sur $\mathbb R$ est une solution sur $]-\infty,0[$ et sur $]0,+\infty[$ qui se raccorde de façon $C^2$ en 0."],
  [r"Face à $x f(x)=g(x)$, poser $z=xy$ : l'équation en $z$ est souvent à coefficients constants.",
   r"Quand le coefficient dominant s'annule (ici en 0), résoudre sur chaque intervalle puis étudier le raccord : la dimension de l'espace des solutions peut chuter.",
   r"Penser à $\frac{\mathrm{sh}\,x}x$ et $\frac{\mathrm{ch}\,x}x$ : seule la première se prolonge en 0."])
B['m-ccmp-02b'] = ([DIAG_POLY,
  r"**Matrice nilpotente diagonalisable.** Une matrice à la fois nilpotente et diagonalisable est nulle (son seul polynôme annulateur scindé simple possible est $X$).",
  r"**Racines complexes.** Sur $\mathbb C$, tout polynôme est scindé ; sur $\mathbb R$, ce n'est plus vrai (exemple : $X^2+1$)."],
  [r"Pour relier $M$ et $M^n$, travailler avec un polynôme annulateur $P$ et observer $P^n$ ou $P(X^n)$.",
   r"Toujours tester un résultat de réduction sur $\mathbb R$ avec une matrice de rotation : valeurs propres non réelles.",
   r"Polynôme $\prod(X-\lambda_i)$ sur les valeurs propres distinctes : c'est le polynôme minimal d'une matrice diagonalisable."])
B['m-ccmp-03a'] = ([BEZOUT,
  r"**Matrice compagnon.** La matrice compagnon de $P$ a $P$ pour polynôme caractéristique et pour polynôme minimal : $P(C)=0$.",
  r"**$\mathbb Q[S]$ est un corps.** Si le polynôme minimal de $S$ est irréductible sur $\mathbb Q$, toute matrice non nulle de $\mathbb Q[S]$ est inversible."],
  [r"Avec deux exposants premiers entre eux, combiner par Bézout : $(p^aS^b)^n=p$ si $an+bm=1$.",
   r"Réduire modulo $p$ une matrice entière : le déterminant modulo $p$ se calcule sur la réduite.",
   r"Descente : diviser par la plus grande puissance de $p$ possible pour se ramener à un cas déjà traité."])
B['m-ccmp-03b'] = ([
  r"**Comparaison série-intégrale.** Si $g$ est $C^1$ avec $g'$ intégrable sur $[1,+\infty[$, alors $\sum\left(g(n)-\int_n^{n+1}g\right)$ converge absolument.",
  r"**Inégalité des accroissements finis.** $|g(n)-g(t)|\le\sup|g'|\cdot|n-t|$."],
  [r"Quand $g$ n'est pas monotone, comparer $g(n)$ et $\int_n^{n+1}g$ via $g'$ plutôt que par monotonie.",
   r"Pour $\sin(\ln n)$ : poser $u=\ln t$, la primitive $-\cos(\ln t)$ oscille sans limite, donc la série diverge.",
   r"Réflexe : $\sum u_n$ et $\int g$ ont même nature dès que $\sum(u_n-\int_n^{n+1}g)$ converge."])
B['m-ccmp-04a'] = ([RAYON, DSE,
  r"**Unicité du développement.** Deux séries entières égales sur un voisinage de 0 ont les mêmes coefficients."],
  [r"Récurrence de type convolution $a_{n+1}=\sum a_ka_{n-k}$ : introduire la série génératrice, qui vérifie une équation algébrique.",
   r"Choisir la racine qui reste bornée en 0 ; plutôt que de justifier un rayon a priori, partir de la solution explicite et identifier les coefficients.",
   r"$\sqrt{1-4x}=\sum\binom{1/2}n(-4x)^n$ fait apparaître $\binom{2n}n$."])
B['m-ccmp-04b'] = ([LAGRANGE,
  r"**Morphisme injectif.** Un morphisme de groupes est injectif ssi son noyau est trivial ; il réalise alors un isomorphisme sur son image.",
  r"**Sous-groupes finis de $\mathbb C^*$.** Le seul sous-groupe d'ordre $N$ de $\mathbb C^*$ est $\mathbb U_N$, cyclique."],
  [r"Pour un groupe de matrices, penser au morphisme $\det$ et calculer son noyau.",
   r"Un élément d'ordre $N$ vérifie $z^N=1$ : dans $\mathbb C$, cela place les éléments dans $\mathbb U_N$.",
   r"Réflexe : un sous-groupe fini d'un groupe commutatif « connu » (ici $\mathbb C^*$) se décrit par Lagrange."])
B['m-ccmp-04c'] = ([GEOM, SOMME_IND],
  [r"Écrire précisément l'ensemble des indices de la convolution ($1\le k\le n-1$ pour deux lois sur $\mathbb N^*$).",
   r"Pour $E$ et $V$ d'une somme de variables indépendantes : additionner, sans calculer la loi.",
   r"Reconnaître une loi de Pascal (temps d'attente du 2ᵉ succès)."])
B['m-ccmp-05a'] = ([
  r"**Filtre des racines de l'unité.** Avec $\omega=e^{2i\pi/p}$ : $\frac1p\sum_{j=0}^{p-1}\omega^{jm}=1$ si $p\mid m$, $0$ sinon.",
  r"**Loi de Poisson.** $P(X=n)=e^{-\lambda}\frac{\lambda^n}{n!}$.", TONELLI],
  [r"Pour sommer une série sur une classe de congruence, insérer le filtre des racines $p$-ièmes de l'unité.",
   r"Intervertir les sommes (convergence absolue) pour reconnaître des exponentielles $e^{\lambda\omega^j}$.",
   r"Vérifier sur $p=2$ : on retrouve $\mathrm{ch}$ et $\mathrm{sh}$ (indices pairs, impairs)."])
B['m-ccmp-05b'] = ([
  r"**Spectre d'une matrice antisymétrique réelle.** Ses valeurs propres complexes sont imaginaires pures ($0$ ou $\pm i\theta$).",
  r"**Valeurs propres de $\exp(A)$ et de $P(A)$.** Si $A$ est trigonalisable de valeurs propres $\lambda_k$, celles de $\exp(A)$ sont les $e^{\lambda_k}$ (avec multiplicités).",
  r"**Déterminant.** $\det M$ est le produit des valeurs propres complexes comptées avec multiplicité."],
  [r"Un déterminant de $f(A)$ se calcule par les valeurs propres : trigonaliser sur $\mathbb C$.",
   r"Regrouper les valeurs propres conjuguées : $(e^{i\varphi}+2)(e^{-i\varphi}+2)=|e^{i\varphi}+2|^2$.",
   r"Minorer $|e^{i\varphi}+2|\ge1$ par l'inégalité triangulaire."])
B['m-ccmp-06a'] = ([DIAG_DIM,
  r"**Base canonique de $\mathcal M_n$.** Les $E_{ij}$ (et les $PE_{ij}P^{-1}$) forment une base ; $E_{ij}E_{kl}=\delta_{jk}E_{il}$."],
  [r"Pour un endomorphisme de $\mathcal M_n$ du type $M\mapsto AMB$, tester sur les $PE_{ij}P^{-1}$ adaptés à la réduction de $A$.",
   r"Si $A=PDP^{-1}$, les $d_id_j$ sont valeurs propres de $\varphi$ : on obtient $n^2$ vecteurs propres libres.",
   r"Réciproque : partir d'un polynôme annulateur de $\varphi$ et l'appliquer à une matrice bien choisie."])
B['m-ccmp-06b'] = ([GENER,
  r"**Théorème de convergence monotone pour les séries.** Pour des termes positifs, $\lim_{t\to1^-}\sum a_nt^n=\sum a_n$ dans $[0,+\infty]$.", CV_NORM],
  [r"Moments factoriels : $E(X(X-1)\cdots(X-m+1))=G^{(m)}(1)$.",
   r"Tout se joue en $t=1$ : sur $[0,1[$, $G$ est $C^\infty$ (série entière de rayon $\ge1$).",
   r"Sens réciproque : croissance de $G^{(m)}$ sur $[0,1[$ et passage à la limite monotone."])
B['m-ccmp-07a'] = ([
  r"**Bijection réciproque.** Une fonction continue strictement monotone sur un intervalle réalise une bijection sur son image, de réciproque continue et de même monotonie.",
  r"**Séries de Bertrand.** $\sum\frac1{n\ln n}$ diverge ; plus généralement $\sum\frac1{n(\ln n)^\beta}$ converge ssi $\beta>1$.", EQUIV_SOMMES],
  [r"Pour un équivalent de $f^{-1}(y)$, partir de l'équation $x=y\ln x$ et prendre le logarithme.",
   r"Sommer des équivalents positifs d'une série divergente donne un équivalent des sommes partielles.",
   r"Comparaison série-intégrale : $\sum_{k\le n}\frac1{k\ln k}\sim\ln\ln n$."])
B['m-ccmp-07b'] = ([SPECTRAL, CHI_AB,
  r"**Similitude orthogonale.** Deux matrices symétriques réelles sont orthogonalement semblables ssi elles ont le même polynôme caractéristique."],
  [r"Pour comparer $AB$ et $BA$, penser à $\chi_{AB}=\chi_{BA}$ (densité de $GL_n$).",
   r"Deux matrices symétriques réelles : comparer les spectres suffit, grâce au théorème spectral.",
   r"Réflexe de densité : prouver un résultat polynomial pour les matrices inversibles puis passer à la limite."])
B['m-ccmp-08a'] = ([
  r"**Diviseurs.** Si $n=\prod p_i^{\alpha_i}$, le nombre de diviseurs est $\tau(n)=\prod(\alpha_i+1)$ ; $d\mapsto n/d$ est une involution des diviseurs."],
  [r"Produit des diviseurs : apparier $d$ et $n/d$, ce qui donne $n^{\tau(n)/2}$.",
   r"Ramener la question à une condition sur $\tau(n)$, puis utiliser la formule $\prod(\alpha_i+1)$.",
   r"$\tau(n)=4$ : $n=p^3$ ou $n=pq$ avec $p\neq q$ premiers."])
B['m-ccmp-08b'] = ([COMP,
  r"**Formule de duplication.** $\sin2a=2\sin a\cos a$, d'où le produit télescopique $\prod_{k=0}^N\cos\frac x{2^k}=\frac{\sin2x}{2^{N+1}\sin(x/2^N)}$."],
  [r"Une somme de logarithmes est le logarithme d'un produit : chercher un produit télescopique.",
   r"Équivalent : $\ln\cos u\sim-\frac{u^2}2$ en 0, d'où la convergence absolue.",
   r"Penser à multiplier par $\sin\frac x{2^N}$ pour faire « remonter » les doublements."])
B['m-ccmp-09'] = ([
  r"**Formule de la moyenne.** Si $f$ est continue et $g\ge0$ continue sur $[a,b]$, il existe $c\in[a,b]$ tel que $\int_a^bfg=f(c)\int_a^bg$.", CHGT],
  [r"Intégrales de Frullani $\int_0^\infty\frac{f(at)-f(bt)}t\,\mathrm dt$ : couper en $\varepsilon$, changer de variable dans chaque morceau et faire apparaître une intégrale sur $[a\varepsilon,b\varepsilon]$.",
   r"La formule de la moyenne permet d'extraire une valeur de $f$ et de faire tendre $\varepsilon\to0$.",
   r"Ne jamais séparer une intégrale semi-convergente sans couper d'abord loin du point délicat."])
B['m-ccmp-10b'] = ([
  r"**Similitude.** Deux matrices semblables ont même spectre (avec multiplicités), même trace, même déterminant.",
  r"**Réduction de Jordan / nilpotentes.** Une matrice nilpotente est semblable à une matrice triangulaire stricte, et $D^{-1}ND$ avec $D=\mathrm{diag}(1,c,\dots,c^{n-1})$ multiplie la $k$-ième surdiagonale par $c^k$."],
  [r"Si $cA\sim A$, le spectre est stable par multiplication par $c$ : un spectre fini non nul impose $c$ racine de l'unité.",
   r"Spectre réduit à $\{0\}$ $\iff$ nilpotente : c'est le seul cas où tous les $c$ conviennent.",
   r"Conjuguer par une matrice diagonale pour « mettre à l'échelle » les coefficients au-dessus de la diagonale."])
B['m-ccmp-11a'] = ([SPECTRAL,
  r"**Rayleigh.** Pour $M$ symétrique réelle : $\lambda_{\min}\|X\|^2\le X^{\top}MX\le\lambda_{\max}\|X\|^2$.",
  r"**Compacts de $\mathbb R^n$.** Ce sont les fermés bornés ; l'image réciproque d'un fermé par une application continue est fermée."],
  [r"Un ensemble défini par une inégalité large d'une fonction continue est fermé : seule la bornitude est en jeu.",
   r"Minorer une forme quadratique par $\lambda_{\min}\|X\|^2$.",
   r"Pour montrer qu'un ensemble n'est pas borné, avancer le long d'un vecteur propre associé à une valeur propre $\le0$."])
B['m-ccmp-11b'] = ([WEIERSTRASS,
  r"**Formule de Taylor avec reste intégral.** $f(x)=f(a)+f'(a)(x-a)+\int_a^x(x-t)f''(t)\,\mathrm dt$.",
  r"**Convexité.** $f$ de classe $C^2$ est convexe ssi $f''\ge0$ ; une limite simple de fonctions convexes est convexe."],
  [r"Pour approcher en conservant une propriété ($f''\ge0$), approcher la dérivée seconde puis intégrer deux fois.",
   r"Ajouter l'erreur $\varepsilon_n$ à l'approximation pour garantir la positivité.",
   r"Réflexe : Weierstrass + Taylor avec reste intégral pour approcher une fonction et ses dérivées."])
B['m-ccmp-12a'] = ([CHGT, TERM_INT,
  r"**Primitive usuelle.** $\int\frac{\mathrm dt}{(t-a)^2+b^2}=\frac1b\arctan\frac{t-a}b$."],
  [r"Mettre un trinôme sous forme canonique avant d'intégrer : on reconnaît une primitive en arctangente.",
   r"Simplifier avec les formules de l'angle moitié : $\frac{1-\cos x}{\sin x}=\tan\frac x2$.",
   r"Développer $\frac1{1-u}$ en série géométrique (avec $|u|<1$) et intégrer terme à terme en justifiant la convergence."])
B['m-ccmp-12b'] = ([TRIGO,
  r"**Changement de base.** Remplacer $e_i$ par $\alpha_ie_i$ multiplie le coefficient $t_{ij}$ par $\frac{\alpha_j}{\alpha_i}$."],
  [r"Commencer par trigonaliser, puis « écraser » le triangle supérieur par une dilatation $e_i\mapsto\varepsilon^ie_i$.",
   r"Le coefficient $t_{ij}$ devient $\varepsilon^{j-i}t_{ij}$, petit pour $j>i$.",
   r"Cette astuce sert aussi à montrer la densité des matrices diagonalisables dans $\mathcal M_n(\mathbb C)$."])
B['m-ccmp-13a'] = ([RANG,
  r"**Rang d'une somme.** $\mathrm{rg}(A+B)\le\mathrm{rg}A+\mathrm{rg}B$ ; $uv^{\top}$ est de rang 1 si $u,v\neq0$.",
  r"**Endomorphisme induit.** Si $F$ est stable par $u$, $\chi_{u_F}$ divise $\chi_u$ ; si $\mathrm{Im}\,u\subset F$, $\chi_u=X^{n-\dim F}\chi_{u_F}$."],
  [r"Décomposer la matrice en somme de matrices de rang 1 : $A=uv^{\top}+vu^{\top}$.",
   r"Travailler sur le plan $\mathrm{Vect}(u,v)$ qui contient l'image : tout se ramène à une matrice $2\times2$.",
   r"Exprimer les résultats avec des sommes ($S_1=\sum a^i$, $S_2=\sum a^{2i}$) plutôt qu'en développant."])
B['m-ccmp-13b'] = ([TAYLOR,
  r"**Concavité.** $f$ de classe $C^2$ est concave ssi $f''\le0$, ssi $f(x+s)+f(x-s)\le2f(x)$ pour tous $x,s$ admissibles."],
  [r"Pour une caractérisation intégrale, étudier $F(r)=\int_{x-r}^{x+r}f-2rf(x)$ au voisinage de $r=0$.",
   r"Dériver plusieurs fois $F$ et conclure par Taylor : le signe de $F$ près de 0 est celui de $f''(x)$.",
   r"Sens facile : intégrer l'inégalité de concavité en $s$."])
B['m-ccmp-14a'] = ([
  r"**Spectre d'une matrice antisymétrique réelle.** Ses valeurs propres complexes sont imaginaires pures, donc $I_n+A$ est inversible.",
  r"**Groupe orthogonal.** $C\in O_n(\mathbb R)\iff C^{\top}C=I_n$ ; $SO_n$ : de plus $\det C=1$.",
  r"**Polynômes en $A$.** Deux polynômes (ou fractions rationnelles) en $A$ commutent."],
  [r"Faire commuter $(I-A)$ et $(I+A)^{-1}$ pour calculer $C^{\top}C$.",
   r"Pour la non-surjectivité, chercher une matrice qui ne peut pas être atteinte ($-I_2$ : $-1$ valeur propre).",
   r"Transformation de Cayley : on inverse par $A=(I-C)(I+C)^{-1}$."])
B['m-ccmp-14b'] = ([DOM_CONT, TONELLI,
  r"**Fonctions $\Gamma$ et $\zeta$.** $\Gamma(s)=\int_0^{+\infty}t^{s-1}e^{-t}\,\mathrm dt$ ($s>0$) ; $\zeta(s)=\sum_{k\ge1}k^{-s}$ ($s>1$)."],
  [r"Développer $\frac1{e^t-1}=\sum_{k\ge1}e^{-kt}$ et intégrer terme à terme (termes positifs).",
   r"Pour la continuité, dominer sur un segment $[a,b]$ par $t^a+t^b$.",
   r"Le changement de variable $u=kt$ fait apparaître $\Gamma(x+1)/k^{x+1}$."])
B['m-ccmp-15a'] = ([
  r"**Suite géométrique bornée.** $(\lambda^n)_{n\in\mathbb Z}$ est bornée ssi $|\lambda|=1$.",
  r"**Suites croissantes de sous-espaces.** En dimension finie, une suite croissante de sous-espaces est stationnaire.", DIAG_POLY],
  [r"Vecteurs propres d'un décalage : chercher des suites géométriques.",
   r"Pour montrer la diagonalisabilité, prouver $\ker(u-\lambda)^2=\ker(u-\lambda)$ pour chaque valeur propre.",
   r"Exploiter la bornitude pour exclure les solutions qui croissent linéairement ($n\lambda^n$)."])
B['m-ccmp-15b'] = ([
  r"**Point extrémal.** $a\in A$ est extrémal s'il n'est le milieu d'aucun segment $[x,y]\subset A$ avec $x\ne y$.",
  r"**Convexité.** $A$ est convexe ssi il contient le segment joignant deux quelconques de ses points."],
  [r"Contraposée : si $A\setminus\{a\}$ n'est pas convexe, on obtient un segment de $A$ qui passe par $a$.",
   r"Symétriser : si $t\le\frac12$, le point $2a-x$ reste sur le segment et $a$ est un milieu.",
   r"Faire un dessin : la plupart des arguments de convexité se lisent sur une figure."])
B['m-ccmp-17a'] = ([
  r"**Équiprobabilité des ordres.** Dans un tirage sans remise complet, tous les ordres des boules sont équiprobables ; on peut oublier les boules qui ne jouent pas de rôle.",
  r"**Linéarité de l'espérance.** $E\left(\sum\mathbf 1_{A_i}\right)=\sum P(A_i)$, même si les événements ne sont pas indépendants."],
  [r"Supprimer les boules inutiles (ici les noires) : l'ordre relatif des autres reste uniforme.",
   r"Espérance d'un nombre d'objets vérifiant une propriété : somme d'indicatrices.",
   r"$P(\text{une rouge donnée sort avant les } c \text{ blanches})=\frac1{c+1}$ par symétrie."])
B['m-ccmp-17b'] = ([
  r"**Somme télescopique.** $g(x)-g(x/2^N)=\sum_{k<N}\left(g(x/2^k)-g(x/2^{k+1})\right)$.",
  r"**Série géométrique.** $\sum_{k\ge0}q^k=\frac1{1-q}$ pour $|q|<1$, utile pour sommer les $o(\sqrt{x/2^k})$."],
  [r"Deviner la forme du développement ($f(0)+\gamma\sqrt x$) puis ajuster $\gamma$ pour que la relation donnée se télescope.",
   r"Télescoper jusqu'à l'infini en utilisant la continuité en 0.",
   r"Majorer une somme de $o(\cdot)$ par un $\varepsilon$ fois une série géométrique."])
B['m-ccmp-17c'] = ([SPECTRAL,
  r"**Racine carrée d'une matrice définie positive.** Pour $A\in\mathcal S_n^{++}(\mathbb R)$, il existe $S\in\mathcal S_n^{++}$ avec $S^2=A$.",
  r"**Matrice antisymétrique réelle.** Elle est diagonalisable sur $\mathbb C$ (elle est normale), à valeurs propres imaginaires pures."],
  [r"Écrire $A=S^2$ et conjuguer : $S^{-1}(AB)S=SBS$ hérite de la symétrie de $B$.",
   r"Tester tout de suite le cas non inversible avec une matrice $2\times2$.",
   r"Réflexe : une matrice semblable à une matrice « sympathique » (symétrique, antisymétrique) hérite de sa diagonalisabilité."])
B['m-ccmp-19a'] = ([
  r"**Matrice non scalaire.** Si $u$ n'est pas une homothétie, il existe $x$ tel que $(x,u(x))$ soit libre.",
  r"**Trace.** Invariante par similitude, linéaire, $\mathrm{Tr}(AB)=\mathrm{Tr}(BA)$ ; une matrice nilpotente a une trace nulle."],
  [r"Lemme classique : une matrice de trace nulle est semblable à une matrice à diagonale nulle (récurrence sur $n$).",
   r"Une matrice à diagonale nulle est somme d'une triangulaire supérieure stricte et d'une inférieure stricte, toutes deux nilpotentes.",
   r"Commencer la base par $x,u(x)$ pour placer un 0 sur la diagonale."])
B['m-ccmp-19b'] = ([RIEMANN, CHGT],
  [r"Avant de calculer, étudier l'existence aux deux bornes avec des équivalents.",
   r"Changement de variable $u=\sqrt{1+tx}$ pour éliminer la racine.",
   r"$\int\frac{2\,\mathrm du}{u^2-1}=\ln\left|\frac{u-1}{u+1}\right|$ : décomposition en éléments simples."])
B['m-ccmp-20a'] = ([CSSA,
  r"**Dérivation terme à terme.** Si $\sum f_n$ converge simplement et $\sum f_n'$ converge uniformément sur tout segment, alors $\sum f_n$ est $C^1$ et $(\sum f_n)'=\sum f_n'$."],
  [r"Pour une série alternée de fonctions, majorer le reste uniformément par le premier terme négligé.",
   r"Les dérivées $k$-ièmes sont alternées à partir d'un rang indépendant de $x$ : convergence uniforme sur $[a,+\infty[$.",
   r"Pour une limite délicate, regrouper les termes deux à deux (transformation d'Abel ou moyenne $2g$)."])
B['m-ccmp-20b'] = ([DIAG_POLY, VP_POLY,
  r"**Racine simple.** $\lambda$ est racine simple de $P$ ssi $P(\lambda)=0$ et $P'(\lambda)\neq0$."],
  [r"$P'(A)$ inversible $\iff$ $P'$ ne s'annule sur aucune valeur propre : toutes les valeurs propres sont racines simples de $P$.",
   r"Le polynôme minimal divise $P$ : il est alors scindé à racines simples.",
   r"Contre-exemple rapide : $A=I_n$ et $P=(X-1)^2$."])
B['m-ccmp-21b'] = ([
  r"**Inégalité triangulaire.** $\big|\|a\|-\|b\|\big|\le\|a\pm b\|\le\|a\|+\|b\|$.",
  r"**Pythagore.** Si $u\perp v$, $\|u+v\|^2=\|u\|^2+\|v\|^2$."],
  [r"Condition nécessaire par l'inégalité triangulaire ; condition suffisante en construisant un point explicite.",
   r"Pour deux sphères, travailler dans un plan contenant les centres (d'où l'hypothèse $n\ge2$).",
   r"Chercher le point sous la forme $c_1+\alpha u+\beta v$ avec $u$ unitaire selon $c_1c_2$ et $v\perp u$."])
B['m-ccmp-24b'] = ([
  r"**Trace d'une matrice nilpotente.** Toutes ses puissances ont une trace nulle (valeurs propres nulles).",
  r"**Forme $\mathrm{Tr}(S^2)$.** Pour $S$ symétrique réelle, $\mathrm{Tr}(S^2)=\sum s_{ij}^2>0$ si $S\neq0$.",
  r"**Formule de Grassmann.** $\dim(F+G)=\dim F+\dim G-\dim(F\cap G)$."],
  [r"Majorer la dimension d'un sous-espace en montrant qu'il est en somme directe avec un sous-espace connu.",
   r"$\dim\mathcal S_n=\frac{n(n+1)}2$ : il reste au plus $\frac{n(n-1)}2$.",
   r"Cas d'égalité : les matrices triangulaires supérieures strictes."])
B['m-ccmp-25a'] = ([IPP,
  r"**Inégalité de Wirtinger.** Si $f$ est $C^1$ sur $[0,1]$ avec $f(0)=f(1)=0$ : $\int_0^1f'^2\ge\pi^2\int_0^1f^2$, avec égalité ssi $f=\lambda\sin(\pi t)$."],
  [r"Pour démontrer une inégalité $\int f'^2\ge c\int f^2$, développer $\int(f'-gf)^2\ge0$ avec une fonction $g$ bien choisie ($\pi\cot\pi t$).",
   r"$ff'=\frac12(f^2)'$ : intégrer par parties pour faire disparaître $f'$.",
   r"Contrôler les bornes : $f(t)=O(t)$ compense la singularité de $\cot(\pi t)$."])
B['m-ccmp-26a'] = ([
  r"**Formule de Moivre et binôme.** $\cos(n\theta)+i\sin(n\theta)=(\cos\theta+i\sin\theta)^n=\sum\binom nk\cos^{n-k}\theta\,(i\sin\theta)^k$.",
  r"**Polynôme scindé.** Un polynôme de degré $d$ avec $d$ racines distinctes connues s'écrit $c\prod(X-x_i)$."],
  [r"Exprimer $\sin(2n\theta)$ ou $\frac{\sin(2n\theta)}{\sin\theta}$ comme polynôme en $\cos\theta$ grâce au binôme.",
   r"Les racines sont des $\cos\frac{k\pi}{2n}$ : les regrouper par paires opposées.",
   r"Calculer une même quantité ($P'(0)$) de deux façons pour obtenir le produit des cosinus."])
B['m-ccmp-27a'] = ([
  r"**Extremum d'une fonction d'une variable.** En un minimum local intérieur, $\varphi'(0)=0$ et, si $\varphi$ est $C^2$, $\varphi''(0)\ge0$."],
  [r"Restreindre une fonction de plusieurs variables aux droites passant par le point : on se ramène à une variable.",
   r"$\varphi_i''(0)=\partial_i^2f(a)$ pour $\varphi_i(t)=f(a+te_i)$.",
   r"Le laplacien est la somme des $\partial_i^2f$, d'où son signe en un minimum."])
B['m-ccmp-27b'] = ([VP_POLY,
  r"**Factorisation sur $\mathbb C$.** $p(X)-\mu=c\prod(X-\alpha_k)$ ; $p(u)-\mu\,\mathrm{id}=c\prod(u-\alpha_k\mathrm{id})$ n'est pas injectif ssi l'un des facteurs ne l'est pas."],
  [r"Inclusion facile : $p(\mathrm{Sp}\,u)\subset\mathrm{Sp}\,p(u)$ par $p(u)x=p(\lambda)x$.",
   r"Inclusion réciproque : factoriser $p(X)-\mu$ et utiliser qu'un produit d'endomorphismes injectifs est injectif.",
   r"Le résultat utilise que $\mathbb C$ est algébriquement clos : il peut tomber en défaut sur $\mathbb R$."])
B['m-ccmp-27c'] = ([BT,
  r"**Croissance de l'espérance.** Si $X\le Y$ (et ces variables ont une espérance), alors $E(X)\le E(Y)$."],
  [r"Comparer des variables aléatoires point par point, puis prendre l'espérance.",
   r"$\mathbf 1_{\{X\ge a\}}\le\frac{h(X)}{h(a)}$ dès que $h$ est positive croissante.",
   r"Cas particuliers : $h(x)=x^2$ (Bienaymé-Tchebychev), $h(x)=e^{tx}$ (inégalités de Chernoff)."])
B['m-ccmp-28a'] = ([
  r"**Projecteur.** $p^2=p$ ; alors $E=\mathrm{Im}\,p\oplus\ker p$ et $\mathrm{rg}\,p=\mathrm{Tr}\,p$.",
  r"**Translations dans un groupe.** Pour $g\in G$, $h\mapsto gh$ est une bijection de $G$."],
  [r"Moyenner sur un groupe fini : $p=\frac1n\sum g$ est un projecteur sur les vecteurs fixes.",
   r"Réindexer les sommes avec la bijection $h\mapsto g_ih$.",
   r"Dimension de l'image d'un projecteur = sa trace : $\dim\mathrm{Fix}=\frac1n\sum\mathrm{Tr}(g)$."])
B['m-ccmp-28b'] = ([DOM_DERIV,
  r"**Intégrale de Dirichlet.** $\int_0^{+\infty}\frac{\sin t}t\,\mathrm dt=\frac\pi2$ (semi-convergente)."],
  [r"Introduire un paramètre $e^{-xt}$ qui rend l'intégrale absolument convergente et dérivable.",
   r"$f'(x)=-\frac1{1+x^2}$ : intégrer et déterminer la constante par la limite en $+\infty$.",
   r"Continuité en 0 : délicate (pas de domination simple), à traiter par une intégration par parties."])
