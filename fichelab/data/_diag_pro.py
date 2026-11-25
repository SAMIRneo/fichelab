# -*- coding: utf-8 -*-
"""Diagnostic ponctuel des generateurs pro-sante (lecture AST, sans execution)."""
import ast
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
CJK = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff]")
FULLWIDTH = re.compile(r"[\uff00-\uffef]")

for name in sys.argv[1:]:
    path = os.path.join(BASE, name)
    src = open(path, encoding="utf-8").read()
    tree = ast.parse(src)
    print("=== %s ===" % name)
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        f = node.func
        if not (isinstance(f, ast.Name) and f.id == "add"):
            continue
        prefix = node.args[0].value
        # le premier argument apres le titre est l'appel a S(...)
        s_call = node.args[4]
        points = [x for x in s_call.args[0].value.split("|") if x.strip()]
        qc = node.args[5].elts
        qt = node.args[6].elts
        problems = []
        if len(points) != 12:
            problems.append("points=%d" % len(points))
        if len(qc) != 7:
            problems.append("qcm=%d" % len(qc))
        if len(qt) != 2:
            problems.append("texte=%d" % len(qt))
        for i, p in enumerate(points):
            if CJK.search(p) or FULLWIDTH.search(p):
                problems.append("point %d CJK/fullwidth" % i)
        for group, items in (("qc", qc), ("txt", qt)):
            for j, item in enumerate(items):
                txt = ast.get_source_segment(src, item) or ""
                if CJK.search(txt) or FULLWIDTH.search(txt):
                    problems.append("%s %d CJK/fullwidth" % (group, j))
        txt_all = " ".join(points)
        if CJK.search(src):
            pass
        print("%-5s %s" % (prefix, ", ".join(problems) if problems else "OK"))
