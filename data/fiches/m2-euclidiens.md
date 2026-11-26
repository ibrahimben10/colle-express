---
titre: Endomorphismes des espaces euclidiens
---
## L'essentiel

Dans un espace euclidien, deux familles d'endomorphismes jouent un rôle central : les **isométries** (qui conservent la norme) et les endomorphismes **autoadjoints** (symétriques), diagonalisables en base orthonormée.

## Adjoint

Pour $u \in \mathcal L(E)$, il existe un unique $u^*$ tel que $\langle u(x), y\rangle = \langle x, u^*(y)\rangle$ ; en base orthonormée, $\operatorname{Mat}(u^*) = {}^t\operatorname{Mat}(u)$.

## Isométries vectorielles

> **Propriété.** Pour $u \in \mathcal L(E)$, il y a équivalence entre : $u$ conserve la norme ; $u$ conserve le produit scalaire ; $u$ transforme une base orthonormée en base orthonormée ; sa matrice $A$ en base orthonormée vérifie ${}^tAA = I_n$ (matrice **orthogonale**).

$O_n(\mathbb R)$ est un groupe ; $\det A = \pm1$. $SO_n(\mathbb R)$ : déterminant 1.

- En dimension 2 : $SO_2$ = rotations $\begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}$ ; les autres éléments de $O_2$ sont des réflexions.
- En dimension 3 : une rotation a un axe (vecteur invariant) ; son angle se lit sur la trace : $\operatorname{tr} = 1 + 2\cos\theta$.

## Théorème spectral

[[fig:m2-euclidiens-1]]

> **Théorème spectral.** Tout endomorphisme autoadjoint d'un espace euclidien est diagonalisable dans une base orthonormée. Version matricielle : si $S \in S_n(\mathbb R)$, il existe $P \in O_n(\mathbb R)$ et $D$ diagonale réelle avec $S = PD\,{}^tP$.

$S$ est **positive** ($S \in S_n^+$) si ${}^tXSX \ge 0$ pour tout $X$, ce qui équivaut à : toutes ses valeurs propres sont positives. Définie positive : valeurs propres strictement positives.

## Exemple corrigé

**Énoncé.** Montrer que pour $A \in M_n(\mathbb R)$, ${}^tAA$ est symétrique positive.

**Solution.** ${}^t({}^tAA) = {}^tAA$ : symétrique. Pour $X \in \mathbb R^n$, ${}^tX({}^tAA)X = {}^t(AX)(AX) = \|AX\|^2 \ge 0$ : positive. Ses valeurs propres sont donc positives.

## Pièges classiques

- Une matrice orthogonale n'est pas forcément symétrique, ni l'inverse.
- Le théorème spectral est faux pour les matrices symétriques **complexes**.
- « Positive » porte sur la forme quadratique, pas sur les coefficients.
