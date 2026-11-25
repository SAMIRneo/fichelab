# Audit FicheLab — filière `but-gea`

Audit des trois lots de fiches prototypes BUT GEA (Gestion des entreprises et des administrations).
Périmètre : `data/butgea-mat-part-A.json`, `data/butgea-mat-part-B.json`,
`data/butgea-mat-part-C.json`. Vérification indépendante par
`data/_verify_butgea.py` (lecture seule). Aucune modification de `index.html`,
`inject_app.py` ni `audit_filieres.py`.

## Compteurs

| Lot | Fiches | Points | Questions | QCM | Texte | SVG |
|---|---:|---:|---:|---:|---:|---:|
| A — Gestion / Comptabilité | 20 | 240 | 180 | 140 | 40 | 60 |
| B — Droit / Marketing / Communication | 20 | 240 | 180 | 140 | 40 | 60 |
| C — Informatique / Maths-stats / Anglais / Méthodologie | 20 | 240 | 180 | 140 | 40 | 60 |
| **Total `but-gea`** | **60** | **720** | **540** | **420** | **120** | **180** |

Chaque fiche : **12 points**, **9 questions** (7 QCM + 2 questions texte,
soit au moins 6 QCM et 2 texte, corrections détaillées), **7 blocs**,
**3 schémas SVG**, source officielle non vide.

Génération (`fixtures.valider_et_ecrire`, sans erreur) :

```
OK butgea-mat-part-A.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK butgea-mat-part-B.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK butgea-mat-part-C.json : 20 fiches, 240 points, 180 questions, 60 SVG
```

## Répartition

### Par matière (matières exactes du questionnaire)

| Matière | Fiches |
|---|---:|
| Gestion | 10 |
| Comptabilité | 10 |
| Droit | 7 |
| Marketing | 7 |
| Communication | 6 |
| Informatique | 7 |
| Maths / stats | 7 |
| Anglais professionnel | 3 |
| Méthodologie | 3 |

### Par année (chaque fiche vise une seule année)

| Lot | BUT1 | BUT2 | BUT3 |
|---|---:|---:|---:|
| A | 8 | 7 | 5 |
| B | 7 | 8 | 5 |
| C | 7 | 7 | 6 |
| **Total** | **22** | **22** | **16** |

### Codes

- Lot A : `GE1.`–`GE10.` (Gestion) · `CP1.`–`CP10.` (Comptabilité)
- Lot B : `DR1.`–`DR7.` (Droit) · `MK1.`–`MK7.` (Marketing) · `CO1.`–`CO6.` (Communication)
- Lot C : `IN1.`–`IN7.` (Informatique) · `MS1.`–`MS7.` (Maths / stats) ·
  `AN1.`–`AN3.` (Anglais professionnel) · `ME1.`–`ME3.` (Méthodologie)

Toutes les fiches déclarent `filieres = ["but-gea"]`, une année unique dans
`{BUT1, BUT2, BUT3}` et une matière de la liste ci-dessus.

## Blocs d'affichage

Ordre strict vérifié sur les 60 fiches, **une seule variante** :

`intro` → `formule` → `grille` → `liste` → `etapes` → `attention` → `exemples`

Aucun bloc manquant, ajouté ou permuté.

## Schémas SVG

- **180 SVG**, exactement 3 par fiche (fabriqués par `diag()` à partir de
  `fixtures.py` : `svg_grille`, `svg_etapes`, `svg_compare`).
- Tous analysables par `xml.etree.ElementTree` (viewBox cohérente).
- Coordonnées de tous les textes dans le cadre `viewBox`.
- Aucune occurrence de `<script`, d'attribut `on*`, de `javascript:` ni de
  `<foreignObject` (`INTERDIT_SVG` de `fixtures.py`).

## Doublons de titres

| Contrôle | Résultat |
|---|---:|
| Doublons dans les 3 lots `but-gea` | **0** (60 titres uniques sur 60 fiches) |
| Titres `but-gea` présents dans un autre lot de `data/` | **0** |
| Titres `but-gea` déjà présents dans `index.html` | **0** |

Les 60 titres sont préfixés `Chapitre GEA <code> · …`, ce qui garantit leur
unicité dans le catalogue. Un titre initial `Chapitre MK2. · Segmentation,
ciblage et positionnement` collisionnait avec le lot `but-tc` : le préfixe
`GEA` a été ajouté aux trois générateurs avant la vérification finale.

## Artefacts CJK

Recherche regex `[\u4e00-\u9fff\u3040-\u30ff]` sur la sérialisation complète
de chaque fiche **et sur les trois scripts générateurs** : **0 occurrence**.

## Sources officielles

Chaque fiche porte un champ `source` non vide qui explicite :

- **Tronc commun** : référentiel BUT GEA, arrêté du 11 mars 2020
  (BO n°12 du 19 mars 2020), programme national, ressources R1 à R6,
  éduscol / iut.fr / onisep.fr.
- **Droit** : Code civil (art. 1101, 1104, 1218, 1240), Code de commerce
  (L121-1, L420-1, L210-1), Code de la consommation (L111-1), Code du travail.
- **Comptabilité / gestion** : plan comptable général (arrêté du 22 juin 1999),
  Code général des impôts, normes ISO 9000 / 9001.
- **Informatique / maths / méthodologie** : règlement UE 2016/679 (RGPD),
  ISO 690, mathématiques financières, statistiques et probabilités.

## Anomalies constatées

1. Les lots `but-gea` ne sont **pas encore injectés** dans `index.html` :
   l'identifiant `but-gea` y figure uniquement dans la liste des filières et
   dans quelques fiches historiques du catalogue de base. L'injection est
   hors périmètre de cette mission (`index.html` et `inject_app.py` n'ont pas
   été modifiés).
2. Le script `data/_verify_butgea.py` est un utilitaire de contrôle en lecture
   seule ajouté pour rendre l'audit reproductible ; il ne modifie aucun lot.

## Verdict

**CONFORME.** Les 60 fiches `but-gea` respectent le prototype FicheLab :
compteurs, répartition, matières et années exactes, ordre des 7 blocs, 3 SVG
valides par fiche, sources officielles, aucun doublon de titre, aucun artefact
CJK. L'audit automatisé rapporte **0 erreur**.
