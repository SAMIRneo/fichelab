# -*- coding: utf-8 -*-
"""Generateur sti2d-mat-part-B.json — lot B : enseignements de specialite (20 fiches).

Technologie, Energie, Physique appliquee et Mathematiques appliquees pour les
quatre specialites STI2D (SIN, EE, ITEC, AC) : 12 points de cours,
9 questions corrigees (7 QCM + 2 texte), 7 blocs en ordre strict, 3 SVG.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_etapes,
                      svg_compare, bloc, valider_et_ecrire)

FIL = ["sti2d"]
REF = (
    "Programme des enseignements de specialite des classes de premiere et terminale de la serie STI2D : "
    "arrete du 17 janvier 2019 (NOR MENE1901591A), Bulletin officiel special n 1 du 22 janvier 2019, "
    "specialites Innovation technologique et eco-conception (ITEC), Energie electrique (EE), Systemes "
    "d'information et numerique (SIN) et Architecture et construction (AC). Physique-chimie et "
    "mathematiques de premiere STI2D : arrete du 17 janvier 2019 (NOR MENE1901630A). Ressources "
    "pedagogiques et sujets : eduscol « Programmes et ressources en serie STI2D » et « Baccalaureat "
    "technologique serie STI2D »."
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


# ============================================================ TEC1
add("TEC1", "Demarche de conception et cahier des charges", "Technologie", ["1re"],
S("La conception est une demarche itérative qui transforme un besoin en solution technique concrete."
  "|Le cahier des charges (CdC) formalise le besoin : il est le contrat entre le demandeur et le concepteur."
  "|Un cahier des charges contient le contexte, la finalite, les fonctions, les contraintes et les critères de validation."
  "|Les contraintes portent sur la technologie, le cout, la norme, la securite, la maintenance et l'impact environnemental."
  "|Une fonction est un service rendu par le produit a un utilisateur ou a l'environnement."
  "|On distingue les fonctions principales (raison d'etre) et les fonctions complementaires (confort, securite, maintenance)."
  "|Un indicateur de performance est une grandeur mesurable qui permet de verifier une fonction : masse, puissance, delai."
  "|La phase d'analyse du besoin precede la recherche de solutions : on ne dessine pas avant d'avoir qualifie le besoin."
  "|La divergeance consiste a produire plusieurs pistes de solutions sans les juger trop tot."
  "|La convergeance selectionne la solution la plus adaptee avec une grille de decision pondérée."
  "|Le choix est trace : chaque critere est évalué et la decision est justifiee dans un compte rendu."
  "|En specialite ITEC, le cahier des charges est un livrable evalue et sert de reference pendant tout le projet."),
[QC("Quel role joue le cahier des charges ?", "Il dessine la solution~Il formalise le besoin et les contraintes~Il remplace le prototype~Il fixe le prix de vente", 1,
    "Le CdC est le document de reference qui decrit le besoin et les contraintes."),
 QC("Qu'est-ce qu'une fonction principale ?", "Une fonction de confort~Le service qui justifie l'existence du produit~Une contrainte de cout~Une norme", 1,
    "La fonction principale est la raison d'etre du produit."),
 QC("Quel element n'appartient pas au cahier des charges ?", "Les contraintes~Les critères de validation~Le besoin~Le resultat des ventes futures", 3,
    "Les ventes ne sont pas une donnee du besoin initial ; les autres elements en font partie."),
 QC("Que permet un indicateur de performance ?", "De mesurer la realisation d'une fonction~De remplacer le plan~De supprimer les essais~De choisir la couleur", 0,
    "Un indicateur rend la verification objective et mesurable."),
 QC("Quelle est la Phase de divergeance ?", "Le choix final~La production de plusieurs pistes sans jugement~La fabrication~La maintenance", 1,
    "On explore d'abord de nombreuses pistes avant de selectionner."),
 QC("Comment faire converger les solutions ?", "Au hasard~Avec une grille de decision pondérée~En prenant la premiere idee~Par vote secret sans critères", 1,
    "La grille pondérée rend le choix explicite et justifiable."),
 QC("Que faut-il tracer apres une selection ?", "Seulement la solution retenue~Les critères, les notes et la justification~Le nom du concepteur~La date de livraison", 1,
    "La tracabilite du choix est exigée en evaluation."),
 QT("Décrire les etapes de la conception d'un support de telephone pour un atelier, du besoin au choix de solution.",
    "On commence par analyser le besoin : le support doit maintenir un telephone à hauteur d'yeux, résister aux vibrations, être fabriqué avec les moyens de l'atelier et coûter moins de 10 euros. On rédige le cahier des charges avec ces fonctions et contraintes, en ajoutant des indicateurs : angle de lecture, masse maximale, encombrement. On imagine ensuite plusieurs pistes (support plié en tole, impression 3D, socle en bois) sans les juger. On compare avec une grille pondérée : cout, rigidité, facilité de fabrication, impact environnemental. On choisit la solution la mieux notee, on justifie le choix par les notes et on conserve les autres pistes dans le dossier. On passe alors seulement au dessin de definition et au prototype.",
    "On attend besoin, CdC, divergeance, grille pondérée, choix justifie et tracabilite."),
 QT("Expliquer la difference entre fonction principale et fonction complementaire, avec des exemples.",
    "La fonction principale est le service essential : pour une lampe de bureau, éclairer une zone de travail. Les fonctions complementaires rendent le produit utilisable, sur, durable ou agreable : etre stable, ne pas chauffer, etre facile a orienter, se replier pour le rangement. Elles ne justifient pas l'achat a elles seules, mais leur absence rend le produit incompatible avec son usage. Les distinguer permet de prioriser les efforts de conception : on ne supprime pas une fonction principale pour ameliorer un confort, alors qu'on peut arbitrer entre plusieurs fonctions complementaires. Cette hierarchie aide aussi a construire la grille de decision et a fixer les criteres de validation du cahier des charges.",
    "On definit les deux types de fonctions et on illustre par un produit concret.")],
C("La conception part d'un besoin formalise : on explore des pistes puis on choisit avec des critères explicites.",
  "Besoin → fonctions → contraintes → solutions → choix trace",
  "Fonction principale / complementaire · divergeance puis convergeance · grille pondérée",
  "Cahier des charges~Formalise le besoin~Fonction~Service rendu~Contrainte~Limite a respecter~Indicateur~Grandeur mesurable",
  "Analyser le besoin et le contexte|Rediger le cahier des charges|Imaginer plusieurs solutions|Evaluer avec une grille pondérée|Tracer le choix et le justifier",
  "Dessiner avant d'analyser le besoin|Oublier les contraintes de maintenance|Juger les idees des la premiere phase|Choisir sans critères explicites",
  "Support telephone~Maintien et vibration~Cout~Moins de 10 euros~Grille~Cout, rigidite, impact~Choix~Solution la mieux notee",
  "Fonction principale~Raison d'etre~Fonction complementaire~Confort ou securite",
  "Divergeance~Multiplier les pistes~Convergeance~Selectionner et justifier"))

# ============================================================ TEC2
add("TEC2", "Analyse fonctionnelle : systeme, fonctions et FAST", "Technologie", ["1re"],
S("L'analyse fonctionnelle decrit ce que le systeme doit faire, independamment des solutions techniques retenues."
  "|Un systeme est un ensemble d'elements en interaction qui rend un service dans un environnement donne."
  "|Le systeme est defini par ses limites : ce qui appartient au systeme et ce qui appartient a son environnement."
  "|Les elements exterieurs (EE) sont les elements avec lesquels le systeme interagit : utilisateur, energies, matieres, autres systemes."
  "|La fonction globale est le service rendu par le systeme a l'utilisateur ou au milieu exterieur."
  "|Le FAST (Function Analysis System Technique) represente les fonctions en arborescence avec les relations POURQUOI et COMMENT."
  "|Dans le FAST, la question POURQUOI monte vers la fonction globale et la question COMMENT descend vers les fonctions techniques."
  "|Les fonctions techniques precisent les grandeurs et les valeurs a atteindre, par exemple debit, temperature ou precision."
  "|Les liaisons du systeme decrivent les flux d'energie, de matiere et d'information entre les elements."
  "|Un graphe de fonctions rend visibles les dependances et aide a detecter les fonctions manquantes."
  "|La valeur d'une fonction se mesure par le rapport entre le service rendu et le cout de sa realisation."
  "|L'analyse de valeur cherche a supprimer ou simplifier les fonctions qui coutent cher sans apporter de service proportionne."),
[QC("Que decrit l'analyse fonctionnelle ?", "Les solutions techniques~Ce que le systeme doit faire~Le cout de fabrication~Le plan de marketing", 1,
    "Elle decrit les fonctions attendues avant le choix des solutions."),
 QC("Qu'appelle-t-on element exterieur ?", "Un element du systeme~Un element de l'environnement qui interagit avec lui~Une vis~Un plan", 1,
    "Les EE sont externes au systeme mais interagissent avec lui."),
 QC("Dans un FAST, que demande la question POURQUOI ?", "Comment réaliser la fonction~Pourquoi la fonction est necessaire~Combien cout-t-elle~Qui la realise", 1,
    "POURQUOI remonte vers la fonction globale, COMMENT descend vers les moyens."),
 QC("Quelle question descend dans un FAST ?", "Pourquoi~Comment~Quand~Combien", 1,
    "La question COMMENT cherche les moyens de realiser une fonction."),
 QC("Qu'est-ce qu'une fonction technique ?", "Une fonction sans mesure~Une fonction precisee par des grandeurs et des valeurs~Une contrainte commerciale~Un element exterieur", 1,
    "Elle donne les performances attendues sous forme de grandeurs mesurables."),
 QC("Quels flux circulent dans un systeme ?", "Energie, matiere et information~Couleur, forme et prix~Only l'information~Eau et air uniquement", 0,
    "Les trois grands types de flux sont energie, matiere et information."),
 QC("Comment calculer la valeur d'une fonction ?", "Service rendu / cout~Cout / service rendu~Service × cout~Cout − service", 0,
    "La valeur est le rapport entre l'utilite et le cout."),
 QT("Construire l'analyse fonctionnelle simplifiee d'un arrosage automatique de plante.",
    "Le systeme est le dispositif d'arrosage ; ses limites excluent la plante et le réservoir d'eau, qui sont des elements exterieurs avec l'utilisateur et l'alimentation. La fonction globale est fournir la quantite d'eau necessaire a la plante. Les fonctions techniques sont : detecting l'humidite du sol avec un seuil, commander une pompe, debiter un volume donne, arreter apres un temps fixe, et signaler un defaut. Le FAST se lit ainsi : pourquoi arroser ? pour maintenir la plante en vie ; comment ? en detecting l'humidite puis en commandant la pompe ; pourquoi detecter ? pour eviter l'exces d'eau ; comment ? avec une sonde et un seuil compare par le controleur. Les flux sont l'information d'humidite vers le controleur, l'energie electrique vers la pompe et l'eau vers la plante.",
    "On attend limites du systeme, fonction globale, fonctions techniques et relation FAST."),
 QT("Expliquer pourquoi l'analyse de valeur peut conduire a supprimer une fonction.",
    "L'analyse de valeur compare le service rendu par une fonction et le cout de sa realisation. Une fonction peut etre techniquement reussie maiseconomiquement injustifiee si son cout est eleve et son usage rare. Par exemple, un regulateur de precision extreme sur un-arrosage domestique apporte un service marginal par rapport a un simple seuil d'humidite, tout en augmentant sensiblement le prix et la complexite. Supprimer cette fonction reduit le cout, le nombre de pieces, les pannes possibles et la consommation de ressources, sans degader le service essential. Il faut neanmoins verifier que la fonction n'est pas liee a une exigence de securite ou a une norme : dans ce cas, sa suppression est interdite malgre son cout.",
    "On lie valeur, service et cout, avec un exemple et la reserve securite/norme.")],
C("L'analyse fonctionnelle decrit le service attendu et ses liens ; le FAST rend la logique POURQUOI/COMMENT visible.",
  "Valeur d'une fonction = service rendu / cout de realisation",
  "Systeme et elements exterieurs · fonction globale · fonctions techniques · FAST",
  "Systeme~Elements en interaction~Fonction globale~Service rendu~Element exterieur~Interaction avec le milieu~FAST~Arborescence des fonctions",
  "Fixer les limites du systeme|Identifier les elements exterieurs|Enoncer la fonction globale|Decliner les fonctions techniques|Construire le FAST et verifier les flux",
  "Confondre fonction et solution technique|Oublier de fixer les limites|Inverser POURQUOI et COMMENT|Ignorer une fonction de securite",
  "Arrosage~Fournir de l'eau a la plante~Sonde~Mesurer l'humidite~Pompe~Debiter le volume~Valeur~Service sur cout",
  "Fonction globale~Objectif du systeme~Fonction technique~Moyen avec grandeurs",
  "POURQUOI~Remonte au but~COMMENT~Descend vers les moyens"))

# ============================================================ TEC3
add("TEC3", "Choix des materiaux et des procedures de fabrication", "Technologie", ["1re"],
S("Le choix d'un materiau resulte d'un compromis entre performances, cout, disponibilite et impact environnemental."
  "|Les grandes familles de materiaux sont les metaux, les polymeres, les ceramiques et les composites."
  "|Un metal est generalement ductile, bon conducteur et recyclable ; l'acier et l'aluminium sont les plus courants."
  "|Les polymeres sont legers et isolants, mais leur resistance thermique et leur recyclabilite varient beaucoup."
  "|Un composite associe une matrice et un renfort, par exemple une resine et des fibres de verre, pour allier legerete et rigidite."
  "|Les proprietes mecaniques utiles sont la limite d'elasticite, la durete, la resilience et la resistance a la fatigue."
  "|Les proprietes thermiques (conductivite, dilatation) et electriques guident le choix dans un environnement contraint."
  "|Une propriete doit etre comparee a la contrainte du cahier des charges et exprimee avec son unite."
  "|Les procedures de fabrication courants sont le decoupage, le pliage, l'usinage, le moulage et la fabrication additive."
  "|Le choix du procede depend de la forme de la piece, de la precision demandee, de la quantite et du cout de l'outillage."
  "|La fabrication additive est avantageuse pour les formes complexes et les petites series, sans moule specifique."
  "|Le recyclage et la fin de vie sont des criteres de l'eco-conception : on privilegie les materiaux separables et les filieres existantes."),
[QC("Quelle famille de materiaux est generalement bonne conductrice et ductile ?", "Les polymeres~Les metaux~Les ceramiques~Les elastomeres", 1,
    "Les metaux conduisent la chaleur et l'electricite et se deformation plastiquement."),
 QC("Qu'est-ce qu'un composite ?", "Un metal pur~Une matrice renforcee par des fibres~Un polymere sans charge~Une ceramique massive", 1,
    "Un composite associe une matrice et un renfort pour combiner leurs proprietes."),
 QC("Quelle grandeur mesure la resistance au choc ?", "La durete~La resilience~La conductivite~La masse volumique", 1,
    "La resilience est l'energie absorbee avant rupture under choc."),
 QC("Quel procede convient le mieux a une forme complexe en petite serie ?", "Le moulage sous pression~La fabrication additive~L'emboutissage~Le coulage en moule permanent", 1,
    "L'impression 3D ne necessite pas d'outillage specifique."),
 QC("Quel critere influence le choix du procede ?", "La couleur du bureau~La precision et la quantite~Le nom du fournisseur~L'heure de la commande", 1,
    "Precision, quantite et cout d'outillage determines le procede."),
 QC("Quelle propriete thermique peut poser probleme dans un assembleage mixte ?", "La masse volumique~La dilatation differentielle~La durete~La resilience", 1,
    "Des dilatations differentes generent des contraintes aux interfaces."),
 QC("Pourquoi privilegier des materiaux separables ?", "Pour augmenter le cout~Pour faciliter le recyclage et la reparation~Pour changer l'aspect~Pour reduire la precision", 1,
    "La separabilite des constituants est une condition du recyclage effectif."),
 QT("Justifier le choix de l'aluminium plutot que de l'acier pour un carter de moteur portable.",
    "L'aluminium a une masse volumique d'environ 2,7 contre 7,8 pour l'acier : a volume egal, le carter est environ trois fois plus leger, ce qui reduit la masse totale de l'engin portable et la fatigue de l'utilisateur. Il possede une bonne conductivite thermique, ce qui aide a evacuer la chaleur du moteur, et il resiste a la corrosion par formation d'une couche d'oxyde. Sa limite d'elasticite est plus faible que celle de l'acier, il faut donc adapter l'epaisseur et les renforts. Son cout de matiere est plus eleve et son usinage exige des precautions, mais l'economie de masse et la recyclabilite compensent ces inconvenients dans un produit portable. On verifie enfin la compatibilite avec les autres pieces pour eviter la corrosion galvanique.",
    "On compare masse, conductivite, resistance, cout et recyclage, avec une nuance sur la rigidity."),
 QT("Expliquer comment la fin de vie d'un produit influence le choix des materiaux des la conception.",
    "Le choix du materiau determine les possibilites de reparation, de demontage et de recyclage. Un assembleage de pieces en plastiques differents collées entre elles est difficile a separer : il finit le plus souvent en dechet, meme si chaque plastic etait recyclable. Un concepteur peut au contraire choisir un seul polymer pour toute une piece, des vis plutot que des colles, et des materiaux reconnus par une filiere de collecte. Il doit aussi eviter les substances interdites qui compliquent le recyclage et se renseigner sur la disponibilite de la matiere recyclée. Cette approche, appelee eco-conception, réduit l'impact du produit sur l'ensemble de son cycle de vie et peut diminuer les couts de traitement en fin de vie.",
    "On lie demontage, separabilite, filieres de recyclage et decision des la conception.")],
C("Choisir un materiau est un arbitrage entre proprietes, procede, cout et fin de vie.",
  "Masse volumique · limite d'elasticite · conductivite · resilience",
  "Metaux, polymeres, ceramiques, composites · decoupage, moulage, fabrication additive",
  "Materiau~Choix arbitre~Propriete~Mecanique ou thermique~Composite~Matrice et renfort~Procede~Façon de produire",
  "Traduire les contraintes en proprietes|Comparer les familles de materiaux|Verifier la compatibilite de fabrication|Estimer le cout et la quantite|Integrer la fin de vie",
  "Choisir le materiau le plus resistant sans regarder le cout|Oublier la masse volumique|Ignorer la dilatation dans un assembleage|Négliger le demontage",
  "Aluminium~2,7 g/cm³~Acier~7,8 g/cm³~Composite~Fibre de verre et resine~Impression 3D~Petite serie complexe",
  "Metaux~Ductiles et conducteurs~Ceramiques~Dures et fragiles",
  "Resilience~Energie au choc~Durete~Resistance a la rayure"))

# ============================================================ TEC4
add("TEC4", "Modelisation CAO et dessin technique : communiquer une forme", "Technologie", ["Terminale"],
S("La modelisation CAO (conception assistee par ordinateur) cree un numerique de la piece avant sa fabrication."
  "|Une esquisse 2D est contrainte par des dimensions et des relations geometriques : horizontalite, parallelisme, symetrie."
  "|Une contrainte geometrique impose une relation, une contrainte dimensionnelle impose une valeur."
  "|Une esquisse totalement contrainte ne peut plus se deformer librement : elle est dite entierement definie."
  "|Les operations de base sont l'extrusion, la revolution, l'enlevement de matiere et le perçage."
  "|Un modele parametrique permet de modifier une cote et de propager automatiquement la modification aux pieces liees."
  "|Un assemblage regroupe plusieurs pieces avec des relations de position : coincidence, alignement, distance."
  "|Le dessin technique 2D presente les vues, les coupes, les cotes et les tolerances necessaires a la fabrication."
  "|La projection europeenne (1re angle) place la vue de dessous au-dessus de la vue de face."
  "|Une coupe montre l'interieur d'une piece grace a un plan de coupe et un hachurage."
  "|La cote nominale est la valeur theorique ; la tolerance definit l'ecart admissible, mais une tolerance trop serrée augmente le cout sans necessite fonctionnelle."
  "|La maquette numerique sert aussi a verifier les interferences et a produire les fichiers de fabrication additive."),
[QC("Quelle difference entre contrainte geometrique et dimensionnelle ?", "Geometrique impose une valeur~Geometrique impose une relation, dimensionnelle une valeur~Elles sont identiques~Dimensionnelle impose une couleur", 1,
    "Parallelisme est geometrique ; 25 mm est dimensionnelle."),
 QC("Qu'appelle-t-on esquisse entierement definie ?", "Une esquisse sans cotes~Une esquisse ou toute deformation est bloquee~Un plan vide~Un assemblage", 1,
    "Toutes les relations et cotes sont fixees."),
 QC("Quelle operation transforme un profil en volume par rotation ?", "L'extrusion~La revolution~Le perçage~Le lissage", 1,
    "La revolution fait tourner un profil autour d'un axe."),
 QC("Que permet un modele parametrique ?", "Changer une cote et mettre a jour les pieces liees~Supprimer les cotes~Imprimer sans plan~Remplacer l'atelier", 0,
    "Les relations parametiques propagent les modifications."),
 QC("Quel est le role d'une coupe sur un dessin ?", "Montrer la couleur~Montrer l'interieur de la piece~Agrandir le plan~Remplacer les cotes", 1,
    "La coupe révèle la geometrie interne et les epaisseurs."),
 QC("Que definit une tolerance ?", "La couleur de la piece~L'ecart admissible autour de la cote~Le nombre de vues~La masse maximale", 1,
    "La tolerance fixe l'intervalle de fabrication acceptable."),
 QC("Quel risque d'une tolerance trop serrée ?", "Une piece plus legere~Un cout de fabrication accru~Une meilleure esthetique~Aucun effet", 1,
    "Une precision excessive exige des moyens et des controles plus couteux."),
 QT("Expliquer la demarche pour modeleur un support en L avec deux trous de fixation dans un logiciel de CAO.",
    "On cree d'abord une esquisse sur un plan : le profil en L avec ses segments. On ajoute des contraintes geometriques (horizontal, vertical, coincidences) puis des cotes (longueur des bras, epaisseur). On controle que l'esquisse est entierement definie. On realise ensuite une extrusion de l'epaisseur choisie. Pour les trous, on esquisse deux cercles sur la face appropriee, on les contraint par leur diametre et leur position, puis on applique une operation d'enlevement de matiere de type perçage. On verifie enfin l'assemblage avec la vis de fixation, on regarde les interferences eventuelles et on genere le dessin 2D cote avec les tolerances et les vues necessaires a l'atelier.",
    "On attend esquisse contrainte, extrusion, perçage, verification et dessin de sortie."),
 QT("Pourquoi faut-il éviter de multiplier les cotes inutiles sur un plan de fabrication ?",
    "Une cote superflu peut contredire une autre cote et rendre la piece impossible a fabriquer. Elle impose aussi un controle supplementaire et peut conduire a rejeter une piece pourtant fonctionnelle. Le principe est de coter chaque element une seule fois, en choisissant les cotes utiles a la fonction et a l'assemblage. Les autres dimensions se deduisent par calcul ou par la geometrie du modele. Un plan clair avec peu de cotes bien choisies est plus lisible et moins source d'erreur qu'un plan surcharge. Il faut en revanche toujours indiquer les cotes fonctionnelles et les tolerances associees, car ce sont elles qui garantissent le montage et le service rendu.",
    "On evoque contradiction, surcharge, cotes fonctionnelles et lisibilite du plan.")],
C("La CAO produit un modele parametrique et un dessin cote : la qualite des contraintes conditionne toute la suite.",
  "Esquisse contrainte + operations = modele · cote nominale + tolerance = definition fabricable",
  "Projection 1er angle · coupe et hachurage · assemblage et interferences",
  "Esquisse~Profil contraint~Contrainte~Relation ou cote~Extrusion~Donne du volume~Assemblage~Pieces et relations",
  "Contruire une esquisse contrainte|Appliquer les operations de volume|Ajouter perçages et congés|Verifier les interferences|Generer le dessin cote",
  "Laisser une esquisse sous-contraintee|Multiplier les cotes redondantes|Oublier la tolerance|Confondre projection 1er et 3e angle",
  "Profil en L~Deux bras et epaisseur~Deux trous~Diametre et position~Extrusion~Volume final~Tolerance~Ecart admissible",
  "Contrainte geometrique~Relation~Contrainte dimensionnelle~Valeur numerique",
  "Coupe~Vue interne~Vue exterieure~Aspect seulement"))

# ============================================================ TEC5
add("TEC5", "Prototypage, essais et validation d'un produit", "Technologie", ["Terminale"],
S("Le prototype est une realisation intermediaire qui permet de tester une hypothese de conception avant la serie."
  "|On distingue le prototype de validation fonctionnelle du prototype de presentation, qui vise surtout l'aspect."
  "|Un plan d'essais definit ce que l'on mesure, dans quelles conditions, avec quel appareil et quel critere de reussite."
  "|Les essais doivent etre reproductibles : meme environment, meme protocole et meme appareil de mesure."
  "|Un essai compare une grandeur mesuree a une exigence du cahier des charges, exprimee avec une tolerance."
  "|Les resultats sont consignes dans un tableau avec la date, la grandeur, la valeur, l'incertitude et la conclusion."
  "|Un resultat non conforme entraine une analyse de cause avant toute modification du prototype."
  "|La methode des 5 pourquoi permet de remonter de symptom a cause racine par questions successives."
  "|Une modification doit etre unique a chaque iteration pour pouvoir attribuer l'effet observé a la bonne cause."
  "|La fabrication additive accelere le prototypage mais impose des etapes de finition et des controles dimensionnels."
  "|Le cout et le delai d'un prototype doivent rester proportionnes a la decision qu'il doit permettre."
  "|La validation finale est une synthese des essais qui declare conformes, conformes avec reserve ou non conformes."),
[QC("Quel est le role principal d'un prototype ?", "Remplacer le produit final~Tester une hypothese de conception~Augmenter le prix~Supprimer les essais", 1,
    "Le prototype sert à valider des choix avant la production."),
 QC("Que doit contenir un plan d'essais ?", "Seulement le resultat~Grandeur, conditions, appareil et critere~La couleur du prototype~Le nom du client", 1,
    "La reproductibilite exige la definition de tous ces elements."),
 QC("Qu'appelle-t-on essai reproductible ?", "Un essai fait une seule fois~Un essai refait dans les memes conditions~Un essai sans mesure~Un essai au hasard", 1,
    "La repetition dans des conditions identiques permet de comparer les resultats."),
 QC("Que faire devant un resultat non conforme ?", "Modifier plusieurs parametres a la fois~Analyser la cause avant toute modification~Ignorer le resultat~Changer l'appareil", 1,
    "Une cause identifiee permet une correction ciblee."),
 QC("Quel outil cherche la cause racine ?", "La methode des 5 pourquoi~Le diagramme de Gantt~Le FAST~La grille de Weber", 0,
    "Les 5 pourquoi remontent successivement du symptom a la cause."),
 QC("Pourquoi ne modifier qu'un parametre a la fois ?", "Pour aller plus vite~Pour attribuer l'effet a la bonne cause~Pour reduire les couts~Pour eviter les mesures", 1,
    "Sinon les effets se melangent et l'interpretation devient impossible."),
 QC("Que contient la validation finale ?", "Un sentiment personnel~Une synthese des essais et une conclusion de conformite~Un seul essai~Le devis", 1,
    "La validation est documentee et conclut sur la conformite aux exigences."),
 QT("Décrire un plan d'essais pour verifier qu'un support imprime en 3D supporte 5 kg sans deformation excessive.",
    "On definit la grandeur : la fleche au centre du support, mesuree en millimetres avec un comparateur ou une regle graduee. La condition d'essai est une charge de 5 kg appliquee au centre, a temperature ambiante, pendant 10 minutes, avec le support pose sur une surface rigide. Le critere de reussite est une fleche inferieure a 2 mm et l'absence de rupture, conformement au cahier des charges. On repete l'essai trois fois sur le meme prototype et sur deux prototypes pour estimer la dispersion. On consigne pour chaque essai la date, la charge reelle, la fleche mesuree avec son incertitude et la conclusion. Si la fleche depasse 2 mm, on analyse la cause (epaisseur, orientation d'impression, materiau) avant de modifier un seul parametre et de recommencer.",
    "On attend grandeur, conditions, appareil, critere, repetition et consignation des resultats."),
 QT("Expliquer pourquoi un prototype doit etre proportionne a la decision a prendre.",
    "Un prototype a un cout en temps, en matiere et en main-d'oeuvre. Fabriquer une maquette tres aboutie pour verifier une simple question de dimension est un gaspillage ; a l'inverse, un prototype trop grossier ne permet pas de decider d'un investissement important. La bonne approche est de choisir le niveau de fidelite minimal qui repond a la question posee : un montage en carton suffit pour valider un encombrement, une piece imprimee pour tester un assemblage, un prototype fonctionnel pour mesurer une performance. On documente ensuite ce que le prototype valide et ce qu'il ne valide pas, afin de ne pas tirer de conclusions excessives d'un essai partiel. Cette rigueur est au coeur de la demarche d'innovation en STI2D.",
    "On relie fidelite, cout et question a trancher, avec la limite des conclusions.")],
C("Le prototype sert a decider : on definit des essais mesurables, on analyse les ecarts puis on corrige une cause a la fois.",
  "Plan d'essais = grandeur + conditions + appareil + critere",
  "5 pourquoi · reproductibilite · une modification par iteration · validation documentee",
  "Prototype~Realisation intermediaire~Essai~Mesure comparee a l'exigence~Reproductibilite~Memes conditions~Cause racine~Veritable origine du defaut",
  "Definir l'hypothese a tester|Etablir le plan d'essais|Realiser et consigner les mesures|Analyser les ecarts|Corriger une cause et reessayer",
  "Tester sans critere defini|Modifier plusieurs parametres en meme temps|Ignorer les essais non conformes|Conclure au-dela de ce que le prototype permet",
  "Charge 5 kg~Fleche maximale 2 mm~Trois repetitions~5 pourquoi~Recherche de cause~Une seule modification~Validation~Synthese des essais",
  "Prototype fonctionnel~Teste le service~Prototype de presentation~Teste l'aspect",
  "Essai~Mesure et comparaison~Validation~Decision de conformite"))

# ============================================================ ENE1
add("ENE1", "Sources d'energie et mix energetique", "Énergie", ["1re"],
S("Une source d'energie est un reservoir ou un flux que l'on peut convertir pour rendre un service."
  "|Les energies primaires sont extraites ou prelevees dans la nature : petrol, gaz, charbon, uranium, soleil, vent, eau."
  "|Les energies secondaires sont obtenues par conversion, comme l'electricite ou le carburant raffine."
  "|Les sources non renouvelables se consomment plus vite qu'elles ne se reconstituent a echelle humaine."
  "|Les sources renouvelables (solaire, eolien, hydraulique, biomasse, geothermie) se renouvellent naturellement."
  "|Le mix energetique est la repartition des sources dans la production d'energie d'un pays ou d'un territoire."
  "|En France, le mix electrique associe une part importante de nucleaire et d'energies renouvelables, avec une faible part fossile."
  "|La facteur de charge d'une installation est le rapport entre l'energie reellement produite et l'energie maximale theorique."
  "|L'intermittence designe la variabilite de la production solaire et eolienne selon les conditions climatiques."
  "|Le stockage et la diversification des sources compensent l'intermittence et sécurisent l'approvisionnement."
  "|Chaque source a une empreinte carbone, un cout de production, une durabilite et des impacts specifiques sur les ecosystems."
  "|Le choix d'un mix est un arbitrage entre securite d'approvisionnement, cout, emissions et acceptabilite sociale."),
[QC("Quel est un exemple d'energie primaire ?", "L'electricite~Le petrol brut~L'essence~Le gaz de ville", 1,
    "L'energie primaire est prelevee dans la nature avant conversion."),
 QC("Quelle source est renouvelable ?", "Le charbon~Le gaz naturel~L'eolien~Le petrol", 2,
    "Le vent se renouvelle naturellement, contrairement aux combustibles fossiles."),
 QC("Que designe le mix energetique ?", "Un seul type de centrale~La repartition des sources de production~Le prix de l'electricite~La consommation d'un menage", 1,
    "Le mix decrit la part de chaque source dans la production."),
 QC("Comment definir le facteur de charge ?", "Production reelle / production maximale~Production maximale / production reelle~Prix / production~Production × prix", 0,
    "C'est le rapport entre energie reelle et energie maximale theorique."),
 QC("Quel est un inconvenient majeur du solaire et de l'eolien ?", "Leur cout nul~Leur intermittence~Leur emission de CO2~Leur rupture de stock", 1,
    "La production dépend de l'ensoleillement et du vent."),
 QC("Quel moyen compense l'intermittence ?", "Augmenter les emissions~Le stockage et la diversification~Supprimer le reseau~Arreter la production", 1,
    "Stockage et diversite des sources securisent l'equilibre offre-demande."),
 QC("Quel critere n'intervient pas dans le choix d'un mix ?", "La securite d'approvisionnement~L'empreinte carbone~L'acceptabilite sociale~La couleur des panneaux", 3,
    "Les autres criteres sont des éléments réels du débat énergétique."),
 QT("Expliquer la difference entre energie primaire et energie secondaire avec l'exemple de l'electricite nucleaire.",
    "L'energie primaire est celle que l'on trouve dans la nature sans transformation : ici l'uranium extrait du mineral. L'energie secondaire est produite par conversion de cette energie primaire : la chaleur de la fission est transformee en vapeur, puis en energie mecanique dans la turbine et enfin en electricite par l'alternateur. L'electricite ne se trouve pas a l'etat naturel dans le milieu : c'est toujours un vecteur d'energie fabrique a partir d'une source primaire. Cette distinction permet de calculer un rendement de conversion et de comparer les filieres entre elles sur la base de l'energie primaire consommee, plutot que de la seule electricite livree au reseau.",
    "On identifie l'uranium comme primaire et l'electricite comme secondaire, avec la chaine de conversion."),
 QT("Analyseer les avantages et les limites d'un mix associant nucleaire et renouvelables.",
    "Le nucleaire fournit une production pilotable et continue, avec de faibles emissions de gaz a effet de serre en fonctionnement et une forte densite energetique ; ses limites sont la gestion des dechets radioactifs, le cout du demantèlement et l'acceptabilite sociale. Les renouvelables solaires et eoliens ont une faible empreinte carbone et des couts marginaux de production bas, mais leur production est intermittente et necessite stockage, renforcement du reseau et pilotage de la demande. Associer les deux permet de combiner une base pilotable et des appoints renouvelables, tout en reduisant la part des combustibles fossiles. Le mix optimal depend du territoire, des ressources locales, du cout du capital et des objectifs de reduction des emissions.",
    "On equilibre les avantages et les limites des deux families et on justifie la complementarite.")],
C("Le mix energetique combine des sources primaires converties en vecteurs : le choix arbitre cout, securite, emissions et acceptabilite.",
  "Facteur de charge = energie reelle / energie maximale theorique",
  "Primaire / secondaire · renouvelable / non renouvelable · intermittence et stockage",
  "Energie primaire~Prelevee dans la nature~Energie secondaire~Apres conversion~Mix~Repartition des sources~Intermittence~Production variable",
  "Identifier les sources disponibles|Classer primaire et secondaire|Evaluer facteur de charge et emissions|Analyser la sécurité d'approvisionnement|Arbiter le mix",
  "Confondre electricite et source primaire|Ignorer l'intermittence|Ne regarder que le cout de production|Oublier la fin de vie des installations",
  "Uranium~Primaire non renouvelable~Electricite~Secondaire~Solaire~Renouvelable intermittent~Facteur de charge~Reel sur theorique~Stockage~Compense l'intermittence",
  "Renouvelable~Se renouvelle naturellement~Non renouvelable~Se consomme definitivement",
  "Primaire~Brut~Secondaire~Converti"))

# ============================================================ ENE2
add("ENE2", "Conversion d'energie et rendement des systemes", "Énergie", ["1re"],
S("Une conversion d'energie transforme une forme d'energie en une autre pour rendre un service."
  "|Le principe de conservation de l'energie dit que l'energie totale d'un systeme isolé reste constante."
  "|Lors d'une conversion, une partie de l'énergie est transferee au service utile et une partie est dissipe en chaleur."
  "|Le rendement d'un convertisseur est le rapport entre energie utile en sortie et energie fournie en entree."
  "|Un rendement s'exprime souvent en pourcentage et reste toujours strictement inferieur a 100 %."
  "|Les pertes proviennent des frottements, des resistances electriques, des pertes magnetiques et des transferts thermiques."
  "|Une chaudiere a condensation recupere la chaleur latente des gaz de combustion pour améliorer son rendement."
  "|Un moteur electrique a un rendement plus eleve qu'un moteur thermique dans de nombreuses applications."
  "|Une pile a combustible convertit directement l'energie chimique en electricite, sans etape thermique intermediaire."
  "|Le bilan energetique d'un systeme presente les flux d'entree, de sortie utile et de pertes."
  "|L'energie totale est conservee mais sa qualite diminue : on parle de degradation energetique."
  "|Ameliorer le rendement reduit la consommation de ressources et les emissions pour un meme service rendu."),
[QC("Que dit le principe de conservation de l'energie ?", "L'energie peut apparaitre~L'energie totale d'un systeme isolé reste constante~L'energie disparait toujours~Le rendement vaut toujours 1", 1,
    "L'energie se transforme ou se transfert, mais ne peut etre creee ni detruit."),
 QC("Comment calculer un rendement ?", "E_utile / E_fournie~E_fournie / E_utile~E_utile × E_fournie~E_fournie − E_utile", 0,
    "Le rendement rapporte la sortie utile a l'entree."),
 QC("Quel rendement est physiquement possible ?", "105 %~100 %~92 %~L'infini", 2,
    "Un convertisseur reel a toujours un rendement inferieur a 1."),
 QC("Quelle est une source de pertes electriques ?", "La resistance des conducteurs~Le vide~L'isolement parfait~La temperature de l'air", 0,
    "L'effet Joule dissipe de la chaleur dans les conducteurs resistifs."),
 QC("Que recupere une chaudiere a condensation ?", "Le bruit~La chaleur latente des gaz~La lumiere~Le gaz non brûlé", 1,
    "La condensation des vapeurs de combustion libere de la chaleur supplementaire."),
 QC("Quel est un avantage de la pile a combustible ?", "Conversion directe sans etape thermique~Aucun rendement~Aucun flux d'energie~Production de chaleur uniquement", 0,
    "La conversion electrochimique evite les pertes d'un cycle thermique."),
 QC("Que represente un bilan energetique ?", "Le prix de l'energie~Les flux d'entree, utiles et perdus~La date d'achat~Le nombre de machine", 1,
    "Le bilan rend visibles toutes les formes d'energie du systeme."),
 QT("Un moteur recoit 2000 J et fournit 1560 J de travail utile. Calculer son rendement et les pertes, puis commenter.",
    "Le rendement vaut eta = 1560/2000 = 0,78, soit 78 %. Les pertes representent 2000 − 1560 = 440 J, soit 22 % de l'énergie fournie, principalement sous forme de chaleur due aux frottements et aux pertes electriques. Le bilan energetique s'ecrit : 2000 J d'entree = 1560 J utiles + 440 J dissipés. L'energie totale est bien conservee, mais une partie n'est plus disponible pour le service. Pour améliorer le rendement, on peut reduire les frottements, utiliser des conducteurs de plus faible resistance ou adapter la charge au point de fonctionnement optimal du moteur.",
    "On attend le rendement, les pertes en joules et en pourcentage, le bilan et des pistes d'amelioration."),
 QT("Expliquer la difference entre conservation et degradation de l'energie.",
    "La conservation est une loi fondamentale : dans un systeme isolé, la somme des energies sous toutes leurs formes reste constante ; une conversion ne fait que transformer ou transferer l'energie. La degradation decrit l'autre face du meme processus : l'energie utile, concentree et facilement convertible, est progressivement transformee en chaleur diffuse a basse temperature, difficile a recuperer. Ainsi, le bilan global reste equilibre, mais la qualite de l'energie diminue et le rendement d'une conversion est toujours inferieur a 1. C'est pourquoi on peut consommer de l'energie sans la detruire : on consomme en realite sa capacite a produire un travail. Cette notion justifie les efforts d'eco-conception et de recuperation de chaleur dans les procedes industriels.",
    "On distingue la quantite conservee de la qualite qui se degrade, avec un exemple.")],
C("Une conversion respecte la conservation de l'energie, mais degrade sa qualite : le rendement mesure l'utile sur le fourni.",
  "eta = E_utile / E_fournie · pertes = E_fournie − E_utile",
  "Conservation : energie totale constante · degradation : qualite qui diminue",
  "Conversion~Changement de forme d'energie~Rendement~Utile sur fourni~Pertes~Chaleur dissipee~Bilan~Entree, sortie et pertes",
  "Definir le systeme et ses frontieres|Identifier les energies d'entree et de sortie|Calculer le rendement|Localiser les pertes|Proposer des ameliorations",
  "Oublier les pertes dans le bilan|Donner un rendement superieur a 1|Confondre puissance et energie|Ignorer la chaleur recupérable",
  "2000 J entree~1560 J utiles~Rendement 78 %~440 J de pertes~22 % dissipes~Condensateur thermique~Chaleur latente recuperee",
  "Conservation~Quantite constante~Degradation~Qualite qui baisse",
  "Energie utile~Service rendu~Energie perdue~Chaleur diffuse"))

# ============================================================ ENE3
add("ENE3", "Stockage de l'energie : batteries et supercondensateurs", "Énergie", ["Terminale"],
S("Le stockage permet de decoupler la production et la consommation d'energie dans le temps."
  "|Une batterie accumule de l'energie chimique et la restitue sous forme electrique par des reactions d'oxydoreduction."
  "|Un accumulateur est rechargeable : les reactions sont reversibles, contrairement a une pile primaire non rechargeable."
  "|La capacite d'une batterie se mesure en ampères-heures (Ah) ; elle indique la quantite de charge qui peut etre fournie."
  "|L'energie stockee est approximativement E = U × C, avec U en volts et C en ampères-heures, soit en wattheures."
  "|La tension nominale depend de la chimie : environ 3,7 V pour une cellule lithium-ion et 2 V pour une cellule plomb-acide."
  "|L'etat de charge (SOC) est le rapport entre la capacite restante et la capacite nominale."
  "|Le nombre de cycles designe le nombre de charges et de décharges complets avant une perte de capacite significative."
  "|La profondeur de decharge influence fortement la duree de vie : une decharge complete repetee use davantage la batterie."
  "|Un systeme de gestion de batterie (BMS) surveille la tension, la temperature et l'equilibrage des cellules."
  "|Le supercondensateur stocke l'energie dans un champ electrique : il se charge tres vite et donne de fortes puissances, mais a faible capacite."
  "|Le choix entre batterie et supercondensateur depend du besoin : autonomie pour l'un, pics de puissance pour l'autre."),
[QC("Quelle est l'unite de capacite d'une batterie ?", "Le watt~L'ampere-heure~Le volt~Le joule", 1,
    "L'ampere-heure mesure la quantite de charge disponible."),
 QC("Que designe un accumulateur ?", "Une pile non rechargeable~Une batterie rechargeable~Un condensateur~Un generateur", 1,
    "Les reactions d'un accumulateur sont reversibles."),
 QC("Quelle est la tension nominale d'une cellule lithium-ion ?", "1,2 V~2 V~3,7 V~12 V", 2,
    "Une cellule lithium-ion a une tension nominale d'environ 3,7 V."),
 QC("Quel est le role d'un BMS ?", "Augmenter la tension~Surveiller et proteger la batterie~Refroidir le moteur~Remplacer le chargeur", 1,
    "Le BMS controle tension, courant, temperature et equilibre des cellules."),
 QC("Quel effet a une profondeur de decharge importante ?", "Elle augmente la duree de vie~Elle accelere l'usure de la batterie~Elle n'a aucun effet~Elle change la tension nominale", 1,
    "Les decharges profondes repetees reduisent le nombre de cycles utiles."),
 QC("Quel est un avantage du supercondensateur ?", "Grande autonomie~Charge et decharge tres rapides~Faible cout par kWh~Tension elevee par cellule", 1,
    "Le supercondensateur fournit de fortes puissances pendant de brefs instants."),
 QC("Quelle grandeur donne l'energie stockee approximative ?", "U × C en Ah~U / C~C − U~U + C", 0,
    "E = U × C donne des wattheures si U est en volts et C en ampères-heures."),
 QT("Une batterie de 12 V a une capacite de 50 Ah. Estimer l'energie stockee et l'autonomie pour une consommation moyenne de 120 W.",
    "L'energie stockee vaut approximativement E = U × C = 12 × 50 = 600 Wh, soit 0,6 kWh. En joules, 600 Wh = 600 × 3600 = 2,16 × 10^6 J. Avec une puissance moyenne de 120 W, l'autonomie theorique est t = E/P = 600/120 = 5 heures. En pratique, l'autonomie est plus faible car la capacite utilisable depend de la profondeur de decharge, du rendement du convertisseur, de la temperature et du vieillissement des cellules. On estime souvent 80 % de la capacite utilisable, soit environ 4 heures reelles.",
    "On attend le calcul en Wh, la conversion en joules, l'autonomie theorique et les reserves pratiques."),
 QT("Justifier l'association d'une batterie et d'un supercondensateur dans un vehicule electrique.",
    "La batterie offre une grande capacite et donc une bonne autonomie, mais elle supporte mal les pics de courant eleves et se decharge plus vite si on lui demande de fortes puissances. Le supercondensateur, lui, peut absorber et fournir des courants importants en quelques secondes, avec un tres grand nombre de cycles. Dans un vehicule, on utilise ainsi le supercondensateur pour les phases d'acceleration et de freinage regeneratif, tandis que la batterie fournit l'energie moyenne sur la duree du trajet. Cette association reduit les contraintes sur la batterie, allonge sa duree de vie et ameliore le rendement global de la recuperation d'energie au freinage.",
    "On oppose autonomie et puissance, puis on explique la complementarite avec le freinage regeneratif.")],
C("Batterie et supercondensateur stockent l'energie selon des principes differents : capacite pour l'un, puissance pour l'autre.",
  "E = U × C (Wh) · SOC = capacite restante / capacite nominale",
  "Lithium-ion 3,7 V · oxydoreduction reversible · BMS · supercondensateur a champ electrique",
  "Batterie~Stockage chimique~Capacite~Ampere-heure~Etat de charge~SOC~BMS~Gestion et protection~Supercondensateur~Puissance rapide",
  "Evaluer le besoin en autonomie et en puissance|Choisir la technologie de stockage|Calculer energie et autonomie|Prevoir le BMS et la securite|Verifier les conditions de vieillissement",
  "Confondre Ah et Wh|Negliger la temperature et le vieillissement|Decharger completeement une batterie lithium|Oublier l'equilibrage des cellules",
  "12 V et 50 Ah~600 Wh~0,6 kWh~120 W~5 heures theoriques~80 % utilisables~3,7 V~Cellule lithium-ion",
  "Batterie~Grande capacite~Supercondensateur~Forte puissance instantanee",
  "Capacite~Quantite de charge~Energie~Capacite fois tension"))

# ============================================================ ENE4
add("ENE4", "Reseaux electriques et pilotage intelligent", "Énergie", ["Terminale"],
S("Un reseau electrique achemine l'energie de la production jusqu'aux consommateurs grâce à des lignes et des postes de transformation."
  "|Le transport a haute tension limite les pertes : pour une puissance donnee, une tension elevee reduit l'intensite et donc les pertes Joule."
  "|Les postes de transformation adaptent la tension grâce a des transformateurs, de la haute tension vers la moyenne et la basse tension."
  "|Le reseau de distribution alimente les consommateurs en basse tension, generalement 230 V entre phase et neutre en France."
  "|L'equilibre entre production et consommation doit etre assure en permanence : l'electricite se stocke difficilement a grande echelle."
  "|Le gestionnaire du reseau ajuste la production des moyens pilotables et peut importer ou exporter avec les pays voisins."
  "|Un smart grid (reseau intelligent) integre des capteurs, des communication et des automatismes pour piloter les flux en temps reel."
  "|Les compteurs communicants fournissent des mesures de consommation et permettent des tarifs variables selon les heures."
  "|Le pilotage de la demande consist a deplacer certains usages hors des periodes de pointe, par exemple le chauffage ou la recharge des vehicules."
  "|Les energies reparties, comme les panneaux solaires sur les toits, injectent de l'electricite aux extremites du reseau."
  "|Cette injection peut provoquer des surtensions locales et necessite une surveillance de la qualite de l'energie."
  "|Le stockage distribue et le pilotage sont des leviers pour integrer davantage d'energies renouvelables intermittentes."),
[QC("Pourquoi transporter l'electricite en haute tension ?", "Pour augmenter les pertes~Pour reduire l'intensite et les pertes Joule~Pour changer la frequence~Pour eviter les transformateurs", 1,
    "A puissance egale, P = U I : une tension elevee diminue I et les pertes R I²."),
 QC("Quel appareil adapte la tension dans un poste ?", "Un compteur~Un transformateur~Un disjoncteur~Un alternateur", 1,
    "Le transformateur élève ou abaisse la tension en courant alternatif."),
 QC("Quelle est la tension basse tension courante en France ?", "48 V~110 V~230 V~4000 V", 2,
    "230 V entre phase et neutre, 400 V entre phases."),
 QC("Que faut-il maintenir en permanence sur un reseau ?", "La frequence uniquement~L'equilibre production-consommation~Le nombre de lignes~Le prix", 1,
    "Tout desequilibre se traduit par une variation de frequence ou de tension."),
 QC("Qu'appelle-t-on smart grid ?", "Un reseau sans fil~Un reseau avec capteurs, communication et pilotage~Une ligne haute tension~Un simple compteur", 1,
    "Le reseau intelligent mesure et pilote les flux en temps reel."),
 QC("Quel est un effet des panneaux solaires repartis sur le reseau ?", "Une baisse de tension~Une possible surtension locale~Une hausse de frequence~Aucun effet", 1,
    "L'injection locale en periode de fort ensoleillement peut elever la tension."),
 QC("Que permet le pilotage de la demande ?", "Augmenter la consommation de pointe~Deplacer des usages hors pointe~Supprimer le comptage~Arreter le reseau", 1,
    "Deplacer les usages lisse la courbe de charge et reduit les pics."),
 QT("Expliquer pourquoi l'elevage de tension reduit les pertes sur une ligne, en utilisant P = U I et P_pertes = R I².",
    "Pour transporter une puissance donnee P, on a I = P/U. Plus la tension U est elevee, plus l'intensite I est faible. Or les pertes dans la ligne valent P_pertes = R × I², avec R la resistance des conducteurs. En élevant U d'un facteur 10, on divise I par 10 et on divise les pertes par 100. C'est pourquoi le transport longue distance utilise des tensions de plusieurs centaines de milliers de volts, que l'on abaisse ensuite dans les postes de transformation pour la distribution. Le transformateur est donc un element central de l' efficacite du reseau.",
    "On relie P = U I, P_pertes = R I² et le role du transformateur, avec le facteur 10/100."),
 QT("Décrire comment un smart grid facilite l'integration des energies renouvelables.",
    "Le smart grid collecte des mesures en temps reel grace aux compteurs communicants et aux capteurs repartis sur les lignes. Il detecte les variations locales de tension dues a l'injection solaire ou eolienne et peut agir sur les organes de regulation, sur le stockage distribue ou sur le pilotage de certains usages. Les tarifs variables incitent les consommateurs a deplacer leur consommation vers les periodes de forte production renouvelable. Le gestionnaire dispose ainsi d'une meilleure visibilite et peut remplacer une partie du pilotage de l'offre par un pilotage de la demande. Ces mecanismes permettent d'augmenter la part d'energies intermittentes sans renforcer excessivement le reseau, tout en maintenant la qualite et la securite de l'alimentation.",
    "On cite mesures, regulation, stockage, tarifs et pilotage de la demande.")],
C("Le reseau doit equilibrer production et consommation en permanence ; haute tension et pilotage reduisent les pertes et integrent le renouvelable.",
  "P = U I · P_pertes = R I² · montée en tension → baisse des pertes",
  "Transport, distribution, transformateurs · smart grid · pilotage de la demande",
  "Haute tension~Transport longue distance~Transformateur~Change la tension~Smart grid~Mesure et pilotage~Equilibre~Production egale consommation",
  "Choisir le niveau de tension|Calculer les pertes de la ligne|Surveiller tension et frequence|Piloter offres et usages|Integrer le stockage distribue",
  "Confondre tension et courant|Oublier les pertes en I²|Croire que l'electricite se stocke facilement|Ignorer les surtensions locales",
  "P=U I~I=P/U~Tension ×10~Pertes /100~230 V~Basse tension~Compteur communicant~Mesure en temps reel~Surtension~Injection locale",
  "Transport~Haute tension~Distribution~Basse tension",
  "Pilotage de l'offre~Agir sur la production~Pilotage de la demande~Agir sur les usages"))

# ============================================================ ENE5
add("ENE5", "Batiment basse consommation et audit energetique", "Énergie", ["Terminale"],
S("Le batiment represente une part importante de la consommation d'energie et des emissions de gaz a effet de serre."
  "|La consommation d'un bâtiment se décompose en chauffage, eau chaude, climatisation, eclairage et usages electriques."
  "|Le besoin de chauffage depend du climat, de l'orientation, de l'inertie, de l'isolation et du volume a chauffer."
  "|Les parois perdent de la chaleur par conduction, convection et rayonnement vers l'exterieur."
  "|La resistance thermique R d'une paroi s'exprime en m².K/W : plus R est grand, mieux la paroi isole."
  "|Le coefficient de transmission thermique U est l'inverse de R : plus U est petit, moins il y a de pertes."
  "|Les ponts thermiques sont des zones de perte accrue aux jonctions entre parois, planchers ou menuiseries."
  "|L'étanchéité a l'air limite les infiltrations et les pertes par renouvellement d'air non controle."
  "|Une ventilation controlee assure la qualite de l'air tout en recuperant une partie de la chaleur de l'air extrait."
  "|Les energies renouvelables (pompe a chaleur, solaire thermique, bois) peuvent couvrir une partie des besoins."
  "|Un audit energetique releve les donnees du batiment, calcule les consommations et propose des travaux priorises."
  "|Le diagnostic de performance energetique (DPE) classe le batiment de A a G selon sa consommation et ses emissions."),
[QC("Quelle unité mesure la resistance thermique ?", "W/m²~m².K/W~K/W~J/s", 1,
    "La resistance R s'exprime en m².K/W."),
 QC("Comment eviter les pertes dans une paroi ?", "En diminuant R~En augmentant R~En augmentant U~En supprimant l'isolation", 1,
    "Plus R est grand, plus l'isolation est performante."),
 QC("Quel est un pont thermique ?", "Une zone de perte accrue~Une paroi parfaitement isolee~Une fenetre double vitrage~Une piece chauffee", 0,
    "Les jonctions de parois creent des zones de pertes supplementaires."),
 QC("Que permet une ventilation double flux ?", "Supprimer l'isolation~Recuperer la chaleur de l'air extrait~Augmenter les pertes~Chauffer avec du bois", 1,
    "L'echangeur recupere la chaleur de l'air sortant pour préchauffer l'air neuf."),
 QC("Quel equipement utilise l'energie de l'air pour chauffer ?", "Une chaudiere fuel~Une pompe a chaleur~Un radiateur electrique~Un four", 1,
    "La pompe a chaleur transfert la chaleur de l'air, du sol ou de l'eau."),
 QC("Que fait un audit energetique ?", "Seulement une estimation visuelle~Releve, calcule et propose des travaux~Remplace le chauffage~Vend le batiment", 1,
    "L'audit aboutit a un plan de travaux priorise et chiffre."),
 QC("Que indique le DPE ?", "Le prix du batiment~Une classe de consommation et d'emissions de A a G~Le nombre de pieces~L'annee de vente", 1,
    "Le DPE classe le batiment sur sept lettres, de A a G."),
 QT("Une paroi de 100 m² a un coefficient U = 0,4 W/m².K. Calculer les pertes pour une difference de temperature de 20 K, puis apres isolation avec U = 0,2.",
    "Les pertes par transmission valent P = U × A × ΔT = 0,4 × 100 × 20 = 800 W. Apres isolation, avec U = 0,2 W/m².K, elles deviennent 0,2 × 100 × 20 = 400 W. Le gain est donc de 400 W, soit 50 % de reduction pour cette paroi. Sur une saison de chauffage de 2000 heures, cela represente 0,4 kW × 2000 h = 800 kWh d'economies pour cette seule paroi. Ce calcul simple montre l'interet de l'isolation, mais il faut aussi considerer les ponts thermiques, l'etancheite et le besoin de ventilation dans une approche globale du batiment.",
    "On attend la formule U A ΔT, les deux resultats, le gain et la mise en garde globale."),
 QT("Expliquer pourquoi améliorer l'isolation peut augmenter le besoin de ventilation controlee.",
    "Une maison ancienne laisse entrer l'air par les fissures et les menuiseries : l'air se renouvelle naturellement, mais de maniere incontrolee et avec des pertes de chaleur. Quand on rend l'enveloppe etanche pour reduire les pertes, ce renouvellement naturel disparait. Sans apport d'air neuf, la qualite de l'air interieur se degrade : humidite, odeurs, composes organiques volatils et dioxyde de carbone s'accumulent. Il faut donc installer une ventilation controlee, idealement double flux avec recuperation de chaleur, pour renouveler l'air de maniere saine sans gaspiller l'energie de chauffage. Isolation et ventilation sont deux elements complements d'une conception performante, pas des solutions qui s'excluent.",
    "On relie etancheite, qualite de l'air interieur et recuperation de chaleur.")],
C("L'audit energetique quantifie les pertes et classe le batiment ; isolation et ventilation controlee doivent progresser ensemble.",
  "Pertes = U × A × ΔT · U = 1/R · DPE de A a G",
  "Conduction, convection, rayonnement · ponts thermiques · etancheite a l'air",
  "Resistance thermique~Isolation de la paroi~Coefficient U~Inverse de R~Pont thermique~Perte localisee~DPE~Classe energetique",
  "Relever les caracteristiques du batiment|Calculer les pertes par paroi|Repérer les ponts thermiques|Evaluer l'etancheite et la ventilation|Proposer des travaux priorises",
  "Augmenter l'etancheite sans ventilation|Oublier les ponts thermiques|Confondre R et U|Ne regarder que le cout du chauffage",
  "U=0,4~800 W de pertes~U=0,2~400 W~100 m² et 20 K~Economie de 400 W~DPE~De A a G",
  "Isolation~Reduit les pertes~Ventilation~Renouvelle l'air",
  "R~Resistance~U~Transmission"))

# ============================================================ PHA1
add("PHA1", "Circuits electriques : lois, theoremes et analysis des charges", "Physique appliquée", ["1re"],
S("Un circuit electrique se represente par un schema ou les composants sont reliés par des conducteurs ideels."
  "|La loi d'Ohm s'ecrit U = R I pour un conducteur ohmique a temperature constante."
  "|La loi des noeuds dit que la somme des intensites entrant dans un noeud egale la somme des intensites qui en sortent."
  "|La loi des mailles dit que la somme algebrique des tensions le long d'une maille fermée est nulle."
  "|Un generateur reel se modele par une source de tension ideale en serie avec une resistance interne."
  "|La tension aux bornes d'un generateur en charge est inferieure a sa tension a vide a cause de la resistance interne."
  "|Un pont diviseur de tension donne U2 = U × R2/(R1 + R2) pour deux resistances en serie."
  "|Le theoreme de superposition permet d'étudier un circuit lineaire avec plusieurs generateurs en activant un generateur a la fois."
  "|Dans le theoreme de superposition, un generateur de tension eteint est remplace par un court-circuit, un generateur de courant par un circuit ouvert."
  "|Une diode ne laisse passer le courant que dans un sens ; un transistor peut servir d'interrupteur commande."
  "|La puissance dissipee dans une resistance vaut P = R I² : elle determine le besoin de dissipation thermique du composant."
  "|Avant toute mesure, on verifie le calibre des appareils et l'absence de court-circuit."),
[QC("Que dit la loi des noeuds ?", "Les tensions s'additionnent~Les intensites entrantes egalent les intensites sortantes~La resistance est nulle~Le courant est constant partout", 1,
    "La loi des noeuds est une consequence de la conservation de la charge."),
 QC("Que dit la loi des mailles ?", "La somme des intensites est nulle~La somme algebrique des tensions est nulle~La puissance est constante~Le courant change de sens", 1,
    "Sur une maille fermée, la somme des tensions est nulle."),
 QC("Comment representer un generateur reel ?", "Source ideale sans resistance~Source ideale en serie avec une resistance interne~Resistance seule~Condensateur seul", 1,
    "La resistance interne rend compte de la chute de tension en charge."),
 QC("Quelle est la tension d'un pont diviseur avec U = 12 V, R1 = 2 et R2 = 4 ohms ?", "2 V~4 V~8 V~12 V", 2,
    "U2 = 12 × 4/(2+4) = 8 V."),
 QC("Que faire d'un generateur de tension eteint en superposition ?", "Le remplacer par un circuit ouvert~Le remplacer par un court-circuit~Le doubler~Le supprimer du schema", 1,
    "Une source de tension eteinte a une tension nulle, donc elle se comporte comme un fil."),
 QC("Un generateur de courant eteint devient...", "Un court-circuit~Un circuit ouvert~Une resistance~Une diode", 1,
    "Un courant nul correspond a un circuit ouvert."),
 QC("Quelle puissance dissipe une resistance de 5 ohms parcourue par 3 A ?", "15 W~30 W~45 W~75 W", 2,
    "P = R I² = 5 × 9 = 45 W."),
 QT("Deux resistances de 4 et 6 ohms sont en serie sous 20 V. Calculer l'intensite et la tension aux bornes de chaque resistance.",
    "La resistance equivalent vaut Req = 4 + 6 = 10 ohms. L'intensite est I = U/Req = 20/10 = 2 A, identique dans les deux resistances puisqu'elles sont en serie. Les tensions sont U1 = R1 × I = 4 × 2 = 8 V et U2 = R2 × I = 6 × 2 = 12 V. On verifie la loi des mailles : 8 + 12 = 20 V, ce qui correspond bien a la tension de la source. La puissance dissipee total est P = U × I = 40 W, repartie en 16 W et 24 W.",
    "On attend Req, I, les deux tensions et la verification par la loi des mailles."),
 QT("Expliquer la difference entre une masse et un circuit ouvert dans un montage electronique.",
    "La masse, ou ground, est le point de reference du circuit : on lui attribue conventionnellement le potentiel zero et toutes les tensions sont mesurees par rapport a elle. Dans un montage avec une alimentation double, la masse est souvent le point milieu entre les tensions positives et negatives. Le circuit ouvert, lui, designe une liaison interrompue : aucun courant ne peut y circuler, quelle que soit la tension imposee a ses extremites. Une masse peut parfaitement etre traversee par un courant de retour, alors qu'un circuit ouvert ne le peut pas. Confondre les deux conduit a des erreurs de cablage :Brancher une masse sur une alimentation ou laisser un fil de masse debranché peut mettre hors tension tout le montage.",
    "On definit la masse comme reference de potentiel et le circuit ouvert comme absence de liaison.")],
C("Les lois d'Ohm, des noeuds et des mailles permettent de prevoir et de verifier le comportement d'un circuit.",
  "U = R I · somme des I aux noeuds · somme des U aux mailles",
  "Generateur reel avec resistance interne · pont diviseur · superposition",
  "Loi des noeuds~Conservation du courant~Loi des mailles~Conservation des tensions~Generateur reel~Source et resistance interne~Diviseur~Repartition de tension",
  "Dessiner le schema et nommer les noeuds|Appliquer les lois d'Ohm|Ecrire les equations de noeuds et de mailles|Resoudre le systeme|Verifier par les puissances",
  "Oublier la resistance interne|Mal orienter une tension dans une maille|Superposer tous les generateurs en meme temps|Depasser le calibre d'un ampèremetre",
  "4 et 6 ohms~Req 10 ohms~I = 2 A~U1 = 8 V, U2 = 12 V~Diviseur~12 V, 2 et 4 ohms~P = R I²~45 W",
  "Loi des noeuds~Intensites~Loi des mailles~Tensions",
  "Circuit ouvert~Courant nul~Masse~Potentiel de reference"))

# ============================================================ PHA2
add("PHA2", "Capteurs et conditionnement des signaux", "Physique appliquée", ["1re"],
S("Un capteur transforme une grandeur physique en signal electrique exploitable par un systeme de mesure."
  "|Un capteur passeif, comme une resistance de temperature, modifie une propriete electrique sans produire d'energie."
  "|Un capteur actif, comme une photodiode ou une thermocouple, delivre un signal electrique propre."
  "|La sensibilite d'un capteur est la variation du signal de sortie pour une variation de la grandeur d'entree."
  "|La plage de mesure definit les valeurs minimales et maximales que le capteur peut mesurer correctement."
  "|La resolution est le plus petit ecart de grandeur d'entree que le capteur peut distinguer."
  "|Un signal analogique prend une valeur continue ; un signal numerique est code en 0 et en 1."
  "|Un convertisseur analogique-numerique (CAN) echantillonne puis quantifie le signal pour le traiter par un microcontroleur."
  "|La frequence d'echantillonnage doit etre au moins deux fois superieure a la frequence maximale du signal, selon le theoreme de Shannon."
  "|Un pont de Wheatstone permet de mesurer une faible variation de resistance avec une meilleure precision."
  "|Un amplificateur operationnel peut amplifier, filtrer ou comparer le signal issu du capteur."
  "|Le bruit et la derive thermique limitent la precision : un etalonnage periodically corrige l'offset et le gain."),
[QC("Quel est un capteur passif ?", "Une thermocouple~Une resistance de temperature~Une photodiode~Un generateur photovoltaique", 1,
    "Une resistance de temperature modifie sa resistance sans generer de tension."),
 QC("Que designe la sensibilite ?", "La masse du capteur~La variation de sortie par variation d'entree~La couleur du boitier~La tension d'alimentation", 1,
    "La sensibilite s'exprime en unité de sortie par unité d'entree."),
 QC("Quel est le role d'un CAN ?", "Amplifier la tension~Convertir un signal analogique en nombre~Alimenter le capteur~Filtrer le bruit", 1,
    "Le convertisseur analogique-numerique code la tension mesurée."),
 QC("Selon Shannon, quelle frequence d'echantillonnage minimale pour un signal de 50 Hz ?", "25 Hz~50 Hz~100 Hz~200 Hz", 2,
    "Il faut au moins 2 × 50 = 100 Hz pour éviter le repliement."),
 QC("A quoi sert un pont de Wheatstone ?", "Mesurer une faible variation de resistance~Augmenter la tension~Refroidir le capteur~Supprimer l'alimentation", 0,
    "Le pont equilibre est tres sensible aux petites variations de resistance."),
 QC("Quelle fonction peut remplir un amplificateur operationnel ?", "Uniquement amplifier~Amplifier, filtrer ou comparer~Remplacer le CAN~Mesurer la temperature", 1,
    "L'amplificateur operationnel est un element de conditionnement polyvalent."),
 QC("Quel effet a la derive thermique ?", "Une meilleure resolution~Une erreur qui varie avec la temperature~Un signal numerique~Aucun effet", 1,
    "La derive modifie l'offset ou le gain avec la temperature."),
 QT("Une sonde de temperature delivre 10 mV par degre Celsius et l'entree du CAN va de 0 a 5 V sur 10 bits. Calculer la resolution en temperature.",
    "Un convertisseur 10 bits donne 2^10 = 1024 niveaux, donc un pas de tension de 5/1024 = 4,88 mV. La sonde fournit 10 mV par degré, soit 0,01 V/°C. La resolution en temperature est donc 4,88 mV / 10 mV/°C = 0,488 °C. On peut l'améliorer en amplifiant le signal de la sonde avant le CAN, par exemple avec un gain de 5, ce qui donnerait environ 0,098 °C. On doit cependant verifier que la tension amplifiee reste dans la plage 0 a 5 V sur toute la plage de temperature mesuree.",
    "On attend 1024 niveaux, le pas en volts, la resolution en degrés et l'effet d'un amplificateur."),
 QT("Expliquer pourquoi un etalonnage est necessaire meme avec un capteur de bonne qualite.",
    "Un capteur reels ne suit jamais exactement sa courbe theorique : sa sensibilite peut differer de la valeur nominale, son offset peut etre non nul et sa reponse peut deriver avec la temperature ou vieillir. L'electronique de conditionnement ajoute elle-meme des offsets et des erreurs de gain. L'etalonnage consiste a mesurer la sortie du systeme pour plusieurs valeurs de reference connues, puis a determiner une relation de correction, souvent affine : grandeur corrigee = a × signal + b. On verifie ensuite la qualite de la correction sur des points non utilises pour le calcul. Sans etalonnage, les mesures peuvent etre precises en repetition mais fausses en valeur absolue : c'est une erreur systematique que la resolution de l'appareil ne permet pas de detecter.",
    "On distingue erreur systematique et dispersion, puis on decrit la relation de correction.")],
C("Le conditionnement adapte le signal d'un capteur a la chaine de mesure : sensibilite, bruit, echantillonnage et etalonnage.",
  "Resolution CAN = plage / 2^n · Shannon : fe >= 2 fmax",
  "Capteur passif ou actif · pont de Wheatstone · amplificateur operationnel",
  "Capteur~Grandeur vers signal~Sensibilite~Variation de sortie~Resolution~Plus petit ecart detectable~CAN~Codage numerique",
  "Choisir le capteur et sa plage|Conditionner le signal|Verifier la frequence d'echantillonnage|Etalonner avec des references|Estimer l'incertitude de mesure",
  "Echantillonner au-dessous de 2 fmax|Confondre resolution et precision|Oublier l'offset du capteur|Ne jamais reetalonner",
  "10 mV par degre~CAN 10 bits~5 V sur 1024~Pas 4,88 mV~Resolution 0,488 degre~Shannon~100 Hz pour 50 Hz",
  "Signal analogique~Valeur continue~Signal numerique~Codage binaire",
  "Capteur passif~Modifie une propriete~Capteur actif~Delivre un signal"))

# ============================================================ PHA3
add("PHA3", "Mecanique et cinematique des systemes", "Physique appliquée", ["Terminale"],
S("La cinematique decrit le mouvement des mecanismes sans s'interesser aux forces qui le produisent."
  "|Un mouvement de rotation est caracterise par une vitesse angulaire en rad/s ou en tours/minute."
  "|Un mouvement de translation est caracterise par une vitesse lineaire en m/s."
  "|Pour une roue de rayon R qui roule sans glisser, la vitesse de avancement vaut v = R × omega."
  "|Un engrenage transmet un mouvement de rotation entre deux axes ; le rapport de transmission depend du nombre de dents."
  "|Avec deux roues dentees Z1 et Z2, le rapport de vitesse vaut omega2/omega1 = −Z1/Z2 : le sens de rotation s'inverse."
  "|Une courroie transmet le mouvement entre deux poulies ; un systeme de poulies et de courroies peut aussi reduire la vitesse."
  "|Un mecanisme bielle-manivelle transforme un mouvement de rotation en mouvement de translation alternative."
  "|Un banc d'essai mesure la vitesse, le couple et la puissance d'un actionneur."
  "|Le couple d'un moteur est une grandeur de rotation, exprimee en newtons-metres."
  "|La puissance mecanique en rotation vaut P = M × omega, avec M le couple et omega la vitesse angulaire en rad/s."
  "|Le dimensionnement d'une transmission verifie la puissance transmise, le couple admissible et la duree de vie des pieces."),
[QC("Quelle est l'unite d'une vitesse angulaire ?", "m/s~rad/s~N/m~W/s", 1,
    "La vitesse angulaire s'exprime en radians par seconde."),
 QC("Quelle relation pour une roue qui roule sans glisser ?", "v = omega/R~v = R × omega~v = R/omega~v = R + omega", 1,
    "La vitesse lineaire est le rayon multiplie par la vitesse angulaire."),
 QC("Que vaut omega2/omega1 pour deux engrenages de 20 et 40 dents ?", "2~−0,5~0,5~−2", 1,
    "omega2/omega1 = −Z1/Z2 = −20/40 = −0,5 : la sortie tourne deux fois moins vite en sens inverse."),
 QC("Quel mecanisme transforme une rotation en translation alternative ?", "Un engrenage~Une bielle-manivelle~Une courroie~Un roulement", 1,
    "La bielle-manivelle convertit la rotation en va-et-vient."),
 QC("Quelle est l'unite d'un couple ?", "Le newton~Le newton-metre~Le watt~Le joule", 1,
    "Un couple est un produit de force par bras de levier."),
 QC("Comment calculer la puissance en rotation ?", "P = M/omega~P = M × omega~P = omega/M~P = M + omega", 1,
    "La puissance est le couple multiplie par la vitesse angulaire."),
 QC("Quel element d'un engrenage change le sens de rotation ?", "La courroie~Le contact entre deux roues dentees~Le roulement~Le chassis", 1,
    "Deux roues dentees en prise tournent en sens opposes."),
 QT("Un moteur tourne a 1500 tours/minute avec un couple de 4 N.m. Calculer sa vitesse angulaire et sa puissance.",
    "On convertit la vitesse : 1500 tours/min = 1500 × 2pi/60 = 50pi rad/s, soit environ 157 rad/s. La puissance vaut P = M × omega = 4 × 157 = 628 W, environ 0,63 kW. On peut aussi calculer directement avec la formule P = M × 2pi × N/60. Ce resultat represente la puissance mecanique fournie a l'arbre ; la puissance electrique consommee est superieure car le moteur a un rendement inferieur a 1. Si le rendement vaut 0,85, la puissance electrique absorbee est d'environ 628/0,85 = 739 W.",
    "On attend la conversion tours/min en rad/s, le calcul de puissance et la distinction avec la puissance electrique."),
 QT("Expliquer l'interet d'une reduction de vitesse dans une transmission et ses consequences sur le couple.",
    "Une reduction permite d'adapter la vitesse et le couple d'un moteur a la charge a entrainer. Un moteur tournant vite fournit souvent un couple modeste, alors qu'une charge comme un convoyeur ou un bras de robot demande un couple eleve et une vitesse plus faible. Un reduiseur, par exemple un train d'engrenages avec un rapport de 10, divise la vitesse par 10 et multiplie le couple par 10, a peu de pertes pres. La puissance restant approximativement constante, P = M × omega montre que la baisse de omega compense la hausse de M. En contrepartie, le reduiseur ajoute des pertes, de l'encombrement, du bruit et des besoins de lubrification. Il faut donc choisir le rapport minimal qui satisfait le couple demandé.",
    "On relie couple et vitesse par P = M omega, avec les pertes et les compromis.")],
C("La cinematique quantifie les mouvements ; une transmission adapte vitesse et couple a la charge.",
  "v = R omega · omega2/omega1 = −Z1/Z2 · P = M omega",
  "Rotation et translation · engrenages · courroies · bielle-manivelle",
  "Vitesse angulaire~Radian par seconde~Couple~Newton-metre~Engrenage~Rapport de transmission~Bielle-manivelle~Rotation en translation",
  "Mesurer la vitesse et le couple|Choisir le type de transmission|Calculer le rapport|Verifier la puissance transmise|Tester sur banc d'essai",
  "Oublier la conversion tours/min en rad/s|Ignorer le sens de rotation|Confondre couple et puissance|Negliger les pertes du reduiseur",
  "1500 tours/min~157 rad/s~Couple 4 N.m~Puissance 628 W~Rendement 0,85~739 W consommes~Rapport 10~Couple ×10",
  "Cinematique~Decrit le mouvement~Dynamique~Etudie les forces",
  "Engrenage~Sens inverse~Courroie~Meme sens generalement"))

# ============================================================ PHA4
add("PHA4", "Thermique et transferts de chaleur", "Physique appliquée", ["Terminale"],
S("La chaleur est un transfert d'energie thermique entre deux systemes de temperatures differentes."
  "|La temperature mesure l'agitation thermique des particules ; elle s'exprime en kelvin ou en degre Celsius."
  "|La conversion between les deux echelles est T(K) = t(°C) + 273,15."
  "|Un corps echange de la chaleur par conduction, convection ou rayonnement."
  "|La conduction se produit dans une matiere sans deplacement global de matière, grâce aux collisions microscopiques."
  "|La convection implique le deplacement d'un fluide, naturel sous l'effet de la densite ou force par une pompe ou un ventilateur."
  "|Le rayonnement transmet de l'energie sous forme d'ondes electromagnetiques, meme dans le vide."
  "|Le flux thermique traverse une paroi selon la loi Q/t = U × A × ΔT, avec U le coefficient de transmission."
  "|La capacite thermique d'un corps est la chaleur necessaire pour l'elever d'un kelvin : C = m × c."
  "|La chaleur latente est l'energie absorbee ou liberee lors d'un changement d'etat, senza variation de temperature."
  "|Un echangeur de chaleur transfert de la chaleur entre deux fluides sans les melanger, avec un rendement donne par l'efficacite."
  "|La maitrise des transferts thermiques est essentielle pour le refroidissement des composants electroniques et le confort des batiments."),
[QC("Quelle est la relation entre kelvin et degre Celsius ?", "T = t − 273,15~T = t + 273,15~T = t × 273,15~T = t/273,15", 1,
    "Le zero kelvin correspond a −273,15 degré Celsius."),
 QC("Quel mode de transfert fonctionne dans le vide ?", "La conduction~La convection~Le rayonnement~Aucun", 2,
    "Seul le rayonnement ne necessite pas de milieu materiel."),
 QC("Quel transfert implique le deplacement d'un fluide ?", "La conduction~La convection~Le rayonnement~L'induction", 1,
    "La convection met en jeu un fluide en mouvement."),
 QC("Quelle est la formule du flux a travers une paroi ?", "Q/t = U × A × ΔT~Q/t = U/(A × ΔT)~Q/t = U + A + ΔT~Q/t = A × ΔT/U", 0,
    "Le flux est proportionnel a la surface et a l'ecart de temperature."),
 QC("Comment calculer la capacite thermique d'un corps ?", "m/c~m × c~c/m~m + c", 1,
    "La capacite thermique est la masse fois la capacite thermique massique."),
 QC("Qu'est-ce que la chaleur latente ?", "Une chaleur qui change la temperature~Une chaleur de changement d'etat~Une chaleur invisible~Une chaleur sans source", 1,
    "Lors d'un changement d'etat, l'energie est absorbe ou restituee sans variation de temperature."),
 QC("Quel role d'un echangeur de chaleur ?", "Melanger deux fluides~Transférer la chaleur sans melanger les fluides~Supprimer la chaleur~Augmenter la temperature", 1,
    "Les deux fluides restent separes par une paroi."),
 QT("Une paroi de 20 m² a un coefficient U = 1,5 W/m².K. La difference de temperature est de 15 K. Calculer le flux thermique sur une heure.",
    "Le flux instantaneous vaut Q/t = U × A × ΔT = 1,5 × 20 × 15 = 450 W. Sur une heure, soit 3600 secondes, l'energie transferee est Q = 450 × 3600 = 1 620 000 J, soit 1,62 MJ ou 0,45 kWh. On verifie l'homogeneite : W × s = J. Cette perte represente une consommation permanente tant que l'ecart de temperature est maintenu. Si on isole la paroi pour passer a U = 0,3, le flux tombe a 90 W et l'energie sur une heure a 0,324 kWh, soit une reduction de 80 %.",
    "On attend le flux en watts, l'energie en joules et en kWh, puis l'effet de l'isolation."),
 QT("Expliquer pourquoi un dissipateur thermique ameliore le refroidissement d'un composant electronique.",
    "Un composant electronique dissipe une puissance sous forme de chaleur due a l'effet Joule. Sans evacuation, sa temperature monte jusqu'a la destruction ou a la mise en securite thermique. Le dissipateur est une piece de metal, generalement en aluminium, fixes au composant : il augmente considerablement la surface d'echange avec l'air. Le flux evacue etant proportionnel a la surface et a l'ecart de temperature, cette augmentation de surface abaisse la temperature de fonctionnement. Des ailettes, un ventilateur ou un contact thermique de qualite reduisent encore la resistance thermique entre le composant et l'air. Le dimensionnement verifie que la resistance thermique totale permet de rester sous la temperature maximale admissible dans le pire cas de charge et de temperature ambiante.",
    "On lie puissance dissipee, surface d'echange, resistance thermique et temperature maximale.")],
C("Les transferts thermiques se font par conduction, convection et rayonnement ; le flux depend de U, de la surface et de l'ecart de temperature.",
  "Q/t = U A ΔT · C = m c · T(K) = t(°C) + 273,15",
  "Conduction, convection, rayonnement · chaleur latente · echangeur",
  "Conduction~Transfert dans la matiere~Convection~Transfert par fluide mobile~Rayonnement~Ondes electromagnetiques~Echangeur~Transfert sans melange",
  "Identifier les modes de transfert|Mesurer les temperatures|Calculer le flux et l'energie|Estimer les resistance thermiques|Verifier la temperature maximale admissible",
  "Confondre temperature et chaleur|Oublier la conversion en kelvin|Negliger la chaleur latente|Ignorer la resistance de contact",
  "U=1,5 et 20 m²~450 W~15 K~1,62 MJ~0,45 kWh~U=0,3~90 W~Reduction de 80 %",
  "Temperature~Etat thermique~Chaleur~Energie transferee",
  "Conducteur~Transmet la chaleur~Isolant~Limite le flux"))

# ============================================================ PHA5
add("PHA5", "Automatismes et asservissement en production", "Physique appliquée", ["Terminale"],
S("Un automatisme commande un processus sans intervention humaine permanente, selon une logique predefinie."
  "|Un systeme a boucle ouverte applique une commande sans mesurer le resultat : il ne corrige pas les perturbations."
  "|Un systeme asservi, ou boucle fermee, compare la valeur mesuree a la consigne et corrige l'ecart."
  "|L'ecart, ou erreur, vaut e = consigne − mesure ; le regulateur elabore la commande a partir de cet ecart."
  "|Un regulateur ON/OFF alterne deux etats ; il est simple mais provoque des oscillations autour de la consigne."
  "|Un regulateur proportionnel applique une commande proportionnelle a l'erreur : u = Kp × e."
  "|Le gain Kp trop eleve rend le systeme instable ; trop faible, il laisse un ecart permanent."
  "|Un regulateur PID ajoute une action integrale, qui supprime l'ecart statique, et une action derivée, qui amortit les oscillations."
  "|Un capteur fournit la mesure, un actionneur applique la commande et un automate execute le programme de regulation."
  "|Le temps de reponse, le depassement et l'ecart statique sont des critères de qualite d'un asservissement."
  "|Un automatisme programmable (PLC) s'execute cycliquement : lecture des entrees, traitement, ecriture des sorties."
  "|La securite d'un systeme automatise exige des arrets d'urgence, des verrouillages et une analyse des defaillances."),
[QC("Quelle est la difference entre boucle ouverte et boucle fermee ?", "La boucle fermee ne mesure rien~La boucle fermee compare mesure et consigne~La boucle ouverte corrige les erreurs~Elles sont identiques", 1,
    "La boucle fermee utilise un retour de mesure pour corriger l'ecart."),
 QC("Comment calculer l'erreur d'asservissement ?", "consigne + mesure~consigne − mesure~consigne × mesure~consigne / mesure", 1,
    "L'ecart est la difference entre consigne et mesure."),
 QC("Quel est un inconvenient du regulateur ON/OFF ?", "Il est trop cher~Il oscille autour de la consigne~Il ne peut pas etre programme~Il ne consomme rien", 1,
    "Le basculement entre deux etats provoque un cycle d'oscillation."),
 QC("Que fait l'action integrale d'un PID ?", "Elle accelere la reponse~Elle supprime l'ecart statique~Elle augmente les oscillations~Elle change la consigne", 1,
    "L'integrale accumule l'erreur passee et annule l'ecart permanent."),
 QC("Quel effet d'un gain proportionnel trop eleve ?", "Une reponse plus lente~Une instabilite et des oscillations~Une meilleure stabilite~Aucun effet", 1,
    "Un gain excessif amplifie les corrections et fait osciller le systeme."),
 QC("Quel est le role de l'action derivée ?", "Supprimer l'ecart statique~Amortir les variations rapides~Augmenter le gain~Mesurer la temperature", 1,
    "La derivation anticipe la tendance de l'erreur et amortit le systeme."),
 QC("Quelles phases composent un cycle d'automate ?", "Lecture, traitement, ecriture~Ecriture, lecture, arret~Mesure, consigne, erreur only~Calcul, vente, maintenance", 0,
    "Le automate lit les entrees, traite le programme puis ecrit les sorties."),
 QT("Expliquer le fonctionnement d'un asservissement de temperature dans un four, en identifiant consigne, mesure, ecart et actionneur.",
    "La consigne est la temperature souhaitee, par exemple 180 °C. Une sonde mesure la temperature reelle dans le four et transmet la valeur au regulateur. Celui-ci calcule l'ecart e = 180 − mesure. Si l'ecart est positif, il commande une puissance de chauffage plus eleve ; si l'ecart est negatif ou nul, il reduit ou coupe la puissance. L'actionneur est ici une resistance de chauffage pilote par un relais statique. Avec un simple ON/OFF, la temperature oscille de part et d'autre de 180 °C. Un regulateur PID module en continu la puissance pour arriver a la consigne sans depassement excessif ni ecart permanent. Les criteres de qualite sont le temps de montee en temperature, le depassement maximal et la stabilite en regime etabli.",
    "On identifie les quatre elements et on compare ON/OFF et PID avec les criteres de performance."),
 QT("Pourquoi un arret d'urgence doit-il agir independamment du programme de l'automate ?",
    "Le programme de l'automate peut contenir une erreur, rester bloque dans une boucle ou etre perturbe par une panne de capteur. Si la securite dependait uniquement de ce programme, un defaut logiciel pourrait empecher la machine de s'arreter en cas de danger. Un arret d'urgence est donc cablé en dur : il coupe directement l'alimentation des actionneurs ou force une entree de securite traitée par un circuit dedie, independamment du cycle de l'automate. Ce circuit est concu pour etre defaillant-safe : un fil coupe ou un contact ouvert doit conduire a l'arret, pas a la continuation du mouvement. On complete par des verrouillages mecaniques, des detecteurs de presence et une analyse des risques conforme aux normes de securite des machines.",
    "On justifye l'independance matérielle, le principle defaillant-safe et les verrouillages.")],
C("Un asservissement compare en permanence consigne et mesure ; la qualite du regulateur se juge au temps de reponse, au depassement et a l'ecart statique.",
  "e = consigne − mesure · P : u = Kp e · PID : proportionnel + integrale + derivé",
  "Boucle ouverte / fermee · regulateur ON/OFF · cycle automate lecture-traitement-ecriture",
  "Consigne~Valeur souhaitee~Mesure~Valeur reellement obtenue~Regulateur~Elabore la commande~Actionneur~Applique l'action",
  "Definir la consigne et la grandeur a regler|Choisir le capteur et l'actionneur|Choisir la loi de commande|Regler les gains et tester|Verifier la securite et les defaillances",
  "Regler un gain au hasard|Oublier le retour de mesure|Confondre integrateur et deriveur|Laisser l'arret d'urgence dependre du programme",
  "Four a 180 degres~Ecart et commande~ON/OFF~Oscillations~PID~Sans ecart statique~Cycle~Lecture, traitement, ecriture",
  "Boucle ouverte~Pas de retour~Boucle fermee~Retour et correction",
  "Proportionnel~Rapide mais ecart~Integrale~Annule l'ecart statique"))

# ============================================================ MTA1
add("MTA1", "Fonctions et derivation : analyser une variation", "Mathématiques appliquées", ["1re"],
S("Une fonction decrit une relation entre une grandeur d'entree et une grandeur de sortie."
  "|La derivee f'(x) donne la vitesse de variation de la fonction au point x."
  "|La derivee est la pente de la tangente a la courbe representatives de f au point considere."
  "|Si f'(x) > 0 sur un intervalle, la fonction est croissante ; si f'(x) < 0, elle est decroissante."
  "|Un point ou la derivee s'annule et change de signe est un extremum local."
  "|La derivee de x^n vaut n x^(n−1) ; la derivee d'une constante est nulle."
  "|La derivee d'un produit uv vaut u'v + uv' ; celle d'un quotient u/v vaut (u'v − uv')/v²."
  "|Laderivee d'une composee f(g(x)) vaut g'(x) × f'(g(x)) : c'est la regle de la chaine."
  "|Une variation instantanée peut s'ecrire df ≈ f'(x) × dx pour un petit accroissement dx."
  "|En physique, la vitesse est la derivee de la position par rapport au temps et l'acceleration la derivee de la vitesse."
  "|Un capteur delivrant une tension en fonction de la temperature a une sensibilite donnee par la derivee de cette fonction."
  "|L'optimisation d'un systeme revient souvent a chercher un extremum d'une fonction de cout, de rendement ou de masse."),
[QC("Que represente la derivee d'une fonction ?", "Sa valeur moyenne~La pente de la tangente~Son aire~Sa racine", 1,
    "La derivee est la pente de la tangente au point considere."),
 QC("Que vaut la derivee de x³ ?", "3x²~x²~3x~x⁴/4", 0,
    "La regle donne n x^(n−1), soit 3x²."),
 QC("Quelle est la condition pour qu'une fonction soit decroissante ?", "f'(x) > 0~f'(x) < 0~f'(x) = 0~f'(x) indefinie", 1,
    "Une derivee negative sur un intervalle implique la decroissance."),
 QC("Que se passe-t-il a un extremum local ?", "La derivee est maximale~La derivee s'annule et change de signe~La fonction est nulle~La derivee est infinie", 1,
    "La tangente y est horizontale et le sens de variation s'inverse."),
 QC("Quelle est la derivee d'un produit uv ?", "u'v'~u'v + uv'~uv~u'/v'", 1,
    "La regle du produit donne u'v + uv'."),
 QC("Quelle est la vitesse d'un mobile ?", "La derivee de sa position~L'integrale de sa position~Sa position multipliee par le temps~Sa masse", 0,
    "v(t) = x'(t)."),
 QC("Comment approximes-t-on une petite variation de f ?", "df ≈ f'(x) dx~df ≈ f(x) dx~df ≈ f'(x)/dx~df ≈ f(x) + dx", 0,
    "Le differential donne une approximation locale lineaire."),
 QT("Une fonction de position est x(t) = t² − 4t + 3, avec t en secondes et x en metres. Calculer vitesse, acceleration et la position minimale.",
    "La vitesse vaut x'(t) = 2t − 4, en m/s. L'acceleration vaut x''(t) = 2 m/s², constante et positive. La vitesse s'annule pour 2t − 4 = 0, soit t = 2 s ; comme l'acceleration est positive, ce point est un minimum. La position minimale est x(2) = 4 − 8 + 3 = −1 m. On peut ecrire x(t) = (t − 2)² − 1, ce qui confirme le minimum en t = 2. Le mobile se rapproche de l'origine jusqu'a 2 s puis s'en eloigne, avec une vitesse negative puis positive.",
    "On attend les deux derivees, l'annulation de la vitesse et la valeur minimale."),
 QT("Expliquer comment la derivee permet de definir la sensibilite d'un capteur et pourquoi elle peut varier avec la grandeur mesuree.",
    "La sensibilite d'un capteur est la variation du signal de sortie pour une petite variation de la grandeur d'entree : c'est precisement la derivee de la fonction de transfert dy/dx. Si la relation est lineaire, la derivee est constante et la sensibilite est la meme partout. Si la relation est non lineaire, par exemple pour une thermistance, la derivee depend de la temperature : le capteur est plus sensible a basse temperature qu'a haute temperature. On peut alors utiliser un developpement local y(x + dx) ≈ y(x) + y'(x) dx pour estimer la mesure, ou linéariser la relation autour du point de fonctionnement. La connaissance de la derivee permet aussi de choisir la plage de mesure ou la sensibilite est suffisante pour la precision requise.",
    "On relie sensibilite et derivee, avec le cas lineaire et non lineaire.")],
C("La derivee mesure une variation instantanee : elle donne la pente, le sens de variation et les extrema d'une fonction.",
  "f'(x) = pente de la tangente · df ≈ f'(x) dx",
  "(x^n)' = n x^(n−1) · (uv)' = u'v + uv' · chaine : (f∘g)' = g' f'(g)",
  "Derivee~Pente de la tangente~Croissance~Derivee positive~Extremum~Derivee nulle et signe changeant~Sensibilite~Derivee de la reponse",
  "Identifier la fonction et la variable|Deriver avec les regles|Etudier le signe de la derivee|Repérer les extrema|Interpreter dans le contexte technique",
  "Oublier le Facteur n dans (x^n)'|Confondre derivee et valeur de la fonction|Conclure sur un extremum sans changer de signe|Ignorer les unites de la derivee",
  "x(t)=t²−4t+3~v=2t−4~a=2 m/s²~Minimum en t=2 s~x=-1 m~Thermistance~Sensibilite variable~df ≈ f' dx",
  "Derivee~Variation instantanee~Derivee seconde~Variation de la derivee",
  "Croissant~f' positif~Decroissant~f' negatif"))

# ============================================================ MTA2
add("MTA2", "Fonctions exponentielles et logarithmiques : modeliser une croissance", "Mathématiques appliquées", ["1re"],
S("Une fonction exponentielle est de la forme f(x) = a^x avec a > 0 et a different de 1."
  "|Si a > 1 la fonction est croissante ; si 0 < a < 1 elle est decroissante."
  "|Toutes les exponentielles passent par le point (0 ; 1), car a^0 = 1."
  "|La fonction exponentielle de base e, notee exp, verifie exp'(x) = exp(x) : elle est sa propre derivee."
  "|La fonction logarithme neperien ln est la reciproque de exp : ln(e^x) = x et e^(ln x) = x pour x > 0."
  "|Le domaine de definition de ln est l'intervalle ]0 ; +infini[ ; ln(1) = 0."
  "|La derivee de ln(x) est 1/x pour x > 0."
  "|Les proprietes du logarithme sont ln(ab) = ln a + ln b, ln(a/b) = ln a − ln b et ln(a^n) = n ln a."
  "|Un phenomenone de croissance ou de decroissance proportionnelle se modele par y(t) = y0 × e^(k t)."
  "|Le temps de doublement d'une croissance exponentielle vaut T = ln(2)/k."
  "|En technologie, la decharge d'un condensateur ou le refroidissement d'un corps suivent une loi exponentielle decroissante."
  "|La constante de temps d'un systeme donne l'echelle de temps de sa reponse : apres une constante de temps, l'ecart a la valeur finale est divise par e."),
[QC("Par quel point passe toute fonction exponentielle ?", "(0 ; 0)~(0 ; 1)~(1 ; 0)~(1 ; 1)", 1,
    "a^0 = 1 quelle que soit la base a."),
 QC("Quelle est la derivee de exp(x) ?", "x exp(x)~exp(x)~1/x~0", 1,
    "La fonction exponentielle de base e est sa propre derivee."),
 QC("Quel est le domaine de definition de ln ?", "Tout ℝ~]0 ; +infini[~[0 ; +infini[~]−infini ; 0[", 1,
    "Le logarithme n'est defini que pour les nombres strictement positifs."),
 QC("Que vaut ln(1) ?", "0~1~e~Indefini", 0,
    "Le logarithme de 1 est nul quelle que soit la base."),
 QC("Comment ecrire ln(ab) ?", "ln a × ln b~ln a + ln b~ln(a+b)~ln a − ln b", 1,
    "Le logarithme d'un produit est la somme des logarithmes."),
 QC("Quel est le temps de doublement pour y = y0 e^(k t) ?", "1/k~ln(2)/k~k/ln(2)~2k", 1,
    "On resout e^(kT) = 2, donc T = ln(2)/k."),
 QC("Que vaut la derivee de ln(x) ?", "1/x~x~ln(x)~−1/x²", 0,
    "Pour x > 0, la derivee de ln est 1/x."),
 QT("Une population de cellules double toutes les 3 heures. Ecrire son evolution et calculer le facteur apres 12 heures.",
    "On modele la population par N(t) = N0 × 2^(t/3), avec t en heures, ou encore N(t) = N0 × e^(k t) avec k = ln(2)/3 environ 0,231 par heure. Apres 12 heures, on a quatre periods de doublement, donc N(12) = N0 × 2^4 = 16 N0. Avec la forme exponentielle, N(12) = N0 × e^(0,231 × 12) = N0 × e^2,77 environ 16 N0. Le resultat confirme la cohérence des deux ecritures. On peut aussi calculer le temps necessaire pour atteindre 100 N0 : t = ln(100)/k environ 20 heures.",
    "On attend le modele, la valeur du facteur 16 et l'equivalence des deux formes."),
 QT("Expliquer pourquoi la constante de temps d'un systeme du premier ordre est liee a la fonction exponentielle.",
    "Un systeme du premier ordre, comme un condensateur qui se charge ou un corps qui se refroidit, obeit a une equation differentielle ou la vitesse de variation est proportionnelle a l'ecart restant : dy/dt = −(y − y_final)/tau. La solution est y(t) = y_final + (y_initial − y_final) × e^(−t/tau). L'ecart a la valeur finale diminue donc de facon exponentielle. Quand t = tau, l'ecart est multiplie par e^(−1) environ 0,37 : il reste 37 % de l'ecart initial. Apres 3 tau, il en reste environ 5 %, ce qui defini pratiquement la fin de la transient. La constante de tau caracterise ainsi la rapidite de la reponse du systeme et se lit directement dans l'exposant.",
    "On relie equation differentielle, solution exponentielle et interpretation de tau.")],
C("Exponentielle et logarithme decrivent croissances, decroissances et temps de reponse ; ln sert a resoudre les exposants.",
  "y = y0 e^(k t) · temps de doublement = ln(2)/k · exp' = exp · (ln)' = 1/x",
  "a^0 = 1 · ln(1) = 0 · ln(ab) = ln a + ln b · constante de temps tau",
  "Exponentielle~Croissance proportionnelle~Par 0,1~Passe par (0,1)~Logarithme~Reciproque de exp~Constante de temps~Echelle de reponse",
  "Reconnaitre une loi exponentielle|Choisir la base ou le parametre k|Utiliser ln pour isoler le temps|Calculer un temps de doublement|Verifier l'ordre de grandeur",
  "Appliquer ln a + ln b a ln(a+b)|Oublier le domaine de ln|Confondre k et temps de doublement|Ignorer la constante de temps",
  "Doublement en 3 h~k = ln2/3~Apres 12 h~Facteur 16~ln(100)/k~Environ 20 h~e^(−t/tau)~37 % apres tau",
  "Exponentielle~Croissance ou decroissance~Lineaire~Variation constante",
  "ln~Reciproque de exp~exp~Base e"))

# ============================================================ MTA3
add("MTA3", "Statistiques et probabilites pour l'ingenieur", "Mathématiques appliquées", ["1re"],
S("La statistique et les probabilites permettent de quantifier la variabilite des mesures et des procedes."
  "|Une variable aleatoire associe une valeur numerique a chaque issue d'une experience aleatoire."
  "|Une loi de probabilite attribue une probabilite a chaque valeur possible ; la somme des probabilites vaut 1."
  "|L'esperance E(X) est la moyenne theorique de la variable aleatoire : E(X) = somme x_i p_i."
  "|La variance V(X) mesure la dispersion : V(X) = E(X²) − [E(X)]² ; l'ecart-type est sa racine carree."
  "|Dans un univers fini equiprobable, P(A) = nombre d'issues favorables / nombre total d'issues."
  "|Deux evenements independants verifient P(A ∩ B) = P(A) × P(B)."
  "|Deux evenements incompatibles ne peuvent pas survenir ensemble : P(A ∪ B) = P(A) + P(B)."
  "|La probabilite conditionnelle P(A sachant B) = P(A ∩ B)/P(B) permet de raisonner avec une information partielle."
  "|Un arbre pondere calcule les probabilites composees en multipliant les probabilites le long des branches."
  "|La loi binomiale modele le nombre de succes parmi n essais independants de meme probabilite p."
  "|Un intervalle de confiance encadre une estimation avec un niveau de confiance : il doit toujours être accompagne de la taille de l'echantillon."),
[QC("Que vaut la somme des probabilites d'une loi ?", "0~1~L'infini~Cela depend de l'experience", 1,
    "Les probabilites de toutes les issues possibles somment a 1."),
 QC("Comment calculer une esperance ?", "Somme des x_i multipliés par p_i~Somme des p_i seuls~Valeur maximale~Racine de la variance", 0,
    "E(X) est une moyenne pondérée par les probabilites."),
 QC("Quelle est la formule de la variance ?", "E(X²) + [E(X)]²~E(X²) − [E(X)]²~E(X)² − E(X²)~E(X) × E(X²)", 1,
    "La variance est l'esperance du carre moins le carre de l'esperance."),
 QC("Que caracterise l'independance de deux evenements ?", "P(A∩B)=P(A)+P(B)~P(A∩B)=P(A)×P(B)~P(A)=P(B)~A et B sont incompatibles", 1,
    "L'independance se traduit par la multiplication des probabilites."),
 QC("Quelle loi modele le nombre de pieces defectueuses sur un lot de n ?", "La loi uniforme~La loi binomiale~La loi exponentielle~La loi normale uniquement", 1,
    "La loi binomiale compte les succes parmi n essais independants."),
 QC("Quel est le role d'un arbre pondere ?", "Tracer un circuit~Calculer des probabilites composees~Mesurer une tension~Representer un plan", 1,
    "On multiplie les probabilites le long des branches et on additionne les issues favorables."),
 QC("Quelles informations doivent accompagner un intervalle de confiance ?", "La couleur du graphique~Le niveau de confiance et la taille de l'echantillon~Le nom du laboratoire~La date seulement", 1,
    "Sans niveau de confiance ni effectif, un intervalle n'est pas interpretable."),
 QT("Une production comporte 5 % de pieces defectueuses. On preleve 10 pieces au hasard. Quelle est la probabilite qu'il y ait exactement une piece defectueuse ?",
    "On utilise la loi binomiale B(n = 10, p = 0,05). La probabilite d'exactement un defaut vaut P(X = 1) = C(10,1) × 0,05 × 0,95^9. Le coefficient binomial vaut 10, 0,95^9 environ 0,630, donc P(X = 1) environ 10 × 0,05 × 0,630 = 0,315, soit 31,5 %. La probabilite d'aucun defaut est 0,95^10 environ 0,599, et celle d'au moins un defaut est 1 − 0,599 = 0,401. Ces resultats supposent un tirage independant et un taux de defaut stable pendant le prelevement.",
    "On attend l'identification de la loi binomiale, le calcul et les hypotheses."),
 QT("Expliquer la difference entre probabilite et frequence observee, et pourquoi un grand echantillon ne garantit pas une probabilite exacte.",
    "La probabilite est une valeur theorique deduite d'un modele, tandis que la frequence est une valeur observee sur un echantillon : elle est egale au nombre de realisations de l'evenement divise par l'effectif. La loi des grands nombres dit que la frequence tend vers la probabilite quand l'effectif augmente, mais la convergence est progressive et aleatoire. Avec 1000 tirages d'une piece equilibre, on n'obtient pas exactement 500 piles : l'ecart residuel est de l'ordre de la racine de l'effectif. Un grand echantillon reduit l'incertitude sans l'annuler. C'est pourquoi on accompagne une estimation d'un intervalle de confiance et d'un niveau de confiance, en indiquant aussi la taille de l'echantillon et le mode de prelevement.",
    "On distingue modele et observation, avec la loi des grands nombres et l'incertitude residuelle.")],
C("Probabilites et statistiques quantifient l'alea : esperance pour la tendance, variance pour la dispersion, intervalles pour la confiance.",
  "E(X) = somme x_i p_i · V(X) = E(X²) − [E(X)]²",
  "Independance : P(A∩B)=P(A)P(B) · loi binomiale B(n,p)",
  "Variable aleatoire~Issue numerique~Esperance~Moyenne theorique~Variance~Dispersion~Loi binomiale~Succes sur n essais",
  "Identifier l'experience et les issues|Choisir la loi de probabilite|Calculer esperance et ecart-type|Construire un intervalle de confiance|Interpreter avec les hypotheses",
  "Confondre frequence et probabilite|Oublier les conditions d'independance|Donner un intervalle sans niveau de confiance|Ignorer la taille de l'echantillon",
  "5 % de defauts~n=10~P(X=1) environ 31,5 %~P(X=0) environ 59,9 %~E(X)~0,5 defaut~Arbre pondere~Produits sur les branches",
  "Esperance~Tendance centrale~Variance~Dispersion autour de l'esperance",
  "Independance~Produit des probabilites~Incompatibilite~Somme nulle"))

# ============================================================ MTA4
add("MTA4", "Geometrie appliquee : vecteurs, distances et volumes", "Mathématiques appliquées", ["1re"],
S("La geometrie dans l'espace permet de decrire la position et la forme des objets techniques."
  "|Dans un repere orthonormal, un point est repere par trois coordonnees (x ; y ; z)."
  "|Un vecteur possede une direction, un sens et une norme ; il est represente par ses composantes."
  "|La norme d'un vecteur de composantes (a ; b ; c) vaut la racine de a² + b² + c²."
  "|La distance entre deux points est la norme du vecteur qui les relie."
  "|Deux vecteurs sont orthogonaux si leur produit scalaire est nul."
  "|Le produit scalaire de deux vecteurs vaut u·v = norme(u) × norme(v) × cos(theta)."
  "|Une droite peut etre representee par un point et un vecteur directeur ; un plan par un point et deux vecteurs directeurs."
  "|Le volume d'un cylindre vaut pi r² h, celui d'une sphere 4/3 pi R³ et celui d'un cube c³."
  "|L'aire de la surface latérale d'un cylindre vaut 2 pi r h."
  "|Une homothetie de rapport k multiplie toutes les longueurs par k, les aires par k² et les volumes par k³."
  "|Le passage d'une maquette a l'objet reel utilise ces relations d'echelle pour estimer masse et cout."),
[QC("Comment calculer la norme d'un vecteur (a ; b ; c) ?", "a+b+c~racine de a²+b²+c²~a²+b²+c²~a×b×c", 1,
    "La norme est la racine carree de la somme des carres des composantes."),
 QC("Que signifie un produit scalaire nul ?", "Les vecteurs sont parallèles~Les vecteurs sont orthogonaux~Les vecteurs sont egaux~Les vecteurs sont nuls", 1,
    "Le produit scalaire s'annule pour deux vecteurs perpendiculaires."),
 QC("Que vaut le produit scalaire u·v ?", "||u|| + ||v||~||u|| ||v|| cos(theta)~||u|| / ||v||~cos(theta) seul", 1,
    "Le produit scalaire fait intervenir les normes et le cosinus de l'angle."),
 QC("Quel est le volume d'une sphere de rayon R ?", "pi R²~4/3 pi R³~4 pi R²~2 pi R³", 1,
    "Le volume d'une sphere vaut 4/3 pi R³."),
 QC("Quel est l'effet d'une homothetie de rapport 2 sur les volumes ?", "Ils doublent~Ils sont multipliés par 4~Ils sont multipliés par 8~Ils sont divises par 2", 2,
    "Les volumes sont multiplies par k³, donc par 8."),
 QC("Quelle est l'aire latérale d'un cylindre ?", "pi r²~2 pi r h~pi r h~2 pi r²", 1,
    "Le developpement de la surface latérale est un rectangle de cote 2 pi r et h."),
 QC("Comment representer une droite dans l'espace ?", "Par un point et un vecteur directeur~Par deux points seulement~Par trois plans~Par un seul nombre", 0,
    "Un point et un vecteur directeur suffisent a definir une droite."),
 QT("Calculer la distance entre A(1 ; 2 ; 2) et B(4 ; 6 ; 2), puis Donner la norme du vecteur AB.",
    "Le vecteur AB a pour composantes (4−1 ; 6−2 ; 2−2) = (3 ; 4 ; 0). Sa norme vaut racine de 3² + 4² + 0² = racine de 25 = 5. La distance AB est donc 5 unites. On remarque que les deux points ont la meme coordonnee z : ils appartiennent au meme plan horizontal et la distance se calcule comme dans le plan avec le theoreme de Pythagore sur un triangle 3-4-5. Ce type de calcul sert par exemple a verifier l'encombrement entre deux composants dans un modele 3D.",
    "On attend les composantes, la norme et la verification par le triangle 3-4-5."),
 QT("Une maquette au 1/10 a une masse de 0,5 kg. Estimer la masse de l'objet reel de meme materiau et meme forme.",
    "Une homothetie de rapport k = 10 multiplie les longueurs par 10, les aires par 100 et les volumes par 1000. La masse etant proportionnelle au volume pour un meme materiau, elle est multipliee par 10³ = 1000. La masse de l'objet reel est donc d'environ 0,5 × 1000 = 500 kg. Ce resultat est une estimation : il suppose que la maquette et l'objet ont exactement la meme forme et sont realises dans le meme materiau. Dans la pratique, une maquette utilise souvent des materiaux differents et des parties pleines la ou l'objet reel est creux, ce qui rend le calcul direct approximatif. On peut alors raisonner sur les volumes de matiere plutot que sur le volume total.",
    "On applique k³ aux volumes et a la masse, puis on discute les hypotheses.")],
C("Vecteurs et coordonnees permettent de calculer distances et angles ; les relations d'echelle relient maquette et objet reel.",
  "||u|| = racine(a²+b²+c²) · u·v = ||u|| ||v|| cos(theta)",
  "Longueurs ×k · aires ×k² · volumes et masses ×k³",
  "Vecteur~Direction, sens et norme~Produit scalaire~Test d'orthogonalite~Distance~Norme du vecteur relatif~Homothetie~Changement d'echelle",
  "Placer les points dans un repere|Calculer les composantes du vecteur|En deduire la norme ou l'angle|Appliquer les relations d'echelle|Verifier la coherence physique",
  "Confondre composantes et coordonnees|Oublier la racine carree|Appliquer k² aux volumes|Supposer une maquette du meme materiau sans le verifier",
  "A(1;2;2) et B(4;6;2)~AB=(3;4;0)~Distance 5~Triangle 3-4-5~Maquette 1/10~Masse ×1000~0,5 kg donne 500 kg",
  "Vecteur~Grandeur directionnelle~Point~Position dans l'espace",
  "Orthogonal~Produit scalaire nul~Parallele~Vecteurs proportionnels"))

# ============================================================ MTA5
add("MTA5", "Modelisation et resolution numerique", "Mathématiques appliquées", ["1re"],
S("La modelisation consiste a traduire une situation reelle en relations mathematiques exploitables."
  "|Un modele est une simplification : il conserve les elements utiles et ignore les details sans influence notable."
  "|Les variables du modele sont les grandeurs que l'on peut faire varier ; les parametres sont fixés pour une etude donnee."
  "|Un modele direct calcule la sortie connaissant les entrees et les parametres."
  "|Un modele inverse recherche les entrees produisant une sortie souhaitee : il necessite souvent la resolution d'une equation."
  "|Une equation non lineaire peut se resoudre par la methode de dichotomie si la fonction change de signe sur un intervalle."
  "|La dichotomie divise l'intervalle en deux à chaque iteration et conserve le demi-intervalle ou le signe change."
  "|Une méthode itérative s'arrête lorsque la precision demandee est atteinte ou apres un nombre maximal d'iterations."
  "|La convergence designe le fait que les approximations se rapprochent de la solution exacte."
  "|Un resultat numerique doit etre accompagne d'une estimation d'erreur et d'un nombre de chiffres significatifs coherent avec les donnees."
  "|Un modele doit etre valide en comparant ses predictions avec des mesures reelles sur un jeu de donnees independant."
  "|En STI2D, ces outils servent a regler un regulateur, estimer une constante de temps ou dimensionner un actionneur."),
[QC("Qu'est-ce qu'un modele ?", "Une copie exacte du reel~Une simplification utile du reel~Un plan de fabrication~Un logiciel de dessin", 1,
    "Le modèle sélectionne les éléments pertinents et néglige les détails inutiles."),
 QC("Quelle est la difference entre variable et parametre ?", "La varie, l'autre est fixé pour l'etude~Les deux varient~Aucune difference~Le parametre est toujours une longueur", 0,
    "Les variables changent ; les parametres sont constants dans une etude donnee."),
 QC("Quand utiliser la dichotomie ?", "Quand la fonction est croissante seulement~Quand la fonction change de signe sur un intervalle~Quand la solution est entière~Jamais", 1,
    "Le changement de signe garantit une racine sur l'intervalle par le theoreme des valeurs intermediaires."),
 QC("Comment la dichotomie réduit-elle l'intervalle ?", "Elle le multiplie par deux~Elle le divise par deux~Elle le supprime~Elle le decale", 1,
    "On garde le demi-intervalle ou le signe change."),
 QC("Que designe la convergence ?", "L'arret du calcul~Le rapprochement vers la solution~L'augmentation de l'erreur~Le changement de modele", 1,
    "Les iterations se rapprochent de la solution exacte."),
 QC("Quand arreter une methode iterative ?", "Au hasard~Quand la precision demandee est atteinte~Toujours apres 100 iterations~Quand le resultat est arondi", 1,
    "On fixe un critere d'arret et un nombre maximal d'iterations."),
 QC("Quel accompagnement est indispensable pour un resultat numerique ?", "Une estimation d'erreur et des chiffres significatifs coherents~La couleur du graphique~Le nom du logiciel~La date de calcul", 0,
    "La qualite du resultat depend de la precision des donnees et de l'erreur de methode."),
 QT("Resoudre par dichotomie l'equation x³ + x − 1 = 0 sur [0 ; 1] avec trois iterations, en encadrant la solution.",
    "On pose f(x) = x³ + x − 1. f(0) = −1 et f(1) = 1 : la fonction change de signe, donc une racine existe sur [0 ; 1]. Premiere iteration : milieu 0,5, f(0,5) = 0,125 + 0,5 − 1 = −0,375 < 0, on garde [0,5 ; 1]. Deuxieme : milieu 0,75, f(0,75) = 0,422 + 0,75 − 1 = 0,172 > 0, on garde [0,5 ; 0,75]. Troisieme : milieu 0,625, f(0,625) = 0,244 + 0,625 − 1 = −0,131 < 0, on garde [0,625 ; 0,75]. La solution est donc encadree par 0,625 et 0,75, avec une precision de 0,125 apres trois iterations ; la valeur exacte est environ 0,682.",
    "On attend les evaluations successives, le choix des demi-intervalles et l'encadrement final."),
 QT("Expliquer pourquoi la validation d'un modele sur des donnees independantes est indispensable.",
    "Un modèle peut reproduire très bien les données qui ont servi a l'elaborer, par exemple en ajustant trop de parametres : c'est le surajustement. Il peut alors donner des predictions fausses sur de nouvelles situations. Pour evaluer sa qualite reelle, on reserve une partie des mesures, ou un jeu de donnees different, et on compare les predictions du modele a ces valeurs non utilisees dans le reglage. On mesure l'ecart moyen et l'ecart maximal, puis on verifie que les erreurs sont comparables a l'incertitude des mesures. Si les erreurs sont beaucoup plus grandes, le modele est invalidé ou ses hypotheses doivent être revues. Cette demarche distingue la qualite d'ajustement interne de la capacite predictive, seule utile pour dimensionner un systeme reel.",
    "On oppose ajustement interne et prediction, avec surajustement et comparaison aux incertitudes.")],
C("Modeliser, c'est simplifier puis resoudre et valider : une solution numerique n'a de valeur que si son erreur et son domaine sont connus.",
  "Dichotomie : garder le demi-intervalle ou f change de signe",
  "Direct / inverse · convergence · critere d'arret · validation sur donnees independantes",
  "Modele~Representation simplifiee~Variable~Grandeur libre~Parametre~Grandeur fixee~Dichotomie~Recherche de racine",
  "Definir les variables et les hypotheses|Ecrire les relations du modele|Choisir une methode de resolution|Fixer le critere d'arret|Valider sur de nouvelles donnees",
  "Confondre modele et realite|Oublier le changement de signe avant dichotomie|Donner un resultat sans estimation d'erreur|Valider sur les donnees d'ajustement",
  "x³+x−1~Racine entre 0,625 et 0,75~Trois iterations~Precision 0,125~Surajustement~Predictions fausses~Jeu independant~Validation",
  "Modele direct~Des entrees vers la sortie~Modele inverse~De la sortie vers les entrees",
  "Convergence~Vers la solution~Divergence~Eloignement de la solution"))

valider_et_ecrire(F, "sti2d-mat-part-B.json")
