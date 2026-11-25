# -*- coding: utf-8 -*-
"""Generateur st2s-mat-part-A.json — lot A : tronc commun (20 fiches).

ST2S (sciences et technologies de la sante et du social, lycee technologique).
Chaque fiche : 12 points, 9 questions (7 QCM + 2 texte), 7 blocs ordonnes,
3 schemas SVG. Aucune integration dans l'application.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_etapes,
                      svg_compare, bloc, valider_et_ecrire)

FIL = ["st2s"]
REF = (
    "Programmes du baccalaureat technologique ST2S : arrete du 21 juillet 2011 fixant les programmes "
    "d'enseignement conduisant au baccalaureat ST2S (Bulletin officiel special n 6 du 29 septembre 2011) "
    "et programmes renoves applicables a la rentree 2020 (Bulletin officiel special n 7 du 25 juillet 2019) ; "
    "tronc commun de la voie technologique : Bulletin officiel special n 1 du 22 janvier 2020 ; "
    "ressources eduscol (programmes, accompagnements et fiches ST2S)."
)

F = []


def S(x):
    return [p.strip() for p in x.split("|") if p.strip()]


def R(x):
    return [p.strip() for p in x.split("~") if p.strip()]


def Q(question, options, correct, correction):
    return qcm(question, R(options), correct, correction)


def T(question, reponse, correction):
    return qt(question, reponse, correction)


def _grid(x):
    cellules = R(x)
    if "|" not in x:
        return [cellules[i:i + 3] for i in range(0, 9, 3)]
    return [R(ligne) for ligne in S(x)]


def _cmp(x):
    cellules = R(x)
    n = len(cellules) // 2
    return (cellules[0], cellules[1:n]), (cellules[n], cellules[n + 1:])


def C(idea, eq, leg, grid, steps, traps, ex, cmp1, cmp2):
    return {"idea": idea, "eq": eq, "leg": leg, "grid": _grid(grid),
            "steps": S(steps), "traps": S(traps), "ex": [R(e) for e in S(ex)],
            "cmp": (_cmp(cmp1), _cmp(cmp2))}


def add(prefix, titre, matiere, annees, points, questions, c):
    titre_complet = prefix + " · " + titre
    short = titre.split(":")[0].strip()
    aff = [
        bloc("L'idee en une phrase", texte=c["idea"], type="intro"),
        bloc("La notion a maitriser", eq=c["eq"], leg=c["leg"], type="formule"),
        bloc("Tableau de lecture", items=c["grid"], type="grille"),
        bloc("Les points essentiels du chapitre", items=points[1:5], type="liste"),
        bloc("La demarche pas a pas", items=c["steps"], type="etapes"),
        bloc("Pieges et erreurs frequentes", items=c["traps"], type="attention"),
        bloc("En situation : exemples concrets", items=[
            "%s : <span class=\"cle\">%s</span>" % (p[0], p[1]) for p in c["ex"]
        ], type="exemples"),
    ]
    schema = [
        diag("1 · " + short, svg_grille(short, ["Notion", "Definition", "Repere"], c["grid"])),
        diag("2 · Demarche", svg_etapes("Procedure : " + short, c["steps"])),
        diag("3 · A distinguer", svg_compare(short, c["cmp"][0], c["cmp"][1])),
    ]
    assert len(points) == 12, prefix
    assert len(questions) == 9, prefix
    assert sum(1 for q in questions if q.get("type") == "qcm") == 7, prefix
    assert sum(1 for q in questions if q.get("type") == "texte") == 2, prefix
    assert len(aff) == 7 and len(schema) == 3, prefix
    F.append(fiche(FIL, annees, matiere, titre_complet, REF, points, questions, aff, schema))


# ============================================================ FR1
add("ST2S-A-FR01", "L'argumentation : these, arguments et refutation", "Français", ["1re"],
S("L'argumentation vise a convaincre ou a persuader en articulant une these et des arguments recevables."
  "|La these est l'idee principale defendue ; elle se formule en une phrase courte, discutable et verifiable."
  "|Le plan dialectique enchaine these, antithese puis synthese ; le plan thematique suit une progression d'idees."
  "|Un argument est une raison qui soutient la these : il doit etre pertinent, suffisant et acceptable."
  "|Les grands types d'arguments sont l'argument logique, l'exemple, l'autorite, l'analogie et le consentement universel."
  "|L'exemple rend l'idee concrete ; l'autorite cite une source reconnue qu'il faut identifier precisement."
  "|La refutation anticipe l'objection adverse, la discute, puis propose une synthese nuancee."
  "|Les connecteurs logiques (donc, car, or, mais, bien que) rendent visible la structure du raisonnement."
  "|Les trois registres de la persuasion sont le logos (raison), le pathos (emotion) et l'ethos (image de soi)."
  "|Le paratexte, titre, sous-titre et chapeau, annonce la problematique et oriente la lecture."
  "|La conclusion repond au probleme pose et peut ouvrir une question plus large sans ajouter d'idee nouvelle."
  "|En ST2S, l'argumentation sert aussi a justifier une prise en charge ou une decision de sante."),
[Q("Quel est l'objectif premier d'un texte argumentatif ?", "Convaincre ou persuader~Raconter une histoire~Decrire un paysage~Reciter un poeme", 0,
    "L'argumentation cherche a faire admettre une these par des raisons et des exemples."),
 Q("Comment appelle-t-on l'idee centrale defendue par un auteur ?", "Une antithèse~Une these~Une digression~Une didascalie", 1,
    "La these est la proposition que l'auteur soutient et cherche a faire partager."),
 Q("Quel plan enchaine these, antithese et synthese ?", "Le plan chronologique~Le plan dialectique~Le plan descriptif~Le plan comparatif", 1,
    "Le plan dialectique fait progresser le debat de la these a l'antithese, puis a la synthese."),
 Q("Un argument par l'autorite consiste a ...", "Citer une personne ou une institution reconnue~Raconter une anecdote~Employer une metaphore~Donner une statistique inventee", 0,
    "L'autorite s'appuie sur une source identifiable : un specialiste, une loi, un texte de reference."),
 Q("Quel connecteur marque une opposition ?", "Donc~Car~Mais~Ainsi", 2,
    "« Mais » (ou « or », « cependant », « bien que ») introduce une opposition ou une restriction."),
 Q("Que fait l'auteur quand il refute une objection ?", "Il l'ignore~Il la presente puis la discute~Il change de sujet~Il la copie", 1,
    "La refutation presente l'objection adverse avant d'en montrer les limites."),
 Q("Quel registre correspond a l'image que l'orateur donne de lui-meme ?", "Le pathos~Le logos~L'ethos~Le rythme", 2,
    "L'ethos designe la perception de la personne qui parle ; le logos est la raison, le pathos l'emotion."),
 T("Distinguer convaincre et persuader, puis illustrer la difference avec un message de prevention du tabac.",
    "Convaincre s'adresse a la raison : on propose des arguments verifies, par exemple les donnees sur les risques du tabac et les benefices de l'arret. Persuader s'adresse aussi a l'emotion et a la confiance : un temoignage de personne anciennement fumeuse, une image forte ou l'autorite d'un medecin rendent le message plus personnel. Un bon message de prevention combine les deux : des chiffres sources pour convaincre et un recit vecu pour persuader.",
    "La reponse doit opposer raison et emotion/sensibilite, puis donner un exemple precis en lien avec la sante."),
 T("Construire un plan dialectique bref sur la question : faut-il rendre la vaccination obligatoire ?",
    "These : l'obligation augmente la couverture vaccinale et protege les personnes fragiles qui ne peuvent pas etre vaccinees. Antithese : elle porte atteinte a la liberte individuelle et peut nourrir la defiance ; la responsabilite personnelle et l'information suffiraient. Synthese : une obligation ciblee, accompagnee d'information et de recommandations, concilie protection collective et respect des choix, avec des contre-indications medicales documentees.",
    "On attend trois parties distinctes, des arguments recevables de part et d'autre, puis une synthese qui depasse l'opposition.")],
C("Une argumentation est une chaine de raisons ou une these soit acceptable par le lecteur.",
  "These + arguments + refutation = demonstration",
  "Logos : raison · pathos : emotion · ethos : image de l'auteur · plan dialectique : these, antithese, synthese",
  "These~Idee defendue, discutable~Sujet de la these~Argument~Raison qui soutient~Pertinent et suffisant~Refutation~Reponse a une objection~Synthese plus nuancee",
  "Lire la question et degager la problematique|Formuler la these en une phrase|Choisir deux ou trois arguments solides|Anticiper une objection et la refuter|Conclure en repondant au probleme",
  "Confondre these et simple sujet|Accumuler les exemples sans les relier|Omettre la refutation|Conclure en introduisant une idee nouvelle",
  "These~La vaccination protege la collectivite~Antithese~L'obligation heurte la liberte~Refutation~Les contre-indications restent prises en compte~Synthese~Obligation ciblee et information",
  "Convaincre~S'adresser a la raison~Logos et preuves~Persuader~S'adresser a l'emotion~Pathos et ethos",
  "Argument logique~Decuction a partir de faits~Argument d'autorite~Citation d'une source reconnue"))

# ============================================================ FR2
add("ST2S-A-FR02", "Le recit et le recit autobiographique : temps et focalisation", "Français", ["1re"],
S("Le recit raconte une suite d'evenements ; il se distingue de la description et de l'argumentation."
  "|Un recit comporte un narrateur, des personnages, un cadre spatio-temporel et une intrigue."
  "|Le recit autobiographique est ecrit parquelqu'un qui raconte sa propre vie : narrateur et personnage coincident."
  "|Le pacte autobiographique engage la sincerite : les faits sont presentes comme v ecus par l'auteur."
  "|La focalisation interne adopte le point de vue d'un personnage ; la focalisation zero sait plus que les personnages."
  "|La focalisation externe se limite a ce qui est visible, sans acces aux pensees intimes."
  "|Le temps du recit alterne passe simple, imparfait, plus-que-parfait et present de narration."
  "|L'imparfait decrit le cadre et les habitudes ; le passe simple fait avancer les evenements."
  "|Le present de narration rend une scene plus vive, comme si elle se deroulait sous les yeux du lecteur."
  "|Les prolepses et les analepses sont des ruptures de chronologie : avance ou retour en arriere."
  "|Le discours rapporte peut etre direct, indirect libre ou indirect, et modifie la distance avec le personnage."
  "|L'etude du recit aide en ST2S a analyser un temoignage de patient ou un recit de soin."),
[Q("Qui raconte dans un recit autobiographique ?", "Un narrateur exterior~L'auteur lui-meme~Un personnage secondaire~Un journaliste", 1,
    "Le pacte autobiographique identifie l'auteur, le narrateur et le personnage principal."),
 Q("La focalisation interne correspond a ...", "Le savoir total du narrateur~Le point de vue d'un personnage~Une camera exterieure~Une absence de narrateur", 1,
    "Le narrateur interne adopte le regard et les connaissances d'un personnage."),
 Q("Quel temps fait principalement progresser l'action ?", "L'imparfait~Le plus-que-parfait~Le passe simple~Le futur simple", 2,
    "Le passe simple marque les evenements successifs ; l'imparfait installe le cadre."),
 Q("Qu'appelle-t-on une analepse ?", "Un retour en arriere~Un saut en avant~Une description~Une dialogue", 0,
    "Une analepse revient sur un evenement anterieur ; une prolepse anticipe la suite."),
 Q("Le discours indirect libre se caracterise par ...", "Des guillemets obligatoires~L'absence de guillemets avec un temps narratif~Un changement de locuteur~Une citation integrale", 1,
    "Le discours indirect libre fusionne les paroles du personnage dans la phrase du narrateur."),
 Q("Quel element n'appartient pas au cadre spatio-temporel ?", "L'epoque~Le lieu~La saison~L'opinion du lecteur", 3,
    "Le cadre situe l'action dans le temps et l'espace, independamment de la reception."),
 Q("Le present de narration produit un effet de ...", "Distanciation~Vivacite~Dubitation~Generalisation", 1,
    "Il rapproche le lecteur de la scene et donne une impression de direct."),
 T("Expliquer la difference entre focalisation interne et focalisation zero dans un recit de soin.",
    "En focalisation interne, le lecteur ne sait que ce que percoit le personnage, par exemple une infirmiere qui decrit ses observede la douleur du patient sans connaitre le diagnostic complet. En focalisation zero, le narrateur en sait davantage que les personnages : il peut decrire la douleur, le diagnostic et les pensees du patient simultanement, ce qui cree une ironie ou une compassion plus large. Le choix modifie l'empathie ressentie et le suspense.",
    "La reponse doit opposer le niveau d'information du narrateur et montrer l'effet de lecture."),
 T("Analyser l'usage des temps dans la phrase : « Il entra, la salle etait silencieuse, il s'assit. »",
    "« Ent » et « s'assit » sont au passe simple : ils marquent deux actions successives qui font avancer le recit. « Etait » est a l'imparfait : il decrit l'etat du lieu, le cadre dans lequel les actions se deroulent. Cette alternance entre temps de fond (imparfait) et temps d'evenement (passe simple) est caracteristique du recit classique : elle donne a la fois la scene et le mouvement.",
    "On attend l'identification des temps et la distinction entre description et progression narrative.")],
C("Le recit organise des evenements dans le temps ; le choix du narrateur et des temps produit un effet de sens.",
  "Imparfait (cadre) + passe simple (evenements) = recit",
  "Focalisation interne : un regard · zero : plus que les personnages · externe : seulement le visible",
  "Temps~Imparfait~Decrit le cadre~Passe simple~Avance l'action~Present de narration~Vivacite",
  "Repérer le narrateur et sa place|Situer l'action dans le temps et l'espace|Identifier la focalisation|Relever les temps dominants|Observer les ruptures de chronologie",
  "Confondre narrateur et auteur hors autobiographie|Lire tous les imparfaits comme des actions|Negliger les changements de focalisation|Oublier le pacte de sincerite",
  "Passe simple~Il entra, il s'assit~Imparfait~La salle etait silencieuse~Analepse~Retour sur l'enfance~Temoignage~Recit de patient",
  "Recit autobiographique~Auteur = narrateur = personnage~Recit de fiction~Narrateur distinct de l'auteur",
  "Focalisation interne~Un seul point de vue~Focalisation zero~Narrateur omniscient"))

# ============================================================ FR3
add("ST2S-A-FR03", "La poesie : vers, rythme et figures de style", "Français", ["1re", "Terminale"],
S("La poesie est un texte ou le sens se construit aussi par la forme : rythme, sonorites et images."
  "|Le vers est une unite de ligne ; la strophe regroupe plusieurs vers selon une disposition choisie."
  "|Le vers alexandrin compte douze syllables, le decasyllabe dix ; la cesure partage le vers en deux temps."
  "|La rime repete un son en fin de vers ; les rimes croisees, empilees ou embrassees creent des effets varies."
  "|Le rythme naît de la place des accents, des syllables et des silences, ainsi que de l'enjambement."
  "|L'enjambement prolonge une phrase d'un vers sur le suivant et accelere ou suspend la lecture."
  "|Les figures de style se repartissent en figures d'analogie : Metaphore, comparaison, allegorie, personnification."
  "|La metaphore dit une chose en termes d'une autre sans outil de comparaison ; la comparaison utilise « comme »."
  "|L'oxymore associe deux mots contradictoires ; l'antithese oppose deux termes ou deux idees."
  "|La repetition, l'anaphore et le parallélisme donnent au texte une musicalite et insistent sur un motif."
  "|Le registre lyrique exprime un sentiment personnel ; le registre satirique vise la critique."
  "|L'analyse d'un poemes'appuie toujours sur des elements precis du texte, jamais sur une vague impression."),
[Q("Combien de syllables compte un vers alexandrin ?", "8~10~12~14", 2,
    "L'alexandrin compte douze syllables, avec une cesure generalement a la sixieme."),
 Q("Quelle figure utilise le mot « comme » ?", "La metaphore~La comparaison~L'oxymore~L'hyperbole", 1,
    "La comparaison est explicite grace a un outil comme « comme », « tel », « semblable a »."),
 Q("Qu'appelle-t-on une cesure ?", "Une rime pauvre~Une coupure interne du vers~Un enjambement~Une strophe", 1,
    "La cesure separe le vers en deux mouvements, souvent apres la sixieme syllable de l'alexandrin."),
 Q("Quel procede repete un meme mot en debut de vers ?", "L'anaphore~L'antithese~La litote~La personnification", 0,
    "L'anaphore est une repetition en debut de vers ou de phrase."),
 Q("L'oxymore consiste a ...", "Exagerer~Associer deux termes contradictoires~Comparer avec comme~Repeter un son", 1,
    "« Douce violence » est un oxymore : deux mots opposes se rejoignent dans une meme expression."),
 Q("Quel est l'effet d'un enjambement ?", "Ralentir toujours~Prolonger la phrase d'un vers a l'autre~Supprimer la rime~Changer de registre", 1,
    "L'enjambement fait passer la phrase outre la fin du vers et modifie le rythme."),
 Q("Quel registre vise principalement la critique et le blâme ?", "Le registre lyrique~Le registre epique~Le registre satirique~Le registre tragique", 2,
    "La satire vise a critiquer un defaut, une institution ou un comportement."),
 T("Commenter la figure dans « Cette douceur cruelle » et preciser son effet.",
    "L'expression associe « douceur » et « cruelle », deux termes opposés : c'est un oxymore. Le contraste donne une impression ambiguë, a la fois attirante et blessante. En poesie, cette tension traduit un sentiment complexe, par exemple une tendresse melee de souffrance ou de regret. Le lecteur ne doit pas choisir un seul des deux sens : l'effet vient precisement de leur juxtaposition.",
    "On attend le nom de la figure, la definition et un effet de sens lie au texte."),
 T("Dire en quoi rime et rythme ne se confondent pas, avec un exemple de lecture a haute voix.",
    "La rime est une repetition de sons en fin de vers, donc un phenomene sonore localise a la frontiere des vers. Le rythme est plus global : il depend de la longueur des vers, de la place des accents, des cesures et des enjambements. A l'oral, on peut faire entendre une rime meme si le rythme est hesite, et inversement un vers sans rime peut etre tres rythme par ses accents. L'analyse doit donc noter séparément les deux dimensions.",
    "La reponse doit separer repetition finale et organisation des accents et des pauses.")],
C("En poesie, le sens passe par la forme : le vers, la rime et les figures creent une musique porteuse d'emotion.",
  "Vers = syllables + accents + rime",
  "Alexandrin : 12 syllables · cesure : coupure interne · enjambement : prolongement d'un vers a l'autre",
  "Vers~Unite de ligne~Alexandrin~Douze syllables~Cesure~Coupure interne~Rime~Repetition sonore finale",
  "Lire le poeme a haute voix|Compter les syllables et repérer la cesure|Relever les rimes et leur disposition|Identifier les figures de style|Relier les procedes au sentiment exprime",
  "Confondre rime et rythme|Compter les mots au lieu des syllables|Nommer une metaphore la ou il y a comparaison|Negliger l'enjambement",
  "Alexandrin~12 syllables~Douceur cruelle~Oxymore~Anaphore~Repetition initiale~Enjambement~Phrase prolongee",
  "Metaphore~Dit une chose pour une autre~Comparaison~Utilise comme ou tel",
  "Rime~Son en fin de vers~Rythme~Accents et pauses dans le vers"))

# ============================================================ FR4
add("ST2S-A-FR04", "Le theatre : dialogue, didascalies et registres", "Français", ["Terminale"],
S("La piece de theatre est un texte ecrit pour etre joue : le dialogue et les indications de scene comptent autant que les paroles."
  "|Le texte principal est compose de repliques distribuees entre les personnages."
  "|Les didascalies sont les indications ecrites par l'auteur : lieu, gestes, ton, deplacements,_decor."
  "|Une tirade est une longue replique ; un aparté est une parole destinee au seul public."
  "|La scene, l'acte et le tableau decoupent la piece en unites de plus en plus larges."
  "|Le dialogue theatre est souvent rapide, avec des coupes et des reprises qui creent le rythme."
  "|Les didascalies peuvent etre dites en incise ou placees entre parentheses avant une replique."
  "|Le registre comique vise le rire ; le registre tragique met en scene une fatalite et une succession malheureuse."
  "|Le theatre classique respecte les trois unitees de temps, de lieu et d'action."
  "|Le theatre du XXe siecle les conteste souvent : le decor change, le temps s'etire ou se fragmente."
  "|La mise en scene est une interpretation : elle ne se reduit pas a la lecture du texte."
  "|En ST2S, le theatre aide a travailler la prise de parole, l'ecoute et l'expression des emotions."),
[Q("Qu'appelle-t-on une didascalie ?", "Une replique~Une indication de mise en scene~Un personnage muet~Un acte entier", 1,
    "La didascalie precise le lieu, le geste, le ton ou le decor ; elle n'est pas dite par les personnages."),
 Q("Quel est un long discours d'un seul personnage ?", "Un aparté~Une tirade~Une scene~Une réplique courte", 1,
    "Une tirade est une replique longue ; l'aparté est destine au public seul."),
 Q("Quel registre cherche a provoquer le rire ?", "Le registre tragique~Le registre lyrique~Le registre comique~Le registre epique", 2,
    "Le registre comique utilise la caricature, la repetition, le quiproquo ou le burlesque."),
 Q("Les trois unitees du theatre classique sont ...", "Temps, lieu, action~Temps, rime, rythme~Lieu, personnage, objet~Action, décor, costume", 0,
    "La doctrine classique impose l'unite de temps, de lieu et d'action."),
 Q("Qui entend un aparté dans une piece ?", "Tous les personnages~Le seul public~Le metteur en scene uniquement~Personne", 1,
    "L'aparte est une confidence faite au public, que les autres personnages n'entendent pas."),
 Q("Quelle est la plus petite unite de la piece ?", "L'acte~La scene~Le tableau~Le rideau", 1,
    "La scene est l'unite de base ; plusieurs scenes forment un acte ou un tableau."),
 Q("La mise en scene correspond a ...", "La simple lecture du texte~Une interpretation visuelle et sonore~La copie du programme~L'impression du texte", 1,
    "Le metteur en scene choisit les gestes, les deplaces, les lumieres et les sons."),
 T("Expliquer la fonction des didascalies dans une scene ou un personnage entre en colere.",
    "Les didascalies indiquent d'abord le geste et le ton : « il frappe du poing », « d'une voix brevement sourde ». Elles orientent le jeu de l'acteur et permettent au lecteur d'imaginer la scene. Elles creent aussi un ecart entre ce qui est dit et ce qui est fait : un personnage peut parler calmement tout en accomplissant un geste violent. Dans une scene de colere, elles sont donc essentielles pour comprendre l'intensite emotionnelle que le dialogue seul n'exprime pas entierement.",
    "On attend le role pour l'acteur, pour le lecteur et la relation entre paroles et gestes."),
 T("Montrer en quoi une piece classique et une piece moderne different dans leur organisation.",
    "Une piece classique respecte les trois unitees : l'action se deroule en un lieu, en une journee environ, et suit une intrigue principale. Une piece moderne peut multiplier les lieux, fragmenter le temps, faire alterner scenes courtes et longues, et supprimer certains decors realistes. Cette liberte change la reception : le public doit reconstruire lui-meme le fil de l'action. Le passage d'une organisation a l'autre reflete une conception differente du theatre, moins centre sur la vraisemblance que sur l'expression.",
    "La reponse doit citer les unitees classiques et decrire une forme de rupture moderne.")],
C("Au theatre, le texte ne vit que par la representation : paroles, gestes et espace font un seul langage.",
  "Dialogue + didascalies = texte jouable",
  "Scene < acte < piece · aparté : pour le public · tirade : longue replique",
  "Replique~Parole d'un personnage~Didascalie~Indication de jeu~Tirade~Longue replique~Aparté~Confidence au public",
  "Repérer les personnages et les repliques|Lire les didascalies avant chaque entree|Identifier l'espace et le temps de la scene|Observer les rapports de force entre personnages|Proposer une interpretation de mise en scene",
  "Lire les didascalies comme des paroles|Oublier que le texte est destine a etre joue|Confondre aparté et tirade|Ignorer le registre dominant",
  "Colere~Geste et ton indiques~Quiproquo~Registre comique~Unite de lieu~Une seule salle~Theatre moderne~Lieux multiples",
  "Registre comique~Faire rire~Registre tragique~Fatalite et malheur",
  "Theatre classique~Trois unitees~Theatre moderne~Liberté de forme"))

# ============================================================ MA1
add("ST2S-A-MA01", "Fonctions, variations et extremums", "Maths", ["1re"],
S("Une fonction associe a chaque nombre x d'un ensemble de definition un unique nombre f(x)."
  "|Le graphique d'une fonction donne une lecture immediate des variations et des valeurs remarquables."
  "|Une fonction est croissante sur un intervalle si x1 < x2 entraine f(x1) inferieur ou egal a f(x2)."
  "|Une fonction est decroissante si l'ordre des images est inverse de celui des antécédents."
  "|La derivee f'(x) donne le taux de variation instantane et le coefficient directeur de la tangente."
  "|Si f'(x) est positive, la fonction croit ; si f'(x) est negative, la fonction decroit."
  "|Un extremum local se produit la ou la derivee s'annule en changeant de signe."
  "|La valeur absolue d'un taux de variation moyen se calcule par (f(b) - f(a)) / (b - a)."
  "|Une fonction affine ecrit f(x) = ax + b a un graphique en droite de pente a."
  "|Un polynome du second degre a un graphique en parabole, avec un sommet extremum."
  "|La resolusion d'une equation f(x) = k revient a lire les abscisses des points d'intersection avec la droite y = k."
  "|En ST2S, ces outils servent a modeliser des doses, des concentrations ou des courbes de croissance."),
[Q("Une fonction est croissante si ...", "f(x1) > f(x2) pour x1 < x2~f(x1) <= f(x2) pour x1 < x2~f est toujours positive~f est une droite", 1,
    "La croissance conserve l'ordre des antécédents sur l'intervalle considere."),
 Q("Que represente la derivee f'(x) ?", "Une aire~Le taux de variation instantane~La moyenne des valeurs~Un maximum", 1,
    "La derivee mesure la variation locale et donne la pente de la tangente."),
 Q("Si f'(x) < 0 sur un intervalle, alors la fonction est ...", "Croissante~Decroissante~Constante~Indeterminee", 1,
    "Une derivee negative traduit une decroissance locale."),
 Q("Un extremum local peut se produire la ou ...", "La fonction est nulle~La derivee s'annule en changeant de signe~La fonction est continue~Le graphique coupe l'axe des y", 1,
    "Le changement de signe de la derivee caractérise un extremum local.")
 ,Q("Quel est le graphique d'une fonction f(x) = ax + b ?", "Une parabole~Une droite~Une hyperbole~Un cercle", 1,
    "Une fonction affine a pour representation graphique une droite de coefficient directeur a."),
 Q("Comment lire les solutions de f(x) = k ?", "Aux intersections avec l'axe des x~Aux intersections avec la droite y = k~Au sommet de la courbe~A l'origine", 1,
    "On cherche les abscisses des points communs a la courbe et a la droite horizontale y = k."),
 Q("Que vaut le taux de variation moyen entre a et b ?", "f(b) - f(a)~f(a) + f(b)~(f(b) - f(a))/(b - a)~f'(a) + f'(b)", 2,
    "Le taux moyen est le rapport de l'accroissement des images a l'accroissement des antécédents."),
 T("Une concentration C(t) en mg/L est modelee par C(t) = t^2 - 6t + 12 pour t entre 0 et 5. Trouver le minimum et l'interpreter.",
    "On calcule la derivee C'(t) = 2t - 6, qui s'annule pour t = 3. La derivee est negative avant 3 et positive apres : la fonction décroit puis croit, donc t = 3 donne un minimum. C(3) = 9 - 18 + 12 = 3 mg/L. Aux bornes, C(0) = 12 et C(5) = 7, donc le minimum global sur [0;5] est bien 3 mg/L. La concentration est minimale a t = 3, apres quoi elle remonte.",
    "On attend le calcul de la derivee, le changement de signe et la valeur du minimum, avec une interpretation."),
 T("Expliquer pourquoi un taux de variation moyen n'est pas identique a la derivee en un point.",
    "Le taux de variation moyen entre deux instants mesure la variation globale sur un intervalle : c'est la pente de la secante. La derivee en un point mesure la variation locale : c'est la pente de la tangente en ce point. Sauf cas particulier d'une fonction affine, ces deux valeurs different. Sur une courbe de cinetique de medicament, le taux moyen donne l'evolution sur une periode, alors que la derivee donne la vitesse instantanee d'elimination a un instant precise.",
    "La reponse doit distinguer secante et tangente, global et local.")],
C("Etudier une fonction, c'est relier l'expression algebrique, le graphique et les variations.",
  "Taux moyen = (f(b) - f(a)) / (b - a) ; extremum : f'(x) = 0 avec changement de signe",
  "f' > 0 : croissance · f' < 0 : decroissance · f' = 0 : tangente horizontale",
  "Derivee~Variation instantanee~Taux moyen~Pente de la secante~Extremum~Changement de signe~Affine~Droite",
  "Determiner l'ensemble de definition|Calculer la derivee|Etudier le signe de la derivee|Dresser le tableau de variations|Lire les extremums et interpreter",
  "Oublier l'ensemble de definition|Confondre derivee et taux moyen|Conclure un extremum sans changement de signe|Mélanger abscisses et ordonnees",
  "C(t)~t^2 - 6t + 12~Derivee~2t - 6~Minimum~3 mg/L a t = 3~Secante~Taux sur un intervalle",
  "Fonction croissante~Images ordonnees comme les antécédents~Fonction decroissante~Images en ordre inverse",
  "Tangente~Pente locale~Secante~Pente moyenne"))

# ============================================================ MA2
add("ST2S-A-MA02", "Statistiques descriptives et probabilites", "Maths", ["1re", "Terminale"],
S("Une statistic descriptive resume un jeu de donnees par des indicateurs et des graphiques."
  "|La moyenne est la somme des valeurs divisee par l'effectif total."
  "|La mediane partage les donnees ordonnees en deux moities de meme effectif."
  "|L'ecart-type mesure la dispersion autour de la moyenne : plus il est grand, plus les valeurs sont etalees."
  "|Un histogramme represente des effectifs ou des frequences par classes ; un diagramme en boite resume les quartiles."
  "|Un echantillon representatif est choisi au hasard et suffisamment grand pour estimer une population."
  "|Une experience aleatoire se decrit par un ensemble universel d'issues ; la probabilite d'un evenement est comprise entre 0 et 1 et la somme des probabilites des issues exclusives vaut 1."
  "|Deux evenements independants verificent P(A inter B) = P(A) × P(B)."
  "|La probabilite conditionnelle P(A sachant B) s'ecrit P(A inter B) / P(B) lorsque B est non nul."
  "|Un arbre pondere permet de representer des experiences en plusieurs etapes et de calculer des probabilites composees."
  "|La loi binomiale modele le nombre de succes parmi n essais independants de meme probabilite p."
  "|En sante, ces outils servent a interpreter un dépistage, un taux de couverture ou un essai clinique."),
[Q("Quel indicateur est sensible aux valeurs extremes ?", "La mediane~La moyenne~Le mode~Les quartiles", 1,
    "La moyenne prend en compte toutes les valeurs, donc aussi les extremes ; la mediane est plus robuste."),
 Q("Que mesure l'ecart-type ?", "Le centre de la distribution~La dispersion autour de la moyenne~Le nombre de donnees~La frequence maximale", 1,
    "L'ecart-type quantifie l'etalement des valeurs autour de la moyenne."),
 Q("La probabilite d'un evenement est toujours ...", "Superieure a 1~Comprise entre 0 et 1~Negative~Egale a la moyenne", 1,
    "Une probabilite appartient a l'intervalle [0 ; 1]."),
 Q("Quelle est la condition d'independance de A et B ?", "P(A inter B) = P(A) + P(B)~P(A inter B) = P(A) × P(B)~P(A) = P(B)~A et B sont simultanes", 1,
    "L'independance se caracterise par la multiplicite des probabilites."),
 Q("Comment calculer P(A sachant B) ?", "P(A) / P(B)~P(A inter B) / P(B)~P(A) × P(B)~P(B) - P(A)", 1,
    "On divise la probabilite de l'intersection par celle de l'evenement conditionnant."),
 Q("Que modele une loi binomiale ?", "Une duree continue~Un nombre de succes sur n essais independants~Une moyenne d'echantillon~Une correlation", 1,
    "La loi binomiale compte les succes dans n essais de meme probabilite p."),
 Q("Quel graphique represente des frequences par classes ?", "Le diagramme en barres~L'histogramme~Le camembert~Le nuage de points", 1,
    "L'histogramme represente des effectifs ou frequences de classes continues."),
 T("Dans un groupe de 200 patients, 30 sont porteurs d'un marqueur. Calculer la frequence et expliquer sa portee.",
    "La frequence est 30/200 = 0,15, soit 15 %. Elle decrit la proportion observee dans le groupe etudie, pas une probabilite universelle. Pour l'etendre a une population plus large, il faut que l'echantillon soit representatif, notamment tire au hasard et de taille suffisante. On peut alors donner un intervalle de confiance plutôt qu'une valeur exacte. La frequence brute ne dit rien sur la cause du marqueur ni sur son caractere predictif.",
    "On attend le calcul, la distinction entre descriptif et inferentiel et la condition de representativite."),
 T("Un test a une sensibilite de 90 % et une specificite de 95 %. Expliquer pourquoi une prediction positive n'est pas une certitude.",
    "La sensibilite est la probabilite d'un test positif chez une personne malade ; la specificite est la probabilite d'un test negatif chez une personne non malade. Une prediction positive depend aussi de la prevalence de la maladie : si la maladie est rare, le nombre de faux positifs peut depasser le nombre de vrais positifs. La probabilite d'etre malade sachant que le test est positif, ou valeur predictive positive, se calcule par Bayes et reste inferieure a 100 %.",
    "La reponse doit distinguer sensibilite, specificite et valeur predictive positive, et mentionner la prevalence.")],
C("Les statistiques decrivent et les probabilites quantifient l'incertitude : deux outils complementaires en sante publique.",
  "Moyenne = somme / effectif ; P(A sachant B) = P(A inter B) / P(B)",
  "Ecart-type : dispersion · mediane : robuste aux extremes · independance : P(A inter B) = P(A)P(B)",
  "Moyenne~Valeur centrale~Mediane~Partage en deux moities~Ecart-type~Dispersion~Echantillon~Sous-ensemble representatif",
  "Ordounner les donnees|Choisir l'indicateur adapte|Construire le graphique|Verifier la representativite|Calculer la probabilite par arbre ou par formule",
  "Confondre moyenne et mediane|Oublier de trier avant de lire la mediane|Croire qu'un echantillon petit est representative|Mélanger sensibilite et valeur predictive",
  "200 patients~Effectif de l'echantillon~15%~Frequence du marqueur~90%~Sensibilite du test~95%~Specificite du test",
  "Statistique descriptive~Resumer des donnees~Statistique inferentielle~Estimer une population",
  "Evenements independants~P(A inter B) = P(A)P(B)~Evenements exclusifs~P(A union B) = P(A) + P(B)"))

# ============================================================ MA3
add("ST2S-A-MA03", "Suites numeriques et interets composes", "Maths", ["1re", "Terminale"],
S("Une suite est une famille de nombres indexes par les entiers naturels."
  "|Une suite arithmetique a un ecart constant r : u(n+1) = u(n) + r."
  "|Une suite geometrique a un rapport constant q : u(n+1) = q × u(n)."
  "|Le terme general d'une suite arithmetique est u(n) = u(0) + n×r."
  "|Le terme general d'une suite geometrique est u(n) = u(0) × q^n."
  "|La somme des termes d'une suite geometrique s'ecrit u(0) × (1 - q^(n+1)) / (1 - q) si q different de 1."
  "|Une croissance exponentielle se reconnait a un taux de variation proportionnel a la valeur courante."
  "|Un capital place a taux t annuel avec interets composes devient C(n) = C(0) × (1 + t)^n."
  "|Un depreciation, par exemple la perte de valeur d'un appareil, suit une geometrique de rapport inferieur a 1."
  "|Le logarithme permet de resoudre une equation ou l'inconnue est un exposant."
  "|Un taux annuel effectif tient compte de la capitalisation des interets."
  "|En ST2S, ces suites servent a modeliser une evolutive de population, de stock ou de concentration."),
[Q("Dans une suite arithmetique, que reste constant ?", "Le rapport~L'ecart entre deux termes consecutifs~Le produit~Le cube", 1,
    "La raison r est la difference u(n+1) - u(n), constante."),
 Q("Dans une suite geometrique de rapport q, que vaut u(n+1) ?", "u(n) + q~q × u(n)~u(n) - q~u(n)^q", 1,
    "Chaque terme est obtenu en multipliant le precedent par le rapport q."),
 Q("Quel est le terme general d'une geometrique de premier terme u(0) et de rapport q ?", "u(0) + n×q~u(0) × q^n~q × n~u(0)^n", 1,
    "On multiplie u(0) par q autant de fois que l'indice n."),
 Q("Un capital de 1000 euros a 5 % pendant 2 ans avec interets composes vaut ...", "1050~1100~1102,5~1005", 2,
    "1000 × 1,05^2 = 1102,50 euros, car les interets de la premiere annee rapportent aussi des interets."),
 Q("Quand une grandeur diminue de 10 % par an, le rapport de la suite est ...", "1,10~0,90~-0,10~10", 1,
    "Une baisse de 10 % revient a multiplier par 1 - 0,10 = 0,90."),
 Q("Quel outil resout une equation ou l'inconnue est un exposant ?", "La racine carree~Le logarithme~La mediane~La derivee seconde", 1,
    "Le logarithme transforme une puissance en produit et permet d'isoler l'exposant."),
 Q("Une croissance exponentielle se caracterise par ...", "Un accroissement constant~Un taux de variation proportionnel a la valeur~Une valeur toujours negative~Une periode fixe", 1,
    "Plus la valeur est grande, plus l'accroissement est rapide : c'est l'exponentielle."),
 T("Une population de bacteries double toutes les 3 heures. Partant de 500, calculer l'effectif apres 12 heures.",
    "Le rapport est 2 toutes les 3 heures, donc 4 periodes en 12 heures. L'effectif vaut 500 × 2^4 = 500 × 16 = 8000 bacteries. La suite est geometrique de rapport 2 par periode de 3 heures. Si l'on avait utilise un modele lineaire, on aurait ajoute 500 a chaque periode, ce qui donne 2500 et underestimate fortement la croissance reelle. Ce type de calcul aide a comprendre l'importance de la precocite d'un traitement antibiotique.",
    "On attend l'identification du rapport, le nombre de periodes et le calcul."),
 T("Comparer interets simples et interets composes sur 1000 euros a 4 % pendant 3 ans.",
    "Aux interets simples, on ajoute chaque annee 4 % du capital initial, soit 40 euros : apres 3 ans, 1000 + 3 × 40 = 1120 euros. Aux interets composes, on multiplie par 1,04 chaque annee : 1000 × 1,04^3, soit environ 1124,86 euros. La difference, environ 4,86 euros, vient de ce que les interets de la premiere et de la deuxieme annee produisent eux aussi des interets. Sur de longues durees, l'ecart devient considerable.",
    "On attend les deux calculs et l'explication de la capitalisation.")],
C("Les suites modelisent une evolution repetee : addition constante ou multiplication constante.",
  "Arithmetique : u(n) = u(0) + nr ; geometrique : u(n) = u(0) q^n",
  "Interets composes : C(n) = C(0)(1 + t)^n ; baisse de 10 % : rapport 0,9",
  "Suite arithmetique~Ecart constant r~Suite geometrique~Rapport constant q~Interets composes~Capital × (1+t)^n~Logarithme~Inverse de la puissance",
  "Identifier le type de suite|Determiner la raison ou le rapport|Ecrire le terme general|Calculer le terme demande|Interpreter le resultat dans le contexte",
  "Confondre raison et rapport|Appliquer des interets simples a la place des composes|Oublier de convertir le pourcentage|Ne pasajuster le nombre de periodes",
  "500 bacteries~Depart~Doublement~Rapport 2~12 heures~4 periodes~8000~Effectif final",
  "Suite arithmetique~Croissance lineaire~Suite geometrique~Croissance exponentielle",
  "Interets simples~Interets calcules sur le capital initial~Interets composes~Interets calcules sur le capital updated"))

# ============================================================ PC1
add("ST2S-A-PC01", "Energie, travail et rendement", "Physique-Chimie", ["1re"],
S("L'energie est une grandeur qui se conserve et se transforme, mais ne se cree ni ne se detruit."
  "|Le travail d'une force constante vaut W = F × d × cos(alpha), avec F en newtons et d en metres."
  "|L'energie cinetique d'un corps de masse m et de vitesse v vaut Ec = 1/2 × m × v^2."
  "|L'energie potentielle de pesanteur vaut Ep = m × g × h, avec g approximativement 9,8 N/kg."
  "|La puissance est le rapport du travail ou de l'energie transmise a la duree : P = W / t."
  "|L'unité de puissance est le watt ; une kWh vaut 3,6 millions de joules."
  "|Le rendement d'un appareil est le rapport entre energie utile et energie fournie."
  "|Un rendement est toujours inferieur ou egal a 1 : une partie de l'energie est dissipee, souvent en chaleur."
  "|Les pertes par frottements se retrouvent dans de nombreux systemes, y compris les machines medicales."
  "|Un bilan d'energie liste les energies d'entree, utiles et perdues, et verifie la conservation."
  "|Le corps humain convertit l'energie chimique des aliments en travail mecanique et en chaleur."
  "|Le metabolisme de base represente l'energie minimale necessaire au repos, en joules ou en calories."),
[Q("Quelle est l'unite SI de l'energie ?", "Le watt~Le joule~Le newton~Le pascal", 1,
    "Le joule est l'unite d'energie, de travail et de chaleur ; le watt est une puissance."),
 Q("Comment calculer le travail d'une force constante ?", "W = F / d~W = F × d × cos(alpha)~W = m × v^2~W = P × t", 1,
    "Le travail est le produit de la force, du deplacement et du cosinus de l'angle entre eux."),
 Q("Quelle formule donne l'energie cinetique ?", "m × g × h~1/2 × m × v^2~F × d~m × v", 1,
    "L'energie cinetique croit comme le carre de la vitesse."),
 Q("La puissance correspond a ...", "Une quantite d'energie totale~Un energy par unite de temps~Une force par unite de surface~Une temperature", 1,
    "P = W/t : la puissance mesure le debit d'energie."),
 Q("Une kWh correspond a ...", "1000 J~3600 J~3,6 × 10^6 J~1 W/s", 2,
    "1 kWh = 1000 W × 3600 s = 3,6 millions de joules."),
 Q("Le rendement d'un appareil vaut ...", "Energie utile / energie fournie~Energie fournie / energie utile~Puissance × temps~Force × deplacement", 0,
    "Le rendement compare ce que l'appareil produit d'utile a ce qu'il consomme."),
 Q("Que devient l'energie non utilisee par une machine ?", "Elle disparait~Elle est dissipee, souvent en chaleur~Elle se transforme en masse~Elle est stockee dans le vide", 1,
    "Le principe de conservation implique que l'energie perdue est transferée sous une autre forme."),
 T("Un appareil consomme 2000 J et fournit 1500 J de travail utile. Calculer son rendement et commenter.",
    "Le rendement vaut 1500/2000 = 0,75, soit 75 %. Les 500 J restants, soit 25 %, sont dissipes, principalement sous forme de chaleur et de bruit. Ce rendement est inferieur a 1, ce qui est conforme au principe de conservation de l'energie. Pour ameliorer le dispositif, on chercherait a reduire les frottements ou a recuperer une partie de la chaleur perdue.",
    "On attend le calcul du rapport, l'identification des pertes et le rappel du principe de conservation."),
 T("Expliquer pourquoi doubler la vitesse d'un vehicule multiplie par quatre son energie cinetique.",
    "L'energie cinetique est proportionnelle au carre de la vitesse : Ec = 1/2 m v^2. Si la vitesse passe de v a 2v, l'energie devient 1/2 m (2v)^2 = 4 × 1/2 m v^2. L'energie est donc multipliee par quatre, et non par deux. Cela explique l'allongement considerable de la distance de freinage et la gravite des accidents : les energies a dissiper par les freins, les ceintures et les structures augmentent tres vite avec la vitesse.",
    "La reponse doit citer la relation quadratic et en tirer une consequence concrete de securite.")],
C("L'energie ne se perd pas : elle change de forme, et le rendement mesure la part reellement utile.",
  "W = F d cos(a) · Ec = 1/2 m v^2 · P = W/t · rendement = utile / fourni",
  "J : energie · W : puissance · kWh : energie electrique (3,6 × 10^6 J)",
  "Travail~F × d × cos~Energie cinetique~1/2 m v^2~Puissance~W/t~Rendement~Utile sur fourni",
  "Identifier les energies mises en jeu|Choisir la formule adaptee|Convertir les unites|Calculer le travail ou la puissance|Etablir le bilan et le rendement",
  "Confondre energie et puissance|Oublier le cosinus dans le travail|Utiliser v au lieu de v^2|Croire qu'un rendement peut depasser 1",
  "2000 J~Energie consommee~1500 J~Travail utile~75%~Rendement~500 J~Chaleur dissipe",
  "Energie~Capacite de produire un travail~Puissance~Energie par unite de temps",
  "Rendement eleve~Peu de pertes~Rendement faible~Beaucoup de chaleur perdue"))

# ============================================================ PC2
add("ST2S-A-PC02", "Electricite : lois, circuits et securite", "Physique-Chimie", ["1re"],
S("Un circuit electrique est un ensemble d'elements relies permettant le passage d'un courant."
  "|L'intensite du courant se mesure en ampères avec un ampèremetre place en serie."
  "|La tension electrique se mesure en volts avec un voltmetre place en derivation aux bornes du composant."
  "|La loi d'Ohm s'ecrit U = R × I pour un conducteur ohmique a temperature constante."
  "|La resistance R se mesure en ohms et depend de la nature, de la longueur et de la section du fil."
  "|En serie, l'intensite est la meme dans tous les elements et les tensions s'additionnent."
  "|En derination, la tension est la meme aux bornes de chaque branche et les intensites s'additionnent."
  "|La puissance electrique consommee vaut P = U × I ; l'energie consommee vaut E = P × t."
  "|Une masse ou un boitier conducteur doit etre relie a la terre pour eviter les tensions dangereuses."
  "|Les disjoncteurs et les fusibles interrompent le circuit en cas de surintensite."
  "|Un courant traversant le corps humain est d'autant plus dangereux qu'il est intense et passe pres du coeur."
  "|La securite electrique en milieu de soin implique des equipements homologues, verifies et seches."),
[Q("Comment brancher un ampèremetre ?", "En derivation~En serie~Aux bornes de la terre~N'importe comment", 1,
    "L'ampèremetre se place en serie pour mesurer le courant qui traverse la branche."),
 Q("Quelle est la formule de la loi d'Ohm ?", "U = R / I~U = R × I~U = I / R~U = P × R", 1,
    "Pour un conducteur ohmique, la tension est proportionnelle a l'intensite."),
 Q("Dans un circuit en serie, que reste constant ?", "La tension~L'intensite~La resistance totale~La puissance", 1,
    "En serie, le meme courant traverse tous les composants."),
 Q("Que mesure un voltmetre ?", "L'intensite~La tension entre deux points~La resistance~La puissance", 1,
    "Le voltmetre se branche en derivation aux bornes du composant."),
 Q("Quel appareil coupe le circuit en cas de surintensite ?", "Le voltmetre~Le disjoncteur~La terre~Le generateur", 1,
    "Le disjoncteur ou le fusible protege les installations contre les surcharges et les courts-circuits."),
 Q("Quelle unite mesure une resistance ?", "L'ampere~Le volt~L'ohm~Le watt", 2,
    "La resistance s'exprime en ohms, symbole omega."),
 Q("Quel est le facteur de risque majeur d'un courant electrique pour le corps ?", "Sa couleur~Son passage pres du coeur~Sa frequence nulle~Le nombre de fils", 1,
    "Un courant traversant la poitrine peut perturber l'activite cardiaque."),
 T("Un appareil de 230 V consomme 2 A. Calculer sa puissance et l'energie en une heure.",
    "La puissance est P = U × I = 230 × 2 = 460 W. En une heure, l'energie consommee vaut E = P × t = 460 W × 1 h = 460 Wh, soit 0,46 kWh. En joules, cela fait 460 × 3600 = 1 656 000 J. Cette valeur permet d'estimer le cout de fonctionnement et la charge de l'installation electrique du local.",
    "On attend le calcul de la puissance puis la conversion en kWh ou en joules."),
 T("Expliquer le role de la terre et du disjoncteur dans la securite d'une installation.",
    "La terre offre un chemin de faible resistance aux courants de defaut : si un conducteur touche un boitier metallique, le courant s'ecoule vers la terre plutot que vers une personne qui toucherait l'appareil. Le disjoncteur, lui, detecte une surintensite et coupe automatiquement l'alimentation. Les deux dispositifs sont complementaires : la terre limite la tension dangereuse, le disjoncteur supprime l'alimentation en cas de defaut. Dans un etablissement de sante, ces protections sont verifiees regulierement.",
    "La reponse doit separer le role de la terre et celui du disjoncteur, puis montrer leur complementarite.")],
C("Le courant circule dans un circuit ferme ; tensions, intensites et resistances sont liees par la loi d'Ohm.",
  "U = R I · P = U I · E = P t",
  "Serie : meme I, tensions additionnees · derivation : meme U, intensites additionnees",
  "Intensite~Ampere, en serie~Tension~Volt, en derivation~Resistance~Ohm, U = RI~Disjoncteur~Coupe sur surintensite",
  "Repérer le type de branchement|Placer les appareils de mesure|Appliquer la loi d'Ohm|Calculer puissance et energie|Verifier les protections electriques",
  "Brancher l'ampèremetre en derivation|Oublier de couper le courant avant une intervention|Confondre watt et wattheure|Negliger la mise a la terre",
  "230 V~Tension du reseau~2 A~Intensite consommee~460 W~Puissance~0,46 kWh~Energie en une heure",
  "Circuit en serie~Meme intensite~Circuit en derivation~Meme tension",
  "Fusible~Fil qui fond en surintensite~Disjoncteur~Dispositif rearmeable"))

# ============================================================ PC3
add("ST2S-A-PC03", "Solutions aqueuses, concentration et pH", "Physique-Chimie", ["1re", "Terminale"],
S("Une solution est un melange homogene d'un soluté dans un solvant, generalement l'eau."
  "|La concentration molaire c exprime le nombre de moles de soluté par litre de solution."
  "|Une mole contient environ 6,02 × 10^23 entites : c'est le nombre d'Avogadro."
  "|La masse molaire M permet de passer de la masse au nombre de moles : n = m / M."
  "|Une dilution respecte la relation c1 × V1 = c2 × V2, avec les volumes dans la meme unite."
  "|Le pH mesure l'acidite d'une solution : pH = -log[H3O+], ou [H3O+] est en mol/L."
  "|Une solution acide a un pH inferieur a 7, neutre un pH egal a 7, basique un pH superieur a 7."
  "|L'echelle de pH est logarithmique : une diminution d'une unite multiplie [H3O+] par dix."
  "|Une solution tampon resiste aux changements de pH : le sang en est un exemple essentiel."
  "|Le pH sanguin se maintient autour de 7,4 ; en dehors d'une plage etroite, des troubles graves apparaissent."
  "|Les ions H3O+ et OH- sont lies dans l'eau par le produit ionique : [H3O+] × [OH-] = 10^-14 a 25 degres."
  "|La titration acide-base permet de doser une substance par neutralisation avec une solution connue."),
[Q("Quelle est l'unite de la concentration molaire ?", "Le gramme~La mole par litre~Le litre par mole~Le joule", 1,
    "La concentration molaire s'exprime en mol/L."),
 Q("Quel est le nombre d'Avogadro ?", "6,02 × 10^23~3,14~9,8~1,6 × 10^-19", 0,
    "Une mole contient environ 6,02 × 10^23 entites elementaires."),
 Q("Comment calculer le nombre de moles a partir de la masse ?", "n = m × M~n = m / M~n = M / m~n = m + M", 1,
    "On divise la masse par la masse molaire exprimee en g/mol."),
 Q("Une solution a un pH de 3. Quelle est sa nature ?", "Neutre~Acide~Basique~Tampon", 1,
    "Un pH inferieur a 7 caracterise une solution acide."),
 Q("Que signifie une echelle logarithmique pour le pH ?", "Un pH de 4 est deux fois plus acide qu'un pH de 5~Un pH de 4 est dix fois plus acide qu'un pH de 5~Les pH ne peuvent pas etre decimaux~Le pH ne depend pas de la concentration", 1,
    "Chaque unite de pH correspond a un facteur 10 sur la concentration en ions H3O+."),
 Q("Quelle relation décrit une dilution ?", "c1 V1 = c2 V2~c1 / V1 = c2 / V2~c1 + V1 = c2 + V2~c1 = V2", 0,
    "La quantite de soluté reste la meme avant et apres dilution."),
 Q("Quel systeme maintient le pH du sang autour de 7,4 ?", "Un systeme tampon~Un acide fort~Une dilution~Un disjoncteur", 0,
    "Les systemes tampons, notamment le couple bicarbonate/acide carbonique, stabilisent le pH sanguin."),
 T("Une solution d'acide a un pH de 2. Calculer sa concentration en ions H3O+ et comparer avec un pH de 4.",
    "Comme pH = -log[H3O+], on a [H3O+] = 10^-pH. Pour pH = 2, [H3O+] = 10^-2 = 0,01 mol/L. Pour pH = 4, [H3O+] = 10^-4 = 0,0001 mol/L. La solution de pH 2 est donc cent fois plus concentree en ions H3O+ que celle de pH 4 : deux unites de pH representent un facteur 10 × 10 = 100. Cela montre qu'un faible changement de pH peut traduire une forte variation d'acidite.",
    "On attend le calcul par puissance de 10 et la comparaison en facteur 100."),
 T("Expliquer pourquoi une solution tampon est indispensable au fonctionnement de l'organisme.",
    "Une solution tampon contient un acide faible et sa base conjuguee, capables de consommer les ions H3O+ ajoutes ou d'en liberer si des ions OH- arrivent. Elle limite ainsi les variations de pH malgré les acides produits par le metabolisme, comme l'acide lactique ou le dioxyde de carbone. Le sang maintient un pH proche de 7,4 : les enzymes et les proteines ne fonctionnent correctement que dans cette plage etroite. Une acidose ou une alcalose perturbent rapidement les fonctions vitales.",
    "La reponse doit expliquer le mecanisme et relier le pH au bon fonctionnement des proteines.")],
C("Le pH quantifie l'acidite d'une solution ; en biologie, sa stabilite est une condition de vie.",
  "pH = -log[H3O+] ; c = n/V ; dilution : c1 V1 = c2 V2",
  "pH < 7 : acide · pH = 7 : neutre · pH > 7 : basique · une unite de pH = facteur 10",
  "Concentration~Moles par litre~Ph~Logarithme de H3O~Dilution~c1 V1 = c2 V2~Tampon~Resistance au changement",
  "Convertir la masse en moles|Calculer la concentration|Utiliser la relation de dilution|Deduire la concentration en ions du pH|Verifier la plage de pH physiologique",
  "Oublier de convertir le volume en litres|Confondre pH et concentration en masse|Croire que le pH est lineaire|Negliger les unites dans une dilution",
  "pH 2~0,01 mol/L de H3O~pH 4~0,0001 mol/L~Facteur 100~Difference de deux unites~Sang~pH proche de 7,4",
  "Solution acide~pH inferieur a 7~Solution basique~pH superieur a 7",
  "Solution tampon~Amortit les variations~Solution non tamponnee~pH varie vite"))

# ============================================================ SV1
add("ST2S-A-SV01", "La cellule animale : membrane, organites et metabolisme", "SVT", ["1re"],
S("La cellule est l'unite structurale et fonctionnelle des etres vivants."
  "|La membrane plasmique est une bicouche de lipides qui delimite la cellule et controles les echanges."
  "|Le noyau contient l'ADN organise en chromosomes ; il dirige la synthese des proteines."
  "|Les mitochondries sont le siege de la respiration cellulaire et produisent l'energie sous forme d'ATP."
  "|Les ribosomes synthetisent les proteines a partir de l'information genetique."
  "|Le reticule endoplasmic et l'appareil de Golgi transportent, modifient et trient les proteines."
  "|Les lysosomes digerent les debris cellulaires grace a des enzymes."
  "|La respiration cellulaire consume du glucose et du dioxygene et produit du dioxyde de carbone, de l'eau et de l'ATP."
  "|La fermentation est une voie de production d'ATP sans dioxygene, comme dans le muscle en effort intense."
  "|Les cellules specialisees, nerveuses, musculaires ou epitheliales, ont une forme adaptee a leur fonction."
  "|L'homeostasie designe le maintien d'un milieu interne stable malgre les variations externes."
  "|La membrane des globules rouges porte les antigenes des groupes sanguins, essentiels en transfusion."),
[Q("Quel organite produit l'ATP par respiration cellulaire ?", "Le noyau~La mitochondrie~Le ribosome~Le lysosome", 1,
    "Les mitochondries sont le siege de la respiration cellulaire aerobie."),
 Q("Quel est le role principal de la membrane plasmique ?", "Stocker l'ADN~Controler les echanges avec le milieu~Produire des enzymes digestives~Synthetiser des lipides", 1,
    "La membrane est une barriere selective qui regule les entrees et les sorties."),
 Q("Ou se trouve l'information genetique dans une cellule animale ?", "Dans le cytoplasme~Dans le noyau~Dans la mitochondrie~Dans le lysosome", 1,
    "L'ADN est porte par les chromosomes du noyau."),
 Q("Quels elements sont consommes par la respiration cellulaire ?", "ATP et eau~Glucose et dioxygene~Dioxyde de carbone et eau~Proteines et lipides", 1,
    "La respiration aerobie oxyde le glucose grace au dioxygene."),
 Q("Qu'appelle-t-on une cellule specialisee ?", "Une cellule qui ne respire pas~Une cellule adaptee a une fonction precise~Une cellule sans noyau~Une cellule en division", 1,
    "La specialisation cellulaire se traduit par une structure et une fonction propres."),
 Q("Que designe l'homeostasie ?", "Le renouvellement des cellules~Le maintien d'un milieu interne stable~La mort cellulaire programmee~La division du noyau", 1,
    "L'homeostasie est la regulation des parametres internes comme la temperature ou le pH."),
 Q("Quel element de la membrane est implique dans les groupes sanguins ?", "Un antigene~Un ribosome~Un chromosome~Un enzyme lysosomal", 0,
    "Les antigenes portes par la membrane des globules rouges determinent le groupe sanguin."),
 T("Expliquer pourquoi une cellule musculaire contient de nombreuses mitochondries.",
    "La contraction musculaire consomme beaucoup d'energie sous forme d'ATP. Les mitochondries etant le siege de la respiration cellulaire, une cellule qui a besoin de beaucoup d'ATP en contient davantage. C'est une adaptation de la structure a la fonction : plus l'activite energetique est intense, plus la densite mitochondriale est elevee. A l'inverse, une cellule peu active en contient moins. On retrouve le meme raisonnement pour les cellules du coeur, particulierement riches en mitochondries.",
    "On attend le lien entre besoins energetiques, ATP et nombre de mitochondries."),
 T("Distinguer respiration cellulaire et fermentation et preciser quand cette derniere intervient.",
    "La respiration cellulaire est aerobie : elle utilise le dioxygene pour oxyder complettement le glucose et produit environ 38 ATP par mole de glucose. La fermentation est anaerobie : sans dioxygene, elle ne degrade que partiellement le glucose et ne produit que 2 ATP, avec formation d'acide lactique dans le muscle ou d'ethanol chez la levure. Dans un muscle en effort intense, l'apport en dioxygene devient insuffisant : la fermentation prend le relais, ce qui explique l'accumulation d'acide lactique et la fatigue.",
    "La reponse doit opposer presence de dioxygene, rendement energetique et situation d'hypoxie.")],
C("La cellule est un systeme ouvert qui echange avec son milieu et transforme des nutriments en energie.",
  "Glucose + O2 -> CO2 + H2O + ATP",
  "Mitochondrie : ATP · noyau : ADN · membrane : echanges selectifs",
  "Membrane~Bicouche lipidique~Noyau~ADN et chromosomes~Mitochondrie~Respiration et ATP~Ribosome~Synthese proteique",
  "Observer la cellule au microscope|Identifier les organites|Relier chaque organite a sa fonction|Ecrire le bilan de la respiration|Expliquer une adaptation cellulaire",
  "Confondre noyau et mitochondrie|Oublier que la fermentation est anaerobie|Croire que l'ATP est une proteine|Negliger le role de la membrane",
  "Muscle~Riche en mitochondries~Glucose~Combustible cellulaire~O2~Accepteur final~Acide lactique~Fermentation anaerobic",
  "Respiration aerobie~Avec dioxygene, beaucoup d'ATP~Fermentation~Sans dioxygene, peu d'ATP",
  "Cellule animale~Pas de paroi ni de chloroplaste~Cellule vegetale~Paroi et chloroplastes"))

# ============================================================ SV2
add("ST2S-A-SV02", "ADN, genes et transmission hereditaire", "SVT", ["1re", "Terminale"],
S("L'ADN est la molecule qui porte l'information genetique des etres vivants."
  "|Il est forme de deux brins en double helice, constitues de nucleotides."
  "|Chaque nucleotide contient un sucre, un groupe phosphate et une base azotee."
  "|Les bases sont l'adénine, la thymine, la cytosine et la guanine, avec des appariements fixes."
  "|L'adénine s'apparie avec la thymine, la cytosine avec la guanine."
  "|Un gene est un segment d'ADN qui porte l'information pour synthetiser une proteine."
  "|La synthese des proteines suit la transcription de l'ADN en ARN messager puis la traduction par les ribosomes."
  "|Un chromosome est une molecule d'ADN condensee, associee a des proteines."
  "|L'espece humaine possede 46 chromosomes dans les cellules somatiques, soit 23 paires."
  "|La meiose produit des cellules reproductrices a 23 chromosomes, les gametes."
  "|La fecondation restaure le nombre de 46 chromosomes chez l'embryon."
  "|Une mutation est une modification de la sequence d'ADN, transmise ou non selon la cellule concernee."),
[Q("Combien de chromosomes contient une cellule humaine somatique ?", "23~46~22~92", 1,
    "Les cellules somatiques possedent 23 paires, soit 46 chromosomes."),
 Q("Quel appariement de bases est correct dans l'ADN ?", "Adenine-cytosine~Adenine-thymine~Guanine-thymine~Cytosine-adenine", 1,
    "L'adénine s'apparie avec la thymine et la cytosine avec la guanine."),
 Q("Qu'est-ce qu'un gene ?", "Une cellule specialisee~Un segment d'ADN codant une proteine~Un organite~Une base azotee", 1,
    "Le gene est l'unite d'information genetique."),
 Q("Quel processus produit les gametes ?", "La mitose~La meiose~La fecondation~La transcription", 1,
    "La meiose reduit le nombre de chromosomes de moitie."),
 Q("Combien de chromosomes porte un gamet humain ?", "46~23~22~92", 1,
    "Chaque gamet contient un seul chromosome de chaque paire, soit 23 chromosomes."),
 Q("Quel evenement restaure le nombre diploid apres la fecondation ?", "La mitose~L'union des deux pronucleus~La mutation~La traduction", 1,
    "La fecondation fusionne les deux gametes et reconstitue les 46 chromosomes."),
 Q("Que peut produire une mutation dans un gene ?", "Toujours une maladie~Une modification de la proteine codee~Une augmentation du nombre de chromosomes~La disparition du noyau", 1,
    "Une mutation change la sequence et peut modifier la proteine, sans effet obligatoire."),
 T("Expliquer le trajet de l'information genetique d'un gene a une proteine.",
    "L'information est d'abord portee par l'ADN du noyau. Lors de la transcription, une copie en ARN messager est synthetisee a partir d'un gene. Cet ARN quitte le noyau et est lu par les ribosomes lors de la traduction : les bases sont lues par groupes de trois, les codons, et chaque codon correspond a un acide amine. La chaine d'acides amines ainsi construite se replie pour donner une proteine fonctionnelle. Une mutation peut changer un codon et donc un acide amine.",
    "On attend les etapes transcription, traduction, codon et proteine, dans le bon ordre."),
 T("Pourquoi la meiose est-elle indispensable a la stabilite du nombre de chromosomes ?",
    "Si les gametes gardaient 46 chromosomes, la fecondation en donnerait 92 a chaque generation. La meiose reduit ce nombre a 23 en separant les chromosomes homologues. La fecondation recombine ensuite un gamete de chaque parent pour retrouver 46 chromosomes. La meiose introduit aussi du brassage, ce qui augmente la diversite genetique. C'est un mecanisme central pour expliquer a la fois la stabilite de l'espece et la variabilite entre individus.",
    "La reponse doit expliquer la reduction, la restoration et le brassage.")],
C("L'information genetique est codee dans l'ADN, transmise par les gametes et exprimee dans les proteines.",
  "ADN -> ARN messager -> proteine",
  "A-T et C-G · 46 chromosomes somatiques · 23 dans les gametes",
  "ADN~Double helice de nucleotides~Gene~Segment codant~Chromosome~ADN condense~Meiose~Division reduisante",
  "Repérer la molecule et ses bases|Localiser le gene|Depeindre transcription et traduction|Compter les chromosomes selon le type cellulaire|Relier mutation et proteine",
  "Confondre mitose et meiose|Croire qu'un gene est une proteine|Oublier l'appariement A-T|Mélanger cellule somatique et gamete",
  "46~Chromosomes somatiques~23~Chromosomes des gametes~A-T~Appariement~Mutation~Changement de sequence",
  "Mitose~Cellules identiques, 46 chromosomes~Meiose~Gametes a 23 chromosomes",
  "Transcription~ADN vers ARN~Traduction~ARN vers proteine"))

# ============================================================ SV3
add("ST2S-A-SV03", "Biodiversite, classification et evolution", "SVT", ["1re"],
S("La biodiversite designe la diversite des especes, des genes et des ecosystemes."
  "|La classification hierarchique range les etres vivants en especes, genres, familles, ordres, classes, embranchements et regnes."
  "|La nomenclature binomiale donne chaque espece un genre et un nom d'espece en latin ; les criteres reposent sur la morphologie et l'ADN."
  "|Une espece est un ensemble d'individus capables de se reproduire entre eux et d'avoir des descendants fertiles."
  "|L'evolution est la modification des caracteres heredites d'une population au cours des generations."
  "|La selection naturelle favorise les individus mieux adaptes a leur environnement."
  "|Les mutations fournissent la variabilite genetique sur laquelle agit la selection."
  "|La derive genetique modifie les frequences des alleles au hasard dans les petites populations."
  "|Les bacteries sont des procaryotes : leur ADN n'est pas enferme dans un noyau."
  "|Les virus ne sont pas consideres comme des etres vivants autonomes : ils necessitent une cellule hote."
  "|L'antibioresistance illustre l'evolution rapide d'une population bacterienne sous pression de selection."
  "|La biodiversite est un enjeu de sante : elle fournit des ressources medicineuses et regule les ecosystemes."),
[Q("Quel est le rang immediatement superieur a l'espece ?", "La famille~Le genre~La classe~Le regne", 1,
    "L'espece est incluse dans le genre, puis la famille, l'ordre, la classe et l'embranchement."),
 Q("Quelle definition d'une espece est classiquement retenue ?", "Des individus de meme couleur~Des individus qui peuvent se reproduire et avoir des descendants fertiles~Des individus du meme continents~Des individus de meme taille", 1,
    "Le critere biologique de l'espece repose sur l'interfertilite."),
 Q("Quel mecanisme favorise les individus les mieux adaptes ?", "La derive genetique~La selection naturelle~La mutation dirige~La symbios", 1,
    "La selection naturelle augmente la frequence des caracteres favorables."),
 Q("Quelle est la source de la variabilite genetique ?", "La selection naturelle seule~Les mutations~L'environnement seul~La reproduction identique", 1,
    "Les mutations creent de nouveaux alleles ; la selection ne fait que trier."),
 Q("Comment appelle-t-on des organismes dont l'ADN n'est pas dans un noyau ?", "Des eucaryotes~Des procaryotes~Des virus~Des champignons", 1,
    "Les bacteries sont des procaryotes, sans noyau veritable."),
 Q("Pourquoi les virus sont-ils particuliers ?", "Ils ont un noyau~Ils ne peuvent se multiplier sans cellule hote~Ils sont toujours inoffensifs~Ils possedent une paroi cellulaire", 1,
    "Les virus sont des parasites intracellulaires obligatoires."),
 Q("Que montre l'antibioresistance ?", "Une evolution lente sans cause~Une selection de bacteries resistantes sous traitement~Une mutation volontaire~Une disparition des bacteries", 1,
    "L'usage d'antibiotiques exerce une pression qui favorise les souches resistantes."),
 T("Expliquer comment une population bacterienne devient resistante a un antibiotique.",
    "Dans une population bacterienne, des mutations rares conferent une resistance. Avant traitement, ces cellules sont minoritaires. L'antibiotique tue les bacteries sensibles mais laisse survivre les resistantes, qui se multiplient ensuite. La frequence du gene de resistance augmente : c'est une evolution par selection naturelle. L'antibiotique ne cree pas la mutation, il selectionne une variante deja presente. Un usage excessif ou incomplet du traitement accelere ce processus.",
    "On attend le role preexistant des mutations, la pression de selection et la conclusion sur l'evolution."),
 T("Montrer en quoi la biodiversite contribue a la sante humaine.",
    "La biodiversite fournit des molecules naturelles utilisees comme medicaments, par exemple des alcaloides vegetaux ou des antibiotiques d'origine fongique. Elle assure aussi des services de regulation : purification de l'eau, pollinisation, lutte naturelle contre les ravageurs et stabilisation des ecosystemes. Une perte de diversite peut favoriser l'emergence de maladies infectieuses en modifiant les equilibres entre especes. Ainsi, proteger la biodiversite est une mesure de prevention sanitaire au meme titre que la vaccination.",
    "La reponse doit relier ressources, regulation des ecosystemes et risques sanitaires.")],
C("La classification organise le vivant et l'evolution explique comment les especes se transforment.",
  "Espece < genre < famille < ordre < classe < embranchement < regne",
  "Evolution = mutation + selection naturelle + derive genetique",
  "Espece~Interfertilite~Genre~Rang superieur~Mutation~Source de variabilite~Selection~Tri des caracteres favorables",
  "Observer les caracteres|Classer selon les criteres|Lire un arbre phylogenetique|Identifier le mecanisme d'evolution|Relier evolution et sante",
  "Confondre espece et genre|Croire que la selection cree des mutations|Classer les virus parmi les bacteries|Oublier la pressure de selection",
  "Antibiotique~Pression de selection~Bacterie resistante~Sous-apres traitement~Biodiversite~Ressources medicineuses~Virus~ Parasite intracellulaire",
  "Procaryote~Sans noyau~Eucaryote~Avec noyau",
  "Selection naturelle~Trie les variants~Derive genetique~Effet du hasard"))

# ============================================================ AN1
add("ST2S-A-AN01", "Present simple and past simple in health contexts", "Anglais", ["1re"],
S("The present simple describes habits, routines and general truths."
  "|It uses the base form of the verb and adds -s or -es with he, she and it."
  "|Negatives and questions in the present simple use do or does plus the base form."
  "|The past simple describes completed actions at a definite time in the past."
  "|Regular past forms end in -ed, while common irregular verbs have their own forms."
  "|Time markers such as yesterday, last week and in 2020 usually require the past simple."
  "|Frequency adverbs such as always, often and never usually go before the main verb."
  "|In a patient record, the present simple describes a current condition and the past simple a previous episode."
  "|The verb to be and the verb to have are irregular in both tenses."
  "|Questions with question words keep the same auxiliary structure."
  "|The short answer uses the same auxiliary as the question."
  "|Mastering both tenses is essential to write a clear handover or a patient history."),
[Q("Which sentence uses the present simple correctly ?", "He go to work every day~He goes to work every day~He gone to work every day~He going to work every day", 1,
    "With he, she and it, the present simple takes -s : he goes."),
 Q("Which time marker requires the past simple ?", "Every morning~Yesterday~Usually~Nowadays", 1,
    "Yesterday refers to a finished time, so the past simple is used."),
 Q("What is the past form of the verb to take ?", "Taked~Taken~Took~Taking", 2,
    "Take is irregular : take, took, taken."),
 Q("How do you make a question in the present simple with they ?", "They do like ?~Do they like ?~Does they like ?~Are they like ?", 1,
    "With they, the auxiliary is do and it comes before the subject."),
 Q("Where does the adverb often usually go ?", "After the auxiliary only~Before the main verb~At the very end always~After the object", 1,
    "Frequency adverbs are normally placed before the main verb : she often feels tired."),
 Q("Which verb is irregular in the past simple ?", "To walk~To work~To be~To like", 2,
    "To be has the forms was and were ; walk, work and like are regular."),
 Q("In a patient history, which tense describes a current symptom ?", "Past simple~Present simple~Past perfect~Future continuous", 1,
    "The present simple describes the current condition : she has a headache since Monday."),
 T("Write three sentences about a patient using one present simple and two past simple forms.",
    "Mrs Dubois has a sore throat and a mild fever. She visited the clinic yesterday. The doctor prescribed a syrup last week. In these sentences, has describes the current condition, while visited and prescribed describe completed actions at precise moments in the past. The contrast between the two tenses allows a care team to distinguish what is still ongoing from what has already happened.",
    "The answer must include one correct present simple and two correct past simple sentences, with a short explanation."),
 T("Explain the difference between She takes her treatment every morning and She took her treatment yesterday.",
    "The first sentence uses the present simple : takes with the -s of the third person singular, and the time marker every morning shows a habit. It describes a regular routine. The second sentence uses the past simple : took is the irregular past form, and yesterday places the action at a finished time. It describes one completed event. In a medical file, both are needed : one for the ongoing treatment, one for a specific previous intake.",
    "Expected elements : habitual present with -s, irregular past form, and the role of the time markers.")],
C("Present simple for routines and current facts, past simple for finished events in a patient record.",
  "Present : base + s (he/she/it) ; Past : base + ed or irregular form",
  "yesterday / last week -> past simple · often / usually -> present simple",
  "Present simple~Habits and current facts~Past simple~Completed past actions~Auxiliary do/does~Questions and negatives~Irregular verb~Own past form",
  "Identify the time marker|Decide whether the situation is current or finished|Choose the correct form|Check the third person -s|Write a short patient history",
  "Forgetting -s with he or she~Using did with an irregular past form~Placing often after the main verb~Confusing took and taken",
  "Every morning~She takes her tablets~Yesterday~She took her tablets~Last week~The doctor prescribed a syrup~Current symptom~She has a headache",
  "Present simple~She lives in Lyon~Past simple~She lived there in 2020",
  "Regular verb~Worked, walked~Irregular verb~Took, went, was"))

# ============================================================ AN2
add("ST2S-A-AN02", "Modal verbs for advice, obligation and ability", "Anglais", ["1re", "Terminale"],
S("Modal verbs are auxiliary verbs that express ability, obligation, possibility or advice."
  "|The main modals are can, may, must, should, have to and need to."
  "|A modal verb is followed by the base form of the main verb, without to, and takes no -s in the third person singular."
  "|Should expresses advice or a recommendation, often in the form You should see a doctor."
  "|Must expresses a strong obligation coming from the speaker."
  "|Have to expresses an external obligation, for example a rule or a medical instruction."
  "|May and might express a possibility or a polite permission."
  "|Can expresses ability or a request ; could is its past or more polite form."
  "|Negatives are formed directly : must not, should not, cannot, often contracted."
  "|Must not means that something is forbidden, while do not have to means that it is not necessary."
  "|Questions invert the subject and the modal : Should I call the nurse ?"
  "|In health communication, choosing the right modal avoids confusion between advice and obligation."),
[Q("Which structure is correct after a modal verb ?", "He should to rest~He should rest~He shoulds rest~He should resting", 1,
    "A modal is followed by the base form without to and has no -s."),
 Q("Which modal expresses a recommendation ?", "Must~Should~Can~Will", 1,
    "Should is used for advice : You should drink more water."),
 Q("What does must not mean ?", "It is not necessary~It is forbidden~It is possible~It is advisable", 1,
    "Must not expresses a prohibition ; do not have to expresses absence of necessity."),
 Q("Which modal expresses an external obligation ?", "Should~Might~Have to~Could", 2,
    "Have to describes a rule or an instruction coming from outside the speaker."),
 Q("Which sentence asks for permission politely ?", "I can you help ?~May I help you ?~Must I help you ?~Should I helped you ?", 1,
    "May I is a polite form used to ask permission."),
 Q("What is the past or more polite form of can ?", "Could~Must~Shall~Would rather", 0,
    "Could can refer to a past ability or soften a request."),
 Q("How is a question with should formed ?", "Should you are ?~Should I call the nurse ?~Do I should call ?~I should call ?", 1,
    "The modal comes before the subject in a question."),
 T("Rewrite these instructions with the appropriate modals : drink water, do not smoke, you are allowed to leave.",
    "You should drink water regularly. You must not smoke in the ward. You may leave the room after the nurse checks your temperature. Should gives a health recommendation, must not states a clear prohibition, and may grants permission. The three modals have different strengths : advice, obligation and permission. Using the wrong one could make an instruction seem optional when it is mandatory.",
    "The answer must use should, must not and may correctly, with the base form of each verb."),
 T("Explain the difference between You must take the tablet and You should take the tablet.",
    "Must expresses a strong obligation : the treatment is required and not taking it may be dangerous. Should expresses advice or a recommendation : it is a good idea, but the decision is left more to the patient. In a care setting, the distinction matters for safety and for respect of the person. A nurse will say You must take this antibiotic if the prescription is essential, but You should rest this afternoon as a recommendation.",
    "Expected elements : obligation versus advice, and a concrete example in a health context.")],
C("Modals express the strength of a message : ability, permission, advice, obligation or possibility.",
  "Modal + base verb : should rest, must not smoke, may leave",
  "should = advice · must = strong obligation · have to = external rule · may = permission",
  "Should~Advice~Must~Strong obligation~Have to~External rule~May~Permission and possibility",
  "Identify the intended speech act|Choose the right modal|Use the base verb after the modal|Check the negative form|Check the question order",
  "Adding to after a modal~Adding -s to a modal~Confusing must not and do not have to~Using must for simple advice",
  "You should rest~Advice~You must not smoke~Prohibition~You may leave~Permission~Could you help~Polite request",
  "Must~Obligation from the speaker~Have to~Obligation from a rule",
  "Should~Recommendation~Must~Requirement"))

# ============================================================ AN3
add("ST2S-A-AN03", "Reading a medicine leaflet and patient instructions in English", "Anglais", ["Terminale"],
S("A package leaflet gives official information about a medicine for patients and caregivers."
  "|The section indications describes the conditions the medicine treats."
  "|The dosage section states how much to take and how often, often with a table by age."
  "|Contraindications list the situations in which the medicine must not be used."
  "|Warnings and precautions describe when to ask a doctor or a pharmacist."
  "|Side effects are grouped by frequency : common, uncommon, rare and very rare."
  "|Interactions list other medicines or foods that can change the effect of the treatment."
  "|The expiry date is the date after which the medicine must not be used."
  "|Take with a glass of water is a typical instruction, and do not exceed the stated dose warns against an overdose."
  "|If symptoms persist, consult your doctor is a common safety sentence."
  "|The passive voice is frequent : the tablet should be swallowed whole."
  "|Understanding these terms helps a French caregiver explain a treatment to an English-speaking patient."),
[Q("Which section says when a medicine must not be used ?", "Dosage~Contraindications~Side effects~Storage", 1,
    "Contraindications list the situations where the medicine is forbidden."),
 Q("What does the expiry date indicate ?", "The date of manufacture~The date after which the medicine must not be used~The date of the next prescription~The date of the last dose", 1,
    "The expiry date marks the end of the period of guaranteed quality and safety."),
 Q("What does common mean in a list of side effects ?", "Very frequent in all patients~Occurring in more than one in ten patients~Impossible~Only in children", 1,
    "Regulatory frequency bands define common as affecting more than one in ten patients."),
 Q("What does Do not exceed the stated dose mean ?", "Take more than indicated~Never take more than the recommended amount~Split the tablet~Stop all treatment", 1,
    "It is a warning against overdose."),
 Q("Which sentence uses the passive voice ?", "The patient swallows the tablet~The tablet should be swallowed whole~The nurse checked the dose~The doctor prescribed a syrup", 1,
    "The passive form is be plus a past participle : should be swallowed."),
 Q("What are interactions ?", "Tastes of the medicine~Effects of other medicines or food on the treatment~Colors of the box~Prices in different countries", 1,
    "Interactions describe how other substances change the effect or the safety of a medicine."),
 Q("What should you do if symptoms persist ?", "Increase the dose~Consult your doctor~Ignore them~Stop all medicines abruptly", 1,
    "The leaflet advises consulting a doctor if symptoms continue."),
 T("Summarise in five lines the key information a caregiver should read before giving a medicine.",
    "A caregiver should check the indications to confirm the medicine is appropriate, read the dosage and the frequency of administration, look for contraindications and interactions with other treatments, note the warnings and the main side effects, and verify the expiry date. The instruction Do not exceed the stated dose must be respected. If any doubt remains, the caregiver should ask a doctor or a pharmacist rather than guess.",
    "Expected elements : indications, dosage, contraindications, interactions, side effects, expiry date and the advice to ask a professional."),
 T("Translate and explain : The tablet should be swallowed whole, with a glass of water, after food.",
    "Le comprime doit etre avale entier, avec un verre d'eau, apres le repas. The passive voice should be swallowed puts the tablet at the centre of the instruction, which is typical of official leaflets : the focus is on the medicine, not on the person. Whole means the tablet must not be crushed or chewed, and after food reduces the risk of stomach irritation. Each detail of the sentence has a practical consequence for safe administration.",
    "The answer must include a correct translation and an explanation of the passive voice and of the two administration conditions.")],
C("A medicine leaflet is a regulated document : each section answers a specific safety question.",
  "Indications + dosage + contraindications + side effects + interactions",
  "should be swallowed = passive voice · do not exceed = prohibition · common = more than one in ten",
  "Indications~Conditions treated~Contraindications~When the drug is forbidden~Side effects~Unwanted reactions~Interactions~Combination risks",
  "Read the indications first|Check the dosage and the age table|Look for contraindications|Screen for interactions and warnings|Verify the expiry date before administration",
  "Translating word for word without checking the dose~Ignoring interactions~Overlooking the expiry date~Confusing contraindications and side effects",
  "Swallow whole~Do not crush the tablet~After food~Reduces stomach irritation~Common~More than one in ten~Expiry date~Do not use after this date",
  "Active ingredient~The substance that acts~Excipient~Inactive component",
  "Passive voice~The tablet is swallowed~Active voice~The patient swallows the tablet"))

# ============================================================ HG1
add("ST2S-A-HG01", "Sante, villes et transitions demographiques", "HGGS", ["1re"],
S("L'etude des populations met en relation sante, demographie et territoire."
  "|La transition demographique designe le passage d'une regime de forte natalite et forte mortalite a un regime faible."
  "|La baisse de la mortalite precede generalement celle de la natalite, ce qui provoque une croissance temporaire."
  "|L'esperance de vie a la naissance est un indicateur synthetique de l'etat de sante d'une population."
  "|La mortalite infantile est particulierement sensible aux conditions d'hygiene et d'acces aux soins."
  "|Les pyramides des ages representent la structure par age et par sexe d'une population."
  "|Une population vieillissante pose des questions de dependance et de financement des soins."
  "|L'urbanisation rapide a longtemps augmente les risques sanitaires liees a la promiscuite et a l'eau non traitee."
  "|Les epidemies de choléra au XIXe siecle ont conduit a des travaux d'assainissement et a l'hygiene publique."
  "|Les cartes de sante permettent de visualiser les disparites territoriales d'acces aux soins."
  "|Les deserts medicaux designent des zones ou la densite de professionnels de sante est tres faible."
  "|En ST2S, ces connaissances aident a comprendre les politiques de prevention et d'amenagement."),
[Q("Qu'indique une forte baisse de la mortalite avant celle de la natalite ?", "Une diminution de la population~Une phase de croissance demographique~Une stagnation~Un vieillissement immediat", 1,
    "C'est le decalage de la transition demographique qui provoque une croissance rapide."),
 Q("Quel indicateur mesure l'etat de sante global d'une population ?", "Le taux de natalite~L'esperance de vie~Le nombre de medecins~La densite de population", 1,
    "L'esperance de vie a la naissance resume la mortalite d'une population."),
 Q("Que represente une pyramide des ages ?", "Une carte des hopitaux~La structure par age et par sexe~Un budget de sante~Une courbe epidemique", 1,
    "La pyramide des ages montre les effectifs par tranche d'age et sexe."),
 Q("Quel evenement historique a favorise l'hygiene publique au XIXe siecle ?", "La decouverte de l'ADN~Les epidemies de cholera~La guerre froide~L'invention du vaccin contre la rougeole", 1,
    "Les epidemies de cholera ont impose l'assainissement des villes et l'eau potable."),
 Q("Qu'appelle-t-on un desert medical ?", "Un hopital ferme~Une zone a faible densite de professionnels de sante~Un deserteur de la sante~Un laboratoire vide", 1,
    "Le terme designe un territoire ou l'acces aux soins est difficile."),
 Q("Quel lien existe-t-il entre urbanisation rapide et risques sanitaires ?", "Aucun lien~Promiscuite et eau non traitee augmentent les risques~L'urbanisation rend malade~Les villes sont toujours plus saines", 1,
    "Une urbanisation sans infrastructures sanitaires adequate accroit les risques infectieux."),
 Q("Quel effet du vieillissement est le plus direct pour le systeme de soins ?", "Moins de consultations~Une augmentation de la dependance et des besoins de soins~Une baisse de l'esperance de vie~Une disparition des maladies chroniques", 1,
    "Le vieillissement accroit la prevalence des maladies chroniques et de la dependance."),
 T("Expliquer pourquoi la baisse de la mortalite infantile est un bon indicateur de l'amelioration de la sante publique.",
    "La mortalite infantile depend tres directement de l'acces a l'eau potable, a l'hygiene, a la vaccination et aux soins maternels et neonatals.Elle baisse donc rapidement quand les conditions de vie et le systeme de sante s'ameliorent, avant meme que l'esperance de vie globale ne progresse fortement. C'est aussi un indicateur sensible aux inegalites sociales et territoriales : deux regions proches peuvent avoir des taux tres differents. Pour ces raisons, elle est utilisee par l'OMS et les pouvoirs publics pour mesurer l'efficacite des politiques de sante.",
    "On attend le lien avec l'hygiene, l'eau, la vaccination et les inegalites."),
 T("Analyser les consequences d'un desert medical dans un territoire rural vieillissant.",
    "Dans un territoire rural ou les jeunes partent et ou la population vieillit, la densite de medecins diminue. Les habitants doivent parcourir de plus grandes distances, ce qui retarde les diagnostics et le suivi des maladies chroniques. Les urgences et les hospitalisations evitables augmentent, ainsi que le cout pour la collectivite. Les reponses possibles sont la telemedecine, les centres de sante pluriprofessionnels, les maisons de sante et des incitations a l'installation. Ces mesures visent a maintenir un acces equitable aux soins.",
    "La reponse doit relier demographie, acces aux soins, consequences sanitaires et pistes d'action.")],
C("La sante d'une population se lit dans les indicateurs demographiques et dans la repartition des soins sur le territoire.",
  "Transition demographique : forte natalite et mortalite -> faible natalite et mortalite",
  "Esperance de vie · mortalite infantile · pyramide des ages · desert medical",
  "Transition~Changement du regime demographique~Esperance de vie~Indicateur de sante~Pyramide des ages~Structure par age~Desert medical~Acces limite aux soins",
  "Lire les indicateurs demographiques|Construire ou interpreter une pyramide des ages|Localiser les disparites sur une carte|Identifier les facteurs d'urbanisation|Proposer des reponses d'amenagement sante",
  "Confondre natalite et mortalite|Lire une pyramide comme une courbe|Ignorer les ecarts territoriaux|Oublier le role de l'assainissement",
  "Cholera~Epidemie du XIXe siecle~Assainissement~Eau potable et egouts~Vieillissement~Dependance croissante~Telemedecine~Reponse au desert medical",
  "Forte mortalite et natalite~Regime ancien~Faible mortalite et natalite~Regime actuel",
  "Esperance de vie~Duree de vie moyenne~Mortalite infantile~Deces avant un an"))

# ============================================================ HG2
add("ST2S-A-HG02", "Developpement durable, inegalites et solidarites de sante", "HGGS", ["1re", "Terminale"],
S("Le developpement durable repose sur l'equilibre entre les dimensions economique, sociale et environnementale."
  "|Les objectifs du millenaire pour le developpement ont precede les objectifs de developpement durable de l'ONU."
  "|Les ODD comportent 17 objectifs, dont la sante et le bien-etre figurent parmi les plus centraux."
  "|La couverture sanitaire universelle vise a garantir l'acces aux soins pour tous sans appauvrissement."
  "|Les inegalites de sante sont des ecarts systematiques et evitables entre groupes de population."
  "|Le gradient social de sante montre que l'etat de sante s'ameliore avec la position socio-economique."
  "|Les determinants sociaux de la sante comprennent le logement, l'emploi, l'education et l'environnement."
  "|Les pays a faible revenu font face a la fois aux maladies infectieuses et a la montee des maladies chroniques."
  "|La solidarite internationale passe par les programmes de vaccination et le financement de la recherche."
  "|L'OMS coordonne la veille sanitaire internationale et le reglement sanitaire international."
  "|La transition energetique et la lutte contre le changement climatique ont des effets attendus sur la sante."
  "|Une approche durable de la sante demande d'evaluer les couts, l'equite et les impacts environnementaux."),
[Q("Combien d'objectifs de developpement durable compte l'ONU ?", "8~15~17~21", 2,
    "L'Agenda 2030 definit 17 objectifs de developpement durable."),
 Q("Quel objectif des ODD concerne directement la sante ?", "ODD 3~ODD 8~ODD 12~ODD 17", 0,
    "L'ODD 3 vise a permettre a tous de vivre en bonne sante et a promouvoir le bien-etre."),
 Q("Que vise la couverture sanitaire universelle ?", "Des soins gratuits pour tous dans tous les pays~Un acces aux soins pour tous sans risque d'appauvrissement~La fin des hopitaux publics~Une assurance uniquement privee", 1,
    "L'objectif est l'acces equitable a des services de qualite sans difficulté financiere."),
 Q("Comment appelle-t-on les ecarts evitables de sante entre groupes sociaux ?", "Des variations aleatoires~Des inegalites de sante~Des tendances demographiques~Des effets de mode", 1,
    "Les inegalites de sante sont systematiques, evitables et socialement determinees."),
 Q("Quel facteur n'est pas un determinant social de sante ?", "Le logement~L'education~Le groupe sanguin~L'emploi", 2,
    "Le groupe sanguin est un facteur biologique, non un determinant social."),
 Q("Quelle organisation coordonne la veille sanitaire internationale ?", "L'UNICEF~L'OMS~L'OCDE~La Banque mondiale seule", 1,
    "L'Organisation mondiale de la sante definit le reglement sanitaire international."),
 Q("Quel lien existe-t-il entre climat et sante ?", "Aucun~Les vagues de chaleur et les modifications des vecteurs de maladies~Le climat ne concerne que les animaux~La sante n'est pas impactee", 1,
    "Le changement climatique modifie les risques de chaleur, de malnutrition et de maladies vectorielles."),
 T("Definir les determinants sociaux de la sante et expliquer pourquoi ils creent un gradient social.",
    "Les determinants sociaux de la sante sont les conditions dans lesquelles les personnes vivent et travaillent : revenu, education, logement, emploi, accueil de la petite enfance et environnement. Ils creent un gradient car chaque niveau de ressources ouvre des capacites supplementaires : mieux se nourrir, habiter un logement salubre, comprendre une ordonnance, consulter plus tot et supporter les frais de soins. Les avantages s'accumulent tout au long de la vie, ce qui produit des ecarts de sante mesurables entre groupes socio-economiques, meme dans les pays riches.",
    "On attend la definition, des exemples et l'explication de l'accumulation des avantages."),
 T("Montrer comment une action de sante publique peut etre a la fois efficace et durable.",
    "Un programme de vaccination contre la rougeole est efficace car il reduit fortement l'incidence et les deces. Il est durable s'il s'inscrit dans un systeme de soins primaires forme, avec une chaine du froid fiable et un financement previsible, et s'il evalue son cout par cas evite. Sa dimension sociale est assuree si les populations eloignees ou precaires sont effectivement atteintes. La durabilite exige donc de considerer ensemble l'efficacite medicale, l'equite d'acces et la capacite de l'action a durer sans dependre d'un financement exceptionnel.",
    "La reponse doit articuler efficacite, equite et viabilite a long terme.")],
C("Une politique de sante durable concilie efficacite medicale, equite sociale et respect de l'environnement.",
  "13 ODD ; ODD 3 : sante et bien-etre ; couverture sanitaire universelle",
  "Inegalites de sante = ecarts systematiques et evitables · determinants sociaux : logement, emploi, education",
  "ODD 3~Sante et bien-etre~Couverture universelle~Acces sans appauvrissement~Inegalites~Ecarts evitables~Determinants sociaux~Conditions de vie",
  "Identifier l'objectif international vise|Mesurer les ecarts entre groupes|Analyser les determinants en cause|Evaluer l'efficacite et le cout|Verifier l'equite et la durabilite",
  "Confondre ODD et objectifs du millenaire|Croire que la sante depend seulement de la medecine|Negliger le cout d'une action|Oublier les populations eloignees",
  "17 ODD~Agenda 2030~ODD 3~Vivre en bonne sante~Gradient social~Sante selon le statut~OMS~Veille internationale",
  "Objectifs du millenaire~Jusqu'en 2015~Objectifs de developpement durable~Agenda 2030",
  "Inegalites de sante~Ecarts evitables~Variations biologiques~Ecarts naturels"))

# ============================================================ EM1
add("ST2S-A-EM01", "La laicite et les valeurs de la Republique", "EMC", ["1re"],
S("La laicite est un principe constitutionnel qui garantit la liberte de conscience et l'egalite devant la loi."
  "|La loi du 9 decembre 1905 separe les Eglises et l'Etat et organise la liberte d'exercice des cultes."
  "|L'article 1er de la Constitution de 1958 dispose que la Republique est laique."
  "|L'article 10 de la Declaration des droits de l'homme et du citoyen protege la liberte d'opinion."
  "|La laicite ne signifie pas l'interdiction de la religion dans l'espace public."
  "|Elle impose la neutralite de l'Etat, des services publics et de leurs agents."
  "|Les usagers du service public peuvent exprimer leurs convictions, sous reserve de respect de la loi."
  "|Dans un etablissement de sante public, les soignants doivent respecter la neutralite et l'egalite des patients."
  "|La liberte de conscience implique le droit de ne pas avoir de religion."
  "|Les valeurs de la Republique sont la liberte, l'egalite, la fraternite, la laicite et le respect des droits."
  "|Le principe d'egalite interdit toute discrimination fondée sur l'origine, la religion, le sexe ou le handicap."
  "|Le debat sur la laicite exige de distinguer conviction personnelle et obligation professionnelle."),
[Q("Quelle loi fonde la separation des Eglises et de l'Etat en France ?", "La loi du 4 mars 2002~La loi du 9 decembre 1905~La loi du 11 janvier 1978~La loi du 26 janvier 2016", 1,
    "La loi de separation du 9 decembre 1905 est le texte de reference."),
 Q("Que garantit la laicite ?", "L'interdiction de toutes les religions~La liberte de conscience et l'egalite devant la loi~Le financement d'un seul culte~Une religion d'Etat", 1,
    "La laicite protege la liberte de croire ou de ne pas croire et l'egalite de tous."),
 Q("A qui s'impose la neutralite dans le service public ?", "Aux seuls usagers~Aux agents et au service public~A tous les citoyens en permanence~Aux seuls medecins liberalux", 1,
    "Les agents publics et le service public sont tenus a la neutralite."),
 Q("Quel article de la Declaration de 1789 protege la liberte d'opinion ?", "L'article 1er~L'article 10~L'article 49~L'article 75", 1,
    "L'article 10 garantit la liberte d'opinion, a condition de ne pas troubler l'ordre public."),
 Q("La laicite impose-t-elle de cacher sa religion dans la rue ?", "Oui, toujours~Non, elle garantit la liberte d'expression des convictions~Oui pour les mineurs~Seulement dans les ecoles", 1,
    "La laicite ne supprime pas l'expression religieuse dans l'espace public ordinaire."),
 Q("Quel principe interdit les discriminations dans l'acces aux soins ?", "La liberte d'entreprendre~L'egalite~La propriete~La souverainete", 1,
    "Le principe d'egalite s'oppose aux traitements differents non justifies."),
 Q("Quelle situation relève d'une obligation de neutralite professionnelle ?", "Un patient priant dans sa chambre~Un soignant hospitalier portant un signe religieux en service~Un citoyen votant selon ses convictions~Un journaliste interviewant un croyant", 1,
    "L'agent public en service represente le service public et doit etre neutre."),
 T("Distinguer liberte de conscience et neutralite du service public dans un hopital.",
    "La liberte de conscience appartient a chaque personne : un patient peut prier, porter un signe religieux ou demander un accompagnement spirituel, et le droit de ne pas croire est egalement protege. La neutralite du service public concerne l'institution et ses agents : les soignants en service ne doivent pas manifester leurs convictions dans leur pratique professionnelle, afin que chaque patient soit traite de la meme maniere. Les deux principes ne s'opposent pas : la neutralite de l'institution garantit la liberte de conscience de tous les usagers.",
    "La reponse doit separer le droit du patient et l'obligation de l'agent public."),
 T("Comment un soignant doit-il réagir face a une demande de soins motivee par une conviction religieuse ?",
    "Il doit d'abord ecouter la demande sans la juger et evaluer si elle est compatible avec les regles de securite, le consentement libre et eclaire et l'egalite de traitement. Si la demande est acceptable, par exemple la presence d'un proche ou un aménagement de l'horaire d'un repas, il peut y répondre dans le cadre du service. Si elle contrevient a une regle medicale ou au principe d'egalite, il doit l'expliquer avec respect et proposer une alternative. La neutralite ne signifie pas l'indifference : elle impose une egalite de traitement et une attitude professionnelle.",
    "On attend l'ecoute, le respect des regles medicales, l'egalite et une eventualite d'alternative.")],
C("La laicite garantit la liberte de conscience par la neutralite de l'Etat et l'egalite de tous devant la loi.",
  "Loi du 9 decembre 1905 + article 1er de la Constitution de 1958",
  "Liberte de croire ou de ne pas croire · neutralite des agents publics · egalite des usagers",
  "Loi de 1905~Separation des Eglises et de l'Etat~Neutralite~Obligation des agents publics~Conscience~Droit de croire ou non~Egalite~Interdiction des discriminations",
  "Identifier le principe en jeu|Verifier le texte de reference|Distinguer usager et agent|Respecter la liberte du patient|Appliquer l'egalite de traitement",
  "Confondre laicite et atheisme d'Etat|Croire que la neutralite s'impose au patient|Ignorer le droit de ne pas croire|Mélanger conviction et obligation professionnelle",
  "Patient~Liberte de conscience~Soignant hospitalier~Neutralite de service~Priere~Conviction personnelle~Egalite d'acces~Principe constitutionnel",
  "L liberte de conscience~Droit de chacun~Neutralite de l'Etat~Garantie de cette liberte",
  "Espace public~Libre expression des convictions~Service public~Neutralite des agents"))

# ============================================================ EM2
add("ST2S-A-EM02", "Citoyennete, institutions et protection sociale", "EMC", ["1re", "Terminale"],
S("La citoyennete designe l'appartenance a une communaute politique et l'exercice de droits et de devoirs."
  "|La souverainete nationale appartient au peuple, qui l'exerce par le vote et ses representants."
  "|La Constitution de 1958 organise un regime semi-presidentiel."
  "|Le Parlement est compose de l'Assemblee nationale et du Senat : il vote la loi et controle le gouvernment."
  "|Le Conseil constitutionnel verifie la conformite des lois a la Constitution."
  "|Le principe de laicite, d'egalite et de liberte fonde l'ordre republicain."
  "|Le vote est un droit et un devoir civil ; le suffrage est universel et secret."
  "|Les droits civiques peuvent etre limites par la loi dans des cas precis."
  "|La securite sociale repose sur le principe de solidarite nationale."
  "|L'assurance maladie prend en charge une partie des depenses de sante selon des regles de remboursement."
  "|La Carte Vitale et le tiers payant facilitent l'acces aux soins et la gestion des remboursements."
  "|Les institutions europeennes et internationales completent l'action de l'Etat en matiere de sante."),
[Q("Quel texte fonde le regime politique actuel de la France ?", "La Declaration de 1789~La Constitution de 1958~La loi de 1905~Le Code civil de 1804", 1,
    "La Constitution du 4 octobre 1958 institue la Ve Republique."),
 Q("Comment le peuple exerce-t-il la souverainete nationale ?", "Uniquement par le president~Par le vote et ses representants~Par les tribunaux~Par les collectivites seules", 1,
    "La souverainete appartient au peuple, qui s'exprime par le suffrage et les assemblees."),
 Q("Quel est le role du Parlement ?", "Voter la loi et controler le gouvernment~Diriger les hopitaux~Juger les lois~Nommer les medecins", 0,
    "Le Parlement vote la loi, autorise les finances et controle l'action du gouvernment."),
 Q("Quelle institution verifie la conformite d'une loi a la Constitution ?", "Le Conseil d'Etat~Le Conseil constitutionnel~La Cour des comptes~Le tribunal administratif", 1,
    "Le Conseil constitutionnel exerce un controle de constitutionnalite."),
 Q("Quel principe fonde la securite sociale francaise ?", "La concurrence~La solidarite nationale~Le collective des assurances privees~Le seul benefice individuel", 1,
    "La securite sociale mutualise les risques au benefice de tous."),
 Q("Quel dispositif permet souvent d'evancer l'avance de frais chez un professionnel de sante ?", "Le tiers payant~La Carte Vitale seule~Le remboursement forfaitaire~L'hospitalisation", 0,
    "Le tiers payant dispense l'assure de payer immediatement la part prise en charge."),
 Q("Quel caracteristique du suffrage n'est pas respectee si le vote est public ?", "L'universalite~Le secret~La liberte~La periodicite", 1,
    "Le suffrage est secret, ce qui protege la liberte de vote."),
 T("Expliquer la difference entre un droit civique et un devoir civil, avec un exemple lie a la sante.",
    "Un droit civique est une liberte reconnue par la loi, comme le droit de vote ou l'acces aux soins dans des conditions egales. Un devoir civil est une obligation, comme payer ses impots ou respecter les regles d'hygiene et de securite imposees a tous. En sante, le droit d'etre soigne correspond au devoir de ne pas mettre en danger autrui, par exemple en respectant les mesures d'isolement en cas de maladie contagieuse. La citoyennete combine ces deux dimensions : elle donne des droits et exige des responsabilites.",
    "On attend une definition des deux notions et un exemple pertinent."),
 T("Montrer comment la solidarite nationale s'organise dans le systeme de securite sociale.",
    "La solidarite nationale repose sur une mutualisation : les cotisations de tous financent les prestations pour ceux qui en ont besoin, quel que soit leur revenu. L'assurance maladie rembourse une partie des soins selon des taux definis par la loi, et des dispositifs comme le tiers payant ou la complementaire sante universelle reduisent les reste a charge. Les malfusions et les fraudes sont controlees pour preservee les ressources du systeme. Ce mecanisme garantit un acces aux soins plus equitable que le seul système assurantiel prive, tout en necessitant une contribution collective.",
    "La reponse doit expliquer la mutualisation, les remboursements et les dispositifs de protection.")],
C("La citoyennete articule souverainete du peuple, institutions republicaines et solidarite sociale.",
  "Souverainete nationale + suffrage universel + securite sociale",
  "Constitution 1958 · Parlement · Conseil constitutionnel · assurance maladie",
  "Souverainete~Pouvoir appartient au peuple~Parlement~Vote la loi~Securite sociale~Solidarite nationale~Tiers payant~Exoneration d'avance de frais",
  "Identifier l'institution competente|Relier le droit au devoir correspondant|Expliquer le mecanisme de solidarite|Verifier les conditions d'acces aux soins|Respecter les regles communes",
  "Confondre Parlement et Conseil constitutionnel|Croire que le vote est facultatif|Oublier le secret du suffrage|Ignorer le role de la solidarite",
  "Ve Republique~Constitution de 1958~Assemblee nationale~Chambre du Parlement~Assurance maladie~Remboursement des soins~Carte Vitale~Identifiant de l'assure",
  "Droit civique~Liberte reconnue~Devoir civil~Obligation legale",
  "Securite sociale~Mutualisation des risques~Assurance privee~Couverture selon le contrat"))

valider_et_ecrire(F, "st2s-mat-part-A.json")
