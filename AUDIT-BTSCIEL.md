# Audit FicheLab — filière `bts-ciel`

Audit de production de la filière **BTS CIEL** (Cybersécurité, Informatique et réseaux, Électronique — **53 416 vœux Parcoursup 2026**, 10ᵉ BTS le plus demandé), option A « Informatique et réseaux » (IR) et option B « Électronique et réseaux » (ELC/ER).

> **Rectificatif de source :** le brief indiquait « arrêté du 19 juillet 2019 ». Le texte fondateur vérifié est l'**arrêté du 25 janvier 2023** (NOR ESRS2300958A, JORF n° 48 du 25 février 2023, 1re session 2025, RNCP37391), qui abroge l'arrêté du 15 novembre 2013 relatif au BTS Systèmes numériques. Les mentions « 19 juillet 2019 » et « ELC » figurent néanmoins dans les 60 champs `source` comme références de travail du cahier des charges, à côté de la référence exacte, du BO, d'éduscol et des arrêtés d'enseignement général (2006, 2008, 2013). Voir [`BTSCIEL-PROGRAMME.md`](BTSCIEL-PROGRAMME.md).

## 1. Compteurs

| Lot | Générateur | JSON | Fiches | Points | Questions | QCM | Textes | SVG |
|---|---|---|---|---|---|---|---|---|
| A | `data/gen_btsciel_A.py` | `data/btsciel-mat-part-A.json` | 20 | 240 | 200 | 160 | 40 | 60 |
| B | `data/gen_btsciel_B.py` | `data/btsciel-mat-part-B.json` | 20 | 240 | 200 | 160 | 40 | 60 |
| C | `data/gen_btsciel_C.py` | `data/btsciel-mat-part-C.json` | 20 | 240 | 200 | 160 | 40 | 60 |
| **Total** | **3** | **3** | **60** | **720** | **600** | **480** | **120** | **180** |

Validation à la génération, sans erreur ni avertissement de `fixtures.valider_et_ecrire` :

```
OK btsciel-mat-part-A.json : 20 fiches, 240 points, 200 questions, 60 SVG
OK btsciel-mat-part-B.json : 20 fiches, 240 points, 200 questions, 60 SVG
OK btsciel-mat-part-C.json : 20 fiches, 240 points, 200 questions, 60 SVG
```

Contrôle croisé sur les trois JSON réunis (`fixtures.valider_fiche` + contrôles spécifiques) : **0 erreur**.

## 2. Répartition par matière et par année

| Matière (orthographe exacte du questionnaire) | Fiches | Préfixes | BTS1 | BTS2 |
|---|---|---|---|---|
| `Informatique` | 12 | `IN1.`–`IN12.` | 7 | 5 |
| `Maths / stats` | 8 | `MS1.`–`MS8.` | 4 | 4 |
| `Droit` | 7 | `DR1.`–`DR7.` | 3 | 4 |
| `Économie` | 7 | `EC1.`–`EC7.` | 2 | 5 |
| `Management` | 6 | `MA1.`–`MA6.` | 3 | 3 |
| `Français` | 4 | `PF1.`–`PF4.` | 2 | 2 |
| `Anglais professionnel` | 4 | `AN1.`–`AN4.` | 2 | 2 |
| `Communication` | 4 | `CO1.`–`CO4.` | 2 | 2 |
| `Méthodologie` | 4 | `ME1.`–`ME4.` | 2 | 2 |
| `Comptabilité et gestion` | 4 | `CG1.`–`CG4.` | 2 | 2 |
| `Marketing` | 0 | — | — | — |

Total par année : **BTS1 = 29 fiches**, **BTS2 = 31 fiches**. Toutes les fiches ont `filieres = ["bts-ciel"]` (60/60) et des années strictement dans `['BTS1']` ou `['BTS2']`. Les matières sont orthographiées exactement comme dans le questionnaire ; aucune variante ni matière supplémentaire. `Marketing` est une matière du questionnaire mais la répartition demandée pour les trois lots ne lui attribue aucun chapitre : la consigne de production (A : Informatique + Maths ; B : Droit + Économie + Management ; C : Français + Anglais + Communication + Méthodologie + Comptabilité) a été suivie à la lettre.

## 3. Contrôles structurels

| Contrôle | Résultat | Attendu | Verdict |
|---|---|---|---|
| Points par fiche | 12 sur 60 fiches | 12 | ✅ |
| Questions par fiche | 10 sur 60 fiches | 9–10 | ✅ |
| QCM / texte par fiche | 8 / 2 sur 60 fiches | ≥ 6 / ≥ 2 | ✅ |
| Correction renseignée | 600 / 600 | toutes | ✅ |
| Blocs par fiche | 7 sur 60 fiches | 7 | ✅ |
| Ordre des blocs | 1 seule variante : `intro, formule, grille, liste, etapes, attention, exemples` | strict | ✅ |
| Schémas par fiche | 3 sur 60 fiches | 2–4 | ✅ |
| Fiches avec `source` officielle | 60 / 60 | toutes | ✅ |
| Préfixes uniques | 60 préfixes distincts | 60 | ✅ |
| Doublons de titres (intra + inter lots) | 0 | 0 | ✅ |
| Artefacts CJK | 0 | 0 | ✅ |

## 4. Schémas SVG

- **180 schémas**, tous produits par `diag()` à partir du contenu de la fiche (`svg_grille`, `svg_etapes`, `svg_compare`).
- **180/180** analysables en XML via `xml.etree.ElementTree.fromstring`, sans erreur de parsing.
- Aucun `<script>`, gestionnaire `on*`, `javascript:` ni `<foreignObject>` : contrôle `INTERDIT_SVG` de `fixtures.py` (0 occurrence).
- Toutes les coordonnées de texte sont dans le `viewBox` : contrôle automatique de `fixtures.valider_fiche` (0 texte hors cadre).

## 5. Doublons et cohérence croisée

- **0 doublon de titre** sur l'ensemble des 60 fiches, contrôle effectué sur les trois JSON réunis (et pas seulement lot par lot).
- **0 doublon de préfixe** : `IN1.`–`IN12.`, `MS1.`–`MS8.`, `DR1.`–`DR7.`, `EC1.`–`EC7.`, `MA1.`–`MA6.`, `PF1.`–`PF4.`, `AN1.`–`AN4.`, `CO1.`–`CO4.`, `ME1.`–`ME4.`, `CG1.`–`CG4.` — 60 préfixes distincts.
- Aucune chaîne CJK (chinois/japonais) détectée dans les 60 fiches sérialisées, contrôle effectué en lecture des trois JSON finaux.
- Tous les scripts importent `fixtures.py` via le module commun `_btsciel_common.py` et copient le modèle `gen_generale_modele.py` (12 points, 10 questions, 7 blocs ordonnés, 3 `diag()`, `valider_et_ecrire`).
- `index.html`, `inject_app.py` et `audit_filieres.py` n'ont pas été modifiés.
- Aucun outil de délégation exposé dans ce harnais : les trois lots ont été produits directement, puis contrôlés lot par lot et de manière croisée.

## 6. Verdict

**AUDIT CONFORME.** La filière `bts-ciel` dispose de ses 60 fiches complètes, structurées et validées : 720 points de cours, 600 questions corrigées, 180 schémas SVG. Aucun doublon, aucun artefact CJK, aucun SVG invalide, aucun bloc hors ordre, aucune matière ou année hors périmètre.

*Seule réserve documentaire, sans incidence sur les données : la date de l'arrêté fondateur est le 25 janvier 2023 et non le 19 juillet 2019 indiqué dans le brief ; le rectificatif est consigné dans `BTSCIEL-PROGRAMME.md` et en tête du présent audit.*
