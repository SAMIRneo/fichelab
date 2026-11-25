# Audit FicheLab — filière `bts-ndrc`

Audit de reprise de la filière BTS NDRC (Négociation et Digitalisation de la Relation Client), arrêté du 19 février 2018 (NOR ESRS1803333A, JO du 6 mars 2018), RNCP 38368.

> **Rectificatif de source :** le brief indiquait « arrêté du 19 juin 2018 ». Le texte officiel fondateur est l'arrêté du **19 février 2018** (vérifié sur Légifrance JORFTEXT000036672161 et France Compétences RNCP 38368). C'est cette référence qui figure dans les champs `source` de tous les lots. Voir [`BTSNDRC-PROGRAMME.md`](BTSNDRC-PROGRAMME.md).

## 1. Compteurs

| Lot | Générateur | JSON | Fiches | Points | Questions | QCM | Textes | SVG |
|---|---|---|---|---|---|---|---|---|
| A (déjà livré) | `data/gen_btsndrc_A.py` | `data/btsndrc-mat-part-A.json` | 20 | 240 | 200 | 160 | 40 | 60 |
| B (repris) | `data/gen_btsndrc_B.py` | `data/btsndrc-mat-part-B.json` | 20 | 240 | 200 | 160 | 40 | 60 |
| C (repris) | `data/gen_btsndrc_C.py` | `data/btsndrc-mat-part-C.json` | 20 | 240 | 200 | 160 | 40 | 60 |
| **Total** | **3** | **3** | **60** | **720** | **600** | **480** | **120** | **180** |

Validation à la génération : `OK btsndrc-mat-part-B.json : 20 fiches, 240 points, 200 questions, 60 SVG` et idem pour le lot C, sans erreur ni avertissement de `fixtures.valider_et_ecrire`.

## 2. Répartition par matière

| Matière (orthographe exacte) | Fiches | Préfixes | Années |
|---|---|---|---|
| `Management` | 10 | `MA1.`–`MA10.` | BTS1 / BTS2 |
| `Communication` | 10 | `CO1.`–`CO10.` | BTS1 / BTS2 |
| `Marketing` | 10 | `MK1.`–`MK10.` | BTS2 |
| `Informatique` | 10 | `IN1.`–`IN10.` | BTS1 / BTS2 |
| `Droit` | 5 | `DR1.`–`DR5.` | BTS1 / BTS2 |
| `Économie` | 5 | `EC1.`–`EC5.` | BTS1 / BTS2 |
| `Maths / stats` | 5 | `MS1.`–`MS5.` | BTS1 / BTS2 |
| `Anglais professionnel` | 3 | `AN1.`–`AN3.` | BTS1 / BTS2 |
| `Français` | 2 | `PF1.`–`PF2.` | BTS1 / BTS2 |

Répartition par année (tous lots) : BTS1 = 24 fiches, BTS2 = 36 fiches. Toutes les fiches ont `filieres = ["bts-ndrc"]` (60/60). Les matières sont exactement celles attendues, sans variante orthographique.

## 3. Contrôles structurels

| Contrôle | Résultat | Attendu |
|---|---|---|
| Points par fiche | 12 sur 60 fiches | 12 ✅ |
| Questions par fiche | 10 sur 60 fiches | 9–10 ✅ |
| QCM / texte par fiche | 8 / 2 sur 60 fiches | ≥ 6 / ≥ 2 ✅ |
| Correction renseignée | 600 / 600 | toutes ✅ |
| Blocs par fiche | 7 sur 60 fiches | 7 ✅ |
| Ordre des blocs | 1 seule variante : `intro, formule, grille, liste, etapes, attention, exemples` | strict ✅ |
| Schémas par fiche | 3 sur 60 fiches | 3 ✅ |
| Fiches avec champ `source` | 60 / 60 | source officielle ✅ |
| Doublons de titres | 0 sur 60 titres | 0 ✅ |
| Préfixes uniques | 60 préfixes distincts | 60 ✅ |
| Artefacts CJK | 0 | 0 ✅ |

## 4. Schémas SVG

- **180 schémas**, tous construits avec `diag()` à partir des blocs de la fiche (grille, étapes, comparaison).
- **180/180** analysables en XML (`xml.etree.ElementTree.fromstring`), sans erreur de parsing.
- Aucun `<script>`, gestionnaire `on*`, `javascript:` ni `<foreignObject>` : contrôle `INTERDIT_SVG` de `fixtures.py`.
- Toutes les coordonnées de texte sont dans le `viewBox` : contrôle automatique de `fixtures.valider_fiche` (0 texte hors cadre).

## 5. Doublons et cohérence

- **0 doublon de titre** sur l'ensemble des 60 fiches, y compris entre le lot A préexistant et les lots B et C.
- Chaque titre est préfixé et unique (`MA1 · …` à `PF2 · …`).
- Aucune chaîne CJK (chinois/japonais) détectée dans les 60 fiches sérialisées.
- `index.html`, `inject_app.py` et `audit_filieres.py` n'ont pas été modifiés.
- Tous les scripts importent `fixtures.py` et respectent le modèle `gen_generale_modele.py` (12 points, 10 questions, 7 blocs ordonnés, 3 `diag()`, `valider_et_ecrire`).

## 6. Délégation

Aucun outil `subagent` n'est exposé dans ce harnais (recherche infructueuse dans le catalogue d'outils : `subagent`, `task`, `agent`, `spawn`, `delegate`). Les lots B et C ont donc été produits **directement** par l'agent, sans délégation, puis contrôlés lot par lot et de manière croisée.

## 7. Verdict

**AUDIT CONFORME.** La filière `bts-ndrc` dispose de ses 60 fiches complètes, structurées et validées. Les lots B et C ajoutent 40 fiches, 480 points, 400 questions corrigées et 120 schémas SVG au lot A déjà livré. Aucun doublon, aucun artefact CJK, aucun SVG invalide, aucun bloc hors ordre.

*Seule réserve documentaire, sans incidence sur les données : la date de l'arrêté fondateur est le 19 février 2018 et non le 19 juin 2018 indiqué dans le brief ; le rectificatif est consigné dans `BTSNDRC-PROGRAMME.md` et en tête du présent audit.*
