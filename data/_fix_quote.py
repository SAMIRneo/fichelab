# -*- coding: utf-8 -*-
import os
BASE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(BASE, "gen_infirmier_B.py")
lines = open(p, encoding="utf-8").read().split("\n")
for n in (1062, 1237, 1675, 1942):
    i = n - 1
    s = lines[i]
    # remplace le '[' initial par '["'
    assert s.lstrip().startswith("[") and not s.lstrip().startswith('["'), (n, s)
    idx = s.index("[")
    lines[i] = s[:idx] + '["' + s[idx+1:]
    print("fixed quote", n)
open(p, "w", encoding="utf-8").write("\n".join(lines))
