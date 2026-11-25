# -*- coding: utf-8 -*-
"""Generateur sti2d-mat-part-A.json — lot A : tronc commun (20 fiches).

Fraises, maths, physique-chimie, anglais, HGGS et EMC pour la serie STI2D :
12 points de cours, 9 questions corrigees (7 QCM + 2 texte),
7 blocs en ordre strict, 3 schemas via diag().
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_etapes,
                      svg_compare, bloc, valider_et_ecrire)

FIL = ["sti2d"]
REF = (
    "Programmes de la voie technologique, serie STI2D : arrete du 17 janvier 2019 (NOR MENE1901591A, "
    "programme des enseignements de specialite des classes de premiere et terminale STI2D), arrete du "
    "17 janvier 2019 (NOR MENE1901630A, mathematiques de premiere technologique), programmes du tronc "
    "commun de seconde (francais MENE1901575A, mathématiques MENE1901631A, physique-chimie MENE1901634A, "
    "langues vivantes MENE1901585A, histoire-geographie MENE1901577A, EMC MENE1901572A), Bulletin officiel "
    "special n 1 du 22 janvier 2019. Ressources et epreuves : eduscol, « Programmes et ressources en serie "
    "STI2D » et « Baccalaureat technologique STI2D »."
)


def S(texte):
    return [x.strip() for x in texte.split("|") if x.strip()]


def R(texte):
    return [x.strip() for x in texte.split("~") if x.strip()]


def QC(question, options, correct, correction):
    return qcm(question, R(options), correct, correction)


def QT(question, reponse, correction):
    return qt(question, reponse, correction)


def _grid(texte):
    lignes = S(texte)
    if len(lignes) == 1:
        cellules = R(lignes[0])
        return [cellules[i:i + 3] for i in range(0, 9, 3)]
    return [R(x) for x in lignes]


def _cmp(texte):
    cellules = R(texte)
    n = len(cellules) // 2
    return (cellules[0], cellules[1:n]), (cellules[n], cellules[n + 1:])


def C(idea, eq, leg, grid, steps, traps, ex, cmp1, cmp2):
    return {"idea": idea, "eq": eq, "leg": leg, "grid": _grid(grid),
            "steps": S(steps), "traps": S(traps), "ex": [R(x) for x in S(ex)],
            "cmp": (_cmp(cmp1), _cmp(cmp2))}


def build(prefix, titre, matiere, annees, points, questions, c):
    """Assemble une fiche prototype complete a partir des donnees compactes."""
    titre_complet = prefix + " · " + titre
    short = titre.split(":")[0].strip()
    aff = [
        bloc("L'idee en une phrase", texte=c["idea"], type="intro"),
        bloc("La notion a maitriser", eq=c["eq"], leg=c["leg"], type="formule"),
        bloc("Tableau de lecture", items=c["grid"], type="grille"),
        bloc("Les points essentiels du chapitre", items=points[1:5], type="liste"),
        bloc("La demarche pas a pas", items=c["steps"], type="etapes"),
        bloc("Pieges et erreurs frequentes", items=c["traps"], type="attention"),
        bloc("En situation : exemples chiffres", items=[
            '%s : <span class="cle">%s</span>' % (p[0], p[1]) for p in c["ex"]
        ], type="exemples"),
    ]
    schema = [
        diag("1 · " + short, svg_grille(short, ["Notion", "Definition", "Repere"], c["grid"])),
        diag("2 · Demarche", svg_etapes("Procedure : " + short, c["steps"])),
        diag("3 · A distinguer", svg_compare(short, c["cmp"][0], c["cmp"][1])),
    ]
    assert len(points) == 12, "12 points attendus pour " + prefix
    assert len(questions) == 9, "9 questions attendues pour " + prefix
    assert sum(1 for q in questions if q.get("type") == "qcm") == 7, prefix
    assert sum(1 for q in questions if q.get("type") == "texte") == 2, prefix
    assert len(aff) == 7 and len(schema) == 3, prefix
    return fiche(FIL, annees, matiere, titre_complet, REF,
                 points, questions, aff, schema)


F = []


def add(prefix, titre, mat, ans, points, questions, c):
    F.append(build(prefix, titre, mat, ans, points, questions, c))


# ============================================================ FRA1
add("FRA1", "Figures de style et registres : produire un effet de sens", "Français", ["1re"],
S("Une figure de style est une manipulation de la langue qui produit un effet de sens au-dela du sens litteral."
  "|La comparaison relie deux elements avec un outil explicite : comme, tel, semblable, pareil."
  "|La métaphore transpose un terme dans un contexte inhabituel, sans outil de comparaison."
  "|La personnification attribue des actions ou des sentiments humains a un animal, un objet ou une abstraction."
  "|L'hyperbole amplifie la realite tandis que l'euphemisme l'attenue, souvent avec une intention ironique."
  "|La litote consistant a dire moins pour suggerer davantage : « je ne te hais point »."
  "|L'antithese oppose deux termes ou deux idees dans une meme phrase pour creer un contraste."
  "|L'oxymore associe deux mots contradictoires dans un meme groupement : « un silence assourdissant »."
  "|L'anaphore repete un mot en debut de phrase ou de vers ; l'epiphore le repete en fin."
  "|Le registre designe la visee d'ensemble du texte : comique, tragique, epique, lyrique, pathétique ou fantastique."
  "|Le registre comique vise le rire (comedie, satire, burlesque) ; le registre tragique met en scene une fatalite."
  "|L'analyse stylistique repere la figure, nomme l'effet produit et le relie a l'intention de l'auteur."),
[QC("Quel outil caracterise la comparaison ?", "Comme~Aucun~Mais~Donc", 0,
    "La comparaison utilise un outil explicite comme, tel ou semblable."),
 QC("« Un silence assourdissant » est une...", "Oxymore~Antithese~Euphemisme~Litote", 0,
    "Deux mots contradictoires forment un oxymore."),
 QC("La litote consiste a...", "Dire moins pour suggerer plus~Exagerer~Repeter~Opposer", 0,
    "La litote atténue l'expression pour laisser deviner une realite plus forte."),
 QC("Quel registre vise principalement le rire ?", "Tragique~Comique~Epique~Lyrique", 1,
    "Le registre comique a pour fonction de divertir et de faire rire."),
 QC("Personnifier consiste a...", "Donner des traits humains a un objet~Comparer avec comme~Attenuer~Repeter", 0,
    "La personnification attribue des caracteres humains a un non-humain."),
 QC("Quelle figure oppose deux idees dans une meme phrase ?", "L'anaphore~L'antithese~La litote~La metaphore", 1,
    "L'antithese joue sur l'opposition de deux termes ou de deux propositions."),
 QC("Apres avoir repere une figure, que faut-il faire ?", "La nommer seulement~Expliquer son effet et le lien avec l'intention~La traduire~L'ignorer", 1,
    "L'analyse complete nomme la figure, explique son effet et le relie au projet de l'auteur."),
 QT("Expliquer la difference entre comparaison et metaphore, en donnant un exemple de chaque.",
    "La comparaison explicite le rapprochement avec un outil : « il est fort comme un lion » ; elle maintient deux termes distincts. La métaphore supprime l'outil et transfere directement un terme : « il est un lion » ; le lecteur doit reconstruire le rapprochement. La comparaison est plus explicite, la métaphore plus dense et plus imagee. Les deux produisent un effet de mise en valeur du comparé, mais la métaphore implique une lecture plus active.",
    "On attend l'opposition outil explicite / transposition implicite, avec deux exemples clairs."),
 QT("Analyser la phrase : « Ce silence assourdissant pesait sur la salle comme un verdict. »",
    "On repere d'abord l'oxymore « silence assourdissant » : l'opposition entre l'absence de bruit et l'intensité exprime une tension insupportable. « Pesait sur la salle » est une personnification du silence, qui devient une force materielle et oppressante. Enfin, « comme un verdict » est une comparaison qui associe le silence a une decision definitive et severe. Le registre est tragique ou pathétique : l'accumulation des figures donne au lecteur le sentiment d'une fatalite et d'une attente angoissante.",
    "On valorise le repérage des trois figures, la nomination du registre et l'explication des effets.")],
C("Une figure de style transforme la langue pour produire un effet ; le registre est la visee generale du texte.",
  "Comparaison = compare + outil + comparant · metaphore = transfert sans outil",
  "Figures : comparaison, metaphore, personnification, antithese, oxymore · registres : comique, tragique, lyrique",
  "Comparaison~Outil explicite~comme, tel~Metaphore~Transposition~sans outil~Oxymore~Mots opposes~silence assourdissant",
  "Repérer une expression inhabituelle|Nommer precisement la figure|Citer les mots du texte|Expliquer l'effet produit|Relier a l'intention de l'auteur",
  "Confondre antithese et oxymore|Oublier de citer le texte|Nommer la figure sans expliquer l'effet|Parler de registre pour une seule phrase",
  "Comparaison~fort comme un lion~Metaphore~il est un lion~Litote~je ne te hais point~Oxymore~silence assourdissant",
  "Comparaison~Outil explicite~Deux termes distincts~Metaphore~Aucun outil~Transposition directe",
  "Antithese~Opposition d'idees~Meme phrase~Oxymore~Opposition de mots~Meme groupement"))

# ============================================================ FRA2
add("FRA2", "Argumentation : these, arguments et construction d'un paragraphe", "Français", ["1re"],
S("Un texte argumentatif vise a convaincre ou a persuader un destinataire d'une these donnee."
  "|La these est l'opinion defendue ; elle est souvent accompagnee d'une antiphrase ou d'un contre-argument."
  "|Les arguments sont des raisons qui justifient la these : ils peuvent etre logiques, moraux, affectifs ou pragmatiques."
  "|Un exemple concret appuie l'argument et le rend plus probant pour le lecteur."
  "|Le connecteur logique organise le raisonnement : d'abord, ensuite, donc, cependant, en effet."
  "|La structure classique d'un paragraphe est : affirmation de l'idee, developpement, exemple, conclusion partielle."
  "|Le debat contradictoire presente une objection puis la refuge, ce qui renforce la credibilite de l'auteur."
  "|La these peut etre implicite : le lecteur doit alors la deduire de l'accumulation des arguments."
  "|Convaincre s'appuie sur la raison et les preuves ; persuader joue davantage sur les emotions et le pathos."
  "|Les modalites d'énonciation (je, nous, on, il) situent l'auteur par rapport a son propos."
  "|Les figures d'autorite (citation, reference a un expert, a la loi) sont des arguments d'autorite."
  "|Dans le bac STI2D, l'ecrit de francais attend une problematique claire et un plan d'argumentation progressif."),
[QC("Qu'est-ce qu'une these ?", "Un exemple~L'opinion defendue~Un connecteur~Une citation", 1,
    "La these est l'affirmation centrale que l'auteur cherche a etablir."),
 QC("Quel role joue un exemple dans un paragraphe argumentatif ?", "Il remplace l'argument~Il appuie et concretise l'argument~Il conclut le debat~Il presente l'objection", 1,
    "L'exemple rend l'argument plus concret et plus crédible."),
 QC("Quel connecteur introduit une opposition ?", "En effet~Cependant~Ainsi~De plus", 1,
    "Cependant, mais, toutefois marquent une opposition ou une restriction."),
 QC("Convaincre s'appuie principalement sur...", "Les emotions~La raison et les preuves~Le hasard~La rime", 1,
    "Convaincre releve de la logique et des preuves ; persuader joue sur le pathos."),
 QC("Que faut-il faire d'une objection dans un debat contradictoire ?", "L'ignorer~La presenter puis la refuter~La transformer en these~La supprimer", 1,
    "Refuter une objection renforce la position defendue."),
 QC("Quel est un argument d'autorite ?", "Une statistique personnelle~Une citation d'expert ou un texte de loi~Une metaphore~Une question rhetorique", 1,
    "L'appel a une source reconnue est un argument d'autorite."),
 QC("Quelle structure est attendue pour un paragraphe argumentatif ?", "Idee, developpement, exemple, conclusion partielle~Exemple, idee, question~Citation seule~Conclusion sans preuve", 0,
    "Le paragraphe progresse de l'idee a sa demonstration, puis a sa conclusion partielle."),
 QT("Distinguer convaincre et persuader, puis indiquer comment les deux procédés peuvent cooperer.",
    "Convaincre vise l'intelligence du lecteur : l'auteur propose une these, des arguments logiques, des exemples et des preuves, dans une demarche ouverte au doute. Persuader vise l'adhesion emotionnelle : l'auteur utilise le pathos, des images, un rythme, des appels au lecteur et une présence forte de l'énonciation. Les deux procedes cohabitent dans la plupart des textes : une preuve bien presentee avec une image frappante touche et convainc en meme temps. Un texte equilibre evite cependant le manipulateur pathos sans argument et la froideur d'une demonstration sans exemple.",
    "On attend la distinction raison / emotion et un exemple de cooperation entre les deux."),
 QT("Construire un paragraphe argumentatif defendant l'idée que le travail en equipe favorise l'innovation.",
    "On affirme d'abord la these : le travail en equipe favorise l'innovation parce qu'il confronte des points de vue differents. On developpe : chaque membre apporte une competence propre, et le dialogue fait apparaitre des solutions qu'aucun n'aurait trouvees seul. On ajoute un exemple : dans un projet de prototype STI2D, l'échange entre un specialiste electronique et un specialiste mecanique permet de réduire l'encombrement d'un capteur. On conclut partiellement : la diversite des regards est donc une source d'innovation, a condition d'etre organisee. On peut enfin introduire une objection (le travail en equipe peut ralentir la decision) et la refuter par une bonne repartition des roles.",
    "On verifie la presence de la these, de l'argument, de l'exemple, du connecteur et de la conclusion partielle.")],
C("Un texte argumentatif defend une these a l'aide d'arguments et d'exemples organises par des connecteurs.",
  "These + arguments + exemples + connecteurs = raisonnement lisible",
  "Convaincre = raison et preuves · persuader = emotion et pathos · objection puis refutation",
  "These~Opinion defendue~Sujet de debat~Argument~Raison avancee~Logique ou moral~Exemple~Cas concret~Preuve appuyee",
  "Enoncer la these|Choisir des arguments varies|Appuyer par un exemple|Introduire et refuter une objection|Conclure le paragraphe",
  "Affirmer sans prouver|Confondre exemple et argument|Ignorer l'objection|Emplier des connecteurs contradictoires",
  "These~Travail en equipe et innovation~Argument~Diversite des regards~Exemple~Projet de prototype~Refutation~Repartition des roles",
  "Convaincre~Raison et preuves~Auditoire reflechi~Persuader~Emotion et images~Adhesion du lecteur",
  "Objection~Contre-argument~A refuter~These~Affirmation centrale~A defendre"))

# ============================================================ FRA3
add("FRA3", "Lecture analytique : construire une interpretation de texte", "Français", ["1re"],
S("La lecture analytique est une explication methodique d'un texte qui rend compte de sa construction et de son sens."
  "|Elle commence par une presentation sobre du document : auteur, oeuvre, date, situation d'énonciation et genre."
  "|Le sens global du texte se degage de son theme et de sa these ou de son intention principale."
  "|Le plan de lecture suit generalement le mouvement du texte plutot qu'une simple liste de figures."
  "|Chaque partie doit combiner une observation precise (citation) et une interpretation (effet produit)."
  "|La citation s'integre dans la phrase et s'accompagne d'une reference precise au vers ou a la ligne."
  "|L'énonciation (je, tu, nous, il, present, passe) construit une relation entre l'auteur, le lecteur et le monde represente."
  "|Les registres, les temps verbaux, la ponctuation et le rythme sont des indices interpretatifs."
  "|Les champs lexicaux donnent au texte une coherences thematicque et orientent la lecture."
  "|Interpreter ne signifie pas inventer : toute hypothese doit etre justifiee par des elements du texte."
  "|La conclusion rapproche le texte de son contexte historique, esthetique ou de la question posesee."
  "|A l'oral du bac STI2D, la lecture analytique est presentee dans un expose suivi d'un entretien avec l'examinateur."),
[QC("Par quoi commence une lecture analytique ?", "Par une citation~Par une presentation du document~Par la conclusion~Par une opinion personnelle", 1,
    "On presente d'abord l'auteur, l'oeuvre, la date et le genre avant d'entrer dans le texte."),
 QC("Comment doit-on integrer une citation ?", "Sans reference~Dans la phrase, avec une reference precise~En fin de copie seulement~En italique obligatoire", 1,
    "La citation s'integre dans le developpement et est localisee (vers ou ligne)."),
 QC("Quel plan est generalement privilegie ?", "L'ordre alphabetique des figures~Le mouvement du texte~La longueur des paragraphes~L'ordre des dates de publication", 1,
    "Le plan suit les etapes de la construction du sens dans le texte."),
 QC("Qu'appelle-t-on champ lexical ?", "Une liste de figures~Un ensemble de mots lies par un theme~Une rime~Un type de phrase", 1,
    "Le champ lexical assure la coherence thematicque d'un passage."),
 QC("Que faut-il faire apres une observation precise ?", "S'arretter~Proposer une interpretation justifiee~Changer de texte~Repeter la citation", 1,
    "Observation et interpretation sont indissociables : on explique l'effet produit."),
 QC("Quel indice d'énonciation oriente la lecture ?", "Le nombre de pages~L'usage de je, tu, nous et des temps~La couverture du livre~La police de caracteres", 1,
    "Les pronoms et les temps situent la parole et construisent la relation au lecteur."),
 QC("Que faire d'une hypothese non justifiee par le texte ?", "La conserver telle quelle~La reformuler ou l'ecarter~La citer comme preuve~L'ignoreer dans la conclusion", 1,
    "Une interpretation doit toujours s'appuyer sur des indices textuels verifies."),
 QT("Décrire la methode a suivre pour analyser un poeme en trois parties.",
    "On lit d'abord le poeme plusieurs fois, on identifie son auteur, sa date, sa forme (vers, rimes, strophes) et son theme general. On observe ensuite le mouvement du texte : exemple, premiere strophe qui pose une situation, deuxieme strophe qui developpe une image ou un conflit, troisieme strophe qui apporte un retournement ou une conclusion. Dans chaque partie, on cite un vers precis, on nomme les procedes (figures, rythme, sonorites, enonciation) et on explique l'effet produit. On termine par une interpretation d'ensemble qui relie la forme au sens et au contexte de l'oeuvre, en repondant a la question posee si elle existe.",
    "On attend une progression presentation, analyse movementee, interpretation finale, avec citations localisees."),
 QT("Pourquoi faut-il eviter le commentaire purement subjectif dans une lecture analytique ?",
    "Parce que l'exercice évalue une competence de lecture et non l'expression d'une preference. Une reaction personnelle (« j'aime ce passage ») n'est pas demontree et ne peut etre discutee. Une lecture analytique produit une connaissance partageable : elle s'appuie sur des marqueurs verifies dans le texte (mots, images, rythme, temps) et propose une interpretation que l'examinateur peut contrôler. Le gout personnel peut etre mentionne en ouverture ou en conclusion, mais il doit toujours etre converti en analyse : dire pourquoi un passage produit un effet et par quels moyens. C'est cette exigence de preuve qui distingue l'analyse de l'opinion.",
    "On oppose opinion subjective et interpretation denonciable par des indices textuels.")],
C("La lecture analytique est une demonstration : chaque citation appuie une interpretation et suit le mouvement du texte.",
  "Observation citee + interpretation justifiee = analyse",
  "Presentation : auteur, date, genre · plan : mouvements du texte · enonciation et champs lexicaux",
  "Citation~Passage precise~Localisee~Observation~Procede repere~Figure ou rythme~Interpretation~Effet produit~Justifiee",
  "Lire et presenter le document|Degager le sens global|Suivre les mouvements du texte|Citer et analyser chaque etape|Conclure en reliant forme et sens",
  "Citer sans interpreter|Inventer une intention non prouvee|Suivre un plan mecanique|Oublier la situation d'énonciation",
  "Poeme~Vers et strophes~Rime~Sonorites~Champ lexical~Coherence thematique~Enonciation~Je et tu~Conclusion~Lien avec le contexte",
  "Observation~Ce que dit le texte~Interpretation~Ce que cela signifie",
  "Citation~Element integral~Reference~Localisation precise"))

# ============================================================ FRA4
add("FRA4", "Ecriture de l'essai : problematique, plan et conclusion", "Français", ["Terminale"],
S("L'essai est un texte personnel et argumente qui repond a une question en proposant une these progressive."
  "|La problematique transforme un sujet simple en question intellectuelle : elle fait apparaitre une tension."
  "|L'introduction presente le contexte, cite le sujet, pose la problematique et annonce le plan."
  "|Le plan dialectique (these, antithese, synthese) est adapte aux sujets comportant une opposition."
  "|Le plan thematique est preferable lorsque la question appelle une enumeration de points de vue ou d'exemples."
  "|Chaque argument doit etre accompagne d'un exemple precise, historique, littéraire ou tiré de l'experience."
  "|Les transitions assurent le passage d'une partie a l'autre et rendent la progression visible."
  "|La these n'est pas necessairement definitive : l'essai peut aboutir a une position nuancee."
  "|La conclusion repond a la problematique, fait le bilan du cheminement et ouvre sur une question plus large."
  "|L'ecrit de francais du bac STI2D dure quatre heures et comporte deux parties : une question de lecture et un essai."
  "|La qualite de la langue, la ponctuation et la presentations sont prises en compte dans la notation."
  "|Un essai reussi concilie une construction rigoureuse et une voix personnelle, sans se contenter de restituer un cours."),
[QC("Qu'est-ce qu'une problematique ?", "Une simple definition~Une question qui fait apparaitre une tension~Un exemple~Une citation", 1,
    "La problematique transforme le sujet en question problematisée et discutable."),
 QC("Que contient l'introduction d'un essai ?", "Seulement la these~Contexte, sujet, problematique, annonce du plan~La conclusion~Les exemples", 1,
    "L'introduction remplit quatre fonctions dans un ordre classique."),
 QC("Quand choisir un plan dialectique ?", "Quand le sujet comporte une opposition~Quand on manque d'arguments~Quand le sujet est une date~Toujours", 0,
    "Le plan these-antithese-synthese convient aux sujets contradictoires."),
 QC("Quel role joue un exemple dans l'essai ?", "Il remplace la these~Il rend l'argument concret et crédible~Il annonce le plan~Il conclut", 1,
    "L'exemple est le soutien concret de l'argument general."),
 QC("Que fait-on dans la conclusion ?", "On pose la problematique~On repond a la problematique et on ouvre~On presente l'auteur~On cite un texte", 1,
    "La conclusion donne la reponse construite et propose une ouverture."),
 QC("Quelle est une qualite attendue d'un essai ?", "Une voix personnelle et un plan rigoureux~Absence de plan~Beaucoup de citations sans analyse~Une simple opinion", 0,
    "L'essai allie rigueur de construction et position personnelle argumentee."),
 QC("Combien de parties comporte l'ecrit de francais au bac STI2D ?", "Une~Deux~Trois~Quatre", 1,
    "L'ecrit comprend une question sur un document et un essai sur une oeuvre ou un theme."),
 QT("Transformer le sujet « La technologie rend-elle les hommes libres ? » en problematique et proposer un plan.",
    "Le sujet oppose une attente d'emancipation a la possibility d'une nouvelle dependance. On peut le problematiser ainsi : « la technique, en supprimant certaines contraintes, ne crée-t-elle pas des formes inédites de dependance et d'aliénation ? » On choisit un plan dialectique : premierement, la technologie libere en economisant le temps et l'effort et en donnant acces a l'information ; deuxiement, elle asservit quand l'utilisateur devient dependant d'un système ou que la donnée est capturee ; troisiemement, la liberation dépend des usages et d'une maitrise critique de l'outil. La conclusion répond que la technologie est un moyen et non une fin, et que la liberte reste liee au jugement de l'utilisateur.",
    "On attend une question problematisée, un plan explicite et une these nuancee."),
 QT("Expliquer la difference entre un plan thematique et un plan dialectique.",
    "Le plan dialectique organise le propos selon une opposition : these, antithese, puis synthese qui depasse le conflit. Il convient aux sujets qui invitent a discuter deux positions contraires. Le plan thematique repartit la matiere en axes independants (par exemple les causes, les consequences, les remedes, ou trois domaines d'application). Il convient lorsque la question demande d'explorer plusieurs facettes sans contradiction centrale. Le choix dépend donc de la nature du sujet : un plan impose une progression logique et doit apparaitre clairement dans l'annonce de l'introduction ; un plan mal adapte rend l'argumentation confuse meme si les idees sont bonnes.",
    "On definit les deux plans, on donne leur domaine d'emploi et on lie le choix au sujet.")],
C("L'essai est une demonstration personnelle : une problematique claire, un plan adapte et des exemples precises.",
  "Introduction = contexte + sujet + problematique + plan",
  "Plan dialectique : these, antithese, synthese · plan thematique : axes paralleles",
  "Problematique~Question centrale~Tension~Introduction~Quatre etapes~Annonce du plan~Argument~Raison appuyee~Exemple a l'appui",
  "Analyser les termes du sujet|Formuler la problematique|Choisir un plan construisant la these|Argumenter avec des exemples|Conclure et ouvrir",
  "Repondre par oui ou non sans nuancer|Confondre plan thematique et dialectique|Entasser des citations sans analyse|Oublier l'annonce du plan",
  "Sujet~La technologie et la liberte~Problematique~Liberation ou dependance~Plan~These, antithese, synthese~Conclusion~Maitrise critique de l'outil",
  "Plan dialectique~Opposition resolue~These puis antithese~Plan thematique~Axes paralleles~Enumeration d'aspects",
  "Problematique~Question discutable~Sujet~Consigne donnee"))

# ============================================================ MTH1
add("MTH1", "Fonctions affines et lineaires : lire et modeliser une relation", "Maths", ["1re"],
S("Une fonction associe a chaque nombre x un seul nombre y, appele image de x."
  "|L'ensemble de definition est l'ensemble des valeurs de x pour lesquelles le calcul est possible."
  "|Une fonction affine est de la forme f(x) = ax + b, ou a est le coefficient directeur et b l'ordonnee a l'origine."
  "|Une fonction lineaire est le cas particulier b = 0 : f(x) = ax et la droite passe par l'origine."
  "|La representations graphique d'une fonction affine est une droite : b donne le point (0 ; b) et a donne la pente."
  "|Si a > 0 la fonction est croissante ; si a < 0 elle est decroissante ; si a = 0 elle est constante."
  "|Le coefficient directeur se calcule avec deux points : a = (y2 − y1) / (x2 − x1)."
  "|Resoudre f(x) = k revient a chercher les abscisses des points d'intersection avec la droite horizontale y = k."
  "|Resoudre f(x) >= k revient a garder les abscisses pour lesquelles la droite est au-dessus de y = k."
  "|Une situation de proportionnalite se modele par une fonction lineaire : le coefficient est le coefficient de proportionnalite."
  "|Une situation avec un cout fixe et un cout variable se modele par une fonction affine : b est le cout fixe."
  "|Ces functions servent en STI2D a relier une grandeur de commande et une grandeur de sortie, ou un cout et une quantite."),
[QC("Quelle est la forme d'une fonction affine ?", "f(x) = ax² + b~f(x) = ax + b~f(x) = a/x~f(x) = x + b²", 1,
    "Une fonction affine s'ecrit f(x) = ax + b."),
 QC("Que represente le coefficient a ?", "L'ordonnee a l'origine~La pente de la droite~Le point d'intersection avec l'axe des x~L'ensemble de definition", 1,
    "Le coefficient directeur a donne la pente et le sens de variation."),
 QC("Par quel point passe toujours une fonction lineaire ?", "(0 ; 1)~L'origine (0 ; 0)~(1 ; 1)~(0 ; b)", 1,
    "Pour f(x) = ax, f(0) = 0 : la droite passe par l'origine."),
 QC("Une droite est decroissante si...", "a > 0~a < 0~a = 0~b > 0", 1,
    "Un coefficient directeur negatif donne une droite decroissante."),
 QC("Comment calculer a avec deux points A et B ?", "(x2 − x1)/(y2 − y1)~(y2 − y1)/(x2 − x1)~y1 × y2~x1 + x2", 1,
    "Le coefficient directeur est le rapport de la variation des ordonnees sur celle des abscisses."),
 QC("Que represente graphiquement f(x) = 3 ?", "Une droite verticale~Une droite horizontale y = 3~Une parabole~Le point (3 ; 0)", 1,
    "L'equation f(x) = 3 se lit sur l'horizontale y = 3."),
 QC("Un cout fixe de 50 et 2 par unite se modele par...", "f(x) = 2x~f(x) = 50x~f(x) = 2x + 50~f(x) = 50 + x/2", 2,
    "Le cout variable est la pente 2 et le cout fixe l'ordonnee a l'origine 50."),
 QT("Une fonction affine passe par A(2 ; 7) et B(5 ; 16). Determiner son equation et calculer f(20).",
    "Le coefficient directeur vaut a = (16 − 7)/(5 − 2) = 9/3 = 3. En utilisant le point A : 7 = 3 × 2 + b, donc b = 1. L'equation est f(x) = 3x + 1 ; on la verifie avec B : 3 × 5 + 1 = 16. Alors f(20) = 3 × 20 + 1 = 61. Graphiquement, la droite coupe l'axe des ordonnees en (0 ; 1) et s'eleve de 3 unites quand x augmente de 1.",
    "On attend le calcul de la pente, le determination de b, le resultat et une verification."),
 QT("Expliquer comment lire graphiquement les solutions de f(x) > 2 pour une droite croissante.",
    "On trace la droite y = f(x) et la droite horizontale y = 2. On repere l'abscisse x0 du point d'intersection, puis on garde les abscisses pour lesquelles la represente graphique de f est strictement au-dessus de y = 2. Pour une droite croissante, cela correspond a x > x0 ; pour une droite decroissante, a x < x0. On verifie le resultat en testant une valeur de chaque cote de x0 dans l'expression de f. La methode graphique donne une lecture immediate, mais le calcul algebrique permet de confirmer la valeur exacte de x0.",
    "On decrit la construction, la comparaison de positions et la verification algebrique.")],
C("Une fonction affine se lit comme une droite : la pente donne le rythme de variation, l'ordonnee a l'origine le depart.",
  "f(x) = ax + b · a = (y2 − y1)/(x2 − x1)",
  "Lineaire : b = 0 · croissante si a > 0 · decroissante si a < 0",
  "Fonction~Antecedent et image~Ensemble de definition~Affine~Droite de pente a~f(x)=ax+b~Lineaire~Passe par l'origine~Proportionnalite",
  "Identifier le type de relation|Calculer a avec deux points|Determiner b|Tracer la droite|Lire ou calculer l'image",
  "Confondre pente et ordonnee a l'origine|Oublier le signe de a|Lire l'ordonnee au lieu de l'abscisse|Ignorer le domaine de definition",
  "A(2;7), B(5;16)~a=3 et b=1~f(20)=61~Cout fixe 50~f(x)=2x+50~x>2~Droite croissante au-dessus de y=2",
  "Fonction affine~Droite decalee~b non nul~Fonction lineaire~Droite par l'origine~b=0",
  "Croissante~a positif~Decroissante~a negatif"))

# ============================================================ MTH2
add("MTH2", "Equations et inequations du premier degre : resoudre et interpreter", "Maths", ["1re"],
S("Une equation est une egalite comportant une inconnue : resoudre revient a trouver les valeurs qui la rendent vraie."
  "|Une equation du premier degre s'ecrit ax + b = c avec a non nul ; elle admet une seule solution x = (c − b)/a."
  "|Les operations autorisees sont l'ajout ou la soustraction du meme nombre des deux cotes, et la multiplication ou la division par un meme nombre non nul."
  "|La methode consiste a isoler le terme contenant x puis a diviser par son coefficient."
  "|Une inequation du premier degre s'ecrit ax + b >= c ou ax + b <= c ; sa solution est un intervalle."
  "|Lorsqu'on multiplie ou divise une inequation par un nombre negatif, le sens de l'inegalite change."
  "|Le signe strict (< ou >) exclut la borne, le signe large (<= ou >=) l'inclut."
  "|Un systeme de deux equations se resout par substitution ou par combinaison lineaire."
  "|Une equation produit nul implique qu'au moins un des facteurs est nul."
  "|Verifier une solution consiste a la remplacer dans l'equation initiale et a controler l'egalite."
  "|Une equation sans solution se traduit par une egalite impossible comme 0 = 5 ; une equation identite a une infinité de solutions."
  "|En technologie, resoudre une equation permet de determiner une tension, une resistance ou une dimension."),
[QC("Combien de solutions admet ax + b = c avec a non nul ?", "Aucune~Une seule~Deux~Une infinité", 1,
    "Une equation du premier degre a une solution unique x = (c − b)/a."),
 QC("Que se passe-t-il quand on divise une inequation par un nombre negatif ?", "Rien~Le sens de l'inegalite change~La solution devient nulle~On ajoute une borne", 1,
    "Multiplier ou divisor par un nombre negatif inverse le sens de l'inegalite."),
 QC("Quelle est la solution de 3x + 6 = 0 ?", "x = 2~x = −2~x = 6~x = −6", 1,
    "3x = −6 donc x = −2."),
 QC("Que represente ]−∞ ; 3[ ?", "x <= 3~x < 3~x > 3~x = 3", 1,
    "Le crochet exclut la borne 3 et l'intervalle va vers moins l'infini."),
 QC("Quelle operation est interdite dans une equation ?", "Ajouter 2 des deux cotes~Diviser par zero~Soustraire x des deux cotes~Multiplier par 3", 1,
    "La division par zero est impossible et doit etre exclue."),
 QC("Comment resoudre un produit de facteurs nul ?", "En additionnant les facteurs~En annulant chacun des facteurs~En les multipliant~En les divisant", 1,
    "Un produit est nul si et seulement si l'un des facteurs est nul."),
 QC("Que faut-il faire apres avoir trouve une solution ?", "La remplacer dans l'equation pour verifier~La changer de signe~L'arrondir~L'oublier", 0,
    "La verification par substitution est indispensable."),
 QT("Resoudre l'inequation −2x + 8 <= 2 et representer l'ensemble des solutions.",
    "On soustrait 8 des deux cotes : −2x <= −6. On divise par −2 en changeant le sens de l'inegalite : x >= 3. L'ensemble des solutions est [3 ; +∞[. On represente un point ferme en 3 puis une fleche vers la droite, car la borne est incluse. On verifie avec x = 4 : −8 + 8 = 0 <= 2, vrai ; avec x = 2 : −4 + 8 = 4 > 2, faux. L'erreur frequente est d'oublier d'inverser le signe lors de la division par le nombre negatif.",
    "On attend l'inversion du signe, l'intervalle [3 ; +∞[ et une verification."),
 QT("Un atelier a un cout fixe de 120 et 8 par piece. Le budget est de 400. Combien de pieces peut-on produire ?",
    "On modele le cout total par C(n) = 8n + 120. La contrainte est 8n + 120 <= 400, soit 8n <= 280, puis n <= 35. Comme le nombre de pieces est un entier naturel, on peut produire au plus 35 pieces, et le budget est alors exactement epuise : 8 × 35 + 120 = 400. Si l'on voulait strictement rester sous le budget, on s'arreterait a 34 pieces. On presente la reponse avec l'equation, l'inequation et la verification du cout final.",
    "On attend la modelisation, la resolution et l'interpretation entiere du resultat.")],
C("Resoudre une equation, c'est isoler l'inconnue par des operations reversibles ; pour une inequation, surveiller le signe.",
  "ax + b = c → x = (c − b)/a · ax + b <= c → intervalle",
  "Division par un nombre negatif : inverser le signe · crochet ferme = borne incluse",
  "Equation~Egalite avec inconnue~Une solution~Inequation~Comparaison~Intervalle de solutions~Substitution~Verification~Controle final",
  "Ecrire l'equation a partir de l'enonce|Regrouper les termes en x|Isoler l'inconnue|Respecter le sens de l'inegalite|Verifier la solution",
  "Diviser par un nombre negatif sans changer le signe|Oublier la verification|Confondre crochet et parenthese|Accepter une solution non entiere sans le dire",
  "3x+6=0~x=-2~−2x+8<=2~x>=3~C(n)=8n+120~n<=35~0=5~Aucune solution",
  "Equation~Une valeur~Solution unique~Inequation~Un intervalle~Plusieurs solutions",
  "Signe strict~Borne exclue~Signe large~Borne incluse"))

# ============================================================ MTH3
add("MTH3", "Statistiques descriptives : decrire et interpreter une serie", "Maths", ["1re"],
S("La statistique descriptive resume un jeu de donnees pour en degager les caracteristiques essentielles."
  "|Une population est l'ensemble complet des individus etudies ; un echantillon en est une partie."
  "|Un echantillon representatif reflète la composition de la population pour les caracteres pertinents."
  "|Un effectif est le nombre d'individus d'une classe ; la frequence est l'effectif divise par l'effectif total."
  "|La moyenne est la somme des valeurs divisée par l'effectif ; elle est sensible aux valeurs extremes."
  "|La mediane est la valeur centrale d'une serie ordonnee : elle resiste aux valeurs aberrantes."
  "|Les quartiles Q1 et Q3 decoupent la serie en quatre parties ; l'ecart interquartile contient 50 % des donnees."
  "|L'etendue est la difference entre la valeur maximale et la valeur minimale."
  "|La variance et l'ecart-type mesurent la dispersion autour de la moyenne."
  "|L'ecart-type est la racine carree de la variance et s'exprime dans la meme unité que la donnee."
  "|L'histogramme convient a une variable continue, le diagramme en batons a une variable discrete."
  "|Toute presention statistique doit indiquer la source, la taille de l'echantillon et les unites."),
[QC("Quel indicateur resiste aux valeurs extremes ?", "La moyenne~La mediane~L'ecart-type~L'etendue", 1,
    "La mediane depend du rang, pas de l'amplitude des valeurs."),
 QC("Comment calcule-t-on une frequence ?", "Effectif × total~Effectif / effectif total~Total / effectif~Max − min", 1,
    "La frequence relative est l'effectif de la classe divisé par l'effectif total."),
 QC("Que mesure l'ecart-type ?", "La tendance centrale~La dispersion~Le nombre d'individus~La correlation", 1,
    "L'ecart-type quantifie la dispersion autour de la moyenne."),
 QC("Dans une serie ordonnee de 7 valeurs, quelle est la position de la mediane ?", "La 3e~La 4e~La 7e~La moyenne des 3e et 4e", 1,
    "Pour n = 7, la mediane est la valeur de rang (n+1)/2 = 4."),
 QC("Que contient l'ecart interquartile ?", "Les 10 % extremes~La moitie centrale des donnees~Toutes les donnees~Seulement la moyenne", 1,
    "L'intervalle entre Q1 et Q3 contient 50 % des observations."),
 QC("Quel graphique convient a une variable quantitative continue ?", "Le camembert~L'histogramme~Le diagramme en batons~La fleche", 1,
    "L'histogramme represente les effectifs par classes de valeurs continues."),
 QC("Quelles informations doivent accompagner un resultat statistique ?", "La couleur du graphique~La source, l'effectif et les unites~Le nom du logiciel~La date du jour", 1,
    "Source, taille d'echantillon et unites sont indispensables a l'interpretation."),
 QT("Une serie de 5 temps de reaction en ms est 10, 12, 14, 16, 98. Calculer moyenne, mediane, etendue et commenter.",
    "La somme vaut 10 + 12 + 14 + 16 + 98 = 150, donc la moyenne est 150/5 = 30 ms. La serie est ordonnee ; avec 5 valeurs, la mediane est la troisieme, soit 14 ms. L'etendue vaut 98 − 10 = 88 ms. L'ecart de 16 ms entre moyenne et mediane est du a la valeur 98 ms, qui tire la moyenne vers le haut. La mediane decrit mieux le comportement habituel. Il faut chercher la cause de cette valeur aberrante avant de conclure sur la performance du systeme, puis eventuellement la signaler sans la supprimer arbitrairement.",
    "On attend les quatre calculs, l'explication de l'ecart par l'extreme et une conclusion prudente."),
 QT("Pourquoi un echantillon non representatif invalide-t-il une generalisation, meme avec un grand effectif ?",
    "La representativite signifie que la composition de l'echantillon reflète celle de la population pour les caracteres utiles. Si le prelevement est biaisé, par exemple en n'interrogeant que les utilisateurs satisfaits ou une seule tranche d'age, les estimateurs comme la moyenne ou la frequence sont systematiquement decales. Augmenter l'effectif ne corrige pas un biais de recrutement : cela rend seulement le resultat biaisé avec plus de precision apparente. Un tirage aleatoire, une stratification et un effectif suffisant limitent ce risque. On indique egalement une marge d'incertitude et un niveau de confiance avant de generaliser.",
    "On relie representativite, biais et impossibilite de corriger un biais par l'effectif seul.")],
C("La statistique descriptive resumee par une tendance centrale et une dispersion, en choisissant des indicateurs adaptes.",
  "Frequence = effectif / total · ecart-type = racine de la variance",
  "Moyenne sensible aux extremes · mediane robuste · Q1 et Q3 pour 50 % central",
  "Population~Ensemble complet~Echantillon~Partie prelevee~Representativite~Moyenne~Somme sur effectif~Mediane~Valeur centrale",
  "Definir la population et l'echantillon|Trier les donnees|Choisir les indicateurs|Construire le graphique|Interpréter avec source et unites",
  "Utiliser la moyenne avec une valeur aberrante|Confondre effectif et frequence|Choisir un camembert pour du continu|Omettre la taille de l'echantillon",
  "10;12;14;16;98~Moyenne 30, mediane 14~Etendue~88 ms~Frequence~Effectif sur total~Histogramme~Variable continue~Q1 Q3~50 % central",
  "Moyenne~Sensible aux extremes~Mediane~Robuste aux extremes",
  "Effectif~Nombre d'individus~Frequence~Part du total"))

# ============================================================ PHY1
add("PHY1", "Grandeurs, unites et mesures : le systeme international", "Physique-Chimie", ["1re"],
S("Une grandeur physiques est une propriete measurable, caracterisee par une valeur numerique et une unité."
  "|Le systeme international (SI) repose sur sept grandeurs de base : longueur, masse, temps, courant, temperature, quantite de matiere et intensite lumineuse."
  "|Les unites de base correspondantes sont le metre, le kilogramme, la seconde, l'ampere, le kelvin, la mole et la candela."
  "|Les multiples et sous-multiples utilisent des prefixes décimaux : kilo (10^3), centi (10^-2), milli (10^-3), micro (10^-6)."
  "|Une conversion d'unite se fait en remplacant le prefixe par sa puissance de 10, sans changer la grandeur physique."
  "|Une mesure comporte toujours une incertitude : elle s'exprime avec une valeur et une incertitude absolue ou relative."
  "|L'ecart maximal est la difference entre la valeur mesuree et la valeur de reference, en valeur absolue."
  "|L'incertitude relative est l'incertitude absolue divisée par la valeur mesuree, souvent en pourcentage."
  "|Les chiffres significatifs indiquent la precision de la mesure : on ne conserve que les chiffres pertinents."
  "|Une grandeur derivee se construit a partir des grandeurs de base, comme la vitesse (m/s) ou la force (newton)."
  "|La notation scientifique ecrit un nombre sous la forme a × 10^n avec 1 <= a < 10."
  "|Savoir convertir et estimer une incertitude est indispensable pour exploiter un relevé de capteur en STI2D."),
[QC("Combien de grandeurs de base compte le SI ?", "Cinq~Six~Sept~Huit", 2,
    "Le systeme international definit sept grandeurs de base."),
 QC("Quelle est l'unite de base du temps ?", "La minute~L'heure~La seconde~Le milliseconde", 2,
    "L'unite de base du temps est la seconde (s)."),
 QC("Que signifie le prefixe milli ?", "10^-2~10^-3~10^3~10^6", 1,
    "milli corresponds a 10^-3, par exemple 1 mm = 10^-3 m."),
 QC("Comment ecrit-on 0,0045 en notation scientifique ?", "4,5 × 10^-3~45 × 10^-4~4,5 × 10^3~0,45 × 10^-2", 0,
    "On decale la virgule de trois rangs vers la droite : 4,5 × 10^-3."),
 QC("Qu'est-ce que l'incertitude absolue ?", "Le rapport entre deux mesures~L'ecart entre valeur mesuree et valeur de reference~La moyenne des mesures~Le nombre de chiffres", 1,
    "L'incertitude absolue s'exprime dans la meme unité que la grandeur mesuree."),
 QC("Comment calcule-t-on une incertitude relative ?", "Incertitude absolue × mesure~Incertitude absolue / mesure~Mesure / incertitude~Mesure − incertitude", 1,
    "L'incertitude relative est l'incertitude absolue divisée par la valeur mesuree."),
 QC("Quelle est l'unite derivee de la vitesse ?", "m~s~m/s~kg", 2,
    "La vitesse est un rapport distance/temps, en metres par seconde."),
 QT("Convertir 2,5 h en secondes et 250 mA en ampères, en detaillant les etapes.",
    "Pour le temps : 1 h = 3600 s, donc 2,5 h = 2,5 × 3600 = 9000 s, soit 9 × 10^3 s. Pour l'intensite : le prefixe milli vaut 10^-3, donc 250 mA = 250 × 10^-3 A = 0,250 A. Dans les deux cas on remplace l'unite de depart par sa valeur en unite de base, puis on effectue le produit. On verifie l'ordre de grandeur : 2,5 h est bien quelques milliers de secondes et 250 mA est bien une fraction d'ampere.",
    "On attend les facteurs de conversion, les resultats et une verification d'ordre de grandeur."),
 QT("Une resistance annoncee 100 ohms est mesuree a 103 ohms. Calculer l'ecart absolu et l'incertitude relative, puis commenter.",
    "L'ecart absolu vaut |103 − 100| = 3 ohms. L'incertitude relative vaut 3/100 = 0,03, soit 3 %. On peut presenter la mesure comme 103 ohms avec une incertitude de 3 %, ou 103 ± 3 ohms par rapport a la valeur de reference. Un ecart de 3 % peut provenir de la tolerance du composant, de la precision de l'appareil ou de la temperature. Avant de conclure a un defaut, on compare avec la tolerance annoncee par le fabricant et on repete la mesure dans les memes conditions.",
    "On attend l'ecart absolu, le pourcentage et une discussion des causes possibles.")],
C("Une grandeur se mesure avec une unite du SI ; toute mesure est accompagnee d'une incertitude qu'il faut savoir exprimer.",
  "Valeur mesuree = nombre × unite · incertitude relative = absolue / mesure",
  "SI : m, kg, s, A, K, mol, cd · milli = 10^-3 · notation scientifique a × 10^n",
  "Grandeur~Propriete measurable~Valeur et unite~Unite de base~Metre, seconde~Systeme international~Prefixe~Milli ou kilo~Incertitude~Ecart et precision",
  "Identifier la grandeur mesuree|Choisir l'unite et le prefixe|Convertir en unite de base|Calculer l'incertitude|Comparer a la tolerance",
  "Confondre masse et poids|Oublier l'unite dans un resultat|Ne pas convertir les prefixes|Donner trop de chiffres significatifs",
  "2,5 h~9000 s~250 mA~0,250 A~100 ohms~Ecart 3 ohms~3 %~Incertitude relative~4,5e-3~Notation scientifique",
  "Incertitude absolue~Ecart dans l'unite~Incertitude relative~Rapport sans unite",
  "Unite de base~SI~Unite derivee~Combinee, comme m/s"))

# ============================================================ PHY2
add("PHY2", "Mouvement et interactions : les lois de Newton", "Physique-Chimie", ["1re"],
S("La mecanique de Newton decrit le lien entre les forces exercees sur un objet et son mouvement."
  "|Un mouvement est etudie par rapport a un referentiel, cadre choisi pour mesurer positions et vitesses."
  "|La position est donnee par un vecteur ; la trajectoire est l'ensemble des positions successives."
  "|La vitesse moyenne sur un intervalle est le deplacement divise par la duree : v = Δx/Δt."
  "|L'acceleration est la variation de vitesse par unite de temps : a = Δv/Δt, en m/s²."
  "|Le principe d'inertie (1re loi) : si la somme des forces est nulle, le mouvement est uniforme ou le corps est immobile."
  "|Le principe fondamental de la dynamique (2e loi) : la somme des forces est egale a la masse multipliee par l'acceleration, ΣF = m × a."
  "|Le principe d'action et reaction (3e loi) : a toute action correspond une reaction de meme intensite et de sens oppose, sur un autre corps."
  "|Le poids est une force due a la gravite : P = m × g avec g environ 9,81 N/kg sur Terre."
  "|La masse est une propriete intrinsique en kg ; le poids est une force en newtons qui depend du lieu."
  "|Un diagramme des forces represente toutes les forces exercees sur un corps, avec leur point d'application et leur direction."
  "|Ces lois permettent de dimensionner un mecanisme ou de calculer l'effort necessaire a un actionneur."),
[QC("Dans quel cadre mesure-t-on une position ?", "Dans un referentiel~Dans un diagramme~Dans un circuit~Dans un graphique", 0,
    "Une position n'a de sens que par rapport a un referentiel choisi."),
 QC("Quelle est l'unite d'une acceleration ?", "m/s~m/s²~m²/s~kg", 1,
    "L'acceleration est une variation de vitesse par temps, en m/s²."),
 QC("Que dit le principe d'inertie ?", "Tout corps accelere en permanence~Si la somme des forces est nulle, le mouvement reste uniforme~La force est toujour nulle~Le poids n'existe pas", 1,
    "Sans force resultant, la vitesse reste constante (ou nulle)."),
 QC("Quelle est la forme du principe fondamental de la dynamique ?", "ΣF = m/a~ΣF = m × a~ΣF = a/m~ΣF = m + a", 1,
    "La somme des forces egale la masse fois l'acceleration."),
 QC("Que vaut le poids d'une masse de 10 kg sur Terre ?", "10 N~9,81 N~98,1 N~981 N", 2,
    "P = m × g = 10 × 9,81 = 98,1 N."),
 QC("Ou s'applique la reaction d'une action ?", "Sur le meme corps~Sur un autre corps~Nulle part~Au referentiel", 1,
    "Action et reaction s'exercent sur deux corps differents."),
 QC("Quel est le role d'un diagramme des forces ?", "Representer les forces sur un corps~Tracer la trajectoire~Calculer une tension~Mesurer une temperature", 0,
    "Le diagramme recense toutes les forces agissant sur le corps etudie."),
 QT("Un objet de 2 kg est soumis a une force horizontale de 10 N, sans frottement. Calculer son acceleration puis sa vitesse apres 3 s s'il part du repos.",
    "D'apres le principe fondamental, la force resultant vaut 10 N, donc a = ΣF/m = 10/2 = 5 m/s². En partant du repos et en supposant une acceleration constante, la vitesse apres 3 s vaut v = v0 + a × t = 0 + 5 × 3 = 15 m/s. Le deplacement parcouru serait x = 1/2 × a × t² = 22,5 m. On verifie l'homogeneite : N/kg donne bien m/s², et m/s² multiplie par s donne m/s.",
    "On attend le calcul de l'acceleration, celui de la vitesse et une verification d'unites."),
 QT("Expliquer pourquoi un passager est projete vers l'avant lors d'un freinage brutal, en utilisant le principe d'inertie.",
    "Avant le freinage, le vehicule et le passager ont la meme vitesse par rapport au sol. Lors du freinage, une force de friction s'exerce sur le vehicule, qui ralentit ; le passager, lui, n'est pas directement soumis a cette force. Par inertie, il conserve sa vitesse initiale par rapport au sol : par rapport au vehicule qui ralentit, il continue donc a avancer, ce qui se traduit par une projection vers l'avant. La ceinture de securite exerce alors sur lui une force opposee a son mouvement, qui le ralentit avec le vehicule. C'est une application directe du principe d'inertie et du principe fondamental de la dynamique.",
    "On lie le changement de referentiel, l'inertie et le role de la ceinture.")],
C("Le mouvement d'un corps se deduit des forces qui s'exercent sur lui : c'est le principe fondamental de la dynamique.",
  "ΣF = m × a · P = m × g · v = Δx/Δt",
  "Inertie : ΣF = 0 → vitesse constante · action et reaction sur deux corps distincts",
  "Referentiel~Cadre de mesure~Position et vitesse~Force~Action sur un corps~Newton~Acceleration~Variation de vitesse~Poids~Masse fois g",
  "Choisir le referentiel|Dessiner le diagramme des forces|Calculer la force resultant|Appliquer ΣF = m × a|Verifier l'unite du resultat",
  "Confondre masse et poids|Oublier une force dans le diagramme|Appliquer action et reaction sur le meme corps|Changer de referentiel en cours de calcul",
  "2 kg et 10 N~a = 5 m/s²~Apres 3 s~v = 15 m/s~10 kg~P = 98,1 N~g~9,81 N/kg",
  "Masse~Propriete intrinsique~Kilogramme~Poids~Force de gravite~Newton",
  "Inertie~Vitesse conserve~Action-reaction~Deux corps distincts"))

# ============================================================ PHY3
add("PHY3", "Energie, travail et puissance : quantifier une conversion", "Physique-Chimie", ["1re"],
S("En mechanique, le travail d'une force est le produit de la force par le deplacement de son point d'application."
  "|Pour une force constante et parallele au deplacement : W = F × d, en joules (1 J = 1 N × 1 m)."
  "|Si la force fait un angle avec le deplacement, on utilise la composante parallèle : W = F × d × cos(alpha)."
  "|Un travail nul correspond a une force perpendiculaire au deplacement ou a l'absence de deplacement."
  "|L'energie cinematique d'un corps de masse m et de vitesse v vaut Ec = 1/2 × m × v²."
  "|L'energie potentielle gravitationnelle près du sol vaut Ep = m × g × h."
  "|Le theoreme de l'energie cinematique relie le travail de la force resultant a la variation d'energie : ΣW = ΔEc."
  "|L'energie mecanique est la somme de l'energie cinematique et de l'energie potentielle."
  "|Les frottements convertissent une partie de l'energie mechanique en energie thermique : l'energie ne disparait pas, elle se transforme."
  "|La puissance est le travail effectue par unite de temps : P = W/Δt, en watts (1 W = 1 J/s)."
  "|Pour un mouvement uniforme avec une force constante, P = F × v."
  "|Le rendement d'une machine est le rapport entre energie utile et energie fournie : eta = E_utile / E_fournie, toujours inférieur a 1."),
[QC("Quelle est l'unite du travail en mecanique ?", "Le newton~Le joule~Le watt~Le pascal", 1,
    "Le travail se mesure en joules, comme l'energie."),
 QC("Que vaut le travail d'une force perpendiculaire au deplacement ?", "F × d~Zero~F/d~F + d", 1,
    "Le cosinus de 90 degres est nul, donc le travail est nul."),
 QC("Quelle est la formule de l'energie cinematique ?", "m × v~1/2 × m × v²~m × g × h~F × d", 1,
    "Ec = 1/2 × m × v², en joules."),
 QC("Quel effet ont les frottements sur l'energie mecanique ?", "Ils la creent~Ils la convertissent en chaleur~Ils la suppriment~Ils la doublent", 1,
    "L'energie est convertie en energie thermique, pas detruit."),
 QC("Comment calculer une puissance ?", "W × Δt~W / Δt~F / v~Ec + Ep", 1,
    "La puissance est le travail divise par la duree."),
 QC("Un moteur fournit 500 J en 10 s. Quelle est sa puissance ?", "5 W~50 W~500 W~5000 W", 1,
    "P = 500/10 = 50 W."),
 QC("Quel est un rendement possible pour une machine reelle ?", "1,2~0,75~2~L'infini", 1,
    "Le rendement est toujours strictement inferieur a 1 pour une machine reelle."),
 QT("Une caisse de 20 kg est soulevee de 2 m. Calculer le travail fourni et l'energie potentielle gagnee.",
    "La force a vaincre est le poids P = m × g = 20 × 9,81 = 196,2 N. Le travail fourni vaut W = P × h = 196,2 × 2 = 392,4 J. L'energie potentielle gravitationnelle gagnee est Ep = m × g × h = 20 × 9,81 × 2 = 392,4 J : les deux valeurs coincident car le travail sert ici exclusivement a augmenter l'energie potentielle, en neglectant les pertes. Si l'operation dure 4 s, la puissance moyenne est P = 392,4/4 = 98,1 W.",
    "On attend le calcul du poids, du travail, de l'energie et eventuellement de la puissance."),
 QT("Expliquer pourquoi le rendement d'un systeme est toujours inferieur a 1 et comment l'ameliorer.",
    "Le rendement compare l'énergie utile à l'énergie consommée : eta = E_utile / E_fournie. Une partie de l'énergie est toujours convertie en formes non utiles, principalement de la chaleur due aux frottements, aux résistances électriques ou aux pertes de conversion. L'énergie totale est conservée, mais sa qualité diminue : c'est une dégradation énergétique. On améliore le rendement en réduisant les frottements (lubrification, roulements), en choisissant des composants plus efficaces, en isolant thermiquement et en adaptant la charge à la conception de la machine. On ne peut cependant jamais atteindre 1, notamment à cause du second principe de la thermodynamique.",
    "On relie la conservation de l'energie aux pertes, puis on propose des actions concretes.")],
C("Travail, energie et puissance permettent de quantifier une conversion et ses pertes.",
  "W = F × d × cos(alpha) · P = W/Δt · eta = E_utile / E_fournie",
  "Ec = 1/2 m v² · Ep = m g h · ΣW = ΔEc · 1 J = 1 N·m · 1 W = 1 J/s",
  "Travail~Force fois deplacement~Joule~Energie~Capacite de produire un travail~Cinematique ou potentielle~Puissance~Travail par temps~Watt",
  "Repérer la force et le deplacement|Calculer le travail|Evaluer l'energie gagnee|Mesurer la duree|Calculer rendement et puissance",
  "Oublier le cosinus d'angle|Confondre travail et puissance|Croire que les frottements detruisent l'energie|Donner un rendement superieur a 1",
  "20 kg sur 2 m~392,4 J~500 J en 10 s~50 W~Rendement 0,75~75 % utile~F perpendiculaire~Travail nul",
  "Travail~Transfert d'energie~Puissance~Rythme du transfert",
  "Energie utile~Objective poursuivi~Energie perdue~Chaleur et frottements"))

# ============================================================ PHY4
add("PHY4", "Electricite : loi d'Ohm, circuits et mesures", "Physique-Chimie", ["1re"],
S("Un circuit electrique est un ensemble d'elements relies par des conducteurs pour permettre le passage du courant."
  "|L'intensite du courant I se mesure en ampères avec un ampèremetre place en serie dans le circuit."
  "|La tension U aux bornes d'un composant se mesure en volts avec un voltmetre place en derivation."
  "|La loi d'Ohm s'ecrit U = R × I pour un conducteur ohmique a temperature constante, avec R en ohms."
  "|Un conducteur ohmique a une characteristicque U = f(I) representee par une droite passant par l'origine."
  "|La resistance equivalent de resistances en serie est la somme : Req = R1 + R2."
  "|En parallele, l'inverse de la resistance equivalent est la somme des inverses : 1/Req = 1/R1 + 1/R2."
  "|En serie, l'intensite est la meme dans tous les elements et les tensions s'additionnent (loi des mailles)."
  "|En parallele, la tension est la meme aux bornes de chaque branche et les intensites s'additionnent (loi des noeuds)."
  "|La puissance electrique dissipee par un composant vaut P = U × I = R × I² = U²/R."
  "|L'energie electrique consommee est E = P × t ; elle se facture en kilowattheures (1 kWh = 3,6 × 10^6 J)."
  "|Le montage d'un capteur et le choix de son alimentation reposent sur ces lois, avec verification des calibres des appareils."),
[QC("Comment brancher un ampèremetre ?", "En derivation~En serie~Aux bornes de la source~Sans le brancher", 1,
    "L'ampèremetre mesure le courant qui le traverse : il se place en serie."),
 QC("Que dit la loi d'Ohm ?", "U = R/I~U = R × I~U = I/R~U = R + I", 1,
    "Pour un conducteur ohmique, la tension est proportionnelle a l'intensite."),
 QC("Quelle est la resistance equivalent de deux resistances de 10 et 20 ohms en serie ?", "5 ohms~15 ohms~30 ohms~200 ohms", 2,
    "En serie, on additionne : 10 + 20 = 30 ohms."),
 QC("Et en parallele ?", "30 ohms~6,7 ohms~15 ohms~200 ohms", 1,
    "1/Req = 1/10 + 1/20 = 0,15, donc Req = 6,7 ohms."),
 QC("Que s'additionne dans un circuit en parallele ?", "Les tensions~Les intensites~Les resistances~Les puissances uniquement", 1,
    "La loi des noeuds donne I = I1 + I2, la tension etant commune."),
 QC("Quelle est la puissance dissipee par une resistance de 10 ohms parcourue par 2 A ?", "5 W~20 W~40 W~200 W", 2,
    "P = R × I² = 10 × 4 = 40 W."),
 QC("Combien de joules dans 1 kWh ?", "1000 J~3600 J~3,6 × 10^6 J~3,6 × 10^3 J", 2,
    "1 kWh = 1000 W × 3600 s = 3,6 × 10^6 J."),
 QT("Deux resistances R1 = 6 ohms et R2 = 3 ohms sont branchées en parallele sous 12 V. Calculer les courants et la resistance equivalent.",
    "La tension etant la meme aux bornes de chaque branche, I1 = U/R1 = 12/6 = 2 A et I2 = U/R2 = 12/3 = 4 A. Le courant total vaut I = I1 + I2 = 6 A. La resistance equivalent est Req = U/I = 12/6 = 2 ohms ; on retrouve le meme resultat avec 1/Req = 1/6 + 1/3 = 1/2. On verifie que Req est bien inferieure a la plus petite resistance, ce qui est toujours le cas en parallele.",
    "On applique la loi d'Ohm branche par branche, la loi des noeuds et on verifie Req < R_min."),
 QT("Expliquer pourquoi un ampèremetre ne doit jamais etre branche en derivation aux bornes d'une source.",
    "Un ampèremetre a une resistance interne tres faible, proche de zero, pour perturber le moins possible le circuit. Le brancher en derivation aux bornes d'une source revient a creer un chemin de resistance quasi nulle : d'apres U = R × I, avec R tres petit, l'intensite devient tres elevee. C'est un court-circuit : le courant depasse le calibre de l'appareil, ce qui peut detruire l'ampèremetre, endommager la source et provoquer un echauffement dangereux des conducteurs. La bonne pratique est de placer l'ampèremetre en serie, en choisissant un calibre superieur au courant attendu, et de verifier les polarites avant de fermer le circuit.",
    "On cite la faible resistance interne, le court-circuit, le depassement de calibre et le branchement correct.")],
C("Les lois d'Ohm, des mailles et des noeuds permettent de prevoir courants, tensions et puissances dans un circuit.",
  "U = R × I · P = U × I · E = P × t",
  "Serie : I commun et tensions additionnees · parallele : U commune et intensites additionnees",
  "Ampèremetre~En serie~Courant~Voltmetre~En derivation~Tension~Resistance~Ohms~Loi d'Ohm~U = R I",
  "Dessiner le schema du circuit|Choisir les montages serie et parallele|Appliquer la loi d'Ohm|Additionner tensions ou intensites|Calculer puissance et verifier les calibres",
  "Brancher l'ampèremetre en parallele|Oublier la resistance interne des appareils|Confondre serie et parallele|Depasser le calibre d'un instrument",
  "6 ohms et 3 ohms~I1 = 2 A, I2 = 4 A~Req = 2 ohms~12 V~P = R I²~40 W~1 kWh~3,6 MJ",
  "Serie~Meme intensite~Tensions additionnees~Parallele~Meme tension~Intensites additionnees",
  "Ampèremetre~Mesure I~Voltmetre~Mesure U"))

# ============================================================ ANG1
add("ANG1", "Present simple and past simple : describing a system", "Anglais", ["1re"],
S("The present simple is used for facts, habits, general truths and technical specifications."
  "|At the present simple, the third person singular takes an -s : the sensor sends a signal."
  "|Negation and questions use the auxiliary do / does : the system does not start automatically."
  "|The past simple describes completed actions at a definite time in the past : the prototype failed yesterday."
  "|Regular verbs add -ed ; irregular verbs have a specific past form, such as go / went or make / made."
  "|The past simple negation uses did not + base form : the test did not confirm the hypothesis."
  "|Signal words for the past include yesterday, last week and two days ago; for the present, always, usually and every day."
  "|For a technical description, the present simple states what a component does and the past simple reports what happened during a test."
  "|The imperative is used for instructions : connect the sensor, check the voltage, press the button."
  "|The modal can expresses possibility or ability : the circuit can supply 12 volts."
  "|Must and have to express obligation : the operator must wear protective gloves."
  "|Mixing present and past tenses in the same paragraph requires a clear time reference for each action."),
[QC("Which form is correct for a general technical fact ?", "The sensor send a signal~The sensor sends a signal~The sensor sending a signal~The sensor is send a signal", 1,
    "At the present simple, the third person singular ends in -s."),
 QC("How do you negate a past simple sentence ?", "Does not + base form~Did not + base form~Not + past participle~Am not + verb", 1,
    "The past negation is did not followed by the base form of the verb."),
 QC("Which word signals the past simple ?", "Always~Usually~Yesterday~Every day", 2,
    "Yesterday refers to a completed time in the past."),
 QC("What is the past form of 'go' ?", "Goed~Went~Gone~Going", 1,
    "Go is irregular : go / went / gone."),
 QC("How do you give an instruction in English ?", "With the base form of the verb~With the present perfect~With a question~With the past participle", 0,
    "The imperative uses the base form : connect, check, press."),
 QC("What does 'can' express in a technical text ?", "Obligation~Ability or possibility~Past time~Negation", 1,
    "Can expresses ability or possibility : the circuit can supply 12 volts."),
 QC("Which sentence reports a test result correctly ?", "The test confirm the hypothesis~The test confirmed the hypothesis~The test confirming the hypothesis~The test is confirm the hypothesis", 1,
    "A completed test at a definite past moment takes the past simple."),
 QT("Put the following description into correct English: 'Le capteur envoie un signal. Hier, le test a échoué.' Explain the tenses used.",
    "The correct sentences are: 'The sensor sends a signal. Yesterday, the test failed.' The first sentence uses the present simple because it describes a permanent function of the sensor, a general truth about the system. The third person singular requires the -s ending: sends. The second sentence uses the past simple because the action is completed at a definite past time indicated by 'yesterday'. The verb fail is regular, so the past form is failed. This contrast between present for function and past for events is typical of technical reports.",
    "On attend present simple pour la fonction, past simple pour l'evenement date, avec les formes correctes."),
 QT("Rewrite these instructions using the imperative and modals: 'Vous devez connecter le capteur. Il est possible de régler la tension.'",
    "The instructions become: 'Connect the sensor. You can adjust the voltage.' The first sentence uses the imperative, formed with the base form of the verb, because it gives a direct instruction. If the obligation must be stressed, one can say 'You must connect the sensor' or 'The operator has to connect the sensor'. The second sentence uses the modal can to express possibility: 'You can adjust the voltage' or 'The voltage can be adjusted'. In a technical manual, imperatives give the procedure while modals state what is possible or required.",
    "On attend l'impératif pour la consigne et can / must pour la possibilite ou l'obligation.")],
C("Technical English uses the present simple for functions and the past simple for completed tests; modals state ability and obligation.",
  "Present simple: fact and function · past simple: completed event",
  "Third person -s · did not + base form · imperative for instructions · can / must",
  "Present simple~Facts and habits~sends~Past simple~Completed actions~failed~Imperative~Direct instruction~connect",
  "Identify the time reference|Choose present for a function|Choose past for a completed event|Use the imperative for procedures|Add modals for ability or obligation",
  "Forget the -s at the third person|Use did not with a past form|Mix two time references without signal words|Confuse can and must",
  "The sensor sends~Present simple~Yesterday the test failed~Past simple~Connect the sensor~Imperative~You must wear gloves~Obligation~can supply 12 V~Ability",
  "Present simple~Permanent function~Past simple~Dated event in a report",
  "Can~Possibility~Must~Obligation"))

# ============================================================ ANG2
add("ANG2", "Linking words and paragraph structure in argumentative English", "Anglais", ["1re"],
S("Linking words show the logical relationship between ideas and make a paragraph easier to follow."
  "|Addition is marked by moreover, furthermore, in addition and also."
  "|Contrast is marked by however, nevertheless, whereas and on the other hand."
  "|Cause is introduced by because, since, as and due to ; consequence by therefore, thus and as a result."
  "|Sequencing uses first, then, next, finally and eventually."
  "|Concession uses although, even though and despite ; these structures introduce a limitation before the main point."
  "|A good argumentative paragraph begins with a topic sentence stating the main idea."
  "|The supporting sentences develop the idea with reasons and concrete examples."
  "|The concluding sentence sums up the paragraph and links it to the next one."
  "|Avoid overusing connecteurs : too many linking words make the text mechanical."
  "|However is usually followed by a comma ; although introduces a subordinate clause and despite is followed by a noun or a gerund."
  "|In the STI2D written exam, a clear structure and accurate connectors are valued as much as vocabulary."),
[QC("Which connector introduces a contrast ?", "Moreover~However~Therefore~Besides", 1,
    "However signals a contrast or a restriction."),
 QC("Which connector introduces a consequence ?", "Because~Although~As a result~Whereas", 2,
    "As a result introduces a consequence ; because introduces a cause."),
 QC("What follows 'despite' ?", "A finite verb~A noun or a gerund~A whole sentence with that~Only an adjective", 1,
    "Despite is a preposition : despite the cost, despite being expensive."),
 QC("What is the role of a topic sentence ?", "To give the final answer~To state the main idea of the paragraph~To translate a word~To ask a question", 1,
    "The topic sentence announces the idea developed in the paragraph."),
 QC("Which group contains only sequencing words ?", "However, nevertheless, yet~First, then, finally~Because, since, as~Moreover, also, too", 1,
    "First, then and finally organise the order of ideas."),
 QC("How is 'however' usually punctuated ?", "Without comma always~With a comma~Between brackets~With a semi-colon only", 1,
    "However is normally followed by a comma when it opens the sentence."),
 QC("Why should linking words not be overused ?", "They are grammatically wrong~They make the text mechanical~They are too short~They change the topic", 1,
    "An excessive number of connectors makes the reasoning artificial."),
 QT("Complete the paragraph with suitable connectors and explain the choices: 'Renewable energy is growing fast. ___, its cost remains high. ___, investment continues to rise.',",
    "The first gap needs a contrast connector: 'However, its cost remains high.' The second gap introduces a consequence or a conclusion: 'Therefore, investment continues to rise' or 'As a result, investment continues to rise.' The first connector marks the opposition between growth and cost ; the second draws the consequence of the previous contrast. One could also use 'Nevertheless' in the first gap and 'Consequently' in the second, but the meaning must remain coherent: the cost is high, yet investment still increases.",
    "On attend however / nevertheless puis therefore / as a result, avec explication logique."),
 QT("Write a short argumentative paragraph about eco-design using a topic sentence, two reasons, an example and a concluding sentence.",
    "A possible paragraph is: 'Eco-design reduces the environmental impact of a product from the very first stages of its conception. First, the choice of recyclable materials limits waste at the end of life. Moreover, a modular design makes repair easier and extends the product's lifetime. For example, a lamp whose light source can be replaced separately avoids throwing away the whole device. Therefore, eco-design is not only an ecological choice but also an economic one.' The topic sentence states the idea, first and moreover introduce two reasons, for example gives a concrete case, and therefore concludes the paragraph.",
    "On verifie la presence de la these, de deux connecteurs, d'un exemple et d'une conclusion.")],
C("Linking words make reasoning visible: addition, contrast, cause, consequence and sequence must be signalled accurately.",
  "Contrast: however, although, despite · consequence: therefore, as a result",
  "Topic sentence + supporting sentences + concluding sentence",
  "Addition~Moreover, also~Adds an idea~Contrast~However, whereas~Opposes ideas~Cause~Because, since~Explains why",
  "Write a clear topic sentence|Choose the connector for each logical link|Support with reasons and an example|Check punctuation after connectors|Conclude and link to the next paragraph",
  "Confuse because and therefore|Use despite with a finite verb|Stack too many connectors|Begin a paragraph without a main idea",
  "However~Contrast with comma~Therefore~Consequence~Although~Concession clause~For example~Concrete support~In conclusion~Summary",
  "Because~Introduces a cause~Therefore~Introduces a consequence",
  "Although~Followed by a clause~Despite~Followed by a noun or gerund"))

# ============================================================ ANG3
add("ANG3", "Oral presentation and technical vocabulary in English", "Anglais", ["Terminale"],
S("An oral presentation in English has three parts: an introduction, a development and a conclusion."
  "|The introduction greets the audience, gives the title and announces the plan."
  "|Signposting phrases guide the listener : I will first present..., then I will deal with..., finally I will conclude."
  "|The development follows the announced plan, with one main idea per part and a concrete example."
  "|The conclusion summarises the main points and may open a question for discussion."
  "|Speakers should use simple and clear sentences rather than reading a written text aloud."
  "|Pronunciation of technical words matters : component, sensor, efficiency, sustainable, assembly."
  "|Key nouns in engineering include system, circuit, frame, load, output, input and prototype."
  "|Useful verbs are to design, to assemble, to measure, to test, to reduce and to improve."
  "|Adjectives such as efficient, reliable, durable and affordable describe the qualities of a product."
  "|The question-and-answer phase requires careful listening : 'I do not understand' becomes 'Could you clarify your question, please ?'"
  "|In the STI2D oral exam, clarity, interaction with the examiner and accurate vocabulary are assessed."),
[QC("What does a good introduction include ?", "Only the title~Greeting, title and plan~The conclusion~A long anecdote", 1,
    "The introduction greets, presents the subject and announces the plan."),
 QC("Which phrase is a signpost in a presentation ?", "I will first present...~It is perhaps interesting~Anyway~I think so", 0,
    "Signposting phrases announce the structure of the talk."),
 QC("Which word is a technical noun ?", "Beautiful~Sensor~Quickly~Blue", 1,
    "Sensor is a technical noun ; the others are not engineering terms."),
 QC("What should a speaker avoid ?", "Using examples~Reading a written text aloud~Signposting the plan~Using simple sentences", 1,
    "Reading aloud reduces eye contact and clarity."),
 QC("Which verb means 'améliorer' ?", "To reduce~To improve~To assemble~To measure", 1,
    "To improve means to make something better."),
 QC("How can you ask the examiner to repeat a question politely ?", "What ?~Could you clarify your question, please ?~Again ?~I do not know", 1,
    "Could you clarify your question, please ? is a polite reformulation."),
 QC("What is assessed in the STI2D oral exam ?", "Only grammar~Clarity, interaction and accurate vocabulary~The length of the answer~Handwriting", 1,
    "The exam values intelligibility, interaction and precise vocabulary."),
 QT("Draft the introduction of a three-part oral presentation about a solar-powered charging station.",
    "A suitable introduction is: 'Good morning. Today I will present a solar-powered charging station for electric bicycles. I will first describe the system and its main components, then I will explain how it is dimensioned and what its limits are, and finally I will give an example of use on a school campus.' This introduction greets the audience, states the subject clearly and announces three parts in the same order as the development. The signposting verbs I will first describe, then I will explain and finally I will give help the listener follow the presentation.",
    "On attend salutation, titre, annonce de trois parties et phrases de guidage."),
 QT("Explain how to handle a question you have not understood during an oral examination.",
    "The worst reaction is to invent an answer to a misunderstood question. One should first remain calm and use a polite reformulation: 'Could you clarify your question, please ?' or 'If I understand correctly, you are asking about...' This shows active listening and gives the examiner a chance to restate the question. One can then ask for precision on a specific term: 'Do you mean the efficiency of the system or its cost ?' After answering, it is useful to check that the answer was relevant: 'Is that what you wanted to know ?' This strategy turns a difficulty into an opportunity for interaction, which is positively assessed in the oral exam.",
    "On valorise la reformulation polie, la demande de precision et la verification de la pertinence.")],
C("A successful oral presentation is structured, signposted and interactive, with precise technical vocabulary.",
  "Introduction: greeting + title + plan · conclusion: summary + opening",
  "Signposting: I will first... then... finally... · reformulate before answering",
  "Introduction~Greeting and plan~Signposting~Guides the listener~Development~One idea per part~Conclusion~Summary and opening",
  "Prepare a three-part plan|Learn the signposting phrases|Use precise technical nouns and verbs|Speak rather than read|Reformulate questions before answering",
  "Read the whole text aloud|Announce a plan not followed|Ignore an unclear question|Overload the slides with text",
  "Sensor~Technical noun~To design~Technical verb~Efficient~Quality adjective~Could you clarify~Polite reformulation~Good morning~Greeting",
  "Signposting~Announces the plan~Example~Supports the idea",
  "To reduce~Lower a value~To improve~Make better"))

# ============================================================ HGG1
add("HGG1", "Regimes politiques et mutations democratiques", "HGGS", ["1re"],
S("Histoire, geographie, geopolitique et sciences sociales (HGGS) etudie les societes dans leur dimension politique et spatiale."
  "|Un regime politique designe la maniere dont le pouvoir est organise et exerce dans un Etat."
  "|Une democratie repose sur la souverainete du peuple, des elections libres et la protection des droits."
  "|Un regime autoritaire concentre le pouvoir, limite le pluralisme et controle les libertes publiques."
  "|Un regime totalitaire vise le contrôle de toute la societe par un parti unique et une ideologie officielle."
  "|La souverainete est le pouvoir supreme de l'Etat ; la separation des pouvoirs (legislatif, executif, judiciaire) limite l'arbitraire et garantit l'Etat de droit."
  "|L'Etat de droit soumet l'administration et les citoyens a des regles juridiques connues et applicables."
  "|Les transitions democratiques sont des processus de passage d'un regime autoritaire a un regime democratique."
  "|Les fractures democratiques designent le recul des liberte et la defiance envers les institutions."
  "|Les populisms se presentent comme la voix du peuple contre une elite designee comme corrompue."
  "|Les reseaux sociaux accelerent la circulation des opinions et peuvent amplifier la polarisation politique."
  "|Comprendre les regimes politiques aide a analyser les contextes d'implantation des projets technologiques."),
[QC("Quel critere caractérise une democratie ?", "Un parti unique~Des elections libres et la souverainete du peuple~Un chef militaire~L'absence de lois", 1,
    "La souverainete populaire et le pluralisme electoral definissent la democratie."),
 QC("Quel est un trait d'un regime totalitaire ?", "Le pluralisme~Le controle de toute la societe par un parti unique~La separation des pouvoirs~La libre expression", 1,
    "Le totalitarisme vise une emprise totale sur la societe."),
 QC("Que designe la separation des pouvoirs ?", "Un seul organe decide tout~Legislatif, executif et judiciaire sont distincts~Les lois sont supprimees~Le peuple ne vote pas", 1,
    "La separation des pouvoirs est un principe de l'Etat de droit."),
 QC("Qu'est-ce qu'une transition democratique ?", "Un coup d'Etat~Un passage d'un regime autoritaire a un regime democratique~Une guerre~Une crise economique", 1,
    "La transition est un processus, souvent progressif et incertain."),
 QC("Que designe une fracture democratique ?", "Une election~Un recul des liberte et de la confiance~Une reforme constitutionnelle~Un traite", 1,
    "Les fractures designent l'erosion des normes democratiques."),
 QC("Comment les populismes presentent-ils le peuple ?", "Comme une elite~Comme une entite opposee a une elite corrompue~Comme un parti unique~Comme une institution", 1,
    "Le populisme oppose le peuple à une elite designee comme illegitime."),
 QC("Quel effet les reseaux sociaux peuvent-ils avoir sur la politique ?", "Supprimer les elections~Amplifier la polarisation des opinions~Garantir la verite~Eliminer les debats", 1,
    "Les algorithmes peuvent renforcer les bulles et la polarisation."),
 QT("Distinguer regime autoritaire et regime totalitaire, avec un exemple historique pour chacun.",
    "Un regime autoritaire concentre le pouvoir entre les mains d'un chef ou d'un groupe, restreint le pluralisme et les libertes, mais laisse souvent subsister une societe civile et des espaces prives relativement autonomes. Le regime totalitaire, lui, vise un controle total de la societe par un parti unique, une ideologie obligatoire, une police politique et la mobilisation permanente des citoyens. Par exemple, le regime de Vichy en France (1940-1944) est autoritaire, tandis que l'URSS stalinienne dans les annees 1930 est totalitaire. La distinction tient au degre d'emprise sur la societe et a la presence ou non d'un pluralisme residuel.",
    "On oppose la limitation des libertes au controle total, avec deux exemples dates."),
 QT("Expliquer pourquoi la separation des pouvoirs est une garantie de l'Etat de droit.",
    "La separation des pouvoirs repartit les fonctions entre un parlement qui vote la loi, un gouvernement qui l'applique et une justice qui la controle. Aucun organe ne peut ainsi a la fois edicter, executer et juger ses propres decisions, ce qui limite l'arbitraire et la concentration du pouvoir. Le juge peut annuler une decision administrative illegale et le parlement peut controler l'action du gouvernement. Cette architecture est completée par des contre-pouvoirs (Cour constitutionnelle, medias, societe civile). Sans elle, la protection des droits individuels dependrait de la seule volonte du prince, ce qui caracterise precisely un regime autoritaire.",
    "On lie les trois pouvoirs, l'absence d'arbitraire et le role du juge.")],
C("Un regime politique se definit par l'organisation du pouvoir, le pluralisme et la place des droits.",
  "Democratie = souverainete du peuple + elections libres + Etat de droit",
  "Autoritaire : pouvoir concentre · totalitaire : emprise totale · transition : passage vers la democratie",
  "Democratie~Souverainete du peuple~Elections libres~Autoritarisme~Pouvoir concentre~Pluralisme limite~Etat de droit~Regles juridiques~Justice independante",
  "Definir le regime etudie|Identifier les institutions|Verifier le pluralisme et les liberte|Situer dans le temps|Comparer avec un autre cas",
  "Confondre autoritaire et totalitaire|Juger avec des categories actuelles un passe lointain|Ignorer le contexte historique|Prendre un discours officiel pour la realite",
  "1940~Regime de Vichy autoritaire~Annees 1930~URSS totalitaire~Separation~Trois pouvoirs~Populisme~Peuple contre elite~Reseaux~Polarisation",
  "Regime autoritaire~Libertes limitees~Regime totalitaire~Emprise totale sur la societe",
  "Transition~Processus vers la democratie~Fracture~Recul democratique"))

# ============================================================ HGG2
add("HGG2", "Espaces et societes : comprendre l'urbanisation", "HGGS", ["1re"],
S("L'urbanisation est la croissance de la population et des activites dans les villes."
  "|Un espace est une portion de territoire construite par les societes et les representations qu'elles en ont."
  "|La population urbaine mondiale a franchi le seuil de la majorite au debut du XXIe siecle."
  "|La metropolitanisation designe le developpement de grandes agglomerations qui concentrent fonctions et flux."
  "|Une metropole est un grand pole urbain qui rayonne bien au-dela de son peripherie administrative."
  "|La periurbanisation est l'extension de l'urbanisme en peripherie des villes, souvent en milieu rural."
  "|La gentrification correspond a l'arrivee de populations plus aisees dans des quartiers populaires, avec hausse des prix."
  "|Les mobilites quotidiennes (navettes) relient les lieux de residence, de travail et de consommation."
  "|La segregation socio-spatiale se lit dans la specialisation des quartiers selon les revenus et l'origine."
  "|Les espaces publics (places, rues, parcs) sont des lieux de rencontre et de citoyennete."
  "|La ville durable vise a reduire la consommation d'espace, d'energie et de ressources."
  "|Analyser une ville necessite de croiser des donnees de population, de revenus, d'habitat et de transports."),
[QC("Que designe la metropolitanisation ?", "La diminution des villes~Le developpement de grandes agglomerations~La creation de villages~La disparition des peripheries", 1,
    "La metropolitanisation concentre fonctions et flux dans de grandes agglomerations."),
 QC("Qu'est-ce que la periurbanisation ?", "Le depart des habitants de la ville~L'extension de l'urbanisme en peripherie~La croissance des centres historiques~La construction de routes", 1,
    "La periurbanisation etale l'habitat en dehors de la ville centre."),
 QC("Que designe la gentrification ?", "La construction de logements sociaux~L'arrivee de populations plus aisees et la hausse des prix~Le depart des entreprises~La fermeture des commerces", 1,
    "La gentrification transforme un quartier populaire sous l'effet de l'arrivee de menages plus riches."),
 QC("Quel indicateur aide a lire la segregation socio-spatiale ?", "La couleur des façades~Les revenus et l'origine des habitants par quartier~Le nombre d'arbres~La date de construction", 1,
    "La repartition des revenus et des populations révèle les specialisations de quartiers."),
 QC("Quel role jouent les espaces publics ?", "Ils sont reserves aux voitures~Ils permettent la rencontre et la citoyennete~Ils sont privés~Ils servent seulement au commerce", 1,
    "Rues, places et parcs sont des lieux de sociabilite et d'expression citoyenne."),
 QC("Qu'est-ce qu'une navette quotidienne ?", "Un deplacement residence-travail~Un voyage de loisir~Une migration définitive~Un transports de marchandises", 0,
    "La navette est un deplacement quotidien domicile-travail ou domicile-etudes."),
 QC("Que vise une ville durable ?", "Plus de consommation d'espace~Moins de ressources et d'emissions~Plus de voitures~Moins de logements", 1,
    "La ville durable limite l'étalement et reduit les consommations."),
 QT("Analyser les effets de la periurbanisation sur les mobilites et l'environnement.",
    "La periurbanisation eloigne les lieux de residence des centres d'emploi et de service, ce qui allonge les distances de navette et augmente la dependances a la voiture. Elle consomme des surfaces agricoles ou naturelles, fragmente les paysages et accroit l'impermeabilisation des sols, avec des effets sur les ecoulements et les inondations. Les infrastructures de transport et les reseaux (eau, electricite, fibre) coutent plus cher a desservir en faible densite. En revanche, elle offre des logements plus grands et une qualite de vie recherchée par les menages. Une ville durable tente de limiter ces effets par la densification, le developpement des transports collectifs et la requalification des friches.",
    "On attend les effets sur les deplacements, les sols, les reseaux et les pistes d'amenagement."),
 QT("Comment construire une analyse geographique d'une agglomeration a partir de documents varies ?",
    "On commence par lire les documents pour identifier l'objet : carte de population, donnees de revenus, plan de transports ou photographie de quartier. On releve les faits visibles (densite, répartition des activites, ecart de prix, temps de trajet), puis on les croise pour faire apparaitre des structures : centre, peripheries, axes de transport, quartiers specialises. On formule ensuite une hypothese sur les processus a l'oeuvre, par exemple la periurbanisation ou la gentrification, et on la confronte aux donnees. On termine en situant le cas dans un contexte plus large (metropolitanisation, transition ecologique) et en indiquant les limites des documents (echelle, date, source). Une bonne analyse ne se contente pas de decrire : elle explique et discute la fiabilite des sources.",
    "On valorise la lecture croisee, la formulation d'hypotheses et la critique des sources.")],
C("L'analyse d'un espace urbain croise des donnees de population, de revenus, de transports et d'habitat.",
  "Urbanisation · metropolitanisation · periurbanisation · gentrification",
  "Ville durable = moins d'etalement, moins de ressources, plus de transports collectifs",
  "Metropole~Grand pole rayonnant~Periurbanisation~Etalement en peripherie~Gentrification~Hausse des prix~Navette~Deplacement quotidien",
  "Lire les documents et leur echelle|Relever les faits et les ecarts|Croiser les donnees|Formuler une hypothese de processus|Discuter la fiabilite des sources",
  "Confondre periurbanisation et gentrification|Generaliser a partir d'un seul quartier|Ignorer la date des documents|Decrire sans expliquer",
  "Majorite urbaine~Debut du XXIe~Navettes~Distances plus longues~Impermeabilisation~Sols artificialises~Friches~Requalification~Transports collectifs~Alternative a la voiture",
  "Periurbanisation~Etalement peripherique~Gentrification~Transformation sociale d'un quartier",
  "Espace public~Rencontre et citoyennete~Espace prive~Logement et entreprise"))

# ============================================================ HGG3
add("HGG3", "Sciences sociales et developpement durable : enjeux et indicateurs", "HGGS", ["Terminale"],
S("Les sciences sociales etudient les faits sociaux et les manieres dont les societes produisent et repartissent les ressources."
  "|Le developpement durable vise a satisfaire les besoins presents sans compromettre la capacite des generations futures."
  "|La definition de reference est celle de la commission Brundtland (1987), reprise par le sommet de Rio (1992)."
  "|Les trois piliers du developpement durable sont economique, social et environnemental ; aucun ne doit etre sacrifie."
  "|Les objectifs de developpement durable (ODD) de l'Agenda 2030 de l'ONU declinent 19 objectifs."
  "|Le PIB mesure la production economique mais ne rend pas compte de la distribution des richesses ni des dommages environnementaux."
  "|L'indice de developpement humain (IDH) combine esperance de vie, niveau d'instruction et revenu par habitant."
  "|L'empreinte ecologique compare la consommation de ressources d'une population a la capacite de regeneration de la planete."
  "|Les inegalites se mesurent avec des indicateurs de revenu, d'acces a la sante, a l'education et au logement."
  "|La justice environnementale questionne la repartition inegale des pollutions et des risques entre populations."
  "|Le principe de precaution permet d'agir face a un risque grave meme si la certitude scientifique n'est pas complete."
  "|En STI2D, l'ingenieur doit articuler performance technique, cout et impact social ou environnemental."),
[QC("Qui a popularise la definition du developpement durable ?", "Le sommet de Rio 1992~La commission Brundtland en 1987~L'ONU en 1945~L'OMC en 1995", 1,
    "Le rapport Brundtland (1987) donne la definition de reference, reprise a Rio."),
 QC("Combien de piliers compte le developpement durable ?", "Deux~Trois~Quatre~Cinq", 1,
    "Les piliers economique, social et environnemental sont au nombre de trois."),
 QC("Que mesure l'IDH ?", "La seule production industrielle~Esperance de vie, instruction et revenu~Le nombre d'habitants~La pollution de l'air", 1,
    "L'indice de developpement humain combine trois dimensions."),
 QC("Que révèle l'empreinte ecologique ?", "Le cout d'un produit~La surface necessaire pour subvenir aux besoins~Le nombre d'emplois~Le taux de croissance", 1,
    "L'empreinte compare la consommation de ressources a la biocapacite."),
 QC("Quel est un limite du PIB ?", "Il est trop precis~Il ignore la distribution et les dommages environnementaux~Il ne peut pas etre calcule~Il compte seulement les services", 1,
    "Le PIB est un agrégat de production, pas un indicateur de bien-etre ou de durabilite."),
 QC("Que designe la justice environnementale ?", "Une regle de commerce~Une repartition equitable des risques et des pollutions~Une taxe~Un label", 1,
    "La justice environnementale porte sur l'equite de l'exposition aux risques."),
 QC("Quand s'applique le principe de precaution ?", "Quand le risque est certain~Face a un risque grave malgre une incertitude scientifique~Uniquement apres un accident~Jamais", 1,
    "La precaution permet d'agir avant la preuve scientifique complete."),
 QT("Expliquer pourquoi le developpement durable ne peut pas se limiter a la protection de l'environnement.",
    "Le developpement durable exige de concilier trois dimensions. Une politique uniquement environnementale peut etre socialement injuste, par exemple si elle supprime des emplois sans proposer de reconversion ou si elle rend des biens essentiels inaccessibles. Une politique uniquement economique epuise les ressources et reporte les couts sur les generations futures. La pauvrete elle-meme est une cause de degradation environnementale, car elle pousse a surexploiter les ressources locales pour survivre. La definition de Brundtland lie explicitement les besoins presents et la capacite des generations futures, ce qui impose d'evaluer ensemble les effets economiques, sociaux et ecologiques d'une decision technique.",
    "On articule les trois piliers et on montre comment l'absence d'un pilier affaiblit les autres."),
 QT("Comment un ingenieur STI2D peut-il integrer le developpement durable dans la conception d'un produit ?",
    "Il peut d'abord realiser une analyse du cycle de vie, de l'extraction des matieres premieres a la fin de vie, pour identifier les phases les plus consommatrices. Il privilege ensuite l'eco-conception : choix de materiaux recyclables ou renouvelables, reduction de la matiere, modularite pour faciliter la reparation, consommation energetique reduite en usage. Il evalue le cout total sur la duree de vie plutot que le seul prix d'achat, et verifie les conditions sociales de fabrication. Il s'appuie sur des indicateurs (empreinte carbone, consommation d'eau, taux de recyclabilite) et sur le principe de precaution pour les substances douteuses. Enfin, il documente ses choix afin que le gain environnemental soit verifiable et non seulement declare.",
    "On attend cycle de vie, eco-conception, indicateurs, cout global et traçabilité des choix.")],
C("Le developpement durable articule efficacite economique, equite sociale et preservation de l'environnement.",
  "Brundtland 1987 : besoins presents sans compromettre les generations futures",
  "3 piliers · 17 ODD de l'Agenda 2030 · PIB, IDH, empreinte ecologique",
  "Developpement durable~Trois piliers~Equilibre des dimensions~IDH~Sante, instruction, revenu~Empreinte~Biocapacite~Precaution~Agir malgre l'incertitude",
  "Definir le besoin et ses limites|Mesurer les impacts avec des indicateurs|Arbitrer entre les trois piliers|Appliquer l'eco-conception|Documenter et verifier les choix",
  "Reduire le durable au recyclage|Croire que le PIB mesure le bien-etre|Ignorer les effets sociaux d'un choix technique|Appliquer la precaution apres le dommage",
  "1987~Rapport Brundtland~1992~Sommet de Rio~17 ODD~Agenda 2030~IDH~Trois dimensions~Empreinte ecologique~Biocapacite",
  "PIB~Production economique~IDH~Developpement humain",
  "Precaution~Anticiper le risque~Prevention~Eviter le dommage connu"))

# ============================================================ EMC1
add("EMC1", "La laicite et les libertes dans la Republique", "EMC", ["1re"],
S("L'enseignement moral et civique (EMC) vise a former des citoyens responsables et a transmettre les valeurs de la Republique."
  "|Les valeurs de la Republique sont la liberte, l'egalite, la fraternite, la laicite et le respect de la dignite humaine."
  "|La laicite repose sur la separation des Eglises et de l'Etat, proclamee par la loi de 1905."
  "|Elle garantit la liberte de conscience et l'egalite de tous devant la loi, quelle que soit la religion."
  "|L'Etat ne reconnait aucun culte officiel et ne subventionne pas les religions, sauf exceptions encadrees."
  "|La laicite de l'Etat n'implique pas la neutralite des citoyens, mais celle des agents publics dans l'exercice de leurs fonctions."
  "|Les signes religieux sont interdits aux agents publics dans le service, dans le respect de leur liberte de conscience privee."
  "|A l'ecole publique, les eleves ne portent pas de signes ou tenues manifestant une appartenance religieuse."
  "|La liberte d'expression est un droit fondamental, limite par le respect d'autrui, l'ordre public et la loi."
  "|La diffamation, l'injure et la provocation a la haine sont des abus de la liberte d'expression reprime par la loi."
  "|Le principe d'egalite interdit les discriminations fondees sur la religion, le sexe, l'origine ou le handicap."
  "|Les debats citoyens permettent de confronter des opinions et de construire une decision collective respectueuse des droits."),
[QC("Quelle loi fonde la separation des Eglises et de l'Etat en France ?", "La loi de 1882~La loi de 1905~La loi de 1958~La loi de 2004", 1,
    "La loi du 9 decembre 1905 pose le principe de laicite."),
 QC("Que garantit la laicite ?", "Une religion officielle~La liberte de conscience et l'egalite devant la loi~Le financement des cultes~L'interdiction de toute religion", 1,
    "Elle protege la liberte de croire ou de ne pas croire et l'egalite de tous."),
 QC("A qui s'impose la neutralite dans le service public ?", "A tous les citoyens~Aux agents publics dans l'exercice de leurs fonctions~Aux seuls enseignants~Aux eleves hors de l'ecole", 1,
    "Les agents publics sont tenus a la neutralite, pas les usagers."),
 QC("Quel est un abus de la liberte d'expression ?", "Une opinion critique~La provocation a la haine~Un debat contradictoire~Une question au professeur", 1,
    "L'incitation a la haine n'est pas protegee par la liberte d'expression."),
 QC("Quel principe interdit les discriminations ?", "La liberte d'entreprendre~Le principe d'egalite~Le principe de realite~La souverainete", 1,
    "L'egalite devant la loi s'oppose a toute discrimination."),
 QC("Dans quel cadre les debats citoyens doivent-ils se derouler ?", "Sans regles~Dans le respect des droits et de la dignite~Avec un seul orateur~En excluant les opinions contraires", 1,
    "Un debat democratique respecte la dignite et les droits de chacun."),
 QC("Subventionner un culte est-il compatible avec la laicite ?", "Toujours~Non, en principe~Seulement pour la religion majoritaire~Oui, sans limite", 1,
    "La loi de 1905 interdit en principe le financement public des cultes."),
 QT("Expliquer la difference entre la neutralite de l'Etat et la liberte de conscience des citoyens.",
    "La neutralite s'impose a l'Etat et a ses agents : ils ne doivent ni favoriser ni combattre une religion, et les agents publics s'abstiennent de tout signe d'appartenance religieuse dans l'exercice de leur fonction. La liberte de conscience, elle, appartient a chaque personne : elle peut croire ou ne pas croire, changer de religion ou n'en avoir aucune, et exprimer ses convictions dans la vie privee et dans l'espace public dans le respect de la loi. La laicite ne supprime donc pas la religion de la societe ; elle empeche que l'Etat s'identifie a un culte et garantit a chacun une egalite reelle. Cette distinction evite deux confusions : croire que la laicite interdit la foi, ou croire que les citoyens doivent etre neutres comme l'Etat.",
    "On distingue l'obligation des agents publics et le droit des citoyens, avec exemples."),
 QT("Un debat de classe porte sur le port de signes religieux. Comment organiser le debat dans le respect de l'EMC ?",
    "On commence par rappeler le cadre legal : la neutralite des agents publics, l'interdiction des signes manifestant une appartenance religieuse pour les eleves dans les ecoles publiques, et la liberte de conscience de chacun. On distribue la parole de maniere equitable, on exige des argumentations plutot que des affirmations d'autorite, et on interdit toute attaque contre une personne ou un groupe. On distingue les faits juridiques, les opinions morales et les emotions. Le professeur veille a ce que les minorites ne soient pas mises en minorite par le nombre et reformule les propos ambigus. On termine par une synthese qui fait apparaitre les points d'accord, les desaccords et ce que la loi permet ou interdit, sans conclure que l'une des convictions est superieure a une autre.",
    "On attend le rappel du droit, l'equite de parole, le respect des personnes et une synthese nuancee.")],
C("La laicite protectrice de la liberte de conscience repose sur la neutralite de l'Etat et l'egalite de tous devant la loi.",
  "Loi du 9 decembre 1905 : separation des Eglises et de l'Etat",
  "Neutralite des agents publics · liberte de conscience des citoyens · egalite et respect de la dignite",
  "Laicite~Separation et egalite~Loi 1905~Neutralite~Agents publics~Liberte de conscience~Droit de croire ou non~Egalite~Interdiction des discriminations",
  "Rappeler le cadre juridique|Definir les notions|Respecter la parole de chacun|Argumenter sans attaquer les personnes|Construire une synthese",
  "Confondre neutralite de l'Etat et liberte des citoyens|Considerer une religion comme hostile a la Republique|Croire que la laicite interdit la foi|Laisser le debat devenir une polémique",
  "1905~Loi de separation~2004~Signes a l'ecole~Agents publics~Neutralite~Citoyens~Liberte de conscience~Egalite~Respect de la dignite",
  "Neutralite de l'Etat~Aucun culte officiel~Liberte de conscience~Conviction personnelle protegee",
  "Liberte d'expression~Droit limite par la loi~Abus~Injure et provocation a la haine"))

# ============================================================ EMC2
add("EMC2", "Citoyennete, engagement et institutions europeennes", "EMC", ["1re"],
S("La citoyennete est une condition juridique et politique qui donne des droits et des devoirs dans une communaute."
  "|En France, la citoyennete s'acquiert par la naissance ou par naturalisation et ouvre le droit de vote."
  "|Les droits politiques (vote, eligibilite) s'accompagnent de devoirs : respect de la loi, impots, service national."
  "|La participation citoyenne prend de nombreuses formes : vote, debat, petition, association, syndicat et consultation."
  "|L'abstention designe le non-vote ; elle peut traduire une defiance ou un desinteret pour la chose publique."
  "|L'engagement associatif permet d'agir sur des problemes locaux et de developper la solidarite."
  "|Le beneficat est une forme d'engagement individuel au service d'une cause ou d'une personne."
  "|La laicite, l'egalite et la fraternite sont des valeurs qui fondent le vivre-ensemble."
  "|L'Union europeenne est une organisation d'Etats qui dispose d'institutions propres et d'un droit commun."
  "|Les institutions europeennes principales sont la Commission, le Parlement, le Conseil et la Cour de justice."
  "|La Commission prepare et applique les politiques ; le Parlement represente les citoyens et vote le budget."
  "|Les elections europeennes permettent aux citoyens de choisir leurs representants au Parlement europeen tous les cinq ans."),
[QC("Comment acquiert-on la nationalite francaise ?", "Uniquement par la naissance~Par la naissance ou la naturalisation~Par le vote~Par le travail", 1,
    "La nationalite s'acquiert par filiation, naissance en France ou naturalisation."),
 QC("Quel est un devoir du citoyen ?", "Voter obligatoirement~Respecter la loi et payer les impots~S'abriculer au vote~Exprimer une opinion", 1,
    "Le respect de la loi et l'impot sont des devoirs civiques."),
 QC("Que designe l'abstention ?", "Un vote blanc~Le non-vote~Une petition~Une manifestation", 1,
    "L'abstention est l'absence de participation au vote."),
 QC("Quelle institution prepare les politiques de l'Union europeenne ?", "La Cour de justice~La Commission europeenne~Le Parlement~La Banque centrale", 1,
    "La Commission a le monopole de l'initiative legislative et met en oeuvre les politiques."),
 QC("Qui represente directement les citoyens europeens ?", "La Commission~Le Parlement europeen~Le Conseil~La Cour des comptes", 1,
    "Le Parlement europeen est elu au suffrage universel direct."),
 QC("Quelle est la duree d'un mandat au Parlement europeen ?", "Deux ans~Cinq ans~Sept ans~Dix ans", 1,
    "Les elections europeennes ont lieu tous les cinq ans."),
 QC("Quel est un effet de l'engagement associatif ?", "Supprimer les droits~Agir localement et developper la solidarite~Remplacer les lois~Interdire le debat", 1,
    "Les associations sont des lieux de participation et de solidarite."),
 QT("Distinguer les droits politiques et les droits sociaux, puis montrer comment ils se completent.",
    "Les droits politiques sont ceux qui permettent de participer a la vie de la cite : droit de vote, eligibilite, liberte d'expression et d'association. Les droits sociaux garantissent des conditions de vie dignes : acces a l'education, a la sante, au travail, a la protection sociale et au logement. Ils se completent parce qu'un citoyen prive d'instruction ou de ressources ne peut pas reellement exercer ses droits politiques, et parce qu'une societe qui ne garantit pas les droits sociaux produit des citoyens exclus de la participation. La Declaration universelle des droits de l'homme et la Constitution de 1958 affirment ensemble ces deux familles de droits. La citoyennete reelle exige donc a la fois des droits d'action politique et des conditions sociales d'exercice.",
    "On définit les deux familles de droits et on explique leur complementarite."),
 QT("Expliquer le role du Parlement europeen et pourquoi son election directe est importante.",
    "Le Parlement europeen represente les citoyens des Etats membres. Il discute et vote les textes legislatives avec le Conseil, il vote le budget de l'Union et il controle la Commission, qu'il peut mettre en cause. Il compte plus de 700 deputes elus tous les cinq ans au suffrage universel direct. Cette election directe est importante parce qu'elle donne une expression electorale aux citoyens au niveau europeen, au-dela de leur vote national : elle rend les decisions europeennes plus legitimement devoilables et elle permet aux electeurs de sanctionner ou de soutenir les orientations politiques europeennes. Elle ne remplace pas le vote national mais s'y ajoute, car les decisions de l'Union concernent des domaines comme l'environnement, l'energie ou la protection des donnees.",
    "On cite les pouvoirs du Parlement, le rythme elections et la legitimite democratique.")],
C("La citoyennete combine des droits, des devoirs et des modes de participation, y compris au niveau europeen.",
  "Droits politiques + droits sociaux = citoyennete reelle",
  "UE : Commission, Parlement, Conseil, Cour de justice · elections tous les cinq ans",
  "Citoyennete~Droits et devoirs~Nationalite~Lien juridique~Vote~Droit politique~Participation~Association et petition~Union europeenne~Institutions communes",
  "Identifier les droits et devoirs en jeu|Choisir un mode de participation|Respecter les regles du debat|S'informer sur les institutions|Agir a son echelle",
  "Confondre citoyennete et nationalite|Croire que l'abstention est sans consequence|Ignorer les droits sociaux|Prendre la Commission pour un parlement",
  "1958~Constitution de la Ve Republique~Cinq ans~Mandat europeen~Commission~Initiative legislative~Parlement~Representant des citoyens~Abstention~Non-vote",
  "Droits politiques~Vote et eligibilite~Droits sociaux~Sante, education, travail",
  "Commission~Prepare et applique~Parlement~Represente et vote"))

# ============================================================ MTH4
add("MTH4", "Trigonometrie et geometrie dans l'espace : calculer un objet technique", "Maths", ["1re"],
S("La trigonometrie relie les angles d'un triangle rectangle aux rapports entre ses cotes."
  "|Dans un triangle rectangle, cos(alpha) = cote adjacente / hypotenuse, sin(alpha) = cote opposee / hypotenuse et tan(alpha) = cote opposee / cote adjacente."
  "|Le theoreme de Pythagore s'ecrit BC² = AB² + AC² dans un triangle rectangle en A, BC etant l'hypotenuse."
  "|La reciproque de Pythagore permet de reconnaitre un triangle rectangle en comparant le carre du plus grand cote a la somme des carres des deux autres."
  "|Les angles se mesurent en degres ou en radians, avec la relation 180 degrés = pi radians."
  "|Pour un angle aigu, le sinus et le cosinus sont compris entre 0 et 1 ; le sinus croit et le cosinus decroit."
  "|La relation sin²(alpha) + cos²(alpha) = 1 decore directement du theoreme de Pythagore."
  "|Dans l'espace muni d'un repere orthonormal, la distance entre deux points vaut la racine de la somme des carres des ecarts de coordonnees."
  "|Le volume d'un cylindre de rayon r et de hauteur h vaut V = pi × r² × h ; celui d'une sphere de rayon R vaut 4/3 × pi × R³."
  "|Une section plane est l'intersection d'un solide avec un plan : elle donne une figure plane dont on peut calculer l'aire."
  "|Les projections (vue de face, de dessus, de cote) et la perspective cavaliere permettent de representer un objet a trois dimensions sur un plan."
  "|Ces outils servent a calculer une longueur, un angle ou un volume a partir d'un plan de conception ou d'un relevé de chantier."),
[QC("Que vaut cos(alpha) dans un triangle rectangle ?", "Cote opposee / hypotenuse~Cote adjacente / hypotenuse~Hypotenuse / cote adjacente~Cote opposee / cote adjacente", 1,
    "Le cosinus est le rapport de la cote adjacente a l'hypotenuse."),
 QC("Quelle relation relie les cotes d'un triangle rectangle en A ?", "BC² = AB² − AC²~BC² = AB² + AC²~BC = AB + AC~AB² = BC² + AC²", 1,
    "Pythagore : l'hypotenuse BC verifie BC² = AB² + AC²."),
 QC("Combien de radians valent 180 degrés ?", "1~pi/2~pi~2pi", 2,
    "Un demi-tour correspond a pi radians."),
 QC("Que vaut sin²(alpha) + cos²(alpha) ?", "0~1~2~Cela depend de alpha", 1,
    "Cette identite est une consequence de Pythagore."),
 QC("Quel est le volume d'un cylindre ?", "pi × r × h~pi × r² × h~2 × pi × r × h~4/3 × pi × r³", 1,
    "Le volume est l'aire de la base multipliee par la hauteur."),
 QC("Qu'appelle-t-on section plane ?", "Une projection~L'intersection d'un solide et d'un plan~Une perspective~Une arete", 1,
    "La section donne la figure d'intersection entre le solide et un plan."),
 QC("Comment obtenir la vue de dessus d'un objet ?", "En le projetant sur un plan horizontal~En le coupant~En le tournant de 90 degres~En le mesurant", 0,
    "La vue de dessus est une projection orthogonale sur un plan horizontal."),
 QT("Un triangle rectangle a une hypoténuse de 10 cm et un cote adjacent de 8 cm. Calculer l'angle.alpha et le cote oppose.",
    "On a cos(alpha) = 8/10 = 0,8, donc alpha = arccos(0,8) environ 36,9 degres. Le cote oppose se calcule par Pythagore : oppose² = 10² − 8² = 100 − 64 = 36, donc le cote oppose vaut 6 cm. On verifie avec le sinus : sin(alpha) = 6/10 = 0,6 et sin² + cos² = 0,36 + 0,64 = 1. Les resultats sont coherents : le cote oppose est plus court que le cote adjacent, ce qui correspond a un angle alpha inferieur a 45 degres.",
    "On attend le calcul du cosinus, de l'angle, du cote oppose par Pythagore et la verification."),
 QT("Expliquer comment passer d'un plan de conception 2D a la determination d'un volume 3D, avec l'exemple d'un réservoir cylindrique.",
    "On lit d'abord les cotes sur les vues du plan : diametre du reservoir et hauteur, en verifiant les echelles et les units. On deduit le rayon r = diametre/2. On identifie la forme du solide, ici un cylindre, puis on choisit la formule de volume V = pi × r² × h. On convertit toutes les longueurs dans la meme unite avant le calcul, puis on exprime le resultat en litres en utilisant 1 litre = 1000 cm³. On controle enfin l'ordre de grandeur et on tient compte de l'epaisseur des parois si le plan donne les dimensions externes : le volume utile est alors calcule avec le rayon interne. Cette demarche illustre le lien entre lecture de plan, geometrie et metrologie.",
    "On attend lecture des cotes, choix de la formule, conversion d'unites et prise en compte des parois.")],
C("Trigonometrie et geometrie dans l'espace permettent de passer d'un plan a des longueurs, angles et volumes reels.",
  "cos = adjacent/hypotenuse · sin = oppose/hypotenuse · tan = oppose/adjacent",
  "Pythagore · sin²+cos²=1 · V cylindre = pi r² h · distance = racine des carres d'ecarts",
  "Sinus~Cote oppose sur hypotenuse~Cosinus~Cote adjacent sur hypotenuse~Tangente~Oppose sur adjacent~Pythagore~Carre de l'hypotenuse",
  "Lire les cotes du plan|Repérer le triangle rectangle|Choisir sinus, cosinus ou tangente|Calculer et convertir les unites|Verifier par une autre relation",
  "Confondre cote adjacent et cote oppose|Oublier de convertir les unites|Utiliser le diametre a la place du rayon|Melanger degres et radians",
  "Hypotenuse 10 et adjacent 8~cote oppose 6 cm~alpha environ 36,9 degres~Cylindre~V = pi r² h~1 litre~1000 cm³~180 degres~pi radians",
  "Degres~Mesure d'angle usuelle~Radians~Mesure liee au rayon",
  "Section plane~Intersection avec un plan~Projection~Representation sur une vue"))

valider_et_ecrire(F, "sti2d-mat-part-A.json")
