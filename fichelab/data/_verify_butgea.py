# -*- coding: utf-8 -*-
"""Verification independante des trois lots but-gea (lecture seule)."""
import collections
import glob
import json
import os
import re
import xml.etree.ElementTree as ET

BASE = os.path.dirname(os.path.abspath(__file__))
LOTS = ["butgea-mat-part-A.json", "butgea-mat-part-B.json", "butgea-mat-part-C.json"]
MATS = {"Gestion", "Comptabilité", "Droit", "Marketing", "Communication",
        "Informatique", "Maths / stats", "Anglais professionnel", "Méthodologie"}
ANNEES = {"BUT1", "BUT2", "BUT3"}
BLOCS = ["intro", "formule", "grille", "liste", "etapes", "attention", "exemples"]
CJK = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff]")
INTERDIT = re.compile(r"<script|\bon\w+\s*=|javascript:|<foreignObject", re.I)

tous = []
for lot in LOTS:
    data = json.load(open(os.path.join(BASE, lot), encoding="utf-8"))
    fiches = data["fiches"]
    tous += fiches
    print("\n== %s : %d fiches ==" % (lot, len(fiches)))
    print("points", sum(len(f["points"]) for f in fiches),
          "questions", sum(len(f["questions"]) for f in fiches),
          "qcm", sum(1 for f in fiches for q in f["questions"] if q["type"] == "qcm"),
          "texte", sum(1 for f in fiches for q in f["questions"] if q["type"] == "texte"),
          "svg", sum(len(f["schema"]) for f in fiches))
    for met, val in collections.Counter(f["matiere"] for f in fiches).items():
        print("  matiere:", met, val)
    for an, val in sorted(collections.Counter(a for f in fiches for a in f["annees"]).items()):
        print("  annee:", an, val)

print("\n== Verification globale ==")
errs = []
vues = collections.Counter()
for i, f in enumerate(tous):
    tag = f["titre"]
    if f["filieres"] != ["but-gea"]:
        errs.append("%s: filieres %s" % (tag, f["filieres"]))
    if not f["annees"] or not set(f["annees"]).issubset(ANNEES) or len(f["annees"]) != 1:
        errs.append("%s: annees %s" % (tag, f["annees"]))
    if f["matiere"] not in MATS:
        errs.append("%s: matiere %s" % (tag, f["matiere"]))
    if len(f["points"]) != 12:
        errs.append("%s: points %d" % (tag, len(f["points"])))
    if not 9 <= len(f["questions"]) <= 10:
        errs.append("%s: questions %d" % (tag, len(f["questions"])))
    qcm = sum(1 for q in f["questions"] if q["type"] == "qcm")
    txt = sum(1 for q in f["questions"] if q["type"] == "texte")
    if qcm < 6 or txt < 2:
        errs.append("%s: qcm/texte %d/%d" % (tag, qcm, txt))
    for j, q in enumerate(f["questions"]):
        if not q.get("correction"):
            errs.append("%s q%d: correction vide" % (tag, j))
    types = [b["type"] for b in f["affichage"]]
    if types != BLOCS:
        errs.append("%s: blocs %s" % (tag, types))
    if len(f["schema"]) != 3:
        errs.append("%s: schemas %d" % (tag, len(f["schema"])))
    for j, sc in enumerate(f["schema"]):
        svg = sc.get("svg", "")
        if INTERDIT.search(svg):
            errs.append("%s s%d: SVG interdit" % (tag, j))
        try:
            root = ET.fromstring(svg)
        except ET.ParseError as e:
            errs.append("%s s%d: SVG invalide" % (tag, j))
            continue
        vb = [float(x) for x in root.get("viewBox", "0 0 660 100").split()]
        for t in root.iter("{http://www.w3.org/2000/svg}text"):
            x, y = float(t.get("x", 0)), float(t.get("y", 0))
            if not (0 <= x <= vb[2] and 0 <= y <= vb[3] + 4):
                errs.append("%s s%d: texte hors cadre" % (tag, j))
    if CJK.search(json.dumps(f, ensure_ascii=False)):
        errs.append("%s: CJK" % tag)
    if not f.get("source"):
        errs.append("%s: source vide" % tag)
    vues[tag.strip().lower()] += 1

print("fiches:", len(tous))
print("titres uniques:", len(vues), "doublons:", [t for t, n in vues.items() if n > 1])
print("matieres:", sorted(collections.Counter(f["matiere"] for f in tous).items()))
print("annees:", sorted(collections.Counter(a for f in tous for a in f["annees"]).items()))
print("erreurs:", len(errs))
for e in errs[:30]:
    print(" -", e)

# prefixes par matiere
for mat in sorted(MATS):
    codes = sorted(set(re.search(r"Chapitre GEA (\w+\d+\.)", f["titre"]).group(1)
                       for f in tous if f["matiere"] == mat))
    print("codes", mat, codes)

# comparaison avec les autres lots du catalogue
others = collections.Counter()
for path in glob.glob(os.path.join(BASE, "*.json")):
    if os.path.basename(path) in LOTS:
        continue
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception:
        continue
    fs = d.get("fiches", []) if isinstance(d, dict) else (d if isinstance(d, list) else [])
    for f in fs:
        if isinstance(f, dict) and "titre" in f:
            others[f["titre"].strip().lower()] += 1
clash = [t for t in vues if t in others]
print("titres but-gea present dans un autre lot data/:", len(clash), clash[:10])

# index.html : fiches deja embarquees
html = open(os.path.join(BASE, "..", "index.html"), encoding="utf-8").read()
print("titres but-gea deja presents dans index.html:",
      sum(1 for t in vues if t in html))
