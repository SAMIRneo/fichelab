# -*- coding: utf-8 -*-
"""Mecanique commune aux trois generateurs de la filiere STD2A.

Structure 'fiche prototype' FicheLab retenue pour STD2A :
  12 points de cours, 9 questions corrigees (7 QCM + 2 texte),
  7 blocs en ordre strict (intro/formule/grille/liste/etapes/attention/exemples),
  3 schemas SVG construits par les helpers de fixtures.py (grille, etapes, comparaison).

Le contenu pedagogique reste ecrit dans les scripts gen_std2a_*.py.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_etapes,
                      svg_compare, bloc, valider_et_ecrire)

FIL = ["std2a"]

REF = (
    "Programmes officiels de la serie STD2A (sciences et technologies du design et des arts "
    "appliques) : arrete du 8 fevrier 2011 (NOR MENE1104094A, BO special n° 3 du 17 mars 2011) "
    "fixant le programme de design et arts appliques du cycle terminal ; arrete du 17 janvier 2019 "
    "fixant le programme des enseignements de specialite de premiere et terminale STD2A (design et "
    "metiers d'art, analyse et methode en design, conception et creation en design et metiers "
    "d'art), BO special n° 1 du 22 janvier 2019 ; arrete du 8 fevrier 2011 (NOR MENE1104152A) "
    "pour les mathematiques de premiere STD2A ; programmes de francais, histoire-geographie, "
    "anglais, EMC et philosophie des classes de 2nde, 1re et terminale technologique (Bulletin "
    "officiel special). Ressources eduscol : "
    "https://eduscol.education.gouv.fr/5850/programmes-et-ressources-en-serie-std2a."
)


def S(texte):
    """Decoupe une ligne compacte en elements (separateur '|')."""
    return [x.strip() for x in texte.split("|") if x.strip()]


def R(texte):
    """Decoupe une ligne compacte en cellules de tableau (separateur '~')."""
    return [x.strip() for x in texte.split("~") if x.strip()]


def QC(question, options, correct, correction):
    """QCM : options ecrites 'a~b~c~d', correct = index 0-based."""
    return qcm(question, R(options), correct, correction)


def QT(question, reponse, correction):
    """Question de texte : reponse developpee et attendu de correction."""
    return qt(question, reponse, correction)


def _grid(texte):
    """3 lignes de 3 cellules ecrites sur une ligne, ou lignes separees par '|'."""
    lignes = S(texte)
    if len(lignes) == 1:
        cellules = R(lignes[0])
        return [cellules[i:i + 3] for i in range(0, 9, 3)]
    return [R(x) for x in lignes]


def _cmp(texte):
    """Deux colonnes : titre puis lignes, ecrites sur une ligne compacte."""
    cellules = R(texte)
    n = len(cellules) // 2
    return (cellules[0], cellules[1:n]), (cellules[n], cellules[n + 1:])


def C(idea, eq, leg, grid, steps, traps, ex, cmp1, cmp2):
    """Contenu pedagogique annexe : un champ par ligne compacte."""
    return {"idea": idea, "eq": eq, "leg": leg, "grid": _grid(grid),
            "steps": S(steps), "traps": S(traps), "ex": [R(x) for x in S(ex)],
            "cmp": (_cmp(cmp1), _cmp(cmp2))}


def build(prefix, titre, matiere, annees, points, questions, c, source=None):
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
    assert len(points) == 12, "%s : %d points (attendu 12)" % (prefix, len(points))
    assert len(questions) == 9, "9 questions attendues pour " + prefix
    assert sum(1 for q in questions if q.get("type") == "qcm") == 7, prefix
    assert sum(1 for q in questions if q.get("type") == "texte") == 2, prefix
    assert len(aff) == 7 and len(schema) == 3, prefix
    return fiche(FIL, annees, matiere, titre_complet, source or REF,
                 points, questions, aff, schema)
