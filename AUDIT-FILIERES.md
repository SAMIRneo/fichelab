# Audit FicheLab — filieres prototype

Audit automatique apres injection. Generé par `data/audit_filieres.py`.

## Resultats

| Controle | Valeur | Attendu |
|---|---|---|
| Catalogue EXTRA_FICHES | 1249 | lisible |
| Fiches prototype | 874 | = 96 BIOALC + nouvelles |
| Annales bibliotheque | 60 | lisible |
| Filieres converties | 13 | bts-bio, bts-mco, bts-ndrc, but-gea, but-tc, cpge-mpsi, cpge-pci, generale, infirmier, lic-droit, lic-eco, lic-staps, pass |
| Questions prototype | 8032 | toutes corrigees |
| Schemas SVG | 2586 | XML valide, sans script |
| Ordre des 7 blocs | 1 | variantes (doit etre 1) |
| Titles uniques | 0 | doublons (doit etre 0) |
| Vrais examens filtres | 12 | bts-bio uniquement |

## Couverture par filiere

**bts-bio** : 111 prototypes (BTS1:58, BTS2:69)
**bts-mco** : 82 prototypes (BTS1:52, BTS2:62)
**bts-ndrc** : 60 prototypes (BTS1:24, BTS2:36)
**but-gea** : 60 prototypes (BUT1:22, BUT2:22, BUT3:16)
**but-tc** : 50 prototypes (BUT1:19, BUT2:30, BUT3:16)
**cpge-mpsi** : 56 prototypes (1re:28, 2e:28)
**cpge-pci** : 56 prototypes (1re:28, 2e:28)
**generale** : 95 prototypes (1re:46, 2nde:29, Terminale:42)
**infirmier** : 62 prototypes (IFSI1:26, IFSI2:25, IFSI3:11)
**lic-droit** : 60 prototypes (L1:20, L2:25, L3:15)
**lic-eco** : 60 prototypes (L1:22, L2:24, L3:14)
**lic-staps** : 60 prototypes (L1:21, L2:23, L3:16)
**pass** : 62 prototypes (PASS1:62)

## Annales par filiere

- **bts-bio** : 23
- **generale** : 19
- **bts-mco** : 18

## Verifications

- Syntaxe JavaScript : **OK**
- Schemas SVG : 2586, tous analysables en XML et sans script/on*/javascript:
- Blocs d'affichage : 874 fiche(s), ordre strict identique
- Questions : 8032, toutes avec correction
- Migrations : filtre prototype + nettoyage + ajout automatique generalises

## Problemes detectes

**Aucun problème détecté — audit CONFORME.**
