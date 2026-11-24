# Audit FicheLab — filière `lic-staps` (Licence STAPS)

> Audit de conformité des trois lots prototype générés pour la filière **lic-staps** (162 357 vœux Parcoursup 2026).
> Référentiel : arrêté du 6 avril 2021 · BO spécial n° 7 du 17 février 2022 · éduscol · Code du sport.
> Contrôles exécutés avec `data/fixtures.py::valider_fiche()` sur les 60 fiches, plus un contrôle croisé des titres, préfixes, matières, années et caractères CJK.

## 1. Résultats globaux

| Contrôle | Valeur | Attendu | Verdict |
|---|---|---|---|
| Fiches prototype | **60** | 3 lots × 20 | ✅ |
| Points de cours | **720** | 12 par fiche | ✅ |
| Questions corrigées | **540** | 9 par fiche | ✅ |
| — dont QCM | **420** | ≥ 6 par fiche (7 ici) | ✅ |
| — dont rédaction | **120** | ≥ 2 par fiche | ✅ |
| Schémas SVG | **180** | 3 par fiche | ✅ |
| Ordre des 7 blocs | **60 / 60 conformes** | `intro, formule, grille, liste, etapes, attention, exemples` | ✅ |
| `diag()` par fiche | **3** | 2 à 4 (3 ici) | ✅ |
| `filieres` | **`["lic-staps"]`** | identique pour les 60 fiches | ✅ |
| `annees` | `L1`, `L2`, `L3` | tableaux d'une seule année | ✅ |
| Matières du questionnaire | **9 matières exactes** | aucune matière inventée | ✅ |
| Titres uniques | **60 / 60** | 0 doublon | ✅ |
| Préfixes de chapitres | **60 uniques** | PSY1-10, ST1-10, DR1-7, EC1-7, MU1-6, PF1-5, AN1-5, IN1-5, MS1-5 | ✅ |
| Artefacts CJK | **0** | 0 | ✅ |
| SVG interdits (script/on*/javascript:) | **0** | 0 | ✅ |
| `valider_et_ecrire()` | **OK, sans erreur** | `OK ...` pour chaque lot | ✅ |

## 2. Couverture par lot

| Lot | Générateur | JSON | Fiches | Points | Questions | SVG |
|---|---|---|---|---|---|---|
| A | `data/gen_licstaps_A.py` | `data/licstaps-mat-part-A.json` | 20 | 240 | 180 | 60 |
| B | `data/gen_licstaps_B.py` | `data/licstaps-mat-part-B.json` | 20 | 240 | 180 | 60 |
| C | `data/gen_licstaps_C.py` | `data/licstaps-mat-part-C.json` | 20 | 240 | 180 | 60 |
| **Total** | — | — | **60** | **720** | **540** | **180** |

Chaque lot a produit une ligne `OK licstaps-mat-part-X.json : 20 fiches, 240 points, 180 questions, 60 SVG` sans erreur ni avertissement.

## 3. Répartition par matière

| Matière | Fiches | Préfixes |
|---|---|---|
| Psychologie | 10 | PSY1. – PSY10. |
| Statistiques | 10 | ST1. – ST10. |
| Droit | 7 | DR1. – DR7. |
| Économie | 7 | EC1. – EC7. |
| Méthodologie universitaire | 6 | MU1. – MU6. |
| Français | 5 | PF1. – PF5. |
| Anglais | 5 | AN1. – AN5. |
| Informatique | 5 | IN1. – IN5. |
| Maths / stats | 5 | MS1. – MS5. |
| **Total** | **60** | — |

## 4. Répartition par année

| Année | Fiches | Détail |
|---|---|---|
| L1 | 21 | PSY1-4, ST1-2, DR1-3, EC1-2, MU1-2, PF1-2, AN1-2, IN1-2, MS1-2 |
| L2 | 23 | PSY5-7, ST3-6, DR4-5, EC3-5, MU3-5, PF3-4, AN3-4, IN3-4, MS3-4 |
| L3 | 16 | PSY8-10, ST7-10, DR6-7, EC6-7, MU6, PF5, AN5, IN5, MS5 |
| **Total** | **60** | — |

## 5. Contrôles détaillés

- **Validation unitaire :** les 60 fiches passent `fixtures.valider_fiche()` sans aucune erreur (champs obligatoires, 10-14 points, 8-10 questions, ≥ 6 QCM et ≥ 2 texte, corrections présentes, types de blocs, SVG analysables et bornés, titres ≥ 12 caractères).
- **Doublons :** 0 titre dupliqué, 0 préfixe dupliqué sur l'ensemble des trois lots.
- **CJK :** recherche par expression rationnelle `[\u4e00-\u9fff\u3040-\u30ff]` sur le contenu sérialisé de chaque fiche → 0 occurrence. Les trois caractères parasites détectés en cours de rédaction (`她`, `微`, `决定` dans le lot A ; `特`, `高`, `发`, `总`, `较` dans le lot B ; `主`, `题` dans le lot C) ont été supprimés avant la validation finale.
- **Blocs :** ordre strict vérifié sur 60/60 fiches ; aucun bloc manquant ou interverti.
- **Questions :** chaque fiche contient 7 QCM (6 notions + 1 QCM transversal) et 2 questions de rédaction avec correction détaillée.
- **Sources :** chaque fiche porte la référence « arrêté du 6 avril 2021 · BO spécial n° 7 du 17 février 2022 · éduscol » et la liste des notions du chapitre.

## 6. Problèmes détectés

**Aucun problème détecté — audit CONFORME.**

> Correctifs apportés pendant la production : (1) la fabrique commune `gen_licstaps_common.py` initialisait trois clés absentes des configurations et a été alignée sur les listes `exemples`/`attention`/`etapes` ; (2) les artefacts CJK listés au §5 ont été supprimés ; (3) une mauvaise indexation de réponse dans le QCM `IN5` (cardiogramme) a été corrigée. Après ces corrections, les trois lots ont été régénérés et revalidés sans erreur.
