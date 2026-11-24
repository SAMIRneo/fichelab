# Audit FicheLab — filière `but-tc`

Audit manuel des trois lots de fiches prototypes BUT Techniques de commercialisation.
Périmètre : `data/buttc-mat-part-A.json`, `data/buttc-mat-part-B.json`,
`data/buttc-mat-part-C.json`. Aucune modification de `index.html`,
`inject_app.py` ni `audit_filieres.py`.

## Compteurs

| Lot | Fiches | Points | Questions | QCM | Texte | SVG |
|---|---:|---:|---:|---:|---:|---:|
| A — Marketing / Communication | 20 | 240 | 180 | 140 | 40 | 60 |
| B — Gestion | 10 | 120 | 90 | 70 | 20 | 30 |
| C — Droit, Maths/stats, Informatique, Anglais, Méthodologie | 20 | 240 | 180 | 140 | 40 | 60 |
| **Total `but-tc`** | **50** | **600** | **450** | **350** | **100** | **150** |

Chaque fiche : **12 points**, **9 questions** (7 QCM + 2 questions texte,
soit au moins 6 QCM et 2 texte), **7 blocs**, **3 schémas**.

Génération : `python data/gen_buttc_C.py` →
`OK buttc-mat-part-C.json : 20 fiches, 240 points, 180 questions, 60 SVG`
(validation `fixtures.valider_et_ecrire` sans erreur).

## Répartition

### Par matière

| Matière | Fiches |
|---|---:|
| Marketing | 10 |
| Communication | 10 |
| Gestion | 10 |
| Droit | 6 |
| Maths / stats | 6 |
| Informatique | 4 |
| Anglais professionnel | 2 |
| Méthodologie | 2 |

### Par année (une fiche peut viser deux années)

| Lot | BUT1 | BUT2 | BUT3 |
|---|---:|---:|---:|
| A | 8 | 10 | 6 |
| B | 2 | 7 | 3 |
| C | 9 | 13 | 7 |
| **Total** | **19** | **30** | **16** |

### Codes du lot C

`DR1.`–`DR6.` (Droit) · `MS1.`–`MS6.` (Maths / stats) ·
`IN1.`–`IN4.` (Informatique) · `AN1.`–`AN2.` (Anglais professionnel) ·
`ME1.`–`ME2.` (Méthodologie).

Toutes les fiches des trois lots déclarent `filieres = ["but-tc"]` et des années
appartenant exclusivement à `{BUT1, BUT2, BUT3}`.

## Blocs d'affichage

Ordre strict vérifié sur les 50 fiches, **une seule variante** :

`intro` → `formule` → `grille` → `liste` → `etapes` → `attention` → `exemples`

Aucun bloc manquant, ajouté ou permuté.

## Schémas SVG

- **150 SVG** au total, exactement 3 par fiche.
- Tous analysables par `xml.etree.ElementTree`.
- Aucune occurrence de `<script`, d'attribut `on*`, de `javascript:` ou de
  `<foreignObject` (`INTERDIT_SVG`).
- Coordonnées des textes dans le cadre `viewBox`.
- Trois familles utilisées : `svg_grille`, `svg_etapes`, `svg_compare`.

## Doublons de titres

| Contrôle | Résultat |
|---|---:|
| Doublons dans les 3 lots `but-tc` | **0** |
| Titres `but-tc` présents dans un doublon du catalogue `data/` | **0** |
| Doublons dans le catalogue embarqué de `index.html` | **0** |

Le dossier `data/` contient 195 paires de titres dupliquées **préexistantes**,
toutes hors filière `but-tc` (fichiers `agent*.json`, lots d'autres filières).
Aucun titre des lots A/B/C n'y est impliqué.

## Artefacts CJK

Recherche regex `[\u4e00-\u9fff\u3040-\u30ff]` sur la sérialisation complète
de chaque fiche : **0 occurrence** dans les 50 fiches.

## Sources officielles

- **A** : référentiel BUT « Techniques de commercialisation », arrêté du
  11 mars 2020 (BO n°12 du 19 mars 2020) ; programme national 2022, arrêté du
  15 avril 2022 (BO n°19 du 12 mai 2022) ; blocs Marketing / Vente /
  Communication commerciale.
- **B** : même référentiel ; plan comptable général (arrêté du 22 juin 1999),
  Code de commerce, Code général des impôts, éduscol.
- **C** : même référentiel ; Code civil (art. 1103 et suivants, 1218, 1231,
  1240, 1245, 2224), Code de commerce (L210-1 à L227-10), Code de la
  consommation (L111-1, L121-1, L217-4, L221-18, L611-1), Code du travail
  (L1221-1, L1242-1, L3121-27, L3141-3, L1237-11), Code de la propriété
  intellectuelle (L111-1, L611-1, L711-1), règlement UE 2016/679 (RGPD),
  CECRL du Conseil de l'Europe, Insee et éduscol.

Chaque fiche porte un champ `source` non vide qui explicite ces références
et les notions du chapitre.

## Anomalies constatées

1. `BUTTC-PROGRAMME.md`, annoncé comme déjà livré, est **absent du disque**
   (recherche récursive dans `fichelab/`). Non recréé : instruction « ne pas
   refaire ». À restaurer si le document est attendu dans la livraison.
2. Les lots `but-tc` ne sont **pas encore injectés** dans `index.html`
   (catalogue embarqué inchangé, 4 filières prototype). Injection hors
   périmètre de cet audit : `index.html` et `inject_app.py` n'ont pas été
   modifiés.

## Modalité d'exécution

Aucun outil `subagent` / `task` n'est exposé par ce harness (recherche dans le
catalogue d'outils vide). Le lot C a donc été produit directement, par copie de la structure de
`gen_generale_modele.py` et des lots `gen_buttc_A.py` / `gen_buttc_B.py`,
avec `fixtures.py` pour les 12 points, les 9 questions, les 7 blocs, les 3
`diag()` et la validation.

## Verdict

**CONFORME.** Les 50 fiches `but-tc` respectent le prototype FicheLab :
compteurs, répartition, matières exactes, années, ordre des 7 blocs, 3 SVG
valides par fiche, sources officielles, aucun doublon de titre impliquant
`but-tc`, aucun artefact CJK.
