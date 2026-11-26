---
titre: Calculs algébriques et inégalités
---
## L'essentiel

Manipuler sommes et produits, coefficients binomiaux, inégalités, valeur absolue et partie entière ; résoudre des systèmes linéaires simples. Ce sont les outils de calcul utilisés dans tout le reste de l'année.

## Sommes et produits

### Règles

- Linéarité : $\sum(\lambda a_k + \mu b_k) = \lambda\sum a_k + \mu\sum b_k$.
- **Changement d'indice** : $\sum_{k=1}^{n}a_k = \sum_{j=0}^{n-1}a_{j+1}$ ; $\sum_{k=0}^na_{n-k} = \sum_{k=0}^na_k$.
- **Télescopage** : $\sum_{k=0}^{n-1}(a_{k+1} - a_k) = a_n - a_0$ ; de même $\prod\frac{a_{k+1}}{a_k} = \frac{a_n}{a_0}$.
- Sommes doubles : $\sum_{i,j}a_ib_j = \left(\sum a_i\right)\left(\sum b_j\right)$ ; $\sum_{1\le i\le j\le n}a_{i,j} = \sum_{j=1}^n\sum_{i=1}^ja_{i,j} = \sum_{i=1}^n\sum_{j=i}^na_{i,j}$.

### Sommes usuelles

| Somme | Valeur |
|---|---|
| $\sum_{k=1}^nk$ | $\frac{n(n+1)}{2}$ |
| $\sum_{k=1}^nk^2$ | $\frac{n(n+1)(2n+1)}{6}$ |
| $\sum_{k=1}^nk^3$ | $\left(\frac{n(n+1)}{2}\right)^2$ |
| $\sum_{k=0}^nq^k$ ($q \ne 1$) | $\frac{1 - q^{n+1}}{1 - q}$ |

> **Propriété — Factorisation.** $a^n - b^n = (a - b)\sum_{k=0}^{n-1}a^kb^{n-1-k}$.

## Coefficients binomiaux

$\binom nk = \frac{n!}{k!(n-k)!}$ pour $0 \le k \le n$ (et 0 sinon). C'est le nombre de parties à $k$ éléments d'un ensemble à $n$ éléments.

- Symétrie : $\binom nk = \binom n{n-k}$.
- **Pascal** : $\binom nk + \binom n{k+1} = \binom{n+1}{k+1}$.
- Formule « pion » : $k\binom nk = n\binom{n-1}{k-1}$.

> **Théorème — Binôme de Newton.** Pour $a$, $b$ qui commutent : $(a + b)^n = \sum_{k=0}^n\binom nka^kb^{n-k}$.

Conséquences : $\sum_k\binom nk = 2^n$, $\sum_k(-1)^k\binom nk = 0$ ($n \ge 1$).

## Inégalités

- Compatibilité de $\le$ avec l'addition ; avec la multiplication par un réel **positif** (un négatif renverse le sens).
- On ne soustrait pas et on ne divise pas des inégalités membre à membre.
- Une fonction croissante conserve le sens, décroissante le renverse ($x \mapsto \frac1x$ sur $]0, +\infty[$).
- **Inégalité arithmético-géométrique** (cas 2) : $\sqrt{ab} \le \frac{a + b}{2}$ pour $a, b \ge 0$, car $(\sqrt a - \sqrt b)^2 \ge 0$ ; et $2|ab| \le a^2 + b^2$.

### Valeur absolue

$|x| = \max(x, -x)$ ; $|xy| = |x||y|$ ; $|x| \le a \Leftrightarrow -a \le x \le a$ ; $|x - a| \le r \Leftrightarrow x \in [a - r, a + r]$.

> **Propriété — Inégalité triangulaire.** $\big||x| - |y|\big| \le |x + y| \le |x| + |y|$.

### Partie entière

$\lfloor x\rfloor$ est l'unique entier $n$ tel que $n \le x < n + 1$ ; donc $x - 1 < \lfloor x\rfloor \le x$. Attention : $\lfloor -1{,}5\rfloor = -2$.

## Systèmes linéaires

Opérations élémentaires sur les lignes (échange, multiplication par un scalaire **non nul**, ajout d'un multiple d'une autre ligne) : elles donnent un système équivalent. La **méthode du pivot de Gauss** ramène à un système échelonné ; l'ensemble des solutions est vide, un point, ou une infinité (paramétrée par les inconnues non principales).

## Exemple corrigé

**Énoncé.** Calculer $S_n = \sum_{k=1}^n\frac{1}{k(k + 1)}$ et $T_n = \sum_{k=0}^nk\binom nk$.

**Solution.** $\frac{1}{k(k + 1)} = \frac1k - \frac{1}{k + 1}$ : par télescopage, $S_n = 1 - \frac{1}{n + 1}$. Pour $T_n$, $k\binom nk = n\binom{n-1}{k-1}$, donc $T_n = n\sum_{j=0}^{n-1}\binom{n-1}j = n2^{n-1}$ (on peut aussi dériver $(1 + x)^n$ et prendre $x = 1$).

## Pièges classiques

- Bien compter le nombre de termes : $\sum_{k=p}^q$ en a $q - p + 1$.
- $\sum a_kb_k \ne \left(\sum a_k\right)\left(\sum b_k\right)$.
- Le binôme de Newton suppose que $a$ et $b$ **commutent** (attention aux matrices).
