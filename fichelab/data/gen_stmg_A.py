# -*- coding: utf-8 -*-
"""Generateur stmg-mat-part-A.json — lot A : tronc commun (20 fiches).

Filiere STMG (lycee technologique). Chaque fiche respecte le modele prototype :
12 points de cours, 9 questions corrigees (7 QCM + 2 texte),
7 blocs en ordre strict (intro, formule, grille, liste, etapes, attention, exemples),
3 schemas SVG produits par les helpers de fixtures.py.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_etapes,
                      svg_compare, bloc, valider_et_ecrire)

FIL = ["stmg"]
REF = (
    "Programmes d'enseignement de la serie STMG : arrete du 17 juillet 2018 fixant les "
    "programmes des classes de seconde, premiere et terminale technologiques (BO special "
    "n° 1 du 22 janvier 2019), ajustements publies au BO en 2020, ressources et documents "
    "d'accompagnement eduscol (eduscol.education.fr) et documents officiels du "
    "baccalaureat technologique."
)


def S(texte):
    """Decoupe une ligne compacte en points (separateur |)."""
    return [x.strip() for x in texte.split("|") if x.strip()]


def R(texte):
    """Decoupe une ligne compacte en cellules (separateur ~)."""
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
        bloc("En situation : exemples", items=[
            '%s : <span class="cle">%s</span>' % (p[0], p[1]) for p in c["ex"]
        ], type="exemples"),
    ]
    schema = [
        diag("1 · " + short, svg_grille(short, ["Notion", "Definition", "Repere"],
                                        c["grid"])),
        diag("2 · Demarche", svg_etapes("Procedure : " + short, c["steps"])),
        diag("3 · A distinguer", svg_compare(short, c["cmp"][0], c["cmp"][1])),
    ]
    assert len(points) == 12, "12 points attendus pour " + prefix
    assert len(questions) == 9, "9 questions attendues pour " + prefix
    assert sum(1 for q in questions if q.get("type") == "qcm") == 7, prefix
    assert sum(1 for q in questions if q.get("type") == "texte") == 2, prefix
    assert len(aff) == 7 and len(schema) == 3, prefix
    return fiche(FIL, annees, matiere, titre_complet, REF, points, questions,
                 aff, schema)


F = []


# ============================================================ A01
add = lambda *a: F.append(build(*a))

add("A01", "Les figures de style et leurs effets", "Français", ["1re", "Terminale"],
S("Une figure de style est une manipulation volontaire de la langue qui produit un effet de sens ou d'image.|"
  "La comparaison etablit un rapprochement explicite entre deux elements grace a un outil : comme, tel, semblable a.|"
  "La metaphore transposer un terme sans outil de comparaison : elle dit une chose en termes d'une autre.|"
  "La personnification attribue des actions ou des sentiments humains a un etre inanime ou a un animal.|"
  "L'hyperbole exagere volontairement une realite pour renforcer l'expression.|"
  "L'euphemisme attenue une realite brutale pour la rendre plus acceptable.|"
  "L'antithese oppose deux termes ou deux idees dans une meme phrase pour souligner un contraste.|"
  "L'oxymore associe deux mots contradictoires pour creer une image forte, par exemple une claire obscurite.|"
  "La repetition, et notamment l'anaphore en debut de phrase, insiste sur un mot et rythme le texte.|"
  "Le chiasme croise deux structures en A-B puis B-A, ce qui equilibre et rend une idee memorable.|"
  "L'alliteration repete une meme consonne pour produire un effet sonore, par exemple les r roulants.|"
  "On identifie une figure par sa forme, puis on l'interprete par son effet sur le lecteur et par l'intention de l'auteur."),
[QC("Quel outil caracterise la comparaison ?", "Comme~Sans outil~Par~Avec", 0,
     "La comparaison utilise un outil explicite comme comme, tel, semblable a."),
 QC("La phrase le vent hurle illustre quelle figure ?", "Comparaison~Personnification~Antithese~Euphemisme", 1,
     "On attribue une action humaine, hurler, au vent : c'est une personnification."),
 QC("Quelle difference oppose metaphore et comparaison ?", "La metaphore n'a pas d'outil de comparaison~La metaphore est toujours courte~La comparaison n'a pas de sens~Aucune difference", 0,
     "La comparaison est explicite avec un outil ; la metaphore est une transposition directe."),
 QC("L'expression une claire obscurite est un ...", "Oxymore~Euphemisme~Chiasme~Hyperbole", 0,
     "Deux termes contradictoires sont associes : c'est un oxymore."),
 QC("L'anaphore est une repetition ...", "En fin de phrase~En debut de phrase~Au milieu du texte~De voyelles", 1,
     "L'anaphore repete un meme mot en debut de phrases successives."),
 QC("Je vous hais, je vous aime illustre ...", "Antithese~Comparaison~Alliteration~Metaphore", 0,
     "Les deux verbes s'opposent : c'est une antithese."),
 QC("Quel est l'effet principal d'une hyperbole ?", "Attenuer~Exagerer pour renforcer~Repeter un son~Croiser des termes", 1,
     "L'hyperbole exagere volontairement pour frapper le lecteur."),
 QT("Identifier et commenter la figure dans la phrase : tes yeux sont deux etoiles.",
    "Il n'y a pas d'outil de comparaison comme comme ou tel : le verbe etre ne compte pas comme outil. La phrase rapproche directement les yeux des etoiles, c'est donc une metaphore. Elle suggere la lumiere, la brillance et la beaute du regard. L'effet est poetique et flatteur : le lecteur voit le visage comme un ciel etoilé, ce qui idealise la personne decrite.",
    "On doit nommer la metaphore, justifier l'absence d'outil de comparaison, puis decrire l'effet d'idealisation"),
 QT("Decrire la demarche pour analyser une figure de style dans un commentaire litteraire.",
    "On releve d'abord la figure en citant exactement le passage. On la nomme ensuite en precisant sa forme : outil de comparaison, opposition, repetition, exageration. On explique alors le mecanisme, c'est-a-dire comment la figure fonctionne dans la phrase. On interprete enfin l'effet produit sur le lecteur et on le relie au sens general du texte et a l'intention de l'auteur. Nommer la figure ne suffit jamais : c'est l'interpretation qui apporte des points.",
    "La demarche attendue est : citer, nommer, decrire le mecanisme, interpreter l'effet, relier au texte.")],
C("Une figure de style est un ecart volontaire de la langue : on l'identifie par sa forme, puis on explique son effet.",
  "Figure = ecart de langue + effet de sens",
  "Comparaison avec outil · metaphore sans outil · personnification avec trait humain",
  "Comparaison~Rapprochement explicite~Outil : comme, tel~Metaphore~Transposition directe~Dit autrement~Personnification~Donne des traits humains~Le vent hurle",
  "Repérer l'ecart dans la phrase|Citer le passage et nommer la figure|Decrire le mecanisme de la figure|Interpreter l'effet sur le lecteur|Relier l'effet au sens du texte",
  "Nommer la figure sans l'analyser|Confondre comparaison et metaphore|Citer sans expliquer l'effet|Inventer une figure absente du texte",
  "Tes yeux sont deux etoiles~Metaphore : lumiere et beaute~Le vent hurle~Personnification : violence du vent~Je vous hais, je vous aime~Antithese : sentiments contradictoires~Une claire obscurite~Oxymore : image paradoxale~Il pleure dans mon coeur~Personnification : tristesse interieure",
  "Comparaison~Avec un outil (comme)~Rapprochement explicite~Effet plus clair~Metaphore~Sans outil de comparaison~Transposition directe~Effet plus dense",
  "Hyperbole~Exagere volontairement~Renforce l'expression~Effet comique ou dramatique~Euphemisme~Attenue la realite~Rend une idee acceptable~Effet de tact ou d'ironie"))


# ============================================================ A02
add("A02", "L'argumentation : these, arguments et exemples", "Français", ["1re"],
S("Un texte argumentatif vise a convaincre ou a persuader un lecteur d'une these.|"
  "La these est l'opinion defenseue ; la these opposee est l'antithese.|"
  "Un argument est une raison generale qui justifie la these ; il s'appuie sur une valeur ou un fait.|"
  "Un exemple est un cas concret qui illustre et rend l'argument credible.|"
  "On distingue les arguments logiques (faits, statistiques, causalite) des arguments pathos (emotion).|"
  "L'ethos designe l'image de soi que l'auteur construit pour gagner la confiance.|"
  "Le plan dialectique presente d'abord les objections (these opposee) avant de les refuter.|"
  "Un connecteur logique : or, donc, car, en effet, cependant, structure le raisonnement.|"
  "La problematique est la question centrale a laquelle le texte tente de repondre.|"
  "Une proposition de transition assure le passage entre deux parties du raisonnement.|"
  "La conclusion reprend la these sous forme de reponse a la problematique et peut ouvrir une perspective.|"
  "La qualite d'un texte argumentatif tient a la clarte de la these, a la pertinence des arguments et a la variete des exemples."),
[QC("Qu'appelle-t-on these dans un texte argumentatif ?", "L'opinion defenseue~Un exemple concret~Un connecteur~La conclusion", 0,
     "La these est l'idee ou l'opinion que l'auteur cherche a faire admettre."),
 QC("Un exemple concreta sert principalement a ...", "Remplacer la these~Illustrer et appuyer un argument~Fermer le texte~Creer une transition", 1,
     "L'exemple rend l'argument plus credible en l'incarnant dans un cas precis."),
 QC("Quel connecteur introduit une opposition ?", "Donc~En effet~Cependant~Ainsi", 2,
     "Cependant marque une opposition ou une concession ; donc et ainsi marquent la consequence."),
 QC("Le plan dialectique commence par ...", "La conclusion~L'antithese et les objections~Les exemples~La citation", 1,
     "On presente d'abord les arguments opposes, puis on les refute avant d'affirmer sa these."),
 QC("Qu'est-ce que l'ethos ?", "L'emotion du lecteur~L'image de l'auteur~La these opposee~Le plan du texte", 1,
     "L'ethos est l'image que le locuteur donne de lui-meme pour etre cru."),
 QC("Une statistique est un argument de type ...", "Pathos~Ethos~Logos~Lyrique", 2,
     "Le logos s'appuie sur la raison, les faits et les chiffres."),
 QC("Que doit faire la conclusion d'un texte argumentatif ?", "Introduire un nouvel argument~Repondre a la problematique~Supprimer les exemples~Changer de these", 1,
     "La conclusion reprend la these en repondant a la question posee."),
 QT("Distinguer these, argument et exemple dans un court developpement sur le travail.",
    "La these est l'affirmation generale : le travail est une valeur essentielle de la vie sociale. L'argument est la raison qui la justifie : le travail permet a chacun de participer a la production collective et d'acquerir une autonomie economique. L'exemple est un cas concret : un eleve de STMG qui effectue un stage en entreprise decouvre les relations entre les services et comprend l'utilite de ses apprentissages. L'argument explique pourquoi la these est vraie ; l'exemple montre qu'elle se verifie dans une situation reelle.",
    "On attend une these general, une raison qui la fonde et un cas concret, avec la fonction de chacun."),
 QT("Comment construire un paragraphe argumentatif clair ?",
    "On annonce d'abord l'argument principal en une phrase courte. On l'explique ensuite en etablissant un lien de causalite ou de consequence avec la these. On appuie alors l'affirmation sur un exemple precis, tire de l'actualite, de l'histoire ou de l'experience. On termine par une phrase de synthese qui relie le paragraphe a la these et annonce le suivant grace a un connecteur. Un bon paragraphe ne melange pas deux arguments differents et reste centre sur une seule idee.",
    "Structure attendue : annonce de l'argument, explication, exemple, synthese et transition.")],
C("Un texte argumentatif avance une these, la justifie par des arguments et la rend credible par des exemples.",
  "These + arguments + exemples = raisonnement convaincant",
  "Logos : faits et raisons · pathos : emotion · ethos : image de l'auteur",
  "These~Opinion defenseue~Reponse a la question~Argument~Raison generale~Fonde la these~Exemple~Cas concret~Rend credible",
  "Poser la problematique|Enoncer la these et les objections|Choisir des arguments pertinents|Appuyer chaque argument par un exemple|Conclure en repondant a la question",
  "Confondre argument et exemple|Avancer une these sans la justifier|Entasser des exemples sans les analyser|Oublier de repondre a la problematique",
  "Le travail~Valeur essentielle~Autonomie~Raison economique~Stage en entreprise~Exemple concret~Statistique d'emploi~Argument logos~Temoignage~Argument pathos",
  "These~Idee defendue par l'auteur~Antithese~Idee opposee~Objection~Argument adverse~Refutation~Reponse a l'objection",
  "Logos~Raison et faits~Pathos~Emotion du lecteur~Ethos~Confiance dans l'auteur~Connecteur~Lien logique"))


# ============================================================ A03
add("A03", "Le commentaire litteraire : axe de lecture et paragraphe", "Français", ["Terminale"],
S("Le commentaire litteraire est un exercice qui explique un texte en suivant un plan construit.|"
  "On distingue le commentaire compose, organise par themes, du commentaire lineaire qui suit l'ordre du texte.|"
  "La lecture attentive releve le genre, le theme, le registre et les procedures d'ecriture.|"
  "L'introduction presente l'auteur, l'oeuvre, le contexte et l'extrait, puis annonce le plan.|"
  "La problematique est une question qui met en relation deux aspects du texte.|"
  "Un axe de lecture est une grande partie du plan : il porte un titre clair, pas une simple citation.|"
  "Chaque axe se decompose en deux ou trois sous-parties, chacune centre sur une seule idee.|"
  "Le paragraphe argumentatif suit le schema assertion, preuve, analyse, synthese.|"
  "La citation doit etre courte, exacte, introduite et analysee : on ne laisse jamais une citation sans commentaire.|"
  "Les connecteurs logiques rendent visible le raisonnement : d'abord, ensuite, en revanche, ainsi.|"
  "La conclusion repond a la problematique et peut ouvrir sur une autre oeuvre ou une question plus large.|"
  "Un bon commentaire equilibre l'analyse des formes et l'interpretation des sens."),
[QC("Un commentaire compose suit ...", "L'ordre du texte~Un plan thematique~La chronologie de l'auteur~Le hasard", 1,
     "Le commentaire compose regroupe les observations en axes theoriques plutot que de suivre le texte."),
 QC("Une citation doit etre ...", "Longue et non expliquee~Courte, exacte et analysee~Inventee~Reservee a la conclusion", 1,
     "On cite peu, exactement, et on commente toujours la citation."),
 QC("Un axe de lecture est ...", "Une grande partie du plan~Une phrase du texte~Une figure de style~La conclusion", 0,
     "L'axe est un titre de partie qui degage une orientation d'analyse."),
 QC("Que doit faire l'introduction ?", "Annoncer le plan~Donner la reponse finale~Citer tout le texte~Critiquer l'auteur", 0,
     "Elle situe le texte et annonce les axes, sans developper l'analyse."),
 QC("La problematique est ...", "Une question centrale~Une citation~Un connecteur~Une biographie", 0,
     "Elle formule la question a laquelle le commentaire va repondre."),
 QC("Quel schema pour un paragraphe ?", "Citation, analyse, assertion~Assertion, preuve, analyse, synthese~Conclusion, introduction~Titre, question", 1,
     "On enonce une idee, la prouve, l'analyse, puis la synthetise."),
 QC("La conclusion ...", "Introduit un nouvel axe~Repond a la problematique~Repete l'introduction~Supprime les citations", 1,
     "Elle apporte une reponse et peut proposer une ouverture."),
 QT("Comment transformer une observation de lecture en axe de plan ?",
    "On part d'une observation precise, par exemple la repetition de images nocturnes dans un poeme. On degage ensuite la constante : le texte construit une atmosphere de melancolie. On formule alors un titre d'axe qui announce une interpretation : « Une ecriture de la nuit et du secret ». On verifie enfin que cet axe couvre plusieurs passages et qu'il n'est pas limite a une seule phrase. Si l'observation reste isolee, on la place en sous-partie plutot que d'en faire un axe.",
    "On attend le passage de l'observation ponctuelle a la constante, puis a un titre interpretatif."),
 QT("Rediger un court paragraphe de commentaire a partir d'une citation.",
    "On commence par annoncer l'idee : le poete fait de la lumiere un symbole d'espoir. On introduit ensuite la citation avec un verbe de dire : le texte ecrit que « l'aube refleurit sur la ville ». On analyse alors les mots : le verbe refleurit associe la lumiere a une renaissance vegetale, et le mot aube marque le passage de la nuit au jour. On termine par une synthese : cette image transforme la ville en un espace renouvele, ce qui prepare le ton optimiste de la fin. La citation restee sans analyse n'aurait aucune valeur dans le commentaire.",
    "Le paragraphe doit comporter assertion, citation introduite, analyse des mots et synthese.")],
C("Le commentaire construit un sens a partir de citations courtes, analysees dans un plan en axes.",
  "Axe = constante de lecture + titre interpretatif",
  "Paragraphe : assertion · preuve · analyse · synthese",
  "Introduction~Auteur et contexte~Problematique~Axe~Grande partie du plan~Titre clair~Citation~Courte et analysee~Conclusion~Reponse et ouverture",
  "Lire le texte et relever les constantes|Formuler la problematique|Construire deux ou trois axes|Choisir les citations dans chaque axe|Rediger en paragraphes argumentes",
  "Reciter le texte sans l'expliquer|Donner un titre d'axe qui est une citation|Laisser une citation sans commentaire|Melanger plusieurs idees dans un paragraphe",
  "Images nocturnes~Constante de lecture~Titre d'axe~Ecriture de la nuit~Citation courte~Aube refleurit~Analyse~Symbole de renaissance~Synthese~Ton optimiste",
  "Commentaire compose~Plan par themes~Operations de lecture~Commentaire lineaire~Ordre du texte~Suivi phrase par phrase",
  "Introduction~Presentation et annonce du plan~Problematique~Question centrale~Conclusion~Reponse et ouverture~Transition~Lien entre parties"))


# ============================================================ A04
add("A04", "La dissertation : problematique et plan dialectique", "Français", ["Terminale"],
S("La dissertation est un exercice de reflexion qui repond a une question generale a partir d'une culture litteraire.|"
  "Le sujet peut etre une citation, une question ou une notion a commenter.|"
  "L'analyse du sujet definit les mots cles et le champ de la question.|"
  "La problematique transforme le sujet en une question precisant les termes en tension.|"
  "Le plan dialectique suit trois temps : these, antithese, synthese.|"
  "Le plan thematique repose sur plusieurs angles d'attaque de la meme question.|"
  "Chaque partie du plan doit correspondre a une reponse partielle a la problematique.|"
  "Les exemples litteraires sont des oeuvres et des passages mobilises avec precision.|"
  "Un exemple n'est pas une simple mention : il doit etreAnalyse en relation avec l'argument.|"
  "La transition evite la juxtaposition des parties en montrant le passagelogique.|"
  "L'introduction amene le sujet, le definit, pose la problematique et annonce le plan.|"
  "La conclusion apporte une reponse claire et peut ouvrir le debat."),
[QC("Un plan dialectique comporte trois temps :", "These, antithese, synthese~Introduction, citation, conclusion~Exemple, analyse, critique~Theme, registre, genre", 0,
     "Le plan dialectique confronte une these et une antithese avant de proposer une synthese."),
 QC("La problematique sert a ...", "Remplacer le sujet~Preciser la question et les tensions du sujet~Citer une oeuvre~Conclure", 1,
     "Elle reformule le sujet en question analytique."),
 QC("Un exemple litteraire doit etre ...", "Simplement cite~Analyse en lien avec l'argument~Invente~Place en introduction", 1,
     "On mobilise une oeuvre precise et on l'analyse pour etayer l'argument."),
 QC("Que contient l'introduction d'une dissertation ?", "La seule reponse~La definition des termes, la problematique, le plan~Tous les exemples~La bibliographie", 1,
     "Elle presente le sujet, le problematise et annonce le plan."),
 QC("Un plan thematique repose sur ...", "Plusieurs angles de la question~L'ordre chronologique de l'auteur~Une seule citation~Le hasard", 0,
     "Les parties explorent differentes faces de la meme question."),
 QC("Une transition sert a ...", "Changer de sujet~Relier deux parties~Terminer le devoir~Introduire une citation", 1,
     "Elle montre le enchainement logique entre deux parties."),
 QC("La conclusion doit ...", "Apporter une reponse a la problematique~Introduire un nouvel axe~Repeter l'introduction~Ignorer les exemples", 0,
     "Elle repond au sujet et peut ouvrir une perspective."),
 QT("Expliquer comment passer d'un sujet de dissertation a une problematique.",
    "On commence par definir les termes du sujet et par delimiter son champ. On repere ensuite les notions qui entrent en tension, par exemple liberte et engagement, ou realisme et idealisme. On formule alors une question qui ne soit ni une simple repetition du sujet ni une reponse deja donnee : en quoi l'ecriture engageante transforme-t-elle la liberte d'expression ? On verifie enfin que la question appelle plusieurs reponses possibles et qu'elle peut etre traitee par les exemples du programme. Une bonne problematique rend le plan necessaire.",
    "On attend definition des termes, identification de la tension, formulation d'une question ouverte et verification de son caracterTraitable."),
 QT("Construire le plan dialectique d'une dissertation sur le pouvoir des mots.",
    "En these, on peut soutenir que les mots ont un pouvoir de transformation : le poete donne une forme au reel et le lecteur voit autrement, comme dans la poesie lyrique. En antithese, on objectera que les mots peuvent aussi masquer le reel : la propagande et la language bureaucratique servent a dissimuler la violence. En synthese, on montrera que le pouvoir des mots depend de l'intention de celui qui les emploie et de l'esprit critique du lecteur : la literature elle-meme peut denoncer la manipulation. Chaque partie s'appuiera sur des oeuvres et des passages prec analysés.",
    "On attend les trois temps, une justification pour chacun et des exemmes litteraires mobilises.")],
C("La dissertation repond a une question par un raisonnement organise et des exemples litteraires analysee.",
  "Sujet → problematique → plan → exemples → reponse",
  "Dialectique : these · antithese · synthese",
  "Sujet~Question ou citation~Analyse des termes~Problematique~Question centrale~Tension a resoudre~Plan~These, antithese, synthese~Exemple~Oeuvre analysee",
  "Definir les mots du sujet|Degager les tensions et poser la question|Choisir un plan compatible avec la question|Repartir les exemples dans les parties|Rediger des paragraphes argumentes",
  "Repondre avant d'avoir analyse le sujet|Confondre exemple et simple nom d'oeuvre|Oublier de repondre a la problematique|Laisser deux parties sans transition",
  "Liberte et engagement~Tension du sujet~Problematique~Question ouverte~These~Pouvoir de transformation~Antithese~Mots qui masquent~Synthese~Intention et esprit critique",
  "Plan dialectique~These puis antithese~Synthese finale~Plan thematique~Plusieurs angles~Reponses simultanees",
  "Introduction~Sujet, problematique, plan~Paragraphe~Argument et exemple~Transition~Lien entre parties~Conclusion~Reponse et ouverture"))


# ============================================================ A05
add("A05", "Fonctions affines et lineaires : lecture graphique", "Maths", ["1re"],
S("Une fonction affine a pour expression f(x) = ax + b, ou a et b sont deux nombres reels.|"
  "Le coefficient a est le coefficient directeur : il donne la variation de f pour un accroissement de 1 de x.|"
  "Le nombre b est l'ordonnnee a l'origine : la droite coupe l'axe des ordonnees au point (0 ; b).|"
  "La representation graphique d'une fonction affine est une droite.|"
  "Si b = 0, la fonction est lineaire de la forme f(x) = ax et traduit une situation de proportionnalite.|"
  "Si a est positif, la fonction est croissante ; si a est negatif, elle est decroissante.|"
  "Si a = 0, la fonction est constante et sa droite est horizontale.|"
  "Pour tracer la droite, on utilise deux points, souvent les intersections avec les axes.|"
  "Resoudre f(x) = 0 revient a lire l'abscisse du point d'intersection avec l'axe des abscisses.|"
  "Resoudre f(x) = k revient a chercher l'abscisse d'un point de la droite d'ordonnnee k.|"
  "Les fonctions affines modelisent des situations a taux fixe : tarif, consommation, depreciation.|"
  "Dans un probleme, on identifie d'abord le taux a, puis la valeur initiale b."),
[QC("Quelle est la representation graphique d'une fonction affine ?", "Une parabole~Une droite~Un cercle~Une hyperbole", 1,
     "Une fonction affine se represente toujours par une droite."),
 QC("Dans f(x) = ax + b, que represente b ?", "Le coefficient directeur~L'ordonnnee a l'origine~La pente~Le domaine", 1,
     "b est la valeur de f(0), donc l'ordonnnee du point d'intersection avec l'axe vertical."),
 QC("Si a < 0, la fonction est ...", "Croissante~Decroissante~Constante~Indeterminee", 1,
     "Un coefficient directeur negatif donne une droite descendante."),
 QC("Une fonction lineaire correspond a ...", "a = 0~b = 0~a = b~b = 1", 1,
     "f(x) = ax est lineaire et traduit une proportionnalite."),
 QC("Comment tracer une droite ?", "Avec un seul point~Avec deux points~Avec trois angles~Avec l'aire", 1,
     "Deux points suffisent pour determiner une droite."),
 QC("Resoudre f(x) = 0 revient a lire ...", "L'ordonnnee a l'origine~L'abscisse du point sur l'axe des abscisses~La pente~Le maximum", 1,
     "On cherche la racine, c'est-a-dire l'abscisse ou la droite coupe l'axe horizontal."),
 QC("Un tarif avec un abonnement fixe plus un prix variable est modele par ...", "Une fonction affine~Une fonction constante~Une fonction exponentielle~Une fonction carree", 0,
     "Le montant fixe est b et le prix variable par unite est le coefficient a."),
 QT("Soit f(x) = 2x - 6. Donner le coefficient directeur, l'ordonnnee a l'origine, la racine et la variation.",
    "Le coefficient directeur est a = 2 : quand x augmente de 1, f(x) augmente de 2. L'ordonnnee a l'origine est b = -6, donc la droite passe par (0 ; -6). Pour la racine, on resout 2x - 6 = 0, soit 2x = 6 et x = 3 : la droite coupe l'axe des abscisses en (3 ; 0). Comme a est positif, la fonction est strictement croissante sur les reels. Le trace est immédiat avec les deux points (0 ; -6) et (3 ; 0).",
    "On attend a = 2, b = -6, racine x = 3, fonction croissante et trace par deux points."),
 QT("Un abonnement coute 15 euros par mois plus 0,20 euro par message. Exprimer le cout C(n) et l'interpreter.",
    "On a C(n) = 0,20 n + 15 ou n est le nombre de messages. Le coefficient 0,20 est le cout marginal : chaque message supplementaire augmente la facture de 0,20 euro. La valeur initiale 15 est le montant fixe paye meme si aucun message n'est envoye : c'est l'ordonnnee a l'origine de la droite. La fonction est croissante car le coefficient est positif. Pour 100 messages, on obtient C(100) = 0,20 x 100 + 15 = 35 euros, ce qui correspond au point (100 ; 35) de la droite.",
    "On attend l'expression, l'identification de a et b, l'interpretation et un calcul de point.")],
C("Une fonction affine est une droite : un taux de variation a et une valeur initiale b.",
  "f(x) = ax + b",
  "a > 0 : croissante · a < 0 : decroissante · b = f(0)",
  "Coefficient a~Taux de variation~Pente de la droite~Ordonnee b~Valeur initiale~Point (0 ; b)~Racine~Solution de f(x)=0~Trace~Deux points",
  "Identifier a et b dans l'expression|Determiner le sens de variation|Calculer deux points de la droite|Tracer et nommer les axes|Lire ou resoudre la valeur demandee",
  "Confondre a et b|Oublier le signe de b dans un calcul|Tracer avec un seul point|Lire la racine sur l'axe des ordonnees",
  "2x - 6~a = 2, b = -6~Racine~x = 3~Abonnement~15 + 0,20 n~100 messages~C(100) = 35 euros~Right~(0 ; -6) et (3 ; 0)",
  "Fonction affine~a non nul et b quelconque~Fonction lineaire~b = 0~Proportionnalite~f(x) = ax~Fonction constante~a = 0",
  "a positif~Droite montante~a negatif~Droite descendante~b positif~Intersection au-dessus de l'origine~b negatif~Intersection en dessous"))


# ============================================================ A06
add("A06", "Statistiques descriptives : moyenne, mediane et dispersion", "Maths", ["1re"],
S("Une serie statistique est un ensemble de valeurs observees sur une population ou un echantillon.|"
  "Les effectifs indiquent le nombre de fois ou chaque valeur apparait.|"
  "La moyenne ponderee se calcule en divisant la somme des produits valeur par effectif par l'effectif total.|"
  "La mediane est la valeur qui partage la serie en deux moities d'effectifs egaux.|"
  "Pour la trouver, on classe les valeurs par ordre croissant avant de se placer au rang (N + 1)/2.|"
  "L'etendue est la difference entre la valeur maximale et la valeur minimale.|"
  "La variance mesure la dispersion moyenne des valeurs autour de la moyenne.|"
  "L'ecart-type est la racine carree de la variance et s'exprime dans la meme unite que les donnees.|"
  "Un ecart-type faible indique une serie homogene ; un ecart-type eleve indique une serie disperse.|"
  "L'histogramme represente les effectifs par des rectangles de largeur proportionnelle aux classes.|"
  "Un diagramme en boite	resume la mediane, les quartiles et l'etendue de la serie.|"
  "La moyenne est sensible aux valeurs extremes, contrairement a la mediane."),
[QC("Comment obtenir la moyenne d'une serie avec effectifs ?", "En divisant la somme des valeurs par le nombre de valeurs differentes~En divisant la somme des produits par l'effectif total~En prenant la valeur centrale~En soustrayant le minimum du maximum", 1,
     "La moyenne ponderee est la somme des produits valeur fois effectif, divisee par l'effectif total."),
 QC("Que represente la mediane ?", "La valeur la plus frequente~La valeur qui partage la serie en deux~La moyenne des extremes~L'ecart-type", 1,
     "La mediane partage les donnees ordonnees en deux moities d'effectifs egaux."),
 QC("Quelle valeur faut-il classer avant de chercher la mediane ?", "Les effectifs~Les valeurs par ordre croissant~Les couleurs~Les pourcentages", 1,
     "Le classement par ordre croissant est indispensable."),
 QC("L'etendue est ...", "La moyenne des valeurs~Le maximum moins le minimum~La racine de la variance~Le quartiles", 1,
     "L'etendue mesure l'intervalle entre la plus petite et la plus grande valeur."),
 QC("Quelle mesure est sensible aux valeurs extremes ?", "La mediane~La moyenne~L'etendue~Le minimum", 1,
     "Une valeur tres elevee tire la moyenne, alors que la mediane reste stable."),
 QC("L'ecart-type s'exprime ...", "En carre de l'unite~Dans la meme unite que les donnees~Sans unite~En pourcentage toujours", 1,
     "L'ecart-type est la racine de la variance, donc dans l'unite d'origine."),
 QC("Que represente un histrogramme ?", "Les valeurs dans l'ordre~Les effectifs par classes~La moyenne~La variance", 1,
     "L'histogramme represente les effectifs de chaque classe."),
 QT("Calculer la moyenne de la serie : valeurs 10, 12, 12, 15 avec effectifs 2, 3, 1, 4.",
    "On calcule d'abord les produits : 10 x 2 = 20, 12 x 3 = 36, 12 x 1 = 12, 15 x 4 = 60. Leur somme vaut 20 + 36 + 12 + 60 = 128. L'effectif total est 2 + 3 + 1 + 4 = 10. La moyenne est donc 128 / 10 = 12,8. On peut remarquer que la valeur 12 apparait avec deux effectifs differents : les lignes du tableau doivent etre additionnees avant le calcul. Le resultat 12,8 se situe bien entre le minimum 10 et le maximum 15.",
    "On attend la somme des produits 128, l'effectif total 10 et la moyenne 12,8."),
 QT("Expliquer pourquoi on peut preférer la mediane a la moyenne pour decrire des salaires.",
    "Les salaires comportent souvent quelques valeurs tres elevees, par exemple les dirigeants. Ces extremes augmentent la moyenne, qui donne alors une image trop optimiste du salaire typique. La mediane, elle, depend seulement du rang central : la moitie des salaries gagne moins et l'autre moitie gagne plus, quelle que soit l'ampleur des extremes. Pour decrire le niveau de vie median d'une population, la mediane est donc plus representative. On peut completer avec les quartiles et un diagramme en boite pour montrer la dispersion et les ecarts entre groupes.",
    "On doit opposer la sensibilité de la moyenne aux extremes a la stabilite de la mediane, et proposer les quartiles.")],
C("Une serie se decrit par une tendance centrale (moyenne, mediane) et une dispersion (etendue, ecart-type).",
  "Moyenne = somme(valueur x effectif) / effectif total",
  "Ecart-type = racine de la variance · mediane = valeur centrale apres classement",
  "Moyenne~Tendance centrale~Sensible aux extremes~Mediane~Valeur centrale~Stable~Etendue~Max moins min~Ecart-type~Dispersion",
  "Classer les valeurs|Construire le tableau des effectifs|Calculer moyenne et mediane|Calculer etendue et ecart-type|Interpretation dans le contexte",
  "Oublier de classer avant la mediane|Confondre variance et ecart-type|Moyenne sans pondération|Conclure sans interprete",
  "Serie 10 12 12 15~Effectifs 2 3 1 4~Moyenne~12,8~Salaires~Quelques extremes~Mediane~Salaire typique~Ecart-type~Homogeneite",
  "Moyenne~Tiree par les extremes~Mediane~Depend du rang central~Faible ecart-type~Serie homogene~Fort ecart-type~Serie disperse",
  "Histogramme~Effectifs par classe~Diagramme en boite~Mediane et quartiles~Variance~Dispersion au carre~Ecart-type~Dispersion en unite"))


# ============================================================ A07
add("A07", "Probabilites : evenements et probabilites conditionnelles", "Maths", ["1re", "Terminale"],
S("Une experience aleatoire a un resultat imprévisible mais appartient a un ensemble connu de resultats.|"
  "L'univers est l'ensemble de tous les resultats possibles, notes omega.|"
  "Un evenement est une partie de l'univers : un ensemble de resultats.|"
  "La probabilite d'un evenement est un nombre entre 0 et 1 ; la somme des probabilites des resultats vaut 1.|"
  "Quand tous les resultats sont equiprobables, on divise le nombre de cas favorables par le nombre de cas possibles.|"
  "Une loi de probabilite associe une probabilite a chaque valeur d'une variable aleatoire.|"
  "L'evenement contraire A barre regroupe les resultats qui ne sont pas dans A, avec P(A barre) = 1 - P(A).|"
  "Deux evenements sont independants si la realisation de l'un ne modifie pas la probabilite de l'autre.|"
  "La probabilite conditionnelle P(A sachant B) se calcule par P(A intersection B) / P(B), avec P(B) non nul.|"
  "Un arbre pondere represente les etapes successives et les probabilites conditionnelles sur les branches.|"
  "L'esperance d'une variable aleatoire est la somme des valeurs pondérees par leurs probabilites.|"
  "Pour un tirage avec remise, les tirages sont independants ; sans remise, ils sont dependants."),
[QC("A quoi appartient un evenement dans une experience aleatoire ?", "A l'univers des resultats~A la moyenne~A l'ecart-type~A la variance", 0,
     "Un evenement est une partie de l'univers des resultats possibles."),
 QC("Quelle est la somme des probabilites de tous les resultats ?", "0~1~10~100", 1,
     "La loi de probabilite est complete : les probabilites somment a 1."),
 QC("Comment calculer P(A barre) ?", "P(A) + 1~1 - P(A)~P(A) / 2~P(A) au carre", 1,
     "L'evenement contraire complemente A dans l'univers."),
 QC("Que represente P(A sachant B) ?", "La probabilite de A sachant B~La probabilite de B sans A~La somme de A et B~Le produit de A et B", 0,
     "C'est une probabilite conditionnelle : on sait que B est realise."),
 QC("Quelle est la formule de la probabilite conditionnelle ?", "P(A et B) / P(B)~P(A) x P(B)~P(A) / P(B)~P(B) / P(A et B)", 0,
     "On divise la probabilite de l'intersection par celle de l'evenement-condition."),
 QC("Dans un tirage avec remise, les tirages sont ...", "Dependants~Independants~Impossibles~Egaux a 1", 1,
     "Le remise restitue l'objet, donc les tirages ne s'influent pas."),
 QC("Que represente un arbre pondere ?", "Les effectifs d'une serie~Les etapes et probabilites conditionnelles~La moyenne d'une loi~L'etendue", 1,
     "Chaque branche porte une probabilite et les feuilles donnent les intersections."),
 QT("Dans une urne contenant 3 boules rouges et 2 bleues, calculer la probabilite de tirer deux rouges avec remise, puis sans remise.",
    "Avec remise, les tirages sont independants : P(R1 et R2) = 3/5 x 3/5 = 9/25 = 0,36. Sans remise, le second tirage est conditionnel au premier : apres une premiere boule rouge, il reste 2 rouges sur 4 boules, donc P(R2 | R1) = 2/4 = 1/2. Par la formule des probabilites conditionnelles, P(R1 et R2) = 3/5 x 1/2 = 3/10 = 0,3. La probabilite est plus faible sans remise parce que le premier tirage appauvrit l'urne en boules rouges.",
    "On attend 9/25 avec remise, 3/10 sans remise, et l'explication de la dependence."),
 QT("Definir l'esperance d'une variable aleatoire et calculer celle d'un jeu : gain 10 avec probabilite 0,2 et perte 2 avec probabilite 0,8.",
    "L'esperance est la moyenne ponderee des valeurs par leurs probabilites : E(X) = somme(x_i x p_i). Ici E(X) = 10 x 0,2 + (-2) x 0,8 = 2 - 1,6 = 0,4. Le gain moyen par partie est donc 0,4 unite : le jeu est legerement favorable au joueur. Si l'esperance etait negative, le jeu serait defavorable ; si elle etait nulle, il serait equitable. L'esperance ne predit pas le resultat d'une partie, mais la tendance moyenne sur un grand nombre de parties.",
    "On attend la definition, le calcul 0,4 et l'interpretation de jeu favorable, defavorable ou equitable.")],
C("Les probabilites structurent l'aleatoire : evenements, lois, conditionnement et esperance.",
  "P(A sachant B) = P(A intersection B) / P(B)",
  "P(contraire de A) = 1 - P(A) · independance : P(A et B) = P(A) x P(B)",
  "Univers~Tous les resultats~Evenement~Partie de l'univers~Contraire~Complement~Conditionnelle~Sachant que B~Independance~Sans influence",
  "Delimiter l'univers des resultats|Identifier l'evenement et ses cas favorables|Choisir la formule adaptee|Construire un arbre si plusieurs etapes|Calculer et interpreter le resultat",
  "Oublier de verifier que P(B) est non nul|Confondre avec remise et sans remise|Additionner au lieu de multiplier les probabilites|Croire que l'esperance predit un resultat",
  "3 rouges 2 bleues~Avec remise 9/25~Sans remise~3/10~Jeu~10 a 0,2 et -2 a 0,8~Esperance~0,4~Arbre~Branches pondérées",
  "Avec remise~Tirages independants~Sans remise~Tirages dependants~Conditionnelle~On sait que B~Contraire~Tout sauf A",
  "Probabilite~Nombre entre 0 et 1~Esperance~Moyenne ponderee~Loi~Probabilites par valeur~Evenement certain~Probabilite 1"))


# ============================================================ A08
add("A08", "Suites numeriques et interets composes", "Maths", ["Terminale"],
S("Une suite est une liste ordonnee de nombres notes u_0, u_1, ..., u_n.|"
  "Une suite arithmetique verifie u(n+1) = u(n) + r, ou r est la raison constante.|"
  "Le terme general d'une suite arithmetique est u(n) = u(0) + n x r.|"
  "Une suite geometrique verifie u(n+1) = q x u(n), ou q est la raison multiplicative.|"
  "Le terme general d'une suite geometrique est u(n) = u(0) x q puissance n.|"
  "La somme des termes d'une suite geometrique s'obtient par la formule a (1 - q puissance n) / (1 - q) si q est different de 1.|"
  "Les interets simples rapportent chaque annee un pourcentage du capital initial seulement.|"
  "Les interets composes rapportent des interets sur le capital deja augmente : la suite des capitaux est geometrique.|"
  "Un taux annuel de t pour cent correspond a un facteur q = 1 + t/100.|"
  "Le capital apres n annees avec interets composes vaut C(0) x (1 + t/100) puissance n.|"
  "Une suite arithmetico-geometrique verifie u(n+1) = a x u(n) + b et alterne multiplication et addition.|"
  "Les suites permettent de modeliser l'epargne, un amortissement, une croissance ou une depreciation."),
[QC("Quelle relation definit une suite arithmetique ?", "u(n+1) = u(n) + r~u(n+1) = r x u(n)~u(n+1) = u(n) / r~u(n+1) = u(n) puissance r", 0,
     "On ajoute toujours la meme raison r au terme precedent."),
 QC("Quelle relation definit une suite geometrique ?", "u(n+1) = u(n) + q~u(n+1) = q x u(n)~u(n+1) = q - u(n)~u(n+1) = u(n) + n", 1,
     "On multiplie le terme precedent par la raison q."),
 QC("Un capital de 1000 euros a 5 pour cent pendant 2 ans en interets composes donne :", "1050 euros~1100 euros~1102,50 euros~1150 euros", 2,
     "1000 x 1,05 x 1,05 = 1102,50 euros."),
 QC("Les interets simples sur 1000 euros a 5 pour cent pendant 2 ans valent :", "50 euros~100 euros~102,50 euros~110 euros", 1,
     "On calcule 1000 x 0,05 x 2 = 100 euros, sans capitalisation."),
 QC("A un taux de 4 pour cent correspond le facteur :", "0,04~1,04~4~1,4", 1,
     "Le facteur de progression est q = 1 + 0,04 = 1,04."),
 QC("Dans les interets composes, la suite des capitaux est ...", "Arithmetique~Geometrique~Constante~Alternativee", 1,
     "Chaque annee multiplie le capital par le meme facteur."),
 QC("Une suite arithmetico-geometrique a pour forme :", "u(n+1) = a x u(n) + b~u(n+1) = u(n) + b~u(n+1) = a x u(n)~u(n+1) = a + b", 0,
     "On multiplie par a puis on ajoute b : c'est une recurrence mixte."),
 QT("Comparer l'epargne de 5000 euros placee 3 ans a 4 pour cent en interets simples et en interets composes.",
    "En interets simples, le gain annuel est 5000 x 0,04 = 200 euros, donc 600 euros sur trois ans : le capital final est 5600 euros. En interets composes, le facteur est 1,04 et le capital final est 5000 x 1,04 puissance 3, soit 5000 x 1,124864 = 5624,32 euros. Les interets composes rapportent 24,32 euros de plus, car la deuxieme et la troisieme annee rapportent aussi des interets sur les interets deja verses. L'ecart augmente avec la duree et avec le taux.",
    "On attend 5600 euros, environ 5624,32 euros et l'explication de la capitalisation."),
 QT("Expliquer comment une suite geometrique peut modeliser la depreciation d'un materiel.",
    "Si un materiel perd chaque annee 10 pour cent de sa valeur, il conserve 90 pour cent de sa valeur precedente. La suite des valeurs verifie V(n+1) = 0,9 x V(n) : c'est une suite geometrique de raison q = 0,9, inferieure a 1, donc decroissante. Le terme general est V(n) = V(0) x 0,9 puissance n. Apres 5 ans, un materiel achete 20000 euros vaut 20000 x 0,9 puissance 5, environ 11809 euros. La depreciation est rapide les premieres annees puis ralentit, ce qui est different d'un amortissement lineaire ou la perte annuelle est constante.",
    "On attend la raison 0,9, le terme general, un calcul et la comparaison avec l'amortissement lineaire.")],
C("Une suite modelise une evolution discrete : arithmetique pour un taux fixe ajoute, geometrique pour un facteur multiplicatif.",
  "Arithmetique : u(n) = u(0) + nr · Geometrique : u(n) = u(0) q puissance n",
  "Capital compose = C(0) x (1 + t/100) puissance n",
  "Suite arithmetique~Raison additive r~Terme general~u(0) + nr~Suite geometrique~Raison multiplicative q~Termes~u(0) q^n~Interets composes~Capitalisation",
  "Identifier le type de suite|Determiner la raison ou le facteur|Ecrire le terme general|Calculer le terme demande|Interpretation dans le contexte",
  "Confondre raison additive et multiplicative|Oublier de convertir le taux en facteur|Appliquer des interets simples a un placement compose|Ne pas arrondir seulement a la fin",
  "5000 a 4 pour cent~Simple : 5600 euros~Compose~5624,32 euros~Materiel~20000 x 0,9^5~Valeur~11809 euros~Taux 10~Facteur 0,9",
  "Interets simples~Interet du capital initial~Interets composes~Interet des interets~Amortissement lineaire~Perte constante~Depreciation~Perte proportionnelle",
  "Suite croissante~q superieur a 1~Suite decroissante~q entre 0 et 1~Suite constante~q egal a 1~Recurrence~Relation entre termes"))


# ============================================================ A09
add("A09", "Derivation et variations d'une fonction", "Maths", ["Terminale"],
S("Le nombre derive d'une fonction f en a est la limite du taux d'accroissement de f entre a et a + h.|"
  "Geometriquement, il donne la pente de la tangente a la courbe de f au point d'abscisse a.|"
  "La fonction derivee f prime associe a chaque x le nombre derive de f en x.|"
  "La derivee d'une fonction affine ax + b est la constante a.|"
  "La derivee de x au carre est 2x ; celle de x au cube est 3x au carre.|"
  "La derivee d'une somme est la somme des derivees ; les constantes facteurs sont conserves.|"
  "Si f prime est strictement positive sur un intervalle, f est strictement croissante sur cet intervalle.|"
  "Si f prime est strictement negative, f est strictement decroissante.|"
  "Un extremum local se produit quand f prime s'annule en changeant de signe.|"
  "Un point ou la derivee est nulle a une tangente horizontale.|"
  "Le signe de la derivee se lit souvent avec un tableau de variations.|"
  "En economie, la derivee d'une fonction de cout donne le cout marginal, c'est-a-dire le cout d'une unite supplementaire."),
[QC("Que represente le nombre derive en a ?", "L'aire sous la courbe~La pente de la tangente en a~La moyenne de f~La valeur de f(a)", 1,
     "Il donne le taux d'accroissement instantane, donc la pente de la tangente."),
 QC("Quelle est la derivee de f(x) = x au carre ?", "x~2x~3x~x au cube", 1,
     "La derivee de x puissance 2 est 2x."),
 QC("Quelle est la derivee de f(x) = 5x + 3 ?", "5~3~5x~8", 0,
     "La pente d'une droite affine est le coefficient de x."),
 QC("Si f prime est negative sur un intervalle, alors f est ...", "Croissante~Decroissante~Constante~Maximum", 1,
     "Une derivee negative traduit une variation decroissante."),
 QC("Quand la derivee s'annule en changeant de signe, on a ...", "Un extremum local~Une asymptote~Une racine de f~Un minimum de la derivee", 0,
     "Le changement de signe de f prime indique un maximum ou un minimum local."),
 QC("Que donne la derivee d'une fonction de cout ?", "Le cout total~Le cout marginal~Le prix de vente~Le benefice", 1,
     "La derivee mesure l'accroissement du cout pour une unite supplementaire."),
 QC("Une tangente horizontale correspond a ...", "f prime strictement positive~f prime nulle~f prime indefinie~f croissante", 1,
     "Une pente nulle donne une tangente horizontale."),
 QT("Etudier les variations de f(x) = x au carre - 4x + 3.",
    "On calcule d'abord la derivee : f prime(x) = 2x - 4. On resout f prime(x) = 0, soit 2x - 4 = 0 et x = 2. Pour x inferieur a 2, par exemple x = 0, f prime(0) = -4 est negatif : f est decroissante sur l'intervalle ouvert moins infini a 2. Pour x superieur a 2, par exemple x = 3, f prime(3) = 2 est positif : f est croissante sur 2 a plus infini. La derivee change de signe de moins a plus en x = 2 : f admet donc un minimum local. Sa valeur est f(2) = 4 - 8 + 3 = -1. La courbe est une parabole qui s'ouvre vers le haut, de sommet (2 ; -1).",
    "On attend f prime = 2x - 4, racine x = 2, decroissance puis croissance et minimum -1."),
 QT("Interpreter le nombre derive d'une fonction de cout C(q) = 0,5 q au carre + 10q + 100 en q = 20.",
    "La derivee est C prime(q) = q + 10. En q = 20, C prime(20) = 30. Cela signifie que si la production passe de 20 a 21 unites, le cout total augmente d'environ 30 unites monetaires : c'est le cout marginal. Le cout moyen, lui, vaut C(20)/20 = (200 + 200 + 100)/20 = 25. Le cout marginal 30 est superieur au cout moyen 25, donc produire une unite supplementaire augmente le cout moyen. Ce raisonnement aide le gestionnaire a decider s'il est rentable d'augmenter la production.",
    "On attend C prime = q + 10, valeur 30 en q = 20, et l'interpretation en cout marginal compare au cout moyen.")],
C("La derivee mesure la variation instantanee d'une fonction et permet de determiner ses variations et ses extrema.",
  "f prime(a) = limite de (f(a+h) - f(a)) / h quand h tend vers 0",
  "f prime positif : croissance · f prime negatif : decroissance · f prime nul : tangente horizontale",
  "Nombre derive~Pente de la tangente~Taux instantane~Fonction derivee~f prime(x)~Signe~Variations~Extremum~Changement de signe",
  "Calculer la derivee|Resoudre f prime(x) = 0|Etudier le signe sur chaque intervalle|Dresser le tableau de variations|Identifier les extrema et interpreter",
  "Confondre f et f prime|Oublier le facteur 2 sur la derivee de x au carre|Conclure une extremum sans changement de signe|Ne pas verifier un signe avec un point test",
  "x^2 - 4x + 3~f prime = 2x - 4~Racine~x = 2~Minimum~f(2) = -1~Cout~q + 10 en q=20~Cout marginal~30",
  "f prime positif~Fonction croissante~f prime negatif~Fonction decroissante~f prime nul~Extremum possible~f prime non defini~Point anguleux",
  "Tangente~Droite de pente f prime(a)~Secante~Pente du taux d'accroissement~Extremum local~Maximum ou minimum~Cout marginal~Derivee du cout"))


# ============================================================ A10
add("A10", "La Revolution francaise et l'Empire", "Histoire-Géographie", ["1re"],
S("La Revolution francaise debute en 1789 dans un contexte de crise financiere et sociale.|"
  "Les etats generaux convoques a Versailles en mai 1789 representent le clerge, la noblesse et le tiers etat.|"
  "La prise de la Bastille, le 14 juillet 1789, marque l'entree du peuple dans la revolution.|"
  "La nuit du 4 aout 1789 supprime les privileges seigneuriaux.|"
  "La Declaration des droits de l'homme et du citoyen, votee en aout 1789, affirme la liberte, l'egalite et la souverainete nationale.|"
  "La constitution de 1791 instaure une monarchie constitutionnelle avec separation des pouvoirs.|"
  "La chute de la monarchie, le 10 aout 1792, conduit a la proclamation de la Republique le 21 septembre.|"
  "Louis XVI est execute le 21 janvier 1793 apres un proces devant la Convention.|"
  "La Terreur, de 1793 a 1794, est marquee par le Comite de salut public et la repression des opposants.|"
  "Le Directoire, instaure en 1795, remplace la Convention mais reste instable.|"
  "Bonaparte prend le pouvoir le 18 Brumaire an VIII, le 9 novembre 1799.|"
  "Il devient empereur en 1804 ; le Code civil consacre l'egalite devant la loi, la propriete et la laicisation partielle de l'etat."),
[QC("Quand debute la Revolution francaise ?", "1789~1792~1799~1804", 0,
     "Les etats generaux s'ouvrent en mai 1789 et la Bastille est prise en juillet."),
 QC("Quels ordres composent les etats generaux ?", "Clerge, noblesse, tiers etat~Rois, princes, ducs~Paysans, ouvriers, bourgeois~Soldats, pretres, juges", 0,
     "La societe d'ancien regime est divisee en trois ordres."),
 QC("Que proclame la Declaration des droits de l'homme ?", "Le droit divin des rois~Liberte, egalite et souverainete nationale~La Terreur~Le Code civil", 1,
     "Les articles fondamentaux affirment les droits naturels et la souverainete de la nation."),
 QC("Quelle date correspond a la prise de la Bastille ?", "4 aout 1789~14 juillet 1789~21 janvier 1793~9 novembre 1799", 1,
     "Le 14 juillet 1789 est devenu la fete nationale."),
 QC("Quel regime la constitution de 1791 instaure-t-elle ?", "Une monarchie absolue~Une monarchie constitutionnelle~Une republique~Un empire", 1,
     "Le roi conserve des pouvoirs limites par une assemblee elue."),
 QC("Qui est execute le 21 janvier 1793 ?", "Robespierre~Louis XVI~Bonaparte~Mirabeau", 1,
     "Louis XVI est condamne par la Convention nationale."),
 QC("Quel texte juridique majeur est adopte sous l'Empire ?", "La Declaration de 1789~Le Code civil~La constitution de 1791~L'edit de Nantes", 1,
     "Le Code civil de 1804 unifie le droit et consacre l'egalite devant la loi."),
 QT("Expliquer pourquoi la Revolution francaise est un moment de rupture politique et juridique.",
    "Avant 1789, la souverainete appartient au roi par droit divin et la societe est divisee en ordres avec des privileges. La rupture tient d'abord au transfert de la souverainete a la nation : les deputes siegent au nom du peuple et la constitution ecrite limite les pouvoirs. Elle tient ensuite a l'egalite juridique proclamee par la Declaration des droits de l'homme et par l'abolition des privileges dans la nuit du 4 aout 1789. Enfin, l'instauration de la Republique en 1792 puis du Code civil en 1804 refondent les institutions et le droit. Les principes de 1789 restent une reference pour la democratie et les droits de l'homme.",
    "On attend le passage de la souverainete royale a la souverainete nationale, l'egalite juridique et la refonte institutionnelle."),
 QT("Distinguer la phase constitutielle de 1789-1791 de la phase radicale de 1792-1794.",
    "De 1789 a 1791, la revolution est d'abord reformiste : les etats generaux deviennent Assemblee constituante, les privileges sont abolis, les droits sont proclames et une monarchie constitutionnelle est etablie. La guerre exterieure et la defiance envers le roi radicalisent le mouvement en 1792 : la monarchie tombe, la Republique est proclamee et la Convention juge le roi. De 1793 a 1794, le Comite de salut public exerce un pouvoir autoritaire et la Terreur frappe les suspects. La difference tient au regime politique et au rapport a la liberte : la premiere phase ecrit des principes, la seconde les suspend au nom de la defense de la Republique.",
    "On oppose reformisme constitutionnel et radicalisation republicaine, avec dates et acteurs.")],
C("La Revolution francaise transfert la souverainete du roi a la nation et installe un nouvel ordre juridique.",
  "Souverainete nationale + egalite devant la loi = nouveau regime",
  "1789 droits · 1792 Republique · 1793 Terreur · 1804 Code civil",
  "Etats generaux~Trois ordres~Bastille~14 juillet 1789~Declaration~Droits de l'homme~Constitution~Monarchie constitutionnelle~Convention~Republique",
  "Situer la crise de l'ancien regime|Etudier les evenements de 1789|Analyser les principes de 1789|Suivre la radicalisation de 1792 a 1794|Mesurer l'heritage de 1804",
  "Confondre les dates de 1789 et 1792|Croire que la Terreur commence en 1789|Oublier le role du tiers etat|Reduire la Revolution a la seule execution du roi",
  "14 juillet 1789~Prise de la Bastille~4 aout 1789~Abolition des privileges~21 janvier 1793~Execution de Louis XVI~An VIII~18 Brumaire~Code civil~Egalite devant la loi",
  "Monarchie constitutionnelle~Roi aux pouvoirs limites~Republique~Souverainete nationale~Terreur~Repression revolutionnaire~Directoire~Regime instable",
  "Declaration des droits~Principes de 1789~Code civil~Droit ecrit de 1804~Souverainete~Du roi a la nation~Egalite~Contre les privileges"))


# ============================================================ A11
add("A11", "Industrialisation et societe au XIXe siecle", "Histoire-Géographie", ["1re"],
S("La revolution industrielle debute en Angleterre a la fin du XVIIIe siecle avant de s'etendre a l'Europe.|"
  "La machine a vapeur, perfectionnee par Watt, fournit une nouvelle source d'energie aux ateliers et aux transports.|"
  "L'usine remplace progressivement l'atelier artisanal et impose une discipline du travail et un horaire regulier.|"
  "La division du travail augmente la productivite mais rend l'ouvrier dependant d'une tache repetitive.|"
  "L'exode rural alimente une croissance urbaine rapide, souvent accompagnee de mauvaises conditions de logement.|"
  "Le chemin de fer se developpe a partir des annees 1830 et transforme les echanges et les delais de transport.|"
  "La classe ouvriere, ou proletariat, se constitue autour des travailleurs de l'industrie.|"
  "La bourgeoisie industrielle tire profit de la croissance et domine la vie economique et politique.|"
  "Les conditions de travail sont difficiles : longues journees, bas salaires, travail des femmes et des enfants.|"
  "Les premiers socialistes et les syndicats denoncent l'exploitation et revendiquent des droits sociaux.|"
  "Les revolutions de 1848 portent des revendications politiques et sociales dans plusieurs pays europeens.|"
  "L'industrialisation s'accompagne d'une expansion coloniale, source de matieres premieres et de debouches."),
[QC("Ou debute la revolution industrielle ?", "En France en 1789~En Angleterre a la fin du XVIIIe siecle~Aux Etats-Unis en 1860~En Allemagne en 1900", 1,
     "L'Angleterre est le premier pays a connaitre l'industrialisation."),
 QC("Quelle invention fournit l'energie des usines et des trains ?", "La machine a vapeur~L'imprimerie~Le telephone~Le moteur electrique", 0,
     "La machine a vapeur est au coeur de la premiere revolution industrielle."),
 QC("Quel est un effet de la division du travail ?", "Une baisse de productivite~Une specialisation des taches~La fin des usines~Une hausse des salaires automatique", 1,
     "Chaque ouvrier se specialise sur une tache, ce qui accroit la productivite."),
 QC("Qu'appelle-t-on proletariat ?", "La bourgeoisie industrielle~La classe des travailleurs industriels~Les paysans proprietaires~Les marchands coloniaux", 1,
     "Le proletariat designe les ouvriers vendant leur force de travail."),
 QC("Quand le chemin de fer se developpe-t-il en Europe ?", "Avant 1750~A partir des annees 1830~Apres 1945~Au XIVe siecle", 1,
     "Les premieres lignes ferroviaires publiques apparaissent dans les annees 1830."),
 QC("Quelle revendication sociale apparait au XIXe siecle ?", "Le retour aux privileges~La journee de huit heures et des droits sociaux~L'abolition du commerce~Le desinteret pour les usines", 1,
     "Les mouvements ouvriers revendiquent de meilleures conditions et des droits."),
 QC("Quel lien existe-t-il entre industrialisation et colonialisation ?", "Aucun lien~Recherche de matieres premieres et de debouches~Colonisation apres 1945 seulement~Remplacement des usines par les colonies", 1,
     "Les puissances industrielles recherchent ressources et marches outre-mer."),
 QT("Expliquer comment l'industrialisation transforme la societe francaise au XIXe siecle.",
    "L'industrialisation deplace la population des campagnes vers les villes : les ouvriers quittent la terre pour les usines et vivent souvent dans des quartiers surpeuples. Elle cree une classe ouvriere, le proletariat, dont la journee est reglee par l'horaire de l'usine et la division du travail. En face se developpe une bourgeoisie industrielle qui accumule le capital et influence la politique. Les inegalites de revenus et les conditions de travail penibles suscitent des mouvements de protestation, des grèves et des theories socialistes. Les revolutions de 1848 expriment ces tensions. Enfin, le chemin de fer et la colonisation inscrivent la France dans une economie nationale et mondiale.",
    "On attend urbanisation, formation des classes, conditions de travail, revendications sociales et ouverture economique."),
 QT("Distinguer les effets economiques et les effets sociaux du chemin de fer au XIXe siecle.",
    "Sur le plan economique, le chemin de fer reduit considerablement le cout et la duree du transport des marchandises. Il permet la circulation rapide du charbon et des produits manufactures, l'extension des marches nationaux et la synchronisation des prix. Il stimule aussi la metallurgie et la construction. Sur le plan social, il modifie les deplacements des personnes, developpe le tourisme et les migrations vers les villes, mais il impose aussi une discipline des horaires et provoque des accidents. Les compagnies ferroviaires deviennent de grands employeurs et le train symbolise la puissance industrielle de l'epoque.",
    "On attend des effets de marché et de production d'un cote, de mobilite et de conditions de vie de l'autre.")],
C("L'industrialisation transforme la production, les villes et les rapports sociaux.",
  "Vapeur + usine + division du travail = productivite accrue",
  "Proletariat · bourgeoisie industrielle · urbanisation · revendications sociales",
  "Machine a vapeur~Energie nouvelle~Usine~Discipline du travail~Division du travail~Specialisation~Exode rural~Croissance urbaine~Chemin de fer~Echanges rapides",
  "Situer la revolution industrielle en Angleterre|Identifier les innovations techniques|Analyser l'organisation de l'usine|Mesurer les effets sociaux et urbains|Relier industrialisation et colonialisation",
  "Dater l'industrialisation au XVIIIe siecle en France|Confondre bourgeoisie et proletariat|Oublier le travail des enfants|Ignorer les revendications ouvrières",
  "Fin XVIIIe~Angleterre~1830~Developpement ferroviaire~1848~Revolutions sociales~Ouvriers~Journees longues~Colonies~Matières premieres",
  "Artisanat~Travail a domicile~Usine~Travail collectif et horaire~Bourgeoisie~Proprietaire du capital~Proletariat~Vendeur de force de travail",
  "Effets economiques~Productivite et marches~Effets sociaux~Urbanisation et inegalites~Chemin de fer~Transport~Colonisation~Ressources et debouches"))


# ============================================================ A12
add("A12", "La Premiere Guerre mondiale et le traite de Versailles", "Histoire-Géographie", ["1re", "Terminale"],
S("La Premiere Guerre mondiale dure de 1914 a 1918 et oppose deux coalitions d'Etats.|"
  "L'assassinat de l'archiduc Francois-Ferdinand a Sarajevo en juin 1914 declenche la crise.|"
  "Les systemes d'alliances et la mobilisation des armies entrainent une generalization du conflit.|"
  "La guerre de position s'installe sur le front occidental avec un reseau de tranchees.|"
  "Les soldats vivent dans des conditions extremes : boue, gaz de combat, maladie et violence de masse.|"
  "La bataille de Verdun, en 1916, devient le symbole de la guerre d'usure.|"
  "L'entree en guerre des Etats-Unis en 1917 et la revolution russe modifient l'equilibre.|"
  "Le conflit mobilise aussi les populations civiles et les economies nationales.|"
  "L'armistice est signe le 11 novembre 1918.|"
  "Le traite de Versailles, signe en juin 1919, impose des conditions severes a l'Allemagne.|"
  "La Societe des Nations est creee pour organiser la paix et la cooperation internationale.|"
  "La guerre laisse des millions de morts, des ruines, des dettes et des tensions qui preparent de nouveaux conflits."),
[QC("Quel evenement declenche la crise de l'ete 1914 ?", "La prise de la Bastille~L'assassinat de Sarajevo~Le traite de Versailles~La revolution russe", 1,
     "L'attentat de Sarajevo contre Francois-Ferdinand declenche la crise diplomatique."),
 QC("Quel type de guerre domine sur le front occidental ?", "Une guerre de movement~Une guerre de position~Une guerre navale seule~Une guerre coloniale", 1,
     "Les armies s'enterrent dans des tranchees et le front se fige."),
 QC("Quelle bataille symbolise la guerre d'usure en 1916 ?", "Verdun~Waterloo~Sedan~Austerlitz", 0,
     "Verdun illustre la violence de masse et la duree du conflit."),
 QC("Quand l'armistice est-il signe ?", "11 novembre 1918~28 juin 1919~2 aout 1914~8 mai 1945", 0,
     "Les combats s'arreent le 11 novembre 1918."),
 QC("Que prevoit le traite de Versailles pour l'Allemagne ?", "Des reparations et des pertes territoriales~Une alliance avec l'Allemagne~Son agrandissement~L'abolition de toutes les frontiers", 0,
     "Le traite impose des reparations, des cessions de territoires et des limites militaires."),
 QC("Quelle organisation internationale est creee apres la guerre ?", "La Societe des Nations~L'Union europeenne~L'ONU~Le Conseil de l'Europe", 0,
     "La SDN est fondee en 1919 pour promouvoir la paix ; l'ONU viendra apres 1945."),
 QC("Quel effet de la guerre sur les populations civiles ?", "Aucun effet~Mobilisation economique et souffrances~Une prospérité generale~La fin des villes", 1,
     "Les economies sont mobilisees et les civils subissent privations et violences."),
 QT("Expliquer pourquoi la Premiere Guerre mondiale est une guerre de masse et totale.",
    "Elle est de masse par le nombre de soldats mobilises, des millions, et par la violence subie par les populations civiles. Elle est totale parce que les Etats mobilisent toutes leurs ressources : l'industrie produit des munitions, les femmes remplacent les hommes dans les usines, les finances publiques sont mises a contribution et la propagande oriente l'opinion. La guerre de position impose une endurance collective et les gouvernements contrôlent l'information. Cette mobilisation explique l'ampleur des pertes et la difficulté a revenir a la paix apres 1918.",
    "On attend mobilisation des hommes, des economies, des civils et de l'opinion, avec des exemples."),
 QT("Analyser les consequences du traite de Versailles pour l'Europe de l'entre-deux-guerres.",
    "Le traite de 1919 met fin a la guerre mais il humilie l'Allemagne : perte de territoires, reduction de l'armee, reparations economiques et reconnaissance de la responsabilite du conflit. Il redessine les frontiers europeennes avec la creation ou la restauration d'Etats en Europe centrale. La Societe des Nations tente d'organiser une paix durable, mais elle reste faible face aux revisions et aux crises economiques. Le ressentiment allemand, les difficultes de paiement des reparations et l'instabilite politique alimentent les tensions des annees 1920 et 1930. Le traite a donc stabilise temporairement l'Europe tout en préparant de futures contestations.",
    "On attend sanctions contre l'Allemagne, redessin des frontieres, role de la SDN et tensions durables.")],
C("La Grande Guerre est un conflit de masse et total dont le reglement de Versailles reste fragile.",
  "Guerre de position + violence de masse + mobilisation totale",
  "1914 Sarajevo · 1916 Verdun · 1918 armistice · 1919 Versailles",
  "Sarajevo~Declencheur~Alliances~Generalisation~Tranchees~Guerre de position~Verdun~Guerre d'usure~Armistice~11 novembre 1918",
  "Expliquer le declenchement|Depeindre la vie des soldats|Analyser la mobilisation totale|Situer les annees 1917 et 1918|Etudier le traite et ses suites",
  "Confondre 1918 et 1919|Reducer la guerre aux seuls soldats|Croire que Versailles satisfait l'Allemagne|Oublier la SDN",
  "Juin 1914~Sarajevo~1916~Verdun~1917~Etats-Unis et Russie~11 novembre 1918~Armistice~Juin 1919~Versailles",
  "Guerre de position~Tranchees et front fige~Guerre de mouvement~Avancees rapides~Guerre totale~Economie et civils mobilises~Guerre de masse~Millions de combattants",
  "Armistice~Arret des combats~Traite~Reglement juridique~Reparations~Paiements imposes~SDN~Cooperation internationale"))


# ============================================================ A13
add("A13", "La construction europeenne et ses enjeux", "Histoire-Géographie", ["Terminale"],
S("La construction europeenne commence apres 1945 dans un souci de paix et de reconstruction.|"
  "La CECA, creee en 1951 par le traite de Paris, met en commun le charbon et l'acier de six Etats.|"
  "Les traites de Rome de 1957 instituent la CEE et l'Euratom, avec l'objectif d'un marche commun.|"
  "Le marche interieur repose sur quatre libertes : circulation des marchandises, des services, des personnes et des capitaux.|"
  "Les institutions principales sont la Commission, le Parlement europeen, le Conseil, la Cour de justice et la Banque centrale europeenne.|"
  "Le traite de Maastricht, signe en 1992, cree l'Union europeenne et definit la citoyennete europeenne.|"
  "L'euro est lance comme monnaie unique en 1999 ; les billets et pieces circulent en 2002.|"
  "Le traite de Lisbonne, entre en vigueur en 2009, renforce les pouvoirs du Parlement et la representation exterieure.|"
  "L'Union s'est elargie a 27 Etats membres, notamment en 2004 et en 2007.|"
  "La politique agricole commune et la politique de cohesion figurent parmi les politiques communes les plus importantes.|"
  "L'Union doit faire face a des defis : le financement, les migrations, la securite, la transition ecologique et la concurrence mondiale.|"
  "Le depart du Royaume-Uni en 2020, ou Brexit, montre que l'integration europeenne reste un projet politique discute."),
[QC("Quel traite cree la CECA en 1951 ?", "Le traite de Rome~Le traite de Paris~Le traite de Maastricht~Le traite de Lisbonne", 1,
     "Le traite de Paris institue la Communaute europeenne du charbon et de l'acier."),
 QC("Quand les traites de Rome sont-ils signes ?", "1951~1957~1992~2009", 1,
     "Les traites de Rome de 1957 creent la CEE et l'Euratom."),
 QC("Combien de libertes fondent le marche interieur ?", "Deux~Trois~Quatre~Cinq", 2,
     "Marchandises, services, personnes et capitaux circulent librement."),
 QC("Quel traite cree officiellement l'Union europeenne ?", "Paris~Rome~Maastricht~Amsterdam", 2,
     "Le traite de Maastricht de 1992 fonde l'Union europeenne."),
 QC("Quelle institution represente directement les citoyens europeens ?", "La Commission~Le Parlement europeen~Le Conseil~La Cour de justice", 1,
     "Le Parlement europeen est elu au suffrage universel direct."),
 QC("En quelle annee l'euro entre-t-il en circulation sous forme de billets ?", "1992~1999~2002~2004", 2,
     "L'euro devient monnaie ecrite en 1999 et physique en 2002."),
 QC("Que designe le Brexit ?", "L'entree du Royaume-Uni dans l'UE~Le depart du Royaume-Uni de l'UE~La creation de l'euro~Un accord commercial", 1,
     "Le Royaume-Uni a quitte l'Union europeenne le 31 janvier 2020."),
 QT("Expliquer pourquoi les premiers projets europeens portent sur le charbon et l'acier.",
    "Apres 1945, le charbon et l'acier sont les ressources essentielles de la reconstruction et de l'industrie de guerre. Les mettre en commun entre la France, l'Allemagne, l'Italie et les pays du Benelux rend un nouveau conflit entre ces Etats materiellement difficile : on ne peut plus preparer une guerre sans que les partenaires le sachent. Le traite de Paris de 1951 cree ainsi une autorite commune independante. C'est une methode fonctionnaliste : l'integration commence par un secteur concret et concretise la reconciliation franco-allemande avant de s'etendre au marche commun en 1957.",
    "On attend la pertinence economique et strategique, la reconciliation et la methode functionaliste."),
 QT("Distinguer les roles de la Commission europeenne et du Parlement europeen.",
    "La Commission est l'organe executif de l'Union : elle propose les textes, veille a leur application et represente l'interet general europeen. Ses commissaires sont nommes puis approuves par le Parlement. Le Parlement, lui, represente les citoyens : il est elu tous les cinq ans, il amendent et vote les lois europeennes avec le Conseil, il controle la Commission et approuve le budget. Le Conseil represente les Etats membres. Ce systeme equilibre une logique intergouvernementale et une logique supra-nationale, ce qui explique que les decisions europeennes soient parfois longues a negocier.",
    "On attend proposition et execution pour la Commission, representation et controle pour le Parlement.")],
C("L'Union europeenne est une construction progressive qui articule marche commun, institutions et citoyennete.",
  "1951 CECA · 1957 CEE · 1992 UE · 1999 euro · 2009 Lisbonne",
  "4 libertes : marchandises · services · personnes · capitaux",
  "CECA~Charbon et acier~CEE~Marche commun~Maastricht~Union et citoyennete~Euro~Monnaie unique~Lisbonne~Institutions renforcees",
  "Situer les grandes dates|Expliquer la logique functionaliste|Identifier les institutions|Comprendre le marche interieur|Analyser les defis actuels",
  "Confondre CEE et UE|Placer l'euro en 1957|Oublier le role du Conseil|Reducer l'UE a un simple accord commercial",
  "1951~Traite de Paris~1957~Traités de Rome~1992~Maastricht~2002~Billets en euro~2020~Brexit",
  "Commission~Propose et execute~Parlement~Represente les citoyens~Conseil~Represente les Etats~Cour de justice~Tranche le droit",
  "Marche interieur~Quatre libertes~Politique agricole~PAC~Politique de cohesion~Solidarite territoriale~Citoyennete~Droits europeens"))


# ============================================================ A14
add("A14", "Present simple, present continuous and past simple", "Anglais", ["1re"],
S("The present simple describes habits, routines and general truths.|"
  "With he, she and it, the verb takes an s in the present simple.|"
  "Negatives and questions in the present simple use do or does plus the base form.|"
  "The present continuous describes an action in progress at the moment of speaking.|"
  "It is formed with the verb to be and the ing form of the main verb.|"
  "Signal words such as now, at the moment and today often introduce the present continuous.|"
  "The past simple describes a completed action at a definite time in the past.|"
  "Regular verbs add ed while irregular verbs have a specific past form, such as go went.|"
  "Questions and negatives in the past simple use did plus the base form.|"
  "Signal words such as yesterday, last week and in 2019 introduce the past simple.|"
  "Stative verbs like know, believe and own are rarely used in the continuous form.|"
  "Choosing the right tense is essential to describe a company, a current project and a past result."),
[QC("Which tense describes a habit or a routine ?", "Present continuous~Present simple~Past simple~Future perfect", 1,
     "The present simple is used for repeated actions and routines."),
 QC("How do you form the present continuous ?", "Do plus base form~Be plus ing form~Did plus base form~Have plus past participle", 1,
     "The present continuous is to be plus the present participle in ing."),
 QC("Which sentence is correct ?", "He go to school~He goes to school~He going to school~He gone to school", 1,
     "With he, she and it, the present simple verb ends in s."),
 QC("Which signal word introduces the past simple ?", "Now~At the moment~Yesterday~Always", 2,
     "Yesterday refers to a finished time, so the past simple is used."),
 QC("What is the past form of the irregular verb go ?", "Goed~Gone~Went~Going", 2,
     "Go is irregular : its past simple form is went."),
 QC("How do you make a question in the past simple ?", "Do you went~Did you go~Are you go~Have you go", 1,
     "Did is followed by the base form of the verb."),
 QC("Which verb is stative and rarely used in continuous form ?", "Run~Know~Write~Build", 1,
     "Know expresses a state, not an action in progress."),
 QT("Choose the correct tense and explain : The company (to grow) fast at the moment, but it (to start) in 2010.",
    "The first verb refers to an action in progress now, so the present continuous is required : the company is growing fast at the moment. The second verb refers to a completed action at a definite past time, given by in 2010, so the past simple is required : it started in 2010. The sentence becomes : The company is growing fast at the moment, but it started in 2010. The signal words at the moment and in 2010 confirm the choice. Using the present simple in the first clause would suggest a permanent routine rather than a current trend.",
    "The answer must give is growing for a current action and started for a dated past event, with the signal words."),
 QT("Write three sentences about your daily routine and explain the grammar used.",
    "I get up at seven o'clock every morning. I study management and economics at school. My sister works in a bank in Paris. All three sentences use the present simple because they describe repeated habits and stable situations. With my sister, the verb takes an s because the subject is third person singular. To make a negative sentence, I would say : I do not get up at seven. To ask a question, I would say : Do you study management ? The present simple gives information about what is generally true, not about what is happening right now.",
    "The answer should use the present simple, mention the third person s, and form a question with do or does.")],
C("The present simple states facts and habits, the present continuous shows an action in progress, the past simple dates a completed action.",
  "Present simple : base form (+ s with he/she/it)",
  "Present continuous : be + ing · past simple : ed or irregular form",
  "Present simple~Habits and facts~Takes an s~Present continuous~Action in progress~Be plus ing~Past simple~Completed action~Ed or irregular",
  "Identify the time of the action|Look for a signal word|Choose the right tense|Check the subject and the ending|Read the sentence aloud to check",
  "Using the present simple for an action in progress|Forgetting the s with he or she|Using did with a past participle|Confusing went and gone",
  "Every morning~I get up~Right now~The company is growing~Yesterday~It started~In 2010~Past simple~At the moment~Continuous",
  "Present simple~Routine and general truth~Present continuous~Temporary and in progress~Past simple~Finished and dated~Stative verb~Know, own, believe",
  "Regular verb~Add ed~Irregular verb~Go went~Question~Do or did plus base form~Negative~Do not or did not"))


# ============================================================ A15
add("A15", "Expressing opinions and structuring an argument in English", "Anglais", ["1re", "Terminale"],
S("Expressing an opinion means stating a personal point of view and supporting it with reasons.|"
  "Simple opinion markers include I think, I believe, in my view and as far as I am concerned.|"
  "To give a balanced view, writers use hedging such as may, might, perhaps and it seems that.|"
  "Linking words organise an argument : first, moreover, however, therefore and in conclusion.|"
  "Contrast is expressed with but, although, whereas and on the other hand.|"
  "Cause and consequence are marked with because, since, as a result and consequently.|"
  "Agreeing can be expressed with I agree with you and that is true, while disagreeing uses I am not sure I agree.|"
  "A strong argument gives a claim, a reason, an example and a short conclusion.|"
  "In a debate, each speaker answers the previous point before developing a new one.|"
  "Persuasive language uses rhetorical questions, repetition and emotive words.|"
  "An email or a report should keep a polite and professional tone.|"
  "The quality of an argument depends on clear structure, relevant evidence and accurate language."),
[QC("Which phrase introduces a personal opinion ?", "In my view~As a result~On the other hand~In conclusion", 0,
     "In my view introduces the speaker's point of view."),
 QC("Which word introduces a contrast ?", "Moreover~However~Therefore~Because", 1,
     "However signals a contrast or a concession."),
 QC("What is a hedging expression ?", "A strong command~A cautious expression such as might~A concluding sentence~A question", 1,
     "Hedging reduces the strength of a claim and makes it more nuanced."),
 QC("How do you politely disagree ?", "You are completely wrong~I am not sure I agree~No, never~That is false", 1,
     "I am not sure I agree is a polite disagreement formula."),
 QC("Which structure makes a complete argument ?", "Claim, reason, example, conclusion~Example only~Opinion only~Question only", 0,
     "A full argument states a claim, justifies it, illustrates it and closes it."),
 QC("Which expression shows a consequence ?", "Although~Whereas~Consequently~Firstly", 2,
     "Consequently introduces the result of a previous statement."),
 QC("What does a rhetorical question do ?", "Ask for information~Persuade by involving the reader~End a letter~Give a date", 1,
     "A rhetorical question does not expect an answer but persuades the reader."),
 QT("Write a short argument in English about the benefits of vocational training, with a claim, a reason, an example and a conclusion.",
    "In my view, vocational training is a valuable pathway for students. First, it combines theoretical knowledge with practical skills, which makes learning more meaningful. For example, a student in a business class can apply accounting concepts during a work placement in a company. Moreover, this type of training helps young people understand the expectations of the professional world. However, it requires good cooperation between schools and employers. Therefore, I believe vocational training should be developed, provided that the quality of placements is carefully monitored.",
    "The answer should contain an opinion marker, a reason, a concrete example, a contrast and a conclusion."),
 QT("Rewrite these direct statements in a more polite and nuanced way : Companies do not train enough. Young people are lazy.",
    "A more balanced version could be : It seems that some companies could invest more in training, especially for young employees. As far as young people are concerned, it may be unfair to generalise : many students are highly motivated but lack clear guidance. The original statements are too categorical and risk offending the reader. Hedging expressions such as it seems, could and may be soften the claims, and precise subjects such as some companies avoid unfair generalisation. A professional email should remain factual and respectful even when it criticises a situation.",
    "The answer should use hedging, avoid generalisation and keep a professional tone.")],
C("A good argument in English states a view, supports it, considers objections and concludes clearly.",
  "Claim + reason + example + conclusion",
  "Opinion markers · hedging · contrast · consequence",
  "In my view~Opinion marker~However~Contrast~Moreover~Addition~Therefore~Consequence~Hedging~Cautious wording",
  "State your opinion clearly|Give a reason with because or since|Illustrate with a concrete example|Answer a possible objection|Conclude with a balanced judgement",
  "Making categorical statements without evidence|Using however as a simple addition|Forgetting to answer the objection|Mixing formal and very informal language",
  "Vocational training~Claim~Work placement~Example~Some companies~Hedging~It seems that~Nuance~Therefore~Conclusion",
  "For and against~Balanced view~Only for~One-sided view~Hedging~Cautious claim~Strong claim~Categorical statement",
  "Linking words~Structure the argument~Rhetorical question~Persuade~Tone~Politeness and professionalism~Evidence~Concrete support"))


# ============================================================ A16
add("A16", "Business and work vocabulary in context", "Anglais", ["Terminale"],
S("A company can be described by its name, its headquarters, its activities and its size.|"
  "A turnover is the total value of sales over a period, while a profit is what remains after costs.|"
  "Employees work for an employer ; a manager is in charge of a team or a department.|"
  "Common departments include human resources, finance, marketing, sales, production and IT.|"
  "A job title gives the position, such as sales manager, accountant or receptionist.|"
  "Recruitment includes writing a job advertisement, interviewing candidates and signing a contract.|"
  "A meeting has an agenda, minutes, a chairperson and decisions to follow up.|"
  "A deadline is the date by which a task must be finished.|"
  "An invoice is a document requesting payment ; a supplier delivers goods to a client.|"
  "To negotiate means to discuss terms in order to reach an agreement.|"
  "Business emails use a subject line, a greeting, a clear request and a polite closing formula.|"
  "Professional vocabulary must be precise because a small word error can change the meaning of a contract."),
[QC("What is a turnover ?", "The profit of a company~The total value of sales~The number of employees~The price of a share", 1,
     "Turnover is the total value of sales during a given period."),
 QC("Who is in charge of a team ?", "A client~A manager~A supplier~An invoice", 1,
     "A manager supervises a team or a department."),
 QC("Which department recruits and trains staff ?", "Finance~Human resources~Production~IT", 1,
     "Human resources manages recruitment, training and employment relations."),
 QC("What does a deadline mean ?", "A meeting room~The date by which a task must be done~A job contract~A payment method", 1,
     "A deadline is the final date for completing a task."),
 QC("Who sends an invoice ?", "The client to the supplier~The supplier to the client~The employee to the manager~The bank to the state", 1,
     "The supplier bills the client for goods or services."),
 QC("What is the purpose of a meeting agenda ?", "To pay the staff~To list the points to discuss~To close a contract~To write an invoice", 1,
     "The agenda fixes the order of the points to be discussed."),
 QC("Which closing formula is appropriate in a business email ?", "See you later, dude~Kind regards~Bye bye~Later", 1,
     "Kind regards is a standard polite closing in professional emails."),
 QT("Describe a company using at least six vocabulary items from this chapter.",
    "Our company is a mid-sized firm specialising in logistics. Its headquarters are in Lyon and it employs about 250 people. The main departments are operations, finance, human resources and IT. Its turnover reached twelve million euros last year and the profit was modest because of rising fuel costs. The human resources department is currently recruiting three accountants and a sales manager. The finance department sends invoices to clients each month and negotiates payment terms with suppliers. Every Monday, the managers hold a meeting with a short agenda and written minutes.",
    "The answer should use precise business words : headquarters, employees, departments, turnover, profit, recruitment, invoice, negotiate, agenda."),
 QT("Explain why precision matters in professional English and give two examples of confusion to avoid.",
    "In a professional context, a word error can change a commitment or a legal obligation. For example, confusing a quotation with an invoice can make a client believe that payment is already due when only a price estimate has been sent. In the same way, mixing up a client and a supplier reverses the direction of the transaction and can cause a serious misunderstanding in a contract. Precision also matters in dates and deadlines : by Monday and until Monday do not mean exactly the same thing. That is why professional writing uses short sentences, clear subjects and standard formulas, and why it is reread before being sent.",
    "The answer should explain the professional risk and give two concrete vocabulary confusions.")],
C("Professional English relies on precise vocabulary for companies, jobs, documents and meetings.",
  "Company = activities + departments + turnover + employees",
  "Invoice is sent by the supplier · deadline is a date · agenda lists meeting points",
  "Turnover~Total sales~Profit~Sales minus costs~Employee~Works for a company~Manager~In charge of a team~Invoice~Request for payment",
  "Identify the company and its activity|Name the relevant department|Choose the precise job title|Use the right document word|Check tone and closing formula",
  "Confusing turnover and profit|Sending a quotation instead of an invoice|Using informal greetings in an email|Confusing client and supplier",
  "Logistics firm~250 employees~Departments~Operations and finance~Turnover~12 million euros~Recruitment~Three accountants~Meeting~Agenda and minutes",
  "Turnover~All sales~Profit~What remains after costs~Quotation~Estimated price~Invoice~Request for payment",
  "Supplier~Delivers goods~Client~Receives goods~Employee~Works in the company~Employer~Hires the employee"))


# ============================================================ A17
add("A17", "Les valeurs de la Republique et la citoyennete", "EMC", ["1re"],
S("La Republique francaise a pour devise liberte, egalite, fraternite, proclamee par la Revolution de 1789.|"
  "La liberte garantit a chacun la possibilite d'agir et de s'exprimer dans le respect d'autrui.|"
  "L'egalite signifie que tous les citoyens sont egaux devant la loi, sans privilege de naissance.|"
  "La fraternite exprime la solidarite entre les membres de la communaute nationale.|"
  "La souverainete nationale appartient au peuple, qui l'exerce par son vote et ses representants.|"
  "La democratie repose sur le suffrage universel, la séparation des pouvoirs et l'Etat de droit.|"
  "La laicite garantit la liberte de conscience et la neutralite de l'Etat.|"
  "Etre citoyen, c'est jouir de droits mais aussi respecter des devoirs, comme le respect de la loi et des autres.|"
  "Le vote est un droit et un devoir civique : il legitimise les decisions politiques.|"
  "L'engagement associatif, le volontariat et la participation locale sont des formes de citoyennete active.|"
  "Les principes de 1789 sont defendus par la Constitution et par les traites europeens.|"
  "Les valeurs republicaines s'apprennent et se transmettent par l'ecole, la famille et les medias."),
[QC("Quelle est la devise de la Republique francaise ?", "Liberte, egalite, fraternite~Paix, travail, patrie~Unite, force, prosperite~Justice, ordre, securite", 0,
     "La devise republicaine est heritee de 1789."),
 QC("Que signifie l'egalite devant la loi ?", "Tous les citoyens ont les memes droits~Tout le monde a le meme salaire~Les privileges sont maintenus~La loi change pour chacun", 0,
     "L'egalite juridique supprime les privileges et garantit les memes droits."),
 QC("Qui detient la souverainete nationale ?", "Le President seul~Le peuple~Le Conseil constitutionnel~Les prefets", 1,
     "La Constitution affirme que la souverainete appartient a la nation."),
 QC("Quel princips garantit la liberte de conscience ?", "La laicite~La censure~Le droit divin~La monarchie", 0,
     "La laicite protege la liberte de croire ou de ne pas croire."),
 QC("Quel est un devoir du citoyen ?", "Respecter la loi~Choisir sa religion imposee~Refuser de voter~Ignorer les autres", 0,
     "Le respect de la loi et d'autrui est un devoir civique essentiel."),
 QC("Que legitimise le vote ?", "La force~Les decisions politiques~La propriete~La religion", 1,
     "Le suffrage donne au pouvoir sa legitimite democratique."),
 QC("Quelle forme de citoyennete active peut-on citer ?", "L'engagement associatif~L'isolement~Le refus des regles~La seule consommation", 0,
     "S'engager dans une association ou un volontariat participe a la vie collective."),
 QT("Expliquer le lien entre liberte et egalite dans les valeurs republicaines.",
    "La liberte permet a chacun d'agir, de penser et de s'exprimer. Mais une liberte sans egalite serait reservee a ceux qui ont le plus de moyens : par exemple, la liberte d'expression n'a de sens que si chacun peut reellement prendre la parole. L'egalite devant la loi garantit a tous les memes droits et les memes protections, ce qui rend la liberte effective pour tous. Les deux principes se completent : la liberte donne la possibilite d'agir et l'egalite en assure l'acces a chacun. La fraternite vient rappeler que cette liberte et cette egalite s'exercent dans le respect des autres et la solidarite.",
    "On doit montrer la complementarite des trois valeurs et donner un exemple concret."),
 QT("Comment la laicite contribue-t-elle a la liberte de conscience ?",
    "La laicite separe les Eglises et l'Etat, comme le fait la loi de 1905. L'Etat ne impose aucune religion et garantit a chacun la liberte de croire ou de ne pas croire. Les agents publics sont neutres dans l'exercice de leur fonction, ce qui assure un traitement egal des usagers, quelle que soit leur conviction. A l'ecole, la laicite protege les eleves des pressions religieuses et permet un debat serein. Elle ne supprime pas les croyances : elle les rend compatibles avec la vie commune et le respect d'autrui. C'est donc une condition de la liberte de conscience et de l'egalite des citoyens.",
    "On attend separation, neutralite, liberte de croire ou non et lien avec l'egalite.")],
C("Les valeurs republicaines forment un ensemble : liberte, egalite, fraternite guident la vie collective.",
  "Liberte + egalite + fraternite = pacte republicain",
  "Souverainete nationale · democratie · laicite · droits et devoirs",
  "Liberte~Agir et s'exprimer~Egalite~Egaux devant la loi~Fraternite~Solidarite~Laicite~Neutralite de l'Etat~Citoyennete~Droits et devoirs",
  "Definir les trois mots de la devise|Relier les valeurs aux principes de 1789|Identifier les droits et les devoirs|Donner des exemples de participation|Expliquer la laicite dans la vie quotidienne",
  "Croire que la liberte est sans limites|Confondre laicite et intolerance|Oublier les devoirs du citoyen|Reducer la citoyennete au seul vote",
  "Devise~Liberte egalite fraternite~Vote~Legitimite democratique~Association~Citoyennete active~Ecole~Transmission des valeurs~Laicite~Liberte de conscience",
  "Droits~Ce que l'Etat garantit~Devoirs~Ce que le citoyen respecte~Citoyennete passive~Recevoir des droits~Citoyennete active~Participer et s'engager",
  "Egalite~Memes droits pour tous~Equite~Traitement adapté aux situations~Liberte~Possibilite d'agir~Fraternite~Solidarite et respect"))


# ============================================================ A18
add("A18", "Laicite, liberte d'expression et respect d'autrui", "EMC", ["Terminale"],
S("La laicite repose sur la separation des Eglises et de l'Etat, inscrite dans la loi du 9 decembre 1905.|"
  "Elle garantit la liberte de culte et l'egalite de tous devant la loi, quelles que soient les convictions.|"
  "L'Etat est neutre : il ne finance pas de culte et ne reconnait aucune religion officielle.|"
  "Les agents publics sont tenus a une obligation de neutralite dans l'exercice de leurs fonctions.|"
  "A l'ecole, la laicite permet aux eleves de croire ou de ne pas croire sans pression.|"
  "La liberte d'expression est un droit fondamental reconnu par la Declaration des droits de l'homme et la Convention europeenne des droits de l'homme.|"
  "Ce droit n'est pas absolu : la loi punit la diffamation, l'injure, la provocation a la haine et l'apologie de crimes.|"
  "Le respect d'autrui suppose de distinguer la critique d'une idee de l'attaque contre une personne.|"
  "Le debat contradictoire permet de confronter des opinions dans le cadre de regles communes.|"
  "Sur les reseaux sociaux, la rapidite de diffusion augmente la responsabilite de chacun.|"
  "Le harcelement et la propagation de rumeurs portent atteinte a la dignite des personnes.|"
  "Une societe laique et democratique demande de la tolérance, de l'esprit critique et du respect des lois."),
[QC("Quelle loi fonde la separation des Eglises et de l'Etat en France ?", "La loi du 9 decembre 1905~La Constitution de 1958~La loi de 1882 sur l'ecole~Le Code civil de 1804", 0,
     "La loi de separation du 9 decembre 1905 est le texte de reference."),
 QC("Quelle est une limite legale a la liberte d'expression ?", "La critique d'un texte~La provocation a la haine~Le debat politique~La publication d'un avis", 1,
     "La provocation a la haine et l'injure sont des delits de la presse."),
 QC("Qui est soumis a une obligation de neutralite ?", "Tous les citoyens~Les agents publics dans leurs fonctions~Les eleves~Les journalistes", 1,
     "Les agents publics representent l'Etat et doivent rester neutres."),
 QC("La laicite garantit ...", "L'imposition d'une religion~La liberte de croire ou de ne pas croire~L'interdiction des debats~La supremacy d'un culte", 1,
     "La liberte de conscience est au coeur de la laicite."),
 QC("Quelle attitude respecte le debat contradictoire ?", "Refuser d'ecouter l'adversaire~Repondre avec des arguments~Insulter~Couper la parole", 1,
     "On confronte les arguments dans le respect des regles du debat."),
 QC("Pourquoi les reseaux sociaux demandent-ils plus de prudence ?", "Parce qu'ils sont lents~Parce que la diffusion est rapide et durable~Parce qu'ils sont interdits~Parce qu'ils sont gratuits", 1,
     "Une publication peut etre vue et conservée rapidement par un grand public."),
 QC("Que faut-il distinguer dans une critique ?", "La personne et l'idee~Le jour et l'heure~Le droit et le devoir~L'ecole et la famille", 0,
     "Critiquer une idee est permis ; attaquer une personne est different."),
 QT("Expliquer pourquoi la liberte d'expression n'est pas un droit absolu.",
    "La liberte d'expression est garantie mais son exercice peut etre limite par la loi pour proteger d'autres droits, comme la dignite des personnes, l'honneur, la vie privee et l'ordre public. Ainsi, la diffamation, l'injure publique, la provocation a la haine ou l'apologie du terrorisme sont des delits : elles ne sont pas de simples opinions. Les limites doivent etre necessaires et proportionnees, comme le rappellent les textes internationaux. Cette notion de limite ne nie pas la liberte : elle permet a chacun d'exercer son droit sans détruire celui des autres. Un debat democratique suppose precisement ces regles communes.",
    "On doit citer des delits, rappeler la protection d'autres droits et la notion de proportionnalite."),
 QT("Comment concilier laicite et respect des convictions dans un college ?",
    "L'etablissement est neutre : il n'enseigne aucune religion et n'impose aucun signe d'appartenance aux eleves dans le cadre des cours. Les élèves peuvent avoir des convictions differentes et les exprimer dans le respect des autres, par exemple dans un debat sur l'histoire des religions. Les agents publics, eux, doivent rester neutres. Les reglements interdisent le proselytisme et le harcelement, mais permettent un enseignement factuel et comparatif. La laicite n'efface pas les croyances : elle garantit un espace commun ou chacun peut garder ses convictions sans faire pression sur les autres. Le dialogue et l'esprit critique sont les outils de cette coexistence.",
    "On attend neutralite de l'institution, liberte des eleves, interdiction du proselytisme et respect d'autrui.")],
C("Laicite et liberte d'expression protegent la liberte de chacun en encadrant les atteintes a autrui.",
  "Liberte d'expression + limites legales = debat democratique",
  "1905 separation · neutralite des agents publics · respect de la dignite",
  "Loi de 1905~Separation des Eglises et de l'Etat~Neutralite~Agents publics~Liberte d'expression~Droit fondamental~Limites~Diffamation et injure~Respect~Dignite d'autrui",
  "Definir la laicite et son histoire|Identifier les droits de la personne|Connaitre les limites legales|Analyser une situation de debat|Respecter les regles de la discussion",
  "Confondre laicite et athéisme d'Etat|Croire que tout est permis au nom de la liberte|Oublier la neutralite des agents publics|Generaliser a partir d'un cas isole",
  "9 decembre 1905~Loi de separation~Agent public~Neutralite~Réseaux sociaux~Diffusion rapide~Injure~Delit de presse~Debat~Arguments et respect",
  "Liberte d'expression~Droit fondamental~Censure~Interdiction prealable~Limite~Delit apres publication~Respect d'autrui~Dignite",
  "Croire~Conviction personnelle~Savoir~Connaissance verifiee~Opinion~Jugement discutable~Fait~Realite constatable"))


# ============================================================ A19
add("A19", "Lire un sujet et respecter les consignes", "Méthodologie", ["1re"],
S("Avant d'ecrire, il faut lire le sujet entirement et ne rien sauter.|"
  "La premiere etape consiste a identifier le type d'exercice : commentaire, dissertation,analyse de document ou synthèse.|"
  "Les mots de la commande, comme expliquer, comparer, justifier ou analyser, determinant la tache a realiser.|"
  "Les mots cles delimitent le champ du sujet et doivent etre definis.|"
  "Il faut distinguer les mots qui sont dans le sujet de ceux qu'on aimerait y mettre.|"
  "Une consigne peut porter sur la longueur, le nombre d'exemples, le plan ou le format attendu.|"
  "Les exemples demandes doivent etre pertinents et tires du programme.|"
  "On reformule le sujet avec ses propres mots pour verifier qu'il est bien compris.|"
  "La problematique se construit en reliant les termes en tension du sujet.|"
  "Un brouillon rapide permet de repartir les idees avant la redaction.|"
  "La gestion du temps impose de reserver une phase de relecture pour l'orthographe et la ponctuation.|"
  "Rendre une copie propre, datée et completement traitee est une exigence de la evaluation."),
[QC("Que fait-on en premier devant un sujet ?", "On ecrit directement~On lit le sujet entierement~On cherche la conclusion~On copie un exemple", 1,
     "Une lecture complete evite les contre-sens et les oublis de consignes."),
 QC("Qu'appelle-t-on mots de la commande ?", "Les verbes qui indiquent la tache~Les noms propres~Les dates~Les exemples", 0,
     "Expliquer, comparer ou justifier indiquent ce qu'il faut faire."),
 QC("A quoi sert de definir les mots cles ?", "A remplir la copie~A delimiter le champ du sujet~A eviter la conclusion~A choisir la police", 1,
     "La definition cadre le raisonnement et evite la digression."),
 QC("Que faut-il faire des consignes de forme ?", "Les ignorer~Les respecter~Les réécrire~Les discuter", 1,
     "Longueur, plan et format font partie de la consigne."),
 QC("Pourquoi reformuler le sujet ?", "Pour le rendre plus court~Pour verifier sa comprehension~Pour changer de sujet~Pour gagner du temps", 1,
     "La reformulation est un test de comprehension du sujet."),
 QC("Quel outil aide a repartir les idees avant la redaction ?", "Une carte mentale ou un brouillon~Une calculatrice~Un dictionnaire seul~La fin de la copie", 0,
     "Le brouillon organise les arguments avant la mise au propre."),
 QC("Que faut-il reserver en fin d'epreuve ?", "Une phase de relecture~Un nouveau sujet~Une pause sans controle~Une page blanche", 0,
     "La relecture permet de corriger orthographe, ponctuation et oublis."),
 QT("Decrire une methode en six etapes pour traiter un sujet d'examen.",
    "On lit d'abord le sujet en entier, puis on souligne les mots de la commande et les mots cles. On identifie ensuite le type d'exercice et les consignes de forme. On definit les termes importants et on releve les tensions qui permettront de poser une problematique. On cherche alors des exemples précis tires du cours et on les repartit dans un plan provisoire. On redige en soignant les transitions et en répondant a chaque question du sujet. On termine par une relecture attentive de l'orthographe, de la ponctuation et de la présentation de la copie.",
    "On attend lecture, identification de la commande, definition, problematique, plan et relecture."),
 QT("Un sujet demande : en quoi la gestion de projet contribue-t-elle a la performance de l'entreprise ? Analyse les consignes implicites.",
    "Le verbe en quoi appelle une analyse de contribution, pas une simple description. Les mots cles sont gestion de projet et performance : il faut les definir, par exemple la conduite d'un projet de sa conception a sa livraison, et la capacite de l'entreprise a atteindre ses objectifs. Il faut montrer un lien de causalite : la clarification des objectifs, la repartition des taches, le suivi des delais et la conduite du changement reduisent les retards et les couts. Le plan peut distinguer la performance organisationnelle, la performance economique et la performance humaine. Les exemples doivent etre tires du cours de management et rattaches a chaque partie.",
    "On attend l'analyse du verbe, la definition des termes, le lien de causalite et des exemples tires du programme.")],
C("Traiter un sujet, c'est d'abord le lire et le decouper avant toute redaction.",
  "Commande + mots cles + consignes = cadre de reponse",
  "Lire · souligner · definir · problematiser · planifier · rediger · relire",
  "Commande~Verbe de la tache~Mots cles~Champ du sujet~Consigne~Format attendu~Reformulation~Test de comprehension~Brouillon~Organisation",
  "Lire le sujet en entier|Souligner la commande et les mots cles|Definir les termes et poser la question|Rechercher des exemples et construire un plan|Rediger puis relire la copie",
  "Repondre avant d'avoir lu les consignes|Confondre le sujet avec un autre|Inventer des exemples hors programme|Negliger la relecture finale",
  "En quoi~Analyse de contribution~Expliquer~Mise en relation~Comparer~Recherche de differences~Justifier~Argument a l'appui~Analyse~Decomposition du reel",
  "Sujet et consignes~Ce qui est demande~Hors sujet~Ce qu'on aimerait traiter~Commande~Ce qu'il faut faire~Exemple~Ce qui illustre",
  "Brouillon~Repartition des idees~Copie~Rédaction propre~Relecture~Correction finale~Problematique~Question centrale"))


# ============================================================ A20
add("A20", "Synthese de documents et note de synthese", "Méthodologie", ["Terminale"],
S("Une synthese de documents consiste a reunir l'information essentielle de plusieurs textes en un seul developpement.|"
  "La consigne precise le nombre de documents, la longueur attendue et le theme a traiter.|"
  "Il faut lire chaque document en identifiant l'auteur, la date, le type et l'idee centrale.|"
  "Une lecture active releve les arguments, les chiffres et les exemples utiles.|"
  "Les documents peuvent se completer, se contredire ou proposer des points de vue differents.|"
  "Le croisement des sources permet de degager les points communs et les divergences.|"
  "Le plan de synthese est generalement thematic, parfois compare ou chronologique.|"
  "La synthese doit rester objective : on rapporte ce que disent les documents sans imposer son opinion.|"
  "Les verbes de synthese comme selon, d'apres, souligner ou estiment introduisent les informations.|"
  "Chaque affirmation importante est attibuee a sa source pour eviter le plagiat.|"
  "L'introduction presente le theme et les documents ; la conclusion fait le bilan sans ajouter d'avis personnel.|"
  "La qualite d'une synthese tient a la selection, a la clarte du plan et a la concision."),
[QC("Quel plan est le plus courant pour une synthese ?", "Chronologique~Thematique~Alphabetique~Au hasard", 1,
     "Le plan thematique regroupe les informations par grandes idees."),
 QC("Que doit faire une synthese avec les contradictions entre documents ?", "Les ignorer~Les mentionner et les expliquer~Les inventer~Choisir un seul document", 1,
     "Les divergences font partie de l'information a restituer."),
 QC("Quel verbe introduit une information attribuee a un auteur ?", "Selon~Donc~Cependant~En revanche", 0,
     "Selon ou d'apres marquent la provenance de l'information."),
 QC("La synthese doit-elle exprimer l'avis personnel du candidat ?", "Oui, toujours~Non, elle reste objective~Uniquement en conclusion~Uniquement en introduction", 1,
     "On restitue les documents sans ajouter son propre jugement."),
 QC("Que contient l'introduction d'une synthese ?", "La conclusion~Le theme et la presentation des documents~Les chiffres~Une opinion", 1,
     "Elle situe le sujet et presente les documents a croiser."),
 QC("Comment eviter le plagiat ?", "En recopiant tout~En attribuant chaque idee a sa source~En changeant seulement la police~En supprimant les noms d'auteurs", 1,
     "On cite ou on attribue les idees empruntees aux documents."),
 QC("Que faut-il selectionner dans un document ?", "Toutes les phrases~Les informations utiles au theme~Les seules opinions~Uniquement les dates", 1,
     "Une synthese selectionne et condense, elle ne recopie pas."),
 QT("Decrire la demarche de realisation d'une note de synthese en cinq etapes.",
    "On lit d'abord la consigne pour connaitre le theme, le nombre de documents et la longueur. On analyse ensuite chaque document en relevant son auteur, sa date, son type et ses idees principales dans une fiche de lecture. On croise alors les informations pour identifier les points communs, les complementarites et les divergences. On construit un plan thematique equilibre en repartissant les sources dans chaque partie. On redige enfin avec des verbes de synthese et des attributions precisent, puis on relit pour verifier l'objectivite, la concision et l'absence de plagiat.",
    "On attend lecture de la consigne, analyse des documents, croisement, plan et redaction objective."),
 QT("Comment traiter deux documents qui s'opposent sur la meme question ?",
    "Il ne faut pas choisir arbitrairement le document qui parait avoir raison. On presente d'abord le point de vue du premier auteur avec ses arguments et ses preuves, en l'attribuant clairement. On expose ensuite la position opposee avec la meme neutralite. On peut alors montrer ce qui explique le desaccord : une date différente, un terrain d'etude different, une definition divergente du probleme ou des interets distincts. On termine par un bilan qui indique ce que les deux documents apportent ensemble et ce qui reste discute. La synthese conserve ainsi la trace du debat tout en restant objective.",
    "On doit presenter les deux positions, expliquer le desaccord et conclure par un bilan neutre.")],
C("Une synthese selectionne et croise les informations de plusieurs documents dans un plan clair et objectif.",
  "Synthese = selection + croisement + plan thematique + objectivite",
  "Selon · d'apres · souligne · estiment : verbes d'attribution",
  "Consigne~Cadre de travail~Document~Source a analyser~Croisement~Points communs et divergences~Plan thematique~Grandes idees~Objectivite~Neutralite",
  "Lire la consigne et identifier le theme|Analyser chaque document et ses idees|Croiser les sources et relever les divergences|Construire un plan thematique|Rediger avec attribution et relire",
  "Recopier des phrases entieres|Donner son propre avis|Ignorer un document|Melanger les sources sans les attribuer",
  "Deux documents~Points de vue opposes~Selon~Attribution~Date différente~Explication du desaccord~Bilan~Synthèse neutre~Verbe de synthese~Concision",
  "Synthese~Information condensee~Resume~Texte plus court~Commentaire~Analyse personnelle~Plagiat~Copie sans attribution",
  "Points communs~Convergences~Divergences~Desaccords~Complementarite~Informations qui s'ajoutent~Contradiction~Informations qui s'opposent"))


# FIN DU LOT A
valider_et_ecrire(F, "stmg-mat-part-A.json")
