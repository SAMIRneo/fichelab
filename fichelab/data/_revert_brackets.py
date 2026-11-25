# -*- coding: utf-8 -*-
import os
BASE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(BASE, "gen_infirmier_B.py")
NUMS = [97,102,106,184,189,193,271,276,280,358,363,367,446,451,455,532,537,541,
619,624,628,711,716,720,799,804,808,887,892,896,975,980,984,1070,1074,1152,
1157,1161,1240,1245,1249,1327,1332,1336,1418,1423,1427,1502,1507,1511,1590,
1595,1599,1678,1683,1687,1765,1770,1774,1853,1858,1862,1946,1950]
lines = open(p, encoding="utf-8").read().split("\n")
for n in NUMS:
    i = n - 1
    s = lines[i]
    if s.rstrip().endswith('",'):
        idx = s.rfind('",')
        lines[i] = s[:idx] + '"],' + s[idx+2:]
open(p, "w", encoding="utf-8").write("\n".join(lines))
print("reverted", len(NUMS))
