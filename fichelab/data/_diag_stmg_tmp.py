# -*- coding: utf-8 -*-
import io
p = r"C:\Users\samir\Desktop\ilane bis\fichelabs\fichelab\data\gen_stmg_A.py"
src = io.open(p, encoding="utf-8").read()
i = src.index('add("A07"')
j = src.index("[QC(", i)
block = src[i:j]
print("pipes:", block.count("|"))
for n, part in enumerate(block.split("|"), 1):
    print(n, part.strip()[:90])
