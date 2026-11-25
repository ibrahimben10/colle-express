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

## Pièges classiques

- Une force dont la droite d'action passe par l'axe a un moment nul, quelle que soit son intensité.
- $J_\Delta$ dépend de l'axe : il est minimal pour un axe passant par le centre de masse.
