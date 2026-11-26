---
titre: Réduction des endomorphismes
---
## L'essentiel

Réduire un endomorphisme, c'est trouver une base où sa matrice est simple : diagonale si possible, triangulaire sinon. Les outils sont les éléments propres, le polynôme caractéristique, les polynômes annulateurs (Cayley-Hamilton, polynôme minimal) et le lemme des noyaux.

## Éléments propres

- $\lambda$ est **valeur propre** de $u$ s'il existe $x \ne 0$ avec $u(x) = \lambda x$ ; $x$ est un vecteur propre. Le **spectre** $\operatorname{Sp}(u)$ est l'ensemble des valeurs propres.
- Sous-espace propre $E_\lambda(u) = \ker(u - \lambda\,\mathrm{id})$ ; $\lambda$ est valeur propre si et seulement si $u - \lambda\,\mathrm{id}$ n'est pas injectif.
- 0 est valeur propre si et seulement si $u$ n'est pas injectif.

> **Propriété.** Des sous-espaces propres associés à des valeurs propres distinctes sont en somme directe ; une famille de vecteurs propres associés à des valeurs propres distinctes est libre.

## Polynôme caractéristique

> **Définition.** $\chi_A(X) = \det(XI_n - A)$ : unitaire de degré $n$, $\chi_A = X^n - \operatorname{tr}(A)X^{n-1} + \dots + (-1)^n\det A$. Ses racines sont les valeurs propres. Deux matrices semblables ont le même polynôme caractéristique.

- Multiplicité $m_\lambda$ de $\lambda$ comme racine de $\chi_u$ : $1 \le \dim E_\lambda \le m_\lambda$.
- Pour $n = 2$ : $\chi_A = X^2 - \operatorname{tr}(A)X + \det A$.
- Le polynôme caractéristique d'un endomorphisme induit sur un sous-espace stable divise $\chi_u$.

> **Théorème de Cayley-Hamilton.** $\chi_u(u) = 0$ ; donc $\pi_u$ divise $\chi_u$.

$\pi_u$ et $\chi_u$ ont les mêmes racines (les valeurs propres).

## Diagonalisation

[[fig:m2-reduction-1]]

$u$ est **diagonalisable** s'il existe une base de vecteurs propres ; $A$ l'est si elle est semblable à une matrice diagonale : $A = PDP^{-1}$, les colonnes de $P$ étant des vecteurs propres.

> **Théorème — Critères de diagonalisabilité.** Il y a équivalence entre :
> - $u$ est diagonalisable ;
> - $E = \bigoplus_{\lambda\in\operatorname{Sp}(u)}E_\lambda$, ou $\sum\dim E_\lambda = n$ ;
> - $\chi_u$ est scindé et $\dim E_\lambda = m_\lambda$ pour toute valeur propre ;
> - $u$ admet un polynôme annulateur **scindé à racines simples** ;
> - $\pi_u$ est scindé à racines simples.

**Condition suffisante** : $\chi_u$ scindé à racines simples ($n$ valeurs propres distinctes).

Conséquences : un projecteur ($X^2 - X$), une symétrie ($X^2 - 1$) sont diagonalisables ; si $u$ est diagonalisable, l'endomorphisme induit sur un sous-espace stable l'est aussi.

> **Méthode — Diagonaliser.** Calculer $\chi_A$ et ses racines ; pour chaque $\lambda$, résoudre $(A - \lambda I)X = 0$ pour obtenir une base de $E_\lambda$ ; vérifier $\sum\dim E_\lambda = n$ ; former $P$ avec ces vecteurs, $D$ avec les valeurs propres dans le même ordre.

## Trigonalisation

> **Théorème.** $u$ est trigonalisable si et seulement si $\chi_u$ est scindé (si et seulement s'il a un annulateur scindé). Sur $\mathbb C$, toute matrice est trigonalisable.

Si $A$ est trigonalisable de valeurs propres $\lambda_1, \dots, \lambda_n$ (avec multiplicité) : $\operatorname{tr}A = \sum\lambda_i$, $\det A = \prod\lambda_i$, et $\operatorname{tr}(A^k) = \sum\lambda_i^k$.

- **Nilpotents** : $u$ est nilpotent si et seulement s'il est trigonalisable avec 0 pour seule valeur propre, si et seulement si $\chi_u = X^n$. L'indice de nilpotence est au plus $n$.
- **Sous-espaces caractéristiques** : si $\chi_u = \prod(X - \lambda_i)^{m_i}$, le lemme des noyaux donne $E = \bigoplus\ker(u - \lambda_i\mathrm{id})^{m_i}$ ; sur chacun, $u = \lambda_i\mathrm{id} + $ nilpotent (réduction en blocs triangulaires).

## Applications

- **Puissances** : $A^k = PD^kP^{-1}$, ou division euclidienne de $X^k$ par un annulateur.
- **Suites récurrentes** $X_{n+1} = AX_n$ : $X_n = A^nX_0$.
- **Systèmes différentiels** $X' = AX$ : poser $X = PY$, avec $Y' = DY$.
- **Commutant** : si $u$ a $n$ valeurs propres distinctes, les endomorphismes qui commutent avec $u$ sont les polynômes en $u$.

## Exemple corrigé

**Énoncé.** Diagonaliser $A = \begin{pmatrix}1 & 2\\ 2 & 1\end{pmatrix}$ et calculer $A^n$.

**Solution.** $\chi_A = X^2 - 2X - 3 = (X - 3)(X + 1)$ : deux valeurs propres distinctes, $A$ est diagonalisable. $E_3 = \operatorname{Vect}\binom11$, $E_{-1} = \operatorname{Vect}\binom1{-1}$. $P = \begin{pmatrix}1 & 1\\ 1 & -1\end{pmatrix}$, $A = P\operatorname{diag}(3, -1)P^{-1}$, d'où $A^n = \frac12\begin{pmatrix}3^n + (-1)^n & 3^n - (-1)^n\\ 3^n - (-1)^n & 3^n + (-1)^n\end{pmatrix}$.

## Exemple corrigé (polynôme annulateur)

**Énoncé.** $A \in M_n(\mathbb R)$ vérifie $A^3 = A$. Est-elle diagonalisable ?

**Solution.** $X^3 - X = X(X - 1)(X + 1)$ est scindé à racines simples sur $\mathbb R$ et annule $A$ : $A$ est diagonalisable, de valeurs propres dans $\{-1, 0, 1\}$.

## Pièges classiques

- Un vecteur propre est **non nul**.
- $\chi_A$ scindé ne suffit pas : $\begin{pmatrix}1 & 1\\ 0 & 1\end{pmatrix}$ n'est pas diagonalisable ($\dim E_1 = 1 < 2$).
- Sur $\mathbb R$, une matrice peut n'avoir aucune valeur propre (rotation d'angle $\frac\pi2$).
- Dans $A = PDP^{-1}$, l'ordre des colonnes de $P$ doit correspondre à l'ordre des valeurs propres dans $D$.
