# Audit CPGE MPSI — FicheLab

> Filière **`cpge-mpsi`** (MPSI1 = `1re`, MPSI2 = `2e`). Audit des trois lots de fiches prototypes, généré le 24 novembre 2026.
> Périmètre : `data/gen_cpge_A.py`, `data/gen_cpge_B.py`, `data/gen_cpge_C.py` et leurs sorties JSON. Les fichiers `index.html`, `inject_app.py` et `audit_filieres.py` n'ont **pas** été modifiés.

## 1. Compteurs

| Lot | Générateur | JSON | Fiches | Points | Questions | QCM | Texte | SVG |
|---|---|---|---:|---:|---:|---:|---:|---:|
| A (préexistant, validé) | `gen_cpge_A.py` | `cpge-mat-part-A.json` | 20 | 240 | 180 | 140 | 40 | 60 |
| B (produit) | `gen_cpge_B.py` | `cpge-mat-part-B.json` | 20 | 240 | 180 | 140 | 40 | 60 |
| C (produit) | `gen_cpge_C.py` | `cpge-mat-part-C.json` | 16 | 192 | 144 | 112 | 32 | 48 |
| **Total** | 3 scripts | 3 JSON | **56** | **672** | **504** | **392** | **112** | **168** |

Chaque fiche contient exactement **12 points**, **9 questions corrigées** (7 QCM + 2 texte) et **3 schémas SVG**. Chiffres conformes au prototype de référence (`FICHE-PROTOTYPE.md`).

## 2. Répartition par matière et par année

| Matière | Préfixes | Fiches | `1re` | `2e` |
|---|---|---:|---:|---:|
| Maths | `MA1.`–`MA10.` | 10 | 5 | 5 |
| Physique | `PH1.`–`PH10.` | 10 | 5 | 5 |
| Chimie | `CH1.`–`CH10.` | 10 | 5 | 5 |
| Français | `FR1.`–`FR5.` | 5 | 2 | 3 |
| Philosophie | `PHI1.`–`PHI5.` | 5 | 3 | 2 |
| Anglais | `AN1.`–`AN6.` | 6 | 3 | 3 |
| Économie | `EC1.`–`EC6.` | 6 | 3 | 3 |
| Maths / stats | `MS1.`–`MS4.` | 4 | 2 | 2 |
| **Total** | | **56** | **28** | **28** |

Toutes les fiches déclarent `filieres = ["cpge-mpsi"]` et une seule année (`["1re"]` ou `["2e"]`).

## 3. Blocs d'affichage et schémas

- **Ordre strict des 7 blocs** : `intro, formule, grille, liste, etapes, attention, exemples` — **56/56 fiches** conformes, une seule variante relevée sur l'ensemble des lots.
- **Schémas** : 168 SVG, soit 3 par fiche. Tous sont analysables en XML, emploient des variables de thème clair/sombre (`var(--ac)`, `var(--card2)`, `var(--fg)`) et ne contiennent ni `<script>`, ni gestionnaire d'événement, ni `javascript:`, ni `foreignObject`. Les textes restent dans le `viewBox`.
- Types de schémas utilisés : `svg_grille` (tableaux de lecture), `svg_etapes` (procédures), `svg_flux` (chaînes), `svg_compare` (oppositions).

## 4. Contrôles d'intégrité

| Contrôle | Résultat |
|---|---|
| Validation `fixtures.valider_fiche()` sur 56 fiches | **0 erreur** |
| Doublons de titres **entre les trois lots** | **0** |
| Préfixes de chapitres dupliqués (`MA1.`, `CH1.`…) | **0** |
| Artefacts CJK (chinois/japonais) | **0** |
| Sources officielles renseignées (arrêté du 19 juillet 2019, BO spéciaux n° 5 et n° 8, éduscol) | **56/56** |
| Titres préfixés et uniques | **56/56** |
| Corrections présentes sur toutes les questions | **504/504** |

Les trois générateurs se relancent sans erreur et réécrivent leurs JSON de façon identique :

```
OK cpge-mat-part-A.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK cpge-mat-part-B.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK cpge-mat-part-C.json : 16 fiches, 192 points, 144 questions, 48 SVG
```

## 5. Délégation

L'outil de délégation `subagent` **n'est pas exposé** dans ce harness (recherche d'outils effectuée : aucun outil `subagent`, `task` ou équivalent). Les lots B et C ont donc été produits **directement par le responsable de filière**, en appliquant strictement les consignes prévues pour les agents : copie de `gen_generale_modele.py` (structure `add`/`schema_des` alignée sur `gen_cpge_A.py`), usage exclusif de `fixtures.py`, 12 points, 9 questions (7 QCM + 2 texte), 7 blocs en ordre strict, 3 schémas `diag()`, validation sans erreur.

## 6. État d'injection dans l'application

Les trois fichiers JSON sont prêts à l'emploi. `index.html` contient encore d'anciennes fiches texte brut pour `cpge-mpsi`, mais **aucun prototype `cpge-mat-part-*.json` n'y a été injecté** : l'injection n'a pas été effectuée, conformément à la consigne de ne pas modifier `index.html`, `inject_app.py` ni `audit_filieres.py`. Cette opération reste à la charge du responsable de l'application.

## 7. Verdict

**Données CONFORMES** — 56 fiches, 672 points, 504 questions corrigées, 168 schémas SVG, zéro doublon, zéro artefact CJK, zéro erreur de validation. Les lots B et C complètent le lot A et portent la filière `cpge-mpsi` à sa cible de 56 fiches.

**Application : EN ATTENTE D'INJECTION** (hors périmètre de cette reprise, fichiers protégés).
