# -*- coding: utf-8 -*-
"""Remplace les artefacts CJK résiduels dans les générateurs par du texte français."""
import glob
import os
import re

D = os.path.dirname(os.path.abspath(__file__))
CJK = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff]+")
REPL = {
    "那些": "les", "一般": "généralement", "于心": "à l'esprit",
    "于": "à", "一": "un", "般": "général", "那": "ce", "些": "ces",
}
for name in ("gen_butgb_B.py", "gen_butgmp_A.py", "gen_butgeii_A.py",
             "gen_btstourisme_A.py", "gen_btscommunication_A.py", "gen_btspi_A.py"):
    p = os.path.join(D, name)
    if not os.path.exists(p):
        continue
    s = open(p, encoding="utf-8").read()
    found = set(CJK.findall(s))
    for tok in found:
        s = s.replace(tok, REPL.get(tok, " "))
    if found:
        open(p, "w", encoding="utf-8", newline="\n").write(s)
    print(name, "CJK remplacés:", found or "aucun")
