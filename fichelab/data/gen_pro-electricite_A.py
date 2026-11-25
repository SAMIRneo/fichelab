# -*- coding: utf-8 -*-
"""Generateur pro-electricite-mat-part-A.json — lot A : tronc commun (20 fiches).

Français (4), Mathématiques (4), Physique-Chimie (3), Histoire-géographie (3),
Anglais (3), EMC (3). Chaque fiche : 12 points, 9 questions (7 QCM + 2 texte),
7 blocs en ordre strict et 3 schemas. Annees : 2nde pro, 1re pro, Terminale pro.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pro_electricite_common import REF, S, R, QC, QT, C, build, valider_et_ecrire

F = []


def add(prefix, titre, mat, ans, points, questions, c):
    F.append(build(prefix, titre, mat, ans, points, questions, c))


# ============================================================ FR1
add("PE-A01", "Figures de style et argumentation écrite", "Français", ["2nde pro"],
    S("Une figure de style est un procédé de langage qui produit un effet de sens ou de rythme."
      "|La métaphore compare deux réalités sans outil de comparaison explicite."
      "|La comparaison emploie un outil tel que comme, tel, semblable à ou pareil à."
      "|La personnification attribue un trait humain à un objet, un animal ou une idée."
      "|L'hyperbole exagère volontairement une réalité pour renforcer l'expression."
      "|L'euphémisme atténue une réalité brutale pour la rendre plus acceptable."
      "|L'antithèse oppose deux termes ou deux idées dans la même phrase."
      "|L'anaphore répète un mot ou un groupe de mots en début de phrase ou de vers."
      "|Le registre désigne la tonalité d'un texte : courant, soutenu, familier, comique ou tragique."
      "|Un argument est une affirmation appuyée par un exemple, une donnée ou une citation."
      "|Dans un texte argumentatif, la thèse est l'idée défendue et l'antithèse l'idée adverse."
      "|Les connecteurs logiques comme donc, or, mais et car rendent le raisonnement lisible."),
    [QC("Quelle figure compare sans outil de comparaison ?", "La comparaison~La métaphore~L'antithèse~L'anaphore", 1,
        "La métaphore supprime l'outil : elle dit directement qu'une chose est une autre."),
     QC("Quel mot signale habituellement une comparaison ?", "Comme~Sans~Mais~Donc", 0,
        "Comme, tel ou semblable à sont des outils explicites de la comparaison."),
     QC("Quel registre convient à un document administratif ?", "Familier~Soutenu~Courant~Comique", 2,
        "Le registre courant reste neutre et clair, sans tournures familières."),
     QC("Que désigne une anaphore ?", "Une exagération~Une répétition en début de phrase~Une opposition~Une atténuation", 1,
        "L'anaphore répète un élément en tête de phrase ou de vers pour créer un rythme."),
     QC("Quel connecteur introduit une conséquence ?", "Car~Or~Donc~Mais", 2,
        "Donc marque la conséquence ; car marque la cause, or une opposition logique."),
     QC("Qu'appelle-t-on une antithèse ?", "Une atténuation~Une opposition de deux idées~Une comparaison explicite~Une répétition", 1,
        "L'antithèse rapproche deux termes contraires pour faire ressortir le contraste."),
     QC("Sur quoi s'appuie un argument solide ?", "Sur une opinion seule~Sur un exemple ou une donnée~Sur la longueur de la phrase~Sur le titre", 1,
        "Un argument doit être étayé par un fait, un exemple, une donnée ou une citation."),
     QT("Expliquer la différence entre métaphore et comparaison et proposer un exemple de chaque.",
        "La comparaison annonce le rapprochement avec un outil : « ce câble est comme un serpent ». La métaphore supprime cet outil et énonce directement le rapprochement : « ce câble est un serpent ». La première explicite l'image, la seconde la fond dans la phrase et produit un effet plus fort. Les deux reposent sur un trait commun, ici la souplesse et le danger supposé du câble.",
        "On doit montrer que la seule différence est la présence ou l'absence de l'outil de comparaison."),
     QT("Comment repérer la thèse et les arguments dans un texte argumentatif ?",
        "On lit d'abord l'introduction et la conclusion, où la thèse est le plus souvent formulée. On repère ensuite les connecteurs logiques : car, parce que, donc, or, mais. Chaque affirmation suivie d'un exemple, d'une donnée ou d'une citation constitue un argument. On distingue enfin les arguments de l'auteur de ceux de l'adversaire, annoncés par des mots comme mais, pourtant ou en revanche.",
        "On attend la recherche de la thèse dans l'introduction ou la conclusion, puis l'analyse des connecteurs et des preuves.")],
    C("Les figures de style créent des effets de sens, les connecteurs rendent le raisonnement lisible.",
      "Figure = procédé + effet de sens · argument = affirmation + preuve",
      "Métaphore sans outil · comparaison avec comme · anaphore en début de phrase",
      "Métaphore~Compare sans outil~Image directe~Comparaison~Emploie comme~Image annoncée~Anaphore~Répète en début~Effet de rythme",
      "Lire le texte dans son ensemble|Repérer les répétitions et les oppositions|Identifier la figure et son effet|Relever la thèse et les arguments|Rédiger une réponse structurée",
      "Confondre métaphore et comparaison|Prendre une opinion pour un argument|Oublier de citer le texte|Ignorer les connecteurs logiques",
      "Métaphore~Un câble est un serpent|Comparaison~Un câble est comme un serpent|Antithèse~Le courant va et vient",
      "Registre courant~Neutre et clair~Textes administratifs~Peu de figures~Registre soutenu~Vocabulaire recherché~Phrases longues~Ton solennel",
      "Métaphore~Compare sans outil~Image directe~Sans comme~Comparaison~Outil explicite~Emploie comme~Image annoncée"))

# ============================================================ FR2
add("PE-A02", "Le récit et les temps narratifs", "Français", ["2nde pro"],
    S("Un récit rapporte une suite d'événements réels ou imaginaires, organisés selon un ordre choisi."
      "|Le narrateur est celui qui raconte : il peut être un personnage de l'histoire ou rester extérieur."
      "|La focalisation interne adopte le point de vue d'un personnage, la focalisation externe se limite aux apparences."
      "|Le passé simple est le temps du récit littéraire : il marque les actions achevées et successives."
      "|L'imparfait décrit les circonstances, les habitudes et les actions en cours dans le passé."
      "|Le plus-que-parfait exprime une action antérieure à une autre action passée."
      "|Le présent de narration rend une scène passée plus vivante pour le lecteur."
      "|L'ordre chronologique suit l'enchaînement réel des faits, tandis que l'ordre inversé commence par la fin."
      "|Une analepse est un retour en arrière, une prolepse une anticipation."
      "|Le schéma narratif comporte situation initiale, élément perturbateur, péripéties, dénouement et situation finale."
      "|Les temps du récit s'analysent toujours par rapport au moment de l'énonciation et au point de vue choisi."
      "|Savoir identifier ces temps aide à commenter un extrait de texte et à écrire un récit cohérent."),
    [QC("Quel temps est considéré comme le temps du récit littéraire ?", "Le présent~Le passé simple~Le futur~L'impératif", 1,
        "Le passé simple relate des actions achevées qui font avancer l'intrigue."),
     QC("Que décrit principalement l'imparfait ?", "Une action future~Les circonstances et les habitudes passées~Une action antérieure~Un ordre", 1,
        "L'imparfait peint le cadre, les habitudes ou une action en cours dans le passé."),
     QC("Qu'appelle-t-on une analepse ?", "Un retour en arrière~Une anticipation~Une description~Un dialogue", 0,
        "L'analepse interrompt le récit pour raconter un événement antérieur."),
     QC("Quel est le premier élément du schéma narratif ?", "L'élément perturbateur~La situation initiale~Le dénouement~Les péripéties", 1,
        "Le schéma narratif s'ouvre sur la situation initiale avant l'élément perturbateur."),
     QC("Qu'est-ce qu'un narrateur interne ?", "Un narrateur qui est personnage de l'histoire~Un narrateur absent du texte~Un lecteur~Un journal", 0,
        "Le narrateur interne participe à l'action et adopte son propre point de vue."),
     QC("Quel temps exprime une action antérieure à une autre action passée ?", "Le passé simple~L'imparfait~Le plus-que-parfait~Le présent", 2,
        "Le plus-que-parfait situe un fait avant un autre fait passé."),
     QC("À quoi sert le présent de narration ?", "À raconter au futur~À rendre une scène passée plus vivante~À supprimer les personnages~À annoncer la conclusion", 1,
        "Le présent de narration rapproche le lecteur de l'action, même si elle est passée."),
     QT("Expliquer l'emploi conjoint du passé simple et de l'imparfait dans un récit.",
        "Le passé simple exprime les actions ponctuelles, achevées et successives qui constituent les événements de l'intrigue. L'imparfait exprime le cadre, les descriptions, les habitudes et les actions en cours. Le passé simple fait donc avancer l'action, tandis que l'imparfait l'enveloppe et la rend crédible. Dans une phrase comme « il pleuvait quand le facteur arriva », l'imparfait peint la circonstance et le passé simple marque l'événement qui la brise.",
        "On attend l'opposition entre actions achevées au passé simple et contexte décrit à l'imparfait."),
     QT("Décrire le schéma narratif d'un court récit et son effet sur le lecteur.",
        "Le récit commence par une situation initiale qui présente le lieu, les personnages et un équilibre. Un élément perturbateur rompt cet équilibre et déclenche l'action. Les péripéties multiplient les obstacles et les tentatives. Le dénouement résout le conflit, puis la situation finale rétablit ou transforme l'équilibre initial. Cette structure crée une attente, maintient la tension et donne au lecteur le sentiment d'une progression aboutie.",
        "La réponse doit citer les cinq éléments du schéma et expliquer l'effet de tension et de résolution.")],
    C("Le récit alterne temps du cadre et temps de l'action pour construire une progression lisible.",
      "Passé simple = événement achevé · imparfait = cadre et habitude",
      "Plus-que-parfait = antériorité · présent de narration = effet de présence",
      "Passé simple~Action achevée~Fait avancer l'action~Imparfait~Cadre et habitude~Dpeint le passé~Plus-que-parfait~Action antérieure~Situe dans le passé",
      "Repérer le narrateur et son point de vue|Identifier les temps employés|Distinguer cadre et événements|Relever les ruptures dans l'ordre|Expliquer l'effet produit",
      "Confondre passé simple et imparfait|Oublier le moment de l'énonciation|Prendre le narrateur pour l'auteur|Négliger les indices de focalisation",
      "Il pleuvait~Le facteur arriva~Habitude~Il allait chaque matin~Antériorité~Il avait fermé la porte",
      "Récit linéaire~Ordre chronologique~Lecture facile~Récit inversé~Commence par la fin~Suspense renforcé~Analepse~Retour en arrière",
      "Narrateur interne~Personnage de l'histoire~Point de vue limité~Narrateur externe~Étranger à l'action~Vue d'ensemble"))

# ============================================================ FR3
add("PE-A03", "Poésie : rythme, images et lecture d'un poème", "Français", ["1re pro"],
    S("Un poème est un texte où le sens s'appuie sur le rythme, les sonorités et les images."
      "|Le vers est une ligne de poème, dont la longueur se compte en syllabes."
      "|L'alexandrin compte douze syllabes, l'octosyllabe huit et le décasyllabe dix."
      "|La césure est une coupure à l'intérieur du vers, souvent après la sixième syllabe pour l'alexandrin."
      "|La rime est une répétition de sonorités à la fin de deux vers ; les rimes peuvent être croisées ou embrassées."
      "|Le strophe est un groupe de vers ; le sonnet en comporte deux quatrains et deux tercets."
      "|Le rythme naît de la place des accents, des coupes et de la longueur des vers."
      "|Les images poétiques associent des réalités proches ou lointaines pour produire un effet sensible."
      "|Le champ lexical regroupe les mots qui relèvent d'une même idée ou d'un même thème."
      "|L'énonciation poétique précise qui parle, à qui et dans quelle situation."
      "|Lire un poème consiste à observer la forme avant de proposer une interprétation du sens."
      "|Un commentaire doit toujours appuyer l'interprétation sur des éléments précis du texte."),
    [QC("Combien de syllabes compte un alexandrin ?", "Huit~Dix~Douze~Quatorze", 2,
        "L'alexandrin est un vers de douze syllabes, avec une césure le plus souvent à la sixième."),
     QC("Comment appelle-t-on une coupure à l'intérieur d'un vers ?", "Une rime~Une césure~Une strophe~Une analepse", 1,
        "La césure partage le vers en deux hémistiches et organise le rythme."),
     QC("Que sont des rimes croisées ?", "ABAB~AABB~ABBA~AAAA", 0,
        "Les rimes croisées alternent les sonorités : rime A, rime B, rime A, rime B."),
     QC("Combien de quatrains contient un sonnet ?", "Un~Deux~Trois~Quatre", 1,
        "Le sonnet se compose de deux quatrains puis de deux tercets."),
     QC("Quel est un vers de huit syllabes ?", "L'alexandrin~Le décasyllabe~L'octosyllabe~L'hexasyllabe", 2,
        "L'octosyllabe compte huit syllabes ; le décasyllabe en compte dix."),
     QC("Qu'appelle-t-on champ lexical ?", "L'ensemble des mots d'une même langue~L'ensemble des mots liés à un même thème~La liste des rimes~Le titre du poème", 1,
        "Le champ lexical regroupe les mots qui relèvent d'une même idée ou d'un même domaine."),
     QC("Dans quel ordre procéder pour lire un poème ?", "Interpréter puis observer la forme~Observer la forme puis interpréter~Lire seulement le titre~Ignorer le rythme", 1,
        "On relève d'abord les faits de langue et de versification, puis on construit une interprétation."),
     QT("Expliquer comment le rythme participe au sens d'un poème.",
        "Le rythme vient de la longueur des vers, de la place des accents et des césures. Un vers court et heurté peut traduire l'urgence ou la rupture, tandis qu'un alexandrin régulier donne une impression d'équilibre et de continuité. Les répétitions et les rimes créent des échos qui mettent en valeur certains mots. Le rythme ne décore pas seulement le texte : il oriente l'émotion et renforce le thème traité.",
        "On attend le lien entre les faits de versification et l'effet de sens produit."),
     QT("Décrire la démarche de commentaire d'un poème en quatre étapes.",
        "On lit le poème plusieurs fois, puis on repère sa forme : type de vers, rimes, strophes et rythme. On relève ensuite les champs lexicaux et les images, en notant les mots qui reviennent. On identifie le thème, le locuteur et la situation d'énonciation. Enfin, on formule une interprétation appuyée sur des citations précises, en expliquant comment la forme sert le sens.",
        "La réponse doit proposer lecture, analyse formelle, relevé lexical et interprétation citée.")],
    C("Dans un poème, la forme elle-même produit du sens : rythme, rimes et images se commentent ensemble.",
      "Alexandrin = 12 syllabes · octosyllabe = 8 · décasyllabe = 10",
      "Césure = coupure interne · rime = écho sonore · sonnet = 2 quatrains + 2 tercets",
      "Alexandrin~Douze syllabes~Vers classique~Octosyllabe~Huit syllabes~Vers court~Césure~Coupure interne~Effet de rythme",
      "Lire le poème à voix haute|Compter les syllabes et repérer les rimes|Relever les images et les champs lexicaux|Identifier le locuteur et le thème|Formuler une interprétation citée",
      "Compter les mots au lieu des syllabes|Ignorer la ponctuation|Interpréter sans citer|Oublier la situation d'énonciation",
      "Alexandrin~12 syllabes~Rime croisée~ABAB~Rime embrassée~ABBA~Sonnet~2 quatrains et 2 tercets",
      "Vers court~Rythme vif~Effet d'urgence~Vers long~Rythme posé~Effet de continuité~Régularité~Équilibre du poème",
      "Rimes croisées~ABAB~Alternance des sons~Rimes embrassées~ABBA~Sonorités enveloppées"))

# ============================================================ FR4
add("PE-A04", "L'oral : prise de parole et débat argumenté", "Français", ["1re pro"],
    S("La prise de parole orale mobilise la voix, le regard, la posture et une organisation claire des idées."
      "|Une introduction orale annonce le sujet et le plan sans recapituler toute la présentation."
      "|Un plan oral s'annonce avec des connecteurs simples : d'abord, ensuite, enfin."
      "|Les repères visuels doivent rester brefs : un mot ou une expression par diapositive ou par carte."
      "|Le débit doit être régulier, ni trop rapide ni trop lent, avec des pauses aux moments importants."
      "|Les silences donnent du poids à une idée et permettent à l'auditoire de suivre."
      "|Un débat argumenté oppose deux positions, chacune défendue par des arguments et des exemples."
      "|Pour réfuter un adversaire, on reprend son argument avant d'en montrer la limite."
      "|Les questions de l'auditoire permettent de préciser une position et de tester sa solidité."
      "|La reformulation est une technique utile : elle redit brièvement ce que l'autre a avancé."
      "|L'évaluation de l'oral porte autant sur la forme que sur la qualité des arguments."
      "|En bac professionnel, l'oral porte sur des situations concrètes et sur la capacité à justifier un choix."),
    [QC("Que doit contenir une introduction orale ?", "Tout le contenu du exposé~Le sujet et l'annonce du plan~La conclusion seule~Une liste de chiffres", 1,
        "L'introduction situe le sujet et annonce brièvement les étapes de la parole."),
     QC("Quel connecteur annonce une première étape ?", "Enfin~Ensuite~D'abord~Pourtant", 2,
        "D'abord ouvre le plan ; ensuite poursuit et enfin clôt."),
     QC("Combien de mots faut-il mettre sur un repère visuel ?", "Un paragraphe~Un mot ou une expression courte~Une page entière~Autant que possible", 1,
        "Un repère visuel doit rester synthétique pour être lu d'un coup d'œil."),
     QC("À quoi sert une pause dans une présentation ?", "À masquer un oubli~À donner du poids à une idée~À terminer plus vite~À changer de sujet", 1,
        "Le silence met en valeur ce qui vient d'être dit et aide l'auditoire à suivre."),
     QC("Comment réfuter un argument adverse ?", "En l'ignorant~En le reprenant puis en montrant sa limite~En haussant le ton~En changeant de sujet", 1,
        "La réfutation reprend l'argument de l'adversaire avant d'en discuter la portée."),
     QC("Qu'appelle-t-on reformulation ?", "Une répétition sans but~Le fait de redire brièvement l'idée de l'autre~Une conclusion~Une question piège", 1,
        "La reformulation montre que l'on a écouté et clarifie le désaccord."),
     QC("Sur quoi porte l'évaluation d'un oral ?", "Sur la seule voix~Sur la forme et sur les arguments~Sur le nombre de diapositives~Sur la durée de silence", 1,
        "On évalue la clarté, la voix, la posture et la solidité des arguments."),
     QT("Comment construire une intervention orale de trois minutes sur un sujet professionnel ?",
        "On prépare une introduction courte qui présente le sujet et les deux ou trois étapes annoncées. On développe chaque étape avec une idée principale et un exemple concret issu du métier. Les repères écrits restent réduits à quelques mots. On surveille le débit, on marque des pauses et on regarde l'auditoire. On conclut en récapitulant la réponse apportée au questionnement initial, sans introduire d'idée nouvelle.",
        "On attend introduction, annonce du plan, idées et exemples, gestion de la voix, conclusion."),
     QT("Expliquer comment réagir à une question critique pendant un débat.",
        "On écoute jusqu'au bout sans interrompre, puis on reformule la question pour vérifier sa compréhension. On distingue la question portant sur un fait de celle portant sur une opinion. On répond par un argument précis, appuyé sur un exemple ou une donnée. Si l'on ne sait pas, on le dit clairement et on propose de vérifier. On reste calme : le ton et la posture comptent autant que le contenu dans la crédibilité de la réponse.",
        "La réponse doit mentionner écoute, reformulation, argument étayé, honnêteté et maîtrise du ton.")],
    C("Un bon oral combine une structure simple, une voix maîtrisée et des arguments étayés.",
      "Parole claire = introduction + étapes annoncées + conclusion",
      "Rythme · pauses · regard · reformulation · réfutation",
      "Introduction~Annonce du sujet~Annonce du plan~Développement~Une idée par étape~Un exemple concret~Conclusion~Récapitulatif~Pas d'idée nouvelle",
      "Choisir une question précise|Préparer deux ou trois idées|Rédiger des repères très brefs|Répéter à voix haute|Gérer pauses et regard",
      "Lire intégralement ses notes|Parler trop vite|Ignorer les questions|Réfuter sans écouter",
      "D'abord~Première étape~Sujet posé~Ensuite~Deuxième étape~Exemple métier~Enfin~Conclusion~Bilan",
      "Débit rapide~Idées qui se télescopent~Auditoire perdu~Débit posé~Pauses marquées~Idées mises en valeur~Silence~Effet d'emphase",
      "Réformuler~Redire l'idée entendue~Vérifier la compréhension~Réfuter~Reprendre et discuter~Montrer la limite"))

# ============================================================ MA1
add("PE-A05", "Fonctions affines et linéaires", "Mathématiques", ["2nde pro"],
    S("Une fonction affine associe à un nombre x le nombre ax + b, avec a et b deux réels donnés."
      "|Le coefficient a est le coefficient directeur : il donne la variation de la fonction."
      "|Si a est positif, la fonction est croissante ; si a est négatif, elle est décroissante."
      "|Si a vaut zéro, la fonction est constante et égale à b."
      "|Une fonction linéaire est une fonction affine dont le terme constant b est nul."
      "|La représentation graphique d'une fonction affine est une droite."
      "|Le coefficient directeur se calcule entre deux points par le quotient des différences de ordonnées et d'abscisses."
      "|L'ordonnée à l'origine correspond au point de la droite dont l'abscisse vaut zéro."
      "|Une fonction est croissante quand x augmente et que f(x) augmente en même temps."
      "|Résoudre f(x) = k revient à chercher les abscisses des points de la droite d'ordonnée k."
      "|Résoudre f(x) > k revient à lire la portion de droite située au-dessus de la droite d'équation y = k."
      "|Ces notions servent à modéliser des dépenses, des conversions et des variations linéaires en électrotechnique."),
    [QC("Quelle est l'image de 3 par la fonction f(x) = 2x + 1 ?", "5~6~7~9", 2,
        "On calcule 2 × 3 + 1 = 7."),
     QC("Que représente le coefficient a dans f(x) = ax + b ?", "L'ordonnée à l'origine~La pente de la droite~L'abscisse du point~La valeur de x", 1,
        "Le coefficient directeur a donne la pente et le sens de variation."),
     QC("Quand une fonction affine est-elle décroissante ?", "Quand a est positif~Quand a est négatif~Quand b est nul~Quand b est positif", 1,
        "Un coefficient directeur négatif rend la fonction décroissante."),
     QC("Qu'appelle-t-on fonction linéaire ?", "Une fonction sans graphique~Une fonction affine avec b = 0~Une fonction constante non nulle~Une fonction à deux variables", 1,
        "La fonction linéaire est de la forme f(x) = ax : elle passe par l'origine."),
     QC("Quelle est la représentation graphique d'une fonction affine ?", "Une parabole~Une droite~Un cercle~Une exponentielle", 1,
        "Toute fonction affine se représente par une droite."),
     QC("Comment calculer le coefficient directeur entre deux points ?", "Par le produit des abscisses~Par le quotient des différences d'ordonnées et d'abscisses~Par la somme des ordonnées~Par la moyenne des abscisses", 1,
        "On calcule a = (y2 - y1) / (x2 - x1)."),
     QC("Que donne l'ordonnée à l'origine b ?", "Le point d'abscisse 1~Le point d'abscisse 0~La pente~Le maximum", 1,
        "b est l'ordonnée du point où la droite coupe l'axe des ordonnées."),
     QT("Étudier la fonction f(x) = -2x + 6 : sens de variation, ordonnée à l'origine et point d'abscisse 2.",
        "Le coefficient directeur vaut -2, donc la fonction est décroissante : quand x augmente de 1, f(x) diminue de 2. L'ordonnée à l'origine est 6, ce qui signifie que la droite passe par le point de coordonnées (0 ; 6). Pour x = 2, on obtient f(2) = -2 × 2 + 6 = 2, donc le point (2 ; 2) appartient à la droite. Le graphique est une droite descendante qui coupe l'axe des abscisses en x = 3.",
        "On attend le signe de a, la lecture de b et le calcul de l'image demandée."),
     QT("Un abonnement coûte 12 € par mois plus 30 € de frais de dossier. Modéliser et calculer le coût de 5 mois.",
        "On pose f(x) = 12x + 30, où x désigne le nombre de mois. Le coefficient 12 correspond au coût mensuel et la constante 30 aux frais fixes. Pour 5 mois, on calcule f(5) = 12 × 5 + 30 = 90 €. La fonction est croissante car le coefficient directeur est positif : chaque mois supplémentaire ajoute 12 € au total. Le graphique est une droite qui ne passe pas par l'origine puisque b vaut 30.",
        "La réponse doit donner l'expression de la fonction affine, le calcul et l'interprétation des coefficients.")],
    C("Une fonction affine se lit sur une droite : le coefficient donne la pente, la constante donne le départ.",
      "f(x) = ax + b · a = coefficient directeur · b = ordonnée à l'origine",
      "a > 0 : croissante · a < 0 : décroissante · b = 0 : fonction linéaire",
      "Coefficient a~Donne la pente~Sens de variation~Constante b~Ordonnée à l'origine~Point (0;b)~Fonction linéaire~Forme ax~Passe par l'origine",
      "Repérer a et b dans l'expression|Calculer deux images|Tracer la droite à la règle|Lire le sens de variation|Résoudre une équation ou une inéquation",
      "Confondre a et b|Oublier le signe négatif|Tracer une courbe au lieu d'une droite|Lire l'abscisse à la place de l'ordonnée",
      "f(x)=2x+1~a=2 et b=1~Droite montante~f(x)=-x+4~a=-1~Droite descendante~f(3)~7~, Calcul direct~2 × 3 + 1",
      "Fonction affine~Forme ax + b~Droite décalée~Passe par (0;b)~Fonction linéaire~Forme ax~Passe par l'origine~Constante nulle",
      "a positif~Fonction croissante~Droite montante~a négatif~Fonction décroissante~Droite descendante"))

# ============================================================ MA2
add("PE-A06", "Équations, inéquations et systèmes", "Mathématiques", ["2nde pro"],
    S("Une équation est une égalité qui n'est vraie que pour certaines valeurs de l'inconnue."
      "|Résoudre une équation consiste à trouver toutes les valeurs qui rendent l'égalité vraie."
      "|On conserve les solutions en appliquant la même opération aux deux membres de l'égalité."
      "|Une équation du premier degré s'écrit ax + b = 0, avec a non nul."
      "|Sa solution est x = -b / a, obtenue en isolant l'inconnue."
      "|Une inéquation du premier degré s'écrit ax + b > 0 ou ax + b < 0."
      "|Quand on multiplie ou divise une inéquation par un nombre négatif, on inverse le sens de l'inégalité."
      "|L'ensemble des solutions d'une inéquation du premier degré est un intervalle."
      "|Un système de deux équations à deux inconnues se résout par substitution ou par combinaison."
      "|La substitution consiste à exprimer une inconnée en fonction de l'autre puis à remplacer."
      "|La combinaison additionne les équations après les avoir multipliées pour éliminer une inconnue."
      "|Ces outils servent à dimensionner des circuits et à résoudre des équilibres de puissances."),
    [QC("Quelle est la solution de 3x + 6 = 0 ?", "x = 2~x = -2~x = 6~x = -6", 1,
        "On isole x : 3x = -6, donc x = -2."),
     QC("Que faut-il faire quand on divise une inéquation par un nombre négatif ?", "Rien~Inverser le sens de l'inégalité~Changer l'inconnue~Ajouter un terme", 1,
        "Le sens de l'inégalité s'inverse lors d'une multiplication ou division par un nombre négatif."),
     QC("Quel est l'ensemble des solutions d'une inéquation du premier degré ?", "Un nombre isolé~Un intervalle~Une droite~Une parabole", 1,
        "Les solutions forment un intervalle de la droite des réels."),
     QC("Comment appelle-t-on la méthode qui isole une inconnue avant de la remplacer ?", "La combinaison~La substitution~La factorisation~La dérivation", 1,
        "La substitution exprime une inconnue en fonction de l'autre, puis remplace dans l'autre équation."),
     QC("Que faut-il faire aux deux membres d'une équation pour garder l'égalité ?", "Ajouter un nombre différent~Appliquer la même opération~Les multiplier par zéro~Les supprimer", 1,
        "Toute opération effectuée sur un membre doit l'être sur l'autre."),
     QC("Quand une équation du premier degré admet-elle une solution unique ?", "Quand a = 0~Quand a est non nul~Quand b = 0~Quand x = 0", 1,
        "Si a n'est pas nul, on peut diviser par a et obtenir x = -b/a."),
     QC("Quelle opération élimine une inconnue dans un système par combinaison ?", "Additionner après mise au même coefficient~Multiplier par zéro~Soustraire b~Diviser par x", 0,
        "On rend les coefficients opposés puis on additionne les deux équations."),
     QT("Résoudre l'inéquation -2x + 4 > 0 et interpréter le résultat sur la droite des réels.",
        "On soustrait 4 des deux membres : -2x > -4. On divise ensuite par -2, ce qui inverse le sens de l'inégalité : x < 2. L'ensemble des solutions est donc l'intervalle ouvert ]-1 ; 2[ borné en haut par 2, exclu puisque l'inégalité est stricte. Sur la droite des réels, on place un cercle creux en 2 et on colore toute la partie située à gauche. On vérifie avec x = 0 : -2 × 0 + 4 = 4 > 0, ce qui confirme le résultat.",
        "On attend l'inversion du sens lors de la division par un nombre négatif et un intervalle ouvert."),
     QT("Résoudre le système x + y = 10 et x - y = 2, puis interpréter la solution.",
        "Par combinaison, on additionne les deux équations : 2x = 12, donc x = 6. En remplaçant dans la première équation, on obtient 6 + y = 10, soit y = 4. La solution du système est le couple (6 ; 4). Par substitution, on aurait écrit y = 10 - x puis x - (10 - x) = 2, soit 2x = 12. Le couple vérifie les deux équations : 6 + 4 = 10 et 6 - 4 = 2.",
        "La réponse doit donner le couple solution et vérifier qu'il satisfait les deux équations.")],
    C("Résoudre une équation ou une inéquation, c'est conserver l'équivalence à chaque étape.",
      "ax + b = 0 donne x = -b/a · ax + b > 0 donne un intervalle",
      "Inverser le sens si l'on multiplie ou divise par un nombre négatif",
      "Équation~Égalité conditionnelle~Solution isolée~Inéquation~Comparaison~Intervalle de solutions~Système~Deux inconnues~Couple solution",
      "Lire le type d'énoncé|Isoler le terme contenant x|Diviser par le coefficient|Inverser le sens si nécessaire|Vérifier la solution trouvée",
      "Oublier d'inverser le sens|Diviser par zéro|Perdre une solution en simplifiant|Ne pas vérifier le couple solution",
      "3x+6=0~x=-2~-2x+4>0~x<2~Système~Couple (6;4)~Vérification~6+4=10",
      "Équation~Une ou plusieurs valeurs~Solutions discrètes~Inéquation~Un intervalle~Solutions continues~Système~Couple solution",
      "Substitution~Exprimer puis remplacer~Une inconnue isolée~Combinaison~Additionner après alignement~Élimination directe"))

# ============================================================ MA3
add("PE-A07", "Vecteurs et trigonométrie dans le plan", "Mathématiques", ["1re pro"],
    S("Un vecteur du plan possède une direction, un sens et une norme, mais pas de point d'application fixé."
      "|Le vecteur AB a pour composantes (xB - xA ; yB - yA) dans un repère orthonormé."
      "|La norme d'un vecteur de composantes (x ; y) vaut la racine carrée de x² + y²."
      "|Le produit scalaire de deux vecteurs permet de calculer l'angle entre leurs directions."
      "|Deux vecteurs sont orthogonaux si leur produit scalaire est nul."
      "|Dans un triangle rectangle, le cosinus d'un angle est le quotient du côté adjacent sur l'hypoténuse."
      "|Le sinus est le quotient du côté opposé sur l'hypoténuse, et la tangente le quotient du opposé sur l'adjacent."
      "|La relation sin² + cos² = 1 permet de passer d'une fonction trigonométrique à l'autre."
      "|Les angles peuvent se mesurer en degrés ou en radians, avec 180 degrés pour π radians."
      "|La décomposition d'une force suit les mêmes règles que celle d'un vecteur."
      "|En courant alternatif, une grandeur sinusoïdale s'écrit avec un amplitude, une pulsation et une phase."
      "|La phase exprime le décalage entre deux grandeurs sinusoïdales de même fréquence."),
    [QC("Quelles sont les composantes du vecteur AB ?", "(xA - xB ; yA - yB)~(xB - xA ; yB - yA)~(xA + xB ; yA + yB)~(xB ; yB)", 1,
        "On retranche les coordonnées du point de départ de celles du point d'arrivée."),
     QC("Quelle est la norme du vecteur (3 ; 4) ?", "5~7~12~25", 0,
        "La norme vaut la racine de 3² + 4², soit la racine de 25, donc 5."),
     QC("Quand deux vecteurs sont-ils orthogonaux ?", "Quand leur norme est égale~Quand leur produit scalaire est nul~Quand ils ont la même direction~Quand leur somme est nulle", 1,
        "Un produit scalaire nul signifie un angle de 90 degrés entre les vecteurs."),
     QC("Dans un triangle rectangle, que vaut le cosinus d'un angle aigu ?", "Opposé sur hypoténuse~Adjacent sur hypoténuse~Opposé sur adjacent~Hypoténuse sur adjacent", 1,
        "Le cosinus est le rapport du côté adjacent à l'hypoténuse."),
     QC("Quelle relation relie sinus et cosinus d'un même angle ?", "sin + cos = 1~sin² + cos² = 1~sin × cos = 1~sin - cos = 1", 1,
        "L'identité sin² + cos² = 1 découle du théorème de Pythagore."),
     QC("Combien de degrés valent π radians ?", "90~180~360~2π", 1,
        "Une demi-circle, soit π radians, correspond à 180 degrés."),
     QC("Qu'est-ce que la phase d'une grandeur sinusoïdale ?", "Son amplitude~Son décalage par rapport à une autre grandeur~Sa fréquence~Sa puissance", 1,
        "La phase exprime le décalage angulaire entre deux signaux de même fréquence."),
     QT("Calculer la norme et le cosinus de l'angle d'un vecteur de composantes (6 ; 8) avec l'axe des abscisses.",
        "La norme du vecteur est la racine de 6² + 8², soit la racine de 100, donc 10. Le cosinus de l'angle entre le vecteur et l'axe des abscisses vaut la composante horizontale divisée par la norme, soit 6/10 = 0,6. Le sinus vaut 8/10 = 0,8, ce qui vérifie bien 0,6² + 0,8² = 0,36 + 0,64 = 1. L'angle associé est d'environ 53,1 degrés.",
        "On attend la norme par Pythagore, puis le rapport entre la composante horizontale et la norme."),
     QT("Expliquer pourquoi la décomposition d'une force et l'analyse d'un signal alternatif utilisent les mêmes outils.",
        "Dans les deux cas, on représente une grandeur orientée dans un repère. Une force se décompose en composantes horizontale et verticale ; une tension sinusoïdale se représente par un vecteur tournant dont la projection sur un axe donne la valeur instantanée. Les formules du cosinus et du sinus permettent de passer de la grandeur totale aux composantes, et la phase joue le rôle de l'angle. Le produit scalaire et la notion d'orthogonalité servent aussi bien à étudier des forces qu'à séparer les parties active et réactive d'une puissance.",
        "La réponse doit montrer que projection, angle et trigonométrie sont communs aux deux domaines.")],
    C("Vecteurs et trigonométrie décrivent les projections utilisées en mécanique et en courant alternatif.",
      "Norme = racine(x² + y²) · cos = adjacent/hypoténuse · sin = opposé/hypoténuse",
      "sin² + cos² = 1 · 180 degrés = π radians",
      "Composante x~Projection horizontale~Différence des abscisses~Norme~Longueur du vecteur~Racine de x²+y²~Cosinus~Adjacent sur hypoténuse~Angle",
      "Choisir un repère orthonormé|Calculer les composantes|Calculer la norme|Employer cosinus ou sinus|Vérifier avec sin²+cos²",
      "Confondre norme et composante|Oublier la racine carrée|Inverser adjacent et opposé|Mélanger degrés et radians",
      "Vecteur (6;8)~Norme 10~Cosinus 0,6~Vecteur (3;4)~Norme 5~Cosinus 0,6~Angle 53 degrés~sin 0,8",
      "Vecteur~Direction et sens~Pas de point fixe~Point~Position dans le repère~Coordonnées x et y~Force~Point d'application",
      "Sinus~Opposé sur hypoténuse~Composante verticale~Cosinus~Adjacent sur hypoténuse~Composante horizontale"))

# ============================================================ MA4
add("PE-A08", "Statistiques et probabilités", "Mathématiques", ["1re pro"],
    S("Une série statistique est un ensemble de valeurs relevées sur une population ou un échantillon."
      "|La moyenne est la somme des valeurs divisée par l'effectif total."
      "|La médiane partage la série ordonnée en deux moitiés de même effectif."
      "|L'étendue est la différence entre la valeur maximale et la valeur minimale."
      "|La variance mesure la dispersion des valeurs autour de la moyenne ; son écart type est la racine carrée."
      "|Un histogramme représente les effectifs ou les fréquences par classes de valeurs."
      "|Une fréquence est le quotient de l'effectif d'une classe par l'effectif total."
      "|Une expérience aléatoire a plusieurs résultats possibles, incertains avant son déroulement."
      "|La probabilité d'un événement est un nombre entre 0 et 1, parfois exprimé en pourcentage."
      "|Si tous les résultats sont équiprobables, la probabilité vaut le nombre de cas favorables divisé par le nombre de cas possibles."
      "|La probabilité complémentaire d'un événement vaut 1 moins la probabilité de cet événement."
      "|Ces outils servent à analyser des mesures, des taux de défauts et la fiabilité d'une installation."),
    [QC("Comment calculer la moyenne d'une série ?", "En divisant la somme des valeurs par l'effectif~En prenant la valeur centrale~En soustrayant le minimum du maximum~En additionnant les fréquences", 0,
        "La moyenne est la somme des valeurs divisée par le nombre de valeurs."),
     QC("Que représente la médiane ?", "La valeur la plus élevée~La valeur qui partage la série ordonnée en deux~La moyenne des extrêmes~L'écart type", 1,
        "La médiane laisse autant de valeurs au-dessus qu'au-dessous elle."),
     QC("Quelle est l'étendue d'une série ?", "La somme des valeurs~La différence entre max et min~Le produit des extrêmes~La moyenne", 1,
        "L'étendue mesure l'écart entre la plus grande et la plus petite valeur."),
     QC("Quel est l'écart type ?", "La variance au carré~La racine carrée de la variance~La médiane~La fréquence", 1,
        "L'écart type est la racine carrée de la variance et s'exprime dans la même unité que les valeurs."),
     QC("Quelle est la probabilité d'un événement impossible ?", "1~0~0,5~100", 1,
        "Un événement impossible a une probabilité nulle ; un événement certain a une probabilité de 1."),
     QC("Comment obtenir la probabilité complémentaire ?", "En doublant la probabilité~En calculant 1 moins la probabilité~En la divisant par deux~En la multipliant par 100", 1,
        "Un événement et son contraire forment une partition : leurs probabilités totalisent 1."),
     QC("Que représente une fréquence dans un histogramme ?", "La hauteur maximale~L'effectif de la classe divisé par l'effectif total~La moyenne~L'étendue", 1,
        "La fréquence relative est l'effectif de la classe divisé par l'effectif total."),
     QT("Calculer la moyenne et l'étendue de la série de mesures 8, 10, 12, 12, 18.",
        "La somme des cinq valeurs vaut 8 + 10 + 12 + 12 + 18 = 60. L'effectif est 5, donc la moyenne vaut 60 / 5 = 12. La valeur maximale est 18 et la valeur minimale est 8, donc l'étendue vaut 18 - 8 = 10. La série ordonnée étant déjà donnée, la médiane est la troisième valeur, soit 12. La moyenne et la médiane coïncident ici, ce qui indique une répartition plutôt symétrique malgré un écart de 10 entre les extrêmes.",
        "On attend la somme divisée par l'effectif, puis la différence entre maximum et minimum."),
     QT("Dans un lot de 200 pièces, 12 sont défectueuses. Calculer la probabilité de tomber sur une pièce conforme et son complément.",
        "Le nombre de pièces conformes vaut 200 - 12 = 188. La probabilité de tirer une pièce conforme est donc 188/200 = 0,94, soit 94 %. La probabilité complémentaire, celle de tirer une pièce défectueuse, vaut 1 - 0,94 = 0,06, soit 6 %. On retrouve directement 12/200 = 0,06. La somme des deux probabilités vaut bien 1, ce qui vérifie le calcul.",
        "La réponse doit donner la probabilité de l'événement, son complément par 1 - p, et le contrôle de la somme.")],
    C("Les statistiques décrivent une série de mesures, les probabilités quantifient l'incertitude d'un tirage.",
      "Moyenne = somme / effectif · étendue = max - min",
      "Probabilité = cas favorables / cas possibles · complément = 1 - p",
      "Moyenne~Valeur centrale~Somme sur effectif~Médiane~Valeur qui sépare~Série ordonnée~Étendue~Max moins min~Dispersion",
      "Ordonner les valeurs|Calculer moyenne et médiane|Calculer étendue et écart type|Construire l'histogramme|Interpréter les résultats",
      "Moyenne sans diviser par l'effectif|Oublier d'ordonner avant la médiane|Confondre fréquence et probabilité|Additionner des probabilités complémentaires",
      "Série~8 10 12 12 18~Moyenne 12~Lot de 200~12 défectueuses~Probabilité 0,94~Complément~0,06",
      "Moyenne~Sensible aux valeurs extrêmes~Médiane~Résistante aux extrêmes~Étendue~Très sensible au minimum et au maximum",
      "Probabilité nulle~Événement impossible~Probabilité égale à 1~Événement certain~Complément~Événement contraire"))

# ============================================================ PC1
add("PE-A09", "Énergie, puissance et conversions", "Physique-Chimie", ["2nde pro"],
    S("L'énergie est une grandeur qui mesure la capacité d'un système à fournir un travail ou de la chaleur."
      "|L'énergie mécanique est la somme de l'énergie cinétique et de l'énergie potentielle de position."
      "|L'énergie cinétique d'un corps de masse m et de vitesse v vaut un demi m v²."
      "|L'énergie potentielle de pesanteur vaut m g h, avec g l'intensité de la gravité."
      "|Le travail d'une force est le produit de la force par le déplacement dans la direction de la force."
      "|La puissance est l'énergie transférée par unité de temps : P = W / t."
      "|L'unité légale de l'énergie est le joule et celle de la puissance est le watt."
      "|Le kilowattheure est une unité courante pour l'énergie électrique : 1 kWh vaut 3,6 millions de joules."
      "|Le principe de conservation de l'énergie énonce que l'énergie ne se crée ni ne se détruit, elle se transforme."
      "|Un rendement est le rapport entre l'énergie utile obtenue et l'énergie fournie."
      "|Les pertes, souvent sous forme de chaleur, expliquent qu'un rendement est toujours inférieur à 1."
      "|Ces notions permettent de comparer la consommation et l'efficacité des équipements électriques."),
    [QC("Quelle est l'unité de l'énergie dans le système international ?", "Le watt~Le joule~Le newton~Le volt", 1,
        "Le joule est l'unité d'énergie et de travail ; le watt est l'unité de puissance."),
     QC("Quelle est la formule de l'énergie cinétique ?", "m v~un demi m v²~m g h~m / v²", 1,
        "L'énergie cinétique vaut 1/2 × m × v²."),
     QC("Que vaut 1 kilowattheure en joules ?", "1000 J~3600 J~3,6 millions de J~1 million de J", 2,
        "1 kWh = 1000 W × 3600 s = 3 600 000 J."),
     QC("Quel est le rendement d'un appareil qui restitue 80 J pour 100 J reçus ?", "0,2~0,8~1,25~80", 1,
        "Le rendement vaut l'énergie utile divisée par l'énergie fournie, soit 0,8."),
     QC("Que devient l'énergie perdue dans une transformation ?", "Elle disparaît~Elle se transforme souvent en chaleur~Elle devient du courant~Elle est stockée dans le vide", 1,
        "Le principe de conservation implique une transformation, fréquemment en chaleur."),
     QC("Quelle est la puissance d'un appareil qui consomme 600 J en 30 s ?", "20 W~30 W~600 W~18 000 W", 0,
        "P = W/t = 600/30 = 20 W."),
     QC("Que mesure le travail d'une force ?", "La masse d'un corps~Le produit force par déplacement~La vitesse~La température", 1,
        "Le travail vaut F × d lorsque la force et le déplacement ont la même direction."),
     QT("Expliquer le principe de conservation de l'énergie et l'illustrer avec un moteur électrique.",
        "L'énergie ne peut être ni créée ni détruite : elle change seulement de forme. Dans un moteur électrique, l'énergie électrique fournie par le réseau est convertie principalement en énergie mécanique de rotation. Une partie devient de la chaleur dans les enroulements à cause de l'effet Joule, et une autre est dissipée par les frottements et le bruit. La somme de l'énergie mécanique utile et des pertes est égale à l'énergie électrique consommée. Le rendement traduit la part effectivement utile de cette conversion.",
        "On attend l'énoncé du principe et un bilan énergétique avec énergie utile plus pertes."),
     QT("Un appareil de 2 kW fonctionne 3 heures par jour. Calculer sa consommation quotidienne en kWh et son coût à 0,20 € le kWh.",
        "L'énergie consommée vaut la puissance multipliée par la durée : 2 kW × 3 h = 6 kWh par jour. En joules, cela représente 6 × 3,6 millions = 21,6 millions de joules. Au tarif de 0,20 € le kWh, le coût journalier est 6 × 0,20 = 1,20 €. Sur une période de 30 jours, la consommation atteint 180 kWh pour un coût de 36 €. Ce calcul montre l'intérêt de raisonner en kWh pour la facturation de l'énergie électrique.",
        "La réponse doit calculer la puissance fois la durée, puis multiplier par le prix unitaire.")],
    C("L'énergie se transforme mais ne disparaît jamais ; la puissance mesure la vitesse de cette transformation.",
      "Ec = 1/2 m v² · Ep = m g h · P = W / t",
      "1 kWh = 3,6 × 10⁶ J · rendement = énergie utile / énergie fournie < 1",
      "Énergie cinétique~Dépend de la vitesse~1/2 m v²~Énergie potentielle~Dépend de la hauteur~m g h~Puissance~Énergie par seconde~W/t",
      "Identifier les formes d'énergie|Calculer l'énergie fournie|Repérer les pertes|Calculer le rendement|Exprimer la consommation en kWh",
      "Confondre énergie et puissance|Oublier de convertir les heures en secondes|Croire que le rendement peut dépasser 1|Négliger les pertes thermiques",
      "2 kW pendant 3 h~6 kWh~600 J en 30 s~20 W~Rendement 80 %~80 J utiles sur 100 J",
      "Énergie~Capacité de fournir un travail~Unité joule~Puissance~Énergie par unité de temps~Unité watt~Travail~Force fois déplacement",
      "Conversion~Changement de forme d'énergie~Bilan conservé~Perte~Énergie non utile~Chaleur et bruit"))

# ============================================================ PC2
add("PE-A10", "Courant électrique, tension et résistance", "Physique-Chimie", ["2nde pro"],
    S("Un courant électrique est un déplacement ordonné de charges dans un conducteur."
      "|L'intensité du courant se mesure en ampères avec un ampèremètre placé en série."
      "|La tension entre deux points se mesure en volts avec un voltmètre placé en dérivation."
      "|La résistance électrique caractérise l'opposition d'un conducteur au passage du courant."
      "|La loi d'Ohm relie la tension, l'intensité et la résistance par U = R I."
      "|Un conducteur ohmique a une résistance constante quand la température reste fixe."
      "|Un générateur fournit une tension et délivre un courant dans un circuit fermé."
      "|Dans un circuit en série, l'intensité est la même en tout point et la résistance équivalente est la somme des résistances."
      "|Dans un circuit en dérivation, la tension est la même aux bornes de chaque branche."
      "|La puissance électrique consommée par un dipôle vaut P = U I, en watts."
      "|L'énergie consommée pendant une durée t vaut W = P t."
      "|Respecter les polarités et choisir la bonne gamme de mesure évite de détériorer les appareils."),
    [QC("Avec quel appareil mesure-t-on l'intensité du courant ?", "Un voltmètre~Un ampèremètre~Un ohmètre~Un thermomètre", 1,
        "L'ampèremètre se place en série dans le circuit et mesure l'intensité en ampères."),
     QC("Comment doit-on brancher un voltmètre ?", "En série~En dérivation aux bornes du dipôle~En court-circuit~Sans le brancher", 1,
        "Le voltmètre se branche en dérivation, aux bornes de l'élément dont on mesure la tension."),
     QC("Quelle est la relation de la loi d'Ohm ?", "U = I / R~U = R I~U = R + I~U = I - R", 1,
        "La tension aux bornes d'un conducteur ohmique vaut le produit R fois I."),
     QC("Que vaut la résistance équivalente de deux résistances en série ?", "Leur produit~Leur somme~Leur moyenne~Leur différence", 1,
        "En série, les résistances s'additionnent."),
     QC("Dans un circuit en dérivation, quelle grandeur est commune à toutes les branches ?", "L'intensité~La tension~La résistance~La puissance", 1,
        "Les branches en parallèle sont soumises à la même tension."),
     QC("Quelle est la puissance d'un dipôle traversé par 2 A sous 12 V ?", "6 W~14 W~24 W~48 W", 2,
        "P = U I = 12 × 2 = 24 W."),
     QC("Quel risque présente un ampèremètre branché en dérivation ?", "Il affiche zéro~Il court-circuite le dipôle et peut être détruit~Il mesure la tension~Il augmente la résistance", 1,
        "L'ampèremètre a une très faible résistance interne : en dérivation, il provoque un court-circuit."),
     QT("Expliquer la différence entre un branchement en série et un branchement en dérivation.",
        "En série, les dipôles se suivent sur un seul chemin : l'intensité est la même dans tout le circuit, les tensions s'ajoutent et la résistance équivalente est la somme des résistances. En dérivation, les dipôles sont branchés entre les mêmes deux points : la tension est identique aux bornes de chaque branche, les intensités s'ajoutent et la résistance équivalente est inférieure à la plus petite résistance. L'éclairage domestique utilise la dérivation pour que chaque appareil puisse fonctionner indépendamment des autres.",
        "On attend la comparaison des grandeurs communes et l'exemple de l'installation domestique."),
     QT("Deux résistances de 10 ohm et 30 ohm sont branchées en série sous 12 V. Calculer l'intensité et la puissance totale.",
        "La résistance équivalente en série vaut 10 + 30 = 40 ohm. Par la loi d'Ohm, l'intensité du courant vaut U/R = 12/40 = 0,3 A. La puissance totale consommée est P = U I = 12 × 0,3 = 3,6 W. On peut aussi la calculer par R I² = 40 × 0,09 = 3,6 W, ce qui confirme le résultat. La tension se répartit proportionnellement aux résistances : 3 V aux bornes de la première et 9 V aux bornes de la seconde.",
        "La réponse doit additionner les résistances, appliquer U = RI puis calculer P = UI.")],
    C("Tension, intensité et résistance sont liées par la loi d'Ohm et se mesurent avec des montages précis.",
      "U = R I · P = U I · W = P t",
      "Ampèremètre en série · voltmètre en dérivation · impédance en courant alternatif",
      "Tension~Différence de potentiel~Volt~Intensité~Débit de charges~Ampère~Résistance~Opposition au courant~Ohm",
      "Vérifier que le circuit est ouvert avant branchement|Placer l'ampèremètre en série|Placer le voltmètre en dérivation|Choisir la gamme de mesure|Relever et interpréter les valeurs",
      "Brancher l'ampèremètre en dérivation|Inverser les polarités|Choisir une gamme trop faible|Mesurer sous tension sans précaution",
      "12 V et 2 A~P = 24 W~10 et 30 ohm en série~R = 40 ohm~I = 0,3 A~P = 3,6 W",
      "Circuit série~Même intensité~Résistances additionnées~Circuit dérivation~Même tension~Intensités additionnées~Court-circuit~Résistance quasi nulle",
      "Voltmètre~Grande résistance interne~Se branche en dérivation~Ampèremètre~Faible résistance interne~Se branche en série"))

# ============================================================ PC3
add("PE-A11", "Signaux lumineux et optique", "Physique-Chimie", ["1re pro"],
    S("La lumière est une onde électromagnétique qui se propage dans le vide à environ 300 000 km par seconde."
      "|Le spectre visible correspond à des longueurs d'onde comprises environ entre 400 et 800 nanomètres."
      "|Une longueur d'onde est la distance parcourue par l'onde pendant une période."
      "|La fréquence et la longueur d'onde sont liées par la relation c = λ f."
      "|La réflexion est le retour d'un rayon lumineux sur la surface qu'il rencontre."
      "|La réfraction est le changement de direction d'un rayon lors du passage d'un milieu à un autre."
      "|Une lentille convergente fait converger les rayons parallèles en un foyer."
      "|La distance focale est la distance entre le centre optique de la lentille et son foyer."
      "|Les fibres optiques guident la lumière par réflexions internes successives."
      "|Une diode électroluminescente convertit une partie de l'énergie électrique en lumière."
      "|Le rendement lumineux d'une source se compare à sa puissance électrique consommée."
      "|Ces notions expliquent les voyants, les afficheurs et les liaisons par fibre optique."),
    [QC("Quelle est la vitesse de la lumière dans le vide ?", "300 km/s~3000 km/s~300 000 km/s~3 millions de km/s", 2,
        "La vitesse de la lumière dans le vide vaut environ 3 × 10⁸ m/s, soit 300 000 km/s."),
     QC("Quelle relation relie vitesse, longueur d'onde et fréquence ?", "c = λ / f~c = λ f~c = f / λ~c = λ + f", 1,
        "La vitesse de propagation vaut le produit de la longueur d'onde par la fréquence."),
     QC("Que se passe-t-il lors d'une réfraction ?", "Le rayon revient en arrière~Le rayon change de direction~Le rayon disparaît~La couleur change toujours", 1,
        "La réfraction modifie la direction du rayon au changement de milieu."),
     QC("Qu'est-ce qu'une lentille convergente ?", "Une lentille qui éloigne les rayons~Une lentille qui rassemble les rayons parallèles en un foyer~Un miroir plan~Une fibre", 1,
        "Les rayons parallèles convergent au foyer d'une lentille convergente."),
     QC("Comment la lumière est-elle guidée dans une fibre optique ?", "Par réfraction interne~Par réflexions internes successives~Par conduction électrique~Par diffraction", 1,
        "Le principe de la fibre optique repose sur la réflexion interne totale."),
     QC("Que convertit une diode électroluminescente ?", "Du courant en chaleur seulement~Une partie de l'énergie électrique en lumière~De la lumière en courant~Du son en lumière", 1,
        "Une LED émet de la lumière sous l'effet d'un courant électrique."),
     QC("Quelle grandeur caractérise la couleur d'une lumière ?", "Son intensité~Sa longueur d'onde~Sa puissance~Sa polarité", 1,
        "La couleur correspond à la longueur d'onde dominante du rayonnement."),
     QT("Expliquer la différence entre réflexion et réfraction, avec un exemple concret.",
        "La réflexion se produit quand un rayon rencontre une surface et revient dans le milieu d'origine, comme sur un miroir : l'angle de réflexion est égal à l'angle d'incidence. La réfraction se produit quand le rayon passe d'un milieu à un autre, par exemple de l'air dans le verre : sa vitesse change et sa direction se modifie, sauf s'il arrive perpendiculairement à la surface. Dans une fibre optique, c'est la réflexion interne totale qui confine la lumière, tandis que dans une lentille c'est la réfraction qui assure la convergence des rayons.",
        "On attend la définition des deux phénomènes et un exemple illustrant chacun."),
     QT("Une lumière rouge a une longueur d'onde de 650 nm. Calculer sa fréquence et la comparer à celle d'une lumière bleue de 450 nm.",
        "La fréquence vaut c divisé par la longueur d'onde. Pour 650 nm, soit 6,5 × 10⁻⁷ m, on obtient f = 3 × 10⁸ / 6,5 × 10⁻⁷, soit environ 4,6 × 10¹⁴ Hz. Pour la lumière bleue de 450 nm, soit 4,5 × 10⁻⁷ m, la fréquence vaut environ 6,7 × 10¹⁴ Hz. La lumière bleue a donc une fréquence plus élevée et une longueur d'onde plus courte que la lumière rouge, conformément à la relation c = λ f.",
        "La réponse doit convertir les nanomètres en mètres, appliquer c = λ f et comparer les deux fréquences.")],
    C("Lumière et signaux optiques relient longueur d'onde, fréquence et propagation dans les fibres.",
      "c = λ f · c ≈ 3 × 10⁸ m/s dans le vide",
      "Spectre visible : environ 400 à 800 nm · réflexion interne dans la fibre",
      "Longueur d'onde~Distance parcourue par période~Nanomètre~Fréquence~Nombre d'oscillations par seconde~Hertz~Réfraction~Changement de direction~Changement de milieu",
      "Identifier le phénomène optique|Tracer le rayon incident|Appliquer la loi adaptée|Calculer la fréquence si besoin|Relier à l'application technique",
      "Confondre réflexion et réfraction|Oublier la conversion en mètres|Croire que la couleur dépend de l'intensité|Ignorer la perte de lumière dans la fibre",
      "650 nm~4,6 × 10¹⁴ Hz~450 nm~6,7 × 10¹⁴ Hz~Fibre optique~Réflexions internes~LED~Conversion électrique en lumière",
      "Réflexion~Retour dans le même milieu~Miroir~Réfraction~Passage dans un autre milieu~Lentille~Diffraction~Contournement d'obstacle",
      "Lumière rouge~Grande longueur d'onde~Basse fréquence~Lumière bleue~Petite longueur d'onde~Haute fréquence"))

# ============================================================ HG1
add("PE-A12", "La Révolution industrielle et ses effets", "Histoire-géographie", ["2nde pro"],
    S("La Révolution industrielle désigne la phase de transformation économique et sociale qui commence en Angleterre au XVIIIe siècle."
      "|La machine à vapeur, perfectionnée par Watt, fournit une nouvelle source d'énergie mécanique."
      "|Le textile est le premier secteur concerné, avec le métier à tisser mécanique et la filature."
      "|La métallurgie et le chemin de fer se développent au XIXe siècle en France et en Europe."
      "|L'industrialisation s'accompagne d'une forte croissance démographique et de l'urbanisation."
      "|Les ouvriers quittent les campagnes pour les villes et les usines."
      "|La journée de travail est longue et les conditions de vie restent difficiles au XIXe siècle."
      "|Le capitalisme industriel se caractérise par l'investissement, la concurrence et la recherche du profit."
      "|Les syndicats et les grèves apparaissent pour défendre les droits des travailleurs."
      "|Les prix de l'énergie et du transport baissent grâce aux innovations techniques."
      "|En France, la révolution industrielle s'accélère après 1830 et surtout sous le Second Empire."
      "|Cette période explique l'importance durable de l'énergie, de la machine et du travail industriel."),
    [QC("Dans quel pays commence la Révolution industrielle ?", "La France~L'Angleterre~L'Allemagne~Les États-Unis", 1,
        "Le mouvement débute en Angleterre dans la seconde moitié du XVIIIe siècle."),
     QC("Quelle invention fournit une nouvelle source d'énergie mécanique ?", "La machine à vapeur~L'imprimerie~Le télégraphe~La roue hydraulique", 0,
        "La machine à vapeur de Watt devient le moteur essentiel de l'industrialisation."),
     QC("Quel secteur est d'abord transformé ?", "La banque~Le textile~L'agriculture~Le tourisme", 1,
        "La filature et le tissage mécaniques constituent le premier secteur concerné."),
     QC("Quel mouvement social accompagne l'industrialisation ?", "L'exode urbain~L'urbanisation~La dépopulation~Le retour à la campagne", 1,
        "Les ouvriers affluent vers les villes où se concentrent les usines."),
     QC("Que défendent les premiers syndicats ?", "Les profits des actionnaires~Les droits et les conditions de travail~La fermeture des usines~Le retour au Moyen Âge", 1,
        "Les organisations ouvrières luttent pour de meilleures conditions de travail et de vie."),
     QC("Quand l'industrialisation s'accélère-t-elle en France ?", "Avant 1750~Après 1830~En 1789~Au XXe siècle", 1,
        "La France s'industrialise plus tardivement, avec un essor net après 1830."),
     QC("Quel effet l'industrialisation a-t-elle sur les prix de transport ?", "Ils augmentent fortement~Ils baissent grâce aux innovations~Ils disparaissent~Ils restent identiques", 1,
        "Chemin de fer et bateaux à vapeur réduisent les coûts et les délais de transport."),
     QT("Expliquer pourquoi la machine à vapeur a joué un rôle central dans la Révolution industrielle.",
        "La machine à vapeur a fourni une énergie mécanique disponible en continu, indépendamment de la force humaine, animale ou hydraulique. Elle a permis d'alimenter les métiers textiles, les hauts fourneaux puis les locomotives et les navires. Elle a aussi favorisé la concentration des usines près des gisements de charbon et des voies de communication. En réduisant le coût de l'énergie et du transport, elle a accéléré la production de masse et l'extension des marchés, transformant en profondeur l'économie et la société.",
        "On attend le lien entre énergie mécanique, usines, transport et croissance de la production."),
     QT("Décrire les principales conséquences sociales de l'industrialisation au XIXe siècle.",
        "L'industrialisation provoque un exode rural et une croissance rapide des villes ouvrières. Les conditions de travail sont difficiles : longues journées, salaires bas, travail des femmes et des enfants. La classe ouvrière se constitue et développe une conscience collective. Des syndicats, des grèves et des mutuelles apparaissent pour obtenir de meilleures conditions. Les pouvoirs publics interviennent progressivement avec des lois sur le travail et la protection des travailleurs, posant les bases de l'État social.",
        "La réponse doit évoquer urbanisation, conditions de travail, syndicalisation et intervention de l'État.")],
    C("La Révolution industrielle transforme l'énergie, le travail et la société en profondeur.",
      "Énergie mécanique + usines + chemin de fer = production de masse",
        "XVIIIe siècle en Angleterre · XIXe siècle en France · capitalisme et syndicats",
      "Machine à vapeur~Énergie mécanique~Charbon~Textile~Premier secteur~Filature~Chemin de fer~Transport moins cher~Urbanisation",
      "Situer la période et le pays|Identifier les innovations techniques|Analyser les secteurs concernés|Relever les effets sociaux|Relier au présent industriel",
      "Confondre Révolution industrielle et Révolution française|Croire que le travail devient vite facile|Oublier le rôle du charbon|Ignorer les résistances ouvrières",
      "Angleterre~XVIIIe siècle~Machine à vapeur~Watt~Textile~Premier secteur~France~Essor après 1830",
      "Travail artisanal~Production lente~Petits ateliers~Travail industriel~Production de masse~Grandes usines~Mécanisation~Remplacement de la force humaine",
      "Capitalisme~Investissement et profit~Initiative privée~Syndicat~Défense des travailleurs~Action collective"))

# ============================================================ HG2
add("PE-A13", "L'Europe depuis 1945 : construction et élargissement", "Histoire-géographie", ["1re pro"],
    S("Après 1945, l'Europe est divisée en deux blocs par la guerre froide entre l'Est et l'Ouest."
      "|La CECA, créée en 1951, met en commun le charbon et l'acier pour éviter de nouvelles guerres."
      "|Le traité de Rome de 1957 institue la Communauté économique européenne, future Union européenne."
      "|Les quatre libertés de circulation concernent les marchandises, les personnes, les services et les capitaux."
      "|Le marché unique est achevé par l'Acte unique européen de 1986."
      "|Le traité de Maastricht de 1992 crée l'Union européenne et prévoit la monnaie unique."
      "|L'euro est introduit comme monnaie scripturale en 1999 et comme monnaie fiduciaire en 2002."
      "|L'élargissement de 2004 intègre dix nouveaux États, surtout d'Europe centrale et orientale."
      "|L'Espace Schengen supprime les contrôles aux frontières intérieures entre les pays participants."
      "|L'Union européenne possède des institutions : Commission, Parlement, Conseil et Cour de justice."
      "|La politique énergétique et la transition écologique sont devenues des priorités communes."
      "|Ces décisions expliquent les normes et les règles de sécurité applicables aux installations électriques."),
    [QC("Quel traité crée la Communauté économique européenne en 1957 ?", "Le traité de Paris~Le traité de Rome~Le traité de Maastricht~Le traité de Lisbonne", 1,
        "Les traités de Rome instituent la CEE et l'Euratom en 1957."),
     QC("Que met en commun la CECA créée en 1951 ?", "Le pétrole et le gaz~Le charbon et l'acier~L'électricité et l'eau~Les armes", 1,
        "La Communauté européenne du charbon et de l'acier vise à rendre la guerre impossible entre ses membres."),
     QC("Combien de libertés de circulation définit le marché unique ?", "Deux~Trois~Quatre~Cinq", 2,
        "Marchandises, personnes, services et capitaux circulent librement."),
     QC("Quel traité crée l'Union européenne en 1992 ?", "Maastricht~Rome~Amsterdam~Nice", 0,
        "Le traité de Maastricht fonde l'Union européenne et lance le projet de monnaie unique."),
     QC("Quand l'euro devient-il une monnaie fiduciaire en espèces ?", "1999~2002~1957~2004", 1,
        "Les billets et pièces en euro circulent à partir du 1er janvier 2002."),
     QC("Que permet l'Espace Schengen ?", "Une monnaie commune~La suppression des contrôles aux frontières intérieures~Une armée commune~Un seul parlement", 1,
        "Schengen supprime les contrôles systématiques entre les pays participants."),
     QC("Quelle institution propose les lois européennes ?", "La Cour de justice~La Commission européenne~La Banque centrale~Le Conseil d'État", 1,
        "La Commission détient le monopole d'initiative législative au niveau européen."),
     QT("Expliquer pourquoi la mise en commun du charbon et de l'acier a précédé le marché unique.",
        "Après la Seconde Guerre mondiale, la France et l'Allemagne devaient réconcilier leurs économies et empêcher une nouvelle guerre. Le charbon et l'acier étaient les deux ressources stratégiques nécessaires à l'armement et à l'industrie : les mettre sous une autorité commune rendait un conflit militaire entre ces pays presque impossible. Cette première réussite a créé un climat de confiance. Elle a permis d'étendre ensuite la coopération à l'ensemble des biens et des services avec le traité de Rome, puis au-delà de l'économie avec l'Union européenne.",
        "On attend le lien entre réconciliation, ressources stratégiques et extension progressive de la coopération."),
     QT("Décrire les étapes qui mènent du traité de Rome à l'euro.",
        "Le traité de Rome de 1957 crée la CEE et un marché commun progressif. L'Acte unique de 1986 relance l'intégration et fixe l'achèvement du marché unique pour 1993. Le traité de Maastricht de 1992 crée l'Union européenne et définit les critères de convergence pour la monnaie unique. L'euro naît comme monnaie scripturale en 1999 pour les pays qui remplissent les critères, puis les billets et pièces circulent en 2002. Cette succession montre une intégration économique de plus en plus poussée.",
        "La réponse doit citer Rome, Acte unique, Maastricht, 1999 et 2002 dans un ordre chronologique.")],
    C("L'Europe s'est construite par étapes, de la mise en commun des ressources à la monnaie unique.",
      "CECA 1951 · Rome 1957 · Acte unique 1986 · Maastricht 1992",
      "Quatre libertés · euro en 1999 et 2002 · élargissement de 2004",
      "CECA~Charbon et acier~1951~CEE~Traité de Rome~1957~Union européenne~Maastricht 1992~Euro",
      "Situer les grandes dates|Identifier les traités|Relever les libertés de circulation|Expliquer l'élargissement|Relier aux normes professionnelles",
      "Confondre CECA et CEE|Placer l'euro en 1957|Oublier l'Acte unique|Croire que Schengen concerne la monnaie",
      "1951~CECA~1957~Traités de Rome~1992~Maastricht~1999~Euro scriptural~2002~Euro en espèces",
      "Marche commun~Suppression des barrières~Libertés de circulation~Marche unique~Intégration approfondie~Quatre libertés~Espace Schengen~Frontières intérieures ouvertes",
      "Union européenne~Structure politique et économique~CEE~Communauté économique~États membres~Pays participants~Institutions~Commission et Parlement"))

# ============================================================ HG3
add("PE-A14", "La France de la Ve République", "Histoire-géographie", ["Terminale pro"],
    S("La Ve République est instaurée en 1958 après la crise politique de la guerre d'Algérie."
      "|Le général de Gaulle est l'artisan de la nouvelle Constitution, adoptée par référendum le 28 septembre 1958."
      "|Le régime est semi-présidentiel : le président de la République et le Premier ministre partagent le pouvoir exécutif."
      "|Le président est élu au suffrage universel direct depuis la réforme de 1962."
      "|Il nomme le Premier ministre et peut dissoudre l'Assemblée nationale."
      "|Le Parlement est bicaméral, composé de l'Assemblée nationale et du Sénat."
      "|La loi est votée par le Parlement puis promulguée par le président de la République."
      "|Le Conseil constitutionnel vérifie la conformité des lois à la Constitution."
      "|Le Conseil d'État conseille le gouvernement et juge les litiges administratifs."
      "|La Cour de cassation est la plus haute juridiction de l'ordre judiciaire."
      "|Le préfet représente l'État dans chaque département et veille au respect des lois."
      "|La collectivité territoriale gère les services locaux sous le contrôle de l'État."),
    [QC("En quelle année la Ve République est-elle instaurée ?", "1945~1958~1962~1968", 1,
        "La Constitution de la Ve République est adoptée en 1958."),
     QC("Comment le président de la République est-il élu depuis 1962 ?", "Par le Parlement~Au suffrage universel direct~Par le Conseil constitutionnel~Par les préfets", 1,
        "La réforme de 1962 instaure l'élection présidentielle au suffrage universel direct."),
     QC("Quel est le système politique de la Ve République ?", "Parlementaire~Semi-présidentiel~Présidentiel absolu~Monarchique", 1,
        "Le pouvoir exécutif est partagé entre le président et le Premier ministre."),
     QC("Qui nomme le Premier ministre ?", "L'Assemblée nationale~Le président de la République~Le Conseil d'État~Le Sénat", 1,
        "Le président nomme le Premier ministre, généralement issu de la majorité parlementaire."),
     QC("Quelles sont les deux chambres du Parlement ?", "Assemblée nationale et Sénat~Conseil d'État et Cour de cassation~Conseil constitutionnel et Sénat~Assemblée et Conseil municipal", 0,
        "Le Parlement français est bicaméral : Assemblée nationale et Sénat."),
     QC("Quel organe vérifie la conformité d'une loi à la Constitution ?", "Le Conseil d'État~Le Conseil constitutionnel~La Cour de cassation~La Cour des comptes", 1,
        "Le Conseil constitutionnel est le juge de la constitutionnalité des lois."),
     QC("Qui représente l'État dans un département ?", "Le maire~Le préfet~Le député~Le sénateur", 1,
        "Le préfet est le représentant de l'État au niveau départemental."),
     QT("Expliquer ce que signifie un régime semi-présidentiel.",
        "Un régime semi-présidentiel associe un président élu au suffrage universel et un gouvernement responsable devant le Parlement. En France, le président définit les grandes orientations, nomme le Premier ministre et dispose de pouvoirs propres comme la dissolution de l'Assemblée nationale ou le référendum. Le Premier ministre dirige l'action du gouvernement et doit pouvoir compter sur une majorité à l'Assemblée. Le président ne peut donc pas gouverner seul : il lui faut un gouvernement soutenu par le Parlement. Cet équilibre distingue la Ve République d'un régime présidentiel pur.",
        "On attend la dualité de l'exécutif et la responsabilité du gouvernement devant le Parlement."),
     QT("Décrire le parcours d'une loi depuis sa proposition jusqu'à son application.",
        "Une loi peut être proposée par le gouvernement ou par un parlementaire. Elle est examinée en commission, puis débattue et votée par l'Assemblée nationale et le Sénat, qui doivent adopter un texte identique. Le texte voté est transmis au président de la République qui le promulgue, après un éventuel contrôle du Conseil constitutionnel. La loi est ensuite publiée au Journal officiel et entre en vigueur. Son application est assurée par l'administration, sous l'autorité du gouvernement et du préfet au niveau local.",
        "La réponse doit suivre l'ordre : proposition, examen parlementaire, promulgation, publication et application.")],
    C("La Ve République repose sur un exécutif dual et un Parlement qui vote la loi sous contrôle constitutionnel.",
      "Président + Premier ministre = exécutif · Parlement = Assemblée nationale + Sénat",
      "Constitution 1958 · suffrage universel direct 1962 · Conseil constitutionnel",
      "Président~Chef de l'État~Élu en 1962~Premier ministre~Chef du gouvernement~Nommé par le président~Parlement~Assemblée et Sénat~Vote la loi",
      "Situer 1958 et 1962|Identifier les organes du pouvoir|Comprendre la répartition des compétences|Suivre le parcours d'une loi|Relier à l'action administrative locale",
      "Confondre président et Premier ministre|Oublier le rôle du Conseil constitutionnel|Croire que le Sénat est supérieur|Ignorer le rôle du préfet",
      "1958~Constitution~1962~Suffrage direct~Dissolution~Pouvoir présidentiel~Préfet~Représentant de l'État",
      "Régime parlementaire~Gouvernement responsable~Parlement dominant~Régime présidentiel~Président seul à la tête de l'exécutif~Séparation stricte~Régime semi-présidentiel~Pouvoirs partagés",
      "Conseil constitutionnel~Contrôle des lois~Conseil d'État~Juge administratif~Cour de cassation~Juge judiciaire"))

# ============================================================ EN1
add("PE-A15", "Present simple and past simple in English", "Anglais", ["2nde pro"],
    S("The present simple describes habits, routines and general truths."
      "|With he, she and it, the verb takes an -s in the present simple."
      "|The auxiliary do or does is used for questions and negatives in the present simple."
      "|The past simple describes completed actions at a definite time in the past."
      "|Regular past forms end in -ed, while common irregular verbs have a special form."
      "|The auxiliary did is used for questions and negatives in the past simple."
      "|After did, the main verb goes back to its base form."
      "|Time expressions such as yesterday, last week and in 2020 signal the past simple."
      "|Frequency adverbs such as always, often and never are common with the present simple."
      "|In technical English, the present simple describes what a device does."
      "|The past simple reports a test, a fault or an intervention that is finished."
      "|Choosing the right tense makes a maintenance report clear and reliable."),
    [QC("Which tense describes a habit or a routine ?", "Present simple~Past simple~Future continuous~Present perfect", 0,
        "The present simple is used for habits, routines and general truths."),
     QC("How do you form the third person singular in the present simple ?", "Add -ed~Add -s~Add -ing~Use did", 1,
        "He, she and it take a verb ending in -s : he works."),
     QC("Which auxiliary is used for a negative in the past simple ?", "Do~Does~Did~Have", 2,
        "The past simple negative is did not, followed by the base form."),
     QC("What is the past form of the irregular verb go ?", "Goed~Went~Gone~Going", 1,
        "Go is irregular : its past simple form is went."),
     QC("Which time expression signals the past simple ?", "Every day~Yesterday~Always~Usually", 1,
        "Yesterday refers to a finished time and requires the past simple."),
     QC("After did, which form does the main verb take ?", "Past form~-s form~Base form~-ing form", 2,
        "Did work + base form : Did you check the circuit ?"),
     QC("Which tense is used to describe what a device does ?", "Past simple~Present simple~Present continuous~Future perfect", 1,
        "Technical descriptions of function use the present simple : the switch closes the circuit."),
     QT("Explain the difference between 'The breaker trips' and 'The breaker tripped'.",
        "'The breaker trips' is in the present simple : it describes what the device normally does, a general function or a repeated event. 'The breaker tripped' is in the past simple : it reports one completed event at a known moment, for example during a test yesterday. The first sentence belongs to a description of operation, the second to an incident report. Mixing the two would confuse a functional description with a record of a fault.",
        "The answer must link present simple to function and past simple to a finished event."),
     QT("Put the following sentences in the correct tense : 'Every morning he (check) the panel. Yesterday he (find) a fault.'",
        "The first sentence describes a routine, so it uses the present simple with the third person -s : Every morning he checks the panel. The second sentence refers to a finished moment, yesterday, so it uses the past simple : Yesterday he found a fault. The verb find is irregular, so its past form is found rather than finded. The auxiliary is not needed in these affirmative sentences.",
        "The expected answer is checks and found, with a justification based on routine and finished time.")],
    C("Present simple states how things work, past simple records what happened at a given time.",
      "Present : verb + s with he/she/it · Past : regular -ed or irregular form",
      "do/does for present questions · did + base form for past questions",
      "Present simple~Habits and functions~Works~Past simple~Finished events~Worked~Irregular~Went, found~Special form",
        "Identify the time reference|Choose present or past|Check the subject for -s|Use did with the base form|Read the sentence aloud",
        "Adding -ed to an irregular verb|Using does in the past|Forgetting -s with he or she|Confusing function and incident",
        "He checks~Routine in the present~He checked~Finished action~Yesterday~Past time marker~The switch closes~Technical function",
        "Present simple~General truth or habit~Routine maintenance~Past simple~Completed event~Fault report~Present continuous~Action in progress",
        "Regular verb~Adds -ed~Worked~Irregular verb~Changes form~Went, found"))

# ============================================================ EN2
add("PE-A16", "Modal verbs and technical instructions", "Anglais", ["1re pro"],
    S("Modal verbs express ability, obligation, permission, possibility and advice."
      "|Can expresses ability or possibility : the technician can test the circuit."
      "|Must expresses a strong obligation : you must wear protective gloves."
      "|Have to also expresses obligation, often because of an external rule."
      "|Should expresses advice or a recommendation, weaker than must."
      "|May expresses permission or a possibility : the fault may be in the cable."
      "|Modals are followed by the base form of the verb, without to."
      "|The negative of must is must not or mustn't, which expresses prohibition."
      "|The negative of have to is do not have to, which means it is not necessary."
      "|In safety instructions, must and must not are essential to avoid ambiguity."
      "|An imperative sentence gives a direct order : Switch off the power."
      "|Understanding modals is necessary to follow an English safety notice correctly."),
    [QC("Which modal expresses ability ?", "Must~Can~Should~May", 1,
        "Can expresses ability or possibility : he can read a wiring diagram."),
     QC("Which modal expresses a strong obligation ?", "Can~May~Must~Might", 2,
        "Must expresses an obligation imposed by the speaker or by a rule."),
     QC("What form follows a modal verb ?", "The -ing form~The past form~The base form~The -s form", 2,
        "Modals are followed by the base form : you must check, not you must checks."),
     QC("What does 'must not' express ?", "A recommendation~A prohibition~An ability~A possibility", 1,
        "Must not or mustn't expresses something that is forbidden."),
     QC("Which expression means that something is not necessary ?", "Must not~Do not have to~Can not~Should not", 1,
        "Do not have to means there is no obligation, unlike must not which forbids."),
     QC("Which modal gives advice ?", "Must~Should~Can~Will", 1,
        "Should gives advice or a recommendation, less strong than must."),
     QC("How is a direct order usually formed in a manual ?", "With a modal only~With the imperative~With the passive and would~With a question", 1,
        "The imperative gives a direct instruction : Isolate the supply before working."),
     QT("Explain the difference between 'You must not touch the terminals' and 'You do not have to touch the terminals'.",
        "The first sentence is a prohibition : touching the terminals is forbidden, even if the power seems to be off. The second sentence means there is no obligation to touch them, but it does not forbid it. Confusing the two could lead to a serious safety error. In a safety notice, must not is used for actions that are dangerous, while do not have to is used for optional actions. A technician must read this distinction carefully before starting work.",
        "The answer must distinguish prohibition from absence of obligation."),
     QT("Rewrite these instructions using the correct modal : '(advice) wear glasses', '(obligation) isolate the supply', '(possibility) the fuse is faulty'.",
        "Advice is expressed with should : You should wear glasses. A strong obligation is expressed with must : You must isolate the supply. A possibility is expressed with may or might : The fuse may be faulty. In each case, the modal is followed by the base form of the verb without to. These three modals give different levels of certainty or constraint, which is why they are chosen carefully in technical documentation.",
        "The expected answer is should wear, must isolate, may be, with the base form after each modal.")],
    C("Modals grade obligation, advice and possibility : they are followed by the base form of the verb.",
      "must = obligation · should = advice · may = possibility · can = ability",
      "must not = prohibition · do not have to = no obligation",
      "Must~Strong obligation~Must check~Should~Advice~Should test~May~Possibility~May fail",
      "Identify the intended meaning|Choose the right modal|Use the base form|Check negative meaning|Apply to a safety instruction",
      "Using to after a modal|Confusing must not and do not have to|Using must for simple advice|Forgetting the base form",
      "Must wear~Safety obligation~Should check~Recommendation~May be faulty~Possible cause~Switch off~Imperative order",
      "Must~Obligation imposed by the speaker~Have to~Obligation from a rule~Should~Advice or recommendation~May~Permission or possibility",
      "Must not~Forbidden action~Do not have to~Optional action~Can not~Unable or not allowed"))

# ============================================================ EN3
add("PE-A17", "Describing a workplace and safety rules in English", "Anglais", ["Terminale pro"],
    S("A workplace description states where people work, what equipment they use and what rules apply."
      "|There is and there are are used to introduce the presence of objects or people."
      "|The present simple describes permanent features : the workshop has two benches."
      "|The passive voice is common in procedures : the cable is connected to the terminal."
      "|Safety rules often use must, must not and the imperative."
      "|Personal protective equipment is called PPE in English."
      "|A risk assessment identifies hazards and the measures taken to reduce them."
      "|An incident report uses the past simple to describe what happened."
      "|Technical vocabulary includes switchboard, breaker, fuse, earth, cable and terminal."
      "|Prepositions of place such as on, under, next to and behind locate objects precisely."
      "|A short report is organised with a heading, facts, consequences and actions taken."
      "|Clear writing avoids vague words and gives exact values, times and positions."),
    [QC("Which structure introduces the presence of an object ?", "There is~It has~This is~They are", 0,
        "There is a fuse in the distribution board introduces an object."),
     QC("What does PPE stand for ?", "Power Point Equipment~Personal Protective Equipment~Primary Power Element~Portable Protection Element", 1,
        "PPE means Personal Protective Equipment : gloves, goggles, helmet and boots."),
     QC("Which voice is frequent in technical procedures ?", "Active~Passive~Continuous~Perfect", 1,
        "The passive focuses on the action : the cable is connected to the terminal."),
     QC("Which tense is used in an incident report ?", "Present simple~Past simple~Future~Present continuous", 1,
        "An incident report relates completed facts and uses the past simple."),
     QC("Which preposition means 'à côté de' ?", "Under~Next to~Behind~On", 1,
        "Next to means beside or à côté de."),
     QC("What is a risk assessment ?", "A list of tools~An identification of hazards and protective measures~A salary document~A timetable", 1,
        "A risk assessment identifies hazards and the measures taken to reduce them."),
     QC("What should a clear technical report contain ?", "Vague comments only~Exact values, times and positions~Only opinions~Long descriptions without facts", 1,
        "Precision is essential : values, times, positions and actions taken."),
     QT("Describe a small electrical workshop in English in three or four sentences.",
        "The workshop has two benches and a testing area. There is a distribution board on the wall next to the door. The technicians must wear PPE when they work on a live circuit. The cables are stored in a cabinet behind the bench, and the earth connection is checked every morning. These sentences combine there is, the present simple for permanent features, a modal for the safety rule and the passive for a repeated procedure.",
        "The answer should use there is or there are, a present simple description, a safety modal and a preposition of place."),
     QT("Write a short incident report in English using the past simple.",
        "Yesterday morning, a technician noticed a burnt smell near the distribution board. He isolated the supply and informed the supervisor. The team checked the circuit and found a loose connection on terminal 3. They replaced the cable and tested the installation before re-energising it. No one was injured. The report states the facts in chronological order, gives precise details and ends with the action taken.",
        "The expected answer uses past simple verbs, a chronological order and precise facts.")],
    C("Technical English combines precise vocabulary, passive procedures and clear safety rules.",
      "There is / there are · passive voice · must and must not",
      "PPE · risk assessment · incident report · past simple for facts",
      "Workshop~Place of work~Benches and tools~Distribution board~Electrical panel~Breakers and fuses~PPE~Protective equipment~Gloves and goggles",
      "List the objects and their positions|Use there is or there are|State the safety rules|Describe the procedure in passive form|Report past events in order",
      "Using vague words such as something|Mixing present and past without reason|Forgetting the article|Omitting safety rules",
      "Next to~À côté de~Under~Dessous~Behind~Derrière~On~Sur~PPE~Personal Protective Equipment",
      "Active voice~Technician checks the cable~Focus on the person~Passive voice~The cable is checked~Focus on the action~Procedure~Steps in a manual",
      "There is~Singular object~There are~Plural objects~Has got~Possession or feature"))

# ============================================================ EMC1
add("PE-A18", "Les institutions de la Ve République et la citoyenneté", "EMC", ["2nde pro"],
    S("L'État de droit garantit que les pouvoirs publics agissent selon des règles connues et contrôlées."
      "|La Constitution de 1958 organise les pouvoirs de la Ve République."
      "|Le pouvoir exécutif est exercé par le président de la République et le Premier ministre."
      "|Le pouvoir législatif appartient au Parlement, qui vote la loi."
      "|Le pouvoir judiciaire est rendu au nom du peuple par les tribunaux."
      "|La séparation des pouvoirs évite la concentration de l'autorité entre les mêmes mains."
      "|Le référendum permet au peuple de se prononcer directement sur une question."
      "|Le suffrage universel donne le droit de vote à tous les citoyens majeurs."
      "|Les élections locales, nationales et européennes permettent de choisir des représentants."
      "|Un citoyen respecte les lois, paie ses impôts et peut participer à la vie publique."
      "|La liberté d'expression permet de manifester ses opinions dans le respect d'autrui."
      "|Comprendre ces institutions aide à situer l'action de l'administration et de l'entreprise."),
    [QC("Quel texte organise les pouvoirs de la Ve République ?", "La Déclaration de 1789~La Constitution de 1958~Le Code du travail~Le traité de Rome", 1,
        "La Constitution du 4 octobre 1958 est celle de la Ve République."),
     QC("Qui exerce le pouvoir législatif ?", "Le président~Le Parlement~Le Conseil d'État~Le préfet", 1,
        "Le Parlement, composé de l'Assemblée nationale et du Sénat, vote la loi."),
     QC("Que garantit un État de droit ?", "L'absence de lois~L'action des pouvoirs selon des règles connues~Le pouvoir du plus fort~La suppression des tribunaux", 1,
        "Dans un État de droit, les pouvoirs sont encadrés par le droit et contrôlés."),
     QC("À quoi sert la séparation des pouvoirs ?", "À concentrer l'autorité~À éviter la concentration des pouvoirs~À supprimer les élections~À remplacer la Constitution", 1,
        "La séparation des pouvoirs est une garantie contre l'arbitraire."),
     QC("Comment le peuple peut-il se prononcer directement ?", "Par le référendum~Par le Conseil constitutionnel~Par le préfet~Par la Cour de cassation", 0,
        "Le référendum est une consultation directe des citoyens."),
     QC("Qui peut voter en France ?", "Tous les habitants sans condition~Tous les citoyens majeurs inscrits~Les seuls fonctionnaires~Les élus locaux", 1,
        "Le suffrage universel s'applique aux citoyens majeurs inscrits sur les listes électorales."),
     QC("Quel devoir du citoyen consiste à respecter les règles communes ?", "Paier ses impôts~Respecter les lois~Voyager~Posséder une entreprise", 1,
        "Le respect des lois est un devoir essentiel de la citoyenneté."),
     QT("Expliquer l'intérêt de la séparation des pouvoirs dans un État de droit.",
        "La séparation des pouvoirs répartit l'autorité entre des organes distincts : le Parlement vote la loi, le gouvernement l'exécute et les tribunaux la font respecter. Ainsi, aucun organe ne peut à la fois décider, appliquer et juger une même affaire. Ce mécanisme limite le risque d'arbitraire et protège les libertés des citoyens. Les contrôles réciproques, comme celui du Conseil constitutionnel, renforcent cette garantie en vérifiant que les lois restent conformes à la Constitution.",
        "On attend la définition des trois pouvoirs et le lien avec la protection des libertés."),
     QT("Comment un citoyen peut-il participer à la vie de la cité ?",
        "Il peut s'inscrire sur les listes électorales et voter lors des élections locales, nationales ou européennes. Il peut s'informer, débattre, exprimer son opinion dans le respect d'autrui et adhérer à une association ou un syndicat. Il peut aussi interpeller ses élus, participer à une consultation ou à un référendum, et respecter les lois ainsi que les devoirs fiscaux. La participation ne se limite donc pas au vote : elle comprend l'information, le dialogue et l'engagement collectif.",
        "La réponse doit mentionner le vote et d'autres formes d'engagement, ainsi que le respect des lois.")],
    C("L'État de droit organise et limite les pouvoirs pour protéger les libertés des citoyens.",
      "Exécutif + législatif + judiciaire = séparation des pouvoirs",
      "Constitution 1958 · suffrage universel · référendum · devoirs du citoyen",
      "Pouvoir exécutif~Président et gouvernement~Applique la loi~Pouvoir législatif~Parlement~Vote la loi~Pouvoir judiciaire~Tribunaux~Juge les litiges",
      "Identifier le type de pouvoir|Relier un organe à sa fonction|Comprendre les contrôles|Repérer les droits et devoirs|Illustrer par une situation concrète",
      "Confondre pouvoir législatif et judiciaire|Croire que le préfet vote la loi|Oublier les devoirs du citoyen|Ignorer le rôle du Conseil constitutionnel",
      "Président~Exécutif~Parlement~Législatif~Tribunal~Judiciaire~Référendum~Vote direct~Suffrage universel~Droit de vote",
      "État de droit~Pouvoirs encadrés par le droit~État autoritaire~Pouvoir sans contrôle~Séparation des pouvoirs~Organes distincts~Concentration~Un seul organe décide",
      "Droit~Liberté garantie~Devoir~Obligation du citoyen~Citoyenneté~Participation et respect des lois"))

# ============================================================ EMC2
add("PE-A19", "Droits, devoirs et vie collective", "EMC", ["1re pro"],
    S("Les droits de la personne sont énoncés dans la Déclaration universelle des droits de l'homme de 1948."
      "|En France, les libertés fondamentales sont garanties par la Constitution et le Conseil constitutionnel."
      "|La liberté d'expression, de réunion et d'association permet la vie démocratique."
      "|Le droit à l'éducation et le droit au travail figurent parmi les droits économiques et sociaux."
      "|Les devoirs sont la contrepartie des droits : respecter les lois, autrui et les biens communs."
      "|La laïcité garantit la liberté de conscience et l'égalité de tous devant la loi."
      "|L'égalité entre les femmes et les hommes est un principe constitutionnel."
      "|La discrimination consiste à traiter différemment une personne sur un critère interdit par la loi."
      "|La solidarité se manifeste par la sécurité sociale, l'école publique et les services publics."
      "|Un conflit collectif se règle par le dialogue, la négociation ou les tribunaux."
      "|Dans l'entreprise, le règlement intérieur précise les droits et les obligations de chacun."
      "|Ces principes fondent le vivre-ensemble et le respect des règles sur un chantier."),
    [QC("Quand la Déclaration universelle des droits de l'homme a-t-elle été adoptée ?", "1789~1948~1958~2000", 1,
        "Elle a été adoptée par l'ONU le 10 décembre 1948."),
     QC("Que garantit la laïcité ?", "Une religion d'État~La liberté de conscience et l'égalité devant la loi~L'interdiction de toute croyance~Le pouvoir des prêtres", 1,
        "La laïcité protège la liberté de croire ou de ne pas croire et l'égalité de tous."),
     QC("Qu'appelle-t-on une discrimination ?", "Un traitement égal pour tous~Un traitement different fondé sur un critère interdit~Une sanction justifiée~Un service public", 1,
        "La discrimination exclut ou désavantage une personne sur un critère prohibé par la loi."),
     QC("Quel est un devoir du citoyen ?", "Respecter les lois~Choisir sa religion imposée~Éviter de voter~Refuser de payer des impôts", 0,
        "Le respect des lois est un devoir fondamental de la citoyenneté."),
     QC("Quel principe oppose-t-on à la discrimination ?", "L'exclusion~L'égalité~La hiérarchie~Le privilège", 1,
        "L'égalité devant la loi est le principe qui s'oppose à la discrimination."),
     QC("Quel service public illustre la solidarité nationale ?", "Un club privé~L'école publique~Une boutique~Un restaurant", 1,
        "L'école publique et la sécurité sociale sont des services publics fondés sur la solidarité."),
     QC("Où trouve-t-on les obligations des salariés dans une entreprise ?", "Dans le règlement intérieur~Dans un manuel de câblage~Dans une facture~Dans un plan de vote", 0,
        "Le règlement intérieur définit les règles de vie et de sécurité dans l'entreprise."),
     QT("Expliquer la relation entre droits et devoirs dans une démocratie.",
        "Un droit est une liberté ou une protection reconnue à chacun, comme la liberté d'expression ou le droit à l'éducation. Un devoir est une obligation qui permet à ces droits d'être exercés par tous : respecter la loi, ne pas porter atteinte à autrui, contribuer aux charges communes. Sans devoirs, les droits de certains empêcheraient ceux des autres. Les citoyens acceptent les deux : ils jouissent de protections et acceptent des contraintes. Cette réciprocité est la condition d'une vie collective paisible.",
        "On attend l'idée de réciprocité : les devoirs rendent possible l'exercice des droits par tous."),
     QT("Comment prévenir une discrimination dans un collectif de travail ?",
        "On commence par connaître les critères interdits par la loi et par refuser tout préjugé. On applique les mêmes règles à tous : même accès à la formation, mêmes consignes de sécurité, mêmes critères d'évaluation. On signale les propos ou les comportements inappropriés au responsable ou au référent. On veille à ce que les consignes soient comprises par tous, quelle que soit la langue ou la situation de la personne. Enfin, on documente les faits si un désaccord persiste, afin de permettre un traitement juste et contradictoire.",
        "La réponse doit proposer des mesures concrètes : règles égales, signalement, compréhension et documentation.")],
    C("Droits et devoirs sont liés : la vie collective exerce des libertés dans le respect d'autrui.",
      "Droits de la personne + devoirs = vivre-ensemble",
      "Déclaration de 1948 · laïcité · égalité · solidarité · règlement intérieur",
      "Droit~Liberté protégée~Liberté d'expression~Devoir~Obligation citoyenne~Respect des lois~Laïcité~Liberté de conscience~Neutralité",
      "Repérer le droit ou le devoir en cause|Vérifier l'égalité de traitement|Identifier la règle applicable|Signaler un comportement inadapté|Documenter les faits",
      "Confondre liberté et licence|Ignorer les critères de discrimination|Croire que la laïcité interdit les croyances|Oublier le règlement intérieur",
      "1948~Déclaration universelle~Égalité~Principe constitutionnel~Laïcité~Liberté de conscience~Solidarité~Services publics",
      "Égalité~Même traitement devant la loi~Discrimination~Traitement inégal et interdit~Solidarité~Entraide et service public~Liberté~Possibilité d'agir",
      "Droits~Protections reconnues~Devoirs~Obligations correspondantes~Réciprocité~Condition du vivre-ensemble"))

# ============================================================ EMC3
add("PE-A20", "La laïcité et le vivre-ensemble au quotidien", "EMC", ["Terminale pro"],
    S("La laïcité est un principe qui organise la liberté de conscience dans l'espace public."
      "|La loi du 9 décembre 1905 sépare les Églises et l'État."
      "|L'État ne finance pas de culte et ne reconnaît pas de religion officielle."
      "|La laïcité garantit à chacun la liberté de croire, de ne pas croire ou de changer de religion."
      "|Elle impose une neutralité stricte aux agents publics dans l'exercice de leurs fonctions."
      "|Les usagers des services publics doivent être traités sans discrimination."
      "|Dans l'entreprise privée, la liberté d'expression existe mais doit respecter la neutralité du service."
      "|Le respect d'autrui implique d'éviter les propos injurieux ou discriminatoires."
      "|Les signes religieux sont encadrés dans certains contextes scolaires et professionnels."
      "|Le vivre-ensemble repose sur la connaissance des règles et le dialogue."
      "|Un désaccord se traite par l'écoute, la médiation et, si besoin, le droit."
      "|Sur un chantier, la laïcité contribue à un climat de travail respectueux et efficace."),
    [QC("Quelle loi consacre la séparation des Églises et de l'État en France ?", "La loi du 9 décembre 1905~La Constitution de 1958~La loi du 29 juillet 1881~Le Code civil de 1804", 0,
        "La loi de séparation des Églises et de l'État date du 9 décembre 1905."),
     QC("Que garantit la laïcité ?", "Une religion d'État~La liberté de conscience de chacun~L'interdiction des croyances~Le financement des cultes", 1,
        "La laïcité protège la liberté de croire ou de ne pas croire."),
     QC("À qui s'impose une neutralité stricte dans l'exercice des fonctions ?", "À tous les citoyens~Aux agents publics~Aux seuls élus~Aux entreprises privées", 1,
        "Les agents publics sont tenus à une neutralité stricte pendant leur service."),
     QC("L'État peut-il financer un culte ?", "Oui, toujours~Non, en vertu de la séparation~Oui, sur demande~Seulement les grandes religions", 1,
        "La séparation interdit le financement public des cultes."),
     QC("Quel comportement nuisible au vivre-ensemble faut-il éviter ?", "Le dialogue~Les propos injurieux~La médiation~L'écoute", 1,
        "Les propos injurieux ou discriminatoires portent atteinte au respect d'autrui."),
     QC("Comment résoudre un désaccord lié à des convictions ?", "Par l'exclusion~Par l'écoute et la médiation~Par la force~En l'ignorant", 1,
        "L'écoute et la médiation permettent de traiter le désaccord dans le respect du droit."),
     QC("Quel effet la laïcité a-t-elle sur un collectif de travail ?", "Elle crée des privilèges~Elle favorise un climat respectueux~Elle interdit tout débat~Elle supprime les règles", 1,
        "En garantissant l'égalité et la liberté de conscience, elle contribue à un climat de travail respectueux."),
     QT("Expliquer en quoi la laïcité protège à la fois les croyants et les non-croyants.",
        "La laïcité ne supprime pas les religions : elle empêche qu'une religion impose ses règles à l'État et à la société. Les croyants peuvent pratiquer leur culte librement et ne sont pas favorisés ni pénalisés. Les non-croyants ne sont pas obligés de se conformer à une croyance dominante et sont traités de la même manière dans les services publics. En garantissant l'égalité de tous devant la loi et la liberté de conscience, la laïcité protège chaque personne, quelle que soit sa position philosophique.",
        "On attend l'idée d'égalité de traitement et de liberté pour tous les choix de conscience."),
     QT("Un collaborateur se plaint d'un propos injurieux lié à ses convictions. Décrire la démarche à adopter.",
        "On écoute d'abord la personne sans minimiser son ressenti et on note les faits précis : date, lieu, mots employés, témoins. On vérifie s'il s'agit d'un propos injurieux ou discriminatoire au regard du règlement intérieur et de la loi. On oriente la personne vers le responsable hiérarchique, le référent ou le service des ressources humaines. On veille à ce qu'aucune représaille n'ait lieu. Si les faits sont établis, une sanction peut être prononcée ; sinon, une médiation peut restaurer le dialogue. Chaque étape est documentée pour garantir un traitement juste.",
        "La réponse doit proposer écoute, relevé des faits, signalement, protection contre les représailles et suite adaptée.")],
    C("La laïcité garantit la liberté de conscience et l'égalité de traitement dans l'espace public et au travail.",
      "Loi du 9 décembre 1905 · liberté de conscience · neutralité des agents publics",
      "Égalité · respect d'autrui · médiation · règlement intérieur",
      "Loi de 1905~Séparation des Églises et de l'État~Neutralité de l'État~Liberté de conscience~Croire ou ne pas croire~Respect de tous~Agent public~Neutralité stricte~Service public",
      "Connaître le principe de laïcité|Repérer la situation et les personnes|Vérifier les règles applicables|Écouter et documenter les faits|Orienter vers la médiation ou le droit",
      "Croire que la laïcité interdit la religion|Confondre neutralité de l'État et neutralité des usagers|Ignorer les propos injurieux|Agir sans conserver de preuve",
      "1905~Loi de séparation~Agent public~Neutralité stricte~Usager~Égalité de traitement~Médiation~Résolution du conflit",
      "Laïcité~Liberté de conscience et égalité~Intolérance~Refus de l'autre~Neutralité~Absence de prise de position~Respect d'autrui~Écoute et considération",
      "Espace public~Règles communes~Espace privé~Liberté individuelle~Milieu professionnel~Règlement intérieur"))

valider_et_ecrire(F, "pro-electricite-mat-part-A.json")
