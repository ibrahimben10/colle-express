---
titre: Représentation des nombres
---
## L'essentiel

En machine, tout est codé en binaire sur un nombre fini de bits. Les entiers sont représentés exactement dans une plage limitée ; les réels sont approchés par des **flottants**, avec des erreurs d'arrondi.

## Bases de numération

$n = \sum_k a_k\,b^k$ avec $0 \le a_k < b$. Exemple : $13 = 1101_2$ ($8 + 4 + 1$), $\mathrm{FF}_{16} = 255$.

> **Méthode — Conversion en base 2.** Divisions euclidiennes successives par 2 : les restes donnent les chiffres, du poids faible au poids fort.

Sur $n$ bits, on code les entiers naturels de $0$ à $2^n - 1$.

## Entiers relatifs : complément à deux

[[fig:i-nombres-1]]

Sur $n$ bits, on représente les entiers de $-2^{n-1}$ à $2^{n-1} - 1$ ; un entier négatif $x$ est codé comme l'entier naturel $2^n + x$. Le bit de poids fort indique le signe.

Pour obtenir l'opposé : inverser tous les bits puis ajouter 1. L'addition fonctionne normalement, mais un dépassement de capacité donne un résultat faux (en Python, les `int` ont une taille illimitée, mais pas ceux de NumPy).

## Flottants

[[fig:i-nombres-2]]

> **Définition — Norme IEEE 754 (double précision).** $x = (-1)^s \times 1{,}m \times 2^{e - 1023}$, avec 52 bits de mantisse : environ 16 chiffres décimaux significatifs.

Conséquences :
- erreurs d'arrondi : `0.1 + 0.2 == 0.3` vaut `False` ;
- **absorption** : `1e16 + 1 - 1e16` donne 0 ;
- **cancellation** : la soustraction de deux nombres très proches perd des chiffres significatifs.

## Ce qui est exigible

Le programme demande de connaître le principe (signe, mantisse, exposant) et les **limites de précision**, en particulier pour les comparaisons. Le détail du format IEEE 754 (nombre de bits, nombres dénormalisés, infinis, `NaN`, modes d'arrondi) et les conversions de base à la main ne sont pas exigibles, mais aident à comprendre.

## Précision relative

L'écart entre 1 et le flottant suivant vaut $\varepsilon = 2^{-52} \approx 2{,}2\cdot10^{-16}$ (`sys.float_info.epsilon`). Tout calcul flottant comporte une erreur relative de cet ordre, qui peut s'accumuler.

```python
from math import isclose
0.1 + 0.2 == 0.3                 # False
isclose(0.1 + 0.2, 0.3)          # True
abs((0.1 + 0.2) - 0.3) < 1e-12   # True
```

## Entiers Python

Les `int` de Python sont en **multiprécision** : pas de dépassement, mais le coût d'une opération dépend du nombre de chiffres (on ne peut plus la compter comme élémentaire pour de très grands entiers). Les tableaux NumPy, eux, utilisent des entiers de taille fixe (souvent 64 bits) et peuvent déborder.

## Exemple corrigé

**Énoncé.** Écrire $-6$ sur 8 bits en complément à deux.

**Solution.**
1. $6 = 00000110_2$.
2. On inverse les bits : $11111001$.
3. On ajoute 1 : $11111010$. Vérification : $2^8 - 6 = 250 = 11111010_2$.

## Pièges classiques

- Ne jamais tester l'égalité de deux flottants avec `==`.
- La plupart des décimaux (comme 0,1) n'ont pas de représentation binaire finie.
