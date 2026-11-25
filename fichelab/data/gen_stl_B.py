# -*- coding: utf-8 -*-
"""Generateur stl-mat-part-B.json — lot B : specialites STL (20 fiches).

Chimie de laboratoire (5), Biochimie (4), Microbiologie (4),
Physique appliquee (4), Analyses et dosages (3).
Chaque fiche : 12 points, 9 questions (7 QCM + 2 texte), 7 blocs, 3 schemas.
Annees : uniquement 1re et Terminale (filtres de l'application).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _stl_common import FIL, REF, S, R, QC, QT, C, build, valider_et_ecrire

F = []


def add(prefix, titre, mat, ans, points, questions, c):
    F.append(build(prefix, titre, mat, ans, points, questions, c))


# ============================================================ CH1
add("CH1", "Nomenclature IUPAC et groupements fonctionnels", "Chimie de laboratoire", ["1re"],
S("La nomenclature IUPAC donne à chaque composé organique un nom unique construit selon des règles précises."
  "|On identifie d'abord la fonction chimique principale, puis on choisit la chaîne carbonée la plus longue qui la contient."
  "|L'ordre de priorité place l'acide carboxylique devant l'ester, l'aldéhyde, la cétone, l'alcool et l'amine."
  "|Les préfixes carbonés sont méth- pour 1 carbone, éth- pour 2, prop- pour 3, but- pour 4, pent- pour 5 et hex- pour 6."
  "|Le suffixe -ane désigne un alcane saturé, -ène une double liaison et -yne une triple liaison."
  "|Un alcool porte le suffixe -ol, un aldéhyde -al, une cétone -one et un acide carboxylique -oïque."
  "|La numérotation de la chaîne donne à la fonction principale l'indice le plus bas possible."
  "|Les substituants sont nommés en préfixes avec leur indice de position, par exemple 2-méthylbutane."
  "|La formule brute donne le nombre d'atomes de chaque élément, tandis que la formule semi-développée montre l'enchaînement."
  "|Deux composés de même formule brute mais de structures différentes sont des isomères."
  "|Un ester est nommé « ...oate de ...yle » : la partie acide précède la partie alcool."
  "|Savoir lire un nom et le traduire en formule est indispensable pour préparer une solution ou interpréter une analyse."),
[QC("Quel suffixe caractérise un acide carboxylique ?", "-ol~-al~-oïque~-one", 2,
     "L'acide carboxylique porte le suffixe -oïque, comme l'acide éthanoïque."),
 QC("Quel préfixe correspond à quatre atomes de carbone ?", "Prop-~But-~Pent-~Hex-", 1,
     "But- correspond à quatre carbones : butane, butanol."),
 QC("Quelle fonction est la plus prioritaire en nomenclature ?", "Alcool~Amine~Acide carboxylique~Cétone", 2,
     "L'acide carboxylique est prioritaire ; les autres fonctions deviennent des préfixes."),
 QC("Que désigne le suffixe -ène ?", "Une triple liaison~Une double liaison~Un alcool~Un acide", 1,
     "Le suffixe -ène indique une double liaison carbone-carbone."),
 QC("Comment nomme-t-on l'ester CH₃COOCH₂CH₃ ?", "Éthanoate d'éthyle~Acide éthanoïque~Éthanol éthylique~Méthanoate de méthyle", 0,
     "La partie acide est l'éthanoate et la partie alcool est l'éthyle."),
 QC("Que sont deux isomères ?", "Deux noms différents d'un même composé~Deux structures différentes de même formule brute~Deux fonctions identiques~Deux réactifs d'une réaction", 1,
     "Les isomères ont la même formule brute mais un enchaînement différent."),
 QC("Quelle règle guide la numérotation de la chaîne ?", "Donner l'indice le plus bas à la fonction principale~Commencer par le carbone le plus à droite~Numéroter dans l'ordre alphabétique~Utiliser toujours 1", 0,
     "On numérote pour attribuer l'indice le plus petit à la fonction prioritaire."),
 QT("Nommer le composé CH₃–CH(OH)–CH₂–CHO en justifiant chaque choix.",
    "La fonction prioritaire est l'aldéhyde, portée par le suffixe -al. La chaîne la plus longue qui contient ce groupement compte quatre carbones : on part donc du butanal. On numérote à partir de la fonction aldéhyde, qui reçoit toujours l'indice 1. Le groupement hydroxyle se trouve alors sur le carbone 3 et est nommé en préfixe. Le nom complet est 3-hydroxybutanal. On vérifie que la formule développée est cohérente avec ce nom.",
    "On identifie la fonction prioritaire, la longueur de chaîne, la numérotation puis le préfixe."),
 QT("Expliquer pourquoi l'acide éthanoïque et le méthanoate de méthyle ont la même formule brute.",
    "L'acide éthanoïque CH₃COOH et le méthanoate de méthyle HCOOCH₃ ont tous deux pour formule brute C₂H₄O₂. Leurs atomes sont identiques en nombre mais leur enchaînement diffère : le premier possède une fonction acide carboxylique −COOH, le second une fonction ester −COO−. Ce sont donc des isomères de fonction. Cette différence de structure explique des propriétés très distinctes, notamment un pH acide en solution aqueuse pour l'acide et une odeur fruitée pour l'ester.",
    "On donne la formule brute commune et on montre que le groupement fonctionnel diffère.")],
C("Nommer un composé, c'est repérer sa fonction prioritaire, sa chaîne et la position de ses substituants.",
  "préfixe + radical + suffixe + indicès de position",
  "priorité COOH > COOR > CHO > CO > OH > NH₂ · isomérie",
  "Fonction~Groupement prioritaire~Donne le suffixe~Chaîne~Suite de carbones~La plus longue~Indice~Position~Le plus bas~Préfixe~Substituant~2-méthyl~Suffixe~Fonction principale~-ol, -al, -oïque~Formule brute~Atomes presents~C₂H₄O₂~Isomère~Même brute, structure differ~",
  "Repérer tous les groupements fonctionnels|Classer par ordre de priorité|Choisir la chaîne la plus longue|Numéroter pour minimiser l'indice|Écrire le nom et vérifier la formule",
  "Donner le suffixe à une fonction secondaire|Compter les carbones d'un cycle comme une chaîne|Oublier les indicès de position|Confondre formule brute et semi-développée|Nommer un ester dans le mauvais sens",
  "CH₃OH~Méthanol~CH₃COOH~Acide éthanoïque~CH₃COOCH₃~Éthanoate de méthyle~3-hydroxybutanal~Aldéhyde prioritaire~C₂H₄O₂~Deux isomères",
  "Acide carboxylique~Prioritaire~Alcool~Secondaire",
  "Formule brute~C₂H₄O₂~Formule semi-developpee~CH₃COOH"))

# ============================================================ CH2
add("CH2", "Équilibres chimiques et cinétique réactionnelle", "Chimie de laboratoire", ["1re"],
S("Une réaction chimique est décrite par une équation bilan équilibrée qui conserve les atomes de chaque élément."
  "|Une réaction est totale lorsqu'elle consomme presque complètement les réactifs limitants."
  "|Une réaction est incomplète ou limitée lorsqu'elle s'arrête avant la consommation totale des réactifs."
  "|À l'équilibre, les réactions directe et inverse se déroulent à la même vitesse : les concentrations restent constantes."
  "|L'équilibre est dynamique : les transformations continuent à l'échelle microscopique sans changement macroscopique."
  "|La constante d'équilibre K relie les concentrations à l'équilibre selon la loi d'action de masse."
  "|Le principe de Le Châtelier prédit qu'un système à l'équilibre réagit pour s'opposer à une perturbation."
  "|Une augmentation de température favorise le sens endothermique de la réaction."
  "|Une augmentation de pression favorise le sens qui diminue le nombre de moles gazeuses."
  "|La vitesse de réaction dépend de la concentration des réactifs, de la température et de la présence d'un catalyseur."
  "|Un catalyseur accélère la réaction en abaissant l'énergie d'activation, sans être consommé ni déplacer l'équilibre."
  "|Suivre l'évolution d'une réaction par des mesures de concentration permet de tracer une courbe de cinétique."),
[QC("Que se passe-t-il à l'équilibre chimique ?", "La réaction s'arrête totalement~Les réactions directe et inverse ont la même vitesse~Les réactifs disparaissent~La température augmente", 1,
     "L'équilibre est dynamique : deux vitesses égales et des concentrations constantes."),
 QC("Que prédit le principe de Le Châtelier ?", "Le système s'oppose à la perturbation~Le système accélère la perturbation~La température reste toujours constante~L'équilibre est supprimé", 0,
     "Le système évolue dans le sens qui compense partiellement la perturbation."),
 QC("Quel effet a un catalyseur sur l'équilibre ?", "Il déplace l'équilibre~Il accélère la réaction sans déplacer l'équilibre~Il consomme les réactifs~Il change la constante K", 1,
     "Le catalyseur agit sur la cinétique, pas sur la thermodynamique."),
 QC("Une augmentation de température favorise…", "Le sens exothermique~Le sens endothermique~Aucun sens~La formation du catalyseur", 1,
     "Le système consomme la chaleur ajoutée en favorisant le sens endothermique."),
 QC("Comment nomme-t-on une réaction qui s'arrête avant d'épuiser les réactifs ?", "Totale~Incomplète ou limitée~Exothermique~Instantanée", 1,
     "Une réaction incomplète atteint un état d'équilibre avec des réactifs encore présents."),
 QC("Sur quoi porte la loi d'action de masse ?", "Sur la masse des réactifs~Sur le produit des concentrations à l'équilibre~Sur la température initiale~Sur le volume du réacteur", 1,
     "La constante K est le rapport des concentrations à l'équilibre, élevées aux coefficients stœchiométriques."),
 QC("Quel facteur n'augmente pas la vitesse d'une réaction ?", "Une température plus élevée~Une concentration plus forte~Un catalyseur~Une dilution des réactifs", 3,
     "Diluer diminue les concentrations et donc la vitesse."),
 QT("Expliquer la différence entre équilibre statique et équilibre dynamique, puis illustrer avec la réaction entre l'acide éthanoïque et l'éthanol.",
    "Un équilibre statique supposerait que toute transformation a cessé. En chimie, l'équilibre est dynamique : les réactions directe et inverse continuent à se produire à l'échelle moléculaire, mais à vitesses égales, de sorte que les concentrations macroscopiques ne varient plus. Pour l'estérification de l'acide éthanoïque par l'éthanol, l'acide et l'alcool réagissent pour former l'éthanoate d'éthyle et de l'eau, tandis que l'ester s'hydrolyse en sens inverse. À l'équilibre, les deux vitesses s'équilibrent et le mélange contient à la fois des réactifs et des produits.",
    "On oppose l'absence de mouvement au mouvement compensé, puis on illustre par une estérification."),
 QT("Un mélange à l'équilibre est refroidi pour une réaction exothermique dans le sens direct. Que se passe-t-il et pourquoi ?",
    "Le refroidissement retire de l'énergie thermique au système. Selon Le Châtelier, le système réagit en produisant de la chaleur, c'est-à-dire en favorisant le sens exothermique, ici le sens direct. La quantité de produits augmente et celle des réactifs diminue jusqu'à un nouvel état d'équilibre. La constante d'équilibre dépendant de la température, sa valeur augmente dans le cas d'une réaction exothermique refroidie. En revanche, l'ajout d'un catalyseur n'aurait aucune influence sur la composition finale : il ne ferait qu'accélérer l'atteinte de l'équilibre.",
    "On applique Le Châtelier au sens exothermique et on précise que K change avec la température.")],
C("Un équilibre est dynamique : deux vitesses égales, des concentrations constantes, et une réponse prévisible aux perturbations.",
  "à l'équilibre : v_directe = v_inverse",
  "Le Châtelier · constante K · catalyseur · énergie d'activation",
  "Équilibre~Vitesses égales~Concentrations constantes~Dynamique~Réactions inverse et directe~Microscopique~Constante K~Loi d'action de masse~Rapport des concentrations~Le Châtelier~Opposition à la perturbation~Concentration, pression, temperature~Catalyseur~Baisse Ea~Non consomme",
  "Équilibrer l'équation de la réaction|Déterminer les concentrations initiales|Suivre l'évolution jusqu'à stabilisation|Appliquer Le Châtelier à la perturbation|Comparer les états avant et après",
  "Croire que l'équilibre est statique|Confondre catalyseur et déplacement d'équilibre|Oublier que K dépend de la température|Mal identifier le sens endothermique|Négliger les réactifs restants",
  "Estérification~Acide + alcool~Ester + eau~v directe = v inverse~Equilibre~Refroidissement~Sens exothermique favorise~Catalyseur~Atteinte plus rapide",
  "Réaction totale~Réactifs épuisés~Réaction limitée~Réactifs restants",
  "Équilibre statique~Aucune réaction~Équilibre dynamique~Deux vitesses égales"))

# ============================================================ CH3
add("CH3", "Titrage acido-basique et exploitation de la courbe", "Chimie de laboratoire", ["Terminale"],
S("Un titrage acido-basique permet de déterminer la concentration d'une solution acide ou basique inconnue."
  "|La solution titrée est placée dans une éprouvette graduée ou un erlenmeyer avec un volume connu V₁."
  "|La solution titrante, de concentration connue c₂, est versée progressivement à l'aide d'une burette."
  "|À l'équivalence, les quantités de matière d'acide et de base sont en proportions stœchiométriques."
  "|Pour un acide monoprotonique et une base forte, c₁·V₁ = c₂·V₂ à l'équivalence."
  "|Le volume équivalent est le volume de solution titrante versé à l'équivalence, noté V_eq."
  "|La courbe de titrage donne le pH du mélange en fonction du volume versé."
  "|Le point d'inflexion de la courbe correspond à l'équivalence : la pente y est maximale."
  "|Un indicateur coloré doit avoir une zone de virage incluse dans la partie à forte pente de la courbe."
  "|Pour un titrage acide fort-base forte, le pH à l'équivalence vaut environ 7 à 25 °C."
  "|Pour un acide faible titré par une base forte, le pH à l'équivalence est supérieur à 7."
  "|La précision du résultat dépend de la qualité de la burette, du repérage du virage et de la répétabilité des essais."),
[QC("Quel matériel sert à verser la solution titrante ?", "Une pipette~Une burette~Une éprouvette~Un bécher", 1,
     "La burette permet un ajout progressif et la lecture du volume versé."),
 QC("Que vaut le pH à l'équivalence d'un titrage acide fort-base forte ?", "0~7~9~14", 1,
     "Le sel formé est neutre : le pH vaut environ 7 à 25 °C."),
 QC("Comment repère-t-on l'équivalence sur une courbe de titrage ?", "Au point le plus bas~Au point d'inflexion~Au début de la courbe~À la fin de la courbe", 1,
     "Le point d'inflexion correspond à la pente maximale et à l'équivalence."),
 QC("Quelle relation utilise-t-on pour un acide monoprotonique ?", "c₁V₁ = c₂V₂~c₁/V₁ = c₂/V₂~c₁ + V₁ = c₂ + V₂~c₁V₂ = c₂²", 0,
     "À l'équivalence, les quantités de matière sont égales : c₁V₁ = c₂V₂."),
 QC("Où doit se situer la zone de virage de l'indicateur ?", "Avant le titrage~Dans la partie à forte pente~Après l'équivalence~N'importe où", 1,
     "La zone de virage doit encadrer le saut de pH à l'équivalence."),
 QC("Quel pH attendre pour un acide faible titré par une base forte ?", "Inférieur à 7~Égal à 7~Supérieur à 7~Égal à 0", 2,
     "La base conjuguée de l'acide faible hydrolyse l'eau : le pH devient basique."),
 QC("Quel facteur améliore la précision du titrage ?", "Verser très vite~Répéter les essais et lire la burette à hauteur d'oeil~Choisir un indicateur quelconque~Ne pas rincer la burette", 1,
     "La répétabilité et une lecture correcte du volume réduisent l'incertitude."),
 QT("Une solution d'acide chlorhydrique de volume 20,0 mL est titrée par une solution de soude 0,100 mol/L. Le virage survient après 15,0 mL. Calculer la concentration de l'acide.",
    "À l'équivalence, pour HCl + NaOH → NaCl + H₂O, les quantités de matière sont égales : n(HCl) = n(NaOH) = c₂·V₂ = 0,100 × 0,0150 = 1,50 × 10⁻³ mol. La concentration de l'acide vaut alors c₁ = n/V₁ = 1,50 × 10⁻³/0,0200 = 0,0750 mol/L. On peut aussi écrire directement c₁ = c₂V₂/V₁ = 0,100 × 15,0/20,0 = 0,0750 mol/L. On exprime le résultat avec trois chiffres significatifs, cohérents avec la précision des volumes relevés.",
    "On convertit les volumes en litres, on calcule la quantité de matière à l'équivalence puis la concentration."),
 QT("Expliquer comment choisir un indicateur coloré pour un titrage et que faire si aucun indicateur ne convient.",
    "On trace ou on consulte la courbe de titrage pour connaître le pH à l'équivalence et l'ampleur du saut de pH. L'indicateur choisi doit changer de couleur dans une zone de virage comprise dans ce saut, afin que le virage coïncide avec l'équivalence. Par exemple, la phénolphtaléine convient pour un acide faible et une base forte, tandis que le bleu de bromothymol convient pour un acide fort et une base forte. Si aucun indicateur ne donne un virage assez net, on utilise un pH-mètre et on détermine l'équivalence par le point d'inflexion de la courbe, ce qui est plus précis et permet de titrer des solutions colorées.",
    "On relie la zone de virage au saut de pH et on propose le pH-métrage comme solution de repli.")],
C("Le titrage convertit un volume versé en concentration : l'équivalence est le pivot de tout le calcul.",
  "à l'équivalence : c₁V₁ = c₂V₂ (acide monoprotonique)",
  "burette · volume équivalent · point d'inflexion · zone de virage · pH-mètre",
  "Solution titrée~Volume connu V₁~Dans l'erlenmeyer~Solution titrante~Concentration connue c₂~Dans la burette~Équivalence~Quantités proportionnelles~c₁V₁ = c₂V₂~V_eq~Volume verse~Lecture de la burette~Courbe~pH en fonction du volume~Point d'inflexion~Saut de pH",
  "Rincer et remplir la burette avec la solution titrante|Pipeter un volume connu de solution titrée|Ajouter l'indicateur choisi|Verser goutte à goutte jusqu'au virage stable|Lire V_eq et calculer la concentration",
  "Verser trop vite près du virage|Oublier de Convertir les mL en L|Choisir un indicateur hors du saut de pH|Confondre solution titrée et titrante|Ne pas répéter le titrage",
  "V₁ = 20,0 mL~c₂ = 0,100 mol/L~V_eq = 15,0 mL~c₁ = 0,0750 mol/L~Acide fort-base forte~pH = 7~Acide faible-base forte~pH > 7",
  "Indicateur~Zone de virage~pH-mètre~Point d'inflexion",
  "Titrage~Détermine une concentration~Dilution~Modifie une concentration"))

# ============================================================ CH4
add("CH4", "Oxydoréduction et piles électrochimiques", "Chimie de laboratoire", ["Terminale"],
S("Une réaction d'oxydoréduction met en jeu des transferts d'électrons entre réactifs."
  "|L'oxydation est la perte d'électrons et la réduction est le gain d'électrons."
  "|Un oxydant capte des électrons tandis qu'un réducteur en cède : les deux processus sont simultanés."
  "|Le nombre d'oxydation permet de suivre les changements d'état d'oxydation des atomes."
  "|Une augmentation du nombre d'oxydation correspond à une oxydation, une diminution à une réduction."
  "|Un couple oxydant-réducteur s'écrit Ox + n e⁻ ⇌ Red."
  "|Le potentiel standard E° caractérise la tendance d'un couple à capter des électrons."
  "|Plus E° est élevé, plus l'oxydant du couple est puissant."
  "|Une réaction d'oxydoréduction est spontanée si l'oxydant a un potentiel plus élevé que le réducteur."
  "|La force électromotrice d'une pile vaut E = E°(cathode) − E°(anode)."
  "|À la cathode a lieu la réduction, à l'anode l'oxydation."
  "|Les piles, la corrosion et les réactions d'oxydation des métaux illustrent ces notions en laboratoire."),
[QC("Qu'est-ce que l'oxydation ?", "Un gain d'électrons~Une perte d'électrons~Un échange de protons~Une dissolution sans transfert", 1,
     "L'oxydation correspond à une perte d'électrons."),
 QC("Quel est le rôle d'un réducteur ?", "Capiter des électrons~Céder des électrons~Restant neutre~Augmenter le pH", 1,
     "Le réducteur cède des électrons et s'oxyde."),
 QC("Comment évolue le nombre d'oxydation lors d'une réduction ?", "Il augmente~Il diminue~Il reste nul~Il double", 1,
     "Gagner des électrons fait diminuer le nombre d'oxydation."),
 QC("Comment s'écrit un couple oxydant-réducteur ?", "Ox + n e⁻ ⇌ Red~Red + n e⁻ ⇌ Ox~Ox + Red ⇌ e⁻~Ox ⇌ Red sans électrons", 0,
     "Le couple s'écrit Ox + n e⁻ ⇌ Red."),
 QC("Que signifie un potentiel standard élevé ?", "Un oxydant faible~Un oxydant puissant~Un réducteur puissant~Une réaction lente", 1,
     "Un E° élevé indique une forte tendance à capter des électrons."),
 QC("Où a lieu l'oxydation dans une pile ?", "À la cathode~À l'anode~Dans le pont salin~Dans le fil", 1,
     "L'anode est le siège de l'oxydation ; la cathode, de la réduction."),
 QC("Comment calcule-t-on la tension d'une pile ?", "E = E°(anode) − E°(cathode)~E = E°(cathode) − E°(anode)~E = E°(anode) + E°(cathode)~E = E°/n", 1,
     "La force électromotrice est la différence des potentiels cathode moins anode."),
 QT("Déterminer les nombres d'oxydation du zinc et du cuivre dans la réaction Zn + Cu²⁺ → Zn²⁺ + Cu et identifier l'oxydant et le réducteur.",
    "Le zinc à l'état métallique a un nombre d'oxydation de 0, de même que le cuivre métallique. Dans Zn²⁺, le zinc vaut +2 : il est passé de 0 à +2, donc il a perdu deux électrons et s'est oxydé. Dans Cu²⁺, le cuivre vaut +2 et devient 0 : il a gagné deux électrons et s'est réduit. Le cuivre Cu²⁺ est donc l'oxydant, puisqu'il capte les électrons, et le zinc métallique est le réducteur. Les deux demi-réactions sont Zn → Zn²⁺ + 2 e⁻ et Cu²⁺ + 2 e⁻ → Cu.",
    "On calcule les variations de nombres d'oxydation, puis on nomme oxydant et réducteur."),
 QT("Expliquer le fonctionnement d'une pile galvanique et le rôle du pont salin.",
    "Une pile galvanique sépare les deux demi-réactions dans deux compartiments : l'oxydation se produit à l'anode et la réduction à la cathode. Les électrons circulent de l'anode vers la cathode dans le circuit externe, ce qui produit un courant électrique. Dans chaque compartiment, la réaction déséquilibre les charges : le pont salin laisse migrer des ions pour compenser ces excès de charge et maintenir l'électroneutralité des solutions, tout en évitant le mélange direct des réactifs. Sans lui, la réaction s'arrêterait rapidement par accumulation de charges. La tension mesurée dépend de la différence des potentiels standards des deux couples.",
    "On décrit le trajet des électrons, le rôle des compartiments et la compensation ionique du pont salin.")],
C("L'oxydoréduction est un transfert d'électrons : l'un perd, l'autre gagne, et la différence de potentiel crée la tension.",
  "E = E°(cathode) − E°(anode)",
  "oxydation = perte e⁻ · réduction = gain e⁻ · anode / cathode",
  "Oxydation~Perte d'electrons~A l'anode~Reduction~Gain d'electrons~A la cathode~Oxydant~Capte les electrons~E° eleve~Reducteur~Cede les electrons~E° faible~Couple~Ox + n e⁻ ⇌ Red~Potentiel~Tendance a capter~Force electromotrice~E cathode moins E anode",
  "Écrire les deux demi-réactions|Calculer les nombres d'oxydation|Comparer les potentiels standards|Repérer anode et cathode|Calculer la tension de la pile",
  "Confondre oxydation et réduction|Inverser anode et cathode|Soustraire les potentiels dans le mauvais sens|Oublier de multiplier les électrons|Ignorer le rôle du pont salin",
  "Zn~0 à +2~Oxydation~Cu²⁺~+2 à 0~Reduction~E° élevé~Oxydant puissant~E = E° cath − E° anod~Tension de la pile",
  "Anode~Oxydation~Cathode~Reduction",
  "Oxydant~Capte e⁻~Reducteur~Cede e⁻"))

# ============================================================ CH5
add("CH5", "Alcools, acides carboxyliques et esters", "Chimie de laboratoire", ["Terminale"],
S("Un alcool possède un groupement hydroxyle −OH fixé sur un atome de carbone."
  "|On classe les alcools en primaire, secondaire ou tertiaire selon le nombre de carbones liés au carbone porteur du −OH."
  "|L'oxydation d'un alcool primaire donne un aldéhyde puis un acide carboxylique."
  "|L'oxydation d'un alcool secondaire donne une cétone, qui ne s'oxyde pas facilement davantage."
  "|Un alcool tertiaire résiste à l'oxydation douce car son carbone porteur du −OH n'a pas d'hydrogène."
  "|Un acide carboxylique possède le groupement −COOH et forme des ions carboxylate en solution."
  "|L'estérification est la réaction d'un acide carboxylique avec un alcool pour donner un ester et de l'eau."
  "|Cette réaction est lente, réversible et catalysee par un acide fort comme l'acide sulfurique concentré."
  "|La saponification est la réaction inverse : l'ester est hydrolysé en présence de soude pour donner un carboxylate et un alcool."
  "|L'équilibre d'estérification peut être déplacé vers les produits en excès d'alcool ou en éliminant l'eau."
  "|Les esters ont souvent des odeurs fruitées et servent d'arômes ou de solvants."
  "|La manipulation de l'acide sulfurique concentré et du méthanol exige des EPI et une hotte aspirante."),
[QC("Quel groupement caractérise un acide carboxylique ?", "−OH~−CHO~−COOH~−NH₂", 2,
     "Le groupement carboxyle −COOH définit les acides carboxyliques."),
 QC("Quel produit obtient-on par oxydation d'un alcool secondaire ?", "Un aldéhyde~Une cétone~Un acide~Un ester", 1,
     "Un alcool secondaire s'oxyde en cétone."),
 QC("Quel alcool résiste à une oxydation douce ?", "Primaire~Secondaire~Tertiaire~Méthanol", 2,
     "L'alcool tertiaire n'a pas d'hydrogène sur le carbone porteur du hydroxyle."),
 QC("Que donne l'estérification ?", "Un acide et de l'eau~Un ester et de l'eau~Un aldéhyde et un alcool~Une cétone et du CO₂", 1,
     "Acide + alcool donnent ester + eau."),
 QC("Quel catalyseur accélère l'estérification ?", "La soude~L'acide sulfurique concentré~Le chlorure de sodium~L'eau", 1,
     "Un acide fort catalyse la réaction d'estérification."),
 QC("Que produit la saponification d'un ester par la soude ?", "Un acide et un alcool~Un carboxylate et un alcool~Une cétone et de l'eau~Un aldéhyde et du méthanol", 1,
     "En milieu basique, l'ester donne un ion carboxylate et un alcool."),
 QC("Comment déplacer l'équilibre vers la formation d'ester ?", "En ajoutant de l'eau~En excès d'alcool ou en éliminant l'eau~En retirant l'acide~En refroidissant fortement", 1,
     "Selon Le Châtelier, excès d'un réactif ou retrait d'un produit favorise la formation d'ester."),
 QT("Écrire l'équation de l'estérification de l'acide éthanoïque par l'éthanol et nommer le produit formé.",
    "CH₃COOH + HOCH₂CH₃ ⇌ CH₃COOCH₂CH₃ + H₂O. Le produit est l'éthanoate d'éthyle, un ester à odeur fruitée. La réaction est réversible et catalysée par quelques gouttes d'acide sulfurique concentré. Pour obtenir un bon rendement, on utilise un excès d'éthanol ou on élimine l'eau au fur et à mesure, ce qui déplace l'équilibre vers la formation de l'ester selon le principe de Le Châtelier.",
    "On écrit l'équation équilibrée, on nomme l'ester et on justifie le déplacement de l'équilibre."),
 QT("Expliquer pourquoi un alcool tertiaire ne peut pas être oxydé dans les conditions douces de laboratoire.",
    "L'oxydation d'un alcool consiste à retirer un atome d'hydrogène porté par le carbone qui porte le groupement −OH, ainsi qu'un hydrogène du hydroxyle, pour former une double liaison avec l'oxygène. Sur un alcool tertiaire, ce carbone est lié à trois autres carbones et ne porte aucun hydrogène : la réaction ne peut donc pas avoir lieu dans les conditions habituelles. Une oxydation forte provoquerait une rupture de liaisons C−C, donnant un mélange de produits. Les alcools primaires et secondaires, qui possèdent au moins un hydrogène sur ce carbone, s'oxydent respectivement en aldéhydes puis acides, ou en cétones.",
    "On explique l'absence d'hydrogène sur le carbone hydroxyle et on compare avec les autres classes.")],
C("Alcools, acides et esters forment une chaîne de transformations où l'oxydation et l'estérification sont les pivots.",
  "acide + alcool ⇌ ester + eau",
  "primaire → aldéhyde → acide · secondaire → cétone · tertiaire non oxydable",
  "Alcool primaire~Un carbone voisin~Aldéhyde puis acide~Alcool secondaire~Deux carbones voisins~Cétone~Alcool tertiaire~Trois carbones voisins~Pas d'oxydation~Acide carboxylique~Groupement COOH~Ion carboxylate~Ester~Odeur fruitée~Arôme",
  "Classer l'alcool selon son carbone hydroxyle|Prévoir le produit d'oxydation|Écrire l'équation d'estérification|Choisir les conditions de déplacement de l'équilibre|Identifi er le produit par son odeur ou son point d'ébullition",
  "Oublier que l'estérification est réversible|Confondre saponification et estérification|Croire qu'un alcool tertiaire donne une cétone|Manipuler l'acide sulfurique sans gants|Chauffer un mélange inflammable à flamme nue",
  "CH₃CH₂OH~Éthanol primaire~CH₃CHO~Éthanal~CH₃COOH~Acide éthanoïque~CH₃COOC₂H₅~Éthanoate d'éthyle~H₂SO₄ concentré~Catalyseur",
  "Oxydation~Primaire en acide~Estérification~Acide + alcool",
  "Saponification~Hydrolyse basique~Estérification~Formation acide"))

# ============================================================ BI1
add("BI1", "Protéines et acides aminés", "Biochimie", ["1re"],
S("Les protéines sont des polymères d'acides aminés reliés par des liaisons peptidiques."
  "|Un acide aminé possède un groupement amine −NH₂, un groupement carboxyle −COOH et un radical R propre à chaque acide aminé."
  "|Vingt acides aminés naturels sont utilisés dans la synthèse des protéines."
  "|La liaison peptidique résulte de la condensation entre le carboxyle d'un acide aminé et l'amine d'un autre, avec élimination d'eau."
  "|Le enchaînement des acides aminés constitue la structure primaire de la protéine."
  "|La structure secondaire correspond aux hélices alpha et aux feuillets bêta, stabilisées par des liaisons hydrogène."
  "|La structure tertiaire est le repliement tridimensionnel de la chaîne, stabilisé par des interactions variées."
  "|Certaines protéines possèdent une structure quaternaire, assemblage de plusieurs sous-unités."
  "|Une dénaturation modifie la structure sans rompre les liaisons peptidiques et entraîne une perte d'activité biologique."
  "|Les enzymes sont des protéines qui catalysent les réactions du métabolisme."
  "|L'hémoglobine, le collagène et les anticorps sont des exemples de protéines aux fonctions très différentes."
  "|La réaction du biuret, qui vire au violet en présence de protéines, permet de les mettre en évidence au laboratoire."),
[QC("Quel est le monomère des protéines ?", "Un glucide~Un acide aminé~Un lipide~Un nucléotide", 1,
     "Les protéines sont des polymères d'acides aminés."),
 QC("Combien d'acides aminés naturels composent les protéines ?", "4~10~20~100", 2,
     "Vingt acides aminés sont couramment utilisés dans la synthèse protéique."),
 QC("Quelle liaison relie les acides aminés ?", "Hydrogène~Peptidique~Ionique~Ester", 1,
     "La liaison peptidique est une liaison amide entre carboxyle et amine."),
 QC("Que représente la structure primaire d'une protéine ?", "Son repliement global~La suite des acides aminés~Ses hélices~Ses sous-unités", 1,
     "La structure primaire est la séquence en acides aminés."),
 QC("Quel type de liaison stabilise les hélices alpha ?", "Peptidique~Hydrogène~Covalente~Disulfure uniquement", 1,
     "Les liaisons hydrogène entre groupements de la chaîne stabilisent les structures secondaires."),
 QC("Qu'est-ce qu'une dénaturation ?", "Une rupture des liaisons peptidiques~Une modification du repliement~Une synthèse d'acides aminés~Une hydrolyse totale", 1,
     "La dénaturation altère la structure spatiale sans casser la chaîne peptidique."),
 QC("Quel test met en évidence les protéines ?", "Le test à l'iode~La réaction du biuret~Le test de Benedict~La flame test", 1,
     "La réaction du biuret donne une coloration violette en présence de liaisons peptidiques."),
 QT("Distinguer la structure primaire et la structure tertiaire d'une protéine et expliquer pourquoi la dénaturation est souvent irréversible.",
    "La structure primaire est la séquence linéaire des acides aminés, maintenue par des liaisons peptidiques covalentes. La structure tertiaire est le repliement tridimensionnel de cette chaîne, stabilisé par des liaisons hydrogène, des interactions ioniques, des ponts disulfures et des interactions hydrophobes. Lors d'une dénaturation par la chaleur, un pH extrême ou un solvant, ces interactions faibles sont rompues et la protéine perd sa forme active, mais les liaisons peptidiques restent intactes. Le retour spontané à la conformation initiale est souvent impossible car de nombreuses interactions doivent se reformer de façon coordonnée : l'activité biologique est alors définitivement perdue, comme lors de la cuisson d'un oeuf.",
    "On oppose la séquence covalente au repliement, puis on explique la perte d'activité."),
 QT("Expliquer le rôle de la cuisinière et du dosage du biuret dans l'identification d'un échantillon protéique.",
    "La réaction du biuret repose sur la formation d'un complexe violet entre les ions cuivre et les liaisons peptidiques en milieu alcalin : plus il y a de liaisons peptidiques, plus la coloration est intense. On réalise un étalonnage avec une solution de protéine de concentration connue, puis on compare l'absorbance ou l'intensité de couleur de l'échantillon à la gamme. La cuisinière, chauffage doux, sert à repérer les protéines qui précipitent ou se dénaturent, mais elle ne donne qu'une information qualitative. Le dosage du biuret, lui, fournit une concentration. Les deux méthodes sont complémentaires : l'une révèle la présence, l'autre la quantité.",
    "On explique le principe colorimétrique du biuret, l'intérêt d'un étalonnage et la différence avec un test qualitatif.")],
C("Une protéine est une chaîne d'acides aminés dont le repliement tridimensionnel détermine la fonction.",
  "acides aminés − H₂O → liaison peptidique",
  "structure primaire, secondaire, tertiaire, quaternaire · dénaturation · biuret",
  "Acide aminé~NH₂ et COOH~Monomère~Liaison peptidique~Condensation~Perte d'eau~Primaire~Séquence~Ordre des acides aminés~Secondaire~Hélices et feuillets~Liaisons hydrogène~Tertiaire~Repliement 3D~Fonction~Biuret~Coloration violette~Dosage",
  "Identifier les groupements de l'acide aminé|Repérer la liaison peptidique|Déterminer le niveau de structure|Observer l'effet d'une dénaturation|Réaliser le test ou le dosage du biuret",
  "Confondre structure primaire et secondaire|Croire que la dénaturation rompt les liaisons peptidiques|Oublier l'élimination d'eau dans la condensation|Prendre le test à l'iode pour un test protéique|Ignorer le pH du réactif de biuret",
  "20 acides aminés~Vingt monomères~Biuret~Complexe violet~Hélice alpha~Liaisons H~Dénaturation~Perte d'activité~Hémoglobine~Transport O₂~Collagène~Soutien",
  "Structure primaire~Séquence~Structure tertiaire~Repliement",
  "Dénaturation~Perte de forme~Hydrolyse~Rupture de liaisons peptidiques"))

# ============================================================ BI2
add("BI2", "Glucides et lipides : structures et fonctions", "Biochimie", ["1re"],
S("Les glucides sont des composés organiques formés de carbones, d'hydrogène et d'oxygène, souvent de formule (CH₂O)n."
  "|Les monosaccharides, comme le glucose et le fructose, sont des sucres simples qui ne peuvent pas être hydrolysés."
  "|Le glucose est un aldose à six carbones ; sa forme cyclique peut être alpha ou bêta en solution."
  "|Les disaccharides résultent de la condensation de deux monosaccharides avec élimination d'eau."
  "|Le saccharose associe glucose et fructose, le lactose glucose et galactose, le maltose deux glucoses."
  "|Les polysaccharides sont des polymères de monosaccharides : amidon, glycogène et cellulose."
  "|L'amidon et le glycogène servent de réserve énergétique, tandis que la cellulose est un constituant structural des parois végétales."
  "|Les lipides sont des molécules hydrophobes comprenant les triglycérides, les phospholipides et les stéroïdes."
  "|Un triglycéride résulte de l'estérification d'un glycérol par trois acides gras."
  "|Les acides gras saturés n'ont pas de double liaison, les insaturés en possèdent une ou plusieurs."
  "|Les phospholipides possèdent une tête polaire et deux queues hydrophobes, ce qui leur permet de former des bicouches membranaires."
  "|Les tests à l'iode pour l'amidon et de Benedict pour les sucres réducteurs sont courants en travaux pratiques."),
[QC("Quelle est la formule générale des glucides ?", "(CH₂O)n~CₙH₂ₙ~C₆H₁₂O₆ seulement~NH₂COOH", 0,
     "Les glucides répondent le plus souvent à la formule (CH₂O)n."),
 QC("Quel sucre est un disaccharide ?", "Le glucose~Le fructose~Le saccharose~L'amidon", 2,
     "Le saccharose est formé d'un glucose et d'un fructose."),
 QC("Que met en évidence le test à l'iode ?", "Les protéines~L'amidon~Les lipides~Le glucose", 1,
     "L'iode forme un complexe bleu-noir avec l'amidon."),
 QC("Quel est le monomère de la cellulose ?", "Le fructose~Le glucose~Le galactose~Un acide aminé", 1,
     "La cellulose est un polymère de glucoses liés en bêta-1,4."),
 QC("Comment appelle-t-on un acide gras sans double liaison ?", "Insaturé~Saturé~Polyinsaturé~Aromatique", 1,
     "Un acide gras saturé ne contient aucune double liaison carbone-carbone."),
 QC("Que forme un triglycéride ?", "Glycérol + trois acides gras~Glucose + fructose~Acide aminé + acide aminé~Nucléotide + phosphate", 0,
     "C'est un triester de glycérol et d'acides gras."),
 QC("Pourquoi les phospholipides forment-ils des bicouches ?", "Ils sont entièrement hydrophiles~Ils ont une tête polaire et des queues hydrophobes~Ils sont solides~Ils contiennent du fer", 1,
     "Leur amphiphilie explique la formation spontanée de bicouches en milieu aqueux."),
 QT("Comparer l'amidon et la cellulose, tous deux polymères du glucose.",
    "L'amidon et la cellulose sont tous deux des polysaccharides formés de motifs glucose, mais leurs liaisons diffèrent. L'amidon utilise des liaisons alpha-1,4 et alpha-1,6, ce qui donne une structure hélicoïdale ou ramifiée, facilement hydrolysable par nos enzymes : c'est une réserve énergétique. La cellulose utilise des liaisons bêta-1,4, qui produisent des chaînes linéaires associées en fibres rigides. L'homme ne possède pas de cellulase et ne peut donc pas digérer la cellulose, qui joue un rôle de fibre alimentaire. Le test à l'iode colore l'amidon en bleu-noir mais ne colore pas la cellulose.",
    "On compare le type de liaison, la structure, la fonction et la digestibilité."),
 QT("Expliquer pourquoi un régime riche en acides gras saturés est déconseillé et relier cela à la structure des lipides.",
    "Les acides gras saturés possèdent des chaînes droites sans double liaison, ce qui leur permet de s'empiler étroitement : leurs points de fusion sont élevés et ils sont souvent solides à température ambiante. Un apport excessif, associé à d'autres facteurs, favorise l'élévation du cholestérol LDL et le dépôt de plaques d'athérome sur les parois artérielles, augmentant le risque cardiovasculaire. Les acides gras insaturés, dont les doubles liaisons courbent la chaîne, s'empilent moins bien et sont généralement liquides : ils ont un effet plus favorable lorsqu'ils remplacent les saturés dans l'alimentation.",
    "On relie l'absence de doubles liaisons à l'empilement et aux effets physiologiques.")],
C("Glucides et lipides diffèrent par leur structure et leur rôle : réserve énergétique pour les uns, membrane et stockage pour les autres.",
  "monosaccharide + monosaccharide → disaccharide + H₂O",
  "alpha-1,4 amidon · bêta-1,4 cellulose · triglycéride = glycérol + 3 acides gras",
  "Monosaccharide~Sucre simple~Glucose~Disaccharide~Deux sucres~Saccharose~Polysaccharide~Polymère~Amidon et cellulose~Triglycéride~Reserve lipidique~Trois acides gras~Phospholipide~Tete polaire~Queues hydrophobes~Iode~Amidon bleu noir",
  "Classer le glucide ou le lipide étudié|Repérer les motifs de base|Identifier le type de liaison|Réaliser le test coloré adapté|Relier structure et fonction biologique",
  "Confondre amidon et cellulose|Oublier l'élimination d'eau lors de la condensation|Appliquer le test de Benedict à un lipide|Croire que tous les acides gras sont liquides|Ignorer le rôle des phospholipides",
  "Glucose + fructose~Saccharose~Glucose + glucose~Maltose~(CH₂O)n~Glucide~Iode~Amidon bleu-noir~Benedict~Sucre réducteur~3 acides gras~Triglycéride",
  "Amidon~Liaison alpha~Cellulose~Liaison bêta",
  "Saturé~Pas de double liaison~Insaturé~Double liaison"))

# ============================================================ BI3
add("BI3", "Enzymes et cinétique enzymatique", "Biochimie", ["Terminale"],
S("Une enzyme est une protéine qui catalyse une réaction biochimique en abaissant son énergie d'activation."
  "|Le substrat est la molécule sur laquelle agit l'enzyme ; le produit est la molécule formée."
  "|La spécificité enzymatique s'explique par la complémentarité de forme et de charge entre le site actif et le substrat."
  "|Le modèle clé-serrure illustre cette spécificité ; le modèle d'ajustement induit décrit une modification du site actif lors de la fixation."
  "|Le complexe enzyme-substrat se forme avant la transformation du substrat en produit."
  "|La vitesse enzymatique augmente avec la concentration en substrat jusqu'à une valeur maximale Vmax."
  "|À Vmax, tous les sites actifs sont saturés : l'enzyme travaille à pleine capacité."
  "|La constante de Michaelis KM correspond à la concentration de substrat pour laquelle la vitesse vaut Vmax/2."
  "|Un KM faible indique une forte affinité de l'enzyme pour son substrat."
  "|La température et le pH influencent l'activité enzymatique : chaque enzyme possède un optimum."
  "|Une température trop élevée dénature l'enzyme et supprime son activité."
  "|Les inhibiteurs compétitifs se fixent sur le site actif et augmentent le KM apparent sans changer la Vmax."),
[QC("Qu'est-ce qu'une enzyme ?", "Un glucide catalyseur~Une protéine catalyseuse~Un lipide de réserve~Un ion métallique", 1,
     "Les enzymes sont des protéines qui accélèrent les réactions sans être consommées."),
 QC("Que désigne le site actif ?", "La partie centrale de la cellule~La région de l'enzyme qui fixe le substrat~Le noyau~Une membrane", 1,
     "Le site actif est la poche complémentaire du substrat."),
 QC("Que se passe-t-il à la saturation de l'enzyme ?", "La vitesse devient nulle~La vitesse atteint Vmax~La vitesse diminue~Le substrat disparaît", 1,
     "Tous les sites sont occupés : la vitesse plafonne à Vmax."),
 QC("Que représente KM ?", "La concentration pour une vitesse Vmax/2~La concentration maximale~La masse de l'enzyme~Le pH optimal", 0,
     "KM est la concentration de substrat donnant la moitié de la vitesse maximale."),
 QC("Un KM faible signifie…", "Une faible affinité~Une forte affinité~Une enzyme dénaturée~Une Vmax élevée", 1,
     "Moins il faut de substrat pour atteindre Vmax/2, plus l'affinité est grande."),
 QC("Quel effet a une température trop élevée sur une enzyme ?", "Elle active l'enzyme~Elle la dénature~Elle augmente sa synthèse~Elle la rend plus spécifique", 1,
     "La chaleur rompt les interactions maintenant le repliement de la protéine."),
 QC("Quel est l'effet d'un inhibiteur compétitif ?", "Il diminue Vmax et augmente KM~Il augmente le KM apparent sans changer Vmax~Il détruit l'enzyme~Il n'a aucun effet", 1,
     "En compétition avec le substrat, il peut être surmonté par un excès de substrat."),
 QT("Expliquer pourquoi la courbe vitesse-concentration en substrat présente un plateau.",
    "À faible concentration de substrat, de nombreux sites actifs sont libres : augmenter la concentration accroît la fréquence des collisions et donc la vitesse. Lorsque la concentration devient élevée, presque toutes les enzymes sont sous forme de complexe enzyme-substrat : il n'y a plus de sites libres disponibles. La vitesse plafonne alors à Vmax, qui correspond au nombre maximal de transformations par unité de temps pour la quantité d'enzyme présente. Augmenter encore la concentration de substrat ne peut plus rien changer ; seule une augmentation de la concentration d'enzyme ferait augmenter Vmax.",
    "On relie le plateau à la saturation des sites actifs et à la notion de Vmax."),
 QT("Décrire une expérience permettant de déterminer l'activité d'une enzyme en fonction du pH.",
    "On prépare une série de tampons couvrant par exemple pH 4 à pH 9, puis on introduit dans chaque tube la même quantité d'enzyme et de substrat. On incub e à température constante, par exemple 37 °C, et on mesure la quantité de produit formé après un temps fixe, par spectrophotométrie ou par un test coloré. On trace ensuite la vitesse initiale en fonction du pH. La courbe passe par un maximum qui correspond au pH optimal de l'enzyme ; de part et d'autre, la diminution d'activité traduit des modifications de charge des groupements du site actif ou une dénaturation aux pH extrêmes. On répète chaque mesure trois fois pour estimer l'incertitude.",
    "On décrit les variables contrôlées, la gamme de pH, la mesure de vitesse et l'interprétation de l'optimum.")],
C("Une enzyme est un catalyseur protéique spécifique, saturable et sensible au pH comme à la température.",
  "v = Vmax·[S]/(KM + [S])",
  "site actif · complexe ES · Vmax · KM · inhibition compétitive",
  "Enzyme~Catalyseur proteique~Abaisse Ea~Substrat~Molecule transformee~Site actif~Complementaire~Specificite~Complexe ES~Etape intermediaire~Vmax~Vitesse maximale~Saturation~KM~Affinite~Demi-Vmax~Inhibiteur~Competitif~Site actif occupe",
  "Choisir le substrat et la méthode de dosage|Préparer une gamme de concentrations|Mesurer la vitesse initiale|Tracer la courbe et lire Vmax et KM|Vérifier l'effet du pH et de la température",
  "Confondre Vmax et KM|Mesurer une vitesse après épuisement du substrat|Oublier de fixer la température|Croire qu'un inhibiteur compétitif diminue Vmax|Négliger les témoins sans enzyme",
  "Vmax~Tous sites occupes~KM~[S] pour Vmax/2~37 °C~Temperature courante~pH 7~Optimum de nombreuses enzymes~Competition~KM apparent plus grand",
  "Modèle clé-serrure~Spécificité rigide~Ajustement induit~Site actif flexible",
  "Inhibiteur compétitif~Sur le site actif~Inhibiteur non compétitif~Ailleurs sur l'enzyme"))

# ============================================================ BI4
add("BI4", "Hémoglobine et transport de l'oxygène", "Biochimie", ["Terminale"],
S("L'hémoglobine est une protéine des globules rouges qui assure le transport de l'oxygène des poumons vers les tissus."
  "|Elle est constituée de quatre sous-unités, chacune comportant une chaîne de globine et un groupement hème."
  "|Le groupement hème contient un ion ferreux Fe²⁺ au centre d'une porphyrine, capable de fixer une molécule d'oxygène."
  "|Une molécule d'hémoglobine peut donc transporter jusqu'à quatre molécules d'oxygène."
  "|La fixation de l'oxygène est coopérative : la première liaison facilite la fixation des suivantes."
  "|La courbe de dissociation de l'hémoglobine a une forme sigmoïde, traduisant cette coopérativité."
  "|Dans les poumons, la forte pression partielle en oxygène favorise la charge de l'hémoglobine."
  "|Dans les tissus, la plus faible pression partielle et l'acidité favorisent la libération d'oxygène : c'est l'effet Bohr."
  "|Lors d'un effort, la production de CO₂ et d'acide lactique diminue le pH sanguin et facilite le relargage d'oxygène."
  "|Le monoxyde de carbone se fixe sur l'hème avec une affinité bien supérieure à celle de l'oxygène."
  "|Une intoxication au monoxyde de carbone réduit la capacité du sang à transporter l'oxygène."
  "|L'hémoglobine glyquée, dosée chez les patients diabétiques, reflète la glycémie moyenne sur plusieurs semaines."),
[QC("Combien de molécules d'oxygène peut transporter une hémoglobine ?", "Une~Deux~Trois~Quatre", 3,
     "Quatre sous-unités, chacune avec un hème, fixes chacune un O₂."),
 QC("Quel ion se trouve au centre du groupement hème ?", "Fe²⁺~Ca²⁺~Na⁺~Mg²⁺", 0,
     "Le fer ferreux Fe²⁺ est le site de fixation de l'oxygène."),
 QC("Quelle est la forme de la courbe de dissociation de l'hémoglobine ?", "Linéaire~Sigmoïde~Horizontale~Exponentielle décroissante", 1,
     "La coopérativité donne une courbe en S."),
 QC("Quel phénomène décrit l'effet Bohr ?", "La fixation du CO₂ sur l'hème~La libération d'O₂ facilitée par un pH plus acide~La synthèse de globine~La destruction des globules rouges", 1,
     "L'acidité diminue l'affinité de l'hémoglobine pour l'oxygène."),
 QC("Où l'hémoglobine se charge-t-elle principalement en oxygène ?", "Dans les tissus~Dans les poumons~Dans le foie~Dans le rein", 1,
     "La pression partielle d'oxygène y est maximale."),
 QC("Pourquoi le monoxyde de carbone est-il dangereux ?", "Il détruit les globules rouges~Il se fixe sur l'hème à la place de l'oxygène~Il abaisse le pH~Il augmente la glycémie", 1,
     "Son affinité pour le fer de l'hème est très supérieure à celle de l'O₂."),
 QC("Que reflète le dosage de l'hémoglobine glyquée ?", "La glycémie moyenne sur plusieurs semaines~La pression artérielle~Le taux d'oxygène~Le nombre de globules blancs", 0,
     "L'HbA1c indique la glycémie moyenne des deux à trois derniers mois."),
 QT("Expliquer le lien entre coopérativité et forme sigmoïde de la courbe de dissociation.",
    "L'hémoglobine possède quatre sites de fixation. Lorsque le premier oxygène se lie, il provoque un changement de conformation de la protéine qui augmente l'affinité des sites restants : la fixation est coopérative. Il en résulte que la saturation augmente d'abord lentement, puis rapidement dans une zone de pressions partielles intermédiaires, avant de plafonner : la courbe a donc une allure sigmoïde. Cette propriété est physiologiquement utile : l'hémoglobine se charge presque complètement dans les poumons, où la pression d'oxygène est élevée, et libère facilement son oxygène dans les tissus, où la pression est plus basse.",
    "On relie le changement de conformation des sous-unités à la pente et aux zones de la courbe."),
 QT("Un patient est exposé à une atmosphère contenant du monoxyde de carbone. Expliquer les conséquences et la conduite à tenir.",
    "Le monoxyde de carbone se fixe sur le fer des groupements hèmes avec une affinité bien plus grande que l'oxygène, formant la carboxyhémoglobine. Les sites ne peuvent plus transporter d'O₂ et la courbe de dissociation est déplacée : l'oxygène restant est libéré plus difficilement dans les tissus. Il en résulte une hypoxie, avec maux de tête, vertiges et, à forte dose, perte de connaissance et décès. La conduite d'urgence consiste à aérer immédiatement la pièce, à éloigner la personne de la source, à appeler les secours et à administrer de l'oxygène pur ; en milieu hospitalier, un traitement par oxygène hyperbare peut accélérer l'élimination du CO.",
    "On explique la compétition pour l'hème, l'hypoxie et les gestes d'urgence.")],
C("L'hémoglobine est un transporteur coopératif : elle charge l'O₂ dans les poumons et le libère dans les tissus acides.",
  "Hb + 4 O₂ ⇌ Hb(O₂)₄",
  "hème Fe²⁺ · coopérativité · courbe sigmoïde · effet Bohr · CO compétitif",
  "Hemoglobine~Transport O₂~Quatre sous-unites~Hème~Fer Fe²⁺~Fixation O₂~Cooperativite~Affinite croissante~Courbe sigmoide~Charge puis plateau~Effet Bohr~pH acide relargage~Monoxyde de carbone~Affinite superieure~Hypoxie",
  "Repérer les sous-unités et les hèmes|Expliquer la coopérativité|Lire la courbe de dissociation|Relier pH et libération d'O₂|Identifier le risque lié au CO",
  "Confondre fer ferreux et ferrique|Croire que la courbe est linéaire|Oublier l'effet Bohr|Ignorer l'affinité du CO|Confondre hémoglobine et myoglobine",
  "4 sites O₂~Quatre hèmes~Fe²⁺~Liaison reversible~pH 7,4~Sang arteriel~pH 7,2~Tissus actifs~CO~Carboxyhemoglobine~HbA1c~Glycemie moyenne",
  "Poumons~Charge en O₂~Tissus~Liberation d'O₂",
  "Coopérativité~Courbe sigmoïde~Fixation indépendante~Courbe hyperbolique"))

# ============================================================ MB1
add("MB1", "Bactéries : structure, croissance et nutrition", "Microbiologie", ["1re"],
S("Les bactéries sont des organismes unicellulaires procaryotes, dépourvus de noyau et d'organites membranaires."
  "|Leur taille se mesure en micromètres, généralement de 1 à 5 µm."
  "|La paroi bactérienne, faite de peptidoglycane, assure la rigidité et protège contre la pression osmotique."
  "|On distingue les bactéries à Gram positif, à paroi épaisse, et les bactéries à Gram négatif, à paroi fine et membrane externe."
  "|Certaines bactéries possèdent une capsule, des flagelles pour le déplacement ou des pili pour l'adhérence."
  "|Le matériel génétique bactérien est un chromosome circulaire unique, parfois complété par des plasmides."
  "|Les bactéries se multiplient par scissiparité : une cellule mère donne deux cellules filles identiques."
  "|Dans des conditions favorables, la population double à chaque génération : c'est une croissance exponentielle."
  "|Le temps de génération est le temps nécessaire pour que la population double, par exemple vingt minutes pour Escherichia coli."
  "|La croissance passe par quatre phases : latence, exponentielle, stationnaire et déclin."
  "|Les besoins nutritionnels varient : les autotrophes synthétisent leurs composés, les hétérotrophes les puisent dans le milieu."
  "|La maîtrise de ces notions est indispensable pour choisir un milieu de culture et interpréter un isolement."),
[QC("Quel type de cellule est une bactérie ?", "Eucaryote~Procaryote~Multicellulaire~Sans membrane", 1,
     "Les bactéries n'ont pas de noyau : elles sont procaryotes."),
 QC("Quel constituant assure la rigidité de la paroi bactérienne ?", "La cellulose~Le peptidoglycane~La chitine~La kératine", 1,
     "Le peptidoglycane est spécifique des bactéries."),
 QC("Comment les bactéries se multiplient-elles ?", "Par méiose~Par scissiparité~Par bourgeonnement~Par sporulation sexuée", 1,
     "La scissiparité donne deux cellules filles génétiquement identiques."),
 QC("Quelle phase suit la phase de latence ?", "Le déclin~La phase stationnaire~La phase exponentielle~La mort", 2,
     "Après l'adaptation, la population entre en croissance exponentielle."),
 QC("Que signifie un temps de génération de 20 minutes ?", "La population meurt en 20 minutes~La population double en 20 minutes~La taille double~Le milieu est épuisé", 1,
     "Le temps de génération est le temps de doublement de la population."),
 QC("Que sont les plasmides ?", "Des organites respiratoires~Des petits ADN circulaires supplémentaires~Des flagelles~Des parois épaisses", 1,
     "Les plasmides sont des molécules d'ADN extra-chromosomiques."),
 QC("Quelle différence entre Gram positif et Gram négatif ?", "La couleur du milieu~L'épaisseur et la structure de la paroi~La taille du chromosome~La présence de flagelles", 1,
     "La coloration de Gram révèle des parois différentes."),
 QT("Décrire l'évolution d'une population bactérienne dans un milieu fermé et expliquer chaque phase.",
    "Après l'ensemencement, la phase de latence correspond à l'adaptation des cellules au milieu : elles synthétisent les enzymes nécessaires mais ne se divisent pas encore. La phase exponentielle suit : chaque cellule se divise à intervalles réguliers, la population double à chaque génération et la croissance est la plus rapide. La phase stationnaire s'installe lorsque les nutriments s'épuisent et que les déchets s'accumulent : le nombre de divisions égale le nombre de morts. Enfin, la phase de déclin voit les morts l'emporter. Courbe et phases dépendent de la température, du pH et de la composition du milieu.",
    "On nomme les quatre phases et on relie chacune à une cause physiologique ou environnementale."),
 QT("Expliquer pourquoi une contamination même légère peut rapidement envahir une culture bactérienne.",
    "Une seule bactérie peut donner naissance à une population immense en quelques heures grâce à la croissance exponentielle. Si son temps de génération est de vingt minutes, il y a trois générations par heure : après six heures, une cellule peut théoriquement produire 2¹⁸, soit environ 260 000 cellules. Un contaminant introduit accidentellement dispose du même potentiel et peut dépasser la souche d'intérêt si ses conditions de croissance sont meilleures. C'est pourquoi la stérilité du matériel, le travail près d'une flamme et l'absence de manipulations superflues sont essentiels en microbiologie.",
    "On illustre la croissance exponentielle par un calcul simple et on en déduit les règles d'asepsie.")],
C("La bactérie est une cellule procaryote à paroi de peptidoglycane qui se multiplie par scissiparité selon une courbe en quatre phases.",
  "N = N₀ × 2ⁿ (n = nombre de générations)",
  "Gram +/- · scissiparité · temps de génération · latence, exponentielle, stationnaire, déclin",
  "Bactérie~Procaryote~Pas de noyau~Paroi~Peptidoglycane~Rigidité~Gram positif~Paroi épaisse~Gram negatif~Membrane externe~Scissiparite~Deux cellules filles~Temps de generation~Doublement~Croissance~Exponentielle",
  "Observer la forme et la coloration de Gram|Repérer les structures externes|Estimer le temps de génération|Relever la courbe de croissance|Relier les phases aux conditions du milieu",
  "Croire que les bactéries ont un noyau|Confondre les phases de croissance|Oublier le rôle des déchets métaboliques|Manipuler sans asepsie|Appliquer un temps de génération à toutes les espèces",
  "E. coli~20 minutes~3 générations par heure~2¹⁸~260 000 cellules~4 phases~Latence, exponentielle, stationnaire, declin~Peptidoglycane~Paroi bactérienne",
  "Gram positif~Paroi épaisse~Gram négatif~Paroi fine et membrane externe",
  "Autotrophe~Synthétise ses composés~Hétérotrophe~Puise dans le milieu"))

# ============================================================ MB2
add("MB2", "Milieux de culture et isolement des bactéries", "Microbiologie", ["1re"],
S("Un milieu de culture apporte aux micro-organismes l'eau, les nutriments et les facteurs de croissance nécessaires."
  "|Un milieu est composé d'une base nutritive, éventuellement gélifiée avec de l'agar-agar."
  "|L'agar se solidifie vers 40 °C et fond vers 85 °C, ce qui permet d'ensemencer à environ 45 °C."
  "|Les milieux ordinaires comme la gélose nutritive conviennent à de nombreuses bactéries non exigeantes."
  "|Les milieux sélectifs contiennent un agent qui inhibit certaines espèces et favorise d'autres."
  "|Les milieux différentiels permettent de distinguer les espèces grâce à une réaction colorée ou à un indicateur."
  "|Le sang ou le sérum ajouté apporte des facteurs de croissance aux bactéries exigeantes."
  "|La stérilisation à l'autoclave, vers 121 °C pendant 15 minutes, détruit toutes les formes vegetatives et les spores."
  "|L'ensemencement doit se faire en conditions d'asepsie, près d'une flamme, avec du matériel stérile."
  "|La technique de la striation permet d'isoler des colonies à partir d'un prélèvement mélangé."
  "|Une colonie isolée provient en principe d'une seule cellule ou d'un petit groupe de cellules identiques."
  "|Les boîtes sont incubées à une température adaptée, souvent 30 ou 37 °C, et observées après 18 à 48 heures."),
[QC("Quel agent gélifie la plupart des milieux de culture ?", "La gélatine~L'agar-agar~L'amidon~La cellulose", 1,
     "L'agar-agar solidifie le milieu et reste solide à la température d'incubation."),
 QC("À quelle température stérilise-t-on un milieu à l'autoclave ?", "60 °C~80 °C~121 °C~200 °C", 2,
     "Le cycle standard est de 121 °C pendant environ 15 minutes."),
 QC("Quel est l'intérêt d'un milieu sélectif ?", "Favoriser certaines espèces~Colorer toutes les colonies~Nourrir les champignons~Remplacer l'incubation", 0,
     "Il contient un agent qui inhibe une partie de la flore et sélectionne un groupe."),
 QC("Que permet la technique de la striation ?", "De compter les cellules~D'obtenir des colonies isolees~De stériliser le milieu~De mesurer le pH", 1,
     "Les streaks successifs diluent l'inoculum jusqu'à obtenir des colonies séparées."),
 QC("Pourquoi ensemencer près d'une flamme ?", "Pour réchauffer le milieu~Pour limiter les contaminations~Pour accélérer la croissance~Pour stériliser la boîte", 1,
     "La flamme crée un courant d'air ascendant protégeant la zone de travail."),
 QC("À quelle température ensemence-t-on une gélose encore liquide ?", "20 °C~45 °C~85 °C~121 °C", 1,
     "Vers 45 °C, l'agar est encore liquide sans brûler les cellules."),
 QC("D'où provient une colonie isolée ?", "De plusieurs espèces~D'une cellule ou d'un petit groupe identique~Du milieu seul~D'une spore de champignon", 1,
     "Une colonie est issue d'une unité formative de colonie."),
 QT("Décrire les étapes de la préparation d'une gélose et de son ensemencement en conditions d'asepsie.",
    "On prépare la poudre de milieu dans l'eau distillée, on ajuste le pH si nécessaire, puis on autoclave à 121 °C pendant 15 minutes. On laisse refroidir vers 45 °C, température à laquelle l'agar reste liquide, puis on coule le milieu dans des boîtes stériles en évitant les bulles. Après solidification, on dessèche légèrement la surface, on étiquette le fond des boîtes et on ensemence par striation à l'anse stérile, près d'une flamme. On referme immédiatement, on incub e à la température adaptée et on observe les colonies après 18 à 48 heures, sans ouvrir les boîtes.",
    "On suit l'ordre : préparation, stérilisation, coulée, ensemencement aseptique, incubation."),
 QT("Expliquer la différence entre un milieu sélectif et un milieu différentiel, et donner un exemple de chaque.",
    "Un milieu sélectif contient un agent qui inhibe la croissance d'une partie des micro-organismes pour favoriser un groupe cible : par exemple, un milieu additionné d'antibiotique sélectionnera des levures résistantes en inhibant les bactéries. Un milieu différentiel ne bloque pas forcément la croissance, mais permet de distinguer les espèces par un signe visible : le milieu EMB colore les colonies d'E. coli en vert métallique grâce au métabolisme du lactose. Un même milieu peut être à la fois sélectif et différentiel. Le choix repose sur l'objectif de l'analyse :isolement d'un groupe ou identification rapide d'une espèce.",
    "On sépare sélection et différenciation, puis on donne un exemple pour chacune.")],
C("Un bon isolement repose sur un milieu adapté, une stérilisation efficace et une manipulation rigoureusement aseptique.",
  "agar : solide à 40 °C, liquide à 85 °C · autoclave 121 °C / 15 min",
  "milieu ordinaire, sélectif ou différentiel · striation · colonie isolée",
  "Milieu~Nutriments et eau~Base de culture~Agar~Gélifiant~Solide à 40 °C~Autoclave~121 °C, 15 min~Stérilisation~Destruction des germes~Milieu selectif~Inhibe un groupe~Milieu differentiel~Coloration distinctive~Striation~Isolement des colonies~Asepsie~Pres d'une flamme",
  "Préparer et stériliser le milieu|Laisser tiédir vers 45 °C et couler|Étiqueter le fond de la boîte|Ensemencer par striation près d'une flamme|Incuber et observer sans ouvrir",
  "Ouvrir une boîte incubée|Ensemencer un milieu trop chaud|Oublier d'étiqueter|Utiliser une anse non stérile|Confondre milieu sélectif et différentiel",
  "121 °C~15 minutes~45 °C~Coulee de l'agar~30 ou 37 °C~Incubation~18 à 48 h~Observation~Agar~Gélifiant~Colonie isolee~Une UFC",
  "Milieu sélectif~Inhibe~Milieu différentiel~Distingue par la couleur",
  "Asepsie~Évite la contamination~Contamination~Germes indésirables"))

# ============================================================ MB3
add("MB3", "Dénombrement et numération des micro-organismes", "Microbiologie", ["Terminale"],
S("La numération permet d'estimer le nombre de micro-organismes présents dans un échantillon."
  "|La numération sur milieu solide consiste à ensemencer une dilution connue puis à compter les colonies apparues."
  "|On exprime le résultat en unités formant colonie par millilitre, noté UFC/mL."
  "|Une colonie peut provenir de plusieurs cellules groupées : le résultat est donc une estimation par excès ou par défaut selon l'agrégation."
  "|La technique des dilutions en cascade réduit la concentration jusqu'à obtenir un nombre dénombrable de colonies."
  "|On retient généralement les boîtes presentant entre 30 et 300 colonies pour une estimation fiable."
  "|Le facteur de dilution est le produit des dilutions successives, par exemple 10⁻⁵ après cinq paliers de 1/10."
  "|La concentration de l'échantillon initial vaut nombre de colonies divisé par le volume ensemencé et par le facteur de dilution."
  "|La numération en cellule de Malassez compte directement les cellules au microscope dans un volume connu."
  "|Cette méthode rapide ne distingue pas les cellules vivantes des cellules mortes."
  "|La turbidimétrie estime la concentration par la mesure de l'absorbance d'une suspension."
  "|Le choix de la méthode dépend du besoin : viabilité, rapidité ou précision."),
[QC("Quelle unité exprime une numération sur milieu solide ?", "mg/L~UFC/mL~mol/L~µm", 1,
     "On compte des unités formant colonie par millilitre."),
 QC("Combien de colonies faut-il de préférence compter sur une boîte ?", "Moins de 5~Entre 30 et 300~Plus de 1000~Exactement 1", 1,
     "La plage 30-300 donne une précision statistique acceptable."),
 QC("Après cinq dilutions au 1/10, quel est le facteur de dilution ?", "10⁻²~10⁻³~10⁻⁵~10¹⁰", 2,
     "Chaque palier divise par 10 : cinq paliers donnent 10⁻⁵."),
 QC("Comment calculer la concentration initiale ?", "Colonies × volume × dilution~Colonies / (volume × dilution)~Colonies + dilution~Volume / colonies", 1,
     "C = N/(V × d), avec d le facteur de dilution."),
 QC("Quel est un avantage de la cellule de Malassez ?", "Elle compte uniquement les cellules vivantes~Elle est rapide et directe~Elle évite toute dilution~Elle donne des colonies", 1,
     "Le comptage au microscope est immédiat mais ne distingue pas vivants et morts."),
 QC("Que mesure la turbidimétrie ?", "Le pH~L'absorbance d'une suspension~La température~Le nombre de colonies", 1,
     "La densité optique est liée à la concentration cellulaire."),
 QC("Pourquoi une colonie peut-elle correspondre à plusieurs cellules ?", "Parce que les cellules peuvent être groupées~Parce que l'agar est épais~Parce que l'incubation est courte~Ce n'est jamais le cas", 0,
     "Une UFC peut être un amas de cellules qui ne forment qu'une colonie."),
 QT("Une boîte ensemencée avec 0,1 mL d'une dilution 10⁻⁴ donne 150 colonies. Calculer la concentration de l'échantillon initial.",
    "La concentration de la dilution ensemencée vaut 150/0,1 = 1500 UFC/mL. Pour remonter à l'échantillon initial, on divise par le facteur de dilution 10⁻⁴, soit 1500/10⁻⁴ = 1,5 × 10⁷ UFC/mL. On peut écrire directement C = N/(V·d) = 150/(0,1 × 10⁻⁴) = 150/10⁻⁵ = 1,5 × 10⁷ UFC/mL. Ce résultat est fiable car 150 colonies se situent dans la plage recommandée de 30 à 300.",
    "On calcule la concentration de la dilution puis on corrige par le facteur de dilution."),
 QT("Comparer la numération sur milieu solide, la cellule de Malassez et la turbidimétrie en indiquant leurs limites.",
    "La numération sur milieu solide ne comptabilise que les cellules capables de se multiplier : elle mesure une viabilité, mais nécessite 18 à 48 heures d'incubation et sous-estime les cellules agrégées. La cellule de Malassez donne un résultat immédiat et peu coûteux, mais elle compte vivantes et mortes et demande une suspension suffisamment dense. La turbidimétrie est très rapide et adaptée au suivi d'une croissance en temps réel, mais elle nécessite un étalonnage pour chaque espèce et ne peut pas distinguer les cellules mortes, qui diffusent aussi la lumière. En pratique, on combine souvent turbidimétrie pour le suivi et numération sur gélose pour la valeur finale en UFC/mL.",
    "On compare viabilité, rapidité, précision et limites des trois méthodes.")],
C("La numération quantifie une populationmicrobienne ; le choix de la méthode dépend de ce que l'on veut mesurer.",
  "C (UFC/mL) = N / (V ensemencé × facteur de dilution)",
  "dilutions en cascade · 30-300 colonies · UFC · Malassez · turbidimétrie",
  "Numeration~Estimer une population~UFC/mL~Unite formant colonie~Un ou plusieurs cellules~Dilution~Cascade de facteurs 10~Boîte~30 à 300 colonies~Plage fiable~Malassez~Comptage au microscope~Cellules vivantes et mortes~Turbidimetrie~Absorbance~Suivi rapide",
  "Choisir la méthode selon l'objectif|Réaliser les dilutions en cascade|Ensemencer un volume connu|Compter les colonies dénombrables|Calculer la concentration initiale",
  "Oublier le volume ensemencé dans le calcul|Se tromper de facteur de dilution|Compter une boîte trop dense|Croire que la cellule de Malassez compte les vivants|Omettre les unités",
  "150 colonies~0,1 mL~Dilution 10⁻⁴~C = 1,5 × 10⁷ UFC/mL~30 à 300~Plage valide~10⁻⁵~Cinq paliers~Densite optique~Turbidimetrie",
  "Milieu solide~Cellules viables~Malassez~Toutes les cellules",
  "Turbidimétrie~Rapidité~Numération~Viabilité"))

# ============================================================ MB4
add("MB4", "Antibiogramme et résistance bactérienne", "Microbiologie", ["Terminale"],
S("Un antibiotique est une substance qui inhibe la croissance bactérienne ou provoque la mort des bactéries."
  "|Un antibiotique bactéricide tue les bactéries, tandis qu'un bactériostatique bloque leur multiplication."
  "|L'antibiogramme permet de tester la sensibilité d'une souche à plusieurs antibiotiques."
  "|La méthode standard dépose des disques imprégnés d'antibiotique sur une gélose uniformément ensemencée."
  "|Après incubation, une zone d'inhibition apparaît autour des disques auxquels la souche est sensible."
  "|Le diamètre de la zone est mesuré et comparé à des valeurs critiques pour classer la souche en sensible, intermédiaire ou résistante."
  "|La concentration minimale inhibitrice, ou CMI, est la plus faible concentration d'antibiotique qui empêche la croissance visible."
  "|Une résistance peut être naturelle, propre à une espèce, ou acquise par mutation ou transfert de gènes."
  "|Les plasmides portant des gènes de résistance peuvent être transférés par conjugaison entre bactéries."
  "|La surconsommation d'antibiotiques exerce une pression de sélection qui favorise les souches résistantes."
  "|Certaines bactéries produisent des enzymes comme les bêta-lactamases qui détruisent l'antibiotique."
  "|Le résultat de l'antibiogramme guide le choix thérapeutique et doit être rendu sous forme d'un antibiogramme standardisé."),
[QC("Que mesure l'antibiogramme ?", "La taille des bactéries~La sensibilité d'une souche aux antibiotiques~Le pH du milieu~La vitesse de croissance", 1,
     "Il détermine le profil de sensibilité d'une souche à plusieurs molécules."),
 QC("Que signifie un antibiotique bactéricide ?", "Il bloque la division~Il tue les bactéries~Il nourrit les bactéries~Il change la couleur du milieu", 1,
     "Bactéricide signifie létal ; bactériostatique signifie seulement inhibition de la croissance."),
 QC("Quelle zone mesure-t-on autour d'un disque ?", "Une zone de croissance~Une zone d'inhibition~Une zone de coloration~Une zone de diffusion de l'agar", 1,
     "Le diamètre de la zone d'inhibition reflète la sensibilité."),
 QC("Que désigne la CMI ?", "Concentration maximale injectable~Concentration minimale inhibitrice~Concentration moyenne~Concentration de l'agar", 1,
     "La CMI est la plus petite concentration empêchant la croissance visible."),
 QC("Comment une résistance peut-elle être acquise ?", "Par mutation ou transfert de gènes~Par simple vieillissement~Par changement de couleur~Par incubation plus longue", 0,
     "Les mutations et les transferts horizontaux de plasmides sont les deux voies principales."),
 QC("Quel mécanisme explique la résistance aux bêta-lactamines ?", "Une paroi plus épaisse~La production de bêta-lactamase~Une membrane plus fine~Un pH acide", 1,
     "La bêta-lactamase hydrolyse le cycle bêta-lactame de la pénicilline."),
 QC("Pourquoi la surconsommation favorise-t-elle la résistance ?", "Elle tue tous les germes~Elle exerce une pression de sélection sur les souches~Elle rend l'antibiotique plus fort~Elle diminue les mutations", 1,
     "Les souches résistantes survivent et se multiplient en l'absence de compétiteurs sensibles."),
 QT("Interpréter un antibiogramme : une souche donne un diamètre de 22 mm pour un antibiotique dont les seuils sont sensible ≥ 20 mm et résistant ≤ 14 mm. Que conclure ?",
    "Le diamètre de 22 mm est supérieur au seuil de sensibilité de 20 mm : la souche est classée sensible à cet antibiotique. La zone d'inhibition montre que la croissance bactérienne est empêchée à cette distance du disque, ce qui signifie que la concentration diffusée reste supérieure à la CMI de la souche. Ce résultat permet d'envisager cet antibiotique pour le traitement, sous réserve de la concentration achievable in vivo et du site de l'infection. On rapporte le résultat en utilisant les catégories standardisées S, I ou R.",
    "On compare le diamètre mesuré aux seuils, puis on relie la zone d'inhibition à la CMI et à la décision thérapeutique."),
 QT("Expliquer comment une bactérie initialement sensible peut devenir résistante à un antibiotique en quelques générations.",
    "Dans une population bactérienne, des mutations aléatoires apparaissent spontanément ; certaines modifient la cible de l'antibiotique, la perméabilité de la membrane ou produisent une enzyme destructrice. En présence de l'antibiotique, les cellules sensibles meurent ou cessent de se multiplier, tandis que les rares mutants résistants survivent et occupent la place libre : c'est une sélection naturelle, et non l'antibiotique qui crée la mutation. La résistance peut aussi être acquise par conjugaison, via un plasmide transféré d'une autre bactérie. Une pression de sélection prolongée, par exemple un traitement trop court ou mal dosé, accélère la dissémination de ces souches.",
    "On distingue mutation aléatoire et sélection, puis on ajoute le transfert horizontal de plasmides.")],
C("L'antibiogramme teste la sensibilité d'une souche ; la résistance est une propriété génétique favorisée par la pression de sélection.",
  "CMI = plus faible concentration qui inhibe la croissance",
  "disque · zone d'inhibition · seuils S/I/R · bêta-lactamase · plasmide",
  "Antibiogramme~Test de sensibilite~Disque~Antibiotique depose~Zone d'inhibition~Croissance empêchee~CMI~Concentration minimale inhibitrice~Sensible~Diamètre superieur au seuil~Resistant~Diamètre inferieur au seuil~Beta-lactamase~Enzyme destructrice~Plasmide~Transfert de resistance",
  "Ensemencer une gélose de façon uniforme|Déposer les disques d'antibiotique|Incuber à température adaptée|Mesurer les diamètres d'inhibition|Comparer aux seuils et rendre le résultat S/I/R",
  "Oublier de standardiser l'inoculum|Mesurer le disque au lieu de la zone|Lire les seuils après une incubation trop courte|Croire que l'antibiotique induit la mutation|Ignorer les résultats intermédiaires",
  "22 mm~Seuil S à 20 mm~Souche sensible~14 mm~Seuil R~Souche résistante~CMI~Plus faible concentration active~S, I, R~Catégories standardisées",
  "Bactéricide~Tue~Bactériostatique~Inhibe la croissance",
  "Résistance naturelle~Propre à l'espèce~Résistance acquise~Mutation ou plasmide"))

# ============================================================ PA1
add("PA1", "Mesures, incertitudes et qualité des résultats", "Physique appliquée", ["1re"],
S("Toute mesure expérimentale est entachée d'une incertitude : elle ne donne qu'une estimation de la valeur vraie."
  "|L'erreur absolue est la différence entre la valeur mesurée et la valeur de référence, lorsqu'elle est connue."
  "|L'erreur relative rapporte l'erreur absolue à la valeur de référence et s'exprime souvent en pourcentage."
  "|Une erreur systématique est reproductible et déplace toutes les mesures dans le même sens."
  "|Une erreur aléatoire varie d'une mesure à l'autre et peut être réduite en répétant les essais."
  "|La justesse est la conformité d'une mesure à la valeur de référence ; la fidélité est la concordance entre mesures répétées."
  "|Une mesure peut être fidèle sans être juste, par exemple si un appareil est mal étalonné."
  "|La résolution d'un appareil est le plus petit écart qu'il peut détecter : elle fixe l'incertitude de lecture."
  "|Une balance analytique peut peser au centième de milligramme, tandis qu'une balance de cuisine affiche le gramme."
  "|Le résultat d'une mesure s'écrit avec une incertitude et une unité, par exemple m = 12,34 ± 0,02 g."
  "|Les chiffres significatifs traduisent la précision de la mesure : on ne doit pas en conserver trop après un calcul."
  "|La traçabilité, le calibrage et la tenue d'un cahier de laboratoire sont essentiels à la qualité des résultats."),
[QC("Que représente une incertitude de mesure ?", "La valeur exacte~L'intervalle dans lequel se situe la valeur vraie~Une erreur de calcul~Le prix de l'appareil", 1,
     "L'incertitude quantifie le doute sur la valeur mesurée."),
 QC("Comment réduit-on les erreurs aléatoires ?", "En répétant les mesures~En changeant d'unité~En arrondissant~En ajoutant une constante", 0,
     "La moyenne de plusieurs essais réduit la dispersion aléatoire."),
 QC("Qu'est-ce qu'une erreur systématique ?", "Une erreur qui change de sens~Une erreur reproductible dans un sens~Une faute de frappe~Une variabilité normale", 1,
     "Elle découle le plus souvent d'un défaut de calibrage ou d'une méthode biaisée."),
 QC("Quelle grandeur mesure la fidélité ?", "L'écart à la référence~La dispersion entre mesures répétées~La résolution~La température", 1,
     "La fidélité s'apprécie par l'écart-type des répétitions."),
 QC("Une mesure fidèle est-elle nécessairement juste ?", "Oui~Non~Seulement en chimie~Seulement si l'appareil est neuf", 1,
     "Un appareil mal étalonné donne des résultats reproductibles mais éloignés de la valeur vraie."),
 QC("Que fixe la résolution d'un appareil ?", "Sa couleur~Le plus petit écart détectable~Sa masse~Son prix", 1,
     "La résolution limite l'incertitude de lecture."),
 QC("Comment écrire correctement un résultat de mesure ?", "12,34 g~12,34 ± 0,02 g~12 g environ~12,340000 g", 1,
     "On donne la valeur, l'incertitude et l'unité, avec un nombre de chiffres cohérent."),
 QT("Expliquer la différence entre justesse et fidélité à l'aide d'un exemple de pesée.",
    "La justesse est la proximité entre la moyenne des mesures et la valeur de référence ; la fidélité est la proximité entre les mesures répétées entre elles. Si une balance est mal tarée de 0,5 g, trois pesées donnant 10,50, 10,51 et 10,49 g pour une masse vraie de 10,00 g sont très fidèles, car leur dispersion est faible, mais elles sont injustes, car leur moyenne est décalée. Après remise à zéro, les mesures deviennent justes et restent fidèles. Une mesure de qualité doit être à la juste et fidèle : l'étalonnage traite la justesse, la répétition et la maîtrise des conditions traitent la fidélité.",
    "On définit les deux notions et on illustre par un décalage de zéro sur une balance."),
 QT("Un étudiant mesure trois fois le même volume et obtient 24,8 ; 25,2 et 25,0 mL. Calculer la moyenne et l'écart maximal, puis proposer une écriture du résultat.",
    "La moyenne vaut (24,8 + 25,2 + 25,0)/3 = 75,0/3 = 25,0 mL. Les écarts à la moyenne sont 0,2 ; 0,2 et 0,0 mL, donc l'écart maximal est 0,2 mL. On peut écrire le résultat sous la forme V = 25,0 ± 0,2 mL, en précisant qu'il s'agit de la moyenne de trois essais. L'incertitude de lecture de l'éprouvette doit aussi être prise en compte : si elle vaut 0,1 mL, l'incertitude globale sera au moins de 0,2 mL et l'écriture reste cohérente. On conserve une décimale, comme la résolution de l'instrument.",
    "On calcule la moyenne et l'écart maximal, puis on donne une écriture avec unité et chiffres significatifs.")],
C("Une mesure n'a de valeur que si elle est accompagnée de son incertitude, de son unité et de sa traçabilité.",
  "erreur relative = erreur absolue / valeur de référence",
  "justesse · fidélité · résolution · erreur systématique · aléatoire",
  "Mesure~Estimation avec incertitude~Erreur absolue~Mesuré moins reference~Erreur relative~Rapport en pourcentage~Systematique~Reproductible et biaise~Aleatoire~Variable, reducible~Justesse~Proximite de la reference~Fidelite~Concordance des essais~Resolution~Plus petit ecart detectable",
  "Identifier la grandeur et l'unité|Vérifier le calibrage de l'appareil|Répéter la mesure plusieurs fois|Calculer moyenne et dispersion|Écrire le résultat avec son incertitude",
  "Donner trop de chiffres significatifs|Oublier l'unité|Confondre justesse et fidélité|Corriger une erreur aléatoire par un facteur arbitraire|Ne pas noter les conditions de mesure",
  "10,50 g~Fidèle mais injuste~25,0 mL~Moyenne de 3 essais~± 0,2 mL~Incertitude~0,01 mg~Balance analytique~1 g~Balance de cuisine",
  "Erreur systématique~Décalage constant~Erreur aléatoire~Dispersion",
  "Justesse~Proche de la vraie valeur~Fidélité~Proche des autres mesures"))

# ============================================================ PA2
add("PA2", "Spectrophotométrie et loi de Beer-Lambert", "Physique appliquée", ["Terminale"],
S("La spectrophotométrie UV-visible mesure l'absorption d'une lumière par une solution en fonction de la longueur d'onde."
  "|Un spectrophotomètre comporte une source lumineuse, un monochromateur, une cuve, un détecteur et un écran."
  "|La cuve est en quartz pour l'ultraviolet et peut être en plastique ou en verre pour le visible."
  "|L'absorbance A est définie par A = log(I₀/I), où I₀ est l'intensité incidente et I l'intensité transmise."
  "|La transmission T vaut I/I₀ et s'exprime en pourcentage ; on a A = −log(T)."
  "|La loi de Beer-Lambert énonce que A = ε·ℓ·c, avec ε le coefficient d'absorption molaire, ℓ le trajet optique et c la concentration."
  "|L'absorbance est proportionnelle à la concentration dans le domaine de linéarité de l'appareil."
  "|Chaque espèce chimique possède un spectre d'absorption avec une longueur d'onde d'absorption maximale λmax."
  "|On choisit λmax pour la mesure afin d'obtenir la meilleure sensibilité."
  "|Avant toute mesure, on réalise un blanc avec le solvant seul pour annuler l'absorption de la cuve et du solvant."
  "|Une gamme d'étalonnage préparée à partir de solutions de concentrations connues permet de doser un échantillon inconnu."
  "|Une solution trop concentrée s'écarte de la loi de Beer-Lambert : il faut alors la diluer avant mesure."),
[QC("Que mesure un spectrophotomètre ?", "La température~L'absorbance d'une solution~La masse d'un échantillon~Le pH", 1,
     "Il mesure l'atténuation d'un faisceau lumineux traversant la solution."),
 QC("Quelle est la formule de Beer-Lambert ?", "A = ε/ℓc~A = ε·ℓ·c~A = c/(εℓ)~A = ε + ℓ + c", 1,
     "L'absorbance est le produit du coefficient molaire, du trajet optique et de la concentration."),
 QC("Quel est le rôle du blanc ?", "À colorer la solution~À annuler l'absorption du solvant et de la cuve~À diluer l'échantillon~À régler la température", 1,
     "Le blanc soustrait la contribution du milieu et du contenant."),
 QC("Quelle cuve utiliser dans l'ultraviolet ?", "Une cuve en verre~Une cuve en quartz~Une cuve en plastique~Une cuve en métal", 1,
     "Le verre et le plastique absorbent les UV ; le quartz est transparent."),
 QC("Que représente λmax ?", "La longueur d'onde la plus courte~La longueur d'onde d'absorption maximale~La taille de la cuve~La concentration maximale", 1,
     "On mesure à λmax pour gagner en sensibilité."),
 QC("Si l'absorbance double, que se passe-t-il ?", "La concentration double~La concentration est divisée par deux~La concentration ne change pas~La cuve change", 0,
     "Dans le domaine de linéarité, A est proportionnelle à c."),
 QC("Que faire si l'échantillon est trop concentré ?", "Le chauffer~Le diluer~Le filtrer~Le centrifuger", 1,
     "La dilution ramène l'absorbance dans le domaine de validité de la loi."),
 QT("Une solution a une absorbance de 0,60 dans une cuve de 1,0 cm à une longueur d'onde où ε = 120 L·mol⁻¹·cm⁻¹. Calculer sa concentration.",
    "La loi de Beer-Lambert donne A = ε·ℓ·c, donc c = A/(ε·ℓ) = 0,60/(120 × 1,0) = 5,0 × 10⁻³ mol/L. On vérifie l'ordre de grandeur : une absorbance de 0,60 correspond à une transmission d'environ 25 %, ce qui est dans la plage de mesure fiable d'un spectrophotomètre. Si l'absorbance avait été supérieure à 2, il aurait fallu diluer la solution car la relation n'est plus linéaire.",
    "On isole la concentration dans la loi de Beer-Lambert et on vérifie la plage de validité."),
 QT("Décrire la démarche complète de dosage d'un colorant par spectrophotométrie.",
    "On détermine d'abord le spectre d'absorption d'une solution de référence pour repérer λmax. On règle le spectrophotomètre à cette longueur d'onde et on fait le zéro avec un blanc contenant le solvant. On prépare ensuite une gamme d'étalonnage avec au moins cinq concentrations connues, faibles et réparties dans le domaine de linéarité, et on mesure leur absorbance. On trace la droite d'étalonnage A = f(c) et on vérifie sa linéarité. On mesure enfin l'échantillon inconnu dans les mêmes conditions, éventuellement après dilution, et on lit sa concentration sur la droite ou par interpolation. On exprime le résultat avec son incertitude et on mentionne la dilution éventuelle.",
    "On décrit le choix de λmax, le blanc, la gamme, la droite d'étalonnage et la mesure de l'échantillon.")],
C("La spectrophotométrie transforme une absorption de lumière en concentration grâce à la loi de Beer-Lambert et à une gamme d'étalonnage.",
  "A = log(I₀/I) = ε·ℓ·c",
  "λmax · blanc · cuve quartz en UV · gamme d'étalonnage · domaine de linéarité",
  "Absorbance~Log du rapport d'intensites~Beer-Lambert~A = εℓc~Coefficient epsilon~Absorption propre a l'espece~Longueur ℓ~Trajets dans la cuve~Concentration c~Grandeur dosee~Lambda max~Absorption maximale~Blanc~Reference solvant~Gamme~Etalonnage",
  "Repérer la longueur d'onde d'absorption maximale|Régler le blanc et le zéro du spectrophotomètre|Préparer la gamme d'étalonnage|Mesurer les absorbances et tracer la droite|Mesurer l'échantillon et en déduire la concentration",
  "Oublier le blanc|Utiliser une cuve en verre en UV|Travailler hors du domaine de linéarité|Confondre absorbance et transmission|Ne pas tenir compte d'une dilution",
  "A = 0,60~ε = 120 L mol⁻¹ cm⁻¹~ℓ = 1,0 cm~c = 5,0 × 10⁻³ mol/L~T = 25 %~Absorbance 0,6~A > 2~Dilution necessaire",
  "Absorbance~Log I₀ sur I~Transmission~I sur I₀",
  "Blanc~Soustrait le solvant~Échantillon~Solution à doser"))

# ============================================================ PA3
add("PA3", "Chromatographie : principes et lecture d'un chromatogramme", "Physique appliquée", ["1re"],
S("La chromatographie est une méthode de séparation des constituants d'un mélange fondée sur leur répartition entre deux phases."
  "|La phase stationnaire est fixe, sur un support comme le papier ou une colonne de gel de silice."
  "|La phase mobile, ou éluant, entraîne les composés à travers la phase stationnaire."
  "|Les espèces qui interagissent fortement avec la phase stationnaire avancent moins vite."
  "|Le temps nécessaire à un composé pour traverser la colonne est son temps de rétention tR."
  "|Un composé qui ne retarde pas sur la colonne sort avec le temps mort tM."
  "|Le facteur de rétention k' compare tR et tM : k' = (tR − tM)/tM."
  "|Sur une plaque ou un papier, on calcule le rapport frontal Rf = distance parcourue par le composé / distance parcourue par l'éluant."
  "|Le Rf est caractéristique d'un composé dans des conditions données de phase stationnaire, d'éluant et de température."
  "|En chromatographie sur couche mince, les taches sont révélées par lumière UV, vapeurs d'iode ou réactif coloré."
  "|Un chromatogramme est le tracé du signal du détecteur en fonction du temps : chaque pic correspond à un composé."
  "|L'aire d'un pic est proportionnelle à la quantité de composé, ce qui permet un dosage après étalonnage."),
[QC("Qu'est-ce que la phase mobile ?", "Le support fixe~Le solvant qui entraîne les composés~La colonne de silice~Le détecteur", 1,
     "La phase mobile, ou éluant, circule et entraîne les espèces à séparer."),
 QC("Quel composé sort en premier d'une colonne ?", "Celui qui interagit le plus avec la phase stationnaire~Celui qui interagit le moins~Le plus lourd~Le plus coloré", 1,
     "Une faible rétention donne un temps de rétention court."),
 QC("Comment calcule-t-on le rapport frontal Rf ?", "Distance éluant / distance composé~Distance composé / distance éluant~tR / tM~tM / tR", 1,
     "Le Rf est le rapport de la distance du composé sur celle de l'éluant."),
 QC("Quel facteur influence le Rf ?", "La couleur du papier~La nature de l'éluant~La taille de la plaque~L'heure de l'expérience", 1,
     "Le Rf dépend du système chromatographique : phase stationnaire, éluant, température."),
 QC("Que représente le temps mort tM ?", "Le temps de fin d'analyse~Le temps de sortie d'un composé non retenu~Le temps de préparation~La durée de séchage", 1,
     "tM correspond à la traversée de la colonne par la phase mobile seule."),
 QC("Comment révéler des taches incolores en CCM ?", "En les pesant~Par lumière UV ou vapeurs d'iode~En les chauffant à 200 °C~En ajoutant de l'eau", 1,
     "L'UV, l'iode ou un réactif coloré permettent de visualiser les taches."),
 QC("Quelle grandeur d'un pic est liée à la quantité de composé ?", "Sa hauteur uniquement~Son aire~Sa largeur~Sa couleur", 1,
     "L'aire du pic est proportionnelle à la quantité injectée après étalonnage."),
 QT("Expliquer pourquoi deux composés peuvent être séparés par chromatographie alors qu'ils ont des points d'ébullition proches.",
    "La séparation chromatographique ne repose pas sur la volatilité mais sur la différence d'affinité pour les deux phases. À chaque équilibre entre la phase mobile et la phase stationnaire, un composé passe un certain temps adsorbé sur le support et un certain temps entraîné par l'éluant. Deux molécules de points d'ébullition voisins mais de polarités différentes interagissent différemment avec une phase stationnaire polaire comme la silice : la plus polaire est retenue davantage et sort plus tard. En choisissant la nature de l'éluant et du support, on peut amplifier cette différence et obtenir une séparation, même pour des composés très proches.",
    "On oppose l'affinité pour les phases à la volatilité et on cite le rôle de la polarité."),
 QT("Sur une CCM, le front de l'éluant a parcouru 8,0 cm et une tache 5,6 cm. Calculer le Rf et expliquer comment l'utiliser pour identifier le composé.",
    "Le rapport frontal vaut Rf = 5,6/8,0 = 0,70. Pour identifier le composé, on dépose sur la même plaque un échantillon de référence connu, puis on compare les Rf après développement dans les mêmes conditions : deux composés ayant le même Rf dans le même système sont probablement identiques. La comparaison doit être faite avec le même support, le même éluant, la même température et la même distance de migration. En cas de doute, on change de système chromatographique : si les Rf restent égaux dans deux systèmes différents, l'identification est renforcée.",
    "On calcule le rapport, puis on explique la comparaison à un témoin dans des conditions identiques.")],
C("La chromatographie sépare selon l'affinité pour deux phases ; le temps de rétention ou le Rf identifie, l'aire quantifie.",
  "Rf = distance composé / distance éluant · k' = (tR − tM)/tM",
  "phase stationnaire · phase mobile · temps de rétention · pic · aire",
  "Phase stationnaire~Support fixe~Silice ou papier~Phase mobile~Eluant entraineur~Retention~Interaction avec le support~Rf~Distance composee sur distance eluant~Temps de retention~Sortie du pic~Temps mort~Composé non retenu~Plaque CCM~Chromatographie sur couche mince~Revelation~UV ou iode~Aire du pic~Quantite",
  "Choisir le couple phase stationnaire et éluant|Déposer l'échantillon et un témoin|Développer la plaque ou lancer la colonne|Révéler et mesurer les distances ou les temps|Calculer Rf ou k' et interpréter",
  "Mélanger les distances du composé et de l'éluant|Changer d'éluant entre deux comparaisons|Oublier de révéler les taches incolores|Prendre la hauteur d'un pic pour une quantité|Laisser la plaque se saturer",
  "5,6 cm sur 8,0 cm~Rf = 0,70~tR~Temps de retention~tM~Temps mort~k'=(tR−tM)/tM~Facteur de retention~Aire du pic~Quantite dosee",
  "Phase stationnaire~Fixe~Phase mobile~En mouvement",
  "CCM~Rapide et qualitative~Colonne~Séparation et dosage"))

# ============================================================ PA4
add("PA4", "Électrophorèse des biomolécules", "Physique appliquée", ["Terminale"],
S("L'électrophorèse sépare des molécules chargées sous l'effet d'un champ électrique."
  "|Les molécules migrent vers l'électrode de charge opposée à la leur."
  "|La vitesse de migration dépend de la charge de la molécule, de sa taille et de la viscosité du milieu."
  "|L'électrophorèse sur gel d'agarose est courante pour séparer les acides nucléiques."
  "|L'ADN porte une charge négative due à ses groupements phosphate et migre vers l'anode positive."
  "|Le gel d'agarose agit comme un tamis : les petits fragments avancent plus vite que les grands."
  "|La distance de migration dépend de la taille du fragment : un marqueur de taille permet de l'estimer."
  "|On révèle les bandes d'ADN avec un colorant fluorescent ou intercalant, sous lumière UV ou bleue."
  "|L'électrophorèse sur gel de polyacrylamide sépare plutôt les protéines."
  "|En PAGE-SDS, le détergent SDS dénature les protéines et leur donne une charge proportionnelle à leur masse."
  "|Le gel se colore avec du bleu de Coomassie ou est transféré sur membrane pour un western blot."
  "|Cette technique est utilisée pour contrôler un extrait d'ADN, un produit PCR ou la pureté d'une protéine."),
[QC("Vers quelle électrode migre l'ADN ?", "Vers la cathode négative~Vers l'anode positive~Il ne bouge pas~Vers les deux à la fois", 1,
     "L'ADN est négatif à cause des phosphates : il va vers l'anode positive."),
 QC("Que représente le gel d'agarose ?", "Une source de courant~Un tamis qui ralentit les grands fragments~Un colorant~Une membrane", 1,
     "Le gel est un réseau poreux dont la maille sépare selon la taille."),
 QC("Quel fragment migre le plus vite ?", "Le plus long~Le plus court~Le plus coloré~Le plus acide", 1,
     "Les petits fragments traversent plus facilement les pores du gel."),
 QC("À quoi sert un marqueur de taille ?", "À colorer le gel~À estimer la taille des fragments~À augmenter le courant~À régler le pH", 1,
     "Le marqueur contient des fragments de tailles connues qui servent d'échelle."),
 QC("Comment révèle-t-on les bandes d'ADN ?", "Par un colorant fluorescent~Par la chaleur~Par pesée~Par le goût", 0,
     "Un colorant intercalant ou fluorescent rend les bandes visibles sous UV ou lumière bleue."),
 QC("Quel est le rôle du SDS en PAGE ?", "Il rend la charge proportionnelle à la masse~Il colore les protéines~Il solidifie le gel~Il coupe l'ADN", 0,
     "Le SDS dénature les protéines et uniformise leur rapport charge/masse."),
 QC("Quelle technique identifie une protéine après transfert sur membrane ?", "La CCM~Le western blot~La PCR~La titration", 1,
     "Le western blot utilise un anticorps spécifique après transfert sur membrane."),
 QT("Expliquer pourquoi deux fragments d'ADN de tailles différentes se séparent sur un gel d'agarose.",
    "L'ADN possède une charge négative à peu près proportionnelle à sa longueur, donc tous les fragments sont attirés vers l'anode avec une force qui croît avec leur taille. Cependant, le gel d'agarose forme un réseau de pores qui oppose une résistance : les grands fragments se coincent plus souvent et avancent plus lentement, tandis que les petits glissent plus facilement. La mobilité dépend donc de la taille et non de la charge seule. En comparant la distance parcourue à celle d'un marqueur de taille, on estime la longueur des fragments en paires de bases.",
    "On oppose la force électrique proportionnelle à la charge à l'effet de tamis du gel."),
 QT("Décrire les précautions à prendre pour réaliser un gel d'agarose et éviter les erreurs d'interprétation.",
    "On prépare le gel avec la concentration d'agarose adaptée à la gamme de tailles visée, on le coule sans bulles et on retire le peigne avec précaution pour garder des puits nets. On dépose les échantillons avec un tampon de charge dense, sans percer le fond des puits, et on dépose un marqueur de taille dans au moins un puits. On vérifie le sens du courant : les puits doivent être côté cathode pour que l'ADN migre vers l'anode. On arrête la migration avant que les petits fragments ne sortent du gel. Enfin, on manipule le colorant et la source UV avec des gants et des lunettes, et on photographie le gel avec une échelle pour mesurer les distances.",
    "On cite la préparation du gel, le sens du courant, le marqueur, l'arrêt de la migration et la sécurité.")],
C("L'électrophorèse sépare les biomolécules chargées par leur taille et leur charge, grâce à un gel servant de tamis.",
  "ADN négatif → anode · petit fragment → migration rapide",
  "agarose · marqueur de taille · révélation UV · PAGE-SDS · western blot",
  "Electrophorese~Migration sous champ~Charge negative~Vers anode~Gel agarose~Tamis moleculaire~Taille~Petit fragment rapide~Marqueur~Echelle de taille~Revelation~Colorant et UV~PAGE-SDS~Proteines~Charge proportionnelle a la masse~Western blot~Anticorps specifique",
  "Préparer le gel et choisir sa concentration|Déposer échantillons et marqueur|Vérifier l'orientation du courant|Arrêter la migration au bon moment|Révéler et mesurer les bandes",
  "Inverser les électrodes|Perforer le fond des puits|Oublier le marqueur de taille|Laisser migrer trop longtemps|Manipuler l'UV sans protection",
  "ADN~Charge negative~Anode positive~Agarose~Tamis~Petit fragment~Avance vite~Marqueur~Paires de bases~Colorant~Bandes visibles",
  "Agarose~Acides nucleiques~Polyacrylamide~Proteines",
  "PAGE-SDS~Sépare par masse~Western blot~Identifie par anticorps"))

# ============================================================ AD1
add("AD1", "Préparation des solutions et dilutions", "Analyses et dosages", ["1re"],
S("Une solution est un mélange homogène d'un soluté dissous dans un solvant, le plus souvent l'eau."
  "|La quantité de matière n se calcule avec la masse m et la masse molaire M selon n = m/M."
  "|La concentration molaire d'une solution vaut c = n/V, avec V le volume de la solution en litres."
  "|Pour préparer 100 mL d'une solution à 0,10 mol/L, on pèse n = c·V = 0,010 mol de soluté."
  "|La masse à peser est alors m = n·M, calculée avant toute manipulation."
  "|On dissout le soluté dans un petit volume d'eau avant de compléter au trait de jauge d'une fiole jaugée."
  "|La fiole jaugée est utilisée pour un volume précis ; l'éprouvette graduée est moins précise."
  "|Le ménisque doit être lu à hauteur d'oeil, sa base affleurant le trait de jauge pour une solution aqueuse."
  "|Une dilution consiste à ajouter du solvant en conservant la quantité de soluté : c₁V₁ = c₂V₂."
  "|Une dilution au 1/10 se prépare par exemple en prélevant 10,0 mL de solution mère et en complétant à 100 mL."
  "|Les solutions mères concentrées permettent de préparer facilement des gammes de faibles concentrations."
  "|Chaque solution doit être étiquetée avec le nom du soluté, la concentration, la date et le nom du préparateur."),
[QC("Quelle verrerie donne le volume le plus précis ?", "Le bécher~L'éprouvette graduée~La fiole jaugée~Le flacon", 2,
     "La fiole jaugée est calibrée pour un volume unique de haute précision."),
 QC("Comment calculer la masse à peser ?", "m = c·V·M~m = c/(V·M)~m = V/(c·M)~m = c + V + M", 0,
     "n = cV puis m = nM, donc m = c·V·M."),
 QC("Que faut-il faire après avoir dissous le soluté ?", "Chauffer jusqu'à évaporation~Compléter au trait de jauge~Ajouter autant de soluté~Filtrer à sec", 1,
     "On complète doucement avec le solvant jusqu'au trait de jauge."),
 QC("Comment lit-on un ménisque ?", "Par dessus~À hauteur d'oeil~Par dessous~Au toucher", 1,
     "Une lecture à hauteur d'oeil évite l'erreur de parallaxe."),
 QC("Que conserve-t-on lors d'une dilution ?", "La concentration~Le volume total~La quantité de soluté~Le pH", 2,
     "La quantité de soluté reste constante : c₁V₁ = c₂V₂."),
 QC("Comment préparer une dilution au 1/10 ?", "10 mL de solution mère complétés à 100 mL~1 mL complété à 10 mL~100 mL complétés à 10 mL~Mélanger 10 mL d'eau et 10 mL de solution", 0,
     "Le facteur 10 s'obtient en passant de 10 mL à 100 mL."),
 QC("Que doit indiquer l'étiquette d'une solution ?", "Seulement la date~Le nom, la concentration, la date et le préparateur~La couleur du bouchon~Le prix du réactif", 1,
     "Une étiquette complète garantit la traçabilité et la sécurité."),
 QT("On veut préparer 250 mL de solution de sulfate de cuivre 0,050 mol/L. La masse molaire vaut 249,7 g/mol. Calculer la masse à peser.",
    "La quantité de matière nécessaire est n = c·V = 0,050 × 0,250 = 0,0125 mol. La masse à peser vaut m = n·M = 0,0125 × 249,7 = 3,12 g environ. On pèsera donc 3,12 g de sulfate de cuivre, on les dissoudra dans un peu d'eau distillée, puis on transférera la solution dans une fiole jaugée de 250 mL et on complétera au trait de jauge. On bouchera et on homogénéisera par retournements avant d'étiqueter.",
    "On calcule n puis m, puis on décrit la préparation avec la fiole jaugée."),
 QT("Expliquer la différence entre une solution mère et une solution fille et l'intérêt des dilutions en cascade.",
    "La solution mère est une solution concentrée préparée une fois par pesée et dissoute dans un volume connu. Les solutions filles sont obtenues par dilution de la solution mère, avec un facteur de dilution connu. Les dilutions en cascade permettent d'obtenir des concentrations très faibles avec un bon contrôle : plutôt que de prélever un volume minuscule directement dans la solution mère, on effectue plusieurs étapes de dilution au 1/10, chacune facile à réaliser avec une pipette et une fiole jaugée. Le facteur total est le produit des facteurs successifs. Cette méthode est utilisée pour préparer les gammes d'étalonnage et les suspensions bactériennes.",
    "On définit mère et fille, puis on justifie la précision et la commodité des dilutions successives.")],
C("Préparer une solution, c'est calculer une masse puis un volume avec soin ; diluer, c'est conserver la quantité de soluté.",
  "n = m/M · c = n/V · c₁V₁ = c₂V₂",
  "fiole jaugée · ménisque · trait de jauge · solution mère · facteur de dilution",
  "Solution~Soluté dans solvant~Quantite n~Masse sur masse molaire~Concentration c~Quantite sur volume~Fiole jaugee~Volume precis~Menisque~Lecture a hauteur d'oeil~Dilution~Ajout de solvant~Solution mere~Concentree~Solution fille~Diluee~Etiquette~Tracabilite",
  "Calculer la quantité de matière puis la masse|Peser et dissoudre le soluté|Transférer dans la fiole jaugée|Compléter au trait et homogénéiser|Étiqueter et consigner la préparation",
  "Compléter avant dissolution complète|Lire le ménisque de travers|Confondre volume de solvant et volume de solution|Oublier de boucher et d'homogénéiser|Ne pas étiqueter la solution",
  "c = 0,050 mol/L, V = 0,250 L~n = 0,0125 mol~M = 249,7 g/mol~m ≈ 3,12 g~10 mL à 100 mL~Dilution au 1/10~Facteur 10⁻³~Trois étapes",
  "Solution mère~Concentrée~Solution fille~Diluée",
  "Fiole jaugée~Volume précis~Éprouvette~Volume approximatif"))

# ============================================================ AD2
add("AD2", "Dosage par étalonnage et gamme de calibration", "Analyses et dosages", ["Terminale"],
S("Un dosage par étalonnage détermine la concentration d'un échantillon en le comparant à des solutions de référence."
  "|On prépare une gamme d'étalonnage avec au moins cinq solutions de concentrations connues et croissantes."
  "|Les solutions de la gamme sont préparées par dilution d'une solution mère, avec un facteur de dilution tracé."
  "|On mesure le même signal pour chaque solution de la gamme, dans les mêmes conditions expérimentales."
  "|La droite d'étalonnage relie le signal mesuré à la concentration : signal = pente × c + ordonnée à l'origine."
  "|Le coefficient de détermination R² évalue la qualité de l'ajustement linéaire : plus il est proche de 1, meilleur est l'ajustement."
  "|L'échantillon est mesuré de la même manière, éventuellement après dilution."
  "|On déduit sa concentration de l'équation de la droite, en tenant compte du facteur de dilution."
  "|La gamme doit encadrer la concentration attendue de l'échantillon : on ne doit pas extrapoler."
  "|Un blanc est mesuré pour soustraire le signal de fond du solvant et des réactifs."
  "|La limite de détection est la plus petite concentration que la méthode peut distinguer du blanc."
  "|La limite de quantification est la plus petite concentration que l'on peut doser avec une précision acceptable."),
[QC("Combien de solutions faut-il au minimum dans une gamme d'étalonnage ?", "Une~Trois~Cinq~Dix", 2,
     "Cinq concentrations au minimum donnent un ajustement fiable."),
 QC("Que relie la droite d'étalonnage ?", "Le temps et la température~Le signal et la concentration~La masse et le volume~Le pH et la couleur", 1,
     "On porte le signal en ordonnée et la concentration en abscisse."),
 QC("Que signifie un R² proche de 1 ?", "Une mauvaise linéarité~Un bon ajustement linéaire~Une gamme trop courte~Un blanc contaminé", 1,
     "R² mesure la part de variance expliquée par la droite."),
 QC("Faut-il extrapoler hors de la gamme ?", "Oui, toujours~Non, il faut que la gamme encadre l'échantillon~Seulement pour les UV~Seulement si R² > 0,9", 1,
     "L'extrapolation n'est pas validée par la droite d'étalonnage."),
 QC("À quoi sert le blanc ?", "À augmenter le signal~À soustraire le signal de fond~À diluer l'échantillon~À remplacer la gamme", 1,
     "Le blanc mesure le signal du solvant et des réactifs seuls."),
 QC("Quelle est la limite de détection ?", "La concentration maximale~La plus petite concentration distinguishable du blanc~Le nombre de solutions de la gamme~L'incertitude sur la pente", 1,
     "Elle correspond au plus faible signal significativement supérieur au bruit de fond."),
 QC("Que faut-il faire si l'échantillon est trop concentré ?", "Le diluer puis tenir compte du facteur~Le chauffer~Le filtrer~Le peser", 0,
     "Après dilution, on multiplie la concentration lue par le facteur de dilution."),
 QT("Une droite d'étalonnage a pour équation A = 1250·c + 0,01, avec c en mol/L. L'échantillon dilué 10 fois donne A = 0,51. Calculer la concentration initiale.",
    "On isole la concentration de l'échantillon dilué : c_dilué = (A − 0,01)/1250 = (0,51 − 0,01)/1250 = 0,50/1250 = 4,0 × 10⁻⁴ mol/L. L'échantillon a été dilué dix fois, donc sa concentration initiale est dix fois supérieure : c_initial = 4,0 × 10⁻³ mol/L. On vérifie que la valeur lue, 0,50 d'absorbance corrigée, se situe bien dans la plage de la gamme d'étalonnage, ce qui valide l'utilisation de la droite.",
    "On soustrait l'ordonnée à l'origine, on divise par la pente, puis on corrige par le facteur de dilution."),
 QT("Expliquer pourquoi il faut préparer la gamme et les échantillons dans les mêmes conditions expérimentales.",
    "Le signal mesuré dépend non seulement de la concentration mais aussi de la température, du pH, du temps de réaction, de la cuve ou du lot de réactifs. Si la gamme et les échantillons ne sont pas traités de la même manière, une partie du signal proviendra de ces différences et la droite d'étalonnage ne sera pas applicable à l'échantillon, ce qui biaiserait le résultat. C'est pourquoi on utilise le même blanc, le même protocole, la même verrerie et la même gamme de concentrations, idéalement en alternant les mesures. On parle de conditions de mesure identiques pour garantir la comparabilité des signaux et la validité du dosage.",
    "On identifie les paramètres qui influencent le signal et on explique le biais possible.")],
C("Le dosage par étalonnage compare un signal inconnu à une gamme de référence : la rigueur de la gamme conditionne la validité du résultat.",
  "signal = pente × c + b · c = (signal − b)/pente × facteur de dilution",
  "gamme · R² · blanc · extrapolation interdite · limite de quantification",
  "Etalonnage~Comparaison a des references~Gamme~Cinq concentrations~Droite~Signal en fonction de c~Pente~Sensibilite de la methode~R²~Qualite de l'ajustement~Blanc~Signal de fond~Extrapolation~Hors gamme, interdite~Limite de detection~Plus petit signal sur bruit~Facteur de dilution~Correction finale",
  "Préparer la solution mère et les dilutions de la gamme|Mesurer le blanc|Relever le signal de chaque solution|Tracer la droite et vérifier R²|Mesurer l'échantillon et corriger la dilution",
  "Utiliser une gamme trop étroite|Extrapoler hors gamme|Oublier de soustraire le blanc|Négliger le facteur de dilution|Changer de cuve entre gamme et échantillon",
  "A = 1250c + 0,01~Signal corrigé 0,50~c dilué = 4,0 × 10⁻⁴ mol/L~Dilution 10~c initial = 4,0 × 10⁻³ mol/L~R² ≈ 1~Bonne linéarité",
  "Étalonnage externe~Gamme separate~Étalonnage interne~Reference ajoutee",
  "Limite de détection~Voir le signal~Limite de quantification~Doser avec précision"))

# ============================================================ AD3
add("AD3", "Gravimétrie et pesée analytique", "Analyses et dosages", ["Terminale"],
S("La gravimétrie est une méthode d'analyse qui détermine une masse, souvent après séparation ou transformation chimique."
  "|Le dosage gravimétrique consiste à isoler un constituant sous forme d'un précipité, à le sécher puis à le peser."
  "|On choisit un précipitant qui forme un composé peu soluble avec l'ion à doser."
  "|La précipitation doit être lente et en milieu approprié pour obtenir des cristaux faciles à filtrer."
  "|Le précipité est filtré, lavé pour éliminer les ions adsorbés, puis séché à l'étuve."
  "|On pèse le précipité jusqu'à masse constante : deux pesées successives doivent être identiques."
  "|La balance analytique est placée sur une table anti-vibratile, à l'abri des courants d'air et des variations de température."
  "|La porte de la balance doit rester fermée pendant la pesée pour éviter les courants d'air."
  "|Le creuset ou le filtre est taré avant d'accueillir le précipité."
  "|La masse du précipité est convertie en quantité de matière puis en concentration de l'ion dosé."
  "|Une erreur de lavage ou de séchage se répercute directement sur le résultat final."
  "|La gravimétrie est une méthode absolue, précise mais lente, souvent utilisée comme méthode de référence."),
[QC("Que détermine un dosage gravimétrique ?", "Un volume~Une masse~Une absorbance~Une température", 1,
     "La gravimétrie repose sur la pesée d'un précipité isolé."),
 QC("Que faut-il faire après la filtration du précipité ?", "Le peser immédiatement avec l'eau~Le laver puis le sécher~Le dissoudre dans l'acide~Le chauffer à flamme nue", 1,
     "Le lavage élimine les ions adsorbés et le séchage donne une masse reproducible."),
 QC("Que signifie peser jusqu'à masse constante ?", "Peser une seule fois~Obtenir deux pesées identiques après séchage~Peser à jeun~Utiliser une balance de cuisine", 1,
     "Deux pesées successives après séchage doivent coïncider."),
 QC("Pourquoi placer la balance sur une table anti-vibratile ?", "Pour la décorer~Pour éviter que les vibrations ne perturbent la mesure~Pour la chauffer~Pour augmenter sa capacité", 1,
     "Les vibrations et les courants d'air sont des sources d'erreur majeures."),
 QC("Que veut dire tarer un creuset ?", "Le laver~Enregistrer sa masse à vide~Le remplir d'eau~Le chauffer au rouge", 1,
     "La tare donne la masse du contenant vide, à soustraire de la masse brute."),
 QC("Quel défaut donne une masse trop élevée du précipité ?", "Un lavage insuffisant~Un séchage trop long~Une balance bien tarée~Une filtration lente", 0,
     "Les sels adsorbés ou entrainés augmentent la masse mesurée."),
 QC("Quel est un avantage de la gravimétrie ?", "Sa rapidité~Sa précision comme méthode absolue~Son absence de verrerie~Sa tolérance aux erreurs", 1,
     "Bien conduite, la gravimétrie est très précise et ne nécessite pas d'étalonnage externe."),
 QT("Un précipité de sulfate de baryum BaSO₄ pèse 0,2334 g après séchage. Calculer la quantité de matière d'ions sulfate dosée. M(BaSO₄) = 233,4 g/mol.",
    "La quantité de matière de sulfate de baryum vaut n = m/M = 0,2334/233,4 = 1,000 × 10⁻³ mol. La réaction de précipitation associe un ion sulfate Ba²⁺ + SO₄²⁻ → BaSO₄ pour un ion sulfate par formule, donc n(SO₄²⁻) = n(BaSO₄) = 1,00 × 10⁻³ mol. On en déduirait la concentration initiale en divisant par le volume d'échantillon traité. La masse ayant été relevée après séchage à masse constante, le résultat est fiable à condition que le précipité ait été correctement lavé.",
    "On convertit la masse en quantité de matière avec la masse molaire, puis on utilise la stœchiométrie."),
 QT("Expliquer pourquoi le lavage et le séchage du précipité sont deux étapes critiques d'une analyse gravimétrique.",
    "Après la filtration, le précipité retient dans ses pores et sur ses cristaux une partie de la solution mère, contenant des ions solubles. S'il n'est pas lavé à l'eau distillée ou avec une solution adaptée, ces sels restent piégés et augmentent la masse mesurée : le dosage donne une valeur trop élevée. Le séchage, généralement à l'étuve, élimine l'eau résiduelle ; une masse encore humide conduit elle aussi à une surestimation. On répète chauffage, refroidissement au dessiccateur et pesée jusqu'à obtenir une masse constante, ce qui prouve que l'eau a été entièrement éliminée. Ces deux étapes conditionnent donc l'exactitude du résultat.",
    "On explique l'effet des sels adsorbés et de l'humidité résiduelle, puis la notion de masse constante.")],
C("La gravimétrie convertit une masse de précipité en quantité d'ion dosée : la rigueur du lavage et du séchage fait la précision.",
  "n = m/M · masse à constante après séchage",
  "précipitation · filtration · lavage · étuve · balance analytique · tare",
  "Gravimetrie~Dosage par masse~Precipite~Compose peu soluble~Precipitation~Formation lente~Filtration~Separation du solide~Lavage~Elimination des ions~Etuve~Sechage~Masse constante~Deux pesées egales~Balance analytique~Precision au 0,1 mg~Tare~Masse du contenant vide",
  "Choisir le précipitant et précipiter lentement|Filtrer et laver le précipité|Sécher à l'étuve puis refroidir|Peser jusqu'à masse constante|Convertir la masse en quantité d'ion",
  "Peser un précipité humide|Négliger le lavage|Laisser la porte de la balance ouverte|Peser sans tarer le creuset|Chauffer trop fort et décomposer le précipité",
  "BaSO₄~0,2334 g~M = 233,4 g/mol~n = 1,00 × 10⁻³ mol~0,1 mg~Resolution balance~Masse constante~Pesées identiques",
  "Gravimétrie~Méthode absolue~Colorimétrie~Nécessite un étalonnage",
  "Tare~Masse du vide~Masse brute~Contenant + produit"))

# FIN_PARTIE_4

valider_et_ecrire(F, "stl-mat-part-B.json")
