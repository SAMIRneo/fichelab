# -*- coding: utf-8 -*-
"""Generateur sti2d-mat-part-C.json — lot C : culture et methodes (20 fiches).

Developpement durable, architecture et construction, systemes d'information et
numerique, methodologie de projet et anglais technique pour la serie STI2D :
12 points de cours, 9 questions corrigees (7 QCM + 2 texte),
7 blocs en ordre strict, 3 schemas via diag().
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_etapes,
                      svg_compare, bloc, valider_et_ecrire)

FIL = ["sti2d"]
REF = (
    "Programme des enseignements de specialite des classes de premiere et terminale de la serie STI2D "
    "(arrete du 17 janvier 2019, NOR MENE1901591A, Bulletin officiel special n 1 du 22 janvier 2019) : "
    "developpement durable, architecture et construction (AC), systemes d'information et numerique (SIN), "
    "methodologie de projet et langues vivantes techniques. Tronc commun : arrete du 17 janvier 2019 "
    "(NOR MENE1901585A, langues vivantes) et programme d'enseignement moral et civique. Ressources : "
    "eduscol « Programmes et ressources en serie STI2D », « Developpement durable » et « Baccalaureat "
    "technologique STI2D » ; Agenda 2030 des Nations unies et objectifs de developpement durable."
)


def S(texte):
    return [x.strip() for x in texte.split("|") if x.strip()]


def R(texte):
    return [x.strip() for x in texte.split("~") if x.strip()]


def QC(question, options, correct, correction):
    return qcm(question, R(options), correct, correction)


def QT(question, reponse, correction):
    return qt(question, reponse, correction)


def _grid(texte):
    lignes = S(texte)
    if len(lignes) == 1:
        cellules = R(lignes[0])
        return [cellules[i:i + 3] for i in range(0, 9, 3)]
    return [R(x) for x in lignes]


def _cmp(texte):
    cellules = R(texte)
    n = len(cellules) // 2
    return (cellules[0], cellules[1:n]), (cellules[n], cellules[n + 1:])


def C(idea, eq, leg, grid, steps, traps, ex, cmp1, cmp2):
    return {"idea": idea, "eq": eq, "leg": leg, "grid": _grid(grid),
            "steps": S(steps), "traps": S(traps), "ex": [R(x) for x in S(ex)],
            "cmp": (_cmp(cmp1), _cmp(cmp2))}


def build(prefix, titre, matiere, annees, points, questions, c):
    """Assemble une fiche prototype complete a partir des donnees compactes."""
    titre_complet = prefix + " · " + titre
    short = titre.split(":")[0].strip()
    aff = [
        bloc("L'idee en une phrase", texte=c["idea"], type="intro"),
        bloc("La notion a maitriser", eq=c["eq"], leg=c["leg"], type="formule"),
        bloc("Tableau de lecture", items=c["grid"], type="grille"),
        bloc("Les points essentiels du chapitre", items=points[1:5], type="liste"),
        bloc("La demarche pas a pas", items=c["steps"], type="etapes"),
        bloc("Pieges et erreurs frequentes", items=c["traps"], type="attention"),
        bloc("En situation : exemples chiffres", items=[
            '%s : <span class="cle">%s</span>' % (p[0], p[1]) for p in c["ex"]
        ], type="exemples"),
    ]
    schema = [
        diag("1 · " + short, svg_grille(short, ["Notion", "Definition", "Repere"], c["grid"])),
        diag("2 · Demarche", svg_etapes("Procedure : " + short, c["steps"])),
        diag("3 · A distinguer", svg_compare(short, c["cmp"][0], c["cmp"][1])),
    ]
    assert len(points) == 12, "12 points attendus pour " + prefix
    assert len(questions) == 9, "9 questions attendues pour " + prefix
    assert sum(1 for q in questions if q.get("type") == "qcm") == 7, prefix
    assert sum(1 for q in questions if q.get("type") == "texte") == 2, prefix
    assert len(aff) == 7 and len(schema) == 3, prefix
    return fiche(FIL, annees, matiere, titre_complet, REF,
                 points, questions, aff, schema)


F = []


def add(prefix, titre, mat, ans, points, questions, c):
    F.append(build(prefix, titre, mat, ans, points, questions, c))


# ============================================================ DUR1
add("DUR1", "Developpement durable : trois piliers et objectifs mondiaux", "Développement durable", ["1re"],
S("Le developpement durable repond a une double exigence : satisfaire les besoins presents et preserver les generations futures."
  "|La definition de reference provient du rapport Brundtland de la commission mondiale sur l'environnement et le developpement, publie en 1987."
  "|Le sommet de la Terre de Rio en 1992 a consacre le principe du developpement durable et le lien entre environnement et developpement."
  "|Les trois piliers sont economique, social et environnemental : une decision durable doit les concilier."
  "|Le pilier economique vise la creation de richesses et la viabilite des activites sur le long terme."
  "|Le pilier social vise l'equite, l'acces aux biens essentiels, la sante, l'education et la participation."
  "|Le pilier environnemental vise la preservation des ressources, de la biodiversite et du climat."
  "|Les objectifs de developpement durable (ODD) de l'Agenda 2030 de l'ONU comptent 17 objectifs et 169 cibles."
  "|Parmi les ODD figurent l'elimination de la pauvrete, l'energie propre, l'innovation et la lutte contre le changement climatique."
  "|Les indicateurs comme le PIB sont insuffisants : l'IDH et l'empreinte ecologique completent la mesure du developpement."
  "|L'empreinte ecologique compare la consommation de ressources a la capacite de regeneration de la planete."
  "|En ingenieurise, le developpement durable se traduit par l'eco-conception, la sobriete et l'analyse du cycle de vie."),
[QC("Quelle annee est associee au rapport Brundtland ?", "1972~1987~1992~2015", 1,
    "Le rapport « Notre avenir a tous » date de 1987."),
 QC("Combien de piliers compte le developpement durable ?", "Deux~Trois~Quatre~Cinq", 1,
    "Les piliers economique, social et environnemental forment trois dimensions."),
 QC("Combien d'objectifs de developpement durable compte l'Agenda 2030 ?", "8~10~15~17", 3,
    "L'Agenda 2030 definit 17 objectifs et 169 cibles."),
 QC("Quel indicateur complete le PIB pour mesurer le developpement humain ?", "L'IDH~Le cours du petrol~La population~Le nombre d'entreprises", 0,
    "L'indice de developpement humain combine sante, instruction et revenu."),
 QC("Que compare l'empreinte ecologique ?", "Le prix et la masse d'un produit~La consommation de ressources et la biocapacite~Les emissions et le PIB~La population et l'emploi", 1,
    "L'empreinte confronte la demande de ressources a la capacite de regeneration."),
 QC("Quel sommet a consacre le developpement durable en 1992 ?", "Rio~Paris~Rome~Geneve", 0,
    "Le sommet de la Terre de Rio a diffusé la notion en 1992."),
 QC("Quelle traduction du developpement durable concerne directement un concepteur ?", "L'eco-conception~Le seul respect des couts~La publicite~L'augmentation des volumes", 0,
    "L'eco-conception intègre l'environnement des les premieres etapes de la conception."),
 QT("Expliquer pourquoi le developpement durable exige de traiter ensemble les trois piliers.",
    "Une action qui ne concerne que l'environnement peut etre socialement injuste : interdire un usage sans proposer d'alternative frappe d'abord les populations les plus fragiles. Une action purement economique qui ignore les limites ecologiques reporte les couts sur les generations futures. Une action sociale sans viabilite economique ne peut etre financee durablement. Les trois piliers sont donc interdependants : la lutte contre la pauvrete passe par l'acces a l'energie et a l'education, mais une energie fossile bon marche augmente les emissions et nuit a la sante. La definition de Brundtland lie explicitement les besoins presents et la capacite des generations futures, ce qui impose une evaluation croisee des effets d'une decision, en particulier d'une decision technique.",
    "On montre l'interdependance des trois dimensions avec des exemples concrets."),
 QT("Comment les objectifs de developpement durable peuvent-ils guider un projet STI2D ?",
    "Les ODD offrent un cadre commun pour formuler les objectifs d'un projet au-dela de la seule performance technique. Un etudiant peut se referer a l'ODD 7 (energie propre) pour un systeme d'alimentation solaire, a l'ODD 9 (innovation) pour une nouvelle architecture de capteur, ou a l'ODD 12 (consommation et production responsables) pour reduire les dechets d'un prototype. Il traduit ensuite chaque objectif en indicateurs mesurables : consommation electrique, taux de matiere recyclée, duree de vie, cout total. Les ODD servent ainsi de grille de questionnement et de justification du choix technique. Ils ne remplacent pas le cahier des charges, mais ils l'enrichissent en explicitant les effets sociaux et environnementaux attendus.",
    "On cite quelques ODD, leur traduction en indicateurs et leur articulation avec le cahier des charges.")],
C("Le developpement durable concilie economie, equite sociale et environnement pour les generations presents et futures.",
  "Brundtland 1987 · Rio 1992 · 17 ODD et 169 cibles (Agenda 2030)",
  "3 piliers · PIB, IDH, empreinte ecologique · eco-conception",
  "Brundtland~Definition de reference~Trois piliers~Economique, social, environnemental~ODD~17 objectifs~IDH~Developpement humain",
  "Identifier les besoins et les generations concernees|Evaluer les trois piliers|Relier aux ODD pertinents|Choisir des indicateurs mesurables|Verifier les effets a long terme",
  "Reduire le durable au seul recyclage|Ignorer la dimension sociale|Croitre que le PIB suffit|Parler des ODD sans indicateurs concrets",
  "1987~Rapport Brundtland~1992~Sommet de Rio~17 ODD~Agenda 2030~169 cibles~IDH~Trois dimensions~Empreinte et biocapacite",
  "PIB~Production economique~IDH~Sante, instruction et revenu",
  "Besoins presents~Generation actuelle~Generations futures~Capacite a satisfaire"))

# ============================================================ DUR2
add("DUR2", "Eco-conception et cycle de vie d'un produit", "Développement durable", ["1re"],
S("L'eco-conception integre les considerations environnementales des la phase de conception, avant la fabrication."
  "|Le cycle de vie d'un produit comprend l'extraction des matieres premieres, la fabrication, la distribution, l'usage et la fin de vie."
  "|Une analyse du cycle de vie (ACV) recense les flux d'energie, de matiere et de dechets a chaque etape."
  "|L'ACV suit une demarche normalisee : definition de l'objectif, inventaire, evaluation d'impact et interpretation."
  "|L'unite fonctionnelle definit le service etudie, par exemple « eclairer une piece pendant 10 000 heures »."
  "|Les limites du systeme precisent quelles etapes sont incluses dans l'etude, du berceau au tombeau ou du berceau au berceau."
  "|Les indicateurs d'impact courants sont l'empreinte carbone, la consommation d'eau, l'eutrophisation et l'epuisement des ressources."
  "|Le principe de sobriete vise a reduire la quantite de matieres et d'energie necessaires au service rendu."
  "|Un produit modulaire est plus facile a reparer : le remplacement d'un element evite de jeter l'ensemble."
  "|Le choix de materiaux recyclees ou renouvelables reduit l'impact de la phase d'extraction."
  "|Une mauvaise ACV peut deplacer le probleme : alléger un produit en utilisant un materiau tres energivore a la fabrication peut augmenter l'impact global."
  "|L'eco-conception est un levier de l'innovation en STI2D car elle oblige a inventer d'autres manieres de rendre le meme service."),
[QC("Quelle est la premiere etape d'une ACV ?", "L'interpretation~La definition de l'objectif et de l'unite fonctionnelle~La fabrication~Le recyclage", 1,
    "L'ACV commence par cadrer l'etude : objectif, unite fonctionnelle et limites."),
 QC("Que definit l'unite fonctionnelle ?", "Le prix du produit~Le service etudie et quantifie~La masse du produit~Le nombre de pieces", 1,
    "Toute comparaison doit porter sur un meme service rendu."),
 QC("Quel indicateur mesure les emissions de gaz a effet de serre ?", "L'eutrophisation~L'empreinte carbone~La dureté~La resilience", 1,
    "L'empreinte carbone agrège les emissions en equivalent CO2."),
 QC("Quel est un benefice d'une conception modulaire ?", "Une masse plus faible~Une reparation plus facile~Un prix de vente plus eleve~Une fabrication plus rapide", 1,
    "La modularite permet de remplacer une partie sans jeter le tout."),
 QC("Que signifie « du berceau au tombeau » ?", "De l'extraction a la fin de vie~Du recyclage a la vente~De l'usage a la fabrication~Sans limites", 0,
    "L'analyse couvre toute la vie du produit jusqu'a l'elimination."),
 QC("Quel risque d'une ACV mal conduite ?", "Ameliorer tous les indicateurs~Deplacer l'impact vers une autre etape~Supprimer l'usage~Augmenter le service", 1,
    "Sans vision du cycle complet, on optimise une etape en degradant une autre."),
 QC("Quand faut-il introduire l'eco-conception ?", "Apres la fabrication~Des la conception~Lors de la mise au rebut~Jamais", 1,
    "Les choix de conception determinent l'essentiel des impacts futurs."),
 QT("Comparer deux gobelets, un jetable en plastique et un gobelet reused en ceramique, en raisonnant en cycle de vie.",
    "La comparaison doit porter sur la meme unite fonctionnelle, par exemple « servir une boisson 100 fois ». Le gobelet jetable demande peu de matiere par usage mais consomme 100 exemplaires, avec des impacts d'extraction, de fabrication et de traitement des dechets repetés. Le gobelet en ceramique demande plus d'energie pour sa fabrication, mais il est réutilisable : son impact par usage diminue avec le nombre d'utilisations. Il faut ajouter le lavage, qui consomme de l'eau et de l'energie, et tenir compte des pertes et de la casse. Le resultat depend donc du nombre reel de reutilisations et des modes de lavage : une ceramique lavee a haute temperature etusage unique peut etre moins favorable. Une ACV permet de chiffrer ces hypotheses plutot que de trancher par intuition.",
    "On respecte l'unite fonctionnelle et on discute fabrication, reuse, lavage et fin de vie."),
 QT("Expliquer comment la sobriete differ de la simple amelioration du rendement.",
    "Ameliorer le rendement consiste a consommer moins d'energie ou de matiere pour rendre le meme service, par exemple un moteur plus efficace. La sobriete va plus loin : elle interroge le besoin lui-meme et la quantite de service necessaire. Elle peut conduire a supprimer une fonction peu utile, a reduire l'encombrement, a allonger la duree de vie ou a mutualiser un equipement entre plusieurs usagers. Le rendement agit sur l'efficacite du procede, la sobriete agit sur le niveau de consommation et sur le nombre de biens produits. Les deux sont complémentaires : unproduit sobre et efficace a le plus faible impact. En ingenieurise, la sobriete invite a demander si la fonction proposee est reellement necessaire avant d'optimiser sa realisation.",
    "On oppose efficacite et reduction du besoin, avec exemples et complementarite.")],
C("L'eco-conception agit sur toute la vie du produit ; l'ACV mesure les impacts pour un meme service rendu.",
  "ACV : objectif, inventaire, evaluation, interpretation",
  "Unite fonctionnelle · limites du systeme · empreinte carbone · sobriete et modularite",
  "Cycle de vie~De l'extraction a la fin de vie~ACV~Analyse des impacts~Unite fonctionnelle~Service etudie~Sobriété~Moins de matieres et d'energie",
  "Definir le service et l'unite fonctionnelle|Fixer les limites du systeme|Inventorier les flux a chaque etape|Evaluer les indicateurs d'impact|Revoir la conception pour reduire les impacts",
  "Comparer des produits sans meme service|Ignorer la phase d'usage|Optimiser une etape en deplaçant l'impact|Oublier la fin de vie",
  "100 usages~Gobelet jetable ou ceramique~ACV~Quatre etapes~Empreinte carbone~En equivalent CO2~Modularite~Reparation facile",
  "Sobriété~Reduire le besoin~Rendement~Moins de consommation pour meme service",
  "Berceau au tombeau~Jusqu'a la fin de vie~Berceau au berceau~Recyclage en boucle"))

# ============================================================ DUR3
add("DUR3", "Indicateurs environnementaux et bilan carbone", "Développement durable", ["Terminale"],
S("Un indicateur environnemental est une grandeur chiffree qui permet de mesurer et de suivre un impact."
  "|L'empreinte carbone additionne les emissions de gaz a effet de serre exprimees en equivalent dioxyde de carbone."
  "|Le bilan carbone est une methode de comptabilisation qui repartit les emissions par poste : energie, transport, dechets, achats."
  "|Les gaz a effet de serre comprennent le dioxyde de carbone, le methane, le protoxyde d'azote et les gaz fluorés."
  "|Le pouvoir de réchauffement global (PRG) convertit chaque gaz en equivalent CO2 sur une duree donnee, souvent 100 ans."
  "|Les facteurs d'emission relient une activite a une quantite d'emissions, par exemple kg de CO2 par kWh."
  "|Une emission directe provient d'une source controlee par l'organisation ; une emission indirecte liee a l'energie provient de la production d'electricite consommee."
  "|La neutralite carbone consiste a equilibre les emissions residuelles avec des puits de carbone ou des reductions ailleurs."
  "|La compensation ne doit intervenir qu'apres la reduction des emissions :on parle de hierarchie eviter, reduire, compenser."
  "|L'analyse des cycles de vie donne des indicateurs complementaires comme la consommation d'eau ou l'usage de sol."
  "|Un indicateur doit etre defini avec son unite, sa source et la periode consideree pour etre exploitable."
  "|Le suivi d'indicateurs dans le temps permet de verifier l'efficacite des actions d'eco-conception engagees."),
[QC("Dans quelle unite exprime-t-on une empreinte carbone ?", "En kilogrammes de dechets~En equivalent CO2~En litres d'eau~En kWh uniquement", 1,
    "Les emissions sont converties en equivalent dioxyde de carbone."),
 QC("Que permet un facteur d'emission ?", "De convertir une activite en emission estimée~De mesurer la masse d'un produit~De calculer un prix~De remplacer l'ACV", 0,
    "Le facteur relie une donnee d'activite a une quantite d'emissions."),
 QC("Quel gaz a un pouvoir de réchauffement eleve mais une faible concentration ?", "Le dioxyde de carbone~Le methane~L'azote~L'oxygene", 1,
    "Le methane a un PRG bien superieur a celui du CO2 sur 100 ans."),
 QC("Quelle est la bonne hierarchie d'action ?", "Compenser, reduire, eviter~Eviter, reduire, compenser~Reduire, compenser, eviter~Compenser seulement", 1,
    "On evite d'abord, puis on reduit, et on compense seulement le residuel."),
 QC("Qu'est-ce qu'une emission indirecte ?", "Une emission non mesuree~Une emission liee a l'energie ou aux achats de l'organisation~Une emission sans gaz~Une emission de CO2 seulement", 1,
    "Les emissions indirectes sont liees aux consommations de l'organisation mais produites chez un tiers."),
 QC("Que designe la neutralite carbone ?", "Zero emission absolue~Equilibre entre emissions residuelles et puits ou reductions~Absence de transport~Un bilan sans indicateur", 1,
    "La neutralite est un equilibre, pas l'absence totale d'emissions."),
 QC("Quelles precisions doivent accompagner un indicateur ?", "Son unite, sa source et la periode~Sa couleur~Le nom du logiciel~La date du jour seulement", 0,
    "Sans ces elements, l'indicateur n'est pas interpretable ni comparable."),
 QT("Une entreprise consomme 20 000 kWh d'electricite avec un facteur de 0,05 kg CO2e/kWh. Calculer l'emission liee et commenter la marge d'incertitude.",
    "L'emission est de 20 000 × 0,05 = 1000 kg CO2e, soit 1 tonne d'equivalent CO2. Le resultat depend directement du facteur utilise : si le mix electrique est different, le facteur peut varier de 0,02 a 0,3 kg CO2e/kWh, ce qui donnerait entre 400 et 6000 kg. Il faut donc indiquer la source du facteur, le pays et l'annee de reference. L'incertitude sur la consommation releve et sur le facteur se propage au resultat final. On presente le bilan avec une precision coherente : un resultat affiche a 0,001 kg n'est pas justifie si le facteur est connu a 10 % pres.",
    "On attend le calcul, l'impact du choix du facteur et une discussion de la precision."),
 QT("Expliquer pourquoi la compensation carbone ne doit pas remplacer la reduction des emissions.",
    "La compensation finance une action de reduction ou de sequestration ailleurs, par exemple la plantation d'arbres ou le financement d'une installation renouvelable. Elle peut presenter des limites : permanence incertaine des puits, difficulté de mesurer l'additionalite, retard entre emission et absorption. Si une organisation compensse sans reduire, ses emissions reelles restent identiques et l'impact local, comme la pollution de l'air en ville, n'est pas traite. La hierarchie eviter, reduire, compenser exige donc d'agir d'abord sur la source : sobriete, efficacite, changement de procede ou d'energie. La compensation ne concerne que les emissions residuelles qui ne peuvent pas etre supprimees avec les moyens disponibles, et elle doit etre documentee et verifiable.",
    "On cite les limites de la compensation et la priorite donnée a la reduction a la source.")],
C("Un indicateur environnemental n'est utile que s'il est defini, source et suivi : le bilan carbone classe les emissions par poste.",
  "Emission = activite × facteur d'emission · PRG en equivalent CO2",
  "Eviter, reduire, compenser · emissions directes et indirectes · neutralite",
  "Empreinte carbone~Emissions en equivalent CO2~Facteur d'emission~Activite vers emission~PRG~Pouvoir de réchauffement~Bilan~Emissions par poste",
  "Definir le perimetre et la periode|Relever les donnees d'activite|Appliquer les facteurs d'emission|Classer les postes|Agir selon eviter, reduire, compenser",
  "Utiliser un facteur sans source|Confondre emission directe et indirecte|Compenser avant de reduire|Donner trop de chiffres significatifs",
  "20000 kWh~Facteur 0,05~1000 kg CO2e~1 tonne~Facteur 0,3~6000 kg~PRG du methane~Superieur au CO2",
  "Emission directe~Source controlee~Emission indirecte~Chez un tiers",
  "Reduction~Agir a la source~Compensation~Agir ailleurs"))

# ============================================================ DUR4
add("DUR4", "Economie circulaire et gestion des dechets", "Développement durable", ["Terminale"],
S("L'economie circulaire vise a maintenir la valeur des ressources dans l'economie en reduisant les dechets."
  "|Elle s'oppose a l'economie lineaire du type extraire, fabriquer, jeter."
  "|Les principes de l'economie circulaire sont reduire, reutiliser, reparer, recycler et recuperer."
  "|La hierarchie de gestion des dechets privilégie la prevention, puis le reuse, puis le recyclage, puis l'incineration avec valorisation energetique et enfin l'enfouissement."
  "|Le taux de recyclabilite est la part de la masse d'un produit pouvant etre recyclee avec les filieres existantes."
  "|Le recyclage effectif depend du demontage, de la separation des materiaux et de l'existence d'une filiere de collecte."
  "|La responsabilite elargie du producteur (REP) rend le fabricant responsable de la fin de vie de ses produits."
  "|En France, des filieres REP couvrent notamment les equipements electriques et electroniques, les piles et les emballages."
  "|L'ecoconception pour le demontage privilégie les vis aux colles et limite le nombre de materiaux differents."
  "|Le marquage des polymeres facilite le tri : sans identification, un plastic melange est difficile a recycler."
  "|La valeur d'un materiau apres recyclage depend de sa purete : un melange degrade la qualite et le prix de la matiere recyclee."
  "|Pour un concepteur STI2D, integrer la fin de vie des la conception est un levier d'innovation et de reduction des couts."),
[QC("Quel modele l'economie circulaire remplace-t-elle ?", "Extraire, fabriquer, jeter~Reduire, reutiliser, recycler~Produire, stocker, vendre~Acheter, revendre, jeter", 0,
    "L'economie circulaire s'oppose au modele lineaire extraire-fabriquer-jeter."),
 QC("Quelle est la premiere priorite de la hierarchie des dechets ?", "L'enfouissement~La prevention~L'incineration~Le recyclage", 1,
    "Le meilleur dechet est celui qui n'est pas produit."),
 QC("Qu'est-ce que la responsabilite elargie du producteur ?", "Une taxe sur les ventes~La responsabilite du fabricant pour la fin de vie~Un label volontaire~Une obligation du consommateur", 1,
    "La REP transfere au producteur la gestion de la fin de vie de ses produits."),
 QC("Quel choix facilite le demontage ?", "La colle forte~Les vis et assemblages reversibles~Le soudage generalise~Le surmoulage", 1,
    "Un assemblage reversible permet de separer les constituants."),
 QC("Pourquoi marquer les polymeres ?", "Pour améliorer l'aspect~Pour faciliter le tri et le recyclage~Pour augmenter la masse~Pour changer la couleur", 1,
    "L'identification de la resine est necessaire au tri mechanique."),
 QC("Quel effet d'un melange de materiaux sur le recyclage ?", "Une meilleure purete~Une baisse de qualite de la matiere recyclee~Aucun effet~Une hausse du prix", 1,
    "Les melanges contaminent la matiere et limitent les usages possibles."),
 QC("Que mesure le taux de recyclabilite ?", "La masse produite~La part recyclable avec les filieres existantes~Le cout de collecte~Le nombre de dechets", 1,
    "La recyclabilite est une propriete potentielle, distincte du recyclage reel."),
 QT("Expliquer la difference entre recyclabilite et recyclage effectif, avec l'exemple d'un emballage composite.",
    "Un emballage est recyclable si ses materiaux peuvent techniquement etre traites par une filiere. Il est effectivement recycle s'il est collecte, trie et oriente vers cette filiere. Un emballage composite associant carton, aluminium et plastic est difficile a separer : meme si chaque materiau est recyclable separement, la filiere de collecte peut ne pas accepter le composite. Son taux de recyclabilite theorique est donc eleve alors que son taux de recyclage reel est faible. Pour ameliorer la situation, on simplifie la structure de l'emballage, on marque les materiaux et on informe le consommateur sur le tri. La difference entre les deux taux mesure l'ecart entre le potentiel technique et l'organisation reelle de la collecte.",
    "On distingue potentiel technique et resultat reel, avec l'exemple du composite."),
 QT("Comment un jeune ingenieur peut-il integrer l'economie circulaire dans un projet de prototype ?",
    "Il peut d'abord choisir des materiaux monomateriaux plutot que des composites, afin de faciliter le tri en fin de vie. Il privilegie des assemblages demontables, par exemple des vis standardisees, et evite les colles definitives. Il limite la quantite de matiere en dimensionnant au plus juste et en reutilisant des elements récupérés pour le prototype lui-meme. Il documente la nature des materiaux et les consignes de demontage dans le dossier projet. Il verifie ensuite l'existence d'une filiere locale pour les dechets generes par le prototypage, notamment les résidus d'impression 3D et les chutes de tole. Enfin, il estime le cout de la fin de vie des la conception, car un produit demontable cout souvent moins cher a traiter.",
    "On attend monomateriau, assemblages reversibles, sobriete, documentation et filiere locale.")],
C("L'economie circulaire conserve la valeur des ressources : mieux vaut prevenir, reutiliser et reparer avant de recycler.",
  "Reduire · reutiliser · reparer · recycler · recuperer",
  "REP · hierarchie des dechets · demontage · marquage des polymeres",
  "Economie circulaire~Boucle de valeur~REP~Responsabilite du producteur~Recyclabilite~Potentiel technique~Demontage~Separation des parties",
  "Estimer les dechets du projet|Choisir des materiaux monomateriaux|Concevoir des assemblages reversibles|Marquer et documenter les materiaux|Verifier la filiere de collecte",
  "Confondre recyclabilite et recyclage reel|Coller des elements qu'il faudra separer|Melanger des polymeres sans identification|Negliger le cout de fin de vie",
  "Emballage composite~Recyclabilite theoreique eleve~Recyclage reel faible~REP~Piles et equipements~Vis~Assemblage reversible~Tri~Marquage des polymeres",
  "Economie lineaire~Extraire et jeter~Economie circulaire~Maintenir la valeur",
  "Prevention~Eviter le dechet~Recyclage~Retransformer la matiere"))

# ============================================================ ARC1
add("ARC1", "Architecture et construction : materiaux et structures", "Architecture et construction", ["1re"],
S("Une structure est un ensemble d'elementsdestines a supporter et a transmettre les charges d'un ouvrage."
  "|Les charges permanentes sont le poids propre des elements ; les charges variables sont la neige, le vent, les personnes et les equipements."
  "|Une structure doit resister, rester stable et presenter une rigidite suffisante pour limiter les deformations."
  "|Les materiaux de construction courants sont le béton, l'acier, le bois, la maçonnerie et le verre."
  "|Le béton resiste bien a la compression mais mal a la traction : on le renforce avec des barres d'acier dans le béton arme."
  "|L'acier resiste a la traction et a la compression, mais il doit etre protege contre la corrosion et le feu."
  "|Le bois est renouvelable et possede un bon rapport resistance sur masse, mais il est sensible a l'humidite et au feu."
  "|Une poutre travaille principalement en flexion : sa partie superieure est comprimee et sa partie inferieure est tendue."
  "|Un poteau travaille principalement en compression ; son elancement peut provoquer un flambement."
  "|Un triangle est une forme intrinsèquement stable : les triangulations rigidifient les charpentes et les ossatures."
  "|Les normes de construction definissent les charges a prendre en compte et les criteres de securite et de durabilite."
  "|Le choix structural arbitre entre resistance, masse, cout, mise en oeuvre, impact environnemental et destination du batiment."),
[QC("Quel materiau resiste surtout a la compression ?", "L'acier~Le béton~Le bois~Le verre", 1,
    "Le béton est performant en compression, d'ou l'ajout d'acier pour la traction."),
 QC("Quel est le role des barres d'acier dans le béton arme ?", "Colorer le béton~Reprendre les efforts de traction~Réduire le poids~Augmenter l'isolation", 1,
    "L'acier reprend la traction que le béton ne supporte pas bien."),
 QC("Comment travaille une poutre en flexion ?", "Toute en traction~En compression en haut et en traction en bas~Toute en compression~Sans contrainte", 1,
    "La fibre superieure est comprimee, la fibre inferieure est tendue."),
 QC("Quel risque pour un poteau tres elance ?", "La corrosion~Le flambement~La traction~La dilatation", 1,
    "Un poteau mince peut perdre sa stabilite par flambement avant d'atteindre sa limite de compression."),
 QC("Pourquoi trianguler une charpente ?", "Pour la rendre plus legere~Pour la rigidifier~Pour la rendre etanche~Pour la decorer", 1,
    "Le triangle est une forme geometriquement indéformable."),
 QC("Quelle est une charge variable ?", "Le poids des murs~La neige sur la toiture~La masse de la dalle~Le poids des fondations", 1,
    "La neige est une charge variable, contrairement au poids propre."),
 QC("Quel critere ne gou-verne pas le choix d'une structure ?", "La resistance~Le cout~L'impact environnemental~La couleur du catalogue", 3,
    "L'esthetique peut intervenir, mais la couleur du catalogue n'est pas un critere d'ingenierie."),
 QT("Expliquer pourquoi le béton arme associe deux materiaux et comment ils cooperent.",
    "Le béton supporte efficacement les efforts de compression et protege l'acier du feu et de la corrosion. L'acier, lui, supporte la traction et la flexion. Dans une poutre en béton arme sous charge, la partie superieure est comprimee par le béton et la partie inferieure est tendue par les barres d'acier. Les deux materiaux ont des dilatations thermiques proches, ce qui evite des contraintes internes importantes lors des variations de temperature. Une bonne adhérence entre l'acier et le béton assure la transmission des efforts. Le concepteur doit aussi prevoir un enrobage suffisant des barres pour garantir la durabilite face a la carbonatation et aux chlorures.",
    "On explique la complementarite compression/traction, l' adherence et la durabilite."),
 QT("Comparer une structure en bois et une structure en acier pour un petit batiment.",
    "Le bois est un materiau renouvelable, avec une faible energie grise et un bon rapport resistance sur masse. Il est facile a mettre en oeuvre avec des assemblages mecaniques, mais il est sensible a l'humidite, au feu et aux insectes ; il necessite des traitements et une protection adaptee. L'acier offre une resistance eleve et une grande capacite de deformation plastique, ce qui est favorable en cas de seisme ; il permet des portees importantes et des elements fins. Ses inconvenient sont une forte energie de production, une sensibilite a la corrosion et un comportement au feu qui exige une protection. Le choix depend du programme, du cout, des normes incendie, de la disponibilite des entreprises et de l'objectif environnemental du projet. Une solution mixte associe souvent les deux materiaux.",
    "On compare resistance, masse, durabilite, feu, cout et impact, sans conclure trop vite.")],
C("Une structure transmet les charges au sol : chaque materiau a un domaine de resistance et des exigences de durabilite.",
  "Poutre : compression en haut, traction en bas · poteau : compression et flambement",
  "Béton, acier, bois · charges permanentes et variables · triangulation",
  "Charge~Effort a supporter~Poutre~Element en flexion~Poteau~Element en compression~Triangulation~Rigidification",
  "Recenser les charges|Preliminer la forme de la structure|Choisir les materiaux|Verifier resistance et stabilite|Traiter durabilite et securite",
  "Oublier les charges variables|Croire que le béton resiste a la traction|Negliger le flambement|Ignorer la protection incendie",
  "Béton arme~Compression et traction~Acier~Traction et ductilité~Bois~Renouvelable et leger~Poutre~Flexion~Poteau~Flambement",
  "Charge permanente~Poids propre~Charge variable~Neige, vent, usagers",
  "Compression~Rapprochement~Traction~Elongation"))

# ============================================================ ARC2
add("ARC2", "Construire durable : isolation et ponts thermiques", "Architecture et construction", ["1re"],
S("Une enveloppe de batiment performante limite les pertes de chaleur en hiver et les apports indesirables en été."
  "|Les parois perdent de la chaleur par conduction a travers les materiaux et par convection aux surfaces."
  "|La resistance thermique R d'une paroi est egale a l'epaisseur divisee par la conductivite du materiau."
  "|Le coefficient U, inverse de R, s'exprime en W/m².K : plus il est petit, mieux la paroi isole."
  "|Les pertes a travers une paroi valent P = U × A × ΔT en regime permanent."
  "|Un pont thermique est une zone ou le flux est plus eleve, par exemple un angle, une dalle ou un linteau."
  "|Les ponts thermiques peuvent provoquer des condensations et des moisissures par refroidissement local de la surface."
  "|Une rupture de pont thermique utilise un materiau isolant ou un element mecanique moins conducteur a la jonction."
  "|L'inertie thermique d'un mur permet de stocker la chaleur et de reduire les variations interieures de temperature."
  "|Uneorientation sud favorable apporte des gains solaires en hiver, mais exige des protections solaires en ete."
  "|L'etancheite a l'air reduit les infiltrations, mais elle doit s'accompagner d'une ventilation controlee."
  "|Le choix de l'isolation arbitre entre performance thermique, epaisseur, cout, recyclabilite et mise en oeuvre."),
[QC("Comment calculer la resistance thermique d'une couche ?", "Conductivite / epaisseur~Epaisseur / conductivite~Epaisseur × conductivite~1 / epaisseur", 1,
    "R = e / lambda, avec lambda la conductivite thermique."),
 QC("Quelle relation entre R et U ?", "U = R~U = 1/R~U = R²~U = R + 1", 1,
    "Le coefficient de transmission U est l'inverse de la resistance R."),
 QC("Que vaut le flux a travers une paroi ?", "P = U A ΔT~P = U/(A ΔT)~P = A ΔT / U~P = U + A + ΔT", 0,
    "Le flux est proportionnel a U, a la surface et a l'ecart de temperature."),
 QC("Quel est un exemple de pont thermique ?", "Le milieu d'un mur bien isole~Une jonction dalle et mur~Une fenetre triple vitrage~Un mur orientation sud", 1,
    "Les jonctions entre elements sont des zones de flux accru."),
 QC("Quel risque d'un pont thermique mal traite ?", "Une surchauffe ete seulement~Une condensation locale~Une baisse du bruit~Une meilleure isolation", 1,
    "La surface froide peut descendre sous le point de rosee et generer de l'humidite."),
 QC("Quel est un role de l'inertie thermique ?", "Supprimer l'isolation~Lisser les variations de temperature~Augmenter les ponts thermiques~Remplacer la ventilation", 1,
    "Une masse importante stocke la chaleur et amortit les ecarts."),
 QC("Pourquoi une maison etanche a t-elle besoin d'une ventilation ?", "Pour augmenter les pertes~Pour renouveler l'air et eviter l'humidite~Pour refroidir le sol~Pour supprimer l'isolation", 1,
    "Sans renouvellement d'air, la qualite de l'air interieur se degrade."),
 QT("Une paroi de 80 m² a U = 0,3 W/m².K et l'ecart de temperature est 18 K. Calculer le flux, puis le flux apres mise en place d'une isolation portant U a 0,15.",
    "Le flux initial vaut P = U × A × ΔT = 0,3 × 80 × 18 = 432 W. Apres isolation, avec U = 0,15, le flux devient 0,15 × 80 × 18 = 216 W. L'economie est de 216 W, soit 50 %. Sur une periode de chauffage de 1500 heures, cela represente 0,216 kW × 1500 h = 324 kWh d'economies pour cette paroi. Ce calcul en regime permanent ne tient pas compte des ponts thermiques, de l'inertie ni des apports solaires ; une etude complete utilise un logiciel de simulation thermique dynamique et controle la qualite de l'air.",
    "On attend le calcul des deux flux, le gain et la liste des limites du calcul simplifie."),
 QT("Expliquer pourquoi traiter les ponts thermiques est aussi important que d'augmenter l'epaisseur de l'isolant.",
    "Si l'isolation principale est performante mais que les jonctions restent conductrices, le flux total est la somme des flux traversant les parois courantes et des flux concentres aux ponts thermiques. Ces derniers peuvent representer une part importante des pertes, surtout dans les petits batiments ou les angles sont nombreux. En outre, un pont thermique refroidit la surface interieure locale, ce qui peut provoquer condensation et moisissure meme si la paroi courante est bien isolée. Augmenter l'epaisseur d'isolant sans traiter les jonctions ameliore peu le confort et peut creates des risques d'humidite. Une bonne conception gere la continuite de l'isolation, les rupteurs de pont thermique et l'etancheite a l'air des la phase d'esquisse, car ces choix sont difficiles a corriger apres le chantier.",
    "On compare l'impact des flux distribues et concentres, avec le risque d'humidite.")],
C("L'enveloppe du batiment se caracterise par U, R, l'inertie et la continuite de l'isolation aux jonctions.",
  "R = e/lambda · U = 1/R · P = U A ΔT",
  "Pont thermique · rupture de pont · inertie · etancheite et ventilation",
  "Resistance R~Isolation de la paroi~Coefficient U~Inverse de R~Pont thermique~Flux local accru~Inertie~Stockage de chaleur",
  "Calculer U et R des parois|Repérer les jonctions a risque|Prevoir des ruptures de pont|Dimensionner la ventilation|Simuler le comportement saisonnier",
  "Confondre R et U|Ignorer les jonctions|Etanchéifier sans ventiler|Choisir l'isolant le plus epais sans verifier la mise en oeuvre",
  "80 m² et 18 K~U=0,3 donne 432 W~U=0,15 donne 216 W~324 kWh economises~R=e/lambda~Dalle et mur~Pont thermique~Point de rosee",
  "Conduction~A travers le materiau~Convection~Par l'air en mouvement",
  "Isolation~Reduit le flux~Inertie~Amortit les variations"))

# ============================================================ ARC3
add("ARC3", "Lire et produire les documents de construction", "Architecture et construction", ["Terminale"],
S("Un projet de construction se documente par des plans, des coupes, des façades et des details d'assemblage."
  "|Le plan de masse situe le batiment sur le terrain avec les limites, les voies et les reseaux."
  "|Un plan d'étage represente une coupe horizontale du batiment a hauteur d'homme, avec murs, ouvertures et circulations."
  "|Une coupe verticale montre les niveaux, les hauteurs, les planchers et la toiture."
  "|Une façade est une projection verticale exterieure qui donne les materiauaux, les menuiseries et les teintes."
  "|Les echelles courantes sont 1/50 pour les plans d'étage, 1/100 pour les coupes et 1/20 pour les details."
  "|Une cote en plan s'exprime en millimetres ou en centimetres et se lit toujours avec l'echelle du document."
  "|Les symboles normalises representent les materiaux, les ouvertures, les escaliers et les equipements."
  "|Le north arrow, ou fleche d'orientation, indique le nord sur le plan de masse et les plans."
  "|Une nomenclature liste les elements avec leurs references, leurs quantites et leurs caracteristiques."
  "|Le descriptif technique precise les performances attendues : isolation, resistance, finitions et normes."
  "|Une maquette numerique (BIM) permet de verifier les collisions entre reseaux et de generer les documents de maniere coherente."),
[QC("Que represente un plan d'étage ?", "Une vue du toit~Une coupe horizontale a hauteur d'homme~Une coupe verticale~Une vue de facade", 1,
    "Le plan d'étage est une section horizontale a environ 1 m du sol."),
 QC("Quel document montre les niveaux et les planchers ?", "Le plan de masse~La coupe~La facade~Le detail", 1,
    "La coupe verticale donne les hauteurs et les niveaux."),
 QC("Quelle echelle convient a un detail d'assemblage ?", "1/1000~1/100~1/20~1/500", 2,
    "Un detail se dessine a grande echelle, par exemple 1/20 ou 1/10."),
 QC("Que donne la fleche d'orientation ?", "La direction du vent~Le nord du plan~La pente de la toiture~La hauteur du batiment", 1,
    "La fleche d'orientation indique le nord, indispensable pour l'etude solaire."),
 QC("Quel est le role d'une nomenclature ?", "Donner les couleurs~Lister les elements, quantites et references~Remplacer les plans~Indiquer le prix total", 1,
    "La nomenclature accompagne les plans et sert au chiffrage."),
 QC("Quel est un avantage du BIM ?", "Supprimer les plans~Detecter les collisions entre reseaux~Remplacer les normes~Augmenter les couts", 1,
    "La maquette numerique coordonne les elements et revele les interferences."),
 QC("Que contient le descriptif technique ?", "Les performances et les normes attendues~Seulement les couleurs~Le nom de l'architecte~La date du chantier", 0,
    "Il definit les caracteristiques techniques et les exigences de mise en oeuvre."),
 QT("Décrire la demarche pour lire un plan d'étage et situer une piece par rapport à l'orientation solaire.",
    "On commence par identifier l'echelle du plan et la fleche d'orientation, puis on repere l'entre du batiment, les circulations et les pieces. On lit les cotes pour connaitre les dimensions et l'epaisseur des murs. On observe la position des ouvertures : une piece avec de grandes fenetres au sud recevra des apports solaires importants en hiver et necessitera une protection solaire en ete, tandis qu'une facade nord recevra peu de soleil direct. On croise ensuite avec la coupe pour connaitre les hauteurs et avec le plan de masse pour verifier les ombres portées par les batiments voisins. On peut alors porter un jugement sur le confort de la piece et proposer des amendements avant le chantier.",
    "On attend echelle, orientation, cotes, ouvertures, croisement avec la coupe et consequences."),
 QT("Expliquer pourquoi une maquette BIM reduit les erreurs par rapport a des plans 2D separes.",
    "Dans une approche 2D, le plan, la coupe et les plans de fluides sont dessines separement : une modification de l'un n'est pas automatiquement reportee sur les autres, et un conduit peut traverser une poutre sans que personne ne s'en apercoive avant le chantier. Dans une maquette BIM, tous les elements sont representes dans un modele 3D unique et les vues en sont extraites automatiquement. Si un mur est deplace, les plans et les coupes se mettent a jour. Les outils de detection de collisions signalent les intersections entre gaines, poutres et equipements. Les quantites sont egalement calculees a partir du modele, ce qui fiabilise le chiffrage. Le BIM ne remplace pas la reflexion de conception, mais il rend la documentation coherente et verifiable.",
    "On oppose coherence automatique et risque de contradiction des plans separes.")],
C("Plans, coupes, façades et nomenclature forment un ensemble coherent ; le BIM en assure la mise a jour commune.",
  "Plans d'étage : coupe horizontale · coupes : niveaux · façades : projection",
  "Echelles 1/50, 1/100, 1/20 · orientation · nomenclature · BIM",
  "Plan d'étage~Coupe horizontale~Coupe~Niveaux et hauteurs~Facade~Projection exterieure~Nomenclature~Liste des elements",
  "Lire l'echelle et l'orientation|Repérer pieces et circulations|Croiser plan, coupe et facade|Verifier les cotes et symboles|Detecter les incoherences",
  "Oublier l'echelle d'un document|Confondre plan et coupe|Ignorer l'orientation solaire|Ne pas mettre a jour la nomenclature",
  "1/50~Plan d'étage~1/100~Coupe~1/20~Detail~Fleche nord~Orientation~BIM~Detection de collisions",
  "Plan~Vue horizontale~Coupe~Vue verticale interieure",
  "Descriptif~Performances attendues~Nomenclature~Quantites et references"))

# ============================================================ ARC4
add("ARC4", "Assemblages, charpentes et mise en oeuvre", "Architecture et construction", ["Terminale"],
S("Le choix d'un assemblage depend des materiaux, des efforts a transmettre et des contraintes de chantier."
  "|Une charpente traditionnelle en bois associe des elements jeux, chevrons et pannes relies par des assemblages."
  "|Les assemblages mecaniques (boulons, vis, connecteurs) sont demontables et verifiables sur chantier."
  "|Les assemblages par collage ou par soudage sont plus rigides mais rendent le demontage difficile."
  "|Une charpente metallique utilise des profiles ouverts ou tubulaires, relies par des boulons ou des soudures."
  "|Les ossatures en béton arme sont coulees sur place ou prefabriquees en usine."
  "|La prefabrication ameliore la qualite et la rapidite de pose, mais exige une logistique et des tolerances strictes."
  "|Une charpente doit transmettre les charges de toiture jusqu'aux fondations sans deformation excessive."
  "|Le contreventement assure la stabilite horizontale de l'ossature face au vent et aux actions sismiques."
  "|Les tolerances de mise en oeuvre definissent les ecarts admissibles de position et de dimension."
  "|Un defaut d'alignement peut empecher le montage ou creer des contraintes supplémentaires dans les assemblages."
  "|La securite sur chantier impose des procedures de levage, d'etaiment et de protection collective."),
[QC("Quel est un avantage des assemblages mecaniques ?", "Ils sont definitifs~Ils sont demontables et controlables~Ils suppriment les efforts~Ils coutent toujours moins cher", 1,
    "Les boulons et vis permettent le demontage et la verification."),
 QC("Quel element assure la stabilite horizontale d'une ossature ?", "Le contreventement~Le revetement~L'isolation~La menuiserie", 0,
    "Le contreventement reprend les efforts horizontaux de vent ou de seisme."),
 QC("Quel est un inconvenient de la prefabrication ?", "Une qualite moindre~Des exigences de logistique et de tolerance~Une pose plus lente sur place~Une structure plus legere", 1,
    "Les elements prefabriques doivent arriver a temps et etre poses avec precision."),
 QC("Que sont des chevrons dans une charpente bois ?", "Des elements de couverture inclines~Des fondations~Des isolants~Des fixations", 0,
    "Les chevrons sont des elements porteurs de la toiture."),
 QC("Que peut provoquer un defaut d'alignement ?", "Une meilleure étanchéité~Un blocage du montage ou des contraintes~Une baisse de charge~Aucun effet", 1,
    "Les pieces ne s'assemblent plus ou travaillent mal."),
 QC("Que definit une tolerance de mise en oeuvre ?", "La couleur de la finition~L'ecart admissible de position ou de dimension~Le prix de la main-d'oeuvre~La duree du chantier", 1,
    "La tolerance fixe la limite acceptable entre theorie et realite."),
 QC("Quelle phase du chantier exige un etaiement ?", "La peinture~Le montage d'elements provisoirement instables~La livraison~Le nettoyage", 1,
    "L'etaiement maintient la stabilite pendant le montage."),
 QT("Comparer une charpente bois boulonnee et une charpente metallique soudee pour un abri de jardin.",
    "La charpente bois boulonnee utilise des elements renouvelables, une mise en oeuvre avec outils simples et des assemblages demontables. Elle est leger, ce qui facilite la pose, mais demande une protection contre l'humidite, les insectes et le feu, et sa section est plus importante qu'en acier. La charpente metallique soudee offre des sections plus fines et une grande rigidite, mais la soudure exige un savoir-faire et un controle, l'acier doit etre traite contre la corrosion et protege au feu. Elle est generalement plus lourde a manipuler et son impact de production est plus eleve. Pour un abri de jardin, le bois boulonne est souvent plus simple et plus durable dans une logique d'eco-conception, tandis que l'acier convient mieux aux portees importantes ou aux contraintes dimensionnelles fortes.",
    "On compare materiau, assemblage, competences, durabilite, cout et impact."),
 QT("Expliquer pourquoi la tolerance de fabrication doit etre choisie avec le monteur et pas seulement par le concepteur.",
    "Une tolerance trop serrée impose des moyens de fabrication precis et couteux, alors que la piece pourrait remplir son role avec un ecart plus large. Une tolerance trop large, elle, peut rendre l'assemblage impossible sur chantier : les trous ne tombent plus en face, les angles ne ferment pas ou les joints sont trop visibles. Le monteur connait les contraintes reelles de pose, la dilatation des materiaux sur le chantier et les capacites des outils disponibles. Le concepteur connait les besoins fonctionnels de la structure. Les definir ensemble permet de trouver un compromis fabricable, verifiable et economicalement acceptable. Cette concertation est une illustration directe de la demarche de projet en STI2D.",
    "On equilibre cout de fabrication, assemblabilite et exigence fonctionnelle, avec le role de chaque acteur.")],
C("Une charpente assemble des elements porteurs : le choix des assemblages et des tolerances conditionne la pose et la durabilite.",
  "Charges de toiture → charpente → poteaux → fondations",
  "Assemblages mecaniques ou soudes · contreventement · prefabrication · tolerances",
  "Charpente~Structure de toiture~Assemblage~Liaison entre elements~Contreventement~Stabilite horizontale~Tolerance~Ecart admissible",
  "Identifier les charges et les portees|Choisir materiau et type d'assemblage|Prevoir contreventement et stabilite|Definir tolerances avec le monteur|Planifier securite et levage",
  "Sous-estimer les efforts horizontaux|Choisir une soudure pour un assemblage demontable|Imposer des tolerances inutiles|Negliger l'etaiement pendant la pose",
  "Abri de jardin~Bois boulonne ou acier soude~Contreventement~Vent et seisme~Tolerance~Ecart admissible~Prefabrication~Logistique",
  "Assemblage mecanique~Demontable~Assemblage soude~Rigide et permanent",
  "Charpente bois~Renouvelable~Charpente acier~Portees importantes"))

# ============================================================ SIN1
add("SIN1", "Architecture d'un systeme d'information industriel", "Systèmes d'information et numérique", ["1re"],
S("Un systeme d'information (SI) collecte, traite, stocke et diffuse des donnees pour piloter une organisation."
  "|Dans une entreprise, le SI relie la production, la maintenance, la qualite, la logistique et la gestion commerciale."
  "|Les composants d'un SI sont les donnees, les logiciels, les equipements, les reseaux, les processus et les personnes."
  "|Une architecture en couches separe la couche physique, la couche reseau, la couche applicative et la couche metier."
  "|Un systeme ERP integre les fonctions de gestion autour d'une base de donnees commune."
  "|Un systeme MES (Manufacturing Execution System) suit et pilote la production en temps reel."
  "|Une base de donnees relationnelle organise les donnees en tables liees par des cles primaires et etrangeres."
  "|Un modele de donnees decrit les entites, leurs attributs et leurs relations avant l'implementation."
  "|Les API permettent a deux applications d'echangeer des donnees et des services de maniere normalisee."
  "|La qualite de la donnee (exactitude, completude, fraicheur, coherence) conditionne lafiabilite des decisions."
  "|La redondance et les sauvegardes assurent la disponibilite du systeme en cas de panne."
  "|Un SI industriel doit aussi respecter des exigences de securite, de traçabilité et de conformite reglementaire."),
[QC("Quelle est une fonction d'un systeme d'information ?", "Dessiner les plans~Collecter, traiter et diffuser des donnees~Remplacer les capteurs~Fabricuer les pieces", 1,
    "Le SI gere le cycle de vie de l'information dans l'organisation."),
 QC("Quel systeme pilote la production en temps reel ?", "Un ERP~Un MES~Un CRM~Un outil de paie", 1,
    "Le MES suit les operations de fabrication et remonte les donnees de terrain."),
 QC("Quel role joue une cle primaire ?", "Identifier uniquement chaque enregistrement~Chiffrer la base~Trier les colonnes~Supprimer les doublons automatiquement", 0,
    "La cle primaire identifie de maniere unique chaque ligne d'une table."),
 QC("Quel est un composant d'un SI ?", "Une seule application~Les donnees, les reseaux et les personnes~Le seul serveur~Le batiment", 1,
    "Un SI associe donnees, logiciels, equipements, reseaux, processus et personnes."),
 QC("Que permet une API ?", "Remplacer la base de donnees~Faire communiquer deux applications~Supprimer les utilisateurs~Augmenter la memoire", 1,
    "L'API definit les services et les formats d'echange entre applications."),
 QC("Quelle qualite de donnee concerne la date de dernière mise a jour ?", "L'exactitude~La fraicheur~La coherence~La completude", 1,
    "La fraicheur indique depuis quand la donnee est a jour."),
 QC("Quel moyen assure la disponibilite en cas de panne ?", "La redondance et les sauvegardes~Le seul mot de passe~La suppression des journaux~Le ralentissement du reseau", 0,
    "Redondance et sauvegardes permettent la reprise apres defaillance."),
 QT("Décrire les couches d'une architecture d'information pour une petite entreprise de fabrication.",
    "La couche physique comprend les serveurs, les postes, les automates, les capteurs et le cablage. La couche reseau assure les liaisons avec les switchs, les routeurs, les VLAN et les liens vers l'exterieur, avec le WiFi pour certains equipements. La couche applicative contient les logiciels : ERP pour la gestion, MES pour le suivi de production, outils de supervision, messagerie et outils collaboratifs. La couche metier porte les regles de l'entreprise : gestion des commandes, plans de fabrication, procedures qualite et indicateurs de performance. Les donnees circulent du terrain vers la base commune, puis les indicateurs sont restitues aux differents services. Chaque couche doit etre documentee et securisee, avec des droits adaptes aux utilisateurs.",
    "On decrit les quatre couches et les flux entre elles avec des exemples d'entreprise."),
 QT("Expliquer pourquoi la qualite des donnees est plus critique dans un SI industriel que dans un outil personnel simple.",
    "Dans un outil personnel, une donnee erronee concerne une seule personne, qui peut souvent la corriger sans consequence grave. Dans un SI industriel, la meme donnee alimente plusieurs applications : une reference erronée peut declencher une commande d'achat, arreter une machine ou fausser un indicateur de qualite. Les effets se propagent rapidement et peuvent toucher la production, la securite et la relation client. C'est pourquoi on definit des regles de validation a la saisie, des controles de coherence, des droits en ecriture et des procedures de correction tracees. On mesure aussi la fraicheur des donnees, car une information exacte mais obsolete peut conduire a une mauvaise decision. La fiabilite du SI repose donc autant sur les processus humains que sur les outils techniques.",
    "On relie propagation des erreurs, effets industriels et mesures de qualite.")],
C("Un systeme d'information relie donnees, applications, reseaux et personnes pour piloter l'organisation.",
  "SI = donnees + logiciels + equipements + reseaux + processus + personnes",
  "ERP / MES · couches physique, reseau, applicative, metier · qualite de donnee",
  "Systeme d'information~Collecte et diffusion~ERP~Gestion integree~MES~Pilotage de production~Base de donnees~Tables et cles",
  "Recenser les besoins des services|Modeleer les donnees et les flux|Choisir les applications|Securiser les acces et les echanges|Surveiller la qualite et la disponibilite",
  "Confondre ERP et MES|Negliger la qualite des donnees|Oublier les utilisateurs dans l'architecture|Laisser des acces sans trace",
  "ERP~Commandes et stocks~MES~Production en temps reel~Cle primaire~Identifiant unique~API~Echange normalise~Fraicheur~Date de mise a jour",
  "ERP~Fonctions de gestion~MES~Execution de production",
  "Couche reseau~Liaisons~Couche applicative~Logiciels"))

# ============================================================ SIN2
add("SIN2", "Reseaux industriels et protocoles de communication", "Systèmes d'information et numérique", ["1re"],
S("Un reseau industriel relie les automates, les capteurs, les actionneurs et les postes de supervision."
  "|Les bus de terrain comme Modbus, Profibus ou CANopen permettent d'echanger des donntes entre automates et equipements."
  "|Modbus est un protocole simple et ouvert, avec une architecture maitre-esclave et des registres lus ou ecrits."
  "|Une architecture dereseau industrielle classique separe le niveau terrain, le niveau controle et le niveau supervision."
  "|Les switchs industriels sont durcis : ils supportent des plages de temperature et des vibrations plus larges que les switchs de bureau."
  "|La redondance des liens et des alimentations ameliore la disponibilite de la production."
  "|Les protocoles industriels doivent garantir une determinisme : une commande doit arriver dans un delai connu."
  "|Le protocole Ethernet industriel utilise des priorites de trames pour limiter les temps de reponse variables."
  "|La segmentation en VLAN separe la production, la supervision, la maintenance et le reseau administratif."
  "|Une passerelle traduit les protocoles entre le terrain et le reseau IP de l'entreprise."
  "|Les equipements industriels ont souvent une duree de vie longue : la compatibilité avec d'anciens protocoles est un enjeu frequent."
  "|La documentation des adresses, des registres et des cablages est indispensable pour la maintenance."),
[QC("Que permet un bus de terrain ?", "Relier automates et equipements~Remplacer l'alimentation~Stocker les plans~Augmenter la temperature", 0,
    "Le bus de terrain transporte les donnees entre les equipements de production."),
 QC("Quel est le mode d'echange de Modbus classique ?", "Pair a pair~Maitre et esclaves~Broadcast sans reponse~Sans adresse", 1,
    "Un maitre interroge des esclaves qui repondent avec leurs registres."),
 QC("Quel niveau relie les capteurs a l'automate ?", "Le niveau supervision~Le niveau terrain~Le niveau administratif~Le cloud uniquement", 1,
    "Le niveau terrain regroupe capteurs, actionneurs et automates."),
 QC("Quelle est une caracteristique d'un switch industriel ?", "Il resiste a des conditions d'environnement plus dures~Il ne consume rien~Il n'a pas de ports~Il remplace l'automate", 0,
    "Les switchs industriels sont durcis en temperature, vibrations et alimentation."),
 QC("Que designe le determinisme dans un reseau industriel ?", "Une reponse dans un delai connu~Une reponse au hasard~Un tres grand debit~L'absence de cablage", 0,
    "La maitrise du temps de reponse est essentielle pour la commande en boucle fermee."),
 QC("Quel role joue une passerelle ?", "Augmenter la tension~Traduire entre protocoles differentes~Supprimer les donnees~Remplacer le serveur", 1,
    "La passerelle fait l'interface entre bus de terrain et reseau IP."),
 QC("Pourquoi segmenter un reseau industriel ?", "Pour reduire les cablages~Pour isoler la production des autres reseaux~Pour supprimer les automates~Pour changer les adresses", 1,
    "La segmentation limite les risques et les perturbations entre services."),
 QT("Expliquer la difference entre un reseau administratif et un reseau de production, et pourquoi les separer.",
    "Le reseau administratif transporte les donnees de gestion : messagerie, documents, ERP, acces Internet. Le reseau de production transporte les communications entre automates, capteurs et postes de supervision, avec des exigences de determinisme et de disponibilite. Les deux ont des besoins differents : une panne du reseau administratif gene les employes, alors qu'une panne du reseau de production arrete la machine. Les separer permet d'eviter qu'une saturation, un virus ou une mise a jour du reseau administratif perturbe la commande des equipements. La separation se fait par des VLAN et des pare-feu, avec des passerelles controlees pour les echanges necessaires. Cette architecture est un element central de la securite industrielle.",
    "On oppose besoins et consequences d'une panne, puis on justifie VLAN et passerelles."),
 QT("Un automate ne repond plus aux requetes de supervision. Décrire une demarche de diagnostic structuree.",
    "On verifie d'abord l'alimentation et les voyants de l'automate et du switch, puis le cablage et les connecteurs. On teste la continuite physique et l'adresse IP de l'equipement avec un ping depuis le poste de supervision. On controle ensuite les paramètres du protocole : identifiant d'esclave, registre interroge, baud ou vitesse de liaison, et correspondance entre la configuration et le programme. On consulte les journaux de l'automate et du switch pour detecter des erreurs de trame ou des collisions. Si le probleme persiste, on isole l'equipement sur un banc de test avec un cablage minimal pour determine si la panne vient de l'automate, du bus ou de la supervision. Chaque etape et son resultat sont consignes dans un compte rendu de maintenance.",
    "On suit l'ordre alimentation, physique, adressage, protocole, journaux, isolement et documentation.")],
C("Un reseau industriel transporte des donnees de commande avec des exigences de delai et de disponibilite.",
  "Niveaux terrain, controle, supervision · maitre/esclave · determinisme",
  "Modbus, Profibus, CANopen · switchs durcis · VLAN · passerelles",
  "Bus de terrain~Liaison entre equipements~Automate~Controleur~Supervision~Vue globale~Passerelle~Traduction de protocole",
  "Cartographier les equipements et les liens|Segmenter les reseaux|Configurer adresses et registres|Verifier les delais de reponse|Documenter pour la maintenance",
  "Melanger reseau administratif et production|Ignorer les delais de reponse|Oublier la redondance des alimentations|Ne pas documenter les registres",
  "Modbus~Maitre et esclaves~Adresse IP~Test par ping~VLAN~Separation des flux~Passerelle~Traduction~Journaux~Diagnostic",
  "Reseau administratif~Gestion et bureautique~Reseau de production~Commande et supervision",
  "Determinisme~Delai connu~Temps variable~Difficulté de commande"))

# ============================================================ SIN3
add("SIN3", "Acquisition de donnees et supervision de procedes", "Systèmes d'information et numérique", ["Terminale"],
S("Un systeme d'acquisition de donnees convertit des signaux physiques en donnees exploitables par un ordinateur."
  "|Une chaine d'acquisition comprend le capteur, le conditionnement, le convertisseur analogique-numerique et le logiciel de traitement."
  "|Une carte d'acquisition, ou DAQ, regroupe plusieurs entrees analogiques ou numeriques et une interface vers l'ordinateur."
  "|La frequence d'echantillonnage determine le nombre de mesures preleves par seconde."
  "|Selon le theoreme de Shannon, la frequence d'echantillonnage doit etre au moins le double de la frequence maximale du signal."
  "|Un sous-echantillonnage provoque un repliement : un signal rapide est pris pour un signal plus lent."
  "|Un logiciel de supervision (SCADA) affiche l'etat des equipements, les mesures et les alarmes en temps reel."
  "|Une IHM (interface homme-machine) presente les donnees sous forme de synoptiques, de courbes et de voyants."
  "|Les alarmes sont definies par des seuils et des priorites, avec des acquittements par les operateurs."
  "|L'historisation enregistre les mesures dans une base de donnees pour permettre l'analyse apres coup."
  "|Les tendances et les statistiques extraites de l'historique aident a la maintenance predictive."
  "|Une horodatation coherente de toutes les donnees est necessaire pour correlér les evenements entre equipements."),
[QC("Quel element convertit un signal analogique en nombre ?", "Le capteur~Le convertisseur analogique-numerique~L'alimentation~Le visualiseur", 1,
    "Le CAN echantillonne et quantifie le signal electrique."),
 QC("Quelle frequence minimale pour un signal de 200 Hz ?", "100 Hz~200 Hz~400 Hz~800 Hz", 2,
    "Le critere de Shannon impose au moins 2 × 200 = 400 Hz."),
 QC("Quel effet d'un sous-echantillonnage ?", "Une meilleure precision~Un repliement du signal~Une alarmee en moins~Aucun effet", 1,
    "Le repliement fait apparaitre une frequence erronee plus basse."),
 QC("Que fait un logiciel SCADA ?", "Remplacer l'automate~Superviser equipements, mesures et alarmes~Coder le programme~Fabriquer les capteurs", 1,
    "Le SCADA collecting les donnees et presente l'etat du procede a l'operateur."),
 QC("Quel est le role d'une IHM ?", "Fournir l'energie~Presenter les donnees a l'operateur~Stocker les plans~Protéger le reseau", 1,
    "L'IHM est l'interface de dialogue entre l'operateur et le systeme."),
 QC("A quoi sert l'historisation ?", "Supprimer les anciennes mesures~Conserver les donnees pour analyse ulterieure~Augmenter le nombre de capteurs~Reduire la precision", 1,
    "L'historique permet l'analyse des tendances et des incidents."),
 QC("Pourquoi horodater les donnees ?", "Pour les rendre plus belles~Pour correlér les evenements entre equipements~Pour reduire leur taille~Pour changer d'unite", 1,
    "Sans horodatation commune, les evenements ne peuvent pas etre compares."),
 QT("Une chaine d'acquisition doit mesurer une vibration de 500 Hz. Justifier le choix d'une frequence d'echantillonnage de 2000 Hz.",
    "Selon Shannon, il faut au moins 2 × 500 = 1000 echantillons par seconde pour reconstruire le signal sans repliement. Choisir 2000 Hz donne une marge de sécurité d'un facteur 4 par rapport a la frequence du signal. Cette marge est utile car les signaux reels ne sont pas parfaitement sinusoidaux : ils contiennent des harmoniques a 1000 Hz ou plus qu'il faut egalement echantillonner. Un filtre passe-bas avant le CAN limite les frequences au-dessus de 1000 Hz pour eviter le repliement des bruits. Le choix de 2000 Hz augmente le volume de donnees a stocker et la charge du processeur, mais il garantit une bonne representation de la vibration pour l'analyse spectrale.",
    "On applique Shannon, on evoque les harmoniques, le filtrage et le compromis volume de donnees."),
 QT("Décrire les informations qu'un operateur doit trouver sur une IHM de supervision et comment les structurer.",
    "L'IHM doit presenter un synoptique du procede avec les equipements principaux et leur etat en temps reel : marche, arret, defaut. Les mesures essentielles apparaissent sous forme de valeurs numeriques et de courbes de tendance pour voir l'evolution. Les alarmes sont regroupees par priorite, avec l'heure de declenchement, le message comprehensible et la procedure d'acquittement. L'operateur doit pouvoir acceder aux donnees historisees, aux rapports de production et aux etats des actionneurs. La structure suit la hierarchie du procede : vue globale, puis vue par atelier, puis detail de chaque equipement. Les couleurs doivent rester coherentes et limitées, et les zones critiques doivent etre visibles sans navigation excessive, notamment en cas d'urgence.",
    "On attend etat des equipements, mesures, alarmes, historique et hierarchie de navigation.")],
C("La supervision transforme des signaux en information pour l'operateur : echantillonnage, alarmes et historique sont les trois piliers.",
  "fe >= 2 fmax · echantillonnage puis quantification",
  "Chaine capteur, conditionnement, CAN, SCADA, IHM, historisation",
  "Acquisition~Du signal a la donnee~Echantillonnage~Prelevements par seconde~SCADA~Supervision du procede~IHM~Interface avec l'operateur",
  "Choisir la frequence d'echantillonnage|Filtrer les frequences non utiles|Configurer les alarmes et priorites|Construire les synoptiques|Historiser et analyser les tendances",
  "Echantillonner sous 2 fmax|Oublier le filtre avant conversion|Multiplier les alarmes sans priorite|Ne pas horodater les donnees",
  "500 Hz~fe minimale 1000 Hz~Choix 2000 Hz~Facteur 4~Filtre passe-bas~Suppression des harmoniques~Historique~Analyse des tendances",
  "SCADA~Surveiller et commander~IHM~Dialoguer avec l'operateur",
  "Repliement~Signal mal interprete~Sur-echantillonnage~Donnees plus nombreuses"))

# ============================================================ SIN4
add("SIN4", "Cybersecurite des systemes industriels", "Systèmes d'information et numérique", ["Terminale"],
S("La securite des systemes industriels vise a proteger la production contre les attaques et les defaillances."
  "|Les enjeux sont la disponibilite de la production, l'integrite des commandes et la confidentialite des donnees."
  "|Un systeme industriel est souvent plus fragile qu'un systeme bureautique car ses equipements sont anciens et difficilement patchables."
  "|Une attaque peut detourner une commande, arreter une ligne, voler des donnees ou utiliser la production comme point d'entree."
  "|La segmentation reseau separe la production, la supervision, la maintenance et le reseau administratif."
  "|Une zone DMZ accueille les services qui doivent etre accessibles depuis l'exterieur sans exposer directement la production."
  "|Le moindre privilegie limite les droits de chaque compte et de chaque equipement au strict necessaire."
  "|Les acces distants a la maintenance doivent etre authentifies, traces et fermes hors des interventions."
  "|Les mises a jour sont testees sur un environnement de recette avant application sur les automates."
  "|Une sauvegarde des programmes d'automates et des configurations est indispensable a la reprise apres incident."
  "|La supervision des journaux permet de detecter des comportements anormaux et de reconstituer une attaque."
  "|Un plan de réponse a incident definit les responsabilites, les etapes de confinement et les critères de reprise."),
[QC("Quel est l'enjeu prioritaire d'un systeme industriel ?", "La seule confidentialite~La disponibilite de la production~Le nombre de mots de passe~La couleur des synoptiques", 1,
    "L'arret de production est souvent le risque le plus couteux."),
 QC("Quel est un moyen de limiter la propagation d'une attaque ?", "Partager tous les mots de passe~La segmentation reseau~Supprimer les journaux~Connecter l'automate a Internet", 1,
    "La segmentation isole les zones et freine le deplacement lateral."),
 QC("A quoi sert une DMZ ?", "A héberger les postes de direction~A exposer des services sans exposer la production~A stocker les sauvegardes hors ligne~A remplacer le pare-feu", 1,
    "La DMZ accueille les services accessibles de l'exterieur, separes de la production."),
 QC("Que designe le moindre privilegie ?", "Un droits illimite pour tous~Des droits limites au strict necessaire~Aucun droit~Un droit identique pour tous les postes", 1,
    "Chaque compte ou equipement recoit uniquement les droits utiles a son role."),
 QC("Que faut-il faire avant de patcher un automate ?", "Appliquer directement en production~Tester en recette et prevoir un retour arriere~Supprimer la sauvegarde~Arreter la supervision", 1,
    "Un correctif mal testé peut arreter la production ; une sauvegarde est indispensable."),
 QC("Quel element aide a reconstituer une attaque ?", "Les journaux horodates~Le synoptique~Le plan de masse~La nomenclature", 0,
    "Les journaux consignent les evenements et permettent l'analyse forensique."),
 QC("Quel doit etre le statut d'un acces de maintenance distant ?", "Permanent et sans trace~Authentifie, trace et ferme apres intervention~Partage entre collègues~Toujours ouvert vers Internet", 1,
    "Un acces durable et non trace est une porte d'entree durable."),
 QT("Expliquer pourquoi un systeme industriel necessite une approche de securite differente de celle d'un reseau bureautique.",
    "Un reseau bureautique peut souvent etre redemarre ou reinstalle rapidement ; un automate industriel pilote des machines dont l'arret coute cher et qui peuvent presenter des risques physiques. Les equipements industriels ont une duree de vie de quinze a vingt ans, avec des systemes d'exploitation anciens qui ne recoivent plus de correctifs. Les protocoles de terrain sont souvent sans authentification ni chiffrement. Une mise a jour comme simple redemarrage peut perturber une production continue. La securite industrielle privilegie donc d'abord la disponibilite et l'integrite des commandes, avec segmentation, durcissement, controle strict des acces distants et tests en recette. La confidentialite reste importante, mais elle ne prime pas sur la securite physique des personnes et des installations.",
    "On oppose duree de vie, consequences physiques et priorite a la disponibilite."),
 QT("Décrire la reponse a une alerte indiquant une commande anormale sur une ligne de production.",
    "On qualifie d'abord l'alerte : est-ce une erreur de capteur, une action legitimate ou une commande suspecte ? On compare l'heure et la source de la commande avec les journaux de l'automate, du SCADA et des comptes d'acces. Si l'incident est confirme, on passe en mode securise, par exemple en passant la ligne en arret programmé et en coupant les acces distants, sans detruire les journaux. On conserve les preuves avec horodatage et on identifie la source de la commande. On restaure ensuite la configuration de reference a partir d'une sauvegarde saine, on verifie l'integrite des programmes d'automates et on remet la ligne en service apres validation par la production. Un retour d'experience documente la cause, les actions correctives et les changements de regles de detection.",
    "On suit qualification, confinement, preuves, restauration, reprise et retour d'experience.")],
C("La securite industrielle protege d'abord la disponibilite et l'integrite des commandes par segmentation, controle des acces et sauvegardes.",
  "CIA industriel : disponibilite, integrite, confidentialite",
  "Segmentation · DMZ · moindre privilegie · recette et sauvegardes · journaux",
  "Disponibilite~Production en marche~Integrite~Commandes non modifiees~Segmentation~Isolement des zones~Journal~Trace des evenements",
  "Cartographier les actifs et les flux|Segmenter et durcir les acces|Tester les changements en recette|Superviser les journaux|Sauvegarder et preparer la reprise",
  "Connecter un automate directement a Internet|Laisser un acces de maintenance permanent|Patchers sans test|Effacer les journaux apres incident",
  "DMZ~Services exterieurs~Moindre privilegie~Droits minimaux~Automate~Equipement ancien~Recette~Environnement de test~Sauvegarde~Reprise",
  "Reseau bureautique~Redemarrage facile~Reseau industriel~Arret couteux et risque physique",
  "Confinement~Isoler sans detruire~Restauration~Revenir a un etat sain"))

# ============================================================ MEP1
add("MEP1", "Cadrage d'un projet et definition des livrables", "Méthodologie de projet", ["1re"],
S("Un projet est une entreprise temporaire qui mobilise des ressources pour atteindre un objectif precis."
  "|Le cadrage definit le pourquoi, le quoi, le qui, le quand, le combien et les criteres de reussite du projet."
  "|Le cahier des charges projet formalise le besoin, les objectifs, les contraintes et les livrables attendus."
  "|Un livrable est un element concret produit et remis : plan, modele, prototype, rapport, maquette ou logiciel."
  "|Une phase, ou jalon, marque une etape importante avec une date et des criteres d'acceptation."
  "|Les parties prenantes sont les personnes ou organismes qui influencent le projet ou en sont affectes."
  "|Le maitre d'ouvrage exprime le besoin et valide le resultat ; le maitre d'oeuvre realise la solution."
  "|Les exigences doivent etre verifiables : une formulation vague comme « rapide » doit être traduite en valeur mesurable."
  "|Unehypothese est une affirmation prise pour vraie au depart et qui doit etre confirmee au cours du projet."
  "|Le planning identifie les taches, leur duree, leurs dependances et les ressources necessaires."
  "|Le budget estime les couts de matiere, d'equipement, de main-d'oeuvre et de sous-traitance."
  "|Une revue de cadrage permet de valider le projet avant d'engager les moyens de realisation."),
[QC("Quel est unlivrable de projet ?", "Une idee non ecrite~Un rapport ou un prototype remis~Une reunion~Une contrainte", 1,
    "Un livrable est un element concret et verifiable remis au commanditaire."),
 QC("Quel est le role du maitre d'ouvrage ?", "Realiser la solution~Exprimer le besoin et valider le resultat~Repairer les machines~Ecrire le code", 1,
    "Le maitre d'ouvrage porte le besoin et accepte le livrable."),
 QC("Comment rendre une exigence verifiable ?", "En la traduisant en valeur mesurable~En la laissant vague~En la repetant~En la datant seulement", 0,
    "Une exigence doit etre mesurable pour etre validee."),
 QC("Qu'est-ce qu'un jalon ?", "Une tache quotidienne~Une etape importante avec critere d'acceptation~Un outil~Un risque", 1,
    "Le jalon marque une etape decisive du projet."),
 QC("Quelles ressources faut-il estimer ?", "Matiere, equipements, temps et competences~Seulement l'argent~La couleur des diapositives~Le nombre de reunions", 0,
    "Le budget et le planning reposent sur tous ces elements."),
 QC("Que faire d'une hypothese non confirmee ?", "La supprimer silencieusement~La mettre a jour et en mesurer l'impact~La considerer comme vraie~L'ignorer", 1,
    "Une hypothese doit etre revue et sa remise en cause documentee."),
 QC("A quoi sert la revue de cadrage ?", "A changer le titre du projet~A valider le projet avant d'engager les moyens~A remplacer le planning~A supprimer les livrables", 1,
    "La revue verifie la coherence du cadrage avant le lancement."),
 QT("Décrire le cadrage d'un projet de station de recharge solaire pour un campus.",
    "Le pourquoi : offrir une recharge electrique aux vélos et petits vehicules du campus en utilisant l'energie solaire, dans le cadre d'une demarche de developpement durable. Le quoi : un prototype de station avec panneau, batterie, regulation de charge et deux prises, accompagne de plans, d'un cahier des charges, d'un rapport d'essais et d'une maquette. Le qui : un maitre d'ouvrage representé par la direction du campus, une equipe etudiante maitre d'oeuvre, un enseignant tuteur et un technicien pour les essais. Le quand : cadrage en septembre, conception en octobre, realisation en novembre, essais et soutenance en decembre. Le combien : budget limite avec matiere, electronique et impression 3D. Les criteres de reussite sont la puissance disponible, l'autonomie, la securite electrique et la qualite des documents livrés. Les hypotheses sur l'ensoleillement et l'usage reel doivent etre verifyes par des mesures.",
    "On retrouve les six questions du cadrage et des criteres mesurables."),
 QT("Expliquer la difference entre exigence fonctionnelle et contrainte, puis donner un exemple de chacune dans un projet.",
    "Une exigence fonctionnelle decrit un service attendu du produit : par exemple, la station doit fournir une tension de 12 V continue sous 5 A. Une contrainte limite les moyens ou le contexte : budget maximal, norme electrique a respecter, encombrement disponible, delai de livraison ou materiaux autorises. L'exigence repond a la question « que doit faire le systeme ? », la contrainte repond a « dans quelles limites ? ». Les deux doivent etre ecrites de facon verifiable, avec une valeur et une methode de controle. Dans un projet, confondre les deux conduit a des debats sans issue : on ne peut pas remplacer une contrainte reglementaire par une preference de conception, mais on peut discuter des moyens de satisfaire une exigence fonctionnelle.",
    "On definit les deux notions et donne des exemples mesurables avec methode de controle.")],
C("Le cadrage transforme un besoin en objectifs, livrables, ressources et criteres de reussite avant toute realisation.",
  "Projet = objectif + livrables + ressources + delai + criteres",
  "Maitre d'ouvrage / maitre d'oeuvre · phases et jalons · parties prenantes",
  "Livrable~Element concret remis~Jalon~Etape et criteria d'acceptation~Partie prenante~Acteur du projet~Exigence~Besoin verifiable",
  "Ecrire le besoin et les objectifs|Identifier parties prenantes et roles|Definir livrables et jalons|Estimer ressources et budget|Valider le cadrage en revue",
  "Confondre besoin et solution|Laisser des exigences vagues|Oublier les parties prenantes|Engager les moyens avant la validation",
  "Station solaire~Prototype et rapports~Jalons~Septembre a decembre~Exigence~12 V sous 5 A~Contrainte~Budget et normes",
  "Maitre d'ouvrage~Porte le besoin~Maitre d'oeuvre~Realise la solution",
  "Exigence~Service attendu~Contrainte~Limite imposee"))

# ============================================================ MEP2
add("MEP2", "Planification et ordonnancement d'un projet", "Méthodologie de projet", ["1re"],
S("La planification convertit les objectifs du projet en taches, dates et charges de travail."
  "|La.WBS, ou decomposee de travail, repartit le projet en phases, lots et taches elementaires."
  "|L'ordonnancement etablit l'ordre des taches et identifie les dependances entre elles."
  "|Une dependance de type fin-debut signifie qu'une tache ne peut commencer qu'apres la fin d'une autre."
  "|Le chemin critique est la suite des taches qui determine la duree minimale du projet."
  "|Un retard sur une tache du chemin critique retarde toute la fin du projet."
  "|Une tache hors chemin critique dispose d'une marge, appelée flottement, qui absorbe un certain retard."
  "|Le diagramme de Gantt represente les taches dans le temps avec leur duree et leurs chevauchements."
  "|Le graphe PERT represente les taches et les dependances sous forme de reseau avec les durees estimees."
  "|Une ressource est une personne, un equipement ou un local, avec une disponibilite limitee."
  "|Une surcharge de ressource impose de deplacer une tache ou de reduire sa duree, ce qui peut allonger le projet."
  "|La planification est un document vivant : on la met a jour a chaque revue de projet."),
[QC("Qu'est-ce que la WBS ?", "Un diagramme de Gantt~La decomposee du projet en taches~Un budget~Un compte rendu", 1,
    "La WBS structure le projet en niveaux de taches de plus en plus fins."),
 QC("Quelle dependance signifie qu'une tache attend la fin d'une autre ?", "Debut-debut~Fin-debut~Fin-fin~Aucune dependance", 1,
    "En fin-debut, la tache suivante demarre apres la precedente."),
 QC("Que se passe-t-il en cas de retard sur le chemin critique ?", "Rien~La date de fin du projet est retardee~La qualite augmentee~Le budget diminue", 1,
    "Le chemin critique determine la duree totale du projet."),
 QC("Qu'est-ce que le flottement d'une tache ?", "La marge de retard disponible~Le cout de la tache~La duree totale~Le nombre de ressources", 0,
    "Une tache non critique peut glisser dans sa marge sans retarder le projet."),
 QC("Que montre un diagramme de Gantt ?", "Les dependances seules~Les taches dans le temps~Les couts par tache~Les risques", 1,
    "Le Gantt est une representation calendaire des taches."),
 QC("Quel est un effet d'une surcharge de ressource ?", "Un gain de temps~Un deplacement de tache ou un allongement du projet~Une meilleure qualite~Aucun effet", 1,
    "On ne peut pas affecter deux fois la meme personne a plein temps sur deux taches simultanees."),
 QC("Quand mettre a jour le planning ?", "Une seule fois au debut~A chaque revue de projet~Jamais~Uniquement a la fin", 1,
    "Le planning est un outil de pilotage vivant, revise regulierement."),
 QT("Un projet comporte les taches A conception (3 jours), B realisation (4 jours) apres A, C documentation (2 jours) apres A, et D essais (2 jours) apres B et C. Determiner la duree et le chemin critique.",
    "Le chemin A-B-D dure 3 + 4 + 2 = 9 jours. Le chemin A-C-D dure 3 + 2 + 2 = 7 jours. La duree minimale du projet est donc 9 jours, determinee par le chemin critique A-B-D. La tache C dispose d'un flottement de 2 jours : elle peut etre retardee de deux jours sans deplacer les essais, a condition de se terminer au plus tard au jour 7. Si la realisation B prend un jour de plus, le projet dure 10 jours ; si la documentation C prend un jour de plus, le projet reste a 9 jours grace au flottement. Ce calcul montre ou concentrer l'attention du chef de projet.",
    "On calcule les deux chemins, on identifie 9 jours et le flottement de C."),
 QT("Expliquer la difference entre Gantt et PERT et leurs usages respectifs.",
    "Le diagramme de Gantt place les taches sur un axe temporel avec des barres proportionnelles a leur duree : il est lisible pour suivre l'avancement, les chevauchements et les dates de debut et de fin. Le graphe PERT represente un reseau de taches et de dependances, avec les durees et les jalons : il met en evidence le chemin critique, les marges et les relations logiques. Le Gantt repond surtout a la question « quand ? », le PERT a la question « dans quel ordre et pourquoi ? ». Dans la pratique, les outils de gestion de projet proposent les deux vues a partir d'une meme base de donnees : modifier la duree d'une tache met a jour le Gantt et recalcule le chemin critique du PERT. Un chef de projet utilise le Gantt en reunion d'avancement et le PERT pour analyser les risques de retard.",
    "On oppose representation temporelle et representation logique, avec les usages typiques.")],
C("Planifier, c'est decomposer, ordonner et suivre : le chemin critique fixe la duree, les autres taches ont une marge.",
  "Duree du projet = longueur du chemin critique",
  "WBS · dependances fin-debut · Gantt · PERT · flottement",
  "WBS~Decomposition en taches~Chemin critique~Determines la duree~Flottement~Marge de retard~Gantt~Vue calendaire",
  "Decomposer le projet en taches|Estimer durees et ressources|Etablir les dependances|Calculer le chemin critique|Suivre et revoir le planning",
  "Oublier une dependance|Considerer toutes les taches comme critiques|Surcharger une ressource|Ne jamais mettre a jour le planning",
  "A-B-D~9 jours~A-C-D~7 jours~Flottement de C~2 jours~PERT~Reseau de dependances~Gantt~Barres dans le temps",
  "Gantt~Quand~PERT~Dans quel ordre",
  "Chemin critique~Aucune marge~Tache non critique~Flottement disponible"))

# ============================================================ MEP3
add("MEP3", "Travail en equipe et outils collaboratifs", "Méthodologie de projet", ["1re"],
S("Un projet STI2D se realise en equipe : la qualite de la collaboration influence directement le resultat."
  "|Une equipe performante combine des competences complementaires : conception, electronique, mecanique, dessin, communication."
  "|La repartition des roles doit etre explicite : chef de projet, responsable technique, responsable qualite, documentaliste, porte-parole."
  "|Un role n'implique pas l'isolement : chaque membre reste informe des decisions qui le concernent."
  "|Les objectifs individuels doivent etre alignes sur les objectifs collectifs du projet."
  "|Une communication reguliere, courte et documentee evite les malentendus et les travaux redondants."
  "|Les outils collaboratifs (espace partage, gestionnaire de taches, messagerie, wiki) centralisent les informations."
  "|Une convention de nommage des fichiers permet de retrouver rapidement la bonne version d'un document."
  "|Le controle de versions evite que deux personnes modifient simultanement le meme fichier sans coordination."
  "|Un compte rendu de reunion consigne les decisions, les responsables et les echeances."
  "|Les desaccords techniques se traitent avec des criteres et des donnees, pas avec l'autorite ou l'anciennete."
  "|La retroaction entre pairs ameliore la qualite des livrables et developpe la competence de chacun."),
[QC("Quel est un avantage de competences complementaires dans une equipe ?", "Faire les memes taches ensemble~Traiter des aspects different du projet~Eviter les reunions~Repartir les memes responsabilites", 1,
    "La diversite des competences couvre les besoins variés du projet."),
 QC("Que doit contenir un compte rendu de reunion ?", "Les decisions, responsables et echeances~Seulement la date~Les blagues~La liste des absents uniquement", 0,
    "Le compte rendu trace ce qui a ete decide et qui fait quoi."),
 QC("A quoi sert une convention de nommage ?", "A changer les couleurs~A retrouver et classer les versions des fichiers~A supprimer les anciens fichiers~A limiter l'acces", 1,
    "Un nom explicite avec date et version rend les documents identifiables."),
 QC("Quel risque d'une modification simultanee d'un fichier ?", "Une meilleure version~Des conflits et une perte de modifications~Un gain de temps~Aucun risque", 1,
    "Sans controle de versions, les changements peuvent s'ecraser."),
 QC("Comment traiter un desaccord technique ?", "Par l'anciennete~En comparant des criteres et des donnees~Par tirage au sort~En l'evitant", 1,
    "Une decision technique s'appuie sur des elements verifiables."),
 QC("Quel est un role d'un porte-parole ?", "Faire toutes les soudures~Presenter le projet et synthetiser les decisions~Ecrire seul le rapport~Gerer le budget exclusivement", 1,
    "Le porte-parole represente l'equipe dans les communications."),
 QC("A quoi sert la retroaction entre pairs ?", "A critiquer sans construire~A ameliorer les livrables et les competences~A supprimer les revisions~A remplacer le chef de projet", 1,
    "Une revue par les pairs ameliore la qualite et fait progresser chacun."),
 QT("Proposer une organisation de travail pour une equipe de quatre eleves realisant un prototype en six semaines.",
    "On repartit les roles : un chef de projet qui anime les revues et suit le planning, un responsable technique pour la mecanique et l'electronique, un responsable de la modelisation et des plans, un responsable de la documentation et de la communication. Chacun travaille sur sa specialite mais participe aux revues hebdomadaires ou l'avancement, les problemes et les decisions sont partages. Un espace commun contient les plans, les comptes rendus, le planning et les versions des documents avec une convention de nommage datee. Les decisions techniques se prennent avec une grille de criteres et un essai quand c'est possible. Chaque livrable est relu par un autre membre avant remise. Le porte-parole prepare la soutenance a partir des contributions de tous. Enfin, une revue finale verifie la coherence entre le cahier des charges, le prototype et les documents.",
    "On attend roles, rythme de communication, outils, regles de decision et relecture croisee."),
 QT("Expliquer pourquoi une decision prise par la seule autorite du chef de projet peut etre risquee.",
    "Le chef de projet a une vision d'ensemble, mais il n'a pas necessairement toutes les competences techniques detaillees. S'il impose une solution sans consulter les membres concernees, il passe a cote d'informations essentielles sur la faisabilite, les materiaux ou les delais. Les autres membres peuvent se desengager, ne pas signaler les problemes et appliquer la decision sans conviction. Une bonne pratique consiste a ecouter les avis, a demander des donnees ou des essais, puis a trancher avec des criteres explicites en expliquant le choix. L'autorite sert alors a arbitrer et a avancer, pas a remplacer la preuve. La qualite du prototype et la cohesion de l'equipe s'en trouvent ameliorees.",
    "On souligne la perte d'information, l'engagement et la decision par criteres plutot que par rang.")],
C("Le travail d'equipe repose sur des roles clairs, des outils partages et des decisions justifiees par des donnees.",
  "Equipe = competences complementaires + roles explicites + communication reguliere",
  "Compte rendu · convention de nommage · controle de versions · revue par les pairs",
  "Role~Responsabilite dans l'equipe~Outil collaboratif~Espace de travail partage~Compte rendu~Trace des decisions~Version~Etat d'un document",
  "Definir les roles et les objectifs|Mettre en place les outils partages|Organiser des revues courtes|Trancher avec des criteres|Relire les livrables entre pairs",
  "Laisser une information dans un seul message prive|Travailler sur la meme version sans coordination|Imposer une solution sans donnees|Oublier de tracer les decisions",
  "Quatre eleves~Six semaines~Revue hebdomadaire~Convention de nommage~Date et version~Grille de criteres~Relecture croisee~Soutenance commune",
  "Decision par autorite~Rapide mais risquee~Decision par criteres~Justifiee et partagee",
  "Compte rendu~Décisions et echeances~Messagerie~Echanges journaliers"))

# ============================================================ MEP4
add("MEP4", "Soutenance, communication et capitalisation de projet", "Méthodologie de projet", ["Terminale"],
S("La soutenance est un temps d'evaluation ou l'equipe presente son projet et repond aux questions du jury."
  "|Elle comprend generalement un expose suivi d'un entretien avec les examinateurs."
  "|L'expose suit un fil conducteur : contexte et besoin, demarche, realisations, essais, resultats et conclusion critique."
  "|Un plan annonce clairement les parties et le temps consacre a chacune."
  "|Les supports de presentation doivent etre lisibles, avec peu de texte et des visualisations explicites."
  "|Chaque member de l'equipe doit intervenir : le jury evalue aussi la repartition de la parole."
  "|Une demonstration du prototype est plus convaincante qu'une simple description, a condition d'etre preparee et sure."
  "|Les resultats sont presentes avec des indicateurs, des mesures et des comparaisons avec le cahier des charges."
  "|Les limites et les erreurs doivent etre assumees : le jury attend une analyse critique, pas un discours commercial."
  "|Pendant l'entretien, il faut ecouter la question, reformuler si besoin et repondre de facon structuree."
  "|Une question peut porter sur un choix technique, une hypothèse, un resultat d'essai ou la contribution de chaque eleve."
  "|La capitalisation consiste a conserver les documents, les essais et les enseignements pour les projets futurs."),
[QC("Quel est un plan d'expose efficace ?", "Contexte, demarche, realisations, essais, conclusion critique~Les resultats seulement~Une liste de dates~Le programme complet du lycée", 0,
    "Le fil conducteur permet au jury de suivre la logique du projet."),
 QC("Comment doit etre un support de presentation ?", "Tres dense en texte~Lisible avec peu de texte et des visualisations~Sans titre~Avec toutes les pages du rapport", 1,
    "Le support accompagne la parole sans la remplacer."),
 QC("Que doit faire un membre face a une question qu'il n'a pas comprise ?", "Repondre au hasard~Reformuler la question poliment~Rester silencieux~Changer de sujet", 1,
    "La reformulation securise la comprehension et montre l'ecoute."),
 QC("Quelle attitude est attendue face aux limites du projet ?", "Les cacher~Les analyser et les assumer~Les attribuer a autrui~Les ignorer", 1,
    "Une analyse critique est evaluee positivement."),
 QC("Quel element rend une demonstration fiable ?", "Une preparation et des conditions surees~Une improvisation totale~Un prototype non teste~Beaucoup de texte", 0,
    "Une demonstration doit etre repetee et presenter peu de risques de panne."),
 QC("Qu'est-ce que la capitalisation ?", "Supprimer les documents~Conserver savoirs et livrables pour le futur~Oublier les essais~Vendre le prototype", 1,
    "La capitalisation rend le travail reutilisable par la suite."),
 QC("Quel element est evalue en plus du resultat technique ?", "La seule note de rapport~La repartition de la parole et l'analyse critique~La couleur des diapositives~Le nombre de pages", 1,
    "Le jury evalue aussi la communication et la reflexivite de l'equipe."),
 QT("Preparer le plan d'une soutenance de 10 minutes pour un projet de prototype, en repartissant le temps entre les membres.",
    "Introduction (1 minute, porte-parole) : contexte, besoin et objectifs du projet. Premiere partie (2 minutes, responsable conception) : analyse fonctionnelle, cahier des charges et choix de solution avec la grille de decision. Deuxieme partie (3 minutes, responsable technique) : modelisation, fabrication du prototype et problemes rencontres, avec des images. Troisieme partie (2 minutes, responsable essais) : protocole, mesures, comparaison aux exigences et limites observees. Conclusion (2 minutes, porte-parole avec l'equipe) : bilan, apports de chacun, pistes d'amelioration et remerciements. L'ensemble est repete deux fois avec un chronometre. Un support unique circule, avec une diapo par partie et une diapo de synthese des resultats. Les reponses aux questions sont preparees a partir des points faibles identifies.",
    "On attend un fil conducteur, des temps, une repartition de parole et une preparation aux questions."),
 QT("Expliquer pourquoi la presentazione des limites d'un prototype est un element positif de la soutenance.",
    "Un prototype est une realisation intermediaire : il ne peut pas satisfaire toutes les exigences des la premiere version. Le jury sait cela et attend que l'equipe soit capable d'en prendre conscience.Presenter les limites, c'est demontrer que l'on a mesure les ecarts entre le cahier des charges et le resultat, compris les causes des defauts et identifie les actions d'amelioration. C'est aussi une preuve d'honnetete intellectuelle et de maturite : un candidat qui cache un defaut sera obligé de le reconnaitre a la question suivante, ce qui deteriore la qualite de l'echange. La conclusion peut alors proposer une nouvelle iteration du prototype avec le changement prioritaire et le moyen de le valider. Cette posture est exactement celle de l'ingenieur en conception : prouver, mesurer, corriger.",
    "On lie autocritique, mesure des ecarts, credibilite et demarche iterative.")],
C("Une soutenance reussie raconte une demarche, montre des preuves, assume les limites et repartit la parole.",
  "Contexte, demarche, realisations, essais, limites, conclusion",
  "Support lisible · demonstration preparee · reformulation des questions · capitalisation",
  "Soutenance~Presentation et entretien~Expose~Fil conducteur~Demonstration~Preuve fonctionnelle~Capitalisation~Savoir reutilise",
  "Construire un plan avec des temps|Repartir les interventions|Preparer des visuels lisibles|Repeter la demonstration|Anticiper les questions et les limites",
  "Lire un texte dense~Laisser une seule personne parler~Cacher les defauts~Improviser la demonstration",
  "10 minutes~Reparties entre quatre membres~Une diapo par partie~Mesures et comparaisons~Limites~Analyse critique~Capitalisation~Dossier reutilisable",
  "Expose~Presente la demarche~Entretien~Verifie la comprehension",
  "Support~Accompagne la parole~Rapport~Contient le detail"))

# ============================================================ ANT1
add("ANT1", "Describing a technical system in English", "Anglais technique", ["1re"],
S("Technical English uses precise, simple sentences to describe how a system works."
  "|The present simple describes permanent functions : the sensor measures the temperature."
  "|The passive voice is frequent when the action matters more than the author : the signal is amplified by the controller."
  "|A technical description follows a logical order : purpose, components, operation and limits."
  "|The purpose answers the question 'What is it for ?' : the device regulates the temperature of a room."
  "|Components are named with technical nouns : sensor, actuator, controller, power supply, housing."
  "|Sequencing words such as first, then and finally describe the operation step by step."
  "|Quantities are expressed with units : 12 volts, 5 amperes, 200 millimetres, 0,5 second."
  "|The modal can describes ability or possibility : the battery can supply 2 amperes for one hour."
  "|The modal must expresses a requirement : the housing must resist water and dust."
  "|Comparatives are useful to justify a choice : aluminium is lighter than steel, but it is more expensive."
  "|Avoid vague words such as 'thing' or 'good' : replace them by the exact name or a measurable property."),
[QC("Which tense describes a permanent technical function ?", "The past simple~The present simple~The future perfect~The present continuous only", 1,
    "The present simple states what a component does permanently."),
 QC("Why use the passive voice in a technical text ?", "To hide the action~To focus on the action and the result~To add emotion~To shorten every sentence", 1,
    "The passive emphasises what happens rather than who does it."),
 QC("Which phrase states the purpose of a device ?", "It is made of aluminium~It regulates the temperature~It costs 20 euros~It was tested yesterday", 1,
    "The purpose describes the service rendered by the system."),
 QC("Which word is a technical noun ?", "Nice~Actuator~Quickly~Yellow", 1,
    "An actuator is a component that produces an action."),
 QC("Which modal expresses a requirement ?", "Can~Must~Might~Would", 1,
    "Must expresses obligation or a technical requirement."),
 QC("How to compare two materials correctly ?", "Aluminium is lighty than steel~Aluminium is lighter than steel~Aluminium is more light than steel~Aluminium is lightest than steel", 1,
    "The comparative of light is lighter, followed by than."),
 QC("Why avoid the word 'thing' in a report ?", "It is too long~It is vague and should be replaced by an exact name~It is grammatically wrong~It is only used in speech", 1,
    "Technical writing requires precise terminology."),
 QT("Write a short description of a temperature control system using purpose, components, operation and limits.",
    "A possible description is: 'This system maintains the temperature of a room at a set value. It contains a temperature sensor, a controller, a heating element and a power supply. First, the sensor measures the room temperature and sends an analog signal to the controller. Then, the controller compares the measured value with the setpoint. If the measured temperature is lower than the setpoint, the controller switches on the heating element. Finally, the system stops heating when the setpoint is reached. The system can maintain the temperature within one degree, but it cannot heat a room larger than twenty square metres.' This description uses the present simple for functions, can for ability, and precise nouns and units.",
    "On attend les quatre parties, le present simple, des noms techniques precises et des units."),
 QT("Rewrite these vague sentences in precise technical English: 'The thing works quickly. The material is good. The machine is big.'",
    "The sentences can be rewritten as: 'The actuator responds within 0,2 second. The material has a tensile strength of 400 MPa. The machine occupies 1,2 cubic metre.' Each vague adjective is replaced by a measurable property with its unit. 'Works quickly' becomes a response time, 'good' becomes a mechanical property, and 'big' becomes a volume or an envelope dimension. This transformation is essential in a technical report because a reader must be able to verify the statement and compare it with a requirement. A precise description also avoids disputes: 'good' can mean different things to different people, while '400 MPa' has a single meaning.",
    "On remplace chaque mot vague par une propriete mesurable avec son unité.")],
C("Technical English favours precision: present simple for functions, passive for processes, exact nouns and units.",
  "Present simple + passive voice + modal can / must",
  "Purpose, components, operation, limits · avoid vague words",
  "Purpose~Service rendu~Component~Element du systeme~Operation~Fonctionnement~Limit~Limite d'usage",
  "State the purpose|Name the components|Describe the operation step by step|Give quantities and units|Mention the limits",
  "Use vague adjectives|Mix past and present without reason|Forget units in measurements|Describe only the appearance",
  "12 volts~Tension d'alimentation~0,2 second~Temps de reponse~400 MPa~Limite d'elasticite~The sensor measures~Fonction au present",
  "Active voice~L'element fait l'action~Passive voice~L'action est subie",
  "Can~Capacite~Must~Obligation technique"))

# ============================================================ ANT2
add("ANT2", "Reading a datasheet and a technical manual", "Anglais technique", ["1re"],
S("A datasheet gives the characteristics of a component in a standardised form."
  "|Most datasheets begin with a general description, a list of features and a table of absolute maximum ratings."
  "|Absolute maximum ratings must never be exceeded : doing so can destroy the component."
  "|Recommended operating conditions define the normal range of use, which is narrower than the absolute maximum."
  "|Electrical characteristics give typical and maximum values for parameters such as supply voltage, current and power."
  "|A parameter is often given with conditions, for example 'output current = 100 mA at 25 °C'."
  "|The letter 'typ' means typical, 'max' means maximum and 'min' means minimum."
  "|Timing diagrams show the sequence and the duration of signals, with parameters such as rise time and delay."
  "|Package drawings give the dimensions and the pinout, which is the numbering and function of each pin."
  "|A technical manual describes installation, configuration, operation, maintenance and troubleshooting."
  "|Warning symbols and the terms 'caution' and 'danger' signal risks for the user or the equipment."
  "|A good reading method consists in identifying the need, locating the relevant table and checking the conditions and units."),
[QC("What do absolute maximum ratings mean ?", "Recommended values~Limits that must never be exceeded~Typical values~Average values", 1,
    "Exceeding an absolute maximum can permanently damage the component."),
 QC("What does 'typ' mean in a datasheet ?", "Typical~Maximum~Minimum~Unknown", 0,
    "Typ indicates a typical value observed under given conditions."),
 QC("Where can you find the function of each pin ?", "In the timing diagram~In the pinout or package drawing~In the features list~In the warning table", 1,
    "The pinout gives the numbering and function of the pins."),
 QC("What is a timing diagram used for ?", "Showing dimensions~Showing signal sequences and durations~Listing warnings~Giving the price", 1,
    "Timing diagrams describe rise time, delay and signal order."),
 QC("Which term signals a risk of serious injury ?", "Note~Danger~Tip~Example", 1,
    "Danger indicates a hazard that can cause serious injury."),
 QC("Why check the conditions attached to a parameter ?", "Because they are decorative~Because the value is only valid under those conditions~Because they change the units~Because they are optional", 1,
    "A value without its conditions cannot be compared or reused safely."),
 QC("What should you do first when reading a datasheet ?", "Read every table in order~Identify the parameter you need~Translate the title~Memorise the values", 1,
    "A targeted reading is faster and less error-prone."),
 QT("A datasheet states 'supply voltage: 4,5 to 5,5 V typ 5 V; absolute maximum 7 V'. Explain how to use these values for a design.",
    "The recommended supply range is 4,5 to 5,5 volts, with a typical value of 5 volts. The circuit should be designed to operate inside this range, for example with a regulated 5 V supply and a tolerance that keeps the voltage between 4,75 and 5,25 V. The absolute maximum of 7 V is not an operating range : it is the limit beyond which the component may be destroyed. A transient above 7 V, even for a short time, is forbidden. The designer must also check the conditions attached to other parameters, such as temperature and load, and protect the input against overvoltage if the environment is noisy. This distinction between operating range and absolute maximum is a common source of error.",
    "On distingue plage de fonctionnement et limite absolue, avec exemple de regulation."),
 QT("Describe the method for finding the cause of a malfunction using a technical manual.",
    "One starts by identifying the symptoms precisely : error message, abnormal noise, incorrect output. The troubleshooting section of the manual usually gives a table of symptoms and possible causes. One checks the simplest causes first : power supply, connectors, fuses and settings. Then one follows the diagnostic procedure, which may require measuring voltages or reading error codes. Each test result is compared with the expected value given in the manual. If several causes are possible, one eliminates them one at a time to avoid masking the real fault. The manual also indicates warnings to respect during intervention, such as disconnecting the power before opening the housing. Finally, the intervention and the measured values are recorded for future maintenance.",
    "On suit symptomes, table de depannage, causes simples, mesures et tracabilite.")],
C("A datasheet is read in a targeted way : identify the parameter, check its conditions and respect the absolute maximum ratings.",
  "Operating conditions ≠ absolute maximum ratings",
  "typ / min / max · pinout · timing diagram · danger and caution",
  "Datasheet~Caracteristiques du composant~Absolute maximum~Limite a ne pas depasser~Pinout~Fonction des broches~Timing~Sequences des signaux",
  "Identifier le parametre cherche|Repérer le tableau pertinent|Verifier les conditions et les unites|Comparer aux besoins du projet|Respecter les avertissements",
  "Confondre valeur typique et limite absolue|Ignorer la temperature de reference|Oublier le pinout|Depasser une valeur maximale par prudence",
  "5 V typ~Valeur nominale~7 V~Maximum absolu~4,5 a 5,5 V~Plage de fonctionnement~0,2 s~Temps de montee~Danger~Risque grave",
  "Operating range~Plage normale~Absolute maximum~Limite de destruction",
  "Typ~Valeur courante~Max~Valeur maximale"))

# ============================================================ ANT3
add("ANT3", "Writing a technical report in English", "Anglais technique", ["1re"],
S("A technical report communicates a method, results and a conclusion in a clear and verifiable way."
  "|Its usual structure is : title, summary, introduction, method, results, discussion, conclusion and references."
  "|The summary, or abstract, gives the objective, the main method and the key result in about 150 words."
  "|The method section describes the equipment, the procedure and the conditions so that the experiment can be repeated."
  "|The results section presents the measurements with tables, graphs and units, without interpretation."
  "|The discussion explains the results, compares them with the requirements and discusses the uncertainties."
  "|The conclusion answers the objective and proposes improvements or further work."
  "|Technical writing uses the passive voice to describe procedures : the temperature was measured with a thermocouple."
  "|The past simple is used for completed actions, the present simple for general conclusions."
  "|Numbers and units follow international rules : a space between the value and the unit, a dot as decimal separator in English."
  "|Figures and tables must have a number, a title and a reference in the text."
  "|References cite the sources used : datasheets, standards, handbooks and previous reports."),
[QC("What is the role of an abstract ?", "To give a long history~To summarise objective, method and key result~To list all references~To describe the author", 1,
    "The abstract allows a reader to decide whether to read the full report."),
 QC("Which section describes the equipment and procedure ?", "Results~Method~Discussion~References", 1,
    "The method section must allow repetition of the experiment."),
 QC("Where should interpretation of results appear ?", "In the results section~In the discussion~In the abstract~In the title", 1,
    "Results present facts, discussion explains them."),
 QC("Which tense is used for a completed experiment ?", "Present simple~Past simple~Future continuous~Present perfect only", 1,
    "Completed actions are described with the past simple, often in the passive voice."),
 QC("How is a figure referenced in a report ?", "By its colour~By a number and a title mentioned in the text~By its size~By the author's name", 1,
    "Every figure must be cited in the text and have a caption."),
 QC("What should the conclusion contain ?", "New measurements only~The answer to the objective and possible improvements~A list of all data~The full method again", 1,
    "The conclusion closes the work and opens perspectives."),
 QC("Why cite datasheets and standards ?", "To make the report longer~To allow verification and credit sources~To replace results~To avoid tables", 1,
    "References ensure traceability and avoid plagiarism."),
 QT("Draft a short abstract for a report on the energy consumption of a solar charging station.",
    "A possible abstract is: 'This report presents the design and testing of a solar charging station for electric bicycles. The objective was to evaluate the daily energy produced and the charging time available on a school campus. A 100 W photovoltaic panel, a charge controller and a 12 V battery were installed and monitored for two weeks. Current and voltage were measured every minute and stored in a data logger. The results show an average production of 0,55 kWh per day, sufficient for two complete charges. The discussion analyses the influence of cloud cover and the limits of the battery capacity. The study concludes that the station is suitable for light use and proposes a larger panel for winter conditions.' This abstract states the objective, the method, a quantitative result and a conclusion in a compact form.",
    "On attend objectif, methode, resultat chiffre et conclusion en environ 150 mots."),
 QT("Explain why the results section should not contain interpretation.",
    "The results section is a factual record : it presents measurements, tables and graphs so that the reader can check them. If the author mixes facts and interpretations, the reader cannot distinguish what was observed from what the author believes. For example, writing 'the efficiency was low because the sensor was badly placed' combines a measurement with a hypothesis. The measurement belongs to the results, the hypothesis to the discussion. Separating the two makes the report more rigorous and allows another reader to propose a different explanation from the same data. The discussion can then compare the results with the requirements, examine uncertainties and suggest causes, clearly identified as interpretations.",
    "On separe faits mesures et hypotheses, avec un exemple et le benefit pour le lecteur.")],
C("A technical report separates facts from interpretation : method allows repetition, results show data, discussion explains them.",
  "Title, abstract, introduction, method, results, discussion, conclusion, references",
  "Passive voice for procedures · past simple for completed actions · units and captions",
  "Abstract~Resume en bref~Method~Materiel et protocole~Results~Donnees et graphiques~Discussion~Interpretation",
  "Write a precise title and abstract|Describe a repeatable method|Present results with units and captions|Discuss causes and uncertainties|Conclude and cite sources",
  "Interpret results in the results section|Forget units or captions|Use vague adjectives|Omit references to datasheets",
  "100 W~Puissance du panneau~0,55 kWh~Production quotidienne~Two weeks~Duree de l'essai~Figure 1~Reference dans le texte",
  "Results~Faits observes~Discussion~Causes proposees",
  "Past simple~Action terminee~Present simple~Conclusion generale"))

# ============================================================ ANT4
add("ANT4", "Job interview and professional vocabulary in English", "Anglais technique", ["Terminale"],
S("A job interview in English tests technical knowledge, communication and motivation."
  "|The opening is short : greet the interviewer, thank him or her and give your name and role."
  "|A self-introduction answers three questions : who you are, what you studied and what experience you have."
  "|Technical vocabulary must be precise : prototype, assembly, tolerance, maintenance, commissioning, quality control."
  "|The STAR method structures an answer to a behavioural question : Situation, Task, Action, Result."
  "|A good answer gives a concrete example and a measurable result rather than a general claim."
  "|Questions about a project should mention the constraint, the choice made and the reason for that choice."
  "|When you do not understand a question, ask for clarification politely before answering."
  "|The phrase 'Could you clarify what you mean by...' is useful and professional."
  "|Avoid translating word for word from French : use simple and direct English sentences."
  "|Preparing questions for the interviewer shows interest in the company and the role."
  "|After the interview, a short thank-you message confirms your motivation and recalls one key point."),
[QC("What does the S in the STAR method mean ?", "Success~Situation~Skill~Solution", 1,
    "STAR stands for Situation, Task, Action, Result."),
 QC("Which answer is the strongest ?", "I am very good at projects~In my last project I reduced the assembly time by 20 %~I like teamwork~I know many things", 1,
    "A concrete example with a measurable result is convincing."),
 QC("How to ask for clarification politely ?", "What ?~Could you clarify what you mean by... ?~Repeat~I don't know", 1,
    "A polite reformulation shows active listening."),
 QC("Which word belongs to technical vocabulary ?", "Nice~Commissioning~Happy~Big", 1,
    "Commissioning is the phase of putting an installation into service."),
 QC("What should a self-introduction include ?", "Only your name~Who you are, your studies and your experience~Your salary expectations first~A long personal story", 1,
    "The introduction gives a concise professional profile."),
 QC("Why prepare questions for the interviewer ?", "To fill the silence~To show interest in the role and the company~To ask the salary immediately~To avoid answering", 1,
    "Relevant questions demonstrate motivation and reflection."),
 QC("What is a good post-interview action ?", "Forget the interview~Send a short thank-you message recalling a key point~Call every hour~Publish the discussion", 1,
    "A brief thank-you note confirms interest and leaves a clear memory."),
 QT("Prepare a one-minute self-introduction for a STI2D graduate applying for a technician position in automation.",
    "A possible introduction is: 'Good morning. My name is Alex Martin and I recently obtained a STI2D baccalaureate with a speciality in information systems and digital technology. During my final year, I worked in a team of four to design and test a prototype of a temperature monitoring station. I was responsible for the sensors and the data acquisition, and I learned to use a data logger and to compare measurements with the requirements. I also completed a two-month internship in a workshop, where I helped to maintain industrial controllers. I am interested in this position because I want to work on real automation systems and continue to learn from experienced technicians. Thank you.' This introduction is short, factual and directly connected to the job.",
    "On attend nom, formation, projet concret, competence technique et motivation pour le poste."),
 QT("Using the STAR method, answer the question: 'Tell me about a time you solved a technical problem.'",
    "A possible answer is: 'Situation: during my final project, the temperature sensor gave unstable readings. Task: I had to find the cause before the final demonstration. Action: I checked the power supply and the wiring, then I compared the signal with a reference sensor and discovered that a poor connection introduced noise. I replaced the connector and added a filter in the acquisition software. Result: the readings became stable and the prototype passed the test. I also wrote the procedure in the project report so that the team could reuse it.' This answer gives a real situation, a precise action and a result that can be checked. It also shows documentation and teamwork, which are valued in a technical role.",
    "On attend les quatre etapes STAR, une cause identifiee et un resultat concret.")],
C("A professional interview combines precise vocabulary, concrete examples and structured answers.",
  "STAR = Situation, Task, Action, Result",
  "Self-introduction · clarify politely · measurable results · thank-you message",
  "Interview~Echange professionnel~STAR~Structure de reponse~Clarification~Demande de precision~Vocabulary~Termes techniques precis",
  "Prepare a short self-introduction|Learn key technical terms|Structure examples with STAR|Ask for clarification when needed|Prepare questions and a follow-up",
  "Give vague claims without evidence|Translate word for word|Pretend to understand a question|Ignore the follow-up message",
  "STAR~Quatre etapes~20 %~Reduction du temps de montage~Commissioning~Mise en service~Could you clarify~Reformulation polie",
  "Vague claim~Affirmation sans preuve~Measurable result~Chiffre verifiable",
  "Technical vocabulary~Termes precis~Everyday words~Langage courant"))

valider_et_ecrire(F, "sti2d-mat-part-C.json")
