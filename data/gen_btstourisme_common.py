# -*- coding: utf-8 -*-
"""Noyau commun des lots BTS Tourisme (fiches au format 'fiche prototype').

Une fiche = 12 points de cours, 9 questions corrigees (7 QCM + 2 texte),
7 blocs en ordre strict et 3 schemas SVG. Ce module ne contient que la
mecanique : le contenu pedagogique est ecrit dans gen_btstourisme_A/B/C.py.

Reference : BTS « Tourisme » — arrete du 5 mars 2019 modifie (JORF n°0093 du
19 avril 2019, RNCP37890), arrete du 30 mars 2026 applicable session 2027,
BO special et éduscol. La consigne initiale mentionnait l'arrete du 14 decembre
2016 : celui-ci porte sur le BTS MCO ; la clarification figure dans
BTSTOURISME-PROGRAMME.md et AUDIT-BTSTOURISME.md.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_etapes,
                      svg_compare, bloc)

REF = (
    "Référentiel BTS « Tourisme », arrêté du 5 mars 2019 modifié (JORF n°0093 du "
    "19 avril 2019, RNCP37890) et arrêté modificatif du 30 mars 2026 (session 2027) "
    "· BO spécial · éduscol, référentiels professionnels · Code de la consommation, "
    "Code du travail et règlement RGPD · 65 896 vœux Parcoursup 2026 (SOURCES.md)"
)
FIL = ["bts-tourisme"]


def _gloss_qcm(gloss, i):
    """Fabrique un QCM de definitioin a partir des 6 notions du chapitre."""
    n = len(gloss)
    j = i % n
    terme, definition = gloss[j]
    autres = [gloss[(j + k) % n] for k in (1, 2, 3)]
    pos = (i * 2 + 1) % 4
    if i % 3 == 0:
        question = "Que désigne « %s » ?" % terme
        pool = [definition] + [o[1] for o in autres]
    elif i % 3 == 1:
        question = "Quel terme correspond à : « %s » ?" % definition
        pool = [terme] + [o[0] for o in autres]
    else:
        question = "Quelle affirmation décrit correctement « %s » ?" % terme
        pool = [definition] + [o[1] for o in autres]
    options = [""] * 4
    options[pos] = pool[0]
    k = 0
    for idx in range(4):
        if idx != pos:
            options[idx] = pool[k + 1]
            k += 1
    return qcm(question, options, pos,
               definition + " Les autres propositions décrivent d'autres notions du chapitre.")


def A(F, code, mat, ans, titre, ref, idee, formule, leg, points, gloss,
      scn, txt, etapes, pieges, chiffres, cmp):
    """Ajoute une fiche complete : 12 points, 9 questions, 7 blocs, 3 diag().

    code   : 'MA1.' (prefixe unique, avec le point)
    ans    : ['BTS1'], ['BTS2'] ou ['BTS1','BTS2']
    gloss  : 6 couples (terme, definition courte) -> 6 QCM
    scn    : (question, [4 options], index correct, correction) -> 1 QCM
    txt    : [(question, reponse, correction), ...] -> 2 questions texte
    cmp    : ((titre gauche, [3 lignes]), (titre droite, [3 lignes]))
    """
    assert len(points) == 12, (code, "points", len(points))
    assert len(gloss) == 6, (code, "gloss", len(gloss))
    assert 4 <= len(etapes) <= 5, (code, "etapes", len(etapes))
    assert len(txt) == 2, (code, "txt", len(txt))
    assert len(cmp) == 2 and all(len(c[1]) >= 3 for c in cmp), (code, "cmp")
    assert len(chiffres) >= 3 and len(pieges) >= 4, (code, "exemples/pieges")

    questions = [_gloss_qcm(gloss, i) for i in range(6)]
    questions.append(qcm(scn[0], scn[1], scn[2], scn[3]))
    for t in txt:
        questions.append(qt(t[0], t[1], t[2]))

    grille = [["Notion", "Définition", "Repère"]]
    for k, g in enumerate(gloss[:4]):
        grille.append([g[0], g[1], "Notion %d" % (k + 1)])
    retenir = [g[0] + " : " + g[1] for g in gloss]

    affichage = [
        bloc("L'idée en une phrase", texte=idee, type="intro"),
        bloc("La formule à connaître", eq=formule, leg=leg, type="formule"),
        bloc("Tableau des notions", items=grille, type="grille"),
        bloc("À retenir sur le chapitre", items=retenir, type="liste"),
        bloc("Procéder étape par étape", items=list(etapes), type="etapes"),
        bloc("Pièges fréquents", items=list(pieges), type="attention"),
        bloc("En chiffres (à savoir refaire)", items=list(chiffres), type="exemples"),
    ]
    schema = [
        diag("1 · Repères : " + code,
             svg_grille("Notions clés : " + titre,
                        ["Notion", "Définition", "Repère"], grille[1:])),
        diag("2 · Procédure : " + code,
             svg_etapes("Méthode : " + titre, list(etapes))),
        diag("3 · Distinction : " + code,
             svg_compare("Deux aspects à distinguer", (cmp[0][0], cmp[0][1]),
                         (cmp[1][0], cmp[1][1]))),
    ]
    F.append(fiche(
        FIL, ans, mat, "Chapitre %s · %s" % (code, titre),
        REF + " · " + ref + " · notions : " + ", ".join(g[0] for g in gloss[:3]),
        points, questions, affichage, schema,
    ))
