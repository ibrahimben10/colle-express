---
titre: Introduction au monde quantique
---
## L'essentiel

À l'échelle microscopique, la lumière et la matière présentent à la fois des aspects **ondulatoires** et **corpusculaires** (dualité onde-particule). On ne prédit plus une trajectoire, mais une **probabilité** de détection, décrite par une fonction d'onde. L'énergie des systèmes liés est quantifiée.

## Le photon

> **Relations de Planck-Einstein.** Une onde lumineuse de fréquence $\nu$ est formée de photons d'énergie $E = h\nu = \hbar\omega$ et de quantité de mouvement $p = h/\lambda = \hbar k$ ; $h = 6{,}63\cdot10^{-34}$ J·s, $\hbar = \frac{h}{2\pi}$.

- **Effet photoélectrique** : un métal éclairé émet des électrons seulement si $\nu$ dépasse un seuil $\nu_0 = \frac{W}{h}$ ($W$ : travail d'extraction), quelle que soit l'intensité ; l'énergie cinétique maximale des électrons vaut $h\nu - W$. L'intensité ne change que le **nombre** d'électrons.
- Flux de photons : une puissance $P$ correspond à $\frac{P}{h\nu}$ photons par seconde.
- Le photon n'a pas de masse et se déplace à $c$.

## La matière comme une onde

> **Relation de de Broglie.** À une particule de quantité de mouvement $p$ est associée une onde de longueur d'onde $\lambda = h/p$.

Mises en évidence : diffraction des électrons par un cristal (Davisson et Germer), interférences d'atomes, de molécules. Les effets ondulatoires apparaissent quand $\lambda$ est comparable aux dimensions caractéristiques (distances interatomiques, fentes).

[[fig:p1-quantique-1]]

Dans une expérience de fentes d'Young réalisée électron par électron (ou photon par photon), chaque particule donne **un seul impact**, à une position aléatoire ; l'accumulation des impacts reconstitue la figure d'interférences.

## Interprétation probabiliste

> **Propriété — Fonction d'onde.** L'état d'une particule est décrit par une fonction d'onde $\psi(x, t)$ ; $|\psi(x, t)|^2\,\mathrm dx$ est la probabilité de la détecter entre $x$ et $x + \mathrm dx$ à l'instant $t$ (normalisation : $\int|\psi|^2 = 1$).

Si l'on cherche par quelle fente passe la particule, les interférences disparaissent : la mesure perturbe le système.

## Quantification de l'énergie

[[fig:p1-quantique-2]]

L'énergie d'un atome ne peut prendre que des valeurs discrètes $E_n$. Une transition entre deux niveaux s'accompagne de l'absorption ou de l'émission d'un photon :
$$h\nu = |E_n - E_p|.$$
C'est l'origine des spectres de raies. Pour l'atome d'hydrogène, $E_n = -\frac{13{,}6}{n^2}$ eV.

> **Propriété — Particule confinée.** Une particule de masse $m$ confinée dans un domaine de taille $L$ a une énergie quantifiée ; modèle de la corde vibrante : $L = n\frac{\lambda_n}{2}$ et $p_n = \frac{h}{\lambda_n}$ donnent $E_n = \frac{p_n^2}{2m} = \frac{n^2h^2}{8mL^2}$. L'énergie minimale n'est pas nulle.

## Inégalité de Heisenberg (spatiale)

$$\Delta x\,\Delta p_x \gtrsim \hbar.$$

On ne peut pas connaître simultanément, avec une précision arbitraire, la position et la quantité de mouvement. Conséquences : une particule confinée a une énergie cinétique minimale d'ordre $\frac{\hbar^2}{2mL^2}$ (énergie de confinement) ; elle explique la stabilité des atomes (l'électron ne s'effondre pas sur le noyau).

## Exemple corrigé

**Énoncé.** Énergie (en eV) d'un photon de 500 nm, et longueur d'onde de de Broglie d'un électron de vitesse $10^6$ m·s⁻¹.

**Solution.**
1. $E = \dfrac{hc}{\lambda} = 4{,}0\cdot10^{-19}$ J, soit $E \approx 2{,}5$ eV.
2. $\lambda_{dB} = \dfrac{h}{mv} \approx 0{,}73$ nm : de l'ordre des distances interatomiques, d'où la diffraction des électrons par les cristaux.

## Exemple corrigé (énergie de confinement)

**Énoncé.** Ordre de grandeur de l'énergie d'un électron confiné dans un atome ($L \approx 0{,}1$ nm), et d'un nucléon dans un noyau ($L \approx 10^{-15}$ m).

**Solution.** $E \approx \frac{\hbar^2}{2mL^2}$. Électron : $\frac{(10^{-34})^2}{2\times9{,}1\cdot10^{-31}\times10^{-20}} \approx 5\cdot10^{-19}$ J $\approx 3$ eV (échelle de la chimie). Nucléon ($m \approx 1{,}7\cdot10^{-27}$ kg) : $\approx 3\cdot10^{-12}$ J $\approx 20$ MeV (échelle nucléaire).

## Pièges classiques

- Le comportement quantique se manifeste quand $\lambda = h/p$ est comparable aux dimensions du système : pour une balle de tennis, $\lambda$ est ridiculement petite.
- Un photon a une énergie et une quantité de mouvement, mais pas de masse.
- L'inégalité de Heisenberg n'est pas une imprécision des appareils : c'est une propriété de l'état quantique.

## Ordres de grandeur

Photon visible : 2 à 3 eV ; énergie d'ionisation de l'hydrogène : 13,6 eV ; électron accéléré sous 100 V : $\lambda \approx 0{,}12$ nm.
