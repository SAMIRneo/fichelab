# Audit FicheLab — filieres prototype

Audit automatique apres injection. Generé par `data/audit_filieres.py`.

## Resultats

| Controle | Valeur | Attendu |
|---|---|---|
| Catalogue EXTRA_FICHES | 1460 | lisible |
| Fiches prototype | 1174 | = 96 BIOALC + nouvelles |
| Annales bibliotheque | 60 | lisible |
| Filieres converties | 18 | bts-bio, bts-ci, bts-mco, bts-ndrc, bts-sio, but-gea, but-info, but-tc, cpge-mpsi, cpge-pci, generale, infirmier, lic-droit, lic-eco, lic-maths, lic-psycho, lic-staps, pass |
| Questions prototype | 10852 | toutes corrigees |
| Schemas SVG | 3486 | XML valide, sans script |
| Ordre des 7 blocs | 1 | variantes (doit etre 1) |
| Titles uniques | 0 | doublons (doit etre 0) |
| Vrais examens filtres | 12 | bts-bio uniquement |
| BIOALC fiches texte brut | 0 | 0 |
| BIOALC Contrôle PC | 15 | 15 visibles BTS1+BTS2 |
| BIOALC annales sans source | 0 | 0 |

## Couverture par filiere

**bts-bio** : 111 prototypes (BTS1:65, BTS2:69)
**bts-ci** : 60 prototypes (BTS1:23, BTS2:37)
**bts-mco** : 82 prototypes (BTS1:52, BTS2:62)
**bts-ndrc** : 60 prototypes (BTS1:24, BTS2:36)
**bts-sio** : 60 prototypes (BTS1:27, BTS2:33)
**but-gea** : 60 prototypes (BUT1:22, BUT2:22, BUT3:16)
**but-info** : 60 prototypes (BUT1:30, BUT2:54, BUT3:28)
**but-tc** : 50 prototypes (BUT1:19, BUT2:30, BUT3:16)
**cpge-mpsi** : 56 prototypes (1re:28, 2e:28)
**cpge-pci** : 56 prototypes (1re:28, 2e:28)
**generale** : 95 prototypes (1re:46, 2nde:29, Terminale:42)
**infirmier** : 62 prototypes (IFSI1:26, IFSI2:25, IFSI3:11)
**lic-droit** : 60 prototypes (L1:20, L2:25, L3:15)
**lic-eco** : 60 prototypes (L1:22, L2:24, L3:14)
**lic-maths** : 60 prototypes (L1:25, L2:30, L3:14)
**lic-psycho** : 60 prototypes (L1:18, L2:23, L3:19)
**lic-staps** : 60 prototypes (L1:21, L2:23, L3:16)
**pass** : 62 prototypes (PASS1:62)

## Annales par filiere

- **bts-bio** : 23
- **generale** : 19
- **bts-mco** : 18

## Verifications

- Syntaxe JavaScript : **OK**
- Schemas SVG : 3486, tous analysables en XML et sans script/on*/javascript:
- Blocs d'affichage : 1174 fiche(s), ordre strict identique
- Questions : 10852, toutes avec correction
- Migrations : filtre prototype + nettoyage + ajout automatique generalises

## Problemes detectes

**Aucun problème détecté — audit CONFORME.**
