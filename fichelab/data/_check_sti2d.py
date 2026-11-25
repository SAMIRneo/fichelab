# -*- coding: utf-8 -*-
"""Diagnostic rapide des generateurs STI2D : compteurs par fiche."""
import ast
import sys

for path in sys.argv[1:]:
    src = open(path, encoding="utf-8").read()
    tree = ast.parse(src)
    print("=== %s ===" % path)
    n_ok = 0
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == "add" and len(node.args) >= 7):
            continue
        prefix = ast.literal_eval(node.args[0])
        pts = node.args[4]
        np = 0
        if isinstance(pts, ast.Call) and getattr(pts.func, "id", "") == "S":
            np = len([x for x in ast.literal_eval(pts.args[0]).split("|") if x.strip()])
        qs = node.args[5]
        nq = len(qs.elts) if isinstance(qs, ast.List) else -1
        nqc = sum(1 for q in getattr(qs, "elts", [])
                  if getattr(getattr(q, "func", None), "id", "") == "QC")
        nqt = sum(1 for q in getattr(qs, "elts", [])
                  if getattr(getattr(q, "func", None), "id", "") == "QT")
        c = node.args[6]
        nc = len(c.args) if isinstance(c, ast.Call) else -1
        flag = "" if (np == 12 and nq == 9 and nqc == 7 and nqt == 2 and nc == 9) else "  <<<"
        print("%-5s points=%2d questions=%2d (QC=%d QT=%d) C=%d%s"
              % (prefix, np, nq, nqc, nqt, nc, flag))
        if not flag:
            n_ok += 1
    print("OK stands: %d" % n_ok)
