# Informatique commune MP (suite) : graphes, programmation dynamique, apprentissage,
# théorie des jeux, nombres flottants. Code testé par tools/test_info.py.
from newlib import ex, E

def src(chapitre):
    E[-1]['enonce'] += f"\n\n*Exercice original sur le chapitre « {chapitre} » du cours d'informatique MP de D. Rupprecht (lycée Pierre-de-Fermat).*"
    E[-1]['ajout'] = '2026-11-25'

M = 'Informatique'

# ------------------------------------------------------------------ 1. BFS
ex('i-gr-bfs', M, 'Graphes', 1, 'Parcours en largeur et distances', 20, r"""
Un graphe non orienté à $n$ sommets numérotés $0,\dots,n-1$ est donné par listes d'adjacence : `G[s]` est la liste des voisins de `s`.

1. Écrire une fonction `distances(G, s)` qui renvoie la liste `D` où `D[t]` est le nombre minimal d'arêtes d'un chemin de `s` à `t`, et `-1` si `t` n'est pas accessible. Utiliser une file (`collections.deque`).
2. Donner la complexité en fonction du nombre de sommets $n$ et du nombre d'arêtes $p$.
3. Appliquer à `G = [[1, 2], [0, 3], [0, 3], [1, 2, 4], [3], []]` depuis le sommet 0.
""", r"""Une file traite les sommets dans l'ordre de leur découverte : d'abord ceux à distance 1, puis à distance 2…""",
r"""Quand on découvre un voisin `v` de `u` jamais vu, `D[v] = D[u] + 1` et on l'enfile.""",
r"""Chaque sommet est enfilé au plus une fois, et chaque liste d'adjacence est parcourue une fois.""",
r"""**Étape 1 — Analyse de l'énoncé.** Dans un graphe non pondéré, le parcours en largeur visite les sommets par distance croissante à la source : il calcule les plus courts chemins en nombre d'arêtes.

**Étape 2 — Rappels du cours.**

> **Définition — File.** Premier entré, premier sorti. `deque` permet `append` et `popleft` en $O(1)$ (alors que `pop(0)` sur une liste coûte $O(n)$).

> **Propriété — Parcours en largeur.** Les sommets sont défilés par distance croissante à la source ; le parcours coûte $O(n+p)$ avec des listes d'adjacence.

**Étape 3 — Stratégie.** `D[t] = -1` sert à la fois de marque « non vu » et de distance inconnue.

**Étape 4 — Résolution détaillée.**

**4.1 Programme.**

```python
from collections import deque

def distances(G, s):
    D = [-1] * len(G)
    D[s] = 0
    F = deque([s])
    while F:
        u = F.popleft()
        for v in G[u]:
            if D[v] == -1:
                D[v] = D[u] + 1
                F.append(v)
    return D
```

**4.2 Complexité.** Un sommet n'est enfilé que si `D[v] == -1`, et `D[v]` reçoit alors une valeur : au plus $n$ passages dans le `while`. La liste `G[u]` est parcourue une fois par sommet défilé ; la somme des longueurs des listes vaut $2p$. Total : $O(n+p)$.

**4.3 Exemple.** File : `[0]` → on découvre 1 et 2 (distance 1) → depuis 1, on découvre 3 (distance 2) → depuis 3, on découvre 4 (distance 3). Le sommet 5 est isolé. Résultat : `[0, 1, 1, 2, 3, -1]`.

**Étape 5 — Vérification.**

> **Vérification — Cohérence.** Pour chaque arête $\{u,v\}$ entre sommets accessibles, $|D[u]-D[v]|\le1$ : ici $(0,1)$, $(0,2)$, $(1,3)$, $(2,3)$, $(3,4)$ la vérifient.

**Étape 6 — Conclusion.**
$$\boxed{\text{BFS : }O(n+p);\quad D=[0,1,1,2,3,-1]}$$""",
r"""File `deque`, marquage par `D[v] == -1` et `D[v] = D[u] + 1` ; $O(n+p)$ ; résultat `[0, 1, 1, 2, 3, -1]`.""")
src('Graphes')

# ------------------------------------------------------------------ 2. Composantes et cycle
ex('i-gr-cycle', M, 'Graphes', 2, 'Composantes connexes et détection de cycle', 25, r"""
On reprend un graphe non orienté simple (sans boucle ni arête multiple) donné par listes d'adjacence `G`, avec $n$ sommets et $p$ arêtes.

1. Écrire une fonction `composantes(G)` qui renvoie le nombre de composantes connexes, à l'aide d'un parcours en profondeur récursif.
2. On rappelle qu'une forêt (graphe sans cycle) à $n$ sommets et $c$ composantes connexes possède exactement $n-c$ arêtes. En déduire une fonction `a_un_cycle(G)` en $O(n+p)$.
3. Écrire une version directe, `cycle_dfs(G)`, qui détecte un cycle pendant le parcours en profondeur en mémorisant le parent de chaque sommet.
""", r"""Lance un parcours depuis chaque sommet non encore visité : chaque lancement découvre une nouvelle composante.""",
r"""Un graphe a un cycle si et seulement s'il a strictement plus de $n-c$ arêtes.""",
r"""Pendant le parcours depuis `u`, un voisin déjà visité qui n'est pas le parent de `u` révèle un cycle.""",
r"""**Étape 1 — Analyse de l'énoncé.** Deux méthodes : compter les arêtes (propriété des forêts), ou détecter directement une arête qui referme un chemin.

**Étape 2 — Rappels du cours.**

> **Propriété — Forêts.** Un graphe non orienté à $n$ sommets et $c$ composantes est sans cycle si et seulement s'il a exactement $n-c$ arêtes ; il en a toujours au moins $n-c$.

> **Propriété — Parcours en profondeur.** Depuis un sommet, il visite toute sa composante connexe, en $O(n+p)$ au total.

**Étape 3 — Stratégie.** Parcours depuis chaque sommet non vu pour compter les composantes ; comparaison $p$ contre $n-c$ ; puis détection via le parent.

**Étape 4 — Résolution détaillée.**

**4.1 Composantes.**

```python
def composantes(G):
    vu = [False] * len(G)
    def explorer(u):
        vu[u] = True
        for v in G[u]:
            if not vu[v]:
                explorer(v)
    c = 0
    for s in range(len(G)):
        if not vu[s]:
            c += 1
            explorer(s)
    return c
```

**4.2 Par comptage.** Le nombre d'arêtes vaut $p=\frac12\sum_s\text{len}(G[s])$.

```python
def a_un_cycle(G):
    p = sum(len(voisins) for voisins in G) // 2
    return p > len(G) - composantes(G)
```

**4.3 Détection directe.**

```python
def cycle_dfs(G):
    vu = [False] * len(G)
    def explorer(u, parent):
        vu[u] = True
        for v in G[u]:
            if not vu[v]:
                if explorer(v, u):
                    return True
            elif v != parent:
                return True
        return False
    return any(not vu[s] and explorer(s, -1) for s in range(len(G)))
```

Si `v` est déjà visité et n'est pas le parent, il existe un chemin de `v` à `u` dans l'arbre du parcours, que l'arête $\{u,v\}$ referme : c'est un cycle. Réciproquement, dans un cycle, le premier sommet atteint par le parcours finit par voir un voisin déjà visité autre que son parent.

**Étape 5 — Vérification.**

> **Vérification — Exemples.** Le chemin `[[1], [0, 2], [1]]` : 1 composante, 2 arêtes $=3-1$, pas de cycle. Le triangle `[[1, 2], [0, 2], [0, 1]]` : 3 arêtes $>2$, cycle. Les deux fonctions concordent.

**Étape 6 — Conclusion.**
$$\boxed{\text{cycle}\iff p>n-c,\ \text{ou voisin déjà vu différent du parent ; }O(n+p)}$$""",
r"""Un parcours par sommet non vu compte les composantes $c$ ; il y a un cycle si et seulement si $p>n-c$ ; en direct, c'est un voisin déjà visité autre que le parent. Tout en $O(n+p)$.""")
src('Graphes')

# ------------------------------------------------------------------ 3. Dijkstra
ex('i-gr-dijk', M, 'Graphes', 2, 'Dijkstra à la main et avec un tas', 30, r"""
Un graphe orienté pondéré à poids positifs est donné par `G[u] = [(v, poids), ...]`. On considère :

`G = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5)], [(4, 3)], []]`

1. Appliquer l'algorithme de Dijkstra depuis le sommet 0 : donner, dans l'ordre, les sommets fixés et leur distance.
2. Écrire `dijkstra(G, s)` en utilisant le module `heapq`, qui renvoie la liste des distances (`float('inf')` si inaccessible).
3. Donner sa complexité. Pourquoi l'algorithme est-il faux avec des poids négatifs ? Donner un contre-exemple à trois sommets.
""", r"""À chaque étape, on fixe le sommet non encore fixé de plus petite distance provisoire, puis on relâche ses arcs sortants.""",
r"""Avec `heapq`, on pousse des couples `(distance, sommet)` ; un couple dont la distance est dépassée est simplement ignoré.""",
r"""Avec un arc négatif, un sommet fixé trop tôt pourrait encore être amélioré par un chemin passant par un sommet fixé plus tard.""",
r"""**Étape 1 — Analyse de l'énoncé.** Plus courts chemins depuis une source, poids positifs : algorithme glouton de Dijkstra, puis implémentation avec une file de priorité.

**Étape 2 — Rappels du cours.**

> **Principe — Algorithme de Dijkstra.** On maintient des distances provisoires ; on fixe le sommet non fixé de distance minimale, puis on relâche ses arcs : `d[v] = min(d[v], d[u] + w)`. Avec des poids positifs, une distance fixée est définitive.

> **Rappel — Module heapq.** `heappush(T, x)` et `heappop(T)` en $O(\log m)$ pour un tas de taille $m$ ; `heappop` renvoie le plus petit élément.

**Étape 3 — Stratégie.** Dérouler à la main, programmer avec un tas, puis chercher un arc négatif qui contredit le choix glouton.

**Étape 4 — Résolution détaillée.**

**4.1 À la main.** Départ $d=(0,\infty,\infty,\infty,\infty)$.
- Fixer 0 (0) : $d_1=4$, $d_2=1$.
- Fixer 2 (1) : $d_1=\min(4,1+2)=3$, $d_3=1+5=6$.
- Fixer 1 (3) : $d_3=\min(6,3+1)=4$.
- Fixer 3 (4) : $d_4=7$.
- Fixer 4 (7).

Distances : `[0, 3, 1, 4, 7]`.

**4.2 Programme.**

```python
import heapq

def dijkstra(G, s):
    d = [float('inf')] * len(G)
    d[s] = 0
    T = [(0, s)]
    while T:
        du, u = heapq.heappop(T)
        if du > d[u]:
            continue                      # entrée périmée
        for v, w in G[u]:
            if du + w < d[v]:
                d[v] = du + w
                heapq.heappush(T, (d[v], v))
    return d
```

**4.3 Complexité.** Chaque arc provoque au plus une insertion : au plus $p+1$ éléments dans le tas, chaque opération en $O(\log p)$. Total $O((n+p)\log p)=O((n+p)\log n)$ puisque $p\le n^2$.

**4.4 Poids négatifs.** Arcs $0\to1$ de poids 2, $0\to2$ de poids 3, $2\to1$ de poids −2. Dijkstra fixe 1 avec la distance 2, alors que le chemin $0\to2\to1$ coûte 1. Le choix glouton repose sur le fait qu'un chemin ne peut que s'allonger quand on ajoute des arcs : c'est faux avec des poids négatifs.

**Étape 5 — Vérification.**

> **Vérification — Chemin de 0 à 4.** $0\to2\to1\to3\to4$ coûte $1+2+1+3=7$, et aucun autre chemin n'est plus court ($0\to1\to3\to4$ coûte 8).

**Étape 6 — Conclusion.**
$$\boxed{d=[0,3,1,4,7];\quad O((n+p)\log n);\quad\text{faux si un poids est négatif}}$$""",
r"""Ordre de fixation 0 (0), 2 (1), 1 (3), 3 (4), 4 (7) : `[0, 3, 1, 4, 7]` ; tas avec entrées périmées ignorées, $O((n+p)\log n)$ ; contre-exemple négatif : $0\to1$ (2), $0\to2$ (3), $2\to1$ (−2).""")
src('Graphes')

# ------------------------------------------------------------------ 4. Biparti
ex('i-gr-bip', M, 'Graphes', 3, 'Graphe biparti et 2-coloration', 30, r"""
Un graphe non orienté est *biparti* si l'on peut colorier ses sommets en deux couleurs de sorte que chaque arête relie deux sommets de couleurs différentes.

1. Écrire une fonction `biparti(G)` qui renvoie une coloration (liste de 0 et 1) si le graphe est biparti, et `None` sinon, à l'aide de parcours en largeur.
2. Prouver que si l'algorithme échoue, le graphe contient un cycle de longueur impaire.
3. En déduire qu'un graphe est biparti si et seulement s'il n'a aucun cycle de longueur impaire.
""", r"""Dans chaque composante, colorie la source en 0, puis chaque sommet découvert de la couleur opposée à celle de son découvreur.""",
r"""Avec le parcours en largeur, la couleur d'un sommet est la parité de sa distance à la source de sa composante.""",
r"""Si une arête $\{u,v\}$ relie deux sommets de même couleur, regarde les chemins de la source vers $u$ et vers $v$ dans l'arbre du parcours.""",
r"""**Étape 1 — Analyse de l'énoncé.** On construit la seule coloration possible (au choix de la couleur de départ près dans chaque composante), puis on caractérise l'échec.

**Étape 2 — Rappels du cours.**

> **Propriété — Parcours en largeur.** Il calcule la distance $D(v)$ à la source, et pour toute arête $\{u,v\}$ de la composante, $|D(u)-D(v)|\le1$.

**Étape 3 — Stratégie.** Colorier par la parité de la distance ; un conflit se produit sur une arête dont les extrémités sont à la même distance, ce qui fabrique un cycle impair.

**Étape 4 — Résolution détaillée.**

**4.1 Programme.**

```python
from collections import deque

def biparti(G):
    coul = [-1] * len(G)
    for s in range(len(G)):
        if coul[s] != -1:
            continue
        coul[s] = 0
        F = deque([s])
        while F:
            u = F.popleft()
            for v in G[u]:
                if coul[v] == -1:
                    coul[v] = 1 - coul[u]
                    F.append(v)
                elif coul[v] == coul[u]:
                    return None
    return coul
```

Complexité : $O(n+p)$, comme un parcours en largeur.

**4.2 Échec ⇒ cycle impair.** La couleur d'un sommet est la parité de sa distance $D$ à la source $s$ de sa composante. Un échec révèle une arête $\{u,v\}$ avec $D(u)\equiv D(v)\pmod2$ ; comme $|D(u)-D(v)|\le1$, on a $D(u)=D(v)=k$. Les chemins de l'arbre de parcours de $s$ à $u$ et de $s$ à $v$ ont $k$ arêtes ; soit $w$ leur dernier sommet commun, à distance $j$. Les deux morceaux de $w$ à $u$ et de $w$ à $v$, plus l'arête $\{u,v\}$, forment un cycle de longueur $2(k-j)+1$ : impair.

**4.3 Caractérisation.** Si le graphe a un cycle impair, il n'est pas biparti : le long du cycle, les couleurs alternent, ce qui est impossible sur un nombre impair d'arêtes. Réciproquement, s'il n'a pas de cycle impair, l'algorithme ne peut pas échouer (sinon 4.2 fournirait un tel cycle), et il renvoie une coloration valable.

**Étape 5 — Vérification.**

> **Vérification — Exemples.** Le carré `[[1, 3], [0, 2], [1, 3], [0, 2]]` est biparti : `[0, 1, 0, 1]`. Le triangle `[[1, 2], [0, 2], [0, 1]]` donne `None`.

**Étape 6 — Conclusion.**
$$\boxed{\text{biparti}\iff\text{aucun cycle de longueur impaire};\ \text{test en }O(n+p)}$$""",
r"""Coloration par parité de la distance (BFS) en $O(n+p)$ ; un conflit sur une arête entre sommets de même distance donne un cycle de longueur $2(k-j)+1$ ; donc biparti si et seulement si aucun cycle impair.""")
src('Graphes')

# ------------------------------------------------------------------ 5. Rendu de monnaie
ex('i-pd-monnaie', M, 'Programmation dynamique', 2, 'Rendu de monnaie : glouton contre programmation dynamique', 25, r"""
On dispose de pièces de valeurs entières `P` (en quantité illimitée, avec `1` dans `P`). On veut rendre une somme $s$ avec le moins de pièces possible.

1. L'algorithme glouton prend toujours la plus grande pièce possible. Montrer qu'il n'est pas optimal pour `P = [1, 4, 6]` et $s=8$.
2. Soit $m(x)$ le nombre minimal de pièces pour rendre $x$. Justifier que $m(0)=0$ et $m(x)=1+\min\{m(x-p)\ :\ p\in P,\ p\le x\}$.
3. Écrire une fonction `rendu(P, s)` qui calcule $m(s)$ de bas en haut, puis la modifier pour renvoyer aussi la liste des pièces utilisées.
4. Donner sa complexité.
""", r"""Le glouton commence par 6. Cherche une décomposition de 8 en deux pièces.""",
r"""Dans une solution optimale pour $x$, retire une pièce $p$ : il reste une solution pour $x-p$, qui doit elle-même être optimale.""",
r"""Remplis un tableau `m` de 0 à $s$, et garde dans un second tableau la pièce choisie pour chaque montant.""",
r"""**Étape 1 — Analyse de l'énoncé.** Le choix local « la plus grande pièce » peut être mauvais ; la programmation dynamique explore toutes les dernières pièces possibles en réutilisant les résultats des montants plus petits.

**Étape 2 — Rappels du cours.**

> **Principe — Programmation dynamique.** Un problème qui se décompose en sous-problèmes qui se chevauchent, dont la solution optimale se construit à partir des solutions optimales des sous-problèmes (sous-structure optimale) ; on calcule chaque sous-problème une seule fois.

**Étape 3 — Stratégie.** Contre-exemple au glouton ; relation de récurrence ; tableau rempli par montants croissants ; reconstruction grâce à la pièce choisie.

**Étape 4 — Résolution détaillée.**

**4.1 Glouton.** $8=6+1+1$ : 3 pièces, alors que $8=4+4$ n'en utilise que 2.

**4.2 Récurrence.** Une solution non vide pour $x>0$ contient au moins une pièce $p\le x$ ; en la retirant, on obtient une solution pour $x-p$. Donc $m(x)\ge1+m(x-p)$ pour cette pièce, et $m(x)\ge1+\min_p m(x-p)$. Inversement, ajouter $p$ à une solution optimale de $x-p$ donne une solution de $x$ avec $1+m(x-p)$ pièces. D'où l'égalité. Comme $1\in P$, le minimum porte sur un ensemble non vide.

**4.3 Programme.**

```python
def rendu(P, s):
    m = [0] + [float('inf')] * s
    choix = [0] * (s + 1)
    for x in range(1, s + 1):
        for p in P:
            if p <= x and m[x - p] + 1 < m[x]:
                m[x] = m[x - p] + 1
                choix[x] = p
    pieces, x = [], s
    while x > 0:
        pieces.append(choix[x])
        x -= choix[x]
    return m[s], pieces
```

**4.4 Complexité.** Deux boucles imbriquées : $O(s\cdot|P|)$ en temps, $O(s)$ en mémoire. C'est polynomial en la valeur $s$, pas en sa taille en binaire.

**Étape 5 — Vérification.**

> **Vérification — Exemple.** `rendu([1, 4, 6], 8)` renvoie `(2, [4, 4])` ; `rendu([1, 4, 6], 12)` renvoie `(2, [6, 6])`.

**Étape 6 — Conclusion.**
$$\boxed{m(x)=1+\min_{p\le x}m(x-p),\ \text{calcul en }O(s\,|P|);\ \text{glouton : 3 pièces au lieu de 2 pour }8}$$""",
r"""Glouton : $8=6+1+1$ contre $4+4$ ; $m(x)=1+\min_{p\le x}m(x-p)$ ; tableau de 0 à $s$ et tableau `choix` pour reconstruire ; $O(s\,|P|)$.""")
src('Programmation dynamique')

# ------------------------------------------------------------------ 6. PLSC
ex('i-pd-plsc', M, 'Programmation dynamique', 2, 'Plus longue sous-séquence commune', 30, r"""
Une *sous-séquence* d'un mot s'obtient en supprimant certaines lettres sans changer l'ordre des autres. On cherche la longueur d'une plus longue sous-séquence commune (PLSC) à deux mots `a` (longueur $n$) et `b` (longueur $m$).

1. Soit $L[i][j]$ la longueur d'une PLSC de `a[:i]` et `b[:j]`. Justifier que $L[i][j]=L[i-1][j-1]+1$ si `a[i-1] == b[j-1]`, et $L[i][j]=\max(L[i-1][j],L[i][j-1])$ sinon.
2. Écrire `plsc(a, b)` qui remplit le tableau et renvoie aussi une PLSC.
3. Calculer à la main $L$ pour `a = 'GATTA'` et `b = 'TACTA'`.
4. Donner la complexité, et comparer avec l'énumération de toutes les sous-séquences de `a`.
""", r"""Regarde les dernières lettres : si elles sont égales, on peut les mettre en dernier dans la sous-séquence commune.""",
r"""Si elles sont différentes, au moins l'une des deux n'est pas utilisée : on la retire.""",
r"""Pour reconstruire, pars de la case $(n,m)$ et remonte en suivant le cas qui a donné la valeur.""",
r"""**Étape 1 — Analyse de l'énoncé.** Problème classique de programmation dynamique sur deux préfixes ; on prouve la récurrence, on remplit un tableau $(n+1)\times(m+1)$, puis on remonte.

**Étape 2 — Rappels du cours.**

> **Principe — Programmation dynamique.** Sous-structure optimale et sous-problèmes communs : on calcule toutes les valeurs $L[i][j]$ une fois, dans un ordre où les dépendances sont déjà connues.

**Étape 3 — Stratégie.** Cas sur la dernière lettre ; remplissage par lignes ; reconstruction en partant du coin.

**Étape 4 — Résolution détaillée.**

**4.1 Récurrence.** Cas de base : $L[0][j]=L[i][0]=0$. Si `a[i-1] == b[j-1] = c` : une PLSC de `a[:i-1]` et `b[:j-1]` prolongée par $c$ est commune, donc $L[i][j]\ge L[i-1][j-1]+1$ ; réciproquement, dans une PLSC de `a[:i]` et `b[:j]`, on peut supposer que la dernière lettre utilise les deux dernières positions, et en la retirant on obtient une sous-séquence commune des préfixes plus courts. Si les lettres diffèrent, une sous-séquence commune ne peut pas utiliser à la fois `a[i-1]` et `b[j-1]` en dernière position : elle est commune à `a[:i-1]` et `b[:j]`, ou à `a[:i]` et `b[:j-1]`.

**4.2 Programme.**

```python
def plsc(a, b):
    n, m = len(a), len(b)
    L = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    s, i, j = '', n, m
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            s = a[i - 1] + s
            i, j = i - 1, j - 1
        elif L[i - 1][j] >= L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return L[n][m], s
```

Attention : `[[0] * (m + 1)] * (n + 1)` serait faux, toutes les lignes partageant la même liste.

**4.3 Exemple.** Pour `GATTA` (lignes) et `TACTA` (colonnes), les lignes 1 à 5 du tableau, colonnes 1 à 5, valent `0 0 0 0 0`, `0 1 1 1 1`, `1 1 1 2 2`, `1 1 1 2 2`, `1 2 2 2 3` : $L[5][5]=3$. Le programme renvoie la PLSC `ATA` ; `TTA` convient aussi.

**4.4 Complexité.** $O(nm)$ en temps et en mémoire. L'énumération des $2^n$ sous-séquences de `a`, chacune testée en $O(m)$, coûte $O(2^nm)$ : exponentiel.

**Étape 5 — Vérification.**

> **Vérification — À la main.** `ATA` est une sous-séquence de `GATTA` (on supprime `G` et un `T`) et de `TACTA` (on supprime le premier `T` et `C`). Les sous-séquences de longueur 4 de `GATTA` sont `GTTA`, `GATA`, `GATT` et `ATTA`. Les trois premières contiennent `G`, absent de `TACTA` ; `ATTA` n'est pas dans `TACTA`, où un seul `T` suit le premier `A`. La longueur maximale est donc bien 3.

**Étape 6 — Conclusion.**
$$\boxed{L[i][j]=\begin{cases}L[i-1][j-1]+1&\text{lettres égales}\\\max(L[i-1][j],L[i][j-1])&\text{sinon}\end{cases},\quad O(nm)}$$""",
r"""Récurrence sur les dernières lettres ; tableau $(n+1)\times(m+1)$ rempli par lignes, puis remontée depuis $(n,m)$ ; pour `GATTA` et `TACTA`, longueur 3 (`ATA`) ; $O(nm)$ contre $O(2^nm)$ par énumération.""")
src('Programmation dynamique')

# ------------------------------------------------------------------ 7. Chemin Nord-Est
ex('i-pd-grille', M, 'Programmation dynamique', 1, 'Meilleur chemin Nord-Est dans une grille', 20, r"""
Une grille `T` de $n$ lignes et $m$ colonnes contient des entiers positifs (des pièces à ramasser). On part de la case en bas à gauche $(n-1,0)$ et on arrive en haut à droite $(0,m-1)$, en ne se déplaçant que vers le Nord (ligne $-1$) ou vers l'Est (colonne $+1$).

1. Combien y a-t-il de chemins possibles ? Pourquoi l'énumération est-elle inenvisageable pour une grille $20\times20$ ?
2. Soit $S[i][j]$ le gain maximal d'un chemin du départ à la case $(i,j)$. Écrire la relation de récurrence.
3. Écrire une fonction `meilleur_gain(T)` en $O(nm)$.
""", r"""Un chemin est une suite de $n-1$ pas Nord et $m-1$ pas Est, dans un certain ordre.""",
r"""Pour arriver en $(i,j)$, on vient de la case au Sud $(i+1,j)$ ou de la case à l'Ouest $(i,j-1)$.""",
r"""Remplis le tableau en parcourant les lignes du bas vers le haut, et les colonnes de gauche à droite.""",
r"""**Étape 1 — Analyse de l'énoncé.** Le nombre de chemins explose, mais le meilleur gain jusqu'à une case ne dépend que des meilleurs gains des deux cases précédentes.

**Étape 2 — Rappels du cours.**

> **Formule — Chemins dans une grille.** Le nombre de mots formés de $a$ lettres N et $b$ lettres E est $\binom{a+b}{a}$.

> **Principe — Programmation dynamique.** Calculer les sous-problèmes dans un ordre compatible avec leurs dépendances.

**Étape 3 — Stratégie.** Dénombrement ; récurrence sur la dernière case ; remplissage du bas vers le haut.

**Étape 4 — Résolution détaillée.**

**4.1 Nombre de chemins.** $\binom{n+m-2}{n-1}$. Pour $20\times20$ : $\binom{38}{19}=35\,345\,263\,800$, soit plus de $3\times10^{10}$ chemins, chacun de 39 cases : inenvisageable.

**4.2 Récurrence.** $S[n-1][0]=T[n-1][0]$ ; sur la ligne du bas, on ne peut venir que de l'Ouest ; sur la colonne de gauche, que du Sud ; ailleurs
$$S[i][j]=T[i][j]+\max\big(S[i+1][j],\,S[i][j-1]\big).$$

**4.3 Programme.**

```python
def meilleur_gain(T):
    n, m = len(T), len(T[0])
    S = [[0] * m for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(m):
            avant = []
            if i < n - 1:
                avant.append(S[i + 1][j])
            if j > 0:
                avant.append(S[i][j - 1])
            S[i][j] = T[i][j] + (max(avant) if avant else 0)
    return S[0][m - 1]
```

Chaque case est calculée en $O(1)$ : $O(nm)$.

**Étape 5 — Vérification.**

> **Vérification — Petite grille.** Pour `T = [[1, 2, 5], [3, 1, 1], [4, 0, 2]]`, départ en bas à gauche (4) : le chemin 4 → 3 → 1 → 2 → 5 rapporte 15, et c'est le maximum.

**Étape 6 — Conclusion.**
$$\boxed{\binom{n+m-2}{n-1}\text{ chemins, mais }S[i][j]=T[i][j]+\max(S[i+1][j],S[i][j-1])\text{ en }O(nm)}$$""",
r"""$\binom{n+m-2}{n-1}$ chemins ($>3\cdot10^{10}$ pour 20×20) ; $S[i][j]=T[i][j]+\max(S[i+1][j],S[i][j-1])$, rempli du bas vers le haut en $O(nm)$.""")
src('Programmation dynamique')

# ------------------------------------------------------------------ 8. Sac à dos
ex('i-pd-sac', M, 'Programmation dynamique', 3, 'Sac à dos 0/1 et partition équilibrée', 30, r"""
On dispose de $n$ objets de poids entiers $p_0,\dots,p_{n-1}$ et de valeurs $v_0,\dots,v_{n-1}$, et d'un sac de capacité entière $C$. Chaque objet est pris au plus une fois.

1. Soit $V[k][c]$ la valeur maximale avec les $k$ premiers objets et une capacité $c$. Établir la récurrence.
2. Écrire `sac(p, v, C)` en $O(nC)$, puis une version qui n'utilise qu'une seule liste de taille $C+1$ en parcourant les capacités dans l'ordre décroissant. Pourquoi cet ordre est-il nécessaire ?
3. Application : on veut partager une liste d'entiers positifs en deux groupes de sommes les plus proches possible. Ramener ce problème à un sac à dos, et le résoudre pour `[3, 1, 4, 2, 2]`.
""", r"""L'objet $k-1$ est pris ou non ; s'il est pris, il faut que $p_{k-1}\le c$.""",
r"""Avec une seule liste, si l'on parcourt les capacités croissantes, on risque d'utiliser deux fois le même objet.""",
r"""Pour la partition, cherche le plus grand total atteignable qui ne dépasse pas la moitié de la somme : poids = valeur = l'entier.""",
r"""**Étape 1 — Analyse de l'énoncé.** Choix binaire par objet, contrainte de capacité : programmation dynamique sur (nombre d'objets, capacité restante).

**Étape 2 — Rappels du cours.**

> **Principe — Programmation dynamique.** On remplit un tableau de sous-problèmes indexés par des paramètres entiers bornés ; le coût est le nombre de cases multiplié par le coût d'une case.

**Étape 3 — Stratégie.** Récurrence « pris / pas pris », tableau puis version à une liste, et réduction de la partition au sac à dos.

**Étape 4 — Résolution détaillée.**

**4.1 Récurrence.** $V[0][c]=0$, et pour $k\ge1$ :
$$V[k][c]=\begin{cases}V[k-1][c]&\text{si }p_{k-1}>c\\\max\big(V[k-1][c],\ v_{k-1}+V[k-1][c-p_{k-1}]\big)&\text{sinon.}\end{cases}$$

**4.2 Programmes.**

```python
def sac(p, v, C):
    n = len(p)
    V = [[0] * (C + 1) for _ in range(n + 1)]
    for k in range(1, n + 1):
        for c in range(C + 1):
            V[k][c] = V[k - 1][c]
            if p[k - 1] <= c:
                V[k][c] = max(V[k][c], v[k - 1] + V[k - 1][c - p[k - 1]])
    return V[n][C]

def sac_1d(p, v, C):
    V = [0] * (C + 1)
    for k in range(len(p)):
        for c in range(C, p[k] - 1, -1):
            V[c] = max(V[c], v[k] + V[c - p[k]])
    return V[C]
```

Dans `sac_1d`, au moment de calculer `V[c]`, la case `V[c - p[k]]` doit encore contenir la valeur **sans** l'objet $k$. En parcourant les capacités décroissantes, les cases plus petites n'ont pas encore été mises à jour pour l'objet $k$. Dans l'ordre croissant, `V[c - p[k]]` pourrait déjà contenir l'objet $k$, qui serait alors pris deux fois.

**4.3 Partition équilibrée.** Si la somme totale est $S$, on cherche un groupe de somme $s_1$ la plus grande possible avec $s_1\le\lfloor S/2\rfloor$ : c'est un sac à dos de capacité $\lfloor S/2\rfloor$ où poids et valeur sont égaux à l'entier. L'écart vaut alors $S-2s_1$. Pour `[3, 1, 4, 2, 2]` : $S=12$, capacité 6, et $6=4+2$ est atteignable, donc l'écart est 0 : groupes $\{4,2\}$ et $\{3,1,2\}$.

**Étape 5 — Vérification.**

> **Vérification — Exemple classique.** Poids `[1, 3, 4, 5]`, valeurs `[1, 4, 5, 7]`, capacité 7 : le maximum vaut 9 (objets de poids 3 et 4), et les deux versions le trouvent.

**Étape 6 — Conclusion.**
$$\boxed{V[k][c]=\max\big(V[k-1][c],\,v_{k-1}+V[k-1][c-p_{k-1}]\big),\ O(nC);\ \text{partition : capacité }\lfloor S/2\rfloor}$$""",
r"""Récurrence « pris ou non » en $O(nC)$ ; avec une seule liste, capacités décroissantes pour ne pas réutiliser l'objet ; partition : sac de capacité $\lfloor S/2\rfloor$, écart $S-2s_1$, ici 0 ($\{4,2\}$ et $\{3,1,2\}$).""")
src('Programmation dynamique')

# ------------------------------------------------------------------ 9. kNN
ex('i-ia-knn', M, 'Apprentissage', 1, 'k plus proches voisins', 20, r"""
On dispose d'un jeu de données étiquetées : une liste `X` de points du plan (couples de flottants) et une liste `Y` de leurs classes (des chaînes).

1. Écrire une fonction `distance(a, b)` (distance euclidienne), puis `knn(X, Y, z, k)` qui renvoie la classe majoritaire parmi les $k$ points de `X` les plus proches de `z` (en cas d'égalité, n'importe laquelle des classes majoritaires).
2. Avec `X = [(1, 1), (2, 1), (1, 2), (5, 5), (6, 5), (5, 6)]` et `Y = ['A', 'A', 'A', 'B', 'B', 'B']`, que renvoie `knn(X, Y, (3, 3), 3)` ? Et avec $k=6$ ?
3. Donner la complexité d'une prédiction en fonction de $n=\text{len}(X)$ (on trie les distances). Pourquoi choisit-on souvent $k$ impair pour deux classes ?
""", r"""Calcule la liste des couples `(distance, classe)`, trie-la, et garde les $k$ premiers.""",
r"""Compte les classes avec un dictionnaire, puis prends celle qui a le plus grand effectif.""",
r"""Pour le point (3, 3), calcule ses distances aux points (2, 1), (1, 2) et (5, 5).""",
r"""**Étape 1 — Analyse de l'énoncé.** L'algorithme ne « s'entraîne » pas : il mémorise les données et vote parmi les voisins au moment de la prédiction.

**Étape 2 — Rappels du cours.**

> **Principe — k plus proches voisins.** Pour classer un point, on prend les $k$ points étiquetés les plus proches et on choisit la classe majoritaire parmi eux.

> **Formule — Distance euclidienne.** $d(a,b)=\sqrt{(a_1-b_1)^2+(a_2-b_2)^2}$.

**Étape 3 — Stratégie.** Calculer toutes les distances, trier, voter.

**Étape 4 — Résolution détaillée.**

**4.1 Programme.**

```python
from math import sqrt

def distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def knn(X, Y, z, k):
    D = sorted((distance(x, z), y) for x, y in zip(X, Y))
    votes = {}
    for _, y in D[:k]:
        votes[y] = votes.get(y, 0) + 1
    return max(votes, key=lambda c: votes[c])
```

**4.2 Exemple.** Distances de $(3,3)$ : à $(2,1)$ et $(1,2)$ : $\sqrt5\approx2{,}24$ ; à $(1,1)$ : $\sqrt8\approx2{,}83$ ; à $(5,5)$ : $\sqrt8\approx2{,}83$ ; à $(6,5)$ et $(5,6)$ : $\sqrt{13}\approx3{,}61$. Les trois plus proches sont $(2,1)$, $(1,2)$, puis l'un des deux points à $\sqrt8$. Le tri des couples départage par la classe : `'A' < 'B'`, donc $(1,1)$ passe avant. Résultat `'A'`. Avec $k=6$, chaque classe a 3 votes : égalité, et la réponse dépend du départage (ici `'A'`, première clé rencontrée par `max`).

**4.3 Complexité et choix de k.** $n$ distances en $O(n)$, tri en $O(n\log n)$, vote en $O(k)$ : $O(n\log n)$ par prédiction. Avec deux classes et $k$ impair, il ne peut pas y avoir d'égalité des votes.

**Étape 5 — Vérification.**

> **Vérification — Sens.** Le point $(3,3)$ est plus près du groupe A (centre $(1{,}33;1{,}33)$, distance $\approx2{,}36$) que du groupe B (centre $(5{,}33;5{,}33)$, distance $\approx3{,}30$) : la réponse `'A'` est cohérente.

**Étape 6 — Conclusion.**
$$\boxed{\texttt{knn(X, Y, (3, 3), 3)}=\texttt{'A'};\ O(n\log n)\text{ par prédiction};\ k\text{ impair évite les égalités}}$$""",
r"""Trier les couples (distance, classe), voter parmi les $k$ premiers ; ici `'A'` pour $k=3$ et égalité 3–3 pour $k=6$ ; $O(n\log n)$ par prédiction ; $k$ impair pour deux classes.""")
src('Intelligence artificielle : apprentissage')

# ------------------------------------------------------------------ 10. k-moyennes
ex('i-ia-kmeans', M, 'Apprentissage', 3, 'k-moyennes : une itération et décroissance de l’inertie', 30, r"""
L'algorithme des $k$-moyennes partitionne des points $x_1,\dots,x_n$ du plan en $k$ groupes. Il alterne deux étapes à partir de centres initiaux $c_1,\dots,c_k$ :
- (A) affecter chaque point au centre le plus proche ;
- (B) remplacer chaque centre par le barycentre (moyenne) des points de son groupe.

On note l'inertie $I=\sum_{i=1}^n\|x_i-c_{g(i)}\|^2$, où $g(i)$ est le groupe du point $x_i$.

1. Points $(0,0)$, $(1,0)$, $(0,1)$, $(5,5)$, $(6,5)$, $(9,9)$ ; centres initiaux $c_1=(0,0)$, $c_2=(1,0)$. Effectuer une itération (A puis B) et calculer l'inertie avant et après.
2. Montrer que l'étape (A) ne peut pas augmenter $I$.
3. Montrer que, pour un groupe fixé de points $y_1,\dots,y_m$, la quantité $\sum_j\|y_j-c\|^2$ est minimale pour $c$ égal à leur barycentre. En déduire que (B) ne peut pas augmenter $I$, puis que l'algorithme s'arrête.
4. Écrire une fonction `iteration(X, C)` qui effectue (A) puis (B) et renvoie les nouveaux centres.
""", r"""Pour (A), chaque terme de la somme ne peut que diminuer quand on change un point de centre pour un plus proche.""",
r"""Pour (B), développe $\sum_j\|y_j-c\|^2=\sum_j\|y_j-\bar y\|^2+m\|\bar y-c\|^2$.""",
r"""Il n'y a qu'un nombre fini de partitions possibles des $n$ points.""",
r"""**Étape 1 — Analyse de l'énoncé.** On fait tourner l'algorithme sur un petit exemple, puis on prouve que chaque étape fait décroître l'inertie, ce qui garantit l'arrêt.

**Étape 2 — Rappels du cours.**

> **Principe — k-moyennes.** Alternance affectation au centre le plus proche / recalcul des centres comme barycentres, jusqu'à stabilisation.

> **Formule — Barycentre.** $\bar y=\frac1m\sum_jy_j$ et $\sum_j(y_j-\bar y)=0$.

**Étape 3 — Stratégie.** Calcul direct ; argument terme à terme pour (A) ; identité de König-Huygens pour (B) ; finitude des partitions.

**Étape 4 — Résolution détaillée.**

**4.1 Exemple.** Avant tout, chaque point est affecté à son centre le plus proche : $(0,0)$ et $(0,1)$ à $c_1$ ; $(1,0)$, $(5,5)$, $(6,5)$, $(9,9)$ à $c_2$ (par exemple $(5,5)$ est à distance $\sqrt{41}$ de $c_2$ et $\sqrt{50}$ de $c_1$). Inertie : $0+1+0+41+50+145=237$. Étape (B) : $c_1=(0;0{,}5)$, $c_2=\big(\frac{21}4;\frac{19}4\big)=(5{,}25;4{,}75)$. Nouvelle inertie avec les mêmes groupes : $0{,}25+0{,}25+(4{,}25^2+4{,}75^2)+(0{,}25^2+0{,}25^2)+(0{,}75^2+0{,}25^2)+(3{,}75^2+4{,}25^2)=0{,}5+40{,}625+0{,}125+0{,}625+32{,}125=74$. Elle a fortement diminué.

**4.2 Étape (A).** Chaque point passe à un centre au moins aussi proche : chaque terme $\|x_i-c_{g(i)}\|^2$ diminue ou reste égal, donc $I$ aussi.

**4.3 Étape (B).** En écrivant $y_j-c=(y_j-\bar y)+(\bar y-c)$ et en développant :
$$\sum_j\|y_j-c\|^2=\sum_j\|y_j-\bar y\|^2+2\Big\langle\sum_j(y_j-\bar y),\,\bar y-c\Big\rangle+m\|\bar y-c\|^2=\sum_j\|y_j-\bar y\|^2+m\|\bar y-c\|^2,$$
minimal pour $c=\bar y$. Remplacer chaque centre par le barycentre de son groupe ne peut donc qu'abaisser l'inertie. L'inertie décroît à chaque itération ; elle ne dépend que de la partition une fois les centres recalculés, et il n'y a qu'un nombre fini de partitions : on finit par retomber sur une partition stable, et l'algorithme s'arrête (dans un minimum local, pas forcément le meilleur).

**4.4 Programme.**

```python
def iteration(X, C):
    groupes = [[] for _ in C]
    for x in X:
        d = [(x[0] - c[0]) ** 2 + (x[1] - c[1]) ** 2 for c in C]
        groupes[d.index(min(d))].append(x)
    nouveaux = []
    for g, c in zip(groupes, C):
        if g:
            nouveaux.append((sum(p[0] for p in g) / len(g), sum(p[1] for p in g) / len(g)))
        else:
            nouveaux.append(c)            # groupe vide : on garde l'ancien centre
    return nouveaux
```

**Étape 5 — Vérification.**

> **Vérification — Itération suivante.** Avec $c_1=(0;0{,}5)$ et $c_2=(5{,}25;4{,}75)$, le point $(1,0)$ est maintenant plus proche de $c_1$ : il change de groupe, et l'inertie continue de baisser. On s'attend à un groupe « en bas à gauche » et un groupe « en haut à droite ».

**Étape 6 — Conclusion.**
$$\boxed{I:\ 237\to74;\quad\sum_j\|y_j-c\|^2=\sum_j\|y_j-\bar y\|^2+m\|\bar y-c\|^2\ \Rightarrow\ I\text{ décroît, arrêt en temps fini}}$$""",
r"""Après une itération : $c_1=(0;0{,}5)$, $c_2=(5{,}25;4{,}75)$, inertie 237 → 74. (A) et (B) font décroître $I$ (König-Huygens) ; un nombre fini de partitions garantit l'arrêt, dans un minimum local.""")
src('Intelligence artificielle : apprentissage')

# ------------------------------------------------------------------ 11. Nim
ex('i-jeu-nim', M, 'Théorie des jeux', 1, 'Jeu de Nim : positions gagnantes', 20, r"""
Deux joueurs retirent à tour de rôle 1, 2 ou 3 allumettes d'un tas de $n$ allumettes. Celui qui prend la dernière allumette gagne.

1. Déterminer à la main, pour $n$ de 0 à 8, si la position est gagnante (le joueur qui doit jouer peut forcer la victoire) ou perdante.
2. Conjecturer puis démontrer : la position $n$ est perdante si et seulement si $n$ est multiple de 4. Donner la stratégie gagnante.
3. Écrire une fonction `gagnante(n, coups=(1, 2, 3))` qui calcule la liste des positions gagnantes de 0 à $n$ par programmation dynamique, pour un ensemble de coups quelconque.
""", r"""Une position est gagnante s'il existe un coup qui mène à une position perdante ; elle est perdante si tous les coups mènent à des positions gagnantes. La position 0 est perdante pour le joueur qui doit jouer.""",
r"""Depuis un multiple de 4, quel que soit le coup $k\in\{1,2,3\}$, on arrive à un non-multiple ; depuis un non-multiple, on peut revenir à un multiple.""",
r"""Remplis la liste `G` de 0 à $n$ : `G[i]` est vrai s'il existe un coup `c <= i` avec `G[i - c]` faux.""",
r"""**Étape 1 — Analyse de l'énoncé.** Jeu à deux joueurs, fini, sans hasard : chaque position est soit gagnante, soit perdante pour le joueur qui doit jouer, et cela se calcule à rebours.

**Étape 2 — Rappels du cours.**

> **Définition — Positions gagnantes et perdantes.** Une position est perdante si tous les coups mènent à une position gagnante (en particulier s'il n'y a aucun coup) ; elle est gagnante s'il existe un coup qui mène à une position perdante.

> **Définition — Stratégie gagnante.** Une règle de choix des coups qui assure la victoire quoi que fasse l'adversaire : jouer vers une position perdante.

**Étape 3 — Stratégie.** Tableau à la main, récurrence forte pour la caractérisation, programme qui reproduit le raisonnement.

**Étape 4 — Résolution détaillée.**

**4.1 Tableau.** 0 : perdante (plus de coup, l'adversaire a pris la dernière). 1, 2, 3 : gagnantes (on prend tout). 4 : tous les coups mènent à 3, 2 ou 1, gagnantes : perdante. 5, 6, 7 : on joue vers 4 : gagnantes. 8 : perdante.

**4.2 Démonstration.** Par récurrence forte sur $n$. Si $n=4q$ avec $q\ge1$ : un coup $k\in\{1,2,3\}$ mène à $4q-k$, qui n'est pas multiple de 4, donc gagnante par hypothèse : $n$ est perdante (et 0 l'est par définition). Si $n=4q+r$ avec $r\in\{1,2,3\}$ : le coup $k=r$ mène à $4q$, perdante, donc $n$ est gagnante. Stratégie : toujours laisser à l'adversaire un multiple de 4, en retirant $n\bmod4$ allumettes.

**4.3 Programme.**

```python
def gagnante(n, coups=(1, 2, 3)):
    G = [False] * (n + 1)
    for i in range(1, n + 1):
        G[i] = any(c <= i and not G[i - c] for c in coups)
    return [i for i in range(n + 1) if G[i]]
```

Complexité $O(n\cdot|\text{coups}|)$.

**Étape 5 — Vérification.**

> **Vérification — Autres coups.** Avec les coups $\{1,3,4\}$, le programme donne les positions perdantes $0, 2, 7, 9, 14, 16,\dots$ : la structure n'est plus « multiples de $k+1$ », d'où l'intérêt du calcul général.

**Étape 6 — Conclusion.**
$$\boxed{n\text{ perdante}\iff4\mid n;\quad\text{stratégie : retirer }n\bmod4\text{ allumettes}}$$""",
r"""Positions perdantes : les multiples de 4 ; stratégie : retirer $n\bmod 4$ allumettes ; calcul général par `G[i] = any(not G[i - c])`.""")
src('Théorie des jeux')

# ------------------------------------------------------------------ 12. Min-max
ex('i-jeu-minmax', M, 'Théorie des jeux', 2, 'Algorithme min-max sur un arbre de jeu', 25, r"""
Un arbre de jeu est représenté par des listes imbriquées : une feuille est un entier (le score de la position pour le joueur Max), un nœud interne est la liste de ses fils. Max joue à la racine, puis les joueurs alternent.

1. Écrire une fonction récursive `minmax(arbre, joueur_max=True)` qui renvoie la valeur de l'arbre.
2. Calculer à la main la valeur de `[[3, 12, 8], [2, 4, 6], [14, 5, 2]]`, et indiquer le coup que doit jouer Max.
3. Dans un vrai jeu, l'arbre est trop grand : on arrête l'exploration à une profondeur $h$ et on évalue les positions avec une heuristique. Combien de positions explore-t-on avec un facteur de branchement $b$ et une profondeur $h$ ? Que devient ce nombre pour $b=30$ et $h=4$ ?
""", r"""À un nœud Max, on prend le maximum des valeurs des fils ; à un nœud Min, le minimum ; une feuille vaut son score.""",
r"""Commence par les trois nœuds Min, au niveau 1.""",
r"""À la profondeur $k$, il y a $b^k$ positions ; additionne de $k=0$ à $h$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Max cherche à maximiser le score, Min à le minimiser ; en supposant les deux joueurs parfaits, la valeur d'une position se calcule récursivement depuis les feuilles.

**Étape 2 — Rappels du cours.**

> **Principe — Min-max.** $\text{val}(\text{feuille})=\text{score}$ ; $\text{val}(\text{nœud Max})=\max$ des valeurs des fils ; $\text{val}(\text{nœud Min})=\min$ des valeurs des fils.

> **Principe — Heuristique.** À profondeur limitée, une fonction d'évaluation estime la valeur d'une position non terminale.

**Étape 3 — Stratégie.** Programme récursif qui alterne le rôle ; calcul à la main niveau par niveau ; dénombrement par série géométrique.

**Étape 4 — Résolution détaillée.**

**4.1 Programme.**

```python
def minmax(arbre, joueur_max=True):
    if isinstance(arbre, int):
        return arbre
    valeurs = [minmax(fils, not joueur_max) for fils in arbre]
    return max(valeurs) if joueur_max else min(valeurs)
```

**4.2 À la main.** Nœuds Min : $\min(3,12,8)=3$, $\min(2,4,6)=2$, $\min(14,5,2)=2$. Racine Max : $\max(3,2,2)=3$. Max joue le premier coup, qui lui garantit 3 quoi que fasse Min.

**4.3 Taille de l'exploration.** $\sum_{k=0}^hb^k=\frac{b^{h+1}-1}{b-1}$ positions. Pour $b=30$, $h=4$ : $1+30+900+27\,000+810\,000=837\,931$ positions, presque toutes au dernier niveau. Chaque niveau supplémentaire multiplie le coût par 30 : c'est ce qui limite la profondeur, et justifie l'élagage alpha-bêta.

**Étape 5 — Vérification.**

> **Vérification — Programme.** `minmax([[3, 12, 8], [2, 4, 6], [14, 5, 2]])` renvoie 3, et `minmax(7)` renvoie 7.

**Étape 6 — Conclusion.**
$$\boxed{\text{valeur }3\ (\text{premier coup});\quad\frac{b^{h+1}-1}{b-1}=837\,931\text{ positions pour }b=30,\ h=4}$$""",
r"""Récursion qui alterne max et min ; valeur 3, premier coup ; $\frac{b^{h+1}-1}{b-1}$ positions, soit 837 931 pour $b=30$, $h=4$.""")
src('Théorie des jeux')

# ------------------------------------------------------------------ 13. Flottants
ex('i-flot', M, 'Nombres flottants', 1, 'Pourquoi 0,1 + 0,2 ≠ 0,3', 15, r"""
1. Expliquer pourquoi `0.1 + 0.2 == 0.3` vaut `False` en Python, alors que `0.5 + 0.25 == 0.75` vaut `True`.
2. Écrire une fonction `proches(x, y, eps=1e-9)` qui teste l'égalité de deux flottants à une tolérance relative près.
3. On calcule la somme $\sum_{k=1}^{n}\frac1k$ avec une boucle `s += 1 / k`, de deux façons : de $k=1$ à $n$, puis de $k=n$ à $1$. Pour $n=10^6$, les résultats diffèrent dans les derniers chiffres. Expliquer quelle somme est la plus précise.
""", r"""Un flottant stocke un nombre sous la forme $m\times2^e$ avec une mantisse de 53 bits : quels réels sont représentables exactement ?""",
r"""$\frac1{10}$ s'écrit en base 2 avec un développement infini et périodique.""",
r"""Ajouter un tout petit nombre à un grand nombre fait perdre les derniers chiffres du petit.""",
r"""**Étape 1 — Analyse de l'énoncé.** Les flottants sont des nombres dyadiques arrondis : on explique les erreurs de représentation, on en déduit la bonne façon de comparer, puis on étudie l'accumulation des arrondis.

**Étape 2 — Rappels du cours.**

> **Définition — Flottants (double précision).** Un flottant normalisé vaut $\pm m\times2^e$ avec une mantisse de 53 bits significatifs ; l'erreur relative d'arrondi est au plus $2^{-53}\approx1{,}1\times10^{-16}$.

> **Propriété — Nombres représentables.** Seuls les rationnels de la forme $\frac p{2^k}$ (et pas trop grands) sont représentés exactement.

**Étape 3 — Stratégie.** Écriture en base 2 ; test avec tolérance ; analyse de l'ordre de sommation.

**Étape 4 — Résolution détaillée.**

**4.1 Représentation.** $0{,}5=2^{-1}$, $0{,}25=2^{-2}$, $0{,}75=2^{-1}+2^{-2}$ : tous exacts, la somme est exacte. En revanche $\frac1{10}=0{,}0001100110011\ldots_2$ a un développement binaire infini : `0.1`, `0.2` et `0.3` sont des arrondis, et l'arrondi de la somme des deux premiers (`0.30000000000000004`) n'est pas le flottant le plus proche de 0,3.

**4.2 Comparaison.**

```python
def proches(x, y, eps=1e-9):
    return abs(x - y) <= eps * max(abs(x), abs(y), 1.0)
```

La tolérance est relative pour les grands nombres, et absolue (`eps`) autour de 0, où une tolérance purement relative serait trop exigeante. Le module `math` propose `math.isclose`.

**4.3 Ordre de sommation.** Chaque addition $s+t$ est arrondie avec une erreur de l'ordre de $2^{-53}|s+t|$. De 1 à $n$ : la somme partielle atteint vite 14 environ, et l'on y ajoute des termes de l'ordre de $10^{-6}$ ; chaque addition perd les derniers chiffres du petit terme. De $n$ à 1 : on additionne d'abord les petits termes entre eux, la somme partielle reste longtemps petite et les arrondis sont plus petits en valeur absolue. La somme de $n$ à 1, par ordre croissant des termes, est la plus précise.

**Étape 5 — Vérification.**

> **Vérification — En pratique.** Pour $n=10^6$, les deux boucles diffèrent d'environ $8\times10^{-13}$. Comparées à `math.fsum` (qui somme sans perte, $\approx14{,}392\,726\,722\,865\,72$), l'erreur de la boucle croissante est d'environ $7\times10^{-13}$, celle de la boucle décroissante d'environ $5\times10^{-14}$. Remarque : depuis Python 3.12, la fonction `sum` compense elle-même les erreurs d'arrondi ; l'expérience se fait donc avec une boucle.

**Étape 6 — Conclusion.**
$$\boxed{0{,}1\text{ n'est pas dyadique};\ \text{comparer avec une tolérance};\ \text{sommer les petits termes d'abord}}$$""",
r"""0,1 a un développement binaire infini, donc il est arrondi ; comparer avec `abs(x - y) <= eps * max(|x|, |y|, 1)` ; sommer par termes croissants (de $n$ à 1) est plus précis.""")
src('Divers : les nombres flottants')
