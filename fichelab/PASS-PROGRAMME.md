# Licence PASS (Parcours Accès Santé Spécifique) — carte des chapitres FicheLab

> Référentiel : **arrêté du 17 mars 2021** modifié relatif aux études de santé (L.631-1 et suivants du Code de l'éducation), programme de l'année universitaire de PASS · BO du 25 mars 2021 · ONDPS / ministère de l'Enseignement supérieur.
> Source : [`SOURCES.md`](SOURCES.md) §1 — **836 177 vœux Parcoursup 2026**, formation la plus demandée.
> Identifiant : `pass`. Année : `PASS1` (année unique, prolongation possible en L.AS).

---

## 1. Sciences fondamentales (UE scientifiques)

| Matière FicheLab | Chapitres |
|---|---|
| `Anatomie` | Organisation générale du corps humain · Appareil locomoteur · Système nerveux · Appareil cardio-vasculaire · Appareil respiratoire · Appareil digestif · Appareil urinaire · Système endocrinien · Organes des sens · Embryologie et anatomie topographique |
| `Physiologie` | Homéostasie et régulation · Physiologie cellulaire et transport membranaire · Système nerveux et perception · Muscle et contraction · Cœur et circulation · Respiration et échanges gazeux · Digestion et absorption · Rein et équilibre hydro-électrolytique · Endocrinologie · Immunologie et inflammation |
| `Biochimie` | Structure des biomolécules · Protéines et enzymes · Métabolisme énergétique · Glucides et glycolyse · Lipides et β-oxydation · Acides aminés et cycle de l'urée · Acides nucléaires et synthèse protéique · Vitamines et coenzymes · Biochimie du sang · Dosages et techniques analytiques |
| `Microbiologie` | Morphologie et classification bactérienne · Structure et paroi bactérienne · Croissance et culture · Génétique bactérienne · Pathogénicité et virulence · Virus et virologie · Champignons et mycologie · Parasitologie · Antibiothérapie et résistance · Hygiène et prévention des infections |
| `Pharmacologie` | Principes généraux et pharmacocinétique · Récepteurs et pharmacodynamie · Médicaments du système nerveux · Médicaments cardio-vasculaires · Anti-infectieux · Anti-inflammatoires et analgésiques · Hormones et médicaments endocriniens · Effets indésirables et interactions · Posologie et formes galéniques · Pharmacovigilance |

## 2. Sciences humaines, droit et méthodologie

| Matière FicheLab | Chapitres |
|---|---|
| `Droit de la santé` | Droit de la santé et organisations sanitaires · Droits du patient et consentement · Secret médical et données de santé · Responsabilité médicale · Déontologie et ordres professionnels · Santé publique et prévention · Sécurité sociale et remboursement · Législation des médicaments |
| `Éthique` | Éthique médicale et principes fondamentaux · Autonomie et consentement · Bénéfice, non-malfaisance et justice · Questions de fin de vie · Éthique de la recherche · Éthique et numérique en santé · Délibération et conflits de valeurs |
| `Français` | Expression et communication scientifique · Analyse de documents · Argumentation et synthèse · Rédaction professionnelle |
| `Maths / stats` | Calcul et unités · Fonctions et graphiques · Statistiques descriptives · Probabilités · Tests statistiques et interprétation · Lecture d'articles scientifiques |
| `Anglais professionnel` | Vocabulaire médical et scientifique · Lecture d'articles · Expression écrite · Communication internationale |
| `Méthodologie` | Méthodes de travail universitaire · Recherche documentaire et bases de données · Lecture critique d'articles · Construction d'un plan · Gestion du temps et révision · Préparation des concours d'accès |

---

## 3. Méthode

Une fiche = un chapitre, 7 blocs + 3 schémas SVG, 12 points, 9-10 questions corrigées, source officielle, information « à vérifier ». Voir [`FICHE-PROTOTYPE.md`](FICHE-PROTOTYPE.md) et [`AUDIT-FILIERES.md`](AUDIT-FILIERES.md).

## 4. Suivi

| Lot | Générateur | Matières | Statut |
|---|---|---|---|
| A | `data/gen_pass_A.py` | Anatomie, Physiologie | ✅ généré (20) |
| B | `data/gen_pass_B.py` | Biochimie, Microbiologie, Pharmacologie | ✅ généré (22) |
| C | `data/gen_pass_C.py` | Droit de la santé, Éthique, Français, Maths / stats, Anglais professionnel, Méthodologie | ✅ généré (20) |

**Déclinaison terminée** : 62 fiches, 186 schémas SVG, 558 questions corrigées. Audit [AUDIT-FILIERES.md](AUDIT-FILIERES.md) : conforme.
