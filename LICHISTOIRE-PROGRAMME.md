# Licence Histoire — carte des chapitres FicheLab

> **Filière :** `lic-histoire` · **75 686 vœux Parcoursup 2026** (10ᵉ formation la plus demandée, source [`SOURCES.md`](SOURCES.md) §1 « Top licences générales » ; libellé questionnaire : 76 000 vœux).
> **Référentiel :** **arrêté du 6 avril 2021** (référence commune des licences dans le catalogue FicheLab) · **BO spécial n° 7 du 17 février 2022** (programmes de licence) · **éduscol / ministère de l'Enseignement supérieur** · programmes des mentions d'histoire diffusés par les universités.
> **Années :** `L1`, `L2`, `L3`. Une fiche = un chapitre, au format « prototype » (12 points, 9 questions corrigées, 7 blocs ordonnés, 3 schémas SVG intégrés).

---

## 1. Référentiel et principes directeurs

Le cursus de licence d'histoire (180 ECTS, six semestres) associe les enseignements disciplinaires — histoire antique, médiévale, moderne et contemporaine, histoire de France, d'Europe et du monde — à des outils méthodologiques et des matières de soutien (droit, économie, statistiques, anglais, informatique, psychologie, expression). L'arrêté du 6 avril 2021 et le BO spécial n° 7 du 17 février 2022 fournissent le cadre national ; les programmes détaillés sont ceux diffusés par éduscol et les facultés.

**Matières exactes du questionnaire licence** (9 retenues pour la filière) : `Droit`, `Économie`, `Psychologie`, `Statistiques`, `Méthodologie universitaire`, `Anglais`, `Informatique`, `Français`, `Maths / stats`. Aucune autre matière n'est utilisée dans les fiches de cette filière.

**Règle d'or :** chaque information générée démarre « à vérifier » avec sa source officielle. Les fiches sont construites à partir du modèle `data/gen_generale_modele.py` et de la bibliothèque `data/fixtures.py`.

---

## 2. Carte des chapitres par année et par matière

### 2.1 Année de L1 — les fondamentaux

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Méthodologie universitaire` | **MU1.** La démarche historique : questionner le passé · **MU2.** La critique des sources · **MU3.** L'historiographie et les écoles · **MU4.** Le commentaire de documents |
| `Français` | **LHFR1.** L'expression écrite · **LHFR2.** La note de synthèse · **LHFR3.** L'analyse d'image |
| `Droit` | **DR1.** L'État et les institutions · **DR2.** Les personnes et la vie civile · **DR3.** La propriété et les biens |
| `Économie` | **EC1.** Offre et demande · **EC2.** Le PIB et les comptes nationaux · **EC3.** Monnaie et inflation |
| `Informatique` | **IN1.** Outils numériques de l'historien · **IN2.** Bases de données et catalogues |
| `Anglais` | **AN1.** Vocabulaire historique anglais · **AN2.** Lire une source anglaise |
| `Statistiques` | **ST1.** Statistiques descriptives · **ST2.** Probabilités |
| `Psychologie` | **PSY1.** Introduction à la psychologie · **PSY2.** Psychologie du développement |
| `Maths / stats` | **MS1.** Fonctions et variations · **MS2.** Pourcentages et proportionnalité |

### 2.2 Année de L2 — les outils d'analyse

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Méthodologie universitaire` | **MU5.** La dissertation historique · **MU6.** Recherche et bibliographie · **MU7.** Les archives · **MU8.** Chronologie et repères |
| `Français` | **LHFR4.** L'argumentation écrite · **LHFR5.** Rédaction académique · **LHFR6.** Style et clarté |
| `Droit` | **DR4.** Droit pénal et sanctions · **DR5.** Droit du travail et relations sociales |
| `Économie` | **EC4.** Chômage et marché du travail · **EC5.** Commerce international et mondialisation |
| `Informatique` | **IN3.** SIG et cartographie historique · **IN4.** Archives numériques |
| `Anglais` | **AN3.** Expression écrite en anglais |
| `Statistiques` | **ST3.** Échantillonnage et estimation · **ST4.** Tests statistiques |
| `Psychologie` | **PSY3.** Psychologie sociale et mémoires collectives |
| `Maths / stats` | **MS3.** Séries chronologiques |

### 2.3 Année de L3 — l'approfondissement et la sortie

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Méthodologie universitaire` | **MU9.** Cartes et espace historique · **MU10.** L'épreuve orale · **MU11.** Le mémoire de licence · **MU12.** Analyse d'image et photographie |
| `Français` | **LHFR7.** Lecture active d'un texte historique · **LHFR8.** L'oral : reformuler et convaincre |
| `Droit` | **DR6.** Droit européen et international · **DR7.** Droit de la culture et du patrimoine |
| `Économie` | **EC6.** Croissance et révolution industrielle · **EC7.** Finances publiques et fiscalité |
| `Informatique` | **IN5.** Visualisation des données · **IN6.** Veille documentaire |
| `Anglais` | **AN4.** Oral et présentation en anglais · **AN5.** Histoire anglophone : Grande-Bretagne et États-Unis |
| `Statistiques` | **ST5.** Corrélation et régression |
| `Psychologie` | **PSY4.** Psychologie cognitive · **PSY5.** Foules, conflits et guerre froide |
| `Maths / stats` | **MS4.** Probabilités et dénombrement · **MS5.** Régression linéaire |

> **Répartition :** 23 fiches en L1 · 18 en L2 · 19 en L3 — soit **60 fiches** sur 9 matières. Trois lots de 20 fiches : lot A = Méthodologie universitaire (12) + Français (8) ; lot B = Droit (7) + Économie (7) + Informatique (6) ; lot C = Anglais (5) + Statistiques (5) + Psychologie (5) + Maths / stats (5).

---

## 3. Méthode en 4 étapes

1. **Étape 1 — Cadrer.** Valider la carte ci-dessus contre l'arrêté du 6 avril 2021, le BO spécial n° 7 du 17 février 2022 et les ressources éduscol ; vérifier que les matières sont exactement celles du questionnaire (`lic-histoire`).
2. **Étape 2 — Prototyper.** Copier `data/gen_generale_modele.py` ; chaque fiche contient 12 points de cours, 7 blocs colorés dans l'ordre strict `intro → formule → grille → liste → etapes → attention → exemples`, 9 questions (7 QCM + 2 rédaction, toutes corrigées) et 3 schémas SVG intégrés.
3. **Étape 3 — Valider et décliner.** Exécuter `valider_et_ecrire()` jusqu'à l'affichage de `OK` sans erreur ; contrôler chaque lot avec `fixtures.valider_fiche()` et vérifier l'unicité des titres préfixés sur l'ensemble A+B+C.
4. **Étape 4 — Auditer et livrer.** Produire `AUDIT-LICHISTOIRE.md` (compteurs, répartition matière/année, blocs, SVG, doublons, CJK, verdict), puis transmettre les trois JSON au coordinateur pour injection globale.

---

## 4. Suivi des lots

| Lot | Générateur | Sortie JSON | Matières | Statut |
|---|---|---|---|---|
| A | `data/gen_lichistoire_A.py` | `data/lichistoire-mat-part-A.json` | Méthodologie universitaire (12, `MU1.`–`MU12.`), Français (8, `LHFR1.`–`LHFR8.`) | ✅ généré (20) |
| B | `data/gen_lichistoire_B.py` | `data/lichistoire-mat-part-B.json` | Droit (7, `DR1.`–`DR7.`), Économie (7, `EC1.`–`EC7.`), Informatique (6, `IN1.`–`IN6.`) | ✅ généré (20) |
| C | `data/gen_lichistoire_C.py` | `data/lichistoire-mat-part-C.json` | Anglais (5, `AN1.`–`AN5.`), Statistiques (5, `ST1.`–`ST5.`), Psychologie (5, `PSY1.`–`PSY5.`), Maths / stats (5, `MS1.`–`MS5.`) | ✅ généré (20) |

> Les préfixes sont disjoints d'un lot à l'autre : aucun doublon de titre n'est possible entre A, B et C. `index.html`, `inject_app.py` et `audit_filieres.py` ne sont pas modifiés.

---

## 5. Répartition du contenu historique dans les fiches

La licence d'histoire est une filière à matières de soutien : le contenu historique est réparti dans les fiches des matières disponibles, à raison d'exemples et d'illustrations datés dans chaque chapitre.

| Contenu historique | Fiches porteuses (exemples) |
|---|---|
| **Antiquité** | `MU1.` (Thucydide et la question du témoignage), `MU3.` (historiographie antique), `LHFR7.` (lecture d'une traduction de Tacite), `DR1.` (cité grecque et *res publica*), `AN5.` (Antiquité britannique), `MS2.` (recensement antique) |
| **Moyen Âge** | `MU2.` (critique d'une charte), `MU7.` (archives médiévales), `LHFR1.` (récit de chronique), `DR3.` (propriété féodale), `EC3.` (monnaie médiévale), `IN3.` (carte des routes médiévales) |
| **Époque moderne** | `MU3.` (École des Annales), `LHFR4.` (argumentation sur les Lumières), `DR7.` (patrimoine et collections), `EC6.` (révolution industrielle), `AN5.` (guerre d'Indépendance américaine), `ST3.` (recensements d'Ancien Régime) |
| **Époque contemporaine** | `MU5.` (dissertation sur la IIIᵉ République), `MU10.` (oral sur la Grande Guerre), `LHFR8.` (débat sur la Vᵉ République), `DR4.` (répression et sanctions), `EC7.` (fiscalité contemporaine), `PSY5.` (mémoire des guerres) |
| **France** | `MU8.` (chronologie des régimes français), `MU5.` (1789, 1848, 1870), `DR1.` (institutions de 1789 à 1958), `LHFR2.` (synthèse sur la France du XIXᵉ siècle), `EC7.` (budget de la France) |
| **Europe** | `MU9.` (cartes de l'Europe), `DR6.` (Union européenne et droits), `EC5.` (marché unique), `AN5.` (Royaume-Uni et Europe), `IN4.` (archives européennes), `MS3.` (séries européennes) |
| **Monde** | `MU6.` (bibliographie internationale), `IN6.` (veille sur l'histoire globale), `EC5.` (mondialisation), `AN5.` (États-Unis), `PSY3.` (mémoires collectives), `MS5.` (séries mondiales) |
| **Guerre froide** | `MU5.` et `MU11.` (problématiques sur la guerre froide), `LHFR6.` (style et propagande), `DR6.` (droit international et blocs), `EC5.` (échanges Est-Ouest), `PSY5.` (peurs et conflits), `ST4.` (tests sur des séries de la guerre froide) |
| **Colonisation** | `MU4.` (commentaire de sources coloniales), `MU9.` (cartes coloniales), `LHFR3.` (analyse d'affiches), `DR7.` (restitutions et patrimoine), `EC6.` (colonisation et économie), `IN3.` (SIG des territoires coloniaux), `AN4.` (sources anglophones sur l'empire) |
| **Révolutions** | `MU5.` (1789), `LHFR4.` (rhétorique révolutionnaire), `DR2.` (droits de l'homme), `EC4.` (marché du travail après 1848), `PSY3.` (psychologie des foules révolutionnaires), `MS4.` (dénombrement des événements) |

---

## 6. Sources officielles mobilisées

- **Arrêté du 6 avril 2021** — référence commune des licences dans le catalogue FicheLab (cf. `LICDROIT-PROGRAMME.md`).
- **BO spécial n° 7 du 17 février 2022** — programmes des licences générales.
- **éduscol / ministère de l'Enseignement supérieur** — ressources et attendus des mentions d'histoire.
- **SOURCES.md** du projet — chiffres Parcoursup 2026 (SIES, Note Flash n° 17, juillet 2026) : Histoire 75 686 vœux.
- Références complémentaires utilisées dans les fiches : Code civil, Code pénal, Code du travail, traités européens, CNIL/RGPD, INSEE, Cadre européen commun de référence pour les langues (Conseil de l'Europe).
