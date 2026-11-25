# -*- coding: utf-8 -*-
"""Generateur st2s-mat-part-C.json — lot C : droit (6), sante publique (6),
methodologie (4), anglais professionnel de sante (4).

ST2S, lycee technologique. 20 fiches prototype : 12 points, 9 questions
(7 QCM + 2 texte), 7 blocs ordonnes, 3 schemas SVG. Aucune integration.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_etapes,
                      svg_compare, bloc, valider_et_ecrire)

FIL = ["st2s"]
REF = (
    "Programmes ST2S : arrete du 21 juillet 2011 fixant les programmes du baccalaureat technologique "
    "Sciences et technologies de la sante et du social (Bulletin officiel special n 6 du 29 septembre 2011) "
    "et programmes renoves applicables a la rentree 2020 (Bulletin officiel special n 7 du 25 juillet 2019) ; "
    "matieres : Droit et reglementation, Sante publique et environnement, Methodologie et Anglais professionnel "
    "de sante ; ressources eduscol ST2S. Textes officiels cites : Code de la sante publique, loi n 2002-303 "
    "du 4 mars 2002, reglement general sur la protection des donnees (reglement UE 2016/679)."
)

F = []


def S(x):
    return [p.strip() for p in x.split("|") if p.strip()]


def R(x):
    return [p.strip() for p in x.split("~") if p.strip()]


def Q(question, options, correct, correction):
    return qcm(question, R(options), correct, correction)


def T(question, reponse, correction):
    return qt(question, reponse, correction)


def _grid(x):
    cellules = R(x)
    if "|" not in x:
        return [cellules[i:i + 3] for i in range(0, 9, 3)]
    return [R(ligne) for ligne in S(x)]


def _cmp(x):
    cellules = R(x)
    n = len(cellules) // 2
    return (cellules[0], cellules[1:n]), (cellules[n], cellules[n + 1:])


def C(idea, eq, leg, grid, steps, traps, ex, cmp1, cmp2):
    return {"idea": idea, "eq": eq, "leg": leg, "grid": _grid(grid),
            "steps": S(steps), "traps": S(traps), "ex": [R(e) for e in S(ex)],
            "cmp": (_cmp(cmp1), _cmp(cmp2))}


def add(prefix, titre, matiere, annees, points, questions, c):
    titre_complet = prefix + " · " + titre
    short = titre.split(":")[0].strip()
    aff = [
        bloc("L'idee en une phrase", texte=c["idea"], type="intro"),
        bloc("La notion a maitriser", eq=c["eq"], leg=c["leg"], type="formule"),
        bloc("Tableau de lecture", items=c["grid"], type="grille"),
        bloc("Les points essentiels du chapitre", items=points[1:5], type="liste"),
        bloc("La demarche pas a pas", items=c["steps"], type="etapes"),
        bloc("Pieges et erreurs frequentes", items=c["traps"], type="attention"),
        bloc("En situation : exemples concrets", items=[
            "%s : <span class=\"cle\">%s</span>" % (p[0], p[1]) for p in c["ex"]
        ], type="exemples"),
    ]
    schema = [
        diag("1 · " + short, svg_grille(short, ["Notion", "Definition", "Repere"], c["grid"])),
        diag("2 · Demarche", svg_etapes("Procedure : " + short, c["steps"])),
        diag("3 · A distinguer", svg_compare(short, c["cmp"][0], c["cmp"][1])),
    ]
    assert len(points) == 12, prefix
    assert len(questions) == 9, prefix
    assert sum(1 for q in questions if q.get("type") == "qcm") == 7, prefix
    assert sum(1 for q in questions if q.get("type") == "texte") == 2, prefix
    assert len(aff) == 7 and len(schema) == 3, prefix
    F.append(fiche(FIL, annees, matiere, titre_complet, REF, points, questions, aff, schema))


DROIT = "Droit et réglementation"
SANTE = "Santé publique et environnement"
METHO = "Méthodologie"
ANGLAIS = "Anglais professionnel de santé"

# ============================================================ D1
add("ST2S-C-DRO01", "Droit de la sante : sources et principes fondamentaux", DROIT, ["1re", "Terminale"],
S("Le droit de la sante est l'ensemble des regles juridiques applicables a la sante et aux soins."
  "|La Constitution de 1958 garantit le droit a la protection de la sante et la liberte d'acces aux soins."
  "|Le Code de la sante publique regroupe la majorite des textes relatifs a l'organisation sanitaire."
  "|Le Code civil complete les regles de responsabilite et de protection de la personne."
  "|Le principe de laicite et d'egalite s'impose dans les etablissements de soins."
  "|Le droit a la sante est un droit de la personne, opposable dans le cadre des lois en vigueur."
  "|Les lois sont votees par le Parlement et publiees au Journal officiel."
  "|Les decrets d'application preciser les modalites pratiques d'une loi."
  "|Les arretes ministeriels fixent des regles plus detaillees, par exemple les normes d'hygiene."
  "|Le Conseil constitutionnel controle la conformite des lois a la Constitution."
  "|Le juge administratif ou judiciaire tranche les litiges selon la nature du conflit."
  "|La reglementation sante evoluant, une veille juridique reguliere est necessaire."),
[Q("Quel texte regroupe l'essentiel des regles relatives a l'organisation sanitaire ?", "Le Code civil~Le Code de la sante publique~Le Code du travail~Le Code penal", 1,
    "Le Code de la sante publique est la source principale du droit sanitaire francais."),
 Q("Qui vote la loi en France ?", "Le president seul~Le Parlement~Le Conseil d'Etat~Les tribunaux", 1,
    "La loi est votee par l'Assemblee nationale et le Senat, puis promulguee."),
 Q("Quel texte precise les modalites d'application d'une loi ?", "Un decret~Une circulaire~Un arrete municipal~Un avis", 0,
    "Le decret d'application fixe les conditions concretes de mise en oeuvre de la loi."),
 Q("Quelle institution controle la constitutionnalite des lois ?", "La Cour des comptes~Le Conseil constitutionnel~Le tribunal administratif~La Cour de cassation", 1,
    "Le Conseil constitutionnel verifie la conformite des lois a la Constitution."),
 Q("Quel principe s'impose dans un etablissement de soins public ?", "La laicite et l'egalite~La priorite de naissance~Le choix du medecin traitant seul~L'absence de reglement", 0,
    "Le service public de sante est laique et doit garantir l'egalite des usagers."),
 Q("Quel juge traite un litige entre un patient et un hopital public ?", "Le juge administratif~Le juge commercial~Le juge penal~Le juge electorale", 0,
    "Les litiges impliquant un service public relevent de la juridiction administrative."),
 Q("Pourquoi faire une veille juridique en sante ?", "Pour connaitre les prix~Parce que la reglementation evolue~Pour changer de metier~Pour eviter les soins", 1,
    "Les textes et recommandations évoluent : il faut s'informer regulierement."),
 T("Classer les sources du droit de la sante de la plus generale a la plus precise.",
    "A la base se trouvent la Constitution et les principes generaux, puis les lois votees par le Parlement, comme la loi du 4 mars 2002 sur les droits des patients. Viennent ensuite les decrets d'application, qui precisent les modalites, puis les arretes ministeriels, par exemple pour les normes d'hygiene ou les qualifications professionnelles. Les circulaires et recommandations de bonnes pratiques constituent un niveau d'orientation, sans avoir la meme force juridique que la loi. Un professionnel doit savoir quel niveau de texte consulte pour une question donnee.",
    "On attend la hierarchie Constitution, loi, decret, arrete, puis recommandations."),
 T("Expliquer pourquoi le droit de la sante est a la fois un droit individuel et un enjeu collectif.",
    "Individuellement, chaque personne a droit a la protection de sa sante, au respect de sa dignite, a l'information et au consentement pour les soins. Collectivement, l'organisation sanitaire doit garantir l'egalite d'acces, la securite des soins, la veille sanitaire et la prevention des risques pour la population. Les deux dimensions se rejoignent : une mesure comme la vaccination protege la personne vaccinee et contribue a l'immunite collective. Le droit de la sante organise donc des droits pour chacun et des obligations pour les pouvoirs publics et les professionnels.",
    "On attend la distinction individu/collectif et un exemple comme la vaccination.")],
C("Le droit de la sante organise les droits des personnes et les obligations des professionnels dans un cadre juridique evolutif.",
  "Constitution -> loi -> decret -> arrete",
  "Code de la sante publique ·egalite · laicite · veille juridique",
  "Constitution~Texte fondateur~Loi~Votee par le Parlement~Decret~Application de la loi~Code de la sante publique~Source principale",
  "Identifier la question juridique|Trouver la source competente|Verifier le texte en vigueur|Appliquer la regle au cas|Signaler un doute a l'equipe",
  "Confondre loi et decret|Oublier que les textes evoluent|Ignorer le Code de la sante publique|Croire qu'une recommandation est une loi",
  "Loi du 4 mars 2002~Droits du patient~CSP~Code de la sante publique~Decret~Modalites pratiques~Veille~Mise a jour reguliere",
  "Droit individuel~Protection de la personne~Droit collectif~Organisation sanitaire",
  "Loi~Votee par le Parlement~Decret~Pris pour son application"))

# ============================================================ D2
add("ST2S-C-DRO02", "Droits du patient et relation soignant-soigne", DROIT, ["1re", "Terminale"],
S("La loi du 4 mars 2002 a renforce les droits des usagers du systeme de sante."
  "|Le consentement libre et eclaire est requis pour tout acte medical, sauf urgence ou incapacite."
  "|Une personne apte peut refuser un soin, apres avoir ete correctement informee."
  "|L'information doit etre claire, loyale et adaptee au niveau de comprehension de la personne."
  "|Le droit a l'information porte sur la maladie, les examens, les traitements et leurs risques."
  "|La personne de confiance, designee par ecrit, peut accompagner les demarches et etre consultee."
  "|Les directives anticipees permettent d'exprimer a l'avance ses souhaits pour la fin de vie."
  "|Le respect de la dignite et de l'intimite s'impose pendant les soins et les examens."
  "|L'acces au dossier medical est garanti a la personne, directement ou par un mediateur."
  "|Les commissions des usagers et les mediateurs medicalegaux facilitent le dialogue en cas de litige."
  "|Un soignant ne doit jamais imposer un acte non consenti, hors situation d'urgence."
  "|La relation de soin repose sur la confiance, l'information et le respect des choix de la personne."),
[Q("Quelle loi a renforce les droits des patients en 2002 ?", "La loi du 9 decembre 1905~La loi du 4 mars 2002~La loi du 11 juillet 1978~La loi du 26 janvier 2016", 1,
    "La loi n 2002-303 du 4 mars 2002 est relative aux droits des malades et a la qualite du systeme de sante."),
 Q("Qu'est-ce qu'un consentement eclaire ?", "Un accord donne sans information~Un accord apres information claire et adaptee~Un silence~Une obligation legale automatique", 1,
    "Le consentement est eclaire lorsque la personne a recu une information intelligible."),
 Q("Une personne apte peut-elle refuser un soin ?", "Non, jamais~Oui, apres information et si sa decision est libre~Oui, sans information~Seulement si elle est mineure", 1,
    "Le refus est un droit, des lors que la personne est informee et apte a decider."),
 Q("Quel est le role de la personne de confiance ?", "Remplacer le medecin~Accompagner et etre consultee~Signer les ordonnances~Payer les soins", 1,
    "La personne de confiance soutient le patient et peut etre consultee si celuici ne peut s'exprimer."),
 Q("Que permettent les directives anticipees ?", "Choisir son medecin~Exprimer a l'avance ses souhaits de fin de vie~Refuser toute hospitalisation~Modifier le dossier", 1,
    "Elles consignent les decisions anticipees relatives a la fin de vie."),
 Q("Qui peut aider en cas de conflit entre un patient et un etablissement ?", "Le mediateur medicalegal~Le voisin~Le comptable~Le fournisseur", 0,
    "Le mediateur medicalegal et la commission des usagers facilitent la resolution des conflits."),
 Q("Quel principe s'applique a l'information donnee au patient ?", "Elle doit etre complexe~Elle doit etre claire, loyale et adaptee~Elle est facultative~Elle est donnee uniquement a la famille", 1,
    "L'information doit etre compréhensible, sincere et adaptee a la personne."),
 T("Comment un soignant obtient-il un consentement libre et eclaire avant un soin ?",
    "Il explique le but de l'acte, son deroulement, les benefices attendus, les risques et les alternatives, avec des mots comprehensibles. Il verifie que la personne a bien compris, par exemple en lui demandant de reformuler. Il laisse un temps de reflexion et s'assure qu'aucune pression ne s'exerce. Il recueille ensuite l'accord, qui peut etre verbal pour un soin courant et ecrit pour certains actes. Si la personne refuse, il respecte cette decision et la trace dans le dossier, sauf urgence vitale.",
    "On attend information adaptee, verification de la comprehension, absence de pression et traçabilité."),
 T("Distinguer personne de confiance et directives anticipees par leur fonction.",
    "La personne de confiance est une personne physique designee par ecrit, choisie pour accompagner le patient dans ses demarches et etre consultee si celuici ne peut plus exprimer sa volonte. Les directives anticipees sont un document ecrit dans lequel une personne exprime a l'avance ses decisions concernant sa fin de vie, notamment sur les traitements. La premiere represente une personne et un accompagnement ; les secondes sont des instructions. Les deux sont des outils de respect de l'autonomie, maisils ne se substituent pas au consentement de la personne tant qu'elle peut s'exprimer.",
    "On attend la distinction personne / document et le lien avec l'autonomie.")],
C("Le consentement libre et eclaire est au coeur de la relation soignant-soigne, complete par l'information et les droits d'accompagnement.",
  "Information claire + comprehension + accord libre = consentement eclaire",
  "Loi du 4 mars 2002 · personne de confiance · directives anticipees · mediateur",
  "Consentement~Accord libre et eclaire~Information~Claire et adaptee~Personne de confiance~Accompagnement~Directives anticipees~Souhaits de fin de vie",
  "Expliquer le soin|Verifier la comprehension|Laisser un delai de reflexion|Recueillir l'accord|Tracer la decision",
  "Imposer un soin non consenti|Donner une information trop technique|Confondre personne de confiance et directives|Negliger le refus exprime",
  "Acte medical~Consentement requis~Refus~Decision a respecter~Dossier medical~Acces garanti~Mediateur~Reglement des conflits",
  "Consentement~Accord apres information~Consentement impose~Sans valeur juridique",
  "Personne de confiance~Accompagne~Directives anticipees~Ecrivent des souhaits"))

# ============================================================ D3
add("ST2S-C-DRO03", "Secret professionnel et protection des donnees de sante", DROIT, ["Terminale"],
S("Les informations de sante sont among les donnees personnelles les plus sensibles."
  "|Le secret professionnel impose aux professionnels de sante la confidentialite des informations recueillies."
  "|Le secret est une obligation legale generale, prevue notamment par le Code penal et le Code de la sante publique."
  "|Le secret professionnel est partage : les professionnels qui cooperent a la prise en charge peuvent echanger."
  "|Le partage doit rester limite aux informations necessaires et aux professionnels concernes."
  "|La personne doit etre informee du partage et peut s'y opposer dans les cas prevus."
  "|Le reglement general sur la protection des donnees, ou RGPD, encadre le traitement des donnees personnelles."
  "|Les principes du RGPD comprennent la minimisation, l'exactitude, la limitation de la conservation et la securite."
  "|La base legale d'un traitement de donnees de sante doit etre identifiee avant sa mise en oeuvre."
  "|Les droits de la personne incluent l'acces, la rectification, l'effacement dans certains cas et l'opposition."
  "|Une violation de donnees doit etre signalee a l'autorite de controle dans les delais reglementaires."
  "|Les mots de passe, le verrouillage des postes et la traçabilité des acces sont des mesures de securite concretes."),
[Q("Quel principe impose la confidentialite des informations de sante ?", "La liberte d'expression~Le secret professionnel~La publicite des soins~La transparence totale", 1,
    "Le secret professionnel est une obligation legale pour les professionnels de sante."),
 Q("Que signifie secret professionnel partage ?", "Toutes les informations sont publiques~Echange entre professionnels cooperant a la prise en charge~Partage avec le voisinage~Absence de secret", 1,
    "Le secret partage autorise un echange limite et necessaire entre professionnels du soin."),
 Q("Quel reglement europeen encadre les donnees personnelles ?", "Le RGPD~Le code de la route~La PAC~Le reglement sanitaire international", 0,
    "Le reglement UE 2016/679, dit RGPD, protege les donnees personnelles."),
 Q("Quel principe du RGPD limite les donnees collectees ?", "La minimisation~La maximisation~La publicite~L'archivage indefini", 0,
    "La minimisation impose de ne collecter que les donnees necessaires a la finalite poursuivie."),
 Q("Quel droit permet a une personne de corriger une donnee inexacte ?", "L'effacement~La rectification~L'opposition~La portabilite seule", 1,
    "La rectification permet de corriger des donnees personnelles inexactes."),
 Q("Quelle situation doit etre signalee comme violation de donnees ?", "Un mot de passe oublie~Un acces non autorise a des donnees~Une simple question d'un patient~Une reunion d'equipe", 1,
    "Toute atteinte a la confidentialite, a l'integrite ou a la disponibilite des donnees doit etre signalee."),
 Q("Quelle mesure de securite est elementary sur un poste de soin ?", "Laisser la session ouverte~Verrouiller le poste~Partager son mot de passe~Ecrire le mot de passe sur un post-it", 1,
    "Le verrouillage et un mot de passe personnel protegent les donnees accessibles."),
 T("Distinguer secret professionnel et secret partage dans une equipe de soin.",
    "Le secret professionnel interdit a chaque professionnel de divulguer les informations confiees dans l'exercice de son metier. Le secret partage est une exception organisee : les professionnels qui participent a la meme prise en charge peuvent echanger les informations utiles a cette prise en charge. Cet echange reste limite aux personnes concernees, aux donnees necessaires et au cadre du soin. La personne doit en etre informee et peut s'y opposer. Les deux notions ne s'opposent donc pas : le secret partage est une modalite controlee du secret, pas sa suppression.",
    "On attend la definition des deux notions, les limites du partage et l'information de la personne."),
 T("Comment appliquer concretement la minimisation des donnees dans un dossier de suivi ?",
    "Avant de saisir une information, le soignant se demande si elle est utile a la prise en charge ou a la traçabilité du soin. Il note les faits objectifs et les decisions, en evitant les commentaires personnels, les rumeurs familiales ou les donnees sans lien avec la sante. Il n'enregistre pas de donnee superflue, par exemple le détail de la vie privee du voisinage. Il verrouille le poste apres chaque saisie et consulte uniquement les dossiers des personnes dont il s'occupe. Enfin, il respecte les durees de conservation definies par l'etablissement.",
    "On attend le lien avec la finalite, l'absence de commentaires personnels et les mesures d'acces.")],
C("Les donnees de sante sont confidentielles : le secret s'impose, le partage reste limite et encadre.",
  "Secret professionnel + secret partage + RGPD = protection des donnees",
  "Minimisation · exactitude · securite · acces et rectification pour la personne",
  "Secret professionnel~Confidentialite legale~Secret partage~Echange limite entre soignants~RGPD~Protection des donnees~Minimisation~Donnees necessaires seulement",
  "Verifier la finalite de la collecte|Ne saisir que les donnees utiles|Limiter les acces aux professionnels concernes|Verrouiller le poste|Signaler toute violation",
  "Partager un dossier avec un non-soignant|Laisser une session ouverte|Noter des commentaires personnels|Conserver les donnees indefiniment",
  "Dossier medical~Donnees sensibles~Verrouillage~Securite~Rectification~Droit de la personne~Violation~Signalement obligatoire",
  "Secret professionnel~Obligation generale~Secret partage~Exception encadree",
  "RGPD~Reglement europeen~Loi informatique et libertes~Droit national"))

# ============================================================ D4
add("ST2S-C-DRO04", "Responsabilite professionnelle, faute et dommage", DROIT, ["Terminale"],
S("La responsabilite professionnelle engage un soignant lorsqu'il commet une faute causant un dommage."
  "|Une faute peut etre une erreur, une negligence, une imprudence ou un manquement a une obligation."
  "|Le dommage est un prejudice subi par la personne : atteinte physique, morale ou financiere."
  "|Un lien de causalite doit exister entre la faute et le dommage pour engage la responsabilite."
  "|La responsabilite contractuelle decoule du contrat de soin entre le patient et l'etablissement ou le professionnel."
  "|La responsabilite delictuelle s'applique en dehors de tout contrat, sur le fondement du droit commun."
  "|En milieu hospitalier, l'etablissement est souvent responsable des fautes commises par son personnel."
  "|La faute professionnelle peut aussi etre conscientieuse : elle se distingue de l'intention de nuire."
  "|Un professionnel peut etre poursuivi sur le plan disciplinaire par son ordre ou son employeur."
  "|Les sanctions disciplinaires vont de l'avertissement a l'interdiction d'exercer."
  "|La competence, la formation continue et le respect des procedures reduisent le risque de faute."
  "|La declaration d'un evenement indesirable permet d'analyser la cause et d'ameliorer la securite des soins."),
[Q("Quels elements sont necessaires pour engager une responsabilite ?", "Une faute, un dommage et un lien de causalite~Un simple doute~Une rumeur~Une prescription non executee", 0,
    "La responsabilite suppose une faute, un dommage et un lien de causalite entre eux."),
 Q("Quel est un exemple de faute par negligence ?", "Oublier de verifier l'identite d'un patient~Appliquer un protocole~Demander un avis medical~Tracer un soin", 0, 
    "L'oubli d'une verification constitue une negligence professionnelle."),
 Q("Quelle responsabilite decoule du contrat de soin ?", "La responsabilite contractuelle~La responsabilite penale~La responsabilite electorale~La responsabilite fiscale", 0,
    "Le contrat de soin fonde la responsabilite contractuelle."),
 Q("Qui est souvent responsable d'une faute commise par un agent hospitalier ?", "Le voisin~L'etablissement de sante~Le fournisseur~La famille", 1,
    "L'etablissement engage sa responsabilite pour les fautes de son personnel dans le service."),
 Q("Quelle sanction disciplinaire est la plus legeres ?", "L'interdiction d'exercer~La radiation~L'avertissement~La prison", 2,
    "L'avertissement est la sanction disciplinaire la plus legeres."),
 Q("Que permet la declaration d'un evenement indesirable ?", "Punir automatiquement~Analyser la cause etame liorer la securite~Effacer le dossier~Eviter toute formation", 1,
    "La declaration alimente une analyse des causes et une demarche d'amelioration continue."),
 Q("Quel moyen reduit le risque de faute professionnelle ?", "Travailler sans procedure~La formation continue et le respect des protocoles~Ignorer les alertes~Ne pas tracer les soins", 1,
    "Competence, procedures et traçabilite sont des leviers de prevention de la faute."),
 T("Analyse une situation : une erreur d'identification entraine un examen sur la mauvaise personne. Quels elements de responsabilite sont reunis ?",
    "La faute consiste dans le defaut de verification de l'identite, alors que les procedures l'imposent. Le dommage est l'examen subi inutilement par la personne, avec son lot de stress et d'inconfort, et eventuellement un retard de prise en charge pour la bonne personne. Le lien de causalite est direct : sans l'erreur de verification, l'examen n'aurait pas ete realise sur cette personne. L'etablissement peut engager sa responsabilite, et le soignant peut etre convoque dans une procedure disciplinaire. L'evenement doit etre declare et analyse pour corriger le Circuit d'identification.",
    "On attend faute, dommage, lien de causalite et suite organisationnelle."),
 T("Distinguer faute professionnelle et intention de nuire, et expliquer l'interet de la declaration.",
    "La faute professionnelle est le plus souvent involontaire : une erreur d'attitude, un oubli de protocole ou une meconnaissance. L'intention de nuire suppose une volonte de causer un dommage, ce qui est exceptionnel et releve alors aussi du penal. La declaration d'un evenement indesirable ne vise pas d'abord a punir : elle permet de comprendre pourquoi la barriere de securite a cede, par exemple une procedure peu claire ou une surcharge de travail, puis de mettre en place des mesures correctives. Cette culture de la securite protege mieux les patients que la seule recherche d'un coupable.",
    "On attend la distinction volontaire/involontaire et la finalite apprentissage de la declaration.")],
C("La responsabilite repose sur une faute, un dommage et un lien de causalite ; la prevention passe par les procedures et la declaration.",
  "Faute + dommage + lien de causalite = responsabilite",
  "Contractuelle / delictuelle · faute involontaire · evenement indesirable",
  "Faute~Manquement a une obligation~Dommage~Prejudice subi~Lien de causalite~Relation faute-dommage~Responsabilite~Obligation de reparer",
  "Identifier la faute|Evaluer le dommage|Verifier le lien de causalite|Declarer l'evenement|Analyser et corriger le circuit",
  "Confondre faute et intention de nuire|Oublier de declarer|Chercher un coupable sans analyser le systeme|Negliger la traçabilité",
  "Erreur d'identite~Faute~Examen inutile~Dommage~Declaration~Analyse des causes~Procedure~Barriere de securite",
  "Responsabilite contractuelle~Issue du contrat de soin~Responsabilite delictuelle~Droit commun",
  "Faute involontaire~Erreur ou negligence~Intention de nuire~Volonte de causer un dommage"))

# ============================================================ D5
add("ST2S-C-DRO05", "Protection sociale et assurance maladie", DROIT, ["1re", "Terminale"],
S("La protection sociale est un ensemble de mecanismes qui protegent les personnes contre les risques de la vie."
  "|Elle couvre la maladie, la maternite, l'invalidite, la vieillesse, la famille et le chomage."
  "|Le systeme francais repose sur le principe de solidarite nationale et la repartition."
  "|L'assurance maladie est financée par les cotisations sociales et les contributions, dont la CSG."
  "|Le regime general concerne la majorite de la population active et leurs ayants droit."
  "|Des regimes particuliers existent pour certains métiers, comme les agriculteurs ou les marins."
  "|Le remboursement des soins depend d'une base de remboursement et d'un taux, par exemple 70 % pour un consultation generaliste."
  "|Le ticket modérateur est la part laissee a la charge de l'assure apres remboursement."
  "|La complementaire sante, obligatoire depuis 2016 dans les entreprises, prend en charge tout ou partie du reste a charge."
  "|La Carte Vitale permet la transmission electronique des actes et le remboursement."
  "|Le tiers payant evite l'avance de frais chez certains professionnels ou en cas d'exemption."
  "|L'aide medicale de l'Etat et la complementaire sante universelle facilitent l'acces aux soins des personnes precaires."),
[Q("Quel principe fonde la protection sociale francaise ?", "La capitalisation individuelle~La solidarite nationale~Le benefice uniquement prive~Le hasard", 1,
    "La protection sociale repose sur la mutualisation et la solidarite entre assurés."),
 Q("Quel risque n'est pas couvert par la protection sociale ?", "La maladie~La vieillesse~Le chomage~Le choix d'une couleur de voiture", 3,
    "Les grands risques couverts sont maladie, maternite, invalidite, vieillesse, famille et chomage."),
 Q("Que finance principalement l'assurance maladie ?", "Les seuls medicaments~Les depenses de soins remboursables~Les seuls salaires~Les transports scolaires", 1,
    "Elle prend en charge une partie des depenses medicales selon des regles definies."),
 Q("Quel est le ticket modérateur ?", "La part rembourse par l'Assurance maladie~La part restant a la charge de l'assure~Le salaire du medecin~Le prix d'une consultation", 1,
    "C'est la fraction non remboursee par l'assurance maladie obligatoire."),
 Q("Depuis quelle annee la complementaire sante est-elle obligatoire en entreprise ?", "2000~2010~2016~2022", 2,
    "La generalisation de la complementaire sante d'entreprise date de 2016."),
 Q("Que permet la Carte Vitale ?", "Payer directement le medecin~Transmettre les actes et obtenir le remboursement~Prescrire des medicaments~Remplacer l'ordonnance", 1,
    "Elle identifie l'assure et permet la teletransmission des feuilles de soins."),
 Q("Que designe le tiers payant ?", "Un remboursement supplementaire~Une dispense d'avance de frais~Une augmentation du ticket modérateur~Un impot sur les soins", 1,
    "Le tiers payant supprime l'avance de frais pour la part prise en charge."),
 T("Expliquer le parcours d'un remboursement de consultation medicale.",
    "Le patient presente sa Carte Vitale au professionnel de sante. Celui-ci teletransmet une feuille de soins contenant les actes et les montants a l'assurance maladie. Celle-ci calcule la base de remboursement et applique le taux, puis verse la part obligatoire directement sur le compte du patient ou du tiers payant si celuici est applique. La complementaire sante intervient ensuite pour le reste a charge selon son contrat. Le patient peut consulter le detail des remboursements sur son compte en ligne. La traçabilité de la feuille de soins est essentielle.",
    "On attend Carte Vitale, teletransmission, base et taux, part complementaire, consultation du compte."),
 T("Montrer comment la protection sociale concilie solidarite et maitrise des depenses.",
    "La solidarite se manifeste par la mutualisation : les cotisations de tous financent les soins de chacun, et des dispositifs comme l'aide medicale de l'Etat ou la complementaire sante universelle protegent les personnes les plus precaires. La maitrise des depenses passe par le controle des prescriptions, le developpement du tiers payant et de la telemedecine, la promotion du bon usage du medicament et la prevention. Un systeme trop generateur de gaspillage menace sa propre viabilite : la prevention et le bon usage sont donc des outils de solidarite durable, autant que des economies.",
    "On attend mutualisation, dispositifs pour les precaires, maitrise des depenses et prevention.")],
C("L'assurance maladie mutualise les risques et rembourse les soins selondes regles de base et de taux.",
  "Remboursement = base x taux ; reste a charge = prix - remboursements",
  "Solidarite · CSG · ticket modérateur · tiers payant · complementaire sante",
  "Assurance maladie~Remboursement des soins~Ticket modérateur~Part non rembourse~Carte Vitale~Identifiant~Tiers payant~Pas d'avance de frais",
  "Presenter sa Carte Vitale|Verifier la teletransmission|Calculer base et taux|Identifier le reste a charge|Orienter vers la complementaire",
  "Confondre base de remboursement et prix paye|Oublier le ticket modérateur|Croire que tout est rembourse|Negliger la complementaire",
  "Consultation~70 % du tarif~Ticket modérateur~30 % a la charge~Complementaire~Reste a charge~Tiers payant~Pas d'avance",
  "Assurance maladie obligatoire~Regime de base~Complementaire sante~Couverture supplementaire",
  "Solidarite~Mutualisation des risques~Capitalisation~Epargne individuelle"))

# ============================================================ D6
add("ST2S-C-DRO06", "Etablissements de sante, ARS et droits des usagers", DROIT, ["Terminale"],
S("Les etablissements de sante sont organizes pour repondre aux besoins de soins de la population."
  "|On distingue les etablissements publics, prives a but non lucratif et prives a but lucratif."
  "|Les hopitaux publics sont des etablissements publics de sante, geres par un conseil de surveillance et un directoire."
  "|Les agences regionales de sante, ou ARS, pilotent la politique de sante dans chaque region."
  "|L'ARS delivre les autorisations d'activite et controle la qualite et la securite des soins."
  "|La haute Autorite de sante produit des recommandations de bonne pratique et évalue les etablissements."
  "|La certification des etablissements verifie la qualite des processus et la securite des patients."
  "|Chaque etablissement dispose d'une commission des usagers, ou CDU, qui represente les patients et les proches."
  "|Le mediateur medicalegal intervient pour faciliter le reglement amiable des litiges."
  "|Le livre d'or et les enquetes de satisfaction recueillent l'avis des usagers."
  "|Les droits des usagers comprennent l'information, le consentement, l'acces au dossier et le respect de la dignite."
  "|Le parcours de soins coordonne le secteur hospitalier, la ville et le secteur medical social."),
[Q("Quel etablissement est gere par un conseil de surveillance et un directoire ?", "Une clinique privee~Un hopital public~Un cabinet liberal~Une pharmacie", 1,
    "L'hopital public est un etablissement public de sante dirige par un directoire sous le controle d'un conseil de surveillance."),
 Q("Quel est le role principal d'une ARS ?", "Vendre des medicaments~Piloter la sante dans la region et controler les etablissements~Remplacer les medecins~Fixer les salaires", 1,
    "L'agence regionale de sante autorise les activites et veille a la qualite des soins."),
 Q("Quelle institution produit des recommandations de bonne pratique ?", "La HAS~L'ARS~Le Conseil d'Etat~L'INSEE", 0,
    "La Haute Autorite de sante elabore des recommandations et certifie les etablissements."),
 Q("Que verifie la certification d'un etablissement ?", "Les seuls prix~La qualite des processus et la securite des patients~Le nombre de lits~La couleur des locaux", 1,
    "La certification evalue l'organisation et la qualite des soins, pas la rentabilite."),
 Q("Quel est le role de la commission des usagers ?", "Representer les patients et les proches~Diriger l'hopital~Prescrire les soins~Facturer les actes", 0,
    "La CDU est l'instance de representation et de dialogue avec les usagers."),
 Q("Qui facilite le reglement amiable d'un litige ?", "Le mediateur medicalegal~Le comptable~Le chirurgien seul~Le fournisseur", 0,
    "Le mediateur medicalegal intervient a la demande du patient ou de l'etablissement."),
 Q("Quel droit n'appartient pas aux usagers ?", "L'information~L'acces au dossier~Le respect de la dignite~Le choix du prix des soins", 3,
    "Les tarifs sont reglementes : le patient n'a pas le droit d'en fixer le prix."),
 T("Distinguer le role de l'ARS et celui de la Haute Autorite de sante.",
    "L'ARS est une autorite administrative regionale : elle pilote la politique de sante, delivre les autorisations d'activite, controle les etablissements et veille a l'acces aux soins dans son territoire. La Haute Autorite de sante est une autorite publique independante qui produit des recommandations de bonne pratique, évalue les medicaments et les dispositifs et certifie les etablissements de sante. L'ARS est donc un operateur regional de regulation et de controle, alors que la HAS est un producteur de references scientifiques et d'evaluation de la qualite.",
    "On attend la distinction territoire/autorisation versus recommandations/certification."),
 T("Comment un etablissement peut-il associer les usagers a l'amelioration de la qualite ?",
    "Il organise une commission des usagers ou les representants des patients et des proches portent les attentes de la population. Il affiche les droits des usagers et les voies de recours, notamment le mediateur medicalegal. Il recueille les plaintes et reclamations, les analyse avec les indicateurs de qualite et met en place des actions correctrices, par exemple l'amélioration de l'information ou de l'accueil. Il peut utiliser le livre d'or et les enquetes de satisfaction pour mesurer le ressenti. La certification evalue ensuite la capacite de l'etablissement a s'ameliorer continument.",
    "On attend CDU, mediateur, analyse des reclamations, actions correctrices et certification.")],
C("L'organisation sanitaire associe des autorites de regulation, des etablissements et des instances de representation des usagers.",
  "ARS : autorisations et controle · HAS : recommandations et certification",
  "CDU : representation · mediateur : litiges · droits : information, consentement, dignite",
  "ARS~Autorite regionale de sante~HAS~Haute Autorite de sante~CDU~Commission des usagers~Certification~Evaluation de la qualite",
  "Identifier l'acteur institutionnel|Determiner son role|Repérer le droit de l'usager|Orienter vers la bonne instance|Suivre les actions d'amelioration",
  "Confondre ARS et HAS|Ignorer la CDU|Croire que la certification juge les prix|Oublier le role du mediateur",
  "Hopital public~Etablissement public de sante~ARS~Pilotage regional~Mediateur~Reglement amiable~CDU~Voix des usagers",
  "ARS~Regulation territoriale~HAS~References scientifiques",
  "Etablissement public~Gestion publique~Clinique privee~Gestion privee"))

# ============================================================ P1
add("ST2S-C-SAN01", "Determinants de la sante et inegalites sociales", SANTE, ["1re", "Terminale"],
S("La sante d'une population depend de facteurs multiples qui interagissent tout au long de la vie."
  "|Les determinants de la sante sont les conditions dans lesquelles les personnes vivent, travaillent et vieillissent."
  "|Les determinants individuels comprennent l'age, le sexe, le patrimoine genetique et les comportements."
  "|Les determinants environnementaux portent sur le logement, l'eau, l'air, le bruit et les risques professionnels."
  "|Les determinants sociaux incluent le revenu, l'education, l'emploi, les liens sociaux et l'acces aux soins."
  "|Le gradient social de sante montre un meilleur etat de sante lorsque le statut socio-economique s'eleve."
  "|Les inegalites de sante sont des ecarts systematiques et evitables entre groupes de population."
  "|L'esperance de vie et la mortalite infantile different sensiblement selon les territoires et les categories sociales."
  "|Les comportements de sante, tabac, alcool, alimentation et activite physique, sont influences par le milieu social."
  "|La prevention universelle s'adresse a tous, tandis que la prevention ciblee vise les groupes les plus exposes."
  "|Une approche de type Health in All Policies integre la sante dans les decisions d'urbanisme, de transport et de logement."
  "|Agir sur les determinants exige une cooperation entre secteurs et une evaluation des politiques menees."),
[Q("Que designent les determinants sociaux de la sante ?", "Des facteurs genetiques only~Les conditions de vie et de travail~Des examens medicalux~Des medicaments", 1,
    "Les determinants sociaux sont les conditions dans lesquelles les personnes vivent et travaillent."),
 Q("Quel est un exemple de determinant environnemental ?", "Le revenu~La qualite de l'air~L'age~Le groupe sanguin", 1,
    "L'air, l'eau, le logement et le bruit sont des determinants environnementaux."),
 Q("Que montre le gradient social de sante ?", "Une sante identique pour tous~Une sante qui s'ameliore avec le statut social~Une sante liee au seul age~Une sante qui ne depend de rien", 1,
    "Chaque niveau socio-economique superieur s'accompagne en moyenne d'un meilleur etat de sante."),
 Q("Quappelle-t-on une inegalite de sante ?", "Un ecart aleatoire~Un ecart systematique et evitable~Une difference genetique inévitable~Un simple choix individuel", 1,
    "Les inegalites de sante sont systematiques, evitables et socialement determinees."),
 Q("Quel indicateur est sensible aux inegalites territoriales ?", "La couleur du drapeau~La mortalite infantile~Le nombre de pharmacies~La temperature", 1,
    "La mortalite infantile varie fortement selon les territoires et les conditions de vie."),
 Q("Quelle est une prevention ciblee ?", "Une campagne pour toute la population~Une action pour un groupe expose~Un depistage obligatoire~Une intervention sans evaluation", 1,
    "La prevention ciblee s'adresse a un groupe presentant un risque accru."),
 Q("Que signifie integrer la sante dans toutes les politiques ?", "Ne s'occuper que des hopitaux~Considerer la sante dans l'urbanisme et les transports~Supprimer la prevention~Laisser les choix au hasard", 1,
    "Les decisions d'amenagement ont des effets sanitaires et doivent etre evaluees comme telles."),
 T("Expliquer pourquoi l'education influence l'etat de sante tout au long de la vie.",
    "Un niveau d'education eleve facilite la comprehension des informations de sante, l'acces a un emploi de qualite et un revenu plus stable. Il favorise aussi des competences d'autonomie : lire une notice, comprendre une ordonnance, naviguer dans le systeme de soins et adopter des comportements protecteurs. Ces avantages s'accumulent des la petite enfance jusqu'a la vieillesse. A l'inverse, un faible niveau d'education est associe a des expositions professionnelles plus risquees et a un moindre recours a la prevention. L'education est donc un determinant social majeur, pas une simple variable individuelle.",
    "On attend comprehension, emploi, revenu, autonomie et accumulation des avantages."),
 T("Proposer une action locale pour reduire une inegalite de sante et expliquer son evaluation.",
    "Dans un quartier ou la mortalite infantile est elevee, on peut mettre en place un programme de suivi de grossesse et de vaccination rapproche du domicile, associe a des mediateurs de sante et a des actions sur le logement et l'alimentation. L'action est evaluee avec des indicateurs : taux de couverture vaccinale, nombre de consultations prenatales, evolution de la mortalite infantile et satisfaction des familles. On compare ces indicateurs avant et apres l'action, et avec des quartiers similaires non concernes. Cette evaluation permet de savoir si l'action réduit réellement l'ecart observe.",
    "On attend une action concrete, des indicateurs et une methode de comparaison.")],
C("La sante se construit dans des conditions de vie et de travail ; les ecarts observes sont evitables et mesurables.",
  "Determinants individuels + sociaux + environnementaux = etat de sante",
  "Gradient social · inegalites evitables · prevention universelle ou ciblee",
  "Determinant social~Revenu, education, emploi~Gradient social~Sante selon le statut~Inegalite~Ecart systematique~Prevention ciblee~Action pour un groupe",
  "Identifier les determinants en presence|Mesurer les ecarts entre groupes|Analyser les causes sociales|Choisir une action adaptee|Evaluer avec des indicateurs",
  "Réduire la sante aux comportements individuels|Ignorer le territoire|Confondre prevention universelle et ciblee|Ne pas evaluer l'action",
  "Quartier~Territoire inegal~Mortalite infantile~Indicateur~Mediateur de sante~Action locale~Couverture vaccinale~Indicateur de suivi",
  "Prevention universelle~Pour tous~Prevention ciblee~Pour un groupe expose",
  "Determinant environnemental~Air, eau, logement~Determinant social~Revenu et education"))

# ============================================================ P2
add("ST2S-C-SAN02", "Prevention, depistage et promotion de la sante", SANTE, ["1re", "Terminale"],
S("La prevention vise a eviter l'apparition ou l'aggravation d'une maladie."
  "|La prevention primaire agit avant la maladie : information, vaccination, hygiene et reduction des risques."
  "|La prevention secondaire intervient a un stade precoce, souvent par le depistage."
  "|La prevention tertiaire limite les consequences d'une maladie et favorise la reeducation et l'autonomie."
  "|La promotion de la sante donne aux personnes les moyens de prendre soin d'elles et de leur environnement."
  "|La charte d'Ottawa define la promotion de la sante comme un processus de creation de conditions favorables."
  "|Le depistage recherche une maladie chez une personne asymptomatique, grace a un test ou un examen."
  "|Un bon test de depistage possede une sensibilite et une specificite satisfaisantes."
  "|La valeur predictive positive depend de la prevalence de la maladie dans la population depistee."
  "|Un resultat positif n'est pas un diagnostic : il doit etre confirme par des examens complementaires."
  "|Les programmes de depistage organisés concernent notamment le cancer du sein et le cancer colorectal."
  "|Une action de prevention est evaluee sur son impact, son cout et son acceptabilite par la population."),
[Q("A quel niveau appartient la vaccination ?", "Prevention primaire~Prevention secondaire~Prevention tertiaire~Diagnostic", 0,
    "La vaccination agit avant la maladie : c'est de la prevention primaire."),
 Q("Quel est l'objectif de la prevention secondaire ?", "Eviter tout contact avec le risque~Detectar la maladie a un stade precoce~Limiter les sequelles~Remplacer le traitement", 1,
    "La prevention secondaire repose sur le depistage et le diagnostic precoce."),
 Q("Que vise la prevention tertiaire ?", "Vacciner la population~Limiter les consequences et maintenir l'autonomie~Faire un depistage~Interdire les soins", 1,
    "Elle intervient apres la maladie pour reduire les sequelles et la dependance."),
 Q("Que recherche un depistage ?", "Une maladie chez une personne asymptomatique~Un traitement~Une allergie seulement~Une fracture", 0,
    "Le depistage s'adresse a des personnes sans symptomes apparents."),
 Q("Quelle est la sensibilite d'un test ?", "Sa capacite a etre accepte~Sa capacite a etre positif chez les personnes malades~Son cout~Sa duree", 1,
    "La sensibilite est la probabilite que le test soit positif chez une personne atteinte."),
 Q("La valeur predictive positive depend notamment de ...", "La couleur du test~La prevalence de la maladie~L'heure de l'examen~Du nom du laboratoire", 1,
    "Plus la maladie est rare, plus un test positif a de chances d'etre un faux positif."),
 Q("Que represente la charte d'Ottawa ?", "Un texte sur la promotion de la sante~Une loi sur les hopitaux~Un protocole de vaccination~Un reglement europeen", 0,
    "La charte d'Ottawa (1986) fonde la promotion de la sante moderne."),
 T("Distinguer prevention primaire, secondaire et tertiaire avec des exemples lies au tabac.",
    "La prevention primaire vise a eviter le contact avec le tabac : campagnes d'information, interdiction de fumer dans les lieux publics, augmentation du prix et accompagnement des jeunes. La prevention secondaire consiste a depister precocement les consequences, par exemple par une consultation pour une toux persistante ou un examen de la fonction respiratoire chez un fumeur. La prevention tertiaire intervient apres la maladie : sevrage tabagique, reeducation respiratoire et suivi d'une bronchopneumopathie chronique obstructive pour maintenir l'autonomie. Les trois niveaux se succedent dans le temps mais sont complémentaires.",
    "On attend les trois niveaux, des exemples precis et la notion de complementarite."),
 T("Expliquer pourquoi un test de depistage positif doit etre confirme avant toute annonce de diagnostic.",
    "Un test de depistage n'est pas parfait : il peut donner des faux positifs, surtout quand la maladie est peu frequente dans la population. Sa valeur predictive positive combine sensibilite, specificite et prevalence. Le resultat positif indique une probabilite, pas une certitude. Une confirmation par un examen plus specifique, une consultation medicale ou une biopsie est necessaire avant d'annoncer un diagnostic, afin d'eviter des inquietudes injustifiees et des traitements inutiles. Le depistage est une etape du parcours, pas son terme.",
    "On attend faux positifs, prevalence, confirmation et consequence pour la personne.")],
C("La prevention agit a trois niveaux ; le depistage est un outil de detection, pas un diagnostic.",
  "Primaire : eviter · secondaire : depister · tertiaire : limiter les sequelles",
  "Sensibilite / specificite / prevalence · confirmation necessaire",
  "Prevention primaire~Avant la maladie~Depistage~Recherche chez l'asymptomatique~Sensibilite~Test positif chez un malade~Prevalence~Frequence de la maladie",
  "Identifier le niveau de prevention|Choisir l'action adaptee|Evaluer la qualite du test|Interpreter le resultat|Confirmer avant diagnostic",
  "Confondre depistage et diagnostic|Ignorer la prevalence|Croire qu'un test positif suffit|Oublier la prevention tertiaire",
  "Vaccination~Primaire~Mammographie~Secondaire~Sevrage tabagique~Tertiaire~Faux positif~Limite du test",
  "Prevention~Agir avant la maladie~Promotion de la sante~Creer des conditions favorables",
  "Sensibilite~Detecte les malades~Specificite~Epargne les non-malades"))

# ============================================================ P3
add("ST2S-C-SAN03", "Maladies infectieuses, veille sanitaire et notification", SANTE, ["1re", "Terminale"],
S("Une maladie infectieuse est causee par un agent pathogene transmis d'une personne ou d'un animal a une autre."
  "|Les agents sont les bacteries, les virus, les champignons et les parasites."
  "|Une epidemic correspond a une augmentation inhabituelle du nombre de cas dans une population."
  "|Une pandemie est une epidemie touchant plusieurs continents ou le monde entier."
  "|Le taux d'incidence compte les nouveaux cas sur une periode donnee et une population donnee."
  "|La prevalence compte l'ensemble des cas, anciens et nouveaux, a un instant donne."
  "|La veille sanitaire collecte et analyse en continu les donnees de sante pour detecter les alertes."
  "|Santé publique France est l'agence qui assure la veille et l'alerte en France."
  "|Certaines maladies sont a declaration obligatoire : le medecin doit les signaler aux autorites."
  "|La notification permet de suivre l'evolution, d'identifier les contacts et de mettre en oeuvre des mesures de controle."
  "|Le reglement sanitaire international organise la cooperation entre pays face aux risques de propagation."
  "|La vaccination, l'hygiene, l'isolement et le traitement des contacts sont les leviers de maitrise d'une epidemie."),
[Q("Quel agent est responsable d'une maladie virale ?", "Une bacterie~Un virus~Un champignon~Un parasite", 1,
    "Les virus sont des agents infectieux non cellulaires, comme ceux de la grippe ou de la rougeole."),
 Q("Que designe une epidemic ?", "Une maladie permanente~Une augmentation inhabituelle de cas dans une population~Une maladie hereditaire~Une absence de cas", 1,
    "Une epidemie est une hausse anormale du nombre de cas dans le temps et l'espace."),
 Q("Quelle est la difference entre incidence et prevalence ?", "L'incidence compte les deces~L'incidence compte les nouveaux cas, la prevalence tous les cas~Elles sont identiques~La prevalence compte les nouveaux cas", 1,
    "L'incidence mesure les nouveaux cas sur une periode ; la prevalence mesure tous les cas a un instant."),
 Q("Quelle agence assure la veille sanitaire en France ?", "La HAS~Sante publique France~L'ARS~L'INSEE", 1,
    "Sante publique France collecte les donnees, detecte les alertes et communique sur les risques."),
 Q("Que permet la notification d'une maladie a declaration obligatoire ?", "Fermer les hopitaux~Suivre l'evolution et organiser les mesures de controle~Augmenter les prix~Supprimer les donnees", 1,
    "La notification alimente la veille et permet une reponse rapide et coordonnee."),
 Q("Quel texte international coordonne la lutte contre les epidemies entre pays ?", "Le RGPD~Le reglement sanitaire international~Le Code civil~La charte d'Ottawa", 1,
    "Le reglement sanitaire international de l'OMS definit les obligations de surveillance et de notification."),
 Q("Quel moyen ne contribue pas a maitriser une epidemie ?", "La vaccination~L'hygiene~L'identification des contacts~L'absence de surveillance", 3,
    "Sans surveillance, on ne peut pas detecter ni suivre la propagation."),
 T("Distinguer incidence et prevalence avec un exemple chiffre simple.",
    "Dans une ville de 10 000 habitants, si 50 personnes contractent la grippe au cours d'un mois, l'incidence mensuelle est de 50 pour 10 000, soit 0,5 %. Si, un jour donne, 80 personnes sont malades, dont certaines depuis plusieurs semaines, la prevalence a cette date est de 80 pour 10 000, soit 0,8 %. L'incidence mesure un flux de nouveaux cas sur une periode, alors que la prevalence mesure un stock de cas a un instant. Les deux indicateurs repondent a des questions differentes : vitesse de propagation et charge de maladie dans la population.",
    "On attend une definition de flux et de stock et un calcul correct."),
 T("Expliquer le parcours d'une alerte sanitaire depuis la detection jusqu'a la reponse.",
    "Un signal est detecte, par exemple une augmentation inhabituelle de consultations pour une maladie. Les donnees sont verifiees et analysées par la veille sanitaire, qui estime l'ampleur et la gravite de la situation. Une alerte est alors declenchee et les autorites informent les professionnels et le public. Les mesures de controle sont mises en oeuvre : notification, isolement des cas, vaccination, hygiene renforcée et suivi des contacts. L'evolution est surveillée en continu pour adapter les mesures. Une fois la situation maitrisee, un bilan est etabli pour ameliorer les procedures.",
    "On attend signal, verification, alerte, mesures, suivi et bilan.")],
C("La veille sanitaire detecte les alertes et la notification permet une reponse coordonnee aux epidemies.",
  "Incidence = nouveaux cas / population / periode ; prevalence = cas totaux / population",
  "Veille · notification · isolement · vaccination · cooperation internationale",
  "Incidence~Nouveaux cas~Prevalence~Tous les cas~Epidemic~Hausse inhabituelle~Veille~Surveillance continue",
  "Detecter un signal|Verifier les donnees|Calculer les indicateurs|Declencher l'alerte|Mettre en oeuvre et suivre les mesures",
  "Confondre incidence et prevalence|Attendre trop longtemps pour notifier|Ignorer les contacts|Oublier le bilan final",
  "10 000 habitants~Population~50 cas/month~Incidence de 0,5 %~80 cas~Prevalence de 0,8 %~Alerte~Reponse coordonnee",
  "Epidemic~Portee locale ou nationale~Pandemie~Portee mondiale",
  "Notification~Signalement obligatoire~Veille~Collecte permanente"))

# ============================================================ P4
add("ST2S-C-SAN04", "Environnement et sante : air, eau, bruit et logement", SANTE, ["1re", "Terminale"],
S("L'environnement est un determinant majeur de la sante des populations."
  "|La qualite de l'air depend des emissions industrielles, des transports, du chauffage et de la pollenisation."
  "|Les particules fines penetrent profondement dans les voies respiratoires et augmentent les risques cardiovasculaires, tandis que le dioxyde d'azote et l'ozone sont des polluants gazeux surveilles par les reseaux de mesure."
  "|La qualite de l'eau potable est controlee par des normes microbiologiques et chimiques."
  "|Une eau contaminee peut transmettre des maladies infectieuses comme le cholera ou la gastro-enterite."
  "|Le bruit excessif provoque des troubles du sommeil, du stress et une reduction de l'audition."
  "|L'exposition au bruit est mesuree en decibels et porte sur la duree comme sur l'intensite."
  "|Un logement insalubre favorise les allergies, les infections respiratoires et les accidents domestiques."
  "|L'humidite et les moisissures aggravent l'asthme et les maladies respiratoires."
  "|Le principe de precaution justifie des mesures meme lorsque les donnces scientifiques sont encore incompletes."
  "|Les plans regionaux de la qualite de l'air et les campagnes de depistage du saturnisme illustrent l'action publique."
  "|L'evaluation des risques environnementaux associe mesure, expertise et communication au public."),
[Q("Quel polluant penetre profondement dans les voies respiratoires ?", "Le pollen~Les particules fines~Le dioxygene~L'azote", 1,
    "Les particules fines de petit diametre atteignent les alveoles et la circulation sanguine."),
 Q("Que controle-t-on pour garantir l'eau potable ?", "La couleur du robinet~Des normes microbiologiques et chimiques~Le prix~Le niveau de la riviere", 1,
    "Des analyses microbiolologiques et chimiques verifient la conformite de l'eau distribuee."),
 Q("Quel effet du bruit est bien documente ?", "Une augmentation de l'audition~Des troubles du sommeil~Une baisse de la glycemie~Une amelioration de la memoire", 1,
    "Le bruit perturbe le sommeil, augmente le stress et peut alterer l'audition."),
 Q("Quelle unite mesure le niveau sonore ?", "Le joule~Le decibel~Le gramme~Le volt", 1,
    "Le decibel est l'unite de niveau sonore, avec une echelle logarithmique."),
 Q("Que favorise un logement humide avec moisissures ?", "Une bonne qualite de l'air~L'asthme et les maladies respiratoires~Une baisse des allergies~Une meilleure audition", 1,
    "L'humidite et les moisissures aggravent les troubles respiratoires et les allergies."),
 Q("Quel principe justifie des mesures face a un risque incertain ?", "Le principe de precaution~Le principe de liberte totale~Le principe d'attente~Le principe de stabilite", 0,
    "Le principe de precaution permet d'agir face a un risque grave meme si les preuves sont incompletes."),
 Q("Quel dispositif illustre une action contre un risque environnemental ?", "Le depistage du saturnisme~La vaccination contre la grippe~Le depistage du cancer du sein~Le tiers payant", 0,
    "Le depistage du saturnisme vise a detecter une exposition au plomb, notamment dans le logement."),
 T("Expliquer pourquoi les particules fines ont un impact sanitaire plus grave que les grosses particules.",
    "Les grosses particules sont arretees par les poils du nez et les muqueuses des voies superieures. Les particules fines, de diametre tres reduit, traversent ces barrieres, atteignent les alveoles et peuvent passer dans le sang. Elles provoquent une inflammation locale, aggravent l'asthme et augmentent le risque de maladies cardiovasculaires. Leur petite taille explique leur penetration profonde et leur persistance dans l'organisme. C'est pourquoi les normes de qualite de l'air portent particulierement sur les fractions fines.",
    "On attend le lien taille, penetration, alveoles et effets respiratoires et cardiovasculaires."),
 T("Comment articuler mesure, expertise et communication dans la gestion d'un risque environnemental ?",
    "La mesure fournit des donnees sur les niveaux de polluants et les expositions reelles de la population. L'expertise interprte ces donnees, estime les risques sanitaires et propose des valeurs de reference ou des mesures de reduction. La communication informe la population et les professionnels avec des messages clairs, honestes sur les incertitudes, par exemple en cas de pic de pollution. Les trois etapes sont liees : sans mesure, pas d'expertise fiable ; sans expertise, pas de message utile ; sans communication, les recommandations ne sont pas appliquees.",
    "On attend les trois etapes et leur articulation, avec un exemple concret.")],
C("L'environnement agit sur la sante par des expositions mesurables ; la precaution permet d'agir malgre l'incertitude.",
  "Exposition + toxicite + vulnerabilite = risque environnemental",
  "Air : particules fines · eau : normes · bruit : decibels · logement : insalubrite",
  "Particule fine~Polluant respiratoire~Eau potable~Normes de qualite~Bruit~Niveau en decibels~Precaution~Agir malgre l'incertitude",
  "Identifier le polluant et la source|Mesurer l'exposition|Comparer aux normes|Evaluer les populations exposes|Communiquer les mesures",
  "Confondre risque et danger|Ignorer la duree d'exposition|Mélanger decibel et joule|Attendre une certitude absolue pour agir",
  "Pic de pollution~Mesure~Eau contaminee~Gastro-enterite~Logement humide~Asthme~Saturnisme~Exposition au plomb",
  "Danger~Potentiel de nuire~Risque~Probabilite de dommage",
  "Precaution~Action malgre l'incertitude~Prevention~Reduction effective du risque"))

# ============================================================ P5
add("ST2S-C-SAN05", "Alimentation, activite physique et promotion de la sante", SANTE, ["1re"],
S("L'alimentation et l'activite physique sont deux leviers majeurs de la promotion de la sante."
  "|Les recommandations nutritionnelles portent sur la diversite, la qualite des graisses, les sucres et le sel."
  "|Les besoins energetiques varient avec l'age, le sexe, l'activite et l'etat physiologique."
  "|Un apport excessif de sucres libres et de sel favorise l'obesite, le diabete et l'hypertension."
  "|Les fibres, fruits et legumes contribuent a un transit regulier et a la satiete."
  "|L'activite physique reguliere renforce le coeur, les muscles, les os et la capacite cardiorespiratoire."
  "|L'OMS recommande aux adultes au moins 150 minutes d'activite moderee par semaine."
  "|La sedentarite est un facteur de risque independant de maladies chroniques et de mortalite."
  "|L'indice de masse corporelle, ou IMC, est le rapport de la masse en kg sur la taille au carre en metres ; c'est un indicateur de population qui ne distingue pas muscle et graisse chez un individu."
  "|Le Programme national nutrition sante, ou PNNS, diffuse des repères alimentaires pour la population."
  "|Une approche de promotion de la sante agit aussi sur l'environnement : cantines, bornes deau, parcours sportifs."
  "|L'evaluation d'une action nutritionnelle porte sur les comportements, les indicateurs biologiques et la participation."),
[Q("Que recommande l'OMS aux adultes en activite physique ?", "30 minutes par an~Au moins 150 minutes par semaine~Une heure par mois~Aucune recommandation", 1,
    "L'OMS recommande au moins 150 minutes d'activite d'intensite moderee par semaine chez l'adulte."),
 Q("Comment calculer l'IMC ?", "Masse / taille~Masse / taille au carre~Taille / masse~Masse × taille", 1,
    "L'IMC se calcule en kg divisés par la taille en metres au carre."),
 Q("Quel effet d'un apport excessif en sel ?", "Une baisse de la pression~Une augmentation du risque d'hypertension~Une meilleure digestion~Une baisse du diabete", 1,
    "Une consommation elevee de sel est associee a l'hypertension arterielle."),
 Q("Quel role des fibres alimentaires ?", "Favoriser la satiete et le transit~Augmenter le cholesterol~Remplacer les proteines~Supprimer l'eau", 0,
    "Les fibres ameliorent le transit et contribuent a la satiete."),
 Q("Quel est un effet benefique de l'activite physique reguliere ?", "Renforcer le coeur et les os~Diminuer la masse osseuse~Augmenter la sedentarite~Remplacer l'alimentation", 0,
    "L'activite physique entretient le systeme cardiovasculaire, musculaire et osseux."),
 Q("Que designe le PNNS ?", "Un medicament~Un programme national de nutrition sante~Un impot~Un laboratoire", 1,
    "Le Programme national nutrition sante diffuse les recommandations alimentaires officielles."),
 Q("Quelle limite de l'IMC chez un individu ?", "Il ne peut pas etre calcule~Il ne distingue pas muscle et graisse~Il depend du groupe sanguin~Il est toujours faux", 1,
    "L'IMC est un indicateur utile en population mais imprécis pour un individu musculeux ou age."),
 T("Calculer l'IMC d'une personne de 70 kg mesurant 1,75 m et interpreter le resultat.",
    "L'IMC vaut 70 / (1,75 × 1,75), soit environ 70 / 3,0625 = 22,9 kg/m2. Cette valeur se situe dans la plage habituellement considerée comme normale chez l'adulte, generalement entre 18,5 et 25. Il faut toutefois rappeler que l'IMC ne refle pas la composition corporelle : une personne tres musculeuse peut avoir un IMC eleve sans exces de graisse, et une personne agee peut avoir un IMC normal avec une masse musculaire faible. L'interpretation doit donc etre completee par d'autres donnees et par un avis medical.",
    "On attend le calcul, l'interpretation et la limite de l'indicateur."),
 T("Montrer qu'une action de promotion de la sante ne se limite pas au conseil individuel.",
    "Dire a une personne de manger des fruits et de bouger est utile mais insuffisant si son environnement ne le permet pas. La promotion de la sante agit aussi sur les conditions : menus equilibres a la cantine, acceso a des points d'eau, amenagement de pistes cyclables, preserved des temps de repas et formation des personnels. Elle associe les collectivites, les etablissements, les associations et les professionnels de sante. L'evaluation porte sur les comportements observés, les indicateurs comme l'IMC ou la tension, et la participation de la population. Cette approche collective rend les choix sains plus faciles et plus durables.",
    "On attend le passage de l'individu a l'environnement et des exemples d'action collective.")],
C("Manger equilibre et bouger regulierement est plus efficace quand l'environnement rend ces choix accessibles.",
  "IMC = masse (kg) / taille (m)^2 ; activite : au moins 150 min/semaine",
  "PNNS · fibres · sel et sucres · sedentarite · promotion collective",
  "IMC~Indice de masse corporelle~PNNS~Programme nutrition sante~Fibres~Satiete et transit~Activite~150 minutes par semaine",
  "Estimer les besoins et les apports|Calculer les indicateurs|Observer les comportements|Agir sur l'environnement|Evaluer les resultats",
  "Confondre IMC et masse musculaire|Oublier le sel et les sucres|Se limiter au conseil individuel|Ignorer la sedentarite",
  "70 kg et 1,75 m~IMC 22,9~150 minutes~Recommandation OMS~Cantine~Action collective~Piste cyclable~Environnement favorable",
  "Alimentation~Apport energetique~Activite physique~Depense energetique",
  "Promotion de la sante~Agir sur les conditions~Conseil individuel~Agir sur la personne"))

# ============================================================ P6
add("ST2S-C-SAN06", "Risques sanitaires, alertes et gestion de crise", SANTE, ["Terminale"],
S("Un risque sanitaire est la probabilite qu'un danger entraine un dommage pour la sante."
  "|Le danger est la source potentielle : agent infectieux, produit chimique, catastrophe ou defaut d'organisation."
  "|L'exposition designe le contact entre la personne et le danger, avec une intensite et une duree."
  "|La vulnerabilite depend de l'age, des maladies, de la grossesse et des conditions sociales."
  "|Le risque combine le danger, l'exposition et la vulnerabilite de la population."
  "|L'analyse de risque comprend l'identification du danger, l'evaluation de l'exposition et la caracterisation du risque."
  "|La gestion de crise suit les phases de preparation, de reponse, de recuperation et de retour d'experience."
  "|Le principe de precaution s'applique quand le risque est grave mais les donnees encore incertaines."
  "|Les plans d'urgence, comme le plan ORSEC ou les plans blancs hospitaliers, organisent les moyens et les responsabilites."
  "|L'alerte doit etre rapide, fiable et adressee aux bons acteurs pour eviter la desinformation."
  "|La communication de crise est claire, transparente sur les incertitudes et repetitive au besoin."
  "|Le retour d'experience analyse ce qui a fonctionne et ce qui doit etre corrige apres la crise."),
[Q("Quels elements composent un risque sanitaire ?", "Le danger seul~Danger, exposition et vulnerabilite~La seule vulnerabilite~Le seul hasard", 1,
    "Le risque depend du danger, du contact avec ce danger et de la sensibilite de la population."),
 Q("Quel facteur de vulnerabilite est cite ?", "L'age et la grossesse~La couleur des vetements~Le groupe sanguin~Le lieu de naissance seul", 0,
    "Les personnes agees, les nourrissons, les femmes enceintes et les malades chroniques sont plus vulnerables."),
 Q("Que fait-on dans la phase de preparation d'une crise ?", "Attendre l'evenement~Former les equipes et preparer les plans~Supprimer les procedures~Communiquer apres coup", 1,
    "La preparation anticipe les moyens, les roles et les formations avant l'evenement."),
 Q("Que designe un plan blanc hospitalier ?", "Un plan de recrutement~Un plan d'organisation en situation exceptionnelle~Un plan de conge~Un plan tarifaire", 1,
    "Le plan blanc organise la mobilisation des moyens hospitaliers en cas d'afflux ou de crise."),
 Q("Quelle qualite doit avoir une alerte sanitaire ?", "Lente et imprecise~Rapide, fiable et ciblee~Amusante~Reservee au seul directeur", 1,
    "Une alerte utile est emise tot, verifiee et transmise aux acteurs concernes."),
 Q("Que vise le retour d'experience ?", "Punir les erreurs~Comprendre les reussites et les dysfonctionnements pour s'ameliorer~Clore le dossier~Recommencer sans changement", 1,
    "Le retour d'experience est une analyse collective visant a ameliorer la preparation et la reponse."),
 Q("Quand s'applique le principe de precaution ?", "Quand le risque est certain et faible~Quand le risque est grave mais les donnees incertaines~Jamais~Uniquement pour les medicaments", 1,
    "La precaution permet d'agir face a un risque grave malgre l'incertitude scientifique."),
 T("Analyser un risque de vague de chaleur dans un etablissement accueillant des personnes agees.",
    "Le danger est la temperature extreme. L'exposition depend de la duree de la vague, de l'isolation du batiment et de l'absence de climatisation. La vulnerabilite est forte : les personnes agees ressentent moins la soif, ont une regulation thermique moins efficace et souffrent souvent de maladies chroniques. Le risque combine ces trois elements. Les mesures comprennent la surveillance de la temperature, l'hydratation programmee, l'adaptation des horaires d'activite, la formation des equipes et un plan de crise avec des procedural d'alerte. Un retour d'experience apres l'episode permet d'ajuster le plan.",
    "On attend danger, exposition, vulnerabilite, mesures et retour d'experience."),
 T("Expliquer pourquoi la communication en situation de crise doit etre a la fois rapide et transparente.",
    "Une communication tardive laisse le champ libre aux rumeurs et retarde les comportements protecteurs. Elle doit donc etre rapide, meme si toutes les donnees ne sont pas encore disponibles. La transparence sur ce qui est su et ce qui reste incertain maintain la confiance : dire « nous ne savons pas encore, nous surveillons et nous vous informerons » est plus credibile qu'une affirmation rassurante non étayee. Les messages sont clairs, repetables, adaptees au public et coordonnes entre autorites et professionnels. Une bonne communication est elle-meme une mesure de sante publique.",
    "On attend rapidite, transparence sur les incertitudes, coordination et effet sur les comportements.")],
C("La gestion d'un risque sanitaire articule l'analyse du danger, de l'exposition et de la vulnerabilite a un cycle de crise.",
  "Risque = danger × exposition × vulnerabilite",
  "Preparation · reponse · recuperation · retour d'experience",
  "Danger~Source potentielle de dommage~Exposition~Contact avec le danger~Vulnerabilite~Sensibilite de la personne~Plan blanc~Organisation hospitaliere de crise",
  "Identifier le danger|Estimer l'exposition|Repérer les populations vulnerables|Activer le plan adapte|Communiquer et faire un retour d'experience",
  "Confondre danger et risque|Minimiser la vulnerabilite|Communiquer trop tard|Omettre le retour d'experience",
  "Vague de chaleur~Danger~Personnes agees~Vulnerabilite~Hydratation~Mesure~Plan blanc~Organisation de crise",
  "Danger~Ce qui peut nuire~Risque~Probabilite de dommage",
  "Precaution~Agir malgre l'incertitude~Certitude~Donnees etablies"))

# ============================================================ M1
add("ST2S-C-MET01", "Recherche documentaire et veille informationnelle", METHO, ["1re", "Terminale"],
S("Une recherche documentaire efficace commence par une analyse precise de la question posee."
  "|On identifie les mots-cles et les synonymes avant d'interroger une base de donnees."
  "|Les opérateurs logiques ET, OU et NON permettent d'affiner ou d'elargir une recherche."
  "|Les guillemets forcent la recherche d'une expression exacte."
  "|Le choix des sources depend de leur fiabilite : organismes officiels, revues scientifiques, ouvrages de reference."
  "|Les sites institutionnels comme ceux du Ministere, de l'OMS ou de la HAS sont des sources de qualite."
  "|Un wikipedia peut servir de premiere approche mais ne doit pas etre la seule source d'un travail."
  "|La date de publication est essentielle pour les sujets de sante, ou les recommandations evoluent."
  "|La methode CRAAP evalue la source selon le credit, la pertinence, l'auteur, la precision et l'objectif."
  "|Les resultats doivent etre verifies par croisement entre plusieurs sources independantes."
  "|Une veille informationnelle consistee a surveiller regulierement des sources choisies pour rester a jour."
  "|Toute information utilisee doit etre citee avec son auteur, son titre, sa date et son adresse."),
[Q("Que faut-il faire avant d'interroger une base ?", "Choisir un moteur au hasard~Identifier les mots-cles et synonymes~Copier le premier resultat~Attendre une idee", 1,
    "La formulation de la question et des mots-cles determine la qualite des resultats."),
 Q("Que permet l'operateur OU dans une recherche ?", "Reduire les resultats~Elargir avec des synonymes~Supprimer un mot~Trier par date", 1,
    "OU ajoute des termes equivalents et elargit donc la recherche."),
 Q("Quelle source est la plus fiable pour une recommandation de sante ?", "Un forum~Le site de la HAS ou du Ministere~Un blog personnel~Une publicite", 1,
    "Les sites institutionnels et les publications scientifiques sont des sources de qualite."),
 Q("Que controle la methode CRAAP ?", "Le prix d'un livre~La credibilite et la pertinence de la source~La longueur d'un article~La couleur du site", 1,
    "CRAAP evalue Credit, Relevance, Authority, Accuracy et Purpose."),
 Q("Pourquoi verifier la date d'une source medicale ?", "Parce que les recommandations evoluent~Parce que les dates sont jolies~Parce que c'est obligatoire pour les images~Sans raison", 0,
    "En sante, les protocoles et les donnees changent : une source ancienne peut etre obsolete."),
 Q("Qu'est-ce qu'une veille informationnelle ?", "Une lecture unique~Une surveillance reguliere de sources choisies~Une copie de texte~Un simple favori", 1,
    "La veille est un processus repetitif et organise de collecte d'informations."),
 Q("Que doit contenir une citation bibliographique ?", "Seulement le titre~Auteur, titre, date et adresse~Seulement l'URL~Le nom du moteur", 1,
    "Une reference complete permet de retrouver et verifier la source."),
 T("Construire une stratégie de recherche sur la prevention du cancer du col de l'uterus.",
    "On analysela question : prevention, cancer, col, uterus, papillomavirus, vaccination, depistage. On identifie les synonymes : HPV, frottis, test HPV. On interroge une base avec une requete du type prevention AND cancer AND col AND uterus, puis on ajoute les termes par OU pour elargir. On filtre sur la date recente et on privilege les sites de l'OMS, de la HAS, de Sante publique France et du Ministere. On croise les informations entre au moins deux sources officielles et on note les references completes avec auteur, titre, date et URL.",
    "On attend mots-cles, operateurs, sources fiables, date, croisement et citation."),
 T("Expliquer pourquoi croiser plusieurs sources est indispensable en sante.",
    "Une source unique peut comporter une erreur, un biais ou une recommandation obsolete. Le croisement permet de verifier qu'un chiffre ou une recommandation est confirmé par plusieurs organismes independants. Il faut toutefois eviter de croiser des sites qui copient le meme texte : ce n'est pas une verification independante. La qualite de la source compte plus que le nombre de resultats. En cas de divergence, on compare les dates, les populations etudiees et les methodes, puis on privilégie les recommandations officielles recentes.",
    "On attend verification, independance reelle, qualite et gestion des divergences.")],
C("Une recherche fiable part d'une question analysee, d'operateurs adaptes et de sources critiques et datees.",
  "Mots-cles + operateurs + sources qualitatives + croisement",
  "ET : intersection · OU : union · NON : exclusion · CRAAP : evaluation de la source",
  "Mot-cle~Terme de recherche~Operateur ET~Intersection des resultats~Source officielle~Organisme de reference~Veille~Surveillance reguliere",
  "Analyser la question|Choisir les mots-cles|Construire la requete|Evaluer les sources|Croiser et citer",
  "Se fier au premier resultat|Utiliser une source non datee|Copier sans citer|Confondre popularite et fiabilite",
  "Prevention du cancer~Sujet~HPV~Mot-cle~HAS~Source officielle~Reference complete~Citation",
  "Recherche ponctuelle~Une seule fois~Veille~Dans la duree",
  "Source primaire~Texte original~Source secondaire~Commentaire ou synthese"))

# ============================================================ M2
add("ST2S-C-MET02", "Raisonnement logique et resolution de probleme", METHO, ["1re"],
S("Un raisonnement logique enchaine des propositions dont la verite est evaluable."
  "|Une proposition est un énoncé qui peut etre vrai ou faux, mais pas les deux a la fois."
  "|La negation d'une proposition inverse sa valeur de verite."
  "|La conjunction ET est vraie si les deux propositions sont vraies."
  "|La disjunction OU est vraie si au moins une des deux propositions est vraie."
  "|Une implication « si A alors B » est fausse seulement lorsque A est vrai et B faux."
  "|La contraposée de « si A alors B » est « si non B alors non A » : elle a la meme valeur de verite, tandis que la reciproque « si B alors A » n'est pas automatiquement vraie."
  "|Un syllogisme tire une conclusion de deux premises, par exemple tous les A sont B, x est A, donc x est B."
  "|La deduction va des generalites vers un cas particulier ; l'induction va d'observations vers une generalisation."
  "|Une hypothese est une proposition provisoire que l'on teste par deduction ou par experience."
  "|Un contre-exemple suffit a invalider une generalization."
  "|Dans une situation de soin, le raisonnement doit distinguer faits observes, interpretations et hypotheses."),
[Q("Quand une implication si A alors B est-elle fausse ?", "A vrai et B vrai~A vrai et B faux~A faux et B vrai~A faux et B faux", 1,
    "L'implication ne faut que si l'antecedent est vrai et le consequent faux."),
 Q("Quelle est la contraposée de si A alors B ?", "Si B alors A~Si non B alors non A~Si non A alors B~Si A alors non B", 1,
    "La contraposée a la meme valeur de verite que l'implication initiale."),
 Q("Quelle est la reciproque de si A alors B ?", "Si B alors A~Si non B alors non A~Si A alors non B~Si non A alors non B", 0,
    "La reciproque n'est pas equivalent a l'implication de depart."),
 Q("Quand une conjonction A ET B est-elle vraie ?", "Si A seul est vrai~Si les deux sont vrais~Si au moins un est vrai~Si aucun n'est vrai", 1,
    "ET exige la verite simultanee des deux propositions."),
 Q("Que Suffit a invalider une generalization ?", "Un exemple~Un contre-exemple~Une opinion~Une repetition", 1,
    "Un seul contre-exemple suffit a montrer qu'une regle generale est fausse."),
 Q("Quel raisonnement va du general au particulier ?", "L'induction~La deduction~L'analogie~La generalisation", 1,
    "La deduction applique une regle generale a un cas precis."),
 Q("Qu'appelle-t-on une hypothese ?", "Une certitude~Une proposition provisoire a tester~Une conclusion finale~Un contre-exemple", 1,
    "L'hypothese est une piste de travail qui doit etre verifiee."),
 T("Distinguer faits, interpretations et hypotheses dans la situation : Madame X a 39 degres et tousse.",
    "Les faits observables sont la temperature de 39 degres et la toux, mesurées et consignees. L'interpretation est que la personne a de la fievre et une symptomelogique respiratoire, ce qui constitue une synthese des faits. L'hypothese est une cause possible : infection virale, pneumopathie, allergie ou effet d'un traitement. Le raisonnement correct consiste a ne pas transformer l'hypothese en certitude : il faut rechercher d'autres signes, interroger la personne et demander des examens. Un contre-exemple, comme une temperature due a un medicament, montre que l'hypothese infectieuse n'est pas automatique.",
    "On attend la distinction des trois niveaux et l'absence de conclusion prematuree."),
 T("Montrer la difference entre implication et reciproque avec un exemple medical.",
    "Considerons : si une personne a une glycosurie, alors sa glycemie est susceptible d'etre elevee. La reciproque dirait : si sa glycemie est elevee, alors elle a une glycosurie. Or ce n'est pas automatique : le seuil renal de reabsorption peut ne pas etre depasse. La contraposée, elle, est equivalente : si la glycemie n'est pas elevee au point de depasser le seuil, alors il n'y a pas de glycosurie. Cet exemple montre qu'une implication vraie n'autorise pas a affirmer sa reciproque, ce qui est une source frequente d'erreur de raisonnement.",
    "On attend un exemple clair, la reciproque non automatique et la contraposée equivalente.")],
C("Le raisonnement tire des conclusions controlees en distinguant faits, hypotheses et portee reel des implications.",
  "Si A alors B : fausse seulement si A vrai et B faux",
  "Contraposée equivalente · reciproque non automatique · contre-exemple invalidant",
  "Proposition~Enonce vrai ou faux~Implication~Si A alors B~Contraposée~Si non B alors non A~Reciproque~Si B alors A",
  "Identifier les propositions|Classer faits et hypotheses|Tester la valeur de verite|Chercher un contre-exemple|Formuler une conclusion prudente",
  "Confondre reciproque et contraposée|Transformer une hypothese en fait|Generaliser sans contre-exemple|Ignorer les exceptions",
  "39 degres~Fait observe~Infection~Hypothese~Toux~Fait~Fievre~Interpretation",
  "Deduction~Du general au particulier~Induction~Du particulier au general",
  "Implication~Si A alors B~Reciproque~Si B alors A"))

# ============================================================ M3
add("ST2S-C-MET03", "Conduite de projet et travail en equipe", METHO, ["1re", "Terminale"],
S("Un projet est une action organisee dans le temps pour atteindre un objectif defini."
  "|La conduite de projet suit les phases de cadrage, de planification, de realisation, de suivi et d'evaluation."
  "|Le cadrage precise le besoin, les objectifs, les contraintes et les parties prenantes."
  "|La planification decompose le projet en taches avec des responsables, des echeances et des ressources."
  "|Le diagramme de Gantt represente les taches dans le temps et leurs chevauchements."
  "|Le chemin critique designe la succession de taches qui determine la duree minimale du projet."
  "|Un retard sur une tache critique retarde toute l'echeance finale."
  "|La repartition des roles clarify les responsabilites et evite les doublons ou les oublis."
  "|Les reunions d'equipe doivent avoir un ordre du jour, un animateur et un compte rendu."
  "|La transmission d'information entre professionnels est indispensable a la continuite du projet."
  "|Les indicateurs de suivi permettent de mesurer l'avancement par rapport au planning."
  "|Une evaluation finale compare les resultats aux objectifs et capitalise les apprentissages pour la suite."),
[Q("Quelle est la premiere phase d'un projet ?", "La realisation~Le cadrage~L'evaluation~Le bilan", 1,
    "On cadre d'abord le besoin, les objectifs et les contraintes avant de planifier."),
 Q("Que represente un diagramme de Gantt ?", "Un budget~Les taches dans le temps~Une liste de contacts~Une carte", 1,
    "Le Gantt visualise les durees, les chevauchements et les jalons des taches."),
 Q("Quel est le chemin critique ?", "La tache la moins chere~La suite de taches determinante pour la duree totale~Le trajet du responsable~La reunion finale", 1,
    "Un retard sur le chemin critique decale l'echeance du projet."),
 Q("Que doit contenir une bonne reunion d'equipe ?", "Un ordre du jour et un compte rendu~Seulement des plaisanteries~Aucun animateur~Une decision non ecrite", 0,
    "Ordre du jour, animateur et compte rendu structurent la reunion et la rendent tracée."),
 Q("A quoi sert un indicateur de suivi ?", "A decorer le dossier~A mesurer l'avancement par rapport au planning~A remplacer le responsable~A supprimer les reunions", 1,
    "L'indicateur donne une mesure objective de l'avancement."),
 Q("Que faire en cas de retard sur une tache critique ?", "Ignorer le retard~Revoir le planning et les ressources~Changer de projet~Attendre la fin", 1,
    "Il faut analyser la cause et ajuster les moyens ou les echeances."),
 Q("Que vise l'evaluation finale ?", "Comparer les resultats aux objectifs et capitaliser~Effacer les traces~Punir les retardataires~Recommencer sans bilan", 0,
    "L'evaluation finale mesure l'atteinte des objectifs et tire des lecons pour la suite."),
 T("Planifier un projet de mise en place d'un atelier de prevention de la chute en etablissement.",
    "Le cadrage definit l'objectif : reduire de 30 % les chutes en six mois, avec les residents et les soignants concernes. Les taches comprennent le recensement des chutes precedentes, l'analyse des lieux a risque, le choix des amenagements, la formation des equipes, le test dans une unite puis la generalisation. Chaque tache recoit un responsable, une echeance et des indicateurs : nombre de chutes, nombre de barres installees, taux de participation des soignants. Un tableau de Gantt situe les taches dans le temps et identifie le chemin critique, ici l'analyse des lieux avant les travaux. Des points d'etape mensuels permettent de reajuster.",
    "On attend objectif, taches, responsables, indicateurs, planning et evaluation."),
 T("Expliquer pourquoi la clarification des roles est essentielle dans un travail d'equipe de soin.",
    "Sans roles clairs, deux professionnels peuvent faire la meme tache pendant qu'une autre est oubliee, par exemple la verification d'une prescription ou la transmission a la famille. La clarification repartit les responsabilites selon les competences de chacun : medecin, infirmier, aide-soignant, kinesitherapeute, assistant social. Elle facilite aussi la communication : chaque personne sait a qui s'adresser et qui rend compte. Elle ne signifie pas une separation etanche : les roles se completent et des relais sont prevus en cas d'absence. La qualite de la prise en charge et la securite du patient en dependent.",
    "On attend les risques de doublon et d'oubli, la complementarite et le lien avec la securite.")],
C("Conduire un projet, c'est cadrer, planifier, realiser, suivre et evaluer avec une equipe aux roles clairs.",
  "Cadrage -> planification -> realisation -> suivi -> evaluation",
  "Gantt : taches dans le temps · chemin critique : duree minimale",
  "Cadrage~Definir le besoin~Gantt~Planning des taches~Chemin critique~Determinant la duree~Indicateur~Mesure de l'avancement",
  "Cadrer le besoin et les objectifs|Decomposer en taches|Repartir les roles|Suivre les indicateurs|Evaluer et capitaliser",
  "Demarrer sans objectif clair|Oublier les dependances entre taches|Ne pas tracer les reunions|Ignorer les retards sur le chemin critique",
  "Atelier chute~Projet~30 %~Objectif~Bilan des chutes~Indicateur~Formation~Tache planifiee",
  "Projet~Action temporaire avec objectif~Activite courante~Travail repetitif",
  "Role~Responsabilite attribuee~Doublon~Tache faite deux fois"))

# ============================================================ M4
add("ST2S-C-MET04", "Communication ecrite et orale professionnelle", METHO, ["1re", "Terminale"],
S("La communication professionnelle vise a transmettre une information utile, claire et fiable."
  "|Un message efficace repond aux questions qui, quoi, quand, comment et pourquoi."
  "|A l'oral, la voix, le rythme, la posture et le regard soutiennent le contenu."
  "|A l'ecrit, la structure en paragraphes et les titres facilitent la lecture."
  "|Un compte rendu de soin relate les faits observes, les actions realisees et les resultats."
  "|Il distingue les donnees objectives des interpretations et evite les jugements personnels."
  "|La transmission orale entre professionnels utilise des codes clairs, par exemple la methodie SBAR : Situation, Background, Assessment, Recommendation, soit contexte, antécédents, evaluation et recommandation."
  "|Une presentation orale comporte une introduction, un developpement ordonne et une conclusion."
  "|Un support visuel lisible accompagne la parole sans la remplacer ni surcharger la diapositive."
  "|L'ecoute de l'auditoire et les questions permettent d'adapter le message en cours de presentation."
  "|Le secret professionnel s'applique aussi aux communications ecrites et aux messages numeriques."
  "|Une relecture finale verifie l'orthographe, les chiffres et la coherence du document."),
[Q("Que signifie le acronyme SBAR ?", "Situation, Background, Assessment, Recommendation~Sante, Bien-etre, Aide, Respect~Soin, Budget, Action, Resultat~Securite, Brief, Analyse, Rapport", 0,
    "SBAR structure une transmission orale : situation, contexte, evaluation, recommandation."),
 Q("Quel element n'appartient pas a un compte rendu de soin ?", "Les faits observes~Les actions realisees~Les resultats~Les gouts personnels du soignant", 3,
    "Le compte rendu relate des faits professionnels, pas des preferences personnelles."),
 Q("Quel critere rend une diapositive efficace ?", "Beaucoup de texte~Peu de texte et une idee par diapositive~Des couleurs nombreuses~Aucun titre", 1,
    "Un support visuel lisible presente une idee principale par diapositive."),
 Q("Quelle est une fonction de la relecture finale ?", "Ajouter des rumeurs~Verifier orthographe, chiffres et coherence~Supprimer les titres~Allonger le texte", 1,
    "La relecture controle la qualite formelle et l'exactitude des informations."),
 Q("Que doit faire un orateur face aux questions de l'auditoire ?", "Ignorer les questions~Repondre en adaptant son message~Se taire jusqu'a la fin~Lire ses notes Sans regarder", 1,
    "Les questions sont une occasion de clarifier et d'adapter le propos."),
 Q("Quelle regle s'applique aux messages numeriques professionnels ?", "Le secret ne s'applique pas~Le secret s'applique aussi~On peut tout ecrire~On peut partager avec n'importe qui", 1,
    "Les courriels et messages sont des supports professionnels soumis au secret."),
 Q("Quel est un avantage d'une structure en paragraphes ?", "Rendre la lecture plus difficile~Faciliter la comprehension~Supprimer les informations~Cacher les chiffres", 1,
    "Une structure claire guide le lecteur et rend l'information accessible."),
 T("Rediger une transmission SBAR pour une personne qui presente une douleur thoracique.",
    "Situation : Monsieur L., 68 ans, se plaint d'une douleur thoracique depuis trente minutes. Background : il est hospitalise pour une pneumopathie et a un antecedent d'hypertension. Assessment : la douleur est intense, le pouls est a 108 et la SpO2 a 94 %, ce qui sugger une situation a risque. Recommendation : demander une evaluation medicale immediate, realiser un electrocardiogramme et installer la personne en position demi-assise en attendant. La transmission est claire, ordonnee, factuelle et accompagnee d'une demande explicite.",
    "On attend les quatre parties SBAR, des donnees objectives et une recommandation precise."),
 T("Expliquer pourquoi un compte rendu doit separer les faits des interpretations.",
    "Un fait est verifiable : la personne a dit avoir mal, la temperature est de 38,2 degres, le pansement est souille. Une interpretation est une hypothese : la personne est anxieuse, la plaie semble infectee. Si l'on melange les deux, le lecteur peut croire que l'hypothese est un constat et prendre une decision inadaptee. La separation permet a chaque professionnel de distinguer ce qui a ete observe de ce qui reste a confirmer. Elle protege aussi la qualite de la transmission et la securite de la personne, notamment en cas de changement d'equipe.",
    "On attend la definition des deux categories et l'effet sur la prise de decision.")],
C("Transmettre, c'est structurer l'information pour qu'elle soit comprise et exploitable par l'equipe.",
  "SBAR : Situation, Background, Assessment, Recommendation",
  "Facts / interpretations · oral et ecrit · secret professionnel · relecture",
  "SBAR~Transmission structuree~Compte rendu~Trace ecrite~Fait~Donnee verifiable~Interpretation~Hypothese a confirmer",
  "Choisir le canal adapte|Structurer le message|Separer faits et interpretations|Formuler une recommandation|Relire et verifier",
  "Mélanger hypothese et fait|Ecrire un message trop long|Oublier le secret professionnel|Negliger la relecture",
  "Douleur thoracique~Situation~SpO2 94 %~Donnee objective~Avis medical~Recommandation~Compte rendu~Transmission",
  "Communication orale~Echange direct~Communication ecrite~Trace durable",
  "Fait~Observation verifiable~Interpretation~Sens donne aux faits"))

# ============================================================ E1
add("ST2S-C-ANG01", "Taking a patient history in English", ANGLAIS, ["1re", "Terminale"],
S("Taking a patient history means collecting structured information about a person and their symptoms."
  "|The interview usually starts with the chief complaint : the main reason for the consultation."
  "|Open questions invite the patient to describe the problem in their own words."
  "|Closed questions are useful to confirm a specific detail, such as the duration of a symptom."
  "|The nurse or caregiver should introduce themselves and explain the purpose of the interview."
  "|Confidentiality must be respected during the whole conversation."
  "|The history includes personal details, current symptoms, past medical history and treatments."
  "|Allergies and current medication are essential safety information."
  "|The SOAPIER structure documents subjective data, objective data, assessment, plan, intervention, evaluation and revision."
  "|Symptoms should be described with their location, intensity, duration, frequency and triggering factors."
  "|The caregiver avoids medical jargon, checks understanding by asking the patient to repeat key points, and uses silence and active listening to encourage the patient to add important details."
  "|The information is then recorded clearly and transmitted to the team."),
[Q("What is the chief complaint ?", "The patient's age~The main reason for the consultation~The nurse's name~The hospital address", 1,
    "The chief complaint is the main problem described by the patient."),
 Q("Which question is open ?", "Do you have a headache ?~Where does it hurt ?~Is it severe ?~Did it start yesterday ?", 1,
    "An open question cannot be answered by yes or no and invites description."),
 Q("What should the caregiver do first ?", "Write the diagnosis~Introduce themselves and explain the purpose~Prescribe a drug~Leave the room", 1,
    "Introducing oneself and explaining the purpose builds trust and consent."),
 Q("Which information is essential for safety ?", "Favourite colour~Allergies and current medication~Holiday plans~Home address only", 1,
    "Allergies and treatments must be known before any new intervention."),
 Q("What does the O stand for in SOAP ?", "Observation~Objective data~Outcome~Order", 1,
    "SOAP stands for Subjective, Objective, Assessment and Plan."),
 Q("How can understanding be checked ?", "By speaking louder~By asking the patient to repeat key points~By changing the topic~By skipping details", 1,
    "Asking the patient to repeat verifies that the information was understood."),
 Q("How should symptoms be described ?", "Only with one word~With location, intensity, duration and triggers~With a joke~With medical jargon", 1,
    "A complete description helps the team assess the problem accurately."),
 T("Write five useful questions to explore a complaint of abdominal pain in English.",
    "Where exactly does the pain hurt ? When did it start ? How would you describe the pain, sharp or dull ? Does anything make it better or worse ? Have you taken any medicine for it ? These questions explore location, onset, character, modifying factors and treatment. They are open or semi-open and avoid suggesting the answer. The caregiver also asks about allergies and other symptoms such as nausea or fever, then records the answers using the patient's own words where possible.",
    "Expected elements : location, onset, character, aggravating or relieving factors, medication."),
 T("Explain why a caregiver should avoid medical jargon when taking a history.",
    "Medical terms such as dyspnoea or nausea may be unfamiliar to a patient, especially if English is not their first language. Using plain words gives a more accurate account of the symptoms. It also respects the person's autonomy : the patient understands what is happening and can give a valid consent. The caregiver can check comprehension by asking the patient to repeat the main points in their own words. Technical terms can still be recorded in the file, but the exchange itself must remain clear and respectful.",
    "Expected elements : accuracy, comprehension, autonomy and verification of understanding.")],
C("A good patient history is structured, respectful and clear : it turns the person's words into useful information.",
  "SOAPIER : subjective, objective, assessment, plan, intervention, evaluation, revision",
  "Open then closed questions · allergies and medication · plain language",
  "Chief complaint~Main reason for consultation~Open question~Invites description~SOAPIER~Documentation structure~Allergy~Safety information",
  "Introduce yourself and explain|Ask open questions|Explore symptoms precisely|Check understanding|Record and transmit",
  "Using jargon~Suggesting the answer~Forgetting allergies~Skipping confidentiality",
  "Abdominal pain~Chief complaint~Where does it hurt ?~Open question~Allergies~Safety~SOAP~Written trace",
  "Open question~Describe in own words~Closed question~Confirm a detail",
  "Subjective data~What the patient says~Objective data~What the caregiver measures"))

# ============================================================ E2
add("ST2S-C-ANG02", "Giving instructions, advice and dosage information", ANGLAIS, ["1re", "Terminale"],
S("Clear instructions help a patient use a treatment safely and correctly."
  "|Take one tablet twice a day means one tablet in the morning and one in the evening."
  "|Before meals, after meals and at bedtime are common timing expressions."
  "|Swallow the tablet whole means that it must not be crushed or chewed."
  "|Drink plenty of water and avoid alcohol are frequent health recommendations."
  "|Do not exceed the stated dose is a standard warning against overdose."
  "|If you miss a dose, do not take a double dose : follow the leaflet or ask a professional."
  "|Complete the full course of antibiotics even if you feel better."
  "|Keep the medicine out of reach of children and store it as indicated on the box."
  "|Side effects such as nausea or drowsiness should be reported if they persist."
  "|The modal should gives advice, must expresses an obligation and may grants permission."
  "|Instructions are easier to follow when they are short, ordered and confirmed by the patient ; the caregiver checks understanding and documents the information given."),
[Q("What does twice a day mean ?", "Once a week~Two times a day~Every two days~Only at night", 1,
    "Twice a day means two administrations in twenty-four hours."),
 Q("What does swallow the tablet whole mean ?", "Take it with sugar~Do not crush or chew it~Cut it in two~Keep it in the mouth", 1,
    "The tablet must be swallowed intact to preserve its formulation."),
 Q("Which modal expresses a strong obligation ?", "May~Might~Must~Could", 2,
    "Must expresses an obligation ; should expresses advice."),
 Q("What should a patient do after missing a dose ?", "Take a double dose~Follow the leaflet or ask a professional~Stop all treatment~Ignore the treatment", 1,
    "Doubling a dose can be dangerous : the leaflet or a professional gives the rule."),
 Q("Why complete the full course of antibiotics ?", "To save money~To avoid recurrence and resistance~Because the box is expensive~To sleep better", 1,
    "Stopping early can leave bacteria and favour resistance."),
 Q("What is a possible side effect ?", "Nausea~A legal obligation~A dosage schedule~A storage condition", 0,
    "Nausea and drowsiness are examples of side effects."),
 Q("How should instructions be given ?", "Long and complex~Short, ordered and confirmed~In medical jargon~Without checking", 1,
    "Short and ordered instructions, confirmed by the patient, are safer."),
 T("Write clear instructions in English for a tablet to be taken twice a day with water, including warnings.",
    "Take one tablet twice a day, in the morning and in the evening, with a glass of water. Swallow the tablet whole : do not crush or chew it. Do not exceed the stated dose. If you miss a dose, do not take a double dose ; follow the leaflet or ask your nurse or pharmacist. If you feel nauseous or unusually sleepy, tell a healthcare professional. Keep the medicine out of reach of children. These sentences combine the dosage, the method, the warnings and the action in case of difficulty.",
    "Expected elements : dosage, timing, water, do not crush, overdose warning, missed dose, side effects."),
 T("Explain the difference between should and must when advising a patient.",
    "Should gives a recommendation : You should drink more water expresses advice that the patient is expected to follow but can discuss. Must expresses a requirement : You must not take this medicine with alcohol states a rule that must be respected for safety. In a care situation, choosing the wrong modal can make an essential instruction sound optional, or a simple suggestion sound like an order. The caregiver also checks that the patient has understood and can repeat the instruction before the treatment is given.",
    "Expected elements : advice versus obligation, safety consequence and confirmation of understanding.")],
C("Patient instructions must be short, precise and checked : dosage, timing, warnings and what to do in case of doubt.",
  "Take one tablet twice a day · swallow whole · do not exceed the dose",
  "should = advice · must = obligation · may = permission",
  "Dosage~Quantity and frequency~Before meals~Timing expression~Overdose~Taking too much~Side effect~Unwanted reaction",
  "State the dose and timing|Explain how to take the medicine|Give the main warnings|Explain what to do if a dose is missed|Check understanding",
  "Giving several instructions at once~Using vague words like later~Forgetting the overdose warning~Skipping the patient's confirmation",
  "One tablet twice a day~Dosage~With water~Method~Do not crush~Whole tablet~Missed dose~Ask a professional",
  "Should~Recommendation~Must~Obligation",
  "Before meals~Prior to eating~After meals~Following the meal"))

# ============================================================ E3
add("ST2S-C-ANG03", "Medical terminology : roots, prefixes and suffixes", ANGLAIS, ["Terminale"],
S("Medical vocabulary is built from Greek and Latin word parts."
  "|A root gives the main meaning, for example cardi for heart or pulmon for lung."
  "|A prefix placed before the root modifies the meaning, such as hypo for low and hyper for high."
  "|A suffix placed after the root also modifies the meaning, such as itis for inflammation and ology for study."
  "|-ectomy means surgical removal, as in appendectomy, and -scopy means visual examination, as in endoscopy."
  "|Hypoglycaemia means a low blood glucose level, while hyperglycaemia means a high level."
  "|Hypertension means high blood pressure and hypotension means low blood pressure."
  "|Tachycardia is a fast heart rate and bradycardia is a slow heart rate."
  "|Dyspnoea means difficulty breathing and apnoea means absence of breathing."
  "|Analgesia means absence of pain, while anaesthesia means loss of sensation."
  "|Understanding word parts helps a caregiver decode an unfamiliar term in a file or a leaflet."
  "|False friends exist : an Anglo-Saxon retreat is not a French retraite but a withdrawal or a side ward."),
[Q("What does the root cardi refer to ?", "The lung~The heart~The liver~The kidney", 1,
    "Cardi comes from the Greek kardia, meaning heart."),
 Q("What does the suffix itis mean ?", "Removal~Inflammation~Study~Examination", 1,
    "Appendicitis means inflammation of the appendix."),
 Q("What does hypo mean ?", "High~Low~Fast~Pain", 1,
    "Hypo indicates a low level, as in hypoglycaemia."),
 Q("What is tachycardia ?", "A slow heart rate~A fast heart rate~An absence of heart rate~A normal heart rate", 1,
    "Tachy means fast ; brady means slow."),
 Q("What does dyspnoea mean ?", "Easy breathing~Difficulty breathing~Absence of breathing~Chest pain only", 1,
    "Dys indicates difficulty ; pnoea refers to breathing."),
 Q("What does an appendectomy involve ?", "Studying the appendix~Removing the appendix~Inflaming the appendix~Examining the appendix visually", 1,
    "The suffix ectomy means surgical removal."),
 Q("What does anaesthesia mean ?", "Absence of pain~Loss of sensation~Inflammation~High blood pressure", 1,
    "Anaesthesia is loss of sensation ; analgesia is absence of pain."),
 T("Decode the terms hypoglycaemia, hypertension and bronchoscopy using word parts.",
    "Hypoglycaemia combines hypo, meaning low, glycaem, referring to glucose in the blood, and the suffix ia, meaning condition : it is a low blood glucose level. Hypertension combines hyper, meaning high, and tension, referring to pressure : it means high blood pressure. Bronchoscopy combines broncho, referring to the bronchi, and scopy, meaning visual examination : it is an examination of the bronchi with an endoscope. Decomposing the word gives a reliable first meaning, which must then be checked against the clinical context.",
    "Expected elements : hypo and hyper, root and suffix for each term, and the caution about context."),
 T("Explain why medical roots and false friends matter for a French caregiver working in English.",
    "Knowing roots and affixes allows a caregiver to understand an unfamiliar term quickly, for example to recognise that a dermatology note concerns the skin or that an analgesia prescription concerns pain relief. False friends can cause the opposite effect : a word that looks French may have a different meaning in English, and a French medical term may not be the obvious translation. Misunderstanding a dosage or a symptom can affect safety. The caregiver therefore uses the word parts as a first clue, confirms with a dictionary or a colleague, and checks understanding with the patient.",
    "Expected elements : decoding, false friends, safety and verification with reliable sources.")],
C("Medical terms are built from roots, prefixes and suffixes : decoding them gives a first reliable meaning.",
  "hypo = low · hyper = high · tachy = fast · brady = slow · itis = inflammation",
  "ectomy = removal · scopy = examination · ology = study",
  "Cardi~Heart~Hyper~High~Hypo~Low~Itis~Inflammation",
  "Identify the root|Identify the prefix|Identify the suffix|Build the literal meaning|Check with the clinical context",
  "Translating word for word~Ignoring false friends~Forgetting the context~Confusing analgesia and anaesthesia",
  "Hypoglycaemia~Low glucose~Hypertension~High pressure~Appendectomy~Removal~Bronchoscopy~Visual examination",
  "Prefix~Before the root~Suffix~After the root",
  "Analgesia~Absence of pain~Anaesthesia~Loss of sensation"))

# ============================================================ E4
add("ST2S-C-ANG04", "Patient education and empathy in professional English", ANGLAIS, ["Terminale"],
S("Patient education helps a person understand their condition and participate in their care."
  "|It starts by assessing what the patient already knows and what they want to know."
  "|Information is given in small steps, with simple words and concrete examples."
  "|The teach-back method asks the patient to explain the information in their own words."
  "|Empathy means showing that the caregiver has understood the person's feelings without judging them."
  "|Useful phrases include I can see this is difficult for you and Tell me how you feel about it."
  "|Empathy is different from sympathy : the caregiver does not have to share the emotion to support the person."
  "|Non-verbal communication includes eye contact, an open posture and an adapted distance, while silence can give the patient time to express a worry."
  "|Encouragement should be sincere :You have made real progress is more useful than a vague compliment."
  "|Shared decision-making presents options, benefits and risks, then respects the patient's choice."
  "|Cultural and language differences require an interpreter when understanding is uncertain."
  "|The caregiver documents the information given and checks the patient's understanding before the end."),
[Q("What is the teach-back method ?", "Asking the patient to repeat the information in their own words~Reading the leaflet aloud~Giving a test~Writing a report", 0,
    "Teach-back verifies comprehension by asking the patient to explain the information back."),
 Q("Which phrase shows empathy ?", "Do not worry, it is nothing~I can see this is difficult for you~You must be quiet~Forget it", 1,
    "This phrase recognises the feeling without minimising it."),
 Q("What does empathy involve ?", "Sharing exactly the same emotion~Understanding the person's feelings without judging~Giving orders~Changing the subject", 1,
    "Empathy is understanding, not emotional fusion or sympathy."),
 Q("What does an adapted distance communicate ?", "Indifference~Respect for intimacy~Urgency~Authority", 1,
    "Distance and posture are part of non-verbal communication and respect for intimacy."),
 Q("When should an interpreter be used ?", "Never~When understanding is uncertain because of language or culture~Only in emergencies~Only for children", 1,
    "An interpreter ensures that information is understood and consent is valid."),
 Q("What is sincere encouragement ?", "A vague compliment~A precise recognition of real progress~A promise that is not certain~A joke", 1,
    "Specific and truthful feedback is more useful than vague reassurance."),
 Q("What does shared decision-making require ?", "Deciding alone~Presenting options and respecting the patient's choice~Hiding the risks~Skipping information", 1,
    "It presents options, benefits and risks, then follows the person's informed choice."),
 T("Write a short dialogue showing empathy when a patient says : I am afraid of the operation.",
    "Caregiver : I can see that you are afraid, and that is understandable. Patient : I had a bad experience before. Caregiver : Thank you for telling me. Tell me what worries you most about this operation. The caregiver keeps an open posture, respects a moment of silence and avoids saying there is nothing to fear. After listening, they explain the procedure step by step, use simple words and ask the patient to repeat the main points. They offer to involve the surgeon for further questions and document the concerns and the information given.",
    "Expected elements : acknowledgement, open question, silence, simple information, teach-back and documentation."),
 T("Explain the difference between empathy and sympathy in a caring relationship.",
    "Empathy means trying to understand the other person's experience and communicating that understanding, while keeping one's own emotional position. Sympathy means feeling with the person, which can create a strong emotional sharing and sometimes reduce professional distance. Both can be supportive, but empathy is more reliable in care because it keeps the caregiver able to act and decide. Showing empathy does not require saying I feel exactly what you feel ; it is enough to say I understand this is hard for you and to adapt the support to what the person needs.",
    "Expected elements : understanding versus emotional sharing, professional distance and a concrete phrase.")],
C("Patient education and empathy turn information into understanding and support the person's autonomy.",
  "Assess knowledge -> give information in steps -> teach-back -> document",
  "Empathy : understand without judging · shared decision-making · interpreter if needed",
  "Teach-back~Verify understanding~Empathy~Understand feelings~Interpreter~Language support~Shared decision~Respect the choice",
  "Assess what the patient knows|Give small, clear pieces of information|Show empathy with words and posture|Use teach-back|Document and confirm",
  "Minimising fears~Using jargon~Promising a certain result~Ignoring language barriers",
  "I am afraid~Feeling expressed~I can see this is difficult~Empathic phrase~Teach-back~Confirmation~Interpreter~Valid consent",
  "Empathy~Understanding the other~Sympathy~Sharing the emotion",
  "Patient education~Build understanding~Information leaflet~Written support"))

valider_et_ecrire(F, "st2s-mat-part-C.json")
