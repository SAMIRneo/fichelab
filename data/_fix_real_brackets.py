# -*- coding: utf-8 -*-
import os
BASE = os.path.dirname(os.path.abspath(__file__))
for name in ["gen_infirmier_B.py", "gen_infirmier_C.py"]:
    p = os.path.join(BASE, name)
    if not os.path.exists(p):
        continue
    lines = open(p, encoding="utf-8").read().split("\n")
    for _ in range(40):
        src = "\n".join(lines)
        try:
            compile(src, name, "exec")
            break
        except SyntaxError as e:
            n = e.lineno
            if not n or n > len(lines):
                print(name, "unexpected", e)
                break
            s = lines[n - 1]
            k = s.rfind('"],')
            if k < 0:
                print(name, "no closing at", n, repr(s))
                break
            lines[n - 1] = s[:k] + '",' + s[k+3:]
            print(name, "fixed genuine error line", n)
    else:
        print(name, "loop exhausted")
    open(p, "w", encoding="utf-8").write("\n".join(lines))
