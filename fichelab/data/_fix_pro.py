# -*- coding: utf-8 -*-
"""Corrections ponctuelles de typo dans les generateurs pro-sante."""
import io
import os

BASE = os.path.dirname(os.path.abspath(__file__))
FIXES = {
    "gen_pro-sante_A.py": {
        "La presentence du cadre": "La présentation du cadre",
        "ou rapportre des informations": "ou reporter des informations",
        "LesDecoratorions": "Les décorations",
        "Lesannees 1980-1990": "Les années 1980-1990",
        "laHaute Autorite": "la Haute Autorité",
        "ontagi directement": "ont agi directement",
        "refleTe": "reflète",
        "desmodalites": "des modalités",
        "une diffrence": "une différence",
        "des obstacleS": "des obstacles",
        "La bienveillante ne remplace": "La bienveillance ne remplace",
        "qui suppressions toute initiative": "qui supprime toute initiative",
        "et les reasons dans": "et les raisons dans",
        "reqête": "requête",
        "ce choices linguistiques": "ces choix linguistiques",
        "le editeur du site": "l'éditeur du site",
    },
    "gen_pro-sante_B.py": {
        "de changes physiologiques": "de changements physiologiques",
        "ces changes avec une demence": "ces changements avec une démence",
        "compenser ces changes": "compenser ces changements",
        "on fracons l'effort": "on fractionne l'effort",
        "Ces two processus": "Ces deux processus",
        "comme intermediary": "comme intermédiaire",
        "Les gants de la驱 équipe": "Les gants de l'équipe",
        "la personne est受害者 ou plutôt victime": "la personne est victime",
        "ecritres medicalux": "écrits médicaux",
        "de la law": "de la loi",
        "j'alerte also le procureur": "j'alerte aussi le procureur",
        "Le materiaI adapte": "Le matériel adapté",
        "ouvers le toilette": "ou vers la toilette",
        "designer une personne de confiance": "désigner une personne de confiance",
    },
}

for name, mapping in FIXES.items():
    path = os.path.join(BASE, name)
    with io.open(path, encoding="utf-8") as fp:
        txt = fp.read()
    for old, new in mapping.items():
        if old in txt:
            txt = txt.replace(old, new)
    with io.open(path, "w", encoding="utf-8", newline="") as fp:
        fp.write(txt)
    print("corrigé", name)
