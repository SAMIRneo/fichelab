# BUT Gestion des entreprises et des administrations — carte des chapitres FicheLab

> Référentiel : **arrêté du 11 mars 2020** (BO n°12 du 19 mars 2020), BUT « Gestion des entreprises et des administrations » (GEA), programmes nationaux et ressources R1 à R6, éduscol / iut.fr / onisep.fr.
> Source : [`SOURCES.md`](SOURCES.md) §1 — **207 919 vœux Parcoursup 2026** (6ᵉ formation la plus demandée, 3ᵉ BUT le plus demandé).
> Identifiant : `but-gea`. Années : `BUT1`, `BUT2`, `BUT3`.

---

## 1. Enseignement professionnel — tronc commun et parcours

| Matière FicheLab | Chapitres |
|---|---|
| `Gestion` | Gestion d'entreprise · Organisation · Ressources humaines · Contrôle de gestion · Budget prévisionnel · Analyse des coûts · Performance et indicateurs · Conduite de projet · Qualité et amélioration continue · Management |
| `Comptabilité` | Bilan · Compte de résultat · Plan comptable général · TVA · Comptabilité analytique · Coûts et marges · Seuil de rentabilité · Budget de trésorerie · Analyse financière · Diagnostic d'entreprise |

Ces dix chapitres par matière couvrent les ressources R1.01 à R1.10 (tronc commun de BUT1) et les ressources R2/R3 des parcours GC2F (finance), CG2P (gestion de projets), GPRH (ressources humaines) et GEMA (management d'activités) en BUT2/BUT3.

## 2. Enseignement général et transversal

| Matière FicheLab | Chapitres |
|---|---|
| `Droit` | Droit des obligations · Droit des sociétés · Droit commercial · Droit de la consommation · Droit du travail · Concurrence et pratiques restrictives · Responsabilité et propriété intellectuelle |
| `Marketing` | Étude de marché · Segmentation et positionnement · Mix marketing · Politique produit · Politique de prix · Distribution et merchandising · Marketing digital |
| `Communication` | Communication écrite · Communication orale et réunion · Négociation et relation client · Communication interne · Communication de crise et e-réputation · Soutenance et présentation |
| `Informatique` | Outils numériques et tableurs · Systèmes d'information (ERP/SIG/CRM) · Bases de données et SQL · Tableaux de bord · RGPD et sécurité · Automatisation et IA · E-commerce et données clients |
| `Maths / stats` | Pourcentages et proportions · Fonctions et graphiques · Statistiques descriptives · Probabilités et échantillonnage · Intérêts et actualisation · Tests et intervalles de confiance · Mathématiques financières |
| `Anglais professionnel` | Correspondance commerciale · Lecture et expression écrite · Communication internationale et soutenance |
| `Méthodologie` | Recherche documentaire et citation · Analyse de situation et conduite de projet · Rapport, soutenance et évaluation |

> Les sept matières ci-dessus reprennent exactement la liste du questionnaire FicheLab pour la filière `but-gea` (base supérieure + liste `but`) : `Gestion`, `Comptabilité`, `Droit`, `Marketing`, `Communication`, `Informatique`, `Maths / stats`, `Anglais professionnel`, `Méthodologie`.

## 3. Méthode de rédaction (4 étapes)

1. **Cadrer** — repérer la ressource du référentiel (R1.xx, R2.xx, parcours GC2F / CG2P / GPRH / GEMA), l'année (`BUT1`, `BUT2` ou `BUT3`) et la source officielle à citer (arrêté du 11 mars 2020, BO, éduscol, PCG, Code civil, Code de commerce, CGI, Code du travail, RGPD, CECRL).
2. **Rédiger** — 12 points de cours par chapitre, sous forme de phrases courtes et vérifiables, puis 9 questions corrigées (7 QCM + 2 questions rédaction, dont des exercices chiffrés) couvrant l'ensemble des points.
3. **Mettre en forme** — 7 blocs d'affichage dans l'ordre strict `intro, formule, grille, liste, etapes, attention, exemples` et 3 schémas SVG `diag()` construits par `fixtures.py` (grille, étapes, comparaison), sans texte qui déborde.
4. **Valider** — `valider_et_ecrire()` (`fixtures.py`) jusqu'à `OK` sans erreur ; contrôle des doublons de titres inter-lots, des matières, des années, des blocs, des SVG et de l'absence d'artefacts CJK. Voir [`FICHE-PROTOTYPE.md`](FICHE-PROTOTYPE.md) et [`AUDIT-BUTGEA.md`](AUDIT-BUTGEA.md).

Toute fiche est livrée avec le statut **à vérifier** : la source est explicite, le contenu reste à relecture pédagogique avant utilisation en exercice.

## 4. Suivi des lots

| Lot | Générateur | Matières | Fiches |
|---|---|---|---:|
| A | `data/gen_butgea_A.py` | Gestion (GE1.–GE10.), Comptabilité (CP1.–CP10.) | 20 |
| B | `data/gen_butgea_B.py` | Droit (DR1.–DR7.), Marketing (MK1.–MK7.), Communication (CO1.–CO6.) | 20 |
| C | `data/gen_butgea_C.py` | Informatique (IN1.–IN7.), Maths / stats (MS1.–MS7.), Anglais professionnel (AN1.–AN3.), Méthodologie (ME1.–ME3.) | 20 |

Fichiers JSON produits : `data/butgea-mat-part-A.json`, `data/butgea-mat-part-B.json`, `data/butgea-mat-part-C.json`.

**Déclinaison terminée** : 60 fiches, 180 schémas SVG, 540 questions corrigées. Audit [`AUDIT-BUTGEA.md`](AUDIT-BUTGEA.md) : CONFORME.

> `index.html`, `inject_app.py` et `audit_filieres.py` n'ont pas été modifiés : l'injection des lots dans l'application relève d'une étape distincte.
