# Bilans — distributions et calcul différentiel & probabilités
B = {}
B['n-dist-heaviside'] = ([r"**Dérivée d'une distribution.** $T'(\varphi)=-T(\varphi')$.", r"**Masse de Dirac.** $\delta(\varphi)=\varphi(0)$."],
  [r"Un saut de hauteur $h$ produit $h\,\delta$ dans la dérivée.", r"Tester contre $\varphi(x/\varepsilon)$ pour concentrer en un point.", r"Découper l'intégrale au point singulier, puis intégrer par parties."])
B['n-dist-equations'] = ([r"**Primitive à support compact** d'une fonction test d'intégrale nulle.", r"**Lemme de division.** $\sigma(0)=0\Rightarrow\sigma(x)=x\int_0^1\sigma'(tx)\,\mathrm dt$."],
  [r"Décomposer une fonction test : partie « facile » plus composante le long d'une fonction fixée.", r"Une solution particulière plus les solutions homogènes, comme pour les équations différentielles.", r"$xT=0$ : la distribution est concentrée là où $x$ s'annule."])
B['n-dist-convergence'] = ([r"**Convergence dominée.**", r"**Inégalité des accroissements finis.**"],
  [r"Changement de variable $u=nx$ pour voir la concentration en $0$.", r"Les oscillations rapides tendent vers $0$ par intégration par parties.", r"La convergence des dérivées vient gratuitement de $T'(\varphi)=-T(\varphi')$."])
B['n-cdp-regression'] = ([r"**Point critique** : gradient nul sur un ouvert.", r"**Taylor à l'ordre 2**, exact pour un polynôme de degré 2 ; hessienne définie positive."],
  [r"Développer le carré et utiliser la linéarité de l'espérance.", r"Une matrice symétrique $2\times2$ est définie positive ssi déterminant et trace sont $>0$.", r"Le minimum d'une erreur quadratique est une variance : il est positif."])
B['n-cdp-laplace'] = ([r"**Règle de la chaîne** pour $\ln L$.", r"**Variance d'une combinaison** : ${}^tw\Sigma w=V(uX+vY)\ge0$."],
  [r"La hessienne de $\ln E(e^{xX+yY})$ est une matrice de covariance.", r"Pondérer la loi par $e^{xX+yY}$ pour ramener un point quelconque à l'origine.", r"Convexité en plusieurs variables : vérifier sur chaque droite."])
B['n-cdp-entropie'] = ([r"**Extrema liés.** $\nabla f(a)$ colinéaire à $\nabla g(a)$.", r"**Inégalité** $\ln x\le x-1$, égalité ssi $x=1$."],
  [r"Le calcul différentiel donne un candidat ; une inégalité prouve le maximum global, bord compris.", r"Inégalité de Gibbs : $\sum p_i\ln\frac{q_i}{p_i}\le0$.", r"À espérance fixée, l'entropie est maximale pour une loi exponentielle."])
