# -*- coding: utf-8 -*-
"""Générateur btsesf-mat-part-A.json — lot A de la filière bts-esf.

20 fiches 'prototype' (BTS1 / BTS2) : Culture générale et expression (7),
Communication (6), Management (7).
Chaque fiche : 12 points de cours, 9 questions corrigées (7 QCM + 2 texte),
7 blocs en ordre strict, 3 schémas SVG. Rien n'est injecté dans l'application.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _btsesf_common import ANNEES, QC, QT, C, S, build, valider_et_ecrire

F = []


def add(prefix, titre, mat, ans, points, questions, c, ref=""):
    F.append(build(prefix, titre, mat, ans, points, questions, c, ref))


U1 = "Unité U1 (culture générale et expression), référentiel BTS ESF 2022"
UG = "Programmes d'enseignement général applicables en BTS, référentiel BTS ESF 2022"
UP = "Programmes d'enseignement professionnel, référentiel BTS ESF 2022"

# ============================================================ CG1
add("CG1.", "L'argumentation : construire et évaluer un raisonnement", "Culture générale et expression", ["BTS1"],
S("Argumenter, c'est présenter une thèse, des raisons qui la soutiennent et des exemples qui les rendent crédibles, dans le but de convaincre un lecteur ou un auditoire."
  "|Une thèse est une affirmation générale que l'on s'engage à défendre ; elle doit être claire, nuancée et formulée dès l'introduction."
  "|Une argumentation complète distingue la thèse, l'antithèse (les objections possibles) et la synthèse (le dépassement proposé)."
  "|Un argument est une raison générale : il relève d'un fait, d'une valeur, d'une loi ou d'une expérience et sert de prémisse au raisonnement."
  "|Un exemple est un cas particulier qui illustre l'argument ; il ne le remplace pas et doit rester pertinent et vérifiable."
  "|Le raisonnement déductif part de prémisses générales pour aboutir à une conclusion nécessaire ; sa validité dépend de la forme, pas du contenu."
  "|Le raisonnement inductif généralise à partir de cas observés : sa conclusion est probable, jamais certaine, et dépend du nombre et de la représentativité des cas."
  "|L'analogie transfère une relation connue vers un domaine comparable : elle éclaire mais ne démontre pas, car les situations diffèrent toujours par quelque point."
  "|Les connecteurs logiques (donc, car, en effet, mais, bien que, en revanche) rendent visible la structure du raisonnement et évitent les ruptures."
  "|Un sophisme est un raisonnement invalide qui paraît convaincant : attaque de la personne, fausse cause, généralisation hâtive, homme de paille."
  "|Évaluer un argument, c'est vérifier sa pertinence, sa vérité, sa acceptabilité et sa force, puis repérer les présupposés non dits."
  "|Dans les épreuves de culture générale du BTS ESF, l'argumentation est exigée dans l'essai, la synthèse et l'expression orale, avec une position personnelle assumée."),
[QC("Quel rôle joue l'exemple dans une argumentation ?", "Il remplace l'argument~Il illustre et concrétise l'argument~Il invalide toujours la thèse~Il sert uniquement à allonger le texte", 1,
    "L'exemple est un cas particulier au service d'une raison générale : il ne tient pas lieu d'argument."),
 QC("Quel raisonnement aboutit à une conclusion seulement probable ?", "La déduction~L'induction~La définition~La contradiction", 1,
    "L'induction généralise à partir d'observations : sa conclusion reste probable et dépend de la représentativité des cas."),
 QC("Qu'est-ce qu'une antithèse ?", "La conclusion finale~Une objection à la thèse~Un exemple chiffré~Une figure de style ornementale", 1,
    "L'antithèse présente les arguments contraires ou les limites de la position défendue."),
 QC("Quel connecteur introduit une conséquence ?", "Bien que~Donc~Or~En revanche", 1,
    "« Donc » marque la conclusion ou la conséquence ; « car » introduit la cause."),
 QC("Quel est un sophisme ?", "Une analogue explicitement nuancée~Une attaque de la personne au lieu de l'idée~Une citation sourcée~Une objection réfutée", 1,
    "L'attaque de la personne (argumentum ad hominem) détourne le débat de l'argument lui-même."),
 QC("Sur quoi porte la validité d'un raisonnement déductif ?", "Sur la longueur du texte~Sur la forme logique et les prémisses~Sur le nombre d'exemples~Sur l'émotion du lecteur", 1,
    "En déduction, la conclusion suit nécessairement des prémisses si la forme est valide et les prémisses vraies."),
 QC("Que doit être une thèse en introduction d'essai ?", "Une question ouverte~Une affirmation claire et nuancée~Une simple citation~Un chiffre isolé", 1,
    "La thèse énonce clairement la position défendue, que le plan permettra de nuancer."),
 QT("Construire un paragraphe argumenté sur la proposition : « La prévention vaut mieux que la réparation. » Vous dégagerez une thèse, deux arguments et une objection.",
    "Thèse : dans l'action sociale comme dans la santé, prévenir un risque coûte moins cher et respecte davantage les personnes que d'intervenir après la crise ; mais la prévention ne peut tout éviter. Premier argument : la prévention agit en amont, avant l'aggravation : un accompagnement budgétaire précoce évite le surendettement et ses conséquences (expulsion, rupture de droits), comme une campagne de vaccination évite une épidémie. Deuxième argument : elle est plus respectueuse de l'autonomie, car elle informe et outille la personne au lieu de la prendre en charge après l'échec. Objection : la prévention exige des moyens durables et ses effets sont différés, donc moins visibles qu'une intervention d'urgence ; on lui reproche aussi de responsabiliser excessivement l'individu face à des causes structurelles. Synthèse partielle : la prévention doit donc être combinée à un dispositif de réparation accessible, les deux étant complémentaires plutôt que concurrents.",
    "On attend une thèse explicite, deux arguments généraux distincts illustrés, une objection réellement contraire et une nuance finale, avec des connecteurs logiques."),
 QT("Repérer et corriger le sophisme : « Ce collègue critique notre dispositif d'accueil ; il n'a même pas de formation en travail social, donc sa critique est sans valeur. »",
    "Le raisonnement commet une attaque de la personne (ad hominem) : au lieu d'examiner le contenu de la critique, il disqualifie son auteur en raison de son absence de formation. Or la valeur d'un argument ne dépend pas du statut de celui qui l'énonce : un usager ou un collègue peut observer un problème réel d'accueil. Pour corriger, on reformule : « Sa critique porte sur l'attente à l'accueil et sur l'absence d'information écrite ; ces deux points méritent d'être vérifiés, indépendamment de sa formation. » On peut ensuite discuter la pertinence de chaque observation, demander des précisions et confronter les données, tout en reconnaissant que la compétence professionnelle reste utile pour juger de la faisabilité des solutions. La correction consiste à déplacer le débat de la personne vers les arguments.",
    "La réponse doit nommer l'ad hominem, expliquer pourquoi il est invalide et proposer une reformulation centrée sur le fond.")],
C("Une argumentation solide enchaîne thèse, arguments généraux, exemples et objections, puis propose une synthèse nuancée.",
  "Thèse + arguments + exemples + objection + synthèse",
  "Un argument est une raison générale ; un exemple est un cas particulier ; un sophisme est un raisonnement invalide mais séduisant.",
  "Thèse~Affirmation défendue~Position initiale|Antithèse~Objections possibles~Limites du propos|Synthèse~Dépassement nuancé~Conclusion",
  "Définir la question et prendre position|Choisir deux ou trois arguments généraux|Illustrer chaque argument par un exemple précis|Formuler une objection et y répondre|Conclure par une synthèse personnelle",
  "Confondre argument et exemple|Généraliser à partir d'un seul cas|Ignorer l'objection contraire|Enchaîner les idées sans connecteurs logiques",
  "Prévention~Agir en amont du risque~Ad hominem~Attaque de la personne~Induction~Conclusion probable~Déduction~Conclusion nécessaire",
  "Déduction~Des prémisses à la conclusion~Certitude si la forme est valide|Induction~Des cas à la règle~Conclusion probable",
  "Argument~Raison générale~Valable pour tous les cas|Exemple~Cas particulier~Sert à illustrer"),
U1)

# ============================================================ CG2
add("CG2.", "L'essai et la dissertation : problématique et plans", "Culture générale et expression", ["BTS1"],
S("L'essai est un exercice de réflexion personnelle sur un sujet d'ordre général : il exige une culture, une positions argumentée et une structure lisible."
  "|La dissertation, plus contraignante, répond à un sujet précis selon un plan annoncé et traite la question sous plusieurs angles."
  "|Analyser le sujet consiste à définir les termes, à repérer les mots-clés et à identifier la portée exacte de la question posée."
  "|La problématique est la question centrale que l'essai cherche à résoudre : elle transforme un thème en problème et évite le catalogue d'idées."
  "|Le plan dialectique (thèse, antithèse, synthèse) convient aux sujets opposant deux positions ou invitant à prendre parti."
  "|Le plan thématique traite un sujet en aspects distincts, par exemple individuel, institutionnel et sociétal, sans proposer de confrontation frontale."
  "|Le plan analytique examine d'abord les causes d'un phénomène, puis ses effets, puis les remèdes possibles."
  "|Chaque partie doit être annoncée, enchaînée et subdivisée : on évite les parties déséquilibrées et les listes d'idées sans explication."
  "|L'introduction appelle le sujet, le définit, pose la problématique et annonce le plan ; la conclusion répond à la problématique et ouvre éventuellement la réflexion."
  "|Les transitions relient les parties en montrant le lien logique : opposition, conséquence, approfondissement."
  "|Une culture générale maîtrisée s'appuie sur des références précises (auteurs, dates, concepts, exemples historiques ou contemporains) et non sur des clichés."
  "|À l'écrit du BTS ESF, la qualité de la problématisation et la cohérence du plan sont déterminantes dans l'évaluation de l'épreuve U1."),
[QC("Quel est le rôle de la problématique ?", "Résumer le plan en une phrase~Transformer le thème en question centrale~Donner la conclusion à l'avance~Citer un auteur", 1,
    "La problématique fait du thème un problème à résoudre et guide toute la réflexion."),
 QC("Quel plan oppose deux positions avant de les dépasser ?", "Le plan thématique~Le plan dialectique~Le plan chronologique~Le plan analytique", 1,
    "Le plan dialectique suit thèse, antithèse et synthèse."),
 QC("Dans une introduction, que place-t-on avant l'annonce du plan ?", "La conclusion~La problématique~Une ouverture~Les références bibliographiques", 1,
    "On accroche, définit les termes, pose la problématique, puis annonce le plan."),
 QC("Quel plan convient à l'étude des causes, effets et remèdes d'un phénomène ?", "Le plan dialectique~Le plan analytique~Le plan par auteurs~Le plan alphabétique", 1,
    "Le plan analytique suit le déroulement logique causes, conséquences, solutions."),
 QC("Qu'est-ce qu'une transition réussie ?", "Un simple retour à la ligne~Un lien logique entre deux parties~Une nouvelle citation sans rapport~Une répétition de l'introduction", 1,
    "La transition montre le rapport logique (opposition, conséquence, approfondissement) entre deux parties."),
 QC("Quel défaut affaiblit un essai ?", "Une problématique claire~Une accumulation d'idées sans fil conducteur~Des exemples analysés~Des parties équilibrées", 1,
    "Sans problématique, les idées s'accumulent sans construire une réponse."),
 QC("À quoi sert de définir les termes du sujet ?", "À gagner du temps~À fixer le sens et le périmètre de la question~À éviter les exemples~À remplacer la conclusion", 1,
    "La définition des termes délimite ce dont on parle et évite le hors-sujet."),
 QT("À partir du sujet « Faut-il toujours écouter la majorité ? », dégagez une problématique et proposez un plan dialectique en annonçant le contenu de chaque partie.",
    "Problématique : la majorité exprime une préférence collective et donne une décision acceptable par le nombre, mais le nombre ne garantit ni la vérité ni le respect des minorités ; comment articuler la règle majoritaire et la protection des droits de chacun ? Première partie (thèse) : la majorité est une règle opérationnelle et démocratique ; elle évite l'immobilisme, donne une décision identifiable et s'impose dans les associations, les conseils d'administration et les collectivités. Deuxième partie (antithèse) : la majorité peut être ignorante, influencée ou oppressive ; l'histoire montre que des majorités ont soutenu des injustices, et la démocratie constitutionnelle soumet précisément la majorité au respect des droits fondamentaux. Troisième partie (synthèse) : la règle majoritaire reste légitime à condition d'être encadrée : droits opposables, délibération de qualité, information des membres, possibilité de réexamen. On aboutit à une majorité éclairée et limitée, pas à une majorité absolue.",
    "On vérifie que la problématique est une question, que les trois parties s'opposent puis se dépassent, et que chaque partie est annoncée brièvement."),
 QT("Expliquer la différence entre un plan thématique et un plan analytique, et indiquer pour quels sujets les choisir.",
    "Le plan thématique découpe la réalité en aspects ou en niveaux : par exemple, dans un sujet sur l'accès aux droits, on traitera successivement l'accès à l'information, l'accès aux dispositifs et l'accès effectif aux prestations. Il convient aux sujets qui demandent de décrire, de comparer des dimensions ou d'explorer un phénomène sous plusieurs faces. Le plan analytique suit une logique de résolution : les causes du problème, ses effets, puis les solutions envisageables. Il convient aux sujets posés en termes de crise, de difficulté ou de remède, par exemple les effets du surendettement et les leviers d'accompagnement. Le plan dialectique, lui, sera préféré dès que le sujet demande de prendre parti entre deux thèses. Le choix dépend donc moins de la mode que de la forme exacte de la question et de la réponse que l'on veut construire.",
    "La réponse doit définir les deux plans, donner un exemple d'application pour chacun et justifier le choix par la nature du sujet.")],
C("Un bon essai naît d'une question précise : définir les termes, problématiser, choisir un plan adapté puis répondre à la question posée.",
  "Introduction = accroche + définition + problématique + annonce du plan",
  "Plan dialectique : thèse / antithèse / synthèse · plan analytique : causes / effets / remèdes · plan thématique : aspects",
  "Problématique~Question centrale~Évite le catalogue|Dialectique~Thèse antithèse synthèse~Prendre parti|Transitions~Liens logiques~Fluidité du texte",
  "Lire et définir les termes du sujet|Formuler la problématique|Choisir le plan adapté|Rédiger des parties équilibrées|Conclure en répondant à la problématique",
  "Répondre à une question qui n'a pas été posée|Annincer un plan non respecté|Confondre exemple et argument|Négliger la définition des termes",
  "Sujet majorité~Règle collective et droits~Plan dialectique~Trois temps~Problématique~Une question~Transition~Un lien logique",
  "Plan dialectique~Affronter deux thèses~Synthèse finale|Plan analytique~Causes, effets, remèdes~Logique de résolution",
  "Introduction~Ouvre le sujet~Conclusion~Répond au sujet"),
U1)

# ============================================================ CG3
add("CG3.", "La synthèse de documents : méthode et contraintes", "Culture générale et expression", ["BTS1"],
S("La synthèse de documents consiste à restituer l'essentiel de plusieurs textes ou documents sur un même thème, en un texte personnel, objectif et structuré."
  "|Elle exige de respecter une commande précise : longueur imposée, nombre de documents, présence ou non d'un titre, d'un sous-titre et d'une introduction."
  "|La première étape est la lecture active : on identifie la nature, l'auteur, la date et la visée de chaque document."
  "|On dégage ensuite les idées principales de chaque document, puis les points communs et les divergences entre eux."
  "|Le plan de synthèse suit le plus souvent les axes de la problématique commune, et non l'ordre des documents."
  "|La reformulation est obligatoire : recopier des phrases entières constitue un plagiat, même avec une référence."
  "|Les emprunts nécessaires doivent être mis entre guillemets et accompagnés de la référence du document et de sa page ou de son paragraphe."
  "|Les chiffres, dates et exemples sont conservés s'ils sont utiles à la démonstration et vérifiables dans les documents."
  "|Le ton reste neutre : le rédacteur ne donne pas son avis personnel dans une synthèse, sauf si la consigne le demande explicitement."
  "|Un équilibre doit être respecté entre les documents : aucun texte ne doit être présenté de manière disproportionnée par rapport aux autres."
  "|L'introduction présente le thème, le contexte et les documents sans développer le plan ; elle ne remplace pas le traitement du sujet."
  "|En BTS ESF, cet exercice évalue la capacité à traiter l'information professionnelle et à produire un écrit synthétique pour un dossier de projet."),
[QC("Comment citer un emprunt exact dans une synthèse ?", "Sans marque particulière~Entre guillemets avec la référence du document~En italique sans source~En changeant simplement un mot", 1,
    "Tout emprunt littéral doit être signalé par des guillemets et la source précisée."),
 QC("Quel plan est attendu dans une synthèse ?", "L'ordre de parution des documents~Les axes communs dégagés après lecture~Le plan de l'auteur le plus long~Un plan chronologique imposé", 1,
    "On construit un plan à partir des idées et des axes partagés, pas de l'ordre des documents."),
 QC("Quel défaut constitue un plagiat ?", "Reformuler une idée en citant sa source~Recopier une phrase sans la signaler~Résumer avec ses propres mots~Sélectionner les idées principales", 1,
    "Recopier sans guillemets ni référence est un plagiat, même pour une seule phrase."),
 QC("Quelle posture adopter dans une synthèse ?", "Polémique et personnelle~Neutre et objective~Ironique~Purement narrative", 1,
    "La synthèse restitue les positions des documents sans y ajouter l'opinion du rédacteur."),
 QC("Que faire des divergences entre documents ?", "Les masquer~Les présenter en les attribuant clairement~Les remplacer par son avis~Les supprimer du plan", 1,
    "Les désaccords font partie de l'information : on les expose en citant les sources."),
 QC("Que contient l'introduction d'une synthèse ?", "La conclusion du rédacteur~Le thème, le contexte et la présentation des documents~Tout le plan détaillé~La liste des références", 1,
    "L'introduction situe le sujet et les documents ; le développement traite les axes."),
 QC("Pourquoi vérifier la nature et la date des documents ?", "Pour choisir la police de caractères~Pour apprécier leur portée et leur contexte~Pour allonger la copie~Pour éviter les guillemets", 1,
    "Un texte de 1990 et un rapport de 2025 n'ont pas la même portée : la date et la nature éclairent le propos."),
 QT("Vous devez synthétiser trois documents sur la précarité étudiante : une enquête statistique (2024), un témoignage d'étudiante (2025) et un communiqué d'une association d'aide (2025). Proposez la démarche complète, du traitement des documents au plan final.",
    "Je relève d'abord la nature et la visée de chaque document : l'enquête donne des grandeurs et des tendances, le témoignage une expérience individuelle, le communiqué une position militante et des propositions. Je lis en confrontant, en relevant pour chaque document les idées principales et les chiffres utiles. Je dégage ensuite les recoupements (par exemple l'augmentation des dépenses de logement et le recours à l'aide alimentaire) et les divergences (l'accent mis sur les causes structurelles ou sur les difficultés personnelles). J'écarte les détails anecdotiques et je vérifie que chaque document est équitablement représenté. Le plan peut suivre trois axes : (1) l'ampleur et les manifestations de la précarité, (2) les effets sur la vie étudiante et les parcours, (3) les réponses existantes et leurs limites. Je rédige en reformulant, en gardant deux ou trois chiffres sourcés et en citant entre guillemets les formules frappantes, avec la référence du document. Je termine par une conclusion neutre qui reprend l'équilibre entre données, vécu et propositions.",
    "On attend les étapes de lecture, de confrontation, de plan, de reformulation avec citations sourcées, et le respect de la neutralité."),
 QT("Un document affirme : « 30 % des étudiants renoncent à se soigner pour des raisons financières. » Comment intégrer correctement cette information dans une synthèse ?",
    "Je vérifie d'abord la source, la date et le périmètre de l'enquête : pays, échantillon, définition de « renoncer à se soigner », marge d'erreur éventuelle. Si le chiffre est employé, je l'intègre comme une donnée attribuée : « selon l'enquête X publiée en 2024, 30 % des étudiants interrogés déclarent renoncer à des soins pour des motifs financiers ». Je ne le transforme pas en vérité générale sur tous les étudiants et je ne le mêle pas à une autre source sans distinguer les périmètres. Si la formulation du document est frappante et que je souhaite la conserver, je la mets entre guillemets avec la référence. J'équilibre enfin ce chiffre avec les autres documents : un témoignage individuel et une prise de position associative apportent un éclairage différent, que je présente comme tel plutôt que de les fondre tous trois en une affirmation unique.",
    "La réponse doit montrer l'attribution de la donnée, la prudence sur le périmètre et l'équilibre entre les documents.")],
C("La synthèse restitue l'essentiel de plusieurs documents dans un texte personnel, neutre et structuré par des axes communs.",
  "Synthèse = idées communes + divergences + reformulation sourcée",
  "Reformuler sans recopier · citer entre guillemets · équilibrer les documents · rester neutre",
  "Lecture~Nature, auteur, date~Contexte|Comparaison~Points communs et divergences~Axes du plan|Réécriture~Reformulation et citations~Texte personnel",
  "Lire les documents et repérer leur visée|Extraire les idées principales de chacun|Degager les axes communs et les divergences|Construire un plan équilibré|Rédiger en reformulant et en citant",
  "Recopier des phrases sans guillemets|Suivre l'ordre des documents au lieu des idées|Donner son avis personnel|Sur-représenter un document",
  "Enquête 2024~Chiffres et tendances~Témoignage 2025~Expérience individuelle~Communiqué~Position associative~30 %~Donnée à attribuer",
  "Synthèse~Neutre et collective~Commentaire~Personnel et interprétatif|Reformulation~Mots changés, sens conservé~Plagiat~Copie non signalée",
  "Idée commune~Fil du plan~Divergence~Différence à exposer"),
U1)

# ============================================================ CG4
add("CG4.", "Commentaire de texte et lecture d'image", "Culture générale et expression", ["BTS1"],
S("Le commentaire de texte est une explication ordonnée d'un passage : il décrit les procédés employés et interprète leur effet de sens."
  "|La lecture d'image applique la même exigence à un support visuel : affiche, photographie, graphique, bande dessinée ou capture d'écran."
  "|On distingue trois niveaux de lecture : le sens littéral (ce qui est dit ou montré), le sens implicite (ce que cela suggère) et la visée (ce que l'auteur cherche à produire)."
  "|L'analyse des champs lexicaux révèle les orientations de sens : un champ lexical de la sécurité, de la peur ou de la confiance n'a pas la même fonction."
  "|Les figures de style (métaphore, comparaison, ironie, antithèse, hyperbole) produisent des effets : frapper, convaincre, émouvoir, distance."
  "|Les modalités (affirmation, interrogation, injonction, conditionnel) indiquent la posture de l'énonciateur vis-à-vis de son propos."
  "|Le rythme de la phrase, la ponctuation et la disposition typographique participent au sens : une phrase courte frappe, une énumération sature."
  "|Dans une image, on analyse le cadrage, le point de vue, la lumière, les couleurs, la composition et les rapports de taille entre les éléments."
  "|Un graphique se lit par son titre, ses axes, son échelle et ses unités : l'échelle peut amplifier ou minimiser une variation."
  "|La dénotation est le sens premier d'un mot ou d'un élément ; la connotation est le sens associé, culturel ou émotionnel, qu'il déclenche."
  "|Un bon commentaire cite ou décrit précisément avant d'interpréter : l'affirmation sans preuve textuelle n'est pas recevable."
  "|Ces compétences servent en BTS ESF à lire des documents d'information sanitaire, des campagnes de prévention et des supports de sensibilisation."),
[QC("Quel est le sens littéral d'un texte ?", "Ce que l'auteur suggère~Ce qui est effectivement dit ou montré~L'opinion du commentateur~La morale de l'histoire", 1,
    "Le sens littéral est le contenu explicite, avant interprétation."),
 QC("Quelle figure de style rapproche deux éléments à l'aide d'un outil de comparaison ?", "La métaphore~La comparaison~L'ironie~L'hyperbole", 1,
    "La comparaison utilise un outil (comme, tel, semblable à) ; la métaphore implique un transfert direct."),
 QC("Dans une image, que désigne le cadrage ?", "La couleur dominante~Le choix de ce qui est inclus ou exclu du champ~La taille du fichier~Le titre de l'affiche", 1,
    "Le cadrage sélectionne ce que le spectateur voit et oriente ainsi l'interprétation."),
 QC("Quel élément d'un graphique peut tromper sur l'ampleur d'une variation ?", "Le titre~L'échelle des axes~La légende~La couleur du papier", 1,
    "Une échelle tronquée ou disproportionnée amplifie visuellement les écarts."),
 QC("Qu'est-ce qu'une connotation ?", "Le sens premier du mot~Le sens associé, culturel ou émotionnel~La définition de dictionnaire~La prononciation", 1,
    "La connotation est le sens second déclenché par un mot ou une image dans un contexte culturel."),
 QC("Pourquoi citer le texte dans un commentaire ?", "Pour allonger la copie~Pour appuyer l'interprétation sur une preuve~Pour éviter de réfléchir~Pour remplacer le plan", 1,
    "Toute interprétation doit s'appuyer sur un élément précis du document."),
 QC("Quelle modalité correspond à un ordre ou à une consigne ?", "L'interrogation~L'injonction~Le conditionnel~La négation", 1,
    "L'injonction (impératif, devoir) marque une consigne adressée au lecteur."),
 QT("Commenter la phrase suivante, relevée dans une affiche de prévention : « Et si votre silence pesait plus que vous ne le pensez ? » Vous analyserez les procédés et la visée.",
    "La phrase est une interrogation : le « et si » ouvre une hypothèse et invite le lecteur à se sentir concerné sans être accusé directement. Le verbe « peser » est une métaphore : le silence est traité comme un poids, ce qui suggère une charge, une responsabilité et une conséquence mesurable pour autrui. Le complément « plus que vous ne le pensez » crée une understatement, une nuance qui ménage le lecteur tout en introducing une inquiétude : ce que l'on croit anodin ne l'est pas. Le champ lexical implicite de la charge et du poids entre en résonance avec le thème de la santé mentale ou de la violence : se taire, c'est parfois laisser le problème grandir. La deuxième personne du possessif « vous » crée une interpellation directe et personnalisée. La visée est double : éveiller une prise de conscience et orienter vers une action (parler, signaler, consulter). L'affiche évite la morale autoritaire au profit d'une question, plus respectueuse et plus susceptible de provoquer une adhésion.",
    "On attend l'identification de l'interrogation, de la métaphore du poids, de l'interpellation et une interprétation de la visée qui reste appuyée sur les mots de la phrase."),
 QT("Vous analysez une affiche de prévention du surendettement : au centre, une enveloppe serrée dans une main ; en arrière-plan, des chiffres flous ; en bas, un slogan « Reprendre la main avant la fin du mois ». Décrivez les éléments et interprétez la composition.",
    "Le premier niveau est la description : une main serre une enveloppe au centre, des chiffres flous occupent le fond, le slogan est placé en bas. Le cadrage est centré sur le geste de serrer, ce qui fait de la main le point de focalisation et suggère à la fois la maîtrise et la tension. Le point de vue rapproché place le spectateur du côté de la personne qui agit, pas du côté d'un observateur extérieur. Le flou des chiffres est significatif : les montants existent, mais ils ne sont pas lisibles, ce qui traduit la confusion et l'angoisse face aux échéances, tout en évitant de donner un chiffre précis qui pourrait exclure une partie du public. Le slogan joue sur le sens littéral de « reprendre la main » et sur son sens figuré de reprendre le contrôle ; « avant la fin du mois » ancre le message dans une urgence concretement vécue. La composition oppose donc un centre net et maîtrisé à un fond flou et menaçant : elle transforme une difficulté financière en un enjeu d'action et de dignité, avec une visée rassurante et mobilisatrice plutôt que culpabilisante.",
    "La réponse doit décrire avant d'interpréter, analyser cadrage et flou, expliquer le jeu de mots du slogan et dégager la visée.")],
C("Commenter, c'est décrire précisément, repérer les procédés, puis expliquer leur effet de sens et la visée du document.",
  "Niveaux de lecture : littéral → implicite → visée",
  "Dénotation / connotation · champs lexicaux · modalités · cadrage et échelle",
  "Sens littéral~Contenu explicite~Description|Sens implicite~Suggestions~Interprétation|Visée~Effet recherché~Intention",
  "Décrire le document sans interpréter|Repérer les procédés pertinents|Citez ou désigner les éléments précis|Interpréter leur effet de sens|Formuler la visée globale",
  "Interpréter sans preuve|Confondre dénotation et connotation|Ignorer le contexte de l'image|Parler de ses goûts personnels",
  "Interrogation~Hypothèse adressée~Métaphore~Transfert de sens~Cadrage~Sélection du visible~Échelle~Amplification visuelle",
  "Dénotation~Sens premier~Objectif|Connotation~Sens associé~Variable selon le contexte",
  "Description~Ce qui est vu~Interprétation~Ce que cela signifie"),
"Unité U1 (culture générale et expression), référentiel BTS ESF 2022")

# ============================================================ CG5
add("CG5.", "Grammaire et syntaxe au service de la clarté", "Culture générale et expression", ["BTS1"],
S("La maîtrise de la langue est une exigence d'évaluation de l'écrit en BTS : elle conditionne la crédibilité du propos."
  "|Une phrase est une unité de sens organisée autour d'un verbe conjugué : sa structure doit rester identifiable même lorsqu'elle est longue."
  "|Les constituants essentiels sont le sujet, le verbe, le complément d'objet et les compléments circonstanciels de temps, de lieu, de cause ou de manière."
  "|L'accord sujet-verbe est une règle fondamentale : le verbe s'accorde avec son sujet, y compris quand plusieurs mots séparent les deux."
  "|Le participe passé employé avec « avoir » s'accorde avec le complément d'objet direct seulement si celui-ci précède le verbe."
  "|Les pronoms relatifs (qui, que, dont, où) relient deux propositions : leur choix dépend de la fonction du mot remplacé dans la proposition relative."
  "|« Dont » remplace un complément introduit par la préposition « de » ; « où » remplace un complément de lieu ou de temps."
  "|La ponctuation organise la respiration et la hiérarchie des idées : la virgule sépare, le point-virgule associe, les deux-points introduisent une explication."
  "|Les mots de liaison doivent être choisis avec précision : « car » introduit une cause, « donc » une conséquence, « cependant » une opposition."
  "|L'ambiguïté d'un pronom ou d'un complément est une faute de clarté : on répète le nom plutôt que de risquer une mauvaise compréhension."
  "|La voix passive permet de mettre en avant l'action ou son objet plutôt que son auteur, utile dans un compte rendu professionnel."
  "|Une relecture méthodique porte successivement sur le sens, la structure des paragraphes, les accords, la ponctuation et l'orthographe."),
[QC("Quel verbe s'accorde avec le sujet dans « Les difficultés que nous avons rencontrées » ?", "Avons~Avons rencontré~Rencontrées~A rencontré", 1,
    "Le participe passé avec « avoir » s'accorde avec le COD placé avant : « les difficultés que nous avons rencontrées »."),
 QC("Quel pronom relatif remplace un complément introduit par « de » ?", "Qui~Que~Dont~Où", 2,
    "« Dont » reprend un complément d'objet indirect ou un complément du nom introduit par « de »."),
 QC("Quelle ponctuation introduit une explication ou une énumération ?", "Le point-virgule~Les deux-points~La virgule~Le point d'exclamation", 1,
    "Les deux-points annoncent une explication, une citation ou une énumération."),
 QC("Quel mot de liaison marque l'opposition ?", "Car~Donc~Cependant~Ainsi", 2,
    "« Cependant » marque l'opposition ; « car » la cause, « donc » et « ainsi » la conséquence."),
 QC("Dans une phrase, que désigne le complément circonstanciel ?", "L'action~Le sujet~Une circonstance comme le temps ou le lieu~L'adjectif", 2,
    "Le complément circonstanciel situe l'action dans le temps, l'espace ou précise sa cause ou sa manière."),
 QC("Quel est l'avantage de la voix passive dans un compte rendu ?", "Elle rend le texte plus long~Elle met en avant l'action ou son objet~Elle supprime les verbes~Elle évite la ponctuation", 1,
    "Le passif permet de présenter le fait traité comme le thème de la phrase, utile dans un écrit professionnel."),
 QC("Que vérifier en premier lors d'une relecture ?", "L'orthographe avant tout~La cohérence du sens et des paragraphes~La couleur du papier~Le nombre de pages", 1,
    "On relit d'abord le fond et la structure, puis la forme (accords, ponctuation, orthographe)."),
 QT("Corrigez les accords et précisez la règle appliquée : « Les décisions que l'équipe a prises hier ont été communiqué aux familles. »",
    "La forme correcte est : « Les décisions que l'équipe a prises hier ont été communiquées aux familles. » Deux règles sont en jeu. D'abord, « prises » porte l'accord du participe passé employé avec « avoir » : le complément d'objet direct « que », qui reprend « les décisions », est placé avant le verbe, donc le participe s'accorde avec lui au féminin pluriel. Ensuite, « communiquées » fait partie d'un verbe à la voix passive (« ont été communiquées ») : le participe passé employé avec « être » s'accorde avec le sujet, ici « les décisions », féminin pluriel. On notera que l'accord ne se fait jamais avec « aux familles », complément d'objet indirect. La phrase gagne aussi en clarté si l'on précise le canal de communication, par exemple « ont été communiquées aux familles par courriel ».",
    "On attend les deux corrections et la distinction entre accord du participe avec COD antérieur et accord du passif avec le sujet."),
 QT("Réécrivez ce passage en améliorant les liaisons et la clarté : « On a fait une réunion. On a parlé du budget. Il a été décidé de réduire les dépenses. Les associations sont concernées. Elles ont dit non. »",
    "Réécriture proposée : « Lors de la réunion du 12 mars, l'équipe a examiné le budget prévisionnel et a décidé de réduire les dépenses de fonctionnement de 8 %. Les associations partenaires, consultées en amont, ont toutefois émis un avis défavorable à cette réduction, estimant qu'elle fragiliserait les actions d'accompagnement. Une nouvelle concertation est donc prévue avant toute décision définitive. » Les modifications portent sur trois points : les phrases courtes et répétitives sont regroupées autour d'un verbe principal ; les connecteurs (« et », « toutefois », « donc ») explicitent l'opposition et la conséquence ; les pronoms ambigus (« il », « elles ») sont remplacés par des noms précis. Le résultat est plus dense, plus lisible et mieux adapté à un compte rendu destiné à des partenaires.",
    "On valorise le regroupement des idées, la variété et la justesse des connecteurs, et la suppression des pronoms ambigus.")],
C("La clarté d'un écrit vient de phrases structures, d'accords corrects et de liaisons choisies avec précision.",
  "Accord du participe : avec COD antérieur après « avoir », avec le sujet après « être »",
  "Qui = sujet · que = COD · dont = complément en « de » · où = lieu ou temps",
  "Sujet~Qui agit~Accord du verbe|COD~Ce qui subit l'action~Accord du participe après avoir|Conjonction~Lien logique~Cause, conséquence, opposition",
  "Repérer le verbe et son sujet dans chaque phrase|Vérifier la fonction des pronoms relatifs|Contrôler les accords du participe passé|Choisir le connecteur logique exact|Relire pour la clarté puis pour l'orthographe",
  "Accorder le participe avec le complément après le verbe|Confondre « dont » et « où »|Employer « car » pour une conséquence|Laisser un pronom sans référence claire",
  "Décisions prises~COD antérieur~Communiquées~Accord du passif~Dont~Complément en de~Cependant~Opposition",
  "Car~La cause~Donc~La conséquence~Cependant~L'opposition",
  "Voix active~Le sujet agit~Voix passive~L'action est mise en avant"),
UG)

# ============================================================ CG6
add("CG6.", "Vocabulaire, registres et figures de style", "Culture générale et expression", ["BTS1"],
S("Le vocabulaire d'un texte n'est pas neutre : chaque choix lexical situe l'auteur sur une échelle de ton, de distance et d'intention."
  "|Le registre courant ou neutre recherche la clarté et la simplicité : c'est le registre privilégié des écrits professionnels."
  "|Le registre soutenu utilise des mots plus recherchés et des tournures plus complexes ; il peut produire de la solennité ou de la distance."
  "|Le registre familier, avec ses abréviations et ses expressions idiomatiques, crée une proximité mais peut nuire à la crédibilité d'un écrit formel."
  "|Un champ lexical est un ensemble de mots partageant un même thème : il oriente l'interprétation et structure la cohérence d'un passage."
  "|La polysémie désigne la pluralité des sens d'un mot : le contexte détermine le sens actualisé."
  "|La synonymie et l'antonymie permettent d'éviter les répétitions ou de construire des oppositions significatives."
  "|La métaphore transpose un terme d'un domaine vers un autre sans outil de comparaison ; la comparaison utilise un outil explicite."
  "|La métonymie remplace un terme par un autre qui lui est lié : « le bras » pour « l'aide apportée », « la plume » pour « lasignature »."
  "|L'ironie dit le contraire de ce que l'on pense pour produire un effet critique ; elle suppose un lecteur capable de déceler le décalage."
  "|L'hyperbole exagère volontairement pour frapper ; la litote atténue pour suggérer davantage que ce qui est dit."
  "|Choisir son vocabulaire en BTS ESF, c'est adapter le ton au destinataire : usager, collègue, partenaire institutionnel ou grand public."),
[QC("Quel registre convient à un courrier administratif ?", "Le registre familier~Le registre courant ou neutre~Le registre comique~Le registre argotique", 1,
    "Le registre neutre privilégie la clarté et la correction, attendues dans un écrit professionnel."),
 QC("Qu'est-ce qu'un champ lexical ?", "Un dictionnaire de synonymes~Un ensemble de mots liés à un même thème~Une figure de style~Une règle de grammaire", 1,
    "Le champ lexical regroupe les mots qui partagent une mêmeorientation sémantique."),
 QC("Quelle figure utilise un outil explicite de comparaison ?", "La métaphore~La comparaison~La métonymie~La litote", 1,
    "La comparaison emploie « comme », « tel », « semblable à » ; la métaphore transfère directement."),
 QC("Quel sens d'un mot est déterminé par le contexte ?", "Le sens étymologique~Le sens actualisé~Le sens littéral du titre~Le sens de la phrase précédente seulement", 1,
    "Un mot polysémique prend dans la phrase le sens que le contexte rend pertinent."),
 QC("Quel procédé remplace un terme par un élément qui lui est lié ?", "La métonymie~L'hyperbole~L'antithèse~L'allitération", 0,
    "La métonymie repose sur un lien de contiguïté, par exemple « la plume » pour l'écriture."),
 QC("Que produit une litote ?", "Une exagération~Une atténuation qui suggère davantage~Une répétition~Une faute de syntaxe", 1,
    "La litote dit moins pour faire entendre plus, à l'inverse de l'hyperbole."),
 QC("Pourquoi adapter son registre au destinataire ?", "Pour utiliser le plus de mots possible~Pour être compris et crédible~Pour masquer le sens~Pour respecter une mode", 1,
    "Le registre doit tenir compte de la relation avec le lecteur et du cadre professionnel."),
 QT("Analysez la phrase : « Ce dossier est un lavabo où l'on vient se laver les mains de toute responsabilité. » Identifiez les procédés et leur effet.",
    "La phrase repose d'abord sur une métaphore filée : le dossier est comparé à un lavabo, sans outil de comparaison, puis le champ lexical de l'eau et du lavage est poursuivi avec « se laver les mains ». Il y a ensuite un jeu de sens sur l'expression « se laver les mains de quelque chose », qui signifie refuser sa responsabilité : l'image littérale du lavabo rend visible cette expression figée. Le terme « lavabo » appartient à un registre courant, presque comique, qui crée une distance critique et une ironie : l'auteur ne dit pas « ce dossier permet de se décharger », il fait voir la scène. L'effet est double : frapper l'imagination par l'image concrète et dénoncer, sur le mode satirique, une pratique professionnelle de déresponsabilisation. Le choix de « vient », au présent, généralise le comportement et l'inscrit dans une habitude plutôt que dans un fait isolé.",
    "On attend l'identification de la métaphore filée, du champ lexical, du jeu sur l'expression et de l'effet critique produit."),
 QT("Dans un rapport destiné à une direction d'établissement, reformulez en registre neutre la phrase suivante : « Le machin qu'on a bricolé a complètement foiré, donc on a dû tout refaire en vitesse. » Expliquez vos choix.",
    "Reformulation : « Le dispositif provisoire mis en place s'est révélé inopérant ; il a été nécessaire de le reprendre intégralement dans un délai court. » Les choix portent sur plusieurs points : « machin » est remplacé par « dispositif provisoire », terme précis et professionnel ; le registre familier « bricolé » et « foiré » cède la place à « mis en place » et « s'est révélé inopérant », qui décrivent le fait sans jugement personnel ; « en vitesse » devient « dans un délai court », plus objectif ; enfin, le pronom indéfini « on » est évité au profit d'une formulation qui centre le propos sur le dispositif et la contrainte de temps. Le rapport gagne en crédibilité : il relate un incident sans dramatisation ni familiarité, tout en conservant l'information essentielle (échec du provisoire, reprise complète, urgence). On pourrait ajouter la cause de l'échec si elle est connue, car un rapport utile autant à comprendre qu'à constater.",
    "La réponse doit proposer une reformulation réellement neutre et justifier le remplacement des termes familiers et des pronoms vagues.")],
C("Le sens d'un texte dépend de choix lexicaux : registre, champs lexicaux et figures de style produisent des effets sur le lecteur.",
  "Métaphore = transfert direct · comparaison = transfert avec outil · métonymie = terme lié",
  "Neutre pour le professionnel · soutenu pour la solennité · familier pour la proximité",
  "Registre~Ton adopté~Destinataire|Champ lexical~Thème récurrent~Orientation du sens|Figure~Procédé de style~Effet produit",
  "Identifier le registre employé|Repérer les champs lexicaux|Nommer les figures de style|Analyser leur effet sur le lecteur|Adapter son propre vocabulaire au destinataire",
  "Confondre métaphore et comparaison|Employer un registre familier dans un rapport|Ignorer la polysémie|Multiplier les figures sans intention",
  "Lavabo~Métaphore filée~Se laver les mains~Expression figée~Inopérant~Registre neutre~Litote~Atténuation~Hyperbole~Exagération",
  "Hyperbole~Exagère~Litote~Atténue pour suggérer~Ironie~Dit le contraire",
  "Métaphore~Transfert sans outil~Comparaison~Transfert avec outil"),
U1)

# ============================================================ CG7
add("CG7.", "L'expression orale : exposé, entretien et prise de parole", "Culture générale et expression", ["BTS1"],
S("La prise de parole en public combine trois dimensions : le contenu, la forme du discours et la présence de l'orateur."
  "|Avant de parler, il faut analyser la consigne, identifier le destinataire, déterminer l'objectif et choisir les idées essentielles."
  "|Un exposé suit une structure simple : annonce du plan, développement de deux ou trois points, conclusion synthétique."
  "|Un plan trop dense est contre-productif : l'auditoire retient mieux trois idées bien illustrées que dix idées effleurées."
  "|Les notes doivent être courtes : mots-clés et chiffres, jamais un texte rédigé que l'on serait tenté de lire."
  "|Le débit, les pauses et le volume rendent le discours intelligible ; les pauses marquent les transitions et laissent le temps de la compréhension."
  "|La voix et le regard distribuent l'attention : regarder l'auditoire plutôt que les notes installe une relation de confiance."
  "|Les gestes doivent rester sobres et cohérents avec le propos ; une posture droite et ouverte renforce la crédibilité."
  "|L'entretien oral est un échange : on répond à la question posée, on appuie ses affirmations sur des exemples et on reste à l'écoute."
  "|Face à une question imprévue, une stratégie utile consiste à reformuler la question, à prendre un temps de réflexion, puis à répondre avec une structure courte."
  "|Le trac est normal : la préparation, la respiration et la répétition à voix haute en réduisent les effets sans le supprimer totalement."
  "|En BTS ESF, l'oral évalue la capacité à présenter un projet, à défendre une position et à interagir avec un jury ou un groupe."),
[QC("Quel contenu doivent avoir des notes d'exposé efficaces ?", "Un texte intégral rédigé~Des mots-clés et des chiffres~La liste des questions du jury~Le plan du voisin", 1,
    "Des notes courtes permettent de regarder l'auditoire et d'improviser les transitions."),
 QC("Combien d'idées principales faut-il privilégier dans un exposé bref ?", "Une dizaine~Trois environ~Autant que de diapositives~Le plus possible", 1,
    "Trois points bien développés sont plus mémorables qu'une longue énumération."),
 QC("Quel est le rôle d'une pause dans une prise de parole ?", "Remplir le temps~Marquer une transition et faciliter la compréhension~Cacher une erreur~Remplacer la conclusion", 1,
    "La pause structure l'écoute et donne du poids aux idées."),
 QC("Que faire face à une question imprévue en entretien ?", "Répondre immédiatement sans y penser~Reformuler, prendre un temps, puis répondre~Refuser de répondre~Changer de sujet", 1,
    "La reformulation et un court temps de réflexion permettent une réponse structurée."),
 QC("Quel comportement renforce la crédibilité de l'orateur ?", "Lire sans lever les yeux~Regarder l'auditoire et adopter une posture ouverte~Parler très vite~Multiplier les gestes", 1,
    "Le regard et une posture stable installent une relation de confiance."),
 QC("Que faut-il faire avant un exposé ?", "Analyser la consigne et le destinataire~Apprendre par coeur un texte long~Ignorer le temps imparti~Éviter toute répétition", 0,
    "La préparation commence par la consigne, le public visé et l'objectif du discours."),
 QC("Comment réduire les effets du trac ?", "En évitant de préparer~En respirant et en répétant à voix haute~En parlant plus vite~En supprimant les pauses", 1,
    "Préparation, respiration et répétition rendent le trac gérable."),
 QT("Préparez l'introduction d'un exposé de cinq minutes intitulé « Comment favoriser l'accès aux droits dans un centre social ? » Vous préciserez l'accroche, la problématique et l'annonce du plan.",
    "Accroche : « Une personne peut avoir droit à une prestation et pourtant ne jamais la demander : dans un centre social, l'accès aux droits ne se limite donc pas à l'information affichée dans le hall. » Cette ouverture part d'un constat concret et crée un écart entre le droit théorique et l'accès réel. Définition rapide : accéder à un droit, c'est connaître l'existence du dispositif, comprendre la démarche, réunir les pièces et être accompagné jusqu'à la décision. Problématique : comment un centre social peut-il réduire les obstacles qui séparent une personne de ses droits, sans se substituer à elle ? Annonce du plan : nous examinerons d'abord les obstacles à l'accès (information, complexité administrative, langue, peur du jugement), puis les leviers d'accompagnement (accueil individualisé, médiation, travail avec les partenaires), avant d'évaluer les limites de l'action et la nécessité de préserver l'autonomie de la personne. Le ton reste clair, neutre et professionnel, avec trois points seulement pour respecter le temps imparti.",
    "On attend une accroche concrète, une problématique formulée en question et une annonce de plan en trois points cohérente avec le titre."),
 QT("Un membre du jury vous interrompt et conteste un chiffre que vous avez avancé. Comment réagir constructivement ?",
    "Je ne cherche pas à avoir le dernier mot : je remercie la personne de sa remarque et je reformule précisément la contestation, par exemple « vous contestez la source du chiffre de 30 % que j'ai cité, est-ce bien cela ? ». Je précise ensuite la source, la date et le périmètre de la donnée, en reconnaissant ses limites si elle repose sur un échantillon restreint. Si je ne suis pas certain de la référence exacte, je le dis simplement et je propose de vérifier après l'exposé ou de raisonner sans ce chiffre, en m'appuyant sur la tendance générale observée dans les documents. Je garde un ton calme, je ne me justifie pas de façon agressive et je reviens rapidement à la question principale. Cette attitude montre au jury que je maîtrise mon propos, que je distingue une donnée sourcée d'une affirmation et que je reste capable d'interagir, ce qui est précisément attendu d'un professionnel de l'action sociale.",
    "La réponse doit montrer écoute, reformulation, précision de la source, reconnaissance des limites et retour au fil de l'exposé.")],
C("Parler en public, c'est préparer trois idées, les structurer, puis les transmettre avec une voix et une posture qui servent le sens.",
  "Exposé = accroche + problématique + 3 points + conclusion",
  "Notes courtes · pauses · regard · débit · reformulation des questions",
  "Contenu~Idées et exemples~Fond de l'exposé|Forme~Voix, pauses, regard~Transmission|Échange~Questions du jury~Interaction",
  "Analyser la consigne et le public|Choisir trois idées essentielles|Préparer des notes courtes|Répéter à voix haute en chronométrant|Gérer le regard, les pauses et les questions",
  "Lire un texte rédigé|Surcharger le plan|Parler sans regarder l'auditoire|Improviser une réponse sans reformuler la question",
  "5 minutes~Trois points~Notes~Mots-clés~Pause~Transition~Trac~Respiration et répétition",
  "Exposé~Discours préparé~Entretien~Échange avec le jury",
  "Débit~Vitesse de parole~Volume~Intensité de la voix"),
"Unité U1 (culture générale et expression), référentiel BTS ESF 2022")

# ============================================================ CO1
add("CO1.", "Les modèles de la communication : émetteur, message, récepteur", "Communication", ["BTS1"],
S("La communication est un processus d'échange d'informations entre acteurs, visant à créer du sens, de la compréhension ou de l'action."
  "|Le modèle linéaire de Shannon et Weaver décrit une chaîne : émetteur, code, message, canal, décodage, récepteur, avec possibilité de bruit."
  "|L'émetteur construit et encode un message ; le récepteur le reçoit et le décode selon ses propres références culturelles et son contexte."
  "|Le code est l'ensemble des signes utilisés : langue, jargon professionnel, images, gestes, codes graphiques."
  "|Le canal est le support de transmission : parole, courriel, téléphone, affiche, réseau social, réunion."
  "|Le bruit désigne tout ce qui perturbe la transmission : mauvaise connexion, ambiguïté lexicale, préjugé, surcharge d'information, contexte culturel différent."
  "|Le modèle de Schramm insiste sur le partage d'un champ d'expérience : la communication réussit quand émetteur et récepteur ont des repères communs."
  "|Le modèle circulaire d'Osgood et Schramm introduit le feed-back : chaque acteur est tour à tour émetteur et récepteur."
  "|Le feed-back (retour d'information) permet de vérifier la compréhension et d'ajuster le message ; son absence expose au malentendu."
  "|La redondance, c'est-à-dire la répétition partielle de l'information, peut compenser le bruit mais excessive elle lasse l'auditoire."
  "|La communication est à la fois un transfert d'information et une construction de sens : le récepteur n'est pas un récipient passif."
  "|Dans un service social, choisir le bon code et le bon canal Conditionne l'accès aux droits et l'efficacité de l'accompagnement."),
[QC("Dans le modèle de Shannon et Weaver, que désigne le « bruit » ?", "Un son trop fort uniquement~Tout élément qui perturbe la transmission~Le récepteur~Le code utilisé", 1,
    "Le bruit est toute perturbation du message, y compris un malentendu culturel ou une ambiguïté."),
 QC("Quel modèle introduit explicitement le feed-back ?", "Le modèle linéaire classique~Le modèle circulaire~Le modèle de la pyramide~Le modèle de Maslow", 1,
    "Le modèle circulaire fait de l'échange un va-et-vient avec retour d'information."),
 QC("Que désigne le « code » dans une situation de communication ?", "Le canal utilisé~L'ensemble des signes employés~Le destinataire~La durée de l'échange", 1,
    "Le code est le système de signes : mots, jargon, gestes, images."),
 QC("Quel est un exemple de bruit lié au contexte culturel ?", "Une surcharge d'information~Une expression idiomatique incomprise par l'usager~Une bonne connexion~Une question de clarification", 1,
    "Une expression locale ou un jargon peut être décodé différemment selon les repères culturels."),
 QC("À quoi sert le feed-back ?", "À allonger le message~À vérifier la compréhension et à ajuster~À supprimer le code~À remplacer le récepteur", 1,
    "Le retour d'information permet de corriger le message et de confirmer sa réception."),
 QC("Que souligne le champ d'expérience commun (Schramm) ?", "Que la communication dépend de repères partagés~Qu'il faut parler plus fort~Que le canal est inutile~Que le message doit être long", 0,
    "Sans repères communs, l'émetteur et le récepteur ne construisent pas le même sens."),
 QC("Quel canal convient pour une information urgente et courte ?", "Un rapport de vingt pages~Un appel téléphonique ou un message court~Une affiche ancienne~Un silence", 1,
    "Le canal doit être choisi selon l'urgence, la cible et la complexité du message."),
 QT("Un centre social envoie un courrier administratif à des usagers pour expliquer une nouvelle procédure. Une semaine après, la moitié d'entre eux n'a pas compris la démarche. Analysez la situation avec les modèles de la communication et proposez des corrections.",
    "L'analyse peut s'appuyer sur la chaîne de Shannon et Weaver. L'émetteur est le centre social, le code est un code administratif probablement trop technique, le canal est le courrier écrit, le message décrit la procédure, et le récepteur est l'usager. Le bruit n'est pas ici un problème technique mais un décalage de codes : jargon, phrases longues, absence d'exemples, méconnaissance des repères de l'usager. Le modèle de Schramm montre que le champ d'expérience commun est insuffisant : le centre et l'usager ne partagent pas les mêmes références administratives. Enfin, l'absence de feed-back est décisive : personne n'a vérifié en amont si le message était compris, et le retour n'arrive qu'après une semaine. Les corrections consistent à simplifier le code (mots courants, phrases courtes, étapes numérotées), à ajouter un exemple concret et une ligne d'explication pour chaque pièce demandée, à compléter le canal (courrier plus accueil téléphonique ou atelier d'information), à tester le message auprès de quelques usagers avant envoi généralisé, et à organiser un feed-back rapide : numéro de contact, questionnaire court, relance par les médiateurs. On vérifie alors non pas que le courrier a été envoyé, mais qu'il a été compris.",
    "On attend l'usage explicite des notions d'émetteur, code, canal, bruit, champ commun et feed-back, puis des actions correctrices adaptées."),
 QT("Distinguer information, communication et médiation, et montrer comment ces trois notions interviennent dans l'accueil d'un usager en difficulté avec un dossier.",
    "L'information est la transmission d'une donnée : par exemple la liste des pièces à fournir, énoncée de façon neutre. La Communication est un processus plus large : elle inclut la manière dont le message est construit, le canal choisi, le ton employé et le retour de l'usager, donc la création de sens partagé. La médiation intervient quand les repères des deux parties sont trop éloignés ou quand un conflit de compréhension apparaît : le médiateur traduit, reformule, explique les enjeux de chaque côté et aide à construire une décision acceptable. Dans l'accueil d'un usager en difficulté, l'information consiste à donner la liste des pièces ; la communication suppose de vérifier que l'usager a compris, d'adapter le vocabulaire et d'écouter ses questions ; la médiation devient nécessaire si l'usager se sent jugé, si le personnel s'impatiente ou si les exigences administratives entrent en conflit avec sa situation concretement vécue. Le médiateur ne décide pas à la place de l'usager : il rend la communication possible pour que l'usager redevienne acteur de sa démarche.",
    "La réponse doit définir les trois notions et les articuler dans un scénario d'accueil concret et réaliste.")],
C("Communiquer, c'est construire du sens entre acteurs : le message circule, mais il peut être déformé sans retour d'information.",
  "Émetteur → code → message → canal → récepteur + feed-back",
  "Bruit = toute perturbation · champ d'expérience commun = repères partagés · feed-back = vérification",
  "Émetteur~Construit le message~Intention|Canal~Support de transmission~Courrier, oral, réseau|Bruit~Perturbation~Jargon ou contexte",
  "Définir l'objectif de la communication|Choisir le code et le canal adaptés|Construire un message clair|Prévoir un feed-back|Vérifier la compréhension et ajuster",
  "Croire que l'envoi garantit la réception|Utiliser le jargon professionnel avec un usager|Négliger le feed-back|Confondre canal et code",
  "Courrier~Canal écrit~Jargon~Bruit sémantique~Feed-back~Retour d'information~Schramm~Champ commun",
  "Modèle linéaire~Sens unique~Modèle circulaire~Va-et-vient et feed-back",
  "Information~Donnée transmise~Communication~Sens construit ensemble"),
"Programmes d'enseignement général applicables en BTS, référentiel BTS ESF 2022")

# ============================================================ CO2
add("CO2.", "Communication verbale et non verbale", "Communication", ["BTS1"],
S("La communication verbale utilise des mots, tandis que la communication non verbale passe par le corps, le regard, la voix, l'espace et les objets."
  "|Les deux dimensions sont simultanées : même un message neutre est accompagné d'une posture, d'un ton et d'un regard qui l'interprètent."
  "|Les gestes, la mimique et la posture constituent la communication non verbale corporelle."
  "|La proxémique étudie la distance entre les personnes : trop proche, elle peut être ressentie comme intrusive ; trop lointaine, comme froide."
  "|La paralangue regroupe les éléments vocaux non lexicaux : débit, volume, timbre, pauses, soupirs, rire."
  "|Le regard régit le contact et la confirmation : il peut inviter à parler, rassurer ou, au contraire, mettre à distance."
  "|L'espace et l'aménagement (disposition des chaises, hauteur du comptoir, présence d'un bureau) portent un message sur le pouvoir et l'accueil."
  "|Les objets et les vêtements (badge, tenue professionnelle, documents) sont également des signes qui construisent une identité professionnelle."
  "|Quand le verbal et le non verbal se contredisent, l'auditoire croit généralement le non verbal : c'est le paradoxe de la communication."
  "|Une écoute attentive se manifeste par des signes visibles : hochement de tête, regard, reformulation, silence respecté."
  "|L'interprétation d'un signe non verbal dépend du contexte culturel : un même geste peut avoir des sens différents selon les personnes."
  "|En accompagnement social, la cohérence entre les mots, le ton et la posture est une condition de confiance et de respect de la personne."),
[QC("Quel élément relève de la paralangue ?", "Le choix d'un mot technique~Le débit et le volume de la voix~La disposition des chaises~La couleur du badge", 1,
    "La paralangue concerne les caractéristiques vocales non lexicales : débit, volume, timbre, pauses."),
 QC("Quand le verbal et le non verbal se contredisent, quel message est le plus souvent cru ?", "Le verbal toujours~Le non verbal~Aucun des deux~Le message écrit", 1,
    "Le non verbal est perçu comme plus spontané et donc plus crédible en cas de contradiction."),
 QC("Que désigne la proxémique ?", "L'étude des gestes~L'étude des distances interpersonnelles~L'étude du vocabulaire~L'étude des couleurs", 1,
    "La proxémiqueanalyse l'usage de l'espace et de la distance dans la communication."),
 QC("Quel signe de bonne écoute est visible ?", "Le silence absolu sans réaction~Le hochement de tête et la reformulation~Le regard vers la sortie~La consultation du téléphone", 1,
    "Les marqueurs d'écoute sont le regard, les hochements de tête et la reformulation."),
 QC("Quel risque présente un comptoir très haut à l'accueil ?", "Aucun~Il peut créer une distance symbolique et une sensation de domination~Il améliore toujours l'écoute~Il supprime les malentendus", 1,
    "L'aménagement spatial porte un message sur le rapport de pouvoir et l'ouverture de l'accueil."),
 QC("Pourquoi interpréter un geste avec prudence ?", "Parce que son sens dépend du contexte culturel~Parce que les gestes n'ont jamais de sens~Parce que le corps ne communique pas~Parce que le verbal est toujours faux", 0,
    "Un même geste peut signifier des choses différentes selon les cultures et les individus."),
 QC("Quelle tenue professionnelle envoie un message de crédibilité ?", "Une tenue négligée~Une tenue propre, adaptée et cohérente avec le service~Un déguisement~Aucune tenue particulière", 1,
    "Les objets et la tenue participent à l'identité professionnelle et à la confiance."),
 QT("Un éducateur dit à un usager « Je vous écoute » tout en regardant sa montre et en tapant sur son clavier. Analysez la situation et proposez une correction.",
    "Le message verbal est accueillant, mais les signes non verbaux le contredisent : le regard vers la montre indique l'impatience ou la contrainte de temps, et le bruit du clavier signale une attention portée à autre chose. Selon le principe de cohérence, l'usager croira vraisemblablement le non verbal : il se sentira dérangé, peu important, peut-être jugé. La situation illustre le paradoxe de la communication : les mots disent une chose, le corps en dit une autre. Pour corriger, l'éducateur peut d'abord s'arrêter de taper, poser les mains sur la table et regarder l'usager ; il peut ensuite dire explicitement « Je vous accorde cinq minutes, après je dois répondre à un appel, mais je reviens vous voir à 15 heures ». Cette formulation rend la contrainte de temps visible et n'improvise pas une disponibilité qu'il n'a pas. Il peut enfin reformuler ce qu'il a entendu pour montrer que l'écoute est réelle. La correction ne consiste donc pas seulement à changer de posture, mais à aligner le discours, le comportement et l'organisation concretement possible de l'entretien.",
    "On attend l'analyse de la contradiction, le principe de crédibilité du non verbal et une correction qui porte à la fois sur le corps et sur la gestion explicite du temps."),
 QT("Comment aménager un espace d'accueil pour favoriser une communication respectueuse avec des usagers en situation de vulnérabilité ?",
    "On agira sur plusieurs dimensions. La distance d'abord : un comptoir très haut ou une vitre installe une barrière ; un espace de discussion avec deux fauteuils à la même hauteur, légèrement de biais plutôt que face à face, réduit la sensation d'interrogatoire. La disposition des lieux ensuite : un chemin d'accès dégagé, un écriteau lisible, un espace d'attente pourvu de chaises et d'informations permettent à la personne de se repérer avant même l'échange. Les objets comptent aussi : supprimer les écrans visibles pendant l'entretien, éviter les dossiers empilés entre l'usager et le professionnel, garder à portée de main de quoi noter avec l'accord de la personne. La lumière et le bruit participent à la qualité de l'écoute : on évitera une pièce trop bruyante ou trop éclairée. Enfin, la posture professionnelle elle-même fait partie de l'aménagement : se lever pour accueillir, se présenter, demander comment la personne souhaite être appelée. Aucun de ces éléments ne remplace l'écoute, mais ils créent les conditions matérielles d'une communication respectueuse et d'un consentement libre à l'échange.",
    "La réponse doit traiter distance, mobilier, objets, environnement sensoriel et posture, en reliant chaque choix à son effet sur la communication.")],
C("Les mots ne suffisent pas : posture, regard, voix et espace interprètent le message et conditionnent la relation d'aide.",
  "Verbal + non verbal = message réellement reçu",
  "Paralangue : débit, volume, pauses · proxémique : distance · cohérence des signes",
  "Verbal~Mots employés~Contenu|Non verbal~Corps, voix, espace~Interprétation|Cohérence~Accord des signes~Confiance",
  "Prendre conscience de sa posture|Adapter la distance et le regard|Contrôler le débit et les pauses|Aligner les mots sur les faits|Vérifier la réception par une reformulation",
  "Dire « je vous écoute » en consultant sa montre|Ignorer les différences culturelles|Garder un bureau fermé pour un entretien confidentiel|Multiplier les gestes sans rapport",
  "Montre~Impatience perçue~Clavier~Attention distrai te~Fauteuils~Distance réduite~Badge~Identité professionnelle",
  "Paralangue~Voix sans mots~Langage verbal~Mots et phrases",
  "Proxémique~Distance~Espace~Disposition des lieux"),
"Programmes d'enseignement professionnel, référentiel BTS ESF 2022")

# ============================================================ CO3
add("CO3.", "L'écoute active et le questionnement", "Communication", ["BTS1"],
S("L'écoute active est une écoute involvée dans laquelle le professionnel cherche à comprendre le point de vue de l'autre avant de répondre ou de conseiller."
  "|Elle se distingue de l'écoute passive, où l'on entend sans manifester de compréhension ni vérifier le sens."
  "|Les techniques d'écoute active incluent la reformulation, la clarification, la synthèse, le silence et la réflexion des émotions."
  "|La reformulation consiste à redire avec ses propres mots ce que l'interlocuteur vient d'exprimer, sans ajouter d'interprétation."
  "|La clarification demande une précision sur un point ambigu : « Pouvez-vous préciser ce que vous entendez par là ? »"
  "|La synthèse regroupe les éléments essentiels d'un long propos pour vérifier la compréhension globale."
  "|La réflexion des émotions nomme le sentiment perceptible sans l'imposer : « Vous semblez inquiet à l'idée de ce rendez-vous. »"
  "|Le silence respecte le temps de la pensée : il ne doit pas être comblé trop vite par une question ou un conseil."
  "|Les questions ouvertes commencent par comment, quoi, qu'est-ce qui, et invitent à un développement ; les questions fermées appellent oui ou non."
  "|Une question fermée reste utile pour vérifier un fait précis ou obtenir une décision, mais elle réduit l'expression."
  "|Les questions suggestives orientent la réponse et doivent être évitées dans un entretien d'aide : « Vous n'avez pas encore fait la démarche, non ? »"
  "|L'écoute active ne signifie pas approuver tout : elle permet de comprendre avant d'évaluer, et elle respecte le cadre déontologique de l'intervention."),
[QC("Qu'est-ce qu'une reformulation ?", "Répéter mot pour mot~Redire avec ses propres mots ce que l'autre a dit~Donner son avis~Poser une question fermée", 1,
    "La reformulation restitue le sens avec d'autres mots, sans interprétation ajoutée."),
 QC("Quelle question invite le plus à développer ?", "Une question fermée~Une question ouverte~Une question suggestive~Une question rhétorique", 1,
    "La question ouverte appelle une réponse construite et laisse le choix des mots à l'interlocuteur."),
 QC("Que permet le silence dans un entretien ?", "À gagner du temps~À laisser la personne penser et s'exprimer~À éviter de répondre~À clore l'entretien", 1,
    "Le silence respecte le rythme de l'autre et favorise l'émergence de ce qu'il a du mal à dire."),
 QC("Quel est un exemple de question suggestive ?", "« Qu'avez-vous compris de la lettre ? »~« Vous êtes bien d'accord pour signer, non ? »~« Pouvez-vous préciser ? »~« Qu'est-ce qui vousinquiète ? »", 1,
    "La question suggestive suggère la réponse attendue et réduit la liberté de l'interlocuteur."),
 QC("À quoi sert la synthèse en fin d'entretien ?", "À conclure administrativement~À vérifier la compréhension globale~À imposer une solution~À changer de sujet", 1,
    "La synthèse regroupe les points essentiels et permet de valider ce qui a été compris."),
 QC("Quel risque présente un conseil donné trop tôt ?", "Il rassure toujours~Il coupe l'expression et peut imposer une solution inadaptée~Il est interdit~Il remplace l'écoute par la contradiction", 1,
    "Conseiller avant d'avoir compris empêche l'usager d'explorer sa propre situation."),
 QC("L'écoute active implique-t-elle d'approuver tout ?", "Oui, toujours~Non, elle vise la compréhension avant l'évaluation~Oui, sauf si le propos est choquant~Non, elle interdit tout jugement professionnel", 1,
    "Comprendre ne signifie pas adhérer ; le cadre déontologique reste applicable."),
 QT("Un usager déclare : « Depuis que mon fils est parti, je ne sais plus quoi faire de mes journées. En plus, la caisse m'a encore demandé une pièce que j'avais déjà envoyée. » Proposez une réponse fondée sur l'écoute active en deux ou trois phrases.",
    "Une réponse possible : « Si je comprends bien, le départ de votre fils a bouleversé votre quotidien, et en plus de cette solitude, la demande de pièce vous donne le sentiment de recommencer sans cesse les mêmes démarches. C'est épuisant d'avoir l'impression que rien n'est pris en compte. Pouvez-vous me dire ce qui vous pèse le plus en ce moment : le vide des journées ou la répétition des démarches ? » Cette réponse comporte trois techniques : une reformulation qui regroupe les deux éléments énoncés sans en hiérarchiser l'importance à la place de l'usager, une réflexion des émotions prudent (« vous donne le sentiment », « c'est épuisant ») qui nomme sans imposer, et une question ouverte qui permet à la personne de choisir le point prioritaire. On évite le conseil immédiat (« il faut prendre un rendez-vous ») et la question fermée (« ça va aller ? »), qui closent prématurément l'échange. La vérification finale est assurée par la question, qui invite l'usager à préciser ou à corriger la compréhension proposée.",
    "On attend une reformulation fidèle, une émotion nommée avec prudence, une question ouverte et l'absence de conseil prématuré."),
 QT("Distinguer question ouverte, question fermée et question suggestive, et indiquer dans quels contextes professionnels les utiliser.",
    "La question ouverte (« Comment se passe la remise des repas ? ») ne peut être réduite à oui ou non ; elle est privilégiée en début d'entretien, pour explorer une situation, laisser l'usager choisir ses mots et faire émerger des informations inattendues. La question fermée (« Avez-vous reçu le courrier ? ») appelle une réponse courte ; elle est utile pour vérifier un fait, confirmer une date ou recueillir une décision, mais elle sature si elle est utilisée en série, car elle transforme l'échange en interrogatoire. La question suggestive (« Vous êtes bien d'accord pour signer, maintenant ? ») contient déjà la réponse souhaitée ; elle doit être évitée dans l'accompagnement, car elle exerce une pression et fausse le consentement. Elle peut cependant être repérée chez autrui : si un usager répond « oui » à ce type de question, le professionnel doit vérifier que le oui est libre et éclairé. Le bon usage combine donc questions ouvertes pour comprendre, questions fermées pour vérifier, et vigilance critique à l'égard des formulations orientées.",
    "La réponse doit définir les trois types de questions, donner un exemple de chacun et préciser leur usage professionnel.")],
C("Écouter activement, c'est reformuler, clarifier, respecter le silence et questionner sans orienter, avant toute proposition d'aide.",
  "Écoute active = compréhension vérifiée avant action",
  "Questions ouvertes pour explorer · fermées pour vérifier · suggestives à éviter",
  "Reformulation~Redire avec ses mots~Vérification|Question ouverte~Laisse développer~Exploration|Silence~Temps de pensée~Respect",
  "Se disposer à écouter sans préparer sa réponse|Reformuler les propos essentiels|Nommer prudemment l'émotion|Poser une question ouverte|Synthétiser et vérifier avant de proposer",
  "Répondre avant d'avoir compris|Multiplier les questions fermées|Combler tous les silences|Confondre compréhension et approbation",
  "Reformulation~Mot pour mot évité~Question ouverte~Comment, quoi~Question suggestive~Réponse suggérée~Silence~Temps laissé",
  "Question ouverte~Explorer le vécu~Question fermée~Vérifier un fait",
  "Écoute active~Comprendre~Écoute passive~Entendre sans vérifier"),
"Programmes d'enseignement professionnel, référentiel BTS ESF 2022")

# ============================================================ CO4
add("CO4.", "L'écrit professionnel : courrier, courriel et compte rendu", "Communication", ["BTS1"],
S("Un écrit professionnel est un document produit dans un cadre institutionnel, destiné à informer, demander, décider ou tracer une action."
  "|Ses qualités principales sont la clarté, la concision, la correction linguistique et l'adaptation au destinataire."
  "|Le courrier administratif comporte un en-tête, une date, un objet, une formule de politesse, un corps structuré et une signature."
  "|La ligne d'objet doit être précise : elle permet de classer le message et d'en connaître l'enjeu avant la lecture."
  "|Le courriel professionnel reprend cette structure en la raccourcissant : objet, salutation, une à trois paragraphes, formule de clôture, signature complète."
  "|Les pièces jointes doivent être annoncées, nommées de façon explicite et limitées à ce qui est utile au destinataire."
  "|Le compte rendu restitue objectivement les points abordés, les décisions prises, les responsabilités et les échéances, sans anecdote ni jugement."
  "|Un bon compte rendu distingue ce qui a été dit de ce qui a été décidé et indique les points en attente de réponse."
  "|La hiérarchie de l'information s'obtient par des paragraphes courts, des titres, des listes et un usage mesuré de la mise en forme."
  "|Les données personnelles doivent être protégées : on limite la diffusion, on évite les détails inutiles et on respecte le RGPD."
  "|Avant l'envoi, une relecture vérifie le destinataire, l'objet, les(pièces jointes, les accords et le ton employé."
  "|Dans les services sociaux, l'écrit engage la structure : il peut être produit en cas de litige et doit donc rester factuel et daté."),
[QC("Quelle information figure dans la ligne d'objet ?", "Le nom du rédacteur~Le sujet précis du message~La date de naissance de l'usager~Le numéro de téléphone", 1,
    "L'objet résume en quelques mots le contenu et l'enjeu du message."),
 QC("Quel élément ne doit pas figurer dans un compte rendu ?", "Les décisions prises~Les échéances~Une anecdote personnelle sans rapport~Les points en attente", 2,
    "Le compte rendu reste factuel : les détails sans lien avec l'objet de la réunion sont écartés."),
 QC("Comment nommer une pièce jointe ?", "doc1.pdf~Demanande_aide_2026_profil.pdf~fichier~new", 1,
    "Un nom explicite permet au destinataire d'identifier le document sans l'ouvrir."),
 QC("Quel réflexe de protection des données s'impose avant un envoi ?", "Joindre tous les dossiers~Vérifier les destinataires et limiter les données transmises~Écrire en majuscules~Supprimer la signature", 1,
    "La vérification des destinataires et la minimisation des données sont des exigences du RGPD."),
 QC("Quelle structure est attendue dans un courrier administratif ?", "Un bloc unique de texte~En-tête, date, objet, corps, politesse, signature~Une liste de questions~Un récit chronologique libre", 1,
    "Le courrier suit une structure codifiée qui facilite son traitement par le destinataire."),
 QC("Quel défaut nuit le plus à un courriel professionnel ?", "Une signature complète~Une absence d'objet et un ton familier~Un paragraphe court~Une pièce jointe annoncée", 1,
    "Sans objet et avec un ton inadapté, le message perd en clarté et en crédibilité."),
 QC("Quand relire un écrit professionnel ?", "Uniquement en cas de plainte~Avant l'envoi systématiquement~Après la réception du destinataire~Jamais, le correcteur suffit", 1,
    "La relecture systématique avant envoi permet de corriger destinataire, pièces jointes et formulation."),
 QT("Rédigez un courriel au directeur d'un centre social pour signaler une difficulté récurrente d'accueil le lundi matin et proposer une réorganisation. Vous respecterez la structure professionnelle.",
    "Objet : Proposition d'aménagement de l'accueil du lundi matin. Monsieur le Directeur, Nous constatons depuis plusieurs semaines que l'accueil du lundi matin connaît une affluence importante dès l'ouverture : les usagers attendent en moyenne vingt minutes avant d'être reçus, et deux rendez-vous de suivi ont dû être reportés en février. Cette situation génère de l'irritation et nuit à la qualité de l'accompagnement. Je propose, pour une période d'essai d'un mois, d'ouvrir un second point d'accueil de 9 h à 11 h les lundis, avec unerépartition des demandes entre les deux postes, et d'afficher un panneau d'information sur les délais. Un point d'étape serait prévu à la fin du mois pour évaluer le temps d'attente et ajuster si nécessaire. Je reste à votre disposition pour préciser les moyens nécessaires et vous transmets en pièce jointe le relevé des attentes observées sur trois lundis. Je vous prie d'agréer, Monsieur le Directeur, l'expression de ma considération distinguée. [Signature complète, fonction, coordonnées.]",
    "On vérifie la présence d'un objet précis, d'une salutation, d'une situation factuelle chiffrée, d'une proposition réaliste, d'une pièce jointe annoncée et d'une formule de politesse."),
 QT("Expliquer pourquoi un compte rendu de réunion doit distinguer les faits, les décisions et les points en attente, et donner un exemple de formulation pour chaque catégorie.",
    "La distinction évite de confondre ce qui a été dit, ce qui a été décidé et ce qui reste ouvert : c'est une exigence de traçabilité et de responsabilité. Les faits relèvent de l'observation : « Mme X a signalé trois demandes de logement non traitées depuis janvier ». Les décisions engagent l'organisation : « Il est décidé d'organiser un point hebdomadaire avec le service logement à compter du 3 mars ; M. Y en assure le pilotage. » Les points en attente ne sont pas des décisions : « La question de la plage horaire d'accueil du samedi reste à examiner après la réponse de la direction des ressources humaines. » Sans cette distinction, un lecteur peut croire qu'une simple suggestion a été adoptée ou qu'une décision est encore discutable. Le compte rendu doit aussi être daté, diffusé aux participants et archivé, car il sert de référence en cas de désaccord ultérieur ; il ne doit pas mentionner d'éléments personnels inutiles, conformément au RGPD.",
    "On attend la justification par la traçabilité, trois formulations distinctes et la mention de l'archivage et de la protection des données.")],
C("Un écrit professionnel clair et factuel facilite la décision et protège la structure comme les usagers.",
  "Objet précis + structure courte + relecture avant envoi",
  "Compte rendu : faits / décisions / points en attente / responsables / échéances",
  "Objet~Sujet du message~Classement|Corps~Paragraphes courts~Lisibilité|Relecture~Contrôle final~Fiabilité",
  "Choisir le destinataire et l'objet|Rédiger un corps structuré|Annoncer les pièces jointes|Vérifier les données personnelles|Relire et envoyer",
  "Omettre l'objet|Écrire un long paragraphe unique|Joindre un dossier complet non trié|Confondre avis personnel et décision",
  "20 minutes~Temps d'attente constaté~Un mois~Période d'essai~Lundi~Jour critique~Samedi~Point à examiner",
  "Fait~Ce qui a été dit~Décision~Ce qui est engageant~Attente~Ce qui reste ouvert",
  "Courriel~Échange rapide~Courrier~Document formel"),
"Programmes d'enseignement général applicables en BTS, référentiel BTS ESF 2022")

# ============================================================ CO5
add("CO5.", "Communication institutionnelle et médias", "Communication", ["BTS2"],
S("La communication institutionnelle est la communication d'une organisation vers ses publics : usagers, partenaires, finanœurs, élus, salariés et grand public."
  "|Elle poursuit des objectifs variés : informer, expliquer une action, renforcer une identité, rassurer en situation de crise ou mobiliser."
  "|Les publics sont hétérogènes : leurs attentes, leurs niveaux d'information et leurs canaux préférés diffèrent."
  "|Un plan de communication définit les objectifs, les cibles, les messages clés, les supports, le calendrier et les indicateurs de suivi."
  "|Les supports peuvent être institutionnels (site, rapport d'activité, plaquette), médiatiques (communiqué de presse, interview) ou numériques (réseaux sociaux, infolettre)."
  "|Le communiqué de presse est court, factual et structuré : un titre, un chapô, les faits, une citation et les coordonnées d'un contact."
  "|Sur les réseaux sociaux, la brièveté et la rapidité augmentent la visibilité mais aussi le risque d'improvisation et de mauvaise interprétation."
  "|La ligne éditoriale définit les thèmes, le ton et les règles de publication d'une organisation pour garantir la cohérence des messages."
  "|En situation de crise, la communication doit être rapide, transparente et coordonnée : le silence laisse le champ libre aux rumeurs."
  "|La protection des données et le droit à l'image imposent une attention particulière à la publication de témoignages ou de photographies d'usagers."
  "|L'efficacité se mesure par des indicateurs : portée des messages, nombre de prises de contact, téléchargements, participation aux actions."
  "|Un service social rend des comptes à ses financeurs et à ses usagers : la communication institutionnelle participe à la transparence de l'action."),
[QC("Quel public n'est pas une cible de la communication institutionnelle d'un centre social ?", "Les usagers~Les partenaires~Les financeurs~Aucun : tous peuvent être concernés", 3,
    "Un centre social communique avec de nombreux publics : usagers, partenaires, institutions, salariés, grand public."),
 QC("Que définit un plan de communication ?", "Le salaire des salariés~Objectifs, cibles, messages, supports et calendrier~Le nombre de réunions~Le budget du chauffage", 1,
    "Le plan de communication organise la démarche et permet d'en suivre les effets."),
 QC("Quel élément ne figure pas dans un communiqué de presse ?", "Un titre et un chapô~Les faits essentiels~Un contact presse~Le relevé intégral des comptes de l'association", 3,
    "Le communiqué est synthétique : il ne contient pas l'intégralité des documents internes."),
 QC("Quel risque majeur des réseaux sociaux ?", "Une portée trop faible~L'improvisation et la mauvaise interprétation~L'absence de public~La lenteur de publication", 1,
    "La rapidité de publication augmente le risque d'erreur et de réception imprévue."),
 QC("Que contient une ligne éditoriale ?", "Les recettes de l'organisation~Les thèmes, le ton et les règles de publication~Les horaires d'ouverture~La liste des salariés", 1,
    "Elle garantit la cohérence des messages et la qualité des publications."),
 QC("Quelle attitude adopter en situation de crise ?", "Attendre la résolution totale~Communiquer rapidement et librement~Se taire~Laisser les rumeurs circuler", 1,
    "Transparence, rapidité et coordination limitent les rumeurs et préservent la confiance."),
 QC("Quel indicateur mesure l'efficacité d'une communication ?", "Le nombre de polices utilisées~La portée et les prises de contact~La longueur du texte~Le nombre de couleurs", 1,
    "Les indicateurs doivent être liés aux objectifs : visibilité, contact, téléchargement, participation."),
 QT("Une rumeur circule sur la fermeture prochaine d'un centre social. Vous êtes chargé de la communication. Définissez les objectifs, les messages et les supports d'une réponse rapide.",
    "Objectifs : démentir ou confirmer rapidement sur la base d'éléments vérifiés, rassurer les usagers et les partenaires, éviter que le vide informationnel ne soit comblé par des versions erronées, préserver la crédibilité de la structure. Messages clés : un état des lieux factuel (« aucune décision de fermeture n'a été prise à ce jour » si tel est le cas), la rappel du calendrier d'information (« le conseil d'administration se réunit le 20 et une information sera diffusée le 21 »), la confirmation de la continuité des services (« les accueils et ateliers maintenus cette semaine ») et un point de contact identifié pour les questions. Supports : un communiqué court envoyé aux partenaires et aux élus, une publication identique sur le site et les réseaux officiels, un affichage à l'accueil et un message oral des professionnels auprès des usagers présents. On évite le déni formulas sans preuve et toute annonce définitive avant décision. Un suivi est prévu : recensement des questions reçues, mise à jour à chaque étape et capitalisation dans le bilan de crise. Les données personnelles des usagers qui s'expriment ne sont pas publiées sans accord.",
    "On attend des objectifs clairs, des messages factuels et datés, une cohérence des supports et un dispositif de suivi."),
 QT("Pourquoi un service social doit-il publier un rapport d'activité et comment le rendre utile à ses différents publics ?",
    "Le rapport d'activité rend des comptes : il justifie l'utilisation des moyens publics ou associatifs, documente les actions réalisées et permet aux partenaires et financiers d'apprécier la pertinence du service. Il contribue aussi à la transparence vis-à-vis des usagers et des habitants. Pour être utile, il doit être lisible par des publics différents : une synthèse en début de document présente les missions, les chiffres clés et les résultats ; des fiches thématiques détaillent chaque action (public accueilli, nombre de personnes, objectifs, résultats, difficultés rencontrées) ; un encadré présente les projets de l'année suivante. Le vocabulaire administratif est limité et les chiffres sont accompagnés d'une explication de leur sens : une hausse du nombre d'accompagnements peut traduire un besoin accru plutôt qu'une amélioration. La diffusion combine version imprimée à l'accueil, version numérique accessible sur le site et présentation orale aux partenaires. Enfin, le rapport ne doit jamais publier de donnée permettant d'identifier un usager sans consentement : la transparence s'arrête là où commence la protection de la vie privée.",
    "La réponse doit lier reddition de comptes, transparence, adaptation aux publics et protection des données.")],
C("La communication institutionnelle construit la confiance : des messages cohérents, adaptés à chaque public et mesurables.",
  "Plan = objectifs + cibles + messages + supports + calendrier + indicateurs",
  "Ligne éditoriale · communiqué de presse · crise : rapidité et transparence · RGPD",
  "Objectif~Résultat attendu~Finalité|Cible~Public visé~Adaptation du message|Indicateur~Mesure de l'effet~Suivi",
  "Définir les objectifs et les publics|Choisir les messages clés| Sélectionner les supports|Établir le calendrier|Mesurer et capitaliser",
  "Improviser en situation de crise|Publier sans vérifier la source|Diffuser une photo d'usager sans accord|Multiplier les messages contradictoires",
  "Communiqué~Texte court pour la presse~Rapport~Reddition de comptes~Réseaux~Visibilité et rapidité~Rumeur~Information non vérifiée",
  "Communication interne~Salariés et équipes~Communication externe~Usagers et partenaires",
  "Portée~Nombre de personnes atteintes~Taux de contact~Mesure de l'effet"),
UP)

# ============================================================ CO6
add("CO6.", "Médiation et gestion des conflits", "Communication", ["BTS2"],
S("Un conflit est une opposition entre deux personnes ou deux groupes dont les intérêts, les besoins ou les représentations divergent."
  "|Dans un service social, le conflit peut opposer usagers et professionnels, usagers entre eux, collègues ou partenaires institutionnels."
  "|La médiation est un processus dans lequel un tiers neutre aide les parties à construire elles-mêmes une solution acceptable."
  "|Le médiateur n'a pas le pouvoir de décider à la place des parties : il facilite l'échange, reformule et vérifie la compréhension."
  "|On distingue les conflits de fait (désaccord sur les événements), de besoin (attentes différentes), de valeur (représentations opposées) et de pouvoir (statut, autorité)."
  "|La médiation ne convient pas à toutes les situations : violence, déséquilibre de pouvoir important ou urgence nécessitent une autre réponse."
  "|Les étapes courantes sont : préparation, exposition des points de vue, identification des intérêts, recherche d'options, accord et suivi."
  "|La distinction entre position et intérêt est centrale : la position est ce que chacun demande, l'intérêt est la raison profonde de cette demande."
  "|Les techniques de désamorçage incluent le calme, la reconnaissance des émotions, la reformulation et le recentrage sur le problème concret."
  "|Une solution durable est une solution que les parties peuvent accepter et appliquer : un accord imposé produit souvent un nouveau conflit."
  "|Le médiateur respecte la confidentialité, sauf danger ou obligation légale, et il explicite les limites de son intervention dès le départ."
  "|Cette compétence s'inscrit dans la fonction de communication professionnelle et de dynamique partenariale du référentiel BTS ESF."),
[QC("Quel est le rôle d'un médiateur ?", "Décider à la place des parties~Aider les parties à construire une solution~Sanctionner le tort~Représenter l'administration", 1,
    "Le médiateur facilite le dialogue sans imposer sa décision."),
 QC("Qu'appelle-t-on conflit de besoin ?", "Un désaccord sur une date~Une divergence d'attentes ou d'intérêts~Une erreur de calcul~Une opposition de vocabulaire", 1,
    "Le conflit de besoin oppose des attentes différentes, par exemple horaires et tranquillité."),
 QC("Quelle situation exclut la médiation ?", "Un désaccord dePlanning~Une violence en cours~Une incompréhension~Un conflit de valeur", 1,
    "En cas de violence ou de déséquilibre grave, la protection prime et une autre intervention est nécessaire."),
 QC("Quel est un intérêt derrière la position « je veux un autre créneau » ?", "Le créneau lui-même~Le besoin de concilier travail et garde d'enfant~Le refus de l'équipe~La couleur de la salle", 1,
    "L'intérêt est la raison profonde : ici, une contrainte de vie à concilier."),
 QC("Quel geste de désamorçage est adapté ?", "Élever le ton~Reconnaître l'émotion et reformuler~Couper la parole~Rappeler le règlement immédiatement", 1,
    "Reconnaître l'émotion et reformuler permet de revenir au problème concret."),
 QC("Quelle condition rend un accord durable ?", "Qu'il soit imposé par la hiérarchie~Qu'il soit acceptable et applicable par les parties~Qu'il soit rédigé en jargon~Qu'il soit secret", 1,
    "Un accord que les parties peuvent réellement appliquer a plus de chances de tenir."),
 QC("Quelle règle déontologique s'impose au médiateur ?", "Publier les propos tenus~Respecter la confidentialité sauf danger ou obligation légale~Prendre parti~Omettre les limites de sa mission", 1,
    "La confidentialité est un principe de la médiation, avec des exceptions légales et de sécurité."),
 QT("Dans un centre social, deux usagers se plaignent l'un de l'autre : l'un occupe régulièrement la salle commune pour ses cours particuliers, l'autre n'a plus de place pour les ateliers collectifs. Menez l'analyse en termes de positions, d'intérêts et de solutions possibles.",
    "Les positions sont explicites : le premier veut continuer à utiliser la salle quand il le souhaite ; le second veut que la salle soit réservée aux ateliers collectifs. Si l'on s'arrête aux positions, le conflit est un jeu de somme nulle. L'entretien individuel permet de dégager les intérêts : le premier a besoin d'un calme et d'un espace stable pour donner des cours rémunérés qui complètent ses revenus ; le second a besoin d'un espace convivial pour retrouver du lien social et animer un atelier avec d'autres habitants. Ces intérêts ne sont pas incompatibles : ils portent sur la qualité de l'usage de l'espace et sur la reconnaissance de chaque activité. Les options possibles incluent un calendrier partagé avec des créneaux dédiés, une salle alternative identifiée pour les cours particuliers, une charte d'usage affichée et une révision mensuelle du planning. Le médiateur soumet ces options aux intéressés, vérifie que chacun peut les appliquer et formalise un accord court avec les horaires et un point de contact. Un suivi à un mois permet d'ajuster. La solution n'est pas de choisir le « bon » usager, mais de rendre l'usage du lieu prévisible et équitable pour les deux.",
    "On attend la distinction positions/intérêts, au moins deux options concrètes, une vérification de l'applicabilité et un suivi."),
 QT("Expliquer pourquoi la médiation est inadaptée en cas de violence ou de déséquilibre de pouvoir important, et indiquer quel autres dispositifs peuvent être mobilisés dans un établissement.",
    "La médiation suppose que les parties puissent s'exprimer librement et que rien ne les empêche de refuser une proposition. En cas de violence, la sécurité physique et psychique prime : la parole de la personne vulnérable peut être contrainte par la peur ou la dépendance, et l'écoute réciproque exposerait à une nouvelle victimisation. De même, un déséquilibre de pouvoir important, par exemple entre un salarié en CDD et sa responsable hiérarchique, rend le consentement suspect : la personne peut accepter un accord par crainte de représailles. Dans ces situations, d'autres dispositifs sont mobilisés : protection immédiate et mise à l'écart de la personne violente, signalement au responsable hiérarchique ou à la direction, recours au service de prévention des risques professionnels, saisi du comité social et économique, accompagnement juridique ou associatif extérieur, et si nécessaire plainte ou signalement à l'autorité administrative. La médiation pourra éventuellement intervenir plus tard, une fois la sécurité rétablie et le déséquilibre réduit, mais elle ne doit jamais servir à éviter une protection nécessaire ou à étouffer une plainte.",
    "La réponse doit expliquer l'exigence de liberté de parole et de consentement, puis citer plusieurs dispositifs de protection et de recours.")],
C("Médier, c'est aider les parties à passer des positions aux intérêts pour construire un accord qu'elles peuvent réellement appliquer.",
  "Position = ce qui est demandé · intérêt = pourquoi c'est demandé",
  "Neutralité · confidentialité · désamorçage · accord applicable · suivi",
  "Position~Revendication affichée~Point de départ|Intérêt~Besin profond~Ce qui compte|Accord~Solution construite~Engagement",
  "Préparer l'entretien et vérifier la sécurité|Écouter chaque point de vue|Identifier les intérêts sous les positions|Proposer des options et les discuter|Formaliser l'accord et prévoir un suivi",
  "Décider à la place des parties|Ignorer la violence ou la pression|Confondre position et intérêt|Négliger le suivi de l'accord",
  "Salle commune~Objet du conflit~Créneaux~Option concrète~Charte~Cadre d'usage~Un mois~Point de suivi",
  "Médiation~Tiers neutre et accord construit~Arbitrage~Décision imposée par un tiers",
  "Conflit de fait~Désaccord sur les faits~Conflit de valeur~Représentations opposées"),
"Fonction de communication professionnelle et de dynamique institutionnelle, référentiel BTS ESF 2022")

# ============================================================ MA1
add("MA1.", "Les fonctions du management : Fayol et Mintzberg", "Management", ["BTS1"],
S("Le management est l'ensemble des actions qui permettent à un groupe de mobiliser ses ressources pour atteindre des objectifs."
  "|Henri Fayol identifie cinq fonctions : prévoir, organiser, commander, coordonner et contrôler."
  "|Prévoir consiste à anticiper les besoins et à fixer des objectifs ; organiser consiste à répartir les tâches, les responsabilités et les moyens."
  "|Commander signifie animer et diriger l'équipe ; coordonner vise à harmoniser les efforts pour éviter les doubles emplois et les contradictions."
  "|Contrôler consiste à comparer les résultats obtenus aux objectifs et à corriger les écarts, sans sanction systématique."
  "|Henry Mintzberg décrit le travail réel du manager à travers trois familles de rôles : interpersonnels, d'information et de décision."
  "|Les rôles interpersonnels comprennent la figure symbolique, le chef et la liaison ; les rôles d'information font du manager un récepteur, un diffuseur et un porte-parole."
  "|Les rôles de décision sont ceux d'entrepreneur, de régulateur des perturbations, de répartiteur de ressources et de négociateur."
  "|Le rôle de figure symbolique implique de représenter l'établissement, recevoir des visiteurs et incarner les valeurs de l'organisation."
  "|Les approches classiques (Fayol) décrivent des fonctions idéales ; les observations de Mintzberg montrent une activité fragmentée, rapide et largement orale."
  "|Dans un service social, le manager doit articuler la mission d'intérêt général, les contraintes budgétaires et l'accompagnement des équipes."
  "|Une bonne pratique consiste à relier chaque fonction à un outil concret : planning pour prévoir, organigramme pour organiser, brief pour animer, indicateurs pour contrôler."),
[QC("Combien de fonctions Fayol attribue-t-il au manager ?", "Quatre~Cinq~Six~Sept", 1,
    "Prévoir, organiser, commander, coordonner et contrôler : cinq fonctions."),
 QC("Quelle fonction correspond à la répartition des tâches et des moyens ?", "Prévoir~Organiser~Contrôler~Négocier", 1,
    "Organiser consiste à répartir les responsabilités, les tâches et les ressources."),
 QC("Dans les rôles de Mintzberg, à quelle famille appartient le porte-parole ?", "Interpersonnelle~D'information~De décision~Technique", 1,
    "Le porte-parole diffuse l'information vers l'extérieur : c'est un rôle d'information."),
 QC("Quel rôle de décision consiste à arbitrer les perturbations imprévues ?", "Entrepreneur~Régulateur des perturbations~Répartiteur~Négociateur", 1,
    "Le régulateur intervient lorsque des événements inattendus désorganisent le service."),
 QC("Que fait le manager lorsqu'il contrôle ?", "Il sanctionne systématiquement~Il compare résultats et objectifs puis corrige~Il rédige le budget~Il recrute", 1,
    "Le contrôle est une comparaison suivie d'actions correctives, pas un verdict automatique."),
 QC("Quelle différence entre les approches de Fayol et de Mintzberg ?", "Fayol décrit des fonctions, Mintzberg des rôles observés~Elles sont identiques~Mintzberg propose cinq fonctions~Fayol étudie le terrain réel", 0,
    "Fayol propose un cadre normatif ; Mintzberg décrit l'activité réelle, fragmentée et orale."),
 QC("Quel outil correspond à la fonction de coordination ?", "Un organigramme seul~Un planning partagé et des réunions de synchronisation~Un logiciel de paie~Une affiche", 1,
    "La coordination s'appuie sur des outils de synchronisation et d'échange entre les acteurs."),
 QT("Un responsable de service social doit préparer l'ouverture d'un nouvel accueil. Montrez comment les cinq fonctions de Fayol s'appliquent concrètement à ce projet.",
    "Prévoir : estimer le nombre d'usagers attendus, définir les horaires, les objectifs d'accueil et le budget nécessaire, en s'appuyant sur les données du territoire. Organiser : répartir les plages de présence entre les agents, désigner un référent pour l'accueil, prévoir la formation, aménager l'espace et les outils (registre, ordinateur, documentation). Commander : expliquer le projet à l'équipe, donner du sens, former aux gestes d'accueil et accompagner la montée en charge. Coordonner : synchroniser avec le service logistique pour le mobilier, avec le service communication pour l'information aux partenaires et avec les associations relais pour les orientations. Contrôler : observer les deux premières semaines, relever le temps d'attente et le nombre de demandes traitées, écouter les retours des agents et des usagers, puis ajuster les plannings et les procédures. Ces fonctions ne se succèdent pas rigidement : le responsable révise sans cesse la prévision à la lumière du contrôle, ce qui illustre le caractère cyclique du management.",
    "On attend une application concrète des cinq fonctions, avec des exemples propres au secteur social et une mention de leur caractère cyclique."),
 QT("Un manager passe sa journée en réunions, appels et interventions imprévues, sans jamais achever son planning. Expliquez cette situation à l'aide des rôles de Mintzberg et proposez une organisation plus efficace.",
    "Cette journée est typique du travail réel décrit par Mintzberg : l'activité du manager est fragmentée, rapide, variée et dominée par l'oral. Les rôles interpersonnels (réception de visiteurs, liaison entre services) et d'information (diffusion, porte-parole) consomment une grande partie du temps ; le rôle de régulateur des perturbations explique les interventions imprévues. Le problème n'est pas l'incompétence mais l'absence de protection des moments de préparation et de synthèse. Pour améliorer, on peut regrouper les rendez-vous en plages horaires, réserver deux créneaux quotidiens au travail préparatoire, déléguer une partie de la diffusion d'information à un référent, utiliser un tableau de bord court pour les indicateurs et instaurer un point d'équipe de quinze minutes plutôt que plusieurs réunions longues. Il faut aussi distinguer les urgences réelles des demandes qui peuvent attendre, et documenter les décisions prises oralement pour éviter de les reprendre. L'objectif n'est pas de supprimer les interactions, elles sont au cœur du rôle, mais de rendre visibles les priorités afin que la prévision et le contrôle ne soient pas toujours sacrifiés.",
    "On attend une mobilisation explicite des rôles de Mintzberg et des mesures organisationnelles concrètes et réalistes.")],
C("Le manager combine des fonctions planifiées (Fayol) et des rôles vécus (Mintzberg) : prévoir, organiser, animer, coordonner, contrôler.",
  "Fayol : prévoir · organiser · commander · coordonner · contrôler",
  "Mintzberg : rôles interpersonnels, d'information, de décision",
  "Prévoir~Anticiper et fixer~Objectifs|Organiser~Répartir~Ressources|Contrôler~Comparer et corriger~Écarts",
  "Fixer un objectif et un indicateur|Répartir les rôles et les moyens|Animer l'équipe par un brief|Coordonner avec les services partenaires|Contrôler les résultats et ajuster",
  "Confondre contrôle et sanction|Négliger la coordination avec les partenaires|Croire que le planning est figé|Oublier le rôle symbolique du manager",
  "Cinq~Fonctions de Fayol~Trois~Familles de rôles~Porte-parole~Rôle d'information~Régulateur~Perturbations",
  "Fayol~Fonctions normatives~Mintzberg~Rôles observés sur le terrain",
  "Commander~Animer l'équipe~Coordonner~Harmoniser les efforts"),
"Programmes d'enseignement professionnel, référentiel BTS ESF 2022")

# ============================================================ MA2
add("MA2.", "Leadership et styles de management", "Management", ["BTS1"],
S("Le leadership est la capacité d'une personne à entraîner l'adhésion et l'engagement d'un groupe autour d'un objectif."
  "|Il se distingue de l'autorité, qui vient de la position hiérarchique et du pouvoir de décision officiel."
  "|Un leader peut ne pas être le responsable hiérarchique : son influence repose sur la compétence, la crédibilité et l'écoute."
  "|Le style autoritaire centralise la décision : il est utile en urgence ou en situation de danger, mais il réduit l'initiative."
  "|Le style participatif associe l'équipe à la réflexion et à la décision : il favorise l'adhésion mais demande du temps."
  "|Le style libéral laisse une large autonomie : il convient à des équipes expérimentées et peut déstabiliser des débutants."
  "|Le management situationnel adapte le style au degré de compétence et d'autonomie de chaque collaborateur et à la nature de la tâche."
  "|La théorie X de McGregor suppose que le salarie évite le travail et doit être contrôlé ; la théorie Y suppose qu'il peut s'autogérer et rechercher des responsabilités."
  "|Le leadership transformationnel cherche à donner du sens et à faire grandir les collaborateurs, au-delà de l'échange salaire-travail."
  "|L'intégrité, la cohérence entre les paroles et les actes, est une condition de la confiance : un leader qui ne respecte pas ses engagements perd sa crédibilité."
  "|Un style efficace n'est pas figé : il évolue avec la maturité de l'équipe, les enjeux du service et le contexte institutionnel."
  "|En action sociale, le leadership s'exerce aussi avec des partenaires externes et des usagers, dans un souci de respect et de co-responsabilité."),
[QC("Quelle est la différence entre leadership et autorité ?", "Aucune~Le leadership repose sur l'influence, l'autorité sur la position~L'autorité est toujours illégale~Le leadership est réservé aux directions", 1,
    "Le leadership vient de l'influence et de l'adhésion, l'autorité du statut hiérarchique."),
 QC("Quel style convient en situation d'urgence ?", "Le style libéral~Le style autoritaire~Le style participatif~Le style absent", 1,
    "En urgence, la centralisation rapide de la décision peut être necessary, à condition d'expliquer ensuite."),
 QC("Quel style associe l'équipe à la décision ?", "Autoritaire~Participatif~Libéral~Hiérarchique strict", 1,
    "Le style participatif implique les membres avant la décision."),
 QC("Que suppose la théorie Y de McGregor ?", "Que le salarié évite le travail~Qu'il peut s'autogérer et aimer son travail~Qu'il faut le surveiller~Qu'il refuse toute responsabilité", 1,
    "La théorie Y fait l'hypothèse d'un salarié autonome et responsable."),
 QC("Quel est un risque du style libéral avec une équipe novice ?", "Une surcharge de décisions~Un manque de repères et d'accompagnement~Une trop grande rapidité~Une autorité excessive", 1,
    "Sans cadre, les collaborateurs peu expérimentés peuvent se sentir abandonnés."),
 QC("Quel facteur entretient la confiance dans le leadership ?", "La distance hiérarchique~La cohérence entre paroles et actes~Le nombre de réunions~La complexité des consignes", 1,
    "L'intégrité et la cohérence sont au fondement de la crédibilité."),
 QC("Quel est un apport du management situationnel ?", "Un style unique pour tous~Une adaptation au niveau d'autonomie de chacun~Une suppression du contrôle~Une hiérarchie plus rigide", 1,
    "Il propose d'ajuster le style à la personne et à la tâche."),
 QT("Un responsable d'équipe souhaite développer l'autonomie de ses agents sans perdre le contrôle des délais. Proposez une démarche progressive en quatre étapes, en mobilisant le management situationnel.",
    "Étape 1 : diagnostic. Le responsable évalue pour chaque agent ses compétences techniques, sa connaissance des procédures et sa capacité à décider ; il identifie aussi les tâches les plus sensibles, par exemple l'accueil des situations d'urgence. Étape 2 : cadrage. Pour les tâches nouvelles ou risquées, il conserve un style directif : consignes précises, critères de qualité explicites et point de contrôle rapproché. En parallèle, il confie à chaque agent une mission délimitée avec un objectif, une échéance et une marge de manœuvre précisée : « tu décides du créneau de passage, tu me préviens si le délai dépasse 24 heures ». Étape 3 : accompagnement. Il passe à un style participatif : avant chaque échéance, il demande à l'agent de proposer sa méthode, il questionne plutôt que de donner la solution, et il organise un retour bref après l'action. Les réussites sont nommées et les erreurs sont analysées comme des apprentissages. Étape 4 : délégation et contrôle allégé. Lorsque la compétence est installée, il réduit la fréquence des points, remplace le contrôle systématique par des indicateurs (délai respecté, nombre de dossiers traités, retours d'usagers) et reste disponible pour les cas complexes. Il précise à chaque étape ce qui change et pourquoi, afin que l'autonomie ne soit pas vécue comme un abandon. Le contrôle ne disparaît pas : il devient un pilotage par les résultats plutôt que par l'activité.",
    "On attend les quatre étapes, une adaptation au niveau d'autonomie, des exemples concrets et un contrôle toujours présent sous forme d'indicateurs."),
 QT("Montrer qu'un même style de leadership peut être utile dans une situation et nuisible dans une autre, en prenant trois exemples de contextes professionnels.",
    "Le style autoritaire est efficace lors d'un déclenchement d'alerte, par exemple une fuite d'eau dans un EHPAD ou un afflux imprévu d'usagers : une décision rapide évite la dispersion. Le même style devient nuisible dans la préparation d'un projet pédagogique, où l'adhésion des animateurs conditionne la qualité de l'action : des consignes imposées produisent une exécution mécanique et peu d'initiatives. Le style participatif est pertinent pour réorganiser un planning d'équipe, car les contraintes de chacun sont mieux prises en compte ; mais il est trop lent face à une situation d'urgence où chaque minute compte et où la responsabilité doit être claire. Le style libéral convient à une équipe de médiateurs expérimentés qui savent gérer seuls des interventions complexes ; il est en revanche délétère pour des agents nouvellement recrutés qui attendent un cadre et une formation. Ces exemples montrent qu'il n'existe pas de meilleur style absolu : la pertinence dépend de l'urgence, de la compétence de l'équipe, de la nature de la tâche et de la culture de l'organisation. Le leader efficace explique aussi pourquoi il change de posture, pour que l'adaptation soit comprise et non vécue comme une incohérence.",
    "La réponse doit donner au moins trois contextes contrasts, montrer l'effet oppose d'un même style et conclure sur l'importance d'expliciter le changement de posture.")],
C("Le leadership est une influence qui s'adapte : autorité, participation ou autonomie selon l'urgence et la maturité de l'équipe.",
  "Leadership = influence + adhésion · autorité = position hiérarchique",
  "Styles : autoritaire · participatif · libéral · situationnel",
  "Autorité~Pouvoir officiel~Hiérarchie|Leadership~Influence et adhésion~Crédibilité|Style situationnel~Adaptation à la personne~Efficacité",
  "Évaluer la compétence et l'autonomie de chaque agent|Choisir la posture adaptée à la tâche|Expliquer le cadre et les objectifs|Accompagner par le questionnement|Alléger le contrôle quand la maîtrise est installée",
  "Confondre leadership et grade|Garder le même style en toutes circonstances|Prendre l'autonomie pour de l'abandon|Ne jamais expliquer un changement de posture",
  "Urgence~Style autoritaire~Projet~Style participatif~Expertise~Style libéral~McGregor~Théories X et Y",
  "Théorie X~Contrôle et surveillance~Théorie Y~Autonomie et responsabilité",
  "Autorité~Statut~Leadership~Influence"),
"Programmes d'enseignement professionnel, référentiel BTS ESF 2022")

# ============================================================ MA3
add("MA3.", "La motivation : Maslow, Herzberg et McGregor", "Management", ["BTS2"],
S("La motivation est la force qui déclenche, oriente et maintient un comportement dans la durée."
  "|La motivation intrinsèque vient de l'activité elle-même : intérêt, sens, plaisir de réussir, autonomie, sentiment d'utilité."
  "|La motivation extrinsèque vient de facteurs externes : salaire, prime, reconnaissance, promotion, avantages, évitement d'une sanction."
  "|Maslow propose une hiérarchie des besoins : physiologiques, de sécurité, d'appartenance, d'estime et d'accomplissement de soi."
  "|Selon Maslow, un besoin de niveau inférieur doit être suffisamment satisfait pour que les niveaux supérieurs deviennent motivateurs."
  "|Le modèle n'est pas strictement séquentiel : un besoin peut rester partiellement satisfait et plusieurs niveaux agissent ensemble."
  "|Herzberg distingue les facteurs d'hygiène (salaire, conditions, relations, politique de l'entreprise) et les facteurs de motivation (réussite, reconnaissance, travail lui-même, responsabilité, croissance)."
  "|Les facteurs d'hygiène évitent l'insatisfaction mais ne créent pas un engagement durable ; les facteurs de motivation produisent l'implication."
  "|McGregor oppose la théorie X, qui postule un salarié paresseux à contrôler, et la théorie Y, qui postule un salarié capable d'autonomie et de créativité."
  "|La reconnaissance est un levier puissant mais elle doit être sincère, précise et proportionnée : une louange vague perd son effet."
  "|La fixation d'objectifs clairs et atteignables, avec un retour régulier, entretient la motivation en rendant les progrès visibles."
  "|Dans le secteur social, le sens de la mission est un moteur important, mais il ne compense pas indéfiniment une surcharge de travail ou un Management deficient."),
[QC("Quel est le dernier niveau de la pyramide de Maslow ?", "La sécurité~L'appartenance~L'estime~L'accomplissement de soi", 3,
    "L'accomplissement de soi occupe le sommet de la hiérarchie des besoins."),
 QC("Quel facteur relève de l'hygiène selon Herzberg ?", "La reconnaissance~Le salaire~La responsabilité~La réussite", 1,
    "Le salaire et les conditions de travail sont des facteurs d'hygiène : leur absence insatisfait sans motiver durablement."),
 QC("Quelle motivation vient de l'activité elle-même ?", "Extrinsèque~Intrinsèque~Financière~Hiérarchique", 1,
    "La motivation intrinsèque naît de l'intérêt, du sens et de l'autonomie dans la tâche."),
 QC("Que suppose la théorie X de McGregor ?", "Que le salarié aime son travail~Qu'il évite le travail et doit être contrôlé~Qu'il est autonome~Qu'il refuse les primes", 1,
    "La théorie X est l'hypothèse pessimiste d'un salarié à surveiller."),
 QC("Quel est un facteur de motivation selon Herzberg ?", "Le nombre de réunions~La reconnaissance du travail accompli~La couleur du bureau~Le règlement intérieur", 1,
    "La reconnaissance, la réussite et la responsabilité sont des facteurs de motivation."),
 QC("Quelle limite de la pyramide de Maslow faut-il connaître ?", "Elle est strictement séquentielle~Plusieurs besoins agissent ensemble~Elle concerne seulement les dirigeants~Elle ignore la rémunération", 1,
    "Les niveaux ne se succèdent pas de façon mécanique : plusieurs besoins coexistent."),
 QC("Pourquoi une reconnaissance vague est-elle peu efficace ?", "Elle coûte trop cher~Elle ne précise pas le comportement valorisé~Elle est interdite~Elle remplace le salaire", 1,
    "Une reconnaissance précise et sincère indique ce qui doit être reproduit."),
 QT("Un service d'accompagnement social connaît un fort turnover et des arrêts de travail répétés. Analyselez cette situation avec Maslow et Herzberg, puis proposez un plan d'action.",
    "Le diagnostic commence par les besoins de base de Maslow : des horaires imprévisibles, une charge de travail excessive et un manque de sécurité dans les interventions peuvent empêcher même les besoins de sécurité d'être satisfaits ; dans ce cas, parler d'accomplissement de soi est illusoire. Le besoin d'appartenance est ensuite interrogé : si les nouveaux agents ne sont pas intégrés, isolés face à des situations difficiles, l'engagement s'effondre. Avec Herzberg, on sépare les deux catégories. Facteurs d'hygiène : rémunération, planning, conditions matérielles, outils, relations avec la hiérarchie, règles de sécurité. Facteurs de motivation : reconnaissance du travail réalisé, sens de l'action auprès des usagers, autonomie dans la conduite des accompagnements, possibilités de formation et d'évolution. Le plan d'action comporte cinq mesures : (1) stabiliser les plannings et respecter les temps de repos, en mesurant le taux d'heures supplémentaires ; (2) organiser un accueil structuré des nouveaux agents avec un tuteur et un référent ; (3) instaurer des temps d'analyse de la pratique pour prévenir l'épuisement ; (4) généraliser une reconnaissance précise, par exemple une mention des réussites en réunion et un entretien de suivi ; (5) ouvrir des perspectives d'évolution avec des formations et des projets confiés. On suivra le turnover, l'absentéisme et un indicateur de climat social sur six mois, en demandant l'avis des agents plutôt qu'en supposant leurs besoins.",
    "On attend une mobilisation distincte des deux modèles, cinq mesures réalistes et des indicateurs de suivi."),
 QT("Un manager affirme : « Pour motiver mon équipe, une prime annuelle suffit. » Discutez cette affirmation en vous appuyant sur les apports de Herzberg et sur la distinction entre motivation intrinsèque et extrinsèque.",
    "L'affirmation est partiellement vraie mais insuffisante. La prime est un facteur extrinsèque : elle agit sur la rémunération, qui est pour Herzberg un facteur d'hygiène. Son absence provoque de l'insatisfaction et son versement peut être apprécié, mais son effet s'estompe rapidement : une fois la prime perçue, la situation redevient normale et n'augmente pas durablement l'engagement. Pour créer une motivation durable, il faut agir sur les facteurs de motivation identifiés par Herzberg : la reconnaissance précise du travail accompli, la responsabilité confiée, la possibilité de progresser, le sens de la mission et la qualité du travail lui-même. Ces éléments relèvent en grande partie de la motivation intrinsèque : l'agent s'engage parce que son activité a du sens, qu'il est reconnu et qu'il peut développer ses compétences. Cela ne signifie pas que le salaire est sans importance : il doit être juste et équitable, sinon il devient un motif de départ. La bonne stratégie combine donc une rémunération correcte, des conditions de travail saines et des leviers intrinsèques : objectifs clairs, feedback régulier, autonomie croissante, formation et participation aux décisions. Le manager doit aussi adapter ses leviers aux personnes : un agent en début de carrière et un agent expérimenté ne sont pas motivés par les mêmes facteurs.",
    "La réponse doit classer la prime parmi les facteurs d'hygiène, expliquer la durée limitée de son effet et proposer des leviers intrinsèques concrets.")],
C("Motiver, c'est agir à la fois sur les conditions (hygiène) et sur le sens, la reconnaissance et l'autonomie (motivation).",
  "Maslow : besoins · Herzberg : hygiène / motivation · McGregor : X / Y",
  "Intrinsèque = de l'activité · extrinsèque = de l'environnement",
  "Hygiène~Évite l'insatisfaction~Salaire, conditions|Motivation~Crée l'engagement~Reconnaissance, sens|Intrinsèque~Vient de soi~Intérêt et autonomie",
  "Mesurer la satisfaction et les besoins de l'équipe|Sécuriser les conditions de travail|Donner du sens et des objectifs clairs|Reconnaître précisément les réussites|Développer autonomie et compétences",
  "Croire qu'une prime suffit|Négliger les besoins de sécurité|Donner une reconnaissance vague|Confondre hygiène et motivation",
  "Pyramide~Cinq niveaux~Herzberg~Deux catégories~Prime~Facteur d'hygiène~Feedback~Reconnaissance",
  "Hygiène~Insatisfaction évitée~Motivation~Engagement créé",
  "Maslow~Hiérarchie des besoins~Herzberg~Contenu du travail"),
"Programmes d'enseignement professionnel, référentiel BTS ESF 2022")

# ============================================================ MA4
add("MA4.", "La conduite de réunion et le briefing d'équipe", "Management", ["BTS1"],
S("Une réunion est un temps de travail collectif organisé pour échanger, décider ou coordonner les actions d'une équipe."
  "|Elle n'est utile que si elle a un objectif explicite : informer, consulter, décider, résoudre un problème ou mobiliser."
  "|Un briefing est une réunion courte et régulière, souvent debout, destinée à synchroniser l'équipe sur les priorités du moment."
  "|La préparation comprend l'ordre du jour, les participants nécessaires, les documents, le lieu, la durée et le rôle de chacun."
  "|L'ordre du jour distingue les points d'information, les points de décision et les questions diverses, en indiquant le temps prévu."
  "|L'animation consiste à faire respecter le temps, à donner la parole, à reformuler et à éviter que quelques personnes monopolisent l'échange."
  "|Un tour de table rapide permet à chaque participant de signaler une difficulté ou une information utile avant la discussion générale."
  "|Les décisions doivent être explicites : qui fait quoi, pour quand, avec quels moyens et selon quel critère de réussite."
  "|Le compte rendu de réunion trace les décisions, les responsables et les échéances ; il est diffusé rapidement aux participants et aux absents."
  "|Une réunion efficace se termine par un récapitulatif à voix haute, ce qui réduit les malentendus sur ce qui a été décidé."
  "|Les réunions trop longues, sans ordre du jour ou sans suite, produisent de la fatigue et une perte de confiance dans le management."
  "|En service social, la réunion d'équipe est aussi un espace de soutien : elle doit préserver la confidentialité des situations d'usagers évoquées."),
[QC("Quel est le premier élément d'une réunion efficace ?", "Un ordre du jour et un objectif clairs~Une longue durée~Un grand nombre de participants~L'absence de compte rendu", 0,
    "Sans objectif ni ordre du jour, la réunion dérive et n'aboutit pas à des décisions."),
 QC("Qu'est-ce qu'un briefing ?", "Une réunion annuelle~Un point court et régulier de synchronisation~Un rapport écrit~Un entretien individuel", 1,
    "Le briefing est court, fréquent et centré sur les priorités immédiates."),
 QC("Dans un ordre du jour, que doit-on distinguer ?", "Les couleurs des diapositives~Les points d'information, de décision et divers~Les noms de famille~Les horaires de transport", 1,
    "La nature des points détermine le mode de traitement et la durée prévue."),
 QC("Quelle phrase relève d'une décision claire ?", "« On verra plus tard »~« Sophie envoie le courrier avant vendredi »~« Il faudrait faire attention »~« Il paraît que c'est compliqué »", 1,
    "Une décision comporte un responsable, une action et une échéance."),
 QC("Pourquoi faire un récapitulatif à la fin de la réunion ?", "Pour remplir le temps restant~Pour vérifier la compréhension des décisions~Pour éviter de rédiger un compte rendu~Pour changer l'ordre du jour", 1,
    "Le récapitulatif verbal permet de corriger immédiatement les malentendus."),
 QC("Quel risque d'une réunion sans suite ?", "Une meilleure autonomie~Une perte de confiance et de la fatigue~Une réduction du temps de travail~Une décision automatique", 1,
    "Sans compte rendu ni application des décisions, les participants cessent de s'impliquer."),
 QC("Quelle précaution s'impose quand des situations d'usagers sont évoquées ?", "Les nommer publiquement~Limiter les informations au nécessaire et respecter la confidentialité~Les photographier~Les transmettre à tous les services", 1,
    "La confidentialité et la minimisation des données s'appliquent aussi en réunion interne."),
 QT("Vous animez la réunion hebdomadaire d'une équipe de six personnes dans un centre social. L'un des participants monopolise la parole, deux autres ne disent rien, et la réunion dépasse régulièrement l'horaire. Proposez une méthode d'animation pour trois réunions successives.",
    "Réunion 1 : je commence par rappeler l'objectif et l'ordre du jour avec un temps prévu par point (10 minutes pour les informations, 15 pour la décision, 5 pour le tour de table). Je préviens que la réunion s'achèvera à l'heure. J'utilise un tour de table avec une consigne courte : « une information, une difficulté, une réussite pour chacun, une minute ». Je remercie le participant bavard après sa contribution et je l'invite à laisser la parole : « merci, je vais maintenant entendre les autres points de vue ». Je sollicite nommément, sans pression, les deux collègues silencieux en leur proposant d'abord un point qu'ils connaissent bien. Je termine par un récapitulatif des décisions avec responsables et échéances. Réunion 2 : je chronomètre réellement chaque séquence et j'affiche le temps restant. Je note les décisions directement dans un tableau visible. Si un point dérive, je propose de le traiter en fin de séance ou en bilatéral avec les personnes concernées. Je demande à un participant différent de faire le compte rendu, pour responsabiliser l'équipe. Réunion 3 : je demande un retour de dix secondes à chacun sur le déroulement : « qu'est-ce qui a été utile, qu'est-ce qui doit changer ? ». J'ajuste la durée du tour de table, je limite les points d'information à ceux qui nécessitent vraiment une parole collective et je diffuse le compte rendu le jour même. Le résultat attendu est une réunion plus courte, où la parole est répartie et où chaque sortie de réunion donne lieu à une action identifiée.",
    "On attend une progression sur trois séances, des techniques d'animation concrètes pour gérer la parole et le temps, et la production d'un compte rendu."),
 QT("Quelle est la différence entre un briefing et un compte rendu de réunion, et comment les articuler dans une journée de service ?",
    "Le briefing est un échange oral, bref et tourné vers l'avenir : il se tient en début de journée ou de vacation, debout, devant l'équipe, pour répartir les priorités, signaler les absences, rappeler les rendez-vous importants et les points de vigilance. Il dure cinq à dix minutes et ne cherche pas à traiter tous les sujets. Le compte rendu est un écrit tourné vers le passé et le suivi : il consigne ce qui a été dit et décidé lors d'une réunion plus longue, avec les responsables, les échéances et les points en attente. Il est diffusé après la séance et sert de trace. Dans une journée type, le briefing du matin s'appuie sur le compte rendu de la veille : le responsable rappelle les trois actions prioritaires issues de la dernière réunion, l'équipe signale les imprévus, puis chacun part avec sa mission. En fin de journée, un court point oral permet de remonter les informations qui alimenteront le prochain compte rendu. L'articulation évite deux écueils : une réunion matinale qui se transforme en long débat, et un compte rendu rédigé trop tard, alors que les décisions sont déjà oubliées. Les deux outils sont complémentaires : l'un synchronise, l'autre trace.",
    "La réponse doit opposer oral/écrit, futur/passé, brièveté/trace, et montrer leur complémentarité dans une journée.")],
C("Une réunion utile a un objectif, un temps, une animation équilibrée et des décisions tracées avec responsables et échéances.",
  "Décision = action + responsable + échéance + critère",
  "Briefing : court, oral, régulier · compte rendu : écrit, factuel, diffusé",
  "Objectif~Finalité de la réunion~Ordre du jour|Décision~Engagement explicite~Suivi|Animation~Gestion de la parole~Équilibre",
  "Préparer l'ordre du jour et les documents|Ouvrir en rappelant l'objectif|Distribuer la parole|Formuler les décisions et les échéances|Diffuser le compte rendu et récapituler",
  "Réunir sans objectif|Laisser un participant monopoliser la parole|Oublier le responsable d'une action|Attendre des jours pour diffuser le compte rendu",
  "Cinq minutes~Durée d'un briefing~Six participants~Taille de l'équipe~Vendredi~Échéance~Tour de table~Outil d'animation",
  "Briefing~Court et oral~Réunion de coordination~Plus longue et décisionnelle",
  "Information~Savoir~Décision~Engager une action"),
"Programmes d'enseignement professionnel, référentiel BTS ESF 2022")

# ============================================================ MA5
add("MA5.", "Délégation, feedback et entretien individuel", "Management", ["BTS2"],
S("Déléguer, c'est confier à une personne une mission avec les moyens et l'autorité nécessaires, tout en restant responsable du résultat."
  "|La délégation ne se limite pas à donner une tâche : elle précise l'objectif, le périmètre, les limites, les ressources et le calendrier."
  "|Un délégataire doit avoir les compétences requises ou bénéficier d'un accompagnement adapté ; sans moyens, la délégation devient un abandon."
  "|Les niveaux de délégation vont de l'exécution stricte à la responsabilité complète du résultat, en passant par la proposition et l'avis consultatif."
  "|Le manager reste redevable envers sa hiérarchie : il ne peut pas transférer sa responsabilité finale, mais il valorise l'autonomie de son collaborateur."
  "|Le feedback est un retour d'information sur un comportement ou un résultat : il peut être positif, correctif ou préventif."
  "|Un feedback utile est précis, factuel, opportun et centré sur le comportement observable plutôt que sur la personnalité."
  "|La méthode dite « situation, comportement, impact, question » structure un retour : décrire le contexte, le geste observé, sa conséquence, puis demander l'avis de la personne."
  "|L'entretien individuel est un temps formalisé d'échange sur la mission, les résultats, les difficultés, les besoins de formation et les perspectives."
  "|Il se prépare : ordre du jour, collecte des faits, indicateurs, points à clarifier et temps d'écoute."
  "|La conclusion de l'entretien doit être synthétisée par écrit avec les engagements de chaque partie et une date de suivi."
  "|Dans le secteur social, l'entretien individuel contribue à prévenir l'épuisement professionnel en donnant un espace légitime aux difficultés du terrain."),
[QC("Que doit contenir une délégation complète ?", "Seulement la tâche~Objectif, périmètre, moyens, limites et échéance~Un ordre oral vague~Le salaire du collaborateur", 1,
    "Une délégation précise le cadre d'action et donne les moyens de réussir."),
 QC("Le manager reste-t-il responsable après délégation ?", "Non, tout est transféré~Oui, il reste redevable du résultat~Oui, mais uniquement financièrement~Non, sauf en cas d'erreur", 1,
    "La responsabilité finale envers la hiérarchie ne se délègue pas."),
 QC("Quel feedback est centré sur le comportement observable ?", "« Tu es négligent »~« Le courrier d'hier ne comportait pas la pièce demandée »~« Tu n'es pas motivé »~« Ton attitude est mauvaise »", 1,
    "Décrire un fait précis évite le jugement de la personne."),
 QC("Que signifie la lettre I dans la méthode situation, comportement, impact, question ?", "Intention~Impact de l'action~Individu~Interdiction", 1,
    "On décrit l'impact concret du comportement avant de demander l'avis de la personne."),
 QC("Quelle est une finalité de l'entretien individuel ?", "Sanctionner systématiquement~Faire le point sur la mission, les difficultés et les perspectives~Remplacer le briefing~Éviter tout écrit", 1,
    "L'entretien individuel est un espace de dialogue et de pilotage, pas seulement de sanction."),
 QC("Quel réflexe avant un entretien individuel ?", "Improviser totalement~Préparer les faits, les indicateurs et l'ordre du jour~Demander à un collègue de le faire~Supprimer le compte rendu", 1,
    "La préparation garantit un échange factuel et respectueux."),
 QC("Quel est un risque d'une délégation sans moyens ?", "Une autonomie réussie~Un abandon déguisé et une culpabilité injuste~Une promotion automatique~Une réduction du contrôle", 1,
    "Sans compétences ni ressources, la personne est mise en échec alors qu'elle n'a pas été accompagnée."),
 QT("Un responsable délègue à une agente chevronnée l'animation d'un atelier budgétaire destiné à dix usagers, avec un objectif de participation et un compte rendu attendu. Rédigez le cadre de délégation en précisant les cinq éléments nécessaires et les points de contrôle.",
    "Cadre proposé. Objectif : animer l'atelier « Comprendre son budget » le 14 mars de 14 h à 16 h, avec pour indicateur au moins huit participants présents et un questionnaire de sortie complété par chacun. Périmètre : l'agente conçoit le déroulé, sélectionne les exercices et anime la séance ; elle peut adapter les exemples au public. Limites : elle ne modifie pas le budget alloué au matériel, ne s'engage pas au nom de l'établissement sur une prise en charge financière et interrompt l'atelier si une donnée personnelle risque d'être divulguée publiquement. Moyens : salle réservée, supports pédagogiques existants, accès à l'imprimante, appui d'un collègue pour l'accueil, et deux heures de préparation comptées dans son planning. Échéances : déroulé transmis le 7 mars, point de préparation le 11 mars, atelier le 14 mars, compte rendu et questionnaires le 17 mars. Points de contrôle : lecture du déroulé par le responsable, observation de la première heure de l'atelier, analyse des questionnaires et court retour oral. À l'issue, le responsable remercie et valorise l'autonomie, puis discute des ajustements pour la prochaine session. Le cadre écrit évite les malentendus sur ce qui était attendu et sécurise l'agente.",
    "On attend les cinq éléments (objectif, périmètre, limites, moyens, échéances) et des points de contrôle proportionnés, pas un contrôle systématique."),
 QT("Comment formuler un feedback correctif à un agent qui a répondu sèchement à une usagère, en utilisant la méthode situation, comportement, impact, question ?",
    "Formulation possible : « Hier matin, vers 9 h 30, à l'accueil (situation), vous avez répondu à Mme D. sans la regarder et en coupant sa phrase, en disant qu'elle devait revenir plus tard (comportement observable). Elle est restée silencieuse et est partie sans poser sa question ; j'ai craint qu'elle renonce à sa démarche et qu'elle se sente jugée (impact). Comment avez-vous vécu ce moment, et que pourrions-nous faire pour que ce type d'échange se passe différemment ? (question) ». La formulation évite « vous avez été grossier », qui juge la personne et déclenche une défense. Elle s'appuie sur un fait daté, décrit un comportement que l'agent peut modifier, expose une conséquence concrète pour l'usager et pour le service, puis ouvre l'échange. La suite consiste à écouter sans interrompre : l'agent était peut-être sous pression, ignorait le contexte de l'usager ou venait de recevoir une information difficile. On convient ensuite d'une action précise, par exemple proposer un siège et reformuler la demande avant de répondre, et on prévoit un point dans une semaine. Le feedback correctif n'est pas une sanction déguisée : il vise à corriger une pratique et à maintenir la qualité de l'accueil, dans le respect de la dignité de l'usager comme de l'agent.",
    "On attend les quatre temps de la méthode, un ton factuel, une écoute de la réaction et un engagement de suivi.")],
C("Déléguer, c'est donner objectif, moyens et limites ; le feedback et l'entretien individuel permettent de piloter sans juger les personnes.",
  "Délégation = mission + autorité + moyens + redevabilité",
  "Feedback : situation · comportement · impact · question",
  "Délégation~Confier avec un cadre~Responsabilité finale conservée|Feedback~Retour factuel~Comportement observable|Entretien~Temps formalisé~Suivi et perspectives",
  "Définir objectif, périmètre, moyens et limites|Vérifier les compétences du délégataire|Fixer les points de contrôle|Formuler un feedback factuel|Synthétiser l'entretien par écrit",
  "Donner une tâche sans moyens|Confondre délégation et abandon|Juger la personne au lieu du comportement|Oublier la date de suivi",
  "14 mars~Date de l'atelier~Huit participants~Indicateur~17 mars~Échéance du compte rendu~9 h 30~Situation précise",
  "Délégation~Autonomie encadrée~Abandon~Aucun moyen donné",
  "Feedback positif~Reconnaître~Feedback correctif~Ajuster une pratique"),
"Programmes d'enseignement professionnel, référentiel BTS ESF 2022")

# ============================================================ MA6
add("MA6.", "Piloter une équipe projet : objectifs et indicateurs", "Management", ["BTS1"],
S("Un projet est une démarche temporaire visant à produire un résultat précis dans un cadre de temps, de coût et de qualité défini."
  "|Piloter une équipe projet consiste à répartir les rôles, planifier les activités, suivre l'avancement et arbitrer les écarts."
  "|Un objectif opérationnel est précis, mesurable, atteignable, pertinent et daté : c'est la logique dite SMART."
  "|Un indicateur est une grandeur observée qui permet de mesurer l'état d'avancement ou le résultat : nombre d'actions réalisées, délai moyen, taux de participation."
  "|On distingue les indicateurs d'activité (ce que l'on fait), de résultat (ce qui est produit) et d'impact (l'effet sur la situation des usagers)."
  "|Un bon indicateur est fiable, disponible à temps, compréhensible et difficile à manipuler ; trop d'indicateurs rendent le pilotage illisible."
  "|Le découpage en lots de travail permet de répartir les responsabilités et de rendre l'avancement visible."
  "|Un échéancier ou planning de Gantt situe les tâches dans le temps et fait apparaître les dépendances entre elles."
  "|Le chemin critique désigne la chaîne de tâches la plus longue : tout retard sur cette chaîne décale la date finale du projet."
  "|Un tableau de bord regroupe les indicateurs essentiels sous forme lisible : il sert à décider, pas à accumuler des données."
  "|Les écarts entre prévu et réalisé donnent lieu à une analyse de cause puis à une action corrective, pas à une recherche de coupable."
  "|Dans un projet social, les indicateurs quantitatifs doivent être complétés par des éléments qualitatifs : retours d'usagers, qualité de l'accompagnement, effets sur l'autonomie."),
[QC("Que signifie la lettre M dans la méthode SMART ?", "Multiple~Mesurable~Manuel~Mensuel", 1,
    "Un objectif SMART est notamment mesurable, ce qui permet de suivre son atteinte."),
 QC("Quel indicateur mesure l'effet sur la situation des usagers ?", "Indicateur d'activité~Indicateur de résultat~Indicateur d'impact~Indicateur de coût", 2,
    "L'indicateur d'impact mesure l'effet obtenu à plus long terme sur la population cible."),
 QC("Qu'est-ce que le chemin critique ?", "La tâche la plus courte~La chaîne de tâches la plus longue~Le budget le plus élevé~La réunion la plus importante", 1,
    "Tout retard sur la chaîne critique décale la fin du projet."),
 QC("À quoi sert un tableau de bord ?", "À accumuler toutes les données~À présenter les indicateurs utiles à la décision~À remplacer le planning~À calculer les salaires", 1,
    "Le tableau de bord est un outil de décision, synthétique et régulièrement mis à jour."),
 QC("Quel défaut nuit à un indicateur ?", "Il est disponible à temps~Il est difficile à mesurer de façon fiable~Il est compris par l'équipe~Il est lié à l'objectif", 1,
    "Un indicateur peu fiable ou ambigu conduit à de mauvaises décisions."),
 QC("Comment réagir à un écart entre prévu et réalisé ?", "Chercher un coupable~Analyser la cause puis corriger le plan~Ignorer l'écart~Augmenter le nombre d'indicateurs", 1,
    "L'écart est une information de pilotage : on cherche la cause puis on ajuste."),
 QC("Pourquoi compléter les chiffres par du qualitatif en projet social ?", "Parce que les chiffres sont faux~Parce que l'effet sur l'autonomie et la qualité échappe au seul comptage~Parce que c'est obligatoire~Parce qu'il faut remplir un rapport", 1,
    "Les indicateurs quantitatifs ne disent pas tout de la qualité de l'accompagnement."),
 QT("Un projet « Accès aux droits » vise à accompagner 60 usagers en six mois. Définissez trois objectifs SMART, les indicateurs associés et la structure d'un tableau de bord mensuel.",
    "Objectifs SMART. (1) Réaliser 60 accompagnements individuels entre le 1er janvier et le 30 juin, soit 10 par mois en moyenne : indicateur d'activité, nombre d'accompagnements réalisés, cible 60. (2) Obtenir un délai moyen inférieur à 15 jours entre la première demande et la première réponse utile, mesuré chaque mois sur les dossiers clos : indicateur de résultat, délai médian, cible inférieur à 15 jours. (3) Atteindre 75 % de personnes déclarant, lors d'un questionnaire court, mieux comprendre la démarche après l'accompagnement : indicateur d'impact perçu, taux de réponses positives, cible 75 % sur au moins 40 réponses. Le tableau de bord mensuel comporte une ligne par indicateur avec la valeur du mois, la valeur cumulée, la cible, l'écart et une tendance sur trois mois ; une rubrique « faits marquants » signale les événements qui expliquent un écart (absence d'un agent, fermeture d'un partenaire, afflux saisonnier) ; une rubrique « actions correctives » indique qui fait quoi avant quelle date ; enfin, une case « voix des usagers » reprend deux ou trois retours anonymisés. Le tableau est présenté en réunion mensuelle, commenté puis archivé. Il reste volontairement court : trop d'indicateurs nuiraient à la lisibilité et détourneraient l'équipe de l'accompagnement lui-même.",
    "On attend trois objectifs avec cible et échéance, des indicateurs de nature différente et un tableau de bord synthétique avec actions correctives."),
 QT("Un retard de trois semaines apparaît sur la tâche « impression des supports », qui précède la formation des bénévoles et la tenue de l'atelier final. Expliquez le raisonnement à tenir et les arbitrages possibles.",
    "Je vérifie d'abord la réalité du retard et sa cause : panne d'imprimante, validation tardive du contenu, absence du responsable ou sous-estimation initiale. Je regarde ensuite si la tâche appartient au chemin critique : puisqu'elle précède directement la formation puis l'atelier, tout retard se répercute sur la date finale sauf si une marge existe. Trois arbitrages sont envisageables. (1) Récupérer du temps sur les tâches suivantes : raccourcir la formation des bénévoles en la concentrant sur une demi-journée, à condition que la qualité reste suffisante. (2) Réduire le périmètre : imprimer moins de supports et prévoir une version numérique projetée, ou reporter à une session ultérieure une partie du public, en informant les partenaires. (3) Ajouter des moyens : faire imprimer par un prestataire externe ou par un partenaire, en vérifiant le coût et le délai réels. Je peux aussi agir en parallèle sur les tâches indépendantes pour gagner du temps ailleurs. Le choix est arbitré avec le commanditaire et l'équipe, en documentant la décision :garder la date finale au prix d'une réduction du nombre de participants ou décaler la date en préservant la qualité. Je préviens immédiatement les usagers et partenaires concernés, car une information tardive nuit davantage à la confiance qu'un report annoncé à temps. Enfin, j'inscris la leçon dans le bilan : le délai d'impression avait été sous-estimé et sera désormais budgété plus largement.",
    "On attend l'analyse de la cause, la notion de chemin critique, au moins deux arbitrages réalistes, l'information des parties prenantes et la capitalisation.")],
C("Piloter un projet, c'est rendre l'avancement visible avec peu d'indicateurs fiables et traiter les écarts comme des informations.",
  "Objectif SMART = précis, mesurable, atteignable, pertinent, daté",
  "Activité · résultat · impact · chemin critique · tableau de bord",
  "Objectif~Cible datée~SMART|Indicateur~Mesure choisie~Activité ou impact|Écart~Prévu moins réalisé~Action corrective",
  "Formuler des objectifs SMART|Choisir peu d'indicateurs fiables|Construire le planning et repérer le chemin critique|Animer le tableau de bord mensuel|Analyser les écarts et décider",
  "Multiplier les indicateurs sans les utiliser|Confondre activité et impact|Attendre la fin du projet pour regarder les écarts|Cacher un retard aux partenaires",
  "60 usagers~Cible d'activité~15 jours~Délai cible~75 %~Impact perçu~Trois semaines~Retard à arbitrer",
  "Indicateur d'activité~Ce qui est fait~Indicateur d'impact~Effet obtenu",
  "Planning~Dates des tâches~Chemin critique~Chaîne la plus longue"),
"Compétence de conduite de projet, référentiel BTS ESF 2022")

# ============================================================ MA7
add("MA7.", "Conduire le changement dans un service social", "Management", ["BTS2"],
S("Le changement est une modification organisationnelle, technique ou humaine qui déplace les habitudes et les repères d'une équipe."
  "|Il peut être subi (fusion, réduction de moyens, évolution réglementaire) ou choisi (nouveau projet, réorganisation, numérisation)."
  "|La résistance au changement n'est pas un obstacle irrationnel : elle exprime des inquiétudes légitimes sur la charge, la compétence, le sens ou la place de chacun."
  "|Les étapes classiques de Lewin sont : dégeler (rendre le changement nécessaire), bouger (expérimenter), geler (installer durablement)."
  "|Le diagnostic doit identifier ce qui change, pourquoi, qui est concerné, quels sont les risques et quelles ressources existent."
  "|La participation des acteurs dès la phase de diagnostic augmente l'adhésion : une décision expliquée est mieux acceptée qu'une décision annoncée."
  "|Un plan de communication annonce les objectifs, le calendrier, les rôles et les réponses apportées aux questions des équipes."
  "|La formation et l'accompagnement permettent d'acquérir les nouveaux gestes ; ils doivent être prévus dans le temps de travail, pas ajoutés à la charge existante."
  "|Les « champions » du changement, salariés volontaires et crédibles, facilitent la diffusion des pratiques auprès de leurs collègues."
  "|Les indicateurs de suivi portent à la fois sur la mise en œuvre (formation réalisée, outils utilisés) et sur l'acceptation (climat, retours, turnover)."
  "|Un changement réussi est évalué après plusieurs mois : l'installation durable demande du temps et des ajustements successifs."
  "|Dans le secteur social, le changement doit préserver la qualité de l'accompagnement et la continuité du service rendu aux usagers."),
[QC("Quel est le premier temps du modèle de Lewin ?", "Bouger~Dégeler~Geler~Évaluer", 1,
    "Dégeler consiste à rendre visible la nécessité du changement et à créer la motivation."),
 QC("Comment interpréter la résistance au changement ?", "Comme une preuve de mauvaise volonté~Comme l'expression d'inquiétudes à entendre~Comme un refus définitif~Comme une faute professionnelle", 1,
    "La résistance révèle des besoins d'information, de formation ou de reconnaissance à traiter."),
 QC("Quel facteur augmente l'adhésion à un changement ?", "Une annonce sans explication~La participation des acteurs au diagnostic~Le silence jusqu'à la mise en œuvre~Une formation imposée hors temps de travail", 1,
    "Associer les équipes en amont permet d'adapter le projet et de le comprendre."),
 QC("Que désigne un « champion » du changement ?", "Un responsable hiérarchique~Un salarié volontaire qui diffuse la nouvelle pratique~Un consultant extérieur~Un usager", 1,
    "Le champion est un relais interne crédible qui accompagne ses collègues."),
 QC("Quel indicateur d'acceptation du changement ?", "Le nombre de réunions tenues~Le climat social et les retours des équipes~Le nombre de courriels envoyés~La taille du bureau", 1,
    "L'acceptation se mesure par des signes qualitatifs et par des données comme le turnover."),
 QC("Quel risque d'une formation ajoutée à la charge de travail habituelle ?", "Elle augmente l'adhésion~Elle est vécue comme une contrainte supplémentaire~Elle supprime les résistances~Elle est obligatoirement efficace", 1,
    "Sans temps dédié, la formation devient une surcharge et produit l'effet inverse."),
 QC("Pourquoi vérifier le changement plusieurs mois après ?", "Parce que l'administration le demande~Parce que l'installation durable demande du temps~Parce que les chiffres sont immédiats~Pour clore le dossier", 1,
    "Le dernier temps de Lewin, geler, suppose de confirmer que la nouvelle pratique tient dans la durée."),
 QT("Une direction décide de numériser le suivi des accompagnements : tablette pour chaque agent, nouvelle application, fin des dossiers papier. Les agents se plaignent d'être débordés et de perdre le contact avec les usagers. Définissez un plan de conduite du changement en cinq actions.",
    "Action 1 : diagnostic et écoute. Organiser des entretiens courts avec les agents et quelques usagers pour comprendre précisément les irritants : temps de saisie, peur de l'erreur, sensation que l'attention se déplace vers l'écran, difficultés avec le matériel. Action 2 : expliciter le pourquoi. Présenter les objectifs réels (traçabilité, sécurité des données, accès partagé aux informations utiles, réduction des doubles saisies) et ce qui ne change pas (le temps d'échange avec l'usager reste prioritaire). Action 3 : former dans le temps de travail. Prévoir trois sessions courtes, un guide d'une page et un binôme de soutien les deux premières semaines ; identifier deux agents volontaires comme relais, sans en faire des responsables hiérarchiques. Action 4 : expérimenter puis ajuster. Tester l'outil sur un service pilote pendant un mois, mesurer le temps de saisie et recueillir les retours, puis corriger les réglages avant généralisation. Action 5 : installer et évaluer. Intégrer les nouvelles pratiques dans les procédures, prévoir un point à un mois, trois mois et six mois, avec des indicateurs d'usage (dossiers renseignés, retards de saisie) et de climat (sentiment de charge, qualité perçue de l'accompagnement). Si le contact avec les usagers se dégrade, on réaffirme une règle simple : l'écran reste fermé pendant l'entretien et la saisie se fait après, avec l'accord de la personne. Le succès se juge à la qualité du service rendu, pas au seul nombre de tablettes distribuées.",
    "On attend cinq actions distinctes couvrant diagnostic, sens, formation, expérimentation et installation, avec des indicateurs et une attention portée aux usagers."),
 QT("Expliquer la formule de Lewin « dégeler, bouger, geler » et montrer pourquoi la dernière étape est souvent négligée à tort.",
    "Dégeler signifie créer les conditions pour que l'ancienne organisation ne paraisse plus évidente : on montre les limites de la situation actuelle, on partage des données, on écoute les difficultés rencontrées et on donne du sens au projet. Sans cette étape, l'équipe reste attachée à ses habitudes et perçoit le changement comme une contrainte arbitraire. Bouger est la phase de transition : on expérimente, on forme, on teste, on se trompe et on corrige ; c'est une période d'incertitude où le soutien de l'encadrement et des pairs est décisif. Geler consiste à rendre la nouvelle pratique stable et durable : mettre à jour les procédures, les documents et les formations, intégrer les nouveaux comportements dans les évaluations et les rituels, vérifier que les anciens réflexes ne reviennent pas. Cette dernière étape est souvent négligée parce que l'attention se relâche une fois le projet lancé et que les indicateurs de fin de chantier donnent l'illusion de la réussite. Or, sans consolidation, les pratiques anciennes reprennent dès que la pression s'absente : la formation initiale est oubliée, les outils sont contournés et le changement reste superficiel. Une évaluation à trois ou six mois, avec des retours d'usagers et d'agents, permet de vérifier que le nouveau fonctionnement est réellement installé et d'ajuster ce qui ne tient pas.",
    "On attend une définition des trois temps, une explication de la négligence fréquente du dernier temps et des mesures de consolidation.")],
C("Conduire le changement, c'est écouter les résistances, expliquer, expérimenter puis installer durablement la nouvelle pratique.",
  "Lewin : dégeler · bouger · geler",
  "Participation · communication · formation dans le temps de travail · relais internes · évaluation à plusieurs mois",
  "Résistance~Inquiétude à entendre~Information à donner|Dégeler~Créer la nécessité~Sens du projet|Geler~Installer durablement~Consolidation",
  "Diagnostiquer les inquiétudes et les besoins|Expliquer les objectifs et ce qui reste stable|Former dans le temps de travail|Expérimenter avec un service pilote|Consolider et évaluer à plusieurs mois",
  "Traiter la résistance comme de la mauvaise volonté|Annoncer sans écouter|Ajouter la formation à la charge existante|Déclarer la réussite dès la fin du déploiement",
  "Tablette~Outil numérique~Dossier papier~Ancienne pratique~Un mois~Durée du test~Six mois~Évaluation finale",
  "Changement subi~Contrainte externe~Changement choisi~Projet porté par l'équipe",
  "Bouger~Expérimenter et ajuster~Geler~Stabiliser les pratiques"),
"Compétence de dynamique institutionnelle, référentiel BTS ESF 2022")

if __name__ == "__main__":
    valider_et_ecrire(F, "btsesf-mat-part-A.json")
