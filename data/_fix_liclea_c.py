# -*- coding: utf-8 -*-
import re

p = "data/gen_liclea_C.py"
s = open(p, encoding="utf-8").read()
for i, line in enumerate(s.splitlines(), 1):
    if re.search(r"[\u4e00-\u9fff\u3040-\u30ff]", line):
        print(i, line)
s = s.replace("设计ee", "designee")
s = s.replace("当 l'increment", "quand l'increment")
s = s.replace("After avoir", "Apres avoir")
s = s.replace("mutually exclusives", "mutuellement exclusives")
s = s.replace("GENERALISATION", "Generalisation")
open(p, "w", encoding="utf-8").write(s)
print("CORRIGE")
