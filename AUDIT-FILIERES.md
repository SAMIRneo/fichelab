# Audit FicheLab — filieres prototype

Audit automatique apres injection. Generé par `data/audit_filieres.py`.

## Resultats

| Controle | Valeur | Attendu |
|---|---|---|
| Catalogue EXTRA_FICHES | 843 | lisible |
| Fiches prototype | 335 | = 96 BIOALC + nouvelles |
| Annales bibliotheque | 60 | lisible |
| Filieres converties | 4 | bts-bio, bts-mco, generale, pass |
| Questions prototype | 3121 | toutes corrigees |
| Schemas SVG | 969 | XML valide, sans script |
| Ordre des 7 blocs | 1 | variantes (doit etre 1) |
| Titles uniques | 0 | doublons (doit etre 0) |
| Vrais examens filtres | 12 | bts-bio uniquement |

## Couverture par filiere

**bts-bio** : 96 prototypes (BTS1:50, BTS2:54)
**bts-mco** : 82 prototypes (BTS1:52, BTS2:62)
**generale** : 95 prototypes (1re:46, 2nde:29, Terminale:42)
**pass** : 62 prototypes (PASS1:62)

## Annales par filiere

- **bts-bio** : 23
- **generale** : 19
- **bts-mco** : 18

## Verifications

- Syntaxe JavaScript : **OK**
- Schemas SVG : 969, tous analysables en XML et sans script/on*/javascript:
- Blocs d'affichage : 335 fiche(s), ordre strict identique
- Questions : 3121, toutes avec correction
- Migrations : filtre prototype + nettoyage + ajout automatique generalises

## Problemes detectes

**Aucun problème détecté — audit CONFORME.**
