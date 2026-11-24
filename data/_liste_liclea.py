# -*- coding: utf-8 -*-
import json
import re

for lot in "ABC":
    with open("data/liclea-mat-part-%s.json" % lot, encoding="utf-8") as f:
        fs = json.load(f)["fiches"]
    print("=== LOT", lot, "===")
    for f in fs:
        m = re.match(r"^Chapitre ([A-Z0-9]+) \(LEA\) · (.+)$", f["titre"])
        print("%s | %s | %s | %s" % (m.group(1), f["matiere"], "/".join(f["annees"]), m.group(2)))
