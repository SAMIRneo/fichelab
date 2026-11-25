# -*- coding: utf-8 -*-
import os
BASE = os.path.dirname(os.path.abspath(__file__))
FIX = {
 "c'est une Convention commune": "c'est une convention commune",
 "lePrincipal cation": "le principal cation",
 "en_termes de canaux": "en termes de canaux",
 "la(logique du contre-courant": "la logique du contre-courant",
 "la bruyère urétrale": "la brûlure urétrale",
 "oxydent complètement": "oxyde complètement",
 "douneurs musculaires": "douleurs musculaires",
 "转移 plasmids = conjugation": "Plasmide transféré = conjugaison",
 "antiblogramme": "antibiogramme",
 "Orinaire": "Ordinaire",
 "formed par": "formée par",
 "deconditions": "de conditions",
 "Les Acides Nucléiques": "Les acides nucléiques",
 "un_site": "un site",
 "modificaton": "modification",
 "Surveillanceée": "surveillée",
 "effetAppears": "effet apparaît",
 "médiation par": "médiée par",
 "L'histamineCause": "L'histamine cause",
 "Quel marqueur est Plus": "Quel marqueur est plus",
 "provoker": "provoquer",
 "la précautions adaptée": "la précaution adaptée",
 "en quelques heures à几天": "en quelques heures à quelques jours",
 "expliquer la alternance": "expliquer l'alternance",
 "la alternance": "l'alternance",
 "cytoto xiques": "cytotoxiques",
 "surveillanceée": "surveillée",
 "des cellules hôtess": "des cellules hôtes",
 "cellules hôtess": "cellules hôtes",
 "seizures": "convulsions",
 "Le roleprotecteur": "Le rôle protecteur",
 "Quel est le rôleprotecteur": "Quel est le rôle protecteur",
}
for name in ["gen_infirmier_A.py", "gen_infirmier_B.py", "gen_infirmier_C.py"]:
    p = os.path.join(BASE, name)
    if not os.path.exists(p):
        continue
    s = open(p, encoding="utf-8").read()
    for a, b in FIX.items():
        s = s.replace(a, b)
    open(p, "w", encoding="utf-8").write(s)
    print("fix", name)
