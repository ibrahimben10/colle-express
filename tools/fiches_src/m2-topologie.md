---
titre: Espaces vectoriels normés
---
## L'essentiel

Une norme permet de parler de distance, de limite et de continuité dans un espace vectoriel. Ouverts, fermés, compacts et connexité par arcs généralisent les intervalles. En dimension finie, toutes les normes sont équivalentes, les compacts sont les fermés bornés et les applications linéaires sont continues.

## Normes et distances

> **Définition.** Une norme vérifie : $\|x\| = 0 \Rightarrow x = 0$ ; $\|\lambda x\| = |\lambda|\|x\|$ ; $\|x + y\| \le \|x\| + \|y\|$. Distance associée $d(x, y) = \|x - y\|$ ; $\big|\|x\| - \|y\|\big| \le \|x - y\|$.

[[fig:m2-topologie-1]]

- Sur $\mathbb K^n$ : $\|x\|_1 = \sum|x_i|$, $\|x\|_2 = \sqrt{\sum|x_i|^2}$, $\|x\|_\infty = \max|x_i|$.
- Sur $\mathcal C([a, b])$ : $\|f\|_\infty = \sup|f|$, $\|f\|_1 = \int|f|$, $\|f\|_2 = \sqrt{\int|f|^2}$.
- Norme d'algèbre sur $M_n$ ou norme subordonnée : $\|AB\| \le \|A\|\|B\|$.
- Boules ouvertes $B(a, r)$, fermées, sphères ; parties bornées ; boules convexes.
- **Normes équivalentes** : $\alpha N_1 \le N_2 \le \beta N_1$ ; elles ont les mêmes suites convergentes, les mêmes ouverts, les mêmes parties bornées. Par exemple $\|x\|_\infty \le \|x\|_2 \le \|x\|_1 \le n\|x\|_\infty$ sur $\mathbb K^n$.

## Suites

$x_n \to \ell$ si $\|x_n - \ell\| \to 0$ ; unicité, suites bornées, suites extraites, valeurs d'adhérence. Dans un produit, convergence composante par composante.

## Topologie

- **Ouvert** : contient une boule autour de chacun de ses points. Réunion quelconque et intersection finie d'ouverts sont des ouverts.
- **Fermé** : complémentaire d'un ouvert. Caractérisation séquentielle : $F$ est fermé si et seulement si toute suite de $F$ qui converge a sa limite dans $F$.
- **Intérieur** $\mathring A$ (plus grand ouvert inclus), **adhérence** $\bar A$ (ensemble des limites de suites de $A$), frontière $\bar A \setminus \mathring A$.
- $A$ est **dense** dans $E$ si $\bar A = E$ : $\mathbb Q$ dans $\mathbb R$, $GL_n(\mathbb K)$ dans $M_n(\mathbb K)$, les polynômes dans $\mathcal C([a, b])$ pour $\|\cdot\|_\infty$ (Weierstrass).

## Limites et continuité

- Caractérisation séquentielle de la limite et de la continuité.
- $f$ continue $\Leftrightarrow$ l'image réciproque de tout ouvert (fermé) est un ouvert (fermé) : $\{x,\ f(x) = 0\}$, $\{x,\ f(x) \le 0\}$ sont fermés, $\{x,\ f(x) > 0\}$ est ouvert.
- Deux fonctions continues égales sur une partie dense sont égales.
- **Lipschitzienne** $\Rightarrow$ uniformément continue $\Rightarrow$ continue. La norme est 1-lipschitzienne ; $x \mapsto d(x, A)$ aussi.

> **Théorème — Applications linéaires continues.** $u$ linéaire est continue si et seulement s'il existe $k$ avec $\|u(x)\| \le k\|x\|$ pour tout $x$. On définit alors la norme subordonnée $|||u||| = \sup_{x\ne0}\frac{\|u(x)\|}{\|x\|}$. Les applications multilinéaires en dimension finie (déterminant, produit matriciel) sont continues.

## Compacité

$K$ est **compact** si toute suite de $K$ admet une valeur d'adhérence dans $K$ (Bolzano-Weierstrass). Un compact est fermé et borné ; un fermé inclus dans un compact est compact ; un produit de compacts est compact.

> **Théorème.** L'image d'un compact par une application continue est compacte. Une fonction continue sur un compact non vide, à valeurs réelles, est bornée et atteint ses bornes. Une fonction continue sur un compact y est uniformément continue (Heine).

## Connexité par arcs

$A$ est connexe par arcs si deux points de $A$ sont toujours reliés par un chemin continu dans $A$. Les convexes (et les parties étoilées) le sont ; dans $\mathbb R$, ce sont les intervalles. L'image d'un connexe par arcs par une application continue est connexe par arcs (généralisation du TVI).

## Dimension finie

> **Théorème.** En dimension finie : toutes les normes sont équivalentes ; les compacts sont les fermés bornés ; les sous-espaces sont fermés ; toute application linéaire (ou polynomiale en les coordonnées) est continue ; une suite bornée a une valeur d'adhérence.

## Exemple corrigé

**Énoncé.** Montrer que $GL_n(\mathbb R)$ est un ouvert dense de $M_n(\mathbb R)$.

**Solution.** $\det$ est polynomiale en les coefficients, donc continue, et $GL_n = \det^{-1}(\mathbb R^*)$ : ouvert. Densité : pour $A \in M_n$, $\det(A - \frac1pI_n)$ est un polynôme en $\frac1p$ qui n'a qu'un nombre fini de racines, donc $A - \frac1pI_n \in GL_n$ pour $p$ assez grand, et cette suite tend vers $A$.

## Exemple corrigé (normes non équivalentes)

**Énoncé.** Sur $\mathcal C([0, 1])$, $\|\cdot\|_1$ et $\|\cdot\|_\infty$ sont-elles équivalentes ?

**Solution.** $\|f\|_1 \le \|f\|_\infty$. Mais $f_n(x) = x^n$ vérifie $\|f_n\|_\infty = 1$ et $\|f_n\|_1 = \frac{1}{n + 1} \to 0$ : il n'existe pas de $\beta$ avec $\|f\|_\infty \le \beta\|f\|_1$. Elles ne sont pas équivalentes (dimension infinie).

## Pièges classiques

- Une partie peut n'être ni ouverte ni fermée ($[0, 1[$), ou les deux ($\emptyset$, $E$).
- En dimension infinie, un fermé borné n'est pas forcément compact et une application linéaire n'est pas forcément continue.
- La notion de partie bornée ou de suite convergente dépend de la norme en dimension infinie.
