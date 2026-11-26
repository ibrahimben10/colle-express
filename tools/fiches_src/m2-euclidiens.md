---
titre: Endomorphismes des espaces euclidiens
---
## L'essentiel

Dans un espace euclidien, deux familles d'endomorphismes sont centrales : les **isométries** (qui conservent la norme, matrices orthogonales) et les endomorphismes **autoadjoints** (matrices symétriques), diagonalisables dans une base orthonormée (théorème spectral).

## Adjoint

> **Propriété.** Pour $u \in \mathcal L(E)$, il existe un unique $u^* \in \mathcal L(E)$ tel que $\langle u(x), y\rangle = \langle x, u^*(y)\rangle$ pour tous $x, y$. Dans une base **orthonormée**, $\operatorname{Mat}(u^*) = {}^t\operatorname{Mat}(u)$.

$(u^*)^* = u$, $(u \circ v)^* = v^* \circ u^*$. Si $F$ est stable par $u$, $F^\perp$ est stable par $u^*$.

## Isométries vectorielles

> **Propriété.** Pour $u \in \mathcal L(E)$, il y a équivalence entre :
> - $u$ conserve la norme : $\|u(x)\| = \|x\|$ ;
> - $u$ conserve le produit scalaire ;
> - $u^* \circ u = \mathrm{id}$ ;
> - $u$ transforme une (toute) base orthonormée en base orthonormée ;
> - sa matrice $A$ dans une base orthonormée vérifie ${}^tAA = I_n$ (colonnes orthonormées).

- $O(E)$ et $O_n(\mathbb R)$ sont des groupes ; $\det A = \pm1$ ; $SO_n(\mathbb R)$ : déterminant 1 (rotations).
- Les valeurs propres réelles d'une isométrie valent $\pm1$. Si $F$ est stable, $F^\perp$ aussi.
- Symétries orthogonales (et réflexions) : symétries par rapport à $F$ parallèlement à $F^\perp$.
- Une matrice de passage entre bases orthonormées est orthogonale : $P^{-1} = {}^tP$.

### Dimension 2

$SO_2(\mathbb R)$ : rotations $R_\theta = \begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}$, avec $R_\theta R_{\theta'} = R_{\theta+\theta'}$ (groupe commutatif). Les éléments de déterminant $-1$ sont les réflexions $\begin{pmatrix}\cos\theta & \sin\theta\\ \sin\theta & -\cos\theta\end{pmatrix}$.

### Dimension 3

Une rotation $r \ne \mathrm{id}$ a un **axe** $D = \ker(r - \mathrm{id})$ (droite) ; orienté par un vecteur unitaire $a$, sa matrice dans une base orthonormée directe $(a, b, c)$ est $\begin{pmatrix}1 & 0 & 0\\ 0 & \cos\theta & -\sin\theta\\ 0 & \sin\theta & \cos\theta\end{pmatrix}$. On lit $\cos\theta$ sur la trace : $\operatorname{tr} = 1 + 2\cos\theta$ ; le signe de $\sin\theta$ est celui de $\det(a, x, r(x))$ pour $x \notin D$.

### Réduction des isométries

> **Théorème.** Toute isométrie d'un espace euclidien a, dans une base orthonormée convenable, une matrice diagonale par blocs, avec des blocs $(1)$, $(-1)$ et des rotations $R_\theta$ de taille 2.

## Endomorphismes autoadjoints

$u$ est **autoadjoint** (symétrique) si $u^* = u$ : $\langle u(x), y\rangle = \langle x, u(y)\rangle$ ; dans une base orthonormée, sa matrice est symétrique. Exemple : les projecteurs orthogonaux.

[[fig:m2-euclidiens-1]]

> **Théorème spectral.** Tout endomorphisme autoadjoint d'un espace euclidien est diagonalisable dans une base **orthonormée** ; ses sous-espaces propres sont orthogonaux. Version matricielle : si $S \in S_n(\mathbb R)$, il existe $P \in O_n(\mathbb R)$ et $D$ diagonale réelle avec $S = PD\,{}^tP$.

### Matrices symétriques positives

- $S \in S_n^+(\mathbb R)$ si ${}^tXSX \ge 0$ pour tout $X$ ; $S_n^{++}$ si ${}^tXSX > 0$ pour $X \ne 0$.
- $S \in S_n^+ \Leftrightarrow \operatorname{Sp}(S) \subset \mathbb R_+$ ; $S \in S_n^{++} \Leftrightarrow \operatorname{Sp}(S) \subset \mathbb R_+^*$.
- Pour toute $A$, ${}^tAA \in S_n^+$.
- Encadrement de Rayleigh : $\lambda_{\min}\|X\|^2 \le {}^tXSX \le \lambda_{\max}\|X\|^2$.

## Exemple corrigé

**Énoncé.** Montrer que pour $A \in M_n(\mathbb R)$, ${}^tAA$ est symétrique positive, et qu'elle est définie positive si et seulement si $A$ est inversible.

**Solution.** ${}^t({}^tAA) = {}^tAA$. Pour $X \in \mathbb R^n$, ${}^tX{}^tAAX = \|AX\|^2 \ge 0$, avec égalité si et seulement si $AX = 0$. Donc ${}^tAA \in S_n^+$, et ${}^tAA \in S_n^{++}$ si et seulement si $\ker A = \{0\}$, c'est-à-dire $A$ inversible.

## Exemple corrigé (rotation en dimension 3)

**Énoncé.** Nature de $A = \begin{pmatrix}0 & 0 & 1\\ 1 & 0 & 0\\ 0 & 1 & 0\end{pmatrix}$.

**Solution.** Ses colonnes sont orthonormées : $A \in O_3$, et $\det A = 1$ : c'est une rotation. Axe : $AX = X$ donne $x = y = z$, axe dirigé par $a = \frac{1}{\sqrt3}(1, 1, 1)$. $\operatorname{tr}A = 0 = 1 + 2\cos\theta$, $\cos\theta = -\frac12$. Avec $x = e_1$ : $\det(a, e_1, Ae_1) = \det(a, e_1, e_2) > 0$, donc $\theta = \frac{2\pi}{3}$.

## Pièges classiques

- Une matrice orthogonale n'est pas forcément symétrique ; son inverse est sa **transposée**.
- Le théorème spectral est faux pour les matrices symétriques **complexes**.
- « Positive » porte sur la forme ${}^tXSX$, pas sur les coefficients.
- La formule $\operatorname{Mat}(u^*) = {}^t\operatorname{Mat}(u)$ exige une base orthonormée.
