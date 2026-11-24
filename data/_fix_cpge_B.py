# -*- coding: utf-8 -*-
p = "data/gen_cpge_B.py"
s = open(p, encoding="utf-8").read()
R = [
 ("Deux paires donent une géométrie", "Deux paires donnent une géométrie"),
 ("température accrule la constante", "température accroît la constante"),
 ("groupes fonctionnels princiapux", "groupes fonctionnels principaux"),
 ("veut faire le inventaire complet", "veut faire l'inventaire complet"),
 ("où n est la nombre de protons", "où n est le nombre de protons"),
 ("recouvrement latéral de orbitales p", "recouvrement latéral d'orbitales p"),
 ("rejette这些 certitudes", "rejette ces certitudes"),
 ("une intrigue causal et un narrateur", "une intrigue causale et un narrateur"),
 ("axes rather que de commenter", "axes plutôt que de commenter"),
 ("une paraphase", "une paraphrase"),
 ('["Fait de langue relevé", « jamais » répété", "Ne suffit pas"]',
  '["Fait de langue relevé", "« jamais » répété", "Ne suffit pas"]'),
 ("mouvements et评论eachun dans sa progression", "mouvements et commente chacun dans sa progression"),
 ("méthodologique :comment connaître", "méthodologique : comment connaître"),
 ("Le cogito carthésien", "Le cogito cartésien"),
 ("compliquent le débat : sociology, psychologie", "compliquent le débat : sociologie, psychologie"),
 ('["Un mensaje aux autres"', '["Un mensonge aux autres"'),
 ('"Assentiment et-refus"', '"Assentiment et refus"'),
 ("Les sceptiques ancient, Pyrrhon", "Les sceptiques anciens, Pyrrhon"),
 ("La_location du pouvoir et la séparation des pouvoirs, théorisée par Montesquieu, visent",
  "La limitation du pouvoir et la séparation des pouvoirs, théorisées par Montesquieu, visent"),
 ("au laquelle il répond", "à laquelle il répond"),
 ('          "Leur poésie de la Résistance mêle engagement politique et expression de l\'identité.",\n          ""),',
  '          "Leur poésie de la Résistance mêle engagement politique et expression de l\'identité."),'),
]
for a, b in R:
    if a not in s:
        print("MANQUANT:", a[:60])
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)
print("fixes appliqués")
