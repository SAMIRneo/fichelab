# -*- coding: utf-8 -*-
"""Helper commun aux lots A/B/C du BUT Genie biologique (FicheLab).

Reproduit strictement le modele 'fiche prototype' de gen_generale_modele.py :
12 points de cours, 9 questions corrigees (7 QCM + 2 texte), 7 blocs dans
l'ordre strict, 3 schemas SVG diag(). Le contenu pedagogique reste dans les
scripts gen_butgb_A/B/C.py.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_flux, svg_etapes,
                      svg_compare, bloc, valider_et_ecrire)

REF = ("Référentiel BUT « Génie biologique », arrêté du 11 mars 2020 (BO n°12 du 19 mars 2020) "
       "· programme national et ressources éduscol / iut.fr · options Diététique, Analyses "
       "biologiques et Bioindustries · blocs de compétences · sources officielles et normes "
       "citées par chapitre")
FIL = ["but-gb"]
F = []


def _gloss_qcm(gloss, i):
    """Six QCM corriges construits a partir du glossaire du chapitre."""
    n = len(gloss)
    j = i % n
    terme, definition = gloss[j]
    autres = [gloss[(j + k) % n] for k in (1, 2, 3)]
    pos = (i * 2 + 1) % 4
    if i % 3 == 0:
        question = "Que désigne « %s » ?" % terme
        pool = [definition] + [o[1] for o in autres]
    elif i % 3 == 1:
        question = "Quel terme correspond a : « %s » ?" % definition
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


def A(code, mat, ans, titre, ref, idee, formule, leg, points, gloss, scn, txt,
      etapes, pieges, chiffres, cmp):
    """Ajoute une fiche complete au lot en cours."""
    questions = [_gloss_qcm(gloss, i) for i in range(6)]
    questions.append(qcm(scn[0], scn[1], scn[2], scn[3]))
    for t in txt:
        questions.append(qt(t[0], t[1], t[2]))
    grille = [["Notion", "Définition", "Repère"]]
    for k, g in enumerate(gloss[:3]):
        grille.append([g[0], g[1], "Notion %d" % (k + 1)])
    retenir = [g[0] + " : " + g[1] for g in gloss[:4]]
    F.append(fiche(
        FIL, ans, mat,
        "Chapitre %s — %s" % (code, titre),
        REF + " • " + ref + " • notions : " + ", ".join(g[0] for g in gloss[:3]),
        points, questions,
        [bloc("L'idée en une phrase", texte=idee, type="intro"),
         bloc("La formule à connaître", eq=formule, leg=leg, type="formule"),
         bloc("Tableau des notions", items=grille, type="grille"),
         bloc("À retenir sur le chapitre", items=retenir, type="liste"),
         bloc("Procéder étape par étape", items=etapes, type="etapes"),
         bloc("Pièges fréquents", items=pieges, type="attention"),
         bloc("En chiffres (à savoir refaire)", items=chiffres, type="exemples")],
        [diag("1 • Repères : " + code,
              svg_grille("Notions clés : " + titre, ["Notion", "Définition", "Repère"],
                         [[g[0], g[1], "Notion %d" % (k + 1)]
                          for k, g in enumerate(gloss[:4])])),
         diag("2 • Procédure : " + code, svg_etapes("Méthode : " + titre, etapes)),
         diag("3 • Distinction : " + code,
              svg_compare("Deux notions à distinguer", (cmp[0][0], cmp[0][1]),
                          (cmp[1][0], cmp[1][1])))]))
