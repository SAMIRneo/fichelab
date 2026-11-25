# -*- coding: utf-8 -*-
"""Copie le bloc mecanique valide du lot A vers les lots B et C."""
import io
base = r"C:\Users\samir\Desktop\ilane bis\fichelabs\fichelab\data"
src = io.open(base + r"\gen_stmg_A.py", encoding="utf-8").read()
prefix = src[:src.index("# ============================================================ A01")]
for lot, desc in [("B", "sciences de gestion et economie"),
                  ("C", "numerique, mathematiques appliquees, anglais professionnel et complements")]:
    out = prefix.replace(
        "Generateur stmg-mat-part-A.json — lot A : tronc commun (20 fiches).",
        "Generateur stmg-mat-part-%s.json — lot %s : %s (20 fiches)." % (lot, lot, desc), 1)
    out += ("# FIN DU LOT %s\n" % lot)
    out += 'valider_et_ecrire(F, "stmg-mat-part-%s.json")\n' % lot
    io.open(base + r"\gen_stmg_%s.py" % lot, "w", encoding="utf-8").write(out)
    print("cree gen_stmg_%s.py" % lot)
