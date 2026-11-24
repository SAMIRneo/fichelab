# Audit FicheLab — filière `bts-ci`

Audit de production de la filière **BTS Commerce international** (138 616 vœux Parcoursup 2026, 3ᵉ BTS le plus demandé), arrêté du 25 novembre 2020 (NOR ESRS2032837A, JORF n° 0310 du 23 décembre 2020, 1re session 2023), unités U1 à U6.

> **Rectificatif de source :** le brief indiquait « arrêté du 26 janvier 2017 ». Le texte fondateur vérifié est l'**arrêté du 25 novembre 2020** (Légifrance JORFTEXT000042722928), qui abroge l'arrêté du 24 juillet 2007 à partir de la session 2022. C'est cette référence, complétée par le BO, le référentiel et éduscol, qui figure dans les 60 champs `source`. Voir [`BTSCI-PROGRAMME.md`](BTSCI-PROGRAMME.md).

## 1. Compteurs

| Lot | Générateur | JSON | Fiches | Points | Questions | QCM | Textes | SVG |
|---|---|---|---|---|---|---|---|---|
| A | `data/gen_btsci_A.py` | `data/btsci-mat-part-A.json` | 20 | 240 | 200 | 160 | 40 | 60 |
| B | `data/gen_btsci_B.py` | `data/btsci-mat-part-B.json` | 20 | 240 | 200 | 160 | 40 | 60 |
| C | `data/gen_btsci_C.py` | `data/btsci-mat-part-C.json` | 20 | 240 | 200 | 160 | 40 | 60 |
| **Total** | **3** | **3** | **60** | **720** | **600** | **480** | **120** | **180** |

Validation à la génération, sans erreur ni avertissement de `fixtures.valider_et_ecrire` :

```
OK btsci-mat-part-A.json : 20 fiches, 240 points, 200 questions, 60 SVG
OK btsci-mat-part-B.json : 20 fiches, 240 points, 200 questions, 60 SVG
OK btsci-mat-part-C.json : 20 fiches, 240 points, 200 questions, 60 SVG
```

## 2. Répartition par matière et par année

| Matière (orthographe exacte du questionnaire) | Fiches | Préfixes | BTS1 | BTS2 |
|---|---|---|---|---|
| `Management` | 10 | `MA1.`–`MA10.` | 4 | 6 |
| `Communication` | 10 | `CO1.`–`CO10.` | 5 | 5 |
| `Marketing` | 10 | `MK1.`–`MK10.` | 4 | 6 |
| `Informatique` | 10 | `IN1.`–`IN10.` | 5 | 5 |
| `Droit` | 6 | `DR1.`–`DR6.` | 3 | 3 |
| `Économie` | 6 | `EC1.`–`EC6.` | 2 | 4 |
| `Comptabilité et gestion` | 4 | `CP1.`–`CP4.` | 1 | 3 |
| `Maths / stats` | 4 | `MS1.`–`MS4.` | 2 | 2 |

Total par année : **BTS1 = 23 fiches**, **BTS2 = 37 fiches**. Toutes les fiches ont `filieres = ["bts-ci"]` (60/60) et des années strictement dans `['BTS1']` ou `['BTS2']`. Les matières sont exactement celles attendues, sans variante orthographique ni matière supplémentaire.

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

- **180 schémas**, tous produits par `diag()` à partir des blocs de la fiche (`svg_grille`, `svg_flux`, `svg_etapes`, `svg_compare`).
- **180/180** analysables en XML via `xml.etree.ElementTree.fromstring`, sans erreur de parsing.
- Aucun `<script>`, gestionnaire `on*`, `javascript:` ni `<foreignObject>` : contrôle `INTERDIT_SVG` de `fixtures.py` (0 occurrence).
- Toutes les coordonnées de texte sont dans le `viewBox` : contrôle automatique de `fixtures.valider_fiche` (0 texte hors cadre).

## 5. Doublons et cohérence croisée

- **0 doublon de titre** sur l'ensemble des 60 fiches, contrôle effectué sur les trois JSON réunis (et pas seulement lot par lot).
- **0 doublon de préfixe** : `MA1.`–`MA10.`, `CO1.`–`CO10.`, `MK1.`–`MK10.`, `IN1.`–`IN10.`, `DR1.`–`DR6.`, `EC1.`–`EC6.`, `CP1.`–`CP4.`, `MS1.`–`MS4.` — 60 préfixes distincts.
- Aucune chaîne CJK (chinois/japonais) détectée dans les 60 fiches sérialisées.
- Tous les scripts importent `fixtures.py` et copient le modèle `gen_generale_modele.py` (12 points, 10 questions, 7 blocs ordonnés, 3 `diag()`, `valider_et_ecrire`).
- `index.html`, `inject_app.py` et `audit_filieres.py` n'ont pas été modifiés.
- Aucun outil de délégation exposé dans ce harnais : les trois lots ont été produits directement, puis contrôlés lot par lot et de manière croisée.

## 6. Verdict

**AUDIT CONFORME.** La filière `bts-ci` dispose de ses 60 fiches complètes, structurées et validées : 720 points de cours, 600 questions corrigées, 180 schémas SVG. Aucun doublon, aucun artefact CJK, aucun SVG invalide, aucun bloc hors ordre, aucune matière ou année hors périmètre.

*Seule réserve documentaire, sans incidence sur les données : la date de l'arrêté fondateur est le 25 novembre 2020 et non le 26 janvier 2017 indiqué dans le brief ; le rectificatif est consigné dans `BTSCI-PROGRAMME.md` et en tête du présent audit.*
