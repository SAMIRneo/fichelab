# PARTIE D — spécialités économiques et autres (SES, EPS spécialité)
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lg_common import f, q, t, a, save

F, AN = [], []

SSES1 = "Programme de spécialité SES de première générale, arrêté du 17 janvier 2019, BO spécial n° 1 du 22 janvier 2019, éduscol"
SSES2 = "Programme de spécialité SES de terminale générale, arrêté du 19 juillet 2019, BO spécial n° 8 du 25 juillet 2019 ; note de service du 11 septembre 2026 (BO spécial n° 4), éduscol"
SEPS1 = "Programme de spécialité éducation physique et sportive de première générale, BO spécial n° 1 du 22 janvier 2019, éduscol"
SEPS2 = "Programme de spécialité éducation physique et sportive de terminale générale, BO spécial n° 8 du 25 juillet 2019, éduscol"

# ---------------- SES ----------------
F.append(f(["1re"], "SES", "Chapitre : La monnaie, le crédit bancaire et la création monétaire", SSES1, [
 "Le programme de première comprend le questionnement « Qu'est-ce que la monnaie et comment est-elle créée ? » dans le champ économie.",
 "La monnaie remplit trois fonctions : intermédiaire des échanges (paiement), unité de compte (mesure de la valeur) et réserve de valeur (conservation du pouvoir d'achat).",
 "Ses formes se sont diversifiées : monnaie marchandise, monnaie métallique, monnaie fiduciaire (billets et pièces), monnaie scripturale (dépôts bancaires) et monnaie électronique.",
 "La monnaie scripturale représente l'essentiel de la masse monétaire : elle circule par virement, chèque, carte bancaire ou prélèvement.",
 "Une banque commerciale reçoit des dépôts (passif) et accorde des crédits (actif) : l'octroi d'un crédit crée simultanément une créance pour la banque et un dépôt pour l'emprunteur.",
 "La monnaie est donc endogène : elle naît du crédit et de la demande d'emprunts des agents économiques, dans un cadre réglementé par la banque centrale.",
 "La Banque centrale européenne (BCE), créée en 1998, pilote la politique monétaire de la zone euro : elle fixe les taux directeurs pour maintenir la stabilité des prix.",
 "Le multiplicateur de crédit est limité par le coefficient de réserves obligatoires, les besoins de liquidité des banques et la demande de crédit.",
 "Les agrégats monétaires (M1, M2, M3) mesurent la masse monétaire selon le degré de liquidité : M1 inclut la monnaie fiduciaire et les dépôts à vue.",
 "La question du financement de l'économie et de la stabilité financière est au cœur de l'actualité : les crises bancaires montrent les risques d'une création monétaire mal contrôlée."
], [
 q("Quelle fonction de la monnaie permet de différer un achat dans le temps ?", ["Unité de compte", "Réserve de valeur", "Intermédiaire des échanges", "Instrument de crédit"], 1, "La fonction de réserve de valeur permet de conserver le pouvoir d'achat ; l'intermédiaire des échanges sert au paiement immédiat."),
 q("Comment une banque commerciale crée-t-elle de la monnaie ?", ["En imprimant des billets", "En accordant un crédit, qui crée un dépôt", "En achetant de l'or", "En levant des impôts"], 1, "La créance sur l'emprunteur (actif) correspond à un dépôt (passif) : la monnaie scripturale naît du crédit."),
 q("Quel est le rôle principal de la BCE ?", ["Financer le budget de l'État", "Assurer la stabilité des prix", "Fixer les salaires", "Contrôler les entreprises"], 1, "La BCE mène la politique monétaire de la zone euro ; son objectif premier est la stabilité des prix (inflation proche de 2 %)."),
 q("Que désigne M1 ?", ["Les billets uniquement", "La monnaie fiduciaire et les dépôts à vue", "Les obligations", "L'or"], 1, "M1 est l'agrégat monétaire le plus liquide : billets, pièces et dépôts à vue."),
 q("Quel terme désigne le fait que la monnaie soit créée par le crédit ?", ["Monnaie exogène", "Monnaie endogène", "Monnaie fiduciaire", "Monnaie-marchandise"], 1, "La monnaie endogène est créée à l'intérieur du système économique par les banques, en réponse à la demande de crédit."),
 t("Quelles sont les trois fonctions de la monnaie ?", "Intermédiaire des échanges, unité de compte et réserve de valeur.", "Ces trois fonctions sont complémentaires : la monnaie permet de payer, de comparer les valeurs et de conserver le pouvoir d'achat."),
 t("Comment la création monétaire par le crédit fonctionne-t-elle ?", "L'octroi d'un crédit crée une créance pour la banque et, en contrepartie, un dépôt utilisable par l'emprunteur.", "Le bilan de la banque s'allonge des deux côtés : la monnaie est avant tout une écriture comptable, dont la circulation dépend de la confiance et de la réglementation."),
 t("Pourquoi la stabilité des prix est-elle un objectif de la banque centrale ?", "Parce qu'une inflation forte ou une déflation perturbent les décisions économiques et la redistribution des richesses.", "Une inflation maîtrisée préserve le pouvoir d'achat et la lisibilité des prix relatifs, ce qui favorise l'investissement et la croissance.")
])),

F.append(f(["1re"], "SES", "Chapitre : Opinion publique, sondages et démocratie d'opinion", SSES1, [
 "Le questionnement « Comment se forme et s'exprime l'opinion publique ? » appartient au champ sociologie et science politique du programme de première.",
 "L'opinion publique naît avec la démocratie et l'imprimerie : d'abord réservée aux catégories éclairées (salons, cafés, presse), elle est aujourd'hui comprise comme l'opinion du plus grand nombre.",
 "Un sondage d'opinion repose sur un échantillon représentatif de la population, tiré au hasard et éventuellement pondéré selon des quotas (âge, sexe, catégorie socioprofessionnelle).",
 "La marge d'erreur dépend de la taille de l'échantillon : pour n = 1000, elle est d'environ ±3 points à 95 % de confiance ; elle ne mesure pas les biais de formulation ou de non-réponse.",
 "Les techniques de recueil (face-à-face, téléphone, en ligne) et la formulation des questions influencent les résultats : un sondage est une construction, pas un simple reflet.",
 "Le recours fréquent aux sondages modifie la vie politique : on parle de « démocratie d'opinion », où les gouvernants tiennent compte des enquêtes dans leur communication et leurs décisions.",
 "Les médias et les réseaux sociaux jouent un rôle d'agenda setting : ils ne disent pas seulement quoi penser, mais sur quoi penser.",
 "La sociologie de l'opinion (Gabriel Tarde, Pierre Bourdieu) souligne l'existence de publics différenciés et de rapports de force dans la production de l'opinion.",
 "Les sondages peuvent avoir des effets stratégiques : effet bandwagon (ralliement au candidat annoncé gagnant) ou effet underdog (soutien au candidat annoncé perdant).",
 "L'enjeu démocratique est de distinguer l'opinion publique, légitime dans une démocratie, de l'opinion mesurée, qui peut être instrumentalisée."
], [
 q("Quelle condition doit remplir un échantillon pour rendre un sondage fiable ?", ["Être représentatif de la population", "Être composé de bénévoles", "Contenir au moins 100 000 personnes", "Être choisi par le commanditaire"], 0, "Un échantillon doit être tiré au hasard et structuré selon les caractéristiques de la population étudiée."),
 q("Qu'est-ce que la démocratie d'opinion ?", ["Un régime où les sondages et l'opinion influencent fortement les gouvernants", "Une démocratie sans élections", "Un régime autoritaire", "Une assemblée de citoyens tirés au sort"], 0, "Le terme désigne une transformation de la démocratie représentative, entre contrôle des citoyens et communication politique."),
 q("Quel est l'ordre de grandeur de la marge d'erreur pour un échantillon de 1000 personnes ?", ["± 0,1 point", "± 3 points", "± 15 points", "± 30 points"], 1, "Pour n = 1000 et une proportion proche de 50 %, la marge d'erreur à 95 % est d'environ 3 points."),
 q("Qu'appelle-t-on « agenda setting » ?", ["Le fait de fixer les sujets dont on parle", "Une technique de tirage au sort", "Un type de sondage", "Une loi électorale"], 0, "Les médias exercent un pouvoir d'agenda en sélectionnant les thèmes qui deviennent des objets de débat public."),
 q("Quel est l'effet « bandwagon » ?", ["Le ralliement vers le candidat annoncé gagnant", "Le rejet des sondages", "Une erreur d'échantillonnage", "Une grève de la presse"], 0, "L'effet bandwagon (« effet train en marche ») décrit le soutien croissant à celui qui est présenté comme le futur vainqueur."),
 t("Pourquoi la formulation d'une question peut-elle biaiser un sondage ?", "Parce que les mots employés orientent la réponse et activent des associations différentes.", "Une question chargée émotionnellement ou suggérant une réponse socialement attendue produit un résultat qui ne reflète pas une opinion stable."),
 t("Comment l'opinion publique s'est-elle transformée avec les médias ?", "Elle est devenue plus large, plus rapide et plus médiatisée, mais aussi plus fragmentée.", "De la presse écrite aux réseaux sociaux, les publics se sont diversifiés : l'opinion n'est plus un bloc mais une multiplicité de courants mesurés et commentés."),
 t("Quel est le risque d'une « démocratie d'opinion » ?", "Que la décision politique suive les sondages plutôt qu'un projet réfléchi et durable.", "Le programme SES invite à analyser la tension entre la légitimité de l'opinion et la nécessaire autonomie du débat démocratique.")
])),

F.append(f(["1re"], "SES", "Chapitre : Comment se forment les prix sur un marché concurrentiel ?", SSES1, [
 "Le programme de première pose la question « Comment se forment les prix sur un marché ? » et étudie le fonctionnement du marché concurrentiel.",
 "Un marché met en relation une offre (les producteurs) et une demande (les consommateurs) pour un bien ou un service, par l'intermédiaire du prix.",
 "La loi de la demande énonce que, toutes choses égales par ailleurs, une hausse du prix entraîne une baisse de la quantité demandée : la courbe de demande est décroissante.",
 "La loi de l'offre énonce qu'une hausse du prix entraîne une hausse de la quantité offerte : la courbe d'offre est croissante.",
 "Le prix d'équilibre est celui pour lequel la quantité offerte égale la quantité demandée : le marché s'y stabilise en l'absence de contraintes.",
 "Si le prix est supérieur à l'équilibre, il y a excédent d'offre : les vendeurs baissent leurs prix. S'il est inférieur, il y a excédent de demande : les prix montent.",
 "Le modèle de concurrence pure et parfaite repose sur cinq hypothèses : atomicité, homogénéité du produit, libre entrée et sortie, transparence de l'information et libre circulation des facteurs.",
 "Une hausse de la demande (déplacement de la courbe) augmente le prix et la quantité d'équilibre ; une hausse de l'offre les modifie en sens contraire pour le prix.",
 "L'élasticité-prix de la demande mesure la sensibilité de la quantité demandée à une variation de prix : elle est forte pour les biens de luxe et faible pour les biens de première nécessité.",
 "Le modèle est un outil d'analyse : il simplifie la réalité et doit être complété par l'étude des défaillances du marché (monopole, externalités, biens publics)."
], [
 q("Que se passe-t-il quand le prix est supérieur au prix d'équilibre ?", ["Excédent de demande", "Excédent d'offre", "Le marché est à l'équilibre", "Les prix augmentent"], 1, "À un prix trop élevé, l'offre dépasse la demande : les vendeurs sont incités à baisser leurs prix pour écouler leurs stocks."),
 q("Quelle est la forme de la courbe de demande ?", ["Croissante", "Décroissante", "Horizontale", "Verticale"], 1, "La demande est décroissante : plus le prix augmente, moins les consommateurs achètent (toutes choses égales par ailleurs)."),
 q("Quelle hypothèse ne fait pas partie de la concurrence pure et parfaite ?", ["Atomicité", "Homogénéité du produit", "Transparence de l'information", "Présence d'un monopole"], 3, "Le monopole est l'opposé de la concurrence : les cinq hypothèses excluent toute position dominante."),
 q("Quel bien a généralement une demande peu élastique ?", ["Un bien de luxe", "Un médicament indispensable", "Une voiture de sport", "Un voyage"], 1, "Un bien nécessaire voit sa demande peu varier quand son prix change : son élasticité est faible."),
 q("Que désigne le prix d'équilibre ?", ["Le prix fixé par l'État", "Le prix où offre et demande s'égalent", "Le prix le plus bas possible", "Le prix moyen des concurrents"], 1, "C'est le prix auquel les quantités offertes et demandées sont égales : le marché s'y stabilise spontanément."),
 t("Comment le marché concurrentiel tend-il vers l'équilibre ?", "Les excédents d'offre ou de demande incitent les agents à modifier les prix jusqu'à l'égalisation.", "Le mécanisme des prix est une boucle de rétroaction : un déséquilibre crée une pression à la hausse ou à la baisse qui ramène vers l'équilibre."),
 t("Quelle est la différence entre un mouvement le long de la courbe et un déplacement de la courbe ?", "Le premier résulte d'une variation du prix ; le second d'une variation d'un autre facteur (revenu, goûts, coûts).", "Une hausse du prix fait varier la quantité demandée sur la même courbe ; une hausse du revenu déplace toute la courbe de demande."),
 t("Pourquoi le modèle de concurrence parfaite est-il un outil et non une description exacte ?", "Parce qu'il repose sur des hypothèses idéalisées rarement réunies dans la réalité.", "Il sert de référence pour mesurer les écarts (pouvoirs de marché, asymétries d'information) et analyser les défaillances.")
])),

F.append(f(["Terminale"], "SES", "Chapitre : Croissance économique, productivité et progrès technique", SSES2, [
 "Le programme de terminale comprend le questionnement « Qu'est-ce qui explique la croissance économique ? » et mobilise les modèles de croissance.",
 "La croissance économique est l'augmentation durable de la production de biens et services d'un pays, mesurée par le taux de variation annuel du PIB réel (corrigé de l'inflation).",
 "Le PIB (produit intérieur brut) additionne les valeurs ajoutées des unités résidentes ; on le mesure par la production, les revenus ou les dépenses.",
 "La croissance peut être extensive (augmentation des facteurs de production : travail et capital) ou intensive (gains de productivité globale des facteurs).",
 "La productivité globale des facteurs (PGF) mesure l'efficacité avec laquelle le travail et le capital sont combinés : elle est liée au progrès technique.",
 "Le modèle de Solow (1956) montre que l'accumulation du capital seule ne peut entretenir la croissance par habitant à long terme : seul le progrès technique le permet (état stationnaire).",
 "Les économistes de la croissance endogène (Romer, Lucas, Aghion) soulignent le rôle de la recherche-développement, du capital humain et des infrastructures dans l'innovation.",
 "Les « trente glorieuses » (1945-1975) illustrent une croissance forte et partagée dans les pays développés, suivie d'un ralentissement et de crises (1973, 2008, 2020).",
 "La croissance a des effets ambivalents : elle améliore les niveaux de vie mais peut s'accompagner de pollutions, d'inégalités et d'épuisement des ressources.",
 "Les débats contemporains portent sur la « croissance verte », la sobriété et la dissociation entre croissance du PIB et impacts environnementaux."
], [
 q("Comment mesure-t-on la croissance économique ?", ["Par le taux de variation du PIB réel", "Par le taux de chômage", "Par le taux d'inflation", "Par la balance commerciale"], 0, "La croissance est la variation annuelle du PIB en volume, c'est-à-dire corrigé de l'inflation."),
 q("Quel économiste a proposé un modèle de croissance néoclassique en 1956 ?", ["Keynes", "Solow", "Smith", "Marx"], 1, "Robert Solow publie son modèle en 1956 : le capital seul ne suffit pas à expliquer la croissance par habitant à long terme."),
 q("Que désigne la productivité globale des facteurs ?", ["Le nombre de travailleurs", "L'efficacité de la combinaison travail-capital", "Le salaire moyen", "Le stock de capital"], 1, "La PGF mesure la part de la production qui ne s'explique pas par la seule augmentation du travail et du capital : elle traduit le progrès technique."),
 q("Quelle période correspond aux « Trente Glorieuses » en France ?", ["1919-1939", "1945-1975", "1980-2000", "2000-2020"], 1, "Les Trente Glorieuses désignent la période de forte croissance et de transformation sociale de 1945 à 1975."),
 q("Selon la croissance endogène, quel facteur est central ?", ["Le hasard", "La recherche et le capital humain", "La monnaie", "Le protectionnisme"], 1, "Romer, Lucas et Aghion montrent que l'innovation, la formation et les infrastructures sont des moteurs internes de la croissance."),
 t("Quelle est la différence entre croissance extensive et intensive ?", "La première augmente les facteurs de production ; la seconde améliore leur efficacité.", "La croissance extensive mobilise plus de travail et de capital ; la croissance intensive repose sur la productivité et le progrès technique."),
 t("Pourquoi le modèle de Solow conclut-il à un état stationnaire ?", "Parce que l'accumulation du capital se heurte à la baisse de sa productivité marginale.", "Sans progrès technique, l'investissement finit par ne plus compenser l'usure du capital et l'accroissement de la population : la croissance par habitant s'arrête."),
 t("La croissance suffit-elle à améliorer le bien-être ?", "Non : elle doit être accompagnée d'une répartition équitable et d'une prise en compte des impacts environnementaux.", "Le PIB mesure la production mais ni les inégalités, ni la santé, ni la qualité de l'environnement : d'autres indicateurs sont nécessaires.")
])),

F.append(f(["Terminale"], "SES", "Chapitre : Commerce international et internationalisation de la production", SSES2, [
 "Le questionnement « Quels sont les fondements du commerce international et de l'internationalisation de la production ? » figure au programme de terminale et est évaluable au bac 2027.",
 "La théorie de l'avantage absolu (Adam Smith, Recherches sur la nature et les causes de la richesse des nations, 1776) explique le commerce par la spécialisation dans les biens produits à moindre coût.",
 "La théorie de l'avantage comparatif (David Ricardo, Des principes de l'économie politique et de l'impôt, 1817) montre que l'échange profite même à un pays moins productif dans toutes les productions, à condition de se spécialiser selon ses coûts relatifs.",
 "Ces théories reposent sur des hypothèses fortes (concurrence parfaite, mobilité des facteurs interne, coûts de transport nuls) qui sont discutées par les économistes.",
 "Le commerce international s'est développé avec la baisse des coûts de transport et de communication, la libéralisation tarifaire et la création de l'OMC en 1995.",
 "L'internationalisation de la production se traduit par les chaînes de valeur mondiales : la conception, la fabrication et la commercialisation d'un bien sont réparties entre plusieurs pays.",
 "Les firmes multinationales (FMN) organisent ces réseaux pour tirer parti des coûts, des compétences et des marchés locaux.",
 "Les échanges sont inégaux : les pays développés dominent les flux de biens à forte valeur ajoutée et de services, tandis que d'autres restent spécialisés dans les matières premières.",
 "Le commerce international suscite des débats : gains d'efficacité et baisse des prix d'un côté, pertes d'emplois dans les secteurs exposés et pressions sur les normes sociales et environnementales de l'autre.",
 "Les politiques commerciales (tarifs douaniers, subventions, accords régionaux comme le marché unique européen) visent à concilier ouverture et protection des intérêts nationaux."
], [
 q("Quel économiste a formulé la théorie de l'avantage comparatif ?", ["Adam Smith", "David Ricardo", "Keynes", "Friedman"], 1, "Ricardo publie l'avantage comparatif en 1817 ; Smith avait formulé l'avantage absolu en 1776."),
 q("Qu'est-ce qu'une chaîne de valeur mondiale ?", ["Une organisation de la production répartie dans plusieurs pays", "Un réseau de vente en ligne", "Une autoroute", "Un accord monétaire"], 0, "Les firmes multinationales fragmentent leurs activités pour tirer parti des coûts et des compétences locales, ce qui accroît les échanges de biens intermédiaires."),
 q("Quand l'Organisation mondiale du commerce a-t-elle été créée ?", ["1945", "1957", "1995", "2008"], 2, "L'OMC succède au GATT en 1995 et administre les accords commerciaux multilatéraux."),
 q("Quel est l'avantage d'une spécialisation selon Ricardo ?", ["Chaque pays produit ce qu'il peut vendre moins cher que les autres", "Chaque pays produit ce qu'il fait relativement le mieux", "Tous les pays produisent la même chose", "Le pays le plus productif produit tout"], 1, "L'avantage comparatif repose sur les coûts relatifs, pas absolus : même le pays le moins productif a intérêt à se spécialiser."),
 q("Quel est un effet discuté du commerce international ?", ["La hausse systématique des prix", "Les pertes d'emplois dans les secteurs exposés à la concurrence", "La disparition des firmes multinationales", "La fin des échanges de services"], 1, "Le commerce crée des gagnants et des perdants : les ajustements sectoriels nécessitent des politiques d'accompagnement."),
 t("Comment l'avantage comparatif justifie-t-il le commerce ?", "Même un pays moins productif a intérêt à se spécialiser dans la production où son coût relatif est le plus faible.", "L'échange permet à chaque pays de consommer plus que s'il produisait tout seul : les gains à l'échange reposent sur les différences de coûts relatifs."),
 t("Comment les chaînes de valeur mondiales transforment-elles la production ?", "Elles fragmentent les étapes de fabrication entre plusieurs pays et multiplient les échanges de biens intermédiaires.", "Un produit final incorpore des composants de nombreux pays : le commerce ne porte plus seulement sur des biens finis, mais sur des tâches et des services."),
 t("Quels sont les débats sur l'ouverture commerciale ?", "Elle est accusée de créer des inégalités et des pertes d'emplois, tout en apportant des gains d'efficacité et de pouvoir d'achat.", "Le programme invite à dépasser l'opposition simple entre libre-échange et protectionnisme en évaluant les effets sur l'emploi, les prix, l'innovation et l'environnement.")
])),

F.append(f(["Terminale"], "SES", "Chapitre : Structure de la société française et mobilité sociale", SSES2, [
 "Le programme de terminale étudie « Comment est structurée la société française actuelle ? » et « Quelles sont les caractéristiques contemporaines et les facteurs de la mobilité sociale ? ».",
 "La société française est analysée en groupes socioprofessionnels (PCS) : cadres et professions intellectuelles supérieures, professions intermédiaires, employés, ouvriers, indépendants, retraités.",
 "La stratification sociale se mesure à partir des revenus, du niveau d'éducation, du prestige des professions et du patrimoine : les inégalités restent fortes (10 % les plus riches détiennent près de la moitié du patrimoine).",
 "La mobilité sociale désigne le changement de position sociale d'un individu entre deux générations (mobilité intergénérationnelle) ou au cours de sa vie (mobilité intragénérationnelle).",
 "On distingue la mobilité structurelle, liée à la transformation de la structure des emplois (montée des cadres, déclin des ouvriers), et la mobilité circulaire, qui résulte de l'ouverture des opportunités.",
 "Les tables de contingence croisant la profession du père et celle de l'enfant permettent de mesurer la reproduction et la mobilité sociale.",
 "Le « taux de mobilité » se calcule en comparant la proportion d'enfants ayant une profession différente de celle de leur père à ce que la seule modification de la structure prédirait.",
 "La réussite scolaire est un facteur majeur de mobilité ascendante, mais l'origine sociale influence fortement les parcours et les orientations (Bourdieu et Passeron, La Reproduction, 1970).",
 "La mobilité sociale est aussi genrée : les femmes subissent davantage de plafonds de verre et de temps partiel subi, ce qui freine leur progression.",
 "Les questions contemporaines portent sur la « justice sociale », l'égalité des chances et l'efficacité des politiques éducatives et fiscales."
], [
 q("Quel indicateur sert à mesurer la mobilité sociale intergénérationnelle ?", ["Le tableau de contingence profession père/enfant", "Le taux de chômage", "L'indice de prix", "La balance commerciale"], 0, "Le tableau croisant la profession du père et celle de l'enfant permet de mesurer la reproduction ou la mobilité sociale."),
 q("Qui sont les auteurs de La Reproduction (1970) ?", ["Bourdieu et Passeron", "Durkheim et Weber", "Marx et Engels", "Tarde et Bureau"], 0, "Pierre Bourdieu et Jean-Claude Passeron y analysent le rôle de l'école dans la reproduction des inégalités sociales."),
 q("Qu'appelle-t-on mobilité structurelle ?", ["Le changement de position lié à la transformation de la structure des emplois", "La réussite d'un individu", "Une mutation professionnelle", "Un déménagement"], 0, "La montée en gamme des qualifications et le déclin du nombre d'ouvriers créent mécaniquement des positions nouvelles."),
 q("Quelle catégorie PCS regroupe les ingénieurs et les enseignants ?", ["Cadres et professions intellectuelles supérieures", "Professions intermédiaires", "Employés", "Indépendants"], 0, "La nomenclature PCS place les cadres, ingénieurs, enseignants et professions libérales dans la même catégorie."),
 q("Qu'est-ce qu'un « plafond de verre » ?", ["Une barrière invisible à la progression des femmes", "Un plafond de salaire légal", "Une limite d'âge", "Un type de contrat"], 0, "Le plafond de verre désigne les obstacles informels qui empêchent les femmes d'accéder aux plus hautes responsabilités."),
 t("Quels facteurs expliquent la mobilité sociale ascendante ?", "L'allongement des études, l'ouverture de certaines professions et la croissance économique.", "Le programme souligne le rôle de l'École et de la qualification, mais aussi des inégalités d'accès selon l'origine sociale."),
 t("Comment mesure-t-on la mobilité sociale ?", "En comparant la profession des parents et celle des enfants dans un tableau de contingence.", "On distingue la mobilité observée de la mobilité attendue par la seule évolution de la structure des emplois : leur écart mesure la mobilité circulaire."),
 t("Pourquoi l'égalité des chances reste-t-elle un idéal difficile à atteindre complètement ?", "Parce que les ressources familiales, culturelles et sociales ne sont pas réparties également dès l'enfance.", "Bourdieu montre que l'école, bien qu'elle se donne pour objectif l'égalité, valorise des dispositions acquises dans les milieux favorisés.")
])),

F.append(f(["Terminale"], "SES", "Chapitre : La socialisation, la famille et l'école", SSES2, [
 "Le questionnement « Comment se construit l'identité sociale des individus ? » se rattache au champ sociologie et science politique du programme de terminale.",
 "La socialisation est le processus par lequel l'individu intègre les normes, valeurs et comportements de la société à laquelle il appartient ; elle est primaire (famille) puis secondaire (école, pairs, médias).",
 "Durkheim voit dans la socialisation le fondement de la cohésion sociale : la société façonne l'individu par l'éducation et les représentations collectives.",
 "La famille est une institution qui assure la reproduction biologique et sociale, la socialisation et le soutien affectif ; ses formes se sont diversifiées (famille nucléaire, monoparentale, recomposée, homoparentale).",
 "L'école est une institution centrale de socialisation et de sélection : elle transmet des savoirs, des normes et attribue des qualifications qui déterminent les parcours.",
 "Les sociologues (Bourdieu, Passeron, Baudelot, Establet) montrent que l'école reproduit les inégalités sociales par la sélection et l'orientation.",
 "La socialisation différenciée selon le genre et l'origine sociale produit des dispositions et des aspirations différentes, que les statistiques scolaires confirment.",
 "Les pairs et les médias, en particulier les réseaux sociaux, constituent des instances de socialisation secondaire de plus en plus influentes à l'adolescence.",
 "La notion de « habitus » (Bourdieu) désigne les dispositions durables et transposables acquises par la socialisation, qui orientent les pratiques sans contrainte explicite.",
 "L'enjeu du chapitre est de comprendre comment l'identité sociale est à la fois héritée et construite, et comment les institutions peuvent favoriser ou limiter l'émancipation."
], [
 q("Quel sociologue a introduit la notion d'« habitus » ?", ["Durkheim", "Pierre Bourdieu", "Weber", "Tarde"], 1, "Bourdieu définit l'habitus comme un système de dispositions durables acquises par la socialisation."),
 q("Quelle est la socialisation primaire ?", ["Celle qui a lieu à l'école", "Celle qui a lieu dans la famille durant l'enfance", "Celle des médias", "Celle du travail"], 1, "La socialisation primaire se déroule dans la famille pendant l'enfance ; la socialisation secondaire intervient ensuite dans les autres institutions."),
 q("Quel est le rôle de l'école selon Durkheim ?", ["Inculquer des règles et créer de la cohésion sociale", "Sélectionner uniquement", "Former au travail manuel", "Remplacer la famille"], 0, "Durkheim voit dans l'éducation la transmission des normes collectives, condition de la solidarité sociale."),
 q("Quel est un effet de la socialisation différenciée ?", ["Des aspirations et des parcours différents selon l'origine sociale", "Une identité identique pour tous", "La disparition des inégalités", "L'absence de normes"], 0, "Les ressources familiales et les expériences socialisatrices produisent des dispositions et des ambitions variables."),
 q("Que désigne une famille « recomposée » ?", ["Une famille avec des enfants d'unions précédentes", "Une famille nucléaire", "Une famille monoparentale", "Une famille sans enfant"], 0, "La famille recomposée résulte d'une nouvelle union où au moins un des conjoints a déjà des enfants."),
 t("Quelle est la différence entre socialisation primaire et secondaire ?", "La première a lieu dans la famille et pose les fondements de la personnalité ; la seconde se poursuit dans les autres institutions.", "La socialisation primaire est plus précoce et plus profonde ; la secondaire (école, pairs, médias) vient la compléter ou la transformer."),
 t("Comment l'école peut-elle reproduire les inégalités sociales ?", "En valorisant des codes culturels et des comportements plus familiers aux milieux favorisés.", "Bourdieu et Passeron montrent que la sélection scolaire n'est pas seulement fondée sur le mérite individuel, mais sur des prérequis culturels inégalement répartis."),
 t("Quel est l'apport des pairs à l'adolescence ?", "Ils constituent un groupe de référence où se négocient l'identité et les normes.", "Les pairs offrent un espace d'autonomie par rapport à la famille et jouent un rôle croissant dans la construction de soi, relayés par les réseaux sociaux.")
])),

# ---------------- EPS SPÉCIALITÉ ----------------
F.append(f(["1re"], "EPS (spécialité)", "Chapitre : Construire une prestation motrice – principes d'entraînement et évaluation", SEPS1, [
 "La spécialité EPS de première (6 heures hebdomadaires) approfondit la pratique sportive et l'analyse des activités physiques et sportives.",
 "Une prestation motrice est une réalisation technique dans une situation donnée : elle est évaluée à partir de critères observables (efficacité, maîtrise, adaptation).",
 "L'entraînement repose sur les principes de progressivité (augmenter progressivement la charge), de spécificité (s'entraîner pour la tâche visée) et de récupération.",
 "La séance d'EPS se structure en trois temps : échauffement (mise en train progressive), corps de séance (apprentissage et situations d'opposition ou de coopération), retour au calme.",
 "Les cycles d'apprentissage (3 à 6 semaines) permettent d'observer l'évolution des compétences par des situations de référence répétées en début et en fin de cycle.",
 "Les activités sont classées selon deux logiques : compétition (opposition directe ou indirecte) et coopération (expression, adaptation à l'environnement).",
 "La planification annuelle répartit les activités en cycles et fixe des objectifs de progrès individualisés, en lien avec le livret scolaire et le socle commun.",
 "L'analyse du geste sportif utilise des repères spatiaux, temporels et dynamiques : trajectoire, appuis, transfert de poids, coordination segmentaire.",
 "La vidéo et l'observation entre pairs sont des outils de régulation : elles permettent de comparer la réalisation au modèle et d'ajuster la pratique.",
 "L'évaluation certificative en spécialité combine des épreuves de performance, des situations de match et une épreuve orale sur la connaissance des activités."
], [
 q("Combien de temps dure généralement un cycle d'apprentissage en EPS ?", ["1 semaine", "3 à 6 semaines", "Un trimestre", "Une année"], 1, "Les cycles de 3 à 6 semaines permettent d'observer des progrès mesurables et d'adapter l'enseignement."),
 q("Quel principe d'entraînement consiste à augmenter progressivement la charge ?", ["La spécificité", "La progressivité", "La récupération", "L'intensité"], 1, "La progressivité évite la blessure et permet une adaptation physiologique et technique durable."),
 q("Quelle activité relève d'une opposition indirecte ?", ["Le basketball", "Le tennis de table", "La lutte", "Le rugby"], 1, "Au tennis de table, les joueurs ne sont pas au contact direct mais s'opposent par l'intermédiaire de la balle et du filet."),
 q("Quel est le rôle de la situation de référence ?", ["Mesurer l'évolution des compétences", "Remplacer l'échauffement", "Fixer une note définitive", "Sélectionner les élèves"], 0, "Répétée en début et fin de cycle, elle rend visible le progrès réalisé par chaque élève."),
 q("Quelles sont les trois parties d'une séance d'EPS ?", ["Échauffement, corps de séance, retour au calme", "Arrivée, match, douche", "Course, saut, lancer", "Théorie, pratique, devoir"], 0, "Cette structure garantit la mise en train, l'apprentissage et la récupération."),
 t("Comment évaluer une prestation motrice ?", "À partir de critères observables : efficacité, maîtrise technique et adaptation à la situation.", "L'évaluation s'appuie sur un référentiel de niveaux et sur des situations types, afin d'objectiver les progrès plutôt que de comparer les élèves entre eux."),
 t("Pourquoi la vidéo est-elle utile dans l'apprentissage sportif ?", "Elle permet de revoir le geste, de le comparer au modèle et de corriger les erreurs.", "L'observation différée et l'analyse image par image facilitent la prise de conscience des aspects techniques invisibles pendant l'exécution."),
 t("Quel est l'intérêt de la spécialité EPS ?", "Elle permet d'approfondir la pratique et la connaissance des sports, et d'envisager des poursuites d'études dans le domaine.", "La spécialité (6 h) prépare aux épreuves du bac et aux formations en STAPS, tout en développant une pratique autonome et réfléchie.")
])),

F.append(f(["Terminale"], "EPS (spécialité)", "Chapitre : Corps, santé et pratique sportive responsable", SEPS2, [
 "La spécialité EPS de terminale consolide l'autonomie dans la pratique et la réflexion sur les enjeux de santé et de citoyenneté du sport.",
 "L'effort soutenu entraîne une augmentation de la fréquence cardiaque et de la consommation d'oxygène ; l'entraînement améliore la VO₂max et la récupération.",
 "La VO₂max exprime le volume maximal d'oxygène consommé par minute et par kilogramme de masse corporelle : c'est un indicateur de la condition aérobie.",
 "Les énergies mises en jeu dans l'effort sont l'énergie aérobie (avec oxygène, pour les efforts longs) et l'énergie anaérobie (sans oxygène, pour les efforts brefs et intenses).",
 "La prévention des blessures repose sur l'échauffement, la progression des charges, la technique correcte, l'hydratation et l'adaptation aux conditions (chaleur, froid, qualité de l'air).",
 "Les blessures sportives les plus fréquentes sont les entorses, les tendinites et les fractures de fatigue ; leur prise en charge suit le protocole GREC (glace, repos, élévation, compression).",
 "Le sport de compétition soulève des enjeux éthiques : fair-play, respect des règles, inclusion, lutte contre le dopage et protection des mineurs.",
 "L'impact environnemental des événements sportifs (déplacements, consommation d'énergie, déchets) est désormais un objet d'analyse dans le programme.",
 "L'évaluation de l'EPS au bac compte pour 10 % de la note finale et repose sur le contrôle continu, l'attestation d'aptitude physique et, si nécessaire, un examen supplémentaire.",
 "Les débouchés de la spécialité incluent les formations STAPS, les métiers de l'enseignement, de l'entraînement, de la réadaptation et du sport professionnel."
], [
 q("Quel indicateur mesure la capacité maximale d'utilisation d'oxygène ?", ["La VO₂max", "Le quotient intellectuel", "La masse corporelle", "La tension maximale"], 0, "La VO₂max exprime le volume maximal d'oxygène consommé par minute et par kilogramme : c'est un indicateur de la condition aérobie."),
 q("Quel type d'énergie domine dans un sprint de 100 mètres ?", ["L'énergie aérobie", "L'énergie anaérobie", "L'énergie solaire", "L'énergie potentielle"], 1, "L'effort bref et intense est fourni principalement par la voie anaérobie (phosphagènes et glycolyse)."),
 q("Que signifie le sigle GREC en cas de blessure ?", ["Glace, repos, élévation, compression", "Gymnastique, course, endurance, coordination", "Groupe, règle, effort, concentration", "Général, rapide, efficace, collectif"], 0, "Le protocole GREC est la prise en charge initiale classique d'une entorse ou d'une contusion."),
 q("Quel est le poids de l'EPS dans la note finale du bac général ?", ["5 %", "10 %", "20 %", "40 %"], 1, "L'EPS compte pour 10 % de la note finale du baccalauréat général et technologique, au titre du contrôle continu."),
 q("Quel enjeu éthique est lié au sport de compétition ?", ["Le dopage", "La météo", "Le prix des billets", "La durée des matchs"], 0, "Le dopage, le fair-play, l'inclusion et la protection des mineurs sont des enjeux éthiques étudiés en spécialité EPS."),
 t("Quels réflexes de sécurité sont indispensables avant une séance de sport ?", "S'échauffer, vérifier le matériel, respecter les consignes et adapter l'effort aux conditions.", "Ces gestes limitent les risques de blessure et font partie des savoirs exigés pour adopter une pratique autonome et responsable."),
 t("Comment l'entraînement améliore-t-il la condition physique ?", "En augmentant la VO₂max, la capacité de récupération et l'économie du geste.", "Les adaptations cardiovasculaires et musculaires sont progressives : elles supposent une charge adaptée, de la régularité et du repos."),
 t("Pourquoi l'impact environnemental du sport est-il étudié ?", "Parce que les événements et les déplacements consomment des ressources et produisent des déchets et des émissions.", "La spécialité invite à concilier les bénéfices du sport avec la responsabilité écologique : mobilité, gestion des sites et sobriété des équipements.")
])),

AN.append(a("Sujet type bac – SES : la monnaie et le crédit bancaire", "SES",
 "Sujet type – épreuve de spécialité SES (dissertation, 6 points).\n"
 "Sujet : « La monnaie est-elle créée par les banques ? »\n"
 "Document 1 : bilan simplifié d'une banque : actif = créances sur l'économie (crédits) 800 M€ ; passif = dépôts 750 M€, capitaux propres 50 M€.\n"
 "Document 2 : extrait d'un rapport de la BCE sur la création monétaire et le rôle des taux directeurs.",
 "Corrigé indicatif. Introduction : la monnaie est un bien particulier qui sert d'intermédiaire des échanges, d'unité de compte et de réserve de valeur. Le document 1 montre que les dépôts (monnaie scripturale) apparaissent au passif de la banque en contrepartie des crédits.\n"
 "I. La création monétaire par le crédit : lorsqu'une banque accorde un prêt, elle crée une créance à son actif et un dépôt au passif : la monnaie est endogène (document 1). Le multiplicateur de crédit est encadré par les réserves obligatoires et les règles prudentielles.\n"
 "II. Le rôle de la banque centrale : la BCE ne « distribue » pas directement la monnaie, mais elle oriente sa création via ses taux directeurs et ses opérations de marché (document 2). Elle vise la stabilité des prix (inflation à 2 % à moyen terme).\n"
 "III. Les limites : la création monétaire dépend aussi de la demande de crédit des agents et de la confiance ; une création excessive peut alimenter l'inflation ou des bulles d'actifs, ce que les crises financières ont montré.\n"
 "Conclusion : la monnaie est bien créée par les banques commerciales, mais dans un cadre défini et contrôlé par la banque centrale."))

AN.append(a("Sujet type bac – SES : mobilité sociale et égalité des chances", "SES",
 "Sujet type – épreuve composée de spécialité SES (6 points).\n"
 "Première partie (mobilisation de connaissances) : « Montrez que l'école est un facteur de mobilité sociale tout en participant parfois à la reproduction des inégalités. »\n"
 "Deuxième partie (étude de document) : tableau de contingence croisant la profession du père (ouvriers, employés, cadres) et celle de l'enfant, extrait d'une enquête INSEE.\n"
 "Troisième partie (raisonnement) : « L'allongement des études suffit-il à garantir l'égalité des chances ? »",
 "Corrigé indicatif. Première partie : l'école diplôme et qualifie, ce qui ouvre l'accès à des professions supérieures et favorise la mobilité ascendante. Mais Bourdieu et Passeron (La Reproduction, 1970) montrent qu'elle valorise des codes culturels inégalement acquis : l'orientation et la sélection reproduisent les positions sociales.\n"
 "Deuxième partie : la lecture du tableau de contingence fait apparaître une probabilité plus forte pour les enfants de cadres de devenir cadres que pour les enfants d'ouvriers ; la mobilité est réelle mais inégale selon l'origine. On distinguera mobilité structurelle et mobilité circulaire.\n"
 "Troisième partie : non. L'allongement des études augmente le niveau de qualification moyen, mais les écarts de réussite selon l'origine sociale persistent à chaque étape (orientation, filières, abandon). L'égalité des chances supposerait aussi une égalité de moyens et d'accompagnement dès l'enfance.\n"
 "Conclusion : l'école est à la fois un ascenseur social et un lieu de reproduction : sa capacité à réduire les inégalités dépend des politiques éducatives et sociales qui l'entourent."))

save("lead-general-partie-D.json", F, AN)
print("Partie D:", len(F), "fiches,", len(AN), "annales")
