# -*- coding: utf-8 -*-
"""Mecanique commune aux trois generateurs de la filiere STL.

Chaque fiche 'prototype' respecte strictement le modele FICHE_UV de index.html :
filieres ['stl'], annees among 2nde / 1re / Terminale, 12 points de cours,
9 questions corrigees (7 QCM + 2 texte), 7 blocs en ordre strict et 3 schemas.
Le contenu pedagogique reste ecrit dans les scripts gen_stl_*.py.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_etapes,
                      svg_compare, bloc, valider_et_ecrire)

FIL = ["stl"]

REF = (
    "Programmes officiels de la serie STL (sciences et technologies de laboratoire), voie "
    "technologique : BO special n° 1 du 22 janvier 2019 (classe de seconde et classe de premiere, "
    "arrete du 17 janvier 2019, NOR MENE1901645A) et BO special n° 8 du 25 juillet 2019 "
    "(classe de terminale) · eduscol, « Programmes et ressources en serie STL » : programmes "
    "de tronc commun et de specialites (biochimie-biologie, sciences physiques et chimiques "
    "en laboratoire) et documents d'accompagnement."
)


def S(texte):
    """Decoupe une ligne compacte en elements (separateur : |)."""
    return [x.strip() for x in texte.split("|") if x.strip()]


def R(texte):
    """Decoupe une ligne compacte en cellules (separateur : ~)."""
    return [x.strip() for x in texte.split("~") if x.strip()]


def QC(question, options, correct, correction):
    return qcm(question, R(options), correct, correction)


def QT(question, reponse, correction):
    return qt(question, reponse, correction)


def _grid(texte):
    """Aplatit les cellules puis les regroupe en lignes de trois."""
    cellules = []
    for ligne in S(texte):
        cellules.extend(R(ligne))
    while len(cellules) % 3:
        cellules.append("")
    return [cellules[i:i + 3] for i in range(0, len(cellules), 3)]


def _cmp(texte):
    """Deux colonnes : titre + 3 lignes pour chaque camps."""
    cellules = R(texte)
    n = len(cellules) // 2
    return (cellules[0], cellules[1:n]), (cellules[n], cellules[n + 1:])


def C(idea, eq, leg, grid, steps, traps, ex, cmp1, cmp2):
    """Contenu pedagogique annexe : un champ par ligne compacte."""
    return {"idea": idea, "eq": eq, "leg": leg, "grid": _grid(grid),
            "steps": S(steps), "traps": S(traps), "ex": [R(x) for x in S(ex)],
            "cmp": (_cmp(cmp1), _cmp(cmp2))}


def build(prefix, titre, mat, annees, points, questions, c):
    """Assemble une fiche prototype complete a partir des donnees compactes."""
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
    assert len(points) == 12, "12 points attendus pour " + prefix
    assert len(questions) == 9, "9 questions attendues pour " + prefix
    assert sum(1 for q in questions if q.get("type") == "qcm") == 7, prefix
    assert sum(1 for q in questions if q.get("type") == "texte") == 2, prefix
    assert all(a in ("1re", "Terminale") for a in annees), prefix
    assert len(aff) == 7 and len(schema) == 3, prefix
    return fiche(FIL, list(annees), mat, titre_complet,
                 REF + " · discipline : " + mat,
                 points, questions, aff, schema)
