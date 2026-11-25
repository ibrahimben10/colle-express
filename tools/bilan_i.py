# Bilans — exercices d'informatique (i-*)
B = {}
INV = r"**Invariant de boucle.** Propriété vraie avant la boucle et conservée par chaque itération ; avec la condition d'arrêt, elle prouve la correction."
VAR = r"**Variant de boucle.** Quantité entière positive qui décroît strictement à chaque itération : elle prouve la terminaison."
PILE = r"**Pile.** Dernier entré, premier sorti ; en Python, `append` et `pop` sur une liste, en $O(1)$."
FILE = r"**File.** Premier entré, premier sorti ; `collections.deque` avec `append` et `popleft` en $O(1)$."
DPR = r"**Diviser pour régner.** $C(n)=2C(n/2)+O(n)$ donne $C(n)=O(n\log n)$."
PD = r"**Programmation dynamique.** Sous-structure optimale et sous-problèmes communs : chaque sous-problème est calculé une seule fois, dans un ordre compatible avec les dépendances."
BFS = r"**Parcours en largeur.** Avec une file, les sommets sont visités par distance croissante à la source ; coût $O(n+p)$ avec des listes d'adjacence."
DFS = r"**Parcours en profondeur.** Depuis un sommet, il visite toute sa composante connexe ; coût total $O(n+p)$."

B['i-py-max2'] = ([INV, r"**Complexité d'un tri par comparaison.** $\Omega(n\log n)$ comparaisons dans le pire cas."],
  [r"Une seule passe suffit pour les deux plus grands : mettre à jour un couple `(a, b)`.", r"Penser aux doublons : `[5, 5, 1]` doit donner `(5, 5)`.", r"Ne pas trier quand on ne cherche que quelques valeurs extrêmes."])
B['i-py-csv'] = ([r"**Fichiers.** `with open(nom) as f` garantit la fermeture ; `strip()` retire le `\n` de fin de ligne.", r"**Dictionnaires.** Accès et insertion en $O(1)$ en moyenne ; `d.get(k, 0)` évite de tester la présence de la clé."],
  [r"Sauter l'en-tête avec `f.readline()` avant la boucle.", r"Ignorer les lignes vides, en particulier la dernière.", r"Regrouper par clé : cumuler somme et effectif, puis diviser."])
B['i-cx-dicho'] = ([VAR, INV, r"**Dichotomie.** Sur une liste triée de longueur $n$, au plus $\lfloor\log_2n\rfloor+1$ itérations."],
  [r"Variant classique : la longueur $d-g+1$ de l'intervalle de recherche.", r"L'invariant décrit où l'élément peut encore se trouver.", r"La division par deux de l'intervalle donne un coût logarithmique."])
B['i-cx-expo'] = ([INV, r"**Écriture binaire.** $n\ge1$ a $\lfloor\log_2n\rfloor+1$ chiffres en base 2."],
  [r"Prouver un invariant en distinguant $k$ pair et $k$ impair.", r"Le nombre de passages est le nombre de bits de $n$ ; les multiplications supplémentaires correspondent aux bits à 1.", r"Exponentiation rapide : $O(\log n)$ multiplications au lieu de $n$."])
B['i-cx-motif'] = ([r"**Complexité dans le pire cas.** Maximum du nombre d'opérations sur les entrées d'une taille donnée."],
  [r"Deux boucles imbriquées : multiplier le nombre de tours externes par le maximum du nombre de tours internes.", r"Pour montrer qu'une borne est atteinte, exhiber une entrée explicite.", r"Les textes très répétitifs (`aaaa…`) sont les pires cas de la recherche naïve."])
B['i-pile-par'] = ([PILE],
  [r"Trois échecs possibles : fermante sur pile vide, mauvais type, pile non vide à la fin.", r"Un seul type de parenthèses : un compteur suffit ; plusieurs types : il faut une pile.", r"Associer fermantes et ouvrantes avec un dictionnaire."])
B['i-pile-rpn'] = ([PILE],
  [r"Le premier élément dépilé est l'opérande de droite : attention à `-` et `/`.", r"Bilan de hauteur : +1 par nombre, −1 par opérateur, il reste 1 à la fin.", r"La notation postfixée se passe de parenthèses et de priorités."])
B['i-rec-fibo'] = ([r"**Suite de Fibonacci.** $F_n\sim\frac{\varphi^n}{\sqrt5}$ avec $\varphi=\frac{1+\sqrt5}2$.", r"**Mémoïsation.** Stocker les résultats déjà calculés (dictionnaire) pour ne jamais recalculer un même appel."],
  [r"Compter les appels : $A(n)=1+A(n-1)+A(n-2)$, puis $A+1$ vérifie la récurrence de Fibonacci.", r"Deux appels récursifs qui se recouvrent donnent un coût exponentiel.", r"Itératif ou mémoïsé : $O(n)$."])
B['i-rec-hanoi'] = ([r"**Récurrence $u_n=2u_{n-1}+1$.** $u_n+1=2(u_{n-1}+1)$, donc $u_n=2^n-1$ si $u_0=0$."],
  [r"Écrire la récursion à partir du plus grand disque.", r"Le même argument que la construction prouve l'optimalité.", r"Le coût d'un algorithme récursif se lit sur une relation de récurrence."])
B['i-tri-ins'] = ([INV, r"**Tri stable.** Conserve l'ordre relatif des éléments égaux.", r"**Somme des entiers.** $\sum_{i=1}^{n-1}i=\frac{n(n-1)}2$."],
  [r"Invariant du tri par insertion : le préfixe `L[0:i]` est trié.", r"Meilleur cas linéaire (liste triée), pire cas quadratique (liste décroissante).", r"Le test strict `>` rend le tri stable."])
B['i-tri-fus'] = ([DPR],
  [r"Fusion à deux indices : linéaire en la somme des longueurs.", r"Pour $n=2^k$, poser $c_k=C(2^k)/2^k$.", r"Le tri fusion n'est pas en place : $O(n)$ de mémoire supplémentaire."])
B['i-tri-cpt'] = ([r"**Tris par comparaison.** $\Omega(n\log n)$ comparaisons dans le pire cas ; le tri par comptage n'en fait aucune."],
  [r"Valeurs entières dans un petit intervalle : compter au lieu de comparer.", r"Coût $O(n+m)$ : à éviter quand $m\gg n$.", r"Reconstruire en parcourant les valeurs dans l'ordre croissant."])
B['i-tri-sel'] = ([r"**Tri rapide.** Coût moyen $O(n\log n)$, pire cas $O(n^2)$ (pivot toujours extrême).", r"**Série géométrique.** $n+\frac n2+\frac n4+\dots\le2n$."],
  [r"Le pivot `L[0]` est le pire choix sur une liste déjà triée.", r"Pour une sélection, ne récurser que dans la partie qui contient l'élément cherché.", r"Partition en trois (petits, égaux, grands) : gère les doublons sans boucle infinie."])
B['i-gr-bfs'] = ([BFS, FILE],
  [r"Marquer un sommet au moment où on l'enfile, pas quand on le défile.", r"`D[v] = -1` sert de marque « non vu ».", r"`pop(0)` sur une liste coûte $O(n)$ : utiliser `deque`."])
B['i-gr-cycle'] = ([DFS, r"**Forêts.** Un graphe à $n$ sommets et $c$ composantes est sans cycle si et seulement s'il a $n-c$ arêtes."],
  [r"Un parcours lancé depuis chaque sommet non vu découvre une composante.", r"Dans un graphe non orienté, ignorer le parent lors de la détection de cycle.", r"$p=\frac12\sum_s\deg(s)$."])
B['i-gr-dijk'] = ([r"**Algorithme de Dijkstra.** Avec des poids positifs, le sommet non fixé de distance minimale a sa distance définitive.", r"**Tas (`heapq`).** Insertion et extraction du minimum en $O(\log m)$."],
  [r"Ignorer les entrées périmées du tas (`du > d[u]`).", r"Complexité $O((n+p)\log n)$ avec un tas.", r"Un seul arc négatif peut rendre Dijkstra faux."])
B['i-gr-bip'] = ([BFS, r"**Graphe biparti.** Biparti si et seulement s'il n'a aucun cycle de longueur impaire."],
  [r"Colorier par la parité de la distance à la source.", r"Ne pas oublier les autres composantes connexes.", r"Un conflit entre deux sommets de même distance fabrique un cycle impair."])
B['i-pd-monnaie'] = ([PD],
  [r"Un algorithme glouton n'est pas toujours optimal : chercher un petit contre-exemple.", r"$m(x)=1+\min_{p\le x}m(x-p)$.", r"Garder la pièce choisie pour reconstruire la solution."])
B['i-pd-plsc'] = ([PD],
  [r"Récurrence sur les dernières lettres des deux préfixes.", r"Créer un tableau 2D avec une compréhension, jamais avec `[[0] * m] * n`.", r"Reconstruire en remontant depuis la case $(n,m)$."])
B['i-pd-grille'] = ([PD, r"**Chemins dans une grille.** $\binom{a+b}{a}$ mots formés de $a$ pas N et $b$ pas E."],
  [r"Écrire la récurrence sur la case précédente (Sud ou Ouest).", r"Choisir l'ordre de remplissage pour que les dépendances soient déjà calculées.", r"Traiter à part la première ligne et la première colonne."])
B['i-pd-sac'] = ([PD],
  [r"Récurrence « objet pris ou non ».", r"Avec une seule liste, parcourir les capacités décroissantes.", r"Partition équilibrée = sac à dos de capacité $\lfloor S/2\rfloor$ avec poids = valeur."])
B['i-ia-knn'] = ([r"**k plus proches voisins.** Classe majoritaire parmi les $k$ points étiquetés les plus proches.", r"**Distance euclidienne.** $d(a,b)=\sqrt{\sum_i(a_i-b_i)^2}$."],
  [r"Trier les couples `(distance, classe)` puis voter parmi les $k$ premiers.", r"Avec deux classes, choisir $k$ impair pour éviter les égalités.", r"Coût d'une prédiction : $O(n\log n)$ avec un tri."])
B['i-ia-kmeans'] = ([r"**k-moyennes.** Alternance affectation au centre le plus proche et recalcul des barycentres.", r"**König-Huygens.** $\sum_j\|y_j-c\|^2=\sum_j\|y_j-\bar y\|^2+m\|\bar y-c\|^2$."],
  [r"Chaque étape fait décroître l'inertie.", r"Un nombre fini de partitions garantit l'arrêt, dans un minimum local.", r"Gérer le cas d'un groupe vide."])
B['i-jeu-nim'] = ([r"**Positions gagnantes et perdantes.** Gagnante s'il existe un coup vers une position perdante ; perdante si tous les coups mènent à une position gagnante."],
  [r"Calculer à rebours depuis la position finale.", r"Conjecturer sur les petites valeurs, puis démontrer par récurrence forte.", r"Stratégie gagnante : toujours jouer vers une position perdante."])
B['i-jeu-minmax'] = ([r"**Min-max.** Max prend le maximum des valeurs des fils, Min le minimum ; une feuille vaut son score."],
  [r"Alterner le rôle du joueur à chaque niveau de la récursion.", r"Taille de l'arbre exploré : $\frac{b^{h+1}-1}{b-1}$.", r"Profondeur limitée + heuristique pour les vrais jeux."])
B['i-flot'] = ([r"**Flottants.** Mantisse de 53 bits : erreur relative d'arrondi au plus $2^{-53}\approx1{,}1\times10^{-16}$ ; seuls les nombres dyadiques sont exacts."],
  [r"Ne jamais tester l'égalité de deux flottants avec `==` : utiliser une tolérance (`math.isclose`).", r"Sommer les petits termes d'abord.", r"`math.fsum` somme sans perte."])
