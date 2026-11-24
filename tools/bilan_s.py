# Bilans — exercices tirés des sujets de concours (n-s-*)
from bilan_lib import *
B = {}

B['n-s-x-kron'] = ([r"**Sommes de Newton.** Si $P=X^d+c_{d-1}X^{d-1}+\dots+c_0$ a pour racines $\lambda_k$, alors $s_{n+d}+c_{d-1}s_{n+d-1}+\dots+c_0s_n=0$.",
  r"**Éléments simples.** La décomposition d'une fraction rationnelle est unique ; ses pôles se lisent sur les dénominateurs."],
  [r"Une suite d'entiers bornée vérifiant une récurrence linéaire est périodique à partir d'un rang (tiroirs sur les blocs de $d$ termes).",
   r"Série génératrice des sommes de Newton : $\sum_ns_nt^n=\sum_k\frac1{1-\lambda_kt}$.",
   r"Contre-exemple utile : sans coefficients entiers, le résultat tombe ($X-\frac12$)."])
B['n-s-x-newton'] = ([r"**Dérivée logarithmique.** $\frac{P'}P=\sum_k\frac1{X-a_k}$ pour $P$ scindé, d'où $\big(\frac{P'}P\big)'=-\sum\frac1{(X-a_k)^2}$.",
  r"**Rolle.** La dérivée d'un polynôme scindé sur $\mathbb R$ est scindée sur $\mathbb R$."],
  [r"Coefficients et dérivées : $a_k=\frac{P^{(k)}(0)}{k!}$ ; ramener une inégalité sur des coefficients à une inégalité en un point.",
   r"$QQ''\le Q'^2$ exprime que $\ln|Q|$ est concave entre deux racines.",
   r"Exemple de contrôle : $(1+X)^n$ et la log-concavité des coefficients binomiaux."])
B['n-s-x-fekete'] = ([r"**Limites supérieure et inférieure.** $u_n\to\ell$ ssi $\limsup u_n\le\ell\le\liminf u_n$."],
  [r"Sous-additivité : découper $n=aq+r$ en blocs de taille fixée $q$, puis faire varier $q$.",
   r"Version multiplicative : $u_{n+m}\le u_nu_m$ donne la convergence de $u_n^{1/n}$ (passer au logarithme).",
   r"Application classique : $\|A^n\|^{1/n}$ converge (vers le rayon spectral)."])
B['n-s-x-ideaux'] = ([r"**Borel-Lebesgue.** De tout recouvrement ouvert d'un compact on extrait un sous-recouvrement fini.",
  r"**Idéal et inversible.** Un idéal qui contient un élément inversible est l'anneau entier."],
  [r"Fabriquer un élément inversible dans l'idéal : sommer des carrés, qui ne se compensent pas.",
   r"$M_a$ est le noyau de l'évaluation en $a$, morphisme surjectif vers le corps $\mathbb R$ : il est maximal.",
   r"La compacité est indispensable : le résultat est faux sur $]0,1]$."])
B['n-s-x-comm'] = ([r"**Codiagonalisation.** Des endomorphismes diagonalisables qui commutent deux à deux sont diagonalisables dans une base commune.",
  r"**Interpolation de Lagrange.** Pour des points distincts, on prescrit les valeurs d'un polynôme."],
  [r"Une famille infinie se ramène à une base finie de l'espace qu'elle engendre.",
   r"Pour que $f=L(g)$ avec $g$ diagonal, il suffit que $g$ sépare les vecteurs propres de valeurs propres différentes pour $f$.",
   r"Des polynômes en un même $g$ commutent : la commutation est nécessaire."])
B['n-s-x-unip'] = ([r"**Cayley-Hamilton.** $\chi_A(A)=0$.", DSE],
  [r"Une série entière évaluée en une matrice nilpotente est un polynôme : on peut définir $\sqrt{I+N}$, $\ln(I+N)$, $e^N$.",
   r"Tronquer une série à l'ordre $n-1$ conserve les identités modulo $X^n$.",
   r"Les coefficients $\binom{1/2}k$ sont rationnels : la racine reste dans $\mathcal M_n(\mathbb Q)$."])
B['n-s-x-traces'] = ([TRIGO, r"**Continuité de la somme.** La somme d'une série entière est continue sur le disque ouvert de convergence."],
  [r"Traces des puissances = sommes de Newton des valeurs propres.",
   r"Lire les valeurs propres dans les pôles de $\sum_n\mathrm{Tr}(u^n)t^n=\sum_k\frac1{1-\lambda_kt}$.",
   r"Une valeur propre de module $>1$ fait exploser les traces : c'est ce que formalise le rayon de convergence."])
B['n-s-x-hoeff'] = ([BT, r"**Convexité.** Une fonction convexe est sous ses cordes."],
  [r"Méthode de Chernoff : $\mathbb P(S\ge s)\le e^{-\lambda s}\mathbb E(e^{\lambda S})$, puis optimiser en $\lambda>0$.",
   r"Indépendance : l'espérance d'un produit de fonctions des $X_i$ est le produit des espérances.",
   r"Hoeffding donne une décroissance exponentielle, bien meilleure que Bienaymé-Tchebychev pour les grandes déviations."])
B['n-s-x-derang'] = ([r"**Formule du crible.** $\big|\bigcup A_i\big|=\sum_k(-1)^{k+1}\sum_{i_1<\dots<i_k}|A_{i_1}\cap\dots\cap A_{i_k}|$.",
  r"**Formule de Leibniz.** $\det M=\sum_\sigma\varepsilon(\sigma)\prod_jm_{\sigma(j),j}$.", CSSA],
  [r"Une somme de signatures sur des permutations contraintes est souvent un déterminant bien choisi.",
   r"$J_n$ (que des $1$) a pour valeurs propres $n$ et $0$ : $\det(J_n-I_n)=(-1)^{n-1}(n-1)$.",
   r"Proportion de dérangements : $\frac{D(n)}{n!}\to\frac1e$."])
B['n-s-x-sompuis'] = ([r"**Petit théorème de Fermat.** $p$ premier, $p\nmid k$ : $k^{p-1}\equiv1\pmod p$.",
  r"**Théorème d'Euler.** $k\wedge N=1$ : $k^{\varphi(N)}\equiv1\pmod N$."],
  [r"Pour une somme $\sum_{k=1}^{n-1}k^m$ modulo $n$, apparier $k$ et $n-k$.",
   r"Pour un entier pair, raisonner modulo la plus grande puissance de $2$ qui le divise.",
   r"Tester les petites valeurs ($n=2,3,4,5$) pour deviner la réponse."])

B['n-s-a-expo'] = ([r"**Lagrange.** L'ordre d'un élément d'un groupe fini divise le cardinal du groupe.",
  r"**Racines dans un corps.** Un polynôme de degré $r$ a au plus $r$ racines dans un corps."],
  [r"Ordres premiers entre eux : $\langle a\rangle\cap\langle b\rangle=\{1\}$ et $\mathrm{ord}(ab)=mn$ (groupe abélien).",
   r"Un élément d'ordre maximal a un ordre multiple de tous les autres (groupe abélien).",
   r"Conséquence : $(\mathbb Z/p\mathbb Z)^*$ et les racines de l'unité forment des groupes cycliques."])
B['n-s-a-deuxn'] = ([r"**Indicatrice d'Euler.** $\varphi(2^n)=2^{n-1}$.",
  r"**Groupe cyclique.** Un groupe fini de cardinal $N$ est cyclique ssi il a un élément d'ordre $N$."],
  [r"Pour montrer qu'un groupe n'est pas cyclique, majorer l'ordre de tous ses éléments.",
   r"Élever au carré $1+2^nm$ fait gagner une puissance de $2$.",
   r"$(\mathbb Z/8\mathbb Z)^*$ est le groupe de Klein : tous les éléments non triviaux sont d'ordre $2$."])
B['n-s-a-heis'] = ([r"**Sous-groupe.** Neutre, stabilité par produit et par inverse.",
  r"**Binôme.** $(I+N)^p=\sum\binom pkN^k$ si $I$ et $N$ commutent ; $p\mid\binom pk$ pour $1\le k\le p-1$."],
  [r"Écrire une matrice unitriangulaire $I+N$ avec $N$ nilpotente pour calculer ses puissances.",
   r"Le cas $p=2$ est différent : le terme $\frac{p(p-1)}2N^2$ ne s'annule plus.",
   r"Tester la commutativité sur deux générateurs simples."])
B['n-s-a-pxx'] = ([r"**Coefficient dominant.** Celui d'un produit est le produit des coefficients dominants.",
  r"**Factorisation.** Un polynôme unitaire de $\mathbb C[X]$ est produit de $(X-\lambda)^{m_\lambda}$."],
  [r"Équation fonctionnelle polynomiale : étudier l'ensemble des racines et ses stabilités.",
   r"Un ensemble fini stable par $z\mapsto z^2$ ne contient que $0$ et des points de module $1$.",
   r"Toujours vérifier la réponse dans l'équation : ici $(X^2-X)^n$, et non $(X^2-X+1)^n$."])
B['n-s-a-pu'] = ([r"**Rigidité.** Deux polynômes égaux en une infinité de points sont égaux.",
  r"**Conjugué sur le cercle.** $|z|=1\Rightarrow\bar z=\frac1z$."],
  [r"Polynôme réciproque $P^*=X^n\overline P(1/X)$ : sur le cercle, $\overline{P(z)}=z^{-n}P^*(z)$.",
   r"Transformer une condition de module en identité polynomiale en multipliant par $\overline{P}$.",
   r"Pour les fractions rationnelles, les produits de Blaschke $\frac{X-a}{1-\bar aX}$ apparaissent."])
B['n-s-a-pprime'] = ([r"**Dérivée logarithmique.** $\big(\frac{P'}P\big)'=-\sum\frac1{(X-a_k)^2}$ pour $P$ scindé à racines simples.",
  r"**Racine simple.** $P(a)=0$ et $P'(a)\neq0$."],
  [r"Traiter séparément les racines de $P$ et les autres points.",
   r"$P'^2-PP''>0$ sur $\mathbb R$ pour $P$ réel scindé : c'est l'inégalité de Laguerre.",
   r"Contre-exemple utile avec une racine double : $P=X^2$."])
B['n-s-a-quot'] = ([r"**Racines de $X^k-1$.** Les racines $k$-ièmes de l'unité, simples ; une racine commune à $X^p-1$ et $X^q-1$ est racine de $X^{p\wedge q}-1$.",
  r"**Division euclidienne.** Par un polynôme unitaire de $\mathbb Z[X]$, elle se fait dans $\mathbb Z[X]$."],
  [r"Divisibilité dans $\mathbb C[X]$ : comparer racines et multiplicités.",
   r"Passer de $\mathbb C[X]$ à $\mathbb Z[X]$ par unicité de la division euclidienne.",
   r"Évaluer en $1$ un quotient de $1-X^k$ en le réécrivant avec des sommes géométriques."])
B['n-s-a-mahler'] = ([r"**Relations coefficients-racines.** Pour $P$ unitaire, $a_{n-j}=(-1)^j\sigma_j(\lambda_1,\dots,\lambda_n)$."],
  [r"Majorer un produit partiel de nombres $\ge1$ par le produit complet.",
   r"$\sum_j\binom nj=2^n$.",
   r"Cas d'égalité typique : toutes les racines sur le cercle unité, de même argument, comme $(X+1)^n$."])
B['n-s-a-cinq'] = ([r"**Polynômes réels.** Les racines non réelles vont par paires conjuguées.",
  r"**Polynôme minimal.** Si $\Phi$ est irréductible et annule $\omega$, aucun polynôme non nul de degré $<\deg\Phi$ n'annule $\omega$."],
  [r"Relation $1+\omega+\dots+\omega^4=0$ : majoration immédiate de la dimension.",
   r"Polynôme réciproque : diviser par $X^2$ et poser $c=X+X^{-1}$.",
   r"Pour $p$ premier, les racines $p$-ièmes de l'unité engendrent un $\mathbb Q$-espace de dimension $p-1$."])
B['n-s-a-proj'] = ([RANG, r"**Projecteur.** $p^2=p$ ; alors $E=\mathrm{Im}\,p\oplus\ker p$."],
  [r"Formule de Grassmann : $\dim(F+G)=\dim F+\dim G-\dim(F\cap G)$.",
   r"Un vecteur qui est à la fois dans $\mathrm{Im}\,p$ et dans $\mathrm{Im}\,q$ est nul dès que la somme est directe.",
   r"$p+q=\mathrm{Id}$ entraîne que $p$ et $q$ commutent."])

B['n-s-n-se1'] = ([RAYON, DSE],
  [r"Décomposer le coefficient en éléments simples en $n$, puis réindexer chaque série.",
   r"Abel radial : si $\sum a_n$ converge, la somme de la série entière tend vers $\sum a_n$ en $1^-$.",
   r"Contrôler une formule par son développement limité en $0$."])
B['n-s-n-arcsin'] = ([DSE, r"**Unicité du développement.** Une série entière nulle au voisinage de $0$ a tous ses coefficients nuls."],
  [r"Coefficients d'un produit : passer par une équation différentielle plutôt que par un produit de Cauchy.",
   r"$1\cdot3\cdots(2n-1)=\frac{(2n)!}{2^nn!}$.",
   r"Parité : une fonction impaire n'a que des coefficients d'indice impair."])
B['n-s-n-nfact'] = ([RAYON, TERM_INT, CSSA, r"**Stirling.** $n!\sim\sqrt{2\pi n}\big(\frac ne\big)^n$."],
  [r"Écrire un coefficient comme une intégrale pour intervertir série et intégrale.",
   r"Au bord du disque : Stirling pour la nature, monotonie de $(1+\frac1n)^{n+1}$ pour l'alternée.",
   r"$\max_{t\ge0}te^{-t}=\frac1e$ fixe exactement le rayon $e$."])
B['n-s-n-interv'] = ([TERM_INT],
  [r"Avant d'intervertir, vérifier $\sum\int|f_n|<+\infty$ : c'est l'hypothèse qui échoue le plus souvent.",
   r"Changement de variable $u=nx$ pour calculer $\int|f_n|$.",
   r"Contre-exemple à retenir : $\sum\int f_n=0$ mais $\int\sum f_n=\ln2$."])
B['n-s-n-conj'] = ([r"**Sommation par paquets.** Pour une famille positive, on somme dans n'importe quel ordre.",
  r"**Indépendance.** $\mathbb P(X=i,Y=j)=\mathbb P(X=i)\mathbb P(Y=j)$ pour tous $i,j$."],
  [r"$\sum ix^i=\frac x{(1-x)^2}$ et $\sum i^2x^i=\frac{x(1+x)}{(1-x)^3}$ ; en $\frac12$ : $2$ et $6$.",
   r"Pour réfuter l'indépendance, chercher un couple de probabilité nulle dont les marginales ne le sont pas.",
   r"Une loi conjointe symétrique donne deux marginales identiques."])
B['n-s-n-poisson'] = ([r"**Loi de Poisson.** $\mathbb P(Y=k)=e^{-\lambda}\frac{\lambda^k}{k!}$, d'espérance et de variance $\lambda$."],
  [r"$\big(1+\frac xn\big)^n\to e^x$ : passer au logarithme.",
   r"Approximation de Poisson : $n$ grand, $p$ petit, $np=\lambda$ modéré.",
   r"Séparer le coefficient binomial en un produit de $k$ facteurs qui tendent vers $1$."])
B['n-s-n-ed1'] = ([r"**Structure des solutions.** Sur un intervalle où le coefficient de $y''$ ne s'annule pas, les solutions d'une équation linéaire homogène d'ordre $2$ forment un plan.", DSE],
  [r"Point singulier : résoudre sur chaque demi-droite, puis recoller en imposant la régularité.",
   r"Recherche en série entière : écrire la relation de récurrence et séparer les indices modulo la période.",
   r"Reconnaître $\mathrm{ch}(x^2)$ et $\mathrm{sh}(x^2)$ dans les coefficients $\frac1{(2p)!}$ et $\frac1{(2p+1)!}$."])
B['n-s-n-ed2'] = ([r"**Variation des constantes.** Pour $y''-y=f$ : $\lambda'=f\,\mathrm{ch}$, $\mu'=-f\,\mathrm{sh}$ avec $y=\lambda\,\mathrm{sh}+\mu\,\mathrm{ch}$."],
  [r"Choisir la base $(\mathrm{sh},\mathrm{ch})$ : le wronskien vaut $\mathrm{ch}^2-\mathrm{sh}^2=1$.",
   r"$\int\frac{dt}{\mathrm{ch}\,t}=2\arctan(e^t)$.",
   r"Toujours vérifier la solution particulière en la dérivant deux fois."])
B['n-s-n-transp'] = ([r"**Règle de la chaîne.** $\partial_u(f\circ\varphi)=\partial_xf\,\partial_u\varphi_1+\partial_yf\,\partial_u\varphi_2$.",
  r"**Dérivée nulle.** Une fonction de dérivée nulle sur un intervalle est constante."],
  [r"Équation de transport $a\partial_xf+b\partial_yf=0$ : solutions $\varphi(bx-ay)$.",
   r"Changement de variables linéaire qui redresse la direction de dérivation.",
   r"Un second membre proportionnel à $f$ se traite par un facteur exponentiel."])
B['n-s-n-ed3'] = ([r"**Structure des solutions.** Solution générale = solution particulière + solution de l'équation homogène $\lambda e^{2x}+\mu e^{-2x}$."],
  [r"Une solution particulière s'écrit avec des intégrales « vers l'infini » adaptées à chaque exponentielle.",
   r"Hors du support de $f$, la solution est une combinaison de $e^{2x}$ et $e^{-2x}$ : lire les limites.",
   r"Condition d'existence d'une solution à support compact : $f$ orthogonale aux solutions $e^{\pm2t}$ de l'équation homogène."])
