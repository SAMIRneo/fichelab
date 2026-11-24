# -*- coding: utf-8 -*-
import re

p = r"C:\Users\samir\Desktop\ilane bis\fichelabs\fichelab\data\gen_liceco_C.py"
s = open(p, encoding="utf-8").read()
s2, n = re.subn(r'"PSY(\d)\. · ', lambda m: '"ECOPSY%s. · ' % m.group(1), s)
print("remplacements:", n)
open(p, "w", encoding="utf-8", newline="\n").write(s2)
