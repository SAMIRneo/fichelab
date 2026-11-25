# -*- coding: utf-8 -*-
"""Generateur sthr-mat-part-A.json — lot A : tronc commun (20 fiches).

Français (4), Maths (4), Histoire-Géographie (3), Anglais (2),
EMC (3), Philosophie (4).
12 points de cours, 9 questions corrigees (7 QCM + 2 texte),
7 blocs en ordre strict, 3 schemas via diag().
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sthr_common import S, R, QC, QT, C, build, valider_et_ecrire

F = []

def add(prefix, titre, mat, ans, points, questions, c):
    questions = list(questions) + EXTRA.get(prefix, [])
    F.append(build(prefix, titre, mat, ans, points, questions, c))

EXTRA = {
 "FR2": [QC("Quel signe delimite le discours direct ?", "La virgule~Les guillemets~Le point~La parenthèse", 1,
            "Les guillemets signalent les paroles rapportees directement.")],
 "FR3": [QC("Comment appelle-t-on une pause a l'interieur du vers ?", "La rime~La cesure~La strophe~La coupe", 1,
            "La cesure est la pause interne du vers, souvent apres la sixieme syllabe.")],
 "FR4": [QC("Que place-t-on avant la signature d'une lettre formelle ?", "Un titre~Une formule de politesse~Une rime~Un chapeau", 1,
            "La formule de politesse precede la signature dans la lettre formelle.")],
 "MA1": [QC("Quelle est l'image de 0 par la fonction f(x) = ax + b ?", "0~a~b~a + b", 2,
            "f(0) = b : c'est l'ordonnée a l'origine.")],
 "MA2": [QC("Quelle est la derivee de f(x) = ax + b ?", "a~x~b~ax", 0,
            "La derivee d'une fonction affine est la constante a.")],
 "MA3": [QC("Comment calculer l'etendue d'une serie statistique ?", "Maximum moins minimum~Somme sur effectif~Valeur centrale~Ecart-type carre", 0,
            "L'etendue est la difference entre la valeur maximale et la valeur minimale.")],
 "MA4": [QC("Quelle est la somme des termes d'une suite arithmetique de u0 a u(n) ?",
            "(n+1)(u0+u(n))/2~u0 × q^n~n × u0~u(n) - u0", 0,
            "La somme arithmetique vaut (nombre de termes) × (premier + dernier) / 2."),
         QC("Quelle est la raison d'une suite geometrique d'interets composes au taux t ?", "t~1 + t~1 - t~t/100", 1,
            "Le capital est multiplie par 1 + t a chaque periode.")],
 "HG1": [QC("Quelle organisation inscrit des biens sur la liste du patrimoine mondial ?", "L'ONU~L'UNESCO~L'OMC~L'OCDE", 1,
            "L'UNESCO gere la liste du patrimoine mondial culturel et naturel."),
         QC("Quel evenement fragilise particulierement le tourisme international ?", "Une crise sanitaire~Une nouvelle ligne aerienne~Une hausse de la demande~Un festival local", 0,
            "Les crises sanitaires ou geopolitiques arretent brutalement les deplacements.")],
 "HG2": [QC("Quelle collectivite elabore le plan local d'urbanisme ?", "La commune~Le prefect~Le departement~L'Etat seul", 0,
            "Le PLU est un document d'urbanisme communal."),
         QC("Quelle activite caractérise une station de montagne ?", "La plage~Le ski~La peche~Le port", 1,
            "Les sports d'hiver et la montagne font l'identite de ces stations."),
         QC("Que designe l'artificialisation des sols ?", "La construction sur des sols naturels~L'agriculture biologique~La reforestation~La protection des dunes", 0,
            "L'artificialisation rend un sol impermeable par des constructions ou des voiries.")],
 "HG3": [QC("Que mesure l'espérance de vie a la naissance ?", "L'age moyen au deces~Le nombre d'annees qu'un nouveau-ne peut esperer vivre~Le taux de natalite~L'indice de fecondite", 1,
            "C'est une estimation de la duree de vie a la naissance dans une population donnee."),
         QC("L'IDH est-il identique au PIB par habitant ?", "Oui toujours~Non, il ajoute la sante et l'education~Oui apres conversion~Non, il ignore totalement le revenu", 1,
            "L'IDH est un indicateur composite qui complete le revenu par la sante et l'instruction.")],
 "AN1": [QC("Which modal expresses advice ?", "Must~Should~Can~Will", 1,
            "Should gives advice; must expresses a strong obligation.")],
 "AN2": [QC("Which expression introduces an example ?", "However~For example~Therefore~Although", 1,
            "« For example » introduces an illustration of the previous idea."),
         QC("Which tense is used in « I have worked here since 2022 » ?", "Simple past~Present perfect~Future~Past continuous", 1,
            "The present perfect is required with « since » for a situation that continues.")],
 "EM1": [QC("Quel organe est dirige par le Premier ministre ?", "Le Parlement~Le Gouvernement~Le Senat~Le Conseil d'Etat", 1,
            "Le Premier ministre dirige l'action du Gouvernement."),
         QC("Combien de chambres compte le Parlement francais ?", "Une~Deux~Trois~Quatre", 1,
            "Le Parlement comprend l'Assemblee nationale et le Senat.")],
 "EM2": [QC("Par quoi la liberte d'expression est-elle protegee ?", "Par le seul code civil~Par la Constitution et la Convention europeenne des droits de l'homme~Par un decret~Par le reglement interieur", 1,
            "La liberte d'expression est garantie par les textes constitutionnels et europeens."),
         QC("En quelle annee la Declaration universelle des droits de l'homme a-t-elle ete adoptee ?", "1789~1948~1958~2000", 1,
            "La Declaration universelle des droits de l'homme date de 1948.")],
 "EM3": [QC("Que faut-il faire en cas d'accident du travail ?", "Le taire~Le signaler a l'employeur~Le noter sur un papier personnel~Attendre la fin de la journee", 1,
            "Le salarie doit signaler tout accident du travail pour declencher la procedure."),
         QC("Que designe le DUERP ?", "Un registre de clientele~Le document unique d'evaluation des risques professionnels~Un contrat de travail~Une facture", 1,
            "Le DUERP recense les risques professionnels et les mesures de prevention.")],
 "PH1": [QC("Quel philosophe a formule « connais-toi toi-meme » ?", "Socrate~Freud~Kant~Descartes", 0,
            "La formule est attribuee a Socrate et rapportee par Platon."),
         QC("Que designe le refoulement chez Freud ?", "Un oubli total~Le fait d'ecarter un desir de la conscience~Une maladie~Une methode de relaxation", 1,
            "Le refoulement met a l'ecart de la conscience une representation ou un desir.")],
 "PH2": [QC("Quel est le contraire de la liberte negative ?", "L'absence de contrainte~La liberte positive~Le determinisme~La contrainte", 1,
            "La liberte positive designe le pouvoir reel d'agir."),
         QC("Qui a ecrit « l'existence precede l'essence » ?", "Kant~Sartre~Freud~Diderot", 1,
            "Cette formule resume l'existentialisme de Sartre.")],
 "PH3": [QC("Quelle est la these des sophistes ?", "La verite est absolue~La verite depend de la persuasion~La verite est universelle~La verite n'existe pas", 1,
            "Les sophistes faisaient de la rhetorique le moyen de faire prevaloir une opinion."),
         QC("Quel est le critere de la verite logique ?", "L'evidence sensible~La coherence de la deduction~Le nombre de partisans~La duree de l'analyse", 1,
            "Une deduction valide est coherente avec ses premisses.")],
 "PH4": [QC("Quel est le principal ouvrage economique d'Adam Smith ?", "Le Capital~La Richesse des nations~L'Etre et le Neant~Le Traite d'economie", 1,
            "Adam Smith a publie « Recherches sur la nature et les causes de la richesse des nations »."),
         QC("Que signifie la technè chez Aristote ?", "Un savoir theorique~Un savoir-faire~Un sort~Une vertu morale", 1,
            "La technè est un savoir-faire oriente vers la realisation d'une oeuvre.")],
}

# ============================================================ FR1
add("FR1", "Figures de style et effet de sens dans un texte", "Français", ["1re"],
S("Une figure de style est un procede d'ecriture qui ecartre l'expression courante pour produire un effet de sens ou d'image."
  "|La comparaison etablit un rapprochement explicite entre deux elements grace a un outil comme « comme », « tel » ou « semblable a »."
  "|La metaphore transpose un terme dans un contexte inhabituel sans outil de comparaison : « un ocean de difficultes »."
  "|La personnification attribue des actions ou des sentiments humains a un etre inanime ou a un animal : « le vent hurle »."
  "|L'hyperbole exagere volontairement une realite pour frapper l'imagination ou marquer une intensite."
  "|L'antithese rapproche deux idees ou deux termes opposes afin de creer un contraste saisissant."
  "|L'anaphore repete un meme mot ou une meme expression en debut de phrases ou de vers : elle crée un rythme et insiste sur une idee."
  "|La gradation ordonne des termes par intensite croissante ou decroissante et conduit le lecteur vers un point d'aboutissement."
  "|L'enumeration presente une serie d'elements de meme nature : elle donne une impression d'abondance ou accelere le rythme."
  "|Le registre est l'effet produit sur le lecteur : comique, tragique, pathétique, epique ou lyrique."
  "|Dans un texte argumentatif, la figure de style ne decore pas : elle rend une these plus sensible et plus memorable."
  "|L'analyse stylistique suit trois temps : repérer la figure, citer le passage exact, puis expliquer l'effet produit en lien avec l'intention de l'auteur."),
[QC("Quelle figure utilise un outil de comparaison explicite ?", "La metaphore~La comparaison~La personnification~L'hyperbole", 1,
     "La comparaison est marquee par « comme », « tel », « semblable a » ; la metaphore supprime l'outil."),
 QC("Dans « cette chambre est un four », quelle figure recognisez-vous ?", "Comparaison~Metaphore~Antithese~Gradation", 1,
     "Il y a transposition directe sans outil de comparaison : c'est une metaphore."),
 QC("Comment appelle-t-on la repetition d'un mot en debut de vers ?", "Anaphore~Gradation~Hyperbole~Litote", 0,
     "L'anaphore repete un element en position initiale, ce qui scande le texte."),
 QC("Quel registre vise a susciter la pitié ou l'emotion attendrie ?", "Comique~Pathétique~Epique~Satirique", 1,
     "Le registre pathétique cherche a émouvoir ; le registre comique vise le rire."),
 QC("La gradation consiste a...", "Repeter un son~Ordonner des termes par intensite~Opposer deux mots~Exagerer un chiffre", 1,
     "La gradation classe les termes du plus faible au plus fort ou inversement."),
 QC("« Le vieux hotelgeveille » est une...", "Metaphore~Personnification~Comparaison~Enumeration", 1,
     "On attribue une action humaine, « geville », a un etre inanime : c'est une personnification."),
 QC("Apres avoir repere une figure, que fait-on dans une analyse ?", "On la nomme et c'est fini~On cite le passage et on explique son effet~On la remplace par une autre~On traduit la phrase", 1,
     "L'analyse complete nomme, cite puis interprete l'effet produit."),
 QT("Analyser la metaphore « un ocean de difficultes » dans une lettre de motivation.",
     "Le mot « ocean » est transporte dans le domaine des difficultes : c'est une metaphore, sans outil de comparaison. Le terme connote l'immensite, la profondeur et le mouvement, ce qui transforme une simple liste de problemes en une epreuve presque insurmontable. L'effet est pathétique et dramatise la situation du locuteur. Dans une lettre de motivation, l'auteur peut employer cette image pour montrer qu'il a traverse des epreuves difficiles avant de postuler, tout en gardant une note de maitrise de soi. On cite exactement l'expression, on nomme la figure, puis on relie la connotation a l'intention.",
     "La bonne reponse nomme la metaphore, releve la connotation d'immensite et relie l'effet a l'intention du scripteur."),
 QT("Decrire la demarche d'analyse stylistique d'un extrait de roman en trois etapes.",
     "On lit d'abord le passage en entier pour identifier le sens global et le registre dominant. On repère ensuite les procedes : figures de style, rythme, vocabulaire, temps verbaux et modalites. Pour chaque procede, on cite les mots exacts entre guillemets, on nomme la figure avec precision, puis on explique l'effet produit sur le lecteur et l'intention de l'auteur. On termine en reliant les observations a une interpretation d'ensemble : le passage presente-t-il le personnage comme fragile, comique ou menacant ? Une analyse ne se contente jamais d'etiqueter : elle demontre.",
     "On attend les trois temps lecture, repérage, interpretation avec citation et lien avec l'intention.")],
C("Une figure de style est un ecart volontaire de langage : on la nomme, on la cite, puis on explique ce qu'elle produit.",
  "Figure = ecart + effet de sens",
  "Comparaison avec outil · metaphore sans outil · anaphore en debut",
  "Comparaison~Rapprochement avec outil~Comme, tel~Metaphore~Transposition directe~Sans outil~Personnification~Donner des traits humains~Le vent hurle~Antithese~Opposer deux termes~Ombre et lumière~Hyperbole~Exagerer volontairement~Mille fois",
  "Lire le passage entier|Repérer les mots qui sortent du langage courant|Nommer la figure avec precision|Citer l'expression exacte|Expliquer l'effet et l'intention",
  "Confondre comparaison et metaphore|Nommer une figure sans la citer|Inventer une citation|Oublier de relier l'effet au contexte",
  "Ocean~Immensite et profondeur~Difficultes~Epreuve difficile~Vent hurle~Personnification~Rhythme~Anaphore et gradation",
  "Comparaison~Outil explicite~Comme, tel~Metaphore~Transposition directe~Aucun outil",
  "Anaphore~Repetition en debut~Rythme et insistance~Enumeration~Suite d'elements~Abondance"))

# ============================================================ FR2
add("FR2", "Recit et roman : situation d'énonciation et point de vue", "Français", ["1re"],
S("Un recit est une suite d'evenements racontes dans un ordre choisi par le narrateur, reel ou fictif."
  "|La situation d'énonciation designe les circonstances dans lesquelles un texte est produit : qui parle, a qui, quand et ou."
  "|Les pronoms personnels sont les repères de l'énonciation : « je » designe le locuteur, « tu » le destinataire, « il » un tiers."
  "|Les deictiques comme « ici », « maintenant », « ce matin » ne prennent leur sens que par rapport a la situation d'énonciation."
  "|Le narrateur peut être interne, quand il participe a l'action, ou externe, quand il se place en dehors de l'histoire."
  "|La focalisation interne adopte le point de vue d'un personnage : le recit rapporte ce qu'il voit, pense et ressent."
  "|La focalisation externe donne a voir les actions et les paroles sans acceder aux pensees des personnages."
  "|La focalisation omnisciente permet au narrateur de connaitre les pensees, les sentiments et l'avenir de tous les personnages."
  "|Le recit au passe simple, typique du roman, presente les actions comme achevees et distantes ; le present de narration rapproche l'evenement du lecteur."
  "|Le discours direct rapporte les paroles entre guillemets, le discours indirect les integre dans la phrase avec des modifications de temps et de pronoms."
  "|Le roman est une fiction narrative longue qui construit un monde, des personnages et une intrigue organises en chapitres."
  "|L'etude d'un extrait de roman consiste a identifier le narrateur, la focalisation, le temps dominant et l'effet de point de vue sur la reception."),
[QC("Quel pronom designe le locuteur dans une situation d'énonciation ?", "Il~Je~On~Ils", 1,
     "« Je » est le pronom de la premiere personne : il designe celui qui parle."),
 QC("Qu'appelle-t-on un deictique ?", "Un mot de liaison~Un mot qui depend de la situation~Un adjectif~Une figure de style", 1,
     "« Ici », « maintenant », « demain » sont des deictiques : leur sens depend du contexte d'énonciation."),
 QC("Un narrateur qui raconte ce qu'il a vecu est...", "Externe~Interne~Omniscient~Impersonnel", 1,
     "Le narrateur interne appartient a l'histoire et emploie souvent la premiere personne."),
 QC("Quelle focalisation donne acces aux pensees de tous les personnages ?", "Externe~Interne~Omnisciente~Esthetique", 2,
     "La focalisation omnisciente donne au narrateur une vue complete sur les consciences."),
 QC("Quel temps est classique du recit de roman ?", "Present de l'indicatif~Passe simple~Futur simple~Imperatif", 1,
     "Le passe simple est le temps du recit historique et romanesque, a cote de l'imparfait."),
 QC("Comment reconnait-on le discours direct ?", "Il est introduit par « que »~Il est place entre guillemets~Il est au passe~Il supprime les verbes de parole", 1,
     "Le discours direct cite les paroles entre guillemets, souvent avec un verbe de parole."),
 QT("Dire ce que change le passage d'une focalisation omnisciente a une focalisation interne dans un extrait.",
     "Avec une focalisation omnisciente, le lecteur sait tout : les pensees des personnages, leurs secrets et parfois leur avenir. Cela crée une distance ironique ou tragique, car le lecteur en sait plus que les personnages. En focalisation interne, le narrateur se limite a une conscience : les evenements sont filtres par les perceptions, les souvenirs et les erreurs de ce personnage. Le lecteur ne connait que ce que celui-ci connait, ce qui renforce l'identification et le suspense, mais peut induire en erreur si le point de vue est partial ou menteur. Le changement de focalisation modifie donc la quantite d'information et la position emotionnelle du lecteur.",
     "La reponse doit opposer etendue du savoir et effets de lecture : distance ou identification, suspense."),
 QT("Dans un extrait, le narrateur dit « je me souviens de cette chambre ou nous avons dine ». Identifier la situation d'énonciation et le temps du recit.",
     "Le « je » marque un narrateur interne qui parle de lui-meme ; le destinataire est le lecteur, non designe. Le passe compose et l'imparfait « avons dine », « etaient » situent le souvenir dans le passe, avec un narrateur qui se souvient apres les faits. Les elements « cette chambre » et « nous » ancrent le recit dans une situation passee precise, que le narrateur reconstruit depuis le present de l'ecriture. On a donc un recit a premiere personne, en focalisation interne, avec une distance temporelle entre le moment vecu et le moment raconte.",
     "On attend l'identification du narrateur interne, du destinataire, du temps et de la distance entre vécu et raconte.")],
C("Le recit depend du point de vue adopte : le narrateur choisit ce qu'il sait, ce qu'il montre et la distance qu'il prend.",
  "Recit = evenements + narrateur + focalisation",
  "Interne = une conscience · externe = actions seules · omnisciente = tous les savoirs",
  "Narrateur~Instance qui raconte~Je ou il~Focalisation interne~Point de vue d'un personnage~Ses pensees~Focalisation externe~Actions et paroles~Rien des pensees~Passe simple~Temps du recit~Actions achevees~Discours indirect~Paroles integrees~Changement de temps",
  "Repérer les pronoms personnels|Identifier le narrateur interne ou externe|Determiner la focalisation|Relever les temps verbaux dominants|Mesurer l'effet sur le lecteur",
  "Confondre auteur et narrateur|Nommer la focalisation sans la justifier|Oublier les changements de temps|Ignorer le destinataire",
  "Je~Narrateur interne~Souvenir~Passe compose~Omniscient~Tout savoir~Distance ironique",
  "Narrateur interne~Vit l'action~Je~Narrateur externe~Dehors~Il",
  "Focalisation interne~Une conscience~Identification~Omnisciente~Toutes les consciences~Distance"))

# ============================================================ FR3
add("FR3", "Poésie : image poétique, rythme et lecture", "Français", ["1re"],
S("Le poeme est un texte ou la forme, le rythme et l'image comptent autant que le sens littéral."
  "|Le vers est une ligne de poeme ; sa mesure correspond au nombre de syllabes, comme l'alexandrin de douze syllabes."
  "|La rime est la repetition d'un son final entre deux vers ; elle peut etre riche, pauvre ou suffisante."
  "|Les strophes regroupent des vers selon une disposition fixe, qui contribue a l'architecture du poeme."
  "|L'image poétique associe deux realites eloignees pour reveler une qualite sensible ou une emotion."
  "|La metaphore, la comparaison, la personnification et le symbolisme sont les principaux procedes de l'image poétique."
  "|Le rythme naît de la disposition des accents, des cesures et des repetitions : il peut etre vif, lent ou solennel."
  "|La cesure est une pause a l'interieur du vers, souvent apres la sixieme syllabe dans l'alexandrin classique."
  "|Le son et la couleur des mots produisent une musicalite que l'on étudie avec les alliterations et les assonances."
  "|Le poeme en prose ne respecte pas la disposition en vers mais recherche les memes effets d'image et de rythme."
  "|Lire un poeme, c'est d'abord respecter les coupures du vers, puis interpreter les images en tenant compte du titre et du contexte."
  "|Une lecture poetique rigoureuse combine observations formelles, repérage des images et interpretation de l'emotion exprimee."),
[QC("Combien de syllabes compte un alexandrin ?", "Huit~Dix~Douze~Quatorze", 2,
     "L'alexandrin classique compte douze syllabes, avec une cesure generalement a la sixieme."),
 QC("Qu'est-ce qu'une alliteration ?", "Repetition d'une voyelle~Repetition d'une consonne~Rime pauvre~Pause interne", 1,
     "L'alliteration repete une consonne ; l'assonance repete une voyelle."),
 QC("Ou se place generalement la cesure de l'alexandrin ?", "Apres la 3e syllabe~Apres la 6e syllabe~Apres la 10e syllabe~En fin de vers", 1,
     "L'alexandrin classique se coupe en deux hemistiches de six syllabes."),
 QC("Qu'appelle-t-on une strophe ?", "Un vers isole~Un groupe de vers~Une rime~Un titre", 1,
     "La strophe est un ensemble de vers organises selon une disposition reguliere."),
 QC("Quel est l'effet d'une image poétique ?", "Donner une definition~Reveler une qualite sensible~Remplacer la ponctuation~Allonger le poeme", 1,
     "L'image cree une association inattendue qui rend sensible une emotion ou une qualite."),
 QC("Un poeme en prose...", "N'a ni rythme ni image~Ne se dispose pas en vers~Est toujours un sonnet~Est un roman court", 1,
     "Le poeme en prose garde la recherche d'image et de rythme sans la disposition en vers."),
 QT("Expliquer comment le rythme contribue au sens d'un poeme.",
     "Le rythme n'est pas un simple decor : il accompagne l'emotion. Des vers courts et des accents nombreux donnent une impression de vivacite, d'urgence ou de colere. Des vers longs, une cesure marquee et des repetitions lentes produisent une atmosphere grave, melancolique ou solennelle. Les alliterations et les assonances creent une musicalite qui peut imiter un bruit, souligner un mot ou installer une harmonie. Le lecteur doit observer la mesure, les pauses, les repetitions et les rimes, puis montrer comment ces choix formels renforcent le sentiment exprime par les images. La forme devient alors une partie du sens.",
     "On attend le lien entre elements formels (mesure, cesure, sons) et emotion produite."),
 QT("Quelle demarche suivre pour commenter un poeme en trois temps ?",
     "On commence par une lecture attentive en respectant les vers et la ponctuation, puis on relève les caracteristiques formelles : type de vers, rimes, strophes, rythme et sons. On identifie ensuite les images principales et les figures de style, en citant les mots exacts et en expliquant leur sens implicite. On termine par une interpretation d'ensemble : le titre, le contexte de publication et les images construisent une emotion ou une reflexion. La conclusion montre comment forme et fond cooperent pour produire le sens du poeme.",
     "On attend lecture, analyse formelle, analyse des images puis interpretation d'ensemble.")],
C("Dans un poeme, la forme produit du sens : mesurer, ecouter et interpreter vont ensemble.",
  "Poeme = vers + rythme + image",
  "Alexandrin : 12 syllabes · cesure apres la 6e · rime en fin de vers",
  "Vers~Ligne de poeme~Alexandrin 12~Rime~Son final repetition~Riche ou pauvre~Cesure~Pause interne~Apres 6 syllabes~Image~Association inattendue~Metaphore~Alliteration~Repetition d'une consonne",
  "Lire en respectant les vers|Mesurer et relever rimes et strophes|Observer les accents et les pauses|Repérer les images et les figures|Interpreter le lien forme-sens",
  "Lire un poeme comme un texte en prose|Confondre alliteration et assonance|Ignorer le titre|Parler d'image sans citer les mots",
  "Alexandrin~Douze syllabes~Rime~Son final~Cesure~Apres la sixieme~Image~Sens implicite",
  "Alliteration~Consonne repetee~Assonance~Voyelle repetee",
  "Poeme en vers~Disposition reguliere~Poeme en prose~Libre mais rythme"))

# ============================================================ FR4
add("FR4", "Écriture d'invention et épreuve orale de français", "Français", ["1re"],
S("L'ecriture d'invention demande de produire un texte personnel en respectant une consigne de genre, de situation et de longueur."
  "|La consigne precise le destinataire, l'intention communicative, le genre attendu et parfois des elements a utiliser."
  "|Avant d'ecrire, on analyse la commande : qui parle, a qui, pourquoi et sous quelle forme ?"
  "|Le plan d'un texte d'invention comporte generalement une introduction, un developpement organise et une conclusion adaptée au genre."
  "|Une lettre comporte une formule d'appel, une formule de politesse et une signature ; un article de presse comporte un titre et un chapeau."
  "|Le raisonnement doit etre progressive : une idee par paragraphe, avec des exemples et des connecteurs logiques."
  "|Les registres employes doivent rester coherents avec la situation d'énonciation imposee par la consigne."
  "|La ponctuation, l'orthographe et la syntaxe sont evaluees : une copie soignee est une copie lisible et corregee."
  "|L'oral de français comporte une exposition d'un texte au programme, un entretien sur le parcours et une explication de texte."
  "|La lecture a voix haute doit etre claire, debrouillee et expressieve : elle montre la comprehension du texte."
  "|L'explication orale suit un plan annonce : situation du texte, axes de lecture, puis analyse precise des procedes."
  "|La preparation de l'oral s'appuie sur une fiche de synthèse courte, des citations choisies et une maîtrise du vocabulaire critique."),
[QC("Que doit-on identifier en premier dans une consigne d'ecriture ?", "La longueur seule~Qui parle, a qui et pourquoi~Le nombre de paragraphes~La police de caracteres", 1,
     "La situation d'énonciation est le premier element a analyser dans une consigne."),
 QC("Quels elements caracterisent une lettre ?", "Un titre et un chapeau~Une formule d'appel et de politesse~Des rimes~Des didascalies", 1,
     "La lettre est un texte epistolaire avec appel, corps et formule de politesse."),
 QC("Comment organizer le developpement d'un texte d'invention ?", "Une idee par paragraphe avec exemples~Tout dans un seul paragraphe~Sans connecteurs~En repetitions identiques", 0,
     "Un paragraphe = une idee principale developpee et illustree."),
 QC("Quel est un objectif de la lecture a voix haute a l'oral ?", "Lire le plus vite possible~Montrer la comprehension par le rythme et les pauses~Eviter les pauses~Changer les mots du texte", 1,
     "Une lecture claire et expressieve traduit la comprehension du texte."),
 QC("Que contient une fiche de preparation pour l'oral ?", "Tout le texte recopie~Des axes, des citations et du vocabulaire critique~Un resume factice~Des images", 1,
     "La fiche doit rester courte et operatoire : axes, citations, notions."),
 QC("Quelle partie de l'oral porte sur plusieurs oeuvres du parcours ?", "La lecture~L'explication~L'entretien sur le parcours~La dictée", 2,
     "L'entretien porte sur le parcours de lecture et les oeuvres etudiees."),
 QT("Comment transformer une consigne « vous ecrivez au directeur pour demander une salle de restauration » en plan de lettre ?",
     "On identifie d'abord la situation : l'ecrivant est un eleve ou un enseignant, le destinataire est le directeur, l'intention est une demande argumentee. On construit ensuite trois parties : rappel du contexte et du besoin, presention des Arguments favorables (effectifs, horaires, usage pedagogique de la salle), puis proposition concrete et formule de politesse. On emploie un registre formel, des formules de requesting (« je vous serais reconnaissant de... »), des connecteurs d'argumentation et une signature. On relit enfin le respect de la consigne : longueur, elements imposes et coherence du ton.",
     "On attend l'analyse de la situation, un plan en trois temps, le registre formel et la relecture de la consigne."),
 QT("Expliquer en quoi l'oral de français evalue la comprehension et non la memoire.",
     "L'explication de texte demande de construire un commentaire organise a partir d'un passage inconnu ou prepare : il faut repérer les procedes, les citer et expliquer leur effet. L'entretien sur le parcours mobilise les oeuvres etudiees, mais il attend une reflexion personnelle, des comparisons et une posture de lecture, pas une recitation. La lecture a voix haute revele la comprehension rythmique et syntaxique du texte. Les examinateurs evaluent la capacite a argumenter, a formuler une opinion motivee et a utiliser un vocabulaire critique precise. Une réponse memorisee mais non adaptée aux questions posées sera donc moins bien evaluée qu'une analyse sincere et structuree.",
     "On doit montrer que l'epreuve mesure l'argumentation, l'analyse et la lecture, pas la restitution mecanique.")],
C("Ecrire, c'est repondre precisement a une consigne ; a l'oral, c'est montrer une lecture comprise et argumentee.",
  "Texte = situation d'énonciation + genre + intention",
  "Consigne : qui, a qui, pourquoi, sous quelle forme",
  "Consigne~Commande precise~Destinataire et genre~Lettre~Appel et politesse~Registre formel~Article~Titre et chapeau~Oral~Explication et entretien~Lecture~Voix claire et pauses",
  "Analyser la consigne|Choisir le genre et le ton|Construire un plan en trois temps|Ecrire puis relire|Preparer fiche et citations pour l'oral",
  "Repondre a cote de la consigne|Melanger les registres|Oublier la formule de politesse|Reciter au lieu d'analyser",
  "Lettre~Destinataire nomme~Demande~Arguments et politesse~Oral~Lexique critique~Fiche~Axes et citations",
  "Ecrit~Texte compose et relu~Oral~Lecture et argumentation en direct",
  "Introduction~Annonce du plan~Conclusion~Reponse a la problematique"))

# ============================================================ MA1
add("MA1", "Fonctions, variations et modélisation", "Maths", ["1re"],
S("Une fonction f associe a chaque nombre x d'un ensemble de depart un nombre unique f(x), appele image."
  "|L'ensemble de definition regroupe les valeurs de x pour lesquelles f(x) existe ; l'ensemble d'arrivee contient les images possibles."
  "|Le graphique d'une fonction represente les couples (x ; f(x)) dans un repere orthonorme."
  "|Une fonction est croissante sur un intervalle si x1 < x2 entraine f(x1) <= f(x2) : la courbe monte de gauche a droite."
  "|Une fonction est decroissante si x1 < x2 entraine f(x1) >= f(x2) : la courbe descend de gauche a droite."
  "|Le coefficient directeur d'une fonction affine f(x) = ax + b donne la pente de la droite : a > 0 pour une croissance, a < 0 pour une decroissance."
  "|Le terme initial b est l'ordinate a l'origine : il donne la valeur de f(0) et souvent le cout fixe d'une situation concrete."
  "|Une fonction lineaire est de la forme f(x) = ax : sa courbe passe toujours par l'origine du repere."
  "|Lire un graphique consiste a retrouver une image, un antecédent, les intersections avec les axes et les extremums."
  "|La lecture graphique doit toujours preciser l'unite et l'echelle des axes pour eviter une interpretation faussee."
  "|En hôtellerie, une fonction peut modele le prix total d'un sejour selon le nombre de nuits ou le cout d'un service selon le nombre de couverts."
  "|La modelisation comporte trois etapes : identifier les grandeurs, choisir un type de fonction, puis verifier la pertinence du modele sur des valeurs connues."),
[QC("Que designe f(3) ?", "L'antecédent de 3~L'image de 3 par f~La pente de f~L'ensemble de definition", 1,
     "f(3) est le nombre associe a 3 par la fonction, appele image de 3."),
 QC("Dans f(x) = ax + b, que represente a ?", "La valeur initiale~Le coefficient directeur~L'image de 0~L'ensemble d'arrivee", 1,
     "a est la pente de la droite : il donne le sens de variation et la vitesse de croissance."),
 QC("Une fonction est decroissante quand...", "La courbe monte~x augmente et f(x) diminue~f(x) est toujours negative~a est positif", 1,
     "La decroissance signifie que l'image diminue quand l'antecédent augmente."),
 QC("Quel point la courbe d'une fonction lineaire passe-t-elle toujours ?", "(0 ; 0)~ (0 ; b)~ (1 ; a)~ (a ; 0)", 0,
     "Pour f(x) = ax, f(0) = 0 : la droite passe par l'origine."),
 QC("Pour f(x) = 25x + 80, quelle est la valeur initiale ?", "25~80~105~0", 1,
     "b = 80 est l'ordonnée a l'origine, soit l'image de 0."),
 QC("Que faut-il preciser pour lire correctement un graphique ?", "La couleur de la courbe~L'echelle et l'unite des axes~Le nom du graphique~Le nombre de points", 1,
     "Sans echelle ni unite, la lecture graphique n'a pas de sens quantitatif."),
 QT("Un hotel facture 90 € par nuit plus 25 € de frais de dossier. Exprimer le cout total en fonction du nombre de nuits et calculer le cout pour 4 nuits.",
     "On designe par x le nombre de nuits et par C(x) le cout total en euros. La partie variable vaut 90x et la partie fixe 25 €, donc C(x) = 90x + 25. Pour x = 4, C(4) = 90 × 4 + 25 = 360 + 25 = 385 €. Le coefficient directeur 90 represente le cout marginal d'une nuit supplementaire et le terme initial 25 le frais fixe paye une seule fois, meme pour une nuit. Le modele est affine et non lineaire puisqu'il ne passe pas par l'origine.",
     "La reponse doit donner C(x) = 90x + 25, calculer 385 € et interpreter les deux coefficients."),
 QT("Expliquer la demarche de modelisation d'une situation de service avec une fonction.",
     "On identifie d'abord les grandeurs : la variable independante (nombre de couverts, de nuits, de kilometres) et la grandeur a expliquer (recette, cout, temps). On choisit ensuite une forme de fonction coherente : affine quand il y a un cout fixe et un cout unitaire constant, lineaire quand il n'y a pas de terme fixe. On ecrit l'expression, on precise l'ensemble de definition en tenant compte des valeurs entieres et des bornes reelles. Enfin, on verifie le modele en calculant une ou deux valeurs de reference et on analyse la pertinence de la pente et de l'ordonnée a l'origine avant de l'utiliser pour prevoir.",
     "On attend identification des grandeurs, choix du modele, domaine de definition et verification.")],
C("Une fonction traduit une dependance entre grandeurs : pente, valeur initiale et variations se lisent sur la courbe.",
  "f(x) = ax + b",
  "a = pente (variation) · b = image de 0 (valeur initiale)",
  "Fonction~Associe un antecédent a une image~f(x)~Image~Croissante~La courbe monte~a positif~Decroissante~La courbe descend~a negatif~Affine~Droite avec terme initial~ ax + b",
  "Identifier les grandeurs|Choisir le type de fonction|Ecrire l'expression et le domaine|Tracer ou lire la courbe|Verifier sur une valeur connue",
  "Confondre image et antecédent|Oublier le terme fixe|Lire une courbe sans echelle|Appliquer le modele hors de son domaine",
  "90 €~Cout par nuit~25 €~Frais de dossier fixes~4 nuits~385 €~Pente~90 euros par nuit",
  "Fonction lineaire~f(x)=ax~Passe par l'origine~Fonction affine~f(x)=ax+b~Ordonnee initiale b",
  "Croissance~a positif~Decroissance~a negatif"))

# ============================================================ MA2
add("MA2", "Dérivation et optimisation d'une quantité", "Maths", ["1re", "Terminale"],
S("La derivee d'une fonction f en un point x donne le taux de variation instantane de f en ce point."
  "|Geometriquement, f'(x) est le coefficient directeur de la tangente a la courbe de f au point d'abscisse x."
  "|La fonction derivee de f(x) = x² est f'(x) = 2x ; celle de f(x) = ax + b est la constante a."
  "|Les regles de derivation usuelles portent sur les sommes, les produits, les quotients et les composees."
  "|Quand f'(x) > 0 sur un intervalle, f est croissante sur cet intervalle ; quand f'(x) < 0, f est decroissante."
  "|Un point ou f'(x) s'annule en changeant de signe est un extremum local de la fonction."
  "|Le signe de la derivee se resume dans un tableau de signes, qui donne directement les variations de f."
  "|Chercher un maximum ou un minimum revient souvent a resoudre f'(x) = 0 puis a étudier le changement de signe."
  "|Dans un probleme d'optimisation, il faut d'abord exprimer la grandeur a optimiser en fonction d'une seule variable."
  "|La derivee donne le cout ou le benefice marginal : par exemple la variation de recette quand on augmente le prix d'une unite."
  "|Il faut toujours verifier que la solution trouvee appartient a l'ensemble de definition et respecte les contraintes du probleme."
  "|En economie hoteliere, l'optimisation peut porter sur le prix de vente, le nombre de chambres ou la quantite commandee."),
[QC("Que represente f'(x) ?", "La valeur de f en x~Le taux de variation instantane~L'aire sous la courbe~L'image de 0", 1,
     "La derivee mesure la variation infinitésimale de la fonction en un point."),
 QC("Quelle est la derivee de f(x) = x² ?", "x~2x~x~2", 1,
     "La regle donne f'(x) = 2x pour une fonction carree."),
 QC("Si f'(x) < 0 sur un intervalle, la fonction est...", "Croissante~Constant~Decroissante~Stationnaire", 2,
     "Une derivee negative traduit une decroissance locale."),
 QC("Comment repérer un extremum avec la derivee ?", "Quand f'(x) est maximum~Quand f'(x) s'annule en changeant de signe~Quand f(x) = 0~Quand la courbe coupe l'axe des x", 1,
     "Un changement de signe de la derivee correspond a un extremum local."),
 QC("Quel outil resumé les variations d'une fonction ?", "Le tableau de signes de la derivee~Le tableau de valeurs de la fonction~Le repere~La regle de trois", 0,
     "Le signe de f' donne directement le sens de variation de f."),
 QC("Dans un probleme d'optimisation, que faire apres avoir resolu f'(x) = 0 ?", "Arreter l'etude~Verifier le changement de signe et les contraintes~Changer de variable~Tracer un histogramme", 1,
     "Il faut qualifier l'extremum et verifier son admissibilite."),
 QT("Une recette est donnee par R(p) = -2p² + 120p, avec p le prix en euros. Trouver le prix qui maximise la recette.",
     "On derive : R'(p) = -4p + 120. On resout R'(p) = 0, soit -4p + 120 = 0, d'ou p = 30. La derivee est positive avant 30 et negative apres 30 : la fonction augmente puis diminue, donc p = 30 donne un maximum. La recette maximale vaut R(30) = -2 × 900 + 120 × 30 = -1800 + 3600 = 1800 €. Ce prix appartient au domaine positif et respecte le modele : il s'agit bien du prix optimal dans le cadre de cette fonction de demande.",
     "On attend le calcul de R', la resolution R'=0, l'etude de signe et la valeur de la recette maximale."),
 QT("Expliquer pourquoi la derivee est utile pour piloter un service, au-delà du simple calcul de variations.",
     "La derivee mesure une variation marginale : elle indique combien la grandeur observee change pour une petite augmentation de la variable de decision. Dans un service, elle repond par exemple a la question : combien gagne-t-on en augmentant le prix d'un euro, ou en ouvrant une heure supplementaire ? Tant que la derivee du benefice est positive, l'augmentation est favorable ; lorsqu'elle devient negative, elle detruit de la valeur. L'etude de signe permet donc de fixer un seuil optimal. Mais le modele reste une simplification : il faut controler les contraintes reelles (capacite, demande, réglementation) et comparer la prediction avec les donnees observees avant de decider.",
     "La reponse doit lier derivee et variation marginale, seuil optimal et verification des contraintes reelles.")],
C("Deriver, c'est mesurer une variation instantanee ; l'etude du signe de la derivee permet d'optimiser.",
  "f'(x) = taux de variation en x",
  "(x²)' = 2x · (ax+b)' = a · f'>0 croissant · f'<0 decroissant",
  "Derivee~Taux instantane~f'(x)~Tangente~Coefficient directeur~Pente locale~Extremum~f' nul et signe change~Optimisation~Chercher un maximum~Tableau de signe~Variations",
  "Exprimer la grandeur en fonction d'une variable|Deriver l'expression|Resoudre f'(x)=0|Etudier le signe de la derivee|Verifier les contraintes du probleme",
  "Oublier le changement de signe|Accepter une solution hors domaine|Confondre f et f'|Ne pas verifier le resultat par un calcul direct",
  "R(p)~-2p²+120p~R'(p)~-4p+120~Prix optimal~30 euros~Recette max~1800 euros",
  "Derivee positive~Fonction croissante~Derivee negative~Fonction decroissante",
  "Extremum local~Changement de signe~Maximum global~Comparer les bornes"))

# ============================================================ MA3
add("MA3", "Statistiques descriptives et probabilités", "Maths", ["1re"],
S("Une statistique descriptive resume un ensemble de donnees par des indicateurs et des graphiques."
  "|Un effectif designe le nombre d'occurrences d'une valeur ; le total des effectifs donne la taille de la serie."
  "|La moyenne est la somme des valeurs divisee par l'effectif total : elle est sensible aux valeurs extremes."
  "|La mediane est la valeur qui partage la serie ordonnee en deux moities ; elle resiste mieux aux outliers que la moyenne."
  "|L'etendue attire la difference entre la valeur maximale et la valeur minimale : elle mesure la dispersion brute."
  "|L'ecart-type measure la dispersion autour de la moyenne : plus il est faible, plus les donnees sont concentrees."
  "|Un histogramme represente des effectifs ou des frequences par classes ; un diagramme circulaire represente des parts d'un tout."
  "|Une frequence est le rapport entre un effectif et l'effectif total ; exprimee en pourcentage, elle se note p × 100."
  "|Une experience aleatoire a des resultats incertains ; l'univers des issues regroupe toutes les issues possibles."
  "|La probabilite d'un evenement est un nombre entre 0 et 1 ; la somme des probabilites de toutes les issues disjointes vaut 1."
  "|Si toutes les issues sont equiprobables, P(A) = nombre d'issues favorables / nombre total d'issues."
  "|En hôtellerie, ces outils servent a analyser le taux d'occupation, la duree moyenne de sejour ou la distribution des notes clients."),
[QC("Quel indicateur est le moins sensible aux valeurs extremes ?", "La moyenne~La mediane~L'ecart-type~L'etendue", 1,
     "La mediane depend du rang des valeurs, pas de leur ecart extrem."),
 QC("Comment calculer une moyenne ?", "Maximum moins minimum~Somme des valeurs divisée par l'effectif~Valeur centrale ordonnee~Somme des frequences", 1,
     "La moyenne est la somme des valeurs divisée par le nombre de valeurs."),
 QC("Que represente une frequence de 0,25 ?", "25 issues~25 % de l'effectif total~Une moyenne de 25~Un ecart de 25", 1,
     "Une frequence de 0,25 correspond a une proportion de 25 pour cent."),
 QC("Quelle probabilite est impossible ?", "0~0,5~1~1,3", 3,
     "Une probabilite appartient toujours a l'intervalle [0 ; 1]."),
 QC("Dans une experience a 8 issues equiprobables, 2 issues sont favorables. Quelle est la probabilite ?", "0,25~0,5~2~8", 0,
     "P = 2/8 = 0,25."),
 QC("Quel graphique represente des parts d'un tout ?", "Histogramme~Diagramme circulaire~Nuage de points~Courbe", 1,
     "Le diagramme circulaire (camembert) montre la repartition en pourcentages."),
 QT("Un hotel a 40 chambres et 28 sont occupees une nuit. Calculer le taux d'occupation et expliquer son interet.",
     "Le taux d'occupation est le rapport entre le nombre de chambres occupees et la capacite totale : 28 / 40 = 0,7, soit 70 %. Cet indicateur mesure l'utilisation du potentiel de l'etablissement. Il se compare a une periode precedeante, a un objectif budgetaire ou a la moyenne du secteur. Un taux de 70 % peut etre satisfaisant hors saison et insuffisant en haute saison : l'interpretation depend du contexte. On peut le complementer par le revenu par chambre disponible et par le prix moyen, car un fort taux avec des prix trop bas ne garantit pas la rentabilite.",
     "On attend 28/40 = 0,7 = 70 %, puis une interpretation contextualisee et des indicateurs complementaires."),
 QT("Une enquete de satisfaction porte sur 200 clients : 120 sont tres satisfaits, 50 satisfaits, 30 insatisfaits. Donner les frequences et commenter.",
     "Les frequences sont : tres satisfaits 120/200 = 0,6 soit 60 % ; satisfaits 50/200 = 0,25 soit 25 % ; insatisfaits 30/200 = 0,15 soit 15 %. La somme vaut 1, ce qui verifie le calcul. La proportion de clients satisfaits ou tres satisfaits atteint 85 %, ce qui est globalement positif, mais 15 % de clients insatisfaits representent 30 personnes a interroger : leur avis peut réveler un defaut precis du service. Une moyenne de notes ne suffirait pas a detecter ce noyau de mécontentement, d'ou l'interet de la distribution complete et du commentaire qualitatif.",
     "On attend les trois frequences, leur somme et une interpretation nuancee.")],
C("Les statistiques decrivent, les probabilites anticipent : dans les deux cas, le denominateur et le contexte commandent l'interpretation.",
  "Moyenne = somme / effectif · frequence = effectif / total",
  "P(A) = issues favorables / issues possibles (equiprobables)",
  "Moyenne~Somme sur effectif~Sensible aux extremes~Mediane~Valeur centrale~Robuste~Ecart-type~Dispersion autour de la moyenne~Probabilite~Entre 0 et 1~Frequence~Effectif sur total",
  "Nettoyer et trier les donnees|Choisir indicateurs et graphiques|Calculer moyenne et dispersion|Calculer les frequences|Interpreter dans le contexte",
  "Confondre moyenne et mediane|Oublier de convertir en pourcentage|Utiliser un graphique inadapte|Donner une probabilite superieure a 1",
  "40 chambres~Capacite~28 occupees~Taux 70 %~200 clients~Effectif total~15 %~Insatisfaits",
  "Moyenne~Sensible aux valeurs extremes~Mediane~Fondee sur le rang",
  "Statistique~Decrit des donnees~Probabilite~Anticipe un evenement"))

# ============================================================ MA4
add("MA4", "Suites numériques et intérêts composés", "Maths", ["Terminale"],
S("Une suite est une liste de nombres indexes par les entiers naturels : u0, u1, u2, etc."
  "|Une suite arithmetique ajoute une raison r constante a chaque terme : u(n+1) = u(n) + r et u(n) = u0 + nr."
  "|Une suite geometrique multiplie chaque terme par une raison q constante : u(n+1) = q × u(n) et u(n) = u0 × q^n."
  "|Le premier terme u0 et la raison suffisent a definir entierement une suite arithmetique ou geometrique."
  "|Une suite arithmetique augmente lineairement : sa representation graphique aligne les points sur une droite."
  "|Une suite geometrique augmente ou diminue de facon exponentielle quand la raison est superieure ou inferieure a 1."
  "|La somme des termes d'une suite arithmetique entre 0 et n vaut (n+1) × (u0 + u(n)) / 2."
  "|La somme des termes d'une suite geometrique de raison q differente de 1 vaut u0 × (1 - q^(n+1)) / (1 - q)."
  "|Les interets composes capitalisent les interets : le capital de depart et les interets acquites produisent a leur tour des interets."
  "|Un capital C place a un taux annuel t devient C × (1 + t)^n apres n annees : c'est une suite geometrique de raison 1 + t."
  "|Le taux effectif annuel tient compte de la capitalisation : avec des versements mensuels, on utilise un taux mensuel et 12 periodes par an."
  "|En gestion hoteliere, les suites modelisent un plan d'amortissement, une evolution de prix ou la croissance d'un fonds de roulement."),
[QC("Dans une suite arithmetique de raison 3, comment passe-t-on d'un terme au suivant ?", "On multiplie par 3~On ajoute 3~On divise par 3~On eleve au carre", 1,
     "La raison arithmetique s'ajoute a chaque terme."),
 QC("Quelle est la formule d'une suite geometrique ?", "u(n) = u0 + nq~u(n) = u0 × q^n~u(n) = q × n~u(n) = u0 + q", 1,
     "La raison geometrique q est elevee a la puissance n."),
 QC("Un capital de 1000 € a 5 % pendant 2 ans devient...", "1050 €~1100 €~1102,50 €~1005 €", 2,
     "1000 × 1,05² = 1102,50 € ; les interets de la premiere annee rapportent aussi des interets."),
 QC("Quelle suite modele des interets composes ?", "Arithmetique~Geometrique~Constant~Oscillante", 1,
     "La capitalisation donne une progression geometrique de raison 1 + t."),
 QC("Quand une suite geometrique decroit-elle ?", "Quand q > 1~Quand 0 < q < 1~Quand q = 1~Quand q est negatif quel que soit n", 1,
     "Une raison comprise entre 0 et 1 donne une decroissance exponentielle."),
 QT("Un hotel investit 20 000 € et la valeur de l'equipement diminue de 10 % par an. Quelle sera sa valeur apres 3 ans ?",
     "La valeur initiale est 20 000 € et la raison de la suite geometrique est 0,9 puisque l'equipement conserve 90 % de sa valeur chaque annee. Apres 3 ans, V(3) = 20 000 × 0,9³ = 20 000 × 0,729 = 14 580 €. La perte cumulee vaut donc 5 420 €. Il s'agit d'un amortissement geometrique, different de l'amortissement lineaire ou la meme somme serait deduite chaque annee. Ce modele est souvent utilise en comptabilite pour representer une decroissance de valeur proportionnelle a la valeur courante.",
     "On attend la raison 0,9, le calcul 14 580 € et la distinction avec un amortissement lineaire."),
 QT("Expliquer la difference entre interets simples et interets composes sur un exemple de 3 ans.",
     "Avec des interets simples, le capital de depart seul produit des interets : 1000 € a 5 % donnent 50 € par an, soit 150 € apres 3 ans et un capital final de 1150 €. Avec des interets composes, les interets de chaque annee s'ajoutent au capital et produisent a leur tour des interets : 1000 × 1,05³ = 1157,63 €, soit 7,63 € de plus. L'ecart parait faible sur trois ans mais croit avec la duree, car la progression est exponentielle. C'est pourquoi le taux effectif annuel est superieur au taux nominal quand la capitalisation est infrannuelle, et pourquoi l'epargne a long terme privilegie la capitalisation.",
     "On attend le calcul comparatif sur 3 ans et l'explication du mecanisme de capitalisation.")],
C("Une suite arithmetique ajoute la meme valeur, une suite geometrique multiplie : interets composes et amortissements sont geometriques.",
  "u(n) = u0 + nr ou u(n) = u0 × q^n",
  "Capital final = C × (1 + t)^n",
  "Suite arithmetique~Raison ajoutee~u0 + nr~Suite geometrique~Raison multipliee~u0 × q^n~Interets composes~Capitalisation~Amortissement~Perte de valeur~Taux effectif~Tannuel reel",
  "Identifier le premier terme|Determiner la raison|Choisir le type de suite|Calculer le terme cherche|Verifier l'ordre de grandeur",
  "Confondre raison additive et multiplicative|Utiliser n au lieu de n+1|Oublier de convertir le pourcentage|Ignorer la periodicite des versements",
  "20 000 €~Valeur initiale~0,9~Raison~3 ans~Periode~14 580 €~Valeur finale~5 420 €~Amortissement cumule",
  "Interets simples~Interets sur le capital initial~Interets composes~Interets sur capital et interets",
  "Suite arithmetique~Progression lineaire~Suite geometrique~Progression exponentielle"))

# ============================================================ HG1
add("HG1", "Mondialisation et mobilités touristiques", "Histoire-Géographie", ["1re", "Terminale"],
S("La mondialisation est l'intensification des echanges de biens, de capitaux, d'informations et de personnes a l'echelle planetaire."
  "|Elle s'appuie sur des reseaux de transport et de communication qui reduisent la distance-temps entre les lieux."
  "|Le tourisme international est l'un des principaux fluxes de personnes : il contribue aux recettes d'exportation de nombreux Etats."
  "|Les mobilites touristiques sont inegalement reparties : les pays du Nord concentrent l'essentiel des departs et des arrivees."
  "|Les pôles touristiques mondiaux sont souvent des metropoles, des littoraux amenages ou des sites patrimoniaux inscrits au patrimoine mondial."
  "|La specialisation touristique d'un territoire peut creer des emplois mais aussi une dependance a la demande exterieure."
  "|Les grandes entreprises de l'hotellerie et du transport sont des acteurs multinationaux qui organisent des chaines de valeur globalisees."
  "|Les plateformes numeriques de reservation ont modifie les equilibres du marche en donnant plus de pouvoir aux distributeurs."
  "|Les crises sanitaires, economiques ou geopolitiques montrent la vulnerabilite d'un secteur tres dependant des deplacements."
  "|Le tourisme de masse exerce des pressions sur les ressources locales : eau, sol, biodiversite et patrimoine."
  "|Le developpement d'un tourisme plus durable cherche a concilier attractivite economique, respect des habitants et protection de l'environnement."
  "|L'etude d'un territoire touristique combine analyse des fluxes, des acteurs, des paysages et des politiques publiques."),
[QC("Qu'est-ce que la mondialisation ?", "Le commerce d'un seul pays~L'intensification des echanges a l'echelle planetaire~La fermeture des frontieres~Un reseau de transports locaux", 1,
     "La mondialisation connecte les economies et les societes a l'echelle du globe."),
 QC("Quel acteur a fortement transforme la reservation d'hotels ?", "La poste~Les plateformes numeriques~Le chemin de fer~Les municipaliites", 1,
     "Les plateformes en ligne ont modifie la distribution et le rapport de force avec les hebergeurs."),
 QC("Quel risque presente une forte specialisation touristique ?", "Une baisse des prix~Une dependance a la demande exterieure~Une hausse de l'emploi~Une meilleure resilience", 1,
     "Une economie mono-active est sensible aux crises qui touchent le tourisme."),
 QC("Quel patrimoine beneficie d'une reconnaissance internationale ?", "Les seuls monuments prives~Les biens inscrits au patrimoine mondial~Les seuls musees~Les routes nationales", 1,
     "L'UNESCO inscrit des biens culturels et naturels sur la liste du patrimoine mondial."),
 QC("Quelle ressource est particulierement sollicitee par le tourisme de masse ?", "Le sable~L'eau~Le gaz~Le fer", 1,
     "La consommation d'eau par touriste est un enjeu majeur dans les regions arides."),
 QT("Expliquer pourquoi le tourisme est a la fois une chance et une vulnerabilite pour un territoire.",
     "Le tourisme apporte des recettes, des emplois directs et indirects, des infrastructures et une visibilite internationale. Il peut financer la preservation du patrimoine et faire vivre des commerces locaux. Mais il rend le territoire dependant d'une demande exterieure sensible aux crises : une pandemie, une crise economique ou un conflit peuvent vider les hotels et les restaurants. La concentration des activites peut aussi provoquer une hausse des prix immobilier, une pression sur les ressources et une perte d'identite locale. Une politique durable cherche a diversifier l'economie, a repartir les flux dans le temps et dans l'espace et a associer les habitants aux decisions.",
     "On attend avantages economiques et sociaux, vulnerabilite aux crises et pistes de resilience."),
 QT("Comment analyser la carte des fluxes touristiques d'un pays ?",
     "On identifie d'abord les principaux pays emetteurs et receveurs, puis on mesure les volumes de touristes et les recettes associees. On observe les axes de circulation : liaisons aeriennes, corridors autoroutiers, liaisons maritimes et ferroviaires. On localise ensuite les pôles d'attraction, qu'ils soient naturels, patrimoniaux ou recreatifs, et on relie leur attractivite a la presence d'infrastructures. Enfin, on compare avec les donnees de frequentation et d'hebergement pour mesurer le poids du tourisme dans l'economie locale et les inegalites territoriales qu'il produit.",
     "On attend lecture des flux, des axes, des pôles et mise en relation avec les donnees economiques.")],
C("Le tourisme est un systeme de fluxes : il relie des territoires, des acteurs et des ressources a des echelles differentes.",
  "Tourisme = fluxes de personnes + infrastructures + acteurs",
  "Mondialisation · specialisation · vulnerabilite · durabilite",
  "Mondialisation~Echanges planeta~ flux~Reseaux~Transport et numerique~Pole touristique~Site attractif~Flux~Deplacements de personnes~Dependance~Risque de crise~Durabilite~Conciliation des usages",
  "Repérer les flux et les axes|Localiser les pôles d'attraction|Identifier les acteurs publics et prives|Evaluer les effets economiques et sociaux|Proposer des pistes durables",
  "Voir le tourisme comme uniquement positif|Confondre flux et stock|Ignorer les acteurs locaux|Oublier les crises et la saisonnalite",
  "UNESCO~Patrimoine mondial~Plateforme~Reservation en ligne~Saisonnalite~Variation des flux~Eau~Ressource critique",
  "Pays du Nord~Principaux emetteurs~Pays du Sud~Recepteurs et investissements",
  "Chance~Emplois et recettes~Vulnerabilite~Dependance aux crises"))

# ============================================================ HG2
add("HG2", "Territoires, villes et aménagement touristique", "Histoire-Géographie", ["1re"],
S("Un territoire est un espace approprie et organise par des societes, a partir de ressources et de representations."
  "|Un paysage est la partie visible d'un territoire : il resulte de l'action des hommes et des processus naturels."
  "|La ville concentre populations, activites et fonctions de commandement ; elle structure les territories autour d'elle."
  "|L'amenagement consiste a organiser l'espace pour repondre a des besoins : logement, transport, activite economique et loisirs."
  "|Les acteurs de l'amenagement sont l'Etat, les collectivites territoriales, les entreprises et les habitants."
  "|Les documents de planification, comme le plan local d'urbanisme, fixent les regles d'occupation des sols et les zones constructibles."
  "|La gentrification designe la transformation d'un quartier populaire par l'arrivee de populations plus aisees et la hausse des prix."
  "|La periurbanisation est l'etirement de la ville vers les communes peripheriques, souvent au detriment des espaces agricoles."
  "|Les stations balneaires et les stations de montagne sont des territoires specialises, amenages pour accueillir des touristes."
  "|La saisonnalite concerne la concentration de l'activite sur quelques mois, avec des effets sur l'emploi et les infrastructures."
  "|La mise en valeur d'un patrimoine peut servir de projet de territoire, a condition d'eviter la muséification et l'eviction des habitants."
  "|L'analyse d'un territoire articule echelle locale, regional et nationale, et croise donnees statistiques, cartes et observations de terrain."),
[QC("Qu'est-ce qu'un territoire en geographie ?", "Un simple paysage naturel~Un espace approprie et organise~Une carte administrative seule~Une region climatique", 1,
     "Le territoire est un espace vécu, aménagé et porteur de representations."),
 QC("Quel document fixe les regles d'urbanisme d'une commune ?", "Le plan local d'urbanisme~Le code de la route~Le budget de la region~Le cadastre national", 0,
     "Le PLU determine les zones constructibles et les regles d'occupation des sols."),
 QC("Que designe la periurbanisation ?", "Le depart des habitants de la ville~L'extension de la ville en peripherie~La renovation du centre~La creation d'un port", 1,
     "La periurbanisation etale l'habitat et les activites hors du centre-ville."),
 QC("Quel effet de la saisonnalite sur l'emploi touristique ?", "Une stabilite totale~Des pics d'activite et des periodes creuses~Une hausse permanente~Une disparition des contrats", 1,
     "L'activite concentree sur quelques mois rend l'emploi saisonnier et précaire."),
 QT("Expliquer comment un projet de renovation d'un quartier peut eviter la gentrification.",
     "Un projet de renovation doit d'abord associer les habitants et les commerces existants a la definition des besoins. Il peut maintenir des logements abordables, encadrer les loyers, proteger les activites de proximite et phaser les travaux pour eviter une hausse brutale des prix. La mobilisation de financements publics et de conventions avec les proprietaires permet de conserver une mixite sociale. Dans un quartier touristique, il faut aussi veiller a ce que les logements ne soient pas transformes en hebergements de courte duree au detriment des residents. Enfin, le suivi d'indicateurs sociaux apres travaux verifie que les populations initiales restent sur place.",
     "On attend participation, mixite sociale, protection des activites et suivi apres amenagement."),
 QT("Comment analyser le paysage d'une station balneaire ?",
     "On decrit d'abord les elements naturels : littoral, plage, dunes, relief et vegetation. On repere ensuite les elements construits : hotels, residences, promenades, port et equipements de loisirs. On lit les usages en observant la repartition entre touristes et habitants, les mobilites et les espaces publics. On s'interroge enfin sur les tensions : artificialisation des sols, érosion du littoral, saturation en haute saison et accessibilite du bord de mer. L'analyse articule description, acteurs et enjeux d'amenagement, a differentes echelles de temps : paysage herite, paysage en projet et paysage subi.",
     "On attend description naturelle et construite, usages, tensions et enjeux d'amenagement.")],
C("Un territoire se lit comme un paysage construit par des acteurs et des regles, a plusieurs echelles.",
  "Territoire = espace + ressources + acteurs + projet",
  "PLU · periurbanisation · gentrification · saisonnalite",
  "Territoire~Espace approprie~Paysage~Partie visible~PLU~Regles d'urbanisme~Periurbanisation~Etalement urbain~Gentrification~Hausse des prix~Saisonnalite~Pics d'activite",
  "Observer le paysage|Identifier les acteurs et les regles|Lire les usages et les fluxes|Repérer les tensions|Proposer un projet d'amenagement",
  "Confondre paysage et territoire|Ignorer les habitants|Ne pas preciser l'echelle|Oublier l'evolution historique",
  "Station balneaire~Littoral amenage~PLU~Zones constructibles~Haute saison~Pression sur les equ ipements~Patrimoine~Projet de territoire",
  "Paysage~Ce qui se voit~Territoire~Espace vecu et organise",
  "Gentrification~Transformation sociale~Periurbanisation~Etalement spatial"))

# ============================================================ HG3
add("HG3", "Démographie, développement et inégalités", "Histoire-Géographie", ["Terminale"],
S("La demographie etudie la taille, la structure et l'evolution des populations a partir des naissances, des deces et des migrations."
  "|La croissance demographique depend de l'accroissement naturel et du solde migratoire."
  "|L'indice de fecondite est le nombre moyen d'enfants par femme ; il determine en grande partie le renouvellement des generations."
  "|L'espérance de vie a la naissance est un indicateur de l'etat sanitaire et des conditions de vie d'une population."
  "|La transition demographique decrit le passage d'une forte natalite et mortalite a une faible natalite et mortalite."
  "|Le vieillissement de la population resulte de la baisse de la fecondite et de l'allongement de la vie."
  "|Le developpement englobe la croissance economique, mais aussi la reduction de la pauvrete, l'acces aux services et la qualité de vie."
  "|Le produit interieur brut par habitant mesure la richesse moyenne, mais il ne dit rien de sa repartition ni des externalites."
  "|L'indice de developpement humain combine revenu, sante et education pour comparer les pays."
  "|Les inegalites se mesurent entre pays, entre regions et entre individus : elles touchent le revenu, l'acces au logement, a la sante et a l'emploi."
  "|Les migrations sont souvent le fait de populations jeunes et contribuent au renouvellement de la main-d'oeuvre dans les pays d'accueil."
  "|Dans l'hotellerie-restauration, les flux de main-d'oeuvre et les inegalites salariales sont des enjeux sociaux et de gestion importants."),
[QC("Que mesure l'indice de fecondite ?", "Le nombre de deces~Le nombre moyen d'enfants par femme~L'espérance de vie~Le solde migratoire", 1,
     "L'indice de fecondite est le nombre moyen d'enfants par femme en age de procreer."),
 QC("Comment appelle-t-on la difference entre naissances et deces ?", "Solde migratoire~Accroissement naturel~Transition demographique~Taux d'activite", 1,
     "L'accroissement naturel = naissances moins deces."),
 QC("Quel indicateur combine revenu, sante et education ?", "Le PIB~L'IDH~Le taux de chomage~La population active", 1,
     "L'indice de developpement humain (IDH) est un indicateur composite."),
 QC("Quelle limite du PIB par habitant ?", "Il est toujours faux~Il ignore la repartition des richesses~Il ne concerne que les services~Il ne peut pas etre compare", 1,
     "Le PIB par habitant est une moyenne qui masque les inegalites et les effets externes."),
 QC("Quel phenomene resulte de la baisse de fecondite et de l'allongement de la vie ?", "La transition demographique~Le vieillissement~La natalite~L'exode rural", 1,
     "Ces deux evolutions conduisent a une part croissante de personnes agees."),
 QT("Expliquer pourquoi un pays peut avoir une croissance economique sans reduction des inegalites.",
     "La croissance mesure l'augmentation de la production totale, pas sa distribution. Si les richesse supplementaires benefit principalement aux detenteurs de capitaux ou aux regions deja dynamiques, la moyenne augmente alors que la situation des plus pauvres stagne. Les inegalites peuvent aussi toucher l'acces aux services : une hausse du PIB ne garantit ni l'acces au logement, ni la qualite de l'ecole ou des soins. De plus, la croissance peut generer des couts environnementaux qui affectent d'abord les populations les plus vulnerables. Il faut donc completer le PIB par des indicateurs de repartition, de pauvrete et de developpement humain, et par des politiques de redistribution et d'acces aux services publics.",
     "On attend distinction croissance et developpement, role de la repartition et indicateurs complementaires."),
 QT("Quel est l'interet d'etudier la pyramide des ages d'un territoire ?",
     "La pyramide des ages montre la repartition de la population par age et par sexe. Elle revele une population jeune, en croissance, ou vieillissante, avec des consequences sur les besoins en ecole, en logements, en sante et en retraites. Pour un employeur du tourisme, elle indique le volume de main-d'oeuvre disponible et les besoins de formation. Comparee a une pyramide anterieure, elle montre l'effet des variations de natalite et des migrations. Elle doit neanmoins etre completee par le taux d'activite, la situation des femmes sur le marche du travail et les niveaux de qualification.",
     "On attend lecture de la structure par age, consequences socio-economiques et limites de l'indicateur.")],
C("Croissance, demographie et developpement sont lies mais distincts : les indicateurs doivent etre croises et contextues.",
  "Developpement = croissance + equitable + services",
  "IDH = revenu + sante + education",
  "Demographie~Etude des populations~Fecondite~Enfants par femme~IDH~Indicateur composite~PIB~Richesse moyenne~Inegalites~Repartition inegale~Vieillissement~Part des ages avances",
  "Choisir l'indicateur adapte|Lire la valeur et son unite|Comparer dans le temps et entre pays|Croiser avec d'autres donnees|Interpret avec le contexte",
  "Identifier croissance et developpement|Confondre moyenne et repartition|Ignorer les migrations|Utiliser un seul indicateur",
  "IDH~Trois dimensions~PIB par habitant~Moyenne~Pyramide des ages~Structure~Migration~Solde et main-d'oeuvre",
  "Croissance~Production en hausse~Developpement~Qualite de vie et equite",
  "Taux de natalite~Naissances~Taux de mortalite~Deces"))

# ============================================================ AN1
add("AN1", "Grammaire et compréhension de l'anglais", "Anglais", ["1re"],
S("The simple present describes habits and facts: « the hotel opens at seven »."
  "|The present continuous describes an action in progress: « I am checking in the guests »."
  "|The simple past narrates completed actions with a definite time: « we received the booking yesterday »."
  "|The present perfect links a past action to the present: « I have already sent the confirmation »."
  "|The future with « will » expresses a decision made at the moment or a prediction."
  "|Articles a, an and the depend on whether the noun is countable, specific or already known."
  "|Countable nouns take a plural form; uncountable nouns such as information or advice never take « a »."
  "|Comparatives use « -er than » for short adjectives and « more ... than » for long adjectives."
  "|Modals such as can, must, should and may express ability, obligation, advice and permission."
  "|The conditional form « would » softens a request and is standard in polite customer service."
  "|Reading comprehension requires identifying the main idea, key details, the writer's purpose and the tone."
  "|In the technological baccalaureate, English also appears through ETLV, where technical vocabulary is practised in a professional situation."),
[QC("Which tense describes an action in progress ?", "Simple present~Present continuous~Simple past~Present perfect", 1,
     "The present continuous (be + -ing) describes an action happening now."),
 QC("« I have already sent the email » uses...", "Simple past~Present perfect~Future~Past continuous", 1,
     "The present perfect connects a past action to the present with already, yet or ever."),
 QC("Which noun is uncountable ?", "Room~Guest~Information~Booking", 2,
     "Information is uncountable: we say « some information », not « an information »."),
 QC("How do you form a polite request ?", "Give me the bill~Would you give me the bill?~You give the bill~Giving the bill", 1,
     "« Would you... » is the standard polite form in service encounters."),
 QC("Which modal expresses obligation ?", "Can~Must~May~Might", 1,
     "Must expresses a strong obligation; should expresses advice."),
 QC("What does a reading comprehension question on the writer's purpose ask ?", "The writer's age~Why the text was written~The number of words~The date of publication", 1,
     "Purpose means the intention: to inform, persuade, complain or entertain."),
 QT("Correct the mistakes: « I am working here since 2022 and I have saw many guests. »",
     "The first sentence needs the present perfect, because « since » links a past starting point to the present: « I have worked here since 2022 ». The second sentence needs the past participle of « see », which is « seen »: « I have seen many guests ». The corrected version is: « I have worked here since 2022 and I have seen many guests. » The present continuous cannot be used with « since » for a state that began in the past and continues now.",
     "On attend have worked avec since et have seen comme participe passe."),
 QT("How do you identify the main idea of a short text ?",
     "First read the title, the subtitle and the first and last sentences of each paragraph, which often carry the topic. Then look for repeated words and ideas: repetition signals what the writer wants to emphasise. Ask what question the text answers and distinguish the main point from the examples and details that support it. Finally, check your hypothesis against the whole text and express it in one short sentence, without adding personal opinion. In an exam, a good main-idea answer covers the entire passage, not only one paragraph.",
     "On attend lecture du titre et des phrases-cles, repérage des repetitions et formulation concise.")],
C("English grammar gives the tools to describe situations precisely; reading comprehension gives the method to extract meaning.",
  "Present perfect = have/has + past participle",
  "Would = polite request · must = obligation · uncountable = no article a",
  "Simple present~Habits and facts~Works~Present continuous~Action in progress~Is working~Present perfect~Past linked to now~Have sent~Modal~Attitude of the speaker~Would, must~Main idea~Central message",
  "Read the title and the first sentences|Identify repeated words|Find the tense and the time markers|Answer with a full sentence|Check the answer against the text",
  "Use present continuous with since|Add « a » before uncountable nouns|Translate word for word|Answer with a single word",
  "Since 2022~Present perfect~Already~Present perfect~Would you~Polite request~Information~Uncountable",
  "Simple past~Finished time~Yesterday~Present perfect~Link with now~Already",
  "Countable~A room, two rooms~Uncountable~Some advice"))

# ============================================================ AN2
add("AN2", "Expression écrite et orale en anglais", "Anglais", ["1re", "Terminale"],
S("Written expression in the baccalaureate asks for a structured text: an introduction, two or three paragraphs and a conclusion."
  "|A discursive essay presents arguments in favour and against, then gives a reasoned personal opinion."
  "|Topic sentences introduce each paragraph and announce the idea that will be developed."
  "|Linking words organise the text: « first », « however », « therefore », « in addition » and « finally »."
  "|Examples and precise details support an argument and make the essay more convincing."
  "|The conclusion answers the question posed in the introduction and may open the debate."
  "|In oral expression, candidates summarise a document, give their opinion and answer the examiner's questions."
  "|A clear structure and signposting help the listener follow the speech: « I will first present..., then I will give my view »."
  "|Pronunciation, intonation and fluency contribute to intelligibility even when the grammar is imperfect."
  "|The ETLV class practises professional situations: welcoming a guest, describing a menu or explaining a service."
  "|Technical vocabulary should be used accurately: check-in, booking, room service, bill, deposit, available."
  "|Preparation relies on useful phrases learned by heart and on regular practice with short timed tasks."),
[QC("What is the role of a topic sentence ?", "To end the essay~To introduce the idea of a paragraph~To give the date~To replace the conclusion", 1,
     "The topic sentence states the main idea of the paragraph that follows."),
 QC("Which linking word introduces a contrast ?", "Therefore~However~In addition~First", 1,
     "However signals a contrast; therefore signals a consequence."),
 QC("What should a conclusion do ?", "Introduce a new argument~Answer the question and open the debate~Repeat the examples~Ignore the introduction", 1,
     "The conclusion answers the initial question and can widen the topic."),
 QC("Which phrase is a professional check-in phrase ?", "« Have a nice meal »~« Could I have your passport, please? »~« It is raining »~« I like music »", 1,
     "Asking for the passport is part of the check-in procedure."),
 QC("What does fluency mean in oral expression ?", "Perfect grammar only~Speaking smoothly and intelligibly~Reading very fast~Using no pauses", 1,
     "Fluency is the ability to speak continuously and be understood."),
 QT("Write a short paragraph arguing that online reviews matter for a hotel, with two arguments.",
     "Online reviews matter first because they influence the booking decision: most travellers read several opinions before choosing a hotel, and a good rating can increase occupancy. Secondly, reviews give the management precise feedback about the service: repeated comments about slow check-in or noisy rooms show where improvements are needed. Of course, reviews can be unfair or exaggerated, so the manager should answer politely and look for trends rather than react to a single complaint. Overall, online reputation has become part of the hotel's commercial capital and must be monitored every day.",
     "On attend deux arguments clairs, des connecteurs et une conclusion nuancee."),
 QT("How should you prepare an oral presentation of a document in English?",
     "Prepare a short plan with three parts: presentation of the document (source, date, type, topic), summary of its main ideas, then personal comment. Learn useful phrases to introduce each part and to express an opinion: « the document deals with... », « in my view... ». Rehearse aloud with a timer to work on fluency, pronunciation and pauses. Anticipate questions the examiner may ask about the theme and prepare one example for each argument. On the day, speak clearly, look at the examiner, and use simple words rather than complicated sentences you cannot control.",
     "On attend plan, phrases utiles, repetition a voix haute et anticipation des questions.")],
C("A good answer in English is structured, supported by examples and delivered clearly.",
  "Essay = introduction + arguments + conclusion",
  "However = contrast · therefore = consequence · would = politeness",
  "Essay~Structured text~Introduction~Question and plan~Topic sentence~Idea of a paragraph~Linking word~However, therefore~Oral~Summary and opinion~ETLV~Professional vocabulary",
  "Analyse the question|Prepare a two or three point plan|Write topic sentences|Add examples and linkers|Rehearse and time the oral",
  "Write without a plan|Use a linker wrongly|Give an opinion with no reason|Read the oral notes mechanically",
  "Check-in~Accueil et enregistrement~Booking~Reservation~Bill~Facture~Review~Avis client~Would you~Formule polie",
  "For~Argument favorable~Against~Argument defavorable",
  "Written~Organised paragraphs~Spoken~Intonation and fluency"))

# ============================================================ EM1
add("EM1", "Institutions et fonctionnement de la République", "EMC", ["1re"],
S("La France est une Republique : le chef de l'Etat est elu et le pouvoir ne se transmet pas hereditairement."
  "|La Constitution de 1958 organise les institutions de la Ve Republique et definit les pouvoirs publics."
  "|Le President de la Republique est elu au suffrage universel direct pour un mandat de cinq ans."
  "|Le Gouvernement, dirige par le Premier ministre, conduit la politique de la nation et est responsable devant le Parlement."
  "|Le Parlement est bicameral : il comprend l'Assemblee nationale et le Senat, qui votent la loi et controlent l'action du Gouvernement."
  "|La loi est vote par le Parlement puis promulguee par le President ; elle peut etre examinee par le Conseil constitutionnel."
  "|Le Conseil constitutionnel verifie la conformite des lois a la Constitution et protege les droits fondamentaux."
  "|Le Conseil d'Etat conseille le Gouvernement et juge les recours contre les actes administratifs."
  "|La Cour de cassation est la juridiction supreme de l'ordre judiciaire ; elle verifie l'application du droit."
  "|La separation des pouvoirs repose sur l'equilibre entre le pouvoir executif, le pouvoir legislatif et le pouvoir judiciaire."
  "|Les collectivites territoriales — communes, departements et regions — disposent d'autonomie pour gestion les affaires locales."
  "|L'Union europeenne est une organisation d'Etats qui edicte des regles communes dans de nombreux domaines, dont l'hygiene alimentaire et le tourisme."),
[QC("Combien de temps dure le mandat du President de la Republique ?", "Trois ans~Quatre ans~Cinq ans~Six ans", 2,
     "Depuis 2000, le mandat presidentiel dure cinq ans."),
 QC("Quel organe vote la loi ?", "Le Conseil d'Etat~Le Parlement~La Cour de cassation~Le Gouvernement seul", 1,
     "Le Parlement, compose de l'Assemblee nationale et du Senat, vote la loi."),
 QC("Qui verifie la conformite d'une loi a la Constitution ?", "Le Conseil constitutionnel~Le Prefet~Le Tribunal de commerce~Le Maire", 0,
     "Le Conseil constitutionnel exerce un controle de constitutionnalite."),
 QC("Quelles sont les deux chambres du Parlement francais ?", "Assemblee nationale et Senat~Senat et Conseil d'Etat~Cour de cassation et Conseil constitutionnel~Assemblee et Gouvernement", 0,
     "Le Parlement est bicameral : Assemblee nationale et Senat."),
 QC("Quelle juridiction juge les recours contre les actes administratifs ?", "La Cour de cassation~Le Conseil d'Etat~Le Tribunal correctionnel~La Cour d'appel", 1,
     "Le Conseil d'Etat est la juridiction supreme de l'ordre administratif."),
 QT("Expliquer la separation des pouvoirs et son interet pour la democratie.",
     "La separation des pouvoirs repartit les fonctions entre le pouvoir executif, qui applique les lois, le pouvoir legislatif, qui les vote, et le pouvoir judiciaire, qui les interprete et tranche les litiges. Aucun organe ne detient seul l'ensemble des pouvoirs : le Parlement peut controler le Gouvernement, le juge peut censurer une decision administrative, et le Conseil constitutionnel peut invalider une loi. Cette repartition limite l'arbitraire et protege les droits des citoyens. Elle ne supprime pas les interactions entre pouvoirs : la Ve Republique organise au contraire une cooperation sous l'autorite du President, avec des mecanismes d'equilibre comme la dissolution ou la motion de censure.",
     "On attend definition des trois pouvoirs, exemples de controles et nuance sur la cooperation."),
 QT("Quel est le role des collectivites territoriales dans la vie locale ?",
     "Les communes, les departements et les regions disposent de competences propres et d'un budget. La commune gere l'etat civil, les ecoles primaires, l'urbanisme et les services de proximite ; le departement intervient dans l'action sociale et les colleges ; la region conduit le developpement economique, la formation et les transports regionaux. Les collectivites public des services publics de proximite et peuvent soutenir le tourisme local par des actions de promotion ou des equipements. Leurs decisions sont prises par des assemblees elues et doivent respecter les lois nationales et les regles europeennes.",
     "On attend les niveaux, des competences concretes et le lien avec les services et le tourisme local.")],
C("Les institutions republicaines organisent les pouvoirs et garantissent les droits par des mecanismes de controle.",
  "Pouvoirs : executif, legislatif, judiciaire",
  "President 5 ans · Parlement bicameral · Conseil constitutionnel",
  "Republique~Chef de l'Etat elu~Constitution~Texte supreme~Parlement~Vote la loi~Executif~President et Gouvernement~Judiciaire~Juges et tribunaux~Collectivites~Communes, departements, regions",
  "Identifier l'institution concernee|Preciser son role et sa composition|Indiquer comment elle est designee|Montrer ses pouvoirs et ses limites|Citer un exemple d'action",
  "Confondre Parlement et Gouvernement|Oublier leSenat|Croire que le juge fait la loi|Ignorer le niveau europeen",
  "5 ans~Mandat presidentiel~Bicameral~Deux chambres~Ve Republique~Constitution de 1958~Union europeenne~Regles communes",
  "Conseil constitutionnel~Controle des lois~Conseil d'Etat~Justice administrative",
  "Executif~Applique~Legislatif~Vote~Judiciaire~Juge"))

# ============================================================ EM2
add("EM2", "Citoyenneté, engagement et laïcité", "EMC", ["1re", "Terminale"],
S("La citoyennete est le statut de la personne qui appartient a une communaute politique et dispose de droits et de devoirs."
  "|En France, la citoyennete s'acquiert par la naissance, la filiation, la naturalisation ou le mariage dans certaines conditions."
  "|Les droits civiques comprennent le droit de vote, l'eligibilite et l'acces a la fonction publique."
  "|Le suffrage universel direct permet aux citoyens majeurs d'elire leurs representants."
  "|L'abstention designe le fait de ne pas voter ; elle interroge la participation democratique et la representation."
  "|L'engagement citoyen peut prendre la forme d'un vote, d'une petition, d'une manifestation, d'un syndicat ou d'une association."
  "|La liberte d'expression est protegee par la Constitution et la Convention europeenne des droits de l'homme, mais elle connait des limites."
  "|La laicite garantit la liberte de conscience, l'egalite de tous devant la loi et la neutralite de l'Etat."
  "|La laicite ne signifie pas l'interdiction de toute religion : elle protege la liberte de croire ou de ne pas croire."
  "|Les agents publics sont tenus a la neutralite dans l'exercice de leurs fonctions, ce qui inclut les personnels des services publics."
  "|Les discriminations sont interdites par la loi : elles peuvent fonder une action en justice et des sanctions."
  "|Dans un etablissement touristique, le respect des convictions des clients et des collegues fait partie de la qualite de service et du droit du travail."),
[QC("Quel droit est typiquement civique ?", "Le droit de propriete~Le droit de vote~Le droit au travail~Le droit de se taire", 1,
     "Le droit de vote et l'eligibilite sont des droits civiques."),
 QC("Que garantit la laicite ?", "L'interdiction des religions~La liberte de conscience et l'egalite~La religion d'Etat~La neutralite des seuls citoyens", 1,
     "La laicite protege la liberte de croire ou de ne pas croire et impose la neutralite de l'Etat."),
 QC("Qui est tenu a la neutralite dans la fonction publique ?", "Tous les citoyens~Les agents publics en service~Les seuls enseignants~Les clients d'un service public", 1,
     "Les agents publics representent le service public et doivent etre neutres en fonction."),
 QC("Qu'est-ce que l'abstention ?", "Voter blanc~Ne pas se presenter au vote~Voter pour le vainqueur~Changer d'avis", 1,
     "L'abstention est l'absence de participation au scrutin."),
 QC("Quelle action est une forme d'engagement collectif ?", "Regarder les informations~Adherer a une association~Changer de chaine~Acheter un journal", 1,
     "L'adhesion a une association est une forme d'engagement citoyen."),
 QT("Distinguer liberte d'expression et limite de celle-ci.",
     "La liberte d'expression permet d'exprimer ses opinions, y compris des avis critiques envers le pouvoir. Elle est garantie par la Declaration des droits de l'homme et la Convention europeenne des droits de l'homme. Elle connait toutefois des limites fixees par la loi : la diffamation, l'injure publique, l'incitation a la haine, le negationnisme et l'atteinte a la vie privee sont reprehensibles. La liberte de la presse et la liberte d'opinion s'exercent donc dans le respect des droits d'autrui et de l'ordre public. Sur les reseaux sociaux, ces regles s'appliquent egalement, ce que les utilisateurs oublient parfois.",
     "On attend definition, fondements juridiques, limites et application au numerique."),
 QT("Comment la laicite s'applique-t-elle dans un service public d'accueil ?",
     "Dans un service public, la laicite impose la neutralite des agents : ils ne manifestent pas leurs convictions pendant le service et traitent tous les usagers de la meme maniere, quelle que soit leur religion ou leur absence de religion. Les usagers, eux, conservent leur liberte de conscience et peuvent porter des signes religieux, dans le respect de l'ordre public et des regles de securite. Concretement, un agent d'accueil ne commente pas les choix religieux d'un client, ne refuse pas un service et adapte les horaires ou les repas lorsque c'est possible et conforme au reglement. C'est une condition d'egalite et de qualite de l'accueil.",
     "On attend neutralite des agents, liberte des usagers et traduction concrete dans l'accueil.")],
C("Citoyennete, laicite et engagement fondent la vie democratique et le respect de la dignite de chacun.",
  "Laicite = liberte de conscience + egalite + neutralite de l'Etat",
  "Droits civiques : vote, eligibilite, fonction publique",
  "Citoyennete~Statut et appartenance~Droits civiques~Vote et eligibilite~Laicite~Neutralite de l'Etat~Expression~Liberte et limites~Engagement~Association, petition~Discrimination~Interdite par la loi",
  "Definir la notion|Identifier les textes de reference|Preciser les droits et les devoirs|Donner un exemple concret|Respecter les limites legales",
  "Confondre laicite et ateisme|Croire que la liberte d'expression est illimitee|Oublier les devoirs|Ignorer les sanctions contre les discriminations",
  "Neutralite~Agent public en service~Suffrage universel~Tous les majeurs~Association~Engagement collectif~Service public~Egalite de traitement",
  "Croyant~Liberte de croire~Non-croyant~Liberte de ne pas croire",
  "Droit~Ce que l'on peut exiger~Devoir~Ce que l'on doit respecter"))

# ============================================================ EM3
add("EM3", "Droits, devoirs et sécurité des personnes", "EMC", ["1re", "Terminale"],
S("La dignite humaine est un principe fondamental : la loi protege la personne contre les traitements degradants et les discriminations."
  "|Le droit a la surete est garanti par la Constitution et par la Convention europeenne des droits de l'homme."
  "|La vie privee et les donnees personnelles sont protegees par la loi du 6 janvier 1978 et le reglement europeen RGPD."
  "|Une donnee personnelle est toute information permettant d'identifier directement ou indirectement une personne physique."
  "|Le RGPD impose la liciteite, la transparence, la minimisation des donnees et la limitation des finalites."
  "|Toute personne dispose d'un droit d'acces, de rectification, d'effacement et d'opposition sur ses donnees."
  "|La surete au travail impose a l'employeur d'evaluer les risques et de mettre en place des mesures de prevention."
  "|Le document unique d'evaluation des risques professionnels recense les risques et les actions de prevention de l'etablissement."
  "|Le harcelement moral et le harcelement sexuel sont des delits : ils doivent etre signales et peuvent etre sanctionnes."
  "|La discrimination a l'embauche ou dans le service est interdite et expose l'auteur a des sanctions penales et civiles."
  "|Les regles d'hygiene et de surete alimentaire completent la protection des clients dans un etablissement de restauration."
  "|Savoir identifier une situation a risque, la signaler et documenter les mesures prises est une competence citoyenne et professionnelle."),
[QC("Quel texte europeen protege les donnees personnelles ?", "Le code de la route~Le RGPD~La convention de Geneve~Le traite de Rome", 1,
     "Le reglement general sur la protection des donnees est applicable depuis 2018."),
 QC("Que signifie la minimisation des donnees ?", "Collecter le plus de donnees possible~Collecter seulement les donnees necessaires~Supprimer toutes les donnees~Vendre les donnees", 1,
     "On ne collecte que les donnees utiles a la finalite declaree."),
 QC("Quel droit permet de corriger une donnee inexacte ?", "Droit d'acces~Droit de rectification~Droit d'opposition~Droit a l'oubli", 1,
     "La rectification permet de corriger ou completer les donnees."),
 QC("Qui doit realiser le document unique d'evaluation des risques ?", "Le salarie~L'employeur~Le client~Le fournisseur", 1,
     "L'employeur a l'obligation legale d'evaluer les risques et de consigner les resultats."),
 QC("Le harcelement moral est...", "Une simple remarque~Un delit sanctionne~Une pratique autorisee~Un droit de l'employeur", 1,
     "Le harcelement moral est repété et sanctionne par le droit du travail et le code penal."),
 QT("Un client demande une copie des donnees que l'hotel conserve sur lui. Que faut-il faire ?",
     "Il exerce son droit d'acces, garanti par le RGPD. L'etablissement doit lui repondre dans un delai d'un mois, lui fournir une copie des donnees le concernant et l'informer des finalites, des destinataires et de la duree de conservation. Il faut verifier l'identite du demandeur pour eviter une divulgation a un tiers, sans exiger pour autant des documents excessifs. Si certaines donnees concernent aussi d'autres personnes, on peut les masquer. Le service doit ensuite conserver une trace de la demande et mettre a jour ses registres. Un refus injustifie exposerait l'etablissement a uneplainte aupres de la CNIL.",
     "On attend droit d'acces, delai d'un mois, verification d'identite et tracabilite."),
 QT("Comment prevenir les risques professionnels dans un service de restauration ?",
     "On commence par identifier les risques : coupures, brulures, glissades, port de charges, exposition au froid ou au chaud, et risques lies au nettoyage. L'employeur consigne ces risques dans le document unique et defence les mesures : formation, equipements de protection, plan de nettoyage, signaletique, procedures en cas d'incident et suivi medical. Les salaries doivent appliquer les consignes, signaler tout accident ou situation dangereuse et participer aux formations. Enfin, on analyse les accidents du travail et les presque-accidents pour mettre a jour l'evaluation : la prevention est un cycle continu, pas un document unique figé.",
     "On attend inventaire des risques, document unique, mesures et retour d'experience.")],
C("La surete des personnes repose sur des droits opposables et sur une prevention organisationnelle permanente.",
  "Dignite + surete + donnees personnelles",
  "RGPD : acces, rectification, effacement, opposition",
  "Dignite~Respect de la personne~Donnee personnelle~Information identifiable~RGPD~Reglement europeen~Droit d'acces~Copie des donnees~Risque professionnel~Evenement dommageable~Document unique~Evaluation et prevention",
  "Identifier le droit ou le risque|Verifier le texte applicable|Preciser les obligations des parties|Appliquer la procedure|Conserver une trace ecrite",
  "Confondre acces et rectification|Ne pas verifier l'identite|Ignorer les presque-accidents|Laisser le document unique non mis a jour",
  "Un mois~Delai de reponse RGPD~CNIL~Autorite de controle~DUERP~Document unique~Harcement~Delit~EPI~Equipement de protection",
  "Droit~Protection accordee~Devoir~Obligation correspondante",
  "Prevention~Agir avant~Repression~Sanctionner apres"))

# ============================================================ PH1
add("PH1", "Conscience et inconscient", "Philosophie", ["Terminale"],
S("La conscience designe le fait, pour un sujet, de se representer le monde et de se representer qu'il se le represente."
  "|Etre conscient, c'est disposer d'une presence a soi et au monde qui rend possible le savoir et la decision."
  "|La conscience de soi ne se reduit pas a la conscience morale : elle est d'abord une lucidite sur ses propres etats."
  "|Socrate fait de l'examen de soi une condition de la vie philosophique : « connais-toi toi-meme »."
  "|Descartes definit la conscience comme le fondement du cogito : je pense, donc je suis."
  "|La conscience morale juge nos actions au regard d'une regle ou d'une valeur, comme le devoir chez Kant."
  "|Freud deconstruit la maitrise du sujet en montrant l'action de desirs et de representations inconscientes."
  "|L'inconscient n'est pas une conscience affaiblie : il est un systeme de representations qui echappent au controle de la raison."
  "|Les actes manques, les reveries et les symptomes revelent, pour Freud, des desirs refoules."
  "|La psychanalyse propose de rendre conscient ce qui etait refoule, afin de comprendre le conflit interieur."
  "|La conscience peut etre critique : elle peut douter de ses propres representations et rectifier ses jugements."
  "|Le probleme philosophique est de savoir si la conscience est vraiment maitresse d'elle-meme ou si elle est influencee par des forces qui l'echappent."),
[QC("Quelle formule resume le cogito de Descartes ?", "Je sens, donc je suis~Je pense, donc je suis~Je veux, donc je suis~Je doute, donc je meurs", 1,
     "Le cogito etablit la certitude du sujet pensant comme point de depart."),
 QC("Qui a developpe la theorie psychanalytique de l'inconscient ?", "Kant~Freud~Socrate~Aristote", 1,
     "Freud place l'inconscient au coeur de la vie psychique."),
 QC("Qu'est-ce qu'un acte manque ?", "Un acte exteriorise par erreur~Un acte realise sans y penser~Une action oubliee~Un acte moral", 0,
     "L'acte manque, ou parapraxie, trahit selon Freud un desir inconscient."),
 QC("La conscience morale juge nos actions au regard de...", "Du plaisir seul~D'une regle ou d'une valeur~De l'opinion d'autrui~Du hasard", 1,
     "Elle rapporte l'action a une exigence, par exemple le devoir chez Kant."),
 QC("Selon Freud, l'inconscient est...", "Une conscience morale~Un systeme de representations inconsciencees~Une maladie~Une memoire parfaite", 1,
     "Il s'agit de representations qui echappent au controle conscient."),
 QT("La conscience est-elle souveraine ? Construire une reponse en deux temps.",
     "D'un cote, la conscience parait souveraine : c'est par elle que nous savons que nous pensons (cogito), que nous nous jugeons et que nous choisissons. Elle peut douter de ses representations et corriger ses erreurs, ce qui la rend critique. De l'autre cote, Freud montre que nos paroles, nos oublis et nos symptomes peuvent exprimer des desirs que nous ne reconnaitrons pas : le sujet n'est donc pas entierement transparent a lui-meme. On peut conclure que la conscience n'est pas souveraine au sens d'une maitrise absolue, mais qu'elle reste la seule instance capable de prendre connaissance de ses propres limites et de travailler a les comprendre.",
     "On attend les deux moments, des references et une conclusion nuancee."),
 QT("Comment l'inconscient peut-il se manifester dans la vie quotidienne ?",
     "Il se manifeste d'abord par les actes manques : un nom oublie, une gaffe ou un objet égaré peuvent, selon Freud, exprimer un desir refoule. Il apparait aussi dans les reves, ou le refoulement se relache et ou des images inhabituelles apparaissent. Enfin, les symptomes et les repetitions de comportement peuvent signaler un conflit interieur non resolu. Ces phenomenes ne prouvent pas, a eux seuls, la theorie freudienne, mais ils invitent a ne pas croire que le sujet connait parfaitement les motifs de ses actions. La psychanalyse consiste precisement a interpreter ces signes avec la personne concernee.",
     "On attend actes manques, reves, symptomes et une conclusion critique.")],
C("La conscience donne au sujet presence a lui-meme, mais Freud montre qu'elle n'est pas entierement maitresse de ses motifs.",
  "Conscience = representation + presence a soi",
  "Cogito · conscience morale · inconscient freudien",
  "Conscience~Presence a soi~Cogito~Je pense donc je suis~Conscience morale~Jugement sur l'action~Inconscient~Representations cachees~Acte manque~Desir refoule~Refoulement~Mise a l'ecart",
  "Definir le terme|Distinguer conscience de soi et conscience morale|Presenter la these classique|Presenter la contestation freudienne|Conclure en pesant les arguments",
  "Confondre inconscient et subconscience|Croire que Freud nie la conscience|Reduire la conscience a la morale|Affirmer une these sans l'argumenter",
  "Cogito~Certitude de penser~Freud~Inconscient~Acte manque~Oubli significatif~Censure~Refoulement",
  "Socrate~Connais-toi toi-meme~Descartes~Je pense~Kant~Le devoir~Freud~Le desir",
  "Conscience de soi~Lucidite~Conscience morale~Exigence"))

# ============================================================ PH2
add("PH2", "Liberté et détermination", "Philosophie", ["Terminale"],
S("La liberte designe la capacite d'agir selon sa propre volonte, sans y etre contraint par une force exterieure."
  "|La liberte d'action s'oppose a la contrainte : un acte est libre si l'agent pouvait ne pas le commettre."
  "|La liberte de volonte est interieure : elle designe le pouvoir de se determiner soi-meme, meme dans la contrainte."
  "|Le determinisme affirme que tout evenement, y compris nos actions, a une cause et suit des lois."
  "|Le determinisme scientifique s'appuie sur l'idee que le comportement humain peut etre explique par des causes physiologiques ou sociales."
  "|Diderot montre que l'idee de liberte peut etre une illusion neccessaire a la morale et a la vie sociale."
  "|Kant distingue le phenomene, ou l'homme est soumis aux causes, et le noumene, ou il peut etre libre en tant qu'etre raisonnable."
  "|Pour Kant, la liberte est la condition de la moralite : on n'est moralement responsable que si l'on est libre."
  "|Sartre affirme que l'homme est condamne a etre libre : il ne peut pas echapper au choix, meme en refusant de choisir."
  "|La liberte negative est l'absence d'obstacles ; la liberte positive est le pouvoir reel d'agir et de se realiser."
  "|Les determinismes sociaux — famille, milieu, culture — limitent les possibilites reelles sans supprimer la capacite de juger."
  "|Le probleme philosophique est de concilier l'explication des actions par des causes avec l'exigence de responsabilite morale et juridique."),
[QC("Quelle definition correspond a la liberte negative ?", "Pouvoir de se realiser~Absence d'obstacles exterieurs~Obéissance a la loi morale~Capacite de douter", 1,
     "La liberte negative est l'absence de contrainte ; la liberte positive est le pouvoir d'agir."),
 QC("Que soutient le determinisme ?", "Que les actions sont sans cause~Que tout evenement a une cause~Que la volonte est toujours libre~Que la morale est inutile", 1,
     "Le determinisme affirme l'universalite du principe de causalite."),
 QC("Selon Kant, pourquoi la liberte est-elle necessaire ?", "Pour etre heureux~Parce qu'elle est la condition de la moralite~Pour eviter la science~Pour gagner de l'argent", 1,
     "Sans liberte, l'imputabilite morale et la responsabilite n'auraient pas de sens."),
 QC("Quelle formule est de Sartre ?", "Je pense, donc je suis~L'homme est condamne a etre libre~Connais-toi toi-meme~La liberte est une illusion", 1,
     "Sartre souligne que le choix est inévitable, meme dans le refus de choisir."),
 QC("Comment Diderot concoit-il l'idee de liberte ?", "Comme une verite scientifique~Comme une illusion utile a la morale~Comme un don divin~Comme une pure absence de lois", 1,
     "Pour Diderot, l'illusion de liberte est socialement et moralement necessaire."),
 QT("Faut-il renoncer a la liberte pour admettre le determinisme ? Construire une dialectique.",
     "Le determinisme parait d'abord menacer la liberte : si chaque action a une cause, l'agent ne pouvait pas agir autrement, et la responsabilite semble injustifiee. Mais cette consequence n'est pas inévitable. Kant montre que la liberte est une exigence de la raison pratique : pour nous juger moralement, nous devons nous considerer comme capables de nous determiner par la raison, independamment des causes naturelles. Sartre, de son cote, rappelle que meme dans une situation contrainte, il reste a choisir le sens que l'on donne a cette situation. On peut donc admettre que nos actes ont des causes sans renoncer a la liberte comprise comme capacite de jugement et de prise en charge de soi.",
     "On attend objection deterministe, reponse kantienne ou sartrienne, et conclusion nuancee."),
 QT("Comment les determinismes sociaux affectent-ils la liberte reelle ?",
     "Le milieu familial, le niveau de formation, le quartier, le reseau de relations ou la situation economique ne determiment pas mécaniquement les choix, mais ils en reducent l'eventail. Deux personnes n'ont pas les memes possibilites reelles d'accès a un emploi ou a une formation, meme si elles sont juridiquement libres. C'est la distinction entre liberte formelle, absence d'interdiction, et liberte reelle, capacite effective d'agir. Reconnaitre ces determinismes ne doit pas conduire au fatalisme : cela permet au contraire d'identifier les obstacles et de mettre en place des politiques d'emancipation, par l'education, l'acces aux droits et l'accompagnement.",
     "On attend distinction liberte formelle et reelle, exemples et consequences pratiques.")],
C("Liberte et determinisme ne s'excluent pas necessairement : tout dépend du sens donne a la liberte.",
  "Liberte negative = absence de contrainte · liberte positive = pouvoir d'agir",
  "Determinisme causal · Kant : liberte condition de la morale · Sartre : condamne a etre libre",
  "Liberte~Capacite de choisir~Determinisme~Universalite de la cause~Liberte negative~Absence d'obstacle~Liberte positive~Pouvoir reel~Responsabilite~Imputabilite de l'acte~Noumenel~Etre raisonnable",
  "Definir les termes|Poser l'objection deterministe|Presenter la reponse kantienne|Presenter la reponse existentielle|Conclure sur la responsabilite",
  "Confondre liberte et licence|Croire que determinisme signifie fatalisme|Oublier la distinction phenomenel ou noumenel|Repondre par une opinion sans argument",
  "Kant~Liberte et morale~Sartre~Choix inévitable~Diderot~Illusion utile~Loi~Contrainte et interdiction",
  "Phenomene~Monde des causes~Noumene~Etre raisonnable libre",
  "Liberte formelle~Aucune interdiction~Liberte reelle~Possibilite effective"))

# ============================================================ PH3
add("PH3", "Vérité, certitude et critique", "Philosophie", ["Terminale"],
S("La verite designe l'accord entre un jugement et ce qui est, ou entre une proposition et la realite qu'elle vise."
  "|La verite logique concerne la coherence interne d'un raisonnement : une conclusion suit necessairement des premisses."
  "|La verite empirique depend de l'experience et de la verification : une assertion est vraie si les faits la confirment."
  "|La certitude est un etat subjectif d'adhésion : on peut etre certain d'une erreur, ce qui distingue certitude et verite."
  "|Le doute methodique de Descartes consiste a rejeter provisoirement toute assertion qui peut etre mise en cause."
  "|Le cogito resite au doute parce que le fait de douter implique l'existence de celui qui doute."
  "|Les sophistes soutenaient que la verite depend du point de vue et de la persuasion, ce qui conduit au relativisme."
  "|Socrate s'oppose aux sophistes : par le dialogue, il cherche une definition stable et un savoir qui ne soit pas simple opinion."
  "|Kant limite la connaissance aux phenomenes : nous connaissons les objets tels qu'ils apparaissent dans les formes de notre entendement."
  "|La critique est l'examen des conditions et des limites d'une connaissance, plutot que l'acceptation immediate de son contenu."
  "|L'erreur n'est pas seulement ignorance : elle peut venir d'un préjuge, d'une mauvaise methode ou d'un interet qui biaise le jugement."
  "|En formation professionnelle, esprit critique signifie verifier une source, distinguer fait et interpretation et reconnaitre l'incertitude."),
[QC("Que désigne la verite logique ?", "L'accord avec les faits~La coherence d'un raisonnement~La certitude subjective~L'opinion majoritaire", 1,
     "La verite logique tient a la validite de la deduction, independamment des faits."),
 QC("Quelle difference entre certitude et verite ?", "Aucune~On peut etre certain d'une erreur~La verite est toujours subjective~La certitude est toujours fausse", 1,
     "La certitude est un etat psychologique, la verite une propriete du jugement."),
 QC("Quel est le resultat du doute methodique chez Descartes ?", "Le scepticisme total~Le cogito~La relativite~L'oubli de soi", 1,
     "Le doute conduit a la certitude de l'existence du sujet pensant."),
 QC("Qui soutenait que la verite depend de la persuasion ?", "Socrate~Les sophistes~Kant~Descartes", 1,
     "Les sophistes faisaient de la rhetorique un instrument de persuasion plutot que de savoir."),
 QC("Selon Kant, nous connaissons...", "Les choses en soi~Les phenomenes~Les seules idees~Le futur", 1,
     "La connaissance porte sur les phenomenes, tels qu'ils apparaissent dans nos formes de connaissance."),
 QT("Peut-on avoir raison d'etre certain et se tromper ? Repondre en analyant la difference entre certitude et verite.",
     "Oui, car la certitude est un etat subjectif : elle designe l'absence de doute chez le sujet, tandis que la verite concerne l'accord du jugement avec son objet. Une personne peut etre profondement convaincue d'une affirmation fausse, par exemple parce qu'elle s'appuie sur un préjuge ou une information erronee. C'est précisément pourquoi Descartes introduit le doute methodique : il faut soumettre nos certitudes a un examen pour savoir si elles resistant. Mais le doute ne peut pas etre absolu, puisque le fait de douter atteste l'existence du douteur. Ainsi, la certitude doit etre critiquee au nom de la verite, sans tomber dans un scepticisme qui rendrait toute connaissance impossible.",
     "On attend distinction nette, exemple et recours au doute methodique sans scepticisme total."),
 QT("Comment exercer son esprit critique face a une information ?",
     "On commence par identifier la source et sa fiabilite : qui publie, dans quel but, a partir de quelles donnees ? On verifie ensuite le contenu par une seconde source independante et on distingue les faits observes des interpretations proposees. On examine les mots employes : les termes generaux, les chiffres sans contexte et les affirmations categoriques doivent etre interrogés. On se demande enfin quelles hypotheses sont supposees et quelles contre-preuves existent. L'esprit critique ne signifie pas refuser systématiquement : il signifie proportionner son adhésion aux preuves et accepter de reconnaitre une erreur quand les faits l'imposent.",
     "On attend verification des sources, distinction fait et interpretation, examen des preuves et modestie intellectuelle.")],
C("La verite demande une methode : distinguer validite logique, verification empirique et adhésion subjective.",
  "Verite = accord du jugement et de l'objet",
  "Certitude subjective differente de verite · doute methodique · critique des conditions",
  "Verite~Accord avec le reel~Certitude~Adhesion subjective~Doute methodique~Refus provisoire~Cogito~Certitude premiere~Sophiste~Relativite et persuasion~Critique~Examen des limites",
  "Definir la notion|Comparer avec la notion voisine|Presenter l'objection sceptique|Presenter la reponse|Conclure en donnant un critere",
  "Confondre certitude et verite|Assimiler relativisme et critique|Croire que douter signifie nier|Accepter une source sans la verifier",
  "Descartes~Doute et cogito~Socrate~Definition par dialogue~Kant~Phenomenes~Sophistes~Persuasion",
  "Verite logique~Coherence~Verite empirique~Verification",
  "Fait~Constate et verifiable~Interpretation~Sens donne au fait"))

# ============================================================ PH4
add("PH4", "Travail, technique et valeur", "Philosophie", ["Terminale"],
S("Le travail designe une activite consacree a la transformation de la nature ou de la societe pour produire des biens ou des services."
  "|Le travail est a la fois une contrainte, car il exige un effort, et une liberte, car il permet de realiser un projet."
  "|La division du travail, analysee par Adam Smith, augmente la productivite en specialisant les taches."
  "|Marx montre que la division capitaliste du travail peut aliener le travailleur : le produit ne lui appartient pas et l'activite perd son sens."
  "|L'alienation designe le fait, pour le sujet, de se retrouver etranger a son travail, au produit et a ses semblables."
  "|La technique est l'ensemble des procedes et des outils permettant de produire ou d'agir efficacement."
  "|Aristote distingue la technè, savoir-faire oriente vers une fin, de la epistèmè, savoir theorique."
  "|La technique augmente la puissance d'agir de l'homme, mais elle peut aussi le rendre dependant d'un systeme qu'il ne maitrise plus."
  "|Heidegger critique la technique moderne comme un mode de revelation du monde qui reduit les etres a des ressources disponibles."
  "|La valeur d'une activite ne se measure pas seulement en argent : elle comprend l'utilite, la reconnaissance et l'epanouissement."
  "|Le salaire est la contrepartie economique du travail, mais il ne suffit pas a rendre compte de la qualite de l'emploi."
  "|Le probleme philosophique est de savoir comment rendre le travail a la fois productif, humain et porteur de sens."),
[QC("Qui a analyse la division du travail dans la Richesse des nations ?", "Marx~Adam Smith~Heidegger~Socrate", 1,
     "Adam Smith montre que la specialisation augmente la productivite."),
 QC("Qu'est-ce que l'alienation chez Marx ?", "Une forme de liberte~Le fait de devenir etranger a son travail~Un salaire eleve~Une methode de production", 1,
     "L'alienation separe le travailleur du produit, du processus et de son humanite."),
 QC("Quelle distinction aristotelicienne oppose savoir-faire et savoir theorique ?", "Technè et epistèmè~Liberte et contrainte~Salariat et capitale~Fait et valeur", 0,
     "La technè est un savoir-faire oriente vers une fin ; l'epistèmè est un savoir demonstratif."),
 QC("Que critique Heidegger dans la technique moderne ?", "Son absence de rentabilite~Sa reduction du monde a des ressources~Sa complication~Son cout eleve", 1,
     "Il dénonce une vision du monde ou tout devient « stock » disponible."),
 QC("La valeur d'un travail ne se reduit pas a...", "La reconnaissance~Son salaire~Son utilite~Son sens", 1,
     "Le salaire est une mesure economique partielle de la valeur du travail."),
 QT("Comment la division du travail peut-elle augmenter la productivite et nuire au travailleur ?",
     "Adam Smith montre que la specialisation des taches procure trois avantages : apprentissage plus rapide, economie de temps et innovation. Dans un hotel, separating l'accueil, l'entretien des chambres et la cuisine permet d'atteindre une meilleure qualite et un gain de temps. Mais Marx observe que la repetition d'une tache parcellaire peut priver le travailleur de la vision d'ensemble de son activite : il ne fabrique plus un produit qu'il reconnait comme le sien. L'aliénation est d'autant plus forte que le produit appartient a autrui et que le rythme est impose. D'ou l'enjeu de former, de rotativiser les postes et de donner du sens a chaque tache.",
     "On attend les gains de productivite et les effets d'aliénation, avec un exemple professionnel."),
 QT("La technique libere-t-elle l'homme du travail ? Repondre de maniere nuancee.",
     "La technique augmente l'efficacite : elle remplace les efforts penibles, reduit le temps de certaines taches et permet de produire davantage. Elle peut donc liberer du temps et de l'energie. Mais elle crée aussi de nouveaux besoins, de nouvelles dependances et de nouvelles contraintes : formation permanente, maintenance, normes de securite, surveillance des systemes. Heidegger montre que la technique moderne peut transformer notre rapport au monde en rapport d'exploitation. Enfin, le temps gagne n'est pas necessarily un temps de liberte : il peut etre absorbe par une intensification du travail. La technique est donc un outil ambigu, dont l'effet depend des choix sociaux et de l'organisation du travail.",
     "On attend gains, nouvelles contraintes, reference critique et conclusion nuancee.")],
C("Travail et technique produisent de la valeur, mais leur organisation peut aussi priver le sujet de sens.",
  "Travail = transformation + projet",
  "Division du travail · alienation · technè et epistèmè",
  "Travail~Activite transformatrice~Division du travail~Specialisation des taches~Alienation~Etrangereté au produit~Technique~Procedes et outils~Technè~Savoir-faire~Valeur~Utilite et reconnaissance",
  "Definir travail et technique|Presenter les gains de productivite|Presenter l'objection alienation|Interroger la valeur du travail|Conclure sur le sens",
  "Reduire le travail au salaire|Confondre technique et technologie|Croire que productivite signifie bien-etre|Omettre la critique de Heidegger",
  "Smith~Division du travail~Marx~Alienation~Aristote~Technè et epistèmè~Heidegger~Critique de la technique~Salaire~Contrepartie economique",
  "Travail contrainte~Effort necessaire~Travail liberte~Projet realise",
  "Productivite~Produire plus avec moins~Sens~Valeur vcue de l'activite"))

# FIN DES LOTS
valider_et_ecrire(F, "sthr-mat-part-A.json")
