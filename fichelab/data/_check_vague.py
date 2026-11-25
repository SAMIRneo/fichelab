# -*- coding: utf-8 -*-
import glob
import json
import os
import sys

D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
from fixtures import valider_fiche

for motif in ("btstourisme", "btscommunication", "btspi", "butgmp", "butgeii", "butgb"):
    print("===", motif)
    for p in sorted(glob.glob(os.path.join(D, "gen_%s_*.py" % motif))):
        s = open(p, encoding="utf-8").read()
        print("  GEN", os.path.basename(p), len(s), "finvalide:",
              "valider_et_ecrire" in s[-300:])
    for p in sorted(glob.glob(os.path.join(D, "%s-mat-part-*.json" % motif))):
        try:
            fs = json.load(open(p, encoding="utf-8"))["fiches"]
            e = []
            for i, f in enumerate(fs):
                e += valider_fiche(f, i)
            print("  JSON", os.path.basename(p), len(fs), "fiches,", len(e), "erreurs")
        except Exception as ex:
            print("  JSON", os.path.basename(p), "ERREUR", ex)
