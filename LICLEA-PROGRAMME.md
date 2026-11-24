# Licence LEA — carte des chapitres FicheLab

> **Filière :** `lic-lea` · **90 648 vœux Parcoursup 2026** (7ᵉ licence générale la plus demandée, source [`SOURCES.md`](SOURCES.md) §1).
> **Référentiel :** licence mention **Langues étrangères appliquées** — **arrêté du 6 avril 2021** (JORF n° 0083 du 8 avril 2021) · **BO spécial n° 7 du 17 février 2022** (programmes de licence) · **éduscol / ministère de l'Enseignement supérieur, de la Recherche et de l'Innovation** · RNCP 39173 · **CECRL** (Conseil de l'Europe).
> **Années :** `L1`, `L2`, `L3`. Une fiche = un chapitre, au format « prototype » (7 blocs + 3 schémas SVG, 12 points, 9 questions corrigées).
> **Matières :** les 9 matières exactes du questionnaire licence : `Droit`, `Économie`, `Psychologie`, `Statistiques`, `Méthodologie universitaire`, `Anglais`, `Informatique`, `Français`, `Maths / stats`.

---

## 1. Référentiel et principes directeurs

L'arrêté du 6 avril 2021 fixe le cadre national de la licence (180 ECTS, six semestres, 30 ECTS par semestre). La mention LEA est une formation pluridisciplinaire et professionnalisante : elle combine le français, au moins deux langues étrangères dont l'anglais, et des matières d'application (économie, droit, gestion, commerce international, communication). Le programme est précisé par le BO spécial n° 7 du 17 février 2022 et les ressources éduscol ; le niveau de langue est référencé au CECRL.

Les fiches FicheLab couvrent les **UE de langue (anglais, français)**, les **UE de professionnalisation (droit, économie, méthodologie)** et les **outils transversaux (informatique, statistiques, psychologie, maths / stats)**. La langue B (allemand, espagnol, italien, etc.), propre à chaque établissement, n'est pas dupliquée : le catalogue se concentre sur l'anglais, langue A obligatoire.

**Règle d'or :** chaque information générée démarre « à vérifier » avec sa source officielle. Les fiches sont construites à partir du modèle `data/gen_generale_modele.py` et de la bibliothèque `data/fixtures.py`, via la fabrique commune `data/gen_liclea_common.py`.

---

## 2. Carte des chapitres par année et par matière

### 2.1 Année de L1 — les fondamentaux

| Matière FicheLab | Chapitres visibles en L1 |
|---|---|
| `Anglais` | **AN1.** Grammaire : temps et structures · **AN2.** Vocabulaire commercial · **AN3.** Traduction anglais-français · **AN4.** Expression écrite · **AN6.** Compréhension de documents |
| `Français` | **PF1.** Expression écrite · **PF2.** Grammaire et accords · **PF3.** Styles et registres · **PF4.** Traduction français-anglais · **PF5.** Argumentation |
| `Droit` | **DR1.** Droit des affaires : l'entreprise · **DR2.** Contrat commercial |
| `Économie` | **EC1.** Microéconomie · **EC2.** Macroéconomie |
| `Méthodologie universitaire` | **MU1.** Recherche documentaire · **MU2.** Note de synthèse · **MU3.** Dissertation et plan |
| `Informatique` | **IN1.** Systèmes et réseaux · **IN2.** Outils bureautiques · **IN3.** Bases de données |
| `Statistiques` | **ST1.** Statistiques descriptives · **ST2.** Probabilités |
| `Psychologie` | **LPSY1.** Introduction · **LPSY2.** Développement et apprentissage |
| `Maths / stats` | **MS1.** Fonctions et dérivation · **MS2.** Algèbre linéaire |

### 2.2 Année de L2 — les matières d'application

| Matière FicheLab | Chapitres visibles en L2 |
|---|---|
| `Anglais` | **AN3.** Traduction · **AN4.** Expression écrite · **AN5.** Expression orale · **AN6.** Compréhension · **AN7.** Civilisation anglo-américaine · **AN8.** Anglais des affaires · **AN9.** Anglais juridique |
| `Français` | **PF3.** Styles et registres · **PF4.** Traduction · **PF5.** Argumentation · **PF6.** Synthèse · **PF7.** Rédaction professionnelle · **PF8.** Commentaire de texte |
| `Droit` | **DR2.** Contrat commercial · **DR3.** Droit européen · **DR4.** Droit international · **DR5.** Concurrence · **DR6.** Consommation · **DR7.** Droit social |
| `Économie` | **EC2.** Macroéconomie · **EC3.** Commerce international · **EC4.** Marché du travail · **EC5.** Croissance · **EC6.** Économie européenne |
| `Méthodologie universitaire` | **MU2.** Note de synthèse · **MU3.** Dissertation · **MU4.** Exposé et soutenance |
| `Informatique` | **IN3.** Bases de données · **IN4.** Sécurité numérique |
| `Statistiques` | **ST2.** Probabilités · **ST3.** Échantillonnage · **ST4.** Tests statistiques |
| `Psychologie` | **LPSY2.** Développement · **LPSY3.** Psychologie sociale · **LPSY4.** Psychologie cognitive |
| `Maths / stats` | **MS2.** Algèbre linéaire · **MS3.** Suites et intérêts · **MS4.** Optimisation |

### 2.3 Année de L3 — approfondissement et sortie

| Matière FicheLab | Chapitres visibles en L3 |
|---|---|
| `Anglais` | **AN9.** Anglais juridique · **AN10.** Communication internationale et traduction technique |
| `Français` | **PF8.** Commentaire de texte · **PF9.** Commentaire littéraire et image · **PF10.** Expression orale |
| `Droit` | **DR5.** Concurrence · **DR7.** Droit social · **DR8.** Propriété intellectuelle |
| `Économie` | **EC5.** Croissance · **EC6.** Économie européenne · **EC7.** Finance |
| `Méthodologie universitaire` | **MU5.** Dossier de recherche et mémoire de L3 |
| `Informatique` | **IN5.** Outils pour la traduction et la veille |
| `Statistiques` | **ST4.** Tests statistiques · **ST5.** Corrélation et régression |
| `Psychologie` | **LPSY4.** Psychologie cognitive · **LPSY5.** Psychologie interculturelle |
| `Maths / stats` | **MS4.** Optimisation · **MS5.** Mathématiques financières |

> **Répartition des déclarations d'année :** L1 26 · L2 38 · L3 19 (certains chapitres sont déclarés sur deux années, d'où un total de 83 déclarations pour 60 fiches).

### 2.4 Index complet par matière (60 fiches)

| Matière | Fiches | Préfixes |
|---|---:|---|
| `Anglais` | 10 | AN1.–AN10. |
| `Français` | 10 | PF1.–PF10. |
| `Droit` | 8 | DR1.–DR8. |
| `Économie` | 7 | EC1.–EC7. |
| `Méthodologie universitaire` | 5 | MU1.–MU5. |
| `Informatique` | 5 | IN1.–IN5. |
| `Statistiques` | 5 | ST1.–ST5. |
| `Psychologie` | 5 | LPSY1.–LPSY5. |
| `Maths / stats` | 5 | MS1.–MS5. |
| **Total** | **60** | **60 préfixes uniques** |

---

## 3. Méthode en 4 étapes

1. **Étape 1 — Cadrer.** Valider la carte ci-dessus contre l'arrêté du 6 avril 2021, le BO spécial n° 7 du 17 février 2022, les programmes diffusés par éduscol et la fiche RNCP 39173. Vérifier que les 9 matières du questionnaire sont couvertes et que la progression L1 → L2 → L3 est cohérente.
2. **Étape 2 — Prototyper.** Copier `data/gen_generale_modele.py`, construire UNE fiche complète par matière pilote : 12 points de cours, 7 blocs colorés (intro, formule, grille, liste, étapes, attention, exemples), 3 schémas SVG intégrés, 9 questions corrigées (7 QCM + 2 rédaction).
3. **Étape 3 — Valider et décliner.** Exécuter `valider_et_ecrire()` jusqu'à l'affichage de `OK` sans erreur, puis décliner le même modèle à tous les chapitres. Contrôler chaque lot avec `fixtures.valider_fiche()` et vérifier les doublons de titres inter-lots et avec le catalogue existant.
4. **Étape 4 — Auditer et livrer.** Produire `AUDIT-LICLEA.md` (compteurs, répartition matière/année, contrôle des blocs, doublons, CJK, verdict), puis transmettre les fichiers JSON au coordinateur pour injection globale.

---

## 4. Suivi des lots

| Lot | Générateur | Sortie JSON | Matières | Statut |
|---|---|---|---|---|
| A | `data/gen_liclea_A.py` | `data/liclea-mat-part-A.json` | Anglais (10), Français (10) | ✅ généré (20) |
| B | `data/gen_liclea_B.py` | `data/liclea-mat-part-B.json` | Droit (8), Économie (7), Méthodologie universitaire (5) | ✅ généré (20) |
| C | `data/gen_liclea_C.py` | `data/liclea-mat-part-C.json` | Informatique (5), Statistiques (5), Psychologie (5), Maths / stats (5) | ✅ généré (20) |

> La fabrique partagée `data/gen_liclea_common.py` applique strictement `filieres = ["lic-lea"]`, `annees` dans `L1`/`L2`/`L3`, 12 points, 9 questions (≥ 6 QCM + ≥ 2 texte), 7 blocs en ordre strict et 3 `diag()`. Les titres sont préfixés et suffixés `(LEA)` pour garantir leur unicité dans le catalogue global.

---

## 5. Sources officielles mobilisées

- **Arrêté du 6 avril 2021** relatif à la licence — JORF n° 0083 du 8 avril 2021, mention Langues étrangères appliquées.
- **BO spécial n° 7 du 17 février 2022** — programmes des licences générales.
- **éduscol / ministère de l'Enseignement supérieur, de la Recherche et de l'Innovation** — fiches cursus et ressources pédagogiques.
- **RNCP 39173** — licence Langues étrangères appliquées (niveau 6, 180 ECTS).
- **CECRL**, Conseil de l'Europe — niveaux B1 à C1 pour les compétences en langues.
- **Code civil, Code de commerce, Code du travail, Code de la consommation, TUE et TFUE** — sources du droit appliqué.
- **INSEE, OCDE, Banque centrale européenne** — statistiques et économie.
- **CNIL / RGPD, ANSSI** — sécurité et protection des données.
- **ISO 690** — citation bibliographique ; **SOURCES.md** du projet — chiffres Parcoursup 2026 (SIES, Note Flash n° 17, juillet 2026).
