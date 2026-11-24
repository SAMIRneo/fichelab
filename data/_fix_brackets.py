# -*- coding: utf-8 -*-
import os, re
BASE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(BASE, "gen_infirmier_B.py")
lines = open(p, encoding="utf-8").read().split("\n")
changed = 0
for i, line in enumerate(lines[:-1]):
    s = line.strip()
    if s.startswith('"') and s.endswith('"],'):
        nxt = ""
        for j in range(i + 1, len(lines)):
            if lines[j].strip():
                nxt = lines[j].strip()
                break
        if nxt.startswith("["):
            lines[i] = line[:line.rfind('"],')] + '",'
            changed += 1
            print("fix line", i + 1)
open(p, "w", encoding="utf-8").write("\n".join(lines))
print("total", changed)
