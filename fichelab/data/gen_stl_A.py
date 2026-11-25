# -*- coding: utf-8 -*-
"""Generateur stl-mat-part-A.json — lot A : tronc commun (20 fiches).

Français (4), Maths (4), Physique-Chimie (4), SVT (4), Anglais (2), HGGS (2).
Chaque fiche : 12 points, 9 questions (7 QCM + 2 texte), 7 blocs, 3 schemas.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _stl_common import FIL, REF, S, R, QC, QT, C, build, valider_et_ecrire

F = []


def add(prefix, titre, mat, ans, points, questions, c):
    F.append(build(prefix, titre, mat, ans, points, questions, c))


# ============================================================ FR1
add("FR1", "L'argumentation et les figures de style", "Français", ["1re"],
S("L'argumentation est une forme de discours qui vise à convaincre ou à persuader un destinataire en s'appuyant sur des raisons et des preuves."
  "|Le plan dialectique organise le propos en trois temps : une these (position defendedue), une antithese (objection) et une synthese (depassement)."
  "|Un argument est une affirmation generale qui justifie la these ; un exemple est un cas concret qui rend l'argument sensible et verifiable."
  "|Les connecteurs logiques structurent le raisonnement : « car », « parce que » pour la cause, « donc », « ainsi » pour la consequence, « cependant » pour l'opposition."
  "|La comparaison explicite un rapport de ressemblance avec un outil de comparaison : « comme », « tel », « ressembler à »."
  "|La métaphore supprime l'outil de comparaison et transfert un sens : « cette lumière est un feu » designate une qualité par image."
  "|La métonymie designe une realite par un elemnet qui lui appartient : « le fer » pour l'epee, « la plume » pour l'ecriture."
  "|La personnification attribue des actions humaines à un etre inanime ou à un animal : « le vent hurle »."
  "|L'antithese rapproche deux termes opposes dans une meme phrase ; l'oxymore associe deux mots contradictoires comme « un silence bruyant »."
  "|Le registre d'un texte oriente la reception : pathétique pour emouvoir, comique pour divertir, tragique pour susciter la crainte, lyrique pour exprimer un sentiment."
  "|Les modalisateurs (« peut-être », « sans doute », « il semble ») nuancent une affirmation et rendent le propos plus credible."
  "|Au bac technologique STL, la maitrise de l'argumentation et l'identification precise des figures sont attendues dans les epreuves de français."),
[QC("Quel est l'objectif principal d'un discours argumentatif ?", "Convaincre ou persuader~Raconter une histoire~Decrire un paysage~Reciter un poeme", 0,
     "L'argumentation cherche à obtenir l'adhesion du lecteur par des raisons et des preuves."),
 QC("Comment appelle-t-on un plan these, antithese, synthese ?", "Plan chronologique~Plan dialectique~Plan thematique~Plan descriptif", 1,
     "Le plan dialectique confronte deux positions avant de proposer un depassement."),
 QC("Quelle figure de style utilise « comme un lion » ?", "La metaphore~La comparaison~La metonymie~L'oxymore", 1,
     "La comparaison est explicite grace à l'outil « comme »."),
 QC("Quel connecteur introduit une opposition ?", "Parce que~Ainsi~Cependant~En effet", 2,
     "« Cependant » marque l'opposition ou la nuance, contrairement aux connecteurs de cause et de consequence."),
 QC("Que designe la metonymie ?", "Un sens figure sans outil~Un terme voisin de la realite designee~Une comparaison explicite~Une repetition de sons", 1,
     "La metonymie remplace un mot par un terme apparente : la plume pour l'ecriture."),
 QC("Quel registre vise à susciter l'emotion et la pitie ?", "Comique~Pathétique~Lyrique~Epique", 1,
     "Le registre pathétique cherche a emouvoir, par le recit d'une souffrance ou d'une injustice."),
 QC("Qu'appelle-t-on un modalisateur ?", "Un connecteur de consequence~Un mot qui nuance une affirmation~Une figure de repetitions~Un type de ponctuation", 1,
     "« Peut-etre », « il semble » attenuent la force d'une affirmation."),
 QT("Distinguer un argument d'un exemple, puis montrer comment ils s'articulent dans un paragraphe.",
    "L'argument est une affirmation generale qui soutient la these : « la formation aux gestes d'urgence reduit les risques ». L'exemple est un cas concret qui l'illustre : « dans le laboratoire X, le nombre d'incidents a diminue de moitie apres une formation ». Le paragraphe articule les deux avec un connecteur : l'argument pose la regle, l'exemple la rend credible, et une phrase de conclusion relie le cas à la these. Un argument sans exemple reste une opinion ; un exemple sans argument ne prouve rien.",
    "On definit les deux notions, puis on montre leur complementarite dans un paragraphe argumente."),
 QT("Identifier les figures de style de « Le vent hurlait, la nuit etait un gouffre, je vivais cette attente » et preciser leur effet.",
    "« Le vent hurlait » est une personnification : on attribue une action humaine au vent, ce qui rend la scene plus vivante et inquietante. « La nuit etait un gouffre » est une metaphore : la nuit est comparee à un gouffre sans outil, ce qui suggere une profondeur angoissante. « Je vivais cette attente » associe le verbe vivre à un nom abstrait par une metonymie ou une personnification de l'attente. Ces figures installent un registre lyricque et pathétique qui traduit l'etat interieur du locuteur.",
    "On nomme chaque figure, on cite le passage, puis on explique son effet sur le lecteur.")],
C("Argumenter, c'est defendre une these avec des arguments appuyes sur des exemples, dans un registre choisi.",
  "Argument + exemple + connecteur = paragraphe convaincant",
  "these · antithese · synthese · comparaison · metaphore · registres · modalisateurs",
  "These~Position defendue~Je soutiens que|Argument~Raison generale~Parce que|Exemple~Cas concret~Par exemple~Comparaison~Ressemblance explicite~Comme~Metaphore~Ressemblance implicite~Est un~Registre~Orientation du texte~Pathétique~Modalisateur~Nuance l'affirmation~Peut-être~Connecteur~Lien logique~Cependant",
  "Lire le sujet et le type de texte|Degager la these defendue|Choisir des arguments pertinents|Appuyer chaque argument par un exemple|Conclure en nuancant la position",
  "Confondre argument et exemple|Employer « comme » dans une metaphore|Choisir un registre inadapté au sujet|Accumuler les figures sans les expliquer|Oublier les connecteurs logiques",
  "« Comme un lion »~Comparaison~« Il est un lion »~Metaphore~« La plume »~Metonymie~« Le vent hurle »~Personnification~« Silence bruyant »~Oxymore",
  "Argument~Affirmation generale~Soutient la these~Portee universelle~Exemple~Cas concret~Illustre l'argument~Un seul cas",
  "Convaincre~Faire adhérer par la raison~Arguments et preuves~Adhesion reflexive~Persuader~Faire adhérer par l'emotion~Registre pathétique~Adhesion sentimentale"))

# ============================================================ FR2
add("FR2", "La synthèse de documents : méthode et restitution", "Français", ["1re"],
S("La synthese de documents consiste à restituer l'essentiel de plusieurs textes portant sur un meme sujet sous forme d'un document nouveau et structure."
  "|Le dossier comprend generalement deux à quatre documents de natures variees : article, extrait d'ouvrage, graphique, texte reglementaire ou temoignage."
  "|La lecture active identifie pour chaque document la source, la date, l'auteur, la these defendue et les arguments a l'appui."
  "|La regle fondamentale est de regrouper les idees par theme et non par document, afin d'eviter la simple juxtaposition."
  "|Un titre et un sous-titre donnent une ligne de conduite avant la rédaction."
  "|L'introduction presente le sujet, le dossier et annonce le plan, sans developper d'opinion personnelle."
  "|Chaque partie s'appuie sur des idees cles, des exemples precis et des references explicites aux documents."
  "|Les chiffres, les dates et les noms propres sont repris exactement : une synthese est fidele a ses sources."
  "|La conclusion fait le bilan des apports du dossier et ouvre sur une prolongation du sujet."
  "|Le style est impersonnel et clair : on evite le « je », les jugements de valeur et les expansions inutiles."
  "|La maitrise de la langue, de l'orthographe et de la presentation est evaluee avec rigueur au baccalaureat technologique."
  "|Cet exercice prepare directement la redaction de comptes rendus et de notes de synthese en laboratoire."),
[QC("Quelle est la regle fondamentale d'une synthese ?", "Resumer chaque document separement~Regrouper les idees par theme~Ajouter son opinion~Recopier les documents", 1,
     "La synthese est thematique : elle reconstruit un propos a partir de plusieurs documents."),
 QC("Que contient l'introduction d'une synthese ?", "Le detail des arguments~Le sujet, le dossier et l'annonce du plan~La conclusion~Une prise de position", 1,
     "L'introduction cadre le sujet et annonce le plan sans developper d'avis personnel."),
 QC("Comment citer un document dans une synthese ?", "Par une note de bas de page obligatoire~En mentionnant le numero du document et l'idee~Par une photographie~Par une reference de bibliotheque", 1,
     "Les references explicites, par exemple « le document 2 souligne que », sont attendues."),
 QC("Quel registre de langue privilégier ?", "Familier~Impersonnel et clair~Argotique~Poetique", 1,
     "Le « on » ou les tournures impersonnelles remplacent le « je »."),
 QC("Que faire d'un chiffre important du dossier ?", "L'arrondir librement~Le reprendre exactement~Le supprimer~Le remplacer par « beaucoup »", 1,
     "Fidelite et exactitude des donnees sont exigees."),
 QC("Combien de documents composent generalement le dossier ?", "Un seul~Deux à quatre~Dix~Vingt", 1,
     "Le dossier comporte le plus souvent deux à quatre documents de natures differentes."),
 QC("Quel plan evite la juxtaposition des documents ?", "Plan par document~Plan thematique~Plan alphabetique~Plan chronologique strict", 1,
     "Le plan thematique confronte plusieurs documents dans chaque partie."),
 QT("Expliquer pourquoi une synthese ne doit pas etre redigee document par document et proposer une methode pour l'eviter.",
    "Rediger document par document produit une juxtaposition : les idees se repetent, les contradictions ne sont pas traitees et les enjeux communs n'apparaissent pas. La methode consiste à lire tous les documents, à relever les idees sur des fiches en indiquant la source, à degager trois axes transversaux, puis à classer chaque idee sous un axe avant de rediger. On obtient un plan thematique ou chaque partie confronte les apports de plusieurs documents, avec des references precises et une progression logique.",
    "On explique le risque de juxtaposition, puis on decrit le classement thematique des idees avant redaction."),
 QT("Depeindre la repartition du temps pour une synthese de quatre documents en deux heures.",
    "On consacre environ 25 minutes à une lecture active : source, date, these et arguments de chaque document, plus les chiffres cles. On passe 20 minutes à construire un plan en trois axes alimentes par plusieurs documents. La redaction occupe environ 60 minutes : introduction avec annonce du plan, trois parties developpees avec references, conclusion bilan et ouverture. On garde 15 minutes pour relire : orthographe, transitions, reprise exacte des chiffres, presence des references et longueur demandee. Une copie aeree avec des paragraphes courts est plus lisible.",
    "On propose une repartition realiste : lecture, plan, redaction, relecture, avec les verifications finales.")],
C("La synthese demonte les documents pour reconstruire un texte thematique, fidele et impersonnel.",
  "Synthese = idees regroupees par theme, jamais par document",
  "lecture active · fiches · plan thematique · references · relecture",
  "Lecture active~Source, date, these~Repérage~Fiches~Idees et references~Classement~Plan thematique~Trois axes~Structure~References~Numero du document~Preuve de fidelite~Chiffres~Repris tels quels~Exactitude~Style~Impersonnel~Pas de « je »",
  "Lire tous les documents|Relever idees, chiffres et sources|Construire un plan thematique|Rediger avec des references|Relire et corriger",
  "Proceder document par document|Ajouter une opinion personnelle|Arrondir les chiffres|Ne pas citer les documents|Negliger la relecture",
  "4 documents~25 minutes de lecture~3 axes~Plan thematique~60 minutes~Redaction~15 minutes~Relecture~2 documents~Minimum courant",
  "Plan par document~Risque de juxtaposition~Plan thematique~Synthese reussie",
  "Introduction~Sujet, dossier, plan~Conclusion~Bilan et ouverture"))

# ============================================================ FR3
add("FR3", "Le récit et les temps narratifs", "Français", ["Terminale"],
S("Le recit est un texte qui rapporte une succession d'evenements reellement vecus ou imagines, organizes dans le temps."
  "|Le narrateur est la voix qui raconte : il peut etre interne (il participe à l'action) ou externe (il est etranger à l'histoire)."
  "|La focalisation interne adopte le point de vue d'un personnage ; la focalisation externe ne rapporte que les apparences."
  "|La focalisation zero, ou omnisciente, permet au narrateur de connaitre les pensees de tous les personnages."
  "|Le passe compose est le temps de base du recit : il exprime les evenements de l'intrigue qui font avancer l'action."
  "|L'imparfait decrit les circonstances, les habitudes et l'etat des lieux ; il cree l'atmosphere et la duree."
  "|Le plus-que-parfait exprime une action anterieure à un evenement du passe compose ou de l'imparfait."
  "|Le present de narration donne de la vivacite en rapprochant l'evenement du lecteur."
  "|Le futur simple peut introduire une prospective ou un evenement annonce par avance."
  "|Les connecteurs temporels (« d'abord », « puis », « soudain », « enfin ») construisent la chronologie."
  "|Les figures de temps que sont l'ellipse, la scene et la pause modifient le rythme du recit."
  "|L'analyse des temps et du point de vue est un exercice frequent de l'epreuve de francais au baccalaureat technologique."),
[QC("Quel temps exprime les evenements qui font avancer l'intrigue ?", "L'imparfait~Le passe compose~Le plus-que-parfait~Le present de l'indicatif", 1,
     "Le passe compose est le temps narratif par excellence ; l'imparfait decorit le cadre."),
 QC("Quel temps decrit les circonstances et les habitudes dans un recit ?", "Le passe simple~Le futur simple~L'imparfait~Le participe present", 2,
     "L'imparfait est le temps de la description, de la duree et de l'habitude."),
 QC("Un narrateur qui connait les pensees de tous les personnages utilise une focalisation…", "Interne~Externe~Zero~Double", 2,
     "La focalisation zero est omnisciente : le narrateur sait tout de tous les personnages."),
 QC("Que designe une ellipse dans un recit ?", "Une longue description~Un temps mort suppose~Une omission de temps entre deux evenements~Une repetition", 2,
     "L'ellipse supprime une periode de temps et accelere le rythme narratif."),
 QC("Quel effet produit le present de narration ?", "Il eloigne le lecteur~Il rend la scene plus vivante~Il indique le futur~Il ralentit le recit", 1,
     "Le present de narration rapproche l'evenement du lecteur et le rend plus frappant."),
 QC("Comment appelle-t-on un narrateur qui participe à l'action ?", "Externe~Interne~Omniscient~Impersonnel", 1,
     "Le narrateur interne est un personnage de l'histoire, souvent à la premiere personne."),
 QC("Quel connecteur marque une rupture dans la chronologie ?", "D'abord~Puis~Soudain~Enfin", 2,
     "« Soudain » introduit un evenement inattendu et rompt le deroulement attendu."),
 QT("Distinguer le passe compose et l'imparfait dans un extrait de recit et expliquer leur role respectif.",
    "Le passe compose rapporte les evenements ponctuels qui constituent l'intrigue : « il ouvrit la porte », « le chien aboya ». L'imparfait decrit l'arriere-plan, les habitudes ou les etats : « la pluie tombait », « il habitait la depuis dix ans ». Le passe compose fait avancer l'action comme une suite de points sur une ligne de temps, tandis que l'imparfait etale une duree et installe l'atmosphere. Leur alternance cree le rythme du recit et permet de distinguer ce qui arrive de ce qui etait deja là.",
    "On oppose l'avancee de l'intrigue à la description du cadre, avec des exemples de verbes."),
 QT("Un extrait commence par « Je me souviens. La lumière déclinait déjà. » Analyser le point de vue et le temps choisis.",
    "La premiere personne du singulier indique un narrateur interne : le recit est ancree dans la memoire d'un personnage, avec une focalisation interne probable. Le present « je me souviens » est un present d'enonciation qui place le lecteur dans l'acte de rememoration, tandis que l'imparfait « declinait » decrit une situation durable et incompletive au moment du souvenir. Cette combinaison installe une distance temporelle et une atmosphere melancolique : l'evenement est passe mais reste present dans la conscience du narrateur.",
    "On identifie le narrateur interne, le present d'enonciation et la valeur descriptive de l'imparfait.")],
C("Le recit articule des evenements dans le temps : le passe compose avance l'action, l'imparfait installe le cadre.",
  "Passe compose = evenements · imparfait = description · plus-que-parfait = anteriorite",
  "narrateur interne ou externe · focalisation · connecteurs temporels · rythme",
  "Passe compose~Evenements~Action avance~Imparfait~Description~Cadre et duree~Plus-que-parfait~Anteriorite~Avant l'evenement~Present de narration~Vivacite~Rapproche le lecteur~Narrateur interne~Personnage~Je~Narrateur externe~Temoignage~Pas de « je »",
  "Repérer le narrateur et sa focalisation|Relever les temps employes|Classer les verbes en actions et descriptions|Observer les connecteurs temporels|Analyser l'effet de rythme obtenu",
  "Confondre passe compose et imparfait|Croire que le narrateur est toujours l'auteur|Oublier le plus-que-parfait|Prendre le present pour un temps du futur|Negliger les connecteurs",
  "« Il ouvrit »~Passe compose~« La pluie tombait »~Imparfait~« Il etait parti »~Plus-que-parfait~« Je me souviens »~Present~« Soudain »~Rupture",
  "Focalisation interne~Un point de vue~Focalisation zero~Omnisciente",
  "Imparfait~Duree et description~Passe compose~Evenements ponctuels"))

# ============================================================ FR4
add("FR4", "La poésie : versification et images poétiques", "Français", ["1re"],
S("Le vers est une ligne de poeme, unité rythmique delimiter par la mise en page, distinct de la phrase qui peut s'etendre sur plusieurs vers."
  "|Le nombre de syllables compte jusqu'à la derniere voyelle pronouncee, avec des regles particulieres pour le « e » muet en fin de vers."
  "|L'hemistiche designe chaque moitie d'un vers, particulierement dans l'alexandrin coupe en deux fois six syllables."
  "|La rime est une repetition de sons à la fin de deux ou plusieurs vers ; on distingue rime masculine et rime feminine."
  "|Les rimes peuvent etre suivies (AABB), croisees (ABAB) ou embrassees (ABBA)."
  "|Le rythme naît de la disposition des accents, des coupes et de la longueur des vers."
  "|le vers libre renonce au nombre fixe de syllables et à la rime reguliere, tout en conservant un rythme propre."
  "|L'image poetique transforme la realite par la comparaison, la metaphore, la personnification ou l'hyperbole."
  "|La valeur symbolicque d'une image depasse sa signification litterale : le vent peut figurer le temps qui passe."
  "|Le Champ lexical regroupe les mots qui se repondent par le sens et construit une ambiance ou une these."
  "|Le son et le sens sont lies en poesie : les alliterations et les assonances rendent la lecture plus sensible."
  "|L'etude d'un poeme au bac technologique demande de relier la forme, les images et le sens global du texte."),
[QC("Combien de syllables compte un alexandrin ?", "Huit~Dix~Douze~Quatorze", 2,
     "L'alexandrin est un vers de douze syllables, souvent coupe en deux hemistiches de six."),
 QC("Que designe une rime croisee ?", "AABB~ABAB~ABBA~AABB", 1,
     "Les rimes croisees alternent les sons : rime A, rime B, rime A, rime B."),
 QC("Qu'appelle-t-on un hemistiche ?", "Un poeme court~Une moitie de vers~Une strophe de quatre vers~Une rime feminine", 1,
     "L'hemistiche est une des deux parties d'un vers, par exemple six syllables dans l'alexandrin."),
 QC("Quel vers renonce au nombre fixe de syllables ?", "L'alexandrin~Le decasyllabe~Le vers libre~L'octosyllabe", 2,
     "Le vers libre garde un rythme mais ne respecte ni metre fixe ni rime reguliere."),
 QC("Quelle figure attribue des actions humaines à un element naturel ?", "L'hyperbole~La personnification~La metonymie~L'alliteration", 1,
     "La personnification donne des actions ou des sentiments humains à un etre inanime."),
 QC("Quel procede repete une consonne pour produire un effet sonore ?", "L'assonance~L'alliteration~La rime~La diurese", 1,
     "L'alliteration repete une consonne ; l'assonance repete une voyelle."),
 QC("Qu'est-ce qu'un champ lexical ?", "Une liste de rimes~Un ensemble de mots lies par le sens~Le nombre de vers d'une strophe~Une figure de style", 1,
     "Le champ lexical regroupe des mots qui se repondent semantiquement et construisent une ambiance."),
 QT("Distinguer la rime feminine de la rime masculine et donner un exemple de chaque.",
    "La rime masculine se termine par une voyelle ou une consonne prononcee, par exemple « jour » et « amour ». La rime feminine se termine par un « e » muet prononce apres la derniere voyelle tonique, par exemple « lumière » et « maniere ». Cette distinction compte dans la versification classique : les rimes feminines et masculines sont generalement alternees dans un sonnet. L'essentiel est d'ecouter la derniere voyelle reellement entendue et non la simple lettre finale ecrite.",
    "On definit les deux types de rimes et on donne des exemples ou la prononciation est explicite."),
 QT("Analyser l'effet de l'image « le temps est un voleur » dans un poeme.",
    "Il s'agit d'une metaphore : le temps est presenté comme un etre qui derobe, sans outil de comparaison. La personnification associe au temps une action intentionnelle, ce qui transforme une notion abstraite en agent concret. L'image suggere que la duree nous prive insensiblement de quelque chose, probablement la jeunesse ou les souvenirs. Elle s'appuie sur un champ lexical possible du vol et de la perte, et son effet est a la fois inquietant et melancolique : le lecteur ressent le passage du temps comme une experience sensible plutot que comme une donnee abstraite.",
    "On nomme la figure, on explique le transfert de sens et on decrit l'effet produit.")],
C("Un poeme se lit deux fois : d'abord pour son rythme et ses sons, puis pour les images et le sens qu'elles construisent.",
  "alexandrin = 12 syllables · rimes ABAB ou ABBA · image = transfert de sens",
  "vers · hemistiche · rime · rythme · vers libre · champ lexical · alliteration",
  "Vers~Unite rythmique~Ligne du poeme~Alexandrin~Douze syllables~Deux hemistiches~Rime~Repetition finale~Masculine ou feminine~Rythme~Accents et coupes~Donne le mouvement~Image~Transfert de sens~Metaphore~Vers libre~Sans metre fixe~Rythme propre",
  "Compter les syllables du vers|Repérer les coupes et les accents|Identifier le type de rimes|Relever les images et les champs lexicaux|Relier la forme au sens du poeme",
  "Compter les lettres au lieu des syllables|Oublier le « e » muet en fin de vers|Confondre vers et phrase|Nommer une figure sans expliquer son effet|Ignorer les sons",
  "12 syllables~Alexandrin~6 + 6~Hemistiches~AABB~Rimes suivies~ABAB~Rimes croisees~ABBA~Rimes embrassees",
  "Rime masculine~Voyelle ou consonne finale~Rime feminine~« e » muet entendu",
  "Vers libre~Pas de metre fixe~Vers classique~Nombre de syllables impose"))

# ============================================================ MA1
add("MA1", "Fonctions affines, linéaires et variations", "Maths", ["1re"],
S("Une fonction affine est une fonction de la forme f(x) = a·x + b, où a et b sont deux réels constants."
  "|Le nombre a est le coefficient directeur ou pente ; le nombre b est l'ordonnée à l'origine, c'est-à-dire f(0)."
  "|Lorsque b = 0, la fonction est linéaire : elle traduit une situation de proportionnalité et sa droite passe par l'origine."
  "|Une fonction affine est définie sur l'ensemble des réels, sauf indication contraire dans l'énoncé."
  "|Si a est strictement positif, la fonction est strictement croissante sur tout l'ensemble de définition."
  "|Si a est strictement négatif, la fonction est strictement décroissante ; si a vaut zéro, la fonction est constante."
  "|La représentation graphique d'une fonction affine est une droite : deux points suffisent à la tracer."
  "|On utilise le plus souvent les points de coordonnées (0 ; b) et (1 ; a + b) pour construire la droite."
  "|Le coefficient directeur se calcule avec deux points quelconques A(x_A ; y_A) et B(x_B ; y_B) par a = (y_B − y_A)/(x_B − x_A)."
  "|Deux droites sont parallèles si et seulement si leurs coefficients directeurs sont égaux, et perpendiculaires si a·a' = −1."
  "|Résoudre f(x) = c revient à chercher l'abscisse du point d'intersection de la droite avec la droite horizontale y = c."
  "|Dans une situation avec un coût fixe et un coût unitaire, le coût total est une fonction affine : f(x) = coût unitaire·x + coût fixe."),
[QC("Quelle est la représentation graphique d'une fonction affine ?", "Une parabole~Une droite~Un cercle~Une hyperbole", 1,
     "Toute fonction de la forme f(x) = ax + b se représente par une droite."),
 QC("Dans f(x) = −3x + 2, que vaut l'ordonnée à l'origine ?", "−3~2~3~−2", 1,
     "L'ordonnée à l'origine est b = 2, donc la droite passe par le point (0 ; 2)."),
 QC("Une fonction affine avec a < 0 est…", "Croissante~Décroissante~Constante~Indéfinie", 1,
     "Un coefficient directeur négatif rend la fonction strictement décroissante."),
 QC("Quel est le coefficient directeur de la droite passant par A(1 ; 3) et B(3 ; 7) ?", "1~2~4~5", 1,
     "a = (7 − 3)/(3 − 1) = 4/2 = 2."),
 QC("Quand une fonction affine est-elle linéaire ?", "Quand a = 0~Quand b = 0~Quand a = b~Quand a > 0", 1,
     "b = 0 donne f(x) = ax : la droite passe par l'origine et traduit la proportionnalité."),
 QC("Deux droites sont parallèles. Que peut-on affirmer ?", "Elles ont la même ordonnée à l'origine~Elles ont le même coefficient directeur~Elles sont perpendiculaires~Elles se coupent", 1,
     "Le parallélisme se lit sur la pente : a = a'."),
 QC("On résout 3x − 1 = 8. Quelle est la solution ?", "x = 2~x = 3~x = 7/3~x = 9", 1,
     "3x = 9 donc x = 3, abscisse du point où la droite coupe y = 8."),
 QT("Une droite passe par A(1 ; 5) et B(3 ; 11). Déterminer son équation et calculer f(10).",
    "Le coefficient directeur vaut a = (11 − 5)/(3 − 1) = 6/2 = 3. En utilisant A(1 ; 5) : 5 = 3 × 1 + b, donc b = 2. L'équation est f(x) = 3x + 2, vérifiée par B puisque 3 × 3 + 2 = 11. Alors f(10) = 3 × 10 + 2 = 32. Graphiquement, la droite coupe l'axe des ordonnées en (0 ; 2) et monte de 3 unités quand x augmente de 1.",
    "On calcule la pente avec les deux points, on isole b, puis on remplace x par 10 et on vérifie."),
 QT("Un abonnement coûte 25 € par mois plus 0,20 € par message. Écrire la fonction du coût mensuel et calculer le coût pour 120 messages.",
    "Le coût fixe est l'ordonnée à l'origine b = 25 et le coût variable par unité est la pente a = 0,20. La fonction est f(x) = 0,20·x + 25. Pour x = 120 : f(120) = 0,20 × 120 + 25 = 24 + 25 = 49 €. On remarque que f est croissante car a > 0 et que f(0) = 25 € correspond à l'abonnement seul, sans aucun message.",
    "Identifier le coût fixe et le coût variable, puis remplacer x par 120 et interpréter f(0).")],
C("Une fonction affine est une droite : sa pente dit si elle monte ou descend, son ordonnée à l'origine dit où elle coupe l'axe vertical.",
  "f(x) = a·x + b · a = Δy/Δx",
  "a > 0 croissante · a < 0 décroissante · b = f(0)",
  "a~Pente et variations~Monte si a > 0~b~Ordonnée à l'origine~Point (0 ; b)~Δx~Écart en abscisses~x_B − x_A~Δy~Écart en ordonnées~y_B − y_A",
  "Repérer a et b dans l'équation|Placer le point (0 ; b)|Placer le point (1 ; a + b)|Tracer la droite à la règle|Vérifier le sens des variations",
  "Confondre a et b|Oublier que a < 0 inverse une inéquation|Croire qu'une droite verticale est une fonction|Diviser par zéro avec deux points de même abscisse|Omettre l'unité dans l'interprétation",
  "f(x) = −3x + 2~Décroissante, passe par (0 ; 2)~A(1 ; 3), B(3 ; 7)~a = 2~b = 0~Droite passant par l'origine~a·a' = −1~Perpendiculaire à pente 2 : a' = −0,5~f(x) = 2x + 25~f(120) = 265 €",
  "Fonction affine~Droite décalée de b~Fonction linéaire~Droite passant par l'origine",
  "a > 0~Fonction croissante~a < 0~Fonction décroissante"))

# ============================================================ MA2
add("MA2", "Équations et inéquations du second degré", "Maths", ["1re"],
S("Une équation du second degré s'écrit a·x² + b·x + c = 0 avec a non nul."
  "|Le discriminant de cette équation vaut Δ = b² − 4·a·c : il détermine le nombre de solutions réelles."
  "|Si Δ est strictement positif, l'équation admet deux solutions réelles distinctes."
  "|Si Δ est nul, l'équation admet une unique solution réelle, appelée racine double, égale à −b/(2a)."
  "|Si Δ est strictement négatif, l'équation n'admet aucune solution réelle."
  "|Les solutions, lorsque Δ est positif ou nul, se calculent avec les formules x₁ = (−b − √Δ)/(2a) et x₂ = (−b + √Δ)/(2a)."
  "|Tout trinôme du second degré peut être factorisé sous la forme a·(x − x₁)·(x − x₂) lorsqu'il admet deux racines réelles."
  "|La résolution par factorisation utilise la propriété : un produit de facteurs est nul si et seulement si l'un des facteurs est nul."
  "|Une identité remarquable utile est (a + b)² = a² + 2ab + b², ainsi que (a − b)(a + b) = a² − b²."
  "|Pour résoudre une inéquation du second degré, on place les racines sur un tableau de signes puis on étudie le signe du trinôme."
  "|Si a est positif, le trinôme est négatif entre les deux racines et positif à l'extérieur ; le sens s'inverse si a est négatif."
  "|Les équations et inéquations du second degré servent en STL à modéliser des trajectoires, des rendements ou des équilibres."),
[QC("Quelle est la formule du discriminant ?", "b² + 4ac~b² − 4ac~2ab − c²~a² − 4b", 1,
     "Pour a·x² + b·x + c = 0, le discriminant vaut Δ = b² − 4ac."),
 QC("Combien de solutions réelles si Δ < 0 ?", "0~1~2~Une infinité", 0,
     "Un discriminant négatif signifie qu'il existe aucune solution réelle."),
 QC("Que vaut la racine double quand Δ = 0 ?", "b/a~−b/(2a)~2a/b~−2a/b", 1,
     "La racine double vaut −b/(2a)."),
 QC("Comment factorise-t-on a² − b² ?", "(a − b)²~(a + b)(a − b)~(a + b)²~a(a − b)", 1,
     "C'est la différence de deux carrés."),
 QC("Quelle est la condition d'existence de 1/(x − 2) ?", "x = 2~x ≠ 2~x > 2~Aucune condition", 1,
     "Le dénominateur ne doit pas être nul, donc x ≠ 2."),
 QC("Que vaut (a + b)² ?", "a² + b²~a² + 2ab + b²~a² − 2ab + b²~a² + ab + b²", 1,
     "Le carré d'une somme comporte le terme croisé 2ab."),
 QC("Avec a > 0 et deux racines r₁ < r₂, où le trinôme est-il négatif ?", "Avant r₁~Entre r₁ et r₂~Après r₂~Partout", 1,
     "Une parabole à coefficeint positif est sous l'axe des abscisses entre ses deux racines."),
 QT("Résoudre x² − 5x + 6 = 0 en détaillant la méthode, puis donner les solutions.",
    "On identifie a = 1, b = −5, c = 6. Le discriminant vaut Δ = b² − 4ac = 25 − 24 = 1 > 0. Les solutions sont x = (−b ± √Δ)/(2a) = (5 ± 1)/2, soit x₁ = 3 et x₂ = 2. On retrouve le même résultat par factorisation : x² − 5x + 6 = (x − 2)(x − 3), et un produit est nul si l'un des facteurs est nul. On vérifie : 9 − 15 + 6 = 0 et 4 − 10 + 6 = 0.",
    "On attend le calcul du discriminant, la formule des racines et une vérification."),
 QT("Développer et réduire A = (2x − 1)² − (x + 3)(x − 3), puis discuter la factorisation du résultat.",
    "(2x − 1)² = 4x² − 4x + 1 et (x + 3)(x − 3) = x² − 9. Donc A = 4x² − 4x + 1 − x² + 9 = 3x² − 4x + 10. Son discriminant vaut Δ = (−4)² − 4 × 3 × 10 = 16 − 120 = −104 < 0 : le trinôme n'est pas factorisable sur ℝ en produit de facteurs du premier degré. Comme a = 3 > 0 et Δ < 0, l'expression reste strictement positive pour tout réel x.",
    "On développe avec les identités, on réduit, puis on justifie l'absence de factorisation par le discriminant.")],
C("Le discriminant donne le nombre de racines ; la factorisation et le tableau de signes donnent les solutions et les inéquations.",
  "Δ = b² − 4ac · x = (−b ± √Δ)/(2a)",
  "Δ > 0 : 2 racines · Δ = 0 : racine double · Δ < 0 : aucune",
  "Δ~Discriminant~Compte les racines~b² − 4ac~Formule~Calcul de Δ~x₁, x₂~Solutions~(−b ± √Δ)/(2a)~Facteur~Produit nul~Un facteur est nul~Tableau de signes~Inéquation~Signe entre les racines",
  "Écrire l'équation sous forme a·x² + bx + c = 0|Calculer le discriminant|Comparer Δ à zéro|Calculer les racines ou factoriser|Dresser le tableau de signes pour une inéquation",
  "Oublier le signe de b dans Δ|Écrire (a + b)² = a² + b²|Négliger les conditions d'existence|Perdre une solution en divisant par x|Inverser le sens d'une inéquation",
  "x² − 5x + 6~Δ = 1, racines 2 et 3~Δ = −104~Aucune racine réelle~(x + 3)(x − 3)~x² − 9~Δ = 0~Racine double~x ≠ 2~Condition d'existence",
  "Δ > 0~Deux solutions~Δ = 0~Racine double",
  "a > 0~Parabole vers le haut~a < 0~Parabole vers le bas"))

# ============================================================ MA3
add("MA3", "Statistiques descriptives et interprétation", "Maths", ["Terminale"],
S("Une population est l'ensemble complet des individus étudiés ; un échantillon en est une partie prélevée pour être analysée."
  "|Un échantillon est représentatif lorsque sa composition reflète celle de la population pour les caractères pertinents."
  "|Un caractère quantitatif discret prend un nombre fini de valeurs, tandis qu'un caractère continu peut prendre toute valeur d'un intervalle."
  "|L'effectif d'une classe est le nombre d'individus qui appartiennent à cette classe ; l'effectif cumulé additionne les effectifs jusqu'à cette classe."
  "|La fréquence relative est l'effectif de la classe divisé par l'effectif total ; elle s'exprime en pourcentage après multiplication par 100."
  "|La moyenne est la somme des valeurs divisée par l'effectif total ; elle est sensible aux valeurs extrêmes."
  "|La médiane est la valeur qui partage la série ordonnée en deux moitiés de même effectif ; elle résiste aux valeurs aberrantes."
  "|Les quartiles Q₁ et Q₃ découpent la série en quatre parts ; l'intervalle interquartile contient la moitié centrale des observations."
  "|Le mode est la valeur la plus fréquente d'une série : c'est l'indicateur de position pertinent pour un caractère qualitatif."
  "|La variance mesure la dispersion autour de la moyenne ; l'écart-type en est la racine carrée et s'exprime dans la même unité que la donnée."
  "|L'histogramme convient à une variable continue, le diagramme en bâtons à une variable discrète et le camembert à une répartition en catégories."
  "|Toute présentation statistique doit indiquer la source, la taille de l'échantillon et les unités pour être interprétable."),
[QC("Quelle mesure de position résiste aux valeurs extrêmes ?", "La moyenne~La médiane~L'écart-type~L'étendue", 1,
     "La médiane dépend du rang des valeurs et non de leur amplitude."),
 QC("Comment calcule-t-on une fréquence relative ?", "Effectif × total~Effectif / effectif total~Total / effectif~Max − min", 1,
     "La fréquence est l'effectif de la classe divisé par l'effectif total."),
 QC("Quel graphique convient à une variable quantitative continue ?", "Le camembert~L'histogramme~Le diagramme en bâtons~L'arbre", 1,
     "L'histogramme représente les effectifs par classes de valeurs continues."),
 QC("Que mesure l'écart-type ?", "La tendance centrale~La dispersion autour de la moyenne~Le nombre d'individus~La corrélation", 1,
     "L'écart-type est la racine de la variance et quantifie la dispersion."),
 QC("Dans une série ordonnée de 9 valeurs, quelle est la position de la médiane ?", "La 4e valeur~La 5e valeur~La 9e valeur~La moyenne des 4e et 5e", 1,
     "Pour un effectif impair, la médiane est la valeur de rang (n+1)/2 = 5."),
 QC("Quel indicateur choisir pour un caractère qualitatif ?", "La moyenne~Le mode~L'écart-type~La médiane", 1,
     "Le mode est la seule mesure de position définie pour une variable qualitative."),
 QC("Que désigne l'intervalle interquartile ?", "L'écart min-max~L'écart entre Q₁ et Q₃~La moyenne des quartiles~La somme des effectifs", 1,
     "Il contient la moitié centrale des observations."),
 QT("Une série de temps de réponse en millisecondes est : 12, 15, 18, 20, 95. Calculer moyenne, médiane et écart, puis commenter.",
    "La somme vaut 12 + 15 + 18 + 20 + 95 = 160, donc la moyenne est 160/5 = 32 ms. La série est déjà ordonnée ; avec 5 valeurs, la médiane est la 3e, soit 18 ms. L'écart entre moyenne et médiane est de 14 ms, causé par la valeur extrême 95 ms qui tire la moyenne vers le haut. La médiane décrit mieux le temps de réponse typique ; on complétera par l'étendue (95 − 12 = 83 ms) et on investiguera la valeur aberrante avant toute conclusion sur la performance.",
    "On calcule les deux indicateurs, on explique l'écart par la valeur extrême et on recommande la médiane."),
 QT("Expliquer pourquoi un échantillon représentatif est indispensable avant de généraliser un résultat statistique.",
    "Un échantillon est représentatif lorsque sa composition reflète celle de la population pour les caractéristiques pertinentes. Si le prélèvement est biaisé, par exemple en n'interrogeant que les utilisateurs satisfaits, les estimateurs comme la moyenne ou la fréquence sont biaisés et toute généralisation est invalide, même avec un grand effectif. Un tirage aléatoire, une stratification et un effectif suffisant réduisent ce risque. On doit aussi indiquer la marge d'incertitude et le niveau de confiance pour quantifier la précision de l'estimation avant de conclure.",
    "On relie représentativité et absence de biais, puis on cite tirage aléatoire, stratification et marge d'incertitude.")],
C("La statistique descriptive résume une série par une tendance centrale et une dispersion adaptées au type de donnée.",
  "fréquence = effectif / total · σ = racine de la variance",
  "moyenne sensible aux extrêmes · médiane robuste · mode pour le qualitatif",
  "Population~Ensemble complet~Échantillon~Partie prélevée~Effectif~Nombre d'individus~Fréquence~Part du total~Moyenne~Somme divisée par n~Médiane~Valeur centrale~Écart-type~Dispersion",
  "Définir la population et l'échantillon|Trier les valeurs|Choisir les indicateurs pertinents|Construire le graphique adapté|Interpréter avec source et unités",
  "Utiliser la moyenne avec une valeur aberrante|Confondre effectif et fréquence|Choisir un camembert pour une variable continue|Omettre la taille de l'échantillon|Généraliser à partir d'un échantillon biaisé",
  "12;15;18;20;95~Moyenne 32, médiane 18~Q₁, Q₃~Moitié centrale~Fréquence~Effectif sur total~Histogramme~Variable continue~Mode~Classe la plus fréquente",
  "Effectif~Nombre absolu~Fréquence~Part relative",
  "Moyenne~Sensible aux extrêmes~Médiane~Résistante aux extrêmes"))

# ============================================================ MA4
add("MA4", "Probabilités et arbres pondérés", "Maths", ["Terminale"],
S("Une expérience aléatoire est une épreuve dont l'issue est incertaine mais dont l'univers des résultats possibles est connu."
  "|Un événement est une partie de l'univers ; sa probabilité est un nombre compris entre 0 et 1."
  "|Dans un univers fini équiprobable, la probabilité d'un événement est le nombre d'issues favorables divisé par le nombre total d'issues."
  "|Une loi de probabilité associe une probabilité à chaque issue ; la somme de toutes ces probabilités vaut 1."
  "|Deux événements incompatibles ne peuvent pas survenir simultanément : P(A ∪ B) = P(A) + P(B)."
  "|Deux événements indépendants vérifient P(A ∩ B) = P(A) × P(B) : la réalisation de l'un n'influence pas la probabilité de l'autre."
  "|La probabilité conditionnelle P(A sachant B) vaut P(A ∩ B)/P(B) lorsque P(B) est non nul."
  "|Un arbre pondéré représente les étapes successives d'une expérience ; on multiplie les probabilités le long d'une branche."
  "|La formule des probabilités totales somme les probabilités conditionnelles pondérées par celles des sous-groupes."
  "|La formule de Bayes inverse une probabilité conditionnelle et sert à interpréter un test de détection ou un diagnostic."
  "|Une variable aléatoire associe un nombre à chaque issue ; son espérance est la moyenne théorique à long terme."
  "|Les probabilités interviennent en STL pour modéliser un risque, un plan d'échantillonnage ou la fiabilité d'une mesure."),
[QC("Quelle est la probabilité d'un événement impossible ?", "0~0,5~1~2", 0,
     "Un événement impossible a une probabilité nulle."),
 QC("Dans un univers équiprobable, comment calculer une probabilité ?", "Issues favorites × total~Issues favorables / total~Total − issues~Une soustraction", 1,
     "P(A) = nombre d'issues favorables divisé par le nombre total d'issues."),
 QC("Que vérifient deux événements indépendants ?", "P(A∩B) = P(A)+P(B)~P(A∩B) = P(A)×P(B)~P(A) = P(B)~A et B incompatibles", 1,
     "L'indépendance se traduit par la multiplication des probabilités."),
 QC("Comment calcule-t-on une probabilité conditionnelle ?", "P(A∩B)/P(B)~P(A)/P(B)~P(B)/P(A)~P(A)+P(B)", 0,
     "P(A sachant B) = P(A ∩ B)/P(B), avec P(B) non nul."),
 QC("Sur un arbre pondéré, comment obtient-on la probabilité d'une branche ?", "En additionnant~En multipliant~En soustrayant~En divisant par 2", 1,
     "On multiplie les probabilités portées par les arcs successifs."),
 QC("À quoi sert la formule de Bayes ?", "À additionner les issues~À inverser une probabilité conditionnelle~À compter les événements~À tracer un histogramme", 1,
     "Bayes permet de calculer P(B sachant A) à partir de P(A sachant B)."),
 QC("Quelle est la somme des probabilités d'une loi complète ?", "0~0,5~1~2", 2,
     "Les probabilités de toutes les issues mutuellement exclusives et exhaustives somment à 1."),
 QT("Une urne contient 5 boules rouges et 3 boules bleues. On tire deux boules avec remise. Calculer la probabilité d'obtenir deux boules rouges.",
    "Il y a 8 boules au total. La probabilité de tirer une boule rouge est p = 5/8. Comme le tirage se fait avec remise, les deux événements sont indépendants et la probabilité de deux rouges vaut (5/8) × (5/8) = 25/64, soit environ 0,391. On peut aussi lire ce résultat sur un arbre pondéré : la branche rouge-rouge porte les probabilités 5/8 puis 5/8, et on les multiplie.",
    "On identifie l'indépendance liée au remisage, puis on multiplie les probabilités."),
 QT("Expliquer pourquoi la formule de Bayes est utile pour interpréter un test de dépistage.",
    "La sensibilité d'un test donne P(test positif sachant maladie) et sa spécificité donne P(test négatif sachant non-maladie). Or ce que souhaite connaître une personne, c'est P(maladie sachant test positif), qui est une probabilité inverse. La formule de Bayes combine la sensibilité, la prévalence de la maladie et la probabilité d'un test positif pour obtenir cette valeur. Si la maladie est rare, même un test très sensible peut produire beaucoup de faux positifs : la valeur prédictive positive reste modeste. Bayes évite donc de confondre la performance du test avec la probabilité réelle d'être malade.",
    "On oppose sensibilité et valeur prédictive positive, puis on montre le rôle de la prévalence.")],
C("Les probabilités modélisent l'aléa : arbre pour composer, Bayes pour inverser, espérance pour moyenniser.",
  "P(A∩B) = P(A)×P(B) si indépendance · P(A|B) = P(A∩B)/P(B)",
  "univers · équiprobabilité · arbre pondéré · probabilités totales · Bayes",
  "Univers~Issues possibles~Événement~Partie de l'univers~Indépendance~Produit des probabilités~Incompatibilité~Somme des probabilités~Arbre pondéré~Multiplication le long des branches~Conditionnelle~P(A ∩ B)/P(B)",
  "Définir l'univers et les événements|Choisir équiprobable ou pondéré|Construire l'arbre ou la formule|Multiplier le long des branches|Additionner les issues favorables",
  "Confondre indépendance et incompatibilité| additionner au lieu de multiplier sur une branche|Oublier de vérifier P(B) ≠ 0|Ignorer la prévalence dans un test|Croire que le passe influence un tirage avec remise",
  "5 rouges sur 8~p = 5/8~Deux tirages avec remise~25/64~Univers à 6 issues~p = 1/6~Loi complète~Somme = 1~Bayes~Probabilité inverse",
  "Indépendance~L'un n'influence pas l'autre~Incompatibilité~Impossible ensemble",
  "Avec remise~Indépendance~Sans remise~Probabilités modifiées"))

# ============================================================ PC1
add("PC1", "Lois de l'électricité et circuits électriques", "Physique-Chimie", ["1re"],
S("Un circuit électrique est un ensemble d'éléments reliés par des conducteurs, parcouru par un courant lorsque le circuit est fermé."
  "|L'intensité du courant se mesure en ampères avec un ampèremètre branché en série dans le circuit."
  "|La tension électrique entre deux points se mesure en volts avec un voltmètre branché en dérivation aux bornes du composant."
  "|La loi d'Ohm énonce que la tension U aux bornes d'un conducteur ohmique est proportionnelle à l'intensité I qui le traverse : U = R·I."
  "|La résistance R s'exprime en ohms et caractérise l'opposition du conducteur au passage du courant."
  "|Dans un circuit en série, l'intensité est la même en tout point et les tensions s'ajoutent : U_total = U₁ + U₂."
  "|Dans un circuit en dérivation, la tension est la même aux bornes de chaque branche et les intensités s'ajoutent : I_total = I₁ + I₂."
  "|La résistance équivalente de deux résistances en série vaut R = R₁ + R₂."
  "|La résistance équivalente de deux résistances en parallèle vérifie 1/R = 1/R₁ + 1/R₂."
  "|La puissance électrique consommée par un dipôle vaut P = U·I, et l'énergie consommée pendant une durée t vaut E = P·t."
  "|Un court-circuit correspond à une liaison de très faible résistance entre deux points : l'intensité devient très élevée et présente un danger."
  "|Un conducteur ohmique a une résistance constante à température constante ; une diode ou un moteur ne sont pas des conducteurs ohmiques."),
[QC("Comment branche-t-on un ampèremètre ?", "En dérivation~En série~Aux bornes de la source~N'importe comment", 1,
     "L'ampèremètre mesure l'intensité qui le traverse : il doit être inséré en série."),
 QC("Que donne la loi d'Ohm ?", "U = R/I~U = R·I~U = I/R~U = R + I", 1,
     "Pour un conducteur ohmique, la tension est le produit de la résistance par l'intensité."),
 QC("Dans un circuit en série, quelle grandeur est identique en tout point ?", "La tension~L'intensité~La puissance~La résistance", 1,
     "En série, aucun nouveau courant ne peut apparaître : l'intensité est la même partout."),
 QC("Comment se combinent deux résistances en parallèle ?", "R = R₁ + R₂~1/R = 1/R₁ + 1/R₂~R = R₁·R₂~R = (R₁+R₂)/2", 1,
     "En dérivation, les inverses des résistances s'additionnent."),
 QC("Quelle est l'unité de la résistance électrique ?", "Le volt~L'ampère~L'ohm~Le watt", 2,
     "La résistance se mesure en ohms, symbole Ω."),
 QC("Que se passe-t-il lors d'un court-circuit ?", "L'intensité devient très faible~L'intensité devient très élevée~La tension devient nulle~Le courant s'arrête", 1,
     "Une résistance très faible entraîne une intensité dangereuse selon I = U/R."),
 QC("Quelle est la puissance d'un dipôle traversé par 2 A sous 12 V ?", "6 W~14 W~24 W~48 W", 2,
     "P = U·I = 12 × 2 = 24 W."),
 QT("Deux résistances de 6 Ω et 3 Ω sont branchées en série sous une tension de 18 V. Calculer l'intensité et la tension aux bornes de chaque résistance.",
    "La résistance équivalente en série vaut R = 6 + 3 = 9 Ω. L'intensité est la même dans tout le circuit : I = U/R = 18/9 = 2 A. La tension aux bornes de la première résistance vaut U₁ = R₁·I = 6 × 2 = 12 V et celle de la deuxième U₂ = 3 × 2 = 6 V. On vérifie que U₁ + U₂ = 12 + 6 = 18 V, ce qui confirme le calcul.",
    "On calcule la résistance équivalente, puis l'intensité commune, puis chaque tension par la loi d'Ohm."),
 QT("Expliquer pourquoi un voltmètre doit être branché en dérivation et non en série.",
    "Le voltmètre mesure la différence de potentiel entre deux points : il doit donc être placé aux bornes du dipôle étudié, c'est-à-dire en dérivation. Il possède une très grande résistance interne pour ne pas prélever de courant et ne pas modifier le fonctionnement du circuit. S'il était branché en série, sa forte résistance s'ajouterait à celle du circuit, l'intensité chuterait fortement et la mesure serait faussée, voire le circuit ne fonctionnerait plus. À l'inverse, l'ampèremètre a une très faible résistance interne et se place en série.",
    "On relie le branchement à la grandeur mesurée et à la résistance interne de l'appareil.")],
C("Le courant se mesure en série, la tension en dérivation ; la loi d'Ohm relie tension, intensité et résistance.",
  "U = R·I · P = U·I · E = P·t",
  "série : I constante, U s'additionne · dérivation : U constante, I s'additionne",
  "U~Tension~Volts~I~Intensite~Ampères~R~Resistance~Ohms~P~Puissance~Watts~Série~I constant~Tensions additionnees~Dérivation~U constante~Intensites additionnees",
  "Dessiner le schema du circuit|Placer ampèremètre en série et voltmètre en dérivation|Fermer le circuit et relever les mesures|Calculer la résistance équivalente|Vérifier les lois de Kirchhoff",
  "Brancher l'ampèremètre en dérivation|Brancher le voltmètre en série|Oublier de fermer le circuit|Confondre tension et intensité|Laisser un court-circuit",
  "U = 18 V, R = 9 Ω~I = 2 A~R₁ = 6 Ω~U₁ = 12 V~R₂ = 3 Ω~U₂ = 6 V~P = 24 W~Sous 12 V et 2 A",
  "Circuit en série~Même intensité~Circuit en dérivation~Même tension",
  "Court-circuit~R très faible, I élevée~Circuit ouvert~I nulle"))

# ============================================================ PC2
add("PC2", "Cinématique et lois de Newton", "Physique-Chimie", ["1re"],
S("La cinématique décrit le mouvement d'un corps sans en rechercher les causes, à l'aide de grandeurs comme la position, la vitesse et l'accélération."
  "|Le mouvement rectiligne uniforme se caractérise par une vitesse constante : la position varie linéairement avec le temps selon x(t) = x₀ + v·t."
  "|Dans un mouvement rectiligne uniformément accéléré, l'accélération a est constante et la vitesse varie selon v(t) = v₀ + a·t."
  "|La position dans un mouvement uniformément accéléré s'écrit x(t) = x₀ + v₀·t + (1/2)·a·t²."
  "|L'accélération est la dérivée de la vitesse par rapport au temps, et la vitesse est la dérivée de la position."
  "|Sur un graphique position-temps, la pente de la courbe donne la vitesse instantanée."
  "|Sur un graphique vitesse-temps, la pente donne l'accélération et l'aire sous la courbe donne le déplacement."
  "|Le principe d'inertie énonce qu'un corps reste au repos ou en mouvement rectiligne uniforme si la somme des forces qui s'exercent sur lui est nulle."
  "|Le deuxième principe de Newton relie la somme des forces à l'accélération : ΣF = m·a, avec la masse en kilogrammes et l'accélération en mètres par seconde carrée."
  "|Le troisième principe énonce que deux corps exercent l'un sur l'autre des actions réciproques de même intensité et de sens opposés."
  "|Le poids d'un corps vaut P = m·g, avec g environ égal à 9,81 N/kg près de la surface terrestre."
  "|Les lois de Newton permettent d'analyser la chute libre, le freinage d'un véhicule ou le mouvement d'un ascenseur."),
[QC("Quelle grandeur donne la pente d'un graphique position-temps ?", "L'accélération~La vitesse~La force~La masse", 1,
     "La dérivée de la position par rapport au temps est la vitesse instantanée."),
 QC("Quelle est l'unité de l'accélération ?", "m/s~m/s²~N/kg~kg", 1,
     "L'accélération s'exprime en mètres par seconde carrée."),
 QC("Que devient la vitesse dans un mouvement rectiligne uniforme ?", "Elle augmente~Elle diminue~Elle reste constante~Elle s'annule", 2,
     "Uniforme signifie vitesse constante ; seule la position varie linéairement."),
 QC("Quelle est la formule du deuxième principe de Newton ?", "ΣF = m/a~ΣF = m·a~ΣF = a/m~ΣF = m + a", 1,
     "La somme des forces est égale au produit de la masse par l'accélération."),
 QC("Que vaut le poids d'une masse de 10 kg sur Terre ?", "9,81 N~10 N~98,1 N~981 N", 2,
     "P = m·g = 10 × 9,81 = 98,1 N."),
 QC("Que fournit l'aire sous un graphique vitesse-temps ?", "La vitesse~L'accélération~Le déplacement~La force", 2,
     "L'intégrale de la vitesse sur le temps donne le déplacement."),
 QC("Dans le troisième principe, les actions réciproques sont…", "De même sens et d'intensités différentes~De sens opposés et de même intensité~Nulles~Toujours verticales", 1,
     "Action et réaction ont même intensité, même droite d'action et des sens opposés."),
 QT("Unmobile part du repos avec une accélération constante de 2 m/s² pendant 5 s. Calculer sa vitesse finale et la distance parcourue.",
    "La vitesse finale vaut v = v₀ + a·t = 0 + 2 × 5 = 10 m/s. La distance parcourue vaut x − x₀ = v₀·t + (1/2)·a·t² = 0 + (1/2) × 2 × 25 = 25 m. On peut vérifier ce résultat sur un graphique vitesse-temps : la vitesse passe linéairement de 0 à 10 m/s, et l'aire du triangle formé vaut (1/2) × 5 × 10 = 25 m, ce qui confirme le calcul.",
    "On applique les équations du mouvement uniformément accéléré et on vérifie par l'aire sous la courbe."),
 QT("Expliquer le principe d'inertie et montrer comment il se déduit du deuxième principe de Newton.",
    "Le principe d'inertie affirme que si la somme des forces extérieures appliquées à un corps est nulle, alors son accélération est nulle : sa vitesse ne change ni en module ni en direction. Le corps reste donc au repos s'il était immobile, ou continue à se déplacer en ligne droite à vitesse constante s'il était en mouvement. Le deuxième principe ΣF = m·a contient ce résultat : en posant ΣF = 0 avec une masse non nulle, on obtient immédiatement a = 0. L'inertie n'est donc pas une force, mais la tendance d'un corps à conserver son état de mouvement ; la masse mesure cette inertie.",
    "On relie l'accélération nulle à l'absence de force résultante et on précise que l'inertie n'est pas une force.")],
C("La cinématique décrit le mouvement ; la dynamique l'explique par les forces, avec ΣF = m·a.",
  "x(t) = x₀ + v₀t + ½at² · v = v₀ + at · ΣF = m·a",
  "pente x-t = vitesse · pente v-t = accélération · P = m·g",
  "x(t)~Position~Fonction du temps~v(t)~Vitesse~Dérivée de x~a~Accélération~Dérivée de v~ΣF~Force résultante~Somme des forces~Poids~P = m·g~Inertie~Vitesse conservée~Sans force",
  "Choisir un repère et orienter l'axe|Relever les positions à differents instants|Tracer le graphique x(t) ou v(t)|Lire pente et aire|Appliquer ΣF = m·a",
  "Confondre vitesse et accélération|Oublier d'orienter l'axe|Prendre g en m/s² au lieu de N/kg|Mélanger poids et masse|Ignorer les frottements dans un bilan de forces",
  "a = 2 m/s², t = 5 s~v = 10 m/s~x = 25 m~m = 10 kg~P = 98,1 N~g ≈ 9,81 N/kg~v constant~a = 0",
  "Mouvement uniforme~Vitesse constante~Mouvement accéléré~Vitesse variable",
  "Poids~Force due à la gravité~Masse~Quantité de matière"))

# ============================================================ PC3
add("PC3", "Solutions aqueuses, pH et titrage", "Physique-Chimie", ["Terminale"],
S("Une solution aqueuse est un mélange homogène d'un soluté dissous dans de l'eau, appelée solvant."
  "|La concentration molaire d'une solution vaut c = n/V, où n est la quantité de matière du soluté en moles et V le volume de la solution en litres."
  "|La masse d'un soluté se calcule avec m = n·M, où M est la masse molaire exprimée en grammes par mole."
  "|Lors d'une dilution, la quantité de soluté est conservée : c₁·V₁ = c₂·V₂."
  "|Selon Brønsted, un acide est un donneur de protons H⁺ et une base est un accepteur de protons."
  "|Un couple acide-base est constitué d'un acide AH et de sa base conjuguée A⁻, qui diffèrent par un proton."
  "|Le pH d'une solution aqueuse est défini par pH = −log[H₃O⁺], où [H₃O⁺] est la concentration en ions oxonium."
  "|À 25 °C, une solution neutre a un pH de 7 ; une solution acide a un pH inférieur à 7 et une solution basique un pH supérieur à 7."
  "|L'échelle des pH est logarithmique : une diminution d'une unité de pH multiplie la concentration en H₃O⁺ par dix."
  "|Un indicateur coloré change de teinte sur une zone de virage étroite : le choix de l'indicateur dépend du pH à l'équivalence."
  "|Un titrage consiste à ajouter progressivement une solution titrante à une solution titrée jusqu'à l'équivalence, où les réactifs sont en proportions stœchiométriques."
  "|La manipulation des acides et des bases exige des gants, des lunettes et l'ajout de l'acide dans l'eau, jamais l'inverse."),
[QC("Que vaut la concentration molaire d'une solution ?", "c = V/n~c = n/V~c = n·V~c = m/V", 1,
     "La concentration molaire est la quantité de matière divisée par le volume de solution."),
 QC("Quel est le pH d'une solution neutre à 25 °C ?", "0~1~7~14", 2,
     "À 25 °C, l'eau pure a un pH de 7."),
 QC("Dans un couple acide-base selon Brønsted, la base est…", "Un donneur de protons~Un accepteur de protons~Un ion négatif~Un solvant", 1,
     "La base accepte un proton H⁺, l'acide le donne."),
 QC("Une solution de pH 3 a une concentration en H₃O⁺…", "Égale à celle de pH 4~Dix fois supérieure à celle de pH 4~Cent fois inférieure à celle de pH 4~Nulle", 1,
     "L'échelle étant logarithmique, un pH de 3 correspond à [H₃O⁺] = 10⁻³, soit dix fois 10⁻⁴."),
 QC("Que conserve-t-on lors d'une dilution ?", "La concentration~Le volume~La quantité de soluté~Le pH", 2,
     "La quantité de matière de soluté reste constante : c₁V₁ = c₂V₂."),
 QC("À quoi sert un indicateur coloré lors d'un titrage ?", "À accélérer la réaction~À repérer le virage proche de l'équivalence~À diluer la solution~À mesurer le volume", 1,
     "L'indicateur change de couleur dans une zone de virage choisie pour encadrer le pH d'équivalence."),
 QC("Comment préparer une solution acide en sécurité ?", "En versant l'eau dans l'acide~En versant l'acide dans l'eau~En mélangeant à sec~En chauffant au préalable", 1,
     "On verse toujours l'acide dans l'eau, lentement, car la dilution est exothermique."),
 QT("Une solution contient 0,20 mol de soluté dans 500 mL d'eau. Calculer sa concentration molaire, puis la concentration après dilution à 1,0 L.",
    "Le volume initial est V₁ = 500 mL = 0,500 L. La concentration initiale vaut c₁ = n/V₁ = 0,20/0,500 = 0,40 mol/L. Lors de la dilution à V₂ = 1,0 L, la quantité de soluté reste n = 0,20 mol, donc c₂ = 0,20/1,0 = 0,20 mol/L. On retrouve le même résultat avec c₁V₁ = c₂V₂ : 0,40 × 0,500 = c₂ × 1,0, d'où c₂ = 0,20 mol/L.",
    "On convertit le volume en litres, on calcule c₁ puis on applique la conservation de la quantité de matière."),
 QT("Expliquer le rôle de l'équivalence dans un titrage acide-base et comment la repérer expérimentalement.",
    "À l'équivalence, les réactifs ont été introduits dans les proportions exactes de la réaction : il ne reste ni acide ni base en excès, seuls les produits sont présents. Le pH à l'équivalence dépend de la force des couples mis en jeu : il vaut environ 7 pour un acide fort et une base forte. Expérimentalement, on repère l'équivalence par le virage d'un indicateur coloré dont la zone de virage encadre ce pH, ou plus précisément par le point d'inflexion de la courbe de pH en fonction du volume versé. On peut alors déduire la concentration inconnue de la solution titrée.",
    "On définit l'équivalence stœchiométrique et on décrit le virage ou la courbe de titrage.")],
C("Le pH mesure l'acidité d'une solution ; le titrage détermine une concentration grâce à l'équivalence.",
  "c = n/V · m = n·M · pH = −log[H₃O⁺] · c₁V₁ = c₂V₂",
  "acide = donneur de H⁺ · base = accepteur de H⁺ · predictat de virage",
  "Soluté~Dissous dans l'eau~Solution homogène~Concentration~Quantité sur volume~n/V~pH~Logarithme décimal~−log[H₃O⁺]~Acide~Donneur de protons~H⁺~Base~Accepteur de protons~Indicateur~Zone de virage~Choix du pH",
  "Choisir la verrerie et les solutions|Calculer la concentration attendue|Verser l'acide dans l'eau pour diluer|Verser la solution titrante goutte à goutte|Repérer le virage et calculer c",
  "Verser l'eau dans l'acide|Oublier de convertir les mL en L|Confondre acidité et concentration|Choisir un indicateur hors zone de virage|Arrêter le titrage après le virage",
  "n = 0,20 mol, V = 0,50 L~c = 0,40 mol/L~V final 1,0 L~c = 0,20 mol/L~pH 3~[H₃O⁺] = 10⁻³~pH 7~Solution neutre",
  "Acide~Donneur de protons~Base~Acceptrice de protons",
  "Dilution~Ajout de solvant~Titrage~Ajout reactif jusqu'equivalence"))

# ============================================================ PC4
add("PC4", "Énergie, travail et transferts thermiques", "Physique-Chimie", ["1re"],
S("Le travail d'une force constante est W = F·d·cos(α), où α est l'angle entre la force et le déplacement ; il s'exprime en joules."
  "|L'énergie cinétique d'un corps de masse m animé d'une vitesse v vaut E_c = (1/2)·m·v²."
  "|L'énergie potentielle de pesanteur à une hauteur h vaut E_p = m·g·h, avec g environ égal à 9,81 N/kg."
  "|L'énergie mécanique d'un système est la somme de son énergie cinétique et de son énergie potentielle."
  "|Le théorème de l'énergie cinétique énonce que la variation d'énergie cinétique est égale à la somme des travaux des forces."
  "|En l'absence de frottements, l'énergie mécanique se conserve au cours du mouvement."
  "|Les frottements transforment une partie de l'énergie mécanique en énergie thermique : l'énergie totale est conservée mais l'énergie mécanique diminue."
  "|La quantité de chaleur échangée par un corps vaut Q = m·c·ΔT, où c est la capacité thermique massique."
  "|La conduction est un transfert thermique par contact direct, la convection par déplacement de fluide et le rayonnement par ondes électromagnétiques."
  "|La puissance est le rapport d'une énergie ou d'un travail sur la durée : P = W/t, en watts."
  "|Le rendement d'une machine est le rapport entre l'énergie utile fournie et l'énergie consommée ; il est toujours inférieur à 1."
  "|Ces notions servent en STL à analyser un bilan énergétique, un échauffement de réacteur ou les pertes d'une installation."),
[QC("Quelle est l'unité du travail d'une force ?", "Le watt~Le joule~Le newton~Le pascal", 1,
     "Travail et énergie s'expriment en joules, symbole J."),
 QC("Que vaut l'énergie cinétique d'un corps de masse m et de vitesse v ?", "m·v~½·m·v²~m·v²~m·g·h", 1,
     "L'énergie cinétique vaut la moitié du produit de la masse par le carré de la vitesse."),
 QC("Dans un mouvement sans frottements, que se passe-t-il ?", "L'énergie mécanique diminue~L'énergie mécanique se conserve~L'énergie cinétique s'annule~La vitesse devient nulle", 1,
     "Sans dissipation, la somme E_c + E_p reste constante."),
 QC("Quel mode de transfert thermique met en jeu un fluide en mouvement ?", "La conduction~La convection~Le rayonnement~L'isolation", 1,
     "La convection correspond à un transport de chaleur par déplacement de matière fluide."),
 QC("Une masse de 2 kg est à 10 m de hauteur. Quelle est son énergie potentielle ?", "20 J~98 J~196 J~200 J", 2,
     "E_p = m·g·h = 2 × 9,81 × 10 = 196,2 J, soit environ 196 J."),
 QC("Comment calcule-t-on une puissance ?", "P = W·t~P = W/t~P = t/W~P = W + t", 1,
     "La puissance est l'énergie transférée par unité de temps."),
 QC("Un rendement peut-il être supérieur à 1 ?", "Oui, pour une machine parfaite~Non, les pertes sont inévitables~Oui, si la machine est neuve~Seulement pour le rayonnement", 1,
     "Le rendement est toujours strictement inférieur à 1 à cause des dissipations."),
 QT("Un corps de 2 kg tombe sans frottements depuis une hauteur de 5 m. Calculer son énergie potentielle initiale et sa vitesse au sol.",
    "L'énergie potentielle initiale vaut E_p = m·g·h = 2 × 9,81 × 5 = 98,1 J. Au sol, l'énergie potentielle est nulle et toute cette énergie s'est transformée en énergie cinétique : ½·m·v² = 98,1, donc v² = 2 × 98,1/2 = 98,1 et v = √98,1 ≈ 9,9 m/s. On retrouve le résultat par v = √(2gh) = √(2 × 9,81 × 5) ≈ 9,9 m/s.",
    "On applique la conservation de l'énergie mécanique, puis on isole la vitesse."),
 QT("Expliquer pourquoi l'énergie mécanique diminue lors d'un freinage alors que l'énergie totale est conservée.",
    "Pendant le freinage, la force de frottement entre les plaquettes et le disque est opposée au déplacement : son travail est négatif. Le théorème de l'énergie cinétique indique donc une diminution de l'énergie cinétique du véhicule. L'énergie perdue n'a pas disparu : elle a été transformée en énergie thermique dans les freins et les pneus, puis transférée à l'air environnant. L'énergie totale du système élargi reste constante, conformément au principe de conservation de l'énergie, mais l'énergie mécanique utilisable a diminué : c'est une dissipation, responsable d'un rendement inférieur à 1.",
    "On relie le travail négatif des frottements à la dissipation thermique et à la conservation globale.")],
C("L'énergie ne se crée ni ne se détruit : elle se transforme, et les frottements la dissipent sous forme thermique.",
  "W = F·d·cos(α) · E_c = ½mv² · E_p = mgh · Q = mcΔT",
  "E_méca = E_c + E_p · rendement = énergie utile / énergie consommée",
  "Travail~Force sur distance~F·d·cos α~E_c~Energie cinétique~½mv²~E_p~Energie potentielle~mgh~Q~Chaleur~mcΔT~Puissance~Energie sur duree~W/t~Rendement~Utile sur consomme~Inférieur à 1",
  "Choisir le système et le repère|Identifier les forces et leurs travaux|Calculer E_c et E_p|Appliquer la conservation ou le bilan|Estimer les dissipations et le rendement",
  "Confondre masse et poids|Oublier le cosinus dans le travail|Prendre g en m/s²|Négliger les frottements dans un bilan réel|Additionner des énergies et des puissances",
  "m = 2 kg, h = 5 m~E_p = 98,1 J~v ≈ 9,9 m/s~Q = mcΔT~Eau : c ≈ 4180 J/(kg·K)~P = W/t~Rendement 0,8~80 % d'énergie utile",
  "Conduction~Contact direct~Convection~Fluide en mouvement",
  "Travail moteur~Positif~Travail des frottements~Negatif"))

# ============================================================ SV1
add("SV1", "La cellule, unité du vivant", "SVT", ["1re"],
S("La théorie cellulaire énonce que tout être vivant est constitué d'une ou plusieurs cellules, unités structurales et fonctionnelles du vivant."
  "|Les cellules procaryotes, comme les bactéries, ne possèdent pas de noyau : leur ADN est localisé dans un nucléoïde."
  "|Les cellules eucaryotes possèdent un noyau délimité par une enveloppe et des organites spécialisés."
  "|La membrane plasmique est une bicouche lipidique qui contrôle les échanges entre la cellule et son environnement."
  "|Le cytoplasme est le milieu intérieur de la cellule, siège de nombreuses réactions métaboliques."
  "|Le noyau contient l'ADN organisé en chromosomes et dirige la synthèse des protéines."
  "|Les mitochondries assurent la respiration cellulaire et produisent l'ATP ; les ribosomes synthétisent les protéines."
  "|Le réticulum endoplasmique et l'appareil de Golgi participent à la synthèse, à la modification et au transport des protéines."
  "|La cellule végétale possède en plus une paroi de cellulose, des chloroplastes et une vacuole."
  "|Les cellules se spécialisent en types variés : neurones, muscles, globules rouges, cellules épithéliales."
  "|Des cellules spécialisées s'organisent en tissus, puis en organes au sein d'un organisme multicellulaire."
  "|L'observation au microscope et le respect de l'homéostasie sont au cœur des pratiques de biologie en STL."),
[QC("Quelle est l'unité structurale et fonctionnelle du vivant ?", "L'atome~La cellule~L'organe~La molécule", 1,
     "La théorie cellulaire fait de la cellule l'unité de base des êtres vivants."),
 QC("Quelle différence oppose procaryotes et eucaryotes ?", "Les procaryotes n'ont pas de membrane~Les procaryotes n'ont pas de noyau~Les eucaryotes n'ont pas d'ADN~Aucune différence", 1,
     "Les procaryotes possèdent une membrane mais pas de noyau véritable."),
 QC("Quel organite produit l'essentiel de l'ATP ?", "Le ribosome~La mitochondrie~Le Golgi~La vacuole", 1,
     "La mitochondrie est le siège de la respiration cellulaire aérobie."),
 QC("Que contrôle la membrane plasmique ?", "La synthèse d'ADN~Les échanges avec l'environnement~La photosynthèse~La Division cellulaire", 1,
     "La membrane plasmique est sélective et régule les entrées et sorties."),
 QC("Quel organite est propre à la cellule végétale ?", "La mitochondrie~Le chloroplaste~Le ribosome~Le noyau", 1,
     "Le chloroplaste contient la chlorophylle et assure la photosynthèse."),
 QC("Où sont synthétisées les protéines ?", "Sur les ribosomes~Dans le noyau~Dans la vacuole~Dans la paroi", 0,
     "Les ribosomes assurent la traduction de l'ARN messager en protéine."),
 QC("Quel ensemble de cellules forme un tissu ?", "Des cellules identiques ou complémentaires associées~Des organes isoles~Des molecules d'ADN~Des organismes différents", 0,
     "Un tissu regroupe des cellules qui associent leurs fonctions."),
 QT("Comparer une cellule animale et une cellule végétale en précisant les structures communes et propres.",
    "Les deux types de cellules possèdent une membrane plasmique, un cytoplasme, un noyau, des mitochondries, des ribosomes, un réticulum endoplasmique et un appareil de Golgi. La cellule végétale s'en distingue par une paroi rigide de cellulose, des chloroplastes qui réalisent la photosynthèse et une grande vacuole qui maintient la turgescence. La cellule animale possède souvent des centres de organisation microtubulaire et une membrane plus souple. Ces différences traduisent des modes de vie distincts : la cellule végétale est fixe et autotrophe, la cellule animale est généralement mobile et hétérotrophe.",
    "On cite les structures communes, puis les trois structures propres aux végétaux, en reliant forme et fonction."),
 QT("Expliquer pourquoi la membrane plasmique est essentielle au maintien de l'homéostasie.",
    "La membrane plasmique sépare le milieu intérieur de la cellule du milieu extérieur tout en restant sélectivement perméable. Elle laisse entrer les nutriments, l'eau et les ions nécessaires, évacue les déchets et empêche l'entrée de substances indésirables. Des protéines membranaires assurent des transports passifs ou actifs, souvent couplés à la consommation d'ATP, et des récepteurs transmettent les signaux du milieu. En régulant finement ces échanges, la membrane maintient des concentrations ioniques, un pH et un volume cellulaire stables : c'est l'homéostasie, condition du bon fonctionnement des enzymes et de la cellule.",
    "On relie la perméabilité sélective, les transports et les récepteurs à la stabilité du milieu intérieur.")],
C("La cellule est le lieu de toutes les fonctions du vivant ; ses organites se partagent les tâches.",
  "cellule = membrane + cytoplasme + ADN (et organites chez les eucaryotes)",
  "procaryote sans noyau · mitochondrie ATP · ribosome protéines · chloroplaste photosynthèse",
  "Membrane~Bicouche lipidique~Echanges selectifs~Noyau~ADN et chromosomes~Controle~Mitochondrie~Respiration cellulaire~ATP~Ribosome~Synthese proteique~Traduction~Chloroplaste~Photosynthese~Cellule végétale~Paroi de cellulose~Rigidité",
  "Observer la cellule au microscope|Repérer membrane, cytoplasme et noyau|Identifier les organites visibles|Comparer avec une cellule d'un autre type|Relier chaque structure à sa fonction",
  "Confondre membrane et paroi|Croire que les bactéries ont un noyau|Attribuer la photosynthèse aux mitochondries|Oublier que le ribosome n'a pas de membrane|Négliger le rôle de la vacuole",
  "Bactérie~Procaryote~Pas de noyau~Cellule vegetale~Chloroplaste et paroi~Mitochondrie~ATP~Ribosome~Proteines~Noyau~ADN",
  "Cellule animale~Pas de paroi~Cellule vegetale~Paroi et chloroplastes",
  "Procaryote~ADN dans le nucleoide~Eucaryote~ADN dans le noyau"))

# ============================================================ SV2
add("SV2", "Métabolisme cellulaire et respiration", "SVT", ["1re"],
S("Le métabolisme désigne l'ensemble des réactions chimiques qui se déroulent dans une cellule."
  "|L'anabolisme construit des molécules complexes à partir de molécules simples et consomme de l'énergie."
  "|Le catabolisme dégrade des molécules complexes en molécules plus simples et libère de l'énergie."
  "|L'ATP est la monnaie énergétique de la cellule : son hydrolyse en ADP et phosphate libère l'énergie nécessaire aux réactions."
  "|La glycolyse est la première étape de la respiration : elle dégrade le glucose en deux molécules de pyruvate dans le cytoplasme."
  "|En présence d'oxygène, le pyruvate entre dans la mitochondrie et alimente le cycle de Krebs."
  "|La chaîne respiratoire, située sur la membrane interne des mitochondries, produit la majeure partie de l'ATP grâce à l'oxygène."
  "|Le bilan de la respiration aérobie est : glucose + oxygène → dioxyde de carbone + eau + énergie sous forme d'ATP."
  "|En absence d'oxygène, la fermentation permet de régénérer l'ATP de la glycolyse mais produit beaucoup moins d'énergie."
  "|La photosynthèse est un processus anabolique : les plantes utilisent la lumière pour synthétiser des glucides à partir de CO₂ et d'eau."
  "|Les enzymes catalysent ces réactions en abaissant l'énergie d'activation, sans être consommées."
  "|Les nutriments glucidiques, lipidiques et protéiques alimentent ces voies métaboliques selon les besoins de l'organisme."),
[QC("Qu'appelle-t-on monnaie énergétique de la cellule ?", "L'ADN~L'ATP~Le glucose~L'eau", 1,
     "L'ATP stocke et transmet l'énergie utilisable par les réactions cellulaires."),
 QC("Quel processus construit des molécules complexes en consommant de l'énergie ?", "Le catabolisme~L'anabolisme~La fermentation~La glycolyse", 1,
     "L'anabolisme est une voie de synthèse ; le catabolisme est une voie de dégradation."),
 QC("Où se déroule la glycolyse ?", "Dans le noyau~Dans le cytoplasme~Dans la membrane~Dans le chloroplaste", 1,
     "La glycolyse est cytoplasmique et ne nécessite pas d'oxygène."),
 QC("Quel est le rôle de l'oxygène dans la respiration ?", "Il fournit de l'énergie directement~Il est le dernier accepteur d'electrons~Il dégrade le glucose~Il produit du CO₂", 1,
     "L'oxygène accepte les électrons à la fin de la chaîne respiratoire et forme de l'eau."),
 QC("Que produit principalement la fermentation ?", "Beaucoup d'ATP~Peu d'ATP et des produits comme l'ethanol~De l'oxygène~Des protéines", 1,
     "La fermentation ne donne que l'ATP de la glycolyse, soit deux molécules par glucose."),
 QC("Quel organite assure l'essentiel de la production d'ATP aérobie ?", "Le ribosome~La mitochondrie~Le Golgi~La vacuole", 1,
     "Le cycle de Krebs et la chaîne respiratoire ont lieu dans la mitochondrie."),
 QC("Comment une enzyme agit-elle ?", "En étant consommée~En abaissant l'énergie d'activation~En augmentant la température~En changeant l'équilibre", 1,
     "L'enzyme accélère la réaction sans être consommée ni déplacer l'équilibre."),
 QT("Décrire les trois grandes étapes de la respiration aérobie du glucose et indiquer où elles ont lieu.",
    "La première étape est la glycolyse, dans le cytoplasme : le glucose est découpé en deux pyruvates avec production nette de deux ATP. La deuxième étape est le cycle de Krebs, dans la matrice mitochondriale : les pyruvates sont oxydés complètement en dioxyde de carbone, produisant des transporteurs d'électrons. La troisième étape est la chaîne respiratoire, sur la membrane interne des mitochondries : les électrons sont transférés à l'oxygène, ce qui alimente la synthèse de la majorité des ATP et forme de l'eau. Au total, la respiration aérobie libère beaucoup plus d'énergie que la fermentation.",
    "On cite glycolyse, cycle de Krebs et chaîne respiratoire avec leur localisation et leur produit principal."),
 QT("Expliquer pourquoi la fermentation est moins rentable que la respiration aérobie.",
    "Lors de la fermentation, le glucose n'est dégradé que jusqu'au pyruvate ou à des dérivés comme l'éthanol ou le lactate. La majeure partie de l'énergie chimique reste stockée dans ces produits de fermentation : la cellule ne récupère que les deux ATP produits par la glycolyse. En respiration aérobie, l'oxydation complète jusqu'au CO₂ et à l'eau permet d'extraire l'énergie restante grâce au cycle de Krebs et à la chaîne respiratoire, pour un rendement bien supérieur. La fermentation présente néanmoins l'avantage de fonctionner sans oxygène et de régénérer rapidement les molécules nécessaires à la glycolyse.",
    "On compare le degré d'oxydation du glucose et le nombre d'ATP obtenus dans les deux voies.")],
C("Le métabolisme couple des réactions de dégradation qui libèrent de l'énergie à des réactions de synthèse qui en consomment.",
  "glucose + O₂ → CO₂ + H₂O + ATP",
  "glycolyse · cycle de Krebs · chaîne respiratoire · fermentation · photosynthèse",
  "Anabolisme~Synthèse~Consomme de l'energie~Catabolisme~Degradation~Libere de l'energie~ATP~Monnaie energetique~Hydrolyse en ADP~Glycolyse~Glucose en pyruvate~Cytoplasme~Cycle de Krebs~Oxydation~Mitochondrie~Chaîne respiratoire~Oxygene~ATP",
  "Identifier la voie metabolique et son besoin en oxygene|Localiser les etapes dans la cellule|Suivre le devenir du carbone|Compter les ATP produits|Comparer avec une autre voie",
  "Croire que la glycolyse a besoin d'oxygene|Confondre anabolisme et catabolisme|Placer le cycle de Krebs dans le cytoplasme|Dire que l'enzyme est consommée|Oublier la fermentation",
  "Glycolyse~2 ATP~Cycle de Krebs~CO₂~Chaîne respiratoire~O₂ en H₂O~Fermentation~Ethanol ou lactate~Photosynthèse~CO₂ + lumière en glucide",
  "Respiration aérobie~Avec oxygene~Fermentation~Sans oxygene",
  "Anabolisme~Construit~Catabolisme~Degrade"))

# ============================================================ SV3
add("SV3", "ADN, gènes et hérédité", "SVT", ["Terminale"],
S("L'ADN est une macromolécule en double hélice constituée de deux chaînes de nucléotides complémentaires."
  "|Chaque nucléotide comprend un groupement phosphate, un sucre désoxyribose et une base azotée."
  "|Les bases adénine et thymine s'apparient entre elles, de même que la guanine et la cytosine."
  "|Un gène est une portion d'ADN qui porte l'information nécessaire à la synthèse d'une protéine ou d'un ARN."
  "|Les gènes sont portés par des chromosomes, situés dans le noyau des cellules eucaryotes."
  "|La mitose produit deux cellules filles génétiquement identiques à la cellule mère, avec le même nombre de chromosomes."
  "|La méiose réduit de moitié le nombre de chromosomes et produit des cellules reproductrices génétiquement différentes."
  "|Un allèle est une version différente d'un même gène ; un individu diploïde porte deux allèles pour chaque gène."
  "|Le génotype désigne l'ensemble des allèles d'un individu, tandis que le phénotype correspond à ses caractères observables."
  "|Un allèle dominant s'exprime même à l'état hétérozygote, alors qu'un allèle récessif ne s'exprime qu'à l'état homozygote."
  "|La mutation est une modification durable de la séquence d'ADN : elle peut être neutre, nuisible ou favorable."
  "|L'expression d'un gène passe par la transcription en ARN messager puis par la traduction en protéine."),
[QC("Quelle base s'apparie avec l'adénine dans l'ADN ?", "La cytosine~La guanine~La thymine~L'uracile", 2,
     "A s'apparie avec T, et G avec C ; l'uracile appartient à l'ARN."),
 QC("Qu'est-ce qu'un gène ?", "Une cellule~Une portion d'ADN portant une information~Un organite~Une protéine", 1,
     "Le gène est un segment d'ADN qui code une information génétique."),
 QC("Quel est le résultat de la mitose ?", "Quatre cellules haploïdes~Deux cellules identiques~Une cellule sans ADN~Deux cellules differentes", 1,
     "La mitose conserve le nombre de chromosomes et l'information génétique."),
 QC("Quel rôle joue la méiose ?", "Produire des cellules reproductrices~Réparer l'ADN~Synthétiser des protéines~Produire de l'ATP", 0,
     "La méiose réduit le nombre de chromosomes et génère de la diversité génétique."),
 QC("Un individu hétérozygote porte…", "Deux allèles identiques~Deux allèles différents~Un seul allèle~Aucun allèle", 1,
     "Hétérozygote signifie que les deux allèles d'un gène sont différents."),
 QC("Qu'appelle-t-on phénotype ?", "L'ensemble des allèles~Les caractères observables~Le nombre de chromosomes~La séquence d'ADN", 1,
     "Le phénotype est l'expression visible ou mesurable du génotype dans un environnement donné."),
 QC("Quelle est la suite correcte de l'expression d'un gène ?", "Traduction puis transcription~Transcription puis traduction~ADN puis protéine puis ARN~Mitose puis méiose", 1,
     "L'ADN est transcrit en ARN messager, puis celui-ci est traduit en protéine."),
 QT("Pourquoi la méiose est-elle indispensable à la reproduction sexuée ?",
    "La méiose réduit le nombre de chromosomes de 2n à n dans les gamètes. Lors de la fécondation, la fusion de deux gamètes restaure le nombre diploïde 2n chez l'embryon : sans cette réduction, le nombre de chromosomes doublerait à chaque génération. De plus, lors de la méiose, les brassages entre chromosomes homologues et la répartition aléatoire des chromosomes créent de nouvelles combinaisons d'allèles. Cette diversité génétique est la matière première de l'évolution et explique que les enfants d'une même famille soient différents.",
    "On mentionne la réduction chromatique, la restauration à la fécondation et le brassage génétique."),
 QT("Un allèle récessif ne s'exprime pas chez un individu hétérozygote. Expliquer pourquoi, puis donner un exemple.",
    "Chez un hétérozygote Aa, l'allèle dominant A commande la production d'une protéine fonctionnelle en quantité suffisante : le phénotype correspond à l'allèle dominant. L'allèle récessif a est masqué, bien qu'il soit présent dans le génotype et transmissible à la descendance. Il ne s'exprime que chez l'homozygote récessif aa, où aucune copie fonctionnelle n'est disponible. Par exemple, dans la couleur des graines de pois étudiée par Mendel, l'allèle dominant pour la couleur jaune masque l'allèle récessif vert : un individu Aa a des graines jaunes mais peut transmettre l'allèle vert à ses descendants.",
    "On explique la dominance par la présence d'une copie fonctionnelle et on illustre par un exemple mendélien.")],
C("L'information génétique est portée par l'ADN, transmise par les chromosomes et exprimée via ARN et protéines.",
  "A–T et G–C · ADN → ARN → protéine",
  "mitose = identique · méiose = haploïde et diversité · génotype ≠ phénotype",
  "ADN~Double helice~Nucleotides~Base~Appariement complementaire~A-T et G-C~Gene~Portion d'ADN~Code une proteine~Chromosome~Support des genes~Dans le noyau~Mitose~Cellules identiques~2n conservé~Méiose~Gamètes haploïdes~n",
  "Repérer le support de l'information génétique|Identifier les appariements de bases|Distinguer mitose et méiose|Raisonner sur les allèles et le phénotype|Suivre transcription et traduction",
  "Apparier A avec C|Confondre génotype et phénotype|Croire qu'un allèle récessif disparaît|Placer la traduction avant la transcription|Oublier que l'ADN est dans le noyau",
  "A-T~Deux liaisons hydrogene~G-C~Trois liaisons hydrogene~Aa~Heteroxygote~AA~Homozygote dominant~aa~Homozygote recessif~2n~Cellule diploide~n~Gamete haploide",
  "Génotype~Allèles portés~Phénotype~Caractères observables",
  "Mitose~Identique~Méiose~Diversifiée"))

# ============================================================ SV4
add("SV4", "Biodiversité et évolution du vivant", "SVT", ["Terminale"],
S("La biodiversité désigne la variété des formes de vie à tous les niveaux : génétique, spécifique et écosystémique."
  "|La diversité génétique correspond à la variété des allèles et des génotypes au sein d'une même population."
  "|La diversité spécifique est le nombre d'espèces présentes dans un milieu donné."
  "|La diversité écosystémique concerne la variété des milieux et des interactions entre êtres vivants."
  "|Une espèce est un ensemble d'individus qui peuvent se reproduire entre eux et donner des descendants fertiles."
  "|La classification biologique organise les êtres vivants en catégories emboîtées : espèce, genre, famille, ordre, classe, embranchement, règne."
  "|Un arbre phylogénétique représente les liens de parenté entre espèces à partir de caractères homologues."
  "|Les mutations et les brassages génétiques produisent des variations héréditaires au sein des populations."
  "|La sélection naturelle favorise les individus porteurs de caractères avantageux dans un environnement donné."
  "|L'adaptation est un caractère qui augmente la survie ou la reproduction dans un milieu, résultat de la sélection sur plusieurs générations."
  "|Les activités humaines, comme la destruction d'habitats ou la surexploitation, entraînent une érosion de la biodiversité."
  "|La préservation des milieux, les aires protégées et la conservation des ressources génétiques sont des réponses à cette érosion."),
[QC("Quels sont les trois niveaux de la biodiversité ?", "Cellule, tissu, organe~Génétique, spécifique, écosystémique~Individu, famille, espèce~ADN, ARN, protéine", 1,
     "On distingue la diversité des gènes, des espèces et des écosystèmes."),
 QC("Quelle est la définition d'une espèce ?", "Des individus de même couleur~Des individus qui peuvent se reproduire et donner des descendants fertiles~Des individus du même genre~Des individus qui vivent ensemble", 1,
     "La fécondité des descendants est le critère biologique classique de l'espèce."),
 QC("Que représente un arbre phylogénétique ?", "Le nombre d'individus~Les liens de parenté entre espèces~La taille des cellules~Le climat d'une région", 1,
     "Il montre les relations d'ascendance et de parenté entre taxons."),
 QC("Quelle est la source première des variations héréditaires ?", "La sélection naturelle~Les mutations~L'adaptation~La concurrence", 1,
     "Les mutations modifient l'ADN et créent de nouveaux allèles."),
 QC("Que favorise la sélection naturelle ?", "Les individus les plus forts physiquement~Les caractères avantageux dans un milieu donné~Toutes les mutations~Les individus les plus âgés", 1,
     "La sélection retient les caractères qui améliorent survie et reproduction dans un contexte donné."),
 QC("Quel danger majeur pèse sur la biodiversité actuelle ?", "L'augmentation du nombre d'espèces~La destruction des habitats~La stabilité des climats~L'absence de mutations", 1,
     "La perte et la fragmentation des habitats sont des causes majeures d'érosion de la biodiversité."),
 QC("Quel caractère est homologue ?", "Un trait identique par convergence~Un trait hérité d'un ancêtre commun~Une couleur identique due au milieu~Une taille comparable", 1,
     "Les caractères homologues partagent une origine évolutive commune."),
 QT("Distinguer sélection naturelle et adaptation, et montrer leur lien.",
    "La sélection naturelle est un mécanisme : dans une population, les individus porteurs de caractères avantageux dans un environnement donné survivent et se reproduisent davantage, transmettant plus souvent leurs allèles. L'adaptation est le résultat de ce mécanisme : c'est le caractère, morphologique, physiologique ou comportemental, qui rend l'individu mieux adapté à son milieu. La sélection agit sur des variations déjà présentes, issues de mutations et de brassages, et non sur un besoin ressenti. Répétée sur de nombreuses générations, elle accumule les caractères favorables et façonne l'espèce.",
    "On sépare le mécanisme du résultat et on insiste sur le rôle des variations préexistantes."),
 QT("Expliquer pourquoi la diversité génétique d'une population est importante pour sa survie à long terme.",
    "Une forte diversité génétique offre un éventail large d'allèles et de combinaisons. Si l'environnement change, par exemple avec l'arrivée d'un pathogène ou une modification du climat, certains individus porteront par hasard des caractères leur permettant de résister et de se reproduire : la population peut alors évoluer. À l'inverse, une population génétiquement pauvre, issue par exemple d'un goulet d'étranglement, réagit de manière uniforme : une seule menace peut toucher tous les individus et entraîner l'extinction locale. C'est pourquoi la conservation des ressources génétiques, y compris chez les espèces domestiques, est un enjeu majeur.",
    "On relie la variété des allèles à la capacité d'évolution face à un changement environnemental.")],
C("L'évolution agit sur des variations héréditaires : la sélection naturelle façonne des adaptations au fil des générations.",
  "variation + hérédité + sélection = évolution",
  "biodiversité génétique, spécifique, écosystémique · espèce · arbre phylogénétique",
  "Biodiversité~Variété du vivant~Trois niveaux~Gene~Diversité des allèles~Population~Espece~Individus interfeconds~Descendants fertiles~Mutation~Nouvel allèle~Variation heritable~Selection naturelle~Survie et reproduction~Avantage~Adaptation~Caractere favorable~Resultat",
  "Définir le niveau de biodiversité étudié|Identifier les variations présentes|Relier un caractère à un avantage|Construire ou lire un arbre phylogénétique|Proposer des mesures de conservation",
  "Confondre adaptation et besoin|Croire que la sélection crée les mutations|Utiliser l'espèce comme synonyme de genre|Ignorer l'impact des activités humaines|Prendre une ressemblance pour une homologue",
  "3 niveaux~Genetique, specifique, ecosystemique~Espèce~Descendants fertiles~Mutation~Variation~Selection~Avantage reproductif~Aire protegee~Conservation",
  "Sélection naturelle~Mécanisme~Adaptation~Résultat",
  "Caractère homologue~Ancêtre commun~Caractère analogue~Convergence"))

# ============================================================ AN1
add("AN1", "English grammar: present simple and daily routines", "Anglais", ["1re"],
S("The present simple tense describes habits, routines and general truths."
  "|With third person singular, the verb takes an -s or -es ending: she works, he goes, it watches."
  "|Negation uses do not or does not followed by the base form: he does not smoke."
  "|Questions use do or does before the subject: does she work in a laboratory?"
  "|Frequency adverbs such as always, often, usually, sometimes and never are placed before the main verb."
  "|The verb to be is irregular: I am, you are, he is, we are, they are."
  "|There is and there are are used to say that something exists or is present in a place."
  "|The modal can expresses ability: I can use a microscope, she cannot prepare a solution."
  "|Countable nouns take a or an in the singular, while uncountable nouns are used without an article."
  "|Laboratory vocabulary includes beaker, flask, pipette, balance, oven, microscope and fume cupboard."
  "|The pronunciation of the third person -s ending is /s/, /z/ or /ɪz/, and a common mistake is to add -s after does: the correct form is does not work."
  "|Mastering the present simple is essential to describe a procedure or a daily routine in a laboratory report."),
[QC("When do we use the present simple?", "For past events~For habits and routines~For future plans only~For completed actions", 1,
     "The present simple describes habits, routines and general truths."),
 QC("What is the correct third person singular form?", "He work~He works~He working~He worked", 1,
     "The verb takes -s in the third person singular: he works."),
 QC("Which sentence is correct?", "She don't like it~She doesn't like it~She isn't like it~She not like it", 1,
     "Negation with third person singular uses does not followed by the base form."),
 QC("Where is the frequency adverb placed?", "After the verb~Before the main verb~At the end only~At the beginning only", 1,
     "Adverbs of frequency generally come before the main verb: she usually works."),
 QC("Which form is correct with 'there'?", "There is two beakers~There are two beakers~There have two beakers~There is beakers", 1,
     "There are is used with a plural countable noun."),
 QC("What does 'can' express?", "Obligation~Ability~Past time~Negation", 1,
     "Can expresses ability: I can measure the temperature."),
 QC("Which word is a laboratory equipment?", "Furnace~Microscope~Armchair~Yesterday", 1,
     "A microscope is a standard laboratory instrument."),
 QT("Correct the following sentences and explain each correction: 'He don't use a pipette. She go to the lab everyday. There is three flasks.'",
    "'He don't use a pipette' becomes 'He doesn't use a pipette': with third person singular, negation requires does not and the base form. 'She go to the lab everyday' becomes 'She goes to the lab every day': the verb takes -s, and 'every day' is written as two words. 'There is three flasks' becomes 'There are three flasks' because the complement is plural. These three corrections illustrate the main rules of the present simple: third person -s, negation with does not, and agreement of there is / there are.",
    "Each correction must be justified by a grammar rule, including the spelling of everyday."),
 QT("Write five short sentences describing your laboratory routine using the present simple and frequency adverbs.",
    "Example answer: I usually wear a lab coat before entering the laboratory. I always check the safety data sheet before handling a chemical. I often use a pipette to measure small volumes. I sometimes calibrate the balance at the beginning of a session. I never eat or drink near the benches. Each sentence uses the base form with I, places the frequency adverb before the main verb, and describes a real repeated action.",
    "The answer must contain five correct sentences, frequency adverbs before the main verb and laboratory vocabulary.")],
C("The present simple describes what happens regularly; its main traps are the third person -s and the use of do/does.",
  "He works · He doesn't work · Does he work?",
  "frequency adverbs before the main verb · there is/there are · can + base form",
  "Present simple~Habits and routines~General truths~Third person~Verb + -s~She works~Negation~Does not + base~He doesn't know~Question~Do or does before subject~Frequency adverb~Before main verb~Usually, never~There are~Plural noun~Two beakers",
  "Identify the subject and its person|Choose affirmative, negative or question form|Apply the third person -s rule|Place the frequency adverb|Check there is / there are and articles",
  "Adding -s after does|Using don't with he or she|Writing 'everyday' instead of 'every day'|Using there is with a plural noun|Forgetting the article with a countable noun",
  "I work~Base form~She works~Third person -s~He doesn't work~Negation~Does she work~Question~There are three flasks~Plural~I can measure~Modal + base",
  "Affirmative~She works~Negative~She doesn't work",
  "Countable noun~A beaker~Uncountable noun~Water, no article"))

# ============================================================ AN2
add("AN2", "Technical English: opinions, linking words and lab reports", "Anglais", ["Terminale"],
S("Giving an opinion in English often starts with I think, in my view or in my opinion."
  "|Linking words organize a text: first, then, afterwards, finally for sequence; however for contrast; therefore for consequence."
  "|Comparatives use -er than for short adjectives and more ... than for longer adjectives."
  "|The modals should, must and may express recommendation, obligation and possibility."
  "|The passive voice is frequent in technical writing: the solution was heated, the samples were weighed."
  "|A lab report usually contains an aim, a list of materials, a method, results and a conclusion."
  "|Useful result phrases include the results show that, we observed that and the value increased by ten percent."
  "|False friends can mislead: actually means en réalité, not actuellement, and eventually means finalement."
  "|Articles a, an and the depend on whether the noun is countable, singular and already known."
  "|Uncountable nouns such as water, information and equipment are not used with a in the singular."
  "|When presenting results orally, short sentences and clear signposting help the listener follow the reasoning."
  "|Reading a scientific abstract requires identifying the aim, the method, the main result and the conclusion."),
[QC("Which phrase introduces an opinion?", "In my view~In the meanwhile~As a result~For instance", 0,
     "In my view and in my opinion introduce a personal point of view."),
 QC("Which linking word shows contrast?", "Therefore~However~Moreover~Finally", 1,
     "However introduces a contrast or a reservation."),
 QC("What is the comparative of 'accurate'?", "Accurater~More accurate~Accuratest~Most accurate", 1,
     "Long adjectives form their comparative with more ... than."),
 QC("Which modal expresses a recommendation?", "Must~Should~May~Can", 1,
     "Should gives advice or a recommendation; must expresses a stronger obligation."),
 QC("Which sentence is in the passive voice?", "We heated the solution~The solution was heated~The solution heats~Heating the solution", 1,
     "The passive uses be + past participle: was heated."),
 QC("What does 'actually' mean in English?", "Actuellement~En réalité~Réellement jamais~Finalement", 1,
     "Actually corresponds to en réalité; currently means actuellement."),
 QC("Which noun is uncountable?", "Beaker~Information~Flask~Balance", 1,
     "Information is uncountable: we say information, not an information."),
 QT("Rewrite these sentences in the passive voice and explain the change: 'We weighed the samples. We heated the solution for ten minutes.'",
    "The samples were weighed. The solution was heated for ten minutes. In each case, the direct object of the active sentence becomes the subject of the passive sentence, the verb be takes the past tense and is followed by the past participle, and the original subject we can be omitted because it is not important. The passive voice is common in lab reports because the procedure and the results matter more than the person who performed the actions.",
    "The object must become the subject, with be + past participle and possible omission of the agent."),
 QT("Write a short conclusion for a lab report on the titration of an acid, using at least three linking words.",
    "Example answer: First, the titration was carried out with a standard sodium hydroxide solution. Then, the indicator changed colour after 12.5 cm³ had been added. Therefore, the concentration of the acid was calculated from the equivalence volume. However, the result is slightly higher than the expected value, probably because of a reading error. In conclusion, the experiment confirms the method, but the measurement should be repeated to improve accuracy. The answer uses first, then, therefore, however and in conclusion to guide the reader.",
    "The conclusion must include an aim reminder, a result, a reservation and at least three linking words.")],
C("Technical English favours clear structures: signposting, passive voice and precise result phrases make a lab report readable.",
  "aim · materials · method · results · conclusion",
  "however = contrast · therefore = consequence · was heated = passive",
  "Opinion~I think, in my view~Personal view~Linking word~However, therefore~Structure~Comparative~More accurate than~Comparison~Modal~Should, must, may~Recommendation~Passive~Was heated~Agent omitted~Lab report~Aim, method, results~Scientific writing",
  "State the aim of the experiment|List the materials and the method|Present the results with neutral phrases|Use linking words to connect ideas|Conclude with a reservation or a recommendation",
  "Confusing actually and currently|Using an before an uncountable noun|Forgetting the past participle in the passive|Overusing I think in a report|Mixing up therefore and however",
  "The results show that~Result phrase~It increased by 10%~Variation~Was weighed~Passive~In my view~Opinion~First, then, finally~Sequence~However~Contrast",
  "Active voice~We heated the solution~Passive voice~The solution was heated",
  "Therefore~Consequence~However~Contrast"))

# ============================================================ HG1
add("HG1", "La France de 1789 à 1914 : révolution et régimes", "HGGS", ["1re"],
S("La Révolution française commence en 1789 avec la convocation des États généraux et la prise de la Bastille."
  "|La Déclaration des droits de l'homme et du citoyen, votée en août 1789, affirme la souveraineté nationale et les libertés individuelles."
  "|La monarchie constitutionnelle succède à l'absolutisme, avec une Assemblée législative et un roi aux pouvoirs limités."
  "|La République est proclamée le 22 septembre 1792, après la chute de la monarchie et la victoire de Valmy."
  "|La période de la Terreur marque une radicalisation révolutionnaire avant le Directoire."
  "|Napoléon Bonaparte instaure le Consulat en 1799 puis l'Empire en 1804, en s'appuyant sur le Code civil."
  "|La Restauration, de 1814 à 1830, rétablit la monarchie bourbonienne avec une charte octroyée."
  "|Les Trois Glorieuses de juillet 1830 portent au pouvoir la monarchie de Juillet, rétablissant le régime parlementaire."
  "|La révolution de 1848 met fin à la monarchie et instaure la Deuxième République, puis le Second Empire en 1852."
  "|La défaite de Sedan en 1870 et la chute de Napoléon III conduisent à la proclamation de la Troisième République."
  "|Les lois Ferry de 1881 et 1882 rendent l'enseignement primaire gratuit, obligatoire et laïque."
  "|La loi de séparation des Églises et de l'État est votée en 1905, dans un contexte de réindustrialisation et d'expansion coloniale."),
[QC("En quelle année débute la Révolution française ?", "1789~1792~1804~1848", 0,
     "Les États généraux se réunissent et la Bastille est prise en 1789."),
 QC("Quel texte affirme la souveraineté nationale en 1789 ?", "Le Code civil~La Déclaration des droits de l'homme et du citoyen~La Charte de 1814~Le Concordat", 1,
     "La DDHC du 26 août 1789 pose les principes de 1789."),
 QC("Quand la Première République est-elle proclamée ?", "1789~1792~1799~1870", 1,
     "La République est proclamée le 22 septembre 1792."),
 QC("Quel régime Napoléon instaure-t-il en 1804 ?", "Le Consulat~L'Empire~La monarchie constitutionnelle~Le Directoire", 1,
     "Napoléon se couronne empereur en 1804 après le Consulat."),
 QC("Que sont les Trois Glorieuses ?", "Une bataille de 1814~Une révolution en juillet 1830~Un traité de 1856~Une loi de 1905", 1,
     "Les journées des 27, 28 et 29 juillet 1830 renversent Charles X."),
 QC("Quel événement entraîne la chute du Second Empire ?", "La Révolution de 1848~La défaite de Sedan en 1870~La prise de la Bastille~L'affaire Dreyfus", 1,
     "La défaite de Sedan et la capture de Napoléon III provoquent la chute du régime."),
 QC("Que établit la loi de 1905 ?", "La gratuité de l'enseignement~La séparation des Églises et de l'État~Le suffrage universel~La monarchie parlementaire", 1,
     "La loi du 9 décembre 1905 sépare les Églises et l'État."),
 QT("Expliquer comment la France passe de la monarchie absolue à la République entre 1789 et 1792.",
    "En 1789, la convocation des États généraux puis la formation de l'Assemblée nationale marquent la fin de la monarchie absolue : la souveraineté passe au nation. La Déclaration des droits proclame les libertés et l'égalité devant la loi. La Constitution de 1791 installe une monarchie constitutionnelle où le roi voit ses pouvoirs limités par une Assemblée législative élue. La fuite du roi à Varennes en 1791, la guerre déclarée en avril 1792 et la victoire de Valmy en septembre précipitent la chute de la monarchie. Le 21 septembre 1792, la Convention abolit la royauté et proclame la République le lendemain.",
    "On suit la chronologie : 1789, Constitution de 1791, Varennes, guerre, Valmy, proclamation de la République."),
 QT("Montrer comment les lois Ferry et la loi de 1905 contribuent à la construction d'une République laïque.",
    "Les lois Ferry de 1881 et 1882 rendent l'école primaire gratuite, obligatoire et laïque : l'instruction publique échappe ainsi à l'influence confessionnelle et forme des citoyens partageant les mêmes références républicaines. La loi du 9 décembre 1905 accomplit la séparation des Églises et de l'État : elle garantit la liberté de culte tout en affirmant la neutralité de l'État, qui ne reconnaît ni ne subventionne aucun culte. Ensemble, ces mesures installent la laïcité comme principe d'organisation de la vie publique et de l'école, condition de l'unité nationale dans une France divisée par les querelles religieuses.",
    "On relie gratuité, obligation et laïcité de l'école à la neutralité de l'État proclamée en 1905.")],
C("Entre 1789 et 1914, la France connaît des régimes successifs et construit durablement la souveraineté nationale et la laïcité.",
  "1789 · 1792 · 1804 · 1830 · 1848 · 1870 · 1881-1882 · 1905",
  "monarchie constitutionnelle · République · Empire · lois Ferry · séparation",
  "1789~Révolution~Droits de l'homme~1792~Première République~Valmy~1804~Empire~Code civil~1830~Monarchie de Juillet~Trois Glorieuses~1870~Troisième République~Sedan~1905~Laïcité",
  "Repérer la date et le régime|Identifier l'événement déclencheur|Relier le changement politique à ses causes|Noter les réformes durables|Comparer deux régimes successifs",
  "Confondre Première et Deuxième République|Placer Sedan en 1848|Attribuer les lois Ferry à la monarchie|Croire que 1789 instaure directement la République|Oublier le Consulat",
  "1789~Prise de la Bastille~1792~République~1804~Empire~1870~Troisième République~1881~École gratuite~1905~Séparation",
  "Monarchie~Souveraineté du roi~République~Souveraineté nationale",
  "Lois Ferry~École laïque~Loi de 1905~Neutralité de l'État"))

# ============================================================ HG2
add("HG2", "Guerres mondiales et construction européenne", "HGGS", ["Terminale"],
S("La Première Guerre mondiale éclate en 1914 à la suite des tensions impérialistes, des alliances et de l'assassinat de Sarajevo."
  "|Elle oppose les puissances centrales aux Alliés et se déroule sur le front occidental, notamment dans les tranchées."
  "|Le traité de Versailles de 1919 impose des réparations à l'Allemagne et redessine la carte de l'Europe."
  "|La crise économique de 1929 aggrave les difficultés politiques et favorise l'essor des régimes fasciste et nazi."
  "|La Seconde Guerre mondiale commence en septembre 1939 avec l'invasion de la Pologne par l'Allemagne."
  "|La France est occupée en 1940 ; la Résistance et les forces alliées organisent la libération en 1944-1945."
  "|La Shoah est le génocide systématique des Juifs d'Europe perpétré par le régime nazi."
  "|L'Organisation des Nations unies est créée en 1945 pour maintenir la paix et la sécurité internationales."
  "|La guerre froide oppose de 1947 à 1991 les blocs occidental et soviétique, sans affrontement direct majeur."
  "|La CECA est créée en 1951 par le traité de Paris, mettant en commun les productions de charbon et d'acier."
  "|Les traités de Rome de 1957 instituent la Communauté économique européenne et l'Euratom."
  "|L'Union européenne est fondée en 1993 par le traité de Maastricht ; l'euro entre en circulation en 2002."),
[QC("Quel événement déclenche la Première Guerre mondiale ?", "La crise de 1929~L'assassinat de Sarajevo en 1914~La chute du mur de Berlin~Le traité de Rome", 1,
     "L'attentat de Sarajevo, le 28 juin 1914, déclenche la crise de juillet puis la guerre."),
 QC("Que prévoit le traité de Versailles en 1919 ?", "La création de l'ONU~Des réparations imposées à l'Allemagne~L'adoption de l'euro~La partition de la France", 1,
     "Le traité impose des pertes territoriales et des réparations économiques à l'Allemagne."),
 QC("Quelle année marque le début de la Seconde Guerre mondiale ?", "1914~1919~1939~1945", 2,
     "L'Allemagne envahit la Pologne en septembre 1939."),
 QC("Que désigne la Shoah ?", "Une bataille de 1940~Le génocide des Juifs d'Europe~Un traité de 1919~Une institution de 1945", 1,
     "La Shoah est l'extermination systématique des Juifs d'Europe par les nazis."),
 QC("Quelle organisation internationale est créée en 1945 ?", "La CECA~L'ONU~L'OTAN~L'UE", 1,
     "L'Organisation des Nations unies est fondée en 1945 à San Francisco."),
 QC("Quel traité crée la CECA en 1951 ?", "Le traité de Versailles~Le traité de Paris~Le traité de Rome~Le traité de Maastricht", 1,
     "Le traité de Paris du 18 avril 1951 institue la Communauté européenne du charbon et de l'acier."),
 QC("En quelle année l'euro entre-t-il en circulation ?", "1957~1993~1999~2002", 3,
     "Les billets et pièces en euros circulent depuis le 1er janvier 2002."),
 QT("Expliquer pourquoi la crise de 1929 a favorisé l'essor des régimes totalitaires en Europe.",
    "La crise de 1929 provoque une chute brutale de la production, une vague de chômage et une paupérisation massive. Les démocraties libérales, comme la France ou l'Allemagne de Weimar, paraissent incapables de répondre efficacement à cette détresse. Les mouvements fasciste et nazi proposent des solutions radicales : un État fort, la discipline, l'expansion et la désignation de boucs émissaires. Ils bénéficient du soutien d'une partie des classes moyennes et des milieux d'affaires, ainsi que de la propagande et de la violence politique. En Allemagne, la nomination de Hitler en 1933 marque la victoire du nazisme, rendue possible par la fragilité de la République de Weimar.",
    "On relie chômage et discrédit des démocraties à la séduction des discours autoritaires, avec l'exemple allemand."),
 QT("Montrer comment la construction européenne a répondu aux guerres mondiales et à la guerre froide.",
    "Après 1945, l'Europe est divisée par le rideau de fer et ruinée par deux guerres mondiales. L'idée européenne vise à rendre une nouvelle guerre impossible en liant durablement les économies et les États. La CECA en 1951 met en commun le charbon et l'acier, c'est-à-dire les ressources stratégiques des deux conflits. Les traités de Rome de 1957 créent un marché commun pour favoriser la prospérité et la coopération. En 1993, le traité de Maastricht ajoute une dimension politique et prépare l'euro, entré en vigueur en 2002. Cette intégration progressive a contribué à la paix, à la stabilité démocratique et à la place de l'Europe dans le monde.",
    "On établit le lien entre les ressources stratégiques, le marché commun et l'objectif de paix.")],
C("Les guerres mondiales bouleversent l'Europe ; la construction européenne tente d'en prévenir le retour par l'intégration.",
  "1914-1918 · 1939-1945 · 1945 ONU · 1951 CECA · 1957 Rome · 1993 UE · 2002 euro",
  "Versailles · Shoah · guerre froide · marché commun",
  "1914~Première guerre~Sarajevo~1919~Versailles~Réparations~1939~Seconde guerre~Pologne~1945~ONU et Shoah~Guerre froide~Blocs~1947-1991~1951~CECA~Charbon et acier~1957~Traites de Rome~Marche commun",
  "Situer l'événement dans le temps|Identifier les causes et les acteurs|Relier le conflit à ses conséquences|Repérer les étapes de la construction européenne|Expliquer l'objectif de paix",
  "Confondre 1919 et 1939|Placer la CECA en 1957|Oublier la Shoah dans le bilan de la guerre|Croire que l'UE existe depuis 1945|Ignorer la guerre froide",
  "28 juin 1914~Sarajevo~1919~Versailles~Septembre 1939~Pologne~1945~ONU~1951~CECA~1957~Rome~1993~Maastricht~2002~Euro",
  "Première guerre~1914-1918~Seconde guerre~1939-1945",
  "CECA~Charbon et acier~Union européenne~Marche et politique"))

# FIN_PARTIE_2

valider_et_ecrire(F, "stl-mat-part-A.json")
