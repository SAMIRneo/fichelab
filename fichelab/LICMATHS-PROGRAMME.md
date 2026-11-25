# Licence Mathématiques — carte des chapitres FicheLab

> **Filière :** `lic-maths` · **102 357 vœux Parcoursup 2026** (5ᵉ licence générale la plus demandée, source [`SOURCES.md`](SOURCES.md) §1, SIES / Note Flash n° 17, juillet 2026).
> **Référentiel :** arrêté du **6 avril 2021** relatif à la licence de mathématiques · **BO spécial n° 7 du 17 février 2022** (programmes de licence) · **éduscol** / ministère de l'Enseignement supérieur, de la Recherche et de l'Innovation.
> **Années :** `L1`, `L2`, `L3`. Une fiche = un chapitre, au format « prototype » (7 blocs colorés, 3 schémas SVG, 12 points, 9 questions corrigées).
> **Périmètre :** 60 fiches réparties en 3 lots de 20, sur 8 matières du questionnaire licence.

---

## 1. Référentiel et principes directeurs

L'arrêté du 6 avril 2021 et le BO spécial n° 7 du 17 février 2022 fixent le cadre national de la licence de mathématiques : **180 ECTS, six semestres**, organisés en unités d'enseignement. Les contenus de L1 à L3 couvrent l'analyse, l'algèbre, la géométrie, les probabilités et les statistiques, complétés par l'informatique scientifique et les outils méthodologiques.

Les matières FicheLab de la filière suivent **exactement la liste du questionnaire licence** (`Droit`, `Économie`, `Psychologie`, `Statistiques`, `Méthodologie universitaire`, `Anglais`, `Informatique`, `Français`, `Maths / stats`). Aucune matière hors liste n'a été introduite.

**Règle d'or :** chaque information générée démarre « à vérifier » avec sa source officielle. Les fiches sont construites à partir du modèle `data/gen_generale_modele.py` et de la bibliothèque `data/fixtures.py`, via le moteur partagé `data/gen_licmaths_common.py`.

> **Note de cadrage :** la matière `Droit` figure bien dans la liste du questionnaire licence, mais la répartition demandée pour la filière `lic-maths` n'y attribue aucun lot : les 60 créneaux sont intégralement pourvus par `Maths / stats`, `Statistiques`, `Informatique`, `Méthodologie universitaire`, `Français`, `Anglais`, `Psychologie` et `Économie`. Le droit reste couvert par la filière `lic-droit` (tronc commun des licences). Aucune fiche « Droit » n'a donc été créée ici, conformément au plan de lots reçu.

---

## 2. Carte des chapitres par année et par matière

### 2.1 Année de L1 — les fondamentaux

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Maths / stats` | **MS1.** Analyse réelle : limites et continuité · **MS2.** Algèbre linéaire : espaces vectoriels et applications linéaires · **MS3.** Suites et séries numériques · **MS4.** Fonctions d'une variable réelle : dérivation · **MS5.** Intégration et calcul d'intégrales (L1/L2) · **MS9.** Arithmétique et nombres premiers |
| `Statistiques` | **ST1.** Statistiques descriptives et graphiques · **ST2.** Probabilités et lois usuelles |
| `Informatique` | **IN1.** Algorithmique fondamentale · **IN2.** Programmation en Python |
| `Méthodologie universitaire` | **MU1.** La démonstration mathématique · **MU2.** Raisonnement logique et quantificateurs · **MU3.** Recherche documentaire et évaluation des sources · **MU4.** Rédaction mathématique et clarté de l'écrit |
| `Français` | **PF1.** Expression écrite et syntaxe française · **PF2.** Analyse de texte et argumentation |
| `Anglais` | **AN1.** Vocabulaire mathématique anglais |
| `Psychologie` | **PSY1.** Introduction à la psychologie cognitive · **PSY2.** Psychologie du développement |
| `Économie` | **EC1.** Offre et demande : formation des prix · **EC2.** Élasticités et décisions de prix |

### 2.2 Année de L2 — les matières de spécialisation

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Maths / stats` | **MS5.** Intégration (L1/L2) · **MS6.** Équations différentielles · **MS7.** Probabilités : espaces et variables aléatoires · **MS8.** Topologie et espaces métriques · **MS10.** Géométrie euclidienne et affine · **MS12.** Calcul matriciel et valeurs propres |
| `Statistiques` | **ST3.** Échantillonnage et estimation (L1/L2) · **ST4.** Tests statistiques et décision · **ST5.** Corrélation et régression linéaire |
| `Informatique` | **IN3.** Structures de données (L1/L2) · **IN4.** Bases de données et SQL · **IN5.** Calcul numérique et erreurs · **IN6.** Visualisation de données · **IN7.** LaTeX et rédaction scientifique (L1/L2) · **IN8.** Git et gestion de versions · **IN9.** Complexité des algorithmes |
| `Méthodologie universitaire` | **MU5.** L'oral et la présentation scientifique · **MU6.** Conduite de projet universitaire · **MU7.** Veille scientifique et technologique |
| `Français` | **PF3.** Rhétorique et style scientifique · **PF4.** Résumé et note de synthèse (L2/L3) |
| `Anglais` | **AN2.** Lecture d'articles scientifiques anglais (L1/L2) · **AN3.** Expression écrite scientifique en anglais · **AN4.** Communication orale en anglais |
| `Psychologie` | **PSY3.** Psychologie sociale |
| `Économie` | **EC3.** Structures de marché et concurrence · **EC4.** Comptes nationaux et PIB |

### 2.3 Année de L3 — l'approfondissement et la sortie

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Maths / stats` | **MS11.** Optimisation et programmation linéaire |
| `Statistiques` | **ST6.** Analyse de la variance (ANOVA) · **ST7.** Statistiques non paramétriques · **ST8.** Lecture critique de données et reproductibilité |
| `Informatique` | **IN10.** Programmation scientifique avec NumPy et SciPy |
| `Méthodologie universitaire` | **MU8.** Travail en équipe et collaboration (L2/L3) · **MU9.** Préparation aux concours et examens · **MU10.** Gestion du temps et techniques de révision |
| `Français` | **PF4.** Résumé et note de synthèse (L2/L3) · **PF5.** Communication écrite professionnelle |
| `Anglais` | **AN5.** Anglais pour la recherche et les conférences |
| `Psychologie` | **PSY4.** Cognition mathématique et apprentissage (L2/L3) · **PSY5.** Motivation et apprentissage |
| `Économie` | **EC5.** Inflation, chômage et politiques économiques |

> **Répartition :** 20 fiches à dominante L1 · 27 à dominante L2 · 13 à dominante L3 — soit **60 fiches** sur 8 matières. Les chapitres à cheval sur deux années (MS5, ST3, IN3, IN7, AN2, PF4, MU8, PSY4) sont comptés dans l'année de leur dominante et déclarent les deux années dans le JSON.

---

## 3. Méthode en 4 étapes

1. **Étape 1 — Cadrer.** Valider la carte des chapitres ci-dessus contre l'arrêté du 6 avril 2021, le BO spécial n° 7 du 17 février 2022 et les programmes diffusés par éduscol. Corriger tout chapitre manquant ou mal nommé.
2. **Étape 2 — Prototyper.** Copier `data/gen_generale_modele.py`, construire UNE fiche complète par matière pilote : 12 points de cours, 7 blocs colorés (intro, formule, grille, liste, étapes, attention, exemples), 3 schémas SVG intégrés, 9 questions corrigées (≥ 6 QCM + ≥ 2 rédaction).
3. **Étape 3 — Valider et décliner.** Exécuter `valider_et_ecrire()` jusqu'à l'affichage de `OK` sans erreur, puis décliner le même modèle à tous les chapitres. Contrôler chaque lot avec `fixtures.valider_fiche()` et le contrôle croisé (`_verify_licmaths.py`).
4. **Étape 4 — Auditer et livrer.** Produire `AUDIT-LICMATHS.md` (compteurs, répartition matière/année, contrôle des blocs, doublons, CJK, verdict), puis transmettre les fichiers JSON au coordinateur pour injection globale.

---

## 4. Suivi des lots

| Lot | Générateur | Sortie JSON | Matières | Statut |
|---|---|---|---|---|
| A | `data/gen_licmaths_A.py` | `data/licmaths-mat-part-A.json` | Maths / stats (12), Statistiques (8) | ✅ généré (20) |
| B | `data/gen_licmaths_B.py` | `data/licmaths-mat-part-B.json` | Informatique (10), Méthodologie universitaire (10) | ✅ généré (20) |
| C | `data/gen_licmaths_C.py` | `data/licmaths-mat-part-C.json` | Français (5), Anglais (5), Psychologie (5), Économie (5) | ✅ généré (20) |

> **Architecture :** le moteur de mise en forme est factorisé dans `data/gen_licmaths_common.py` (dérivation des 12 points, des 9 questions, des 7 blocs et des 3 schémas à partir de données pedagogiques compactes). Les trois générateurs n'utilisent que `fixtures.py` : `fiche`, `qcm`, `qt`, `diag`, `bloc`, `svg_grille`, `svg_flux`, `svg_etapes`, `svg_compare`, `valider_et_ecrire`. Aucun fichier interdit (`index.html`, `inject_app.py`, `audit_filieres.py`) n'a été modifié.

**Résultats de génération :**

```
OK licmaths-mat-part-A.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK licmaths-mat-part-B.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK licmaths-mat-part-C.json : 20 fiches, 240 points, 180 questions, 60 SVG
```

---

## 5. Sources officielles mobilisées

- **Arrêté du 6 avril 2021** relatif à la licence de mathématiques · **BO spécial n° 7 du 17 février 2022** — programmes des licences générales.
- **éduscol / Onisep / Campus France** — présentation des cursus de mathématiques et débouchés.
- **Unisciel** — ressources pédagogiques universitaires en mathématiques.
- **INSEE** — méthodes statistiques, comptes nationaux, indice des prix à la consommation.
- **INRIA, CNIL/RGPD** — algorithmique, documentation Python / NumPy / SciPy, protection des données.
- **Conseil de l'Europe** — Cadre européen commun de référence pour les langues (CECRL).
- **APA, Publication Manual** — normes de rédaction scientifique en psychologie · **ISO 690** — citation bibliographique.
- **Banque de France** — politique monétaire et taux directeurs.
- **SOURCES.md** du projet — chiffres Parcoursup 2026 (SIES, Note Flash n° 17, juillet 2026).
