# Informatique commune MP — 4e série (10 exercices originaux) : graphes, programmation dynamique,
# apprentissage, théorie des jeux et bases de données (SQL), sur le cours de D. Rupprecht
# (lycée Pierre-de-Fermat). Code Python et requêtes SQL testés par tools/test_info.py.
from newlib import ex, E

def src(chapitre, texte=None):
    E[-1]['enonce'] += '\n\n*' + (texte or f"Exercice original sur le chapitre « {chapitre} » du cours d'informatique MP de D. Rupprecht (lycée Pierre-de-Fermat).") + '*'
    E[-1]['ajout'] = '2026-11-25'

M = 'Informatique'

# ------------------------------------------------------------------ 11. Tri topologique
ex('i-gr-topo', M, 'Graphes', 2, 'Ordonner des chapitres : le tri topologique', 25, r"""
Un graphe orienté est représenté par un dictionnaire d'adjacence : `G[s]` est la liste des successeurs de `s`. Un arc $s\to t$ signifie « le chapitre $s$ doit être étudié avant le chapitre $t$ ». Par exemple :

```python
G = {'algebre': ['analyse', 'proba'], 'analyse': ['proba', 'edo'],
     'proba': [], 'edo': []}
```

Un **ordre topologique** est une liste de tous les sommets où, pour chaque arc $s\to t$, $s$ apparaît avant $t$.

1. Écrire une fonction `degres_entrants(G)` qui renvoie le dictionnaire des degrés entrants.
2. On applique l'algorithme suivant : placer dans une file les sommets de degré entrant nul ; tant que la file n'est pas vide, en retirer un sommet $s$, l'ajouter au résultat, et diminuer de 1 le degré entrant de chacun de ses successeurs, en enfilant ceux qui tombent à 0. Écrire `tri_topologique(G)`, qui renvoie l'ordre obtenu, ou `None` si certains sommets n'ont jamais été placés.
3. Donner le résultat sur l'exemple.
4. Montrer que si le graphe a un cycle, la fonction renvoie `None`, et que sinon elle renvoie un ordre topologique.
5. Quelle est la complexité, en fonction du nombre $n$ de sommets et $p$ d'arcs ?
""", r"""Parcours toutes les listes de successeurs et incrémente le degré de chaque successeur.""",
r"""Utilise `collections.deque` ; un sommet est ajouté au résultat seulement quand tous ses prédécesseurs y sont déjà.""",
r"""Sur un cycle, aucun sommet ne peut être le premier à atteindre un degré entrant nul.""",
r"""**Étape 1 — Analyse de l'énoncé.** On veut un ordre compatible avec toutes les contraintes « avant ». L'idée : commencer par les sommets qui n'ont aucun prérequis, puis retirer leurs arcs.

**Étape 2 — Rappels du cours.**

> **Définition — Degré entrant.** Nombre d'arcs qui arrivent sur un sommet ; la somme des degrés entrants vaut le nombre $p$ d'arcs.

> **Propriété — File.** `deque` réalise `append` et `popleft` en $O(1)$.

**Étape 3 — Stratégie.** Invariant : un sommet est enfilé au moment où tous ses prédécesseurs ont été placés dans le résultat.

**Étape 4 — Résolution détaillée.**

**4.1 Degrés entrants.**

```python
from collections import deque

def degres_entrants(G):
    deg = {s: 0 for s in G}
    for s in G:
        for t in G[s]:
            deg[t] += 1
    return deg
```

**4.2 Tri topologique.**

```python
def tri_topologique(G):
    deg = degres_entrants(G)
    F = deque(s for s in G if deg[s] == 0)
    ordre = []
    while F:
        s = F.popleft()
        ordre.append(s)
        for t in G[s]:
            deg[t] -= 1
            if deg[t] == 0:
                F.append(t)
    return ordre if len(ordre) == len(G) else None
```

**4.3 Exemple.** Degrés entrants : algebre 0, analyse 1, proba 2, edo 1. On place `algebre` ; `analyse` tombe à 0 et `proba` à 1. On place `analyse` ; `proba` et `edo` tombent à 0. Résultat :
`['algebre', 'analyse', 'proba', 'edo']`.

**4.4 Correction.** À tout instant, `deg[t]` est le nombre de prédécesseurs de $t$ pas encore placés. Un sommet est donc enfilé, puis placé, seulement après tous ses prédécesseurs : si tous les sommets sont placés, la liste est un ordre topologique.
- **Avec un cycle** $s_1\to s_2\to\dots\to s_k\to s_1$ : supposons qu'un sommet du cycle soit placé, et prenons le premier placé, $s_i$. Son prédécesseur sur le cycle n'est pas encore placé, donc `deg[s_i]` n'est pas nul : contradiction. Aucun sommet du cycle n'est placé, et la fonction renvoie `None`.
- **Sans cycle** : si la file se vide alors qu'il reste des sommets non placés, chacun a un prédécesseur non placé. En remontant de prédécesseur en prédécesseur parmi un nombre fini de sommets, on revient sur un sommet déjà rencontré : il y a un cycle, contradiction. Tous les sommets sont donc placés.

**4.5 Complexité.** Le calcul des degrés parcourt toutes les listes : $O(n+p)$. Chaque sommet est enfilé et défilé au plus une fois, et chaque arc fait diminuer un degré une seule fois : $O(n+p)$ au total.

**Étape 5 — Vérification.**

> **Vérification — Cycle.** Avec `{'a': ['b'], 'b': ['c'], 'c': ['a'], 'd': ['a']}`, seul `d` est placé : la fonction renvoie `None`.

**Étape 6 — Conclusion.**
$$\boxed{\text{ordre topologique en }O(n+p)\text{, ou }\texttt{None}\text{ si et seulement s'il y a un cycle}}$$""",
r"""Ordre `['algebre', 'analyse', 'proba', 'edo']` ; aucun sommet d'un cycle n'atteint le degré 0 ; $O(n+p)$.""")
src('Graphes')

# ------------------------------------------------------------------ 12. Graphe inverse et coloration
ex('i-gr-inverse', M, 'Graphes', 1, 'Graphe inverse et coloration valide', 20, r"""
Un graphe orienté de sommets $0,\dots,N-1$ est représenté par un dictionnaire d'adjacence, par exemple

```python
d = {0: [1, 2], 1: [3], 2: [3, 4], 3: [0], 4: [], 5: [4]}
```

1. Écrire une fonction `degre_max(d)` qui renvoie le plus grand degré sortant.
2. Le **graphe inverse** a les mêmes sommets et les arcs retournés. Écrire `graphe_inverse(d)` et donner le résultat sur l'exemple (les successeurs étant ajoutés dans l'ordre croissant des sommets de départ).
3. Une **coloration** est une liste `L` où `L[s]` est la couleur (un entier) du sommet `s`. Elle est **valide** si les deux extrémités de chaque arc ont des couleurs différentes. Écrire `coloration_valide(d, L)`. Les colorations `[0, 1, 1, 2, 0, 1]` et `[0, 1, 0, 2, 0, 1]` sont-elles valides ?
4. Donner la complexité des trois fonctions en fonction de $N$ et du nombre $M$ d'arcs.
""", r"""Le degré sortant de `s` est `len(d[s])`.""",
r"""Crée d'abord une liste vide pour chaque sommet, puis, pour chaque arc $s\to t$, ajoute `s` à la liste de `t`.""",
r"""Une coloration est invalide dès qu'un arc relie deux sommets de même couleur : on peut renvoyer `False` immédiatement.""",
r"""**Étape 1 — Analyse de l'énoncé.** Trois parcours classiques d'un dictionnaire d'adjacence : par sommet, puis par arc.

**Étape 2 — Rappels du cours.**

> **Définition — Liste d'adjacence.** Pour chaque sommet, la liste de ses successeurs ; la somme des longueurs des listes est le nombre $M$ d'arcs.

> **Propriété — Parcours.** Visiter tous les arcs d'un dictionnaire d'adjacence coûte $O(N+M)$.

**Étape 3 — Stratégie.** Écrire chaque fonction comme un parcours des sommets, avec une boucle interne sur les successeurs quand on a besoin des arcs.

**Étape 4 — Résolution détaillée.**

**4.1 Degré maximal.**

```python
def degre_max(d):
    m = 0
    for s in d:
        m = max(m, len(d[s]))
    return m
```

Sur l'exemple, les degrés sortants sont $2,1,2,1,0,1$ : le résultat est $2$.

**4.2 Graphe inverse.**

```python
def graphe_inverse(d):
    inv = {s: [] for s in d}
    for s in d:
        for t in d[s]:
            inv[t].append(s)
    return inv
```

Sur l'exemple : `{0: [3], 1: [0], 2: [0], 3: [1, 2], 4: [2, 5], 5: []}`.

**4.3 Coloration valide.**

```python
def coloration_valide(d, L):
    for s in d:
        for t in d[s]:
            if L[s] == L[t]:
                return False
    return True
```

Pour `[0, 1, 1, 2, 0, 1]`, les arcs $0\to1$, $0\to2$, $1\to3$, $2\to3$, $2\to4$, $3\to0$, $5\to4$ relient les couleurs $(0,1)$, $(0,1)$, $(1,2)$, $(1,2)$, $(1,0)$, $(2,0)$, $(1,0)$ : valide. Pour `[0, 1, 0, 2, 0, 1]`, l'arc $0\to2$ relie deux sommets de couleur 0 : non valide.

**4.4 Complexité.** `degre_max` fait un tour par sommet, avec `len` en $O(1)$ : $O(N)$. `graphe_inverse` crée $N$ listes puis traite chaque arc en $O(1)$ : $O(N+M)$. `coloration_valide` examine au pire tous les arcs : $O(N+M)$.

**Étape 5 — Vérification.**

> **Vérification — Double inversion.** Inverser deux fois le graphe redonne le même ensemble d'arcs, et la coloration valide l'est encore pour le graphe inverse (la condition ne dépend pas du sens des arcs).

**Étape 6 — Conclusion.**
$$\boxed{\text{degré max }2\ ;\ \text{inverse et validité en }O(N+M)}$$""",
r"""Degré maximal $2$ ; inverse `{0: [3], 1: [0], 2: [0], 3: [1, 2], 4: [2, 5], 5: []}` ; première coloration valide, seconde non ; $O(N)$ et $O(N+M)$.""")
src('Graphes', "Exercice original dans l'esprit des questions de graphes des sujets CCINP MP rassemblés dans le cours d'informatique MP de D. Rupprecht (lycée Pierre-de-Fermat).")

# ------------------------------------------------------------------ 13. Plus court chemin dans un labyrinthe
ex('i-gr-chemin', M, 'Graphes', 2, 'Plus court chemin dans un labyrinthe', 25, r"""
Un labyrinthe est une liste de chaînes de même longueur : `'#'` est un mur, `'.'` une case libre. On se déplace d'une case libre à une case libre voisine (haut, bas, gauche, droite).

```python
lab = ["..#.",
       ".##.",
       "....",
       "#.#."]
```

1. Écrire une fonction `voisins(lab, c)` qui renvoie la liste des cases libres voisines de la case `c = (i, j)`.
2. Écrire une fonction `chemin(lab, dep, arr)` qui renvoie la liste des cases d'un plus court chemin de `dep` à `arr` (extrémités comprises), ou `None` s'il n'en existe pas. On utilisera un parcours en largeur et un dictionnaire des prédécesseurs.
3. Donner le résultat pour `dep = (0, 0)` et `arr = (0, 3)`.
4. Pourquoi le chemin obtenu est-il de longueur minimale ? Quelle est la complexité pour un labyrinthe de $n$ lignes et $p$ colonnes ?
""", r"""Teste que l'indice reste dans la grille avant de lire le caractère.""",
r"""Le dictionnaire `pred` sert à la fois de marque « déjà vu » et de mémoire pour reconstruire le chemin.""",
r"""Remonte de `arr` à `dep` en suivant `pred`, puis renverse la liste.""",
r"""**Étape 1 — Analyse de l'énoncé.** La grille est un graphe implicite : les sommets sont les cases libres, les arêtes relient deux cases libres voisines. Toutes les arêtes ont le même poids : un parcours en largeur donne les plus courts chemins.

**Étape 2 — Rappels du cours.**

> **Propriété — Parcours en largeur.** Avec une file, les sommets sont découverts par distance croissante à la source ; coût $O(n+p)$ en sommets et arêtes.

> **Méthode — Prédécesseurs.** Mémoriser, pour chaque sommet découvert, le sommet depuis lequel on l'a découvert permet de reconstruire le chemin.

**Étape 3 — Stratégie.** Parcours en largeur depuis `dep`, arrêt possible dès que `arr` est découvert, puis remontée des prédécesseurs.

**Étape 4 — Résolution détaillée.**

**4.1 Voisins.**

```python
from collections import deque

def voisins(lab, c):
    i, j = c
    n, p = len(lab), len(lab[0])
    res = []
    for a, b in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if 0 <= a < n and 0 <= b < p and lab[a][b] == '.':
            res.append((a, b))
    return res
```

**4.2 Parcours et reconstruction.**

```python
def chemin(lab, dep, arr):
    pred = {dep: None}
    F = deque([dep])
    while F:
        c = F.popleft()
        if c == arr:
            break
        for v in voisins(lab, c):
            if v not in pred:
                pred[v] = c
                F.append(v)
    if arr not in pred:
        return None
    res = []
    c = arr
    while c is not None:
        res.append(c)
        c = pred[c]
    res.reverse()
    return res
```

**4.3 Exemple.** La case $(0,1)$ est une impasse (ses voisines $(0,2)$ et $(1,1)$ sont des murs). Le chemin passe par la colonne de gauche, la ligne 2, puis remonte la colonne de droite :
`[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (1, 3), (0, 3)]`, soit 7 déplacements.

**4.4 Minimalité et coût.** Le parcours en largeur découvre les cases par distance croissante à `dep`, et `pred[v]` est une case de distance $d(v)-1$ : la remontée suit un chemin de longueur $d(\texttt{arr})$, minimale. Chaque case est enfilée au plus une fois (grâce au test `v not in pred`) et a au plus 4 voisines : $O(np)$ en temps et en mémoire.

**Étape 5 — Vérification.**

> **Vérification — Cas sans issue.** Si l'on remplace `lab[2]` par `"#..."`, la case $(0,3)$ n'est plus reliée à $(0,0)$ et la fonction renvoie `None`.

**Étape 6 — Conclusion.**
$$\boxed{\text{BFS + prédécesseurs : 7 déplacements, en }O(np)}$$""",
r"""Parcours en largeur avec dictionnaire `pred` ; chemin de 8 cases (7 déplacements) ; minimal par la propriété du BFS ; $O(np)$.""")
src('Graphes')

# ------------------------------------------------------------------ 14. Distance d'édition
ex('i-pd-levensh', M, 'Programmation dynamique', 3, 'Distance d\'édition entre deux mots', 30, r"""
La **distance d'édition** $d(a,b)$ entre deux mots est le nombre minimal d'opérations pour transformer $a$ en $b$, chaque opération étant l'insertion, la suppression ou le remplacement d'une lettre.

1. Que valent $d(\texttt{kayak},\texttt{yak})$ et $d(\varepsilon,\texttt{abc})$, où $\varepsilon$ est le mot vide ?
2. On note $D(i,j)$ la distance entre les préfixes `a[:i]` et `b[:j]`. Justifier
$$D(i,j)=\min\big(D(i-1,j)+1,\ D(i,j-1)+1,\ D(i-1,j-1)+\delta_{ij}\big),$$
où $\delta_{ij}=0$ si `a[i-1] == b[j-1]` et $1$ sinon, et donner $D(i,0)$ et $D(0,j)$.
3. Écrire une fonction `distance(a, b)` en $O(nm)$, avec $n$ et $m$ les longueurs des mots, et calculer $d(\texttt{chien},\texttt{niche})$.
4. Réécrire la fonction en ne gardant que deux lignes du tableau. Quelle mémoire utilise-t-elle ?
""", r"""Regarde la **dernière** opération d'une transformation optimale de `a[:i]` en `b[:j]` : elle concerne la dernière lettre de l'un des préfixes.""",
r"""Remplis le tableau ligne par ligne : la case $(i,j)$ dépend des cases $(i-1,j)$, $(i,j-1)$ et $(i-1,j-1)$.""",
r"""La ligne $i$ ne dépend que de la ligne $i-1$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Une suite d'opérations se lit comme un alignement des deux mots. On cherche une récurrence sur les préfixes, puis on la calcule de bas en haut.

**Étape 2 — Rappels du cours.**

> **Méthode — Programmation dynamique.** Sous-structure optimale et sous-problèmes communs : on calcule chaque sous-problème une fois, dans un ordre compatible avec les dépendances.

> **Piège — Tableaux.** Créer un tableau 2D avec une compréhension, jamais avec `[[0] * m] * n`.

**Étape 3 — Stratégie.** Récurrence sur la dernière opération, tableau $(n+1)\times(m+1)$, puis réduction de la mémoire.

**Étape 4 — Résolution détaillée.**

**4.1 Exemples.** `kayak` → `yak` : on supprime les deux premières lettres `k` et `a`, et on ne peut pas faire mieux car il faut au moins perdre $5-3=2$ lettres : $d=2$. Du mot vide à `abc`, trois insertions : $d=3$.

**4.2 Récurrence.** $D(i,0)=i$ ($i$ suppressions) et $D(0,j)=j$ ($j$ insertions). Pour $i,j\ge1$, considérons une transformation optimale de `a[:i]` en `b[:j]`, écrite comme un alignement. La dernière colonne est :
- la suppression de `a[i-1]` : coût $D(i-1,j)+1$ ;
- l'insertion de `b[j-1]` : coût $D(i,j-1)+1$ ;
- l'alignement de `a[i-1]` avec `b[j-1]`, gratuit si les lettres sont égales, sinon un remplacement : coût $D(i-1,j-1)+\delta_{ij}$.

Le reste de l'alignement est une transformation des préfixes restants, qu'on peut supposer optimale. Le minimum des trois cas donne $D(i,j)$.

**4.3 Programme.**

```python
def distance(a, b):
    n, m = len(a), len(b)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            delta = 0 if a[i - 1] == b[j - 1] else 1
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + delta)
    return D[n][m]
```

$(n+1)(m+1)$ cases calculées en $O(1)$ : $O(nm)$ en temps et en mémoire. Le tableau pour `chien` (lignes) et `niche` (colonnes) a pour dernière ligne $5,4,4,4,4,4$ : $d(\texttt{chien},\texttt{niche})=4$.

**4.4 Deux lignes.**

```python
def distance_lignes(a, b):
    m = len(b)
    prec = list(range(m + 1))
    for i in range(1, len(a) + 1):
        cour = [i] + [0] * m
        for j in range(1, m + 1):
            delta = 0 if a[i - 1] == b[j - 1] else 1
            cour[j] = min(prec[j] + 1, cour[j - 1] + 1, prec[j - 1] + delta)
        prec = cour
    return prec[m]
```

Mémoire $O(m)$ (ou $O(\min(n,m))$ en échangeant les mots), même temps $O(nm)$. On perd en revanche la possibilité de reconstruire la suite d'opérations, qui demande le tableau entier.

**Étape 5 — Vérification.**

> **Vérification — Propriétés.** $d(a,a)=0$, $d(a,b)=d(b,a)$, $|n-m|\le d(a,b)\le\max(n,m)$ ; les deux versions coïncident sur des mots aléatoires, et $d(\texttt{colle},\texttt{collet})=1$.

**Étape 6 — Conclusion.**
$$\boxed{D(i,j)=\min(D(i-1,j)+1,D(i,j-1)+1,D(i-1,j-1)+\delta_{ij}),\ d(\texttt{chien},\texttt{niche})=4}$$""",
r"""$d(\texttt{kayak},\texttt{yak})=2$, $d(\varepsilon,\texttt{abc})=3$ ; récurrence sur la dernière opération ; $O(nm)$ ; $d(\texttt{chien},\texttt{niche})=4$ ; deux lignes : mémoire $O(m)$.""")
src('Programmation dynamique')

# ------------------------------------------------------------------ 15. Escalier
ex('i-pd-escalier', M, 'Programmation dynamique', 1, 'Monter un escalier : récursion, mémoïsation, boucle', 15, r"""
On monte un escalier de $n$ marches en faisant des pas de 1 ou 2 marches. On note $W(n)$ le nombre de façons de le monter ; $W(0)=1$ (ne rien faire).

1. Montrer que $W(n)=W(n-1)+W(n-2)$ pour $n\ge2$, et calculer $W(1)$, $W(2)$, $W(3)$.
2. Écrire une fonction récursive directe. Pourquoi est-elle très lente pour $n=40$ ?
3. Écrire une version mémoïsée avec un dictionnaire, puis une version itérative en $O(n)$ sans dictionnaire.
4. Généraliser : écrire `nb_facons(n, pas)` où `pas` est la liste des tailles de pas autorisées. Calculer $W(10)$ pour les pas $\{1,2\}$ et pour les pas $\{1,2,3\}$.
""", r"""Classe les façons de monter selon la taille du **dernier** pas.""",
r"""La récursion directe recalcule les mêmes valeurs un nombre exponentiel de fois, comme pour Fibonacci.""",
r"""Pour la généralisation, $W(k)=\sum_{p\in\text{pas},\,p\le k}W(k-p)$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Un problème de dénombrement dont la récurrence est celle de Fibonacci : l'occasion de comparer trois façons de la calculer.

**Étape 2 — Rappels du cours.**

> **Définition — Mémoïsation.** On stocke dans un dictionnaire les valeurs déjà calculées d'une fonction récursive pour ne jamais les recalculer.

> **Propriété — Fibonacci.** La récursion naïve $F(n)=F(n-1)+F(n-2)$ fait un nombre d'appels exponentiel en $n$.

**Étape 3 — Stratégie.** Récurrence sur le dernier pas, puis trois implémentations.

**Étape 4 — Résolution détaillée.**

**4.1 Récurrence.** Pour $n\ge2$, une montée se termine soit par un pas de 1 (précédé d'une montée de $n-1$ marches), soit par un pas de 2 (précédé d'une montée de $n-2$ marches). Ces deux cas sont disjoints : $W(n)=W(n-1)+W(n-2)$. On a $W(1)=1$, donc $W(2)=2$ (1+1 ou 2) et $W(3)=3$ (1+1+1, 1+2, 2+1). En fait $W(n)=F_{n+1}$.

**4.2 Récursion directe.**

```python
def W_rec(n):
    if n <= 1:
        return 1
    return W_rec(n - 1) + W_rec(n - 2)
```

Le nombre d'appels vérifie la même récurrence que $W$, à une constante près : il croît comme $\varphi^n$ avec $\varphi\approx1{,}618$. Pour $n=40$, il y a plus de $3\times10^8$ appels.

**4.3 Mémoïsation et boucle.**

```python
memo = {0: 1, 1: 1}

def W_memo(n):
    if n not in memo:
        memo[n] = W_memo(n - 1) + W_memo(n - 2)
    return memo[n]

def W_iter(n):
    a, b = 1, 1          # W(0), W(1)
    for _ in range(n - 1):
        a, b = b, a + b
    return b if n >= 1 else 1
```

Chaque valeur est calculée une seule fois : $O(n)$ opérations. La version itérative n'utilise que deux variables.

**4.4 Généralisation.**

```python
def nb_facons(n, pas):
    W = [0] * (n + 1)
    W[0] = 1
    for k in range(1, n + 1):
        for p in pas:
            if p <= k:
                W[k] += W[k - p]
    return W[n]
```

Pour $\{1,2\}$ : $1,1,2,3,5,8,13,21,34,55,89$, donc $W(10)=89$. Pour $\{1,2,3\}$ : $1,1,2,4,7,13,24,44,81,149,274$, donc $W(10)=274$.

**Étape 5 — Vérification.**

> **Vérification — Concordance.** Les quatre fonctions donnent les mêmes valeurs pour $n\le25$ ; à la main, pour $n=4$ et les pas $\{1,2\}$ : 1111, 112, 121, 211, 22, soit $5=W(4)$.

**Étape 6 — Conclusion.**
$$\boxed{W(n)=W(n-1)+W(n-2)=F_{n+1}\ ;\ W(10)=89,\ \text{et }274\text{ avec les pas }\{1,2,3\}}$$""",
r"""Récurrence sur le dernier pas, $W(n)=F_{n+1}$ ; récursion exponentielle, mémoïsation ou boucle en $O(n)$ ; $W(10)=89$ et $274$.""")
src('Programmation dynamique')

# ------------------------------------------------------------------ 16. Plus longue sous-suite croissante
ex('i-pd-pls', M, 'Programmation dynamique', 2, 'Plus longue sous-suite strictement croissante', 25, r"""
Une **sous-suite** de `L` s'obtient en supprimant des termes sans changer l'ordre des autres. On cherche une sous-suite strictement croissante de longueur maximale.

1. Pourquoi l'essai de toutes les sous-suites est-il inenvisageable pour $n=60$ ?
2. On note $\ell_j$ la longueur maximale d'une sous-suite strictement croissante **qui se termine** par `L[j]`. Exprimer $\ell_j$ à l'aide des $\ell_i$, $i<j$.
3. Écrire une fonction `pssc(L)` en $O(n^2)$ qui renvoie une plus longue sous-suite strictement croissante (et pas seulement sa longueur). On mémorisera pour chaque $j$ l'indice du terme précédent.
4. Que renvoie-t-elle pour `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]`, si l'on garde, en cas d'égalité, le premier indice trouvé ?
""", r"""Il y a $2^n$ sous-suites.""",
r"""Une sous-suite finissant par `L[j]` est `[L[j]]` seule, ou une sous-suite finissant par un `L[i]` avec $i<j$ et `L[i] < L[j]`, prolongée par `L[j]`.""",
r"""La réponse se termine à l'indice $k$ qui maximise $\ell_k$ ; remonte ensuite les prédécesseurs.""",
r"""**Étape 1 — Analyse de l'énoncé.** Le problème rappelle la tranche de somme maximale, mais les termes ne sont plus consécutifs : la valeur en $j$ dépend de **tous** les indices précédents.

**Étape 2 — Rappels du cours.**

> **Méthode — Programmation dynamique.** Définir le bon sous-problème (ici : « qui se termine en $j$ »), écrire la récurrence, remplir dans l'ordre, puis reconstruire la solution avec les choix mémorisés.

**Étape 3 — Stratégie.** Deux tableaux : `lg` (longueurs) et `pred` (indice précédent), puis remontée depuis le meilleur indice.

**Étape 4 — Résolution détaillée.**

**4.1 Force brute.** Chaque terme est gardé ou non : $2^n$ sous-suites. Pour $n=60$, $2^{60}\approx10^{18}$ : inenvisageable.

**4.2 Récurrence.**
$$\ell_j=1+\max\big(\{0\}\cup\{\ell_i\mid i<j,\ L_i<L_j\}\big).$$
En effet, en retirant `L[j]` d'une sous-suite croissante qui se termine par `L[j]`, on obtient soit la suite vide, soit une sous-suite croissante qui se termine par un `L[i] < L[j]`, $i<j$.

**4.3 Programme.**

```python
def pssc(L):
    n = len(L)
    if n == 0:
        return []
    lg = [1] * n
    pred = [-1] * n
    for j in range(n):
        for i in range(j):
            if L[i] < L[j] and lg[i] + 1 > lg[j]:
                lg[j] = lg[i] + 1
                pred[j] = i
    k = 0
    for j in range(n):
        if lg[j] > lg[k]:
            k = j
    S = []
    while k != -1:
        S.append(L[k])
        k = pred[k]
    S.reverse()
    return S
```

Deux boucles imbriquées : $\frac{n(n-1)}2$ comparaisons, $O(n^2)$ ; la reconstruction est en $O(n)$.

**4.4 Exemple.** Les longueurs sont `lg = [1, 1, 2, 1, 3, 4, 2, 4, 3, 3, 4]`. Le premier maximum, $4$, est atteint à l'indice 5 (valeur 9) ; en remontant : $9\leftarrow5\leftarrow4\leftarrow3$. Résultat : `[3, 4, 5, 9]`. D'autres réponses de même longueur existent, par exemple `[1, 2, 3, 5]`.

> **Remarque.** Un algorithme plus fin, avec une recherche dichotomique, atteint $O(n\log n)$.

**Étape 5 — Vérification.**

> **Vérification — Contrôle.** Le résultat est bien une sous-suite strictement croissante, et sa longueur coïncide avec celle trouvée par force brute sur des listes aléatoires de longueur au plus 10.

**Étape 6 — Conclusion.**
$$\boxed{\ell_j=1+\max_{i<j,\,L_i<L_j}\ell_i\ ;\ \text{réponse }[3,4,5,9]\text{ de longueur }4,\ O(n^2)}$$""",
r"""$2^n$ sous-suites ; $\ell_j=1+\max\{\ell_i: i<j, L_i<L_j\}$ ; $O(n^2)$ avec reconstruction par `pred` ; `[3, 4, 5, 9]`.""")
src('Programmation dynamique')

# ------------------------------------------------------------------ 17. Matrice de confusion
ex('i-ia-confusion', M, 'Apprentissage', 1, 'Matrice de confusion, précision et rappel', 20, r"""
Un classifieur (par exemple les $k$ plus proches voisins) a été testé sur 10 images dont on connaît la vraie classe :

```python
vrais   = ['chat', 'chat', 'chat', 'chat', 'chien',
           'chien', 'chien', 'lapin', 'lapin', 'lapin']
predits = ['chat', 'chat', 'chien', 'chat', 'chien',
           'chien', 'chat', 'lapin', 'chien', 'lapin']
```

1. Écrire une fonction `confusion(vrais, predits, classes)` qui renvoie la matrice `C` où `C[a][b]` est le nombre d'éléments de vraie classe `classes[a]` prédits dans la classe `classes[b]`. La calculer avec `classes = ['chat', 'chien', 'lapin']`.
2. Exprimer le taux de bonnes réponses à l'aide de `C`, et le calculer.
3. Pour une classe $c$, la **précision** est la proportion de bonnes réponses parmi les éléments prédits dans $c$, le **rappel** la proportion d'éléments de $c$ correctement prédits. Les calculer pour `chien`.
4. Un classifieur qui répond toujours `chat` sur un jeu de test contenant 95 % de chats a un taux de bonnes réponses de 95 %. Pourquoi est-ce trompeur ?
""", r"""Associe à chaque classe son indice avec un dictionnaire, puis incrémente une case par élément.""",
r"""Les bonnes réponses sont sur la diagonale.""",
r"""Précision : diagonale divisée par la somme de la **colonne** ; rappel : diagonale divisée par la somme de la **ligne**.""",
r"""**Étape 1 — Analyse de l'énoncé.** La matrice de confusion détaille les erreurs d'un classifieur : quelle classe est confondue avec quelle autre.

**Étape 2 — Rappels du cours.**

> **Définition — Matrice de confusion.** Lignes : vraies classes ; colonnes : classes prédites. Un classifieur parfait a une matrice diagonale.

**Étape 3 — Stratégie.** Indexer les classes, compter, puis lire les sommes de lignes et de colonnes.

**Étape 4 — Résolution détaillée.**

**4.1 Construction.**

```python
def confusion(vrais, predits, classes):
    k = len(classes)
    num = {c: a for a, c in enumerate(classes)}
    C = [[0] * k for _ in range(k)]
    for v, p in zip(vrais, predits):
        C[num[v]][num[p]] += 1
    return C
```

Sur l'exemple : `[[3, 1, 0], [1, 2, 0], [0, 1, 2]]`. Par exemple, la première ligne dit que sur 4 chats, 3 ont été reconnus et 1 a été pris pour un chien.

**4.2 Taux de bonnes réponses.** C'est la trace divisée par le nombre total d'éléments :
$$\frac{3+2+2}{10}=0{,}7.$$

**4.3 Précision et rappel pour `chien`.** La colonne `chien` contient $1+2+1=4$ prédictions dont 2 justes : précision $\frac24=0{,}5$. La ligne `chien` contient 3 vrais chiens dont 2 reconnus : rappel $\frac23\approx0{,}67$.

```python
def precision_rappel(C, a):
    col = sum(C[b][a] for b in range(len(C)))
    lig = sum(C[a])
    return C[a][a] / col, C[a][a] / lig
```

**4.4 Classes déséquilibrées.** Ce classifieur ne reconnaît aucun élément des autres classes : leur rappel est nul. Le taux global est dominé par la classe majoritaire et masque cet échec ; la matrice de confusion, ou la précision et le rappel par classe, le révèlent.

**Étape 5 — Vérification.**

> **Vérification — Sommes.** La somme des coefficients vaut 10 ; les sommes des lignes $4,3,3$ sont les effectifs réels, celles des colonnes $4,4,2$ les effectifs prédits.

**Étape 6 — Conclusion.**
$$\boxed{C=\begin{pmatrix}3&1&0\\1&2&0\\0&1&2\end{pmatrix},\ \text{taux }0{,}7,\ \text{chien : précision }0{,}5,\ \text{rappel }\tfrac23}$$""",
r"""`[[3, 1, 0], [1, 2, 0], [0, 1, 2]]` ; taux $0{,}7$ ; chien : précision $0{,}5$, rappel $2/3$ ; le taux global masque les classes minoritaires.""")
src('Intelligence artificielle : apprentissage')

# ------------------------------------------------------------------ 18. Attracteur
ex('i-jeu-attr', M, 'Théorie des jeux', 3, 'Jeux d\'accessibilité : calcul de l\'attracteur', 30, r"""
Une **arène** est un graphe orienté dont chaque sommet appartient à l'un des deux joueurs, 0 ou 1 ; chaque sommet a au moins un successeur. Un jeton est posé sur un sommet ; le propriétaire du sommet courant choisit un successeur, et ainsi de suite. Le joueur 0 gagne si le jeton atteint un sommet de l'ensemble cible $F$ ; sinon (partie infinie évitant $F$), le joueur 1 gagne.

```python
succ = {0: [1, 2], 1: [3, 4], 2: [4, 6], 3: [5, 0], 4: [5],
        5: [5], 6: [6, 3]}
joueur = [0, 1, 1, 0, 0, 1, 1]
F = {5}
```

On définit $A_0=F$ et
$$A_{k+1}=A_k\cup\{s\text{ au joueur }0 : \text{un successeur de }s\text{ est dans }A_k\}\cup\{s\text{ au joueur }1 : \text{tous les successeurs de }s\text{ sont dans }A_k\}.$$

1. Calculer à la main $A_1$, $A_2$, $A_3$, … sur l'exemple, jusqu'à ce que la suite soit stationnaire. On note $A$ sa limite, l'**attracteur** de $F$.
2. Écrire une fonction `attracteur(succ, joueur, F)` qui calcule $A$ en itérant la définition.
3. Montrer que depuis tout sommet de $A$, le joueur 0 peut forcer l'arrivée dans $F$, et que depuis tout sommet hors de $A$, le joueur 1 peut empêcher indéfiniment le jeton d'entrer dans $A$. Donner une stratégie gagnante pour le joueur 0 sur l'exemple.
4. Quelle est la complexité de la fonction de la question 2, avec $n$ sommets et $p$ arcs ? Proposer une version en $O(n+p)$.
""", r"""Le **rang** d'un sommet est le plus petit $k$ tel qu'il appartienne à $A_k$. Sur l'exemple, 3 et 4 ont le rang 1.""",
r"""Pour le joueur 0, choisir toujours un successeur de rang strictement plus petit. Pour la réciproque, montre qu'un sommet du joueur 1 hors de $A$ a un successeur hors de $A$, et qu'un sommet du joueur 0 hors de $A$ n'a que des successeurs hors de $A$.""",
r"""Pour la version linéaire, compte pour chaque sommet du joueur 1 le nombre de successeurs pas encore attirés, et propage depuis $F$ avec une file et le graphe inverse.""",
r"""**Étape 1 — Analyse de l'énoncé.** L'attracteur est l'ensemble des positions gagnantes du joueur 0 dans un jeu d'accessibilité. On le construit par couches : $A_k$ contient les sommets depuis lesquels le joueur 0 peut forcer $F$ en au plus $k$ coups.

**Étape 2 — Rappels du cours.**

> **Définition — Stratégie.** Une stratégie d'un joueur associe à chaque sommet qui lui appartient un successeur ; elle est gagnante si elle gagne contre toutes les réponses de l'adversaire.

> **Propriété — Suite croissante d'ensembles.** Une suite croissante de parties d'un ensemble fini à $n$ éléments est stationnaire au plus tard à partir du rang $n$.

**Étape 3 — Stratégie.** Calcul par couches, preuve par récurrence sur le rang, puis amélioration avec des compteurs.

**Étape 4 — Résolution détaillée.**

**4.1 Calcul à la main.** $A_0=\{5\}$. Les sommets 3 et 4 (joueur 0) ont le successeur 5 : $A_1=\{3,4,5\}$. Le sommet 1 (joueur 1) n'a que des successeurs dans $A_1$ : $A_2=\{1,3,4,5\}$. Le sommet 0 (joueur 0) a le successeur 1 : $A_3=\{0,1,3,4,5\}$. Ensuite, 2 a le successeur $6\notin A_3$ et 6 le successeur $6\notin A_3$ : $A_4=A_3$. Donc
$$A=\{0,1,3,4,5\},\qquad\text{de rangs }3,2,1,1,0.$$

**4.2 Itération naïve.**

```python
def attracteur(succ, joueur, F):
    A = set(F)
    change = True
    while change:
        change = False
        for s in succ:
            if s not in A:
                if joueur[s] == 0:
                    ok = any(t in A for t in succ[s])
                else:
                    ok = all(t in A for t in succ[s])
                if ok:
                    A.add(s)
                    change = True
    return A
```

Ajouter un sommet en cours de tour ne fait qu'accélérer la convergence : le résultat est le même ensemble $A$ (tout sommet ajouté vérifie la condition par rapport à un ensemble inclus dans $A$, et la boucle s'arrête quand plus aucun sommet ne la vérifie).

**4.3 Correction.**
- **Depuis $A$, le joueur 0 gagne.** Par récurrence sur le rang $k$. Rang 0 : le jeton est dans $F$. Rang $k\ge1$ : si le sommet est au joueur 0, il a un successeur de rang $<k$, que le joueur 0 choisit ; s'il est au joueur 1, tous ses successeurs sont de rang $<k$. Dans les deux cas, le rang diminue strictement à chaque coup : $F$ est atteint en au plus $k$ coups.
- **Hors de $A$, le joueur 1 gagne.** Comme $A$ est stable, un sommet $s\notin A$ du joueur 0 n'a aucun successeur dans $A$, et un sommet $s\notin A$ du joueur 1 a au moins un successeur hors de $A$ (sinon $s$ serait ajouté). Le joueur 1 choisit toujours un tel successeur : le jeton reste hors de $A$, donc hors de $F\subset A$, indéfiniment.

Stratégie gagnante du joueur 0 sur l'exemple : de 0 aller en 1, de 3 aller en 5, de 4 aller en 5. Depuis 2 ou 6, le joueur 1 gagne en jouant 6 puis en restant sur 6.

**4.4 Complexité et version linéaire.** Chaque passage de la boucle `while` examine tous les arcs, en $O(n+p)$, et ajoute au moins un sommet, sauf le dernier : au plus $n+1$ passages, d'où $O(n(n+p))$.

Version linéaire : on parcourt le graphe inverse depuis $F$. Pour un sommet du joueur 1, un compteur indique combien de ses successeurs ne sont pas encore attirés ; il est attiré quand ce compteur tombe à 0.

```python
from collections import deque

def attracteur_lineaire(succ, joueur, F):
    pred = {s: [] for s in succ}
    for s in succ:
        for t in succ[s]:
            pred[t].append(s)
    reste = {s: len(succ[s]) for s in succ}
    A = set(F)
    file = deque(F)
    while file:
        t = file.popleft()
        for s in pred[t]:
            if s not in A:
                reste[s] -= 1
                if joueur[s] == 0 or reste[s] == 0:
                    A.add(s)
                    file.append(s)
    return A
```

Chaque sommet est enfilé au plus une fois, et chaque arc $s\to t$ est examiné une fois, quand $t$ est défilé : $O(n+p)$.

**Étape 5 — Vérification.**

> **Vérification — Concordance.** Les deux fonctions renvoient `{0, 1, 3, 4, 5}` sur l'exemple, et coïncident sur des arènes aléatoires.

**Étape 6 — Conclusion.**
$$\boxed{A=\{0,1,3,4,5\}\ ;\ \text{joueur 0 : descendre en rang ; joueur 1 : rester hors de }A\ ;\ O(n+p)}$$""",
r"""$A_0=\{5\}$, $A_1=\{3,4,5\}$, $A_2=\{1,3,4,5\}$, $A=\{0,1,3,4,5\}$ ; récurrence sur le rang ; hors de $A$ le joueur 1 reste hors de $A$ ; $O(n(n+p))$ naïf, $O(n+p)$ avec compteurs.""")
src('Théorie des jeux')

# ------------------------------------------------------------------ 19. SQL : locations de films
ex('i-sql-films', M, 'Bases de données (SQL)', 1, 'Requêtes SQL sur des locations de films', 20, r"""
On considère deux tables :
- `films(idf, titre, annee)` : `idf` est la clé primaire ;
- `locations(idc, idf, debut, duree)` : un client `idc` loue le film `idf` à la date `debut` pour `duree` jours (un flottant) ; `idf` fait référence à `films`.

Elles contiennent :

| idf | titre | annee |
|---|---|---|
| 1 | Les Intégrales | 2012 |
| 2 | Le Pivot de Gauss | 2001 |
| 3 | Taylor-Lagrange | 2011 |
| 4 | La Colle | 1995 |

| idc | idf | debut | duree |
|---|---|---|---|
| 10 | 1 | 2026-01-03 | 1.0 |
| 11 | 1 | 2026-01-05 | 2.0 |
| 10 | 2 | 2026-02-01 | 3.5 |
| 12 | 2 | 2026-02-02 | 4.5 |
| 11 | 3 | 2026-02-10 | 1.5 |

1. Écrire une requête qui renvoie la plus grande durée de location. Quel est son résultat ?
2. Écrire une requête qui renvoie les titres et années des films sortis depuis 2000, du plus récent au plus ancien.
3. Écrire une requête qui renvoie, pour chaque film loué en moyenne moins de 2 jours, son identifiant, son titre et sa durée moyenne de location, par durée moyenne décroissante. Quel est son résultat ?
4. Pourquoi la condition `AVG(duree) < 2` ne peut-elle pas figurer dans un `WHERE` ?
5. Écrire une requête qui renvoie les identifiants des films jamais loués.
""", r"""Les fonctions d'agrégation `MAX`, `AVG`, `COUNT` résument une colonne.""",
r"""Pour la question 3, il faut une jointure `films JOIN locations ON ...`, puis `GROUP BY` et `HAVING`.""",
r"""Pour la question 5, pense aux opérateurs ensemblistes : `EXCEPT`.""",
r"""**Étape 1 — Analyse de l'énoncé.** On interroge deux tables reliées par `idf`. Les questions mobilisent une agrégation, un tri, une jointure avec regroupement, et une différence ensembliste.

**Étape 2 — Rappels du cours.**

> **Méthode — Ordre logique d'une requête.** `FROM` (et `JOIN`) construit les lignes, `WHERE` filtre les lignes, `GROUP BY` forme les groupes, `HAVING` filtre les groupes, `SELECT` calcule les colonnes, `ORDER BY` trie, `LIMIT` coupe.

> **Définition — Clé primaire.** Attribut (ou groupe d'attributs) qui identifie une ligne de façon unique.

**Étape 3 — Stratégie.** Traduire chaque question en clauses, dans l'ordre logique ci-dessus.

**Étape 4 — Résolution détaillée.**

**4.1 Plus grande durée.**

```sql
SELECT MAX(duree) FROM locations;
```

Résultat : $4{,}5$.

**4.2 Films récents.**

```sql
SELECT titre, annee
FROM films
WHERE annee >= 2000
ORDER BY annee DESC;
```

Résultat : Les Intégrales (2012), Taylor-Lagrange (2011), Le Pivot de Gauss (2001).

**4.3 Films loués en moyenne moins de 2 jours.**

```sql
SELECT f.idf, f.titre, AVG(l.duree) AS moy
FROM films AS f
JOIN locations AS l ON f.idf = l.idf
GROUP BY f.idf, f.titre
HAVING AVG(l.duree) < 2
ORDER BY moy DESC;
```

Les moyennes sont $1{,}5$ (film 1), $4$ (film 2) et $1{,}5$ (film 3) ; le film 4 n'apparaît pas dans la jointure. Résultat : les films 1 et 3, de moyenne $1{,}5$ (à égalité, l'ordre entre eux n'est pas fixé, sauf à ajouter un second critère de tri).

**4.4 `WHERE` et `HAVING`.** `WHERE` s'applique à chaque ligne **avant** le regroupement : la moyenne d'un groupe n'existe pas encore. Une condition sur un agrégat se place dans `HAVING`, évalué après `GROUP BY`.

**4.5 Films jamais loués.**

```sql
SELECT idf FROM films
EXCEPT
SELECT idf FROM locations;
```

Résultat : le film 4.

**Étape 5 — Vérification.**

> **Vérification — Exécution.** Ces requêtes ont été exécutées avec SQLite sur les deux tables ci-dessus et donnent les résultats annoncés.

**Étape 6 — Conclusion.**
$$\boxed{4{,}5\ ;\ \text{films }1\text{ et }3\ (\text{moyenne }1{,}5)\ ;\ \text{film }4\text{ jamais loué}}$$""",
r"""`MAX(duree)` vaut 4,5 ; jointure + `GROUP BY` + `HAVING AVG(duree) < 2` : films 1 et 3 ; `EXCEPT` donne le film 4.""")
src('Bases de données (SQL)', "Exercice original dans l'esprit des questions SQL des sujets CCINP MP rassemblés dans le cours d'informatique MP de D. Rupprecht (lycée Pierre-de-Fermat).")

# ------------------------------------------------------------------ 20. SQL : notes
ex('i-sql-notes', M, 'Bases de données (SQL)', 2, 'Requêtes SQL : moyennes, groupes et autojointure', 25, r"""
On considère les tables `eleves(ide, nom, classe)`, de clé primaire `ide`, et `notes(ide, matiere, note)`, où `ide` fait référence à `eleves` :

| ide | nom | classe |
|---|---|---|
| 1 | Amine | MP |
| 2 | Lina | MP |
| 3 | Yanis | PC |
| 4 | Sara | MP |
| 5 | Noé | PC |

| ide | matiere | note |
|---|---|---|
| 1 | maths | 14 |
| 1 | physique | 9 |
| 1 | info | 16 |
| 2 | maths | 12 |
| 2 | physique | 15 |
| 2 | info | 13 |
| 3 | maths | 8 |
| 3 | physique | 11 |
| 4 | maths | 17 |
| 4 | physique | 16 |
| 4 | info | 18 |

1. Écrire une requête qui renvoie le nom et la moyenne de chaque élève ayant au moins une note.
2. Écrire une requête qui renvoie le nom de l'élève de MP de meilleure moyenne. Résultat ?
3. Écrire une requête qui renvoie le nom des élèves dont toutes les notes sont au moins égales à 10. Résultat ?
4. Écrire une requête qui renvoie, pour chaque classe, le nombre d'élèves ayant au moins une note. Pourquoi faut-il `COUNT(DISTINCT ...)` ?
5. Écrire une requête qui renvoie tous les couples de noms d'élèves distincts d'une même classe, chaque couple n'apparaissant qu'une fois. Combien y en a-t-il ?
""", r"""Joindre `eleves` et `notes` sur `ide`, puis regrouper par élève.""",
r"""« Toutes les notes au moins 10 » équivaut à « la plus petite note au moins 10 » : `HAVING MIN(note) >= 10`.""",
r"""Pour la question 5, joindre la table `eleves` avec elle-même, avec deux alias, et imposer `e1.ide < e2.ide`.""",
r"""**Étape 1 — Analyse de l'énoncé.** On manipule une jointure, des regroupements avec agrégats, un tri limité et une autojointure. Noé n'a aucune note : il disparaît de toute jointure avec `notes`.

**Étape 2 — Rappels du cours.**

> **Méthode — Regroupement.** Après `GROUP BY`, chaque colonne du `SELECT` doit être une colonne de regroupement ou un agrégat (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`).

> **Définition — Autojointure.** Jointure d'une table avec elle-même, en la renommant avec deux alias.

**Étape 3 — Stratégie.** Écrire la jointure une fois, puis faire varier le regroupement et le filtre sur les groupes.

**Étape 4 — Résolution détaillée.**

**4.1 Moyenne par élève.**

```sql
SELECT e.nom, AVG(n.note) AS moy
FROM eleves AS e
JOIN notes AS n ON e.ide = n.ide
GROUP BY e.ide, e.nom;
```

Moyennes : Amine $13$, Lina $\frac{40}3\approx13{,}3$, Yanis $9{,}5$, Sara $17$. On regroupe par `ide` (et pas seulement par `nom`) car deux élèves peuvent porter le même nom.

**4.2 Meilleur élève de MP.**

```sql
SELECT e.nom
FROM eleves AS e
JOIN notes AS n ON e.ide = n.ide
WHERE e.classe = 'MP'
GROUP BY e.ide, e.nom
ORDER BY AVG(n.note) DESC
LIMIT 1;
```

Résultat : Sara. La condition sur la classe porte sur les lignes : elle va dans `WHERE`.

**4.3 Aucune note sous 10.**

```sql
SELECT e.nom
FROM eleves AS e
JOIN notes AS n ON e.ide = n.ide
GROUP BY e.ide, e.nom
HAVING MIN(n.note) >= 10;
```

Résultat : Lina et Sara. Écrire `WHERE note >= 10` serait faux : on éliminerait seulement les mauvaises notes, et Amine apparaîtrait avec ses deux autres notes.

**4.4 Élèves notés par classe.**

```sql
SELECT e.classe, COUNT(DISTINCT e.ide) AS nb
FROM eleves AS e
JOIN notes AS n ON e.ide = n.ide
GROUP BY e.classe;
```

La jointure contient une ligne **par note** : sans `DISTINCT`, on compterait 9 lignes en MP au lieu de 3 élèves. Résultat : MP 3, PC 1 (Noé n'a pas de note).

**4.5 Couples d'une même classe.**

```sql
SELECT e1.nom, e2.nom
FROM eleves AS e1
JOIN eleves AS e2 ON e1.classe = e2.classe
WHERE e1.ide < e2.ide;
```

La condition `e1.ide < e2.ide` exclut les couples d'un élève avec lui-même et ne garde qu'un ordre par couple. En MP, 3 élèves donnent $\binom32=3$ couples ; en PC, 1 couple : **4 couples**.

**Étape 5 — Vérification.**

> **Vérification — Exécution.** Toutes ces requêtes ont été exécutées avec SQLite sur les tables ci-dessus et donnent les résultats annoncés.

**Étape 6 — Conclusion.**
$$\boxed{\text{Sara ; Lina et Sara ; MP }3,\ \text{PC }1\ ;\ 4\text{ couples}}$$""",
r"""Jointure sur `ide` + `GROUP BY` ; Sara (17) ; `HAVING MIN(note) >= 10` : Lina et Sara ; `COUNT(DISTINCT ...)` : MP 3, PC 1 ; autojointure avec `e1.ide < e2.ide` : 4 couples.""")
src('Bases de données (SQL)', "Exercice original sur le langage SQL du programme d'informatique commune (requêtes, agrégats, jointures), en lien avec les sujets CCINP MP rassemblés dans le cours de D. Rupprecht (lycée Pierre-de-Fermat).")
