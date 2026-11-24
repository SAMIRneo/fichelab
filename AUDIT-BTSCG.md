# Audit de la filière `bts-cg` — BTS Comptabilité et gestion

> Audit exécuté le 24 novembre 2026. Périmètre : les trois lots prototype produits pour la filière `bts-cg` (111 112 vœux Parcoursup 2026, source [`SOURCES.md`](SOURCES.md) §1).
> Cartographie : [`BTSCG-PROGRAMME.md`](BTSCG-PROGRAMME.md) · modèle : [`FICHE-PROTOTYPE.md`](FICHE-PROTOTYPE.md) · référence voisine : [`AUDIT-FILIERES.md`](AUDIT-FILIERES.md).

## 1. Périmètre audité

| Lot | Générateur | JSON | Fiches |
|---|---|---|---|
| A | `data/gen_btscg_A.py` | `data/btscg-mat-part-A.json` | 20 |
| B | `data/gen_btscg_B.py` | `data/btscg-mat-part-B.json` | 20 |
| C | `data/gen_btscg_C.py` | `data/btscg-mat-part-C.json` | 20 |
| **Total** | **3** | **3** | **60** |

Fichiers non modifiés : `index.html`, `inject_app.py`, `audit_filieres.py`.

## 2. Validation des générateurs

Exécution de `python gen_btscg_A.py`, `python gen_btscg_B.py`, `python gen_btscg_C.py` dans `data/` (avec `PYTHONIOENCODING=utf-8`). Sorties :

```
OK btscg-mat-part-A.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK btscg-mat-part-B.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK btscg-mat-part-C.json : 20 fiches, 240 points, 180 questions, 60 SVG
```

`fixtures.valider_et_ecrire()` valide pour chaque fiche la présence des 9 champs, 10–14 points, 8–10 questions, ≥ 6 QCM et ≥ 2 questions rédaction, l'ordre strict des 7 blocs, 2–4 schémas SVG parsables, l'absence de code SVG interdit, l'absence d'artefacts CJK et l'unicité des titres dans le lot. **Aucune erreur signalée.**

## 3. Conformité stricte (contrôle supplémentaire)

Contrôle indépendant sur les 60 fiches JSON (script de vérification ad hoc) :

| Critère | Résultat |
|---|---|
| `filieres == ["bts-cg"]` sur toutes les fiches | ✅ 60/60 |
| `annees == ["BTS1"]` ou `["BTS2"]` (une seule année par fiche) | ✅ 60/60 |
| `matiere` dans les 11 matières exactes du questionnaire BTS | ✅ 60/60 |
| 12 points de cours par fiche | ✅ 60/60 |
| 9 questions par fiche, dont ≥ 6 QCM et ≥ 2 rédaction | ✅ 60/60 (540 questions) |
| 7 blocs dans l'ordre `intro, formule, grille, liste, etapes, attention, exemples` | ✅ 60/60 |
| 3 schémas par fiche construits avec `diag()` | ✅ 60/60 (180 SVG) |
| Sources officielles renseignées (arrêté 6 mai 2013 modifié, BO, éduscol, PCG, Code de commerce, CGI, Code du travail, INSEE) | ✅ 60/60 |
| Aucun caractère CJK | ✅ 60/60 |
| Titres uniques préfixés (`CP`, `MS`, `DR`, `EC`, `MA`, `PF`, `AN`, `CO`, `IN`, `ME`) | ✅ 60/60 |

**Erreurs de conformité : 0.**

## 4. Doublons de titres avec les autres filières

Une recherche a été effectuée sur l'ensemble des fichiers JSON du catalogue (`data/*.json`, soit plus de 2 000 fiches préexistantes).

- Un doublon initial a été détecté : `DR4. · Droit de la consommation : information et protection du client`, identique à une fiche du BTS MCO (`mco-mat-part-C.json`).
- Correction apportée : le titre BTS CG est devenu **`DR4. · Droit de la consommation : information, rétractation et garanties`**, puis le lot B a été régénéré.
- **Doublons résiduels impliquant `bts-cg` : 0.**

Les préfixes `DR1.`, `AN1.`, `PF1.` etc. sont réutilisés par d'autres filières, mais les titres complets sont tous distincts.

## 5. Répartition des matières

| Matière FicheLab | Fiches | Lots |
|---|---:|---|
| `Comptabilité et gestion` | 12 | A (CP1–CP12) |
| `Maths / stats` | 8 | A (MS1–MS8) |
| `Droit` | 7 | B (DR1–DR7) |
| `Économie` | 7 | B (EC1–EC7) |
| `Management` | 6 | B (MA1–MA6) |
| `Français` | 4 | C (PF1–PF4) |
| `Anglais professionnel` | 4 | C (AN1–AN4) |
| `Communication` | 4 | C (CO1–CO4) |
| `Informatique` | 4 | C (IN1–IN4) |
| `Méthodologie` | 4 | C (ME1–ME4) |
| `Marketing` | 0 | Fait partie du vocabulaire exact du questionnaire et du programme E3, mais le plan de production 20 + 20 + 20 ne lui attribue pas de chapitre dédié (notions traitées dans `MA`, `EC` et `CP`). |
| **Total** | **60** | |

Répartition par année : **BTS1 = 29 fiches**, **BTS2 = 31 fiches**.

## 6. Totaux de la filière

- **60 fiches** au format prototype
- **720 points de cours** (12 × 60)
- **540 questions corrigées** (9 × 60)
- **180 schémas SVG** (3 × 60)

## 7. Conclusion

La filière `bts-cg` est **conforme** au prototype FicheLab et aux consignes de production. Les trois lots passent la validation sans erreur, couvrent les 11 matières exactes du questionnaire BTS (dont 10 avec des chapitres dédiés), ne présentent aucun doublon de titre avec les 15 filières déjà intégrées et respectent l'intégralité des contraintes de format, d'ordre des blocs, de schémas et de sources.
