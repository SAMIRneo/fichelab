# -*- coding: utf-8 -*-
"""Generateur pro-gestion-mat-part-B.json — lot B : economie, comptabilite, droit (20 fiches).

Economie et gestion (7), Comptabilité (7), Droit et gestion administrative,
comptable, financière (6).
12 points, 9 questions corrigees (7 QCM + 2 texte), 7 blocs ordonnes, 3 SVG.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _progestion_common import S, R, QC, QT, C, build, valider_et_ecrire

F = []


def add(prefix, titre, mat, ans, points, questions, c):
    F.append(build(prefix, titre, mat, ans, points, questions, c))


# ============================================================ EG1
add("EG1", "Les besoins, les biens et le fonctionnement d'un marché", "Économie et gestion", ["2nde pro", "1re pro"],
S("Un besoin est un manque ressenti par un individu ou un groupe : il peut être physiologique, social ou culturel."
  "|Un désir est la forme que prend un besoin lorsqu'il s'adresse à un produit ou à un service précis."
  "|Les biens et les services sont les moyens qui permettent de satisfaire les besoins : un bien est matériel, un service est immatériel."
  "|Un bien privé est rival et excluable : sa consommation par l'un prive les autres et l'accès peut être limité."
  "|Un bien public n'est ni rival ni excluable, comme la défense nationale ou l'éclairage public, et il est souvent financé par l'impôt."
  "|Un marché est le lieu, physique ou virtuel, où se rencontrent l'offre et la demande pour aboutir à un échange."
  "|Les acteurs du marché sont les consommateurs, les producteurs, les distributeurs, les intermédiaires et les pouvoirs publics."
  "|La demande représente les quantités que les consommateurs sont disposés et capables d'acheter à différents niveaux de prix."
  "|L'offre représente les quantités que les producteurs sont disposés et capables de vendre à différents niveaux de prix."
  "|Le prix d'équilibre est celui pour lequel la quantité offerte égale la quantité demandée : le marché s'y stabilise."
  "|Les études de marché combinent des données secondaires, déjà existantes, et des données primaires recueillies par enquête ou observation."
  "|La segmentation divise un marché en groupes de consommateurs aux besoins proches, afin de choisir une cible et un positionnement."),
[QC("Quel est un besoin physiologique ?", "Le besoin de se nourrir~Le besoin d'appartenir à un groupe~Le besoin de reconnaissance~Le besoin de loisir", 0,
     "Se nourrir répond à un besoin biologique de survie, contrairement aux besoins sociaux."),
 QC("Quelle est une différence entre un bien et un service ?", "Le bien est immatériel~Le bien est matériel et le service est immatériel~Le service est toujours gratuit~Il n'y a aucune différence", 1,
     "Un bien est un objet matériel ; un service est une prestation immatérielle."),
 QC("Quelles sont les deux caractéristiques d'un bien public ?", "Rival et excluable~Non rival et non excluable~Rival et non excluable~Non rival et excluable", 1,
     "La consommation de l'un ne prive pas les autres et l'accès ne peut pas être restreint."),
 QC("Qui représente l'offre sur un marché ?", "Les consommateurs~Les producteurs~L'État seul~Les banques seules", 1,
     "Les producteurs ou vendeurs proposent des biens et des services."),
 QC("Quand le marché est-il en équilibre ?", "Quand la demande dépasse l'offre~Quand l'offre égale la demande~Quand les prix sont nuls~Quand l'État fixe le prix", 1,
     "L'équilibre correspond à l'égalité des quantités offertes et demandées."),
 QC("Qu'appelle-t-on données primaires ?", "Des données publiées par l'Insee~Des données collectées directement pour l'étude~Des données gratuites~Des données anciennes", 1,
     "Les données primaires sont recueillies spécifiquement par enquête, entretien ou observation."),
 QC("Quel est l'objectif de la segmentation ?", "Augmenter le nombre de produits~Regrouper des consommateurs aux besoins similaires~Supprimer la concurrence~Fixer les prix", 1,
     "On découpe le marché pour identifier une cible et adapter l'offre."),
 QT("Expliquer pourquoi un prix trop élevé ne peut pas se maintenir durablement sur un marché concurrentiel.",
     "À un prix trop élevé, la quantité offerte dépasse la quantité demandée : il apparaît un excédent d'offre, c'est-à-dire des invendus. Les vendeurs, pour écouler leurs stocks, sont incités à baisser leur prix. Cette baisse stimule la demande et réduit l'offre jusqu'à ce que les quantités s'équilibrent. Inversement, un prix trop bas crée une pénurie et pousse les acheteurs à accepter un prix plus élevé. Sur un marché concurrentiel, la confrontation de l'offre et de la demande tend donc vers un prix d'équilibre, même si des facteurs comme la réglementation ou la rareté peuvent le faire varier.",
     "On décrit l'excédent d'offre, la pression à la baisse et le retour à l'équilibre."),
 QT("Distinguer étude de marché documentaire et étude de terrain, puis indiquer quand les utiliser.",
     "L'étude documentaire exploite des données secondaires : statistiques Insee, rapports sectoriels, chiffres de la concurrence, études déjà publiées. Elle est rapide et peu coûteuse et permet de cadrer le projet. L'étude de terrain recueille des données primaires par questionnaire, entretien, observation ou test produit : elle coûte plus cher mais donne une information adaptée au problème précis. En pratique, on commence par l'étude documentaire pour définir les hypothèses et la cible, puis on la complète par une enquête de terrain pour valider les attentes réelles des clients avant de lancer l'offre.",
     "On oppose données secondaires et primaires, puis on propose un enchaînement logique.")],
C("Le marché met en relation une offre et une demande ; le prix y est le signal qui révèle les tensions.",
  "Équilibre : quantité offerte = quantité demandée",
  "Bien privé : rival et excluable · bien public : ni rival ni excluable",
  "Besoin~Manque ressenti~Bien~Matériel et rival~Service~Immatériel~Marche~Rencontre offre et demande~Equilibre~Prix de rencontre",
  "Identifier le besoin|Préciser le bien ou le service|Repérer les acteurs|Analyser offre et demande|Construire l'étude de marché",
  "Confondre besoin et désir|Croire que tout bien est rival|Oublier les données primaires|Confondre offre et demande",
  "Prix d'equilibre~Offre egale demande~Bien public~Non rival et non excluable~Donnees secondaires~Deja publiees~Segmentation~Groupes homogenes",
  "Bien prive~Rival et excluable~Bien public~Ni rival ni excluable",
  "Donnees primaires~Collectees pour l'etude~Donnees secondaires~Deja existantes"))

# ============================================================ EG2
add("EG2", "L'offre, la demande et la formation des prix", "Économie et gestion", ["1re pro"],
S("La loi de la demande énonce que, toutes choses égales par ailleurs, une hausse du prix entraîne une baisse de la quantité demandée."
  "|La loi de l'offre énonce qu'une hausse du prix entraîne une hausse de la quantité offerte, les autres facteurs restant constants."
  "|La courbe de demande est décroissante : elle représente les quantités souhaitées à chaque prix."
  "|La courbe d'offre est croissante : elle représente les quantités que les producteurs acceptent de vendre à chaque prix."
  "|Le prix d'équilibre se situe à l'intersection des deux courbes ; il satisfait simultanément acheteurs et vendeurs."
  "|Un prix inférieur à l'équilibre crée une pénurie : la demande dépasse l'offre et les acheteurs se disputent le produit."
  "|Un prix supérieur à l'équilibre crée un excédent : l'offre dépasse la demande et les stocks s'accumulent."
  "|Les déterminants de la demande sont le revenu, le prix des produits substituables ou complémentaires, les goûts et les attentes."
  "|Les déterminants de l'offre sont le coût de production, la technologie, le nombre de producteurs, les taxes et les subventions."
  "|Un déplacement de courbe diffère d'un mouvement le long de la courbe : le premier change les données, le second suit une variation de prix."
  "|L'élasticité-prix de la demande mesure la sensibilité de la quantité demandée à une variation du prix."
  "|Une demande est rigide quand l'élasticité est inférieure à 1 et élastique quand elle est supérieure à 1, ce qui influe sur la politique de prix."),
[QC("Que se passe-t-il si le prix augmente, selon la loi de la demande ?", "La quantité demandée augmente~La quantité demandée diminue~La demande disparaît~Le prix n'a aucun effet", 1,
     "La relation entre prix et quantité demandée est décroissante."),
 QC("Quelle est la pente de la courbe d'offre ?", "Décroissante~Croissante~Horizontale~Verticale", 1,
     "Plus le prix est élevé, plus les producteurs offrent de quantités."),
 QC("Que désigne un prix inférieur à l'équilibre ?", "Un excédent~Une pénurie~Un prix plancher~Un équilibre", 1,
     "La demande dépasse alors l'offre : il manque des unités."),
 QC("Quel facteur déplace la courbe de demande ?", "Une variation du prix du produit~Une hausse du revenu des consommateurs~Une variation de la quantité~Un changement d'échelle", 1,
     "Le revenu est un déterminant : la courbe se déplace, on ne se contente pas de glisser dessus."),
 QC("Qu'appelle-t-on produit substituable ?", "Un produit complémentaire~Un produit qui peut le remplacer~Un produit importé~Un produit de luxe", 1,
     "Le thé et le café sont par exemple des substituables."),
 QC("Que mesure l'élasticité-prix ?", "Le coût de production~La sensibilité de la quantité au prix~La durée de vie du produit~Le nombre de concurrents", 1,
     "Elle compare la variation relative de quantité à la variation relative du prix."),
 QC("Quelle demande est qualifiée de rigide ?", "Élasticité supérieure à 1~Élasticité inférieure à 1~Élasticité nulle seulement~Élasticité égale à 1", 1,
     "Une élasticité inférieure à 1 signale une faible réaction de la quantité au prix."),
 QT("Expliquer comment le marché corrige spontanément un excédent d'offre.",
     "À un prix supérieur au prix d'équilibre, les producteurs offrent plus que ce que les consommateurs souhaitent acheter : il se constitue un stock invendu. Pour écouler ce stock, les vendeurs réduisent leur prix, éventuellement sous la pression de la concurrence. Cette baisse rend le produit plus attractif, donc la quantité demandée augmente, tandis que certains producteurs réduisent leur offre parce que la marge diminue. Le processus se poursuit jusqu'au prix d'équilibre, où l'offre et la demande s'égalisent. Dans la réalité, des facteurs comme les contrats de livraison ou les prix administrés peuvent ralentir cet ajustement.",
     "On décrit l'excédent, la baisse des prix, la hausse de la demande et la baisse de l'offre."),
 QT("Un produit a une demande rigide. Quelles conséquences pour la politique de prix de l'entreprise ?",
     "Une demande rigide signifie que l'élasticité est inférieure à 1 : une hausse de 10 % du prix ne réduit la quantité vendue que de moins de 10 %. Le chiffre d'affaires, qui est le produit du prix par la quantité, augmente donc lors d'un relèvement de prix. L'entreprise a intérêt à augmenter son prix si ses coûts unitaires stagnent, à condition de ne pas fragiliser son image ou sa relation client. À l'inverse, une baisse de prix diminuerait son chiffre d'affaires sans gains de volume suffisants. Cette analyse reste à croiser avec la réaction des concurrents et avec le seuil de saturation du marché.",
     "On relie élasticité inférieure à 1, effet sur le chiffre d'affaires et décision stratégique.")],
C("Offre et demande se rencontrent en un prix d'équilibre ; les écarts de prix créent pénurie ou excédent.",
  "Prix d'équilibre : offre = demande · élasticité = variation % quantité / variation % prix",
  "Pénurie si prix < équilibre · excédent si prix > équilibre",
  "Loi de la demande~Prix monte, quantite baisse~Loi de l'offre~Prix monte, quantite monte~Equilibre~Intersection des courbes~Elasticite~Sensibilite au prix",
  "Tracer les deux courbes|Repérer le point d'intersection|Identifier l'écart entre offre et demande|Analyser les déterminants|Calculer l'élasticité",
  "Confondre mouvement le long d'une courbe et déplacement|Croire qu'une hausse de prix augmente toujours les ventes|Oublier les déterminants|Ignorer la concurrence",
  "Prix sous l'equilibre~Pénurie~Prix au-dessus~Excedent et stocks~Elasticite 0,5~Demande rigide~Elasticite 1,5~Demande elastique",
  "Pénurie~Demande superieure a l'offre~Excedent~Offre superieure a la demande",
  "Rigide~Elasticite < 1~Elastique~Elasticite > 1"))

# ============================================================ EG3
add("EG3", "La concurrence et les stratégies de l'entreprise", "Économie et gestion", ["1re pro", "Terminale pro"],
S("La concurrence oppose des entreprises qui cherchent à satisfaire les mêmes besoins pour gagner des clients et des parts de marché."
  "|Dans une concurrence pure et parfaite, de nombreux offreurs vendent un produit homogène et aucun ne peut influencer le prix."
  "|Le monopole suppose un seul offreur, peu de substituables et des barrières à l'entrée comme un brevet ou un coût élevé."
  "|L'oligopole réunit un petit nombre d'entreprises dont les décisions sont interdépendantes : une baisse de prix de l'une provoque une réaction des autres."
  "|La concurrence monopolistique associe de nombreux offreurs et des produits différenciés par la marque, la qualité ou le service."
  "|Les barrières à l'entrée peuvent être juridiques, technologiques, financières ou commerciales."
  "|Une stratégie de différenciation vise à rendre l'offre unique sur un critère valorisé par le client."
  "|Une stratégie de domination par les coûts vise à proposer un prix inférieur à celui des concurrents grâce à une productivité élevée."
  "|La concentration s'accroît lorsque des entreprises fusionnent ou s'allient : elle peut renforcer leur pouvoir de marché."
  "|Le pouvoir de négociation dépend du nombre et de la taille des acteurs, ainsi que de la dépendance entre eux."
  "|Le positionnement stratégique combine le choix d'une cible, les avantages concurrentiels et les moyens mis en œuvre."
  "|L'assistant de gestion contribue à cette analyse en consolidant les chiffres de ventes, les marges et les données de la concurrence."),
[QC("Quelle situation correspond à un seul offreur ?", "L'oligopole~Le monopole~La concurrence parfaite~La concurrence monopolistique", 1,
     "Le monopole se caractérise par un seul vendeur et des barrières à l'entrée."),
 QC("Quel critère définit la concurrence pure et parfaite ?", "Un seul acheteur~Un produit homogène et de nombreux offreurs~Une marque célèbre~Un brevet", 1,
     "L'homogénéité du produit et l'atomicité des offreurs sont deux conditions du modèle."),
 QC("Pourquoi les entreprises d'un oligopole sont-elles interdépendantes ?", "Elles vendent toutes le même prix~Une décision de l'une provoque la réaction des autres~Elles sont toutes publiques~Elles n'ont pas de clients communs", 1,
     "Le petit nombre d'acteurs rend chaque décision visible et stratégique."),
 QC("Quel est un exemple de barrière juridique à l'entrée ?", "Un brevet~Une nouvelle usine~Un réseau de distribution~Une campagne publicitaire", 0,
     "Le brevet protège légalement une invention et bloque l'entrée des concurrents."),
 QC("En quoi consiste une stratégie de différenciation ?", "À vendre moins cher que tous~À rendre l'offre unique sur un critère valorisé~À supprimer la publicité~À copier le concurrent", 1,
     "La différenciation repose sur une caracteristique perçue comme supérieure ou unique."),
 QC("Quel est l'objectif d'une domination par les coûts ?", "Augmenter les prix~Obtenir un coût unitaire plus faible que la concurrence~Réduire les ventes~Changer de clientèle", 1,
     "Une productivité élevée permet de proposer un prix compétitif tout en conservant une marge."),
 QC("Quel outil aide à consolider l'analyse de la concurrence ?", "Le plan comptable~Le suivi des ventes et des marges~Le code du travail~Le tableau d'amortissement", 1,
     "Les données commerciales et financières alimentent le diagnostic stratégique."),
 QT("Comparer monopole et oligopole du point de vue du pouvoir de marché.",
     "Dans un monopole, une seule entreprise contrôle l'offre : elle peut influencer le prix et le volume, mais elle reste limitée par la demande et par la menace d'entrée. Dans un oligopole, quelques entreprises se partagent le marché : chacune détient un pouvoir certain, mais ses choix dépendent des réactions probables des autres. Cette interdépendance crée des situations de coopération tacite ou de guerre des prix, et justifie le contrôle des concentrations par les autorités de la concurrence. Dans les deux cas, le pouvoir de marché réduit la pression concurrentielle et peut nuire aux consommateurs si aucune régulation ne s'applique.",
     "On oppose pouvoir unilatéral et interdépendance stratégique, puis on évoque la régulation."),
 QT("Une entreprise veut se lancer sur un marché saturé. Quelle démarche stratégique recommandez-vous ?",
     "On commence par analyser le marché : taille, croissance, parts de marché des concurrents, barrières à l'entrée et attentes des clients non satisfaites. On réalise ensuite un diagnostic interne des ressources et des compétences, puis on choisit une cible précise plutôt que de s'adresser à tous. On construit un avantage concurrentiel, par différenciation sur un service, une qualité ou une expertise, ou par maîtrise des coûts sur un segment particulier. On vérifie enfin la cohérence du modèle économique : prix, marge, volume nécessaire et investissements. Un test à petite échelle permet de valider les hypothèses avant un déploiement plus large.",
     "On attend analyse du marché, diagnostic interne, choix d'une cible, avantage concurrentiel et test.")],
C("La concurrence structure le pouvoir de marché ; l'entreprise répond par un positionnement et un avantage durable.",
  "Concurrence parfaite : produit homogène et nombreux offreurs",
  "Monopole : un offreur · oligopole : peu d'offreurs interdépendants",
  "Concurrence~Rivalite pour les clients~Monopole~Un seul offreur~Oligopole~Peu d'offreurs lies~Barriere~Empeche l'entree~Differentiation~Offre unique",
  "Analyser la structure du marché|Repérer les barrières à l'entrée|Évaluer le pouvoir de négociation|Choisir la cible|Construire un avantage durable",
  "Confondre monopole et oligopole|Ignorer les réactions des concurrents|Copier sans différenciation|Oublier les barrières à l'entrée",
  "Brevet~Barriere juridique~Oligopole~Interdependance~Marque~Differentiation~Couts~Domination par les couts~Parts de marche~Indicateur cle",
  "Monopole~Pouvoir sur le prix~Concurrence parfaite~Prix subi par l'entreprise",
  "Differentiation~Valeur perceue~Domination par les couts~Prix bas et productivite"))

# ============================================================ EG4
add("EG4", "La production et la chaîne de valeur", "Économie et gestion", ["1re pro"],
S("La production est la transformation de facteurs de production, travail et capital, en biens ou en services destinés à satisfaire des besoins."
  "|Les facteurs de production sont le travail, le capital, la terre et, pour l'entreprise moderne, l'information et la technologie."
  "|La productivité mesure le rapport entre la production obtenue et les moyens utilisés, par exemple la valeur ajoutée par salarié."
  "|La valeur ajoutée est la différence entre la valeur de la production et la valeur des consommations intermédiaires."
  "|Les consommations intermédiaires sont les biens et services consommés au cours du processus de production : matières, énergie, sous-traitance."
  "|La chaîne de valeur décrit l'enchaînement des activités qui créent de la valeur, de la conception à la livraison et au service après-vente."
  "|Les activités principales comprennent la recherche, la production, la logistique, la commercialisation et le service."
  "|Les activités de soutien, comme la gestion des ressources humaines, la finance ou le système d'information, rendent possible l'ensemble."
  "|Un processus est un ensemble d'activités liées qui transforment une entrée en sortie pour un client interne ou externe."
  "|L'externalisation consiste à confier une activité à un prestataire extérieur pour se concentrer sur le cœur de métier."
  "|La sous-traitance comporte des risques de dépendance, de qualité et de confidentialité qui doivent être encadrés contractuellement."
  "|Le suivi des flux physiques et d'information permet de détecter les goulots d'étranglement et d'améliorer la productivité globale."),
[QC("Que sont les consommations intermédiaires ?", "Les salaires versés~Les biens et services consommés pendant la production~Les immobilisations durables~Les dividendes", 1,
     "Matières premières, énergie et sous-traitance sont consommées au cours du cycle de production."),
 QC("Comment calcule-t-on la valeur ajoutée ?", "Production plus consommations intermédiaires~Production moins consommations intermédiaires~Salaires plus charges~Chiffre d'affaires divisé par le nombre de salariés", 1,
     "La valeur ajoutée est la production diminuée des consommations intermédiaires."),
 QC("Quel est un exemple d'activité de soutien ?", "La fabrication du produit~La gestion des ressources humaines~La livraison au client~La publicité", 1,
     "Les fonctions de soutien accompagnent les activités principales sans produire directement."),
 QC("Qu'appelle-t-on goulot d'étranglement ?", "Un poste très rentable~Une étape qui limite le flux de production~Un client fidèle~Une externalisation réussie", 1,
     "C'est l'étape la plus lente qui bloque le débit de l'ensemble du processus."),
 QC("Quel risque principal présente l'externalisation ?", "Une productivité toujours meilleure~Une dépendance au prestataire~Une baisse des coûts garantie~La disparition des contrats", 1,
     "La dépendance, la qualité et la confidentialité doivent être encadrées."),
 QC("Que mesure la productivité ?", "Le nombre de salariés~Le rapport entre production et moyens utilisés~Le chiffre d'affaires seul~La durée du contrat", 1,
     "On compare les résultats obtenus aux ressources mobilisées."),
 QC("Que décrit la chaîne de valeur ?", "L'organigramme de l'entreprise~L'enchaînement des activités qui créent de la valeur~Le bilan comptable~Le plan de trésorerie", 1,
     "Elle suit la création de valeur de la conception jusqu'au service après-vente."),
 QT("Expliquer la différence entre valeur ajoutée et chiffre d'affaires.",
     "Le chiffre d'affaires mesure la valeur totale des ventes de l'entreprise sur une période, avant déduction des achats et charges externes. La valeur ajoutée retranche de la production les consommations intermédiaires : elle mesure ce que l'entreprise a réellement créé par son propre travail et son capital. Par exemple, une entreprise qui achète des composants pour 60 000 € et les revend 100 000 € dégage 40 000 € de valeur ajoutée, qui servira à rémunérer les salariés, les capitaux et l'État. La valeur ajoutée est un indicateur plus pertinent que le chiffre d'affaires pour apprécier la contribution réelle d'une activité.",
     "On oppose valeur des ventes et richesse effectivement créée, avec un exemple chiffré."),
 QT("Comment une entreprise peut-elle améliorer sa productivité sans dégrader la qualité ?",
     "Elle peut d'abord cartographier ses processus pour repérer les tâches sans valeur ajoutée, les doubles saisies et les attentes inutiles. Elle peut ensuite simplifier les circuits, former les salariés, mieux organiser les postes et investir dans des outils adaptés, notamment numériques. La maintenance préventive réduit les arrêts de production et la standardisation des tâches répétitives limite les erreurs. Il faut enfin mesurer les effets avec des indicateurs : délai de traitement, taux de défaut, quantité produite par heure. Une productivité durable associe gains de temps, qualité maintenue et implication des équipes, plutôt qu'une simple accélération imposee aux salariés.",
     "On attend cartographie, suppression des gaspillages, formation, outils et indicateurs de qualité.")],
C("La production transforme des facteurs en valeur ; la chaîne de valeur rend visible chaque étape de cette création.",
  "Valeur ajoutée = production − consommations intermédiaires",
  "Productivité = production / moyens utilisés · chaîne de valeur : conception à service",
  "Production~Transformation des facteurs~Valeur ajoutee~Richesse creee~Consommation intermediaire~Bien consomme~Productivite~Rapport et rendement~Processus~Entree et sortie",
  "Cartographier les processus|Relever les flux physiques et d'information|Mesurer la valeur ajoutée|Repérer les goulots|Améliorer et contrôler",
  "Confondre chiffre d'affaires et valeur ajoutée|Ignorer les consommations intermédiaires|Externaliser sans contrat|Chercher le volume au détriment de la qualité",
  "Achat 60 000 et vente 100 000~Valeur ajoutee 40 000~Goulot~Etape la plus lente~Sous-traitance~Risque de dependance~Maintenance~Arrets reduits",
  "Valeur ajoutee~Richesse creee~Chiffre d'affaires~Valeur des ventes",
  "Activite principale~Cree directement de la valeur~Activite de soutien~Rend possible la production"))

# ============================================================ EG5
add("EG5", "Les circuits de distribution et la logistique", "Économie et gestion", ["1re pro"],
S("La distribution assure le cheminement du producteur vers le consommateur : elle met le produit à disposition au bon endroit et au bon moment."
  "|Un circuit direct ne comporte aucun intermédiaire : le producteur vend lui-même, en boutique ou sur Internet."
  "|Un circuit indirect fait intervenir des intermédiaires comme le grossiste, le détaillant, le distributeur ou la plateforme."
  "|Le grossiste achète en grande quantité et revend en plus petites quantités aux détaillants, assurant un rôle de regroupement et de fractionnement."
  "|Le détaillant vend au consommateur final en petite quantité et assure l'accueil, le conseil et le service."
  "|La distribution sélective choisit des points de vente selon des critères, tandis que la distribution intensive cherche la couverture maximale."
  "|La distribution exclusive réserve un territoire ou une clientèle à un seul distributeur, sous conditions juridiques strictes."
  "|La logistique organise les flux de marchandises, d'information et financiers entre les acteurs de la chaîne."
  "|Les principales fonctions logistiques sont l'approvisionnement, le stockage, la préparation de commandes, le transport et la livraison."
  "|Le stock de sécurité protège contre les variations de la demande et les retards d'approvisionnement imprévus."
  "|Le point de commande correspond au stock de sécurité augmenté de la consommation moyenne multipliée par le délai de livraison."
  "|Le coût logistique doit être arbitré avec le niveau de service : réduire les stocks trop fortement augmente le risque de rupture."),
[QC("Qu'appelle-t-on circuit direct ?", "Un circuit avec un grossiste~Un circuit sans intermédiaire~Un circuit international~Un circuit avec plateforme", 1,
     "Le producteur vend directement au consommateur final."),
 QC("Quel est le rôle principal d'un grossiste ?", "Vendre au consommateur final~Acheter en gros et revendre en quantités plus petites~Fabriquer le produit~Fixer les prix publics", 1,
     "Le grossiste assure regroupement, fractionnement et souvent stockage."),
 QC("Que vise la distribution intensive ?", "Un nombre réduit de points de vente~Une couverture maximale du marché~Un seul distributeur par région~La vente uniquement en ligne", 1,
     "La distribution intensive multiplie les points de vente pour être présente partout."),
 QC("Quelle fonction logistique prépare les commandes clients ?", "L'approvisionnement~La préparation de commandes~La comptabilité~Le recrutement", 1,
     "La préparation de commandes comprend picking, contrôle et emballage."),
 QC("À quoi sert un stock de sécurité ?", "À afficher plus de produits~À couvrir les aléas de demande et de livraison~À supprimer les inventaires~À réduire les prix", 1,
     "Il constitue une protection contre l'incertitude."),
 QC("Comment calcule-t-on le point de commande ?", "Stock de sécurité moins consommation~Stock de sécurité plus consommation journalière × délai~Consommation divisée par délai~Stock maximal moins stock minimal", 1,
     "On ajoute au stock de sécurité la consommation prévue pendant le délai d'approvisionnement."),
 QC("Quel est le risque d'une réduction trop forte des stocks ?", "Une baisse des coûts garantie~Une rupture de stock~Une hausse du service~Une disparition des transporteurs", 1,
     "Moins de stocks signifie moins de marge de sécurité face à la demande."),
 QT("Une entreprise consomme 20 unités par jour avec un délai d'approvisionnement de 6 jours et un stock de sécurité de 40 unités. Calculer son point de commande et l'interpréter.",
     "Le point de commande vaut stock de sécurité + consommation journalière × délai, soit 40 + 20 × 6 = 40 + 120 = 160 unités. Cela signifie que l'entreprise doit passer commande dès que son stock disponible descend à 160 unités : les 120 unités consommées pendant les six jours d'attente seront alors couvertes, et les 40 unités de sécurité resteront disponibles à la réception. Si le fournisseur livre en retard ou si la demande augmente, le stock de sécurité absorbera tout ou partie de l'écart.",
     "On calcule 40 + 20 × 6 = 160 et on explique le rôle des deux composantes."),
 QT("Expliquer le compromis entre coût logistique et qualité de service.",
     "Un niveau de service élevé suppose des stocks importants, des livraisons rapides et souvent plusieurs entrepôts : cela augmente les coûts de stockage, d'assurance et de transport. À l'inverse, réduire les stocks et regrouper les livraisons diminue ces coûts mais accroît le risque de rupture et allonge les délais, ce qui peut décevoir le client. La démarche consiste à identifier les niveaux de service attendus par segment de clientèle, à chiffrer le coût de chaque option et à comparer ce coût au risque de perte de vente. Les indicateurs comme le taux de service, le délai de livraison et le taux de rotation des stocks permettent de piloter cet arbitrage dans la durée.",
     "On décrit l'arbitrage coût/service, puis les indicateurs de pilotage et la segmentation client.")],
C("La distribution rapproche l'offre du client ; la logistique pilote les flux et arbitre entre coût et niveau de service.",
  "Point de commande = stock de sécurité + consommation × délai",
  "Circuit direct : sans intermédiaire · circuit indirect : avec grossiste et détaillant",
  "Circuit direct~Producteur vers client~Circuit indirect~Intermediaires~Grossiste~Achats en gros~Logistique~Flux et stocks~Point de commande~Seuil de relance",
  "Choisir le circuit de distribution|Identifier les intermédiaires|Cartographier les flux logistiques|Calculer les seuils de stock|Piloter coût et service",
  "Confondre grossiste et détaillant|Oublier le stock de sécurité|Négliger le délai de livraison|Réduire les stocks sans mesurer le risque",
  "20 unités/jour et 6 jours~Consommation 120~Stock de securite 40~Point de commande 160~Taux de service~Indicateur cle~Rupture~Risque client",
  "Circuit direct~Sans intermediaire~Circuit indirect~Avec grossiste et detaillant",
  "Distribution intensive~Presence maximale~Distribution selective~Points de vente choisis"))

# ============================================================ EG6
add("EG6", "Le marketing mix et le plan de marketing", "Économie et gestion", ["1re pro", "Terminale pro"],
S("Le marketing consiste à identifier les besoins des clients et à mobiliser les moyens de l'entreprise pour y répondre de façon rentable."
  "|Le marketing stratégique analyse le marché, segmente la clientèle, choisit une cible et définit un positionnement."
  "|Le marketing opérationnel met en œuvre les décisions produits, prix, distribution et communication."
  "|Le marketing mix reproduit les quatre P : Product, Price, Place, Promotion, que l'on traduit par produit, prix, distribution et communication."
  "|Le produit comprend la qualité, la marque, le design, l'emballage et les services associés comme la garantie ou le service après-vente."
  "|Le prix doit couvrir les coûts, tenir compte de la valeur perçue par le client et rester cohérent avec le positionnement."
  "|La distribution choisit les canaux physiques ou numériques et vise la disponibilité du produit au bon endroit."
  "|La communication informe, persuade et rappelle l'existence de l'offre à travers la publicité, la promotion des ventes et les relations publiques."
  "|La segmentation peut reposer sur des critères géographiques, démographiques, psychographiques ou comportementaux."
  "|Le plan de marketing organise les objectifs, les actions, le budget, le calendrier et les indicateurs de contrôle."
  "|Les indicateurs de performance portent sur les ventes, les parts de marché, la notoriété, la satisfaction et la rentabilité."
  "|Le suivi du plan suppose de comparer les résultats aux objectifs et d'ajuster les actions si les écarts sont significatifs."),
[QC("Que désignent les quatre P du marketing mix ?", "Produit, Prix, Place, Promotion~Personnes, Prix, Plan, Publicité~Production, Prix, Partage, Promotion~Produit, Personnel, Place, Publicité", 0,
     "Les 4 P sont Product, Price, Place et Promotion."),
 QC("Quel critère de segmentation repose sur le mode de consommation ?", "Géographique~Démographique~Comportemental~Psychographique", 2,
     "Le critère comportemental s'appuie sur l'usage, la fréquence ou la fidélité."),
 QC("Quel est un élément de la politique de produit ?", "Le taux de TVA~La marque et l'emballage~Le délai de paiement~Le plan de trésorerie", 1,
     "La marque, le design et le conditionnement font partie de l'offre produit."),
 QC("Que doit couvrir le prix de vente ?", "Uniquement les matières premières~Les coûts tout en tenant compte de la valeur perçue~Uniquement la publicité~Le salaire du dirigeant", 1,
     "Le prix intègre les coûts et la valeur perçue, dans le respect du positionnement."),
 QC("Quel outil relève de la communication ?", "Le choix d'un grossiste~La publicité et la promotion des ventes~Le calcul de l'amortissement~Le plan comptable", 1,
     "La communication informe et persuade le client ; la distribution rend le produit disponible."),
 QC("Que contient un plan de marketing ?", "Seulement le budget publicitaire~Objectifs, actions, budget, calendrier et indicateurs~Le bilan uniquement~Les seules prévisions de ventes", 1,
     "C'est un document de pilotage complet et daté."),
 QC("Quel indicateur mesure la place de l'entreprise sur son marché ?", "La notoriété~La part de marché~Le taux de TVA~Le coût de production", 1,
     "La part de marché rapporte les ventes de l'entreprise aux ventes totales du marché."),
 QT("Expliquer la différence entre marketing stratégique et marketing opérationnel.",
     "Le marketing stratégique porte sur les choix de long terme : analyser le marché et la concurrence, segmenter la clientèle, choisir les cibles et construire un positionnement différenciant. Il mobilise des études et des prévisions. Le marketing opérationnel traduit ces choix en actions concrètes à court terme : fixer le prix, choisir les canaux de distribution, construire la campagne de communication et adapter le produit. Il dispose d'un budget et d'un calendrier, et il est évalué par des indicateurs. Les deux niveaux sont liés : une décision opérationnelle incohérente avec le positionnement choisi affaiblit la stratégie.",
     "On oppose les choix de long terme aux actions de court terme, puis on montre leur cohérence nécessaire."),
 QT("Une entreprise lance une nouvelle gamme de produits écologiques. Comment construire son plan de marketing ?",
     "On fixe d'abord des objectifs précis et mesurables, par exemple atteindre une part de marché de 5 % en un an. On identifie la cible, ici des clients sensibles à l'environnement, et on précise le positionnement sur la qualité et la traçabilité. On décline ensuite le mix : un produit certifié et bien identifiable, un prix reflétant la valeur perçue, une distribution dans des points de vente adaptés et une communication appuyée sur la preuve et les réseaux sociaux. On chiffre le budget, on établit un calendrier de lancement et on définit des indicateurs : ventes, notoriété, satisfaction, retours produits. Un suivi trimestriel permet de corriger les actions si les résultats s'écartent des objectifs.",
     "On attend objectifs, cible, positionnement, déclinaison des 4 P, budget, calendrier et indicateurs.")],
C("Le marketing relie une cible, un positionnement et quatre leviers opérationnels pilotés par un plan.",
  "4 P : Product, Price, Place, Promotion",
  "Stratégie : segmentation, cible, positionnement · Opérationnel : budget, actions, indicateurs",
  "Marketing~Besoins et rentabilite~Segmentation~Groupes homogenes~Cible~Segment retenu~Positionnement~Place souhaitee~Mix~Quatre leviers",
  "Analyser le marche|Segmenter et choisir la cible|Definir le positionnement|Decliner les 4 P|suivre les indicateurs",
  "Confondre segmentation et positionnement|Négliger le prix par rapport au produit|Lancer sans budget défini|Oublier le contrôle des résultats",
  "4 P~Produit, prix, distribution, communication~Part de marche~Ventes sur marche total~Notoriete~Connaissance de la marque~Budget~Ressources allouees~Objectif 5 %~Cible chiffree",
  "Strategique~Choix de long terme~Operationnel~Actions de court terme",
  "Segmenter~Decouper le marche~Cibler~Choisir un segment"))

# ============================================================ EG7
add("EG7", "La communication commerciale et la fidélisation client", "Économie et gestion", ["Terminale pro"],
S("La communication commerciale transmet un message à une cible dans le but d'informer, de persuader ou de déclencher une action d'achat."
  "|Le plan de communication définit les objectifs, les messages, les cibles, les canaux, le budget et les indicateurs d'efficacité."
  "|Les objectifs peuvent être de notoriété, de considération ou de conversion, et doivent être mesurables."
  "|La publicité est une communication payante et identifiée, diffusée dans les médias de masse ou sur Internet."
  "|La promotion des ventes propose un avantage temporaire, comme une remise, un échantillon ou un concours, pour stimuler l'achat."
  "|Les relations publiques visent à construire une image durable auprès des publics de l'entreprise, sans achat d'espace direct."
  "|Le marketing direct adresse un message personnalisé à une personne identifiée, par courrier, e-mail ou téléphone."
  "|Les réseaux sociaux permettent une communication interactive et favorisent le bouche-à-oreille numérique."
  "|Le message doit être clair, crédible et adapté au canal : un format court ne supporte pas un argumentaire complexe."
  "|La fidélisation vise à conserver les clients existants, dont le coût d'acquisition est généralement supérieur à celui de la rétention."
  "|Les outils de fidélisation comprennent les cartes de fidélité, les programmes de points, les offres personnalisées et le service après-vente."
  "|La mesure de l'efficacité repose sur des indicateurs comme le taux d'ouverture, le taux de clic, le coût par contact et le taux de réachat."),
[QC("Quel est un objectif de notoriété ?", "Vendre immédiatement~Faire connaître la marque~Réduire les coûts~Fidéliser un client", 1,
     "La notoriété mesure le degré de connaissance de la marque par le public."),
 QC("Quelle communication est payante et identifiée ?", "Les relations publiques~La publicité~Le bouche-à-oreille~Le service après-vente", 1,
     "La publicité est un message payant dont l'émetteur est clairement identifié."),
 QC("Quel outil relève de la promotion des ventes ?", "Une remise temporaire~Un communiqué de presse~Un colloque~Un rapport annuel", 0,
     "La promotion des ventes offre un avantage court pour déclencher l'achat."),
 QC("Quel canal permet une interaction directe avec la communauté ?", "L'affichage~Les réseaux sociaux~La presse écrite~La télévision", 1,
     "Les réseaux sociaux rendent possible un dialogue et la diffusion de contenus par les utilisateurs."),
 QC("Pourquoi fidéliser un client ?", "Parce que c'est toujours gratuit~Parce que l'acquisition d'un nouveau client coûte généralement plus cher~Parce que le client ne peut pas partir~Parce que cela supprime la publicité", 1,
     "Rétention et acquisition ont des coûts très différents."),
 QC("Quel est un indicateur d'une campagne d'e-mailing ?", "Le taux d'ouverture~Le nombre de salariés~Le bilan~Le plan comptable", 0,
     "Le taux d'ouverture, le taux de clic et les conversions mesurent l'efficacité."),
 QC("Quel principe s'applique à un message sur un format court ?", "Développer tous les arguments~Être clair et aller à l'essentiel~Supprimer la signature~Utiliser un jargon technique", 1,
     "Le message doit être adapté au canal et compréhensible immédiatement."),
 QT("Expliquer la différence entre publicité, promotion des ventes et relations publiques.",
     "La publicité est une communication massive, payante et identifiée, qui vise à faire connaître ou préférer une marque sur la durée. La promotion des ventes propose un avantage limité dans le temps, comme une réduction ou un échantillon, pour accélérer la décision d'achat. Les relations publiques cherchent à construire une image et une confiance durables à travers des actions non payantes directement, comme les communiqués de presse, les événements ou le mécénat. Ces trois outils sont complémentaires : la publicité installe la notoriété, la promotion déclenche l'acte d'achat et les relations publiques entretiennent la réputation.",
     "On distingue objectif, durée et mode de diffusion des trois outils."),
 QT("Comment mesurer l'efficacité d'une action de fidélisation et l'adapter ?",
     "On définit d'abord un indicateur de rétention, par exemple le taux de clients réacheteurs sur une période, et on le compare à la situation avant l'action. On suit aussi la fréquence d'achat, le panier moyen, l'utilisation des cartes de fidélité et le taux de désabonnement. Les données clients permettent de segmenter les comportements et d'identifier les clients à risque de départ. On teste ensuite des offres personnalisées sur un échantillon, on mesure leur effet en comparant avec un groupe témoin, puis on généralise les actions efficaces. Enfin, on vérifie la rentabilité : une fidélisation coûteuse n'est utile que si elle augmente la valeur vie client plus que son coût.",
     "On attend indicateurs, comparaison avant/après, test,segmentation et contrôle de rentabilité.")],
C("La communication commerciale construit la notoriété, déclenche la vente et entretient la relation client.",
  "Objectifs : notoriété → considération → conversion",
  "Publicité payante · promotion temporaire · relations publiques · marketing direct",
  "Communication~Emetteur, message, canal~Publicite~Payante et identifiee~Promotion~Avantage temporaire~Fidelisation~Retenir le client~Indicateur~Taux de clic et de reachat",
  "Fixer un objectif mesurable|Choisir la cible et le message|Sélectionner les canaux|Budgéter et diffuser|Mesurer et ajuster",
  "Confondre publicité et relations publiques|Multiplier les messages sans objectif|Négliger la mesure|Offrir des remises en permanence",
  "Taux d'ouverture~Message recu~Taux de clic~Interet suscite~Cout par contact~Efficacite budgetaire~Taux de reachat~Fidelite mesuree",
  "Publicite~Payante et de masse~Relations publiques~Image et confiance",
  "Acquisition~Nouveau client~Fidelisation~Client existant"))

# ============================================================ CO1
add("CO1", "Le bilan et l'équilibre comptable", "Comptabilité", ["1re pro"],
S("Le bilan est un document de synthèse qui décrit le patrimoine de l'entreprise à une date donnée, en France généralement le 31 décembre."
  "|Il se présente en deux parties : l'actif, qui montre ce que l'entreprise possède, et le passif, qui montre comment ces biens sont financés."
  "|L'actif immobilisé regroupe les biens durables destinés à être utilisés pendant plusieurs exercices, comme les machines ou les bureaux."
  "|L'actif circulant comprend les stocks, les créances clients, les disponibilités et les comptes de régularisation."
  "|Au passif, les capitaux propres représentent l'apport des associés et les résultats accumulés depuis la création."
  "|Les dettes sont classées selon leur échéance : dettes financières, fournisseurs, fiscales et sociales notamment."
  "|L'équation comptable fondamentale s'écrit : Actif = Capitaux propres + Dettes, c'est-à-dire Actif = Passif."
  "|Le bilan après inventaire intègre les amortissements, les provisions et le résultat de l'exercice."
  "|Le total du bilan donne une indication de la taille de l'entreprise, mais il ne dit rien à lui seul de sa rentabilité."
  "|Le fonds de roulement net global se calcule par capitaux propres plus dettes durables moins actif immobilisé."
  "|Un fonds de roulement positif signifie qu'une partie des immobilisations est financée par des ressources durables : la situation est plus sûre."
  "|Le besoin en fonds de roulement traduit le décalage entre les décaissements et les encaissements liés au cycle d'exploitation."),
[QC("Que montre l'actif du bilan ?", "Les seules dettes~Ce que l'entreprise possède~Le résultat de l'exercice~Les apports des associés", 1,
     "L'actif décrit les biens et les droits de l'entreprise à la date du bilan."),
 QC("Quelle est l'équation fondamentale du bilan ?", "Actif = Dettes~Actif = Capitaux propres + Dettes~Actif = Charges + Produits~Passif = Résultat", 1,
     "L'actif est toujours financé par des capitaux propres et des dettes."),
 QC("Où classe-t-on une créance client ?", "À l'actif immobilisé~À l'actif circulant~Au passif~Hors bilan", 1,
     "Une créance est un droit d'encaisser, donc un élément de l'actif circulant."),
 QC("Que représente le poste « capitaux propres » ?", "Les dettes à court terme~Les apports et les résultats accumulés~Les stocks~Les charges de l'exercice", 1,
     "Les capitaux propres appartiennent économiquement aux associés."),
 QC("Quand le fonds de roulement est-il négatif ?", "Quand les ressources durables financent tout l'actif immobilisé~Quand une partie de l'actif immobilisé est financée par des dettes courantes~Quand l'entreprise n'a pas de dettes~Quand le résultat est nul", 1,
     "Un FRNG négatif révèle une situation de tension financière."),
 QC("Que mesure le besoin en fonds de roulement ?", "La durée d'amortissement~Le décalage entre décaissements et encaissements d'exploitation~Le montant des immobilisations~Le résultat fiscal", 1,
     "Le BFR traduit le financement nécessaire au cycle d'exploitation."),
 QC("Que donne le total du bilan ?", "La rentabilité~Une indication de taille du patrimoine~Le chiffre d'affaires~Le résultat net", 1,
     "Le total bilan mesure l'importance du patrimoine, pas la performance."),
 QT("Une entreprise a 400 000 € d'actif, dont 250 000 € d'immobilisations, 120 000 € de capitaux propres et 80 000 € de dettes durables. Calculer son fonds de roulement net global et l'interpréter.",
     "Les ressources durables valent capitaux propres plus dettes durables, soit 120 000 + 80 000 = 200 000 €. Le FRNG vaut ressources durables moins actif immobilisé, soit 200 000 − 250 000 = −50 000 €. Il est négatif : l'entreprise finance 50 000 € de ses immobilisations par des dettes à court terme. Cette situation est risquée, car des refinancements fréquents seront nécessaires ; elle doit être comparée au besoin en fonds de roulement et à la trésorerie disponible pour apprécier la gravité.",
     "On calcule les ressources durables (200 000), puis 200 000 − 250 000 = −50 000, et on conclut à un risque."),
 QT("Expliquer pourquoi une entreprise peut être bénéficiaire et avoir des difficultés de trésorerie.",
     "Le résultat est calculé en comptabilité d'engagement : une vente est comptabilisée lorsqu'elle est réalisée, même si le client paie plus tard. La trésorerie, elle, enregistre les mouvements d'argent réels. Si les ventes augmentent fortement, les créances clients grossissent avant d'être encaissées, tandis que les fournisseurs, les salaires et les charges doivent être payés rapidement. Le besoin en fonds de roulement augmente alors et mobilise de la trésorerie. Une entreprise peut donc afficher un bénéfice comptable tout en manquant de liquidités, d'où l'importance du suivi du plan de trésorerie et du délai de paiement des clients.",
     "On oppose comptabilité d'engagement et mouvements d'espèces, puis on relie au BFR.")],
C("Le bilan photographie le patrimoine : l'actif décrit les emplois, le passif décrit les ressources qui les financent.",
  "Actif = Capitaux propres + Dettes",
  "FRNG = capitaux propres + dettes durables − actif immobilisé",
  "Actif~Biens et droits~Immobilise~Biens durables~Circulant~Stocks et creances~Passif~Capitaux et dettes~Equilibre~Actif egal passif",
  "Repérer la date du bilan|Classer les postes à l'actif|Classer les postes au passif|Vérifier l'équilibre|Calculer le FRNG et le BFR",
  "Confondre actif et passif|Oublier que le résultat est au passif|Croire qu'un bilan équilibré est rentable|Négliger l'échéance des dettes",
  "Actif 400 000~Immobilisations 250 000~Capitaux 120 000~Dettes durables 80 000~FRNG~-50 000 et tension",
  "Actif~Emplois du patrimoine~Passif~Origine des financements",
  "FRNG~Ressources durables moins immobilises~BFR~Cycle d'exploitation"))

# ============================================================ CO2
add("CO2", "Le compte de résultat et la formation du résultat", "Comptabilité", ["1re pro"],
S("Le compte de résultat récapitule les charges et les produits d'une entreprise sur un exercice, généralement l'année civile."
  "|Une charge est une consommation de biens ou de services, ou un décaissement, qui diminue le résultat."
  "|Un produit est une augmentation des ressources, notamment les ventes, qui accroît le résultat."
  "|Le résultat net est la différence entre les produits et les charges de l'exercice : il peut être bénéficiaire ou déficitaire."
  "|Les charges d'exploitation comprennent les achats, les salaires, les amortissements, les impôts et taxes et les autres charges."
  "|Les produits d'exploitation comprennent le chiffre d'affaires et les autres produits courants de l'activité."
  "|Le résultat d'exploitation mesure la performance de l'activité normale, avant résultats financiers et exceptionnels."
  "|Le résultat financier regroupe les produits et charges financiers, comme les intérêts perçus ou payés."
  "|Le résultat exceptionnel concerne des opérations inhabituelles, comme la vente d'un terrain ou une pénalité exceptionnelle."
  "|L'impôt sur les sociétés et la participation des salariés sont déduits pour obtenir le résultat net de l'exercice."
  "|Le taux de marge commerciale rapporte la marge commerciale au chiffre d'affaires hors taxes."
  "|Le compte de résultat se lit avec le bilan : le résultat net est repris en capitaux propres dans le bilan après inventaire."),
[QC("Quel est le rôle du compte de résultat ?", "Photographier le patrimoine~Récapituler charges et produits sur l'exercice~Lister les salariés~Prévoir la trésorerie", 1,
     "Il mesure la performance sur une période, à la différence du bilan qui est un état à une date."),
 QC("Quel effet a une charge sur le résultat ?", "Elle l'augmente~Elle le diminue~Elle le rend nul~Elle n'a aucun effet", 1,
     "Les charges diminuent le résultat, les produits l'augmentent."),
 QC("Quel poste fait partie des produits d'exploitation ?", "Les salaires~Le chiffre d'affaires~Les intérêts payés~L'impôt sur les sociétés", 1,
     "Le chiffre d'affaires est le principal produit d'exploitation."),
 QC("Que mesure le résultat d'exploitation ?", "La performance de l'activité normale~Le résultat après impôt~Les seules opérations financières~Le montant des immobilisations", 0,
     "Il isole la performance courante avant résultats financier et exceptionnel."),
 QC("Quel élément relève du résultat exceptionnel ?", "La vente de marchandises~La vente d'un terrain hors activité normale~Les achats de matières~Les salaires", 1,
     "Les opérations inhabituelles et non courantes sont exceptionnelles."),
 QC("Comment calcule-t-on le résultat net ?", "Produits moins charges, puis impôt et participation déduits~Charges moins produits~Chiffre d'affaires divisé par charges~Actif moins passif", 0,
     "On part des produits et charges, puis on tient compte de l'impôt et de la participation."),
 QC("Que rapporte le taux de marge commerciale ?", "La marge au chiffre d'affaires HT~Le résultat au bilan~Les charges aux produits~La trésorerie au chiffre d'affaires", 0,
     "Taux de marge commerciale = marge commerciale / chiffre d'affaires HT."),
 QT("Une entreprise a un chiffre d'affaires HT de 500 000 €, des achats de marchandises de 300 000 €, des variations de stock de −20 000 € et des salaires de 90 000 €. Calculer la marge commerciale et dégager un résultat partiel.",
     "La marge commerciale vaut chiffre d'affaires HT + variation de stock − achats de marchandises, soit 500 000 − 20 000 − 300 000 = 180 000 €. Le taux de marge commerciale est 180 000 / 500 000 = 0,36, soit 36 %. Après déduction des salaires de 90 000 €, la valeur ajoutée disponible avant les autres charges s'élève à 180 000 − 90 000 = 90 000 €. Il faudra encore retrancher les autres charges d'exploitation, amortissements, impôts et taxes, pour obtenir le résultat d'exploitation. Le résultat définitif dépend donc de l'ensemble des charges, pas de la seule marge commerciale.",
     "On calcule la marge (180 000 €), son taux (36 %) puis on déduit les salaires en rappelant les charges restantes."),
 QT("Distinguer résultat d'exploitation, résultat financier et résultat net, et expliquer leur intérêt.",
     "Le résultat d'exploitation provient de l'activité courante : ventes, achats, salaires, amortissements. Il montre si le métier de l'entreprise est rentable. Le résultat financier regroupe les produits et charges liés aux financements et aux placements, comme les intérêts d'emprunt ; il traduit le coût de la structure financière. Le résultat exceptionnel enregistre les événements inhabituels. Le résultat net, après impôt et participation, est le bénéfice ou la perte final qui sera repris en capitaux propres. Cette décomposition permet de séparer la performance durable du métier des effets ponctuels ou financiers, et donc de mieux porter un jugement sur la santé de l'entreprise.",
     "On définit chaque niveau de résultat et on explique l'intérêt de cette lecture en couches.")],
C("Le compte de résultat mesure la performance d'une période en comparant produits et charges, niveau par niveau.",
  "Résultat = Produits − Charges · marge commerciale = CA HT + variation de stock − achats",
  "Exploitation → financier → exceptionnel → impôt → résultat net",
  "Charge~Consommation qui diminue le resultat~Produit~Ressource qui l'augmente~Marge commerciale~CA moins achats~Resultat net~Benefice final~Exercice~Periode de reference",
  "Repérer la période|Classer charges et produits|Calculer la marge commerciale|Déduire les charges successives|Lire le résultat net et son affectation",
  "Confondre bilan et compte de résultat|Oublier la variation de stock|Mélanger résultat financier et exceptionnel|Ignorer l'impôt",
  "CA 500 000~Achats 300 000~Variation −20 000~Marge 180 000~Taux 36 %~Salaires 90 000~Solde 90 000",
  "Bilan~Etat a une date~Compte de resultat~Flux sur une periode",
  "Resultat d'exploitation~Activite courante~Resultat financier~Financements et placements"))

# ============================================================ CO3
add("CO3", "La nomenclature du plan comptable général et les classes", "Comptabilité", ["1re pro"],
S("Le plan comptable général, ou PCG, définit la nomenclature des comptes et les règles de fonctionnement applicables aux entreprises en France."
  "|Il est révisé par l'Autorité des normes comptables et coordonne les obligations comptables, fiscales et sociales."
  "|Le PCG repose sur le principe de la partie double : toute opération modifie au moins deux comptes pour un montant égal."
  "|La classe 1 regroupe les capitaux propres et les dettes durables, qui sont des ressources de l'entreprise."
  "|La classe 2 concerne les immobilisations : terrain, matériel, logiciels et autres biens durables."
  "|La classe 3 enregistre les stocks et les travaux en cours, qui font l'objet d'un suivi quantitatif et valorisé."
  "|La classe 4 rassemble les comptes de tiers : fournisseurs, clients, salariés, organismes sociaux et administration fiscale."
  "|La classe 5 est celle des comptes financiers, notamment la banque, la caisse et les valeurs mobilières."
  "|La classe 6 enregistre les charges, qui diminuent le résultat, et la classe 7 les produits, qui l'augmentent."
  "|La classe 8 est réservée aux comptes spéciaux, comme les résultats ou les écarts de conversion."
  "|Le numéro de compte indique sa classe par son premier chiffre, puis sa subdivision par les chiffres suivants."
  "|Le respect de la nomenclature permet d'échanger des informations comparables entre entreprises et avec l'administration."),
[QC("Quel est le rôle du plan comptable général ?", "Fixer les salaires~Définir la nomenclature des comptes et les règles comptables~Remplacer le bilan~Gérer les paies", 1,
     "Le PCG est le référentiel des comptes et de leur fonctionnement."),
 QC("Dans quelle classe se trouvent les immobilisations ?", "Classe 1~Classe 2~Classe 3~Classe 4", 1,
     "La classe 2 enregistre les biens durables destinés à l'activité."),
 QC("Quelle classe regroupe les charges ?", "Classe 4~Classe 5~Classe 6~Classe 7", 2,
     "La classe 6 contient les charges ; la classe 7 contient les produits."),
 QC("Quel principe impose un débit et un crédit de montant égal ?", "La partie double~La comptabilité de caisse~Le principe de prudence~L'annualité", 0,
     "En partie double, chaque opération équilibre débits et crédits."),
 QC("Où enregistre-t-on une créance client ?", "Classe 2~Classe 3~Classe 4~Classe 6", 2,
     "Les clients sont des tiers, donc des comptes de la classe 4."),
 QC("Quelle classe concerne la banque et la caisse ?", "Classe 1~Classe 4~Classe 5~Classe 8", 2,
     "La classe 5 regroupe les comptes financiers et les disponibilités."),
 QC("Quel est l'intérêt d'une nomenclature commune ?", "Rendre les comptes comparables~Augmenter le chiffre d'affaires~Supprimer les impôts~Réduire le nombre de salariés", 0,
     "Un référentiel commun rend les comptes lisibles et comparables."),
 QT("Pourquoi la partie double garantit-elle l'équilibre de la balance ?",
     "Chaque opération est enregistrée au moins deux fois : une fois au débit d'un compte, une fois au crédit d'un autre, pour le même montant. La somme des débits est donc toujours égale à la somme des crédits, ce que vérifie la balance. Cet équilibre arithmétique ne prouve pas l'absence d'erreur : une écriture peut être passée au mauvais compte ou omise des deux côtés et la balance restera équilibrée. La partie double apporte une première sécurité de calcul et une traçabilité des flux, mais elle doit être complétée par des contrôles sur la réalité et la justification des opérations.",
     "On explique l'égalité débits/crédits, puis les limites du contrôle. "),
 QT("Une entreprise achète du matériel de bureau 3 000 € TTC, TVA 20 % incluse, payé par virement bancaire. Indiquer les comptes concernés.",
     "Le montant hors taxes vaut 3 000 / 1,20 = 2 500 € et la TVA déductible 500 €. L'écriture comprend un débit au compte 2154 « Matériel bureau et informatique » pour 2 500 €, un débit au compte 445662 « TVA déductible sur acquisitions » pour 500 €, et un crédit au compte 512 « Banque » pour 3 000 €. Les débits totalisent 3 000 € et le crédit 3 000 € : la partie double est respectée. On retrouve ici la classe 2 pour l'immobilisation, la classe 4 pour la TVA due au Trésor et la classe 5 pour le moyen de paiement.",
     "On calcule HT et TVA, puis on donne les trois comptes et on vérifie l'équilibre.")],
C("Le plan comptable général organise les comptes en classes : la première lettre ou le premier chiffre indique la nature de l'élément.",
  "Partie double : débit = crédit pour chaque opération",
  "Classe 1 ressources durables · 2 immobilisations · 3 stocks · 4 tiers · 5 finance · 6 charges · 7 produits",
  "Classe 1~Capitaux et dettes~Classe 2~Immobilisations~Classe 3~Stocks~Classe 4~Tiers~Classe 5~Banque et caisse~Classe 6~Charges",
  "Identifier la nature de l'opération|Choisir la classe adaptée|Préciser le compte|Appliquer le débit et le crédit|Vérifier l'équilibre de l'écriture",
  "Confondre classe 6 et classe 7|Oublier la TVA dans un achat|Créditer un compte au lieu de le débiter|Négliger le détail du numéro de compte",
  "Achat 3 000 TTC~HT 2 500 et TVA 500~Compte 2154~Materiel de bureau~Compte 445662~TVA deductible~Compte 512~Banque",
  "Classe 6~Charges~Classe 7~Produits",
  "Compte 512~Banque~Compte 411~Client~Compte 401~Fournisseur"))

# ============================================================ CO4
add("CO4", "La TVA, la facturation et les obligations fiscales", "Comptabilité", ["1re pro", "Terminale pro"],
S("La taxe sur la valeur ajoutée, ou TVA, est un impôt indirect perçu à chaque stade de la production et de la distribution."
  "|Le taux normal en France métropolitaine est de 20 % ; des taux réduits de 10 % et 5,5 % s'appliquent à certains biens et services."
  "|La TVA est calculée sur le prix hors taxes : montant TTC = montant HT × (1 + taux)."
  "|Un assujetti est une entreprise soumise à la TVA ; elle facture la TVA à ses clients et la reverse à l'administration."
  "|La TVA collectée correspond à la taxe facturée aux clients ; la TVA déductible est celle payée aux fournisseurs."
  "|L'entreprise ne reverse que la différence entre TVA collectée et TVA déductible, ou obtient un crédit de TVA si celle-ci est supérieure."
  "|La facture doit mentionner l'identité des parties, la date, le numéro de facture, le détail des opérations, le total HT, le taux et le montant de TVA, et le total TTC."
  "|Une facture acquittée porte la mention « payée » avec la date et le mode de règlement."
  "|Les mentions obligatoires permettent au client d'exercer son droit à déduction et à l'administration de contrôler l'impôt."
  "|Le paiement de la TVA suit une périodicité mensuelle ou trimestrielle selon le régime de l'entreprise."
  "|La déclaration de TVA est télématique et doit être déposée dans les délais, même en l'absence d'opération."
  "|Une erreur de taux ou une mention manquante expose l'entreprise à une régularisation et à des pénalités."),
[QC("Quel est le taux normal de TVA en France métropolitaine ?", "5,5 %~10 %~20 %~33 %", 2,
     "Le taux normal est de 20 %, avec des taux réduits à 10 % et 5,5 %."),
 QC("Comment obtenir un prix TTC à partir d'un prix HT ?", "HT multiplié par (1 + taux)~HT divisé par (1 + taux)~HT moins taux~HT plus 20 €", 0,
     "TTC = HT × (1 + taux de TVA)."),
 QC("Qu'appelle-t-on TVA déductible ?", "La TVA facturée aux clients~La TVA payée aux fournisseurs~La TVA reversée à l'État~L'impôt sur les sociétés", 1,
     "La TVA supportée sur les achats est déductible de la TVA collectée."),
 QC("Quel montant l'entreprise reverse-t-elle à l'administration ?", "La TVA collectée seule~La TVA collectée moins la TVA déductible~Le chiffre d'affaires TTC~Le bénéfice net", 1,
     "Seul le solde entre TVA collectée et déductible est dû."),
 QC("Laquelle de ces mentions est obligatoire sur une facture ?", "La couleur du papier~Le numéro de facture~Le nom du commercial~L'heure d'émission", 1,
     "Le numéro de facture, les identités, les montants HT, la TVA et le TTC sont obligatoires."),
 QC("Quand l'entreprise obtient-elle un crédit de TVA ?", "Quand la TVA collectée dépasse la déductible~Quand la TVA déductible dépasse la collectée~Quand elle ne vend rien~Quand elle est exonérée", 1,
     "Un crédit apparaît lorsque les achats génèrent plus de TVA déductible que les ventes n'en collectent."),
 QC("Que se passe-t-il en cas de mention obligatoire manquante ?", "Rien~Une régularisation et des pénalités possibles~Un crédit automatique~Une exonération", 1,
     "Le non-respect des obligations fiscales expose l'entreprise à des sanctions."),
 QT("Une entreprise vend une prestation 1 200 € HT au taux de 20 % et achète pour 400 € HT de fournitures au même taux. Calculer la TVA due.",
     "La TVA collectée sur la vente vaut 1 200 × 0,20 = 240 €. La TVA déductible sur l'achat vaut 400 × 0,20 = 80 €. Le montant à reverser à l'administration est la différence : 240 − 80 = 160 €. Le client paie 1 200 + 240 = 1 440 € TTC et le fournisseur reçoit 400 + 80 = 480 € TTC. L'entreprise ne supporte pas la TVA économiquement : elle la collecte pour le compte de l'État, après déduction de celle qu'elle a elle-même payée en amont.",
     "On calcule 240 € et 80 €, puis la différence de 160 € à reverser."),
 QT("Expliquer pourquoi la facture est un document central à la fois commercial, comptable et fiscal.",
     "Sur le plan commercial, la facture matérialise l'accord entre le vendeur et le client : elle décrit la prestation, le prix et les conditions de règlement, et elle constitue une preuve en cas de litige. Sur le plan comptable, elle justifie l'enregistrement d'un produit chez le vendeur et d'une charge ou d'un immobilisé chez l'acheteur, et elle alimente les comptes de tiers. Sur le plan fiscal, elle permet de calculer la TVA collectée ou déductible et elle doit comporter les mentions légales obligatoires. Un même document sert donc à la fois à vendre, à comptabiliser et à déclarer, ce qui explique la rigueur exigée dans sa rédaction et sa conservation.",
     "On développe les trois dimensions commerciale, comptable et fiscale.")],
C("La TVA est un impôt sur la consommation collecté par les entreprises ; la facture en est le support obligatoire.",
  "TTC = HT × (1 + taux) · TVA due = collectée − déductible",
  "Taux normal 20 % · taux réduits 10 % et 5,5 %",
  "TVA collectee~Taxe facturee aux clients~TVA deductible~Taxe payee aux fournisseurs~Facture~Justificatif obligatoire~HT~Avant impot~TTC~Apres impot",
  "Repérer le taux applicable|Calculer la base HT|Determiner la TVA collectée et déductible|Vérifier les mentions de la facture|Déclarer dans les délais",
  "Appliquer le taux au montant TTC|Oublier le numéro de facture|Confondre collectée et déductible|Négliger les déclarations",
  "Vente 1 200 HT~TVA collectee 240~Achat 400 HT~TVA deductible 80~Solde a reverser~160~TTC client~1 440",
  "TVA collectee~Due par le client~TVA deductible~Payee sur les achats",
  "Prix HT~Hors taxes~Prix TTC~Toutes taxes comprises"))

# ============================================================ CO5
add("CO5", "Les écritures comptables, le journal et la balance", "Comptabilité", ["1re pro"],
S("Une écriture comptable enregistre une opération dans les comptes de l'entreprise selon le principe de la partie double."
  "|Elle comporte une date, un numéro, un libellé, le montant, et les comptes débités et crédités."
  "|Le journal est le livre dans lequel les écritures sont inscrites chronologiquement, sans omission ni interruption."
  "|Le grand livre répartit ensuite les écritures par compte, ce qui permet de suivre l'historique de chacun."
  "|La balance est la liste des soldes de tous les comptes à une date donnée ; elle vérifie l'égalité des débits et des crédits."
  "|La balance avant inventaire est établie avant les écritures d'inventaire comme les amortissements ou les provisions."
  "|Un compte est un outil de classement : son solde peut être débiteur ou créditeur selon la nature des opérations."
  "|Les comptes de charges et d'immobilisations ont généralement un solde débiteur, tandis que les capitaux et les dettes ont un solde créditeur."
  "|Une écriture de régularisation enregistre un fait comptable qui ne correspond pas à un mouvement d'argent immédiat."
  "|Les pièces justificatives, factures, reçus ou contrats, doivent être conservées et référencées pour prouver chaque écriture."
  "|Une erreur de compte peut laisser la balance équilibrée : la vérification porte aussi sur la nature des comptes utilisés."
  "|La tenue régulière des comptes est une obligation légale et permet de produire des comptes annuels fiables."),
[QC("Que contient une écriture comptable ?", "Seulement la date~Date, libellé, montant, comptes débités et crédités~Le bilan complet~Le plan de trésorerie", 1,
     "Ces éléments sont nécessaires pour identifier et justifier l'opération."),
 QC("Dans quel ordre les écritures sont-elles portées au journal ?", "Par ordre alphabétique~Par ordre chronologique~Par montant décroissant~Par numéro de compte", 1,
     "Le journal est un registre chronologique des opérations."),
 QC("Quel est le rôle du grand livre ?", "Conserver les pièces~Regrouper les écritures par compte~Remplacer la facture~Calculer la TVA", 1,
     "Le grand livre présente l'historique des mouvements de chaque compte."),
 QC("Que vérifie une balance ?", "La rentabilité~L'égalité des totaux de débits et de crédits~La trésorerie disponible~Le montant des impôts", 1,
     "Une balance équilibrée vérifie l'égalité arithmétique des débits et des crédits."),
 QC("Quel est le solde habituel d'un compte de charge ?", "Débiteur~Créditeur~Nul toujours~Négatif", 0,
     "Une charge augmente au débit, donc son solde est généralement débiteur."),
 QC("Qu'est-ce qu'une écriture de régularisation ?", "Une écriture sans pièce~Une écriture qui constate un fait sans mouvement d'argent~Une écriture de caisse~Une écriture de vente uniquement", 1,
     "Amortissements et provisions en sont des exemples."),
 QC("Pourquoi conserver les pièces justificatives ?", "Pour décorer les dossiers~Pour prouver et justifier chaque écriture~Pour réduire la TVA~Pour remplacer le grand livre", 1,
     "Elles constituent la preuve comptable et facilitent le contrôle."),
 QT("Une entreprise paie 1 500 € de salaires par virement bancaire. Décrire l'écriture et vérifier son équilibre.",
     "Les salaires sont une charge de la classe 6 : le compte 641 « Salaires et appointements » est débité de 1 500 €. Le moyen de paiement est la banque, compte 512, qui est crédité de 1 500 € puisque la trésorerie diminue. L'écriture est donc : débit 641 pour 1 500 €, crédit 512 pour 1 500 €. Les deux montants sont égaux, la partie double est respectée et la balance restera équilibrée. Pièce justificative : la fiche de paie et le relevé bancaire du virement.",
     "On donne le débit de la charge, le crédit de la banque, l'égalité des montants et la pièce justificative."),
 QT("Une balance est équilibrée. Peut-on en conclure que la comptabilité est exacte ? Justifier.",
     "Non. L'équilibre de la balance vérifie seulement que la somme des débits égale la somme des crédits, ce qui résulte mécaniquement de la partie double. Plusieurs erreurs peuvent échapper à ce contrôle : une opération entièrement omise, une écriture passée au mauvais compte mais avec le bon montant, une inversion de débit et de crédit sur deux comptes de même nature, ou encore un montant erroné reporté des deux côtés. Il faut donc compléter la balance par d'autres vérifications : rapprochement bancaire, contrôle des pièces justificatives, analyse des soldes inhabituels et rapprochement avec les états physiques des stocks.",
     "On affirme que non et on donne plusieurs types d'erreurs invisibles avec des contrôles complémentaires.")],
C("Le journal enregistre les opérations dans l'ordre, le grand livre les classe par compte, la balance vérifie leur équilibre.",
  "Écriture = date + libellé + montant + débit + crédit",
  "Débit = crédit · solde débiteur pour les charges · créditeur pour les capitaux",
  "Journal~Chronologique~Grand livre~Par compte~Balance~Soldes et equilibre~Ecriture~Debit et credit~Piece justificative~Preuve",
  "Récupérer la pièce justificative|Repérer le compte à débiter|Repérer le compte à créditer|Enregistrer au journal|Contrôler la balance",
  "Oublier le libellé|Confondre débit et crédit|Classer dans le mauvais compte|Croire qu'une balance équilibrée prouve tout",
  "Salaires 1 500~Debit compte 641~Virement~Credit compte 512~Egalite~1 500 des deux cotes~Regularisation~Sans mouvement d'argent",
  "Journal~Par date~Grand livre~Par compte",
  "Solde debiteur~Charges et immobilisations~Solde crediteur~Capitaux et dettes"))

# ============================================================ CO6
add("CO6", "L'amortissement, les stocks et les inventaires", "Comptabilité", ["Terminale pro"],
S("Les écritures d'inventaire ajustent les valeurs comptables à la réalité de fin d'exercice, notamment pour les immobilisations et les stocks."
  "|L'amortissement constate la perte de valeur d'une immobilisation due à l'usage, au temps ou à l'obsolescence."
  "|La durée d'utilisation et la valeur résiduelle permettent de calculer l'annuité d'amortissement selon le mode retenu."
  "|L'amortissement linéaire répartit la valeur amortissable de façon constante sur la durée de vie."
  "|L'amortissement dégressif applique un taux plus élevé les premières années, car l'actif rend plus de services au début."
  "|La valeur nette comptable vaut valeur d'acquisition moins amortissements cumulés."
  "|Le stock final est évalué selon une méthode de coût : coût d'acquisition, coût de production ou coût de remplacement."
  "|La méthode du premier entré, premier sorti, ou FIFO, valorise les sorties avec le coût des premiers articles entrés."
  "|La méthode du dernier entré, premier sorti, ou LIFO, valorise les sorties avec le coût des derniers articles entrés."
  "|En période d'inflation, FIFO conduit à un stock final plus élevé et à un résultat plus élevé que LIFO."
  "|L'inventaire physique confronte la quantité comptable et la quantité réelle : il révèle les écarts de vol, casse ou erreur de saisie."
  "|Une provision pour dépréciation est constituée lorsqu'un actif perd durablement de la valeur : elle est réversible, contrairement à l'amortissement."),
[QC("Quel est l'objet d'un amortissement ?", "Augmenter le chiffre d'affaires~Constater la perte de valeur d'une immobilisation~Réduire la TVA~Financer un emprunt", 1,
     "L'amortissement étale la perte de valeur d'un bien durable sur sa durée d'utilisation."),
 QC("Comment calcule-t-on l'amortissement linéaire annuel ?", "Valeur d'acquisition divisée par durée de vie (après valeur résiduelle)~Valeur d'acquisition multipliée par le taux de TVA~Valeur nette multipliée par 2~Chiffre d'affaires moins achats", 0,
     "On répartit la valeur amortissable de manière constante sur la durée d'utilisation."),
 QC("Quels effets a l'amortissement dégressif ?", "Une charge constante~Une charge plus forte au début~Aucune charge~Une charge uniquement la dernière année", 1,
     "Le taux dégressif est multiplié par un coefficient les premières années."),
 QC("Que vaut la valeur nette comptable ?", "Valeur d'acquisition plus amortissements~Valeur d'acquisition moins amortissements cumulés~Prix de revente~Valeur de la TVA", 1,
     "La VNC diminue au fur et à mesure des amortissements constatés."),
 QC("Quelle méthode valorise les sorties avec les premiers articles entrés ?", "LIFO~FIFO~Linéaire~Dégressif", 1,
     "FIFO signifie premier entré, premier sorti."),
 QC("En période d'inflation, quelle méthode donne le résultat le plus élevé ?", "LIFO~FIFO~Les deux sont identiques~Aucune des deux", 1,
     "FIFO laisse au stock final les coûts récents les plus élevés et réduit le coût des ventes."),
 QC("Quelle différence essentielle entre amortissement et provision ?", "L'amortissement est réversible, la provision ne l'est pas~La provision est réversible, l'amortissement ne l'est pas~Elles sont identiques~La provision concerne seulement la TVA", 1,
     "Une provision peut être reprise si la dépréciation disparaît, pas un amortissement."),
 QT("Un matériel est acquis 12 000 €, avec une valeur résiduelle de 2 000 € et une durée de vie de 5 ans. Calculer l'amortissement linéaire annuel et la valeur nette comptable après 3 ans.",
     "La valeur amortissable vaut 12 000 − 2 000 = 10 000 €. L'annuité linéaire est 10 000 / 5 = 2 000 € par an. Après 3 ans, les amortissements cumulés atteignent 3 × 2 000 = 6 000 €. La valeur nette comptable vaut donc 12 000 − 6 000 = 6 000 €. Elle reste supérieure à la valeur résiduelle de 2 000 €, qui sera atteinte en fin de cinquième année. Chaque année, l'écriture débite le compte d'amortissement et crédite le compte d'immobilisation ou un compte d'amortissement cumulé.",
     "On calcule la valeur amortissable (10 000), l'annuité (2 000), puis la VNC après 3 ans (6 000)."),
 QT("Expliquer pourquoi le choix d'une méthode de valorisation des stocks influe sur le résultat.",
     "Le résultat dépend du coût des marchandises vendues, qui est déterminé par la méthode de valorisation. Avec FIFO, les premières entrées, souvent moins coûteuses en période d'inflation, sont imputées aux ventes : le coût des ventes est faible et le résultat élevé, tandis que le stock final reste valorisé à des coûts récents plus élevés. Avec LIFO, le coût des ventes intègre les prix récents, donc le résultat est plus faible et le stock final reste à des coûts anciens. Ce choix n'est pas neutre : il modifie la marge, l'impôt et la perception de la rentabilité, ce qui impose de le préciser dans l'annexe et de l'appliquer de façon constante d'un exercice à l'autre.",
     "On relie méthode, coût des ventes, stock final, résultat et obligation de constance.")],
C("Les écritures d'inventaire ajustent la valeur des actifs : amortissements, valorisation des stocks et provisions.",
  "Amortissement linéaire = (acquisition − résiduelle) / durée",
  "VNC = acquisition − amortissements cumulés · FIFO ou LIFO",
  "Amortissement~Perte de valeur durable~VNC~Valeur nette comptable~Stock~Bien en attente de vente~FIFO~Premier entre premier sorti~Inventaire~Confrontation reel et comptable",
  "Identifier les immobilisations à amortir|Choisir le mode et la durée|Calculer l'annuité|Valoriser les stocks|Réaliser l'inventaire physique",
  "Confondre amortissement et provision|Oublier la valeur résiduelle|Changer de méthode de stock sans justification|Ignorer les écarts d'inventaire",
  "Acquisition 12 000~Valeur residuelle 2 000~Amortissable 10 000~Annuite 2 000~Apres 3 ans~VNC 6 000~FIFO~Resultat plus eleve",
  "Amortissement~Non reversible~Provision~Reversible si la valeur revient",
  "FIFO~Premieres entrees en sortie~LIFO~Dernieres entrees en sortie"))

# ============================================================ CO7
add("CO7", "L'analyse financière et les ratios de gestion", "Comptabilité", ["Terminale pro"],
S("L'analyse financière interprète les comptes de l'entreprise pour porter un jugement sur sa solidité, sa rentabilité et son efficacité."
  "|Elle repose sur les comptes annuels : bilan, compte de résultat et annexe, complétés si possible par le plan de trésorerie."
  "|L'analyse horizontale compare un même poste d'une année sur l'autre pour dégager les tendances et les ruptures."
  "|L'analyse verticale exprime chaque poste en pourcentage d'un agrégat de référence, comme le total du bilan ou le chiffre d'affaires."
  "|Le ratio est le rapport entre deux grandeurs choisies pour mettre en évidence un aspect de la situation."
  "|Le fonds de roulement net global mesure la capacité de financement à long terme : ressources durables moins actif immobilisé."
  "|Le besoin en fonds de roulement traduit les besoins de financement liés au cycle d'exploitation."
  "|La trésorerie nette s'obtient par FRNG moins BFR : elle montre les disponibilités immédiates ou le découvert."
  "|La rentabilité des capitaux propres, ou ROE, rapporte le résultat net aux capitaux propres."
  "|La rentabilité économique rapporte le résultat d'exploitation au capital employé, tous financements confondus."
  "|Le délai de paiement des clients se calcule en rapportant les créances clients au chiffre d'affaires TTC, puis en multipliant par 365."
  "|Un ratio n'a de sens que comparé à une norme sectorielle, à l'historique de l'entreprise ou à un concurrent, et jamais isolément."),
[QC("Quel document n'est pas un compte annuel ?", "Le bilan~Le compte de résultat~L'annexe~Le plan de trésorerie", 3,
     "Les comptes annuels comprennent le bilan, le compte de résultat et l'annexe."),
 QC("Qu'est-ce qu'une analyse verticale ?", "Une comparaison dans le temps~Une expression en pourcentage d'un agrégat~Une comparaison entre entreprises~Une prévision de trésorerie", 1,
     "L'analyse verticale met chaque poste en relation avec un total de référence."),
 QC("Que mesure le FRNG ?", "La rentabilité~La capacité de financement à long terme~Le chiffre d'affaires~Les seules dettes", 1,
     "Le FRNG compare ressources durables et actif immobilisé."),
 QC("Comment obtient-on la trésorerie nette ?", "FRNG plus BFR~FRNG moins BFR~Capitaux propres plus dettes~Résultat moins impôt", 1,
     "La trésorerie nette est la différence entre fonds de roulement et besoin en fonds de roulement."),
 QC("Que rapporte le ROE ?", "Le résultat net aux capitaux propres~Le résultat d'exploitation au chiffre d'affaires~Les dettes aux capitaux~Le stock aux ventes", 0,
     "ROE = résultat net / capitaux propres."),
 QC("Pourquoi comparer les ratios à une norme sectorielle ?", "Parce qu'un chiffre isolé n'a pas de sens~Parce que la loi l'impose~Pour réduire les impôts~Pour supprimer l'annexe", 0,
     "L'interprétation exige un point de comparaison pertinent."),
 QC("Que révèle un allongement du délai de paiement clients ?", "Une amélioration de la trésorerie~Un risque de tension de trésorerie~Une hausse de la rentabilité~Une baisse des stocks", 1,
     "Les créances mettent plus de temps à être encaissées, ce qui mobilise de la trésorerie."),
 QT("Une entreprise a un FRNG de 60 000 € et un BFR de 85 000 €. Calculer sa trésorerie nette et interpréter la situation.",
     "La trésorerie nette vaut FRNG − BFR, soit 60 000 − 85 000 = −25 000 €. Elle est négative : l'entreprise a une position de découvert net de 25 000 €. Ses ressources durables ne suffisent pas à couvrir à la fois ses immobilisations et son besoin de financement d'exploitation. Elle devra recourir à des concours bancaires court terme ou réduire son BFR, par exemple en raccourcissant les délais de paiement clients ou en négociant ses délais fournisseurs. Un FRNG positif ne garantit donc pas une trésorerie saine si le BFR est plus élevé.",
     "On calcule −25 000 €, puis on explique le découvert et les pistes d'action."),
 QT("Expliquer la démarche d'une analyse financière complète et ses limites.",
     "On commence par lire les comptes annuels et vérifier leur cohérence, puis on réalise une analyse horizontale pour repérer les évolutions et une analyse verticale pour mesurer la structure du patrimoine et des charges. On calcule ensuite des ratios regroupés par famille : structure financière avec le FRNG, gestion du BFR et de la trésorerie, rentabilité avec le ROE et la rentabilité économique, et performance d'exploitation. On compare ces ratios à l'historique, aux normes sectorielles et aux concurrents. Enfin, on croise les constats pour formuler un diagnostic. Les limites sont importantes : les comptes sont des photographies passées, les méthodes comptables varient, l'inflation et les choix d'amortissement faussent les comparaisons, et aucun ratio ne remplace l'analyse du contexte et des perspectives.",
     "On décrit les étapes, les familles de ratios et les limites (données passées, comparabilité, contexte).")],
C("L'analyse financière transforme les comptes en indicateurs : structure, gestion, rentabilité et trésorerie.",
  "Trésorerie nette = FRNG − BFR · ROE = résultat net / capitaux propres",
  "Analyse horizontale dans le temps · analyse verticale en pourcentage",
  "Ratio~Rapport entre deux grandeurs~FRNG~Ressources durables moins immobilises~BFR~Besoin d'exploitation~Tresorerie~FRNG moins BFR~ROE~Rente des capitaux",
  "Lire les comptes annuels|Comparer dans le temps et en pourcentage|Calculer les ratios par famille|Comparer aux normes du secteur|Formuler un diagnostic nuance",
  "Interpréter un ratio isolément|Oublier le secteur d'activité|Confondre rentabilité et trésorerie|Ignorer les limites des comptes",
  "FRNG 60 000~BFR 85 000~Tresorerie~-25 000 et decouvert~ROE~Resultat sur capitaux propres~Delai clients~Credites sur CA TTC",
  "Analyse horizontale~Evolution dans le temps~Analyse verticale~Structure en pourcentage",
  "Rentabilite~Capacite a generer du resultat~Liquidite~Capacite a payer"))

# ============================================================ DR1
add("DR1", "Les sources du droit et les institutions de la Ve République", "Droit", ["2nde pro"],
S("Le droit est un ensemble de règles juridiques organisées qui régissent la vie en société et les relations entre les personnes."
  "|Les sources écrites du droit sont la Constitution, les lois votées par le Parlement et les règlements pris par le pouvoir exécutif."
  "|La Constitution du 4 octobre 1958 est la loi fondamentale de la Ve République : elle organise les pouvoirs et les droits des citoyens."
  "|Le bloc de constitutionnalité comprend la Constitution de 1958, la Déclaration des droits de l'homme de 1789 et le préambule de 1946."
  "|Les sources non écrites incluent la jurisprudence, c'est-à-dire les décisions des tribunaux, et les usages."
  "|Le Parlement est composé de l'Assemblée nationale et du Sénat : il vote la loi et contrôle l'action du Gouvernement."
  "|Le Président de la République est élu au suffrage universel direct ; il nomme le Premier ministre et peut dissoudre l'Assemblée nationale."
  "|Le Gouvernement, dirigé par le Premier ministre, définit et met en œuvre la politique de la Nation."
  "|Le Conseil constitutionnel vérifie la conformité des lois à la Constitution et peut être saisi par les parlementaires."
  "|Le Conseil d'État est la juridiction administrative suprême et conseille le Gouvernement sur les projets de texte."
  "|La Cour de cassation est la juridiction suprême de l'ordre judiciaire : elle vérifie la bonne application du droit."
  "|Le Conseil européen et la Cour de justice de l'Union européenne produisent un droit qui s'impose aux États membres dans leurs domaines de compétence."),
[QC("Quelle est la loi fondamentale de la Ve République ?", "La Déclaration de 1789~La Constitution de 1958~Le Code civil~La loi de 1905", 1,
     "La Constitution du 4 octobre 1958 organise les institutions de la Ve République."),
 QC("Quel organe vote la loi ?", "Le Conseil d'État~Le Parlement~La Cour de cassation~Le Gouvernement", 1,
     "Le Parlement, composé de l'Assemblée nationale et du Sénat, vote la loi."),
 QC("Qui peut dissoudre l'Assemblée nationale ?", "Le Premier ministre~Le Président de la République~Le Conseil constitutionnel~Le Sénat", 1,
     "Le Président dispose du pouvoir de dissolution, prévu à l'article 12."),
 QC("Quelle juridiction vérifie la conformité des lois à la Constitution ?", "La Cour de cassation~Le Conseil constitutionnel~Le Conseil d'État~La Cour européenne des droits de l'homme", 1,
     "Le Conseil constitutionnel exerce un contrôle de constitutionnalité."),
 QC("Qu'appelle-t-on jurisprudence ?", "Une loi votée~Un ensemble de décisions de justice~Un règlement ministériel~Un usage professionnel", 1,
     "La jurisprudence est formée par les décisions rendues par les tribunaux."),
 QC("Quel est le rôle du Conseil d'État ?", "Juger les litiges administratifs et conseiller le Gouvernement~Juger les affaires pénales~Voter le budget~Nommer les préfets", 0,
     "Il est à la fois conseiller du Gouvernement et juge administratif suprême."),
 QC("Quel texte de 1789 fait partie du bloc de constitutionnalité ?", "Le Code pénal~La Déclaration des droits de l'homme et du citoyen~Le traité de Versailles~La loi de finances", 1,
     "La Déclaration de 1789 est intégrée au bloc de constitutionnalité."),
 QT("Expliquer comment une loi est adoptée et contrôlée sous la Ve République.",
     "Un projet de loi est déposé par le Gouvernement ou une proposition par un parlementaire. Le texte est examiné en commission, puis discuté et voté par l'Assemblée nationale et le Sénat ; en cas de désaccord, une commission mixte paritaire cherche un texte commun et le Gouvernement peut engager sa responsabilité pour accélérer l'adoption. La loi est ensuite promulguée par le Président de la République et publiée au Journal officiel. Avant ou après sa promulgation, le Conseil constitutionnel peut être saisi par soixante députés ou soixante sénateurs, ou par le Conseil d'État et la Cour de cassation pour une question prioritaire de constitutionnalité, et il censure les dispositions contraires à la Constitution.",
     "On décrit dépôt, examen, vote, promulgation et contrôle de constitutionnalité."),
 QT("Distinguer sources écrites et sources non écrites du droit, et expliquer leur complémentarité.",
     "Les sources écrites sont les textes officiels : Constitution, lois, règlements, traités et directives européennes. Elles offrent la sécurité juridique car elles sont publiées et accessibles. Les sources non écrites sont la jurisprudence, les usages et les principes généraux du droit : elles complètent les textes lorsque ceux-ci sont imprécis ou silencieux. La jurisprudence interprète la loi et l'adapte à des situations nouvelles, par exemple dans le domaine numérique. Les deux catégories sont complémentaires : le juge applique le texte écrit tout en s'appuyant sur une interprétation construite au fil des décisions, ce qui rend le droit vivant sans remettre en cause la primauté de la loi.",
     "On définit les deux catégories et on montre comment la jurisprudence complète le texte.")],
C("Le droit français s'appuie sur une hiérarchie de textes et sur des institutions qui les élaborent, les appliquent et les contrôlent.",
  "Constitution > lois > règlements · jurisprudence et usages complètent",
  "Parlement : loi · Gouvernement : action · Conseil constitutionnel : contrôle",
  "Constitution~Loi fondamentale~Parlement~Assemblee et Senat~Gouvernement~Politique nationale~Jurisprudence~Decisions de justice~Controle~Constitutionnalite",
  "Situer la source dans la hiérarchie|Identifier l'institution competente|Préciser la procédure|Vérifier le contrôle|Appliquer au cas presente",
  "Confondre loi et règlement|Ignorer le bloc de constitutionnalité|Mélanger les ordres judiciaire et administratif|Oublier le droit européen",
  "1958~Constitution de la Ve Republique~1789~Declaration des droits~Conseil constitutionnel~Controle des lois~Conseil d'Etat~Juge administratif~Cassation~Juge judiciaire",
  "Sources ecrites~Textes publies~Sources non ecrites~Jurisprudence et usages",
  "Assemblee nationale~Chambre basse~Senat~Chambre haute"))

# ============================================================ DR2
add("DR2", "Le contrat et la responsabilité civile", "Droit", ["1re pro"],
S("Un contrat est un accord de volontés entre deux ou plusieurs personnes destiné à créer, modifier ou éteindre des obligations."
  "|Le Code civil pose le principe de la liberté contractuelle : chacun est libre de contracter ou non, et de choisir son cocontractant."
  "|La formation d'un contrat suppose un consentement valable : il doit être libre, éclairé et non vicié par l'erreur, le dol ou la violence."
  "|L'offre est une proposition de contrat et l'acceptation est l'adhésion à cette proposition : leur rencontre forme l'accord."
  "|Un contrat peut être écrit, oral ou tacite, mais certains contrats exigent un écrit pour être prouvés ou pour être valables."
  "|Les parties doivent avoir la capacité juridique : être majeures et non privées de leurs droits par une mesure de protection."
  "|L'objet du contrat doit être licite et certain : on ne peut contracter pour une prestation interdite par la loi."
  "|Le principe de la bonne foi s'impose dans la négociation, la formation et l'exécution du contrat."
  "|La responsabilité civile contractuelle engage un cocontractant qui n'exécute pas ses obligations : il doit réparer le dommage."
  "|La responsabilité civile délictuelle s'applique en l'absence de contrat, lorsqu'une faute cause un dommage à autrui."
  "|Pour obtenir réparation, il faut établir une faute, un dommage et un lien de causalité entre les deux."
  "|Une clause de non-responsabilité ne peut pas exonérer une personne de sa faute grave, dolosive ou d'une atteinte à la personne."),
[QC("Qu'est-ce qu'un contrat ?", "Un simple échange de courrier~Un accord de volontés créant des obligations~Une décision de justice~Un règlement intérieur", 1,
     "Le contrat suppose un accord entre les parties qui produit des effets juridiques."),
 QC("Quel vice du consentement correspond à une tromperie volontaire ?", "L'erreur~Le dol~La violence~La contrainte", 1,
     "Le dol est une manœuvre frauduleuse destinée à obtenir le consentement."),
 QC("Quelle condition concerne l'objet du contrat ?", "Il doit être gratuit~Il doit être licite et certain~Il doit être écrit~Il doit être public", 1,
     "Une prestation illicite ou indéterminée rend le contrat nul."),
 QC("Quand naît la responsabilité délictuelle ?", "Lorsqu'un contrat est signé~En l'absence de contrat, à la suite d'une faute~Uniquement en matière pénale~Uniquement entre commerçants", 1,
     "Le délit civil ne suppose aucun lien contractuel entre les parties."),
 QC("Quels sont les trois éléments de la responsabilité civile ?", "Faute, dommage, lien de causalité~Offre, acceptation, consentement~Loi, décret, arrêté~Dette, paiement, quittance", 0,
     "Il faut prouver une faute, un dommage et le lien entre les deux."),
 QC("Quel principe gouverne l'exécution du contrat ?", "La bonne foi~La discrétion absolue~La gratuité~Le secret professionnel", 0,
     "Les parties doivent exécuter le contrat de bonne foi."),
 QC("Une clause peut-elle exclure toute responsabilité en cas de faute grave ?", "Oui, toujours~Non, elle est réputée non écrite~Oui, si elle est manuscrite~Oui, entre professionnels seulement", 1,
     "Une telle clause est frappée de nullité car elle vide le contrat de sa substance."),
 QT("Un client signe un contrat de prestation après avoir été trompé sur les qualifications du prestataire. Quel est le problème juridique et quelle solution ?",
     "Le consentement du client a été vicié par le dol : le prestataire a usé de manœuvres frauduleuses en se présentant avec des qualifications qu'il n'a pas, ce qui a déterminé le client à signer. Un consentement obtenu par dol est un consentement non valable. Le client peut agir en nullité du contrat : l'acte est alors anéanti rétroactivement, avec restitution des prestations et éventuellement des dommages-intérêts. Il peut aussi demander une réduction du prix ou une indemnisation sur le fondement de la responsabilité contractuelle. La bonne foi, exigée dès la négociation, n'a pas été respectée.",
     "On identifie le dol, la nullité du consentement et les conséquences (restitutions, dommages)."),
 QT("Distinguer responsabilité contractuelle et responsabilité délictuelle et donner un exemple de chacune.",
     "La responsabilité contractuelle suppose un contrat valable et une inexécution d'une obligation : par exemple un prestataire qui ne livre pas au terme prévu doit réparer le préjudice du client. La responsabilité délictuelle n'exige aucun contrat : elle repose sur une faute, un dommage et un lien de causalité, par exemple un passant blessé par la chute d'un objet sur un chantier. Les deux regimes diffèrent par la preuve et par les clauses possibles : le contrat peut prévoir des pénalités de retard ou aménager certaines responsabilités, ce qui n'existe pas entre étrangers. Dans les deux cas, la réparation vise à remettre la victime dans la situation où elle aurait été sans le dommage.",
     "On donne une définition et un exemple pour chaque régime, puis les différences de preuve.")],
C("Le contrat crée des obligations ; sa validité repose sur le consentement et sa méconnaissance engage une responsabilité.",
  "Consentement + capacité + objet licite + cause = contrat valable",
  "Responsabilité : faute + dommage + lien de causalité",
  "Contrat~Accord de volontes~Consentement~Libre et eclaire~Dol~Tromperie volontaire~Responsabilite~Reparation du dommage~Bonne foi~Exécution loyal",
  "Vérifier la formation du contrat|Contrôler le consentement|Vérifier la capacité et l'objet|Qualifier le régime de responsabilité|Évaluer le dommage et la réparation",
  "Confondre dol et erreur|Oublier la preuve du lien de causalité|Croire que toute clause est valable|Négliger la bonne foi précontractuelle",
  "Dol~Tromperie sur les qualifications~Nullite~Contrat aneanti~Retard de livraison~Responsabilite contractuelle~Chantier~Responsabilite delictuelle",
  "Contractuelle~Inexecution d'une obligation~Delictuelle~Faute sans contrat",
  "Erreur~Croyance fausse~Dol~Manœuvre frauduleuse"))

# ============================================================ DR3
add("DR3", "Le droit du travail et la relation de travail", "Droit", ["1re pro", "Terminale pro"],
S("Le contrat de travail est une convention par laquelle une personne s'engage à travailler pour le compte d'une autre, sous sa direction, moyennant une rémunération."
  "|Trois critères caractérisent la relation de travail : la prestation de travail, la rémunération et le lien de subordination."
  "|Le lien de subordination suppose que l'employeur dispose d'un pouvoir de direction, de contrôle et de sanction."
  "|Le contrat à durée indéterminée, ou CDI, est la forme normale et permanente de la relation de travail."
  "|Le contrat à durée déterminée, ou CDD, est réservé à des cas limités : remplacement, surcroît d'activité ou saisonnalité."
  "|La durée légale du travail est de 35 heures par semaine en France ; les heures au-delà sont des heures supplémentaires majorées."
  "|Le salaire brut comprend le salaire de base, les primes et les heures supplémentaires ; le salaire net est calculé après cotisations salariales."
  "|L'employeur supporte des cotisations patronales qui s'ajoutent au salaire brut pour former le coût total de l'emploi."
  "|Le bulletin de salaire doit mentionner l'identité des parties, la période, le nombre d'heures, les rubriques de rémunération et les cotisations."
  "|Le salarié bénéficie de droits, comme le repos quotidien, les congés payés et la protection contre le licenciement sans cause réelle et sérieuse."
  "|Il a également des obligations : accomplir sa prestation, respecter les consignes et ne pas divulguer les informations confidentielles de l'entreprise."
  "|Le comité social et économique, ou CSE, représente les salariés et est consulté sur les décisions importantes de l'entreprise."),
[QC("Quel est le critère central du contrat de travail ?", "La rémunération seule~Le lien de subordination~La durée du contrat~Le lieu de travail", 1,
     "Le pouvoir de direction, de contrôle et de sanction distingue le salarié du prestataire indépendant."),
 QC("Quelle est la forme normale du contrat de travail ?", "Le CDD~Le CDI~Le contrat saisonnier~Le contrat d'apprentissage", 1,
     "Le CDI est la forme de droit commun ; le CDD reste exceptionnel."),
 QC("Dans quel cas peut-on recourir à un CDD ?", "Pour un poste permanent~Pour remplacer un salarié absent~Pour éviter une embauche~Sans motif particulier", 1,
     "Le CDD est limité à des motifs précis prévus par le Code du travail."),
 QC("Quelle est la durée légale hebdomadaire du travail en France ?", "30 heures~35 heures~39 heures~40 heures", 1,
     "La durée légale est fixée à 35 heures par semaine."),
 QC("Comment obtient-on le salaire net ?", "Brut plus cotisations patronales~Brut moins cotisations salariales~Brut multiplié par le taux de TVA~Brut divisé par 35", 1,
     "Les prélèvements à la charge du salarié sont déduits du brut."),
 QC("Quel rôle joue le CSE ?", "Représenter les salariés et être consulté~Fixer les prix de vente~Remplacer l'inspecteur du travail~Signer les contrats clients", 0,
     "Le comité social et économique est l'instance représentative du personnel."),
 QC("Quel contenu ne figure pas sur un bulletin de salaire ?", "Le nombre d'heures~Les cotisations~La rubrique de rémunération~Le chiffre d'affaires de l'entreprise", 3,
     "Le bulletin de paie est individuel et ne comporte pas les résultats commerciaux."),
 QT("Un salarié accomplit 5 heures supplémentaires dans une semaine à 25 % de majoration, sur la base d'un salaire horaire de 16 €. Calculer le montant brut correspondant.",
     "Le salaire horaire majoré vaut 16 × 1,25 = 20 €. Les 5 heures supplémentaires donnent donc 5 × 20 = 100 € brut. On peut aussi calculer le salaire normal de ces heures, 5 × 16 = 80 €, puis la majoration de 25 %, soit 20 €, pour un total de 100 €. Ce montant s'ajoute au salaire de base dans la rubrique heures supplémentaires du bulletin et il est soumis aux cotisations sociales. Les heures supplémentaires doivent être justifiées et respecter le contingent annuel et les limites quotidiennes prévues par le Code du travail.",
     "On calcule le taux majoré (20 €), puis 5 × 20 = 100 €, avec rappel des cotisations."),
 QT("Expliquer la différence entre salarié et travailleur indépendant et ses conséquences.",
     "Le salarié est lié à l'employeur par un contrat de travail et un lien de subordination : il reçoit des consignes, est contrôlé et peut être sanctionné. Le travailleur indépendant exerce son activité pour son propre compte, fixe librement son organisation et supporte le risque économique de son entreprise. Les conséquences sont importantes : le salarié bénéficie du salaire minimum, des congés payés, de la protection contre le licenciement et du régime de sécurité sociale salarié, tandis que l'indépendant paie ses cotisations et n'a pas de droit au chômage dans les mêmes conditions. La qualification juridique est donc déterminante et le juge requalifie parfois une collaboration en contrat de travail lorsque la subordination est réelle.",
     "On oppose subordination et autonomie, puis les conséquences en droit social et en protection.")],
C("La relation de travail repose sur un contrat et un lien de subordination ; elle crée des droits et des obligations pour les deux parties.",
  "Lien de subordination = direction + contrôle + sanction",
  "CDI : forme normale · CDD : motifs limités · 35 heures légales",
  "Contrat de travail~Prestation et remuneration~Subordination~Pouvoir de direction~CDI~Forme normale~CDD~Motifs limites~Bulletin de paie~Document obligatoire",
  "Qualifier la relation de travail|Vérifier le type de contrat|Contrôler la durée du travail|Calculer la rémunération|Appliquer les droits et obligations",
  "Confondre salarié et indépendant|Oublier la majoration des heures supplémentaires|Calculer le net à partir du brut sans cotisations|Ignorer le rôle du CSE",
  "16 €/h et 25 %~Taux majore 20 €~5 heures~Montant brut 100 €~35 heures~Duree legale~CSE~Representation du personnel",
  "Salarie~Lien de subordination~Independant~Autonomie et risque",
  "Salaire brut~Avant cotisations~Salaire net~Apres cotisations salariales"))

# ============================================================ DR4
add("DR4", "La protection des données personnelles et le RGPD", "Droit", ["Terminale pro"],
S("Une donnée personnelle est toute information relative à une personne physique identifiée ou identifiable, directement ou indirectement."
  "|Le règlement général sur la protection des données, ou RGPD, est entré en application le 25 mai 2018 dans l'Union européenne."
  "|Il remplace la directive de 1995 et renforce les droits des personnes ainsi que les obligations des organisations."
  "|Les principes fondamentaux sont la licéité, la loyauté, la transparence, la finalité, la minimisation et l'exactitude des données."
  "|La minimisation impose de ne collecter que les données nécessaires à la finalité poursuivie, ni plus ni moins."
  "|La conservation doit être limitée dans le temps : les données sont supprimées ou anonymisées dès qu'elles ne sont plus utiles."
  "|La base légale du traitement doit être identifiée : consentement, exécution du contrat, obligation légale, intérêt vital, mission publique ou intérêt légitime."
  "|Le consentement doit être libre, éclairé, spécifique et univoque, et il peut être retiré à tout moment."
  "|Les personnes disposent de droits : accès, rectification, effacement, limitation, portabilité et opposition."
  "|Le responsable de traitement doit tenir un registre des traitements, informer les personnes et sécuriser les données."
  "|La CNIL est l'autorité de contrôle française : elle conseille, contrôle et peut prononcer des sanctions administratives."
  "|Une violation de données doit être notifiée à la CNIL dans les 72 heures suivant sa prise de connaissance si le risque est élevé."),
[QC("Quelle est la date d'application du RGPD ?", "25 mai 2018~1er janvier 2016~17 décembre 2018~6 mai 1949", 0,
     "Le RGPD s'applique depuis le 25 mai 2018 dans toute l'Union européenne."),
 QC("Quel principe impose de collecter le minimum de données nécessaires ?", "La transparence~La minimisation~La portabilité~La finalité", 1,
     "La minimisation limite la collecte à ce qui est strictement utile."),
 QC("Quelle base légale repose sur un accord libre et éclairé ?", "L'obligation légale~Le consentement~L'intérêt légitime~Le contrat", 1,
     "Le consentement doit être libre, éclairé, spécifique et univoque."),
 QC("Quel droit permet d'obtenir une copie de ses données ?", "Le droit à l'effacement~Le droit d'accès~Le droit d'opposition~Le droit à la limitation", 1,
     "Le droit d'accès permet de prendre connaissance et d'obtenir une copie des données."),
 QC("Quel est le rôle de la CNIL ?", "Éditer les lois~Contrôler la protection des données et sanctionner~Gérer les impôts~Représenter les salariés", 1,
     "La CNIL est l'autorité de contrôle française en matière de données personnelles."),
 QC("Quel délai s'applique à la notification d'une violation à la CNIL ?", "24 heures~72 heures~7 jours~30 jours", 1,
     "L'article 33 du RGPD prévoit 72 heures après la prise de connaissance."),
 QC("Qu'une donnée anonymisée n'est-elle plus une donnée personnelle ?", "Parce qu'elle est chiffrée~Parce qu'elle ne permet plus d'identifier la personne~Parce qu'elle est stockée en France~Parce qu'elle est ancienne", 1,
     "L'anonymisation rend l'identification impossible par des moyens raisonnables."),
 QT("Une entreprise souhaite envoyer une newsletter à ses clients. Décrire les obligations essentielles au regard du RGPD.",
     "Elle doit d'abord identifier une base légale : pour de la prospection, le consentement est généralement requis, sauf exceptions pour les clients existants concernant des produits similaires avec possibilité de s'opposer dès le premier message. Le formulaire d'inscription doit être clair, non précoché, et préciser la finalité et le responsable de traitement. L'entreprise ne collecte que l'adresse e-mail nécessaire, informe sur la durée de conservation et sur les droits de la personne, et prévoit un lien de désinscription simple dans chaque message. Elle tient un registre des traitements, sécurise la base de données et doit pouvoir répondre rapidement à une demande d'accès, de rectification ou d'effacement. En cas de fuite de la base, elle notifiera la CNIL dans les 72 heures si le risque est élevé.",
     "On attend base légale, consentement, information, minimisation, droits, registre, sécurité et notification."),
 QT("Expliquer la différence entre pseudonymisation et anonymisation et leurs conséquences juridiques.",
     "La pseudonymisation remplace les identifiants directs par des pseudonymes tout en conservant séparément les informations permettant de réidentifier la personne : les données restent des données personnelles et le RGPD continue de s'appliquer. L'anonymisation supprime définitivement tout moyen d'identifier la personne, compte tenu des moyens raisonnables disponibles : les données sortent alors du champ du RGPD. La différence est donc une question de réversibilité. La pseudonymisation réduit le risque et constitue une mesure de sécurité recommandée, mais elle n'exonère pas des obligations : registre, information, sécurité et réponse aux droits. Une anonymisation mal réalisée, par exemple avec des quasi-identifiants comme la date de naissance et le code postal, peut être réidentifiée par recoupement.",
     "On oppose réversibilité et sortie du champ d'application, avec un exemple de réidentification.")],
C("Le RGPD encadre la collecte et l'usage des données personnelles par des principes, une base légale et des droits.",
  "Donnée personnelle = information sur une personne identifiée ou identifiable",
  "Licéité · loyauté · transparence · finalité · minimisation · exactitude · limitation",
  "Donnee personnelle~Information identifiable~RGPD~Reglement de 2018~Consentement~Libre et eclaire~Minimisation~Donnees necessaires~CNIL~Autorite de controle",
  "Identifier la finalité du traitement|Choisir la base légale|Collecter le minimum|Informer et sécuriser|Répondre aux droits et notifier",
  "Précocher une case de consentement|Conserver les données indéfiniment|Confondre pseudonymisation et anonymisation|Oublier la notification à 72 heures",
  "25 mai 2018~Application du RGPD~72 heures~Notification de violation~Droit d'acces~Copie des donnees~Desinscription~Retrait du consentement",
  "Pseudonymisation~Reversible et encore personnelle~Anonymisation~Irreversible et hors RGPD",
  "Consentement~Accord explicite~Interet legitime~Base legale alternative"))

# ============================================================ DR5
add("DR5", "Gestion administrative : courrier, archives et circuits d'information", "Droit", ["1re pro"],
S("La gestion administrative organise la circulation, le traitement et la conservation des informations au sein d'une organisation."
  "|Le courrier entrant est réceptionné, daté, enregistré puis orienté vers le service ou la personne compétente."
  "|L'accusé de réception permet de confirmer à l'expéditeur que sa demande a bien été reçue et prise en charge."
  "|Le courrier sortant est préparé, relu, validé par l'autorité compétente, puis envoyé et archivé avec sa pièce justificative."
  "|Un registre ou un logiciel de gestion documentaire assure la traçabilité des flux : date, expéditeur, objet, destinataire et suite donnée."
  "|Le circuit d'information décrit les étapes par lesquelles passe un document, de sa création à sa destination finale."
  "|Un circuit court limite le nombre d'intervenants et réduit les délais, tout en conservant les contrôles nécessaires."
  "|Le classement peut être chronologique, alphabétique, thématique ou selon le plan de classement de l'organisation."
  "|Les archives courantes concernent les affaires en cours ; les archives intermédiaires sont conservées avant versement ou élimination."
  "|Les délais de conservation varient selon la nature des documents : par exemple, les factures sont conservées dix ans en comptabilité."
  "|La confidentialité impose de limiter l'accès aux documents sensibles et de détruire les copies inutiles."
  "|Les outils numériques, messagerie, gestion électronique de documents et signature électronique, transforment ces pratiques sans supprimer les règles de preuve."),
[QC("Quelle est la première étape du traitement du courrier entrant ?", "L'archivage~La réception et l'enregistrement~La signature~L'expédition", 1,
     "On date et on enregistre le courrier dès son arrivée avant de l'orienter."),
 QC("À quoi sert un accusé de réception ?", "À payer la facture~À confirmer la bonne réception d'une demande~À classer les archives~À signer un contrat", 1,
     "Il apporte la preuve de la réception et rassure l'expéditeur."),
 QC("Quel document suit le courrier sortant ?", "Aucun document~Une copie archivée avec sa validation~Un bon de commande~Un bulletin de paie", 1,
     "La copie et les preuves d'envoi constituent les archives de l'organisation."),
 QC("Qu'appelle-t-on circuit court ?", "Un circuit sans contrôle~Un circuit avec peu d'intervenants~Un circuit obligatoirement papier~Un circuit uniquement externe", 1,
     "On réduit les étapes inutiles tout en gardant les validations requises."),
 QC("Quel critère de classement groupe les documents par sujet ?", "Chronologique~Alphabétique~Thématique~Numérique", 2,
     "Le classement thématique suit les matières ou les affaires."),
 QC("Combien de temps sont conservées les factures en comptabilité ?", "3 ans~5 ans~10 ans~Indéfiniment", 2,
     "Le délai légal de conservation comptable est de dix ans."),
 QC("Quel risque présente une copie inutile de document sensible ?", "Aucun~Une fuite de confidentialité~Une meilleure traçabilité~Une baisse des délais", 1,
     "Multiplier les copies augmente la surface d'exposition de l'information."),
 QT("Décrire le parcours d'une demande reçue par courriel dans un service administratif.",
     "Le message est d'abord identifié : date, expéditeur, objet et pièces jointes sont vérifiés, puis l'accusé de réception est envoyé. La demande est enregistrée dans le logiciel de gestion avec un numéro et un destinataire interne. Le responsable du service qualifie l'urgence et la compétence : il traite la demande, la transmet à un autre service ou la soumet à une validation hiérarchique. Une réponse est préparée, relue et envoyée, avec les pièces annoncées. Enfin, le message, la réponse et les preuves d'envoi sont archivés selon le plan de classement et le délai de conservation. Chaque étape est tracée pour permettre le suivi et la preuve.",
     "On attend réception, accusé, enregistrement, orientation, réponse, envoi et archivage avec traçabilité."),
 QT("Expliquer pourquoi la traçabilité et la confidentialité sont deux exigences simultanées de la gestion administrative.",
     "La traçabilité permet de savoir qui a reçu, traité et validé un document, à quelle date et avec quelle suite : elle est indispensable pour répondre à une réclamation, prouver une décision et retrouver une information. La confidentialité impose de limiter la diffusion des informations sensibles aux seules personnes autorisées. Ces deux exigences peuvent sembler opposées, car enregistrer chaque étape augmente le nombre de traces accessibles. Elles sont en fait complémentaires si l'accès au registre est contrôlé, si les droits sont attribués par rôle et si les copies inutiles sont détruites. Une bonne organisation documentaire concilie la preuve du traitement et la protection des données, notamment dans une logique de RGPD.",
     "On définit les deux exigences, puis on montre leur articulation par les droits d'accès et la destruction des copies.")],
C("La gestion administrative fait circuler l'information dans un circuit tracé, tout en maîtrisant les délais, l'accès et la conservation.",
  "Circuit : réception → enregistrement → orientation → traitement → réponse → archivage",
  "Factures : 10 ans · confidentialité · traçabilité",
  "Courrier entrant~Accuse et enregistrement~Circuit~Etapes de traitement~Classement~Thematique ou chronologique~Archive~Conservation~Tracabilite~Preuve du suivi",
  "Réceptionner et dater|Enregistrer et accuser réception|Orienter vers le bon service|Traiter et répondre|Archiver et détruire les copies",
  "Oublier l'accusé de réception|Laisser un document sans destinataire|Conserver trop longtemps|Multiplier les copies non contrôlées",
  "Accuse de reception~Preuve d'arrivee~Registre~Tracabilite~10 ans~Conservation des factures~Circuit court~Moins d'etapes~RGPD~Protection",
  "Archives courantes~Affaires en cours~Archives intermediaires~Avant versement ou elimination",
  "Classement chronologique~Par date~Classement thematique~Par sujet"))

# ============================================================ DR6
add("DR6", "Gestion financière : budget, trésorerie et moyens de paiement", "Droit", ["Terminale pro"],
S("La gestion financière de l'entreprise vise à prévoir, suivre et maîtriser ses flux d'argent pour faire face à ses engagements."
  "|Le budget prévisionnel compare les recettes et les dépenses attendues sur une période, souvent l'année à venir."
  "|Le suivi budgétaire mesure les écarts entre prévisions et réalisations et déclenche des actions correctives si nécessaire."
  "|Le plan de trésorerie prévoit mois par mois les encaissements et les décaissements pour anticiper les besoins de financement."
  "|Une entreprise bénéficiaire peut manquer de trésorerie si ses clients paient tardivement alors que ses fournisseurs doivent être réglés rapidement."
  "|Les principaux moyens de paiement sont l'espèce, le chèque, le virement, la carte bancaire, le prélèvement et l'effet de commerce."
  "|Le virement bancaire est un ordre donné par le débiteur à sa banque de transférer une somme sur le compte du bénéficiaire."
  "|Le prélèvement est un ordre donné par le créancier, avec mandat du débiteur, pour être payé à échéance."
  "|Le délai de paiement entre professionnels est en principe de 30 jours après réception de la facture, avec des exceptions possibles."
  "|Les intérêts de retard sont dus automatiquement en cas de dépassement du délai, sans mise en demeure préalable."
  "|La banque peut accorder une facilité de caisse ou un découvert autorisé pour couvrir un besoin temporaire de trésorerie."
  "|Le rapprochement bancaire compare les écritures de l'entreprise et le relevé de compte pour repérer décalages, erreurs et frais."),
[QC("Quel document prévoit les encaissements et décaissements mois par mois ?", "Le bilan~Le plan de trésorerie~Le compte de résultat~L'inventaire", 1,
     "Le plan de trésorerie établit le calendrier prévisionnel des flux d'argent."),
 QC("Quel moyen de paiement part d'un ordre du créancier ?", "Le virement~Le chèque~Le prélèvement~L'espèce", 2,
     "Le prélèvement est initié par le créancier avec un mandat du débiteur."),
 QC("Quel est le délai légal de paiement entre professionnels ?", "8 jours~30 jours~60 jours~90 jours", 1,
     "Le délai de référence est de 30 jours après réception de la facture."),
 QC("Quand des intérêts de retard sont-ils dus ?", "Après une mise en demeure~Automatiquement en cas de dépassement du délai~Jamais entre professionnels~Uniquement sur les chèques", 1,
     "Ils courent de plein droit dès l'échéance dépassée."),
 QC("Qu'est-ce qu'une facilité de caisse ?", "Un impôt~Un concours bancaire court pour un besoin temporaire~Une assurance~Un compte d'épargne", 1,
     "Elle permet de couvrir momentanément un découvert de trésorerie."),
 QC("À quoi sert le rapprochement bancaire ?", "À calculer la TVA~À comparer les écritures internes et le relevé bancaire~À préparer la paie~À clore les stocks", 1,
     "Il met en évidence les écarts de date, les erreurs et les frais bancaires."),
 QC("Pourquoi une entreprise peut-elle manquer de trésorerie malgré un bénéfice ?", "Parce que le bénéfice est fictional~Parce que les encaissements sont décalés par rapport aux décaissements~Parce que la TVA est nulle~Parce que le bilan est faux", 1,
     "Le décalage des flux, ou BFR, explique cette situation courante."),
 QT("Une entreprise prévoit 80 000 € d'encaissements et 95 000 € de décaissements en mai, avec un solde initial de 20 000 €. Calculer le solde prévisionnel de fin mai et proposer une action.",
     "Le solde prévisionnel de fin mai vaut solde initial + encaissements − décaissements, soit 20 000 + 80 000 − 95 000 = 5 000 €. La trésorerie reste positive mais elle s'est fortement dégradée, passant de 20 000 € à 5 000 € en un mois. Si la tendance se poursuit en juin, un découvert apparaîtra. L'entreprise peut accélérer le recouvrement des créances, négocier un délai supplémentaire avec un fournisseur, étaler un investissement prévu ou demander une facilité de caisse à sa banque. Elle doit surtout mettre à jour le plan de trésorerie avec les dates précises d'encaissement plutôt qu'avec des montants mensuels globaux.",
     "On calcule 5 000 €, puis on propose des actions de recouvrement, de délai et de financement."),
 QT("Expliquer l'intérêt d'un rapprochement bancaire et décrire les écarts les plus fréquents.",
     "Le rapprochement bancaire compare le solde du compte 512 dans la comptabilité de l'entreprise avec le solde du relevé envoyé par la banque à une même date. Il permet de détecter les erreurs de saisie, les écritures omises, les chèques non encore encaissés, les virements en cours et les frais ou agios prélevés par la banque mais pas encore comptabilisés. Il révèle aussi des opérations non autorisées et constitue donc un contrôle interne important. On aboutit à un solde rapproché identique des deux côtés, après avoir enregistré les écritures de régularisation nécessaires. Sa régularité renforce la fiabilité de la trésorerie affichée et limite les risques de fraude.",
     "On décrit la comparaison, les types d'écarts, les régularisations et le rôle de contrôle interne.")],
C("La gestion financière anticipe les flux, arbitre les moyens de paiement et contrôle la trésorerie par le rapprochement bancaire.",
  "Solde prévisionnel = solde initial + encaissements − décaissements",
  "Délai légal : 30 jours · intérêts de retard automatiques",
  "Budget~Previsions de recettes et depenses~Tresorerie~Disponibilites~Plan de tresorerie~Calendrier des flux~Virement~Ordre du debiteur~Prelevement~Ordre du creancier",
  "Établir le budget prévisionnel|Construire le plan de trésorerie|Choisir le moyen de paiement|Surveiller les échéances|Réaliser le rapprochement bancaire",
  "Confondre virement et prélèvement|Oublier les intérêts de retard|Négliger les délais clients|Ne jamais rapprocher le compte bancaire",
  "Solde initial 20 000~Encaissements 80 000~Decaissements 95 000~Solde final 5 000~30 jours~Delai legal~Agios~Frais bancaires a regulariser",
  "Virement~Ordre du debiteur~Prelevement~Ordre du creancier",
  "Budget~Prevision globale~Plan de tresorerie~Calendrier mensuel"))

# FIN DES LOTS
valider_et_ecrire(F, "pro-gestion-mat-part-B.json")
