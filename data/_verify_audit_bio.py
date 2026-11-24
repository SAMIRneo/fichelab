# -*- coding: utf-8 -*-
import json
import os

APP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "index.html")
src = open(APP, encoding="utf-8").read()
lines = src.split("\n")

print("A-07 regex svgSur corrigee:", "[^\\2]" not in src)

def embedded(name):
    s = next(x for x in lines if x.startswith("const " + name)).strip()
    return json.loads(s[s.index("[") : s.rindex("]") + 1])

extra = embedded("EXTRA_FICHES")
ann = embedded("ANNALES_BIB")
cg = [f for f in extra if f["titre"].startswith("Contrôle PC ·")]
print("A-02 fiches CG:", len(cg), "| visibles BTS1:",
      sum(1 for f in cg if "BTS1" in f["annees"]), "| BTS2:",
      sum(1 for f in cg if "BTS2" in f["annees"]))
print("A-06 titres a double numero:",
      [f["titre"] for f in cg if "·" in f["titre"].replace("Contrôle PC · ", "")][:3])
bio = [a for a in ann if "bts-bio" in a.get("filieres", [])]
print("A-04 annales bio:", len(bio), "| sans source:",
      sum(1 for a in bio if not a.get("source")))

# A-01 : fiches bts-bio non prototype dans MODELES (avant FICHE_UV / EXTRA_FICHES)
mod_start = src.index("const MODELES=")
mod_end = src.index("const MODELES2")
chunk = src[mod_start:mod_end]
print("A-01 'bts-bio' restant dans MODELES:", chunk.count("'bts-bio'"))
