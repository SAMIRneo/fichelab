# -*- coding: utf-8 -*-
"""Generateur std2a-mat-part-A.json — lot A : tronc commun (20 fiches).

Français (5), Maths (5), HGGS (4), Anglais (2), EMC (2), Philosophie (2).
Chaque fiche : 12 points, 9 questions (7 QCM + 2 texte), 7 blocs, 3 SVG.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _std2a_common import FIL, REF, S, R, QC, QT, C, build, valider_et_ecrire

F = []
T = ["1re", "Terminale"]
P12 = ["1re", "Terminale"]
TER = ["Terminale"]

def add(prefix, titre, mat, ans, points, questions, c):
    F.append(build(prefix, titre, mat, ans, points, questions, c))

# ============================================================ FR01
add("FR01", "Argumentation et rhetorique : construire un texte persuasif", "Français", T,
S("L'argumentation vise a convaincre un destinataire en avancant des raisons et des preuves."
  "|La these est l'idee defendue ; elle peut etre nuancee par une objection ou une concession."
  "|Le plan dialectique suit l'ordre these, antitese, synthese ; le plan analytique presente le probleme, les causes puis les solutions."
  "|Un argument est une raison generale ; un exemple est un cas particulier qui l'illustre."
  "|Les trois appels rhetoriques sont le logos (raison), l'ethos (credibilite de l'orateur) et le pathos (emotion)."
  "|La rhetorique classique distingue cinq parties : invention, disposition, elocution, memoire et action."
  "|L'anaphore repete un mot en tete de phrases ; l'antithese oppose deux idees pour frapper l'esprit."
  "|Les connecteurs logiques (donc, car, or, mais) rendent visible la structure du raisonnement."
  "|La concession « certes... mais... » desamorce une objection et donne une impression d'objectivite."
  "|La refutation repond directement a l'argument adverse pour le deconstruire."
  "|Une conclusion ne introduit pas d'argument nouveau : elle resume et ouvre une perspective."
  "|En STD2A, l'argumentation sert aussi a justifier un choix de design dans un rapport de projet."),
[QC("Quelle est la finalite principale de l'argumentation ?", "Convaincre un destinataire~Raconter une histoire~Decrire un paysage~Etablir un catalogue", 0,
     "L'argumentation a pour but de convaincre en s'appuyant sur des raisons et des preuves."),
 QC("Quel est l'ordre du plan dialectique ?", "Antithese, these, synthese~These, antitese, synthese~Cause, effet, solution~Exemple, argument, these", 1,
     "Le plan dialectique se deroule en these, antitese puis synthese (ou nuance)."),
 QC("Quelle difference existe-t-il entre argument et exemple ?", "L'argument est un cas particulier~L'argument est une raison generale, l'exemple un cas concret~Il n'y en a aucune~L'exemple est toujours chiffre", 1,
     "L'argument est une raison generale ; l'exemple est un cas particulier qui l'illustre."),
 QC("A quoi correspond l'appel rhetorique « ethos » ?", "A l'emotion~A la logique~A l'image de l'orateur~Au rythme de la phrase", 2,
     "L'ethos designe la credibilite et l'image que l'orateur donne de lui-meme."),
 QC("Quel connecteur introduit une concession ?", "Cependant n'est pas une concession~Certes... mais...~Donc~En effet", 1,
     "La structure « certes... mais... » concede un point avant de le nuancer."),
 QC("Quelle figure repete un mot en debut de phrases successives ?", "L'antithese~La metaphore~L'anaphore~La litote", 2,
     "L'anaphore est la repetition d'un meme mot en tete de plusieurs phrases ou vers."),
 QC("Que fait-on dans une ouverture de conclusion ?", "On ajoute un argument decisif~On elargit la perspective~On change de these~On presente la bibliographie", 1,
     "L'ouverture elargit le sujet sans introduire d'argument nouveau."),
 QT("Expliquer la difference entre argument et exemple, puis illustrer avec un choix de design.",
    "Un argument est une raison generale qui soutient la these : par exemple, le choix d'une matiere conditionne l'empreinte environnementale d'un objet. Un exemple est un cas concret qui rend cette raison sensible : le carton recycle utilise dans un emballage reduit la consommation de ressources vierges. L'argument donne la regle, l'exemple la rend credible et memorable. Dans un rapport de projet, on enchaine donc « les matieres recyclables limitent l'impact (argument) ; notre boitier en carton compressé en est une illustration (exemple) ».",
    "On attend la distinction raison generale / cas concret et un exemple lie au design ou a l'objet."),
 QT("Rediger un court paragraphe argumentatif justifiant le choix d'une matiere recyclee.",
    "Notre projet retient le carton recycle pour le boitier. Ce choix repond d'abord a une exigence environnementale : la matiere provient d'une filiere de collecte et evite l'extraction de ressources nouvelles. Certes, sa resistance a l'humidité est plus faible que celle d'un polymer, mais un traitement de surface et une forme etanche compensent cette limite. Des lors, le produit concilie sobriete de moyens et usage quotidien, ce qui donne tout son sens a la demarche de design durable.",
    "Le paragraphe doit contenir une these, au moins un argument, une concession et un connecteur logique.")],
C("Argumenter, c'est organiser des raisons et des preuves pour faire adherer un destinataire a une these tout en anticipant ses objections.",
  "Convaincre = these + arguments + exemples + refutation",
  "logos = raisons · ethos = credibilite · pathos = emotion · anaphore = repetition en tete de phrase",
  "These~Idee defendue~Peut etre nuancee~Argument~Raison generale~Soutient la these~Exemple~Cas concret~Illustre l'argument",
  "Definir la these et le destinataire|Choisir les arguments et les preuves|Anticiper les objections|Construire le plan et placer les connecteurs|Conclure et ouvrir la perspective",
  "Confondre argument et exemple|Enchainer les idees sans connecteurs|Oublier de nuancer la these|Introduire un argument nouveau en conclusion",
  "These~Le design doit etre durable~Argument~La matiere impacte le cycle de vie~Exemple~Le carton recycle reduit l'empreinte~Refutation~L'objection du cout~Ouverture~L'eco-conception des le croquis",
  "These~Idee defendue~Position de depart~Antitese~Idee contraire~Permet la nuance",
  "Logos~Raisons et preuves~Fait appel a l'intelligence~Pathos~Emotion et images~Fait appel a la sensibilite"))

# ============================================================ FR02
add("FR02", "Figures de style et registres : identifier et interpreter", "Français", T,
S("Une figure de style est un ecart volontaire par rapport a l'usage ordinaire de la langue."
  "|La comparaison rapproche deux elements avec un outil (comme, tel, semblable) ; la metaphore les identifie sans outil."
  "|La personnification attribue des actions ou des sentiments humains a un objet, un animal ou une idee abstraite."
  "|L'oxymore associe en un seul syntagme deux termes contradictoires."
  "|L'antithese oppose deux idees ou deux termes dans une meme phrase ou un meme vers."
  "|L'hyperbole exaggeres une realite ; la litote dit moins pour suggérer davantage."
  "|L'euphemisme attenue une realite brutale par un mot plus doux."
  "|Le registre tragique suscite la pitie et la terreur ; le registre pathos la compassion."
  "|Le registre comique vise le rire ; le registre satirique se moque pour corriger."
  "|Le registre epique celebre une action heroique ; le registre lyrique exprime un sentiment intime."
  "|Le registre realiste decrit le quotidien ; le registre fantastique introduit l'etrange dans le reel."
  "|Interpreter une figure, c'est relier son effet de sens a l'intention du texte et a son contexte."),
[QC("Quelle figure compare sans outil de comparaison ?", "La comparaison~La metaphore~L'antithese~La litote", 1,
     "La metaphore identifie deux elements sans comme ni tel ; la comparaison garde un outil."),
 QC("Que designe un oxymore ?", "Deux mots opposes dans un meme syntagme~Une repetition en debut de vers~Une exaggeration~Une atténuation", 0,
     "L'oxymore juxtapose deux termes contradictoires, comme « un silence assourdissant »."),
 QC("« Un silence de plomb » est une...", "Personnification~Metaphore~Hyperbole~Litote", 1,
     "Le silence est compare implicitement au plomb : c'est une metaphore."),
 QC("Quel registre vise la pitie et la terreur ?", "Comique~Tragique~Epique~Reel", 1,
     "Le registre tragique est defini par la pitie et la terreur depuis la poetique d'Aristote."),
 QC("Quelle figure attribue des traits humains a un objet ?", "L'euphemisme~La personnification~L'oxymore~L'antithese", 1,
     "La personnification donne des actions ou des sentiments humains a un non-humain."),
 QC("Que permet la litote ?", "Dire plus en paraitre moins~Dire moins pour suggérer plus~Repeter un mot~Exaggerer un trait", 1,
     "La litote dit moins pour laisser le lecteur deviner davantage."),
 QC("Quel registre introduit l'etrange dans un cadre quotidien ?", "Realiste~Fantastique~Lyrique~Satirique", 1,
     "Le fantastique fait irrompre l'etrange dans un monde par ailleurs reel."),
 QT("Distinguer comparaison et metaphore et expliquer leur effet respectif.",
    "La comparaison explicite le rapprochement au moyen d'un outil : « cette etoffe est comme une peau ». La metaphore supprime l'outil et present le terme image comme une realite : « cette etoffe est une peau ». La comparaison laisse le lecteur conscient de l'analogie, tandis que la metaphore produit un effet de surprise et d'incarnation plus fort. Dans l'analyse d'une image publicitaire, repérer cette difference permet de comprendre si le createur montre la ressemblance ou s'il donne a voir une identite entre le produit et ce qu'il symbolise.",
    "On attend la presence ou l'absence d'outil de comparaison et une explicitation de l'effet de sens."),
 QT("Analyser la phrase « cette chaise est une invitation au repos ».",
    "Il s'agit d'une metaphore : le terme « invitation » est applique a la chaise sans outil de comparaison. Le siege n'invite pas litteralement, mais la phrase transforme un objet en une promesse de detente. Cette personnification legere associe un confort physique a une experience emotionnelle. Dans une fiche produit, une telle figure ne decrit pas seulement la forme : elle construit une image de marque et une valeur d'usage desirante.",
    "La reponse doit nommer la metaphore, expliquer le mecanisme et proposer une interpretation en contexte.")],
C("Une figure de style est un ecart maitrise qui produit un effet de sens ; le registre designe la tonalite generale d'un texte.",
  "Comparaison = avec outil · Metaphore = sans outil · Litote = dire moins",
  "oxymore = termes opposes · antithese = idees opposees · hyperbol = exaggeration",
  "Metaphore~Rapprochement sans outil~Image forte~Comparaison~Rapprochement avec outil~Analogie visible~Personnification~Traits humains~Effet d'incarnation",
  "Repérer l'ecart dans la phrase|Nommer la figure precisement|Citer les mots qui la composent|Expliquer l'effet produit|Relier au registre et a l'intention",
  "Confondre metaphore et comparaison|Nommer une figure sans la justifier|Ignorer le contexte de l'oeuvre|Confondre registre et genre litteraire",
  "Silence de plomb~Metaphore~Poids du silence~Certes, il est lourd~Litote~Nuance~Lumiere aveuglante~Oxymore~Contraste saisissant",
  "Comparaison~Avec comme ou tel~Analogie explicite~Metaphore~Sans outil~Identite imaginee",
  "Tragique~Pitie et terreur~Destin~Comique~Rire et detente~Exces"))

# ============================================================ FR03
add("FR03", "Recit et roman : temps, narrateur et focalisation", "Français", T,
S("Un recit est une suite d'evenements racontes ; il se distingue de la description et de l'argumentation."
  "|Le narrateur omniscient sait tout des personnages et peut se deplacer dans l'espace et le temps."
  "|Le narrateur interne est un personnage de l'histoire ; le narrateur externe reste a l'exterieur."
  "|La focalisation interne adopte le point de vue d'un personnage ; la focalisation externe ne montre que les apparences."
  "|La focalisation zero correspond au narrateur omniscient qui connait les pensees de tous."
  "|L'ordre du recit peut etre chronologique ou bouleverse par une analepse (retour en arriere) ou une prolepse (anticipation)."
  "|La duree joue sur la vitesse : scene, resume, ellipse ou pause descriptive."
  "|La frequence indique si un evenement est raconte une fois, plusieurs fois ou comme habituel."
  "|Le dialogue donne l'illusion de la parole ; le discours indirect integre les propos au recit."
  "|La description ralentit le rythme et construit l'atmosphere ou le decor."
  "|Le roman realiste presente une societe et des personnages typiques ; le roman graphique transpose le recit en images."
  "|En design, la bande dessinee et le storyboard utilisent les memes outils de temps, de cadre et de point de vue."),
[QC("Qu'appelle-t-on un narrateur omniscient ?", "Un personnage de l'histoire~Un narrateur qui connait tout des personnages~Un lecteur~Un auteur absent", 1,
     "Le narrateur omniscient connait les pensees, les sentiments et le passe de tous les personnages."),
 QC("Quelle focalisation adopte le point de vue d'un seul personnage ?", "Externe~Interne~Zero~Multiple", 1,
     "La focalisation interne filtre le recit par la conscience d'un personnage."),
 QC("Qu'est-ce qu'une analepse ?", "Une anticipation~Un retour en arriere~Une ellipse~Une pause", 1,
     "L'analepse est un retour en arriere dans le temps du recit."),
 QC("Quel procede fait avancer le recit en quelques lignes sur plusieurs annees ?", "La scene~Le resume~Le dialogue~La description", 1,
     "Le resume condense une longue periode ; la scene, elle, est etalee en direct."),
 QC("Quel narrateur ne montre que ce qu'un observateur exterieur peut voir ?", "Omniscient~Interne~Externe~Personnage", 2,
     "La focalisation externe ignore les pensees et ne fait etat que des apparences."),
 QC("A quoi sert une ellipse dans un recit ?", "A ralentir l'action~A supprimer un passage de temps~A decrire le decor~A introduire un dialogue", 1,
     "L'ellipse passe sous silence une periode pour accelerer le rythme."),
 QC("Quel lien existe-t-il entre storyboard et recit ?", "Aucun~Le storyboard découpe le temps en images comme le recit en evenements~Le storyboard remplace le texte~Le storyboard est un roman", 1,
     "Le storyboard segmente l'action en plans et rend visible la duree et le point de vue."),
 QT("Expliquer la difference entre narrateur interne et narrateur omniscient.",
    "Le narrateur interne est un personnage de la fiction : il ne connait que ce qu'il voit, entend et ressent, et il peut se tromper ou etre partial. Le narrateur omniscient se place au-dela de l'histoire : il connait le passe, l'avenir et les pensees secretes de chaque personnage, et il peut changer de point de vue. Cette difference modifie la focalisation : interne dans le premier cas, zero dans le second. Elle change aussi la confiance du lecteur, qui doit reconstruire la verite avec un narrateur interne, alors qu'il recoit une information complete avec un narrateur omniscient.",
    "On attend la distinction appartenance a l'histoire / savoir total et la consequence sur la focalisation."),
 QT("Analyser les effets d'une analepse dans un recit de design.",
    "L'analepse interrompt l'ordre chronologique pour revenir sur un evenement passe, par exemple la premiere esquisse d'un objet ou un echec de prototypage. Elle crée une suspension et donne au lecteur une cle de comprehension du present : on comprend pourquoi le designer a retenu telle matiere ou telle forme. Elle permet aussi de construire une image de l'auteur du projet en montrant son parcours. En bande dessinee ou en storyboard, ce retour en arriere se traduit par un changement de cadre ou de couleur, qui signalle la rupture de temps.",
    "La reponse doit definir l'analepse et expliquer son effet sur la comprehension et le rythme.")],
C("Le recit organise des evenements dans le temps et adopte un point de vue : narrator et focalisation determinent ce que le lecteur sait.",
  "Recit = temps + narrateur + focalisation",
  "analepse = retour arriere · prolepse = anticipation · ellipse = temps supprime",
  "Omniscient~Sait tout~Focalisation zero~Interne~Est un personnage~Savoir limite~Externe~Voit l'apparence~Focalisation externe",
  "Identifier le narrateur et sa place|Determiner la focalisation|Relever les indices de temps|Repérer analepses et prolepses|Analyser l'effet sur le lecteur",
  "Confondre narrateur et auteur|Nommer la focalisation sans preuve textuelle|Ignorer les ruptures de chronologie|Croire que le dialogue est toujours au present",
  "Analepse~Retour sur le premier croquis~Prolepse~Annonce du resultat final~Ellipse~Passage sous silence des essais~Scene~Echange au present~Storyboard~Découpage en plans",
  "Narrateur interne~Partial et limite~Narrateur omniscient~Savoir complet et mobile",
  "Analepse~Retour en arriere~Prolepse~Anticipation"))

# ============================================================ FR04
add("FR04", "Poésie et versification : rythme, image et sens", "Français", T,
S("Le vers est une ligne de poeme soumise a une mesure ; la strophe est un groupe de vers."
  "|En poesie classique, l'alexandrin compte douze syllables ; l'octosyllabe en compte huit."
  "|La cesure est une coupe a l'interieur du vers qui organise le souffle et le rythme."
  "|La diérèse separe deux voyelles en deux syllables ; la synalephe les fond en une seule."
  "|L'enjambement prolonge une phrase ou un sens au vers suivant ; le rejet est un enjambement court en debut de vers."
  "|La rime est la repetition d'une sonie finale ; les rimes peuvent etre croisees, embrassees ou suivies."
  "|Le sonnet comporte deux quatrains puis deux tercets, avec une volta ou un retournement final."
  "|Le poeme en prose n'a pas de vers mais garde la densite imagee et le rythme."
  "|Le vers libre se libere de la mesure reguliere tout en travaillant le rythme et la repetition."
  "|L'image poétique associe des elements pour produire un sens nouveau, souvent par metaphore."
  "|La musicalite d'un poeme vient des sons, des repetitions et des silences autant que du sens."
  "|Les procédés poétiques aident en design a travailler le rythme d'une composition et le slogan."),
[QC("Combien de syllables compte un alexandrin ?", "8~10~12~14", 2,
     "L'alexandrin classique compte douze syllables, avec une cesure generalement a la sixieme."),
 QC("Qu'appelle-t-on une cesure ?", "Une rime finale~Une coupe a l'interieur du vers~Un enjambement~Une strophe", 1,
     "La cesure partage le vers en deux hémistiches et organise le souffle."),
 QC("Quel phenomene separe deux voyelles en deux syllables ?", "La synalephe~La diérèse~L'enjambement~La rime", 1,
     "La diérèse prononce separement deux voyelles ; la synalephe les contracte."),
 QC("Comment sont disposees les rimes croisees ?", "ABBA~AABB~ABAB~AAAA", 2,
     "Les rimes croisees alternent les sonies selon le schema ABAB."),
 QC("Quelle structure caracterise un sonnet ?", "Trois quatrains~Deux quatrains et deux tercets~Quatre tercets~Deux distiques", 1,
     "Le sonnet se compose de deux quatrains puis de deux tercets."),
 QC("Qu'est-ce qu'un enjambement ?", "Une rime riche~Une prolongation du sens au vers suivant~Une coupe fixe~Un poeme en prose", 1,
     "L'enjambement fait passer la phrase ou le sens d'un vers au suivant."),
 QC("Quel procede travaille le rythme sans mesure reguliere ?", "L'alexandrin~Le vers libre~La rime croisee~Le quatrain", 1,
     "Le vers libre renonce a la mesure fixe mais construit un rythme par d'autres moyens."),
 QT("Expliquer la difference entre diérèse et synalephe avec un exemple.",
    "La diérèse fait entendre deux syllables la ou l'ecriture semble en proposer une : « aventure » se prononce a-ven-ture avec un « a » et un « u » distincts dans la mesure classique. La synalephe, au contraire, elide une voyelle finale devant une voyelle initiale pour n'en faire qu'une : « le amour » se prononce « l'amour » en une seule syllable commune. Ces deux procedes permettent au poete d'ajuster exactement le nombre de syllables du vers et donc sa musicalite, sans modifier l'ecriture du texte.",
    "On attend une definition opposee et un exemple montant l'effet sur la mesure du vers."),
 QT("Analyser l'effet d'un enjambement dans un poeme.",
    "L'enjambement force le vers a ne pas s'arreter sur sa fin : le lecteur enjambe la rime ou la coupe pour aller chercher la suite. Il crée une tension, accelere le movement ou au contraire erre le sens. Par exemple, un vers qui se termine par « le vent » et se prolonge par « emporte la réponse » fait glisser l'image du souffle vers l'idee de message. Le rejet, tres bref au debut du vers suivant, produit un effet de surprise. Dans une affiche ou un slogan, ce principe se retrouve quand une phrase continue sur une autre ligne pour retarder la lecture et capter l'attention.",
    "La reponse doit expliquer le mecanisme, l'effet de rythme et proposer une application.")],
C("La versification organise le souffle et le son du poeme ; image et rythme produisent ensemble du sens.",
  "Alexandrin = 12 syllables · cesure a la 6e",
  "enjambement = sens prolonge · diérèse = voyelles separees · synalephe = voyelles fusionnees",
  "Alexandrin~Douze syllables~Vers classique~Cesure~Coupe interne~Deux hemistiches~Enjambement~Sens au vers suivant~Tension rythmique",
  "Compter les syllables|Repérer la cesure|Identifier les rimes et leur schema|Noter enjambements et rejets|Relier rythme et sens",
  "Compter les lettres au lieu des syllables|Confondre diérèse et synalephe|Ignorer la ponctuation|Croire que le vers libre n'a pas de rythme",
  "Alexandrin~12 syllables~Cesure~Apres la sixieme~Rime croisee~ABAB~Sonnet~2 quatrains + 2 tercets~Vers libre~Rythme sans mesure",
  "Vers libre~Libere de la mesure~Rythme construit~Vers classique~Mesure fixe~Regles de rime",
  "Dierese~Voyelles separees~Mesure ajustee~Synalephe~Voyelles fondues~Elision"))

# ============================================================ FR05
add("FR05", "Littérature et idées : essai, these et contre-discours", "Français", T,
S("L'essai est un genre qui defend une these sur un sujet de societe, de culture ou d'art."
  "|La these est une affirmation generale que l'essayiste argumente et nuance."
  "|Le paradoxe presente une idée qui choque la opinion commune pour faire penser."
  "|L'argument d'autorite s'appuie sur le propos d'une personne reconnue, sans pour autant prouver la these."
  "|La citation doit etre exacte, introduite et analysee pour etre probante."
  "|L'antimythe deconstruit un recit traditionnel pour en denoncer l'ideologie."
  "|L'utopie decrit une societe idealisee ; la dystopie en montre le revers sombre."
  "|L'engagement de l'ecrivain prend position dans le debat public au nom de valeurs."
  "|La vulgarisation rend accessible un savoir scientifique ou technique sans le trahir."
  "|Le contre-discours confronte une these a une objection pour progresser vers une nuance."
  "|L'album et la bande dessinee documentaire transmettent des idees par le texte et l'image."
  "|En terminale STD2A, ces outils servent a construire un discours personnel sur le design."),
[QC("Quel genre defend une these sur un sujet de societe ou de culture ?", "Le roman~L'essai~La nouvelle~La tragedie", 1,
     "L'essai expose et argumente une these, souvent sur un sujet de societe ou d'art."),
 QC("Qu'est-ce qu'un paradoxe ?", "Une idee evidente~Une affirmation qui heurte l'opinion courante~Une citation~Une conclusion", 1,
     "Le paradoxe choque la doxa pour provoquer la reflexion."),
 QC("Quel est le risque d'un argument d'autorite ?", "Il est toujours faux~Il ne prouve pas par lui-meme la verite de la these~Il est interdit~Il remplace la conclusion", 1,
     "L'autorite de celui qui parle ne constitue pas une preuve logique de la these."),
 QC("Que doit-on faire d'une citation dans un essai ?", "La laisser seule~L'introduire et l'analyser~La raccourcir sans le dire~La placer en conclusion", 1,
     "Une citation probante est introduite, citee exactement puis analysee."),
 QC("Qu'appelle-t-on une dystopie ?", "Une societe ideale~Une societe imaginaire sombre et controlee~Un essai politique~Un poeme", 1,
     "La dystopie decrit un monde futur negatif, souventcontre-utopique."),
 QC("Quel est le role d'un contre-discours ?", "Repeter la these~Confronter une objection pour nuancer~Supprimer les exemples~Clore le debat", 1,
     "Le contre-discours fait progresser l'analyse en integrant l'objection."),
 QC("Quel support transmet des idees par le texte et l'image ?", "Le traite de physique~La bande dessinee documentaire~Le dictionnaire~La lettre", 1,
     "La bande dessinee documentaire couple information ecrite et representation visuelle."),
 QT("Expliquer la difference entre antimythe et simple critique d'un recit.",
    "La critique d'un recit peut se contenter d'en souligner les defauts ou les biais. L'antimythe va plus loin : il reprend la structure meme du mythe ou du grand recit collectif et la retourne pour montrer comment il construit une ideologie. Par exemple, reecrire l'histoire d'une invention depuis le point de vue des artisans rend visibles ceux que le recit officiel efface. L'antimythe ne dit pas seulement « ce recit est faux », il montre « ce recit produit une certaine vision du monde ». C'est un outil puissant pour analyser les representations dans la publicite ou le design.",
    "On attend la dimension de deconstruction ideologique, au-dela de la simple critique."),
 QT("Comment construire un point de vue personnel et argumente sur un objet de design ?",
    "On commence par definir precisement l'objet et la question : a qui sert-il, dans quel contexte, quels besoins satisfait-il ? On rassemble ensuite des faits et des exemples (matieres, usage, reception), puis on formulate une these claire. On confronte cette these a des objections : le cout, l'accessibilite, l'impact environnemental. On cite une source ou un auteur pour situer le debat, puis on nuance la these en synthese. Enfin, on presents le resultat sous forme de texte, d'audio ou de planche, en veillant a ce que le medium choisi serve l'argument et non l'inverse.",
    "La demarche attendue : cadrage, faits, these, objections, sources, nuance et choix du medium.")],
C("Litterature et idees s'appuient sur des genres qui organisent la these, l'objection et la nuance.",
  "These + arguments + objections => position nuancee",
  "essai · paradoxe · antimythe · utopie / dystopie · engagement",
  "Essai~Defense d'une these~Genre argumentatif~Paradoxe~Idee choquante~Fait penser~Antimythe~Deconstruction d'un recit~Ideologie",
  "Cadrer le sujet et la question|Rassembler faits et exemples|Formuler la these|Confronter les objections|Nuancer et presenter le point de vue",
  "Confondre citation et opinion|Utiliser une autorite comme preuve|Refuser toute objection|Choisir le medium apres avoir ecrit le texte",
  "These~Le design est politique~Objection~Il reste un usage~Nuance~Tout choix engage~Citation~Source identifiee~Synthese~Position personnelle",
  "Utopie~Societe ideale~Projection positive~Dystopie~Societe sombre~Mise en garde",
  "These~Affirmation defendue~Antithese~Objection formulee"))

# ============================================================ MA01
add("MA01", "Fonctions affines et linéaires : modéliser une relation", "Maths", T,
S("Une fonction associe a chaque nombre x de son ensemble de definition un unique nombre f(x)."
  "|L'ensemble de definition est l'ensemble des valeurs de x pour lesquelles la fonction est calculee."
  "|L'image de a est f(a) ; un antecedent de y est un nombre x tel que f(x) = y."
  "|Une fonction affine ecrit f(x) = a x + b, ou a est le coefficient directeur et b l'ordonnée a l'origine."
  "|Une fonction lineaire est une fonction affine avec b = 0 : f(x) = a x."
  "|Le coefficient directeur a donne le taux de variation : quand x croit de 1, f(x) varie de a."
  "|La representation graphique d'une fonction affine est une droite qui passe par (0, b)."
  "|Si a > 0 la fonction est croissante ; si a < 0 elle est decroissante ; si a = 0 elle est constante."
  "|Une situation de proportionnalite se modele par une fonction lineaire."
  "|Lire un graphique, c'est retrouver les coordonnees d'un point et interpréter la pente dans la situation."
  "|Resoudre f(x) = k revient a chercher les antecedents de k, graphiquement ou par le calcul."
  "|En design, ces fonctions modelisent une echelle, un devis ou l'evolution d'une cote."),
[QC("Quelle est l'image de 2 pour f(x) = 3x + 1 ?", "5~6~7~9", 2,
     "f(2) = 3 × 2 + 1 = 7."),
 QC("Dans f(x) = a x + b, que represente a ?", "L'ordonnée a l'origine~Le coefficient directeur~L'image de 0~L'ensemble de definition", 1,
     "a est le coefficient directeur, c'est-a-dire le taux de variation de la fonction."),
 QC("Quelle fonction est lineaire ?", "f(x) = 2x + 5~f(x) = 2x~f(x) = x²~f(x) = 1/x", 1,
     "Une fonction lineaire est de la forme f(x) = a x, sans terme constant."),
 QC("Quelle est la representation graphique d'une fonction affine ?", "Une parabole~Une droite~Un cercle~Une hyperbole", 1,
     "Le graphique d'une fonction affine est toujours une droite."),
 QC("Si a < 0, la fonction affine est...", "Croissante~Decroissante~Constante~Indeterminee", 1,
     "Un coefficient directeur negatif donne une fonction decroissante."),
 QC("Quel point la droite d'equation y = 2x + 3 coupe-t-elle l'axe des ordonnees ?", "(0, 2)~ (0, 3)~ (3, 0)~ (2, 0)", 1,
     "A x = 0, y = b = 3 : le point est (0, 3)."),
 QC("Resoudre f(x) = k revient a chercher...", "Les images de k~Les antecedents de k~La pente~L'ordonnée a l'origine", 1,
     "On cherche les valeurs de x telles que f(x) prenne la valeur k."),
 QT("Une impression coute 12 euros plus 0,30 euro par page. Modele le cout total et calculer celui de 40 pages.",
    "On definit C(n) = 12 + 0,30 n, ou n est le nombre de pages. C est une fonction affine de coefficient directeur 0,30 et d'ordonnée a l'origine 12 : la valeur 12 represente le cout fixe de mise en route et 0,30 le cout marginal par page. Pour n = 40, C(40) = 12 + 0,30 × 40 = 12 + 12 = 24 euros. Graphiquement, la droite passe par (0, 12) et (40, 24) ; sa pente de 0,30 traduit l'augmentation du cout pour une page supplementaire.",
    "On attend le modele C(n) = 12 + 0,30n, le calcul a 24 euros et l'interpretation des parametres."),
 QT("Expliquer comment lire le coefficient directeur sur un graphique et l'interpretent dans un contexte de mise a l'echelle.",
    "On choisit deux points de la droite, par exemple (x1, y1) et (x2, y2), puis on calcule a = (y2 - y1) / (x2 - x1). Ce nombre est la variation de y pour une augmentation de 1 de x. Dans une mise a l'echelle ou y represente la cote sur le dessin et x la cote reelle, a est l'echelle : a = 1/50 signifie qu'un centimetre sur le plan represente 50 centimetres dans la realite. Une droite passant par l'origine indique une proportionnalite exacte, sans decalage initial.",
    "La reponse doit donner la formule de la pente et son interpretation comme echelle ou taux.")],
C("Une fonction affine relie deux grandeurs par une droite : pente et ordonnée a l'origine se lisent et s'interpretent.",
  "f(x) = a x + b · a = (f(x2) - f(x1)) / (x2 - x1)",
  "a > 0 croissante · a < 0 decroissante · b = f(0)",
  "Fonction~Associe x a f(x)~Definition~Valeurs de x~Image~Resultat f(a)~Antecedent~Valeur de x~Coefficient~Pente de la droite",
  "Identifier les deux grandeurs|Choisir la forme affine ou lineaire|Calculer a et b|Tracer la droite|Interpreter la pente dans la situation",
  "Confondre image et antecedent|Oublier le terme b|Lire la pente comme une ordonnée|Tracer une courbe au lieu d'une droite",
  "Devis~C(n) = 12 + 0,30n~Echelle~y = x/50~Croissance~a = 1,2~Decroissance~a = -0,5~Constant~a = 0",
  "Fonction affine~a x + b~Droite decalee~Fonction lineaire~a x~Droite passant par l'origine",
  "Coefficient a~Taux de variation~Ordonnee b~Valeur initiale"))

# ============================================================ MA02
add("MA02", "Dérivation et optimisation : tangente et extremum", "Maths", P12,
S("Le taux de variation moyen de f entre a et b vaut (f(b) - f(a)) / (b - a)."
  "|Le nombre dérive en a est la limite du taux de variation quand b tend vers a."
  "|Il represente le coefficient directeur de la tangente a la courbe de f au point d'abscisse a."
  "|La fonction dérivee f' associe a chaque x le nombre dérive de f en x."
  "|La dérivee de x^n est n x^(n-1) ; celle d'une constante est 0."
  "|La dérivee d'une somme est la somme des dérivees ; f' de a.f + b.g vaut a.f' + b.g'."
  "|Une fonction est croissante sur un intervalle la ou sa dérivee est positive."
  "|Un extremum local se produit en un point ou la dérivee s'annule en changeant de signe."
  "|Une tangente d'equation y = f'(a)(x - a) + f(a) donne une approximation locale de la courbe."
  "|Optimiser, c'est chercher le maximum ou le minimum d'une grandeur sous contrainte."
  "|Le calcul de l'aire maximale d'un rectangle de perimetre fixe est un exemple classique d'optimisation."
  "|En STD2A, la dérivation aide a modeliser une courbe de forme ou un cout de production."),
[QC("Que represente le nombre dérive en a ?", "L'aire sous la courbe~Le coefficient directeur de la tangente~La valeur f(a)~La distance a l'origine", 1,
     "f'(a) est la pente de la tangente a la courbe de f au point d'abscisse a."),
 QC("Quelle est la dérivee de x³ ?", "3x²~x²~3x~x⁴", 0,
     "La formule (x^n)' = n x^(n-1) donne (x³)' = 3x²."),
 QC("Quelle est la dérivee d'une constante ?", "1~0~La constante elle-meme~Indeterminee", 1,
     "Une fonction constante a un taux de variation nul, donc une dérivee nulle."),
 QC("Sur un intervalle ou f' est negative, la fonction f est...", "Croissante~Decroissante~Constante~Stationnaire", 1,
     "Une dérivee negative traduit une fonction decroissante."),
 QC("Quelle condition signale un extremum local ?", "f'(a) = 0 avec changement de signe~f(a) = 0~f'(a) > 0~f''(a) = 0", 0,
     "Un extremum correspond a une dérivee nulle avec changement de signe de f'."),
 QC("Quelle est l'equation de la tangente en a ?", "y = f(a) x + f'(a)~y = f'(a)(x - a) + f(a)~y = f'(a) x~y = f(a)(x - a) + f'(a)", 1,
     "La tangente passe par (a, f(a)) et a pour pente f'(a)."),
 QC("Que signifie optimiser une grandeur ?", "La rendre visible~Lui trouver son maximum ou son minimum~La multiplier~La mesurer au centimetre", 1,
     "Optimiser revient a rechercher un extremum, souvent sous contrainte."),
 QT("Calculer le nombre dérive de f(x) = x² - 4x + 1 en x = 3 et en donner l'interpretation graphique.",
    "On dérive terme a terme : f'(x) = 2x - 4, donc f'(3) = 6 - 4 = 2. Le nombre dérive en 3 vaut 2. Graphiquement, la tangente a la parabole au point d'abscisse 3 a pour coefficient directeur 2 : quand x croit de 1 a partir de 3, la tangente monte de 2 unites. Le point de tangence a pour ordonnee f(3) = 9 - 12 + 1 = -2, donc la tangente passe par (3, -2) et a pour equation y = 2(x - 3) - 2 = 2x - 8.",
    "On attend f'(x) = 2x - 4, f'(3) = 2, et l'equation ou l'interpretation de la tangente."),
 QT("Expliquer la demarche pour trouver l'aire maximale d'un rectangle de perimetre 20 cm.",
    "On note x et y les cotes du rectangle. Le perimetre impose 2x + 2y = 20, donc y = 10 - x. L'aire s'ecrit A(x) = x(10 - x) = 10x - x², avec 0 < x < 10. On derive : A'(x) = 10 - 2x. On resout A'(x) = 0, ce qui donne x = 5. La dérivee est positive avant 5 et negative apres : A admet donc un maximum en x = 5. Alors y = 5 et l'aire maximale vaut 25 cm², obtenue pour un carre. On verifie que la valeur appartient bien a l'intervalle et on interprete le resultat dans le contexte de fabrication.",
    "La demarche attendue : exprimer une variable, former la fonction a optimiser, dériver, annuler, discuter le signe et conclure.")],
C("La dérivee mesure une variation instantanee : elle donne la pente de la tangente et permet de trouver des extrema.",
  "f'(a) = lim (f(a+h) - f(a)) / h · tangente : y = f'(a)(x - a) + f(a)",
  "(x^n)' = n x^(n-1) · (u+v)' = u' + v' · extremum si f' change de signe",
  "Taux moyen~Variation sur un intervalle~Nombre dérive~Variation instantanee~Tangente~Droite approximative~Extremum~f' nul et signe change",
  "Definir la fonction a etudier|Calculer la fonction dérivee|Resoudre f'(x) = 0|Etudier le signe de f'|Conclure sur l'extremum et verifier la contrainte",
  "Confondre f et f'|Oublier de verifier le changement de signe|Ne pas controler l'intervalle de definition|Tracer la tangente sans passer par le point",
  "x²~f' = 2x~x³~f' = 3x²~Cout~C'(q) cout marginal~Rectangle~A'(x) = 10 - 2x~Maximum~x = 5 et aire 25",
  "Taux moyen~Sur un intervalle~Taux instantane~En un point~Limite du precedent",
  "f' positif~Fonction croissante~f' negatif~Fonction decroissante"))

# ============================================================ MA03
add("MA03", "Géométrie dans l'espace : vecteurs, droites et plans", "Maths", T,
S("Un repere orthonormal de l'espace est forme d'une origine et de trois axes perpendiculaires."
  "|Un vecteur se represente par trois coordonnees et independamment de son point d'application."
  "|La norme d'un vecteur donne sa longueur : la norme de (x, y, z) est la racine de x² + y² + z²."
  "|Le produit scalaire de deux vecteurs vaut la somme des produits de leurs coordonnees."
  "|Deux vecteurs non nuls sont orthogonaux si et seulement si leur produit scalaire est nul."
  "|Une droite vectorielle a pour vecteur directeur ; sa representation parametrique s'ecrit M = A + t.v."
  "|Un plan est definit par un point et deux vecteurs non colineaires, ou par une equation ax + by + cz + d = 0."
  "|Le vecteur (a, b, c) est normal au plan d'equation ax + by + cz + d = 0."
  "|La distance d'un point a un plan se calcule par la formule avec la valeur absolue du membre de gauche divisee par la norme du vecteur normal."
  "|Deux droites sont paralleles si leurs vecteurs directeurs sont colineaires."
  "|L'angle entre deux vecteurs se deduit du produit scalaire et de leurs normes."
  "|Ces outils fondent les codes de la perspective et le dessin technique coté."),
[QC("Quelle est la norme du vecteur (3, 4, 0) ?", "5~7~12~25", 0,
     "La norme vaut racine carree de 3² + 4² + 0² = 25, soit 5."),
 QC("Quand deux vecteurs sont-ils orthogonaux ?", "Quand leurs normes sont egales~Quand leur produit scalaire est nul~Quand ils ont la meme origine~Quand ils sont colineaires", 1,
     "L'orthogonalite se characterise par un produit scalaire nul."),
 QC("Que represente le vecteur (a, b, c) dans l'equation ax + by + cz + d = 0 ?", "Un vecteur directeur~Un vecteur normal au plan~Le point d'origine~La distance", 1,
     "Les coefficients donne un vecteur perpendiculaire au plan."),
 QC("Quelle est une representation parametrique d'une droite ?", "M = A + t.v~x² + y² = r²~ax + by = c~f(x) = ax + b", 0,
     "On part d'un point A et on ajoute un multiple d'un vecteur directeur v."),
 QC("Quelle est la condition pour qu'un point appartienne a un plan ?", "Ses coordonnees verifient l'equation du plan~Sa norme est nulle~Il est a l'origine~Son produit scalaire est nul", 0,
     "Un point appartient au plan si ses coordonnees satisfont ax + by + cz + d = 0."),
 QC("Comment reconstituer un angle entre deux vecteurs ?", "Par la difference des normes~Par le produit scalaire et les normes~Par la somme des coordonnees~Par le produit des coordonnees", 1,
     "cos(theta) = (u.v) / (norme(u) × norme(v))."),
 QC("A quoi sert la geometrie dans l'espace en dessin technique ?", "A colorier les plans~A fonder les codes perspectifs et les cotes~A ecrire le rapport~A choisir la police", 1,
     "Vecteurs, plans et distances sous-tendent la representation perspective et la cotation."),
 QT("Calculer le produit scalaire de u = (1, 2, -1) et v = (3, 0, 2), puis dire s'ils sont orthogonaux.",
    "Le produit scalaire vaut 1×3 + 2×0 + (-1)×2 = 3 + 0 - 2 = 1. Comme ce resultat est non nul, les deux vecteurs ne sont pas orthogonaux. Leur angle est aigu puisque le produit scalaire est positif : cos(theta) = 1 / (racine(6) × racine(13)), soit un angle proche de 83 degrees. Pour etre orthogonaux, il aurait fallu que la somme des produits des coordonnees soit exactement nulle, par exemple avec v = (2, -1, 0).",
    "On attend le calcul 3 + 0 - 2 = 1 et la conclusion d'absence d'orthogonalite."),
 QT("Expliquer comment un vecteur normal permet de calculer la distance entre un point et un plan.",
    "Soit le plan d'equation ax + by + cz + d = 0 et P un point de coordonnees (x0, y0, z0). On evalue S = a x0 + b y0 + c z0 + d. Si S = 0, le point est dans le plan et la distance est nulle. Sinon, on divise la valeur absolue de S par la norme du vecteur normal (a, b, c) : dist(P, plan) = |S| / racine(a² + b² + c²). Le denominateur ramene la mesure a une unité de longueur, car le vecteur n'est pas necessairement unitaire. Cette formule sert, par exemple, a verifier l'ecartement d'une paroi par rapport a un plan de facade dans un projet d'architecture interieure.",
    "On attend la formule, le role de la norme du vecteur normal et une interpretation concrete.")],
C("La geometrie dans l'espace munit le dessin d'outils de mesure : vecteurs, produits scalaires, plans et distances.",
  "u.v = x1x2 + y1y2 + z1z2 · orthogonaux si u.v = 0",
  "norme(u) = racine(x² + y² + z²) · plan : ax + by + cz + d = 0",
  "Vecteur~Trois coordonnees~Independant du point~Norme~Longueur du vecteur~Racine des carres~Produit scalaire~Somme des produits~Orthogonalite~Produit nul",
  "Placer le probleme dans un repere|Ecrire les coordonnees des vecteurs|Calculer produit scalaire ou norme|Traduire parallele ou orthogonal|Conclure par la formule adaptee",
  "Confondre point et vecteur|Oublier la valeur absolue dans la distance|Utiliser un vecteur nul comme directeur|Ne pas verifier l'appartenance au plan",
  "Vecteur (3,4,0)~Norme 5~Vecteurs (1,2,-1) et (3,0,2)~Produit 1~Plan x+y+z=3~Normal (1,1,1)~Perspective~Fuite et point de vue",
  "Vecteur directeur~Porte la droite~Vecteur normal~Perpendiculaire au plan",
  "Colineaires~Paralleles~Orthogonaux~Perpendiculaires"))

# ============================================================ MA04
add("MA04", "Statistiques descriptives : indicateurs et graphiques", "Maths", T,
S("Une population est l'ensemble etudie ; un echantillon en est une partie representatif."
  "|Une variable qualitative decrit une categorie ; une variable quantitative prend des valeurs numeriques."
  "|L'effectif est le nombre d'occurrences d'une valeur ; la frequence est l'effectif divise par l'effectif total."
  "|La moyenne est la somme des valeurs divisee par l'effectif."
  "|La mediane est la valeur qui partage la serie rangee en deux moities."
  "|Les quartiles Q1 et Q3 decoupent la serie en quatre parties ; l'ecart interquartile vaut Q3 - Q1."
  "|L'etendue est la difference entre la valeur maximale et la valeur minimale."
  "|La variance et l'ecart-type mesurent la dispersion autour de la moyenne."
  "|L'histogramme represente des classes contigues par des rectangles de surface proportionnelle a l'effectif."
  "|Le diagramme circulaire montre la repartition des frequences en pourcentages."
  "|La boite a machoires resume mediane, quartiles et valeurs extremes ; elle aide a detecter des valeurs aberrantes."
  "|Une lecture critique verifie l'echelle, l'origine et le biais d'echantillonnage avant de conclure."),
[QC("Quelle est la mediane de la serie 2, 3, 5, 9, 10 ?", "3~5~9~6", 1,
     "La serie rangee compte cinq valeurs : la mediane est la troisieme, soit 5."),
 QC("Quelle variable est qualitative ?", "La taille en cm~La couleur d'un produit~Le prix~Le nombre de pages", 1,
     "La couleur est une categorie, donc une variable qualitative."),
 QC("Comment calcule-t-on une frequence ?", "Effectif total divise par effectif~Effectif divise par effectif total~Moyenne divisee par 2~Maximum moins minimum", 1,
     "La frequence est l'effectif de la classe divise par l'effectif total."),
 QC("Quel indicateur mesure la dispersion autour de la moyenne ?", "La mediane~L'ecart-type~Le minimum~La frequency", 1,
     "L'ecart-type, racine de la variance, quantifie la dispersion."),
 QC("Que represente un histogramme ?", "Des categories sont representees par des camemberts~Des classes contigues par des rectangles~Une courbe de tendance~Un nuage de points", 1,
     "L'histogramme utilise des rectangles dont la surface represente l'effectif de chaque classe."),
 QC("Quel reseau de droite resume mediane, quartiles et extremes ?", "Le diagramme circulaire~La boite a machoires~Le tableau de frequences~La courbe de Gauss", 1,
     "La boite a machoires, ou box-plot, affiche ces cinq nombres resume."),
 QC("Quel biais faut-il verifier avant de conclure sur un sondage ?", "La couleur du graphique~La representativite de l'echantillon~Le nombre de pages du rapport~La police utilisee", 1,
     "Un echantillon non representatif rend les resultats non generalisables."),
 QT("Calculer la moyenne et l'ecart-type de la serie 2, 4, 4, 6.",
    "La moyenne vaut (2 + 4 + 4 + 6) / 4 = 16 / 4 = 4. Les ecarts a la moyenne sont -2, 0, 0 et 2 ; leurs carres valent 4, 0, 0 et 4, dont la somme est 8. La variance est 8 / 4 = 2 et l'ecart-type est la racine carree de 2, soit environ 1,41. La mediane vaut 4 et l'etendue vaut 6 - 2 = 4. Ces indicateurs montrent une serie centree sur 4 avec une dispersion moderee.",
    "On attend moyenne = 4, variance = 2 et ecart-type = racine(2) environ 1,41."),
 QT("Expliquer pourquoi deux graphiques peuvent donner des impressions differentes des memes donnees.",
    "Deux graphiques des memes donnees peuvent tromper par le choix de l'echelle des axes, par une origine non nulle, par la largeur des barres ou par l'ordre des categories. Un axe des ordonnees tronque exagere les variations ; un diagramme circulaire sans ordre cache les petites categories ; une image 3D fausse la comparaison des surfaces. Il faut aussi verifier la taille de l'echantillon, la facon dont les classes sont construites et la presence de valeurs aberrantes. En design de donnees, la responsabilite du createur est de choisir une representation fidèle, lisible et explicitement legende.",
    "La reponse doit citer echelle, origine, classes, legendre et biais, puis rappeler l'ethique de la dataviz.")],
C("La statistique descriptive resume une serie par des indicateurs et la rend visible par des graphiques : toujours verifier la representation.",
  "Moyenne = somme des valeurs / effectif",
  "frequence = effectif / total · etendue = max - min · ecart-type = racine(variance)",
  "Moyenne~Valeur centrale~Sensible aux extremes~Mediane~Valeur centrale rangee~Robuste~Ecart-type~Dispersion~Racine de la variance",
  "Delimiter la population et l'echantillon|Trier la serie|Calculer moyenne et mediane|Calculer dispersion et quartiles|Choisir un graphique fidele et le legender",
  "Confondre moyenne et mediane|Oublier de trier avant la mediane|Tronquer l'origine d'un axe|Generaliser a partir d'un echantillon biaise",
  "Serie 2 4 4 6~Moyenne 4~Ecart-type~Environ 1,41~Classe~Effectif et frequence~Boite~Q1 mediane Q3~Sondage~Representativite a verifier",
  "Moyenne~Sensible aux valeurs extremes~Mediane~Resiste aux extremes",
  "Histogramme~Classes contigues~Diagramme circulaire~Parts en pourcentage"))

# ============================================================ MA05
add("MA05", "Suites numériques : récurrence et modélisation", "Maths", T,
S("Une suite est une famille de nombres indexee par les entiers naturels."
  "|Le terme general u(n) donne la valeur du terme de rang n."
  "|Une suite arithmetique verifie u(n+1) = u(n) + r, ou r est la raison."
  "|Son terme general s'ecrit u(n) = u(0) + n r."
  "|Une suite geometrique verifie u(n+1) = q u(n), ou q est la raison."
  "|Son terme general s'ecrit u(n) = u(0) × q^n."
  "|Une suite definie par recurrence peut melanger les deux : u(n+1) = a u(n) + b."
  "|Une suite est croissante si u(n+1) superieure a u(n) pour tout n, decroissante dans le cas contraire."
  "|Une suite geometrique converge vers 0 si la valeur absolue de q est strictement inferieure a 1."
  "|La somme des termes d'une suite arithmetique s'ecrit n multiplie par la moyenne du premier et du dernier terme."
  "|Les interets composes et l'amortissement sont modelises par des suites geometriques."
  "|Ces suites decrivent la croissance d'une production ou la decroissance d'un stock de matiere."),
[QC("Dans une suite arithmetique, que represente r ?", "Le premier terme~La raison, ecart constant~Le rang~La somme", 1,
     "La raison r est l'ecart constant entre deux termes consecutifs."),
 QC("Quel est le terme general d'une suite geometrique de premier terme u0 et de raison q ?", "u(n) = u0 + n q~u(n) = u0 × q^n~u(n) = q × n~u(n) = u0^n × q", 1,
     "On multiplie le premier terme par la raison elevee a la puissance n."),
 QC("Une suite geometrique de raison q = 0,8 converge-t-elle ?", "Non~Oui, vers 0~Oui, vers 1~Vers l'infini", 1,
     "Si |q| < 1, les termes tendent vers 0."),
 QC("Que decrit u(n+1) = a u(n) + b ?", "Une suite arithmetique pure~Une recurrence affine du premier ordre~Une suite constante~Une fonction dérivee", 1,
     "Chaque terme depend du precedent de facon affine."),
 QC("Quelle est la somme des n premiers termes d'une suite arithmetique ?", "n × (u0 + u(n-1)) / 2~n × u0~u(n) - u0~n² × r", 0,
     "La somme vaut n fois la moyenne du premier et du dernier terme."),
 QC("Quel modele utilise-t-on pour des interets composes ?", "Suite arithmetique~Suite geometrique~Suite constante~Suite alternative", 1,
     "Le capital est multiplie par un facteur constant chaque periode."),
 QC("Une suite est decroissante si...", "u(n+1) est superieur a u(n)~u(n+1) est inferieur a u(n)~u(n) est nul~la raison est nulle", 1,
     "La decroissance signifie que chaque terme est strictement plus petit que le precedent."),
 QT("Une machine coute 10 000 euros et perd 20 % de sa valeur chaque annee. Donner la suite et la valeur au bout de 3 ans.",
    "On definit u(0) = 10 000 et u(n+1) = 0,8 u(n) : c'est une suite geometrique de raison q = 0,8. Son terme general est u(n) = 10 000 × 0,8^n. Au bout de 3 ans, u(3) = 10 000 × 0,8³ = 10 000 × 0,512 = 5 120 euros. La valeur a diminue de 48,8 % en trois ans. On peut aussi calculer les termes successifs : 8 000, 6 400, 5 120 euros. Ce modele sert a estimer la valeur residuelle d'un equipement de production.",
    "On attend la recurrence, le terme general et le calcul exact a 5 120 euros."),
 QT("Expliquer la difference entre suite arithmetique et suite geometrique et donner un exemple de design pour chacune.",
    "Dans une suite arithmetique, on ajoute une raison constante a chaque terme : u(n) = u0 + n r. La croissance est lineaire et la representation graphique est une droite. Par exemple, l'ajout de 5 cm a chaque module d'une etagere donne des hauteurs 20, 25, 30, 35 cm. Dans une suite geometrique, on multiplie par une raison constante : u(n) = u0 × q^n. La croissance est exponentielle si q > 1, decroissante si 0 < q < 1. Par exemple, une serie de tirages ou chaque niveau reduit la taille d'un motif de moitie donne 80, 40, 20, 10 mm. La distinction est essentielle pour prevoir une quantite de matiere ou un cout.",
    "On attend les deux formules, la nature lineaire/exponentielle et un exemple concret pour chaque.")],
C("Les suites modelisent une evolution discrete : on ajoute une raison (arithmetique) ou on multiplie (geometrique).",
  "Arithmetique : u(n) = u0 + n r · Geometrique : u(n) = u0 × q^n",
  "recurrence : u(n+1) = a u(n) + b · convergence si |q| < 1",
  "Suite arithmetique~Ecart constant~Croissance lineaire~Suite geometrique~Facteur constant~Croissance exponentielle~Raison~Pas ou facteur~Terme general~Formule explicite",
  "Identifier le premier terme|Determiner la raison|Choisir arithmetique ou geometrique|Ecrire le terme general|Calculer le terme demande et interpreter",
  "Confondre raison additive et multiplicative|Oublier l'indice de depart|Croire qu'une suite geometrique diverge toujours|Ne pas verifier |q| < 1",
  "Machine~u(n) = 10000 × 0,8^n~Etageres~20 + 5n~Motif~80 × 0,5^n~Interets~Capital × 1,03^n~Stock~Decroissance geometrique",
  "Suite arithmetique~On ajoute r~Droite~Suite geometrique~On multiplie par q~Courbe exponentielle",
  "q superieur a 1~Croissance~q entre 0 et 1~Decroissance vers zero"))

# ============================================================ HG01
add("HG01", "Histoire des arts et des techniques : repères chronologiques", "HGGS", T,
S("L'histoire des arts et des techniques situe les oeuvres dans le temps et dans leur societe."
  "|La prehistoire voit apparaitre les outils de pierre, le feu et les premieres representations."
  "|L'antiquite grecque et romaine developpe l'architecture, la statuaire et les techniques de construction."
  "|Le Moyen Age est marque par l'architecture romane puis gothique, la taille de la pierre et les vitraux."
  "|La Renaissance redecouvre l'antiquite, la perspective lineaire et le dessin d'architecture."
  "|Le classicisme puise dans l'ordre, la symmetrie et la raison ; le baroque privilégie le mouvement et la lumiere."
  "|La revolution industrielle transforme les procedes de fabrication et les modes de vie au XIXe siecle."
  "|L'impressionnisme, le cubisme et les avant-gardes rompent avec les conventions academiques."
  "|Le design industriel nait au XXe siecle de la rencontre entre art, technique et production de serie."
  "|Une meme periode peut voir cohabiter des courants opposes : il faut eviter le repertoire lineaire simpliste."
  "|Un repere chronologique doit toujours etre associe a un contexte politique, social, economique et technique."
  "|En STD2A, cette culture permet de choisir et de justifier des references dans un projet."),
[QC("Quel procede caracterise l'architecture gothique ?", "Le dome et la coupole~L'arc brise et le vitrail~La colonne dorique~Le beton arme", 1,
     "L'arc brise, la voulte sur croisee d'ogives et le vitrail sont des marqueurs du gothique."),
 QC("Quelle invention est associee a la Renaissance dans le domaine du dessin ?", "La perspective lineaire~Le collage~La photographie~Le cube de Rubik", 0,
     "La perspective lineaire codifie la representation de l'espace au XVe siecle."),
 QC("Quel courant privilege le mouvement, le contraste et la lumiere ?", "Le classicisme~Le baroque~Le néoclassicisme~Le minimalisme", 1,
     "Le baroque se distingue par le dynamisme, le clair-obscur et le faste."),
 QC("Quel evenement transforme les procedes de fabrication au XIXe siecle ?", "La Revolution francaise~La revolution industrielle~La Renaissance~La guerre froide", 1,
     "La revolution industrielle introduit la machine a vapeur et la production de serie."),
 QC("Quel mouvement rompt avec la representation academique au debut du XXe siecle ?", "Le cubisme~Le classicisme~Le romantisme~Le gothique", 0,
     "Le cubisme deconstruit les formes et refuse la perspective unique."),
 QC("Quelle est la bonne methode pour dater une oeuvre ?", "Se fier uniquement au style~La situer avec son contexte historique et technique~La comparer a une photo~Lire uniquement le titre", 1,
     "Le style doit etre recoupe avec les faits historiques, sociaux et techniques."),
 QC("Pourquoi etudier l'histoire des techniques en design ?", "Pour copier les formes anciennes~Pour comprendre les choix et les contraintes des createurs~Pour eviter toute innovation~Pour choisir une couleur", 1,
     "Elle eclaire les rapports entre besoin, materiau, procede et forme."),
 QT("Expliquer comment le passe d'une technique éclaire un projet de design contemporain.",
    "Connaitre l'histoire d'une technique permet de comprendre pourquoi une forme existe et quels problemes elle resolvait. Par exemple, le cannage ou le pliage du bois repondent a des contraintes de materiau et de transport ; les reprendre aujourd'hui, c'est faire un choix technique et culturel, pas seulement decoratif. Cette connaissance aide aussi a eviter les contresens : une forme issue d'un procede industriel de serie ne se transpose pas tel quelle dans l'artisanat. Enfin, elle fournit des references argumentees pour justifier une orientation devant un commanditaire, en montrant la filiation et les ecarts du projet.",
    "On attend le lien entre technique, forme et contexte, ainsi que l'usage argumentatif des references."),
 QT("Construire une chronologie courte de l'objet imprime, de Gutenberg a nos jours.",
    "Vers 1450, Gutenberg met au point l'imprimerie a caracteres mobiles en Europe, ce qui accelere la diffusion des textes. Au XIXe siecle, la lithographie puis les procedes mecaniques permettent l'illustration et l'affiche. Au XXe siecle, l'offset domine l'impression industrielle et le design graphique se professionalise. A la fin du XXe siecle, l'infographie et l'impression numerique rapprochent conception et production. Aujourd'hui, le numerique et l'impression a la demande modifient les metiers du livre et de l'edition. A chaque etape, le changement technique a transforme les formes, les usages et les professions.",
    "La chronologie doit respecter l'ordre et relier chaque innovation a une consequence culturelle ou professionnelle.")],
C("L'histoire des arts et des techniques relie les formes a leur contexte : une oeuvre se date et s'explique par son epoque.",
  "Oeuvre = forme + technique + contexte historique",
  "Renaissance : perspective · XIXe : industrialisation · XXe : avant-gardes et design",
  "Prehistoire~Outils et premieres images~Antiquite~Ordre et architecture~Moyen Age~Pierre et vitrail~Renaissance~Perspective et dessin",
  "Observer l'oeuvre et ses caracteres|La situer dans le temps|Identifier le contexte politique et social|Relier forme et technique|Comparer avec d'autres references",
  "Reduire une periode a un seul style|Copier une forme sans connaitre son usage|Ignorer le contexte social|Confondre courant artistique et mouvement politique",
  "Gothique~Arc brise et lumiere~Renaissance~Perspective lineaire~Baroque~Mouvement et contraste~Cubisme~Formes deconstruites~Design industriel~Serie et fonction",
  "Classicisme~Ordre et symmetrie~Baroque~Mouvement et exces",
  "Artisanat~Piece unique~Industrie~Production de serie"))

# ============================================================ HG02
add("HG02", "Révolutions industrielles et mutations du travail", "HGGS", T,
S("La premiere revolution industrielle, XVIIIe-XIXe siecles, repose sur la vapeur, le textile et le fer."
  "|La deuxieme, a la fin du XIXe siecle, ajoute l'electricite, l'acier, la chimie et les moteurs."
  "|La troisieme revolution, apres 1945, introduit l'informatique, l'automatisation et l'electronique."
  "|La quatrieme, en cours, associe numerique, donnees, intelligence artificielle et robotique."
  "|La mechanisation modifie les gestes et la division du travail."
  "|Le taylorisme rationalise les taches ; le fordisme generalise la chaine de montage et la production de masse."
  "|L'urbanisation accompagne l'industrialisation et fait naitre de nouvelles classes sociales."
  "|Les conditions de travail ont suscite des luttes, des syndicats et des legislations sociales."
  "|L'artisanat, la manufacture et l'industrie sont trois modes de production distincts."
  "|Le design industriel nait de la necessite de concilier fonction, production de serie et attrait commercial."
  "|La mondialisation fragmente les chaines de valeur et delocalise certaines productions."
  "|Les enjeux actuels portent sur la sobriete des procedes, la reparation et le recyclage."),
[QC("Quelle source d'energie caracterise la premiere revolution industrielle ?", "L'electricite~La machine a vapeur~Le nucleaire~Le solaire", 1,
     "La machine a vapeur est le moteur de la premiere revolution industrielle."),
 QC("Quel systeme generalise la chaine de montage ?", "Le taylorisme~Le fordisme~L'artisanat~La manufacture", 1,
     "Le fordisme organise la production de masse en chaine de montage."),
 QC("Quelle revolution introduit l'informatique et l'automatisation ?", "La premiere~La deuxieme~La troisieme~La quatrieme", 2,
     "La troisieme revolution, apres 1945, est celle de l'informatique et de l'automatisation."),
 QC("Quel est un effet social majeur de l'industrialisation ?", "La disparition des villes~L'urbanisation et de nouvelles classes sociales~Le retour au Moyen Age~La fin du commerce", 1,
     "Les usines attirent les populations et font naitre la classe ouvrier."),
 QC("Quelle difference existe-t-il entre artisanat et industrie ?", "L'artisanat produit en serie~L'industrie produit en grande serie avec des machines~Il n'y a aucune difference~L'industrie travaille sans materiau", 1,
     "L'artisanat valorise la piece unique et le geste ; l'industrie vise la serie et la standardisation."),
 QC("Quel enjeu contemporain concerne les procedes de production ?", "Leur sobriete et leur recyclabilite~Leur nombre de breves~Leur couleur~Leur titre", 0,
     "La consommation de ressources, la reparation et le recyclage sont des enjeux majeurs."),
 QC("Quel concept designe la fragmentation des chaines de production a l'echelle mondiale ?", "La mondialisation~La Renaissance~Le classisme~Le taylorisme", 0,
     "La mondialisation repartit les etapes de production entre pays et territoires."),
 QT("Expliquer en quoi la revolution industrielle a fait naitre le metier de designer industriel.",
    "Avant l'industrialisation, l'objet etait concu et fabrique par le meme artisan. La production de serie separe la conception de la fabrication : il faut dessiner a l'avance un objet qui sera reproduit des milliers de fois. Cette separation cree un nouveau role, celui de concepteur qui determine la forme, la fonction et le procede. Le designer industriel doit alors composer avec la machine, les materiaux standardises, le cout de l'outillage et les attentes du marche. C'est cette rencontre entre art, technique et economie qui donne naissance au design industriel au XXe siecle.",
    "On attend le lien separation conception/fabrication, production de serie et contraintes industrielles."),
 QT("Comparer les effets de la troisieme et de la quatrieme revolution sur les metiers du design.",
    "La troisieme revolution informatise la conception : la CAO remplace progressivement le dessin a la main, le DAO accelere la mise en page et la production devient plus rapide et plus precise. Les metiers se reorganisent autour de l'ordinateur et de nouveaux outils numeriques. La quatrieme revolution ajoute la donnee, l'intelligence artificielle, la fabrication additive et la robotique : le designer travaille avec des outils generatifs, des prototypes rapides et des objets connectes. Les comptences attendues deviennent transversales : il faut maitriser le code, les donnees, l'ethique et la collaboration avec des machines. Dans les deux cas, l'outil transforme le geste mais ne remplace pas l'intention de conception.",
    "La comparaison doit opposer CAO/DAO et donnees/IA/Fabrication additive, avec les competences associees.")],
C("Les revolutions industrielles transforment les energies, les gestes et les metiers : le design nait de cette separation entre concevoir et fabriquer.",
  "Vapeur → electricite → informatique → donnees et IA",
  "artisanat (piece unique) · manufacture · industrie (grande serie)",
  "Vapeur~Premiere revolution~Textile et fer~Electricite~Deuxieme revolution~Acier et chimie~Informatique~Troisieme revolution~Automatisation~Donnees et IA~Quatrieme revolution",
  "Situer la periode et l'energie dominante|Identifier les procedes et les machines|Observer la division du travail|Analyser les effets sociaux|Relier aux pratiques du design",
  "Confondre les quatre revolutions|Ignorer les consequences sociales|Croire que la machine supprime le concepteur|Oublier les enjeux environnementaux",
  "Machine a vapeur~XVIIIe et XIXe~Chaine de montage~Fordisme~CAO~Troisieme revolution~Impression 3D~Quatrieme revolution~Recyclage~Enjeu actuel",
  "Artisanat~Geste et piece unique~Industrie~Machine et grande serie",
  "Taylorisme~Rationalisation des taches~Fordisme~Chaine de montage"))

# ============================================================ HG03
add("HG03", "Géographie des territoires et des métropoles créatives", "HGGS", T,
S("Un territoire est un espace approprie et organise par une societe."
  "|Une metropole est un grand pole urbain qui rayonne sur un vaste espace."
  "|Le centre et la peripherie designent des zones aux fonctions et aux inegalites differentes."
  "|La gentrification est la transformation d'un quartier populaire par l'arrivee de populations plus aisees."
  "|Un cluster creatif rassemble entreprises, designers, artistes et institutions sur un meme territoire."
  "|Les tiers-lieux sont des espaces de travail et de rencontre partages, souvent reconvertis."
  "|Les reseaux de transport structurent les possibilites de rencontre et de diffusion."
  "|La mondialisation connecte les metropoles mais creuse aussi les ecarts entre territoires."
  "|La delocalisation deplace une production vers un territoire ou le cout est plus faible."
  "|Les echelles locale, nationale et globale doivent etre articulees dans l'analyse."
  "|Les systemes d'information geographique permettent de cartographier les usages et les flux."
  "|En design d'espace, la connaissance du territoire conditionne la pertinence d'un projet."),
[QC("Qu'appelle-t-on un cluster creatif ?", "Un quartier residentiel~Un rassemblement d'acteurs de la creation sur un territoire~Un type de police~Un reseau de transport", 1,
     "Le cluster creatif concentre designers, artistes, entreprises et institutions."),
 QC("Quel effet designe la gentrification ?", "La baisse des loyers~La transformation d'un quartier par l'arrivee de populations plus aisees~La delocalisation~La creation d'un tiers-lieu", 1,
     "La gentrification modifie les populations et les prix d'un quartier populaire."),
 QC("Qu'est-ce qu'un tiers-lieu ?", "Un bureau prive~Un espace partage de travail et de rencontre~Une gare~Un muse national", 1,
     "Les tiers-lieux sont des espaces communs, souvent issus de reconversion."),
 QC("Quel outil permet de cartographier les usages d'un territoire ?", "Le SIG~Le traitement de texte~La palette de couleurs~Le tableur seul", 0,
     "Un systeme d'information geographique croise donnees spatiales et attributaires."),
 QC("Quel lien existe-t-il entre transport et creativite urbaine ?", "Aucun~Les reseaux facilitent les rencontres et la diffusion~Les transports arretent les echanges~Ils remplacent les designer", 1,
     "L'accessibilite favorise les interactions et les projects collaboratifs."),
 QC("Quelle est une consequence de la mondialisation sur les territoires ?", "Une uniformisation totale~Des connexions fortes et des inegalites renforcees~La disparition des villes~La fin des reseaux", 1,
     "Les metropoles sont connectees mais les ecarts entre territoires persistent ou s'accentuent."),
 QC("Pourquoi un designer d'espace doit-il etudier le territoire ?", "Pour choisir une couleur tendance~Pour comprendre les usages, les flux et les acteurs~Pour eviter toute carte~Pour copier une autre ville", 1,
     "La pertinence d'un projet depend de sa connaissance des lieux et de leurs usagers."),
 QT("Analyser les effets positifs et negatifs d'un cluster creatif sur un quartier.",
    "Un cluster creatif attire des entreprises, des formations et des evenements : il dynamise l'economie locale, offre des emplois et favorise les rencontres entre designers et habitants. Il peut aussi entrainer une hausse des loyers, une gentrification et l'eviction des habitants initiaux, ainsi qu'une uniformisation des commerces. Les effets dependent de la gouvernance : des politiques de logement, des espaces accessibles et une concertation avec les habitants permettent de limiter les effets negatifs. Pour un designer, travailler dans un tel quartier implique donc une responsabilite sociale autant qu'une opportunite professionnelle.",
    "On attend des effets positifs et negatifs et une mention de la gouvernance ou de la concertation."),
 QT("Comment un projet de design d'espace peut-il s'adapter a un territoire donne ?",
    "On commence par une reconnaissance du site : usages, flux, luminosite, bruit, patrimoine et acteurs. On croise ces observations avec des donnees cartographiques et statistiques a l'echelle pertinente. On identifie ensuite les besoins des usagers et les contraintes reglementaires, techniques et budgetaires. On confronte plusieurs hypothèses d'amenagement, en testant leur insertion dans le contexte plutot qu'en imposant un modele universel. On presente enfin le projet avec des plans, des coupes et des vues qui montrent le lien entre l'espace propose et son territoire. Cette demarche evite le « plug-and-play » et produit un projet situe.",
    "La reponse doit suivre l'ordre observation, donnees, besoins, hypotheses et restitution contextuelle.")],
C("Un projet d'espace se construit à partir du territoire : usages, flux, acteurs et echelles determinent ses choix.",
  "Territoire = espace approprie + usages + representations",
  "centre / peripherie · cluster creatif · tiers-lieu · SIG · gentrification",
  "Metropole~Grand pole urbain~Centre~Fonctions et valeur~Peripherie~Autres usages~Tiers-lieu~Espace partage~Cluster~Acteurs de la creation",
  "Observer le site et ses usages|Croiser cartes et donnees|Identifier acteurs et contraintes|Comparer hypotheses d'amenagement|Restituer avec plans et vues",
  "Imposer un modele universel|Ignorer les habitants|Confondre echelle locale et globale|Ne voir que la tendance architecturale",
  "Cluster~Rencontres et emplois~Gentrification~Hausse des loyers~Tiers-lieu~Reconversion~SIG~Cartographie des flux~Echelle~Locale a globale",
  "Centre~Forte densite~Peripherie~Autre rythme et usages",
  "Mondialisation~Connexions~Territoire~Ancrage local"))

# ============================================================ HG04
add("HG04", "Citoyenneté et espaces publics : place, mémoire et usage", "HGGS", T,
S("L'espace public est un lieu accessible a tous, ou s'exercent la rencontre et le debat."
  "|La place est un espace collectif qui structure la vie urbaine et les usages."
  "|L'urbanisme organise les espaces, les volumes et les circulations selon des choix politiques."
  "|Le patrimoine designe les biens, les savoirs et les lieux transmis dont une societe se reconnait."
  "|La memoire collective se construit par des récits, des monuments, des musées et des pratiques."
  "|La commemoration selectionne ce qui est celebre et peut aussi exclure d'autres memories."
  "|Le musee est un lieu de conservation, de mediation et de construction du sens."
  "|L'usage reelle d'un lieu peut differer de la fonction prevue par le concepteur."
  "|Le detournement est une reappropriationcreative d'un objet ou d'un espace."
  "|L'accessibilite doit permettre a tous les usagers, y compris en situation de handicap, d'utiliser le lieu."
  "|La mixite sociale et la concertation sont des enjeux de la conception des espaces partages."
  "|En design d'espace et en scenographie, ces questions determinant la pertinence du projet."),
[QC("Qu'appelle-t-on espace public ?", "Un lieu prive clos~Un lieu accessible a tous ou s'exercent rencontre et debat~Un bureau~Un entrepot", 1,
     "L'espace public est ouvert a l'ensemble des citoyens et permet le debat."),
 QC("Que designe le patrimoine ?", "Uniquement les monuments anciens~Des biens et savoirs transmis qui fondent une identite~Les seuls musees~Les routes", 1,
     "Le patrimoine comprend des biens materiaux et immatériels transmis et reconnus."),
 QC("Quel risque est lie a la commemoration ?", "Trop de luminosite~Selectionner une memoire et en exclure d'autres~Augmenter la surface~Supprimer les usagers", 1,
     "Toute commemoration fait un choix qui peut invisibiliser d'autres recits."),
 QC("Qu'est-ce qu'un detournement d'usage ?", "Une reappropriation creative d'un lieu ou d'un objet~Une demolition~Une norme de securite~Un plan de circulation", 0,
     "Le detournement modifie l'usage prevu pour en proposer un autre."),
 QC("Quelle exigence concerne les usagers en situation de handicap ?", "La seule esthetique~L'accessibilite du lieu~Le cout minimal~L'absence de signaletique", 1,
     "L'accessibilite est une exigence ethique et souvent reglementaire de l'espace public."),
 QC("A quoi sert la concertation dans un projet d'espace ?", "A supprimer les usages existants~A associer les habitants et a enrichir le projet~A remplacer les plans~A reduire le nombre d'acteurs", 1,
     "La concertation permet d'integrer les besoins et les savoirs des usagers."),
 QC("Quel role joue un musee dans la construction de la memoire ?", "Conserver, medier et donner du sens~Vendre uniquement des objets~Effacer le passe~Remplacer l'ecole", 0,
     "Le musee conserve, presente et construit un recit avec le public."),
 QT("Expliquer pourquoi un meme lieu peut recevoir des usages differents de ceux prevus.",
    "Le concepteur imagine un usage a partir d'un besoin identifie, mais les usagers developpent des pratiques reelles qui dependent de leurs habitudes, de leurs besoins et du contexte. Un banc peut devenir un lieu de repos, de rencontre ou de jeu ; une place de marche peut etre investie par des events ou des commerces informels. Ces ecarts ne sont pas necessairement des echecs : ils revelent la vitalite du lieu et peuvent nourrir une nouvelle conception. Le designer doit donc observer les usages apres livraison, dialoguer avec les acteurs et prevoir des espaces suffisamment souples pour accueillir des appropriations.",
    "On attend la distinction usage prevu / usage reelle et la consequence pour la conception."),
 QT("Comment un projet de scénographie peut-il traiter la memoire d'un lieu sans la figer ?",
    "On commence par recueillir des sources et des temoignages contradictoires, en reconnaissant que la memoire est plurielle. On choisit ensuite un dispositif qui montre le processus plutôt qu'un.resultat unique : documents, sons, projections, objets et vides peuvent se succeder. On evite le monument unique qui impose un seul recit et on privilégie des parcours qui laissent le visiteur construire son propre sens. La scenographie doit aussi s'adapter au lieu existant, a sa lumiere et a sa circulation. Enfin, on explicite les choix de selection dans la mediation, pour rendre visible le travail de memoire plutot que de le faire passer pour une evidence.",
    "La reponse doit defendre la plurialite des memories, la mobilisation de plusieurs media et l'explicitation des choix.")],
C("L'espace public est un bien commun : sa conception engage des choix sur la memoire, l'usage et l'accessibilite.",
  "Espace public = accessibilite + usages + debat",
  "patrimoine · memoire · commemoration · detournement · concertation",
  "Espace public~Accessible a tous~Lieu de debat~Patrimoine~Bien transmis~Identite~Memoire~Recits collectifs~Usages~Pratiques reelles",
  "Recenser les usages reels et les acteurs|Etudier le patrimoine et les memories|Identifier les conflits d'usage|Concevoir des espaces souples et accessibles|Confronter le projet aux habitants",
  "Imposer un recit unique|Ignorer les usages existants|Oublier l'accessibilite|Confondre patrimoine et simple decoration",
  "Place~Rencontre urbaine~Musee~Mediation et conservation~Detournement~Reappropriation~Banc~Usage imprevu~Concertation~Decision partagee",
  "Memoire~Plurielle et construite~Commemoration~Selection officielle",
  "Usage prevu~Intention du concepteur~Usage reelle~Pratique des usagers"))

# ============================================================ AN01
add("AN01", "English for design : describing an object and its function", "Anglais", T,
S("A product description uses precise vocabulary for materials, shapes and functions."
  "|Common materials : wood, metal, plastic, glass, fabric, leather and cardboard."
  "|Common shapes : round, square, rectangular, curved, flat, thin and cylindrical."
  "|Adjectives such as lightweight, durable, flexible and recyclable qualify an object."
  "|The verb 'to be made of' identifies the material : 'The shell is made of recycled plastic'."
  "|The present simple describes a permanent function : 'It folds into a flat shape'."
  "|The passive voice is frequent : 'The handle is attached with two screws'."
  "|'It is designed to...' expresses the intention of the designer."
  "|Comparatives and superlatives compare solutions : lighter than, the most sustainable."
  "|Linkers such as 'however', 'therefore' and 'in addition' structure the description."
  "|Measurements use units : centimetres, millimetres, kilograms, grams."
  "|A good description moves from general appearance to details and then to function."),

[QC("Which material is 'cardboard' ?", "A metal~A paper-based material~A fabric~A glass", 1,
     "Cardboard is a stiff paper-based material used for packaging."),
 QC("Which sentence uses the passive voice ?", "It folds easily~It is made of aluminium~It has a round handle~It is light", 1,
     "'Is made of' is a passive structure: the object receives the action."),
 QC("What does 'durable' mean ?", "Easy to break~Able to last a long time~Very light~Made of glass", 1,
     "Durable means able to last long or resist wear."),
 QC("Which phrase expresses the designer's intention ?", "It is designed to fold~It is folding now~It folded yesterday~It folds of", 0,
     "'It is designed to + verb' states the purpose of the object."),
 QC("Which word is a shape adjective ?", "Recyclable~Cylindrical~Durable~Flexible", 1,
     "Cylindrical describes a shape; the others describe properties."),
 QC("Which linker introduces a contrast ?", "Therefore~However~In addition~Moreover", 1,
     "However signals a contrast or a reservation."),
 QC("What is the correct comparative of 'light' ?", "Light~Lighter~More light~Lightest", 1,
     "The comparative of the short adjective light is lighter."),
 QT("Describe in English a chair made of recycled wood, in four sentences.",
    "This chair is made of recycled wood. It has a curved back and four thin legs. The seat is flat and lightweight, so the chair is easy to move. It is designed to be repaired: the legs are attached with visible screws. However, it is not suitable for outdoor use because wood absorbs water.",
    "The answer should include a material, a shape, a function and at least one linker or passive form."),
 QT("Explain the difference between 'It is made of wood' and 'It is designed to last'.",
    "'It is made of wood' describes the material: the passive voice 'is made of' tells what the object consists of. 'It is designed to last' describes the intention or function: the structure 'is designed to + infinitive' explains what the designer wanted the object to do. The first sentence answers 'What is it?', the second answers 'What is it for?'. In a product sheet, both are needed: the material informs the user, and the intention gives value to the design choice.",
    "The expected answer distinguishes material (what) from intention (why), with correct structures.")],
C("A product description in English combines material, shape, property and function with precise structures.",
  "It is made of + material · It is designed to + verb",
  "present simple for function · passive for manufacturing · however/therefore for logic",
  "Material~Wood metal plastic~Shape~Round curved flat~Property~Lightweight durable recyclable",
  "Name the object and its general appearance|Give the material with 'made of'|Describe shape and details|Explain the function with 'designed to'|Add a reservation or a comparison",
  "Translate word for word from French|Forget the 's' at the present simple|Use 'it is made by' for the material|Confuse shape and property",
  "Shell~Made of recycled plastic~Handle~Attached with two screws~Seat~Flat and lightweight~Function~Designed to fold~Restriction~However, not for outdoor use",
  "Made of~Says the material~Made by~Says the producer or process",
  "Designed to~Expresses purpose~Used for~Expresses common use"))

# ============================================================ AN02
add("AN02", "Presenting a project : vocabulary of brief and critique", "Anglais", T,
S("A brief is a document that states the client's request, the context and the constraints."
  "|The client or commissioner defines the need and validates the proposal."
  "|The target audience is the group of people the product is intended for."
  "|A requirement is something the solution must satisfy ; a constraint limits the possible solutions."
  "|A prototype is a preliminary model used to test an idea."
  "|A mock-up is a static representation, often full size, used to evaluate appearance and scale."
  "|To iterate means to improve a solution through repeated cycles of testing."
  "|Feedback is information given about a work in progress to help improve it."
  "'The aim of this project is to...' is a useful opening sentence for a presentation."
  "|Signposting expressions such as 'firstly', 'then' and 'finally' guide the listener."
  "'I would suggest...' and 'What about...?' are polite ways to give a critique."
  "|A portfolio gathers the projects, the process and the results of a designer."
  "|Clear pronunciation and signposting help an international audience follow the talk."
  "|A good presentation ends by summarising choices and inviting questions."),
[QC("What is a 'brief' ?", "A final invoice~A document stating the request and constraints~A drawing tool~A type of material", 1,
     "The brief states the need, context and constraints given to the designer."),
 QC("What does 'to iterate' mean ?", "To stop the project~To improve through repeated cycles~To draw a line~To choose a colour", 1,
     "Iterating means repeating cycles of test and improvement."),
 QC("Which phrase is useful for opening a presentation ?", "By the way~The aim of this project is to...~I have no idea~It is finished", 1,
     "This sentence states the purpose clearly at the beginning."),
 QC("What is a mock-up used for ?", "To test the final budget~To evaluate appearance and scale~To replace the brief~To print the report", 1,
     "A mock-up is a static model that helps judge form and scale."),
 QC("Which expression gives a polite critique ?", "This is wrong~I would suggest another shape~It is bad~No, thanks", 1,
     "'I would suggest...' is a polite and constructive formulation."),
 QC("What is 'feedback' ?", "A payment~Information given to improve a work~A material~A type of prototype", 1,
     "Feedback is the information received to help improve a proposal."),
 QC("Which word is a signposting expression ?", "Firstly~However~Wood~Curved", 0,
     "Firstly, then and finally structure the different parts of a talk."),
 QT("Write the opening of a short presentation of a design project in English.",
    "Good morning. The aim of this project is to design a portable lamp for students. Our client asked for a light object, made of recycled materials, with a battery life of at least eight hours. I will first present the brief and the constraints, then show two prototypes, and finally explain the choice we made. Do not hesitate to ask questions at the end of the presentation.",
    "The answer should state the aim, mention the client or constraints, and use signposting."),
 QT("How can you give a constructive critique of a classmate's prototype in English?",
    "Start with a positive observation: 'The shape is clear and the proportions are balanced.' Then identify one precise point: 'The handle seems difficult to grip.' Offer an alternative with a polite structure: 'I would suggest a wider handle or a softer material.' Finish by inviting a reaction: 'What do you think about this option?' This structure separates the observation from the judgement, gives a concrete proposal and keeps the exchange respectful. It is the same attitude as in a professional design review, where feedback must be usable rather than merely negative.",
    "The expected answer includes a positive point, a precise observation, a polite suggestion and a question.")],
C("Presenting a design project in English requires a clear structure, precise vocabulary and constructive feedback formulas.",
  "The aim of this project is to... · I would suggest...",
  "brief / constraint / prototype / mock-up / iterate / feedback",
  "Brief~Client request~Constraint~Limit~Prototype~Test model~Mock-up~Static representation",
  "State the aim and the client|Present the brief and constraints|Show the prototypes in order|Explain the choices and the iterations|Invite feedback and questions",
  "Read a written text aloud|Use vague vocabulary|Criticise without a proposal|Forget to define the audience",
  "Aim~Portable lamp~Client~Students~Prototype~Two versions tested~Feedback~Handle too narrow~Iteration~Wider grip proposed",
  "Prototype~Tests a function~Mock-up~Shows appearance and scale",
  "Requirement~Must be satisfied~Constraint~Limits the solutions"))

# ============================================================ EM01
add("EM01", "Citoyenneté et engagement : institutions et valeurs", "EMC", T,
S("La citoyennete designe l'appartenance a une communaute politique et l'exercice de droits et de devoirs."
  "|La nationalite ouvre la jouissance des droits civils et politiques."
  "|Les droits fondamentaux comprennent la liberte d'expression, d'association et d'egale dignite."
  "|Les devoirs incluent le respect des lois, des autres et des biens communs."
  "|La democratie repose sur la souverainete du peuple et le vote."
  "|Le suffrage universel direct ou indirect determine la-designation des representants."
  "|L'Assemblee nationale et le Senat forment le Parlement, qui vote la loi et control le gouvernement."
  "|Le Conseil constitutionnel verifie la conformite des lois a la Constitution."
  "|L'Etat de droit impose que l'autorite publique agisse selon des regles connues et controllees."
  "|La separation des pouvoirs, souvent presentee comme un principe, est en France un equilibre entre pouvoirs."
  "|L'engagement peut etre associatif, syndical, politique ou benefole."
  "|La participation citoyenne nourrit la decision publique et la responsabilite individuelle."),
[QC("Quels sont les deux organes qui forment le Parlement francais ?", "Le gouvernement et le Conseil d'Etat~L'Assemblee nationale et le Senat~La Cour de cassation et le Conseil constitutionnel~Le President et le Premier ministre", 1,
     "Le Parlement est compose de l'Assemblee nationale et du Senat."),
 QC("Quel organe verifie la conformite d'une loi a la Constitution ?", "Le Conseil constitutionnel~Le Conseil d'Etat~La Cour des comptes~Le tribunal de commerce", 0,
     "Le Conseil constitutionnel exerce un controle de constitutionnalite."),
 QC("Qu'appelle-t-on Etat de droit ?", "Un Etat ou tout est permis au pouvoir~Un Etat ou l'autorite agit selon des regles et sous controle~Un Etat sans lois~Un Etat gouverne par les seuls élus", 1,
     "L'Etat de droit soumet le pouvoir a des regles et a un controle juridictionnel."),
 QC("Quel droit permet de s'exprimer et de publier librement ?", "Le droit de vote~La liberte d'expression~Le droit de propriete~La liberte d'aller et venir", 1,
     "La liberte d'expression est un droit fondamental, encadre par la loi."),
 QC("Quel est un exemple d'engagement associatif ?", "Voter aux elections~Devenir benevole dans une association~Signer un contrat de travail~Payer ses impots", 1,
     "Le benevolat associatif est une forme d'engagement citoyen."),
 QC("Qui vote la loi en France ?", "Le seul President~Le Parlement~Les tribunaux~Les prefets", 1,
     "La loi est votee par l'Assemblee nationale et le Senat."),
 QC("Quel principle est au coeur de la democratie ?", "La souverainete du peuple~Le pouvoir hereditaire~La diktee d'un seul~L'absence devote", 0,
     "La democratie repose sur la souverainete du peuple et le vote."),
 QT("Expliquer la difference entre un droit et un devoir du citoyen.",
    "Un droit est une faculte reconnue et protegee par le droit, comme la liberte d'expression ou le droit de vote : il permet au citoyen d'agir et d'etre protege. Un devoir est une obligation, comme respecter les lois, payer des impots ou respecter autrui : il garantit la possibilite pour tous d'exercer leurs droits. Les deux sont lies : mes droits s'arretent la ou commencent ceux des autres, et le respect des devoirs rend la liberte durable pour la communaute. En design de communication, cette exigence se traduit par le respect de la dignite des personnes representees.",
    "On attend une definition opposee, des exemples et le lien entre droits et devoirs."),
 QT("Comment un jeune peut-il s'engager dans la vie de sa cite et quels en sont les effets ?",
    "Il peut s'inscrire dans une association, participer a des conseils de quartier ou de lycee, soutenir un syndicat ou une cause, voter des qu'il a 18 ans, ou agir comme benevole. Cet engagement permet de faire entendre des besoins, d'apprendre le debat et la negotiation, et de transformer une critique en proposition concrete. Il renforce aussi la qualite des decisions publiques en apportant des points de vue vécus. Pour un futur designer, s'engager aide a comprendre les usagers et les enjeux d'un territoire, donc a concevoir des projets plus pertinents et plus responsables.",
    "On attend des formes d'engagement variees et des effets sur la decision et sur la formation civique.")],
C("La citoyennete combine des droits proteges et des devoirs : les institutions organisent leur exercice et l'engagement le rend vivant.",
  "Droits + devoirs + participation = citoyennete active",
  "Parlement : Assemblee nationale + Senat · Conseil constitutionnel · Etat de droit",
  "Citoyennete~Appartenance politique~Droit~Faculte protegee~Devoir~Obligation~Suffrage~Vote universel~Parlement~Vote de la loi",
  "Identifier le droit ou le devoir en jeu|Nommer l'institution competente|Expliquer la procedure prevue|Relier a une situation concrete|Proposer une forme d'engagement",
  "Confondre droit et devoir|Ignorer le role du Conseil constitutionnel|Croire que l'abstention est un vote|Oublier les devoirs lies aux droits",
  "Vote~Suffrage universel~Loi~Votee par le Parlement~Constitution~Controlee par le Conseil~Association~Engagement benefole~Debat~Participation",
  "Droit~Ce que l'on peut exiger~Devoir~Ce que l'on doit faire",
  "Assemblee nationale~Chambre basse~Senat~Chambre haute"))

# ============================================================ EM02
add("EM02", "Laïcité et liberté d'expression : principes et débats", "EMC", T,
S("La laicite garantit la liberte de conscience et l'absence de religion d'Etat."
  "|La loi du 9 decembre 1905 separa les Eglises et l'Etat en France."
  "|La neutralite s'impose aux agents publics dans l'exercice de leurs fonctions."
  "|Les usagers du service public sont libres de leurs convictions, dans le respect de l'ordre public."
  "|La liberte d'expression permet de dire, d'ecrire et de representer, mais elle connait des limites."
  "|L'injure, la diffamation, l'incitation a la haine et la contestation de crimes contre l'humanite sont limitees par la loi."
  "|La liberte de la presse et le droit de reponse encadrent le debat public."
  "|Les reseaux sociaux amplifient la diffusion des propos et rendent la trace des publications durable."
  "|La caricature est une forme de critique permise, qui peut aussi blesser et declencher un debat."
  "|Le respect d'autrui et le refus du harcelement sont des exigences de la vie commune."
  "|Un debat contradictoire oppose des arguments et des points de vue dans le respect des regles."
  "|En design, representer des personnes ou des symboles engage une responsabilite ethique et juridique."),
[QC("Que garantit la laicite ?", "Une religion d'Etat~La liberte de conscience et l'absence de religion officielle~L'interdiction de toute religion~Le controle des croyances", 1,
     "La laicite protege la liberte de conscience et refuse toute religion d'Etat."),
 QC("Quelle loi francaise a separa les Eglises et l'Etat ?", "La loi du 9 decembre 1905~La loi du 4 juin 2013~La Constitution de 1958~La loi du 1er fevrier 1994", 0,
     "La loi de separation du 9 decembre 1905 fonde la laicite francaise."),
 QC("A qui s'impose la neutralite dans le service public ?", "A tous les citoyens en permanence~Aux agents publics dans l'exercice de leurs fonctions~Aux seuls enseignants~Aux usagers uniquement", 1,
     "La neutralite s'impose aux agents publics, pas aux usagers dans leur vie privee."),
 QC("Laquelle de ces propos est en general limite par la loi ?", "Une critique d'une politique~Une caricature politique~L'incitation a la haine~Un avis sur un film", 2,
     "L'incitation a la haine ou a la violence est un abus de la liberte d'expression."),
 QC("Quel dispositif permet de rectifier une information publiee ?", "Le droit de reponse~Le droit de vote~La prescription~Le copyright", 0,
     "Le droit de reponse permet de répondre a une information inexacte ou attentatoire."),
 QC("Quel risque est lie aux reseaux sociaux ?", "Une diffusion rapide et une trace durable~L'absence de public~La suppression automatique de tous les messages~L'interdiction de debattre", 0,
     "La viralite et la persistance des publications posent des problemes nouveaux."),
 QC("Comment qualifier un echange ou des arguments s'opposent dans le respect des regles ?", "Un monologue~Un debat contradictoire~Une sanction~Une censure", 1,
     "Le debat contradictoire confronte des positions adverses selon des regles communes."),
 QT("Expliquer pourquoi la liberte d'expression comporte des limites.",
    "La liberte d'expression est un droit fondamental, mais son exercice ne peut pas porter atteinte a d'autres droits ou a l'ordre public. La loi repreme notamment l'injure publique, la diffamation, l'incitation a la haine ou a la violence et la contestation de crimes contre l'humanite. Ces limites ne visent pas a interdire la critique : elles protegent la dignite des personnes et la possibilite d'un debat paisible. La question est toujours de trouver un equilibre entre la liberte de dire et le respect d'autrui, equilibre que le juge doit often preciser au cas par cas.",
    "On attend la protection des autres droits et d'ordres publics, avec des exemples d'abus."),
 QT("Quelle responsabilite pour un designer qui utilise des symboles religieux ou culturels dans une campagne ?",
    "Le designer doit d'abord identifier les symboles et comprendre leur sens pour les communautes concernees. Il verifie ensuite le contexte juridique : injure, incitation a la haine et droits de propriete intellectuelle. Il doit se demander si l'usage est respectueux, necessaire au message et justifiable devant le commanditaire et le public. En cas de doute, il propose des alternatives, documente ses choix et accepte le debat. La neutralite de l'Etat ne signifie pas l'absence de culture dans les images, mais elle impose de ne pas transformer un symbole en instrument de stigmatisation.",
    "La reponse doit traiter la connaissance des symboles, le cadre legal et la justification ethique des choix.")],
C("La laicite et la liberte d'expression protegent la conscience et le debat, tout en imposant des limites pour respecter autrui.",
  "Liberte de conscience + separation Eglises/Etat = laicite",
  "1905 · neutralite des agents · injure et incitation : limites legales",
  "Laicite~Separatation et liberte~Neutralite~Agents publics~Expression~Dire et representer~Limites~Injure et haine~Debat~Confrontation respectueuse",
  "Identifier le principe en jeu|Verifier le cadre legal et historique|Mesurer l'impact sur les personnes|Comparer les points de vue|Justifier le choix de representation",
  "Croire que la laicite interdit la religion|Confondre neutralite de l'agent et de l'usager|Penser que tout est permis sur Internet|Ignorer la sensibilite des symboles",
  "1905~Loi de separation~Usager~Libre de ses convictions~Agent~Neutralite~Reseaux~Trace durable~Caricature~Critique et debat",
  "Neutralite~Imposee a l'agent~Liberte de conscience~Protegee pour tous",
  "Critique~Admise~Injure~Limitee par la loi"))

# ============================================================ PH01
add("PH01", "Conscience et liberté : le sujet et le choix", "Philosophie", TER,
S("La conscience est la faculte de se representer soi-meme et le monde, et de se juger."
  "|La liberte designe la capacite d'agir par soi-meme, sans y etre contraint."
  "|Le libre arbitre est l'idee que le choix humain n'est pas entierement determine par des causes externes."
  "|Le determinisme soutient au contraire que tout evenement, y compris nos actes, a une cause."
  "|Kant lie la liberte a l'autonomie : se donner sa propre loi morale par la raison."
  "|Sartre affirme que l'existence precede l'essence et que l'homme est condamne a etre libre."
  "|La responsabilite est la consequence de la liberte : on repond de ses actes devant autrui et devant la loi."
  "|Une valeur est ce qui est juge important et qui oriente le choix."
  "|Le probleme philosophique se construit en confrontant une these et une objection."
  "|Une notion est un concept general qui organise le discours, comme liberte, conscience ou devoir."
  "|La morale concerne le bien et le mal ; le droit concerne le licite et l'illicite."
  "|En design, le choix d'une solution engage une part de liberte et de responsabilite."),
[QC("Quelle philosophie lie liberte et autonomie de la raison ?", "Sartre~Kant~Aristote~Benjamin", 1,
     "Kant definit la liberte comme autonomie : se donner sa loi par la raison."),
 QC("Quelle these affirme que l'existence precede l'essence ?", "Le determinisme~L'existentialisme sartrien~Le positivisme~Le stoicisme", 1,
     "Sartre resume l'existentialisme par « l'existence precede l'essence »."),
 QC("Qu'appelle-t-on determinisme ?", "La liberte absolue~La these selon laquelle tout evenement a une cause~Le refus de toute morale~Le hasard pur", 1,
     "Le determinisme affirme que les actes, comme les autres evenements, ont des causes."),
 QC("Quelle difference existe-t-il entre morale et droit ?", "Aucune~La morale juge le bien et le mal, le droit le licite et l'illicite~Le droit juge le bien, la morale la loi~La morale est ecrite, le droit ne l'est pas", 1,
     "La morale porte sur le bien et le mal, le droit sur ce qui est permis par la loi."),
 QC("Qu'est-ce qu'une valeur ?", "Un prix affiche~Ce qui est juge important et oriente le choix~Une regle de grammaire~Un type de ligne", 1,
     "Une valeur est ce qui compte pour un sujet ou une societe et guide ses decisions."),
 QC("Comment construit-on un probleme philosophique ?", "En donnant une seule opinion~En confrontant une these et une objection~En citant uniquement un auteur~En resumant un cours", 1,
     "Le probleme nait de la tension entre une affirmation et une objection."),
 QC("Pourquoi la responsabilite suit-elle la liberte ?", "Parce que l'on choisit, on peut etre juge de son choix~Parce que la loi l'impose toujours~Parce que le hasard decide~Parce que l'on n'a pas le choix", 0,
     "Etre libre implique de pouvoir repondre de ses actes."),
 QT("Expliquer la tension entre liberte et determinisme.",
    "Le determinisme affirme que nos actes ont des causes : l'education, le milieu, la biologie ou l'histoire. Si tout est cause, il semble difficile de dire que nous choisissons vraiment. Pourtant, nous faisons l'experience de la deliberation : nous hesitate, nous comparons des motifs et nous nous sentons responsables. Kant repond en distinguant l'apparence et la raison pratique : meme si le monde physiquement est determine, la raison peut se donner une loi et agir par devoir. Sartre, lui, part de la conscience pour affirmer que nous ne pouvons pas echapper au choix, meme dans l'absence de justification. Le debat porte donc sur le sens de « pouvoir faire autrement ».",
    "On attend la presentation des deux positions et une tentative de depassement ou de clarification."),
 QT("En quoi un choix de design est-il une decision philosophique ?",
    "Choisir une matiere, une forme ou une fonction, ce n'est pas seulement resoudre un probleme technique : c'est selectionner des valeurs. Retenir un materiau recyclable exprime une preference pour la durabilite ; simplifier une interface exprime une valeur d'accessibilite. Ces choix ne sont pas dictes uniquement par la demande du client : le designer exerce un jugement et peut refuser une option qu'il estime nuisible. Il devient alors responsable des effets de son projet sur les usagers et sur l'environnement. La liberte du concepteur se mesure donc a sa capacite a expliciter les valeurs qui fondent ses decisions et a en assumer les consequences.",
    "On doit relier le choix technique a des valeurs et a la responsabilite du concepteur.")],
C("La liberte est l'exercice d'un jugement autonome : elle entraine une responsabilite devant autrui et devant soi.",
  "Liberte = agir par soi-meme · Autonomie = se donner sa loi",
  "determinisme ↔ libre arbitre · Kant · Sartre · responsabilite",
  "Conscience~Se representer et se juger~Liberte~Agir par soi~Autonomie~Se donner sa loi~Determinisme~Tout a une cause",
  "Definir la notion avec precision|Formuler une these claire|Lui opposer une objection|Chercher un depassement|Illustrer par un choix concret",
  "Confondre liberte et licence|Reduire le determinisme au fatalisme|Donner une opinion sans argument|Oublier la dimension de responsabilite",
  "Kant~Liberte et devoir~Sartre~Existence avant essence~Valeur~Ce qui oriente le choix~Responsabilite~Repondre de ses actes~Design~Choix de valeurs",
  "Liberte~Peut faire autrement~Determinisme~Les causes expliquent tout",
  "Morale~Bien et mal~Droit~Licite et illicite"))

# ============================================================ PH02
add("PH02", "Art et esthétique : le beau, la technique et le goût", "Philosophie", TER,
S("L'esthetique est la reflexion sur le beau, l'art et le jugement de gout."
  "|Le beau est une valeur qui suscite une satisfaction desinteressee, selon Kant."
  "|Le jugement de gout prétend a l'universalite tout en etant ressenti subjectivement."
  "|Kant distingue l'agreeable, qui plait aux sens, du beau, qui plait par la forme."
  "|La technique, ou techne chez les Grecs, designe un savoir-faire oriente vers une fin."
  "|L'art imite la nature selon le concept de mimesis, mais il peut aussi la transformer."
  "|L'originalite et la creation distinguent l'oeuvre d'art de la simple reproduction."
  "|Benjamin analyse la perte de l'aura de l'oeuvre a l'epoque de la reproduction technique."
  "|L'industrie culturelle produit des biens standardises pour une consommation de masse."
  "|Le gout est a la fois une sensibilite personnelle et un code social acquis."
  "|Le design interroge le rapport entre fonction, beaute et usage."
  "|En STD2A, cette reflexion aide a justifier des choix plastiques plutot qu'a les subir."),
[QC("Selon Kant, qu'est-ce qui distingue le beau de l'agreeable ?", "Le beau plait aux sens, l'agreeable a la raison~Le beau plait par la forme, l'agreeable flatte les sens~Il n'y a aucune difference~L'agreeable est universel", 1,
     "Le beau est un jugement desinteresse sur la forme, l'agreeable depend de l'inclination sensible."),
 QC("Quel concept designe l' imitation de la nature dans l'art antique ?", "La techne~La mimesis~L'aura~La dialectique", 1,
     "La mimesis est le principe d'imitation du reel."),
 QC("Qu'appelle-t-on « aura » chez Walter Benjamin ?", "La luminosite d'une oeuvre~L'unicite et la presence de l'oeuvre originale~Un type de couleur~Une technique de gravure", 1,
     "L'aura designe l'unicite de l'oeuvre, fragilisee par la reproduction technique."),
 QC("Que designe l'industrie culturelle ?", "Un musee~La production standardisee de biens culturels de masse~Un atelier d'artiste~La peinture classique", 1,
     "Le concept designe la standardisation et la diffusion industrielle des oeuvres."),
 QC("Quel lien existe-t-il entre technique et art selon la notion de techne ?", "La technique est estrangere a l'art~La technique est un savoir-faire au service d'une fin~La technique interdit la creation~L'art n'a pas besoin de savoir-faire", 1,
     "La techne est un savoir-faire rationnel oriente vers une realisation."),
 QC("Quelle affirmation est compatible avec le jugement de gout kantien ?", "Le gout est purement prive~Le gout est subjectif mais prétend a l'universalite~Le gout est impose par la loi~Le gout ne peut etre discute", 1,
     "Le jugement de gout est ressenti par un sujet mais il prétend valoir pour tous."),
 QC("Pourquoi la reflexion esthetique est-elle utile a un designer ?", "Elle remplace la pratique~Elle aide a justifier les choix plastiques~Elle interdit la couleur~Elle supprime le commanditaire", 1,
     "Elle permet de donner des raisons a des preferences formelles."),
 QT("Expliquer pourquoi une meme forme peut etre jolie pour l'un et laide pour l'autre.",
    "Le jugement de gout est personnel : il depend de la sensibilite, de l'education, de la culture et des experiences de chacun. Pourtant, quand nous disons « c'est beau », nous ne parlons pas seulement de nous : nous presentons notre sentiment comme s'il devait etre partage. C'est cette pretention a l'universalite qui rend le debat esthetique possible. Les differents de gout ne prouvent pas que tout se vaut : ils montrent que la perception est situee. Le designer doit donc composer avec cette pluralite, en proposant des formes qu'il peut justifier par des criteres explicites (equilibre, proportion, appropriation de l'usage) plutot que par le seul « j'aime ».",
    "On attend la subjectivite du gout, la pretention a l'universalite et la consequence pour le design."),
 QT("La reproduction technique d'une image affaiblit-elle sa valeur esthetique ?",
    "Selon Benjamin, la reproduction technique affaiblit l'aura de l'oeuvre : l'image perd son unicite et sa presence ici et maintenant. Le tirage photographique ou le fichier numerique circule, se decontextualise et devient accessible a tous. Cela ne signifie pas la fin de l'art : la reproduction peut au contraire democratise l'acces et creer de nouveaux usages, comme l'affiche ou le design graphique. La valeur se deplace de l'objet unique vers la diffusion, le contexte et l'intention. Pour un designer graphique, cette analyse est centrale : son travail est fait pour etre reproduit, et c'est dans la qualite de cette reproduction et de sa reception que se joue sa valeur.",
    "On attend la notion d'aura, ses consequences et une application au design graphique.")],
C("L'esthetique interroge le beau et le gout : le jugement est subjectif mais prétend a l'universalite, et la technique transforme la valeur de l'oeuvre.",
  "Beau = satisfaction desinteressee · Gout = subjectivite + pretention universelle",
  "mimesis · techne · aura (Benjamin) · industrie culturelle",
  "Beau~Satisfaction desinteressee~Gout~Jugement subjectif~Techne~Savoir-faire~Aura~Unicite de l'oeuvre~Mimesis~Imitation du reel",
  "Definir les notions d'esthetique|Degager la these de l'auteur|Lui opposer une objection|Relier au contexte technique|Appliquer a un choix de design",
  "Reduire le beau au j'aime|Confondre gout et morale|Ignorer l'effet de la reproduction|Juger sans criteres explicites",
  "Kant~Beau et desinteressement~Benjamin~Aura et reproduction~Mimesis~Imitation~Industrie culturelle~Standardisation~Design~Fonction et forme",
  "Agreeable~Plait aux sens~Beau~Plait par la forme",
  "Aura~Oeuvre unique~Reproduction~Diffusion de masse"))

valider_et_ecrire(F, "std2a-mat-part-A.json")
