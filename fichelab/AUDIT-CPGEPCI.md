# Audit CPGE PCSI — FicheLab

> Filière **`cpge-pci`** (PCSI1 = `1re`, PCSI2 = `2e`). Audit des trois lots de fiches prototypes, généré le 24 novembre 2026.
> Périmètre : `data/gen_cpgepci_A.py`, `data/gen_cpgepci_B.py`, `data/gen_cpgepci_C.py` et leurs sorties JSON. Les fichiers protégés `index.html`, `inject_app.py` et `audit_filieres.py` n'ont **pas** été modifiés.

## 1. Compteurs

| Lot | Générateur | JSON | Fiches | Points | Questions | QCM | Texte | SVG |
|---|---|---|---:|---:|---:|---:|---:|---:|
| A | `gen_cpgepci_A.py` | `cpgepci-mat-part-A.json` | 20 | 240 | 180 | 140 | 40 | 60 |
| B | `gen_cpgepci_B.py` | `cpgepci-mat-part-B.json` | 20 | 240 | 180 | 140 | 40 | 60 |
| C | `gen_cpgepci_C.py` | `cpgepci-mat-part-C.json` | 16 | 192 | 144 | 112 | 32 | 48 |
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

Toutes les fiches déclarent `filieres = ["cpge-pci"]` et une seule année (`["1re"]` ou `["2e"]`). Les matières sont exactement celles de la carte [`CPGEPCI-PROGRAMME.md`](CPGEPCI-PROGRAMME.md), avec un préfixe de chapitre unique par fiche.

## 3. Blocs d'affichage et schémas

- **Ordre strict des 7 blocs** : `intro, formule, grille, liste, etapes, attention, exemples` — **56/56 fiches** conformes.
- **Schémas** : 168 SVG, soit **3 par fiche**. Tous sont analysables en XML, emploient des variables de thème clair/sombre (`var(--ac)`, `var(--card2)`, `var(--fg)`, `var(--ac-tx)`) et ne contiennent ni `<script>`, ni gestionnaire d'événement, ni `javascript:`, ni `foreignObject`. Les textes restent dans le `viewBox` (contrôle `fixtures.valider_fiche()`).
- Types de schémas utilisés : `svg_grille` (tableaux de lecture), `svg_etapes` (procédures), `svg_flux` (chaînes), `svg_compare` (oppositions).

## 4. Contrôles d'intégrité

| Contrôle | Résultat |
|---|---|
| Validation `fixtures.valider_fiche()` sur 56 fiches | **0 erreur** |
| Doublons de titres **entre les trois lots** | **0** |
| Préfixes de chapitres dupliqués (`MA1.`, `CH1.`…) | **0** |
| Préfixe cohérent avec la matière | **56/56** |
| Artefacts CJK (chinois/japonais) | **0** |
| Sources officielles renseignées (arrêté du 19 juillet 2019, BO spéciaux n° 5 et n° 8, éduscol) | **56/56** |
| Titres préfixés et uniques | **56/56** |
| Corrections présentes sur toutes les questions | **504/504** |
| `filieres = ["cpge-pci"]` | **56/56** |
| `annees` = `["1re"]` ou `["2e"]` | **56/56** |

Les trois générateurs se relancent sans erreur et réécrivent leurs JSON de façon identique :

```
OK cpgepci-mat-part-A.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK cpgepci-mat-part-B.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK cpgepci-mat-part-C.json : 16 fiches, 192 points, 144 questions, 48 SVG
```

Le script de vérification indépendant `data/_audit_cpgepci.py` confirme : `ERREURS VALIDATION: 0`, `DOUBLONS TITRES: []`, `DOUBLONS PREFIXES: []`, `ATTENDU OK: True`, `BLOCS OK: True`, `INTERDIT SVG: False`.

## 5. Couverture thématique

- **Maths** : algèbre, analyse, suites, intégration, fonctions de référence (`1re`) ; équations différentielles, probabilités, géométrie, complexes, arithmétique et logique (`2e`).
- **Physique** : cinématique, dynamique, énergie, quantité de mouvement, oscillations (`1re`) ; ondes, optique, électricité, électromagnétisme, thermique (`2e`).
- **Chimie** : atomistique, liaisons, réactivité, acide-base, oxydoréduction (`1re`) ; cinétique, équilibres, thermochimie, organique, analyse (`2e`). Les attendus de sciences de l'ingénieur sont intégrés transversalement (`PH4.`, `PH8.`, `CH3.`, `CH10.`).
- **Français / Philosophie / Anglais / Économie / Maths-stats** : littérature des XIXᵉ et XXᵉ siècles, méthodologie des épreuves, questions philosophiques classiques, grammaire et civilisation anglo-saxonnes, micro- et macroéconomie, probabilités et inférence.

## 6. État d'injection dans l'application

Les trois fichiers JSON sont prêts à l'emploi. Aucune injection n'a été effectuée dans `index.html`, conformément à la consigne de ne pas modifier les fichiers protégés. Cette opération reste à la charge du responsable de l'application.

## 7. Verdict

**DONNÉES CONFORMES** — 56 fiches, 672 points, 504 questions corrigées, 168 schémas SVG, zéro doublon inter-lots, zéro artefact CJK, zéro erreur de validation. La filière `cpge-pci` atteint sa cible de 56 fiches au format prototype.

**Application : EN ATTENTE D'INJECTION** (hors périmètre, fichiers protégés).
