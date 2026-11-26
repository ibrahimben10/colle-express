# Bilans — exercices difficiles (probabilités, réduction, topologie)
B = {}
B['n-mp-polya'] = ([r"**Probabilités totales** sur le système complet $(R_n=j)_j$.", r"**Loi uniforme** sur un ensemble fini."],
  [r"Calculer les premiers cas à la main pour deviner la loi.", r"Une transition qui ne fait passer que de $j$ à $j$ ou $j+1$ : deux termes seulement dans les probabilités totales.", r"Pour la couleur du tirage suivant, conditionner par l'état de l'urne."])
B['n-mp-glnp'] = ([r"**Corps $\mathbb Z/p\mathbb Z$** : un sous-espace de dimension $k$ a $p^k$ éléments.", r"**Inégalité de Weierstrass.** $\prod(1-a_j)\ge1-\sum a_j$ pour $a_j\in[0,1]$."],
  [r"Compter les bases colonne par colonne.", r"Produit infini : passer au logarithme et comparer $\ln(1-x)$ à $-x$.", r"Si une minoration est triviale, isoler le premier facteur."])
B['n-mp-commutateur'] = ([r"**Trace.** $\operatorname{tr}(XY-YX)=0$, invariance par similitude.", r"**Homothéties.** Tout vecteur propre ⇒ homothétie."],
  [r"Un vecteur non propre $x$ donne une base $(x,u(x),\dots)$ où le coefficient $(1,1)$ est nul.", r"Récurrence par blocs : le bloc restant garde une trace nulle.", r"$(DB-BD)_{ij}=(i-j)b_{ij}$ avec $D$ diagonale à coefficients distincts."])
B['n-mp-nilptr'] = ([r"**Trigonalisation.** $\operatorname{tr}(A^k)=\sum\lambda_i^k$.", r"**Vandermonde.** $\det(x_i^{j-1})=\prod_{i<j}(x_j-x_i)$."],
  [r"Les traces des puissances déterminent les valeurs propres avec multiplicité.", r"Un système $\sum m_i\mu_i^k=0$ à $\mu_i$ distincts non nuls : Vandermonde.", r"Une relation de commutation $AB-BA=A$ se propage aux puissances par récurrence."])
B['n-mp-glconnexe'] = ([r"**Image continue d'un connexe par arcs** ; les connexes par arcs de $\mathbb R$ sont les intervalles.", r"**Un polynôme non nul** n'a qu'un nombre fini de racines."],
  [r"Le déterminant sépare $GL_n(\mathbb R)$ selon son signe.", r"Dans $\mathbb C$, contourner un nombre fini de points avec une famille d'arcs deux à deux disjoints.", r"Une fonction continue à valeurs entières sur un connexe par arcs est constante."])
B['n-mp-sgR'] = ([r"**Borne inférieure** : caractérisation par $\varepsilon$.", r"**Densité** et image d'une partie dense par une application continue."],
  [r"Si la borne n'est pas atteinte, deux éléments proches donnent une différence trop petite.", r"Montrer qu'un sous-groupe n'est pas monogène par l'irrationalité.", r"$\cos$ est $2\pi$-périodique et paire : passer de $\mathbb Z+2\pi\mathbb Z$ à $\mathbb N$."])
