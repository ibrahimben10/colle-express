---
titre: Bases de données et SQL
---
## L'essentiel

Une base de données relationnelle stocke l'information dans des **tables** (relations). Chaque ligne est un enregistrement, chaque colonne un **attribut**. Le langage SQL permet de les interroger.

## Schéma relationnel

[[fig:i-sql-1]]

- **Clé primaire** : attribut (ou ensemble d'attributs) qui identifie chaque ligne de manière unique.
- **Clé étrangère** : attribut qui fait référence à la clé primaire d'une autre table ; il traduit une association entre entités.

## Requêtes de base

```sql
SELECT nom, note                 -- projection
FROM Eleve
WHERE note >= 10 AND id_classe = 1   -- sélection
ORDER BY note DESC
LIMIT 5;
```

`SELECT DISTINCT` supprime les doublons ; `LIKE 'A%'` filtre sur un motif.

## Jointure

[[fig:i-sql-2]]

```sql
SELECT e.nom, c.nom
FROM Eleve AS e
JOIN Classe AS c ON e.id_classe = c.id;
```

## Agrégation

```sql
SELECT id_classe, COUNT(*), AVG(note)
FROM Eleve
GROUP BY id_classe
HAVING AVG(note) > 12;
```

> **Propriété.** `WHERE` filtre les lignes **avant** le regroupement ; `HAVING` filtre les **groupes** après agrégation (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`).

Sous-requêtes : `WHERE note > (SELECT AVG(note) FROM Eleve)`.

## Exemple corrigé

**Énoncé.** Donner le nom de chaque classe et le nombre de ses élèves ayant au moins 10.

**Solution.**
```sql
SELECT c.nom, COUNT(*)
FROM Eleve AS e
JOIN Classe AS c ON e.id_classe = c.id
WHERE e.note >= 10
GROUP BY c.id, c.nom;
```
On joint, on filtre les lignes, puis on compte par classe.

## Pièges classiques

- Mettre une condition sur un agrégat dans `WHERE` au lieu de `HAVING`.
- Oublier la condition `ON` : on obtient le produit cartésien de toutes les lignes.
- Dans un `GROUP BY`, ne sélectionner que les attributs du regroupement et des agrégats.
