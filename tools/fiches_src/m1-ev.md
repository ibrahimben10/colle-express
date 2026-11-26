---
titre: Espaces vectoriels et applications linéaires
---
## L'essentiel

Un espace vectoriel est un ensemble où l'on peut additionner et multiplier par un scalaire. Les applications linéaires respectent ces opérations ; leur noyau et leur image décrivent leur injectivité et leur surjectivité. Projecteurs et symétries sont les exemples clés.

## Espaces vectoriels

> **Définition.** Un $\mathbb K$-espace vectoriel $E$ est un groupe abélien $(E, +)$ muni d'une multiplication externe vérifiant $1\cdot x = x$, $\lambda(\mu x) = (\lambda\mu)x$, $(\lambda + \mu)x = \lambda x + \mu x$, $\lambda(x + y) = \lambda x + \lambda y$.

Exemples : $\mathbb K^n$, $\mathbb K[X]$, $M_{n,p}(\mathbb K)$, $\mathcal F(I, \mathbb K)$, suites $\mathbb K^{\mathbb N}$, $\mathcal C^k(I)$.

### Sous-espaces vectoriels

> **Propriété — Caractérisation.** $F$ est un sous-espace de $E$ si $0 \in F$ et si pour tous $x, y \in F$ et $\lambda \in \mathbb K$, $\lambda x + y \in F$.

- L'intersection de sous-espaces en est un ; la réunion en général non.
- **Sous-espace engendré** $\operatorname{Vect}(x_1, \dots, x_p)$ : ensemble des combinaisons linéaires, plus petit sous-espace contenant les $x_i$.
- Méthode : montrer qu'un ensemble est un espace vectoriel en le voyant comme sous-espace d'un espace connu, ou comme noyau d'une application linéaire, ou comme un $\operatorname{Vect}$.

### Somme et somme directe

$F + G = \{x + y,\ x \in F, y \in G\}$. La somme est **directe** ($F \oplus G$) si $F \cap G = \{0\}$, ce qui équivaut à l'unicité de la décomposition. $F$ et $G$ sont **supplémentaires** si $E = F \oplus G$ : tout $x$ s'écrit de façon unique $x = x_F + x_G$.

## Familles de vecteurs

- **Libre** : $\sum\lambda_ix_i = 0 \Rightarrow$ tous les $\lambda_i = 0$. **Génératrice** : $E = \operatorname{Vect}(x_i)$. **Base** : libre et génératrice ; chaque vecteur a des coordonnées uniques.
- Une famille de polynômes de degrés échelonnés (deux à deux distincts) est libre.
- Une famille est liée si et seulement si l'un des vecteurs est combinaison linéaire des autres.

## Applications linéaires

> **Définition.** $u : E \to F$ est linéaire si $u(\lambda x + y) = \lambda u(x) + u(y)$. Endomorphisme si $F = E$, isomorphisme si bijective, automorphisme les deux. $\mathcal L(E, F)$ est un espace vectoriel ; $GL(E)$ est le groupe des automorphismes.

- La composée de linéaires est linéaire ; la réciproque d'un isomorphisme est linéaire.
- Une application linéaire est déterminée par l'image d'une base.

> **Propriété — Noyau et image.** $\ker u = \{x,\ u(x) = 0\}$ et $\operatorname{Im}u = u(E)$ sont des sous-espaces. $u$ est injective si et seulement si $\ker u = \{0\}$, surjective si et seulement si $\operatorname{Im}u = F$. Si $(e_i)$ engendre $E$, $\operatorname{Im}u = \operatorname{Vect}(u(e_i))$.

Une application linéaire injective transforme une famille libre en famille libre ; surjective, une famille génératrice en génératrice ; un isomorphisme, une base en base.

### Équations linéaires

Les solutions de $u(x) = b$ forment soit l'ensemble vide, soit $x_0 + \ker u$ (solution particulière plus solutions homogènes). C'est la structure commune aux systèmes linéaires, aux équations différentielles linéaires et aux suites récurrentes linéaires.

## Projecteurs et symétries

[[fig:m1-ev-1]]

> **Définition.** Si $E = F \oplus G$, la **projection** sur $F$ parallèlement à $G$ est $p : x = x_F + x_G \mapsto x_F$ ; la **symétrie** par rapport à $F$ parallèlement à $G$ est $s : x \mapsto x_F - x_G$.

> **Propriété.**
> - $p$ est un projecteur si et seulement si $p \circ p = p$ ; alors $E = \operatorname{Im}p \oplus \ker p$ et $\operatorname{Im}p = \ker(p - \mathrm{id})$.
> - $s$ est une symétrie si et seulement si $s \circ s = \mathrm{id}$ ; alors $E = \ker(s - \mathrm{id}) \oplus \ker(s + \mathrm{id})$.
> - $s = 2p - \mathrm{id}$, où $p$ est la projection sur le même $F$ parallèlement au même $G$.

## Exemple corrigé

**Énoncé.** Dans $E = \mathcal F(\mathbb R, \mathbb R)$, montrer que $E = \mathcal P \oplus \mathcal I$ (fonctions paires et impaires).

**Solution.** $\mathcal P$ et $\mathcal I$ sont des sous-espaces (contiennent 0, stables par combinaison linéaire). $\mathcal P \cap \mathcal I$ : $f(-x) = f(x) = -f(x)$ donne $f = 0$. Somme : $f = \frac{f(x) + f(-x)}{2} + \frac{f(x) - f(-x)}{2}$, paire plus impaire. Donc $E = \mathcal P \oplus \mathcal I$.

## Exemple corrigé (noyau et image)

**Énoncé.** $u : \mathbb R^3 \to \mathbb R^2$, $u(x, y, z) = (x + y, y - z)$. Noyau et image ?

**Solution.** $u(x, y, z) = 0 \Leftrightarrow x = -y$ et $z = y$ : $\ker u = \operatorname{Vect}(-1, 1, 1)$, donc $u$ n'est pas injective. $u(1, 0, 0) = (1, 0)$ et $u(0, 0, -1) = (0, 1)$ : $\operatorname{Im}u = \mathbb R^2$, $u$ est surjective.

## Pièges classiques

- $F \cup G$ n'est pas un sous-espace (sauf si l'un contient l'autre) ; c'est $F + G$ qui sert.
- Pour trois sous-espaces ou plus, $F_i \cap F_j = \{0\}$ deux à deux ne suffit pas pour que la somme soit directe.
- Un supplémentaire n'est pas unique, et ce n'est pas le complémentaire ensembliste.
