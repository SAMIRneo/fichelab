# État des lieux — reprise (23 novembre 2026)

## Ce qui est terminé et intégré dans l'appli

**4 filières converties au format prototype** (7 blocs + schémas SVG), audit global CONFORME :

| Filière | Fiches | Points | Questions | SVG | Doc programme |
|---|---:|---:|---:|---:|---|
| `bts-bio` (BTS BIOALC) | 96 | 1 081 | 926 | 252 | `fichelab/BIOALC-PROGRAMME.md` |
| `generale` (voie générale) | 95 | 1 140 | 895 | 285 | `fichelab/GENERALE-PROGRAMME.md` |
| `bts-mco` | 82 | 984 | 742 | 246 | `fichelab/BTSMCO-PROGRAMME.md` |
| `pass` | 62 | 744 | 558 | 186 | `fichelab/PASS-PROGRAMME.md` |

**Cumul : 335 fiches prototype, 969 schémas SVG, 3 121 questions corrigées, 0 doublon de titre, 0 anomalie.** Détail dans `fichelab/AUDIT-FILIERES.md`.

## Outillage installé (dans `fichelab/data/`)

- `fixtures.py` — bibliothèque de génération + validateur (`fiche`, `qcm`, `qt`, `diag`, `svg_grille`, `svg_flux`, `svg_etapes`, `svg_compare`, `bloc`, `valider_fiche`, `valider_et_ecrire`).
- `gen_generale_modele.py` — fiche-modèle validée, à copier pour toute nouvelle filière.
- `inject_app.py` — reconstruit `EXTRA_FICHES`, met à jour `PROTO_FILIERES`, le filtre, les migrations et le nettoyage des fiches texte brut. **Générique** : repère automatiquement tous les `*-mat-part-*.json` (hors BIOALC déjà intégré et hors `-MODELE.json`).
- `audit_filieres.py` — audit complet (structure, blocs, SVG, CJK, doublons, syntaxe JS via `node --check`, couverture par filière/année, vrais examens filtrés). Écrit `AUDIT-FILIERES.md`.
- `_audit_contenu.py` — contrôle qualitatif complémentaire (longueurs, placeholders, variété des SVG et des sources).

## Avancement du 24 novembre 2026 (fin de journée)

**9 filières intégrées et auditées** : `bts-bio` (96), `generale` (95), `bts-mco` (82), `pass` (62), `lic-droit` (60), `infirmier` (62), `but-tc` (50), `cpge-mpsi` (56), `bts-ndrc` (60) = **623 fiches prototype**, 1 833 SVG, 5 773 questions, audit CONFORME.

**Nouveauté produit** : rubrique « 🧪 Contrôle groupé » pour le profil `bts-bio`, avec les **15 chapitres** communiqués par l'étudiant (captures WhatsApp du 19/11) — 15 fiches (`data/bioalc-cg-part-A.json` 8 + `-B.json` 7), 135 questions, 45 SVG. Fiches, quizz par chapitre et contrôle de 20 questions via le moteur d'examen existant. Doc : `fichelab/CONTROLE-GROUPE-PC.md`.

**GitHub** : dépôt `SAMIRneo/fichelab`, site https://samirneo.github.io/fichelab/ — dernier commit `35e702e` poussé.

## En cours (reprise du 24 novembre 2026)

Les 5 responsables lancés la veille avaient produit des lots partiels valides avant d'être annulés. Ils ont été **relancés le 24/11 avec des consignes de reprise** (ne pas refaire l'existant, compléter uniquement les lots manquants).

| Session responsable (reprise) | Filière | Déjà validé | Reste à produire |
|---|---|---|---|
| `ses_df3641fb4ffeMDJaRJO6HMhxYx` | `infirmier` | prog. + A(20) + B(22) | C(~20) + audit |
| `ses_df3641fb3ffePIrYGixDZ4QZJx` | `lic-droit` | **TERMINÉ** : prog. + A(20) + B(20) + C(20) = 60 fiches, audit | ✅ intégré dans l'appli |
| `ses_df3641fb1ffeetE8CmmT3MRKvY` | `but-tc` | prog. + A(20) + B(10) | C(~20) + audit |
| `ses_df3641faaffe9kA6rBWdbPWjWz` | `cpge-mpsi` | prog. + A(20) | B(~20) + C(~16) + audit |
| `ses_df3641fa9ffeQUFTpg4h6BI6Pp` | `bts-ndrc` | A(20) | programme + B(~20) + C(~20) + audit |

`gen_infirmier_C.py` était incomplet (commentaire final `# __LOT_C_MATHS__`) : à terminer. `buttc-mat-part-B.json` a été régénéré à la reprise (10 fiches valides).

**Découverte importante : l'outil `subagent` n'est PAS disponible dans les sessions enfants.** Le modèle « responsable + équipe » ne peut donc pas être délégué en cascade : chaque responsable produit ses lots lui-même (le coordinateur principal garde la possibilité de lancer plusieurs responsables en parallèle). Le modèle reste néanmoins « un responsable par filière », avec programme, lots validés et audit de filière.

**Liste blanche d'intégration** : `inject_app.py` contient `FILIERES_A_INTEGRER` (9 filières terminées). Ajouter chaque nouvelle filière à cette liste au fur et à mesure des rapports (laisser `[]` pour tout intégrer automatiquement).

**6 responsables lancés le 24/11 soir** (3 lots chacun, ~60 fiches par filière) :

| Session | Filière |
|---|---|
| `ses_df3392af7ffeo6cXOVnW47ar0j` | `but-gea` |
| `ses_df3392af6ffe70MdmQfzMxSzPW` | `cpge-pci` |
| `ses_df3392af2ffenmkOcrTmQsbQnP` | `lic-staps` |
| `ses_df3392acfffewyy53PvQ3P2hDy` | `lic-psycho` |
| `ses_df3392acfffdyVmTnhjm4LPxpP` | `lic-eco` |
| `ses_df3392acbffez31L4pITJZak9Q` | `bts-ci` | ✅ TERMINÉ et intégré (60 fiches) |

**Vague suivante lancée le 24/11 (6 responsables, 3 lots chacun)** :

| Session | Filière |
|---|---|
| `ses_df3175e5bffd8pVvRP500bWjWY` | `bts-cg` |
| `ses_df3175e5affeizgyr8wlyNsA3D` | `bts-gpme` |
| `ses_df3175e58ffdnck3lzpov8XnRn` | `lic-maths` |
| `ses_df3175e43ffeCzjdkY34wUeNUT` | `but-info` |
| `ses_df3175e42ffee5MJZ5DvlBIn6Q` | `bts-sio` |
| `ses_df3175e3effezws9CwnnJ9Akhj` | `bts-ciel` |

**État intégré au 24/11 (fin) : 26 filières, ~1 550 fiches prototype, audit CONFORME, GitHub commit `4c05bcc`.** Certification BIOALC profonde faite (`AUDIT-BIOALC-PROFOND.md`, 7 anomalies corrigées + contrôles de non-régression).

**Vague finale lancée (6 responsables)** : `ses_df2cc961cffeHuH0uxYOf1l3JK` bts-tourisme · `ses_df2cc961bffeD9HkglfQMJA8pT` bts-communication · `ses_df2cc961bffdQjFKseyHu7e3lT` bts-pi · `ses_df2cc9616ffdv3qqaSq4qnXWuv` but-gmp · `ses_df2cc9612ffemlB7rlphzzoETA` but-geii · `ses_df2cc9610ffevo4ilDygcEds47` but-gb. Restent ensuite : lic-histoire (vague précédente) + 12 filières lycée/techno/pro.

**Vague suivante lancée (6 responsables)** : `ses_df2e54fdaffe53GPI2i8kbj343` lic-svt · `ses_df2e54fd9ffep9TYU8ogZf1tuD` lic-lea · `ses_df2e54fd7ffeEZFoWN8uoxLf7I` lic-histoire · `ses_df2e54fccffeRJ9HF2AzNgL71N` lic-info · `ses_df2e54fccffdy9f6MptkvB13tD` cpge-ecg · `ses_df2e54fcaffeZ2099Tkg8g1wpO` commerce.

À la réception des rapports : vérifier chaque lot avec `fixtures.valider_fiche()`, puis lancer :
```
cd fichelab/data
python inject_app.py
python audit_filieres.py
```
L'injecteur ajoutera automatiquement les nouvelles filières à `PROTO_FILIERES`.

## Important

- Les responsables ont interdiction de modifier `index.html`, `inject_app.py` et `audit_filieres.py` : l'intégration reste centralisée.
- Vrais examens : 12 sujets, tous marqués `filieres:["bts-bio"]` et filtrés par `annalesReellesPour()`.
- Migrations au démarrage généralisées à toutes les filières de `PROTO_FILIERES` (retrait des vieilles fiches texte brut par titre+source, ajout automatique des nouvelles fiches, conversion des statuts).
**Reste 41 filières** après ces 5 (sur 46 au total).

## Reprise terminée dans « ilane bis » (25 novembre 2026)

**État final : 46 filières intégrées, 2 850 fiches prototype, 26 168 questions corrigées, 8 514 SVG, audit CONFORME.** Détail dans `fichelab/AUDIT-FILIERES.md`.

Point de rupture repris : l'injection de 35 filières avait eu lieu le 24/11 à 13:15, puis 6 responsables avaient écrit les générateurs des 11 dernières filières sans les exécuter (`stmg-mat-part-C.json` resté vide, 7 générateurs orphelins, 3 lots jamais créés).

**Travail réalisé à la reprise** (6 responsables en parallèle, un par groupe de filières, intégration centrale strictement réservée au coordinateur) :
- Lots réparés et validés : `stmg-C` (CJK corrompu), `st2s-C`, `sti2d-C`, `pro-gestion-C` (parenthèse en trop + CJK), `pro-maintenance-C`, `pro-sante-C`, `btsesf-B` (points manquants + CJK), `btssp3s-B` (17 → 20 fiches).
- Lots créés : `pro-commerce-C`, `btsesf-C`, `btssp3s-C` (20 fiches neuves chacun, titres uniques).
- 2 doublons de titres détectés par l'audit (`MA3` pro-gestion/stl et `EM1` pro-maintenance/stl) : corrigés dans les générateurs `gen_pro-gestion_A.py` et `gen_pro-maintenance_A.py`, lots A régénérés.
- `inject_app.py` : les 11 identifiants ajoutés à `FILIERES_A_INTEGRER` ; `python inject_app.py` puis `python audit_filieres.py` relancés → **AUDIT : CONFORME**.

**Méthode à conserver** : un responsable par filière, aucun sous-agent en cascade ; le coordinateur seul modifie `index.html`, `inject_app.py` et `audit_filieres.py`. Vérification systématique : `python inject_app.py` → `python audit_filieres.py`.

**Attention non résolue** : dans cette copie `ilane bis`, `fichelabs/` est non suivi et `origin` pointe sur `SAMIRneo/elan.git` (pas sur `SAMIRneo/fichelab`). Régler la question du dépôt avant de pousser.

**Anomalies historiques non bloquantes** : les lots `bioalc-mat-part-A/B/C.json` (ancien format texte brut) sont exclus par l'injecteur ; `buttc` n'a que 50 fiches (lot B = 10) mais est déjà audité CONFORME.
