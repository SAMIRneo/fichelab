# PARTIE A — tronc commun de la voie générale (2nde, 1re, Terminale)
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lg_common import f, q, t, a, save

F, AN = [], []

SF2 = "Programme de français de classe de seconde, arrêté du 17 janvier 2019, BO spécial n° 1 du 22 janvier 2019, éduscol"
SF1 = "Programme de français de classe de première, BO spécial n° 1 du 22 janvier 2019 (épreuve anticipée), éduscol"
SPH = "Programme de philosophie de terminale générale, arrêté du 19 juillet 2019, BO spécial n° 8 du 25 juillet 2019, éduscol"
SHG = "Programme d'histoire-géographie du lycée général, arrêté du 17 janvier 2019, BO spécial n° 1 du 22 janvier 2019 ; programmes actualisés 2026, éduscol"
SEMC = "Programme d'éducation morale et civique du lycée, BO spécial n° 1 du 22 janvier 2019, éduscol ; socle commun, BO n° 11 du 26 novembre 2015"
SM2 = "Programme de mathématiques de la classe de seconde générale et technologique, BO n° 14 du 2 avril 2026, éduscol"
SM1 = "Programme de mathématiques intégré à l'enseignement scientifique de première générale, BO n° 14 du 2 avril 2026, éduscol"
SMT = "Programme d'enseignement optionnel de mathématiques complémentaires de terminale générale, BO n° 14 du 2 avril 2026, éduscol"
SLV = "Programme de langues vivantes du lycée général et technologique, BO n° 22 du 29 mai 2026 ; arrêté du 17 janvier 2019, éduscol"
SEPS = "Programme d'éducation physique et sportive du lycée, BO spécial n° 1 du 22 janvier 2019 ; circulaire d'examen 2026, éduscol"
SES = "Programme d'enseignement scientifique du lycée général, arrêté du 17 janvier 2019, BO spécial n° 1 du 22 janvier 2019, éduscol"

# ---------------- FRANÇAIS ----------------
F.append(f(["2nde"], "Français", "Chapitre : Le roman et le récit du Moyen Âge au XVIIIe siècle", SF2, [
 "Le programme de seconde fait du roman et du récit un objet d'étude couvrant le Moyen Âge au XXIe siècle ; la première séquence s'intéresse aux récits médiévaux et classiques.",
 "Au Moyen Âge, le roman courtois (Chrétien de Troyes, Le Chevalier au lion, vers 1180) mêle aventure merveilleuse et code de l'amour courtois ; le lai de Marie de France met en scène des situations tragiques en vers octosyllabiques.",
 "Le Roman de Renart (XIIe-XIIIe siècles) est une parodie animale du roman courtois : les animaux parlent et raillent la société féodale et le clergé.",
 "Au XVIIe siècle, la « question du roman » est débattue : on reproche au roman d'être une fiction mensongère ; Madeleine de Scudéry répond par la « clé », lecture allégorique des romans de mœurs.",
 "Le roman comique de Scarron (1651) et le roman burlesque renouvellent le genre par la satire et le réalisme comique des troupes de comédiens.",
 "Au XVIIIe siècle, le roman épistolaire se codifie : Lettres persanes (Montesquieu, 1721) utilise le regard de deux Persans pour critiquer la société française par le décalage ethnographique.",
 "Rousseau publie Julie ou la Nouvelle Héloïse (1761) : le roman épistolaire devient le lieu d'une morale sensible et d'une critique de l'inégalité sociale.",
 "L'étude du récit exige de distinguer le narrateur de l'auteur, le temps de l'histoire et le temps du récit (ordre, durée, fréquence), et le point de vue (externe, interne, omniscient).",
 "La lecture du texte médiéval suppose une adaptation : traduction, orthographe modernisée et repérage des formules épiques (laisses, épithètes, répétitions).",
 "Les notions à maîtriser pour l'écrit sont le registre (comique, tragique, pathétique), le champ lexical et les figures de style qui construisent le sens du passage."
], [
 q("Quel auteur a écrit Le Chevalier au lion vers 1180 ?", ["Chrétien de Troyes", "Marie de France", "Rabelais", "Scarron"], 0, "Chrétien de Troyes est le principal romancier courtois du XIIe siècle ; Le Chevalier au lion met en scène Yvain."),
 q("Quel ouvrage de Montesquieu paru en 1721 utilise le regard de deux Persans ?", ["Lettres persanes", "Julie ou la Nouvelle Héloïse", "Candide", "Le Roman comique"], 0, "Les Lettres persanes (1721) font d'Usbek et Rica des observateurs critiques de la France de la Régence."),
 q("Qu'appelle-t-on une « clé » dans le roman du XVIIe siècle ?", ["Une grille de lecture allégorique", "Une serrure symbolique", "Un personnage comique", "Un procédé de rime"], 0, "La clé permet de reconnaître, derrière les personnages romanesques, des personnalités réelles de la société du temps."),
 q("Dans quelle forme Marie de France écrit-elle ses lais ?", ["En alexandrins", "En octosyllabiques", "En vers libres", "En prose"], 1, "Les lais de Marie de France sont des récits en octosyllabiques, souvent brefs et tragiques."),
 q("Quel est le rôle du narrateur dans un récit à focalisation interne ?", ["Il sait tout des personnages", "Il adopte le point de vue d'un personnage", "Il commente l'action du dehors", "Il est absent du texte"], 1, "La focalisation interne limite le récit à ce que sait, voit et ressent un personnage."),
 t("Comment le Roman de Renart parodie-t-il le roman courtois ?", "Il remplace les chevaliers par des animaux qui parlent et se moquent des valeurs féodales.", "La parodie animale inverse les codes courtois : ruse et appétit remplacent l'honneur et l'amour idéalisé, pour une satire de la société médiévale."),
 t("Quelle différence établir entre temps de l'histoire et temps du récit ?", "Le temps de l'histoire est la chronologie des événements ; le temps du récit est l'ordre dans lequel le narrateur les présente.", "Le narrateur peut inverser, accélérer ou ralentir la chronologie : c'est l'objet de l'analyse des effets de temps (analepse, ellipse, scène)."),
 t("Pourquoi Lettres persanes est-il un roman d'observation critique ?", "Parce que le regard extérieur des deux Persans rend visibles les absurdités des institutions et des mœurs françaises.", "Le décalage culturel est un procédé de distanciation : Montesquieu peut critiquer la monarchie, la religion et les salons sans s'exposer directement.")
])),

F.append(f(["2nde"], "Français", "Chapitre : La poésie du XIXe au XXIe siècle : romantisme et modernité", SF2, [
 "Le programme de seconde étudie la poésie du XIXe au XXIe siècle à partir de recueils et de textes qui font de la forme poétique un enjeu esthétique.",
 "Le romantisme exalte le moi, le sentiment et la nature : Hugo publie Les Contemplations en 1856 et La Légende des siècles en 1859, où le poète se dit « pasteur d'hommes ».",
 "Baudelaire publie Les Fleurs du mal en 1857 : le recueil est condamné pour outrage aux mœurs et invente une modernité faite de spleen, de correspondances et de beauté étrange.",
 "Verlaine et Rimbaud incarnent la « poésie maudite » : Le Bateau ivre (1871) et les Illuminations rompent avec la versification classique par le vers libre et le dérèglement des sens.",
 "Mallarmé pousse la suggestion à son comble : « L'après-midi d'un faune » (1876) fait du silence et du blanc des vers une partie du sens, ouvrant la voie au symbolisme.",
 "Apollinaire théorise le vers libre dans Alcools (1913) et invite le calligramme : le poème se donne à lire comme une image, le « Zone » mêle actualité et mythologie.",
 "Le surréalisme (Breton, Éluard, Aragon) revendique l'écriture automatique et l'image inattendue : « Liberté » superpose le politique et le rêve.",
 "La poésie du XXe siècle s'engage aussi : Éluard écrit « Liberté » en 1942 dans la clandestinité ; René Char publie les Feuillets d'Hypnos en 1946.",
 "L'analyse d'un poème porte sur le rythme (mètre, césure, enjambement), les sonorités (allitérations, assonances), les images (métaphore, comparaison, symbole) et la structure du recueil.",
 "Le commentaire doit toujours relier la forme au sens : le vers libre n'est pas l'absence de rythme mais une autre organisation de la voix poétique."
], [
 q("Quel recueil de Baudelaire est condamné en 1857 ?", ["Les Contemplations", "Les Fleurs du mal", "Alcools", "Le Bateau ivre"], 1, "Les Fleurs du mal (1857) font l'objet d'une condamnation partielle pour outrage aux mœurs ; six pièces sont retranchées."),
 q("Qui a écrit Le Bateau ivre en 1871 ?", ["Paul Verlaine", "Arthur Rimbaud", "Stéphane Mallarmé", "Guillaume Apollinaire"], 1, "Rimbaud compose Le Bateau ivre en 1871 : le poème est un récit de voyage halluciné en alexandrins libérés."),
 q("Quel poète a inventé le calligramme ?", ["Hugo", "Baudelaire", "Apollinaire", "Éluard"], 2, "Apollinaire publie des calligrammes dans Alcools (1913) et Calligrammes (1918) : la disposition typographique dessine l'objet chanté."),
 q("Quel mouvement littéraire revendique l'écriture automatique ?", ["Le romantisme", "Le parnasse", "Le surréalisme", "Le classicisme"], 2, "Le surréalisme, fondé par Breton en 1924, explore l'écriture automatique et les associations libres."),
 q("Que désigne le « spleen » chez Baudelaire ?", ["Une forme de gaîté", "Un état de mélancolie et d'enfermement", "Un genre poétique antique", "Une rime riche"], 1, "Le spleen est la mélancolie moderne : l'impuissance à s'évader du temps et de la douleur, que le poète tente de vaincre par l'idéal."),
 t("Comment le vers libre se distingue-t-il du vers classique ?", "Il refuse le mètre et la rime réguliers mais garde un rythme et des images.", "Le vers libre, théorisé par Apollinaire, substitue au mètre fixe une respiration et une architecture internes, sans renoncer à la musicalité."),
 t("Qu'est-ce que la théorie des correspondances chez Baudelaire ?", "C'est l'idée que les sens et le monde visible répondent à un monde invisible de symboles.", "Le sonnet « Correspondances » (1857) pose que la nature est un réseau de signes à interpréter, où les parfums, les couleurs et les sons se répondent."),
 t("Pourquoi la poésie d'Éluard pendant la guerre est-elle engagée ?", "Parce qu'elle répond à l'oppression nazie par un langage simple et collectif, diffusé clandestinement.", "« Liberté » (1942) est écrit pour résister : le poème répète un mot-devise et transforme le lecteur en complice de la lutte.")
])),

F.append(f(["1re"], "Français", "Chapitre : Le roman et le récit du XVIIIe au XXIe siècle (épreuve anticipée)", SF1, [
 "En classe de première, l'objet d'étude « Le roman et le récit du XVIIIe au XXIe siècle » prépare l'épreuve anticipée de français écrite et orale.",
 "Les Lumières utilisent le récit comme laboratoire d'idées : Candide (Voltaire, 1759) critique l'optimisme et les institutions par le voyage et l'ironie.",
 "Le roman réaliste s'impose au XIXe siècle : Balzac construit La Comédie humaine (1829-1848) comme une « histoire naturelle de la société » ; Flaubert publie Madame Bovary en 1857.",
 "Le naturalisme de Zola (Les Rougon-Macquart, 1871-1893) applique au roman une méthode expérimentale : le milieu et l'hérédité déterminent les personnages.",
 "Le récit se fragmente au XXe siècle : Proust (À la recherche du temps perdu, 1913-1927) fait de la mémoire involontaire le principe même de la narration.",
 "Camus publie L'Étranger en 1942 : le récit à la première personne et le style « blanc » traduisent l'absurde et le détachement du narrateur.",
 "Sartre et les existentialistes mettent le récit au service d'une philosophie de la liberté ; La Nausée (1938) interroge la contingence des choses.",
 "Les récits de guerre et de déportation (Primo Levi, Si c'est un homme, 1947) posent la question du témoignage et des limites de la représentation.",
 "La lecture doit repérer le statut du narrateur, la focalisation, le traitement du temps et la manière dont le récit construit une critique sociale ou une réflexion sur la condition humaine.",
 "À l'écrit, la dissertation et le commentaire littéraires exigent une problématique, un plan structuré et des exemples précis tirés des œuvres du programme."
], [
 q("Quel roman de Voltaire critique l'optimisme en 1759 ?", ["Candide", "Emile", "Le Contrat social", "Les Misérables"], 0, "Candide ou l'Optimisme (1759) est un conte philosophique qui réfute le « meilleur des mondes possibles »."),
 q("Comment s'intitule le cycle romanesque d'Émile Zola ?", ["La Comédie humaine", "Les Rougon-Macquart", "À la recherche du temps perdu", "Le Cycle de Dune"], 1, "Les Rougon-Macquart (1871-1893) comprennent vingt volumes étudiant une famille sous le Second Empire."),
 q("Quel roman de Camus paraît en 1942 ?", ["La Nausée", "L'Étranger", "Le Mythe de Sisyphe", "La Peste"], 1, "L'Étranger (1942) est publié avant Le Mythe de Sisyphe (1942) et La Peste (1947)."),
 q("Qui a écrit À la recherche du temps perdu ?", ["Marcel Proust", "Gustave Flaubert", "Honoré de Balzac", "Jean-Paul Sartre"], 0, "Proust publie les sept volumes de sa recherche entre 1913 et 1927 ; la mémoire involontaire en est le moteur."),
 q("Quel est l'objet du réalisme balzacien ?", ["Décrire la société et ses déterminismes", "Chanter l'amour courtois", "Raconter des voyages merveilleux", "Explorer l'inconscient"], 0, "Balzac se donne pour ambition de peindre toutes les classes et tous les métiers de son époque dans La Comédie humaine."),
 t("Qu'est-ce que le « style blanc » de Camus dans L'Étranger ?", "Une écriture simple, descriptive, qui refuse les effets pathétiques et les jugements.", "Meursault rapporte les faits sans commentaire : cette neutralité apparente produit un effet d'étrangeté et fait sentir l'absurde de l'existence."),
 t("Quelle différence oppose roman réaliste et roman naturaliste ?", "Le réalisme décrit les mœurs ; le naturalisme ajoute une explication scientifique par l'hérédité et le milieu.", "Zola se réclame de Claude Bernard : le roman devient une expérience où l'on observe comment les caractères réagissent aux influences sociales et biologiques."),
 t("Comment le terme « focalisation » aide-t-il à analyser un récit ?", "Il désigne le point de vue adopté par le narrateur : externe, interne ou omniscient.", "La focalisation détermine ce que le lecteur sait et ne sait pas ; elle crée du suspense, de l'ironie ou de l'identification selon le cas.")
])),

F.append(f(["1re"], "Français", "Chapitre : La littérature d'idées et la presse aux XVIIIe et XIXe siècles", SF1, [
 "L'objet d'étude « Littérature d'idées et presse aux XVIIIe et XIXe siècles » prépare l'épreuve anticipée en entraînant à l'argumentation et à la lecture de documents.",
 "Les philosophes des Lumières écrivent pour convaincre : Voltaire publie le Traité sur la tolérance en 1763 après l'affaire Calas, Rousseau le Contrat social en 1762.",
 "Montesquieu publie De l'esprit des lois en 1748 : la théorie de la séparation des pouvoirs devient un modèle pour les constitutions modernes.",
 "La presse naît et se développe : le Journal des savants (1665) puis la Gazette ; au XIXe siècle, le journal devient un acteur politique et commercial de premier plan.",
 "Le roman-feuilleton, popularisé par Eugène Sue (Les Mystères de Paris, 1842-1843), est publié en épisodes dans Le Constitutionnel et fidélise un lectorat de masse.",
 "Zola publie « J'Accuse... ! » dans L'Aurore le 13 janvier 1898 : l'article est un modèle de polémique argumentée en faveur de Dreyfus.",
 "Hugo intervient dans le débat public (Les Misérables, 1862) et ses discours à l'Assemblée font de l'écrivain une conscience politique.",
 "L'analyse d'un texte argumentatif repose sur la distinction entre thèse, arguments, exemples et réfutation, et sur l'étude des procédés rhétoriques (analogie, ironie, accumulation, question rhétorique).",
 "Le débat journalistique mêle information et opinion ; savoir repérer le genre de l'article (éditorial, chronique, reportage, lettre ouverte) est indispensable.",
 "L'épreuve écrite de première propose un commentaire, une dissertation ou une contraction suivie d'un essai ; la maîtrise de l'argumentation y est déterminante."
], [
 q("Dans quel journal Zola publie-t-il « J'Accuse... ! » ?", ["Le Figaro", "L'Aurore", "Le Constitutionnel", "La Libre Parole"], 1, "L'article paraît dans L'Aurore du 13 janvier 1898, sous la forme d'une lettre ouverte au président de la République."),
 q("Quel est l'auteur de De l'esprit des lois (1748) ?", ["Voltaire", "Rousseau", "Montesquieu", "Diderot"], 2, "Montesquieu y expose la séparation des pouvoirs législatif, exécutif et judiciaire."),
 q("Quel roman-feuilleton d'Eugène Sue paraît à partir de 1842 ?", ["Les Misérables", "Les Mystères de Paris", "Le Comte de Monte-Cristo", "La Dame aux camélias"], 1, "Les Mystères de Paris est publié en feuilleton dans Le Constitutionnel de 1842 à 1843 et connaît un immense succès."),
 q("Que désigne la « thèse » d'un texte argumentatif ?", ["L'exemple choisi", "L'opinion défendue", "La conclusion seulement", "Une figure de style"], 1, "La thèse est l'affirmation centrale que l'auteur cherche à faire admettre ; les arguments en sont les justifications."),
 q("Quel événement est à l'origine du Traité sur la tolérance ?", ["L'affaire Dreyfus", "L'affaire Calas", "La Révolution française", "Le procès de Socrate"], 1, "Voltaire écrit en 1763 pour réhabiliter Jean Calas, protestant injustement condamné."),
 t("Comment fonctionne la réfutation dans un texte d'idées ?", "Elle consiste à énoncer l'objection adverse puis à la démontrer fausse ou insuffisante.", "La réfutation renforce la thèse en anticipant les critiques : l'auteur donne l'impression d'avoir déjà répondu à son contradicteur."),
 t("Pourquoi la presse est-elle un objet d'étude du programme de première ?", "Parce qu'elle est devenue un espace public de débat et de diffusion des idées, avec ses genres et ses stratégies.", "L'étude de la presse permet de comprendre comment l'opinion se construit, entre information, commentaire et mise en scène rhétorique."),
 t("Quel est l'intérêt de la contraction d'un texte pour l'épreuve de français ?", "Elle impose de distinguer l'essentiel de l'anecdotique et de restituer fidèlement une argumentation.", "L'exercice évalue la compréhension et la synthèse : il faut conserver la thèse, les arguments principaux et l'enchaînement logique.")
])),

# ---------------- PHILOSOPHIE ----------------
F.append(f(["Terminale"], "Philosophie", "Chapitre : La conscience et l'inconscient – le problème du sujet", SPH, [
 "Le thème « La conscience » ouvre le programme de terminale : la conscience désigne à la fois le fait d'être présent à soi et le fait de savoir que l'on pense.",
 "Descartes fait du cogito le fondement de la philosophie : « je pense, donc je suis » est une intuition immédiate qui résiste au doute méthodique (Discours de la méthode, 1637).",
 "La conscience cartésienne est transparente à elle-même : le sujet est une substance pensante (res cogitans) distincte de la substance étendue (res extensa).",
 "Locke propose une autre approche : la conscience est une perception interne de nos opérations, liée à la mémoire ; l'identité personnelle repose sur la continuité du souvenir.",
 "Hume conteste l'unité du moi : quand je m'observe, je ne rencontre qu'un flux de perceptions, jamais un « moi » stable (Traité de la nature humaine, 1739-1740).",
 "Freud ouvre une brèche décisive : l'inconscient est un réservoir de désirs refoulés qui se manifestent dans les rêves, les lapsus, les actes manqués et les symptômes (L'Interprétation du rêve, 1900).",
 "Freud distingue le ça, le moi et le surmoi : le moi n'est pas maître de ses propres désirs, il négocie entre les pulsions, la réalité et l'exigence morale.",
 "Sartre conteste la notion d'inconscient : la « mauvaise foi » est une conscience qui se déguise à elle-même, un projet de fuite de sa liberté (L'Être et le Néant, 1943).",
 "Merleau-Ponty rappelle que la conscience est incarnée : elle est d'abord un « corps propre » engagé dans le monde, avant d'être un regard abstrait.",
 "Le problème philosophique reste ouvert : si une partie de notre vie psychique nous échappe, peut-on encore parler d'un sujet souverain et responsable de ses actes ?"
], [
 q("Quel est le fondateur de la psychanalyse ?", ["Descartes", "Sigmund Freud", "Jean-Paul Sartre", "John Locke"], 1, "Freud publie L'Interprétation du rêve en 1900 et pose la notion d'inconscient comme objet d'étude."),
 q("Que signifie le cogito cartésien ?", ["Je doute, donc j'existe seulement si je prouve Dieu", "Je pense, donc je suis", "Je sens, donc je suis", "Je veux, donc je suis libre"], 1, "Le cogito est l'intuition que l'existence du sujet pensant est certaine au moment même où il pense."),
 q("Qui a critiqué l'unité du moi en le réduisant à un faisceau de perceptions ?", ["Hume", "Descartes", "Kant", "Hegel"], 0, "Hume soutient qu'il ne se saisit jamais que d'une succession de perceptions, sans « moi » permanent."),
 q("Quel est le rôle du surmoi dans la topique freudienne ?", ["Il représente les pulsions", "Il représente l'exigence morale et l'interdit", "Il assure la perception", "Il est le souvenir"], 1, "Le surmoi intègre les interdits parentaux et sociaux ; il juge et culpabilise le moi."),
 q("Comment Sartre définit-il la mauvaise foi ?", ["Un mensonge aux autres", "Une conscience qui se déguise à elle-même", "Une erreur de jugement", "Une omission involontaire"], 1, "La mauvaise foi est un projet : le sujet choisit de se donner le change pour fuir sa liberté et sa responsabilité."),
 t("Comment Descartes répond-il au scepticisme ?", "En découvrant dans le doute même une certitude : l'existence de la pensée qui doute.", "Le doute est méthodique et provisoire ; il conduit au cogito, première évidence à partir de laquelle la connaissance peut être reconstruite."),
 t("Quelle est la différence entre le « moi » et le « ça » chez Freud ?", "Le ça est la source des pulsions inconscientes ; le moi est l'instance qui négocie avec la réalité.", "Le moi n'est pas le maître de la maison : il doit composer avec le ça, le surmoi et les exigences du monde extérieur."),
 t("En quoi la conscience est-elle « incarnée » selon Merleau-Ponty ?", "Elle est toujours celle d'un corps situé dans le monde, qui perçoit et agit avant de penser.", "La phénoménologie refuse de séparer l'esprit du corps : le « corps propre » est notre première manière d'être au monde.")
])),

F.append(f(["Terminale"], "Philosophie", "Chapitre : La liberté – déterminisme, libre arbitre et émancipation", SPH, [
 "Le thème « La liberté » demande d'articuler l'expérience de la délibération avec les contraintes qui pèsent sur l'action.",
 "Le déterminisme scientifique (Laplace, Essai philosophique sur les probabilités, 1814) suppose que l'état présent du monde détermine son état futur : toute chose aurait une cause nécessaire.",
 "Diderot illustre le déterminisme dans Jacques le fataliste (1796) : le personnage croit à un « grand livre » où tout est écrit, tout en agissant comme s'il choisissait.",
 "Kant répond au déterminisme par la distinction entre phénomènes et noumènes : l'homme, comme être de raison, est libre même si, comme être sensible, il est soumis aux causes.",
 "Sartre radicalise la liberté : « nous sommes condamnés à être libres » ; l'existence précède l'essence et l'homme se définit par ses choix (L'Existentialisme est un humanisme, 1946).",
 "Mais la liberté est aussi une expérience politique : Rousseau (Du contrat social, 1762) définit la liberté comme l'obéissance à la loi que l'on s'est prescrite soi-même.",
 "Constant distingue la liberté des Anciens (participation directe au pouvoir) et la liberté des Modernes (protection de l'indépendance privée), dans un discours de 1819.",
 "La psychologie et la sociologie tempèrent l'idée d'un sujet souverain : les habitudes, l'inconscient, les normes sociales et les situations réduisent la marge de choix réelle.",
 "La question philosophique est donc de savoir si la liberté est une illusion subjective ou une exigence irréductible de la raison et de la morale.",
 "Une copie réussie doit définir les termes, montrer l'opposition entre déterminisme et libre arbitre, puis proposer un dépassement (par exemple la liberté comme élasticité de la raison ou comme émancipation)."
], [
 q("Quel est le titre de l'essai de Laplace sur le déterminisme ?", ["Essai philosophique sur les probabilités", "Discours de la méthode", "Traité de la nature humaine", "La Liberté des Modernes"], 0, "Laplace expose en 1814 l'idée qu'une intelligence connaissant toutes les causes pourrait prédire l'avenir."),
 q("Qui a écrit « Nous sommes condamnés à être libres » ?", ["Sartre", "Kant", "Rousseau", "Diderot"], 0, "La formule est de Sartre : la liberté n'est pas un don mais une charge, puisque chacun répond de ses choix."),
 q("Comment Kant concilie-t-il liberté et déterminisme ?", ["En niant le déterminisme", "En distinguant le monde des phénomènes et celui des noumènes", "En niant la responsabilité", "En admettant le hasard pur"], 1, "Comme phénomène, l'homme est soumis aux causes ; comme noumène, il est libre et moralement responsable."),
 q("Quelle distinction Benjamin Constant a-t-il proposée en 1819 ?", ["Liberté des Anciens / liberté des Modernes", "Liberté positive / liberté négative", "Liberté intérieure / liberté extérieure", "Liberté politique / liberté économique"], 0, "Constant oppose la participation citoyenne directe des Anciens à la protection de l'indépendance individuelle des Modernes."),
 q("Selon Rousseau, la liberté consiste à…", ["Faire ce que l'on veut sans contrainte", "Obéir à la loi que l'on s'est donnée", "Refuser toute autorité", "Suivre ses désirs"], 1, "La liberté républicaine n'est pas l'arbitraire : elle est l'obéissance à une volonté générale dont on est soi-même membre."),
 t("Pourquoi Sartre parle-t-il de « condamnation » à la liberté ?", "Parce que l'homme ne choisit pas d'être libre mais doit porter la responsabilité de tous ses actes.", "Nous n'avons pas choisi d'exister, mais une fois jetés dans le monde, nous ne pouvons déléguer le sens de nos choix à une nature ou à un destin."),
 t("Qu'est-ce que le « grand livre » dans Jacques le fataliste ?", "Une image du déterminisme : tout serait écrit d'avance, même si les personnages agissent comme s'ils choisissaient.", "Diderot se joue du lecteur : il expose le fatalisme tout en montrant que l'action et le récit exigent l'illusion de la liberté."),
 t("La liberté est-elle incompatible avec les normes sociales ?", "Non : elles peuvent au contraire rendre la liberté possible en garantissant les conditions de l'autonomie.", "La conception républicaine (Rousseau, Kant) fait de la loi une condition de la liberté, tandis qu'une conception libérale la conçoit comme protection d'un domaine privé.")
])),

F.append(f(["Terminale"], "Philosophie", "Chapitre : La vérité – scepticisme, évidence et critères du vrai", SPH, [
 "Le thème « La vérité » interroge la possibilité de distinguer le vrai du faux et les critères qui permettent de le faire.",
 "Le scepticisme antique (Sextus Empiricus) suspend le jugement (épochè) devant l'opposition des opinions et l'incertitude des sens.",
 "Montaigne reprend cette attitude dans les Essais : « Que sais-je ? » exprime une modestie de la raison qui ne renonce pas pour autant au jugement.",
 "Descartes répond par le critère de l'évidence : est vrai ce qui apparaît avec clarté et distinction à un esprit attentif, comme le cogito.",
 "Le critère de cohérence (Leibniz) exige la non-contradiction : les vérités de raison sont nécessaires, tandis que les vérités de fait sont contingentes.",
 "Le critère de correspondance (Aristote) définit la vérité comme l'accord de l'énoncé avec la réalité : « dire de ce qui est qu'il est ».",
 "Le pragmatisme (William James, John Dewey) juge une idée à son efficacité et à ses conséquences vérifiables dans l'expérience.",
 "Nietzsche conteste la valeur absolue de la vérité : elle serait une « mobilité de métaphores » et un instrument au service de la vie plutôt qu'un reflet du réel.",
 "Hannah Arendt distingue la vérité de fait, fragile et politique, de la vérité rationnelle : les régimes totalitaires s'attaquent d'abord aux faits.",
 "Le débat contemporain sur les « post-vérités » et les réseaux sociaux prolonge ces questions : la vérité a besoin de critères et d'institutions pour être reconnue."
], [
 q("Quel critère de vérité est associé à Leibniz ?", ["L'évidence", "La cohérence non contradictoire", "La sensation", "L'autorité"], 1, "Leibniz distingue vérités de raison (principe de non-contradiction) et vérités de fait (principe de raison suffisante)."),
 q("Qui a formulé la devise « Que sais-je ? » ?", ["Montaigne", "Descartes", "Pascal", "Nietzsche"], 0, "Montaigne place cette question comme devise sur son tour et dans les Essais, marquant un scepticisme modéré."),
 q("Selon Aristote, la vérité est…", ["L'accord de l'énoncé avec la réalité", "L'utilité de l'énoncé", "La clarté de l'idée", "Le consensus"], 0, "Aristote définit la vérité comme la correspondance entre le discours et ce qui est, dans la Métaphysique."),
 q("Quel courant juge une idée d'après ses effets et son efficacité ?", ["Le rationalisme", "Le pragmatisme", "Le scepticisme", "Le platonisme"], 1, "Le pragmatisme (James, Dewey) fait de la vérification par les conséquences le critère de la vérité."),
 q("Qui a parlé de la vérité comme « mobilité de métaphores » ?", ["Nietzsche", "Kant", "Hegel", "Comte"], 0, "Nietzsche, dans « De la vérité et du mensonge au sens moral » (1873), conteste la transparence du langage."),
 t("Comment Descartes répond-il au scepticisme ?", "Par le doute méthodique qui conduit à l'évidence du cogito, première certitude indubitable.", "Le doute n'est pas un point d'arrêt mais un outil : il élimine ce qui peut être faux pour laisser subsister ce qui ne peut pas l'être."),
 t("Quelle est la différence entre vérité de fait et vérité de raison ?", "La vérité de raison est nécessaire et universelle ; la vérité de fait est contingente et fondée sur l'expérience.", "Leibniz illustre cette distinction : « 7 + 5 = 12 » est nécessaire, « Napoléon est mort à Sainte-Hélène » est vrai mais aurait pu ne pas l'être."),
 t("Pourquoi la vérité de fait est-elle fragile en politique ?", "Parce qu'elle repose sur des témoignages et des archives que le pouvoir peut nier ou détruire.", "Arendt montre que le totalitarisme ne se contente pas de mentir : il détruit les conditions mêmes de la vérification des faits.")
])),

F.append(f(["Terminale"], "Philosophie", "Chapitre : La justice, l'égalité et la reconnaissance", SPH, [
 "La justice est une valeur morale et politique qui consiste à rendre à chacun ce qui lui est dû ; elle est au cœur du thème du même nom au programme.",
 "Aristote distingue la justice distributive, qui répartit les biens selon une proportion géométrique et le mérite, de la justice commutative, qui corrige les torts selon une proportion arithmétique.",
 "La justice commutative s'applique aux contrats et aux délits : elle vise une égalité stricte entre ce qui est reçu et ce qui est donné.",
 "Kant fonde le droit sur la liberté de chacun compatible avec la liberté de tous : l'égalité devant la loi est une exigence de la raison pratique.",
 "Hegel va dans le même sens : l'État de droit garantit la « liberté dans l'obéissance » et l'« égalité devant la loi » (Principes de la philosophie du droit, 1821).",
 "Rawls (Théorie de la justice, 1971) imagine la « position originale » : derrière un voile d'ignorance, on ignore son talent, sa classe et son genre, ce qui conduit à choisir des principes justes.",
 "Nozick critique Rawls : toute redistribution serait une atteinte à la propriété de soi et aux droits individuels (Anarchie, État et Utopie, 1974).",
 "Fraser et Honneth déplacent le débat vers la reconnaissance : l'injustice n'est pas seulement une mauvaise répartition, mais aussi un déni de dignité et de considération.",
 "La question philosophique : faut-il traiter tous les êtres de la même manière (égalité formelle) ou tenir compte des différences de situation pour parvenir à une réelle équité ?",
 "La copie peut s'appuyer sur des exemples contemporains : discrimination salariale, quotas, égalité civile, réparations historiques, sans confondre justice et simple bienveillance."
], [
 q("Quel est le nom du dispositif imaginé par Rawls ?", ["Le cogito", "Le voile d'ignorance", "Le contrat social", "La main invisible"], 1, "Le voile d'ignorance place les individus dans une position originale où ils ne connaissent pas leur place dans la société."),
 q("Quelle distinction est propre à Aristote en matière de justice ?", ["Justice distributive / commutative", "Justice pénale / civile", "Justice sociale / individuelle", "Justice naturelle / positive"], 0, "La première répartit les biens selon le mérite, la seconde répare les torts et règle les échanges."),
 q("Qui a écrit Anarchie, État et Utopie en 1974 ?", ["John Rawls", "Robert Nozick", "Hegel", "Kant"], 1, "Nozick y défend un État minimal et critique les théories redistributives de Rawls."),
 q("Quelle proportion caractérise la justice commutative ?", ["Géométrique", "Arithmétique", "Exponentielle", "Harmonique"], 1, "Aristote parle de proportion arithmétique : le tort et la réparation doivent être égaux, indépendamment du mérite des personnes."),
 q("Quel est l'objet de la « reconnaissance » chez Honneth ?", ["La distribution des richesses", "La considération et la dignité des sujets", "La peine des crimes", "Le vote"], 1, "Honneth analyse trois formes de reconnaissance : amour, droit et estime sociale, dont le déni produit des souffrances spécifiques."),
 t("Quelle est la différence entre justice distributive et justice commutative ?", "La première répartit les biens selon une proportion ; la seconde vise l'égalité dans les échanges et la réparation des torts.", "La première concerne les rapports entre la collectivité et ses membres ; la seconde règle les relations entre particuliers."),
 t("Comment le voile d'ignorance garantit-il l'impartialité ?", "En empêchant chacun de choisir des principes adaptés à sa propre situation sociale.", "Si j'ignore si je serai riche ou pauvre, talentueux ou handicapé, je choisis des principes qui protègent les plus défavorisés (principe de différence)."),
 t("L'égalité formelle suffit-elle à la justice ?", "Non : elle traite différemment des situations inégales et peut laisser subsister des dominations réelles.", "La justice doit aussi prendre en compte les capacités d'agir (Sen) et la reconnaissance, sans quoi l'égalité devant la loi reste abstraite.")
])),

# ---------------- HISTOIRE-GÉOGRAPHIE ----------------
F.append(f(["2nde"], "Histoire-géographie", "Chapitre : Le monde méditerranéen médiéval (Ve–XVe siècle)", SHG, [
 "Le programme de seconde commence par l'étude du monde méditerranéen médiéval, situé entre l'héritage romain, le christianisme et l'islam.",
 "Après la disparition de l'Empire romain d'Occident en 476, l'Empire byzantin, centré sur Constantinople, conserve la tradition juridique et culturelle romaine pendant un millénaire.",
 "Le droit byzantin est codifié sous Justinien : le Corpus juris civilis (529-534) reste une référence majeure pour le droit européen.",
 "L'islam naît au VIIe siècle avec Mahomet ; la Hégire de 622 marque le début de l'ère musulmane et la constitution d'une communauté religieuse et politique.",
 "Les califats omeyyade (661-750) puis abbasside (750-1258) étendent leur domination de l'Espagne à l'Irak ; Bagdad devient un centre intellectuel et commercial.",
 "L'Europe latine se structure autour de la monarchie capétienne, du Saint-Empire romain germanique et de la chrétienté romaine, dont le pape est le chef spirituel.",
 "Les croisades (1095-1291) mettent en contact violent mais durable l'Occident latin et l'Orient : elles favorisent les échanges de techniques, de produits et d'idées.",
 "Les universités apparaissent aux XIe-XIIIe siècles (Bologne, Paris) : elles sont des corporations de maîtres et d'étudiants, avec des cursus et des grades.",
 "L'économie médiévale repose sur l'agriculture, les foires (Champagne) et les routes commerciales qui relient l'Occident aux ports d'Orient (Venise, Gênes).",
 "La peste noire (1347-1353) et la guerre de Cent Ans (1337-1453) bouleversent les équilibres démographiques et politiques de la fin du Moyen Âge."
], [
 q("En quelle année l'Empire romain d'Occident disparaît-il ?", ["395", "476", "622", "800"], 1, "La déposition de Romulus Augustule en 476 marque la fin de l'Empire romain d'Occident."),
 q("Quel empereur a fait codifier le droit romain au VIe siècle ?", ["Charlemagne", "Justinien", "Auguste", "Constantin"], 1, "Justinien fait élaborer le Corpus juris civilis entre 529 et 534, conservé à Byzance puis redécouvert en Occident."),
 q("Que commémore l'Hégire de 622 ?", ["La naissance de Mahomet", "Le départ de Mahomet vers Médine", "La prise de Jérusalem", "La fondation de Bagdad"], 1, "L'Hégire est le départ de La Mecque vers Médine ; elle marque le début du calendrier musulman."),
 q("Quelle dynastie succède aux Omeyyades en 750 ?", ["Les Fatimides", "Les Abbassides", "Les Almoravides", "Les Seldjoukides"], 1, "Les Abbassides renversent les Omeyyades et déplacent la capitale à Bagdad."),
 q("Quel est le rôle des universités médiévales ?", ["Former des clercs et des professionnels du droit et de la médecine", "Organiser les croisades", "Diriger les monarchies", "Frapper la monnaie"], 0, "Les universités sont des corporations enseignantes qui délivrent des grades et structurent le savoir savant."),
 t("Comment l'Empire byzantin a-t-il conservé l'héritage romain ?", "En maintenant le droit, la fiscalité et la culture grecque et romaine pendant un millénaire.", "Constantinople a préservé le Corpus juris civilis et la tradition des cités, transmis ensuite à l'Occident notamment après 1453."),
 t("Quels effets les croisades ont-elles eus sur les échanges ?", "Elles ont favorisé la circulation de produits, de techniques et de connaissances entre l'Occident et l'Orient.", "Elles ont aussi renforcé les tensions religieuses ; leur bilan est à la fois violence et ouverture commerciale et intellectuelle."),
 t("Pourquoi la peste noire est-elle un moment de rupture ?", "Elle a provoqué une chute démographique majeure et une réorganisation des rapports de travail et des prix.", "La mortalité, estimée entre un tiers et la moitié de la population européenne, a entraîné une pénurie de main-d'œuvre et des revendications sociales.")
])),

F.append(f(["2nde"], "Histoire-géographie", "Chapitre : L'ouverture atlantique et la formation d'un monde interconnecté (XVe–XVIIIe siècle)", SHG, [
 "À partir du XVe siècle, les Européens franchissent l'Atlantique : cette ouverture transforme les réseaux d'échange et les rapports de force mondiaux.",
 "Les Portugais, sous l'impulsion d'Henri le Navigateur, longent les côtes africaines ; Vasco de Gama atteint les Indes en 1498.",
 "Christophe Colomb, financé par les Rois catholiques, atteint les Antilles en 1492 : il croit être arrivé aux Indes, d'où le nom d'« Indiens ».",
 "Le traité de Tordesillas (1494) partage le monde entre la Castille et le Portugal selon un méridien, sans consulter les peuples concernés.",
 "Magellan accomplit le premier tour du monde entre 1519 et 1522 : l'expédition démontre l'unité des océans et l'étendue réelle du globe.",
 "L'échange colombien fait circuler plantes, animaux et maladies entre l'Ancien et le Nouveau Monde : maïs, pomme de terre, cacao, tabac, mais aussi variole et syphilis.",
 "La traite atlantique déporte des millions d'Africains vers les Amériques : le commerce triangulaire relie l'Europe, l'Afrique et les colonies sur trois siècles.",
 "Les monarchies européennes se consolident : la France de François Ier, l'Espagne de Charles Quint et l'Angleterre d'Henri VIII affrontent la Réforme et les guerres de religion.",
 "La Réforme protestante (Luther, 1517 ; Calvin, 1536) divise la chrétienté et conduit aux guerres de religion, dont la Saint-Barthélemy (1572) en France.",
 "Cette première mondialisation est inégale : elle enrichit les puissances maritimes et instruit, par la comparaison des sociétés, la réflexion des Lumières sur l'altérité."
], [
 q("Quel navigateur atteint les Indes en 1498 ?", ["Christophe Colomb", "Vasco de Gama", "Magellan", "Jacques Cartier"], 1, "Vasco de Gama contourne le cap de Bonne-Espérance et atteint Calicut en 1498."),
 q("Quel traité partage le monde entre l'Espagne et le Portugal en 1494 ?", ["Le traité de Tordesillas", "Le traité d'Utrecht", "Le traité de Versailles", "La paix d'Augsbourg"], 0, "Le traité de Tordesillas fixe une ligne de démarcation au sud des îles Canaries."),
 q("Qui a dirigé le premier tour du monde (1519-1522) ?", ["Magellan", "Colomb", "Vasco de Gama", "Amerigo Vespucci"], 0, "Magellan meurt en 1521 aux Philippines ; Juan Sebastián Elcano ramène l'expédition en Espagne en 1522."),
 q("Qu'appelle-t-on « échange colombien » ?", ["Un traité commercial", "La circulation des plantes, animaux et maladies entre les deux mondes", "Une bataille navale", "Une technique de navigation"], 1, "L'échange colombien désigne la diffusion réciproque des espèces et des pathogènes après 1492."),
 q("Quel est le principe du commerce triangulaire ?", ["Europe → Afrique → Amériques → Europe", "Europe → Asie → Europe", "Afrique → Europe → Asie", "Amériques → Asie → Afrique"], 0, "Les navires partent d'Europe avec des marchandises, chargent des esclaves en Afrique, puis du sucre et du coton aux Amériques."),
 t("Comment l'ouverture atlantique a-t-elle transformé le monde ?", "Elle a relié durablement les océans et les continents, créant un premier système mondial d'échanges.", "Les flux de marchandises, d'hommes et d'idées se sont accélérés, au prix de la traite, de la colonisation et de la domination des puissances maritimes."),
 t("Pourquoi le nom d'« Indiens » est-il une erreur ?", "Colomb croyait atteindre les Indes en arrivant aux Antilles en 1492.", "Le terme s'est propagé malgré la découverte d'un continent inconnu des Européens, confirmée par Amerigo Vespucci."),
 t("Quel lien existe-t-il entre ouverture atlantique et Lumières ?", "La découverte de sociétés différentes a nourri la réflexion sur la relativité des coutumes et des institutions.", "Montaigne (« Des cannibales ») et plus tard Voltaire utilisent le regard sur l'Autre pour critiquer l'Europe et ses prétentions.")
])),

F.append(f(["1re"], "Histoire-géographie", "Chapitre : La Révolution française et l'Empire (1789–1815)", SHG, [
 "En première, l'étude de la Révolution française s'inscrit dans la séquence « Révolutions et constructions nationales en Europe et en Amérique (XVIIIe–XIXe siècles) ».",
 "La crise de l'Ancien Régime est à la fois financière, sociale et politique : la dette publique, les privilèges de la noblesse et du clergé et la contestation des idées des Lumières précipitent la convocation des États généraux en 1789.",
 "La prise de la Bastille, le 14 juillet 1789, marque l'entrée du peuple de Paris dans la Révolution ; l'Assemblée constituante vote l'abolition des privilèges dans la nuit du 4 août.",
 "La Déclaration des droits de l'homme et du citoyen, adoptée le 26 août 1789, énonce les principes de liberté, d'égalité devant la loi, de souveraineté nationale et de séparation des pouvoirs.",
 "La Constitution de 1791 instaure une monarchie constitutionnelle ; la fuite de Louis XVI à Varennes (juin 1791) porte un coup grave à sa crédibilité.",
 "La guerre avec l'Autriche et la Prusse, puis la chute de la monarchie le 10 août 1792, conduisent à la proclamation de la République le 21 septembre 1792 et à l'exécution de Louis XVI le 21 janvier 1793.",
 "La Terreur (septembre 1793 – juillet 1794) est une réponse à la guerre civile et à la coalition étrangère ; le Comité de salut public, dirigé par Robespierre, est renversé par le 9 Thermidor an II (27 juillet 1794).",
 "Le Directoire (1795-1799) succède à la Convention ; il est renversé par le coup d'État du 18 Brumaire an VIII (9 novembre 1799), portant Napoléon Bonaparte au pouvoir.",
 "Napoléon devient empereur en 1804 ; le Code civil (1804) consacre l'égalité devant la loi et la propriété, tandis que le Concordat (1801) règle les relations avec l'Église catholique.",
 "La défaite de Waterloo (18 juin 1815) et le retour de Louis XVIII marquent la fin de l'Empire, mais la Révolution a durablement installé les principes de 1789 en Europe et en Amérique latine."
], [
 q("Quelle date est celle de la Déclaration des droits de l'homme et du citoyen ?", ["14 juillet 1789", "4 août 1789", "26 août 1789", "21 janvier 1793"], 2, "La DDHC est adoptée le 26 août 1789 par l'Assemblée constituante."),
 q("Quel événement met fin à la monarchie constitutionnelle ?", ["La prise de la Bastille", "La journée du 10 août 1792", "Le 18 Brumaire", "Waterloo"], 1, "L'insurrection du 10 août 1792 renverse Louis XVI ; la République est proclamée le 21 septembre suivant."),
 q("Qui dirige le Comité de salut public pendant la Terreur ?", ["Danton", "Robespierre", "Mirabeau", "La Fayette"], 1, "Robespierre est l'une des figures centrales du Comité de salut public jusqu'au 9 Thermidor (27 juillet 1794)."),
 q("Quel texte de 1804 consacre l'égalité devant la loi ?", ["La DDHC", "Le Code civil", "Le Concordat", "La Constitution de 1791"], 1, "Le Code civil des Français, promulgué en mars 1804, est l'un des grands apports juridiques de l'époque napoléonienne."),
 q("Quelle bataille met définitivement fin à l'Empire en 1815 ?", ["Austerlitz", "Iéna", "Waterloo", "Valmy"], 2, "Napoléon est battu à Waterloo le 18 juin 1815 par les forces coalisées commandées par Wellington et Blücher."),
 t("Quelles sont les causes de la crise de 1789 ?", "Des difficultés financières, sociales et politiques, aggravées par les idées des Lumières et le refus des privilèges.", "La dette de l'État, la résistance des ordres privilégiés et l'exemple américain rendent la convocation des États généraux inévitable."),
 t("Comment la souveraineté nationale s'exprime-t-elle en 1789 ?", "Par l'Assemblée nationale issue d'élections et par la Déclaration des droits qui font de la nation la source de tout pouvoir.", "L'article 3 de la DDHC érige la souveraineté en principe : « Elle réside essentiellement dans la Nation. »"),
 t("Quel bilan tirer de la Révolution française ?", "Elle a aboli les privilèges, instauré l'égalité juridique et la citoyenneté, mais a aussi connu la violence et l'exclusion des femmes.", "L'historiographie souligne la tension entre universalisme des principes et limites de leur application, notamment pour les femmes, les esclaves et les colonies.")
])),

F.append(f(["Terminale"], "Histoire-géographie", "Chapitre : La France de la IIIe République à la Ve République (1870–2000)", SHG, [
 "Le programme de terminale étudie les régimes politiques français contemporains et les mutations de la société et de l'État depuis 1870.",
 "La IIIe République est proclamée le 4 septembre 1870 après la défaite de Sedan et la capture de Napoléon III ; elle dure jusqu'en 1940.",
 "Les lois constitutionnelles de 1875 organisent un régime parlementaire bicaméral : le président de la République, le Sénat et la Chambre des députés se partagent le pouvoir.",
 "L'« affaire Dreyfus » (1894-1906) divise la société française entre dreyfusards et antidreyfusards ; Zola publie « J'Accuse... ! » en 1898.",
 "La laïcité est consacrée par la loi du 9 décembre 1905 sur la séparation des Églises et de l'État : elle garantit la liberté de culte et la neutralité de l'État.",
 "La Première Guerre mondiale (1914-1918) entraîne la destruction d'une grande partie du pays, environ 1,4 million de morts français et de profondes transformations sociales.",
 "L'entre-deux-guerres voit l'instabilité ministérielle, la crise de 1929 et la montée des extrêmes ; le 6 février 1934 marque une crise parlementaire grave.",
 "Après la défaite de 1940 et l'Occupation, la Libération (1944-1945) conduit à la IVe République (1946-1958), caractérisée par un régime parlementaire instable.",
 "Le 13 mai 1958, la crise algérienne provoque le retour de Charles de Gaulle ; la Constitution du 4 octobre 1958 instaure la Ve République, régime semi-présidentiel.",
 "La Ve République se caractérise par un président élu au suffrage universel direct depuis 1962, un Premier ministre responsable devant le Parlement et un Conseil constitutionnel créé en 1958."
], [
 q("En quelle année la IIIe République est-elle proclamée ?", ["1848", "1870", "1914", "1946"], 1, "La République est proclamée le 4 septembre 1870, après la défaite de Sedan."),
 q("Quelle loi consacre la laïcité en 1905 ?", ["La loi Ferry", "La loi sur la séparation des Églises et de l'État", "La loi de finance", "La loi d'amnistie"], 1, "La loi du 9 décembre 1905 sépare les Églises et l'État et garantit la liberté de culte."),
 q("Quel président est élu au suffrage universel direct à partir de 1962 ?", ["Le président de la République", "Le Premier ministre", "Le président du Sénat", "Le préfet"], 0, "Le référendum du 28 septembre 1962 institue l'élection du président au suffrage universel direct, effective en 1965."),
 q("Quel événement déclenche le retour de de Gaulle au pouvoir en 1958 ?", ["La crise de Suez", "La crise algérienne", "La grève générale", "La chute du Mur"], 1, "Le 13 mai 1958, le comité de salut public d'Alger et la menace de coup d'État imposent le retour de de Gaulle."),
 q("Quand la Constitution de la Ve République est-elle adoptée ?", ["1946", "1958", "1962", "1969"], 1, "La Constitution est adoptée par référendum le 28 septembre et promulguée le 4 octobre 1958."),
 t("Quelles sont les caractéristiques du régime de la IIIe République ?", "Un régime parlementaire avec un président au rôle effacé, deux chambres et une forte instabilité ministérielle.", "Les lois constitutionnelles de 1875 organisent un équilibre entre la Chambre des députés, le Sénat et le président, élu par les parlementaires."),
 t("Comment l'affaire Dreyfus a-t-elle transformé la vie politique ?", "Elle a opposé deux conceptions de la République et renforcé le camp républicain laïque et réformateur.", "L'affaire a durablement discrédité l'armée et l'Église catholique conservatrice et accéléré la séparation de 1905."),
 t("Qu'est-ce qui distingue la Ve République de la IVe ?", "Un président fort, élu directement, dispose de pouvoirs propres, notamment la dissolution et l'article 16.", "Le Parlement reste souverain mais le Premier ministre est nommé par le président, ce qui réduit l'instabilité ministérielle.")
])),

F.append(f(["Terminale"], "Histoire-géographie", "Chapitre : La géographie de la France dans la mondialisation : métropoles, territoires et réseaux", SHG, [
 "Le programme de géographie de terminale étudie la France dans la mondialisation et les recompositions de son territoire.",
 "Paris est une métropole mondiale : elle figure parmi les premiers centres financiers et culturels globaux, et exerce une fonction de commandement sur le réseau national.",
 "Lyon, Marseille, Lille, Toulouse et Bordeaux forment des métropoles régionales qui structurent l'espace national et rayonnent à l'échelle européenne.",
 "La métropolisation désigne la concentration des activités, des populations et des fonctions de commandement dans les grandes villes : elle creuse les écarts avec les espaces périphériques.",
 "Les espaces productifs se transforment : l'industrie se modernise et se concentre dans des pôles de compétitivité, tandis que les services et le numérique se développent dans les métropoles.",
 "L'agriculture française, fortement mécanisée et subventionnée par la PAC, occupe un tiers du territoire et fait de la France un grand exportateur de produits agroalimentaires.",
 "Les espaces ruraux sont multifonctionnels : ils produisent, hébergent des populations périurbaines et assurent des fonctions environnementales et récréatives.",
 "Les réseaux de transport et de communication (TGV, autoroutes, fibre, portuaire) organisent la continuité territoriale et l'insertion de la France dans les flux européens et mondiaux.",
 "L'aménagement du territoire vise à réduire les inégalités : la DATAR (délégation interministérielle à l'aménagement du territoire et à l'attractivité régionale) pilote cette politique depuis 1963.",
 "Les enjeux contemporains sont la transition écologique, l'attractivité des territoires, le vieillissement et les effets de la crise du logement dans les grandes agglomérations."
], [
 q("Quelle est la fonction première d'une métropole mondiale comme Paris ?", ["Fonction de commandement financier et culturel", "Fonction de production agricole", "Fonction minière", "Fonction de simple transit"], 0, "Paris concentre des sièges sociaux, des marchés financiers, des institutions culturelles et des fonctions de décision à portée globale."),
 q("Quel organisme pilote l'aménagement du territoire en France depuis 1963 ?", ["La DATAR", "L'INSEE", "Le CNRS", "La Cour des comptes"], 0, "La DATAR, créée en 1963, coordonne les politiques d'aménagement et d'attractivité des territoires."),
 q("Quel pourcentage approximatif du territoire français est occupé par l'agriculture ?", ["10 %", "30 %", "50 %", "70 %"], 1, "Environ un tiers du territoire métropolitain est consacré à l'agriculture, qui pèse fortement dans les paysages et l'économie."),
 q("Que désigne la « métropolisation » ?", ["La croissance démographique rurale", "La concentration des fonctions et des populations dans les grandes villes", "Le déclin des villes", "La décentralisation industrielle"], 1, "La métropolisation est un processus de concentration des activités de commandement et des flux dans les métropoles."),
 q("Quel est le rôle de la PAC dans l'agriculture française ?", ["Elle régule les prix et subventionne les exploitations", "Elle fixe les salaires", "Elle gère les universités", "Elle contrôle la pêche"], 0, "La politique agricole commune de l'Union européenne soutient les revenus agricoles et organise les marchés."),
 t("Comment les métropoles françaises s'intègrent-elles dans la mondialisation ?", "Par des flux de capitaux, d'entreprises, de touristes et d'étudiants, et par leur insertion dans les réseaux européens.", "Elles attirent des sièges internationaux, accueillent des événements mondiaux et connectent le territoire national aux grandes métropoles européennes."),
 t("Quels effets la métropolisation a-t-elle sur les territoires périphériques ?", "Elle peut provoquer un déséquilibre en concentrant emplois et services, tout en créant des dépendances fonctionnelles.", "Certains espaces périphériques se spécialisent dans le tourisme ou la production agricole et dépendent des flux et des décisions métropolitaines."),
 t("Pourquoi parle-t-on d'espaces ruraux « multifonctionnels » ?", "Parce qu'ils produisent, hébergent et protègent la biodiversité et les paysages.", "Ils ne sont plus seulement des espaces agricoles : ils accueillent des résidents périurbains, des activités de loisirs et assurent des services environnementaux.")
])),

# ---------------- MATHS TRONC, LV, EPS, SCIENTIFIQUE, EMC ----------------
F.append(f(["2nde"], "Maths", "Chapitre : Nombres, calcul littéral et équations (programme 2026)", SM2, [
 "Le nouveau programme de mathématiques de seconde, publié au BO n° 14 du 2 avril 2026, entre en application à la rentrée 2026-2027.",
 "Il s'organise autour des thèmes « Nombres et calculs », « Algèbre », « Fonctions », « Géométrie », « Statistiques et probabilités » et « Algorithmique et programmation ».",
 "Le chapitre d'algèbre porte sur le calcul littéral : développer, factoriser et réduire une expression pour en simplifier l'écriture.",
 "Les identités remarquables (a+b)² = a²+2ab+b², (a–b)² = a²–2ab+b² et (a+b)(a–b) = a²–b² sont des outils de factorisation essentiels.",
 "Résoudre une équation du premier degré ax + b = 0 repose sur les opérations inverses ; le cas a = 0 doit être discuté (une solution, aucune ou une infinité).",
 "Une équation du second degré ax² + bx + c = 0 se résout par le discriminant Δ = b² – 4ac : deux solutions si Δ > 0, une si Δ = 0, aucune si Δ < 0.",
 "Les fonctions affines ont la forme f(x) = ax + b : leur représentation graphique est une droite, avec a comme coefficient directeur et b comme ordonnée à l'origine.",
 "En géométrie, le théorème de Pythagore et son réciproque, le théorème de Thalès et les propriétés des droites parallèles et perpendiculaires sont au programme.",
 "En statistiques, on calcule moyenne, médiane, quartiles et écart-type, et on choisit la représentation graphique adaptée (histogramme, diagramme circulaire).",
 "La probabilité d'un événement est un nombre entre 0 et 1 ; dans une expérience à issues équiprobables, on la calcule par le rapport des cas favorables aux cas possibles."
], [
 q("Quel est le discriminant d'une équation ax² + bx + c = 0 ?", ["b² – 4ac", "b² + 4ac", "2ab", "a² + c²"], 0, "Le discriminant Δ = b² – 4ac détermine le nombre de solutions réelles de l'équation."),
 q("Si Δ < 0, combien l'équation a-t-elle de solutions réelles ?", ["Deux", "Une", "Aucune", "Une infinité"], 2, "Un discriminant négatif signifie que l'équation n'admet aucune solution réelle."),
 q("Quelle est la représentation graphique d'une fonction affine ?", ["Une parabole", "Une droite", "Un cercle", "Une exponentielle"], 1, "Une fonction f(x) = ax + b a pour représentation une droite de coefficient directeur a."),
 q("Que vaut (a+b)(a–b) ?", ["a² + b²", "a² – b²", "a² + 2ab + b²", "2ab"], 1, "C'est la troisième identité remarquable : la différence de carrés."),
 q("Dans quel BO le nouveau programme de maths de seconde est-il publié ?", ["BO n° 1 du 22 janvier 2019", "BO n° 14 du 2 avril 2026", "BO n° 8 du 25 juillet 2019", "BO n° 4 du 22 janvier 2026"], 1, "Le BO n° 14 du 2 avril 2026 publie les programmes de mathématiques du lycée, dont celui de seconde."),
 t("Comment choisir la méthode de résolution d'une équation du second degré ?", "Selon la forme de l'équation : factorisation directe, complétion du carré ou formule du discriminant.", "La factorisation est rapide quand les racines sont évidentes ; sinon, le discriminant donne une méthode systématique."),
 t("Quelle est la différence entre une fonction affine et une fonction linéaire ?", "Une fonction linéaire est un cas particulier de fonction affine, avec b = 0.", "La fonction linéaire f(x) = ax passe par l'origine ; la fonction affine f(x) = ax + b admet une ordonnée à l'origine b."),
 t("Comment interpréter l'écart-type d'une série statistique ?", "Il mesure la dispersion des valeurs autour de la moyenne.", "Un écart-type faible indique des valeurs concentrées autour de la moyenne ; un écart-type élevé indique une forte dispersion.")
])),

F.append(f(["1re"], "Maths", "Chapitre : Mathématiques intégrées à l'enseignement scientifique (programme 2026)", SM1, [
 "Le BO n° 14 du 2 avril 2026 publie le programme de mathématiques intégré à l'enseignement scientifique de première générale.",
 "Ce module vise à outiller tous les élèves de première, y compris ceux qui ne choisissent pas la spécialité mathématiques, pour les raisonnements scientifiques.",
 "La statistique descriptive et les probabilités y occupent une place importante : moyenne, variance, échantillonnage et intervalles de confiance.",
 "Le raisonnement proportionnel et la modélisation linéaire permettent de traduire des situations concrètes en relations mathématiques.",
 "La fonction exponentielle intervient dans les modèles de croissance et de décroissance : population, radioactivité, intérêts composés.",
 "La géométrie et la trigonométrie servent à résoudre des problèmes de mesure et de modélisation de l'espace.",
 "L'algorithmique et la programmation (souvent en Python) permettent de simuler des phénomènes et de traiter des données.",
 "La démarche de modélisation comporte plusieurs étapes : analyser la situation, choisir des variables, formuler des hypothèses, calculer et interpréter.",
 "Les outils numériques (tableur, calculatrice, Python) sont utilisés pour explorer, mais les résultats doivent être justifiés mathématiquement.",
 "L'épreuve de mathématiques est anticipée en première : ce programme intégré prépare aussi aux épreuves scientifiques et au grand oral."
], [
 q("Dans quel BO le programme de maths intégré de première est-il publié ?", ["BO n° 14 du 2 avril 2026", "BO n° 22 du 29 mai 2026", "BO spécial n° 8 du 25 juillet 2019", "BO n° 11 du 26 novembre 2015"], 0, "Le programme de mathématiques intégré à l'enseignement scientifique de première figure au BO n° 14 du 2 avril 2026."),
 q("Quel modèle utilise la fonction exponentielle ?", ["La croissance linéaire", "La croissance ou décroissance exponentielle", "La proportionnalité inverse", "La variation constante"], 1, "La fonction exponentielle modélise des phénomènes dont le taux de variation est proportionnel à la valeur présente."),
 q("Quel outil sert à mesurer la dispersion d'une série ?", ["La moyenne", "L'écart-type", "La médiane", "Le maximum"], 1, "L'écart-type quantifie la dispersion des valeurs autour de la moyenne."),
 q("Quelle est une étape de la démarche de modélisation ?", ["Choisir des variables et formuler des hypothèses", "Ignorer les données", "Refuser le calcul", "Supprimer les graphiques"], 0, "Modéliser suppose de simplifier la réalité en choisissant des variables et des hypothèses explicites."),
 q("Quel langage est couramment utilisé en algorithmique au lycée ?", ["Python", "HTML", "CSS", "SQL"], 0, "Python est le langage de référence des programmes de NSI et de l'algorithmique au lycée."),
 t("Comment un intervalle de confiance aide-t-il à interpréter un sondage ?", "Il donne une plage de valeurs plausibles pour la proportion réelle de la population.", "Sa largeur dépend de la taille de l'échantillon et du niveau de confiance choisi : il ne corrige pas les biais de recueil."),
 t("Pourquoi faut-il distinguer corrélation et causalité ?", "Parce que deux variables peuvent varier ensemble sans que l'une cause l'autre.", "Une corrélation peut être due à une variable commune ou au hasard : seule une démarche expérimentale permet d'établir une causalité."),
 t("Quel est l'intérêt d'un tableur en statistique ?", "Il permet de calculer rapidement des indicateurs et de construire des graphiques.", "Le tableur facilite l'exploration des données, mais l'élève doit savoir choisir les formules et interpréter les résultats.")
])),

F.append(f(["Terminale"], "Maths", "Chapitre : Mathématiques complémentaires – fonctions et probabilités", SMT, [
 "L'option de mathématiques complémentaires de terminale générale est destinée aux élèves n'ayant pas choisi la spécialité mathématiques ; son programme est publié au BO n° 14 du 2 avril 2026.",
 "Elle vise à consolider les outils mathématiques utiles aux études supérieures et à l'exercice de la citoyenneté.",
 "L'étude des fonctions porte sur la fonction exponentielle, la fonction logarithmique népérienne et leurs propriétés (croissance, limites, asymptotes).",
 "La résolution d'équations et d'inéquations exponentielles ou logarithmiques s'appuie sur les relations ln(e^x) = x et e^(ln x) = x (x > 0).",
 "La dérivation permet d'étudier les variations et les extrema de ces fonctions et de résoudre des problèmes d'optimisation simples.",
 "En probabilités, on travaille avec des variables aléatoires discrètes, leur espérance et leur écart-type.",
 "La loi binomiale B(n ; p) modélise le nombre de succès lors de n épreuves indépendantes de même probabilité p.",
 "Les intervalles de fluctuation et les tests statistiques simples permettent de décider si un échantillon est compatible avec une hypothèse.",
 "Les suites numériques (arithmétiques, géométriques) et leur somme sont également au programme, avec des applications financières.",
 "L'évaluation se fait en contrôle continu, avec une épreuve anticipée ; la maîtrise des outils et la clarté de la démarche sont valorisées."
], [
 q("Quelle relation est vraie pour x > 0 ?", ["ln(e^x) = x", "e^(ln x) = x²", "ln(x²) = x", "e^x = ln x"], 0, "La fonction ln est la réciproque de l'exponentielle : ln(e^x) = x pour tout x réel et e^(ln x) = x pour x > 0."),
 q("Quelle est la dérivée de e^x ?", ["x·e^(x–1)", "e^x", "1/x", "ln x"], 1, "L'exponentielle népérienne est égale à sa propre dérivée."),
 q("Que modélise une loi binomiale B(n ; p) ?", ["Le nombre de succès en n épreuves indépendantes", "Une durée d'attente", "Une mesure continue", "Un graphique"], 0, "La loi binomiale compte les succès dans n essais indépendants de probabilité p."),
 q("Qui est concerné par l'option maths complémentaires ?", ["Les élèves ayant choisi la spé maths", "Les élèves n'ayant pas choisi la spé maths", "Les élèves de 2nde uniquement", "Les étudiants de L1"], 1, "L'option s'adresse aux élèves de terminale générale qui n'ont pas retenu la spécialité mathématiques."),
 q("Quelle est l'espérance d'une loi binomiale B(n ; p) ?", ["n·p", "n·p·(1–p)", "p/n", "n²"], 0, "L'espérance d'une binomiale vaut n p ; sa variance vaut n p (1 – p)."),
 t("Comment résoudre une équation e^(2x) = 5 ?", "En prenant le logarithme népérien des deux membres : 2x = ln 5, donc x = (ln 5)/2.", "Le logarithme est l'inverse de l'exponentielle : il permet de « descendre » l'exposant."),
 t("Quel est l'intérêt d'un intervalle de fluctuation à 95 % ?", "Il définit la plage des résultats considérés comme compatibles avec une hypothèse.", "Si la proportion observée tombe hors de cet intervalle, l'hypothèse est remise en cause : c'est le principe d'un test statistique simple."),
 t("Comment calculer la somme des termes d'une suite géométrique ?", "Par la formule q^n–1 etc., selon le premier terme et la raison.", "Pour u_n = u_0·q^n, la somme des termes de u_0 à u_(n–1) vaut u_0·(1 – q^n)/(1 – q) si q ≠ 1.")
])),

F.append(f(["2nde", "1re", "Terminale"], "EMC", "Chapitre : La laïcité et les valeurs de la République", SEMC, [
 "L'éducation morale et civique vise à former des citoyens responsables, attachés aux valeurs et aux institutions de la République.",
 "La laïcité est un principe constitutionnel : l'article 1er de la Constitution du 4 octobre 1958 proclame que la France est une République « laïque ».",
 "La loi du 9 décembre 1905 sur la séparation des Églises et de l'État garantit la liberté de conscience et le libre exercice des cultes, tout en refusant toute reconnaissance officielle d'une religion.",
 "La laïcité repose sur plusieurs principes : liberté de conscience, égalité de tous devant la loi, neutralité de l'État et respect du pluralisme.",
 "À l'école, les enseignants et agents publics sont tenus à la neutralité ; les élèves ne le sont pas, mais doivent respecter le cadre de la laïcité et la sérénité des apprentissages.",
 "La Charte de la laïcité à l'école (2013) explicite ces règles et rappelle que l'école transmet les valeurs de la République : liberté, égalité, fraternité.",
 "D'autres valeurs fondent le vivre-ensemble : la dignité humaine, le respect d'autrui, l'égalité entre les femmes et les hommes et la lutte contre les discriminations.",
 "Le socle commun de connaissances, de compétences et de culture (BO n° 11 du 26 novembre 2015) définit les compétences civiques attendues à la fin de la scolarité obligatoire.",
 "L'EMC aborde aussi les grands principes juridiques : droits de l'homme, État de droit, séparation des pouvoirs et souveraineté nationale.",
 "L'objectif est de développer l'esprit critique, le respect des règles et la capacité de débattre dans le cadre d'une démocratie."
], [
 q("Dans quel article de la Constitution la laïcité est-elle proclamée ?", ["L'article 1er", "L'article 2", "L'article 16", "L'article 34"], 0, "L'article 1er de la Constitution du 4 octobre 1958 définit la France comme une République laïque."),
 q("Quelle loi consacre la séparation des Églises et de l'État en 1905 ?", ["La loi du 9 décembre 1905", "La loi du 28 mars 1882", "La loi du 16 juillet 2019", "La loi du 4 octobre 1958"], 0, "La loi du 9 décembre 1905 est la loi cadre de la laïcité française."),
 q("Qui est tenu à la neutralité dans l'école publique ?", ["Les élèves uniquement", "Les agents publics, dont les enseignants", "Les parents", "Tout le monde sans exception"], 1, "Les agents publics sont tenus à la neutralité ; les élèves bénéficient de la liberté de conscience, dans le respect des règles de vie scolaire."),
 q("Quelles sont les trois valeurs de la devise républicaine ?", ["Liberté, égalité, fraternité", "Paix, travail, patrie", "Force, courage, honneur", "Unité, dignité, solennité"], 0, "La devise de la République française est « Liberté, Égalité, Fraternité »."),
 q("Que garantit la liberté de conscience ?", ["Le droit d'avoir ou de ne pas avoir de religion", "L'obligation de croire", "L'interdiction des cultes", "La religion d'État"], 0, "La liberté de conscience inclut la liberté de croire, de ne pas croire et de changer de religion."),
 t("Comment articuler laïcité et respect des croyances ?", "En garantissant à chacun sa liberté de conscience sans donner à une religion de statut officiel.", "La laïcité n'est pas l'effacement des religions de l'espace public, mais un cadre d'égalité qui permet leur coexistence et le débat."),
 t("Quel est le rôle de l'EMC dans la formation du citoyen ?", "Transmettre les valeurs républicaines et développer l'esprit critique et la participation.", "L'EMC aide à comprendre les institutions, à respecter la loi et à exercer une citoyenneté active et éclairée."),
 t("Pourquoi la laïcité est-elle parfois présentée comme une protection ?", "Parce qu'elle empêche qu'une religion domestique l'État ou discrimine les citoyens.", "En séparant les Églises et l'État, la laïcité protège aussi bien les croyants des persécutions que les non-croyants d'une imposition.")
])),

F.append(f(["2nde", "1re", "Terminale"], "LV1 (anglais)", "Chapitre : Expression et compréhension en langue vivante – le citoyen et le monde", SLV, [
 "Le programme de langues vivantes du lycée, actualisé par le BO n° 22 du 29 mai 2026, vise une maîtrise progressive de la langue et une ouverture interculturelle.",
 "L'élève doit atteindre le niveau B1 en fin de seconde et le niveau B2 en fin de terminale pour la LV1, selon le Cadre européen commun de référence.",
 "Les compétences travaillées sont la compréhension de l'oral et de l'écrit, l'expression orale (interaction et production) et l'expression écrite.",
 "L'étude de documents (textes littéraires, articles de presse, discours, images, vidéos) est au cœur de la démarche : on identifie le point de vue, le registre et l'intention de l'auteur.",
 "Des notions Culturelles et linguistiques sont travaillées : « identities and exchanges », « innovations and responsibilities », « territories and memories » structurent les programmes de cycle.",
 "La grammaire et le lexique sont enseignés en contexte : modaux, temps du passé, voix passive, comparatifs, propositions relatives et connecteurs logiques.",
 "La phonologie (prononciation, intonation, rythme) fait l'objet d'un entraînement régulier, notamment en vue de l'épreuve orale.",
 "Le programme encourage l'autonomie : utilisation du dictionnaire, stratégies de compréhension (inférence, repérage des mots-clés) et réinvestissement des connaissances.",
 "L'interculturel suppose de comparer les réalités culturelles sans stéréotype, en mobilisant des exemples précis de la civilisation étudiée.",
 "L'évaluation prend la forme d'épreuves de compréhension, d'expression écrite (essai, compte rendu) et d'expression orale (présentation, débat)."
], [
 q("Quel niveau du CECRL vise la LV1 en fin de terminale ?", ["A2", "B1", "B2", "C1"], 2, "La LV1 doit atteindre le niveau B2 en fin de terminale ; la LV2 vise le niveau B1."),
 q("Dans quel BO le programme de langues vivantes de 2026 est-il publié ?", ["BO n° 22 du 29 mai 2026", "BO n° 14 du 2 avril 2026", "BO spécial n° 1 du 22 janvier 2019", "BO n° 4 du 22 janvier 2026"], 0, "Le BO n° 22 du 29 mai 2026 actualise les programmes de langues vivantes du lycée."),
 q("Quel outil aide à inférer le sens d'un mot inconnu ?", ["Le contexte et les mots-clés", "La traduction mot à mot", "Le hasard", "Le dictionnaire uniquement"], 0, "L'inférence à partir du contexte est une stratégie de compréhension essentielle, avant le recours au dictionnaire."),
 q("Quel est un connecteur logique de cause en anglais ?", ["However", "Therefore", "Although", "Meanwhile"], 1, "« Therefore » marque la conséquence ; « however » marque l'opposition et « although » la concession."),
 q("Quelle compétence est travaillée lors d'un débat en classe ?", ["L'interaction orale", "La traduction", "La dictée", "La copie"], 0, "Le débat développe l'expression orale en interaction, compétence centrale du CECRL."),
 t("Comment analyser le point de vue d'un document ?", "En identifiant l'auteur, son intention, les mots évaluatifs et les arguments avancés.", "Le point de vue se construit par des choix lexicaux et syntaxiques : repérer les modalisateurs et les connecteurs permet de le caractériser."),
 t("Qu'est-ce qu'une démarche interculturelle ?", "Elle consiste à comparer des cultures sans jugement ethnocentrique, en s'appuyant sur des faits.", "L'interculturel vise à comprendre l'altérité et à relativiser ses propres représentations, compétence clé du programme 2026."),
 t("Comment préparer une expression orale en anglais ?", "En structurant son propos (introduction, arguments, conclusion) et en révisant le vocabulaire et la prononciation.", "Une bonne prestation combine contenu, organisation et intelligibilité : la clarté de l'intonation compte autant que la richesse du vocabulaire.")
])),

F.append(f(["2nde", "1re", "Terminale"], "LV2", "Chapitre : LV2 – compréhension et expression dans une deuxième langue", SLV, [
 "La LV2 est enseignée à partir de la seconde ; son volume horaire est inférieur à celui de la LV1, avec un objectif de niveau B1 en fin de terminale.",
 "Le programme de LV2 s'appuie sur le même Cadre européen commun de référence et sur les mêmes principes d'approche par compétences.",
 "Les documents étudiés sont adaptés au niveau : textes courts, dialogues, messages, affiches et extraits de presse simple.",
 "Le lexique et la grammaire sont progressifs : présent, passé composé, futur proche, pronoms, prépositions et connecteurs courants.",
 "La compréhension de l'oral et de l'écrit est privilégiée, avec des tâches d'identification d'informations explicites et d'inférences simples.",
 "L'expression écrite porte sur des messages, des descriptions et des courts textes argumentatifs avec des modèles guidés.",
 "L'expression orale vise l'interaction simple : se présenter, poser des questions, exprimer une préférence et justifier brièvement.",
 "Le programme de 2026 renforce l'accompagnement personnalisé pour les élèves en difficulté et la continuité avec le collège.",
 "L'évaluation en LV2 tient compte du niveau de départ ( débutant ou poursuite) et mesure les progrès réalisés.",
 "Le grand oral peut être passé en langue vivante : l'élève y présente un sujet en LV1 ou en LV2, avec l'accord de son enseignant."
], [
 q("Quel niveau vise la LV2 en fin de terminale ?", ["A1", "A2", "B1", "C1"], 2, "La LV2 vise le niveau B1 en fin de terminale, contre B2 pour la LV1."),
 q("À partir de quelle classe la LV2 est-elle enseignée au lycée ?", ["La 2nde", "La 1re", "La Terminale", "Le collège uniquement"], 0, "La LV2 est généralement introduite en classe de seconde au lycée."),
 q("Quel type de document est adapté au niveau LV2 ?", ["Un roman complexe", "Un dialogue simple", "Un traité philosophique", "Un article scientifique"], 1, "Les dialogues et textes courts constituent des supports adaptés au niveau A2/B1."),
 q("Quelle compétence est privilégiée en LV2 ?", ["La compréhension et l'expression guidée", "La traduction littéraire", "L'écriture de thèses", "Le débat expert"], 0, "Le programme privilégie la compréhension et une expression progressivement autonome."),
 q("Quel temps du passé est couramment travaillé en LV2 en français ?", ["Le passé simple", "Le passé composé", "Le plus-que-parfait", "Le futur antérieur"], 1, "Le passé composé est le temps du passé de base, travaillé dès le collège et consolidé au lycée."),
 t("Comment améliorer sa compréhension de l'oral en LV2 ?", "En s'entraînant régulièrement avec des documents audio et en identifiant les mots-clés.", "La répétition, le repérage des marqueurs de discours et l'habituation à différents accents facilitent la compréhension orale."),
 t("Quelle est la différence entre LV1 et LV2 ?", "La LV1 a un volume horaire plus important et un objectif de niveau plus élevé (B2 contre B1).", "La LV2 s'appuie sur une progression plus lente et des supports adaptés, tout en suivant les mêmes grands principes."),
 t("Comment réussir un court exposé oral en LV2 ?", "En préparant des phrases simples et en s'entraînant à les prononcer clairement.", "La répétition et l'enregistrement de soi permettent de gagner en fluidité et en confiance.")
])),

F.append(f(["Terminale"], "EPS", "Chapitre : L'EPS au baccalauréat – modalités et enjeux", SEPS, [
 "Au baccalauréat, l'EPS est une épreuve obligatoire du contrôle continu : elle compte pour 10 % de la note finale en voie générale et technologique.",
 "Depuis la réforme du bac appliquée depuis 2020, l'évaluation prend appui sur trois composantes : les résultats scolaires des trois années, l'attestation d'aptitude physique et pratique (AAP) et, le cas échéant, un examen supplémentaire.",
 "Les bulletins de 2nde, 1re et Terminale fournissent l'essentiel de la note : la régularité et la progression sont donc déterminantes.",
 "L'AAP valide la capacité de l'élève à pratiquer une activité physique en sécurité ; elle est délivrée par le médecin scolaire.",
 "Un examen supplémentaire est prévu pour les élèvesdispensés ou pour ceux dont les résultats ne peuvent être pris en compte, selon la circulaire d'examen annuelle.",
 "Les critères d'évaluation portent sur la réalisation d'une prestation motrice, la maîtrise des règles et des stratégies, et la participation active et autonome.",
 "Les activités de compétition (sports collectifs, sports de raquette) et de coopération (gymnastique, escalade, danse) sont toutes évaluables.",
 "La notation prend en compte le progrès individuel plutôt que la seule comparaison entre élèves, conformément aux principes du livret scolaire.",
 "L'EPS contribue aussi au grand oral : l'élève peut choisir une question liée au sport, à la santé ou aux sciences du mouvement.",
 "Les enjeux de l'épreuve sont la promotion d'une pratique autonome, la connaissance des effets de l'activité physique sur la santé et l'adoption d'un comportement responsable."
], [
 q("Quel est le poids de l'EPS dans la note finale du bac général ?", ["5 %", "10 %", "20 %", "40 %"], 1, "L'EPS compte pour 10 % de la note finale du baccalauréat général et technologique, au titre du contrôle continu."),
 q("Que signifie AAP ?", ["Attestation d'aptitude physique et pratique", "Avis d'aptitude professionnelle", "Allocation d'aide pédagogique", "Assurance accidents personnelle"], 0, "L'AAP valide la capacité de l'élève à pratiquer une activité physique en toute sécurité."),
 q("Combien d'années de bulletins sont prises en compte ?", ["Une", "Deux", "Trois", "Quatre"], 2, "Les résultats de 2nde, 1re et Terminale sont pris en compte dans la note d'EPS."),
 q("Quel critère n'est pas utilisé en évaluation de l'EPS ?", ["La prestation motrice", "La maîtrise des règles", "La participation active", "La taille de l'élève"], 3, "L'évaluation porte sur des compétences observées, pas des caractéristiques physiques."),
 q("Quand l'EPS est-elle devenue une épreuve de contrôle continu ?", ["Avec la réforme du bac de 2020", "En 2015", "En 2019", "En 2000"], 0, "La réforme du baccalauréat, appliquée depuis 2020, a intégré l'EPS au contrôle continu à hauteur de 10 %."),
 t("Comment se construit la note d'EPS au bac ?", "À partir des bulletins des trois années, de l'AAP et, si nécessaire, d'un examen supplémentaire.", "Le contrôle continu valorise la progression et la régularité ; l'AAP et l'examen supplémentaire couvrent les cas particuliers."),
 t("Pourquoi valoriser le progrès individuel ?", "Parce que les niveaux de départ sont très différents d'un élève à l'autre.", "L'évaluation mesure ce que l'élève a appris et sa capacité à s'engager, plutôt qu'une performance absolue."),
 t("Quel lien existe-t-il entre EPS et grand oral ?", "Un élève peut choisir une question de grand oral en rapport avec le sport ou la santé.", "Le grand oral permet de faire dialoguer les savoirs disciplinaires avec une question citoyenne ou scientifique, y compris en lien avec l'activité physique.")
])),

F.append(f(["2nde", "1re", "Terminale"], "Enseignement scientifique", "Chapitre : Le ciel, la Terre et l'environnement : observations et modèles", SES, [
 "L'enseignement scientifique est obligatoire en voie générale ; il propose une culture scientifique commune aux élèves, quel que soit leur choix de spécialité.",
 "Le programme de seconde aborde le ciel et la Terre : le système solaire, les mouvements apparents des astres et les phases de la Lune.",
 "La Terre est une planète du système solaire : sa rotation produit le jour et la nuit, sa révolution autour du Soleil et l'inclinaison de son axe produisent les saisons.",
 "Les modèles géocentrique et héliocentrique se sont succédé : Copernic (1543), Galilée et Kepler ont imposé le modèle héliocentrique.",
 "En première, l'enseignement scientifique traite de la Terre dans l'Univers, de la chimie de la matière et de l'énergie et du climat.",
 "En terminale, les programmes portent sur les grandes theories scientifiques et les enjeux contemporains, dont le changement climatique.",
 "La démarche scientifique repose sur l'observation, la formulation d'hypothèses, l'expérimentation, la modélisation et la confrontation aux données.",
 "La chimie explique les transformations de la matière : réactions, acides et bases, oxydoréduction, sans négliger les applications environnementales.",
 "Le climat est étudié à partir de données (températures, CO₂, forçage radiatif) et de modèles qui permettent de distinguer variabilité naturelle et influence humaine.",
 "L'objectif est de former des citoyens capables de lire des informations scientifiques, de comprendre les enjeux et de participer aux débats."
], [
 q("Quel mouvement de la Terre produit le jour et la nuit ?", ["La révolution", "La rotation", "La précession", "La nutation"], 1, "La rotation de la Terre sur elle-même en 24 heures produit l'alternance jour/nuit."),
 q("Qui a publié un modèle héliocentrique en 1543 ?", ["Ptolémée", "Copernic", "Newton", "Aristote"], 1, "Copernic publie De revolutionibus orbium coelestium en 1543."),
 q("Quel gaz est principalement responsable de l'augmentation anthropique de l'effet de serre ?", ["Le méthane", "Le dioxyde de carbone", "L'azote", "L'ozone"], 1, "Le CO₂ issu des combustibles fossiles est le principal contributeur au forçage radiatif humain."),
 q("Quelle est une étape de la démarche scientifique ?", ["Formuler une hypothèse puis la tester", "Ignorer les données", "Refuser le débat", "Imposer une conclusion"], 0, "La démarche scientifique est itérative : observation, hypothèse, expérience, modèle et confrontation aux faits."),
 q("Comment appelle-t-on un modèle qui décrit les interactions chimiques ?", ["Une équation bilan", "Une carte", "Une courbe de température", "Un graphique"], 0, "L'équation bilan, équilibrée, représente les réactifs et les produits d'une transformation chimique."),
 t("Comment les saisons s'expliquent-elles ?", "Par la révolution terrestre combinée à l'inclinaison de l'axe de rotation.", "L'inclinaison de 23,4° modifie l'angle d'incidence des rayons solaires et la durée du jour selon la position de la Terre sur son orbite."),
 t("Quelle est la différence entre météorologie et climat ?", "La météorologie décrit l'état à court terme ; le climat étudie les tendances sur de longues périodes.", "Le climat est une statistique des conditions météorologiques sur 30 ans ou plus : cette distinction est essentielle pour interpréter les données."),
 t("Comment un modèle scientifique peut-il être remis en cause ?", "Lorsque de nouvelles observations ne correspondent plus à ses prédictions.", "Un modèle est une représentation provisoire : sa validité dépend de sa capacité à expliquer et prévoir les observations.")
])),

AN.append(a("Sujet type bac – Histoire, thème 1 : la France de la Révolution à la Première Guerre mondiale", "Histoire",
 "Sujet de type 1 (composition, 4 points). « La Révolution française a-t-elle transformé la France en profondeur ? »\n"
 "Document 1 : Déclaration des droits de l'homme et du citoyen, 26 août 1789 (article 1er : « Les hommes naissent et demeurent libres et égaux en droits. »).\n"
 "Document 2 : Code civil, article 8 (1804) : « Tout Français jouira des droits civils. »\n"
 "Consigne : rédiger une réponse structurée (introduction, deux ou trois parties, conclusion) en mobilisant les acquis du cours et les documents.",
 "Corrigé indicatif. Introduction : la Révolution de 1789 marque la fin de l'Ancien Régime et l'avènement d'un ordre juridique nouveau ; on mesurera la portée réelle de la rupture.\n"
 "I. Une transformation juridique et politique majeure : abolition des privilèges (4 août 1789), DDHC (26 août 1789), souveraineté nationale, égalité devant la loi et l'impôt, Constitution de 1791, puis République en 1792. Le Code civil de 1804 consacre juridiquement l'égalité (doc. 2).\n"
 "II. Des transformations sociales inachevées : les paysans achètent des terres, la bourgeoisie s'élargit, mais les ouvriers urbains restent sans droits politiques ; la laïcité de 1905 achève longuement la séparation. Les femmes restent privées du vote jusqu'en 1944 ; l'esclavage est aboli en 1794, rétabli en 1802, définitivement aboli en 1848.\n"
 "III. Une transformation ambivalente : la Terreur et la guerre montrent que la rupture s'accompagne de violences et d'un pouvoir autoritaire (1799-1815). La IIIe République (1870-1940) rétablit durablement les principes de 1789.\n"
 "Conclusion : la Révolution a transformé en profondeur le droit et la citoyenneté, mais l'égalité réelle s'est construite sur un siècle de luttes et de compromis."))

AN.append(a("Sujet type bac – Géographie, thème : la France dans la mondialisation", "Géographie",
 "Sujet de type 2 (analyse de documents, 6 points). « Montrez que la France est intégrée à la mondialisation tout en conservant des territoires contrastés. »\n"
 "Document 1 : carte des principales aires métropolitaines françaises et des flux aériens au départ de Paris-CDG (2024).\n"
 "Document 2 : tableau comparant le PIB par habitant en Île-de-France et dans les régions rurales (INSEE, 2024).\n"
 "Consigne : décrire les documents, dégager les contrastes et proposer une interprétation géographique.",
 "Corrigé indicatif. I. Description : Paris-CDG est l'un des premiers aéroports européens ; les métropoles se concentrent le long des grands axes (Rhône, Atlantique, Nord). Le tableau fait apparaître un écart fort de PIB par habitant entre l'Île-de-France et les territoires ruraux.\n"
 "II. Interprétation : la France est intégrée aux flux mondiaux par ses métropoles, ses entreprises exportatrices et son agriculture (premier exportateur agroalimentaire européen). La métropolisation concentre les fonctions de commandement et creuse les inégalités avec les espaces périphériques.\n"
 "III. Nuance : l'aménagement du territoire (DATAR, 1963), les réseaux TGV et numériques et la PAC visent à corriger ces déséquilibres ; les espaces ruraux sont multifonctionnels (production, hébergement, environnement).\n"
 "Conclusion : l'intégration mondiale est un moteur de croissance mais produit des territoires différenciés, ce qui fait de la cohésion territoriale un enjeu central de l'action publique."))

AN.append(a("Sujet type bac – Français, épreuve anticipée : commentaire de poésie", "Français",
 "Sujet d'épreuve anticipée de français (écrit, 5 points). Commentaire littéraire du poème « Correspondances » de Charles Baudelaire (Les Fleurs du mal, 1857) :\n"
 "« La Nature est un temple où de vivants piliers / Laissent parfois sortir de confuses paroles ; / L'homme y passe à travers des forêts de symboles / Qui l'observent avec des regards familiers. »\n"
 "Consigne : proposer une lecture commentée du poème en mettant en relation les images et la théorie des correspondances, puis ouvrir sur la modernité poétique baudelairienne.",
 "Corrigé indicatif. Introduction : Baudelaire, condamné en 1857, publie Les Fleurs du mal ; le sonnet « Correspondances » est un manifeste de la poésie symboliste.\n"
 "I. Une nature peuplée de signes : la métaphore du « temple » et des « vivants piliers » transforme le paysage en édifice sacré ; les « forêts de symboles » font du monde un langage à déchiffrer. La personnification (« regards familiers ») crée une intimité inquiétante.\n"
 "II. Une théorie des sens : le poème énonce que les parfums, les couleurs et les sons se répondent (synesthésie). La sensation devient le point de départ d'une élévation spirituelle.\n"
 "III. Une modernité ambiguë : la correspondance promet une unité perdue mais reste « confuse » ; le poète est un traducteur qui peine à transcrire le message du monde. Cette tension définit le spleen baudelairien.\n"
 "Conclusion : le poème fait de la poésie une quête de sens à travers les sens, ouvrant la voie à Mallarmé et aux symbolistes."))

AN.append(a("Sujet type bac – Philosophie : la liberté est-elle une illusion ?", "Philosophie",
 "Sujet de composition n° 1 (4 points). « La liberté est-elle une illusion ? »\n"
 "Consignes : définir les termes, construire un plan argumenté, mobiliser au moins trois auteurs du programme et répondre directement à la question.",
 "Corrigé indicatif. Introduction : nous nous vivons comme libres lorsque nous délibérons, mais la science et les sciences humaines semblent nier cette liberté. On distinguera l'illusion subjective de la liberté et l'exigence rationnelle qu'elle représente (Kant, Sartre).\n"
 "I. L'objection déterministe : Laplace (Essai philosophique sur les probabilités, 1814) imagine une intelligence qui prédirait l'avenir ; Diderot joue de cette idée dans Jacques le fataliste. La biologie, la psychologie et la sociologie montrent l'emprise des pulsions, des habitudes et des normes.\n"
 "II. La liberté comme expérience irréductible : Kant distingue phénomènes et noumènes : la liberté est une idée de la raison pratique sans laquelle la morale n'aurait pas de sens. Sartre en fait le point de départ de l'existentialisme : l'homme se définit par ses choix.\n"
 "III. Dépassement : la liberté n'est pas l'absence de déterminismes mais la capacité de prendre conscience d'eux et d'agir en fonction de fins choisies (Rousseau : obéir à la loi qu'on s'est donnée). Elle est donc moins une illusion qu'un idéal qui oriente l'action et le droit.\n"
 "Conclusion : si la liberté est illusoire comme absence de causes, elle est réelle comme exigence de responsabilité et d'émancipation."))

AN.append(a("Sujet type bac – Mathématiques complémentaires (Terminale) : fonctions et statistiques", "Maths",
 "Sujet type – Terminale, option maths complémentaires (4 points).\n"
 "Exercice 1. Soit la fonction f définie sur ℝ par f(x) = 3·e^(0,2x) – 2.\n"
 "1° Étudier les variations de f et déterminer ses limites en –∞ et +∞.\n"
 "2° Résoudre f(x) = 4 (on donnera la valeur arrondie au centième).\n"
 "Exercice 2. Une enquête porte sur 200 élèves ; 60 % pratiquent un sport. On prélève un échantillon de 10 élèves au hasard avec remise. X désigne le nombre d'élèves pratiquant un sport.\n"
 "1° Quelle est la loi de X ? 2° Calculer P(X = 7). 3° Donner un intervalle de fluctuation asymptotique à 95 % de la proportion pour un échantillon de 200 élèves.",
 "Corrigé. Ex. 1 : 1° f'(x) = 0,6·e^(0,2x) > 0 sur ℝ, donc f est strictement croissante ; lim_(x→–∞) f = –2 et lim_(x→+∞) f = +∞. La droite y = –2 est asymptote horizontale en –∞.\n"
 "2° 3e^(0,2x) – 2 = 4 ⇔ e^(0,2x) = 2 ⇔ 0,2x = ln 2 ⇔ x = 5 ln 2 ≈ 3,47.\n"
 "Ex. 2 : 1° X suit une loi binomiale B(10 ; 0,6). 2° P(X = 7) = C(10,7)·0,6^7·0,4^3 = 120 × 0,0279936 × 0,064 ≈ 0,215.\n"
 "3° Intervalle : 0,6 ± 1,96·√(0,24/200) ≈ 0,6 ± 0,068, soit [0,532 ; 0,668]."))

AN.append(a("Sujet type bac – Enseignement scientifique (Terminale) : climat et données", "Enseignement scientifique",
 "Sujet type – épreuve d'enseignement scientifique (5 points).\n"
 "Document 1 : courbe des concentrations atmosphériques en CO₂ (Mauna Loa, 1958-2025) passant d'environ 315 ppm à plus de 425 ppm.\n"
 "Document 2 : schéma de l'effet de serre : rayonnement solaire entrant, réémission infrarouge par la surface, absorption par les gaz à effet de serre.\n"
 "Questions : 1° Décrire l'évolution du CO₂. 2° Expliquer le mécanisme de l'effet de serre naturel. 3° Pourquoi l'augmentation du CO₂ est-elle liée à l'activité humaine ? 4° Citez deux conséquences et deux leviers d'action.",
 "Corrigé indicatif. 1° La concentration augmente de façon continue avec une oscillation annuelle liée au cycle saisonnier de la végétation ; elle dépasse 425 ppm en 2025.\n"
 "2° Le Soleil émet un rayonnement dont une partie est absorbée par la surface, qui réémet un rayonnement infrarouge. Les gaz à effet de serre (H₂O, CO₂, CH₄) en absorbent une partie et la réémettent vers le sol, maintenant une température moyenne d'environ 15 °C.\n"
 "3° La combustion des énergies fossiles, la déforestation et l'agriculture émettent du CO₂ et du méthane plus vite que les puits naturels ne peuvent les absorber.\n"
 "4° Conséquences : hausse des températures, fonte des glaciers, montée des eaux, événements extrêmes, acidification des océans. Leviers : sobriété et efficacité énergétique, énergies bas carbone, restauration des puits de carbone, adaptation des territoires."))

AN.append(a("Sujet type bac – EMC : la laïcité et les valeurs de la République", "EMC",
 "Sujet type – épreuve orale ou écrit court (4 points). « La laïcité est-elle une contrainte ou une protection pour la liberté de chacun ? »\n"
 "Document 1 : loi du 9 décembre 1905, article 1er : « La République assure la liberté de conscience. »\n"
 "Document 2 : article 2 : « La République ne reconnaît, ne salarie ni ne subventionne aucun culte. »\n"
 "Consigne : analyser les documents, expliquer le principe de laïcité et discuter sa portée dans une école républicaine.",
 "Corrigé indicatif. Introduction : la laïcité est un principe constitutionnel issu de la loi de 1905 ; elle peut apparaître comme une contrainte (neutralité) mais elle est d'abord une protection.\n"
 "I. Un principe de liberté : la loi de 1905 garantit la liberté de conscience (doc. 1) et la libre organisation des cultes ; l'État ne privilégie aucune religion (doc. 2).\n"
 "II. Une contrainte assumée : les agents publics, dont les enseignants, sont tenus à la neutralité ; les élèves ne le sont pas, mais le cadre scolaire doit préserver la sérénité et l'égalité entre croyants et non-croyants.\n"
 "III. Une exigence d'égalité : la laïcité empêche que la religion devienne un critère d'accès aux droits ou un motif de discrimination ; elle permet le vivre-ensemble dans une société pluraliste.\n"
 "Conclusion : plus qu'une contrainte, la laïcité est la condition de la liberté de conscience et de l'égalité républicaine, à condition qu'elle s'accompagne de la connaissance des faits religieux et du dialogue."))

AN.append(a("Sujet type bac – LV1 anglais : expression écrite – réseau social et démocratie", "LV1 (anglais)",
 "Sujet type – expression écrite (5 points).\n"
 "Document : « Social media has transformed the way young people get information. Algorithms select what they see, and false news can spread faster than the truth. Yet these platforms also give a voice to minorities and allow citizens to mobilise. »\n"
 "Question : In 250-300 words, discuss the following statement: « Social media is more of a threat than an opportunity for democracy. » Give your opinion, support it with examples and propose solutions.",
 "Corrigé indicatif (plan attendu et amorce). Introduction : hook (the spread of social media among teenagers), define the issue (information, algorithms, democracy), announce the plan (threats / opportunities / solutions).\n"
 "I. Threats: algorithmic bubbles (filter bubbles), misinformation, outrage-driven engagement, foreign interference, cyberbullying.\n"
 "II. Opportunities: citizen journalism, mobilisation (Arab Springs, climate marches), voices for minorities, access to independent sources.\n"
 "III. Solutions: media literacy at school (a key skill of the 2026 LV programme), fact-checking, transparency of algorithms, regulation (Digital Services Act), personal responsibility.\n"
 "Conclusion: social media is neither good nor bad in itself; its impact depends on users' critical skills and on the rules that frame it. Useful links: however, moreover, on the one hand / on the other hand, therefore. Expected grammar: modals, concession (although, despite)."))

save("lead-general-partie-A.json", F, AN)
print("Partie A:", len(F), "fiches,", len(AN), "annales")
