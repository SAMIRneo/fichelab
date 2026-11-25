# -*- coding: utf-8 -*-
"""Generateur pro-maintenance-mat-part-C.json — lot C : pratique et environnement.

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


# ============================================================ PP1
add("PP1", "Outillage manuel et outils électroportatifs", "Pratique professionnelle",
S("L'outillage manuel reste indispensable pour les réglages fins et les accès difficiles."
  "|Un tournevis doit être choisi selon la tête de vis et la taille de l'empreinte."
  "|Une clé dynamométrique permet de serrer à un couple déterminé."
  "|Le serrage au couple évite aussi bien le desserrage que l'écrasement des pièces."
  "|Les clés à molette sont pratiques mais moins précises que les clés à taille fixe."
  "|Un outil électroportatif est alimenté par le secteur ou par une batterie."
  "|Les batteries lithium-ion nécessitent un chargeur adapté et une surveillance de la température."
  "|Avant chaque usage, on contrôle l'état du câble, de la fiche et des protecteurs."
  "|Le port des lunettes et des gants dépend de l'opération et des risques identifiés."
  "|Un outil mal entretenu ou émoussé demande plus d'effort et augmente le risque d'accident."
  "|Les outils doivent être nettoyés, rangés et vérifiés après utilisation."
  "|L'inventaire du matériel garantit la disponibilité des outils pour chaque intervention."),
[QC("Que permet une clé dynamométrique ?", "De serrer plus vite~De serrer à un couple déterminé~De desserrer sans effort~De mesurer une tension", 1,
     "Le couple de serrage est une valeur précise indiquée sur la notice."),
 QC("Quel est l'inconvénient d'une clé à molette ?", "Elle est trop lourde~Elle est moins précise qu'une clé à taille fixe~Elle ne existe pas~Elle est interdite", 1,
     "Son réglage joue et peut abîmer les faces de l'écrou."),
 QC("Que contrôler avant d'utiliser un outil électroportatif ?", "Sa couleur~Le câble, la fiche et les protecteurs~Le prix~La marque du chargeur", 1,
     "Le contrôle visuel précède toute mise en service."),
 QC("Quelle précautions avec une batterie lithium-ion ?", "La charger avec n'importe quel chargeur~Utiliser un chargeur adapté et surveiller la température~La mettre au micro-ondes~La laisser au soleil", 1,
     "Une batterie endommagée ou mal chargée peut s'enflammer."),
 QC("Quel est un risque d'un outil émoussé ?", "Aucun~Plus d'effort et plus de risque d'accident~Une meilleure précision~Une baisse de consommation", 1,
     "L'effort supplémentaire peut provoquer un geste brusque et une blessure."),
 QC("Quand porter des lunettes de protection ?", "Toujours, même au bureau~Selon l'opération et les risques identifiés~Jamais~Uniquement le vendredi", 1,
     "Le choix des EPI dépend de la tâche et de l'évaluation des risques."),
 QC("Pourquoi tenir un inventaire des outils ?", "Pour décorer l'atelier~Pour garantir leur disponibilité~Pour augmenter les prix~Pour éviter la formation", 1,
     "Un outil manquant retarde l'intervention."),
 QT("Expliquer la différence entre un serrage au couple et un serrage à la force, et donner un exemple d'application.",
    "Un serrage à la force dépend de la perception de l'opérateur : la même force exercée avec une clé courte ou longue ne donne pas le même couple. Un serrage au couple utilise une clé dynamométrique calibrée qui s'arrête ou signale la valeur atteinte, par exemple 25 N.m pour un boulon de roue. C'est indispensable sur les assemblages où un serrage insuffisant provoquerait un desserrage et un serrage excessif un écrasement du joint ou un filetage endommagé. La valeur provient de la notice constructeur et doit être respectée après contrôle de l'outil.",
    "On explique le rôle de la longueur de la clé et on donne une valeur de couple et une conséquence."),
 QT("Décrire la procédure de vérification quotidienne de l'outillage d'un atelier de maintenance.",
    "On commence par une inspection visuelle : câbles non abîmés, fiches intactes, carters en place, batteries sansgonflement. On teste ensuite le fonctionnement à vide pendant quelques secondes, en écoutant les bruits anormaux. On vérifie le chargement des batteries et la disponibilité des chargeurs. On contrôle l'état des embouts et des lames, qu'on remplace s'ils sont usés. On note tout défaut dans le registre ou la GMAO et on retire immédiatement l'outil défectueux du service avec une étiquette. Enfin, on range le matériel à sa place pour qu'il soit disponible lors d'une intervention urgente.",
    "On attend contrôle visuel, essai, vérification des batteries, signalement et rangement.")],
C("Un outil bien choisi, contrôlé et entretenu est plus sûr et plus efficace : le couple de serrage remplace l'à-peu-près.",
  "Couple de serrage = force x longueur de la clé",
  "Avant usage : câble, fiche, protecteurs, batterie",
  "Outil manuel~Reglages fins~Cle dynamometrique~Serrage au couple~Electroportatif~Batterie ou secteur~EPI~Lunettes et gants~Inventaire~Disponibilite",
  "Choisir l'outil adapte|Contrôler visuellement l'outil|Vérifier batteries et protecteurs|Essayer à vide|Ranger et signaler tout défaut",
  "Utiliser un outil abîmé|Serrer à la force sans référence|Charger une batterie avec un chargeur quelconque|Laisser les outils éparpillés",
  "Boulon de roue~Couple 25 N.m~Clé~Dynamométrique~Batterie~Chargeur d'origine~Defaut~Outil retire du service~Inventaire~Mise a jour",
  "Cle a molette~Pratique mais imprecise~Cle a taille fixe~Plus precise",
  "Serrage au couple~Valeur definie~Serrage a la force~Depend de l'operateur"))

# ============================================================ PP2
add("PP2", "Mesures et contrôle dimensionnel en atelier", "Pratique professionnelle",
S("Le contrôle dimensionnel vérifie la conformité d'une pièce aux cotes du plan."
  "|Le mètre et le réglet servent aux mesures courantes avec une précision limitée."
  "|Le pied à coulisse mesure les longueurs, les diamètres extérieurs et intérieurs et les profondeurs."
  "|Sa résolution courante est de 0,1 mm ou 0,05 mm."
  "|Le micromètre offre une résolution de 0,01 mm pour les diamètres de précision."
  "|Le comparateur mesure des écarts par rapport à une référence, notamment le faux-rond."
  "|Une mesure doit toujours être accompagnée de son unité et de son incertitude."
  "|Avant de mesurer, on nettoie la pièce et l'outil et on vérifie le zéro."
  "|La mesure doit être prise sans forcer, dans le sens prévu par l'instrument."
  "|Une erreur de parallaxe apparaît si l'œil n'est pas perpendiculaire à la graduation."
  "|Les cotes du plan comportent des tolérances qui définissent les limites acceptables."
  "|Les résultats sont relevés sur une fiche de contrôle ou dans la GMAO."),
[QC("Quelle est la résolution courante d'un micromètre ?", "1 mm~0,1 mm~0,01 mm~0,001 mm", 2,
     "Le micromètre mesure au centième de millimètre."),
 QC("Que mesure un pied à coulisse ?", "Uniquement les longueurs~Longueurs, diamètres et profondeurs~Seulement la température~La masse", 1,
     "Ses mors extérieurs, intérieurs et sa jauge de profondeur permettent plusieurs mesures."),
 QC("À quoi sert un comparateur ?", "À mesurer des écarts par rapport à une référence~À serrer au couple~À couper~À souder", 0,
     "Il est utilisé pour le faux-rond et les contrôles de parallélisme."),
 QC("Qu'est-ce que la parallaxe ?", "Une erreur due à l'angle de lecture~Une erreur de température~Un défaut de matière~Une unité", 0,
     "L'œil doit être perpendiculaire au plan gradué."),
 QC("Que faut-il faire avant de mesurer ?", "Nettoyer et vérifier le zéro~Forcer sur le mors~Ignorer les tolérances~Lire de travers", 0,
     "Une surface sale ou un zéro décalé faussent la mesure."),
 QC("À quoi servent les tolérances sur un plan ?", "À décorer le dessin~À définir les limites acceptables~À indiquer le prix~À donner le nom du fournisseur", 1,
     "Elles définissent la plage de valeurs conformes."),
 QC("Où consigner les résultats de contrôle ?", "Sur une fiche de contrôle ou dans la GMAO~Sur la machine~Nulle part~Sur le plan du fournisseur", 0,
     "La traçabilité des mesures est nécessaire au suivi qualité."),
 QT("Un arbre doit mesurer 25,00 mm avec une tolérance de plus ou moins 0,02 mm. Le pied à coulisse donne 25,03 mm. Que conclure ?",
    "Les limites acceptables sont 24,98 mm et 25,02 mm. La mesure de 25,03 mm est supérieure à la limite haute de 0,01 mm : la pièce est donc non conforme. Avant de la rebuter, on vérifie la mesure : nettoyage de l'arbre et du pied, contrôle du zéro, mesure en plusieurs points et dans deux directions pour détecter une ovalisation. On confirme avec un micromètre, plus précis. Si le résultat est confirmé, on isole la pièce, on alerte le responsable qualité et on recherche la cause, par exemple un réglage de machine ou une usure d'outil.",
    "On calcule les limites, on conclut et on propose une confirmation avant rebut."),
 QT("Expliquer la différence entre précision d'un instrument et incertitude de mesure.",
    "La précision, ou plutôt la résolution d'un instrument, est le plus petit écart qu'il peut afficher : 0,01 mm pour un micromètre. L'incertitude est la plage dans laquelle se situe la valeur vraie compte tenu de l'instrument, de l'opérateur, de la température et de l'état de la pièce. Une mesure affichée à 0,01 mm n'est pas exacte à 0,01 mm près : la dilation thermique d'une pièce métallique de 25 mm pour 5 °C peut déjà représenter environ 0,003 mm. C'est pourquoi on indique l'unité, la résolution et, pour un contrôle qualité, les conditions de mesure.",
    "On distingue le plus petit pas affiché de la plage d'incertitude réelle.")],
C("Le contrôle dimensionnel compare une mesure fiable à une cote tolérée : instrument adapté, zéro vérifié et traçabilité.",
  "Conformité si cote mesurée dans [cote nominale - tolérance ; cote nominale + tolérance]",
  "Pied à coulisse 0,05 mm · micromètre 0,01 mm",
  "Pied a coulisse~Mesures multiples~Micrometre~Haute resolution~Comparateur~Ecarts et faux-rond~Tolerance~Plage acceptable~Parallaxe~Erreur de lecture~Fiche de controle~Tracabilite",
  "Lire le plan et la tolérance|Nettoyer la pièce et l'instrument|Vérifier le zéro|Mesurer sans forcer|Relever et comparer",
  "Lire avec un angle|Oublier l'unité|Forcer sur le mors|Rebuter sans confirmer la mesure",
  "Arbre~25 mm plus ou moins 0,02~Limites~24,98 et 25,02~Mesure~25,03~Conclusion~Hors tolerance~Action~Confirmer au micrometre",
  "Resolution~Plus petit pas~Incertitude~Plage de doute",
  "Pied a coulisse~Polyvalent~Micrometre~Plus precis"))

# ============================================================ PP3
add("PP3", "Sécurité au travail et prévention des risques", "Pratique professionnelle",
S("La prévention vise à supprimer ou réduire les risques avant qu'ils ne provoquent un accident."
  "|Un risque est la combinaison de la probabilité d'un événement et de la gravité de ses conséquences."
  "|Le document unique d'évaluation des risques professionnels recense les risques par poste."
  "|Les risques courants en atelier sont les chutes, les coupures, les brûlures, le bruit et les produits chimiques."
  "|La hiérarchie des mesures de prévention commence par supprimer le risque à la source."
  "|Viennent ensuite les protections collectives, puis les protections individuelles."
  "|Les EPI ne protègent que s'ils sont adaptés, portés correctement et entretenus."
  "|Une formation et une information des salariés sont obligatoires."
  "|Le port de charges doit respecter les limites et utiliser les aides à la manutention."
  "|Les issues de secours et les extincteurs doivent rester accessibles et signalés."
  "|Tout accident, même bénin, doit être signalé et analysé."
  "|Le comité social et économique est consulté sur les questions de santé et de sécurité."),
[QC("Qu'appelle-t-on risque ?", "Un événement certain~Probabilité multipliée par la gravité~Une règle de sécurité~Un EPI", 1,
     "Le risque combine la fréquence possible et la sévérité de l'effet."),
 QC("Quel document recense les risques par poste ?", "Le devis~Le document unique~La facture~Le plan de maintenance", 1,
     "Le DUERP est obligatoire dans les entreprises."),
 QC("Quelle est la première mesure de prévention ?", "Distribuer des gants~Supprimer le risque à la source~Signaler l'accident~Fermer l'atelier", 1,
     "La hiérarchie commence par la suppression du danger."),
 QC("Quel est un risque courant en atelier ?", "Le bruit~La couleur des murs~Le nombre de fenêtres~Le prix des outils", 0,
     "Bruit, chutes, coupures et brûlures sont des risques fréquents."),
 QC("Quand les EPI sont-ils efficaces ?", "Toujours~S'ils sont adaptés, bien portés et entretenus~S'ils sont neufs uniquement~Sans formation", 1,
     "Un EPI inadapté ou mal porté ne protège pas."),
 QC("Que faut-il faire après un accident bénin ?", "Rien~Le signaler et l'analyser~Le cacher~Attendre un accident grave", 1,
     "L'analyse permet d'éviter la récidive."),
 QC("Quel est le rôle du CSE en matière de sécurité ?", "Vendre la production~Être consulté sur la santé et la sécurité~Fixer les prix~Remplacer l'inspecteur", 1,
     "Le CSE est un acteur de la prévention en entreprise."),
 QT("Appliquer la hiérarchie des mesures de prévention au risque de chute de hauteur lors d'une intervention sur une machine.",
    "La meilleure solution est de supprimer le travail en hauteur, par exemple en descendant l'organe à hauteur d'homme ou en utilisant une plateforme au sol. Si ce n'est pas possible, on met en place une protection collective : garde-corps, plateforme fixe, point d'ancrage et filet. Viennent ensuite les mesures individuelles : harnais avec longe et absorbeur, vérifiés avant usage, ainsi que des chaussures adaptées. On complète par une consigne écrite, une formation, une autorisation de travail en hauteur et une surveillance. Enfin, on prévoit les secours et un plan d'évacuation. Les EPI seuls ne suffisent jamais si une protection collective est possible.",
    "On respecte l'ordre : suppression, protection collective, protection individuelle, puis formation et organisation."),
 QT("Un technicien signale une odeur de gaz dans l'atelier. Décrire la conduite à tenir.",
    "On ne manipule aucun interrupteur, car une étincelle pourrait provoquer une explosion. On prévient immédiatement les personnes proches et on évacue le local par le chemin le plus court, sans courir. On coupe l'alimentation générale depuis un endroit sûr si cela est possible, puis on alerte le responsable d'atelier et les services d'urgence selon la procédure. On interdit l'accès à la zone, on ouvre les portes et fenêtres si la sécurité le permet et on attend l'autorisation des secours avant de rentrer. Après l'incident, on consigne les faits et on analyse la cause pour mettre en place des mesures correctives.",
    "On attend évacuation, absence de manipulation électrique, alerte, consignation de la zone et analyse.")],
C("La prévention suit une hiérarchie : supprimer le danger, protéger collectivement, puis protéger individuellement et former.",
  "Risque = probabilité x gravité",
  "Suppression · protections collectives · EPI · information",
  "Risque~Probabilite fois gravite~DUERP~Document unique~Prevention~Supprimer le danger~EPI~Protection individuelle~Formation~Information obligatoire~CSE~Consultation",
  "Identifier les dangers par poste|Évaluer probabilité et gravité|Supprimer ou isoler le danger|Choisir les protections adaptées|Former, signaler et surveiller",
  "Se contenter des gants|Ignorer un accident bénin|Laisser les issues obstruées|Ne pas documenter l'évaluation",
  "Travail en hauteur~Risque de chute~Priorite~Supprimer la hauteur~Collectif~Garde-corps~Individuel~Harnais~Apres~Analyse et formation",
  "Prevention~Avant l'accident~Protection~Pendant l'exposition",
  "Risque faible~Peu probable ou peu grave~Risque eleve~Probable et grave"))

# ============================================================ PP4
add("PP4", "Lecture de plans et dessin industriel", "Pratique professionnelle",
S("Un dessin industriel est un langage normalisé qui décrit une pièce ou un ensemble."
  "|La projection orthogonale représente un objet selon plusieurs vues distinctes."
  "|Les vues courantes sont la vue de face, la vue de dessus et la vue de côté."
  "|La disposition européenne place la vue de dessus sous la vue de face."
  "|Les lignes visibles sont continues, les lignes cachées sont en pointillés."
  "|Un axe de symétrie est représenté par un trait mixte."
  "|Les cotes indiquent les dimensions réelles, indépendamment de l'échelle du dessin."
  "|Une cote se lit avec sa valeur, son unité et sa tolérance éventuelle."
  "|Les tolérances géométriques définissent des écarts de forme ou de position admissibles."
  "|Un état de surface est indiqué par un symbole et une valeur de rugosité."
  "|La nomenclature liste les composants d'un ensemble avec leurs repères et quantités."
  "|Le respect des normes ISO permet à tous les intervenants de lire le même document."),
[QC("Comment sont représentées les lignes cachées ?", "En trait continu~En pointillés~En couleur rouge~En trait épais", 1,
     "Les lignes cachées sont dessinées en traits interrompus fins."),
 QC("Où se place la vue de dessus en disposition européenne ?", "Au-dessus de la vue de face~En dessous de la vue de face~À droite~À gauche", 1,
     "La disposition européenne place la vue de dessous la vue principale."),
 QC("Que represente un trait mixte ?", "Une arête visible~Un axe ou une ligne de symétrie~Une cote~Une section", 1,
     "Le trait mixte matérialise les axes et les plans de symétrie."),
 QC("Les cotes dépendent-elles de l'échelle du dessin ?", "Oui~Non, elles donnent les dimensions réelles~Seulement pour les petites pièces~Uniquement en 3D", 1,
     "On cote la pièce réelle, pas sa représentation."),
 QC("Quelle information donne un symbole d'état de surface ?", "Le prix~La rugosité attendue~La masse~La couleur", 1,
     "La rugosité, par exemple Ra 3,2 micromètres, conditionne le contact entre pièces."),
 QC("Que contient une nomenclature ?", "Les repères et quantités des composants~Les horaires~Les salaires~Les couleurs", 0,
     "Elle permet d'identifier chaque pièce d'un ensemble."),
 QC("Pourquoi normaliser les dessins ?", "Pour rendre le dessin unique~Pour que tous les intervenants lisent la même chose~Pour réduire le nombre de vues~Pour supprimer les cotes", 1,
     "Les normes ISO garantissent une interprétation commune."),
 QT("Expliquer la différence entre une vue en projection orthogonale et une vue en perspective.",
    "La projection orthogonale utilise des rayons parallèles perpendiculaires au plan de projection : les arêtes parallèles restent parallèles et les dimensions sont conservées, ce qui permet de coter précisément la pièce. La perspective reproduit la vision humaine, avec des lignes convergentes et des dimensions qui diminuent avec l'éloignement : elle est utile pour la lecture d'ensemble mais ne permet pas de mesurer. Un dessin industriel utilise plusieurs vues orthogonales complétées, si besoin, par une vue isométrique pour la compréhension.",
    "On oppose conservation des dimensions et rendu visuel, avec l'usage de chaque mode."),
 QT("Une pièce porte la cote 40 plus ou moins 0,1 mm. Quelles sont les limites acceptables et que faire si une mesure donne 40,15 mm ?",
    "Les limites sont 39,9 mm et 40,1 mm. Une mesure de 40,15 mm dépasse la limite haute de 0,05 mm : la pièce est hors tolérance. On vérifie d'abord la mesure elle-même, en contrôlant l'instrument, le zéro et la propreté de la surface, puis on répète le relevé en plusieurs points. Si le résultat est confirmé, on isole la pièce et on prévient le responsable qualité. Selon le cas, la pièce peut être reprise en usinage si le surplus de matière le permet, ou mise au rebut. On recherche ensuite la cause : réglage de machine, usure d'outil ou erreur de lecture du plan.",
    "On calcule les limites, on vérifie la mesure puis on décrit le traitement de la non-conformité.")],
C("Un plan industriel normalisé se lit avec ses vues, ses lignes, ses cotes et ses tolérances : il est la référence de la fabrication et du contrôle.",
  "Cote réelle ≠ taille dessinée à l'échelle",
  "Continu : visible · pointillé : caché · mixte : axe",
  "Projection orthogonale~Vues normalisees~Ligne cachee~Trait interrompu~Axe~Trait mixte~Cote~Dimension reelle~Tolerance~Ec admissible~Nomenclature~Liste des composants",
  "Repérer la vue principale|Lire les lignes et les axes|Relever les cotes et tolérances|Consulter la nomenclature|Contrôler la pièce",
  "Mesurer sur le dessin au lieu de lire la cote|Ignorer les tolérances|Confondre ligne cachée et axe|Oublier l'échelle pour se repérer",
  "Cote 40~Plus ou moins 0,1~Limites~39,9 et 40,1~Mesure~40,15~Decision~Hors tolerance~Nomenclature~Repere et quantite",
  "Projection orthogonale~Cotable~Perspective~Non mesurable",
  "Vue de face~Vue principale~Vue de dessus~Sous la vue de face"))

# ============================================================ PP5
add("PP5", "Techniques de montage et d'assemblage mécanique", "Pratique professionnelle",
S("Un assemblage mécanique doit assurer la fonction tout en restant démontable si nécessaire."
  "|Les assemblages démontables utilisent des vis, des écrous, des goupilles ou des clavettes."
  "|Les assemblages permanents comprennent le soudage, le rivetage et le collage structurel."
  "|Le choix des vis dépend du diamètre, du pas, de la classe de résistance et de l'environnement."
  "|Une clavette transmet un couple entre un arbre et un moyeu."
  "|Le montage d'un roulement exige une propreté parfaite et des outils adaptés."
  "|La force de montage doit s'appliquer sur la bague concernée, jamais sur les éléments roulants."
  "|Un joint d'étanchéité doit être neuf et posé dans le sens indiqué."
  "|Le couple de serrage et l'ordre de serrage sont donnés par la notice constructeur."
  "|Un serrage en croix permet de répartir uniformément la pression sur un joint de bride."
  "|Les filetages peuvent être protégés par un frein-filet adapté aux vibrations."
  "|Après montage, on vérifie le jeu, l'alignement et la libre rotation."),
[QC("Quel assemblage est démontable ?", "Le soudage~Le vissage~Le rivetage~Le collage", 1,
     "Une vis se dévisse, contrairement à une soudure ou à un rivet."),
 QC("À quoi sert une clavette ?", "À étanchéifier~À transmettre un couple entre arbre et moyeu~À lubrifier~À mesurer", 1,
     "La clavette est insérée dans une rainure et transmet l'effort tangentiel."),
 QC("Sur quoi appliquer la force lors du montage d'un roulement ?", "Sur les billes~Sur la bague concernée~Sur la cage~Sur le joint", 1,
     "Appliquer la force sur les éléments roulants les endommagerait."),
 QC("Pourquoi serrer en croix une bride ?", "Pour gagner du temps~Pour répartir uniformément la pression~Pour utiliser moins de vis~Pour changer le joint", 1,
     "Le serrage croisé évite la déformation et les fuites."),
 QC("Que faire d'un joint d'étanchéité lors d'un remontage ?", "Le réutiliser tel quel~Le remplacer par un neuf~Le retourner~Le graisser avec n'importe quoi", 1,
     "Un joint usé ne garantit plus l'étanchéité."),
 QC("Que vérifier après montage ?", "La couleur de la pièce~Le jeu, l'alignement et la libre rotation~Le prix~La date", 1,
     "Ces contrôles détectent un montage incorrect avant la mise en service."),
 QC("À quoi sert un frein-filet ?", "À augmenter le couple~À éviter le desserrage sous vibration~À lubrifier le filetage~À colorer la vis", 1,
     "Il bloque le filetage, avec une force adaptée au démontage ultérieur."),
 QT("Décrire les précautions à prendre lors du remplacement d'un roulement monté sur un arbre.",
    "On prépare un plan de travail propre, les outils adaptés, le roulement neuf et la graisse prescrite. On dépose l'ancien roulement avec un extracteur en prenant appui sur la bonne bague, sans choquer l'arbre. On nettoie et contrôle le logement et l'arbre : absence de bavures, d'usure et de traces d'oxydation. On vérifie les cotes et le sens de montage indiqué sur la bague. On pose le roulement neuf avec une douille ou une presse, en appliquant l'effort uniquement sur la bague montée serrée, jamais sur les billes. On ajoute la quantité de graisse recommandée, on remet les joints neufs, puis on vérifie à la main la libre rotation et le jeu avant de remonter le carter.",
    "On attend propreté, extracteur, contrôle des portées, effort sur la bague et essai de rotation."),
 QT("Expliquer pourquoi l'ordre de serrage des vis d'une bride est important.",
    "Une bride est une pièce relatively rigide mais les joints sont compressibles. Si on serre les vis les unes à côté des autres, la bride se déforme en biais : certains points sont écrasés et d'autres restent peu comprimés, ce qui crée une fuite. Un serrage en croix, en plusieurs passes à couple croissant par exemple 30 %, 60 % puis 100 % du couple final, répartit la charge uniformément sur le joint. On commence par la vis opposée à la première et on suit un ordre défini au plan ou dans la notice. On vérifie ensuite l'absence de fuite lors du essai en pression.",
    "On explique la déformation, l'ordre en croix et le serrage progressif en passes.")],
C("Un assemblage fiable respecte la propreté, le sens de montage, le couple de serrage et un contrôle final avant mise en service.",
  "Couple de serrage : valeur de la notice · serrage en croix",
  "Démontable : vis, goupille, clavette · permanent : soudure, rivet",
  "Assemblage demontable~Vis et clavettes~Clavette~Transmet un couple~Roulement~Monter par la bague~Joint neuf~Etancheite~Serrage en croix~Repartition uniforme~Frein-filet~Anti-desserrage",
  "Préparer outils et pièces propres|Contrôler portées et cotes|Respecter le sens de montage|Serrer au couple en croix|Vérifier jeu et rotation",
  "Frapper sur les billes du roulement|Réutiliser un joint usé|Serrer les vis dans l'ordre circulaire|Oublier le contrôle final",
  "Roulement~Remplace~Extracteur~Outil adapte~Bague~Effort applique~Couple~Selon notice~Essai~Rotation libre",
  "Démontable~Vis~Permanent~Soudure",
  "Serrage direct~Deformation possible~Serrage en croix~Pression uniforme"))

# ============================================================ PP6
add("PP6", "Soudage, brasage et sécurité associée", "Pratique professionnelle",
S("Le soudage est un assemblage permanent obtenu par fusion locale des pièces."
  "|Le brasage assemble des pièces sans les fondre, grâce à un métal d'apport fondu à plus basse température."
  "|Le soudage à l'arc électrique utilise un courant électrique pour créer un arc entre l'électrode et la pièce."
  "|Le procédé MIG MAG utilise un fil d'apport continu et un gaz de protection."
  "|Le procédé TIG utilise une électrode de tungstène et un gaz protecteur, avec un apport éventuel."
  "|Le choix du procédé dépend du métal, de l'épaisseur, de la position et de la qualité demandée."
  "|Les principaux défauts sont les soufflures, les inclusions, les criques et le manque de pénétration."
  "|Une préparation correcte des bords et le nettoyage des surfaces améliorent la qualité du cordon."
  "|Les gaz de protection et la ventilation évitent l'oxydation et l'inhalation de fumées."
  "|Les risques du soudage sont les brûlures, les rayonnements, les fumées, le bruit et l'incendie."
  "|Le port d'un masque à filtre adapté, de gants et de vêtements ignifugés est obligatoire."
  "|Une autorisation de travail par point chaud est requise dans les zones à risque d'incendie."),
[QC("Quelle est la différence entre soudage et brasage ?", "Le brasage fond les pièces~Le brasage ne fond pas les pièces, seul l'apport fond~Aucune~Le soudage utilise toujours un gaz", 1,
     "Le brasage reste en dessous de la température de fusion des pièces assemblées."),
 QC("Quel procédé utilise une électrode de tungstène ?", "MIG~MAG~TIG~Electrode enrobée", 2,
     "Le TIG utilise une électrode non fusible en tungstène."),
 QC("Quel rôle joue le gaz de protection ?", "Refroidir le fil~Protéger le bain de fusion de l'oxydation~Augmenter le courant~Colorer le cordon", 1,
     "Le gaz isolé le métal en fusion de l'air ambiant."),
 QC("Quel est un défaut de soudage ?", "Une soufflure~Un cordon régulier~Une pénétration correcte~Une surface propre", 0,
     "Les soufflures sont des cavités gazeuses incluses dans le cordon."),
 QC("Quel EPI est spécifique au soudage ?", "Un masque à filtre adapté~Des lunettes de lecture~Un casque anti-bruit seulement~Des gants de cuisine", 0,
     "Le masque protège les yeux et le visage des rayonnements et des projections."),
 QC("Quelle autorisation est requise pour un travail par point chaud ?", "Une autorisation de travail par point chaud~Aucune~Un bon de commande~Une facture", 0,
     "Cette procédure prévient les incendies dans les zones sensibles."),
 QC("Pourquoi ventiler la zone de soudage ?", "Pour rafraîchir la salle~Pour évacuer les fumées~Pour augmenter l'arc~Pour sécher le métal", 1,
     "Les fumées de soudage sont nocives pour les voies respiratoires."),
 QT("Comparer les procédés MIG/MAG et TIG et indiquer leurs domaines d'utilisation.",
    "Le procédé MIG/MAG utilise un fil d'apport consommable alimenté en continu et un gaz protecteur. Il est rapide, productif, adapté aux tôles et aux constructions métalliques courantes, avec une préparation de joint moins exigeante. Le procédé TIG utilise une électrode de tungstène non fusible, un gaz protecteur et un apport éventuel à la main. Il est plus lent mais donne des cordons très propres et précis, idéaux pour les aciers inoxydables, l'aluminium et les passes de racine sur des tubes. Le choix dépend de la qualité demandée, de la productivité et du métal à assembler.",
    "On oppose fil consommable et électrode non fusible, vitesse et qualité, avec des exemples d'usage."),
 QT("Décrire les mesures de sécurité à mettre en place avant une intervention de soudage dans un atelier.",
    "On vérifie d'abord que le poste est conforme : câbles, masse, connecteurs et système de ventilation. On obtient l'autorisation de travail par point chaud si la zone est à risque incendie. On éloigne ou protège les matières combustibles, on prévoit un extincteur et une surveillance après l'arrêt du travail, car des braises peuvent rester actives. On porte le masque avec filtre adapté au procédé, les gants, les vêtements ignifugés et les protections auditives. On signale la zone pour éviter qu'une personne non protégée regarde l'arc. On contrôle enfin que la pièce est propre, dégraissée et correctement positionnée avant d'amorcer l'arc.",
    "On attend autorisation, éloignement des combustibles, EPI, signalisation et surveillance après travail.")],
C("Soudage et brasage produisent des assemblages permanents : la qualité du cordon et la sécurité dépendent de la préparation et des EPI.",
  "Soudage : fusion des pièces · brasage : fusion de l'apport seulement",
  "MIG/MAG : fil consommable · TIG : électrode tungstène",
  "Soudage~Fusion des pieces~Brasage~Apport seul fond~MIG MAG~Fil et gaz~TIG~Electrode de tungstene~Soufflure~Defaut gazeux~Point chaud~Autorisation incendie",
  "Obtenir l'autorisation|Éloigner les combustibles|Préparer et nettoyer les bords|Porter les EPI adaptés|Souder puis surveiller la zone",
  "Regarder l'arc sans masque|Laisser des produits inflammables à proximité|Négliger le nettoyage des bords|Partir sans surveillance après le travail",
  "Tole inoxydable~Procédé TIG~Production~MIG MAG~Defaut~Soufflure~EPI~Masque et gants~Apres~Surveillance incendie",
  "Soudage~Pièces fondues~Brasage~Pièces non fondues",
  "MIG MAG~Rapide~TIG~Precis et propre"))

# ============================================================ EG1
add("EG1", "Coûts de maintenance et prix de revient", "Économie et gestion",
S("Le coût de maintenance comprend toutes les dépenses liées au maintien en état des équipements."
  "|On distingue les coûts directs : main-d'oeuvre, pièces et sous-traitance."
  "|Les coûts indirects comprennent l'encadrement, l'outillage, la formation et les frais généraux."
  "|Le coût de la main-d'oeuvre s'obtient en multipliant le temps passé par le taux horaire."
  "|Le taux horaire charges comprises inclut le salaire et les charges sociales."
  "|Le coût d'une intervention est la somme de la main-d'oeuvre, des pièces et des frais divers."
  "|Le coût d'arrêt de production est souvent supérieur au coût de l'intervention elle-même."
  "|Un coût évité correspond à une panne qui n'a pas eu lieu grâce à la prévention."
  "|Le prix de revient enablede déterminer la rentabilité d'une action de maintenance."
  "|Le coût global de possession inclut l'achat, l'exploitation, la maintenance et la fin de vie."
  "|Un équipement peu coûteux à l'achat peut être cher à exploiter."
  "|Les données de coût alimentent le tableau de bord et les décisions d'investissement."),
[QC("Quel est un coût direct de maintenance ?", "La formation~La main-d'oeuvre~Le loyer du bureau~L'encadrement", 1,
     "Main-d'oeuvre, pièces et sous-traitance sont affectées directement à l'intervention."),
 QC("Comment calculer le coût de main-d'oeuvre ?", "Temps passé multiplié par le taux horaire~Nombre de pièces divisé par le temps~Prix d'achat plus TVA~Salaires divisés par douze", 0,
     "On utilise le temps réellement passé et un taux horaire chargé."),
 QC("Quel coût est souvent supérieur à celui de la réparation ?", "Le coût de la pièce~Le coût d'arrêt de production~Le coût du graissage~Le coût de l'outil", 1,
     "Une heure d'arrêt sur une ligne coûte cher en production non réalisée."),
 QC("Que désigne un coût évité ?", "Une dépense non prévue~Une panne empêchée par la prévention~Un achat annulé~Une facture en retard", 1,
     "Il justifie l'investissement dans la maintenance préventive."),
 QC("Que comprend le coût global de possession ?", "Le seul prix d'achat~Achat, exploitation, maintenance et fin de vie~Le salaire uniquement~La TVA uniquement", 1,
     "Le TCO considère toute la durée de vie de l'équipement."),
 QC("Quel est un coût indirect ?", "Une pièce remplacée~L'outillage et la formation~Le temps de réparation~La sous-traitance", 1,
     "Les coûts indirects ne sont pas rattachés à une seule intervention."),
 QC("À quoi servent les données de coût ?", "À décorer les rapports~Aux décisions d'investissement et au pilotage~À supprimer la maintenance~À fixer les horaires", 1,
     "Elles permettent d'arbitrer entre réparer et remplacer."),
 QT("Une intervention a mobilisé 2,5 h de main-d'oeuvre à 48 €/h, pour 85 € de pièces et 30 € de frais. Calculer son coût total.",
    "Main-d'oeuvre : 2,5 x 48 = 120 €. Pièces : 85 €. Frais divers : 30 €. Coût total de l'intervention = 120 + 85 + 30 = 235 €. Si l'arrêt de production a duré 3 h et que chaque heure d'arrêt coûte 400 €, le coût d'arrêt s'élève à 1 200 €, soit plus de cinq fois le coût de l'intervention. Ce comparatif montre pourquoi une maintenance préventive bien calibrée est économiquement favorable.",
    "On calcule le coût direct puis on le compare au coût d'arrêt."),
 QT("Expliquer pourquoi un équipement bon marché à l'achat peut revenir plus cher sur sa durée de vie.",
    "Le prix d'achat ne représente qu'une partie du coût global de possession. Un équipement d'entrée de gamme peut consommer plus d'énergie, tomber plus souvent en panne, nécessiter des pièces coûteuses ou indisponibles et demander plus de main-d'oeuvre. Il peut aussi provoquer des arrêts de production plus longs et avoir une durée de vie plus courte. Le coût global additionne l'achat, la consommation, la maintenance, les arrêts et la mise hors service. Pour un moteur, un modèle plus efficace mais plus cher peut économiser assez d'énergie en quelques années pour compenser la différence d'achat. Le gestionnaire raisonne donc sur le coût de possession, pas sur le seul prix d'achat.",
    "On définit le coût global et on donne un exemple d'arbitrage achat contre exploitation.")],
C("Le coût de maintenance se décompose en main-d'oeuvre, pièces et frais : le pilotage raisonne en coût global, pas en prix d'achat.",
  "Coût intervention = temps x taux horaire + pièces + frais",
  "TCO = achat + exploitation + maintenance + fin de vie",
  "Cout direct~Main-d'oeuvre et pieces~Cout indirect~Encadrement et formation~Taux horaire~Salaire plus charges~Cout d'arret~Production perdue~TCO~Cout global de possession~Cout evite~Panne empêchee",
  "Relever le temps passé|Valoriser la main-d'oeuvre|Ajouter pièces et frais|Comparer au coût d'arrêt|Décider avec le tableau de bord",
  "Oublier les charges sociales|Ignorer le coût d'arrêt|Raisonner sur le seul prix d'achat|Ne pas valoriser les pannes évitées",
  "Intervention~2,5 h a 48 €~Main-d'oeuvre~120 €~Pieces~85 €~Frais~30 €~Total~235 €",
  "Cout direct~Affecte a l'action~Cout indirect~Partage entre actions",
  "Prix d'achat~Court terme~Cout global~Toute la duree de vie"))

# ============================================================ EG2
add("EG2", "Devis, commande et facturation", "Économie et gestion",
S("Un devis est un document commercial qui propose une prestation à un prix déterminé."
  "|Il précise l'identité des parties, la description des travaux, les délais et les conditions de paiement."
  "|Un devis est gratuit ou payant, et il engage son auteur pendant sa durée de validité."
  "|La commande est l'acceptation du devis par le client : elle rend la prestation ferme."
  "|Une facture doit être émise pour toute vente ou prestation de service."
  "|Elle mentionne le numéro, la date, le client, le détail des prestations et les totaux."
  "|Le prix hors taxes, le taux de TVA et le montant de la TVA doivent apparaître séparément."
  "|Le prix TTC s'obtient en ajoutant la TVA au prix HT."
  "|Un acompte peut être demandé avant le début des travaux."
  "|Le délai de paiement et les pénalités de retard doivent être indiqués."
  "|Une facture impayée peut faire l'objet d'une relance puis d'une mise en demeure."
  "|Les documents commerciaux doivent être conservés pour la comptabilité et le suivi de l'entreprise."),
[QC("Quel document propose un prix avant l'exécution ?", "La facture~Le devis~Le bon de livraison~Le contrat de travail", 1,
     "Le devis est une proposition commerciale, la facture constate la vente."),
 QC("Quand la prestation devient-elle ferme ?", "À l'émission du devis~À l'acceptation du devis, soit la commande~À la facture~Au paiement", 1,
     "La commande matérialise l'accord entre les parties."),
 QC("Quelles mentions doit contenir une facture ?", "Le nom du client et le détail des prestations~La couleur du papier~La marque de l'ordinateur~Le nombre de salariés", 0,
     "Les mentions légales et fiscales sont obligatoires."),
 QC("Comment calculer le prix TTC ?", "HT moins TVA~HT plus TVA~HT multiplié par le taux uniquement~TVA divisée par HT", 1,
     "TTC = HT + montant de la TVA."),
 QC("Quelle est la durée de validité d'un devis ?", "Illimitée~Limitée, indiquée sur le devis~Toujours un an~Jamais précisée", 1,
     "Le devis engage son auteur pendant la période indiquée."),
 QC("Que peut exiger un vendeur avant de commencer ?", "Un acompte~Une facture finale~Un reçu~Une mise en demeure", 0,
     "L'acompte sécurise le démarrage de la prestation."),
 QC("Que faire face à une facture impayée ?", "Rien~Relancer puis mettre en demeure~Augmenter le prix~Supprimer la facture", 1,
     "La relance puis la mise en demeure sont les étapes habituelles."),
 QT("Un devis de maintenance porte sur 1 200 € HT de main-d'oeuvre et 350 € HT de pièces, avec une TVA de 20 %. Calculer le total TTC.",
    "Total HT = 1 200 + 350 = 1 550 €. Montant de la TVA = 1 550 x 0,20 = 310 €. Total TTC = 1 550 + 310 = 1 860 €. Le devis doit faire apparaître séparément le total HT, le taux de 20 %, le montant de TVA de 310 € et le total TTC de 1 860 €. Un acompte de 30 %, soit 558 € TTC, peut être demandé si cette condition est indiquée au devis.",
    "On calcule la base HT puis la TVA et le TTC, en présentant les montants séparément."),
 QT("Expliquer le rôle respectif du devis, de la commande et de la facture dans une intervention de maintenance.",
    "Le devis est la proposition : il décrit la prestation, le prix, les délais et les conditions. Il permet au client de comparer et de décider, sans l'obliger tant qu'il ne l'accepte pas. La commande est l'acceptation du devis : elle crée l'engagement juridique des deux parties et déclenche la planification de l'intervention. La facture intervient après la réalisation : elle constate la prestation accomplie, chiffre le montant dû et fait naître l'obligation de paiement à échéance. Ces trois documents assurent la traçabilité commerciale et comptable de l'opération.",
    "On distingue proposition, engagement et constatation de la vente.")],
C("Devis, commande et facture jalonnent l'opération : proposer, s'engager, puis constater la vente avec TVA distincte.",
  "TTC = HT + HT x taux de TVA",
  "Devis = proposition · commande = acceptation · facture = constatation",
  "Devis~Proposition commerciale~Commande~Acceptation du devis~Facture~Constatation de la vente~HT~Hors taxes~TTC~Toutes taxes comprises~Acompte~Paiement partiel",
  "Établir le devis avec toutes les mentions|Obtenir la commande du client|Réaliser la prestation|Émettre la facture|Suivre le paiement et relancer",
  "Confondre devis et facture|Oublier de faire apparaître la TVA|Ne pas préciser la durée de validité|Négliger les relances",
  "Devis~1 200 et 350 € HT~Total HT~1 550 €~TVA 20 %~310 €~TTC~1 860 €~Acompte~30 % soit 558 €",
  "Devis~Avant~Facture~Apres",
  "Prix HT~Base de calcul~Prix TTC~Montant a payer"))

# ============================================================ EG3
add("EG3", "Budget et suivi financier d'un service maintenance", "Économie et gestion",
S("Un budget prévisionnel estime les recettes et les dépenses d'une période à venir."
  "|Le budget de maintenance comprend la main-d'oeuvre, les pièces, la sous-traitance et les investissements."
  "|Il s'appuie sur l'historique des interventions et le plan de maintenance."
  "|Une provision pour interventions exceptionnelles permet de faire face aux pannes majeures."
  "|Le suivi budgétaire compare régulièrement le réalisé au prévisionnel."
  "|Un écart peut venir d'un volume d'activité different ou d'un prix unitaire modifié."
  "|L'analyse des écarts distingue l'effet volume et l'effet prix."
  "|Un dépassement doit être expliqué et validé avant d'être accepté."
  "|Les investissements sont arbitrés selon leur impact sur la disponibilité et les coûts futurs."
  "|Le taux de consommation des pièces aide à dimensionner le stock."
  "|Un rapport régulier présente le budget consommé, les prévisions et les risques."
  "|La maîtrise budgétaire ne doit pas sacrificed la sécurité des interventions."),
[QC("Que contient un budget de maintenance ?", "Les seuls salaires~Main-d'oeuvre, pièces, sous-traitance et investissements~Le prix du client~Les horaires", 1,
     "Le budget couvre toutes les ressources nécessaires à l'activité."),
 QC("Sur quoi s'appuie le budget prévisionnel ?", "Sur l'historique et le plan de maintenance~Sur le hasard~Sur le prix du fournisseur uniquement~Sur la météo", 0,
     "Les données passées et les interventions programmées servent de base."),
 QC("Que permet une provision pour aléas ?", "D'augmenter les prix~De faire face aux pannes exceptionnelles~De supprimer le stock~De réduire la formation", 1,
     "C'est une réserve financière pour les événements imprévus."),
 QC("Que compare le suivi budgétaire ?", "Le réalisé et le prévisionnel~Deux fournisseurs~Les salaires et les prix~Les machines et les clients", 0,
     "L'écart entre prévu et réalisé est le premier signal."),
 QC("Quelle est une cause d'écart budgétaire ?", "Un effet volume ou prix~La couleur des factures~Le nombre de pages du rapport~La marque des outils", 0,
     "On décompose l'écart en quantité et en prix unitaire."),
 QC("Que faut-il faire face à un dépassement ?", "L'ignorer~L'expliquer et le faire valider~Augmenter la production~Supprimer la maintenance", 1,
     "Tout écart doit être justifié et validé."),
 QC("Que ne faut-il jamais sacrifier à la maîtrise budgétaire ?", "La sécurité~La couleur du rapport~La durée des réunions~Le nombre d'indicateurs", 0,
     "Les contraintes économiques ne justifient pas une intervention risquée."),
 QT("Un budget pièces prévoit 40 000 € pour l'année. À mi-année, 26 000 € ont été consommés. Commenter cet écart et proposer une action.",
    "À mi-année, la consommation prévue par répartition linéaire serait de 20 000 €. L'écart est donc de 6 000 €, soit 30 % au-dessus du rythme prévisionnel. Si aucune panne exceptionnelle n'est survenue, on analyse les prix unitaires et les quantités : hausse des tarifs fournisseurs, remplacements évitables, stock mal géré ou erreur de prévision. On vérifie si des interventions préventives ont été anticipées, ce qui peut être favorable malgré le dépassement. On propose ensuite une révision du budget, une renégociation des prix ou un meilleur suivi des stocks, puis on surveille le taux de consommation des Prochains mois.",
    "On compare au rythme prévu, on décompose l'écart et on propose des actions correctives."),
 QT("Expliquer comment un suivi budgétaire régulier contribue à la fiabilité des équipements.",
    "Un suivi régulier révèle les dérives avant qu'elles ne deviennent critiques : une consommation anormale de pièces signale une usure rapide, un recours croissant à la sous-traitance indique un manque de compétences interne ou de disponibilité. Les données financières croisées avec la GMAO permettent de repérer les équipements les plus coûteux et d'arbitrer entre réparation et remplacement. Le budget donne aussi les moyens de programmer la prévention plutôt que de subir les pannes. Il ne s'agit pas de dépenser moins à tout prix, mais de dépenser utilement, en conservant la sécurité et la disponibilité comme priorités.",
    "On relie suivi financier, détection des dérives et décisions de maintenance.")],
C("Le suivi budgétaire compare prévu et réalisé, décompose les écarts et oriente les arbitrages sans sacrifier la sécurité.",
  "Écart = réalisé - prévisionnel",
  "Analyse : effet volume + effet prix",
  "Budget~Prevision de depenses~Realise~Depenses constatees~Ecart~Difference~Provision~Reserve pour aleas~Effet volume~Quantite differente~Effet prix~Tarif modifie",
  "Élaborer le budget à partir de l'historique|Suivre les dépenses mois par mois|Calculer les écarts|Analyser volume et prix|Proposer des arbitrages et valider",
  "Attendre la fin d'année pour regarder le budget|Confondre effet prix et effet volume|Réduire les dépenses de sécurité|Ne pas documenter les écarts",
  "Budget pièces~40 000 €/an~Mi-année~20 000 € prevus~Realise~26 000 €~Ecart~6 000 €~Action~Analyser et revoir",
  "Prévisionnel~Avant~Réalisé~Après",
  "Effet volume~Quantite~Effet prix~Tarif"))

# ============================================================ EG4
add("EG4", "Tableaux de bord et indicateurs de pilotage", "Économie et gestion",
S("Un tableau de bord regroupe des indicateurs permettant de piloter une activité."
  "|Un indicateur est une grandeur calculée à partir de données, comparée à un objectif."
  "|Les indicateurs de maintenance portent sur la disponibilité, la fiabilité, les coûts et les délais."
  "|Un bon indicateur est simple, fiable, calculable régulièrement et actionnable."
  "|La périodicité de mise à jour doit être adaptée au rythme de décision."
  "|Les objectifs donnent une cible chiffrée, par exemple 95 % de disponibilité."
  "|Une tendance est plus informative qu'une valeur isolée."
  "|Les seuils d'alerte définissent le moment où une action est nécessaire."
  "|Une comparaison doit porter sur une période et un périmètre identiques."
  "|Trop d'indicateurs nuise à la lisibilité et dilue l'attention."
  "|Chaque indicateur doit avoir un responsable et un usage défini."
  "|Le tableau de bord est un outil de dialogue entre maintenance, production et direction."),
[QC("Qu'est-ce qu'un indicateur ?", "Une opinion~Une grandeur calculée comparée à un objectif~Un document commercial~Une machine", 1,
     "Un indicateur transforme des données en information décisionnelle."),
 QC("Quel est un indicateur de maintenance ?", "La disponibilité~La couleur des armoires~Le nombre de fenêtres~La marque des outils", 0,
     "Disponibilité, MTBF, MTTR et coût sont des indicateurs courants."),
 QC("Quelle qualité n'est pas attendue d'un bon indicateur ?", "La simplicité~La fiabilité~L'actionnabilité~La complexité inutile", 3,
     "Un indicateur complexe et inexploitable ne sert pas au pilotage."),
 QC("Pourquoi suivre une tendance ?", "Pour voir une évolution dans le temps~Pour éviter de calculer~Pour réduire les données~Pour supprimer les objectifs", 0,
     "La dérive progressive est révélatrice d'un problème naissant."),
 QC("À quoi sert un seuil d'alerte ?", "À définir quand une action est nécessaire~À fixer le prix~À remplacer l'objectif~À masquer les données", 0,
     "Le seuil déclenche la décision ou l'investigation."),
 QC("Que faut-il pour comparer deux périodes ?", "Un périmètre et une méthode identiques~Des graphiques différents~Des unités différentes~Aucune précaution", 0,
     "Sans méthodes homogènes, la comparaison est trompeuse."),
 QC("Quel est un risque d'un tableau de bord trop chargé ?", "Trop de clarté~Une attention diluée~Moins de réunions~Une meilleure décision", 1,
     "L'excès d'indicateurs rend la lecture difficile et retarde la décision."),
 QT("Un tableau de bord affiche une disponibilité de 94 % alors que l'objectif est de 96 %. Proposer une analyse.",
    "L'écart est de 2 points, ce qui est significatif. On vérifie d'abord la méthode de calcul : période identique à l'objectif, périmètre des équipements concernés, façon de comptabiliser les arrêts planifiés. On décompose ensuite la disponibilité en MTBF et MTTR : si le MTBF a baissé, les pannes sont plus fréquentes ; si le MTTR a augmenté, la remise en état est plus lente. On croise avec les coûts et les ordres de travail de la GMAO pour identifier les équipements responsables. On définit alors une action ciblée, un objectif intermédiaire et une date de réévaluation, puis on suit la courbe de tendance.",
    "On vérifie la méthode, on décompose l'indicateur et on propose une action avec suivi."),
 QT("Pourquoi un indicateur doit-il être actionnable ?",
    "Un indicateur actionnable permet de décider ce qu'il faut faire : si le taux de pannes d'un équipement augmente, on doit pouvoir identifier l'action, la personne responsable et le délai. Un indicateur non actionnable, comme le nombre total d'heures travaillées sans lien avec un objectif, consomme du temps de collecte sans éclairer la décision. Pour être actionnable, l'indicateur doit être comprises par les équipes, calculé à partir de données fiables, comparé à une cible et accompagné d'un seuil. Il doit aussi être suivi dans le temps pour vérifier que l'action entreprise produit bien un effet.",
    "On insiste sur le lien entre mesure, décision, responsable et vérification de l'effet.")],
C("Un tableau de bord utile contient peu d'indicateurs fiables, actionnables et suivis dans le temps, avec objectifs et seuils clairs.",
  "Indicateur = donnée calculée + objectif + seuil d'alerte",
  "Disponibilité · MTBF · MTTR · coût · délais",
  "Tableau de bord~Outil de pilotage~Indicateur~Grandeur calculee~Objectif~Cible chiffree~Tendance~Evolution dans le temps~Seuil d'alerte~Declencheur d'action~Actionnable~Utile a la decision",
  "Choisir peu d'indicateurs pertinents|Fixer methodes, objectifs et seuils|Calculer à périodicité régulière|Analyser les tendances et écarts|Décider, responsabiliser et vérifier",
  "Multiplier les indicateurs|Comparer des périodes différentes|Ignorer la tendance|Laisser un indicateur sans responsable",
  "Disponibilite~94 %~Objectif~96 %~Ecart~2 points~Analyse~MTBF et MTTR~Action~Ciblee et datée",
  "Valeur isolee~Peu informative~Tendance~Evolution exploitable",
  "Indicateur fiable~Donnees propres~Indicateur actionnable~Permet de decider"))

# ============================================================ DR1
add("DR1", "Contrat de travail et droits des salariés", "Droit",
S("Le contrat de travail est une convention par laquelle une personne s'engage à travailler sous la direction d'un employeur."
  "|Il comporte une subordination juridique : l'employeur donne les ordres et contrôle l'exécution."
  "|Le contrat à durée indéterminée est la forme normale d'embauche."
  "|Le contrat à durée déterminée est prévu pour des besoins temporaires et limités dans le temps."
  "|L'apprentissage associe un contrat de travail et une formation diplômante."
  "|La période d'essai permet à l'employeur et au salarié d'évaluer la relation."
  "|Le salaire doit être au moins égal au SMIC ou à la convention collective applicable."
  "|La durée légale du travail est de 35 heures par semaine pour un temps plein."
  "|Les heures supplémentaires sont majorées ou compensées par un repos compensateur."
  "|Le salarié a droit à des congés payés et à une protection sociale."
  "|La rupture du contrat suit des règles : démission, licenciement ou rupture conventionnelle."
  "|Le licenciement doit avoir une cause réelle et sérieuse et respecter une procédure."),
[QC("Quelle est la forme normale du contrat de travail ?", "Le CDD~Le CDI~Le contrat d'intérim~Le contrat saisonnier", 1,
     "Le CDI est la forme de droit commun, le CDD étant exceptionnel."),
 QC("Quel est le critère du contrat de travail ?", "Le libre choix des horaires~La subordination juridique~Le bénéfice de l'entreprise~L'absence de salaire", 1,
     "Le pouvoir de direction et de contrôle de l'employeur caractérise le lien de subordination."),
 QC("Que garantit le SMIC ?", "Un salaire maximum~Un salaire minimum~Une prime de fin d'année~Une durée de travail", 1,
     "Le SMIC est le salaire minimum interprofessionnel de croissance."),
 QC("Quelle est la durée légale hebdomadaire ?", "30 h~35 h~39 h~40 h", 1,
     "La durée légale est de 35 heures pour un salarié à temps plein."),
 QC("Comment sont rémunérées les heures supplémentaires ?", "Au même tarif~Avec une majoration ou un repos compensateur~En nature uniquement~Elles ne sont pas comptées", 1,
     "La majoration est au moins de 25 % pour les premières heures."),
 QC("Qu'est-ce qu'une rupture conventionnelle ?", "Un licenciement discrétionnaire~Une rupture négociée entre l'employeur et le salarié~Une démission forcée~Une fin automatique", 1,
     "Elle nécessite l'accord des deux parties et une homologation."),
 QC("Que doit avoir un licenciement ?", "Une cause réelle et sérieuse~Une simple lettre~L'accord d'un collègue~Aucune procédure", 0,
     "La cause et la procédure sont encadrées par le Code du travail."),
 QT("Distinguer le contrat à durée indéterminée, le contrat à durée déterminée et le contrat d'apprentissage.",
    "Le CDI n'a pas de terme prévu : il peut durer jusqu'à la retraite et ne peut être rompu que selon des règles strictes. Le CDD comporte un terme précis et ne peut être utilisé que dans des cas autorisés, comme le remplacement d'un salarié absent ou une augmentation temporaire d'activité ; il ne peut pas pourvoir durablement un emploi lié à l'activité normale. Le contrat d'apprentissage est un CDD ou CDI spécifique qui associe l'exécution d'un travail et une formation menant à un diplôme, avec une rémunération et un tuteur. Il répond à un double objectif de qualification et d'emploi.",
    "On oppose durée, motif et finalité formatrice des trois contrats."),
 QT("Un salarié effectue régulièrement 40 heures par semaine sans majoration. Quels sont ses droits ?",
    "La durée légale étant de 35 heures, les 5 heures au-delà sont des heures supplémentaires. Elles doivent être majorées d'au moins 25 % pour les premières heures, ou faire l'objet d'un repos compensateur équivalent si un accord le prévoit. Elles doivent être décomptées par semaine, sauf dérogation, et apparaître sur le bulletin de salaire. Le salarié peut d'abord demander à l'employeur de régulariser la situation en se référant au Code du travail et à la convention collective. En l'absence de régularisation, il peut saisir l'inspection du travail ou le conseil de prud'hommes.",
    "On calcule le nombre d'heures supplémentaires, on rappelle la majoration et les voies de recours.")],
C("Le contrat de travail crée un lien de subordination et ouvre des droits : salaire, durée, congés et protection contre la rupture abusive.",
  "CDI = forme normale · CDD = besoin temporaire",
  "35 h/semaine · SMIC · heures supplémentaires majorées",
  "Contrat de travail~Lien de subordination~CDI~Sans terme~CDD~Terme precise~Apprentissage~Travail et formation~SMIC~Salaire minimum~Heures supplementaires~Au-dela de 35 h",
  "Identifier le type de contrat|Vérifier salaire et durée|Contrôler le bulletin de salaire|Repérer les écarts|Connaitre les voies de recours",
  "Confondre CDD et CDI|Ignorer les heures supplémentaires|Croire que le SMIC est un maximum|Accepter une rupture sans procédure",
  "Salarie~40 h par semaine~Legales~35 h~Supplementaires~5 h~Majoration~Au moins 25 %~Recours~Inspection du travail",
  "CDI~Durable~CDD~Temporaire",
  "Subordination~Pouvoir de direction~Independance~Absence de lien de subordination"))

# ============================================================ DR2
add("DR2", "Hygiène, sécurité et responsabilités en entreprise", "Droit",
S("L'employeur a une obligation de sécurité envers ses salariés."
  "|Il doit prendre les mesures nécessaires pour assurer leur sécurité et protéger leur santé."
  "|Le Code du travail et la convention collective fixent des règles précises."
  "|Le document unique d'évaluation des risques est obligatoire et doit être mis à jour."
  "|Le comité social et économique est informé et consulté sur les conditions de travail."
  "|Les salariés doivent respecter les consignes de sécurité et signaler les dangers."
  "|Un salarié peut refuser une tâche s'il a un motif raisonnable de penser qu'elle présente un danger grave et imminent."
  "|Ce droit de retrait ne doit pas être utilisé abusivement."
  "|Les accidents du travail et les maladies professionnelles ouvrent des droits à réparation."
  "|L'employeur doit déclarer tout accident du travail dans les délais légaux."
  "|La médecine du travail surveille l'aptitude des salariés à leur poste."
  "|Les sanctions disciplinaires doivent être proportionnées et respecter une procédure."),
[QC("Qui a une obligation de sécurité en entreprise ?", "Le salarié seulement~L'employeur~Le client~Le fournisseur", 1,
     "L'employeur doit assurer la sécurité et protéger la santé de ses salariés."),
 QC("Quel document recense les risques professionnels ?", "La facture~Le document unique d'évaluation des risques~Le devis~Le bulletin de salaire", 1,
     "Le DUERP est obligatoire et doit être révisé régulièrement."),
 QC("Quel est le rôle du CSE ?", "Fixer les prix~Être informé et consulté sur les conditions de travail~Remplacer le médecin~Diriger l'atelier", 1,
     "Le CSE intervient notamment sur la santé, la sécurité et les conditions de travail."),
 QC("Dans quel cas un salarié peut-il exercer son droit de retrait ?", "S'il est fatigué~S'il a un motif raisonnable de croire à un danger grave et imminent~S'il n'aime pas la tâche~Sans raison", 1,
     "Le danger doit être grave, imminent et raisonnablement percevable."),
 QC("Que doit faire l'employeur après un accident du travail ?", "Le cacher~Le déclarer dans les délais légaux~Attendre~Renvoyer le salarié", 1,
     "La déclaration est obligatoire, généralement sous 48 heures."),
 QC("Quel est le rôle de la médecine du travail ?", "Vendre des médicaments~Surveiller l'aptitude au poste~Fixer les salaires~Remplacer le responsable", 1,
     "Le médecin du travail vérifie l'aptitude et propose des adaptations."),
 QC("Comment doit être une sanction disciplinaire ?", "Sans procédure~Proportionnée et précédée d'une procédure~Secrète~Illimitée", 1,
     "La sanction doit être justifiée et respecter les droits de la défense."),
 QT("Un salarié constate un câble électrique dénudé et décide d'exercer son droit de retrait. Analyser la situation.",
    "Le droit de retrait est possible lorsque le salarié a un motif raisonnable de penser que la situation présente un danger grave et imminent pour sa vie ou sa santé. Un câble dénudé sous tension constitue un risque électrique réel : le salarié peut interrompre sa tâche, s'éloigner et alerter immédiatement son responsable. Il ne doit pas réparer lui-même s'il n'est pas habilité. L'employeur doit prendre les mesures pour supprimer le danger, consigner le circuit et faire intervenir une personne qualifiée. Le salarié doit pouvoir justifier sa décision par les faits observés : un retrait abusif, sans danger réel, pourrait être critiqué. Une fois le danger écarté et la consignation vérifiée, le travail reprend normalement.",
    "On vérifie les conditions du droit de retrait et on décrit la suite : alerte, consignation, reprise."),
 QT("Expliquer la répartition des responsabilités entre employeur, salarié et CSE en matière de sécurité.",
    "L'employeur porte la responsabilité principale : il évalue les risques, met en place les protections, forme les salariés et fournit les EPI. Le salarié doit respecter les consignes, utiliser correctement les protections et signaler toute situation dangereuse ; il n'est pas passif. Le CSE est un acteur de consultation : il est informé des risques, peut proposer des améliorations et être saisi en cas de danger grave et imminent. Ces responsabilités sont complémentaires : une consigne non appliquée ou un danger non signalé peuvent engager la responsabilité individuelle, tandis qu'une absence de prévention engage celle de l'employeur.",
    "On distingue obligation de moyens de l'employeur, devoirs du salarié et rôle consultatif du CSE.")],
C("La sécurité repose sur une obligation de l'employeur, des devoirs du salarié et la consultation du CSE, dans un cadre légal précis.",
  "Droit de retrait : danger grave et imminent",
  "DUERP obligatoire · accident déclaré sous 48 h",
  "Obligation de securite~Doit de l'employeur~DUERP~Evaluation des risques~CSE~Consultation~Droit de retrait~Face au danger~Signalement~Devoir du salarie~Accident du travail~Declaration obligatoire",
  "Repérer le danger|Signaler et alerter le responsable|Consigner si nécessaire|Faire intervenir une personne habilitée|Documenter et analyser",
  "Ignorer un câble dénudé|Réparer sans habilitation|Abuser du droit de retrait|Ne pas déclarer un accident",
  "Cable denude~Danger electrique~Retrait~Motif raisonnable~Alerte~Responsable~Consignation~Personne habilitee~Reprise~Apres verification",
  "Employeur~Obligation de securite~Salarie~Respect des consignes",
  "Danger grave et imminent~Retrait justifie~Simple gene~Retrait abusif"))

# ============================================================ DR3
add("DR3", "Responsabilités et secret professionnel", "Droit",
S("Une responsabilité est l'obligation de répondre de ses actes devant la loi."
  "|La responsabilité civile vise à réparer un dommage causé à autrui."
  "|La responsabilité pénale peut entraîner des sanctions comme une amende ou une peine de prison."
  "|La faute peut être une négligence, une imprudence ou une violation d'une règle."
  "|En matière de sécurité, un employeur peut être pénalement responsable d'un accident s'il a manqué à ses obligations."
  "|Le secret professionnel impose de ne pas révéler des informations confidentielles."
  "|Un technicien peut avoir accès à des données techniques, commerciales ou personnelles."
  "|La discrétion professionnelle s'applique aussi aux informations d'entreprise."
  "|La protection des données personnelles est encadrée par le RGPD."
  "|Les données doivent être collectées pour un but précis et conservées seulement le temps nécessaire."
  "|Un manquement au secret peut entraîner des sanctions disciplinaires et judiciaires."
  "|Le signalement interne d'un danger ou d'une irrégularité est protégé dans certaines conditions."),
[QC("Que vise la responsabilité civile ?", "À punir~À réparer un dommage causé à autrui~À augmenter les prix~À supprimer les contrats", 1,
     "La responsabilité civile déclenche une réparation, souvent financière."),
 QC("Quelle sanction relève de la responsabilité pénale ?", "Une remise à l'ordre~Une amende ou une peine de prison~Une augmentation de salaire~Un congé", 1,
     "Les sanctions pénales sont prévues par la loi."),
 QC("Qu'est-ce qu'une faute ?", "Une action conforme~Une négligence ou une violation de règle~Un simple avis~Une réussite", 1,
     "La faute peut être intentionnelle ou résulter d'une imprudence."),
 QC("Que impose le secret professionnel ?", "De tout raconter~De ne pas révéler d'informations confidentielles~De vendre des données~D'ignorer les consignes", 1,
     "La confidentialité protège les personnes et les entreprises."),
 QC("Que régit le RGPD ?", "La protection des données personnelles~Le prix des pièces~La durée du travail~Les contrats d'achat", 0,
     "Le règlement général sur la protection des données encadre les traitements de données."),
 QC("Combien de temps conserver des données personnelles ?", "Toujours~Le temps nécessaire à la finalité poursuivie~Un siècle~Aucune limite", 1,
     "Le principe de minimisation impose une durée de conservation limitée."),
 QC("Le signalement interne d'un danger est-il protégé ?", "Jamais~Oui, dans certaines conditions~Toujours sans cadre~Uniquement par la presse", 1,
     "La loi protège le lanceur d'alerte qui respecte la procédure."),
 QT("Un technicien découvre des données clients sur un poste non sécurisé. Quelles sont ses obligations ?",
    "Il ne doit ni copier ni diffuser ces données, même par curiosité. Il signale immédiatement la situation à son responsable hiérarchique ou au délégué à la protection des données, en décrivant précisément ce qu'il a constaté sans transmettre les données elles-mêmes. Il évite de modifier ou supprimer les fichiers, car la preuve doit être préservée. Si un risque pour les personnes est imminent, il utilise la procédure de signalement interne prévue. L'entreprise doit ensuite sécuriser le poste, vérifier qui a eu accès aux données et, si nécessaire, notifier l'autorité de contrôle. La discrétion du technicien est une obligation professionnelle, mais elle ne doit pas empêcher le signalement d'une faille.",
    "On attend absence de diffusion, signalement, préservation des preuves et protection des données."),
 QT("Expliquer la différence entre responsabilité civile et responsabilité pénale dans le cas d'un accident causé par une négligence.",
    "La responsabilité civile concerne la réparation du dommage : si une négligence provoque une panne et un préjudice à un client, l'entreprise ou la personne concernée peut être condamnée à verser des dommages-intérêts. La responsabilité pénale concerne la violation d'une règle de droit : si la négligence consiste à avoir ignoré une consigne de sécurité alors qu'une vie était en danger, des sanctions pénales peuvent être prononcées contre les personnes physiques responsables. Les deux responsabilités peuvent être engagées en même temps : l'une répare, l'autre punit. C'est pourquoi le respect des procédures et la traçabilité des interventions sont essentiels.",
    "On oppose réparation et sanction, avec un exemple d'accident.")],
C("La responsabilité engage celui qui commet une faute : civile pour réparer, pénale pour sanctionner ; la confidentialité protège les données.",
  "Responsabilité civile = réparation · responsabilité pénale = sanction",
  "RGPD : finalité précise et durée limitée",
  "Responsabilite civile~Reparer le dommage~Responsabilite penale~Sanction prevue par la loi~Faute~Negligence ou imprudence~Secret professionnel~Confidentialite~RGPD~Donnees personnelles~Signalement~Alerte interne",
  "Identifier les données et leur sensibilité|Ne pas les diffuser|Signaler au responsable ou au DPO|Préserver les éléments de preuve|Documenter la situation",
  "Copier des données confidentielles|Révéler des informations clients|Supprimer des preuves|Confondre discrétion et silence en cas de danger",
  "Donnees clients~Poste non securise~Action~Signalement~Responsable~Alerte interne~RGPD~Finalite et duree~Sanction~Disciplinaire ou penale",
  "Civile~Reparation~Penale~Sanction",
  "Secret~Ne pas reveler~Signalement~Informer la bonne personne"))

# ============================================================ AT1
add("AT1", "Vocabulaire technique de la maintenance en anglais", "Anglais technique",
S("Technical English uses precise words for tools, actions and failures."
  "|A fault is a defect; a failure is the loss of the required function."
  "|To troubleshoot means to find the cause of a problem."
  "|Preventive maintenance is carried out before a failure occurs."
  "|Corrective maintenance is carried out after a failure is detected."
  "|A spare part is a component kept in stock for replacement."
  "|To wear out means to become unusable through use."
  "|A leak is an unintended escape of fluid or gas."
  "|Overheating means a temperature higher than the allowed limit."
  "|To tighten a bolt means to increase its tightening torque."
  "|A service interval is the time between two scheduled maintenance actions."
  "|Learning word families, such as to fail, a failure and faulty, improves technical reading."),
[QC("What is a fault ?", "A correct function~A defect~A spare part~A maintenance plan", 1,
     "A fault is a defect or an imperfection in a component."),
 QC("What does to troubleshoot mean ?", "To repair immediately~To find the cause of a problem~To clean a machine~To buy a spare part", 1,
     "Troubleshooting is the diagnostic phase of corrective maintenance."),
 QC("When is preventive maintenance carried out ?", "After a failure~Before a failure~Only at night~Never", 1,
     "Preventive maintenance acts before the failure occurs."),
 QC("What is a spare part ?", "A tool~A component kept in stock for replacement~A report~A safety rule", 1,
     "Spare parts are stored to reduce downtime."),
 QC("What does overheating mean ?", "A temperature below the limit~A temperature above the allowed limit~A normal pressure~A low vibration", 1,
     "Overheating is a temperature above the allowed limit."),
 QC("What does to tighten mean ?", "To loosen a bolt~To increase the tightening torque~To measure a voltage~To replace a filter", 1,
     "Tightening increases the torque applied to a fastener."),
 QC("What is a service interval ?", "The time between two scheduled actions~The price of a service~The size of a machine~The name of a tool", 0,
     "A service interval is the period between two planned maintenance actions."),
 QT("Translate into English: 'La panne a été détectée grâce à une vibration anormale ; le roulement est usé.'",
    "The failure was detected thanks to an abnormal vibration; the bearing is worn out. Failure names the loss of function, vibration is the measured symptom, and worn out describes the state of the bearing. The passive form was detected is common in technical reports because the important information is the event, not the person who observed it.",
    "Distinguish failure, symptom and component state; use the passive form."),
 QT("Explain the difference between a fault and a failure with a bearing example.",
    "A fault is a defect or an abnormal condition, for example a small crack in a bearing race or insufficient lubrication. A failure is the loss of the required function: the bearing no longer allows the shaft to rotate correctly and the machine stops. A fault can exist for some time without causing a failure, especially if it is detected by condition monitoring. Maintenance aims to detect faults early, through vibration or temperature measurements, so that action can be taken before the fault becomes a failure.",
    "Show that a fault is an abnormal state and a failure is the loss of function.")],
C("Technical English distinguishes the defect, the symptom and the loss of function: the right word makes a report precise.",
  "Fault = defect · failure = loss of function",
  "Preventive before failure · corrective after failure",
  "Fault~Defaut~Failure~Perte de fonction~Troubleshooting~Recherche de cause~Spare part~Piece de rechange~Worn out~Use~Overheating~Surchauffe",
  "Identify the object and the action|Choose the precise technical word|Use the active or passive form correctly|Add measurements and units|Check the spelling of word families",
  "Confusing fault and failure|Using to loosen for to tighten|Forgetting the unit in a measurement|Translating word for word",
  "Bearing~Roulement~Vibration~Symptom~Failure~Machine stop~Spare~In stock~Torque~25 N.m",
  "Fault~Defect before stop~Failure~Function lost",
  "Preventive~Before~Corrective~After"))

# ============================================================ AT2
add("AT2", "Lire une notice technique et une plaque signalétique", "Anglais technique",
S("A nameplate gives the main characteristics of a machine or a component."
  "|Typical nameplate data include voltage, current, frequency, power, speed and insulation class."
  "|The abbreviation kW means kilowatt and rpm means revolutions per minute."
  "|A rated value is the value for which the equipment is designed."
  "|A manual usually contains sections such as safety, installation, operation, maintenance and troubleshooting."
  "|Warnings are introduced by Danger, Warning or Caution, depending on the level of risk."
  "|Danger indicates an immediate hazard that will cause death or serious injury."
  "|Warning indicates a potentially hazardous situation that could cause serious injury."
  "|Caution indicates a situation that could cause minor injury or equipment damage."
  "|A torque value is given in newton metres, written Nm or N.m."
  "|A service interval may be expressed in operating hours or in months."
  "|Always check the manual edition and the serial number before ordering a spare part."),
[QC("What does rpm mean ?", "Revolutions per minute~Repairs per month~Rated power maximum~Resistance per metre", 0,
     "rpm is revolutions per minute, the unit of rotational speed."),
 QC("What does a nameplate provide ?", "The price of the machine~The main rated characteristics~The name of the operator~The date of the next holiday", 1,
     "Voltage, current, power and speed are typical nameplate data."),
 QC("Which warning indicates an immediate hazard causing death ?", "Caution~Warning~Danger~Note", 2,
     "Danger is used for an immediate hazard with severe consequences."),
 QC("What is a rated value ?", "The maximum measured value~The value for which the equipment is designed~A random value~The value after failure", 1,
     "Rated values define the normal operating conditions."),
 QC("In which unit is a torque expressed ?", "Volt~Newton metre~Joule~Hertz", 1,
     "Torque is force times distance, in N.m."),
 QC("What is the purpose of a troubleshooting section ?", "To list prices~To help find and solve problems~To describe the company~To give the delivery time", 1,
     "Troubleshooting guides the diagnostic process."),
 QC("Why check the serial number ?", "For decoration~To identify the exact version of the equipment~To increase power~To change the voltage", 1,
     "The serial number ensures the right part and manual are used."),
 QT("A motor nameplate reads: 400 V, 50 Hz, 4 kW, 1440 rpm, class F. Interpret each value.",
    "400 V is the rated supply voltage between phases; 50 Hz is the rated frequency of the network; 4 kW is the rated mechanical output power; 1440 rpm is the rated speed under normal load, slightly below the synchronous speed of 1500 rpm for a four-pole motor; class F is the insulation class, which indicates the maximum allowable winding temperature. These values are used to check the supply, to select the protection devices and to verify that the motor operates within its nominal conditions.",
    "Give the meaning and the practical use of every nameplate value."),
 QT("Explain why the warning words Danger, Warning and Caution must not be translated loosely in a manual.",
    "These three words form a legal and safety hierarchy. Danger means an immediate hazard that will cause death or serious injury if not avoided. Warning means a potentially hazardous situation that could cause serious injury. Caution means a situation that could cause minor injury or damage to equipment. If a translator uses a weaker word for Danger, the reader may underestimate the risk and remove a guard while the machine is live. Safety messages must therefore keep their precise level, together with the required PPE and the consequence of ignoring the instruction.",
    "Define the hierarchy and explain the consequence of an inaccurate translation.")],
C("A manual and a nameplate give the rated values and the safety level: read them before intervening or ordering a part.",
  "Rated values = design conditions",
  "Danger > Warning > Caution",
  "Nameplate~Plaque signaletique~Rated value~Valeur nominale~Manual~Notice~Warning~Avertissement~Danger~Danger immediat~Torque~Newton metre",
  "Identify the equipment and serial number|Read the rated values|Locate the safety section|Find the maintenance interval|Order the correct part",
  "Ignoring the edition of the manual|Confusing Warning and Danger|Using a part from another serial number|Forgetting to convert units",
  "Motor~400 V, 50 Hz, 4 kW~Speed~1440 rpm~Insulation~Class F~Torque~25 N.m~Interval~2000 h",
  "Danger~Hazard immediate~Warning~Potential hazard",
  "Manual~Notice~Nameplate~Plaque"))

# ============================================================ AT3
add("AT3", "Rédiger un compte rendu et un e-mail technique", "Anglais technique",
S("A technical report and an e-mail must be clear, factual and concise."
  "|Start an e-mail with a subject line that states the machine and the problem."
  "|State the purpose of the message in the first sentence."
  "|Describe the symptoms with measured values and units."
  "|Use the past simple for completed actions and the present perfect for recent results with a present consequence."
  "|The passive voice is common: the belt was replaced, the sensor was calibrated."
  "|List the actions taken in chronological order."
  "|Give the current status and any remaining risk."
  "|Ask a clear question or state the decision expected from the reader."
  "|Close with a professional formula such as Kind regards."
  "|Avoid slang, humour and vague expressions such as it is better now."
  "|Check spelling, units and the attachment before sending."),
[QC("What should the subject line contain ?", "A joke~The machine and the problem~The name of the sender~Only the date", 1,
     "The subject line allows the reader to identify the issue immediately."),
 QC("Which tense is used for a completed action ?", "Present simple~Past simple~Future~Present continuous", 1,
     "The past simple reports completed actions at a definite time."),
 QC("What does 'the belt was replaced' use ?", "The active voice~The passive voice~The imperative~The conditional", 1,
     "The passive focuses on the action and the equipment rather than the person."),
 QC("How should a symptom be described ?", "With vague words~With measured values and units~With humour~With a long story", 1,
     "Measurements make the report verifiable."),
 QC("What is a professional closing ?", "Bye~Kind regards~See you~Later", 1,
     "Kind regards is a standard formal closing."),
 QC("What should you avoid in a technical e-mail ?", "Units~Slang and vague expressions~Dates~Measurements", 1,
     "Technical writing must stay factual and precise."),
 QC("What should be checked before sending ?", "Only the spelling of the first word~Spelling, units and attachments~The colour of the screen~The weather", 1,
     "A final check prevents avoidable mistakes."),
 QT("Write a short e-mail to report that pump P2 was repaired and restarted after a seal replacement.",
    "Subject: Pump P2 - seal replacement completed. Dear Sir or Madam, I am writing to confirm that pump P2 in workshop 3 was repaired on 14 March. The mechanical seal was replaced and the cooling circuit was refilled. After a 30-minute test, the flow rate was 12 m³/h and the temperature was 62 °C, which is within the normal range. The pump is now back in service, and no further problem was observed. Please let me know if you require the full report. Kind regards, [Name].",
    "Include a subject, the past simple, passive forms, measurements, status and a formal closing."),
 QT("Explain why 'it is better now' should not appear in a technical report.",
    "The expression gives no measurable information: it does not say what changed, by how much, under which conditions or compared to which reference. A colleague cannot verify it, and the GMAO cannot use it as a reliable history. A technical report must replace it with a measurement and a comparison, for example: vibration decreased from 4,8 mm/s to 2,1 mm/s after balancing, measured at 1500 rpm under normal load. This formulation is factual, repeatable and useful for future diagnosis. Clear reports also reduce misunderstandings between sites and between the maintenance and production teams.",
    "Point out the lack of measurement and propose a precise reformulation.")],
C("A technical e-mail states the issue, the facts, the actions and the status in concise language with correct units.",
  "Subject + purpose + facts + actions + status + closing",
  "Past simple for actions · passive for equipment-focused statements",
  "Subject line~Objet du message~Past simple~Actions terminees~Passive voice~Action mise en avant~Measurement~Valeur et unité~Status~Etat actuel~Kind regards~Formule de politesse",
  "Write a clear subject|State the purpose immediately|Give facts and measurements|List actions and current status|Check spelling and attachments",
  "Using vague expressions|Omitting units|Writing a long informal message|Forgetting the attachment",
  "Subject~Pump P2 repaired~Test~30 min at 12 m³/h~Temperature~62 °C~Status~Back in service~Closing~Kind regards",
  "Active~The technician replaced the seal~Passive~The seal was replaced",
  "Better now~Vague~2,1 mm/s after balancing~Precis"))

# ============================================================ DD1
add("DD1", "Efficacité énergétique et sobriété en atelier", "Développement durable",
S("L'efficacité énergétique consiste à obtenir le même service avec moins d'énergie."
  "|La sobriété énergétique vise à réduire les besoins eux-mêmes, pas seulement les pertes."
  "|Les postes de consommation d'un atelier sont les moteurs, le chauffage, l'éclairage et l'air comprimé."
  "|L'air comprimé est souvent une source de gaspillage : une fuite de 1 mm peut coûter cher par an."
  "|Un compresseur bien entretenu et un réseau sans fuite réduisent la consommation électrique."
  "|Le variateur de fréquence adapte la vitesse des moteurs au besoin réel."
  "|L'isolation des conduites et des bâtiments limite les pertes thermiques."
  "|Un éclairage LED et une gestion par détecteur réduisent la consommation d'éclairage."
  "|Le suivi des consommations permet de repérer les dérives et de vérifier les économies."
  "|Un bilan énergétique compare l'énergie consommée à la production réalisée."
  "|Les investissements énergétiques sont rentables si le gain annuel couvre l'investissement en quelques années."
  "|La sobriété concerne aussi les déplacements, le chauffage et l'usage raisonnable de la climatisation."),
[QC("Que vise l'efficacité énergétique ?", "À consommer plus~À obtenir le même service avec moins d'énergie~À arrêter la production~À augmenter la température", 1,
     "L'efficacité agit sur le rendement, la sobriété agit sur le besoin."),
 QC("Quelle est une source fréquente de gaspillage en atelier ?", "Une fuite d'air comprimé~Un moteur bien dimensionné~Un éclairage LED~Une isolation correcte", 0,
     "Les fuites d'air comprimé sont souvent invisibles et coûteuses."),
 QC("Comment un variateur réduit-il la consommation ?", "En augmentant la tension~En adaptant la vitesse au besoin~En supprimant le glissement~En chauffant le moteur", 1,
     "La puissance d'une ventilation varie environ comme le cube de la vitesse."),
 QC("Que permet un suivi des consommations ?", "De repérer les dérives~D'augmenter les prix~De supprimer la maintenance~De cacher les données", 0,
     "La mesure est la condition de l'action."),
 QC("Quel est un effet de l'isolation thermique ?", "Augmenter les pertes~Limiter les pertes de chaleur~Augmenter la consommation~Changer la fréquence", 1,
     "L'isolation réduit les besoins de chauffage et de refroidissement."),
 QC("Quand un investissement énergétique est-il rentable ?", "Immédiatement toujours~Quand les économies annuelles remboursent l'investissement~Jamais~Uniquement s'il est subventionné", 1,
     "Le temps de retour est un critère classique d'arbitrage."),
 QC("La sobriété concerne-t-elle seulement l'industrie ?", "Oui~Non, elle concerne aussi les déplacements et le chauffage~Seulement les usines~Seulement les transports", 1,
     "La sobriété est une question de modes de consommation dans tous les secteurs."),
 QT("Une fuite d'air comprimé de 1 mm entraîne une perte de 0,5 kW en continu. Calculer le coût annuel pour 6000 h de fonctionnement à 0,12 €/kWh.",
    "L'énergie perdue vaut 0,5 kW x 6000 h = 3000 kWh par an. Le coût annuel est de 3000 x 0,12 = 360 €. Une simple détection de fuite et son élimination permettent donc d'économiser cette somme chaque année, pour un coût de détection très faible. Cet exemple montre pourquoi la recherche de fuites fait partie de la maintenance énergétique courante : l'air comprimé est un fluide coûteux à produire et souvent mal surveillé.",
    "On calcule l'énergie perdue puis le coût, avec un commentaire sur la rentabilité de l'action."),
 QT("Distinguer efficacité énergétique et sobriété et donner un exemple de chaque dans un atelier.",
    "L'efficacité énergétique réduit l'énergie nécessaire à un service identique : remplacer un moteur IE1 par un moteur IE4, installer un variateur sur une ventilation ou réparer une fuite d'air comprimé. La sobriété réduit le besoin lui-même : éteindre l'éclairage et la ventilation des zones inoccupées, limiter la température de consigne du chauffage, mutualiser les déplacements ou éviter de fonctionner à vide. L'efficacité agit sur le rendement technique, la sobriété agit sur les usages et les comportements. Les deux sont complémentaires : un équipement très efficace mais inutilement allumé consomme encore de l'énergie.",
    "On définit les deux notions et on donne au moins un exemple technique et un exemple comportemental.")],
C("Économiser l'énergie combine efficacité technique et sobriété d'usage : mesurer, repérer les fuites, adapter les besoins.",
  "Coût annuel = puissance perdue x heures x prix du kWh",
  "Efficacité : moins d'énergie pour le même service · sobriété : moins de besoin",
  "Efficacite~Moins d'energie~Sobriete~Moins de besoin~Air comprime~Fluide couteux~Variateur~Vitesse ajustee~Fuite~Gaspillage~Bilan energetique~Consommation sur production~Temps de retour~Rentabilite",
  "Mesurer les consommations par poste|Repérer les fuites et les dysfonctionnements|Agir sur les réglages et l'isolation|Suivre les économies réalisées|Sensibiliser les utilisateurs",
  "Ignorer les fuites d'air|Surchauffer les locaux|Laisser les machines tourner à vide|Ne pas mesurer avant d'agir",
  "Fuite~0,5 kW en continu~6000 h~3000 kWh~Prix~0,12 €/kWh~Cout annuel~360 €~Action~Detection de fuite",
  "Efficacite~Rendement~Sobriete~Usage",
  "Avant action~Consommation de reference~Apres action~Economie mesuree"))

# ============================================================ DD2
add("DD2", "Gestion des déchets et recyclage en maintenance", "Développement durable",
S("Un déchet est tout objet ou substance dont son détenteur se défait."
  "|Les déchets industriels se classent en déchets non dangereux et déchets dangereux."
  "|Les huiles usagées, les solvants, les piles et les tubes fluorescents sont des déchets dangereux."
  "|Un déchet dangereux ne doit jamais être mélangé avec les ordures ménagères."
  "|Chaque déchet dangereux est identifié par un code dans la nomenclature officielle."
  "|Le tri à la source facilite la valorisation et réduit les coûts de traitement."
  "|La hiérarchie de gestion privilégie la réduction, la réutilisation, puis le recyclage."
  "|L'incinération avec récupération d'énergie et l'enfouissement sont les solutions de dernier rang."
  "|Les emballages et les pièces métalliques sont souvent recyclables."
  "|Un bordereau de suivi accompagne les déchets dangereux jusqu'à leur traitement."
  "|La traçabilité protège l'entreprise en cas de contrôle ou de pollution."
  "|Une bonne gestion des déchets contribue aussi à la sécurité et à la propreté de l'atelier."),
[QC("Quel est un déchet dangereux ?", "Un carton propre~Une huile usagée~Une pièce métallique propre~Un emballage plastique vide", 1,
     "L'huile usagée est classée dangereuse et nécessite une filière spécifique."),
 QC("Que faut-il faire d'un déchet dangereux ?", "Le jeter dans la poubelle~Le trier à part et le confier à une filière agréée~Le brûler~Le mélanger aux métaux", 1,
     "Le mélange interdit souvent toute valorisation ultérieure."),
 QC("Quel document accompagne un déchet dangereux ?", "Un bon de commande~Un bordereau de suivi~Une facture~Un plan de maintenance", 1,
     "Le bordereau de suivi garantit la traçabilité jusqu'au traitement."),
 QC("Quel est le premier rang de la hiérarchie de gestion ?", "Le recyclage~La réduction à la source~L'enfouissement~L'incinération", 1,
     "Le meilleur déchet est celui que l'on ne produit pas."),
 QC("Que signifie trier à la source ?", "Trier après mélange~Séparer les déchets là où ils sont produits~Tout mélanger~Trier une fois par an", 1,
     "Le tri à la source préserve la qualité des matières recyclables."),
 QC("Quel déchet est généralement recyclable ?", "Une pile usagée~Un métal propre~Un solvant~Un tube fluorescent", 1,
     "Les métaux sont valorisables après tri et compactage."),
 QC("Pourquoi conserver les bordereaux ?", "Pour décorer~Pour prouver la traçabilité en cas de contrôle~Pour augmenter les déchets~Pour ne rien faire", 1,
     "Ils constituent la preuve d'une gestion conforme."),
 QT("Décrire la procédure de gestion des huiles usagées après une vidange de réducteur.",
    "On prépare un récipient étanche et étiqueté, compatible avec l'huile et muni d'un couvercle. On vidange à froid ou tiède selon la procédure, en évitant tout déversement au sol ; les gants et les lunettes sont portés. On transvase l'huile dans le récipient dédié aux huiles usagées, sans la mélanger avec d'autres fluides ou avec l'eau. On note la date, l'équipement, la quantité et le type d'huile sur le registre. Le récipient est ensuite stocké sur une rétention, à l'abri de la pluie, puis enlevé par un prestataire agréé qui fournit un bordereau de suivi. On conserve ce bordereau et on nettoie la zone de travail.",
    "On attend récipient adapté, absence de mélange, étiquetage, registre, prestataire agréé et bordereau."),
 QT("Expliquer pourquoi le tri à la source est plus efficace qu'un tri après mélange.",
    "Au moment de la production du déchet, on sait encore exactement ce qu'il est et d'où il vient. Un métal propre peut être recyclé directement, alors qu'un métal mélangé à des solvants ou à d'autres déchets devient dangereux et coûteux à traiter. Le tri à la source préserve la qualité des matières, augmente leur valeur de reprise et réduit les quantités envoyées en décharge. Il demande peu de moyens : des bacs identifiés, une formation courte et une vérification régulière. Un tri tardif, lui, exige des installations complexes et donne souvent des matières de mauvaise qualité, difficilement valorisables.",
    "On insiste sur la connaissance du déchet, la qualité de la matière et les coûts évités.")],
C("Bien gérer les déchets commence sur le lieu de production : trier, étiqueter, tracer et confier à une filière agréée.",
  "Hiérarchie : réduire · réutiliser · recycler · traiter",
  "Déchet dangereux = bordereau de suivi + filière agréée",
  "Dechet~Objet dont on se.defait~Dechet dangereux~Huile, solvant, pile~Tri a la source~Separation au depart~Bordereau~Tracabilite~Recyclage~Valorisation~R-etention~Stockage securise",
  "Identifier la nature du déchet|Choisir le contenant adapté|Trier et étiqueter sans mélanger|Stocker sur rétention|Confier à un prestataire et archiver",
  "Mélanger huile et solvants|Jeter une pile avec les ordures|Laisser un fût sans étiquette|Perdre le bordereau de suivi",
  "Huile usee~Vidange reducteur~Contenant~Etanche et etiquete~Registre~Date et quantite~Prestataire~Filiere agreee~Bordereau~Archive",
  "Dechet dangereux~Filiere specific~Dechet ordinaire~Filiere classique",
  "Tri a la source~Matiere propre~Tri tardif~Matiere degradee"))

# ============================================================ DD3
add("DD3", "Réglementation environnementale et produits chimiques", "Développement durable",
S("L'activité industrielle est encadrée par des réglementations environnementales."
  "|Les installations classées pour la protection de l'environnement sont soumises à autorisation ou à déclaration."
  "|L'exploitant doit respecter des prescriptions techniques et déclarer certains incidents."
  "|La réglementation ICPE s'applique notamment aux stockages et aux rejets."
  "|Le règlement REACH encadre la fabrication, l'importation et l'usage des substances chimiques."
  "|Une substance très préoccupante peut être soumise à autorisation ou à restriction."
  "|La fiche de données de sécurité accompagne tout produit chimique dangereux."
  "|La FDS compporte seize rubriques, dont l'identification, les risques et les mesures de protection."
  "|Les pictogrammes et les mentions de danger informent sur les risques du produit."
  "|La protection de l'eau impose d'éviter tout rejet d'huile ou de solvant dans les égouts."
  "|Les bacs de rétention et les séparateurs d'hydrocarbures limitent les pollutions accidentelles."
  "|Le respect de la réglementation est une responsabilité de l'entreprise et de chaque utilisateur."),
[QC("Que régit le règlement REACH ?", "Les salaires~Les substances chimiques~Les horaires~Les prix", 1,
     "REACH encadre l'enregistrement, l'évaluation et l'autorisation des substances chimiques."),
 QC("Quel document accompagne un produit chimique dangereux ?", "La facture~La fiche de données de sécurité~Le devis~Le contrat", 1,
     "La FDS est obligatoire et comporte seize rubriques."),
 QC("Combien de rubriques comporte une FDS ?", "6~10~16~20", 2,
     "La fiche de données de sécurité suit un format harmonisé de seize rubriques."),
 QC("Que signalent les pictogrammes sur un bidon ?", "Le prix~Les risques du produit~La date de fabrication~Le fournisseur", 1,
     "Les pictogrammes GHS et les mentions de danger informent sur les risques."),
 QC("Que faut-il faire avec une huile usagée ?", "La verser dans l'évier~La collecter séparément~La brûler sur place~La diluer", 1,
     "Tout rejet dans les égouts est interdit et polluant."),
 QC("À quoi sert un bac de rétention ?", "À ranger les outils~À contenir les fuites et éviter la pollution~À chauffer le local~À mesurer la température", 1,
     "Il retient les liquides en cas de fuite ou de débordement."),
 QC("Quelle est une obligation d'un exploitant d'ICPE ?", "Respecter des prescriptions et déclarer certains incidents~Vendre plus~Supprimer la FDS~Ignorer les rejets", 0,
     "Les installations classées sont soumises à des exigences et à une déclaration d'incidents."),
 QT("Expliquer l'utilité de la fiche de données de sécurité (FDS) pour un technicien de maintenance.",
    "La FDS est la source d'information officielle sur un produit chimique. Elle indique l'identification du produit, ses dangers, sa composition, les premiers secours, les mesures de lutte contre l'incendie, les précautions de manipulation et de stockage, les EPI nécessaires, les propriétés physico-chimiques et les informations relatives à l'élimination. Avant d'utiliser un solvant ou un dégraissant, le technicien consulte la FDS pour choisir les gants et les lunettes adaptés, connaître les incompatibilités et savoir comment réagir en cas de projection. La FDS doit être accessible à tous les utilisateurs et tenue à jour.",
    "On cite quelques rubriques clés et l'usage concret pour la sécurité et l'élimination."),
 QT("Un fût de solvant fuit dans un local disposant d'un bac de rétention. Décrire la conduite à tenir.",
    "On alerte immédiatement le responsable et on éloigne les sources d'ignition, car de nombreux solvants sont inflammables. On porte les EPI indiqués par la FDS : gants adaptés, lunettes et éventuellement protection respiratoire. On colmate ou déplace le fût si cela peut être fait sans risque, puis on contient le liquide avec des absorbants ou des barrages, sans le laisser rejoindre les égouts. On récupère le solvant et les absorbants dans un conteneur étiqueté comme déchet dangereux, puis on nettoie la surface selon la FDS. On vérifie que le bac de rétention n'a pas débordé, on aère le local et on consigne l'incident avec la quantité estimée et les actions menées.",
    "On attend alerte, suppression des sources d'ignition, EPI, confinement, collecte et traçabilité.")],
C("La conformité environnementale repose sur la connaissance des produits, la FDS, la rétention et la traçabilité des incidents.",
  "REACH : substances chimiques · ICPE : installations",
  "FDS = 16 rubriques · jamais de rejet dans les égouts",
  "REACH~Reglement des substances~ICPE~Installations classees~FDS~Fiche de securite~Pictogramme~Signal de danger~Retention~Contenir les fuites~Rejet~Pollution interdite",
  "Identifier le produit et consulter la FDS|Porter les EPI prescrits|Vérifier stockage et rétention|Agir en cas de fuite sans risque|Consigner et déclarer l'incident",
  "Verser un solvant à l'égout|Ignorer les pictogrammes|Stocker sans rétention|Ne pas déclarer un débordement",
  "Fut de solvant~Fuite~Ignition~A éloigner~FDS~EPI a porter~Absorbant~Contenir~Dechet~Conteneur etiquete~Declaration~Incident consigne",
  "REACH~Substances~ICPE~Installations",
  "FDS~Information complete~Etiquette~Signal rapide"))

# ============================================================ DD4
add("DD4", "Développement durable et responsabilité des entreprises", "Développement durable",
S("Le développement durable répond aux besoins du présent sans compromettre les générations futures."
  "|Il repose sur trois piliers : économique, social et environnemental."
  "|La responsabilité sociétale des entreprises, ou RSE, intègre ces préoccupations dans la stratégie."
  "|Une démarche RSE concerne les salariés, les clients, les fournisseurs et le territoire."
  "|La maintenance contribue au pilier environnemental par la durée de vie des équipements."
  "|Allonger la durée de vie d'une machine réduit la consommation de matières premières."
  "|La réparabilité et la disponibilité des pièces sont des enjeux de sobriété."
  "|Le pilier social comprend la santé, la sécurité, la formation et l'égalité de traitement."
  "|Le pilier économique suppose une activité rentable et des prix honnêtes."
  "|Les objectifs de développement durable sont un cadre international de référence."
  "|Une entreprise publie souvent un rapport RSE avec des indicateurs et des objectifs."
  "|Chaque salarié contribue par ses gestes : tri, économies, sécurité et signalement."),
[QC("Combien de piliers compte le développement durable ?", "Deux~Trois~Quatre~Cinq", 1,
     "Les piliers sont économique, social et environnemental."),
 QC("Que signifie RSE ?", "Réglementation sociale européenne~Responsabilité sociétale des entreprises~Réseau de sécurité entreprise~Rendement social estimé", 1,
     "La RSE intègre les enjeux sociaux et environnementaux dans la stratégie."),
 QC("Quel est un enjeu environnemental de la maintenance ?", "Allonger la durée de vie des équipements~Augmenter les rejets~Réduire la formation~Supprimer le tri", 0,
     "Réparer plutôt que remplacer économise des matières premières."),
 QC("Quel thème relève du pilier social ?", "La santé et la sécurité~Le prix des pièces~La consommation d'énergie~Le chiffre d'affaires", 0,
     "Santé, sécurité, formation et égalité appartiennent au pilier social."),
 QC("Que contient généralement un rapport RSE ?", "Des indicateurs et des objectifs~Seulement les salaires~Les coordonnées des clients~Le prix de l'action", 0,
     "Le rapport rend compte des engagements et des résultats."),
 QC("Les objectifs de développement durable sont...", "Un cadre international~Une loi francaise uniquement~Un label publicitaire~Une norme comptable", 0,
     "Les ODD ont été adoptés par les Nations unies dans l'agenda 2030."),
 QC("Comment un technicien contribue-t-il à la RSE ?", "Par des gestes quotidiens de tri et d'économie~En ignorant les consignes~En augmentant les déchets~En refusant la formation", 0,
     "Les comportements individuels s'inscrivent dans la démarche collective."),
 QT("Expliquer comment la maintenance participe au développement durable dans une entreprise industrielle.",
    "La maintenance agit sur les trois piliers. Sur le plan environnemental, elle allonge la durée de vie des équipements, réduit les consommations d'énergie par un meilleur rendement, limite les fuites et les pollutions et organise le recyclage des pièces et des huiles. Sur le plan économique, elle réduit les arrêts de production et les achats de remplacement, ce qui améliore la compétitivité. Sur le plan social, elle assure la sécurité des installations, la formation des techniciens et la transmission des compétences. Un service maintenance qui documente ses interventions et suit des indicateurs fournit des preuves utiles au rapport RSE de l'entreprise.",
    "On traite les trois piliers avec un exemple concret pour chacun."),
 QT("Une entreprise souhaite améliorer sa démarche RSE. Proposer trois actions réalistes pour un atelier de maintenance.",
    "Premièrement, mettre en place un suivi des consommations d'énergie et d'air comprimé avec détection des fuites, objectif chiffré et relevé mensuel : c'est une action environnementale et économique. Deuxièmement, organiser le tri des déchets avec des bacs identifiés, des bordereaux de suivi pour les huiles et une formation courte des équipes, ce qui améliore la sécurité et la traçabilité. Troisièmement, planifier la formation continue des techniciens sur les nouveaux équipements et la consignation électrique, action sociale qui renforce les compétences et la sécurité. Chaque action doit avoir un responsable, un indicateur et une date de réévaluation pour être crédible dans le rapport RSE.",
    "On propose trois actions couvrant au moins deux piliers, avec responsable et indicateur.")],
C("Le développement durable associe économie, social et environnement : la maintenance y contribue par la durée de vie, la sécurité et la sobriété.",
  "Développement durable = présent + générations futures",
  "3 piliers : économique · social · environnemental",
  "Developpement durable~Present et futur~RSE~Responsabilite des entreprises~Pilier economique~Rentabilite~Pilier social~Sante et formation~Pilier environnemental~Ressources~ODD~Objectifs mondiaux",
  "Identifier les enjeux par pilier|Choisir des actions concretes|Nommer un responsable et un indicateur|Suivre les resultats dans le temps|Communiquer de maniere transparente",
  "Réduire la RSE à la publicité|Ignorer le pilier social|Ne pas mesurer les résultats|Laisser une action sans responsable",
  "Maintenance~Prolonge la vie des machines~Energie~Suivi et fuite~Dechets~Tri et bordereaux~Social~Formation et securite~RSE~Rapport annuel",
  "Pilier social~Personnes~Pilier environnemental~Ressources",
  "RSE~Engagement voluntarie~Obligation legale~Cadre contraignant"))

# FIN DES LOTS
valider_et_ecrire(F, "pro-maintenance-mat-part-C.json")
