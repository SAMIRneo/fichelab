# Audit CPGE ECG — FicheLab

> Filière **`cpge-ecg`** (ECG1 = `1re`, ECG2 = `2e`). Audit des trois lots de fiches prototypes, généré le 24 novembre 2026.
> Périmètre : `data/gen_cpgeecg_A.py`, `data/gen_cpgeecg_B.py`, `data/gen_cpgeecg_C.py`, le module partagé `data/_cpgeecg_common.py` et leurs sorties JSON. Les fichiers protégés `index.html`, `inject_app.py` et `audit_filieres.py` n'ont **pas** été modifiés.

## 1. Compteurs

| Lot | Générateur | JSON | Fiches | Points | Questions | QCM | Texte | SVG |
|---|---|---|---:|---:|---:|---:|---:|---:|
| A | `gen_cpgeecg_A.py` | `cpgeecg-mat-part-A.json` | 20 | 240 | 180 | 140 | 40 | 60 |
| B | `gen_cpgeecg_B.py` | `cpgeecg-mat-part-B.json` | 20 | 240 | 180 | 140 | 40 | 60 |
| C | `gen_cpgeecg_C.py` | `cpgeecg-mat-part-C.json` | 16 | 192 | 144 | 112 | 32 | 48 |
| **Total** | 3 scripts | 3 JSON | **56** | **672** | **504** | **392** | **112** | **168** |

Chaque fiche contient exactement **12 points**, **9 questions corrigées** (7 QCM + 2 texte) et **3 schémas SVG**. Chiffres conformes au prototype de référence (`FICHE-PROTOTYPE.md`).

## 2. Répartition par matière et par année

| Matière | Préfixes | Fiches | `1re` | `2e` |
|---|---|---:|---:|---:|
| Maths | `MA1.`–`MA12.` | 12 | 6 | 6 |
| Économie | `EC1.`–`EC8.` | 8 | 4 | 4 |
| Philosophie | `PHI1.`–`PHI10.` | 10 | 5 | 5 |
| Français | `FR1.`–`FR10.` | 10 | 5 | 5 |
| Anglais | `AN1.`–`AN6.` | 6 | 3 | 3 |
| Maths / stats | `MS1.`–`MS5.` | 5 | 2 | 3 |
| Méthodologie | `ME1.`–`ME5.` | 5 | 3 | 2 |
| **Total** | | **56** | **28** | **28** |

Toutes les fiches déclarent `filieres = ["cpge-ecg"]` et une seule année (`["1re"]` ou `["2e"]`). Les matières sont exactement celles de la carte [`CPGEECG-PROGRAMME.md`](CPGEECG-PROGRAMME.md) : le questionnaire CPGE est prioritaire (Maths, Économie, Philosophie, Français, Anglais), complété par Maths / stats et Méthodologie. Physique, Chimie et Histoire-Géographie sont absentes de la liste CPGE du questionnaire et n'ont donc pas été retenues, conformément à la consigne.

## 3. Blocs d'affichage et schémas

- **Ordre strict des 7 blocs** : `intro, formule, grille, liste, etapes, attention, exemples` — **56/56 fiches** conformes.
- **Schémas** : 168 SVG, soit **3 par fiche**. Tous sont analysables en XML, emploient des variables de thème clair/sombre (`var(--ac)`, `var(--card2)`, `var(--fg)`, `var(--ac-tx)`, `var(--ac-tx)`) et ne contiennent ni `<script>`, ni gestionnaire d'événement, ni `javascript:`, ni `foreignObject`. Les textes restent dans le `viewBox` (contrôle `fixtures.valider_fiche()`).
- Types de schémas utilisés : `svg_grille` (tableaux de lecture), `svg_etapes` (procédures numérotées), `svg_flux` (chaînes), `svg_compare` (oppositions).

## 4. Contrôles d'intégrité

| Contrôle | Résultat |
|---|---|
| Validation `fixtures.valider_fiche()` sur 56 fiches | **0 erreur** |
| Doublons de titres **entre les trois lots** | **0** |
| Préfixes de chapitres dupliqués (`MA1.`, `PHI1.`…) | **0** |
| Préfixes contigus et cohérents avec la matière | **56/56** |
| Artefacts CJK (chinois/japonais) | **0** |
| Sources officielles (arrêté du 19 juillet 2019, BO spéciaux n° 1 du 11 février 2021, n° 5 et n° 8 du 25 juillet 2019, éduscol) | **56/56** |
| Titres préfixés et uniques | **56/56** |
| Corrections présentes sur toutes les questions | **504/504** |
| `filieres = ["cpge-ecg"]` | **56/56** |
| `annees` = `["1re"]` ou `["2e"]` | **56/56** |
| 12 points / 9 questions / 3 SVG par fiche | **56/56** |

Les trois générateurs se relancent sans erreur et réécrivent leurs JSON de façon identique :

```
OK cpgeecg-mat-part-A.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK cpgeecg-mat-part-B.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK cpgeecg-mat-part-C.json : 16 fiches, 192 points, 144 questions, 48 SVG
```

Le script de vérification indépendant `data/_audit_cpgeecg.py` confirme :

```
OK lot A : 20 fiches
OK lot B : 20 fiches
OK lot C : 16 fiches

Total : 56 fiches, 672 points, 504 questions (392 QCM / 112 texte), 168 SVG
Annees : {"1re": 28, "2e": 28}
ERREURS VALIDATION: 0
DOUBLONS TITRES: []
```

## 5. Couverture thématique

- **Maths (12)** : algèbre linéaire, limites et continuité, fonctions de référence, suites (`1re`) ; probabilités, inférence, optimisation, calcul matriciel, économie mathématique, suites récurrentes (`2e`) ; intégrales et dérivation complètent le tronc commun.
- **Économie (8)** : rareté, offre et demande, élasticités, structures de marché (`1re`) ; comptabilité nationale, croissance et PGF, monnaie et inflation, commerce international et change (`2e`) — cohérent avec l'option ESH.
- **Philosophie (10)** : conscience, liberté, vérité, technique, justice (`1re`) ; bonheur, art, religion, langage, méthode de dissertation (`2e`).
- **Français (10)** : littérature des XIXᵉ et XXᵉ siècles, grammaire, dissertation, commentaire (`1re`) ; traduction, oral, œuvre au programme, argumentation, synthèse (`2e`).
- **Anglais (6)** : grammaire, compréhension écrite, expression écrite (`1re`) ; expression orale, civilisation anglo-saxonne, méthodologie des concours (`2e`).
- **Maths / stats (5)** et **Méthodologie (5)** : statistique descriptive et probabilités, lois usuelles, estimation, tests et régression ; révision espacée, fiches et synthèse, gestion du temps, analyse de sujet et logique argumentative (Cepeda 2006, Roediger & Karpicke 2006).

## 6. État d'injection dans l'application

Les trois fichiers JSON sont prêts à l'emploi. Aucune injection n'a été effectuée dans `index.html`, conformément à la consigne de ne pas modifier les fichiers protégés. Cette opération reste à la charge du responsable de l'application.

## 7. Verdict

**DONNÉES CONFORMES** — 56 fiches, 672 points, 504 questions corrigées, 168 schémas SVG, zéro doublon inter-lots, zéro artefact CJK, zéro erreur de validation. La filière `cpge-ecg` atteint sa cible de 56 fiches au format prototype.

**Application : EN ATTENTE D'INJECTION** (hors périmètre, fichiers protégés).
