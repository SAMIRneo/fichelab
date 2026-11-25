# -*- coding: utf-8 -*-
"""Verification complete des trois lots CPGE PCSI (lecture seule)."""
import collections
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
from fixtures import BLOCS_ATTENDUS, CJK, INTERDIT_SVG, valider_fiche

FICHIERS = ["cpgepci-mat-part-A.json", "cpgepci-mat-part-B.json", "cpgepci-mat-part-C.json"]
MATIERES = {"Maths": "MA", "Physique": "PH", "Chimie": "CH", "Français": "FR",
            "Philosophie": "PHI", "Anglais": "AN", "Économie": "EC", "Maths / stats": "MS"}
ATTENDU = {"Maths": 10, "Physique": 10, "Chimie": 10, "Français": 5,
           "Philosophie": 5, "Anglais": 6, "Économie": 6, "Maths / stats": 4}

fiches = []
for nom in FICHIERS:
    data = json.load(open(os.path.join(BASE, nom), encoding="utf-8"))
    fiches.extend(data["fiches"])

errs = []
for i, f in enumerate(fiches):
    errs += ["%s f%d: %s" % (FICHIERS[0], i, e) for e in valider_fiche(f, i)]
    if f["filieres"] != ["cpge-pci"]:
        errs.append("f%d: filieres %s" % (i, f["filieres"]))
    if f["annees"] not in (["1re"], ["2e"]):
        errs.append("f%d: annees %s" % (i, f["annees"]))
    if CJK.search(json.dumps(f, ensure_ascii=False)):
        errs.append("f%d: CJK" % i)

# doublons
titres = collections.Counter(f["titre"].lower().strip() for f in fiches)
dups = [t for t, c in titres.items() if c > 1]
prefixes = collections.Counter(re.search(r"Chapitre ([A-Z]+[0-9]+\.)", f["titre"]).group(1)
                               for f in fiches)
pdups = [t for t, c in prefixes.items() if c > 1]

par_mat = collections.Counter(f["matiere"] for f in fiches)
par_an = collections.Counter(f["annees"][0] for f in fiches)
par_lot = collections.Counter()
for nom in FICHIERS:
    data = json.load(open(os.path.join(BASE, nom), encoding="utf-8"))
    par_lot[nom] = len(data["fiches"])

print("ERREURS VALIDATION:", len(errs))
for e in errs[:30]:
    print("  -", e)
print("DOUBLONS TITRES:", dups)
print("DOUBLONS PREFIXES:", pdups)
print("FICHES:", len(fiches), "LOTS:", dict(par_lot))
print("PAR MATIERE:", dict(par_mat))
print("PAR ANNEE:", dict(par_an))
print("ATTENDU OK:", all(par_mat[m] == n for m, n in ATTENDU.items()))
print("POINTS:", sum(len(f["points"]) for f in fiches))
print("QUESTIONS:", sum(len(f["questions"]) for f in fiches))
print("QCM:", sum(1 for f in fiches for q in f["questions"] if q["type"] == "qcm"))
print("TEXTE:", sum(1 for f in fiches for q in f["questions"] if q["type"] == "texte"))
print("SVG:", sum(len(f["schema"]) for f in fiches))
print("BLOCS OK:", all([b["type"] for b in f["affichage"]] == BLOCS_ATTENDUS for f in fiches))
print("CORRECTIONS:", sum(1 for f in fiches for q in f["questions"] if q.get("correction")))
print("INTERDIT SVG:", any(INTERDIT_SVG.search(sc["svg"]) for f in fiches for sc in f["schema"]))

# Verification prefixes par matiere
bad_prefix = [f["titre"] for f in fiches
              if not re.search(r"Chapitre " + MATIERES[f["matiere"]] + r"[0-9]+\.", f["titre"])]
print("PREFIXES MATIERE INCOHERENTS:", bad_prefix)
