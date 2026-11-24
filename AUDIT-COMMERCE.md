# Audit de la filière `commerce` — FicheLab

> Audit réalisé après génération des trois lots, le 24 novembre 2026.
> Périmètre : `COMMERCE-PROGRAMME.md`, `data/gen_commerce_common.py`, `data/gen_commerce_A/B/C.py` et `data/commerce-mat-part-A/B/C.json`.
> **Fichiers applicatifs non modifiés** : `index.html`, `inject_app.py`, `audit_filieres.py` (consigne du chantier respectée).

## 1. Résultat global

| Contrôle | Valeur | Attendu | Résultat |
|---|---:|---:|---|
| Fiches prototype | 60 | 60 (3 × 20) | ✅ |
| Points de cours | 720 | 12 par fiche | ✅ |
| Questions corrigées | 600 | 10 par fiche | ✅ |
| — dont QCM | 480 | ≥ 6 par fiche (8 ici) | ✅ |
| — dont questions texte | 120 | ≥ 2 par fiche (2 ici) | ✅ |
| Schémas SVG | 180 | 3 par fiche, via `diag()` | ✅ |
| Blocs d'affichage | 60 × 7 | ordre strict `intro, formule, grille, liste, etapes, attention, exemples` | ✅ |
| Titres uniques | 60 / 60 | aucun doublon | ✅ |
| Artefacts CJK | 0 | aucun | ✅ |
| SVG interdits (`<script>`, `on*`, `javascript:`, `foreignObject`) | 0 | aucun | ✅ |
| XML des SVG | 180 / 180 analysables | valide | ✅ |
| Erreurs `fixtures.valider_fiche` | 0 | 0 | ✅ |

**Verdict : CONFORME — validation OK sans erreur.**

## 2. Lots générés

| Lot | Générateur | JSON | Fiches | Points | Questions | SVG | Statut |
|---|---|---|---:|---:|---:|---:|---|
| A | `data/gen_commerce_A.py` | `data/commerce-mat-part-A.json` | 20 | 240 | 200 (160 QCM + 40 texte) | 60 | ✅ OK |
| B | `data/gen_commerce_B.py` | `data/commerce-mat-part-B.json` | 20 | 240 | 200 (160 QCM + 40 texte) | 60 | ✅ OK |
| C | `data/gen_commerce_C.py` | `data/commerce-mat-part-C.json` | 20 | 240 | 200 (160 QCM + 40 texte) | 60 | ✅ OK |

Sorties des générateurs :

```
OK commerce-mat-part-A.json : 20 fiches, 240 points, 200 questions, 60 SVG
OK commerce-mat-part-B.json : 20 fiches, 240 points, 200 questions, 60 SVG
OK commerce-mat-part-C.json : 20 fiches, 240 points, 200 questions, 60 SVG
```

## 3. Vérification des matières et des codes

Matières exactes du questionnaire (`MATIERES.but` + base sup `Français`) — aucune matière inventée :

| Lot | Matière | Codes attendus | Codes présents | Compte |
|---|---|---|---|---:|
| A | `Marketing` | `MK1.` … `MK12.` | MK1 … MK12 | 12 |
| A | `Communication` | `CO1.` … `CO8.` | CO1 … CO8 | 8 |
| B | `Gestion` | `GE1.` … `GE10.` | GE1 … GE10 | 10 |
| B | `Comptabilité` | `CP1.` … `CP10.` | CP1 … CP10 | 10 |
| C | `Droit` | `DR1.` … `DR5.` | DR1 … DR5 | 5 |
| C | `Maths / stats` | `MS1.` … `MS5.` | MS1 … MS5 | 5 |
| C | `Informatique` | `IN1.` … `IN4.` | IN1 … IN4 | 4 |
| C | `Anglais professionnel` | `AN1.` … `AN4.` | AN1 … AN4 | 4 |
| C | `Français` | `PF1.`, `PF2.` | PF1, PF2 | 2 |

Chaque code apparaît **une et une seule fois** dans son lot ; la `Méthodologie` de la base sup est traitée comme contenu transversal dans `PF1`, `PF2`, `CO1`, `GE9` et `GE10` (aucun chapitre hors barème demandé n'a été ajouté).

## 4. Années et préfixes

- `filieres` vaut exactement `["commerce"]` sur **60 / 60** fiches.
- `annees` vaut exactement `["Bac+1"]`, `["Bac+2"]` ou `["Bac+3"]` sur **60 / 60** fiches (jamais plusieurs années ni de valeur « all »).

| Lot | Bac+1 | Bac+2 | Bac+3 |
|---|---:|---:|---:|
| A | 7 | 8 | 5 |
| B | 6 | 8 | 6 |
| C | 7 | 8 | 5 |
| **Total** | **20** | **24** | **16** |

- Titres préfixés de la forme `Commerce <lot> · <code> · <sujet>` : 60 / 60.
- Aucun titre en double, ni dans un lot, ni entre les trois lots, ni avec le catalogue existant (préfixe `Commerce` inutilisé ailleurs).
- Aucune question en double à l'intérieur d'une même fiche.

## 5. Sources et contenu

- Chaque fiche porte une source explicite mêlant référentiels officiels et programmes : référentiel BUT Techniques de commercialisation (arrêté du 11 mars 2020, BO n°12), référentiel BUT GEA, plan comptable général (arrêté du 22 juin 1993), Code civil, Code de commerce, Code de la consommation, Code du travail, RGPD, CECRL, programmes des écoles de commerce (RNCP), éduscol / iut.fr / onisep.fr.
- Chaque fiche démarre au statut « à vérifier » conformément à la règle du catalogue ; les exercices ne sont pas présentés comme des sujets officiels.
- Contrôle CJK : expression régulière `[\u4e00-\u9fff\u3040-\u30ff]` appliquée à la sérialisation JSON complète → **0 occurrence**.

## 6. Méthode de contrôle

1. Exécution de `python data/gen_commerce_A.py`, `python data/gen_commerce_B.py`, `python data/gen_commerce_C.py` : la fonction `valider_et_ecrire` de `fixtures.py` valide champs, corrections, ordre des blocs, coordonnées des textes SVG, XML, CJK et doublons du lot.
2. Contrôle croisé des trois JSON par un script indépendant (hors dépôt) comparant codes, matières, années, préfixes, compteurs, sources, XML des SVG, absence de CJK et doublons globaux de titres et de questions.
3. Aucune modification des fichiers applicatifs protégés.

## 7. Intégration (à faire par l'orchestrateur)

`inject_app.py` contient une liste `FILIERES_A_INTEGRER` figée qui n'inclut pas encore `"commerce"`. Pour rendre les fiches visibles dans l'application :

1. ajouter `"commerce"` à `FILIERES_A_INTEGRER` dans `data/inject_app.py` (opération volontairement hors du périmètre de ce lot) ;
2. relancer `python data/inject_app.py` pour reconstruire `EXTRA_FICHES`, `PROTO_FILIERES` et la migration ;
3. relancer `python data/audit_filieres.py` pour vérifier le catalogue injecté.

Les trois lots sont prêts et validés ; aucune autre action n'est nécessaire sur les fichiers de la filière `commerce`.
