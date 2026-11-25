# Audit — filière `lic-psycho` (lots A, B, C)

> Date : 24 novembre 2026 · Racine : `fichelabs/fichelab` · Fichiers audités :
> `data/licpsycho-mat-part-A.json`, `data/licpsycho-mat-part-B.json`,
> `data/licpsycho-mat-part-C.json`.
> Contrôle exécuté avec `data/fixtures.py :: valider_fiche()` sur **60 fiches**,
> plus un contrôle croisé des titres, des blocs, des SVG, des matières et des artefacts CJK.

## 1. Compteurs et conformité structurelle

| Lot | Générateur | Fiches | Points | Questions | QCM | Rédaction | SVG | Erreurs `valider_fiche()` |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| A | `gen_licpsycho_A.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| B | `gen_licpsycho_B.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| C | `gen_licpsycho_C.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| **Total** | — | **60** | **720** | **540** | **420** | **120** | **180** | **0** |

Chaque fiche respecte le prototype : **12 points**, **9 questions** (7 QCM + 2
rédaction, toutes corrigées), **7 blocs** dans l'ordre strict
`intro → formule → grille → liste → etapes → attention → exemples`, **3 schémas**.
Toutes les fiches déclarent `filieres = ["lic-psycho"]` et des années dans
`L1`, `L2`, `L3`.

Sorties des générateurs ( Validation OK sans erreur) :

```
OK licpsycho-mat-part-A.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK licpsycho-mat-part-B.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK licpsycho-mat-part-C.json : 20 fiches, 240 points, 180 questions, 60 SVG
```

## 2. Répartition des lots

| Lot | Matières (effectifs) | L1 | L2 | L3 |
|---|---|---:|---:|---:|
| A | Psychologie 10 (`PSY1.`–`PSY10.`) · Statistiques 10 (`ST1.`–`ST10.`) | 6 | 8 | 6 |
| B | Droit 7 (`DR1.`–`DR7.`) · Économie 7 (`EC1.`–`EC7.`) · Méthodologie universitaire 6 (`MU1.`–`MU6.`) | 7 | 7 | 6 |
| C | Français 5 (`PF1.`–`PF5.`) · Anglais 5 (`AN1.`–`AN5.`) · Informatique 5 (`IN1.`–`IN5.`) · Maths / stats 5 (`MS1.`–`MS5.`) | 5 | 8 | 7 |
| **Total** | **9 matières** | **18** | **23** | **19** |

Les **9 matières** sont exactement celles demandées : `Psychologie`,
`Statistiques`, `Droit`, `Économie`, `Méthodologie universitaire`, `Français`,
`Anglais`, `Informatique`, `Maths / stats`. Aucune matière supplémentaire
ni variante orthographique n'a été introduite.

Sources mobilisées : arrêté du 6 avril 2021 (JORF n° 0083 du 8 avril 2021) ·
BO spécial n° 7 du 17 février 2022 · éduscol / MESR · fiches RNCP de mention
Psychologie · Code civil, Code pénal, Code du travail, Code de la santé
publique, CNIL/RGPD · INSEE, Dares · norme ISO 690 · programmes diffusés par
les universités. Ces sources figurent dans le champ `source` de chaque fiche.

Les générateurs sont calqués sur `data/gen_generale_modele.py` et utilisent
exclusivement `fixtures.py` (`fiche`, `qcm`, `qt`, `diag`, `bloc`, `svg_grille`,
`svg_flux`, `svg_etapes`, `svg_compare`, `valider_et_ecrire`). Aucun fichier
`index.html`, `inject_app.py` ou `audit_filieres.py` n'a été modifié.

## 3. Blocs et schémas

- **Blocs :** 60/60 fiches ont exactement la séquence attendue ; aucun bloc
  manquant, ajouté ou permuté.
- **SVG :** 180 schémas au total (3 par fiche). Chaque SVG est un XML bien formé
  (`ElementTree.fromstring`), ne contient ni `<script`, ni gestionnaire
  d'événement inline, ni `javascript:`, ni `foreignObject`, et toutes les
  coordonnées de texte sont dans le `viewBox`.
- Les quatre familles de schémas de `fixtures.py` sont utilisées : tableaux
  (`svg_grille`), enchaînements (`svg_flux`), procédures (`svg_etapes`) et
  comparaisons (`svg_compare`), répartis sur les 60 chapitres.
- Les 3 schémas de chaque fiche portent des titres distincts et adaptés au
  chapitre (ex. « Les trois systèmes mnésiques », « Mesurer l'inflation »,
  « Structure d'un compte rendu », « Résoudre une équation »).

## 4. Contrôle des doublons de titres

- **60 préfixes uniques** : `PSY1.`–`PSY10.`, `ST1.`–`ST10.`, `DR1.`–`DR7.`,
  `EC1.`–`EC7.`, `MU1.`–`MU6.`, `PF1.`–`PF5.`, `AN1.`–`AN5.`,
  `IN1.`–`IN5.`, `MS1.`–`MS5.` — aucun préfixe dupliqué.
- **0 doublon de titre interne** aux trois lots (60 titres uniques).
- **0 collision avec les autres JSON du catalogue** (lots des filières
  `lic-droit`, `pass`, `infirmier`, `bts-*`, `but-*`, `generale`, etc.).
  Trois titres initiaux entraient en collision avec `licdroit-mat-part-C.json`
  (`PSY1.`, `PF2.`, `IN1.`) : ils ont été renommés en ajoutant un complément
  (« objet et méthodes », « en psychologie », « d'information »), puis les lots
  A et C ont été régénérés.
- **0 collision avec `index.html`** (4 696 titres extraits du catalogue
  existant, y compris les anciennes fiches `lic-psycho` non prototype).

## 5. Artefacts CJK

- Recherche du motif `[\u4e00-\u9fff\u3040-\u30ff]` sur la sérialisation JSON
  complète de chaque fiche : **0 occurrence** sur les 60 fiches (A : 0, B : 0,
  C : 0). Quelques caractères parasites insérés par erreur dans les brouillons
  ont été repérés par `valider_fiche()` puis remplacés avant la validation finale.

## 6. Verdict

| Critère | Résultat |
|---|---|
| Génération des 3 lots (`.py` + `.json`) | ✅ OK |
| Validation `fixtures.valider_fiche()` sur 60 fiches | ✅ 0 erreur |
| `filieres = ["lic-psycho"]`, années L1/L2/L3, 9 matières exactes | ✅ partout |
| 12 points / 9 questions (7 QCM + 2 rédaction) / 7 blocs / 3 SVG | ✅ partout |
| Titres uniques (interne, inter-lots, catalogue, `index.html`) | ✅ 60/60 |
| Absence de CJK | ✅ 60/60 fiches |
| Fichiers protégés inchangés | ✅ `index.html`, `inject_app.py`, `audit_filieres.py` non modifiés |

**Verdict final : FILIÈRE `lic-psycho` CONFORME ET LIVRABLE.** Les 60 fiches
peuvent être transmises au coordinateur pour injection globale.
