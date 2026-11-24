# -*- coding: utf-8 -*-
import os
import subprocess

PUBLISH = r"C:\Users\samir\AppData\Local\Temp\opencode\fichelab-publish"
APP = r"C:\Users\samir\Desktop\ilane bis\fichelabs\fichelab\index.html"

r = subprocess.run(["git", "-C", PUBLISH, "show", "ec59f52:index.html"],
                   capture_output=True)
old = r.stdout.decode("utf-8")
a = old.index("const MODELES2")
b = old.index("const FICHE_UV")
block = old[a:b]
print("bloc MODELES2 restaure:", len(block), "octets")

cur = open(APP, encoding="utf-8").read()
insert_at = cur.index("const FICHE_UV")
cur = cur[:insert_at] + block + "\n" + cur[insert_at:]
open(APP, "w", encoding="utf-8", newline="\n").write(cur)
print("OK")
