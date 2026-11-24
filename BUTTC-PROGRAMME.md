# BUT Techniques de commercialisation — carte des chapitres FicheLab

> Référentiel : **arrêté du 11 mars 2020** modifié, BUT « Techniques de commercialisation » (BO, référentiel BUT TC, éduscol), applicable à la rentrée 2025.
> Source : [`SOURCES.md`](SOURCES.md) §1 — **208 804 vœux Parcoursup 2026** (5ᵉ formation la plus demandée).
> Identifiant : `but-tc`. Années : `BUT1`, `BUT2`, `BUT3`.

---

## 1. Enseignement général et transversal

| Matière FicheLab | Chapitres |
|---|---|
| `Droit` | Droit des affaires · Contrats commerciaux · Concurrence et consommation · Droit social · Propriété intellectuelle · Responsabilité |
| `Maths / stats` | Calcul et pourcentages · Fonctions et représentations · Statistiques descriptives · Probabilités · Échantillonnage et tests · Mathématiques financières |
| `Informatique` | Outils numériques de gestion · Données clients et CRM · SIG / ERP · E-commerce · RGPD et données personnelles · Tableaux de bord numériques |
| `Anglais professionnel` | Vocabulaire commercial · Lecture de documents · Expression écrite · Communication internationale |
| `Méthodologie` | Recherche documentaire · Analyse de situation · Conduite de projet · Soutenance et oral |

## 2. Enseignement professionnel

| Matière FicheLab | Chapitres |
|---|---|
| `Marketing` | Étude de marché · Segmentation et positionnement · Mix marketing · Politique produit · Politique de prix · Distribution et merchandising · Communication et promotion · Marketing digital · Réseaux sociaux · Plan marketing et indicateurs |
| `Communication` | Négociation commerciale · Relation client · Fidélisation · Traitement des réclamations · Communication écrite et orale · Animation d'équipe · Gestion de projet · E-réputation |
| `Gestion` | Gestion d'entreprise · Contrôle de gestion · Budget prévisionnel · Analyse des coûts · Performance commerciale · Gestion des ressources humaines · Logistique et supply chain · Qualité et amélioration continue · Conduite du changement · Management d'équipe |
| `Comptabilité` | Bilan et compte de résultat · Plan comptable général · TVA · Comptabilité analytique · Coûts et marges · Seuil de rentabilité · Budgets · Contrôle budgétaire · Analyse financière · Diagnostic d'entreprise |

## 3. Méthode

Une fiche = un chapitre, 7 blocs + 3 schémas SVG, 12 points, 9 questions corrigées, source officielle, information « à vérifier ». Voir [`FICHE-PROTOTYPE.md`](FICHE-PROTOTYPE.md) et [`AUDIT-FILIERES.md`](AUDIT-FILIERES.md).

## 4. Suivi des lots

| Lot | Générateur | Matières | Fiches |
|---|---|---|---:|
| A | `data/gen_buttc_A.py` | Marketing, Communication | 20 |
| B | `data/gen_buttc_B.py` | Gestion, Comptabilité | 10 |
| C | `data/gen_buttc_C.py` | Droit, Maths / stats, Informatique, Anglais professionnel, Méthodologie | 20 |

**Déclinaison terminée** : 50 fiches, 150 schémas SVG, 450 questions corrigées. Audit [`AUDIT-BUTTC.md`](AUDIT-BUTTC.md) : CONFORME.

> Note d'organisation : l'outil de sous-délégation n'étant pas disponible dans les sessions enfants, le responsable de filière a rédigé les lots directement.
