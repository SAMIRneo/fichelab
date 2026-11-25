# -*- coding: utf-8 -*-
import io
p = "gen_pro-maintenance_A.py"
s = io.open(p, encoding="utf-8").read()
rep = [
 ("une反对 previsible", "une objection previsible"),
 ("A anticiper une反对 et a la refuter", "A anticiper une objection et a la refuter"),
 ("Pythagore et trigonometric转化 les mesures", "Pythagore et la trigonometrie transforment les mesures"),
 ("|否定 sentences use did not", "|Negative sentences use did not"),
 ("|La maitrise du vocabulaire technique fait partie des competences professionnelles attendues.", ""),
 ("passant par l'origine.\"\n  \"Un pourcentage", "passant par l'origine.|\"\n  \"Un pourcentage"),
 ("|Une serie doit etre accompagnee de son unite et de la periode de relevé.", ""),
 ("|La resistance R s'exprime en ohms et depend du materiau et de la temperature.", ""),
 ("|Un calculateur de couple doit tenir compte des pertes pour choisir un moteur.", ""),
 ("|Les electrolytes accelerent la corrosion en facilitant la circulation des ions.", ""),
 ("|Les lois sociales du debut du XXe siecle limitent la duree du travail et encadrent le travail des enfants.", ""),
 ("|La Seconde Guerre mondiale est suivie d'une periode de reconstruction et de croissance.", ""),
 ("|Un technicien peut etre appele a intervenir sur plusieurs sites d'un meme groupe.", ""),
 ("|Reading a datasheet requires recognizing units and abbreviations.", ""),
 ("overheating, breakdown and shutdown.\",\n   \"|Keep reports factual", "overheating, breakdown and shutdown.\"\n   \"|Keep reports factual"),
 ("|Always include measurements and units in an English incident report.\"),", "|Always include measurements and units in an English incident report.\")"),
 ("Quel favicon de style est conseille ?", "Quel style de phrase est conseille ?"),
 ("Laphrase d'origine", "La phrase d'origine"),
 ("Quel register correspond a une consigne de securite ecrite ?", "Quel registre correspond a une consigne de securite ecrite ?"),
 ("Une pompe ne peut pas reclamer", "Une pompe ne peut pas reclamer"),
 ("la courroie est le coeur", "la courroie est le coeur"),
 ("Les deux transfert une image", "Les deux transferent une image"),
 ("energie utile", "energie utile"),
 ("enerie consommee", "energie consommee"),
 ("Energie~Puissance multipliee par le temps", "Energie~Puissance multipliee par le temps"),
 ("|Les grandeurs physiques doivent etre exprimees", "|Les grandeurs physiques doivent etre exprimees"),
]
for a, b in rep:
    if a not in s:
        print("MANQUANT:", a[:60])
    s = s.replace(a, b, 1)
io.open(p, "w", encoding="utf-8").write(s)
print("OK fix A")
