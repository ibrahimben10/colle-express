---
titre: Matrices
---
## L'essentiel

Une matrice représente une application linéaire dans des bases choisies. Le produit matriciel correspond à la composée ; changer de base revient à multiplier par des matrices de passage.

## Calcul matriciel

- Produit : $(AB)_{ij} = \sum_kA_{ik}B_{kj}$ ; non commutatif en général.
- Transposée : ${}^t(AB) = {}^tB\,{}^tA$ ; inverse : $(AB)^{-1} = B^{-1}A^{-1}$.
- **Trace** : $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.

> **Propriété — Inversibilité.** Pour $A \in M_n(\mathbb K)$, il y a équivalence entre : $A$ inversible ; $\operatorname{rg}A = n$ ; $AX = 0 \Rightarrow X = 0$ ; $\det A \ne 0$ ; il existe $B$ avec $AB = I_n$.

## Matrice d'une application linéaire

La $j$-ième colonne de $\operatorname{Mat}_{\mathcal B, \mathcal C}(u)$ contient les coordonnées de $u(e_j)$ dans $\mathcal C$. $\operatorname{Mat}(v\circ u) = \operatorname{Mat}(v)\operatorname{Mat}(u)$.

## Changement de base

> **Formule.** Si $P$ est la matrice de passage de $\mathcal B$ à $\mathcal B'$ (colonnes = vecteurs de $\mathcal B'$ dans $\mathcal B$) : $X = PX'$ et, pour un endomorphisme, $A' = P^{-1}AP$.

Deux matrices sont **semblables** si elles représentent le même endomorphisme dans deux bases : même trace, même déterminant, même rang.

## Calcul de l'inverse

Pivot de Gauss sur $(A \mid I_n)$ jusqu'à $(I_n \mid A^{-1})$, ou résolution de $AX = Y$.

## Exemple corrigé

**Énoncé.** Calculer $A^n$ pour $A = \begin{pmatrix}1 & 1\\ 0 & 1\end{pmatrix}$.

**Solution.** $A = I + N$ avec $N = \begin{pmatrix}0 & 1\\ 0 & 0\end{pmatrix}$, $N^2 = 0$, et $I$ commute avec $N$. Par le binôme, $A^n = I + nN = \begin{pmatrix}1 & n\\ 0 & 1\end{pmatrix}$.

## Pièges classiques

- $AB = 0$ n'implique pas $A = 0$ ou $B = 0$.
- Le binôme ne s'applique que si les matrices commutent.
- Ne pas confondre la matrice de passage de $\mathcal B$ à $\mathcal B'$ et son inverse.
