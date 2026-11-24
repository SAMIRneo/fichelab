# BTS Services informatiques aux organisations (SIO) — carte des chapitres FicheLab

> Référentiel : **arrêté du 6 mai 2013** portant création du BTS « Services informatiques aux organisations », **modifié** (JORF n° 0110 du 11 mai 2013, BO), décliné en deux options : **SISR** (Solutions d'infrastructure, systèmes et réseaux) et **SLAM** (Solutions logicielles et applications métiers). Programmes d'enseignement général et ressources : BO / éduscol.
> Sources : [`SOURCES.md`](SOURCES.md) §1 — **57 125 vœux Parcoursup 2026**, 8ᵉ BTS le plus demandé ; annales et référentiels SIO disponibles dans la bibliothèque.
> L'appli utilise l'identifiant `bts-sio`. Années : `BTS1`, `BTS2`. Matières : exactement celles du questionnaire BTS (`Français`, `Anglais professionnel`, `Maths / stats`, `Méthodologie`, `Management`, `Droit`, `Économie`, `Comptabilité et gestion`, `Communication`, `Marketing`, `Informatique`).

---

## 1. Enseignement général (tronc commun BTS)

| Unité | Matière FicheLab | Chapitres |
|---|---|---|
| U1 | `Français` | Synthèse de documents · Analyse de situation et argumentation · Expression écrite professionnelle · Culture générale et ouverture numérique |
| U2 | `Anglais professionnel` | Compréhension de documents techniques · Lexique de l'informatique · Expression écrite professionnelle · Expression orale et présentation |
| U3 | `Maths / stats` | Calcul numérique et littéral · Fonctions et représentations · Statistiques descriptives · Probabilités · Échantillonnage et estimation · Suites et récurrences · Mathématiques financières · Corrélation et régression |
| — | `Méthodologie` | Analyse de situation et étude de cas · Recherche et veille technologique · Soutenance et présentation de projet · Résolution de problèmes et révision |

## 2. Enseignement professionnel — socle commun et options

| Unité | Matière FicheLab | Chapitres |
|---|---|---|
| U4 | `Droit` + `Économie` | Droit des affaires · Droit des contrats · Concurrence et consommation · Droit social · Propriété intellectuelle et logicielle · Données personnelles et RGPD · Cybercriminalité · Offre et demande · Coûts de production · Conjoncture · Monnaie et inflation · Emploi · Mondialisation · Économie numérique |
| U5 | `Management` | Gestion de projet informatique · Management d'équipe · Conduite du changement · Qualité et amélioration continue · AMOA et besoins · Pilotage et indicateurs |
| U6 | `Informatique` | Réseaux et télécommunications · Systèmes d'exploitation · Sécurité · Administration des serveurs · Virtualisation · Scripts Bash/PowerShell · Bases de données · Développement web · Python · Génie logiciel · SISR/SLAM · Cybersécurité |
| U7 | `Communication` + `Management` | Communication interpersonnelle · Communication écrite et numérique · Réunion et présentation · Communication de crise · Relation client et usagers |
| U8 | `Comptabilité et gestion` | Bilan et compte de résultat · Coûts et prix de revient · Budget et contrôle de gestion · Indicateurs de gestion (déclinaison programme BTS) |
| U9 | `Méthodologie` + `Marketing` | Projet professionnel et soutenance · Veille et innovation · Éthique et responsabilité · (Marketing : étude de marché et offre — chapitres couverts par la filière MCO) |

> Les options **SISR** et **SLAM** partagent le socle U4/U5 ; l'option SISR approfondit infrastructure, systèmes, réseaux et sécurité, l'option SLAM approfondit développement, bases de données et génie logiciel. Les chapitres `IN1.` à `IN12.` indiquent l'option concernée dans leur source.

---

## 3. Méthode (identique au BIOALC, au BTS MCO et à la voie générale)

Une fiche = un chapitre : **12 points de cours**, **10 questions corrigées** (8 QCM + 2 rédaction), **7 blocs d'affichage** dans l'ordre strict `intro, formule, grille, liste, etapes, attention, exemples`, **3 schémas SVG** intégrés (`diag()`). Chaque information démarre « à vérifier » avec sa source officielle. Voir [`FICHE-PROTOTYPE.md`](FICHE-PROTOTYPE.md), [`BTSMCO-PROGRAMME.md`](BTSMCO-PROGRAMME.md) et [`AUDIT-FILIERES.md`](AUDIT-FILIERES.md).

## 4. Suivi des lots

| Lot | Générateur | JSON | Matières | Statut |
|---|---|---|---|---|
| A | `data/gen_btssio_A.py` | `data/btssio-mat-part-A.json` | Informatique (12), Maths / stats (8) | ✅ généré (20) |
| B | `data/gen_btssio_B.py` | `data/btssio-mat-part-B.json` | Droit (7), Économie (7), Management (6) | ✅ généré (20) |
| C | `data/gen_btssio_C.py` | `data/btssio-mat-part-C.json` | Français (4), Anglais professionnel (4), Communication (4), Méthodologie (4), Comptabilité et gestion (4) | ✅ généré (20) |

**Déclinaison terminée** : 60 fiches, 180 schémas SVG, 600 questions corrigées. Audit détaillé : [`AUDIT-BTSSIO.md`](AUDIT-BTSSIO.md).
