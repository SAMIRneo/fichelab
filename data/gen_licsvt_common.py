# -*- coding: utf-8 -*-
"""Fabrique commune aux trois lots de la filiere lic-svt (Licence Sciences de la vie).

Une fiche = un chapitre au format 'prototype' FicheLab :
  filieres=['lic-svt'], annees=['L1'|'L2'|'L3'], matiere exacte du questionnaire,
  12 points, 9 questions (7 QCM + 2 texte), 7 blocs en ordre strict, 3 schemas SVG.

Reference : licence mention Sciences de la vie, arrete du 6 avril 2021 relatif a
la licence (JORF n°0083 du 8 avril 2021), BO special n° 7 du 17 fevrier 2022
(programmes des licences generales), eduscol / ministere de l'Enseignement
superieur, de la Recherche et de l'Innovation.

Contrainte propre a la filiere : le questionnaire ne propose PAS la matiere
'Biologie'. Le contenu biologique (cellule, genetique, physiologie, ecologie,
evolution, biochimie, microbiologie, botanique, zoologie, biologie moleculaire)
est donc reparti dans les matieres disponibles : les titres de fiches portent
le theme biologique, mais la matiere reste une matiere du questionnaire.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_etapes, svg_compare,
                      bloc, valider_et_ecrire, valider_fiche)

REF = ("Licence Sciences de la vie - arrete du 6 avril 2021 relatif a la licence "
       "(JORF n°0083 du 8 avril 2021) - BO special n° 7 du 17 fevrier 2022 - "
       "eduscol / ministere de l'Enseignement superieur, de la Recherche et de "
       "l'Innovation")


def build(cfg):
    """Assemble une fiche complete depuis une configuration compacte."""
    notions = cfg["notions"]                      # 6 couples (nom, definition)
    noms = [n for n, _ in notions]
    defs = [d for _, d in notions]

    # --- 12 points de cours -------------------------------------------------
    points = [cfg["idee"]]
    points += ["%s : %s" % (n, d) for n, d in notions]
    points.append("Repere formel : %s - %s" % (cfg["formule"][0], cfg["formule"][1]))
    points.append("Exemple : %s" % cfg["exemples"][0])
    points.append("Piege : %s" % cfg["attention"][0])
    points.append("Methode : %s" % cfg["etapes"][0])
    points.append(cfg["lien"])

    # --- 9 questions : 6 QCM auto + 1 QCM explicite + 2 rédaction -----------
    questions = []
    for i, (nom, definition) in enumerate(notions):
        idx = i % 4
        autres = [defs[j] for j in range(6) if j != i][:3]
        options = autres[:idx] + [definition] + autres[idx:]
        questions.append(qcm(
            "Quelle est la definition de « %s » ?" % nom,
            options, idx,
            "« %s » : %s. Les autres propositions decrivent d'autres notions du chapitre."
            % (nom, definition)))
    questions.append(qcm(*cfg["qcm_extra"]))
    questions.append(qt(*cfg["qt1"]))
    questions.append(qt(*cfg["qt2"]))

    # --- 7 blocs en ordre strict --------------------------------------------
    grille = cfg["grille"]                        # (titre, colonnes, lignes)
    affichage = [
        bloc("L'idee en une phrase", texte=cfg["idee"], type="intro"),
        bloc("La formule a connaitre", eq=cfg["formule"][0],
             leg=cfg["formule"][1], type="formule"),
        bloc("Tableau de lecture", items=grille[2], type="grille"),
        bloc("A retenir sur le chapitre", items=cfg["liste"], type="liste"),
        bloc("Methode pas a pas", items=cfg["etapes"], type="etapes"),
        bloc("Pieges frequents", items=cfg["attention"], type="attention"),
        bloc("Exemples et applications", items=cfg["exemples"], type="exemples"),
    ]

    # --- 3 schemas SVG ------------------------------------------------------
    cmp_ = cfg["compare"]                        # (titre, (gt, gl), (dt, dl))
    schema = [
        diag("1 · " + grille[0], svg_grille(grille[0], grille[1], grille[2])),
        diag("2 · Procedure", svg_etapes(grille[0] + " : procedure", cfg["etapes"])),
        diag("3 · " + cmp_[0], svg_compare(cmp_[0], cmp_[1], cmp_[2])),
    ]

    source = cfg.get("source", REF + " · notions : " + ", ".join(noms))
    return fiche(
        ["lic-svt"], cfg["annees"], cfg["matiere"],
        "Chapitre %s · %s" % (cfg["prefix"], cfg["titre"]),
        source, points, questions, affichage, schema)


def ecrire(cfgs, chemin):
    """Construit, valide et ecrit un lot."""
    F = [build(c) for c in cfgs]
    valider_et_ecrire(F, chemin)
    return F
