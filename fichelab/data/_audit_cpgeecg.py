# -*- coding: utf-8 -*-
"""Audit independant des trois lots CPGE ECG (FicheLab)."""
import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import BLOCS_ATTENDUS, CJK, valider_fiche

BASE = os.path.dirname(os.path.abspath(__file__))
LOTS = [
    ("A", "cpgeecg-mat-part-A.json"),
    ("B", "cpgeecg-mat-part-B.json"),
    ("C", "cpgeecg-mat-part-C.json"),
]
PREFIXES = {"Maths": "MA", "Économie": "EC", "Philosophie": "PHI",
            "Français": "FR", "Anglais": "AN", "Maths / stats": "MS",
            "Méthodologie": "ME"}


def main():
    erreurs = []
    titres = {}
    prefixes = collections.defaultdict(list)
    par_matiere = collections.Counter()
    par_annee = collections.Counter()
    totaux = collections.Counter()

    for lot, nom in LOTS:
        with open(os.path.join(BASE, nom), encoding="utf-8") as fp:
            fiches = json.load(fp)["fiches"]
        for i, f in enumerate(fiches):
            erreurs += ["%s fiche %d: %s" % (lot, i, e)
                        for e in valider_fiche(f, i)]
            t = f["titre"].strip()
            if t.lower() in titres:
                erreurs.append("DOUBLON TITRE %s : %s / %s" % (t, titres[t.lower()], lot))
            titres[t.lower()] = lot
            if f["filieres"] != ["cpge-ecg"]:
                erreurs.append("%s fiche %d: filieres %s" % (lot, i, f["filieres"]))
            if f["annees"] not in (["1re"], ["2e"]):
                erreurs.append("%s fiche %d: annees %s" % (lot, i, f["annees"]))
            if len(f["points"]) != 12:
                erreurs.append("%s fiche %d: %d points" % (lot, i, len(f["points"])))
            if not 9 <= len(f["questions"]) <= 10:
                erreurs.append("%s fiche %d: %d questions" % (lot, i, len(f["questions"])))
            qcm = sum(1 for q in f["questions"] if q.get("type") == "qcm")
            txt = sum(1 for q in f["questions"] if q.get("type") == "texte")
            if qcm < 6 or txt < 2:
                erreurs.append("%s fiche %d: %d QCM / %d texte" % (lot, i, qcm, txt))
            if [b.get("type") for b in f["affichage"]] != BLOCS_ATTENDUS:
                erreurs.append("%s fiche %d: blocs" % (lot, i))
            if len(f["schema"]) != 3:
                erreurs.append("%s fiche %d: %d schemas" % (lot, i, len(f["schema"])))
            if not all(sc.get("svg", "").strip().startswith("<svg") for sc in f["schema"]):
                erreurs.append("%s fiche %d: SVG manquant" % (lot, i))
            if not all(q.get("correction") for q in f["questions"]):
                erreurs.append("%s fiche %d: correction manquante" % (lot, i))
            src = f["source"].lower()
            if "19 juillet 2019" not in src or "bo spécial" not in src:
                erreurs.append("%s fiche %d: source officielle absente" % (lot, i))
            m = re.match(r"^([A-Z]+)(\d+)\.", t)
            if not m:
                erreurs.append("%s fiche %d: titre non prefixe %s" % (lot, i, t))
            else:
                pref, num = m.group(1), int(m.group(2))
                prefixes[pref].append((t, f["matiere"]))
                attendu = PREFIXES.get(f["matiere"])
                if pref != attendu:
                    erreurs.append("%s fiche %d: prefixe %s pour %s" %
                                   (lot, i, pref, f["matiere"]))
            par_matiere[f["matiere"]] += 1
            par_annee[f["annees"][0]] += 1
            totaux["fiches"] += 1
            totaux["points"] += len(f["points"])
            totaux["questions"] += len(f["questions"])
            totaux["qcm"] += qcm
            totaux["texte"] += txt
            totaux["svg"] += len(f["schema"])
        print("OK lot %s : %d fiches" % (lot, len(fiches)))

    for pref, liste in sorted(prefixes.items()):
        nums = [int(re.match(r"^[A-Z]+(\d+)\.", t).group(1)) for t, _ in liste]
        if len(nums) != len(set(nums)):
            erreurs.append("PREFIXE DUPLIQUE %s : %s" % (pref, nums))
        if sorted(nums) != list(range(1, len(nums) + 1)):
            erreurs.append("PREFIXE NON CONTIGU %s : %s" % (pref, sorted(nums)))
        matieres = set(m for _, m in liste)
        if len(matieres) != 1:
            erreurs.append("PREFIXE %s PARTAGE ENTRE MATIERES : %s" % (pref, matieres))

    print("\nTotal : %d fiches, %d points, %d questions (%d QCM / %d texte), %d SVG" %
          (totaux["fiches"], totaux["points"], totaux["questions"],
           totaux["qcm"], totaux["texte"], totaux["svg"]))
    print("Matieres :", json.dumps(dict(par_matiere), ensure_ascii=True))
    print("Annees :", json.dumps(dict(par_annee), ensure_ascii=True))
    print("Prefixes :", json.dumps({p: len(v) for p, v in sorted(prefixes.items())}, ensure_ascii=True))
    print("ERREURS VALIDATION:", len(erreurs))
    print("DOUBLONS TITRES:", [t for t in titres if sum(
        1 for _, nom in LOTS for f in json.load(open(os.path.join(BASE, nom), encoding="utf-8"))["fiches"]
        if f["titre"].strip().lower() == t) > 1])
    for e in erreurs[:40]:
        print(" -", e)
    return 1 if erreurs else 0


if __name__ == "__main__":
    raise SystemExit(main())
