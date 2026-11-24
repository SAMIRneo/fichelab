# -*- coding: utf-8 -*-
"""Outils partages par les lots gen_commerce_A.py, gen_commerce_B.py et gen_commerce_C.py.

Structure copiee de data/gen_generale_modele.py : 12 points, 10 questions
(8 QCM + 2 texte), 7 blocs d'affichage en ordre strict, 3 schemas via diag().
L'identifiant de filiere est unique : "commerce" ; annees : Bac+1, Bac+2, Bac+3.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_etapes,
                      svg_compare, bloc)

REF = (
    "Référentiel BUT « Techniques de commercialisation » (arrêté du 11 mars 2020, "
    "BO n°12 du 19 mars 2020), compétences C1 à C6 et ressources R1 à R6 ; "
    "référentiel BUT « Gestion des entreprises et des administrations » ; "
    "programmes bachelor des écoles de commerce et de gestion (fiches RNCP) · "
    "éduscol, iut.fr, onisep.fr"
)

BLOCS = ["intro", "formule", "grille", "liste", "etapes", "attention", "exemples"]


def _qcm_gloss(gloss, i):
    """Un QCM par notion du glossaire, avec formulation et position variables."""
    j = i % len(gloss)
    terme, definition, _repere = gloss[j]
    autres = [gloss[(j + k) % len(gloss)] for k in (1, 2, 3)]
    variante = (i % 3 + i // len(gloss)) % 3
    if variante == 0:
        question = "Que désigne le terme « %s » ?" % terme
        pool = [definition] + [o[1] for o in autres]
    elif variante == 1:
        question = "Quel terme correspond à la définition : « %s » ?" % definition
        pool = [terme] + [o[0] for o in autres]
    else:
        question = "Quelle affirmation est exacte à propos de « %s » ?" % terme
        pool = [definition] + [o[1] for o in autres]
    pos = (i * 3 + 1) % 4
    options = [""] * 4
    options[pos] = pool[0]
    k = 0
    for idx in range(4):
        if idx != pos:
            options[idx] = pool[k + 1]
            k += 1
    detail = " ; ".join("%s : %s" % (o[0], o[1]) for o in autres)
    correction = ("Réponse correcte : %s — %s. Les autres propositions décrivent %s."
                  % (terme, definition, detail))
    return qcm(question, options, pos, correction,
               contexte="Notion du référentiel écoles de commerce / BUT Techniques de commercialisation.")


def A(lot, code, mat, an, titre, ref, idee, formule, leg, points, gloss,
      scn, txt, etapes, pieges, chiffres, cmp):
    """Ajoute une fiche complete au lot A, B ou C."""
    questions = [_qcm_gloss(gloss, i) for i in range(7)]
    questions.append(qcm(scn[0], scn[1], scn[2], scn[3],
                         contexte=scn[4] if len(scn) > 4 else "",
                         calcul=bool(len(scn) > 5 and scn[5])))
    for t in txt:
        questions.append(qt(t[0], t[1], t[2],
                            contexte=t[3] if len(t) > 3 else "",
                            calcul=bool(len(t) > 4 and t[4])))
    grille = [["Notion", "Définition courte", "Repère"]]
    for g in gloss[:3]:
        grille.append([g[0], g[1], g[2]])
    retenir = ["%s : %s" % (g[0], g[1]) for g in gloss[:4]]
    prefix = "Commerce %s · %s · %s" % (lot, code.rstrip("."), titre)
    F.append(fiche(
        ["commerce"], [an], mat, prefix,
        REF + " · " + ref + " · notions : " + ", ".join(g[0] for g in gloss[:3]),
        points, questions,
        [bloc("L'idée en une phrase", texte=idee, type="intro"),
         bloc("La formule à connaître", eq=formule, leg=leg, type="formule"),
         bloc("Tableau des notions clés", items=grille, type="grille"),
         bloc("À retenir sur le chapitre", items=retenir, type="liste"),
         bloc("Méthode en cinq étapes", items=etapes, type="etapes"),
         bloc("Pièges fréquents", items=pieges, type="attention"),
         bloc("En chiffres (à savoir refaire)", items=chiffres, type="exemples")],
        [diag("1 · Repères : " + code.rstrip("."),
              svg_grille("Notions clés : " + titre,
                         ["Notion", "Définition courte", "Repère"],
                         [[g[0], g[1], "Notion %d" % (k + 1)]
                          for k, g in enumerate(gloss[:4])])),
         diag("2 · Procédure : " + code.rstrip("."),
              svg_etapes("Méthode : " + titre, etapes)),
         diag("3 · Distinction : " + code.rstrip("."),
              svg_compare("Deux situations à distinguer",
                          (cmp[0][0], cmp[0][1]), (cmp[1][0], cmp[1][1])))]))


F = []
