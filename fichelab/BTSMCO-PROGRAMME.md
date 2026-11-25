# BTS Management Commercial Opérationnel (MCO) — carte des chapitres FicheLab

> Référentiel : **arrêté du 14 décembre 2016** modifié (BO du 22 décembre 2016), BTS « Management commercial opérationnel », code RNCP 36114 · programmes d'enseignement général applicables à la session 2026.
> Sources : [`SOURCES.md`](SOURCES.md) §1 — **186 656 vœux Parcoursup 2026**, 8ᵉ formation la plus demandée ; 21 annales déjà présentes dans la bibliothèque.
> L'appli utilise l'identifiant `bts-mco`. Années : `BTS1`, `BTS2`.

---

## 1. Enseignement général

| Unité | Matière FicheLab | Chapitres |
|---|---|---|
| U1 | `Français` | Synthèse de documents · Analyse de situation et argumentation · Expression écrite professionnelle · Culture générale et ouverture · Communication écrite et numérique |
| U2 | `Anglais professionnel` | Compréhension de documents commerciaux · Lexique du commerce et de la vente · Expression écrite professionnelle · Relation client à l'écrit · Présentation et expression orale |
| U3 | `Maths / stats` | Calcul numérique et littéral · Fonctions et représentations · Statistiques descriptives · Probabilités et échantillonnage · Étude de marchés et indicateurs · Mathématiques financières |
| — | `Méthodologie` | Méthode d'analyse de situation · Conduite de projet · Recherche et veille · Présentation et soutenance |

## 2. Enseignement professionnel

| Unité | Matière FicheLab | Chapitres |
|---|---|---|
| U4 | `Droit` + `Économie` | Droit des affaires et des contrats · Droit de la concurrence et de la consommation · Droit social et relations de travail · Économie générale et marchés · Économie de l'entreprise et de la distribution · Conjoncture et environnement économique |
| U5 | `Management` | Management opérationnel d'une unité commerciale · Organisation et planification de l'activité · Animation et pilotage d'équipe · Gestion des ressources et des talents · Qualité et amélioration continue · Conduite du changement |
| U6 | `Management` / `Communication` | Négociation et relation client · Prospection et fidélisation · Traitement des réclamations · Communication commerciale et digitale · Animation d'équipe et leadership · CRM et données clients |
| U7 | `Marketing` + `Comptabilité et gestion` | Étude de marché et segmentation · Politique de produit et de prix · Distribution et merchandising · Politique de communication et promotion · Suivi budgétaire et coûts · Contrôle de gestion et indicateurs commerciaux |
| U8 | `Informatique` / `Communication` | Systèmes d'information commerciale · Outils numériques de gestion · Données clients et RGPD · E-commerce et canaux digitaux · Cybersécurité et usages responsables |
| U9 | `Méthodologie` | Projet professionnel et soutenance · Construction d'une démarche projet · Veille et innovation commerciale · Éthique et responsabilité professionnelle |

---

## 3. Méthode (identique au BIOALC et à la voie générale)

Une fiche = un chapitre, 7 blocs colorés + 3 schémas SVG, 12 points de cours, 9-10 questions corrigées. Chaque information démarre « à vérifier » avec sa source. Voir [`FICHE-PROTOTYPE.md`](FICHE-PROTOTYPE.md), [`GENERALE-PROGRAMME.md`](GENERALE-PROGRAMME.md) et [`AUDIT-FILIERES.md`](AUDIT-FILIERES.md).

## 4. Suivi de la déclinaison

| Lot | Générateur | Matières | Statut |
|---|---|---|---|
| A | `data/gen_mco_A.py` | Français, Anglais professionnel, Méthodologie | ✅ généré (18) |
| B | `data/gen_mco_B.py` | Maths / stats, Informatique | ✅ généré (18) |
| C | `data/gen_mco_C.py` | Droit, Économie, Comptabilité et gestion | ✅ généré (22) |
| D | `data/gen_mco_D.py` | Management, Marketing, Communication | ✅ généré (24) |

**Déclinaison terminée** : 82 fiches, 246 schémas SVG, 742 questions corrigées. Audit [AUDIT-FILIERES.md](AUDIT-FILIERES.md) : conforme.
