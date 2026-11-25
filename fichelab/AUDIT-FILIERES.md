# Audit FicheLab — filieres prototype

Audit automatique apres injection. Generé par `data/audit_filieres.py`.

## Resultats

| Controle | Valeur | Attendu |
|---|---|---|
| Catalogue EXTRA_FICHES | 2850 | lisible |
| Fiches prototype | 2850 | = 96 BIOALC + nouvelles |
| Annales bibliotheque | 60 | lisible |
| Filieres converties | 46 | bts-bio, bts-cg, bts-ci, bts-ciel, bts-communication, bts-esf, bts-gpme, bts-mco, bts-ndrc, bts-pi, bts-sio, bts-sp3s, bts-tourisme, but-gb, but-gea, but-geii, but-gmp, but-info, but-tc, commerce, cpge-ecg, cpge-mpsi, cpge-pci, generale, infirmier, lic-droit, lic-eco, lic-histoire, lic-info, lic-lea, lic-maths, lic-psycho, lic-staps, lic-svt, pass, pro-commerce, pro-electricite, pro-gestion, pro-maintenance, pro-sante, st2s, std2a, sthr, sti2d, stl, stmg |
| Questions prototype | 26168 | toutes corrigees |
| Schemas SVG | 8514 | XML valide, sans script |
| Ordre des 7 blocs | 1 | variantes (doit etre 1) |
| Titles uniques | 0 | doublons (doit etre 0) |
| Vrais examens filtres | 12 | bts-bio uniquement |
| BIOALC fiches texte brut | 0 | 0 |
| BIOALC Contrôle PC | 15 | 15 visibles BTS1+BTS2 |
| BIOALC annales sans source | 0 | 0 |

## Couverture par filiere

**bts-bio** : 111 prototypes (BTS1:65, BTS2:69)
**bts-cg** : 60 prototypes (BTS1:29, BTS2:31)
**bts-ci** : 60 prototypes (BTS1:23, BTS2:37)
**bts-ciel** : 60 prototypes (BTS1:29, BTS2:31)
**bts-communication** : 60 prototypes (BTS1:24, BTS2:36)
**bts-esf** : 60 prototypes (BTS1:40, BTS2:20)
**bts-gpme** : 60 prototypes (BTS1:31, BTS2:31)
**bts-mco** : 82 prototypes (BTS1:52, BTS2:62)
**bts-ndrc** : 60 prototypes (BTS1:24, BTS2:36)
**bts-pi** : 60 prototypes (BTS1:27, BTS2:33)
**bts-sio** : 60 prototypes (BTS1:27, BTS2:33)
**bts-sp3s** : 60 prototypes (BTS1:25, BTS2:35)
**bts-tourisme** : 60 prototypes (BTS1:52, BTS2:58)
**but-gb** : 60 prototypes (BUT1:20, BUT2:54, BUT3:40)
**but-gea** : 60 prototypes (BUT1:22, BUT2:22, BUT3:16)
**but-geii** : 60 prototypes (BUT1:26, BUT2:52, BUT3:42)
**but-gmp** : 60 prototypes (BUT1:21, BUT2:24, BUT3:15)
**but-info** : 60 prototypes (BUT1:30, BUT2:54, BUT3:28)
**but-tc** : 50 prototypes (BUT1:19, BUT2:30, BUT3:16)
**commerce** : 60 prototypes (Bac+1:20, Bac+2:24, Bac+3:16)
**cpge-ecg** : 56 prototypes (1re:28, 2e:28)
**cpge-mpsi** : 56 prototypes (1re:28, 2e:28)
**cpge-pci** : 56 prototypes (1re:28, 2e:28)
**generale** : 95 prototypes (1re:46, 2nde:29, Terminale:42)
**infirmier** : 62 prototypes (IFSI1:26, IFSI2:25, IFSI3:11)
**lic-droit** : 60 prototypes (L1:20, L2:25, L3:15)
**lic-eco** : 60 prototypes (L1:22, L2:24, L3:14)
**lic-histoire** : 60 prototypes (L1:23, L2:18, L3:19)
**lic-info** : 60 prototypes (L1:24, L2:35, L3:19)
**lic-lea** : 60 prototypes (L1:26, L2:38, L3:19)
**lic-maths** : 60 prototypes (L1:25, L2:30, L3:14)
**lic-psycho** : 60 prototypes (L1:18, L2:23, L3:19)
**lic-staps** : 60 prototypes (L1:21, L2:23, L3:16)
**lic-svt** : 60 prototypes (L1:17, L2:24, L3:19)
**pass** : 62 prototypes (PASS1:62)
**pro-commerce** : 60 prototypes (1re pro:27, 2nde pro:20, Terminale pro:13)
**pro-electricite** : 60 prototypes (1re pro:25, 2nde pro:10, Terminale pro:25)
**pro-gestion** : 60 prototypes (1re pro:36, 2nde pro:19, Terminale pro:29)
**pro-maintenance** : 60 prototypes (1re pro:60, 2nde pro:60, Terminale pro:60)
**pro-sante** : 60 prototypes (1re pro:24, 2nde pro:13, Terminale pro:23)
**st2s** : 60 prototypes (1re:48, Terminale:42)
**std2a** : 60 prototypes (1re:54, Terminale:60)
**sthr** : 60 prototypes (1re:35, Terminale:42)
**sti2d** : 60 prototypes (1re:41, Terminale:19)
**stl** : 60 prototypes (1re:31, Terminale:29)
**stmg** : 60 prototypes (1re:33, Terminale:34)

## Annales par filiere

- **bts-bio** : 23
- **generale** : 19
- **bts-mco** : 18

## Verifications

- Syntaxe JavaScript : **OK**
- Schemas SVG : 8514, tous analysables en XML et sans script/on*/javascript:
- Blocs d'affichage : 2850 fiche(s), ordre strict identique
- Questions : 26168, toutes avec correction
- Migrations : filtre prototype + nettoyage + ajout automatique generalises

## Problemes detectes

**Aucun problème détecté — audit CONFORME.**
