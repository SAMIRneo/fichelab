# -*- coding: utf-8 -*-
"""Mécanique commune aux trois générateurs de la filière bts-esf.

20 fiches par lot : 12 points de cours, 9 questions corrigées
(7 QCM + 2 texte), 7 blocs en ordre strict, 3 schémas diag().
Le contenu pédagogique reste écrit dans les scripts gen_btsesf_A/B/C.py.

Référence : BTS « Économie sociale et familiale », arrêté du 24 janvier 2022
portant définition et fixant les conditions de délivrance du diplôme
(JORF n° 0050 du 1er mars 2022, RNCP36938, première session 2024),
succédant à l'arrêté du 31 juillet 2009. Programmes d'enseignement général
et professionnel applicables en BTS, BO spécial, ressources éduscol,
France compétences, textes du Code de l'action sociale et des familles,
du Code de la santé publique et du Code du travail.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_etapes,
                      svg_compare, bloc, valider_et_ecrire)

FIL = ["bts-esf"]
ANNEES = ["BTS1", "BTS2"]  # ANNEES.bts de index.html

REF = (
    "Référentiel BTS « Économie sociale et familiale » : arrêté du 24 janvier 2022 "
    "portant définition et fixant les conditions de délivrance du diplôme (JORF n° 0050 "
    "du 1er mars 2022, RNCP36938, première session 2024), succédant à l'arrêté du "
    "31 juillet 2009 · programmes d'enseignement général et professionnel applicables "
    "en BTS, Bulletin officiel spécial et ressources éduscol (BTS ESF) · France compétences "
    "· Code de l'action sociale et des familles, Code de la santé publique, Code du travail "
    "et règlement (UE) 2016/679 (RGPD)."
)


def S(texte):
    """Découpe une ligne compacte en éléments (séparateur '|')."""
    return [x.strip() for x in texte.split("|") if x.strip()]


def R(texte):
    """Découpe une ligne compacte en cellules (séparateur '~')."""
    return [x.strip() for x in texte.split("~") if x.strip()]


def QC(question, options, correct, correction):
    return qcm(question, R(options), correct, correction)


def QT(question, reponse, correction):
    return qt(question, reponse, correction)


def _grid(texte):
    """3 lignes de 3 cellules, écrites en une seule ligne compacte."""
    lignes = S(texte)
    if len(lignes) == 1:
        cellules = R(lignes[0])
        return [cellules[i:i + 3] for i in range(0, 9, 3)]
    return [R(x) for x in lignes]


def _cmp(texte):
    """Deux colonnes : titre puis lignes, écrites en une seule ligne compacte."""
    cellules = R(texte)
    n = len(cellules) // 2
    return (cellules[0], cellules[1:n]), (cellules[n], cellules[n + 1:])


def C(idea, eq, leg, grid, steps, traps, ex, cmp1, cmp2):
    """Contenu pédagogique annexe : une ligne par champ, séparable par | ou ~."""
    return {"idea": idea, "eq": eq, "leg": leg, "grid": _grid(grid),
            "steps": S(steps), "traps": S(traps), "ex": [R(x) for x in S(ex)],
            "cmp": (_cmp(cmp1), _cmp(cmp2))}


def build(prefix, titre, matiere, annees, points, questions, c, ref=""):
    """Assemble une fiche prototype complète à partir des données compactes."""
    titre_complet = prefix + " · " + titre
    short = titre.split(":")[0].strip()
    aff = [
        bloc("L'idée en une phrase", texte=c["idea"], type="intro"),
        bloc("La notion à maîtriser", eq=c["eq"], leg=c["leg"], type="formule"),
        bloc("Tableau de lecture", items=c["grid"], type="grille"),
        bloc("Les points essentiels du chapitre", items=points[1:5], type="liste"),
        bloc("La démarche pas à pas", items=c["steps"], type="etapes"),
        bloc("Pièges et erreurs fréquentes", items=c["traps"], type="attention"),
        bloc("En situation : exemples chiffrés", items=[
            '%s : <span class="cle">%s</span>' % (p[0], p[1]) for p in c["ex"]
        ], type="exemples"),
    ]
    schema = [
        diag("1 · " + short, svg_grille(short, ["Notion", "Définition", "Repère"],
                                        c["grid"])),
        diag("2 · Démarche", svg_etapes("Procédure : " + short, c["steps"])),
        diag("3 · À distinguer", svg_compare(short, c["cmp"][0], c["cmp"][1])),
    ]
    assert len(points) == 12, "12 points attendus pour " + prefix
    assert len(questions) == 9, "9 questions attendues pour " + prefix
    assert sum(1 for q in questions if q.get("type") == "qcm") == 7, prefix
    assert sum(1 for q in questions if q.get("type") == "texte") == 2, prefix
    assert len(aff) == 7 and len(schema) == 3, prefix
    source = REF + (" · " + ref if ref else "")
    return fiche(FIL, annees, matiere, titre_complet, source,
                 points, questions, aff, schema)
