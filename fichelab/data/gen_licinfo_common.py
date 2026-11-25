# -*- coding: utf-8 -*-
"""Moteur commun des generateurs de la filiere Licence Informatique (FicheLab).

Transforme une fiche « compacte » (donnees pedagogiques propres a un chapitre)
en une fiche prototype complete au format FICHE_UV :
  12 points, 9 questions (7 QCM + 2 redaction), 7 blocs ordonnes, 3 schemas SVG.

Le moteur n'utilise que les utilitaires de data/fixtures.py. Aucun fichier
interdit (index.html, inject_app.py, audit_filieres.py) n'est modifie.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fixtures import (fiche, qcm, qt, diag, bloc,
                      svg_grille, svg_flux, svg_etapes, svg_compare)

# --- Constructeurs de blocs (type explicite = ordre garanti) ----------------
def Bi(t, x): return bloc(t, texte=x, type="intro")
def Bf(t, e, l): return bloc(t, eq=e, leg=l, type="formule")
def Bg(t, cols, rows): return bloc(t, items=[cols] + list(rows), type="grille")
def Bl(t, items): return bloc(t, items=list(items), type="liste")
def Be(t, items): return bloc(t, items=list(items), type="etapes")
def Ba(t, items): return bloc(t, items=list(items), type="attention")
def Bx(t, items): return bloc(t, items=list(items), type="exemples")

# --- Constructeurs de schemas -----------------------------------------------
def SG(t, cols, rows): return diag(t, svg_grille(t, cols, rows))
def SF(t, steps): return diag(t, svg_flux(t, steps))
def SE(t, steps): return diag(t, svg_etapes(t, steps))
def SC(t, g, d): return diag(t, svg_compare(t, g, d))

STEMS = [
    "Que faut-il retenir de {lab} ?",
    "Quelle affirmation est exacte au sujet de {lab} ?",
    "Dans ce chapitre, {lab} correspond à :",
    "Quelle est la bonne formulation pour {lab} ?",
    "À propos de {lab}, quelle réponse est correcte ?",
    "Quel énoncé décrit correctement {lab} ?",
    "{lab} se définit par :",
]


def build(FIL, AN, MAT, rec, REF):
    """Transforme un enregistrement compact en fiche prototype validable."""
    titre = "%s. · %s" % (rec["p"], rec["t"])
    facts = rec["facts"]                      # 7 tuples (label, valeur courte, detail)
    n = len(facts)
    if n < 7:
        raise ValueError("%s : 7 faits minimum" % titre)
    if len(rec["list"]) < 3:
        raise ValueError("%s : 3 points de liste minimum" % titre)

    # --- 12 points de cours -------------------------------------------------
    pts = [rec["idea"]]
    for lab, val, det in facts[:6]:
        pts.append("%s : %s. %s" % (lab, val, det))
    pts.append("La formule de référence : %s — %s" % (rec["eq"], rec["leg"]))
    lab, val, det = facts[6]
    pts.append("%s : %s. %s" % (lab, val, det))
    for it in rec["list"][:3]:
        pts.append(it)
    pool = list(rec["steps"]) + list(rec["trap"]) + list(rec["ex"])
    k = 0
    while len(pts) < 12:
        pts.append(pool[k % len(pool)])
        k += 1
    pts = pts[:12]

    # --- 9 questions : 7 QCM + 2 redaction ---------------------------------
    qs = []
    for i in range(7):
        lab, val, det = facts[i % n]
        others = []
        for j in range(1, n):
            v = facts[(i + j) % n][1]
            if v != val and v not in others:
                others.append(v)
            if len(others) == 3:
                break
        while len(others) < 3:
            others.append("aucune de ces réponses")
        ci = i % 4
        opts = others[:ci] + [val] + others[ci:]
        opts = opts[:4]
        if val not in opts:
            opts[3] = val
            ci = 3
        qs.append(qcm(STEMS[i].format(lab=lab), opts, opts.index(val), det))

    l0, _v0, d0 = facts[0]
    l1, _v1, _d1 = facts[1]
    qs.append(qt(
        "Expliquer %s et illustrer par un exemple du chapitre." % l0.lower(),
        "%s : %s Exemple : %s." % (l0, d0, rec["ex"][0]),
        "On énonce l'idée centrale, puis on la relie à un exemple concret du chapitre."))
    qs.append(qt(
        "Décrire la démarche pour « %s », puis donner un cas d'application." % rec["t"],
        " ".join(rec["steps"][:4]) + " Cas d'application : " + rec["ex"][1] + ".",
        "On suit les étapes de la méthode dans l'ordre, puis on montre leur application "
        "sur un cas concret. Point de vigilance : " + rec["trap"][0]))

    # --- 7 blocs en ordre strict -------------------------------------------
    aff = [Bi("L'idée en une phrase", rec["idea"]),
           Bf("La formule à connaître", rec["eq"], rec["leg"]),
           Bg("Tableau de synthèse", rec["grille"][0], rec["grille"][1]),
           Bl("À retenir", rec["list"]),
           Be("Méthode pas à pas", rec["steps"]),
           Ba("Pièges fréquents", rec["trap"]),
           Bx("Exemples d'application", rec["ex"])]

    # --- 3 schemas ----------------------------------------------------------
    schemas = []
    for spec in rec["schemas"]:
        kind = spec[0]
        if kind == "g":
            schemas.append(SG(spec[1], spec[2], spec[3]))
        elif kind == "s":
            schemas.append(SF(spec[1], spec[2]))
        elif kind == "e":
            schemas.append(SE(spec[1], spec[2]))
        elif kind == "c":
            schemas.append(SC(spec[1], spec[2], spec[3]))
        else:
            raise ValueError("type de schéma inconnu : %s" % kind)

    return fiche(FIL, AN, MAT, titre, REF, pts, qs, aff, schemas)


def reference(extra=""):
    REF = ("Arrêté du 6 avril 2021 relatif aux licences générales (mention informatique) · "
           "BO spécial n° 7 du 17 février 2022 (programmes de licence) · éduscol / "
           "ministère de l'Enseignement supérieur")
    return REF + (" · " + extra if extra else "")
