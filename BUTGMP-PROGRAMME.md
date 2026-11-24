# BUT Génie mécanique et productique — carte des chapitres FicheLab

> Référentiel : **arrêté du 11 mars 2020** portant création du diplôme national de bachelor de technologie (BO n° 12 du 19 mars 2020), spécialité « Génie mécanique et productique », complété par l'arrêté du 15 avril 2022 (BO n° 19 du 12 mai 2022) et les ressources éduscol / iut.fr / onisep.fr.
> Source : [`SOURCES.md`](SOURCES.md) §1 / §2 — BUT : **148 600 inscrits** à la rentrée 2025, 6 semestres / 180 ECTS, référentiels des 24 spécialités (iut.fr).
> Identifiant : `but-gmp`. Années : `BUT1`, `BUT2`, `BUT3`.

---

## 1. Matières du questionnaire (nomenclature exacte)

Les huit matières ci-dessous sont celles proposées par le questionnaire FicheLab pour toute filière `but-*` (`MATIERES.but` dans `index.html`). Le catalogue `but-gmp` les reprend **à l'identique**, sans ajout ni variante :

`Gestion` · `Comptabilité` · `Droit` · `Marketing` · `Informatique` · `Maths / stats` · `Communication` · `Anglais professionnel`

> Les enseignements professionnels spécifiques du référentiel GMP (conception mécanique, procédés de fabrication, automatisation, maintenance) sont traités ici sous l'angle des **outils et méthodes** : ils alimentent les chapitres `Informatique` (CAO/DAO, FAO, CN, PLM, simulation) et `Gestion` (méthodes, qualité, maintenance, supply chain).

## 2. Carte BUT1 / BUT2 / BUT3 par matière

Lecture : **BUT1** = découverte et outils de base (niveau 1 des blocs de compétences), **BUT2** = mise en œuvre autonome en environnement complexe (niveau 2), **BUT3** = pilotage, optimisation et transversalité (niveau 3, projet de fin d'études).

| Matière FicheLab | BUT1 — fondamentaux | BUT2 — mise en œuvre | BUT3 — pilotage |
|---|---|---|---|
| `Informatique` | CAO/DAO 2D, modélisation 3D, initiation GMAO/ERP, données de production | FAO, programmation CNC, simulation mécanique, cybersécurité industrielle, PLM | PLM avancé, données de production et pilotage, cybersécurité OT |
| `Maths / stats` | Calcul littéral, fonctions, statistiques descriptives, probabilités | Dérivation, intégration, loi normale, échantillonnage et tests | Matrices et systèmes linéaires, optimisation linéaire, tests avancés |
| `Gestion` | Gestion de production, coûts, sécurité | Planification, méthodes, qualité, maintenance, supply chain, projet | Amélioration continue, pilotage de la performance, gestion de projet industriel |
| `Comptabilité` | Bilan, résultat, TVA, coûts de production | Comptabilité analytique, budgets, amortissements, calcul de prix | Investissements, contrôle budgétaire, diagnostic financier |
| `Droit` | Droit des affaires, contrat, concurrence | Droit social, propriété intellectuelle, responsabilité | Droit de la production, conformité et contrats industriels |
| `Marketing` | Étude de marché, mix marketing | Segmentation, prix, distribution, marketing industriel | Plan marketing, indicateurs, marketing B to B et international |
| `Communication` | Communication écrite et orale, vocabulaire technique | Réunion, compte rendu, négociation fournisseur | Conduite de réunion, soutenance, gestion de projet et changement |
| `Anglais professionnel` | Vocabulaire technique, lecture de notices | Expression écrite, email, rapport technique | Communication internationale, présentation et négociation |

## 3. Répartition des 60 fiches

| Matière | Codes | BUT1 | BUT2 | BUT3 | Total |
|---|---|---:|---:|---:|---:|
| Informatique | `IN1.`–`IN10.` | 3 | 4 | 3 | 10 |
| Maths / stats | `MS1.`–`MS10.` | 4 | 4 | 2 | 10 |
| Gestion | `GE1.`–`GE10.` | 3 | 5 | 2 | 10 |
| Comptabilité | `CP1.`–`CP10.` | 4 | 4 | 2 | 10 |
| Communication | `CO1.`–`CO5.` | 2 | 2 | 1 | 5 |
| Droit | `DR1.`–`DR5.` | 2 | 2 | 1 | 5 |
| Marketing | `MK1.`–`MK5.` | 2 | 2 | 1 | 5 |
| Anglais professionnel | `AN1.`–`AN5.` | 2 | 2 | 1 | 5 |
| **Total** | | **22** | **25** | **13** | **60** |

Chaque fiche est un chapitre complet au **format prototype** : 12 points de cours, 9 questions corrigées (7 QCM + 2 rédaction), 7 blocs d'affichage dans l'ordre strict, 3 schémas SVG intégrés, source officielle, statut « à vérifier ». Voir [`FICHE-PROTOTYPE.md`](FICHE-PROTOTYPE.md).

## 4. Méthode de production en 4 étapes

1. **Cadrer** — lire le référentiel BUT GMP (arrêté du 11 mars 2020), la nomenclature exacte du questionnaire et la carte ci-dessus ; attribuer un code unique préfixé par matière (`IN`, `MS`, `GE`, `CP`, `CO`, `DR`, `MK`, `AN`).
2. **Rédiger** — pour chaque code, écrire les 12 points, le glossaire (6 notions), la formule, les 5 étapes de méthode, les pièges et les exemples chiffrés ; ancrer chaque chapitre dans un attendu du référentiel et un usage GMP concret (atelier, bureau d'études, production).
3. **Générer** — construire la fiche avec `data/fixtures.py` (`fiche`, `qcm`, `qt`, `diag`, `svg_*`, `bloc`) puis valider via `valider_et_ecrire()` : 12 points, 9 questions (≥6 QCM, ≥2 texte), 7 blocs ordre strict, 2–4 SVG, aucun artefact CJK, titres uniques.
4. **Vérifier** — régénérer les trois lots, contrôler les doublons de titres **entre lots** et la couverture BUT1/BUT2/BUT3, puis consigner le résultat dans [`AUDIT-BUTGMP.md`](AUDIT-BUTGMP.md).

## 5. Suivi des lots

| Lot | Générateur | Matières | Fiches | JSON |
|---|---|---|---:|---|
| A | `data/gen_butgmp_A.py` | Informatique (10), Maths / stats (10) | 20 | `data/butgmp-mat-part-A.json` |
| B | `data/gen_butgmp_B.py` | Gestion (10), Comptabilité (10) | 20 | `data/butgmp-mat-part-B.json` |
| C | `data/gen_butgmp_C.py` | Communication (5), Droit (5), Marketing (5), Anglais professionnel (5) | 20 | `data/butgmp-mat-part-C.json` |

**Déclinaison terminée** : 60 fiches, 180 schémas SVG, 540 questions corrigées. Audit [`AUDIT-BUTGMP.md`](AUDIT-BUTGMP.md).
