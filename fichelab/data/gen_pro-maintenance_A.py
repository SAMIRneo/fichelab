# -*- coding: utf-8 -*-
"""Generateur pro-maintenance-mat-part-A.json — lot A : tronc commun.

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


# ============================================================ FR1
add("FR1", "Figures de style et argumentation dans un texte technique", "Français",
S("Une figure de style est un procede volontaire qui s'ecarte de l'usage courant pour produire un effet de sens."
  "|La comparaison rapproche explicitement deux elements avec un outil comme, tel, semblable a."
  "|La metaphore est un rapprochement implicite, sans outil de comparaison."
  "|La personnification attribue un trait humain a un objet, un animal ou une machine."
  "|L'enumeration accumule des termes pour donner du rythme et insister sur une realite."
  "|La repetition relance un mot ou une structure et renforce la memorisation."
  "|L'antithese oppose deux termes pour rendre un contraste visible."
  "|La litote dit moins pour suggerer davantage."
  "|L'ironie dit le contraire de ce que l'on pense pour produire un effet critique."
  "|Dans un texte technique, la figure sert surtout a vulgariser une notion abstraite et a convaincre."
  "|Un argument est une raison appuyee sur un fait, une regle ou une experience."
  "|L'analyse identifie d'abord le sens, puis le procede, puis l'effet produit."),
[QC("Quel mot introduit une comparaison explicite ?", "Mais~Comme~Donc~Or", 1,
     "Comme est un outil de comparaison ; mais, donc et or sont des connecteurs logiques."),
 QC("Quelle figure ne comporte aucun outil de comparaison ?", "La comparaison~La metaphore~L'enumeration~La litote", 1,
     "La metaphore est implicite : aucun outil tel que comme n'apparait."),
 QC("Quelle figure attribue des traits humains a une machine ?", "L'antithese~La personnification~La repetition~La litote", 1,
     "La personnification donne une intention ou un sentiment a un etre non humain."),
 QC("Quel effet produit une enumeration ?", "Ralentir la lecture~Accumuler et rythmer~Supprimer le sens~Cacher l'argument", 1,
     "L'enumeration donne une impression d'abondance et cadence la phrase."),
 QC("Quel connecteur marque l'opposition ?", "Pourtant~En effet~De plus~Ainsi", 0,
     "Pourtant introduce une opposition ; en effet explique, de plus ajoute, ainsi conclut."),
 QC("A quoi sert une figure de style dans un texte technique ?", "A compliquer le propos~A vulgariser et convaincre~A remplacer les donnees~A masquer une erreur", 1,
     "La figure rend une notion abstraite plus accessible et renforce l'adhésion."),
 QC("Quelle figure dit le contraire de ce que l'on pense ?", "L'ironie~La litote~L'antithese~La metaphore", 0,
     "L'ironie affirme le contraire pour produire un effet critique."),
 QT("Distinguer la comparaison de la metaphore et donner un exemple pour chacune dans un contexte de maintenance.",
    "La comparaison explicite le rapprochement avec un outil : 'le roulement gronde comme un tambour'. La metaphore supprime l'outil : 'ce roulement est un tambour', ou 'la courroie est le coeur de la transmission'. Les deux transferent une image connue vers une realite technique, mais la metaphore est plus compacte et frappante, tandis que la comparaison reste plus claire pour un lecteur non specialiste.",
    "On attend la presence ou l'absence d'outil de comparaison et un exemple technique pour chaque figure."),
 QT("Analyser l'effet de la personnification dans la phrase : 'la pompe reclame sa vidange'.",
    "Une pompe ne peut pas reclamer : le verbe est emprunte au langage humain. La personnification rend la consigne plus memorable et suggere une necessite presque vitale. Elle ne remplace pas l'instruction technique : il faut ensuite expliciter 'effectuer la vidange toutes les 500 heures' pour rester precis et verifiable.",
    "On identifie le procede, on decrit l'effet produit, puis on rappelle que le texte technique doit rester exact.")],
C("Une figure de style est un ecart volontaire du langage : nommer le procede permet de comprendre l'effet de sens voulu.",
  "Figure = ecart + intention + effet",
  "Comparaison : avec outil · Metaphore : sans outil · Personnification : trait humain",
  "Comparaison~Rapprochement explicite~Comme, tel~Metaphore~Rapprochement implicite~Sans outil~Personnification~Trait humain~Donne vie a la machine",
  "Lire le passage|Repérer les écarts de sens|Nommer la figure|Décrire l'effet|Relier à l'intention du texte",
  "Confondre comparaison et métaphore|Nommer la figure sans expliquer l'effet|Oublier le contexte technique|Prendre l'image au sens littéral",
  "Comparaison~Le joint fuit comme une gouttière|Métaphore~Cette courroie est le coeur de la ligne|Antithèse~Simple apparence, réalité complexe|Personnification~La pompe réclame sa vidange",
  "Comparaison~Avec un outil~Plus claire~Metaphore~Sans outil~Plus frappante",
  "Figure~Effet de sens~Argument~Fait ou règle~Soutien~Exemple concret"))

# ============================================================ FR2
add("FR2", "Construire un texte argumenté : thèse, arguments, exemples", "Français",
S("Un texte argumente vise a convaincre un lecteur d'une these."
  "|La these est l'opinion defensive, presenter des le debut ou a la fin."
  "|Un argument est une raison generale qui justifie la these."
  "|Un exemple est un cas concret qui rend l'argument credible."
  "|Les connecteurs logiques organisent le raisonnement : en effet, donc, pourtant, ainsi."
  "|Le plan deductif part de l'idee generale pour arriver au cas particulier."
  "|Le plan inductif part d'exemples pour degager une conclusion generale."
  "|Le plan dialectique confronte une these et une objection avant une synthese."
  "|Une objection est une objection previsible qu'il faut refuter pour renforcer son propos."
  "|La nuance evite la generalisation abusive et rend le propos plus juste."
  "|Dans un rapport d'intervention, l'argumentation s'appuie sur des mesures et des faits."
  "|La conclusion repond a la probleme pose et ouvre eventuellement une perspective."),
[QC("Qu'appelle-t-on these dans un texte argumente ?", "Un exemple~L'opinion defensive~Un connecteur~Une objection", 1,
     "La these est le point de vue que l'auteur cherche a faire admettre."),
 QC("Quel rôle joue un exemple ?", "Remplacer l'argument~Rendre l'argument concret~Introduire une objection~Conclure le texte", 1,
     "L'exemple illustre et rend credible la raison generale."),
 QC("Quel connecteur introduit une cause ?", "Pourtant~En effet~Ainsi~Cependant", 1,
     "En effet introduce une explication ou une cause ; ainsi marque la consequence."),
 QC("Comment fonctionne un plan inductif ?", "De la these au cas~Des exemples a la conclusion~De l'objection a la these~Sans exemple", 1,
     "L'induction part de cas observes pour degager une regle generale."),
 QC("A quoi sert une objection ?", "A affaiblir le texte~A anticiper une objection et a la refuter~A remplacer la these~A supprimer les exemples", 1,
     "L'objection, une fois refutee, renforce la these."),
 QC("Quel est le risque d'une generalisation abusive ?", "Un texte trop court~Une affirmation fausse ou injuste~Trop de connecteurs~Un plan dialectique", 1,
     "Sans nuance, l'affirmation depasse ce que les faits permettent."),
 QC("Sur quoi s'appuie l'argumentation d'un rapport d'intervention ?", "Sur des mesures et des faits~Sur des opinions personnelles~Sur la longueur du texte~Sur le hasard", 0,
     "Un rapport technique argumente a partir de releves, de mesures et de constats."),
 QT("Distinguer plan deductif, inductif et dialectique et indiquer quand les utiliser.",
    "Le plan deductif pose d'abord la these, puis developpe les arguments et les exemples : il convient quand l'opinion est claire des le depart. Le plan inductif presente d'abord des cas concrets, puis degage la conclusion : il est utile quand les mesures parlent d'elles-memes. Le plan dialectique confronte these, objection et synthese : il est adapte quand le sujet est discute ou incertain, par exemple pour choisir entre maintenance preventive et corrective.",
    "On definit chaque plan et on propose un contexte d'usage pertinent."),
 QT("Rédiger un court paragraphe argumente en faveur de la maintenance preventive en atelier.",
    "La maintenance preventive doit etre prioritaire sur les equipements critiques, car elle réduit les arrets non prevus. En effet, le remplacement programmé d'une courroie avant sa rupture evite une interruption de production et les degats collateraux. Par exemple, un relevé de vibrations hebdomadaire permet de detecter une degradation naissante et de planifier l'intervention. Pourtant, la preventive a un cout : elle doit donc etre dimensionnee a partir des donnees de fiabilité et non appliquee aveuglément a toutes les machines.",
    "On attend une these, au moins deux arguments, un exemple, une nuance et des connecteurs.")],
C("Argumenter, c'est defendre une these avec des raisons et des exemples, en anticipant les objections et en nuancant.",
  "These + arguments + exemples + nuances",
  "Deductif : these d'abord · Inductif : exemples d'abord · Dialectique : these, objection, synthese",
  "These~Opinion defensive~Argument~Raison generale~Exemple~Cas concret~Objection~Opinion contraire~Synthese~Decision nuancee",
  "Choisir la these a defendre|Reunir arguments et exemples|Anticiper une objection|Ordonner avec des connecteurs|Conclure en repondant au probleme",
  "Avancer une these sans preuve|Confondre argument et exemple|Generaliser a partir d'un seul cas|Oublier de refuter l'objection",
  "En effet~Introduit une cause~Donc~Marque la consequence~Pourtant~Introduit une objection~Ainsi~Introduit la conclusion",
  "Deductif~These puis preuves~Inductif~Exemples puis these",
  "Objection~Point faible anticipe~Refutation~Reponse apportee a l'objection"))

# ============================================================ FR3
add("FR3", "Le compte rendu d'intervention : structure et précision", "Français",
S("Le compte rendu d'intervention est un ecrit professionnel qui relate une action technique."
  "|Il doit etre factuel : seuls les faits observes et les mesures relevees sont rapportes."
  "|La structure courante comprend l'identification, le contexte, les operations, les resultats et la conclusion."
  "|L'identification precise la date, le lieu, l'equipement et l'intervenant."
  "|Le contexte rappelle le symptome signale et la demande du client."
  "|Les operations sont decrites dans l'ordre chronologique avec des verbes d'action."
  "|Les resultats sont exprimes avec des valeurs chiffrees et des unites."
  "|Le vocabulaire technique doit etre exact et univoque."
  "|Les phrases courtes et la voix passive facilitent la lecture rapide."
  "|Les abbreviations doivent etre definies ou evitees."
  "|La conclusion indique l'etat final, les pieces remplacees et les recommandations."
  "|Un compte rendu relu et signeengage la responsabilite de son auteur."),
[QC("Quelle qualité est Prioritaire dans un compte rendu ?", "La fantasy~Le caracter factuel~La longueur~Le tone humoristique", 1,
     "Le compte rendu doit rapporter des faits verifiables, pas des impressions."),
 QC("Quelle information appartient a l'identification ?", "La couleur de la machine~La date et l'equipement~Une hypothese~Une recommandation", 1,
     "Date, lieu, machine et intervenant identifient l'intervention."),
 QC("Dans quel ordre decrire les operations ?", "Par ordre d'importance~Par ordre chronologique~Au hasard~Par ordre alphabetique", 1,
     "La chronologie permet de reconstituer le deroulement exact."),
 QC("Comment exprimer un resultat ?", "Avec des adjectifs~Avec des valeurs chiffrees et des unites~Avec des métaphores~Sans precision", 1,
     "Une mesure sans unite n'est pas exploitable."),
 QC("Quel style de phrase est conseille ?", "Des phrases courtes~Des phrases tres longues~Beaucoup d'ironie~Des abréviations inconnues", 0,
     "La concision et la clarte priment dans un ecrit professionnel."),
 QC("Que contient la conclusion ?", "Un souhait personnel~L'etat final et les recommandations~Une blague~Le prix du client", 1,
     "On indique l'etat de l'equipement et les suites a donner."),
 QC("Qui engage sa responsabilite en signant le compte rendu ?", "Le fournisseur seul~L'auteur du document~Le client~Personne", 1,
     "La signature engage la personne qui a redige et valide le contenu."),
 QT("Rédiger les trois phrases principales d'un compte rendu apres le remplacement d'une courroie sur un convoyeur.",
    "Le 14 mars, sur le convoyeur CV2 de l'atelier Nord, nous avons procede au remplacement de la courroie de transmission apres un arret signale a 8 h 15. La courroie d'origine presentait une usure prononcee et une fissure sur 40 mm ; la tension mesurée avant intervention etait de 120 N au lieu des 180 N prescrits. Apres montage d'une courroie neuve et reglage a 180 N, un essai de 30 minutes a donne une vitesse stable de 0,8 m/s et aucune anomalie de bruit.",
    "On attend identification, chronologie, mesures avec unites et etat final."),
 QT("Expliquer pourquoi un compte rendu doit eviter les termes vagues comme 'ca va mieux' ou 'la machine est réparée'.",
    "Ces formulations ne sont ni mesurables ni vérifiables. 'Ca va mieux' ne dit pas quelle grandeur a évolue ni dans quelle proportion ; 'la machine est réparée' ne precise pas ce qui a ete fait ni si un essai a ete realise. Un compte rendu professionnel leur prefere : 'vibration mesurée a 2,1 mm/s apres equilibrage, seuil d'alerte 4,5 mm/s' ou 'courroie remplacee, essai de 30 minutes sans anomalie'. La precision permet au lecteur de juger de la qualite de l'intervention et facilite le suivi par la GMAO.",
    "On doit montrer le caracter non mesurable des termes vagues et proposer des reformulations chiffrees.")],
C("Le compte rendu transforme une intervention en traceécrite, datée, chiffree et signee, exploitable par le service maintenance.",
  "Fait + mesure + unité + chronologie",
  "Identification · Contexte · Operations · Resultats · Conclusion",
  "Date~Identifie l'intervention~Equipement~Precision de la machine~Symptome~Motif de l'appel~Mesure~Valeur et unité~Signature~Responsabilite engagee",
  "Rassembler les releves et les faits|Rédiger l'identification|Décrire les operations dans l'ordre|Ecrire les resultats chiffres|Conclure, relire et signer",
  "Ecrire d'après la mémoire plusieurs jours apres|Omettre les unités|Utiliser des termes vagues|Signer sans relire",
  "Courroie~Remplacee le 14/03~Tension~120 N avant, 180 N apres~Essai~30 min a 0,8 m/s~Vibration~2,1 mm/s",
  "Impression~Ressenti personnel~Fait~Observation verifiable",
  "Compte rendu~Trace ecrite et signee~Note de service~Consigne collective"))

# ============================================================ FR4
add("FR4", "Registres de langue et vocabulaire technique", "Français",
S("Le registre de langue depend du contexte de communication."
  "|Le registre courant est neutre et constitue le niveau de reference a l'ecrit comme a l'oral."
  "|Le registre soutenu utilise des tournures plus elaborées et un vocabulaire précieux."
  "|Le registre familier est propre a la conversation entre proches."
  "|Le registre technique employe les termes exacts d'un metier ou d'une discipline."
  "|Un terme technique possede generalement un sens plus etroit que son equivalent courant."
  "|Le jargon regroupe les mots et expressions compris seulement par les specialistes."
  "|Un acronyme est forme des initiales de plusieurs mots, comme GMAO."
  "|La definition technique evite la circularite : on ne definit pas un mot par lui-meme."
  "|Un synonyme courant peut aider a vulgariser sans remplacer le terme exact."
  "|Le niveau de langue doit s'adapter a l'interlocuteur : client, collegue ou hierarchy."
  "|Un meme mot peut changer de sens selon le domaine, comme 'portee' en mecanique ou en droit."
  ""),
[QC("Quel registre sert de reference neutre ?", "Familier~Courant~Soutenu~Technique", 1,
     "Le registre courant est le niveau neutre recommande par defaut."),
 QC("Qu'est-ce qu'un acronyme ?", "Un mot inverse~Une formation a partir d'initiales~Un synonyme~Une figure de style", 1,
     "GMAO, par exemple, est forme des initiales de gestion de maintenance assistee par ordinateur."),
 QC("Quel est le risque du jargon ?", "Etre trop clair~Ne pas etre compris par un non-specialiste~Etre trop court~Etre interdit", 1,
     "Le jargon suppose une connaissance partagee du domaine."),
 QC("Comment eviter une definition circulaire ?", "En repetant le mot~En employant des mots plus simples et differents~En ajoutant une image~En utilisant un acronyme", 1,
     "Definir 'usure' par 'usure' n'apporte aucune information."),
 QC("Que faut-il faire face a un client non specialiste ?", "Garder le jargon~Vulgariser sans perdre la precision~Refuser de repondre~Employer le registre familier", 1,
     "On explique le terme technique avec des mots courants, puis on le nomme."),
 QC("Le mot 'portee' a-t-il toujours le meme sens ?", "Oui, toujours~Non, il depend du domaine~Seulement en droit~Seulement en mecanique", 1,
     "Le sens d'un mot se determine par son contexte d'usage."),
 QC("Quel registre correspond a une consigne de securite ecrite ?", "Familier~Technique et courant~Soutenu~Ironique", 1,
     "Une consigne de securite doit etre claire, precise et non ambigue."),
 QT("Expliquer la difference entre registre courant et registre technique, puis donner un exemple avec le mot 'jeu'.",
    "Le registre courant vise la clarte pour tous : 'jeu' y designe un loisir ou une distance faible. Le registre technique donne au mot un sens precise et conventionnel : en mecanique, le jeu est l'espace de deplacement libre entre deux pieces, par exemple un jeu radial de 0,05 mm entre un arbre et son roulement. Le registre technique réduit l'ambiguïte, mais il exige que l'interlocuteur connaisse la convention ; c'est pourquoi on l'accompagne d'une definition ou d'une mesure.",
    "On oppose la portee generale du registre courant au sens precise et souvent chiffre du registre technique."),
 QT("Réécrire en registre courant la phrase : 'Le desalignement du coupleur induit une sollicitation radiale excessive du palier.'",
    "Le coupling est mal aligne ; il exerce une force trop importante sur le palier, ce qui use le roulement plus vite que la normale. La phrase d'origine est exacte mais resume deux mecanismes : le desalignement et la surcharge radiale. La version courte les rend accessibles a un interlocuteur non specialiste tout en conservant l'information essentielle. On peut ensuite ajouter la mesure : 'ecart de 0,6 mm au lieu de 0,1 mm tolere'.",
    "On doit garder le sens technique, simplifier les termes et rester fidel aux faits.")],
C("Le vocabulaire technique précise le sens courant pour éviter l'ambiguïté, mais il doit être expliqué selon l'interlocuteur.",
  "Mot courant + precision technique + unite",
  "Registre courant : neutre · Registre technique : exact · Jargon : reserve aux specialistes",
  "Registre courant~Comprehensible par tous~Registre technique~Sens precise~Jargon~Entre specialistes~Acronyme~Initiales~Unite~Precision de la mesure",
  "Identifier l'interlocuteur|Choisir le niveau de langue|Employer le terme exact|Expliquer le terme si besoin|Verifier la comprehension",
  "Confondre jargon et precision|Supprimer les unites|Employer le registre familier a l'ecrit|Croire qu'un acronyme est compris par tous",
  "Jeu~0,05 mm entre arbre et roulement~Portee~Mesure ou portee d'un arret~GMAO~Gestion de maintenance assistee par ordinateur~Cou coupleur~Organe de liaison de deux arbres",
  "Courant~Clair pour tous~Technique~Precis mais exigeant",
  "Terme exact~Vocabulaire metier~Synonyme courant~Aide a la vulgarisation"))

# ============================================================ MA1
add("MA1", "Proportionnalité, pourcentages et taux de rendement", "Mathématiques",
S("Deux grandeurs sont proportionnelles lorsque leur rapport est constant."
  "|On ecrit alors y = k x, ou k est le coefficient de proportionnalite."
  "|La representation graphique d'une proportionnalite est une droite passant par l'origine.|"
  "Un pourcentage est un rapport rapporte a 100 : 15 % = 15/100 = 0,15."
  "|Augmenter une grandeur de p % revient a la multiplier par 1 + p/100."
  "|La diminuer de p % revient a la multiplier par 1 - p/100."
  "|Le taux de rendement est le rapport entre energie utile et energie fournie."
  "|Un taux de 85 % signifie que 85 parties sur 100 sont utilisees."
  "|Les pourcentages successifs ne s'additionnent pas : 10 % puis 10 % donnent 1,1 x 1,1 = 1,21."
  "|La regle de trois permet de calculer une grandeur manquante dans une situation de proportionnalite."
  "|Dans un devis, la TVA s'applique au prix hors taxes."
  "|Arrondir trop tot introduit une erreur : on garde les decimals jusqu'au resultat final."),
[QC("Quelle est l'equation d'une proportionnalite ?", "y = x + k~y = k x~y = k/x~y = x²", 1,
     "Le rapport y/x est constant et vaut k."),
 QC("A combien correspond 15 % ?", "15~1,5~0,15~0,015", 2,
     "Un pourcentage se divise par 100 : 15/100 = 0,15."),
 QC("Quel facteur multiplie une grandeur apres une hausse de 20 % ?", "0,20~1,20~20~1,02", 1,
     "On multiplie par 1 + 20/100 = 1,20."),
 QC("Un rendement de 85 % signifie que...", "85 J sont perdus~85 parties sur 100 sont utiles~La machine chauffe de 85 °C~Le cout augmente de 85 %", 1,
     "Le rendement rapporte l'energie utile a l'enerie fournie."),
 QC("Combien vaut une hausse de 10 % suivie d'une baisse de 10 % ?", "Retour au depart~Une baisse de 1 %~Une hausse de 1 %~Une baisse de 10 %", 1,
     "1,10 x 0,90 = 0,99, soit une baisse nette de 1 %."),
 QC("Sur quoi s'applique la TVA dans un devis ?", "Sur le prix TTC~Sur le prix HT~Sur la marge uniquement~Sur le cout de la main-d'oeuvre seule", 1,
     "La TVA se calcule sur le prix hors taxes."),
 QC("Pourquoi garder les decimales jusqu'au bout ?", "Pour faire plus long~Pour éviter les erreurs d'arrondi cumulees~Par habitude~Pour impressionner le client", 1,
     "Un arrondi premature modifie le resultat final."),
 QT("Un moteur recoit 4,8 kWh et fournit 3,6 kWh de travail utile. Calculer son rendement et l'exprimer en pourcentage.",
    "Rendement = energie utile / energie fournie = 3,6 / 4,8 = 0,75. Exprime en pourcentage, cela fait 0,75 x 100 = 75 %. Les 25 % restants sont dissipes principalement en chaleur et en pertes mecaniques. On verifie la coherence : le rendement est inferieur a 1, ce qui est toujours le cas pour une machine reelle.",
    "On donne le rapport, le resultat decimal et le pourcentage, avec une verification de coherence."),
 QT("Une piece coute 240 € HT. Appliquer successivement une remise de 10 % puis la TVA de 20 %, et donner le prix TTC.",
    "Apres remise : 240 x (1 - 0,10) = 216 € HT. Applies la TVA de 20 % : 216 x 1,20 = 259,20 € TTC. On peut aussi calculer le montant de TVA : 216 x 0,20 = 43,20 €, puis 216 + 43,20 = 259,20 €. On n'additionne pas les pourcentages : la remise et la TVA s'appliquent sur des bases differentes.",
    "On attend le calcul etape par etape et le resultat TTC exact.")],
C("Proportionnalite et pourcentages permettent de passer du releve au taux : rendement, remise, TVA et taux de panne.",
  "Taux = grandeur rapportee / grandeur de reference",
  "Hausse de p % : x (1 + p/100) · Baisse : x (1 - p/100)",
  "Proportionnalite~Rapport constant~Coefficient~k = y/x~Pourcentage~Rapport sur 100~Rendement~Utile sur fourni~TVA~Taxe sur le prix HT",
  "Identifier les deux grandeurs|Verifier la proportionalite|Ecrire le rapport|Appliquer le facteur|Verifier la coherence du resultat",
  "Additionner deux pourcentages successifs|Appliquer la TVA au prix TTC|Arrondir des le debut|Oublier de multiplier par 100",
  "240 € HT~Remise 10 % -> 216 €~TVA 20 %~43,20 €~Prix TTC~259,20 €~Rendement~3,6/4,8 = 75 %",
  "Hausse de 10 %~Multiplie par 1,10~Baisse de 10 %~Multiplie par 0,90",
  "Rendement~Utile sur fourni~Pertes~Fourni moins utile"))

# ============================================================ MA2
add("MA2", "Équations et fonctions pour modéliser une grandeur", "Mathématiques",
S("Une fonction associe a chaque valeur d'entree une seule valeur de sortie."
  "|Une fonction affine a la forme f(x) = a x + b, avec a le coefficient directeur."
  "|Une fonction lineaire est un cas affine ou b = 0."
  "|Le coefficient directeur represente le taux de variation de la grandeur."
  "|Resoudre une equation, c'est trouver les valeurs de l'inconnue qui la rendent vraie."
  "|Une equation du premier degre a la forme a x + b = 0."
  "|La solution est x = -b/a, a etant non nul."
  "|Une inequation donne un domaine de solutions, souvent un intervalle."
  "|Le graphique d'une fonction affine est une droite ; l'ordonnee a l'origine vaut b."
  "|Les grandeurs physiques doivent etre exprimees dans la meme unite avant calcul."
  "|La modelisation consiste a traduire une situation reelle en relations mathematiques."
  "|Il faut toujours verifier que la solution obtenue est compatible avec la realite."),
[QC("Quelle est la forme d'une fonction affine ?", "f(x)=a/x+b~f(x)=a x+b~f(x)=x²+b~f(x)=a x²", 1,
     "La forme affine est a x + b ; si b vaut zero, on parle de fonction lineaire."),
 QC("Que represente le coefficient a ?", "L'ordonnee a l'origine~Le taux de variation~La solution~L' unite", 1,
     "a mesure la variation de f(x) pour une augmentation de 1 de x."),
 QC("Quelle est la solution de 3x + 6 = 0 ?", "2~-2~6~-6", 1,
     "3x = -6 donc x = -2."),
 QC("Quel est le graphique d'une fonction affine ?", "Une courbe~Une droite~Un cercle~Une parabole", 1,
     "Une fonction affine se represente par une droite."),
 QC("Quelle est l'ordonnee a l'origine de f(x)=2x+5 ?", "2~5~-5~0", 1,
     "Le terme constant b vaut 5, donc la droite coupe l'axe des ordonnees en 5."),
 QC("Une inequation donne...", "Une seule solution~Un ensemble de solutions~Toujours zero~Une droite", 1,
     "Le plus souvent un intervalle de valeurs."),
 QC("Pourquoi verifier la solution ?", "Pour le plaisir~Pour ecarter une valeur physiquement impossible~Pour allonger le devoir~Pour changer d'unite", 1,
     "Une racine negative peut etre inadmissible pour une duree ou une masse."),
 QT("Un capteur delivre une tension U = 0,02 T + 4, ou T est la temperature en degres Celsius. Calculer U pour T = 25 °C et interpreter le coefficient 0,02.",
    "U = 0,02 x 25 + 4 = 0,5 + 4 = 4,5 V. Le coefficient 0,02 represente la sensibilite du capteur : une augmentation de 1 °C de la temperature entraine une augmentation de 0,02 V de la tension, soit 20 mV par degré. Le terme constant 4 V correspond a la tension fournie a 0 °C.",
    "On attend le calcul, l'identification de la sensibilite et de l'ordonnée a l'origine."),
 QT("Resoudre 5x - 15 = 0 puis expliquer pourquoi une solution negativeserait rejetee si x representait une duree de fonctionnement.",
    "5x - 15 = 0 donne 5x = 15, donc x = 3. Si x represente une duree, une valeur negative comme x = -3 n'aurait pas de sens physique : le temps ne peut pas etre negatif dans ce contexte. La modelisation doit donc s'accompagner d'un domaine de definition, ici x >= 0, et toute solution hors de ce domaine est écartee meme si elle satisfait l'equation.",
    "On donne la resolution et on justifie le rejet par le domaine physique de la grandeur.")],
C("Une fonction affine traduit une variation constante ; resoudre une equation revient a chercher la valeur qui annule un ecart.",
  "f(x) = a x + b ; solution de ax+b=0 : x = -b/a",
  "a = pente ou sensibilite · b = valeur a l'origine",
  "Fonction~Associe une seule sortie~Affine~Droite a x+b~Coefficient~Taux de variation~Solution~Valeur qui verifie~Domaine~Valeurs admissibles",
  "Lire l'enonce et identifier les grandeurs|Choisir les unites|Ecrire la relation|Resoudre l'equation|Interpreter et verifier",
  "Mélanger les unites|Oublier le signe de la solution|Ne pas verifier le domaine|Confondre a et b",
  "Capteur~U = 0,02T + 4~A 25 °C~U = 4,5 V~Sensibilite~20 mV par °C~Equation~5x-15=0 -> x=3",
  "Affine~a non nul~Lineaire~b nul, droite passant par l'origine",
  "Equation~Une ou plusieurs values~Inequation~Un intervalle de solutions"))

# ============================================================ MA3
add("MA3", "Statistiques descriptives : moyenne, écart-type, médiane", "Mathématiques",
S("Une serie statistique est un ensemble de valeurs relevees sur une population ou un echantillon."
  "|L'effectif total est la somme des effectifs de chaque valeur."
  "|La moyenne est la somme des valeurs divisee par l'effectif."
  "|La mediane est la valeur qui partage la serie en deux parties egales."
  "|Le mode est la valeur la plus frequente."
  "|L'ecart-type mesure la dispersion des valeurs autour de la moyenne."
  "|Un ecart-type nul signifie que toutes les valeurs sont identiques."
  "|Plus l'ecart-type est grand, plus la serie est etalee."
  "|L'etendue est la difference entre la valeur maximale et la valeur minimale."
  "|La moyenne est sensible aux valeurs aberrantes, contrairement a la mediane."
  "|Un histogramme represente les effectifs par classes de valeurs."
  "|Dans le suivi de maintenance, on compare souvent la moyenne et l'ecart-type de temps entre pannes."
  ""),
[QC("Comment calculer la moyenne ?", "Somme des valeurs divisée par l'effectif~Valeur maximale moins minimale~Valeur centrale~Somme des carres", 0,
     "La moyenne est la somme des valeurs divisée par le nombre de valeurs."),
 QC("Quelle mesure resiste le mieux aux valeurs aberrantes ?", "La moyenne~La mediane~L'ecart-type~L'etendue", 1,
     "La mediane depend du rang central, pas de l'ampleur des extremes."),
 QC("Que mesure l'ecart-type ?", "Le centre de la serie~La dispersion autour de la moyenne~Le nombre de valeurs~La periode", 1,
     "Plus l'ecart-type est grand, plus les valeurs sont etalees."),
 QC("Quel est l'ecart-type d'une serie ou toutes les valeurs sont egales ?", "1~0~La moyenne~L'etendue", 1,
     "Aucune valeur ne s'ecarte de la moyenne, donc l'ecart-type est nul."),
 QC("Comment appelle-t-on la valeur la plus frequente ?", "Le median~Le mode~L'ecart~Le quartile", 1,
     "Le mode est la valeur d'effectif maximal."),
 QC("Quelle est l'etendue d'une serie allant de 12 a 20 ?", "12~16~8~20", 2,
     "L'etendue vaut 20 - 12 = 8."),
 QC("Quelle representation utilise des classes de valeurs ?", "Le camembert~L'histogramme~Le diagramme en barres~La courbe", 1,
     "L'histogramme represente des effectifs par classes contigues."),
 QT("Calculer la moyenne et l'etendue de la serie de temps entre pannes suivante, en heures : 120, 140, 130, 150, 210.",
    "Somme = 120 + 140 + 130 + 150 + 210 = 750 heures. Effectif = 5, donc la moyenne vaut 750 / 5 = 150 heures. L'etendue vaut 210 - 120 = 90 heures. La valeur 210 est nettement superieure aux autres : elle attire la moyenne vers le haut. La mediane, ici 140 heures, decrit mieux le fonctionnement habituel de l'equipement.",
    "On attend le calcul detaille de la moyenne, l'etendue et une remarque sur la valeur aberrante."),
 QT("Expliquer pourquoi un service maintenance suit both la moyenne et l'ecart-type des temps entre pannes.",
    "La moyenne donne le temps de fonctionnement moyen avant panne, utile pour planifier les interventions et estimer la disponibilite. L'ecart-type indique la regularite : un faible ecart-type signifie des pannes previsibles, donc une maintenance preventive bien calibree ; un fort ecart-type signale un comportement erratique, peut-etre lie a des conditions d'utilisation variables ou a un defaut intermittent. Deux equipements peuvent avoir la meme moyenne de 150 heures mais des ecarts-types de 10 et de 60 heures : leur fiabilite est tres differente, et seul le suivi des deux indicateurs le revele.",
    "On doit opposer niveau moyen et regularite, avec un exemple comparatif.")],
C("La moyenne situe le niveau d'une serie, l'ecart-type en mesure la regularite : les deux sont necessaires en fiabilite.",
  "Moyenne = somme / effectif · ET = racine de la variance",
  "Etendue = max - min · mediane = valeur centrale",
  "Moyenne~Niveau moyen~Mediane~Valeur centrale~Mode~Valeur la plus frequente~Ecart-type~Dispersion~Etendue~Max moins min",
  "Rassembler les releves sur une periode|Verifier les unites|Calculer moyenne et dispersion|Repérer les valeurs aberrantes|Comparer a la periode precedente",
  "Moyenner des valeurs d'origines differentes|Ignorer les valeurs aberrantes|Confondre ecart-type et etendue|Oublier l'unite",
  "Serie~120, 140, 130, 150, 210 h~Moyenne~150 h~Etendue~90 h~Mediane~140 h~Ecart~210 hors tendance",
  "Moyenne~Sensible aux extremes~Mediane~Resiste aux extremes",
  "Faible ecart-type~Comportement regulier~Fort ecart-type~Comportement erratique"))

# ============================================================ MA4
add("MA4", "Géométrie, pentes et trigonométrie dans les mesures", "Mathématiques",
S("Le théoreme de Pythagore relie les cotes d'un triangle rectangle : a² + b² = c²."
  "|L'hypotenuse est le cote oppose a l'angle droit, le plus long."
  "|Dans un triangle rectangle, sin(A) = cote oppose / hypoténuse."
  "|cos(A) = cote adjacent / hypoténuse et tan(A) = cote oppose / cote adjacent."
  "|Une pente est le rapport entre la variation verticale et la variation horizontale."
  "|Une pente de 5 % signifie 5 unites verticales pour 100 unites horizontales."
  "|L'angle correspondant verifie tan(alpha) = pente."
  "|Les angles se mesurent en degres ou en radians."
  "|Un cercle de rayon R a pour circonference 2 pi R et pour surface pi R²."
  "|Le volume d'un cylindre de rayon R et de hauteur h vaut pi R² h."
  "|Les conversions d'unites doivent etre faites avant le calcul de superficie ou de volume."
  "|Un resultat geometrique doit etre donne avec son unite, carree ou cubique."),
[QC("Quelle relation donne le theoreme de Pythagore ?", "a+b=c~a²+b²=c²~a×b=c~a²-b²=c", 1,
     "Dans un triangle rectangle, le carre de l'hypotenuse egal la somme des carres des deux autres cotes."),
 QC("Quel cote est l'hypotenuse ?", "Le plus court~Celui oppose a l'angle droit~Celui adjacent a l'angle~La base", 1,
     "L'hypotenuse est toujours opposee a l'angle droit et c'est le cote le plus long."),
 QC("Comment exprimer tan(A) ?", "Oppose / hypoténuse~Oppose / adjacent~Adjacent / hypoténuse~Hypoténuse / oppose", 1,
     "La tangente est le rapport du cote oppose au cote adjacent."),
 QC("Une pente de 5 % correspond a...", "5 m vertical pour 100 m horizontal~5 degres~5 cm au total~5 m horizontal pour 100 m vertical", 0,
     "La pente en pourcentage rapporte la montee a la distance horizontale."),
 QC("Quelle est la circonference d'un cercle de rayon R ?", "pi R~2 pi R~pi R²~2 pi R²", 1,
     "La circonference vaut 2 pi R ; pi R² est l'aire."),
 QC("Quelle est l'unite d'un volume ?", "Le metre~Le metre carre~Le metre cube~Le degré", 2,
     "Un volume s'exprime en unite cubique, par exemple m³."),
 QC("Quand faut-il convertir les unites ?", "Apres le calcul~Avant le calcul~Jamais~Uniquement pour les angles", 1,
     "Des unites homogenes sont necessaires des le depart."),
 QT("Une rampe de 6 m de long s'eleve de 0,9 m. Calculer l'angle alpha de la pente et le taux en pourcentage.",
    "La longueur de 6 m est l'hypotenuse et la hauteur de 0,9 m est le cote oppose a l'angle alpha. On a donc sin(alpha) = 0,9 / 6 = 0,15, d'ou alpha = arcsin(0,15) environ 8,6 degres. Le taux de pente se calcule avec la distance horizontale : d = racine carree de (6² - 0,9²) = racine carree de 35,19, soit environ 5,93 m. Le taux vaut 0,9 / 5,93 = 0,152, soit environ 15,2 %. Pour une petite pente, on peut approximer par 0,9/6 = 15 %.",
    "On identifie les cotes du triangle, on calcule l'angle, puis la distance horizontale avant le taux."),
 QT("Calculer le volume d'un reservoir cylindrique de 1,2 m de rayon et 2,5 m de hauteur, puis le convertir en litres.",
    "V = pi R² h = pi x (1,2)² x 2,5 = pi x 1,44 x 2,5 = 3,6 pi, soit environ 11,31 m³. Comme 1 m³ = 1000 L, la capacite est d'environ 11 310 litres. On arrondit au litre pres compte tenu de la precision des mesures de rayon et de hauteur. Ce volume sert par exemple a estimer la quantite d'huile necessaire lors d'une vidange complete.",
    "On applique la formule, on convertit en litres et on donne un resultat arrondi de maniere coherente.")],
C("Pythagore et la trigonometrie transforment les mesures de terrain en angles, pentes et volumes exploitables.",
  "a²+b²=c² · sin = oppose/hypoténuse · tan = oppose/adjacent",
  "Pente % = montee / distance horizontale x 100",
  "Pythagore~Triangle rectangle~Hypoténuse~Cote oppose a l'angle droit~Sinus~Oppose sur hypoténuse~Tangente~Oppose sur adjacent~Volume cylindre~pi R² h",
  "Dessiner la figure et nommer les cotes|Convertir toutes les unites|Choisir la relation adaptee|Calculer l'angle ou la longueur|Verifier l'ordre de grandeur",
  "Utiliser la pente au lieu de l'angle dans sin|Oublier de convertir les unites|Confondre aire et circonference|Donner un volume en metres",
  "Rampe~6 m de long, 0,9 m de haut~Angle~Environ 8,6 degres~Taux~Environ 15,2 %~Reservoir~1,2 m x 2,5 m~Volume~Environ 11,3 m³",
  "Sinus~Oppose sur hypoténuse~Cosinus~Adjacent sur hypoténuse",
  "Pente en pourcentage~Rapport montee sur horizontal~Pente en degree~Angle alpha"))

# ============================================================ PC1
add("PC1", "Loi d'Ohm, puissance et énergie électrique", "Physique-Chimie",
S("Le courant electrique est un deplacement de charges dans un conducteur."
  "|L'intensite I se mesure en amperes avec un ampèremetre place en serie."
  "|La tension U se mesure en volts avec un voltmetre place en derivation."
  "|La loi d'Ohm s'ecrit U = R I pour un conducteur ohmique a temperature constante."
  ""
  "|Dans un circuit en serie, l'intensite est la meme en tout point."
  "|Dans un circuit en parallele, la tension est la meme aux bornes de chaque branche."
  "|La puissance electrique absorbee vaut P = U I."
  "|L'energie consommee vaut W = P t, avec t en secondes."
  "|Le kilowattheure vaut 3,6 millions de joules."
  "|Une resistance qui dissipe trop de puissance chauffe et peut etre detruite."
  "|Un court-circuit presente une tres faible resistance et une intensite elevee."
  "|Le disjoncteur protege les conducteurs contre les surintensites."),
[QC("Comment brancher un ampèremetre ?", "En derivation~En serie~Aux bornes du generateur~N'importe comment", 1,
     "L'ampèremetre s'insere dans la boucle pour mesurer le courant qui le traverse."),
 QC("Quelle est la loi d'Ohm ?", "U = R/I~U = R I~U = I/R~U = R + I", 1,
     "Pour un conducteur ohmique, la tension est proportionnelle a l'intensite."),
 QC("Dans un circuit en serie, quelle grandeur est identique partout ?", "La tension~L'intensite~La puissance~La resistance", 1,
     "L'intensite est la meme en tout point d'une branche serie."),
 QC("Quelle est l'unite de puissance ?", "Le joule~Le watt~L'ampere~Le volt", 1,
     "La puissance se mesure en watts ; le joule est l'unite d'energie."),
 QC("Combien de joules vaut 1 kWh ?", "1000~3600~3 600 000~1 000 000", 2,
     "1 kWh = 1000 W x 3600 s = 3,6 x 10⁶ J."),
 QC("Que se passe-t-il lors d'un court-circuit ?", "L'intensite devient tres faible~La resistance devient tres faible et l'intensite elevee~La tension devient nulle~Le courant s'arrete", 1,
     "La forte intensite provoque un echauffement dangereux."),
 QC("Quel appareil protege contre les surintensites ?", "Le voltmetre~Le disjoncteur~Le transformateur~Le condensateur", 1,
     "Le disjoncteur coupe le circuit en cas de surcharge ou de court-circuit."),
 QT("Un moteur est alimente sous 230 V et absorbe 4 A. Calculer sa puissance absorbee, puis l'energie consommee en 2 heures.",
    "P = U I = 230 x 4 = 920 W. L'energie consommee en 2 heures vaut W = P t = 0,920 kW x 2 h = 1,84 kWh. En joules : 1,84 x 3 600 000 = 6,624 x 10⁶ J. A titre de verification, on peut aussi calculer 920 W x 7200 s = 6 624 000 J, soit le meme resultat.",
    "On attend P=UI, la conversion en kWh et l'equivalence en joules."),
 QT("Expliquer pourquoi un conducteur de faible section peut chauffer lorsqu'il est traverse par un courant important.",
    "Tout conducteur possede une resistance. La puissance dissipee par effet Joule vaut P = R I² : elle croit comme le carre de l'intensite. Si la section est faible, la resistance est plus elevee, et la dissipation de chaleur augmente encore. Pour un courant de 16 A dans une resistance de 0,5 ohm, la puissance dissipee atteint 16² x 0,5 = 128 W, ce qui peut porter le conducteur a une temperature dangereuse. C'est pourquoi le dimensionnement de la section et le choix du disjoncteur sont lies.",
    "On doit citer P = R I², le role de la section et le lien avec la protection.")],
C("Tension, intensite et resistance sont lies par U = R I ; la puissance et l'energie se deduisent pour dimensionner et proteger.",
  "U = R I · P = U I = R I² · W = P t",
  "1 kWh = 3,6 x 10⁶ J · serie : I constant · parallele : U constant",
  "Tension~Difference de potentiel~Intensite~Debit de charges~Resistance~Opposition au courant~Puissance~P = U I~Energie~W = P t",
  "Verifier l'alimentation et les mesures|Choisir le montage serie ou parallele|Appliquer la loi d'Ohm|Calculer puissance et energie|Verifier le dimensionnement",
  "Brancher l'ampèremetre en parallele|Oublier de convertir les heures en secondes|Confondre puissance et energie|Negliger l'effet Joule",
  "Moteur~230 V et 4 A~Puissance~920 W~Energie~1,84 kWh en 2 h~Court-circuit~Fort courant~Disjoncteur~Protection",
  "Serie~Meme intensite~Parallele~Meme tension",
  "Puissance~Energie par seconde~Energie~Puissance multipliee par le temps"))

# ============================================================ PC2
add("PC2", "Forces, travail et puissance mécanique", "Physique-Chimie",
S("Une force est une action mecanique caracterisee par son point d'application, sa direction, son sens et son intensite."
  "|L'intensite d'une force se mesure en newtons."
  "|Le poids d'un corps vaut P = m g, avec g environ 9,81 N/kg sur Terre."
  "|La masse s'exprime en kilogrammes, le poids en newtons."
  "|Deux forces s'equilibrent si leur somme vectorielle est nulle."
  "|Le travail d'une force vaut W = F d cos(alpha), avec d le deplacement."
  "|Le travail est nul si la force est perpendiculaire au deplacement."
  "|L'unite de travail est le joule."
  "|La puissance mecanique est le travail effectue par unite de temps : P = W/t."
  "|En rotation, la puissance vaut P = couples x vitesse angulaire."
  "|Le rendement d'une machine est le rapport entre puissance utile et puissance fournie."
  "|Les frottements transforment une partie de l'energie en chaleur."
  ""),
[QC("Quelle est l'unite d'une force ?", "Le kilogramme~Le newton~Le joule~Le watt", 1,
     "L'intensite d'une force se mesure en newtons."),
 QC("Quel est le poids d'une masse de 10 kg ?", "10 N~98,1 N~981 N~1 N", 1,
     "P = m g = 10 x 9,81 = 98,1 N."),
 QC("Quand le travail d'une force est-il nul ?", "Quand la force est grande~Quand la force est perpendiculaire au deplacement~Quand la distance est grande~Quand la force est verticale", 1,
     "cos(90°) = 0, donc W = 0 : la force ne fournit aucun travail."),
 QC("Quelle est l'unite du travail ?", "Le newton~Le joule~Le watt~Le pascal", 1,
     "Un joule correspond a un newton applique sur un metre."),
 QC("Comment calculer une puissance ?", "P = W t~P = W/t~P = F/t~P = t/W", 1,
     "La puissance est le rapport du travail a la duree."),
 QC("Que represente un rendement de 80 % ?", "80 % de la puissance est perdue~80 % de la puissance fournie est utile~La machine chauffe a 80 °C~Le couple vaut 80 N", 1,
     "Le rendement rapporte la puissance utile a la puissance fournie."),
 QC("Que devient l'energie perdue par frottements ?", "Elle disparait~Elle se transforme en chaleur~Elle devient du courant~Elle augmente la masse", 1,
     "L'energie se conserve mais change de forme, souvent en chaleur."),
 QT("Un ouvrier souleve une caisse de 25 kg de 1,8 m en 3 s. Calculer le travail fourni et la puissance developpee.",
    "La force a vaincre est le poids de la caisse : F = m g = 25 x 9,81 = 245,25 N. Le travail vaut W = F d = 245,25 x 1,8 = 441,45 J. La puissance est P = W/t = 441,45 / 3 = 147,15 W, soit environ 147 W. Ce resultat correspond a la puissance utile ; la puissance muscles developpee est superieure a cause du rendement du corps humain.",
    "On calcule le poids, puis le travail, puis la puissance avec les unites."),
 QT("Un moteur fournit un couple de 20 N.m a 1500 tours/min. Calculer sa puissance utile, sachant que la vitesse angulaire en rad/s vaut 2 pi n/60.",
    "La vitesse angulaire vaut omega = 2 pi x 1500 / 60 = 50 pi, soit environ 157 rad/s. La puissance utile est P = couple x omega = 20 x 157 = 3140 W, soit environ 3,14 kW. Si le rendement global du groupe est de 0,85, la puissance electrique absorbee vaut 3,14 / 0,85, soit environ 3,7 kW. Ce dimensionnement permet de choisir un moteur et un variateur adaptes.",
    "On convertit la vitesse en rad/s, on calcule P, puis on deduit la puissance absorbee avec le rendement.")],
C("Le travail mesure l'energie transferee par une force ; la puissance en donne le debit, grandeur decisive pour choisir un moteur.",
  "W = F d cos(alpha) · P = W/t",
  "Poids = m g · rotation : P = couple x omega",
  "Force~Action mecanique~Poids~m fois g~Travail~Fois d~Puissance~Travail sur temps~Rendement~Utile sur fourni",
  "Identifier les forces et le deplacement|Convertir les unites|Calculer le travail|Diviser par la duree|Comparer a la puissance disponible",
  "Confondre masse et poids|Omettre cos(alpha)|Utiliser les tours/min au lieu de rad/s|Negliger le rendement",
  "Caisse 25 kg~Poids 245 N~Hausse 1,8 m~Travail 441 J~Duree 3 s~Puissance 147 W~Moteur~3,14 kW utiles",
  "Travail~Energie transferee~Puissance~Debit d'energie",
  "Masse~En kg~Poids~En newtons"))

# ============================================================ PC3
add("PC3", "Température, chaleur et rendement thermique", "Physique-Chimie",
S("La temperature mesure l'agitation thermique des particules ; elle s'exprime en degres Celsius ou en kelvins."
  "|La relation entre les deux echelles est T(K) = t(°C) + 273,15."
  "|La chaleur est un transfert d'energie du corps le plus chaud vers le plus froid."
  "|La quantite de chaleur recue par un corps vaut Q = m c delta T."
  "|La capacite thermique massique c depend de la matiere, par exemple 4186 J/(kg.K) pour l'eau."
  "|Les transferts thermiques se font par conduction, convection et rayonnement."
  "|La conduction domine dans les solides, la convection dans les fluides en mouvement."
  "|Le rayonnement peut se propager sans milieu material."
  "|L'isolation thermique reduit les pertes par conduction et convection."
  "|Le rendement thermique est le rapport entre chaleur utile et energie consommee."
  "|Une machine en surchauffe voit ses pertes augmenter et sa fiabilite diminuer."
  "|Les dilatations thermiques doivent etre prises en compte dans les assemblages mecaniques."),
[QC("Quelle est la relation Celsius / kelvin ?", "T = t - 273~T = t + 273,15~T = 2t~T = t x 273", 1,
     "Le zero absolu correspond a -273,15 °C."),
 QC("Quelle est l'unite de capacite thermique massique ?", "J/(kg.K)~J/kg~W/K~kJ uniquement", 0,
     "Elle rapporte une energie a une masse et a une variation de temperature."),
 QC("Quel mode de transfert domine dans un solide ?", "La convection~La conduction~Le rayonnement~L'evaporation", 1,
     "Les solides conduisent la chaleur par contact entre particules."),
 QC("Quel transfert ne necessite pas de milieu ?", "La conduction~La convection~Le rayonnement~Le contact", 2,
     "Le rayonnement electromagnetique se propage dans le vide."),
 QC("Que represente Q = m c delta T ?", "Une puissance~Une quantite de chaleur~Une temperature~Un rendement", 1,
     "Cette formule donne l'energie thermique echangee."),
 QC("Comment reduire les pertes par convection ?", "En augmentant la ventilation~En isolant~En chauffant davantage~En changeant de couleur", 1,
     "L'isolation limite les echanges avec l'environnement."),
 QC("Quel est l'effet d'une surchauffe sur une machine ?", "Elle ameliore le rendement~Elle augmente les pertes et use les composants~Elle n'a aucun effet~Elle reduit la consommation", 1,
     "La surchauffe accelere le vieillissement des isolants et des lubrifiants."),
 QT("Calculer la chaleur necessaire pour porter 50 kg d'eau de 20 °C a 80 °C. On prendra c = 4186 J/(kg.K).",
    "La variation de temperature vaut delta T = 80 - 20 = 60 K. La quantite de chaleur est Q = m c delta T = 50 x 4186 x 60 = 12 558 000 J, soit environ 12,6 MJ. En kWh, cela represente 12,558 / 3,6, soit environ 3,49 kWh. Si le chauffe-eau a un rendement de 0,90, l'energie electrique consommee est d'environ 3,88 kWh.",
    "On calcule delta T, puis Q, puis on peut en deduire l'energie consommee selon le rendement."),
 QT("Expliquer pourquoi un moteur electrique doit être refroidi et citer trois modes de transfert thermique mis en jeu.",
    "Les pertes electriques et mecaniques se transforment en chaleur : si cette chaleur n'est pas evacuee, la temperature des enroulements monte, l'isolant vieillit et le moteur peut griller. Le refroidissement met en jeu la conduction de la chaleur des enroulements vers le carter, la convection forcee par le ventilateur ou l'air ambiant, et le rayonnement du carter vers l'environnement. Les ailettes augmentent la surface d'echange et ameliorent la convection. Une ventilation obstruee ou un filtre colmate est donc une cause classique de surchauffe.",
    "On relie les pertes a la surchauffe, puis on nomme conduction, convection et rayonnement.")],
C("La chaleur est un transfert d'energie : la maitriser passe par le calcul de Q, l'isolation et le controle des surchauffes.",
  "Q = m c delta T · T(K) = t(°C) + 273,15",
  "Conduction · convection · rayonnement",
  "Temperature~Etat thermique~Chaleur~Transfert d'energie~Capacite massique~Propriete du materiau~Conduction~Dans les solides~Rayonnement~Sans milieu",
  "Mesurer les temperatures|Choisir la capacite massique|Calculer la chaleur|Identifier les modes de transfert|Verifier le refroidissement",
  "Confondre temperature et chaleur|Oublier la conversion en kelvins|Negliger les pertes|Ignorer l'effet des ailettes",
  "Eau 50 kg~20 a 80 °C~Delta T~60 K~Chaleur~12,6 MJ~Rendement 0,90~3,88 kWh consommes",
  "Temperature~Degre d'agitation~Chaleur~Energie transferee",
  "Conduction~Contact direct~Convection~Mouvement du fluide"))

# ============================================================ PC4
add("PC4", "Solutions aqueuses, pH et corrosion des métaux", "Physique-Chimie",
S("Une solution est un melange homogene d'un solvant et d'un ou several solutes."
  "|La concentration molaire C s'exprime en moles par litre."
  "|Le nombre de moles n se calcule avec la masse molaire M : n = m/M."
  "|Une dilution conserve le nombre de moles : C1 V1 = C2 V2."
  "|Le pH mesure l'acidite d'une solution : pH = -log[H+]."
  "|Une solution est acide si son pH est inferieur a 7, basique s'il est superieur a 7."
  "|Une solution neutre a un pH voisin de 7 a 25 °C."
  "|Chaque unite de pH correspond a un facteur 10 sur la concentration en ions H+."
  "|La corrosion est une degradation chimique ou electrochimique d'un materiau."
  "|La rouille du fer est une oxydation favorisee par l'eau et l'oxygene."
  "|La protection peut etre passive, comme une peinture, ou active, comme une anode sacrificielle."
  ""
  "|Le controle du pH et de la conductivite fait partie de la maintenance des circuits d'eau."),
[QC("Quelle est l'unite de concentration molaire ?", "Le gramme~La mole par litre~Le litre~Le newton", 1,
     "La concentration molaire s'exprime en mol/L."),
 QC("Quelle relation donne le nombre de moles ?", "n = M/m~n = m/M~n = m M~n = M + m", 1,
     "Le nombre de moles est la masse divisée par la masse molaire."),
 QC("Que signifie pH = 3 ?", "Une solution basique~Une solution acide~Une solution neutre~Une concentration nulle", 1,
     "Un pH inferieur a 7 caracterise une solution acide."),
 QC("De combien la concentration en H+ change-t-elle entre pH 3 et pH 5 ?", "Un facteur 2~Un facteur 100~Un facteur 10~Aucun changement", 1,
     "Deux unites de pH representent un facteur 10² = 100."),
 QC("Comment s'appelle la dilution qui conserve les moles ?", "C1V1 = C2V2~P = UI~U = RI~Q = mcT", 0,
     "Le produit concentration par volume reste constant lors d'une dilution."),
 QC("Quel facteur accelere la corrosion du fer ?", "L'absence d'eau~La presence d'eau et d'oxygene~Une temperature basse~Une peinture intacte", 1,
     "L'eau et l'oxygene sont les reactifs de la formation de la rouille."),
 QC("Quelle protection est une anode sacrificielle ?", "Une protection passive~Une protection active~Une peinture~Un vernis", 1,
     "L'anode sacrificielle se corrode a la place de la piece protegee."),
 QT("Une solution acide a un pH de 2. Quelle sera la concentration en ions H+ apres dilution 100 fois ? Quel sera le nouveau pH ?",
    "Un pH de 2 correspond a une concentration en ions H+ de 10⁻² mol/L, soit 0,01 mol/L. Apres une dilution 100 fois, la concentration devient 0,01 / 100 = 10⁻⁴ mol/L. Le nouveau pH vaut alors -log(10⁻⁴) = 4. On retrouve la regle pratique : diluer 100 fois augmente le pH de 2 unites pour un acide fort.",
    "On passe par la concentration en ions H+ puis on recalcule le pH."),
 QT("Expliquer pourquoi un circuit de refroidissement industriel necessite un suivi du pH et de la conductivite.",
    "Un pH trop acide attaque les metaux et peut provoquer des fuites, tandis qu'un pH trop eleve favorise les depots de calcaire qui reduisent les echanges thermiques et perturbent la circulation. La conductivite,elle, traduit la quantite de sels dissous : une augmentation signale une pollution, une evaporation excessive ou un apport d'eau de mauvaise qualite. Le suivi de ces deux parametres permet d'ajuster le traitement chimique, de programmer les purges et de prevenir la corrosion comme l'entartrage, deux causes frequentes de pannes de refroidissement.",
    "On relie pH a corrosion ou entartrage et conductivite a la qualite de l'eau.")],
C("Le pH et la conductivite sont des indicateurs de l'etat chimique d'un circuit : leur derive annonce corrosion ou entartrage.",
  "[H+] = 10^-pH · C1 V1 = C2 V2",
  "pH < 7 acide · pH = 7 neutre · pH > 7 basique",
  "Concentration~Moles par litre~pH~Acidite~Dilution~C1V1 = C2V2~Corrosion~Oxydation~Anode sacrificielle~Protection active",
  "Prelever un echantillon|Mesurer pH et conductivite|Comparer aux valeurs de consigne|Diagnostiquer la derive|Traiter et renouveler le bain",
  "Additionner les pH|Oublier que l'echelle est logarithmique|Confondre corrosion et entartrage|Ne pas noter la temperature de mesure",
  "pH 2~0,01 mol/L de H+~Dilution 100~0,0001 mol/L~Nouveau pH~4~Routille~Oxydation du fer",
  "Corrosion~Destruction du metal~Entartrage~Depot de calcaire",
  "Peinture~Protection passive~Anode sacrificielle~Protection active"))

# ============================================================ HG1
add("HG1", "Révolution industrielle et mutations du travail", "Histoire-Géographie",
S("La revolution industrielle designe la transition d'une economie agraire vers une economie industrielle."
  "|Elle debute en Grande-Bretagne au XVIIIe siecle avant de s'etendre a l'Europe et au monde."
  "|La machine a vapeur est l'une des innovations decisives du XIXe siecle."
  "|Le developpement des usines transforme les modes de production et l'organisation du travail."
  "|La division du travail accroit la productivite mais rend l'ouvrier dependant d'une tache repetee."
  "|L'exode rural fournit une main-d'oeuvre abondante aux villes industrielles."
  "|Les conditions de travail au XIXe siecle sont souvent difficiles : longues journees et faibles salaires."
  "|Les syndicats et les greves apparaissent pour defendre les interets des travailleurs."
  ""
  "|Le taylorisme, au debut du XXe siecle, recherche l'optimisation des gestes et des temps."
  "|Le fordisme ajoute la production en serie et le salaire permettant d'acheter le produit."
  "|L'automatisation et la robotique constituent une nouvelle etape de cette mutation."
  "|Ces transformations expliquent l'importance actuelle de la formation et de la maintenance industrielle."),
[QC("Ou debute la revolution industrielle ?", "En France au XVIe siecle~En Grande-Bretagne au XVIIIe siecle~Aux Etats-Unis au XXe siecle~En Chine au XIXe siecle", 1,
     "La Grande-Bretagne est le premier pays a connaitre l'industrialisation."),
 QC("Quelle invention est symbolique de cette periode ?", "La machine a vapeur~L'imprimerie~Le telephone~L'avion", 0,
     "La machine a vapeur alimente les usines et les transports au XIXe siecle."),
 QC("Quel est un effet de la division du travail ?", "Moins de productivite~Plus de productivite mais plus de repetition~La fin des usines~La disparition des salaires", 1,
     "La specialisation augmente le rendement mais peut rendre la tache monotone."),
 QC("Quel phenomene accompagne la croissance des usines ?", "L'exode rural~Le retour a la campagne~La baisse des villes~La fin du commerce", 0,
     "Les paysans quittent les campagnes pour travailler en usine."),
 QC("Quel est le role des syndicats ?", "Defendre les interets des travailleurs~Diriger les usines~Fixer les prix~Remplacer l'Etat", 0,
     "Les syndicats negocient les conditions de travail et les salaires."),
 QC("Que recherche le taylorisme ?", "L'optimisation des gestes et des temps~La reduction de la production~Le travail artisanal~La suppression des machines", 0,
     "Le taylorisme repose sur l'etude scientifique du travail."),
 QC("Quel lien avec la maintenance aujourd'hui ?", "Aucun~Les machines complexes exigent des competences de maintenance~La maintenance a disparu~Les usines n'utilisent plus de machines", 1,
     "L'automatisation accroit le besoin de techniciens qualifes."),
 QT("Expliquer en quoi la revolution industrielle a transforme a la fois le travail et la societe.",
    "Elle a deplace la production de l'atelier artisanal vers l'usine, impose la division du travail et la discipline des horaires, et rendu le salariat dominant. Elle a provoque un exode rural, une croissance rapide des villes et l'emergence d'une classe ouvrieres. Les difficultes de travail ont entraine des luttes syndicales et des lois sociales. Enfin, elle a installe une logique de productivite et d'innovation technique qui se prolonge aujourd'hui dans l'automatisation et la maintenance industrielle.",
    "On attend les transformations du travail, les effets sociaux et les continuites jusqu'aujourd'hui."),
 QT("Montrer comment le taylorisme et le fordisme ont prepare la production industrielle moderne.",
    "Le taylorisme a analyse les gestes et les temps pour reduire les gaspillages et separer la conception de l'execution. Le fordisme y a ajoute la chaine de montage, la standardisation des pieces et des salaires suffisants pour que les ouvriers deviennent consommateurs. Cette organisation a permis une production de masse a cout reduit. Elle exige toutefois des machines fiables et disponibles en permanence : c'est la que naissent les fonctions de maintenance preventive et de diagnostic, devenues essentielles dans les usines modernes.",
    "On definit les deux systemes et on etablit le lien avec le besoin de maintenance.")],
C("La revolution industrielle a remplace l'atelier par l'usine et rendu la machine centrale : le travail devient salarie, divise et regulé.",
  "Innovation + usine + salariat + villes",
  "XVIIIe siecle : machine a vapeur · XIXe : usines et syndicats · XXe : taylorisme et fordisme",
  "Machine a vapeur~Innovation decisive~Exode rural~Main-d'oeuvre vers la ville~Taylorisme~Optimisation des gestes~Fordisme~Production en serie~Syndicat~Defense des salaries",
  "Situer la periode|Identifier les innovations|Analyser les effets sur le travail|Observer les reactions sociales|Relier au present",
  "Confondre les siecles|Reduire l'histoire aux machines|Oublier les conditions de travail|Ignorer les luttes sociales",
  "1780~Debut de l'industrialisation~XIXe~Croissance des usines~1911~Taylor publie ses principes~Ford~Chaine de montage~Aujourd'hui~Robotique et maintenance",
  "Artisanat~Savoir faire complet~Usine~Travail divise et salarie",
  "Taylorisme~Gestes et temps~Fordisme~Serie et salaire"))

# ============================================================ HG2
add("HG2", "Le monde du travail au XXe siècle : luttes et conquêtes sociales", "Histoire-Géographie",
S("Le XXe siecle voit la generalisation du salariat et la croissance des grands groupes industriels."
  "|La Premiere Guerre mondiale entraine une mobilisation economique et une forte presence de l'Etat."
  "|La crise de 1929 provoque une montée du chomage et des protections sociales."
  "|Le Front populaire, en 1936, institue les conges payes et la semaine de 40 heures."
  ""
  "|Les Trente Glorieuses, de 1945 a 1975, sont marquees par une forte productivite et la hausse des salaires."
  "|Les syndicats obtiennent des conventions collectives et une representation du personnel."
  "|Le comite d'entreprise, cree en 1945, donne des droits collectifs aux salaries."
  "|Les crises petrolieres de 1973 et 1979 mettent fin a la croissance rapide."
  "|La desindustrialisation touche certaines regions a partir des annees 1970."
  "|Les annees 1980 et 1990 voient l'automatisation et la mondialisation des echanges."
  "|Le droit du travail actuel porte la trace de ces conquetes : duree du travail, repos, securite."
  "|La formation professionnelle devient un reponse aux mutations des competences."),
[QC("Quelle mesure est associee au Front populaire ?", "La semaine de 35 heures~Les conges payes~Le SMIC~Le comite d'entreprise", 1,
     "L'accord de 1936 institue deux semaines de conges payes et la semaine de 40 heures."),
 QC("Comment appelle-t-on la periode 1945-1975 ?", "Les Trente Glorieuses~La Grande Depression~La Reconstruction lente~Les Annees noires", 0,
     "Cette periode est celle d'une croissance economique exceptionnelle."),
 QC("Quel evenement marque la fin des Trente Glorieuses ?", "La crise petroliere de 1973~La Premiere Guerre mondiale~Le Front populaire~La Revolution industrielle", 0,
     "Le choc petrolier de 1973 ouvre une periode de ralentissement et de chomage."),
 QC("Quel role joue le comite d'entreprise ?", "Representer les salaries~Diriger la production~Fixer les prix~Remplacer le syndicat", 0,
     "Le CSE, successeur du comite d'entreprise, represente les salaries."),
 QC("Quel effet a la mondialisation sur les entreprises ?", "Moins de concurrence~Une concurrence accrue et des delocalisations~La fin des usines~La disparition du salariat", 1,
     "L'ouverture des echanges accroit la concurrence et peut entrainer des delocalisations."),
 QC("Quelle consequence de la crise de 1929 ?", "Une baisse du chomage~Une montée du chomage et des protections~Plus de croissance~La fin des syndicats", 1,
     "La crise entraine une forte hausse du chomage et des politiques de protection."),
 QC("Pourquoi la formation professionnelle est-elle importante ?", "Elle remplace le salaire~Elle permet de s'adapter aux mutations des competences~Elle supprime le chomage~Elle est facultative", 1,
     "Les evolutions techniques exigent une mise a jour reguliere des competences."),
 QT("Raconter les principales etapes de l'evolution du salariat en France du Front populaire aux Trente Glorieuses.",
    "En 1936, le Front populaire obtient les conges payes et la semaine de 40 heures, ce qui reconnait le droit au repos. Pendant la Seconde Guerre mondiale, l'economie est mobilisee et l'Etat intervient davantage. La Liberation est suivie de la mise en place de la securite sociale et du comite d'entreprise en 1945. Les Trente Glorieuses apportent la hausse des salaires, la generalisation des avantages sociaux et une forte croissance de la productivite. Le salariat devient la situation dominante, avec des droits collectifs reconnus par la loi et les conventions collectives.",
    "On attend une chronologie claire et l'evocation des droits acquis."),
 QT("Expliquer pourquoi la fin des Trente Glorieuses a rendu la maintenance et la formation plus strategiques.",
    "Apres 1973, la croissance ralentit, le cout de l'energie augmente et la concurrence internationale s'intensifie. Les entreprises ne peuvent plus compenser les gaspillages par une croissance facile : elles doivent reduire les couts, allonger la duree de vie des equipements et eviter les arrets de production. La maintenance preventive et le suivi des performances deviennent alors des leviers de competitivite. En parallele, l'automatisation modifie les competences demandees : les techniciens doivent savoir diagnostiquer, lire des schemas et utiliser des outils numeriques, ce qui rend la formation professionnelle continue indispensable.",
    "On relie la crise economique a la recherche de productivite, puis aux besoins de competences.")],
C("Le droit social francais est le resultat de luttes et de crises : chaque periode a laisse des acquis qui encadrent aujourd'hui le travail.",
  "Contexte economique + mobilisation sociale + loi",
  "1936 conges payes · 1945 securite sociale · 1945-1975 croissance · 1973 crise",
  "Front populaire~Conges payes 1936~Trente Glorieuses~Croissance 1945-1975~Crise 1973~Fin de la croissance~Comite d'entreprise~Representation~Chomage~Effet des crises",
  "Placer les evenements dans le temps|Relier economie et societe|Identifier les acteurs|Nommer les acquis sociaux|Relier a la situation actuelle",
  "Confondre 1936 et 1945|Ignorer le role des crises|Croire que les droits sont permanents|Oublier les syndicats",
  "1936~Conges payes et 40 h~1945~Securite sociale~1973~Choc petrolier~1980-1990~Automatisation~Aujourd'hui~CSE et formation",
  "Croissance~Hausse des salaires~Crise~Chomage et rigueur",
  "Syndicat~Negocie les droits~Etat~Legifere et protege"))

# ============================================================ HG3
add("HG3", "L'usine, la ville et les territoires industriels", "Histoire-Géographie",
S("Un territoire industriel est un espace ou les activites de production structures l'economie locale."
  "|La localisation d'une usine depend des transports, de l'energie, de la main-d'oeuvre et du marche."
  "|Les grandes usines se sont souvent installees pres des voies ferrees, des canaux ou des ports."
  "|L'industrie a façonne des villes entieres, comme les cites ouvrieres."
  "|La concentration industrielle produit des avantages d'agglomeration : main-d'oeuvre, fournisseurs, infrastructures."
  "|Elle entraine aussi des contraintes : pollution, congestion et dependance a un seul employeur."
  "|La desindustrialisation a touché les regions specialisees dans la metallurgie, le textile ou la mine."
  "|Elle se traduit par des fermetures d'usines, du chomage et un declin demographique local."
  "|La reconversion industrielle passe par la diversification et la formation aux nouveaux metiers."
  "|Les zones d'activite et les parcs industriels regroupent aujourd'hui des entreprises plus petites."
  "|La maintenance industrielle est un emploi present dans presque tous les territoires ou l'on produit."
  "|Les transitions energetique et numerique redessinent la carte des activites."
  ""),
[QC("Quel facteur n'influe pas sur la localisation d'une usine ?", "Les transports~L'energie~La couleur des batiments~La main-d'oeuvre", 2,
     "Les transports, l'energie et la main-d'oeuvre sont des criteres de localisation."),
 QC("Qu'appelle-t-on cite ouvrieres ?", "Un quartier residentiel sans usine~Un ensemble de logements construits pour les ouvriers~Une usine automatisee~Un port", 1,
     "Les cites ouvrieres logeaient les travailleurs pres de leur usine."),
 QC("Quel est un avantage de l'agglomeration industrielle ?", "Moins de fournisseurs~Un reservoirs de competences et de fournisseurs~Plus de pollution uniquement~La disparition des transports", 1,
     "La proximite facilite les echanges et le recrutement."),
 QC("Quelle est une consequence de la desindustrialisation ?", "Une hausse de l'emploi industriel~Des fermetures et du chomage local~Plus d'usines~Une baisse du chomage", 1,
     "La fermeture d'un site entraine des pertes d'emplois et un appauvrissement local."),
 QC("Que signifie reconversion industrielle ?", "Fermer definitivement un site~Diversifier les activites et former aux nouveaux metiers~Augmenter les heures de travail~Supprimer la formation", 1,
     "La reconversion vise a replacing les activites disparues par de nouvelles."),
 QC("Quel secteur est present dans presque tous les territoires de production ?", "La maintenance industrielle~La banque~Le tourisme uniquement~L'agriculture uniquement", 0,
     "Toute installation mecanisee a besoin de maintenance."),
 QC("Quel phenomenon redessine aujourd'hui la carte industrielle ?", "La transition energetique et le numerique~La fin des transports~Le retour a l'artisanat seul~La disparition des usines", 0,
     "Les transitions energetique et numerique modifient les localisations."),
 QT("Analyser les facteurs qui expliquent la localisation d'une usine metallurgique au bord d'un canal au XIXe siecle.",
    "Au XIXe siecle, la metallurgie consomme beaucoup d'energie et de matieres premières. Le canal assure un transport bon march pour le minerai, le charbon et les produits finis, avec une capacite bien superieure a la route de l'epoque. La presence d'eau sert aussi au refroidissement et a l'alimentation des machines a vapeur. Enfin, l'usine attire une main-d'oeuvre qui se loge dans les cites ouvrieres voisines. Ces facteurs combinent cout de transport, acces a l'energie et disponibilite de travailleurs.",
    "On doit citer transport, energie, matieres premieres et main-d'oeuvre."),
 QT("Expliquer le lien entre desindustrialisation, reconversion et besoins de formation technique.",
    "La desindustrialisation provoque la fermeture de sites, la perte d'emplois et une baisse d'activite locale. Une reconversion reussie ne se limite pas a attirer de nouvelles entreprises : elle doit aussi adapter les competences des habitants aux technologies actuelles, comme l'automatisation, la commande numerique ou la maintenance desystemes connectes. Les centres de formation et les baccalaureats professionnels jouent alors un role central. Sans cette mise a jour, le territoire risque de cumuler chomage des anciens salaries et penurie de techniciens pour les nouveaux emplois.",
    "On relie perte d'emplois, diversification et adaptation des competences.")],
C("L'industrie faconne les territoires : les usines choisissent leur site, puis leur declin ou leur reconversion transforme la ville.",
  "Localisation = transports + energie + main-d'oeuvre + marche",
  "Agglomeration : avantages et contraintes · reconversion : diversification et formation",
  "Localisation~Choix du site~Cite ouvriere~Logement des travailleurs~Agglomeration~Regroupement d'entreprises~Desindustrialisation~Fermeture de sites~Reconversion~Nouvelles activites",
  "Décrire le territoire|Identifier les facteurs de localisation|Analyser les effets sur la ville|Observer les mutations|Relier aux emplois locaux",
  "Reduire la localisation au hasard|Ignorer les effets environnementaux|Confondre reconversion et fermeture|Oublier le role de la formation",
  "Canal~Transport du minerai~Cite ouvriere~Logements pres de l'usine~1970~Desindustrialisation~Aujourd'hui~Parcs d'activites~Maintenance~Emploi transversal",
  "Agglomeration~Effets positifs~Concentration~Pollution et dependance",
  "Desindustrialisation~Perte d'emplois~Reconversion~Creation de nouveaux emplois"))

# ============================================================ EN1
add("EN1", "Present simple and technical descriptions", "Anglais",
S("The present simple describes habits, routines and general truths."
  "|Use the base form for I, you, we and they."
  "|Add -s or -es to the third person singular: he checks, she watches."
  "|Negatives use does not or doesn't with the base form."
  "|Questions use do or does before the subject."
  "|The verb to be is irregular: I am, he is, they are."
  "|Frequency adverbs such as always, usually and never come before the main verb."
  "|Technical English prefers short, precise sentences and an active voice."
  "|The impersonal it is used for measurements: it is 20 degrees."
  "|Must expresses an obligation, can expresses an ability or a possibility."
  "|A manual often uses the imperative to give an instruction: check the oil level."
  "|The present passive is formed with be plus the past participle: the pump is driven by a motor."
  ""),
[QC("Which sentence is correct ?", "He check the oil~He checks the oil~He checking the oil~He checked the oil yesterday", 1,
     "With he, the present simple takes -s: he checks."),
 QC("How do you form a negative with he ?", "He don't check~He doesn't check~He not check~He isn't check", 1,
     "Use doesn't followed by the base form: he doesn't check."),
 QC("Which verb is irregular ?", "To check~To be~To measure~To start", 1,
     "To be has am, is, are in the present."),
 QC("Where does usually go in a sentence ?", "After the verb~Before the main verb~At the end only~At the beginning only", 1,
     "Frequency adverbs are placed before the main verb."),
 QC("What does must express ?", "An obligation~A possibility~A suggestion~A past habit", 0,
     "Must expresses a strong obligation or necessity."),
 QC("How is the present passive formed ?", "Be plus past participle~Have plus past participle~Do plus verb~Will plus verb", 0,
     "For example: the belt is driven by the motor."),
 QC("What does a manual often use to give an instruction ?", "The imperative~The future tense~The conditional~The passive only", 0,
     "Instructions are commonly written in the imperative: check, replace, tighten."),
 QT("Translate into English: 'Le technicien vérifie la tension toutes les semaines et remplace le filtre si nécessaire.'",
    "The technician checks the voltage every week and replaces the filter if necessary. The third person singular requires -s on both verbs, checks and replaces. The frequency expression every week is placed at the end of the first clause, and the conditional structure if necessary is a common concise form in technical documents.",
    "Check the -s at the third person and the order of the frequency expression."),
 QT("Explain the difference between 'The pump is powered by a motor' and 'The motor powers the pump'.",
    "Both sentences describe the same reality but adopt different viewpoints. The first is passive: the pump, the receiver of the action, is the subject, which is typical of a technical description focused on the equipment being described. The second is active: the motor, the agent, becomes the subject, which makes the sentence more direct. Technical manuals often prefer the passive when the agent is obvious or unimportant, and the active when the cause must be emphasized.",
    "Identify the passive and active forms and explain which element is foregrounded.")],
C("The present simple states facts, routines and instructions; technical English favours precision, short sentences and the passive when the agent is not the focus.",
  "He/she/it + verb-s · do/does for questions",
  "Passive : be + past participle · must = obligation",
  "Present simple~Facts and routines~Third person~Verb plus s~Imperative~Instruction~Passive~Be plus participle~Manual~Technical document",
  "Identify the subject|Choose the right verb form|Place frequency adverbs|Select active or passive|Check units and spelling",
  "Forgetting the -s with he|Using don't with he|Confusing can and must|Translating word for word",
  "He checks~Third person present~Doesn't check~Negative form~Is driven~Present passive~Check the oil~Imperative",
  "Active~The motor powers the pump~Passive~The pump is powered by a motor",
  "Must~Obligation~Can~Ability or possibility"))

# ============================================================ EN2
add("EN2", "Past simple and incident reports", "Anglais",
S("The past simple describes completed actions at a definite time in the past."
  "|Regular verbs add -ed: check becomes checked, stop becomes stopped."
  "|Irregular verbs have their own forms: see saw, take took, break broke."
  "|Negative sentences use did not or didn't plus the base form."
  "|The verb to be has two past forms: was for I, he, she, it and were for you, we, they."
  "|Time expressions such as yesterday, last week and in 2025 signal the past simple."
  "|The past continuous describes an action in progress: was running."
  "|Use the past simple for an interrupting action: the belt broke while the machine was running."
  "|An incident report states what happened, when, where and what action was taken."
  "|Technical vocabulary includes failure, leakage, overheating, breakdown and shutdown."
  "|Keep reports factual and avoid emotional language."
  "|Always include measurements and units in an English incident report."),
[QC("Which is the past form of break ?", "Breaked~Broke~Broken~Breaking", 1,
     "Break is irregular: break, broke, broken."),
 QC("How do you form a negative in the past simple ?", "Don't plus verb~Didn't plus base form~Didn't plus -ed~Wasn't plus -ed", 1,
     "Use didn't followed by the base form: didn't check."),
 QC("Which time expression signals the past simple ?", "Tomorrow~Yesterday~Now~Every day", 1,
     "Yesterday refers to a completed time in the past."),
 QC("What does the past continuous describe ?", "A habit~An action in progress~A future plan~A permanent state", 1,
     "It describes an ongoing action at a past moment."),
 QC("Which word means 'une fuite' ?", "Failure~Leakage~Shutdown~Overheating", 1,
     "Leakage is a leak; failure is a breakdown, overheating is excessive heat."),
 QC("What should an incident report contain ?", "Only opinions~Facts, time, place and actions taken~Jokes~Only the date", 1,
     "A report must be factual and complete."),
 QC("Which sentence is correct ?", "The belt broke while the machine was running~The belt was breaking while the machine run~The belt break while the machine was running~The belt broke while the machine runs", 0,
     "Past simple for the interruption and past continuous for the ongoing action."),
 QT("Write a short incident report in English: yesterday, pump P2 overheated, technician replaced the seal, machine restarted at 14:30.",
    "Yesterday at 10:15, pump P2 overheated in workshop 3. The technician checked the cooling circuit and found a damaged mechanical seal. He replaced the seal and refilled the circuit. The machine restarted at 14:30 and the temperature returned to 62 degrees Celsius. No further problem was observed during the two-hour test.",
    "Use the past simple for completed actions, include time, place and measurements."),
 QT("Explain when to use the past continuous instead of the past simple in an incident description.",
    "Use the past continuous for the background situation or an action that was in progress when something happened: the conveyor was running at full speed. Use the past simple for the completed event that interrupts or follows it: the belt broke. Combining the two tenses shows the sequence and the circumstances, which is useful in an incident report because it explains the context of the failure without adding opinions. For example: while the operator was cleaning the area, the sensor detected an abnormal vibration and the line stopped automatically.",
    "The distinction between background action and interrupting event must be clear.")],
C("The past simple reports what happened; the past continuous sets the scene. An incident report combines both with precise facts and units.",
  "Regular : verb + ed · irregular : own form",
  "Negative : didn't + base form · past continuous : was/were + verb-ing",
  "Past simple~Completed action~Irregular verb~Own past form~Past continuous~Action in progress~Incident report~Facts and actions~Leakage~Fuite",
  "State what happened|Give time and place|Describe the background|List actions taken|Add measurements and units",
  "Adding -ed to irregular verbs|Using didn't with a past form|Writing opinions in a report|Omitting units",
  "Broke~Past of break~Was running~Background action~Leakage~Fuite~Overheating~Surchauffe~Shutdown~Arret",
  "Past simple~Interrupting event~Past continuous~Ongoing situation",
  "Failure~Defaillance~Leakage~Fuite"))

# ============================================================ EN3
add("EN3", "Modals and safety instructions at work", "Anglais",
S("Modal verbs express ability, obligation, permission, possibility and advice."
  "|Can expresses ability or possibility: I can read a wiring diagram."
  "|Must expresses a strong obligation: you must wear safety glasses."
  "|Have to also expresses obligation, often imposed by a rule or a person."
  "|Must not expresses prohibition: you must not remove the guard."
  "|Do not have to means that something is not necessary."
  "|Should expresses advice: you should check the oil level."
  "|Modals are followed by the base form of the verb, without to."
  "|They do not take -s at the third person singular."
  "|Questions are formed by placing the modal before the subject."
  "|Safety instructions are short, clear and use imperatives or modals."
  "|Common safety vocabulary includes PPE, hazard, lockout and permit to work."),
[QC("Which modal expresses ability ?", "Must~Can~Should~May", 1,
     "Can expresses ability: I can weld, I can read a diagram."),
 QC("Which sentence expresses a prohibition ?", "You must wear gloves~You must not remove the guard~You should wear gloves~You can remove the guard", 1,
     "Must not means it is forbidden."),
 QC("What follows a modal verb ?", "The -ing form~The base form~The past participle~The infinitive with to", 1,
     "Say 'you must check', not 'you must to check'."),
 QC("Which modal gives advice ?", "Can~Should~Must~May", 1,
     "Should is used for recommendations and advice."),
 QC("What does 'do not have to' mean ?", "It is forbidden~It is not necessary~It is obligatory~It is impossible", 1,
     "No obligation: the action is optional."),
 QC("Do modals take -s at the third person ?", "Yes, always~No~Only with he~Only in questions", 1,
     "Say 'he must wear', not 'he musts wear'."),
 QC("What does PPE stand for ?", "Personal Protective Equipment~Permanent Power Equipment~Process Planning Engineering~Pressure Protection Engine", 0,
     "PPE means personal protective equipment, such as gloves and goggles."),
 QT("Translate these safety rules into English: 'Il faut porter des gants, il est interdit de retirer la protection et il est conseillé de vérifier la pression.'",
    "You must wear gloves. You must not remove the guard. You should check the pressure. Must expresses the obligation, must not the prohibition and should the recommendation. Each modal is followed by the base form of the verb, with no -s even though the subject is you, and no 'to' before the verb.",
    "Check the use of must, must not and should with the base form."),
 QT("Explain the difference between 'must not' and 'do not have to' with a workshop example.",
    "Must not expresses a prohibition: you must not open the electrical cabinet while the power is on, because it is dangerous. Do not have to expresses the absence of obligation: you do not have to wear a hard hat in the office, because there is no risk there. Confusing the two can be dangerous: saying 'you do not have to remove the guard' would wrongly suggest that removing it is optional, when in fact it is forbidden. Safety instructions must therefore choose the modal carefully.",
    "The difference between forbidden and optional must be explicit, with an example.")],
C("Modals give the right level of obligation: must for rules, must not for prohibitions, should for advice, can for ability.",
  "Modal + base form (no to, no -s)",
  "Must : obligation · must not : interdiction · should : conseil · can : possibilite",
  "Must~Obligation~Must not~Interdiction~Should~Conseil~Can~Capacite~PPE~Equipement de protection",
  "Identify the type of rule|Choose the right modal|Use the base form|Keep the sentence short|Check the safety vocabulary",
  "Adding to after must|Adding -s to the modal|Confusing must not and don't have to|Using a long complicated sentence",
  "Wear gloves~Must~Remove the guard~Must not~Check pressure~Should~Read a diagram~Can~Lockout~Consignation",
  "Must not~Interdit~Don't have to~Non obligatoire",
  "Must~Regle stricte~Should~Recommandation"))

# ============================================================ EM1
add("EM1", "Laïcité et neutralité dans l’entreprise", "Enseignement moral et civique",
S("La laicite est un principe qui garantit la liberte de conscience et l'egalite de tous devant la loi."
  "|La loi du 9 decembre 1905 separer les Eglises et l'Etat."
  "|L'Etat ne reconnait aucun culte officiel et ne subventionne pas les religions."
  "|La liberte de culte est protegee, dans le respect de l'ordre public."
  "|La laicite ne signifie pas l'absence de religion, mais la neutralite de l'Etat."
  "|Les agents publics sont tenus a une obligation de neutralite dansexercice de leurs fonctions."
  "|Les usagers du service public doivent respecter les regles de neutralite et de laicite."
  "|Les valeurs de la Republique sont : liberte, egalite, fraternite."
  "|La devise de la Republique figure sur les documents officiels."
  "|L'egalite interdit les discriminations fondees sur l'origine, la religion, le sexe ou l'age."
  "|Dans un atelier ou une entreprise, le respect d'autrui fait partie des regles de vie collective."
  "|Le dialogue et le respect des differences permettent de prevenir les conflits."),
[QC("Que garantit la laicite ?", "Une religion d'Etat~La liberte de conscience et l'egalite~L'interdiction des religions~La suprematie d'un culte", 1,
     "La laicite protege la liberte de croire ou de ne pas croire et l'egalite de tous."),
 QC("Quelle loi separe les Eglises et l'Etat ?", "La loi du 9 decembre 1905~La Constitution de 1958~La loi de 1882~La loi du 1er juillet 1901", 0,
     "C'est la loi de separation du 9 decembre 1905."),
 QC("La laicite signifie-t-elle interdire les religions ?", "Oui~Non, elle garantit leur liberte dans le respect de l'ordre public~Uniquement a l'ecole~Uniquement dans l'entreprise", 1,
     "La liberte de culte est protegee par la loi."),
 QC("Qui est tenu a la neutralite dans le service public ?", "Tous les citoyens~Les agents publics en fonction~Personne~Seulement les eleves", 1,
     "Les agents publics representent l'Etat et doivent etre neutres."),
 QC("Quelles sont les valeurs de la Republique ?", "Liberte, egalite, fraternite~Ordre, autorite, discipline~Travail, famille, patrie~Paix, force, unite", 0,
     "La devise officielle est liberte, egalite, fraternite."),
 QC("Quel comportement est contraire a l'egalite ?", "Respecter un collegue~Discriminer selon l'origine~Ecouter une opinion differente~Signaler une insulte", 1,
     "La discrimination est interdite par la loi."),
 QC("Comment prevenir les conflits dans un atelier ?", "Ignorer les differences~Par le dialogue et le respect des regles communes~En imposant son point de vue~En evitant tout echange", 1,
     "Le respect et le dialogue sont les moyens de vivre ensemble."),
 QT("Expliquer pourquoi la laicite est une condition de l'egalite dans une entreprise.",
    "La laicite garantit que l'origine ou la religion d'une personne n'influence pas son traitement. Dans une entreprise, cela signifie que les regles s'appliquent a tous de la meme maniere, que les salaries ne subissent pas de pression religieuse et que personne n'est desavantage a cause de ses convictions. L'employeur doit respecter la liberte de conscience de chacun tout en assurant la neutralite du service rendu. Cette egalite de traitement favorise la cohesion de l'equipe et la securite, car chacun peut signaler un probleme sans crainte de discrimination.",
    "On relie laicite, egalite de traitement et vie collective dans le travail."),
 QT("Un collegue demande a ne pas participer a une tache un jour de fete religieuse. Comment aborder la situation ?",
    "On ecoute d'abord la demande avec respect, sans porter de jugement. On verifie ensuite ce que prevoit le reglement interieur et la convention collective, car certains aménagements d'horaires peuvent etre negocies. On cherche une solution equitable, par exemple un échange de service avec un autre collegue volontaire, en veillant a ce que la continuite du service et la securite soient assurees. On traite la demande comme toute autre demande personnelle, selon les memes regles pour tous, ce qui est precisement le principe d'egalite.",
    "On attend une demarche de dialogue, de verification des regles et de traitement equitable.")],
C("La laicite protege la liberte de conscience et garantit l'egalite : dans le travail, elle impose neutralite, respect et traitement identique pour tous.",
  "Liberte de conscience + neutralite de l'Etat +egalite devant la loi",
  "Loi du 9 decembre 1905 · devise : liberte, egalite, fraternite",
  "Laicite~Neutralite de l'Etat~Loi 1905~Separation des Eglises et de l'Etat~Neutralite~Obligation des agents~Egalite~Interdiction des discriminations~Fraternite~Solidarite",
  "Ecouter la demande|Verifier le cadre legal et le reglement|Chercher une solution equitable|Respecter la continuite du service|Documenter la decision",
  "Confondre laicite et interdiction de la religion|Imposer ses convictions|Traiter differemment deux demandes semblables|Ignorer le reglement interieur",
  "1905~Separation des Eglises et de l'Etat~Devise~Liberte, egalite, fraternite~Agent public~Neutralite~Atelier~Respect d'autrui",
  "Laicite~Neutralite de l'Etat~Tolerance~Respect des differences",
  "Egalite~Meme traitement~Discrimination~Traitement different injustifie"))

# ============================================================ EM2
add("EM2", "Citoyenneté, engagement et règles collectives au travail", "Enseignement moral et civique",
S("La citoyennete designe l'appartenance a une communaute politique et le respect de ses regles."
  "|Un citoyen dispose de droits et doit respecter des devoirs."
  "|Le respect de la loi est un devoir fundamental."
  "|La participation a la vie collective peut prendre des formes variees : vote, syndicat, association."
  "|Dans une entreprise, le reglement interieur fixe les regles de vie et de securite."
  "|Le respect des regles de securite protège le salarie et ses collegues."
  "|Signaler un danger ou un incident est une forme d'engagement responsable."
  "|La solidarite se manifeste par l'entraide et le soutien aux collegues en difficulté."
  "|Le dialogue social passe par les representants du personnel et les instances consultatives."
  "|Un conflit collectif doit se regler par le dialogue et le respect de la legalite."
  "|La laicite et l'egalite de traitement s'appliquent aussi dans le monde professionnel."
  "|L'engagement citoyen se construit des la jeunesse, notamment par la vie scolaire et l'apprentissage."),
[QC("Qu'est-ce qu'un citoyen ?", "Une personne qui travaille~Un membre d'une communaute politique avec des droits et des devoirs~Un salarie d'usine~Un representant syndical", 1,
     "La citoyennete associe des droits et des devoirs."),
 QC("Quel document fixe les regles de vie dans une entreprise ?", "Le bulletin de salaire~Le reglement interieur~Le plan de formation~Le contrat de client", 1,
     "Le reglement interieur definite les regles collectives et de securite."),
 QC("Que faire face a une situation dangereuse ?", "L'ignorer~Signaler le danger et appliquer la procedure~Attendre un accident~Le cacher au responsable", 1,
     "Le signalement permet de prevenir les accidents."),
 QC("Quel est un moyen de participation collective ?", "Le vote et le syndicat~La resistance individuelle~Le refus de dialoguer~L'absence de regles", 0,
     "Le vote, le syndicat et les associations sont des formes de participation."),
 QC("Comment regler un conflit collectif ?", "Par la force~Par le dialogue dans le respect de la loi~En isolant les salaries~En supprimant les regles", 1,
     "Le dialogue social est le cadre legal de reglement des conflits."),
 QC("La solidarite au travail consiste a...", "Ne s'occuper que de sa tache~Aider un collegue en difficulté~Refuser de travailler en equipe~Critiquer les autres", 1,
     "L'entraide est une composante de la vie collective."),
 QC("L'engagement citoyen commence-t-il a l'age adulte ?", "Oui, seulement apres 18 ans~Non, il se construit des la jeunesse~Uniquement en entreprise~Jamais a l'ecole", 1,
     "La vie scolaire et l'apprentissage sont deja des lieux d'engagement."),
 QT("Expliquer le lien entre respect des regles de securite et citoyennete dans un atelier.",
    "Respecter les regles de securite, ce n'est pas seulement obeir a une consigne : c'est respecter la vie et la sante de ses collegues. Une personne qui retire un protecteur ou ne signale pas une fuite met en danger toute l'equipe, pas seulement elle-meme. La citoyennete sur le lieu de travail se traduit donc par une attitude responsable : connaitre les regles, les appliquer, signaler les ecarts et accepter les controles. Cet engagement collectif est aussi une condition de la qualite et de la productivite de l'entreprise.",
    "On doit relier securite, responsabilite individuelle et interet collectif."),
 QT("Un desequipements de protection manque dans l'atelier. Décrire la demarche responsable a suivre.",
    "On arrete immediatement l'utilisation de la machine concernee si la protection est indispensable, on signale le manque au responsable d'equipe et on le consigne dans le registre ou la GMAO. On informe les collegues pour eviter qu'ils utilisent la machine, en posant si possible une signalisation temporaire. On suit la procedure de consignation si une intervention est necessaire. Enfin, on verifie la remise en etat avant la reprise. Cette demarche montre un engagement responsable : on ne cherche pas un coupable, on protege les personnes et on documente l'ecart.",
    "On attend: arret ou signalement, information, consignation, suivi et verification.")],
C("Etre citoyen au travail, c'est respecter les regles communes, signaler les dangers et contribuer a la vie collective dans le respect de la loi.",
  "Droits + devoirs + participation + solidarite",
  "Reglement interieur · securite · dialogue social · signalement",
  "Citoyennete~Droits et devoirs~Reglement interieur~Regles de l'entreprise~Securite~Protection de tous~Solidarite~Entraide~Dialogue social~Representation du personnel",
  "Connaitre les regles|Appliquer les consignes|Signaler les ecarts|Informer l'equipe|Suivre la remise en etat",
  "Ignorer une consigne de securite|Ne pas signaler un danger|Regler un conflit par la force|Laisser un collegue sans protection",
  "Protection manquante~Signaler et consigner~Consignation~Procedure de securite~Registre~Trace de l'ecart~Reprise~Verification avant redemarrage",
  "Citoyennete~Vie politique et sociale~Engagement~Action responsable",
  "Reglement interieur~Cadre local~Loi~Cadre national"))

# FIN DES LOTS
valider_et_ecrire(F, "pro-maintenance-mat-part-A.json")
