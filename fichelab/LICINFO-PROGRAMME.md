# Licence Informatique — carte des chapitres FicheLab

> **Filière :** `lic-info` · **42 867 vœux Parcoursup 2026** (licence générale la plus demandée après maths, source [`SOURCES.md`](SOURCES.md) §1, SIES / Note Flash n° 17, juillet 2026).
> **Référentiel :** **arrêté du 6 avril 2021** relatif aux licences générales (mention informatique) · **BO spécial n° 7 du 17 février 2022** (programmes de licence) · **éduscol** / ministère de l'Enseignement supérieur, de la Recherche et de l'Innovation.
> **Années :** `L1`, `L2`, `L3`. Une fiche = un chapitre, au format « prototype » (7 blocs colorés, 3 schémas SVG, 12 points, 9 questions corrigées).
> **Périmètre :** 60 fiches réparties en 3 lots de 20, sur 9 matières du questionnaire licence.

---

## 1. Référentiel et principes directeurs

L'arrêté du 6 avril 2021 et le BO spécial n° 7 du 17 février 2022 fixent le cadre national des licences générales : **180 ECTS, six semestres**, organisés en unités d'enseignement. La mention informatique couvre de L1 à L3 les fondamentaux (algorithmique, programmation, mathématiques), les systèmes et réseaux, le génie logiciel, les données, puis l'approfondissement (architecture parallèle, intelligence artificielle, sécurité) et le projet personnel.

Les matières FicheLab de la filière suivent **exactement la liste du questionnaire licence** : `Droit`, `Économie`, `Psychologie`, `Statistiques`, `Méthodologie universitaire`, `Anglais`, `Informatique`, `Français`, `Maths / stats`. Aucune matière hors liste n'a été introduite. Les neuf matières sont toutes représentées dans les trois lots.

**Règle d'or :** chaque fiche générée démarre « à vérifier » avec sa source officielle explicite. Les fiches sont construites à partir du modèle `data/gen_generale_modele.py` et de la bibliothèque `data/fixtures.py`, via le moteur partagé `data/gen_licinfo_common.py`.

---

## 2. Carte des chapitres par année et par matière

### 2.1 Année de L1 — les fondamentaux

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Informatique` | **IN1.** Algorithmique fondamentale et spécification · **IN2.** Programmation en Python : bases et idiomes · **IN3.** Structures de données linéaires et arborescentes (L1/L2) · **IN5.** Bases de données relationnelles et langage SQL (L1/L2) · **IN9.** Programmation orientée objet et modélisation UML (L1/L2) |
| `Maths / stats` | **MS1.** Logique propositionnelle et algèbre de Boole · **MS2.** Algèbre linéaire et espaces vectoriels · **MS3.** Calcul matriciel et systèmes linéaires (L1/L2) · **MS4.** Suites, récurrences et récursivité · **MS5.** Probabilités discrètes et continues (L1/L2) |
| `Statistiques` | **ST1.** Statistiques descriptives et exploration de données · **ST2.** Probabilités et lois usuelles pour le numérique (L1/L2) |
| `Méthodologie universitaire` | **MU1.** Investigation documentaire et évaluation des sources · **MU2.** Raisonnement logique et preuves en informatique (L1/L2) · **MU3.** Rédaction d'un rapport technique · **MU8.** Gestion du temps et planification des révisions |
| `Français` | **PF1.** Expression écrite et structures de la phrase · **PF2.** Analyse de texte et argumentation écrite |
| `Anglais` | **AN1.** Vocabulaire informatique anglais : concepts clés · **AN2.** Lecture de documentation technique anglaise (L1/L2) |
| `Psychologie` | **PSY1.** Introduction à la psychologie scientifique · **PSY2.** Psychologie cognitive : attention et mémoire de travail (L1/L2) |
| `Économie` | **EC1.** Offre, demande et mécanisme des prix · **EC2.** Structures de marché et concurrence imparfaite (L1/L2) |

### 2.2 Année de L2 — les matières de spécialisation

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Informatique` | **IN3.** Structures de données (L1/L2) · **IN4.** Complexité des algorithmes et notations asymptotiques · **IN5.** Bases de données et SQL (L1/L2) · **IN6.** Réseaux informatiques et modèle TCP/IP · **IN7.** Systèmes d'exploitation et gestion des ressources · **IN8.** Génie logiciel, tests et cycle de développement · **IN9.** Programmation orientée objet et UML (L1/L2) · **IN12.** Sécurité informatique et cryptographie appliquée (L2/L3) |
| `Maths / stats` | **MS3.** Calcul matriciel (L1/L2) · **MS5.** Probabilités (L1/L2) · **MS6.** Statistiques descriptives et analyse de données · **MS7.** Théorie des graphes et algorithmes associés |
| `Statistiques` | **ST2.** Probabilités et lois usuelles (L1/L2) · **ST3.** Échantillonnage et estimation paramétrique · **ST4.** Tests d'hypothèses et prise de décision (L2/L3) |
| `Méthodologie universitaire` | **MU2.** Raisonnement logique (L1/L2) · **MU4.** Soutenance d'un projet informatique · **MU5.** Conduite de projet agile en licence · **MU6.** Veille technologique et veille scientifique (L2/L3) · **MU7.** Travail en équipe et revue de code (L2/L3) |
| `Droit` | **DR1.** Droit de l'informatique et société numérique · **DR2.** RGPD et protection des données personnelles · **DR3.** Propriété intellectuelle et logiciels libres (L2/L3) · **DR4.** Contrats informatiques et licences d'utilisation |
| `Français` | **PF3.** Rhétorique et registres de discours · **PF4.** Synthèse de documents et note de synthèse (L2/L3) |
| `Anglais` | **AN2.** Lecture de documentation technique (L1/L2) · **AN3.** Expression écrite technique en anglais · **AN4.** Présentation orale d'un projet en anglais (L2/L3) |
| `Psychologie` | **PSY2.** Attention et mémoire de travail (L1/L2) · **PSY3.** Psychologie du développement et apprentissage · **PSY4.** Psychologie sociale et interactions |
| `Économie` | **EC2.** Structures de marché (L1/L2) · **EC3.** Comptes nationaux et mesure de l'activité · **EC4.** Inflation, monnaie et politiques économiques (L2/L3) |

### 2.3 Année de L3 — l'approfondissement et la sortie

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Informatique` | **IN10.** Calcul parallèle et architectures multicœurs · **IN11.** Intelligence artificielle et apprentissage automatique · **IN12.** Sécurité informatique et cryptographie appliquée (L2/L3) |
| `Maths / stats` | **MS8.** Optimisation combinatoire et programmation linéaire |
| `Statistiques` | **ST4.** Tests d'hypothèses et prise de décision (L2/L3) |
| `Méthodologie universitaire` | **MU6.** Veille technologique (L2/L3) · **MU7.** Travail en équipe et revue de code (L2/L3) · **MU9.** Répétition espacée et testing effect · **MU10.** Préparation aux examens et aux oraux de licence |
| `Droit` | **DR3.** Propriété intellectuelle et logiciels libres (L2/L3) · **DR5.** Cyberdroit : infractions et fraude numérique · **DR6.** Responsabilité civile, pénale et contractuelle du numérique |
| `Français` | **PF4.** Synthèse de documents (L2/L3) · **PF5.** Communication écrite professionnelle en informatique |
| `Anglais` | **AN4.** Présentation orale d'un projet (L2/L3) · **AN5.** Anglais pour la recherche en informatique |
| `Psychologie` | **PSY5.** Psychologie du travail et ergonomie cognitive |
| `Économie` | **EC4.** Inflation et politiques économiques (L2/L3) · **EC5.** Économie du numérique et transformation digitale |

> **Répartition :** 24 déclarations L1 · 35 déclarations L2 · 19 déclarations L3, soit **78 déclarations annuelles pour 60 fiches** : 18 chapitres à cheval sur deux années sont comptés dans les deux colonnes.

---

## 3. Méthode de rédaction (4 étapes)

1. **Étape 1 — Cadrer.** Valider la carte des chapitres ci-dessus contre l'arrêté du 6 avril 2021, le BO spécial n° 7 du 17 février 2022 et les programmes diffusés par éduscol. Vérifier les neuf matières exactes du questionnaire licence et la cohérence des années L1/L2/L3.
2. **Étape 2 — Prototyper.** Copier `data/gen_generale_modele.py`, construire UNE fiche complète par matière pilote : 12 points de cours, 7 blocs colorés (intro, formule, grille, liste, etapes, attention, exemples), 3 schémas SVG intégrés, 9 questions corrigées (7 QCM + 2 rédaction).
3. **Étape 3 — Valider et décliner.** Exécuter `valider_et_ecrire()` jusqu'à l'affichage de `OK` sans erreur, puis décliner le même modèle à tous les chapitres via `data/gen_licinfo_common.py`. Contrôler chaque lot avec `fixtures.valider_fiche()` et le contrôle croisé des titres, préfixes, matières, années et schémas.
4. **Étape 4 — Auditer et livrer.** Produire [`AUDIT-LICINFO.md`](AUDIT-LICINFO.md) (compteurs, répartition matière/année, contrôle des blocs, doublons inter-lots et inter-filières, CJK, verdict), puis transmettre les fichiers JSON au coordinateur pour injection globale.

Toute fiche est livrée avec le statut **à vérifier** : la source est explicite, le contenu reste à relecture pédagogique avant utilisation en exercice.

---

## 4. Suivi des lots

| Lot | Générateur | Sortie JSON | Matières | Fiches |
|---|---|---|---|---:|
| A | `data/gen_licinfo_A.py` | `data/licinfo-mat-part-A.json` | Informatique (IN1.–IN12.), Maths / stats (MS1.–MS8.) | 20 |
| B | `data/gen_licinfo_B.py` | `data/licinfo-mat-part-B.json` | Méthodologie universitaire (MU1.–MU10.), Droit (DR1.–DR6.), Statistiques (ST1.–ST4.) | 20 |
| C | `data/gen_licinfo_C.py` | `data/licinfo-mat-part-C.json` | Français (PF1.–PF5.), Anglais (AN1.–AN5.), Psychologie (PSY1.–PSY5.), Économie (EC1.–EC5.) | 20 |

> **Architecture :** le moteur de mise en forme est factorisé dans `data/gen_licinfo_common.py` (dérivation des 12 points, des 9 questions, des 7 blocs et des 3 schémas à partir de données pédagogiques compactes). Les trois générateurs n'utilisent que `fixtures.py` : `fiche`, `qcm`, `qt`, `diag`, `bloc`, `svg_grille`, `svg_flux`, `svg_etapes`, `svg_compare`, `valider_et_ecrire`. Aucun fichier interdit (`index.html`, `inject_app.py`, `audit_filieres.py`) n'a été modifié.

**Résultats de génération :**

```
OK licinfo-mat-part-A.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK licinfo-mat-part-B.json : 20 fiches, 240 points, 180 questions, 60 SVG
OK licinfo-mat-part-C.json : 20 fiches, 240 points, 180 questions, 60 SVG
```

**Déclinaison terminée** : 60 fiches, 720 points de cours, 540 questions corrigées, 180 schémas SVG. Audit [`AUDIT-LICINFO.md`](AUDIT-LICINFO.md) : **CONFORME**.

---

## 5. Sources officielles mobilisées

- **Arrêté du 6 avril 2021** relatif aux licences générales (mention informatique) · **BO spécial n° 7 du 17 février 2022** — programmes des licences générales.
- **éduscol / Onisep / Campus France** — présentation des cursus d'informatique et débouchés.
- **INRIA, RFC, OWASP** — algorithmique, langages, réseaux, génie logiciel et sécurité des systèmes.
- **Légifrance** (Code civil, Code pénal), **RGPD** (règlement UE 2016/679), **CNIL** — droit du numérique, protection des données, cyberdroit et responsabilité.
- **ISO 690** — citation bibliographique · **CECRL**, Conseil de l'Europe — niveaux d'anglais.
- **APA, Publication Manual** — rédaction scientifique en psychologie · **Cepeda et al. (2006)**, **Roediger et Karpicke (2006)** — répétition espacée et *testing effect*.
- **INSEE** — comptes nationaux, indice des prix · **Banque de France** — politique monétaire et taux directeurs.
- **SOURCES.md** du projet — chiffres Parcoursup 2026 (SIES, Note Flash n° 17, juillet 2026).
