# -*- coding: utf-8 -*-
"""Generateur pro-electricite-mat-part-B.json — lot B : Electrotechnique (20 fiches).

Lois electriques, machines, moteurs, transformateurs, physique appliquee,
schemas et normes electriques. Chaque fiche : 12 points, 9 questions
(7 QCM + 2 texte), 7 blocs en ordre strict et 3 schemas.
Annees : 2nde pro, 1re pro, Terminale pro.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pro_electricite_common import REF, S, R, QC, QT, C, build, valider_et_ecrire

F = []


def add(prefix, titre, mat, ans, points, questions, c):
    F.append(build(prefix, titre, mat, ans, points, questions, c))


# ============================================================ EL1
add("PE-B01", "Loi d'Ohm et résistance des conducteurs", "Électrotechnique", ["1re pro"],
    S("Une résistance électrique caractérise l'opposition d'un conducteur au passage du courant."
      "|La résistance d'un fil dépend de sa résistivité, de sa longueur et de sa section."
      "|On calcule la résistance par la relation R = rho L / S, où rho est la résistivité du matériau."
      "|Plus un conducteur est long, plus sa résistance augmente."
      "|Plus sa section est grande, plus sa résistance diminue."
      "|Le cuivre est couramment utilisé en câblage grâce à sa faible résistivité."
      "|La loi d'Ohm énonce que la tension aux bornes d'une résistance est proportionnelle au courant qui la traverse."
      "|On l'écrit U = R I, avec U en volts, I en ampères et R en ohms."
      "|La caractéristique U = f(I) d'un conducteur ohmique est une droite passant par l'origine."
      "|La résistance interne d'un générateur entraîne une chute de tension quand il délivre du courant."
      "|L'effet Joule échauffe le conducteur et augmente la résistance des métaux avec la température."
      "|La loi d'Ohm permet de dimensionner les conducteurs et de contrôler une installation."),
    [QC("Quelle est la relation de la loi d'Ohm ?", "U = I / R~U = R I~U = R + I~U = I - R", 1,
        "La tension aux bornes d'une résistance vaut le produit de la résistance par l'intensité."),
     QC("Comment la résistance varie-t-elle avec la longueur du fil ?", "Elle diminue~Elle augmente~Elle reste constante~Elle devient nulle", 1,
        "R est proportionnelle à la longueur L du conducteur."),
     QC("Comment la résistance varie-t-elle avec la section du fil ?", "Elle augmente~Elle diminue~Elle reste constante~Elle double", 1,
        "R est inversement proportionnelle à la section S du conducteur."),
     QC("Quelle est l'unité de la résistance électrique ?", "Le volt~L'ampère~L'ohm~Le watt", 2,
        "La résistance se mesure en ohms, symbole Ω."),
     QC("Quelle est la forme de la caractéristique U = f(I) d'un conducteur ohmique ?", "Une parabole~Une droite passant par l'origine~Un cercle~Une exponentielle", 1,
        "La proportionnalité entre U et I donne une droite qui passe par l'origine."),
     QC("Pourquoi le cuivre est-il utilisé pour les câbles ?", "Il est très résistif~Il a une faible résistivité~Il est isolant~Il coûte très cher", 1,
        "Sa faible résistivité limite les pertes par effet Joule."),
     QC("Quel effet la température a-t-elle sur la résistance d'un métal ?", "Elle la diminue~Elle l'augmente~Elle l'annule~Elle n'a aucun effet", 1,
        "Pour un métal, la résistance augmente avec la température."),
     QT("Un conducteur de cuivre a une résistivité de 1,7 × 10⁻⁸ ohm·m, une longueur de 20 m et une section de 2,5 mm². Calculer sa résistance.",
        "On convertit d'abord la section en mètres carrés : 2,5 mm² = 2,5 × 10⁻⁶ m². La formule donne R = rho L / S = (1,7 × 10⁻⁸ × 20) / (2,5 × 10⁻⁶) = 3,4 × 10⁻⁷ / 2,5 × 10⁻⁶ = 0,136 ohm. Cette faible valeur est conforme à l'usage du cuivre pour le câblage. Si la longueur doublait, la résistance doublerait également ; si la section doublait, elle serait divisée par deux.",
        "On attend la conversion de la section, l'application de R = rho L/S et le résultat en ohms."),
     QT("Une résistance de 48 ohm est traversée par un courant de 0,5 A. Calculer la tension à ses bornes et la puissance dissipée.",
        "Par la loi d'Ohm, U = R I = 48 × 0,5 = 24 V. La puissance dissipée sous forme de chaleur vaut P = U I = 24 × 0,5 = 12 W, ce que l'on retrouve par P = R I² = 48 × 0,25 = 12 W. Cette puissance doit être évacuée : c'est la raison pour laquelle les résistances sont dimensionnées en watt. Une résistance de puissance insuffisante chaufferait et pourrait être détruite.",
        "La réponse doit calculer U = RI puis P = UI ou RI² et rappeler l'échauffement.")],
    C("La résistance dépend du matériau et de la géométrie ; la loi d'Ohm relie tension et courant.",
      "R = rho L / S · U = R I · P = R I²",
      "rho en ohm·m · L en m · S en m² · R en ohm",
      "Résistivité~Propriété du matériau~Cuivre faible~Longueur~R proportionnelle à L~Fil long~Section~R inversement proportionnelle~Fil gros",
      "Relever les données et convertir les unités|Calculer la résistance|Appliquer la loi d'Ohm|Calculer la puissance dissipée|Vérifier le dimensionnement",
      "Oublier de convertir les mm² en m²|Confondre résistance et résistivité|Inverser longueur et section|Négliger l'échauffement",
      "Cuivre~rho 1,7 × 10⁻⁸~20 m et 2,5 mm²~R = 0,136 ohm~48 ohm sous 0,5 A~U = 24 V~P = 12 W",
      "Conducteur ohmique~U proportionnel à I~Droite par l'origine~Conducteur non ohmique~Caractéristique courbe~Résistance variable",
      "R = rho L/S~Géométrie du fil~U = R I~Loi d'Ohm~P = R I²~Effet Joule"))

# ============================================================ EL2
add("PE-B02", "Lois de Kirchhoff et analyse des circuits", "Électrotechnique", ["1re pro"],
    S("Les lois de Kirchhoff permettent d'analyser les courants et les tensions dans un réseau électrique."
      "|La loi des nœuds énonce que la somme des courants entrant dans un nœud est égale à la somme des courants en sortie."
      "|Elle traduit la conservation de la charge électrique : aucune charge ne s'accumule dans un nœud."
      "|La loi des mailles énonce que la somme algébrique des tensions le long d'une maille fermée est nulle."
      "|Elle traduit la conservation de l'énergie sur un parcours fermé."
      "|Une maille est un boucle fermée de conducteurs et de dipôles."
      "|Un nœud est un point de connexion où au moins trois conducteurs se rencontrent."
      "|Pour appliquer la loi des mailles, on choisit un sens de parcours et on respecte les signes."
      "|Une tension parcourue dans le sens de la flèche est comptée positivement."
      "|En régime continu, une résistance en série provoque une chute de tension égale à R I."
      "|Les résistances en parallèle ont la même tension à leurs bornes et des courants qui s'ajoutent."
      "|La résistance équivalente de deux résistances en dérivation vaut le produit divisé par la somme."),
    [QC("Que dit la loi des nœuds ?", "La somme des courants entrants égale la somme des courants sortants~La somme des tensions est nulle~Le courant est constant partout~La résistance est nulle", 0,
        "La loi des nœuds exprime la conservation de la charge électrique."),
     QC("Que dit la loi des mailles ?", "Les courants s'ajoutent~La somme algébrique des tensions d'une maille est nulle~La tension est constante~Les résistances s'annulent", 1,
        "La loi des mailles exprime la conservation de l'énergie sur un circuit fermé."),
     QC("Qu'appelle-t-on un nœud ?", "Une résistance~Un point de connexion d'au moins trois conducteurs~Une maille~Un générateur", 1,
        "Un nœud est un point où se rejoignent plusieurs conducteurs."),
     QC("Quelle grandeur se conserve selon la loi des mailles ?", "La charge~L'énergie~La masse~La température", 1,
        "La loi des mailles traduit la conservation de l'énergie."),
     QC("Que faut-il choisir pour appliquer la loi des mailles ?", "Une couleur de câble~Un sens de parcours et des signes~Une résistance arbitraire~Une bornier", 1,
        "Le sens de parcours détermine le signe de chaque tension rencontrée."),
     QC("Quelle est la résistance équivalente de deux résistances de 10 ohm en dérivation ?", "20 ohm~10 ohm~5 ohm~2,5 ohm", 2,
        "Deux résistances égales en parallèle donnent une résistance équivalente divisée par deux."),
     QC("Dans une dérivation, quelle grandeur est commune aux branches ?", "L'intensité~La tension~La puissance~La résistance", 1,
        "Les branches en parallèle sont soumises à la même tension."),
     QT("Appliquer la loi des nœuds à un nœud où entrent 3 A et 1 A, et où sortent 2 A et un courant inconnu I.",
        "La loi des nœuds impose que la somme des courants entrants soit égale à la somme des courants sortants. On écrit donc 3 + 1 = 2 + I, soit 4 = 2 + I. Le courant inconnu vaut donc I = 2 A, dans le sens sortant choisi. Si le calcul avait donné une valeur négative, cela aurait signifié que le courant circule en réalité dans le sens opposé à celui qui avait été supposé. Cette méthode permet de vérifier la cohérence d'un schéma de câblage.",
        "On attend l'équation 3 + 1 = 2 + I et l'interprétation d'un résultat négatif."),
     QT("Dans une maille, on rencontre une source de 24 V, puis des chutes de tension de 5 V, 7 V et une chute inconnue U. Calculer U.",
        "La loi des mailles impose que la somme algébrique des tensions soit nulle. En parcourant la maille, on compte la source positive à +24 V et les chutes négatives à -5 V, -7 V et -U. On écrit donc 24 - 5 - 7 - U = 0, d'où U = 24 - 12 = 12 V. La somme des chutes de tension est bien égale à la tension fournie par la source. Ce contrôle est utile pour vérifier le calcul d'une tension aux bornes d'un dipôle dans un circuit complexe.",
        "La réponse doit écrire l'équation de la maille avec les signes et en déduire U = 12 V.")],
    C("Kirchhoff vérifie la cohérence d'un circuit : courants au nœud, tensions à la maille.",
      "Nœud : somme I entrants = somme I sortants · maille : somme des U = 0",
      "Dérivation : même tension · série : même courant",
      "Nœud~Connexion de conducteurs~Conservation de la charge~Maille~Boucle fermée~Conservation de l'énergie~Dérivation~Tension commune~Courants additionnés",
      "Dessiner le schéma et nommer les nœuds|Choisir les sens de courant|Appliquer la loi des nœuds|Parcourir chaque maille avec des signes|Résoudre le système obtenu",
      "Oublier un signe lors du parcours|Supposer un courant nul sans preuve|Confondre nœud et maille|Additionner des tensions de mailles différentes",
      "3 A et 1 A~Entrants~2 A et I~Sortants~I = 2 A~Loi des nœuds~24 - 5 - 7~U = 12 V",
      "Loi des nœuds~Conservation de la charge~Au point de connexion~Loi des mailles~Conservation de l'énergie~Sur un parcours fermé~Loi d'Ohm~Relation locale U = RI",
      "Série~Même intensité~Résistances additionnées~Dérivation~Même tension~Intensités additionnées"))

# ============================================================ EL3
add("PE-B03", "Puissance et énergie électrique en régime continu", "Électrotechnique", ["1re pro"],
    S("La puissance électrique absorbée par un dipôle vaut le produit de sa tension par l'intensité qui le traverse."
      "|On écrit P = U I, avec P en watts, U en volts et I en ampères."
      "|Pour une résistance, la puissance dissipée s'écrit aussi P = R I² ou P = U² / R."
      "|Cette puissance est convertie en chaleur : c'est l'effet Joule."
      "|La puissance fournie par un générateur doit être égale à la somme des puissances absorbées, pertes comprises."
      "|L'énergie électrique consommée pendant une durée t vaut W = P t."
      "|Le kilowattheure est l'unité utilisée sur les factures d'électricité."
      "|Un kilowattheure correspond à une puissance de 1 kW maintenue pendant une heure."
      "|Le rendement d'un convertisseur est le rapport de la puissance utile à la puissance absorbée."
      "|Les pertes correspondent à la différence entre puissance absorbée et puissance utile."
      "|Un conducteur trop petit s'échauffe car sa résistance dissipe trop de puissance."
      "|Le dimensionnement électrique vérifie la puissance, l'intensité et l'échauffement des câbles."),
    [QC("Quelle est la formule de la puissance électrique ?", "P = U / I~P = U I~P = U + I~P = I / U", 1,
        "La puissance est le produit de la tension par l'intensité."),
     QC("Quelle est l'unité de la puissance électrique ?", "Le joule~Le watt~Le volt~L'ampère", 1,
        "La puissance se mesure en watts, symbole W."),
     QC("Que vaut 1 kWh en joules ?", "1000 J~3600 J~3,6 × 10⁶ J~1 J", 2,
        "1 kWh = 1000 W × 3600 s = 3,6 millions de joules."),
     QC("Quelle expression donne la puissance dissipée par une résistance ?", "R / I²~R I²~I² / R~U R", 1,
        "La puissance dissipée par effet Joule vaut R I²."),
     QC("Que devient la puissance perdue dans un circuit ?", "Elle disparaît~Elle se transforme en chaleur~Elle devient du courant~Elle est stockée", 1,
        "Les pertes sont principalement des échauffements par effet Joule."),
     QC("Comment calculer un rendement ?", "Puissance utile multipliée par la puissance absorbée~Puissance utile divisée par la puissance absorbée~Puissance absorbée moins puissance utile~Puissance utile plus pertes", 1,
        "Le rendement est un rapport sans unité, toujours inférieur à 1."),
     QC("Que se passe-t-il si la section d'un câble est trop faible ?", "Le courant diminue~Le câble s'échauffe~La tension augmente~Rien ne change", 1,
        "Une section faible augmente la résistance et donc l'échauffement par effet Joule."),
     QT("Un moteur absorbe 230 V et 4 A. Sa puissance mécanique utile est de 750 W. Calculer la puissance absorbée, les pertes et le rendement.",
        "La puissance électrique absorbée vaut P = U I = 230 × 4 = 920 W. La puissance utile est de 750 W, donc les pertes valent 920 - 750 = 170 W, principalement sous forme de chaleur et de bruit. Le rendement vaut 750 / 920, soit environ 0,815, soit 81,5 %. On vérifie que le rendement est bien inférieur à 1. Cet écart justifie le refroidissement du moteur et le dimensionnement de son alimentation.",
        "On attend P = UI, pertes = absorbée - utile et rendement = utile / absorbée."),
     QT("Un appareil de 1,5 kW fonctionne 4 h par jour pendant 30 jours. Calculer l'énergie consommée et le coût à 0,18 € le kWh.",
        "L'énergie journalière vaut 1,5 kW × 4 h = 6 kWh. Sur 30 jours, la consommation atteint 6 × 30 = 180 kWh. Au tarif de 0,18 € le kWh, le coût est 180 × 0,18 = 32,40 €. En joules, cette énergie représente 180 × 3,6 × 10⁶ = 6,48 × 10⁸ J. Ce type de calcul permet d'estimer l'impact d'un équipement sur la facture et de comparer deux solutions techniques.",
        "La réponse doit multiplier puissance, durée quotidienne et nombre de jours, puis appliquer le tarif.")],
    C("Puissance, énergie et rendement relient l'électricité consommée à l'effet utile obtenu.",
      "P = U I = R I² · W = P t · rendement = P utile / P absorbée",
      "1 kWh = 3,6 × 10⁶ J · pertes = absorbée - utile",
      "Puissance~Énergie par seconde~P = UI~Énergie~Puissance fois durée~W = Pt~Rendement~Rapport sans unité~Utile sur absorbée",
      "Calculer la puissance absorbée|Identifier la puissance utile|En déduire les pertes|Calculer le rendement|Estimer la consommation en kWh",
      "Confondre puissance et énergie|Oublier les pertes|Croire qu'un rendement dépasse 1|Multiplier au lieu de diviser pour le rendement",
      "230 V et 4 A~920 W~750 W utiles~170 W de pertes~Rendement 81,5 %~1,5 kW sur 4 h~6 kWh par jour",
      "Puissance~Flux d'énergie~Watt~Énergie~Quantité transférée~Joule ou kWh~Rendement~Efficacité de conversion~Pourcentage",
      "P = UI~Formule générale~P = RI²~Cas de la résistance~P = U²/R~Autre forme pour une résistance"))

# ============================================================ EL4
add("PE-B04", "Régimes transitoires des circuits RC et RL", "Électrotechnique", ["Terminale pro"],
    S("Un régime transitoire est la phase de transition entre deux états permanents d'un circuit."
      "|Il apparaît lors d'une mise sous tension, d'une coupure ou d'une commutation."
      "|La constante de temps tau caractérise la durée de la transition."
      "|Pour un circuit RC, la constante de temps vaut le produit de la résistance par la capacité."
      "|Pour un circuit RL, elle vaut le rapport de l'inductance sur la résistance."
      "|Au bout de cinq constantes de temps, le régime est considéré comme établi."
      "|La tension aux bornes d'un condensateur ne peut pas varier brutalement."
      "|Le courant dans une bobine ne peut pas varier brutalement."
      "|À la fermeture d'un circuit RC, le condensateur se charge progressivement selon une exponentielle."
      "|À l'ouverture d'un circuit RL, la bobine entretient le courant et peut produire une surtension."
      "|Une diode de roue libre protège le circuit contre cette surtension lors de la coupure d'une bobine."
      "|Ces phénomènes expliquent les temporisations et les précautions de commutation."),
    [QC("Que vaut la constante de temps d'un circuit RC ?", "R / C~R C~C / R~R + C", 1,
        "La constante de temps d'un circuit RC vaut le produit R multiplié par C."),
     QC("Que vaut la constante de temps d'un circuit RL ?", "L R~R / L~L / R~L + R", 2,
        "Pour un circuit RL, tau vaut le rapport de l'inductance L sur la résistance R."),
     QC("Quand le régime permanent est-il considéré comme atteint ?", "Après une constante de temps~Après cinq constantes de temps~Immédiatement~Après dix secondes", 1,
        "On considère usuellement le régime établi après cinq fois la constante de temps."),
     QC("Quelle grandeur ne peut pas varier brutalement aux bornes d'un condensateur ?", "Le courant~La tension~La résistance~La puissance", 1,
        "La tension aux bornes d'un condensateur varie en continu."),
     QC("Quelle grandeur ne peut pas varier brutalement dans une bobine ?", "La tension~Le courant~La capacité~La température", 1,
        "Le courant dans une inductance ne peut pas changer instantanément."),
     QC("Quel composant protège un circuit lors de la coupure d'une bobine ?", "Une diode de roue libre~Un condensateur en série~Une résistance variable~Un transformateur", 0,
        "La diode de roue libre offre un chemin au courant induit et limite la surtension."),
     QC("Quelle est la forme de la charge d'un condensateur en régime transitoire ?", "Linéaire~Exponentielle~Carrée~Sinusoïdale", 1,
        "La tension de charge suit une loi exponentielle de la forme U(1 - exp(-t/tau))."),
     QT("Un circuit RC comporte une résistance de 10 kΩ et un condensateur de 100 µF. Calculer la constante de temps et la durée d'établissement du régime.",
        "La constante de temps vaut tau = R C = 10 000 × 100 × 10⁻⁶ = 1 seconde. Le régime est considéré comme établi après environ cinq constantes de temps, soit 5 secondes. À t = tau, la tension aux bornes du condensateur atteint environ 63 % de sa valeur finale ; à t = 5 tau, elle dépasse 99 %. Ce calcul est utile pour dimensionner une temporisation ou choisir la valeur d'un condensateur de filtrage.",
        "On attend le produit R par C avec conversion des unités, puis cinq fois tau."),
     QT("Expliquer pourquoi la coupure brutale du courant dans une bobine provoque une surtension.",
        "Une bobine s'oppose à toute variation rapide de son courant. Lors de l'ouverture du circuit, l'énergie magnétique stockée doit être dissipée : la bobine génère une tension dite de self-induction qui tente de maintenir le courant. Comme le circuit est ouvert, cette tension peut atteindre une valeur très élevée et endommager les contacts ou les composants. Une diode montée en opposition, dite diode de roue libre, permet au courant de circuler dans une boucle locale pendant la extinction, ce qui limite la surtension et protège l'interrupteur ou le transistor de commande.",
        "La réponse doit relier énergie magnétique, self-induction, surtension et diode de roue libre.")],
    C("Les circuits RC et RL introduisent une constante de temps qui commande la vitesse de transition.",
      "RC : tau = R C · RL : tau = L / R",
      "5 tau pour le régime établi · U_C et I_L continus · diode de roue libre",
      "Constante de temps~Durée de transition~R multiplié par C~Condensateur~Tension continue~Charge exponentielle~Bobine~Courant continu~Self-induction",
      "Repérer le type de circuit|Calculer la constante de temps|Écrire la loi exponentielle|Évaluer la valeur à un instant donné|Prévoir les précautions de commutation",
      "Oublier la conversion des unités|Croire que la transition est instantanée|Négliger la surtension à l'ouverture|Confondre tau RC et tau RL",
      "10 kΩ et 100 µF~tau = 1 s~5 tau~5 s~63 % à tau~99 % à 5 tau~Bobine~Diode de roue libre",
      "Régime transitoire~Phase de transition~Courte durée~Régime permanent~État stable~Après 5 tau~Commutation~Changement brusque",
      "Circuit RC~Résistance et condensateur~tau = RC~Circuit RL~Résistance et bobine~tau = L/R"))

# ============================================================ EL5
add("PE-B05", "Courant alternatif monophasé", "Électrotechnique", ["1re pro"],
    S("Un courant alternatif est un courant dont l'intensité change de sens périodiquement."
      "|La forme la plus courante est la sinusoïde, utilisée pour le réseau électrique public."
      "|Une grandeur sinusoïdale se définit par son amplitude, sa fréquence et sa phase."
      "|La période T est la durée d'un cycle complet ; la fréquence f vaut l'inverse de T."
      "|En France, le réseau basse tension a une fréquence de 50 Hz et une tension efficace de 230 V."
      "|La pulsation omega vaut 2 π f et s'exprime en radians par seconde."
      "|Une grandeur sinusoïdale s'écrit x(t) = X max sin(omega t + phi)."
      "|La valeur efficace d'une tension sinusoïdale vaut son amplitude divisée par la racine de deux."
      "|Les appareils de mesure afficcent généralement des valeurs efficaces."
      "|La phase phi traduit le décalage temporel entre deux grandeurs de même fréquence."
      "|Dans un circuit purement résistif, tension et courant sont en phase."
      "|Le déphasage apparaît dès que le circuit contient des bobines ou des condensateurs."),
    [QC("Quelle est la fréquence du réseau électrique français ?", "25 Hz~50 Hz~60 Hz~400 Hz", 1,
        "Le réseau public français fonctionne à 50 Hz."),
     QC("Quelle est la tension efficace du réseau basse tension monophasé en France ?", "110 V~220 V~230 V~400 V", 2,
        "La tension nominale est de 230 V entre phase et neutre."),
     QC("Quelle est la relation entre période et fréquence ?", "T = f~f = 1/T~T = f²~f = T + 1", 1,
        "La fréquence est l'inverse de la période, exprimée en hertz."),
     QC("Quelle est la pulsation d'un signal de fréquence 50 Hz ?", "50 rad/s~100 rad/s~Environ 314 rad/s~3140 rad/s", 2,
        "omega = 2 π f = 2 × 3,14 × 50, soit environ 314 rad/s."),
     QC("Quelle est la valeur efficace d'une tension sinusoïdale d'amplitude 311 V ?", "155 V~220 V~230 V~311 V", 2,
        "La valeur efficace vaut 311 divisé par la racine de deux, soit environ 220 V ; le réseau nominal est 230 V pour une amplitude d'environ 325 V."),
     QC("Dans un circuit purement résistif, quel est le déphasage entre tension et courant ?", "90 degrés~45 degrés~0 degré~180 degrés", 2,
        "En résistance pure, tension et courant sont en phase : le déphasage est nul."),
     QC("Qu'appelle-t-on phase d'une grandeur sinusoïdale ?", "Son amplitude~Son décalage angulaire par rapport à une référence~Sa puissance~Sa fréquence", 1,
        "La phase exprime le décalage angulaire du signal."),
     QT("Écrire l'expression d'une tension sinusoïdale de valeur efficace 230 V, de fréquence 50 Hz et de phase nulle, puis calculer sa valeur à t = 5 ms.",
        "L'amplitude vaut U max = U efficace × racine de deux = 230 × 1,414, soit environ 325 V. La pulsation vaut omega = 2 π × 50 = 314 rad/s. La tension s'écrit donc u(t) = 325 sin(314 t) volts. À t = 5 ms, l'angle vaut 314 × 0,005 = 1,57 radian, soit π/2. Le sinus valant 1, on obtient u(5 ms) = 325 V, c'est-à-dire le maximum positif de la tension. Ce calcul illustre le passage entre grandeur efficace et valeur instantanée.",
        "On attend le calcul de l'amplitude, de la pulsation, puis l'évaluation à l'instant demandé."),
     QT("Expliquer pourquoi les voltmètres affichent une valeur efficace plutôt qu'une amplitude.",
        "La valeur efficace est définie comme la valeur continue qui produirait le même effet thermique, donc la même puissance dissipée dans une résistance, que le signal alternatif. C'est elle qui intervient dans les formules P = U I et dans le dimensionnement des câbles et des appareils. L'amplitude est la valeur maximale du signal et ne traduit pas directement l'énergie transférée. Un voltmètre affiche donc la valeur efficace, ce qui permet de comparer directement un réseau alternatif et une source continue équivalente.",
        "La réponse doit définir la valeur efficace par l'effet thermique et expliquer son intérêt pour la puissance.")],
    C("Le courant alternatif se décrit par amplitude, fréquence et phase ; les mesures donnent des valeurs efficaces.",
      "x(t) = X max sin(omega t + phi) · omega = 2 π f",
      "U efficace = U max / racine(2) · réseau : 230 V, 50 Hz",
      "Fréquence~Nombre de cycles par seconde~Hertz~Période~Durée d'un cycle~1/f~Amplitude~Valeur maximale~Valeur efficace",
      "Identifier amplitude et fréquence|Calculer la pulsation|Écrire l'expression du signal|Calculer une valeur instantanée|Comparer efficace et amplitude",
      "Confondre amplitude et valeur efficace|Oublier la conversion en secondes|Utiliser 60 Hz|Ignorer le déphasage",
      "230 V~325 V d'amplitude~50 Hz~314 rad/s~5 ms~Valeur maximale~Résistance pure~Déphasage nul",
      "Courant continu~Sens constant~Courant alternatif~Sens variable et périodique~Signal sinusoïdal~Forme régulière~Signal carré~Commutation rapide",
      "Valeur efficace~Effet thermique équivalent~Mesure usuelle~Amplitude~Valeur de crête~Isolation à dimensionner"))

# ============================================================ EL6
add("PE-B06", "Courant triphasé et puissances", "Électrotechnique", ["Terminale pro"],
    S("Le courant triphasé utilise trois tensions sinusoïdales de même fréquence et de même amplitude."
      "|Les trois phases sont décalées de 120 degrés, soit un tiers de période."
      "|La tension entre deux phases vaut la racine de trois fois la tension phase-neutre."
      "|Dans le réseau français, la tension entre phases est de 400 V et la tension phase-neutre de 230 V."
      "|Un système triphasé équilibré a des amplitudes égales et des décalages réguliers."
      "|La puissance active d'une charge équilibrée vaut P = racine(3) U I cos phi."
      "|Le facteur de puissance cos phi traduit le déphasage entre tension et courant."
      "|La puissance réactive Q vaut racine(3) U I sin phi et ne fournit pas de travail utile."
      "|La puissance apparente S vaut racine(3) U I et s'exprime en voltampères."
      "|Les moteurs asynchrones consomment de la puissance réactive pour leur aimantation."
      "|Le condensateur de démarrage ou les batteries de condensateurs améliorent le facteur de puissance."
      "|Le triphasé est utilisé pour les moteurs car il fournit une puissance plus régulière et un meilleur rendement."),
    [QC("Quel est le décalage entre deux phases d'un système triphasé équilibré ?", "60 degrés~90 degrés~120 degrés~180 degrés", 2,
        "Les trois phases sont décalées de 120 degrés, soit un tiers de période."),
     QC("Quelle est la tension entre phases d'un réseau français ?", "230 V~400 V~380 V~690 V", 1,
        "La tension entre phases est de 400 V, la tension phase-neutre de 230 V."),
     QC("Quelle est la relation entre tension entre phases et tension phase-neutre ?", "U = Up / racine(3)~U = Up × racine(3)~U = Up~U = 2 Up", 1,
        "La tension entre phases vaut la tension phase-neutre multipliée par la racine de trois."),
     QC("Quelle est la formule de la puissance active triphasée équilibrée ?", "P = U I~P = racine(3) U I~P = racine(3) U I cos phi~P = 3 U I sin phi", 2,
        "La puissance active dépend du facteur de puissance cos phi."),
     QC("Que représente le facteur de puissance ?", "Le rendement du moteur~Le cosinus de l'angle de déphasage~La tension nominale~La fréquence", 1,
        "cos phi vaut le rapport entre puissance active et puissance apparente."),
     QC("Dans quelle unité exprime-t-on la puissance apparente ?", "En watts~En voltampères~En joules~En ohms", 1,
        "La puissance apparente s'exprime en voltampères, symbole VA."),
     QC("Pourquoi utilise-t-on le triphasé pour les moteurs ?", "Il est moins cher à câbler~Il fournit une puissance plus régulière~Il supprime les pertes~Il n'a pas besoin de terre", 1,
        "La somme des trois puissances est constante, ce qui réduit les vibrations et améliore le rendement."),
     QT("Un moteur triphasé équilibré consomme 400 V et 10 A avec un facteur de puissance de 0,8. Calculer la puissance active, apparente et réactive.",
        "La puissance apparente vaut S = racine(3) × U × I = 1,732 × 400 × 10 = 6 928 VA, soit environ 6,93 kVA. La puissance active vaut P = S × cos phi = 6 928 × 0,8 = 5 542 W, soit environ 5,54 kW. La puissance réactive vaut Q = S × sin phi ; avec cos phi = 0,8, sin phi = 0,6, donc Q = 6 928 × 0,6 = 4 157 VAr, soit environ 4,16 kVAr. Le triangle des puissances vérifie S² = P² + Q².",
        "On attend le calcul de S, puis P = S cos phi et Q = S sin phi avec sin phi = 0,6."),
     QT("Expliquer pourquoi les moteurs asynchrones consomment de la puissance réactive et comment la compenser.",
        "Le moteur asynchrone a besoin d'un champ magnétique tournant pour fonctionner. L'aimantation du circuit magnétique impose un courant déphasé par rapport à la tension, appelé courant réactif. Ce courant ne produit pas de travail mécanique mais charge le réseau et augmente les pertes dans les câbles et les transformateurs. On compense ce besoin en plaçant des batteries de condensateurs en dérivation près des moteurs : le courant capacitif absorbé par les condensateurs compense le courant inductif du moteur. Le facteur de puissance se rapproche alors de 1 et la facture d'électricité diminue.",
        "La réponse doit lier aimantation, courant réactif, dégradation du cos phi et compensation par condensateurs.")],
    C("Le triphasé associe trois décalages de 120 degrés ; la puissance active dépend du cos phi.",
      "P = racine(3) U I cos phi · Q = racine(3) U I sin phi · S = racine(3) U I",
      "U entre phases = racine(3) × U phase-neutre · 400 V / 230 V",
      "Triphasé~Trois tensions décalées~120 degrés~Puissance active~Travail fourni~P = S cos phi~Puissance réactive~Aimantation~Q = S sin phi",
      "Identifier la tension et le courant|Relever le facteur de puissance|Calculer la puissance apparente|En déduire active et réactive|Vérifier le triangle des puissances",
      "Utiliser 230 V au lieu de 400 V|Oublier le facteur racine(3)|Confondre active et apparente|Croire que la réactive est utile",
      "400 V et 10 A~S = 6,93 kVA~cos phi 0,8~P = 5,54 kW~sin phi 0,6~Q = 4,16 kVAr",
      "Monophasé~Deux conducteurs~Usage domestique~Triphasé~Trois conducteurs actifs~Usage industriel~Charge équilibrée~Puissances égales~Décalages réguliers",
      "Puissance active~Transformée en travail~Watt~Puissance réactive~Échangée avec le champ~Voltampère réactif~Puissance apparente~Somme vectorielle~Voltampère"))

# ============================================================ EL7
add("PE-B07", "Redressement et conversion statique", "Électrotechnique", ["Terminale pro"],
    S("Un redresseur convertit une tension alternative en tension continue."
      "|Le redressement monophasé simple utilise une seule diode et ne conserve qu'une alternance."
      "|Le redressement en pont utilise quatre diodes et exploite les deux alternances."
      "|La tension redressée est ondulée : elle reste positive mais varie au rythme du réseau."
      "|Un condensateur de filtrage placé en dérivation réduit l'ondulation résiduelle."
      "|Plus la capacité est grande, plus l'ondulation est faible."
      "|La tension moyenne d'un pont redresseur monophasé vaut environ 0,9 fois la valeur efficace."
      "|Une diode ne conduit que lorsqu'elle est polarisée en direct, dans le sens anode vers cathode."
      "|La tension inverse maximale est la contrainte que la diode doit supporter en blocage."
      "|Les variateurs de vitesse utilisent un redresseur puis un onduleur pour alimenter un moteur."
      "|L'onduleur fabrique une tension alternative de fréquence réglable à partir d'un bus continu."
      "|La modulation de largeur d'impulsion, ou PWM, permet de régler la tension et la fréquence."),
    [QC("Que fait un redresseur ?", "Convertit du continu en alternatif~Convertit de l'alternatif en continu~Augmente la fréquence~Isolie le circuit", 1,
        "Le redresseur transforme une tension alternative en tension continue ondulée."),
     QC("Combien de diodes contient un pont de redressement monophasé ?", "Une~Deux~Quatre~Six", 2,
        "Le pont de Graetz monophasé utilise quatre diodes pour exploiter les deux alternances."),
     QC("Quel composant réduit l'ondulation d'une tension redressée ?", "Une bobine~Un condensateur en dérivation~Une résistance~Un transformateur", 1,
        "Le condensateur se charge au sommet et se décharge entre deux sommets."),
     QC("Dans quel sens une diode est-elle conductrice ?", "De cathode vers anode~De l'anode vers la cathode~Dans les deux sens~Jamais", 1,
        "La diode conduit lorsqu'elle est polarisée en direct, de l'anode vers la cathode."),
     QC("Quelle est la tension moyenne approximative d'un pont monophasé alimenté sous 230 V efficaces ?", "230 V~325 V~207 V~115 V", 2,
        "On retient environ 0,9 × 230 V, soit 207 V, avant filtrage."),
     QC("Que produit un onduleur ?", "Une tension continue~Une tension alternative à partir d'un bus continu~Une résistance~Une surtension", 1,
        "L'onduleur convertit le continu en alternatif de fréquence réglable."),
     QC("Qu'est-ce que la modulation PWM ?", "Un filtre~Une technique de découpage pour régler tension et fréquence~Un type de diode~Une mesure de puissance", 1,
        "La PWM ajuste la largeur des impulsions pour contrôler la tension de sortie."),
     QT("Expliquer le rôle du condensateur de filtrage après un pont de redressement.",
        "À la sortie du pont, la tension est continue mais fortement ondulée : elle passe de zéro à la valeur de crête à chaque demi-période. Le condensateur placé en dérivation se charge rapidement au voisinage du sommet de la tension, puis se décharge lentement dans la charge entre deux sommets. La tension de sortie reste donc élevée et l'ondulation résiduelle diminue. Plus la capacité est grande et plus le courant demandé est faible, plus la tension est lisse. Le condensateur doit toutefois supporter la tension de crête et le courant d'ondulation.",
        "On attend le mécanisme charge-décharge et le lien entre capacité et ondulation."),
     QT("Décrire la chaîne de conversion d'un variateur de vitesse pour moteur asynchrone.",
        "Le variateur prélève la tension alternative du réseau, la redresse avec un pont de diodes pour obtenir une tension continue sur un bus, puis lisse ce bus avec des condensateurs. Un onduleur à transistors découpe ensuite cette tension continue en impulsions de largeur modulée, ce qui synthétise une tension alternative de fréquence et d'amplitude réglables. En faisant varier la fréquence, on fixe la vitesse de rotation du moteur ; en ajustant la tension, on maintient un flux magnétique convenable. Les protections surveillent la surintensité, la surtension du bus et la température des composants.",
        "La réponse doit citer redressement, bus continu, onduleur PWM, réglage de fréquence et protections.")],
    C("Redresser, filtrer, onduler : la conversion statique adapte la forme et la fréquence de la tension.",
      "Pont monophasé : 4 diodes · U moyenne ≈ 0,9 U efficace",
      "Filtrage par condensateur · onduleur PWM · variateur de vitesse",
      "Redresseur~Alternatif vers continu~Pont de diodes~Filtrage~Condensateur en dérivation~Ondulation réduite~Onduleur~Continu vers alternatif~PWM",
      "Vérifier la tension d'entrée|Choisir le type de redressement|Dimensionner le condensateur de filtrage|Configurer l'onduleur|Contrôler les protections thermiques",
      "Brancher une diode à l'envers|Oublier la tension inverse maximale|Sous-dimensionner le condensateur|Ignorer l'échauffement des transistors",
      "230 V efficaces~U moyenne 207 V~325 V de crête~Pont~4 diodes~PWM~Fréquence réglable~Variateur de moteur",
      "Redressement~Alternatif vers continu~Une ou deux alternances~Ondulation~Variation résiduelle~Filtrage~Redressement~Continu ondulé~Condensateur",
      "Redresseur~Conversion AC vers DC~Diode de puissance~Onduleur~Conversion DC vers AC~Transistors~PWM~Découpage à largeur variable"))

# ============================================================ EL8
add("PE-B08", "Transformateur monophasé", "Électrotechnique", ["1re pro"],
    S("Un transformateur monophasé modifie la tension alternative sans changer sa fréquence."
      "|Il repose sur l'induction électromagnétique entre deux enroulements placés sur un même circuit magnétique."
      "|L'enroulement primaire reçoit la tension d'entrée, l'enroulement secondaire fournit la tension de sortie."
      "|Le rapport de transformation vaut le nombre de spires primaires divisé par le nombre de spires secondaires."
      "|La tension secondaire se déduit de la tension primaire par ce rapport de spires."
      "|Le noyau en fer laminé concentre le flux magnétique et limite les pertes par courants de Foucault."
      "|À puissance constante, l'intensité varie en raison inverse de la tension."
      "|Un transformateur abaisseur diminue la tension et augmente l'intensité disponible."
      "|Le rendement d'un transformateur est élevé, souvent supérieur à 95 %."
      "|Les pertes proviennent de la résistance des enroulements et des pertes magnétiques dans le noyau."
      "|La puissance nominale s'exprime en voltampères et conditionne l'échauffement admissible."
      "|La borne de terre et les bornes de protection sont repérées sur le schéma du transformateur."),
    [QC("Quel principe utilise un transformateur ?", "L'effet Joule~L'induction électromagnétique~La réfraction~La capacitance", 1,
        "Le transformateur fonctionne par induction entre deux enroulements couplés par un flux magnétique."),
     QC("Que vaut le rapport de transformation ?", "N2 / N1~N1 / N2~N1 + N2~N1 × N2", 1,
        "Le rapport est le nombre de spires primaires divisé par le nombre de spires secondaires."),
     QC("Quel enroulement reçoit la tension d'entrée ?", "Le secondaire~Le primaire~Le noyau~L'écran", 1,
        "Le primaire est l'enroulement alimenté, le secondaire délivre la tension transformée."),
     QC("Que se passe-t-il dans un transformateur abaisseur ?", "La tension baisse et l'intensité augmente~La tension et l'intensité baissent~La tension monte~La fréquence change", 0,
        "À puissance constante, la baisse de tension s'accompagne d'une hausse d'intensité."),
     QC("Pourquoi le noyau est-il laminé ?", "Pour augmenter le poids~Pour limiter les courants de Foucault~Pour isoler les spires~Pour changer la fréquence", 1,
        "Les tôles laminées réduisent les pertes par courants de Foucault dans le fer."),
     QC("Dans quelle unité exprime-t-on la puissance nominale d'un transformateur ?", "En watts~En voltampères~En joules~En ohms", 1,
        "La puissance apparente nominale s'exprime en VA car le courant peut être déphasé."),
     QC("Un transformateur change-t-il la fréquence ?", "Oui~Non~Seulement en charge~Seulement à vide", 1,
        "La fréquence de sortie reste identique à la fréquence d'entrée."),
     QT("Un transformateur possède 1000 spires au primaire et 100 spires au secondaire. Alimenté sous 230 V, calculer la tension secondaire et l'intensité secondaire pour une intensité primaire de 2 A.",
        "Le rapport de transformation vaut N1/N2 = 1000/100 = 10. La tension secondaire vaut donc U2 = U1 / 10 = 230 / 10 = 23 V. En négligeant les pertes, la puissance est conservée : U1 I1 = U2 I2, soit 230 × 2 = 23 × I2. L'intensité secondaire vaut donc I2 = 460 / 23 = 20 A. On retrouve bien que l'intensité est multipliée par le rapport, ici par 10, tandis que la tension est divisée par 10.",
        "On attend le calcul du rapport de spires, la tension secondaire et l'intensité par conservation de la puissance."),
     QT("Expliquer l'origine des pertes dans un transformateur et les moyens de les limiter.",
        "Les pertes cuivre proviennent de la résistance des enroulements et croissent avec le courant selon R I². Les pertes fer proviennent de l'aimantation cyclique du noyau : hystérésis et courants de Foucault. Pour les réduire, on utilise un fil de cuivre de section adaptée, un noyau en tôles fines et isolées, un acier à faible hystérésis et on évite la saturation magnétique. Le rendement élevé des transformateurs tient à ces choix de conception. Un fonctionnement prolongé en surcharge augmente les pertes cuivre et provoque un échauffement excessif.",
        "La réponse doit distinguer pertes cuivre et pertes fer et proposer les moyens de réduction.")],
    C("Le transformateur adapte la tension par le rapport de spires, sans modifier la fréquence.",
      "m = N1 / N2 · U2 = U1 / m · U1 I1 ≈ U2 I2",
      "Noyau laminé · puissance en VA · rendement supérieur à 95 %",
      "Primaire~Enroulement alimenté~Tension d'entrée~Secondaire~Enroulement de sortie~Tension transformée~Rapport~N1 divisé par N2~Nombre de spires",
      "Identifier primaire et secondaire|Calculer le rapport de spires|En déduire la tension secondaire|Conserver la puissance pour l'intensité|Vérifier la puissance nominale",
      "Inverser le rapport|Oublier que la fréquence est inchangée|Dépasser la puissance nominale|Négliger les pertes fer",
      "1000 spires et 100 spires~Rapport 10~230 V vers 23 V~2 A vers 20 A~Puissance 460 VA",
      "Transformateur abaisseur~Tension réduite~Intensité augmentée~Transformateur élévateur~Tension augmentée~Intensité réduite~Rapport~Nombre de spires",
      "Pertes cuivre~Résistance des enroulements~R I²~Pertes fer~Hystérésis et Foucault~Tôles laminées"))

# ============================================================ EL9
add("PE-B09", "Transformateurs triphasés et couplages", "Électrotechnique", ["Terminale pro"],
    S("Un transformateur triphasé transforme simultanément les trois tensions d'un réseau triphasé."
      "|Il peut être constitué de trois transformateurs monophasés ou d'un noyau triphasé commun."
      "|Les enroulements peuvent être couplés en étoile ou en triangle."
      "|Le couplage en étoile relie une extrémité de chaque enroulement à un point neutre commun."
      "|Le couplage en triangle relie la fin d'un enroulement au début du suivant."
      "|En étoile, la tension entre phases vaut la racine de trois fois la tension par enroulement."
      "|En triangle, la tension entre phases est égale à la tension aux bornes de chaque enroulement."
      "|Les symboles des couplages sont Y pour l'étoile, D pour le triangle et y ou d pour le basse tension."
      "|Un couplage Yd est courant pour l'alimentation de moteurs asynchrones."
      "|Le décalage angulaire entre couplages est indiqué par un chiffre horaire, souvent 0, 5 ou 11."
      "|Le point neutre permet d'alimenter des circuits monophasés et de relier la terre du réseau."
      "|Le choix du couplage influe sur les courants de circulation et sur la tenue aux défauts."),
    [QC("Comment appelle-t-on le couplage qui relie les enroulements à un point neutre commun ?", "Le couplage triangle~Le couplage étoile~Le couplage série~Le couplage ouvert", 1,
        "Dans le couplage étoile, les trois enroulements sont reliés à un neutre commun."),
     QC("Quel symbole désigne le couplage triangle ?", "Y~D~N~S", 1,
        "Le couplage triangle est noté D, l'étoile est notée Y."),
     QC("En couplage étoile, quelle est la relation entre tension entre phases et tension par enroulement ?", "Elles sont égales~La tension entre phases vaut racine(3) fois la tension d'enroulement~La tension entre phases est divisée par racine(3)~Elles sont opposées", 1,
        "En étoile, U entre phases = racine(3) multiplié par la tension de chaque enroulement."),
     QC("En couplage triangle, que vaut la tension entre phases ?", "Le tiers de la tension d'enroulement~La racine de trois fois la tension d'enroulement~La tension d'enroulement~Le double", 2,
        "En triangle, chaque enroulement est directement branché entre deux phases."),
     QC("Quel couplage est courant pour alimenter un moteur asynchrone ?", "Yy~Yd~Dd~Yn", 1,
        "Le couplage Yd est fréquent pour les transformateurs de distribution de moteurs."),
     QC("Que représente le chiffre horaire d'un transformateur triphasé ?", "Sa puissance~Le décalage angulaire entre primaire et secondaire~Sa fréquence~Son rendement", 1,
        "Le groupe de couplage indique le décalage de phase, par exemple 0, 5 ou 11 heures."),
     QC("Quel rôle joue le point neutre ?", "Il augmente la tension~Il permet d'alimenter des circuits monophasés et de raccorder la terre~Il supprime les pertes~Il fixe la fréquence", 1,
        "Le neutre sert de référence pour les tensions monophasées et pour la mise à la terre."),
     QT("Un transformateur triphasé couplé en étoile a une tension de 230 V aux bornes de chaque enroulement. Calculer la tension entre phases et la tension disponible entre phase et neutre.",
        "En couplage étoile, la tension entre phase et neutre est la tension aux bornes de chaque enroulement, soit 230 V. La tension entre deux phases vaut la racine de trois fois cette valeur, soit 1,732 × 230 = 398 V, arrondie à 400 V. On retrouve les valeurs nominales du réseau basse tension français : 400 V entre phases et 230 V entre phase et neutre. Le point neutre est donc le référentiel des tensions monophasées du réseau.",
        "On attend la distinction entre tension d'enroulement, tension phase-neutre et tension entre phases."),
     QT("Expliquer l'intérêt du couplage triangle du côté basse tension d'un transformateur de moteur.",
        "Le couplage triangle offre plusieurs avantages. Il permet de fermer le chemin des courants harmoniques de rang 3, ce qui limite leur propagation dans le réseau amont. Il supprime le problème de déplacement du point neutre lors d'une charge déséquilibrée. En cas de défaut monophasé à la terre, le courant de défaut reste limité si le neutre n'est pas directement mis à la terre, ce qui améliore la continuité de service. Enfin, il donne un décalage angulaire déterminé, souvent 11 heures, qui facilite la mise en parallèle des transformateurs.",
        "La réponse doit évoquer harmoniques, neutre, courant de défaut et décalage angulaire.")],
    C("Le couplage étoile ou triangle fixe les tensions, les courants et le décalage du transformateur triphasé.",
      "Étoile : U entre phases = racine(3) U enroulement · triangle : U entre phases = U enroulement",
      "Y, D, y, d · chiffre horaire 0, 5 ou 11 · neutre",
      "Couplage étoile~Point neutre commun~Tension racine(3)~Couplage triangle~Enroulements en boucle~Tension égale~Groupe~Yd, chiffre horaire~Décalage angulaire",
      "Repérer le couplage primaire et secondaire|Calculer les tensions d'enroulement|En déduire les tensions entre phases|Vérifier le groupe de couplage|Contrôler la charge et le neutre",
      "Appliquer racine(3) au triangle|Confondre tension d'enroulement et tension de phase|Ignorer le chiffre horaire|Oublier le neutre",
      "Étoile~230 V par enroulement~400 V entre phases~Triangle~400 V par enroulement~Yd~Décalage 11 heures",
      "Couplage étoile~Six bornes plus neutre~Courant de phase égal au courant de ligne~Couplage triangle~Trois bornes~Courant de ligne vaut racine(3) fois le courant de phase~Neutre~Point commun",
      "Transformateur monophasé~Un enroulement par tension~Une relation de spires~Transformateur triphasé~Trois enroulements~Trois tensions décalées"))

# ============================================================ EL10
add("PE-B10", "Machine asynchrone à cage : structure et fonctionnement", "Électrotechnique", ["1re pro"],
    S("Le moteur asynchrone à cage est le moteur électrique le plus utilisé en industrie."
      "|Il comporte un stator fixe muni d'enroulements triphasés et un rotor en cage d'écureuil."
      "|La cage du rotor est formée de barres de cuivre ou d'aluminium reliées par des bagues."
      "|Les enroulements du stator, alimentés en triphasé, créent un champ magnétique tournant."
      "|La vitesse du champ tournant dépend de la fréquence et du nombre de paires de pôles."
      "|Le rotor est entraîné par les courants induits dans les barres : c'est le principe de l'induction."
      "|Le rotor tourne toujours moins vite que le champ tournant : c'est le glissement."
      "|Sans glissement, aucun courant ne serait induit et aucun couple ne serait développé."
      "|Le glissement s'exprime en pourcentage par rapport à la vitesse du champ tournant."
      "|Le couple moteur dépend du glissement et de la tension d'alimentation."
      "|La cage est robuste, sans balais ni collectionneur, ce qui réduit l'entretien."
      "|Ce moteur est utilisé pour les pompes, les ventilateurs, les convoyeurs et les machines-outils."),
    [QC("Comment s'appelle la partie fixe du moteur asynchrone ?", "Le rotor~Le stator~La cage~Le collecteur", 1,
        "Le stator est la partie fixe qui porte les enroulements d'alimentation."),
     QC("Quel élément crée le champ magnétique tournant ?", "Les barres du rotor~Les enroulements du stator~Les bagues~Le ventilateur", 1,
        "Les enroulements triphasés du stator produisent un champ tournant."),
     QC("Que désigne le glissement ?", "La différence de vitesse entre le champ et le rotor~La perte de tension~Le bruit du moteur~L'échauffement du stator", 0,
        "Le glissement est l'écart de vitesse entre le champ tournant et le rotor."),
     QC("Pourquoi le rotor doit-il tourner moins vite que le champ ?", "Pour éviter l'échauffement~Pour qu'un courant soit induit dans les barres~Pour réduire le bruit~Pour augmenter la tension", 1,
        "Sans différence de vitesse, il n'y a pas d'induction et donc pas de couple."),
     QC("Quel est l'avantage principal de la cage d'écureuil ?", "Elle augmente le glissement~Elle supprime balais et collecteur~Elle change la fréquence~Elle réduit le nombre de pôles", 1,
        "L'absence de balais et de collecteur rend le moteur robuste et peu entretenu."),
     QC("Quelle grandeur fixe la vitesse du champ tournant ?", "La tension et la résistance~La fréquence et le nombre de paires de pôles~Le courant et la charge~La température", 1,
        "La vitesse de synchronisme dépend de la fréquence et du nombre de paires de pôles."),
     QC("Quelle application courante utilise un moteur asynchrone ?", "Un fer à repasser~Une pompe ou un ventilateur~Une lampe~Une prise de courant", 1,
        "Pompes, ventilateurs et convoyeurs sont entraînés par des moteurs asynchrones."),
     QT("Calculer la vitesse du champ tournant d'un moteur à 4 pôles alimenté à 50 Hz, puis le glissement si le rotor tourne à 1440 tr/min.",
        "Le nombre de paires de pôles vaut 4 / 2 = 2. La vitesse du champ tournant vaut n_s = 60 f / p = 60 × 50 / 2 = 1500 tr/min. Le glissement vaut g = (n_s - n) / n_s = (1500 - 1440) / 1500 = 60 / 1500 = 0,04, soit 4 %. Cette valeur faible est typique d'un moteur fonctionnant à sa charge nominale. À vide, le glissement serait encore plus petit, de l'ordre de 1 %.",
        "On attend le calcul de la vitesse de synchronisme puis celui du glissement en pourcentage."),
     QT("Expliquer pourquoi un moteur asynchrone ne peut pas tourner à la vitesse du champ tournant.",
        "Le couple moteur naît de l'induction des courants dans les barres du rotor par le champ tournant. Cette induction nécessite un mouvement relatif entre le champ et les barres, donc une différence de vitesse appelée glissement. Si le rotor atteignait la vitesse du champ, il n'y aurait plus de variation de flux dans les barres, plus de courant induit et plus de couple. Le moteur ralentirait alors sous l'effet de la charge jusqu'à ce qu'un glissement suffisant réapparaisse. Le fonctionnement asynchrone est donc une condition nécessaire à la production du couple.",
        "La réponse doit relier induction, mouvement relatif et production du couple.")],
    C("Le moteur asynchrone transforme l'énergie électrique en rotation grâce au glissement et à l'induction.",
      "n_s = 60 f / p · glissement g = (n_s - n) / n_s",
      "Stator triphasé · rotor en cage · pas de balais",
      "Stator~Partie fixe~Enroulements triphasés~Rotor~Partie tournante~Cage d'écureuil~Champ tournant~Créé par le stator~Vitesse de synchronisme",
      "Repérer le nombre de pôles|Calculer la vitesse du champ|Mesurer la vitesse du rotor|En déduire le glissement|Comparer à la valeur nominale",
      "Confondre pôles et paires de pôles|Oublier le facteur 60|Croire que le glissement est une perte de tension|Ignorer la charge du moteur",
      "4 pôles et 50 Hz~1500 tr/min~Rotor 1440 tr/min~Glissement 4 %~Cage~Sans balais",
      "Moteur asynchrone~Rotor plus lent~Glissement nécessaire~Moteur synchrone~Rotor à la vitesse du champ~Rotor aimanté~Induction~Courant dans les barres~Couple moteur",
      "Cage d'écureuil~Barres et bagues~Robuste~Rotor bobiné~Enroulements et bagues~Démarrage réglable"))

# ============================================================ EL11
add("PE-B11", "Démarrage et rendement du moteur asynchrone", "Électrotechnique", ["Terminale pro"],
    S("Au démarrage, le glissement du moteur asynchrone vaut 1 car le rotor est immobile."
      "|Le courant de démarrage peut atteindre cinq à sept fois le courant nominal."
      "|Ce courant élevé provoque une chute de tension sur le réseau et un échauffement rapide."
      "|Le couple de démarrage doit être supérieur au couple résistant de la machine entraînée."
      "|Un démarrage direct est simple mais réservé aux puissances modestes ou aux réseaux robustes."
      "|Le démarrage étoile-triangle réduit la tension appliquée à chaque enroulement pendant la phase de démarrage."
      "|En étoile, la tension par enroulement vaut la tension du réseau divisée par la racine de trois."
      "|Après accélération, un contacteur commute le moteur en triangle pour le fonctionnement nominal."
      "|Un démarreur progressif électronique limite la tension et le courant pendant la montée en vitesse."
      "|Un variateur de fréquence règle la tension et la fréquence pour un démarrage doux et une vitesse variable."
      "|Le rendement du moteur est le rapport entre puissance mécanique utile et puissance électrique absorbée."
      "|Les pertes comprennent les pertes cuivre, les pertes fer, les frottements et les pertes ventilatoires."),
    [QC("Quel est le glissement au démarrage d'un moteur asynchrone ?", "0~0,5~1~2", 2,
        "Le rotor étant immobile, la différence de vitesse est totale : le glissement vaut 1."),
     QC("Combien de fois le courant nominal le courant de démarrage peut-il atteindre ?", "1 à 2~5 à 7~20 à 30~0,5", 1,
        "Le courant de démarrage peut atteindre cinq à sept fois le courant nominal."),
     QC("Quel est l'inconvénient d'un démarrage direct ?", "Il est trop lent~Il appelle un courant élevé et perturbe le réseau~Il supprime le couple~Il change la fréquence", 1,
        "Le fort appel de courant provoque une chute de tension et sollicite les contacteurs."),
     QC("Que fait le démarrage étoile-triangle ?", "Il augmente la tension au démarrage~Il réduit la tension par enroulement au démarrage~Il inverse le sens de rotation~Il change le nombre de pôles", 1,
        "En étoile, chaque enroulement reçoit une tension divisée par la racine de trois."),
     QC("Quelle tension reçoit un enroulement en étoile branché sur un réseau de 400 V ?", "400 V~230 V~200 V~690 V", 1,
        "400 divisé par la racine de trois donne environ 230 V."),
     QC("Quel appareil permet un démarrage doux et une vitesse variable ?", "Un contacteur~Un variateur de fréquence~Un disjoncteur~Une diode", 1,
        "Le variateur ajuste tension et fréquence pour contrôler l'accélération et la vitesse."),
     QC("Comment calculer le rendement d'un moteur ?", "Puissance absorbée divisée par puissance utile~Puissance utile divisée par puissance absorbée~Puissance utile plus pertes~Courant divisé par tension", 1,
        "Le rendement est le rapport de la puissance utile sur la puissance absorbée."),
     QT("Un moteur absorbe 5 kW et fournit 4,4 kW sur son arbre. Calculer les pertes et le rendement.",
        "Les pertes valent la différence entre puissance absorbée et puissance utile, soit 5000 - 4400 = 600 W. Elles se répartissent entre pertes cuivre dans les enroulements, pertes fer dans le circuit magnétique, frottements mécaniques et pertes ventilatoires. Le rendement vaut 4400 / 5000 = 0,88, soit 88 %. On vérifie que puissance utile et pertes totalisent la puissance absorbée. Un rendement de 88 % est typique d'un moteur asynchrone de cette puissance.",
        "On attend pertes = absorbée - utile et rendement = utile / absorbée."),
     QT("Expliquer le principe du démarrage étoile-triangle et son intérêt pour le réseau.",
        "Au démarrage, les trois enroulements du stator sont reliés en étoile. Chaque enroulement reçoit donc une tension réduite, égale à la tension entre phases divisée par la racine de trois, soit 230 V sur un réseau de 400 V. Le courant de ligne est alors divisé par trois environ et le couple de démarrage est réduit d'un facteur trois. Une fois le moteur acceleré, les contacteurs commutent les enroulements en triangle : chaque enroulement reçoit alors 400 V et le moteur développe son couple nominal. Cette méthode limite la chute de tension sur le réseau et l'usure mécanique, mais elle ne convient que si le couple résistant au démarrage est modéré.",
        "La réponse doit citer la réduction de tension, la commutation et la limitation du courant de ligne.")],
    C("Le démarrage maîtrise l'appel de courant ; le rendement mesure la part d'énergie transformée en travail.",
      "g démarrage = 1 · I démarrage ≈ 5 à 7 I nominale",
      "Étoile-triangle : U enroulement = U réseau / racine(3) · rendement = P utile / P absorbée",
      "Courant de démarrage~Appel élevé~Chute de tension~Glissement initial~Égal à 1~Rotor immobile~Étoile-triangle~Tension réduite~Commutation",
      "Comparer couple moteur et couple résistant|Choisir le mode de démarrage|Calculer la tension par enroulement|Vérifier les contacteurs|Mesurer le rendement en charge",
      "Oublier la racine de trois|Croire que le couple augmente en étoile|Négliger l'échauffement au démarrage|Confondre rendement et facteur de puissance",
      "5 kW absorbés~4,4 kW utiles~600 W de pertes~Rendement 88 %~400 V en triangle~230 V en étoile",
      "Démarrage direct~Tension pleine~Courant élevé~Démarrage étoile-triangle~Tension réduite~Courant divisé par trois~Variateur~Tension et fréquence ajustées",
      "Pertes cuivre~R I²~Pertes fer~Hystérésis et Foucault~Pertes mécaniques~Frottements et ventilation"))

# ============================================================ EL12
add("PE-B12", "Machine synchrone et alternateur", "Électrotechnique", ["Terminale pro"],
    S("Une machine synchrone tourne à la vitesse exacte du champ magnétique tournant."
      "|Elle peut fonctionner en moteur ou en génératrice, selon le sens de transfert d'énergie."
      "|L'alternateur est une machine synchrone utilisée comme génératrice pour produire de l'énergie électrique."
      "|Le stator porte les enroulements d'induit où est produite la tension."
      "|Le rotor porte les pôles et reçoit le courant d'excitation continu par l'intermédiaire de balais ou d'un excitateur sans balais."
      "|La tension produite dépend de la vitesse de rotation, du flux d'excitation et du nombre de spires."
      "|La fréquence de la tension est liée à la vitesse et au nombre de paires de pôles par f = n p / 60."
      "|Pour produire 50 Hz avec un alternateur bipolaire, la vitesse doit être de 3000 tr/min."
      "|Les alternateurs de centrale sont souvent à pôles saillants et tournent à vitesse plus basse."
      "|Lorsque la machine est couplée au réseau, sa vitesse est imposée par la fréquence du réseau."
      "|Le facteur de puissance d'une machine synchrone peut être réglé par le courant d'excitation."
      "|Une excitation trop faible ou trop forte peut provoquer une perte de synchronisme."),
    [QC("Quelle est la vitesse d'une machine synchrone par rapport au champ tournant ?", "Plus lente~Égale~Plus rapide~Variable sans limite", 1,
        "Le rotor d'une machine synchrone tourne exactement à la vitesse du champ tournant."),
     QC("Quel organe porte les enroulements d'induit d'un alternateur ?", "Le rotor~Le stator~Les balais~L'excitateur", 1,
        "La tension est produite dans les enroulements du stator."),
     QC("Quelle relation donne la fréquence d'un alternateur ?", "f = n / p~f = n p / 60~f = 60 p / n~f = 60 n p", 1,
        "La fréquence vaut la vitesse en tr/min multipliée par le nombre de paires de pôles, divisée par 60."),
     QC("À quelle vitesse tourne un alternateur bipolaire produisant 50 Hz ?", "1000 tr/min~1500 tr/min~3000 tr/min~6000 tr/min", 2,
        "Avec une paire de pôles, n = 60 f / p = 60 × 50 = 3000 tr/min."),
     QC("Que règle le courant d'excitation d'une machine synchrone ?", "La fréquence uniquement~Le flux et le facteur de puissance~La résistance du stator~La vitesse mécanique", 1,
        "L'excitation ajuste le flux magnétique et le déphasage par rapport au réseau."),
     QC("Que se passe-t-il si l'excitation est trop faible ?", "La machine accélère~La machine peut perdre le synchronisme~La tension devient nulle~La fréquence double", 1,
        "Une excitation insuffisante réduit le couple et peut entraîner une perte de synchronisme."),
     QC("Quel rôle joue un alternateur de centrale ?", "Il consomme de l'électricité~Il produit de l'électricité à partir d'un moteur primaire~Il redresse le courant~Il filtre le réseau", 1,
        "L'alternateur convertit l'énergie mécanique du moteur primaire en énergie électrique."),
     QT("Un alternateur possède 4 pôles et tourne à 1500 tr/min. Calculer la fréquence de la tension produite.",
        "Le nombre de paires de pôles vaut 4 / 2 = 2. La fréquence vaut f = n p / 60 = 1500 × 2 / 60 = 50 Hz. On retrouve la fréquence du réseau public français. Si la vitesse passait à 1000 tr/min, la fréquence deviendrait 1000 × 2 / 60, soit environ 33,3 Hz, ce qui empêcherait le couplage au réseau. La relation entre vitesse, pôles et fréquence est donc un impératif de conception des groupes de production.",
        "On attend le calcul des paires de pôles puis l'application de f = n p / 60."),
     QT("Expliquer comment le courant d'excitation influe sur le fonctionnement d'une machine synchrone couplée au réseau.",
        "Lorsque la machine est couplée, la fréquence et la vitesse sont imposées par le réseau. Le courant d'excitation fixe le flux magnétique et donc la tension interne de la machine. En augmentant l'excitation, on fournit de la puissance réactive au réseau et le courant prend une phase en avance : la machine fonctionne en mode capacitif. En réduisant l'excitation, la machine absorbe de la puissance réactive et le courant est en retard : elle fonctionne en mode inductif. Un réglage convenable permet d'améliorer le facteur de puissance du site. Une excitation trop éloignée de la valeur nominale réduit la marge de stabilité et peut provoquer une perte de synchronisme.",
        "La réponse doit relier excitation, tension interne, puissance réactive et stabilité.")],
    C("La machine synchrone impose sa vitesse au champ ; l'alternateur produit une tension de fréquence determinée.",
      "f = n p / 60 · n = 60 f / p",
      "Stator = induit · rotor = excitation · réglage du cos phi par l'excitation",
      "Alternateur~Production d'électricité~Moteur primaire~Stator~Enroulements d'induit~Tension produite~Rotor~Pôles et excitation~Courant continu",
      "Repérer le nombre de pôles|Calculer la vitesse ou la fréquence|Vérifier l'excitation|Contrôler le couplage au réseau|Régler la puissance réactive",
      "Confondre pôles et paires de pôles|Oublier le facteur 60|Croire que la vitesse est libre une fois couplée|Ignorer la limite d'excitation",
      "4 pôles~2 paires~1500 tr/min~50 Hz~Bipolaire~3000 tr/min~Courant d'excitation~Facteur de puissance",
      "Moteur asynchrone~Vitesse inférieure au champ~Glissement~Moteur synchrone~Vitesse égale au champ~Pas de glissement~Alternateur~Conversion mécanique en électrique",
      "Excitation~Courant continu au rotor~Flux magnétique~Induit~Enroulement où naît la tension~Stator"))

# ============================================================ EL13
add("PE-B13", "Moteur à courant continu", "Électrotechnique", ["Terminale pro"],
    S("Le moteur à courant continu transforme une tension continue en mouvement de rotation."
      "|Il comporte un stator à aimants permanents ou à enroulements d'excitation et un rotor appelé induit."
      "|L'induit est alimenté en courant continu par l'intermédiaire d'un collecteur à lames et de balais de charbon."
      "|Le collecteur inverse le sens du courant dans les bobines du rotor à chaque demi-tour."
      "|Cette inversion entretient un couple de rotation constant."
      "|La force de Laplace explique l'action du champ magnétique sur les conducteurs parcourus par un courant."
      "|La vitesse du moteur dépend de la tension d'induit, du flux d'excitation et de la charge."
      "|Augmenter la tension d'induit augmente la vitesse de rotation."
      "|Réduire le flux d'excitation augmente également la vitesse, mais diminue le couple disponible."
      "|Le couple est proportionnel au produit du flux d'excitation par le courant d'induit."
      "|Les moteurs série ont un couple de démarrage élevé mais une vitesse qui varie beaucoup avec la charge."
      "|Les balais s'usent et nécessitent une maintenance régulière, contrairement au moteur asynchrone."),
    [QC("Quel organe alimente l'induit en courant continu ?", "Un transformateur~Un collecteur avec balais~Une diode~Un condensateur", 1,
        "Le collecteur à lames et les balais assurent l'alimentation de l'induit tournant."),
     QC("Pourquoi le collecteur inverse-t-il le courant dans le rotor ?", "Pour réduire la tension~Pour maintenir un couple de rotation constant~Pour augmenter la résistance~Pour changer la fréquence", 1,
        "L'inversion à chaque demi-tour garde le couple dans le même sens de rotation."),
     QC("Quelle loi explique la force sur un conducteur parcouru par un courant dans un champ ?", "La loi d'Ohm~La force de Laplace~La loi de Kirchhoff~La loi de Coulomb", 1,
        "La force de Laplace agit sur un conducteur traversé par un courant placé dans un champ magnétique."),
     QC("Que se passe-t-il quand on augmente la tension d'induit ?", "La vitesse diminue~La vitesse augmente~Le couple devient nul~La résistance augmente", 1,
        "À flux constant, la vitesse est sensiblement proportionnelle à la tension d'induit."),
     QC("Quel est l'effet d'une réduction du flux d'excitation ?", "La vitesse baisse et le couple augmente~La vitesse monte et le couple baisse~Rien ne change~Le moteur s'arrête", 1,
        "Diminuer le flux augmente la vitesse mais réduit le couple disponible."),
     QC("Quel moteur à courant continu a un couple de démarrage élevé ?", "Le moteur shunt~Le moteur série~Le moteur asynchrone~Le moteur synchrone", 1,
        "Le moteur série développe un couple de démarrage important, utile pour la traction."),
     QC("Quel entretien est spécifique au moteur à courant continu ?", "Remplacer les tôles du stator~Remplacer les balais usés~Réglage du glissement~Contrôle des phase", 1,
        "Les balais de charbon s'usent au contact du collecteur et doivent être remplacés."),
     QT("Expliquer le rôle du collecteur à lames dans un moteur à courant continu.",
        "L'induit est solidaire du rotor et ne peut pas être relié directement à une source fixe de courant. Le collecteur, solidaire de l'axe, et les balais fixes assurent le contact électrique entre la source et les bobines tournantes. À chaque demi-tour, les lames du collecteur inversent le sens du courant dans une bobine donnée. Cette commutation mécanique est indispensable : sans elle, le couple exercé sur la bobine changerait de sens à chaque demi-tour et le rotor s'arrêterait. Les balais s'usent, ce qui impose une maintenance et limite la vitesse maximale.",
        "On attend le lien entre alimentation du rotor, inversion du courant et maintien du couple."),
     QT("Un moteur à courant continu tourne à 1000 tr/min sous 24 V. Quelle sera sa vitesse approximative sous 12 V, à flux et charge constants ?",
        "À flux constant et à charge inchangée, la vitesse d'un moteur à courant continu est sensiblement proportionnelle à la tension d'induit. En divisant la tension par deux, on divise la vitesse par deux : elle passe donc d'environ 1000 tr/min à 500 tr/min. En pratique, la charge et les pertes introduisent un écart, mais l'ordre de grandeur reste valable. C'est ce principe qui permet la variation de vitesse simple par variation de tension, par exemple avec un hacheur à modulation de largeur d'impulsion.",
        "La réponse doit utiliser la proportionnalité entre tension et vitesse à flux constant.")],
    C("Le moteur à courant continu règle sa vitesse par la tension et son couple par le courant et le flux.",
      "Couple proportionnel à flux × courant d'induit · vitesse proportionnelle à tension / flux",
      "Collecteur et balais · force de Laplace · moteur série ou shunt",
      "Induit~Partie tournante~Alimenté en continu~Excitation~Crée le flux~Aimants ou bobines~Collecteur~Inverse le courant~Balais de charbon",
      "Identifier le type d'excitation|Vérifier l'état des balais|Appliquer la tension d'induit|Estimer la vitesse|Contrôler le couple demandé",
      "Oublier d'inverser le courant|Confondre flux et tension|Croire que le couple est constant quelle que soit la charge|Négliger l'usure des balais",
      "24 V~1000 tr/min~12 V~500 tr/min~Moteur série~Couple élevé au démarrage~Moteur shunt~Vitesse plus stable",
      "Moteur à courant continu~Collecteur et balais~Variation de vitesse facile~Moteur asynchrone~Sans balais~Peu d'entretien~Moteur pas à pas~Position précise",
      "Moteur série~Excitation en série avec l'induit~Couple élevé~Moteur shunt~Excitation en dérivation~Vitesse stable"))

# ============================================================ EL14
add("PE-B14", "Champ magnétique et forces électromagnétiques", "Physique appliquée", ["1re pro"],
    S("Un champ magnétique est une région de l'espace où des aimants ou des courants exercent une force."
      "|L'induction magnétique B se mesure en tesla et caractérise l'intensité locale du champ."
      "|Les lignes de champ indiquent la direction du champ : elles sortent du pôle nord et entrent dans le pôle sud."
      "|Un conducteur parcouru par un courant crée un champ magnétique circulaire autour de lui."
      "|La règle de la main droite donne le sens de ce champ en fonction du sens du courant."
      "|Une bobine parcourue par un courant se comporte comme un aimant, avec un pôle nord et un pôle sud."
      "|Le produit de l'intensité par le nombre de spires, appelé ampères-tours, fixe l'intensité de l'aimantation."
      "|La force de Laplace s'exerce sur un conducteur parcouru par un courant placé dans un champ magnétique."
      "|Son expression est F = B I L sin alpha, où alpha est l'angle entre le conducteur et le champ."
      "|La force est maximale quand le conducteur est perpendiculaire au champ."
      "|Le sens de la force se determine avec la règle de la main gauche ou la règle du tire-bouchon."
      "|Cette force est à la base du fonctionnement des moteurs électriques et des contacteurs."),
    [QC("Quelle est l'unité de l'induction magnétique ?", "L'ampère~Le tesla~Le volt~Le weber", 1,
        "L'induction magnétique B se mesure en tesla, symbole T."),
     QC("Quel sens ont les lignes de champ à l'extérieur d'un aimant ?", "Du sud vers le nord~Du nord vers le sud~Elles sont fermées sur elles-mêmes~Elles n'ont pas de sens", 1,
        "À l'extérieur, les lignes vont du pôle nord vers le pôle sud."),
     QC("Quel champ crée un conducteur rectiligne parcouru par un courant ?", "Un champ radial~Un champ circulaire autour du conducteur~Aucun champ~Un champ uniforme", 1,
        "Les lignes de champ sont des cercles concentriques autour du conducteur."),
     QC("Que vaut le produit intensité fois nombre de spires d'une bobine ?", "Le flux magnétique~Les ampères-tours~La résistance~La puissance", 1,
        "Le nombre d'ampères-tours NI caractérise l'aimantation de la bobine."),
     QC("Quelle est l'expression de la force de Laplace ?", "F = B I L sin alpha~F = B / (I L)~F = B I L cos alpha~F = B + I + L", 0,
        "La force vaut B I L multiplié par le sinus de l'angle entre conducteur et champ."),
     QC("Quand la force de Laplace est-elle maximale ?", "Quand le conducteur est parallèle au champ~Quand le conducteur est perpendiculaire au champ~Quand le courant est nul~Quand le champ est faible", 1,
        "Le sinus vaut 1 pour un angle de 90 degrés, donc pour une direction perpendiculaire."),
     QC("Quelle application utilise directement la force de Laplace ?", "Un transformateur~Un moteur électrique~Une diode~Un condensateur", 1,
        "Les conducteurs de l'induit d'un moteur sont soumis à la force de Laplace."),
     QT("Un conducteur de 0,5 m est parcouru par un courant de 8 A dans un champ de 0,2 T. Calculer la force maximale et la force à 30 degrés.",
        "La force maximale, pour un conducteur perpendiculaire au champ, vaut F = B I L = 0,2 × 8 × 0,5 = 0,8 N. À un angle de 30 degrés, le sinus vaut 0,5, donc la force vaut 0,8 × 0,5 = 0,4 N. Si le conducteur était parallèle au champ, le sinus serait nul et la force disparaîtrait. Cette relation explique pourquoi les enroulements d'un moteur sont disposés pour être le plus possible perpendiculaires au champ afin de produire un couple maximal.",
        "On attend F = BIL pour 90 degrés et la multiplication par sin 30 = 0,5."),
     QT("Expliquer comment une bobine parcourue par un courant peut attirer une pièce de fer.",
        "Une bobine parcourue par un courant produit un champ magnétique analogue à celui d'un aimant. L'intensité de ce champ dépend du produit du courant par le nombre de spires et de la présence d'un noyau ferromagnétique. Le fer placé à proximité se aimante par influence : ses domaines magnétiques s'orientent dans le sens du champ et la pièce devient elle-même un aimant dont le pôle le plus proche est de signe opposé à celui de la bobine. Il en résulte une force d'attraction. C'est le principe du contacteur électromécanique : le courant de la bobine ferme les contacts de puissance par attraction du noyau mobile.",
        "La réponse doit relier courant, champ de la bobine, aimantation du fer et force d'attraction.")],
    C("Courant et champ magnétique sont liés : la force de Laplace transforme l'énergie électrique en mouvement.",
      "F = B I L sin alpha · ampères-tours = N I",
      "Lignes du nord vers le sud · tesla · règle de la main droite",
      "Induction B~Intensité du champ~Tesla~Ampères-tours~Produit N I~Bobine~Force de Laplace~B I L sin alpha~Direction",
      "Repérer le sens du courant et du champ|Tracer les lignes de champ|Calculer l'induction ou la force|Choisir l'angle favorable|Relier à l'application mécanique",
      "Confondre champ et induction|Oublier le sinus|Prendre la règle de la main droite pour la force|Ignorer le noyau ferromagnétique",
      "0,2 T et 8 A~0,5 m~F maximale 0,8 N~À 30 degrés~F = 0,4 N~Bobine~Aimantation du fer",
      "Champ magnétique~Région d'influence~Aimant ou courant~Champ électrique~Force sur les charges~Tension~Induction~Grandeur locale du champ~Tesla",
      "Main droite~Sens du champ créé par un courant~Autour du conducteur~Main gauche~Sens de la force sur le conducteur~Moteur"))

# ============================================================ EL15
add("PE-B15", "Inductance et bobinages", "Physique appliquée", ["Terminale pro"],
    S("Une bobine possède une inductance L qui exprime sa capacité à stocker de l'énergie magnétique."
      "|L'inductance se mesure en henry, symbole H."
      "|Elle dépend du nombre de spires, de la section et de la longueur du noyau, ainsi que de sa perméabilité."
      "|Le nombre de spires intervient au carré dans l'expression de l'inductance."
      "|Lorsque le courant varie, la bobine produit une tension dite de self-induction."
      "|Cette tension s'oppose à la variation du courant, conformément à la loi de Lenz."
      "|Son expression est e = - L di/dt, avec di/dt la vitesse de variation du courant."
      "|L'énergie stockée dans une bobine parcourue par un courant I vaut un demi L I²."
      "|En courant alternatif, la bobine présente une réactance inductive X_L = 2 π f L."
      "|Cette réactance augmente avec la fréquence : la bobine s'oppose davantage aux courants rapides."
      "|Dans un circuit en courant continu à l'état établi, une bobine idéale se comporte comme un court-circuit."
      "|Les bobines sont utilisées dans les filtres, les transformateurs, les moteurs et les contacteurs."),
    [QC("Quelle est l'unité de l'inductance ?", "Le farad~Le henry~Le tesla~L'ohm", 1,
        "L'inductance se mesure en henry, symbole H."),
     QC("Comment l'inductance varie-t-elle avec le nombre de spires ?", "Proportionnellement~Comme le carré du nombre de spires~En raison inverse~Elle ne dépend pas des spires", 1,
        "L'inductance est proportionnelle au carré du nombre de spires."),
     QC("Quelle est l'expression de la tension de self-induction ?", "e = L i~e = - L di/dt~e = L / i~e = di/dt", 1,
        "La tension induite est proportionnelle à la dérivée du courant et s'y oppose."),
     QC("Que stocke une bobine parcourue par un courant ?", "Une charge électrique~Une énergie magnétique~Une tension continue~Une chaleur utile", 1,
        "L'énergie stockée dans le champ magnétique vaut un demi L I²."),
     QC("Que vaut la réactance inductive d'une bobine ?", "X = 1 / (2 π f L)~X = 2 π f L~X = L / f~X = f L", 1,
        "La réactance inductive croît linéairement avec la fréquence."),
     QC("Que devient une bobine idéale en courant continu établi ?", "Un circuit ouvert~Un court-circuit~Une résistance infinie~Un condensateur", 1,
        "En régime permanent continu, di/dt est nul donc la tension induite est nulle."),
     QC("Quelle est la conséquence d'une coupure brutale du courant dans une bobine ?", "Une surtension~Une sous-tension~Aucun effet~Une baisse de fréquence", 0,
        "La self-induction s'oppose à la chute du courant et peut générer une surtension."),
     QT("Une bobine de 0,5 H est traversée par un courant de 4 A. Calculer l'énergie stockée, puis la tension induite si le courant tombe à zéro en 10 ms.",
        "L'énergie stockée vaut W = un demi L I² = 0,5 × 0,5 × 4² = 4 J. La variation de courant vaut di = -4 A en dt = 0,01 s, soit di/dt = -400 A/s. La tension de self-induction vaut e = - L di/dt = -0,5 × (-400) = 200 V. Cette tension positive s'oppose à la diminution du courant : elle tend à maintenir le courant dans la bobine. C'est pourquoi une diode de roue libre est nécessaire lors de la commande d'une bobine.",
        "On attend le calcul de l'énergie par 1/2 L I² puis de e = -L di/dt."),
     QT("Une bobine de 0,2 H est alimentée à 50 Hz. Calculer sa réactance inductive et expliquer son évolution à 500 Hz.",
        "La réactance inductive vaut X_L = 2 π f L = 2 × 3,14 × 50 × 0,2, soit environ 62,8 ohm. À 500 Hz, la fréquence est multipliée par dix, donc la réactance est également multipliée par dix et vaut environ 628 ohm. La bobine laisse donc passer le courant à basse fréquence mais s'oppose fortement aux courants de haute fréquence. Cette propriété est utilisée dans les bobines de filtrage et les selfs de blocage des variateurs.",
        "On attend le calcul à 50 Hz et la proportionnalité de la réactance avec la fréquence.")],
    C("L'inductance caractérise la capacité d'une bobine à stocker de l'énergie magnétique et à s'opposer aux variations de courant.",
      "W = 1/2 L I² · e = - L di/dt · X_L = 2 π f L",
      "L en henry · énergie en joules · réactance en ohms",
      "Inductance~Stockage magnétique~Henry~Self-induction~Opposition à la variation~Loi de Lenz~Réactance~2 π f L~Croît avec la fréquence",
      "Relever L et le courant|Calculer l'énergie stockée|Évaluer la vitesse de variation|Calculer la tension induite|Vérifier la réactance à la fréquence donnée",
      "Oublier le signe de Lenz|Confondre inductance et capacité|Utiliser la fréquence en radians par seconde|Négliger la surtension à la coupure",
      "0,5 H et 4 A~W = 4 J~Coupure en 10 ms~e = 200 V~0,2 H à 50 Hz~X = 62,8 ohm~À 500 Hz~628 ohm",
      "Bobine~Inductance série~S'oppose au courant variable~Condensateur~Capacité dérivation~S'oppose à la tension variable~Résistance~Dissipe l'énergie",
      "Régime continu~Réactance nulle~Court-circuit~Régime alternatif~Réactance croissante~Filtrage"))

# ============================================================ EL16
add("PE-B16", "Condensateurs et filtres", "Physique appliquée", ["Terminale pro"],
    S("Un condensateur est constitué de deux électrodes séparées par un diélectrique isolant."
      "|Sa capacité C se mesure en farad, symbole F, et dépend de la géométrie et du diélectrique."
      "|Un condensateur stocke une charge électrique et de l'énergie sous forme de champ électrique."
      "|La charge stockée vaut Q = C U et l'énergie vaut un demi C U²."
      "|La tension aux bornes d'un condensateur ne peut pas varier brutalement."
      "|En courant continu établi, un condensateur idéal est un circuit ouvert."
      "|En courant alternatif, il présente une réactance capacitive X_C = 1 / (2 π f C)."
      "|Cette réactance diminue lorsque la fréquence augmente."
      "|Le condensateur laisse donc passer les courants de haute fréquence et bloque le continu."
      "|Dans un redresseur, un condensateur en dérivation lisse la tension ondulée."
      "|Plus la capacité est grande, plus l'ondulation résiduelle est faible."
      "|La tension nominale du condensateur doit être supérieure à la tension de crête qu'il subit."),
    [QC("Quelle est l'unité de la capacité électrique ?", "Le henry~Le farad~Le tesla~Le watt", 1,
        "La capacité se mesure en farad, symbole F."),
     QC("Quelle est l'expression de la charge stockée ?", "Q = C / U~Q = C U~Q = U / C~Q = C + U", 1,
        "La charge vaut la capacité multipliée par la tension."),
     QC("Que vaut l'énergie stockée dans un condensateur ?", "C U²~un demi C U²~C U~deux C U²", 1,
        "L'énergie électrostatique vaut 1/2 C U²."),
     QC("Quelle est la réactance capacitive ?", "X = 2 π f C~X = 1 / (2 π f C)~X = f C~X = C / f", 1,
        "La réactance capacitive est inversement proportionnelle à la fréquence et à la capacité."),
     QC("Que devient un condensateur idéal en courant continu établi ?", "Un court-circuit~Un circuit ouvert~Une résistance~Une source", 1,
        "Une fois chargé, le condensateur ne laisse plus passer de courant continu."),
     QC("Que se passe-t-il quand la fréquence augmente ?", "La réactance capacitive augmente~La réactance capacitive diminue~La capacité double~La tension devient nulle", 1,
        "X_C = 1/(2 π f C) diminue quand la fréquence augmente."),
     QC("Quelle précaution pour le choix d'un condensateur de filtrage ?", "Choisir une tension nominale inférieure à la crête~Choisir une tension nominale supérieure à la crête~Ignorer la polarité~Le placer en série", 1,
        "La tension nominale doit supporter la valeur de crête, sinon le condensateur peut être détruit."),
     QT("Un condensateur de 100 µF est chargé sous 24 V. Calculer la charge et l'énergie stockées.",
        "On convertit la capacité : 100 µF = 100 × 10⁻⁶ F = 10⁻⁴ F. La charge vaut Q = C U = 10⁻⁴ × 24 = 2,4 × 10⁻³ C, soit 2,4 mC. L'énergie vaut W = un demi C U² = 0,5 × 10⁻⁴ × 24² = 0,5 × 10⁻⁴ × 576 = 2,88 × 10⁻² J, soit environ 28,8 mJ. On vérifie l'homogénéité avec W = un demi Q U = 0,5 × 2,4 × 10⁻³ × 24 = 28,8 mJ.",
        "On attend Q = C U et W = 1/2 C U² après conversion de la capacité."),
     QT("Un condensateur de 1 µF est soumis à une tension alternative de 50 Hz. Calculer sa réactance, puis celle à 1 kHz.",
        "À 50 Hz, X_C = 1 / (2 π × 50 × 10⁻⁶) = 1 / (3,14 × 10⁻³), soit environ 318 ohm. À 1000 Hz, la fréquence est multipliée par 20, donc la réactance est divisée par 20 et vaut environ 15,9 ohm. Le condensateur oppose donc une forte impédance aux basses fréquences et une faible impédance aux hautes fréquences. C'est ce comportement qui permet de réaliser des filtres passe-haut ou de découpler les composantes continues et alternatives d'un signal.",
        "On attend le calcul à 50 Hz et la variation en raison inverse de la fréquence.")],
    C("Le condensateur stocke de l'énergie électrostatique et laisse passer les hautes fréquences.",
      "Q = C U · W = 1/2 C U² · X_C = 1/(2 π f C)",
      "Farad · tension nominale supérieure à la crête · filtrage en dérivation",
      "Capacité~Stockage de charge~Farad~Réactance capacitive~Inversement proportionnelle à f~Filtrage~Condensateur en dérivation~Tension lissée~Ondulation",
      "Convertir la capacité en farads|Calculer la charge et l'énergie|Évaluer la réactance|Vérifier la tension nominale|Observer l'effet de filtrage",
      "Oublier la conversion des microfarads|Confondre capacité et inductance|Choix d'une tension trop faible|Inverser la loi de variation avec la fréquence",
      "100 µF sous 24 V~Q = 2,4 mC~W = 28,8 mJ~1 µF à 50 Hz~X = 318 ohm~À 1 kHz~15,9 ohm",
      "Condensateur~Bloque le continu~Laisse le alternatif~Bobine~Laisse le continu~Bloque le alternatif~Résistance~Dissipe sans stocker",
      "Filtrage~Réduction de l'ondulation~Condensateur en dérivation~Découplage~Séparation des composantes~Signal continu et alternatif"))

# ============================================================ EL17
add("PE-B17", "Symboles et schémas électriques normalisés", "Schémas et normes électriques", ["1re pro"],
    S("Un schéma électrique est un document normalisé qui représente les liaisons entre composants."
      "|Les symboles sont définis par les normes de la série NF EN 60617 et par la norme NF C 03-200."
      "|Un schéma de principe montre la fonction logique du circuit, indépendamment de l'implantation physique."
      "|Un schéma de câblage montre les conducteurs, les bornes et les connexions réelles de l'installation."
      "|Un plan d'implantation situe physiquement les appareils dans un local ou une armoire."
      "|Les conducteurs sont repérés par des indications comme L1, L2, L3, N et PE."
      "|Les bornes sont numérotées pour permettre un raccordement sans ambiguïté."
      "|Une liaison est représentée par un trait continu ; un point marque une connexion électrique."
      "|Le croisement de deux traits sans point signifie qu'il n'y a pas de connexion."
      "|Chaque appareil porte un identifiant unique, par exemple Q1 pour un disjoncteur ou KM1 pour un contacteur."
      "|Les schémas sont orientés selon un sens de lecture précis, généralement de gauche à droite et de haut en bas."
      "|Une documentation à jour est indispensable pour la maintenance et la sécurité des interventions."),
    [QC("Quelle norme définit les symboles graphiques des schémas électriques ?", "NF C 15-100~NF EN 60617~ISO 9001~NF S 31-100", 1,
        "La série NF EN 60617normalise les symboles des schémas électriques."),
     QC("Que montre un schéma de principe ?", "L'implantation physique~La fonction logique du circuit~La couleur des câbles~Le prix des composants", 1,
        "Le schéma de principe décrit la fonction, sans tenir compte de la disposition réelle."),
     QC("Quel repère désigne le conducteur de protection ?", "L1~N~PE~L2", 2,
        "PE désigne le conducteur de protection, relié à la terre."),
     QC("Que signifie un point à la croisée de deux conducteurs ?", "Une absence de liaison~Une connexion électrique~Une coupure~Une résistance", 1,
        "Le point marque une connexion ; sans point, les conducteurs se croisent sans être reliés."),
     QC("Quel identifiant désigne habituellement un contacteur ?", "Q1~KM1~FU1~X1", 1,
        "KM est l'identifiant normalisé d'un contacteur, FU celui d'un fusible."),
     QC("Dans quel sens lit-on généralement un schéma ?", "De droite à gauche~De gauche à droite et de haut en bas~Au hasard~De bas en haut", 1,
        "La lecture suit le sens gauche-droite et haut-bas."),
     QC("Pourquoi faut-il tenir le schéma à jour ?", "Pour le rendre plus beau~Pour garantir la sécurité et la maintenance~Pour augmenter la tension~Pour réduire le nombre de conducteurs", 1,
        "Un schéma exact est indispensable pour intervenir en sécurité et diagnostiquer une panne."),
     QT("Expliquer la différence entre un schéma de principe et un schéma de câblage.",
        "Le schéma de principe représente la fonction du circuit avec des symboles normalisés et des liaisons logiques : il montre comment l'énergie est distribuée et comment les organes de commande agissent. Le schéma de câblage, lui, représente la réalité physique : chaque conducteur, chaque borne et chaque appareil y sont identifiés avec leur repère et leur numéro de borne. Le premier sert à comprendre le fonctionnement, le second à raccorder et à vérifier l'installation. Les deux sont complémentaires et doivent être cohérents.",
        "On attend l'opposition entre fonction logique et réalité physique des connexions."),
     QT("Comment lire un schéma simple comportant un disjoncteur Q1, un contacteur KM1 et un moteur M1 ?",
        "On repère d'abord l'alimentation, en haut ou à gauche du schéma, puis on suit le chemin du courant. Le disjoncteur Q1 assure la protection contre les surintensités et l'isolement. Le contacteur KM1 comporte une bobine de commande et des contacts de puissance qui ouvrent ou ferment le circuit vers le moteur M1. Enfin, le moteur est repéré M1 et ses bornes sont numérotées. La lecture consiste à relier les contacts de commande à la bobine et à vérifier que la fermeture de KM1 alimente bien le moteur, tout en respectant le sens de lecture du schéma.",
        "La réponse doit suivre le chemin de l'alimentation et expliquer le rôle de Q1, KM1 et M1.")],
    C("Un schéma normalisé rend lisible une installation : symboles, repères et sens de lecture sont essentiels.",
      "NF EN 60617 pour les symboles · NF C 03-200 pour les repères",
      "L1, L2, L3, N, PE · Q1 disjoncteur · KM1 contacteur · M1 moteur",
      "Schéma de principe~Fonction logique~Symboles normalisés~Schéma de câblage~Connexions réelles~Bornes numérotées~Repère~Identifiant unique~Q1 ou KM1",
      "Identifier le type de schéma|Repérer l'alimentation|Suivre le chemin du courant|Lire les repères et bornes|Vérifier la cohérence avec l'installation",
      "Confondre schéma de principe et schéma de câblage|Ignorer les points de connexion|Oublier le repère PE|Travailler sur un schéma obsolète",
      "Q1~Disjoncteur~KM1~Contacteur~M1~Moteur~PE~Terre~L1 L2 L3~Phases",
      "Schéma de principe~Comprendre la fonction~Lecture logique~Schéma de câblage~Raccorder les bornes~Lecture physique~Plan d'implantation~Situer les appareils",
      "Point de connexion~Conducteurs reliés~Croisement sans point~Conducteurs indépendants~Trait continu~Liaison électrique"))

# ============================================================ EL18
add("PE-B18", "Norme NF C 15-100 et installations basse tension", "Schémas et normes électriques", ["Terminale pro"],
    S("La norme NF C 15-100 fixe les règles de conception et de réalisation des installations électriques basse tension."
      "|Elle s'applique aux installations domestiques, tertiaires et industrielles alimentées en basse tension."
      "|Une installation doit assurer la sécurité des personnes, des biens et le bon fonctionnement des équipements."
      "|La mise à la terre relie les masses métalliques accessibles à un conducteur de protection."
      "|Le conducteur de protection est repéré par les couleurs vert et jaune."
      "|Le conducteur neutre est repéré par la couleur bleue."
      "|Les phases sont repérées par des couleurs distinctes, par exemple brun, noir et gris."
      "|Un disjoncteur différentiel coupe le circuit lorsqu'un courant de fuite apparaît vers la terre."
      "|Le seuil de sensibilité courant pour la protection des personnes est de 30 milliampères."
      "|Une installation est organisée en circuits distincts : éclairage, prises, chauffage et machines."
      "|Chaque circuit possède sa propre protection contre les surcharges et les courts-circuits."
      "|La vérification et la mise en service doivent être documentées par un procès-verbal."),
    [QC("Que fixe la norme NF C 15-100 ?", "Le prix des câbles~Les règles des installations basse tension~La puissance des moteurs~La couleur des murs", 1,
        "La NF C 15-100 est la norme de référence des installations électriques basse tension."),
     QC("Quelle est la couleur du conducteur de protection ?", "Bleu~Vert et jaune~Brun~Rouge", 1,
        "Le conducteur de protection PE est vert et jaune."),
     QC("Quelle est la couleur du conducteur neutre ?", "Vert et jaune~Bleu~Gris~Noir", 1,
        "Le neutre est identifié par la couleur bleue."),
     QC("Que détecte un disjoncteur différentiel ?", "Une surcharge seulement~Un courant de fuite vers la terre~Une baisse de tension~Une surtension", 1,
        "Le différentiel compare le courant aller et retour et coupe en cas de fuite."),
     QC("Quel seuil de sensibilité est courant pour la protection des personnes ?", "30 mA~300 mA~30 A~3 mA", 0,
        "Un différentiel 30 mA est couramment utilisé pour protéger les personnes."),
     QC("Pourquoi séparer les circuits d'une installation ?", "Pour utiliser moins de câbles~Pour limiter les perturbations et adapter les protections~Pour augmenter la tension~Pour supprimer la terre", 1,
        "Des circuits séparés permettent une protection adaptée à chaque usage."),
     QC("Quel document atteste de la vérification d'une installation ?", "Une facture~Un procès-verbal de vérification~Un schéma de principe seul~Un bon de commande", 1,
        "La mise en service donne lieu à un procès-verbal consignant les contrôles effectués."),
     QT("Expliquer le rôle de la mise à la terre dans une installation électrique.",
        "La mise à la terre relie les masses métalliques des appareils et les parties conductrices accessibles à la terre par un conducteur de protection vert et jaune. En cas de défaut d'isolement, le courant de fuite s'écoule vers la terre au lieu de traverser une personne. Ce courant est détecté par le disjoncteur différentiel, qui coupe l'alimentation rapidement. La mise à la terre stabilise également le potentiel des installations et facilite l'écoulement des courants de défaut. Elle ne remplace pas le différentiel : les deux mesures sont complémentaires.",
        "On attend le lien entre masses, conducteur de protection, fuite et coupure différentielle."),
     QT("Décrire les grandes étapes de la vérification d'une installation avant mise sous tension.",
        "On compare d'abord l'installation réalisée avec les schémas et le cahier des charges. On vérifie ensuite la continuité du conducteur de protection et des liaisons équipotentielles, ainsi que la valeur de la résistance de terre. On contrôle l'isolement des conducteurs entre eux et par rapport à la terre avec un ohmmètre ou un testeur adapté. On vérifie le repérage des conducteurs, la section des câbles, les raccordements et le calibrage des protections. On teste enfin le fonctionnement des différentiels et la cohérence des circuits, puis on consigne les résultats dans un procès-verbal avant la mise en service.",
        "La réponse doit citer conformité au schéma, continuité terre, isolement, protection et procès-verbal.")],
    C("La NF C 15-100 organise la sécurité des installations : terre, repérage, protection et vérification.",
      "PE = vert et jaune · neutre = bleu · différentiel 30 mA",
      "Circuits séparés · surcharge et court-circuit · procès-verbal de mise en service",
      "NF C 15-100~Règles d'installation~Basse tension~Mise à la terre~Masses reliées~Conducteur PE~Différentiel~Courant de fuite~30 mA",
      "Consulter la norme et les schémas|Vérifier la continuité de la terre|Contrôler l'isolement|Tester les protections|Rédiger le procès-verbal",
      "Inverser les couleurs des conducteurs|Oublier le conducteur de protection|Régler un différentiel trop sensible au-delà de la norme|Mettre sous tension sans vérification",
      "Vert et jaune~Terre~Bleu~Neutre~30 mA~Protection personnes~Disjoncteur~Surcharge et court-circuit~PV~Mise en service",
      "Surcharge~Courant supérieur au calibrage~Disjoncteur thermique~Court-circuit~Courant très élevé~Disjoncteur magnétique~Fuite~Courant vers la terre~Différentiel",
      "Mise à la terre~Liaison à la terre~Sécurité des personnes~Neutre~Conducteur de retour~Repérage bleu~Phase~Conducteur actif"))

# ============================================================ EL19
add("PE-B19", "Schémas de câblage et plan de bornier", "Schémas et normes électriques", ["1re pro"],
    S("Un schéma de câblage décrit les liaisons électriques réelles entre les appareils d'une armoire."
      "|Il Complète le schéma de principe en précisant les bornes et les numéros de conducteurs."
      "|Chaque appareil possède un repère unique et un bornier identifié."
      "|Un plan de bornier regroupe les connexions entrantes et sortantes d'un ensemble."
      "|Sur un plan de bornier, chaque borne porte un numéro et une désignation fonctionnelle."
      "|Les conducteurs portent un numéro de fil qui doit rester le même d'une extrémité à l'autre."
      "|Le repérage des fils peut être réalisé par des manchons ou des étiquettes."
      "|Un conducteur est raccordé à une borne par un connecteur adapté à sa section."
      "|Le desserrage et le resserrage des bornes doivent respecter le couple de serrage prescrit."
      "|Une borne ne doit jamais recevoir plus de conducteurs que le constructeur ne l'autorise."
      "|Le schéma de câblage sert au montage, au contrôle qualité et au diagnostic de panne."
      "|Toute modification réalisée sur chantier doit être reportée sur les documents."),
    [QC("Quelle information un schéma de câblage apporte-t-il en plus du schéma de principe ?", "La couleur de l'armoire~Les bornes et les numéros de conducteurs~Le prix des appareils~La date de fabrication", 1,
        "Le schéma de câblage précise les connexions réelles et les repères de bornes."),
     QC("Qu'appelle-t-on un plan de bornier ?", "Un plan de montage mécanique~Le regroupement des connexions entrantes et sortantes~Un schéma de principe~Une facture", 1,
        "Le plan de bornier liste les bornes et leur fonction."),
     QC("Que doit-on conserver identique d'une extrémité à l'autre d'un conducteur ?", "La couleur de la gaine~Le numéro de fil~La longueur~Le diamètre", 1,
        "Le numéro de fil garantit la traçabilité de la liaison."),
     QC("Comment repère-t-on les fils de façon durable ?", "Par un trait de craie~Par des manchons ou des étiquettes~Par la mémoire~Par le sens du câble", 1,
        "Les manchons et étiquettes assurent un repérage lisible et durable."),
     QC("Que faut-il respecter lors du serrage d'une borne ?", "Le couple de serrage prescrit~La couleur du tournevis~Le nombre de spires~La température", 0,
        "Un serrage conforme évite les échauffements et les desserrages."),
     QC("Quel risque présente une borne surchargée de conducteurs ?", "Une tension plus élevée~Un échauffement et un mauvais contact~Une fréquence plus basse~Aucun risque", 1,
        "Trop de conducteurs sur une borne détériore le contact et provoque des échauffements."),
     QC("Que faut-il faire après une modification sur chantier ?", "Rien~Reporter la modification sur les documents~Changer le schéma de principe uniquement~Effacer l'ancien repère", 1,
        "La documentation doit toujours refléter l'installation réelle."),
     QT("Expliquer la différence entre numéro de borne et numéro de fil sur un schéma de câblage.",
        "Le numéro de borne identifie le point de connexion sur un appareil ou un bornier : il est propre à l'appareil, par exemple la borne 13 d'un contacteur. Le numéro de fil identifie le conducteur lui-même et reste le même à ses deux extrémités : le fil 105 relie la borne 13 du contacteur à la borne 2 du moteur. La borne décrit où l'on se connecte, le fil décrit ce qui relie deux points. Cette distinction permet de retrouver rapidement une liaison lors du câblage ou du diagnostic d'une panne.",
        "On attend que la borne appartienne à un appareil et que le fil identifie le conducteur sur toute sa longueur."),
     QT("Décrire la démarche de câblage d'une armoire à partir d'un plan de bornier.",
        "On commence par comparer le plan de bornier avec le schéma de principe pour vérifier la cohérence des repères. On repère ensuite les appareils et leurs bornes dans l'armoire, puis on prépare les conducteurs à la bonne section et à la bonne longueur. Chaque fil reçoit son numéro à chaque extrémité. On raccorde les conducteurs en respectant le couple de serrage et le nombre maximum de fils par borne. On contrôle ensuite la continuité de chaque liaison à l'aide du plan, puis on vérifie l'absence de court-circuit avant la mise sous tension. Enfin, on reporte sur les documents toute modification apportée pendant le montage.",
        "La réponse doit suivre : cohérence des documents, préparation, repérage, raccordement, contrôle et mise à jour.")],
    C("Le schéma de câblage et le plan de bornier rendent chaque liaison identifiable et vérifiable.",
      "Repère appareil + numéro de borne + numéro de fil",
      "Manchons d'identification · couple de serrage · documentation mise à jour",
      "Schéma de câblage~Liaisons réelles~Bornes numérotées~Plan de bornier~Entrées et sorties~Désignation fonctionnelle~Numéro de fil~Traçabilité~Manchons",
      "Comparer schéma de principe et plan de bornier|Repérer les appareils et les bornes|Préparer et étiqueter les conducteurs|Raccorder en respectant le serrage|Contrôler la continuité et documenter",
      "Changer le numéro d'un fil en cours de route|Surcharger une borne|Oublier de serrer au couple prescrit|Ne pas mettre à jour les documents",
      "Borne 13~Point de connexion~Fil 105~Liaison complète~Manchon~Repérage durable~Couple~Serrage conforme~PV~Document final",
      "Schéma de principe~Fonction et logique~Schéma de câblage~Réalité et bornes~Plan de bornier~Liste des connexions~Plan d'implantation~Position des appareils",
      "Numéro de borne~Appartient à l'appareil~Numéro de fil~Identifie le conducteur~Repère appareil~Identifiant unique"))

# ============================================================ EL20
add("PE-B20", "Mesures électriques et incertitudes", "Physique appliquée", ["Terminale pro"],
    S("Une mesure électrique associe une valeur numérique et une unité, accompanied d'une incertitude."
      "|L'incertitude traduit le doute qui subsiste sur la valeur vraie de la grandeur mesurée."
      "|Les instruments affichent une classe de précision, souvent exprimée en pourcentage de la valeur maximale."
      "|Un voltmètre possède une résistance interne élevée pour perturber le moins possible le circuit."
      "|Un ampèremètre possède une résistance interne faible et se place en série."
      "|La résistance interne d'appareil provoque une erreur de mesure appelée erreur de chargement."
      "|La valeur absolue de l'incertitude s'exprime dans la même unité que la mesure."
      "|L'incertitude relative est le rapport entre l'incertitude absolue et la valeur mesurée."
      "|Le résultat s'écrit avec le nombre de chiffres significatifs cohérent avec l'incertitude."
      "|Une mesure directe est lue sur l'instrument ; une mesure indirecte est calculée à partir d'autres grandeurs."
      "|Pour une mesure indirecte, les incertitudes se propagent selon les opérations effectuées."
      "|Un étalonnage régulier garantit la traçabilité des mesures à une référence connue."),
    [QC("Qu'appelle-t-on incertitude de mesure ?", "La valeur exacte~Le doute sur la valeur vraie~L'unité de la grandeur~La classe de l'instrument", 1,
        "L'incertitude quantifie l'intervalle dans lequel se situe la valeur vraie."),
     QC("Comment est placé un ampèremètre ?", "En dérivation~En série~Au bornier de terre~Sans raccordement", 1,
        "L'ampèremètre s'insère dans le circuit en série et possède une faible résistance interne."),
     QC("Quelle résistance interne caractéristique un voltmètre ?", "Très faible~Très élevée~Nulle~Variable", 1,
        "Une résistance élevée limite le courant prélevé et donc la perturbation."),
     QC("Que vaut l'incertitude relative ?", "Incertitude absolue multipliée par la mesure~Incertitude absolue divisée par la mesure~Mesure divisée par l'incertitude~Incertitude absolue plus mesure", 1,
        "L'incertitude relative est un rapport sans unité, souvent exprimé en pourcentage."),
     QC("Qu'est-ce qu'une mesure indirecte ?", "Une mesure lue directement~Une mesure calculée à partir d'autres grandeurs~Une mesure sans instrument~Une mesure approchée", 1,
        "Une grandeur calculée, comme une puissance, est une mesure indirecte."),
     QC("Que permet un étalonnage régulier ?", "Changer l'unité~Garantir la traçabilité à une référence~Supprimer les incertitudes~Augmenter la tension", 1,
        "L'étalonnage compare l'instrument à une référence et documente ses écarts."),
     QC("Combien de chiffres significatifs faut-il afficher ?", "Le plus possible~Ceux qui sont cohérents avec l'incertitude~Toujours trois~Aucun", 1,
        "Afficher trop de chiffres donnerait une précision fictive."),
     QT("Une tension est mesurée à 12,4 V avec une incertitude absolue de 0,2 V. Donner l'incertitude relative et l'écriture du résultat.",
        "L'incertitude relative vaut 0,2 / 12,4, soit environ 0,0161, donc 1,6 %. Le résultat peut s'écrire U = (12,4 ± 0,2) V. L'incertitude porte sur le premier chiffre après la virgule, il est donc cohérent de conserver une seule décimale. Écrire 12,400 V suggérerait une précision que l'instrument ne possède pas. Une mesure ainsi encadrée signifie que la valeur vraie se situe très probablement entre 12,2 V et 12,6 V.",
        "On attend le rapport 0,2/12,4, le pourcentage et l'écriture avec chiffres cohérents."),
     QT("Une puissance est calculée par P = U I avec U = 12,0 ± 0,2 V et I = 2,00 ± 0,02 A. Calculer P et estimer son incertitude relative.",
        "La puissance vaut P = 12,0 × 2,00 = 24,0 W. Pour un produit, les incertitudes relatives s'ajoutent en première approximation. Celle de U vaut 0,2 / 12,0 = 1,67 % et celle de I vaut 0,02 / 2,00 = 1,00 %. L'incertitude relative de la puissance vaut donc environ 2,67 %, soit une incertitude absolue de 24,0 × 0,0267 = 0,64 W. On écrira P = (24,0 ± 0,6) W. Le résultat montre que l'incertitude de la tension, plus grande, domine la précision finale.",
        "La réponse doit calculer le produit puis additionner les incertitudes relatives pour un produit.")],
    C("Une mesure complète donne une valeur, une unité et une incertitude cohérente avec la précision de l'instrument.",
      "Incertitude relative = incertitude absolue / valeur mesurée",
      "Produit : les incertitudes relatives s'ajoutent · étalonnage et traçabilité",
      "Incertitude~Doute sur la valeur~Absolue ou relative~Classe de précision~Pourcentage du fond d'échelle~Instrument~Erreur de chargement~Résistance interne",
      "Choisir l'instrument et la gamme|Lire la valeur et l'unité|Estimer l'incertitude absolue|Calculer l'incertitude relative|Écrire le résultat avec les bons chiffres",
      "Afficher trop de décimales|Confondre incertitude absolue et relative|Brancher l'ampèremètre en dérivation|Oublier l'étalonnage",
      "12,4 V ± 0,2 V~Incertitude relative 1,6 %~12,0 V et 2,00 A~P = 24,0 W~Incertitude 2,67 %~P = 24,0 ± 0,6 W",
      "Mesure directe~Lecture sur l'instrument~Voltmètre~Mesure indirecte~Calcul à partir d'autres grandeurs~Puissance UI~Erreur systématique~Biais répétable~Erreur aléatoire~Dispersion",
      "Voltmètre~Forte résistance interne~En dérivation~Ampèremètre~Faible résistance interne~En série"))

valider_et_ecrire(F, "pro-electricite-mat-part-B.json")
