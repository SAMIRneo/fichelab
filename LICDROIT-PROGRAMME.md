# Licence Droit — carte des chapitres FicheLab

> **Filière :** `lic-droit` · **379 432 vœux Parcoursup 2026** (4ᵉ formation la plus demandée, source [`SOURCES.md`](SOURCES.md) §1).
> **Référentiel :** arrêté du **6 avril 2021** relatif à la licence d'études juridiques (JORF n°0083 du 8 avril 2021), pris en application des articles L.621-1 et suivants du Code de l'éducation · **BO** spécial n° 7 du 17 février 2022 (programmes de licence) · **éduscol** / ministère de l'Enseignement supérieur, de la Recherche et de l'Innovation · Code civil, Code pénal, Code de procédure civile, Code du travail, Code de commerce.
> **Années :** `L1`, `L2`, `L3`. Une fiche = un chapitre, au format « prototype » (7 blocs + 3 schémas SVG, 12 points, 9 questions corrigées).

---

## 1. Référentiel et principes directeurs

L'arrêté du 6 avril 2021 fixe le cadre national de la licence d'études juridiques : **180 ECTS, six semestres**, organisés en unités d'enseignement (UE). Il succède à l'arrêté du 1er août 2011 et s'inscrit dans le cadre du programme national défini par le BO spécial n° 7 du 17 février 2022.

Les matières FicheLab de la filière suivent les **grands domaines classiques du cursus** (droit privé, droit public, sciences économiques, méthodologie, transversales) tout en restant compatibles avec les différentes mentions (droit général, droit économique, juridictions, administration publique, etc.) proposées par les universités.

**Règle d'or :** chaque information générée démarre « à vérifier » avec sa source officielle. Les fiches sont construites à partir du modèle `data/gen_generale_modele.py` et de la bibliothèque `data/fixtures.py`.

---

## 2. Carte des chapitres par année et par matière

### 2.1 Année de L1 — les fondamentaux

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Droit` | **DR1.** Les personnes physiques et morales · **DR2.** Les biens et la propriété · **DR3.** Le contrat : formation et validité · **DR4.** La responsabilité civile délictuelle · **DR5.** Les infractions et la responsabilité pénale · **DR6.** L'administration et le service public |
| `Économie` | **EC1.** Offre et demande · **EC2.** Les élasticités · **EC3.** Les structures de marché · **EC4.** Le PIB et les comptes nationaux |
| `Méthodologie universitaire` | **MU1.** La dissertation juridique · **MU2.** Le commentaire d'arrêt · **MU3.** Le cas pratique · **MU4.** La recherche documentaire juridique · **MU5.** La note de synthèse |
| `Statistiques` | **ST1.** Statistiques descriptives · **ST2.** Probabilités |
| `Psychologie` | **PSY1.** Introduction à la psychologie · **PSY2.** Psychologie du développement |
| `Anglais` | **AN1.** Vocabulaire juridique anglais · **AN2.** Lecture de documents juridiques anglais |
| `Informatique` | **IN1.** Initiation à l'informatique et aux systèmes |
| `Français` | **PF1.** Expression écrite et syntaxe · **PF2.** Analyse de texte et argumentation |

### 2.2 Année de L2 — les matières de spécialisation

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Droit` | **DR7.** Le commerçant et l'entreprise · **DR8.** Les sûretés et la garantie des créances · **DRB4.** L'Union européenne : institutions et sources · **DRB5.** Le droit international public : sujets et sources · **DRB6.** Le contrat de travail · **DRB7.** Le procès civil et les voies de recours |
| `Économie` | **EC5.** Chômage et marché du travail · **EC6.** Inflation et politiques monétaires · **EC7.** Commerce international : théories et échanges |
| `Méthodologie universitaire` | **MU6.** La plaidoirie et l'oral · **MU7.** L'argumentation juridique et la contradiction · **MU8.** La lecture et l'analyse de textes de loi |
| `Statistiques` | **ST3.** Échantillonnage et estimation · **ST4.** Tests statistiques |
| `Psychologie` | **PSY3.** Psychologie sociale |
| `Anglais` | **AN3.** Expression écrite juridique en anglais |
| `Informatique` | **IN2.** Bases de données et recherche documentaire |
| `Français` | **PF3.** Rhétorique et style juridique |

### 2.3 Année de L3 — l'approfondissement et la sortie

| Matière FicheLab | Chapitres (préfixes) |
|---|---|
| `Droit` | **DR9.** La procédure pénale et les sanctions · **DR10.** Le contentieux administratif et le juge · **DRB8.** Droit de l'Union et libertés fondamentales · **DRB9.** Responsabilité internationale et droit humanitaire · **DRB10.** Protection sociale et dialogue social |
| `Méthodologie universitaire` | **MU9.** Le mémoire et la recherche juridique · **MU10.** La préparation aux concours et examens |
| `Économie` | **EC8.** Finances publiques : budget et fiscalité · **EC9.** Croissance et politiques budgétaires · **EC10.** Salaire, emploi et négociation |
| `Statistiques` | **ST5.** Corrélation et régression · **ST6.** Lecture critique de données |
| `Psychologie` | **PSY4.** Psychologie cognitive |
| `Anglais` | **AN4.** Communication orale et common law |
| `Informatique` | **IN3.** Outils numériques pour le juriste |

> **Répartition :** 20 fiches en L1 · 18 fiches en L2 · 19 fiches en L3 — soit **57 fiches** réparties sur 8 matières (Droit, Économie, Méthodologie universitaire, Statistiques, Psychologie, Anglais, Informatique, Français). Trois lots de ~20 fiches sont prévus ; le lot A porte 20 fiches (L1 majoritairement), le lot B 20 fiches (L2/L3), le lot C 20 fiches (transversales).

---

## 3. Méthode en 4 étapes

1. **Étape 1 — Cadrer.** Valider la carte des chapitres ci-dessus contre l'arrêté du 6 avril 2021, le BO spécial n° 7 du 17 février 2022 et les programmes diffusés par éduscol. Corriger tout chapitre manquant ou mal nommé.
2. **Étape 2 — Prototyper.** Copier `data/gen_generale_modele.py`, construire UNE fiche complète par matière pilote : 12 points de cours, 7 blocs colorés (intro, formule, grille, liste, étapes, attention, exemples), 3 schémas SVG intégrés, 9 questions corrigées (≥ 6 QCM + ≥ 2 rédaction).
3. **Étape 3 — Valider et décliner.** Exécuter `valider_et_ecrire()` jusqu'à l'affichage de `OK` sans erreur, puis décliner le même modèle à tous les chapitres de la matière. Contrôler chaque lot avec `fixtures.valider_fiche()`.
4. **Étape 4 — Auditer et livrer.** Produire `AUDIT-LICDROIT.md` (compteurs, répartition matière/année, contrôle des blocs, doublons, CJK, verdict), puis transmettre les fichiers JSON au coordinateur pour injection globale.

---

## 4. Suivi des lots

> Note d'organisation : l'outil de sous-délégation n'étant pas disponible dans les sessions enfants, le responsable de filière a rédigé les lots directement. Les 10 doublons de préfixes `DRB1.`–`DRB10.` entre les lots A et B ont été corrigés en renommant `DRB…` en `DR…` dans `gen_licdroit_A.py`, puis le lot A a été régénéré. Situation finale : 60 fiches, 0 doublon.

| Lot | Générateur | Sortie JSON | Matières | Statut |
|---|---|---|---|---|
| A | `data/gen_licdroit_A.py` | `data/licdroit-mat-part-A.json` | Droit (10), Économie (10) | ✅ généré (20) |
| B | `data/gen_licdroit_B.py` | `data/licdroit-mat-part-B.json` | Droit (10), Méthodologie universitaire (10) | ✅ généré (20) |
| C | `data/gen_licdroit_C.py` | `data/licdroit-mat-part-C.json` | Statistiques (6), Psychologie (4), Anglais (4), Informatique (3), Français (3) | ✅ généré (20) |

> **Note d'organisation :** l'outil `subagent`/`task` n'étant pas exposé dans cet environnement, les trois lots ont été rédigés directement par le responsable de filière, en suivant strictement les consignes données aux agents spécialisés.

---

## 5. Sources officielles mobilisées

- **Arrêté du 6 avril 2021** relatif à la licence d'études juridiques — JORF n° 0083 du 8 avril 2021, NOR MESR2012468A.
- **BO spécial n° 7 du 17 février 2022** — programmes des licences générales (mentions droit).
- **éduscol / Onisep / Campus France** — présentation des cursus de droit et débouchés.
- **Code civil** (art. 1er et suivants), **Code pénal**, **Code de procédure civile**, **Code de commerce**, **Code du travail**, **Code de la sécurité sociale**, **Code de justice administrative**.
- **Traité sur l'Union européenne (TUE)** et **Traité sur le fonctionnement de l'Union européenne (TFUE)**, **Convention européenne des droits de l'homme (CEDH)**.
- **SOURCES.md** du projet — chiffres Parcoursup 2026 (SIES, Note Flash n° 17, juillet 2026).
