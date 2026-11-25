# -*- coding: utf-8 -*-
import io
p = "gen_pro-maintenance_B.py"
lines = io.open(p, encoding="utf-8").readlines()
targets = ["revue après toute modification", "capitalisation passe par",
           "détente d'un gaz", "classes d'efficacité IE2"]
out = []
for line in lines:
    if any(t in line for t in targets) and line.rstrip().endswith('"),'):
        out[-1] = out[-1].rstrip("\n") + "),\n"
        continue
    out.append(line)
io.open(p, "w", encoding="utf-8").writelines(out)
print("OK fix B2")
