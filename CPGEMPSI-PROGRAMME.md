# CPGE MPSI — carte des chapitres FicheLab

> **Filière** : Classes préparatoires aux grandes écoles, voie MPSI (mathématiques, physique, sciences de l'ingénieur) — **197 775 vœux Parcoursup 2026** (7ᵉ formation la plus demandée, source SIES / [`SOURCES.md`](SOURCES.md) §1).
> **Référentiels** : arrêté du **19 juillet 2019** fixant les programmes des classes préparatoires aux grandes écoles (NOR MENE1922062A), **BO spécial n° 5 du 25 juillet 2019** (mathématiques, physique, chimie, sciences de l'ingénieur), BO spécial n° 8 du 25 juillet 2019 (français, philosophie, langues vivantes), circulaires et ressources **éduscol / Onisep / SIES**.
> **Identifiant appli** : `cpge-mpsi`. **Années** : `1re` (MPSI1) et `2e` (MPSI2).
> Sources chiffrées et programmes : [`SOURCES.md`](SOURCES.md) §1 et §2 · format : [`FICHE-PROTOTYPE.md`](FICHE-PROTOTYPE.md) · méthode : [`GENERALE-PROGRAMME.md`](GENERALE-PROGRAMME.md).

---

## 1. Principaux enseignements — MPSI1 (`1re`)

| Matière | Chapitres couverts (fiches FicheLab) |
|---|---|
| **Maths** | `MA1.` Espaces vectoriels et applications linéaires · `MA2.` Limites, continuité et dérivation · `MA3.` Fonctions de référence et variations · `MA4.` Suites numériques · `MA5.` Intégration et primitives |
| **Physique** | `PH1.` Cinématique du point · `PH2.` Dynamique et lois de Newton · `PH3.` Travail, énergie et puissance · `PH4.` Mécanique : quantité de mouvement et chocs · `PH5.` Oscillations mécaniques |
| **Chimie** | `CH1.` Structure atomique et orbitales · `CH2.` Liaisons chimiques et géométrie moléculaire · `CH3.` Réactivité et mécanismes réactionnels · `CH4.` Acide-base et pH · `CH5.` Oxydoréduction et piles |
| **Français** | `FR1.` Littérature et civilisation du XIXᵉ siècle · `FR2.` Littérature et civilisation du XXᵉ siècle |
| **Philosophie** | `PHI1.` Conscience et inconscient · `PHI2.` Liberté et détermination · `PHI3.` Vérité et doute |
| **Anglais** | `AN1.` Grammaire et structures de base · `AN2.` Compréhension de documents écrits · `AN3.` Expression écrite : lettre, essai, compte rendu |
| **Économie** | `EC1.` Rareté et allocation des ressources · `EC2.` Offre, demande et prix de marché · `EC3.` Structures de marché et concurrence |
| **Maths / stats** | `MS1.` Statistiques descriptives et probabilités · `MS2.` Variables aléatoires et lois usuelles |

## 2. Principaux enseignements — MPSI2 (`2e`)

| Matière | Chapitres couverts (fiches FicheLab) |
|---|---|
| **Maths** | `MA6.` Équations différentielles · `MA7.` Probabilités et variables aléatoires · `MA8.` Géométrie dans l'espace · `MA9.` Arithmétique et nombres complexes · `MA10.` Réduction des endomorphismes et séries |
| **Physique** | `PH6.` Ondes et phénomènes vibratoires · `PH7.` Optique géométrique · `PH8.` Électricité : circuits et lois · `PH9.` Électromagnétisme · `PH10.` Thermique et thermodynamique |
| **Chimie** | `CH6.` Cinétique chimique · `CH7.` Équilibres chimiques · `CH8.` Thermochimie · `CH9.` Chimie organique · `CH10.` Analyse chimique et titrages |
| **Français** | `FR3.` La dissertation littéraire · `FR4.` Le commentaire de texte · `FR5.` L'oral de français : explication et entretien |
| **Philosophie** | `PHI4.` Justice et État · `PHI5.` Travail, technique et art |
| **Anglais** | `AN4.` Compréhension et expression orales · `AN5.` Civilisation et culture anglo-saxonne · `AN6.` Méthodologie des épreuves de concours |
| **Économie** | `EC4.` Croissance et développement · `EC5.` Monnaie, inflation et politiques monétaires · `EC6.` Commerce international et globalisation |
| **Maths / stats** | `MS3.` Estimation et intervalles de confiance · `MS4.` Tests statistiques et régression |

---

## 3. Méthode de travail en 4 étapes (identique au BIOALC et à la voie générale)

1. **Étape 1 — Cartographier** : valider la carte ci-dessus chapitre par chapitre, en confrontant les programmes officiels de CPGE (arrêté du 19 juillet 2019, BO spécial n° 5 et n° 8) et les attendus des concours (ENS, Polytechnique, Centrale, Mines, ESA, etc.).
2. **Étape 2 — Fiche prototype** : construire UNE fiche = UN chapitre, avec **12 points de cours**, **9 questions corrigées** (≥ 6 QCM + ≥ 2 rédaction), **7 blocs colorés** et **3 schémas SVG** intégrés — jamais un mur de texte.
3. **Étape 3 — Valider puis décliner** : contrôler le rendu dans l'appli (lisibilité des schémas, niveau du texte, couverture des questions), puis appliquer le même modèle à toute la matière.
4. **Étape 4 — Répéter** matière par matière, en gardant la règle « une fiche = un chapitre » et la règle d'or : **chaque information générée démarre « à vérifier » avec sa source**.

---

## 4. Format prototype (identique aux autres filières)

Chaque fiche contient exactement 9 champs : `filieres` (`["cpge-mpsi"]`), `annees` (`["1re"]` ou `["2e"]`), `matiere`, `titre` (préfixé, unique), `source` (officielle), `points` (12), `questions` (9-10 dont ≥ 6 QCM et ≥ 2 texte), `affichage` (7 blocs dans l'ordre strict `intro, formule, grille, liste, etapes, attention, exemples`) et `schema` (3 schémas SVG thémables clair/sombre). Aucun caractère CJK.

---

## 5. Suivi des lots

| Lot | Générateur | Sortie JSON | Matières | Fiches | Statut |
|---|---|---|---|---|---|
| A | `data/gen_cpge_A.py` | `cpge-mat-part-A.json` | Maths (10), Physique (10) | 20 | ✅ généré |
| B | `data/gen_cpge_B.py` | `cpge-mat-part-B.json` | Chimie (10), Français (5), Philosophie (5) | 20 | ✅ généré |
| C | `data/gen_cpge_C.py` | `cpge-mat-part-C.json` | Anglais (6), Économie (6), Maths / stats (4) | 16 | ✅ généré |

**Total : 56 fiches** — 504 questions corrigées, 168 schémas SVG, 672 points de cours.

> Équipe : l'outil de délégation `subagent` n'est pas disponible dans ce harness ; les trois lots ont été produits directement par le responsable de filière, avec les mêmes contrôles de qualité que les agents spécialisés auraient dû appliquer.
