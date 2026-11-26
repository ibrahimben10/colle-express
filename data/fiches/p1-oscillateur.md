---
titre: Oscillateur harmonique
---
## L'essentiel

Un système est un **oscillateur harmonique** lorsque sa grandeur caractéristique $x(t)$ obéit à
$$\ddot x + \omega_0^2\,x = 0,$$
où $\omega_0$ est la pulsation propre. Les solutions sont sinusoïdales, de période indépendante de l'amplitude (isochronisme), et l'énergie se conserve.

[[fig:p1-oscillateur-1]]

## Le système masse-ressort

> **Loi — Force de rappel élastique.** Un ressort de raideur $k$ et de longueur à vide $\ell_0$ exerce $\vec F = -k(\ell - \ell_0)\,\vec u_{\text{ext}}$, où $\vec u_{\text{ext}}$ est dirigé vers l'extérieur du ressort : la force tend à ramener la longueur vers $\ell_0$.

### Ressort horizontal

Pour une masse $m$ sur un support horizontal sans frottement, avec $x$ l'écart à la position d'équilibre, le PFD projeté sur $\vec u_x$ donne
$$m\ddot x = -kx \quad\Longleftrightarrow\quad \ddot x + \omega_0^2 x = 0,\qquad \omega_0 = \sqrt{\frac{k}{m}}.$$

### Ressort vertical

À l'équilibre, $k(\ell_{\text{éq}} - \ell_0) = mg$ (allongement statique). En posant $x = \ell - \ell_{\text{éq}}$, le poids disparaît de l'équation : on retrouve $\ddot x + \omega_0^2x = 0$ avec la même $\omega_0$.

## Solutions

$$x(t) = X_m\cos(\omega_0 t + \varphi) = A\cos(\omega_0 t) + B\sin(\omega_0 t),\qquad T_0 = \frac{2\pi}{\omega_0},\quad f_0 = \frac{1}{T_0}.$$

Les deux constantes ($X_m$ et $\varphi$, ou $A$ et $B$) sont fixées par les **conditions initiales** $x(0)$ et $\dot x(0)$ : $A = x(0)$ et $B = \dot x(0)/\omega_0$ ; $X_m = \sqrt{A^2 + B^2}$.

[[fig:p1-oscillateur-2]]

Vitesse $\dot x = -\omega_0X_m\sin(\omega_0t + \varphi)$, en quadrature avance sur $x$ ; accélération $\ddot x = -\omega_0^2x$, en opposition de phase.

## Énergie

> **Propriété — Conservation de l'énergie.** $E_m = \tfrac12 m\dot x^2 + \tfrac12 kx^2 = \tfrac12 kX_m^2$ est constante : l'énergie passe sans cesse de la forme cinétique à la forme potentielle.

- Énergie potentielle élastique $E_p = \tfrac12k(\ell - \ell_0)^2$.
- Les moyennes sur une période sont égales : $\langle E_c\rangle = \langle E_p\rangle = E_m/2$.
- Méthode énergétique : dériver $E_m = $ cte par rapport au temps redonne l'équation du mouvement.

[[fig:p1-oscillateur-3]]

Dans le plan de phase $(x, \dot x)$, la trajectoire est une ellipse de demi-axes $X_m$ et $\omega_0 X_m$, parcourue dans le sens horaire (un cercle si l'on trace $(x, \dot x/\omega_0)$).

## Universalité

Au voisinage d'une position d'équilibre stable $x_0$, toute énergie potentielle s'approxime par $E_p(x) \approx E_p(x_0) + \tfrac12E_p''(x_0)(x - x_0)^2$ : les petits mouvements sont harmoniques de pulsation $\omega_0 = \sqrt{E_p''(x_0)/m}$. Exemples : pendule simple aux petits angles ($\omega_0 = \sqrt{g/\ell}$), circuit LC ($\omega_0 = 1/\sqrt{LC}$), vibrations moléculaires.

## Méthode

- Faire le bilan des forces, choisir l'axe, écrire l'équation à l'équilibre pour éliminer les constantes.
- Mettre l'équation sous la forme canonique $\ddot x + \omega_0^2 x = 0$ et **identifier** $\omega_0$.
- Utiliser les conditions initiales en dernier.
- Vérifier l'homogénéité : $\sqrt{k/m}$ est en s⁻¹.

## Exemple corrigé

**Énoncé.** Une masse $m = 200$ g accrochée à un ressort de raideur $k = 20$ N·m⁻¹ est écartée de $X_0 = 3$ cm de sa position d'équilibre puis lâchée sans vitesse. Donner $x(t)$, la période et la vitesse maximale.

**Solution.**
1. PFD projeté sur l'axe : $m\ddot x = -kx$, soit $\ddot x + \omega_0^2x = 0$ avec $\omega_0 = \sqrt{k/m} = 10$ rad·s⁻¹.
2. $x(0) = X_0$, $\dot x(0) = 0$ donnent $A = X_0$, $B = 0$ : $x(t) = X_0\cos(\omega_0t)$.
3. Période $T_0 = 2\pi/\omega_0 \approx 0{,}63$ s.
4. $v_{\max} = \omega_0X_0 = 0{,}30$ m·s⁻¹. Vérification énergétique : $\tfrac12kX_0^2 = \tfrac12mv_{\max}^2$.

## Exemple corrigé (association de ressorts)

**Énoncé.** Une masse est reliée à deux murs par deux ressorts $k_1$ et $k_2$ de part et d'autre. Pulsation ?

**Solution.** Pour un déplacement $x$ depuis l'équilibre, un ressort s'allonge de $x$ et l'autre se raccourcit de $x$ : la force totale est $-(k_1 + k_2)x$. Donc $\omega_0 = \sqrt{\frac{k_1 + k_2}{m}}$. (Deux ressorts en série bout à bout donneraient $\frac{1}{k} = \frac{1}{k_1} + \frac{1}{k_2}$.)

## Pièges classiques

> **Attention — Origine de l'axe.** $x$ doit être mesuré depuis la **position d'équilibre** pour obtenir la forme canonique ; sinon un terme constant apparaît.

- La période ne dépend pas de l'amplitude : ce n'est vrai que pour un oscillateur **harmonique** (le pendule simple ne l'est qu'aux petits angles).
- $\omega_0$ en rad·s⁻¹, $f_0 = \omega_0/2\pi$ en Hz : ne pas les confondre.

## Ordres de grandeur

Masse de 100 g et ressort de 10 N·m⁻¹ : $\omega_0 = 10$ rad·s⁻¹, $T_0 \approx 0{,}63$ s ; pendule de 1 m : $T_0 \approx 2$ s ; quartz de montre : 32 768 Hz.
