---
titre: Résolution numérique d'équations
---
## L'essentiel

Pour résoudre $f(x) = 0$ quand on ne sait pas le faire à la main, on construit une suite d'approximations de la racine $\alpha$. Deux méthodes à connaître : la **dichotomie** (sûre mais lente) et la **méthode de Newton** (très rapide, mais demande $f'$ et un bon point de départ).

## Dichotomie

[[fig:i-zeros-1]]

Hypothèses : $f$ continue sur $[a, b]$ avec $f(a)f(b) \le 0$ (théorème des valeurs intermédiaires).

```python
def dichotomie(f, a, b, eps):
    while b - a > eps:
        m = (a + b) / 2
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
    return (a + b) / 2
```

> **Propriété.** Après $n$ itérations, l'erreur est au plus $\dfrac{b - a}{2^{n+1}}$ : on gagne un chiffre binaire par itération (environ 3,3 itérations par chiffre décimal). Nombre d'itérations pour une précision $\varepsilon$ : $\left\lceil\log_2\dfrac{b - a}{\varepsilon}\right\rceil$.

## Méthode de Newton

[[fig:i-zeros-2]]

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}.$$

```python
def newton(f, fp, x0, eps, nmax=100):
    x = x0
    for _ in range(nmax):
        dx = f(x) / fp(x)
        x = x - dx
        if abs(dx) < eps:
            return x
    raise ValueError("pas de convergence")
```

> **Propriété.** Si $f$ est de classe $\mathcal C^2$ et $f'(\alpha) \ne 0$, la convergence est **quadratique** près de $\alpha$ : le nombre de chiffres exacts double à chaque itération. Mais la méthode peut diverger si $x_0$ est loin de $\alpha$ ou si $f'$ s'annule.

Variante sans dérivée : la **méthode de la sécante**, qui remplace $f'(x_n)$ par $\dfrac{f(x_n) - f(x_{n-1})}{x_n - x_{n-1}}$.

## Comparaison

| | Dichotomie | Newton |
|---|---|---|
| hypothèses | $f$ continue, changement de signe | $f$ dérivable, $f'(\alpha) \ne 0$, $x_0$ proche |
| convergence | toujours, linéaire | locale, quadratique |
| itérations pour $10^{-12}$ sur $[0, 1]$ | 40 | environ 5 |

En pratique (TP, oral) : `scipy.optimize.brentq(f, a, b)` combine sûreté et rapidité.

## Exemple corrigé

**Énoncé.** Calculer $\sqrt2$ par la méthode de Newton à partir de $x_0 = 1$.

**Solution.** $f(x) = x^2 - 2$, $f'(x) = 2x$, donc $x_{n+1} = \dfrac{x_n}{2} + \dfrac{1}{x_n}$ (méthode de Héron). $x_1 = 1{,}5$ ; $x_2 \approx 1{,}41667$ ; $x_3 \approx 1{,}4142157$ ; $x_4 \approx 1{,}41421356237$. Les chiffres exacts passent de 1 à 3, 6 puis 12 : convergence quadratique.

## Pièges classiques

- Test d'arrêt sur `f(x) == 0` : n'arrive presque jamais avec des flottants.
- Oublier de limiter le nombre d'itérations de Newton : boucle infinie en cas de divergence.
- Pour la dichotomie, calculer `f(a)` à chaque tour est inutile : le mémoriser.
