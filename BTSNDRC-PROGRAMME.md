# BTS Négociation et Digitalisation de la Relation Client (NDRC) — carte des chapitres FicheLab

> **Référentiel :** arrêté du **19 février 2018** portant définition et fixant les conditions de délivrance du BTS « Négociation et digitalisation de la relation client » (NOR **ESRS1803333A**, JO n° 0054 du 6 mars 2018), modifié ; référentiel de certification en annexes I a, I b, II a, II b ; unités U1 à U6 + UF1, RNCP **38368**. Première session : 2020.
> **Rectificatif de source :** le brief de reprise mentionnait « arrêté du 19 juin 2018 ». Le texte officiel fondateur est bien celui du **19 février 2018** (vérifié sur [Légifrance, JORFTEXT000036672161](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000036672161) et [France Compétences, RNCP 38368](https://www.francecompetences.fr/recherche/rncp/34030)). C'est cette référence qui est retenue dans les fiches. Le programme de **culture économique, juridique et managériale (CEJM, U3)** relève de l'arrêté du 15 février 2018, commun à plusieurs BTS.
> **Sources complémentaires :** [`SOURCES.md`](SOURCES.md) § Parcoursup — **155 647 vœux 2026** pour le BTS NDRC ; [`éduscol — le BTS`](https://eduscol.education.gouv.fr/5583/le-brevet-de-technicien-superieur) (référentiel NDRC et épreuve CEJM).
> **Identifiant appli :** `bts-ndrc`. **Années :** `BTS1`, `BTS2`. **Matières FicheLab :** `Management`, `Communication`, `Marketing`, `Informatique`, `Droit`, `Économie`, `Maths / stats`, `Anglais professionnel`, `Français` (orthographe exacte, identique à celle utilisée par `index.html`).

---

## 1. Enseignement général — U1, U2 et UF1

| Unité officielle | Matière FicheLab | Chapitres (préfixes de fiches) |
|---|---|---|
| U1 · Culture générale et expression (coef. 4) | `Français` | Synthèse de documents · Analyse de situation et argumentation · Expression écrite et numérique · Culture générale et ouverture (`PF1.`, `PF2.`) |
| U2 · Communication en langue vivante étrangère 1 (coef. 3) | `Anglais professionnel` | Compréhension de documents commerciaux · E-mail professionnel · Présentation et négociation orale (`AN1.`–`AN3.`) |
| UF1 · Langue vivante étrangère 2 (facultative) | `Anglais professionnel` | Extension et approfondissement des situations professionnelles anglophones |

## 2. Enseignement professionnel — U4, U5, U6

| Unité officielle | Matière FicheLab | Chapitres (préfixes de fiches) |
|---|---|---|
| U4 · Relation client et négociation-vente (coef. 5) | `Management` + `Communication` | Cibler et prospecter · Négocier et accompagner la relation client · Événement commercial · Information commerciale · Relation omnicanale (`MA1.`–`MA10.`, `CO1.`–`CO10.`) |
| U5 · Relation client à distance et digitalisation | `Informatique` + `Communication` | CRM et données clients · Outils numériques · Visioconférence et télétravail · E-commerce · Social media · Cybersécurité · Tableaux de bord (`IN1.`–`IN10.`, `CO6.`, `CO7.`) |
| U6 · Relation client et animation de réseaux | `Management` + `Marketing` | Animation de réseau · Partenaires et distributeurs · Segmentation · Étude de marché · Positionnement ·Produit · Prix · Distribution · Promotion · Marketing digital · Fidélisation · Pilotage (`MA7.`–`MA9.`, `MK1.`–`MK10.`) |

## 3. Culture économique, juridique et managériale — U3 (unité commune)

| Volet | Matière FicheLab | Chapitres (préfixes de fiches) |
|---|---|---|
| Droit | `Droit` | Contrat et obligations · Consommation et pratiques commerciales · Concurrence et distribution · Droit social · Responsabilité et données personnelles (`DR1.`–`DR5.`) |
| Économie | `Économie` | Offre et demande · L'entreprise et son environnement · Conjoncture et croissance · Commerce international · Économie numérique (`EC1.`–`EC5.`) |
| Management | `Management` | Organisation, animation d'équipe, pilotage de la performance (lot A, `MA1.`–`MA10.`) |

## 4. Outils quantitatifs — transverse (appui à U3, U4, U6)

Le BTS NDRC ne comporte pas d'unité distincte de mathématiques : les calculs commerciaux, les statistiques et les probabilités sont mobilisés dans les situations professionnelles de négociation, de pilotage et d'étude de marché. FicheLab les regroupe sous la matière `Maths / stats` pour coller aux autres filières.

| Matière FicheLab | Chapitres (préfixes de fiches) |
|---|---|
| `Maths / stats` | Calculs commerciaux et marges · Statistiques descriptives · Probabilités et décision · Séries temporelles et prévisions · Échantillonnage et tests (`MS1.`–`MS5.`) |

---

## 5. Méthode (identique à BTS MCO, BIOALC et voie générale)

Une fiche = un chapitre : **12 points de cours**, **10 questions corrigées** (8 QCM + 2 questionstexte), **7 blocs colorés en ordre strict** (intro, formule, grille, liste, étapes, attention, exemples) et **3 schémas SVG** construits avec `diag()`. Chaque fiche porte sa source officielle dans le champ `source`. Voir [`FICHE-PROTOTYPE.md`](FICHE-PROTOTYPE.md), [`GENERALE-PROGRAMME.md`](GENERALE-PROGRAMME.md), [`BTSMCO-PROGRAMME.md`](BTSMCO-PROGRAMME.md) et [`AUDIT-BTSNDRC.md`](AUDIT-BTSNDRC.md).

## 6. Suivi de la déclinaison

| Lot | Générateur | JSON | Matières | Fiches | Statut |
|---|---|---|---|---|---|
| A | `data/gen_btsndrc_A.py` | `data/btsndrc-mat-part-A.json` | Management (10), Communication (10) | 20 | ✅ livré et validé (non repris) |
| B | `data/gen_btsndrc_B.py` | `data/btsndrc-mat-part-B.json` | Marketing (10), Informatique (10) | 20 | ✅ généré, validé |
| C | `data/gen_btsndrc_C.py` | `data/btsndrc-mat-part-C.json` | Droit (5), Économie (5), Maths / stats (5), Anglais professionnel (3), Français (2) | 20 | ✅ généré, validé |

**Déclinaison terminée :** 60 fiches, 720 points de cours, 600 questions corrigées, 180 schémas SVG. Contrôle détaillé : [`AUDIT-BTSNDRC.md`](AUDIT-BTSNDRC.md).
