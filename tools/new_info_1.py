# Informatique commune MP — exercices originaux sur les chapitres du cours de D. Rupprecht
# (lycée Pierre-de-Fermat) : Python, complexité et preuves, piles et récursivité, tris.
# Tout le code des corrigés est exécuté et testé par tools/test_info.py.
from newlib import ex, E

def src(chapitre):
    E[-1]['enonce'] += f"\n\n*Exercice original sur le chapitre « {chapitre} » du cours d'informatique MP de D. Rupprecht (lycée Pierre-de-Fermat).*"
    E[-1]['ajout'] = '2026-11-25'

M = 'Informatique'

# ------------------------------------------------------------------ 1. Deux plus grands
ex('i-py-max2', M, 'Python : listes et fichiers', 1, 'Les deux plus grands en un seul passage', 15, r"""
Soit `L` une liste d'entiers de longueur $n\ge2$.

1. Écrire une fonction `deux_plus_grands(L)` qui renvoie le couple `(a, b)` formé du plus grand élément `a` et du deuxième plus grand `b` (avec $b=a$ si le maximum apparaît au moins deux fois), en **un seul parcours** de la liste, sans la trier ni la modifier.
2. Combien de comparaisons entre éléments la fonction effectue-t-elle dans le pire cas ?
3. Pourquoi `sorted(L)[-2:]` donne-t-il le même résultat mais n'est-il pas optimal ?
""", r"""Garde deux variables `a` (le plus grand vu) et `b` (le deuxième), initialisées avec les deux premiers éléments.""",
r"""Pour chaque nouvel élément `x` : s'il dépasse `a`, l'ancien `a` devient `b` ; sinon, s'il dépasse `b`, il remplace `b`.""",
r"""Au pire, chaque élément est comparé à `a` puis à `b` : compte les comparaisons du premier couple à part.""",
r"""**Étape 1 — Analyse de l'énoncé.** On cherche les deux plus grandes valeurs, doublons compris : pour `[5, 5, 1]` la réponse est `(5, 5)`. La contrainte est un seul parcours, donc une complexité linéaire.

**Étape 2 — Rappels du cours.**

> **Définition — Complexité.** On compte les opérations élémentaires significatives (ici les comparaisons entre éléments) en fonction de la taille $n$ de l'entrée, dans le pire cas.

> **Propriété — Tri.** Les tris par comparaison efficaces (tri fusion, `sorted` de Python) coûtent $O(n\log n)$.

**Étape 3 — Stratégie.** On maintient l'invariant : après avoir lu les $k$ premiers éléments, `a` est le plus grand d'entre eux et `b` le deuxième plus grand.

**Étape 4 — Résolution détaillée.**

**4.1 Programme.**

```python
def deux_plus_grands(L):
    a, b = L[0], L[1]
    if b > a:
        a, b = b, a
    for x in L[2:]:
        if x > a:
            a, b = x, a
        elif x > b:
            b = x
    return (a, b)
```

**4.2 Invariant.** Il est vrai après les deux premiers éléments. Si `x > a`, le nouveau maximum est `x` et l'ancien maximum devient le deuxième ; sinon le maximum ne change pas et le deuxième devient `max(b, x)`. L'invariant est conservé, et en fin de boucle il porte sur toute la liste.

**4.3 Comparaisons.** Une comparaison pour le premier couple, puis au plus deux par élément restant : au plus $1+2(n-2)=2n-3$ comparaisons, atteint quand les éléments sont rangés par ordre décroissant (chaque `x` échoue au premier test puis passe le second).

**4.4 Le tri.** `sorted(L)[-2:]` renvoie bien les deux plus grands, mais coûte $O(n\log n)$ comparaisons et crée une copie de la liste : c'est asymptotiquement plus lent qu'un passage linéaire.

**Étape 5 — Vérification.**

> **Vérification — Cas limites.** `[3, 7]` donne `(7, 3)` ; `[5, 5, 1]` donne `(5, 5)` ; `[1, 2, 3, 4]` donne `(4, 3)` ; `[4, 3, 2, 1]` donne `(4, 3)`.

**Étape 6 — Conclusion.**
$$\boxed{\text{un parcours, au plus }2n-3\text{ comparaisons, contre }O(n\log n)\text{ pour un tri}}$$""",
r"""Parcours unique avec deux variables `a` ≥ `b` ; au plus $2n-3$ comparaisons ; le tri coûte $O(n\log n)$.""")
src('Rappels de base sur Python')

# ------------------------------------------------------------------ 2. Fichier csv
ex('i-py-csv', M, 'Python : listes et fichiers', 1, 'Moyennes par ville dans un fichier de mesures', 20, r"""
Un fichier texte `mesures.csv` contient une ligne d'en-tête `ville;temperature`, puis une mesure par ligne, par exemple `Toulouse;14.5`. Une même ville apparaît plusieurs fois.

1. Écrire une fonction `lire(nom)` qui renvoie la liste des couples `(ville, temperature)`, la température étant un flottant.
2. Écrire une fonction `moyennes(mesures)` qui renvoie un dictionnaire associant à chaque ville la moyenne de ses températures.
3. Quelle est la complexité de `moyennes` en fonction du nombre $n$ de mesures, en admettant que les opérations sur un dictionnaire coûtent $O(1)$ en moyenne ?
""", r"""Ouvre le fichier avec `with open(nom) as f`, saute la première ligne, puis découpe chaque ligne avec `split(';')`.""",
r"""Pense à `strip()` pour retirer le retour à la ligne, et à ignorer une ligne vide en fin de fichier.""",
r"""Accumule d'abord, pour chaque ville, la somme et le nombre de mesures dans deux dictionnaires, puis divise.""",
r"""**Étape 1 — Analyse de l'énoncé.** On lit un fichier texte ligne par ligne, on convertit les champs, puis on regroupe les mesures par clé (la ville).

**Étape 2 — Rappels du cours.**

> **Rappel — Fichiers.** `with open(nom, 'r') as f` ouvre le fichier et garantit sa fermeture ; `f.readline()` lit une ligne, et `for ligne in f` parcourt les suivantes. Chaque ligne se termine par `\n`.

> **Rappel — Dictionnaires.** `d.get(k, 0)` renvoie `d[k]` si la clé existe, `0` sinon ; insertion et accès coûtent $O(1)$ en moyenne.

**Étape 3 — Stratégie.** Une passe pour lire, une passe pour cumuler sommes et effectifs par ville, une dernière sur les villes pour diviser.

**Étape 4 — Résolution détaillée.**

**4.1 Lecture.**

```python
def lire(nom):
    mesures = []
    with open(nom, 'r', encoding='utf-8') as f:
        f.readline()                      # en-tête
        for ligne in f:
            ligne = ligne.strip()
            if ligne:                     # ignore une ligne vide
                ville, t = ligne.split(';')
                mesures.append((ville, float(t)))
    return mesures
```

**4.2 Moyennes.**

```python
def moyennes(mesures):
    somme, nb = {}, {}
    for ville, t in mesures:
        somme[ville] = somme.get(ville, 0) + t
        nb[ville] = nb.get(ville, 0) + 1
    return {v: somme[v] / nb[v] for v in somme}
```

**4.3 Complexité.** La boucle fait $n$ itérations à coût $O(1)$ en moyenne ; la construction finale parcourt au plus $n$ villes. Total : $O(n)$ en moyenne.

**Étape 5 — Vérification.**

> **Vérification — Exemple.** Avec les mesures `Toulouse;14.5`, `Lille;8`, `Toulouse;15.5`, on obtient `{'Toulouse': 15.0, 'Lille': 8.0}`.

**Étape 6 — Conclusion.**
$$\boxed{\text{lecture ligne à ligne, cumul somme / effectif par clé, complexité }O(n)}$$""",
r"""`lire` saute l'en-tête et découpe avec `split(';')` ; `moyennes` cumule somme et effectif par ville dans deux dictionnaires : $O(n)$ en moyenne.""")
src('Rappels de base sur Python (fichiers csv)')

# ------------------------------------------------------------------ 3. Dichotomie
ex('i-cx-dicho', M, 'Complexité et preuves', 1, 'Recherche dichotomique : terminaison et coût', 20, r"""
On considère la fonction suivante, où `L` est une liste triée par ordre croissant.

```python
def dicho(L, x):
    g, d = 0, len(L) - 1
    while g <= d:
        m = (g + d) // 2
        if L[m] == x:
            return m
        elif L[m] < x:
            g = m + 1
        else:
            d = m - 1
    return -1
```

1. Montrer que la boucle termine, à l'aide d'un variant.
2. Énoncer un invariant qui prouve la correction : si `x` est dans `L`, sa position est entre `g` et `d`.
3. Montrer que le nombre de passages dans la boucle est au plus $\lfloor\log_2 n\rfloor+1$ pour une liste de longueur $n\ge1$.
""", r"""Prends comme variant la longueur de l'intervalle de recherche, $d-g+1$.""",
r"""Si `L[m] < x`, comme la liste est triée, tous les indices $\le m$ portent des valeurs $<x$.""",
r"""Montre que la longueur $\ell=d-g+1$ devient au plus $\lfloor\ell/2\rfloor$ après un passage.""",
r"""**Étape 1 — Analyse de l'énoncé.** Trois propriétés distinctes : la boucle s'arrête (terminaison), le résultat est juste (correction), et l'on borne le nombre d'itérations (complexité).

**Étape 2 — Rappels du cours.**

> **Définition — Variant.** Une quantité entière, positive tant que la boucle s'exécute, qui décroît strictement à chaque itération : elle garantit la terminaison.

> **Définition — Invariant.** Une propriété vraie avant la boucle et conservée par chaque itération ; combinée à la condition d'arrêt, elle donne la correction.

**Étape 3 — Stratégie.** Variant $\ell=d-g+1$ ; invariant sur la zone où `x` peut encore se trouver ; puis étude de la décroissance de $\ell$.

**Étape 4 — Résolution détaillée.**

**4.1 Terminaison.** Tant que $g\le d$, $\ell\ge1$. Comme $g\le m\le d$, la mise à jour `g = m + 1` ou `d = m - 1` fait perdre au moins un élément à l'intervalle : $\ell$ décroît strictement. Un entier positif ne peut décroître indéfiniment, donc la boucle termine (ou bien la fonction renvoie avant).

**4.2 Invariant.** « Si `x` est dans `L`, alors il est présent à un indice de $[g,d]$. » Vrai au départ ($[0,n-1]$). Si `L[m] < x`, la liste étant triée, `L[i] < x` pour tout $i\le m$ : on peut écarter $[g,m]$. Symétriquement si `L[m] > x`. En sortie de boucle, $g>d$ : l'intervalle est vide, donc `x` n'est pas dans `L` et renvoyer `-1` est correct. Si l'on renvoie `m`, c'est que `L[m] == x`.

**4.3 Nombre d'itérations.** Soit $\ell=d-g+1$ et $m=\lfloor(g+d)/2\rfloor$. Les deux nouveaux intervalles ont pour longueurs $m-g$ et $d-m$, toutes deux $\le\lfloor\ell/2\rfloor$. Après $k$ itérations, $\ell_k\le n/2^k$. La boucle s'exécute encore tant que $\ell_k\ge1$, ce qui impose $2^k\le n$, soit $k\le\log_2n$. Au plus $\lfloor\log_2n\rfloor+1$ passages.

**Étape 5 — Vérification.**

> **Vérification — Cas extrême.** Pour $n=8$ et un élément absent plus grand que tous, les longueurs successives sont $8,4,2,1$ puis $0$ : 4 passages, et $\lfloor\log_28\rfloor+1=4$.

**Étape 6 — Conclusion.**
$$\boxed{\text{variant }d-g+1,\quad\text{invariant : }x\in L\Rightarrow x\in L[g..d],\quad\text{au plus }\lfloor\log_2n\rfloor+1\text{ itérations}}$$""",
r"""Variant $d-g+1$ (strictement décroissant) ; invariant « `x` présent ⇒ dans `L[g..d]` » ; la longueur est au moins divisée par 2 : au plus $\lfloor\log_2 n\rfloor+1$ itérations, soit $O(\log n)$.""")
src('Algorithmes, complexité et preuves')

# ------------------------------------------------------------------ 4. Exponentiation rapide
ex('i-cx-expo', M, 'Complexité et preuves', 2, 'Exponentiation rapide itérative : invariant', 25, r"""
On considère la fonction suivante, pour $a$ réel et $n$ entier naturel.

```python
def puissance(a, n):
    r, b, k = 1, a, n
    while k > 0:
        if k % 2 == 1:
            r = r * b
        b = b * b
        k = k // 2
    return r
```

1. Montrer que $r\cdot b^k=a^n$ est un invariant de boucle. En déduire que la fonction renvoie $a^n$.
2. Exprimer le nombre de passages dans la boucle en fonction de $n\ge1$, puis le nombre de multiplications dans le pire cas.
3. Comparer avec l'algorithme naïf qui multiplie $n$ fois par $a$. Combien de multiplications pour $n=1000$ dans les deux cas ?
""", r"""Distingue les cas $k$ pair et $k$ impair : $k=2q$ ou $k=2q+1$, et regarde ce que deviennent $r$, $b$, $k$.""",
r"""Le nombre de passages est le nombre de chiffres de $n$ en base 2.""",
r"""Au pire, chaque passage fait deux multiplications : quand tous les bits de $n$ valent 1.""",
r"""**Étape 1 — Analyse de l'énoncé.** L'algorithme lit les bits de $n$ du poids faible au poids fort ; on prouve sa correction par un invariant, puis on compte ses opérations.

**Étape 2 — Rappels du cours.**

> **Définition — Invariant de boucle.** Propriété vraie avant la boucle et préservée par chaque itération ; à la sortie, elle se combine avec la négation de la condition de boucle.

> **Propriété — Écriture binaire.** Un entier $n\ge1$ s'écrit avec $\lfloor\log_2n\rfloor+1$ chiffres en base 2.

**Étape 3 — Stratégie.** Vérifier l'invariant au départ, sa conservation selon la parité de $k$, puis conclure avec $k=0$.

**Étape 4 — Résolution détaillée.**

**4.1 Invariant.** Au départ, $r\,b^k=1\cdot a^n$. Si $k=2q$ : les nouvelles valeurs sont $r'=r$, $b'=b^2$, $k'=q$, et $r'b'^{k'}=r\,b^{2q}=r\,b^k$. Si $k=2q+1$ : $r'=rb$, $b'=b^2$, $k'=q$, et $r'b'^{k'}=rb\cdot b^{2q}=r\,b^k$. L'invariant est conservé. La boucle termine car $k$ est un entier positif qui décroît strictement ($\lfloor k/2\rfloor<k$ pour $k\ge1$). À la sortie, $k=0$, donc $r=a^n$.

**4.2 Comptage.** $k$ prend les valeurs $n,\lfloor n/2\rfloor,\lfloor n/4\rfloor,\dots$ : il y a autant de passages que de chiffres binaires de $n$, soit $p=\lfloor\log_2n\rfloor+1$. Chaque passage fait une multiplication `b * b`, plus une `r * b` quand le bit courant vaut 1. Au pire (tous les bits à 1, $n=2^p-1$) : $2p$ multiplications, donc $O(\log n)$.

**4.3 Comparaison.** L'algorithme naïf fait $n$ multiplications (ou $n-1$ en partant de $a$). Pour $n=1000=1111101000_2$ : 10 chiffres dont 6 à 1, donc $10+6=16$ multiplications, contre environ $1000$.

**Étape 5 — Vérification.**

> **Vérification — Exécution.** `puissance(3, 13)` : $13=1101_2$. Les couples $(r,b,k)$ valent $(1,3,13)\to(3,9,6)\to(3,81,3)\to(243,6561,1)\to(1594323,\dots,0)$, et $3^{13}=1594323$.

**Étape 6 — Conclusion.**
$$\boxed{r\,b^k=a^n\ \text{invariant};\quad \lfloor\log_2n\rfloor+1\ \text{passages};\quad \text{au plus }2(\lfloor\log_2n\rfloor+1)\text{ multiplications}}$$""",
r"""Invariant $r\,b^k=a^n$ (cas pair / impair), sortie avec $k=0$ ; $\lfloor\log_2 n\rfloor+1$ passages, au plus le double de multiplications ; pour $n=1000$ : 16 contre environ 1000.""")
src('Algorithmes, complexité et preuves')

# ------------------------------------------------------------------ 5. Recherche de motif
ex('i-cx-motif', M, 'Complexité et preuves', 1, 'Recherche naïve d’un mot dans un texte', 15, r"""
On cherche si un mot `m` de longueur $p$ apparaît dans un texte `t` de longueur $n\ge p$.

1. Écrire une fonction `occurrences(t, m)` qui renvoie la liste des positions $i$ telles que `t[i:i+p] == m`, en comparant caractère par caractère (sans utiliser le découpage `t[i:i+p]`).
2. Montrer que le nombre de comparaisons de caractères est au plus $(n-p+1)p$.
3. Donner un exemple de texte et de mot pour lesquels cette borne est atteinte.
""", r"""Pour chaque position de départ $i$ de $0$ à $n-p$, compare `t[i+j]` et `m[j]` pour $j$ croissant, et arrête-toi à la première différence.""",
r"""Il y a $n-p+1$ positions de départ, et au plus $p$ comparaisons pour chacune.""",
r"""Pour atteindre la borne, il faut que chaque essai aille jusqu'au bout : pense à un texte et un mot formés presque uniquement de la même lettre.""",
r"""**Étape 1 — Analyse de l'énoncé.** Algorithme à deux boucles imbriquées : la boucle externe choisit la position de départ, la boucle interne compare. On veut un majorant puis un cas qui l'atteint.

**Étape 2 — Rappels du cours.**

> **Définition — Complexité dans le pire cas.** Le maximum, sur toutes les entrées de taille donnée, du nombre d'opérations effectuées.

**Étape 3 — Stratégie.** Compter les comparaisons par position de départ, puis chercher une entrée où aucune comparaison n'échoue avant la dernière.

**Étape 4 — Résolution détaillée.**

**4.1 Programme.**

```python
def occurrences(t, m):
    n, p = len(t), len(m)
    pos = []
    for i in range(n - p + 1):
        j = 0
        while j < p and t[i + j] == m[j]:
            j += 1
        if j == p:
            pos.append(i)
    return pos
```

**4.2 Majorant.** La boucle externe fait $n-p+1$ tours ; à chaque tour, la boucle `while` fait au plus $p$ comparaisons `t[i + j] == m[j]`. Total : au plus $(n-p+1)p$, donc $O(np)$.

**4.3 Cas extrême.** Avec `t = 'a' * n` et `m = 'a' * p`, chaque position est une occurrence : chaque essai fait exactement $p$ comparaisons, et la borne $(n-p+1)p$ est atteinte. On l'atteint aussi avec `m = 'a' * (p - 1) + 'b'` : chaque essai échoue seulement sur le dernier caractère.

**Étape 5 — Vérification.**

> **Vérification — Exemple.** `occurrences('abracadabra', 'abra')` renvoie `[0, 7]`.

**Étape 6 — Conclusion.**
$$\boxed{\text{au plus }(n-p+1)\,p\text{ comparaisons, atteint pour }t=a^n,\ m=a^p}$$""",
r"""Deux boucles imbriquées : au plus $(n-p+1)p$ comparaisons, atteint pour `t = 'a'*n`, `m = 'a'*p` (ou `'a'*(p-1)+'b'`).""")
src('Algorithmes, complexité et preuves')

# ------------------------------------------------------------------ 6. Parenthésage
ex('i-pile-par', M, 'Piles, files et récursivité', 1, 'Parenthésage bien formé avec une pile', 15, r"""
Une chaîne ne contenant que les caractères `(`, `)`, `[`, `]` est *bien formée* si chaque ouvrante est fermée par la fermante de même type, dans le bon ordre : `([])[]` est bien formée, `([)]` et `(()` ne le sont pas.

1. Écrire une fonction `bien_formee(s)` qui utilise une pile (une liste Python avec `append` et `pop`).
2. Justifier sa complexité.
3. Si l'on n'a qu'un seul type de parenthèses, montrer qu'un simple compteur suffit, et dire pourquoi ce n'est plus vrai avec deux types.
""", r"""Empile chaque ouvrante ; à chaque fermante, le sommet de la pile doit être l'ouvrante correspondante.""",
r"""Trois cas d'échec : une fermante quand la pile est vide, un sommet du mauvais type, une pile non vide à la fin.""",
r"""Pour un seul type, le compteur est la hauteur de la pile ; avec deux types, `([)]` a des compteurs corrects mais n'est pas bien formée.""",
r"""**Étape 1 — Analyse de l'énoncé.** La dernière parenthèse ouverte est la première à fermer : c'est exactement le comportement d'une pile (dernier entré, premier sorti).

**Étape 2 — Rappels du cours.**

> **Définition — Pile.** Structure où l'on ajoute (`empiler`) et retire (`dépiler`) au même bout, en $O(1)$. En Python : `append` et `pop` sur une liste.

**Étape 3 — Stratégie.** On parcourt la chaîne une fois : empiler les ouvrantes, et à chaque fermante vérifier puis dépiler.

**Étape 4 — Résolution détaillée.**

**4.1 Programme.**

```python
def bien_formee(s):
    paire = {')': '(', ']': '['}
    pile = []
    for c in s:
        if c in '([':
            pile.append(c)
        else:
            if not pile or pile.pop() != paire[c]:
                return False
    return pile == []
```

**4.2 Complexité.** Un passage sur la chaîne de longueur $n$, avec des opérations en $O(1)$ (accès au dictionnaire, `append`, `pop`) : $O(n)$ en temps, $O(n)$ en mémoire au pire (chaîne d'ouvrantes).

**4.3 Un seul type.** La pile ne contient alors que des `(` : seule sa hauteur compte. Le compteur `h` (+1 pour `(`, −1 pour `)`) doit rester $\ge0$ et finir à $0$. Avec deux types, l'ordre compte : pour `([)]`, les compteurs de `(` et de `[` restent positifs et finissent à 0, pourtant `)` ferme un `[`. Il faut mémoriser la suite des ouvrantes, donc une pile.

**Étape 5 — Vérification.**

> **Vérification — Exemples.** `bien_formee('([])[]')` vaut `True` ; `'([)]'`, `'(()'` et `'())'` donnent `False` ; la chaîne vide donne `True`.

**Étape 6 — Conclusion.**
$$\boxed{\text{pile des ouvrantes : }O(n);\ \text{un compteur ne suffit qu'avec un seul type}}$$""",
r"""Empiler les ouvrantes, vérifier et dépiler à chaque fermante, pile vide à la fin : $O(n)$. Un compteur suffit pour un seul type, pas pour deux (`([)]`).""")
src('Piles et récursivité')

# ------------------------------------------------------------------ 7. Postfixe
ex('i-pile-rpn', M, 'Piles, files et récursivité', 2, 'Évaluer une expression en notation postfixée', 20, r"""
En notation postfixée (polonaise inverse), l'opérateur suit ses opérandes : `3 4 + 2 *` vaut $(3+4)\times2=14$. On représente une expression par une liste de chaînes, par exemple `['3', '4', '+', '2', '*']`, avec les opérateurs `+`, `-`, `*`.

1. Écrire une fonction `evaluer(expr)` qui calcule la valeur d'une expression postfixée bien formée à l'aide d'une pile.
2. Traduire en notation postfixée l'expression $(5-1)\times(2+3)-4$, puis l'évaluer.
3. Montrer qu'une liste de longueur $n$ est une expression bien formée seulement si $n$ est impair. Que vaut la hauteur maximale de la pile pour `['1', '2', '3', ..., 'k', '+', '+', ..., '+']` ($k$ nombres puis $k-1$ opérateurs) ?
""", r"""Un nombre est empilé ; un opérateur dépile deux valeurs, calcule, et empile le résultat.""",
r"""Attention à l'ordre pour la soustraction : le premier dépilé est l'opérande de droite.""",
r"""Chaque nombre fait monter la pile de 1, chaque opérateur la fait baisser de 1, et il doit rester exactement une valeur.""",
r"""**Étape 1 — Analyse de l'énoncé.** La notation postfixée se lit de gauche à droite sans parenthèses ni priorités : quand un opérateur arrive, ses deux opérandes sont les deux derniers résultats calculés, au sommet d'une pile.

**Étape 2 — Rappels du cours.**

> **Définition — Pile.** Dernier entré, premier sorti ; `append` et `pop` en $O(1)$.

**Étape 3 — Stratégie.** Parcours unique ; on suit l'évolution de la hauteur de la pile pour la question 3.

**Étape 4 — Résolution détaillée.**

**4.1 Programme.**

```python
def evaluer(expr):
    pile = []
    for jeton in expr:
        if jeton in ('+', '-', '*'):
            droite = pile.pop()
            gauche = pile.pop()
            if jeton == '+':
                pile.append(gauche + droite)
            elif jeton == '-':
                pile.append(gauche - droite)
            else:
                pile.append(gauche * droite)
        else:
            pile.append(int(jeton))
    return pile.pop()
```

**4.2 Traduction.** $(5-1)\times(2+3)-4$ devient `5 1 - 2 3 + * 4 -`. Évaluation : $5-1=4$, $2+3=5$, $4\times5=20$, $20-4=16$.

**4.3 Parité.** Soit $a$ le nombre de nombres et $o$ le nombre d'opérateurs. Chaque nombre augmente la hauteur de 1, chaque opérateur la diminue de 1 (deux dépilés, un empilé). À la fin il reste une valeur : $a-o=1$, donc $n=a+o=2o+1$ est impair. Pour $k$ nombres puis $k-1$ additions, la pile monte jusqu'à $k$ : la hauteur peut être de l'ordre de $n/2$.

**Étape 5 — Vérification.**

> **Vérification — Ordre.** `evaluer(['5', '1', '-'])` vaut 4 et non −4 : le premier dépilé (1) est bien l'opérande de droite.

**Étape 6 — Conclusion.**
$$\boxed{(5-1)\times(2+3)-4\ \to\ \texttt{5 1 - 2 3 + * 4 -}=16;\qquad n=2o+1\text{ impair}}$$""",
r"""Pile : un nombre est empilé, un opérateur dépile droite puis gauche. `5 1 - 2 3 + * 4 -` vaut 16. Nombres − opérateurs = 1, donc la longueur est impaire ; la pile peut monter jusqu'à $(n+1)/2$.""")
src('Piles et récursivité')

# ------------------------------------------------------------------ 8. Fibonacci : nombre d'appels
ex('i-rec-fibo', M, 'Piles, files et récursivité', 2, 'Fibonacci récursif : compter les appels', 20, r"""
On définit $F_0=0$, $F_1=1$, $F_{n+2}=F_{n+1}+F_n$, et la fonction :

```python
def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)
```

1. Soit $A(n)$ le nombre total d'appels à `fibo` (appel initial compris) lors du calcul de `fibo(n)`. Établir une relation de récurrence sur $A(n)$.
2. Montrer que $A(n)=2F_{n+1}-1$. En déduire que la complexité est exponentielle.
3. Écrire une version itérative en $O(n)$, puis une version récursive mémoïsée avec un dictionnaire.
""", r"""L'appel `fibo(n)` pour $n\ge2$ compte pour 1, plus les appels de `fibo(n-1)` et de `fibo(n-2)`.""",
r"""Pose $B(n)=A(n)+1$ : la récurrence devient celle de Fibonacci.""",
r"""Pour l'exponentielle, utilise $F_n\sim\varphi^n/\sqrt5$ avec $\varphi=\frac{1+\sqrt5}2$.""",
r"""**Étape 1 — Analyse de l'énoncé.** La version naïve recalcule plusieurs fois les mêmes valeurs ; on mesure ce gaspillage par le nombre d'appels, puis on l'évite.

**Étape 2 — Rappels du cours.**

> **Définition — Récursivité.** Une fonction qui s'appelle elle-même, avec un cas de base qui arrête les appels.

> **Propriété — Suite de Fibonacci.** $F_n=\frac{\varphi^n-\psi^n}{\sqrt5}$ avec $\varphi=\frac{1+\sqrt5}2$, $\psi=\frac{1-\sqrt5}2$, donc $F_n\sim\frac{\varphi^n}{\sqrt5}$.

**Étape 3 — Stratégie.** Récurrence sur $A$, changement $B=A+1$, puis deux versions qui ne calculent chaque $F_k$ qu'une fois.

**Étape 4 — Résolution détaillée.**

**4.1 Récurrence.** $A(0)=A(1)=1$ et, pour $n\ge2$, $A(n)=1+A(n-1)+A(n-2)$.

**4.2 Formule.** Avec $B(n)=A(n)+1$ : $B(0)=B(1)=2$ et $B(n)=B(n-1)+B(n-2)$. Comme $2F_1=2$ et $2F_2=2$, une récurrence double donne $B(n)=2F_{n+1}$, d'où $A(n)=2F_{n+1}-1\sim\frac{2\varphi^{n+1}}{\sqrt5}$ : la complexité est en $\Theta(\varphi^n)$, exponentielle ($\varphi\approx1{,}618$). Pour $n=30$, $A(30)=2F_{31}-1=2\,692\,537$ appels.

**4.3 Versions efficaces.**

```python
def fibo_iter(n):
    a, b = 0, 1           # a = F_k, b = F_{k+1}
    for _ in range(n):
        a, b = b, a + b
    return a

def fibo_memo(n, memo=None):
    if memo is None:
        memo = {0: 0, 1: 1}
    if n not in memo:
        memo[n] = fibo_memo(n - 1, memo) + fibo_memo(n - 2, memo)
    return memo[n]
```

La version itérative fait $n$ tours en $O(1)$ chacun. La version mémoïsée calcule chaque $F_k$ une seule fois : $O(n)$ appels.

**Étape 5 — Vérification.**

> **Vérification — Petites valeurs.** $A(2)=3$ (appels sur 2, 1, 0) et $2F_3-1=3$ ; $A(4)=9$ et $2F_5-1=9$.

**Étape 6 — Conclusion.**
$$\boxed{A(n)=2F_{n+1}-1=\Theta(\varphi^n)\quad\text{contre }O(n)\text{ en itératif ou mémoïsé}}$$""",
r"""$A(n)=1+A(n-1)+A(n-2)$, donc $A(n)+1=2F_{n+1}$ et $A(n)=2F_{n+1}-1=\Theta(\varphi^n)$ ; versions itérative et mémoïsée en $O(n)$.""")
src('Piles et récursivité')

# ------------------------------------------------------------------ 9. Hanoï
ex('i-rec-hanoi', M, 'Piles, files et récursivité', 1, 'Les tours de Hanoï', 15, r"""
On doit déplacer $n$ disques de tailles toutes différentes, empilés du plus grand au plus petit sur le piquet 1, vers le piquet 3, en s'aidant du piquet 2. On déplace un seul disque à la fois et on ne pose jamais un disque sur un plus petit.

1. Écrire une fonction récursive `hanoi(n, dep, arr, aux)` qui renvoie la liste des déplacements, chacun étant un couple `(depart, arrivee)`.
2. Soit $u_n$ le nombre de déplacements produits. Établir une relation entre $u_n$ et $u_{n-1}$, puis montrer que $u_n=2^n-1$.
3. Montrer qu'on ne peut pas faire mieux.
""", r"""Pour déplacer $n$ disques, déplace d'abord les $n-1$ du dessus vers le piquet auxiliaire.""",
r"""Puis déplace le plus grand disque, et ramène les $n-1$ disques sur lui.""",
r"""Pour l'optimalité : le plus grand disque ne peut bouger que lorsque les $n-1$ autres sont tous sur un même autre piquet.""",
r"""**Étape 1 — Analyse de l'énoncé.** Le problème à $n$ disques se ramène à deux problèmes à $n-1$ disques et un déplacement : c'est un schéma récursif.

**Étape 2 — Rappels du cours.**

> **Définition — Récursivité.** Un problème est résolu à partir de la solution de sous-problèmes plus petits, avec un cas de base (ici $n=0$ : rien à faire).

> **Propriété — Suite arithmético-géométrique.** Si $u_n=2u_{n-1}+1$, alors $u_n+1=2(u_{n-1}+1)$.

**Étape 3 — Stratégie.** Écrire la récursion, en déduire la récurrence, puis prouver la minoration par le même argument.

**Étape 4 — Résolution détaillée.**

**4.1 Programme.**

```python
def hanoi(n, dep=1, arr=3, aux=2):
    if n == 0:
        return []
    return hanoi(n - 1, dep, aux, arr) + [(dep, arr)] + hanoi(n - 1, aux, arr, dep)
```

**4.2 Nombre de déplacements.** $u_0=0$ et $u_n=2u_{n-1}+1$. Donc $u_n+1=2(u_{n-1}+1)=\dots=2^n(u_0+1)=2^n$, soit $u_n=2^n-1$.

**4.3 Optimalité.** Soit $v_n$ le nombre minimal de déplacements. Pour déplacer le plus grand disque, les $n-1$ autres doivent être empilés sur le troisième piquet : cela demande au moins $v_{n-1}$ coups. Le plus grand bouge au moins une fois. Ensuite, pour que les $n-1$ disques le rejoignent, il faut encore au moins $v_{n-1}$ coups. Donc $v_n\ge2v_{n-1}+1$, et par récurrence $v_n\ge2^n-1$ : l'algorithme est optimal.

**Étape 5 — Vérification.**

> **Vérification — n = 2.** `hanoi(2)` renvoie `[(1, 2), (1, 3), (2, 3)]`, soit $3=2^2-1$ déplacements.

**Étape 6 — Conclusion.**
$$\boxed{u_n=2u_{n-1}+1,\ u_n=2^n-1,\ \text{et c'est le minimum possible}}$$""",
r"""$u_n=2u_{n-1}+1$, $u_0=0$, donc $u_n=2^n-1$ ; optimal car le plus grand disque impose deux déplacements complets des $n-1$ autres.""")
src('Piles et récursivité')

# ------------------------------------------------------------------ 10. Tri par insertion
ex('i-tri-ins', M, 'Tris', 1, 'Tri par insertion : invariant et comparaisons', 20, r"""
On considère le tri par insertion d'une liste `L` de longueur $n$.

```python
def tri_insertion(L):
    for i in range(1, len(L)):
        x = L[i]
        j = i
        while j > 0 and L[j - 1] > x:
            L[j] = L[j - 1]
            j -= 1
        L[j] = x
```

1. Énoncer un invariant de la boucle `for` qui prouve que la liste est triée à la fin.
2. Compter le nombre de comparaisons `L[j - 1] > x` dans le meilleur et dans le pire cas, en précisant les listes correspondantes.
3. Le tri est-il stable ? Pourquoi est-il intéressant pour une liste « presque triée » ?
""", r"""Regarde la tranche `L[0:i]` au début de chaque tour de boucle.""",
r"""Le nombre de comparaisons au tour $i$ est entre 1 et $i$ ; additionne.""",
r"""Le décalage s'arrête dès que `L[j - 1] > x` est faux : un élément égal à `x` n'est jamais dépassé.""",
r"""**Étape 1 — Analyse de l'énoncé.** On prouve la correction par un invariant, puis on dénombre les comparaisons selon l'ordre initial des données.

**Étape 2 — Rappels du cours.**

> **Définition — Tri stable.** Un tri est stable s'il conserve l'ordre relatif des éléments égaux.

> **Formule — Somme des entiers.** $\sum_{i=1}^{n-1}i=\frac{n(n-1)}2$.

**Étape 3 — Stratégie.** Invariant sur le préfixe trié ; dénombrement tour par tour.

**Étape 4 — Résolution détaillée.**

**4.1 Invariant.** « Au début du tour $i$, `L[0:i]` contient les $i$ premiers éléments initiaux, rangés dans l'ordre croissant. » Vrai pour $i=1$. Le tour $i$ décale vers la droite les éléments de `L[0:i]` strictement plus grands que `x`, puis place `x` dans le trou : `L[0:i+1]` est trié. En fin de boucle ($i=n$), toute la liste est triée.

**4.2 Comparaisons.** Au tour $i$, la boucle `while` fait au moins 1 comparaison (si `L[i-1] <= x`) et au plus $i$ (si `x` est plus petit que tout le préfixe). Meilleur cas : liste déjà triée, $n-1$ comparaisons. Pire cas : liste triée en ordre décroissant, $\sum_{i=1}^{n-1}i=\frac{n(n-1)}2$ comparaisons, donc $O(n^2)$.

**4.3 Stabilité et listes presque triées.** Le test strict `L[j - 1] > x` arrête le décalage devant un élément égal : `x` reste après lui, l'ordre des égaux est conservé, le tri est stable. Le nombre de décalages est égal au nombre d'inversions de la liste : pour une liste presque triée, il y en a peu et le tri est presque linéaire.

**Étape 5 — Vérification.**

> **Vérification — Liste décroissante de 4 éléments.** `[4, 3, 2, 1]` : 1, puis 2, puis 3 comparaisons, total $6=\frac{4\times3}2$.

**Étape 6 — Conclusion.**
$$\boxed{\text{meilleur cas }n-1,\quad\text{pire cas }\tfrac{n(n-1)}2\text{ comparaisons};\ \text{tri stable}}$$""",
r"""Invariant : `L[0:i]` trié ; meilleur cas $n-1$ comparaisons (liste triée), pire cas $\frac{n(n-1)}2$ (liste décroissante) ; stable, et rapide si peu d'inversions.""")
src('Tris')

# ------------------------------------------------------------------ 11. Tri fusion
ex('i-tri-fus', M, 'Tris', 2, 'Tri fusion : fusion et récurrence de coût', 25, r"""
1. Écrire une fonction `fusion(A, B)` qui, à partir de deux listes triées, renvoie la liste triée de tous leurs éléments, en $O(\text{len}(A)+\text{len}(B))$.
2. En déduire une fonction récursive `tri_fusion(L)`.
3. Soit $C(n)$ le nombre de comparaisons effectuées dans le pire cas pour $n=2^k$. Montrer que $C(n)\le2C(n/2)+n$, puis que $C(n)\le n\log_2n$.
4. Le tri fusion trie-t-il « en place » ? Quelle mémoire supplémentaire utilise-t-il ?
""", r"""Deux indices `i`, `j` avancent dans `A` et `B` : on prend à chaque fois le plus petit des deux éléments de tête.""",
r"""Récursion : coupe `L` en deux moitiés, trie chacune, fusionne. Cas de base : longueur au plus 1.""",
r"""Pour $n=2^k$, pose $c_k=C(2^k)/2^k$ et montre que $c_k\le c_{k-1}+1$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Le tri fusion suit le schéma « diviser pour régner » : couper, résoudre récursivement, combiner. Le coût se lit sur une récurrence.

**Étape 2 — Rappels du cours.**

> **Principe — Diviser pour régner.** Si un problème de taille $n$ se ramène à deux problèmes de taille $n/2$ et une combinaison linéaire, son coût vérifie $C(n)=2C(n/2)+O(n)$, d'où $C(n)=O(n\log n)$.

**Étape 3 — Stratégie.** Écrire la fusion linéaire, puis majorer par récurrence en posant $c_k=C(2^k)/2^k$.

**Étape 4 — Résolution détaillée.**

**4.1 Fusion.**

```python
def fusion(A, B):
    i, j, R = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            R.append(A[i])
            i += 1
        else:
            R.append(B[j])
            j += 1
    return R + A[i:] + B[j:]
```

Chaque comparaison place un élément dans `R` : au plus $\text{len}(A)+\text{len}(B)-1$ comparaisons.

**4.2 Tri.**

```python
def tri_fusion(L):
    if len(L) <= 1:
        return L[:]
    m = len(L) // 2
    return fusion(tri_fusion(L[:m]), tri_fusion(L[m:]))
```

**4.3 Coût.** Pour $n=2^k$ : deux appels sur $n/2$ éléments puis une fusion d'au plus $n-1\le n$ comparaisons, donc $C(n)\le2C(n/2)+n$ et $C(1)=0$. Avec $c_k=C(2^k)/2^k$ : $c_k\le c_{k-1}+1$ et $c_0=0$, donc $c_k\le k$, soit $C(n)\le n\log_2n$.

**4.4 Mémoire.** Cette version crée de nouvelles listes (tranches et résultat de la fusion) : elle n'est pas en place et utilise $O(n)$ mémoire supplémentaire à chaque niveau de fusion, en plus d'une pile d'appels de profondeur $\log_2n$.

**Étape 5 — Vérification.**

> **Vérification — Petit cas.** `tri_fusion([5, 2, 4, 6, 1, 3])` renvoie `[1, 2, 3, 4, 5, 6]`, et pour $n=8$ la borne vaut $8\times3=24$ comparaisons.

**Étape 6 — Conclusion.**
$$\boxed{C(n)\le2C(n/2)+n\ \Rightarrow\ C(n)\le n\log_2n=O(n\log n),\ \text{mémoire }O(n)}$$""",
r"""Fusion à deux indices, linéaire ; $C(n)\le2C(n/2)+n$ et $c_k=C(2^k)/2^k\le k$ donnent $C(n)\le n\log_2n$ ; pas en place, $O(n)$ de mémoire.""")
src('Tris')

# ------------------------------------------------------------------ 12. Tri par comptage
ex('i-tri-cpt', M, 'Tris', 1, 'Tri par comptage de notes', 15, r"""
On veut trier une liste `notes` de $n$ entiers compris entre $0$ et $20$.

1. Écrire une fonction `tri_comptage(notes, m=20)` qui compte les occurrences de chaque valeur dans une liste de taille $m+1$, puis reconstruit la liste triée.
2. Donner sa complexité en fonction de $n$ et $m$. Pourquoi peut-elle battre la borne $O(n\log n)$ des tris par comparaison ?
3. Dans quel cas ce tri devient-il un mauvais choix ?
""", r"""`compte[v]` contient le nombre de fois où la valeur `v` apparaît.""",
r"""Pour reconstruire, parcours les valeurs `v` de 0 à $m$ et ajoute `compte[v]` fois la valeur `v`.""",
r"""Ce tri ne compare jamais deux éléments entre eux : il utilise le fait que les valeurs sont des petits entiers.""",
r"""**Étape 1 — Analyse de l'énoncé.** Les valeurs appartiennent à un petit ensemble connu à l'avance : on peut les compter au lieu de les comparer.

**Étape 2 — Rappels du cours.**

> **Propriété — Tris par comparaison.** Tout tri qui ne procède que par comparaisons fait $\Omega(n\log n)$ comparaisons dans le pire cas.

**Étape 3 — Stratégie.** Un tableau de compteurs indexé par les valeurs, puis une reconstruction dans l'ordre des valeurs.

**Étape 4 — Résolution détaillée.**

**4.1 Programme.**

```python
def tri_comptage(notes, m=20):
    compte = [0] * (m + 1)
    for v in notes:
        compte[v] += 1
    R = []
    for v in range(m + 1):
        R += [v] * compte[v]
    return R
```

**4.2 Complexité.** Comptage : $O(n)$ ; reconstruction : $O(n+m)$ (on parcourt $m+1$ valeurs et on écrit $n$ éléments). Total $O(n+m)$, linéaire quand $m$ est fixé (ici 20). La borne $\Omega(n\log n)$ ne s'applique pas : aucune comparaison entre éléments n'est faite, on utilise la valeur comme indice.

**4.3 Limites.** Si l'intervalle des valeurs est grand devant $n$ (par exemple trier 100 entiers entre 0 et $10^9$), le tableau `compte` coûte $O(m)$ en temps et en mémoire : le tri devient bien pire qu'un tri fusion. Il ne s'applique pas non plus directement à des flottants ou à des chaînes.

**Étape 5 — Vérification.**

> **Vérification — Exemple.** `tri_comptage([12, 5, 20, 5, 0])` renvoie `[0, 5, 5, 12, 20]`.

**Étape 6 — Conclusion.**
$$\boxed{O(n+m)\ \text{en temps et }O(m)\text{ en mémoire : excellent si }m=O(n),\ \text{mauvais si }m\gg n}$$""",
r"""Compter les occurrences dans une liste de taille $m+1$, puis reconstruire : $O(n+m)$, sans comparaison ; à éviter quand $m$ est très grand devant $n$.""")
src('Tris')

# ------------------------------------------------------------------ 13. Tri rapide et sélection
ex('i-tri-sel', M, 'Tris', 3, 'Tri rapide et k-ième plus petit élément', 30, r"""
On utilise la partition suivante, qui renvoie trois listes.

```python
def partition(L, pivot):
    petits = [x for x in L if x < pivot]
    egaux = [x for x in L if x == pivot]
    grands = [x for x in L if x > pivot]
    return petits, egaux, grands
```

1. Écrire un tri rapide `tri_rapide(L)` qui prend `L[0]` comme pivot. Montrer que, sur une liste déjà triée d'éléments distincts, il effectue un nombre de comparaisons de l'ordre de $n^2$.
2. Écrire une fonction `kieme(L, k)` qui renvoie le $k$-ième plus petit élément ($k\ge1$) sans trier toute la liste, en ne faisant qu'**un** appel récursif.
3. On suppose que le pivot coupe toujours la liste en deux moitiés. Montrer que `kieme` fait alors $O(n)$ comparaisons, alors qu'un tri en ferait $O(n\log n)$.
""", r"""Le tri rapide trie récursivement `petits` et `grands`, puis concatène `petits + egaux + grands`.""",
r"""Pour `kieme`, compare $k$ aux tailles de `petits` et `egaux` pour savoir dans quelle partie chercher.""",
r"""Si chaque appel coûte au plus $c\,n$ et que la taille est divisée par 2, le coût total est une série géométrique.""",
r"""**Étape 1 — Analyse de l'énoncé.** Même partition pour deux usages : le tri rapide traite les deux côtés, la sélection n'en garde qu'un. On compare les coûts.

**Étape 2 — Rappels du cours.**

> **Principe — Tri rapide.** Choisir un pivot, partitionner, trier récursivement les deux parties. Coût moyen $O(n\log n)$, pire cas $O(n^2)$.

> **Formule — Série géométrique.** $n+\frac n2+\frac n4+\dots\le2n$.

**Étape 3 — Stratégie.** Analyse du pire cas sur une liste triée ; sélection par élimination d'une partie ; somme géométrique.

**Étape 4 — Résolution détaillée.**

**4.1 Tri rapide.**

```python
def tri_rapide(L):
    if len(L) <= 1:
        return L[:]
    petits, egaux, grands = partition(L, L[0])
    return tri_rapide(petits) + egaux + tri_rapide(grands)
```

Sur une liste triée d'éléments distincts, le pivot `L[0]` est le minimum : `petits` est vide et `grands` a $n-1$ éléments. La partition d'une liste de longueur $m$ fait ici $3m$ comparaisons ; le total est $3(n+(n-1)+\dots+2)$, de l'ordre de $\frac32n^2$ : quadratique.

**4.2 Sélection.**

```python
def kieme(L, k):
    petits, egaux, grands = partition(L, L[0])
    if k <= len(petits):
        return kieme(petits, k)
    if k <= len(petits) + len(egaux):
        return L[0]
    return kieme(grands, k - len(petits) - len(egaux))
```

Si $k$ ne dépasse pas la taille de `petits`, l'élément cherché y est, avec le même rang. Sinon, s'il tombe dans `egaux`, c'est le pivot. Sinon il est dans `grands`, avec le rang $k$ diminué des éléments écartés.

**4.3 Coût avec un pivot médian.** Une partition de $m$ éléments coûte au plus $3m$ comparaisons, et l'on ne relance que sur au plus $m/2$ éléments : $T(n)\le3n+T(n/2)\le3n(1+\frac12+\frac14+\dots)\le6n$. Donc $O(n)$, contre $O(n\log n)$ pour trier puis lire la $k$-ième case.

**Étape 5 — Vérification.**

> **Vérification — Exemple.** `kieme([7, 2, 9, 4, 4, 1], 3)` vaut 4 ; `kieme([7, 2, 9, 4, 4, 1], 6)` vaut 9.

**Étape 6 — Conclusion.**
$$\boxed{\text{tri rapide : }\Theta(n^2)\text{ sur liste triée};\quad\text{sélection à un appel : }T(n)\le3n+T(n/2)=O(n)}$$""",
r"""Pivot `L[0]` sur liste triée : partitions de tailles $n, n-1, \dots$, donc $\Theta(n^2)$. `kieme` ne récurse que d'un côté ; avec des coupes en deux, $T(n)\le 3n+T(n/2)\le 6n$.""")
src('Tris')
