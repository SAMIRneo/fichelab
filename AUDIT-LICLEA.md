# Audit — filière `lic-lea` (lots A, B, C)

> Date : 24 novembre 2026 · Racine : `fichelabs/fichelab` · Fichiers audités :
> `data/liclea-mat-part-A.json`, `data/liclea-mat-part-B.json`,
> `data/liclea-mat-part-C.json`.
> Contrôle exécuté avec `data/fixtures.py :: valider_fiche()` sur **60 fiches**,
> complété par un contrôle croisé des titres, des blocs, des SVG, des préfixes,
> des matières, des années et des artefacts CJK (`data/_verify_liclea.py`).

## 1. Compteurs et conformité structurelle

| Lot | Générateur | Fiches | Points | Questions | QCM | Rédaction | SVG | Erreurs `valider_fiche()` |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| A | `gen_liclea_A.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| B | `gen_liclea_B.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| C | `gen_liclea_C.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| **Total** | — | **60** | **720** | **540** | **420** | **120** | **180** | **0** |

Chaque fiche respecte le prototype : **12 points**, **9 questions** (7 QCM + 2
rédaction, toutes corrigées), **7 blocs** dans l'ordre strict
`intro → formule → grille → liste → etapes → attention → exemples`, **3 schémas**.
Toutes les fiches déclarent `filieres = ["lic-lea"]` et des `annees` dans
`{L1, L2, L3}`.

Sorties des trois générateurs (aucune erreur) :

```
OK liclea-mat-part-A.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK liclea-mat-part-B.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK liclea-mat-part-C.json : 20 fiches, 240 points, 180 questions, 60 SVG
```

## 2. Répartition des lots

### Lot A — langues (20 fiches)

| Matière | Fiches | Préfixes | L1 | L2 | L3 |
|---|---:|---|---:|---:|---:|
| Anglais | 10 | AN1.–AN10. | 5 | 7 | 2 |
| Français | 10 | PF1.–PF10. | 5 | 6 | 3 |
| **Total lot A** | **20** | — | **10** | **13** | **5** |

### Lot B — droit, économie, méthodologie (20 fiches)

| Matière | Fiches | Préfixes | L1 | L2 | L3 |
|---|---:|---|---:|---:|---:|
| Droit | 8 | DR1.–DR8. | 2 | 6 | 3 |
| Économie | 7 | EC1.–EC7. | 2 | 5 | 3 |
| Méthodologie universitaire | 5 | MU1.–MU5. | 3 | 3 | 1 |
| **Total lot B** | **20** | — | **7** | **14** | **7** |

### Lot C — outils et transversales (20 fiches)

| Matière | Fiches | Préfixes | L1 | L2 | L3 |
|---|---:|---|---:|---:|---:|
| Informatique | 5 | IN1.–IN5. | 3 | 2 | 1 |
| Statistiques | 5 | ST1.–ST5. | 2 | 3 | 2 |
| Psychologie | 5 | LPSY1.–LPSY5. | 2 | 3 | 2 |
| Maths / stats | 5 | MS1.–MS5. | 2 | 3 | 2 |
| **Total lot C** | **20** | — | **9** | **11** | **7** |

**Total filière :** L1 26 · L2 38 · L3 19 déclarations (83 au total, 23 fiches
étant partagées entre deux années). Les 9 matières du questionnaire licence sont
toutes couvertes, avec les dénominations exactes, dont `Maths / stats`.

Sources mobilisées dans les 60 fiches : arrêté du 6 avril 2021 (JORF n° 0083),
BO spécial n° 7 du 17 février 2022, éduscol, RNCP 39173, CECRL, Code civil,
Code de commerce, Code du travail, Code de la consommation, TUE/TFUE, INSEE,
OCDE, BCE, CNIL/RGPD, ANSSI, ISO 690.

## 3. Blocs et schémas

- **Blocs :** 60/60 fiches ont exactement la séquence attendue ; aucun bloc
  manquant, ajouté ou permuté.
- **SVG :** 180 schémas au total (3 par fiche). Chaque SVG est un XML bien formé
  (`ElementTree.fromstring`), ne contient ni `<script`, ni gestionnaire
  d'événement inline, ni `javascript:`, ni `foreignObject`, et toutes les
  coordonnées de texte sont dans le `viewBox`.
- Les schémas utilisent les familles de `fixtures.py` : tableaux (`svg_grille`),
  procédures (`svg_etapes`) et comparaisons (`svg_compare`), avec des titres
  adaptés à chaque chapitre (ex. « Choisir son temps », « Les actes de l'Union »,
  « Lire une série », « Évaluer une source »).

## 4. Contrôle des doublons de titres

- **Doublons internes `lic-lea` : 0.** Les 60 titres sont uniques.
- **Doublons inter-lots : 0.** Les préfixes `AN*`, `PF*`, `DR*`, `EC*`, `MU*`,
  `IN*`, `ST*`, `LPSY*` et `MS*` sont répartis sans recouvrement entre A, B et C.
- **Collisions avec le catalogue existant : 0.** Les 60 titres ont été comparés
  aux 2 415 titres déjà présents dans les fichiers JSON de `data/` et dans
  `index.html` (`EXTRA_FICHES`). Le suffixe `(LEA)` garantit l'unicité globale.
- Les 60 préfixes attendus sont tous présents, un et un seul.

## 5. Artefacts CJK

- Recherche du motif `[\u4e00-\u9fff\u3040-\u30ff]` sur la sérialisation JSON
  complète de chaque fiche : **0 occurrence** sur les 60 fiches (A : 0, B : 0,
  C : 0). Aucun caractère chinois ou japonais parasite.

## 6. Verdict

| Critère | Résultat |
|---|---|
| Génération des 3 lots (`gen_liclea_A/B/C.py` + JSON) | ✅ OK |
| Validation `fixtures.valider_fiche()` sur 60 fiches | ✅ 0 erreur |
| 12 points / 9 questions (7 QCM + 2 rédaction) / 7 blocs / 3 SVG | ✅ partout |
| `filieres = ["lic-lea"]` et années `L1`/`L2`/`L3` | ✅ 60/60 |
| 9 matières exactes du questionnaire licence | ✅ 9/9 |
| Titres uniques et préfixés | ✅ 60/60 (0 collision catalogue) |
| Absence de CJK | ✅ 60/60 fiches |
| Sources officielles présentes | ✅ 60/60 |

**Verdict final : FILIÈRE `lic-lea` CONFORME ET LIVRABLE.** Les 60 fiches peuvent
être transmises au coordinateur pour injection globale dans `index.html`.
