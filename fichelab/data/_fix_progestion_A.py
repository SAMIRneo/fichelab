# -*- coding: utf-8 -*-
from pathlib import Path
p = Path("gen_pro-gestion_A.py")
s = p.read_text(encoding="utf-8")
repl = {
 "dans un même groupe, creating une tension expressive": "dans un même groupe, créant une tension expressive",
 "une反对 possible": "une objection possible",
 ",尤其是 dans les secteurs": ", surtout dans les secteurs",
 "~文献~Ruralite": "~References~Ruralite",
 "vait π × rayon²": "vaut π × rayon²",
 "égalité de treatment": "égalité de traitement",
}
for a, b in repl.items():
    if a not in s:
        print("INTROUVABLE:", a)
    s = s.replace(a, b)
p.write_text(s, encoding="utf-8")
print("corrections appliquees")
