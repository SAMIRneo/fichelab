# Audit FicheLab — filieres prototype

Audit automatique apres injection. Generé par `data/audit_filieres.py`.

## Resultats

| Controle | Valeur | Attendu |
|---|---|---|
| Catalogue EXTRA_FICHES | 881 | lisible |
| Fiches prototype | 395 | = 96 BIOALC + nouvelles |
| Annales bibliotheque | 60 | lisible |
| Filieres converties | 5 | bts-bio, bts-mco, generale, lic-droit, pass |
| Questions prototype | 3661 | toutes corrigees |
| Schemas SVG | 1149 | XML valide, sans script |
| Ordre des 7 blocs | 1 | variantes (doit etre 1) |
| Titles uniques | 0 | doublons (doit etre 0) |
| Vrais examens filtres | 12 | bts-bio uniquement |

## Couverture par filiere

**bts-bio** : 96 prototypes (BTS1:50, BTS2:54)
**bts-mco** : 82 prototypes (BTS1:52, BTS2:62)
**generale** : 95 prototypes (1re:46, 2nde:29, Terminale:42)
**lic-droit** : 60 prototypes (L1:20, L2:25, L3:15)
**pass** : 62 prototypes (PASS1:62)

## Annales par filiere

- **bts-bio** : 23
- **generale** : 19
- **bts-mco** : 18

## Verifications

- Syntaxe JavaScript : **OK**
- Schemas SVG : 1149, tous analysables en XML et sans script/on*/javascript:
- Blocs d'affichage : 395 fiche(s), ordre strict identique
- Questions : 3661, toutes avec correction
- Migrations : filtre prototype + nettoyage + ajout automatique generalises

## Problemes detectes

**Aucun problème détecté — audit CONFORME.**
