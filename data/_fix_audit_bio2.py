# -*- coding: utf-8 -*-
"""Suite des corrections audit BIOALC : A-04, A-02, A-06."""
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(BASE, "..", "index.html")

lines = open(APP, encoding="utf-8").read().split("\n")
i = next(k for k, l in enumerate(lines) if l.startswith("const ANNALES_BIB"))
s = lines[i].strip()
a = s.index("[")
b = s.rindex("]")
annales = json.loads(s[a:b + 1])
n = 0
for an in annales:
    if "bts-bio" in an.get("filieres", []) and an.get("type") == "genere" and not an.get("source"):
        an["source"] = ("Sujet type construit à partir du référentiel BTS BIOALC 2024/2025 "
                        "(arrêté du 12 mars 2024 modifié le 24 juin 2025, RNCP38884) — à vérifier.")
        n += 1
lines[i] = "const ANNALES_BIB=" + json.dumps(annales, ensure_ascii=False, separators=(",", ":")) + ";"
open(APP, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print("A-04 : %d annales bts-bio ont reçu une source" % n)

p = os.path.join(BASE, "gen_cg_pc_B.py")
t = open(p, encoding="utf-8").read()
t2 = t.replace('["BTS2"]', '["BTS1","BTS2"]')
t2 = re.sub(r'"Contrôle PC · (\d+) · ', '"Contrôle PC · ', t2)
open(p, "w", encoding="utf-8", newline="\n").write(t2)
print("A-02/A-06 : gen_cg_pc_B.py mis à jour")
