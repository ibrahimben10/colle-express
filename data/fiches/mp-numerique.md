---
titre: Électronique numérique
---
## L'essentiel

Numériser un signal, c'est l'**échantillonner** (le relever à intervalles réguliers $T_e$) puis le **quantifier** (arrondir chaque valeur à un nombre fini de niveaux). L'échantillonnage ne perd pas d'information si le critère de Shannon est respecté.

## Échantillonnage

[[fig:mp-numerique-1]]

Fréquence d'échantillonnage $f_e = 1/T_e$. Le spectre du signal échantillonné est celui du signal de départ, **répété** autour de chaque multiple de $f_e$.

[[fig:mp-numerique-2]]

> **Loi — Critère de Shannon-Nyquist.** Pour pouvoir reconstituer le signal, il faut $f_e > 2f_{\max}$, où $f_{\max}$ est la plus haute fréquence de son spectre.

Sinon, il y a **repliement** : une composante de fréquence $f$ apparaît à la fréquence $|f - kf_e|$. On place un filtre passe-bas **anti-repliement** avant l'échantillonneur.

## Quantification

[[fig:mp-numerique-3]]

Un convertisseur analogique-numérique sur $n$ bits et de pleine échelle $U$ a un pas $q = \dfrac{U}{2^n}$. L'erreur de quantification est d'au plus $q/2$.

## Filtrage numérique

On calcule la sortie à partir des échantillons, par une relation de récurrence.

| Filtre | Équation différentielle | Récurrence (méthode d'Euler, pas $T_e$) |
|---|---|---|
| passe-bas du 1er ordre | $\tau\dfrac{\mathrm ds}{\mathrm dt} + s = e$ | $s_{k+1} = s_k + \dfrac{T_e}{\tau}(e_k - s_k)$ |

## Exemple corrigé

**Énoncé.** On échantillonne à $f_e = 1$ kHz une sinusoïde de fréquence 800 Hz. Quelle fréquence observe-t-on sur le signal reconstruit ?

**Solution.**
1. Critère de Shannon : il faudrait $f_e > 1600$ Hz ; il n'est pas respecté.
2. Le spectre échantillonné contient les raies $|800 - kf_e|$ : la plus basse est $|800 - 1000| = 200$ Hz.
3. On observe une sinusoïde à 200 Hz : c'est le repliement. Il fallait un filtre anti-repliement coupant au-dessus de 500 Hz.

## Pièges classiques

- Le stroboscope et l'effet « roue qui tourne à l'envers » sont des cas de repliement.
- Il faut $f_e > 2f_{\max}$, et non $f_e > f_{\max}$ ; en pratique on prend une marge.
