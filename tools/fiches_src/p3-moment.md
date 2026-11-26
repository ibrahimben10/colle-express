---
titre: Moment cinétique et solide en rotation
---
## L'essentiel

Pour les rotations, le **moment cinétique** joue le rôle de la quantité de mouvement et le **moment des forces** celui des forces. Le théorème du moment cinétique est l'outil adapté à un solide tournant autour d'un axe fixe.

## Moment d'une force

[[fig:p3-moment-1]]

> **Définition — Moment par rapport à un point et à un axe.** $\vec{\mathcal M}_O(\vec F) = \overrightarrow{OM}\wedge\vec F$ ; par rapport à un axe $\Delta$ orienté de vecteur $\vec u_\Delta$ : $\mathcal M_\Delta = \vec{\mathcal M}_O\cdot\vec u_\Delta = \pm Fd$.

$d$ est le **bras de levier** : la distance entre l'axe et la droite d'action. Le signe dépend du sens de rotation que la force tend à imposer.

## Moment cinétique

Point matériel : $\vec L_O = \overrightarrow{OM}\wedge m\vec v$. Solide en rotation autour d'un axe fixe : $L_\Delta = J_\Delta\,\omega$, où $J_\Delta = \sum m_ir_i^2$ est le **moment d'inertie**.

> **Théorème du moment cinétique (axe fixe, référentiel galiléen).** $J_\Delta\,\dfrac{\mathrm d\omega}{\mathrm dt} = \sum\mathcal M_\Delta$.

## Couple

[[fig:p3-moment-3]]

Un couple est un ensemble de forces de résultante nulle mais de moment non nul ; pour deux forces opposées : $\Gamma = Fd$. Une liaison pivot parfaite exerce un moment nul par rapport à son axe.

## Pendule pesant

[[fig:p3-moment-2]]

$$J_\Delta\ddot\theta = -mga\sin\theta,\qquad \omega_0 = \sqrt{\frac{mga}{J_\Delta}}\ \text{(petits angles)}.$$

## Énergie

$E_c = \tfrac12J_\Delta\omega^2$ ; puissance d'une force ou d'un couple : $\mathcal P = \mathcal M_\Delta\,\omega$.

## Exemple corrigé

**Énoncé.** Une tige homogène de masse $m$ et de longueur $\ell$ tourne autour d'un axe horizontal fixe passant par une extrémité ($J = m\ell^2/3$). Écrire l'équation du mouvement et la période des petites oscillations.

**Solution.**
1. Théorème du moment cinétique par rapport à l'axe : $J\ddot\theta = \mathcal M_\Delta(\text{poids})$, le moment de la liaison pivot parfaite étant nul.
2. Le poids s'applique au centre de masse, à $\ell/2$ de l'axe : $\mathcal M_\Delta = -mg\dfrac\ell2\sin\theta$.
3. $\ddot\theta + \dfrac{3g}{2\ell}\sin\theta = 0$ ; pour de petits angles, $T_0 = 2\pi\sqrt{\dfrac{2\ell}{3g}}$.

## Pièges classiques

- Une force dont la droite d'action passe par l'axe a un moment nul, quelle que soit son intensité.
- $J_\Delta$ dépend de l'axe : il est minimal pour un axe passant par le centre de masse.
