# BTS CIEL (Cybersécurité, Informatique et réseaux, Électronique) — carte des chapitres FicheLab

> **Référentiel retenu :** arrêté du **25 janvier 2023** portant définition et fixation des conditions de délivrance du BTS « Cybersécurité, Informatique et réseaux, Électronique », option A « Informatique et réseaux » (**IR**) et option B « Électronique et réseaux » (**ELC/ER**) — NOR **ESRS2300958A**, JORF n° 48 du 25 février 2023, première session 2025, fiche France compétences **RNCP37391**. Il remplace l'arrêté du 15 novembre 2013 relatif au BTS Systèmes numériques. Unités : **U1** culture générale et expression, **U2** langue vivante 1 (anglais), **U3** mathématiques, **U4** étude et conception, **U5** exploitation et maintenance, **U6** valorisation de la donnée et cybersécurité (IR), UF1/UF2 facultatives.
> **Rectificatif de source :** le cahier des charges indiquait « arrêté du 19 juillet 2019 ». Aucun texte fondateur du BTS CIEL ne porte cette date : la référence en vigueur est l'arrêté du 25 janvier 2023. Les mentions « 19 juillet 2019 » et « ELC » ont été conservées comme références de travail dans les 60 champs `source` et sont explicitées dans [`AUDIT-BTSCIEL.md`](AUDIT-BTSCIEL.md). Les programmes d'enseignement général renvoient aux arrêtés du 16 novembre 2006 (U1), du 22 juillet 2008 modifié (U2) et du 4 juin 2013 (U3).
> **Sources complémentaires :** Bulletins officiels et [éduscol — le BTS](https://eduscol.education.gouv.fr/5583/le-brevet-de-technicien-superieur) · [Légifrance, JORFTEXT000047226070](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047226070) · [France compétences RNCP37391](https://www.francecompetences.fr/recherche/rncp/37391) · [SOURCES.md](SOURCES.md) §1 : **53 416 vœux Parcoursup 2026**, 10ᵉ BTS le plus demandé · ANSSI (guides et parcours certifiant), CNIL, RGPD (UE 2016/679), NIS2 (UE 2022/2555), directives DMA/DSA, normes ISO/IEC 27001 et 27002, RFC TCP/IP, Code civil et Code pénal.
> **Identifiant appli :** `bts-ciel`. **Années :** `BTS1`, `BTS2`. **Matières du questionnaire (`index.html`, `matieresPour()`) :** `Français`, `Anglais professionnel`, `Maths / stats`, `Méthodologie`, `Management`, `Droit`, `Économie`, `Comptabilité et gestion`, `Communication`, `Marketing`, `Informatique` — 11 matières, orthographe exacte. `Marketing` est bien une matière de la filière, mais la répartition demandée pour les trois lots ne lui attribue aucun chapitre : les 60 fiches couvrent les 10 autres matières.

---

## 1. Carte des chapitres — vue d'ensemble

| Unité officielle / domaine | Matières FicheLab | Préfixes |
|---|---|---|
| U1 · Culture générale et expression | `Français`, `Communication` | `PF1.`–`PF4.`, `CO1.`–`CO4.` |
| U2 · Langue vivante 1 (anglais) | `Anglais professionnel` | `AN1.`–`AN4.` |
| U3 · Mathématiques | `Maths / stats` | `MS1.`–`MS8.` |
| U4 · Étude et conception de réseaux (IR) | `Informatique` | `IN1.`, `IN2.` |
| U5 · Exploitation et maintenance de réseaux (IR) | `Informatique` | `IN3.`–`IN9.` |
| U6 · Valorisation de la donnée et cybersécurité (IR) | `Informatique` | `IN10.`–`IN12.` |
| Enseignement général transversal | `Méthodologie` | `ME1.`–`ME4.` |
| Culture économique, juridique et managériale | `Droit`, `Économie`, `Management`, `Comptabilité et gestion` | `DR1.`–`DR7.`, `EC1.`–`EC7.`, `MA1.`–`MA6.`, `CG1.`–`CG4.` |

## 2. Lot A — `Informatique` (12) et `Maths / stats` (8)

| Matière | Année | Préfixes et chapitres |
|---|---|---|
| `Informatique` | BTS1 | `IN1.` architecture réseau : modèles, topologies et équipements · `IN2.` protocoles TCP/IP : adressage, encapsulation et diagnostic · `IN3.` sécurité des réseaux : risques, modèles et bonnes pratiques · `IN4.` pare-feu et filtrage : règles, zones et journalisation · `IN5.` réseaux privés virtuels (VPN) : tunnels et chiffrement · `IN6.` systèmes d'exploitation : processus, mémoire et droits · `IN7.` Linux : système de fichiers, permissions et administration |
| `Informatique` | BTS2 | `IN8.` virtualisation : hyperviseurs, machines virtuelles et ressources · `IN9.` supervision et exploitation : métriques, alertes et journaux · `IN10.` cryptographie : chiffrement, hachage et signature · `IN11.` gestion des identités et des accès : IAM, MFA et annuaires · `IN12.` cyberdéfense : détection, réponse à incident et retour d'expérience |
| `Maths / stats` | BTS1 | `MS1.` calcul littéral et algèbre : identités et factorisation · `MS2.` fonctions et représentations graphiques · `MS3.` statistiques descriptives : résumer et interpréter un jeu de données · `MS4.` probabilités et échantillonnage : modéliser l'aléa |
| `Maths / stats` | BTS2 | `MS5.` suites numériques et intérêts composés · `MS6.` mathématiques financières : emprunts et tableaux d'amortissement · `MS7.` dérivation et optimisation : étude des variations · `MS8.` intervalles de confiance et tests d'hypothèses |

## 3. Lot B — `Droit` (7), `Économie` (7), `Management` (6)

| Matière | Année | Préfixes et chapitres |
|---|---|---|
| `Droit` | BTS1 | `DR1.` cyberdroit : principes juridiques du numérique · `DR2.` RGPD : principes, rôles et obligations de conformité · `DR3.` propriété intellectuelle et logicielle |
| `Droit` | BTS2 | `DR4.` droit des technologies et contrats numériques · `DR5.` responsabilité civile et pénale dans le numérique · `DR6.` contrats, marchés publics et achats informatiques · `DR7.` réglementation NIS, NIS2 et sécurité des réseaux essentiels |
| `Économie` | BTS1 | `EC1.` économie du numérique : acteurs, valeurs et modèles · `EC3.` emploi, compétences et formation dans le numérique |
| `Économie` | BTS2 | `EC2.` coûts, rentabilité et tableau de bord d'un SI · `EC4.` conjoncture, inflation et décisions d'investissement · `EC5.` économie des plateformes et modèles multimodaux · `EC6.` commerce électronique et valorisation des données clients · `EC7.` financement de l'innovation et arbitrage des projets SI |
| `Management` | BTS1 | `MA1.` gestion de projet informatique : cycle et pilotage · `MA2.` gouvernance de la sécurité des systèmes d'information · `MA3.` management d'une équipe technique et conduite de réunion |
| `Management` | BTS2 | `MA4.` audit et conformité des systèmes d'information · `MA5.` conduite de crise et gestion des incidents cyber · `MA6.` veille technologique et pilotage des risques émergents |

## 4. Lot C — `Français` (4), `Anglais professionnel` (4), `Communication` (4), `Méthodologie` (4), `Comptabilité et gestion` (4)

| Matière | Année | Préfixes et chapitres |
|---|---|---|
| `Français` | BTS1 | `PF1.` synthèse de documents : méthode et restitution · `PF2.` analyse de situation et argumentation écrite |
| `Français` | BTS2 | `PF3.` expression écrite professionnelle : note, courriel et compte rendu · `PF4.` culture générale et expression : enjeux numériques et société |
| `Anglais professionnel` | BTS1 | `AN1.` comprendre un document technique en anglais · `AN2.` lexique technique : réseaux, systèmes et cybersécurité |
| `Anglais professionnel` | BTS2 | `AN3.` écrire un courriel et un rapport d'incident en anglais · `AN4.` présentation technique et soutenance en anglais |
| `Communication` | BTS1 | `CO1.` communication professionnelle et relation client · `CO2.` communication écrite et numérique en équipe |
| `Communication` | BTS2 | `CO3.` animer une réunion et communiquer à l'oral · `CO4.` gestion des conflits et communication de crise |
| `Méthodologie` | BTS1 | `ME1.` analyser une situation professionnelle : méthode en 4 étapes · `ME2.` résolution de problème et outils d'amélioration continue |
| `Méthodologie` | BTS2 | `ME3.` recherche documentaire et évaluation des sources · `ME4.` préparer et réussir sa soutenance de projet |
| `Comptabilité et gestion` | BTS1 | `CG1.` comptabilité générale : bilan et compte de résultat · `CG2.` coûts et contrôle de gestion appliqués à l'informatique |
| `Comptabilité et gestion` | BTS2 | `CG3.` budget prévisionnel et suivi budgétaire d'un projet SI · `CG4.` analyse financière et indicateurs de performance |

**Total par année : BTS1 = 29 fiches, BTS2 = 31 fiches.**

---

## 5. Méthode — 4 étapes

1. **Cadrer le référentiel.** Lire `SOURCES.md`, le modèle `FICHE-PROTOTYPE.md`, `BTSMCO-PROGRAMME.md`, `BTSCI-PROGRAMME.md`, `data/fixtures.py` et `data/gen_generale_modele.py` ; relever les matières exactes du questionnaire (`index.html`, `matieresPour()`), les années (`BTS1`/`BTS2`) et l'identifiant `bts-ciel` ; vérifier les arrêtés et BO sur Légifrance/éduscol.
2. **Rédiger la carte et les lots.** Écrire `BTSCIEL-PROGRAMME.md`, puis décliner chaque chapitre dans `gen_btsciel_A.py`, `gen_btsciel_B.py`, `gen_btsciel_C.py` (mécanique commune dans `_btsciel_common.py`) : **12 points**, **10 questions** (8 QCM + 2 texte), **7 blocs en ordre strict** `intro, formule, grille, liste, etapes, attention, exemples`, **3 schémas via `diag()`**, source officielle et titre unique préfixé.
3. **Valider à la génération.** Exécuter chaque générateur : `fixtures.valider_et_ecrire` contrôle la structure, les corrections, l'ordre des blocs, le XML des SVG, les coordonnées de texte, les artefacts CJK et les doublons de titres du lot.
4. **Contrôler en croisé et auditer.** Comparer les 3 JSON réunis (titres, préfixes, matières, années, compteurs), vérifier l'absence de CJK et de SVG interdit, puis consigner les résultats dans `AUDIT-BTSCIEL.md`.

La même logique sert à la révision du BTS : lire les 12 points, refaire les calculs et les QCM, revoir les 3 schémas, puis repasser le questionnaire.

## 6. Suivi de la déclinaison

| Lot | Générateur | JSON | Matières | Fiches | Statut |
|---|---|---|---|---|---|
| A | `data/gen_btsciel_A.py` | `data/btsciel-mat-part-A.json` | Informatique (12), Maths / stats (8) | 20 | ✅ généré et validé |
| B | `data/gen_btsciel_B.py` | `data/btsciel-mat-part-B.json` | Droit (7), Économie (7), Management (6) | 20 | ✅ généré et validé |
| C | `data/gen_btsciel_C.py` | `data/btsciel-mat-part-C.json` | Français (4), Anglais professionnel (4), Communication (4), Méthodologie (4), Comptabilité et gestion (4) | 20 | ✅ généré et validé |

**Déclinaison terminée : 60 fiches, 720 points de cours, 600 questions corrigées (480 QCM + 120 texte), 180 schémas SVG.** Contrôle détaillé : [`AUDIT-BTSCIEL.md`](AUDIT-BTSCIEL.md). `index.html`, `inject_app.py` et `audit_filieres.py` n'ont pas été modifiés.
