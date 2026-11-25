---
titre: Oscillateur harmonique
---
## L'essentiel

Un système est un **oscillateur harmonique** lorsque sa grandeur caractéristique $x(t)$ obéit à
$$\ddot x + \omega_0^2\,x = 0,$$
où $\omega_0$ est la pulsation propre. Les solutions sont sinusoïdales, de période indépendante de l'amplitude (isochronisme).

[[fig:p1-oscillateur-1]]

## Le système masse-ressort

> **Loi — Force de rappel élastique.** Un ressort de raideur $k$ et de longueur à vide $\ell_0$ exerce $\vec F = -k(\ell - \ell_0)\,\vec u_{\text{ext}}$, dirigée vers sa position d'équilibre.

Pour une masse $m$ sur un support horizontal sans frottement, avec $x$ l'écart à la position d'équilibre, le principe fondamental de la dynamique projeté sur $\vec u_x$ donne
$$m\ddot x = -kx \quad\Longleftrightarrow\quad \ddot x + \omega_0^2 x = 0,\qquad \omega_0 = \sqrt{\frac{k}{m}}.$$

## Solutions

$$x(t) = X_m\cos(\omega_0 t + \varphi) = A\cos(\omega_0 t) + B\sin(\omega_0 t),\qquad T_0 = \frac{2\pi}{\omega_0}.$$

Les deux constantes ($X_m$ et $\varphi$, ou $A$ et $B$) sont fixées par les **conditions initiales** $x(0)$ et $\dot x(0)$ : $A = x(0)$ et $B = \dot x(0)/\omega_0$.

[[fig:p1-oscillateur-2]]

## Énergie

> **Propriété — Conservation de l'énergie.** $E_m = \tfrac12 m\dot x^2 + \tfrac12 kx^2 = \tfrac12 kX_m^2$ est constante : l'énergie passe sans cesse de la forme cinétique à la forme potentielle.

Les moyennes sur une période sont égales : $\langle E_c\rangle = \langle E_p\rangle = E_m/2$.

[[fig:p1-oscillateur-3]]

Dans le plan $(x, \dot x)$, la trajectoire est une ellipse de demi-axes $X_m$ et $\omega_0 X_m$, parcourue dans le sens horaire.

## Méthode

- Faire le bilan des forces, choisir l'axe, écrire l'équation à l'équilibre pour éliminer les constantes (cas vertical : le poids compense l'allongement statique).
- Mettre l'équation sous la forme canonique $\ddot x + \omega_0^2 x = 0$ et **identifier** $\omega_0$.
- Utiliser les conditions initiales en dernier.

## Pièges classiques

> **Attention — Origine de l'axe.** $x$ doit être mesuré depuis la **position d'équilibre** pour obtenir la forme canonique ; sinon un terme constant apparaît.

- La période ne dépend pas de l'amplitude : ce n'est vrai que pour un oscillateur **harmonique** (le pendule simple ne l'est qu'aux petits angles).
- $\omega_0$ en rad·s⁻¹, $f_0 = \omega_0/2\pi$ en Hz : ne pas les confondre.

## Ordres de grandeur

Masse de 100 g et ressort de 10 N·m⁻¹ : $\omega_0 = 10$ rad·s⁻¹, $T_0 \approx 0{,}63$ s.
