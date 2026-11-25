# -*- coding: utf-8 -*-
"""Mecanique commune aux trois generateurs de la filiere bts-sp3s.

Structure identique aux generateurs valides du projet : 12 points de cours,
9 questions corrigees (7 QCM + 2 texte), 7 blocs en ordre strict, 3 schemas
via diag(). Le contenu pedagogique reste ecrit dans les scripts gen_btssp3s_*.py.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_etapes,
                      svg_compare, bloc, valider_et_ecrire)

FIL = ["bts-sp3s"]

REF_BASE = (
    "Référentiel BTS SP3S « Services et prestations des secteurs sanitaire et social » : "
    "arrêté du 24 janvier 2022 portant définition et fixation des conditions de délivrance du diplôme, "
    "Journal officiel du 23 février 2022, annexes II (référentiel des activités professionnelles), "
    "III (référentiel de compétences et savoirs associés), IV (référentiel d'évaluation) et V "
    "(organisation de la formation) ; guide d'accompagnement pédagogique BTS SP3S (mars 2022) ; "
    " Bulletin officiel et ressources éduscol (PNF STMS) ; France compétences, RNCP 36939. "
)

SOURCES = {
    "Culture générale et expression": (
        "Programme de culture générale et expression des BTS (BO spécial, éduscol) ; "
        + REF_BASE),
    "Communication": (
        "Référentiel BTS SP3S, annexe III : cadre juridique de la communication professionnelle, "
        "éthique et déontologie, techniques et outils d'accueil, d'entretien et de communication ; "
        + REF_BASE),
    "Management": (
        "Référentiel BTS SP3S, annexe III, bloc de compétences 4 : collaboration à la gestion de la "
        "structure et du service, coordination et encadrement des équipes ; " + REF_BASE),
    "Droit": (
        "Référentiel BTS SP3S, annexe III, savoirs associés STMS : droits des usagers, droit de la "
        "santé, protection des données, cadre juridique de la communication professionnelle ; "
        + REF_BASE),
    "Économie": (
        "Référentiel BTS SP3S, annexe III : organisation, financement et prestations proposées, "
        "politiques sanitaires et sociales, appui à la logistique financière ; " + REF_BASE),
    "Santé publique et environnement professionnel": (
        "Référentiel BTS SP3S, annexe III : répercussions sanitaires et sociales des pathologies, "
        "typologie des principaux risques professionnels, prévention et qualité de vie au travail ; "
        + REF_BASE),
    "Sciences sanitaires et sociales": (
        "Référentiel BTS SP3S, annexe III, savoirs associés STMS : identité sociale, stigmatisation, "
        "intégration et exclusion, contexte socio-démographique, analyse de la demande et du besoin ; "
        + REF_BASE),
    "Techniques de prévention et d'accompagnement": (
        "Référentiel BTS SP3S, annexe II, domaine 1 : accueil et accompagnement de la personne, "
        "logistique administrative, veille documentaire, prévention et gestion des conflits ; "
        + REF_BASE),
    "Anglais professionnel": (
        "Référentiel BTS SP3S, unité U2 « Communication en langue vivante étrangère » et annexes IV "
        "et V ; programme d'anglais professionnel des BTS (BO spécial, éduscol) ; " + REF_BASE),
    "Méthodologie de projet": (
        "Référentiel BTS SP3S, annexe III, bloc de compétences 2 (U6) : conception et mise en œuvre "
        "d'une démarche de projet et participation à la démarche qualité ; " + REF_BASE),
}

REF = REF_BASE


def S(texte):
    """Decoupe une ligne compacte en elements."""
    return [x.strip() for x in texte.split("|") if x.strip()]


def R(texte):
    """Decoupe une ligne compacte en cellules de tableau / de comparaison."""
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
        return [cellules[i:i + 3] for i in range(0, 9, 3)]
    return [R(x) for x in lignes]


def _cmp(texte):
    """Deux colonnes : titre puis lignes, ecrites en une seule ligne compacte."""
    cellules = R(texte)
    n = len(cellules) // 2
    return (cellules[0], cellules[1:n]), (cellules[n], cellules[n + 1:])


def C(idea, eq, leg, grid, steps, traps, ex, cmp1, cmp2):
    """Contenu pedagogique annexe : une ligne par champ, separable par | ou ~."""
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
        bloc("En situation : exemples", items=[
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
    assert len(aff) == 7 and len(schema) == 3, prefix
    src = source or SOURCES.get(matiere, REF)
    return fiche(FIL, annees, matiere, titre_complet, src,
                 points, questions, aff, schema)
