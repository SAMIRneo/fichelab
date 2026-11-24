# -*- coding: utf-8 -*-
import collections
import json
import re
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import valider_fiche, BLOCS_ATTENDUS, CJK

BASE = os.path.dirname(os.path.abspath(__file__))
ATTENDU = {
    "A": {"Maths / stats": 12, "Statistiques": 8},
    "B": {"Informatique": 10, "Méthodologie universitaire": 10},
    "C": {"Français": 5, "Anglais": 5, "Psychologie": 5, "Économie": 5},
}
PREFIXES = {
    "A": ([f"MS{i}." for i in range(1, 13)], [f"ST{i}." for i in range(1, 9)]),
    "B": ([f"IN{i}." for i in range(1, 11)], [f"MU{i}." for i in range(1, 11)]),
    "C": ([f"PF{i}." for i in range(1, 6)], [f"AN{i}." for i in range(1, 6)],
          [f"PSY{i}." for i in range(1, 6)], [f"EC{i}." for i in range(1, 6)]),
}
MATIERES = set().union(*[set(d) for d in ATTENDU.values()])
tout = []
problems = []
for lot in "ABC":
    path = os.path.join(BASE, f"licmaths-mat-part-{lot}.json")
    data = json.load(open(path, encoding="utf-8"))
    fiches = data["fiches"]
    print(f"LOT {lot} : {len(fiches)} fiches")
    cnt = collections.Counter(f["matiere"] for f in fiches)
    yrs = collections.Counter(a for f in fiches for a in f["annees"])
    print("  matieres :", dict(cnt))
    print("  annees   :", dict(yrs))
    if cnt != collections.Counter(ATTENDU[lot]):
        problems.append(f"lot {lot}: matieres {dict(cnt)} != {ATTENDU[lot]}")
    for i, f in enumerate(fiches):
        errs = valider_fiche(f, i)
        if errs:
            problems.extend(f"lot {lot} fiche {i}: {e}" for e in errs)
        if f["filieres"] != ["lic-maths"]:
            problems.append(f"lot {lot} fiche {i}: filieres {f['filieres']}")
        if not set(f["annees"]) <= {"L1", "L2", "L3"}:
            problems.append(f"lot {lot} fiche {i}: annees {f['annees']}")
        if f["matiere"] not in MATIERES:
            problems.append(f"lot {lot} fiche {i}: matiere {f['matiere']}")
        types = [b["type"] for b in f["affichage"]]
        if types != BLOCS_ATTENDUS:
            problems.append(f"lot {lot} fiche {i}: blocs {types}")
        if len(f["schema"]) != 3 or len({s["titre"] for s in f["schema"]}) != 3:
            problems.append(f"lot {lot} fiche {i}: schemas")
        if len(f["points"]) != 12 or len(f["questions"]) != 9:
            problems.append(f"lot {lot} fiche {i}: points/questions")
        nqcm = sum(q["type"] == "qcm" for q in f["questions"])
        ntxt = sum(q["type"] == "texte" for q in f["questions"])
        if nqcm < 6 or ntxt < 2:
            problems.append(f"lot {lot} fiche {i}: qcm/texte {nqcm}/{ntxt}")
        if CJK.search(json.dumps(f, ensure_ascii=False)):
            problems.append(f"lot {lot} fiche {i}: CJK")
        if not re.match(r"^(MS|ST|IN|MU|PF|AN|PSY|EC)\d+\. · .{12,}", f["titre"]):
            problems.append(f"lot {lot} fiche {i}: titre non prefixe {f['titre']}")
        for q in f["questions"]:
            if len(set(q.get("options", []))) != len(q.get("options", [])):
                problems.append(f"lot {lot} fiche {i}: options dupliquees")
        tout.append((lot, f))
    prefixes = [f["titre"].split(".")[0] + "." for f in fiches]
    expected = [p for grp in PREFIXES[lot] for p in grp]
    if sorted(prefixes) != sorted(expected):
        problems.append(f"lot {lot}: prefixes {prefixes}")

titles = collections.Counter(f["titre"].strip().lower() for _, f in tout)
dups = [t for t, n in titles.items() if n > 1]
prefix_all = collections.Counter(f["titre"].split(".")[0] for _, f in tout)
dup_prefix = [p for p, n in prefix_all.items() if n > 1]
n = len(tout)
print("TOTAL fiches :", n)
print("Titres uniques :", len(titles), "| doublons titres :", len(dups))
print("Prefixes uniques :", len(prefix_all), "| doublons prefixes :", len(dup_prefix))
print("Points:", sum(len(f["points"]) for _, f in tout))
print("Questions:", sum(len(f["questions"]) for _, f in tout))
print("QCM:", sum(q["type"] == "qcm" for _, f in tout for q in f["questions"]))
print("Textes:", sum(q["type"] == "texte" for _, f in tout for q in f["questions"]))
print("SVG:", sum(len(f["schema"]) for _, f in tout))
print("PROBLEMES :", len(problems))
for p in problems[:30]:
    print(" -", p)
if dups:
    print("Doublons:", dups)
if dup_prefix:
    print("Prefixes dupliques:", dup_prefix)
sys.exit(1 if problems or dups or dup_prefix else 0)
