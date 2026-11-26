---
titre: Réduction des endomorphismes
---
## L'essentiel

Réduire un endomorphisme, c'est trouver une base où sa matrice est simple : diagonale si possible, triangulaire sinon. Les outils : valeurs propres, sous-espaces propres, polynôme caractéristique, polynômes annulateurs.

## Éléments propres

$\lambda$ est valeur propre de $u$ s'il existe $x \ne 0$ avec $u(x) = \lambda x$ ; $E_\lambda = \ker(u - \lambda\,\mathrm{id})$. Les sous-espaces propres sont en somme directe.

> **Définition — Polynôme caractéristique.** $\chi_A(X) = \det(XI_n - A)$ : unitaire de degré $n$, $\chi_A = X^n - \operatorname{tr}(A)X^{n-1} + \dots + (-1)^n\det A$. Ses racines sont les valeurs propres.

> **Théorème de Cayley-Hamilton.** $\chi_u(u) = 0$.

## Diagonalisation

[[fig:m2-reduction-1]]

> **Théorème — Critères de diagonalisabilité.** Il y a équivalence entre :
> - $u$ est diagonalisable ;
> - $E = \bigoplus_\lambda E_\lambda$ ;
> - $\chi_u$ est scindé et $\dim E_\lambda = m_\lambda$ (multiplicité) pour toute valeur propre ;
> - $u$ admet un polynôme annulateur **scindé à racines simples** (ou : $\pi_u$ est scindé à racines simples).

Condition suffisante : $\chi_u$ scindé à racines simples ($n$ valeurs propres distinctes).

## Trigonalisation

> **Théorème.** $u$ est trigonalisable si et seulement si $\chi_u$ est scindé. Sur $\mathbb C$, toute matrice est trigonalisable.

Alors $\operatorname{tr}A = \sum\lambda_i$ et $\det A = \prod\lambda_i$ (avec multiplicités).

## Applications

Puissances $A^n = PD^nP^{-1}$, suites récurrentes linéaires, systèmes différentiels $X' = AX$.

## Exemple corrigé

**Énoncé.** Diagonaliser $A = \begin{pmatrix}1 & 2\\ 2 & 1\end{pmatrix}$.

**Solution.** $\chi_A = (X - 1)^2 - 4 = (X - 3)(X + 1)$ : deux valeurs propres distinctes, donc $A$ est diagonalisable. $E_3 = \operatorname{Vect}\binom11$, $E_{-1} = \operatorname{Vect}\binom1{-1}$. Avec $P = \begin{pmatrix}1 & 1\\ 1 & -1\end{pmatrix}$ : $A = P\operatorname{diag}(3, -1)P^{-1}$.

## Pièges classiques

- Une valeur propre est associée à un vecteur propre **non nul**.
- $\chi_A$ scindé ne suffit pas pour diagonaliser : $\begin{pmatrix}1 & 1\\ 0 & 1\end{pmatrix}$ n'est pas diagonalisable.
- Sur $\mathbb R$, une matrice peut n'avoir aucune valeur propre (rotation).
