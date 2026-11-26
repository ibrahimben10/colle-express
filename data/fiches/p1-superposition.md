---
titre: Superposition de deux signaux sinusoïdaux
---
## L'essentiel

Deux signaux sinusoïdaux de **même fréquence** s'ajoutent en un signal sinusoïdal de même fréquence dont l'amplitude dépend de leur **déphasage** : c'est le principe des interférences. Deux ondes en sens opposés forment des ondes stationnaires (modes propres) ; deux fréquences voisines donnent des battements.

## Somme de deux sinusoïdes de même pulsation

Pour $s_1 = A_1\cos(\omega t + \varphi_1)$ et $s_2 = A_2\cos(\omega t + \varphi_2)$, avec $\Delta\varphi = \varphi_2 - \varphi_1$ (calcul par les complexes ou par Fresnel) :
$$A^2 = A_1^2 + A_2^2 + 2A_1A_2\cos\Delta\varphi.$$

> **Propriété — Interférences.** Amplitude maximale $A_1 + A_2$ si $\Delta\varphi = 2p\pi$ (constructives), minimale $|A_1 - A_2|$ si $\Delta\varphi = (2p+1)\pi$ (destructives).

Pour des amplitudes égales : $A = 2A_1\left|\cos\frac{\Delta\varphi}{2}\right|$. L'intensité (proportionnelle à $A^2$) vaut $I = I_1 + I_2 + 2\sqrt{I_1I_2}\cos\Delta\varphi$.

## Interférences de deux ondes

[[fig:p1-superposition-1]]

Pour deux sources synchrones en phase, en un point $M$ : $\Delta\varphi = \dfrac{2\pi}{\lambda}\,\delta$ avec $\delta = S_2M - S_1M$ la **différence de marche**.

- Interférences constructives : $\delta = p\lambda$ ; destructives : $\delta = (p + \frac12)\lambda$.
- Les points d'interférence constructive dessinent des hyperboles de foyers $S_1$ et $S_2$ (cuve à ondes).
- Condition : sources **cohérentes** (même fréquence, déphasage constant). Deux sources indépendantes ne produisent pas d'interférences stables : leurs intensités s'ajoutent.

## Ondes stationnaires

La superposition de deux ondes progressives de même amplitude et même fréquence se propageant en sens inverses (par exemple une onde et sa réflexion) donne
$$s(x,t) = 2A\cos(kx + \alpha)\cos(\omega t + \beta) :$$
les dépendances en $x$ et en $t$ sont **séparées**. Les nœuds (amplitude nulle) sont distants de $\lambda/2$, les ventres aussi ; un nœud et le ventre voisin sont distants de $\lambda/4$. Entre deux nœuds, tous les points vibrent en phase. L'énergie ne se propage pas en moyenne.

[[fig:p1-superposition-2]]

> **Propriété — Modes propres d'une corde fixée en $x = 0$ et $x = L$.** Les extrémités sont des nœuds, donc $L = n\dfrac{\lambda_n}{2}$ et $f_n = n\dfrac{c}{2L}$, $n \in \mathbb N^*$. Le mode $n = 1$ est le fondamental ; les autres sont ses harmoniques.

- Corde de guitare : $c = \sqrt{T/\mu}$, donc $f_1 = \frac{1}{2L}\sqrt{\frac{T}{\mu}}$ ; on raccourcit la corde ou on augmente la tension pour monter la note.
- Tuyau sonore ouvert aux deux bouts : nœuds de surpression aux extrémités (pression atmosphérique imposée), mêmes fréquences $f_n = n\frac{c}{2L}$ ; fermé à un bout : $f_n = (2n - 1)\frac{c}{4L}$ (harmoniques impaires seulement).
- **Corde de Melde** : excitée à la fréquence $f$, la corde entre en **résonance** quand $f$ est égale à une fréquence propre.

Une vibration quelconque d'une corde fixée est une superposition de modes propres : elle détermine le **timbre** de l'instrument.

## Battements

[[fig:p1-superposition-3]]

$\cos\omega_1 t + \cos\omega_2 t = 2\cos\!\left(\dfrac{\omega_1 - \omega_2}{2}t\right)\cos\!\left(\dfrac{\omega_1 + \omega_2}{2}t\right)$ : une oscillation rapide à la fréquence moyenne, modulée par une enveloppe lente, de période $T_b = 1/|f_1 - f_2|$. Utilisé pour accorder un instrument (les battements disparaissent quand les fréquences sont égales).

## Exemple corrigé

**Énoncé.** Deux haut-parleurs en phase émettent un son de fréquence $f = 680$ Hz ($c = 340$ m·s⁻¹). Un micro est à $d_1 = 3{,}00$ m de l'un et $d_2 = 3{,}75$ m de l'autre. Les ondes y interfèrent-elles de façon constructive ?

**Solution.**
1. $\lambda = c/f = 0{,}50$ m.
2. $\delta = d_2 - d_1 = 0{,}75$ m, soit $\delta/\lambda = 1{,}5$.
3. $\delta$ est un multiple **impair** de $\lambda/2$ : interférence **destructive** (amplitude minimale, nulle si les deux amplitudes sont égales).

## Exemple corrigé (corde vibrante)

**Énoncé.** Une corde de longueur 65 cm a un fondamental de 440 Hz. Célérité des ondes ? Fréquence du 3e mode ?

**Solution.** $c = 2Lf_1 = 572$ m·s⁻¹ ; $f_3 = 3f_1 = 1320$ Hz.

## Pièges classiques

- Il faut des sources **cohérentes** pour observer des interférences stables.
- La période des battements est $1/|f_1 - f_2|$, et non $2/|f_1 - f_2|$ : l'enveloppe s'annule deux fois par période de son cosinus.
- Dans une onde stationnaire, deux points de part et d'autre d'un nœud vibrent en opposition de phase.
