---
titre: Mesures et incertitudes
---
## L'essentiel

Toute mesure est entachée d'erreurs ; le résultat s'écrit $x = x_{\text{mesuré}} \pm u(x)$, où $u(x)$ est l'**incertitude-type**, avec une unité et un nombre de chiffres significatifs cohérent.

## Deux façons d'évaluer une incertitude

[[fig:px-incertitudes-1]]

> **Définition — Évaluation de type A (statistique).** Sur $N$ mesures indépendantes de moyenne $\bar x$ et d'écart-type $\sigma$ : $u(\bar x) = \dfrac{\sigma}{\sqrt N}$.

> **Définition — Évaluation de type B.** Une seule mesure : on estime $u$ à partir des données de l'instrument. Lecture sur une graduation de pas $\Delta$ : $u = \dfrac{\Delta}{2\sqrt3}$ ; tolérance $\pm a$ du constructeur : $u = \dfrac{a}{\sqrt3}$.

## Propagation des incertitudes

| Relation | Incertitude-type |
|---|---|
| $y = x_1 + x_2$ ou $x_1 - x_2$ | $u(y) = \sqrt{u(x_1)^2 + u(x_2)^2}$ |
| $y = x_1x_2$ ou $x_1/x_2$ | $\dfrac{u(y)}{\lvert y\rvert} = \sqrt{\left(\dfrac{u(x_1)}{x_1}\right)^2 + \left(\dfrac{u(x_2)}{x_2}\right)^2}$ |

Pour les cas plus compliqués, on utilise une **simulation de Monte-Carlo** (tirages aléatoires des grandeurs d'entrée).

## Comparer deux valeurs

> **Définition — Écart normalisé.** $E_N = \dfrac{|x_1 - x_2|}{\sqrt{u(x_1)^2 + u(x_2)^2}}$ ; les valeurs sont jugées compatibles si $E_N \lesssim 2$.

## Régression linéaire

[[fig:px-incertitudes-2]]

Pour valider un modèle affine : tracer les points avec leurs barres d'incertitude, vérifier que la droite passe par (presque) toutes les barres et que les **résidus** sont répartis sans tendance.

## Exemple corrigé

**Énoncé.** On mesure la période d'un pendule 6 fois : 2,01 ; 2,03 ; 1,99 ; 2,02 ; 2,00 ; 2,03 s. Donner le résultat avec son incertitude-type.

**Solution.**
1. Moyenne : $\bar T = 2{,}013$ s.
2. Écart-type expérimental : $\sigma \approx 0{,}016$ s.
3. Incertitude-type sur la moyenne (type A) : $u(\bar T) = \sigma/\sqrt6 \approx 0{,}0065$ s.
4. Résultat : $T = 2{,}013 \pm 0{,}007$ s (incertitude arrondie à 1 ou 2 chiffres significatifs, valeur arrondie au même rang).

## Pièges classiques

- Ne pas donner plus de deux chiffres significatifs à l'incertitude, et arrondir la valeur au même rang.
- Une incertitude n'est pas une erreur : elle caractérise la dispersion possible, pas l'écart à une valeur vraie inconnue.
