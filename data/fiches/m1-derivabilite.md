---
titre: Dérivabilité
---
## L'essentiel

La dérivée mesure la pente de la tangente. Les théorèmes de Rolle et des accroissements finis relient la dérivée aux variations de la fonction ; la convexité décrit la position de la courbe par rapport à ses cordes et ses tangentes.

## Dérivée en un point

> **Définition.** $f$ est dérivable en $a$ si le taux d'accroissement $\frac{f(x) - f(a)}{x - a}$ a une limite finie $f'(a)$ quand $x \to a$. De façon équivalente : $f(a + h) = f(a) + f'(a)h + o(h)$ (développement limité à l'ordre 1).

- Dérivable en $a$ implique continue en $a$ ; la réciproque est fausse ($|x|$ en 0).
- Tangente : $y = f(a) + f'(a)(x - a)$. Dérivées à gauche et à droite ; point anguleux si elles diffèrent.
- Opérations : $(fg)' = f'g + fg'$, $\left(\frac fg\right)' = \frac{f'g - fg'}{g^2}$, $(g \circ f)' = f'\cdot g' \circ f$, $(f^{-1})' = \frac{1}{f' \circ f^{-1}}$ (si $f'$ ne s'annule pas).

### Dérivées successives

$f$ est de classe $\mathcal C^n$ si elle est $n$ fois dérivable et $f^{(n)}$ continue ; $\mathcal C^\infty$ si elle l'est pour tout $n$.

> **Théorème — Formule de Leibniz.** $(fg)^{(n)} = \sum_{k=0}^n\binom nkf^{(k)}g^{(n-k)}$.

## Extremums

> **Propriété.** Si $f$ est dérivable en un point $a$ **intérieur** à l'intervalle et y admet un extremum local, alors $f'(a) = 0$.

La réciproque est fausse ($x^3$ en 0). Aux bornes de l'intervalle, un extremum peut avoir une dérivée non nulle.

## Rolle et accroissements finis

> **Théorème de Rolle.** Si $f$ est continue sur $[a, b]$, dérivable sur $]a, b[$ et $f(a) = f(b)$, il existe $c \in ]a, b[$ avec $f'(c) = 0$.

[[fig:m1-derivabilite-1]]

> **Théorème des accroissements finis.** Si $f$ est continue sur $[a, b]$ et dérivable sur $]a, b[$, il existe $c \in ]a, b[$ tel que $f(b) - f(a) = f'(c)(b - a)$.

> **Théorème — Inégalité des accroissements finis.** Si $|f'| \le M$ sur un intervalle $I$, alors $|f(x) - f(y)| \le M|x - y|$ : $f$ est $M$-lipschitzienne. Cette version reste vraie pour les fonctions à valeurs **complexes** (contrairement à l'égalité).

### Conséquences

- **Monotonie** : sur un intervalle, $f' \ge 0 \Leftrightarrow f$ croissante ; $f' > 0$ (sauf en un nombre fini de points) $\Rightarrow f$ strictement croissante ; $f' = 0 \Leftrightarrow f$ constante.
- **Théorème de la limite de la dérivée** : si $f$ est continue sur $I$, dérivable sur $I \setminus \{a\}$ et $f'(x) \to \ell$ en $a$, alors $f$ est dérivable en $a$ et $f'(a) = \ell$ (et $f'$ est continue en $a$). Outil pour les prolongements $\mathcal C^1$.
- Suites récurrentes : si $|f'| \le k < 1$ sur un intervalle stable contenant un point fixe $\ell$, alors $|u_n - \ell| \le k^n|u_0 - \ell|$.

## Convexité

[[fig:m1-derivabilite-2]]

> **Définition.** $f$ est convexe sur $I$ si pour tous $x, y \in I$ et $t \in [0, 1]$ : $f(tx + (1 - t)y) \le tf(x) + (1 - t)f(y)$ (la courbe est sous ses cordes).

- Équivalent : les pentes $\frac{f(y) - f(x)}{y - x}$ sont croissantes (en chacune des variables).
- Si $f$ est dérivable : $f$ convexe $\Leftrightarrow$ $f'$ croissante $\Leftrightarrow$ la courbe est au-dessus de ses tangentes. Si $f$ est deux fois dérivable : $f$ convexe $\Leftrightarrow f'' \ge 0$.
- **Inégalité de Jensen** : $f\left(\sum\lambda_ix_i\right) \le \sum\lambda_if(x_i)$ pour $\lambda_i \ge 0$, $\sum\lambda_i = 1$.

Inégalités classiques obtenues par convexité : $e^x \ge 1 + x$, $\ln x \le x - 1$, $\sin x \ge \frac2\pi x$ sur $[0, \frac\pi2]$ (concavité), inégalité arithmético-géométrique (concavité de $\ln$).

## Exemple corrigé

**Énoncé.** Montrer que pour $0 < a < b$ : $\frac{b - a}{b} < \ln\frac ba < \frac{b - a}{a}$.

**Solution.** On applique les accroissements finis à $\ln$ sur $[a, b]$ : il existe $c \in ]a, b[$ avec $\ln b - \ln a = \frac{b - a}{c}$. Comme $a < c < b$, $\frac1b < \frac1c < \frac1a$, d'où l'encadrement.

## Exemple corrigé (Rolle)

**Énoncé.** Montrer qu'un polynôme réel de degré $n$ à $n$ racines réelles distinctes a une dérivée à $n - 1$ racines réelles distinctes.

**Solution.** Entre deux racines consécutives $x_i < x_{i+1}$, Rolle donne une racine de $P'$ dans $]x_i, x_{i+1}[$. Cela fournit $n - 1$ racines distinctes de $P'$, qui est de degré $n - 1$ : ce sont toutes ses racines.

## Pièges classiques

- Rolle et les accroissements finis (égalité) sont faux pour les fonctions complexes : $e^{ix}$ sur $[0, 2\pi]$.
- $f'(a) = 0$ ne donne pas forcément un extremum.
- La dérivabilité de $f$ n'entraîne pas la continuité de $f'$.
