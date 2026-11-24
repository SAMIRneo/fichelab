# -*- coding: utf-8 -*-
"""Générateur de licdroit-mat-part-C.json — lot C de la filière Licence Droit.

20 fiches transversales au format « prototype » (identique au modèle
FICHE_UV / gen_generale_modele.py) :
 Statistiques (6, ST1. à ST6.), Psychologie (4, PSY1. à PSY4.),
 Anglais (4, AN1. à AN4.), Informatique (3, IN1. à IN3.),
 Français (3, PF1. à PF3.).

Sources : arrêté du 6 avril 2021 (licence d'études juridiques), BO spécial n° 7
du 17 février 2022, éduscol, INSEE, CECRL (Conseil de l'Europe), CNIL.

Chaque fiche : 12 points, 9 questions (7 QCM + 2 rédaction), 7 blocs dans
l'ordre strict, 3 schémas SVG construits par fixtures.py.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fixtures import (fiche, qcm, qt, diag, bloc, valider_et_ecrire,
                      svg_grille, svg_flux, svg_etapes, svg_compare)

FIL = ["lic-droit"]
L1, L2, L3 = ["L1"], ["L2"], ["L3"]

REF = ("Arrêté du 6 avril 2021 relatif à la licence d'études juridiques "
       "(JORF n° 0083 du 8 avril 2021) · BO spécial n° 7 du 17 février 2022 · éduscol")
REF_S = REF + " · INSEE, méthodes statistiques"
REF_P = REF + " · référentiel de la licence de psychologie (enseignements supérieurs)"
REF_A = REF + " · Cadre européen commun de référence pour les langues (Conseil de l'Europe)"
REF_I = REF + " · CNIL, règlement général sur la protection des données (RGPD)"
REF_F = REF + " · programmes de lettres et de rhétorique de licence"


# --- raccourcis de blocs (ordre strict garanti à la construction) -----------
def Bi(t, x): return bloc(t, texte=x, type="intro")
def Bf(t, e, l): return bloc(t, eq=e, leg=l, type="formule")
def Bg(t, cols, rows): return bloc(t, items=[cols] + list(rows), type="grille")
def Bl(t, items): return bloc(t, items=items, type="liste")
def Be(t, items): return bloc(t, items=items, type="etapes")
def Ba(t, items): return bloc(t, items=items, type="attention")
def Bx(t, items): return bloc(t, items=items, type="exemples")

def SG(t, cols, rows): return diag(t, svg_grille(t, cols, rows))
def SF(t, steps): return diag(t, svg_flux(t, steps))
def SE(t, steps): return diag(t, svg_etapes(t, steps))
def SC(t, g, d): return diag(t, svg_compare(t, g, d))


def build(an, mat, titre, ref, points, qcms, texts,
          idea, formule, leg, grille, liste, etapes, attention, exemples, schemas):
    aff = [Bi("L'idée en une phrase", idea),
           Bf("La règle à retenir", formule, leg),
           Bg("Tableau de synthèse", grille[0], grille[1]),
           Bl("À retenir", liste),
           Be("Méthode pas à pas", etapes),
           Ba("Pièges fréquents", attention),
           Bx("Exemples d'application", exemples)]
    qs = [qcm(q, o, c, r) for (q, o, c, r) in qcms] + [qt(q, r, c) for (q, r, c) in texts]
    return fiche(FIL, an, mat, titre, ref, points, qs, aff, schemas)


F = []

# === STATISTIQUES — 6 fiches (ST1. à ST6.) ==================================

F.append(build(
    L1, "Statistiques", "ST1. · Statistiques descriptives", REF_S,
    [
        "La statistique descriptive organise, résume et présente un jeu de données observé, sans tirer de conclusion qui dépasse ces données.",
        "Une variable qualitative est catégorielle : nominale sans ordre (nationalité) ou ordinale avec un ordre (niveau d'étude). Une variable quantitative est discrète (nombre d'enfants) ou continue (taille, revenu).",
        "La population est l'ensemble complet étudié ; l'unité statistique en est un élément ; l'échantillon est une partie de la population prélevée pour l'observer.",
        "Pour chaque modalité, l'effectif n_i compte les individus et la fréquence relative vaut f_i = n_i / N, avec N l'effectif total ; la somme des fréquences vaut 1, soit 100 %.",
        "La moyenne x̄ = (Σ n_i·x_i) / N est le centre de gravité de la série ; elle utilise toutes les valeurs mais est sensible aux valeurs extrêmes.",
        "La médiane est la valeur qui partage la série ordonnée en deux moitiés ; si N est pair, on retient la moyenne des deux valeurs centrales.",
        "Les quartiles Q1 et Q3 partagent la série ordonnée en quatre groupes ; l'écart interquartile Q3 − Q1 décrit la dispersion du cœur de la distribution.",
        "La variance v = (Σ (x_i − x̄)²) / N et l'écart-type σ = √v mesurent la dispersion autour de la moyenne ; σ s'exprime dans la même unité que la variable.",
        "Le mode est la modalité la plus fréquente ; il existe pour une variable qualitative comme quantitative et peut être unique ou multiple.",
        "Un diagramme en barres représente les effectifs d'une variable qualitative ; un histogramme représente une variable continue par des rectangles dont l'aire est proportionnelle à l'effectif.",
        "En cas de distribution asymétrique ou de valeurs aberrantes, la médiane et l'écart interquartile sont plus robustes que la moyenne et l'écart-type.",
        "Toute présentation doit préciser la source, l'unité, l'effectif N et le mode de calcul : une moyenne sans mesure de dispersion ni taille d'échantillon est insuffisante.",
    ],
    [
        ("Quelle est la somme des fréquences relatives d'une série complète ?",
         ["0", "1", "100", "N"], 1,
         "Les fréquences relatives n_i/N partagent l'unité : leur somme vaut 1, ou 100 %."),
        ("La variable « catégorie socioprofessionnelle » est :",
         ["Qualitative nominale", "Qualitative ordinale", "Quantitative discrète", "Quantitative continue"], 0,
         "Les catégories socioprofessionnelles sont des modalités sans ordre naturel : c'est une variable qualitative nominale."),
        ("Quelle est la moyenne de la série 2 ; 4 ; 4 ; 8 ?",
         ["4", "4,5", "5", "18"], 1,
         "La somme vaut 18 et l'effectif 4, donc x̄ = 18/4 = 4,5."),
        ("Quelle est la médiane de la série 3 ; 7 ; 9 ; 12 ?",
         ["7", "8", "9", "7,5"], 1,
         "L'effectif est pair : la médiane est la moyenne des deux valeurs centrales (7 + 9)/2 = 8."),
        ("L'écart interquartile se calcule par :",
         ["Q3 − Q1", "Q1 + Q3", "Q2", "σ"], 0,
         "L'écart interquartile Q3 − Q1 mesure l'étendue du milieu de la distribution, en ignorant les queues."),
        ("Quel graphique convient à une variable qualitative ?",
         ["Histogramme", "Diagramme en barres", "Nuage de points", "Courbe de densité"], 1,
         "Le diagramme en barres représente des modalités distinctes ; l'histogramme est réservé aux variables continues."),
        ("Une valeur aberrante influence davantage :",
         ["La médiane", "La moyenne", "Le mode", "L'écart interquartile"], 1,
         "La moyenne intègre toutes les valeurs, donc une valeur extrême la déplace ; la médiane et les quartiles sont robustes."),
    ],
    [
        ("Calculer la moyenne, la médiane et la variance de la série 2 ; 4 ; 4 ; 8.",
         "Moyenne : x̄ = (2+4+4+8)/4 = 18/4 = 4,5. Médiane : (4+4)/2 = 4. Variance : v = [(2−4,5)² + (4−4,5)² + (4−4,5)² + (8−4,5)²]/4 = (6,25+0,25+0,25+12,25)/4 = 4,75, soit un écart-type d'environ 2,18.",
         "On calcule d'abord la moyenne, puis on range la série pour la médiane, puis les écarts au carré autour de la moyenne avant de diviser par N."),
        ("Pourquoi préférer la médiane et l'écart interquartile à la moyenne et à l'écart-type pour décrire des salaires ?",
         "Les salaires comportent souvent quelques très hauts revenus qui tirent la moyenne vers le haut et gonflent l'écart-type. La médiane donne le revenu typique et l'écart interquartile décrit la dispersion de la majorité des salariés ; cette paire résiste aux valeurs extrêmes et reflète mieux la réalité du cœur de la distribution.",
         "Il faut relier la robustesse de la médiane et des quartiles à l'asymétrie de la distribution des revenus, puis en tirer une conséquence pour la lecture sociale des données."),
    ],
    "Décrire une série, c'est compter les effectifs, résumer le centre (moyenne, médiane) et mesurer la dispersion (écart-type, quartiles).",
    "f_i = n_i / N · x̄ = Σ n_i·x_i / N · v = Σ (x_i − x̄)² / N",
    "N : effectif total · n_i : effectif de la modalité i · x_i : valeur · σ = √v : écart-type",
    (["Indicateur", "Ce qu'il mesure", "Sensible aux extrêmes"],
     [["Moyenne", "Centre de gravité", "Oui"],
      ["Médiane", "Valeur centrale", "Non"],
      ["Mode", "Modalité la plus fréquente", "Non"],
      ["Écart-type", "Dispersion autour de la moyenne", "Oui"],
      ["Écart interquartile", "Dispersion du cœur de la série", "Non"]]),
    [
        "Toujours préciser la population, l'effectif N, l'unité et la source.",
        "Distinguer variable qualitative (catégories) et quantitative (nombres).",
        "Lire la forme de la distribution avant de choisir le bon indicateur de centre.",
        "Associer systématiquement une mesure de centre et une mesure de dispersion.",
        "Vérifier que les fréquences relatives somment à 1.",
    ],
    [
        "Recenser les modalités et compter les effectifs n_i.",
        "Calculer N = Σ n_i et les fréquences f_i = n_i / N.",
        "Choisir le graphique adapté au type de variable.",
        "Calculer le centre (moyenne ou médiane) selon la forme de la série.",
        "Calculer la dispersion (écart-type ou écart interquartile) et rédiger la conclusion.",
    ],
    [
        "Confondre effectif et fréquence : n_i compte, f_i rapporte à N.",
        "Oublier de convertir en pourcentage ou d'indiquer l'unité.",
        "Utiliser la moyenne sur une série très asymétrique sans le signaler.",
        "Prendre la moyenne des deux valeurs centrales quand N est impair.",
        "Tracer un histogramme pour une variable qualitative.",
    ],
    [
        '<span class="cle">2 ; 4 ; 4 ; 8</span> → moyenne 4,5, médiane 4, écart-type ≈ 2,18.',
        '<span class="cle">3 ; 7 ; 9 ; 12</span> → médiane (7 + 9)/2 = 8.',
        '<span class="cle">N = 200, n = 50</span> → fréquence 50/200 = 0,25 = 25 %.',
        '<span class="cle">Q1 = 12, Q3 = 20</span> → écart interquartile = 8.',
        '<span class="cle">Salaires</span> → médiane et Q1/Q3 plus lisibles que moyenne et écart-type.',
    ],
    [
        SG("Lire un tableau de fréquences",
           ["Modalité", "Effectif", "Fréquence"],
           [["A", "40", "20 %"], ["B", "100", "50 %"],
            ["C", "60", "30 %"], ["Total", "200", "100 %"]]),
        SE("Résumer une série",
           ["Compter les effectifs n_i et l'effectif total N",
            "Calculer les fréquences f_i = n_i / N",
            "Choisir le graphique selon le type de variable",
            "Calculer moyenne ou médiane",
            "Mesurer la dispersion et conclure"]),
        SC("Moyenne / médiane",
           ("Moyenne", ["Utilise toutes les valeurs", "Sensible aux extrêmes", "Écart-type associé"]),
           ("Médiane", ["Valeur centrale ordonnée", "Robuste aux extrêmes", "Quartiles associés"])),
    ]))

F.append(build(
    L1, "Statistiques", "ST2. · Probabilités", REF_S,
    [
        "Une expérience aléatoire est une épreuve dont le résultat est incertain mais dont l'ensemble des résultats possibles est connu à l'avance.",
        "L'univers Ω est l'ensemble de toutes les issues possibles ; un événement est une partie de Ω, c'est-à-dire un ensemble d'issues.",
        "Dans le cas fini équiprobable, la probabilité d'un événement A vaut P(A) = |A| / |Ω|, où |A| désigne le nombre d'issues favorables.",
        "Les axiomes de Kolmogorov posent P(A) ≥ 0, P(Ω) = 1 et l'additivité pour des événements deux à deux disjoints.",
        "L'événement contraire Ā regroupe les issues qui ne sont pas dans A ; sa probabilité vaut P(Ā) = 1 − P(A).",
        "Si A et B sont disjoints (incompatibles), P(A ∪ B) = P(A) + P(B) ; sinon P(A ∪ B) = P(A) + P(B) − P(A ∩ B).",
        "Deux événements A et B sont indépendants si et seulement si P(A ∩ B) = P(A)·P(B) ; indépendance et incompatibilité sont deux notions distinctes.",
        "La probabilité conditionnelle de A sachant B est P(A | B) = P(A ∩ B) / P(B), définie pour P(B) > 0.",
        "Un arbre pondéré représente un enchaînement d'épreuves : on multiplie les probabilités le long d'une branche et on additionne les branches conduisant au même événement.",
        "Une loi de probabilité associe à chaque valeur d'une variable aléatoire sa probabilité ; les probabilités sont positives et somment à 1.",
        "L'espérance mathématique d'une variable aléatoire discrète vaut E(X) = Σ x_i·P(X = x_i) : c'est la valeur moyenne pondérée à long terme.",
        "Un tirage sans remplacement modifie les probabilités des étapes suivantes ; un tirage avec remplacement les laisse inchangées.",
    ],
    [
        ("Dans un cas fini équiprobable, P(A) vaut :",
         ["|Ω| / |A|", "|A| / |Ω|", "|A| + |Ω|", "1 − |A|"], 1,
         "On divise le nombre d'issues favorables par le nombre total d'issues."),
        ("La probabilité de l'événement contraire est :",
         ["1 + P(A)", "1 − P(A)", "P(A) − 1", "P(A)²"], 1,
         "A et son contraire forment une partition de Ω, donc P(A) + P(Ā) = 1."),
        ("Si A et B sont indépendants, alors :",
         ["P(A∩B) = 0", "P(A∩B) = P(A) + P(B)", "P(A∩B) = P(A)·P(B)", "P(A∪B) = 0"], 2,
         "L'indépendance se définit par la multiplication des probabilités."),
        ("La probabilité conditionnelle P(A | B) vaut :",
         ["P(A)/P(B)", "P(B)/P(A)", "P(A∩B)/P(B)", "P(A∩B)/P(A)"], 2,
         "On restreint l'univers à B : on divise la probabilité de l'intersection par celle de B."),
        ("En lançant un dé équilibré, la probabilité d'obtenir un nombre pair est :",
         ["1/6", "1/3", "1/2", "2/3"], 2,
         "Les issues paires sont 2, 4, 6, soit 3 issues favorables sur 6 : P = 3/6 = 1/2."),
        ("Si A et B sont incompatibles et de probabilités non nulles :",
         ["P(A∩B) = P(A)·P(B)", "P(A∩B) = 0", "P(A∪B) = 0", "P(A) = P(B)"], 1,
         "Incompatibles signifie qu'aucune issue ne réalise A et B en même temps."),
        ("L'espérance d'une variable aléatoire discrète est :",
         ["La valeur la plus probable", "Σ x_i·P(X = x_i)", "La médiane des valeurs", "Le nombre d'issues"], 1,
         "L'espérance est une moyenne pondérée par les probabilités."),
    ],
    [
        ("Une urne contient 5 boules rouges et 3 boules bleues. On tire deux boules sans remplacement. Calculer la probabilité de tirer deux boules rouges.",
         "P(R1) = 5/8. Après un premier tirage rouge, il reste 4 rouges sur 7 boules, donc P(R2 | R1) = 4/7. Par la règle de multiplication : P(R1 ∩ R2) = (5/8) × (4/7) = 20/56 = 5/14.",
         "Reconnaître un tirage sans remplacement, utiliser la probabilité conditionnelle de la seconde étape et multiplier les probabilités le long de la branche."),
        ("Deux événements A et B vérifient P(A) = 0,4, P(B) = 0,5 et P(A∩B) = 0,2. Sont-ils indépendants ? Calculer P(A∪B).",
         "P(A)·P(B) = 0,4 × 0,5 = 0,2 = P(A∩B) : les événements sont indépendants. P(A∪B) = P(A) + P(B) − P(A∩B) = 0,4 + 0,5 − 0,2 = 0,7.",
         "Tester d'abord l'égalité caractéristique de l'indépendance, puis appliquer la formule de l'union en retirant l'intersection pour ne pas la compter deux fois."),
    ],
    "Les probabilités mesurent l'incertitude : on recense les issues, on applique les règles de l'union, du complément et de l'indépendance.",
    "P(A | B) = P(A∩B)/P(B) · P(A∩B) = P(A)·P(B) si indépendance",
    "Ω : univers · A, B : événements · Ā : événement contraire · E(X) = Σ x_i·P(X = x_i)",
    (["Notion", "Formule", "Condition"],
     [["Complément", "P(Ā) = 1 − P(A)", "Toujours"],
      ["Union", "P(A∪B) = P(A)+P(B)−P(A∩B)", "Toujours"],
      ["Union disjoints", "P(A∪B) = P(A)+P(B)", "A ∩ B = ∅"],
      ["Indépendance", "P(A∩B) = P(A)·P(B)", "À vérifier"],
      ["Conditionnelle", "P(A|B) = P(A∩B)/P(B)", "P(B) > 0"]]),
    [
        "Un événement est toujours une partie de l'univers Ω.",
        "La somme des probabilités de toutes les issues est égale à 1.",
        "Indépendance et incompatibilité ne veulent pas dire la même chose.",
        "Sans remplacement, les probabilités changent à chaque tiret.",
        "Un arbre pondéré se lit en multipliant le long des branches et en additionnant entre branches.",
    ],
    [
        "Définir l'expérience et recenser toutes les issues de Ω.",
        "Repérer l'événement recherché et les issues favorables.",
        "Vérifier l'équiprobabilité avant d'utiliser |A|/|Ω|.",
        "Choisir la règle adaptée : complément, union, conditionnelle ou indépendance.",
        "Vérifier que le résultat est compris entre 0 et 1 et le rédiger en phrase.",
    ],
    [
        "Compter les issues sans ordre quand l'ordre importe, et inversement.",
        "Confondre « incompatible » (P(A∩B) = 0) et « indépendant ».",
        "Oublier de retirer l'intersection dans une union quelconque.",
        "Diviser par P(B) = 0 dans une probabilité conditionnelle.",
        "Oublier de modifier les effectifs lors d'un tirage sans remplacement.",
    ],
    [
        '<span class="cle">Dé équilibré</span> → P(pair) = 3/6 = 1/2.',
        '<span class="cle">5 rouges, 3 bleus, sans remplacement</span> → P(2 rouges) = 5/14.',
        '<span class="cle">P(A) = 0,4, P(B) = 0,5, P(A∩B) = 0,2</span> → indépendants, P(A∪B) = 0,7.',
        '<span class="cle">P(pluie) = 0,3</span> → P(pas de pluie) = 0,7.',
        '<span class="cle">Loi : 0 ; 1 ; 2 avec 0,25 ; 0,50 ; 0,25</span> → E(X) = 1.',
    ],
    [
        SG("Les règles de calcul",
           ["Règle", "Formule", "Usage"],
           [["Complément", "1 − P(A)", "Événement contraire"],
            ["Union", "P(A)+P(B)−P(A∩B)", "Au moins un"],
            ["Conditionnelle", "P(A∩B)/P(B)", "Sachant B"],
            ["Indépendance", "P(A)·P(B)", "Sans influence"]]),
        SF("Enchaîner deux tirages",
           [("Univers", "Recenser Ω"), ("1er tirage", "P(A1)"),
            ("2e tirage", "P(A2 | A1)"), ("Intersection", "Produire les probabilités"),
            ("Conclusion", "Additionner les branches")]),
        SC("Indépendance / incompatibilité",
           ("Indépendants", ["P(A∩B) = P(A)·P(B)", "Peuvent se réaliser ensemble", "A n'influence pas B"]),
           ("Incompatibles", ["P(A∩B) = 0", "Jamais ensemble", "A exclut B"])),
    ]))

# === INSÉRER LA SUITE ICI ===
