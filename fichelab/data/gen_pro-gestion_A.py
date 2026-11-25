# -*- coding: utf-8 -*-
"""Generateur pro-gestion-mat-part-A.json — lot A : tronc commun (20 fiches).

Français (6), Mathématiques (6), Histoire-géo (4), Anglais (2),
EMC (1), Méthodologie (1).
12 points, 9 questions corrigees (7 QCM + 2 texte), 7 blocs ordonnes, 3 SVG.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _progestion_common import S, R, QC, QT, C, build, valider_et_ecrire

F = []


def add(prefix, titre, mat, ans, points, questions, c):
    F.append(build(prefix, titre, mat, ans, points, questions, c))


# ============================================================ FR1
add("FR1", "Les figures de style et leurs effets de sens", "Français", ["2nde pro"],
S("Une figure de style est un procédé d'écriture qui s'écarte de l'expression ordinaire pour produire un effet de sens ou de rythme."
  "|La comparaison rapproche explicitement deux éléments à l'aide d'un outil : comme, tel, semblable à, ressembler à."
  "|La métaphore est une comparaison implicite : elle transfère un sens image sur un mot sans employer d'outil de comparaison."
  "|La personnification attribue des actions, des sentiments ou des paroles humains à un être inanimé ou à un animal."
  "|L'hyperbole amplifie ou atténue une réalité pour frapper l'imagination, sans prétendre à l'exactitude."
  "|La litote dit moins qu'elle ne pense pour suggérer davantage et produire un effet de modestie ou d'ironie."
  "|L'antithèse rapproche dans une même phrase deux termes opposés afin de rendre le contraste plus sensible."
  "|L'oxymore associe deux mots contradictoires dans un même groupe, créant une tension expressive."
  "|La métonymie désigne un être ou une chose par un terme qui lui est lié : la plume pour l'écrivain, le toit pour la maison."
  "|La synecdoque est une forme de métonymie qui substitue la partie au tout ou le tout à la partie."
  "|L'anaphore répète un même mot ou un même groupe en tête de plusieurs phrases ou de plusieurs vers, créant un effet d'insistance."
  "|L'analyse d'une figure se fait en trois temps : repérer l'écart, nommer la figure, interpréter son effet dans le contexte."),
[QC("Quel mot est un outil de comparaison ?", "Comme~Dont~Lequel~Pourtant", 0,
     "Comme, tel ou semblable à introduisent une comparaison explicite."),
 QC("Comment distinguer une métaphore d'une comparaison ?", "La métaphore emploie comme~La métaphore n'emploie pas d'outil de comparaison~La comparaison est toujours plus courte~Il n'y a aucune différence", 1,
     "La métaphore est une comparaison implicite, sans outil explicite."),
 QC("Que nomme-t-on dans « un silence assourdissant » ?", "Une antithèse~Une litote~Un oxymore~Une personnification", 2,
     "Deux termes contradictoires sont associés dans un même groupe : c'est un oxymore."),
 QC("La personnification consiste à…", "Répéter un mot en début de vers~Attribuer des traits humains à un inanimé~Exagérer une réalité~Dire moins pour suggérer plus", 1,
     "On prête une action ou un sentiment humain à un objet, un animal ou une abstraction."),
 QC("Quel est l'effet d'une litote ?", "Amplifier systématiquement~Suggérer davantage en disant moins~Créer un contraste~Répéter une structure", 1,
     "La litote est un procédé d'atténuation qui donne plus à penser qu'elle ne dit."),
 QC("Qu'appelle-t-on anaphore ?", "Une opposition de deux termes~Une répétition en début de phrase ou de vers~Une image sans outil~Une exagération", 1,
     "L'anaphore est une répétition placée en tête de segments successifs."),
 QC("Quelle est la bonne démarche d'analyse d'une figure ?", "Nommer seulement~Repérer, nommer, interpréter~Traduire en anglais~Supprimer la figure", 1,
     "On repère l'écart, on nomme la figure, puis on explique son effet dans le contexte."),
 QT("Analyser la figure de style dans : « Cette ville est une fourmilière en perpétuelle agitation. »",
     "On repère le mot « fourmilière », employé pour désigner la ville : c'est une métaphore, car aucun outil de comparaison n'est présent. Le transfert image associe la ville à un lieu grouillant d'activité collective et organisée. L'effet est de suggérer le mouvement, la densité humaine et une forme d'agitation mécanique, plus vivement que ne le ferait une comparaison explicite.",
     "On attend l'identification de la métaphore, l'absence d'outil, et l'interprétation de l'effet d'agitation collective."),
 QT("Distinguer comparaison, métaphore et personnification en donnant un exemple de chacune.",
     "La comparaison rapproche deux éléments avec un outil : « il court comme le vent ». La métaphore supprime l'outil : « il est le vent de l'équipe ». La personnification prête un trait humain à un non-humain : « la machine réclame une pause ». La différence porte donc sur la présence de l'outil pour les deux premières et sur le type de transfert pour la troisième.",
     "On valorise un exemple correct par figure et la formulation du critère distinctif.")],
C("Une figure de style est un écart volontaire à la langue ordinaire : on la repère, on la nomme, puis on explique son effet.",
  "Figure de style = écart + effet de sens ou de rythme",
  "Comparaison : outil explicite · métaphore : sans outil · antithèse : contraste · oxymore : contradiction",
  "Comparaison~Rapprochement explicite~comme, tel~Metaphore~Rapprochement implicite~sans outil~Oxymore~Mots contradictoires~silence assourdissant",
  "Lire la phrase lentement|Repérer le mot qui fait écart|Nommer la figure avec précision|Citer les mots concernés|Expliquer l'effet en contexte",
  "Confondre comparaison et métaphore|Nommer sans jamais interpréter|Citer un seul mot à l'appui|Inventer une figure inexistante",
  "Une fourmilière~Metaphore de la ville~Silence assourdissant~Oxymore~Je ne vous dis pas~Litote",
  "Comparaison~Avec un outil~comme, tel~Metaphore~Sans outil~transfert direct",
  "Antithese~Deux termes opposes~contraste~Oxymore~Contradiction interne~tension"))

# ============================================================ FR2
add("FR2", "L'argumentation : thèse, arguments et raisonnement", "Français", ["2nde pro"],
S("Un texte argumentatif vise à convaincre ou à persuader en présentant une prise de position et des raisons de l'adopter."
  "|La thèse est l'opinion défendue par l'auteur ; l'antithèse est l'opinion adverse, souvent mentionnée pour être discutée."
  "|Un argument est une raison générale qui soutient la thèse ; un exemple est un cas concret qui l'illustre et la rend crédible."
  "|Le plan Argument + Exemple + Mini-conclusion forme un paragraphe argumentatif complet et autonome."
  "|Les connecteurs logiques organisent le raisonnement : d'abord, ensuite, donc, car, cependant, par conséquent."
  "|La déduction part d'une règle générale pour aboutir à une conclusion particulière (si A alors B)."
  "|L'induction part de faits particuliers pour dégager une régularité ou une règle générale."
  "|L'analogie transfère un raisonnement d'un domaine connu vers un domaine moins connu."
  "|L'objection présente une objection possible, et la réfutation la discute pour renforcer la thèse."
  "|La modalisation exprime le degré d'adhésion de l'auteur par des modalisateurs : sans doute, il est clair, peut-être."
  "|Les appels à la raison (logos), à l'émotion (pathos) et à la confiance dans l'auteur (ethos) sont les trois registres de persuasion."
  "|La conclusion reprend la thèse, répond à la problématique et peut ouvrir sur une question plus large."),
[QC("Quel rôle joue un exemple dans un paragraphe argumentatif ?", "Il remplace l'argument~Il illustre et rend crédible l'argument~Il conclut le texte~Il présente l'antithèse", 1,
     "L'exemple est un cas concret au service d'une raison générale."),
 QC("Quel connecteur introduit une opposition ?", "Donc~Car~Cependant~Ensuite", 2,
     "Cependant marque l'opposition ou la concession ; donc et car marquent la conséquence et la cause."),
 QC("La déduction part…", "De faits particuliers~D'une règle générale~D'une analogie~D'une émotion", 1,
     "La déduction applique une règle générale à un cas particulier."),
 QC("Qu'est-ce qu'une réfutation ?", "Une thèse adverse~La réponse apportée à une objection~Un exemple chiffré~Une conclusion", 1,
     "On réfute en discutant l'objection pour défendre sa thèse."),
 QC("Quel modalisateur exprime une adhésion prudente ?", "Il est évident que~Sans doute~Bien entendu~Assurément", 1,
     "« Sans doute » atténue l'affirmation ; les autres marquent une certitude."),
 QC("À quel registre appartient l'appel à la confiance dans l'auteur ?", "Logos~Pathos~Ethos~Chronos", 2,
     "L'ethos construit l'image de celui qui parle et sa crédibilité."),
 QC("Que contient la conclusion d'un texte argumentatif ?", "Un nouvel exemple~La reprise de la thèse et la réponse à la problématique~Une simple liste d'arguments~La présentation de l'auteur", 1,
     "La conclusion synthétise et répond à la question posée, avec une éventuelle ouverture."),
 QT("Construire un paragraphe argumentatif sur la généralisation du télétravail, en appliquant le modèle Argument + Exemple + Mini-conclusion.",
     "Argument : le télétravail peut accroître la productivité parce qu'il réduit les temps de déplacement et les interruptions. Exemple : dans une étude interne, des salariés ayant supprimé une heure de trajet quotidien ont traité davantage de dossiers sur la même période. Mini-conclusion : le gain de temps constitue donc un avantage réel, à condition d'organiser autrement la coordination. Le paragraphe reste centré sur une seule idée et enchaîne à l'aide de connecteurs explicites.",
     "On attend une idée directrice, un exemple concret, une mini-conclusion et des connecteurs logiques."),
 QT("Expliquer la différence entre convaincre et persuader, puis dire comment les trois registres y contribuent.",
     "Convaincre s'adresse à la raison : on propose des arguments et des exemples pour démontrer une thèse (logos). Persuader s'adresse davantage à la sensibilité et à l'adhésion : on suscite une émotion (pathos) et on s'appuie sur la crédibilité de l'orateur (ethos). Un même texte combine les trois registres : des chiffres rassurent la raison, une image touche l'auditoire, et la stature de l'auteur inspire confiance. L'équilibre dépend du public visé et de l'objectif du discours.",
     "On distingue raison et adhésion, puis on définit logos, pathos et ethos avec un effet pr?cis.")],
C("L'argumentation organise une prise de position en raisons appuyées par des exemples, avec une méthode explicite.",
  "Paragraphe = Argument + Exemple + Mini-conclusion",
  "Deduction : regle general → cas · Induction : cas → regle · Logos, pathos, ethos",
  "These~Opinion defendue~Position de l'auteur~Argument~Raison generale~Parce que~Exemple~Cas concret~Par exemple",
  "Lire la question et choisir sa these|Degager deux ou trois arguments solides|Illustrer chaque argument|Enchainer avec des connecteurs|Repondre et ouvrir en conclusion",
  "Donner une opinion sans raison|Confondre argument et exemple|Multiplier les connecteurs sans logique|Negliger l'objection adverse",
  "Teletravail~Gain de temps~Productivite~Exemple d'entreprise~Objection~Coordination a organiser",
  "Convaincre~Raison et logos~Arguments~Persuader~Emotion et ethos~Pathos",
  "Deduction~Du general au particulier~Induction~Du particulier au general"))

# ============================================================ FR3
add("FR3", "Le récit et le point de vue narratif", "Français", ["2nde pro"],
S("Un récit rapporte une suite d'événements réels ou fictifs ; le narrateur est celui qui les raconte, ce qui n'est pas nécessairement l'auteur."
  "|Dans un récit à la première personne, le narrateur est un personnage de l'histoire et ne connaît que ce qu'il voit ou ressent."
  "|Dans un récit à la troisième personne, le narrateur est extérieur ; il peut être omniscient et savoir tout des personnages."
  "|La focalisation interne adopte le point de vue d'un personnage : le lecteur ne sait que ce qu'il perçoit."
  "|La focalisation externe montre seulement les paroles et les gestes visibles, sans accès aux pensées."
  "|La focalisation omnisciente donne accès aux pensées, aux souvenirs et à l'avenir des personnages."
  "|L'ordre du récit peut être chronologique ou inversé par des analepses (retours en arrière) et des prolepses (anticipations)."
  "|La durée narrative joue sur la pause (description), la scène (dialogue), le résumé et l'ellipse (passage sous silence)."
  "|Le personnage se définit par ses paroles, ses actes, son aspect physique et le regard des autres personnages."
  "|La description suspend l'action pour peindre un lieu, un objet ou un être, et crée une atmosphère."
  "|Le dialogue donne l'illusion de la parole vivante ; le style indirect libre mêle discours du personnage et narration."
  "|Étudier un récit, c'est repérer qui voit, qui parle, dans quel ordre et avec quelle distance."),
[QC("Qui est le narrateur ?", "L'auteur du livre~Celui qui raconte l'histoire~Le personnage principal~Le lecteur", 1,
     "Narrateur et auteur sont deux notions distinctes : le narrateur est la voix du récit."),
 QC("Quelle focalisation adopte le point de vue d'un personnage ?", "Externe~Omnisciente~Interne~Zéro", 2,
     "La focalisation interne limite le savoir narratif à la perception d'un personnage."),
 QC("Qu'appelle-t-on analepse ?", "Une anticipation~Un retour en arrière~Une description~Un dialogue", 1,
     "L'analepse est un retour en arrière ; la prolepse est une anticipation."),
 QC("Quel procédé passe sous silence une partie de l'action ?", "La pause~La scène~L'ellipse~Le résumé", 2,
     "L'ellipse supprime un intervalle de temps ; la pause, elle, arrête le récit."),
 QC("Le style indirect libre…", "Est toujours entre guillemets~Mêle discours du personnage et narration~Est réservé au théâtre~Supprime les verbes", 1,
     "Il conserve les paroles du personnage sans les introduire par un verbe de dire."),
 QC("Comment nomme-t-on le fait de décrire un lieu pour créer une atmosphère ?", "Une ellipse~Une description~Une prolepse~Une antithèse", 1,
     "La description suspend l'action et construit une ambiance."),
 QC("Dans un récit à la première personne, le narrateur…", "Sait tout des autres~Est un personnage de l'histoire~Est toujours l'auteur~Ne parle jamais de lui", 1,
     "Le narrateur interne ne connaît que son propre point de vue."),
 QT("Identifier le point de vue d'un extrait où le narrateur dit : « Je n'avais rien vu venir ; la porte claquait déjà. »",
     "L'emploi de « je » indique un narrateur-personnage, donc une narration à la première personne. La focalisation est interne : le lecteur partage la perception limitée du personnage, qui découvre l'événement en même temps que lui. L'expression « je n'avais rien vu venir » marque l'ignorance du narrateur au moment de l'action, tandis que le récit est raconté après coup. Cette distance entre le « je » qui raconte et le « je » qui a vécu crée un effet de suspense et d'émotion.",
     "On attend : première personne, focalisation interne, limite du savoir et effet produit."),
 QT("Expliquer comment l'ordre et la durée narrative transforment un simple fait divers en récit.",
     "Un même fait peut être raconté dans l'ordre chronologique ou bouleversé par une analepse qui révèle une cause cachée : le lecteur ne reçoit pas l'information dans le même ordre et l'effet change. La durée joue aussi : une scène dialoguée ralentit le rythme et donne à voir l'émotion, tandis qu'une ellipse franchit plusieurs années en une phrase et souligne le passage du temps. Le narrateur choisit donc ce qu'il montre, ce qu'il résume et ce qu'il tait : c'est ce travail sur l'ordre et la durée qui fait du récit une construction et non un simple catalogue d'événements.",
     "On relie ordre et durée aux effets de suspense, de rythme et de sens.")],
C("Un récit se construit par le choix d'un narrateur, d'une focalisation, d'un ordre et d'un rythme.",
  "Focalisation interne = savoir limité à un personnage",
  "Analepse : retour arrière · prolepse : anticipation · ellipse : temps supprimé",
  "Narrateur~Voix qui raconte~Je ou il~Focalisation~Point de vue~Interne, externe, omnisciente~Ordre~Chronologie~Analepse",
  "Repérer la personne du narrateur|Determiner qui sait quoi|Observer l'ordre des evenements|Mesurer la duree narrative|Interpretation l'effet produit",
  "Confondre auteur et narrateur|Croire que la 3e personne est toujours omnisciente|Ignorer les retours en arriere|Raconter sans analyser",
  "Je n'avais rien vu~Focalisation interne~Porte claquait~Suspense~Analepse~Cause revelee plus tard~Ellipse~Annees franchies",
  "Focalisation interne~Savoir d'un personnage~Focalisation externe~Gestes visibles seulement",
  "Analepse~Retour en arriere~Prolepse~Anticipation"))

# ============================================================ FR4
add("FR4", "La poésie : vers, rimes et images poétiques", "Français", ["2nde pro"],
S("Le poème est un texte à part, souvent court, où le sens naît autant du rythme, des sonorités et des images que du contenu explicite."
  "|Le vers est une ligne de poème ; la strophe est un groupe de vers, souvent séparé par un blanc."
  "|L'alexandrin compte douze syllabes ; l'hexasyllabe en compte six et l'octosyllabe huit."
  "|La césure est une coupe à l'intérieur du vers ; l'enjambement prolonge une phrase d'un vers sur le suivant."
  "|La rime est la répétition d'une sonorité en fin de vers ; les rimes peuvent être croisées (ABAB), embrassées (ABBA) ou suivies (AABB)."
  "|Le rythme repose sur l'alternance des syllabes accentuées et non accentuées et sur la place de la césure."
  "|L'image poétique compare ou transfère des propriétés : métaphore, comparaison, personnification, symbole."
  "|Le sonnet est un poème de quatorze alexandrins répartis en deux quatrains et deux tercets, avec une volta après le huitième vers."
  "|Le poème en prose adopte la forme de la prose mais recherche la densité image et le rythme du poème."
  "|Le lyrisme exprime des sentiments intimes et une voix qui chante, souvent à la première personne."
  "|Les sonorités (allitérations, assonances) et les figures de style construisent une musicalité propre au texte."
  "|Commenter un poème, c'est observer la forme, repérer les images, puis relier ces choix au sens et à l'émotion."),
[QC("Combien de syllabes compte un alexandrin ?", "8~10~12~14", 2,
     "L'alexandrin comprend douze syllabes ; l'octosyllabe en compte huit."),
 QC("Qu'appelle-t-on enjambement ?", "Une coupe au milieu du vers~Une phrase qui continue au vers suivant~Une rime croisée~Une strophe de quatre vers", 1,
     "L'enjambement prolonge la phrase d'un vers sur le suivant, au-delà de la fin du vers."),
 QC("Quel schéma correspond à des rimes embrassées ?", "ABAB~ABBA~AABB~ABCABC", 1,
     "ABBA est le schéma des rimes embrassées ; ABAB est croisé et AABB suivi."),
 QC("Combien de vers contient un sonnet ?", "10~12~14~16", 2,
     "Le sonnet comporte quatorze vers : deux quatrains puis deux tercets."),
 QC("Quel est le rôle de la césure ?", "Marquer la fin du poème~Couper l'intérieur du vers~Remplacer la rime~Allonger la strophe", 1,
     "La césure est une coupe interne qui structure le rythme du vers."),
 QC("Quel poème prend la forme de la prose ?", "Le sonnet~Le poème en prose~L'alexandrin~La ballade", 1,
     "Le poème en prose n'a pas de vers mais garde la densité et l'image poétique."),
 QC("Que désigne une assonance ?", "Répétition de consonnes~Répétition de voyelles~Rime en fin de vers~Nombre de syllabes", 1,
     "L'assonance répète des sons voyelles ; l'allitération répète des consonnes."),
 QT("Commenter la musicalité d'un vers à partir de la rime, de la césure et de l'enjambement.",
     "On commence par compter les syllabes et repérer le mètre. On situe ensuite la césure, qui divise le vers en deux hémistiches et organise une respiration. On relève le schéma des rimes, qui crée une attente et un retour de son, puis on observe un éventuel enjambement qui fait glisser la phrase d'un vers à l'autre et modifie le rythme. On relie enfin ces observations à l'effet produit : une césure marquée et des rimes régulières donnent un effet de pose et d'équilibre, tandis qu'un enjambement accélère le mouvement et traduit une émotion plus vive.",
     "On attend le relevé des faits de versification puis leur interprétation en termes de rythme et de sens."),
 QT("Distinguer image poétique et figure de style, et expliquer leur rôle dans un poème.",
     "La figure de style est un procédé général de la langue (métaphore, personnification, litote) qui crée un écart. L'image poétique est un cas particulier de figure, au service d'une évocation sensible : elle associe deux domaines pour faire voir ou ressentir autrement. Dans un poème, l'image condense une émotion en quelques mots et permet de dire l'indicible, par exemple en comparant un sentiment à un élément naturel. Son rôle n'est pas de décorer mais de produire une perception et une résonance chez le lecteur.",
     "On précise le lien de genre à espèce, puis la fonction expressive de l'image.")],
C("Dans le poème, le sens passe par la forme : mètre, rimes et images produisent ensemble une émotion.",
  "Alexandrin = 12 syllabes · sonnet = 14 vers",
  "Rimes croisées ABAB · embrassées ABBA · suivies AABB",
  "Vers~Ligne de poeme~Alexandrin 12~Rime~Sonorite finale~ABAB, ABBA~Cesure~Coupe interne~Image~Transfert sensible",
  "Compter les syllabes|Relever le schema des rimes|Situer la cesure|Repérer les images|Relier forme et emotion",
  "Compter les lettres au lieu des syllabes|Confondre rime et assonance|Oublier l'enjambement|Parler du sens sans parler de la forme",
  "Alexandrin~12 syllabes~Sonnet~14 vers~Quatrains~2 x 4~Tercets~2 x 3~Volta~Bascule apres le vers 8",
  "Rimes croisees~ABAB~Rimes embrassees~ABBA~Alternance~Attente et retour",
  "Image poetique~Evocation sensible~Figure de style~Procede general"))

# ============================================================ FR5
add("FR5", "Le théâtre et le dialogue dramatique", "Français", ["2nde pro"],
S("Le texte dramatique est écrit pour être joué : il se compose principalement de paroles de personnages et de indications de mise en scène."
  "|Les didascalies sont les indications de l'auteur : lieu, époque, gestes, ton, entrées et sorties des personnages."
  "|Une pièce se divise en actes, eux-mêmes coupés en scènes ; un changement de scène correspond à une entrée ou une sortie."
  "|Une réplique est l'intervention d'un personnage ; une tirade est une réplique longue, un monologue une parole sans interlocuteur présent."
  "|L'aparté est une parole adressée au public que les autres personnages ne sont pas censés entendre."
  "|Le conflit dramatique oppose des personnages aux désirs ou aux valeurs incompatibles : c'est le moteur de l'action."
  "|La comédie vise à divertir et se termine souvent par un dénouement heureux ; la tragédie met en scène une fatalité et une issue grave."
  "|Le drame romantique mêle comique et tragique et refuse la séparation stricte des genres."
  "|Les trois unités classiques sont l'unité de lieu, de temps et d'action : une même scène, une journée, une intrigue principale."
  "|Le dialogue doit être vivant : répliques courtes, interruptions, reprises et questions entretiennent le rythme."
  "|Le sens d'une réplique dépend autant de son contenu que de la situation et des didascalies qui l'entourent."
  "|Analyser une scène, c'est identifier les personnages en présence, le conflit, les paroles et les indications de jeu."),
[QC("Que sont les didascalies ?", "Les paroles des personnages~Les indications de mise en scène~Les titres des actes~Les rimes du texte", 1,
     "Les didascalies précisent le lieu, les gestes et le ton ; elles ne sont pas prononcées."),
 QC("Qu'appelle-t-on une tirade ?", "Une courte réplique~Une réplique longue~Un changement de décor~Une sortie de scène", 1,
     "Une tirade est une intervention longue d'un même personnage."),
 QC("Quel personnage est concerné par un aparté ?", "Le seul autre acteur~Le public, sans que les autres personnages entendent~Le metteur en scène~Le narrateur", 1,
     "L'aparté est une confidence au public, invisible pour les autres personnages."),
 QC("Quel est le moteur de l'action dramatique ?", "La description du décor~Le conflit entre personnages~La longueur des tirades~Le nombre d'actes", 1,
     "Le conflit oppose des volontés et fait avancer la pièce."),
 QC("Quel genre se termine généralement par un dénouement heureux ?", "La tragédie~La comédie~Le drame~Le monologue", 1,
     "La comédie vise le divertissement et une issue favorable."),
 QC("Combien d'unités classiques la tragédie classique respecte-t-elle ?", "Une~Deux~Trois~Quatre", 2,
     "Les trois unités sont celles de lieu, de temps et d'action."),
 QC("Que marque un changement de scène ?", "Un changement d'acteur~Une entrée ou une sortie de personnage~Une fin de pièce~Un nouveau personnage imaginaire", 1,
     "La scène change dès qu'un personnage entre ou sort."),
 QT("Analyser une réplique de théâtre en tenant compte de la situation et des didascalies.",
     "On identifie d'abord le locuteur et le destinataire de la réplique, puis la situation au moment où elle est prononcée. On lit les didascalies qui indiquent le ton, le geste ou l'émotion : elles orientent le sens. On repère ensuite les procédés du dialogue, comme une interruption, une question ou une reprise du mot de l'autre. Enfin, on explique ce que la réplique révèle du conflit et du caractère du personnage : au théâtre, parler est déjà agir sur l'autre.",
     "On attend la prise en compte du locuteur, du destinataire, des didascalies et du conflit."),
 QT("Comparer la comédie et la tragédie et expliquer ce que le drame romantique change.",
     "La comédie met en scène des personnages ordinaires, vise le rire et se conclut par un mariage ou une réconciliation. La tragédie met en jeu des personnages de rang élevé confrontés à une fatalité, avec une issue douloureuse et souvent la mort. Le drame romantique refuse cette hiérarchie : il mélange le comique et le tragique dans une même pièce, multiplie les lieux et les scènes et donne plus de place au peuple et à l'action historique. Il remplace la vraisemblance classique par une liberté revendiquée.",
     "On oppose finalité, personnages et dénouement, puis on montre la rupture apportée par le drame.")],
C("Une pièce de théâtre est un jeu de paroles : le sens naît du conflit, de la situation et des didascalies.",
  "Dialogue + didascalies + découpage en actes et scènes",
  "Comédie : rire et dénouement heureux · tragédie : fatalité · drame : mélange des genres",
  "Didascalie~Indication de jeu~Non prononcee~Replique~Parole d'un personnage~Tirade si longue~Scene~Entree ou sortie~Conflit~Moteur de l'action",
  "Repérer les personnages présents|Lire les didascalies|Identifier qui parle à qui|Observer les interruptions|Relier la replique au conflit",
  "Lire une pièce comme un roman|Ignorer les didascalies|Confondre acte et scène|Résumer sans citer les paroles",
  "Aparté~Confidence au public~Monologue~Parole sans interlocuteur~Tirade~Longue intervention~Unites~Lieu, temps, action",
  "Comedie~Rire et final heureux~Tragedie~Fatalite et issue grave",
  "Tirade~Longue parole~Replique courte~Echange vif"))

# ============================================================ FR6
add("FR6", "La phrase : grammaire, accords et orthographe", "Français", ["2nde pro"],
S("La phrase est une unité de sens délimitée par une majuscule et un point ; elle se compose de mots ayant une nature et une fonction."
  "|Les natures lexicales courantes sont le nom, le verbe, l'adjectif, le déterminant, le pronom, l'adverbe, la préposition et la conjonction."
  "|La fonction d'un mot dépend de sa place et de sa relation avec les autres : sujet, verbe, complément d'objet, complément circonstanciel, attribut."
  "|Une phrase simple contient une seule proposition ; une phrase complexe en contient plusieurs, coordonnées ou subordonnées."
  "|La coordination relie des propositions de même niveau par et, ou, mais, donc ; la subordination introduit une proposition dépendante."
  "|Le verbe s'accorde en personne et en temps avec son sujet : les signes d'accord se lisent à la terminaison."
  "|Le participe passé employé avec avoir s'accorde avec le complément d'objet direct seulement si celui-ci est placé avant le verbe."
  "|Le participe passé employé avec être s'accorde avec le sujet du verbe, sauf pour les verbes pronominaux à complément direct placé après."
  "|Les homophones les plus fréquents sont a/à, ou/où, ce/se, son/sont, leur/leurs et leur/leur."
  "|L'adverbe modifie un verbe, un adjectif ou un autre adverbe et reste généralement invariable."
  "|La ponctuation organise la phrase : virgule pour les éléments coordonnés, point-virgule pour deux propositions liées, deux-points pour une explication."
  "|Une relecture efficace vérifie d'abord le sens, puis les accords, la ponctuation et les homophones, sans corriger au hasard."),
[QC("Quelle est la fonction du mot qui accomplit l'action ?", "Complément d'objet~Sujet~Attribut~Adverbe", 1,
     "Le sujet est celui dont le verbe exprime l'action ou l'état."),
 QC("Quel mot coordonne deux propositions de même niveau ?", "Parce que~Bien que~Mais~Quand", 2,
     "Mais, et, ou, donc sont des conjonctions de coordination ; les autres introduisent une subordination."),
 QC("Quand le participe passé avec avoir s'accorde-t-il avec le COD ?", "Toujours~Jamais~Si le COD est placé avant le verbe~Si le COD est un nom propre", 2,
     "La règle porte sur un COD antéposé : les lettres que j'ai écrites."),
 QC("Quel homophone convient dans « Je vais ___ la banque » ?", "a~à~as~avez", 1,
     "À est une préposition de lieu ; a est une forme du verbe avoir."),
 QC("Quel mot est un adverbe ?", "Rapidement~Rapidité~Rapide~Rapider", 0,
     "Rapidement modifie le verbe ; les autres sont un nom ou un adjectif."),
 QC("Que marque le deux-points dans une phrase ?", "Une opposition~Une explication ou une énumération~Une pause finale~Une question", 1,
     "Le deux-points introduit une précision, une explication ou une énumération."),
 QC("Quel ordre suit une relecture efficace ?", "Homophones, ponctuation, sens, accords~Sens, accords, ponctuation, homophones~Ponctuation seulement~Accords seulement", 1,
     "On relit d'abord pour le sens, puis pour les accords, la ponctuation et les homophones."),
 QT("Corriger et justifier : « Les documents que j'ai envoyé hier sont arrivé ce matin. »",
     "Deux accords sont fautifs. Le pronom relatif « que » est complément d'objet direct de « ai envoyé » et il est placé avant le verbe : le participe passé prend donc un accord avec lui, ce qui donne « que j'ai envoyés ». Ensuite, « sont arrivé » emploie l'auxiliaire être : le participe s'accorde avec le sujet « les documents », donc « sont arrivés ». La phrase corrigée est : « Les documents que j'ai envoyés hier sont arrivés ce matin. »",
     "On attend les deux règles : COD antéposé avec avoir et accord avec le sujet avec être."),
 QT("Expliquer la différence entre phrase simple et phrase complexe, et donner une méthode pour repérer les propositions.",
     "Une phrase simple ne contient qu'une proposition, donc un seul verbe conjugué : « Le client signe le devis ». Une phrase complexe contient au moins deux verbes conjugués et donc plusieurs propositions : « Le client signe le devis après que la direction l'a validé ». Pour les repérer, on souligne chaque verbe conjugué, on identifie son sujet, puis on délimite le groupe de mots qui en dépend. On qualifie ensuite le lien : coordination quand les propositions sont de même niveau, subordination quand l'une dépend de l'autre.",
     "On donne une définition par le nombre de verbes conjugués et une méthode de repérage.")],
C("La maîtrise de la phrase repose sur la nature et la fonction des mots, puis sur des règles d'accord vérifiées à la relecture.",
  "Avoir + COD antéposé = accord du participe · être = accord avec le sujet",
  "Coordination : et, ou, mais, donc · subordination : que, qui, parce que, bien que",
  "Sujet~Qui fait l'action~Verbe conjugue~Fonction~Rôle dans la phrase~COD~Complement direct~Participant~Nature~Categorie du mot",
  "Lire la phrase pour le sens|Repérer chaque verbe conjugue|Trouver le sujet de chaque verbe|Appliquer la règle d'accord|Relire ponctuation et homophones",
  "Corriger sans comprendre la phrase|Accorder avec avoir n'importe comment|Confondre nature et fonction|Oublier les homophones",
  "Envoyes~COD antéposé~Arrives~Accord avec être~A~Preposition de lieu~Donc~Coordination",
  "Phrase simple~Un seul verbe conjugue~Phrase complexe~Plusieurs verbes conjugues",
  "Coordination~Meme niveau~Subordination~Proposition dependante"))

# ============================================================ MA1
add("MA1", "Calcul littéral et résolution d'équations", "Mathématiques", ["2nde pro"],
S("Le calcul littéral manipule des expressions où figurent des variables : on développe, on réduit et on factorise selon des règles exactes."
  "|Le développement distribue un facteur sur une somme : a(b + c) = ab + ac ; on peut aussi développer un produit de deux sommes."
  "|La réduction regroupe les termes de même nature pour obtenir une expression plus courte, équivalente à la première."
  "|Les trois identités remarquables sont (a + b)² = a² + 2ab + b², (a − b)² = a² − 2ab + b² et (a + b)(a − b) = a² − b²."
  "|La factorisation transforme une somme en produit par facteur commun, identité remarquable ou recherche de deux nombres."
  "|Une équation du premier degré s'écrit ax + b = 0 ; sa solution est x = −b/a lorsque a est non nul."
  "|Une équation du second degré s'écrit ax² + bx + c = 0 ; son discriminant vaut Δ = b² − 4ac."
  "|Si Δ est strictement positif, l'équation admet deux solutions réelles ; si Δ est nul, une solution double ; sinon aucune."
  "|Les solutions sont alors x = (−b ± √Δ)/(2a) ; une factorisation directe donne parfois le même résultat plus vite."
  "|Un produit de facteurs est nul si et seulement si l'un des facteurs est nul : c'est la propriété fondamentale de résolution."
  "|Les fractions littérales imposent de vérifier les conditions d'existence : un dénominateur ne peut jamais être nul."
  "|Dans un contexte de gestion, ces outils servent à isoler une variable dans un calcul de budget, de marge ou de taux."),
[QC("Que vaut (a − b)² ?", "a² − b²~a² − 2ab + b²~a² + 2ab + b²~a² − ab + b²", 1,
     "Le carré d'une différence comporte le terme croisé −2ab."),
 QC("Comment factorise-t-on a² − b² ?", "(a − b)²~(a + b)(a − b)~(a + b)²~a(a − b)", 1,
     "C'est la différence de deux carrés, donc le produit de la somme et de la différence."),
 QC("Quel est le discriminant de x² − 5x + 6 = 0 ?", "1~5~25~49", 0,
     "Δ = (−5)² − 4 × 1 × 6 = 25 − 24 = 1."),
 QC("Combien de solutions réelles si Δ < 0 ?", "0~1~2~Une infinité", 0,
     "Un discriminant négatif exclut toute solution réelle."),
 QC("Quelle est la solution de 3x + 6 = 0 ?", "−2~2~−6~6", 0,
     "3x = −6 donc x = −2."),
 QC("Quelle est la condition d'existence de 5/(x − 3) ?", "x = 3~x ≠ 3~x > 3~Aucune", 1,
     "Le dénominateur x − 3 doit être non nul, donc x ≠ 3."),
 QC("Quelle propriété permet de résoudre (x − 1)(x + 4) = 0 ?", "La distributivité~Un produit nul impose un facteur nul~La soustraction~L'arrondi", 1,
     "On en déduit x = 1 ou x = −4."),
 QT("Résoudre x² + x − 12 = 0 par factorisation, puis par le discriminant, et comparer.",
     "Par factorisation, on cherche deux nombres de somme 1 et de produit −12 : ce sont 4 et −3, donc x² + x − 12 = (x + 4)(x − 3). Le produit est nul pour x = −4 ou x = 3. Par le discriminant, Δ = 1² − 4 × 1 × (−12) = 1 + 48 = 49, donc √Δ = 7 et x = (−1 ± 7)/2, soit x = 3 ou x = −4. Les deux méthodes donnent le même résultat ; la factorisation est plus rapide quand les nombres se devinent, le discriminant reste systématique.",
     "On attend les deux méthodes, les mêmes solutions et une comparaison de leur efficacité."),
 QT("Développer puis réduire A = (2x + 3)² − (2x + 3)(2x − 3) et donner le résultat.",
     "On développe (2x + 3)² = 4x² + 12x + 9. Ensuite (2x + 3)(2x − 3) est une différence de carrés : 4x² − 9. Donc A = 4x² + 12x + 9 − 4x² + 9 = 12x + 18. On peut factoriser : A = 6(2x + 3). Le contrôle par x = 0 donne 9 − (−9) = 18, ce qui correspond bien à 12 × 0 + 18.",
     "On utilise les deux identités remarquables, on réduit et on vérifie par une valeur particulière.")],
C("Le calcul littéral repose sur trois identités et sur la factorisation, outil central de la résolution d'équations.",
  "Δ = b² − 4ac · solutions = (−b ± √Δ)/(2a)",
  "(a+b)² = a²+2ab+b² · (a−b)² = a²−2ab+b² · (a+b)(a−b) = a²−b²",
  "Developpement~a(b+c)=ab+ac~Distribution~Reduction~Termes semblables~Factorisation~Somme en produit~Equation~Δ et racines",
  "Repérer la structure de l'expression|Choisir développement ou factorisation|Appliquer l'identité adaptée|Réduire les termes semblables|Vérifier la solution trouvée",
  "Oublier le terme croisé 2ab|Écrire (a+b)² = a²+b²|Négliger les conditions d'existence|Perdre un signe en réduisant",
  "x²+x−12~(x+4)(x−3)~Δ=49~Deux solutions 3 et −4~5/(x−3)~x≠3~(2x+3)²~4x²+12x+9",
  "Developper~Du produit vers la somme~Factoriser~De la somme vers le produit",
  "Δ>0~Deux racines~Δ=0~Racine double"))

# ============================================================ MA2
add("MA2", "Fonctions et lecture de graphiques", "Mathématiques", ["2nde pro"],
S("Une fonction associe à chaque nombre d'un ensemble de définition un unique nombre d'arrivée : à un antécédent correspond une seule image."
  "|Une fonction affine s'écrit f(x) = ax + b ; sa représentation graphique est une droite de coefficient directeur a et d'ordonnée à l'origine b."
  "|Le coefficient directeur se calcule avec deux points : a = (y₂ − y₁)/(x₂ − x₁) ; il donne la pente de la droite."
  "|Une fonction linéaire est le cas b = 0 : la droite passe par l'origine et traduit une situation de proportionnalité."
  "|La fonction carrée f(x) = x² se représente par une parabole symétrique par rapport à l'axe des ordonnées, de sommet (0 ; 0)."
  "|La fonction exponentielle f(x) = a^x passe par (0 ; 1) ; elle est croissante si a > 1 et décroissante si 0 < a < 1."
  "|La fonction logarithme népérien est la réciproque de l'exponentielle : ln(e^x) = x pour tout x et e^(ln x) = x pour x > 0."
  "|Une fonction est croissante sur un intervalle si, quand x augmente, f(x) augmente ; elle est décroissante dans le cas contraire."
  "|Résoudre graphiquement f(x) = k revient à lire les abscisses des intersections de la courbe avec la droite horizontale y = k."
  "|Résoudre f(x) ≥ k revient à conserver les abscisses pour lesquelles la courbe est au-dessus ou sur la droite y = k."
  "|La composition vérifie (g ∘ f)(x) = g(f(x)) : on applique d'abord f, puis g au résultat obtenu."
  "|Lire un graphique, identifier un modèle et interpréter une pente sont des compétences utiles pour suivre un budget ou une évolution d'activité."),
[QC("Quelle est la courbe d'une fonction affine ?", "Une parabole~Une droite~Un cercle~Une hyperbole", 1,
     "Toute fonction de la forme ax + b se représente par une droite."),
 QC("Quel est le coefficient directeur de y = −3x + 4 ?", "4~3~−3~−4", 2,
     "C'est le coefficient de x, ici −3 ; la droite est décroissante."),
 QC("Par quel point passe toujours y = e^x ?", "(0 ; 0)~ (1 ; 0)~ (0 ; 1)~ (1 ; 1)", 2,
     "e⁰ = 1, donc la courbe passe par (0 ; 1)."),
 QC("Quelle est la réciproque de l'exponentielle népérienne ?", "La fonction carrée~La fonction logarithm~La fonction affine~La valeur absolue", 1,
     "ln est la réciproque de x ↦ e^x."),
 QC("Comment résoudre graphiquement f(x) = 2 ?", "Lire l'ordonnée en x=2~Lire les abscisses des intersections avec y=2~Multiplier les coefficients~Additionner les points", 1,
     "On projette sur l'axe des abscisses les points d'intersection avec la droite y = 2."),
 QC("Une fonction est croissante si…", "Sa courbe descend~Sa courbe monte~Elle passe par l'origine~Elle est carrée", 1,
     "Quand x augmente, l'image augmente aussi : la courbe monte."),
 QC("Que vaut (g ∘ f)(x) ?", "g(x)f(x)~g(f(x))~f(g(x))~g(x)+f(x)", 1,
     "La composition applique d'abord f puis g."),
 QT("Une droite passe par A(2 ; 7) et B(5 ; 16). Déterminer son équation et calculer f(12).",
     "Le coefficient directeur vaut a = (16 − 7)/(5 − 2) = 9/3 = 3. En remplaçant par les coordonnées de A : 7 = 3 × 2 + b, donc b = 1. L'équation est f(x) = 3x + 1. Vérification avec B : 3 × 5 + 1 = 16. Alors f(12) = 3 × 12 + 1 = 37. La droite coupe l'axe des ordonnées en (0 ; 1) et monte de 3 unités pour 1 unité vers la droite.",
     "On calcule la pente, on isole b, on vérifie avec le second point puis on évalue en 12."),
 QT("Expliquer comment lire graphiquement l'ensemble des solutions de x² ≤ 4.",
     "On trace la parabole y = x² et la droite horizontale y = 4. Les intersections ont pour abscisses −2 et 2, car (±2)² = 4. On recherche les portions de la parabole situées au-dessous ou sur la droite : comme la parabole est en dessous de y = 4 entre ses deux points d'intersection, les solutions sont toutes les valeurs de x comprises entre −2 et 2, bornes incluses. L'ensemble de solutions est donc l'intervalle [−2 ; 2]. On vérifie avec x = 0, qui donne 0 ≤ 4, et avec x = 3, qui donne 9 > 4.",
     "On trace les deux courbes, on lit les abscisses d'intersection, puis on choisit le bon intervalle et on vérifie.")],
C("Une fonction associe une image à chaque antécédent ; sa courbe donne accès aux variations et aux solutions.",
  "f(x) = ax + b · a = Δy/Δx",
  "Droite si affine · parabole si carrée · exponentielle croissante si a > 1",
  "Fonction~Antecedent et image~Domaine de definition~Affine~Droite de pente a~f(x)=ax+b~Carree~Parabole symetrique~Sommet en zero",
  "Repérer le type de fonction|Determiner le domaine|Tracer les points caracteristiques|Lire les intersections avec y=k|Interpréter dans le contexte",
  "Confondre pente et ordonnée à l'origine|Oublier le domaine de définition|Lire l'ordonnée au lieu de l'abscisse|Croire que x² est croissante partout",
  "A(2;7), B(5;16)~a=3 et b=1~f(12)=37~x²≤4~Intervalle [−2 ; 2]~e⁰~Vaut 1",
  "Fonction affine~Droite~Pente constante~Fonction carree~Parabole~Pente variable",
  "Proportionnalite~Droite passant par l'origine~Affine generale~Droite decalee"))

# ============================================================ MA3
add("MA3", "Statistiques descriptives appliquées à la gestion", "Mathématiques", ["2nde pro"],
S("La statistique descriptive résume un ensemble de données pour en dégager les caractéristiques essentielles sans perdre l'information utile."
  "|Une population est l'ensemble complet des individus étudiés ; un échantillon en est une partie prélevée pour être représentative."
  "|Un caractère qualitatif se traite par des effectifs et des pourcentages ; un caractère quantitatif par des mesures de position et de dispersion."
  "|L'effectif d'une classe est le nombre d'individus qui s'y trouvent ; l'effectif cumulé additionne les effectifs jusqu'à cette classe."
  "|La fréquence relative vaut effectif de la classe divisé par l'effectif total ; elle se convertit en pourcentage par multiplication par 100."
  "|La moyenne est la somme des valeurs divisée par l'effectif : elle est sensible aux valeurs extrêmes."
  "|La médiane est la valeur qui partage une série ordonnée en deux moitiés ; elle résiste aux valeurs aberrantes."
  "|Les quartiles Q1 et Q3 découpent la série en quatre parts ; l'intervalle interquartile Q3 − Q1 contient la moitié centrale des données."
  "|Le mode est la valeur la plus fréquente : c'est le seul indicateur de position pertinent pour un caractère qualitatif."
  "|L'étendue est la différence entre la valeur maximale et la valeur minimale ; la variance et l'écart-type mesurent la dispersion."
  "|L'écart-type est la racine carrée de la variance et s'exprime dans la même unité que la donnée, ce qui facilite son interprétation."
  "|Un graphique doit indiquer la source, l'effectif et les unités ; l'histogramme convient à une variable continue et le camembert à une répartition."),
[QC("Quelle mesure résiste aux valeurs extrêmes ?", "La moyenne~La médiane~L'écart-type~L'étendue", 1,
     "La médiane dépend du rang des valeurs, non de leur amplitude."),
 QC("Comment calcule-t-on une fréquence relative ?", "Effectif × total~Effectif / total~Total / effectif~Max − min", 1,
     "La fréquence est le rapport de l'effectif de la classe à l'effectif total."),
 QC("Quel graphique convient à une variable quantitative continue ?", "Le camembert~L'histogramme~Le diagramme en bâtons~Le pictogramme", 1,
     "L'histogramme représente les effectifs par classes de valeurs continues."),
 QC("Que mesure l'écart-type ?", "La tendance centrale~La dispersion autour de la moyenne~L'effectif total~La corrélation", 1,
     "C'est la racine de la variance, exprimée dans l'unité de la donnée."),
 QC("Dans une série ordonnée de 7 valeurs, quelle est la position de la médiane ?", "La 3e~La 4e~La 5e~La moyenne des 3e et 4e", 1,
     "Pour un effectif impair, le rang est (n+1)/2 = 4."),
 QC("Quel indicateur choisir pour un caractère qualitatif ?", "La moyenne~Le mode~L'écart-type~La médiane", 1,
     "Le mode est la classe ou la valeur la plus fréquente."),
 QC("Que désigne l'intervalle interquartile ?", "Max moins min~Q3 moins Q1~La moyenne des quartiles~La somme des effectifs", 1,
     "Il contient 50 % des observations centrales."),
 QT("Une série de temps de traitement en minutes est : 4, 6, 7, 9, 38. Calculer moyenne, médiane et étendue, puis commenter.",
     "La somme vaut 4 + 6 + 7 + 9 + 38 = 64, donc la moyenne est 64/5 = 12,8 minutes. La série est ordonnée et compte 5 valeurs : la médiane est la 3e, soit 7 minutes. L'étendue vaut 38 − 4 = 34 minutes. L'écart important entre la moyenne (12,8) et la médiane (7) révèle l'influence de la valeur 38, probablement un incident isolé. La médiane décrit mieux le temps habituel de traitement ; on cherchera la cause de la valeur aberrante avant de conclure sur la performance du service.",
     "On calcule les trois indicateurs, puis on explique l'écart moyen/médiane par la valeur extrême."),
 QT("Expliquer pourquoi un échantillon représentatif est nécessaire avant de généraliser un résultat.",
     "Un échantillon est représentatif lorsque sa composition reflète celle de la population pour les caractéristiques pertinentes. Si le prélèvement est biaisé, par exemple en n'interrogeant que les clients satisfaits, les indicateurs calculés sont biaisés et aucune généralisation n'est valable, même avec un grand effectif. Un tirage aléatoire, une stratification par catégorie et un effectif suffisant limitent ce risque. On doit également indiquer la marge d'incertitude et le niveau de confiance pour exprimer la précision de l'estimation avant de conclure.",
     "On relie représentativité, absence de biais, tirage aléatoire et marge d'incertitude.")],
C("La statistique descriptive résume une série par une tendance centrale et une dispersion adaptées au type de donnée.",
  "Fréquence = effectif / total · écart-type = racine de la variance",
  "Moyenne sensible aux extrêmes · médiane robuste · mode pour le qualitatif",
  "Population~Ensemble complet~Echantillon~Partie prelevee~Representativite~Moyenne~Somme divisée par n~Mediane~Valeur centrale~Ecart-type~Dispersion",
  "Définir population et échantillon|Trier et classer les données|Choisir les indicateurs|Construire le graphique adapté|Interpréter avec source et unités",
  "Utiliser la moyenne avec une valeur aberrante|Confondre effectif et fréquence|Choisir un camembert pour du continu|Omettre la taille de l'échantillon",
  "4;6;7;9;38~Moyenne 12,8 et médiane 7~Etendue 34~Valeur aberrante~Q1 et Q3~Moitié centrale~Fréquence~Effectif sur total",
  "Moyenne~Sensible aux extrêmes~Mediane~Resistante aux extrems",
  "Effectif~Nombre d'individus~Frequence~Part du total"))

# ============================================================ MA4
add("MA4", "Probabilités et modélisation de l'aléa", "Mathématiques", ["1re pro"],
S("Une expérience aléatoire est une épreuve dont l'issue est incertaine mais dont l'ensemble des résultats possibles, l'univers, est connu."
  "|Un événement est une partie de l'univers ; sa probabilité est un nombre compris entre 0 et 1, égale à 1 s'il est certain et à 0 s'il est impossible."
  "|Dans un univers fini équiprobable, la probabilité d'un événement vaut nombre d'issues favorables divisé par nombre total d'issues."
  "|Une loi de probabilité associe une probabilité à chaque issue ; la somme de toutes ces probabilités vaut exactement 1."
  "|Deux événements incompatibles ne peuvent pas survenir ensemble : P(A ∪ B) = P(A) + P(B)."
  "|Deux événements indépendants vérifient P(A ∩ B) = P(A) × P(B) : la réalisation de l'un ne modifie pas la probabilité de l'autre."
  "|La probabilité conditionnelle P(A sachant B) vaut P(A ∩ B) / P(B) : on restreint l'univers à la réalisation de B."
  "|Un arbre pondéré représente les étapes successives ; on multiplie les probabilités le long d'une branche et on additionne les chemins favorables."
  "|La formule des probabilités totales calcule P(A) en sommant les probabilités conditionnelles pondérées par celles des sous-groupes."
  "|La formule de Bayes inverse une probabilité conditionnelle et sert à interpréter un test ou une alerte."
  "|Une variable aléatoire associe un nombre à chaque issue ; son espérance est la moyenne théorique à long terme."
  "|Les probabilités aident à arbitrer une décision de gestion, à évaluer un risque ou à dimensionner un plan d'échantillonnage."),
[QC("Quelle est la probabilité d'un événement impossible ?", "0~0,5~1~2", 0,
     "Un événement impossible a une probabilité nulle."),
 QC("Dans un univers équiprobable, comment calculer P(A) ?", "Favorables × total~Favorables / total~Total − favorables~Total / 2", 1,
     "On divise le nombre d'issues favorables par le nombre total d'issues."),
 QC("Quelle relation caractérise deux événements indépendants ?", "P(A∩B)=P(A)+P(B)~P(A∩B)=P(A)×P(B)~P(A)=P(B)~P(A∪B)=P(A)P(B)", 1,
     "L'indépendance se traduit par la multiplication des probabilités."),
 QC("Quelle est la formule de la probabilité conditionnelle ?", "P(A|B)=P(A)+P(B)~P(A|B)=P(A∩B)/P(B)~P(A|B)=P(B)/P(A)~P(A|B)=P(A)−P(B)", 1,
     "On divise par P(B) parce que l'univers se limite à B."),
 QC("À quoi sert un arbre pondéré ?", "Trier des données~Représenter des étapes et composer des probabilités~Dessiner un histogramme~Résoudre une équation", 1,
     "On multiplie le long des branches puis on additionne les chemins favorables."),
 QC("Que vaut la somme des probabilités d'une loi complète ?", "0~1~L'effectif total~La moyenne", 1,
     "Les probabilités d'une loi complète forment une somme égale à 1."),
 QC("Quel théorème permet de calculer P(A) à partir d'une partition ?", "Bayes~Probabilités totales~Pythagore~Théorème central limite", 1,
     "Les probabilités totales pondèrent les conditionnelles par les probabilités des sous-groupes."),
 QT("On lance deux dés équilibrés. Calculer la probabilité d'obtenir une somme de 8, puis une somme inférieure à 4.",
     "L'univers compte 6 × 6 = 36 issues équiprobables. La somme 8 s'obtient par (2,6), (3,5), (4,4), (5,3), (6,2), soit 5 issues : P(somme = 8) = 5/36. Une somme inférieure à 4 correspond à 2 ou 3 : (1,1) pour 2, (1,2) et (2,1) pour 3, soit 3 issues. P(somme < 4) = 3/36 = 1/12. Les deux résultats appartiennent bien à l'intervalle [0 ; 1].",
     "On dénombre l'univers (36), les issues favorables (5 puis 3), puis on simplifie."),
 QT("Un test de contrôle révèle une anomalie avec probabilité 0,95 quand le défaut est présent et 0,04 à tort quand il est absent. La probabilité du défaut est 0,02. Expliquer le calcul de la probabilité qu'une alerte signale vraiment un défaut.",
     "On note D le défaut et A l'alerte. On a P(D) = 0,02, P(A|D) = 0,95, P(A|non D) = 0,04 et P(non D) = 0,98. Par les probabilités totales : P(A) = 0,95 × 0,02 + 0,04 × 0,98 = 0,019 + 0,0392 = 0,0582. Par Bayes : P(D|A) = P(A|D) × P(D) / P(A) = 0,019 / 0,0582 ≈ 0,326, soit environ 33 %. Malgré un test apparemment fiable, la plupart des alertes sont des faux positifs parce que le défaut est rare : c'est le paradoxe de la base rate, qui justifie une deuxième vérification avant de rejeter un lot.",
     "On applique probabilités totales puis Bayes, et on interprète le résultat par la rareté du défaut.")],
C("Les probabilités modélisent l'aléa : on dénombre les issues, on compose les événements, puis on révise les croyances avec Bayes.",
  "P(A|B) = P(A ∩ B) / P(B) · P(A ∩ B) = P(A)P(B) si indépendance",
  "Univers équiprobable : issues favorables / issues totales",
  "Univers~Ensemble des issues~Evenement~Partie de l'univers~Probabilite~Entre zero et un~Independance~P(A)P(B)~Conditionnelle~P(A sachant B)",
  "Définir l'expérience et l'univers|Recenser les issues equiprobables|Identifier les issues favorables|Composer avec arbre ou formules|Interpréter le résultat",
  "Confondre indépendance et incompatibilité|Oublier que la somme vaut 1|Multiplier au lieu de diviser|Ignorer la rareté de la base",
  "2 dés~36 issues~Somme 8~5 issues sur 36~Somme < 4~3 issues sur 36~Alerte~Environ 33 % de vrais défauts",
  "Incompatibles~P(A∪B)=P(A)+P(B)~Independants~P(A∩B)=P(A)×P(B)",
  "Probabilite~Avant information~Conditionnelle~Apres information"))

# ============================================================ MA5
add("MA5", "Suites numériques et calcul financier", "Mathématiques", ["1re pro", "Terminale pro"],
S("Une suite numérique est une famille ordonnée de nombres u₀, u₁, u₂… indexée par les entiers naturels."
  "|Une suite arithmétique vérifie u(n+1) = u(n) + r : la différence entre deux termes consécutifs est constante, égale à la raison r."
  "|Le terme général d'une suite arithmétique vaut u(n) = u₀ + n·r ; la somme des n premiers termes vaut n(u₀ + u(n))/2."
  "|Une suite géométrique vérifie u(n+1) = q·u(n) : le rapport entre deux termes consécutifs est constant, égal à la raison q."
  "|Le terme général d'une suite géométrique vaut u(n) = u₀·q^n ; la somme des n premiers termes vaut u₀(1 − q^n)/(1 − q) si q ≠ 1."
  "|Une suite arithmétique croît si r > 0 ; une suite géométrique positive croît si q > 1 et décroît si 0 < q < 1."
  "|Les intérêts simples donnent un capital final C(n) = C₀(1 + n·t) : l'intérêt est calculé uniquement sur le capital initial."
  "|Les intérêts composés capitalisent les intérêts : C(n) = C₀(1 + t)^n, ce qui correspond à une suite géométrique de raison 1 + t."
  "|L'actualisation ramène un flux futur à sa valeur actuelle en divisant par (1 + t)^n, ce qui permet de comparer des flux à des dates différentes."
  "|Le taux effectif annuel tient compte de la capitalisation : un taux nominal i divisé en m périodes donne (1 + i/m)^m − 1."
  "| Le taux réel approché vaut taux nominal moins inflation ; le calcul exact utilise le rapport des facteurs d'évolution."
  "|Ces outils servent à prévoir un budget pluriannuel, à calculer un amortissement dégressif ou à comparer des offres de financement."),
[QC("Quelle est la raison d'une suite arithmétique ?", "Le rapport entre deux termes~La différence constante~Le premier terme~La somme des termes", 1,
     "Dans une suite arithmétique, u(n+1) − u(n) = r est constante."),
 QC("Quel est le terme général d'une suite géométrique ?", "u₀ + n·q~u₀·q^n~n·q~u₀·q·n", 1,
     "La progression géométrique est exponentielle."),
 QC("Quelle suite modélise les intérêts composés ?", "Arithmétique~Géométrique~Constante~Alternée", 1,
     "Le capital est multiplié par (1 + t) à chaque période."),
 QC("Que vaut 1 000 € à 5 % pendant 2 ans en intérêts composés ?", "1 050 €~1 100 €~1 102,50 €~1 200 €", 2,
     "1000 × 1,05² = 1000 × 1,1025 = 1 102,50 €."),
 QC("Comment nomme-t-on l'operation qui ramène un flux futur à sa valeur actuelle ?", "Capitalisation~Actualisation~Amortissement~Indexation", 1,
     "L'actualisation divise par (1 + t)^n ; la capitalisation multiplie."),
 QC("Si 0 < q < 1, une suite géométrique positive…", "Croît~Décroît vers 0~Est constante~Diverge", 1,
     "Multiplier par un nombre entre 0 et 1 réduit chaque terme."),
 QC("Quel est le taux effectif d'un nominal de 12 % capitalisé mensuellement ?", "12 %~Environ 12,68 %~1 %~24 %", 1,
     "(1 + 0,12/12)^12 − 1 ≈ 0,1268, soit 12,68 %."),
 QT("Un matériel acheté 6 000 € perd 25 % de sa valeur chaque année. Donner la suite de valeur et calculer sa valeur après 3 ans.",
     "La valeur suit une suite géométrique de premier terme v₀ = 6 000 et de raison q = 1 − 0,25 = 0,75, donc v(n) = 6 000 × 0,75^n. Après 3 ans : v(3) = 6 000 × 0,75³ = 6 000 × 0,421875 = 2 531,25 €. La perte cumulée est de 3 468,75 €. L'amortissement est dégressif : la première année enlève 1 500 €, la troisième seulement 562,50 €, car le pourcentage s'applique à une valeur déjà réduite.",
     "On identifie la suite, sa raison 0,75, on calcule 6 000 × 0,75³ et on interprète la dégressivité."),
 QT("Comparer intérêts simples et intérêts composés sur 5 000 € à 4 % sur 4 ans, et expliquer l'écart.",
     "En intérêts simples : 5 000 × (1 + 4 × 0,04) = 5 000 × 1,16 = 5 800 €, soit 800 € d'intérêts. En intérêts composés : 5 000 × 1,04⁴ ≈ 5 000 × 1,169859 = 5 849,29 €, soit environ 49,29 € de plus. L'écart provient de la capitalisation : chaque année, les intérêts déjà acquis produisent à leur tour des intérêts. Cet effet croît avec la durée et le taux ; il faut donc toujours préciser le mode de calcul dans un comparatif financier.",
     "On calcule les deux montants puis on explique l'effet boule de neige de la capitalisation.")],
C("Suites arithmétique et géométrique modélisent des évolutions linéaires ou exponentielles ; intérêts et actualisation en sont les applications.",
  "C(n) = C₀(1 + t)^n · actualisation : C₀ = C(n)/(1 + t)^n",
  "Arithmétique : +r · géométrique : ×q · simple : 1 + nt · composé : (1+t)^n",
  "Suite arithmetique~u(n+1)=u(n)+r~Suite geometrique~u(n+1)=q·u(n)~Interets simples~1+nt~Interets composes~(1+t)^n",
  "Repérer le type de suite|Identifier le premier terme et la raison|Ecrire le terme general|Calculer le terme demande|Interpréter dans le contexte",
  "Confondre raison additive et multiplicative|Oublier la période|Appliquer des intérêts simples aux composés|Négliger l'inflation",
  "6 000 € à −25 %/an~Valeur après 3 ans : 2 531,25 €~5 000 € à 4 %~Composés : 5 849,29 €~12 % mensuel~Effectif 12,68 %~Actualisation~Diviser par (1+t)^n",
  "Interets simples~Interet constant~Interets composes~Interet croissant",
  "Suite arithmetique~Croissance lineaire~Suite geometrique~Croissance exponentielle"))

# ============================================================ MA6
add("MA6", "Géométrie, mesures et lecture de plan", "Mathématiques", ["2nde pro"],
S("La géométrie permet de calculer des longueurs, des aires et des volumes à partir de figures et de relations exactes."
  "|Le théorème de Pythagore s'applique au triangle rectangle : l'hypoténuse au carré vaut la somme des carrés des deux autres côtés."
  "|Le théorème de Thalès établit des proportionalités entre longueurs when deux droites parallèles coupent deux droites sécantes."
  "|Dans un triangle quelconque, la somme des angles internes vaut 180 degrés ; dans un quadrilatère, elle vaut 360 degrés."
  "|L'aire d'un rectangle vaut longueur multipliée par largeur ; celle d'un triangle vaut base multipliée par hauteur divisée par deux."
  "|L'aire d'un disque vaut π multiplié par le rayon au carré ; sa circonférence vaut 2π multiplié par le rayon."
  "|Le volume d'un pavé droit vaut longueur × largeur × hauteur ; celui d'un cylindre vaut π × rayon² × hauteur."
  "|Le périmètre est la longueur du contour d'une figure plane ; il s'exprime en unités de longueur, pas en unités d'aire."
  "|Une homothétie multiplie toutes les longueurs par un même facteur : les aires sont multipliées par le carré de ce facteur."
  "|Une rotation conserve les longueurs et les angles ; une translation conserve aussi les directions."
  "|Les unités doivent être homogènes : on convertit mètres et centimètres avant tout calcul, puis on vérifie l'unité du résultat."
  "|Sur un plan à l'échelle 1/100, 1 cm sur le papier représente 100 cm dans la réalité, soit 1 mètre."),
[QC("Dans un triangle rectangle, que dit Pythagore ?", "h² = a + b~h² = a² + b²~h = a² + b²~h² = a × b", 1,
     "Le carré de l'hypoténuse vaut la somme des carrés des deux autres côtés."),
 QC("Quelle est la somme des angles d'un triangle ?", "90°~180°~270°~360°", 1,
     "Les trois angles internes d'un triangle totalisent 180 degrés."),
 QC("Quelle est l'aire d'un triangle de base 8 cm et de hauteur 5 cm ?", "20 cm²~40 cm²~13 cm²~80 cm²", 0,
     "Aire = 8 × 5 / 2 = 20 cm²."),
 QC("Quel est le volume d'un cylindre de rayon 2 et de hauteur 3 ?", "6π~12π~18π~24π", 1,
     "V = π × r² × h = π × 4 × 3 = 12π."),
 QC("Quand applique-t-on le théorème de Thalès ?", "À tout triangle~Quand deux parallèles coupent deux sécantes~Uniquement au disque~Uniquement aux cubes", 1,
     "Thalès exige la présence de droites parallèles."),
 QC("Que deviennent les aires lors d'une homothétie de rapport 3 ?", "Elles triplent~Elles sont multipliées par 9~Elles sont divisées par 3~Elles ne changent pas", 1,
     "Les longueurs sont multipliées par 3, les aires par 3² = 9."),
 QC("À l'échelle 1/100, combien de mètres représente 1 cm sur le plan ?", "0,01 m~0,1 m~1 m~100 m", 2,
     "1 cm × 100 = 100 cm = 1 mètre."),
 QT("Un triangle rectangle a deux côtés de l'angle droit de 9 cm et 12 cm. Calculer l'hypoténuse et l'aire.",
     "Par Pythagore, h² = 9² + 12² = 81 + 144 = 225, donc h = √225 = 15 cm. L'aire du triangle rectangle vaut produit des côtés de l'angle droit divisé par 2 : 9 × 12 / 2 = 54 cm². On vérifie la cohérence : l'hypoténuse est bien le plus grand côté (15 > 12), et l'aire exprimée en cm² correspond à des longueurs en cm.",
     "On applique Pythagore, puis la formule de l'aire, avec vérification de l'unité et de la taille relative."),
 QT("Expliquer la démarche pour calculer la quantité de peinture nécessaire pour recouvrir un mur rectangulaire.",
     "On mesure d'abord la longueur et la hauteur du mur dans la même unité, par exemple en mètres. On calcule l'aire en multipliant ces deux grandeurs : un mur de 6 m sur 2,5 m a une aire de 15 m². On déduit éventuellement la surface des ouvertures (portes, fenêtres) en calculant leur aire propre. On consulte ensuite le rendement du produit, par exemple 10 m² par litre, et on divise l'aire nette par ce rendement pour obtenir le nombre de litres. On arrondit à la hausse et on prévoit une couche supplémentaire si nécessaire, puis on vérifie l'homogénéité des unités à chaque étape.",
     "On attend mesure, calcul d'aire, déduction des ouvertures, usage du rendement et contrôle des unités.")],
C("La géométrie relie longueurs, aires et volumes par des formules et des théorèmes ; l'homogénéité des unités est permanente.",
  "Pythagore : h² = a² + b² · Thalès : rapports de parallelisme",
  "Aire triangle = base × hauteur / 2 · volume pavé = L × l × h",
  "Pythagore~Triangle rectangle~Hypotenuse au carre~Thales~Paralleles et proportions~Aire~Surface en carres~Volume~Espace en cubes~Echelle~1 cm pour 100 cm",
  "Lire les donnees et les unites|Dessiner la figure|Choisir le theoreme ou la formule|Effectuer le calcul|Verifier l'unite et la vraisemblance",
  "Mélanger mètres et centimètres|Confondre périmètre et aire|Appliquer Pythagore sans angle droit|Oublier de diviser l'aire du triangle par 2",
  "9 et 12~Hypotenuse 15 cm~Aire du triangle~54 cm²~Cylindre r=2, h=3~Volume 12π~Echelle 1/100~1 cm = 1 m",
  "Pythagore~Triangle rectangle~Thales~Configuration avec paralleles",
  "Perimetre~Longueur du contour~Aire~Surface occupee"))

# ============================================================ HG1
add("HG1", "La France de la Révolution à la Commune", "Histoire-géo", ["2nde pro"],
S("La Révolution française de 1789 renverse l'Ancien Régime et instaure une souveraineté nationale fondée sur le citoyen."
  "|La Déclaration des droits de l'homme et du citoyen d'août 1789 proclame l'égalité juridique et les libertés individuelles."
  "|La Constituante vote la Constitution de 1791, instaurant une monarchie constitutionnelle et une assemblée législative élue."
  "|La chute de la monarchie, le 10 août 1792, puis la proclamation de la République, le 21 septembre, radicalisent le mouvement."
  "|La Convention adopte la constitution de l'an I et juge Louis XVI, exécuté le 21 janvier 1793."
  "|La Terreur, organisée par le Comité de salut public, frappe les suspects jusqu'à la chute de Robespierre en thermidor an II."
  "|Le Directoire succède à la Convention en 1795 mais s'appuie sur un régime fragile et corrompu."
  "|Bonaparte prend le pouvoir le 18 Brumaire an VIII (9 novembre 1799) et instaure le Consulat, puis l'Empire en 1804."
  "|Le Code civil de 1804 consacre l'égalité devant la loi et la propriété, tout en maintenant des inégalités de statut."
  "|La Restauration (1814-1830) puis la monarchie de Juillet (1830-1848) tentent de concilier ordre et libertés."
  "|La révolution de février 1848 instaure la IIe République et le suffrage universel masculin, puis Louis-Napoléon est élu président."
  "|Le coup d'État du 2 décembre 1851 ouvre le Second Empire ; la Commune de Paris en 1871 défend la république et les droits sociaux avant d'être réprimée."),
[QC("En quelle année est proclamée la République ?", "1789~1791~1792~1793", 2,
     "La République est proclamée le 21 septembre 1792 ; la monarchie tombe le 10 août."),
 QC("Que proclame la Déclaration de 1789 ?", "Le retour à l'Ancien Régime~Les droits de l'homme et du citoyen~L'Empire~La Terreur", 1,
     "Elle affirme l'égalité juridique et les libertés individuelles."),
 QC("Quel régime succède à la Convention en 1795 ?", "Le Consulat~Le Directoire~L'Empire~La Restauration", 1,
     "Le Directoire dure de 1795 au coup d'État de Brumaire en 1799."),
 QC("Qui dirige le Comité de salut public pendant la Terreur ?", "Louis XVI~Robespierre~Bonaparte~Louis-Philippe", 1,
     "Robespierre en est la figure centrale jusqu'à sa chute en thermidor an II."),
 QC("Quel texte de 1804 consacre l'égalité devant la loi ?", "La Déclaration de 1789~Le Code civil~La Constitution de 1791~L'édit de Nantes", 1,
     "Le Code civil napoléonien fixe les règles du droit civil et l'égalité juridique."),
 QC("Quel événement instaure le suffrage universel masculin ?", "La révolution de 1848~Le coup d'État de 1851~La Commune~La Restauration", 0,
     "La IIe République issue de février 1848 adopte le suffrage universel masculin."),
 QC("Quel est le président élu en 1848 avant le coup d'État ?", "Louis-Philippe~Louis-Napoléon Bonaparte~Napoléon Ier~Thiers", 1,
     "Louis-Napoléon Bonaparte est élu président, puis devient empereur en 1852."),
 QT("Expliquer comment la souveraineté nationale transforme la légitimité du pouvoir en 1789.",
     "Sous l'Ancien Régime, le roi tire sa légitimité du droit divin et de la tradition. La Révolution déplace cette légitimité vers la nation : l'article 3 de la Déclaration de 1789 affirme que la souveraineté réside essentiellement dans la nation et que nul corps, nul individu ne peut exercer une autorité qui n'en émane. Cela implique une assemblée élue, des lois votées par des représentants et des citoyens égaux devant la loi. Le passage de la monarchie absolue à la monarchie constitutionnelle, puis à la République, traduit cette mutation : le pouvoir ne s'impose plus par naissance mais par la volonté collective exprimée par des institutions.",
     "On oppose droit divin et souveraineté nationale, puis on cite la Déclaration et ses conséquences institutionnelles."),
 QT("Décrire les étapes qui mènent du Directoire au Second Empire.",
     "Le Directoire, installé en 1795, est un régime fragile divisé entre royalistes et républicains. Bonaparte renverse le Directoire le 18 Brumaire an VIII (9 novembre 1799) et établit le Consulat, régime autoritaire qu'il domine comme Premier Consul. En 1804, il se fait proclamer empereur et promulgue le Code civil. Après sa défaite en 1814 et les Cent-Jours, la Restauration ramène les Bourbons, puis la monarchie de Juillet arrive au pouvoir en 1830. La révolution de 1848 instaure la IIe République et élit Louis-Napoléon président ; celui-ci organise un coup d'État le 2 décembre 1851, se fait proclamer empereur en 1852 et fonde le Second Empire, renversé après la défaite de 1870.",
     "On suit l'ordre chronologique en nommant chaque régime et l'événement qui le fait passer au suivant.")],
C("De 1789 à 1871, la France invente une légitimité nationale et républicaine à travers des régimes successifs et des conflits.",
  "Souveraineté nationale = le pouvoir émane de la nation",
  "1789 : Droits de l'homme · 1792 : République · 1804 : Code civil · 1848 : suffrage universel",
  "Revolution 1789~Fin de l'Ancien Regime~Droits de l'homme~Egalite juridique~Convention~Terreur et execution~Consulat~Bonaparte au pouvoir~Code civil~Egalite devant la loi",
  "Situer l'evenement dans le temps|Identifier le regime au pouvoir|Preciser l'acteur principal|Expliquer la rupture|Relier aux libertés publiques",
  "Confondre 1789 et 1792|Placer la Terreur avant la République|Mélanger Consulat et Directoire|Oublier le suffrage universel de 1848",
  "1789~Declaration des droits~1792~Proclamation de la Republique~1793~Execution de Louis XVI~1804~Code civil~1848~Suffrage universel",
  "Monarchie absolue~Pouvoir de droit divin~Monarchie constitutionnelle~Pouvoir limite par une assemblee",
  "Terreur~Repression politique~Thermidor~Chute de Robespierre"))

# ============================================================ HG2
add("HG2", "La Première Guerre mondiale et ses suites", "Histoire-géo", ["2nde pro"],
S("La Première Guerre mondiale éclate en juillet 1914 après l'assassinat de l'archiduc François-Ferdinand à Sarajevo."
  "|Les empires centraux (Allemagne, Autriche-Hongrie, Empire ottoman, Bulgarie) s'opposent aux Alliés (France, Royaume-Uni, Russie, puis Italie et États-Unis)."
  "|La guerre de mouvement laisse rapidement place à une guerre de position sur le front occidental, avec un réseau de tranchées."
  "|La bataille de Verdun, en 1916, symbolise l'endurance des soldats et l'ampleur des pertes des deux camps."
  "|La guerre totale mobilise les économies, les populations civiles et les empires coloniaux : usines, transports et propagande sont mis au service du conflit."
  "|Les soldats subissent des conditions extrêmes : boue, gaz de combat, maladie et violence de masse."
  "|Les mutineries de 1917 et la révolution russe de février puis d'octobre 1917 changent le cours du conflit."
  "|L'entrée en guerre des États-Unis en avril 1917 apporte un soutien matériel et humain décisif aux Alliés."
  "|L'armistice est signé le 11 novembre 1918 ; le traité de Versailles en juin 1919 impose des conditions sévères à l'Allemagne."
  "|La Société des Nations est créée pour garantir la paix et la coopération internationale, mais elle reste fragile."
  "|La carte de l'Europe est redessinée : dislocation des empires centraux, naissance de nouveaux États en Europe centrale et orientale."
  "|Le coût humain est considérable : environ dix millions de morts militaires et des millions de blessés et de civils touchés."),
[QC("Quel événement déclenche la guerre en 1914 ?", "L'assassinat de Sarajevo~Le traité de Versailles~La révolution russe~La bataille de Verdun", 0,
     "L'attentat contre François-Ferdinand le 28 juin 1914 déclenche la crise de juillet."),
 QC("Quel type de guerre domine sur le front occidental ?", "Une guerre de mouvement~Une guerre de position~Une guerre navale seule~Une guerre coloniale seule", 1,
     "Les tranchées et la stabilisation du front caractérisent la guerre de position."),
 QC("En quelle année a lieu la bataille de Verdun ?", "1914~1915~1916~1918", 2,
     "Verdun dure de février à décembre 1916."),
 QC("Quand les États-Unis entrent-ils en guerre ?", "1914~1916~Avril 1917~1918", 2,
     "Les États-Unis déclarent la guerre à l'Allemagne en avril 1917."),
 QC("Quelle est la date de l'armistice ?", "11 novembre 1918~28 juin 1919~8 mai 1945~14 juillet 1914", 0,
     "L'armistice est signé le 11 novembre 1918 à 11 heures."),
 QC("Quel traité est signé en juin 1919 avec l'Allemagne ?", "Versailles~Utrecht~Vienne~Paris", 0,
     "Le traité de Versailles est signé le 28 juin 1919."),
 QC("Quelle organisation est créée après la guerre pour garantir la paix ?", "La Société des Nations~L'Union européenne~L'ONU~L'OTAN", 0,
     "La SDN voit le jour en 1920 ; l'ONU sera créée en 1945."),
 QT("Expliquer le passage de la guerre de mouvement à la guerre de position sur le front occidental.",
     "En août 1914, les armées avancent rapidement : c'est la guerre de mouvement. Après la bataille de la Marne, en septembre 1914, les deux camps sont épuisés et creusent des tranchées pour se protéger. Le front se stabilise de la mer du Nord à la frontière suisse : c'est la guerre de position. Les soldats vivent dans des tranchées boueuses, protégées par des réseaux de fil de fer, sous le feu de l'artillerie et des gaz. Les offensives coûtent très cher en vies humaines pour des gains territoriaux minimes, comme à Verdun en 1916. Cette situation explique la violence de masse et l'usure des armées.",
     "On relie la Marne, le creusement des tranchées et les conséquences sur les pertes et l'usure."),
 QT("Décrire les principales conséquences de la Première Guerre mondiale en Europe.",
     "Le conflit provoque la dislocation des empires allemand, autrichien, ottoman et russe. De nouveaux États apparaissent en Europe centrale et orientale, comme la Pologne, la Tchécoslovaquie ou la Yougoslavie. Le traité de Versailles impose à l'Allemagne des pertes territoriales, des réparations et une limitation de son armée, ce qui nourrit un ressentiment durable. La Société des Nations est créée pour organiser la paix mais peine à s'imposer. Sur le plan humain, dix millions de soldats meurent, des millions de blessés et de civils sont touchés, et la guerre totale a transformé l'économie et la place des femmes dans la société.",
     "On attend la redessination de la carte, le traitement de l'Allemagne, la SDN et le bilan humain.")],
C("La Première Guerre mondiale est une guerre totale et de position qui bouleverse durablement l'Europe et ses institutions.",
  "Guerre totale = mobilisation des civils, de l'économie et des empires",
  "1914 : Sarajevo · 1916 : Verdun · 1917 : entrée des États-Unis · 1918 : armistice",
  "Sarajevo~Declencheur~Guerre de position~Tranchees~Verdun~Symbole des pertes~Guerre totale~Economie et civils~Versailles~Traite de 1919",
  "Situer la date et le lieu|Identifier les belligérants|Preciser le type de guerre|Mesurer les consequences|Relier au monde de l'apres-guerre",
  "Confondre 1914 et 1918|Placer Verdun en 1914|Citer l'ONU pour 1919|Oublier les empires coloniaux",
  "28 juin 1914~Sarajevo~1916~Verdun~Avril 1917~Entree des Etats-Unis~11 novembre 1918~Armistice~Juin 1919~Versailles",
  "Guerre de mouvement~Avancee rapide~Guerre de position~Tranchees stables",
  "SDN~Societe des Nations~ONU~Organisation de 1945"))

# ============================================================ HG3
add("HG3", "La Seconde Guerre mondiale et la Résistance", "Histoire-géo", ["2nde pro"],
S("La Seconde Guerre mondiale commence le 1er septembre 1939 par l'invasion de la Pologne par l'Allemagne nazie."
  "|La France déclare la guerre le 3 septembre 1939 ; la période de la « drôle de guerre » précède l'offensive allemande de mai 1940."
  "|La défaite de juin 1940 conduit à l'armistice du 22 juin et à l'occupation du nord de la France, tandis que le régime de Vichy s'installe au sud."
  "|Le 18 juin 1940, le général de Gaulle lance depuis Londres un appel à la résistance, refusant l'armistice."
  "|La France libre, les Forces françaises libres et le mouvement de résistance intérieure se structurent progressivement."
  "|Le régime de Vichy applique une politique de collaboration avec l'Allemagne et met en œuvre la persécution des juifs."
  "|La rafle du Vél d'Hiv, en juillet 1942, est l'une des étapes de la déportation des juifs de France vers les camps d'extermination."
  "|La résistance se manifeste par les maquis, les sabotages, les journaux clandestins et les réseaux d'évasion, avec des figures comme Jean Moulin."
  "|La Libération s'engage après le débarquement de Normandie, le 6 juin 1944, puis la libération de Paris en août 1944."
  "|La conférence de Yalta en février 1945 organise la fin de la guerre et le partage de l'Europe en zones d'influence."
  "|La guerre se termine en Europe le 8 mai 1945 avec la capitulation sans condition de l'Allemagne, puis en Asie en septembre 1945."
  "|Le bilan est terrible : des dizaines de millions de morts, la Shoah, et une Europe divisée qui annonce la Guerre froide."),
[QC("Quelle est la date du début de la Seconde Guerre mondiale ?", "1er septembre 1939~3 septembre 1939~22 juin 1940~6 juin 1944", 0,
     "L'Allemagne envahit la Pologne le 1er septembre 1939."),
 QC("Quel régime s'installe dans le sud de la France après l'armistice ?", "La France libre~Le régime de Vichy~La IIIe République~La Commune", 1,
     "Le régime de Vichy, dirigé par Pétain, s'installe en zone non occupée."),
 QC("Que lance le général de Gaulle le 18 juin 1940 ?", "Un appel à la collaboration~Un appel à la résistance~Un armistice~Une offensive", 1,
     "L'appel du 18 juin refuse l'armistice et invite à continuer le combat."),
 QC("Quand a lieu la rafle du Vél d'Hiv ?", "1940~1941~Juillet 1942~1944", 2,
     "Les 16 et 17 juillet 1942, plus de 13 000 personnes sont arrêtées à Paris."),
 QC("Qui est une figure majeure de la résistance intérieure ?", "Philippe Pétain~Jean Moulin~Pierre Laval~Adolf Hitler", 1,
     "Jean Moulin unifie les mouvements de résistance au sein du CNR."),
 QC("Quelle est la date du débarquement de Normandie ?", "6 juin 1944~8 mai 1945~22 juin 1940~1er septembre 1939", 0,
     "Le débarquement allié a lieu le 6 juin 1944, jour J."),
 QC("Quand l'Allemagne capitule-t-elle en Europe ?", "8 mai 1945~6 juin 1944~2 septembre 1945~11 novembre 1918", 0,
     "La capitulation sans condition est signée le 8 mai 1945."),
 QT("Expliquer la différence entre la résistance intérieure et la France libre.",
     "La résistance intérieure regroupe les mouvements nés en France occupée : maquis, sabotages, presse clandestine, réseaux d'évasion. Elle agit dans des conditions de clandestinité et sous la menace de la répression. La France libre, animée par de Gaulle depuis Londres, rassemble les Forces françaises libres et les territoires qui ont répondu à l'appel du 18 juin ; elle combat aux côtés des Alliés et dispose d'une reconnaissance internationale croissante. Jean Moulin a précisément pour mission de coordonner les mouvements intérieurs avec la France libre, aboutissant à la création du Conseil national de la Résistance en 1943.",
     "On oppose clandestinité intérieure et combat extérieur allié, puis on cite le rôle de coordination."),
 QT("Décrire les étapes de la Libération de la France en 1944.",
     "Le débarquement de Normandie, le 6 juin 1944, ouvre un second front en Europe. Les forces alliées et la résistance intérieure coordonnent leurs actions : sabotages des voies ferrées, insurrections locales et maquis facilitent l'avancée. Paris se libère en août 1944 après l'insurrection parisienne et l'arrivée de la 2e Division blindée du général Leclerc ; de Gaulle y prononce un discours le 25 août. Le régime de Vichy s'effondre et le Gouvernement provisoire de la République française s'installe. Les combats se poursuivent jusqu'à la capitulation de l'Allemagne le 8 mai 1945.",
     "On suit l'ordre : jour J, coordination avec la résistance, libération de Paris, chute de Vichy et capitulation.")],
C("La Seconde Guerre mondiale oppose les Alliés à l'Axe ; en France, défaite, occupation, collaboration et résistance s'entrelacent.",
  "Appel du 18 juin : refus de l'armistice et poursuite du combat",
  "1939 : invasion de la Pologne · 1940 : défaite · 1944 : Libération · 1945 : capitulation",
  "Occupation~Zone nord sous autorite allemande~Vichy~Collaboration~Appel du 18 juin~Refus de l'armistice~Resistance~Maquis et sabotages~Liberation~Jour J et Paris",
  "Situer la date|Identifier le camp et les acteurs|Preciser le territoire|Expliquer la rupture|Mesurer le bilan humain",
  "Confondre les deux guerres mondiales|Placer l'appel du 18 juin en 1944|Oublier la collaboration de Vichy|Ignorer la Shoah",
  "1er septembre 1939~Invasion de la Pologne~22 juin 1940~Armistice~Juillet 1942~Rafle du Vel d'Hiv~6 juin 1944~Jour J~8 mai 1945~Capitulation",
  "Resistance interieure~Clandestinite en France~France libre~Londres et forces francaises libres",
  "Collaboration~Accord avec l'occupant~Resistance~Refus et combat"))

# ============================================================ HG4
add("HG4", "L'aménagement du territoire et les mobilités en France", "Histoire-géo", ["1re pro"],
S("L'aménagement du territoire vise à répartir les activités, les populations et les équipements de façon équilibrée sur l'espace national."
  "|La France se caractérise par un fort contraste entre des métropoles dynamiques et des espaces ruraux ou périurbains moins dotés."
  "|Paris exerce une attractivité considérable : c'est le principal centre de décision, de finance et d'innovation du pays."
  "|Les grandes métropoles régionales, comme Lyon, Marseille, Lille ou Bordeaux, structurent l'espace et rayonnent sur leur région."
  "|La métropolisation renforce la concentration des emplois qualifiés et des services dans les grandes villes."
  "|La périurbanisation traduit le départ des habitants des centres vers les communes périphériques, souvent à la recherche de logements moins chers."
  "|Les espaces ruraux connaissent des situations contrastées : certains se dépeuplent, d'autres attirent de nouveaux habitants ou développent le tourisme."
  "|Les politiques d'aménagement s'appuient sur la DATAR, créée en 1963, et sur des dispositifs comme les pôles de compétitivité ou les CPER."
  "|La décentralisation transfère des compétences de l'État vers les collectivités territoriales : régions, départements et communes."
  "|Les grands axes de communication, autoroutes, lignes à grande vitesse et connections numériques, orientent les flux et l'implantation des activités."
  "|Les mobilités domicile-travail génèrent des flux quotidiens et posent des enjeux de transport, de logement et d'environnement."
  "|Les inégalités territoriales d'accès aux services publics, à l'emploi et au logement restent un enjeu majeur des politiques publiques."),
[QC("Qu'appelle-t-on métropolisation ?", "Le départ des habitants des villes~La concentration des activités dans les grandes métropoles~Le repeuplement rural~La fermeture des administrations", 1,
     "La métropolisation renforce le poids économique et démographique des grandes villes."),
 QC("Quel organisme créé en 1963 pilote l'aménagement du territoire ?", "L'INSEE~La DATAR~Le CNRS~L'ONU", 1,
     "La DATAR, devenue France 2030 dans ses missions, a été créée en 1963."),
 QC("Que désigne la périurbanisation ?", "Le retour vers les centres-villes~L'installation en périphérie des villes~La création de nouvelles regions~La baisse de la population", 1,
     "Les ménages s'installent dans les communes autour des villes, souvent en maison individuelle."),
 QC("Quelle collectivité est chargée du développement économique régional ?", "La commune~Le département~La région~L'intercommunalité", 2,
     "La région est chef de file du développement économique et de la formation."),
 QC("Quel effet a une ligne à grande vitesse sur un territoire ?", "Elle isole la région~Elle rapproche le territoire des grands centres~Elle supprime les emplois~Elle n'a aucun effet", 1,
     "Les infrastructures de transport réduisent le temps d'accès et peuvent attirer des activités."),
 QC("Quel est un enjeu majeur des mobilités domicile-travail ?", "La gratuité des logements~La congestion et l'accès au logement~La disparition des transports~L'absence de flux", 1,
     "Les déplacements quotidiens posent des questions de transport, de coût et d'étalement urbain."),
 QC("Quel territoire est généralement le plus attractif en France ?", "La zone rurale éloignée~L'agglomération parisienne~Le massif montagneux~Le littoral peu équipé", 1,
     "Paris et son agglomération concentrent décisions, emplois et services."),
 QT("Expliquer pourquoi les métropoles attirent les activités et les populations.",
     "Les métropoles offrent une forte densité d'emplois, surtout dans les secteurs de la finance, de l'innovation et des services aux entreprises. Elles concentrent les universités, les laboratoires, les grands équipements culturels et de santé, ainsi que les réseaux de transport. Cette diversité crée un effet d'agglomération : les entreprises s'installent là où se trouvent les compétences et les clients, ce qui attire à son tour de nouveaux habitants. Le revers de cette attractivité est la cherté du logement, la congestion et une pression sur les services, ce qui pousse une partie des ménages vers la périurbie.",
     "On cite emplois, services, réseaux et effet d'agglomération, puis les effets induits."),
 QT("Comment une politique d'aménagement peut-elle réduire les inégalités territoriales ?",
     "Elle peut d'abord améliorer l'accessibilité en développant les infrastructures de transport et le très haut débit, afin que les territoires éloignés ne soient pas pénalisés. Elle peut ensuite soutenir l'emploi local par des pôles de compétitivité, des aides aux entreprises et la formation professionnelle adaptée aux besoins régionaux. Le maintien ou la création de services publics de proximité, comme les maisons France services, les écoles ou les centres de santé, est un autre levier. Enfin, la décentralisation permet aux collectivités locales d'adapter leurs actions aux réalités du terrain, sous réserve de moyens financiers suffisants et d'une évaluation régulière des résultats.",
     "On attend accessibilité, soutien à l'emploi, services publics, décentralisation et évaluation.")],
C("L'aménagement du territoire cherche à corriger les déséquilibres entre métropoles attractives et espaces moins dotés.",
  "Métropolisation = concentration des emplois et des services",
  "DATAR (1963) · décentralisation · axes de transport · services publics de proximité",
  "Metropolisation~Concentration des activites~Grandes villes~Periurbanisation~Installation en peripherie~References~Ruralite~Desequilibre~Amenagement~Politique publique",
  "Localiser les territoires|Mesurer les flux et les contrasts|Identifier les acteurs|Analyser les politiques|Evaluer les effets",
  "Confondre périurbanisation et métropolisation|Ignorer le rôle des transports|Croire que l'État agit seul|Oublier les inégalités de services",
  "Paris~Principal centre de decision~DATAR~Creee en 1963~Region~Chef de file economique~LGV~Temps d'acces reduit~France services~Proximite",
  "Metropole~Emplois et services denses~Espace rural~Faible densite et vieillissement",
  "Amenagement~Corriger les ecarts~Decentralisation~Transfert de competences"))

# ============================================================ AN1
add("AN1", "English tenses in everyday professional situations", "Anglais", ["2nde pro"],
S("English uses tenses to locate an action in time and to express its aspect: completed, ongoing or repeated."
  "|The present simple describes habits, routines and general facts: « I check the invoices every morning »."
  "|With third-person singular subjects, the present simple takes an -s ending: she works, he manages, it contains."
  "|The present continuous describes an action in progress at the moment of speaking: « I am preparing the report »."
  "|The past simple describes a completed action at a definite past time, often with yesterday, last week or in 2020."
  "|Regular verbs form the past simple with -ed, while irregular verbs have specific forms: go/went, take/took, write/wrote."
  "|The present perfect links a past action to the present: « The client has already signed the contract »."
  "|Signal words such as already, yet, ever and never commonly accompany the present perfect."
  "|The future with will expresses a decision made at the moment of speaking or a prediction: « I will send the file »."
  "|Going to expresses an intention or a plan already made: « We are going to launch the product in June »."
  "|Negatives and questions usually require auxiliary verbs: do/does for the present simple, did for the past simple."
  "|In professional writing, choosing the right tense makes the difference between a routine, a finished task and a planned action : identify the time marker first, then the aspect, and finally check the auxiliary and the verb form."),
[QC("Which tense describes a regular habit?", "Present continuous~Present simple~Past simple~Future with will", 1,
     "The present simple is used for routines and repeated actions."),
 QC("How do you form the third person singular of the present simple?", "Add -ing~Add -s or -es~Add -ed~Use will", 1,
     "She works, he watches: the verb takes -s or -es."),
 QC("Which sentence uses the present continuous?", "I work in a bank~I am working on the file now~I worked yesterday~I will call you", 1,
     "The present continuous is be + -ing and describes an action in progress."),
 QC("Which word is typical of the present perfect?", "Yesterday~Already~Last year~Tomorrow", 1,
     "Already, yet, ever and never are common markers of the present perfect."),
 QC("What is the past simple of « write »?", "Writed~Wrote~Written~Writing", 1,
     "Write is irregular: write / wrote / written."),
 QC("Which form expresses a plan already made?", "Will~Going to~Past simple~Present perfect", 1,
     "Going to expresses an intention decided before the moment of speaking."),
 QC("Which auxiliary is used for a question in the past simple?", "Do~Does~Did~Will", 2,
     "Did you send the email? The main verb stays in the base form."),
 QT("Choose the correct tense and explain: « I (to wait) for the client since 9 a.m. »",
     "The correct form is « I have been waiting for the client since 9 a.m. » The word « since » introduces a starting point in the past and the action is still continuing in the present, which calls for the present perfect continuous: have/has been + -ing. The present perfect simple (« I have waited ») would be possible but less natural here because it emphasizes the result rather than the duration. The past simple would be wrong because the waiting is not finished.",
     "On attend le present perfect continuous et l'explication liée à since et à la durée encore en cours."),
 QT("Explain the difference between « I will call you » and « I am going to call you » in a work context.",
     "« I will call you » presents the decision as taken at the moment of speaking, often in response to a new piece of information: the speaker decides now to make the call. « I am going to call you » presents the call as an intention or plan that already existed, for example one noted in the agenda before the conversation. The first form is also used for predictions, while the second suggests that arrangements have been made. In professional communication this distinction helps show whether a commitment is spontaneous or already planned.",
     "On oppose décision spontanée et intention antérieure, avec un exemple professionnel.")],
C("English tenses combine time and aspect: the time marker guides the choice, the verb form expresses the aspect.",
  "Present simple : routine · present continuous : in progress · past simple : finished",
  "Present perfect : past linked to present · will : decision now · going to : prior plan",
  "Present simple~Habits and facts~Every morning~Present continuous~Action in progress~Right now~Past simple~Completed action~Yesterday",
  "Repérer le marqueur de temps|Identifier l'aspect de l'action|Choisir le temps adapté|Conjuguer l'auxiliaire|Vérifier la forme du verbe",
  "Employer le present simple pour une action en cours|Oublier le -s de la 3e personne|Confondre will et going to|Utiliser le passe simple avec since",
  "I check invoices~Routine~I am preparing~En cours~I sent~Action finie~I have signed~Lien avec le present~Since 9 a.m.~Duree en cours",
  "Will~Decision au moment ou l'on parle~Going to~Intention deja formee",
  "Present perfect~Lien passe-present~Past simple~Action achevee et datee"))

# ============================================================ AN2
add("AN2", "Professional email and commercial correspondence in English", "Anglais", ["1re pro", "Terminale pro"],
S("A professional email must be clear, concise and adapted to the relationship with the recipient."
  "|The subject line summarizes the purpose of the message in a few words so that it can be filed and found easily."
  "|The salutation depends on the level of formality: « Dear Ms Martin » is formal, « Hello Paul » is neutral, « Hi » is informal."
  "|The opening states the reason for writing: « I am writing to confirm our meeting of 12 June »."
  "|The body is organized into short paragraphs, each dealing with one point, often introduced by bullet points."
  "|Requests should be polite and precise: « Could you please send me the updated quotation by Friday? »"
  "|Attachments must be announced in the body: « Please find attached the signed agreement »."
  "|The closing formula echoes the salutation: « Kind regards » is standard, « Yours sincerely » is used when the name is known."
  "|A signature block includes the full name, job title, company, phone number and sometimes the company logo."
  "|Business letters are more formal than emails and often include the sender's and recipient's addresses and a date."
  "|Tone and register must avoid slang, excessive abbreviations and emotional language in professional exchanges."
  "|Proofreading checks spelling, grammar, the spelling of names, the accuracy of dates and the presence of attachments : a good message lets the recipient understand the request and act without asking for clarification."),
[QC("What should the subject line of a professional email contain?", "The whole message~A short summary of the purpose~Only the date~The sender's address", 1,
     "The subject line states the purpose in a few words so the message can be classified."),
 QC("Which salutation is the most formal?", "Hi Paul~Hello Paul~Dear Ms Martin~Hey", 2,
     "Dear + title and surname is the formal register."),
 QC("How do you politely introduce an attachment?", "Look at the file~Please find attached the document~I put a file~See file", 1,
     "Please find attached is the standard professional formula."),
 QC("Which closing is standard in a neutral professional email?", "Cheers mate~Kind regards~See you~Bye now", 1,
     "Kind regards suits most professional contexts."),
 QC("What must a signature block normally include?", "Only a first name~Full name, job title and company~A photo only~The company's address only", 1,
     "The signature identifies the sender and gives a way to contact them."),
 QC("Why should a message be divided into short paragraphs?", "To look longer~To make the request easy to follow~To avoid using verbs~To hide the attachments", 1,
     "One idea per paragraph improves readability and actionability."),
 QC("What does proofreading include?", "Only spelling~Names, dates, grammar and attachments~Only the subject line~Nothing, the software corrects everything", 1,
     "Names and dates are critical details in business correspondence."),
 QT("Write the opening and closing of a formal email requesting an updated quotation, then explain your choices.",
     "Opening: « Dear Mr Dupont, I am writing to request an updated quotation for the supply of office furniture, following our telephone conversation of 6 May. » Closing: « Thank you for your help. I look forward to receiving your reply by 15 May. Kind regards, [Full name], Purchasing Assistant, [Company]. » The salutation uses the title and surname because the recipient is known and the context is formal. The opening states the purpose and a precise reference immediately. The closing includes a clear deadline and a standard formula, followed by a complete signature block so the recipient can identify and contact the sender.",
     "On attend une ouverture qui annonce l'objet, une formule de clôture adaptée et une signature complète."),
 QT("Explain three common mistakes in professional emails and how to avoid them.",
     "First, a vague subject such as « Hello » prevents the recipient from classifying the message: it should state the topic and, if useful, a reference number. Second, a long undifferentiated paragraph hides the request: the writer should use short paragraphs or bullet points and put the action required in a prominent position. Third, forgetting an attachment while writing « please find attached » forces a follow-up email: the file must actually be added and named clearly before sending. In all three cases the rule is the same: think about what the recipient needs in order to act without a further exchange.",
     "On attend trois erreurs concrètes et une parade pour chacune.")],
C("A professional email is judged by its clarity and by the ease with which the recipient can act on it.",
  "Subject + salutation + purpose + body + closing + signature",
  "Formal : Dear Ms X / Yours sincerely · neutral : Kind regards",
  "Subject~Purpose in a few words~Salutation~Dear and surname~Opening~Reason for writing~Attachment~Please find attached~Signature~Name and role",
  "Choisir le registre|Rédiger un objet precis|Annoncer l'objet des la premiere phrase|Structurer le corps|V?rifier la pi?ce jointe et signature",
  "Objet vague ou absent~Langage familier~Oublier la piece jointe~Signature incomplete",
  "Dear Ms Martin~Registre formel~Please find attached~Annonce de piece jointe~Kind regards~Formule standard~By 15 May~Echeance precis",
  "Formal~Dear Ms Martin~Informal~Hi or Hello",
  "Email~Rapide et neutre~Lettre commerciale~Plus formelle et datee"))

# ============================================================ EM1
add("EM1", "Les valeurs de la République et la laïcité", "EMC", ["2nde pro"],
S("L'enseignement moral et civique vise à former des citoyens capables de vivre ensemble et d'exercer leur citoyenneté."
  "|Les valeurs de la République sont la liberté, l'égalité, la fraternité, auxquelles s'ajoutent la laïcité et le respect de la dignité humaine."
  "|La liberté permet à chacun d'agir et de s'exprimer dans le respect des droits d'autrui et de l'ordre public."
  "|L'égalité signifie que tous les citoyens sont égaux devant la loi et bénéficient des mêmes droits, sans discrimination."
  "|La fraternité implique la solidarité entre les membres de la communauté nationale et le refus de l'exclusion."
  "|La laïcité garantit la liberté de conscience et le libre exercice des cultes, tout en assurant la neutralité de l'État."
  "|La loi de 1905 sur la séparation des Églises et de l'État est le texte fondateur de la laïcité française."
  "|La neutralité s'impose aux agents publics dans l'exercice de leurs fonctions, mais pas aux usagers dans leur vie privée."
  "|Les signes d'appartenance religieuse sont interdits aux agents publics en service et dans les écoles publiques pour les élèves depuis 2004."
  "|Le principe de dignité humaine interdit toute atteinte à la personne, qui ne peut être traitée comme un simple moyen."
  "|La citoyenneté s'exerce par des droits et des devoirs : vote, expression, solidarité, respect des lois et des institutions."
  "|Dans un contexte professionnel, ces principes encadrent l'accueil, la neutralité du service et le traitement équitable des usagers."),
[QC("Quelles sont les trois valeurs de la devise républicaine ?", "Liberté, Égalité, Fraternité~Paix, Travail, Famille~Ordre, Travail, Patrie~Justice, Santé, Solidarité", 0,
     "La devise de la République française est Liberté, Égalité, Fraternité."),
 QC("Quel texte fonde la laïcité française ?", "La Déclaration de 1789~La loi de 1905~Le Code civil~La Constitution de 1958", 1,
     "La loi du 9 décembre 1905 sépare les Églises et l'État."),
 QC("La laïcité garantit d'abord…", "L'interdiction de toutes les religions~La liberté de conscience~Le financement des cultes~L'officialisation d'une religion", 1,
     "Elle protège la liberté de croire ou de ne pas croire et le libre exercice des cultes."),
 QC("À qui s'impose la neutralité dans la fonction publique ?", "À tous les citoyens en permanence~Aux agents publics dans l'exercice de leurs fonctions~Aux seuls enseignants~Aux seuls élèves", 1,
     "Les agents publics sont neutres en service ; les usagers gardent leur liberté.", ),
 QC("Quel principe interdit de traiter une personne comme un simple moyen ?", "La liberté d'expression~La dignité humaine~La souveraineté~La laïcité", 1,
     "La dignité de la personne humaine est un principe fondamental du droit."),
 QC("Quelle est une conséquence de l'égalité devant la loi ?", "Des droits différents selon l'origine~L'absence de discrimination~Des privilèges de naissance~Une justice privée", 1,
     "Tous les citoyens bénéficient des mêmes droits et sont soumis aux mêmes lois."),
 QC("Comment se manifeste la citoyenneté ?", "Uniquement par le vote~Par des droits et des devoirs~Par l'obéissance aveugle~Par le refus des institutions", 1,
     "On est citoyen par des droits exercés et des devoirs respectés."),
 QT("Expliquer en quoi la laïcité protège à la fois la liberté de conscience et l'égalité des citoyens.",
     "La laïcité sépare l'État des religions : l'État ne reconnaît aucun culte officiel et garantit à chacun la liberté de croire ou de ne pas croire. En même temps, cette neutralité assure l'égalité des citoyens : personne ne bénéficie d'un traitement favorable en raison de sa religion et personne n'est discriminé en raison de ses convictions. Les agent publics doivent être neutres en service pour que le service rendu soit identique pour tous les usagers. La laïcité n'est donc pas l'effacement des croyances, mais la condition de leur coexistence pacifique dans un espace public commun.",
     "On relie liberté de conscience, neutralité de l'État et égalité de traitement des usagers."),
 QT("Un usager porte un signe religieux dans un service public. Comment l'agent doit-il réagir et pourquoi ?",
     "L'agent doit accueillir la personne normalement, sans commentaire sur son signe religieux, car les usagers ne sont pas soumis à l'obligation de neutralité dans leur vie privée. Lui-même doit rester neutre : ni prosélytisme, ni hostilité, et il traite la demande comme celle de tout autre usager. Si le signe pose un problème de sécurité ou de bon fonctionnement du service, l'agent en réfère à sa hiérarchie et applique le règlement intérieur, sans jugement de valeur. Cette attitude respecte à la fois la liberté de conscience de l'usager, l'égalité de traitement et l'obligation de neutralité du service public.",
     "On distingue la situation de l'usager de celle de l'agent, puis on rappelle neutralité et égalité de traitement.")],
C("La laïcité et les valeurs républicaines organisent le vivre-ensemble et le service rendu à tous les citoyens.",
  "Liberté, Égalité, Fraternité + laïcité + dignité humaine",
  "Loi de 1905 : séparation des Églises et de l'État · neutralité des agents publics",
  "Liberte~Agir et s'exprimer~Egalite~Meme droit pour tous~Fraternite~Solidarite~Laicite~Liberte de conscience~Neutralite~Neutralite des agents",
  "Identifier la valeur en jeu|Preciser le cadre legal|Distinguer agent et usager|Verifier l'egalite de traitement|Expliquer la decision",
  "Croire que la laicite interdit les religions|Confondre neutralite de l'agent et de l'usager|Oublier la loi de 1905|Ignorer la dignite humaine",
  "1905~Separation des Eglises et de l'Etat~2004~Signes religieux a l'ecole~Agent public~Neutralite en service~Usager~Liberte conserve",
  "Neutralite~Neutralite de l'agent~Liberte de conscience~Droit de l'usager",
  "Egalite~Traitement identique~Discrimination~Traitement different"))

# ============================================================ ME1
add("ME1", "La fiche de lecture et la note de synthèse", "Méthodologie", ["2nde pro"],
S("La fiche de lecture est un outil de travail qui restitue l'essentiel d'un document de façon courte, structurée et fidèle."
  "|Elle commence par la présentation : auteur, titre, date de publication, nature du document et contexte."
  "|La problématique est la question centrale à laquelle le document cherche à répondre ; elle oriente toute la lecture."
  "|Le plan suit la progression de l'auteur : on respecte les grandes parties et on les résume dans l'ordre."
  "|Résumer consiste à reformuler les idées avec ses propres mots, sans ajouter d'opinion personnelle."
  "|La citation est courte, placée entre guillemets, et toujours accompagnée de la référence de la page."
  "|La note de synthèse combine plusieurs documents sur un même sujet et dégage les informations communes et les divergences."
  "|Une synthèse ne juxtapose pas les documents : elle les croise et construit un plan thématique."
  "|Les connecteurs logiques (d'abord, mais, cependant, par conséquent) rendent explicites les relations entre les idées."
  "|La conclusion apporte une réponse synthétique à la problématique et, si besoin, une ouverture."
  "|La rigueurdocumentaire exige de distinguer ce que dit l'auteur, ce que l'on cite et ce que l'on interprète."
  "|Une bonne fiche est relue pour vérifier l'exactitude des chiffres, la présence des références et l'absence de copie littérale."),
[QC("Que contient la présentation d'une fiche de lecture ?", "Seulement le titre~Auteur, titre, date et nature du document~L'avis personnel du lecteur~La conclusion", 1,
     "La présentation identifie précisément le document et son contexte."),
 QC("Qu'est-ce qu'une problématique ?", "Le résumé de la conclusion~La question centrale du document~La liste des références~La biographie de l'auteur", 1,
     "Elle oriente la lecture et structure la synthèse."),
 QC("Comment résumer une idée ?", "En copiant mot pour mot~En reformulant avec ses propres mots~En ajoutant son avis~En supprimant les chiffres", 1,
     "La reformulation garantit la compréhension et évite le plagiat."),
 QC("Comment signaler une citation ?", "Sans guillemets~Entre guillemets avec la page~En italique sans référence~En majuscules", 1,
     "Les guillemets et la référence de page sont indispensables."),
 QC("Quelle est la différence entre fiche et synthèse ?", "La fiche porte sur un document, la synthèse en croise plusieurs~La synthèse est plus courte~Elles sont identiques~La fiche est toujours orale", 0,
     "La fiche analyse un document ; la synthèse en croise plusieurs sur un thème."),
 QC("Quel plan privilégier pour une synthèse de plusieurs textes ?", "Un plan par document~Un plan thématique~Un plan chronologique imposé~Aucun plan", 1,
     "Le plan thématique permet de croiser les documents plutôt que de les aligner."),
 QC("Que vérifier à la relecture finale ?", "La longueur seulement~Les chiffres, les références et l'absence de copie~Le nombre de paragraphes~La couleur du support", 1,
     "La fiabilité documentaire est la priorité de la relecture."),
 QT("Décrire la méthode pour réaliser une fiche de lecture en cinq étapes.",
     "On lit d'abord le document dans son ensemble pour identifier le thème et la problématique. On relève ensuite les références bibliographiques complètes : auteur, titre, date, éditeur. On dégage le plan en notant les idées principales de chaque partie et les arguments qui les soutiennent. On rédige alors la fiche en reformulant, en insérant quelques citations courtes et en indiquant les pages. On termine par une relecture qui vérifie l'exactitude des chiffres, la présence des références, la clarté des connecteurs et l'absence de copie littérale.",
     "On attend cinq étapes ordonnées : lecture globale, références, plan, rédaction, relecture."),
 QT("Expliquer pourquoi une note de synthèse ne doit pas être un simple juxtaposition de résumés.",
     "Une juxtaposition présente les documents les uns après les autres sans les mettre en relation : le lecteur ne sait pas ce qui est commun, ce qui diverge et quelle conclusion tirer. La synthèse doit au contraire dégager un plan thématique, regrouper les informations qui se confirment, signaler les contradictions et préciser les nuances propres à chaque auteur. Elle construit ainsi une réponse à la problématique à partir de plusieurs sources, en citant précisément les documents à l'appui. C'est ce travail de croisement qui donne à la synthèse sa valeur et permet une décision ou une analyse argumentée.",
     "On oppose juxtaposition et croisement thématique, puis on souligne la réponse à la problématique.")],
C("Une fiche de lecture restitue fidèlement un document ; une note de synthèse croise plusieurs documents pour répondre à une question.",
  "Fiche = 1 document · Synthèse = plusieurs documents + plan thématique",
  "Présentation · problématique · plan · reformulation · citations · conclusion",
  "Fiche de lecture~Un seul document~Presentation~Auteur, titre, date~Problem~Question centrale~Synthese~Croisement de sources",
  "Lire l'ensemble du document|Relever les references|Degager le plan et les idees|Reformuler avec citations|Relire pour verifier",
  "Copier littéralement|Donner son avis dans le résumé|Oublier les références de page|Aligner les documents sans les croiser",
  "Auteur~Identite du document~Page~Reference de la citation~Themes~Plan de synthese~Connecteurs~Relations logiques",
  "Fiche~Un document~Synthese~Plusieurs documents croises",
  "Resume~Reformulation fidèle~Citation~Mots de l'auteur entre guillemets"))

# FIN DES LOTS
valider_et_ecrire(F, "pro-gestion-mat-part-A.json")
