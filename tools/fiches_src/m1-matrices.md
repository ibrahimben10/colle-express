---
titre: Matrices
---
## L'essentiel

Une matrice représente une application linéaire dans des bases choisies ; le produit matriciel correspond à la composition. On calcule avec les matrices (inverse, rang, changement de base) pour résoudre des problèmes d'algèbre linéaire.

## Calcul matriciel

- $M_{n,p}(\mathbb K)$ est un espace de dimension $np$, de base canonique $(E_{ij})$.
- Produit : $(AB)_{ij} = \sum_kA_{ik}B_{kj}$ ; il est associatif, distributif, **non commutatif**, et a des diviseurs de zéro.
- Transposée : ${}^t(AB) = {}^tB\,{}^tA$. Matrices symétriques (${}^tA = A$), antisymétriques ; $M_n = S_n \oplus A_n$.
- Matrices remarquables : diagonales, triangulaires (stables par produit), nilpotentes.
- Puissances : binôme de Newton si $A$ et $B$ commutent, par exemple $(I + N)^k$ avec $N$ nilpotente.
- **Trace** : $\operatorname{tr}A = \sum a_{ii}$, linéaire, et $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.

## Inversibilité

$A \in M_n(\mathbb K)$ est inversible s'il existe $B$ avec $AB = BA = I_n$ ; en dimension finie, $AB = I_n$ suffit. $GL_n(\mathbb K)$ est un groupe : $(AB)^{-1} = B^{-1}A^{-1}$, $({}^tA)^{-1} = {}^t(A^{-1})$.

> **Propriété — Caractérisations.** $A$ est inversible si et seulement si : ses colonnes forment une base ; $AX = 0 \Rightarrow X = 0$ ; $\operatorname{rg}A = n$ ; $\det A \ne 0$.

- Inverse d'une matrice $2\times2$ : $\begin{pmatrix}a & b\\ c & d\end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix}d & -b\\ -c & a\end{pmatrix}$.
- Méthode : résoudre $AX = Y$ (on obtient $X = A^{-1}Y$) ou pivot de Gauss sur $(A \mid I_n)$ ; ou un polynôme annulateur ($A^2 - 3A + 2I = 0$ donne $A\cdot\frac{3I - A}{2} = I$).
- Une matrice triangulaire est inversible si et seulement si ses coefficients diagonaux sont non nuls.

## Matrices et applications linéaires

$\operatorname{Mat}_{\mathcal B, \mathcal C}(u)$ : la colonne $j$ contient les coordonnées de $u(e_j)$ dans $\mathcal C$. Alors $Y = AX$ traduit $y = u(x)$, et $\operatorname{Mat}(v \circ u) = \operatorname{Mat}(v)\operatorname{Mat}(u)$. L'application canoniquement associée à $A$ est $X \mapsto AX$ ; $\ker A$ et $\operatorname{Im}A$ (engendrée par les colonnes).

## Changement de base

La matrice de passage $P = P_{\mathcal B \to \mathcal B'}$ a pour colonnes les coordonnées des vecteurs de $\mathcal B'$ dans $\mathcal B$. On a $X = PX'$.

> **Théorème — Formule de changement de base.** Pour un endomorphisme, $A' = P^{-1}AP$ ; pour $u \in \mathcal L(E, F)$, $A' = Q^{-1}AP$.

Deux matrices **semblables** ($A' = P^{-1}AP$) représentent le même endomorphisme ; elles ont même trace, même rang, même déterminant. Deux matrices sont **équivalentes** si et seulement si elles ont le même rang ; toute matrice de rang $r$ est équivalente à $J_r = \begin{pmatrix}I_r & 0\\ 0 & 0\end{pmatrix}$.

## Rang d'une matrice

$\operatorname{rg}A$ = rang des colonnes = rang des lignes ($\operatorname{rg}{}^tA = \operatorname{rg}A$). Les opérations élémentaires ne changent pas le rang ; on calcule le rang par pivot de Gauss.

## Systèmes linéaires

$AX = B$ : compatible si et seulement si $B \in \operatorname{Im}A$ ; solutions $X_0 + \ker A$. Système de Cramer ($A$ inversible) : solution unique $X = A^{-1}B$. Opérations élémentaires = multiplication à gauche par des matrices inversibles (transvections, dilatations, permutations).

## Matrices par blocs

Le produit par blocs fonctionne comme le produit ordinaire si les tailles sont compatibles. Une matrice triangulaire par blocs traduit un sous-espace stable.

## Exemple corrigé

**Énoncé.** $A = \begin{pmatrix}1 & 1\\ 0 & 1\end{pmatrix}$. Calculer $A^n$.

**Solution.** $A = I + N$ avec $N = \begin{pmatrix}0 & 1\\ 0 & 0\end{pmatrix}$, $N^2 = 0$, et $I$ commute avec $N$. Binôme : $A^n = I + nN = \begin{pmatrix}1 & n\\ 0 & 1\end{pmatrix}$.

## Exemple corrigé (changement de base)

**Énoncé.** $u$ endomorphisme de $\mathbb R^2$ de matrice $A = \begin{pmatrix}3 & -2\\ 1 & 0\end{pmatrix}$. Matrice dans la base $e_1' = (1, 1)$, $e_2' = (2, 1)$ ?

**Solution.** $u(e_1') = (1, 1) = e_1'$ et $u(e_2') = (4, 2) = 2e_2'$. Donc $A' = \operatorname{diag}(1, 2)$, et $A = PA'P^{-1}$ avec $P = \begin{pmatrix}1 & 2\\ 1 & 1\end{pmatrix}$.

## Pièges classiques

- $AB \ne BA$ en général ; $AB = 0$ n'implique pas $A = 0$ ou $B = 0$.
- $(A + B)^2 = A^2 + AB + BA + B^2$.
- $\operatorname{tr}(ABC) = \operatorname{tr}(CAB)$, mais pas forcément $\operatorname{tr}(ACB)$.
