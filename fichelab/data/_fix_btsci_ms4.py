# -*- coding: utf-8 -*-
p = r"C:\Users\samir\Desktop\ilane bis\fichelabs\fichelab\data\gen_btsci_C.py"
s = open(p, encoding="utf-8").read()
old = 'add("MS4", "Séries temporelles et prévisions de ventes"'
new = 'add("MS4", "Séries temporelles et prévisions commerciales (BTS CI)"'
assert old in s
open(p, "w", encoding="utf-8", newline="\n").write(s.replace(old, new))
print("titre BTS CI renomme")
