# Audit FicheLab — filière `bts-sio`

Audit de production de la filière **BTS Services informatiques aux organisations** (57 125 vœux Parcoursup 2026, 8ᵉ BTS le plus demandé), référentiel **arrêté du 6 mai 2013 modifié** (JORF n° 0110 du 11 mai 2013, BO), options **SISR** et **SLAM**, programmes d'enseignement général et ressources éduscol. Voir [`BTSSIO-PROGRAMME.md`](BTSSIO-PROGRAMME.md) et [`SOURCES.md`](SOURCES.md) §1.

## 1. Compteurs

| Lot | Générateur | JSON | Fiches | Points | Questions | QCM | Textes | SVG |
|---|---|---|---|---|---|---|---|---|
| A | `data/gen_btssio_A.py` | `data/btssio-mat-part-A.json` | 20 | 240 | 200 | 160 | 40 | 60 |
| B | `data/gen_btssio_B.py` | `data/btssio-mat-part-B.json` | 20 | 240 | 200 | 160 | 40 | 60 |
| C | `data/gen_btssio_C.py` | `data/btssio-mat-part-C.json` | 20 | 240 | 200 | 160 | 40 | 60 |
| **Total** | **3** | **3** | **60** | **720** | **600** | **480** | **120** | **180** |

Validation à la génération, sans erreur ni avertissement de `fixtures.valider_et_ecrire` :

```
OK btssio-mat-part-A.json : 20 fiches, 240 points, 200 questions, 60 SVG
OK btssio-mat-part-B.json : 20 fiches, 240 points, 200 questions, 60 SVG
OK btssio-mat-part-C.json : 20 fiches, 240 points, 200 questions, 60 SVG
```

## 2. Répartition par matière, préfixe et année

| Matière (orthographe exacte du questionnaire BTS) | Fiches | Préfixes | BTS1 | BTS2 |
|---|---|---|---|---|
| `Informatique` | 12 | `IN1.`–`IN12.` | 5 | 7 |
| `Maths / stats` | 8 | `MS1.`–`MS8.` | 4 | 4 |
| `Droit` | 7 | `DR1.`–`DR7.` | 3 | 4 |
| `Économie` | 7 | `EC1.`–`EC7.` | 3 | 4 |
| `Management` | 6 | `MA1.`–`MA6.` | 3 | 3 |
| `Français` | 4 | `PF1.`–`PF4.` | 2 | 2 |
| `Anglais professionnel` | 4 | `AN1.`–`AN4.` | 2 | 2 |
| `Communication` | 4 | `CO1.`–`CO4.` | 2 | 2 |
| `Méthodologie` | 4 | `ME1.`–`ME4.` | 2 | 2 |
| `Comptabilité et gestion` | 4 | `CG1.`–`CG4.` | 1 | 3 |

Total par année : **BTS1 = 27 fiches**, **BTS2 = 33 fiches**. Toutes les fiches ont `filieres == ["bts-sio"]` (60/60) et des années strictement dans `['BTS1']` ou `['BTS2']`. Les matières sont exactement celles du questionnaire, sans variante orthographique ni matière supplémentaire (`Marketing` fait partie du questionnaire mais n'est pas décliné dans le périmètre des trois lots demandés).

## 3. Contenu des lots

- **Lot A** — `IN1.` à `IN12.` : réseaux et télécommunications, systèmes d'exploitation, sécurité SI, administration des serveurs, virtualisation, scripts Bash/PowerShell, bases de données et SQL, développement web, Python, génie logiciel, options SISR/SLAM, cybersécurité et gestion d'incident. `MS1.` à `MS8.` : calcul, fonctions, statistiques descriptives, probabilités, échantillonnage, suites, mathématiques financières, corrélation/régression.
- **Lot B** — `DR1.` à `DR7.` : droit des affaires, contrats, concurrence/consommation, droit social, propriété intellectuelle et logicielle, RGPD, cybercriminalité. `EC1.` à `EC7.` : offre/demande, coûts, conjoncture, monnaie, emploi, mondialisation, économie numérique. `MA1.` à `MA6.` : gestion de projet, management d'équipe, conduite du changement, qualité, AMOA, pilotage.
- **Lot C** — `PF1.` à `PF4.` : synthèse, essai, expression écrite professionnelle, culture générale numérique. `AN1.` à `AN4.` : compréhension technique, lexique, mail/compte rendu, expression orale. `CO1.` à `CO4.` : écoute et feedback, écrit numérique, réunion/présentation, communication de crise. `ME1.` à `ME4.` : étude de cas, veille, soutenance, résolution de problème. `CG1.` à `CG4.` : bilan et compte de résultat, coûts, budget, trésorerie et BFR.

## 4. Contrôles structurels

| Contrôle | Résultat | Attendu | Verdict |
|---|---|---|---|
| Points par fiche | 12 sur 60 fiches | 12 | ✅ |
| Questions par fiche | 10 sur 60 fiches | 9–10 | ✅ |
| QCM / texte par fiche | 8 / 2 sur 60 fiches | ≥ 6 / ≥ 2 | ✅ |
| Correction renseignée | 600 / 600 | toutes | ✅ |
| Blocs par fiche | 7 sur 60 fiches | 7 | ✅ |
| Ordre des blocs | 1 seule variante : `intro, formule, grille, liste, etapes, attention, exemples` | strict | ✅ |
| Schémas par fiche | 3 sur 60 fiches | 2–4 | ✅ |
| Fiches avec source officielle (arrêté du 6 mai 2013, BO, éduscol, unité/option) | 60 / 60 | toutes | ✅ |
| Préfixes uniques et séries complètes | 60/60, `IN1`–`IN12`, `MS1`–`MS8`, etc. | 60 | ✅ |
| Doublons de titres (intra, inter lots, cross-JSON) | 0 | 0 | ✅ |
| Artefacts CJK | 0 | 0 | ✅ |

## 5. Schémas SVG

- **180 schémas**, tous produits par `diag()` à partir des blocs (`svg_grille`, `svg_flux`, `svg_etapes`, `svg_compare`).
- **180/180** analysables en XML via `xml.etree.ElementTree.fromstring`, sans erreur de parsing.
- Aucun `<script>`, gestionnaire `on*`, `javascript:` ni `<foreignObject>` : contrôle `INTERDIT_SVG` de `fixtures.py` (0 occurrence).
- Toutes les coordonnées de texte sont dans le `viewBox` : contrôle automatique de `fixtures.valider_fiche` (0 texte hors cadre).

## 6. Doublons et cohérence croisée

- Vérification effectuée sur les trois JSON réunis **et** par rapport aux autres fichiers JSON prototypes du répertoire `data/` : **0 doublon de titre**.
- **0 doublon de préfixe** : chaque série est complète et contiguë de 1 à son maximum.
- Aucune chaîne CJK (chinois/japonais) détectée dans les 60 fiches sérialisées.
- Tous les scripts importent `fixtures.py` et respectent le modèle `gen_generale_modele.py` (12 points, 10 questions, 7 blocs ordonnés, 3 `diag()`, `valider_et_ecrire`).
- `index.html`, `inject_app.py` et `audit_filieres.py` n'ont **pas** été modifiés. L'injection n'a pas été lancée : `inject_app.py` découvre automatiquement les fichiers `*-mat-part-*.json`, donc les trois nouveaux JSON seront intégrés lors de la prochaine injection par l'orchestrateur.
- Aucun outil de délégation exposé dans ce harnais : les trois lots ont été produits directement, puis contrôlés lot par lot et de manière croisée.

## 7. Verdict

**AUDIT CONFORME.** La filière `bts-sio` dispose de ses 60 fiches complètes, structurées et validées : 720 points de cours, 600 questions corrigées, 180 schémas SVG. Aucun doublon, aucun artefact CJK, aucun SVG invalide, aucun bloc hors ordre, aucune matière ou année hors périmètre.

*Réserve documentaire sans incidence sur les données : le référentiel fondateur retenu est l'arrêté du 6 mai 2013 modifié (et non une date plus récente) ; les modifications successives et les programmes d'enseignement général sont couverts par la mention « modifié (BO) » et par les références éduscol figurant dans les 60 champs `source`.*
