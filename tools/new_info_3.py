# Informatique commune MP — 3e série (10 exercices originaux) sur les chapitres du cours de D. Rupprecht
# (lycée Pierre-de-Fermat) : Python, complexité et preuves, piles et récursivité, flottants, tris.
# Tout le code des corrigés est exécuté et testé par tools/test_info.py.
from newlib import ex, E

def src(chapitre):
    E[-1]['enonce'] += f"\n\n*Exercice original sur le chapitre « {chapitre} » du cours d'informatique MP de D. Rupprecht (lycée Pierre-de-Fermat).*"
    E[-1]['ajout'] = '2026-11-25'

M = 'Informatique'

# ------------------------------------------------------------------ 1. Compression par plages
ex('i-py-rle', M, 'Python : listes et fichiers', 1, 'Compression d\'une chaîne par plages', 15, r"""
On compresse une chaîne en remplaçant chaque plage de caractères identiques consécutifs par le couple (caractère, longueur). Par exemple `'aaabccdddd'` devient `[('a', 3), ('b', 1), ('c', 2), ('d', 4)]`.

1. Écrire une fonction `compresser(s)` qui renvoie la liste des couples associée à la chaîne `s` (liste vide si `s` est vide).
2. Écrire la fonction réciproque `decompresser(L)`.
3. Donner la complexité des deux fonctions en fonction de la longueur $n$ de la chaîne.
4. On compte qu'un couple occupe deux cases et un caractère une case. Pour quelles chaînes la compression fait-elle gagner de la place ?
""", r"""Parcours la chaîne une seule fois en regardant le dernier couple déjà construit : soit le caractère prolonge la plage, soit il en commence une nouvelle.""",
r"""Un couple est non mutable : pour allonger la dernière plage, remplace `L[-1]` par un nouveau couple.""",
r"""Pour la question 4, si la chaîne a $r$ plages, compare $2r$ à $n$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Une plage est une suite maximale de caractères égaux et consécutifs. La chaîne `'abab'` a quatre plages de longueur 1 : on ne regroupe que des caractères **voisins**.

**Étape 2 — Rappels du cours.**

> **Propriété — Listes Python.** `L.append(x)`, l'accès `L[-1]` et l'affectation `L[-1] = v` coûtent $O(1)$.

> **Propriété — Chaînes.** Une chaîne n'est pas mutable : `''.join(morceaux)` construit le résultat en temps linéaire en sa longueur.

**Étape 3 — Stratégie.** On maintient l'invariant : après lecture des $k$ premiers caractères, `L` est la compression du préfixe `s[:k]`.

**Étape 4 — Résolution détaillée.**

**4.1 Compression.**

```python
def compresser(s):
    L = []
    for c in s:
        if L and L[-1][0] == c:
            L[-1] = (c, L[-1][1] + 1)
        else:
            L.append((c, 1))
    return L
```

Si le caractère lu est celui de la dernière plage, il l'allonge ; sinon il ouvre une nouvelle plage. L'invariant est conservé et, à la fin, `L` compresse toute la chaîne.

**4.2 Décompression.**

```python
def decompresser(L):
    return ''.join(c * k for c, k in L)
```

**4.3 Complexité.** `compresser` fait un tour de boucle par caractère, chacun en $O(1)$ : $O(n)$. `decompresser` produit $n$ caractères au total : $O(n)$ grâce à `join`.

**4.4 Gain de place.** Avec $r$ plages, la compression occupe $2r$ cases contre $n$. Elle est utile si et seulement si $2r<n$, c'est-à-dire si les plages ont en moyenne une longueur supérieure à 2. Pour une chaîne sans deux caractères voisins égaux, $r=n$ et la taille **double**.

**Étape 5 — Vérification.**

> **Vérification — Aller-retour.** `decompresser(compresser(s)) == s` pour toute chaîne ; `compresser('')` vaut `[]` et `compresser('abab')` a 4 couples.

**Étape 6 — Conclusion.**
$$\boxed{\text{compression et décompression en }O(n)\text{ ; gain si et seulement si }2r<n}$$""",
r"""Un parcours qui allonge ou crée la dernière plage ; réciproque par `join` ; $O(n)$ ; utile seulement si $2r<n$.""")
src('Rappels de base sur Python')

# ------------------------------------------------------------------ 2. Matrices en listes de listes
ex('i-py-matrice', M, 'Python : listes et fichiers', 1, 'Matrices en listes de listes : le piège et le produit', 20, r"""
Une matrice de taille $n\times p$ est représentée par une liste de $n$ listes de longueur $p$.

1. On exécute :
```python
M = [[0] * 3] * 3
M[0][0] = 1
```
Que vaut `M` ? Expliquer.
2. Écrire une fonction `zeros(n, p)` qui renvoie une matrice nulle $n\times p$ correcte.
3. Écrire une fonction `transposee(A)`.
4. Écrire une fonction `produit(A, B)` qui renvoie le produit matriciel $AB$ (on suppose les tailles compatibles). Combien de multiplications de nombres effectue-t-elle pour $A$ de taille $n\times p$ et $B$ de taille $p\times q$ ?
""", r"""`[x] * 3` recopie trois fois la **même référence** `x`.""",
r"""Crée une nouvelle ligne à chaque tour avec une compréhension : `[[0] * p for _ in range(n)]`.""",
r"""Le coefficient $(i,j)$ du produit est $\sum_k a_{ik}b_{kj}$ : trois boucles imbriquées.""",
r"""**Étape 1 — Analyse de l'énoncé.** Une liste Python contient des références vers des objets. Copier une liste de listes avec `*` copie les références, pas les lignes.

**Étape 2 — Rappels du cours.**

> **Propriété — Représentation interne.** Une variable est une référence vers un objet ; les listes sont mutables, donc une modification à travers une référence est visible par toutes les autres.

> **Définition — Produit matriciel.** Si $A$ est $n\times p$ et $B$ est $p\times q$, $AB$ est $n\times q$ et $(AB)_{ij}=\sum_{k=0}^{p-1}a_{ik}b_{kj}$.

**Étape 3 — Stratégie.** Construire chaque ligne comme un nouvel objet, puis traduire les définitions par des boucles.

**Étape 4 — Résolution détaillée.**

**4.1 Le piège.** `[0] * 3` crée **une** liste `[0, 0, 0]` ; `[...] * 3` crée une liste qui contient trois fois la même référence vers elle. Modifier `M[0][0]` modifie donc la seule ligne existante, vue trois fois :

```python
M = [[0] * 3] * 3
M[0][0] = 1
# M vaut [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
```

**4.2 Matrice nulle correcte.**

```python
def zeros(n, p):
    return [[0] * p for _ in range(n)]
```

La compréhension évalue `[0] * p` à chaque tour : les $n$ lignes sont distinctes. (Pour `[0] * p` le partage est sans danger, car un entier n'est pas mutable.)

**4.3 Transposée.**

```python
def transposee(A):
    n, p = len(A), len(A[0])
    T = zeros(p, n)
    for i in range(n):
        for j in range(p):
            T[j][i] = A[i][j]
    return T
```

**4.4 Produit.**

```python
def produit(A, B):
    n, p, q = len(A), len(B), len(B[0])
    C = zeros(n, q)
    for i in range(n):
        for j in range(q):
            s = 0
            for k in range(p):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C
```

Chacun des $nq$ coefficients demande $p$ multiplications : $npq$ multiplications, soit $n^3$ pour deux matrices carrées.

**Étape 5 — Vérification.**

> **Vérification — Exemple.** `produit([[1, 2], [3, 4]], [[0, 1], [1, 0]])` vaut `[[2, 1], [4, 3]]` : multiplier à droite par cette matrice échange les colonnes. Et `transposee([[1, 2, 3]])` vaut `[[1], [2], [3]]`.

**Étape 6 — Conclusion.**
$$\boxed{[[0]*p]*n\text{ partage une seule ligne ; produit en }npq\text{ multiplications}}$$""",
r"""Les trois lignes sont la même liste, d'où `[[1, 0, 0]] * 3` ; utiliser une compréhension ; le produit coûte $npq$ multiplications.""")
src('Rappels de base sur Python (listes)')

# ------------------------------------------------------------------ 3. Division euclidienne et Euclide
ex('i-cx-euclide', M, 'Complexité et preuves', 1, 'Division par soustractions et algorithme d\'Euclide', 20, r"""
On considère, pour des entiers $a\ge0$ et $b>0$ :

```python
def division(a, b):
    q, r = 0, a
    while r >= b:
        q, r = q + 1, r - b
    return q, r
```

1. Montrer que la boucle termine et que la fonction renvoie le quotient et le reste de la division euclidienne de $a$ par $b$.
2. Combien de tours de boucle sont effectués ? Pourquoi cet algorithme est-il lent pour $a=10^{18}$, $b=3$ ?
3. On calcule le pgcd par l'algorithme d'Euclide :
```python
def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```
Combien de tours de boucle sont effectués pour `pgcd(F[k + 1], F[k])`, où $F_0=0$, $F_1=1$, $F_{k+2}=F_{k+1}+F_k$, et $k\ge2$ ?
""", r"""Variant : `r`. Invariant : $a=bq+r$ et $r\ge0$.""",
r"""Le nombre de tours est le quotient $q$ ; compare-le à la taille de $a$ en nombre de chiffres.""",
r"""Montre que $F_{k+1}\bmod F_k=F_{k-1}$ pour $k\ge3$, puis suis les couples successifs.""",
r"""**Étape 1 — Analyse de l'énoncé.** On prouve un algorithme (terminaison et correction), on mesure son coût, puis on étudie l'algorithme d'Euclide sur un exemple extrême.

**Étape 2 — Rappels du cours.**

> **Définition — Variant.** Quantité entière positive qui décroît strictement à chaque tour : elle prouve la terminaison.

> **Définition — Invariant.** Propriété vraie avant la boucle et conservée par chaque tour ; avec la condition de sortie, elle prouve la correction.

> **Théorème — Division euclidienne.** Il existe un unique couple $(q,r)$ d'entiers avec $a=bq+r$ et $0\le r<b$.

**Étape 3 — Stratégie.** Invariant $a=bq+r$, $r\ge0$ ; variant $r$. Pour Euclide, calculer les restes successifs grâce à la récurrence de Fibonacci.

**Étape 4 — Résolution détaillée.**

**4.1 Terminaison.** Tant que la boucle tourne, $r\ge b>0$, et un tour remplace $r$ par $r-b<r$ avec $r-b\ge0$ : $r$ est un entier positif qui décroît strictement, la boucle termine.

**4.2 Correction.** Au départ $bq+r=0+a=a$ et $r=a\ge0$. Si $a=bq+r$ et $r\ge b$, après le tour $b(q+1)+(r-b)=a$ et $r-b\ge0$ : l'invariant est conservé. En sortie, $a=bq+r$, $r\ge0$ et $r<b$ : par unicité, $(q,r)$ est le couple de la division euclidienne.

**4.3 Coût.** Chaque tour augmente $q$ de 1 : il y a exactement $\lfloor a/b\rfloor$ tours. Pour $a=10^{18}$ et $b=3$, cela fait environ $3\times10^{17}$ tours, soit des années de calcul, alors que $a$ ne s'écrit qu'avec 19 chiffres : le coût est **exponentiel en la taille** de l'entrée. L'opérateur `%` de Python fait le même travail en temps quasi constant.

**4.4 Euclide sur Fibonacci.** Pour $k\ge3$, $F_{k+1}=F_k+F_{k-1}$ avec $0\le F_{k-1}<F_k$, donc $F_{k+1}\bmod F_k=F_{k-1}$. Le couple $(F_{k+1},F_k)$ devient $(F_k,F_{k-1})$, puis $(F_{k-1},F_{k-2})$, etc., jusqu'à $(F_3,F_2)=(2,1)$, qui devient $(1,0)$ en un tour. On compte un tour par couple de $(F_{k+1},F_k)$ à $(F_3,F_2)$ :
$$k-2+1=k-1\text{ tours.}$$

> **Remarque.** Le théorème de Lamé (admis) affirme que ce sont les pires cas : le nombre de tours est $O(\log b)$, logarithmique en $b$, contrairement aux soustractions.

**Étape 5 — Vérification.**

> **Vérification — Petits cas.** `division(17, 5)` vaut `(3, 2)` ; `pgcd(3, 2)` fait 2 tours ($(3,2)\to(2,1)\to(1,0)$) et $k=3$ donne bien $k-1=2$ ; `pgcd(89, 55)` ($k=10$) fait 9 tours.

**Étape 6 — Conclusion.**
$$\boxed{\lfloor a/b\rfloor\text{ tours par soustractions ; }k-1\text{ tours pour }\mathrm{pgcd}(F_{k+1},F_k)}$$""",
r"""Variant $r$, invariant $a=bq+r$, $r\ge0$ ; $\lfloor a/b\rfloor$ tours (exponentiel en la taille) ; Euclide fait $k-1$ tours sur $(F_{k+1},F_k)$.""")
src('Algorithmes, complexité et preuves')

# ------------------------------------------------------------------ 4. Tranche de somme maximale
ex('i-cx-maxsub', M, 'Complexité et preuves', 2, 'Tranche de somme maximale : de n³ à n', 25, r"""
Soit `L` une liste non vide d'entiers relatifs de longueur $n$. Une **tranche** est une sous-liste non vide de termes consécutifs `L[i:j]` avec $i<j$. On cherche la plus grande somme d'une tranche.

1. Écrire une fonction naïve qui essaie toutes les tranches et calcule chaque somme avec une boucle. Quelle est sa complexité ?
2. Améliorer la fonction pour obtenir un coût $O(n^2)$.
3. On note $c_i$ la plus grande somme d'une tranche **qui se termine** à l'indice $i$. Exprimer $c_i$ en fonction de $c_{i-1}$ et de `L[i]`, puis en déduire une fonction en $O(n)$. Justifier sa correction par un invariant.
4. Que renvoie-t-elle pour `[2, -5, 3, -1, 4, -6, 2]` ?
""", r"""Il y a $\frac{n(n+1)}2$ tranches ; pour $O(n^2)$, mets à jour la somme quand on allonge la tranche d'un terme.""",
r"""Une tranche finissant en $i$ est soit `[L[i]]` seule, soit une tranche finissant en $i-1$ prolongée par `L[i]`.""",
r"""$c_i=\max(L_i,\,c_{i-1}+L_i)$ ; la réponse est $\max_i c_i$.""",
r"""**Étape 1 — Analyse de l'énoncé.** Les termes peuvent être négatifs : il ne faut ni tout sommer, ni prendre seulement le maximum. Si tous les termes sont négatifs, la réponse est le plus grand terme (une tranche est non vide).

**Étape 2 — Rappels du cours.**

> **Définition — Ordres de grandeur.** $O(n^3)$, $O(n^2)$ et $O(n)$ séparent des algorithmes utilisables pour $n=10^3$, $10^4$ ou $10^7$.

> **Définition — Invariant de boucle.** Propriété vraie avant la boucle, conservée à chaque tour, qui donne le résultat en sortie.

**Étape 3 — Stratégie.** Réduire le travail redondant : recalculer une somme de zéro (naïf), l'allonger (quadratique), puis ne garder que la meilleure tranche finissant à l'indice courant (linéaire).

**Étape 4 — Résolution détaillée.**

**4.1 Naïf.**

```python
def tranche_max_naif(L):
    n = len(L)
    best = L[0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            s = 0
            for k in range(i, j):
                s += L[k]
            best = max(best, s)
    return best
```

Le nombre d'additions est $\sum_{i<j}(j-i)=\sum_{\ell=1}^{n}\ell(n-\ell+1)=\frac{n(n+1)(n+2)}6$ : complexité $O(n^3)$.

**4.2 Quadratique.** La somme de `L[i:j+1]` est celle de `L[i:j]` plus `L[j]` :

```python
def tranche_max_quad(L):
    n = len(L)
    best = L[0]
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += L[j]
            best = max(best, s)
    return best
```

$\frac{n(n+1)}2$ additions : $O(n^2)$.

**4.3 Linéaire.** Une tranche finissant en $i$ est `[L[i]]` ou une tranche finissant en $i-1$ suivie de `L[i]`, d'où
$$c_0=L_0,\qquad c_i=\max(L_i,\;c_{i-1}+L_i).$$

```python
def tranche_max(L):
    best = cur = L[0]
    for x in L[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
```

Invariant après le traitement de l'indice $i$ : `cur` $=c_i$ et `best` $=\max(c_0,\dots,c_i)$, la plus grande somme d'une tranche incluse dans `L[0:i+1]` (toute tranche se termine quelque part). Il est vrai pour $i=0$ et conservé par la relation ci-dessus ; en sortie, `best` est la réponse. Un seul parcours : $O(n)$.

**4.4 Exemple.** Les valeurs de $c_i$ sont $2,-3,3,2,6,0,2$ ; le maximum est $6$, atteint par la tranche `[3, -1, 4]`.

**Étape 5 — Vérification.**

> **Vérification — Cas négatif.** Pour `[-3, -1, -2]`, la fonction renvoie $-1$ : la tranche `[-1]`. Les trois versions donnent le même résultat sur des listes aléatoires.

**Étape 6 — Conclusion.**
$$\boxed{c_i=\max(L_i,c_{i-1}+L_i),\ \text{réponse }\max_ic_i=6\text{ en }O(n)}$$""",
r"""$O(n^3)$ puis $O(n^2)$ en allongeant les sommes ; $c_i=\max(L_i,c_{i-1}+L_i)$ donne $O(n)$ ; réponse $6$.""")
src('Algorithmes, complexité et preuves')

# ------------------------------------------------------------------ 5. Deux indices
ex('i-cx-deuxsomme', M, 'Complexité et preuves', 2, 'Deux termes de somme donnée dans une liste triée', 20, r"""
Soit `L` une liste d'entiers **triée par ordre croissant** et `s` un entier. On cherche deux indices $i<j$ tels que `L[i] + L[j] == s`.

1. Quelle est la complexité de l'algorithme naïf qui teste tous les couples ?
2. On propose :
```python
def deux_somme(L, s):
    i, j = 0, len(L) - 1
    while i < j:
        t = L[i] + L[j]
        if t == s:
            return (i, j)
        elif t < s:
            i += 1
        else:
            j -= 1
    return None
```
Montrer que la fonction termine, puis qu'elle renvoie un couple solution dès qu'il en existe un.
3. Quelle est sa complexité ? La comparer à une méthode qui, pour chaque $i$, cherche `s - L[i]` par dichotomie.
4. Si la liste n'est pas triée, comment obtenir un coût linéaire en moyenne ?
""", r"""Variant : $j-i$.""",
r"""Invariant : s'il existe une solution, il en existe une $(i',j')$ avec $i\le i'<j'\le j$. Si `L[i] + L[j] < s`, montre qu'aucune solution n'utilise l'indice $i$.""",
r"""Pour la question 4, un dictionnaire des valeurs déjà rencontrées permet de tester `s - x` en $O(1)$ en moyenne.""",
r"""**Étape 1 — Analyse de l'énoncé.** La liste triée permet d'éliminer un indice entier à chaque comparaison : c'est la méthode « des deux indices ».

**Étape 2 — Rappels du cours.**

> **Définition — Variant et invariant.** Le variant prouve la terminaison, l'invariant la correction.

> **Propriété — Dichotomie.** Une recherche dans une liste triée de longueur $n$ coûte $O(\log n)$.

**Étape 3 — Stratégie.** Montrer qu'un indice éliminé ne peut appartenir à aucune solution restante.

**Étape 4 — Résolution détaillée.**

**4.1 Naïf.** On teste $\frac{n(n-1)}2$ couples : $O(n^2)$.

**4.2 Terminaison.** À chaque tour sans retour, $i$ augmente ou $j$ diminue de 1 : l'entier $j-i$ décroît strictement. Il est positif tant que la boucle tourne, donc la boucle s'arrête.

**4.3 Correction.** Invariant $(\mathcal I)$ : s'il existe une solution, il en existe une $(i',j')$ avec $i\le i'<j'\le j$. Il est vrai au départ ($i=0$, $j=n-1$). Supposons-le vrai et `t = L[i] + L[j]` différent de `s`, avec une solution $(i',j')$ dans l'intervalle.
- Si $t<s$ : pour tout $k\le j$, `L[i] + L[k]` $\le t<s$ car la liste est croissante. Aucune solution n'utilise l'indice $i$, donc $i'>i$, et l'invariant reste vrai pour $i+1$.
- Si $t>s$ : symétriquement, pour tout $k\ge i$, `L[k] + L[j]` $\ge t>s$, donc $j'<j$.

Si une solution existe, l'intervalle $[i,j]$ en contient toujours une, donc $i<j$ reste vrai jusqu'à ce qu'on la trouve : la fonction renvoie un couple. Sinon, elle ne peut rien renvoyer d'autre que `None`, car elle ne renvoie un couple qu'après avoir vérifié l'égalité.

**4.4 Complexité.** Au plus $n-1$ tours de coût constant : $O(n)$. La méthode par dichotomie coûte $n$ recherches de $O(\log n)$ : $O(n\log n)$, moins bonne.

**4.5 Liste non triée.** Trier d'abord coûte $O(n\log n)$. Pour du linéaire en moyenne, on mémorise les valeurs déjà vues :

```python
def deux_somme_dict(L, s):
    vus = {}
    for j, x in enumerate(L):
        if s - x in vus:
            return (vus[s - x], j)
        vus[x] = j
    return None
```

Chaque test et chaque insertion coûtent $O(1)$ en moyenne : $O(n)$.

**Étape 5 — Vérification.**

> **Vérification — Exemple.** Pour `L = [1, 3, 4, 6, 9]` et `s = 10`, les couples examinés sont $(0,4)$ : $10$, trouvé, d'où `(0, 4)`. Pour `s = 8` : $(0,4)\to10>8$, $(0,3)\to7<8$, $(1,3)\to9>8$, $(1,2)\to7<8$, puis $i=j$ : `None`.

**Étape 6 — Conclusion.**
$$\boxed{\text{deux indices : }O(n)\text{, contre }O(n\log n)\text{ (dichotomie) et }O(n^2)\text{ (naïf)}}$$""",
r"""Variant $j-i$ ; invariant « une solution reste dans $[i,j]$ » ; $O(n)$ ; dictionnaire pour une liste non triée.""")
src('Algorithmes, complexité et preuves')

# ------------------------------------------------------------------ 6. File avec deux piles
ex('i-pile-file2', M, 'Piles, files et récursivité', 2, 'Une file avec deux piles', 20, r"""
On réalise une file (premier entré, premier sorti) avec deux piles, représentées par deux listes Python `entree` et `sortie` dont on n'utilise que `append` et `pop()` :

```python
def file_vide():
    return ([], [])

def enfiler(F, x):
    F[0].append(x)

def defiler(F):
    entree, sortie = F
    if not sortie:
        while entree:
            sortie.append(entree.pop())
    return sortie.pop()
```

1. Exécuter à la main : `enfiler` 1, 2, 3, puis `defiler`, puis `enfiler` 4, puis trois `defiler`. Que renvoient les appels à `defiler` ?
2. Montrer que `defiler` renvoie toujours l'élément le plus ancien de la file.
3. Quel est le coût d'un appel à `defiler` dans le pire cas ?
4. Montrer qu'une suite de $m$ opérations à partir d'une file vide coûte $O(m)$ au total.
""", r"""Lorsqu'on vide `entree` dans `sortie`, l'ordre des éléments est renversé.""",
r"""Invariant : la file est `sortie` lue de la fin vers le début, suivie de `entree` lue du début vers la fin.""",
r"""Compte, pour chaque élément, le nombre de fois où il est empilé et dépilé au cours de sa vie.""",
r"""**Étape 1 — Analyse de l'énoncé.** Une pile renverse l'ordre ; deux renversements successifs le rétablissent. On étudie la correction, puis le coût **amorti** : le coût total d'une suite d'opérations.

**Étape 2 — Rappels du cours.**

> **Définition — Pile et file.** Une pile est « dernier entré, premier sorti » (`append` et `pop()` en $O(1)$), une file est « premier entré, premier sorti ».

> **Propriété — `deque`.** En pratique, `collections.deque` réalise directement une file avec `append` et `popleft` en $O(1)$.

**Étape 3 — Stratégie.** Écrire l'invariant qui relie le contenu des deux piles au contenu de la file, puis compter les mouvements de chaque élément.

**Étape 4 — Résolution détaillée.**

**4.1 Exécution.** Après trois `enfiler` : `entree = [1, 2, 3]`, `sortie = []`. Le premier `defiler` vide `entree` dans `sortie`, qui devient `[3, 2, 1]`, et renvoie `1`. On enfile 4 : `entree = [4]`. Les trois `defiler` suivants renvoient `2` puis `3` (pris dans `sortie`), puis, `sortie` étant vide, transfèrent `[4]` et renvoient `4`. On obtient $1,2,3,4$ : l'ordre d'arrivée.

**4.2 Correction.** Invariant : le contenu de la file, du plus ancien au plus récent, est `sortie` lue de la fin vers le début, puis `entree` lue du début vers la fin.
- `enfiler` ajoute `x` à la fin de `entree`, c'est-à-dire en queue de file.
- Le transfert, fait seulement quand `sortie` est vide, place le plus ancien élément d'`entree` en dernière position de `sortie` : l'invariant est conservé.
- `sortie.pop()` retire alors le dernier élément de `sortie`, c'est-à-dire la tête de la file.

**4.3 Pire cas.** Si $k$ éléments sont dans `entree` et `sortie` est vide, `defiler` fait $k$ transferts : $O(k)$, linéaire dans le pire cas.

**4.4 Coût amorti.** Chaque élément est empilé au plus deux fois (dans `entree`, puis dans `sortie`) et dépilé au plus deux fois. Une suite de $m$ opérations manipule au plus $m$ éléments, donc fait au plus $4m$ opérations élémentaires sur les piles : $O(m)$ au total, soit $O(1)$ **en moyenne par opération**, même si un appel isolé peut coûter cher.

**Étape 5 — Vérification.**

> **Vérification — Simulation.** Sur des suites aléatoires d'`enfiler` et de `defiler`, les valeurs renvoyées coïncident avec celles d'une `deque`.

**Étape 6 — Conclusion.**
$$\boxed{\text{ordre FIFO respecté ; pire cas }O(k)\text{ par appel, }O(m)\text{ pour }m\text{ opérations}}$$""",
r"""Résultats $1,2,3,4$ ; l'invariant relie les deux piles à la file ; $O(1)$ amorti par opération.""")
src('Piles et récursivité')

# ------------------------------------------------------------------ 7. Permutations
ex('i-rec-perm', M, 'Piles, files et récursivité', 2, 'Engendrer toutes les permutations', 20, r"""
On considère la fonction récursive :

```python
def permutations(L):
    if len(L) <= 1:
        return [L[:]]
    res = []
    for i in range(len(L)):
        reste = L[:i] + L[i + 1:]
        for p in permutations(reste):
            res.append([L[i]] + p)
    return res
```

1. Que renvoie `permutations([1, 2, 3])` ?
2. Montrer par récurrence que, pour une liste de $n\ge1$ éléments distincts, la fonction renvoie les $n!$ permutations, chacune une seule fois.
3. On note $A(n)$ le nombre d'appels à `permutations` déclenchés par un appel sur une liste de longueur $n$ (cet appel compris). Établir une relation entre $A(n)$ et $A(n-1)$, puis montrer que $A(n)=\sum_{k=1}^{n}\frac{n!}{k!}$.
4. En déduire que $A(n)\le(e-1)\,n!$.
""", r"""Les permutations commençant par `L[i]` sont `L[i]` suivi d'une permutation des autres éléments.""",
r"""Un appel sur $n\ge2$ éléments lance $n$ appels sur $n-1$ éléments : $A(n)=1+nA(n-1)$, $A(1)=1$.""",
r"""Divise la relation par $n!$ : la suite $A(n)/n!$ devient une somme télescopique.""",
r"""**Étape 1 — Analyse de l'énoncé.** On choisit le premier élément, puis on permute récursivement le reste : c'est la définition même d'une permutation.

**Étape 2 — Rappels du cours.**

> **Définition — Récursivité.** Une fonction récursive a un cas de base et un appel sur une donnée plus petite ; sa correction se prouve par récurrence.

> **Propriété — Série de l'exponentielle.** $\sum_{k=0}^{+\infty}\frac1{k!}=e$.

**Étape 3 — Stratégie.** Récurrence sur $n$ pour la correction ; relation de récurrence sur le nombre d'appels, divisée par $n!$.

**Étape 4 — Résolution détaillée.**

**4.1 Exemple.** `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]` : l'ordre lexicographique, car la liste de départ est triée.

**4.2 Correction.** Pour $n=1$, la fonction renvoie `[L[:]]`, la seule permutation. Supposons le résultat vrai pour $n-1\ge1$. Une permutation de $L$ s'écrit de façon unique `[L[i]] + p` où `L[i]` est son premier terme et `p` une permutation des $n-1$ autres éléments. Par hypothèse, `permutations(reste)` les fournit toutes, une seule fois : la double boucle produit chaque permutation exactement une fois, soit $n\times(n-1)!=n!$ listes.

**4.3 Nombre d'appels.** $A(1)=1$ et, pour $n\ge2$, $A(n)=1+nA(n-1)$. En posant $u_n=\frac{A(n)}{n!}$ :
$$u_n=\frac1{n!}+u_{n-1},\qquad u_1=1,$$
donc $u_n=\sum_{k=1}^{n}\frac1{k!}$ et $A(n)=\sum_{k=1}^{n}\frac{n!}{k!}$. Par exemple $A(2)=2+1=3$ et $A(3)=6+3+1=10$.

**4.4 Majoration.** $\sum_{k=1}^{n}\frac1{k!}\le\sum_{k=1}^{+\infty}\frac1{k!}=e-1$, d'où $A(n)\le(e-1)\,n!\approx1{,}72\,n!$. Comme le résultat contient lui-même $n!$ listes de longueur $n$, le coût total est $O(n\cdot n!)$ : inévitable quand on veut toutes les permutations.

**Étape 5 — Vérification.**

> **Vérification — Comptage.** En comptant les appels par programme, on trouve $A(4)=24+12+4+1=41$ et $1+4A(3)=41$.

**Étape 6 — Conclusion.**
$$\boxed{n!\text{ permutations ; }A(n)=\sum_{k=1}^n\frac{n!}{k!}\le(e-1)\,n!}$$""",
r"""Les $n!$ permutations dans l'ordre lexicographique ; $A(n)=1+nA(n-1)$ donne $A(n)=\sum_{k=1}^n n!/k!\le(e-1)n!$.""")
src('Piles et récursivité')

# ------------------------------------------------------------------ 8. Epsilon machine
ex('i-flot-eps', M, 'Nombres flottants', 1, 'Epsilon machine et absorption', 15, r"""
Les flottants Python sont des nombres en double précision : une mantisse de 53 bits (le premier, implicite, valant 1) et un exposant.

1. Pourquoi `0.1 + 0.2 == 0.3` vaut-il `False` ?
2. On considère :
```python
def epsilon():
    e = 1.0
    while 1.0 + e / 2 != 1.0:
        e = e / 2
    return e
```
Que renvoie cette fonction ? Interpréter le résultat.
3. Que valent `(1.0 + 1e-17) - 1.0` et `1e-17 + (1.0 - 1.0)` ? Qu'en conclure sur l'associativité de l'addition flottante ?
4. Proposer un test correct pour décider si deux flottants `x` et `y` sont « égaux ».
""", r"""$0{,}1$ n'a pas d'écriture binaire finie : il est arrondi.""",
r"""Le flottant qui suit $1$ est $1+2^{-52}$. Que devient $1+2^{-53}$ une fois arrondi ?""",
r"""Une addition flottante arrondit son résultat : un terme trop petit devant l'autre est absorbé.""",
r"""**Étape 1 — Analyse de l'énoncé.** Un flottant est un nombre dyadique $m\times2^e$ à mantisse bornée : tout résultat de calcul est arrondi au flottant le plus proche.

**Étape 2 — Rappels du cours.**

> **Propriété — Double précision.** Les flottants de $[1,2[$ sont les $1+k2^{-52}$ pour $0\le k<2^{52}$ ; l'erreur relative d'un arrondi est au plus $2^{-53}$.

> **Propriété — Représentation exacte.** Seuls les rationnels de la forme $\frac p{2^k}$ (et pas trop grands) sont représentés exactement.

**Étape 3 — Stratégie.** Raisonner sur l'écart entre $1$ et le flottant suivant, puis sur l'arrondi d'une somme.

**Étape 4 — Résolution détaillée.**

**4.1 Le test d'égalité.** $0{,}1=\frac1{10}$ a un développement binaire infini ($0{,}000110011\ldots_2$) : `0.1`, `0.2` et `0.3` sont des approximations. La somme des deux premières, arrondie, vaut `0.30000000000000004`, qui n'est pas le flottant le plus proche de $0{,}3$.

**4.2 Epsilon.** Les valeurs successives de `e` sont $1,\frac12,\frac14,\dots$ La boucle s'arrête dès que $1+\frac e2$ est arrondi à $1$. Pour $e=2^{-52}$, $1+2^{-53}$ est exactement au milieu de $1$ et $1+2^{-52}$ : l'arrondi « au pair » donne $1$. Pour $e=2^{-51}$, $1+2^{-52}$ est représentable. La fonction renvoie donc
$$\varepsilon=2^{-52}\approx2{,}22\times10^{-16},$$
l'écart entre $1$ et le flottant suivant : c'est `sys.float_info.epsilon`. Il fixe la précision relative : environ 16 chiffres significatifs.

**4.3 Absorption.** $1+10^{-17}$ est arrondi à $1$, car $10^{-17}<2^{-53}$ : `(1.0 + 1e-17) - 1.0` vaut `0.0`. Au contraire `1e-17 + (1.0 - 1.0)` vaut `1e-17`. Ces deux expressions sont égales en mathématiques : **l'addition flottante n'est pas associative**, et l'ordre des calculs compte (sommer les petits termes d'abord).

**4.4 Comparaison.** On remplace `x == y` par un test de proximité relative :

```python
def proches(x, y, tol=1e-9):
    return abs(x - y) <= tol * max(abs(x), abs(y), 1.0)
```

Le `1.0` évite qu'un test près de zéro devienne trop exigeant. La bibliothèque fournit `math.isclose(x, y)`.

**Étape 5 — Vérification.**

> **Vérification — Exécution.** `epsilon() == 2 ** -52` vaut `True` et `proches(0.1 + 0.2, 0.3)` vaut `True`.

**Étape 6 — Conclusion.**
$$\boxed{\varepsilon=2^{-52}\approx2{,}2\times10^{-16}\text{ ; addition non associative ; tester }|x-y|\le\text{tol}}$$""",
r"""`0.1` est arrondi ; `epsilon()` vaut $2^{-52}$ ; $1+10^{-17}$ est absorbé, l'addition n'est pas associative ; comparer avec une tolérance.""")
src('Divers : les nombres flottants')

# ------------------------------------------------------------------ 9. Tri à bulles et inversions
ex('i-tri-bulle', M, 'Tris', 2, 'Tri à bulles et inversions', 20, r"""
Une **inversion** d'une liste `L` est un couple d'indices $(i,j)$ avec $i<j$ et `L[i] > L[j]`.

```python
def tri_bulles(L):
    n = len(L)
    ech = 0
    for i in range(n - 1):
        fini = True
        for j in range(n - 1 - i):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                ech += 1
                fini = False
        if fini:
            break
    return ech
```

1. Montrer qu'après le tour d'indice $i$ de la boucle externe, les $i+1$ plus grands éléments sont à leur place définitive à la fin de la liste.
2. Montrer que la fonction renvoie le nombre d'inversions de la liste initiale.
3. Quel est le nombre maximal d'échanges pour une liste de longueur $n$ ? Pour quelle liste ?
4. En admettant que chaque couple $i<j$ forme une inversion avec probabilité $\frac12$ pour une permutation aléatoire, quel est le nombre moyen d'échanges ?
""", r"""Lors d'un passage, le plus grand élément de la partie non triée est poussé jusqu'au bout.""",
r"""Échanger deux voisins `L[j] > L[j+1]` supprime exactement une inversion et ne change pas les autres.""",
r"""Utilise la linéarité de l'espérance sur les $\binom n2$ couples.""",
r"""**Étape 1 — Analyse de l'énoncé.** Le tri à bulles échange des voisins mal ordonnés. Le nombre d'échanges mesure le désordre de la liste : c'est le nombre d'inversions.

**Étape 2 — Rappels du cours.**

> **Définition — Invariant.** Propriété conservée par chaque tour de boucle.

> **Propriété — Linéarité de l'espérance.** L'espérance d'une somme de variables aléatoires est la somme des espérances.

**Étape 3 — Stratégie.** Invariant de la boucle externe pour la correction ; effet d'un échange de voisins sur l'ensemble des inversions.

**Étape 4 — Résolution détaillée.**

**4.1 Correction.** Pendant le tour $i$, la boucle interne parcourt `L[0:n-i]` en déplaçant vers la droite le plus grand élément rencontré : à la fin du tour, le maximum de `L[0:n-i]` est en position $n-1-i$. Par récurrence, après le tour $i$, les positions $n-1-i,\dots,n-1$ contiennent les $i+1$ plus grands éléments, triés. Si un tour ne fait aucun échange, la partie restante est déjà triée (chaque voisin est ordonné) : l'arrêt anticipé est justifié.

**4.2 Échanges et inversions.** Si `L[j] > L[j+1]`, l'échange supprime l'inversion $(j,j+1)$. Pour tout autre couple, les deux valeurs sont les mêmes qu'avant ou se déplacent ensemble par rapport aux autres positions, donc leur ordre relatif est inchangé. Chaque échange diminue le nombre d'inversions de exactement 1, et une liste triée n'en a aucune : le nombre d'échanges est le nombre d'inversions initial.

**4.3 Maximum.** Une liste a au plus $\binom n2=\frac{n(n-1)}2$ inversions, atteint quand **tous** les couples sont inversés : la liste strictement décroissante.

**4.4 Moyenne.** En notant $X_{ij}$ l'indicatrice de l'inversion $(i,j)$, le nombre d'échanges est $\sum_{i<j}X_{ij}$, d'espérance
$$\sum_{i<j}\frac12=\frac{n(n-1)}4.$$
Le tri à bulles est donc quadratique en moyenne, comme dans le pire cas.

**Étape 5 — Vérification.**

> **Vérification — Exemples.** `tri_bulles([3, 1, 2])` renvoie $2$ (inversions $(3,1)$ et $(3,2)$) ; sur `[5, 4, 3, 2, 1]`, il renvoie $10=\binom52$ ; sur une liste triée, $0$ après un seul passage.

**Étape 6 — Conclusion.**
$$\boxed{\text{échanges}=\text{inversions}\le\frac{n(n-1)}2,\ \text{en moyenne }\frac{n(n-1)}4}$$""",
r"""Chaque échange de voisins retire exactement une inversion ; au plus $n(n-1)/2$ (liste décroissante), $n(n-1)/4$ en moyenne.""")
src('Tris')

# ------------------------------------------------------------------ 10. Compter les inversions en n log n
ex('i-tri-inv', M, 'Tris', 3, 'Compter les inversions en O(n log n)', 30, r"""
On reprend la notion d'inversion : un couple $(i,j)$, $i<j$, avec `L[i] > L[j]`. Compter les inversions en testant tous les couples coûte $O(n^2)$.

1. On coupe `L` en deux moitiés `A` et `B`. Montrer que le nombre d'inversions de `L` est la somme des inversions de `A`, de celles de `B` et du nombre de couples $(x,y)$, $x$ dans `A`, $y$ dans `B`, avec $x>y$.
2. Écrire une fonction récursive `tri_inv(L)` qui renvoie le couple (liste triée, nombre d'inversions), en comptant les inversions « croisées » pendant la fusion des deux moitiés triées.
3. Justifier le comptage pendant la fusion et donner la complexité.
4. Deux élèves classent les mêmes $n$ exercices par difficulté. Comment mesurer en $O(n\log n)$ le nombre de couples d'exercices sur lesquels ils sont en désaccord ?
""", r"""Une inversion a ses deux indices dans `A`, ses deux indices dans `B`, ou un dans chaque.""",
r"""Pendant la fusion, quand on prend `B[j]` parce qu'il est strictement plus petit que `A[i]`, il est aussi plus petit que tous les éléments restants de `A`.""",
r"""Pour la question 4, renumérote les exercices selon le classement du premier élève et lis le second classement dans cette numérotation.""",
r"""**Étape 1 — Analyse de l'énoncé.** On adapte le tri fusion : le tri permet de compter les inversions croisées en temps linéaire, et la récurrence de coût reste $C(n)=2C(n/2)+O(n)$.

**Étape 2 — Rappels du cours.**

> **Méthode — Diviser pour régner.** Si $C(n)=2C(n/2)+O(n)$, alors $C(n)=O(n\log n)$.

> **Propriété — Fusion.** Fusionner deux listes triées de longueurs $p$ et $q$ coûte $O(p+q)$.

**Étape 3 — Stratégie.** Trier et compter en même temps : chaque appel renvoie la liste triée et son nombre d'inversions.

**Étape 4 — Résolution détaillée.**

**4.1 Décomposition.** Un couple $i<j$ est soit dans `A` (les deux indices avant le milieu), soit dans `B`, soit croisé ($i$ dans `A`, $j$ dans `B`). Ces trois cas sont disjoints et couvrent tous les couples. Pour un couple croisé, la condition d'inversion ne dépend que des valeurs : trier `A` et `B` séparément ne change pas le nombre de couples croisés inversés.

**4.2 Programme.**

```python
def tri_inv(L):
    if len(L) <= 1:
        return L[:], 0
    m = len(L) // 2
    A, a = tri_inv(L[:m])
    B, b = tri_inv(L[m:])
    R, i, j, c = [], 0, 0, a + b
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            R.append(A[i])
            i += 1
        else:
            R.append(B[j])
            j += 1
            c += len(A) - i
    R += A[i:] + B[j:]
    return R, c
```

**4.3 Justification et coût.** Quand on prend `B[j]` parce que `A[i] > B[j]`, la liste `A` étant triée, tous les éléments `A[i:]` sont strictement plus grands que `B[j]` : ce sont exactement les $\texttt{len(A)} - i$ éléments de `A` qui forment une inversion croisée avec `B[j]` (ceux de `A[:i]` sont $\le$ `B[j]`, déjà placés). Chaque `B[j]` est compté une fois. Le test `<=` garantit que deux valeurs égales ne sont pas comptées.

Le coût vérifie $C(n)=C(\lfloor n/2\rfloor)+C(\lceil n/2\rceil)+O(n)$ (découpages et fusion linéaires), donc $C(n)=O(n\log n)$.

**4.4 Désaccord entre deux classements.** On numérote les exercices $0,\dots,n-1$ dans l'ordre du premier élève, puis on écrit la liste $P$ des numéros dans l'ordre du second. Deux exercices sont classés différemment si et seulement s'ils forment une inversion de $P$ : `tri_inv(P)[1]` donne le nombre de désaccords (distance de Kendall) en $O(n\log n)$.

**Étape 5 — Vérification.**

> **Vérification — Exemple.** `tri_inv([2, 4, 1, 3, 5])` renvoie `([1, 2, 3, 4, 5], 3)` : les inversions sont $(2,1)$, $(4,1)$ et $(4,3)$. Sur des listes aléatoires, le résultat coïncide avec le comptage naïf en $O(n^2)$.

**Étape 6 — Conclusion.**
$$\boxed{\text{inversions}=a+b+\sum(\texttt{len(A)}-i)\text{ pendant la fusion, en }O(n\log n)}$$""",
r"""Inversions de `A`, de `B` et croisées ; à chaque `B[j]` pris, ajouter `len(A) - i` ; $O(n\log n)$ ; distance de Kendall entre deux classements.""")
src('Tris')
