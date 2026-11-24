# -*- coding: utf-8 -*-
"""Lot B — CEJM : 19 chapitres des 6 thèmes du programme officiel."""
import json, os

OUT = os.path.join(os.path.dirname(__file__), "lead-mco-partie-B.json")
SRC = "Arrêté du 15 février 2018 portant définition du programme et de l'épreuve de culture économique, juridique et managériale du BTS (JORF du 6 mars 2018) ; programme CEJM, 6 thèmes ; code civil, code de commerce, code du travail, règlement RGPD ; annales officielles BTS MCO (mybts.fr, cejm.fr)."

def Q(q, opts, ci, corr):
    return {"type": "qcm", "q": q, "options": opts, "correct": ci, "correction": corr}

def T(q, rep, corr):
    return {"type": "texte", "q": q, "reponse": rep, "correction": corr}

def F(titre, points, questions, annees=None):
    return {"filieres": ["bts-mco"], "annees": annees or ["BTS1", "BTS2"],
            "matiere": "CEJM", "titre": titre, "source": SRC,
            "points": points, "questions": questions}

fiches = []

fiches.append(F("Chapitre 1 — CEJM (thème 1) — Les agents économiques, le marché et les externalités", [
 "Les agents économiques se répartissent en ménages (consommateurs et épargnants), entreprises (productrices), administrations publiques (allocatrices, redistributrices, régulatrices), institutions financières (banques, assurances) et reste du monde.",
 "Chaque agent occupe un rôle multiple : un ménage est à la fois consommateur, épargnant, contribuable et travailleur ; une entreprise est productrice, acheteuse et investisseuse.",
 "Le marché met en relation l'offre et la demande ; le prix est le signal qui coordonne les décisions décentralisées des agents et assure l'allocation des ressources.",
 "La concurrence suppose de nombreux offreurs, des produits homogènes, une libre entrée et une information parfaite ; en situation de monopole ou d'oligopole, le price making remplace le price taking.",
 "Les barrières à l'entrée (brevets, économies d'échelle, coûts de changement, réglementation, contrôle d'un réseau de distribution) protègent les positions acquises et limitent la concurrence.",
 "L'asymétrie d'information naît quand une partie détient des informations que l'autre n'a pas : sélection adverse avant la signature du contrat, aléa moral après.",
 "Une externalité est un effet non marchand d'une activité sur un tiers : positive (recherche, vaccination) ou négative (pollution, bruit), elle conduit à une surproduction ou une sous-production par rapport à l'optimum social.",
 "La correction des externalités passe par la taxation (principe du pollueur-payeur), les subventions, la réglementation ou la création de marchés de quotas.",
 "Les banques et le marché financier assurent l'intermédiation : ils collectent l'épargne, la prêtent aux entreprises et permettent le financement de l'investissement.",
 "Dans l'épreuve E4, une situation d'affaires doit être analysée en identifiant les agents concernés, le type de marché et les défaillances éventuelles du marché avant toute proposition de solution."
], [
 Q("Quel agent économique assure la fonction de redistribution ?", ["L'entreprise", "Le ménage", "L'administration publique", "La banque commerciale"], 2, "Les administrations publiques prélèvent des impôts et redistribuent des prestations et services."),
 Q("Comment appelle-t-on un marché où un seul offreur fixe le prix ?", ["Une concurrence parfaite", "Un monopole", "Un oligopole", "Une monopsonie"], 1, "Dans un monopole, l'offreur est price maker ; dans une monopsonie, c'est l'acheteur qui détient le pouvoir."),
 Q("Quelle situation illustre une externalité négative ?", ["Un brevet déposé par une entreprise", "Une baisse des coûts grâce à la technologie", "Une usine qui pollue une rivière", "Un consommateur qui épargne"], 2, "La pollution est un effet non marchand subi par des tiers, non pris en compte dans le prix."),
 Q("Quelle différence existe-t-il entre sélection adverse et aléa moral ?", ["Elles sont identiques", "La première est avant le contrat, le second après", "La première concerne l'État, le second l'entreprise", "La première est après le contrat, le second avant"], 1, "L'asymétrie d'information ex ante crée la sélection adverse, ex post l'aléa moral."),
 Q("Quel est le rôle principal des intermédiaires financiers ?", ["Fixer les prix de vente", "Collecter l'épargne et financer les investissements", "Produire des biens publics", "Contrôler la concurrence"], 1, "Banques et assurances transforment l'épargne en financement."),
 T("Comment un marché concurrentiel coordonne-t-il les décisions des agents ?", "Le prix constitué par la confrontation de l'offre et de la demande donne à chacun un signal : les producteurs investissent là où le prix est élevé, les consommateurs arbitrent selon leur budget.", "Le prix est le mécanisme de coordination décentralisé : il renseigne sur la rareté relative des biens et oriente les décisions."),
 T("Pourquoi une externalités négative conduit-elle à une surproduction ?", "Parce que le producteur ne supporte pas le coût subi par les tiers ; son coût privé est inférieur au coût social, donc le prix est trop bas et la quantité produite trop élevée.", "La correction suppose d'internaliser le coût externe par une taxe ou une réglementation.")
]))

fiches.append(F("Chapitre 2 — CEJM (thème 1) — La formation et la validité du contrat", [
 "Le contrat est un accord de volontés destiné à produire des effets juridiques ; il est régi par le code civil, notamment les articles 1103 et suivants depuis la réforme du droit des contrats de 2016.",
 "Le principe de liberté contractuelle permet de choisir son cocontractant et le contenu du contrat, dans les limites de l'ordre public et des lois impératives.",
 "La formation du contrat passe par une offre (proposition précise) et une acceptation (adhésion sans réserve) ; le consentement doit être libre, éclairé et non vicié.",
 "Les vices du consentement sont l'erreur, le dol (manœuvre frauduleuse) et la violence ; ils peuvent entraîner la nullité de la convention.",
 "La capacité juridique est requise : les mineurs non émancipés et les majeurs protégés ne peuvent pas contracter librement dans certaines matières.",
 "Un objet certain et licite est indispensable : une convention portant sur une chose interdite ou indéterminée est nulle.",
 "La cause, au sens du code civil, désigne la contrepartie attendue : l'intérêt légitime que chaque partie trouve dans l'échange.",
 "Les contrats d'adhésion (conditions générales de vente) ne sont pas nuls de ce seul fait, mais les clauses abusives sont réputées non écrites dans les contrats conclus avec un consommateur.",
 "Le contrat fait loi entre les parties (article 1103) : il doit être exécuté de bonne foi, mais le juge peut le réviser en cas d'imprévision ou le résoudre en cas de force majeure.",
 "En BTS MCO, la qualification juridique d'une situation précontractuelle (simple document publicitaire ou véritable offre) et la vérification des conditions de validité sont des attentes classiques de l'épreuve E4."
], [
 Q("Quels sont les trois vices du consentement ?", ["L'erreur, le dol, la violence", "L'erreur, le délai, la force", "Le dol, la force majeure, l'imprévision", "La violence, la nullité, l'usage"], 0, "Erreur, dol et violence sont les trois vices du consentement du code civil."),
 Q("Quand y a-t-il acceptation au sens juridique ?", ["Quand on reçoit un devis", "Quand on adhère sans réserve à une offre précise", "Quand on négocie le prix", "Quand on signe un simple reçu"], 1, "L'acceptation doit être une adhésion sans réserve à l'offre."),
 Q("Une clause abusive dans un contrat de consommation est…", ["Toujours valable", "Réputée non écrite", "Nulle avec effet rétroactif total", "Sans conséquence"], 1, "Le code de la consommation frappe de nullité les clauses abusives : elles sont réputées non écrites."),
 Q("Que signifie « le contrat fait loi entre les parties » ?", ["Le juge ne peut jamais intervenir", "Les parties doivent exécuter ce qu'elles ont convenu", "L'État fixe le contenu du contrat", "Le contrat est always écrit"], 1, "L'article 1103 du code civil consacre la force obligatoire du contrat, sous réserve des correctifs prévus par la loi."),
 T("Comment qualifier une offre commerciale plutôt qu'une simple publicité ?", "L'offre doit être précise sur les caractéristiques essentielles et manifester la volonté d'être liée ; une publicité générale ne crée pas d'obligation contractuelle.", "La distinction est classique en droit commercial : seules les propositions suffisamment déterminées valent offre."),
 T("Dans quels cas le juge peut-il adapter ou résoudre un contrat ?", "En cas d'imprévision (événement imprévisible, inévitable, rendant l'exécution excessivement onéreuse) ou de force majeure (impossibilité définitive d'exécuter).", "La force majeure entraîne la résolution ; l'imprévision permet une révision judiciaire du contrat.")
]))

fiches.append(F("Chapitre 3 — CEJM (thème 1) — Finalités de l'entreprise, parties prenantes et performance", [
 "L'entreprise poursuit des finalités économiques (création de valeur, profit, pérennité) mais aussi sociales, environnementales et sociétales ; cette plurifonctionnalité est au cœur de la RSE.",
 "Les parties prenantes (stakeholders) sont tous les individus ou groupes affectés par l'activité ou capables de l'influencer : salariés, clients, fournisseurs, actionnaires, collectivités, associations, concurrents.",
 "Les parties prenantes primaires sont liées par une transaction directe à l'entreprise ; les secondaires exercent une influence indirecte (opinion publique, ONG, médias).",
 "La logique entrepreneuriale repose sur l'innovation, la prise de risque et la création de nouvelles combinaisons de ressources (Schumpeter) ; la logique managériale vise l'efficacité dans la gestion de l'existant.",
 "Le manager doit composer avec ces deux logiques : explorer de nouvelles opportunités tout en exploitant les ressources actuelles.",
 "La performance est multidimensionnelle : rentabilité (résultat, marges), productivité, qualité, satisfaction client, engagement des salariés et impact environnemental.",
 "Les indicateurs de performance permettent de piloter : chiffre d'affaires, taux de marge, taux de rotation des stocks, NPS, taux d'absentéisme, empreinte carbone.",
 "La création de valeur partagée consiste à concilier l'intérêt de l'entreprise et celui de la société, au-delà de la simple redistribution du profit.",
 "Le conflit d'agence oppose dirigeants et actionnaires : la séparation entre propriété et gestion peut conduire à des objectifs divergents (taille, prestige, rémunération).",
 "Dans une réponse d'épreuve E4, il faut identifier les parties prenantes concernées par une décision et expliquer comment leurs intérêts s'opposent ou convergent."
], [
 Q("Quel économiste a lié entrepreneuriat et destruction créatrice ?", ["Keynes", "Schumpeter", "Smith", "Ricardo"], 1, "Schumpeter fait de l'innovation et de la destruction créatrice le moteur du capitalisme."),
 Q("Qui est une partie prenante secondaire ?", ["Un fournisseur", "Un client", "Une association de défense de l'environnement", "Un salarié"], 2, "L'ONG agit par influence indirecte, sans transaction directe avec l'entreprise."),
 Q("Quel indicateur mesure la satisfaction client ?", ["Le taux de rotation", "Le NPS", "Le BFR", "Le résultat net"], 1, "Le Net Promoter Score mesure la propension des clients à recommander l'entreprise."),
 Q("Quelle est la différence entre logique entrepreneuriale et logique managériale ?", ["Aucune", "L'une innove et prend des risques, l'autre gère l'existant avec efficacité", "L'une concerne les grandes entreprises, l'autre les petites", "L'une est publique, l'autre privée"], 1, "L'entrepreneuriat explore, le management exploite et optimise."),
 T("Comment définir une partie prenante ?", "Toute personne ou tout groupe qui affecte l'activité de l'entreprise ou en est affecté, directement ou indirectement.", "La définition de Freeman est classique : stakeholder = tout individu ou groupe influençant ou influencé par l'entreprise."),
 T("Pourquoi la performance ne se limite-t-elle pas au profit ?", "Parce que la pérennité de l'entreprise dépend aussi de la satisfaction des clients, de l'engagement des salariés, de la qualité des relations avec les partenaires et de son impact sociétal.", "Une entreprise peut être profitable à court terme et fragile à long terme si elle dégrade ses relations avec ses parties prenantes.")
]))

fiches.append(F("Chapitre 4 — CEJM (thème 2) — Le rôle de l'État dans la régulation économique", [
 "L'État remplit trois fonctions économiques classiques (Musgrave) : allocation des ressources, redistribution des richesses et régulation/stabilisation de l'activité.",
 "La croissance économique se mesure par le taux de variation annuel du PIB en volume ; le PIB par habitant permet de tenir compte de la démographie.",
 "L'inflation est une hausse généralisée et durable des prix ; elle érode le pouvoir d'achat et rend les prévisions économiques plus difficiles.",
 "Le chômage se mesure au sens du BIT : chômeurs / population active ; on distingue chômage conjoncturel, structurel, frictionnel et saisonnier.",
 "Les politiques conjoncturelles (budgétaire et monétaire) visent à stabiliser l'activité à court terme : relance par la dépense publique ou baisse des taux, restrictive en cas de surchauffe.",
 "Les politiques structurelles agissent sur les fondamentaux : formation, innovation, concurrence, marché du travail, fiscalité, infrastructure.",
 "Les stabilisateurs automatiques (impôts progressifs, allocations chômage) amortissent les fluctuations sans nouvelle décision politique.",
 "La régulation européenne (politique monétaire de la BCE, coordination budgétaire, marché unique) limite la marge de manœuvre nationale.",
 "Les limites de l'intervention publique sont connues : défaillance de l'État, effet d'éviction, coût de la dette publique, difficulté à évaluer les politiques.",
 "Dans l'analyse d'une situation, il faut distinguer le diagnostic (inflation, chômage, croissance) de l'instrument de politique mobilisé et de ses effets attendus sur l'entreprise."
], [
 Q("Comment mesure-t-on le chômage au sens du BIT ?", ["Chômeurs / population totale", "Chômeurs / population active", "Chômeurs / salariés", "Chômeurs / PIB"], 1, "La population active comprend les personnes employées et les chômeurs disponibles et en recherche active."),
 Q("Quelle politique vise à relancer la demande à court terme ?", ["Une politique structurelle", "Une politique budgétaire expansive", "Une politique de formation", "Une dérégulation du marché du travail"], 1, "L'augmentation des dépenses publiques ou la baisse des impôts soutient la demande globale."),
 Q("Quelle est une limite de l'intervention de l'État ?", ["L'absence de dette publique", "L'effet d'éviction et la défaillance de l'État", "La stabilité des prix garantie", "La croissance automatique"], 1, "L'intervention publique peut évincer l'investissement privé et n'est pas toujours efficace."),
 Q("Que désigne le PIB en volume ?", ["Le PIB courant", "Le PIB corrigé de l'inflation", "Le PIB par habitant", "Le PIB nominal"], 1, "Le PIB en volume est déflaté : il mesure la croissance réelle."),
 T("Quelle différence entre politique conjoncturelle et politique structurelle ?", "La première agit à court terme sur la demande globale ; la seconde modifie en profondeur l'offre et les conditions de production (formation, innovation, concurrence).", "Un plan de relance conjoncturel soutient la demande ; une réforme de la formation professionnelle agit sur le potentiel de croissance."),
 T("Comment l'inflation affecte-t-elle la décision d'investissement ?", "Elle augmente l'incertitude sur les coûts futurs, complique l'actualisation des flux et peut conduire à exiger un taux de rentabilité plus élevé.", "Une inflation élevée et imprévisible réduit la visibilité sur les cash-flows futurs et renchérit le coût du capital.")
]))

fiches.append(F("Chapitre 5 — CEJM (thème 2) — Droit de la concurrence et propriété industrielle", [
 "Le droit de la concurrence vise à préserver un processus concurrentiel loyal ; il est encadré par le code de commerce et le droit de l'Union européenne.",
 "L'Autorité de la concurrence est une autorité administrative indépendante : elle instruit les pratiques anticoncurrentielles, peut prononcer des sanctions et rend des avis.",
 "Les pratiques anticoncurrentielles sont les ententes (accords entre concurrents sur prix, marchés, production) et les abus de position dominante (prix prédatoires, refus de vente, discrimination, ventes liées).",
 "Les concentrations (fusions, acquisitions) peuvent être contrôlées : l'Autorité vérifie qu'elles ne portent pas atteinte à la concurrence durablement.",
 "La publicité mensongère et la publicité comparative sont réglementées : la seconde est licite si elle est objective, vérifiable et non dénigrante.",
 "Les pratiques commerciales trompeuses et les ventes avec prime font l'objet d'un encadrement précis au bénéfice du consommateur.",
 "La propriété industrielle protège les créations : le brevet protège une invention technique (20 ans) sous réserve de nouveauté, d'activité inventive et d'application industrielle.",
 "La marque protège un signe distinctif (10 ans renouvelables) : elle peut être déposée à l'INPI et donne un droit d'opposition.",
 "Le design, les modèles et les indications géographiques (AOP, IGP) complètent le dispositif de protection.",
 "La contrefaçon expose son auteur à des sanctions civiles (dommages-intérêts, saisie) et pénales ; l'entreprise doit surveiller et défendre ses actifs immatériels."
], [
 Q("Quelle autorité contrôle les pratiques anticoncurrentielles en France ?", ["La CNIL", "L'Autorité de la concurrence", "L'AMF", "Le Conseil d'État"], 1, "L'Autorité de la concurrence est l'autorité administrative indépendante compétente."),
 Q("Quelle pratique constitue une entente ?", ["Un concurrent baisse ses prix", "Deux concurrents s'accordent sur un prix de vente", "Une entreprise innove", "Un distributeur organise une promotion"], 1, "L'entente est un accord entre concurrents qui restreint le jeu de la concurrence."),
 Q("Quelle durée de protection un brevet confère-t-il en principe ?", ["10 ans", "20 ans", "50 ans", "Illimitée"], 1, "Le brevet est délivré pour 20 ans ; la marque pour 10 ans renouvelables."),
 Q("Quand une publicité comparative est-elle licite ?", ["Quand elle dénigre le concurrent", "Quand elle est objective, vérifiable et non dénigrante", "Quand elle est gratuite", "Quand elle cite un prix approximatif"], 1, "La comparaison doit porter sur des éléments objectifs et vérifiables sans dénigrement."),
 T("Quelle différence entre entente et abus de position dominante ?", "L'entente résulte d'un accord entre plusieurs entreprises ; l'abus de position dominante est le comportement unilatéral d'une entreprise puissante sur un marché.", "Les deux pratiques sont interdites mais mettent en cause des comportements différents."),
 T("Pourquoi la marque est-elle un actif stratégique ?", "Elle distingue l'offre de l'entreprise, fidélise la clientèle, facilite l'extension de gamme et peut être valorisée ou cédée.", "La marque est un actif immatériel protégé par le droit, qui contribue à la valeur de l'entreprise.")
]))

fiches.append(F("Chapitre 6 — CEJM (thème 2) — PESTEL, innovation et connaissance de l'environnement", [
 "Le macro-environnement désigne les facteurs généraux qui affectent toutes les entreprises : Politique, Économique, Socioculturel, Technologique, Écologique et Légal (PESTEL).",
 "Le facteur politique comprend la stabilité institutionnelle, la fiscalité et les orientations de politique économique ; le facteur légal recouvre les lois et réglementations contraignantes.",
 "Le facteur économique intègre la croissance, l'inflation, les taux d'intérêt, le chômage et le pouvoir d'achat, qui influencent directement la demande.",
 "Le facteur socioculturel porte sur les valeurs, les modes de consommation, la démographie et les attentes en matière d'éthique ou de bien-être.",
 "Le facteur technologique couvre l'innovation, la digitalisation, l'automatisation et l'obsolescence des technologies.",
 "Le facteur écologique intègre la raréfaction des ressources, le climat, les normes environnementales et les attentes en matière de développement durable.",
 "L'analyse PESTEL est dynamique : les facteurs évoluent et doivent être surveillés par une veille régulière pour anticiper les opportunités et les menaces.",
 "L'innovation est un moteur de compétitivité : innovation de produit, de procédé, de marketing ou d'organisation (classification d'Oslo).",
 "La connaissance de l'environnement alimente le diagnostic stratégique : elle permet de comprendre les opportunités offertes par un nouveau modèle économique ou les risques pesant sur l'activité.",
 "Dans une étude de cas CEJM, il faut sélectionner les facteurs pertinents pour l'entreprise étudiée et expliquer leur impact, plutôt que de reciter la liste PESTEL de manière mécanique."
], [
 Q("Que signifie la lettre S dans PESTEL ?", ["Social", "Socioculturel", "Sécuritaire", "Stratégique"], 1, "PESTEL = Politique, Économique, Socioculturel, Technologique, Écologique, Légal."),
 Q("Quel facteur concerne le climat et les normes environnementales ?", ["Politique", "Économique", "Écologique", "Légal uniquement"], 2, "Le facteur Écologique recouvre les enjeux environnementaux et la raréfaction des ressources."),
 Q("Quelle innovation concerne la manière de produire ?", ["Innovation de produit", "Innovation de procédé", "Innovation marketing", "Innovation financière"], 1, "L'innovation de procédé modifie les méthodes de production ou de distribution."),
 Q("Quel est le principal intérêt de la veille environnementale ?", ["Réduire les impôts", "Anticiper opportunités et menaces", "Remplacer le diagnostic interne", "Garantir le profit"], 1, "La veille permet d'anticiper les évolutions et d'adapter la stratégie."),
 T("Comment utiliser le PESTEL dans une étude de cas ?", "On sélectionne les facteurs qui ont un impact direct sur l'entreprise, on explique leur effet (opportunité ou menace) et on en déduit des consequences pour la décision à prendre.", "Une liste exhaustive non analysée n'est pas une analyse : la sélectivité et l'argumentation sont évaluées."),
 T("Pourquoi l'innovation peut-elle être destructrice ?", "Parce qu'elle rend obsolètes des produits, des compétences ou des modèles économiques existants, tout en créant de nouvelles opportunités (destruction créatrice).", "Schumpeter montre que le progrès technologique bouleverse les positions établies et redistribue les parts de marché.")
]))

fiches.append(F("Chapitre 7 — CEJM (thème 3) — Facteurs de production, coûts, productivité et chaîne de valeur", [
 "Les facteurs de production sont le travail et le capital ; leur combinaison dépend de leur coût respectif et de la technologie disponible.",
 "La productivité globale des facteurs mesure l'efficacité de la combinaison : elle augmente quand la production croît plus vite que les facteurs utilisés.",
 "Les gains de productivité permettent de réduire les coûts unitaires ou d'améliorer la qualité ; ils résultent de l'innovation, de l'organisation et de la formation.",
 "Une structure de coûts distingue charges fixes (indépendantes du volume) et charges variables (évoluant avec l'activité) ; cette distinction est essentielle pour le seuil de rentabilité.",
 "Le coût d'achat comprend le prix d'achat et les frais accessoires (transport, douane) ; le coût de revient y ajoute les frais de distribution.",
 "La chaîne de valeur (Porter) décompose l'activité en activités principales (logistique entrante, production, logistique sortante, marketing, service après-vente) et activités de soutien.",
 "L'avantage concurrentiel naît d'une maîtrise des coûts ou d'une différenciation sur des activités créatrices de valeur.",
 "L'impartition (outsourcing) consiste à confier à un prestataire externe une activité previously réalisée en interne ; elle suppose de comparer coût interne et coût externe, mais aussi les risques de dépendance et de perte de compétences.",
 "Le choix « faire ou faire faire » dépend de la stratégie, de la criticité de l'activité, du contrôle qualité et des coûts de transaction.",
 "Dans l'épreuve E4, une décision d'externalisation doit être justifiée par des critères économiques ET stratégiques."
], [
 Q("Quels sont les deux facteurs de production classiques ?", ["Le travail et le capital", "L'argent et le temps", "Le client et le fournisseur", "La technologie et le marketing"], 0, "La théorie économique distingue le facteur travail et le facteur capital."),
 Q("Qui a conceptualisé la chaîne de valeur ?", ["Porter", "Maslow", "Herzberg", "Drucker"], 0, "Michael Porter a publié « Competitive Advantage » en 1985."),
 Q("Une charge variable est une charge qui…", ["Ne change jamais", "Évolue avec le niveau d'activité", "Est toujours plus élevée qu'une charge fixe", "Est supportée uniquement par l'État"], 1, "Les charges variables suivent le volume de production ou de vente."),
 Q("Quel risque majeur de l'impartition ?", ["La baisse des coûts", "La dépendance au prestataire et la perte de compétences", "L'augmentation de la productivité", "La disparition des charges fixes"], 1, "L'externalisation crée un risque stratégique de dépendance et d'érosion du savoir-faire."),
 T("Comment une entreprise obtient-elle un avantage concurrentiel selon Porter ?", "En maîtrisant mieux ses coûts que ses concurrents ou en proposant une offre différenciée que les clients valorisent, sur tout ou partie de la chaîne de valeur.", "Les deux stratégies génériques sont la domination par les coûts et la différenciation."),
 T("Comment raisonner un choix « faire ou faire faire » ?", "On compare le coût complet interne au coût d'externalisation, puis on intègre les critères qualitatifs : contrôle, confidentialité, flexibilité, dépendance et compétences clés.", "Une décision purement financière peut être dangereuse si elle affaiblit une compétence distinctive.")
]))

fiches.append(F("Chapitre 8 — CEJM (thème 3) — Choisir une structure juridique pour l'entreprise", [
 "Le choix de la structure juridique dépend de plusieurs facteurs : nombre d'associés, montant du capital, niveau de responsabilité souhaité, régime fiscal et social, besoins de financement et projet de transmission.",
 "L'entreprise individuelle (EI) est créée par une seule personne, sans capital minimum ; depuis 2016, l'EIRL permet de séparer le patrimoine professionnel du patrimoine personnel.",
 "La micro-entreprise (auto-entreprise) est un régime simplifié de l'EI avec des limites de chiffre d'affaires et un régime micro-fiscal.",
 "L'EURL (entreprise unipersonnelle à responsabilité limitée) est une SARL à un seul associé : la responsabilité est limitée aux apports.",
 "La SARL réunit de 2 à 100 associés ; les parts sociales ne sont pas librement cessibles et les gérants ont un statut social précis.",
 "La SA (société anonyme) exige un capital minimum de 37 000 € ; les actions sont librement négociables et la direction peut être assurée par un conseil d'administration ou un directoire.",
 "La SAS (société par actions simplifiée) offre une grande souplesse statutaire : le président représente la société et les associés organisent librement son fonctionnement.",
 "La SCI, la SNC (responsabilité solidaire et indéfinie des associés) et la SA à conseil de surveillance complètent les formes courantes.",
 "L'économie sociale et solidaire (ESS) comprend coopératives (SCOP), mutuelles, associations et fondations, avec des principes de gouvernance démocratique et de lucrativité limitée.",
 "Le dirigeant doit aussi choisir un régime fiscal (impôt sur le revenu ou impôt sur les sociétés) et un statut social (TNS ou salarié), qui influencent le revenu net et la protection sociale."
], [
 Q("Quel est le capital minimum d'une SA ?", ["1 €", "7 500 €", "37 000 €", "Aucun minimum"], 2, "La SA requiert un capital minimum de 37 000 € ; la SARL n'a pas de minimum légal."),
 Q("Quelle structure correspond à une SARL à un seul associé ?", ["L'EURL", "La SCI", "La SNC", "La SA"], 0, "L'EURL est l'une des formes de SARL unipersonnelle."),
 Q("Quel est un principe de l'économie sociale et solidaire ?", ["Le profit avant tout", "Une gouvernance démocratique et une lucrativité limitée", "L'absence de salariés", "Le capitalisme actionnarial"], 1, "L'ESS repose sur des principes de solidarité, de démocratie et d'utilité sociale."),
 Q("Dans une SNC, les associés ont une responsabilité…", ["Limitée aux apports", "Solidaire et indéfinie", "Nulle", "Assurée par l'État"], 1, "En SNC, les associés répondent indéfiniment et solidairement des dettes sociales."),
 T("Comment choisir entre EI et EURL ?", "L'EI est simple et peu coûteuse mais l'EIRL protège mieux le patrimoine ; l'EURL offre une personnalité juridique distincte et une responsabilité limitée aux apports, avec plus de formalisme.", "Le choix dépend du patrimoine à protéger, du nombre d'associés envisagé, du régime fiscal et des besoins de financement."),
 T("Pourquoi la SAS est-elle appréciée des startups ?", "Parce que son fonctionnement est très souple (statuts libres, président aux pouvoirs étendus) et qu'elle facilite l'entrée d'investisseurs via des actions.", "La souplesse statutaire et la facilité d'évolution du capital expliquent le succès de la SAS.")
]))

fiches.append(F("Chapitre 9 — CEJM (thème 3) — Risques, inexécution et responsabilité", [
 "Un risque est un événement incertain dont la survenance peut affecter l'entreprise ; on distingue risques commerciaux, financiers, sociaux, juridiques, informatiques, sanitaires et environnementaux.",
 "La gestion des risques comporte quatre étapes : identification, évaluation (probabilité × gravité), choix d'un traitement (évitement, réduction, transfert, acceptation) et suivi.",
 "L'inexécution d'une obligation contractuelle peut être totale, partielle, retardée ou défectueuse ; elle engage la responsabilité du débiteur.",
 "La responsabilité contractuelle suppose un contrat valable, une inexécution et un préjudice ; le débiteur peut s'exonérer en cas de force majeure.",
 "La responsabilité extracontractuelle (délictuelle) repose sur l'article 1240 du code civil : tout fait quelconque qui cause à autrui un dommage oblige son auteur à le réparer.",
 "La responsabilité civile vise la réparation du dommage (dommages-intérêts), la responsabilité pénale vise la sanction d'une infraction (amende, emprisonnement).",
 "Une personne morale peut être pénalement responsable d'infractions commises pour son compte ; la responsabilité du dirigeant peut aussi être engagée pour faute de gestion.",
 "Les clauses limitatives ou exonératoires de responsabilité sont encadrées : elles sont nulles en cas de dol, de faute lourde ou dans les contrats de consommation.",
 "Les moyens de couverture sont l'assurance, la provision, la garantie contractuelle, la diversification et les procédures de contrôle interne.",
 "En situation d'examen, il faut qualifier le risque, identifier la nature de la responsabilité encourue et proposer une mesure de prévention ou de couverture adaptée."
], [
 Q("Quel article du code civil fonde la responsabilité délictuelle ?", ["L'article 1103", "L'article 1240", "L'article 1231-1", "L'article 1384"], 1, "L'article 1240 pose l'obligation de réparer le dommage causé à autrui par sa faute."),
 Q("Quelle est la différence entre responsabilité civile et pénale ?", ["Aucune", "La civile répare le dommage, la pénale sanctionne l'infraction", "La civile concerne les entreprises", "La pénale est toujours privée"], 1, "La responsabilité civile indemnise la victime ; la responsabilité pénale punit l'auteur de l'infraction."),
 Q("Quand une clause exonératoire de responsabilité est-elle nulle ?", ["Toujours", "En cas de dol ou de faute lourde", "Quand elle est écrite", "Dans les contrats entre professionnels"], 1, "Les clauses exonératoires sont invalidées en cas de dol ou de faute lourde, et sont interdites dans les contrats de consommation."),
 Q("Quelle mesure relève du transfert de risque ?", ["La formation du personnel", "La souscription d'une assurance", "L'inventaire", "La procédure de contrôle"], 1, "L'assurance transfère le risque à un tiers moyennant une prime."),
 T("Comment évalue-t-on un risque ?", "En croisant la probabilité de survenance et la gravité du préjudice potentiel, afin de classer les risques et de prioriser les actions.", "La matrice probabilité/gravité permet de choisir entre évitement, réduction, transfert et acceptation."),
 T("Quand la force majeure exonère-t-elle le débiteur ?", "Lorsque l'événement est imprévisible, inévitable et rend l'exécution impossible ; elle doit être indépendante de la volonté du débiteur.", "L'imprévision, qui rend seulement l'exécution plus coûteuse, n'exonère pas mais peut conduire à une révision.")
]))

fiches.append(F("Chapitre 10 — CEJM (thème 3) — Ressources, coordination, styles de management et RSE", [
 "Les ressources de l'entreprise sont tangibles (capitaux, équipements, stocks) et intangibles (marque, brevets, savoir-faire, données, réputation).",
 "La ressource est stratégique lorsqu'elle est précieuse, rare, difficile à imiter et exploitée par une organisation adaptée (modèle VRIO).",
 "La coordination assure la cohérence des efforts individuels : elle passe par la hiérarchie, les procédures, les objectifs, la culture et les systèmes d'information.",
 "Les mécanismes de contrôle comprennent le contrôle budgétaire, les tableaux de bord, les procédures qualité et l'évaluation individuelle.",
 "Les styles de management de Lewin : autocratique (décision unilatérale), démocratique (participation) et libéral (large autonomie).",
 "Le modèle de Likert oppose système autoritaire paternaliste et système participatif ; le manager doit adapter son style à la situation et à la maturité de l'équipe.",
 "La RSE (responsabilité sociétale des entreprises) intègre les préoccupations sociales, environnementales et économiques dans la stratégie, selon la norme ISO 26000.",
 "Les dimensions de la RSE incluent la gouvernance, les droits de l'homme, les relations et conditions de travail, l'environnement, la loyauté des pratiques, les questions de consommation et le développement local.",
 "L'éthique et la déontologie complètent le cadre juridique : elles guident les décisions quand la loi ne prévoit pas tout, notamment en matière de conflits d'intérêts et de discrimination.",
 "Dans une situation managériale, on articule ressources disponibles, mode de coordination et responsabilité éthique pour proposer une décision soutenable."
], [
 Q("Quel modèle évalue une ressource selon quatre critères VRIO ?", ["Porter", "Barney", "Maslow", "Lewin"], 1, "Le cadre VRIO (Value, Rarity, Imitability, Organization) est associé à Jay Barney."),
 Q("Quel style de management implique une décision unilatérale ?", ["Démocratique", "Libéral", "Autocratique", "Participatif"], 2, "Le style autocratique centralise la décision et la communication descendante."),
 Q("Quelle norme internationale cadre la RSE ?", ["ISO 9001", "ISO 26000", "ISO 27001", "ISO 14001"], 1, "L'ISO 26000 donne des lignes directrices relatives à la responsabilité sociétale."),
 Q("Quelle ressource est immatérielle ?", ["Une machine", "Un stock", "Une marque", "Un bâtiment"], 2, "La marque, le savoir-faire et les données sont des actifs immatériels."),
 T("Pourquoi une ressource rare et précieuse n'est-elle pas nécessairement un avantage durable ?", "Si elle est facile à imiter ou si l'organisation ne sait pas l'exploiter, l'avantage est temporaire : le cadre VRIO exige les quatre conditions.", "L'avantage concurrentiel durable suppose valeur, rareté, inimitabilité et organisation adaptée."),
 T("Comment un manager peut-il concilier performance et RSE ?", "En intégrant les enjeux sociaux et environnementaux dans les décisions courantes (achats, staffing, animation) et en mesurant leur impact avec des indicateurs adaptés.", "La RSE n'est pas un surplus : elle peut réduire les risques, renforcer l'image et motiver les équipes.")
]))

fiches.append(F("Chapitre 11 — CEJM (thème 3) — Financement de l'entreprise : cycles, bilan et équilibre financier", [
 "Le cycle d'exploitation décrit la succession achats → stockage → vente → encaissement ; le cycle d'investissement concerne les immobilisations durables.",
 "Le besoin en fonds de roulement (BFR) correspond au montant des ressources immobilisées par le cycle d'exploitation : BFR = actif circulant d'exploitation − dettes circulantes d'exploitation.",
 "Un BFR positif signifie que l'entreprise finance temporairement son exploitation ; un BFR négatif (cas de la grande distribution) signifie qu'elle est financée par ses fournisseurs et clients.",
 "Le fonds de roulement net global (FRNG) = ressources stables − emplois stables ; il doit couvrir le BFR pour assurer une trésorerie positive.",
 "Trésorerie nette = FRNG − BFR ; cette équation fondamentale permet de diagnostiquer l'équilibre financier à court terme.",
 "Le compte de résultat enregistre charges et produits par nature ; les soldes intermédiaires de gestion (marge commerciale, valeur ajoutée, EBE, résultat d'exploitation, résultat courant, résultat net) structurent l'analyse.",
 "Le bilan fonctionnel condensé répartit les emplois (stables, circulants) et les ressources (stables, circulantes) pour analyser l'équilibre.",
 "Les financements internes (autofinancement, cession) et externes (emprunt, crédit-bail, subventions, augmentation de capital) répondent à des besoins différents.",
 "Les ratios d'endettement, de liquidité et d'autonomie financière complètent le diagnostic ; un endettement élevé augmente le risque financier.",
 "Dans l'épreuve E4, on articule diagnostic financier et décision : choix d'un mode de financement, capacité de remboursement et impact sur la structure du bilan."
], [
 Q("Comment calcule-t-on la trésorerie nette ?", ["FRNG + BFR", "FRNG − BFR", "BFR − FRNG", "Ressources stables + emplois stables"], 1, "Trésorerie nette = FRNG − BFR."),
 Q("Quel solde intermédiaire de gestion correspond au chiffre d'affaires moins les achats consommés ?", ["L'EBE", "La marge commerciale", "Le résultat net", "La valeur ajoutée"], 1, "La marge commerciale = vente de marchandises − achat de marchandises."),
 Q("Un BFR négatif signifie que…", ["L'entreprise a un problème de trésorerie", "L'exploitation est financée par les fournisseurs et clients", "L'entreprise n'a pas de stock", "Le FRNG est nul"], 1, "C'est le modèle de la grande distribution : les délais fournisseurs dépassent les délais clients."),
 Q("Le crédit-bail est un financement…", ["Interne", "Externe", "Public", "Sans intérêt"], 1, "Le crédit-bail (leasing) est un mode de financement externe de l'investissement."),
 T("Comment diagnostiquer un déséquilibre financier ?", "En comparant le FRNG au BFR : si le FRNG est inférieur au BFR, la trésorerie nette est négative et l'entreprise risque une crise de liquidité.", "On complète par l'analyse des délais de paiement, de la rotation des stocks et des ratios d'endettement."),
 T("Quelle différence entre cycle d'exploitation et cycle d'investissement ?", "Le premier est court et répétitif (achats, ventes, encaissements) ; le second est long et concerne les immobilisations destinées à servir plusieurs exercices.", "Le BFR est lié au cycle d'exploitation, tandis que les immobilisations relèvent du cycle d'investissement.")
]))

fiches.append(F("Chapitre 12 — CEJM (thème 4) — Numérique, plateformes et nouveaux modèles économiques", [
 "Le numérique transforme l'environnement des entreprises : dématérialisation des échanges, désintermédiation, plateformisation et modification des chaînes de valeur.",
 "Une place de marché (marketplace) met en relation offreurs et demandeurs : elle crée de la valeur par la liquidité et la réduction des coûts de recherche.",
 "Les externalités de réseau existent lorsque la valeur d'un service augmente avec le nombre d'utilisateurs : elles expliquent les effets « winner takes all » et les stratégies de subvention d'un côté du marché.",
 "Les modèles économiques numériques incluent l'abonnement, le freemium, la publicité, la commission et l'économie à la demande ( Uber, Deliveroo).",
 "Les relations d'échange se diversifient : B to B, B to C, C to C, B to G et désormais C to B (consommateur créateur de valeur).",
 "Le ROPO (Research Online, Purchase Offline), le showrooming et le webrooming illustrent la complexification du parcours d'achat omnicanal.",
 "Les normes et standards (protocoles, formats, API, interoperability) facilitent la circulation des informations mais créent aussi des dépendances technologiques.",
 "La donnée devient une ressource stratégique : sa collecte, son traitement et sa valorisation alimentent la personnalisation de l'offre et la décision.",
 "Les risques du numérique incluent la cybersécurité, la dépendance aux plateformes, l'opacité des algorithmes et l'impact sur l'emploi.",
 "En CEJM, l'analyse doit montrer comment la transformation numérique modifie à la fois l'environnement concurrentiel, le modèle économique et le management."
], [
 Q("Quel phénomène explique qu'un service gagne en valeur avec le nombre d'utilisateurs ?", ["L'externalité de réseau", "L'économie d'échelle", "La déséconomie", "Le monopole naturel"], 0, "Les externalités de réseau sont au cœur des stratégies de plateforme."),
 Q("Que désigne le modèle freemium ?", ["Un service payant uniquement", "Une version gratuite avec options payantes", "Une vente aux enchères", "Un abonnement professionnel"], 1, "Le freemium propose une offre gratuite et monétise des fonctionnalités avancées."),
 Q("Que signifie showrooming ?", ["Acheter en ligne après avoir vu en magasin", "Voir en magasin puis acheter en ligne", "Acheter en magasin", "Vendre sur une marketplace"], 1, "Le showrooming consist à observer le produit en magasin puis à l'acheter sur internet."),
 Q("Quel est un risque lié aux plateformes ?", ["La baisse du nombre d'utilisateurs", "La dépendance et l'opacité algorithmique", "L'absence de données", "La disparition du numérique"], 1, "Les plateformes peuvent créer une dépendance et contrôler l'accès au marché."),
 T("Comment une marketplace crée-t-elle de la valeur ?", "En réduisant les coûts de recherche et de transaction, en augmentant la liquidité du marché et en facilitant la rencontre entre offre et demande.", "Les effets de réseau et la confiance (notations, avis) sont des leviers clés de la valeur d'une plateforme."),
 T("Comment le numérique modifie-t-il le parcours d'achat ?", "Les canaux s'entremêlent : le client s'informe en ligne, compare, achète en magasin ou en ligne, et attend une continuité de l'expérience et de l'information.", "L'omnicanalité suppose une cohérence des stocks, des prix et de la relation client sur tous les points de contact.")
]))

fiches.append(F("Chapitre 13 — CEJM (thème 4) — Droit du numérique : RGPD, preuve et contrats électroniques", [
 "La CNIL (Commission nationale de l'informatique et des libertés) est l'autorité administrative indépendante chargée de veiller à la protection des données personnelles.",
 "Le RGPD (règlement européen 2016/679, applicable depuis le 25 mai 2018) harmonise la protection des données dans l'Union européenne et renforce les droits des personnes.",
 "Les principes du RGPD : licéité, loyauté, transparence, limitation des finalités, minimisation des données, exactitude, conservation limitée, intégrité et confidentialité, responsabilité (accountability).",
 "La base légale du traitement doit être identifiée : consentement, exécution du contrat, obligation légale, intérêt vital, mission d'intérêt public ou intérêt légitime.",
 "Le consentement doit être libre, éclairé, spécifique et univoque ; il peut être retiré à tout moment ; le consentement n'est pas requis dans tous les cas (intérêt légitime).",
 "Les personnes disposent de droits : accès, rectification, effacement, limitation, portabilité et opposition ; le responsable de traitement doit y répondre dans un délai d'un mois.",
 "Les violations de données doivent être notifiées à la CNIL dans les 72 heures suivant la prise de connaissance, et aux personnes concernées si le risque est élevé.",
 "La preuve électronique est admise : signature électronique, horodatage, journaux d'audit et certificats permettent d'établir l'existence et le contenu d'un contrat.",
 "Le contrat de vente électronique est valable ; le code de la consommation impose des informations précontractuelles et un droit de rétractation de 14 jours pour la vente à distance.",
 "Les actifs immatériels numériques (données, logiciels, bases de données, noms de domaine) nécessitent une protection juridique et technique adaptée."
], [
 Q("Quelle autorité veille à la protection des données personnelles en France ?", ["L'Autorité de la concurrence", "La CNIL", "L'ARCEP", "La CADA"], 1, "La CNIL est l'autorité administrative indépendante compétente en matière d'informatique et de libertés."),
 Q("Depuis quand le RGPD est-il applicable ?", ["25 mai 2018", "1er janvier 2016", "6 janvier 1978", "1er mars 2022"], 0, "Le règlement général sur la protection des données est applicable depuis le 25 mai 2018."),
 Q("Quel délai pour notifier une violation de données à la CNIL ?", ["24 heures", "72 heures", "8 jours", "1 mois"], 1, "La notification doit intervenir dans les 72 heures suivant la connaissance de la violation."),
 Q("Quel droit permet à une personne de récupérer ses données dans un format structuré ?", ["Le droit à l'oubli", "Le droit à la portabilité", "Le droit d'opposition", "Le droit de rectification"], 1, "Le droit à la portabilité est prévu à l'article 20 du RGPD."),
 T("Quand le consentement est-il une base légale adaptée ?", "Lorsque la personne donne librement et explicitement son accord pour une finalité précise, notamment pour la prospection commerciale ou les cookies non essentiels.", "Le consentement n'est pas la seule base légale : l'exécution du contrat ou l'intérêt légitime peuvent aussi fonder un traitement."),
 T("Comment sécuriser juridiquement une vente en ligne ?", "En affichant les mentions légales et conditions générales de vente, en recueillant valablement le consentement, en conservant la preuve de la commande et en prévoyant le droit de rétractation.", "La preuve électronique (logs, accusés de réception, signature) est essentielle en cas de litige.")
]))

fiches.append(F("Chapitre 14 — CEJM (thème 4) — Système d'information et-management : coordination et décision", [
 "Un système d'information (SI) est un ensemble de ressources (données, logiciels, matériels, procédures, personnes) permettant de collecter, traiter, stocker et diffuser l'information.",
 "Le système d'information commercial (SIC) alimente la relation client, la vente, le pilotage et le reporting : CRM, ERP/PGI, outils de BI et tableaux de bord.",
 "Le SI participe à la coordination : il partage les données entre services, standardise les procédures et réduit les asymétries d'information internes.",
 "La spécialisation des tâches, l'intégration des processus et l'action collective sont trois dimensions de l'organisation numérique.",
 "Les modes de Coordination évoluent : coordination hiérarchique, par procédures, par objectifs et par communautés de pratique.",
 "La flexibilité organisationnelle désigne la capacité de l'entreprise à s'adapter rapidement : télétravail, équipes projets, management par objectifs.",
 "La qualité de l'information est déterminante : exactitude, complétude, fraîcheur, pertinence et accessibilité conditionnent la décision.",
 "Le SI doit être sécurisé : contrôle d'accès, sauvegardes, traçabilité, protection contre les cyberattaques, conformité RGPD.",
 "Le manager doit maîtriser les outils numériques pour animer son équipe : plannings partagés, messagerie, visioconférence, espaces collaboratifs et reporting automatisé.",
 "Une décision managériale efficace articule données chiffrées, analyse qualitative et jugement : le SI éclaire la décision sans s'y substituer."
], [
 Q("Quel outil est spécifiquement dédié à la gestion de la relation client ?", ["Un ERP", "Un CRM", "Un tableur", "Un système de paie"], 1, "Le CRM (Customer Relationship Management) centralise les informations clients et le suivi commercial."),
 Q("Quelle qualité d'information est indispensable pour décider ?", ["La quantité", "La fraîcheur et la pertinence", "La complexité", "L'anonymat"], 1, "Une information exacte, à jour et pertinente est indispensable à la décision."),
 Q("Quel mode de coordination repose sur des règles formalisées ?", ["La coordination par communauté", "La coordination par procédures", "La coordination par objectifs", "La coordination hiérarchique directe"], 1, "La coordination par procédures s'appuie sur des règles et des processus standardisés."),
 Q("Quel risque du SI doit être traité par des sauvegardes ?", ["L'obsolescence des données", "La perte de données", "La surcharge d'information", "Le coût du logiciel"], 1, "Les sauvegardes protègent contre la perte accidentelle ou malveillante de données."),
 T("Comment le SI améliore-t-il la coordination d'une équipe commerciale ?", "En partageant les mêmes données (stocks, clients, commandes), en automatisant les remontées d'information et en donnant à chacun une vision commune des objectifs et des résultats.", "Le SI réduit les asymétries d'information et facilite la délégation grâce à un reporting fiable."),
 T("Pourquoi la donnée doit-elle être sécurisée ?", "Parce qu'elle est une ressource stratégique et souvent personnelle : sa fuite expose l'entreprise à des risques juridiques (RGPD), financiers et d'image.", "La sécurité combine mesures techniques (accès, chiffrement, sauvegarde) et organisationnelles (procédures, formation).")
]))

fiches.append(F("Chapitre 15 — CEJM (thème 5) — Marché du travail, segmentation et politiques de l'emploi", [
 "Le marché du travail met en relation l'offre de travail (les travailleurs) et la demande de travail (les employeurs) ; le salaire est le prix du travail.",
 "La population active comprend les personnes en emploi et les chômeurs au sens du BIT, c'est-à-dire disponibles et en recherche active.",
 "Le taux d'activité rapporte la population active à la population en âge de travailler ; le taux d'emploi rapporte les personnes en emploi à cette même population.",
 "La segmentation du marché du travail oppose un marché primaire (emplois stables, qualifiés, protégés) et un marché secondaire (emplois précaires, faiblement qualifiés).",
 "Les déséquilibres du marché du travail peuvent être conjoncturels (manque de demande), structurels (inadaptation des compétences) ou摩擦nels (recherche d'emploi).",
 "La politique de l'emploi combine des mesures actives (formation, accompagnement, emplois aidés) et passives (allocations chômage).",
 "Les acteurs de l'emploi sont l'État, les régions, Pôle emploi (devenu France Travail), les partenaires sociaux et les entreprises.",
 "Les mutations du travail (numérisation, télétravail, portage salarial, plateformes, gig economy) redessinent les frontières de l'emploi salarié.",
 "La productivité du travail et le coût du travail (salaires + charges) influencent la demande de travail des entreprises.",
 "Pour le manager commercial, comprendre le marché du travail aide à anticiper les difficultés de recrutement et à adapter les profils recherchés."
], [
 Q("Qui fait partie de la population active ?", ["Tous les habitants", "Les employés et les chômeurs au sens du BIT", "Les seuls salariés", "Les personnes de plus de 18 ans"], 1, "La population active = personnes en emploi + chômeurs disponibles et en recherche active."),
 Q("Quel marché regroupe les emplois précaires et peu qualifiés ?", ["Le marché primaire", "Le marché secondaire", "Le marché unique", "Le marché du capital"], 1, "La théorie de la segmentation oppose marché primaire et marché secondaire."),
 Q("Quelle mesure relève d'une politique active de l'emploi ?", ["Le versement d'une allocation chômage", "Une action de formation professionnelle", "La retraite", "Le congé parental"], 1, "Les politiques actives visent le retour à l'emploi par la formation et l'accompagnement."),
 Q("Quel est le prix du travail sur le marché ?", ["Le taux d'intérêt", "Le salaire", "Le loyer", "Le dividende"], 1, "Le salaire est la rémunération du facteur travail."),
 T("Quelles sont les causes d'un chômage structurel ?", "Une inadaptation entre les qualifications disponibles et les besoins des entreprises, souvent liée aux mutations technologiques ou sectorielles.", "Contrairement au chômage conjoncturel, le chômage structurel persiste même quand la demande globale se redresse."),
 T("Comment le numérique transforme-t-il le marché du travail ?", "Il crée de nouveaux métiers, rend certaines compétences obsolètes, développe le télétravail et de nouvelles formes d'emploi (plateformes, freelance), tout en augmentant l'exigence de formation continue.", "Ces mutations renforcent l'importance de la GPEC et de la formation tout au long de la vie.")
]))

fiches.append(F("Chapitre 16 — CEJM (thème 5) — Droit du travail : contrats, obligations et rupture", [
 "Le droit du travail est une branche du droit social qui organise les relations entre employeurs et salariés ; ses sources sont la loi, le code du travail, les accords collectifs, le contrat de travail et la jurisprudence.",
 "Le salarié est lié à l'employeur par un contrat de travail caractérisé par trois éléments : une prestation de travail, une rémunération et un lien de subordination.",
 "Le travailleur indépendant accomplit son activité sans lien de subordination : il supporte le risque économique et choisit son organisation.",
 "Le CDI est le contrat de droit commun, sans durée déterminée ; le CDD est conclu pour un motif précis (remplacement, surcroît d'activité, saisonnier) et ne peut pas pourvoir un emploi durable lié à l'activité normale de l'entreprise.",
 "Le contrat d'intérim associe une entreprise de travail temporaire, un salarié intérimaire et une entreprise utilisatrice, pour des missions définies.",
 "Le contrat d'apprentissage et le contrat de professionnalisation combinent formation et activité professionnelle, avec des objectifs de qualification.",
 "L'employeur doit respecter des obligations : paiement du salaire, durée du travail et repos, sécurité et santé, égalité de traitement, remise de documents (bulletins de salaire, contrat).",
 "Le salarié doit exécuter sa prestation, respecter les instructions, la discrétion professionnelle et le règlement intérieur.",
 "Les modes de rupture : démission, rupture conventionnelle, licenciement (pour motif personnel ou économique), fin de CDD, invalidité ou retraite.",
 "Le licenciement obéit à une procédure stricte : entretien préalable, notification écrite, préavis, indemnités ; le non-respect expose l'employeur au prud'hommes."
], [
 Q("Quel est le contrat de travail de droit commun ?", ["Le CDD", "Le CDI", "L'intérim", "Le contrat d'apprentissage"], 1, "Le CDI est le contrat normal ; le CDD est strictement encadré par des motifs légaux."),
 Q("Quel critère distingue le salarié du travailleur indépendant ?", ["Le montant du salaire", "Le lien de subordination", "L'ancienneté", "Le secteur d'activité"], 1, "Le lien de subordination (pouvoir de direction, contrôle, sanction) caractérise le salariat."),
 Q("Quelle est une obligation de l'employeur ?", ["Fournir un logement", "Assurer la sécurité et payer le salaire", "Travailler sans contrat", "Refuser les congés"], 1, "L'employeur doit notamment payer le salaire et assurer la santé et la sécurité des salariés."),
 Q("Que doit précéder un licenciement pour motif personnel ?", ["Un avertissement oral obligatoire", "Un entretien préalable", "Une assemblée générale", "Un avis du comité social et économique systématique"], 1, "L'entretien préalable est une formalité substantielle du licenciement."),
 T("Comment qualifier juridiquement une relation de travail ?", "On vérifie les trois critères : prestation de travail, rémunération et lien de subordination ; l'absence de subordination oriente vers le travail indépendant.", "La qualification est importante car elle détermine le régime applicable (code du travail, protection du salarié, cotisations)."),
 T("Quelle différence entre rupture conventionnelle et démission ?", "La rupture conventionnelle est un accord mutuel avec indemnité et droit à l'ARE ; la démission est une initiative unilatérale du salarié, en principe sans indemnité.", "La rupture conventionnelle doit être homologuée par l'administration du travail.")
]))

fiches.append(F("Chapitre 17 — CEJM (thème 5) — Gestion des compétences, motivation et conditions de travail", [
 "La GPEC (gestion prévisionnelle des emplois et des compétences) anticipe les besoins futurs en compétences et organise l'adaptation des ressources humaines à la stratégie.",
 "La démarche GPEC comporte : analyser l'existant, prévoir les évolutions, identifier les écarts et mettre en œuvre des actions (formation, recrutement, mobilité).",
 "La formation professionnelle est un levier majeur : plan de formation de l'entreprise, compte personnel de formation (CPF), alternance, validation des acquis de l'expérience (VAE).",
 "Les théories de la motivation : Maslow (hiérarchie des besoins), Herzberg (facteurs d'hygiène et facteurs de motivation), McClelland (besoins d'accomplissement, d'appartenance, de pouvoir).",
 "La théorie de l'équité (Adams) montre que le salarié compare ses contributions et ses récompenses à celles des autres ; un sentiment d'injustice démotive.",
 "Le contrat psychologique désigne les attentes non écrites entre le salarié et l'entreprise : son respect favorise l'engagement.",
 "Les conditions de travail comprennent l'organisation du temps de travail, l'environnement physique, la charge de travail, l'autonomie et les relations sociales.",
 "Les risques psycho-sociaux (RPS) résultent d'une exposition à des situations de travail délétères : stress, harcèlement, burn-out, violence. L'employeur a une obligation de prévention.",
 "Le manager dispose de leviers de motivation : fixation d'objectifs clairs, feedback, reconnaissance, participation, autonomie, rémunération variable et animation d'équipe.",
 "L'évaluation des performances individuelles (entretien annuel) doit distinguer la performance de la personne, les moyens mis à disposition et le contexte."
], [
 Q("Que signifie GPEC ?", ["Gestion prévisionnelle des emplois et des compétences", "Gestion permanente des équipes commerciales", "Groupement d'employeurs pour l'emploi collectif", "Gestion des performances et des carrières"], 0, "La GPEC anticipe les besoins en emplois et compétences."),
 Q("Selon Herzberg, quel facteur est un vrai facteur de motivation ?", ["Le salaire", "La reconnaissance", "Les conditions de travail", "La politique de l'entreprise"], 1, "Pour Herzberg, salaire et conditions sont des facteurs d'hygiène ; la reconnaissance et l'accomplissement sont des motivateurs."),
 Q("Quel dispositif permet de financer une formation individuelle ?", ["Le CPF", "Le CDD", "Le BFR", "Le NPS"], 0, "Le compte personnel de formation est mobilisable par le salarié tout au long de sa vie professionnelle."),
 Q("Quelle est une obligation de l'employeur en matière de RPS ?", ["Supprimer tout stress", "Assurer une prévention des risques psycho-sociaux", "Augmenter la charge de travail", "Éviter les réunions"], 1, "L'employeur doit évaluer et prévenir les risques psycho-sociaux, notamment via le DUERP."),
 T("Comment la GPEC aide-t-elle le manager commercial ?", "Elle permet d'anticiper les compétences nécessaires à l'évolution de l'activité (digitalisation, omnicanalité) et de prévoir recrutements, formations et mobilités en conséquence.", "La GPEC relie la stratégie commerciale aux besoins humains et évite les pénuries de compétences."),
 T("Comment motiver une équipe de vente sans augmenter les salaires ?", "En fixant des objectifs clairs et atteignables, en donnant du feedback régulier, en valorisant les réussites, en favorisant l'autonomie et la participation et en organisant des challenges collectifs.", "La reconnaissance, la clarté des objectifs et l'équité de traitement sont des leviers puissants et peu coûteux.")
]))

fiches.append(F("Chapitre 18 — CEJM (thème 6) — Diagnostic stratégique : environnement et ressources", [
 "La démarche stratégique comporte trois temps : diagnostic (où sommes-nous ?), choix stratégiques (où voulons-nous aller ?) et mise en œuvre (comment y aller ?).",
 "Le diagnostic externe analyse l'environnement général (PESTEL) et l'environnement concurrentiel : la structure et le comportement du marché, barrières à l'entrée, pouvoir de négociation des clients et fournisseurs, menace des substituts.",
 "Le modèle des cinq forces de Porter structure l'analyse concurrentielle : rivalité entre concurrents, menace d'entrants, pouvoir des fournisseurs, pouvoir des clients, menace des produits de substitution.",
 "Le diagnostic interne évalue les ressources et compétences de l'entreprise avec le modèle VRIO et la chaîne de valeur.",
 "La matrice SWOT croise les forces et faiblesses internes avec les opportunités et menaces externes : elle synthétise le diagnostic mais ne constitue pas une décision.",
 "Le portefeuille d'activités peut être analysé avec la matrice BCG (poids du marché et part de marché relative) pour arbitrer les investissements.",
 "Les groupes stratégiques regroupent les entreprises poursuivant des stratégies similaires sur un marché ; leur analyse révèle les positions occupées et les espaces libres.",
 "Le benchmark compare l'entreprise aux meilleures pratiques du secteur pour identifier les écarts de performance.",
 "Un diagnostic pertinent est sélectif : il met en évidence les facteurs clés de succès du secteur et les déséquilibres qui appellent une décision.",
 "Dans l'épreuve E4, le candidat doit établir un diagnostic (ou une partie) préparant une décision stratégique, en exploitant la base documentaire fournie."
], [
 Q("Que signifie l'acronyme SWOT ?", ["Strengths, Weaknesses, Opportunities, Threats", "Sales, Workforce, Output, Turnover", "Strategy, Work, Organization, Time", "Strengths, Wages, Orders, Trends"], 0, "SWOT = Forces, Faiblesses, Opportunités, Menaces."),
 Q("Combien de forces concurrentielles le modèle de Porter comporte-t-il ?", ["3", "4", "5", "6"], 2, "Le modèle des cinq forces de Porter analyse la rivalité, les entrants, les substituts, les clients et les fournisseurs."),
 Q("Quel outil analyse le portefeuille d'activités ?", ["La matrice BCG", "Le modèle VRIO", "Le PESTEL", "La chaîne de valeur"], 0, "La matrice BCG classe les activités selon la croissance du marché et la part de marché relative."),
 Q("Quel est un facteur clé de succès ?", ["Un avantage dont dispose l'entreprise", "Une condition indispensable pour réussir dans le secteur", "Un simple chiffre", "Une opinion du dirigeant"], 1, "Les FCS sont les compétences ou ressources nécessaires pour être compétitif sur un marché donné."),
 T("Comment réaliser un diagnostic externe pertinent ?", "On analyse le macro-environnement (PESTEL), puis les forces concurrentielles du secteur, en sélectionnant les facteurs qui influencent réellement l'activité de l'entreprise.", "Le diagnostic doit déboucher sur l'identification d'opportunités et de menaces hiérarchisées."),
 T("Quelle est la limite de la matrice SWOT ?", "Elle ne hiérarchise pas les éléments et ne propose pas de décision : elle est un outil de synthèse, pas d'action.", "Le SWOT doit être prolongé par des choix stratégiques et un plan de mise en œuvre.")
]))

fiches.append(F("Chapitre 19 — CEJM (thème 6) — Choix stratégiques : DAS, options et croissance", [
 "Un domaine d'activité stratégique (DAS) est un segment du marché sur lequel l'entreprise décide d'être compétitive, défini par des produits, des marchés, des technologies et des clients.",
 "La décision stratégique répond à trois questions : dans quels domaines être présent, avec quel avantage concurrentiel et avec quels moyens.",
 "Les options stratégiques globales incluent la spécialisation, la diversification (connexe ou non), l'intégration verticale et l'internationalisation.",
 "Les options par domaine s'appuient sur les stratégies génériques de Porter : domination par les coûts, différenciation, concentration (focus).",
 "La croissance peut être interne (investissement, création d'activité) ou externe (fusion, acquisition, partenariat, franchise) ; chaque mode présente des risques et des délais différents.",
 "Les partenariats stratégiques (alliances, co-traitance, réseaux) permettent de partager les risques et d'accéder à des compétences complémentaires.",
 "La décision doit être évaluée selon sa cohérence avec les ressources, sa faisabilité financière, son acceptabilité par les parties prenantes et sa capacité à créer un avantage durable.",
 "La mise en œuvre suppose un plan d'action, un budget, un calendrier, des indicateurs de suivi et une responsabilité clairement identifiée.",
 "Le contrôle stratégique compare les résultats aux objectifs et déclenche des actions correctrices si les écarts sont significatifs.",
 "Dans une étude de cas E4, une proposition stratégique doit être argumentée à partir du diagnostic, chiffrée si possible, et présenter ses effets attendus et ses risques."
], [
 Q("Que désigne un DAS ?", ["Un document comptable", "Un domaine d'activité stratégique", "Un dirigeant d'entreprise", "Un indicateur social"], 1, "Le DAS délimite le segment de marché sur lequel l'entreprise choisit de se battre."),
 Q("Quelles sont les stratégies génériques de Porter ?", ["Croissance, rentabilité, liquidité", "Coûts, différenciation, concentration", "Production, vente, achat", "Locale, nationale, internationale"], 1, "Porter propose domination par les coûts, différenciation et concentration."),
 Q("Quelle est une forme de croissance externe ?", ["Créer un nouveau produit", "Acquérir une entreprise", "Augmenter les prix", "Former les salariés"], 1, "La croissance externe passe par fusion, acquisition ou prise de participation."),
 Q("Quel critère ne doit pas être négligé dans un choix stratégique ?", ["L'acceptabilité par les parties prenantes", "Le hasard", "La couleur du logo", "Le nombre de réunions"], 0, "Un choix doit être cohérent, faisable et acceptable pour les acteurs concernés."),
 T("Comment articuler diagnostic et décision stratégique ?", "Le diagnostic met en évidence les enjeux (opportunités, menaces, forces, faiblesses) ; la décision y répond en choisissant un domaine d'activité et un mode d'avantage concurrentiel cohérents avec les ressources.", "Une proposition sans lien avec le diagnostic n'est pas recevable dans l'épreuve E4."),
 T("Quels risques accompagnent une croissance par acquisition ?", "Le coût d'acquisition, l'intégration culturelle, la perte de contrôle, l'endettement et la difficulté à réaliser les synergies attendues.", "La croissance externe est rapide mais fragile si l'intégration est mal préparée.")
]))

annales = []
annales.append({"filieres":["bts-mco"],"annees":["BTS2"],"titre":"CEJM 2026 — La Savonnerie du Paradou (sujet national)", "matiere":"CEJM","type":"genere",
 "contenu":"Épreuve E4 — Culture économique, juridique et managériale (4 heures, coefficient 3). Sujet national 2026, d'après le cas officiel « La Savonnerie du Paradou » (mybts.fr).\n\nCONTEXTE : une savonnerie artisanale familiale, créée en Provence, fabrique des savons naturels. Elle fait face à une concurrence accrue, à la hausse du coût des matières premières et à l'opportunité du e-commerce et de l'export.\n\nDOCUMENTS (4 documents) : 1. présentation de l'entreprise et de ses finalités ; 2. article sur le marché du savon naturel et les nouvelles attentes des consommateurs ; 3. tableau comparatif des canaux de distribution (distribution spécialisée, marketplace, site propre) ; 4. extrait du règlement européen sur les cosmétiques et les allégations.\n\nMISSIONS : Mission 1 — Présenter l'activité de la Savonnerie du Paradou et son modèle économique (finalités, parties prenantes, création de valeur). Mission 2 — Analyser l'environnement de l'entreprise et les opportunités offertes par l'international (PESTEL, forces concurrentielles, stratégies de distribution). Mission 3 — Analyser l'impact de la modernisation numérique et proposer des choix stratégiques cohérents (SIC, canaux digitaux, financement, risques).",
 "correction":"Mission 1 : identifier l'entreprise comme une PME artisanale à finalité économique et sociétale (savoir-faire, terroir, emploi local) ; recenser les parties prenantes (dirigeants, salariés, fournisseurs d'huiles essentielles, distributeurs, clients, collectivité) et expliquer la création de valeur partagée. Le modèle économique articule sourcing, production, distribution et valorisation de la marque.\n\nMission 2 : le PESTEL met en évidence l'évolution de la demande (consommation responsable, naturalité), la pression concurrentielle (grandes marques, marques de distributeur), la réglementation cosmétique et les opportunités d'export. L'analyse des cinq forces montre un pouvoir de négociation des distributeurs et une menace de substituts. Les canaux doivent être comparés par le contrôle de l'image, la marge et l'accès au marché.\n\nMission 3 : la modernisation numérique (site propre, marketplace, CRM, outils de pilotage) transforme la chaîne de valeur et le relation client ; elle exige des compétences et un financement. Le candidat propose une stratégie cohérente (différenciation par l'authenticité, canaux digitaux complémentaires, partenariats à l'export), chiffre si possible les investissements et identifie les risques (dépendance aux plateformes, conformité réglementaire, protection de la marque). Une conclusion synthétique répond aux trois missions."})
annales.append({"filieres":["bts-mco"],"annees":["BTS2"],"titre":"CEJM 2025 — Tout en perles (sujet national)", "matiere":"CEJM","type":"genere",
 "contenu":"Épreuve E4 (4 heures, coefficient 3). Sujet national 2025, d'après le cas officiel « Tout en perles » (mybts.fr).\n\nCONTEXTE : la SARL « Tout en perles » commercialise des perles de culture et des bijoux ; son dirigeant, Dominique Partol, développe l'entreprise sur un marché de niche.\n\nDOCUMENTS : 1. présentation de la SARL et de son positionnement ; 2. étude du marché de la bijouterie et des tendances de consommation ; 3. tableau des modes de financement envisagés ; 4. extrait sur la protection des données et le e-commerce.\n\nMISSIONS : Mission 1 — Montrer comment « Tout en perles » est ancrée sur son marché (finalités, sources de revenus, parties prenantes). Mission 2 — Analyser les opportunités saisies par Dominique Partol et les choix de développement (diagnostic, stratégie, financement). Mission 3 — Étudier l'impact du numérique sur l'activité de la SARL et proposer des actions (canal de vente, RGPD, sécurisation, compétences).",
 "correction":"Mission 1 : la SARL est une société à responsabilité limitée dont l'associé unique ou les associés répondent à concurrence de leurs apports ; l'entreprise est ancrée sur un marché de niche par son savoir-faire et sa maîtrise de la chaîne d'approvisionnement.Les parties prenantes incluent les fournisseurs de perles, les artisans, les clients et les plateformes de vente.\n\nMission 2 : le diagnostic met en évidence une demande pour des produits authentiques, une concurrence sur la qualité et le prix, et une opportunité de croissance par la diversification et l'export. Le dirigeant arbitre entre autofinancement et emprunt en comparant coût, capacité de remboursement et dilution du contrôle ; la stratégie de différenciation est cohérente avec le positionnement.\n\nMission 3 : le e-commerce ouvre de nouveaux canaux mais crée des obligations (mentions légales, CGV, droit de rétractation, RGPD : consentement, sécurité des données, 72 heures en cas de violation). Les actions proposées : structurer un site propre ou une marketplace, outiller le SIC (CRM), former les équipes et protéger la marque."})
annales.append({"filieres":["bts-mco"],"annees":["BTS2"],"titre":"CEJM 2024 — NOTARIUS (sujet national)", "matiere":"CEJM","type":"genere",
 "contenu":"Épreuve E4 (4 heures, coefficient 3). Sujet national 2024, d'après le cas officiel NOTARIUS (mybts.fr).\n\nCONTEXTE : une étude notariale doit faire face à l'évolution de son environnement : concurrence, numérisation des démarches, attentes des clients et mutation du métier.\n\nDOCUMENTS : 1. organisation de l'étude et répartition des compétences ; 2. données sur le marché des services juridiques et la concurrence ; 3. témoignage de collaborateurs sur les conditions de travail ; 4. texte sur la transformation numérique des services.\n\nMISSIONS : Mission 1 — Réaliser l'analyse interne de l'étude et identifier les éléments de préservation de son activité (ressources, compétences, organisation). Mission 2 — Étudier le marché et son impact sur l'étude (concurrence, PESTEL, attentes clients). Mission 3 — Proposer des pistes de développement (organisation du travail, gestion des compétences, numérisation, pilotage).",
 "correction":"Mission 1 : l'analyse interne recense les ressources tangibles (locaux, outils) et intangibles (expertise juridique, confiance, notoriété), la répartition des rôles (notaires, clercs, assistants) et les compétences clés ; la valeur repose sur l'expertise et la relation de confiance.\n\nMission 2 : le marché des services juridiques se transforme (conseil en ligne, plateformes, concurrence entre études) ; les facteurs PESTEL pertinents sont la réglementation des professions, la digitalisation et l'évolution des attentes des clients (rapidité, transparence, prix). L'étude doit transformer ces contraintes en opportunités de différenciation par la qualité et l'accompagnement.\n\nMission 3 : les pistes portent sur l'organisation (répartition des tâches, plannings), la montée en compétences (formation au numérique, GPEC), la numérisation des parcours (signature électronique, portail client, SIC) et le pilotage (indicateurs de satisfaction, délais de traitement). Les propositions sont hiérarchisées et leur faisabilité est discutée."})
annales.append({"filieres":["bts-mco"],"annees":["BTS2"],"titre":"CEJM 2023 — GEMDOUBS (sujet national)", "matiere":"CEJM","type":"genere",
 "contenu":"Épreuve E4 (4 heures, coefficient 3). Sujet national 2023, d'après le cas officiel GEMDOUBS (mybts.fr).\n\nCONTEXTE : GEMDOUBS est une entreprise qui développe un nouveau modèle économique dans le secteur de la bijouterie / horlogerie en ligne.\n\nDOCUMENTS : 1. présentation de l'entreprise et de son modèle économique ; 2. analyse du marché et des concurrents ; 3. description des parties prenantes (investisseurs, fournisseurs, clients, salariés) ; 4. données financières prévisionnelles.\n\nMISSIONS : Mission 1 — Analyser l'environnement de l'entreprise et les opportunités offertes par son nouveau modèle économique. Mission 2 — Présenter les parties prenantes de GEMDOUBS et analyser leurs attentes, convergentes ou divergentes. Mission 3 — Analyser l'activité de l'entreprise et proposer des choix de développement cohérents avec ses ressources.",
 "correction":"Mission 1 : le modèle économique repose sur la vente en ligne, la maîtrise de la chaîne de valeur et une proposition de valeur différenciée ; l'analyse PESTEL et des cinq forces met en évidence la croissance de l'e-commerce, l'intensité concurrentielle, l'importance de la logistique et de la confiance (avis, retours).\n\nMission 2 : les parties prenantes sont les fondateurs et investisseurs (rentabilité, croissance), les fournisseurs (volumes, délais), les clients (prix, qualité, livraison), les salariés (emploi, compétences) et les plateformes (commissions). Le manager doit arbitrer entre ces attentes par une gouvernance et une communication adaptées.\n\nMission 3 : l'analyse des ressources (VRIO) montre ce qui est stratégique (savoir-faire, marque, données clients) ; les choix de développement (canaux, partenariats, investissement logistique) sont justifiés par leur cohérence avec le modèle et leur faisabilité financière, à partir des documents chiffrés."})

with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"fiches": fiches, "annales": annales}, f, ensure_ascii=False, indent=2)
print("B", len(fiches), len(annales))
