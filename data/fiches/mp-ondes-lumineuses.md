---
titre: Modèle scalaire des ondes lumineuses
---
## L'essentiel

La lumière est décrite par une grandeur scalaire $s(M,t)$, une **vibration lumineuse**. Les détecteurs ne mesurent que l'**intensité** $I = K\langle s^2\rangle$, moyennée sur leur temps de réponse.

## Chemin optique

Le chemin optique le long d'un rayon de A à B est $(AB) = \int_A^B n\,\mathrm ds$. Le retard de phase correspondant est $\varphi = \dfrac{2\pi}{\lambda_0}(AB)$, avec $\lambda_0$ la longueur d'onde dans le vide.

> **Théorème de Malus.** Les rayons lumineux sont orthogonaux aux surfaces d'onde ; le chemin optique entre deux surfaces d'onde est le même le long de tous les rayons.

[[fig:mp-ondes-lumineuses-1]]

Conséquences : ondes sphériques autour d'une source ponctuelle, planes après une lentille si la source est au foyer ; une lentille n'introduit pas de différence de chemin optique entre un objet et son image (stigmatisme).

## Modèle des trains d'onde

[[fig:mp-ondes-lumineuses-2]]

Une source réelle émet des trains d'onde de durée moyenne $\tau_c$ ; leurs phases sont aléatoires. La **longueur de cohérence** vaut $\ell_c = c\,\tau_c$, et la largeur spectrale vérifie $\Delta\nu \approx 1/\tau_c$.

## Ordres de grandeur

| Source | $\ell_c$ |
|---|---|
| lumière blanche | 1 µm |
| lampe spectrale | 1 mm à 1 cm |
| laser He-Ne | 10 cm à plusieurs mètres |

## Exemple corrigé

**Énoncé.** Une lame de verre d'indice $n = 1{,}5$ et d'épaisseur $e = 10$ µm est placée sur un rayon. Quel chemin optique supplémentaire introduit-elle ?

**Solution.**
1. Sans lame, le rayon parcourt $e$ dans l'air ($n \approx 1$) : chemin optique $e$.
2. Avec la lame : $ne$.
3. Supplément : $(n - 1)e = 5$ µm, soit environ 9 longueurs d'onde pour $\lambda_0 = 560$ nm : un décalage de 9 franges dans un interféromètre.

## Pièges classiques

- La réflexion sur un milieu plus réfringent ajoute un déphasage de $\pi$ (soit $\lambda/2$ sur le chemin optique).
- Un détecteur ne « voit » pas la phase : seules des différences de phase sont observables, par interférences.
