# -*- coding: utf-8 -*-
import io
p = "gen_pro-maintenance_B.py"
s = io.open(p, encoding="utf-8").read()
rep = [
 ("contrôle de tension。", "contrôle de tension."),
 ("la seule振幅 globale", "la seule amplitude globale"),
 ("Le rotor est一般ement de type", "Le rotor est généralement de type"),
 ("Prévention降低 occurrence", "Prévention : réduire l'occurrence"),
 ("  \"|La température est un indicateur complémentaire simple, mesuré au contact ou par infrarouge.\"\n", ""),
 ("  \"|La bobine d'un contacteur est représentée par un rectangle ou un cercle selon la norme.\"\n", ""),
 ("  \"|Les condensateurs doivent être déchargés avant toute mesure de résistance.\"\n", ""),
 ("  \"|Les travaux sous tension sont exceptionnels et strictement encadrés.\"\n", ""),
 ("  \"|Une comparaison n'est valable que si les méthodes de calcul sont identiques.\"\n", ""),
 ("  \"|La FMEA doit être revue après toute modification ou retour d'expérience significatif.\"\n", ""),
 ("  \"|La capitalisation passe par des documents mis à jour et accessibles à tous.\"\n", ""),
 ("  \"|La détente d'un gaz Produit du travail dans un moteur ou une turbine.\"\n", ""),
 ("  \"|Les classes d'efficacité IE2, IE3 ou IE4 normalisent le rendement des moteurs.\"\n", ""),
 ("  \"MTBF = temps de marche / nombre de pannes\",\n  \"MTTR = durée des réparations / nombre d'interventions\",\n  \"Disponibilité = MTBF / (MTBF + MTTR)\",",
  "  \"MTBF = temps de marche / nombre de pannes · MTTR = durée des réparations / nombre d'interventions\",\n  \"Disponibilité = MTBF / (MTBF + MTTR)\","),
 ("     \"AC/DC puis DC/AC avec un circuit intermédiaire continua le plus souvent.\",\n  ),",
  "     \"AC/DC puis DC/AC avec un circuit intermédiaire continu, le plus souvent.\"),"),
]
for a, b in rep:
    if a not in s:
        print("MANQUANT:", a[:70])
    s = s.replace(a, b, 1)
io.open(p, "w", encoding="utf-8").write(s)
print("OK fix B")
