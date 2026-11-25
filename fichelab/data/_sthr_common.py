# -*- coding: utf-8 -*-
"""Mecanique commune aux trois generateurs de la filiere STHR.

20 fiches par lot : 12 points de cours, 9 questions corrigees
(7 QCM + 2 texte), 7 blocs en ordre strict, 3 schemas diag().
Le contenu pedagogique reste ecrit dans les scripts gen_sthr_*.py.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_etapes,
                      svg_compare, bloc, valider_et_ecrire)

FIL = ["sthr"]

REF = (
    "Programmes et ressources de la serie STHR (sciences et technologies de l'hotellerie et de la restauration), "
    "eduscol / DGESCO (programmes en vigueur, ressources d'accompagnement, horaires). "
    "Arrete du 11 mars 2015, BO n° 14 du 2 avril 2015 : enseignements specifiques de seconde STHR "
    "(sciences, economie et gestion hoteliere, sciences et technologies des services, sciences et technologies culinaires). "
    "Arrete du 17 janvier 2019, BO special n° 1 du 22 janvier 2019 (NOR MENE1901630A et MENE1901600A) : "
    "mathematiques, francais, histoire-geographie, langues vivantes et EMC en seconde et premiere technologiques. "
    "Arrete du 15 fevrier 2016, BO n° 11 du 17 mars 2016 (NOR MENE1604565A), modifie par l'arrete du 19 juillet 2019, "
    "BO special n° 8 du 25 juillet 2019 (NOR MENE1921268A) : enseignements de specialite de premiere et terminale STHR "
    "(economie-gestion hoteliere, sciences et technologies culinaires et des services, enseignement scientifique alimentation-environnement). "
    "Arrete du 17 janvier 2019 : programme de philosophie de terminale technologique. "
    "Textes professionnels de reference : code de la sante publique et arrete du 29 septembre 1997 (HACCP), "
    "reglement (CE) n° 852/2004, code du travail et conventions collectives de l'hotellerie-restauration, "
    "code general des impots et code de la sante publique (licence IV), reglement (UE) 2016/679 (RGPD)."
)


def S(texte):
    """Decoupe une ligne compacte en points de cours."""
    return [x.strip() for x in texte.split("|") if x.strip()]


def R(texte):
    """Decoupe une ligne compacte en cellules de tableau."""
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
