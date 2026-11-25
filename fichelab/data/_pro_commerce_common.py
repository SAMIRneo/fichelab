# -*- coding: utf-8 -*-
"""Mecanique commune aux trois generateurs de la filiere pro-commerce.

Format strict : 12 points, 9 questions corrigees (7 QCM + 2 texte),
7 blocs en ordre strict, 3 schemas SVG construits par les helpers de fixtures.
Le contenu pedagogique reste ecrit dans les scripts gen_pro_commerce_*.py.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_etapes,
                      svg_compare, bloc, valider_et_ecrire)

FIL = ["pro-commerce"]
ANNEES_OK = ("2nde pro", "1re pro", "Terminale pro")

REF_COMMUN = (
    "Programme du baccalauréat professionnel Métiers du commerce et de la vente : "
    "arrêté du 17 décembre 2018 portant création de la spécialité (modifié) et arrêté "
    "du 21 novembre 2018 relatif aux enseignements dispensés sous statut scolaire "
    "préparant au baccalauréat professionnel (modifié, notamment par l'arrêté du "
    "27 octobre 2025) ; programmes et référentiels publiés au Bulletin officiel de "
    "l'Éducation nationale et sur éduscol (referentiels-professionnels.eduscol.education.fr)."
)

REF_MAT = {
    "Français": "Programme de français de la voie professionnelle, arrêté du 21 novembre 2018 modifié, Bulletin officiel et éduscol.",
    "Maths": "Programme de mathématiques de la voie professionnelle, arrêté du 21 novembre 2018 modifié, Bulletin officiel et éduscol.",
    "Histoire-géo": "Programme d'histoire-géographie de la voie professionnelle, arrêté du 21 novembre 2018 modifié, Bulletin officiel et éduscol.",
    "Anglais": "Programme de langues vivantes (anglais) de la voie professionnelle, arrêté du 21 novembre 2018 modifié, Bulletin officiel et éduscol.",
    "EMC": "Programme d'éducation morale et civique de la voie professionnelle, arrêté du 21 novembre 2018 modifié, Bulletin officiel et éduscol.",
    "Méthodologie": "Programme de la voie professionnelle : démarche documentaire, expression écrite et orale, arrêté du 21 novembre 2018 modifié, Bulletin officiel et éduscol.",
    "Économie et gestion": "Référentiel du bac pro Métiers du commerce et de la vente, arrêté du 17 décembre 2018 modifié, annexes « Économie et gestion », Bulletin officiel et éduscol.",
    "Droit": "Référentiel du bac pro Métiers du commerce et de la vente, arrêté du 17 décembre 2018 modifié, annexes « Droit », Bulletin officiel et éduscol.",
    "Comptabilité": "Référentiel du bac pro Métiers du commerce et de la vente, arrêté du 17 décembre 2018 modifié, annexes « Comptabilité », Bulletin officiel et éduscol.",
    "Pratique professionnelle": "Référentiel d'activités et de compétences du bac pro Métiers du commerce et de la vente, arrêté du 17 décembre 2018 modifié (options A et B), Bulletin officiel et éduscol.",
    "Français professionnel": "Programme de français appliqué aux situations professionnelles, arrêté du 21 novembre 2018 modifié, et référentiel du bac pro MCV, Bulletin officiel et éduscol.",
    "Langues": "Programme de langues vivantes de la voie professionnelle et référentiel du bac pro MCV, arrêté du 21 novembre 2018 modifié, Bulletin officiel et éduscol.",
    "Développement durable": "Programme de la voie professionnelle (éducation au développement durable) et référentiel du bac pro MCV, arrêté du 21 novembre 2018 modifié, Bulletin officiel et éduscol.",
}


def src(matiere):
    """Reference officielle complete : matiere + texte de reference du diplome."""
    return REF_MAT.get(matiere, REF_COMMUN) + " " + REF_COMMUN


def S(texte):
    """Decoupe une ligne compacte en elements (separateur |)."""
    return [x.strip() for x in texte.split("|") if x.strip()]


def R(texte):
    """Decoupe une ligne compacte en cellules (separateur ~)."""
    return [x.strip() for x in texte.split("~") if x.strip()]


def QC(question, options, correct, correction):
    return qcm(question, R(options), correct, correction)


def QT(question, reponse, correction):
    return qt(question, reponse, correction)


def _grid(texte):
    """3 lignes de 3 cellules, ecrites en une seule ligne compacte."""
    lignes = S(texte)
    if len(lignes) == 1:
        cellules = R(lignes[0])
        assert len(cellules) >= 6, "grille : cellules insuffisantes"
        return [cellules[i:i + 3] for i in range(0, len(cellules), 3)]
    return [R(x) for x in lignes]


def _cmp(texte):
    """Deux colonnes : titre puis 3 lignes de chaque cote."""
    cellules = R(texte)
    assert len(cellules) >= 4 and len(cellules) % 2 == 0, "comparaison : cellules impaires"
    n = len(cellules) // 2
    return (cellules[0], cellules[1:n]), (cellules[n], cellules[n + 1:])


def C(idea, eq, leg, grid, steps, traps, ex, cmp1, cmp2):
    """Contenu pedagogique annexe : une ligne par champ, separable par | ou ~."""
    cellules = R(ex.replace("|", "~"))
    assert len(cellules) % 2 == 0, "exemples : nombre impair de cellules"
    paires = [cellules[i:i + 2] for i in range(0, len(cellules), 2)]
    return {"idea": idea, "eq": eq, "leg": leg, "grid": _grid(grid),
            "steps": S(steps), "traps": S(traps), "ex": paires,
            "cmp": (_cmp(cmp1), _cmp(cmp2))}


def build(prefix, titre, matiere, annees, points, questions, c, source=None):
    """Assemble une fiche prototype complete a partir des donnees compactes."""
    for a in annees:
        assert a in ANNEES_OK, "annee invalide %s (%s)" % (a, prefix)
    titre_complet = prefix + " · " + titre
    short = titre.split(":")[0].strip()
    aff = [
        bloc("L'idee en une phrase", texte=c["idea"], type="intro"),
        bloc("La notion a maitriser", eq=c["eq"], leg=c["leg"], type="formule"),
        bloc("Tableau de lecture", items=c["grid"], type="grille"),
        bloc("Les points essentiels du chapitre", items=points[1:5], type="liste"),
        bloc("La demarche pas a pas", items=c["steps"], type="etapes"),
        bloc("Pieges et erreurs frequentes", items=c["traps"], type="attention"),
        bloc("En situation : exemples chiffres", items=[
            '%s : <span class="cle">%s</span>' % (p[0], p[1]) for p in c["ex"]
        ], type="exemples"),
    ]
    schema = [
        diag("1 · " + short, svg_grille(short, ["Notion", "Definition", "Repere"],
                                        c["grid"])),
        diag("2 · Demarche", svg_etapes("Procedure : " + short, c["steps"])),
        diag("3 · A distinguer", svg_compare(short, c["cmp"][0], c["cmp"][1])),
    ]
    assert len(points) == 12, "12 points attendus pour %s (%d)" % (prefix, len(points))
    assert len(questions) == 9, "9 questions attendues pour %s (%d)" % (prefix, len(questions))
    assert sum(1 for q in questions if q.get("type") == "qcm") == 7, prefix
    assert sum(1 for q in questions if q.get("type") == "texte") == 2, prefix
    for p in c["ex"]:
        assert len(p) == 2, "exemples : paires attendues pour %s" % prefix
    assert len(aff) == 7 and len(schema) == 3, prefix
    return fiche(FIL, annees, matiere, titre_complet, source or src(matiere),
                 points, questions, aff, schema)
