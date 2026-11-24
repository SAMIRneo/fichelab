# Écoles de commerce — carte des chapitres FicheLab

> Filière **`commerce`** (Écoles de commerce, gestion, vente) : **262 100 étudiants** à la rentrée 2025, soit 8,6 % de l'enseignement supérieur — [`SOURCES.md`](SOURCES.md) §1, SIES *Note Flash* n° 17 (juillet 2026).
> Identifiant appli : `commerce`. Années : **`Bac+1`**, **`Bac+2`**, **`Bac+3`** (`ANNEES.commerce` dans `index.html`).
> Matières affichées par le questionnaire : `MATIERES.but` (`Gestion`, `Comptabilité`, `Droit`, `Marketing`, `Informatique`, `Maths / stats`, `Communication`, `Anglais professionnel`) + base sup (`Français`, `Méthodologie`) — voir `matieresPour()` dans `index.html`.
> Aucune modification de `index.html`, `inject_app.py` ni `audit_filieres.py` dans ce chantier.

---

## 1. Carte Bac+1 / Bac+2 / Bac+3 par matière

| Matière FicheLab | Bac+1 (fondations) | Bac+2 (méthodes) | Bac+3 (stratégie) |
|---|---|---|---|
| `Marketing` | `MK1.` étude de marché · `MK2.` segmentation · `MK3.` positionnement · `MK4.` mix 4P/7P | `MK5.` produit · `MK6.` prix · `MK7.` distribution et merchandising · `MK8.` communication et promotion · `MK9.` digital, SEO/SEA et social ads | `MK10.` marque et image · `MK11.` plan marketing et KPI · `MK12.` marketing international |
| `Communication` | `CO1.` relation client et parcours · `CO2.` négociation · `CO3.` communication écrite | `CO4.` expression orale et présentation · `CO5.` fidélisation et CRM · `CO6.` traitement des réclamations | `CO7.` animation d'équipe et leadership · `CO8.` e-réputation et crise |
| `Gestion` | `GE1.` environnement et fonctions · `GE2.` organisation et management · `GE3.` pilotage commercial | `GE4.` budget prévisionnel · `GE5.` coûts et marges · `GE6.` contrôle de gestion · `GE7.` ressources humaines | `GE8.` logistique et supply chain · `GE9.` management de projet · `GE10.` stratégie et RSE |
| `Comptabilité` | `CP1.` principes et PCG · `CP2.` bilan · `CP3.` compte de résultat | `CP4.` TVA · `CP5.` ventes et clients · `CP6.` achats et fournisseurs · `CP7.` comptabilité analytique | `CP8.` seuil de rentabilité · `CP9.` analyse financière · `CP10.` trésorerie et BFR |
| `Droit` | `DR1.` droit des affaires et formes juridiques · `DR2.` contrats commerciaux | `DR3.` concurrence et pratiques restrictives · `DR4.` droit de la consommation | `DR5.` propriété intellectuelle et données personnelles |
| `Maths / stats` | `MS1.` pourcentages et calculs commerciaux · `MS2.` statistiques descriptives | `MS3.` probabilités et décision · `MS4.` échantillonnage et tests | `MS5.` régression et prévisions |
| `Informatique` | `IN1.` SIG, ERP et outils numériques | `IN2.` CRM et données clients · `IN3.` e-commerce et tunnel de conversion | `IN4.` cybersécurité, RGPD et usages responsables |
| `Anglais professionnel` | `AN1.` lexique commercial et lecture de documents | `AN2.` expression écrite · `AN3.` réunion et négociation | `AN4.` anglais du marketing international |
| `Français` | `PF1.` synthèse de documents et argumentation | — | `PF2.` expression écrite et dossier professionnel |
| `Méthodologie` | Transversal : recherche documentaire et analyse de situation (`PF1`, `CO1`, `GE1`) | Transversal : conduite de projet et indicateurs (`GE9`, `MK11`) | Transversal : soutenance, veille et démarche projet (`PF2`, `GE10`) |

**Total : 60 chapitres** (20 par lot), répartis sur les trois années, chacun avec 12 points de cours, 10 questions corrigées (8 QCM + 2 texte), 7 blocs d'affichage et 3 schémas SVG.

---

## 2. Programmes, référentiels et sources mobilisés

- **Tronc commun des écoles de commerce / BUT** : référentiel BUT « Techniques de commercialisation », arrêté du 11 mars 2020 (BO n°12 du 19 mars 2020), compétences C1 à C6 et ressources R1 à R6 ; référentiel BUT « Gestion des entreprises et des administrations » ; programmes des formations des écoles de commerce et de gestion délivrant grade de licence ou de master (fiches RNCP) — éduscol, iut.fr, onisep.fr.
- **Marketing / Communication** : référentiel BUT TC (blocs « étude de marché », « communication commerciale », « pilotage »), programmes bachelor des écoles de commerce, normes et usages professionnels (charte RSE, RGPD pour la donnée client).
- **Gestion / Comptabilité** : référentiels BUT GEA et BUT TC, programme de BTS CG / MCO, Plan comptable général (arrêté du 22 juin 1993), règles de calcul des marges, du BFR et des ratios financiers.
- **Droit** : Code civil (contrat, responsabilité), Code de commerce (concurrence, pratiques restrictives), Code du travail, Code de la consommation, règlement (UE) 2016/679 (RGPD) et lois Informatique et Libertés.
- **Maths / stats** : programmes de mathématiques applicables en BUT/BTS, méthodes statistiques INSEE, notions de probabilités, d'échantillonnage et de régression.
- **Informatique** : référentiel de compétences numériques, outils SIG/ERP/CRM, recommandations CNIL et RGPD, principes de cybersécurité des systèmes d'information commerciale.
- **Anglais professionnel** : Cadre européen commun de référence pour les langues (CECRL), programmes de langues vivantes des écoles de commerce, lexique commercial et pratiques de la réunion d'affaires.
- **Français / Méthodologie** : programmes de culture générale et expression des formations supérieures (arrêté du 13 juillet 2023 pour le tronc commun), éduscol ; méthodes de synthèse, d'argumentation et de conduite de projet.
- **Rythme de révision** : répétition espacée (Cepeda et al., 2006) et effet du test (Roediger & Karpicke, 2006), détaillés dans [`LEARNING-SCIENCE.md`](LEARNING-SCIENCE.md).

Chaque fiche conserve une source explicite et démarre au statut « à vérifier » ; le format exact est décrit dans [`FICHE-PROTOTYPE.md`](FICHE-PROTOTYPE.md).

---

## 3. Méthode de production — 4 étapes

1. **Cadrer le référentiel.** Lire `SOURCES.md`, `FICHE-PROTOTYPE.md`, `BTSMCO-PROGRAMME.md`, `BUTTC-PROGRAMME.md` et `data/fixtures.py` ; relever les matières exactes du questionnaire (`MATIERES.but` + base sup), les années `Bac+1`/`Bac+2`/`Bac+3` et l'identifiant `commerce`.
2. **Rédiger la carte et les lots.** Écrire `COMMERCE-PROGRAMME.md`, puis décliner chaque chapitre dans `data/gen_commerce_A/B/C.py` en copiant la structure de `data/gen_generale_modele.py` : **12 points**, **10 questions** (8 QCM + 2 texte), **7 blocs en ordre strict** (`intro`, `formule`, `grille`, `liste`, `etapes`, `attention`, `exemples`), **3 schémas via `diag()`**, source officielle et titre unique préfixé `Commerce <lot> · <code> · …`.
3. **Valider à la génération.** Exécuter chaque générateur : `fixtures.valider_et_ecrire` contrôle les champs, les corrections, l'ordre des blocs, le XML des SVG, les coordonnées de texte, les artefacts CJK et les doublons de titres dans le lot.
4. **Contrôler en croisé et auditer.** Comparer les trois JSON entre eux (préfixes, codes, matières, années, compteurs, absence de CJK et de SVG interdit), puis consigner les résultats dans [`AUDIT-COMMERCE.md`](AUDIT-COMMERCE.md).

La même logique sert à la révision : lire les 12 points, refaire les calculs et les QCM, relire les 3 schémas, puis repasser le questionnaire.

---

## 4. Suivi de la déclinaison

| Lot | Générateur | JSON | Matières (fiches) | Fiches | Statut |
|---|---|---|---|---:|---|
| A | `data/gen_commerce_A.py` | `data/commerce-mat-part-A.json` | Marketing (12), Communication (8) | 20 | ✅ généré et validé |
| B | `data/gen_commerce_B.py` | `data/commerce-mat-part-B.json` | Gestion (10), Comptabilité (10) | 20 | ✅ généré et validé |
| C | `data/gen_commerce_C.py` | `data/commerce-mat-part-C.json` | Droit (5), Maths / stats (5), Informatique (4), Anglais professionnel (4), Français (2) | 20 | ✅ généré et validé |

Outils partagés : `data/gen_commerce_common.py` (construction des questions, des 7 blocs et des 3 SVG).

**Déclinaison terminée : 60 fiches, 720 points de cours, 600 questions corrigées (480 QCM + 120 texte), 180 schémas SVG.** Contrôle détaillé : [`AUDIT-COMMERCE.md`](AUDIT-COMMERCE.md).

> Note d'intégration : `inject_app.py` n'a pas été modifié (consigne du chantier). Pour injecter la filière dans `index.html`, l'orchestrateur doit ajouter `"commerce"` à `FILIERES_A_INTEGRER` puis relancer `inject_app.py` et `audit_filieres.py`.
