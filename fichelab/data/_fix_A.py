p = "gen_btstourisme_A.py"
s = open(p, encoding="utf-8").read()
repl = [
    ("montrer un\u652f\u6301 visuel", "montrer un support visuel"),
    ("SituationS potentiellement", "situations potentiellement"),
    ("échéances fixed", "échéances fixées"),
    ("ton reste calme et Neutre", "ton reste calme et neutre"),
    ("un bilan measure la fréquentation", "un bilan mesure la fréquentation"),
    ("Mesurer les résultats etcapitaliser", "Mesurer les résultats et capitaliser"),
    ("Improvider le déroulé", "Improviser le déroulé"),
    ("Programmer etpublier au bon moment", "Programmer et publier au bon moment"),
    ("souhaite une.option", "souhaite une option"),
    ("enchaînement des Arguments", "enchaînement des arguments"),
    ("Le rôle duanimateur", "Le rôle de l'animateur"),
    ("Attitude corporelleted du locuteur", "Attitude corporelle du locuteur"),
    ("sont conclats pour", "sont conclus pour"),
    ("Les créneaux de pointe", "Les créneaux de pointe"),
]
for a, b in repl:
    if a not in s:
        print("ABSENT:", a)
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)
print("OK")
