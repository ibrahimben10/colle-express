---
titre: Espaces vectoriels et applications linéaires
---
## L'essentiel

Un espace vectoriel est un ensemble où l'on peut additionner et multiplier par un scalaire. Les applications linéaires préservent cette structure ; leur noyau et leur image sont des sous-espaces.

## Sous-espaces

> **Propriété — Caractérisation.** $F \subset E$ est un sous-espace vectoriel si $0 \in F$ et $\lambda x + \mu y \in F$ pour tous $x, y \in F$ et scalaires $\lambda, \mu$.

- $\operatorname{Vect}(x_1, \dots, x_p)$ : plus petit sous-espace contenant ces vecteurs (combinaisons linéaires).
- **Somme directe** $F \oplus G$ : tout vecteur de $F + G$ s'écrit de façon unique ; équivalent à $F \cap G = \{0\}$ (pour deux sous-espaces).
- **Supplémentaires** : $E = F \oplus G$.

## Familles

Famille **libre** (aucune combinaison linéaire non triviale nulle), **génératrice**, **base** (les deux à la fois : chaque vecteur a des coordonnées uniques).

## Applications linéaires

> **Définition.** $u : E \to F$ est linéaire si $u(\lambda x + \mu y) = \lambda u(x) + \mu u(y)$.

- $\ker u = \{x,\ u(x) = 0\}$ et $\operatorname{Im}u$ sont des sous-espaces ; $u$ injective $\Leftrightarrow \ker u = \{0\}$.
- Isomorphisme = application linéaire bijective ; endomorphisme = de $E$ dans $E$.

## Projecteurs et symétries

[[fig:m1-ev-1]]

> **Propriété.** $p$ est un projecteur ($p\circ p = p$) si et seulement si c'est la projection sur $\operatorname{Im}p$ parallèlement à $\ker p$, avec $E = \operatorname{Im}p \oplus \ker p$. $s$ est une symétrie ($s\circ s = \mathrm{id}$) si et seulement si $s = 2p - \mathrm{id}$.

## Exemple corrigé

**Énoncé.** Dans $E = \mathcal F(\mathbb R, \mathbb R)$, montrer que $E = \mathcal P \oplus \mathcal I$ (fonctions paires et impaires).

**Solution.** *Analyse* : si $f = g + h$ ($g$ paire, $h$ impaire), alors $f(-x) = g(x) - h(x)$, d'où $g(x) = \frac{f(x) + f(-x)}{2}$ et $h(x) = \frac{f(x) - f(-x)}{2}$ : unicité. *Synthèse* : ces $g$ et $h$ conviennent : existence. La somme est directe et vaut $E$.

## Pièges classiques

- Montrer qu'un ensemble est un sous-espace : ne pas oublier de vérifier qu'il est non vide (contient 0).
- $F \cup G$ n'est en général pas un sous-espace ; c'est $F + G$ qu'il faut considérer.
- Pour trois sous-espaces ou plus, intersections deux à deux nulles ne suffisent pas pour une somme directe.
