# Audit de certification approfondi — Filière BTS BIOALC (`bts-bio`)

> **Objet** : vérification exhaustive de la filière BIOALC dans FicheLab.
> **Racine auditée** : `fichelabs/fichelab/` — **lecture seule** (aucun fichier applicatif ni document modifié).
> **Méthode** : extraction et évaluation des constantes JS de `index.html` avec Node.js (contexte reconstruit identique à `fichesPour()`), validation XML des 301 schémas avec Python `ElementTree`, analyse croisée des 6 documents de référence, `node --check` sur le script complet.
> **Date** : 24 novembre 2026.

---

## 1. Tableau des contrôles

| # | Contrôle | Attendu | Constaté | Statut |
|---|----------|---------|----------|--------|
| a.1 | `EXTRA_FICHES` extractible (L923) | présent | 1 335 fiches, JSON valide | **OK** |
| a.2 | `ANNALES_BIB` (L936), `ANNALES_REELLES` (L1324) | présentes | 60 / 12 entrées | **OK** |
| a.3 | `PROTO_FILIERES`, `FICHE_UV`, `fichesPour`, `estPrototype`, `renderBlocs`, `svgSur`, `questionsPour`, `annalesReellesPour`, migrations | présents | tous présents (L939, L787, L940, L938, L1184, L1676, L1590, L1327, L1844) | **OK** |
| b.1 | Prototypes `bts-bio` dans `EXTRA_FICHES` | 96 + 15 CG = **111** | 96 de base + 15 `Contrôle PC ·` = **111** | **OK** |
| b.2 | Prototypes réellement servis par `fichesPour()` | 111 (cohérence attendue) | **112** (97 base + 15 CG) — `FICHE_UV` s'ajoute | **ÉCART** |
| b.3 | Répartition BTS1/BTS2 (`EXTRA_FICHES`) | cohérente | 58 BTS1 / 69 BTS2 (visibles) | **OK** |
| b.4 | Répartition servie | 58 / 69 | **59 / 70** | **ÉCART** |
| b.5 | Aucune fiche « texte brut » `bts-bio` dans le catalogue | 0 | **6** dans `MODELES` (L562, L587, L612, L619, L626, L633) | **ÉCART** |
| b.6 | Unicité des titres (exacte + normalisée) | 0 doublon | 0 doublon sur 112 | **OK** |
| b.7 | 9 champs renseignés | 112/112 | 112/112 (`filiers`, `annees`, `matiere`, `titre`, `source`, `points`, `affichage`, `schema`, `questions`) | **OK** |
| b.8 | 7 blocs en ordre strict | 112/112 | 112/112 (`intro, formule, grille, liste, etapes, attention, exemples`) | **OK** |
| b.9 | 2–3 schémas SVG par fiche, valides | 2–4 | 301 SVG, 100 % XML valide, 0 script/`on*`/`javascript:` réel | **OK** |
| b.10 | Questions : type/options/correct/correction/contexte-calcul | 0 erreur | 1 071 questions, 0 erreur structurelle ; 206 `contexte`, 205 `calcul` | **OK** |
| b.11 | Sources renseignées sur les fiches | 112/112 | 112/112 | **OK** |
| b.12 | Aucun CJK | 0 | 0 (titres, sources, points, blocs, questions, SVG) | **OK** |
| c.1 | 15 chapitres « Contrôle groupé PC » | 15 | 15 | **OK** |
| c.2 | 6 thèmes « hors programme » exclus | 0 présent | 0 présent (liste L1067) | **OK** |
| c.3 | `renderControle()` + handlers `data-cgouvrir` / `data-cgquizz` | présents | L1065, L1083–L1084, L1706–L1708 | **OK** |
| c.4 | `questionsPour('controle')` | fonctionnel | L1594–L1597, 135 questions disponibles | **OK** |
| c.5 | Contrôle groupé 20 questions câblé | présent | L1074, L1087–L1088 (`nbQ=20`) | **OK** |
| c.6 | 15 chapitres visibles pour chaque profil BIOALC | 15 | **BTS1 : 8 / BTS2 : 15** (7 fiches marquées BTS2 uniquement) | **ÉCART** |
| d.1 | 23 annales `bts-bio` | 21 `genere` + 2 `officiel` | 21 + 2 | **OK** |
| d.2 | ≥ 6 vrais examens `filieres:["bts-bio"]` | ≥ 6 | **12** | **OK** |
| d.3 | Filtrage par profil | actif | `annalesReellesPour()` L1327 | **OK** |
| d.4 | Aucune fuite BIOALC vers autres profils | 0 fuite | 0 fuite (aucun sujet sans `filieres`, aucun mixte) | **OK** |
| d.5 | Source renseignée sur les annales générées | 23/23 | **2/23** (21 annales `genere` sans `source`) | **ÉCART** |
| e.1 | `ANCIENS_PAR_FILIERE["bts-bio"]` | 79 clés | 79 clés, 0 doublon, 0 collision avec fiches actuelles | **OK** |
| e.2 | Filtre prototype | actif | L947 `PROTO_FILIERES.has(...) && estPrototype(m)` | **OK** |
| e.3 | Ajout automatique des nouvelles fiches | actif | L1862–L1865 (déduplication `titre||source`) | **OK** |
| e.4 | Nettoyage des textes bruts | effectif | L1848 effectif sur `D.fiches`, mais **6 textes bruts du catalogue `MODELES` non couverts** | **ÉCART** |
| f.1 | Couverture référentiel (114 points contrôlés) | 0 chapitre manquant | **0 manquant** (faux positif « environnement » dû à l'apostrophe typographique, vérifié) | **OK** |
| f.2 | U4 physique-chimie | 18/18 | **19 fiches servies** (18 attendues + viscosité) | **ÉCART (doc)** |
| f.3 | U1/U2/U3/U5/U6/U7/U8/biochimie/microbio/moléculaire/bioindustries | couvert | couvert | **OK** |
| g.1 | Cohérence des chiffres documentaires | identiques | **5 documents contradictoires** (voir A-05) | **ÉCART** |
| h.1 | `node --check` sur le script extrait | OK | **OK** (exit 0, script 17 106 792 octets) | **OK** |

**Synthèse du tableau : 27 contrôles OK / 8 ÉCART (35 contrôles).**

---

## 2. Anomalies détaillées

### CRITIQUE — aucune

Aucun défaut bloquant : syntaxe JS valide, 301 SVG XML-valides et sans contenu exécutable, aucune fuite d'examen BIOALC vers un autre profil, aucune donnée corrompue.

### ÉLEVÉ

**A-01 — Six fiches « texte brut » `bts-bio` subsistent dans le catalogue**
- **Localisation** : `index.html`, catalogue `MODELES` (L270–L640), fiches aux lignes **L562, L587, L612, L619, L626, L633** ; présentes aussi dans `TOUT` utilisé par `fichesPour()` (L944).
- **Titres** :
  1. `Génétique : ADN, gènes et mutations` (L562, `filiers:["lic-svt","pass","bts-bio"]`)
  2. `Les enzymes et la cinétique enzymatique` (L587, `["pass","infirmier","bts-bio"]`)
  3. `Les dilutions et le calcul de concentration` (L612, `["bts-bio","pass"]`)
  4. `L'antibiogramme et l'interprétation des souches` (L619, `["bts-bio"]`)
  5. `La numération formule sanguine (NFS)` (L626, `["bts-bio"]`)
  6. `La norme ISO 17025 en laboratoire` (L633, `["bts-bio"]`)
- **Constat** : aucune n'a `affichage` ni `schema` (4 points, 2 questions) ; aucune de leurs clés `titre||source` n'est dans `ANCIENS_PAR_FILIERE["bts-bio"]` (vérification croisée : 0 correspondance, y compris par titre seul).
- **Impact** : le contrat « aucune fiche texte brut `bts-bio` dans le catalogue » n'est pas respecté. L'impact utilisateur est atténué par le filtre L947 (elles ne sont jamais servies au profil `bts-bio`), mais 3 d'entre elles sont **exclusivement `bts-bio`** et constituent du code/data mort. Le document `BIOALC-PROGRAMME.md` L158 affirme pourtant que « les anciennes fiches texte brut du catalogue sont filtrées à la génération et retirées du stockage local » : le retrait du *catalogue source* n'a pas eu lieu.

**A-02 — Le profil BTS1 ne voit que 8 des 15 chapitres du « Contrôle groupé PC »**
- **Localisation** : `index.html` L923 (`EXTRA_FICHES`), fiches `Contrôle PC · 9` à `Contrôle PC · 15` ; `cgFiches()` L1057–L1064 ; `fichesPour()` filtre d'année L948 ; `renderControle()` L1065–L1086.
- **Constat** : les fiches 1–8 ont `annees:["BTS1","BTS2"]`, les fiches 9–15 ont `annees:["BTS2"]` uniquement. Le migration L1864 n'ajoute dans `D.fiches` que les fiches renvoyées par `fichesPour(D.profil)`, donc un profil BTS1 reçoit 8 fiches CG ; `renderControle()` affiche alors dynamiquement « 8 chapitres » et le contrôle de 20 questions ne tire que de 72 questions (8 × 9).
- **Impact** : `CONTROLE-GROUPE-PC.md` L15/L37 annonce « 15 chapitres » pour la rubrique. Un étudiant BTS1 préparant la même partiale n'a pas accès à cinétique, équilibres K°, pKa, nucléophile/électrophile, projection de Fischer. À confirmer comme choix pédagogique assumé ou à corriger.

### MOYEN

**A-03 — Un 112ᵉ prototype servi, absent de tous les totaux documentés**
- **Localisation** : `index.html` L787–L902 (`const FICHE_UV`, `filiers:['bts-bio']` L788), ajouté à `TOUT` en L944.
- **Constat** : `EXTRA_FICHES` contient exactement 111 prototypes `bts-bio` (96 base + 15 CG), conformément à l'attendu. Mais `FICHE_UV` (« Spectroscopie UV-visible et loi de Beer-Lambert », 7 blocs, 4 schémas, 10 questions, 12 points) est un prototype supplémentaire injecté séparément. Totaux réellement servis : **112 fiches (59 BTS1 / 70 BTS2), 301 SVG, 1 071 questions, 1 273 points**. Totaux `EXTRA_FICHES` seuls : 111 fiches, 297 SVG, 1 061 questions. Totaux historiques documentés : 96 fiches, 252 SVG, 926 questions (soit exactement `EXTRA_FICHES` hors CG, `FICHE_UV` exclu).
- **Impact** : l'incertitude sur la périmétrie (`EXTRA_FICHES` vs catalogue servi) rend les chiffres de certification invérifiables. La fiche UV est comptée dans « 18/18 phys-chim » de `BIOALC-PROGRAMME.md` L164, alors qu'`EXTRA_FICHES` contient déjà 18 fiches phys-chim hors UV + viscosité, soit **19 fiches servies en U4**.

**A-04 — 21 annales générées `bts-bio` sans source**
- **Localisation** : `index.html` L936 (`ANNALES_BIB`), toutes les entrées `type:"genere"` de la filière.
- **Constat** : 23 annales `bts-bio` = 2 `officiel` (avec URL Aix-Marseille) + 21 `genere`. Les 21 `genere` ont les clés `filieres, annees, titre, matiere, type, contenu, correction` mais **aucune clé `source`** (2/23 seulement en ont une). Le phénomène est global (58/60 annales sans source), mais il concerne 21 annales de la filière certifiée.
- **Impact** : la « règle d'or » répétée dans `README.md` L10/L16 et `BIOALC-PROGRAMME.md` L173 (« chaque information générée démarre à vérifier avec sa source ») n'est pas respectée pour ces annales. Exemple : `Sujet type E7-U7 – La vinification : contrôles qualité (inspiré de la session 2024)` — la mention « inspiré de la session 2024 » est dans le titre, pas dans un champ `source` exploitable.

**A-05 — Chiffres documentaires contradictoires sur la filière**
- **Localisations et écarts** :
  | Document | Ligne | Annoncé | Réel |
  |---|---|---|---|
  | `README.md` | L16 | 96 fiches (50 BTS1 / 54 BTS2) | 97 de base servies (51/54 + UV commune) ; 112 au total avec CG |
  | `README.md` | L40 | 96 fiches / 252 SVG / 926 questions | 97 / 256 / 936 pour le socle servi (hors CG) ; 112 / 301 / 1 071 avec CG |
  | `SOURCES.md` | L81 | 51 BTS1 / 55 BTS2, 96 fiches | 59 / 70 servis, 112 fiches |
  | `AUDIT-FILIERES.md` | L21 | 111 prototypes (58 BTS1 / 69 BTS2) | exact pour `EXTRA_FICHES` ; 112 (59/70) pour le catalogue servi |
  | `BIOALC-PROGRAMME.md` | L149 | BTS1 : 11 fiches / BTS2 : 8 | 59 / 70 |
  | `BIOALC-PROGRAMME.md` | L160, L169, L171 | 96 fiches, 51/55, 252 SVG | 97 socle / 112 total, 59/70, 301 SVG |
  | `CONTROLE-GROUPE-PC.md` | L15, L37 | 15 chapitres pour la rubrique | 15 pour BTS2, 8 pour BTS1 (cf. A-02) |
- **Constat** : les chiffres 96/252/926 correspondent à un état antérieur (`EXTRA_FICHES` hors CG et hors `FICHE_UV`) ; 111/58/69 correspondent à `EXTRA_FICHES` après ajout des 15 fiches CG ; 51/55 correspondent au socle + `FICHE_UV`. Les trois conventions coexistent sans être nommées.
- **Impact** : un contrôle de certification ne peut pas déterminer quel chiffre fait foi. Les lignes `README.md` L16 (« 994 fiches prototype, 2 946 schémas, 9 172 questions ») et `AUDIT-FILIERES.md` L10/L13/L14 ne sont pas non plus recalculées après l'ajout des 15 fiches CG.

### FAIBLE

**A-06 — Double numérotation dans 7 titres de fiches CG**
- **Localisation** : `index.html` L923, fiches `Contrôle PC · 9 · …` à `Contrôle PC · 15 · …`.
- **Constat** : le préfixe `Contrôle PC ·` est déjà un numéro d'ordre dans la liste ; les fiches 9–15 répètent leur numéro juste après (`Contrôle PC · 12 · Favoriser le sens direct…`). L'affichage `renderControle()` L1080 et le libellé d'examen L1614 retirent le préfixe, donc l'utilisateur voit `12 · Favoriser…` : l'impact est nul à l'écran, mais les données brutes sont incohérentes avec les fiches 1–8.

**A-07 — Regex de sanitisation SVG imparfaite (observation hors périmètre BIOALC)**
- **Localisation** : `index.html` L1682, fonction `svgSur()`.
- **Constat** : le motif `/\b(href|xlink:href)\s*=\s*(['"])\s*javascript:[^\2]*\2/gi` utilise `\2` **dans une classe de caractères** (`[^\2]`), où il est interprété comme le code U+0002 et non comme une référence arrière. La correspondance peut donc engloutir le guillemet fermant. Aucun SVG BIOALC ne contient de `javascript:` (contrôle : 0 occurrence), donc l'impact est nul pour la filière ; signalé pour robustesse de l'import JSON.
- **Note de rigueur** : notre détecteur de motifs interdits a produit **1 faux positif** sur `Contrôle PC · Topologie : nommer ou dessiner une molécule` (schéma #0) : la chaîne `Hexagone = 6 C` matchait `/on[a-z]+\s*=/` via le fragment « **one =** ». Après vérification du contexte, **0 motif interdit réel** dans les 301 SVG.

---

## 3. Verdict final

> ## **NON CONFORME**

La filière BIOALC est **techniquement saine** (données, schémas, questions, annales, migrations, syntaxe : 27 contrôles OK sur 35) mais **non certifiable en l'état** en raison de deux écarts ÉLEVÉ (résidus de fiches texte brut dans le catalogue ; couverture incomplète du contrôle groupé pour BTS1) et de trois écarts MOYEN (comptage 112 vs 111, annales générées sans source, documentation contradictoire).

**Dénombrement des anomalies :**

| Gravité | Nombre |
|---|---|
| CRITIQUE | 0 |
| ÉLEVÉ | 2 |
| MOYEN | 3 |
| FAIBLE | 2 |
| **Total** | **7** |

---

## 4. Recommandations actionnables

### Priorité 1 — avant toute certification
1. **A-01** : retirer du catalogue `MODELES` (`index.html` L562, L587, L612, L619, L626, L633) les 6 fiches texte brut, ou retirer `bts-bio` de leur tableau `filiers` pour les 3 partagées avec `pass`/`infirmier`/`lic-svt` (L562, L587, L612). Ajouter les 3 fiches `bts-bio`-only (L619, L626, L633) aux clés `ANCIENS_PAR_FILIERE["bts-bio"]` (L1843) pour purger les `localStorage` existants.
2. **A-02** : décider explicitement du périmètre BTS1. Si les chapitres 9–15 doivent être révisés en BTS1, passer leur `annees` à `["BTS1","BTS2"]` dans les 7 fiches concernées (L923) ; sinon, modifier `CONTROLE-GROUPE-PC.md` L15/L37 pour annoncer « 15 chapitres (8 en BTS1, 15 en BTS2) » et adapter `renderControle()` L1070.

### Priorité 2 — avant prochaine publication
3. **A-03 / A-05** : choisir une convention de comptage unique et la documenter en tête de `AUDIT-FILIERES.md` et `README.md`. Suggestion : `socle = EXTRA_FICHES hors Contrôle PC (96)` ; `catalogue = socle + FICHE_UV (97)` ; `servi = catalogue + CG (112)`. Mettre à jour `AUDIT-FILIERES.md` L10/L13/L14/L21, `README.md` L16/L40, `SOURCES.md` L79/L81, `BIOALC-PROGRAMME.md` L149/L160/L169/L171 avec les trois niveaux et les totaux servis (**112 fiches / 301 SVG / 1 071 questions / 23 annales / 15 chapitres CG**).
4. **A-04** : ajouter un champ `source` aux 21 annales `genere` de `ANNALES_BIB` (L936), même minimal (« Sujet type construit à partir du référentiel BIOALC 2024/2025, arrêté du 12 mars 2024 modifié le 24 juin 2025 — à vérifier »), pour respecter la règle d'or.

### Priorité 3 — nettoyage
5. **A-06** : normaliser les 7 titres `Contrôle PC · N · …` en `Contrôle PC · …` (L923) ; la numérotation est déjà portée par l'ordre d'affichage.
6. **A-07** : corriger `svgSur()` L1682 en `...[^'"]*\\2...` ou en utilisant un callback de remplacement, puis ajouter un test unitaire avec un SVG hostile (`<svg><a href="javascript:alert(1)">…`).
7. Ajouter un contrôle automatique de non-régression dans `data/audit_filieres.py` : échec si une fiche `bts-bio` du catalogue n'est pas prototype, si le total servi diffère du total documenté, ou si une annale `genere` n'a pas de `source`.

---

*Rapport produit en lecture seule. Aucun fichier applicatif ou document n'a été modifié.*
