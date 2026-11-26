---
titre: Dynamique dans un référentiel non galiléen
---
## L'essentiel

Dans un référentiel R′ non galiléen, le principe fondamental de la dynamique reste valable à condition d'ajouter deux **forces d'inertie** : la force d'inertie d'entraînement et la force d'inertie de Coriolis.

> **Loi — PFD dans R′.** $m\vec a_r = \sum\vec F + \vec F_{ie} + \vec F_{ic}$, avec $\vec F_{ie} = -m\vec a_e$ et $\vec F_{ic} = -2m\,\vec\omega\wedge\vec v_r$.

## Référentiel en translation

$\vec F_{ie} = -m\,\vec a(O')$ et $\vec F_{ic} = \vec 0$.

[[fig:mp-non-galileen-3]]

Dans un véhicule d'accélération $\vec a$, tout se passe comme si la pesanteur valait $\vec g_{\text{app}} = \vec g - \vec a$ : le pendule s'incline vers l'arrière d'un angle $\alpha$ tel que $\tan\alpha = a/g$.

## Référentiel en rotation uniforme

[[fig:mp-non-galileen-1]]

> **Formule — Force centrifuge.** $\vec F_{ie} = m\omega^2\,\overrightarrow{HM}$ : elle dérive de l'énergie potentielle $E_p = -\tfrac12 m\omega^2 r^2$.

La force de Coriolis $-2m\vec\omega\wedge\vec v_r$ est perpendiculaire à la vitesse relative : elle **ne travaille pas**.

[[fig:mp-non-galileen-2]]

## Le référentiel terrestre

[[fig:mp-non-galileen-4]]

Le **poids** $m\vec g$ est la somme de l'attraction gravitationnelle et de la force d'inertie d'entraînement due à la rotation de la Terre ($\Omega = 7{,}3\cdot10^{-5}$ rad·s⁻¹). Il dépend de la latitude ; l'écart avec la gravitation est faible (au plus 0,3 %).

Effets de Coriolis : déviation vers l'est d'un corps en chute libre, sens de rotation des vents autour des dépressions, pendule de Foucault.

## Exemple corrigé

**Énoncé.** Dans un train qui accélère à $a = 2$ m·s⁻², un pendule est à l'équilibre relatif. Quel angle fait-il avec la verticale ?

**Solution.**
1. Référentiel du train, en translation rectiligne accélérée : on ajoute la force d'inertie d'entraînement $-m\vec a$ (pas de Coriolis).
2. Équilibre : $m\vec g - m\vec a + \vec T = \vec 0$ ; le fil est aligné avec $\vec g - \vec a$.
3. $\tan\alpha = a/g \approx 0{,}20$, soit $\alpha \approx 11{,}5°$, le pendule penchant vers l'arrière du train.

## Pièges classiques

- Pas de forces d'inertie dans un référentiel galiléen.
- Dans le référentiel terrestre, la force d'inertie d'entraînement est déjà comprise dans le poids : ne pas l'ajouter une deuxième fois.
