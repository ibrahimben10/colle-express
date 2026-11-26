# Bilans — exercices dans l'esprit des oraux Mines-Ponts (n-mp-*)
B = {}
B['n-mp-racine'] = ([r"**Critère de diagonalisabilité.** Diagonalisable ⇔ annule un polynôme scindé à racines simples.",
  r"**Composition.** Si $Q$ annule $A^2$, alors $Q(X^2)$ annule $A$."],
  [r"Pour remonter de $f(A)$ à $A$, composer un annulateur de $f(A)$ avec $f$.",
   r"Vérifier séparément que $\alpha\ne-\alpha$ (non-nullité) et que $\alpha_i\ne\pm\alpha_j$ (carrés distincts).",
   r"Deux contre-exemples réflexes : une nilpotente non nulle, une rotation d'angle $\pi/2$ sur $\mathbb R$."])
B['n-mp-commutant'] = ([r"**Stabilité.** Si $u$ et $v$ commutent, les sous-espaces propres de $u$ sont stables par $v$.",
  r"**Interpolation de Lagrange.** $n$ points distincts, $n$ valeurs : un unique polynôme de degré $\le n-1$."],
  [r"Valeurs propres distinctes ⇒ droites propres ⇒ tout commutant est diagonal dans la même base.",
   r"$\mathbb K[u]\subset\mathcal C(u)$ toujours ; l'égalité se prouve par Lagrange ou par les dimensions.",
   r"Tester sur $u=\mathrm{Id}$ pour voir que l'hypothèse est indispensable."])
B['n-mp-tracerang'] = ([r"**Théorème spectral.** $A\in\mathcal S_n(\mathbb R)$ est diagonalisable en base orthonormée ; son rang est le nombre de valeurs propres non nulles.",
  r"**Cauchy-Schwarz.** $(\sum x_iy_i)^2\le\sum x_i^2\sum y_i^2$, égalité ssi colinéarité."],
  [r"Trace, trace du carré et rang d'une symétrique se lisent sur les valeurs propres.",
   r"Comparer une somme à la somme des carrés : Cauchy-Schwarz contre $(1,\dots,1)$.",
   r"Projecteur orthogonal : valeurs propres $0$ et $1$, donc rang = trace."])
B['n-mp-geom'] = ([r"**Loi géométrique.** $P(X=k)=q^{k-1}p$, $P(X>k)=q^k$.",
  r"**Survie et minimum.** $P(\min(X,Y)>k)=P(X>k)P(Y>k)$ si $X$ et $Y$ sont indépendantes."],
  [r"Pour un minimum, passer par la fonction de survie.",
   r"$P(X=Y)$ : probabilités totales sur la valeur commune, puis série géométrique.",
   r"Exploiter la symétrie : $P(X<Y)=P(Y<X)$."])
B['n-mp-involutions'] = ([r"**Dérivation terme à terme** d'une série entière sur $]-R,R[$.",
  r"**Produit de Cauchy** et **unicité des coefficients** d'une série entière."],
  [r"Dénombrement : regarder ce que devient le dernier élément.",
   r"Majorer $a_n$ par $n!$ pour obtenir un rayon minimal.",
   r"Série génératrice exponentielle : la récurrence devient une équation différentielle."])
B['n-mp-logint'] = ([r"**Dérivation sous l'intégrale** avec domination indépendante du paramètre.",
  r"**Intégrale de référence.** $\int_0^{+\infty}e^{at}\,\mathrm dt=-\frac1a$ pour $\operatorname{Re}a<0$."],
  [r"Dériver par rapport au paramètre pour faire disparaître un facteur $\frac1t$ gênant.",
   r"Calculer $\int e^{-t}\sin(xt)$ comme partie imaginaire d'une exponentielle complexe.",
   r"Fixer la constante avec une valeur simple du paramètre ($F(0)=0$)."])
B['n-mp-sinrac'] = ([r"**Séries alternées.** $\sum(-1)^na_n$ converge si $(a_n)$ décroît vers $0$.",
  r"**Développement de $(1+x)^\alpha$** en $0$."],
  [r"$\sin(\pi n+h)=(-1)^n\sin h$ : factoriser l'entier le plus proche.",
   r"Terme de signe non constant : développement asymptotique, partie alternée + reste $O(n^{-\alpha})$, $\alpha>1$.",
   r"Toujours vérifier d'abord que le terme général tend vers $0$."])
B['n-mp-deuxcarres'] = ([r"**Factorisation dans $\mathbb C[X]$** et racines conjuguées d'un polynôme réel.",
  r"**Signe et multiplicité.** Une racine réelle de multiplicité impaire fait changer le signe."],
  [r"$A^2+B^2=(A+iB)(A-iB)$ : chercher $P=Q\overline Q$.",
   r"Prendre la moitié de chaque racine réelle et une racine par paire conjuguée.",
   r"Sur un exemple, compléter le carré : $X^4+1=(X^2-1)^2+2X^2$."])
B['n-mp-sinc'] = ([r"**Cauchy-Lipschitz linéaire** sur un intervalle où l'équation est sous forme résolue.",
  r"**Unicité des coefficients** d'une série entière."],
  [r"$(xy)''=xy''+2y'$ : reconnaître une dérivée de produit.",
   r"Recollement en un point singulier : imposer la bornitude et la continuité.",
   r"Hors du cadre de Cauchy-Lipschitz, la dimension de l'espace des solutions peut changer."])
B['n-mp-chiab'] = ([r"**Densité de $GL_n(\mathbb C)$** dans $\mathcal M_n(\mathbb C)$.",
  r"**Prolongement par continuité** d'une identité vraie sur une partie dense."],
  [r"Approcher $A$ par $A-\frac1pI_n$, inversible pour $p$ grand.",
   r"Prouver d'abord une identité pour $A$ inversible, puis passer à la limite.",
   r"Même polynôme caractéristique n'implique pas semblables : comparer à la matrice nulle."])
