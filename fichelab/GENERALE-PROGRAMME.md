# Voie générale (lycée) — carte des chapitres FicheLab

> Référentiels : programmes de l'école au lycée — **BO spécial n° 1 du 22 janvier 2019** (classe de 2nde), **BO spécial n° 1 du 22 janvier 2019** (classe de 1re), **BO du 22 juillet 2020** (spécialités de Terminale), arrêtés du 17 juillet 2018, éduscol / circulaires BO.
> Sources : [`SOURCES.md`](SOURCES.md) §1 (effectifs DEPP rentrée 2025 : **1 599 420 élèves** en lycée GT, dont ~75 % en voie générale) et §2 (programmes officiels).
> L'appli utilise l'identifiant `generale` ; le nom affiché est « Voie générale — 1,2 M d'élèves ».

---

## 1. Tronc commun — classe de 2nde

| Matière | Chapitres couverts |
|---|---|
| Français | Théâtre du XVIIe au XXIe siècle · Poésie du XIXe au XXIe siècle · Roman et récit · Argumentation, essai et littérature d'idées |
| Mathématiques | Fonctions affines et de référence · Second degré · Dérivation et variations · Statistiques descriptives · Vecteurs et géométrie · Trigonométrie · Probabilités |
| Physique-chimie | Structure de la matière et transformations · Analyse d'échantillons et dosage · Énergie et conversions · Électricité · Mouvement et interactions · Ondes et signaux · Sécurité chimique |
| SVT | La cellule, unité du vivant · Organisation et fonctionnement des êtres vivants · Génétique et hérédité · Évolution et biodiversité · La planète et les enjeux environnementaux |
| Histoire-Géographie | Monde méditerranéen médiéval · Sociétés et États XVIe-XVIIIe · Révolutions et nations · Industrialisation · Impérialismes et guerres mondiales · Grands ensembles géographiques |
| EMC | La laïcité et les libertés · Institutions de la Ve République · Citoyenneté et engagement |
| Anglais | Grammaire et temps · Expression écrite · Compréhension de documents · Vocabulaire thématique |
| LCA | Langues et civilisations de l'Antiquité : mythes, traduction, civilisation |

## 2. Tronc commun — classe de 1re

| Matière | Chapitres couverts |
|---|---|
| Français | Théâtre et représentation · Poésie et engagement · Roman, récit et argumentation |
| Mathématiques | Suites numériques · Fonction exponentielle · Fonction logarithmique · Intégration et primitives · Probabilités conditionnelles · Lois de probabilité · Géométrie dans l'espace |
| Physique-chimie | Acide-base et titrages · Oxydoréduction et piles · Cinétique chimique · Thermochimie · Ondes lumineuses et couleurs · Signaux et traitement |
| SVT | Génétique et expression du patrimoine · Variations génétiques et santé · Système immunitaire · Neurosciences et perception |
| Histoire-Géographie | Croissance et crises économiques · État et société en France · Ve République · Métropolisation et mobilités · Territoires et mondialisation |
| SES | Formation des prix · Monnaie et financement · Croissance et chômage · Échanges internationaux · Socialisation et division du travail · Consommation |
| Spécialités | SES · NSI · SI · HGGSP · HLP · LLCE · Arts · Biologie-écologie (3 spécialités choisies par l'élève) |

## 3. Terminale — tronc commun et spécialités

| Matière | Chapitres couverts |
|---|---|
| Philosophie | Conscience · Liberté · Vérité · Justice et État · Travail, technique et art |
| Mathématiques (spé) | Limites et continuité · Dérivation approfondie · Intégrales · Suites récurrentes · Fonctions de deux variables · Lois usuelles |
| Physique-chimie (spé) | Thermodynamique et équilibres · Cinétique et catalyse · Électrochimie · Optique et interférences · Diffraction · Photons |
| SVT (spé) | Génétique et évolution · Anatomie et fonctionnement du corps humain · Écologie et dynamique des populations |
| Histoire-Géographie | Guerre froide · Fin des colonies · France depuis 1958 · Construction européenne · Mondialisation · Développement durable |
| Spécialités | NSI (algorithmique, données, réseaux) · SI (modélisation, matériaux, énergie) · HGGSP (géopolitique, frontières, médias) · HLP (littérature et pensée) · LLCE · Arts · Biologie-écologie |
| Grand oral | Choix d'un sujet · Construction de la question · Argumentaire et communication |

---

## 4. Méthode de travail convenue (identique au BIOALC)

1. **Étape 1** — Valider la carte des chapitres ci-dessus.
2. **Étape 2** — Construire UNE fiche prototype : **une fiche = un chapitre**, du texte court en 7 blocs colorés + schémas SVG, avec 12 points de cours et 10 questions corrigées — jamais un mur de texte.
3. **Étape 3** — Valider le rendu dans l'appli puis décliner le même modèle à tous les chapitres de la matière.
4. **Étape 4** — Répéter matière par matière.

Règle d'or conservée : **chaque information générée démarre « à vérifier » avec sa source** (`fichesPour()` marque toutes les fiches `a-lire`) ; une fiche ne devient « lue » qu'après un quizz réussi à 8/10.

---

## 5. Format prototype (identique au BIOALC)

Chaque fiche contient exactement 9 champs : `filieres`, `annees`, `matiere`, `titre`, `source`, `points` (12), `questions` (9-10 dont ≥ 6 QCM et ≥ 2 rédaction, corrections détaillées), `affichage` (7 blocs dans l'ordre `intro, formule, grille, liste, etapes, attention, exemples`) et `schema` (3 schémas SVG intégrés, thémables clair/sombre).

Bibliothèque de référence : [`FICHE-PROTOTYPE.md`](FICHE-PROTOTYPE.md), [`LEARNING-SCIENCE.md`](LEARNING-SCIENCE.md), [`SOURCES.md`](SOURCES.md).

---

## 6. Suivi de la déclinaison

| Lot | Fichier générateur | Matières | Statut |
|---|---|---|---|
| A | `data/gen_generale_A.py` | Français, Philosophie, Méthodologie | ✅ généré |
| B | `data/gen_generale_B.py` | Maths | ✅ généré |
| C | `data/gen_generale_C.py` | Physique-Chimie | ✅ généré |
| D | `data/gen_generale_D.py` | SVT, Biologie-écologie | ✅ généré |
| E | `data/gen_generale_E.py` | Histoire-Géographie, EMC | ✅ généré |
| F | `data/gen_generale_F.py` | Anglais, SES, HGGSP, HLP | ✅ généré |
| G | `data/gen_generale_G.py` | NSI, SI, LLCE, LCA, Arts | ✅ généré |

**Déclinaison terminée** : toutes les fiches de la voie générale utilisent le même format que le BTS BIOALC. Les profils `generale` ne voient plus que ces fiches : les anciennes fiches « texte brut » du catalogue sont filtrées à la génération et retirées du stockage local au démarrage (les fiches personnelles sont conservées). Voir [`AUDIT-FILIERES.md`](AUDIT-FILIERES.md) pour le contrôle final (effectifs, schémas, doublons, syntaxe JS).
