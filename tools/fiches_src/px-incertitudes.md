---
titre: Mesures et incertitudes
---
## L'essentiel

Toute mesure est entachée d'erreurs aléatoires et systématiques. Le résultat s'écrit $x = x_{\text{mesuré}} \pm u(x)$, où $u(x)$ est l'**incertitude-type**, avec une unité et un nombre de chiffres significatifs cohérent. On propage les incertitudes, on compare des résultats et on valide des modèles.

## Variabilité et erreurs

- **Mesurande** : grandeur que l'on veut mesurer. Une mesure répétée donne des valeurs dispersées : on modélise le résultat par une variable aléatoire.
- **Erreur aléatoire** : varie d'une mesure à l'autre ; on la réduit en moyennant. **Erreur systématique** : même décalage à chaque mesure (appareil mal étalonné, méthode biaisée) ; on la corrige ou on la supprime.
- L'incertitude-type $u(x)$ est l'écart-type associé au résultat ; l'**incertitude relative** est $\frac{u(x)}{|x|}$.

## Deux façons d'évaluer une incertitude

[[fig:px-incertitudes-1]]

> **Définition — Évaluation de type A (statistique).** Sur $N$ mesures indépendantes de moyenne $\bar x$ et d'écart-type expérimental $\sigma = \sqrt{\frac{1}{N - 1}\sum(x_i - \bar x)^2}$ : $u(\bar x) = \dfrac{\sigma}{\sqrt N}$.

> **Définition — Évaluation de type B.** Une seule mesure : on estime $u$ à partir des données de l'instrument. Lecture sur une graduation de pas $\Delta$ : $u = \dfrac{\Delta}{2\sqrt3}$ ; tolérance $\pm a$ du constructeur (loi uniforme) : $u = \dfrac{a}{\sqrt3}$. Pour un multimètre, la notice donne la tolérance en pourcentage de la lecture plus un nombre de digits.

Si plusieurs sources d'incertitude indépendantes interviennent, on les combine : $u = \sqrt{u_1^2 + u_2^2 + \dots}$.

## Propagation des incertitudes

| Relation | Incertitude-type |
|---|---|
| $y = x_1 + x_2$ ou $x_1 - x_2$ | $u(y) = \sqrt{u(x_1)^2 + u(x_2)^2}$ |
| $y = x_1x_2$ ou $x_1/x_2$ | $\dfrac{u(y)}{\lvert y\rvert} = \sqrt{\left(\dfrac{u(x_1)}{x_1}\right)^2 + \left(\dfrac{u(x_2)}{x_2}\right)^2}$ |
| $y = x^\alpha$ | $\dfrac{u(y)}{\lvert y\rvert} = \lvert\alpha\rvert\dfrac{u(x)}{\lvert x\rvert}$ |
| $y = kx$ | $u(y) = \lvert k\rvert u(x)$ |

Pour une formule quelconque (grandeurs indépendantes) : $u(y)^2 = \sum_i\left(\frac{\partial f}{\partial x_i}\right)^2u(x_i)^2$. Pour les cas compliqués, on utilise une **simulation de Monte-Carlo** : on tire au hasard les grandeurs d'entrée selon leurs lois, on calcule $y$ pour chaque tirage, et l'écart-type des résultats donne $u(y)$ (en Python avec `numpy.random`).

## Écrire un résultat

- Incertitude arrondie à 1 ou 2 chiffres significatifs, valeur arrondie au **même rang** : $g = 9{,}81 \pm 0{,}03$ m·s⁻².
- Toujours l'unité. On peut écrire $g = 9{,}81(3)$ m·s⁻².
- On peut aussi donner une incertitude élargie $U = ku$ ($k = 2$ correspond à environ 95 % de confiance pour une loi normale).

## Comparer deux valeurs

> **Définition — Écart normalisé.** $E_N = \dfrac{|x_1 - x_2|}{\sqrt{u(x_1)^2 + u(x_2)^2}}$ ; les valeurs sont jugées compatibles si $E_N \lesssim 2$. Avec une valeur de référence sans incertitude : $E_N = \frac{|x - x_{\text{réf}}|}{u(x)}$.

## Régression linéaire

[[fig:px-incertitudes-2]]

Pour valider un modèle affine $y = ax + b$ :

1. Tracer les points avec leurs barres d'incertitude.
2. Effectuer la régression (moindres carrés, `numpy.polyfit`).
3. Vérifier que la droite passe par (presque) toutes les barres et que les **résidus** $y_i - (ax_i + b)$ sont répartis aléatoirement autour de 0, sans tendance, avec des écarts normalisés $\frac{|y_i - (ax_i + b)|}{u(y_i)}$ de l'ordre de 2 au plus.
4. Les incertitudes sur $a$ et $b$ s'obtiennent par Monte-Carlo (tirages des $y_i$, puis nouvelle régression).

Le coefficient de corrélation $r$ proche de 1 ne suffit pas à valider un modèle linéaire. Pour une loi non linéaire, on **linéarise** (par exemple $T^2$ en fonction de $\ell$ pour un pendule, $\ln y$ en fonction de $x$ pour une exponentielle).

## Exemple corrigé

**Énoncé.** On mesure la période d'un pendule 6 fois : 2,01 ; 2,03 ; 1,99 ; 2,02 ; 2,00 ; 2,03 s. Donner le résultat avec son incertitude-type.

**Solution.**
1. Moyenne : $\bar T = 2{,}013$ s.
2. Écart-type expérimental : $\sigma \approx 0{,}016$ s.
3. $u(\bar T) = \sigma/\sqrt6 \approx 0{,}0065$ s.
4. Résultat : $T = 2{,}013 \pm 0{,}007$ s.

## Exemple corrigé (propagation)

**Énoncé.** $g = \frac{4\pi^2\ell}{T^2}$ avec $\ell = 1{,}000 \pm 0{,}002$ m et $T = 2{,}006 \pm 0{,}004$ s. Calculer $g$ et $u(g)$.

**Solution.** $g = 9{,}81$ m·s⁻². $\frac{u(g)}{g} = \sqrt{\left(\frac{0{,}002}{1}\right)^2 + \left(2\times\frac{0{,}004}{2{,}006}\right)^2} \approx 4{,}5\cdot10^{-3}$, donc $u(g) \approx 0{,}04$ m·s⁻² : $g = 9{,}81 \pm 0{,}04$ m·s⁻². L'incertitude sur $T$ domine (elle compte double).

## Pièges classiques

- Ne pas donner plus de deux chiffres significatifs à l'incertitude, et arrondir la valeur au même rang.
- Une incertitude n'est pas une erreur : elle caractérise la dispersion possible, pas l'écart à une valeur vraie inconnue.
- Moyenner réduit l'incertitude aléatoire, pas les erreurs systématiques.
