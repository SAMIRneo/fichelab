# Audit — filière `lic-eco` (lots A, B, C)

> Date : 24 novembre 2026 · Racine : `fichelabs/fichelab` · Fichiers audités :
> `data/liceco-mat-part-A.json`, `data/liceco-mat-part-B.json`,
> `data/liceco-mat-part-C.json`.
> Contrôle exécuté avec `data/fixtures.py :: valider_fiche()` sur **60 fiches**,
> complété par un contrôle croisé des filières, années, matières, préfixes, blocs,
> SVG, doublons, CJK et sources officielles.

## 1. Compteurs et conformité structurelle

| Lot | Générateur | Fiches | Points | Questions | QCM | Rédaction | SVG | Erreurs `valider_fiche()` |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| A | `gen_liceco_A.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| B | `gen_liceco_B.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| C | `gen_liceco_C.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| **Total** | — | **60** | **720** | **540** | **420** | **120** | **180** | **0** |

Sorties des trois générateurs (aucune erreur) :

```
OK liceco-mat-part-A.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK liceco-mat-part-B.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK liceco-mat-part-C.json : 20 fiches, 240 points, 180 questions, 60 SVG
```

Chaque fiche respecte le prototype : **12 points**, **9 questions**
(7 QCM + 2 rédaction, toutes corrigées), **7 blocs** dans l'ordre strict
`intro → formule → grille → liste → etapes → attention → exemples`, **3 schémas**.
Toutes les fiches déclarent `filieres = ["lic-eco"]`, des années dans `L1/L2/L3`,
et une source contenant l'arrêté du 6 avril 2021.

## 2. Répartition des lots et des matières

| Lot | Matières (effectifs) | L1 | L2 | L3 |
|---|---|---:|---:|---:|
| A | Économie 10 (`EC1.`–`EC10.`) · Statistiques 10 (`ST1.`–`ST10.`) | 8 | 8 | 4 |
| B | Droit 7 (`DR1.`–`DR7.`) · Informatique 7 (`IN1.`–`IN7.`) · Méthodologie universitaire 6 (`MU1.`–`MU6.`) | 6 | 8 | 6 |
| C | Français 5 (`PF1.`–`PF5.`) · Anglais 5 (`AN1.`–`AN5.`) · Psychologie 5 (`PSY1.`–`PSY5.`) · Maths / stats 5 (`MS1.`–`MS5.`) | 8 | 8 | 4 |
| **Total** | **9 matières, 60 fiches** | **22** | **24** | **14** |

Les matières sont **exactement** celles du questionnaire pour la filière :
`Économie`, `Statistiques`, `Droit`, `Informatique`, `Méthodologie universitaire`,
`Français`, `Anglais`, `Psychologie`, `Maths / stats` (aucune variante orthographique).

Chaque chapitre porte un préfixe unique, numéroté de façon contiguë :
`EC1.`–`EC10.`, `ST1.`–`ST10.`, `DR1.`–`DR7.`, `IN1.`–`IN7.`, `MU1.`–`MU6.`,
`PF1.`–`PF5.`, `AN1.`–`AN5.`, `PSY1.`–`PSY5.`, `MS1.`–`MS5.`.

## 3. Blocs et schémas

- **Blocs :** 60/60 fiches ont la séquence attendue, sans bloc manquant, ajouté ou permuté.
- **SVG :** 180 schémas, tous XML bien formés (`ElementTree.fromstring`), sans
  `<script`, gestionnaire d'événement inline, `javascript:` ni `foreignObject`.
  Toutes les coordonnées de texte sont dans le `viewBox`.
- Les quatre familles de `fixtures.py` sont utilisées : `svg_grille`, `svg_flux`,
  `svg_etapes`, `svg_compare`, réparties sur les trois schémas de chaque fiche.
- Les préfixes des thèmes économiques couvrent bien le questionnaire : microéconomie
  (offre/demande, élasticité, concurrence, défaillances), macroéconomie (PIB,
  croissance, chômage, inflation, politiques budgétaire et monétaire), commerce
  international, finances publiques et économie du travail ; statistiques
  (descriptives, probabilités, tests, régression, séries temporelles, indices,
  échantillonnage, incertitudes, lecture de tableaux, logiciels) ; droit des
  affaires, droit social, concurrence, contrats ; outils bureautiques, bases de
  données, tableaux de bord, RGPD ; recherche documentaire, note de synthèse,
  mémoire et oral.

## 4. Contrôle des doublons

- **0 doublon de titre** sur les 60 fiches (contrôle inter-lots inclus).
- **0 collision de préfixe** : chaque identifiant `EC…`, `ST…`, `DR…`, `IN…`,
  `MU…`, `PF…`, `AN…`, `PSY…`, `MS…` n'apparaît qu'une fois.
- Aucun chevauchement entre les lots : A porte `EC`/`ST`, B porte `DR`/`IN`/`MU`,
  C porte `PF`/`AN`/`PSY`/`MS`.

## 5. Artefacts CJK et sources

- Motif `[\u4e00-\u9fff\u3040-\u30ff]` appliqué à la sérialisation JSON complète
  de chaque fiche : **0 occurrence** (A : 0, B : 0, C : 0). Aucun caractère chinois
  ou japonais parasite.
- Sources officielles mobilisées dans les 60 fiches : arrêté du 6 avril 2021
  (JORF n° 0083), arrêté du 22 janvier 2014 (nomenclature des mentions), BO spécial
  n° 7 du 17 février 2022, éduscol, référentiels DGESIP/RNCP (24424, 24425, 24426),
  INSEE, Banque de France, Code civil/commerce/travail, RGPD/CNIL, CECRL et chiffres
  Parcoursup 2026 de `SOURCES.md`.

## 6. Périmètre des modifications

Fichiers créés : `LICECO-PROGRAMME.md`, `AUDIT-LICECO.md`,
`data/gen_liceco_A.py`, `data/gen_liceco_B.py`, `data/gen_liceco_C.py`,
`data/liceco-mat-part-A.json`, `data/liceco-mat-part-B.json`,
`data/liceco-mat-part-C.json`.

**Non modifiés :** `index.html`, `inject_app.py`, `audit_filieres.py`, ainsi que
tous les générateurs et JSON des autres filières.

## 7. Verdict

| Critère | Résultat |
|---|---|
| Génération des 3 lots (générateurs + JSON) | ✅ OK |
| Validation `fixtures.valider_fiche()` sur 60 fiches | ✅ 0 erreur |
| `filieres=["lic-eco"]`, années L1/L2/L3, matières exactes | ✅ 60/60 |
| 12 points / 9 questions (7 QCM + 2 rédaction) / 7 blocs / 3 SVG | ✅ partout |
| Titres uniques préfixés et numérotation contiguë | ✅ 60/60 |
| Absence de CJK et de SVG interdit | ✅ 60/60 |
| Sources officielles citées | ✅ 60/60 |
| Doublons inter-lots | ✅ 0 |

**Verdict final : FILIÈRE `lic-eco` CONFORME ET LIVRABLE** — 60 fiches réparties en
3 lots de 20, prêtes à être transmises au coordinateur pour injection globale.
