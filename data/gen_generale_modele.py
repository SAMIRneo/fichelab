# -*- coding: utf-8 -*-
"""FICHE-MODELE — une seule fiche, reference stricte pour toutes les filieres.

Copier exactement cette structure dans les scripts gen_<filiere>_*.py.
Sources : programme de mathematiques de classe de seconde, BO special n°1 du
22 janvier 2019 (arrette du 17-07-2018), eduscol.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import fiche, qcm, qt, diag, svg_grille, svg_flux, svg_etapes, svg_compare, bloc, valider_et_ecrire

REF = ("Programme de mathématiques de classe de seconde, BO spécial n° 1 du 22 janvier 2019 "
       "(arrêté du 17 juillet 2018) · éduscol, ressources_maths")
FIL = ["generale"]
AN = ["2nde"]
MAT = "Maths"

F = []

F.append(fiche(
    FIL, AN, MAT,
    "Chapitre M1 · Fonctions affines : variations et représentation graphique",
    REF + " · notions : fonction, ensemble de définition, pente, ordonnée à l'origine",
    [
        "Une fonction affine est une fonction de la forme f(x) = a·x + b, où a et b sont deux réels constants : a est le coefficient directeur (ou pente) et b l'ordonnée à l'origine. Si b = 0, on obtient une fonction linéaire f(x) = a·x.",
        "L'ensemble de définition d'une fonction affine est toujours ℝ : on peut calculer f(x) pour tout réel x. Son ensemble d'arrivée est également ℝ, sauf restriction explicite énoncée dans l'énoncé.",
        "Le tableau de variations d'une fonction affine se lit directement sur le signe de a. Si a > 0, la fonction est strictement croissante sur ℝ : quand x augmente, f(x) augmente. Si a < 0, elle est strictement décroissante. Si a = 0, la fonction est constante égale à b.",
        "La représentation graphique d'une fonction affine est une droite. Pour la tracer, deux points suffisent : le plus souvent on choisit l'intersection avec l'axe des ordonnées, le point de coordonnées (0 ; b), et un second point obtenu pour x = 1, de coordonnées (1 ; a + b).",
        "Le coefficient directeur se calcule à partir de deux quelconques points A(x_A ; y_A) et B(x_B ; y_B) de la droite par la formule a = (y_B − y_A) / (x_B − x_A). Le résultat ne dépend pas du couple de points choisi : c'est une propriété caractéristique de la droite.",
        "Le nombre a mesure la pente : a = Δy / Δx. Si a = 2, une augmentation de 1 unité de x provoque une augmentation de 2 unités de y ; si a = −1/2, y diminue d'une demi-unité quand x augmente d'une unité. Une droite verticale n'est pas une fonction affine : son coefficient directeur n'existe pas.",
        "Deux droites d'équations y = a·x + b et y = a'·x + b' sont parallèles si et seulement si a = a' (même pente, positions différentes). Elles sont confondues si a = a' et b = b'. Elles sont perpendiculaires si a·a' = −1 (à condition qu'a et a' soient non nuls).",
        "Pour résoudre une équation du type f(x) = c, on isole x : a·x + b = c donne x = (c − b)/a si a ≠ 0. Graphiquement, chercher les solutions revient à chercher les abscisses des points d'intersection de la droite y = f(x) avec la droite horizontale y = c.",
        "Résoudre une inéquation f(x) > c revient, lorsque a > 0, à garder les x situés à droite de la solution de f(x) = c ; lorsque a < 0, à garder les x situés à gauche. On peut toujours se reporter au graphique pour vérifier le sens de l'inégalité.",
        "Deux fonctions affines f(x) = a·x + b et g(x) = a'·x + b' ont le même point de concours si le système f(x) = g(x) admet une solution ; celle-ci vérifie (a − a')x = b' − b, soit x = (b' − b)/(a − a') lorsque a ≠ a'. Si a = a' et b ≠ b', les droites sont parallèles distinctes : aucune solution.",
        "Dans une situation de proportionnalité, la fonction qui associe la quantité à son prix est linéaire : f(x) = a·x, avec a le coefficient de proportionnalité (prix unitaire). Le graphique passe alors toujours par l'origine du repère.",
        "Dans une situation avec un coût fixe (abonnement, frais de dossier), la fonction est affine non linéaire : f(x) = a·x + b où b est le coût fixe et a le coût variable par unité. Interpréter a et b dans le contexte est une compétence attendue au baccalauréat.",
    ],
    [
        qcm("Quelle est la représentation graphique d'une fonction affine ?",
            ["Une parabole", "Une droite", "Une hyperbole", "Un cercle"], 1,
            "Toute fonction f(x) = ax + b a pour représentation graphique une droite : c'est la définition même d'une fonction affine."),
        qcm("Si f(x) = −3x + 2, que peut-on dire de ses variations ?",
            ["Elle est croissante", "Elle est décroissante", "Elle est constante", "Elle n'a pas de variations"], 1,
            "Le coefficient directeur a = −3 est négatif : la fonction est strictement décroissante sur ℝ."),
        qcm("Quel est le coefficient directeur de la droite passant par A(1 ; 3) et B(3 ; 7) ?",
            ["1", "2", "4", "5"], 1,
            "a = (7 − 3)/(3 − 1) = 4/2 = 2. Le résultat est le même dans l'autre sens : (3 − 7)/(1 − 3) = 2."),
        qcm("Une droite passe par (0 ; 5) et a pour pente −2. Quelle est son équation ?",
            ["y = 5x − 2", "y = −2x + 5", "y = 2x + 5", "y = −2x − 5"], 1,
            "L'ordonnée à l'origine vaut b = 5 car la droite coupe l'axe des y en (0 ; 5) ; la pente est a = −2."),
        qcm("Deux droites sont parallèles. Que peut-on affirmer ?",
            ["Elles ont la même ordonnée à l'origine", "Elles ont le même coefficient directeur", "Elles sont perpendiculaires", "Elles se coupent en un point"], 1,
            "Le parallélisme se lit sur la pente : a = a'. Si en plus b = b', les droites seraient confondues."),
        qcm("Quelle fonction représente un prix avec 10 € de frais fixes et 2 € l'unité ?",
            ["f(x) = 10x + 2", "f(x) = 2x + 10", "f(x) = 12x", "f(x) = 2x − 10"], 1,
            "Le coût fixe est l'ordonnée à l'origine b = 10 et le coût variable par unité est la pente a = 2."),
        qcm("On résout 3x − 1 = 8. Quelle est la solution ?",
            ["x = 2", "x = 3", "x = 7/3", "x = 9"], 1,
            "3x = 9 donc x = 3. Graphiquement, c'est l'abscisse du point où la droite y = 3x − 1 coupe la droite y = 8."),
        qt("Expliquer pourquoi une droite verticale n'est pas la représentation d'une fonction affine, puis donner le coefficient directeur d'une droite perpendiculaire à y = 2x + 1.",
           "Une droite verticale associe à une même abscisse plusieurs ordonnées : elle ne satisfait pas la définition d'une fonction. Une droite perpendiculaire à y = 2x + 1 a pour coefficient directeur a' tel que 2·a' = −1, donc a' = −1/2.",
           "On vérifie la définition de fonction (unicité de l'image) et on applique la condition de perpendicularité a·a' = −1."),
        qt("Un abonnement coûte 25 € par mois plus 0,20 € par message. Écrire la fonction donnant le coût mensuel selon le nombre x de messages, puis calculer le coût pour 120 messages.",
           "f(x) = 0,20·x + 25. Pour x = 120 : f(120) = 0,20 × 120 + 25 = 24 + 25 = 49 €.",
           "Identifier le coût fixe (ordonnée à l'origine) et le coût variable (pente), puis remplacer x par 120."),
    ],
    [
        bloc("L'idée en une phrase", texte="Une fonction affine, c'est une droite : sa pente dit si elle monte ou descend, et son ordonnée à l'origine dit où elle coupe l'axe vertical."),
        bloc("La formule à connaître", eq="f(x) = a·x + b", leg="a : coefficient directeur (pente) · b : ordonnée à l'origine · définition : tout ℝ"),
        bloc("Tableau des trois grandeurs", items=[
            ["a", "Pente : variation de y pour +1 sur x", "a > 0 croissante, a < 0 décroissante"],
            ["b", "Ordonnée à l'origine", "f(0) = b, point (0 ; b)"],
            ["Δ", "Écart entre deux points", "a = Δy / Δx"]]),
        bloc("À retenir sur la droite", items=[
            "Deux points suffisent pour tracer une droite : (0 ; b) et (1 ; a + b)",
            "Parallèles ↔ même a · perpendiculaires ↔ a·a' = −1",
            "a = 0 donne une fonction constante, pas une droite oblique",
            "b = 0 donne une fonction linéaire : la droite passe par l'origine"]),
        bloc("Tracer et résoudre, étape par étape", items=[
            "Repérer a et b dans l'équation",
            "Placer le point (0 ; b) sur l'axe des ordonnées",
            "Placer un second point, par exemple (1 ; a + b)",
            "Tracer la droite à la règle et vérifier le sens des variations",
            "Pour f(x) = c, lire l'abscisse du point d'intersection avec y = c"]),
        bloc("Pièges fréquents", items=[
            "Confondre a et b : a est la pente, b est la valeur initiale",
            "Oublier que a < 0 inverse le sens d'une inéquation",
            "Croire qu'une droite verticale est une fonction",
            "Diviser par zéro en cherchant a avec deux points de même abscisse",
            "Oublier l'unité dans une interprétation de coût"]),
        bloc("En chiffres (à savoir refaire)", items=[
            "<span class=\"cle\">f(x) = −3x + 2</span> → décroissante, passe par (0 ; 2)",
            "<span class=\"cle\">A(1 ; 3), B(3 ; 7)</span> → a = 4/2 = 2",
            "<span class=\"cle\">3x − 1 = 8</span> → x = 3",
            "<span class=\"cle\">2 €/unité + 25 € fixes</span> → f(x) = 2x + 25, f(120) = 265 €",
            "<span class=\"cle\">a·a' = −1</span> → perpendiculaire à pente 2 : a' = −0,5"]),
    ],
    [
        diag("1 · Anatomie de la droite", svg_grille("Lire une équation y = ax + b",
             ["Élément", "Rôle", "Lecture graphique"],
             [["a", "Pente, variations", "Monte si a > 0"],
              ["b", "Valeur initiale", "Point (0 ; b)"],
              ["f(x)", "Image de x", "Ordonnée du point d'abscisse x"]])),
        diag("2 · Construire la droite", svg_etapes("Tracer y = ax + b",
             ["Repérer a et b dans l'équation", "Placer (0 ; b) sur l'axe des y",
              "Placer (1 ; a + b) comme second point", "Tracer la droite à la règle",
              "Vérifier le sens des variations"])),
        diag("3 · Variations selon a", svg_compare("pente positive / négative",
             ("a > 0", ["Droite montante", "f croissante sur ℝ", "x augmente → y augmente"]),
             ("a < 0", ["Droite descendante", "f décroissante sur ℝ", "x augmente → y diminue"]))),
    ],
))

valider_et_ecrire(F, "generale-mat-part-MODELE.json")
