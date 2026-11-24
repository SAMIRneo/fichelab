# -*- coding: utf-8 -*-
import glob
import json
import os

D = os.path.dirname(os.path.abspath(__file__))
for p in sorted(glob.glob(os.path.join(D, "bioalc-cg-*.json"))):
    try:
        fs = json.load(open(p, encoding="utf-8"))["fiches"]
        print(os.path.basename(p), len(fs), "fiches")
        for f in fs:
            print("  -", f["titre"][:85])
    except Exception as e:
        print(os.path.basename(p), "ERREUR", e)
for p in sorted(glob.glob(os.path.join(D, "gen_cg_pc_*.py"))):
    s = open(p, encoding="utf-8").read()
    print(os.path.basename(p), len(s), "octets, fin valider_et_ecrire:",
          s.strip().endswith('valider_et_ecrire(F, "bioalc-cg-part-B.json")') or
          s.strip().endswith('valider_et_ecrire(F, "bioalc-cg-part-A.json")'))
