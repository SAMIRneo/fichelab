# Licence Économie et gestion — carte des chapitres FicheLab

> **Filière :** `lic-eco` · **152 897 vœux Parcoursup 2026** (4ᵉ licence générale la plus demandée, derrière Droit, STAPS et Psychologie — source [`SOURCES.md`](SOURCES.md) §1, SIES *Note Flash* n° 17, juillet 2026).
> **Référentiel :** arrêté du **6 avril 2021** relatif à la licence (cadre national des mentions, dont *Économie* et *Économie et gestion*, JORF n° 0083 du 8 avril 2021) · arrêté du **22 janvier 2014** fixant la nomenclature des mentions du diplôme national de licence · **BO spécial n° 7 du 17 février 2022** (programmes de licence) · **éduscol / DGESIP**, référentiels de compétences des mentions Économie, Gestion et Économie et gestion (fiches RNCP 24424, 24425, 24426) · INSEE, Banque de France, CNIL.
> **Années :** `L1`, `L2`, `L3`. Une fiche = un chapitre, au format « prototype » (12 points, 9 questions corrigées, 7 blocs, 3 schémas SVG).

---

## 1. Référentiel et principes directeurs

La licence d'économie et gestion est un diplôme national de **180 ECTS, six semestres**. Les référentiels DGESIP/RNCP de la mention Économie attendent la mobilisation des grands domaines : **microéconomie, macroéconomie, monnaie et finance, politique économique, histoire et pensée économiques, économie internationale**, complétés par les **méthodes quantitatives**, les **usages numériques** et l'**expression écrite et orale**. La mention Économie et gestion y ajoute comptabilité, finance, marketing, stratégie, GRH et systèmes d'information.

Les matières FicheLab de la filière reprenent **exactement les intitulés du questionnaire** : `Économie`, `Statistiques`, `Droit`, `Informatique`, `Méthodologie universitaire`, `Français`, `Anglais`, `Psychologie`, `Maths / stats`.

**Règle d'or :** chaque information générée démarre « à vérifier » avec sa source officielle. Les fiches sont construites à partir du modèle `data/gen_generale_modele.py` et de la bibliothèque `data/fixtures.py`.

---

## 2. Carte des chapitres par année et par matière

### 2.1 Lot A — tronc commun économique et quantitatif (20 fiches)

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Économie` (10) | **EC1.** Offre, demande et équilibre de marché (L1) · **EC2.** Élasticités et décisions de prix (L1) · **EC3.** Concurrence et structures de marché (L1) · **EC4.** Défaillances de marché et intervention publique (L1) · **EC5.** PIB et comptes nationaux (L1) · **EC6.** Croissance et productivité (L2) · **EC7.** Chômage, emploi et salaires (L2) · **EC8.** Inflation et politique monétaire (L2) · **EC9.** Finances publiques et politique budgétaire (L3) · **EC10.** Commerce international : théories et échanges (L3) |
| `Statistiques` (10) | **ST1.** Statistiques descriptives : position et dispersion (L1) · **ST2.** Probabilités : notions fondamentales (L1) · **ST3.** Tests statistiques : principes et décision (L2) · **ST4.** Corrélation et régression linéaire (L2) · **ST5.** Séries temporelles : tendance et saisonnalité (L2) · **ST6.** Indices et comparaisons dans le temps (L2) · **ST7.** Échantillonnage et représentativité (L1) · **ST8.** Incertitudes et intervalles de confiance (L2) · **ST9.** Lecture critique de tableaux et graphiques (L3) · **ST10.** Logiciels statistiques et reproductibilité (L3) |

### 2.2 Lot B — droit, outils numériques et méthodologie (20 fiches)

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Droit` (7) | **DR1.** Le contrat : formation et validité (L1) · **DR2.** Exécution et rupture du contrat (L1) · **DR3.** Droit des affaires : commerçant et entreprise (L2) · **DR4.** Les sociétés commerciales (L2) · **DR5.** Concurrence : ententes et abus de position dominante (L2) · **DR6.** Droit social : contrat de travail et relations collectives (L3) · **DR7.** Responsabilité civile dans les affaires (L3) |
| `Informatique` (7) | **IN1.** Outils bureautiques et traitement de texte (L1) · **IN2.** Tableurs et fonctions essentielles (L1) · **IN3.** Bases de données relationnelles et SQL (L2) · **IN4.** Structuration et qualité des données (L2) · **IN5.** Tableaux de bord et visualisation (L2) · **IN6.** RGPD et données personnelles (L3) · **IN7.** Outils collaboratifs et sécurité numérique (L3) |
| `Méthodologie universitaire` (6) | **MU1.** Recherche documentaire universitaire (L1) · **MU2.** Lire et analyser un texte académique (L1) · **MU3.** La note de synthèse (L2) · **MU4.** Dissertation et argumentation (L2) · **MU5.** Le mémoire de licence (L3) · **MU6.** L'oral : exposé et soutenance (L3) |

### 2.3 Lot C — transversales (20 fiches)

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Français` (5) | **PF1.** Expression écrite : syntaxe et ponctuation (L1) · **PF2.** Analyse de texte et commentaire (L1) · **PF3.** Argumentation et figures de style (L2) · **PF4.** Rhétorique et style académique (L2) · **PF5.** Réécriture et reformulation (L3) |
| `Anglais` (5) | **AN1.** Vocabulaire économique et général (L1) · **AN2.** Compréhension de documents anglais (L1) · **AN3.** Expression écrite : courriel et compte rendu (L2) · **AN4.** Anglais des affaires et du commerce (L2) · **AN5.** Communication orale en anglais (L3) |
| `Psychologie` (5) | **PSY1.** Introduction à la psychologie (L1) · **PSY2.** Psychologie du développement (L1) · **PSY3.** Psychologie sociale (L2) · **PSY4.** Psychologie cognitive (L2) · **PSY5.** Psychologie du travail et des organisations (L3) |
| `Maths / stats` (5) | **MS1.** Calcul littéral et équations (L1) · **MS2.** Fonctions et variations (L1) · **MS3.** Probabilités et statistiques appliquées (L2) · **MS4.** Optimisation linéaire (L2) · **MS5.** Mathématiques financières : intérêts et actualisation (L3) |

> **Répartition :** 20 fiches par lot, soit **60 fiches**, 9 matières, 3 années. Chaque préfixe (`EC.`, `ST.`, `DR.`, `IN.`, `MU.`, `PF.`, `AN.`, `PSY.`, `MS.`) est propre à une matière et à un lot : aucun doublon de titre attendu.

---

## 3. Méthode en 4 étapes

1. **Étape 1 — Cadrer.** Valider la carte des chapitres contre l'arrêté du 6 avril 2021, l'arrêté du 22 janvier 2014 (nomenclature), le BO spécial n° 7 du 17 février 2022, les référentiels DGESIP et les ressources éduscol/INSEE/Banque de France. Corriger tout chapitre manquant ou mal nommé.
2. **Étape 2 — Prototyper.** Copier `data/gen_generale_modele.py`, construire UNE fiche complète par matière pilote : 12 points de cours, 7 blocs colorés (intro, formule, grille, liste, étapes, attention, exemples), 3 schémas SVG intégrés, 9 questions corrigées (7 QCM + 2 rédaction).
3. **Étape 3 — Valider et décliner.** Exécuter `valider_et_ecrire()` jusqu'à l'affichage de `OK` sans erreur, puis décliner le même modèle à tous les chapitres. Contrôler chaque lot avec `fixtures.valider_fiche()` et vérifier l'unicité des titres.
4. **Étape 4 — Auditer et livrer.** Produire `AUDIT-LICECO.md` (compteurs, répartition matière/année, contrôle des blocs, doublons, CJK, verdict), puis transmettre les trois JSON au coordinateur pour injection globale.

---

## 4. Suivi des lots

| Lot | Générateur | Sortie JSON | Matières | Statut |
|---|---|---|---|---|
| A | `data/gen_liceco_A.py` | `data/liceco-mat-part-A.json` | Économie (10), Statistiques (10) | ✅ généré (20) |
| B | `data/gen_liceco_B.py` | `data/liceco-mat-part-B.json` | Droit (7), Informatique (7), Méthodologie universitaire (6) | ✅ généré (20) |
| C | `data/gen_liceco_C.py` | `data/liceco-mat-part-C.json` | Français (5), Anglais (5), Psychologie (5), Maths / stats (5) | ✅ généré (20) |

> **Note d'organisation :** l'outil de sous-délégation n'étant pas exposé dans cet environnement, les trois lots ont été rédigés directement par le responsable de filière, en appliquant strictement les consignes données aux agents spécialisés. Aucun fichier hors périmètre (`index.html`, `inject_app.py`, `audit_filieres.py`) n'a été modifié.

---

## 5. Sources officielles mobilisées

- **Arrêté du 6 avril 2021** relatif à la licence — JORF n° 0083 du 8 avril 2021 (mentions Économie, Économie et gestion, Gestion).
- **Arrêté du 22 janvier 2014** fixant la nomenclature des mentions du diplôme national de licence (JORF du 23 janvier 2014), modifié en 2024.
- **BO spécial n° 7 du 17 février 2022** — programmes des licences générales.
- **DGESIP / France Compétences** — référentiels d'activités, de compétences et d'évaluation des mentions Économie (RNCP 24424), Gestion (24425), Économie et gestion (24426) : micro/macroéconomie, monnaie et finance, politique économique, économie internationale, méthodes quantitatives, numérique, expression.
- **Code civil, Code de commerce, Code du travail** — droit des contrats, des affaires, de la concurrence et du travail.
- **RGPD** (règlement UE 2016/679) et **loi Informatique et Libertés du 6 janvier 1978** — protection des données personnelles.
- **INSEE** (comptes nationaux, indices, nombre d'heures), **Banque de France** (politique monétaire, taux), **OCDE / OMC** (commerce international), **CADRCE / CECRL** (anglais), **éduscol** (méthodologie, expression).
- **SOURCES.md** du projet — chiffres Parcoursup 2026 (SIES, *Note Flash* n° 17, juillet 2026).
