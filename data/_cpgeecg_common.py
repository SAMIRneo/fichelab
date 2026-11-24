# -*- coding: utf-8 -*-
"""Mecanique partagee par les trois lots de la filiere CPGE ECG (FicheLab).

Le contenu pedagogique reste dans les scripts gen_cpgeecg_A/B/C.py ; ce module
ne fait qu'assembler les fiches avec les outils de fixtures.py, exactement comme
gen_generale_modele.py.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_flux,
                      svg_etapes, svg_compare, bloc, valider_et_ecrire)

REF = (
    "Programmes de la classe préparatoire économique et commerciale générale (ECG), "
    "arrêté du 19 juillet 2019 (NOR MENE1922062A), BO spécial n° 1 du 11 février 2021 "
    "(tronc commun et options ESH / HGG), BO spécial n° 5 du 25 juillet 2019 "
    "(mathématiques de CPGE), BO spécial n° 8 du 25 juillet 2019 "
    "(français, philosophie, langues vivantes) · éduscol, Onisep, SIES"
)


def blocs7(intro, formule, leg, grille, liste, etapes, pieges, exemples):
    """Les 7 blocs, dans l'ordre strict exige par le prototype."""
    return [
        bloc("L'idee en une phrase", texte=intro),
        bloc("La formule a connaitre", eq=formule, leg=leg),
        bloc("Tableau de lecture", items=grille),
        bloc("A retenir", items=liste),
        bloc("Methode pas a pas", items=etapes),
        bloc("Pieges frequents", items=pieges),
        bloc("Exemples et chiffres", items=exemples),
    ]


def dg(titre, colonnes, lignes):
    return diag(titre, svg_grille(titre, colonnes, lignes))


def de(titre, etapes):
    return diag(titre, svg_etapes(titre, etapes))


def dc(titre, gauche, droite):
    return diag(titre, svg_compare(titre, gauche, droite))


def df(titre, etapes):
    etapes = [e if isinstance(e, (tuple, list)) else (e, "") for e in etapes]
    return diag(titre, svg_flux(titre, etapes))


def make(filieres, annees, matiere, titre, source, points, questions, blocs, schemas):
    return fiche(filieres, annees, matiere, titre, source, points,
                 questions, blocs, schemas)
