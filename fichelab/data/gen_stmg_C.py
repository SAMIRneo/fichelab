# -*- coding: utf-8 -*-
"""Generateur stmg-mat-part-C.json — lot C : numerique, mathematiques appliquees, anglais professionnel et complements (20 fiches).

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

add = lambda *a: F.append(build(*a))


# ============================================================ C01
add("C01", "Algorithmique et resolution de problemes", "Numerique", ["1re"],
S("Un algorithme est une suite finie et ordonnee d'instructions permettant de resoudre un probleme ou d'effectuer une tache.|"
  "Une variable est un emplacement memoire designe par un nom et contenant une valeur qui peut changer.|"
  "On represente souvent un algorithme par un schema logique : debut, traitements, decision et fin.|"
  "Le schema logique utilise des formes convenues : ovale pour le debut, rectangle pour un traitement, losange pour un test.|"
  "Une structure sequence execute les instructions les unes apres les autres, dans un ordre determine.|"
  "Une structure conditionnelle, si alors sinon, choisit une branche selon la verite d'une condition.|"
  "Une boucle repete un bloc d'instructions : la boucle pour quand le nombre de tours est connu.|"
  "La boucle tant que repete un bloc jusqu'a ce qu'une condition devienne fausse, sans nombre de tours fixe.|"
  "Un algorithme doit etre general : il traite toutes les donnees d'entree possibles, pas seulement un exemple particul|"
  "La terminaison est une propriete essentielle : chaque boucle doit conduire a la fin de l'algorithme.|"
  "Les donnees d'entree sont les informations fournies ; les donnees de sortie sont les resultats produits.|"
  "Avant de programmer, on analyse le probleme, on decompose la tache et on valide l'algorithme par des tests."),
[QC("Qu'est-ce qu'un algorithme ?", "Une suite finie et ordonnee d'instructions~Un langage de programmation~Un schema de base de donnees~Un reseau informatique", 0,
     "Un algorithme est une procedure finie et ordonnee, independante d'un langage donne."),
 QC("Dans un schema logique, le losange represente ...", "Un traitement~Une decision~La fin~Une affectation", 1,
     "Le losange porte le test ou la condition, avec deux branches de sortie."),
 QC("Quelle structure repete un bloc un nombre connu de fois ?", "La sequence~La boucle pour~La condition simple~L'affectation", 1,
     "La boucle pour utilise un compteur dont la borne est connue a l'avance."),
 QC("Une boucle tant que s'arrete lorsque ...", "La condition devient fausse~Le compteur atteint 10~La variable est vide~On change de langage", 0,
     "La repetition continue tant que la condition est vraie et s'arrete quand elle devient fausse."),
 QC("Que garantit la terminaison d'un algorithme ?", "Qu'il affiche un resultat~Qu'il s'arrete toujours~Qu'il utilise peu de memoire~Qu'il est ecrit en Python", 1,
     "Un algorithme terminating doit toujours parvenir a sa fin, quelle que soit l'entree conforme."),
 QC("Une variable est ...", "Un emplacement nomme contenant une valeur~Une instruction de sortie~Un type de boucle~Un fichier de donnees", 0,
     "La variable possede un nom, un type et une valeur que l'on peut modifier par affectation."),
 QC("Pour valider un algorithme, on utilise notamment ...", "Des cas limites~Le seul hasard~Une unique valeur~La couleur du schema", 0,
     "Les cas limites, comme une liste vide ou une valeur extreme, revelent les defauts de logique."),
 QT("Decrire la demarche pour construire un algorithme qui calcule la moyenne de n notes saisies au clavier.",
    "On identifie d'abord les donnees d'entree : le nombre n puis les n notes. On initialise une variable somme a zero. On utilise une boucle pour avec un compteur i allant de 1 a n : a chaque tour, on lit une note et on l'ajoute a somme. A la sortie de la boucle, on calcule moyenne = somme / n puis on affiche le resultat. Il faut prevoir le cas n = 0 pour eviter une division par zero. On teste ensuite avec n = 3 et les notes 10, 12 et 14 : somme = 36 et moyenne = 12, ce qui valide l'algorithme.",
    "On attend l'identification des entrees, l'initialisation, la boucle pour avec cumul, le calcul final, le cas n nul et un test chiffre."),
 QT("Expliquer la difference entre boucle pour et boucle tant que, et donner un exemple pour chacune.",
    "La boucle pour convient quand le nombre d'iterations est connu avant de commencer : par exemple parcourir les douze mois de l'annee ou les lignes d'un tableau dont on connait la taille. Son compteur est initialise, teste et incremente automatiquement. La boucle tant que convient quand l'arret depend d'une condition observable pendant l'execution : par exemple lire des notes jusqu'a rencontrer la valeur 0 utilisee comme indicateur de fin. Le risque est que la condition ne devienne jamais fausse : il faut donc modifier au moins une variable testee a chaque tour. Dans les deux cas, on dessine le schema logique avant d'ecrire le code.",
    "On doit opposer nombre d'iterations connu et arret conditionnel, donner un exemple de chaque cote et signaler le risque de non-terminaison.")],
C("Un algorithme est une suite finie d'instructions : on analyse le probleme, on choisit les structures, puis on teste.",
  "Algorithme = donnees d'entree + traitements + donnees de sortie",
  "Sequence · condition si/sinon · iteration pour ou tant que",
  "Variable~Emplacement nomme~Contient une valeur~Affectation~Donne une valeur~Remplace l'ancienne~Condition~Test vrai ou faux~Choisit une branche",
  "Analyser le probleme et les donnees|Decomposer la tache en etapes|Choisir les structures adaptees|Ecrire le schema logique|Tester avec des cas limites",
  "Oublier d'initialiser une variable|Ecrire une boucle qui ne s'arrete pas|Confondre condition et affectation|Ne tester qu'un seul exemple",
  "Entree~Donnee fournie au depart~Traitement~Operation realisee~Sortie~Resultat affiche~Compteur~Variable de boucle~Test~Condition a verifier",
  "Sequence~Instructions dans l'ordre~Aucun choix~Une seule execution~Condition~Test de verite~Deux branches~Choix exclusif",
  "Boucle pour~Nombre de tours connu~Compteur~Exemple : 12 mois~Boucle tant que~Arret selon condition~Pas de borne fixe~Exemple : lire jusqu'a zero"))


# ============================================================ C02
add("C02", "Le tableur : cellules, formules et references", "Numerique", ["1re"],
S("Un tableur est un logiciel de traitement de donnees organisees en lignes et en colonnes.|"
  "Chaque cellule est designee par une adresse : la lettre de la colonne suivie du numero de la ligne, par exemple B4.|"
  "Une cellule peut contenir du texte, un nombre, une date ou une formule.|"
  "Une formule commence toujours par le signe egal et utilise des operateurs ou des fonctions.|"
  "Une reference relative, comme A1, s'adapte lorsqu'on copie la formule dans une autre cellule.|"
  "Une reference absolue, comme $A$1, reste fixe lors de la copie : les symboles dollar bloquent ligne et colonne.|"
  "La fonction SOMME additionne une plage de cellules, par exemple =SOMME(B2:B10).|"
  "La fonction MOYENNE calcule la moyenne d'une plage et la fonction NB compte les cellules non vides.|"
  "Les fonctions SI et NB.SI permettent d'effectuer des tests et des comptes conditionnels.|"
  "Un graphique lie a une plage de donnees permet de visualiser une evolution ou une repartition.|"
  "Le tri et le filtre classent les lignes ou n'affichent que celles qui satisfont un critere.|"
  "Avant de diffuser un classeur, on verifie les formules, la mise en forme et la protection des cellules sensibles."),
[QC("Quelle est l'adresse de la cellule colonne C ligne 5 ?", "C5~5C~C-5~35", 0,
     "L'adresse donne d'abord la lettre de la colonne, puis le numero de la ligne."),
 QC("Par quoi commence une formule dans un tableur ?", "Par le signe egal~Par le signe plus~Par une lettre~Par un nombre", 0,
     "Le signe egal signale au tableur qu'il doit evaluer une expression et non afficher du texte."),
 QC("Que fait =SOMME(B2:B6) ?", "Additionne les cellules de B2 a B6~Compte les cellules~Calcule la moyenne~Trie les valeurs", 0,
     "SOMME calcule la somme de toutes les cellules de la plage indiquee."),
 QC("Une reference absolue s'ecrit ...", "$A$1~A1~A$1~$A1", 0,
     "Les deux symboles dollar bloquent la colonne et la ligne ; les autres formes sont des references mixtes."),
 QC("Quelle fonction compte les cellules non vides d'une plage ?", "NB~SOMME~MOYENNE~MAX", 0,
     "NB denombre les cellules contenant une valeur, y compris les nombres et le texte."),
 QC("En copiant =A1+B1 de C1 vers C2, on obtient ...", "=A2+B2~=A1+B1~=A1+B2~=B2+C2", 0,
     "Les references relatives sont decalees d'une ligne lors de la copie vers le bas."),
 QC("Un graphique dans un tableur sert principalement a ...", "Visualiser les donnees~Ecrire du texte~Proteger le classeur~Creer une base de donnees", 0,
     "Le graphique traduit visuellement les valeurs d'une plage pour rendre les tendances lisibles."),
 QT("Expliquer la difference entre reference relative et reference absolue avec un exemple de copie de formule.",
    "Une reference relative, ecrite A1, est modifiee lors de la copie : si la formule =B2*C2 placee en D2 est copiee en D3, elle devient =B3*C3, car chaque reference est decalee d'une ligne. Une reference absolue, ecrite $B$2, ne bouge pas lors de la copie. C'est utile pour un taux unique place en B2 : dans la cellule D2 on ecrit =C2*$B$2, puis on copie vers le bas ; la reference au taux reste $B$2 alors que C2 devient C3, C4 et ainsi de suite. Une reference mixte comme B$2 ou $B2 ne bloque qu'une seule dimension. Choisir le bon type de reference evite les erreurs de calcul sur toute une colonne.",
    "On attend la definition des deux types, un exemple de copie avec decalage et l'usage d'un taux fixe bloque par les symboles dollar."),
 QT("Decrire comment construire un tableau de suivi de ventes avec un total, une moyenne et un graphique.",
    "On cree quatre colonnes : Produit, Quantite, Prix unitaire et Montant. Dans la premiere ligne de donnees, on saisit le produit, la quantite et le prix, puis on ecrit en D2 la formule =B2*C2. On copie cette formule vers le bas pour toutes les lignes grace a la poignee de recopie. On ajoute une ligne de total avec =SOMME(D2:D10) et une ligne de moyenne avec =MOYENNE(D2:D10). On selectionne ensuite la plage des produits et des montants, puis on insere un graphique en colonnes pour comparer les ventes. On termine par une relecture des formules et par la verification que les references ne se sont pas decalees incorrectement.",
    "On attend la creation des colonnes, la formule de montant, sa copie, le total, la moyenne, le graphique et une etape de verification.")],
C("Le tableur organise les donnees en cellules et calcule grace a des formules dont les references sont relatives ou absolues.",
  "=SOMME(B2:B10) · =MOYENNE(C2:C10) · =B2*$E$1",
  "Reference relative : s'adapte a la copie · reference absolue : reste fixe",
  "Cellule~Adresse colonne et ligne~B4~Formule~Commence par egal~Calcule un resultat~Reference~Relative ou absolue~S'adapte ou non",
  "Saisir les donnees dans les colonnes|Ecrire la premiere formule|Copier la formule vers le bas|Verifier les references|Inserer un graphique",
  "Oublier le signe egal|Confondre plage et cellule|Copier sans bloquer un taux|Ne pas verifier une division par zero",
  "Adresse~Colonne B ligne 4~Plage~Ensemble de cellules~Formule~Calcul automatique~Taux~Reference absolue~Graphique~Lecture visuelle",
  "Reference relative~A1~Change a la copie~Calcul ligne par ligne~Reference absolue~$A$1~Reste fixe~Taux unique",
  "SOMME~Additionne les valeurs~Total d'une colonne~Rapidite~MOYENNE~Calcule la moyenne~Tendance centrale~Arrondi a preciser"))


# ============================================================ C03
add("C03", "Bases de donnees : tables, champs et requetes", "Numerique", ["Terminale"],
S("Une base de donnees est un ensemble organise d'informations structurees, destine a etre interroge.|"
  "Un systeme de gestion de base de donnees permet de creer, alimenter, modifier et interroger la base.|"
  "Les donnees sont rangees dans des tables : une table correspond a un theme, par exemple les clients.|"
  "Chaque ligne d'une table est un enregistrement, ou tuple, qui decrit une entite.|"
  "Chaque colonne est un champ, ou attribut, auquel on donne un type : texte, nombre, date ou booleen.|"
  "Une cle primaire identifie de maniere unique chaque enregistrement : elle n'est ni vide ni repetee.|"
  "Une cle etrangere est un champ qui reference la cle primaire d'une autre table et cree une liaison.|"
  "Le modele relationnel represente les donnees sous forme de tables reliees entre elles.|"
  "Une requete extrait les donnees qui satisfont des criteres, avec le langage SQL ou une interface graphique.|"
  "La clause SELECT ... FROM ... WHERE choisit les champs, la table et les conditions de filtrage.|"
  "Les operateurs ET, OU et NON combinent les criteres et LIKE permet une recherche partielle sur du texte.|"
  "La qualite d'une base repose sur la coherence des donnees, l'unicite des cles et la documentation du schema."),
[QC("Dans une table, que represente une ligne ?", "Un champ~Un enregistrement~Une requete~Une base entiere", 1,
     "Une ligne correspond a une entite, c'est-a-dire a un enregistrement complet."),
 QC("Qu'est-ce qu'une cle primaire ?", "Un champ qui identifie uniquement chaque enregistrement~Un mot de passe~Une requete~Un graphique", 0,
     "La cle primaire est unique et non nulle dans la table."),
 QC("Que fait la clause WHERE en SQL ?", "Choisir les champs~Filtrer les lignes selon des criteres~Nommer la table~Trier les resultats", 1,
     "WHERE exprime la condition que doivent satisfaire les lignes retournees."),
 QC("Une cle etrangere sert a ...", "Lier deux tables~Proteger la base~Compter les lignes~Afficher un formulaire", 0,
     "Elle reference la cle primaire d'une autre table pour etablir une relation."),
 QC("Quel type de champ convient pour une date de naissance ?", "Texte~Date~Booleen~Image", 1,
     "Le type date permet le tri chronologique et le calcul d'age."),
 QC("Dans SELECT nom FROM Clients, que designe Clients ?", "Le champ~La table~La condition~Le tri", 1,
     "La clause FROM indique la table source des donnees."),
 QC("Quel operateur exige que deux criteres soient vrais en meme temps ?", "OU~ET~NON~LIKE", 1,
     "ET correspond a l'intersection des conditions ; OU correspond a leur union."),
 QT("Expliquer le role des cles primaire et etrangere dans une base de donnees de commandes.",
    "La table Clients contient un champ id_client qui est sa cle primaire : chaque client possede un identifiant unique et jamais vide. La table Commandes contient sa propre cle primaire id_commande et un champ id_client qui est une cle etrangere, car il reference la table Clients. Grace a cette liaison, on peut retrouver le client associe a chaque commande et verifier qu'aucune commande ne renvoie a un client inexistant. L'unicite de la cle primaire garantit qu'une commande ou un client n'est pas enregistre deux fois, et la cle etrangere garantit la coherence des relations entre les tables. C'est le principe de l'integrite referentielle dans le modele relationnel.",
    "On attend la definition des deux cles, un exemple concret avec Clients et Commandes, et la notion d'integrite referentielle."),
 QT("Ecrire une requete SQL pour afficher le nom et la ville des clients habitant a Lyon, tries par nom, puis expliquer chaque clause.",
    "La requete s'ecrit : SELECT nom, ville FROM Clients WHERE ville = 'Lyon' ORDER BY nom. La clause SELECT designe les deux champs a afficher, nom et ville. La clause FROM indique que les donnees sont prises dans la table Clients. La clause WHERE filtre les lignes en ne gardant que celles dont le champ ville vaut exactement Lyon ; la valeur textuelle est entouree d'apostrophes. La clause ORDER BY nom classe le resultat par ordre alphabetique croissant sur le nom. Si l'on voulait aussi les clients de Marseille, on ecrirait WHERE ville = 'Lyon' OR ville = 'Marseille'.",
    "On attend la requete complete et l'explication de SELECT, FROM, WHERE et ORDER BY, avec les apostrophes autour du texte.")],
C("Une base relationnelle organise les donnees en tables liees par des cles et interrogeables par des requetes.",
  "SELECT champs FROM table WHERE condition",
  "ET / OU / NON · LIKE · ORDER BY",
  "Table~Theme des donnees~Clients~Champ~Colonne et type~Nom, date~Cle primaire~Identifiant unique~id_client",
  "Identifier les entites|Definir les champs et leurs types|Choisir les cles primaires|Creer les liaisons par cles etrangeres|Ecrire et tester les requetes",
  "Oublier la cle primaire|Repeter un identifiant|Confondre ET et OU|Interroger une table inexistante",
  "Enregistrement~Une ligne de table~Attribut~Une colonne~Requete~Extraction filtree~SQL~Langage d'interrogation~Schema~Structure de la base",
  "Cle primaire~Unique dans la table~Jamais vide~Identifie un enregistrement~Cle etrangere~Reference une autre table~Peut se repetee~Cree une liaison",
  "ET~Deux criteres vrais~Intersection~Moins de resultats~OU~Au moins un critere vrai~Union~Plus de resultats"))


# ============================================================ C04
add("C04", "Securite numerique et donnees personnelles", "Numerique", ["Terminale"],
S("La securite de l'information vise a proteger la confidentialite, l'integrite et la disponibilite des donnees.|"
  "La confidentialite garantit que seules les personnes autorisees peuvent consulter une information.|"
  "L'integrite garantit que les donnees ne sont ni modifiees ni detruites par erreur ou par malveillance.|"
  "La disponibilite garantit que le service et les donnees restent accessibles quand on en a besoin.|"
  "L'authentification verifie l'identite d'un utilisateur, souvent par un mot de passe et un second facteur.|"
  "Un mot de passe robuste est long, unique et melange majuscules, minuscules, chiffres et symboles.|"
  "Le chiffrement rend les donnees illisibles sans cle, notamment lors des echanges sur internet avec HTTPS.|"
  "Le phishing est une tentative d'arnaque qui imite un organisme de confiance pour voler des identifiants.|"
  "Un ransomware chiffre les fichiers de la victime et exige une rancon pour les rendre a nouveau lisibles.|"
  "Les logiciels malveillants s'installent souvent par une piece jointe, un lien ou un telechargement inconscient.|"
  "Une sauvegarde reguliere, de preference hors ligne, permet de restaurer les donnees apres une attaque.|"
  "Le reglement RGPD impose la minimisation des donnees, la transparence et le respect des droits des personnes."),
[QC("Quels sont les trois piliers de la securite de l'information ?", "Confidentialite, integrite, disponibilite~Rapidite, cout, qualite~Texte, image, son~Lecture, ecriture, suppression", 0,
     "Ces trois proprietes forment le modele de reference de la securite des systemes d'information."),
 QC("Que garantit la confidentialite ?", "Que les donnees restent accessibles~Que seules les personnes autorisees lisent~Que les donnees soient exactes~Que le site soit rapide", 1,
     "La confidentialite limite l'acces aux seules personnes habilitees."),
 QC("Qu'est-ce que le phishing ?", "Une sauvegarde~Une arnaque imitant un organisme de confiance~Un type de chiffrement~Un pare-feu", 1,
     "Le phishing utilise un message trompeur pour obtenir des mots de passe ou des donnees bancaires."),
 QC("Un ransomware ...", "Chiffre les fichiers et demande une rancon~Supprime les virus~Accelere le reseau~Protege le mot de passe", 0,
     "Ce logiciel hostile rend les donnees inaccessibles jusqu'au paiement d'une rancon."),
 QC("Face a un courriel suspect, il faut ...", "Cliquer sur le lien~Ouvrir la piece jointe~Verifier l'expediteur sans cliquer~Repondre avec son mot de passe", 2,
     "La bonne reaction est de verifier l'adresse de l'expediteur et de ne pas interagir avec les elements du message."),
 QC("Le chiffrement permet de ...", "Rendre les donnees illisibles sans cle~Augmenter le debit~Supprimer les doublons~Changer de format", 0,
     "Sans la cle de dechiffrement, le contenu chiffre reste incomprehensible."),
 QC("Le RGPD impose notamment ...", "La minimisation des donnees~Le partage de tous les mots de passe~L'absence de sauvegarde~La suppression des droits", 0,
     "On ne collecte que les donnees necessaires et on informe les personnes de leur utilisation."),
 QT("Expliquer les regles d'un mot de passe robuste et l'interet de l'authentification a deux facteurs.",
    "Un mot de passe robuste comporte au moins douze caracteres, n'est pas un mot du dictionnaire, est unique pour chaque service et combine majuscules, minuscules, chiffres et symboles. Il ne contient ni date de naissance ni nom d'entreprise facile a trouver. L'authentification a deux facteurs ajoute une seconde preuve apres le mot de passe : un code recu par SMS, une application generating un code temporaire ou une cle physique. Ainsi, meme si le mot de passe est vole, l'attaquant ne peut pas se connecter sans le second facteur. Ces regles reduisent fortement le risque d'acces non autorise, surtout lorsque les services sont accessibles depuis internet.",
    "On attend la longueur, l'unicite, la variete des caracteres et l'explication du second facteur avec un exemple."),
 QT("Decrire la procedure a suivre lorsqu'une attaque par ransomware est suspectee.",
    "On isole d'abord la machine infectee du reseau, en debranchant le cable ou en coupant le Wi-Fi, pour eviter la propagation aux autres postes. On ne paie pas la rancon et on ne supprime pas les fichiers chiffres, car ils peuvent servir a l'enquete. On previent ensuite le service informatique ou le responsable securite, qui identifie la porte d'entree, souvent un courriel de phishing ou une piece jointe. On restaure les donnees a partir d'une sauvegarde propre et recente, apres avoir verifie qu'elle n'est pas elle-meme infectee. On applique enfin les mises a jour de securite, on change les mots de passe exposes et on documente l'incident dans un rapport pour eviter la repetition.",
    "On attend isolation, signalement, non-paiement, restauration depuis sauvegarde saine, mise a jour et retour d'experience.")],
C("Proteger un systeme, c'est garantir confidentialite, integrite et disponibilite par des mesures techniques et organisationnelles.",
  "Securite = confidentialite + integrite + disponibilite",
  "Authentification · chiffrement · sauvegarde · mise a jour",
  "Confidentialite~Acces limite~Autorises seulement~Integrite~Donnees exactes~Pas d'alteration~Disponibilite~Acces quand necessaire~Service actif",
  "Detecter la menace|Isoler le poste ou le service|Prevenir le responsable securite|Restaurer depuis une sauvegarde saine|Appliquer les mises a jour et documenter",
  "Cliquer sur un lien suspect|Reutiliser le meme mot de passe|Ne jamais faire de sauvegarde|Oublier de verifier l'expediteur",
  "Phishing~Courriel trompeur~Ransomware~Fichiers chiffres~Chiffrement~Donnees illisibles~Sauvegarde~Restauration possible~RGPD~Donnees minimales",
  "Confidentialite~Personnes autorisees~Integrite~Donnees non modifiees~Disponibilite~Service accessible~Attaque~Atteinte a un pilier",
  "Mot de passe~Premier facteur~Deuxieme facteur~Code temporaire~Compte robuste~Long et unique~Compte fragile~Court et reutilise"))


# ============================================================ C05
add("C05", "Reseaux informatiques et fonctionnement d'internet", "Numerique", ["1re"],
S("Un reseau informatique relie des equipements afin de partager des ressources et des donnees.|"
  "Un reseau local, ou LAN, couvre un batiment ; un reseau etendu, ou WAN, relie plusieurs sites geographiques.|"
  "Le commutateur relie les machines d'un meme reseau local et aiguille les trames grace aux adresses matérielles.|"
  "Le routeur connecte deux reseaux differents et choisit le chemin des paquets grace aux adresses IP.|"
  "Le modem convertit le signal numerique pour le transporter sur la ligne de l'operateur.|"
  "Une adresse IP identifie une machine sur un reseau : par exemple 192.168.1.10 en IPv4.|"
  "Le protocole TCP/IP definit les regles de communication : decoupage en paquets, adressage et accusement de reception.|"
  "Le serveur DNS traduit un nom de domaine lisible, comme fichelab.fr, en adresse IP.|"
  "Une URL designe une ressource sur internet : le protocole, le domaine, le chemin et d'eventuels parametres.|"
  "Le modele client/serveur oppose un client qui demande un service et un serveur qui fournit la ressource.|"
  "La liaison est filaire avec Ethernet ou sans fil avec Wi-Fi ; le debit et la latence qualifient la connexion.|"
  "Un pare-feu filtre les flux entrants et sortants pour proteger le reseau des acces non autorises."),
[QC("Quel equipement relie deux reseaux differents ?", "Le commutateur~Le routeur~L'ecran~L'imprimante", 1,
     "Le routeur fait communiquer des reseaux distincts en utilisant les adresses IP."),
 QC("A quoi sert le serveur DNS ?", "A traduire un nom de domaine en adresse IP~A chiffrer les donnees~A imprimer des documents~A sauvegarder les fichiers", 0,
     "Le DNS ressemble a un annuaire qui associe un nom lisible a une adresse IP."),
 QC("Une adresse IP permet de ...", "Identifier une machine sur un reseau~Mesurer la temperature~Compter les fichiers~Formater un disque", 0,
     "L'adresse IP identifie l'interface d'une machine et permet de lui acheminer des paquets."),
 QC("Que designe une URL ?", "Une ressource sur internet~Un type de commutateur~Une adresse physique~Une regle de pare-feu", 0,
     "L'URL precise le protocole, le domaine et le chemin de la ressource demandee."),
 QC("Dans le modele client/serveur, le serveur ...", "Demande une page~Fournit la ressource demande~Affiche le resultat~Stocke uniquement les images", 1,
     "Le client formule la demande et le serveur y repond en envoyant la ressource."),
 QC("Quel protocole definit la communication sur internet ?", "TCP/IP~HTTP seul~DNS seul~Ethernet seul", 0,
     "TCP/IP est la suite de protocoles de base qui structure les echanges sur internet."),
 QC("Un pare-feu sert a ...", "Filtrer les flux réseau~Accelerer l'impression~Augmenter le stockage~Traduire les adresses", 0,
     "Il controle les connexions entrantes et sortantes selon des regles de securite."),
 QT("Expliquer le chemin d'une requete lorsqu'un utilisateur saisit une adresse de site web dans son navigateur.",
    "Le navigateur est le client : il extrait le nom de domaine de l'URL et interroge le serveur DNS pour obtenir l'adresse IP correspondante. Il etablit ensuite une connexion, souvent en TCP avec chiffrement HTTPS, vers cette adresse. La requete HTTP est decoupee en paquets qui traversent le reseau local, le commutateur, puis le routeur, qui choisit le chemin vers le serveur d'hebergement. Le routeur de destination achemine les paquets au serveur, lequel renvoie la page web en plusieurs paquets. Le navigateur reassemble les paquets, affiche la page et conserve certains elements en cache pour les visites suivantes. Le pare-feu controle les echanges a chaque franchissement de frontiere de reseau.",
    "On attend le role du DNS, la translation en adresse IP, le role du routeur, la requete et la reponse du serveur, ainsi que la mention du pare-feu."),
 QT("Distinguer un reseau local d'un reseau etendu et donner un exemple concret pour chacun.",
    "Un reseau local, ou LAN, couvre une zone reduite comme une salle d'ordinateurs ou un batiment d'entreprise : les postes partagent une imprimante, des fichiers et une connexion internet via le meme routeur. Les equipements sont relies par un commutateur, en Ethernet ou en Wi-Fi. Un reseau etendu, ou WAN, relie plusieurs sites eloignes, par exemple le siege parisien et une agence a Lyon : les liaisons passent par le reseau de l'operateur et internet. Le routeur de chaque site interconnecte les LAN et applique des regles de routage et de securite. Le LAN est rapide et prive, tandis que le WAN depend de la bande passante de l'operateur et necessite davantage de protections.",
    "On attend la definition des deux echelles, des exemples, le role du commutateur et du routeur, et la diffrence de securite.")],
C("Un reseau interconnecte des machines grace a des equipements et a des protocoles qui organisent les echanges.",
  "Client + DNS + IP + routeur = acces a une ressource",
  "LAN local · WAN etendu · TCP/IP · pare-feu",
  "Commutateur~Relie un LAN~Adresses matérielles~Routeur~Relie deux reseaux~Adresses IP~DNS~Nom vers IP~Pare-feu~Filtre les flux",
  "Identifier les equipements du reseau|Attribuer les adresses IP|Configurer le DNS et le routage|Tester la connexion|Verifier les regles du pare-feu",
  "Confondre commutateur et routeur|Oublier le DNS|Croire qu'une URL est une adresse IP|Laisser le Wi-Fi sans protection",
  "LAN~Reseau d'un batiment~WAN~Reseau multi-sites~IP~Adresse logique~Paquet~Unite de transport~Serveur~Fournit une ressource",
  "Commutateur~Un seul reseau local~Adresses matérielles~Transport interne~Routeur~Entre deux reseaux~Adresses IP~Choix du chemin",
  "Wi-Fi~Liaison sans fil~Ethernet~Liaison filaire~Debit~Volume transmis~Latence~Temps de reponse"))


# ============================================================ C06
add("C06", "Traitement de texte et mise en forme d'un document", "Numerique", ["1re"],
S("Un traitement de texte permet de creer, modifier et mettre en page un document ecrit.|"
  "Les styles de caracteres, comme le gras ou l'italique, s'appliquent a une selection de texte.|"
  "Les styles de paragraphe, titre, sous-titre ou corps de texte, structurent le document et facilitent sa mise a jour.|"
  "La mise en page definit les marges, l'orientation, le format de papier et le nombre de colonnes.|"
  "L'en-tete et le pied de page contiennent des informations repetees : titre, date et numero de page.|"
  "Une table organise des donnees en lignes et en colonnes, par exemple un tableau de resultats.|"
  "Le sommaire automatique se construit a partir des styles de titre et se met a jour en une seule commande.|"
  "La correction orthographique et grammaticale signale les erreurs mais ne remplace pas une relecture attentive.|"
  "Les notes de bas de page renvoient a une source ou a un commentaire sans interrompre la lecture.|"
  "Les images doivent etre redimensionnees et accompagnees d'un texte alternatif pour l'accessibilite.|"
  "La fonction suivre les modifications enregistre les corrections de plusieurs auteurs avant leur acceptation.|"
  "On enregistre dans un format editable comme docx ou odt, puis on exporte en PDF pour la diffusion."),
[QC("Quel style permet de generer automatiquement un sommaire ?", "Le style de caracteres gras~Le style de titre~La couleur de police~La marge de page", 1,
     "Le sommaire est construit a partir des paragraphes auxquels on a applique un style de titre."),
 QC("Que contient generalement un pied de page ?", "Le sommaire~Le numero de page~Le corps du texte~Les images", 1,
     "Le pied de page accueille les elements repetes comme la pagination."),
 QC("A quoi sert une table dans un document ?", "A organiser des images~A organiser des donnees en lignes et colonnes~A changer de police~A proteger le fichier", 1,
     "La tableau permet de presenter des donnees sous forme de grille."),
 QC("Le texte alternatif d'une image sert a ...", "Rendre l'image accessible~Agrandir l'image~Changer sa couleur~La supprimer", 0,
     "Il decrit l'image pour les lecteurs d'ecran et lorsque l'affichage est impossible."),
 QC("La correction orthographique ...", "Remplace la relecture~Signale des erreurs mais doit etre verifiee~Interdit les accents~Efface le texte", 1,
     "Le correcteur propose des corrections qui doivent etre validees par l'auteur."),
 QC("La fonction suivre les modifications permet de ...", "Enregistrer les corrections avant acceptation~Supprimer toutes les images~Creer un graphique~Changer le format de papier", 0,
     "Elle rend visibles les ajouts et suppressions proposes par chaque auteur."),
 QC("Quel format est adapte a une diffusion non modifiable ?", "DOCX~ODT~PDF~TXT", 2,
     "Le PDF fixe la mise en page et limite les modifications accidentelles."),
 QT("Decrire la demarche pour produire un rapport de stage bien structure avec un sommaire.",
    "On definit d'abord la mise en page : format A4, marges, interlignage, en-tete avec le titre du rapport et pied de page avec la pagination. On saisit ensuite le contenu en utilisant systematiquement les styles de paragraphe : Titre 1 pour les grandes parties, Titre 2 pour les sous-parties et corps de texte pour le reste. Ce travail de structure permet d'inserer un sommaire automatique en une commande et de le mettre a jour apres chaque ajout. On integre les tableaux de donnees et les images avec une legende et un texte alternatif. Les notes de bas de page signalent les sources. On active enfin la fonction suivre les modifications pour relire avec le tuteur, on accepte les corrections, puis on exporte une version PDF pour la diffusion.",
    "On attend mise en page, styles de titre, sommaire automatique, tableaux et images, notes de bas de page, suivi des modifications et export PDF."),
 QT("Expliquer pourquoi il faut distinguer le format editable et le format de diffusion d'un document.",
    "Le format editable, comme docx ou odt, conserve la structure du document : styles, titres, champs et elements que l'on peut encore modifier. Il est adapte au travail collaboratif et aux corrections successives. Le format PDF fige l'apparence : les polices, les marges et la pagination restent identiques sur tous les ordinateurs, ce qui evite les mauvaises surprises a l'impression ou a l'affichage. En revanche, le PDF est moins pratique pour retravailler le texte. Une bonne methode consiste a toujours conserver le fichier editable source et a ne diffuser que le PDF, en verifiant avant export que les images, les tableaux et la pagination sont corrects.",
    "On attend la distinction entre structure modifiable et mise en page fixe, avec les usages respectifs et une regle de conservation du source.")],
C("Un document de qualite combine une structure logique, une mise en page soignee et une diffusion controlee.",
  "Styles de titre + sommaire automatique = document navigable",
  "Edition : DOCX, ODT · diffusion : PDF",
  "Style de titre~Structure du document~Sommaire~Mise en page~Marges et orientation~Presentation~Tableau~Donnees en grille~Image~Texte alternatif",
  "Definir la mise en page|Appliquer les styles de titre|Saisir et structurer le contenu|Inserer tableaux et images|Mettre a jour le sommaire et exporter",
  "Mettre en forme manuellement chaque titre|Oublier le texte alternatif|Accepter les corrections sans les lire|Diffuser le fichier editable par erreur",
  "Titre 1~Grande partie~Titre 2~Sous-partie~Sommaire~Liste des titres~Note~Source en bas de page~PDF~Version fige",
  "Styles de caracteres~Gras, italique, couleur~Styles de paragraphe~Titre et corps~Mise en forme directe~Rapide mais fragile~Styles~Coherents et reutilisables",
  "DOCX~Format editable~ODT~Format editable libre~PDF~Mise en page fixe~Suivi des modifications~Corrections visibles"))


# ============================================================ C07
add("C07", "Proportionnalite, taux et pourcentages", "Maths", ["1re"],
S("Deux grandeurs sont proportionnelles lorsque le rapport de l'une a l'autre reste constant.|"
  "Le coefficient de proportionnalite k verifie egalite y = k x pour tous les couples de valeurs.|"
  "Dans un tableau de proportionnalite, une ligne est obtenue en multipliant l'autre par le coefficient.|"
  "La regle de trois permet de calculer une valeur intermediaire ou situee hors du tableau.|"
  "Un pourcentage est une fraction de denominateur 100 : 25 pour cent valent 25/100, soit 0,25.|"
  "Un taux t se convertit en coefficient multiplicateur : 1 + t/100 pour une hausse, 1 - t/100 pour une baisse.|"
  "Une augmentation de 20 pour cent puis une diminution de 20 pour cent ne retrouvent pas la valeur initiale.|"
  "Le taux d'evolution se calcule par la difference nouveau moins ancien, divisee par ancien, multipliee par 100.|"
  "Une remise commerciale est un pourcentage deduit du prix affiche.|"
  "La TVA est un pourcentage ajoute au prix hors taxes pour obtenir le prix toutes taxes comprises.|"
  "Les arrondis doivent etre effectues en fin de calcul pour eviter les erreurs cumulees.|"
  "Dans un probleme de taux, on identifie d'abord la grandeur de reference qui represente 100 pour cent."),
[QC("Si 3 articles coutent 12 euros, combien coutent 5 articles ?", "20 euros~15 euros~60 euros~4 euros", 0,
     "Le prix unitaire est 4 euros, donc 5 articles coutent 20 euros."),
 QC("Dans l'egalite y = 3x, le coefficient de proportionnalite est ...", "3~x~1/3~0", 0,
     "Le coefficient est le nombre fixe qui multiplie x pour obtenir y."),
 QC("25 pour cent de 80 euros valent ...", "20 euros~25 euros~2 euros~200 euros", 0,
     "On calcule 80 x 0,25 = 20 euros."),
 QC("Un prix de 50 euros qui augmente de 20 pour cent devient ...", "60 euros~70 euros~52 euros~100 euros", 0,
     "Le coefficient multiplicateur est 1,2 et 50 x 1,2 = 60 euros."),
 QC("Le coefficient pour une baisse de 15 pour cent est ...", "0,85~1,15~15~0,15", 0,
     "On conserve 100 pour cent moins 15 pour cent, soit 85 pour cent, donc 0,85."),
 QC("Apres une hausse de 20 pour cent puis une baisse de 20 pour cent, 100 euros deviennent ...", "96 euros~100 euros~104 euros~120 euros", 0,
     "On calcule 100 x 1,2 x 0,8 = 96 euros : les coefficients ne s'annulent pas."),
 QC("Une TVA de 20 pour cent sur un prix hors taxes de 50 euros donne un TTC de ...", "60 euros~10 euros~52 euros~70 euros", 0,
     "On ajoute 10 euros de TVA au prix de 50 euros, soit 60 euros TTC."),
 QT("Un article affiche 80 euros et beneficie d'une remise de 15 pour cent, puis une TVA de 20 pour cent s'applique au prix remise. Calculer le prix final et expliquer les etapes.",
    "On commence par la remise : le coefficient est 1 - 15/100 = 0,85, donc le prix apres remise vaut 80 x 0,85 = 68 euros. On applique ensuite la TVA sur ce prix remise, et non sur le prix initial : le coefficient est 1 + 20/100 = 1,2. Le prix final est donc 68 x 1,2 = 81,60 euros. La TVA represente 13,60 euros. Il faut bien respecter l'ordre des operations et ne pas additionner les taux : 15 pour cent puis 20 pour cent ne font pas 5 pour cent ni 35 pour cent de variation globale. Le prix final est superieur au prix initial malgre la remise, car la base de calcul de la TVA est le prix apres remise.",
    "On attend le coefficient 0,85, le prix intermediaire 68 euros, le coefficient 1,2 et le resultat 81,60 euros avec l'ordre des etapes."),
 QT("Expliquer comment reconnaître une situation de proportionnalite et construire le tableau associe.",
    "On reconnait une proportionnalite lorsque multiplier une grandeur par un nombre multiplie l'autre grandeur par le meme nombre, et lorsqu'une valeur nulle correspond toujours a une valeur nulle. On peut verifier que les rapports y/x sont egaux pour toutes les lignes du tableau. Le coefficient de proportionnalite k est ce rapport constant. On construit alors un tableau a deux lignes : on place les valeurs de la premiere grandeur dans la premiere ligne et les valeurs correspondantes dans la seconde, en utilisant k pour passer d'une colonne a l'autre. La regle de trois permet ensuite de trouver une valeur manquante, par exemple le prix de 7 articles si 4 articles coutent 10 euros. Enfin, on verifie que la valeur obtenue est coherente avec l'ordre de grandeur des donnees.",
    "On attend la definition par le rapport constant, le test de la valeur nulle, la construction du tableau et l'usage de la regle de trois.")],
C("La proportionnalite repose sur un coefficient constant ; les taux se traduisent par des coefficients multiplicateurs.",
  "y = k x · coefficient = 1 + t/100 ou 1 - t/100",
  "Taux = (nouveau - ancien) / ancien x 100",
  "Coefficient~Rapport constant~k=y/x~Pourcentage~Fraction sur 100~0,25~Hausse~1+t/100~Baisse~1-t/100",
  "Identifier la grandeur de reference 100 pour cent|Verifier la proportionalite|Convertir le taux en coefficient|Effectuer les calculs dans l'ordre|Arrondir et verifier la coherence",
  "Additionner deux taux successifs|Appliquer la TVA avant la remise|Arrondir a chaque etape|Oublier la grandeur de reference",
  "3 articles~12 euros~Prix unitaire~4 euros~Remise 15~Coefficient 0,85~TVA 20~Coefficient 1,2~Prix final~81,60 euros",
  "Augmentation~Coefficient superieur a 1~Diminution~Coefficient entre 0 et 1~Taux negatif~Baisse~Taux positif~Hausse",
  "Proportionnalite~Rapport constant~Non proportionnalite~Frais fixes~Regle de trois~Calcul intermediaire~Pourcentage~Base 100"))


# ============================================================ C08
add("C08", "Fonction exponentielle et taux de croissance", "Maths", ["Terminale"],
S("La fonction exponentielle, notee exp, associe a x le nombre e eleve a la puissance x.|"
  "Le nombre e est un reel environ egal a 2,718 ; on a exp(0) = 1 et exp(1) = e.|"
  "La fonction exp est strictement croissante et strictement positive sur l'ensemble des reels.|"
  "Pour tous reels a et b, exp(a + b) = exp(a) x exp(b) : une addition devient une multiplication.|"
  "Une suite geometrique de raison q se ecrit u(n) = u(0) x q puissance n, soit u(0) x exp(n ln q) si q est positif.|"
  "Un taux de croissance continu t correspond au facteur exp(t) sur une unite de temps.|"
  "Le modele exponentiel decrit une evolution proportionnelle a la valeur presente : la derivee est k fois la fonction.|"
  "Le temps de doublement est la duree necessaire pour que la grandeur soit multipliee par deux.|"
  "Une depreciation continue utilise un taux negatif : la valeur diminue selon exp(-k t).|"
  "Sur un graphique semi-logarithmique, une croissance exponentielle apparait comme une droite.|"
  "Quand x tend vers plus l'infini, exp(x) tend vers plus l'infini ; quand x tend vers moins l'infini, exp(x) tend vers zero.|"
  "Pour resoudre exp(x) = a avec a strictement positif, on ecrit x = ln(a) grace a la fonction reciproque."),
[QC("Quelle est la valeur de exp(0) ?", "0~1~e~2,718", 1,
     "Toute puissance d'exposant nul vaut 1, donc exp(0) = 1."),
 QC("La fonction exponentielle est ...", "Decroissante et negative~Croissante et positive~Constante~Non definie pour les negatifs", 1,
     "exp est strictement croissante et toujours strictement positive."),
 QC("Quelle propriete est vraie ?", "exp(a+b) = exp(a) + exp(b)~exp(a+b) = exp(a) x exp(b)~exp(a+b) = exp(a b)~exp(a+b) = a exp(b)", 1,
     "L'exponentielle transforme une somme en produit."),
 QC("Un taux continu de 5 pour cent correspond au facteur ...", "exp(0,05)~0,05~1,05^-1~exp(5)", 0,
     "Le facteur continu est e eleve a la taux, ici exp(0,05)."),
 QC("Une population qui double regulierement suit un modele ...", "Lineaire~Exponentiel~Constant~Affine decroissant", 1,
     "Un doublement revient a multiplier par 2 a chaque periode : c'est exponentiel."),
 QC("Quel est le comportement de exp(x) quand x tend vers moins l'infini ?", "Il tend vers 0~Il tend vers l'infini~Il tend vers 1~Il n'existe pas", 0,
     "La courbe se rapproche de l'axe des abscisses sans jamais le toucher."),
 QC("Pour resoudre exp(x) = 7, on ecrit ...", "x = ln(7)~x = exp(7)~x = 7~x = 1/7", 0,
     "On applique la fonction reciproque ln des deux cotes."),
 QT("Etudier la fonction f(x) = exp(2x) - 1 : domaine, limite en moins l'infini, racine et variations.",
    "La fonction est definie sur tous les reels car l'exponentielle accepte tout exposant. Quand x tend vers moins l'infini, 2x tend vers moins l'infini, donc exp(2x) tend vers 0 et f(x) tend vers -1 : la droite d'ordonnnee -1 est asymptote horizontale. La racine verifie exp(2x) = 1, soit 2x = 0 et x = 0 : la courbe passe par l'origine. La derivee est f'(x) = 2 exp(2x), strictement positive pour tout x : f est strictement croissante sur les reels. Quand x tend vers plus l'infini, f(x) tend vers plus l'infini. Le graphique part de l'asymptote y = -1 a gauche, traverse (0 ; 0), puis monte rapidement vers la droite.",
    "On attend le domaine des reels, la limite -1, la racine x = 0, la derivee 2 exp(2x) et la croissance."),
 QT("Une entreprise estime que son chiffre d'affaires croit de 3 pour cent par an de facon continue, a partir de 2 millions d'euros. Exprimer le modele et calculer la valeur apres 5 ans.",
    "On modele par C(t) = 2 x exp(0,03 t), ou t est le temps en annees et C est en millions d'euros. Le facteur continu associe au taux 3 pour cent est exp(0,03), environ 1,03045. Apres 5 ans, on obtient C(5) = 2 x exp(0,15). Comme exp(0,15) est environ egal a 1,16183, le chiffre d'affaires sera d'environ 2,32 millions d'euros. Le gain est d'environ 0,32 million d'euros, soit 16,2 pour cent sur la periode. Ce modele continu differe legerement d'une capitalisation annuelle discrete qui donnerait 2 x 1,03 puissance 5, environ 2,319 millions : l'ecart reste faible pour un taux modeste et une courte duree.",
    "On attend le modele 2 exp(0,03t), le calcul a t = 5, une valeur proche de 2,32 millions et la comparison avec le calcul annuel.")],
C("L'exponentielle modelise une croissance ou une diminution proportionnelle a la valeur presente.",
  "f(x) = exp(x) · exp(a+b) = exp(a) x exp(b)",
  "exp croissante et positive · exp(-) tend vers 0 · reciproque ln",
  "Exponentielle~Fonction croissante~Toujours positive~Propriete~exp(a+b)~Produit~Reciproque~ln~Asymptote~y=0",
  "Reconnaitre un modele exponentiel|Identifier le taux et le facteur|Ecrire la fonction|Etudier variations et limites|Resoudre avec ln",
  "Confondre exp(t) et 1+t|Appliquer ln a une valeur negative|Oublier que exp est toujours positive|Melanger taux continu et annuel",
  "Croissance 3~2 exp(0,03t)~Apres 5 ans~2,32 millions~Depreciation~exp(-kt)~Doublement~ln(2)/k~Racine~exp(2x)=1",
  "Croissance continue~Facteur exp(t)~Croissance annuelle~Facteur 1+t~Taux positif~Fonction croissante~Taux negatif~Fonction decroissante",
  "exp(x)~Tend vers l'infini~exp(-x)~Tend vers 0~ln(x)~Reciproque~Semi-logarithmique~Droite"))


# ============================================================ C09
add("C09", "Logarithme neperien et lecture des echelles", "Maths", ["Terminale"],
S("La fonction logarithme neperien, notee ln, est la reciproque de la fonction exponentielle sur l'intervalle ouvert zero a l'infini.|"
  "ln(x) n'est definie que pour x strictement positif ; on a ln(1) = 0 et ln(e) = 1.|"
  "La fonction ln est strictement croissante et concave sur son domaine de definition.|"
  "Pour a et b positifs, ln(a x b) = ln(a) + ln(b) et ln(a/b) = ln(a) - ln(b).|"
  "La propriete ln(a puissance n) = n ln(a) transforme une puissance en produit.|"
  "Resoudre exp(x) = a revient a ecrire x = ln(a) ; resoudre ln(x) = b revient a x = exp(b).|"
  "Une echelle logarithmique remplace une grandeur par son logarithme afin de traiter des ecarts tres importants.|"
  "Le decibel mesure un rapport de puissances et l'echelle de pH, qui mesure l'acidite, est egalement logarithmique.|"
  "Sur un graphique semi-logarithmique, une droite signale une croissance exponentielle.|"
  "Le temps de doublement d'une croissance continue de taux k se calcule par ln(2) divise par k.|"
  "Un ecart constant sur une echelle logarithmique correspond a une multiplication par une constante.|"
  "Les valeurs negatives et la valeur zero n'ont pas de logarithme : cette contrainte de domaine doit toujours être verifiee."),
[QC("Quel est le domaine de definition de la fonction ln ?", "Les reels~Les reels strictement positifs~Les reels positifs ou nul~Les reels superieurs a 1", 1,
     "ln(x) n'existe que pour x strictement positif."),
 QC("Quelle est la valeur de ln(1) ?", "0~1~e~Indefinie", 0,
     "Comme exp(0) = 1, la reciproque donne ln(1) = 0."),
 QC("Que vaut ln(a x b) pour a et b positifs ?", "ln(a) + ln(b)~ln(a) x ln(b)~ln(a+b)~ln(a) - ln(b)", 0,
     "Le logarithme transforme un produit en somme."),
 QC("La fonction ln est ...", "Decroissante et convexe~Croissante et concave~Constante~Non definie pour x > 1", 1,
     "ln est strictement croissante et concave sur son domaine."),
 QC("Pour resoudre ln(x) = 3, on ecrit ...", "x = exp(3)~x = 3~x = ln(3)~x = 1/3", 0,
     "On applique la fonction exponentielle des deux cotes."),
 QC("Le temps de doublement avec un taux continu k vaut ...", "ln(2)/k~2/k~k/ln(2)~exp(k)", 0,
     "On resout exp(k t) = 2, soit k t = ln(2)."),
 QC("Une echelle logarithmique permet de ...", "Representer des ecarts de grande amplitude~Supprimer les valeurs negatives~Rendre toutes les courbes droites~Eviter les arrondis", 0,
     "Compresser les grandes valeurs rend lisibles des phenomenes tres etendus."),
 QT("Resoudre l'equation exp(2x) = 5 puis l'equation ln(3x - 1) = 2, en precisant les conditions.",
    "Pour exp(2x) = 5, on applique ln des deux cotes : 2x = ln(5), donc x = ln(5)/2. Comme ln(5) est environ 1,609, on obtient x environ 0,8045. L'exponentielle etant positive, l'equation admet toujours une solution pour un second membre positif. Pour ln(3x - 1) = 2, il faut d'abord imposer 3x - 1 > 0, soit x > 1/3. On applique ensuite l'exponentielle : 3x - 1 = exp(2), donc 3x = exp(2) + 1 et x = (exp(2) + 1)/3. Comme exp(2) est environ 7,389, x vaut environ 2,796, ce qui respecte la condition. La verification du domaine est indispensable avant de valider une solution.",
    "On attend les deux solutions exactes, les valeurs approchees et la condition 3x-1 > 0 pour la seconde equation."),
 QT("Expliquer pourquoi l'echelle de pH est logarithmique et montrer l'effet d'une variation d'une unite.",
    "Le pH est defini par l'oppose du logarithme decimal de la concentration en ions hydrogenes : pH = -log10(H+). Comme les concentrations varient sur plusieurs puissances de dix, le logarithme rend les valeurs lisibles. Une diminution d'une unite de pH signifie que la concentration est multipliee par 10 : un pH de 3 est dix fois plus acide qu'un pH de 4 et cent fois plus acide qu'un pH de 5. De meme, une augmentation d'une unite divise la concentration par 10. Une echelle lineaire masquerait les ecarts entre les solutions faiblement acides et fortement acides. C'est pourquoi les echelles logarithmiques sont utilisees aussi pour le bruit en decibels et pour la magnitude des tremblements de terre.",
    "On attend la definition par le logarithme, la multiplication par 10 par unite et la justification de la compression des ecarts.")],
C("Le logarithme neperien est la reciproque de l'exponentielle : il transforme produits en sommes et puissances en produits.",
  "ln(ab) = ln a + ln b · ln(a^n) = n ln a",
  "Domaine : x > 0 · ln(1) = 0 · ln(e) = 1",
  "Definition~Reciproque de exp~Domaine positif~Propriete~Produit en somme~Puissance en produit~Echelle~Compression des ecarts",
  "Verifier le domaine de definition|Choisir la propriete de ln adaptee|Transformer l'equation|Resoudre puis verifier|Interpreter dans le contexte",
  "Prendre ln d'une valeur negative|Oublier ln(1) = 0|Confondre ln et log decimal|Ne pas verifier la condition initiale",
  "Equation~exp(2x)=5~Solution~ln(5)/2~Domaine~3x-1>0~pH~Echelle logarithmique~Doublement~ln(2)/k",
  "ln~Reciproque de exp~log decimal~Base 10~Echelle lineaire~Ecart constant~Echelle log~Rapport constant",
  "ln(a+b)~Aucune regle simple~ln(ab)~Somme~ln(a/b)~Difference~ln(a^n)~Produit"))


# ============================================================ C10
add("C10", "Loi binomiale et repetition d'epreuves", "Maths", ["Terminale"],
S("Une epreuve de Bernoulli a deux issues seulement : succes de probabilite p et echec de probabilite 1 - p.|"
  "Lorsqu'on repete n epreuves de Bernoulli independantes et identiques, on parle de schema de Bernoulli.|"
  "La variable aleatoire X compte le nombre de succes obtenus parmi les n epreuves.|"
  "La variable X suit une loi binomiale de parametres n et p, notee B(n, p).|"
  "La probabilite d'obtenir exactement k succes vaut P(X = k) = C(n, k) p puissance k (1 - p) puissance (n - k).|"
  "Le nombre de combinaisons C(n, k) compte les facons de choisir les k succes parmi les n epreuves.|"
  "Les probabilites associees a toutes les valeurs de zero a n ont une somme egale a 1.|"
  "L'esperance de X vaut n p et sa variance vaut n p (1 - p).|"
  "La probabilite d'obtenir au moins un succes est 1 - P(X = 0), soit 1 - (1 - p) puissance n.|"
  "Un arbre pondere ou la fonction binomiale de la calculatrice permettent de calculer chaque probabilite.|"
  "Ce schema s'applique au controle qualite, aux sondages et a la repetition de lancers.|"
  "L'independance des epreuves est indispensable : sans elle, les formules de la loi binomiale ne sont pas valables."),
[QC("Combien d'issues possede une epreuve de Bernoulli ?", "Une~Deux~Trois~Un nombre quelconque", 1,
     "Les deux issues sont succes et echec."),
 QC("Que compte la variable X dans une loi binomiale ?", "Le nombre d'echecs~Le nombre de succes~La somme des probabilites~Le nombre d'epreuves", 1,
     "X represente le nombre de succes parmi les n epreuves."),
 QC("Quelle est l'esperance d'une loi B(n, p) ?", "p~n~n p~n p (1-p)", 2,
     "L'esperance d'une loi binomiale est le produit n p."),
 QC("La variance d'une loi B(n, p) vaut ...", "n p~p(1-p)~n p(1-p)~n^2 p", 2,
     "La variance est n p (1 - p)."),
 QC("Comment obtenir la probabilite d'au moins un succes ?", "P(X=0)~1 - P(X=0)~P(X=1)~1 - P(X=1)", 1,
     "L'evenement contraire de au moins un succes est aucun succes."),
 QC("Dans la formule, que represente C(n, k) ?", "La probabilite de reussite~Le nombre de facons de choisir k succes~L'esperance~La variance", 1,
     "C(n, k) est le nombre de combinaisons de k elements parmi n."),
 QC("Quelle condition est necessaire pour appliquer la loi binomiale ?", "Que p soit superieur a 0,5~Que les epreuves soient independantes~Que n soit pair~Que X soit negative", 1,
     "Les epreuves doivent etre independantes et avoir la meme probabilite p."),
 QT("Dans un lot de 200 pieces, 5 pour cent sont defectueuses. On preleve 10 pieces avec remise. Calculer la probabilite qu'il y ait exactement une piece defectueuse, puis au moins une.",
    "Chaque prelevement est une epreuve de Bernoulli avec p = 0,05 de succes si l'on compte une piece defectueuse, et n = 10 epreuves independantes puisqu'il y a remise. On a donc X suit B(10 ; 0,05). Pour exactement une piece defectueuse : P(X = 1) = C(10, 1) x 0,05 x 0,95 puissance 9 = 10 x 0,05 x 0,6302, soit environ 0,3151. Pour au moins une piece defectueuse, on utilise l'evenement contraire : P(X >= 1) = 1 - P(X = 0) = 1 - 0,95 puissance 10. Comme 0,95 puissance 10 est environ 0,5987, on obtient environ 0,4013. On peut verifier avec la calculatrice que la somme des probabilites de 0 a 10 vaut bien 1.",
    "On attend l'identification B(10 ; 0,05), le calcul de P(X=1) environ 0,315 et celui de P(X>=1) environ 0,401 par l'evenement contraire."),
 QT("Expliquer pourquoi le schema binomial ne s'applique pas a un tirage sans remise et quelle loi convient alors.",
    "La loi binomiale suppose que la probabilite p reste la meme a chaque epreuve et que les epreuves soient independantes. Lors d'un tirage sans remise dans une urne ou un lot fini, prelever un objet modifie la composition du reste : la probabilite de l'issue suivante change et les tirages sont dependants. Les formules P(X = k) = C(n, k) p^k (1-p)^(n-k) et n p ne sont donc pas valables. Il faut utiliser la loi hypergeometrique, qui fait intervenir les combinaisons du nombre total d'objets, du nombre d'objets favorables et de la taille du prelevement. Si le prelevement reste petit devant la population, la loi binomiale constitue une approximation acceptable, mais il faut le signaler explicitement.",
    "On doit expliquer la modification de probabilite, la perte d'independance, citer la loi hypergeometrique et la condition d'approximation.")],
C("La loi binomiale compte les succes lors de n epreuves independantes ayant la meme probabilite p.",
  "P(X=k) = C(n,k) p^k (1-p)^(n-k)",
  "E(X) = n p · V(X) = n p (1-p)",
  "Bernoulli~Succes ou echec~Parametre p~Probabilite de succes~Parametre n~Nombre d'epreuves~Combinaison~Choix des succes~Esperance~n p",
  "Verifier independance et probabilite constante|Identifier n et p|Definir l'evenement X=k|Calculer avec la formule ou la calculatrice|Interpreter le resultat",
  "Oublier que p doit etre constant|Confondre esperance et variance|Additionner les probabilites au lieu de multiplier|Ignorer le cas sans remise",
  "Lot 200~5 pour cent defectueux~10 pieces~B(10 ; 0,05)~Une defectueuse~0,315~Au moins une~0,401~Sans remise~Loi hypergeometrique",
  "Avec remise~Epreuves independantes~Sans remise~Epreuves dependantes~Bernoulli~Une epreuve~Binomiale~Repetition de Bernoulli",
  "P(X=k)~Exactement k succes~P(X>=1)~Au moins un succes~P(X=0)~Aucun succes~Evenement contraire~1 moins P"))


# ============================================================ C11
add("C11", "Intervalle de confiance et estimation", "Maths", ["Terminale"],
S("Une population est l'ensemble complet des individus etudies ; un echantillon en est une partie seulement.|"
  "Une estimation ponctuelle fournit une seule valeur approchee d'un parametre inconnu.|"
  "La frequence observee dans l'echantillon sert a estimer une proportion dans la population.|"
  "Un intervalle de confiance donne une plage de valeurs plausibles pour le parametre, avec un niveau de confiance.|"
  "Le niveau le plus courant est 95 pour cent : sur un grand nombre d'echantillons, 95 pour cent des intervalles contiennent la vraie valeur.|"
  "La marge d'erreur maximale d'une proportion vaut environ 1 divise par la racine carree de la taille de l'echantillon.|"
  "Pour diviser la marge d'erreur par deux, il faut multiplier la taille de l'echantillon par quatre.|"
  "Un echantillon representatif est tire au hasard et suffisamment grand ; il evite les biais de selection.|"
  "Un sondage telephone ou en ligne peut etre biaise si certaines categories sont sous-representees.|"
  "On communique le resultat avec la proportion estimee, la marge d'erreur, le niveau de confiance et la taille de l'echantillon.|"
  "L'intervalle ne signifie pas que la vraie valeur a 95 pour cent de chances d'etre dedans : c'est la methode qui a cette fiabilite.|"
  "Toute estimation doit preciser la date, la source et la population interrogee pour etre verifiable."),
[QC("Qu'est-ce qu'un echantillon ?", "La totalite de la population~Une partie de la population~Un parametre~Une marge d'erreur", 1,
     "L'echantillon est un sous-ensemble representatif de la population etudiee."),
 QC("Que fournit une estimation ponctuelle ?", "Une plage de valeurs~Une seule valeur approchee~Une probabilite~Un echantillon", 1,
     "L'estimation ponctuelle donne une valeur unique, par exemple une frequence observee."),
 QC("Quel niveau de confiance est le plus courant ?", "50 pour cent~90 pour cent~95 pour cent~100 pour cent", 2,
     "Le niveau de 95 pour cent est la convention la plus utilisee dans les sondages."),
 QC("La marge d'erreur maximale d'une proportion est environ ...", "1/n~1/racine carree de n~n~racine carree de n", 1,
     "Elle est inversement proportionnelle a la racine carree de la taille de l'echantillon."),
 QC("Pour reduire la marge d'erreur de moitie, on multiplie la taille par ...", "2~4~10~1/2", 1,
     "Comme la marge varie en 1/racine(n), il faut quatre fois plus d'individus."),
 QC("Un sondage representatif doit etre ...", "Tire au hasard et suffisamment grand~Fait sur les seuls volontaires~Fait un jour de semaine~Limite a une ville", 0,
     "Le tirage au hasard et une taille suffisante limitent les biais de selection."),
 QC("Que faut-il communiquer avec une proportion estimee ?", "La marge d'erreur et la taille de l'echantillon~Seule la proportion~Le nom du sondager~La date du jour uniquement", 0,
     "Une estimation complete indique la valeur, la marge, le niveau de confiance et l'effectif."),
 QT("Un sondage aupres de 400 eleves donne 60 pour d'entre eux favorables a une mesure. Donner l'intervalle de confiance au niveau 95 pour cent et l'interpretation.",
    "La proportion estimee est p = 0,60. La marge d'erreur maximale au niveau 95 pour cent est environ 1 / racine carree de 400, soit 1/20 = 0,05, donc 5 points de pourcentage. L'intervalle de confiance est donc 0,60 - 0,05 a 0,60 + 0,05, c'est-a-dire de 55 pour cent a 65 pour cent. On peut dire que, selon la methode utilisee, 95 pour cent des intervalles construits de cette facon sur des echantillons de meme taille contiennent la proportion veritable dans la population des eleves. Il faut en revanche eviter de dire que la vraie proportion a 95 pour cent de chances d'etre entre 55 et 65 pour cent : la proportion est fixe, c'est l'intervalle qui est aleatoire.",
    "On attend le calcul 1/racine(400)=0,05, l'intervalle [55 pour cent ; 65 pour cent] et l'interpretation correcte du niveau de confiance."),
 QT("Expliquer les principaux biais qui peuvent rendre un sondage non representatif et comment les limiter.",
    "Un biais de selection apparait quand on interroge uniquement des volontaires ou une categorie trop homogene, par exemple les eleves presents un jour donne. Un biais de non-reponse survient lorsque les personnes refusees different systematiquement des autres. Un biais de formulation apparait si la question est ambigue ou orientee. Un biais de couverture existe quand une partie de la population ne peut pas etre atteinte, par exemple les personnes sans telephone. Pour les limiter, on tire les individus au hasard dans une liste exhaustive, on fixe une taille suffisante, on formule des questions neutres et on publie le taux de reponse. On presente enfin les resultats avec la marge d'erreur et la description exacte de la population interrogee, afin que le lecteur puisse juger la portee des conclusions.",
    "On attend plusieurs types de biais, des moyens de les reduire et la necessite de documenter la population et la marge d'erreur.")],
C("Estimer, c'est donner une valeur et une marge d'incertitude issues d'un echantillon representatif.",
  "Marge d'erreur maximale environ 1 / racine(n)",
  "Niveau de confiance 95 pour cent · intervalle = p +/- marge",
  "Population~Ensemble complet~Echantillon~Partie observee~Proportion~Frequence estimee~Marge~Incertitude~Intervalle~Plage plausible",
  "Definir la population cible|Construire un echantillon au hasard|Calculer la proportion et la marge|Donner l'intervalle de confiance|Communiquer les limites de l'estimation",
  "Confondre echantillon et population|Oublier la marge d'erreur|Mal interprester le niveau de confiance|Negliger les biais de selection",
  "Sondage 400~60 pour cent favorables~Marge~5 points~Intervalle~55 a 65 pour cent~Biais~Volontaires~Taille~4 fois pour diviser par 2",
  "Estimation ponctuelle~Une seule valeur~Intervalle~Plage de valeurs~Niveau 95~Fiabilite de lamethode~Biais~Erreur systematique",
  "1/racine(n)~Marge maximale~n quadruple~Marge divisee par deux~Tirage au hasard~Representativite~Taux de reponse~Qualite"))


# ============================================================ C12
add("C12", "The present perfect for experience and results", "Anglais", ["1re"],
S("The present perfect is formed with have or has followed by the past participle of the verb.|"
  "We use it to talk about a past action that has a result or a consequence in the present.|"
  "We also use it to describe personal experience, without saying exactly when it happened.|"
  "I have worked in a bank means that the experience is relevant now; I worked in a bank in 2019 refers to a finished time.|"
  "Common signal words are ever, never, already, yet, just, since, for and recently.|"
  "With for and since, the action often continues: for is followed by a duration and since by a starting point.|"
  "The negative form uses have not or has not, often shortened to haven't or hasn't.|"
  "The question form inverts the subject and the auxiliary: Have you ever managed a team?|"
  "The past simple is used for a finished action at a precise time, often with yesterday, last year or in 2020.|"
  "We do not use the present perfect with a finished time expression: say I saw her yesterday, not I have seen her yesterday.|"
  "In a CV or an interview, the present perfect introduces experience and the past simple gives precise details.|"
  "He has worked here for five years means he still works here; he worked here for five years means he no longer does."),
[QC("How is the present perfect formed?", "Have or has plus the past participle~Was or were plus the -ing form~Will plus the infinitive~Did plus the infinitive", 0,
     "The auxiliary have or has is followed by the past participle, for example has finished."),
 QC("Which sentence describes personal experience without a precise time?", "I visited Paris in 2020~I have visited Paris~I am visiting Paris~I will visit Paris", 1,
     "The present perfect presents the experience as relevant now, without dating it."),
 QC("Which word usually introduces a duration?", "Since~For~Yesterday~Already", 1,
     "For is followed by a length of time: for three years. Since introduces a starting point."),
 QC("Choose the correct negative form.", "He hasn't finished~He haven't finished~He doesn't has finished~He not has finished", 0,
     "With the third person singular, the auxiliary is has and the negative is hasn't."),
 QC("Which time expression cannot be used with the present perfect?", "Already~Yet~Yesterday~Recently", 2,
     "Yesterday is a finished time expression and requires the past simple."),
 QC("What does She has lived here for ten years mean?", "She still lives here~She no longer lives here~She will move~She lived here long ago", 0,
     "With for and a continuing situation, the present perfect links the past to the present."),
 QC("How do you form a question with the present perfect?", "Invert the subject and have or has~Add do at the end~Use was before the subject~Put never first", 0,
     "For example: Have you ever led a project?"),
 QT("Complete and explain: I (never / use) a spreadsheet before I joined this company. Then give the past simple form of the same idea with a precise date.",
    "The correct form is: I have never used a spreadsheet before I joined this company. The present perfect is required because the experience is presented as a situation valid up to now, and the word never is placed between the auxiliary and the past participle. The verb use becomes used, the past participle of the regular verb. With a precise finished time, the past simple is needed: I used a spreadsheet for the first time in 2021, or I did not use any spreadsheet in 2020. The key difference is the presence of a finished time expression, which excludes the present perfect.",
    "The answer must give have never used, explain the position of never and the past participle, and give a correct past simple sentence with a precise date."),
 QT("Explain how to use the present perfect and the past simple together when talking about your professional experience in an interview.",
    "A natural answer starts with the present perfect to introduce the experience: I have worked in customer service for three years. Then the past simple gives precise details about a finished event: Last year I handled a difficult complaint and I received a letter of thanks from the manager. The present perfect answers the question What experience do you have?, while the past simple answers What exactly happened then?. Signal words help the listener: for, since, ever and already usually go with the present perfect, while yesterday, last week, in 2019 and two days ago go with the past simple. Mixing the two tenses correctly shows that the candidate can link past facts to present skills, which is exactly what an employer wants to see.",
    "The answer must present both tenses, give an example of each, mention signal words and link the tenses to the idea of present relevance.")],
C("The present perfect links a past action to the present; the past simple places it at a finished time.",
  "have or has + past participle",
  "for + duration · since + starting point · ever / never / already / yet",
  "Form~Have or has plus participle~Use~Past action with present result~Experience~Life achievements~Signal~Ever, never, already~Contrast~Past simple",
  "Identify whether the time is finished|Choose have or has|Write the past participle|Place the signal word correctly|Check the meaning and the time expression",
  "Using the present perfect with yesterday|Forgetting the past participle|Mixing for and since|Confusing have and has",
  "Experience~I have worked in a bank~Result~She has finished the report~Duration~for three years~Starting point~since 2021~Precise time~in 2019",
  "Present perfect~Linked to now~Past simple~Finished time~Ever and never~Experience~Already and yet~Result expected",
  "For~Duration~Since~Starting point~Have~I, you, we, they~Has~He, she, it"))


# ============================================================ C13
add("C13", "Modal verbs at work: obligation, advice, permission", "Anglais", ["1re", "Terminale"],
S("Modal verbs are auxiliary verbs that express obligation, advice, permission, ability or possibility.|"
  "They are followed by a bare infinitive, without to: You must finish, not You must to finish.|"
  "Must expresses a strong obligation that comes from the speaker or from a rule.|"
  "Have to expresses an external obligation imposed by circumstances or by another person.|"
  "Should and ought to express advice or recommendation; they are softer than must.|"
  "Can expresses ability or informal permission, while could is the past form and also a polite request.|"
  "May expresses formal permission or possibility, while might expresses a weaker possibility.|"
  "Must not expresses a prohibition, whereas do not have to means that there is no obligation.|"
  "Needn't also means that something is not necessary, without expressing a prohibition.|"
  "At work, You must wear protective equipment states a rule, while You should check the figures gives advice.|"
  "Modal verbs do not take an s at the third person singular: He can drive, not He cans drive.|"
  "Questions are formed by inversion: May I leave early? Could you send the report?"),
[QC("Which structure is correct after a modal verb?", "He must to go~He must go~He musts go~He must going", 1,
     "A modal verb is followed by the bare infinitive, without to and without an s."),
 QC("Which modal expresses an external obligation?", "Must~Have to~Might~Needn't", 1,
     "Have to describes an obligation coming from outside, while must often comes from the speaker."),
 QC("What does Must not mean?", "It is not necessary~It is forbidden~It is possible~It is advised", 1,
     "Must not expresses a prohibition; do not have to expresses absence of obligation."),
 QC("Which modal is the most polite for a request?", "Must~Can~Could~Will", 2,
     "Could you...? is a polite and common way to make a request at work."),
 QC("What does Should express?", "A strong rule~Advice~A prohibition~A past habit", 1,
     "Should gives advice or a recommendation and is softer than must."),
 QC("Which sentence is grammatically correct?", "She cans drive~She can drive~She can drives~She can to drive", 1,
     "The modal does not take an s at the third person singular."),
 QC("What is the difference between must not and needn't?", "They are identical~Must not forbids, needn't says it is not necessary~Needn't is stronger~Must not is a question form", 1,
     "Needn't means there is no obligation, while must not means it is forbidden."),
 QT("Rewrite these ideas with the correct modal verb and explain your choice: (1) it is compulsory to wear a badge; (2) it is a good idea to arrive early; (3) it is forbidden to use a personal phone during the meeting.",
    "(1) You must wear a badge. The rule is presented as compulsory, so must is appropriate. (2) You should arrive early. This is advice, not a rule, so should is the right modal. (3) You must not use a personal phone during the meeting. A prohibition is expressed by must not, and not by do not have to, which would only mean that using a phone is not required. In each case, the modal is followed by the bare infinitive: wear, arrive, use, with no to and no third-person s.",
    "The answer must give must wear, should arrive and must not use, and explain the difference between obligation, advice and prohibition."),
 QT("Explain how to ask for permission and make a request politely in a professional email, with two examples.",
    "In a professional email, direct commands can sound rude, so modal verbs soften the request. For permission, May I...? is formal and clear: May I leave fifteen minutes early on Friday? For a request, Could you...? is polite and widely used: Could you send me the updated figures before Thursday? Would you mind...? is even more indirect and is followed by the -ing form: Would you mind checking the attachment? Can I...? is acceptable in an informal internal message but is less formal than May I...? In all cases, the modal is followed by the bare infinitive except after Would you mind, and the sentence ends with a question mark. Adding please and a thank-you formula keeps the tone cooperative without becoming vague.",
    "The answer must give at least two correct examples, explain the degree of formality and respect the bare infinitive rule.")],
C("Modal verbs show the speaker's attitude: obligation, advice, permission, ability or possibility.",
  "modal + bare infinitive (no to, no -s)",
  "must / have to · should · can / could · may / might",
  "Obligation~Must or have to~Advice~Should~Permission~May or can~Prohibition~Must not~No obligation~Needn't",
  "Identify the intention of the sentence|Choose the right modal|Use the bare infinitive|Check the negative form|Check politeness and context",
  "Adding to after a modal|Adding an s at the third person|Confusing must not and needn't|Using must for simple advice",
  "Safety rule~You must wear a badge~Advice~You should arrive early~Prohibition~You must not use a phone~Request~Could you send the report~Permission~May I leave early",
  "Must~Internal strong obligation~Have to~External obligation~Should~Advice~Might~Weak possibility",
  "Must not~Forbidden~Don't have to~Not required~Needn't~Not necessary~Could~Polite request"))


# ============================================================ C14
add("C14", "Writing a professional email in English", "Anglais", ["Terminale"],
S("A professional email is clear, concise and polite, with a precise subject line.|"
  "The subject line summarises the purpose, for example Meeting confirmed - Tuesday 14 May.|"
  "Choose an appropriate salutation: Dear Ms Martin, Dear Sir or Madam, or Hello Paul for a known contact.|"
  "Open with a short sentence stating your purpose: I am writing to confirm our appointment.|"
  "Organise the body into short paragraphs, one idea per paragraph, and use bullet points for lists.|"
  "Use neutral and polite language such as could you, would you mind and thank you for.|"
  "Avoid slang, emojis and excessive capital letters in a professional context.|"
  "Mention any attachment explicitly and check that it is actually attached before sending.|"
  "Close with a standard formula such as Kind regards, Best regards or Yours sincerely.|"
  "Include your name, your position and your contact details in the signature.|"
  "Proofread spelling, grammar, dates, names and figures before sending the message.|"
  "Reply within a reasonable time and keep a copy of important messages for later follow-up."),
[QC("What should a good subject line do?", "Describe every detail of the message~Summarise the purpose briefly~Contain the full signature~Replace the salutation", 1,
     "The subject line must be short and tell the reader what the email is about."),
 QC("Which salutation is suitable for an unknown recipient?", "Hi mate~Dear Sir or Madam~Hey~To whom", 1,
     "Dear Sir or Madam is the standard formal salutation when the name is unknown."),
 QC("What does I am writing to... introduce?", "The purpose of the email~The signature~The attachment~The date", 0,
     "This opening sentence states why the message is sent."),
 QC("Which expression is politely neutral?", "Give me the report~Could you send the report?~Send it now~I want the report", 1,
     "Could you...? is a polite request suitable for professional correspondence."),
 QC("What should you do before sending an email with a document?", "Close the computer~Check that the attachment is present~Delete the subject line~Add emojis", 1,
     "Forgetting an attachment is a common error that must be checked before sending."),
 QC("Which closing formula is correct after Dear Ms Martin?", "Cheers mate~Yours sincerely~See you~Bye now", 1,
     "Yours sincerely is used when the recipient's name is known; Yours faithfully follows Dear Sir or Madam."),
 QC("What should the signature contain?", "Only a first name~Name, position and contact details~A joke~The whole previous conversation", 1,
     "A professional signature identifies the sender and gives a way to reply."),
 QT("Write a short email to a supplier to ask for a revised quotation before Friday, and explain the structure you used.",
    "Subject: Request for revised quotation - order 245. Dear Mr Dubois, I am writing to ask for a revised quotation for order 245, as we would like to add ten units to the initial request. Could you send the updated document before Friday 18 May so that we can validate the budget? Please find attached the amended specification. Thank you for your help. Kind regards, Sophie Laurent, Purchasing Assistant, sophie.laurent@company.fr. The structure is: a precise subject line, a formal salutation, a purpose sentence, the request with a deadline, a mention of the attachment, a thank-you formula, a closing formula and a complete signature. Each paragraph contains one idea and the tone remains polite and direct.",
    "The answer must include subject, salutation, purpose, request, attachment, closing, signature and a short explanation of the structure."),
 QT("Explain three common mistakes in professional emails and how to avoid them.",
    "The first mistake is an empty or vague subject line, which makes the message hard to find later: it should summarise the purpose in a few words. The second mistake is a tone that is too familiar, with slang, emojis or capitalised words, which can appear unprofessional: neutral phrases and a suitable salutation should be used instead. The third mistake is forgetting the attachment or sending the wrong version of a document: the sender should mention the attachment explicitly and open it once before sending. Other frequent problems include unclear deadlines, spelling mistakes in names and figures, and an incomplete signature. A final proofreading step and a short checklist before sending prevent most of these errors.",
    "The answer must give three concrete mistakes with a correction for each and mention a final proofreading step.")],
C("A professional email combines a clear structure, a polite tone and careful checking before sending.",
  "Subject + salutation + purpose + body + closing + signature",
  "Could you...? · Would you mind...? · Thank you for...",
  "Subject~Purpose in brief~Salutation~Formal greeting~Body~One idea per paragraph~Attachment~Explicitly mentioned~Signature~Identity and contact",
  "Write a precise subject|Choose the salutation|State the purpose in one sentence|Develop one idea per paragraph|Proofread and check attachments",
  "Using an empty subject line|Writing in slang or capitals|Forgetting the attachment|Omitting the signature",
  "Request~Revised quotation~Deadline~Before Friday~Polite form~Could you send~Attachment~Amended specification~Closing~Kind regards",
  "Dear Sir or Madam~Unknown recipient~Yours faithfully~Formal closing~Dear Ms Martin~Known name~Yours sincerely~Matching closing",
  "Formal~Polite and neutral~Informal~Slang and short forms~Request~Could you~Instruction~Send me"))


# ============================================================ C15
add("C15", "Giving a short business presentation in English", "Anglais", ["Terminale"],
S("A short business presentation usually has three parts: an introduction, a development and a conclusion.|"
  "The introduction captures attention, gives the topic and states the plan.|"
  "Signposting phrases guide the listener: First, Then, Finally and To conclude.|"
  "The development should be limited to three main points so that the message stays memorable.|"
  "Each point should be supported by one clear example or figure.|"
  "Visual aids must remain simple: one idea per slide, a large font and few words.|"
  "Do not read the slides word for word; use short notes and speak naturally.|"
  "Timing matters: rehearse with a clock and keep a buffer for questions at the end.|"
  "Pronunciation and word stress help the listener: emphasise key words and pause after important ideas.|"
  "Eye contact and an open posture make the speaker appear confident and trustworthy.|"
  "Invite questions at the end with phrases such as Any questions? or What do you think?|"
  "If you do not know an answer, say so and promise to follow up by email rather than inventing a figure."),
[QC("How many main points are recommended in a short presentation?", "One~Three~Ten~As many as possible", 1,
     "Three points are easy to follow and to remember for the audience."),
 QC("What is the role of signposting phrases?", "To decorate the slides~To guide the listener through the talk~To replace the conclusion~To hide weak arguments", 1,
     "Phrases like First and Finally make the structure audible."),
 QC("What should a slide contain?", "One idea and few words~The full script~Several paragraphs~All the figures at once", 0,
     "Slides support the speech and should not duplicate it entirely."),
 QC("What does To conclude introduce?", "The first point~The final part~A question~An example", 1,
     "It signals that the speaker is moving to the conclusion."),
 QC("Why should you rehearse with a clock?", "To fill the time completely~To respect the time limit and leave room for questions~To avoid notes~To change the topic", 1,
     "Time management includes a buffer for the question session."),
 QC("What is a good reaction when you do not know an answer?", "Invent a figure~Say so and promise a written follow-up~Ignore the question~End the presentation immediately", 1,
     "Honesty and a concrete follow-up preserve credibility."),
 QC("Which behaviour helps the speaker look confident?", "Reading the slides aloud~Looking at the floor~Keeping eye contact and an open posture~Speaking very quickly", 2,
     "Eye contact and posture are important non-verbal signals."),
 QT("Plan a five-minute presentation about your company's new customer service process, with an introduction, three points and a conclusion.",
    "Introduction, about forty seconds: greet the audience, introduce the topic with a question such as How do we handle a customer request today?, then announce the plan: the problem, the new process and the expected benefits. First point, about one minute: the current process has three handovers and an average response time of two days. Give one concrete example of a delayed request. Second point, about one minute: the new process uses a single shared ticket, with an automatic acknowledgement and a clear owner for each request. Third point, about one minute: the expected results are a response within four hours and fewer duplicated tasks. Conclusion, about forty seconds: summarise the three points and end with an invitation: What do you think about this first step? Then leave time for questions. Use signposting phrases and slides with one idea each.",
    "The answer must include a clear three-part structure, one example or figure per point, signposting phrases, timing and an invitation to ask questions."),
 QT("Explain how to use voice and body language to make a short presentation more effective.",
    "Voice: speak a little slower than in conversation, vary the intonation and stress the key words so that the main ideas stand out. Pause for about one second after an important figure to let the audience absorb it. Avoid filler words such as um and er by replacing them with a short silence. Body language: stand with an open posture, keep your arms free, and look at different members of the audience rather than at the slides or the floor. Gestures should support the message, for example counting three points with the fingers, without becoming repetitive. Movement should be limited and intentional. Finally, smile at the beginning and thank the audience at the end. These signals reinforce credibility and make the content easier to follow, but they cannot compensate for a poorly prepared structure.",
    "The answer must cover pace, stress, pauses, filler words, posture, eye contact, gestures and the limits of non-verbal technique.")],
C("A good short presentation has a clear structure, three main points, simple slides and a confident delivery.",
  "Introduction + three points + conclusion + questions",
  "First · Then · Finally · To conclude · Any questions?",
  "Structure~Introduction and conclusion~Signposting~Guides the listener~Slide~One idea per slide~Timing~Rehearsal~Delivery~Voice and posture",
  "Define the message and the audience|Plan three main points|Prepare simple slides|Rehearse with a clock|Deliver and handle questions",
  "Reading the slides word for word|Overloading a slide with text|Ignoring the time limit|Inventing an answer to a question",
  "Topic~New service process~Point one~Two-day delay~Point two~Shared ticket~Point three~Four-hour response~Conclusion~Invitation to ask",
  "Introduction~Topic and plan~Development~Three main points~Conclusion~Summary~Questions~Follow-up",
  "Formal~Business context~Signposting~First, then, finally~Polite invitation~Any questions~Uncertain answer~I will follow up"))


# ============================================================ C16
add("C16", "Reading and understanding a job advertisement", "Anglais", ["1re"],
S("A job advertisement usually gives the job title, the company, the location and the type of contract.|"
  "The duties section describes the main tasks and the responsibilities of the position.|"
  "The requirements section lists qualifications, skills, experience and languages.|"
  "Essential requirements are compulsory, while desirable requirements are only advantages.|"
  "Keywords such as teamwork, deadline, budget and customer help identify the profile sought.|"
  "Transferable skills, for example organisation or communication, can come from school or from a previous job.|"
  "The salary, the benefits and the working hours are often mentioned near the end of the advertisement.|"
  "The application procedure states what to send, to whom and before which date.|"
  "A CV presents facts and dates, whereas a cover letter explains motivation and fit with the profile.|"
  "Adapt your CV to the advertisement by repeating relevant keywords honestly.|"
  "Check the date of publication, because an old advertisement may no longer be valid.|"
  "After applying, keep a copy of the advert and note the reference number for a later follow-up."),
[QC("Where are the main tasks of the position usually described?", "In the duties section~In the salary section~In the signature~In the date of publication", 0,
     "The duties or responsibilities section lists what the employee will do."),
 QC("What is the difference between essential and desirable requirements?", "Essential are compulsory, desirable are advantages~They are identical~Desirable are compulsory~Essential are optional", 0,
     "Essential requirements are mandatory; desirable ones simply improve the candidature."),
 QC("Which word is a typical keyword in a job advert?", "Teamwork~Yesterday~Colour~Weather", 0,
     "Teamwork, deadline, budget and customer are frequent keywords describing skills."),
 QC("What does a cover letter do?", "List dates only~Explain motivation and fit~Replace the CV~Give the salary", 1,
     "The cover letter connects the candidate's experience to the needs of the employer."),
 QC("What should you check before applying?", "The date of publication~The colour of the advert~The number of words~The name of the designer", 0,
     "An old advert may correspond to a position that is no longer open."),
 QC("What is a transferable skill?", "A skill usable in different contexts~A qualification that expires~A salary~A working hour", 0,
     "Organisation or communication learned at school can be used in a job."),
 QC("What should you keep after applying?", "A copy of the advert and the reference number~Nothing~Only the salary~The name of the recruiter's friend", 0,
     "Keeping the reference number allows a precise follow-up by email or phone."),
 QT("Read this extract: Essential: good command of English, ability to work to deadlines, basic knowledge of a spreadsheet. Desirable: previous experience in a call centre. Identify the essential requirements and explain how a STMG graduate can answer them.",
    "The essential requirements are three: a good command of English, the ability to work to deadlines and a basic knowledge of a spreadsheet. They are compulsory: a candidate who does not meet them is unlikely to be selected. The desirable requirement is previous experience in a call centre, which is only an advantage. A STMG graduate can answer the first requirement by mentioning English courses and, if possible, a short stay in an English-speaking country. For deadlines, the candidate can give a concrete example of a report or a presentation delivered on time at school or during a stage. For spreadsheets, the graduate can refer to the tableur lessons followed in the numerique course and to a concrete use, for example a budget prepared with formulas. The cover letter should use the same keywords as the advert, honestly and with examples.",
    "The answer must separate essential from desirable requirements and propose three concrete pieces of evidence linked to the STMG background."),
 QT("Explain how to adapt a CV and a cover letter to a specific job advertisement, and why this is more effective than sending the same application everywhere.",
    "Start by underlining the keywords of the advertisement: the job title, the main duties, the essential skills and the required language level. In the CV, place these keywords in the professional experience and skills sections when they correspond to real facts; for example, if budget management is required, mention the budget actually handled during a stage. In the cover letter, write three short paragraphs: why the company interests you, which two or three requirements you meet with concrete examples, and a polite call for an interview. A generic application does not show that the candidate has understood the specific needs of the employer, and recruiters often scan for keywords. Adapting the documents demonstrates motivation and saves the recruiter time, which increases the chance of being invited to an interview.",
    "The answer must describe keyword analysis, concrete adaptation of CV and cover letter, and explain the advantage over a generic application.")],
C("A job advert is a structured text: identify the duties, the essential and desirable requirements, and the application procedure.",
  "Job title + duties + requirements + salary + how to apply",
  "Essential = compulsory · desirable = advantage",
  "Job title~Position offered~Duties~Tasks~Requirements~Skills and qualifications~Salary~Pay and benefits~Application~What and when to send",
  "Read the title and the company|Underline the key duties|Separate essential and desirable requirements|Compare with your own skills|Prepare an adapted CV and letter",
  "Ignoring the date of publication|Applying without checking essential requirements|Sending the same generic CV everywhere|Forgetting the reference number",
  "Advert~Customer assistant~Essential~English and deadlines~Desirable~Call centre experience~Keyword~Teamwork~Follow-up~Reference number",
  "CV~Facts and dates~Cover letter~Motivation and fit~Essential~Mandatory~Desirable~Optional advantage",
  "Job title~Name of the position~Duties~What to do~Location~Where~Contract~Type and duration"))


# ============================================================ C17
add("C17", "L'explication de texte a l'oral du bac", "Methodologie", ["Terminale"],
S("L'explication de texte est un exercice oral : apres un temps de preparation, le candidat presente une lecture interpretee d'un extrait.|"
  "La preparation commence par une lecture attentive qui identifie le genre, le theme et le registre du texte.|"
  "On situe l'auteur, l'oeuvre et le contexte de publication en quelques phrases precises.|"
  "On degage une problematique, c'est-a-dire une question qui met en relation deux aspects du texte.|"
  "Le plan suit generalement deux ou trois axes qui organisent l'interpretation.|"
  "Chaque axe s'appuie sur des citations courtes, choisies pour leur pertinence plutot que pour leur longueur.|"
  "La citation doit etre introduite, lue avec expression, puis analysee dans ses mots et ses images.|"
  "L'analyse articule le releve des procedes d'ecriture et l'interpretation du sens produit.|"
  "Les transitions rendent visible le passage d'un axe a l'autre devant le jury.|"
  "L'expression orale exige une voix claire, un rythme pose et un regard adresse au jury.|"
  "La conclusion repond a la problematique et peut proposer une ouverture vers une autre oeuvre.|"
  "Le jury evalue la comprehension du texte, la qualite de l'analyse et la clarte de l'expression."),
[QC("Combien de temps faut-il consacrer a la lecture attentive du texte ?", "Aucun~Quelques minutes de preparation~Toute l'epreuve~Uniquement la conclusion", 1,
     "La lecture attentive est la premiere etape de la preparation et conduit au choix des axes."),
 QC("Qu'est-ce qu'une problematique ?", "Une citation longue~Une question qui relie deux aspects du texte~La biographie de l'auteur~La conclusion", 1,
     "Elle met en tension deux elements et donne au plan sa necessite."),
 QC("Un axe de plan doit etre ...", "Une citation~Un titre interpretatif~Une figure de style~La derniere phrase", 1,
     "L'axe porte une orientation de lecture, pas une simple repetition du texte."),
 QC("Comment traiter une citation ?", "La lire sans commentaire~L'introduire, la lire puis l'analyser~La remplacer par sa propre phrase~La mettre en conclusion", 1,
     "Une citation non analysee n'apporte aucun element d'interpretation."),
 QC("Quel element n'appartient pas a l'analyse ?", "Le releve d'un procede~L'interpretation d'une image~L'explication d'un mot~L'invention d'un evenement absent du texte", 3,
     "Il ne faut jamais inventer un fait qui n'est pas dans le texte ou son contexte."),
 QC("Que doit faire la conclusion ?", "Repondre a la problematique~Introduire un nouvel axe~Lire une nouvelle citation~Supprimer les transitions", 0,
     "Elle apporte une reponse et peut ouvrir le debat."),
 QC("Quel critere est evalue par le jury ?", "La seule vitesse de parole~La comprehension et la clarte de l'analyse~Le nombre de citations~La couleur de la copie", 1,
     "Le jury juge la comprehension du texte, l'analyse et l'expression orale."),
 QT("Decrire la methode pour passer d'une premiere lecture a un plan d'explication en deux axes.",
    "On lit une premiere fois le texte pour identifier le genre, le theme et le registre. On releve ensuite les elements qui reviennent : images, repetitions, oppositions ou changements de ton. On formule alors une problematique qui relie deux de ces observations, par exemple comment un poeme passe de la tristesse a l'espoir. On choisit deuxaxes : le premier decrit la construction de la tristesse, le second etudie le basculement vers l'espoir. Dans chaque axe, on selectionne deux ou trois citations courtes et on prepare pour chacune le procede a relever et l'effet a interpreter. On verifie enfin que les deux axes couvrent tout le texte et qu'une transition relie le passage du premier au second. Cette preparation rend l'oral fluide sans avoir a memoriser un texte ecrit.",
    "On attend lecture, releve des constantes, problematique, deux axes, citations analysees et verification de la couverture du texte."),
 QT("Expliquer comment lire une citation a l'oral et comment eviter les erreurs frequentes devant le jury.",
    "La citation doit etre courte et introduite par une phrase simple : le texte ecrit que... ou l'auteur denonce... On la lit avec une voix claire, en marquant la ponctuation et en s' arretant legerement apres les mots importants. On la commente ensuite sans la repetre : on nomme le procede, on explique le sens des mots, puis on relie l'effet a la problematique. Les erreurs frequentes sont la citation trop longue, lue sans introduction, l'analyse sautee au profit d'un simple commentaire general, et le regard fixe sur ses notes. Pour les eviter, on prepare une fiche avec les citations et trois mots cles par axe, on s'entraine a parler sans lire cette fiche et on regarde le jury regulierement. Enfin, on ne corrige pas une petite hesitation : on continue calmement la demonstration.",
    "On attend introduction de la citation, lecture expressi, analyse, et une liste d'erreurs avec les remedies correspondants.")],
C("L'explication de texte transforme une lecture attentive en une interpretation orale structuree et argumentee.",
  "Texte + problematique + axes + citations analysees",
  "Genre · theme · registre · procedes · effets",
  "lecture~Identifier genre et theme~Problematique~Question centrale~Axe~Titre interpretatif~Citation~Courte et analysee~Transition~Lien entre axes",
  "Lire le texte et relever les constantes|Formuler la problematique|Construire deux axes|Choisir les citations|Entrainer l'expression orale",
  "Reciter le texte sans analyser|Laisser une citation sans commentaire|Inventer un fait absent|Lire ses notes sans regarder le jury",
  "Poeme~Tristesse puis espoir~Axe un~Construction de la tristesse~Axe deux~Basculement~Citation~L'aube refleurit~Ouverture~Autre oeuvre",
  "Commentaire ecrit~Plan redige~Explication orale~Plan parle~Lecture~Premiere etape~Analyse~Deuxieme etape",
  "Voix~Claire et posee~Regard~Vers le jury~Rythme~Ni trop vite ni trop lent~Fiche~Appui discret"))


# ============================================================ C18
add("C18", "Preparer l'epreuve de mathematiques du bac technologique", "Methodologie", ["Terminale"],
S("L'epreuve de mathematiques du baccalauréat technologique dure deux heures et comporte plusieurs exercices.|"
  "Les exercices sont souvent decoupes en parties independantes ou partiellement liees.|"
  "On lit d'abord tout le sujet pour reperer les exercices les plus accessibles.|"
  "La calculatrice est autorisee : il faut savoir utiliser les fonctions de calcul, de graphe et de statistique.|"
  "On note les donnees, les notations et les resultats intermediaires pour faciliter la relecture.|"
  "Toute assertion importante doit etre justifiee par un calcul ou par une propriete citee.|"
  "Les etapes de calcul doivent etre lisibles, environ une ligne par operation.|"
  "On gere son temps en revenant aux questions laissees de cote apres avoir traite les autres.|"
  "Les questions de lecture graphique exigent une lecture precise des axes, des unites et des points.|"
  "Les exercices de probabilites demandent de delimiter l'univers et de nommer clairement les evenements.|"
  "Une verification finale porte sur les unites, les arrondis et la coherence des resultats.|"
  "Une copie propre et aeree facilite la lecture du correcteur et valorise la demarche."),
[QC("Que faut-il faire des le debut de l'epreuve ?", "Commencer par le dernier exercice~Lire tout le sujet~Utiliser la calculatrice sans lire~Ecrire la conclusion", 1,
     "Une lecture globale permet de choisir l'ordre des exercices et d'gerer le temps."),
 QC("Comment justifier une affirmation dans une copie ?", "Par un calcul ou une propriete citee~Par une intuition~Par le resultat final seul~Par la couleur du stylo", 0,
     "Le correcteur attend une justification visible de la demarche."),
 QC("Que faut-il faire d'une question difficile en premier lieu ?", "La laisser de cote et y revenir~Laisser la copie vide~La copier au hasard~Refuser de continuer", 0,
     "Traiter d'abord les questions accessibles permet de sécuriser les points."),
 QC("Dans un exercice de probabilites, que faut-il delimiter ?", "L'univers des resultats~La couleur du graphique~Le nombre de pages~Le type de calculatrice", 0,
     "Sans univers clairement defini, les evenements et les probabilites sont ambigus."),
 QC("Quel element n'est pas verifie en fin de copie ?", "Les unites~La coherence des resultats~Les arrondis~La longueur du nom de l'eleve", 3,
     "La verification porte sur le fond du calcul et la presentation, pas sur des elements administratifs."),
 QC("Une lecture graphique exige ...", "De lire les axes et les unites~De deviner la reponse~D'ignorer les points~De changer d'exercice", 0,
     "La precision de lecture des axes et des units est essentielle."),
 QC("Une copie aeree ...", "Facilite la lecture et valorise la demarche~Remplace les justifications~Est interdite~Cache les calculs", 0,
     "La clarte de la presentation aide le correcteur a suivre le raisonnement."),
 QT("Decrire une strategie de gestion du temps pour une epreuve de deux heures comportant quatre exercices.",
    "On consacre les cinq premieres minutes a une lecture complete du sujet et a un classement des exercices par difficulte perçue. On traite ensuite les deux exercices les plus accessibles sur environ cinquante minutes, en ecrivant chaque etape de calcul de maniere lisible. On accorde ensuite quarante minutes aux deux exercices restants, en sautant une question bloquee plutot que de s'y attarder. On garde dix minutes pour revenir aux questions laissees de cote et dix dernieres minutes pour la verification : unites, arrondis, coherence des resultats et presence des justifications. Si une question reste sans reponse, on ecrit au moins la methode envisagee, car la demarche est partiellement valorisee. Cette organisation evite de passer trop de temps sur un seul exercice.",
    "On attend lecture initiale, choix de l'ordre, blocs de temps pour chaque exercice, retour aux questions sautees et phase finale de verification."),
 QT("Expliquer pourquoi une copie lisible et justifiee est valorisee, meme lorsque le resultat final est inexact.",
    "Le correcteur evalue une demarche, pas seulement un chiffre. Lorsque les etapes sont ecrites clairement, il peut identifier la propriete utilisee, la formule choisie et le calcul intermediaire, et attribuer les points correspondants meme si une erreur arithmetique modifie le resultat final. Une justification courte, comme l'application d'un theoreme ou la resolution d'une equation, rend visible la competence de l'eleve. A l'inverse, une copie ou le raisonnement est cache ne permet pas de donner ces points. Il faut donc ecrire les hypotheses, nommer les evenements en probabilites, faire apparaitre les calculs intermediaires et encadrer le resultat. La relecture finale verifie aussi que chaque question a recu une reponse et que les unites sont indiquees.",
    "On attend l'idee de notation de la demarche, des exemples de justifications et le lien entre lisibilite et attribution des points.")],
C("Reussir une epreuve de maths, c'est lire, organiser, justifier et verifier, autant que calculer.",
  "Lecture du sujet + gestion du temps + demarche justifiee",
  "Calculatrice · notation des etapes · verification finale",
  "Sujet~Lecture globale~Temps~Repartition des exercices~Justification~Propriete et calcul~Copie~Clarte et aeration~Verification~Unites et coherence",
  "Lire tout le sujet et classer les exercices|Traiter les questions accessibles|Ecrire chaque etape de calcul|Revenir aux questions sautees|Verifier unites, arrondis et coherence",
  "Se lancer sans lire le sujet|Passer trop de temps sur une question|Ne donner que le resultat final|Oublier les unites",
  "Epreuve~Deux heures~Quatre exercices~Ordre choisi~Question bloquee~Mise en attente~Demarche~Points partiels~Resultat~Encadrement",
  "Calculatrice~Outil autorise~Raisonnement~Demarche ecrite~Resultat~Reponse finale~Verification~Controle de coherence",
  "Copie propre~Lecture facile~Calcul lisible~Une ligne par operation~Justification~Texte ou formule~Arrondi~En fin de calcul"))


# ============================================================ C19
add("C19", "Rechercher un stage et preparer son orientation", "Methodologie", ["1re"],
S("Un stage permet de decouvrir un metier, d'observer une organisation et de valider un projet d'orientation.|"
  "La recherche commence par un inventaire des secteurs, des entreprises et des contacts possibles.|"
  "Le CV presente de maniere concise l'identite, la formation, les competences et les experiences.|"
  "La lettre de motivation explique pourquoi l'entreprise est visee et ce que le candidat peut apporter.|"
  "On adapte chaque candidature avec des exemples precis et en evitant les formules generiques.|"
  "Une convention de stage, signee avant le debut, definit les dates, les horaires et le tuteur.|"
  "Le tuteur accompagne l'eleve, valide les objectifs et evalue les acquis en fin de periode.|"
  "Le rapport de stage decrit l'entreprise, les missions realisees et les apprentissages.|"
  "L'entretien se prepare : on se documente sur l'entreprise et on formule quelques questions.|"
  "La ponctualite, une tenue adaptee et l'ecoute active sont observees des les premieres minutes.|"
  "La recherche doit etre diversifiee : annonces, candidatures spontanees, réseau familial et enseignants.|"
  "Apres un refus, on demande un retour et on garde le contact pour une opportunite future."),
[QC("Que doit contenir une convention de stage ?", "Les seules dates~Les dates, les horaires et le tuteur~Le salaire uniquement~La liste des amis", 1,
     "La convention cadre les conditions materiales et le suivi pedagogique du stage."),
 QC("Quel est le role de la lettre de motivation ?", "Repeter le CV~Expliquer la motivation et l'apport du candidat~Donner l'adresse~Remplacer la convention", 1,
     "Elle etablit un lien entre le profil du candidat et les besoins de l'entreprise."),
 QC("Qu'est-ce qu'une candidature spontanee ?", "Une reponse a une annonce~Une candidature envoyee sans annonce prealable~Un entretien~Un rapport de stage", 1,
     "Elle consiste a proposer sa candidature a une entreprise choisie, meme sans offre publiee."),
 QC("Qui valide les objectifs du stage ?", "Le tuteur~Le facteur~Le voisin~Le fournisseur", 0,
     "Le tuteur accompagne l'eleve et valide les objectifs avec lui."),
 QC("Que fait-on juste apres un refus ?", "On abandonne~On demande un retour et garde le contact~On critique l'entreprise~On envoie un second CV identique", 1,
     "Un retour permet de s'ameliorer et le contact peut deboucher sur une autre opportunite."),
 QC("Quel element est observe des les premieres minutes d'un entretien ?", "La ponctualite et la tenue~Le prix du CV~La marque du stylo~La longueur de la lettre", 0,
     "Les premiers signaux non verbaux countent beaucoup dans la perception du candidat."),
 QC("Que decrit le rapport de stage ?", "L'entreprise, les missions et les apprentissages~Le salaire des collegues~Les seules photos~La météo", 0,
     "Le rapport formalise la decouverte et les acquis de la periode."),
 QT("Rediger les grandes lignes d'une lettre de motivation pour un stage de quatre semaines dans un service comptable, en trois paragraphes.",
    "Premier paragraphe : je suis eleve de premiere STMG et je souhaite effectuer un stage de quatre semaines dans votre service comptable afin de decouvrir le suivi des operations courantes. Deuxieme paragraphe : j'ai etudie le bilan, le compte de resultat et la comptabilite en partie double, et j'ai utilise un tableur pour etablir un suivi de depenses lors d'un projet de classe ; je peux egalement faire preuve de rigueur et de discretion. Troisieme paragraphe : je serais heureux de contribuer au classement des justificatifs et a la saisie des ecritures, et je vous propose un entretien pour presenter plus precisement ma motivation. La lettre evite les formules generiques et s'appuie sur des elements verifies du parcours et du projet professionnel.",
    "On attend trois paragraphes : objet du stage, competences liees a la formation et a des exemples, contribution proposee et demande d'entretien."),
 QT("Expliquer comment diversifier sa recherche de stage et pourquoi il ne faut pas attendre une seule reponse.",
    "On consulte d'abord les annonces publiees par les entreprises et les plateformes scolaires. On complete avec des candidatures spontanees aupres des entreprises du secteur vise, en adaptant le CV et la lettre a chaque destinataire. Le reseau personnel, la famille, les enseignants et les anciens eleves peuvent signaler des opportunites non publiees. On prepare egalement une version courte de son projet en quelques lignes pour saisir une opportunite lors d'un salon ou d'un entretien imprevu. Il faut postuler a plusieurs endroits parce que le taux de reponse est faible et que les calendriers de recrutement varient. Chaque refus est une information : on demande un retour, on corrige sa candidature et on maintaint le contact, car une entreprise qui refuse en janvier peut proposer un stage en juin.",
    "On attend plusieurs canaux de recherche, l'adaptation des candidatures et l'explication du nombre multiple de demandes.")],
C("Trouver un stage demande une recherche diversifiee, des candidatures adaptees et un suivi apres chaque reponse.",
  "CV + lettre motivee + convention + rapport",
  "Annonces · spontanee · reseau · suivi",
  "Stage~Decouverte d'un metier~CV~Facts et competences~Lettre~Motivation~Convention~Cadre du stage~Tuteur~Suivi pedagogique",
  "Inventarier les secteurs et les entreprises|Adapter CV et lettre a chaque entreprise|Preparer l'entretien|Signer la convention avant le debut|Rediger le rapport et garder le contact",
  "Envoyer le meme CV partout|Oublier la convention|Attendre une seule reponse|Ne pas se presenter a l'heure",
  "Stage comptable~Quatre semaines~Competence~Bilan et tableur~Motivation~Suivi des ecritures~Refus~Demande de retour~Rapport~Apprentissages",
  "Candidature spontanee~Sans annonce~Annonce~Offre publiee~Reseau~Contacts personnels~Entretien~Echange direct",
  "Ponctualite~Premier signal~Tenue~Adaptee~Ecoute active~Comprehension~Questions~Preparer a l'avance"))


# ============================================================ C20
add("C20", "Veille informationnelle et recherche documentaire", "Methodologie", ["1re"],
S("Une veille informationnelle est une recherche organisee et reguliere d'informations sur un sujet donne.|"
  "On definit d'abord le besoin avec precision : questions, mots cles, periode et zone geographique.|"
  "Les sources primaires publient l'information d'origine, tandis que les sources secondaires la commentent.|"
  "Un moteur de recherche explore le web ; un annuaire ou une base specialisee donne des resultats plus qualifies.|"
  "Les operateurs comme ET, OU, les guillemets et le signe moins affinent les resultats d'une recherche.|"
  "La fiabilite d'une source s'evalue avec l'auteur, la date, le support et les references citees.|"
  "Un site institutionnel ou une revue avec comite de lecture presente plus de garanties qu'un forum.|"
  "Il faut comparer au moins deux sources avant de retenir un chiffre ou une affirmation.|"
  "Les resultats utiles sont classes dans un tableau avec titre, source, date, adresse et resume.|"
  "Toute citation doit etre accompagnee de sa source afin d'eviter le plagiat.|"
  "Les alertes et les flux RSS permettent de recevoir automatiquement les nouvelles publications.|"
  "Une veille efficace produit une synthese courte qui repond au besoin initial et signale les incertitudes."),
[QC("Que faut-il faire avant de lancer une recherche ?", "Definir preciseement le besoin~Ouvrir tous les sites~Copier le premier resultat~Ecrire la synthese", 0,
     "Sans definition du besoin, les resultats sont disperses et difficilement utilisables."),
 QC("Qu'est-ce qu'une source primaire ?", "Un commentaire~L'information d'origine~Un resume~Un forum", 1,
     "La source primaire publie directement le fait, le document ou la donnee."),
 QC("A quoi servent les guillemets dans une recherche ?", "A exclure un mot~A rechercher une expression exacte~A changer de langue~A fermer la fenetre", 1,
     "Les guillemets imposent que les mots apparaissent ensemble et dans cet ordre."),
 QC("Quel critere n'evalue pas la fiabilite d'une source ?", "L'auteur~La date de publication~Les references citees~Le nombre de couleurs de la page", 3,
     "L'apparence graphique n'est pas un critere de fiabilite."),
 QC("Pourquoi comparer plusieurs sources ?", "Pour confirmer un chiffre et detecter les divergences~Pour remplir la page~Pour eviter de lire~Pour utiliser le meme texte", 0,
     "La confrontation des sources permet de verifier les informations et de repérer les biais."),
 QC("Que contient un tableau de veille bien tenu ?", "Titre, source, date, adresse et resume~Seulement le titre~Les couleurs des sites~Le nombre de mots", 0,
     "Ces champs permettent de retrouver et d'evaluer chaque document plus tard."),
 QC("Comment eviter le plagiat ?", "En changeant quelques mots~En citant la source de chaque emprunt~En ne citant personne~En ecrivant plus vite", 1,
     "Toute citation ou donnee empruntee doit etre attribuee a sa source."),
 QT("Decrire la demarche pour realiser une veille sur l'evolution du salaire minimum dans un pays donne.",
    "On definit le besoin : le salaire minimum dans un pays, sur les cinq dernieres annees, avec les montants annuels et les dates d'application. On choisit des mots cles precis et on utilise des operateurs, par exemple avec les guillemets pour figer l'expression et le signe moins pour exclure les resultats straniers. On interroge d'abord les sources primaires : le journal officiel, le site du ministere du travail et les textes de loi. On complete avec des sources secondaires fiables, comme des rapports d'organismes publics ou des articles de revue specialisee, en verifiant l'auteur et la date. On note chaque document dans un tableau avec le titre, la source, la date, l'adresse et un resume. On compare les chiffres entre deux sources avant de les retenir. On termine par une synthese courte qui presente l'evolution, la date de la derniere valeur et les incertitudes eventuelles.",
    "On attend definition du besoin, mots cles et operateurs, sources primaires et secondaires, tableau de collecte, comparaison et synthese."),
 QT("Expliquer la difference entre une veille ponctuelle et une veille continue, et donner les outils adaptes a chacune.",
    "Une veille ponctuelle repond a une question precise et unique, par exemple preparer un dossier pour une exposition orale : on effectue une recherche approfondie, on selectionne quelques sources et on produit une synthese. Une veille continue suit un sujet sur la duree, par exemple surveiller l'actualite d'un secteur professionnel ou d'une entreprise pendant un stage : on definit des mots cles permanents et on consulte regulierement les memes sources. Pour la veille ponctuelle, les outils utiles sont les moteurs de recherche, les bases de donnees specialisees et les annuaires. Pour la veille continue, on utilise les flux RSS, les alertes de moteurs de recherche, les newsletters et les favoris classes par theme. Dans les deux cas, il faut conserver les reference complete de chaque document et distinguer les faits verifies des simples opinions.",
    "On doit opposer reponse unique et suivi dans le temps, donner des outils pour chaque cas et rappeler la traçabilité des sources.")],
C("La veille informationnelle transforme une recherche dispersee en une connaissance organisee et verifiable.",
  "Besoin + sources + operateurs + evaluation + synthese",
  "Primaire / secondaire · fiabilite · citation",
  "Besoin~Question precise~Source primaire~Information d'origine~Operateur~Affinage de la recherche~Fiabilite~Auteur et date~Synthese~Resultat court",
  "Definir le besoin et les mots cles|Choisir des sources primaires et secondaires|Affiner avec les operateurs|Evaluer et comparer les sources|Classer les resultats et rediger la synthese",
  "Copier le premier resultat trouve|Croire qu'un forum est une source sure|Oublier de citer ses sources|Ne jamais verifier la date",
  "Salaire minimum~Cinq annees~Journal officiel~Source primaire~Rapport~Source secondaire~Guillemets~Expression exacte~Flux RSS~Veille continue",
  "Moteur~Recherche large~Base specialisee~Resultats qualifies~Source primaire~Directe~Source secondaire~Commentee",
  "ET~Les deux mots~OU~Au moins un mot~Guillemets~Expression exacte~Signe moins~Exclusion"))


# FIN DU LOT C
valider_et_ecrire(F, "stmg-mat-part-C.json")
