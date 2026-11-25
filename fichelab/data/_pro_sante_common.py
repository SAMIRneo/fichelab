# -*- coding: utf-8 -*-
"""Mecanique commune aux trois generateurs de la filiere pro-sante (bac pro ASSP).

Meme contract que le modele btsciel : 12 points, 9 questions corrigees
(7 QCM + 2 texte), 7 blocs en ordre strict, 3 schemas diag().
Le contenu pedagogique reste ecrit dans les scripts gen_pro-sante_*.py.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_etapes,
                      svg_compare, bloc, valider_et_ecrire)

FIL = ["pro-sante"]

REF = (
    "Referentiel du baccalaureat professionnel, specialite « Accompagnement, soins et "
    "services a la personne » (ASSP) : arrete du 2 fevrier 2022, NOR MENE2134461A "
    "(JORF du 4 fevrier 2022), annexes II a V (activites, competences, evaluation, "
    "periodes de formation en milieu professionnel), premiere session 2025 ; arrete "
    "du 11 mai 2011 pour les unites anterieures. Programmes d'enseignement general : "
    "arrete du 19 juillet 2011, BO special n° 3 du 28 juin 2012, modalites "
    "d'evaluation arrete du 17 juin 2020 modifie. Ressources eduscol et "
    "referentiels-professionnels.eduscol.education.fr, France competences."
)


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
    assert len(aff) == 7 and len(schema) == 3, prefix
    return fiche(FIL, annees, matiere, titre_complet, source or REF,
                 points, questions, aff, schema)
