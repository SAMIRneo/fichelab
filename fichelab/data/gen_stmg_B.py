# -*- coding: utf-8 -*-
"""Generateur stmg-mat-part-B.json — lot B : sciences de gestion et economie (20 fiches).

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


# ============================================================ B01
add("B01", "Les fonctions de l'entreprise", "Management", ["1re"],
S("Une entreprise est une organisation qui mobilise des ressources humaines, financieres et materielles pour produire des biens ou des services.|"
  "La fonction production transforme les matieres premieres en produits ou realise la prestation de service.|"
  "La fonction commerciale recherche des clients, negocie les ventes et assure la distribution.|"
  "La fonction financiere gere la tresorerie, les investissements, les comptes et les relations avec les banques.|"
  "La fonction ressources humaines recrute, forme, paye et accompagne les salaries.|"
  "La fonction administrative et juridique gere les contrats, les obligations legales et les archives.|"
  "La fonction informatique fournit les outils numeriques, les donnees et la securite des systemes.|"
  "La direction generale definit la strategie, arbitre entre les fonctions et represente l'entreprise.|"
  "Les fonctions sont interdependantes : une decision commerciale engage la production et la tresorerie.|"
  "La chaine de valeur decrit la suite des activites qui creent de la valeur, de l'approvisionnement au service apres-vente.|"
  "Dans une petite entreprise, un meme salarie exerce plusieurs fonctions ; dans une grande, les services sont specialises.|"
  "La finalite de l'entreprise combine la rentabilite, la perennite et la prise en compte des parties prenantes."),
[QC("Quelle fonction transforme les matieres premieres ?", "La fonction commerciale~La fonction production~La fonction financiere~La direction", 1,
     "La production assure la transformation ou la realisation du service."),
 QC("Quelle fonction gere la tresorerie ?", "Ressources humaines~Financiere~Administrative~Production", 1,
     "La fonction financiere suit les flux d'argent et les comptes."),
 QC("Qui definit la strategie generale de l'entreprise ?", "Le service comptable~La direction generale~Le tresorier~Le responsable production", 1,
     "La direction arbitre et represente l'entreprise."),
 QC("Quelle fonction recrute et accompagne les salaries ?", "Commerciale~Ressources humaines~Financiere~Juridique", 1,
     "La fonction RH pilote le recrutement, la formation et la paie."),
 QC("Que decrit la chaine de valeur ?", "Les seuls benefices~Les activites qui creent de la valeur~Les actionnaires~Les impots", 1,
     "Elle va de l'approvisionnement jusqu'au service apres-vente."),
 QC("Dans une PME, les fonctions sont ...", "Toujours separees~Souvent exercees par les memes personnes~Inexistantes~Identiques a celles d'un grand groupe", 1,
     "La petite taille entraine une polyvalence des salaries."),
 QC("Quelle est une finalite de l'entreprise ?", "La seule rentabilite immediate~La rentabilite et la perennite~Le hasard~L'absence de concurrence", 1,
     "L'entreprise doit etre rentable et durable, tout en tenant compte des parties prenantes."),
 QT("Decrire les principales fonctions d'une entreprise de 50 salaries specialisee en restauration.",
    "Dans cette entreprise, la fonction production correspond a la preparation des plats et a la gestion des approvisionnements. La fonction commerciale attire les clients, gere les reservations, les promotions et la relation avec la clientele. La fonction financiere suit les recettes quotidiennes, paye les fournisseurs et controle la tresorerie. La fonction ressources humaines recrute les cuisiniers et les serveurs, organise les plannings et la formation. La fonction administrative gere les contrats, les licenses et les obligations d'hygiene. Le dirigeant arbitre entre ces besoins, par exemple entre l'embauche d'un cuisinier supplementaire et l'achat d'un nouvel equipement.",
    "On attend production, commerce, finance, RH, administration et role de la direction, avec des exemples concrets."),
 QT("Expliquer pourquoi les fonctions d'une entreprise sont interdependantes.",
    "Chaque fonction consomme les resultats d'une autre et produit pour les suivantes. Une campagne commerciale reussie augmente les commandes, ce qui oblige la production a augmenter son rythme et la fonction financiere a financer les achats de matieres premieres. Si la fonction RH ne recrute pas assez vite, la production ne peut pas repondre a la demande et la qualite du service se degrade. Inversement, une panne informatique bloque la prise de commande et la facturation. La direction doit donc arbitrer globalement plutot que d'optimiser un seul service : c'est cette coordination qui cree de la valeur pour le client.",
    "On doit montrer des liens de cause a effet entre au moins trois fonctions et le role d'arbitrage de la direction.")],
C("L'entreprise est un systeme de fonctions specialisees qui doivent etre coordonnees par la direction.",
  "Production + commerce + finance + RH + administration = valeur creee",
  "Chaine de valeur : approvisionnement → production → distribution → service apres-vente",
  "Production~Transformation~Commercial~Vente et clients~Finance~Tresorerie et comptes~Ressources humaines~Recrutement et paie~Direction~Strategie et arbitrage",
  "Identifier la finalite de l'entreprise|Recenser les fonctions exercees|Preciser les ressources mobilisees|Analyser les liens entre fonctions|Arbitrer les priorites de la direction",
  "Reducer l'entreprise a la seule production|Ignorer la fonction financiere|Croire que les fonctions ne se parlent pas|Oublier les parties prenantes",
  "Restauration~Preparation des plats~Reservations~Activite commerciale~Tresorerie~Recettes quotidiennes~Plannings~Role des RH~Arbitrage~Embauche ou equipement",
  "PME~Polyvalence des salaries~Grande entreprise~Services specialises~Fonction~Ensemble de taches coherentes~Service~Unite organisationnelle",
  "Chaine de valeur~Creation de valeur successive~Interdependance~Liens entre services~Parties prenantes~Salaries, clients, fournisseurs~Perenite~Durabilite"))


# ============================================================ B02
add("B02", "Organisation, organigramme et repartition des responsabilites", "Management", ["1re"],
S("L'organisation repartit les taches, les responsabilites et les relations entre les membres de l'entreprise.|"
  "La division du travail specialise les salaries sur des taches reduites et repetees.|"
  "L'organigramme represente graphiquement les services, les niveaux hierarchiques et les liens formels.|"
  "La ligne hierarchique va du dirigeant aux employes : chaque salarie rend compte a un responsable.|"
  "L'ecart de management designe le nombre de subordonnes directs d'un responsable.|"
  "Une organisation centralisee concentre les decisions au sommet ; une organisation decentralisee les rapproche du terrain.|"
  "L'organisation fonctionnelle regroupe les salaries par specialite : production, finance, marketing.|"
  "L'organisation par produit ou par clientele adapte les equipes a un marche precis.|"
  "L'organisation matricielle croise un responsable hierarchique et un responsable de projet.|"
  "Une relation fonctionnelle conseille sans donner d'ordre, contrairement a une relation hierarchique.|"
  "La clarification des responsabilites evite les conflits de competence et les taches non realisees.|"
  "Les canaux de communication interne completent l'organigramme en rendant possible la circulation de l'information."),
[QC("Que represente un organigramme ?", "Les comptes de l'entreprise~Les services et les liens hierarchiques~Les clients~Les fournisseurs", 1,
     "C'est une representation graphique de la structure organisationnelle."),
 QC("Qu'appelle-t-on ecart de management ?", "Le nombre de subordonnes directs~La duree d'une reunion~Le salaire d'un dirigeant~Le nombre de clients", 0,
     "Il mesure l'ampleur de l'equipe placee sous l'autorite d'un responsable."),
 QC("Dans une organisation centralisee, les decisions sont ...", "Prises par le terrain~Concentrees au sommet~Supprimees~Prises par les clients", 1,
     "La centralisation concentre le pouvoir de decision a la direction."),
 QC("Une organisation matricielle se caracterise par ...", "Un seul responsable par salarie~Deux axes de responsabilite~L'absence de projet~Une structure sans services", 1,
     "Le salarie depend d'un responsable hierarchique et d'un responsable de projet."),
 QC("Une relation fonctionnelle ...", "Donne des ordres~Conseille sans donner d'ordre~Remplace la hierarchie~Est interdite", 1,
     "Le specialiste fonctionnel apporte son expertise sans exercer l'autorite hierarchique."),
 QC("Que permet la division du travail ?", "Une specialisation des taches~Une suppression des responsabilites~Une hausse immediate des prix~Une egalite parfaite des salaires", 0,
     "Chaque salarie se concentre sur une tache et gagne en efficacite."),
 QC("Pourquoi clarifier les responsabilites ?", "Pour eviter les doublons et les oublis~Pour augmenter les impots~Pour supprimer les reunion~Pour cacher les erreurs", 0,
     "Une responsabilite precise limite les conflits de competence."),
 QT("Lire un organigramme simple et identifier les niveaux de decision.",
    "Un organigramme se lit de haut en bas : le dirigeant occupe le sommet, les responsables de services sont au niveau intermediaire et les employes occupent la base. Les traits verticaux indiquent l'autorite hierarchique, tandis que les traits horizontaux ou pointilles representent des relations fonctionnelles de conseil. Le nombre de personnes rattachees a un responsable donne son ecart de management. Un ecart trop large rend le controle difficile, un ecart trop etroit alourdit la structure. Enfin, la presence d'un responsable de projet a cote d'un responsable de service signale une organisation matricielle, ou deux logiques de decision coexistent.",
    "On attend la lecture du sommet vers la base, la distinction des liens hierarchiques et fonctionnels, et l'ecart de management."),
 QT("Comparer organisation fonctionnelle et organisation par produit.",
    "L'organisation fonctionnelle regroupe les competences : tous les comptables sont dans le service finance, tous les commerciaux dans le service commercial. Elle favorise la specialisation et la mutualisation des moyens, mais elle peut rendre lente la reponse a un client car plusieurs services doivent intervenir. L'organisation par produit ou par clientele constitue des equipes dediees a une gamme ou a un segment : chacune réunit ses propres ressources commerciales, financieres et techniques. Elle est plus reactive et plus proche du marche, mais elle duplique les moyens et peut creer des rivalites internes. Le choix depend de la diversite des produits et de la taille de l'entreprise.",
    "On doit opposer specialisation des competences et proximite client, avec avantages et limites pour chacune.")],
C("L'organisation repartit autorite et responsabilites : l'organigramme en donne la photographie formelle.",
  "Hierarchie + division du travail + coordination",
  "Fonctionnelle · par produit · matricielle · centralisee ou decentralisee",
  "Organigramme~Representation formelle~Ligne hierarchique~Autorite~Ecart de management~Subordonnes directs~Centralisation~Decision au sommet~Matrice~Double rattachement",
  "Identifier les services et les niveaux|Lire les liens hierarchiques|Repérer les relations fonctionnelles|Mesurer les ecarts de management|Evaluer la coherence de la structure",
  "Confondre autorite et conseil|Ignorer les relations informelles|Laisser deux responsables donner le meme ordre|Oublier d'actualiser l'organigramme",
  "Dirigeant~Sommet de l'organigramme~Responsable~Niveau intermediaire~Employe~Base~Ecart~Cinq subordonnes~Matrice~Projet et service",
  "Organisation fonctionnelle~Specialites regroupees~Organisation par produit~Equipes dediees~Centralisee~Decisions au sommet~Decentralisee~Decisions au terrain",
  "Relation hierarchique~Droit de donner des ordres~Relation fonctionnelle~Expertise et conseil~Responsabilite~Obligation de rendre compte~Communication~Circulation d'information"))


# ============================================================ B03
add("B03", "Leadership, motivation et travail d'equipe", "Management", ["1re", "Terminale"],
S("Le management conduit une equipe vers des objectifs ; le leadership designe la capacite a entrainer les autres.|"
  "L'autorite formelle vient de la position dans l'organigramme, pas necessairement de la competence personnelle.|"
  "On distingue plusieurs styles : autoritaire, participatif, laissez-faire et situationnel.|"
  "Le style autoritaire décide rapidement mais peut reduire l'engagement de l'equipe.|"
  "Le style participatif associe les salaries aux decisions et favorise l'adhésion.|"
  "Le style laissez-faire laisse une grande autonomie et convient a des equipes experimentees.|"
  "La motivation intrinseque vient de l'interet de la tache, de l'autonomie et de la reconnaissance.|"
  "La motivation extrinseque vient de recompenses externes comme le salaire ou le bonus.|"
  "La pyramide de Maslow classe les besoins de la survie a l'accomplissement de soi.|"
  "Herzberg distingue les facteurs d'hygiene, qui evitent l'insatisfaction, et les motivateurs, qui creent l'engagement.|"
  "La delegation confie une tache avec les moyens et la responsabilite de la realiser.|"
  "La gestion des conflits passe par l'ecoute, la clarification des faits et la recherche d'une solution commune."),
[QC("Quelle est la difference entre autorite formelle et leadership ?", "L'autorite vient de la position, le leadership de l'adhésion~Il n'y a aucune difference~Le leadership vient de la position~L'autorite est toujours illegale", 0,
     "L'autorite est institutionnelle ; le leadership repose sur l'influence et l'adhésion."),
 QC("Quel style de management associe les salaries aux decisions ?", "Autoritaire~Participatif~Laissez-faire~Technocratique", 1,
     "Le style participatif implique l'equipe dans la decision."),
 QC("Quel besoin se situe au sommet de la pyramide de Maslow ?", "Se nourrir~Se loger~S'accomplir~Etre paye", 2,
     "L'accomplissement de soi est le besoin le plus eleve dans ce modele."),
 QC("Qu'appelle-t-on motivation intrinseque ?", "Le bonus~L'interet de la tache~Le salaire~La sanction", 1,
     "Elle vient de la tache elle-meme, de l'autonomie et de la reconnaissance."),
 QC("Quel est un facteur d'hygiene selon Herzberg ?", "La reconnaissance~Le salaire et les conditions de travail~La responsabilite~L'apprentissage", 1,
     "Les facteurs d'hygiene evitent l'insatisfaction sans creer un engagement durable."),
 QC("Que suppose une delegation reussie ?", "Donner la tache sans moyens~Confier tache, moyens et responsabilite~Tout controler soi-meme~Supprimer les objectifs", 1,
     "La delegation doit etre accompagnee de ressources et d'une responsabilite claire."),
 QC("Quelle est une etape de la gestion d'un conflit ?", "Ignorer le probleme~Ecouter et clarifier les faits~Choisir un coupable~Raccourcir la reunion", 1,
     "On ecoute les points de vue puis on s'appuie sur les faits pour chercher une solution."),
 QT("Distinguer motivation intrinseque et motivation extrinseque dans un service commercial.",
    "Un commercial motive par des facteurs extrinseques travaille surtout pour le salaire, les commissions et les classements : il augmentera son effort si la prime augmente. Un commercial motive par des facteurs intrinseques trouve de l'interet dans la negociation, la relation avec le client et l'autonomie dans l'organisation de sa journee. En pratique, les deux motivations coexistent : une prime peut declencher l'effort, mais la reconnaissance du manager et la qualite du travail entretiennent l'engagement. Le manager doit donc eviter de tout ramener a l'argent et menager des possibilites d'apprentissage et de responsabilite.",
    "On attend la definition des deux motivations et des exemples lies au metier commercial."),
 QT("Comment un manager peut-il animer une equipe en difficulté apres un echec de projet ?",
    "Il commence par reconnaitre l'échec sans chercher un bouc emissaire, puis il organise un temps d'echange ou chaque membre expose les faits et les difficultes rencontrees. Il distingue les causes techniques, les problemes de coordination et les erreurs de planning. Il associe ensuite l'equipe a la definition d'actions correctives, ce qui restaure la motivation intrinseque par l'autonomie et la reconnaissance. Il fixe des objectifs realistes a court terme pour recreer la confiance et il communique les progres. Enfin, il tire les lecons de l'echec et les formalise pour eviter qu'elles se repetent.",
    "On attend ecoute, analyse des causes, participation, objectifs realistes et capitalisation d'experience.")],
C("Le manager obtient l'engagement en adaptant son style, en comprenant les motivations et en deleguant clairement.",
  "Leadership = influence + adhésion + objectifs partages",
  "Intrinseque · extrinseque · Maslow · Herzberg · delegation",
  "Leadership~Influence et adhésion~Autorite~Position formelle~Participatif~Decision partagee~Motivation~Moteur de l'action~Delegation~Tache et responsabilite",
  "Identifier le style de management observe|Diagnostiquer les motivations de l'equipe|Repérer les besoins non satisfaits|Clarifier les delegations|Accompagner et reconnaitre",
  "Confondre autorite et leadership|Croire que la prime suffit a motiver|Deleger sans donner les moyens|Eviter le conflit au lieu de le traiter",
  "Commercial~Prime et salaire~Motivation extrinseque~Commission~Motivation intrinseque~Interet de la negociation~Echec~Analyse des causes~Reconnaissance~Engagement",
  "Style autoritaire~Decision rapide~Style participatif~Adhesion plus forte~Laissez-faire~Autonomie~Style situationnel~Adapte au contexte",
  "Facteurs d'hygiene~Salaire et conditions~Motivateurs~Reconnaissance et responsabilite~Besoin~Mobilise l'energie~Satisfaction~Resultat de l'action"))


# ============================================================ B04
add("B04", "Gestion de projet et conduite du changement", "Management", ["Terminale"],
S("Un projet est une entreprise temporaire avec un objectif precis, des ressources limitees et une date de fin.|"
  "Le cycle de projet comporte l'initiation, la planification, la realisation, le suivi et la cloture.|"
  "La definition du projet precise le besoin, les objectifs, les livrables et les criteres de reussite.|"
  "Les parties prenantes sont les personnes ou organismes qui influencent ou subissent le projet.|"
  "Le planning decompose le travail en taches avec des responsables, des durees et des jalons.|"
  "Le diagramme de Gantt represente les taches dans le temps et leurs chevauchements.|"
  "Les indicateurs de suivi mesurent l'avancement, le respect du budget et la qualite des livrables.|"
  "La gestion des risques identifie les menaces, estime leur probabilite et prepare des actions correctives.|"
  "La methode agile organise le travail en cycles courts avec des points de synchronisation reguliers.|"
  "La conduite du changement accompagne les salaries confronted a une nouvelle organisation ou un nouvel outil.|"
  "La resistance au changement s'explique par la peur de perdre des habitudes, des competences ou du pouvoir.|"
  "La communication et la formation sont essentielles pour obtenir l'adhésion au projet."),
[QC("Quelle est une caracteristique d'un projet ?", "Permanent~Temporaire avec une date de fin~Sans objectif~Sans ressources", 1,
     "Le projet a un debut et une fin, contrairement a l'activite courante."),
 QC("Quelle phase suit l'initiation d'un projet ?", "La cloture~La planification~La mise en oeuvre d'un outil~Le bilan social", 1,
     "On planifie avant de realiser."),
 QC("Qu'appelle-t-on partie prenante ?", "Un client uniquement~Toute personne qui influe ou subit le projet~Un actionnaire uniquement~Un fournisseur uniquement", 1,
     "Les parties prenantes incluent clients, salaries, direction, partenaires et autorites."),
 QC("Que represente un diagramme de Gantt ?", "Les comptes~Les taches dans le temps~Les salaries par age~Les prix de vente", 1,
     "Il visualise le debut, la fin et le chevauchement des taches."),
 QC("Quel est un indicateur de suivi de projet ?", "Le taux d'avancement~La couleur du logo~Le nombre de pages~L'heure de debut de la journee", 0,
     "On suit l'avancement, le budget, les delais et la qualite."),
 QC("Pourquoi une equipe resiste-t-elle au changement ?", "Par exces de formation~Par peur de perdre ses habitudes~Par manque de risques~Par absence de projet", 1,
     "Les changements d'habitudes, de competences ou de pouvoir generent des resistances."),
 QC("Comment obtenir l'adhésion au changement ?", "En imposant sans expliquer~En communiquant et en formant~En supprimant les reunions~En changeant le Planning secretement", 1,
     "La transparence, la formation et l'accompagnement creent l'adhésion."),
 QT("Construire le planning simplifie d'un projet de mise en place d'un nouvel outil de gestion.",
    "On commence par decomposer le projet en phases : expression du besoin, choix de l'outil, parametrage, formation des utilisateurs, test puis deployment. Pour chaque tache, on designe un responsable et une duree estimee. On place les jalons : validation du besoin, fin du parametrage, fin de la formation, mise en service. Le diagramme de Gantt permet de visualiser les chevauchements, par exemple la formation peut commencer avant la fin du parametrage si les supports sont prets. On identifie ensuite les risques, comme un retard de livraison du fournisseur, et on prepare une solution de repli. Un point hebdomadaire permet de comparer l'avancement réel au planning previsionnel.",
    "On attend phases, responsables, jalons, représentation temporelle, risques et suivi régulier."),
 QT("Expliquer pourquoi un projet peut echouer malgre un bon planning technique.",
    "Un planning correct ne garantit pas l'adhésion des personnes. Si les utilisateurs ne comprennent pas pourquoi l'outil change, ils continuent a utiliser leurs anciennes methodes et les donnees restent dispersees. La resistance peut venir de la peur de perdre une expertise ou de voir son role modifie. Le chef de projet doit donc associer les parties prenantes des le debut, communiquer sur les objectifs, former les salaries et designer des ambassadeurs dans les equipes. Il doit aussi mesurer l'usage réel de l'outil apres le deploiement et corriger les irritants. La conduite du changement est donc aussi important que le respect du calendrier.",
    "On doit relier l'echec aux facteurs humains et proposer communication, formation et suivi de l'usage.")],
C("Un projet est un effort temporaire et coordonne ; sa reussite depend autant du planning que de l'adhésion.",
  "Objectif + parties prenantes + planning + risques + changement",
  "Initier · planifier · realiser · suivre · cloturer",
  "Projet~Action temporaire~Parties prenantes~Influencent ou subissent~Livrable~Resultat attendu~Jalon~Date cle~Diagramme de Gantt~Taches dans le temps",
  "Definir le besoin et les objectifs|Identifier les parties prenantes|Decomposer les taches et fixer les jalons|Anticiper les risques|Accompagner le changement et tirer le bilan",
  "Confondre projet et activite courante|Oublier les utilisateurs dans le projet|Ne pas prevoir de formation|Clore sans capitaliser les lecons",
  "Nouvel outil~Projet de gestion~Jalon~Validation du besoin~Gantt~Chevauchement des taches~Risque~Retard fournisseur~Adhesion~Formation",
  "Methode classique~Phases successives~Methode agile~Cycles courts et retours frequents~Gestion de projet~Coordination~Conduite du changement~Accompagnement humain",
  "Resistance~Peur du changement~Communication~Information transparente~Formation~Acquisition de competences~Ambassadeur~Relais interne"))


# ============================================================ B05
add("B05", "Fonction commerciale et marketing", "Management", ["Terminale"],
S("La fonction commerciale a pour objectif de vendre et de developper la relation avec les clients.|"
  "Le marketing identifie les besoins du marche et propose une offre adaptee.|"
  "Le marketing mix classique repose sur quatre leviers : produit, prix, distribution et communication.|"
  "L'etude de marché recueille des informations sur les clients, la concurrence et les tendances.|"
  "La segmentation decoupe le marche en groupes homogènes de consommateurs.|"
  "Le ciblage choisit les segments prioritaires et le positionnement definit la place de l'offre dans l'esprit du client.|"
  "Le cycle de vie d'un produit comprend le lancement, la croissance, la maturite et le declin.|"
  "Le prix peut etre fixe selon les couts, la concurrence ou la valeur perçue par le client.|"
  "La distribution choisit les canaux : magasin, site internet, revendeurs ou vente directe.|"
  "La communication commerciale comprend la publicite, la promotion, les relations publiques et le personal selling.|"
  "La force de vente negocie les contrats et suit les clients dans la duree.|"
  "Les principaux indicateurs sont le chiffre d'affaires, la part de marche, le taux de transformation et la satisfaction client."),
[QC("Quels sont les quatre leviers du marketing mix ?", "Produit, prix, distribution, communication~Prix, salaire, impot, banque~Client, fournisseur, banque, Etat~Production, comptes, RH, loi", 0,
     "Les 4P sont product, price, place, promotion."),
 QC("Que permet la segmentation ?", "Augmenter les impots~Regrouper des clients aux besoins proches~Supprimer la concurrence~Fixer les salaires", 1,
     "Elle decoupe le marche en segments homogènes."),
 QC("Que designe le positionnement ?", "Le prix le plus bas~La place de l'offre dans l'esprit du client~L'adresse de l'entreprise~Le nombre de salaries", 1,
     "Il s'agit de la perception de l'offre par rapport a la concurrence."),
 QC("Quelle est une phase du cycle de vie d'un produit ?", "La maturite~La comptabilite~La hierarchie~La paie", 0,
     "Lancement, croissance, maturite et declin composent le cycle de vie."),
 QC("Comment fixer un prix selon la valeur perçue ?", "En ajoutant un pourcentage au cout~En tenant compte de ce que le client est pret a payer~En copiant le salaire~En tirant au sort", 1,
     "L'approche client s'appuie sur l'utilite et la valeur ressentie."),
 QC("Quel canal de distribution est a la fois direct et numerique ?", "Le revendeur~Le site internet de l'entreprise~Le grossiste~Le magazine", 1,
     "La vente en ligne directe supprime l'intermediaire."),
 QC("Quel indicateur mesure la proportion de visiteurs qui achètent ?", "Le chiffre d'affaires~Le taux de transformation~La part de marche~Le cout de production", 1,
     "Le taux de transformation rapporte les ventes aux contacts ou visites."),
 QT("Expliquer la demarche d'une etude de marche avant le lancement d'un produit.",
    "On definit d'abord l'objet de l'etude et les données necessaires : besoins des clients, concurrents, prix pratiques et taille du marche. On collecte ensuite des donnees secondaires, par exemple des rapports sectoriels, puis des donnees primaires par questionnaire, entretien ou observation. On analyse les resultats pour identifier les segments et les besoins non couverts. On en deduit une recommandation : le produit a lancer, le prix envisageable, les canaux de distribution et les arguments de communication. L'etude ne donne pas une certitude, mais elle reduit le risque commercial et aide a formuler le positionnement.",
    "On attend objectif, collecte secondaire et primaire, analyse, segmentation et recommandation."),
 QT("Comment adapter le marketing mix a un produit arrivant a maturite ?",
    "A la maturite, la croissance des ventes ralentit et la concurrence est forte. Sur le produit, on peut proposer des variantes, une nouvelle formulation ou une meilleure qualite perçue. Sur le prix, on peut jouer sur des offres groupees ou des remises sans detruire la valeur de la marque. Sur la distribution, on cherche a couvrir davantage de points de vente ou a developper la vente en ligne. Sur la communication, on insiste sur la fidelisation, le service apres-vente et la difference par rapport aux concurrents. On suit la part de marche et la satisfaction pour verifier que l'offre reste pertinente, tout en preparant le renouvellement du produit avant le declin.",
    "On doit traiter les quatre leviers et relier les actions a la situation de maturite.")],
C("La fonction commerciale adapte l'offre au marche en combinant produit, prix, distribution et communication.",
  "Marketing mix = 4P : product, price, place, promotion",
  "Segmentation → ciblage → positionnement",
  "Etude de marche~Besoins et concurrence~Segmentation~Groupes homogènes~Positionnement~Place dans l'esprit~Marketing mix~Quatre leviers~Part de marche~Indicateur",
  "Realiser l'etude de marche|Segmenter et choisir une cible|Definir le positionnement|Combiner les quatre leviers|Suivre les indicateurs commerciaux",
  "Confondre segmentation et ciblage|Proposer un prix sans etude|Negliger le service apres-vente|Mesurer seulement le chiffre d'affaires",
  "Lancement~Debut du cycle~Maturite~Concurrence forte~Prix~Valeur perçue~Site internet~Vente directe~Taux de transformation~Visites puis ventes",
  "Segmentation~Decouper le marche~Ciblage~Choisir les segments~Positionnement~Se distinguer~Differentiation~Argument de vente",
  "Produit~Ce qui est vendu~Prix~Ce qui est paye~Distribution~Comment l'offre parvient au client~Communication~Comment l'offre est connue"))


# ============================================================ B06
add("B06", "Le bilan : actif, passif et equilibre", "Comptabilité", ["1re"],
S("Le bilan est un document comptable qui decrit le patrimoine de l'entreprise a une date precise.|"
  "Il se presente en deux parties : l'actif et le passif.|"
  "L'actif correspond aux emplois : ce que l'entreprise possede et ou elle a investi.|"
  "Les immobilisations, comme les machines ou les batiments, sont des emplois durables.|"
  "Les stocks, les creances clients et la tresorerie sont des emplois courants.|"
  "Le passif correspond aux ressources : l'origine des fonds qui financent ces emplois.|"
  "Les capitaux propres comprennent le capital social et les resultats cumules.|"
  "Les dettes, par exemple les fournisseurs ou les emprunts, sont des ressources externes.|"
  "Le principe d'equilibre impose que l'actif total soit egal au passif total.|"
  "A l'actif, les elements sont classes du moins liquide au plus liquide.|"
  "Le fonds de roulement se calcule par ressources stables moins emplois stables.|"
  "La tresorerie nette s'obtient par fonds de roulement moins besoin en fonds de roulement."),
[QC("Que represente l'actif du bilan ?", "Les ressources~Les emplois du patrimoine~Les seules dettes~Le resultat de l'exercice", 1,
     "L'actif decrit les biens possedes et les investissements realises."),
 QC("Que represente le passif ?", "Les emplois~L'origine des ressources~Les stocks~Les machines", 1,
     "Le passif indique comment les emplois sont finances."),
 QC("Quel principe fondamental regit le bilan ?", "Actif = passif~Actif superieur au passif~Passif nul~Resultat nul", 0,
     "Le bilan doit toujours etre equilibre : total actif egal total passif."),
 QC("Une machine est un element ...", "De la tresorerie~Des immobilisations~Des creances~Des dettes", 1,
     "Une machine est un emploi durable, donc une immobilisation."),
 QC("Les capitaux propres se trouvent ...", "A l'actif~Au passif~Hors du bilan~Dans le compte de resultat uniquement", 1,
     "Ils figurent au passif, parmi les ressources internes."),
 QC("Comment calculer le fonds de roulement ?", "Ressources stables moins emplois stables~Actif moins passif~Ventes moins achats~Creances moins dettes", 0,
     "Le fonds de roulement mesure la marge de financement a long terme."),
 QC("Que sont les creances clients ?", "Des dettes envers les fournisseurs~Des sommes dues par les clients~Des immobilisations~Des capitaux propres", 1,
     "Une creance est un droit a recevoir de l'argent."),
 QT("Commenter la structure d'un bilan ou l'actif total atteint 500 000 euros et les capitaux propres 180 000 euros.",
    "Le bilan s'equilibre : le passif total vaut egalement 500 000 euros. Les capitaux propres representent 180 000 euros, soit 36 pour cent du total : l'entreprise est financee pour une part par ses actionnaires et pour le reste, 320 000 euros, par des dettes. On peut ensuite examiner la nature des dettes, en distinguant les emprunts a long terme des dettes courantes envers les fournisseurs. A l'actif, il faut verifier la part des immobilisations par rapport aux actifs courants : une proportion elevee d'immobilisations indique une activite industrielle. Enfin, le rapprochement avec le compte de resultat permet de voir si l'entreprise est rentable.",
    "On attend l'equilibre 500 000, le calcul de 36 pour cent, la distinction des dettes et l'analyse de la structure."),
 QT("Expliquer la difference entre fonds de roulement, besoin en fonds de roulement et tresorerie nette.",
    "Le fonds de roulement compare les ressources stables, comme les capitaux propres et les emprunts a long terme, aux emplois stables, comme les immobilisations. Il indique si l'entreprise a les moyens de financer son activite courante sur la duree. Le besoin en fonds de roulement correspond a l'argent immobilise dans l'exploitation : stocks, creances clients, diminues des dettes fournisseurs. La tresorerie nette est la difference entre les deux : fonds de roulement moins besoin en fonds de roulement. Une tresorerie nette positive signifie que l'entreprise dispose de liquidites ; negative, elle doit trouver des financements a court terme.",
    "On attend les trois definitions et la relation tresorerie nette = fonds de roulement moins besoin en fonds de roulement.")],
C("Le bilan photographie le patrimoine : l'actif montre les emplois, le passif les ressources, et les deux s'equilibrent.",
  "Actif total = passif total",
  "Fonds de roulement = ressources stables - emplois stables",
  "Actif~Emplois du patrimoine~Passif~Ressources de financement~Immobilisations~Emplois durables~Capitaux propres~Ressources internes~Equilibre~Actif egal passif",
  "Lire la date du bilan|Separer emplois et ressources|Classer les postes du haut vers le bas du bilan|Verifier l'equilibre|Calculer les indicateurs de structure",
  "Confondre actif et passif|Oublier que le bilan est une photographie a une date|Classer une creance parmi les dettes|Ne pas verifier l'equilibre",
  "Bilan~500 000 euros~Capitaux propres~180 000 euros~Part~36 pour cent~Dettes~320 000 euros~Tresorerie~FR moins BFR",
  "Emplois~Ce que l'entreprise possede~Ressources~Comment elle finance~Haut de bilan~Immobilisations~Bas de bilan~Stocks et creances",
  "Fonds de roulement~Ressources long terme~Besoin en fonds de roulement~Argent immobilise~Tresorerie nette~Liquidite disponible~Dette~Ressource externe"))


# ============================================================ B07
add("B07", "Le compte de resultat et le calcul du resultat", "Comptabilité", ["1re"],
S("Le compte de resultat resume les produits et les charges d'une periode, generalement un exercice annuel.|"
  "Contrairement au bilan, il decrit un flux et non un patrimoine a une date donnee.|"
  "Un produit est une ressource acquise lors de l'activite, comme une vente.|"
  "Une charge est une consommation de ressources, comme un achat ou un salaire.|"
  "Le chiffre d'affaires correspond aux ventes de biens ou de services de l'activite principale.|"
  "Le resultat d'exploitation s'obtient en soustrayant les charges d'exploitation des produits d'exploitation.|"
  "Le resultat financier regroupe les produits et charges financiers, par exemple les interets d'emprunt.|"
  "Le resultat exceptionnel concerne les operations inhabituelles, comme la vente d'un equipement.|"
  "On retranche ensuite l'impot sur les societes pour obtenir le resultat net.|"
  "Un resultat positif est un benefice ; un resultat negatif est une perte.|"
  "Le compte de resultat se presente sous forme de tableau avec produits d'un cote et charges de l'autre.|"
  "Sa lecture permet de calculer des taux de marge et d'apprecier la rentabilite de l'entreprise."),
[QC("Quel document decrit un flux sur un exercice ?", "Le bilan~Le compte de resultat~L'organigramme~Le plan comptable", 1,
     "Le compte de resultat enregistre les produits et charges de la periode."),
 QC("Le chiffre d'affaires correspond ...", "Aux salaries~Aux ventes de l'activite principale~Aux emprunts~Aux impots", 1,
     "Il mesure les ventes de biens ou de services."),
 QC("Quel est un exemple de charge ?", "Une vente~Un achat de matieres premieres~Un encaissement client~Une subvention", 1,
     "Un achat consomme des ressources : c'est une charge."),
 QC("Comment obtenir le resultat d'exploitation ?", "Produits financiers moins charges financieres~Produits d'exploitation moins charges d'exploitation~Chiffre d'affaires plus impot~Capitaux propres moins dettes", 1,
     "On soustrait les charges d'exploitation des produits d'exploitation."),
 QC("Les interets d'un emprunt sont ...", "Une charge d'exploitation~Une charge financiere~Un produit exceptionnel~Un impot", 1,
     "Ils sont classes dans le resultat financier."),
 QC("Que signifie un resultat net negatif ?", "Un benefice~Une perte~Une tresorerie positive~Un chiffre d'affaires nul", 1,
     "Un resultat negatif correspond a une perte de l'exercice."),
 QC("Quel impot est retranche pour obtenir le resultat net ?", "La TVA~L'impot sur les societes~La taxe fonciere~Les charges sociales", 1,
     "L'impot sur les societes s'applique au benefice."),
 QT("D'un compte de resultat : chiffre d'affaires 400 000, charges d'exploitation 330 000, charges financieres 10 000, impot 15 000. Calculer les resultats.",
    "Le resultat d'exploitation vaut 400 000 - 330 000 = 70 000 euros. Le resultat financier est egal a 0 - 10 000 = -10 000 euros si l'on suppose qu'il n'y a pas de produits financiers. Le resultat avant impot est donc 70 000 - 10 000 = 60 000 euros, en faisant abstraction d'un eventuel resultat exceptionnel. Apres l'impot sur les societes de 15 000 euros, le resultat net est 45 000 euros. Le taux de marge nette rapporte ce resultat au chiffre d'affaires : 45 000 / 400 000 = 11,25 pour cent. L'entreprise est beneficiaire.",
    "On attend 70 000, moins 10 000, resultat avant impot 60 000, resultat net 45 000 et marge nette 11,25 pour cent."),
 QT("Expliquer pourquoi une entreprise peut avoir un benefice comptable et des difficultes de tresorerie.",
    "Le resultat est calcule selon les principes comptables, notamment la separation de l'exercice et l'enregistrement des creances et des dettes. Une vente peut etre comptabilisee comme produit alors que le client n'a pas encore paye : le benefice existe mais l'argent n'est pas entre. A l'inverse, des investissements ou le remboursement d'emprunts consomment de la tresorerie sans etre immediatement des charges de l'exercice. C'est pourquoi on complete le compte de resultat par le bilan et par un plan de tresorerie. Le fonds de roulement et le besoin en fonds de roulement expliquent alors l'ecart entre rentabilite et liquidite.",
    "On doit opposer logique comptable et logique de cash, avec exemple de creance client et d'investissement.")],
C("Le compte de resultat mesure la performance de l'exercice en comparant produits et charges.",
  "Resultat net = produits - charges - impot",
  "Exploitation · financier · exceptionnel · impot",
  "Compte de resultat~Flux de l'exercice~Produit~Ressource acquise~Charge~Ressource consommee~Chiffre d'affaires~Ventes~Resultat net~Benefice ou perte",
  "Delimiter la periode|Classer produits et charges|Calculer le resultat d'exploitation| Ajouter les resultats financiers et exceptionnels|Deduire l'impot et analyser la marge",
  "Confondre bilan et compte de resultat|Oublier les charges financieres|Appeler benefice un resultat avant impot|Ignorer les produits exceptionnels",
  "CA 400 000~Charges 330 000~Resultat d'exploitation~70 000~Financier~-10 000~Resultat net~45 000~Marge nette~11,25 pour cent",
  "Produit~Entree de ressource~Charge~Sortie de ressource~Benefice~Resultat positif~Perte~Resultat negatif~Taux de marge~Resultat sur chiffre d'affaires",
  "Resultat d'exploitation~Activite principale~Resultat financier~Emprunts et placements~Resultat exceptionnel~Operations inhabituelles~Impot sur les societes~Prelevement sur benefice"))


# ============================================================ B08
add("B08", "La comptabilite en partie double", "Comptabilité", ["1re"],
S("La comptabilite en partie double enregistre chaque operation dans au moins deux comptes.|"
  "Un compte releve les augmentations et les diminutions d'un element du patrimoine.|"
  "Chaque operation produit une ecriture avec un montant egal au debit et au credit.|"
  "Le debit augmente les actifs et les charges, tandis que le credit augmente les capitaux propres, les dettes et les produits.|"
  "Le journal enregistre les operations chronologiquement, avec la date, le libelle et le montant.|"
  "Le grand livre reprend les ecritures du journal classees par compte.|"
  "La balance fait la somme des debits et des credits de tous les comptes : elle doit etre equilibree.|"
  "Le plan comptable general code les comptes par classes, de 1 a 7.|"
  "La classe 1 regroupe les capitaux propres, la classe 2 les immobilisations et la classe 3 les stocks.|"
  "La classe 4 concerne les tiers, la classe 5 la tresorerie, la classe 6 les charges et la classe 7 les produits.|"
  "Une vente a credit s'enregistre au credit du compte de produits et au debit du compte de creances clients.|"
  "Les ecritures de regularisation ajustent les comptes en fin d'exercice avant l'etablissement des documents de synthese."),
[QC("Combien de comptes sont touches par une operation en partie double ?", "Un seul~Au moins deux~Toujours trois~Aucun", 1,
     "Chaque ecriture comporte un debit et un credit de meme montant."),
 QC("Quel coté d'un compte augmente les charges ?", "Le credit~Le debit~Les deux~Aucun", 1,
     "Les charges et les actifs sont augmentes au debit."),
 QC("Que contient le journal comptable ?", "Les comptes classes par numero~Les ecritures par ordre chronologique~Le bilan seul~Le compte de resultat seul", 1,
     "Le journal suit l'ordre des dates des operations."),
 QC("Que controle la balance ?", "L'egalite des debits et des credits~Le chiffre d'affaires~La tresorerie~L'impot", 0,
     "La balance verifie que la somme des debits egale celle des credits."),
 QC("Quelle classe du plan comptable regroupe les charges ?", "Classe 1~Classe 4~Classe 6~Classe 7", 2,
     "La classe 6 enregistre les charges, la classe 7 les produits."),
 QC("Une vente a credit est enregistree ...", "Au debit des produits et au credit des creances~Au credit des produits et au debit des creances~Au debit de la tresorerie et au credit des dettes~Au seul credit de la tresorerie", 1,
     "On constate une creance client au debit et un produit au credit."),
 QC("A quoi servent les ecritures de regularisation ?", "A changer le plan comptable~A ajuster les comptes en fin d'exercice~A supprimer le journal~A calculer la TVA uniquement", 1,
     "Elles Corrigent les comptes avant la clôture et les documents de synthese."),
 QT("Enregistrer une vente de 1 200 euros hors taxes a credit en precisant les comptes touches.",
    "La vente de 1 200 euros hors taxes a credit se decompose en deux ecritures simultanees. On debite le compte 411 Client pour 1 200 euros, car l'entreprise acquiert une creance sur son client : c'est un actif qui augmente. On credite le compte 701 Vente de marchandises pour 1 200 euros, car la vente est un produit de l'exercice. La somme des debits egale la somme des credits, ce qui respecte la partie double. Si la TVA s'applique, on ajoute au debit du client le montant de la TVA collectee et on credite un compte de TVA collectee. Le journal portera cette ecriture a la date de la vente avec le libelle vente a credit.",
    "On attend debit creances clients 1 200 et credit produit vente 1 200, avec l'egalite des montants."),
 QT("Pourquoi la balance est-elle un outil de controle indispensable ?",
    "La balance additionne tous les soldes debit et credit des comptes du grand livre. Si les deux totaux different, une erreur a ete commise : montant oublie, ecriture sens inverse, erreur de report ou compte non solde. Elle ne garantit pas que toutes les operations ont ete enregistrees, mais elle detecte les incoherences mecaniques de la comptabilite. C'est pourquoi elle precede la preparation du bilan et du compte de resultat. Un comptable doit egalement verifier les pieces justificatives et les rapprochements bancaires, car une ecriture equilibree peut malgre tout etre erronee dans son principe.",
    "On doit expliquer le controle de l'egalite, donner des exemples d'erreurs et rappeler les limites du controle.")],
C("La partie double enregistre chaque operation par un debit et un credit de meme montant.",
  "Ecriture = compte debite + compte credite + montant identique",
  "Journal → grand livre → balance → documents de synthese",
  "Partie double~Double enregistrement~Debit~Augmente actifs et charges~Credit~Augmente produits et dettes~Journal~Ordre chronologique~Balance~Controle d'equilibre",
  "Analyser l'operation et les comptes touches|Determiner le sens debit ou credit|Ecrire au journal avec date et libelle|Reporter au grand livre|Verifier l'equilibre de la balance",
  "Inverser debit et credit|Oublier d'enregistrer une operation|Confondre classe 6 et classe 7|Croire qu'une balance equilibree prouve tout",
  "Vente 1 200~Debit client 411~Credit vente 701~TVA~Ajouter au debit du client~Balance~Debits egale credits~Regularisation~Fin d'exercice",
  "Debit~Actifs et charges en hausse~Credit~Dettes et produits en hausse~Creance~Droit de recevoir~Dette~Obligation de payer",
  "Journal~Chronologie~Grand livre~Par compte~Balance~Par solde~Plan comptable~Classes 1 a 7~Document de synthese~Bilan et resultat"))


# ============================================================ B09
add("B09", "TVA, facturation et documents commerciaux", "Comptabilité", ["Terminale"],
S("La taxe sur la valeur ajoutee, ou TVA, est un impot indirect sur la consommation.|"
  "Elle est collectee par les entreprises lors de leurs ventes et reversee a l'Etat.|"
  "La TVA collectee est celle facturee aux clients ; la TVA deductible est celle payee aux fournisseurs.|"
  "La TVA due s'obtient par TVA collectee moins TVA deductible.|"
  "Le taux normal est de 20 pour cent en France, avec des taux reduits pour certains biens et services.|"
  "Une facture doit mentionner les coordonnees du vendeur et du client, la date, le detail des operations et le numero de TVA.|"
  "Le total d'une facture hors taxes, plus TVA, donne le montant toutes taxes comprises.|"
  "Une facture simplifiee est utilisee pour les petites ventes au detail.|"
  "Un avoir est un document qui corrige une facture, par exemple apres un retour de marchandise.|"
  "Le bon de commande formalise la demande du client avant la vente.|"
  "Le bon de livraison prouve la remise physique des marchandises.|"
  "La declaration de TVA recapitule les montants collectes et deductibles pour une periode donnee."),
[QC("Qui collecte la TVA pour le compte de l'Etat ?", "Les consommateurs~Les entreprises~Les banques~Les collectivites", 1,
     "Les assujettis facturent et reversent la TVA."),
 QC("Comment calculer la TVA due ?", "Collectee plus deductible~Collectee moins deductible~Deductible seule~Chiffre d'affaires moins achats", 1,
     "On deduit la TVA payee en amont de la TVA facturee en aval."),
 QC("Quel est le taux normal de TVA en France ?", "5,5 pour cent~10 pour cent~20 pour cent~33 pour cent", 2,
     "Le taux normal est de 20 pour cent ; 10 et 5,5 sont des taux reduits."),
 QC("Quel document corrige une facture deja emise ?", "Un bon de commande~Un avoir~Un relevé bancaire~Un contrat de travail", 1,
     "L'avoir est une facture negative ou rectificative."),
 QC("Que prouve le bon de livraison ?", "Le paiement~La remise des marchandises~La commande~La declaration de TVA", 1,
     "Il atteste de la livraison physique des biens."),
 QC("Quelle mention est obligatoire sur une facture ?", "La couleur du papier~Le numero de TVA du vendeur~Le nom du commercial~L'heure de mise en page", 1,
     "Le numero d'identification TVA est une mention obligatoire."),
 QC("Un article a 80 euros hors taxes a 20 pour cent de TVA. Le total TTC est :", "84 euros~88 euros~96 euros~100 euros", 2,
     "La TVA est 16 euros, donc le total est 96 euros."),
 QT("Calculer la TVA due pour une entreprise qui facture 50 000 euros HT et achète 20 000 euros HT au taux de 20 pour cent.",
    "La TVA collectee sur les ventes vaut 50 000 x 0,20 = 10 000 euros. La TVA deductible sur les achats vaut 20 000 x 0,20 = 4 000 euros. La TVA due a l'Etat est donc 10 000 - 4 000 = 6 000 euros. L'entreprise ne supporte pas definitivement la taxe sur ses achats : elle la recupere parce que les biens achetes sont utilises pour son activite taxable. Le montant de 6 000 euros correspond approximativement a la valeur ajoutee de l'entreprise, soit 30 000 euros, multipliee par 20 pour cent. C'est precisement la logique de la taxe sur la valeur ajoutee.",
    "On attend collectee 10 000, deductible 4 000, due 6 000 et le lien avec la valeur ajoutee."),
 QT("Distinguer le role du bon de commande, du bon de livraison et de la facture dans une vente.",
    "Le bon de commande est emis par le client : il precise la quantite, le prix et les conditions, et il vaut acceptation de l'offre. Le bon de livraison est emis par le vendeur : il prouve que les marchandises ont effectivement ete remises au client a une date donnee. La facture est egalement emise par le vendeur : elle constate la vente, chiffre le montant hors taxes et TTC, indique la TVA et sert de piece comptable et de titre de paiement. Les trois documents correspondent a des moments differents de la transaction : avant la livraison, pendant la livraison et apres la vente. Ils doivent etre coherents en quantite et en prix.",
    "On doit situer les trois documents dans le temps et preciser leur auteur et leur fonction.")],
C("La TVA est collectee sur les ventes, deductible sur les achats, et documentee par la facturation.",
  "TVA due = TVA collectee - TVA deductible",
  "Total TTC = base HT + TVA · taux normal 20 pour cent",
  "TVA collectee~Facturee aux clients~TVA deductible~Payee aux fournisseurs~Facture~Piece justificative~Avoir~Correction~Bon de livraison~Preuve de remise",
  "Determiner le taux applicable|Calculer la base hors taxes|Calculer la TVA collectee et deductible|Etablir la facture avec ses mentions|Declarer le solde de TVA",
  "Appliquer le taux au montant TTC|Oublier la mention du numero de TVA|Confondre avoir et facture|Deduire une TVA non afferente a l'activite",
  "Ventes 50 000~Collectee 10 000~Achats 20 000~Deductible 4 000~TVA due~6 000~Article 80 HT~TTC 96 euros~Valeur ajoutee~30 000",
  "Bon de commande~Avant la vente~Bon de livraison~Au moment de la livraison~Facture~Apres la vente~Avoir~Rectification",
  "Hors taxes~Base de calcul~TTC~Montant paye~TVA due~Solde a reverser~Declaration~Periode fiscale"))


# ============================================================ B10
add("B10", "Couts, marges et seuil de rentabilite", "Comptabilité", ["Terminale"],
S("Le cout de revient represente l'ensemble des charges necessaires pour produire et vendre un bien ou un service.|"
  "Un cout direct est affecte sans ambiguite a un produit, comme la matiere premiere.|"
  "Un cout indirect doit etre reparti selon une cle, par exemple les frais generaux.|"
  "Un cout variable augmente avec le volume de production, tandis qu'un cout fixe reste constant dans un certain intervalle.|"
  "La marge sur cout variable s'obtient par chiffre d'affaires moins couts variables.|"
  "Le taux de marge sur cout variable est la marge rapportee au chiffre d'affaires.|"
  "Le resultat s'obtient en soustrayant les charges fixes de la marge sur cout variable.|"
  "Le seuil de rentabilite est le chiffre d'affaires pour lequel le resultat est nul.|"
  "On le calcule en divisant les charges fixes par le taux de marge sur cout variable.|"
  "Le point mort designe le meme seuil exprime en nombre de produits vendus.|"
  "La marge commerciale est la difference entre le chiffre d'affaires et le cout d'achat des marchandises vendues.|"
  "Ces calculs aident a decider d'un prix, d'une commande speciale ou d'un investissement."),
[QC("Quel est un cout direct ?", "Les frais generaux~La matiere premiere d'un produit~Le loyer du siege~Les salaries administratifs", 1,
     "La matiere premiere est affectee directement au produit fabrique."),
 QC("Quel cout reste constant quand le volume varie peu ?", "Un cout variable~Un cout fixe~Un cout marginal~Une charge directe", 1,
     "Le cout fixe ne varie pas avec le volume dans un intervalle donne."),
 QC("Comment calculer la marge sur cout variable ?", "CA moins couts fixes~CA moins couts variables~CA plus couts variables~Charges fixes moins charges variables", 1,
     "C'est la contribution des ventes apres deduction des couts variables."),
 QC("Comment obtenir le seuil de rentabilite en chiffre d'affaires ?", "Charges fixes divisées par le taux de marge~Charges variables multipliees par le taux~CA divisé par les charges~Marge plus charges fixes", 0,
     "Le seuil est atteint quand la marge couvre exactement les charges fixes."),
 QC("Que vaut le resultat au seuil de rentabilite ?", "Maximum~Zero~Egal au chiffre d'affaires~Negatif", 1,
     "Au seuil, l'entreprise n'a ni benefice ni perte."),
 QC("La marge commerciale est ...", "CA moins achats de marchandises~CA moins salaires~Achats plus TVA~Resultat net", 0,
     "Elle measure la marge realisée sur la revente."),
 QC("Un cout qui augmente d'une unite supplementaire est un cout ...", "Fixe~Marginal~Historique~Indirect", 1,
     "Le cout marginal est le surcout d'une unite produite en plus."),
 QT("Calculer le seuil de rentabilite : chiffre d'affaires 200 000, couts variables 120 000, charges fixes 50 000.",
    "La marge sur cout variable vaut 200 000 - 120 000 = 80 000 euros. Le taux de marge sur cout variable est 80 000 / 200 000 = 0,4, soit 40 pour cent. Le seuil de rentabilite en chiffre d'affaires est charges fixes divisées par le taux de marge : 50 000 / 0,4 = 125 000 euros. A ce niveau de ventes, la marge sur cout variable est 125 000 x 0,4 = 50 000 euros, ce qui couvre exactement les charges fixes : le resultat est nul. Le resultat actuel est 80 000 - 50 000 = 30 000 euros de benefice. L'entreprise supporte donc bien au-dessus de son point mort.",
    "On attend marge 80 000, taux 40 pour cent, seuil 125 000 euros et resultat 30 000 euros."),
 QT("Faut-il accepter une commande speciale a un prix inferieur au cout de revient complet ?",
    "La reponse depend de la capacite de production disponible. Si l'entreprise a des capacites inutilisees, les charges fixes sont deja couvertes par l'activite normale : il suffit que le prix de la commande soit superieur au cout variable supplementaire pour que l'operation degage une marge additionnelle positive. Accepter peut alors etre rentable meme si le prix est inferieur au cout complet. En revanche, si la commande mobilise toute la capacite et decale des ventes plus rentables, il faut comparer les marges perdues. Il faut aussi verifier que le prix ne destabilise pas le marche et que la qualite et les delais sont tenus.",
    "On doit raisonner en couts variables et en capacite disponible, et mentionner les risques commerciaux.")],
C("La marge sur cout variable couvre les charges fixes ; le seuil de rentabilite est le point ou le resultat devient nul.",
  "Resultat = marge sur cout variable - charges fixes",
  "Seuil = charges fixes / taux de marge sur cout variable",
  "Cout variable~Suit le volume~Cout fixe~Constant~Marge~CA moins couts variables~Taux de marge~Marge sur CA~Seuil~Resultat nul",
  "Classer les couts en fixes et variables|Calculer la marge sur cout variable|Determiner le taux de marge|Calculer le seuil de rentabilite|Decider avec le cout marginal",
  "Utiliser le cout complet pour une decision a court terme|Confondre marge commerciale et marge sur cout variable|Oublier la capacite disponible|Ignorer les couts fixes dans le seuil",
  "CA 200 000~Variables 120 000~Marge 80 000~Taux 40 pour cent~Fixes 50 000~Seuil 125 000~Resultat~30 000~Commande~Cout marginal",
  "Cout direct~Affecte au produit~Cout indirect~Reparti~Cout variable~Fonction du volume~Cout fixe~Independent du volume",
  "Seuil de rentabilite~CA sans benefice ni perte~Point mort~Volume correspondant~Marge commerciale~CA moins achats~Cout marginal~Une unite de plus"))


# ============================================================ B11
add("B11", "Les sources du droit et la hierarchie des normes", "Droit", ["1re"],
S("Le droit objectif est l'ensemble des regles juridiques applicables dans un Etat.|"
  "Les droits subjectifs sont les pouvoirs reconnus a chaque personne, comme le droit de propriété.|"
  "La loi est une regle generale et abstracte votee par le Parlement et promulguee par le President.|"
  "Un decret est pris par le Premier ministre pour appliquer la loi ; un arrete est pris par un ministre ou un prefet.|"
  "La Constitution de 1958 est la norme superieure de l'ordre juridique interne.|"
  "Le bloc de constitutionnalite comprend la Constitution, la Declaration de 1789 et le preambule de 1946.|"
  "Le Conseil constitutionnel verifie la conformite des lois a la Constitution, notamment par la question prioritaire de constitutionnalite.|"
  "La jurisprudence est l'ensemble des solutions degagees par les tribunaux, en particulier la Cour de cassation et le Conseil d'Etat.|"
  "La coutume est une pratique generale accompagnee de la conviction qu'elle est obligatoire.|"
  "La doctrine correspond aux analyses des professeurs de droit ; elle est une source d'influence, non une source obligatoire.|"
  "Le droit europeen comprend les traites, les reglements directement applicables et les directives transposees en droit interne.|"
  "La hierarchie des normes impose qu'une regle inferieure ne contredise pas une regle superieure."),
[QC("Quel texte est la norme superieure en droit interne francais ?", "Une loi~La Constitution~Un arrete~Un decret", 1,
     "La Constitution prime sur toutes les autres regles internes."),
 QC("Qui vote la loi ?", "Le President seul~Le Parlement~Le Conseil d'Etat~Le Prefet", 1,
     "La loi est votee par l'Assemblee nationale et le Senat."),
 QC("Quel texte est pris par le Premier ministre ?", "Une loi~Un decret~Une ordonnance du Conseil~Un jugement", 1,
     "Le decret est un acte reglementaire du Premier ministre."),
 QC("Que control le Conseil constitutionnel ?", "La conformite des lois a la Constitution~Les comptes des entreprises~Les contrats prives~Les election locales", 0,
     "Il assure le controle de constitutionnalite, notamment par la QPC."),
 QC("Quelle source est constituee par les decisions des tribunaux ?", "La doctrine~La coutume~La jurisprudence~Le decret", 2,
     "La jurisprudence denomme l'ensemble des solutions jurisprudentielles."),
 QC("Un reglement europeen est ...", "Directement applicable~Toujours transpose~Sans valeur~Une simple recommandation", 0,
     "Le reglement s'applique directement dans tous les Etats membres."),
 QC("Que signifie la hierarchie des normes ?", "Une regle superieure prime sur une regle inferieure~Toutes les regles se valent~Le juge choisit au hasard~La coutume prime toujours", 0,
     "Une norme inferieure ne peut deroger a une norme superieure."),
 QT("Distinguer droit objectif et droits subjectifs et donner un exemple de chacun.",
    "Le droit objectif designe l'ensemble des regles juridiques qui s'imposent a tous dans un Etat, comme l'interdiction du vol ou les regles du Code civil. Les droits subjectifs sont les prerogatives dont jouit une personne physique ou morale en vertu de ces regles, par exemple son droit de propriete sur un appartement ou son droit a la liberte d'expression. Le droit objectif est la regle collective, tandis que le droit subjectif est la situation individuelle protegee. Les deux sont lies : c'est parce que le droit objectif protege la propriete que le proprietaire dispose d'un droit subjectif opposable aux autres.",
    "On attend la definition des deux notions, un exemple pour chacune et leur lien."),
 QT("Classer les normes suivantes de la plus haute a la plus basse : loi, arrete prefectoral, Constitution, decret, reglement europeen.",
    "Au sommet se trouve la Constitution, norme interieure suprieure. Le reglement europeen occupe une place particuliere : il prime sur les lois nationales dans son domaine en vertu de la primauté du droit de l'Union. Vient ensuite la loi votee par le Parlement, puis le decret du Premier ministre, et enfin l'arrete prefectoral pris pour l'application locale d'une regle. Si un arrete contredit la loi, le juge administratif peut l'annuler pour exces de pouvoir. Cette gradation est la hierarchie des normes : chaque acte doit etre conforme a celui qui le domine et ne peut creer une regle contraire.",
    "On attend Constitution, droit europeen, loi, decret, arrete, avec l'idee de conformite et de controle.")],
C("Le droit s'organise en une hierarchie de normes ou chaque regle doit respecter la regle superieure.",
  "Constitution > lois et traites > reglements > actes individuels",
  "Sources : loi · decret · arrete · jurisprudence · coutume · doctrine",
  "Droit objectif~Regles generales~Droit subjectif~Prerogative individuelle~Constitution~Norme supreme~Loi~Votee par le Parlement~Decret~Acte du Premier ministre",
  "Identifier la nature de la regle|Determiner son auteur|La situer dans la hierarchie|Verifier sa conformite|Consulter la jurisprudence applicable",
  "Confondre loi et decret|Croire que la doctrine est obligatoire|Ignorer la primauté europeenne|Appliquer un arrete contraire a la loi",
  "Constitution~1958~Declaration~1789~Preambule~1946~QPC~Controle de constitutionnalite~Jurisprudence~Cour de cassation",
  "Loi~Parlement~Decret~Premier ministre~Arrete~Ministre ou prefet~Coutume~Pratique obligatoire~Doctrine~Analyse professee",
  "Reglement europeen~Directement applicable~Directive~Transposee en loi~Hierarchie~Conformite~Norme~Regle juridique"))


# ============================================================ B12
add("B12", "La personne, la capacite juridique et les droits de la personnalite", "Droit", ["1re"],
S("Une personne physique est un etre humain titulaire de droits et de devoirs.|"
  "La personnalite juridique s'acquiert a la naissance et prend fin au deces.|"
  "La capacite de jouissance est l'aptitude a etre titulaire de droits, reconnue a tous.|"
  "La capacite d'exercice est l'aptitude a accomplir soi-meme des actes juridiques valables.|"
  "Un mineur a une capacite d'exercice limitee : il ne peut pas conclure seul tous les contrats.|"
  "L'emancipation permet a un mineur de seize ans d'acquerir une capacite d'exercice plus etendue.|"
  "La majorite est fixee a dix-huit ans depuis 1974.|"
  "Un majeur peut etre prive d'exercice sous tutelle ou voir ses actes encadres sous curatelle.|"
  "Une personne morale est un groupement reconnu comme sujet de droits, comme une association ou une societe.|"
  "La personnalite morale suppose une organisation, des organes et souvent une immatriculation.|"
  "L'etat civil constate l'identite, la naissance, la filiation et le deces des personnes.|"
  "Les droits de la personnalite protegent le nom, l'image, la vie privee et l'integrite de la personne."),
[QC("Quand s'acquiert la personnalite juridique ?", "A la conception~A la naissance~A la majorite~Au mariage", 1,
     "La personnalite juridique commence a la naissance et s'eteint au deces."),
 QC("Quelle est la capacite d'exercice ?", "Le droit d'etre titulaire~L'aptitude a accomplir des actes valables~Le droit de vote~La nationalite", 1,
     "La capacite d'exercice permet d'agir juridiquement soi-meme."),
 QC("Quel age marque la majorite en France ?", "16 ans~18 ans~21 ans~25 ans", 1,
     "La majorite est fixee a 18 ans depuis la reforme de 1974."),
 QC("Quel regime encadre un majeur qui ne peut plus agir seul ?", "La tutelle ou la curatelle~L'emancipation~La minorite~Le mariage", 0,
     "La tutelle et la curatelle sont des mesures de protection des majeurs."),
 QC("Une association est ...", "Une personne physique~Une personne morale~Un acte juridique~Une jurisdiction", 1,
     "L'association est un groupement dote de la personnalite morale."),
 QC("Que constate l'etat civil ?", "Les comptes~L'identite et les evenements familiaux~Les impots~Les contrats commerciaux", 1,
     "Il enregistre naissance, filiation, mariage et deces."),
 QC("Quel droit protege l'utilisation du visage d'une personne ?", "Le droit de propriete~Le droit a l'image~Le droit de vote~Le droit au salaire", 1,
     "Le droit a l'image fait partie des droits de la personnalite."),
 QT("Distinguer capacite de jouissance et capacite d'exercice dans le cas d'un mineur.",
    "Un mineur de quinze ans a la capacite de jouissance : il est titulaire de droits, par exemple le droit a son image, a sa scolarite ou a des biens qu'il recoit en donation. En revanche, sa capacite d'exercice est limitee : il ne peut pas vendre seul un bien immobilier ou conclure seul un contrat important, car ses actes sont en principe annulables. Ses representants légaux agissent pour lui. A seize ans, l'emancipation peut lui donner une capacite d'exercice plus large, sous certaines conditions. A dix-huit ans, il acquiert la pleine capacite d'exercice : il peut accomplir seul la plupart des actes juridiques.",
    "On attend la definition des deux capacites, des exemples et l'evolution avec l'age."),
 QT("Expliquer pourquoi la personnalite morale est utile a la vie economique.",
    "La personnalite morale permet a un groupement d'agir comme un sujet de droits distinct de ses membres. Une societe peut ainsi conclure des contrats, posseder des biens, etre poursuivie en justice et payer des impots en son nom propre. Cette distinction protege les associes : dans une societe a responsabilite limitee, leur engagement est en principe limite au montant de leur apport. Elle assure aussi la continuite de l'activite : le depart ou le deces d'un associe ne met pas fin a la societe. Enfin, elle simplifie la gestion grace a des organes, comme le gerant ou le conseil d'administration, qui representent le groupement.",
    "On doit montrer l'autonomie juridique, la limitation de responsabilite et la continuite.")],
C("La personne physique ou morale est titulaire de droits ; sa capacite determine les actes qu'elle peut accomplir.",
  "Personnalite juridique = jouissance + exercice",
  "Naissance → minorite → emancipation ou majorite → protection eventuelle",
  "Personne physique~Etre humain~Personnalite juridique~Titulaire de droits~Capacite de jouissance~Avoir des droits~Capacite d'exercice~Agir valablement~Personne morale~Groupement reconneu",
  "Determiner la qualite de la personne|Verifier sa capacite d'exercice|Identifier les actes autorises|Controle la forme de l'acte|Proteger les droits de la personnalite",
  "Confondre jouissance et exercice|Croire qu'un mineur n'a aucun droit|Ignorer la tutelle des majeurs|Oublier l'immatriculation d'une personne morale",
  "Mineur de 15 ans~Droits mais actes limites~Emancipation~16 ans~Majorite~18 ans~Tutelle~Representation~Association~Personne morale",
  "Capacite de jouissance~Titulaire de droits~Capacite d'exercice~Accomplir des actes~Minorite~Capacite reduite~Majorite~Capacite pleine",
  "Etat civil~Identite et filiation~Nom~Droit de la personnalite~Image~Droit a l'image~Vie privee~Protection~Integrite~Respect de la personne"))


# ============================================================ B13
add("B13", "Le contrat : formation, validite et effets", "Droit", ["1re", "Terminale"],
S("Le contrat est un accord de volontes destine a creer, modifier ou eteindre des obligations.|"
  "L'article 1103 du Code civil pose que les contrats legalement formes ont force de loi entre les parties.|"
  "La formation du contrat suppose un consentement, une capacite, un contenu licite et certain et souvent une forme.|"
  "Le consentement resulte d'une offre et d'une acceptation claires et concordantes.|"
  "Une offre peut etre retractee avant l'acceptation, sous certaines conditions de delai.|"
  "L'erreur, le dol et la violence sont des vices qui peuvent annuler le consentement.|"
  "L'erreur porte sur une qualité essentielle de la chose ou de la personne.|"
  "Le dol est une manoeuvre frauduleuse pour obtenir le consentement.|"
  "Un contrat synallagmatique cree des obligations reciproques ; un contrat unilatéral n'en cree que pour une partie.|"
  "Un contrat a titre onereux comporte une contrepartie, contrairement au contrat a titre gratuit.|"
  "Certains contrats solennels doivent etre ecrits, comme la donation ou la vente immobiliere.|"
  "L'inexecution contractuelle entraine une responsabilite et peut conduire a la resolution du contrat."),
[QC("Qu'est-ce qu'un contrat ?", "Un acte unilateral~Un accord de volontes creant des obligations~Une decision de justice~Un simple document fiscal", 1,
     "La definition legale repose sur l'accord de volontes."),
 QC("Quel article du Code civil consacre la force obligatoire du contrat ?", "Article 1103~Article 1240~Article 1~Article 1382", 0,
     "L'article 1103 dispose que le contrat a force de loi entre les parties."),
 QC("Quels elements sont necessaires a la formation d'un contrat ?", "Consentement, capacite, contenu licite et forme eventuelle~Seulement l'ecrit~Seulement le prix~Le cachet du maire", 0,
     "Ce sont les conditions classiques de validite du contrat."),
 QC("Qu'appelle-t-on dol ?", "Une erreur sur la chose~Une manoeuvre frauduleuse~Une violence physique~Un simple retard", 1,
     "Le dol est une tromperie destinee a obtenir le consentement."),
 QC("Un contrat synallagmatique ...", "Ne cree aucune obligation~Cree des obligations reciproques~Est toujours gratuit~Doit etre ecrit", 1,
     "Chaque partie est a la fois debiteur et creancière d'une obligation."),
 QC("Quel contrat est a titre gratuit ?", "Une vente~Une donation~Un bail commercial~Un contrat de travail", 1,
     "La donation ne comporte pas de contrepartie onereuse."),
 QC("Que peut prononcer le juge en cas d'inexecution grave ?", "La resolution du contrat~La creation d'un nouveau contrat~L'annulation automatique de la loi~La suppression du tribunal", 0,
     "La resolution met fin au contrat et aux obligations restant a executer."),
 QT("Analyse la formation d'un contrat de vente entre un particulier et un commerçant.",
    "Le commerçant fait une offre en proposant un bien a un prix determine, par exemple dans une vitrine ou sur un site. Le particulier accepte en disant qu'il achete : le consentement est alors forme par la rencontre de l'offre et de l'acceptation. Les deux parties ont la capacite d'exercice necessaire. Le contenu est licite et certain : la chose est designee et le prix est fixe. La vente d'un objet courant peut etre verbale, mais une facture est fort utile comme preuve. Si le commerçant a cache un defaut important, le consentement peut etre annule pour dol ou erreur. Une fois le contrat forme, l'acheteur doit payer et le vendeur doit livrer.",
    "On attend offre, acceptation, capacite, contenu licite et certain, forme et effets."),
 QT("Expliquer la difference entre responsabilite contractuelle et responsabilite delictuelle.",
    "La responsabilite contractuelle s'applique lorsqu'une partie n'execute pas une obligation nee d'un contrat valable : le creancier doit prouver l'inexecution et peut demander des dommages-interets ou la resolution. La responsabilite delictuelle s'applique en l'absence de contrat, lorsqu'une faute cause un dommage a autrui, sur le fondement de l'article 1240 du Code civil. Les conditions different : faute, dommage et lien de causalite pour le delit, inexcution d'une obligation preexistante pour le contrat. Le contrat peut aussi prevoir des clauses limitatives de responsabilite, alors que la responsabilite delictuelle est plus difficile a aménager a l'avance.",
    "On doit opposer l'origine contractuelle et l'origine delictuelle, avec les conditions propres a chacune.")],
C("Le contrat est un accord de volontes qui cree des obligations legalement protegees.",
  "Formation : consentement + capacite + contenu licite et certain",
  "Force obligatoire · vices du consentement · inexecution · resolution",
  "Contrat~Accord de volontes~Offre~Proposition~Acceptation~Accord~Consentement~Volonte concordante~Vice~Erreur, dol, violence~Force obligatoire~Loi entre les parties",
  "Verifier l'offre et l'acceptation|Controler la capacite des parties|Verifier le contenu et la forme|Identifier les vices eventuels|Analyser les obligations nees et leur execution",
  "Confondre offre et acceptation|Ignorer un vice du consentement|Croire qu'un contrat verbal n'a aucune valeur|Oublier que la force obligatoire n'est pas absolue",
  "Vente~Offre et acceptation~Facture~Preuve~Defaut cache~Dol ou erreur~Prix~Contenu certain~Livraison~Obligation du vendeur",
  "Contrat synallagmatique~Obligations reciproques~Contrat unilateral~Obligation d'une partie~Onereux~Avec contrepartie~Gratuit~Sans contrepartie",
  "Responsabilite contractuelle~Inexecution d'un contrat~Responsabilite delictuelle~Faute et dommage~Resolution~Fin du contrat~Dommages-interets~Reparation"))


# ============================================================ B14
add("B14", "Responsabilite civile et responsabilite penale", "Droit", ["Terminale"],
S("La responsabilite civile a pour fonction de reparer le dommage subi par une victime.|"
  "L'article 1240 du Code civil pose que tout fait quelconque qui cause un dommage a autrui oblige son auteur a le reparer.|"
  "La responsabilite delictuelle repose sur trois elements : une faute, un dommage et un lien de causalite.|"
  "On peut etre responsable de son propre fait, du fait d'autrui, comme un parent ou un employeur, ou du fait des choses que l'on a sous sa garde.|"
  "Le dommage peut etre materiel, corporel ou moral.|"
  "La reparation prend generalement la forme de dommages-interets verses a la victime.|"
  "La responsabilite contractuelle s'applique en cas d'inexecution d'une obligation issue d'un contrat.|"
  "La responsabilite penale vise a punir une infraction au nom de la societe.|"
  "Les infractions se classent en contraventions, delits et crimes, selon leur gravite.|"
  "Une infraction comporte un element materiel, le fait commis, et souvent un element intentionnel.|"
  "Les peines peuvent etre des amendes, des peines de prison ou des peines complementaires.|"
  "La prescription eteint l'action apres un delai legal ; les principes generaux du droit penal imposent une loi prealable et precise."),
[QC("Quel article du Code civil fonde la responsabilite delictuelle ?", "Article 1103~Article 1240~Article 1~Article 1104", 1,
     "L'article 1240 impose la reparation du dommage cause par un fait fautif."),
 QC("Quels sont les trois elements de la responsabilite delictuelle ?", "Faute, dommage, lien de causalite~Contrat, prix, livraison~Loi, decret, arrete~Offre, acceptation, capacite", 0,
     "Il faut une faute, un dommage et un lien de causalite entre les deux."),
 QC("Qui est responsable du dommage cause par un enfant mineur ?", "Personne~Ses parents en principe~L'Etat toujours~Le voisin", 1,
     "Les parents sont responsables du fait de leurs enfants mineurs vivant avec eux."),
 QC("Quelle est une categorie d'infraction penale ?", "Le delit~La clause~La creance~Le bail", 0,
     "Contraventions, delits et crimes sont les trois categories d'infractions."),
 QC("Quel element est souvent requis en droit penal ?", "L'intention ou la faute~Le contrat ecrit~La facture~Le salaire", 0,
     "La plupart des delits exigent un element intentionnel, sauf infractions de negligence."),
 QC("Que permet la prescription ?", "D'augmenter la peine~D'eteindre l'action apres un delai~De supprimer le tribunal~De creer une infraction", 1,
     "Au-dela du delai legal, l'action penale ou civile ne peut plus etre exercee."),
 QC("Quelle est la finalite de la responsabilite penale ?", "Reparer la victime~Punir l'infraction au nom de la societe~Payer une facture~Signer un contrat", 1,
     "La responsabilite penale a une fonction repressive, distincte de la reparation civile."),
 QT("Distinguer responsabilite civile et responsabilite penale dans un accident de la route.",
    "Si un conducteur cause un accident, la responsabilite civile vise a reparer les dommages : l'assurance indemnise la victime pour les blessures et les dégats matériels, sur le fondement de l'article 1240 ou de la legislation sur les accidents de la circulation. La responsabilite penale, elle, vise a sanctionner une infraction au code de la route, par exemple l'exces de vitesse ou la conduite en etat d'ivresse : le conducteur peut recevoir une amende, une suspension de permis ou une peine de prison. Une meme situation peut donc donner lieu a deux actions distinctes, devant des juridictions differentes, avec des finalites differentes : reparer d'un cote, punir de l'autre.",
    "On attend la finalite reparatrice et la finalite punitive, avec des exemples et des juridictions."),
 QT("Expliquer la responsabilite du fait d'autrui dans le cadre d'une entreprise.",
    "Un employeur peut etre declare responsable des dommages causes par ses salaries dans l'exercice de leurs fonctions. Par exemple, si un livreur endommage le bien d'un client pendant une livraison, l'entreprise engage sa responsabilite civile parce qu'elle a organise l'activite et tire profit du travail du salarie. Cette responsabilite ne supprime pas celle du salarie, mais elle offre a la victime un debiteur solvable. Elle incite aussi l'employeur a former ses equipes, a definir des procedures et a souscrire une assurance. En droit penal, la responsabilite des personnes morales peut egalement etre engagee pour certaines infractions commises pour leur compte.",
    "On attend la notion de fait d'autrui, l'exemple de l'employeur et la fonction de protection de la victime.")],
C("La responsabilite civile repare le dommage, la responsabilite penale punit l'infraction.",
  "Responsabilite delictuelle = faute + dommage + lien de causalite",
  "Contravention · delit · crime · amendes et peines",
  "Responsabilite civile~Reparation~Article 1240~Fait personnel~Fait d'autrui~Parent ou employeur~Fait des choses~Chose sous garde~Responsabilite penale~Sanction",
  "Identifier la nature du dommage|Verifier l'existence d'une faute|Etablir le lien de causalite|Determiner la juridiction competente|Evaluer la reparation ou la peine",
  "Confondre responsabilite civile et penale|Oublier le lien de causalite|Ignorer la prescription|Croire que l'assurance supprime la faute",
  "Accident~Dommages corporel et materiel~Assurance~Indemnisation~Exces de vitesse~Infraction~Amende~Peine~Prescription~Extinction de l'action",
  "Responsabilite civile~Dommages-interets~Responsabilite penale~Amende et prison~Responsabilite contractuelle~Inexecution~Responsabilite delictuelle~Sans contrat",
  "Contravention~Infraction legere~Delit~Infraction plus grave~Crime~Infraction la plus grave~Faute~Comportement reproche~Dommage~Prejudice subi"))


# ============================================================ B15
add("B15", "Droit du travail et contrat de travail", "Droit", ["Terminale"],
S("Le contrat de travail est un accord par lequel une personne s'engage a travailler sous la direction d'un employeur, en echange d'un salaire.|"
  "Le critere essentiel est le lien de subordination : l'employeur donne des ordres, controle et sanctionne.|"
  "Le contrat a duree indeterminee, ou CDI, est la forme normale de l'embauche.|"
  "Le contrat a duree determinee, ou CDD, est limite dans le temps et strictement encadre par la loi.|"
  "Un employeur peut recruter en CDD pour remplacer un salarie absent ou faire face a un surcroît temporaire d'activite.|"
  "La periode d'essai permet a l'employeur et au salarie de verifier leur accord avant l'embauche definitive.|"
  "Le salaire ne peut etre inferieur au salaire minimum interprofessionnel de croissance, ou SMIC.|"
  "La duree legale du travail est fixee a trente-cinq heures hebdomadaires pour un temps plein.|"
  "Le salarie a droit a des conges payes et au repos hebdomadaire.|"
  "La convention collective de la branche peut prevoir des avantages supérieurs a la loi.|"
  "Le licenciement doit avoir une cause reelle et serieuse, economique ou personnelle, et respecter un preavis.|"
  "Les litiges relatifs au contrat de travail sont juges par le conseil de prud'hommes."),
[QC("Quel est le critere essentiel du contrat de travail ?", "Le salaire seul~Le lien de subordination~L'anciennete~Le lieu de travail", 1,
     "La subordination distingue le salarie du travailleur independant."),
 QC("Quelle est la forme normale d'embauche ?", "Le CDD~Le CDI~Le contrat de mission~Le stage", 1,
     "Le contrat a duree indeterminee est le regime de droit commun."),
 QC("Quel motif peut justifier un CDD ?", "Un surcroît temporaire d'activite~Le simple choix de payer moins~L'absence de convention~Une preference du salarie", 0,
     "Le CDD est autorise dans des cas limites precisement enumeres."),
 QC("Quel salaire plancher doit respecter l'employeur ?", "Le SMIG~Le SMIC~Le salaire moyen~Le prix de vente", 1,
     "Le SMIC est le salaire minimum legal."),
 QC("Quelle est la duree legale hebdomadaire du temps plein ?", "30 heures~35 heures~39 heures~40 heures", 1,
     "La duree legale est de trente-cinq heures par semaine."),
 QC("Qui juge les conflits individuels du travail ?", "Le tribunal de commerce~Le conseil de prud'hommes~La cour d'appel administrative~Le conseil constitutionnel", 1,
     "Les prud'hommes sont une juridiction paritaire du travail."),
 QC("Qu'appelle-t-on periode d'essai ?", "Une periode sans salaire~Une periode de verification réciproque~Un conge~Un licenciement", 1,
     "Elle permet a chaque partie d'evaluer la relation avant la confirmation."),
 QT("Distinguer un salarie d'un travailleur independant a partir du lien de subordination.",
    "Le salarie est lie par un contrat de travail : l'employeur lui donne des directives, controle l'execution de sa tache et peut le sanctionner s'il ne respecte pas les consignes. Le travailleur independant, lui, organise librement son activite, choisit ses methodes et supporte le risque economique de son entreprise ; il est paye sur facture. Par exemple, un developpeur recrute qui travaille selon les horaires et les procedures de l'entreprise est salarie, alors qu'un consultant qui fournit une prestation de courte duree avec ses propres outils est independant. La qualification juridique entraine des regimes fiscaux et sociaux differents et protege le salarie.",
    "On attend le critere de subordination, des exemples concrets et les consequences juridiques."),
 QT("Decrire les obligations respectives de l'employeur et du salarie dans un CDI.",
    "L'employeur doit payer le salaire convenu, au moins egal au SMIC, fournir le travail et les moyens necessaires, assurer la securite et la sante au travail, accorder les conges payes et respecter la duree legale du temps de travail. Le salarie doit executer sa tache avec diligence, respecter les instructions legitimes, la confidentialite et le reglement interieur, et ne pas faire concurrence a son employeur pendant le contrat. La convention collective peut ajouter des avantages. En cas de manquement grave, chaque partie peut engager une procedure, et le conseil de prud'hommes tranche le litige.",
    "On doit repartir les obligations des deux cotes et mentionner la convention collective et les prud'hommes.")],
C("Le contrat de travail repose sur un lien de subordination et cree des obligations reciproques.",
  "Salaire + subordination + duree = contrat de travail",
  "CDI · CDD · periode d'essai · SMIC · licenciement · prud'hommes",
  "Contrat de travail~Accord de volonte~Subordination~Direction et controle~CDI~Duree indeterminee~CDD~Duree determinee~Salaire~Contrepartie du travail",
  "Identifier le lien de subordination|Determiner le type de contrat|Verifier la periode d'essai|Controler salaire et duree du travail|Connaitre les regles de rupture",
  "Confondre salarie et independant|Oublier le respect du SMIC|Utiliser un CDD hors cas autorise|Negliger le preavis de licenciement",
  "Employeur~Donne les directives~Salarie~Execute sous autorite~CDI~Embauche normale~CDD~Remplacement~SMIC~Salaire minimum~Prud'hommes~Juridiction paritaire",
  "Salarie~Lien de subordination~Independant~Organisation libre~CDI~Sans date de fin~CDD~Date de fin precisee~Temps partiel~Duree reduite",
  "Licenciement~Rupture par l'employeur~Cause reelle et serieuse~Motif legal~Preavis~Delai avant depart~Conge paye~Droit du salarie~Convention collective~Avantages de branche"))


# ============================================================ B16
add("B16", "Les grands equilibres economiques", "Économie", ["1re"],
S("Une economie nationale se decrit a partir de quelques grandeurs essentielles.|"
  "Le produit interieur brut, ou PIB, mesure la valeur des biens et services produits dans un pays sur une periode.|"
  "La croissance est la variation relative du PIB d'une periode sur l'autre.|"
  "La population active comprend les personnes occupees et celles qui cherchent un emploi.|"
  "Le taux de chomage rapporte le nombre de chomeurs a la population active.|"
  "L'inflation correspond a la hausse generale et durable des prix, mesuree par l'indice des prix a la consommation.|"
  "La balance des paiements enregistre les echanges de biens, de services et de capitaux avec l'etranger.|"
  "Le deficit public est l'ecart negatif entre les recettes et les depenses de l'Etat et des administrations.|"
  "La dette publique est l'accumulation des deficits non rembourses.|"
  "L'equilibre global suppose que la production trouve une demande suffisante pour etre écoulée.|"
  "Les pouvoirs publics influencent cet equilibre par le budget, la fiscalite et la regulation.|"
  "Les grands equilibres sont rarement realises en meme temps : la lutte contre l'inflation peut freiner la croissance."),
[QC("Que mesure le PIB ?", "Le nombre d'habitants~La valeur de la production nationale~Le taux d'interet~La dette", 1,
     "Le PIB additionne les valeurs ajoutees ou la demande finale d'un pays."),
 QC("Comment calcule-t-on un taux de croissance ?", "PIB divisé par la population~Variation relative du PIB~PIB moins inflation~Salaires plus impots", 1,
     "C'est le pourcentage de variation du PIB entre deux periodes."),
 QC("Que comprend la population active ?", "Les enfants et les retraites~Les occupes et les chomeurs~Les seuls salaries~Les seuls fonctionnaires", 1,
     "Elle comprend les personnes en emploi et celles en recherche d'emploi."),
 QC("Comment mesure-t-on l'inflation ?", "Par le chomage~Par l'indice des prix a la consommation~Par le PIB~Par la dette", 1,
     "L'IPC suit l'evolution du prix d'un panier de biens et services."),
 QC("Qu'est-ce que le deficit public ?", "Un excedent de recettes~Des depenses superieures aux recettes~Une hausse des prix~Une baisse du PIB", 1,
     "Le deficit correspond a un solde negatif des finances publiques."),
 QC("Que represente la dette publique ?", "L'accumulation des deficits~Le total des salaires~La valeur de la monnaie~Le nombre d'entreprises", 0,
     "Les deficits non rembourses s'ajoutent pour former la dette."),
 QC("Quel lien existe-t-il entre croissance et chomage ?", "Aucun lien~Une croissance soutenue favorise souvent l'emploi~Le chomage augmente toujours avec la croissance~Le PIB et l'emploi sont identiques", 1,
     "Une activite plus forte accroit generalement la demande de travail."),
 QT("Expliquer pourquoi les grands equilibres economiques sont difficiles a atteindre simultanement.",
    "Une relance de la demande peut augmenter la production et reduire le chomage, mais si l'offre ne suit pas, les prix montent : l'inflation apparait. Une politique de rigueur pour controler l'inflation reduit la demande et peut accroitre le chomage et ralentir la croissance. Le deficit budgetaire peut soutenir l'activite a court terme, mais il accroit la dette et peut inquieter les preteurs. Enfin, un excedent commercial peut accompagner une croissance faible si la demande interne est atone. Les gouvernements doivent donc arbitrer entre objectifs parfois contradicttoires et tenir compte des delais d'action des politiques.",
    "On attend des arbitrages entre inflation, chomage, croissance et finances publiques, avec exemples."),
 QT("Comment lire une situation ou le PIB augmente de 1,5 pour cent, l'inflation de 5 pour cent et le chomage de 8 pour cent ?",
    "La croissance de 1,5 pour cent indique une levee d'activite modestemment positive. Une inflation de 5 pour cent est nettement superieure a l'objectif de la Banque centrale europeenne, fixe a 2 pour cent a moyen terme : le pouvoir d'achat des menages est erode. Un chomage de 8 pour cent signifie qu'une part importante de la population active est sans emploi. On peut parler de stagflation moderee : croissance faible et inflation forte coexistent. Les autorites doivent alors distinguer les causes du choc : hausse des couts energétiques, tensions sur les salaires ou demande excessive, car les reponses different.",
    "On attend l'analyse des trois indicateurs et l'identification d'une situation de croissance faible avec inflation.")],
C("Les grands equilibres se lisent avec le PIB, l'emploi, les prix et les comptes externes et publics.",
  "Croissance · chomage · inflation · deficit · dette",
  "Objectifs parfois contradictoires : relance et stabilite des prix",
  "PIB~Production nationale~Croissance~Variation du PIB~Population active~Occupes et chomeurs~Inflation~Hausse des prix~Deficit public~Depenses superieures aux recettes",
  "Mesurer la production et sa variation|Calculer les taux d'emploi et de chomage|Suivre l'indice des prix|Analyser les soldes publics et exterieurs|Arbitrer entre objectifs",
  "Confondre PIB et croissance|Oublier les chomeurs dans la population active|Assimiler hausse d'un prix et inflation|Ne pas distinguer deficit et dette",
  "PIB 1,5 pour cent~Croissance faible~Inflation 5 pour cent~Pouvoir d'achat~Chomage 8 pour cent~Sous-utilisation du travail~Stagflation~Croissance faible et prix hauts~BCE~Objectif 2 pour cent",
  "Deficit~Solde negatif~Dette~Deficits cumules~Excedent~Solde positif~Balance des paiements~Echanges exterieurs~Administrations~Etat et collectivites",
  "Inflation~Hausse generale des prix~Desinflation~Ralentissement de la hausse~Deflation~Baisse des prix~Pouvoir d'achat~Capacite d'achat reelle"))


# ============================================================ B17
add("B17", "Offre, demande et prix de marché", "Économie", ["1re"],
S("Sur un marche, la demande represente les quantites que les acheteurs souhaitent acquerir a chaque prix.|"
  "La loi de la demande indique que la quantite demandee diminue quand le prix augmente, toutes choses egales par ailleurs.|"
  "L'offre represente les quantites que les producteurs souhaitent vendre a chaque prix.|"
  "La loi de l'offre indique que la quantite offerte augmente quand le prix augmente.|"
  "Le prix d'equilibre est le prix pour lequel la quantite offerte egale la quantite demandee.|"
  "La quantite d'equilibre est le volume echange a ce prix.|"
  "Si le prix est superieur a l'equilibre, il apparait un excedent d'offre, ou invendus.|"
  "Si le prix est inferieur, il apparait une penurie, ou excedent de demande.|"
  "Un changement de prix entraine un mouvement le long de la courbe ; un changement des autres facteurs deplace la courbe.|"
  "Le revenu, les gouts et les prix des autres biens font partie des facteurs de la demande.|"
  "Le cout de production, la technologie et le nombre de producteurs font partie des facteurs de l'offre.|"
  "L'elasticite-prix mesure la sensibilite de la quantite demande a une variation de prix."),
[QC("Que dit la loi de la demande ?", "La quantite demandee augmente avec le prix~La quantite demandee diminue quand le prix augmente~Le prix n'influe pas~L'offre et la demande sont identiques", 1,
     "La relation entre prix et quantite demandee est decroissante."),
 QC("Que dit la loi de l'offre ?", "La quantite offerte diminue avec le prix~La quantite offerte augmente avec le prix~L'offre est constante~Le prix n'influe pas", 1,
     "La relation entre prix et quantite offerte est croissante."),
 QC("Quand le marche est-il en equilibre ?", "Quand offre et demande s'egalent~Quand le prix est nul~Quand l'offre est maximale~Quand la demande est nulle", 0,
     "A l'equilibre, quantite offerte et quantite demandee sont egales."),
 QC("Que se passe-t-il si le prix est superieur au prix d'equilibre ?", "Une penurie~Un excedent d'offre~Un equilibre~Une hausse de la demande", 1,
     "Les producteurs proposent plus que ce que les acheteurs veulent prendre."),
 QC("Quel facteur deplace la courbe de demande ?", "Le prix du bien lui-meme~Le revenu des consommateurs~La quantite offerte~Le cout de production", 1,
     "Le prix du bien provoque un mouvement sur la courbe ; le revenu la deplace."),
 QC("Quel facteur deplace la courbe d'offre ?", "Le prix de vente~Le cout de production~Le revenu~Le gout des consommateurs", 1,
     "Une hausse des couts reduit l'offre a chaque prix."),
 QC("Que mesure l'elasticite-prix de la demande ?", "La sensibilite de la quantite demande au prix~Le benefice du producteur~Le nombre de vendeurs~Le prix d'equilibre", 0,
     "Elle compare la variation relative de la quantite a celle du prix."),
 QT("Expliquer comment le prix d'equilibre se forme sur un marche concurrentiel.",
    "A un prix trop eleve, les producteurs offrent davantage que les acheteurs n'en demandent : les invendus les incitent a baisser leur prix. A un prix trop bas, la demande depasse l'offre : les acheteurs se disputent le peu de biens disponibles et sont disposes a payer davantage, ce qui fait monter le prix. Le processus s'arrete au niveau ou les quantites offertes et demandees sont egales. Ce prix d'equilibre est aussi le prix auquel le plus grand nombre de transactions peut avoir lieu. Si les conditions changent, par exemple une hausse du cout des matieres premieres, la courbe d'offre se decale et un nouvel equilibre apparait.",
    "On doit decrire excedent et penurie, le mecanisme d'ajustement et le deplacement des courbes."),
 QT("Distinguer un mouvement le long de la courbe de demande et un deplacement de la courbe.",
    "Une baisse du prix d'un produit entraine une hausse de la quantite demandee : on se deplace le long de la meme courbe de demande, par un simple effet de prix. Si, a prix constant, le revenu des consommateurs augmente et que le bien est normal, la demande augmente : toute la courbe se decale vers la droite. De meme, une mode nouvelle ou une hausse du prix d'un bien substitut deplace la demande. Pour l'offre, une hausse du prix de vente entraine un mouvement sur la courbe, tandis qu'une hausse du cout du travail deplace l'offre vers la gauche. Confondre les deux est une erreur frequente dans l'analyse de marche.",
    "On attend la distinction effet de prix et changement des autres facteurs, avec exemples.")],
C("Le prix d'equilibre concilie offre et demande ; les autres facteurs deplacent les courbes.",
  "Offre = demande au prix d'equilibre",
  "Prix plus haut : excedent d'offre · prix plus bas : penurie",
  "Demande~Quantite souhaitee par les acheteurs~Loi de la demande~Relation decroissante~Offre~Quantite proposee~Equilibre~Offre egale demande~Elasticite~Sensibilite au prix",
  "Lire les axes du graphique|Tracer les courbes d'offre et de demande|Identifier le prix et la quantite d'equilibre|Analyser excedent ou penurie|Prevoir les effets d'un changement de facteur",
  "Confondre mouvement et deplacement de courbe|Oublier la condition toutes choses egales|Lire la quantite sur l'axe des prix|Croire qu'un prix impose est un equilibre",
  "Prix bas~Penurie~Prix haut~Invendus~Revenu~Deplacement de la demande~Cout du travail~Deplacement de l'offre~Elasticite~Fortement sensible",
  "Loi de la demande~Quantite en baisse si prix monte~Loi de l'offre~Quantite en hausse si prix monte~Equilibre~Quantites egales~Desequilibre~Excedent ou penurie",
  "Bien normal~Demande croit avec le revenu~Bien inferieur~Demande baisse avec le revenu~Substitut~Peut remplacer~Complement~Consomme ensemble"))


# ============================================================ B18
add("B18", "Croissance, productivite et developpement", "Économie", ["Terminale"],
S("La croissance economique est l'augmentation durable de la production d'un pays, mesuree par le PIB.|"
  "Elle peut etre extensive, quand elle vient de l'augmentation des facteurs de production, ou intensive, quand elle vient de leur meilleure utilisation.|"
  "Les deux facteurs de production classiques sont le travail et le capital.|"
  "La productivite du travail est le rapport entre la production et le volume de travail utilise.|"
  "La productivite globale des facteurs mesure l'efficacite avec laquelle travail et capital sont combines.|"
  "L'investissement accroit le capital productif et permet d'innover.|"
  "Le capital humain, c'est-a-dire la formation et les competences, contribue a la productivite.|"
  "L'innovation technologique est une source majeure de gains de productivite.|"
  "Une croissance forte ne garantit pas le developpement : elle peut etre inegalement partagee.|"
  "Le developpement est une amelioration durable des conditions de vie, mesuree notamment par l'indice de developpement humain.|"
  "L'IDH combine l'esperance de vie, le niveau d'instruction et le revenu par habitant.|"
  "La question de la soutenabilite rappelle que la croissance doit preserver les ressources et limiter les emissions."),
[QC("Comment mesure-t-on la productivite du travail ?", "PIB divisé par la population~Production divisée par le volume de travail~Salaires divisés par les impots~Investissement divisé par la dette", 1,
     "C'est le rapport entre la production et le travail utilise."),
 QC("Quel facteur augmente le capital productif ?", "La consommation~L'investissement~Le chomage~L'inflation", 1,
     "L'investissement en machines, batiments ou logiciels accroit le capital."),
 QC("Qu'appelle-t-on capital humain ?", "Le nombre de machines~Les competences et la formation~Les stocks de matieres~La monnaie en circulation", 1,
     "Le capital humain correspond aux savoirs et savoir-faire de la population."),
 QC("Quelle croissance provient d'une meilleure combinaison des facteurs ?", "Extensive~Intensive~Nulle~Negative", 1,
     "La croissance intensive vient des gains de productivite."),
 QC("Que combine l'indice de developpement humain ?", "PIB, dette et inflation~Esperance de vie, instruction et revenu~Chomage, prix et salaires~Offre, demande et prix", 1,
     "L'IDH associe sante, education et niveau de vie."),
 QC("Pourquoi une croissance peut-elle ne pas etre un developpement ?", "Parce qu'elle est toujours fausse~Parce que ses gains peuvent etre inegalement repartis~Parce qu'elle supprime les prix~Parce qu'elle interdit l'innovation", 1,
     "Le developpement suppose aussi une amelioration des conditions de vie pour tous."),
 QC("Que vise la soutenabilite ?", "Augmenter les emissions~Preserver les ressources pour les generations futures~Supprimer la croissance~Ignorer l'environnement", 1,
     "La soutenabilite concilie economie, social et environnement."),
 QT("Expliquer la difference entre croissance extensive et croissance intensive.",
    "Une croissance extensive resulte de l'augmentation des quantites de travail et de capital : on embauche plus de salaries ou on construit plus d'usines. Elle se heurte a des limites, car les ressources et la population active ne sont pas extensibles a l'infini. Une croissance intensive resulte de l'augmentation de la productivite : avec le meme nombre de travailleurs et le meme capital, on produit davantage grace a l'innovation, a la formation ou a une meilleure organisation. Dans les economies developpees, la croissance intensive est devenue dominante. Les deux modes peuvent coexister, mais seul le second permet d'augmenter durablement le niveau de vie sans accroitre la pression sur les ressources.",
    "On attend la definition des deux modes, des exemples et la question des limites."),
 QT("Pourquoi le developpement ne se reduit-il pas a la croissance du PIB ?",
    "Le PIB mesure la production, mais il ne dit rien de la repartition des richesses ni de la qualite de vie. Un pays peut avoir un PIB eleve grace a une ressource naturelle exportee alors que la majorite de la population reste pauvre et mal scolarisee. Le PIB ne compte pas non plus les dommages environnementaux ni le travail non paye. C'est pourquoi on utilise l'indice de developpement humain, qui ajoute l'esperance de vie et le niveau d'instruction au revenu. Le developpement est donc un processus pluridimensionnel : il suppose la sante, l'education, l'equite et une croissance soutenable. La croissance est un moyen, pas une fin en soi.",
    "On doit montrer les limites du PIB et presenter l'IDH et la dimension environnementale.")],
C("La croissance augmente la production ; le developpement ameliore durablement les conditions de vie.",
  "Productivite = production / facteur utilise",
  "IDH = sante + education + revenu",
  "Croissance~Hausse du PIB~Extensive~Plus de facteurs~Intensive~Plus de productivite~Productivite~Efficacite~Investissement~Capital accru~IDH~Developpement humain",
  "Mesurer la croissance et la productivite|Identifier les facteurs de production|Evaluer le role de l'innovation|Comparer PIB et indicateurs de developpement|Integrer la dimension environnementale",
  "Confondre croissance et developpement|Oublier le role du capital humain|Ignorer la repartition des richesses|Ne pas tenir compte des limites ecologiques",
  "PIB en hausse~Croissance~Gains de productivite~Innovation~Formation~Capital humain~IDH~Trois dimensions~Soutenabilite~Ressources preservees",
  "Croissance extensive~Plus de travail et de capital~Croissance intensive~Meilleure productivite~Productivite du travail~Production par salarie~Productivite globale~Efficacite combinee",
  "Developpement~Qualite de vie~IDH~Indice composite~Inegalites~Repartition inegale~Soutenabilite~Long terme~Ressources~Limites naturelles"))


# ============================================================ B19
add("B19", "Inflation, chomage et politiques economiques", "Économie", ["Terminale"],
S("L'inflation est une hausse generale et durable du niveau des prix.|"
  "Elle peut provenir d'une demande trop importante par rapport a l'offre, ou d'une hausse des couts de production.|"
  "Les anticipations d'inflation influencent les comportements : si les agents s'attendent a une hausse des prix, ils peuvent l'alimenter.|"
  "L'inflation erode le pouvoir d'achat des revenus fixes et redistribue les richesses entre debiteurs et creanciers.|"
  "Le chomage se distingue en chomage conjoncturel, lie a un ralentissement de l'activite, et chomage structurel, lie a une inadaptation des competences.|"
  "Le chomage frictionnel correspond aux transitions entre emplois et a la recherche d'un premier emploi.|"
  "La politique monetaire agit sur les taux d'interet et la masse monetaire ; en zone euro, elle est menee par la Banque centrale europeenne.|"
  "Une hausse des taux rend le credit plus cher et freine l'investissement et la consommation.|"
  "La politique budgetaire agit par les depenses publiques et les impots.|"
  "Une relance budgetaire peut soutenir la demande et l'emploi, mais elle accroit le deficit.|"
  "Le multiplicateur decrivant l'effet amplifie d'une depense initiale sur l'activite totale.|"
  "Les autorites doivent composer avec le delai d'action des politiques et les conflits entre objectifs."),
[QC("Quelle est une cause d'inflation par les couts ?", "Une hausse du prix du petrole~Une baisse de la demande~Un excedent budgétaire~Une hausse du chomage", 0,
     "La hausse des intrants energies accroit les couts de production."),
 QC("Quel effet a l'inflation sur un revenu fixe ?", "Il augmente en valeur reelle~Il permet d'acheter moins de biens~Il devient imposable~Il disparait", 1,
     "La hausse des prix reduit le pouvoir d'achat d'un revenu nominal fixe."),
 QC("Quel chomage est lie a un ralentissement conjoncturel ?", "Structurel~Conjoncturel~Frictionnel~Volontaire", 1,
     "Le chomage conjoncturel apparait quand la demande d'activite faiblit."),
 QC("Quelle institution mene la politique monetaire dans la zone euro ?", "La BCE~Le Conseil europeen~La Commission~Le FMI", 0,
     "La Banque centrale europeenne fixe les taux directeurs."),
 QC("Que produit une hausse des taux d'interet ?", "Un credit moins cher~Un credit plus cher et une baisse de l'investissement~Une hausse de l'inflation~Une hausse de la masse monetaire", 1,
     "Le cout du credit augmente, ce qui freine la demande."),
 QC("Quel outil appartient a la politique budgetaire ?", "Le taux directeur~Les depenses publiques~La masse monetaire~Le taux de reserve", 1,
     "Le budget de l'Etat utilise recettes fiscales et depenses."),
 QC("Que designe le multiplicateur ?", "Le nombre de chomeurs~L'effet amplifie d'une depense sur l'activite~Le taux d'inflation~La masse monetaire", 1,
     "Une depense initiale entraine des effets en cascade sur le revenu national."),
 QT("Expliquer pourquoi une baisse des taux peut relancer l'activite et pourquoi elle peut aussi alimenter l'inflation.",
    "Quand la banque centrale baisse ses taux directeurs, les taux des prets bancaires diminuent. Les entreprises investissent davantage et les menages consomment a credit, ce qui augmente la demande globale et la production. L'emploi peut s'améliorer. Mais si l'offre ne peut pas suivre cette hausse de demande, les prix montent : l'inflation apparait. De plus, un credit trop bon marche peut financer des actifs immobiliers ou financiers et creer des bulles. La banque centrale doit donc surveiller a la fois l'inflation et la stabilite financiere, et retirer son soutien quand les tensions apareissent.",
    "On doit decrire le canal du credit, l'effet sur la demande, puis le risque inflationniste et financier."),
 QT("Comment articuler politique budgetaire et politique monetaire face a une recession ?",
    "En recession, l'activite et l'emploi baissent. La politique budgetaire peut augmenter les depenses publiques ou reduire les impots pour soutenir la demande : c'est une relance, qui creuse le deficit mais active le multiplicateur. La politique monetaire peut baisser ses taux pour rendre le credit moins cher et accompagner la reprise. Les deux politiques sont complementaires : le budget agit directement sur la demande, la monnaie agit sur le cout du credit et les anticipations. Leurs effets ne sont pas immediats et doivent etre coordonnes. Une fois la reprise engagee, il faut progressivement revenir a une situation plus soutenable pour maitriser la dette et l'inflation.",
    "On attend la complementarite des deux politiques, les instruments, les delais et la sortie de crise.")],
C("Inflation et chomage sont les deux grands desequilibres que les politiques economiques cherchent a maitriser.",
  "Politique monetaire : taux et masse monetaire · politique budgetaire : depenses et impots",
  "Chomage conjoncturel · structurel · frictionnel",
  "Inflation~Hausse durable des prix~Chomage~Sans emploi~Taux directeur~Prix de l'argent~Credit~Pret bancaire~Relance~Hausse de la demande~Multiplicateur~Effet amplifie",
  "Mesurer inflation et chomage|Identifier la cause du desequilibre|Choisir l'instrument adapte|Evaluer les effets et les delais|Coordonner les politiques",
  "Confondre inflation et hausse d'un seul prix|Ignorer le delai d'action des politiques|Croire que la baisse des taux suffit toujours|Oublier le cout de la dette",
  "Prix du petrole~Inflation par les couts~Baisse des taux~Credit moins cher~Relance~Depenses publiques~Multiplicateur~Effet en cascade~BCE~Taux directeurs",
  "Chomage conjoncturel~Manque de demande~Chomage structurel~Competences inadaptees~Chomage frictionnel~Transition entre emplois~Pleins emplois~Emploi disponible",
  "Politique monetaire~Taux et monnaie~Politique budgetaire~Impots et depenses~Anticipations~Attentes des agents~Pouvoir d'achat~Capacite d'achat"))


# ============================================================ B20
add("B20", "Monnaie, banque et financement de l'economie", "Économie", ["Terminale"],
S("La monnaie remplit trois fonctions : unite de compte, intermédiaire des echanges et reserve de valeur.|"
  "La monnaie fiduciaire est constituee des billets et des pieces.|"
  "La monnaie scripturale correspond aux depots bancaires utilisables par virement, carte ou cheque.|"
  "Une grande partie de la masse monetaire est donc creee par les banques lorsqu'elles accordent des credits.|"
  "L'octroi d'un credit genere en meme temps un depot, donc de la monnaie scripturale.|"
  "La banque centrale controle la creation monetaire grace aux taux directeurs et aux reserves obligatoires.|"
  "Les taux directeurs sont les taux auxquels la banque centrale prete ou remunere les banques.|"
  "Le financement direct met en relation emprunteurs et preteurs, par exemple par l'emission d'actions ou d'obligations.|"
  "Le financement indirect passe par un intermediaire, generalement une banque, qui collecte l'epargne et distribue des credits.|"
  "Le taux d'interet represente le prix de l'argent emprunte et influence l'investissement.|"
  "La Banque centrale europeenne veille a la stabilite des prix dans la zone euro.|"
  "Les banques sont egalement soumises a des regles prudentielles et a la lutte contre le blanchiment d'argent."),
[QC("Quelle est une fonction de la monnaie ?", "Unite de compte~Unite de production~Unite de salaire~Unite de TVA", 0,
     "La monnaie sert a mesurer la valeur, a echanger et a conserver du pouvoir d'achat."),
 QC("Qu'appelle-t-on monnaie scripturale ?", "Les billets~Les depots en banque~Les pieces~L'or", 1,
     "Elle circule par virement, carte ou cheque, sans support physique."),
 QC("Comment les banques creent-elles de la monnaie ?", "En imprimant des billets~En accordant des credits~En achetant de l'or~En levant des impots", 1,
     "Le credit accorde genere un depot, donc de la monnaie scripturale."),
 QC("Quel outil de la banque centrale influence directement le cout du credit ?", "Le taux directeur~Le taux de TVA~Le SMIC~La duree legale", 0,
     "En modifiant ses taux, la banque centrale influe sur les taux bancaires."),
 QC("Dans le financement direct, l'intermediaire est ...", "Toujours une banque~Absent ou reduction~L'Etat~La BCE", 1,
     "Les preteurs financent directement les emprunteurs, par exemple via des obligations."),
 QC("Quel est le prix de l'argent emprunte ?", "Le salaire~Le taux d'interet~Le prix de vente~Le SMIC", 1,
     "Le taux d'interet est la remuneration du preteur et le cout pour l'emprunteur."),
 QC("Quel est l'objectif principal de la BCE ?", "La stabilite des prix~Le chomage zero~La croissance maximale~Le deficit zero", 0,
     "La stabilite des prix, avec un objectif d'inflation a 2 pour cent a moyen terme, est prioritaire."),
 QT("Expliquer le mecanisme de creation monetaire par le credit.",
    "Lorsqu'une banque accorde un pret de 10 000 euros a un client, elle credite son compte du meme montant. Elle a cree un depot, donc de la monnaie scripturale, sans imprimer de billets. La banque doit ensuite respecter des regles prudentielles : elle ne peut pas preter sans limite et doit detenir des fonds propres et des liquidites suffisants. La banque centrale influe sur ce processus par ses taux directeurs et ses exigences de reserves. Si les taux augmentent, les credits deviennent plus chers, leur demande diminue et la creation monetaire ralentit. La masse monetaire est donc en grande partie endogene, creee par l'activite bancaire.",
    "On doit decrire credit et depot simultanes, les limites prudentielles et le role de la banque centrale."),
 QT("Comparer financement direct et financement indirect pour une entreprise qui veut investir.",
    "Dans le financement indirect, l'entreprise s'adresse a une banque : celle-ci collecte l'epargne des menages et lui accorde un pret. L'entreprise rembourse avec interets et la banque supporte le risque de defaillance, qu'elle evalue avant l'octroi. Dans le financement direct, l'entreprise emet des obligations ou des actions et trouve des investisseurs, eventuellement via les marches financiers. Elle paie des interets ou distribue des dividendes, et le risque est supporte directement par les investisseurs. Le financement direct peut mobiliser des montants plus importants et diversifier les sources, mais il suppose une information financiere fiable et des marches ouverts. Les deux modes coexistent dans une economie.",
    "On attend la presence ou l'absence d'intermediaire, le risque supporte et des exemples.")],
C("La monnaie sert a echanger et a conserver la valeur ; les banques en creent une grande partie par le credit.",
  "Credit bancaire → depot → monnaie scripturale",
  "Fonctions : unite de compte · intermédiaire · reserve de valeur",
  "Monnaie~Trois fonctions~Fiduciaire~Billets et pieces~Scripturale~Depots bancaires~Credit~Creation de monnaie~Taux directeur~Outil de la BCE~Banque~Intermediaire",
  "Identifier la fonction de la monnaie|Distinguir les formes de monnaie|Expliquer la creation par credit|Comparer les modes de financement|Analyser l'effet des taux",
  "Croire que seule la banque centrale cree de la monnaie|Confondre financement direct et indirect|Oublier les regles prudentielles|Ignorer le role des taux d'interet",
  "Pret 10 000~Depot 10 000~Taux directeur~Credit plus cher~Obligation~Financement direct~Banque~Financement indirect~BCE~Stabilite des prix",
  "Monnaie fiduciaire~Billets et pieces~Monnaie scripturale~Depots et virements~Masse monetaire~Ensemble des moyens de paiement~Credit~Pret bancaire",
  "Financement direct~Sans intermediaire~Financement indirect~Avec intermediaire~Taux d'interet~Prix du credit~Reserve obligatoire~Regle prudentielle~Blanchiment~Origine illicite"))


# FIN DU LOT B
valider_et_ecrire(F, "stmg-mat-part-B.json")
