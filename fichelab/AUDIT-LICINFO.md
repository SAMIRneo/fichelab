# Audit — filière `lic-info` (lots A, B, C)

> Date : 24 novembre 2026 · Racine : `fichelabs/fichelab` · Fichiers audités :
> `data/licinfo-mat-part-A.json`, `data/licinfo-mat-part-B.json`,
> `data/licinfo-mat-part-C.json`.
> Contrôle exécuté avec `data/fixtures.py :: valider_fiche()` sur **60 fiches**,
> plus un contrôle croisé des titres, des préfixes, des matières, des années,
> des blocs, des SVG et des artefacts CJK (inter-lots **et** inter-filières).

## 1. Compteurs et conformité structurelle

| Lot | Générateur | Fiches | Points | Questions | QCM | Rédaction | SVG | Erreurs `valider_fiche()` |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| A | `gen_licinfo_A.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| B | `gen_licinfo_B.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| C | `gen_licinfo_C.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| **Total** | — | **60** | **720** | **540** | **420** | **120** | **180** | **0** |

Chaque fiche respecte le prototype : **12 points**, **9 questions** (7 QCM + 2
rédaction, toutes corrigées), **7 blocs** dans l'ordre strict
`intro → formule → grille → liste → etapes → attention → exemples`, **3 schémas
SVG au titre distinct**. Toutes les fiches déclarent `filieres = ["lic-info"]`
et au moins une année parmi `L1`, `L2`, `L3`.

Sorties des trois générateurs, sans erreur :

```
OK licinfo-mat-part-A.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK licinfo-mat-part-B.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK licinfo-mat-part-C.json : 20 fiches, 240 points, 180 questions, 60 SVG
```

## 2. Répartition des lots

### Lot A — Informatique et mathématiques

- **Informatique : 12** — `IN1.` à `IN12.` (algorithmique, Python, structures de
  données, complexité, bases de données, réseaux, systèmes, génie logiciel,
  programmation orientée objet, calcul parallèle, intelligence artificielle,
  sécurité et cryptographie).
- **Maths / stats : 8** — `MS1.` à `MS8.` (logique et algèbre de Boole, algèbre
  linéaire, calcul matriciel, suites et récurrences, probabilités, statistiques
  descriptives, graphes, optimisation combinatoire).
- Années (déclarations) : L1 10 · L2 12 · L3 4 — 26 déclarations.

### Lot B — Méthodologie, droit et statistiques

- **Méthodologie universitaire : 10** — `MU1.` à `MU10.` (recherche
  documentaire, logique et preuves, rapport technique, soutenance, projet agile,
  veille, travail en équipe et revue de code, gestion du temps, répétition
  espacée, préparation aux examens).
- **Droit : 6** — `DR1.` à `DR6.` (droit de l'informatique, RGPD, propriété
  intellectuelle et logiciels libres, contrats informatiques, cyberdroit,
  responsabilité civile, pénale et contractuelle).
- **Statistiques : 4** — `ST1.` à `ST4.` (descriptif, probabilités et lois
  usuelles, échantillonnage et estimation, tests d'hypothèses).
- Années (déclarations) : L1 6 · L2 12 · L3 8 — 26 déclarations.

### Lot C — Transversales

| Matière | Fiches | Préfixes | L1 | L2 | L3 |
|---|---:|---|---:|---:|---:|
| Français | 5 | `PF1.`–`PF5.` | 2 | 2 | 2 |
| Anglais | 5 | `AN1.`–`AN5.` | 2 | 3 | 2 |
| Psychologie | 5 | `PSY1.`–`PSY5.` | 2 | 3 | 1 |
| Économie | 5 | `EC1.`–`EC5.` | 2 | 3 | 2 |
| **Total lot C** | **20** | — | **8** | **11** | **7** |

Récapitulatif par matière (60 fiches, 9 matières) :

| Matière | Fiches | L1 | L2 | L3 |
|---|---:|---:|---:|---:|
| Informatique | 12 | 5 | 8 | 3 |
| Maths / stats | 8 | 5 | 4 | 1 |
| Méthodologie universitaire | 10 | 4 | 5 | 4 |
| Droit | 6 | 0 | 4 | 3 |
| Statistiques | 4 | 2 | 3 | 1 |
| Français | 5 | 2 | 2 | 2 |
| Anglais | 5 | 2 | 3 | 2 |
| Psychologie | 5 | 2 | 3 | 1 |
| Économie | 5 | 2 | 3 | 2 |
| **Total** | **60** | **24** | **35** | **19** |

> Les totaux annuels (78 déclarations) dépassent 60 car 18 chapitres portent
> deux années : `IN3.`, `IN5.`, `IN9.`, `IN12.`, `MS3.`, `MS5.`, `ST2.`, `ST4.`,
> `MU2.`, `MU6.`, `MU7.`, `DR3.`, `PF4.`, `AN2.`, `AN4.`, `PSY2.`, `EC2.`, `EC4.`.
> Les neuf matières du questionnaire licence sont toutes couvertes ; `Droit`
> commence en L2, conformément à la progression retenue.

## 3. Blocs et schémas

- **Blocs :** 60/60 fiches ont exactement la séquence attendue ; aucun bloc
  manquant, ajouté ou permuté.
- **SVG :** 180 schémas au total (3 par fiche, 3 titres distincts par fiche).
  Chaque SVG est un XML bien formé (`ElementTree.fromstring`), ne contient ni
  `<script`, ni gestionnaire d'événement inline, ni `javascript:`, ni
  `foreignObject`, et toutes les coordonnées de texte sont dans le `viewBox`.
- Les quatre familles de schémas de `fixtures.py` sont utilisées : tableaux
  (`svg_grille`), procédures (`svg_etapes`), enchaînements (`svg_flux`) et
  comparaisons (`svg_compare`), répartis sur les 60 chapitres.
- **Questions :** 420 QCM et 120 questions de rédaction, toutes avec correction.
  Aucune option de QCM n'est dupliquée à l'intérieur d'une même question.

## 4. Contrôle des doublons de titres et de préfixes

- **60 titres uniques pour 60 fiches : 0 doublon**, ni interne à un lot, ni
  entre lots.
- **Contrôle inter-filières : 0 collision.** Les 60 titres (`titre.strip().lower()`)
  ont été comparés à ceux de tous les autres fichiers JSON du catalogue :
  **0 titre en double**.
- **60 préfixes uniques : 0 collision.** Les familles `IN.`, `MS.`, `MU.`, `DR.`,
  `ST.`, `PF.`, `AN.`, `PSY.`, `EC.` sont disjointes et chaque numéro n'apparaît
  qu'une fois (`IN1.`–`IN12.`, `MS1.`–`MS8.`, `MU1.`–`MU10.`, `DR1.`–`DR6.`,
  `ST1.`–`ST4.`, `PF1.`–`PF5.`, `AN1.`–`AN5.`, `PSY1.`–`PSY5.`, `EC1.`–`EC5.`).
- Tous les titres sont préfixés selon le motif `CODEn. · Titre du chapitre` et
  respectent la longueur minimale imposée par `fixtures.py`.

## 5. Artefacts CJK

- Recherche du motif `[\u4e00-\u9fff\u3040-\u30ff]` sur la sérialisation JSON
  complète de chaque fiche : **0 occurrence sur les 60 fiches** (A : 0, B : 0,
  C : 0). Aucun caractère chinois ou japonais parasite.
- Trois caractères parasites saisis pendant la rédaction ont été repérés par le
  contrôle de validation puis remplacés par leur terme français ; le contrôle
  final est propre.

## 6. Verdict

| Critère | Résultat |
|---|---|
| Génération des 3 lots (générateurs + JSON) | ✅ OK |
| Validation `fixtures.valider_fiche()` sur 60 fiches | ✅ 0 erreur |
| 12 points / 9 questions (≥6 QCM, ≥2 rédaction) / 7 blocs / 3 SVG | ✅ partout |
| `filieres = ["lic-info"]`, années L1/L2/L3 | ✅ 60/60 |
| Matières exactes du questionnaire licence (9 matières) | ✅ 9/9 utilisées, aucune inventée |
| Titres uniques préfixés | ✅ 60/60 |
| Absence de CJK | ✅ 60/60 fiches |
| Doublons inter-lots et inter-filières | ✅ 0 |
| Fichiers interdits non modifiés | ✅ `index.html`, `inject_app.py`, `audit_filieres.py` intacts |

**Verdict final : FILIÈRE `lic-info` CONFORME ET LIVRABLE.** Les trois lots A, B
et C totalisent 60 fiches prototypes structurellement valides, couvrant les
neuf matières du questionnaire licence, sans doublon ni artefact. L'injection
des lots dans l'application relève d'une étape distincte et n'a pas été
réalisée ici.
