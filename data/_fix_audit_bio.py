# -*- coding: utf-8 -*-
"""Corrections suite à l'audit BIOALC profond (A-01, A-02, A-04, A-06, A-07)."""
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(BASE, "..", "index.html")

# ---------- A-01 : retirer bts-bio des fiches texte brut du catalogue MODELES ----------
lines = open(APP, encoding="utf-8").read().split("\n")
out = []
i = 0
removed = 0
while i < len(lines):
    l = lines[i]
    # 3 fiches partagées : on retire seulement 'bts-bio' du tableau filiers
    if l.startswith("F(['lic-svt','pass','bts-bio'],'Biologie cellulaire'"):
        l = l.replace("['lic-svt','pass','bts-bio']", "['lic-svt','pass']")
    elif l.startswith("F(['pass','infirmier','bts-bio'],'Biochimie'"):
        l = l.replace("['pass','infirmier','bts-bio']", "['pass','infirmier']")
    elif l.startswith("F(['bts-bio','pass'],'Biochimie / analyses'"):
        l = l.replace("['bts-bio','pass']", "['pass']")
    # 3 fiches exclusivement bts-bio : on saute tout le bloc F(...) jusqu'à ']),'
    elif l.startswith("F(['bts-bio'],'Microbiologie','L’antibiogramme") or \
         l.startswith("F(['bts-bio'],'Hématologie','La numération") or \
         l.startswith("F(['bts-bio'],'Normes & réglementation','La norme ISO 17025"):
        while i < len(lines) and not lines[i].rstrip().endswith("]),"):
            i += 1
        i += 1
        removed += 1
        continue
    out.append(l)
    i += 1

src = "\n".join(out)

# ---------- A-07 : corriger la regex de svgSur (référence arrière dans classe de caractères) ----------
src = src.replace(r"[^\\2]*", r"[^'\"]*")

open(APP, "w", encoding="utf-8", newline="\n").write(src)
print("A-01 : %d fiches texte brut bts-bio supprimées de MODELES" % removed)

# ---------- A-04 : ajouter un source aux annales genere ----------
lines = src.split("\n")
i = next(k for k, l in enumerate(lines) if l.startswith("const ANNALES_BIB="))
s = lines[i].strip()
a = s.index("[")
b = s.rindex("]")
annales = json.loads(s[a:b + 1])
n = 0
for an in annales:
    if "bts-bio" in an.get("filieres", []) and an.get("type") == "genere" and not an.get("source"):
        an["source"] = ("Sujet type construit à partir du référentiel BTS BIOALC 2024/2025 "
                        "(arrêté du 12 mars 2024 modifié le 24 juin 2025, RNCP38884) — à vérifier.")
        n += 1
lines[i] = "const ANNALES_BIB=" + json.dumps(annales, ensure_ascii=False, separators=(",", ":")) + ";"
open(APP, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print("A-04 : %d annales bts-bio ont reçu une source" % n)

# ---------- A-02 + A-06 : fiches Contrôle PC 9-15 visibles en BTS1 et titres normalisés ----------
for name in ("gen_cg_pc_B.py",):
    p = os.path.join(BASE, name)
    s = open(p, encoding="utf-8").read()
    s2 = s.replace('["BTS2"]', '["BTS1","BTS2"]')
    s2 = re.sub(r'"Contrôle PC · (\d+) · ', '"Contrôle PC · ', s2)
    open(p, "w", encoding="utf-8", newline="\n").write(s2)
    print(name, ": annees BTS1+BTS2 et titres normalisés")
