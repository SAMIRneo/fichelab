# Audit FicheLab — filière `but-info`

Audit des trois lots de fiches prototypes BUT Informatique. Périmètre :
`data/butinfo-mat-part-A.json`, `data/butinfo-mat-part-B.json`,
`data/butinfo-mat-part-C.json` et leurs générateurs `data/gen_butinfo_A/B/C.py`.
Aucune modification de `index.html`, `inject_app.py` ni `audit_filieres.py`.

## Compteurs

| Lot | Fiches | Points | Questions | QCM | Texte | SVG |
|---|---:|---:|---:|---:|---:|---:|
| A — Informatique / Maths-stats | 20 | 240 | 180 | 140 | 40 | 60 |
| B — Gestion / Comptabilité / Droit | 20 | 240 | 180 | 140 | 40 | 60 |
| C — Anglais / Communication / Marketing / Méthodologie | 20 | 240 | 180 | 140 | 40 | 60 |
| **Total `but-info`** | **60** | **720** | **540** | **420** | **120** | **180** |

Chaque fiche : **12 points**, **9 questions** (7 QCM + 2 questions texte, soit au moins 6 QCM et 2 texte), **7 blocs**, **3 schémas**.

Validation `fixtures.valider_et_ecrire` sans erreur pour les trois lots :

```
OK butinfo-mat-part-A.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK butinfo-mat-part-B.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK butinfo-mat-part-C.json : 20 fiches, 240 points, 180 questions, 60 SVG
```

Un contrôle indépendant sur les 60 objets JSON confirme **0 erreur de contrainte**
(champs obligatoires, 12 points, 9 questions, types de questions, ordre des blocs,
3 schémas, source non vide, préfixe de titre, absence de CJK).

## Répartition

### Par matière (matières exactes du questionnaire BUT)

| Matière | Fiches | Codes |
|---|---:|---|
| Informatique | 12 | IN1.–IN12. |
| Maths / stats | 8 | MS1.–MS8. |
| Gestion | 7 | GE1.–GE7. |
| Comptabilité | 7 | CP1.–CP7. |
| Droit | 6 | DR1.–DR6. |
| Anglais professionnel | 5 | AN1.–AN5. |
| Communication | 5 | CO1.–CO5. |
| Marketing | 5 | MK1.–MK5. |
| Méthodologie | 5 | ME1.–ME5. |

Le lot B couvre bien les six thèmes de droit demandés : droit de l'informatique
(DR1.), RGPD (DR2.), propriété intellectuelle (DR3.), contrats (DR4.), cyberdroit
(DR5.), responsabilité (DR6.). `Méthodologie`, issue de la base du questionnaire
supérieur, est bien utilisée (lot C).

### Par année (une fiche peut viser deux ou trois années)

| Lot | BUT1 | BUT2 | BUT3 |
|---|---:|---:|---:|
| A | 11 | 17 | 6 |
| B | 8 | 19 | 11 |
| C | 11 | 18 | 11 |
| **Total** | **30** | **54** | **28** |

Toutes les fiches déclarent `filieres = ["but-info"]` et des années appartenant
exclusivement à `{BUT1, BUT2, BUT3}`.

## Blocs d'affichage

Ordre strict vérifié sur les 60 fiches, **une seule variante** :

`intro` → `formule` → `grille` → `liste` → `etapes` → `attention` → `exemples`

Aucun bloc manquant, ajouté ou permuté.

## Schémas SVG

- **180 SVG** au total, exactement 3 par fiche.
- Tous analysables par `xml.etree.ElementTree` et conformes aux contrôles de
  `fixtures.py` (coordonnées des textes dans le `viewBox`).
- Aucune occurrence de `<script`, d'attribut `on*`, de `javascript:` ou de
  `<foreignObject` (`INTERDIT_SVG`).
- Trois familles utilisées, une par diagramme : `svg_grille` (repères),
  `svg_etapes` (procédure), `svg_compare` (distinction).

## Doublons de titres

| Contrôle | Résultat |
|---|---:|
| Doublons dans les 3 lots `but-info` | **0** |
| Titres `but-info` présents dans un autre fichier de `data/` | **0** |
| Titres `but-info` présents dans le catalogue embarqué de `index.html` | **0** |

Le dossier `data/` contient 194 paires de titres dupliquées **préexistantes**,
toutes hors filière `but-info` (lots d'autres filières, fichiers d'agent).
Aucun titre des lots A/B/C n'y est impliqué.

## Artefacts CJK

Recherche regex `[\u4e00-\u9fff\u3040-\u30ff]` sur la sérialisation complète
de chaque fiche : **0 occurrence** dans les 60 fiches. Trois caractères
parasites détectés en cours de rédaction ont été supprimés avant la validation
finale.

## Sources officielles

- **Référentiel commun** : BUT « Informatique », arrêté du 11 mars 2020
  (BO n°12 du 19 mars 2020) ; programme national 2022, arrêté du 15 avril 2022
  (BO n°19 du 12 mai 2022) ; blocs de compétences BC01 à BC05, éduscol / iut.fr.
- **A** : documentation officielle Python (python.org), norme ISO/IEC 9075 (SQL),
  modèles OSI et TCP/IP (RFC 1122), norme ISO/IEC 12207 (cycle de vie logiciel),
  W3C (HTML5/CSS), RFC 7230 (HTTP), documentation Python/Java, théorie de Landau.
- **B** : plan comptable général (arrêté du 22 juin 1999), Code de commerce,
  Code général des impôts (art. 256 à 261), directive UE 2006/112/CE, Code civil
  (art. 1103 à 1231-6, 1240 à 1245-2), Code pénal (art. 323-1 à 323-7-1),
  RGPD (UE 2016/679), CNIL, Code de la propriété intellectuelle (L111-1, L121-1,
  L611-1), directives 2000/31/CE et 2009/24/CE, normes ISO 9001 et 21500.
- **C** : CECRL du Conseil de l'Europe, Légifrance, CNIL, directive ePrivacy,
  Google Search Central, Insee, ISO 690, méthodes de Pareto, Ishikawa, Lewin,
  Kotter, Scrum/Kanban, Cepeda et al. (2006) et Roediger & Karpicke (2006).

Chaque fiche porte un champ `source` non vide qui explicite ces références et
les notions du chapitre.

## Anomalies constatées

Aucune anomalie bloquante sur le périmètre livré. Point d'organisation :

1. Les lots `but-info` ne sont **pas encore injectés** dans `index.html`.
   L'injection est une étape distincte, hors périmètre de cette mission :
   `index.html`, `inject_app.py` et `audit_filieres.py` n'ont pas été modifiés.

## Modalité d'exécution

Les trois lots ont été rédigés directement, par copie de la structure de
`gen_generale_modele.py` et des lots `gen_buttc_*.py` / `gen_butgea_*.py`, avec
`fixtures.py` pour les 12 points, les 9 questions, les 7 blocs, les 3 `diag()` et
la validation. Chaque chapitre porte un titre unique préfixé `Chapitre <CODE> —`.

## Verdict

**CONFORME.** Les 60 fiches `but-info` respectent le prototype FicheLab :
compteurs, matières exactes du questionnaire BUT, années BUT1/BUT2/BUT3, ordre
des 7 blocs, 3 SVG valides par fiche, sources officielles, aucun doublon de
titre impliquant `but-info`, aucun artefact CJK.
