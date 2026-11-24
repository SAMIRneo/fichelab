# -*- coding: utf-8 -*-
"""Verification croisee des trois lots de la filiere lic-lea."""
import collections
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import BLOCS_ATTENDUS, CJK, INTERDIT_SVG, valider_fiche
import xml.etree.ElementTree as ET

BASE = os.path.dirname(os.path.abspath(__file__))
LOTS = ["A", "B", "C"]
ATTENDU = {
    "Anglais": (10, {"AN1", "AN2", "AN3", "AN4", "AN5", "AN6", "AN7", "AN8", "AN9", "AN10"}),
    "Français": (10, {"PF1", "PF2", "PF3", "PF4", "PF5", "PF6", "PF7", "PF8", "PF9", "PF10"}),
    "Droit": (8, {"DR1", "DR2", "DR3", "DR4", "DR5", "DR6", "DR7", "DR8"}),
    "Économie": (7, {"EC1", "EC2", "EC3", "EC4", "EC5", "EC6", "EC7"}),
    "Méthodologie universitaire": (5, {"MU1", "MU2", "MU3", "MU4", "MU5"}),
    "Informatique": (5, {"IN1", "IN2", "IN3", "IN4", "IN5"}),
    "Statistiques": (5, {"ST1", "ST2", "ST3", "ST4", "ST5"}),
    "Psychologie": (5, {"LPSY1", "LPSY2", "LPSY3", "LPSY4", "LPSY5"}),
    "Maths / stats": (5, {"MS1", "MS2", "MS3", "MS4", "MS5"}),
}
ANNEES_OK = {"L1", "L2", "L3"}

fiches = {}
for lot in LOTS:
    path = os.path.join(BASE, "liclea-mat-part-%s.json" % lot)
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    fiches[lot] = data["fiches"]
    print("LOT %s : %d fiches" % (lot, len(fiches[lot])))

problems = []
allf = [f for lot in LOTS for f in fiches[lot]]
print("TOTAL :", len(allf), "fiches")

# 1. validation fixtures
errs = []
for i, f in enumerate(allf):
    errs += ["fiche %d: %s" % (i, e) for e in valider_fiche(f, i)]
print("valider_fiche :", len(errs), "erreur(s)")
problems += errs

# 2. compteurs par lot / matiere / annee
for lot in LOTS:
    fs = fiches[lot]
    pts = sum(len(f["points"]) for f in fs)
    qs = sum(len(f["questions"]) for f in fs)
    qcm = sum(1 for f in fs for q in f["questions"] if q["type"] == "qcm")
    txt = sum(1 for f in fs for q in f["questions"] if q["type"] == "texte")
    svg = sum(len(f["schema"]) for f in fs)
    print("  %s: %d points, %d questions (%d QCM + %d texte), %d SVG" %
          (lot, pts, qs, qcm, txt, svg))

par_matiere = collections.Counter(f["matiere"] for f in allf)
par_annee = collections.Counter()
for f in allf:
    for a in f["annees"]:
        par_annee[a] += 1
print("Matieres :", dict(par_matiere))
print("Annees :", dict(par_annee))

for mat, (n, prefixes) in ATTENDU.items():
    if par_matiere.get(mat, 0) != n:
        problems.append("matiere %s: %d fiches, attendu %d" % (mat, par_matiere.get(mat, 0), n))
prefixes_vus = set()
for f in allf:
    m = re.match(r"^Chapitre ([A-Z0-9]+) \(LEA\) · (.+)$", f["titre"])
    if not m:
        problems.append("titre non prefixe: %s" % f["titre"])
        continue
    pref = m.group(1)
    prefixes_vus.add(pref)
    if pref not in ATTENDU.get(f["matiere"], (0, set()))[1]:
        problems.append("prefixe %s inattendu pour %s" % (pref, f["matiere"]))
attendus_prefix = set().union(*[v[1] for v in ATTENDU.values()])
if prefixes_vus != attendus_prefix:
    problems.append("prefixes manquants: %s / en trop: %s" %
                    (sorted(attendus_prefix - prefixes_vus), sorted(prefixes_vus - attendus_prefix)))

# 3. conformite stricte
for i, f in enumerate(allf):
    if f["filieres"] != ["lic-lea"]:
        problems.append("fiche %d: filieres %s" % (i, f["filieres"]))
    if not all(a in ANNEES_OK for a in f["annees"]) or not f["annees"]:
        problems.append("fiche %d: annees %s" % (i, f["annees"]))
    if len(f["points"]) != 12:
        problems.append("fiche %d: points %d" % (i, len(f["points"])))
    if not 9 <= len(f["questions"]) <= 10:
        problems.append("fiche %d: questions %d" % (i, len(f["questions"])))
    n_qcm = sum(1 for q in f["questions"] if q["type"] == "qcm")
    n_txt = sum(1 for q in f["questions"] if q["type"] == "texte")
    if n_qcm < 6 or n_txt < 2:
        problems.append("fiche %d: %d QCM / %d texte" % (i, n_qcm, n_txt))
    if [b["type"] for b in f["affichage"]] != BLOCS_ATTENDUS:
        problems.append("fiche %d: blocs" % i)
    if len(f["schema"]) != 3:
        problems.append("fiche %d: schemas %d" % (i, len(f["schema"])))
    if not f.get("source") or "6 avril 2021" not in f["source"]:
        problems.append("fiche %d: source incomplete" % i)
    if CJK.search(json.dumps(f, ensure_ascii=False)):
        problems.append("fiche %d: CJK" % i)
    for sc in f["schema"]:
        if INTERDIT_SVG.search(sc["svg"]):
            problems.append("fiche %d: SVG interdit" % i)
        ET.fromstring(sc["svg"])

# 4. doublons internes et inter-lots
titles = [f["titre"].strip().lower() for f in allf]
dup_int = [t for t, n in collections.Counter(titles).items() if n > 1]
print("Doublons internes lic-lea :", len(dup_int), dup_int[:5])
problems += ["doublon interne: %s" % t for t in dup_int]

# 5. doublons avec le catalogue existant
existants = set()
for p in glob.glob(os.path.join(BASE, "*.json")):
    if os.path.basename(p).startswith("liclea-"):
        continue
    try:
        with open(p, encoding="utf-8") as fp:
            obj = json.load(fp)
    except Exception:
        continue
    items = obj if isinstance(obj, list) else obj.get("fiches", [])
    for f in items:
        if isinstance(f, dict) and f.get("titre"):
            existants.add(f["titre"].strip().lower())
with open(os.path.join(BASE, "..", "index.html"), encoding="utf-8", errors="ignore") as fp:
    for line in fp:
        if line.startswith("const EXTRA_FICHES = "):
            try:
                extra = json.loads(line[line.index("["):line.rindex("]") + 1])
            except Exception:
                extra = []
            for f in extra:
                if f.get("titre"):
                    existants.add(f["titre"].strip().lower())
            break
collisions = sorted(set(titles) & existants)
print("Titres existants dans le catalogue :", len(existants))
print("Collisions avec le catalogue :", len(collisions), collisions[:5])
problems += ["collition catalogue: %s" % t for t in collisions]

# 6. sources officielles mobilisees
src = " ".join(f["source"] for f in allf)
for ref in ["6 avril 2021", "BO special", "eduscol", "RNCP 39173"]:
    if ref not in src:
        problems.append("source manquante: %s" % ref)

print("\nVERDICT :", "OK" if not problems else "%d PROBLEME(S)" % len(problems))
for p in problems[:30]:
    print(" -", p)
sys.exit(0 if not problems else 1)
