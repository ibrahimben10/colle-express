---
titre: Nombres complexes et trigonométrie
---
## L'essentiel

Un complexe s'écrit $z = a + ib$ (forme algébrique) ou $z = re^{i\theta}$ (forme exponentielle). La forme exponentielle transforme les produits en sommes d'arguments, et donne les formules de trigonométrie.

## Module et argument

[[fig:m1-complexes-1]]

- $|z|^2 = z\bar z = a^2 + b^2$ ; $|zz'| = |z||z'|$ ; **inégalité triangulaire** $|z + z'| \le |z| + |z'|$.
- $e^{i\theta}e^{i\theta'} = e^{i(\theta + \theta')}$ : $\arg(zz') \equiv \arg z + \arg z'\ [2\pi]$.

> **Formules d'Euler et de Moivre.** $\cos\theta = \dfrac{e^{i\theta} + e^{-i\theta}}{2}$, $\sin\theta = \dfrac{e^{i\theta} - e^{-i\theta}}{2i}$ ; $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$.

## Trigonométrie

- $\cos(a + b) = \cos a\cos b - \sin a\sin b$, $\sin(a + b) = \sin a\cos b + \cos a\sin b$.
- **Linéarisation** ($\cos^n$) : formules d'Euler puis binôme. **Factorisation** de $e^{ia} + e^{ib}$ par l'angle moitié : $e^{ia} + e^{ib} = 2\cos\frac{a-b}{2}e^{i\frac{a+b}{2}}$.

## Équations

- Racines carrées de $\Delta$ : résoudre $(x + iy)^2 = \Delta$ avec le module.
- $az^2 + bz + c = 0$ : $z = \frac{-b \pm \delta}{2a}$ avec $\delta^2 = b^2 - 4ac$.
- Racines $n$-ièmes de l'unité : $e^{2ik\pi/n}$, $k = 0, \dots, n-1$.

## Géométrie

$\frac{c - a}{b - a}$ donne l'angle et le rapport des longueurs ; l'application $z \mapsto az + b$ est une similitude (rotation si $|a| = 1$).

## Exemple corrigé

**Énoncé.** Calculer $\sum_{k=0}^n\cos(k\theta)$ pour $\theta \notin 2\pi\mathbb Z$.

**Solution.** C'est la partie réelle de $\sum_{k=0}^ne^{ik\theta} = \frac{e^{i(n+1)\theta} - 1}{e^{i\theta} - 1}$. Par l'angle moitié, ce quotient vaut $e^{in\theta/2}\frac{\sin((n+1)\theta/2)}{\sin(\theta/2)}$. Donc $\sum_{k=0}^n\cos k\theta = \dfrac{\cos(n\theta/2)\sin((n+1)\theta/2)}{\sin(\theta/2)}$.

## Pièges classiques

- L'argument n'est défini qu'à $2\pi$ près, et pas pour $z = 0$.
- $\sqrt{\ }$ n'a pas de sens pour un complexe : parler d'**une** racine carrée.
- $|a + b| = |a| + |b|$ seulement si $a$ et $b$ ont le même argument (ou l'un est nul).
