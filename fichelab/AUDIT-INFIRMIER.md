# Audit FicheLab — filière `infirmier` (IFSI)

Date : 24 novembre 2026 · Périmètre : `infirmier` (`Infirmier (IFSI)`) · Années : `IFSI1`, `IFSI2`, `IFSI3`.

Audit indépendant des trois lots MCP (matières) réalisé avec `data/fixtures.py` :
`valider_fiche()` sur chaque fiche des JSON livrés, contrôle des doublons de titre
intra-lot **et inter-lots**, analyse XML des SVG, recherche d'artefacts CJK et
vérification de l'ordre strict des 7 blocs d'affichage.

---

## 1. Compteurs par lot

| Lot | Générateur | JSON | Fiches | Points | Questions | QCM | Texte | SVG | Sources |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| A | `data/gen_infirmier_A.py` | `data/infirmier-mat-part-A.json` | 20 | 240 | 180 | 140 | 40 | 60 | 20/20 |
| B | `data/gen_infirmier_B.py` | `data/infirmier-mat-part-B.json` | 22 | 264 | 198 | 154 | 44 | 66 | 22/22 |
| C | `data/gen_infirmier_C.py` | `data/infirmier-mat-part-C.json` | 20 | 240 | 180 | 140 | 40 | 60 | 20/20 |
| **Total** | — | — | **62** | **744** | **558** | **434** | **124** | **186** | **62/62** |

Chaque fiche respecte 12 points, 9 questions corrigées (7 QCM + 2 rédaction),
3 schémas `diag()` et une source explicite. Aucun écart détecté sur ces compteurs.

## 2. Répartition par matière

| Matière | Fiches | Lots |
|---|---:|---|
| Anatomie | 7 | A |
| Physiologie | 14 | A (7) + B (7) |
| Biochimie | 6 | A |
| Microbiologie | 7 | B |
| Pharmacologie | 8 | B |
| Droit de la santé | 5 | C (`DS1.`–`DS5.`) |
| Éthique | 4 | C (`ET1.`–`ET4.`) |
| Français | 3 | C (`PF1.`–`PF3.`) |
| Maths / stats | 3 | C (`PS1.`–`PS3.`) |
| Anglais professionnel | 2 | C (`PE1.`–`PE2.`) |
| Méthodologie | 3 | C (`PM1.`–`PM3.`) |

Répartition du lot C conforme à la carte `INFIRMIER-PROGRAMME.md` §6 :
Droit 5 · Éthique 4 · Français 3 · Maths 3 · Anglais 2 · Méthodologie 3 = 20.

## 3. Répartition par année

| Année | Fiches | Détail |
|---|---:|---|
| `IFSI1` | 26 | A (20) + C : Français 3, Maths / stats 3 |
| `IFSI2` | 25 | B (22) + C : Droit 3 |
| `IFSI3` | 11 | C : Droit 2, Éthique 4, Anglais 2, Méthodologie 3 |

## 4. Contrôles de conformité

| Contrôle | Résultat | Attendu |
|---|---|---|
| `valider_fiche()` sur 62 fiches | **0 erreur** | 0 |
| Ordre des 7 blocs (`intro, formule, grille, liste, etapes, attention, exemples`) | 62/62 | 62/62 |
| Points par fiche | 12 sur 62/62 | 10–14 (cible 12) |
| Questions par fiche | 9 sur 62/62 | 8–10 (cible 9) |
| QCM / texte | ≥6 / ≥2 sur 62/62 | ≥6 / ≥2 |
| Corrections renseignées | 558/558 | 558/558 |
| Schémas SVG | 186, XML valides, sans `<script>`, `on*`, `javascript:` ou `foreignObject` | conformes |
| Texte dans le `viewBox` | 186/186 | conformes |
| Doublons de titre intra-lots | 0 | 0 |
| Doublons de titre inter-lots | 0 | 0 |
| Artefacts CJK (chinois/japonais) | 0 | 0 |
| Sources officielles renseignées | 62/62 | 62/62 |
| Titres préfixés uniques (`AT.`, `PH.`, `PHB.`, `BC.`, `MI.`, `PA.`, `DS.`, `ET.`, `PF.`, `PS.`, `PE.`, `PM.`) | OK | OK |

## 5. Actions correctives effectuées sur le lot C

- `data/gen_infirmier_C.py` était incomplet (arrêt sur `# __LOT_C_MATHS__`, sans appel à
  `valider_et_ecrire`) et non exécutable : 13 erreurs de construction des listes
  d'arguments de `blocs()` et 3 artefacts CJK (`必须`, `便利`, `杰伦`) corrigées.
- Ajout des 8 fiches manquantes (`PS1.`–`PS3.`, `PE1.`–`PE2.`, `PM1.`–`PM3.`) selon le
  modèle `data/gen_generale_modele.py`, avec `fixtures.py`, 12 points, 9 questions
  (7 QCM + 2 texte), 7 blocs en ordre strict, 3 schémas `diag()` et sources officielles.
- Appel final `valider_et_ecrire(F, "infirmier-mat-part-C.json")`, exécuté jusqu'à :
  `OK infirmier-mat-part-C.json : 20 fiches, 240 points, 180 questions, 60 SVG`.
- Lots A et B **non modifiés** (déjà livrés et validés). `index.html`, `inject_app.py`
  et `audit_filieres.py` **non modifiés**.

## 6. Verdict

**AUDIT CONFORME** — 62 fiches, 0 erreur de validation, 0 doublon de titre,
0 artefact CJK, 186 SVG valides, 7 blocs en ordre strict sur l'ensemble des fiches.

Note opérationnelle : l'outil `subagent` n'est pas exposé dans cet environnement
(aucun outil de délégation dans le catalogue, seul `automation`/`opencode` est
disponible). Le lot C a donc été produit directement ; les consignes de délégation
(modèle, `fixtures.py`, 12 points, 9 questions, 7 blocs, 3 `diag()`, sources
officielles, aucun CJK, validation jusqu'à `OK`) ont été appliquées telles quelles.
