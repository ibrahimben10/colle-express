---
titre: Nombres complexes et trigonométrie
---
## L'essentiel

Les nombres complexes permettent de résoudre toutes les équations polynomiales, de représenter les points et les transformations du plan, et de calculer facilement en trigonométrie grâce à l'exponentielle $e^{i\theta}$.

## Trigonométrie

### Valeurs et formules

$\cos^2 + \sin^2 = 1$ ; $\cos$ et $\sin$ sont $2\pi$-périodiques, $\tan$ est $\pi$-périodique.

- Addition : $\cos(a + b) = \cos a\cos b - \sin a\sin b$, $\sin(a + b) = \sin a\cos b + \cos a\sin b$, $\tan(a + b) = \frac{\tan a + \tan b}{1 - \tan a\tan b}$.
- Duplication : $\cos 2a = \cos^2a - \sin^2a = 2\cos^2a - 1 = 1 - 2\sin^2a$ ; $\sin 2a = 2\sin a\cos a$.
- Linéarisation : $\cos^2a = \frac{1 + \cos 2a}{2}$, $\sin^2a = \frac{1 - \cos 2a}{2}$.
- Produits : $\cos a\cos b = \frac12[\cos(a - b) + \cos(a + b)]$, etc. ; sommes : $\cos p + \cos q = 2\cos\frac{p + q}{2}\cos\frac{p - q}{2}$.
- Angles associés : $\cos(\pi - x) = -\cos x$, $\sin(\pi - x) = \sin x$, $\cos(\frac\pi2 - x) = \sin x$.

### Équations

$\cos a = \cos b \Leftrightarrow a \equiv \pm b\ [2\pi]$ ; $\sin a = \sin b \Leftrightarrow a \equiv b$ ou $a \equiv \pi - b\ [2\pi]$ ; $\tan a = \tan b \Leftrightarrow a \equiv b\ [\pi]$.

Pour $a\cos x + b\sin x$ : on l'écrit $r\cos(x - \varphi)$ avec $r = \sqrt{a^2 + b^2}$.

## Forme algébrique

$z = a + ib$, $\operatorname{Re}z = a$, $\operatorname{Im}z = b$. Conjugué $\bar z = a - ib$ : $\overline{z + w} = \bar z + \bar w$, $\overline{zw} = \bar z\bar w$, $z + \bar z = 2\operatorname{Re}z$. Module $|z| = \sqrt{z\bar z} = \sqrt{a^2 + b^2}$ ; $|zw| = |z||w|$ ; $\frac1z = \frac{\bar z}{|z|^2}$.

> **Propriété — Inégalité triangulaire.** $|z + w| \le |z| + |w|$, avec égalité si et seulement si $z$ et $w$ sont positivement liés ($w = \lambda z$, $\lambda \ge 0$, ou $z = 0$).

## Forme exponentielle

[[fig:m1-complexes-1]]

$e^{i\theta} = \cos\theta + i\sin\theta$ ; $e^{i(\theta + \theta')} = e^{i\theta}e^{i\theta'}$. Tout $z \ne 0$ s'écrit $z = re^{i\theta}$ avec $r = |z|$ et $\theta$ un **argument** (défini modulo $2\pi$) ; $\arg(zw) \equiv \arg z + \arg w$.

> **Théorème — Formules d'Euler et de Moivre.** $\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}$, $\sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$ ; $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$.

> **Méthode — Angle moitié.** $e^{ia} + e^{ib} = e^{i\frac{a+b}{2}}\cdot2\cos\frac{a - b}{2}$ ; en particulier $1 + e^{i\theta} = 2\cos\frac\theta2\,e^{i\theta/2}$.

Usages : **linéariser** $\cos^n\theta$ (Euler puis binôme) ; exprimer $\cos n\theta$ en fonction de $\cos\theta$ (Moivre) ; calculer $\sum\cos(k\theta)$ comme partie réelle d'une somme géométrique.

Exponentielle complexe : $e^z = e^ae^{ib}$ pour $z = a + ib$ ; $|e^z| = e^{\operatorname{Re}z}$ ; $e^z = 1 \Leftrightarrow z \in 2i\pi\mathbb Z$.

## Équations algébriques

- Racines carrées de $w = a + ib$ : poser $z = x + iy$, utiliser $x^2 - y^2 = a$, $x^2 + y^2 = |w|$, et le signe de $2xy = b$.
- $az^2 + bz + c = 0$ ($a \ne 0$) : $\Delta = b^2 - 4ac$ ; si $\delta^2 = \Delta$, les racines sont $\frac{-b \pm \delta}{2a}$. Somme $-\frac ba$, produit $\frac ca$.
- **Racines $n$-ièmes de l'unité** : $\omega_k = e^{2ik\pi/n}$, $k = 0, \dots, n - 1$ ; leur somme est nulle pour $n \ge 2$. Racines $n$-ièmes de $w = \rho e^{i\alpha}$ : $\rho^{1/n}e^{i\alpha/n}\omega_k$.

## Géométrie

- Distance $AB = |b - a|$ ; angle $(\overrightarrow{AB}, \overrightarrow{AC}) \equiv \arg\frac{c - a}{b - a}$.
- $A$, $B$, $C$ alignés $\Leftrightarrow \frac{c - a}{b - a} \in \mathbb R$ ; orthogonalité $\Leftrightarrow \frac{c - a}{b - a} \in i\mathbb R$.
- Transformations : translation $z \mapsto z + b$, homothétie $z \mapsto \omega + k(z - \omega)$, rotation $z \mapsto \omega + e^{i\theta}(z - \omega)$ ; plus généralement les **similitudes directes** $z \mapsto az + b$ ($a \ne 0$).

## Exemple corrigé

**Énoncé.** Calculer $S = \sum_{k=0}^n\cos(k\theta)$ pour $\theta \notin 2\pi\mathbb Z$.

**Solution.** $S = \operatorname{Re}\sum_{k=0}^n e^{ik\theta} = \operatorname{Re}\frac{e^{i(n+1)\theta} - 1}{e^{i\theta} - 1}$. Avec l'angle moitié, $\frac{e^{i(n+1)\theta} - 1}{e^{i\theta} - 1} = e^{in\theta/2}\frac{\sin\frac{(n+1)\theta}{2}}{\sin\frac\theta2}$, donc $S = \frac{\cos\frac{n\theta}{2}\sin\frac{(n+1)\theta}{2}}{\sin\frac\theta2}$.

## Pièges classiques

- L'argument n'est défini que modulo $2\pi$, et pas pour $z = 0$.
- Ne pas écrire $\sqrt z$ pour un complexe : il a deux racines carrées opposées.
- $z \mapsto \bar z$ n'est pas une similitude directe (elle renverse les angles).
