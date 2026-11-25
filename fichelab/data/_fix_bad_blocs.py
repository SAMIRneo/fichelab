# -*- coding: utf-8 -*-
import os
BASE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(BASE, "gen_infirmier_B.py")
lines = open(p, encoding="utf-8").read().split("\n")
# (premiere ligne du groupe de chaines, derniere ligne du groupe)
GROUPS = [(1062, 1065), (1237, 1240), (1675, 1678), (1942, 1946)]
for start, end in GROUPS:
    i = start - 1
    j = end - 1
    s = lines[i]
    assert s.lstrip().startswith('"'), (start, s)
    lines[i] = s.replace('"', '[', 1)
    t = lines[j]
    k = t.rfind('",')
    assert k >= 0, (end, t)
    lines[j] = t[:k] + '"],' + t[k+3:]
    print("fixed group", start, end)
open(p, "w", encoding="utf-8").write("\n".join(lines))
