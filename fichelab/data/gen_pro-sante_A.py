# -*- coding: utf-8 -*-
"""Generateur pro-sante-mat-part-A.json — lot A : tronc commun (20 fiches).

Filiere pro-sante (bac pro ASSP). Chaque fiche : 12 points, 9 questions
corrigees (7 QCM + 2 texte), 7 blocs en ordre strict, 3 schemas via diag().
Annees : 2nde pro, 1re pro, Terminale pro.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pro_sante_common import S, R, QC, QT, C, build, valider_et_ecrire

F = []


def add(prefix, titre, mat, ans, points, qcm, txt, c):
    """Les QCM et les questions texte sont fournis en deux listes distinctes."""
    F.append(build(prefix, titre, mat, ans, points, qcm + txt, c))


# ============================================================ FR1
add("FR1", "Énonciation et situation d'énonciation dans un récit", "Français", ["2nde pro"],
S("L'énonciation est l'acte par lequel un locuteur produit un énoncé dans une situation donnee, pour un destinataire."
  "|La situation d'énonciation se definit par qui parle, a qui, quand, ou et dans quelle intention."
  "|Les marques d'énonciation sont les pronoms personnels, les adverbes de temps et de lieu et les demonstratifs."
  "|Le recit s'ecrit le plus souvent au passe simple et a l'imparfait : le passe simple marque une action achevee, l'imparfait une action durable ou habituelle."
  "|Le discours direct rapporte les paroles telles quelles, entre guillemets, avec un verbe de dire."
  "|Le discours indirect integre les paroles dans la phrase du narrateur, avec des pronoms et des temps modifies."
  "|Le discours indirect libre supprime le verbe introducteur et les guillemets tout en conservant les marques du personnage."
  "|Le narrateur est interne lorsqu'il est personnage de l'histoire, externe lorsqu'il lui est etranger."
  "|La focalisation interne adopte le point de vue d'un personnage ; la focalisation zero donne une vue d'ensemble."
  "|« Je » marque l'engagement de celui qui ecrit ; « nous » peut designer une equipe de travail."
  "|Dans un compte rendu de stage ASSP, le choix du temps et des pronoms indique la distance prise avec les evenements."
  "|Repérer ces marques permet de commenter un texte et d'adapter sa propre ecriture."),
[QC("Qu'appelle-t-on situation d'énonciation ?", "Le cadre graphique de la page~Qui parle, à qui, quand, où et dans quelle intention~Le nombre de mots du texte~La simple ponctuation", 1,
     "La situation d'énonciation est definie par le locuteur, le destinataire, le moment, le lieu et l'intention."),
 QC("Quel temps marque une action achevée dans un récit ?", "L'imparfait~Le passé simple~Le présent~Le futur", 1,
     "Le passe simple presente l'action comme un fait accompli et ponctuel."),
 QC("Quel signe signale le discours direct ?", "Les guillemets~Un verbe à l'imparfait~Un adverbe de temps~Une virgule", 0,
     "Les guillemets encadrent les paroles rapportees telles quelles."),
 QC("Qui est un narrateur interne ?", "Un personnage de l'histoire~Un personnage absent de l'intrigue~Le lecteur~L'auteur réel", 0,
     "Le narrateur interne participe a l'action qu'il raconte."),
 QC("Que modifie le passage au discours indirect ?", "Les temps et les pronoms~Seulement la ponctuation~Rien du tout~Le nombre de paragraphes", 0,
     "Le discours indirect adapte les temps, les pronoms et les marques d'énonciation."),
 QC("Lequel de ces mots est une marque d'énonciation ?", "Lentement~Ici~Peut-être~Souvent", 1,
     "« Ici » est un adverbe de lieu qui renvoie au lieu de l'énonciation."),
 QC("Dans un compte rendu de stage, que traduit le « nous » ?", "Une distance ironique~L'appartenance à une équipe~Une faute de grammaire~Un doute", 1,
     "Le « nous » implique le locuteur dans un collectif, ici l'equipe professionnelle.")],
[QT("Expliquer la différence entre discours direct et discours indirect, puis illustrer avec une phrase de soignant.",
     "Le discours direct reproduit les paroles telles qu'elles ont ete prononcees : il conserve les guillemets, le present et les pronoms de la personne qui parle, par exemple : « Je vais vous installer. » Le discours indirect les integre dans la phrase du narrateur : il supprime les guillemets, introduit un verbe comme « dire » ou « expliquer », et modifie les temps et les pronoms : « L'aide-soignante a expliqué qu'elle allait installer la personne. » Le premier donne a entendre la voix du personnage ; le second rapporte son propos avec la distance du narrateur.",
     "On oppos la reproduction fidèle des paroles et leur integration grammaticale dans le recit, en citant un exemple et les transformations subies."),
 QT("Dans la phrase « Ce matin, je suis arrivée ici et j'ai retrouvé Madame Martin », relever les marques d'énonciation et en déduire le point de vue.",
     "Les marques sont « ce matin » (adverbe de temps), « je » (locutrice), « ici » (adverbe de lieu), « suis arrivée » et « ai retrouvé » (passe compose a la premiere personne). Le « je » et le passe compose indiquent une locutrice qui raconte sa propre experience : le point de vue est interne. Le destinataire n'est pas explicite mais le lecteur est implicitement impliqué. Ce type de phrase est courant dans un cahier de suivi ou un compte rendu de stage : la professionnelle s'engage personnellement dans ce qu'elle decrit.",
     "On attend le relevé des pronoms et adverbes, l'identification du locuteur et la conclusion sur la focalisation interne.")],
C("Tout énoncé prend sens dans une situation : identifier qui parle, à qui et quand permet de lire un texte et d'écrire juste.",
  "énonciation = locuteur + destinataire + contexte spatio-temporel + intention",
  "je/tu/ici/maintenant = marques de discours · passé simple et imparfait = marques de récit",
  "Récit~Passé simple et imparfait~Fait passé~Discours direct~Guillemets et présent~Paroles telles quelles~Discours indirect~Verbe introducteur~Temps modifiés",
  "Repérer le temps du verbe|Identifier locuteur et destinataire|Repérer pronoms et adverbes|Choisir le mode de rapport des paroles|Justifier le point de vue adopté",
  "Confondre auteur et narrateur|Oublier l'accord des temps en discours indirect|Croire que l'imparfait marque l'action achevée|Négliger les adverbes de lieu",
  "Je~Marque du locuteur|Ici~Repère spatial|Il entra~Passé simple achevé|Elle parlait~Imparfait durable|Nous~Équipe pluriprofessionnelle",
  "Discours direct~Guillemets et verbe de dire~Paroles telles quelles~Discours indirect~Verbe introducteur~Pronoms et temps modifiés",
  "Narrateur interne~Personnage de l'histoire~Vue limitée~Narrateur externe~Étranger à l'action~Vue plus large"))

# ============================================================ FR2
add("FR2", "Les figures de style et leurs effets de sens", "Français", ["1re pro"],
S("Une figure de style est un procede de langage qui modifie l'expression pour produire un effet de sens."
  "|La comparaison etablit un rapprochement explicite grace a un outil comme « comme », « tel » ou « semblable a »."
  "|La metaphore transposite un terme sans outil de comparaison : elle dit une chose en termes d'une autre."
  "|La personnification attribue un trait humain a un etre vivant, a un objet ou a une notion abstraite."
  "|La metonymie designe une realite par un element qui lui est lie : la cause pour l'effet, l'instrument pour l'action."
  "|La synecdoque est une metonymie particuliere qui emploie la partie pour le tout ou le tout pour la partie."
  "|L'antithese oppose deux termes ou deux idees dans la meme phrase pour souligner un contraste."
  "|L'oxymore associe deux mots contradictoires dans une expression courte."
  "|L'hyperbole exagere une expression pour insister ; l'euphemisme atténue une realite difficile."
  "|L'anaphore repete un meme mot en debut de phrase ou de vers pour insister."
  "|Identifier une figure ne suffit pas : il faut citer le passage, nommer le procede et expliquer l'effet produit."
  "|Dans un texte sur l'accompagnement, les figures servent souvent a rendre sensible la souffrance ou la dignite de la personne."),
[QC("Quel outil signale une comparaison ?", "Comme~Sans~Avec~Pour", 0,
     "La comparaison est explicite grace a un outil de comparaison comme « comme »."),
 QC("Qu'est-ce qu'une métaphore ?", "Une comparaison avec « comme »~Un rapprochement sans outil explicite~Une repetition de consonnes~Une exageration", 1,
     "La metaphore supprime l'outil de comparaison et transposite directement un terme."),
 QC("Que fait la personnification ?", "Elle attribue un trait humain~Elle oppose deux mots~Elle atténue une idée~Elle compte les syllabes", 0,
     "La personnification donne des attributs humains a un etre ou a une notion."),
 QC("« La plume » pour « l'écriture » est une…", "Synecdoque~Métonymie~Antithèse~Allitération", 1,
     "L'instrument est pris pour l'action : c'est une metonymie."),
 QC("Quelle figure associe deux mots contradictoires ?", "L'antithèse~L'oxymore~L'anaphore~L'hyperbole", 1,
     "L'oxymore réunit deux termes opposés en une expression brève, comme « silence assourdissant »."),
 QC("Quel est l'effet d'une hyperbole ?", "Atténuer~Exagérer pour insister~Répéter une voyelle~Raconter au passé", 1,
     "L'hyperbole force le trait pour marquer l'intensité."),
 QC("Que désigne une anaphore ?", "Une opposition~Une répétition en début de phrase~Une image sans outil~Une exagération", 1,
     "L'anaphore répète un même mot ou groupe de mots en tête de phrase ou de vers.")],
[QT("Commenter la phrase « Sa voix était une lumière dans la chambre » en identifiant la figure et son effet.",
     "La phrase contient une metaphore : « sa voix était une lumière » rapproche directement la voix et la lumière, sans outil de comparaison. La voix est presentee comme ce qui eclaire et rassure dans un lieu clos, la chambre. Ce rapprochement suggere la presence bienveillante de la personne soignante et l'effet d'apaisement qu'elle produit, sans le dire explicitement. Le lecteur comprend l'importance de la parole et de l'écoute dans l'accompagnement. On pourrait aussi relever une valeur symbolique de la lumière, opposee implicitement a l'obscurite de la maladie ou de la solitude.",
     "On attend : identification de la metaphore, citation du segment, explication de l'effet sur le lecteur et mise en relation avec le theme."),
 QT("Distinguer l'antithèse et l'oxymore, puis proposer un exemple de chacune en lien avec le soin.",
     "L'antithese oppose deux termes ou deux idees dans une meme phrase, par exemple « la faiblesse du corps et la force du lien » ; le contraste est explicite et peut porter sur une longue sequence. L'oxymore concentre la contradiction dans un groupe de mots court, comme « une douceur brutale » ou « un silence assourdissant ». L'antithese met en scene deux poles distincts, tandis que l'oxymore fusionne deux qualites contradictoires en un seul etre ou une seule sensation. Dans un texte de soin, ces figures traduisent la complexite de l'experience : la personne est a la fois fragile et digne, dependante et capable d'initiative.",
     "La réponse doit opposer l'opposition explicite et la contradiction concentree, avec un exemple pertinent pour chacune.")],
C("Une figure de style n'est pas un ornement : elle modifie la perception du lecteur et doit toujours être reliée au sens du texte.",
  "figure = écart de langue + effet de sens",
  "comparaison avec outil · métaphore sans outil · oxymore = contradiction courte",
  "Comparaison~Outil comme ou tel~Rapprochement explicite~Métaphore~Transposition directe~Image sans outil~Personnification~Trait humain~Être ou notion",
  "Lire la phrase entière~Repérer un écart de langue~Nommer précisément la figure~Citer le segment concerné~Expliquer l'effet produit",
  "Nommer une figure sans la justifier|Confondre comparaison et métaphore|Oublier de citer le texte|Inventer un effet sans lien avec le contexte",
  "Comme~Outil de comparaison~Une lumière~Métaphore~Silence assourdissant~Oxymore~La plume~Métonymie~Je répète~Anaphore",
  "Antithèse~Deux pôles opposés~Contraste explicite~Oxymore~Contradiction concentrée~Groupe court",
  "Métonymie~Lien de contiguïté~Instrument pour l'action~Synecdoque~La partie pour le tout"))

# ============================================================ FR3
add("FR3", "L'argumentation : thèse, arguments et exemples", "Français", ["Terminale pro"],
S("Un texte argumentatif vise a convaincre ou a persuader un destinataire d'une these."
  "|La these est l'opinion defendue ; elle peut etre explicite ou implicite."
  "|Les arguments sont les raisons proposees pour etayer la these : ils doivent etre pertinents et suffisants."
  "|L'exemple illustre un argument et le rend concret ; il ne remplace pas l'argument."
  "|Les connecteurs logiques organisent le raisonnement : « d'abord », « donc », « cependant », « enfin »."
  "|Le schema argumentatif peut etre deductif (these puis preuves) ou inductif (exemples puis generalisation)."
  "|La concession reconnait un argument adverse avant de le refuter, ce qui renforce la credibilite."
  "|La refutation conteste l'objection par un contre-argument ou une distinction."
  "|Les registres persuasif et polémique utilisent davantage les figures et les appels a l'emotion."
  "|Les modaux de necessite et d'obligation (« il faut », « on doit ») marquent l'engagement de l'auteur."
  "|Dans le domaine de la sante, argumenter permet de justifier une hygiene de vie ou une action d'education."
  "|Une conclusion reformule la these et ouvre parfois une question ou une proposition d'action."),
[QC("Qu'appelle-t-on these dans un texte argumentatif ?", "Un exemple~L'opinion defendue~Un connecteur~Une figure de style", 1,
     "La these est le point de vue que l'auteur cherche a faire admettre."),
 QC("Quel rôle joue un exemple ?", "Il remplace l'argument~Il illustre l'argument~Il introduit la these~Il clôt le texte", 1,
     "L'exemple rend l'argument concret mais ne tient pas lieu de raison."),
 QC("Quel connecteur marque une opposition ?", "Donc~Cependant~D'abord~Ainsi", 1,
     "« Cependant » introduit une concession ou une opposition."),
 QC("Qu'est-ce qu'une concession ?", "Un refus total~La reconnaissance d'un argument adverse~Une repetition~Une conclusion", 1,
     "La concession admet une objection avant d'y répondre."),
 QC("Quel schema part des exemples pour generaliser ?", "Deductif~Inductif~Chronologique~Descriptif", 1,
     "Le schema inductif part de cas concrets pour dégager une règle."),
 QC("Quel modale marque l'obligation ?", "Peut-être~Il faut~Peut-être bien~Souvent", 1,
     "« Il faut » exprime la necessite et l'engagement de l'auteur."),
 QC("Que doit faire la conclusion ?", "Introduire un nouvel argument~Reformuler la these~Supprimer les exemples~Changer de registre", 1,
     "La conclusion reformule la these et peut ouvrir une perspective.")],
[QT("Analyser un court texte argumentatif sur l'importance du lavage des mains : relever these, arguments et exemples.",
     "La these est que le lavage des mains est un geste indispensable en milieu de soin. Les arguments sont : les mains sont le principal vecteur de transmission des micro-organismes ; le lavage avec un savon ou une solution hydro-alcoolique reduit la charge microbienne ; le geste protege la personne accompagnee mais aussi le professionnel. Les exemples concrets sont la friction des mains avant une toilette, apres un change ou entre deux personnes. On relevera les connecteurs « d'abord », « ensuite » et « donc », qui organisent le raisonnement de maniere deductive. La conclusion reformule l'idee de responsabilite partagee.",
     "On attend le repérage de la these, la distinction entre raisons et exemples, et l'analyse des connecteurs."),
 QT("Construire un paragraphe argumente en faveur de la bientraitance, avec concession et refutation.",
     "On peut ecrire : « Certains pensent que la bientraitance se limite a l'absence de gestes brutaux. Certes, la violence physique doit etre exclue, mais la bientraitance va plus loin : elle exige d'ecouter la personne, de respecter son rythme et de lui expliquer les soins. Une attitude correcte mais silencieuse peut etre vécue comme froide et humiliante. Il faut donc former les professionnels a la communication et a la reflexivite, car le respect de la dignite se joue aussi dans les mots et les regards. » La concession est introduite par « certes », la refutation par « mais », et l'argument par « car ». La these est finalement reformulee dans la derniere phrase.",
     "La réponse doit contenir une these explicite, une concession, une refutation et un connecteur de cause.")],
C("Argumenter, c'est defendre une these avec des raisons, illustrées par des exemples et organisees par des connecteurs.",
  "thèse + arguments + exemples + connecteurs = raisonnement",
  "concession = admettre une objection · réfutation = y répondre",
  "Thèse~Opinion defendue~Pas toujours explicite~Argument~Raison qui etaye~Pertinence requise~Exemple~Cas concret~Illustration",
  "Formuler clairement la these~Choisir deux ou trois arguments solides~Illustrer par un exemple precis~Prevoir une objection et y répondre~Conclure en reformulant",
  "Confondre exemple et argument|Aligner les arguments sans connecteurs|Ignorer l'objection adverse|Conclure en introduisant un nouvel argument",
  "Donc~Consequence~Cependant~Opposition~Il faut~Obligation~Certes~Concession~Enfin~Organisation",
  "Deductif~These puis preuves~Raisonnement general~Inductif~Exemples puis generalisation~Règle tiree du concret",
  "Convaincre~S'appuyer sur la raison~Persuader~S'appuyer sur l'emotion"))

# ============================================================ FR4
add("FR4", "Écrire un compte rendu de stage en ASSP", "Français", ["Terminale pro"],
S("Le compte rendu de stage est un ecrit professionnel qui relate et analyse une experience de formation en milieu professionnel."
  "|Il repond a une commande precise : destinataire, longueur, format et date de remise doivent etre respectes."
  "|Sa structure comprend une introduction, une presentence du cadre, le recit des activites, une analyse et une conclusion."
  "|La présentation du cadre indique l'etablissement, le service, les professionnels rencontres et la duree du stage."
  "|Le recit suit l'ordre chronologique ou l'ordre des activites, jamais l'ordre des pensees."
  "|Les faits sont distingues des impressions : « j'ai observe » n'a pas la meme valeur que « j'ai ressenti »."
  "|Le vocabulaire professionnel est precis : bionettoyage, toilette, transmission, projet individualise."
  "|La premiere personne du singulier est acceptable dans un compte rendu reflection, mais le ton reste sobre."
  "|L'analyse relie les observations aux connaissances du cours et identifie les competences mobilisees."
  "|Le respect du secret professionnel interdit de nommer les personnes ou de rapportre des informations confidentielles."
  "|La ponctuation, les accents et les accords sont verifies avant remise : une faute nuit a la credibilite."
  "|Une relecture finale permet de verifier la coherence des temps et la presence de toutes les parties demandees."),
[QC("Quelle est la première partie d'un compte rendu de stage ?", "Une analyse~Une introduction presentant le cadre~Une conclusion~Une liste de fautes", 1,
     "On presente d'abord le contexte : stage, etablissement, service et periode."),
 QC("Comment organiser le récit des activités ?", "Dans l'ordre des souvenirs~Dans l'ordre chronologique ou par activite~Au hasard~Par ordre alphabetique", 1,
     "Le recit suit un plan clair, chronologique ou thematique."),
 QC("Quelle phrase distingue un fait d'une impression ?", "J'ai ressenti de la fatigue~J'ai observé une toilette~Il faisait bon~C'était intéressant", 1,
     "« J'ai observé » rapporte un fait verifiable, contrairement aux jugements personnels."),
 QC("Quel terme professionnel convient pour le nettoyage d'une chambre ?", "Nettoyage~Bionettoyage~Rangement~Entretien", 1,
     "Le bionettoyage designe la procedure de nettoyage et de desinfection en milieu de soin."),
 QC("Que faut-il éviter absolument dans un compte rendu ?", "Les temps du récit~Les noms des personnes accompagnées~Les connecteurs~Les décorations", 1,
     "Le secret professionnel interdit d'identifier les personnes ou de divulguer leur situation."),
 QC("À quoi sert la partie analyse ?", "À répéter le récit~À relier les observations aux cours et aux compétences~À ajouter des exemples inventés~À remplacer la conclusion", 1,
     "L'analyse montre ce que le stagiaire a appris et mobilise ses connaissances."),
 QC("Que vérifier lors de la relecture finale ?", "Le nombre de pages seulement~La cohérence des temps, les accords et les parties demandées~Le prix du papier~La couverture", 1,
     "La relecture porte sur la forme et sur la conformite a la consigne.")],
[QT("Rédiger l'introduction d'un compte rendu de stage en EHPAD en respectant les règles vues.",
     "« Du 6 au 31 janvier, j'ai effectue un stage de quatre semaines au sein d'un EHPAD de 82 lits, plus precisement dans l'unite de vie protegee. Encadree par une aide-soignante referente, j'ai participe aux soins d'hygiene et de confort, aux transfers et aux repas. Ce compte rendu presente les activites observees et realisees, puis analyse les competences mobilisees au regard du referentiel du bac professionnel ASSP. » Cette introduction indique la periode, le lieu, le service, l'encadrement et le plan annonce, sans nommer les residents.",
     "On attend la presence du cadre spatio-temporel, du service, de l'encadrement et de l'annonce du plan."),
 QT("Expliquer pourquoi il ne faut pas noter le nom d'une personne accompagnée dans un compte rendu de stage.",
     "Le secret professionnel s'impose a tout professionnel et a tout stagiaire : il interdit de divulguer des informations sur l'etat de sante, la situation sociale ou l'identite d'une personne. Un compte rendu de stage circule dans un cadre scolaire et peut etre lu par des personnes etrangeres au service. Meme un prenom associe a un diagnostic constitue une violation. On utilisera donc des formules neutres comme « une residente de 84 ans » ou « une personne en situation de dependance », sans detail permettant de l'identifier. Cette prudence fait partie de la posture professionnelle evaluee en stage.",
     "La réponse doit relier secret professionnel, circles de lecture et neutralisation des identites.")],
C("Un compte rendu de stage est un ecrit commandé : il relate des faits, analyse des compétences et respecte le secret professionnel.",
  "cadre + faits + analyse + conclusion = compte rendu",
  "j'ai observé (fait) / j'ai ressenti (impression) · secret professionnel",
  "Introduction~Cadre et commande~Période et lieu~Récit~Activités réalisées~Ordre chronologique~Analyse~Lien avec les cours~Compétences mobilisées",
  "Lire la commande et le format~Présenter le cadre~Raconter les activités dans l'ordre~Analyser les apprentissages~Relire et anonymiser",
  "Raconter sans analyser|Nommer les personnes accompagnées|Mélanger faits et impressions|Oublier la relecture",
  "Bionettoyage~Procédure de nettoyage~Transmission~Information écrite orale~Projet individualisé~Accompagnement personnalisé~EHPAD~Établissement d'hébergement",
  "Fait~Observation vérifiable~Impression~Ressenti personnel~À distinguer~Ne pas confondre",
  "Récit~Ce qui s'est passé~Analyse~Ce que cela apprend"))

# ============================================================ MA1
add("MA1", "Proportionnalité, pourcentages et taux", "Maths", ["2nde pro"],
S("Deux grandeurs sont proportionnelles lorsque l'une est obtenue en multipliant l'autre par un coefficient constant."
  "|On ecrit alors y = k x, ou k est le coefficient de proportionnalite."
  "|La representation graphique d'une fonction linéaire est une droite passant par l'origine du repere."
  "|Un pourcentage est une fraction de denominateur 100 : 15 % = 15/100 = 0,15."
  "|Pour calculer p % d'une grandeur G, on multiplie G par p/100."
  "|Pour determiner un taux, on divise la part par le total puis on multiplie par 100."
  "|Une augmentation de t % s'obtient en multipliant la valeur initiale par (1 + t)."
  "|Une diminution de t % s'obtient en multipliant par (1 − t)."
  "|Deux augmentations successives de 10 % donnent 1,1 × 1,1 = 1,21, soit une hausse de 21 %."
  "|La regle de trois permet de calculer une valeur intermediaire dans une situation de proportionnalite."
  "|En ASSP, les pourcentages servent a lire un taux d'occupation, une part de repas ou un resultat de qualite."
  "|Il faut arrondir seulement a la fin du calcul et verifier l'ordre de grandeur du resultat."),
[QC("À combien vaut 15 % sous forme décimale ?", "1,5~0,15~0,015~15", 1,
     "15 % signifie 15/100, soit 0,15."),
 QC("Que vaut 20 % de 150 ?", "20~30~50~170", 1,
     "150 × 0,20 = 30."),
 QC("Comment calculer un taux ?", "Total divisé par la part~Part divisée par le total, puis fois 100~Part multipliée par le total~Total moins la part", 1,
     "Le taux en pourcentage vaut (part / total) × 100."),
 QC("Quel coefficient correspond à une hausse de 10 % ?", "0,10~1,10~10~0,90", 1,
     "On multiplie par 1 + 0,10 = 1,10."),
 QC("Quelle est la hausse totale après deux augmentations de 10 % ?", "20 %~21 %~10 %~110 %", 1,
     "Les coefficients se multiplient : 1,1 × 1,1 = 1,21, donc +21 %."),
 QC("Quelle est la représentation graphique de y = k x ?", "Une parabole~Une droite passant par l'origine~Une hyperbole~Un cercle", 1,
     "Une fonction linéaire se represente par une droite passant par (0 ; 0)."),
 QC("Quand faut-il arrondir un résultat ?", "Dès la première opération~À la fin du calcul~Avant de lire l'énoncé~Jamais", 1,
     "Arrondir trop tôt accumule les erreurs ; on arrondit au dernier moment.")],
[QT("Un EHPAD compte 60 lits et 48 sont occupés. Calculer le taux d'occupation et l'exprimer en pourcentage.",
     "Le taux d'occupation se calcule en divisant le nombre de lits occupes par le nombre total de lits, puis en multipliant par 100 : 48 / 60 = 0,8, soit 0,8 × 100 = 80 %. On peut aussi remarquer que 48 = 4 × 12 et 60 = 5 × 12, donc le rapport est 4/5 = 0,8. Le taux d'occupation est donc de 80 %, ce qui signifie que douze lits restent libres sur soixante. On verifiera l'ordre de grandeur : 48 est inferieur a 60, donc le taux doit etre inferieur a 100 %.",
     "On attend le calcul du rapport, la multiplication par 100 et une verification de coherence."),
 QT("Un tarif de 80 € augmente de 5 %, puis la nouvelle valeur diminue de 5 %. Calculer le prix final et expliquer pourquoi il n'est pas égal à 80 €.",
     "Apres la hausse de 5 %, le prix vaut 80 × 1,05 = 84 €. Apres la baisse de 5 %, il vaut 84 × 0,95 = 79,80 €. Le coefficient global est 1,05 × 0,95 = 0,9975, soit une diminution finale de 0,25 %. Le prix n'est pas egal a 80 € car la diminution s'applique a une base plus elevee (84 €) que la base initiale (80 €) : la baisse de 4,20 € est superieure a la hausse de 4 €. C'est une application directe de la non-commutativite des variations successives en pourcentage.",
     "On attend les deux calculs, le coefficient global et l'explication de l'ecart.")],
C("Un taux est un rapport multiplié par cent : le calculer, c'est divider la part par le total puis passer en pourcentage.",
  "p % de G = G × p/100 · taux = (part / total) × 100",
  "hausse de t % = multiplier par (1 + t) · baisse = multiplier par (1 − t)",
  "Proportionnalité~Coefficient constant k~Droite par l'origine~Pourcentage~Fraction sur 100~Écriture décimale~Taux~Part sur total~Multiplié par 100",
  "Repérer la grandeur de référence~Écrire le rapport part sur total~Multiplier par 100~Vérifier l'ordre de grandeur~Arrondir en fin de calcul",
  "Confondre 15 % et 15|Appliquer la baisse à l'ancienne valeur|Additionner deux pourcentages successifs|Arrondir au début du calcul",
  "48/60~Taux de 80 %~80 € × 1,05~84 €~84 € × 0,95~79,80 €~1,1 × 1,1~Hausse de 21 %",
  "Augmentation~Multiplier par 1+t~Diminution~Multiplier par 1-t",
  "Pourcentage~Rapport sur 100~Proportionnalité~Coefficient constant"))

# ============================================================ MA2
add("MA2", "Fonctions affines et linéaires : modéliser une situation", "Maths", ["1re pro"],
S("Une fonction associe a chaque nombre x de son ensemble de definition un unique nombre f(x)."
  "|Une fonction lineaire est de la forme f(x) = k x : elle traduit une situation de proportionnalite."
  "|Une fonction affine est de la forme f(x) = a x + b, ou a est le coefficient directeur et b l'ordonnée a l'origine."
  "|Sa representation graphique est une droite : b donne le point de depart et a la pente."
  "|Si a est positif, la fonction est croissante ; si a est negatif, elle est decroissante."
  "|Le coefficient directeur se calcule avec deux points : a = (y2 − y1) / (x2 − x1)."
  "|L'ordonnée a l'origine s'obtient en remplaçant x par zero dans l'equation."
  "|Resoudre f(x) = k revient a chercher l'abscisse du point de la droite d'ordonnee k."
  "|Resoudre f(x) ≤ k revient a lire la partie de la droite situee sous la droite horizontale y = k."
  "|Une fonction peut modeliser un cout : cout fixe b plus cout variable a multiplie par le nombre d'unites."
  "|Le domaine de definition doit etre precise : un nombre de personnes est un entier positif."
  "|Dans un service de soins, une fonction peut relier la consommation de linge au nombre de residents."),
[QC("Quelle est la forme d'une fonction affine ?", "f(x) = x²~f(x) = a x + b~f(x) = a/x~f(x) = a^x", 1,
     "Une fonction affine s'ecrit f(x) = a x + b."),
 QC("Quel est le coefficient directeur de f(x) = −2x + 5 ?", "5~2~−2~−5", 2,
     "Le coefficient de x est −2 : la droite est decroissante."),
 QC("Comment calculer la pente avec deux points ?", "(y2 − y1)/(x2 − x1)~x2 − x1~y1 + y2~(x1+x2)/2", 0,
     "La pente est le rapport de la variation des ordonnees sur celle des abscisses."),
 QC("Par quel point une fonction lineaire passe-t-elle toujours ?", "(0 ; 1)~Le point d'origine (0 ; 0)~(1 ; 1)~Aucun point particulier", 1,
     "f(0) = 0 pour une fonction lineaire, donc la droite passe par l'origine."),
 QC("Que represente b dans f(x) = a x + b ?", "La pente~L'ordonnée à l'origine~Le domaine~La racine", 1,
     "b est la valeur de f(0), point de croisement avec l'axe des ordonnees."),
 QC("Une fonction est décroissante si…", "a > 0~a < 0~a = 0~b > 0", 1,
     "Un coefficient directeur negatif rend la fonction decroissante."),
 QC("Que faut-il préciser pour un nombre de personnes ?", "Un domaine de définition entier positif~Une valeur négative~Un nombre décimal quelconque~Aucune contrainte", 0,
     "Le contexte impose un domaine : ici des entiers positifs ou nuls.")],
[QT("Une fonction affine passe par A(2 ; 7) et B(5 ; 16). Déterminer son équation, puis calculer f(12).",
     "Le coefficient directeur vaut a = (16 − 7)/(5 − 2) = 9/3 = 3. En utilisant le point A(2 ; 7) : 7 = 3 × 2 + b, donc b = 1. L'equation est donc f(x) = 3x + 1. On verifie avec B : 3 × 5 + 1 = 16. Alors f(12) = 3 × 12 + 1 = 37. La droite coupe l'axe des ordonnees en (0 ; 1) et monte de 3 unites lorsque x augmente de 1. Si x represente un nombre de residents, on limitera le domaine aux entiers positifs.",
     "On attend le calcul de la pente, celui de b, la verification avec le second point et le resultat final."),
 QT("Dans un EHPAD, le linge consommé vaut 3 kg par résident et par jour, plus 4 kg fixes pour l'entretien. Modéliser et interpréter la fonction.",
     "On ecrit f(n) = 3n + 4, ou n est le nombre de residents presents dans l'unite. Le coefficient 3 represente la consommation variable par personne ; la constante 4 represente la consommation fixe liee a l'entretien des locaux, meme sans resident. Pour 20 residents, la consommation est f(20) = 3 × 20 + 4 = 64 kg par jour. La fonction est croissante car le coefficient est positif. Le domaine est l'ensemble des entiers naturels, eventuellement limites par la capacite d'accueil. Resoudre f(n) = 100 revient a 3n + 4 = 100, soit n = 32 residents.",
     "La réponse doit identifier a et b, calculer une image et interpreter le domaine.")],
C("Une fonction affine décrit une évolution régulière : une valeur de départ b, puis une variation constante a par unité.",
  "f(x) = a x + b · a = (y2 − y1)/(x2 − x1)",
  "a > 0 : croissante · a < 0 : décroissante · b = f(0)",
  "Fonction affine~Droite de pente a~f(x)=ax+b~Fonction linéaire~Cas b=nul~Proportionnalité~Coefficient directeur~Variation de y sur variation de x~Domaine~Valeurs possibles de x",
  "Identifier les deux grandeurs~Choisir le type de fonction~Calculer a avec deux points~Déterminer b par substitution~Interpréter le domaine et la pente",
  "Confondre pente et ordonnée à l'origine|Oublier le domaine de définition|Diviser par x2−x1 dans le mauvais sens|Croire qu'une droite est toujours croissante",
  "A(2;7)~a=3 et b=1~f(12)=37~3n+4~64 kg pour 20~f(n)=100~32 résidents~a négatif~Fonction décroissante",
  "Fonction linéaire~Droite par l'origine~f(x)=kx~Fonction affine~Droite décalée de b",
  "Croissante~Coefficient positif~Décroissante~Coefficient négatif"))

# ============================================================ MA3
add("MA3", "Statistiques descriptives et graphiques", "Maths", ["1re pro"],
S("La statistique descriptive resume un ensemble de donnees pour en degager les caracteristiques essentielles."
  "|Une population est l'ensemble complet estudie ; un echantillon en est une partie."
  "|Un effectif est le nombre d'individus dans une classe ; un effectif cumule additionne les effectifs precedents."
  "|La frequence relative est l'effectif de la classe divise par l'effectif total."
  "|La moyenne est la somme des valeurs divisée par l'effectif ; elle est sensible aux valeurs extremales."
  "|La mediane est la valeur qui partage la serie ordonnee en deux moities."
  "|Le mode est la valeur la plus frequente : c'est la seule mesure de position pertinente pour un caractere qualitatif."
  "|L'etendue est la difference entre la valeur maximale et la valeur minimale."
  "|La variance mesure la dispersion autour de la moyenne ; l'ecart-type en est la racine carree."
  "|L'ecart-type s'exprime dans la meme unité que la donnee, ce qui facilite son interpretation."
  "|L'histogramme convient a une variable continue, le diagramme en batons a une variable discrete."
  "|Une presentation rigoureuse indique la source, la taille de l'echantillon et les unites."),
[QC("Quelle mesure résiste aux valeurs extrêmes ?", "La moyenne~La médiane~L'écart-type~L'étendue", 1,
     "La mediane depend du rang des valeurs, pas de leur amplitude."),
 QC("Comment calculer une fréquence relative ?", "Effectif fois le total~Effectif divisé par l'effectif total~Total moins l'effectif~Valeur max moins valeur min", 1,
     "La frequence relative vaut effectif de la classe sur effectif total."),
 QC("Quel graphique convient à une variable continue ?", "Le camembert~L'histogramme~Le diagramme en bâtons~Le pictogramme", 1,
     "L'histogramme represente les effectifs par classes de valeurs continues."),
 QC("Que mesure l'écart-type ?", "La tendance centrale~La dispersion autour de la moyenne~Le nombre d'individus~La corrélation", 1,
     "L'ecart-type quantifie la dispersion dans la meme unité que la variable."),
 QC("Dans une série ordonnée de 9 valeurs, quel est le rang de la médiane ?", "Le 4e~Le 5e~Le 9e~La moyenne des 4e et 5e", 1,
     "Pour un effectif impair, la mediane est la valeur de rang (n+1)/2, soit 5."),
 QC("Quel indicateur choisir pour un caractère qualitatif ?", "La moyenne~Le mode~L'écart-type~La médiane", 1,
     "Le mode est la classe la plus frequente, seul indicateur pertinent pour le qualitatif."),
 QC("Que désigne l'intervalle interquartile ?", "L'écart entre min et max~L'écart entre Q1 et Q3~La moyenne des quartiles~La somme des effectifs", 1,
     "Il contient la moitie centrale des observations, soit 50 % de la serie.")],
[QT("Une série de 5 durées de toilette en minutes est : 12, 15, 18, 20, 95. Calculer moyenne et médiane, puis commenter.",
     "La somme vaut 12 + 15 + 18 + 20 + 95 = 160, donc la moyenne est 160/5 = 32 minutes. La serie est deja ordonnee ; avec 5 valeurs, la mediane est la troisieme, soit 18 minutes. L'ecart entre moyenne et mediane est de 14 minutes, cause par la valeur 95 qui tire la moyenne vers le haut. La mediane decrit mieux la duree habituelle d'une toilette. On completera par l'etendue (95 − 12 = 83 minutes) et on cherchera a comprendre la valeur aberrante, par exemple une situation d'urgence ou une erreur de saisie, avant toute conclusion.",
     "On attend les deux calculs, l'explication de l'ecart par la valeur extremale et la recommandation d'usage."),
 QT("Expliquer pourquoi un échantillon représentatif est indispensable avant de généraliser un résultat.",
     "Un echantillon est representatif lorsque sa composition reflète celle de la population pour les caracteristiques pertinentes. Si le prelevement est biaise, par exemple en n'interrogeant qu'un seul etage d'un etablissement, les estimateurs comme la moyenne ou la frequence sont biaises et toute generalisation est invalide, meme avec un grand effectif. Un tirage aleatoire, une stratification et un effectif suffisant reduisent ce risque. On doit aussi indiquer la marge d'incertitude et le niveau de confiance pour quantifier la precision avant de conclure sur l'ensemble de la population.",
     "On relie representativite et absence de biais, puis on cite tirage aleatoire, stratification et marge d'incertitude.")],
C("La statistique descriptive résume une série par une tendance centrale et une dispersion, en choisissant des indicateurs adaptés au type de donnée.",
  "fréquence = effectif / effectif total · écart-type = racine de la variance",
  "moyenne sensible aux extrêmes · médiane robuste · mode pour le qualitatif",
  "Population~Ensemble complet~Échantillon~Partie prélevée~Moyenne~Somme sur effectif~Médiane~Valeur centrale~Écart-type~Dispersion",
  "Définir population et échantillon~Trier et classer les données~Choisir les indicateurs~Construire le graphique adapté~Interpréter avec source et unités",
  "Utiliser la moyenne avec une valeur aberrante|Confondre effectif et fréquence|Choisir un camembert pour une variable continue|Omettre la taille de l'echantillon",
  "12;15;18;20;95~Moyenne 32, médiane 18~48 sur 60~Fréquence 80 %~Q1 et Q3~Moitié centrale~Histogramme~Variable continue~Mode~Classe la plus fréquente",
  "Moyenne~Sensible aux extrêmes~Médiane~Résistante aux extrêmes",
  "Effectif~Nombre d'individus~Fréquence~Part du total"))

# ============================================================ MA4
add("MA4", "Probabilités et estimation : lire un risque", "Maths", ["Terminale pro"],
S("Une experience aleatoire est une epreuve dont l'issue est incertaine mais dont les resultats possibles sont connus."
  "|L'univers est l'ensemble de toutes les issues ; un evenement en est une partie."
  "|Dans un univers fini equiprobable, la probabilite d'un evenement est le nombre d'issues favorables divise par le nombre total d'issues."
  "|Une loi de probabilite associe une probabilite a chaque issue ; la somme des probabilites vaut 1."
  "|Deux evenements incompatibles ne peuvent pas survenir ensemble : P(A UNION B) = P(A) + P(B)."
  "|Deux evenements independants verifient P(A INTERSECTION B) = P(A) multiplie par P(B)."
  "|La probabilite conditionnelle P(A sachant B) vaut P(A INTERSECTION B) divise par P(B)."
  "|Un arbre pondere represente les etapes successives et permet de multiplier les probabilites le long des branches."
  "|La formule des probabilites totales somme les probabilites conditionnelles ponderees par celles des sous-groupes."
  "|Une variable aleatoire associe un nombre a chaque issue ; son esperance est la moyenne theorique a long terme."
  "|Un intervalle de confiance donne une plage de valeurs plausibles pour un parametre, avec un niveau de confiance."
  "|En sante, ces outils aident a lire un risque, un taux d'incidence ou le resultat d'un test de depistage."),
[QC("Quelle est la probabilité d'un événement impossible ?", "0~0,5~1~2", 0,
     "Un evenement impossible a une probabilite nulle."),
 QC("Dans un univers équiprobable, comment calculer une probabilité ?", "Issues favorables multipliées par le total~Issues favorables divisées par le total~Total moins les issues~Une soustraction", 1,
     "P(A) = nombre d'issues favorables sur nombre total d'issues."),
 QC("Que vérifient deux événements indépendants ?", "P(A∩B) = P(A)+P(B)~P(A∩B) = P(A)×P(B)~P(A) = P(B)~A et B sont incompatibles", 1,
     "L'independance se traduit par la multiplication des probabilites."),
 QC("À quoi sert un arbre pondéré ?", "À compter les pages~À calculer des probabilités composées~À tracer une droite~À arrondir des valeurs", 1,
     "On multiplie les probabilites le long de chaque branche puis on additionne les issues favorables."),
 QC("Que vaut la somme des probabilités d'une loi ?", "0~1~100~Dépend de l'échantillon", 1,
     "La somme des probabilites d'une loi complete vaut 1."),
 QC("Comment interpréter une espérance ?", "Comme le résultat certain~Comme la moyenne théorique à long terme~Comme le maximum possible~Comme un pourcentage", 1,
     "L'esperance est la moyenne ponderee des valeurs de la variable aleatoire."),
 QC("Quel niveau de confiance correspond le plus souvent à z = 1,96 ?", "90 %~95 %~99 %~50 %", 1,
     "Le quantile 0,975 de la loi normale centrée réduite vaut environ 1,96.")],
[QT("Dans un service, 30 % des résidents pratiquent une activité physique et 20 % sont diabétiques. On suppose les deux événements indépendants. Calculer la probabilité qu'un résident soit à la fois actif et diabétique.",
     "Soit A l'evenement « pratique une activite physique » avec P(A) = 0,30, et D l'evenement « diabetique » avec P(D) = 0,20. L'independance donne P(A INTERSECTION D) = P(A) × P(D) = 0,30 × 0,20 = 0,06, soit 6 % des residents. On peut representer la situation par un arbre : la premiere branche A a une probabilite 0,30, et sur cette branche la probabilite de D reste 0,20 puisque les evenements sont independants. On verifiera que le resultat est inferieur a chacune des deux probabilites, ce qui est bien le cas.",
     "On attend l'utilisation correcte de l'independance, le calcul 0,06 et une verification de coherence."),
 QT("Expliquer la différence entre probabilité conditionnelle et probabilité d'un événement, puis donner un exemple lié à un test de dépistage.",
     "La probabilite simple P(A) est calculee sur l'ensemble de la population : par exemple la proportion de personnes atteintes d'une maladie. La probabilite conditionnelle P(A sachant B) ne porte plus que sur le sous-groupe ou l'evenement B est realise : par exemple la probabilite d'etre malade sachant que le test est positif. Elle se calcule par P(A INTERSECTION B) / P(B). Cette distinction est essentielle pour interpreter un test : une sensibilité élevée ne signifie pas qu'une personne positive est surement malade, car la prevalence de la maladie dans la population influence le resultat. C'est la formule de Bayes qui permet de reviser la probabilite initiale grace au resultat du test.",
     "La réponse doit definir les deux probabilites, donner la formule et expliquer l'influence de la prevalence.")],
C("Les probabilités quantifient l'incertitude : on identifie l'univers, la loi, puis on calcule selon les relations entre événements.",
  "P(A) = issues favorables / issues totales (univers équiprobable)",
  "indépendance : P(A∩B) = P(A)×P(B) · conditionnelle : P(A|B) = P(A∩B)/P(B)",
  "Univers~Ensemble des issues~Événement~Partie de l'univers~Indépendance~Produit des probabilités~Conditionnelle~Restriction à un sous-groupe~Espérance~Moyenne théorique",
  "Définir l'expérience et l'univers~Repérer les événements~Tester indépendance ou incompatibilité~Construire un arbre si nécessaire~Calculer et interpréter",
  "Confondre incompatibilité et indépendance|Oublier que la somme des probabilités vaut 1|Multiplier au lieu de diviser pour la conditionnelle|Interpréter une probabilité comme une certitude",
  "0,30 et 0,20~Produit 0,06~Indépendance~P(A∩B)=P(A)P(B)~1,96~Niveau 95 %~Arbre pondéré~Multiplication des branches~Espérance~Moyenne pondérée",
  "Incompatibles~A et B ne peuvent coexister~Indépendants~La réalisation de l'un n'influence pas l'autre",
  "Probabilité simple~Sur toute la population~Conditionnelle~Sur un sous-groupe connu"))

# ============================================================ HG1
add("HG1", "Les grandes étapes de la protection sociale en France", "Histoire-Géographie", ["1re pro"],
S("La protection sociale designe l'ensemble des mecanismes qui protegent les individus contre les risques de la vie."
  "|Elle couvre la sante, la vieillesse, l'invalidite, la famille, le chomage et les accidents du travail."
  "|Les premiers systemes d'assurance sociale apparaissent au XIXe siecle avec les societes de secours mutuel."
  "|La loi du 9 avril 1898 instaure la reprobation des accidents du travail : l'employeur est responsable."
  "|Les lois sociales de 1930 creent les assurances sociales pour les salaries."
  "|Le Front populaire de 1936 etablit les conges payes et renforce les conventions collectives."
  "|Apres 1945, la Securite sociale est creee par les ordonnances d'octobre 1945 : elle repose sur la solidarite nationale."
  "|Le systeme francais est un regime mixte : contributions professionnelles et impots alimentent les caisses."
  "|Les années 1980-1990 voient le developpement des prestations familiales et de la couverture maladie."
  "|La CMU de 1999, puis la CMU-C et l'ACS, visent a garantir l'acces aux soins des personnes precaires."
  "|La loi du 4 mars 2002 renforce les droits des malades et creer la Haute Autorité de sante."
  "|Aujourd'hui, le systeme fait face au vieillissement et a la maitrise des depenses, tout en maintenant l'egalite d'acces."),
[QC("Quelle loi de 1898 fonde la réparation des accidents du travail ?", "La loi du 9 avril 1898~La loi de 1901~La loi de 1930~La loi de 1945", 0,
     "La loi du 9 avril 1898 met la responsabilite de l'accident du travail a la charge de l'employeur."),
 QC("Quand la Sécurité sociale est-elle créée ?", "En 1789~En 1898~En 1945~En 2002", 2,
     "Les ordonnances d'octobre 1945 instituent la Securite sociale."),
 QC("Quel principe fonde la Sécurité sociale ?", "La charité individuelle~La solidarité nationale~Le bénévolat seul~L'assurance privée obligatoire", 1,
     "La Securite sociale repose sur la mutualisation et la solidarite nationale."),
 QC("Qu'est-ce que la CMU-C ?", "Une caisse de retraite~Une couverture maladie complémentaire pour les personnes précaires~Un impôt~Une convention collective", 1,
     "La CMU-C garantissait une prise en charge complementaire des frais de sante."),
 QC("Quel événement de 1936 est lié aux droits sociaux ?", "La création de la CMU~Les congés payés~La Haute Autorité de santé~La réforme des retraites", 1,
     "Le Front populaire a instaure les conges payes en 1936."),
 QC("Que recouvre la protection sociale ?", "Uniquement les retraites~La santé, la famille, le chômage et la vieillesse~Seulement l'hospitalisation~Les seuls accidents du travail", 1,
     "Elle couvre l'ensemble des risques sociaux de la vie."),
 QC("Quel défi actuel est mentionné ?", "La baisse de l'espérance de vie~Le vieillissement et la maîtrise des dépenses~La fin des caisses~Le retour du travail des enfants", 1,
     "Le vieillissement de la population et le cout de la sante sont les grands enjeux actuels.")],
[QT("Expliquer la différence entre un régime contributif et un régime solidaire, en donnant un exemple chacun.",
     "Un regime contributif est finance par des cotisations verse es par les salaries et les employeurs : les prestations sont liees a l'activite professionnelle et aux cotisations, comme l'assurance maladie des salaries ou les allocations chomage. Un regime solidaire est finance par l'impot ou par des contributions generales et beneficie a tous sans contrepartie directe : c'est le cas de la solidarite vieillesse ou de la prise en charge des personnes sans ressources. Le systeme francais melange les deux logiques : la Securite sociale repose sur les cotisations, tandis que certaines prestations comme le RSA ou la CMU-C relevent de la solidarite nationale. Cette mixite explique les debats sur le financement et l'equite entre generations.",
     "On attend la definition des deux regimes, un exemple pour chacun et la mention du caractere mixte du systeme francais."),
 QT("Montrer comment l'histoire de la protection sociale éclaire le métier d'accompagnant en établissement.",
     "L'histoire montre que la prise en charge de la dependance est progressivement passee de la charite individuelle a un droit collectif. Les lois de 1898 et de 1930 ont reconnu des risques professionnels, la Securite sociale de 1945 a generalise l'acces aux soins, et la loi de 2002 a affirme les droits des malades. Un accompagnant travaille donc dans un systeme ou la personne a des droits opposables, et non dans une logique de bienveillance discretionnaire. Cela explique l'importance des procedures, des transmissions ecrites et du respect du projet individualise : l'accompagnement s'inscrit dans une continuite historique de reconnaissance de la dignite et de l'egalite d'acces.",
     "On attend le passage de la charite au droit, quelques dates cles et le lien avec les pratiques professionnelles.")],
C("La protection sociale est passée de l'entraide privée à un droit collectif financé par la solidarité nationale.",
  "protection sociale = santé + famille + vieillesse + chômage + accidents du travail",
  "1898 : accidents du travail · 1930 : assurances sociales · 1945 : Sécurité sociale · 2002 : droits des malades",
  "1898~Accidents du travail~Responsabilité employeur~1930~Assurances sociales~Salariés~1945~Sécurité sociale~Solidarité nationale",
  "Repérer la période et le texte~Identifier le risque couvert~Déterminer le mode de financement~Relier à la situation actuelle~Expliquer l'effet sur les droits",
  "Confondre assurance et assistance|Oublier que le système est mixte|Placer la CMU en 1945|Réduire la protection sociale à la retraite",
  "1898~Loi sur les accidents~1936~Congés payés~1945~Ordonnances fondatrices~1999~CMU~2002~Loi sur les droits des malades",
  "Régime contributif~Financé par cotisations~Prestations liées au travail~Régime solidaire~Financé par l'impôt~Accès pour tous",
  "Charité~Aide discrétionnaire~Droit social~Prestation opposable"))

# ============================================================ HG2
add("HG2", "L'évolution de la santé publique et de la vaccination", "Histoire-Géographie", ["Terminale pro"],
S("La sante publique vise a ameliorer la sante des populations par la prevention, l'organisation des soins et la surveillance."
  "|Au XIXe siecle, les progres de l'hygiene urbaine reduisent les maladies infectieuses : egouts, eau potable, ventilation."
  "|Louis Pasteur et Robert Koch developpent la bacteriologie et la theorie des germes."
  "|La vaccine contre la variole, mise au point par Edward Jenner en 1796, ouvre la voie de la vaccination."
  "|Au XXe siecle, les vaccins contre la diphtherie, le tetanos, la poliomyelite et la rougeole generalisent la prevention."
  "|Le programme national de vaccination est officialise apres 1945 et rend obligatoires plusieurs vaccins."
  "|L'Organisation mondiale de la sante est creee en 1948 ; la variole est eradiquee en 1980."
  "|La loi du 4 mars 2002 organise la protection maternelle et infantile et les droits des malades."
  "|Le calendrier vaccinal est actualise chaque annee pour adapter les recommandations."
  "|La couverture vaccinale mesure la proportion de la population correctement vaccinee."
  "|Une couverture insuffisante favorise la resurgence d'epidemies, malgre l'existence d'un vaccin."
  "|L'historique de la sante publique montre que la prevention et la confiance sont aussi essentielles que le traitement."),
[QC("Qui a mis au point la vaccine contre la variole ?", "Louis Pasteur~Edward Jenner~Robert Koch~Albert Calmette", 1,
     "Edward Jenner realise la premiere vaccination contre la variole en 1796."),
 QC("Quand l'OMS est-elle créée ?", "1796~1898~1948~1980", 2,
     "L'Organisation mondiale de la sante est fondee en 1948."),
 QC("Quelle maladie a été éradiquée en 1980 ?", "La rougeole~La poliomyélite~La variole~Le tétanos", 2,
     "L'OMS a declare l'eradication de la variole en 1980."),
 QC("Que mesure la couverture vaccinale ?", "Le nombre de lits d'hôpital~La proportion de personnes correctement vaccinées~Le prix des vaccins~Le nombre de médecins", 1,
     "C'est la part de la population ayant recu les doses recommandees."),
 QC("Quel progrès du XIXe siècle a réduit les maladies infectieuses ?", "Les antibiotiques~L'hygiène urbaine et l'eau potable~La chirurgie~Les vaccins obligatoires", 1,
     "Les travaux d'assainissement ont considerablement reduit la mortalite infectieuse."),
 QC("À quoi sert le calendrier vaccinal ?", "À fixer les prix~À actualiser chaque année les recommandations~À remplacer le médecin~À fermer les écoles", 1,
     "Le calendrier vaccinal est revise annuellement selon les donnees epidemiologiques."),
 QC("Pourquoi une couverture vaccinale insuffisante est-elle un problème ?", "Elle coûte plus cher~Elle permet la résurgence d'épidémies~Elle rend les vaccins inefficaces~Elle supprime les obligations", 1,
     "Un seuil de couverture insuffisant laisse circuler l'agent infectieux.")],
[QT("Expliquer pourquoi l'hygiène urbaine a précédé la vaccination dans la baisse de la mortalité au XIXe siècle.",
     "Au XIXe siecle, la theorie des germes n'etait pas encore etablie et peu de vaccins existaient. Les grandes villes etaient confrontees a des epidemies de cholera, de typhoide et de variole, favorisees par l'absence d'egouts et d'eau potable. Les travaux d'assainissement, la construction de réseaux d'egouts et l'amelioration de l'habitat ont agi directement sur la transmission des agents pathogenes, avant meme que l'on sache les identifier. Pasteur et Koch ont ensuite donne une explication scientifique a ces observations, ce qui a permis de developper des vaccins et des traitements cibles. L'histoire montre que les mesures d'hygiene et la vaccination sont complementaires.",
     "On attend la chronologie, le role de l'assainissement et le lien avec la decouverte des germes."),
 QT("Dans le cadre d'une action d'éducation à la santé, expliquer comment présenter la vaccination à un public adulte hésitant.",
     "On commence par ecouter les questions et les representations, sans juger, afin de comprendre les sources d'hesitation : peur des effets indesirables, defiance envers les institutions, souvenirs d'obligations passees. On donne ensuite des informations simples et verifiees en s'appuyant sur des sources officielles : calendrier vaccinal, recommandations de la Haute Autorite de sante, donnees de couverture. On explique l'interet collectif : proteger les personnes fragiles qui ne peuvent pas etre vaccinees, comme les immunodeprimes. On evite le discours autoritaire, on propose un entretien individuel avec un professionnel de sante et on laisse un document ecrit. L'evaluation de l'action se fera sur la comprehension et le nombre de personnes ayant pris rendez-vous, pas sur le seul nombre de vaccins administres.",
     "On attend une demarche d'ecoute, des sources fiables, l'argument de protection collective et une evaluation.")],
C("La santé publique a d'abord agi sur l'environnement, puis sur l'immunité : prévention et confiance restent indissociables.",
  "couverture vaccinale = personnes correctement vaccinées / population concernée",
  "1796 Jenner · 1948 OMS · 1980 éradication de la variole · calendrier vaccinal actualisé chaque année",
  "Hygiène urbaine~Eau et égouts~Baisse de la mortalité~Bactériologie~Pasteur et Koch~Théorie des germes~Vaccination~ Immunité collective~Prévention",
  "Situer la période~Identifier la maladie visée~Expliquer le moyen de prévention~Relier aux acteurs institutionnels~Évaluer l'impact sur la population",
  "Confondre hygiène et vaccination|Placer l'OMS au XIXe siècle|Croire qu'un vaccin éradique seul une maladie|Ignorer le rôle de la confiance",
  "1796~Vaccine de Jenner~1948~Création de l'OMS~1980~Variole éradiquée~Chaque année~Calendrier mis à jour~95 %~Objectif de couverture",
  "Prévention~Agir avant la maladie~Traitement~Agir après le diagnostic",
  "Vaccination~Immunité acquise~Hygiène~Réduction des contacts"))

# ============================================================ HG3
add("HG3", "Vieillissement et politiques de l'autonomie", "Histoire-Géographie", ["Terminale pro"],
S("Le vieillissement de la population est une evolution demographique majeure : la part des personnes agees augmente."
  "|Il resulte de l'augmentation de l'esperance de vie et de la baisse de la natalite."
  "|L'esperance de vie a franchi 80 ans en France au debut du XXIe siecle."
  "|On distingue l'esperance de vie en bonne sante de l'esperance de vie totale."
  "|La dependance est l'incapacite relative a accomplir les actes de la vie quotidienne."
  "|La grille AGGIR mesure l'autonomie : elle classe de 1 (dependance totale) a 6 (autonomie)."
  "|Les actes de la vie quotidienne comprennent la toilette, l'habillage, l'alimentation, la locomotion et les transfers."
  "|L'Allocation personnalisee d'autonomie, creee en 2002, finance des aides pour les personnes agees dependantes."
  "|Les EHPAD accueillent les personnes qui ne peuvent plus rester a domicile en toute securite."
  "|Le maintien a domicile est privilégie par les politiques publiques, avec des services de soins et d'aide."
  "|La silver economie designe les activites economiques liees au vieillissement, dont la domotique."
  "|Les enjeux sont le financement, les conditions de travail des professionnels et le respect du projet de vie."),
[QC("Quel seuil l'espérance de vie en France a-t-elle franchi au début du XXIe siècle ?", "70 ans~75 ans~80 ans~90 ans", 2,
     "L'esperance de vie a depasse 80 ans au debut du XXIe siecle."),
 QC("À quoi sert la grille AGGIR ?", "À mesurer la douleur~À évaluer l'autonomie~À calculer un budget~À choisir un médicament", 1,
     "La grille AGGIR classe la dependance de 1 a 6."),
 QC("Quel niveau AGGIR correspond à la dépendance totale ?", "1~3~4~6", 0,
     "Le niveau 1 designe la dependance totale, le niveau 6 l'autonomie."),
 QC("Quand l'APA a-t-elle été créée ?", "1945~1980~2002~2015", 2,
     "L'Allocation personnalisee d'autonomie a ete instituee en 2002."),
 QC("Que désigne le maintien à domicile ?", "Une hospitalisation~Le fait de rester chez soi avec des aides adaptées~Un EHPAD~Une cure", 1,
     "Le maintien a domicile associe l'environnement familier et des services d'aide et de soins."),
 QC("Qu'est-ce que la silver économie ?", "L'économie des jeunes~Les activités liées au vieillissement~Le marché du sport~L'industrie automobile", 1,
     "Elle regroupe les biens et services destines aux personnes agees, dont la domotique."),
 QC("Quel acte n'est pas un acte de la vie quotidienne ?", "La toilette~L'alimentation~Les transferts~La signature d'un contrat", 3,
     "Les actes de la vie quotidienne concernent les soins personnels et la mobilite.")],
[QT("Expliquer la différence entre espérance de vie et espérance de vie en bonne santé, puis en tirer une conséquence pour l'accompagnement.",
     "L'esperance de vie indique le nombre moyen d'annees vecues a la naissance, toutes choses egales par ailleurs. L'esperance de vie en bonne sante compte seulement les annees vecues sans limitation fonctionnelle importante. L'ecart entre les deux represente une periode de dependance ou de maladie, plus ou moins longue selon les individus. Pour l'accompagnement, cela signifie qu'il ne suffit pas de prolonger la vie : il faut maintenir l'autonomie et la qualite de vie. Les activites d'acquisition ou de maintien de l'autonomie, la prevention des chutes et l'adaptation du logement deviennent essentielles. L'objectif n'est pas seulement de soigner, mais de permettre a la personne de continuer a faire ses choix.",
     "On attend la definition des deux indicateurs, l'ecart et la consequence sur les pratiques."),
 QT("Un résident AGGIR 3 souhaite rentrer chez lui avec des aides. Présenter les éléments à prendre en compte.",
     "Un niveau AGGIR 3 correspond a une dependance partielle : la personne a besoin d'aide pour plusieurs actes de la vie quotidienne, mais conserve des capacites. Le projet de vie doit etre au centre de la decision : on interroge la personne sur ses attentes, ses habitudes et ses priorités. On evalue ensuite le logement : accessibility, salle de bain, escaliers, domotique possible. On organise les aides : service d'aide a domicile, soins infirmiers, portage de repas, teleassistance. On verifie le financement, notamment l'Allocation personnalisee d'autonomie, et on coordonne les intervenants. Enfin, on prevoit une periode d'essai et des points de suivi pour ajuster le dispositif. Le role de l'accompagnant est de faire le lien entre le souhait de la personne et les moyens disponibles.",
     "On attend le lien avec l'AGGIR, le respect du projet de vie, l'evaluation du logement et la coordination des aides.")],
C("Le vieillissement démographique transforme les métiers de l'accompagnement : l'objectif est de maintenir l'autonomie, pas seulement de prolonger la vie.",
  "AGGIR : 1 = dépendance totale · 6 = autonomie",
  "ESPÉRANCE de vie en bonne santé = années sans limitation fonctionnelle",
  "Vieillissement~Part des personnes âgées~Espérance de vie~Durée de vie~AGGIR~Niveau de dépendance~Autonomie~Capacité d'agir~APA~Financement des aides",
  "Évaluer l'autonomie avec la grille~Écouter le projet de vie~Examiner le logement~Organiser les aides et le financement~Suivre et réajuster",
  "Confondre AGGIR et mesure de la douleur|Croire que le maintien à domicile est toujours possible|Ignorer le projet de la personne|Oublier la coordination des intervenants",
  "AGGIR 1~Dépendance totale~AGGIR 6~Autonomie~APA~Aide financière~80 ans~Espérance de vie~Domotique~Aide technique",
  "Maintien à domicile~Environnement familier~EHPAD~Accueil collectif",
  "Espérance de vie~Durée de vie~Espérance en bonne santé~Années sans limitation"))

# ============================================================ HG4
add("HG4", "La question du handicap : de l'institution à l'inclusion", "Histoire-Géographie", ["1re pro"],
S("Le handicap est defini comme une limitation d'activite subie par une personne en situation d'impossibilite ou de difficulté."
  "|La loi du 11 février 2005 affirme le droit a la compensation des consequences du handicap."
  "|Elle pose le principe de l'egalite des droits et des chances, de la participation et de la citoyennete."
  "|Avant cette loi, les personnes handicapees etaient souvent accueillies dans des institutions separées."
  "|L'institution specialisee offrait un cadre protege mais pouvait limiter la vie sociale et l'autonomie."
  "|L'inclusion vise a permettre a la personne de vivre dans la societe avec les adaptations necessaires."
  "|La classification internationale des handicaps distingue deficience, incapacite et desavantage."
  "|Une deficience est une alteration d'une structure ou d'une fonction ; l'incapacite en est la consequence fonctionnelle."
  "|Le desavantage social resulte des obstacles environnementaux et des attitudes de la societe."
  "|La notion de situation de handicap remplace celle de personne handicapée pour montrer le role de l'environnement."
  "|Un environnement inaccessible transforme une différence en handicap : c'est le modele social du handicap."
  "|En ASSP, l'accompagnement consiste a compenser, adapter et favoriser la participation plutot qu'a protéger en excluant."),
[QC("Quelle loi de 2005 est un texte clé du handicap ?", "La loi du 4 mars 2002~La loi du 11 février 2005~La loi de 1898~La loi de 1945", 1,
     "La loi du 11 fevrier 2005 organise la compensation et l'egalite des droits."),
 QC("Quel principe cette loi affirme-t-elle ?", "La séparation institutionnelle~L'égalité des droits et des chances~L'obligation de retraite~Le travail bénévole", 1,
     "Elle affirme l'egalite des droits, la participation et la citoyennete."),
 QC("Que désigne une déficience ?", "Un obstacle administratif~Une altération d'une fonction ou d'une structure~Une difficulté financière~Un refus d'embauche", 1,
     "La deficience est l'atteinte organique ou fonctionnelle."),
 QC("Qu'est-ce qu'un désavantage social ?", "Une conséquence liée à l'environnement~Une maladie~Un diagnostic~Un traitement", 0,
     "Le desavantage resulte des barriers et des representations de la societe."),
 QC("Quel modèle explique que l'environnement crée le handicap ?", "Le modèle médical~Le modèle social~Le modèle religieux~Le modèle économique", 1,
     "Le modele social met l'accent sur les obstacles environnementaux et les attitudes."),
 QC("Que vise l'inclusion ?", "À regrouper les personnes dans un établissement~À permettre la participation dans la société~À supprimer les aides~À éviter tout contact social", 1,
     "L'inclusion vise la participation et l'egalite dans la societe ordinaire."),
 QC("Quel est le rôle de l'accompagnant selon cette logique ?", "Protéger en excluant~Compenser, adapter et favoriser la participation~Décider à la place de la personne~Refuser les aides techniques", 1,
     "L'accompagnement vise l'autonomie et la participation, dans le respect du projet de la personne.")],
[QT("Expliquer la différence entre le modèle médical et le modèle social du handicap.",
     "Le modele medical considere le handicap comme une consequence directe de la deficience : l'action vise alors a traiter, reeducer ou reparer l'atteinte, et la personne est définie par son diagnostic. Le modele social considere que la limitation principale vient de l'environnement : un escalier rend une personne en fauteuil dependante, alors qu'une rampe lui rend son autonomie. L'action porte alors sur l'accessibilite, les adaptations, les representations et les droits. Les deux modeles ne s'excluent pas : les soins restent utiles, mais le modele social a transforme les politiques publiques, notamment avec la loi du 11 fevrier 2005. Pour un accompagnant, cela signifie qu'il doit autant agir sur l'environnement que sur la personne.",
     "On attend l'opposition des deux approches, des exemples concrets et le lien avec la loi de 2005."),
 QT("Dans un établement, une personne en situation de handicap refuse l'activité proposée. Comment analyser la situation ?",
     "On commence par vérifier si le refus exprime un choix personnel ou une difficulté non dite : activite trop bruyante, horaire inadapte, absence d'aide technique, relation tendue avec le groupe. On ecoute la personne sans la forcer, car le respect du projet individualise implique de prendre son avis au serieux. On observe ensuite l'environnement : accessibilite du lieu, clarté des consignes, presence d'un accompagnement suffisant. On propose des adaptations concretes et on reformule l'activite avec elle. On en informe l'equipe pluriprofessionnelle et on trace la decision dans les transmissions. Si le refus persiste, on respecte la decision et on propose une alternative, car l'inclusion n'impose pas la participation a tout prix mais rend les choix possibles.",
     "On attend l'ecoute, l'analyse de l'environnement, l'adaptation, le travail d'equipe et le respect du choix.")],
C("Le handicap naît de la rencontre entre une déficience et un environnement : l'inclusion agit sur l'environnement et sur les droits.",
  "déficience → incapacité → désavantage (classification internationale)",
  "loi du 11 février 2005 : compensation, égalité des droits, participation",
  "Déficience~Altération d'une fonction~Incapacité~Limitation d'activité~Désavantage~Obstacle social~Situation de handicap~Rôle de l'environnement~Compensation",
  "Écouter la personne~Repérer la déficience et ses conséquences~Analyser les obstacles du lieu~Proposer des adaptations~Évaluer la participation",
  "Définir la personne par son diagnostic|Forcer la participation|Ignorer l'accessibilité du lieu|Décider sans l'équipe pluriprofessionnelle",
  "Loi de 2005~Droit à la compensation~Rampe~Adaptation d'accès~AGGIR~Autonomie~Institution~Cadre protégé~Inclusion~Participation",
  "Modèle médical~Agir sur la personne~Traitement et rééducation~Modèle social~Agir sur l'environnement~Accessibilité et droits",
  "Institution~Accueil séparé~Inclusion~Vie dans la société"))

# ============================================================ AN1
add("AN1", "Se présenter et décrire son environnement de travail", "Anglais", ["2nde pro"],
S("Se presenter en anglais, c'est donner son nom, son age, sa formation et son projet professionnel."
  "|La formule « My name is ... » est plus neutre que « I am ... » dans une situation formelle."
  "|Le verbe « to be » se conjugue : I am, you are, he/she is, we are, they are."
  "|Pour parler de sa formation, on utilise « I am training to be a carer » ou « I study nursing assistance »."
  "|« I am in my second year » indique l'annee d'etude ; « I am doing a work placement » designe le stage."
  "|Le present simple decrit une habitude ou une situation permanente : « I work in a nursing home. »"
  "|Le present continuous decrit une action en cours : « I am helping a resident. »"
  "|Les articles « a » et « the » ne s'emploient pas de la meme facon : « a nursing home » puis « the nursing home »."
  "|Les adjectifs se placent avant le nom : « a quiet room », « an elderly resident »."
  "|Pour decrire un lieu, on utilise « there is » au singulier et « there are » au pluriel."
  "|Les numeros et les heures s'ecrivent differemment : « 8:30 » se lit « eight thirty »."
  "|Dans un echange professionnel, la politesse se marque par « please », « thank you » et un ton calme."),
[QC("Quelle formule est la plus neutre pour se présenter ?", "I'm called...~My name is...~Call me...~I say...", 1,
     "« My name is » convient dans une situation formelle."),
 QC("Quelle est la conjugaison correcte de « to be » à la troisième personne ?", "He are~He is~He am~He be", 1,
     "On dit he is, she is, it is."),
 QC("Que signifie « I am doing a work placement » ?", "Je travaille à l'hôpital~Je fais un stage~Je suis diplômé~Je cherche un emploi", 1,
     "A work placement est une periode de formation en milieu professionnel."),
 QC("Quel temps décrit une habitude ?", "Present continuous~Present simple~Past simple~Future", 1,
     "Le present simple exprime une habitude ou une situation permanente."),
 QC("Comment dire « il y a trois résidents » ?", "There is three residents~There are three residents~There have three residents~Is there three residents", 1,
     "On emploie there are avec un pluriel."),
 QC("Quel est l'ordre correct de l'adjectif ?", "A room quiet~A quiet room~Quiet a room~A room of quiet", 1,
     "En anglais, l'adjectif qualificatif precede le nom."),
 QC("Comment se lit « 8:30 » ?", "Eight and thirty~Eight thirty~Thirty eight~Eight past thirty", 1,
     "L'heure se dit en premier : eight thirty.")],
[QT("Rédiger une courte présentation de dix lignes pour un stage en EHPAD, en utilisant le présent simple et le present continuous.",
     "« My name is Lea Martin. I am seventeen years old and I am in my first year of vocational training in health and personal care. I am doing a four-week work placement in a nursing home near my school. The home has got sixty beds and there are three wards. I work with a qualified care assistant. Every morning, I help with breakfast and I make the beds. At the moment, I am learning how to give a wash safely. I like talking to the residents because I want to become a professional carer. Thank you for listening. » Le present simple decrit les situations permanentes et les habitudes ; le present continuous « I am learning » marque une action en cours pendant le stage.",
     "On attend nom, age, formation, stage, description du lieu, habitudes, action en cours et formule de politesse."),
 QT("Corriger les phrases suivantes et expliquer la règle : « There is two nurses. I work in the nursing home since Monday. She is a old resident. »",
     "Les formes correctes sont : « There are two nurses », car le sujet est pluriel ; « I have worked in the nursing home since Monday », car since introduit un point de depart et exige le present perfect ; « She is an old resident », car le adjectif « old » commence par une voyelle et l'article indefini devient « an ». La premiere regle concerne l'accord de there is/there are, la deuxieme l'emploi du present perfect avec since, et la troisieme le choix de a ou an devant une voyelle. Ces trois points sont frequents dans une presentation ecrite et meritent une relecture systematique.",
     "On attend trois corrections et l'énoncé de la règle correspondante pour chacune.")],
C("Se présenter, c'est combiner des formules simples et le bon temps : habitudes au présent simple, actions en cours au present continuous.",
  "I am / you are / he is · there is (singulier) / there are (pluriel)",
  "a devant une consonne · an devant une voyelle · since + present perfect",
  "Présentation~Nom, âge et formation~My name is~Stage~Work placement~En cours d'action~Present continuous~Habitude~Present simple~Politesse",
  "Donner son identité~Préciser sa formation~Situer son stage~Décrire le lieu avec there is/are~Terminer par une formule polie",
  "Confondre there is et there are|Employer le present simple avec since|Oublier l'article|Placer l'adjectif après le nom",
  "My name is~Présentation formelle~I am doing~Stage en cours~There are~Pluriel~An old resident~Article devant voyelle~8:30~Eight thirty",
  "Present simple~Habitude et fait permanent~Present continuous~Action en cours maintenant",
  "A~Devant consonne~An~Devant voyelle"))

# ============================================================ AN2
add("AN2", "Comprendre une consigne de soins en anglais", "Anglais", ["1re pro"],
S("Une consigne de soins en anglais est un texte court qui decrit un geste a realiser dans un contexte professionnel."
  "|Les verbes d'action les plus frequents sont wash, dress, feed, lift, check et record."
  "|L'impératif exprime une consigne directe : « Wash your hands before the care. »"
  "|La forme « Make sure that ... » introduit une verification a effectuer."
  "|« Do not / Don't » exprime une interdiction : « Don't lift the patient alone. »"
  "|Les expressions de temps indiquent le moment : before, after, during, every morning, twice a day."
  "|Les expressions de lieu precise : in the bathroom, on the bed, near the window."
  "|Les aides techniques se nomment : hoist, wheelchair, walking frame, slide sheet."
  "|La securite est souvent exprimee par « carefully », « slowly » ou « with help »."
  "|« Report any change to the nurse » demande de transmettre une information."
  "|Le vocabulaire medical de base comprend pain, fever, rash, blood pressure et pulse."
  "|Avant d'appliquer une consigne, il faut identifier le verbe, le complément et les conditions de realisation."),
[QC("Que signifie le verbe « to lift » ?", "Laver~Soulever~Nourrir~Habil", 1,
     "To lift signifie soulever ou deplacer une personne ou un objet."),
 QC("Quelle forme exprime une interdiction ?", "Wash your hands~Don't lift the patient alone~Make sure that~Check the temperature", 1,
     "Don't est la forme negative de l'imperatif."),
 QC("Que demande « Report any change to the nurse » ?", "De laver les mains~De prévenir l'infirmier de tout changement~De fermer la porte~De préparer le repas", 1,
     "On doit transmettre toute modification observee a l'infirmier."),
 QC("Quel mot signifie « douleur » ?", "Fever~Pain~Rash~Pulse", 1,
     "Pain designe la douleur ; fever est la fievre, rash une eruption."),
 QC("Quel outil sert à soulever une personne ?", "A slide sheet~A hoist~A thermometer~A wheelchair", 1,
     "Un hoist est un lève-personne ; la slide sheet est un drap de glissement."),
 QC("Que signifie « twice a day » ?", "Une fois par semaine~Deux fois par jour~Tous les matins~Jamais", 1,
     "Twice a day signifie deux fois par jour."),
 QC("Quel adverbe indique une action prudente ?", "Quickly~Carefully~Loudly~Always", 1,
     "Carefully signifie avec precaution.")],
[QT("Traduire en français la consigne : « Wash your hands, put on the gloves and check the water temperature before the wash. Report any redness to the nurse. »",
     "« Lavez-vous les mains, enfilez les gants et vérifiez la température de l'eau avant la toilette. Signalez toute rougeur à l'infirmier. » La consigne se compose de quatre actions a l'imperatif : laver, enfiler, verifier et signaler. Le mot « before » indique l'ordre de realisation : la verification de la temperature doit preceder la toilette. « Any redness » designe une rougeur, quelle qu'elle soit, et « report » impose une transmission. On retrouve les regles de securite et d'hygiene enseignees en pratique professionnelle : protection des mains, verification de la temperature et surveillance de l'etat de la peau.",
     "On attend les quatre actions, le respect de l'ordre et la mention de la transmission."),
 QT("Expliquer la méthode pour aborder une consigne de soins en anglais que l'on ne comprend pas entièrement.",
     "On identifie d'abord les verbes, car ce sont eux qui portent l'action : wash, check, report. On repere ensuite les complements et les expressions de temps ou de lieu, qui preciserent quand et ou agir. On cherche le sens des mots inconnus dans un dictionnaire ou auprès d'un colleague, sans deviner. On reformule la consigne avec ses propres mots dans sa langue, puis on la fait confirmer par le professionnel responsable avant toute application. On ne jamais appliquer une consigne ambiguë sur une personne. Enfin, on note le vocabulaire nouveau dans un carnet pour le reutiliser lors des prochaines situations. Cette demarche respecte les limites de competences et la securite de la personne.",
     "On attend : repérage des verbes, recherche du sens, reformulation, confirmation et refus d'agir dans le doute.")],
C("Une consigne de soins se lit en identifiant d'abord le verbe d'action, puis les conditions de sécurité et de transmission.",
  "impératif : Wash / Check / Report · interdiction : Don't + verbe",
  "before / after / twice a day · carefully · report any change",
  "Verbes d'action~Wash, dress, lift~Impératif~Consigne directe~Interdiction~Don't~Sécurité~Carefully et with help~Transmission~Report to the nurse",
  "Repérer les verbes~Identifier les compléments~Repérer temps et lieu~Vérifier les mots inconnus~Reformuler et faire confirmer",
  "Deviner le sens d'un mot|Appliquer une consigne ambiguë|Oublier la transmission|Confondre before et after",
  "Wash your hands~Hygiène~Don't lift alone~Sécurité~Hoist~Aide technique~Twice a day~Fréquence~Any redness~Signe à signaler",
  "Impératif~Ordre direct~Interdiction~Don't + base verbale",
  "Before~Avant l'action~After~Après l'action"))

# ============================================================ AN3
add("AN3", "Écrire un e-mail professionnel en anglais", "Anglais", ["Terminale pro"],
S("Un e-mail professionnel en anglais suit une structure codee : objet, salutation, corps et formule de cloture."
  "|L'objet, « subject », doit etre court et precis : « Work placement dates »."
  "|La salutation depend du destinataire : « Dear Mrs Smith » si le nom est connu, « Dear Sir or Madam » sinon."
  "|On evite « Hi » dans un echange formel avec un etablissement ou un responsable de stage."
  "|Le corps se compose de paragraphes courts, un theme par paragraphe."
  "|On commence souvent par remercier : « Thank you for your message. »"
  "|La demande se formule poliment : « Could you please send me ... ? » ou « I would like to ... »."
  "|« Can you ... ? » est plus direct et moins formel que « Could you ... ? »."
  "|Les dates s'ecrivent « 3 March 2026 » ou « 03/03/2026 » selon la convention du pays."
  "|La formule de cloture est « Kind regards » ou « Yours sincerely » lorsque le nom est connu."
  "|« Yours faithfully » accompagne « Dear Sir or Madam »."
  "|Avant l'envoi, on verifie l'orthographe, les accents inutiles, la piece jointe et le destinataire."),
[QC("Quel objet d'e-mail est correct ?", "Hello~Work placement dates~A question~Urgent!!!", 1,
     "L'objet doit etre precis et informatif, sans exclamation excessive."),
 QC("Quelle salutation convient si l'on connaît le nom ?", "Dear Sir or Madam~Dear Mrs Smith~Hi everyone~To whom", 1,
     "Quand le nom est connu, on utilise Dear suivi du titre et du nom."),
 QC("Quelle formule est la plus polie ?", "Can you send me...~Could you please send me...~Send me...~I want...", 1,
     "Could you please est la formulation la plus respectueuse."),
 QC("Quelle cloture accompagne « Dear Sir or Madam » ?", "Yours sincerely~Yours faithfully~Kindly yours~Best friend", 1,
     "On emploie Yours faithfully quand le nom du destinataire est inconnu."),
 QC("Que signifie « subject » ?", "Le destinataire~L'objet du message~La signature~La pièce jointe", 1,
     "Subject designe la ligne d'objet de l'e-mail."),
 QC("Quel est un avantage de paragraphes courts ?", "Ils sont plus longs~Ils rendent le message lisible~Ils suppriment la signature~Ils évitent la relecture", 1,
     "Un paragraphe par idee facilite la lecture."),
 QC("Que faut-il vérifier avant l'envoi ?", "La couleur du texte~Le destinataire, l'orthographe et la pièce jointe~Le nombre de mots seulement~L'heure d'envoi", 1,
     "Ces vérifications évitent les erreurs professionnelles courantes.")],
[QT("Rédiger un e-mail pour demander les dates de stage à une responsable de formation, en respectant la structure vue.",
     "Subject: Work placement dates - September 2026. Dear Mrs Smith, Thank you for your message. I am writing to ask about the dates of my work placement in September 2026. Could you please confirm the first day and the total number of weeks? I would also like to know if I need to bring a uniform. Please find attached my training agreement. Kind regards, Lea Martin. Ce message comporte un objet precis, une salutation nominative, une formule de remerciement, deux demandes polies avec « could you please » et « I would like », la mention d'une piece jointe et une cloture adaptee.",
     "On attend les cinq parties, deux demandes polies et la mention de la pièce jointe."),
 QT("Expliquer pourquoi il faut éviter « Hi » et « Can you » dans un e-mail à un responsable d'établissement.",
     "« Hi » est une salutation familiere, adaptee a un collègue ou un ami, mais elle marque une distance insuffisante vis-a-vis d'un responsable d'etablissement ou d'un tuteur de stage. De meme, « Can you ... ? » est une demande directe qui peut paraitre abrupte : elle interroge la capacite de l'interlocuteur plus qu'elle ne formule une requête respectueuse. « Could you please ... ? » ou « I would like to ... » marquent la consideration et laissent de la place a un refus eventuel. Dans un contexte professionnel, ces choices linguistiques contribuent a la posture professionnelle : elles montrent que l'on respecte le rang et le temps de son interlocuteur. On gardera « Hi » et « Can you » pour les echanges informels avec les pairs.",
     "On attend la distinction registre formel / informel et des reformulations polies.")],
C("Un e-mail professionnel est un écrit codifié : objet précis, salutation adaptée, demandes polies et clôture conventionnelle.",
  "Could you please + verbe · I would like to + verbe",
  "Dear Mrs Smith + Yours sincerely · Dear Sir or Madam + Yours faithfully",
  "Objet~Subject précis~Salutation~Dear et titre~Corps~Paragraphes courts~Demande~Could you please~Clôture~Kind regards",
  "Choisir l'objet~Adapter la salutation~Remercier~Formuler la demande poliment~Vérifier avant envoi",
  "Employer Hi avec un responsable|Oublier la pièce jointe|Mélanger plusieurs demandes dans un paragraphe|Confondre sincerely et faithfully",
  "Subject~Work placement dates~Dear Mrs Smith~Salutation formelle~Could you please~Demande polie~Kind regards~Clôture~Attached~Pièce jointe",
  "Yours sincerely~Nom connu~Yours faithfully~Nom inconnu",
  "Can you~Direct et informel~Could you~Pol et formel"))

# ============================================================ EM1
add("EM1", "La laïcité et la liberté de conscience dans l'accompagnement", "EMC", ["1re pro"],
S("La laicite est un principe constitutionnel qui garantit la liberte de conscience et l'egalite de tous devant la loi."
  "|La loi du 9 decembre 1905 separe les Eglises et l'Etat et organise la liberte d'exercice des cultes."
  "|L'article 1er de la Constitution de 1958 affirme que la France est une Republique indivisible, laique, democratique et sociale."
  "|La laicite ne signifie pas l'absence de religion, mais la neutralite de l'Etat et des services publics."
  "|Les agents des services publics sont tenus a une obligation de neutralite dans l'exercice de leurs fonctions."
  "|Les usagers, eux, beneficient de la liberte de conscience et de culte, dans le respect de l'ordre public."
  "|Dans un etablissement de sante, la neutralite s'applique aux professionnels, pas aux personnes accompagnees."
  "|Respecter la liberte de conscience, c'est entendre les croyances sans les partager ni les juger."
  "|Les pratiques religieuses peuvent entrer en tension avec les regles de securite ou d'hygiene."
  "|Dans ce cas, on recherche une adaptation raisonnable, avec l'equipe et le cadre reglementaire."
  "|Les signes d'appartenance des personnels sont encadres par la neutralite de service."
  "|Une posture professionnelle laique implique de ne jamais imposer sa propre conception de la vie."),
[QC("Quelle loi de 1905 organise la séparation des Églises et de l'État ?", "La loi du 9 décembre 1905~La loi du 11 février 2005~La loi du 4 mars 2002~La loi de 1881", 0,
     "La loi du 9 decembre 1905 est la loi de separation des Eglises et de l'Etat."),
 QC("Que garantit la laïcité ?", "L'absence de religion~La liberté de conscience et l'égalité devant la loi~L'obligation de croyance~La supériorité d'une religion", 1,
     "La laicite protege la liberte de croire ou de ne pas croire et l'egalite de tous."),
 QC("À qui s'impose la neutralité dans un service public ?", "Aux seuls usagers~Aux agents dans l'exercice de leurs fonctions~À personne~Aux seuls bénévoles", 1,
     "Les agents publics sont tenus a la neutralite, pas les usagers."),
 QC("Comment un accompagnant doit-il accueillir les croyances d'une personne ?", "En les jugeant~En les écoutant sans les imposer~En les refusant~En les partageant", 1,
     "Il respecte la liberte de conscience sans adhérer ni imposer."),
 QC("Que faire face à une tension entre pratique religieuse et sécurité ?", "Interdire immédiatement~Rechercher une adaptation avec l'équipe~Ignorer la règle~Laisser la personne seule décider", 1,
     "On concilie les droits dans le cadre reglementaire, en equipe."),
 QC("La laïcité est-elle mentionnée dans la Constitution de 1958 ?", "Non~Oui, à l'article 1er~Uniquement dans la loi de 1905~Seulement pour l'école", 1,
     "L'article 1er de la Constitution qualifie la France de Republique laique."),
 QC("Qu'est-ce qu'une obligation de réserve ?", "Le droit de tout dire~La retenue attendue d'un agent dans l'expression de ses opinions~Une interdiction de penser~Une règle pour les usagers", 1,
     "Les agents publics doivent faire preuve de retenue dans leur expression professionnelle.")],
[QT("Expliquer la différence entre neutralité des agents et liberté des usagers dans un établissement de santé.",
     "La neutralite est une obligation qui pese sur les professionnels : dans l'exercice de leurs fonctions, ils ne doivent pas afficher leurs convictions ni les imposer, car ils représentent le service public. La liberte de conscience est un droit des personnes accompagnees : elles peuvent croire ou ne pas croire, prier, porter des signes d'appartenance ou demander des adaptations, dans la limite de l'ordre public et des regles de securite. Un accompagnant peut donc ecouter une personne exprimer sa foi sans la partager, et refuser d'imposer la sienne. Cette distinction evite deux erreurs : exclure la parole de la personne au nom de la laicite, ou imposer sa propre vision au nom du soin.",
     "On attend l'opposition obligation / droit et deux exemples concrets de posture professionnelle."),
 QT("Une famille demande que le repas serve un plat específique pour des raisons religieuses. Comment traiter la demande ?",
     "On ecoute d'abord la demande sans la juger et on la reformule pour etre sur de l'avoir comprise. On verifie ensuite les contraintes du service : reglementation sanitaire, composition des menus, couts et delais de preparation. On consulte le responsable de restauration et l'equipe soignante pour determine si une adaptation est possible sans mettre en cause l'equilibre alimentaire ni l'hygiene. Si oui, on organise la solution et on la trace dans le dossier de la personne. Si non, on explique les raisons avec respect et on propose une alternative. Dans tous les cas, on ne melange pas l'analyse de la demande avec un jugement sur la religion : le principe de laicite impose la neutralite du personnel et le respect de la liberte de conscience de la famille.",
     "On attend écoute, vérification des contraintes, décision collégiale, traçabilité et respect.")],
C("La laïcité protège la liberté de conscience des personnes et impose la neutralité des professionnels du service public.",
  "loi du 9 décembre 1905 · Constitution de 1958, article 1er",
  "neutralité des agents · liberté des usagers · adaptation raisonnable",
  "Laïcité~Liberté de conscience~Neutralité de l'État~Loi de 1905~Séparation des cultes~Agent public~Obligation de neutralité~Usager~Liberté de culte",
  "Écouter sans juger~Identifier la croyance ou la demande~Vérifier le cadre réglementaire~Rechercher une adaptation en équipe~Tracer la décision",
  "Confondre laïcité et absence de religion|Imposer sa croyance|Refuser toute adaptation|Juger la personne croyante",
  "1905~Loi de séparation~Article 1er~République laïque~Agent~Neutralité~Usager~Liberté~Repas~Adaptation possible",
  "Neutralité~Obligation des agents~Liberté de conscience~Droit des personnes",
  "Tolérance~Respect de l'autre~Prosélytisme~Imposition de ses convictions"))

# ============================================================ EM2
add("EM2", "Les droits de la personne et la dignité", "EMC", ["2nde pro"],
S("La dignite humaine est un principe fondamental : elle interdit de traiter une personne comme un objet ou un moyen."
  "|Elle est affirmee par la Declaration universelle des droits de l'homme de 1948 et par la Constitution de 1958."
  "|Les droits de la personne sont universels, inalienables et opposables a tous."
  "|Un droit opposable peut etre invoque devant une autorite ou un juge."
  "|La liberte d'aller et venir, le respect de la vie privee et l'integrite physique sont des droits fondamentaux."
  "|La loi du 4 mars 2002 affirme les droits des malades, dont le droit a l'information et au consentement."
  "|Le consentement doit etre libre, eclaire et peut etre retire a tout moment."
  "|Une personne majeure capable peut refuser un soin, sauf cas d'urgence ou de protection particuliere."
  "|La bienveillance ne remplace pas le droit : on peut etre gentil et pourtant ne pas respecter une liberte."
  "|La maltraitance peut etre physique, verbale, psychologique, financiere ou institutionnelle."
  "|La bientraitance suppose d'ecouter, d'expliquer, de choisir avec la personne et de respecter son rythme."
  "|Un professionnel respectueux de la dignite rend la personne actrice de son accompagnement."),
[QC("Quand la Déclaration universelle des droits de l'homme a-t-elle été adoptée ?", "1789~1945~1948~2002", 2,
     "La Declaration universelle des droits de l'homme a ete adoptee en 1948."),
 QC("Qu'est-ce qu'un droit opposable ?", "Un droit conseillé~Un droit que l'on peut invoquer devant une autorité~Un droit facultatif~Un droit uniquement moral", 1,
     "Un droit opposable peut etre exige et defendu, notamment en justice."),
 QC("Quel droit est affirmé par la loi du 4 mars 2002 ?", "Le droit au travail~Le droit à l'information et au consentement~Le droit de vote~Le droit à la retraite", 1,
     "La loi du 4 mars 2002 renforce les droits des malades."),
 QC("Quand un consentement est-il éclairé ?", "Quand la personne a reçu une information comprise~Quand elle est pressée~Quand le soignant décide~Quand la famille décide", 0,
     "Le consentement eclaire suppose une information claire, comprendre et acceptee librement."),
 QC("Quelle forme de maltraitance est institutionnelle ?", "Une insulte~Une procédure qui suppresses toute initiative de la personne~Une négligence d'hygiène~Un vol", 1,
     "La maltraitance institutionnelle résulte d'un fonctionnement qui efface la personne."),
 QC("Quel geste relève de la bientraitance ?", "Décider à la place de la personne~Expliquer le soin avant de le réaliser~Presser la personne~Ignorer ses préférences", 1,
     "Expliquer et associer la personne sont des gestes de bientraitance."),
 QC("La dignité peut-elle être limitée par une maladie ?", "Oui, toujours~Non, elle reste entière quelle que soit la situation~Seulement en fin de vie~Seulement en institution", 1,
     "La dignite est inalienable : la dependance ou la maladie ne la diminue pas.")],
[QT("Expliquer la différence entre bienveillance et respect des droits dans l'accompagnement.",
     "La bienveillance est une disposition personnelle : on souhaite le bien de l'autre, on est attentionne et gentil. Le respect des droits est une obligation juridique et ethique : il ne depend pas de l'humeur du professionnel et s'impose meme lorsque la relation est tendue. On peut etre bienveillant et pourtant imposer un soin sans consentement, parler de la personne sans son accord ou decider a sa place. A l'inverse, le respect des droits impose d'informer, d'ecouter, de demander l'accord et de tracer les decisions. La bienveillance devient professionnelle lorsqu'elle se met au service des droits et non de l'envie de faire du bien coûte que coûte.",
     "On attend la distinction intention / obligation et un exemple ou la gentillesse ne suffit pas."),
 QT("Une résidente refuse la toilette proposée à 9 heures. Comment réagir dans le respect de sa dignité ?",
     "On ne force pas le geste. On s'arrete, on remercie la personne de s'etre exprimee et on lui demande si elle souhaite en parler : est-elle fatiguee, a-t-elle peur, prefere-t-elle un autre horaire ou une autre personne ? On propose de revenir plus tard, en respectant son rythme. On explique calmement pourquoi la toilette est importante pour sa sante et son confort, sans la menacer ni la culpabiliser. On trace le refus et les raisons dans les transmissions et on en informe l'infirmier si le refus se repete, car il peut reveler une douleur ou une depression. Le projet individualise peut prevoir des preferences d'horaire : la dignite se traduit ici par le choix laissé a la personne, dans le cadre de la securite et de l'hygiene.",
     "On attend : pas de contrainte, ecoute, recherche des motifs, alternative, transmission et lien avec le projet.")],
C("La dignité est inaliénable : l'accompagnement doit rendre la personne actrice de ses choix, même lorsqu'elle est dépendante.",
  "droit opposable = droit que l'on peut invoquer devant une autorité",
  "1948 : Déclaration universelle · 2002 : droits des malades · consentement libre et éclairé",
  "Dignité~Principe inaliénable~Droits~Universels et opposables~Consentement~Libre et éclairé~Bientraitance~Écoute et respect~Maltraitance~Atteinte à la personne",
  "Reconnaître la personne~Informer clairement~Demander le consentement~Respecter le refus~Transmettre et réévaluer",
  "Confondre gentillesse et droit|Forcer un soin au nom du bien|Ignorer un refus|Parler de la personne devant elle",
  "1948~Déclaration universelle~2002~Loi sur les droits des malades~Consentement~Accord libre~Refus~Droit à respecter~Bientraitance~Posture quotidienne",
  "Bienveillance~Intention personnelle~Respect des droits~Obligation professionnelle",
  "Maltraitance~Atteinte physique ou verbale~Bientraitance~Respect et écoute"))

# ============================================================ EM3
add("EM3", "La citoyenneté et la participation sociale", "EMC", ["Terminale pro"],
S("La citoyennete est le statut de la personne qui appartient a une communaute politique et en respecte les regles."
  "|Elle comporte des droits, comme le vote, et des devoirs, comme le respect des lois et des autres."
  "|La participation sociale designe l'implication d'une personne dans la vie de la cite, du quartier ou de l'etablissement."
  "|Elle peut prendre la forme d'un vote, d'une association, d'un conseil de la vie sociale ou d'une petition."
  "|Le conseil de la vie sociale, present dans les etablissements medico-sociaux, associe les residents et les familles."
  "|La participation ne se limite pas aux actions politiques : elle inclut la vie quotidienne et les choix personnels."
  "|Une personne en situation de dependance reste un citoyen : la perte d'autonomie n'efface pas la citoyennete."
  "|Le droit de vote est universel et secret pour les citoyens majeurs."
  "|Les personnes sous tutelle ou curatelle conservent leur droit de vote."
  "|L'associatif permet de defendre des interets communs et de developper la solidarite."
  "|Les collectivites territoriales organisent des services de proximite : action sociale, sport, culture."
  "|Un accompagnant favorise la participation en informant, en accompagnant aux elections et en respectant les opinions."),
[QC("Qu'est-ce que la citoyenneté ?", "Un titre de séjour~Un statut de membre d'une communauté politique~Une assurance~Une profession", 1,
     "La citoyennete lie des droits et des devoirs a l'appartenance a une communaute politique."),
 QC("Quel est un devoir du citoyen ?", "Voter obligatoirement~Respecter les lois~Payer une amende~Refuser le débat", 1,
     "Le respect des lois et des autres est un devoir civique."),
 QC("Quel est le rôle d'un conseil de la vie sociale ?", "Gérer le budget de l'État~Associer les résidents et les familles à la vie de l'établissement~Remplacer le médecin~Organiser les examens", 1,
     "Le CVS est une instance de participation des usagers en établissement médico-social."),
 QC("Une personne sous tutelle conserve-t-elle son droit de vote ?", "Non~Oui~Seulement avec l'accord du tuteur~Seulement si elle est majeure", 1,
     "La measure de protection ne prive pas du droit de vote."),
 QC("Quelle forme de participation est locale ?", "Une élection présidentielle~Une réunion de quartier~Un traité international~Une grève nationale", 1,
     "La participation locale s'exerce dans la vie de quartier et les services de proximité."),
 QC("Quel rôle de l'accompagnant favorise la citoyenneté ?", "Décider du vote de la personne~Informer et accompagner sans orienter~Interdire les débats~Remplacer la personne", 1,
     "Il informe et accompagne, sans influencer le choix politique."),
 QC("La dépendance supprime-t-elle la citoyenneté ?", "Oui~Non, elle reste entière~Seulement en EHPAD~Seulement après 80 ans", 1,
     "La perte d'autonomie ne fait pas perdre la qualite de citoyen.")],
[QT("Expliquer pourquoi la participation sociale est un enjeu pour une personne âgée en établissement.",
     "L'entree en etablissement peut entrainer une perte de repères, de roles sociaux et de relations. La participation sociale permet de conserver une identite au-dela de la dependance : choisir ses activites, donner son avis sur les menus ou les horaires, rencontrer d'autres personnes, continuer a voter. Elle contribue a la sante mentale et a l'estime de soi. Le conseil de la vie sociale offre un cadre institutionnel pour que la parole des residents soit entendue et transformee en decisions. Pour l'accompagnant, favoriser cette participation signifie informer les personnes de leurs droits, organiser des temps d'echange et transmettre les demandes a la direction plutot que de decider a leur place.",
     "On attend le lien entre participation, identite, sante mentale et dispositifs comme le CVS."),
 QT("Comment organiser l'accompagnement au vote d'un résident en établissement, sans influencer son choix ?",
     "On informe d'abord la personne des modalités : date, lieu, horaires et accessibilite du bureau de vote. On demande si elle souhaite être accompagnee et par qui, en respectant son choix et sa dignite. On organise le transport avec l'aide adaptee, en veillant a la confidentialite du vote : l'accompagnant ne regarde pas le bulletin et n'entre pas dans l'isoloir avec la personne, sauf avenir une aide strictement necessaire et autorisee. On ne commente pas les candidats et on n'exprime pas d'opinion personnelle. On respecte le secret du vote, y compris apres le retour. Enfin, on note l'action dans les transmissions comme un accompagnement a la citoyennete, sans mentionner le choix exprime.",
     "On attend information, respect du secret, neutralite et traçabilité sans révéler le vote.")],
C("La citoyenneté accompagne la personne partout, y compris en situation de dépendance : l'enjeu est de rendre la participation possible.",
  "citoyenneté = droits + devoirs + appartenance",
  "CVS · droit de vote secret · participation locale · neutralité de l'accompagnant",
  "Citoyenneté~Droits et devoirs~Vote~Droit universel et secret~Participation~Implication dans la cité~Conseil de la vie sociale~Parole des usagers~Solidarité~Action associative",
  "Informer des droits~Proposer des modalités d'implication~Accompagner sans orienter~Respecter le secret~Transmettre les demandes",
  "Décider à la place de la personne|Confondre tutelle et perte du vote|Influencer un choix politique|Réduire la participation au seul vote",
  "CVS~Instance de participation~Vote~Secret garanti~Tutelle~Protection sans perte de citoyenneté~Quartier~Service de proximité~Association~Solidarité",
  "Droits~Vote et libertés~Devoirs~Respect des lois",
  "Participation politique~Élections et débats~Participation sociale~Vie quotidienne et associatif"))

# ============================================================ ME1
add("ME1", "Lire et analyser un sujet : méthode et reformulation", "Méthodologie", ["2nde pro"],
S("Lire un sujet, c'est d'abord identifier la commande : ce que l'on attend exactement comme production."
  "|Les verbes d'instruction orientent le travail : « analyser », « expliquer », « comparer » ou « proposer »."
  "|« Analyser » demande de decomposer ; « comparer » demande de relever ressemblances et differences."
  "|Le theme designe le domaine, le probleme designe la question a traiter."
  "|Les consignes de forme — longueur, plan impose, documents autorises — font partie du sujet."
  "|Une reformulation personnelle permet de verifier la comprehension avant de commencer."
  "|Le plan doit repondre a la problematique, et non suivre le hasard des idees."
  "|Une introduction presente le contexte, la problematique et annonce le plan."
  "|Chaque partie developpe une idee principale appuyee sur des exemples ou des arguments."
  "|La transition assure le lien entre deux parties sans les melanger."
  "|La conclusion repond a la problematique et ouvre eventuellement une perspective."
  "|En ASSP, cette methode sert aussi a analyser une situation professionnelle ou un protocole."),
[QC("Quel verbe demande de décomposer un sujet ?", "Comparer~Analyser~Proposer~Rédiger", 1,
     "Analyser consiste a separer les elements d'un ensemble pour les etudier."),
 QC("Que désigne la problématique ?", "Le titre du devoir~La question centrale à traiter~La conclusion~La bibliographie", 1,
     "La problematique est la question a laquelle le devoir doit repondre."),
 QC("Quel élément fait partie des consignes de forme ?", "Le thème~La longueur demandée~L'opinion de l'auteur~L'exemple choisi", 1,
     "Longueur, plan et documents autorises sont des consignes de forme."),
 QC("À quoi sert la reformulation ?", "À recopier l'énoncé~À vérifier sa compréhension avant de travailler~À remplacer le plan~À conclure", 1,
     "Reformuler avec ses mots permet de detecter les malentendus."),
 QC("Que contient une introduction ?", "Uniquement la conclusion~Le contexte, la problématique et l'annonce du plan~Les exemples~Les références", 1,
     "L'introduction remplit ces trois fonctions."),
 QC("Quel rôle joue une transition ?", "Elle ajoute une nouvelle question~Elle relie deux parties sans les mélanger~Elle remplace la conclusion~Elle supprime un exemple", 1,
     "La transition assure le passage d'une partie a la suivante."),
 QC("Que doit faire la conclusion ?", "Poser une nouvelle problématique~Répondre à la problématique~Présenter le plan~Ignorer les parties précédentes", 1,
     "La conclusion apporte une reponse claire et peut ouvrir une perspective.")],
[QT("Appliquer la méthode de lecture à un sujet : « En quoi l'accompagnement de la personne suppose-t-il une posture professionnelle adaptée ? »",
     "Commande : expliquer (« en quoi »), production attendue de type analyse. Theme : l'accompagnement de la personne. Problematique : le lien entre accompagnement et posture professionnelle. Mots-clés : accompagnement, posture professionnelle, adaptee. Reformulation : « Comment le professionnel doit-il se comporter pour accompagner une personne dans le respect de sa dignite et de ses droits ? » Les consignes de forme ne sont pas precisees dans cet extrait ; on supposera un developpement organise. Le plan possible : 1) la posture professionnelle repose sur des principes ethiques et deontologiques ; 2) elle s'adapte a la situation et a la personne ; 3) elle s'inscrit dans le travail d'equipe et la remise en question. Chaque partie sera illustree par une situation de stage ou un exemple de transmission.",
     "On attend identification de la commande, du theme, de la problematique, reformulation et plan."),
 QT("Expliquer pourquoi une reformulation personnelle est utile avant de rédiger une réponse à une situation professionnelle.",
     "La reformulation oblige a traduire l'énoncé avec ses propres mots, ce qui revele les parties mal comprises ou les termes ambigus. Dans une situation professionnelle, un detail change souvent la reponse : l'age de la personne, le lieu de l'intervention, l'existence d'un trouble ou le role de l'infirmier. Sans reformulation, on risque de repondre a une question voisine mais differente, par exemple de proposer une toilette complete alors que le sujet porte sur le refus de soin. La reformulation permet aussi de verifier que l'on a identifie l'objectif de la production : analyser une situation, proposer une action ou transmettre une information. On peut la faire a l'oral avec un camarade ou par ecrit en une ou deux phrases, puis la confronter a l'énoncé original avant de construire le plan.",
     "On attend la detection des ambiguites, l'exemple professionnel et la verification de la commande.")],
C("Analyser un sujet, c'est identifier la commande et la question centrale avant de construire un plan qui y répond.",
  "commande = verbe d'instruction · problématique = question centrale",
  "analyser = décomposer · comparer = ressemblances et différences · proposer = suggérer",
  "Verbe d'instruction~Ce qu'il faut faire~Thème~Domaine du sujet~Problématique~Question centrale~Consignes~Forme et longueur~Reformulation~Compréhension vérifiée",
  "Lire l'énoncé deux fois~Surligner les mots-clés~Repérer le verbe de commande~Formuler la problématique~Reformuler et bâtir le plan",
  "Répondre avant d'avoir compris|Confondre thème et problématique|Ignorer les consignes de forme|Recopier l'énoncé en introduction",
  "En quoi~Commande d'analyse~Analyser~Décomposer~Comparer~Ressemblances et différences~Introduction~Contexte et plan~Conclusion~Réponse",
  "Thème~Domaine général~Problématique~Question précise",
  "Introduction~Annonce du plan~Conclusion~Réponse à la question"))

# ============================================================ ME2
add("ME2", "Organiser une recherche documentaire et citer ses sources", "Méthodologie", ["Terminale pro"],
S("Une recherche documentaire commence par une question precise et des mots-cles pertinents."
  "|On distingue les sources primaires, comme un texte officiel ou un témoignage, des sources secondaires, comme un manuel."
  "|Les sources officielles — legislation, programmes, recommandations — ont une valeur de reference superieure."
  "|Un moteur de recherche donne des resultats hierarchises : il faut verifier la date, l'auteur et le site."
  "|Les sites institutionnels comme le Bulletin officiel, eduscol, Legifrance ou l'OMS sont prioritaires."
  "|La qualite d'une source s'evalue selon l'autorite de l'auteur, la date et la presence de references."
  "|Un resume personnel evite le copier-coller et assure que l'information a ete comprise."
  "|Les notes de lecture distinguent les informations, les idees personnelles et les questions restees ouvertes."
  "|Une citation reproduce exactement un passage court, entre guillemets, avec la source precise."
  "|Une reference bibliographique indique l'auteur, le titre, l'editeur, l'annee et parfois l'URL."
  "|Le plagiat consiste a presenter comme sien le travail ou les mots d'autrui : il est sanctionne."
  "|Dans un dossier de stage ASSP, citer ses sources renforce la credibilite et respecte la propriete intellectuelle."),
[QC("Quelle source est considérée comme officielle ?", "Un blog personnel~Un arrêté publié au Bulletin officiel~Un forum~Une photo sans légende", 1,
     "Un texte publie au BO ou sur Legifrance fait autorite."),
 QC("Qu'est-ce qu'une source primaire ?", "Un manuel scolaire~Un texte original ou un témoignage direct~Un résumé~Une encyclopédie", 1,
     "La source primaire est le document d'origine, non un commentaire."),
 QC("Quel critère ne permet pas d'évaluer une source ?", "La date de publication~L'autorité de l'auteur~La couleur du site~La présence de références", 2,
     "L'apparence graphique n'est pas un critere de fiabilite."),
 QC("Que doit contenir une référence bibliographique ?", "Seulement le titre~Auteur, titre, éditeur et année~Seulement l'URL~Le prix du livre", 1,
     "Ces elements permettent de retrouver et verifier la source."),
 QC("Comment éviter le plagiat ?", "En changeant quelques mots~En citant la source et en reformulant~En supprimant les guillemets~En copiant un site connu", 1,
     "La reformulation personnelle et la citation explicite evitent le plagiat."),
 QC("À quoi sert une note de lecture ?", "À recopier le document~À distinguer informations, idées et questions~À remplacer la source~À éviter de lire", 1,
     "Elle organise la comprehension et garde une trace du travail."),
 QC("Quel site est prioritaire pour un texte réglementaire français ?", "Un réseau social~Legifrance~Un blog~Une vidéo", 1,
     "Legifrance publie les textes de loi et reglements.")],
[QT("Construire une référence bibliographique correcte pour un texte officiel et expliquer chaque élément.",
     "Ministère de l'Éducation nationale, Référentiel du baccalauréat professionnel « Accompagnement, soins et services à la personne », arrêté du 2 février 2022, NOR MENE2134461A, annexes du référentiel, 2022. L'auteur est le ministere, ce qui etablit l'autorite du document. Le titre precis identifie la specialite visee. La nature du texte — arrete et referentiel — indique sa valeur juridique. Le NOR et la date permettent de le retrouver exactement sur Legifrance ou eduscol, et de verifier qu'il n'a pas ete modifie. L'annee situe le document dans le temps, ce qui est indispensable pour un programme susceptible d'evoluer.",
     "On attend auteur, titre, nature du texte, identifiant, date et explication de l'utilite de chaque champ."),
 QT("Expliquer la démarche à suivre pour vérifier la fiabilité d'un site trouvé lors d'une recherche sur la bientraitance.",
     "On identifie d'abord l'éditeur du site : ministere, agence sanitaire, association reconnue ou particulier. On regarde la date de mise a jour, car les recommandations evoluent. On verifie si les affirmations sont appuyees par des textes ou des études accessibles, et si les liens fonctionnent. On compare l'information avec une source officielle, par exemple un texte du ministere ou de la Haute Autorite de sante. On se méfie des sites qui vendent un produit ou qui presentent des témoignages sans cadre. On note enfin les elements de reference — auteur, titre, date, URL — des maintenant, pour pouvoir citer la source dans le dossier. Si le doute persiste, on écarte la source plutot que de l'utiliser.",
     "On attend : identité de l'éditeur, date, preuves à l'appui, recoupement et collecte des références.")],
C("Une recherche fiable part de mots-clés précis, privilégie les sources officielles et cite toujours ce qui est emprunté.",
  "source primaire = document d'origine · source secondaire = commentaire",
  "référence = auteur + titre + éditeur + année + URL si utile",
  "Mots-clés~Termes de recherche~Source primaire~Document original~Source officielle~Legifrance et BO~Référence~Auteur et date~Plagiat~Appropriation indue",
  "Formuler la question~Choisir les mots-clés~Sélectionner des sources fiables~Reformuler les notes~Citer et référencer",
  "Copier-coller un texte|Croire le premier résultat venu|Oublier la date de la source|Citer sans donner l'URL pour un site",
  "Legifrance~Texte de loi~Éduscol~Ressource pédagogique~OMS~Source internationale~Arrêté 2022~Référentiel ASSP~NOR~Identifiant unique",
  "Source primaire~Témoignage ou texte d'origine~Source secondaire~Analyse ou manuel",
  "Citation~Passage exact entre guillemets~Référence~Identification complète"))

# FIN DES LOTS
valider_et_ecrire(F, "pro-sante-mat-part-A.json")
