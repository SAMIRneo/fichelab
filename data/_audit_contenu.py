# -*- coding: utf-8 -*-
"""Controle qualitatif des fiches generees (longueurs, placeholders, sources, variete)."""
import collections
import glob
import json
import os
import re

D = os.path.dirname(os.path.abspath(__file__))
files = [p for p in sorted(glob.glob(os.path.join(D, "generale-mat-part-*.json")))
         if not p.endswith("-MODELE.json")]
allf = []
for p in files:
    allf += json.load(open(p, encoding="utf-8"))["fiches"]

bad = []
placeholder = re.compile(r"\b(TODO|lorem ipsum|TBD|à compléter|XXX)\b", re.I)
for i, f in enumerate(allf):
    for j, pt in enumerate(f["points"]):
        if len(pt) < 70:
            bad.append(("point court", i, j, len(pt), pt[:60]))
        if placeholder.search(pt):
            bad.append(("placeholder point", i, j))
    for k, q in enumerate(f["questions"]):
        if len(q.get("correction", "")) < 30:
            bad.append(("correction courte", i, k, len(q.get("correction", ""))))
        if placeholder.search(json.dumps(q, ensure_ascii=False)):
            bad.append(("placeholder question", i, k))
    if len(f["source"]) < 50:
        bad.append(("source courte", i, len(f["source"])))
    if not re.search(r"BO|arr[eê]t|duscol|programme|circulaire|note de service", f["source"], re.I):
        bad.append(("source non officielle ?", i, f["source"][:80]))

print("fiches:", len(allf))
print("anomalies:", len(bad))
for x in bad[:30]:
    print(" -", x)
print("correct indices:", dict(collections.Counter(
    q.get("correct") for f in allf for q in f["questions"] if q.get("type") == "qcm")))
print("SVG uniques:", len(set(s["svg"] for f in allf for s in f["schema"])),
      "/", sum(len(f["schema"]) for f in allf))
print("sources uniques:", len(set(f["source"] for f in allf)))
print("longueur moyenne point:", sum(len(p) for f in allf for p in f["points"]) // sum(len(f["points"]) for f in allf))
