# -*- coding: utf-8 -*-
"""Nettoyage final de la forme des generateurs lic-lea."""
import re

REPL = {
    "interpretre": "interpreter",
    "derivater": "deriver",
    "scientistifiquement": "scientifiquement",
    "aux outliers": "aux valeurs extremes",
    "mutually exclusives": "mutuellement exclusives",
    "si necessary": "si necessaire",
    "la frequency de capitalisation": "la frequence de capitalisation",
    "si seulement": "seulement si",
}

for p in ["data/gen_liclea_A.py", "data/gen_liclea_B.py", "data/gen_liclea_C.py"]:
    s = open(p, encoding="utf-8").read()
    before = s
    for a, b in REPL.items():
        s = s.replace(a, b)
    if s != before:
        open(p, "w", encoding="utf-8").write(s)
        print("nettoye", p)
print("OK")
