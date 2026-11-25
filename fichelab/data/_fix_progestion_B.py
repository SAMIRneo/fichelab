# -*- coding: utf-8 -*-
from pathlib import Path
p = Path("gen_pro-gestion_B.py")
s = p.read_text(encoding="utf-8")
repl = {
 "les indicateurs de efficacité": "les indicateurs d'efficacité",
 "|budgeter et diffuser|": "|Budgéter et diffuser|",
 "ressources durables etactif immobilisé": "ressources durables et actif immobilisé",
 "|Precisionner le compte|": "|Préciser le compte|",
}
for a, b in repl.items():
    if a not in s:
        print("INTROUVABLE:", a)
    s = s.replace(a, b)
p.write_text(s, encoding="utf-8")
print("corrections appliquees")
