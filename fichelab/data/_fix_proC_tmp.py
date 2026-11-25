# -*- coding: utf-8 -*-
import io
p = "gen_pro-maintenance_C.py"
s = io.open(p, encoding="utf-8").read()
rep = [
 ("de la qualité要求", "de la qualité requise"),
 ("Sans这些方法 homogènes", "Sans méthodes homogènes"),
 ("Sans理由", "Sans raison"),
 ("计划ifier la formation", "planifier la formation"),
 ("prix de revient enablede déterminer", "prix de revient permet de déterminer"),
 ("ne doit pas sacrificed la sécurité", "ne doit pas sacrifier la sécurité"),
 ("des Prochains mois", "des prochains mois"),
 ("R-etention~Stockage securise", "Retention~Stockage securise"),
 ("dont son détenteur se défait", "dont le détenteur se défait"),
 ("une pièce relatively rigide", "une pièce relativement rigide"),
 ("Engagement~Engagement voluntarie", "Engagement~Engagement volontaire"),
 ("La FDS compporte seize rubriques", "La FDS comporte seize rubriques"),
 ("  \"|Les assemblages permanents comprennent le soudage, le rivetage et le collage structurel.\"\n", ""),
 ("  \"|La présentation graphique facilite la lecture des évolutions.\"\n", ""),
 ("  \"|Use a formal greeting such as Dear Sir or Madam when the recipient is unknown.\"\n", ""),
]
for a, b in rep:
    if a not in s:
        print("MANQUANT:", a[:70])
    s = s.replace(a, b, 1)
io.open(p, "w", encoding="utf-8").write(s)
print("OK fix C")
