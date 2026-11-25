# -*- coding: utf-8 -*-
"""Generateur pro-maintenance-mat-part-B.json — lot B : maintenance et physique appliquee.

20 fiches 'prototype' pour la filiere pro-maintenance (2nde pro, 1re pro,
Terminale pro) : 12 points, 9 questions corrigees (7 QCM + 2 texte),
7 blocs en ordre strict, 3 schemas via diag().
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pro_maint_common import S, R, QC, QT, C, build, valider_et_ecrire

F = []


def add(prefix, titre, mat, points, questions, c):
    F.append(build(prefix, titre, mat, points, questions, c))


# ============================================================ ME1
add("ME1", "Maintenance préventive : principes et planification", "Maintenance mécanique",
S("La maintenance préventive vise à éviter la panne avant qu'elle ne se produise."
  "|Elle s'oppose à la maintenance corrective, qui intervient après la défaillance."
  "|La maintenance systématique est réalisée selon un calendrier ou un nombre d'heures de fonctionnement."
  "|La maintenance conditionnelle déclenche l'action selon l'état réel de l'équipement."
  "|Un plan de maintenance recense les tâches, les périodicités et les responsables."
  "|La périodicité est déterminée à partir de la durée de vie des composants et du retour d'expérience."
  "|Les interventions préventives réduisent les arrêts non prévus mais ont un coût propre."
  "|Le coût total de maintenance doit être optimisé, pas simplement minimisé."
  "|Une intervention trop fréquente peut être inutile et générer des pannes d'initiative."
  "|La GMAO permet de programmer les ordres de travail et de suivre leur exécution."
  "|Les pièces et les outils nécessaires doivent être disponibles avant l'intervention."
  "|Chaque intervention doit faire l'objet d'un compte rendu et d'une mise à jour du plan."),
[QC("Quand intervient la maintenance préventive ?", "Après la panne~Avant la panne~Uniquement la nuit~Sans planification", 1,
     "La préventive agit avant la défaillance selon un calendrier ou un état mesuré."),
 QC("Quelle maintenance est déclenchée par une mesure d'état ?", "Systématique~Conditionnelle~Corrective~Curative", 1,
     "La maintenance conditionnelle utilise l'état réel, par exemple une vibration."),
 QC("Que contient un plan de maintenance ?", "Seulement les prix~Les tâches, périodicités et responsables~Les horaires du personnel~Le nom du client", 1,
     "Le plan définit quoi faire, quand et par qui."),
 QC("Que vise l'optimisation du coût de maintenance ?", "Le coût le plus bas possible~Le meilleur compromis coût et disponibilité~Le plus grand nombre d'interventions~La suppression des contrôles", 1,
     "Trop ou pas assez de maintenance sont également coûteux."),
 QC("Quel est un inconvénient d'une maintenance trop fréquente ?", "Plus de fiabilité~Des pannes d'initiative et un coût inutile~Moins de papier~Une meilleure disponibilité", 1,
     "Démonter et remonter trop souvent peut créer de nouveaux défauts."),
 QC("Quel outil programme et suit les ordres de travail ?", "Un tableur de paie~Une GMAO~Un logiciel de dessin~Un navigateur web", 1,
     "La GMAO gère les ordres de travail et l'historique des interventions."),
 QC("Quelle est la dernière étape d'une intervention préventive ?", "Fermer la GMAO sans commentaire~Rédiger le compte rendu et mettre à jour le plan~Remplacer toute la machine~Ignorer les mesures", 1,
     "Le retour d'expérience alimente le plan de maintenance."),
 QT("Distinguer maintenance systématique et maintenance conditionnelle, et indiquer quand choisir chacune.",
    "La maintenance systématique est exécutée à échéance fixe, par exemple tous les 2 000 heures ou tous les six mois, que l'équipement soit en bon état ou non. Elle convient aux composants à usure prévisible et aux équipements dont la défaillance aurait des conséquences graves. La maintenance conditionnelle repose sur des mesures : vibration, température, taux d'humidité de l'huile. Elle est plus économique pour les machines dont l'état varie beaucoup selon l'usage, mais elle exige des capteurs et une interprétation fiable. En pratique, on combine souvent les deux approches sur un même site.",
    "On oppose échéance fixe et état mesuré, puis on justifie le choix par la criticité et la variabilité d'usage."),
 QT("Un convoyeur présente une usure de courroie après 1 800 h alors que la periodicité prévue est de 2 500 h. Que faire ?",
    "On ne se contente pas de remplacer la courroie : on analyse la cause de l'usure prématurée, par exemple un mauvais alignement, une tension excessive ou un produit abrasif. On relève la tension, l'alignement et l'état des rouleaux, puis on consigne les mesures dans la GMAO. On ajuste la périodicité à 1 500 h pour éviter une nouvelle rupture tant que la cause n'est pas supprimée, puis on reprogramme une intervention corrective sur les rouleaux. Enfin, on met à jour le plan de maintenance et le retour d'expérience pour les convoyeurs du même atelier.",
    "On attend une analyse de cause, une action immédiate et une mise à jour du plan.")],
C("La préventive agit avant la panne : on planifie, on mesure, puis on met à jour le plan à partir du retour d'expérience.",
  "Coût global = coût des interventions + coût des arrêts évités",
  "Systématique : à échéance fixe · Conditionnelle : selon l'état mesuré",
  "Préventive~Avant la défaillance~Systématique~Selon un calendrier~Conditionnelle~Selon l'état~Corrective~Après la panne~GMAO~Planification des ordres",
  "Recenser les équipements et leur criticité|Définir les tâches et périodicités|Planifier les ordres dans la GMAO|Réaliser et documenter l'intervention|Analyser les écarts et réviser le plan",
  "Confondre préventive et corrective|Intervenir trop souvent sans justification|Ignorer le retour d'expérience|Oublier de vérifier la disponibilité des pièces",
  "Courroie~Usure à 1 800 h~Périodicité~2 500 h prévus~Action~Révision à 1 500 h~Cause~Alignement à contrôler~GMAO~Historique mis à jour",
  "Systématique~Échéance fixe~Conditionnelle~Mesure de l'état",
  "Préventive~Évite la panne~Corrective~Répare la panne"))

# ============================================================ ME2
add("ME2", "Maintenance corrective : diagnostic et remise en état", "Maintenance mécanique",
S("La maintenance corrective intervient après la détection d'une défaillance."
  "|Elle est dite curative lorsqu'elle vise à rétablir la fonction sans Analyse de cause."
  "|La maintenance palliative supprime temporairement le symptôme sans éliminer la cause."
  "|Un diagnostic correct commence par l'observation des symptômes et des conditions d'apparition."
  "|La méthode des 5 Pourquoi permet de remonter à la cause racine."
  "|L'analyse fonctionnelle compare le comportement réel à la fonction attendue."
  "|Le test par élimination consiste à isoler successivement les causes possibles."
  "|Un arbre de défaillance représente les combinaisons de causes conduisant au dysfonctionnement."
  "|La sécurité de l'intervention précède toujours le diagnostic : consignation et vérification."
  "|La remise en état comprend le remplacement, le réglage puis un essai fonctionnel."
  "|L'essai doit être réalisé dans les conditions réelles de charge et de vitesse."
  "|Le compte rendu consigne le symptôme, la cause, l'action et le résultat de l'essai."),
[QC("Quand intervient la maintenance corrective ?", "Avant la panne~Après la détection d'une panne~Jamais~Uniquement en préventif", 1,
     "La corrective est déclenchée par une défaillance observée."),
 QC("Que fait une maintenance palliative ?", "Elle supprime la cause~Elle supprime temporairement le symptôme~Elle planifie la prévention~Elle remplace la machine", 1,
     "Le palliatif soulage sans éliminer la cause profonde."),
 QC("À quoi sert la méthode des 5 Pourquoi ?", "À calculer un rendement~À rechercher la cause racine~À rédiger un devis~À dessiner un schéma", 1,
     "On répète la question Pourquoi jusqu'à atteindre la cause fondamentale."),
 QC("Quelle est la première priorité avant tout diagnostic ?", "Démonter la machine~La sécurité et la consignation~Appeler le client~Augmenter la vitesse", 1,
     "On met l'équipement en sécurité avant d'intervenir."),
 QC("Que compare l'analyse fonctionnelle ?", "Le prix et la qualité~Le comportement réel et la fonction attendue~Deux marques~Les horaires", 1,
     "La panne est un écart entre la fonction attendue et le comportement observé."),
 QC("Qu'est-ce qu'un arbre de défaillance ?", "Un schéma de câblage~Une représentation des combinaisons de causes~Un graphique de production~Un plan de maintenance", 1,
     "Il relie l'événement indésirable à ses causes par des portes logiques."),
 QC("Que doit contenir l'essai final ?", "Uniquement un démarrage à vide~Les conditions réelles de charge et de vitesse~Une estimation~L'avis du seul opérateur", 1,
     "Un essai à vide ne révèle pas tous les défauts de charge."),
 QT("Décrire la démarche de diagnostic d'une pompe qui ne débite plus, depuis le signalement jusqu'à la remise en service.",
    "On relève d'abord le signalement : date, symptôme, conditions de fonctionnement. On met la pompe en sécurité par consignation et on vérifie l'absence de tension et de pression. On observe ensuite les signes : bruit, vibration, température, pression d'aspiration et de refoulement. On compare ces mesures aux valeurs nominales, puis on élimine les causes possibles les unes après les autres : alimentation, sens de rotation, obturation de la crépine, cavitation, usure de la roue. Une fois la cause identifiée, on remplace ou règle l'organe fautif, on remonte, puis on effectue un essai en charge avec relevé du débit et de la pression. On termine par le compte rendu et la mise à jour de la GMAO.",
    "On attend: sécurité, observation, mesures, élimination des causes, réparation, essai et documentation."),
 QT("Appliquer la méthode des 5 Pourquoi au cas suivant : 'une courroie de convoyeur s'est rompue prématurément'.",
    "1. Pourquoi la courroie s'est-elle rompue ? Parce qu'elle était trop tendue. 2. Pourquoi était-elle trop tendue ? Parce que le tendeur a été serré sans repère de tension. 3. Pourquoi n'y avait-il pas de repère ? Parce que la procédure de remplacement ne précisait pas la valeur de tension. 4. Pourquoi la procédure était-elle incomplète ? Parce qu'elle n'a pas été mise à jour après le changement de modèle de courroie. 5. Pourquoi n'a-t-elle pas été mise à jour ? Parce qu'aucune revue documentaire n'est programmée après modification. La cause racine n'est donc pas la courroie mais l'absence de revue des procédures. L'action corrective consiste à rédiger la valeur de tension et à instaurer une revue systématique.",
    "On doit aboutir à une cause organisationnelle et proposer une action qui empêche la récidive.")],
C("La corrective rétablit la fonction, mais seul le diagnostic de cause évite la récidive : sécurité, mesures, essai, trace.",
  "Symptôme ≠ cause · cause racine = niveau le plus profond",
  "5 Pourquoi · arbre de défaillance · test par élimination",
  "Corrective~Après la panne~Palliative~Supprime le symptôme~Symptôme~Signe observe~Cause racine~Origine profonde~Consignation~Mise en securite",
  "Sécuriser et consigner|Observer et relever les symptômes|Mesurer et comparer aux valeurs nominales|Éliminer les causes possibles|Réparer, essayer et documenter",
  "Réparer sans chercher la cause|Se contenter d'un palliatif durable|Intervenir avant consignation|Essayer uniquement à vide",
  "Pompe~Ne débite plus~Pression~Relevée aux deux brides~Cavitation~Cause possible~Essai~Débit nominal vérifié~GMAO~Historique complet",
  "Curative~Rétablit la fonction~Palliative~Supprime le symptôme",
  "Symptôme~Ce que l'on voit~Cause~Ce qui a provoqué"))

# ============================================================ ME3
add("ME3", "Lubrification et usure des organes mécaniques", "Maintenance mécanique",
S("La lubrification réduit le frottement et l'usure entre deux surfaces en mouvement."
  "|Le lubrifiant forme un film séparant les aspérités des surfaces."
  "|Les principales fonctions d'une huile sont la lubrification, le refroidissement et l'évacuation des contaminants."
  "|Une huile est caractérisée par sa viscosité, son indice de viscosité et son point d'écoulement."
  "|La norme ISO VG classe les huiles par famille de viscosité."
  "|La graisse est utilisée lorsque le renouvellement d'huile est difficile, par exemple sur un roulement."
  "|Une lubrification insuffisante provoque échauffement, usure abrasive et grippage."
  "|Un excès de lubrifiant peut également nuire, notamment en entraînant des pertes par barattage."
  "|Les modes d'usure courants sont l'abrasion, l'adhérence, la fatigue et la corrosion."
  "|L'analyse d'huile permet de détecter la présence de métaux, d'eau ou de produits de dégradation."
  "|La propreté lors du remplissage est essentielle : une poussière devient un abrasif."
  "|Le choix du lubrifiant et de la périodicité doit respecter la notice constructeur."),
[QC("Quelle est la fonction principale d'un lubrifiant ?", "Augmenter le frottement~Réduire le frottement et l'usure~Refroidir uniquement~Nettoyer uniquement", 1,
     "Le film d'huile sépare les surfaces et limite l'usure."),
 QC("Quelle grandeur classe les huiles selon la norme ISO VG ?", "La couleur~La viscosité~Le prix~L'odeur", 1,
     "ISO VG classe les huiles par plages de viscosité."),
 QC("Quand utilise-t-on plutôt une graisse ?", "Quand le renouvellement est difficile~Quand la vitesse est très élevée~Toujours~Jamais", 0,
     "La graisse reste en place, utile pour un roulement peu accessible."),
 QC("Quel risque entraîne une lubrification insuffisante ?", "Un grippage~Une meilleure étanchéité~Une baisse de température~Une purge automatique", 0,
     "Sans film lubrifiant, les surfaces entrent en contact et peuvent se gripper."),
 QC("Quel est un inconvénient d'un excès de lubrifiant ?", "Aucun~Des pertes par barattage et échauffement~Plus de propreté~Une usure moindre dans tous les cas", 1,
     "Trop d'huile peut provoquer des pertes d'énergie et des fuites."),
 QC("Que révèle une analyse d'huile ?", "La couleur du bidon~La présence de métaux, d'eau ou de dégradation~La marque de la machine~Le nombre d'heures seulement", 1,
     "L'analyse d'huile est un outil de maintenance conditionnelle."),
 QC("Quelle précaution est essentielle lors d'un remplissage ?", "Travailler vite~Garder la propreté~Utiliser n'importe quelle huile~Laisser le bouchon ouvert", 1,
     "Une contamination particulate accélère fortement l'usure."),
 QT("Expliquer le rôle du film lubrifiant et les conséquences d'un film rompu entre un arbre et son roulement.",
    "Le film lubrifiant sépare les micro-aspérités des deux surfaces : le frottement devient celui du liquide, beaucoup plus faible que le contact métal contre métal. Il évacue aussi la chaleur et les débris. Si le film se rompt, par suite d'une viscosité trop faible, d'une surcharge ou d'une température excessive, les aspérités entrent en contact : la température monte, des particules métalliques sont arrachées, l'usure s'accélère et le grippage peut conduire au blocage du roulement. Une analyse d'huile révèle alors une augmentation du taux de fer et une dégradation de l'huile.",
    "On décrit le film, ses fonctions, puis la chaîne de conséquences d'une rupture."),
 QT("Un moteur consomme anormalement son huile. Proposer une démarche de diagnostic et les actions possibles.",
    "On vérifie d'abord le niveau et l'aspect de l'huile, puis on recherche des fuites externes au niveau des joints et du bouchon de vidange. On contrôle ensuite les symptômes associés : fumée bleue, consommation de liquide de refroidissement, pression d'huile anormale. On relève les heures de fonctionnement et on compare avec la périodicité de vidange et la qualité d'huile prescrite. Les causes possibles sont un joint usé, un remplissage excessif, une huile trop fluide ou un segment de piston défectueux. On remplace le joint ou l'organe fautif, on refait le niveau avec la bonne huile, puis on contrôle la consommation après un essai en charge.",
    "On attend une recherche structurée des fuites, la vérification de la qualité d'huile et un essai final.")],
C("Une huile adaptée, propre et renouvelée à temps protège les organes : la lubrification est un levier de fiabilité.",
  "Film séparateur = viscosité + charge + vitesse",
  "ISO VG : famille de viscosité · analyse d'huile : particules et eau",
  "Viscosite~Resistance a l'ecoulement~Film~Se aure les surfaces~ISO VG~Classement des huiles~Graisse~Lubrifiant fixe~Analyse d'huile~Diagnostic conditionnel",
  "Identifier le lubrifiant prescrit|Vérifier niveau et aspect|Prélever un échantillon si besoin|Remplir dans la propreté|Noter l'intervention dans la GMAO",
  "Mélanger deux huiles incompatibles|Remplir sans contrôle de propreté|Confondre graisse et huile|Ignorer la notice constructeur",
  "Huile ISO VG 46~Viscosite nominale~Roulement~Graissage initial~Analyse~Fer et eau detectes~Pannes~Usure abrasive~Vidange~Selon prescription",
  "Huile~Renouvelable~Graisse~Reste en place",
  "Sous-lubrification~Grippage~Sur-lubrification~Barattage et fuites"))

# ============================================================ ME4
add("ME4", "Courroies, chaînes et roulements : contrôle et réglage", "Maintenance mécanique",
S("Une courroie transmission le mouvement entre deux poulies par adhérence."
  "|Une chaîne transmet le mouvement par engrènement sur des pignons."
  "|La courroie plate ou trapézoïdale est silencieuse mais peut patiner."
  "|La chaîne ne patine pas mais nécessite une lubrification et un contrôle de tension."
  "|La tension d'une courroie doit respecter la valeur indiquée par le constructeur."
  "|Une courroie trop lâche patine et s'échauffe ; trop tendue, elle use les roulements."
  "|L'alignement des poulies se contrôle avec une règle ou un laser."
  "|Un désalignement provoque une usure latérale et une détérioration prématurée."
  "|Un roulement est composé de deux bagues, d'éléments roulants et d'une cage."
  "|Un roulement usé se manifeste par du bruit, des vibrations et un échauffement."
  "|Le contrôle de l'état se fait par écoute, mesure de vibration et vérification du jeu."
  "|Le remplacement doit respecter le montage, la lubrification et le sens de montage indiqués."),
[QC("Comment une courroie transmet-elle le mouvement ?", "Par engrènement~Par adhérence~Par aimantation~Par gravité", 1,
     "La courroie adhère à la gorge de la poulie ; la chaîne, elle, s'engrène."),
 QC("Quel est un avantage d'une chaîne ?", "Elle est silencieuse~Elle ne patine pas~Elle ne demande aucun entretien~Elle ne s'use jamais", 1,
     "L'engrènement évite le patinage mais exige lubrification et tension."),
 QC("Que provoque une courroie trop lâche ?", "Un patinage~Une usure des roulements par surcharge~Une meilleure transmission~Aucun effet", 0,
     "Le patinage réduit la transmission et génère de la chaleur."),
 QC("Comment contrôler l'alignement des poulies ?", "A l'oreille~Avec une règle ou un laser~Avec un voltmètre~Avec une balance", 1,
     "Une règle ou un laser permet de mesurer le désalignement."),
 QC("Quels sont les éléments d'un roulement ?", "Deux bagues, éléments roulants, cage~Un arbre, une clé, un écrou~Un stator, un rotor, un entrefer~Une poulie, une courroie, un moteur", 0,
     "Le roulement se compose de deux bagues, d'éléments roulants et d'une cage."),
 QC("Quel signe indique un roulement usé ?", "Un silence total~Du bruit et des vibrations~Une baisse de tension electrique~Une couleur uniforme", 1,
     "Bruit, vibrations et échauffement sont les signes classiques."),
 QC("Quelle précaution lors du remplacement d'un roulement ?", "Monter à coups de marteau~Respecter le sens de montage et la lubrification~Ne pas lire la notice~Laisser le jeu libre", 1,
     "Un montage incorrect réduit fortement la durée de vie."),
 QT("Comparer les avantages et inconvénients d'une transmission par courroie et par chaîne.",
    "La courroie est silencieuse, absorbe les chocs, ne nécessite pas de lubrification et coûte peu. En revanche, elle peut patiner, vieillit sous l'effet de la chaleur et exige un contrôle de tension et d'alignement. La chaîne transmet sans patinage, supporte des charges importantes et reste efficace en environnement sale, mais elle est plus bruyante, doit être lubrifiée et s'allonge avec l'usure. Le choix dépend de la puissance à transmettre, de la distance entre axes, du bruit admissible et des contraintes d'entretien.",
    "On attend une comparaison sur la transmission, le bruit, l'entretien et la durée de vie."),
 QT("Un roulement de moteur chauffe et fait du bruit après 6 mois. Décrire le diagnostic et la remise en état.",
    "On arrête et consigne le moteur, puis on vérifie la température au thermomètre ou au thermomètre infrarouge et on mesure les vibrations avec un vibromètre. On contrôle la lubrification : quantité, type de graisse et état des joints d'étanchéité. On vérifie également l'alignement du moteur et de la machine entraînée, car un désalignement surcharge le roulement. Si le bruit persiste à la rotation manuelle et que le jeu est anormal, on dépose le roulement, on examine les bagues et les éléments roulants, puis on le remplace en respectant le sens de montage et la graisse prescrite. On refait un essai en charge et on relève les vibrations après remontage.",
    "On attend mesures, vérification de la cause, remplacement conforme et essai de contrôle.")],
C("Courroie, chaîne et roulement sont des organes de transmission : tension, alignement et lubrification conditionnent leur vie.",
  "Tension conforme + alignement + lubrification = durée de vie",
  "Courroie : adhérence · chaîne : engrènement · roulement : éléments roulants",
  "Courroie~Adherence et silence~Chaine~En-grenement sans patinage~Tension~Valeur constructeur~Alignement~Controle a la regle~Roulement~Bagues et billes",
  "Consigner et sécuriser|Contrôler tension et alignement|Mesurer bruit, vibration et température|Vérifier lubrification et jeu|Remplacer et essayer en charge",
  "Confondre adhérence et engrènement|Tendre excessivement une courroie|Monter un roulement sans lubrifiant|Oublier l'alignement",
  "Courroie~Patine si lache~Chaine~Lubrification necessaire~Roulement~Bruit et vibration~Alignement~Usure laterale~Vibration~Mesure en mm/s",
  "Courroie~Adherence~Chaine~En-grenement",
  "Roulement sain~Silencieux~Roulement use~Bruyant et chaud"))

# ============================================================ ME5
add("ME5", "Contrôles mécaniques : vibrations, alignement et jeux", "Maintenance mécanique",
S("Le contrôle mécanique permet de suivre l'état d'un équipement sans le démonter."
  "|La vibration est une oscillation mécanique caractérisée par une amplitude et une fréquence."
  "|La vitesse de vibration s'exprime en millimètres par seconde, selon la norme ISO 10816."
  "|Une augmentation de la vibration signale souvent un déséquilibre, un désalignement ou un roulement usé."
  "|Le déséquilibre se manifeste à la fréquence de rotation."
  "|Le désalignement produit des vibrations radiales et axiales, souvent à deux fois la fréquence de rotation."
  "|Un capteur accéléromètre convertit la vibration en signal électrique."
  "|L'analyse spectrale répartit l'amplitude selon les fréquences pour identifier la cause."
  "|L'alignement se mesure avec un comparateur, une règle ou un outil laser."
  "|Le jeu radial est le déplacement libre perpendiculaire à l'axe ; le jeu axial est parallèle à l'axe."
  "|Les valeurs relevées doivent être comparées à des références et enregistrées dans la GMAO."
  "|Une tendance à la hausse est plus informative qu'une mesure isolée."),
[QC("Quelle unité exprime la vitesse de vibration selon ISO 10816 ?", "Le mm/s~Le volt~Le degré~Le kg", 0,
     "La norme utilise la vitesse efficace en mm/s."),
 QC("Quelle cause produit une vibration à la fréquence de rotation ?", "Le désalignement~Le déséquilibre~La cavitation~Le court-circuit", 1,
     "Le déséquilibre tourne avec la machine, donc à sa fréquence de rotation."),
 QC("Que mesure un accéléromètre ?", "La température~L'accélération de la vibration~La pression~La tension", 1,
     "Il convertit l'accélération mécanique en signal électrique."),
 QC("À quoi sert l'analyse spectrale ?", "À mesurer la couleur~À répartir l'amplitude par fréquence~À compter les heures~À régler la tension", 1,
     "Chaque défaut a une signature fréquentielle particulière."),
 QC("Quel est le jeu radial ?", "Le déplacement le long de l'axe~Le déplacement perpendiculaire à l'axe~La température~La vitesse", 1,
     "Radial signifie perpendiculaire à l'axe de rotation."),
 QC("Pourquoi suivre une tendance plutôt qu'une mesure isolée ?", "C'est plus rapide~Cela révèle une dégradation progressive~C'est moins cher~Cela évite de mesurer", 1,
     "La dérive dans le temps est le signe d'une usure en cours."),
 QC("Où enregistrer les relevés de contrôle ?", "Sur un coin de papier~Dans la GMAO~Dans la paie~Nulle part", 1,
     "La GMAO conserve l'historique et permet de suivre les tendances."),
 QT("Un moteur présente une vitesse de vibration de 2,1 mm/s puis 4,8 mm/s en trois semaines. Interpréter cette évolution.",
    "La valeur de 2,1 mm/s correspond à un état acceptable pour beaucoup de machines de taille moyenne selon ISO 10816. Trois semaines plus tard, 4,8 mm/s traduisent une dégradation rapide, probablement due à un déséquilibre, un désalignement ou un début de défaut de roulement. On ne peut pas déterminer la cause avec la seule amplitude globale : il faut réaliser une analyse spectrale et comparer les composantes à la fréquence de rotation, à 2 fois cette fréquence et aux fréquences propres des roulements. On programme une intervention avant d'atteindre le seuil d'alerte, en complétant par une mesure de température et un contrôle d'alignement.",
    "On interprète la tendance, puis on propose une analyse fréquentielle et une action préventive."),
 QT("Expliquer la différence entre mesure globale de vibration et analyse spectrale.",
    "La mesure globale donne une valeur unique, par exemple 4,8 mm/s, qui indique l'état général de la machine et permet de suivre une tendance ou de comparer à une norme. Elle ne dit pas quelle est la cause. L'analyse spectrale décompose le signal en fréquences : une pointe à la fréquence de rotation évoque un déséquilibre, une pointe à deux fois la fréquence un désalignement, et des composantes à fréquences élevées un défaut de roulement. On utilise donc la mesure globale pour alerter et l'analyse spectrale pour diagnostiquer.",
    "On oppose suivi de tendance et identification de la cause par fréquence.")],
C("Le contrôle mécanique transforme bruit, vibration et température en indicateurs : la tendance alerte, le spectre diagnostique.",
  "Vitesse de vibration en mm/s · ISO 10816",
  "Fréquence de rotation : déséquilibre · 2x rotation : désalignement",
  "Vibration~Oscillation mecanique~mm/s~Unite normalisee~Spectre~Amplitude par frequence~Desequilibre~A la rotation~Jeu radial~Perpendiculaire a l'axe",
  "Choisir le point de mesure|Relever vibration et température|Comparer aux seuils et à l'historique|Analyser le spectre si anomalie|Programmer l'action et archiver",
  "Comparer des mesures prises en des points différents|Se fier à une seule mesure|Ignorer la charge au moment du relevé|Oublier d'enregistrer la date",
  "Moteur~2,1 puis 4,8 mm/s~Tendance~Fort hausse~Spectre~A faire~Temp~Mesure complementaire~GMAO~Historique",
  "Mesure globale~Etat general~Analyse spectrale~Cause du defaut",
  "Jeu radial~Perpendiculaire~Jeu axial~Parallele a l'axe"))

# ============================================================ EL1
add("EL1", "Lecture des schémas électriques et respect des normes", "Maintenance électrique",
S("Un schéma électrique est un document normalisé qui décrit les liaisons entre composants."
  "|Le schéma de principe montre la fonction logique, indépendamment de l'implantation physique."
  "|Le schéma de câblage représente les conducteurs et les bornes réels."
  "|Le plan d'implantation situe les matériels dans l'armoire ou sur la machine."
  "|La norme IEC 60617 définit les symboles graphiques des composants."
  "|La norme IEC 61346 ou IEC 81346 définit les règles d'identification des équipements."
  "|Un repère tel que KM1 identifie un contacteur, QF un disjoncteur et FR un relais thermique."
  "|Les bornes sont numérotées pour retrouver les points de raccordement."
  "|Un schéma se lit généralement de gauche à droite et de haut en bas."
  "|Les contacts sont représentés dans leur état au repos, c'est-à-dire sans excitation."
  "|Un contact NO est ouvert au repos, un contact NF est fermé au repos."
  "|Toute modification doit être reportée sur le schéma pour conserver sa conformité."),
[QC("Quel schéma montre la fonction logique ?", "Le plan d'implantation~Le schéma de principe~Le schéma de câblage~Le devis", 1,
     "Le schéma de principe décrit la fonction sans se préoccuper du câblage réel."),
 QC("Quelle norme définit les symboles électriques ?", "ISO 10816~IEC 60617~ISO 9001~IEC 60364 uniquement", 1,
     "La norme IEC 60617 normalise les symboles graphiques."),
 QC("Que signifie un contact NO ?", "Fermé au repos~Ouvert au repos~Toujours fermé~Sans borne", 1,
     "NO signifie Normalement Ouvert : le contact est ouvert sans excitation."),
 QC("Que représente le repère KM1 ?", "Un moteur~Un contacteur~Une résistance~Un capteur de pression", 1,
     "KM désigne un contacteur, le chiffre indique son rang."),
 QC("Dans quel état sont représentés les contacts sur un schéma ?", "Excités~Au repos~En défaut~Aléatoire", 1,
     "La convention est de dessiner les contacts dans leur état de repos."),
 QC("Quel document situe les matériels dans l'armoire ?", "Le schéma de principe~Le plan d'implantation~La nomenclature~Le calendrier", 1,
     "Le plan d'implantation donne la position physique des composants."),
 QC("Que faut-il faire après une modification du câblage ?", "Rien~Reporter la modification sur le schéma~Jeter le schéma~Attendre la prochaine visite", 1,
     "Un schéma non mis à jour devient une source d'erreur et de danger."),
 QT("Expliquer la différence entre schéma de principe et schéma de câblage, et dire quand utiliser chacun.",
    "Le schéma de principe présente la chaîne fonctionnelle : alimentation, protection, commande et puissance, avec les relations logiques entre les composants. Il est destiné à comprendre le fonctionnement et à raisonner sur un défaut. Le schéma de câblage représente les conducteurs réels, les bornes et les cheminements dans l'armoire ; il sert au montage, à la vérification des raccordements et au dépannage sur site. Pour diagnostiquer un défaut, on part du principe pour identifier la fonction concernée, puis on utilise le câblage pour mesurer au bon endroit.",
    "On oppose fonction logique et réalisation physique, avec un usage pour chacun."),
 QT("Dans un schéma de commande de moteur, décrire le rôle du contacteur KM1, du relais thermique FR et du disjoncteur QF.",
    "QF est le disjoncteur de protection : il coupe l'alimentation en cas de court-circuit ou de surcharge et assure la consignation. KM1 est le contacteur : sa bobine, alimentée par la commande, ferme ses contacts principaux pour alimenter le moteur et son contact auxiliaire pour l'auto-maintenu. FR est le relais thermique : il détecte un échauffement lié à une surcharge prolongée et ouvre son contact NF dans le circuit de commande, ce qui fait tomber la bobine KM1. Ces trois appareils assurent respectivement la protection, la commande et la protection contre la surcharge.",
    "On attribue à chaque appareil sa fonction et on explique leur coordination.")],
C("Un schéma normalisé se lit selon des conventions : symboles, repères, bornes et état de repos des contacts.",
  "Principe = fonction · câblage = conducteurs réels",
  "IEC 60617 : symboles · IEC 81346 : identification",
  "Schema de principe~Fonction logique~Schema de cablage~Liaisons reelles~IEC 60617~Symboles~Contact NO~Ouvert au repos~Repere KM~Contacteur~Borne~Point de raccordement",
  "Repérer le circuit de puissance et le circuit de commande|Lire les repères d'équipement|Identifier l'état de repos des contacts|Suivre le cheminement logique|Vérifier la conformité sur site",
  "Lire un contact NF comme un contact NO|Ignorer la numérotation des bornes|Oublier de mettre à jour le schéma|Confondre principe et implantation",
  "QF~Disjoncteur~KM1~Contacteur moteur~FR~Relais thermique~NO~Ouvert au repos~NF~Ferme au repos",
  "Principe~Comprendre la fonction~Cablage~Retrouver les fils",
  "Contact NO~Ouvert au repos~Contact NF~Ferme au repos"))

# ============================================================ EL2
add("EL2", "Moteurs asynchrones : constitution et fonctionnement", "Maintenance électrique",
S("Le moteur asynchrone est le moteur électrique le plus utilisé en industrie."
  "|Il comprend un stator fixe et un rotor mobile séparés par un entrefer."
  "|Le stator porte les enroulements alimentés par le réseau triphasé."
  "|Le réseau triphasé crée un champ magnétique tournant à la vitesse de synchronisme."
  "|La vitesse de synchronisme vaut ns = 60 f / p, avec f la fréquence et p le nombre de paires de pôles."
  "|Le rotor est généralement de type cage d'écureuil, sans connexion électrique externe."
  "|Le couple naît de l'induction : le rotor suit le champ tournant avec un glissement."
  "|Le glissement g = (ns - n) / ns est d'environ 2 à 6 % à pleine charge."
  "|Un moteur asynchrone ne peut pas tourner à la vitesse de synchronisme en charge."
  "|Le sens de rotation dépend de l'ordre des phases : inverser deux phases inverse le sens."
  "|Le démarrage direct absorbe un courant plusieurs fois supérieur au courant nominal."
  "|Le relais thermique protège le moteur contre les surcharges prolongées."),
[QC("Combien de paires de pôles faut-il pour un moteur 50 Hz tournant à 1500 tr/min environ ?", "1~2~4~8", 1,
     "ns = 60 x 50 / 2 = 1500 tr/min ; la vitesse réelle est légèrement inférieure."),
 QC("Comment appelle-t-on l'espace entre stator et rotor ?", "L'entrefer~Le glissement~L'encoche~La cage", 0,
     "L'entrefer est la faible distance d'air séparant les deux parties."),
 QC("Que vaut typiquement le glissement à pleine charge ?", "0 %~2 à 6 %~20 %~50 %", 1,
     "Le rotor tourne légèrement moins vite que le champ tournant."),
 QC("Que se passe-t-il si on inverse deux phases ?", "Le moteur s'arrête~Le sens de rotation s'inverse~La vitesse double~Le courant devient nul", 1,
     "L'ordre des phases détermine le sens du champ tournant."),
 QC("Quel est le rôle du relais thermique ?", "Augmenter le courant~Protéger contre la surcharge~Changer la fréquence~Inverser le sens", 1,
     "Il coupe la commande lorsque le moteur chauffe trop."),
 QC("Quel est le inconvénient du démarrage direct ?", "Un courant de démarrage élevé~Une vitesse trop basse~Un couple nul~Une fréquence trop haute", 0,
     "Le courant de démarrage peut atteindre plusieurs fois le courant nominal."),
 QC("Quel type de rotor est le plus courant ?", "Rotor bobiné~Cage d'écureuil~Rotor à aimants~Rotor à reluctance", 1,
     "La cage d'écureuil est robuste et sans entretien."),
 QT("Un moteur triphasé 400 V, 50 Hz, 4 pôles a une vitesse nominale de 1440 tr/min. Calculer la vitesse de synchronisme et le glissement.",
    "La vitesse de synchronisme vaut ns = 60 f / p = 60 x 50 / 2 = 1500 tr/min, car 4 pôles correspondent à 2 paires de pôles. Le glissement vaut g = (ns - n) / ns = (1500 - 1440) / 1500 = 60 / 1500 = 0,04, soit 4 %. Cette valeur est typique d'un moteur asynchrone à pleine charge : le rotor tourne 60 tr/min moins vite que le champ tournant.",
    "On calcule ns, puis g, avec l'identification du nombre de paires de pôles."),
 QT("Expliquer pourquoi un moteur asynchrone absorbe un courant élevé au démarrage et comment y remédier.",
    "Au démarrage, le rotor est immobile : le champ tournant balaie les conducteurs de la cage à la fréquence réseau, ce qui induit des courants importants et produit un fort couple, mais avec un facteur de puissance défavorable. Le courant absorbé peut atteindre cinq à sept fois le courant nominal. Cela provoque des chutes de tension et sollicite le réseau et les contacts. On y remédie par un démarrage étoile-triangle, un variateur de fréquence qui augmente progressivement la fréquence et la tension, ou un démarreur électronique. Le choix dépend du couple de démarrage nécessaire et de la puissance du moteur.",
    "On explique l'induction à rotor arrêté et on cite au moins deux solutions de démarrage.")],
C("Le moteur asynchrone suit le champ tournant avec un glissement : vitesse, sens de rotation et protection en découlent.",
  "ns = 60 f / p · g = (ns - n) / ns",
  "Cage d'écureuil · 2 phases inversées = sens inversé",
  "Stator~Partie fixe~Rotor~Partie mobile~Entrefer~Intervalle d'air~Champ tournant~Cree par le triphase~Glissement~Difference de vitesse~Relais thermique~Protection surcharge",
  "Vérifier la plaque signalétique|Contrôler l'alimentation et l'ordre des phases|Mesurer la vitesse|Calculer le glissement|Vérifier la protection thermique",
  "Confondre pôles et paires de pôles|Croire que le rotor atteint ns|Inverser les phases sans précautions|Ignorer le courant de démarrage",
  "50 Hz 4 pôles~ns = 1500 tr/min~Vitesse reelle~1440 tr/min~Glissement~4 %~Demarrage~Courant 5 a 7 fois nominal~Protection~Relais thermique",
  "Stator~Fixe~Rotor~Mobile",
  "Asynchrone~Avec glissement~Synchrone~Sans glissement"))

# ============================================================ EL3
add("EL3", "Diagnostic électrique : tension, continuité et isolement", "Maintenance électrique",
S("Le diagnostic électrique repose sur des mesures comparées aux valeurs nominales."
  "|Le multimètre mesure la tension, l'intensité, la résistance et parfois la température."
  "|La mesure de tension se fait en parallèle aux bornes du composant."
  "|La mesure d'intensité se fait en série dans le circuit."
  "|Un contrôle de continuité vérifie qu'un conducteur n'est pas rompu."
  "|La continuité se mesure avec la fonction ohmètre ou le testeur de continuité, hors tension."
  "|La mesure d'isolement vérifie la résistance entre un conducteur actif et la terre."
  "|Le mégohmmètre applique une tension continue élevée, par exemple 500 V."
  "|Une résistance d'isolement faible signale une humidité ou un vieillissement des isolants."
  "|Les mesures doivent être effectuées hors tension pour la résistance et l'isolement."
  "|Une terre défectueuse compromet la sécurité des personnes et le fonctionnement des protections."
  "|Les résultats sont consignés avec la date, les valeurs et les références utilisées."),
[QC("Comment mesurer une tension ?", "En série~En parallèle aux bornes~A la terre uniquement~Sans brancher", 1,
     "Le voltmètre se branche en dérivation aux bornes du composant."),
 QC("Quand mesurer une résistance ?", "Sous tension~Hors tension~Pendant le démarrage~Peu importe", 1,
     "L'ohmmètre envoie son propre courant : la tension doit être coupée."),
 QC("Que vérifie un test de continuité ?", "La puissance~Qu'un conducteur n'est pas rompu~La fréquence~L'isolement", 1,
     "La continuité confirme que le chemin du courant est intact."),
 QC("Quel appareil mesure l'isolement ?", "Un voltmètre~Un mégohmmètre~Une pince ampèremétrique~Un oscilloscope", 1,
     "Le mégohmmètre applique une tension élevée et mesure une forte résistance."),
 QC("Qu'indique une faible résistance d'isolement ?", "Un bon état~Une humidité ou un isolant dégradé~Une tension trop élevée~Une charge normale", 1,
     "Une valeur basse révèle un défaut d'isolation."),
 QC("Que faire avant de mesurer une résistance sur un circuit avec condensateurs ?", "Rien~Les décharger~Augmenter la tension~Laisser le courant branché", 1,
     "Un condensateur chargé fausse la mesure et peut endommager l'appareil."),
 QC("Pourquoi consigner les mesures ?", "Pour le dossier papier seulement~Pour suivre l'évolution et tracer l'intervention~Pour augmenter la tension~Pour éviter de mesurer", 1,
     "L'historique permet de détecter une dérive et de justifier l'action."),
 QT("Décrire la procédure de contrôle d'isolement d'un moteur avant sa remise en service.",
    "On consigne le moteur et on vérifie l'absence de tension. On déconnecte les câbles d'alimentation et on décharge les éventuels condensateurs. On règle le mégohmmètre à la tension adaptée à la tension nominale du moteur, par exemple 500 V pour un moteur 400 V. On mesure la résistance entre chaque phase et la terre, puis entre les phases, en respectant le temps de charge de l'appareil. On compare les valeurs obtenues aux prescriptions du constructeur et aux mesures précédentes. On décharge ensuite les enroulements, on rebranche, puis on consigne les résultats avec la date et les références du mégohmmètre.",
    "On attend consignation, déconnexion, choix de la tension, mesure, comparaison et traçabilité."),
 QT("Un moteur fonctionne mais le disjoncteur se déclenche après quelques minutes. Proposer un diagnostic.",
    "On mesure d'abord l'intensité absorbée en fonctionnement avec une pince ampèremétrique et on la compare au courant nominal. Si elle est trop élevée, on recherche une surcharge mécanique, un désalignement ou un défaut de roulement. On contrôle ensuite la résistance d'isolement au mégohmmètre, hors tension, car une isolation dégradée peut provoquer un courant de fuite et un déclenchement différé. On vérifie également le réglage du relais thermique et l'état de ses contacts, ainsi que la tension d'alimentation. On teste enfin le disjoncteur lui-même si les mesures sont normales. Chaque mesure est relevée avant toute modification.",
    "On doit évoquer surcharge, isolement, réglage du relais et état du disjoncteur.")],
C("Le diagnostic électrique compare des mesures fiables aux valeurs nominales : tension en dérivation, intensité en série, isolement hors tension.",
  "Tension // · intensité série · isolement avec mégohmmètre",
  "Hors tension pour résistance et isolement · décharger les condensateurs",
  "Multimetre~Mesures multiples~Tension~En derivation~Intensite~En serie~Continuite~Conducteur intact~Megohmmetre~Mesure d'isolement",
  "Consigner et vérifier l'absence de tension|Déconnecter et décharger|Choisir la gamme et l'appareil|Mesurer et comparer aux références|Consigner les résultats",
  "Mesurer une résistance sous tension|Oublier de décharger un condensateur|Brancher l'ampèremètre en dérivation|Ne pas noter la date",
  "Moteur 400 V~Megohmmetre 500 V~Isol~Valeur conforme~Intensite~Comparee au nominal~Declaration~Mesure avant action~Terre~Securite",
  "Tension~En parallele~Intensite~En serie",
  "Continuite~Fils intact~Isolement~Resistance a la terre"))

# ============================================================ EL4
add("EL4", "Sécurité électrique et consignation des équipements", "Maintenance électrique",
S("La sécurité électrique vise à protéger les personnes contre les risques de choc et d'arc électrique."
  "|Le courant traverse le corps d'autant plus facilement que la tension est élevée et la peau humide."
  "|Une tension supérieure à 50 V en courant alternatif est considérée comme dangereuse."
  "|La mise à la terre et la liaison équipotentielle limitent les tensions de contact."
  "|Le disjoncteur différentiel détecte un courant de fuite vers la terre et coupe rapidement."
  "|Un seuil de 30 mA est couramment utilisé pour la protection des personnes."
  "|La consignation est une procédure qui met un équipement hors tension et l'empêche de redémarrer."
  "|Elle comprend la séparation, le verrouillage et la vérification d'absence de tension."
  "|La vérification d'absence de tension doit être faite avec un appareil fiable, avant et après l'essai."
  "|Le port des équipements de protection individuelle est obligatoire : gants isolants, lunettes, chaussures."
  "|Une attestation d'habilitation électrique est requise pour intervenir sur certaines installations."
  "|La remise sous tension suit une procédure : retrait des outils, fermeture des capots et information de l'équipe."),
[QC("À partir de quelle tension alternative le risque devient-il important ?", "5 V~12 V~50 V~230 V uniquement", 2,
     "Au-delà d'environ 50 V en alternatif, le courant peut traverser le corps."),
 QC("Que détecte un disjoncteur différentiel ?", "Une surcharge~Un courant de fuite vers la terre~Une baisse de tension~Une surchauffe moteur", 1,
     "Il compare courant aller et retour et coupe en cas de déséquilibre."),
 QC("Quel seuil est courant pour la protection des personnes ?", "300 mA~30 mA~3 A~30 A", 1,
     "Un différentiel 30 mA offre une protection complémentaire des personnes."),
 QC("Que signifie consigner un équipement ?", "Le nettoyer~Le mettre hors tension et empêcher tout redémarrage~Le repeindre~Le déplacer", 1,
     "La consignation sépare, verrouille et vérifie l'absence de tension."),
 QC("Quelle est la dernière étape de la consignation ?", "Fermer l'interrupteur~Vérifier l'absence de tension~Débrancher les outils~Appeler le client", 1,
     "La vérification d'absence de tension conclut la mise en sécurité."),
 QC("Quel EPI est spécifique aux interventions électriques ?", "Des gants isolants~Un casque de chantier~Des lunettes de soleil~Un tablier de cuisine", 0,
     "Les gants isolants protègent contre le contact électrique."),
 QC("Quand peut-on travailler sous tension ?", "Toujours~Exceptionnellement, dans un cadre réglementaire strict~Jamais, même pour un test~Sans habilitation", 1,
     "Les travaux sous tension sont exceptionnels et nécessitent une habilitation et une procédure."),
 QT("Décrire les étapes de la consignation d'une armoire électrique avant une intervention de maintenance.",
    "On informe d'abord les opérateurs concernés et on identifie précisément l'équipement. On coupe l'alimentation par le disjoncteur ou l'interrupteur approprié, puis on sépare les conducteurs si nécessaire. On verrouille l'organe de coupure avec un cadenas personnel et on appose une étiquette de consignation. On vérifie ensuite l'absence de tension avec un appareil contrôlé, en testant l'appareil avant et après la mesure sur une source connue. On vérifie également l'absence de tension résiduelle sur les condensateurs. On peut alors intervenir avec les EPI adaptés. À la fin, on retire les outils, on ferme les capots, on retire son cadenas et on remet sous tension en informant l'équipe.",
    "On attend séparation, verrouillage, vérification d'absence de tension, EPI et remise en service encadrée."),
 QT("Expliquer le rôle complémentaire de la mise à la terre et du disjoncteur différentiel.",
    "La mise à la terre offre un chemin de faible résistance au courant de défaut : elle limite la tension que peut prendre une masse métallique et permet au courant de fuite de circuler. Le disjoncteur différentiel surveille l'équilibre entre le courant aller et le courant retour ; dès qu'une partie du courant s'échappe vers la terre, généralement à travers une personne ou un isolant dégradé, il coupe en quelques millisecondes si le déséquilibre déprite le seuil, par exemple 30 mA. La terre rend le défaut détectable, le différentiel l'interrompt : aucun des deux ne remplace l'autre. La consignation reste nécessaire car ces protections ne mettent pas hors tension de façon durable.",
    "On doit montrer la complémentarité et rappeler que la protection automatique ne remplace pas la consignation.")],
C("La consignation met physiquement hors tension et verrouille la source : les protections automatiques ne la remplacent pas.",
  "Séparer + verrouiller + vérifier absence de tension",
  "Differentiel 30 mA · mise à la terre · EPI isolants",
  "Consignation~Mise hors tension~Verrouillage~Cadenas personnel~VAT~Verification absence de tension~Differentiel~Courant de fuite~Terre~Chemin du defaut",
  "Informer l'equipe|Couper et separer|Verrouiller et etiqueter|Verifier l'absence de tension|Intervenir avec EPI puis remettre en service",
  "Se fier au seul interrupteur|Ne pas tester l'appareil de mesure|Oublier les condensateurs|Remettre sous tension sans prevenir",
  "Armoire~Consignee par cadenas~VAT~Appareil teste avant et apres~EPI~Gants isolants~Differentiel~30 mA~Remise~Capots fermes",
  "Differentiel~Detecte la fuite~Disjoncteur~Coupe surcharge et court-circuit",
  "Consignation~Securite durable~Protection automatique~Securite immediate"))

# ============================================================ EL5
add("EL5", "Variateurs de vitesse et commandes de moteurs", "Maintenance électrique",
S("Un variateur de fréquence règle la vitesse d'un moteur asynchrone en modifiant la fréquence d'alimentation."
  "|Il convertit le courant alternatif réseau en courant continu, puis en alternatif de fréquence variable."
  "|Cette conversion passe par un redresseur, un circuit intermédiaire et un onduleur."
  "|La relation n = 60 f (1 - g) / p montre que la vitesse dépend de la fréquence."
  "|Le variateur permet un démarrage progressif et limite le courant de démarrage."
  "|Il peut assurer un freinage par injection continue ou par frein mécanique."
  "|Les paramètres principaux sont la fréquence maximale, la rampe d'accélération et le courant nominal moteur."
  "|Un mauvais réglage de la rampe peut provoquer un défaut de surintensité ou de surtension."
  "|Le variateur doit être refroidi : une ventilation obstruée provoque une surchauffe."
  "|Les defauts courants sont affichés sous forme de codes : surcourant, surtension, sous-tension, surchauffe."
  "|Le câblage du variateur doit respecter les recommandations du constructeur, notamment pour les câbles moteur blindés."
  "|Avant toute intervention, le circuit intermédiaire doit être déchargé et l'absence de tension vérifiée."),
[QC("Que modifie un variateur pour changer la vitesse ?", "La tension uniquement~La fréquence d'alimentation~Le nombre de pôles~La résistance du câble", 1,
     "La vitesse du moteur asynchrone dépend principalement de la fréquence."),
 QC("Quelles sont les trois parties d'un variateur ?", "Redresseur, circuit intermédiaire, onduleur~Stator, rotor, entrefer~Disjoncteur, contacteur, relais~Capteur, automate, écran", 0,
     "AC/DC puis DC/AC avec un circuit intermédiaire continu, le plus souvent."),
 QC("Quel est un avantage du démarrage par variateur ?", "Courant de démarrage limité~Vitesse maximale accrue~Suppression du glissement~Aucun refroidissement nécessaire", 0,
     "La montée en fréquence progressive évite l'appel de courant important."),
 QC("Que signifie un défaut de surcourant ?", "La tension est trop basse~Le courant dépasse la valeur admissible~La fréquence est nulle~Le moteur est à l'arrêt", 1,
     "Le variateur coupe pour se protéger et protéger le moteur."),
 QC("Pourquoi refroidir le variateur ?", "Pour augmenter la fréquence~Les composants électroniques dissipent de la chaleur~Pour réduire le bruit~Pour éviter le glissement", 1,
     "Une surchauffe réduit la durée de vie des condensateurs et de l'électronique."),
 QC("Quelle précaution avant d'intervenir sur un variateur ?", "Laisser le courant branché~Décharger le circuit intermédiaire et vérifier l'absence de tension~Retirer le refroidissement~Augmenter la fréquence", 1,
     "Les condensateurs du circuit intermédiaire restent chargés après coupure."),
 QC("Que régle-t-on généralement dans un variateur ?", "La couleur du boîtier~La rampe d'accélération et le courant nominal~Le nombre de vis~La longueur du câble", 1,
     "Ces paramètres conditionnent le démarrage et la protection du moteur."),
 QT("Un variateur affiche un défaut de surcourant au démarrage. Proposer une méthode de diagnostic.",
    "On relève d'abord le code de défaut et les conditions d'apparition : démarrage à froid, après arrêt prolongé ou sous charge. On vérifie la rampe d'accélération : si elle est trop courte, le moteur n'a pas le temps d'accélérer et le courant reste élevé, il faut l'allonger. On contrôle ensuite le réglage du courant nominal par rapport à la plaque du moteur, la tension d'alimentation, la présence d'une phase manquante et l'état du câblage moteur. On vérifie enfin que la charge n'est pas bloquée ou trop importante et que le frein est bien relâché. Après correction, on effectue un essai progressif en observant le courant affiché.",
    "On examine rampe, réglages, alimentation, câblage et charge mécanique."),
 QT("Expliquer pourquoi le variateur améliore l'efficacité énergétique d'une installation de ventilation.",
    "Dans une ventilation, le débit d'air est proportionnel à la vitesse de rotation, mais la puissance nécessaire croît approximativement comme le cube de la vitesse. Réduire le débit de 20 % par le variateur diminue donc la puissance consommée d'environ 50 %. Sans variateur, on réglerait le débit par une vanne, ce qui créerait des pertes de charge tout en gardant le moteur à pleine vitesse. Le variateur adapte la vitesse au besoin réel, réduit la consommation, diminue l'usure mécanique et supprime les chocs de démarrage. Il doit être correctement réglé et refroidi pour conserver ces bénéfices.",
    "On cite la loi cubique et on compare avec le réglage par vanne.")],
C("Le variateur pilote la vitesse par la fréquence : il épargne l'énergie mais exige réglages, refroidissement et précautions de consignation.",
  "n = 60 f (1 - g) / p",
  "Redresseur · circuit intermédiaire · onduleur",
  "Variateur~Regulation de vitesse~Redresseur~AC vers DC~Onduleur~DC vers AC~Rampe~Acceleration progressive~Surchauffe~Ventilation a verifier",
  "Relever le code defaut|Verifier réglages et plaque moteur|Contrôler alimentation et câblage|Vérifier charge et frein|Décharger et consigner avant intervention",
  "Oublier la décharge du circuit intermédiaire|Régler une rampe trop courte|Ignorer la surchauffe|Toucher aux paramètres sans relevé initial",
  "Ventilation~Débit moins 20 %~Puissance~Environ moins 50 %~Demarrage~Rampe progressive~Defaut~Surcourant~Consignation~Condensateurs decharges",
  "Sans variateur~Reglage par vanne~Avec variateur~Vitesse ajustee",
  "Surcourant~Courant trop eleve~Surtension~Tension trop eleve"))

# ============================================================ MI1
add("MI1", "GMAO : structure et exploitation des données", "Maintenance industrielle",
S("La GMAO est un logiciel de gestion de la maintenance assistée par ordinateur."
  "|Elle centralise les équipements, les interventions, les pièces et les documents."
  "|La base d'équipements décrit chaque machine, ses composants et sa localisation."
  "|Une arborescence fonctionnelle permet de descendre du site jusqu'à la pièce."
  "|Un ordre de travail porte un numéro, un libellé, une priorité et un statut."
  "|Les statuts courants sont : créé, planifié, en cours, terminé, clôturé."
  "|Le plan de maintenance génère automatiquement les ordres préventifs à échéance."
  "|L'historique des interventions constitue la mémoire technique du site."
  "|La gestion des stocks de pièces détachées est souvent intégrée à la GMAO."
  "|Les indicateurs sont calculés à partir des données saisies : fiabilité, coût, délais."
  "|La qualité des indicateurs dépend de la qualité et de la régularité des saisies."
  "|L'accès à la GMAO est nominatif afin d'assurer la traçabilité des actions."),
[QC("Que centralise une GMAO ?", "Les seuls salaires~Équipements, interventions, pièces et documents~Les seuls courriels~Le planning des vacances", 1,
     "La GMAO est la base de données technique du service maintenance."),
 QC("Que contient un ordre de travail ?", "Un numéro, un libellé, une priorité, un statut~Le prix d'achat uniquement~La couleur de la machine~Le nom du fournisseur uniquement", 0,
     "Ces champs permettent de suivre et de prioriser l'intervention."),
 QC("Quel est un statut d'ordre de travail ?", "Terminé~Brouillon personnel~Archivé sans date~Invisible", 0,
     "Le cycle comprend notamment créé, planifié, en cours, terminé, clôturé."),
 QC("Que permet l'arborescence fonctionnelle ?", "De descendre du site à la pièce~De calculer la TVA~D'envoyer des courriels~De dessiner des plans", 0,
     "Elle structure les équipements en niveaux hiérarchiques."),
 QC("D'où viennent les ordres préventifs ?", "Du hasard~Du plan de maintenance qui génère les échéances~Du client uniquement~De la paie", 1,
     "La GMAO planifie les interventions selon les périodicités définies."),
 QC("Que fournit l'historique des interventions ?", "Une mémoire technique exploitable~Une liste de prix~Un calendrier scolaire~Une photo du site", 0,
     "L'historique sert au diagnostic et aux indicateurs."),
 QC("Pourquoi la saisie doit-elle être rigoureuse ?", "Pour occuper les techniciens~Parce que les indicateurs en dépendent~Pour remplir la base~Pour éviter les réunions", 1,
     "Une donnée manquante fausse les indicateurs et les décisions."),
 QT("Expliquer le parcours d'une intervention corrective dans la GMAO, de la demande à la clôture.",
    "La demande est enregistrée avec le symptôme, l'équipement concerné, la date et la personne qui signale. Le responsable crée un ordre de travail, lui attribue une priorité selon la criticité et le planifie avec les compétences et les pièces nécessaires. Le technicien prend l'ordre, consulte l'historique et les documents, puis réalise l'intervention en renseignant les mesures, les pièces consommées et le temps passé. Il indique la cause du défaut et l'action effectuée. Le responsable vérifie le compte rendu, contrôle l'essai et clôture l'ordre. Les données alimentent ensuite l'historique et les indicateurs de fiabilité.",
    "On attend les étapes : demande, ordre, planification, exécution, compte rendu, clôture et indicateurs."),
 QT("Une GMAO affiche des indicateurs de fiabilité embellissants. Quelles causes possibles et quelles corrections ?",
    "Des indicateurs trop favorables peuvent provenir de temps d'arrêt non saisis, d'ordres clôturés sans date de fin réelle, de défaillances classées à tort en préventif ou de périodes sans données. On vérifie d'abord la complétude des champs obligatoires et la cohérence des dates, puis on compare les données GMAO aux rapports de production et aux bons de intervention. On forme les utilisateurs à saisir chaque arrêt et chaque cause, on met en place des contrôles automatiques de cohérence, puis on recalcule les indicateurs sur une période fiable. Une donnée non saisie n'est pas une donnée favorable : elle rend le pilotage aveugle.",
    "On identifie des causes de saisie et de classement, puis on propose formation, contrôles et recalcul.")],
C("La GMAO est la mémoire technique du service : sa valeur dépend de la qualité des saisies et de la disponibilité des documents.",
  "Équipement + ordre de travail + historique + indicateurs",
  "Statuts : créé · planifié · en cours · terminé · clôturé",
  "GMAO~Base de maintenance~Ordre de travail~Unite d'action~Statut~Avancement~Arborescence~Structure fonctionnelle~Historique~Memoire technique~Indicateur~Donnee calculee",
  "Créer la demande|Qualifier et prioriser l'ordre|Planifier moyens et pièces|Réaliser et saisir les résultats|Clôturer et exploiter les indicateurs",
  "Clôturer sans compte rendu|Oublier la cause du défaut|Saisir des dates approximatives|Laisser des champs obligatoires vides",
  "Ordre 214~Priorite forte~Statut~En cours~Pieces~Roulement et joint~Temps~2 h 30~Cloture~Apres essai en charge",
  "Donnee saisie~Information disponible~Donnee manquante~Indicateur fausse",
  "Corrective~Apres defaut~Preventive~Selon plan"))

# ============================================================ MI2
add("MI2", "Indicateurs de maintenance : MTBF, MTTR et disponibilité", "Maintenance industrielle",
S("Un indicateur transforme des données en information décisionnelle."
  "|Le MTBF est le temps moyen de bon fonctionnement entre deux pannes."
  "|Le MTTR est le temps moyen de réparation, depuis l'arrêt jusqu'à la remise en service."
  "|Le MTBF se calcule en divisant le temps de fonctionnement total par le nombre de pannes."
  "|Le MTTR se calcule en divisant la somme des durées d'intervention par le nombre d'interventions."
  "|La disponibilité intrinsèque vaut MTBF / (MTBF + MTTR)."
  "|Une disponibilité de 95 % signifie que l'équipement est opérationnel 95 % du temps considéré."
  "|La fiabilité est la probabilité de fonctionner sans défaillance pendant une durée donnée."
  "|La maintenabilité mesure la facilité et la rapidité de remise en état."
  "|Le taux de panne est l'inverse du MTBF pour un composant à taux constant."
  "|Les indicateurs doivent être calculés sur une période et un périmètre définis."
  "|Les indicateurs servent à piloter, pas à rechercher un coupable."),
[QC("Que mesure le MTBF ?", "La durée d'une intervention~Le temps moyen entre deux pannes~Le coût des pièces~Le nombre de techniciens", 1,
     "MTBF signifie Mean Time Between Failures."),
 QC("Comment calculer le MTTR ?", "Temps de fonctionnement / nombre de pannes~Durée totale des réparations / nombre d'interventions~Nombre de pannes / temps total~Prix / durée", 1,
     "Le MTTR est une moyenne des durées de remise en état."),
 QC("Une machine a un MTBF de 190 h et un MTTR de 10 h. Quelle est sa disponibilité ?", "90 %~95 %~99 %~10 %", 1,
     "190 / (190 + 10) = 0,95, soit 95 %."),
 QC("Que mesure la maintenabilité ?", "La solidité de la machine~La facilité et la rapidité de réparation~La consommation d'énergie~Le nombre de capteurs", 1,
     "Une bonne maintenabilité réduit le MTTR."),
 QC("Quel est le taux de panne si le MTBF vaut 100 h ?", "0,01 par heure~100 par heure~1 par heure~10 par heure", 0,
     "Le taux est l'inverse du MTBF : 1/100 = 0,01 h⁻¹."),
 QC("Que faut-il préciser avec un indicateur ?", "La marque du logiciel~La période et le périmètre de calcul~Le nom du responsable~La couleur du graphique", 1,
     "Sans période ni périmètre, l'indicateur n'est pas interprétable."),
 QC("À quoi servent les indicateurs ?", "À punir les équipes~À piloter et à orienter les actions~À remplacer le diagnostic~À supprimer la maintenance", 1,
     "Ce sont des outils de décision, non de culpabilisation."),
 QT("Un equipement a fonctionné 1900 h sur une periode et subi 10 pannes, avec une duree totale de reparation de 100 h. Calculer MTBF, MTTR et disponibilite.",
    "MTBF = temps de fonctionnement / nombre de pannes = 1900 / 10 = 190 h. MTTR = durée totale des réparations / nombre d'interventions = 100 / 10 = 10 h. Disponibilité = MTBF / (MTBF + MTTR) = 190 / 200 = 0,95, soit 95 %. On peut également la calculer par 1900 / (1900 + 100) = 0,95. Ces valeurs signifient qu'en moyenne l'équipement tourne 190 h avant de tomber en panne et qu'il faut 10 h pour le rétablir.",
    "On attend les trois calculs avec leurs formules et leur interprétation."),
 QT("Un service voit son MTTR augmenter alors que le MTBF est stable. Que cela indique-t-il et quelles actions mener ?",
    "Un MTTR qui augmente à MTBF constant signifie que les pannes sont aussi fréquentes mais qu'on met plus de temps à réparer. Cela peut venir d'un manque de pièces détachées, d'une formation insuffisante, de documents techniques obsolètes, d'un diagnostic lent ou d'une difficulté croissante d'accès aux organes. On analyse la répartition du temps entre attente de pièce, diagnostic, réparation et essai. On agit ensuite sur le stock de pièces critiques, la formation des techniciens, la mise à jour des schémas et l'amélioration de l'accessibilité. On suit l'évolution du MTTR après les actions pour vérifier leur efficacité.",
    "On interprète l'écart entre les deux indicateurs et on propose des actions ciblées sur la réparation.")],
C("MTBF et MTTR résument fiabilité et maintenabilité : leur combinaison donne la disponibilité, indicateur de pilotage.",
  "MTBF = temps de marche / nombre de pannes · MTTR = durée des réparations / nombre d'interventions",
  "Disponibilité = MTBF / (MTBF + MTTR)",
  "MTBF~Temps entre pannes~MTTR~Temps de reparation~Disponibilite~Capacite a fonctionner~Fiabilite~Probabilite sans panne~Maintenabilite~Facilite de reparation",
  "Définir période et périmètre|Extraire les données de la GMAO|Calculer MTBF et MTTR|Calculer la disponibilité|Interpréter et décider d'actions",
  "Comparer des périodes différentes|Confondre MTBF et MTTR|Oublier les arrêts non enregistrés|Utiliser les indicateurs pour culpabiliser",
  "1900 h~Temps de fonctionnement~10 pannes~Evenements~MTBF~190 h~MTTR~10 h~Disponibilite~95 %",
  "Fiabilite~Moins de pannes~Maintenabilite~Reparer plus vite",
  "MTBF~Temps de bon fonctionnement~MTTR~Temps de remise en etat"))

# ============================================================ MI3
add("MI3", "Analyse de risques : criticité et méthode FMEA", "Maintenance industrielle",
S("Une analyse de risques identifie les défaillances possibles et leurs conséquences."
  "|La FMEA est une méthode d'analyse des modes de défaillance, de leurs effets et de leur criticité."
  "|Un mode de défaillance est la manière dont un composant ne remplit plus sa fonction."
  "|L'effet est la conséquence observée sur l'équipement, la production ou la sécurité."
  "|La gravité note la sévérité de l'effet, généralement de 1 à 10."
  "|L'occurrence note la fréquence de la cause, généralement de 1 à 10."
  "|La détectabilité note la difficulté à repérer la défaillance avant son effet, de 1 à 10."
  "|L'indice de criticité est le produit gravité fois occurrence fois détectabilité."
  "|Une criticité élevée impose une action de prévention ou de protection."
  "|Les actions possibles sont la prévention, la détection et la réduction de gravité."
  "|L'analyse est collective : elle associe maintenance, production, qualité et sécurité."
  "|Le classement des équipements par criticité permet de prioriser les efforts de maintenance."),
[QC("Que signifie FMEA ?", "Analyse des modes de défaillance, de leurs effets et de leur criticité~Formation de maintenance et d'exploitation~France Maintenance Entreprise Associée~Contrôle de la qualité de l'air", 0,
     "Failure Modes and Effects Analysis, traduit par analyse des modes de défaillance et de leurs effets."),
 QC("Que note la gravité ?", "La fréquence de la panne~La sévérité de l'effet~La difficulté de détection~Le coût de la pièce", 1,
     "La gravité évalue la conséquence, indépendamment de la fréquence."),
 QC("Comment calculer l'indice de criticité ?", "G + O + D~G x O x D~G / O~O - D", 1,
     "Les trois notes sont multipliées ; l'indice varie de 1 à 1000."),
 QC("Que représente l'occurrence ?", "La probabilité de détecter~La fréquence de la cause~La gravité~La durée de réparation", 1,
     "L'occurrence note la fréquence à laquelle la cause se produit."),
 QC("Une criticité élevée impose...", "De ne rien faire~Une action de prévention ou de protection~Attendre la panne~Une augmentation de production", 1,
     "L'objectif est de réduire au moins un des trois facteurs."),
 QC("Qui doit participer à une FMEA ?", "Le seul responsable maintenance~Plusieurs métiers : maintenance, production, qualité, sécurité~Le client uniquement~Personne", 1,
     "Le regard croisé améliore l'identification des modes de défaillance."),
 QC("Quand revoir une FMEA ?", "Jamais~Après modification ou retour d'expérience important~Tous les dix ans~Uniquement en cas d'audit", 1,
     "C'est un document vivant, mis à jour quand le système change."),
 QT("Une pompe alimente un circuit de refroidissement critique. Appliquer une FMEA simplifiée à la défaillance 'perte de débit'.",
    "Mode de défaillance : perte de débit par cavitation ou obstruction. Effet : montée en température du procédé, arrêt de production et risque pour la sécurité. Gravité notée 9 sur 10. Cause probable : crépine colmatée ou niveau d'alimentation trop bas, occurrence notée 4. Détectabilité : une alarme de débit existe mais le capteur est rarement testé, note 5. Criticité = 9 x 4 x 5 = 180, ce qui justifie une action. Actions : installer un capteur de débit avec alarme testée mensuellement (détectabilité réduite à 2), nettoyer la crépine selon une périodicité définie (occurrence réduite à 2) et prévoir une pompe de secours (gravité réduite à 5). Nouvelle criticité : 5 x 2 x 2 = 20.",
    "On attend identification du mode, de l'effet, des trois notes, le calcul et des actions de réduction."),
 QT("Expliquer la différence entre prévention, détection et réduction de gravité dans une FMEA.",
    "La prévention agit sur l'occurrence : lubrifier, remplacer à échéance ou former réduit la probabilité que la cause apparaisse. La détection agit sur la note de détectabilité : capteurs, alarmes, contrôles visuels et tests périodiques permettent de repérer la dérive avant la conséquence. La réduction de gravité agit sur l'effet : redondance, pompe de secours, protection mécanique ou arrêt d'urgence limitent les dommages quand la panne survient. Une bonne stratégie combine les trois leviers, car aucun n'est suffisant seul : la détection ne supprime pas la panne et la prévention ne protège pas contre un événement imprévu.",
    "On définit les trois leviers et on montre leur complémentarité.")],
C("La FMEA hiérarchise les risques par gravité, occurrence et détectabilité : on agit là où le produit est le plus élevé.",
  " Criticité = G x O x D (de 1 à 1000)",
  "Prévention : réduire l'occurrence · détection améliore la détectabilité · redondance réduit la gravité",
  "FMEA~Analyse des modes de defaillance~Gravite~Severite de l'effet~Occurrence~Frequence de la cause~Detectabilite~Capacite a reperer~Criticite~Produit G O D",
  "Décrire la fonction et le système|Identifier les modes de défaillance|Noter gravité, occurrence, détectabilité|Calculer la criticité et classer|Proposer des actions et réévaluer",
  "Confondre gravité et occurrence|Oublier la détectabilité|Travailler seul sans production ni sécurité|Ne jamais réévaluer après action",
  "Pompe~Perte de debit~Notes~9, 4, 5~Criticite~180~Actions~Capteur et nettoyage~Nouvelle criticite~20",
  "Prevention~Moins de causes~Detection~Repérer plus tot",
  "Gravite~Consequence~Occurrence~Frequence"))

# ============================================================ MI4
add("MI4", "Maintenance prédictive et capteurs connectés", "Maintenance industrielle",
S("La maintenance prédictive estime l'état futur d'un équipement à partir de données mesurées."
  "|Elle va plus loin que la maintenance conditionnelle en anticipant la date de défaillance."
  "|Les données proviennent de capteurs : vibrations, température, pression, courant, humidité d'huile."
  "|Un capteur transforme une grandeur physique en signal électrique exploitable."
  "|L'acquisition numérique convertit le signal analogique en valeurs discrètes."
  "|La fréquence d'échantillonnage doit être suffisante pour ne pas perdre d'information."
  "|Le traitement du signal extrait des indicateurs : valeur efficace, pic, tendance, spectre."
  "|Une tendance divergente déclenche une alerte avant le seuil de panne."
  "|L'IoT industriel connecte les capteurs à une plateforme d'analyse via un réseau filaire ou sans fil."
  "|Les données sont historisées et corrélées avec les interventions de la GMAO."
  "|Un faux positif provoque une intervention inutile, un faux négatif une panne non évitée."
  "|La cybersécurité des équipements connectés doit être prise en compte dès la conception."),
[QC("Quelle est la différence entre conditionnel et prédictif ?", "Aucune~Le prédictif anticipe l'évolution future~Le conditionnel ne mesure rien~Le prédictif n'utilise pas de capteurs", 1,
     "Le prédictif exploite l'historique pour estimer une date de défaillance."),
 QC("Que fait un capteur ?", "Il refroidit la machine~Il transforme une grandeur physique en signal~Il remplace la GMAO~Il augmente la vitesse", 1,
     "Un capteur assure la mesure et la conversion du signal."),
 QC("Quel risque avec une fréquence d'échantillonnage trop faible ?", "Une perte d'information du signal~Une meilleure précision~Un coût plus élevé~Aucun effet", 0,
     "Le théorème de Shannon impose au moins deux fois la fréquence maximale utile."),
 QC("Quel indicateur extrait-on d'un signal de vibration ?", "La couleur~La valeur efficace et le spectre~Le prix~Le numéro de série", 1,
     "Valeur efficace et analyse spectrale sont les traitements courants."),
 QC("Que déclenche une tendance divergente ?", "Une alerte avant le seuil de panne~Une augmentation de production~La suppression des capteurs~Rien", 0,
     "L'alerte permet de programmer l'intervention à temps."),
 QC("Qu'est-ce qu'un faux positif ?", "Une panne non détectée~Une alerte sans défaillance réelle~Une mesure exacte~Un capteur absent", 1,
     "Le faux positif entraîne une intervention inutile."),
 QC("Pourquoi sécuriser les équipements connectés ?", "Pour augmenter la consommation~Parce qu'ils sont exposés à des accès non autorisés~Pour changer leur couleur~Pour supprimer les données", 1,
     "Un capteur connecté peut devenir un point d'entrée dans le réseau."),
 QT("Décrire la chaîne de traitement d'une donnée de vibration jusqu'à la décision de maintenance.",
    "Le capteur accéléromètre convertit l'accélération mécanique en signal analogique. Ce signal est conditionné, puis converti par un convertisseur analogique-numérique à une fréquence d'échantillonnage adaptée à la bande de fréquence utile. Le système calcule des indicateurs comme la valeur efficace en mm/s et réalise une analyse spectrale. Ces valeurs sont comparées à des seuils d'alerte et à l'historique de la machine. Si la tendance augmente de façon significative, une alerte est créée dans la GMAO avec le relevé et le spectre. Le responsable maintenance planifie alors une intervention conditionnelle avant la rupture, puis confirme ou infirme le diagnostic lors du contrôle.",
    "On attend capteur, conversion, traitement, comparaison, alerte et décision."),
 QT("Un capteur de température connecté génère de nombreuses fausses alertes. Comment améliorer le système ?",
    "On vérifie d'abord le positionnement du capteur et sa fixation, car un contact médiocre donne des mesures erratiques. On contrôle l'étalonnage et la plage de mesure, puis on examine les conditions environnementales : courant d'air, ensoleillement ou vibration du support. On analyse les données historiques pour distinguer les variations normales liées à la charge des véritables dérives. On remplace un seuil fixe par une alerte sur la tendance ou par un seuil dépendant de la charge de la machine. On filtre les données, on augmente la fréquence de mesure si nécessaire et on teste le nouveau réglage avant déploiement. Enfin, on documente la modification et on surveille le taux de fausses alertes.",
    "On agit sur le capteur, l'environnement, le traitement du signal et le réglage de l'alerte.")],
C("La maintenance prédictive transforme des mesures en tendances : capteur, acquisition, traitement, alerte, décision.",
  "Grandeur physique → signal → donnée → indicateur → alerte",
  "Fréquence d'échantillonnage ≥ 2 x fréquence maximale utile",
  "Capteur~Conversion du signal~Echantillonnage~Conversion analogique numerique~Tendance~Evolution dans le temps~Alerte~Signal avant panne~IoT~Capteurs connectes~Faux positif~Alerte injustifiee",
  "Choisir la grandeur à surveiller|Installer et étalonner le capteur|Acquérir et traiter le signal|Comparer aux seuils et tendances|Décider et tracer l'action",
  "Sous-estimer la fréquence d'échantillonnage|Ignorer la dérive du capteur|Confondre seuil et tendance|Négliger la cybersécurité",
  "Accelerometre~Signal analogique~Conversion~Valeurs numeriques~Valeur efficace~mm/s~Tendance~Hausse progressive~Alerte~Ordre GMAO",
  "Conditionnel~Etat present~Predictif~Etat futur estime",
  "Faux positif~Intervention inutile~Faux negatif~Panne non evitee"))

# ============================================================ MI5
add("MI5", "Amélioration continue et retour d'expérience en maintenance", "Maintenance industrielle",
S("L'amélioration continue vise à réduire durablement les pertes et les défauts."
  "|Le cycle PDCA organise la démarche : Plan, Do, Check, Act."
  "|Plan consiste à analyser la situation et à définir les objectifs."
  "|Do correspond à la mise en œuvre des actions choisies."
  "|Check vérifie les résultats avec des indicateurs."
  "|Act capitalise et ajuste la démarche pour le cycle suivant."
  "|Le retour d'expérience est l'analyse structurée des événements passés."
  "|Un arbre des causes ou la méthode des 5 Pourquoi aide à identifier les causes racines."
  "|Les actions correctives suppriment une cause existante, les actions préventives évitent qu'elle apparaisse."
  "|La démarche 5S améliore l'ordre, la propreté et l'efficacité du poste de travail."
  "|Les cercles de qualité associent les opérateurs à la recherche d'améliorations."
  "|Une action n'est terminée que si son efficacité a été vérifiée par des données."),
[QC("Que signifie PDCA ?", "Plan, Do, Check, Act~Production, Distribution, Contrôle, Achat~Préventif, Défaut, Correctif, Audit~Plan, Durée, Coût, Arrêt", 0,
     "Le cycle Plan, Do, Check, Act structure l'amélioration continue."),
 QC("Quelle phase vérifie les résultats ?", "Plan~Do~Check~Act", 2,
     "Check compare les indicateurs avant et après l'action."),
 QC("Quelle est la différence entre action corrective et préventive ?", "Aucune~La corrective traite une cause existante, la préventive empêche son apparition~La préventive est toujours moins chère~La corrective n'est jamais documentée", 1,
     "Les deux visent des causes, mais à des moments différents du cycle."),
 QC("Que vise la démarche 5S ?", "Augmenter le nombre de pannes~Ordre, propreté et efficacité du poste~Supprimer les indicateurs~Réduire la formation", 1,
     "Les 5S sont : débarrasser, ranger, nettoyer, standardiser, maintenir."),
 QC("Quel est l'intérêt du retour d'expérience ?", "Raconter des anecdotes~Capitaliser sur les événements pour éviter la répétition~Remplacer la GMAO~Augmenter les stocks", 1,
     "Il transforme un incident en connaissance partagée."),
 QC("Quand une action est-elle réellement terminée ?", "Quand elle est décidée~Quand son efficacité est vérifiée par des données~Quand elle est écrite~Quand le réunion est finie", 1,
     "La vérification est indispensable avant clôture."),
 QC("Qui peut proposer des améliorations ?", "Les seuls ingénieurs~Tous les acteurs, notamment les opérateurs~Le client uniquement~Personne", 1,
     "Les cercles de qualité valorisent l'expérience de terrain."),
 QT("Décrire l'application du cycle PDCA à la réduction des pannes d'un convoyeur.",
    "Plan : on analyse les douze derniers mois, on relève les pannes de courroie et on fixe un objectif de réduction de 30 % du nombre d'arrêts. On identifie par un arbre des causes une tension mal contrôlée lors du remplacement. Do : on rédige une procédure de tension avec une valeur et un outil de mesure, on forme les techniciens et on met à jour la GMAO. Check : après trois mois, on compare le nombre de pannes et le MTBF avec la période de référence, en vérifiant que la charge de production est comparable. Act : si l'objectif est atteint, on généralise la procédure aux autres convoyeurs ; sinon, on cherche une cause complémentaire et on relance un cycle.",
    "On attend une étape par lettre du cycle, un objectif chiffré et une vérification."),
 QT("Pourquoi une action corrective doit-elle être suivie d'une vérification d'efficacité ?",
    "Une action peut être bien intentionnée et pourtant ne pas traiter la vraie cause, ou être appliquée de façon incomplète. Sans mesure après l'action, on ne sait pas si la situation s'est améliorée, si elle est stable ou si elle s'est dégradée. La vérification compare les indicateurs avant et après sur une période suffisante et dans des conditions comparables : nombre de pannes, MTBF, taux de rebut ou temps d'intervention. Elle permet de décider de généraliser la solution, de l'ajuster ou de la abandonner. C'est cette boucle de retour qui distingue l'amélioration continue d'une simple succession d'improvisations.",
    "On insiste sur la preuve par les données et la décision qui en découle.")],
C("L'amélioration continue est une boucle : on planifie, on agit, on vérifie par les données puis on capitalise.",
  "PDCA : Plan · Do · Check · Act",
  "Correctif : traite la cause · préventif : empêche la cause",
  "PDCA~Cycle d'amelioration~Retour d'experience~Analyse du passe~Cause racine~Origine du defaut~5S~Ordre et propreté~Indicateur~Preuve d'efficacite~Capitalisation~Document mis a jour",
  "Analyser les données et fixer un objectif|Identifier la cause racine|Mettre en œuvre l'action|Vérifier les indicateurs|Capitaliser et relancer le cycle",
  "Clôturer une action sans mesure|Confondre correctif et préventif|Generaliser sans vérification|Ignorer l'avis des opérateurs",
  "Convoyeur~12 pannes par an~Objectif~Moins 30 %~Action~Procedure de tension~Controle~MTBF apres 3 mois~Decision~Generaliser",
  "Corrective~Cause existante~Preventive~Cause avoidée",
  "Check~Mesure des resultats~Act~Capitalisation"))

# ============================================================ PA1
add("PA1", "Mécanique des fluides et circuits hydrauliques", "Physique appliquée",
S("Un fluide est un milieu qui se déforme sous l'action d'une force : liquide ou gaz."
  "|La masse volumique rapporte la masse au volume, en kg/m³."
  "|La pression est la force exercée par unité de surface, en pascals."
  "|La pression absolue vaut la pression relative plus la pression atmosphérique."
  "|Dans un liquide au repos, la pression augmente avec la profondeur selon p = rho g h."
  "|Le principe de Pascal énonce qu'une pression appliquée à un fluide incompressible se transmet intégralement."
  "|Le débit volumique Q est le volume écoulé par unité de temps, en m³/s ou L/min."
  "|En régime permanent dans une conduite, le débit est constant : S v = constante."
  "|La perte de charge traduit la dissipation d'énergie due aux frottements et aux singularités."
  "|Une pompe fournit une élévation de pression, exprimée par sa courbe débit-pression."
  "|Le point de fonctionnement est l'intersection de la courbe pompe et de la courbe réseau."
  "|La cavitation apparaît quand la pression absolue tombe au-dessus de la tension de vapeur du liquide."),
[QC("Quelle est l'unité de pression ?", "Le newton~Le pascal~Le joule~Le litre", 1,
     "Un pascal correspond à un newton par mètre carré."),
 QC("Comment évolue la pression dans un liquide au repos ?", "Elle diminue avec la profondeur~Elle augmente avec la profondeur~Elle reste nulle~Elle dépend de la couleur", 1,
     "p = rho g h : la pression croît linéairement avec la profondeur."),
 QC("Que énonce le principe de Pascal ?", "Une pression se transmet intégralement dans un fluide incompressible~Le débit est constant~La chaleur se dilate~Le gaz est incompressible", 0,
     "C'est le fondement des vérins et des presses hydrauliques."),
 QC("Quelle est la relation de continuité ?", "S v = constante~P V = constante~U = R I~F = m a", 0,
     "Le débit Q = S v reste constant en régime permanent."),
 QC("Qu'est-ce qu'une perte de charge ?", "Une augmentation de débit~Une dissipation d'énergie par frottement~Une hausse de pression~Un type de pompe", 1,
     "Les pertes dépendent de la longueur, du diamètre et des accessoires."),
 QC("Comment obtenir le point de fonctionnement d'une pompe ?", "En croisant courbe pompe et courbe réseau~En lisant la plaque~En divisant par deux~En mesurant la température", 0,
     "L'intersection donne le débit et la pression réels."),
 QC("Quelle cause provoque une cavitation ?", "Une pression absolue trop basse~Une pression trop élevée~Un débit nul~Une température basse", 0,
     "Si la pression passe sous la tension de vapeur, des bulles se forment puis implosent."),
 QT("Une conduite de section 20 cm² transporte un débit de 12 L/min. Calculer la vitesse moyenne du fluide.",
    "Le débit vaut 12 L/min, soit 12 x 10⁻³ m³ / 60 s = 2 x 10⁻⁴ m³/s. La section vaut 20 cm², soit 20 x 10⁻⁴ m² = 2 x 10⁻³ m². La vitesse moyenne est v = Q / S = 2 x 10⁻⁴ / 2 x 10⁻³ = 0,1 m/s. On vérifie l'ordre de grandeur : un faible débit dans une section relativement large donne une vitesse modérée, cohérente avec un écoulement calme.",
    "On convertit d'abord débit et section en unités SI, puis on applique v = Q/S."),
 QT("Expliquer le phénomène de cavitation dans une pompe et ses conséquences.",
    "À l'aspiration, la pression absolue peut tomber sous la tension de vapeur du liquide, surtout si la hauteur d'aspiration est trop grande, si la température est élevée ou si la crépine est colmatée. Des bulles de vapeur se forment puis implosent brutalement lorsque la pression remonte dans la roue. Ces implosions provoquent des chocs microscopiques qui érodent la roue, du bruit, des vibrations et une chute de débit. On prévient la cavitation en réduisant la hauteur d'aspiration, en nettoyant la crépine, en augmentant la pression d'entrée ou en choisissant une pompe adaptée au NPSH disponible.",
    "On décrit la formation des bulles, leur implosion et les moyens de prévention.")],
C("Dans un circuit hydraulique, pression, débit et pertes de charge déterminent le point de fonctionnement et les risques de cavitation.",
  "p = rho g h · Q = S v · 1 bar = 10⁵ Pa",
  "Pascal : pression transmise intégralement",
  "Pression~Force par surface~Debit~Volume par temps~Perte de charge~Dissipation d'energie~Pascal~Transmission de pression~Cavitation~Bulles et erosion~Pompe~Elevation de pression",
  "Convertir les grandeurs en unités SI|Calculer débit, vitesse et pression|Tracer ou lire les courbes|Vérifier la pression d'aspiration|Vérifier les pertes et la cavitation",
  "Confondre pression relative et absolue|Oublier la conversion L/min en m³/s|Ignorer les pertes de charge|Négliger la cavitation",
  "Conduite~20 cm² et 12 L/min~Vitesse~0,1 m/s~Pression~1 bar = 10⁵ Pa~Cavitation~Bruit et erosion~Pompe~Courbe debit-pression",
  "Pression relative~Par rapport a l'atmosphere~Pression absolue~Relative plus atmospherique",
  "Cavitation~Pression trop basse~Surcharge~Pression trop haute"))

# ============================================================ PA2
add("PA2", "Thermodynamique appliquée aux équipements", "Physique appliquée",
S("La thermodynamique étudie les transformations de l'énergie thermique et mécanique."
  "|Un système échange de la chaleur et du travail avec son environnement."
  "|Le premier principe énonce la conservation de l'énergie : delta U = W + Q."
  "|Le travail reçu par un système et la chaleur reçue augmentent son énergie interne."
  "|La chaleur est un transfert lié à une différence de température."
  "|Le travail est un transfert lié à une force et à un déplacement."
  "|Une transformation isotherme se fait à température constante."
  "|Une transformation adiabatique se fait sans échange de chaleur."
  "|Le rendement d'une machine thermique est le rapport entre travail utile et chaleur fournie."
  "|Le second principe interdit de convertir intégralement la chaleur en travail."
  "|Un compresseur augmente la pression d'un gaz au prix d'un apport de travail."
  "|Le refroidissement d'un compresseur limite la montée en température et améliore son rendement."),
[QC("Que traduit le premier principe ?", "La conservation de l'énergie~La augmentation du désordre~La loi d'Ohm~La proportionnalité", 0,
     "delta U = W + Q : l'énergie du système varie selon les échanges."),
 QC("Qu'est-ce qu'une transformation adiabatique ?", "A température constante~Sans échange de chaleur~Sans travail~À pression constante", 1,
     "Adiabatique signifie Q = 0."),
 QC("Comment définir le rendement thermique ?", "Chaleur fournie / travail utile~Travail utile / chaleur fournie~Température / pression~Volume / masse", 1,
     "Le rendement rapporte ce que l'on obtient à ce que l'on consomme."),
 QC("Que fait un compresseur ?", "Il détend un gaz~Il augmente la pression d'un gaz~Il refroidit un liquide~Il mesure la température", 1,
     "La compression demande un apport de travail."),
 QC("Que dit le second principe ?", "Toute la chaleur peut devenir du travail~On ne peut pas convertir toute la chaleur en travail~L'énergie se crée~La température est constante", 1,
     "Une partie de la chaleur doit être rejetée à une température plus basse."),
 QC("Quelle est l'unité de la chaleur ?", "Le watt~Le joule~Le newton~Le pascal", 1,
     "Chaleur, travail et énergie s'expriment en joules."),
 QC("Pourquoi refroidir un compresseur ?", "Pour augmenter la pression~Pour limiter la température et améliorer le rendement~Pour réduire le bruit~Pour supprimer la lubrification", 1,
     "Une compression trop chaude dégrade le rendement et les lubrifiants."),
 QT("Une machine thermique reçoit 500 kJ de chaleur et fournit 180 kJ de travail utile. Calculer son rendement et la chaleur rejetée.",
    "Le rendement vaut travail utile / chaleur fournie = 180 / 500 = 0,36, soit 36 %. Par conservation de l'énergie, la chaleur rejetée à l'environnement vaut 500 - 180 = 320 kJ. On vérifie que le rendement est bien inférieur à 1, conformément au second principe : une machine thermique ne peut pas convertir toute la chaleur reçue en travail.",
    "On calcule le rendement puis la chaleur évacuée par bilan d'énergie."),
 QT("Expliquer pourquoi la température d'un compresseur augmente et quelles conséquences cela a sur la maintenance.",
    "Lors de la compression, le travail fourni à la gaz augmente son énergie interne : la température monte, notamment si la compression est rapide et proche d'une transformation adiabatique. Une température élevée réduit le rendement, dilue l'huile lubrifiante, accélère le vieillissement des joints et peut provoquer des dépôts de carbone. La maintenance doit donc vérifier la ventilation, le niveau et la qualité d'huile, le colmatage du filtre d'admission et l'état des ailettes de refroidissement. Une sonde de température et une alerte permettent de détecter une dérive avant la panne.",
    "On relie travail, énergie interne, température, puis conséquences et actions de maintenance.")],
C("Les principes de la thermodynamique expliquent rendement, échauffement et efforts sur les machines thermiques.",
  "delta U = W + Q · rendement = travail utile / chaleur fournie",
  "Adiabatique : Q = 0 · isotherme : T constante",
  "Premier principe~Conservation de l'energie~Chaleur~Transfert thermique~Travail~Force fois deplacement~Rendement~Utile sur fourni~Adiabatique~Sans echange de chaleur~Compresseur~Augmente la pression",
  "Délimiter le système|Identifier les échanges de chaleur et de travail|Appliquer le bilan d'énergie|Calculer le rendement|Vérifier températures et refroidissement",
  "Confondre chaleur et température|Oublier la chaleur rejetée|Croire à un rendement supérieur à 1|Négliger l'effet de la température sur l'huile",
  "Machine~500 kJ recus~Travail~180 kJ utiles~Rendement~36 %~Rejet~320 kJ~Compresseur~Temperature surveillee",
  "Chaleur~Transfert d'energie~Travail~Transfert mecanique",
  "Isotherme~Temperature constante~Adiabatique~Pas de chaleur echangee"))

# ============================================================ PA3
add("PA3", "Électricité appliquée : moteurs et rendement énergétique", "Physique appliquée",
S("L'énergie électrique consommée par un moteur se transforme en énergie mécanique et en pertes."
  "|La puissance électrique active absorbée vaut P = U I cos phi en monophasé."
  "|En triphasé, la puissance active vaut P = racine(3) U I cos phi."
  "|Le facteur de puissance cos phi traduit le décalage entre tension et courant."
  "|Une charge inductive comme un moteur absorbe de l'énergie réactive."
  "|L'énergie réactive ne produit pas de travail mais charge le réseau et les câbles."
  "|La puissance mécanique utile est liée au couple et à la vitesse de rotation."
  "|Le rendement global rapporte la puissance mécanique utile à la puissance électrique absorbée."
  "|Les pertes comprennent les pertes cuivre, fer, mécaniques et les frottements."
  "|Un moteur sous-chargé a souvent un rendement et un facteur de puissance dégradés."
  "|La compensation par condensateurs améliore le facteur de puissance."
  "|Le suivi de la consommation permet de détecter une dérive de rendement."),
[QC("Que vaut la puissance active en triphasé ?", "U I cos phi~racine(3) U I cos phi~3 U I~U / I", 1,
     "Le facteur racine de 3 provient de la relation entre tension entre phases et tension de phase."),
 QC("Que représente cos phi ?", "Le rendement~Le facteur de puissance~La vitesse~Le glissement", 1,
     "cos phi est le rapport entre puissance active et puissance apparente."),
 QC("Quelle énergie ne produit pas de travail utile ?", "L'énergie active~L'énergie réactive~L'énergie mécanique~Le travail", 1,
     "L'énergie réactive circule mais ne fournit pas de travail."),
 QC("Que rapporte le rendement global ?", "Puissance utile / puissance absorbée~Puissance absorbée / puissance utile~Tension / courant~Couple / vitesse", 0,
     "C'est toujours sortie divisée par entrée."),
 QC("Quel est un effet d'un moteur sous-chargé ?", "Un meilleur rendement~Un rendement et un cos phi dégradés~Une baisse du bruit~Une tension plus élevée", 1,
     "Les pertes fixes deviennent proportionnellement plus importantes."),
 QC("Comment améliorer le facteur de puissance ?", "En ajoutant des condensateurs~En augmentant la charge mécanique uniquement~En réduisant la tension~En changeant de fréquence", 0,
     "Les condensateurs fournissent localement l'énergie réactive nécessaire."),
 QC("Que signifie la classe IE3 ?", "Une classe d'efficacité énergétique~Un type de roulement~Une tension de 3 kV~Une vitesse de 3000 tr/min", 0,
     "Les classes IE normalisent le rendement minimal des moteurs."),
 QT("Un moteur triphasé 400 V absorbe 10 A avec un facteur de puissance de 0,85 et fournit 5,2 kW mécaniques. Calculer la puissance absorbée et le rendement.",
    "P.absorbée = racine(3) x 400 x 10 x 0,85 = 1,732 x 400 x 10 x 0,85, soit environ 5 889 W, donc 5,89 kW. Le rendement vaut P utile / P absorbée = 5,2 / 5,89 = 0,883, soit environ 88 %. Cette valeur est cohérente pour un moteur asynchrone de cette puissance. Les pertes représentent environ 0,69 kW, dissipés surtout en chaleur.",
    "On applique la formule triphasée puis le rapport sortie sur entrée."),
 QT("Expliquer pourquoi un moteur sous-chargé consomme proportionnellement plus qu'un moteur bien dimensionné.",
    "Un moteur présente des pertes fixes, notamment les pertes fer et les frottements, qui existent dès qu'il tourne, et des pertes variables liées au courant, comme les pertes cuivre. À faible charge, la puissance utile diminue alors que les pertes fixes restent presque constantes : le rendement baisse mécaniquement. Le facteur de puissance se dégrade également car la part de courant de magnétisation devient prépondérante. Il est donc plus efficace de choisir un moteur dont la puissance nominale correspond à la charge réelle, ou d'utiliser un variateur pour adapter la vitesse au besoin, plutôt que de surdimensionner le moteur.",
    "On distingue pertes fixes et variables et on relie charge, rendement et cos phi.")],
C("Le rendement et le facteur de puissance mesurent la qualité énergétique d'un moteur : le suivi de la consommation révèle les dérives.",
  "P triphasé = racine(3) U I cos phi",
  "Rendement = P mécanique utile / P électrique absorbée",
  "Puissance active~Travail reel~Facteur de puissance~cos phi~Energie reactive~Charge le reseau~Rendement~Utile sur absorbee~Pertes~Cuivre, fer, frottements~Classe IE~Efficacite normalisee",
  "Relever tension, courant et cos phi|Calculer la puissance absorbée|Comparer à la puissance mécanique|Calculer le rendement|Vérifier le dimensionnement du moteur",
  "Oublier le facteur racine de 3|Confondre rendement et cos phi|Supposer un rendement de 100 %|Ignorer la charge réelle",
  "Moteur~400 V, 10 A, cos 0,85~Puissance~5,89 kW~Utile~5,2 kW~Rendement~88 %~Pertes~0,69 kW",
  "Puissance active~Fournit du travail~Puissance reactive~Oscillle sans travail",
  "Surcharge~Rendement appele~Sous-charge~Rendement degrade"))

# ============================================================ PA4
add("PA4", "Vibrations mécaniques et équilibrage des rotors", "Physique appliquée",
S("Une vibration mécanique est une oscillation d'un système autour de sa position d'équilibre."
  "|Un mouvement harmonique se caractérise par une amplitude, une fréquence et une phase."
  "|La fréquence propre est la fréquence naturelle d'oscillation d'un système."
  "|La résonance se produit quand la fréquence d'excitation approche la fréquence propre."
  "|À la résonance, l'amplitude devient maximale et peut provoquer des dégâts."
  "|Un déséquilibre de masse crée une force centrifuge tournante proportionnelle à la vitesse au carré."
  "|Cette force excite la machine à la fréquence de rotation."
  "|L'équilibrage consiste à ajouter ou retirer une masse pour annuler le déséquilibre."
  "|L'équilibrage statique corrige le centre de gravité ; l'équilibrage dynamique corrige aussi le couple de déséquilibre."
  "|Le balourd est exprimé en grammes millimètres ou en mm/s de vibration."
  "|Un amortisseur dissipe l'énergie de vibration sous forme de chaleur."
  "|La mesure de vibration doit être effectuée dans des conditions de charge et de vitesse stables."),
[QC("Quand se produit la résonance ?", "Quand la fréquence d'excitation est très basse~Quand elle approche la fréquence propre~Quand la vitesse est nulle~Quand la masse est nulle", 1,
     "L'amplitude devient maximale au voisinage de la fréquence propre."),
 QC("Comment évolue la force de déséquilibre avec la vitesse ?", "Linéairement~Comme le carré de la vitesse~Comme l'inverse~Pas du tout", 1,
     "F = m omega² r : la force croît très vite avec la vitesse."),
 QC("À quelle fréquence se manifeste un déséquilibre ?", "À la fréquence de rotation~Au double~À la moitié~Au hasard", 0,
     "La force tourne avec le rotor, donc à sa fréquence de rotation."),
 QC("Que corrige l'équilibrage statique ?", "Le couple de déséquilibre~Le centre de gravité~La température~La tension", 1,
     "L'équilibrage dynamique corrige en plus le couple de déséquilibre."),
 QC("Quelle est l'unité courante de balourd ?", "Le gramme millimètre~Le volt~Le degré~Le pascal", 0,
     "Le balourd est un produit masse-rayon."),
 QC("Que fait un amortisseur ?", "Il augmente l'amplitude~Il dissipe l'énergie de vibration~Il change la fréquence propre~Il supprime la masse", 1,
     "L'énergie mécanique est convertie en chaleur."),
 QC("Dans quelles conditions mesurer une vibration ?", "À vide et à froid~En charge et à vitesse stable~Pendant le démarrage~Au hasard", 1,
     "Les conditions de mesure doivent être reproductibles."),
 QT("Un rotor de 10 kg présente un balourd de 200 g.mm à 1500 tr/min. Calculer la force de déséquilibre.",
    "Le balourd vaut 200 g.mm, soit 0,2 kg x 0,001 m = 2 x 10⁻⁴ kg.m. La vitesse angulaire vaut omega = 2 pi x 1500 / 60 = 50 pi, soit environ 157 rad/s. La force de déséquilibre vaut F = balourd x omega² = 2 x 10⁻⁴ x 157² = 2 x 10⁻⁴ x 24 649, soit environ 4,93 N. Cette force tournante excite les roulements et la structure à la fréquence de rotation ; elle justifie un équilibrage.",
    "On convertit le balourd en kg.m, la vitesse en rad/s, puis on applique F = m omega² r."),
 QT("Expliquer la différence entre équilibrage statique et équilibrage dynamique.",
    "L'équilibrage statique suffit pour les disques minces : on place le centre de gravité sur l'axe de rotation pour qu'à l'arrêt la pièce ne tourne pas d'elle-même. Pour un rotor long, deux plans de correction sont nécessaires : même si le centre de gravité est sur l'axe, les masses peuvent être réparties de part et d'autre et créer un couple de déséquilibre qui fait osciller les paliers en opposition de phase. L'équilibrage dynamique corrige simultanément le balourd statique et ce couple, en ajoutant ou retirant des masses dans deux plans. Il se réalise sur une machine à équilibrer, mesure de vibration et calcul des corrections à la clé.",
    "On distingue centre de gravité et couple de déséquilibre, avec le nombre de plans de correction.")],
C("Le déséquilibre crée une force tournante croissante avec la vitesse : l'équilibrage et le contrôle vibratoire protègent les paliers.",
  "F = balourd x omega² · omega = 2 pi n / 60",
  "Résonance : excitation proche de la fréquence propre",
  "Vibration~Oscillation mecanique~Frequence propre~Frequence naturelle~Resonance~Amplitude maximale~Balourd~Masse fois rayon~Equilibrage~Correction du balourd~Amortisseur~Dissipation d'energie",
  "Mesurer la vibration dans des conditions stables|Analyser la fréquence dominante|Identifier balourd ou désalignement|Choisir les plans de correction|Équilibrer et revérifier",
  "Confondre balourd et désalignement|Mesurer pendant le démarrage|Oublier la conversion en rad/s|Ignorer la résonance de la structure",
  "Rotor 10 kg~Balourd 200 g.mm~1500 tr/min~omega 157 rad/s~Force~4,9 N~Correction~Deux plans si rotor long~Controle~Vibration apres equilibrage",
  "Equilibrage statique~Centre de gravite~Equilibrage dynamique~Couple aussi corrige",
  "Dese qu'ilibre~Frequence de rotation~Desalignement~Double frequence"))

# ============================================================ PA5
add("PA5", "Transferts thermiques et refroidissement industriel", "Physique appliquée",
S("Un transfert thermique se produit toujours d'une source chaude vers une source froide."
  "|La conduction se fait par contact, sans déplacement de matière."
  "|La convection met en jeu le mouvement d'un fluide."
  "|Le rayonnement est un transfert d'énergie électromagnétique, sans milieu nécessaire."
  "|Le flux thermique de conduction vaut phi = lambda S deltaT / e."
  "|La conductivité thermique lambda caractérise la capacité d'un matériau à conduire la chaleur."
  "|Les métaux sont de bons conducteurs, l'air et les isolants sont de mauvais conducteurs."
  "|La convection forcée utilise une pompe ou un ventilateur pour augmenter les échanges."
  "|Un échangeur transfère la chaleur entre deux fluides sans les mélanger."
  "|L'efficacité d'un échangeur dépend des débits, des températures et des surfaces d'échange."
  "|L'entartrage et le colmatage réduisent les performances d'un échangeur."
  "|Le suivi des températures d'entrée et de sortie permet de détecter une dégradation."),
[QC("Quel transfert se fait sans milieu matériel ?", "La conduction~La convection~Le rayonnement~Le contact", 2,
     "Le rayonnement électromagnétique se propage même dans le vide."),
 QC("Quel est le rôle de la conductivité lambda ?", "Mesurer la masse~Caractériser la capacité à conduire la chaleur~Mesurer le débit~Indiquer la pression", 1,
     "Une forte conductivité signifie un bon conducteur thermique."),
 QC("Quel matériau est un bon conducteur ?", "L'air~Le cuivre~Le plastique~La laine de roche", 1,
     "Les métaux comme le cuivre conduisent bien la chaleur."),
 QC("Qu'appelle-t-on convection forcée ?", "Une convection sans fluide~Une convection avec ventilateur ou pompe~Une conduction dans un métal~Un rayonnement", 1,
     "Le mouvement du fluide est imposé mécaniquement."),
 QC("Que fait un échangeur ?", "Il mélange deux fluides~Il transfère la chaleur sans mélanger les fluides~Il produit de l'électricité~Il augmente la pression", 1,
     "Les deux fluides circulent de part et d'autre d'une paroi."),
 QC("Quel effet a l'entartrage d'un échangeur ?", "Il améliore les échanges~Il réduit les performances thermiques~Il n'a aucun effet~Il augmente le débit", 1,
     "Le dépôt forme une résistance thermique supplémentaire."),
 QC("Comment détecter une dégradation d'un échangeur ?", "En comparant les températures d'entrée et de sortie~En regardant sa couleur~En comptant les vis~En augmentant la charge", 0,
     "L'écart de température et le débit renseignent sur son état."),
 QT("Une paroi de 0,02 m d'épaisseur, de surface 2 m² et de conductivité 50 W/(m.K) sépare deux milieux à 80 °C et 30 °C. Calculer le flux de conduction.",
    "La différence de température vaut deltaT = 80 - 30 = 50 K. Le flux thermique vaut phi = lambda S deltaT / e = 50 x 2 x 50 / 0,02 = 5000 / 0,02 = 250 000 W, soit 250 kW. Un tel flux correspond à un métal très conducteur et à une faible épaisseur. Dans un échangeur réel, des résistances de contact et les films de convection réduisent le flux global.",
    "On identifie chaque grandeur, on applique la formule et on donne le résultat en watts."),
 QT("Expliquer pourquoi le suivi des températures et des débits permet de diagnostiquer un échangeur colmaté.",
    "Un échangeur est dimensionné pour un débit et un écart de température donnés. S'il se colmate, la perte de charge augmente et le débit diminue, tandis que la surface d'échange effective se réduit. La température de sortie du fluide à refroidir s'éloigne alors de la valeur attendue : le fluide est moins refroidi, ou le fluide chaud sort moins chaud. En comparant les mesures actuelles aux valeurs de référence à charge comparable, on détecte la dérive. On complète par la mesure de la perte de charge, qui augmente nettement en cas de colmatage, puis on nettoie ou détarte l'échangeur selon la procédure.",
    "On relie colmatage, débit, écart thermique et perte de charge.")],
C("Les trois modes de transfert expliquent le fonctionnement des échangeurs : leur suivi thermique et hydraulique révèle le colmatage.",
  "phi = lambda S deltaT / e",
  "Conduction · convection · rayonnement",
  "Conduction~Contact direct~Convection~Mouvement de fluide~Rayonnement~Onde electromagnetique~Echangeur~Transfert sans melange~Conductivite~Propriete du materiau~Entartrage~Depot isolant",
  "Identifier les modes de transfert|Relever températures et débits|Comparer aux valeurs de référence|Mesurer la perte de charge|Nettoyer et revérifier",
  "Confondre température et flux|Ignorer le sens du transfert|Oublier l'épaisseur de la paroi|Ne pas comparer à charge égale",
  "Paroi~2 m² et 20 mm~Conductivite~50 W/(m.K)~DeltaT~50 K~Flux~250 kW~Echangeur~Colmatage surveille",
  "Conduction~Sans mouvement de matiere~Convection~Avec mouvement de fluide",
  "Echangeur propre~Bons echanges~Echangeur entarre~Performance reduite"))

# FIN DES LOTS
valider_et_ecrire(F, "pro-maintenance-mat-part-B.json")
