# Audit FicheLab — filière `bts-gpme` (BTS Gestion de la PME)

> Audit de la déclinaison prototype, réalisé après génération des trois lots. Vérification automatique avec `data/fixtures.py` (`valider_fiche`, `BLOCS_ATTENDUS`, `CJK`, `INTERDIT_SVG`), analyse XML des schémas et contrôle des doublons sur le catalogue complet.
> Date : 24 novembre 2026. Cartographie : [`BTSGPME-PROGRAMME.md`](BTSGPME-PROGRAMME.md).

## 1. Résultat global

**AUCUNE ERREUR DÉTECTÉE — AUDIT CONFORME.**

| Contrôle | Valeur | Attendu | Résultat |
|---|---|---|---|
| Générateurs exécutés | 3 / 3 | `OK` sans erreur | ✅ |
| Fiches prototype | 60 | 20 + 20 + 20 | ✅ |
| Points de cours | 720 | 12 par fiche | ✅ |
| Questions corrigées | 600 | 10 par fiche | ✅ |
| — QCM | 480 | ≥ 6 par fiche (8 ici) | ✅ |
| — questions rédaction | 120 | ≥ 2 par fiche (2 ici) | ✅ |
| Schémas SVG | 180 | 3 par fiche, XML valide | ✅ |
| Blocs d'affichage | 60 fiches | ordre strict `intro, formule, grille, liste, etapes, attention, exemples` | ✅ |
| `filieres` | 60 / 60 | `["bts-gpme"]` | ✅ |
| `annees` | 60 / 60 | sous-ensemble de `BTS1`, `BTS2` | ✅ |
| Sources officielles | 60 / 60 | arrêté 26 janvier 2017 + BO + CEJM + RNCP38363 | ✅ |
| Artefacts CJK | 0 | aucun | ✅ |
| Scripts / événements SVG | 0 | aucun `<script>`, `on*`, `javascript:`, `foreignObject` | ✅ |
| Titres uniques | 60 / 60 | aucun doublon interne | ✅ |
| Doublons avec le catalogue existant | 0 | 995 fiches + `index.html` vérifiés | ✅ |
| Fichiers protégés | inchangés | `index.html`, `inject_app.py`, `audit_filieres.py` non modifiés | ✅ |

## 2. Détail par lot

| Lot | Générateur | JSON | Fiches | Points | QCM | Rédaction | SVG | Validation |
|---|---|---|---|---|---|---|---|---|
| A | `data/gen_btsgpme_A.py` | `data/btsgpme-mat-part-A.json` | 20 | 240 | 160 | 40 | 60 | `OK` |
| B | `data/gen_btsgpme_B.py` | `data/btsgpme-mat-part-B.json` | 20 | 240 | 160 | 40 | 60 | `OK` |
| C | `data/gen_btsgpme_C.py` | `data/btsgpme-mat-part-C.json` | 20 | 240 | 160 | 40 | 60 | `OK` |
| **Total** | — | — | **60** | **720** | **480** | **120** | **180** | **OK** |

## 3. Couverture par matière (matières exactes du questionnaire BTS)

| Matière | Fiches | Préfixes |
|---|---|---|
| `Comptabilité et gestion` | 12 | CG1. … CG12. |
| `Management` | 8 | MA1. … MA8. |
| `Droit` | 7 | DR1. … DR7. |
| `Économie` | 7 | EC1. … EC7. |
| `Maths / stats` | 6 | MS1. … MS6. |
| `Français` | 4 | PF1. … PF4. |
| `Anglais professionnel` | 4 | AN1. … AN4. |
| `Communication` | 4 | CO1. … CO4. |
| `Informatique` | 4 | IN1. … IN4. |
| `Marketing` | 4 | MK1. … MK4. |
| **Total** | **60** | 60 préfixes tous distincts |

**Total par lot** : A = CG (12) + MA (8) = 20 · B = DR (7) + EC (7) + MS (6) = 20 · C = PF (4) + AN (4) + CO (4) + IN (4) + MK (4) = 20.

> La matière `Gestion` demandée pour le lot A est bien portée par l'intitulé exact du questionnaire `Comptabilité et gestion` (aucun doublon `Comptabilité` ou `Gestion` n'a été créé).

## 4. Couverture par année

| Répartition | Fiches |
|---|---|
| `BTS1` uniquement | 29 |
| `BTS2` uniquement | 29 |
| `BTS1` + `BTS2` (CG6 trésorerie/BFR, MA4 suivi du personnel) | 2 |
| **Fiches visibles en BTS1** | **31** |
| **Fiches visibles en BTS2** | **31** |

Aucune autre valeur d'année (`2nde`, `BUT1`, `L1`, …) n'est utilisée.

## 5. Conformité au prototype

- **12 points** par fiche : définitions, règles, formules, chiffres et exemples contextualisés en PME.
- **10 questions** par fiche : 8 QCM (indices de réponse valides) + 2 questions de rédaction avec `reponse` et `correction` renseignées ; exercices chiffrés dans CG, DR (calculs de criticité), EC, MS, IN et MK.
- **7 blocs** en ordre strict et typés explicitement via `fixtures.bloc(type=...)` : `intro` → `formule` → `grille` → `liste` → `etapes` → `attention` → `exemples`.
- **3 diagrammes** par fiche via `diag()` : `svg_grille` (repères), `svg_etapes` (méthode), puis `svg_compare` ou `svg_flux` selon le chapitre. Tous analysables en XML et sans contenu exécutable.
- **Sources** : chaque fiche cite l'arrêté du 26 janvier 2017, sa modification de 2018, le programme CEJM du 15 février 2018 et le RNCP38363 ; les matières jurídiques ajoutent les codes applicables.
- **Méthode des 4 étapes** et suivi des lots consignés dans [`BTSGPME-PROGRAMME.md`](BTSGPME-PROGRAMME.md) §4 et §5.

## 6. Contrôles de doublons

- 60 titres uniques à l'intérieur de la filière (préfixes `CGn.`, `MAn.`, `DRn.`, `ECn.`, `MSn.`, `PFn.`, `ANn.`, `COn.`, `INn.`, `MKn.`).
- Comparaison avec les **995 fiches** des 76 fichiers `*-part-*.json` préexistants : **0 collision**.
- Comparaison avec les fiches embarquées dans `index.html` : **0 collision**.
- Vérification CJK sur la sérialisation JSON complète : **0 artefact** (y compris les corrections apportées pendant la rédaction).

## 7. Conclusion

La filière `bts-gpme` est complète et prête pour injection : **60 fiches au format prototype, conformes au modèle `FICHE_UV`, validées sans erreur, sans doublon et sans artefact**. La couverture BTS1/BTS2 est équilibrée (31 fiches visibles par année) et les 10 matières du questionnaire BTS sont toutes représentées.
