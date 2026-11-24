# PARTIE B — spécialités littéraires (HLP, LLCE, LCA, Arts)
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lg_common import f, q, t, a, save

F, AN = [], []

SHLP1 = "Programme de spécialité HLP de première générale, arrêté du 17 janvier 2019, BO spécial n° 1 du 22 janvier 2019, éduscol"
SHLP2 = "Programme de spécialité HLP de terminale générale, arrêté du 19 juillet 2019, BO spécial n° 8 du 25 juillet 2019, éduscol"
SLL = "Programme de spécialité LLCER, BO spécial n° 8 du 25 juillet 2019 ; programme limitatif 2026-2027, BO n° 21 du 22 mai 2026, éduscol"
SLCA = "Programme de spécialité langues et cultures de l'Antiquité (latin, grec), BO spéciaux n° 1 du 22 janvier 2019 et n° 8 du 25 juillet 2019, éduscol"
SART1 = "Programme de spécialité arts plastiques de première, BO spécial n° 1 du 22 janvier 2019 ; programmes limitatifs 2026, BO n° 4 du 22 janvier 2026, éduscol"
SART2 = "Programme de spécialité arts plastiques de terminale, BO spécial n° 8 du 25 juillet 2019 ; programmes limitatifs 2026, BO n° 4 du 22 janvier 2026, éduscol"
SMUS = "Programme de spécialité musique, BO spéciaux n° 1 du 22 janvier 2019 et n° 8 du 25 juillet 2019 ; arrêté du 2 mars 2020, éduscol"

# ---------------- HLP ----------------
F.append(f(["1re"], "HLP", "Chapitre : Les pouvoirs de la parole – rhétorique et éloquence dans l'Antiquité", SHLP1, [
 "Le premier objet d'étude de première, « Les pouvoirs de la parole », se décline en trois entrées : l'art de la parole, son autorité, ses séductions ; il couvre l'Antiquité et l'âge classique.",
 "La rhétorique est théorisée par Aristote dans la Rhétorique (IVe siècle av. J.-C.) : elle distingue trois genres de discours – judiciaire, délibératif, épidictique – selon le temps (passé, futur, présent) et la finalité (accuser/défendre, convaincre, louer/blâmer).",
 "Cicéron, dans De Oratore (55 av. J.-C.), transpose la rhétorique grecque à Rome et définit cinq parties du discours : invention, disposition, élocution, mémoire et action.",
 "Quintilien, dans les Institutiones oratoriae (Ier siècle apr. J.-C.), systématise la formation de l'orateur : grammaire, lecture, exercices de déclamation et maîtrise du geste.",
 "L'idéal cicéronien se résume dans la formule « instruire, plaire, émouvoir » (docere, delectare, movere) : le discours doit convaincre par la raison tout en touchant l'auditoire.",
 "Les sophistes, dont Protagoras et Gorgias, sont soupçonnés de faire de la parole un commerce : Platon les attaque dans le Gorgias et oppose la vraie rhétorique, qui vise le bien de l'âme, à la flatterie.",
 "Dans le Phèdre, Platon critique l'écriture comme un simulacre de parole vivante : seule la parole prononcée devant un auditoire peut répondre et s'adapter.",
 "Le programme invite à comparer les trois registres de persuasion : l'ethos (caractère de l'orateur), le pathos (émotion de l'auditoire) et le logos (argument rationnel), déjà distingués par Aristote.",
 "L'étude des discours (Cicéron, Contre Catilina ; Démosthène, Contre Philippe) demande de repérer les figures, la progression de l'argument et l'effet visé sur l'assemblée.",
 "La question centrale de l'objet est politique : qui détient le pouvoir de la parole, et comment cette parole devient-elle une autorité ou une séduction ?"
], [
 q("Combien la rhétorique classique distingue-t-elle de parties du discours ?", ["Trois", "Cinq", "Sept", "Douze"], 1, "Les cinq parties sont l'invention, la disposition, l'élocution, la mémoire et l'action."),
 q("Quel est l'auteur de De Oratore ?", ["Quintilien", "Cicéron", "Aristote", "Démosthène"], 1, "Cicéron publie De Oratore en 55 av. J.-C., dialogue où il définit l'orateur idéal."),
 q("Quels sont les trois genres de discours chez Aristote ?", ["Judiciaire, délibératif, épidictique", "Épique, lyrique, dramatique", "Narratif, descriptif, argumentatif", "Public, privé, sacré"], 0, "Le genre judiciaire juge le passé, le délibératif concerne le futur, l'épidictique loue ou blâme au présent."),
 q("Que désigne le « logos » dans la persuasion aristotélicienne ?", ["Le caractère de l'orateur", "L'émotion de l'auditoire", "L'argument rationnel", "Le rythme de la voix"], 2, "Aristote distingue ethos (caractère), pathos (émotion) et logos (raisonnement)."),
 q("Quelle critique Platon adresse-t-il à l'écriture dans le Phèdre ?", ["Elle est trop lente", "Elle est un simulacre de parole vivante", "Elle est réservée aux esclaves", "Elle détruit la mémoire"], 1, "Socrate reproche à l'écriture de ne pas pouvoir répondre aux questions : elle imite la parole sans la remplacer."),
 t("Quelle différence le programme établit-il entre convaincre et séduire ?", "Convaincre s'adresse à la raison par des arguments ; séduire agit sur le plaisir et l'émotion.", "L'entrée « Les séductions de la parole » étudie la fable, l'allégorie et la déclaration amoureuse ; elle pose la limite entre persuasion et manipulation, dénoncée par le procès des sophistes."),
 t("Comment la formule « docere, delectare, movere » résume-t-elle l'idéal oratoire ?", "L'orateur doit instruire, plaire et émouvoir son auditoire.", "Ces trois finalités hiérarchisent les moyens du discours : la vérité reste le but, le plaisir et l'émotion sont des moyens de la faire accepter."),
 t("Pourquoi l'étude de la parole est-elle politique ?", "Parce que celui qui maîtrise la parole peut orienter le jugement et la décision de la cité.", "Dans la démocratie athénienne comme dans la Rome républicaine, l'agora et le Sénat sont des lieux où le discours produit de l'autorité et du pouvoir.")
])),

F.append(f(["1re"], "HLP", "Chapitre : Représentations du monde – voyage, utopie et regard sur l'Europe", SHLP1, [
 "Le second objet de première, « Les représentations du monde » (Renaissance, âge classique, Lumières), comporte les entrées « Découverte du monde et pluralité des cultures », « Décrire, figurer, imaginer » et « L'homme et l'animal ».",
 "Les grands voyages maritimes (Colomb, 1492 ; Magellan, 1519-1522) et la révolution astronomique de Copernic (De revolutionibus, 1543) et Galilée déplacent le centre du monde et élargissent l'horizon connu.",
 "Les récits de voyage (Jean de Léry, Histoire d'un voyage fait en la terre du Brésil, 1578) mêlent observation ethnographique et jugement ethnocentrique.",
 "Thomas More publie Utopia en 1516 et Campanella La Cité du soleil en 1602 : ces fictions situées dans un ailleurs imaginaire servent à critiquer les sociétés européennes.",
 "Montaigne, dans les Essais (I, 31, « Des cannibales », 1580), inverse le regard ethnographique : les mœurs amérindiennes y sont jugées plus justes que celles de l'Europe de la conquête.",
 "La carte, le plan et la figure géométrique deviennent des modes de représentation du monde : la projection de Mercator (1569) simplifie la navigation mais déforme les surfaces.",
 "L'entrée « L'homme et l'animal » confronte les classifications de Buffon et Linné aux récits de voyage qui attribuent aux animaux des comportements sociaux et moraux.",
 "La fable et le bestiaire (La Fontaine, Fables, 1668-1694) utilisent l'animal pour discourir sur la condition humaine et la politique, dans la lignée d'Ésope.",
 "Le programme invite à interroger la fiabilité des témoignages de voyage : entre observation, merveilleux et idéologie coloniale, la description est toujours une construction.",
 "L'enjeu de l'objet est de comprendre comment la découverte de l'altérité a transformé la pensée européenne sur elle-même, préparant le relativisme des Lumières."
], [
 q("Quel est l'auteur d'Utopia, paru en 1516 ?", ["Thomas More", "Campanella", "Montaigne", "Copernic"], 0, "Thomas More, humaniste anglais, publie Utopia en 1516 ; Campanella écrit La Cité du soleil en 1602."),
 q("Dans quel chapitre des Essais Montaigne parle-t-il des cannibales ?", ["Livre I, chapitre 31", "Livre II, chapitre 12", "Livre III, chapitre 9", "Livre I, chapitre 1"], 0, "« Des cannibales » est le chapitre 31 du premier livre des Essais (1580)."),
 q("Qui a proposé une projection cartographique en 1569 ?", ["Copernic", "Mercator", "Galilée", "Linné"], 1, "Gerardus Mercator publie sa projection cylindrique conforme en 1569 ; elle conserve les angles mais agrandit les hautes latitudes."),
 q("Quel naturaliste a classé les êtres vivants dans le Systema Naturae ?", ["Buffon", "Linné", "Lamarck", "Cuvier"], 1, "Carl von Linné publie Systema Naturae en 1735 et popularise la nomenclature binomiale."),
 q("Quelle est la fonction de l'utopie selon le programme ?", ["Décrire un pays réel", "Critiquer la société présente en l'imaginant ailleurs", "Raconter un voyage maritime", "Classifier les animaux"], 1, "L'utopie déplace le regard : le « nulle part » (outopos) devient un miroir critique de l'Europe."),
 t("Comment Montaigne utilise-t-il le « nouveau monde » dans les Essais ?", "Il compare les mœurs amérindiennes aux coutumes européennes pour relativiser la prétendue supériorité de l'Europe.", "Le chapitre « Des cannibales » retourne le regard colonial : la « barbarie » est renvoyée à l'Europe des conquêtes, fondant un relativisme culturel."),
 t("Quelle est la différence entre récit de voyage et utopie ?", "Le récit prétend témoigner d'un pays réel ; l'utopie invente une société imaginaire pour critiquer la sienne.", "Les deux genres se répondent : le voyage fournit la matière de l'ailleurs, l'utopie en fait un outil politique et philosophique."),
 t("Pourquoi faut-il se méfier des récits de voyage ?", "Parce qu'ils mêlent observation, merveilleux et préjugés ethnocentriques.", "Le témoignage est toujours orienté par la culture de l'observateur et par le public auquel il s'adresse ; l'historien doit confronter les sources.")
])),

F.append(f(["Terminale"], "HLP", "Chapitre : La recherche de soi – éducation, sensibilité et métamorphoses du moi", SHLP2, [
 "En terminale, l'enseignement de spécialité HLP (6 heures hebdomadaires) s'organise autour de deux objets : « La recherche de soi », du romantisme au XXe siècle, et « L'humanité en question » à l'époque contemporaine.",
 "L'entrée « Éducation, transmission, émancipation » confronte les modèles pédagogiques depuis les Lumières : Rousseau (Émile, 1762), Condorcet (Esquisse d'un tableau historique des progrès de l'esprit humain, 1795) et les récits d'écoliers du XIXe siècle.",
 "L'école républicaine (lois Ferry, 1881-1882) devient un enjeu de justice sociale : le programme lit les récits d'apprentissage et d'échec scolaire comme des révélateurs des inégalités.",
 "L'entrée « Les expressions de la sensibilité » étudie la revendication des droits du sentiment dans les romantismes européens (Goethe, Werther, 1774 ; Chateaubriand, René, 1802).",
 "La sensibilité n'est pas seulement un thème : elle transforme la forme littéraire (journal intime, poésie lyrique, roman d'analyse) et la manière de représenter la conscience.",
 "Bergson (Essai sur les données immédiates de la conscience, 1889) oppose la durée vécue, qualitative, au temps mesurable de la science : le moi intérieur est un continuum.",
 "La psychanalyse freudienne déloge le sujet de la transparence : le moi est traversé par des désirs inconscients et par l'histoire de l'enfance.",
 "L'entrée « Les métamorphoses du moi » interroge l'unité du sujet : chez Proust (À la recherche du temps perdu), le « moi » est à la fois continuité et reconstruction par la mémoire.",
 "Le programme demande de confronter récits d'enfance, autobiographies et fictions pour comprendre comment s'écrit et se réécrit une identité.",
 "La problématique centrale : la recherche de soi est-elle une découverte d'une essence cachée ou une construction permanente par le langage et le regard d'autrui ?"
], [
 q("Quel ouvrage de Rousseau paru en 1762 traite de l'éducation ?", ["Du contrat social", "Émile", "Les Confessions", "La Nouvelle Héloïse"], 1, "Émile ou De l'éducation expose une pédagogie fondée sur le développement naturel de l'enfant."),
 q("Qui a publié un Essai sur les données immédiates de la conscience en 1889 ?", ["Bergson", "Freud", "Proust", "Sartre"], 0, "Henri Bergson y distingue la durée vécue du temps quantifié de la science."),
 q("Quel roman de Goethe incarnation du romantisme européen paraît en 1774 ?", ["Werther", "René", "Les Souffrances du jeune Werther", "Wilhelm Meister"], 0, "Werther (1774) connaît un succès européen et fait du sentiment une valeur souveraine."),
 q("Que désigne l'entrée « Les métamorphoses du moi » ?", ["L'étude des insectes", "L'unité et l'identité du sujet", "La croissance des villes", "L'évolution des genres"], 1, "Elle interroge la continuité et les transformations de la subjectivité du long XIXe siècle au XXe siècle."),
 q("Quel apport la psychanalyse a-t-elle au récit de soi ?", ["Elle supprime le récit", "Elle révèle l'inconscient et l'importance de l'enfance", "Elle interdit l'autobiographie", "Elle remplace la mémoire par l'histoire"], 1, "Freud montre que le moi n'est pas transparent à lui-même et que le passé infantile structure la vie adulte."),
 t("Comment l'école est-elle un enjeu d'émancipation dans le programme ?", "Parce qu'elle transmet des savoirs et peut corriger les inégalités d'origine, tout en les révélant.", "Les récits d'écoliers montrent l'ambivalence de l'institution scolaire : elle promet la réussite mais sélectionne aussi selon l'origine sociale."),
 t("Qu'est-ce que la « durée » chez Bergson ?", "Un temps vécu, qualitatif et continu, distinct du temps mesurable des horloges.", "La durée est le milieu de la conscience : elle ne se divise pas en instants identiques et rend compte de la liberté et de la création."),
 t("En quoi la recherche de soi est-elle une construction ?", "Le sujet se raconte à travers des langages, des souvenirs et le regard d'autrui, plutôt qu'il ne découvre une essence toute faite.", "Le programme confronte autobiographie, journal intime et fiction pour montrer que l'identité est une mise en récit toujours révisable.")
])),

F.append(f(["Terminale"], "HLP", "Chapitre : L'humanité en question – création, violence et limites de l'humain", SHLP2, [
 "Le second objet de terminale, « L'humanité en question », se divise en trois entrées : « Création, continuités et ruptures », « Histoire et violence », « L'humain et ses limites ».",
 "La première entrée interroge les avant-gardes du XXe siècle et l'idée de crise de la rationalité : la rupture est-elle réellement radicale en art et en pensée, ou prolonge-t-elle des questionnements plus anciens ?",
 "La deuxième entrée confronte les grands traumatismes du siècle à leur représentation littéraire : Primo Levi (Si c'est un homme, 1947), Jorge Semprún et Hannah Arendt font de la violence un objet de réflexion politique.",
 "Le témoignage pose un problème de forme : comment dire l'indicible ? Le programme confronte récits concentrationnaires, journaux et textes philosophiques sur la « banalité du mal ».",
 "Hannah Arendt (Eichmann à Jérusalem, 1963) soutient que le mal totalitaire peut être le fait de fonctionnaires ordinaires, sans haine personnelle, par soumission à la règle.",
 "La troisième entrée étudie l'extension des capacités humaines par la technique et la question écologique : Hans Jonas (Le Principe responsabilité, 1979) formule une éthique de la précaution envers les générations futures.",
 "Gilbert Simondon (L'Individuation à la lumière des notions de forme et d'information, 1965) renouvelle la pensée de la technique et de l'individuation, en refusant de séparer l'homme et la machine.",
 "Le programme aborde la finitude : la mort, le vieillissement et la vulnérabilité deviennent des objets de pensée, dans le sillage de Levinas et de la phénoménologie.",
 "Les œuvres au programme sont étudiées dans leur contexte et dans leurs enjeux de traduction et de réception, en lien avec l'épreuve orale de spécialité.",
 "La question centrale : l'humain est-il encore maître de ses créations, et comment penser une responsabilité qui dépasse le présent et l'espèce humaine ?"
], [
 q("Quel auteur a publié Le Principe responsabilité en 1979 ?", ["Hans Jonas", "Hannah Arendt", "Primo Levi", "Gilbert Simondon"], 0, "Hans Jonas y formule le principe de responsabilité envers les générations futures, à l'âge de la technique."),
 q("Qui a écrit Eichmann à Jérusalem (1963) ?", ["Hannah Arendt", "Primo Levi", "Jorge Semprún", "Emmanuel Levinas"], 0, "Arendt y analyse la « banalité du mal » à partir du procès d'Adolf Eichmann."),
 q("Quel est le titre du témoignage de Primo Levi sur les camps ?", ["Si c'est un homme", "La Trêve", "Le Système périodique", "L'Œuvre d'or"], 0, "Si c'est un homme (1947) est le récit de la déportation de Primo Levi à Auschwitz."),
 q("Quel philosophe a travaillé sur l'individuation et la technique ?", ["Simondon", "Jonas", "Arendt", "Levi"], 0, "Gilbert Simondon analyse la technique comme un mode d'individuation dans L'Individuation (1965)."),
 t("Pourquoi la notion de « limite » est-elle centrale en terminale HLP ?", "Parce que la technique étend les capacités humaines tout en révélant la finitude et la responsabilité envers la nature.", "L'entrée « L'humain et ses limites » articule technique, écologie et finitude sans postuler une maîtrise sans bornes."),
 t("Quel problème de forme le témoignage des camps pose-t-il ?", "Il faut dire une expérience extrême avec des mots ordinaires, tout en résistant à la spectacularisation.", "Primo Levi et Semprún réfléchissent dans leur récit aux limites du langage et à la responsabilité du lecteur face à ce qui est rapporté."),
 t("Comment Hans Jonas renouvelle-t-il l'éthique ?", "Il étend la responsabilité morale aux générations futures et à la nature, face aux pouvoirs de la technique.", "Le principe de responsabilité demande d'éviter les actions dont les effets, différés et irréversibles, compromettent la survie de l'humanité."),
 t("Qu'appelle-t-on « banalité du mal » ?", "Le fait que le mal puisse être commis par des individus ordinaires obéissant à des règles, sans motivation sadique.", "Arendt déplace l'explication du mal de la monstruosité individuelle vers la routine administrative et la soumission à l'autorité.")
])),

# ---------------- LLCE ----------------
F.append(f(["1re"], "LLCE", "Chapitre : Le roman victorien – Dickens, Eliot et la critique sociale", SLL, [
 "La spécialité LLCER (4 heures en première, 6 heures en terminale) étudie une langue étrangère à travers sa littérature et sa civilisation, dans une perspective interculturelle et bilingue.",
 "Charles Dickens publie Oliver Twist (1838) puis David Copperfield (1850) : ses romans exposent la misère urbaine, le travail des enfants et les institutions de l'Angleterre industrielle.",
 "Le « workhouse » (maison de travail) et les « debtors' prisons » sont des cibles récurrentes de la satire dickensienne, qui mêle humour, pathétique et indignation morale.",
 "George Eliot (Middlemarch, 1871-1872) analyse les déterminismes sociaux et les aspirations des femmes dans une Angleterre provinciale en mutation.",
 "Thomas Hardy (Tess d'Urberville, 1891 ; Jude l'Obscur, 1895) fait du determinisme social et des normes morales le ressort de tragédies paysannes.",
 "L'étude du texte en langue originale suppose de repérer le point de vue narratif, le registre (satirique, pathétique, ironique) et les références culturelles propres à la civilisation britannique.",
 "Le programme de 2026 renforce l'exigence de compréhension de documents de civilisation (discours, articles, images) en lien avec les œuvres littéraires.",
 "Les notions clés à maîtriser en anglais sont : narrative voice, setting, social critique, irony, symbolism, et la capacité à reformuler (paraphrase) un passage.",
 "L'épreuve orale de spécialité demande une présentation en langue étrangère de l'œuvre au programme, suivie d'un entretien sur les enjeux culturels.",
 "Le roman victorien reste un observatoire privilégié de la révolution industrielle : urbanisation, classes sociales, enfance et statut des femmes y sont traités à travers des personnages concrets."
], [
 q("Quel romancier a écrit Oliver Twist ?", ["Charles Dickens", "George Eliot", "Thomas Hardy", "Jane Austen"], 0, "Charles Dickens publie Oliver Twist en 1838 : le roman dénonce le workhouse et l'exploitation des enfants."),
 q("Quel roman de George Eliot paraît en 1871-1872 ?", ["Middlemarch", "Tess d'Urberville", "Great Expectations", "Wuthering Heights"], 0, "Middlemarch est un vaste roman de mœurs provinciales, publié en huit livraisons en 1871-1872."),
 q("Quel est l'objet principal de la satire de Dickens ?", ["La monarchie", "Les institutions sociales et la misère urbaine", "La religion catholique", "Les universités"], 1, "Dickens s'attaque aux workhouses, aux prisons pour dettes et à l'exploitation du travail des enfants."),
 q("Quel écrivain a publié Tess d'Urberville en 1891 ?", ["Thomas Hardy", "Charles Dickens", "George Eliot", "Robert Louis Stevenson"], 0, "Thomas Hardy signe ce roman en 1891 ; il y décrit l'oppression des normes morales et sociales sur une jeune paysanne."),
 q("Que signifie le terme « workhouse » ?", ["Une école privée", "Une maison de travail pour les pauvres", "Une prison militaire", "Un hôpital"], 1, "Le workhouse est un établissement où les pauvres étaient envoyés et soumis à un travail forcé, dénoncé par Dickens."),
 t("En quoi le roman victorien est-il un outil de critique sociale ?", "Il donne à voir les effets de l'industrialisation sur les classes populaires et met en question les normes morales du temps.", "Dickens, Eliot et Hardy font du roman un observatoire de la société : pauvreté, statut des femmes et déterminisme y sont traités à travers des situations concrètes."),
 t("Quels mots anglais désignent le point de vue narratif et l'ironie ?", "Narrative voice (ou point of view) et irony.", "L'analyse bilingue exige ces outils : le narrateur peut être omniscient, interne ou fiable/incroyable (unreliable narrator), et l'ironie repose sur un écart entre dit et voulu."),
 t("Comment l'étude de la civilisation éclaire-t-elle le roman ?", "Elle explique les institutions, les lois et les mentalités qui pèsent sur les personnages.", "Sans connaître le système des classes, le travail des enfants ou la condition féminine au XIXe siècle, la lecture du roman victorien reste partielle.")
])),

F.append(f(["Terminale"], "LLCE", "Chapitre : Le rêve américain et sa critique dans la littérature anglophone", SLL, [
 "En terminale LLCER, l'étude associe texte littéraire et documents de civilisation ; la question du « American Dream » structure l'étude des États-Unis.",
 "Le « rêve américain » désigne l'idée selon laquelle chacun peut, par son travail et sa vertu, accéder à la prospérité ; il est formulé au XIXe siècle et relayé par le mythe de la frontier.",
 "Le mythe de la frontier, théorisé par Frederick Jackson Turner en 1893, fait de la conquête de l'Ouest le moteur du caractère national américain (individualisme, mobilité, renouvellement).",
 "F. Scott Fitzgerald publie Gatsby le Magnifique (The Great Gatsby, 1925) : la réussite apparente de Jay Gatsby cache une aspiration impossible et dénonce la corruption morale de l'« ère du jazz ».",
 "Le personnage de Nick Carraway, narrateur interne, est un « reliable but limited narrator » : sa lucidité s'accompagne d'une complicité ambiguë avec le monde qu'il juge.",
 "John Steinbeck (The Grapes of Wrath, 1939) oppose au récit de réussite l'expérience des migrants de la Grande Dépression et la solidarité de classe.",
 "Toni Morrison (Beloved, 1987) fait de l'esclavage et de ses séquelles psychiques un objet de mémoire qui contredit le mythe d'une Amérique innocente.",
 "Le programme de 2026 (BO n° 21 du 22 mai 2026) fixe les œuvres au programme de l'épreuve ; les auteurs étudiés doivent être replacés dans leur contexte historique et culturel.",
 "L'analyse porte sur les images du rêve (lumière, richesse, ascension), sur le point de vue et sur le traitement de l'échec : le « green light » de Gatsby est le symbole d'un avenir toujours différé.",
 "L'épreuve écrite de spécialité propose une traduction, une question de compréhension et un essai en anglais ; la maîtrise du vocabulaire analytique est déterminante."
], [
 q("Quel roman de F. Scott Fitzgerald critique le rêve américain ?", ["The Great Gatsby", "The Grapes of Wrath", "Beloved", "Great Expectations"], 0, "The Great Gatsby (1925) montre l'échec d'une aspiration née du rêve américain dans l'Amérique des années 1920."),
 q("Qui a formulé la « Frontier Thesis » en 1893 ?", ["Frederick Jackson Turner", "Fitzgerald", "Steinbeck", "Morrison"], 0, "L'historien Turner soutient que la frontière a façonné le caractère démocratique et individualiste des États-Unis."),
 q("Quel roman de John Steinbeck porte sur la Grande Dépression ?", ["The Grapes of Wrath", "Beloved", "The Great Gatsby", "Of Mice and Men"], 0, "The Grapes of Wrath (1939) suit la famille Joad, paysans okies chassés par la sécheresse et la crise."),
 q("Quel est le symbole central de la lumière verte dans Gatsby ?", ["L'argent", "Un avenir désiré et inaccessible", "La guerre", "La nature"], 1, "La « green light » située de l'autre côté de la baie représente le rêve de Daisy et, plus largement, un bonheur toujours hors de portée."),
 q("Quel type de narrateur est Nick Carraway ?", ["Omniscient", "Interne et limité", "Absent", "Collectif"], 1, "Nick participe à l'action et ne rapporte que ce qu'il voit ou apprend : sa lucidité reste partielle."),
 t("Comment le rêve américain est-il critiqué dans la littérature ?", "Il est présenté comme un mythe qui masque les inégalités, le racisme et les déceptions de la mobilité sociale.", "Fitzgerald, Steinbeck et Morrison montrent les limites du mythe : réussite illusoire, misère des migrants et héritage de l'esclavage."),
 t("Quel est l'intérêt de l'expression « Jazz Age » pour Gatsby ?", "Elle situe le roman dans les années 1920, marquées par la prospérité, la consommation et la désillusion après la guerre.", "Le terme, popularisé par Fitzgerald lui-même, désigne une époque d'euphorie qui cache la corruption morale et le vide spirituel décrits dans le roman."),
 t("Pourquoi Toni Morrison est-elle une autrice clé du programme ?", "Parce qu'elle réinscrit l'histoire afro-américaine et la mémoire de l'esclavage dans la littérature canonique.", "Prix Nobel en 1993, Morrison invente une écriture de la mémoire où les fantômes du passé sont des personnages à part entière.")
])),

F.append(f(["Terminale"], "LLCE", "Chapitre : Modernisme et identité dans la littérature anglophone du XXe siècle", SLL, [
 "Le modernisme anglophone rompt avec le roman réaliste du XIXe siècle : la conscience, la mémoire et la langue deviennent les matières mêmes de l'œuvre.",
 "Virginia Woolf publie Mrs Dalloway (1925) et To the Lighthouse (1927) : elle adopte le monologue intérieur et une structure temporelle fragmentée, où une journée contient toute une vie.",
 "James Joyce publie Ulysse (Ulysses, 1922) : le roman transpose l'Odyssée dans une journée dublinoise et exploite le flux de conscience (stream of consciousness).",
 "T. S. Eliot publie The Waste Land (La Terre désolée, 1922) : le poème montre la fragmentation du monde après la Première Guerre mondiale par des voix, des langues et des citations multiples.",
 "Le modernisme est aussi une réflexion sur le temps : Henri Bergson (durée) et la psychologie naissante influencent la manière de représenter la conscience.",
 "Après 1945, la littérature postcoloniale interroge l'identité hybride et l'héritage de l'empire : Chinua Achebe (Things Fall Apart, 1958) répond au regard de Conrad sur l'Afrique.",
 "Salman Rushdie (Midnight's Children, 1981) mêle histoire de l'Inde indépendante et réalisme magique : le narrateur né à minuit incarne une nation multiple et fracturée.",
 "Le programme invite à comparer les formes du récit : fragmentation, multiperspectivité, analepse et mélange des registres sont des marqueurs du modernisme et du postmodernisme.",
 "La lecture bilingue porte sur la langue : néologismes, jeux de mots, citations et changements de registre participent à la construction du sens.",
 "L'enjeu culturel est de comprendre comment la littérature anglophone a représenté les mutations du monde moderne : guerre, urbanisation, décolonisation et migration."
], [
 q("Quel roman de Virginia Woolf paraît en 1925 ?", ["Mrs Dalloway", "Ulysses", "The Waste Land", "Midnight's Children"], 0, "Mrs Dalloway (1925) est un roman moderniste construit autour d'une journée et de la conscience des personnages."),
 q("Qui a écrit Ulysses en 1922 ?", ["James Joyce", "Virginia Woolf", "T. S. Eliot", "Salman Rushdie"], 0, "James Joyce publie Ulysses en 1922 ; le roman transpose l'Odyssée dans le Dublin de 1904."),
 q("Quel poème de T. S. Eliot date de 1922 ?", ["The Waste Land", "Prufrock", "Four Quartets", "The Hollow Men"], 0, "The Waste Land (1922) est un poème moderniste majeur, publié avec les notes d'Ezra Pound."),
 q("Quel roman de Chinua Achebe paraît en 1958 ?", ["Things Fall Apart", "Midnight's Children", "Beloved", "The Arrow of God"], 0, "Things Fall Apart (1958) raconte la rencontre entre le monde igbo et les missionnaires coloniaux."),
 q("Quel est le principe du « stream of consciousness » ?", ["Un récit à la troisième personne", "La restitution du flux des pensées d'un personnage", "Une intrigue linéaire", "Un poème en prose"], 1, "Le flux de conscience restitue directement les pensées, sensations et souvenirs d'un personnage, sans médiation logique."),
 t("Quelle différence oppose le roman réaliste et le roman moderniste ?", "Le premier décrit une réalité extérieure et une intrigue ; le second explore la conscience et fragmente le temps.", "Woolf et Joyce remplacent la chronologie par la durée vécue et le point de vue multiple, estimant que la réalité psychique est plus vraie que la description objective."),
 t("Comment le modernisme représente-t-il la crise du monde moderne ?", "Par la fragmentation des formes, la multiplicité des voix et le collage de citations.", "The Waste Land de Eliot juxtapose des langues et des figures culturelles pour exprimer la désintégration de l'Europe après 1918."),
 t("Comment la littérature postcoloniale répond-elle au modernisme ?", "Elle réapproprie les formes modernistes pour raconter l'expérience coloniale et l'hybridation des identités.", "Achebe corrige le regard de Conrad, Rushdie invente une écriture de la diaspora : la forme même du récit devient un enjeu politique.")
])),

# ---------------- LCA ----------------
F.append(f(["1re"], "LCA", "Chapitre : Cicéron et l'art oratoire à Rome", SLCA, [
 "L'enseignement de LCA (latin ou grec) associe la maîtrise de la langue à l'étude de la civilisation et des textes antiques, dans une approche bilingue et interculturelle.",
 "Marcus Tullius Cicéron (106-43 av. J.-C.) est le principal orateur de la fin de la République : ses discours et ses traités rhétoriques fondent le modèle de l'éloquence latine.",
 "Les Catilinaires (63 av. J.-C.) sont quatre discours prononcés contre Lucius Sergius Catilina, accusé de conjuration contre la République ; le premier s'ouvre sur la formule « Quousque tandem abutere, Catilina, patientia nostra ? ».",
 "Dans De Oratore (55 av. J.-C.), Cicéron définit l'orateur idéal par l'ensemble des connaissances, la maîtrise du style et l'action oratoire ; il transpose à Rome la rhétorique grecque.",
 "Le cursus honorum (carrière des honneurs) structure la vie politique romaine : questeur, édile, préteur, consul, censeur ; Cicéron est consul en 63 av. J.-C.",
 "Les discours judiciaires (Pro Roscio Amerino, 80 av. J.-C.) et politiques (Philippiques, contre Antoine, 44-43 av. J.-C.) montrent la place de la parole dans les procès et le Sénat.",
 "La langue latine étudiée porte sur la morphologie (déclinaisons, conjugaisons), la syntaxe des cas et le vocabulaire politique : res publica, senatus, imperium, virtus.",
 "Le travail de traduction exige de rendre les figures (anaphore, antithèse, chiasme) et le rythme de la période cicéronienne, analysée par Quintilien et par Cicéron lui-même dans l'Orator.",
 "L'étude du contexte (guerres civiles, fin de la République, alliance de Pompée, César et Crassus) est indispensable pour comprendre les enjeux des discours.",
 "Le programme de terminale approfondit la lecture des textes dans leur langue et leur contexte, en lien avec l'épreuve de spécialité et l'option LCA."
], [
 q("Contre qui Cicéron prononce-t-il les Catilinaires en 63 av. J.-C. ?", ["Catilina", "César", "Pompée", "Néron"], 0, "Les quatre discours visent Lucius Sergius Catilina et sa conjuration contre la République."),
 q("Quel traité de Cicéron théorise l'éloquence ?", ["De Oratore", "De Republica", "De Natura Deorum", "De Officiis"], 0, "De Oratore (55 av. J.-C.) définit les qualités et les savoirs de l'orateur parfait."),
 q("Quelle fonction Cicéron exerce-t-il en 63 av. J.-C. ?", ["Questeur", "Consul", "Tribun", "Censeur"], 1, "Cicéron est consul en 63, année où il déjoue la conjuration de Catilina."),
 q("Que signifie « res publica » ?", ["La propriété privée", "La chose publique / la République", "Le Sénat", "L'armée"], 1, "Littéralement « chose publique », l'expression désigne l'État et le bien commun à Rome."),
 q("Quel est le premier mot du début des Catilinaires ?", ["Quousque", "O tempora", "Veni", "Cave"], 0, "Le discours s'ouvre sur « Quousque tandem abutere, Catilina, patientia nostra ? » (« Jusqu'à quand abuseras-tu de notre patience ? »)."),
 t("Comment les Catilinaires mêlent-elles genres judiciaire et délibératif ?", "Cicéron accuse Catilina tout en délibérant avec le Sénat sur les mesures à prendre pour sauver la République.", "Le premier discours est une accusation directe (genre judiciaire) et une exhortation à l'assemblée (genre délibératif), selon les catégories aristotéliciennes."),
 t("Quel est l'intérêt de traduire la période cicéronienne ?", "Elle montre comment la structure syntaxique sert la persuasion et le rythme de l'argumentation.", "La période est une phrase longue et équilibrée, où les propositions s'enchaînent selon un rythme qui prépare la chute : la traduction doit en restituer l'architecture."),
 t("Pourquoi le contexte de la fin de la République est-il essentiel ?", "Parce que les discours s'inscrivent dans les tensions entre le Sénat, les généraux et le peuple.", "La conjuration de Catilina révèle la fragilité des institutions républicaines, quelques années avant la domination de César et la fondation du Principat.")
])),

F.append(f(["1re"], "LCA", "Chapitre : Virgile et l'Énéide – épopée et identité romaine", SLCA, [
 "L'Énéide de Virgile (70-19 av. J.-C.), publiée après sa mort en 19 av. J.-C., est l'épopée nationale de Rome : elle relate la fuite d'Énée de Troie et la fondation de la cité latine.",
 "Le poème emprunte à Homère : l'Odyssée fournit le modèle du voyage et des épreuves (livres I-VI), tandis que l'Iliade inspire les combats du livre XII.",
 "Virgile construit une généalogie légendaire qui relie Rome à Troie et à Vénus, légitimant ainsi l'empire d'Auguste par un passé mythique.",
 "L'œuvre s'inscrit dans le programme culturel d'Auguste : elle célèbre la paix revenue après les guerres civiles et le retour à l'ordre (livres VII-XII : l'arrivée en Italie et la guerre contre Turnus).",
 "Énée est un héros « pius » : sa piété filiale (il porte son père Anchise hors de Troie) et sa soumission aux dieux définissent un modèle de vertu romaine.",
 "Le chant VI (descente aux Enfers) est un moment clé : Énée y rencontre Didon, Anchise et les âmes des héros, et reçoit la vision du futur peuple romain.",
 "Didon, reine de Carthage, incarne l'obstacle passionnel : son suicide après le départ d'Énée oppose l'amour individuel au devoir historique du héros.",
 "La langue de l'Énéide (hexamètres dactyliques, allitérations, comparaisons) est un objet d'étude privilégié : traduction et commentaire stylistique sont au programme.",
 "Les notions de « translatio imperii » (transfert de l'empire de Troie vers Rome) et de « pietas » structurent l'interprétation de l'œuvre.",
 "La réception de l'Énéide, de la Rome antique à la littérature moderne, montre comment l'épopée virgilienne a façonné l'idée même de destin national."
], [
 q("Quel poème grec a servi de modèle au voyage d'Énée ?", ["L'Odyssée", "L'Iliade", "La Théogonie", "Les Travaux et les Jours"], 0, "L'Odyssée d'Homère fournit le cadre du voyage d'Énée ; l'Iliade inspire les épisodes guerriers."),
 q("En quelle année l'Énéide est-elle publiée ?", ["19 av. J.-C.", "44 av. J.-C.", "70 av. J.-C.", "27 av. J.-C."], 0, "Virgile meurt en 19 av. J.-C. ; l'Énéide est publiée peu après, sur ordre d'Auguste."),
 q("Quel adjectif qualifie traditionnellement Énée ?", ["Pius", "Saevus", "Dulcis", "Felix"], 0, "La « pietas » (piété envers les dieux, la famille et la patrie) est la vertu centrale du héros virgilien."),
 q("Qui Énée rencontre-t-il dans le chant VI aux Enfers ?", ["Anchise", "Achille", "Agamemnon", "Pompée"], 0, "Énée y retrouve son père Anchise, qui lui révèle le destin glorieux de Rome."),
 q("Que représente Didon dans l'Énéide ?", ["La sagesse", "L'obstacle de l'amour au devoir du héros", "La victoire romaine", "La déesse Vénus"], 1, "Reine de Carthage, Didon aime Énée mais celui-ci doit la quitter pour accomplir sa mission : sa mort symbolise le prix de l'empire."),
 t("Pourquoi l'Énéide est-elle une épopée « nationale » ?", "Elle fonde une généalogie mythique de Rome et légitime le pouvoir d'Auguste en rattachant la cité à Troie.", "Virgile compose sous Auguste : le mythe d'Énée devient le récit d'origine de la Romanité et du Principat."),
 t("Comment Virgile s'inspire-t-il d'Homère ?", "Il reprend le modèle du voyage et des combats, mais le met au service d'une réflexion sur le destin de Rome.", "L'Énéide est une réécriture consciente : les trois premiers livres imitent l'Odyssée, les livres VII-XII s'inspirent de l'Iliade, avec une visée politique nouvelle."),
 t("Quel est l'effet de la rencontre avec Didon pour Énée ?", "Elle met à l'épreuve sa piété et son sacrifice : il doit renoncer à l'amour pour accomplir sa mission.", "Le chant IV fait du départ d'Énée un moment tragique : le lecteur comprend la grandeur du destin romain mais en mesure le coût humain.")
])),

F.append(f(["Terminale"], "LCA", "Chapitre : Sophocle et la tragédie grecque – Œdipe roi", SLCA, [
 "En terminale, la spécialité LCA approfondit l'étude des textes grecs et latins dans leur contexte historique, culturel et linguistique.",
 "Sophocle (vers 496-406 av. J.-C.) est l'un des trois grands tragédiens athéniens avec Eschyle et Euripide ; Œdipe roi (vers 429 av. J.-C.) est la pièce la plus commentée d'Aristote.",
 "La tragédie met en scène la tentative d'Œdipe pour échapper à l'oracle de Delphes qui le destine à tuer son père Laïos et épouser sa mère Jocaste.",
 "La structure de la pièce repose sur une enquête : Œdipe, roi de Thèbes, cherche à identifier le meurtrier de Laïos pour conjurer la peste, et découvre qu'il est lui-même le coupable.",
 "Aristote analyse la tragédie dans la Poétique (IVe s. av. J.-C.) : il y définit la catharsis (purification des émotions) et fait d'Œdipe le modèle de la reconnaissance (anagnorisis) et du revirement (péripétie).",
 "L'ironie tragique naît du décalage entre le savoir du spectateur (qui connaît le mythe) et l'ignorance du héros : les efforts d'Œdipe pour fuir l'oracle accomplissent la prophétie.",
 "Le chœur, composé de vieillards thébains, commente l'action, exprime la piété collective et fait le lien entre le héros et la cité.",
 "Le théâtre grec est un objet civique : les tragédies sont jouées aux fêtes des Dionysies, devant un public de citoyens, et financées par les liturgies des riches Athéniens.",
 "L'étude du grec ancien porte sur le vocabulaire du savoir et de l'aveuglement (oida, « je sais » ; Œdipe = « pied enflé »), la morphologie et les figures du texte.",
 "Le débat interprétatif porte sur la responsabilité d'Œdipe : est-il coupable malgré lui, ou sa recherche de la vérité est-elle une forme de grandeur ?"
], [
 q("Quel philosophe analyse Œdipe roi dans sa Poétique ?", ["Aristote", "Platon", "Socrate", "Épicure"], 0, "Aristote, dans la Poétique (IVe s. av. J.-C.), prend Œdipe roi comme modèle de la tragédie et de la reconnaissance."),
 q("Quel oracle reçoit Œdipe à Delphes ?", ["Il tuera son père et épousera sa mère", "Il deviendra roi de Thèbes", "Il périra en mer", "Il aura trois fils"], 0, "La prophétie annonce à Œdipe le parricide et l'inceste, qu'il tente vainement d'éviter."),
 q("Quel est le nom du meurtrier que Œdipe recherche ?", ["Laïos", "Jocaste", "Créon", "Tirésias"], 0, "Œdipe cherche à punir le meurtrier de Laïos, son prédécesseur sur le trône de Thèbes, ignorant qu'il est lui-même."),
 q("Que désigne la « catharsis » chez Aristote ?", ["La purification des émotions par la tragédie", "La mise en scène du chœur", "Le dénouement heureux", "La colère des dieux"], 0, "La catharsis est l'effet de la tragédie : elle purge la pitié et la terreur en les portant à leur intensité."),
 q("Qui révèle la vérité à Œdipe ?", ["Tirésias", "Sophocle", "Aristote", "Achille"], 0, "Le devin Tirésias, puis le messager de Corinthe et le berger, conduisent Œdipe à la reconnaissance."),
 t("Qu'est-ce que l'ironie tragique dans Œdipe roi ?", "Le spectateur sait ce que le personnage ignore : les efforts d'Œdipe pour fuir l'oracle accomplissent la prophétie.", "Ce décalage entre savoir du public et ignorance du héros est analysé par Aristote comme un ressort central de la tragédie sophocléenne."),
 t("Comment la recherche de la vérité devient-elle une épreuve pour Œdipe ?", "Chaque indice qu'il découvre le rapproche de sa propre culpabilité, alors qu'il croit sauver Thèbes.", "L'enquête est une structure tragique : la science du héros se retourne contre lui, et la reconnaissance (anagnorisis) coïncide avec sa perte."),
 t("Quel rôle le chœur joue-t-il dans la tragédie grecque ?", "Il commente l'action, exprime les valeurs de la cité et médite sur la piété et la destinée humaine.", "Le chœur représente la communauté des citoyens : ses odes rythment le drame et généralisent le problème individuel d'Œdipe à la condition humaine.")
])),

# ---------------- ARTS ----------------
F.append(f(["1re"], "Arts plastiques", "Chapitre : La photographie – du procédé technique au langage artistique", SART1, [
 "Le programme d'arts plastiques de première définit l'œuvre comme un objet singulier dont on analyse les formes, les statuts et les usages, dans une perspective de création et de culture artistique.",
 "La photographie naît avec le daguerréotype, rendu public en 1839 par Daguerre, puis avec le procédé au gélatino-bromure d'argent (1871) qui permet les tirages multiples.",
 "Au XIXe siècle, la photographie est débattue : elle est tour à tour considérée comme un simple outil de reproduction du réel et douée d'un statut artistique discuté (Baudelaire, « Le public et la photographie », 1859).",
 "Les portraitistes (Nadar) et les photographes de voyage (Maxime Du Camp, Félix Teynard) construisent une image documentaire et une mise en scène du réel.",
 "Au XXe siècle, Man Ray et László Moholy-Nagy explorent la photographie abstraite, la solarisation et le photogramme, affirmant l'autonomie du médium.",
 "Le photogramme est une image obtenue sans appareil, en plaçant des objets sur une surface photosensible exposée à la lumière.",
 "Le surréalisme et le Bauhaus jouent un rôle décisif dans la reconnaissance de la photographie comme langage : cadrage, lumière, grain et échelle deviennent des paramètres expressifs.",
 "L'analyse d'une photographie porte sur le cadrage (ce qui est inclus et exclu), le point de vue, la lumière, le contraste, le grain et le contexte de présentation (tirage, album, mur, écran).",
 "Le programme distingue les quatre grands types de pratiques : pratiques bidimensionnelles (graphiques et picturales), tridimensionnelles (sculpturales et architecturales), photographiques et numériques.",
 "La question centrale : la photographie est-elle une trace du réel ou une construction, et comment l'artiste peut-il en faire un langage singulier ?"
], [
 q("En quelle année le daguerréotype est-il rendu public ?", ["1839", "1851", "1888", "1900"], 0, "Le daguerréotype est présenté en 1839 par Daguerre : c'est le premier procédé photographique exploitable."),
 q("Quel artiste a réalisé des photogrammes sans appareil ?", ["Man Ray", "Monet", "Rodin", "Picasso"], 0, "Man Ray, comme Moholy-Nagy, explore le photogramme : des objets posés sur une surface photosensible et exposés à la lumière."),
 q("Quel est l'apport du procédé au gélatino-bromure d'argent ?", ["Il permet la couleur", "Il permet le tirage multiple sur papier", "Il supprime la lumière", "Il invente le cinéma"], 1, "Ce procédé, mis au point en 1871, rend possible la production de négatifs et de tirages en série."),
 q("Que signifie le « cadrage » d'une photographie ?", ["Le choix de ce qui est inclus et exclu de l'image", "La lumière utilisée", "Le format du tirage", "Le nom du photographe"], 0, "Le cadrage est un choix constructif : il délimite le champ, définit un hors-champ et oriente la lecture de l'image."),
 q("Quel texte de Baudelaire porte sur la photographie ?", ["Le Public et la photographie", "Les Fleurs du mal", "Le Salon de 1859", "Peintres et aquafortistes"], 0, "Baudelaire publie « Le public et la photographie » en 1859 : il y conteste la confusion entre art et reproduction mécanique."),
 t("Qu'est-ce qu'un photogramme ?", "Une image obtenue sans appareil, en exposant à la lumière des objets posés sur une surface photosensible.", "Man Ray et Moholy-Nagy l'utilisent pour libérer la photographie de la représentation et en faire une expérience graphique."),
 t("Comment une photographie peut-elle être un langage artistique ?", "Par des choix de cadrage, de lumière, de grain et de présentation qui produisent du sens.", "La photographie n'est pas un simple enregistrement : chaque paramètre technique devient un moyen d'expression et de mise en scène du réel."),
 t("Quelle question le programme pose-t-il sur le statut de l'œuvre ?", "Faut-il voir dans la photographie une trace du réel ou une construction, et quels critères la font reconnaître comme art ?", "Le débat baudelairien et les pratiques du XXe siècle montrent que le statut de l'œuvre dépend autant du contexte et de l'intention que du procédé technique.")
])),

F.append(f(["1re"], "Arts plastiques", "Chapitre : Architecture et espace – du monument à l'installation", SART1, [
 "L'architecture est l'une des quatre grandes familles de pratiques du programme d'arts plastiques : elle engage le rapport entre forme, fonction, structure et usage de l'espace.",
 "L'architecture grecque codifie les ordres (dorique, ionique, corinthien) et cherche un équilibre entre proportion, symétrie et fonction du bâtiment.",
 "Le Parthénon (447-432 av. J.-C.) sur l'Acropole d'Athènes illustre l'ordre dorique et les corrections optiques (entasis des colonnes, léger bombement du stylobate).",
 "Au Moyen Âge, l'architecture gothique (Chartres, Amiens) invente la croisée d'ogives, l'arc-boutant et le vitrail pour élever des édifices lumineux et structurer un imaginaire religieux.",
 "À la Renaissance, Alberti et Palladio théorisent la proportion et la symétrie héritées de Vitruve ; la villa rotonda (Palladio, 1566-1590) en est un modèle.",
 "Au XXe siècle, Le Corbusier formule les « cinq points d'une architecture nouvelle » (pilotis, plan libre, façade libre, fenêtre en bandeau, toit-terrasse), mis en pratique à la villa Savoye (1928-1931).",
 "L'installation, développée à partir des années 1960-1970 (Joseph Beuys, Daniel Buren), déplace l'œuvre de l'objet autonome vers la situation : l'espace, le spectateur et le dispositif deviennent partie intégrante du travail.",
 "L'analyse d'une œuvre architecturale ou d'une installation porte sur les matériaux, l'échelle, la structure, la lumière et le parcours du spectateur.",
 "Le programme demande de comparer les statuts de l'œuvre : le monument est durable et autonome, l'installation est souvent temporaire et dépendante de son contexte de présentation.",
 "L'enjeu est de comprendre comment l'espace devient un medium artistique et comment la présentation elle-même produit du sens."
], [
 q("Quel architecte a formulé les « cinq points d'une architecture nouvelle » ?", ["Le Corbusier", "Gaudí", "Frank Lloyd Wright", "Palladio"], 0, "Le Corbusier énonce ces cinq points vers 1925-1927 ; ils sont mis en pratique dans la villa Savoye."),
 q("Quelle innovation technique caractérise l'architecture gothique ?", ["La voûte en berceau", "La croisée d'ogives et l'arc-boutant", "Le béton armé", "La coupole"], 1, "La croisée d'ogives et l'arc-boutant permettent d'élever des murs hauts percés de grands vitraux."),
 q("Quel édifice illustre l'ordre dorique à Athènes ?", ["Le Parthénon", "L'Érechthéion", "Le Temple de Zeus", "L'Odéon"], 0, "Le Parthénon (447-432 av. J.-C.) est le temple dorique majeur de l'Acropole."),
 t("Quelle différence oppose monument et installation ?", "Le monument est durable et autonome ; l'installation est temporaire et intègre l'espace et le spectateur.", "Le programme d'arts plastiques demande de comparer les statuts de l'œuvre : l'installation fait de la présentation un langage plastique."),
 q("Qui a théorisé l'architecture de la Renaissance dans De re aedificatoria ?", ["Alberti", "Vitruve", "Le Corbusier", "Viollet-le-Duc"], 0, "Leon Battista Alberti publie De re aedificatoria vers 1450, traité fondé sur le Vitruve antique."),
 t("Comment la villa Savoye illustre-t-elle les cinq points du Corbusier ?", "Elle est portée sur pilotis, avec un plan libre, une façade libre, une fenêtre en bandeau et un toit-terrasse.", "Construite en 1928-1931 à Poissy, elle est un manifeste du Style international : la structure indépendante libère le plan et la façade."),
 t("En quoi l'installation renouvelle-t-elle le statut de l'œuvre ?", "Elle déplace l'œuvre de l'objet vers le dispositif et l'expérience du spectateur.", "L'œuvre n'est plus seulement un objet à contempler mais une situation à traverser : le contexte, la durée et le public deviennent des matériaux."),
 t("Comment analyser l'espace d'une œuvre plastique ?", "En étudiant l'échelle, la structure, la lumière, les matériaux et le parcours imposé au spectateur.", "Ces critères permettent de comprendre comment l'artiste construit une expérience spatiale et donne une forme à une intention esthétique.")
])),

F.append(f(["Terminale"], "Arts plastiques", "Chapitre : L'impressionnisme et la naissance de la modernité picturale", SART2, [
 "La terminale d'arts plastiques étudie l'œuvre dans son histoire et ses statuts ; l'impressionnisme est un objet de référence pour comprendre la rupture moderne.",
 "Le mot « impressionnisme » vient d'un article du critique Louis Leroy en 1874, qui se moque d'une toile de Monet intitulée Impression, soleil levant (1872).",
 "Monet, Renoir, Degas, Pissarro, Sisley et Berthe Morisot privilégient la peinture en plein air, la touche visible, la lumière changeante et des cadrages inspirés de la photographie et de l'estampe japonaise.",
 "La première exposition impressionniste a lieu en 1874, 35 boulevard des Capucines, à Paris ; huit expositions suivront jusqu'en 1886.",
 "Cette rupture est aussi technique : le tube de couleur métallique (1841), la boîte de couleurs portative et la toile légère sur châssis permettent de peindre devant le motif.",
 "Le Salon officiel reste attaché au dessin, au fini et à la hiérarchie des genres : l'impressionnisme lui oppose une peinture de la sensation et du moment.",
 "Les séries de Monet (Meules, 1890-1891 ; Cathédrale de Rouen, 1892-1894 ; Nymphéas) montrent que le même motif change avec la lumière : la série devient un procédé d'analyse.",
 "Degas, tout en refusant le plein air systématique, renouvelle le cadrage par la photographie et le japonisme (danseuses, courses de chevaux).",
 "L'analyse d'un tableau impressionniste porte sur la touche, la couleur (ombres colorées, refus du noir), la composition et le traitement de la lumière.",
 "L'enjeu du programme est de comprendre comment ce mouvement a déplacé le critère de la ressemblance vers la perception : la modernité picturale naît de ce déplacement."
], [
 q("De quelle toile de Monet le terme « impressionnisme » est-il tiré ?", ["Impression, soleil levant", "Les Nymphéas", "Le Déjeuner sur l'herbe", "La Danse"], 0, "Le critique Louis Leroy se moque d'Impression, soleil levant (1872) en 1874 ; le nom reste."),
 q("En quelle année a lieu la première exposition impressionniste ?", ["1863", "1874", "1886", "1900"], 1, "La première exposition du groupe se tient en 1874, boulevard des Capucines à Paris."),
 q("Quelle innovation technique rend possible la peinture en plein air ?", ["Le tube de peinture métallique", "La photographie couleur", "Le chevalet pliant en aluminium", "La peinture acrylique"], 0, "Le tube de couleur, la boîte portative et la toile légère permettent de travailler directement devant le motif."),
 q("Quel artiste a peint la série des Cathédrales de Rouen ?", ["Monet", "Renoir", "Degas", "Pissarro"], 0, "Monet peint la cathédrale à différentes heures entre 1892 et 1894 pour étudier les variations de lumière."),
 q("Quel est le rapport des impressionnistes au japonisme ?", ["Ils le refusent", "Il inspire leurs cadrages et leurs aplats", "Ils l'ignorent", "Ils le copient sans le transformer"], 1, "Les estampes japonaises, découvertes au XIXe siècle, influencent les cadrages décentrés et les aplats de couleur."),
 t("Quelles innovations techniques rendent possible la peinture en plein air ?", "Le tube de peinture métallique, la boîte de couleurs portative et la toile légère sur châssis.", "Ces outils, apparus au XIXe siècle, permettent de travailler devant le motif et de saisir les effets fugaces de la lumière."),
 t("Comment la série transforme-t-elle le motif chez Monet ?", "Le motif reste identique mais la lumière et l'heure changent, montrant que la perception est mouvante.", "Les Meules et les Nymphéas ne visent pas à reproduire un objet mais à enregistrer une succession d'impressions, faisant du temps un sujet de la peinture."),
 t("Quelle rupture l'impressionnisme introduit-il dans la peinture ?", "Il déplace l'exigence de la ressemblance vers la sensation visuelle et la touche personnelle.", "Le fini académique cède la place à une facture visible : le tableau devient le témoignage d'un regard plutôt que la copie d'un modèle.")
])),

F.append(f(["Terminale"], "Musique", "Chapitre : La musique et le temps – rythme, forme et écoute", SMUS, [
 "La spécialité musique associe la pratique instrumentale ou vocale, la culture musicale et l'analyse d'œuvres ; elle s'inscrit dans le programme d'arts de la voie générale.",
 "La musique est un art temporel : elle se déploie dans la durée, contrairement aux arts de l'espace comme la peinture ou l'architecture.",
 "Le rythme organise cette durée : il repose sur le tempo (vitesse), la mesure (groupement des temps), les accents et les valeurs (noires, croches, blanches).",
 "La forme musicale est une architecture sonore : la forme sonate (exposition, développement, réexposition) structure la musique classique de Haydn, Mozart et Beethoven.",
 "La sonate « Clair de lune » de Beethoven (op. 27 n° 2, 1801) et la Symphonie n° 5 (1808) sont des références du programme pour l'analyse de la forme et du motif.",
 "Au XXe siècle, Debussy (Prélude à l'après-midi d'un faune, 1894) dissout la tonalité dans une écriture impressionniste ; les compositeurs explorent de nouveaux rythmes (Stravinsky, Le Sacre du printemps, 1913).",
 "L'analyse musicale repose sur l'écoute active : repérer le motif, la mélodie, l'harmonie, le timbre, la dynamique et l'orchestration, puis les relier à une intention expressive.",
 "Le solfège et la lecture de partition permettent de décrire précisément hauteurs, durées et nuances ; l'oreille doit être entraînée à reconnaître les intervalles et les accords.",
 "Le programme invite à confronter des cultures musicales différentes (musique européenne, jazz, musiques traditionnelles) pour comprendre la diversité des organisations rythmiques et des systèmes sonores.",
 "L'épreuve de spécialité comprend une épreuve d'interprétation et un oral de culture musicale portant sur un programme limitatif publié au BO."
], [
 q("Quel compositeur a écrit Le Sacre du printemps en 1913 ?", ["Debussy", "Stravinsky", "Beethoven", "Mozart"], 1, "Igor Stravinsky compose Le Sacre du printemps, dont la création en 1913 provoque un scandale au Théâtre des Champs-Élysées."),
 q("Combien de parties comporte la forme sonate classique ?", ["Deux", "Trois", "Quatre", "Cinq"], 1, "La forme sonate comprend l'exposition, le développement et la réexposition."),
 q("Quel est le tempo d'un mouvement lent en italien ?", ["Presto", "Adagio", "Allegro", "Vivace"], 1, "Adagio désigne un tempo lent ; presto et vivace sont rapides, allegro est vif et modéré."),
 q("Quel compositeur a écrit Prélude à l'après-midi d'un faune (1894) ?", ["Debussy", "Ravel", "Bach", "Haydn"], 0, "Claude Debussy compose cette pièce d'après le poème de Mallarmé ; elle ouvre la musique impressionniste."),
 q("Que désigne le « timbre » d'un son ?", ["Sa hauteur", "Sa durée", "Sa couleur sonore", "Son intensité"], 2, "Le timbre est la qualité qui permet de distinguer deux instruments jouant la même note : c'est la « couleur » du son."),
 t("Pourquoi la musique est-elle un art du temps ?", "Parce qu'elle n'existe que dans le déroulement d'une durée, contrairement aux arts de l'espace.", "Une œuvre musicale se construit dans le temps : le rythme, la mesure et la forme sonore organisent cette durée et créent l'attente et la mémoire."),
 t("Comment analyser un motif musical ?", "En repérant sa mélodie, son rythme et ses transformations (reprise, variation, développement) au cours de l'œuvre.", "Le motif est la cellule génératrice : la forme sonate montre comment il est exposé, transformé puis réaffirmé, ce qui donne à l'œuvre son unité."),
 t("Quel est l'apport de l'écoute active ?", "Elle permet de reconnaître les éléments musicaux et de relier les choix du compositeur à l'effet produit.", "L'écoute active est une méthode : on identifie tour à tour les paramètres (hauteur, durée, intensité, timbre) puis on interprète leur organisation.")
])),

AN.append(a("Sujet type bac – HLP, épreuve orale de spécialité : commentaire d'un texte de rhétorique", "HLP",
 "Sujet type – épreuve orale de spécialité HLP, première (20 minutes de préparation, 12 minutes d'exposé).\n"
 "Texte : Cicéron, Première Catilinaire, § 1 : « Quousque tandem abutere, Catilina, patientia nostra ? Quamdiu etiam furor iste tuus nos eludet ? »\n"
 "Consigne : présenter le texte, le situer dans son contexte historique et littéraire, en proposer une lecture commentée (traduction, figures, effets), puis ouvrir sur la question des pouvoirs de la parole.",
 "Corrigé indicatif. I. Présentation : Cicéron, consul en 63 av. J.-C., prononce la première Catilinaire devant le Sénat après la découverte de la conjuration de Catilina. Le texte relève du genre judiciaire et délibératif.\n"
 "II. Lecture : l'anaphore interrogative (« Quousque tandem... Quamdiu... ») crée une accumulation qui traduit l'indignation et impose un rythme accusateur. Le vocatif « Catilina » interpelle directement l'adversaire ; « patientia nostra » oppose la retenue du Sénat au « furor » (fureur) du conjuré. La traduction doit rendre la violence de l'apostrophe.\n"
 "III. Ouverture : la parole devient ici une arme politique : l'orateur construit son autorité (ethos de défenseur de la République), émeut l'assemblée (pathos) et argumente (logos). On peut confronter à la critique platonicienne des sophistes (Gorgias) : la même maîtrise oratoire peut servir la vérité ou la manipulation.\n"
 "Conclusion : ce début de discours condense les enjeux de l'objet « Les pouvoirs de la parole » : l'éloquence est à la fois un art, une autorité et une séduction."))

AN.append(a("Sujet type bac – LLCER, épreuve écrite de spécialité : essai sur The Great Gatsby", "LLCE",
 "Sujet type – épreuve écrite de spécialité LLCER (terminale, 4 points).\n"
 "Document 1 : extrait de The Great Gatsby (F. Scott Fitzgerald, 1925) : « Gatsby believed in the green light, the orgastic future that year by year recedes before us. »\n"
 "Document 2 : extrait de The Grapes of Wrath (John Steinbeck, 1939) sur les migrants « Okies ».\n"
 "Question : « How do American writers of the 1920s and 1930s challenge the myth of the American Dream? » (300 words, in English).",
 "Corrigé indicatif. Introduction : define the American Dream (social mobility through hard work) and introduce both authors and their historical contexts (the Jazz Age / the Great Depression).\n"
 "I. Fitzgerald's disillusionment: the green light symbolises an always-deferred future; Gatsby's wealth is built on illegal activities and his love for Daisy is an illusion. The narrator Nick observes the moral corruption of the rich.\n"
 "II. Steinbeck's social protest: the Joad family loses its farm and discovers exploitation in California; the novel opposes individual success to collective solidarity.\n"
 "III. Comparison: both writers denounce a myth that hides inequality, but Fitzgerald emphasises moral emptiness while Steinbeck stresses economic injustice. Useful vocabulary: disillusionment, social mobility, critique, symbolic, hardship, solidarity.\n"
 "Conclusion: the American Dream functions as a compelling narrative that literature exposes as partly fictional, without completely abandoning the hope it carries."))

AN.append(a("Sujet type bac – LCA (latin), version et commentaire : Cicéron", "LCA",
 "Sujet type – épreuve de spécialité LCA (latin), version et questions de civilisation (5 points).\n"
 "Texte à traduire : « Quousque tandem abutere, Catilina, patientia nostra ? Quamdiu etiam furor iste tuus nos eludet ? Quem ad finem sese effrenata iactabit audacia ? » (Cicéron, Première Catilinaire, 63 av. J.-C.)\n"
 "Questions : 1° Traduire le passage. 2° Relever et nommer les procédés rhétoriques. 3° Présenter le contexte politique de 63 av. J.-C.",
 "Corrigé indicatif. 1° Traduction : « Jusqu'à quand, Catilina, abuseras-tu de notre patience ? Combien de temps encore cette fureur te jouera-t-elle de nous ? À quelle limite portera ton audace déchaînée ? »\n"
 "2° Procédés : anaphore interrogative (quousque / quamdiu / quem ad finem), vocatif et apostrophe directe (« Catilina »), antithèse entre « patientia nostra » (patience du Sénat) et « furor iste tuus » (fureur de Catilina), métaphore de l'audace « effrenata » (sans frein, comme un cheval emporté), accumulation qui crée un effet de crescendo.\n"
 "3° Contexte : en 63 av. J.-C., Cicéron est consul. Lucius Sergius Catilina, ancien préteur endetté, prépare un coup d'État avec des partisans. Le Sénat vote le senatus consultum ultimum ; Catilina quitte Rome et est battu à Pistoia en 62. Les discours de Cicéron visent à isoler le conjuré et à rassurer l'opinion.\n"
 "Ouverture : on rapprochera ce texte de la rhétorique aristotélicienne (genre délibératif) et de la figure de l'orateur idéal développée dans De Oratore."))

save("lead-general-partie-B.json", F, AN)
print("Partie B:", len(F), "fiches,", len(AN), "annales")
