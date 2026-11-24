# Audit — filière `lic-histoire` (lots A, B, C)

> Date : 24 novembre 2026 · Racine : `fichelabs/fichelab` · Fichiers audités :
> `data/lichistoire-mat-part-A.json`, `data/lichistoire-mat-part-B.json`,
> `data/lichistoire-mat-part-C.json`.
> Contrôle exécuté avec `data/fixtures.py :: valider_fiche()` sur **60 fiches**,
> complété par un contrôle croisé des filières, années, matières, titres, blocs,
> SVG et artefacts de caractères.

## 1. Compteurs et conformité structurelle

| Lot | Générateur | Fiches | Points | Questions | QCM | Rédaction | SVG | Erreurs `valider_fiche()` |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| A | `gen_lichistoire_A.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| B | `gen_lichistoire_B.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| C | `gen_lichistoire_C.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| **Total** | — | **60** | **720** | **540** | **420** | **120** | **180** | **0** |

Chaque fiche respecte strictement le prototype : **12 points**, **9 questions**
(7 QCM + 2 questions de rédaction, toutes corrigées), **7 blocs** dans l'ordre
strict `intro → formule → grille → liste → etapes → attention → exemples`,
**3 schémas SVG**. Toutes déclarent `filieres = ["lic-histoire"]` et une année
parmi `L1`, `L2`, `L3`.

Sorties des générateurs (validation `OK`, sans erreur) :

```text
OK lichistoire-mat-part-A.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK lichistoire-mat-part-B.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK lichistoire-mat-part-C.json : 20 fiches, 240 points, 180 questions, 60 SVG
```

## 2. Répartition des lots

### Lot A — Méthodologie universitaire et Français

| Matière | Fiches | Préfixes | L1 | L2 | L3 |
|---|---:|---|---:|---:|---:|
| Méthodologie universitaire | 12 | `MU1.`–`MU12.` | 4 | 4 | 4 |
| Français | 8 | `LHFR1.`–`LHFR8.` | 3 | 3 | 2 |
| **Total lot A** | **20** | — | **7** | **7** | **6** |

Contenu : démarche historique, critique des sources, historiographie,
commentaire de documents, dissertation, recherche, archives, chronologie,
cartes, oral, mémoire, analyse d'image ; expression écrite, synthèse,
argumentation, rédaction, style, lecture, oral.

### Lot B — Droit, Économie, Informatique

| Matière | Fiches | Préfixes | L1 | L2 | L3 |
|---|---:|---|---:|---:|---:|
| Droit | 7 | `DR1.`–`DR7.` | 3 | 2 | 2 |
| Économie | 7 | `EC1.`–`EC7.` | 3 | 2 | 2 |
| Informatique | 6 | `IN1.`–`IN6.` | 2 | 2 | 2 |
| **Total lot B** | **20** | — | **8** | **6** | **6** |

Contenu : institutions, citoyenneté, propriété, justice, travail, droit
européen, patrimoine ; offre/demande, PIB, monnaie, chômage, mondialisation,
révolution industrielle, fiscalité ; outils numériques, bases de données, SIG,
archives numériques, visualisation, veille.

### Lot C — Anglais, Statistiques, Psychologie, Maths / stats

| Matière | Fiches | Préfixes | L1 | L2 | L3 |
|---|---:|---|---:|---:|---:|
| Anglais | 5 | `AN1.`–`AN5.` | 2 | 1 | 2 |
| Statistiques | 5 | `ST1.`–`ST5.` | 2 | 2 | 1 |
| Psychologie | 5 | `PSY1.`–`PSY5.` | 2 | 1 | 2 |
| Maths / stats | 5 | `MS1.`–`MS5.` | 2 | 1 | 2 |
| **Total lot C** | **20** | — | **8** | **5** | **7** |

**Répartition générale :** L1 23 · L2 18 · L3 19 = 60 fiches.
**Matières :** 9 matières exactes du questionnaire licence, sans aucune autre.

## 3. Blocs, schémas et sources

- **Blocs :** 60/60 fiches ont exactement la séquence attendue ; aucun bloc
  manquant, ajouté ou permuté. Le bloc « À retenir » est construit à partir
  des points 1, 4, 7 et 10 de chaque chapitre.
- **SVG :** 180 schémas (3 par fiche), tous XML bien formés
  (`ElementTree.fromstring`), sans `<script`, sans gestionnaire d'événement
  inline, sans `javascript:` ni `foreignObject`, avec des coordonnées de texte
  dans le `viewBox`. Quatre familles sont utilisées : `svg_grille`,
  `svg_flux`, `svg_etapes`, `svg_compare`.
- **Sources :** les 60 fiches citent l'arrêté du 6 avril 2021, le BO spécial
  n° 7 du 17 février 2022 et éduscol ; des références complémentaires sont
  ajoutées par matière (Code civil et traités européens, INSEE, CECRL, CNIL/RGPD).
- Les préfixes des titres sont uniques par matière et disjoints entre lots.

## 4. Contrôle des doublons de titres

- **60 titres uniques pour 60 fiches — 0 doublon**, ni interne ni inter-lots.
- Les familles de préfixes (`MU*`, `LHFR*`, `DR*`, `EC*`, `IN*`, `AN*`, `ST*`,
  `PSY*`, `MS*`) sont propres à un lot et à une matière : aucune collision
  possible avec les lots A/B/C ni avec les autres filières du catalogue.

## 5. Artefacts de caractères

- Recherche du motif CJK `[\u4e00-\u9fff\u3040-\u30ff]` sur la sérialisation
  JSON complète : **0 occurrence** sur les 60 fiches (A : 0, B : 0, C : 0).
- Contrôle complémentaire sur d'autres/scripts non latins (grec, cyrillique,
  hébreu, arabe, thaï) : **0 occurrence**. Les notations mathématiques ont été
  écrites en caractères latins (`Cov/Var`, `Somme des carrés`, `e` pour l'erreur).

## 6. Contenu historique vérifié

Les grands repères demandés sont effectivement répartis dans les fiches des
matières de soutien (détail complet dans `LICHISTOIRE-PROGRAMME.md` §5) :
Antiquité (MU1, MU3, DR1, AN5), Moyen Âge (MU2, MU7, DR3, EC3), époque moderne
(MU3, LHFR4, EC6, AN5), époque contemporaine (MU5, MU10, DR4, PSY5), France
(MU8, DR1, LHFR2), Europe (MU9, DR6, EC5, IN4), monde (MU6, IN6, PSY3),
guerre froide (MU5, MU11, DR6, PSY5, ST4), colonisation (MU4, MU9, DR7, EC6,
IN3, AN4), révolutions (MU5, LHFR4, DR2, PSY3, MS4).

## 7. Verdict

| Critère | Résultat |
|---|---|
| Génération des trois lots (scripts + JSON) | ✅ OK, 3/3 |
| Validation `fixtures.valider_fiche()` sur 60 fiches | ✅ 0 erreur |
| 12 points / 9 questions (7 QCM + 2 rédaction) / 7 blocs / 3 SVG | ✅ partout |
| Matières exactes du questionnaire (`lic-histoire`) | ✅ 9/9 |
| Années L1 / L2 / L3 | ✅ 23 / 18 / 19 |
| Titres uniques | ✅ 60/60 |
| Absence de CJK et d'autres scripts non latins | ✅ 60/60 |
| Fichiers protégés (`index.html`, `inject_app.py`, `audit_filieres.py`) | ✅ non modifiés |

**Verdict final : FILIÈRE `lic-histoire` CONFORME ET LIVRABLE.** Les trois lots
(60 fiches) peuvent être transmis au coordinateur pour injection globale.
