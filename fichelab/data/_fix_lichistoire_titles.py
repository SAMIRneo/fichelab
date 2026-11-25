# -*- coding: utf-8 -*-
import glob
import os
import re

D = os.path.dirname(os.path.abspath(__file__))
for p in sorted(glob.glob(os.path.join(D, "gen_lichistoire_*.py"))):
    s = open(p, encoding="utf-8").read()
    s2, n = re.subn(r'"(ST|PSY|PF|AN|IN|MS|MU|DR|EC|LHFR)(\d+\. · )',
                    lambda m: '"LH%s%s' % (m.group(1), m.group(2)), s)
    if n:
        open(p, "w", encoding="utf-8", newline="\n").write(s2)
    print(os.path.basename(p), n, "titres renommes")
