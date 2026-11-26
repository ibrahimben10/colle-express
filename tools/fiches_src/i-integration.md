---
titre: Intégration et dérivation numériques
---
## L'essentiel

Pour calculer $\displaystyle\int_a^bf(x)\,\mathrm dx$ numériquement, on découpe $[a, b]$ en $n$ intervalles de largeur $h = \dfrac{b - a}{n}$ et on approche $f$ sur chacun. Plus la méthode est précise, plus l'erreur décroît vite quand $h$ diminue.

## Méthode des rectangles

[[fig:i-integration-1]]

$$R_n = h\sum_{k=0}^{n-1}f(a + kh)\quad\text{(rectangles à gauche)}.$$

```python
def rectangles(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + k * h) for k in range(n))
```

> **Propriété.** Si $f$ est de classe $\mathcal C^1$, l'erreur est au plus $\dfrac{(b - a)^2}{2n}\max|f'|$ : elle est en $O(h)$. Doubler $n$ divise l'erreur par 2.

Variante : le **point milieu** $h\sum f\big(a + (k + \tfrac12)h\big)$, en $O(h^2)$.

## Méthode des trapèzes

[[fig:i-integration-2]]

$$T_n = h\left(\frac{f(a) + f(b)}{2} + \sum_{k=1}^{n-1}f(a + kh)\right).$$

```python
def trapezes(f, a, b, n):
    h = (b - a) / n
    s = (f(a) + f(b)) / 2
    for k in range(1, n):
        s += f(a + k * h)
    return h * s
```

> **Propriété.** Pour $f$ de classe $\mathcal C^2$, l'erreur est au plus $\dfrac{(b - a)^3}{12n^2}\max|f''|$ : en $O(h^2)$. Doubler $n$ divise l'erreur par 4.

| Méthode | Erreur | Exacte pour |
|---|---|---|
| rectangles | $O(h)$ | les constantes |
| point milieu, trapèzes | $O(h^2)$ | les fonctions affines |
| Simpson | $O(h^4)$ | les polynômes de degré 3 |

En pratique : `scipy.integrate.quad(f, a, b)` renvoie la valeur et une estimation de l'erreur.

## Dérivation numérique

$$f'(x) \approx \frac{f(x + h) - f(x)}{h}\ \ (\text{erreur } O(h)),\qquad f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}\ \ (\text{erreur } O(h^2)).$$

Attention : si $h$ est trop petit, la soustraction de deux nombres très proches fait perdre des chiffres (erreur d'arrondi en $\varepsilon/h$). Un bon compromis est $h \approx 10^{-5}$ pour la différence centrée.

Pour des mesures (tableaux `t`, `x`) : `v = (x[1:] - x[:-1]) / (t[1:] - t[:-1])` avec NumPy, ou `np.gradient(x, t)`.

## Exemple corrigé

**Énoncé.** On approche $\displaystyle\int_0^1e^x\,\mathrm dx = e - 1 \approx 1{,}71828$ avec $n = 10$. Comparer rectangles et trapèzes.

**Solution.** Rectangles à gauche : $R_{10} \approx 1{,}63379$, erreur $\approx 8{,}5\cdot10^{-2}$. Trapèzes : $T_{10} \approx 1{,}71971$, erreur $\approx 1{,}4\cdot10^{-3}$. Avec $n = 20$, l'erreur des rectangles est divisée par 2 environ, celle des trapèzes par 4.

## Pièges classiques

- Oublier le facteur $h$, ou faire $n + 1$ rectangles.
- Confondre le nombre de points ($n + 1$) et le nombre d'intervalles ($n$).
