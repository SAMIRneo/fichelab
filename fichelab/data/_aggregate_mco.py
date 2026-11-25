# -*- coding: utf-8 -*-
"""Aggregation des 4 lots BTS MCO -> lead-mco-final.json, avec validation."""
import json, os, re

D = os.path.dirname(__file__)
fiches, annales = [], []
for part in "ABCD":
    p = os.path.join(D, "lead-mco-partie-%s.json" % part)
    with open(p, encoding="utf-8") as f:
        data = json.load(f)
    fiches.extend(data["fiches"])
    annales.extend(data["annales"])

errors = []
seen = set()
for i, f in enumerate(fiches):
    for k in ("filieres", "annees", "matiere", "titre", "source", "points", "questions"):
        if k not in f:
            errors.append("fiche %d: champ %s manquant" % (i, k))
    if f.get("filieres") != ["bts-mco"]:
        errors.append("fiche %d: filieres" % i)
    if not set(f.get("annees", [])) <= {"BTS1", "BTS2"}:
        errors.append("fiche %d: annees" % i)
    if not f.get("titre", "").startswith("Chapitre"):
        errors.append("fiche %d: titre" % i)
    if not 8 <= len(f.get("points", [])) <= 12:
        errors.append("fiche %d: %d points" % (i, len(f.get("points", []))))
    if not 6 <= len(f.get("questions", [])) <= 10:
        errors.append("fiche %d: %d questions" % (i, len(f.get("questions", []))))
    if f["titre"] in seen:
        errors.append("fiche %d: doublon %s" % (i, f["titre"]))
    seen.add(f["titre"])
    for j, q in enumerate(f.get("questions", [])):
        if q.get("type") == "qcm":
            if len(q.get("options", [])) < 2 or not 0 <= q.get("correct", -1) < len(q["options"]):
                errors.append("fiche %d q%d: correct invalide" % (i, j))
        elif q.get("type") == "texte":
            if not q.get("reponse") or not q.get("correction"):
                errors.append("fiche %d q%d: texte incomplet" % (i, j))
        else:
            errors.append("fiche %d q%d: type inconnu" % (i, j))
        if not q.get("correction"):
            errors.append("fiche %d q%d: correction manquante" % (i, j))

for i, a in enumerate(annales):
    for k in ("filieres", "annees", "titre", "matiere", "type", "contenu", "correction"):
        if k not in a:
            errors.append("annale %d: champ %s manquant" % (i, k))
    if a.get("filieres") != ["bts-mco"] or a.get("type") != "genere":
        errors.append("annale %d: filieres/type" % i)
    if len(a.get("contenu", "")) < 300 or len(a.get("correction", "")) < 300:
        errors.append("annale %d: contenu ou correction trop court" % i)
    numbered = re.findall(r"(?<!\d)([1-9])\.", a["contenu"]) + re.findall(r"QUESTION\s*([1-9])", a["contenu"])
    if len(set(numbered)) < 5:
        errors.append("annale %d: moins de 6 questions" % i)

if errors:
    print("ERREURS:", len(errors))
    for e in errors[:60]:
        print(" -", e)
    raise SystemExit(1)

out = os.path.join(D, "lead-mco-final.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump({"fiches": fiches, "annales": annales}, f, ensure_ascii=False, indent=2)

# Contrôle des artefacts linguistiques non francophones
suspects = re.findall(r"[\u4e00-\u9fff\u3040-\u30ff]+", json.dumps({"fiches": fiches, "annales": annales}, ensure_ascii=False))
print("OK — fiches:", len(fiches), "annales:", len(annales), "artefacts CJK:", len(suspects))
