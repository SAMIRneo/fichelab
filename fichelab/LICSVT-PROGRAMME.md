# Licence Sciences de la vie — carte des chapitres FicheLab

> **Filière :** `lic-svt` · **100 640 vœux Parcoursup 2026** (7ᵉ licence générale la plus demandée, source [`SOURCES.md`](SOURCES.md) §1 — « Top licences générales »).
> **Référentiel :** **arrêté du 6 avril 2021** relatif à la licence (JORF n° 0083 du 8 avril 2021, NOR MESR2012468A), pris en application des articles L.621-1 et suivants du Code de l'éducation · **BO spécial n° 7 du 17 février 2022** (programmes des licences générales) · **éduscol** / ministère de l'Enseignement supérieur, de la Recherche et de l'Innovation · **Code de la santé publique**, **Code civil**, **RGPD** pour les volets droit, éthique et données de santé.
> **Années :** `L1`, `L2`, `L3`. Une fiche = un chapitre, au format « prototype » (7 blocs + 3 schémas SVG, 12 points, 9 questions corrigées).
> **Matières du questionnaire (respectées à l'identique) :** Droit, Économie, Psychologie, Statistiques, Méthodologie universitaire, Anglais, Informatique, Français, Maths / stats.

---

## 1. Référentiel et principes directeurs

L'arrêté du 6 avril 2021 fixe le cadre national de la licence : **180 ECTS, six semestres**, organisés en unités d'enseignement (UE). La mention **Sciences de la vie** articule :

- des **UE fondamentales de biologie** (biologie cellulaire et moléculaire, génétique, biochimie, physiologie, microbiologie, botanique, zoologie, écologie, évolution) ;
- des **UE quantitatives et numériques** (mathématiques, statistiques, informatique, bioinformatique) ;
- des **UE de méthodologie et de communication** (démarche scientifique, lecture d'articles, rédaction, oral, projet, veille, anglais) ;
- des **UE de contexte** (droit de la santé, bioéthique, économie de la santé et de la recherche, psychologie de la santé).

Les matières FicheLab de la filière suivent les **matières exactes du questionnaire licence**, telles qu'elles sont proposées à l'utilisateur. Les chapitres sont construits à partir du modèle `data/gen_generale_modele.py` et de la bibliothèque `data/fixtures.py`.

### Contrainte propre à la filière : le contenu biologique sans matière « Biologie »

Le questionnaire de la licence ne comprend **aucune matière intitulée « Biologie »**. Le contenu biologique n'est donc pas perdu : il est **réparti dans les matières disponibles**, chaque fiche portant un intitulé biologique dans son titre tout en étant rattachée à une matière du questionnaire.

| Contenu biologique | Matière du questionnaire utilisée | Exemple de fiche |
|---|---|---|
| Bioinformatique, bases de données biologiques, séquençage, structures 3D | `Informatique` | *Chapitre IN4 · Bases de séquences : ADN, protéines et alignement* |
| Statistiques descriptives, tests, plans d'expérience, données « -omiques » | `Statistiques` | *Chapitre ST6 · Analyse de variance et comparaison de groupes cellulaires* |
| Calcul, fonctions, modèles de population, lecture critique des chiffres | `Maths / stats` | *Chapitre MS4 · Équations différentielles et modélisation des populations* |
| Démarche scientifique, protocoles, articles, rédaction, veille, rapport | `Méthodologie universitaire` | *Chapitre MU1 · Démarche scientifique et raisonnement expérimental en biologie* |
| Droit de la santé, bioéthique, déontologie, données de santé | `Droit` | *Chapitre DR2 · Bioéthique et droit du corps humain* |
| Économie de la santé, de la recherche, industries biotech, médicament | `Économie` | *Chapitre EC3 · Industries biotechnologiques et valorisation de la recherche* |
| Expression et argumentation appliquées aux textes biologiques | `Français` | *Chapitre LSPF4 · Rédaction de rapports de laboratoire en français* |
| Vocabulaire, lecture et publication scientifiques en anglais | `Anglais` | *Chapitre LSPAN5 · Anglais spécialisé : génétique, physiologie et publication* |
| Perception, apprentissage, comportements de santé, stress en contexte de soin | `Psychologie` | *Chapitre PSY4 · Psychologie de la santé et observance thérapeutique* |

**Règle d'or :** chaque information générée démarre « à vérifier » avec sa source officielle. Aucune matière n'a été inventée, aucune matière du questionnaire n'a été écartée.

---

## 2. Carte des chapitres par année et par matière

### 2.1 Année de L1 — les fondamentaux (17 fiches)

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Statistiques` | **ST1.** Statistiques descriptives des données biologiques · **ST2.** Probabilités et transmission génétique mendelienne |
| `Informatique` | **IN1.** Initiation à la bioinformatique : données et outils · **IN2.** Tableurs et traitement de données biologiques |
| `Méthodologie universitaire` | **MU1.** Démarche scientifique et raisonnement expérimental en biologie · **MU2.** Lecture critique d'un article scientifique de biologie · **MU3.** Recherche documentaire et sources fiables en sciences de la vie |
| `Droit` | **DR1.** Droit de la santé : organisation et principes généraux |
| `Économie` | **EC1.** Économie de la santé : offre, demande et financement |
| `Français` | **LSPF1.** Expression écrite et syntaxe du français scientifique · **LSPF2.** Analyse de texte et figures de style dans les écrits biologiques |
| `Anglais` | **LSPAN1.** Vocabulaire anglais de la biologie cellulaire et moléculaire · **LSPAN2.** Lecture d'articles scientifiques anglais en biologie |
| `Psychologie` | **PSY1.** Psychologie cognitive : perception, attention et mémoire · **PSY2.** Psychologie du développement et apprentissage des sciences |
| `Maths / stats` | **MS1.** Calcul numérique, unités et ordres de grandeur en biologie · **MS2.** Fonctions et modèles mathématiques du vivant |

### 2.2 Année de L2 — les matières de spécialisation (24 fiches)

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Statistiques` | **ST3.** Échantillonnage et estimation appliqués à la biologie · **ST4.** Tests statistiques et décision en biologie expérimentale · **ST5.** Corrélation et régression appliquées aux données biologiques · **ST6.** Analyse de variance et comparaison de groupes cellulaires |
| `Informatique` | **IN3.** Bases de données relationnelles pour la biologie · **IN4.** Bases de séquences : ADN, protéines et alignement · **IN5.** Programmation Python pour l'analyse biologique · **IN6.** Visualisation des données biologiques expérimentales |
| `Méthodologie universitaire` | **MU4.** Protocoles expérimentaux et traçabilité au laboratoire · **MU5.** Rédaction scientifique : plan, figures et références · **MU6.** Communication orale et présentation de posters biologiques · **MU7.** Conduite de projet et travail en équipe en licence SVT |
| `Droit` | **DR2.** Bioéthique et droit du corps humain · **DR3.** Déontologie et exercice des professions biologiques |
| `Économie` | **EC2.** Économie de la recherche publique et privée · **EC3.** Industries biotechnologiques et valorisation de la recherche |
| `Français` | **LSPF3.** Argumentation et rhétorique du texte biologique · **LSPF4.** Rédaction de rapports de laboratoire en français |
| `Anglais` | **LSPAN3.** Expression écrite en anglais : résumé et courriels de laboratoire · **LSPAN4.** Communication orale en anglais : présentation de résultats biologiques |
| `Psychologie` | **PSY3.** Psychologie sociale et comportements de santé · **PSY4.** Psychologie de la santé et observance thérapeutique |
| `Maths / stats` | **MS3.** Probabilités et statistiques descriptives pour la biologie · **MS4.** Équations différentielles et modélisation des populations |

### 2.3 Année de L3 — l'approfondissement et la sortie (19 fiches)

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Statistiques` | **ST7.** Plans d'expérience en biologie végétale et animale · **ST8.** Mesures, incertitudes et qualité des données biologiques · **ST9.** Statistiques multivariées et données omiques · **ST10.** Synthèse statistique et projet de données en sciences de la vie |
| `Informatique` | **IN7.** Traitement des données de séquençage à haut débit · **IN8.** Modélisation structurale et biologie moléculaire numérique · **IN9.** Automatisation et reproductibilité des analyses biologiques · **IN10.** Projet intégré de bioinformatique et de restitution |
| `Méthodologie universitaire` | **MU8.** Veille scientifique et bibliographie dynamique · **MU9.** Mémoire, stage et rapport de recherche en biologie · **MU10.** Intégrité scientifique et éthique de la recherche biologique |
| `Droit` | **DR4.** Responsabilité et sécurité des produits de santé · **DR5.** Données de santé, confidentialité et règlement général |
| `Économie` | **EC4.** Marché du médicament : prix, remboursement et innovation · **EC5.** Politiques de santé publique et évaluation des actions |
| `Français` | **LSPF5.** Style, correction et qualité de l'écrit universitaire en biologie |
| `Anglais` | **LSPAN5.** Anglais spécialisé : génétique, physiologie et publication |
| `Psychologie` | **PSY5.** Stress, émotion et décision en contexte de soin et de recherche |
| `Maths / stats` | **MS5.** Lecture critique des données chiffrées en sciences de la vie |

> **Répartition :** **17 fiches en L1 · 24 en L2 · 19 en L3** — soit **60 fiches** réparties sur **9 matières** (Statistiques, Informatique, Méthodologie universitaire, Droit, Économie, Français, Anglais, Psychologie, Maths / stats). Trois lots de 20 fiches couvrent l'intégralité du catalogue.

---

## 3. Méthode en 4 étapes

1. **Étape 1 — Cadrer.** Valider la carte des chapitres ci-dessus contre l'arrêté du 6 avril 2021, le BO spécial n° 7 du 17 février 2022 et les programmes diffusés par éduscol. Vérifier que le contenu biologique est bien réparti dans les seules matières du questionnaire et corriger tout chapitre manquant ou mal nommé.
2. **Étape 2 — Prototyper.** Copier `data/gen_generale_modele.py`, construire UNE fiche complète par matière pilote : 12 points de cours, 7 blocs colorés (intro, formule, grille, liste, étapes, attention, exemples), 3 schémas SVG intégrés, 9 questions corrigées (7 QCM + 2 rédaction).
3. **Étape 3 — Valider et décliner.** Exécuter `valider_et_ecrire()` jusqu'à l'affichage de `OK` sans erreur, puis décliner le même modèle à tous les chapitres de la matière. Contrôler chaque lot avec `fixtures.valider_fiche()`.
4. **Étape 4 — Auditer et livrer.** Produire `AUDIT-LICSVT.md` (compteurs, répartition matière/année, contrôle des blocs, doublons, CJK, verdict), puis transmettre les fichiers JSON au coordinateur pour injection globale.

---

## 4. Suivi des lots

| Lot | Générateur | Sortie JSON | Matières | Statut |
|---|---|---|---|---|
| A | `data/gen_licsvt_A.py` | `data/licsvt-mat-part-A.json` | Statistiques (10), Informatique (10) | ✅ généré (20) |
| B | `data/gen_licsvt_B.py` | `data/licsvt-mat-part-B.json` | Méthodologie universitaire (10), Droit (5), Économie (5) | ✅ généré (20) |
| C | `data/gen_licsvt_C.py` | `data/licsvt-mat-part-C.json` | Français (5), Anglais (5), Psychologie (5), Maths / stats (5) | ✅ généré (20) |

> **Module partagé :** `data/gen_licsvt_common.py` assemble les fiches à partir du modèle `data/gen_generale_modele.py` et de `data/fixtures.py`. La fabrique garantit `filieres=["lic-svt"]`, `annees` en `['L1']`/`['L2']`/`['L3']`, les matières exactes du questionnaire, 12 points, 9 questions (7 QCM + 2 texte), 7 blocs en ordre strict et 3 `diag()` par fiche.
>
> **Note d'organisation :** l'outil `subagent`/`task` n'étant pas exposé dans cet environnement, les trois lots ont été rédigés directement par le responsable de filière, en suivant strictement les consignes données aux agents spécialisés.

---

## 5. Sources officielles mobilisées

- **Arrêté du 6 avril 2021** relatif à la licence — JORF n° 0083 du 8 avril 2021, NOR MESR2012468A.
- **BO spécial n° 7 du 17 février 2022** — programmes des licences générales (mentions Sciences de la vie).
- **éduscol / Onisep / Campus France** — présentation du cursus de licence Sciences de la vie, volumes horaires et débouchés.
- **Code de la santé publique**, **Code civil**, **RGPD** — droit de la santé, bioéthique, déontologie, responsabilité, protection des données de santé.
- **SOURCES.md** du projet — chiffres Parcoursup 2026 (SIES, Note Flash n° 17, juillet 2026) : 100 640 vœux pour la licence Sciences de la vie.

---

**Déclinaison terminée : 60 fiches, 180 schémas SVG, 540 questions corrigées.** Audit [`AUDIT-LICSVT.md`](AUDIT-LICSVT.md) : conforme.
