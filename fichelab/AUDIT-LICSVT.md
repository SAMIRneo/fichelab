# Audit FicheLab — filière `lic-svt` (Licence Sciences de la vie)

> Audit de conformité des trois lots prototype générés pour la filière **lic-svt** (100 640 vœux Parcoursup 2026).
> Référentiel : arrêté du 6 avril 2021 · BO spécial n° 7 du 17 février 2022 · éduscol · Code de la santé publique · RGPD.
> Contrôles exécutés avec `data/fixtures.py::valider_fiche()` sur les 60 fiches, plus un contrôle croisé des titres, préfixes, matières, années et caractères CJK, et une comparaison des 60 titres avec l'ensemble des fichiers JSON déjà présents dans `data/`.

## 1. Résultats globaux

| Contrôle | Valeur | Attendu | Verdict |
|---|---|---|---|
| Fiches prototype | **60** | 3 lots × 20 | ✅ |
| Points de cours | **720** | 12 par fiche | ✅ |
| Questions corrigées | **540** | 9 par fiche | ✅ |
| — dont QCM | **420** | ≥ 6 par fiche (7 ici) | ✅ |
| — dont rédaction | **120** | ≥ 2 par fiche (2 ici) | ✅ |
| Schémas SVG | **180** | 3 par fiche | ✅ |
| Ordre des 7 blocs | **60 / 60 conformes** | `intro, formule, grille, liste, etapes, attention, exemples` | ✅ |
| `diag()` par fiche | **3** | 2 à 4 (3 ici) | ✅ |
| `filieres` | **`["lic-svt"]`** | identique pour les 60 fiches | ✅ |
| `annees` | `L1` (17), `L2` (24), `L3` (19) | tableaux d'une seule année | ✅ |
| Matières du questionnaire | **9 matières exactes** | aucune matière inventée | ✅ |
| Titres uniques | **60 / 60** | 0 doublon interne | ✅ |
| Collisions avec le catalogue | **0** | 0 titre identique à un autre fichier JSON | ✅ |
| Préfixes de chapitres | **60 uniques** | ST1-10, IN1-10, MU1-10, DR1-5, EC1-5, LSPF1-5, LSPAN1-5, PSY1-5, MS1-5 | ✅ |
| Artefacts CJK | **0** | 0 | ✅ |
| SVG interdits (script/on*/javascript:) | **0** | 0 | ✅ |
| `valider_et_ecrire()` | **OK, sans erreur** | `OK ...` pour chaque lot | ✅ |

## 2. Couverture par lot

| Lot | Générateur | JSON | Fiches | Points | Questions | SVG |
|---|---|---|---|---|---|---|
| A | `data/gen_licsvt_A.py` | `data/licsvt-mat-part-A.json` | 20 | 240 | 180 | 60 |
| B | `data/gen_licsvt_B.py` | `data/licsvt-mat-part-B.json` | 20 | 240 | 180 | 60 |
| C | `data/gen_licsvt_C.py` | `data/licsvt-mat-part-C.json` | 20 | 240 | 180 | 60 |
| **Total** | — | — | **60** | **720** | **540** | **180** |

Chaque lot a produit une ligne `OK licsvt-mat-part-X.json : 20 fiches, 240 points, 180 questions, 60 SVG` sans erreur ni avertissement.

## 3. Répartition par matière

| Matière (questionnaire) | Fiches | Préfixes |
|---|---|---|
| Statistiques | 10 | ST1. – ST10. |
| Informatique | 10 | IN1. – IN10. |
| Méthodologie universitaire | 10 | MU1. – MU10. |
| Droit | 5 | DR1. – DR5. |
| Économie | 5 | EC1. – EC5. |
| Français | 5 | LSPF1. – LSPF5. |
| Anglais | 5 | LSPAN1. – LSPAN5. |
| Psychologie | 5 | PSY1. – PSY5. |
| Maths / stats | 5 | MS1. – MS5. |
| **Total** | **60** | — |

**Contrainte biologique respectée :** le questionnaire ne contient pas la matière « Biologie ». Le contenu biologique (cellule, génétique, physiologie, écologie, évolution, biochimie, microbiologie, botanique, zoologie, biologie moléculaire) est réparti dans les neuf matières ci-dessus, avec des titres de fiches biologiques explicites : bioinformatique et bases de séquences en `Informatique`, plans d'expérience et données omiques en `Statistiques`, modélisation des populations et lecture critique des chiffres en `Maths / stats`, démarche scientifique et protocoles en `Méthodologie universitaire`, bioéthique et données de santé en `Droit`, économie et industries biotech en `Économie`, textes biologiques en `Français`, vocabulaire et publication en `Anglais`, comportements de santé et stress en contexte de soin en `Psychologie`. Aucune matière n'a été substituée ni ajoutée.

## 4. Répartition par année

| Année | Fiches | Détail |
|---|---|---|
| L1 | 17 | ST1-2, IN1-2, MU1-3, DR1, EC1, LSPF1-2, LSPAN1-2, PSY1-2, MS1-2 |
| L2 | 24 | ST3-6, IN3-6, MU4-7, DR2-3, EC2-3, LSPF3-4, LSPAN3-4, PSY3-4, MS3-4 |
| L3 | 19 | ST7-10, IN7-10, MU8-10, DR4-5, EC4-5, LSPF5, LSPAN5, PSY5, MS5 |
| **Total** | **60** | — |

## 5. Contrôles détaillés

- **Validation unitaire :** les 60 fiches passent `fixtures.valider_fiche()` sans aucune erreur (champs obligatoires, 12 points, 9 questions, ≥ 6 QCM et ≥ 2 texte, corrections présentes, types de blocs, SVG analysables et bornés, titres ≥ 12 caractères).
- **Doublons internes :** 0 titre dupliqué et 0 préfixe dupliqué sur l'ensemble des trois lots.
- **Doublons externes :** les 60 titres ont été comparés aux titres de tous les autres fichiers JSON du dossier `data/` → 0 collision. Les préfixes partagés avec d'autres filières (ST, IN, DR, EC, MU, PSY, MS) portent tous des titres biologiques distincts.
- **CJK :** recherche par expression rationnelle `[\u4e00-\u9fff\u3040-\u30ff]` sur le contenu sérialisé de chaque fiche et sur les trois scripts générateurs → 0 occurrence. Les artefacts détectés en cours de rédaction (`镰` dans le lot A ; `结`, `构`, `重`, `新`, `果`, `与`, `服`, `务` dans le lot B ; `操`, `作`, `长` dans le lot C) ont été supprimés avant la validation finale.
- **Blocs :** ordre strict vérifié sur 60/60 fiches ; aucun bloc manquant ou interverti ; chaque bloc porte les clés adaptées à son type (`texte`, `eq`/`leg` ou `items`).
- **Questions :** chaque fiche contient 7 QCM (6 notions + 1 QCM transversal) et 2 questions de rédaction avec correction détaillée. Certaines questions comportent un calcul chiffré (moyenne et écart-type, intervalle de confiance, probabilité génétique, conversion d'unités, croissance exponentielle, taille d'effet).
- **Schémas :** 3 `diag()` par fiche construits par `svg_grille`, `svg_etapes` et `svg_compare` ; tous les SVG sont analysables par `xml.etree.ElementTree` et toutes les coordonnées de texte sont dans le `viewBox`.
- **Sources :** chaque fiche porte la référence « arrêté du 6 avril 2021 · BO spécial n° 7 du 17 février 2022 · éduscol » et la liste des notions du chapitre. Les volets droit, bioéthique et données de santé s'appuient en outre sur le Code de la santé publique et le RGPD.

## 6. Problèmes détectés

**Aucun problème détecté — audit CONFORME.**

> Correctifs apportés pendant la production : (1) les artefacts CJK listés au §5 ont été éliminés dans les trois scripts ; (2) plusieurs coquilles linguistiques et traductions automatiques parasite ont été corrigées dans les lots B et C ; (3) une clé inutilisée du lot C a été retirée. Après ces corrections, les trois lots ont été régénérés et revalidés sans erreur.
