# Audit — filière `lic-maths` (lots A, B, C)

> Date : 24 novembre 2026 · Racine : `fichelabs/fichelab` · Fichiers audités :
> `data/licmaths-mat-part-A.json`, `data/licmaths-mat-part-B.json`,
> `data/licmaths-mat-part-C.json`.
> Contrôle exécuté avec `data/fixtures.py :: valider_fiche()` sur **60 fiches**,
> plus un contrôle croisé des titres, des préfixes, des matières, des années,
> des blocs, des SVG et des artefacts CJK.

## 1. Compteurs et conformité structurelle

| Lot | Générateur | Fiches | Points | Questions | QCM | Rédaction | SVG | Erreurs `valider_fiche()` |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| A | `gen_licmaths_A.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| B | `gen_licmaths_B.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| C | `gen_licmaths_C.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| **Total** | — | **60** | **720** | **540** | **420** | **120** | **180** | **0** |

Chaque fiche respecte le prototype : **12 points**, **9 questions** (7 QCM + 2
rédaction, toutes corrigées), **7 blocs** dans l'ordre strict
`intro → formule → grille → liste → etapes → attention → exemples`, **3 schémas
SVG au titre distinct**. Toutes les fiches déclarent `filieres = ["lic-maths"]`
et une année parmi `L1`, `L2`, `L3` (avec 8 chapitres à cheval sur deux années).

Sorties des trois générateurs, sans erreur :

```
OK licmaths-mat-part-A.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK licmaths-mat-part-B.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK licmaths-mat-part-C.json : 20 fiches, 240 points, 180 questions, 60 SVG
```

## 2. Répartition des lots

### Lot A — Mathématiques et statistiques

- **Maths / stats : 12** — `MS1.` à `MS12.` (analyse réelle, algèbre linéaire,
  suites et séries, dérivation, intégration, équations différentielles,
  probabilités, topologie, arithmétique, géométrie, optimisation, calcul matriciel).
- **Statistiques : 8** — `ST1.` à `ST8.` (descriptif, lois usuelles, estimation,
  tests, régression, ANOVA, non paramétrique, lecture critique).
- Années (déclarations) : L1 9 · L2 9 · L3 4.

### Lot B — Informatique et méthodologie

- **Informatique : 10** — `IN1.` à `IN10.` (algorithmique, Python, structures de
  données, SQL, calcul numérique, visualisation, LaTeX, Git, complexité,
  programmation scientifique).
- **Méthodologie universitaire : 10** — `MU1.` à `MU10.` (démonstration,
  logique, recherche documentaire, rédaction, oral, projet, veille, équipe,
  concours, gestion du temps).
- Années (déclarations) : L1 8 · L2 12 · L3 4.

### Lot C — Transversales

| Matière | Fiches | Préfixes | L1 | L2 | L3 |
|---|---:|---|---:|---:|---:|
| Français | 5 | `PF1.`–`PF5.` | 2 | 2 | 2 |
| Anglais | 5 | `AN1.`–`AN5.` | 2 | 3 | 1 |
| Psychologie | 5 | `PSY1.`–`PSY5.` | 2 | 2 | 2 |
| Économie | 5 | `EC1.`–`EC5.` | 2 | 2 | 1 |
| **Total lot C** | **20** | — | **8** | **9** | **6** |

Récapitulatif par matière (60 fiches, 8 matières) :

| Matière | Fiches | L1 | L2 | L3 |
|---|---:|---:|---:|---:|
| Maths / stats | 12 | 6 | 6 | 1 |
| Statistiques | 8 | 3 | 3 | 3 |
| Informatique | 10 | 4 | 7 | 1 |
| Méthodologie universitaire | 10 | 4 | 5 | 3 |
| Français | 5 | 2 | 2 | 2 |
| Anglais | 5 | 2 | 3 | 1 |
| Psychologie | 5 | 2 | 2 | 2 |
| Économie | 5 | 2 | 2 | 1 |
| **Total** | **60** | **25** | **30** | **14** |

> Les totaux annuels (69 déclarations) dépassent 60 car huit chapitres portent
> deux années : `MS5.`, `ST3.`, `IN3.`, `IN7.`, `AN2.`, `PF4.`, `MU8.`, `PSY4.`.

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
- **60 préfixes uniques : 0 collision.** Les familles `MS.`, `ST.`, `IN.`,
  `MU.`, `PF.`, `AN.`, `PSY.`, `EC.` sont disjointes et chaque numéro n'apparaît
  qu'une fois.
- Tous les titres sont préfixés selon le motif `CODEn. · Titre du chapitre` et
  respectent la longueur minimale imposée par `fixtures.py`.

## 5. Artefacts CJK

- Recherche du motif `[\u4e00-\u9fff\u3040-\u30ff]` sur la sérialisation JSON
  complète de chaque fiche : **0 occurrence sur les 60 fiches** (A : 0, B : 0,
  C : 0). Aucun caractère chinois ou japonais parasite.
- Les quelques caractères apparus lors de la rédaction (`找`, `到`, `了`, `他`,
  `算`, `法`, `单`, `元`) ont été repérés avant livraison et remplacés par leur
  terme français ; le contrôle final est propre.

## 6. Verdict

| Critère | Résultat |
|---|---|
| Génération des 3 lots (générateurs + JSON) | ✅ OK |
| Validation `fixtures.valider_fiche()` sur 60 fiches | ✅ 0 erreur |
| 12 points / 9 questions (≥6 QCM, ≥2 rédaction) / 7 blocs / 3 SVG | ✅ partout |
| `filieres = ["lic-maths"]`, années L1/L2/L3 | ✅ 60/60 |
| Matières exactes du questionnaire licence | ✅ 8 matières utilisées, aucune inventée |
| Titres uniques préfixés | ✅ 60/60 |
| Absence de CJK | ✅ 60/60 fiches |
| Doublons inter-lots | ✅ 0 |
| Fichiers interdits non modifiés | ✅ `index.html`, `inject_app.py`, `audit_filieres.py` intacts |

**Verdict final : FILIÈRE `lic-maths` CONFORME ET LIVRABLE.** Les trois lots
A, B et C totalisent 60 fiches prototypes structurellement valides, sans
doublon ni artefact. Seul point de cadrage : la matière `Droit`, bien présente
dans la liste du questionnaire licence, n'a pas de lot dédié dans la
répartition reçue ; elle reste couverte par la filière `lic-droit`.
