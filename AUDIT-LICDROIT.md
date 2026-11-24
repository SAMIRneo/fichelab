# Audit — filière `lic-droit` (lots A, B, C)

> Date : 24 novembre 2026 · Racine : `fichelabs/fichelab` · Fichiers audités :
> `data/licdroit-mat-part-A.json`, `data/licdroit-mat-part-B.json`,
> `data/licdroit-mat-part-C.json`.
> Contrôle exécuté avec `data/fixtures.py :: valider_fiche()` sur **60 fiches**,
> plus un contrôle croisé des titres, des blocs, des SVG et des artefacts CJK.

## 1. Compteurs et conformité structurelle

| Lot | Générateur | Fiches | Points | Questions | QCM | Rédaction | SVG | Erreurs `valider_fiche()` |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| A | `gen_licdroit_A.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| B | `gen_licdroit_B.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| C | `gen_licdroit_C.py` | 20 | 240 | 180 | 140 | 40 | 60 | **0** |
| **Total** | — | **60** | **720** | **540** | **420** | **120** | **180** | **0** |

Chaque fiche respecte le prototype : **12 points**, **9 questions** (7 QCM + 2
rédaction, toutes corrigées), **7 blocs** dans l'ordre strict
`intro → formule → grille → liste → etapes → attention → exemples`, **3 schémas**.
Toutes les fiches déclarent `filieres = ["lic-droit"]`.

Validation du lot C : `OK licdroit-mat-part-C.json : 20 fiches, 240 points,
180 questions, 60 SVG` (sortie de `valider_et_ecrire()`, sans erreur).

## 2. Répartition des lots

### Lot A (déjà livré, non modifié)

- **Droit : 20** — `DR1.` à `DR10.` (droit privé, pénal, administratif, commerce)
  et `DRB1.` à `DRB10.` (droit public, Union européenne, travail, procédure).
- Années : L1 6 · L2 9 · L3 5.

### Lot B (déjà livré, non modifié)

- **Droit : 10** — `DRB1.` à `DRB10.` ; **Méthodologie universitaire : 10** —
  `MU1.` à `MU10.`.
- Années : L1 5 · L2 10 · L3 5.

### Lot C (nouveau)

| Matière | Fiches | Préfixes | L1 | L2 | L3 |
|---|---:|---|---:|---:|---:|
| Statistiques | 6 | `ST1.`–`ST6.` | 2 | 2 | 2 |
| Psychologie | 4 | `PSY1.`–`PSY4.` | 2 | 1 | 1 |
| Anglais | 4 | `AN1.`–`AN4.` | 2 | 1 | 1 |
| Informatique | 3 | `IN1.`–`IN3.` | 1 | 1 | 1 |
| Français | 3 | `PF1.`–`PF3.` | 2 | 1 | 0 |
| **Total lot C** | **20** | — | **9** | **6** | **5** |

Sources du lot C (5 variantes officielles) : arrêté du 6 avril 2021 relatif à la
licence d'études juridiques (JORF n° 0083 du 8 avril 2021) · BO spécial n° 7 du
17 février 2022 · éduscol · INSEE (méthodes statistiques) · Cadre européen commun
de référence pour les langues (Conseil de l'Europe) · CNIL/RGPD.

Tous les chapitres du lot C correspondent à la carte de `LICDROIT-PROGRAMME.md`
§2 (transversales). Le générateur est calqué sur `gen_generale_modele.py` et
utilise exclusivement `fixtures.py` (`fiche`, `qcm`, `qt`, `diag`, `bloc`,
`svg_grille`, `svg_flux`, `svg_etapes`, `svg_compare`, `valider_et_ecrire`).

## 3. Blocs et schémas

- **Blocs :** 60/60 fiches ont exactement la séquence attendue ; aucun bloc
  manquant, ajouté ou permuté.
- **SVG :** 180 schémas au total (3 par fiche). Chaque SVG est un XML bien formé
  (`ElementTree.fromstring`), ne contient ni `<script`, ni gestionnaire
  d'événement inline, ni `javascript:`, ni `foreignObject`, et toutes les
  coordonnées de texte sont dans le `viewBox`.
- Le lot C utilise les quatre familles de schémas de `fixtures.py` : tableaux
  (`svg_grille`), procédures (`svg_etapes`), enchaînements (`svg_flux`) et
  comparaisons (`svg_compare`), répartis sur les 20 chapitres.
- Les 3 schémas de chaque fiche portent des titres distincts et adaptés au
  chapitre (ex. « Lire un tableau de fréquences », « Construire un intervalle
  de confiance », « La structure IRAC », « Les appels rhétoriques »).

## 4. Contrôle des doublons de titres (inter-lots)

- **Lot C : 0 doublon**, ni interne ni avec les lots A et B. Les préfixes
  `ST.`, `PSY.`, `AN.`, `IN.`, `PF.` sont propres au lot C.
- **A / B : 10 doublons de titres** — les fiches `DRB1.` à `DRB10.` figurent
  dans les deux lots (contenus différents, mais intitulés identiques).
Total : **50 titres uniques pour 60 fiches** ; sans ces doublons A/B, la filière
  en compterait 60.
- Conformément à la consigne, les lots A et B n'ont **pas** été modifiés. Ce
  point doit être arbitré par le coordinateur avant l'injection globale :
  soit dédupliquer les `DRB*` d'un des deux lots, soit les renommer pour refléter
  un contenu distinct. Le lot C n'est pas concerné.

## 5. Artefacts CJK

- Recherche du motif `[\u4e00-\u9fff\u3040-\u30ff]` sur la sérialisation JSON
  complète de chaque fiche : **0 occurrence** sur les 60 fiches (A : 0, B : 0,
  C : 0). Aucun caractère chinois ou japonais parasite.

## 6. Verdict

| Critère | Résultat |
|---|---|
| Génération du lot C (`gen_licdroit_C.py` + JSON) | ✅ OK |
| Validation `fixtures.valider_fiche()` sur 60 fiches | ✅ 0 erreur |
| 12 points / 9 questions (≥6 QCM, ≥2 rédaction) / 7 blocs / 3 SVG | ✅ partout |
| Titres uniques dans le lot C | ✅ 20/20 |
| Absence de CJK | ✅ 60/60 fiches |
| Doublons inter-lots | ⚠️ 10 doublons de titres `DRB1.`–`DRB10.` entre A et B (lots non modifiés, arbitrage coordinateur requis) |

**Verdict final : LOT C CONFORME ET LIVRABLE.** L'ensemble A+B+C est structurellement
valide ; le seul réservoir d'attention est la duplication des intitulés `DRB*`
entre les lots A et B, existante avant cette reprise et hors périmètre de
modification.
