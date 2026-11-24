# -*- coding: utf-8 -*-
import ast, os
BASE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(BASE, "gen_infirmier_B.py")
src = open(p, encoding="utf-8").read()
tree = ast.parse(src)
for node in ast.walk(tree):
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "blocs":
        if len(node.args) != 8:
            print("line", node.lineno, "args", len(node.args))
            for a in node.args:
                print("   ", type(a).__name__, getattr(a, "lineno", "?"))
