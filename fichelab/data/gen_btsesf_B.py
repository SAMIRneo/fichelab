# -*- coding: utf-8 -*-
"""Générateur btsesf-mat-part-B.json — lot B de la filière bts-esf.

20 fiches 'prototype' (BTS1 / BTS2) : Droit (7), Économie (7),
Comptabilité et gestion (6).
Chaque fiche : 12 points de cours, 9 questions corrigées (7 QCM + 2 texte),
7 blocs en ordre strict, 3 schémas SVG. Aucune injection dans l'application.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _btsesf_common import QC, QT, C, S, build, valider_et_ecrire

F = []


def add(prefix, titre, mat, ans, points, questions, c, ref=""):
    F.append(build(prefix, titre, mat, ans, points, questions, c, ref))


UG = "Programmes d'enseignement général applicables en BTS, référentiel BTS ESF 2022"
UP = "Programmes d'enseignement professionnel, référentiel BTS ESF 2022"

# ============================================================ DR1
add("DR1.", "Les sources du droit et la hiérarchie des normes", "Droit", ["BTS1"],
S("Le droit est un ensemble de règles juridiques organisées, édictées par des autorités compétentes et sanctionnées par l'État."
  "|La hiérarchie des normes classe les règles selon leur force : constitution, traités et lois, règlements, actes individuels."
  "|La Constitution de 1958 est la norme suprême de l'ordre juridique interne : toute loi contraire peut être censurée par le Conseil constitutionnel."
  "|Les traités et accords internationaux ratifiés ont une autorité supérieure à la loi, sous réserve de réciprocité."
  "|La loi est votée par le Parlement ; le règlement (décret, arrêté) est pris par le pouvoir exécutif pour son application."
  "|Le principe de légalité impose à l'administration d'agir conformément aux règles qui la fondent et la limitent."
  "|Le juge administratif contrôle la légalité des actes administratifs ; le juge judiciaire protège les libertés et les droits privés."
  "|La Cour européenne des droits de l'homme vérifie le respect de la Convention européenne des droits de l'homme par les États."
  "|Le droit de l'Union européenne, notamment les règlements et directives, s'impose aux États membres dans les domaines de sa compétence."
  "|Une norme inférieure ne peut déroger à une norme supérieure : c'est le principe de conformité hiérarchique."
  "|La sécurité juridique exige que les règles soient claires, publiées et non rétroactives, afin que chacun puisse connaître ses droits et devoirs."
  "|Pour un professionnel de l'action sociale, savoir identifier la source d'une règle permet de vérifier un droit et d'orienter correctement un usager."),
[QC("Quelle est la norme suprême de l'ordre juridique interne ?", "La loi~Le décret~La Constitution~L'arrêté préfectoral", 2,
    "La Constitution de 1958 occupe le sommet de la hiérarchie des normes internes."),
 QC("Quel organe censure une loi contraire à la Constitution ?", "Le Conseil d'État~Le Conseil constitutionnel~La Cour de cassation~Le préfet", 1,
    "Le Conseil constitutionnel vérifie la conformité des lois à la Constitution."),
 QC("Quelle autorité prend un décret ?", "Le Parlement~Le président de la République ou le Premier ministre~Le juge administratif~Le conseil municipal", 1,
    "Le décret est un acte réglementaire du pouvoir exécutif."),
 QC("Que signifie le principe de légalité pour l'administration ?", "Elle peut agir librement~Elle doit agir selon les règles qui la fondent et la limitent~Elle n'a pas besoin de motif~Elle est au-dessus du droit", 1,
    "L'administration est soumise au droit et ne peut agir sans base légale."),
 QC("Quel juge contrôle la légalité d'un acte administratif ?", "Le juge judiciaire~Le juge administratif~Le juge pénal~Le juge constitutionnel", 1,
    "Le juge administratif annule les actes administratifs illégaux."),
 QC("Un règlement peut-il contredire une loi ?", "Oui, toujours~Non, il doit être conforme à la loi~Oui, si le préfet l'accepte~Non, sauf en cas d'urgence", 1,
    "La hiérarchie des normes interdit à une norme inférieure de déroger à une norme supérieure."),
 QC("Que garantit la sécurité juridique ?", "La gratuité des démarches~Des règles claires, publiées et non rétroactives~L'absence de juge~Une procédure secrète", 1,
    "La clarté, la publication et la non-rétroactivité permettent de connaître le droit à l'avance."),
 QT("Un usager conteste une décision administrative refusant une prestation. Expliquez comment identifier la règle applicable et la voie de recours possible.",
    "Je commence par identifier la nature de la décision : acte administratif individuel pris par un organisme chargé d'une mission de service public. Je recherche ensuite sa base légale : texte législatif ou réglementaire, circulaire d'application, et je vérifie qu'il est toujours en vigueur et conforme aux normes supérieures, notamment le droit européen et la Constitution. Je contrôle la compétence de l'auteur de l'acte, la procédure suivie (droit d'être entendu, motivation, délai) et la proportionnalité de la décision. Si une illégalité est probable, je privilégie d'abord le recours administratif : demande de réexamen auprès de l'organisme, puis, en cas de rejet, recours contentieux pour excès de pouvoir devant le tribunal administratif compétent dans le délai de deux mois suivant la notification. Je peux également saisir le Défenseur des droits si une discrimination ou un manquement aux droits est soupçonné, ou un médiateur institutionnel. J'informe l'usager des délais et de la nécessité de conserver la décision écrite, les justificatifs et les traces des échanges. Le rôle du professionnel n'est pas de garantir le succès du recours, mais de rendre la démarche compréhensible et accessible.",
    "On attend l'identification de l'acte, la recherche de la base légale, la vérification de la procédure et la distinction recours administratif / contentieux."),
 QT("Distinguer la loi et le règlement, puis expliquer pourquoi une circulaire ne peut pas aller à l'encontre d'un décret.",
    "La loi est votée par le Parlement et porte les règles les plus importantes dans les matières que la Constitution lui réserve ; elle est publiée au Journal officiel. Le règlement est une règle générale et abstraite prise par le pouvoir exécutif : décret en Conseil d'État ou décret simple pris par le Premier ministre ou le président de la République, arrêté ministériel ou préfectoral. Il précise les conditions d'application de la loi sans en modifier le contenu. La circulaire est une instruction d'ordre interne adressée aux services pour harmoniser la mise en œuvre d'une règle : elle n'a pas la valeur d'un règlement et ne peut créer de nouveaux droits ni de nouvelles obligations pour les usagers. En vertu de la hiérarchie des normes, une norme inférieure doit rester conforme à la norme supérieure : une circulaire qui contredirait un décret serait illégale et pourrait être annulée par le juge administratif, même si elle est appliquée dans la pratique. Pour un professionnel, cette distinction est concrète : face à un refus fondé sur une circulaire, on vérifie le décret et la loi auxquels elle se rapporte, car c'est la règle supérieure qui fait foi.",
    "La réponse doit définir loi, règlement et circulaire, puis invoquer la hiérarchie des normes et le contrôle du juge.")],
C("Le droit s'organise en pyramid : la norme supérieure commande la norme inférieure et le juge en garantit le respect.",
  "Constitution > traités > lois > règlements > actes individuels",
  "Légalité · sécurité juridique · contrôle du juge administratif ou constitutionnel",
  "Constitution~Norme suprême~Conseil constitutionnel|Loi~Votée par le Parlement~Journal officiel|Règlement~Décret ou arrêté~Pouvoir exécutif",
  "Identifier la décision contestée|Rechercher le texte applicable et son autorité|Vérifier la compétence et la procédure|Comparer avec les normes supérieures|Choisir la voie de recours adaptée",
  "Utiliser une circulaire comme une loi|Ignorer le délai de recours|Confondre juge administratif et juge judiciaire|Supposer qu'une décision écrite est toujours légale",
  "Deux mois~Délai de recours~1958~Constitution~Juge administratif~Contrôle de légalité~Circulaire~Instruction interne",
  "Loi~Vote parlementaire~Règlement~Application de la loi",
  "Légalité~Agir selon le droit~Sécurité juridique~Règle prévisible"),
UG)

# ============================================================ DR2
add("DR2.", "Droit civil : personnes, capacité et responsabilité", "Droit", ["BTS1"],
S("Le droit civil régit les rapports entre personnes privées : état des personnes, biens, contrats et responsabilité."
  "|Une personne physique est un être humain titulaire de droits ; une personne morale est un groupement doté de la personnalité juridique, comme une association."
  "|La personnalité juridique commence à la naissance et s'achève au décès ; elle confère la titularité des droits et des obligations."
  "|La capacité juridique est l'aptitude à exercer ses droits et à accomplir des actes juridiques valables."
  "|Les mineurs et les majeurs protégés ont une capacité limitée : ils sont représentés ou assistés par leur représentant légal."
  "|L'émancipation permet à un mineur de seize ans, avec l'accord de ses parents et du juge, d'acquérir la capacité juridique."
  "|La tutelle et la curatelle sont des mesures de protection des majeurs incapables, prononcées par le juge des tutelles."
  "|La responsabilité civile impose de réparer le dommage causé à autrui : elle peut être contractuelle ou délictuelle."
  "|La responsabilité contractuelle résulte de l'inexécution d'un contrat ; la responsabilité délictuelle naît d'une faute en dehors de tout contrat."
  "|La responsabilité du fait des choses implique de répondre du dommage causé par une chose dont on a la garde, même sans faute."
  "|Les dommages-intérêts visent à réparer le préjudice subi : perte financière, atteinte à l'intégrité ou préjudice moral."
  "|En action sociale, la question de la capacité est quotidienne : signer un contrat, consentir à une démarche ou représenter une personne exige de vérifier son régime de protection."),
[QC("Quand commence la personnalité juridique ?", "À la conception~À la naissance~À la majorité~Au mariage", 1,
    "La personnalité juridique commence à la naissance et prend fin au décès."),
 QC("Quel est un exemple de personne morale ?", "Un salarié~Une association~Un usager majeur~Un enfant", 1,
    "Une association dispose de la personnalité juridique, distincte de celle de ses membres."),
 QC("Quel régime concerne un majeur qui a besoin d'être assisté sans être remplacé ?", "La tutelle~La curatelle~L'émancipation~La garde", 1,
    "En curatelle, la personne agit avec l'assistance du curateur ; en tutelle, elle est représentée."),
 QC("Quelle responsabilité naît d'une faute commise sans contrat ?", "Contractuelle~Délictuelle~Pénale~Administrative", 1,
    "La responsabilité délictuelle découle d'une faute, d'un dommage et d'un lien de causalité, hors contrat."),
 QC("Quel âge minimum pour l'émancipation ?", "Seize ans~Dix-huit ans~Quinze ans~Vingt-un ans", 0,
    "Un mineur de seize ans peut être émancipé avec l'accord de ses représentants légaux et du juge."),
 QC("Que vise l'indemnisation d'un préjudice moral ?", "À punir systématiquement~À réparer une atteinte non économique~À rembourser un salaire~À annuler un contrat", 1,
    "Le préjudice moral correspond à une atteinte à la dignité, à l'honneur ou à la tranquillité."),
 QC("Que doit vérifier un professionnel avant de faire signer un document à une personne protégée ?", "Son âge seulement~Sa capacité juridique et l'accord du représentant légal~Son adresse~Son niveau de revenu", 1,
    "La validité de l'acte dépend de la capacité et, selon le régime, de l'assistance ou de la représentation."),
 QT("Un usager majeur placé sous curatelle souhaite signer seul un contrat d'énergie. Expliquez la démarche à suivre et les risques juridiques.",
    "Je vérifie d'abord la décision du juge des tutelles : en curatelle, la personne conserve la capacité d'agir mais doit être assistée par son curateur pour les actes importants. Un contrat d'énergie comportant un engagement financier durable entre dans cette catégorie : la signature seule peut être annulée si le curateur n'a pas donné son concours. Je contacte alors le curateur pour l'informer de la demande, je lui transmets les conditions générales, le montant estimé, la durée et les modalités de résiliation, et je l'invite à donner son accord écrit ou à contresigner. J'explique également à l'usager, avec des mots simples, ce à quoi il s'engage : prix, durée, prélèvement automatique, conséquences d'un retard de paiement. Si l'usager est sous tutelle, la règle est plus stricte : le tuteur agit en son nom et la signature de l'intéressé ne suffit pas. Dans tous les cas, je conserve une trace de la vérification et de l'accord obtenu, et j'oriente vers le juge ou le conseil départemental en cas de désaccord entre l'usager et son représentant. Le respect de la capacité protège l'usager, mais il protège aussi la structure contre une remise en cause ultérieure du contrat.",
    "On attend la distinction curatelle/tutelle, l'exigence d'assistance ou de représentation, l'information claire de l'usager et la conservation d'une trace."),
 QT("Expliquer les trois conditions de la responsabilité civile délictuelle et les distinguer de la responsabilité contractuelle.",
    "La responsabilité délictuelle repose sur trois conditions cumulatives : une faute, un dommage et un lien de causalité entre la faute et le dommage. La faute peut être une violation d'une obligation de prudence ou un comportement fautif ; le dommage doit être certain, légitime et direct ; le lien de causalité exige que le dommage soit la conséquence de la faute, sans qu'une autre cause exclusive l'explique. Il existe aussi des responsabilités sans faute, comme la responsabilité du fait des choses ou du fait d'autrui, où la victime doit seulement prouver le dommage et le lien avec la chose ou la personne sous garde. La responsabilité contractuelle, elle, naît de la violation d'une obligation prévue par un contrat valable : le créancier doit démontrer l'inexécution, et le débiteur peut s'exonérer en prouvant une cause étrangère, par exemple un événement de force majeure. Les deux régimes diffèrent donc par leur fondement, par la charge de la preuve et par les exonérations possibles. En pratique, un même fait peut donner lieu à un concours de responsabilités : on choisit alors le fondement le plus favorable à la victime, sous le contrôle du juge.",
    "On attend faute, dommage, causalité, une mention des responsabilités sans faute et une comparaison avec le contrat.")],
C("Le droit civil organise la vie des personnes et répare les dommages : capacité, représentation et responsabilité sont indissociables.",
  "Personnalité juridique ≠ capacité juridique",
  "Responsabilité : faute + dommage + lien de causalité",
  "Personne physique~Être humain~Titulaire de droits|Personne morale~Groupement~Association|Capacité~Aptitude à agir~Limitée ou pleine",
  "Identifier le régime juridique de la personne|Vérifier sa capacité pour l'acte envisagé|Contacter le représentant légal si nécessaire|Expliquer les effets de l'acte|Conserver la preuve de l'accord",
  "Confondre personnalité et capacité|Ignorer la curatelle pour un engagement financier|Croire que la tutelle se réduit à un conseil|Négliger la preuve écrite",
  "Seize ans~Âge de l'émancipation~Curatelle~Assistance~Tutelle~Représentation~Trois conditions~Faute, dommage, causalité",
  "Tutelle~Représenter la personne~Curatelle~Assister la personne",
  "Contractuelle~Violation d'un contrat~Délictuelle~Faute hors contrat"),
UG)

# ============================================================ DR3
add("DR3.", "Le contrat : formation, validité et effets", "Droit", ["BTS1"],
S("Le contrat est un accord de volontés destiné à créer, modifier ou éteindre des obligations entre deux ou plusieurs parties."
  "|Le principe de liberté contractuelle permet de choisir son cocontractant et de déterminer le contenu du contrat, dans la limite de l'ordre public."
  "|La formation du contrat suppose un consentement valable : l'offre et l'acceptation doivent se rencontrer."
  "|Une offre est une proposition précise de contrat qui engage son auteur pendant un délai déterminé."
  "|L'acceptation est l'adhésion sans réserve à l'offre : une modification des conditions constitue une contre-offre."
  "|Le consentement est vicié lorsqu'il résulte d'une erreur, d'un dol (manœuvre frauduleuse) ou d'une violence."
  "|Pour être valable, le contrat exige aussi une capacité juridique des parties, un objet certain et licite et une cause licite."
  "|Les contrats sont en principe consensuels : ils se forment par le seul échange des consentements, sauf forme particulière imposée par la loi."
  "|Le contrat fait loi entre les parties : il doit être exécuté de bonne foi, selon les usages et l'équité."
  "|L'inexécution contractuelle expose le débiteur à des dommages-intérêts, à une pénalité prévue ou à la résolution du contrat."
  "|Une clause abusive est une clause qui crée un déséquilibre significatif au détriment d'une partie, notamment dans un contrat d'adhésion."
  "|Le Code civil, entré en vigueur dans sa version rénovée en 2016, constitue le texte de référence du droit des contrats."),
[QC("Quand le contrat est-il formé en principe ?", "Lors de la signature chez un notaire~Dès l'échange des consentements~Après paiement intégral~Après enregistrement au tribunal", 1,
    "Le contrat est consensuel : l'offre et l'acceptation suffisent, sauf exigence légale de forme."),
 QC("Qu'est-ce qu'une contre-offre ?", "Une acceptation sans réserve~Une modification apportée à l'offre~Un simple accusé de réception~Une résiliation", 1,
    "Modifier l'offre revient à refuser celle-ci et à en proposer une nouvelle."),
 QC("Quel vice du consentement correspond à une manœuvre frauduleuse ?", "L'erreur~Le dol~La violence~La capacité", 1,
    "Le dol est une manœuvre ou un mensonge destiné à obtenir un consentement."),
 QC("Quelle condition de validité concerne le but du contrat ?", "La forme écrite~La cause licite~La durée minimale~Le lieu de signature", 1,
    "La cause, c'est-à-dire le but poursuivi, doit être licite et conforme à l'ordre public."),
 QC("Que signifie « le contrat fait loi entre les parties » ?", "Il ne peut jamais être modifié~Il oblige les parties comme une règle pour elles~Il est supérieur à la loi~Il dispense de tout contrôle", 1,
    "Le contrat crée des obligations que les parties doivent exécuter, sous le contrôle du juge."),
 QC("Quel est un exemple de clause abusive ?", "Une clause de résiliation après préavis raisonnable~Une clause imposant un déséquilibre significatif~Une clause de confidentialité~Une clause de paiement du prix", 1,
    "La clause abusive désavantage fortement une partie, notamment dans un contrat d'adhésion."),
 QC("Quel texte régit principalement le droit des contrats en France ?", "Le Code pénal~Le Code civil~Le Code du travail~Le Code de la route", 1,
    "Le Code civil, rénové en 2016, contient les règles générales du contrat."),
 QT("Un usager signe un contrat d'accompagnement dont il ne comprend pas une clause de résiliation unilatérale. Analysez la situation et proposez une réponse professionnelle.",
    "Je me demande d'abord s'il y a eu consentement éclairé : une clause rédigée dans un jargon incompréhensible peut faire douter de la portée de l'accord, surtout si aucune explication n'a été donnée avant la signature. Je vérifie le régime de la clause : une résiliation unilatérale est licite dans de nombreux contrats, mais elle doit être prévue clairement, respecter un préavis et ne pas créer un déséquilibre significatif. Si tel est le cas, je me trouve en présence d'une clause potentiellement abusive, en particulier dans un contrat d'adhésion. J'explique alors à l'usager, avec ses mots, ce que la clause permet, dans quel délai et avec quelles conséquences ; je lui remets un exemplaire et je l'invite à poser ses questions. Si le déséquilibre paraît réel, je préviens le responsable juridique de la structure pour une révision du modèle de contrat, et j'oriente l'usager vers une association de consommateurs ou un conseil juridique gratuit si une contestation est envisagée. Je n'affirme jamais que la clause est nulle sans vérification : la qualification relève du juge. Enfin, je consigne l'échange dans le dossier, car l'information donnée fait partie de la qualité de l'accompagnement et de la preuve du consentement éclairé.",
    "On attend l'analyse du consentement, la notion de clause abusive, l'information claire de l'usager et l'orientation vers les bons interlocuteurs."),
 QT("Distinguer offre, acceptation et promesse de contrat, puis montrer pourquoi une réponse « oui, mais à condition de... » n'est pas une acceptation.",
    "L'offre est une proposition de contrat suffisamment déterminée : elle identifie les parties, le contenu et les obligations essentielles, et elle engage son auteur dès qu'elle est reçue, pendant le délai qu'elle fixe ou un délai raisonnable. L'acceptation est l'adhésion sans réserve ni condition à cette offre : elle peut être expresse ou tacite, mais elle doit porter sur tous les éléments proposés. La promesse de contrat est un acte par lequel une personne s'engage à conclure ultérieurement un contrat ; elle produit des effets propres et peut engager la responsabilité de celui qui la respecte mal. Une réponse formulée « oui, mais à condition de... » ne constitue pas une acceptation, car elle subordonne l'accord à une modification : juridiquement, c'est une contre-offre. Le contrat n'est donc pas formé à ce stade ; il ne le sera que si l'auteur de l'offre initiale accepte à son tour la nouvelle proposition. Cette nuance a des conséquences pratiques importantes : si l'un des deux partenaires commence à exécuter le contrat en croyant à un accord, il peut se retrouver sans base contractuelle. La règle est donc de faire confirmer explicitement chaque modification par écrit, afin que l'échange des consentements soit certain et prouvable.",
    "La réponse doit définir les trois notions et expliquer la qualification de contre-offre avec une conséquence concrète.")],
C("Le contrat naît d'un consentement rencontré et valable : offre, acceptation, capacité, objet et cause licite.",
  "Contrat = accord de volontés + obligation",
  "Vices du consentement : erreur, dol, violence · contrat d'adhésion et clauses abusives",
  "Offre~Proposition précise~Engage son auteur|Acceptation~Adhésion sans réserve~Forme le contrat|Validité~Capacité, objet, cause~Conditions cumulatives",
  "Vérifier l'offre et son délai de validité|Contrôler l'absence de réserve dans l'acceptation|Vérifier capacité et licéité|Repérer les clauses déséquilibrées|Expliquer les effets avant signature",
  "Croire qu'un « oui » conditionnel suffit|Ignorer une clause de résiliation|Négliger la capacité d'une personne protégée|Laisser une ambiguïté sur le prix",
  "2016~Réforme du Code civil~Dol~Manœuvre frauduleuse~Clause abusive~Déséquilibre~Bonne foi~Exécution loyale",
  "Offre~Proposition initiale~Contre-offre~Modification proposée",
  "Erreur~Fausse représentation~Violence~Contrainte exercée"),
UG)

# ============================================================ DR4
add("DR4.", "Le droit du travail : contrat, durée et protection du salarié", "Droit", ["BTS1"],
S("Le contrat de travail est une convention par laquelle une personne s'engage à travailler sous la direction d'une autre, moyennant une rémunération."
  "|Trois critères le caractérisent : la prestation de travail, la subordination juridique et la rémunération."
  "|La subordination implique un pouvoir de direction, de contrôle et de sanction de l'employeur."
  "|Le contrat à durée indéterminée (CDI) est la forme normale de l'embauche ; le contrat à durée déterminée (CDD) est encadré par des motifs légaux."
  "|Le CDD ne peut être utilisé pour pourvoir durablement un emploi lié à l'activité normale de l'entreprise."
  "|La période d'essai permet à l'employeur d'évaluer le salarié et à celui-ci de vérifier l'emploi, dans des limites de durée et avec un préavis."
  "|Le temps de travail est plafonné légalement à 35 heures hebdomadaires en moyenne, avec des heures supplémentaires majorées et compensées."
  "|Le salaire minimum interprofessionnel de croissance (SMIC) garantit une rémunération plancher pour les salariés majeurs."
  "|Le salarié bénéficie de congés payés, de repos quotidiens et hebdomadaires, ainsi que d'une protection en cas de maladie ou de maternité."
  "|Le licenciement doit avoir une cause réelle et sérieuse, respecter une procédure et ouvrir droit à des indemnités selon les cas."
  "|Les représentants du personnel, le comité social et économique et l'inspection du travail contribuent à la protection des salariés."
  "|Dans le secteur social, la convention collective applicable complète le Code du travail sur les salaires, les horaires et les conditions d'emploi."),
[QC("Quels sont les trois critères du contrat de travail ?", "Prestation, subordination, rémunération~Lieu, horaire, ancienneté~Diplôme, âge, adresse~Offre, acceptation, écrit", 0,
    "Le contrat de travail suppose un travail, un lien de subordination et une rémunération."),
 QC("Quelle est la forme normale d'embauche ?", "Le CDD~Le CDI~Le contrat saisonnier~Le contrat d'apprentissage", 1,
    "Le CDI est la forme normale ; le CDD doit répondre à un motif précis."),
 QC("Quel motif peut justifier un CDD ?", "Pourvoir durablement un poste permanent~Remplacer une salariée en congé de maternité~Réduire le coût salarial~Éviter une période d'essai", 1,
    "Le remplacement d'un salarié absent est un motif légal de recours au CDD."),
 QC("Que désigne la subordination juridique ?", "Une simple hiérarchie sociale~Un pouvoir de direction, contrôle et sanction~Une obligation de ponctualité~Un lien de parenté", 1,
    "La subordination est le critère central qui distingue le salarié du travailleur indépendant."),
 QC("Quelle est la durée légale hebdomadaire de référence ?", "35 heures~39 heures~40 heures~32 heures", 0,
    "La durée légale est fixée à 35 heures par semaine en moyenne."),
 QC("Quel organisme contrôle l'application du droit du travail ?", "La CNIL~L'inspection du travail~La CAF~Le Conseil constitutionnel", 1,
    "L'inspection du travail veille au respect des règles dans les entreprises."),
 QC("Quel texte complète le Code du travail pour une branche professionnelle ?", "Le règlement intérieur~La convention collective~Le décret lois~Le contrat de garantie", 1,
    "La convention collective fixe des règles plus favorables ou plus précises pour la branche."),
 QT("Une association emploie une salariée en CDD depuis dix-huit mois pour une mission d'accueil qui se poursuit sans interruption. Analysez la situation et indiquez les risques.",
    "Le CDD est un contrat dérogatoire : il ne peut être conclu que pour un motif légal limitatif, par exemple le remplacement d'un salarié absent, une augmentation temporaire d'activité ou un chantier déterminé. Il ne peut pas servir à pourvoir durablement un emploi qui correspond à l'activité normale et permanente de l'association. Si la salariée occupe depuis dix-huit mois un poste d'accueil permanent, sans remplacement précis ni mission définie, le contrat est susceptible d'être requalifié en CDI par le juge prud'homal. Cette requalification entraîne des conséquences financières : indemnité de requalification, rappel de salaire lié à l'ancienneté, congés payés et indemnités de licenciement si une rupture intervient ensuite. Le risque est renforcé si le même poste est occupé successivement par plusieurs CDD. La démarche correcte consiste à régulariser la situation en proposant un CDI, après avoir vérifié le motif initial et les conditions de renouvellement. Parallèlement, l'association doit vérifier la convention collective applicable, la rémunération au moins égale au SMIC, le respect des repos et l'affiliation aux organismes sociaux. Je préviens la direction par écrit, avec les dates et les éléments factuels, et je propose un calendrier de régularisation plutôt que d'attendre un contrôle de l'inspection du travail.",
    "On attend la finalité limitative du CDD, le risque de requalification en CDI, ses conséquences et une proposition de régularisation."),
 QT("Un salarié invoque 44 heures de travail effectif sur une semaine. Expliquez les règles applicables et les vérifications à opérer.",
    "La durée légale est de 35 heures par semaine, mais elle s'entend en moyenne sur une période plus longue lorsque l'employeur applique un aménagement du temps de travail autorisé. Les heures au-delà de 35 heures sont des heures supplémentaires : elles ouvrent droit à une majoration de salaire, généralement 25 % pour les huit premières heures et 50 % au-delà, ou à un repos compensateur équivalent selon les dispositions applicables. Un plafond absolu existe également : la durée hebdomadaire maximale est en principe de 48 heures, avec un maximum de 44 heures en moyenne sur une période de douze semaines consécutives. Les vérifications portent donc sur le temps de travail effectif, c'est-à-dire le temps pendant lequel le salarié est à la disposition de l'employeur et ne peut disposer librement de son temps : les pauses non travaillées sont exclues, les astreintes obéissent à des règles particulières. Je vérifie également l'éventuel accord d'aménagement du temps de travail, les modalités de décompte, le paiement des majorations sur le bulletin de salaire et le respect du repos quotidien de onze heures. Si les heures ne sont pas payées ou compensées, je préviens le service des ressources humaines et j'invite le salarié à conserver ses relevés d'horaires avant de saisir, si nécessaire, l'inspection du travail ou le conseil de prud'hommes.",
    "On attend la durée légale, la notion d'heures supplémentaires, les plafonds, la définition du temps effectif et les vérifications concrètes.")],
C("Le contrat de travail repose sur un lien de subordination et bénéficie d'un encadrement protecteur : durée, salaire, repos, procédure.",
  "Contrat de travail = prestation + subordination + rémunération",
  "CDI = forme normale · CDD = motif légal · 35 heures · SMIC · inspection du travail",
  "CDI~Durée indéterminée~Forme normale|CDD~Durée déterminée~Motif encadré|Subordination~Pouvoir de direction~Critère central",
  "Vérifier la présence des trois critères|Identifier le type de contrat et son motif|Contrôler durée, salaire et repos|Respecter la procédure en cas de rupture|Consulter la convention collective",
  "Utiliser un CDD pour un poste permanent|Oublier la majoration des heures supplémentaires|Confondre pause et temps de travail effectif|Ignorer la convention collective",
  "35 heures~Durée légale~25 %~Majoration courante~48 heures~Plafond hebdomadaire~SMIC~Salaire minimum",
  "CDI~Emploi durable~CDD~Emploi temporaire motivé",
  "Temps de travail effectif~À la disposition de l'employeur~Pause libre~Non comptabilisée"),
"Code du travail et programmes d'enseignement général applicables en BTS, référentiel BTS ESF 2022")

# ============================================================ DR5
add("DR5.", "La protection sociale : risques et prestations", "Droit", ["BTS1"],
S("La protection sociale comprend les mécanismes qui protègent les personnes contre les risques de la vie et leur garantissent des ressources."
  "|Elle repose sur le principe de solidarité : les cotisations des actifs financent les prestations servies aux ayants droit."
  "|Les grands risques couverts sont la maladie, la maternité, l'invalidité, le décès, les accidents du travail, le chômage et la vieillesse."
  "|Le régime général de la Sécurité sociale comprend notamment l'assurance maladie, l'assurance vieillesse et l'assurance accidents du travail."
  "|L'Unédic gère l'assurance chômage, financée par des cotisations employeurs et salariés."
  "|La Caisse d'allocations familiales verse les prestations familiales et sociales, comme les allocations familiales ou le RSA."
  "|Les prestations peuvent être contributives, financées par des cotisations, ou non contributives, financées par l'État ou la collectivité."
  "|Le principe d'unicité du régime tend à éviter les disparités, mais des régimes particuliers subsistent pour certaines professions."
  "|Le ticket modérateur est la part des dépenses de santé laissée à la charge de l'assuré, souvent prise en charge par une complémentaire."
  "|La couverture maladie universelle complémentaire (CMU-C), aujourd'hui complémentaire santé solidaire, aide les personnes aux faibles revenus."
  "|La CNSF et les conseils départementaux interviennent dans l'action sociale ; le droit à l'accompagnement relève aussi de la solidarité nationale."
  "|Les indemnités journalières remplacent une partie du salaire lors d'un arrêt de travail, après un délai de carence et sous conditions d'ouverture de droits."),
[QC("Quel organisme gère l'assurance chômage ?", "La CNAM~L'Unédic~La CAF~Le CNESER", 1,
    "L'Unédic est l'organisme gestionnaire du régime d'assurance chômage."),
 QC("Quel risque est couvert par l'assurance accidents du travail ?", "Le chômage~La vieillesse~Les accidents survenus à l'occasion du travail~Les disputes familiales", 2,
    "L'assurance accidents du travail et maladies professionnelles couvre les risques liés à l'activité professionnelle."),
 QC("Qu'appelle-t-on prestation non contributive ?", "Une prestation financée par les seules cotisations~Une prestation financée par l'État ou la collectivité~Une prestation réservée aux retraités~Une prestation versée par l'employeur", 1,
    "Les prestations non contributives sont financées par des ressources publiques, sans cotisation préalable de l'intéressé."),
 QC("Que désigne le ticket modérateur ?", "Le montant total de la facture~La part laissée à la charge de l'assuré~Le délai de remboursement~Le numéro de sécurité sociale", 1,
    "Le ticket modérateur est la fraction des dépenses non remboursée par l'assurance maladie obligatoire."),
 QC("Quel principe fonde le financement de la protection sociale ?", "La concurrence~La solidarité~Le bénéfice individuel~La gratuité totale", 1,
    "La protection sociale repose sur la mutualisation des risques et la solidarité entre les membres de la collectivité."),
 QC("Quel organisme verse les prestations familiales ?", "La CNIL~La CAF~La CNAM~France Travail", 1,
    "Les caisses d'allocations familiales servent les prestations familiales et sociales."),
 QC("Quel dispositif aide les personnes aux faibles revenus à accéder à une complémentaire santé ?", "La complémentaire santé solidaire~L'assurance chômage~Le RSA~La prime d'activité", 0,
    "La complémentaire santé solidaire remplace la CMU-C et l'aide à la complémentaire santé (ACS)."),
 QT("Une personne âgée de 58 ans, en arrêt de travail pour maladie depuis trois mois, s'interroge sur ses ressources et ses démarches. Expliquez les mécanismes susceptibles de l'aider.",
    "Plusieurs mécanismes peuvent intervenir, sans se cumuler automatiquement. D'abord, les indemnités journalières de l'assurance maladie remplacent une partie du salaire pendant l'arrêt de travail, après un délai de carence et sous condition d'activité ou de cotisations suffisantes ; l'employeur peut maintenir tout ou partie du salaire selon la convention collective. Ensuite, si l'état de santé devient durablement incompatible avec tout emploi, une demande de reconnaissance de la qualité de travailleur handicapé peut être déposée auprès de la MDPH, ce qui ouvre des droits à des aménagements et à des prestations comme l'allocation adulte handicapé sous conditions de ressources. À 58 ans, la question de l'invalidité et de la retraite anticipée pour incapacité de travail se pose également : le dossier doit être instruit avec la caisse de retraite et le médecin du travail. Enfin, le CCAS de la commune peut accorder une aide financière d'urgence ou orienter vers le département pour une aide sociale. Ma démarche professionnelle consiste à faire le point sur les ressources réelles, à vérifier les dates et les justificatifs, à orienter la personne vers les bons organismes et à l'aider à formuler ses demandes, sans me substituer à elle ni garantir une décision favorable. Je reste attentif à la dignité de la personne et à la confidentialité des informations de santé.",
    "On attend une distinction entre indemnités journalières, MDPH et prestations, invalidité/retraite et aide sociale, avec une posture professionnelle adaptée."),
 QT("Expliquer la différence entre prestation contributive et non contributive, et illustrer avec deux exemples.",
    "Une prestation contributive est financée par des cotisations versées au titre d'une activité professionnelle ou d'un régime obligatoire : c'est le cas des indemnités journalières maladie ou de la pension de retraite du régime général, dont le montant dépend de la durée d'assurance et des revenus antérieurs. Elle repose sur un droit acquis par la participation au financement du régime. Une prestation non contributive est financée par l'État ou les collectivités territoriales et n'exige pas de cotisations préalables de la part du bénéficiaire : le revenu de solidarité active ou l'allocation adulte handicapé en sont des exemples. Elle est generalement soumise à des conditions de résidence et de ressources, et relève d'une logique d'assistance et de solidarité nationale plutôt que d'un droit à retour sur cotisation. Cette distinction n'est pas seulement comptable : elle détermine l'organisme à saisir, les pièces à fournir, les délais et les voies de recours. Un professionnel de l'action sociale doit la maîtriser pour orienter correctement une personne, par exemple en expliquant qu'une demande de RSA relève du département alors qu'une demande d'indemnités journalières relève de la caisse primaire d'assurance maladie. Les deux catégories peuvent se combiner dans le parcours d'un même usager, et il faut vérifier les règles de cumul avant de conseiller une démarche.",
    "La réponse doit définir les deux catégories, donner deux exemples pertinents et montrer les conséquences pratiques de la distinction.")],
C("La protection sociale mutualise les risques : des cotisations financent des prestations, complétées par une solidarité publique.",
  "Prestations contributives = cotisations · non contributives = solidarité nationale",
  "Maladie · vieillesse · chômage · accidents du travail · famille",
  "Solidarité~Mutualisation des risques~Financement|Contributive~Financée par cotisations~Indemnités journalières|Non contributive~Financée par l'État~RSA, AAH",
  "Recenser les risques et les droits potentiels|Identifier l'organisme gestionnaire|Vérifier les conditions d'attribution|Rassembler les justificatifs|Accompagner la demande sans garantir la décision",
  "Confondre CAF, CNAM et Unédic|Promettre une prestation avant décision|Négliger les conditions de ressources|Ignorer les délais de carence",
  "Trois mois~Durée de l'arrêt~58 ans~Âge de la personne~MDPH~Dossier handicap~CCAS~Aide communale",
  "Contributive~Droit acquis par cotisation~Non contributive~Solidarité et conditions de ressources",
  "Maladie~Indemnités journalières~Chômage~Allocation de retour"),
UG)

# ============================================================ DR6
add("DR6.", "Droit de la famille et protection de l'enfance", "Droit", ["BTS2"],
S("Le droit de la famille organise les liens de parenté, le mariage, le divorce, la filiation et l'exercice de l'autorité parentale."
  "|L'autorité parentale est un ensemble de droits et de devoirs destinés à protéger l'enfant et à assurer son éducation."
  "|Elle appartient en principe aux deux parents, même après une séparation : la résidence de l'enfant ne prive pas l'autre parent de ses droits."
  "|Le juge aux affaires familiales statue sur la résidence, le droit de visite et d'hébergement, la pension alimentaire et les modalités d'exercice."
  "|L'intérêt supérieur de l'enfant est le critère directeur de toute décision le concernant, consacré par la Convention internationale des droits de l'enfant."
  "|Le divorce peut être prononcé pour faute, pour rupture de la vie commune, pour abandon de famille ou par consentement mutuel."
  "|Le divorce par consentement mutuel est en principe extrajudiciaire depuis 2017 : il est constaté par un acte notarié, sauf situations particulières."
  "|Une pension alimentaire peut être fixée pour contribuer à l'entretien et à l'éducation de l'enfant ; son non-paiement expose à des sanctions."
  "|La protection de l'enfance relève des conseils départementaux, qui organisent l'accueil, le suivi et les mesures d'accompagnement."
  "|L'ASE (aide sociale à l'enfance) peut proposer un accueil familial ou un placement en établissement lorsque la situation de l'enfant le nécessite."
  "|Le juge des enfants peut ordonner des mesures d'assistance éducative, comme un suivi par un éducateur ou un placement provisoire."
  "|Les professionnels sont tenus de signaler les situations de danger : la loi prévoit une obligation de signalement et protège le signalement de bonne foi."),
[QC("Quel critère guide les décisions concernant un enfant ?", "L'intérêt des parents~L'intérêt supérieur de l'enfant~Le coût de la mesure~L'avis du voisinage", 1,
    "L'intérêt supérieur de l'enfant est le principe directeur, consacré internationalement et en droit interne."),
 QC("Qui exerce l'autorité parentale en principe ?", "La mère seule~Le père seul~Les deux parents ensemble~Le juge des enfants", 2,
    "Les deux parents exercent l'autorité parentale, y compris après séparation."),
 QC("Quel juge statue sur la résidence d'un enfant après un divorce ?", "Le juge des enfants~Le juge aux affaires familiales~Le juge administratif~Le juge d'instruction", 1,
    "Le juge aux affaires familiales règle les modalités de la séparation et de l'exercice de l'autorité parentale."),
 QC("Depuis quelle réforme le divorce par consentement mutuel est-il en principe notarié ?", "2004~2017~2022~1993", 1,
    "La loi du 18 novembre 2016, applicable en 2017, a créé le divorce par consentement mutuel extrajudiciaire."),
 QC("Quel organisme gère l'aide sociale à l'enfance ?", "La CAF~Le conseil départemental~La mairie seulement~L'Éducation nationale", 1,
    "L'ASE est une compétence du conseil départemental."),
 QC("Quelle mesure relève de l'assistance éducative ?", "Une amende~Un suivi éducatif ordonné par le juge des enfants~Une saisie bancaire~Une expulsion", 1,
    "L'assistance éducative comprend des mesures de suivi et de placement ordonnées par le juge des enfants."),
 QC("Que doit faire un professionnel face à un danger pour un enfant ?", "Attendre une plainte~Signaler la situation aux autorités compétentes~En parler seulement à la famille~Publier les faits", 1,
    "Le signalement de bonne foi est une obligation et une protection pour le professionnel."),
 QT("Un parent refuse à l'autre l'exercice du droit de visite après une séparation. Quels principes et quelles démarches professionnelles sont concernés ?",
    "Le refus unilatéral du droit de visite méconnaît le principe de co-parentalité : l'autorité parentale appartient aux deux parents, et le parent chez qui l'enfant réside doit faciliter les relations avec l'autre, sauf motif grave et documenté. Si aucun jugement n'a fixé les modalités, la première démarche est de tenter une médiation familiale ou une concertation, éventuellement avec l'appui d'un service de médiation ou du CCAS. En cas d'échec, il faut saisir le juge aux affaires familiales, qui fixera un calendrier de rencontres, un droit d'hébergement et les modalités de communication, en tenant compte de l'âge de l'enfant et de son intérêt supérieur. Le professionnel ne prend pas parti : il écoute chaque parent, vérifie s'il existe des éléments de danger ou de violence qui justifieraient une protection, et oriente vers le juge ou le conseil départemental si la situation l'exige. Il conserve des traces datées des échanges, respecte la confidentialité et évite d'utiliser des termes qui discréditent l'un des parents. Si l'enfant exprime un refus, il faut l'entendre avec prudence, sans l'instrumentaliser, et transmettre son propos au juge si le conflit persiste.",
    "On attend le principe de co-parentalité, la médiation puis la saisine du juge aux affaires familiales, et une posture neutre et documentée."),
 QT("Distinguer l'aide sociale à l'enfance et l'assistance éducative, et préciser le rôle du professionnel dans chaque dispositif.",
    "L'aide sociale à l'enfance est un service public départemental qui intervient auprès des enfants et des familles en difficulté : il peut organiser un accompagnement à domicile, une mesure d'accueil familial ou un placement en établissement, et il suit la situation de l'enfant jusqu'à sa majorité. L'assistance éducative est une mesure judiciaire : le juge des enfants, saisi par le procureur, la famille ou un service, ordonne des interventions comme un suivi éducatif, une mesure d'aide à domicile ou un placement, pour une durée déterminée et révisable. Les deux dispositifs peuvent se combiner : un placement ASE peut être ordonné par le juge dans le cadre de l'assistance éducative, et le département en assure alors l'exécution matérielle. Le rôle du professionnel diffère selon le cadre : dans l'ASE, il accompagne la famille dans un objectif de soutien et de préparation de la sortie, en lien avec le service référent ; dans l'assistance éducative, il rend des comptes au juge, respecte le mandat confié et doit documenter ses observations. Dans les deux cas, il reste attentif à la parole de l'enfant, à la place de la famille et à la continuité des liens, tout en appliquant les règles de signalement et de confidentialité. Sa posture n'est jamais celle d'un juge : il observe, accompagne et transmet.",
    "La réponse doit opposer dispositif départemental et mesure judiciaire, puis décrire le rôle professionnel dans chacun.")],
C("Le droit de la famille protège l'enfant : autorité parentale partagée, intérêt supérieur, intervention du juge et du département.",
  "Autorité parentale = droits et devoirs des deux parents",
  "Juge aux affaires familiales · juge des enfants · conseil départemental · ASE",
  "Autorité parentale~Droits et devoirs~Deux parents|Intérêt supérieur~Critère directeur~Convention internationale|ASE~Service départemental~Accueil et suivi",
  "Écouter chaque parent et l'enfant|Repérer un éventuel danger|Rechercher une solution amiable|Orienter vers le juge ou l'ASE si nécessaire|Documenter et respecter la confidentialité",
  "Prendre parti dans un conflit parental|Ignorer la parole de l'enfant|Confondre juge aux affaires familiales et juge des enfants|Négliger le signalement d'un danger",
  "2017~Divorce notarié~ASE~Aide sociale à l'enfance~Juge des enfants~Assistance éducative~Deux parents~Co-parentalité",
  "ASE~Dispositif départemental~Assistance éducative~Mesure judiciaire",
  "Droit de visite~Rencontre avec l'enfant~Droit d'hébergement~Accueil temporaire"),
"Code civil, loi sur la protection de l'enfance et programmes applicables en BTS, référentiel BTS ESF 2022")

# ============================================================ DR7
add("DR7.", "Données personnelles, RGPD et secret professionnel", "Droit", ["BTS2"],
S("Une donnée personnelle est toute information relative à une personne physique identifiée ou identifiable, directement ou indirectement."
  "|Le règlement général sur la protection des données (RGPD), applicable depuis 2018, encadre le traitement de ces données dans l'Union européenne."
  "|La loi informatique et libertés du 6 janvier 1978, modifiée, complète le RGPD en droit français ; la CNIL en assure le contrôle."
  "|Un traitement de données doit reposer sur une base légale : consentement, exécution d'un contrat, obligation légale, intérêt vital, mission d'intérêt public ou intérêt légitime."
  "|Les principes fondamentaux sont la licéité, la loyauté, la transparence, la finalité déterminée, la minimisation et l'exactitude des données."
  "|La minimisation impose de ne collecter que les données nécessaires à la finalité poursuivie, ni plus ni moins."
  "|La durée de conservation doit être limitée : une donnée qui n'est plus utile doit être supprimée ou anonymisée."
  "|Les personnes disposent de droits : accès, rectification, effacement, limitation, opposition et portabilité, dans les conditions prévues par le règlement."
  "|Une violation de données doit être notifiée à la CNIL dans les 72 heures suivant sa prise de connaissance, et aux personnes si le risque est élevé."
  "|Le secret professionnel impose aux professionnels de ne pas divulguer les informations-confidentielles reçues dans l'exercice de leur mission."
  "|Le secret professionnel est une obligation déontologique et pénale, avec des exceptions légales : danger pour la personne, consentement, obligation de signalement."
  "|Le partage d'informations entre professionnels doit être limité au nécessaire, tracé et conforme au cadre légal, notamment pour la protection de l'enfance."),
[QC("Depuis quand le RGPD est-il applicable ?", "2016~2018~2020~2004", 1,
    "Le RGPD est applicable depuis le 25 mai 2018."),
 QC("Quelle autorité contrôle la protection des données en France ?", "La CNIL~La CNAM~La CADA~Le Défenseur des droits", 0,
    "La Commission nationale de l'informatique et des libertés contrôle l'application du RGPD en France."),
 QC("Quel principe impose de ne collecter que les données nécessaires ?", "La transparence~La minimisation~La portabilité~La conservation illimitée", 1,
    "La minimisation limite la collecte aux données strictement nécessaires à la finalité."),
 QC("Quel délai pour notifier une violation de données à la CNIL ?", "24 heures~72 heures~7 jours~30 jours", 1,
    "L'article 33 du RGPD prévoit une notification dans les 72 heures après prise de connaissance."),
 QC("Quel droit permet à une personne d'obtenir une copie de ses données ?", "Le droit d'effacement~Le droit d'accès~Le droit d'opposition~Le droit à l'oubli", 1,
    "Le droit d'accès permet de connaître et d'obtenir copie des données traitées."),
 QC("Le secret professionnel est-il absolu ?", "Oui, toujours~Non, il connaît des exceptions légales~Non, il disparaît en cas de demande d'un collègue~Oui, sauf pour la famille", 1,
    "Des exceptions existent, notamment le danger pour la personne ou l'obligation de signalement."),
 QC("Quelle est une base légale d'un traitement de données ?", "L'habitude de l'équipe~Le consentement ou une obligation légale~La curiosité d'un agent~Une demande verbale", 1,
    "Le traitement doit reposer sur l'une des bases légales énumérées par le RGPD."),
 QT("Un professionnel souhaite transmettre à un partenaire les coordonnées et la situation d'un usager pour organiser une prise en charge. Définissez les conditions de ce partage.",
    "Le partage doit être préalablement vérifié sur quatre points. D'abord, la finalité : organiser la prise en charge de la personne est un objectif légitime, mais encore faut-il que le partenaire ait besoin de ces informations pour sa mission. Ensuite, la base légale : dans le secteur social, elle repose le plus souvent sur l'exécution d'une mission d'intérêt public ou sur une obligation légale de coopération, rarement sur le seul consentement, qui peut être fragile dans une relation d'aide. Troisièmement, la minimisation : je transmets uniquement les données nécessaires, par exemple les coordonnées et la nature du besoin d'accompagnement, et non l'intégralité du dossier ni des informations de santé sans lien avec la finalité. Je vérifie la durée de conservation et les mesures de sécurité du canal utilisé : messagerie sécurisée ou plateforme partagée plutôt qu'un courriel ordinaire ou une clé USB. Quatrièmement, je respecte le secret professionnel et je trace le partage dans le dossier : date, destinataire, données transmises et motif. J'informe l'usager, dans un langage compréhensible, des données échangées et de ses droits d'accès et d'opposition, conformément au RGPD. En cas de danger ou de protection de l'enfance, les règles de signalement priment, mais le principe de nécessité reste applicable.",
    "On attend finalité, base légale, minimisation, sécurité du canal, traçabilité et information de la personne."),
 QT("Expliquer la différence entre secret professionnel et obligation de signalement, et montrer comment un professionnel peut concilier les deux.",
    "Le secret professionnel interdit la divulgation des informations confiées dans le cadre de la mission : il protège la confidentialité de la relation et la dignité de la personne. Son non-respect expose à des sanctions pénales et disciplinaires. L'obligation de signalement impose, dans certaines situations, de transmettre des informations aux autorités compétentes : c'est le cas lorsque la vie ou l'intégrité d'une personne est en danger, en particulier pour un mineur ou une personne vulnérable, ou lorsque la loi le prévoit expressément. La conciliation repose sur plusieurs règles. Le signalement doit être limité aux faits nécessaires à l'appréciation de la situation, adressé uniquement aux autorités habilitées, et realisé dans les plus brefs délais. Il ne s'agit pas de transmettre un dossier complet ni d'informer toute l'équipe ou l'entourage. Le professionnel consigne son action et sa motivation, ce qui le protège en cas de contrôle. Lorsque la situation le permet, il informe la personne concernée de la démarche, sauf si cette information risque d'aggraver le danger. Enfin, le signalement de bonne foi, sans faute ni intention de nuire, est protégé par la loi : le professionnel ne doit pas le confondre avec une dénonciation publique. Ainsi, le secret reste la règle, le signalement l'exception encadrée, et la traçabilité permet de démontrer que l'exception était justifiée.",
    "On attend la définition des deux notions, la limitation du signalement aux faits nécessaires, la notification aux seules autorités habilitées et la protection du signalement de bonne foi.")],
C("Les données des usagers sont protégées : finalité, minimisation, sécurité, droits de la personne et secret professionnel encadré.",
  "RGPD : licéité · minimisation · durée limitée · droits",
  "Violation : notification CNIL sous 72 h · secret professionnel avec exceptions légales",
  "Donnée personnelle~Information sur une personne~Identifiable|Minimisation~Données nécessaires seulement~Réduction|Signalement~Exception encadrée~Danger",
  "Identifier la finalité du traitement|Vérifier la base légale|Limiter les données transmises|Sécuriser le canal et tracer|Informer la personne de ses droits",
  "Transmettre un dossier complet par courriel|Conserver une donnée indéfiniment|Confondre secret et silence absolu|Oublier de tracer le partage",
  "2018~Application du RGPD~72 heures~Notification CNIL~CNIL~Autorité de contrôle~Minimisation~Principe clé",
  "Secret professionnel~Règle générale~Signalement~Exception légale",
  "Droit d'accès~Obtenir copie~Droit d'effacement~Supprimer ses données"),
"Règlement (UE) 2016/679 (RGPD), loi du 6 janvier 1978 modifiée et programmes applicables en BTS, référentiel BTS ESF 2022")

# ============================================================ EC1
add("EC1.", "Besoins, biens et ressources rares", "Économie", ["BTS1"],
S("L'économie étudie la façon dont les sociétés utilisent des ressources rares pour satisfaire des besoins qui sont, eux, illimités."
  "|Un besoin est un manque ressenti par un individu : il est physiologique, psychologique ou social et se renouvelle au fil du temps."
  "|Un désir est un besoin orienté vers un objet précis, influencé par la culture, la publicité et le revenu."
  "|La rareté caractérise une ressource dont la quantité disponible est inférieure à ce que les individus souhaiteraient en consommer."
  "|Le coût d'opportunité d'un choix est la meilleure alternative à laquelle on renonce : il mesure le prix réel d'une décision."
  "|Un bien est un objet ou un service qui satisfait un besoin ; on distingue les biens privés, rivaux et exclusifs, et les biens publics."
  "|Un bien rival est dont la consommation par une personne réduit la quantité disponible pour les autres ; un bien non rival peut être consommé par tous."
  "|L'exclusivité désigne la possibilité d'empêcher une personne de consommer le bien, par exemple par le prix ou un accès contrôlé."
  "|Les biens publics, comme l'éclairage public, sont non rivaux et non exclusifs : leur financement relève souvent de l'impôt."
  "|Les biens communs, comme une ressource naturelle partagée, sont rivaux mais difficiles à exclure : ils exposent au risque de surconsommation."
  "|La production combine des facteurs de production : travail, capital, terre et, dans l'analyse moderne, l'innovation et l'information."
  "|Ces notions permettent de comprendre les arbitrages des ménages, des entreprises et des politiques publiques, y compris dans l'action sociale."),
[QC("Quelle est la définition de la rareté ?", "Une ressource gratuite~Une quantité disponible inférieure aux souhaits de consommation~Un bien interdit~Un prix trop élevé", 1,
    "La rareté est l'écart entre les ressources disponibles et les désirs de consommation."),
 QC("Qu'est-ce que le coût d'opportunité ?", "Le prix affiché d'un produit~La meilleure alternative à laquelle on renonce~Le coût de production d'une entreprise~Le montant de l'impôt", 1,
    "Le coût d'opportunité mesure la valeur de l'option non retenue."),
 QC("Quel bien est non rival et non exclusif ?", "Un sandwich~L'éclairage public~Une place de cinéma~Un vêtement", 1,
    "L'éclairage public peut bénéficier à tous sans priver autrui de sa consommation."),
 QC("Quel facteur de production correspond aux machines et aux équipements ?", "Le travail~Le capital~La terre~La consommation", 1,
    "Le capital désigne les biens durables utilisés pour produire."),
 QC("Quel est un exemple de bien commun ?", "Un pain~Une ressource naturelle partagée~Un abonnement privé~Une voiture individuelle", 1,
    "Les biens communs sont rivaux mais difficiles à exclure, ce qui pose un problème de gestion."),
 QC("Quelle différence entre besoin et désir ?", "Aucune~Le désir est un besoin orienté vers un objet précis~Le besoin est toujours futile~Le désir est toujours physiologique", 1,
    "Le besoin est un manque général ; le désir lui donne une forme et un objet."),
 QC("Pourquoi un bien rival pose-t-il un problème d'allocation ?", "Parce qu'il est gratuit~Parce que sa consommation par l'un prive les autres~Parce qu'il est illimité~Parce qu'il n'a pas de prix", 1,
    "La rivalité impose de répartir le bien entre les usagers potentiels."),
 QT("Un ménage dispose de 300 euros pour se chauffer ou cuisiner en fin de mois. Expliquez le raisonnement économique en termes de besoins, de coût d'opportunité et d'arbitrage.",
    "Le ménage fait face à des besoins illimités : se chauffer, manger, se déplacer, communiquer. Avec 300 euros, il ne peut satisfaire que certains d'entre eux : c'est la rareté de la ressource financière. Le raisonnement commence par hiérarchiser les besoins : se nourrir est un besoin physiologique prioritaire, mais le froid peut également devenir un risque pour la santé, surtout pour des personnes âgées ou des enfants. Le coût d'opportunité du choix du chauffage est la qualité et la quantité d'aliments auxquelles le ménage renonce, et inversement. L'arbitrage consiste à comparer les effets respectifs des deux dépenses, à rechercher des solutions qui réduisent le coût de l'un des besoins : isolation, application d'aides, achat groupé, repas préparés à moindre coût, tarif social de l'énergie. Le ménage peut aussi étaler ses dépenses dans le temps ou recourir à un dispositif d'aide, ce qui modifie l'ensemble des contraintes. La décision finale n'est pas seulement un calcul : elle dépend des préférences, de l'information disponible et des aides dont le ménage a connaissance. Le rôle d'un professionnel de l'action sociale est précisément d'améliorer cette information et d'élargir l'éventail des options, plutôt que de décider à la place du ménage.",
    "On attend la mobilisation des notions de besoin, rareté, coût d'opportunité et arbitrage, et une solution réaliste d'accompagnement."),
 QT("Distinguer bien privé, bien public et bien commun, et expliquer pourquoi leur mode de financement diffère.",
    "Un bien privé est rival et exclusif : si je mange un pain, personne ne peut le manger à ma place, et le vendeur peut refuser la vente à qui ne paie pas. Son financement par le prix est donc efficace, car le marché peut exclure les non-payants. Un bien public est non rival et non exclusif : l'éclairage public profite à tous et l'on ne peut empêcher un passant d'en bénéficier. Comme personne n'a intérêt à le financer seul, le financement repose sur l'impôt et la décision publique ; c'est le problème du passager clandestin. Un bien commun, comme un puits partagé ou un pâturage collectif, est rival mais difficile à exclure : chacun peut y accéder, mais la consommation de l'un réduit la disponibilité pour les autres. Son financement et sa gestion exigent des règles collectives, une régulation ou une tarification d'accès pour éviter l'épuisement de la ressource, ce que l'économiste Garrett Hardin a appelé la tragédie des biens communs. Ces trois catégories ne sont pas des types de produits absolus : un même bien peut changer de statut selon la technologie ou les règles, par exemple une autoroute devient non rival quand elle n'est pas saturée, puis redevient rivale aux heures de pointe.",
    "La réponse doit définir les trois catégories par la rivalité et l'exclusivité, puis justifier le mode de financement de chacune.")],
C("L'économie part d'un arbitre fondamental : des besoins illimités face à des ressources rares, d'où le coût d'opportunité.",
  "Rareté → choix → coût d'opportunité",
  "Bien privé : rival et exclusif · bien public : non rival et non exclusif · bien commun : rival et peu exclusif",
  "Besoin~Manque ressenti~Illimité|Rareté~Ressources limitées~Arbitrage|Coût d'opportunité~Alternative sacrifiée~Choix",
  "Identifier le besoin à satisfaire|Mesurer les ressources disponibles|Comparer les alternatives possibles|Choisir en connaissant le coût d'opportunité|Évaluer le résultat de l'arbitrage",
  "Confondre besoin et désir|Ignorer le coût d'opportunité|Croire qu'un bien public est financé par le marché|Négliger les biens communs",
  "300 euros~Ressource du ménage~Chauffage et cuisine~Arbitrage~Éclairage public~Bien public~Puits partagé~Bien commun",
  "Bien privé~Rival et exclusif~Bien public~Non rival et non exclusif",
  "Rareté~Quantité limitée~Coût d'opportunité~Valeur de l'alternative"),
UG)

# ============================================================ EC2
add("EC2.", "Offre, demande et fonctionnement d'un marché", "Économie", ["BTS1"],
S("Un marché est un lieu ou un mécanisme de rencontre entre l'offre des producteurs et la demande des consommateurs."
  "|La demande exprime les quantités d'un bien que les consommateurs sont disposés et capables d'acheter à différents prix."
  "|Selon la loi de la demande, lorsque le prix augmente, la quantité demandée diminue, toutes choses égales par ailleurs."
  "|L'offre exprime les quantités que les producteurs sont disposés et capables de vendre à différents prix."
  "|Selon la loi de l'offre, lorsque le prix augmente, la quantité offerte augmente, car la production devient plus rentable."
  "|Le prix d'équilibre est le prix auquel la quantité offerte égale la quantité demandée : le marché s'y stabilise temporairement."
  "|Un excédent apparaît si le prix est supérieur à l'équilibre : l'offre dépasse la demande et les vendeurs sont incités à baisser leurs prix."
  "|Une pénurie apparaît si le prix est inférieur à l'équilibre : la demande dépasse l'offre et les acheteurs se disputent le produit."
  "|La demande peut varier pour des raisons autres que le prix : revenu, goûts, prix des autres biens, démographie, attentes."
  "|L'offre peut varier à la suite d'un changement de coût de production, de technologie, du nombre de producteurs ou de réglementation."
  "|L'élasticité-prix de la demande mesure la sensibilité de la quantité demandée à une variation de prix : un bien très élastique voit sa demande fortement baisser quand le prix monte."
  "|Les prix ne sont pas toujours libres : un prix plafond peut protéger les consommateurs, un prix plancher peut protéger les producteurs, au risque de pénurie ou d'excédent."),
[QC("Que se passe-t-il quand le prix est supérieur au prix d'équilibre ?", "Une pénurie~Un excédent de l'offre~Une disparition du marché~Une hausse automatique du prix", 1,
    "À un prix trop élevé, l'offre dépasse la demande : il apparaît un excédent."),
 QC("Quelle est la relation entre prix et quantité demandée ?", "Positive~Inverse~Nulle~Aléatoire", 1,
    "Quand le prix augmente, la quantité demandée baisse en général : la relation est inverse."),
 QC("Quel facteur décale la courbe de demande ?", "Une variation du prix du bien~Une variation du revenu des consommateurs~Une variation de la quantité offerte~Une variation du coût de production", 1,
    "Le revenu est un facteur externe qui décale la demande ; le prix fait seulement glisser le long de la courbe."),
 QC("Qu'est-ce qu'un prix plancher ?", "Un prix maximum autorisé~Un prix minimum imposé~Un prix d'équilibre~Un prix négocié", 1,
    "Le prix plancher fixe un minimum, par exemple le SMIC sur le marché du travail."),
 QC("Que mesure l'élasticité-prix de la demande ?", "Le coût de production~La sensibilité de la demande à une variation de prix~La durée de vie du produit~Le nombre de vendeurs", 1,
    "L'élasticité compare la variation relative des quantités à celle du prix."),
 QC("Une hausse du coût des matières premières déplace quelle courbe ?", "La demande~L'offre~Les deux~Aucune", 1,
    "Une hausse de coût réduit l'offre à chaque prix : la courbe d'offre se déplace."),
 QC("Quel marché se rapproche le plus de la concurrence pure et parfaite ?", "Un monopole~Un marché avec de nombreux offreants et un produit homogène~Une situation de penetration~Un marché très réglementé", 1,
    "La concurrence suppose de nombreux acteurs, des produits comparables, une information accessible et une libre entrée."),
 QT("Le prix d'une place de cinéma augmente de 20 % et la fréquentation baisse de 10 %. Calculez l'élasticité-prix et interprétez le résultat pour le gestionnaire.",
    "L'élasticité-prix de la demande se calcule en divisant la variation relative de la quantité demandée par la variation relative du prix : ici, −10 % / +20 % = −0,5. La valeur absolue, 0,5, est inférieure à 1 : la demande est inélastique. En pratique, une hausse de prix de 1 % entraîne une baisse de la fréquentation de 0,5 % seulement. Pour le gestionnaire, l'augmentation du prix est favorable à la recette totale si les coûts par place restent constants : la recette par séance évolue selon (1,20 × 0,90) = 1,08, soit une hausse d'environ 8 %. Mais cette conclusion doit être nuancée : l'élasticité peut varier selon le public, le créneau horaire et l'existence de substituts, et une baisse de fréquentation peut réduire les ventes annexes (boissons, confiseries). Le gestionnaire doit aussi tenir compte de l'objectif social et culturel de l'établissement : une hausse trop forte peut exclure les publics les plus fragiles. Une meilleure stratégie pourrait consister à moduler les prix par tranche horaire ou par catégorie de spectateurs, plutôt que d'augmenter uniformément le tarif.",
    "On attend le calcul (−0,5), l'interprétation en termes de demande inélastique et une discussion de la recette et des effets sociaux."),
 QT("Expliquer pourquoi un prix plafond peut provoquer une pénurie, puis donner un exemple dans le secteur du logement.",
    "Un prix plafond interdit de vendre au-dessus d'un certain montant. Si ce plafond est fixé sous le prix d'équilibre, la quantité demandée à ce prix devient supérieure à la quantité offerte : les propriétaires acceptent moins de louer à un prix qu'ils jugent insuffisant, tandis que davantage de locataires souhaitent en profiter. Cette situation crée une pénurie, avec des listes d'attente, un rationnement ou un développement du marché parallèle. Dans le logement, un encadrement des loyers peut rendre des logements accessibles à des ménages qui en étaient exclus, ce qui est son objectif ; mais s'il est trop strict et non accompagné, il peut décourager la mise en location ou l'entretien des biens, réduisant l'offre disponible. L'effet dépend donc du niveau du plafond, de la réaction des bailleurs et des mesures complémentaires : aides à la rénovation, construction de logements sociaux, garanties locatives. Un autre effet pervers est la sélection des locataires par des critères non tarifaires. Les économistes ne concluent pas pour autant à l'inutilité de l'encadrement : ils soulignent qu'il doit être évalué avec des indicateurs d'offre, de durée de vacance et d'accès réel des ménages modestes, plutôt qu'apprécié seulement à l'aune du loyer affiché.",
    "On attend la mécanisme offre/demande sous le prix d'équilibre, un exemple de logement et des effets pervers possibles avec nuance.")],
C("Le marché confronte offre et demande : le prix d'équilibre les harmonise, mais les variations de l'environnement les déplacent.",
  "Prix d'équilibre : quantité offerte = quantité demandée",
  "Élasticité = variation % quantité / variation % prix",
  "Demande~Quantité souhaitée~Loi inverse du prix|Offre~Quantité proposée~Loi directe du prix|Équilibre~Offre égale demande~Prix de rencontre",
  "Repérer les facteurs qui ont changé|Identifier la courbe déplacée|Comparer offre et demande au prix considéré|Calculer l'élasticité si besoin|Anticiper excédent ou pénurie",
    "Confondre déplacement le long d'une courbe et décalage de la courbe|Oublier le signe négatif de l'élasticité|Croire qu'un prix plafond augmente l'offre|Ignorer les effets indirects sur les autres marchés",
  "20 %~Hausse du prix~10 %~Baisse de fréquentation~Élasticité 0,5~Demande inélastique~Prix plafond~Risque de pénurie",
  "Excédent~Prix trop élevé~Pénurie~Prix trop bas",
  "Variation du prix~Glissement sur la courbe~Variation du revenu~Décalage de la courbe"),
UG)

# ============================================================ EC3
add("EC3.", "Monnaie, inflation et pouvoir d'achat", "Économie", ["BTS1"],
S("La monnaie est un bien généralement accepté pour régler des transactions : elle sert d'intermédiaire des échanges, d'unité de compte et de réserve de valeur."
  "|Les trois fonctions de la monnaie sont : moyen de paiement, unité de mesure des prix et conservation de la valeur dans le temps."
  "|La monnaie fiduciaire comprend les billets et les pièces ; la monnaie scripturale correspond aux dépôts bancaires utilisés par virement, carte ou chèque."
  "|La masse monétaire désigne l'ensemble des moyens de paiement en circulation à un moment donné."
  "|L'inflation est une hausse généralisée et durable du niveau des prix, mesurée par un indice des prix à la consommation."
  "|Un taux d'inflation de 3 % signifie qu'en moyenne les prix ont augmenté de 3 % sur la période considérée, généralement un an."
  "|La désinflation désigne un ralentissement du rythme de hausse des prix : les prix augmentent toujours, mais plus lentement."
  "|La déflation est une baisse généralisée et durable des prix, souvent associée à une baisse de la demande et à un risque de récession."
  "|Le pouvoir d'achat mesure la quantité de biens et de services qu'un revenu permet d'acheter : il baisse quand les prix montent plus vite que les revenus."
  "|L'indice des prix est calculé à partir d'un panier de biens et de services représentatif des dépenses des ménages, avec des pondérations."
  "|La Banque centrale européenne vise une inflation de 2 % à moyen terme ; elle agit principalement par ses taux d'intérêt directeurs."
  "|Une hausse des taux rend le crédit plus cher, ce qui freine l'investissement et la consommation, mais peut aussi ralentir l'activité économique."),
[QC("Quelle est une fonction de la monnaie ?", "Uniquement moyen de paiement~Unité de compte, moyen de paiement et réserve de valeur~Réserver les bénéfices~Fixer les salaires", 1,
    "La monnaie remplit trois fonctions classiques : intermédiaire des échanges, unité de compte et réserve de valeur."),
 QC("Quel est un exemple de monnaie scripturale ?", "Un billet de 20 euros~Un virement bancaire~Une pièce de 1 euro~Un lingot", 1,
    "La monnaie scripturale circule par écritures bancaires : virement, carte, chèque."),
 QC("Que mesure l'indice des prix à la consommation ?", "Le nombre de produits disponibles~La variation moyenne du prix d'un panier de biens et services~Le salaire moyen~Le taux de chômage", 1,
    "L'INSEE calcule l'IPC à partir d'un panier pondéré représentatif des dépenses des ménages."),
 QC("Quelle situation correspond à une désinflation ?", "Les prix baissent~Les prix augmentent moins vite qu'avant~Les prix stagnent~Les prix augmentent plus vite", 1,
    "La désinflation est un ralentissement du rythme d'inflation, pas une baisse des prix."),
 QC("Quel est l'objectif d'inflation de la Banque centrale européenne à moyen terme ?", "0 %~2 %~5 %~10 %", 1,
    "La BCE vise un taux d'inflation de 2 % à moyen terme."),
 QC("Quel effet a une hausse des taux directeurs sur le crédit ?", "Il devient moins cher~Il devient plus cher~Il disparaît~Il n'a aucun effet", 1,
    "Une hausse des taux renchérit le coût du crédit et tend à freiner la demande."),
 QC("Quand le pouvoir d'achat baisse-t-il ?", "Quand les prix baissent~Quand les prix augmentent plus vite que les revenus~Quand les revenus stagnent et les prix baissent~Quand l'inflation est nulle", 1,
    "Le pouvoir d'achat recule si la hausse des prix dépasse celle du revenu."),
 QT("Un ménage percevait 2 000 euros de revenu mensuel l'an dernier ; il perçoit 2 040 euros cette année, tandis que les prix ont augmenté de 3 %. Calculez l'évolution de son pouvoir d'achat et commentez.",
    "Le revenu nominal progresse de 40 euros, soit 40 / 2 000 = 2 %. Les prix ont augmenté de 3 %. Le revenu réel, c'est-à-dire le revenu corrigé de l'inflation, évolue approximativement de 2 % − 3 % = −1 % ; le calcul exact donne 1,02 / 1,03 = 0,9903, soit une baisse d'environ 0,97 %. Le pouvoir d'achat du ménage a donc légèrement diminué : avec ses 2 040 euros, il peut acheter un peu moins de biens et services que l'an dernier avec 2 000 euros. Le montant sur le compte a augmenté, mais la quantité de biens accessibles a reculé. Pour retrouver son pouvoir d'achat initial, le ménage aurait dû recevoir au moins 2 000 × 1,03 = 2 060 euros, soit 60 euros de plus qu'auparavant et 20 euros de plus que ce qu'il a obtenu. Cette situation est fréquente lorsque les négociations salariales prennent du retard sur l'inflation. Un professionnel peut aider le ménage en recherchant des aides, en comparant les tarifs et en l'informant des dispositifs d'accompagnement, mais il ne doit pas confondre hausse nominale et gain réel.",
    "On attend le calcul de la hausse nominale (2 %), la comparaison avec 3 %, l'évolution réelle d'environ −1 % et le revenu de compensation (2 060 euros)."),
 QT("Distinguer inflation, désinflation et déflation, puis expliquer pourquoi la déflation peut être dangereuse pour l'activité économique.",
    "L'inflation est une hausse généralisée et durable du niveau des prix ; la désinflation est un ralentissement de cette hausse, les prix continuant d'augmenter à un rythme plus faible ; la déflation est une baisse généralisée et durable des prix. Ces trois situations se mesurent avec le même indice des prix, mais elles n'ont pas les mêmes effets. Une inflation modérée est considérée comme normale dans une économie en croissance : elle accompagne la hausse des coûts et permet des ajustements relatifs des prix. Une inflation forte érode le pouvoir d'achat et rend les prix moins lisibles, ce qui nuit aux décisions d'investissement et pénalise les ménages dont les revenus suivent avec retard. La déflation, malgré l'apparence attrayante de prix qui baissent, est redoutée des économistes : lorsqu'ils anticipent de nouvelles baisses, les consommateurs reportent leurs achats et les entreprises réduisent leur production et leurs investissements, ce qui alimente le chômage et la baisse des salaires. La valeur réelle des dettes augmente, alourdissant la charge des emprunteurs. Les banques centrales surveillent donc ces trois situations et adaptent leurs taux pour maintenir la stabilité des prix, objectif qui contribue à la stabilité de l'activité et de l'emploi.",
    "On attend trois définitions précises et une explication du cercle vicieux déflationniste (report des achats, baisse de production et de l'emploi).")],
C("La monnaie mesure et transmet la valeur ; l'inflation érode le pouvoir d'achat quand les prix montent plus vite que les revenus.",
  "Revenu réel ≈ revenu nominal / indice des prix",
  "Inflation : hausse des prix · désinflation : ralentissement · déflation : baisse",
  "Monnaie~Moyen de paiement~Trois fonctions|Inflation~Hausse durable des prix~Indice IPC|Pouvoir d'achat~Biens accessibles~Revenu réel",
  "Repérer l'évolution des prix et des revenus|Calculer le taux d'inflation|Comparer hausse nominale et hausse réelle|Analyser les effets sur le budget|Envisager les aides et arbitrages possibles",
  "Confondre désinflation et déflation|Croire qu'une hausse de salaire accroît toujours le pouvoir d'achat|Oublier la pondération du panier de l'IPC|Ignorer l'effet des taux sur le crédit",
  "2 000 euros~Revenu initial~2 040 euros~Revenu nominal~3 %~Inflation~2 060 euros~Revenu compensatoire~2 %~Objectif BCE",
  "Inflation~Prix en hausse~Déflation~Prix en baisse",
  "Nominal~Montant affiché~Réel~Montant corrigé des prix"),
UG)

# ============================================================ EC4
add("EC4.", "Budget des ménages, consommation et surendettement", "Économie", ["BTS1"],
S("Le budget d'un ménage retrace ses ressources et ses emplois sur une période donnée, généralement un mois ou une année."
  "|Les ressources comprennent les salaires, les prestations sociales, les pensions, les revenus fonciers et les éventuels revenus complémentaires."
  "|Les emplois se divisent en dépenses contraintes, comme le logement et l'énergie, et dépenses libres, comme les loisirs ou l'épargne."
  "|L'épargne est la partie du revenu qui n'est pas consommée : elle constitue une réserve pour les imprévus ou un projet futur."
  "|La propension à consommer désigne la part du revenu consacrée à la consommation ; elle dépend notamment du niveau de revenu."
  "|La consommation est influencée par le revenu disponible, les prix, les attentes, les goûts et l'information dont dispose le ménage."
  "|Un crédit permet d'acheter un bien immédiatement en remboursant plus tard, mais il engage l'avenir et_SUPPORTSUPPORT entraîne un coût (intérêts, assurance)."
  "|Le taux d'endettement rapporte les mensualités de crédit au revenu : un taux élevé réduit la capacité de remboursement en cas d'imprévu."
  "|Le surendettement est une situation dans laquelle un ménage ne peut plus honorer ses dettes et faire face à ses dépenses essentielles."
  "|La Banque de France instruit les dossiers de surendettement et peut proposer un plan de remboursement, une réduction ou une effacement partiel des dettes."
  "|Le premier réflexe face à une difficulté budgétaire est de faire le point : recenser les dettes, les échéances, les ressources et les dépenses prioritaires."
  "|L'accompagnement budgétaire proposé par les services sociaux vise à restaurer l'autonomie de la personne, sans se substituer à elle dans ses choix."),
[QC("Quel est un exemple de dépense contrainte ?", "Une sortie au cinéma~Le loyer du logement~Un achat de vêtement non nécessaire~Un abonnement loisir", 1,
    "Le logement est une dépense contrainte, difficilement réductible à court terme."),
 QC("Que désigne la propension à consommer ?", "La part du revenu consacrée à l'épargne~La part du revenu consacrée à la consommation~Le montant des dettes~Le taux d'imposition", 1,
    "C'est la fraction du revenu utilisée pour consommer plutôt que pour épargner."),
 QC("Quel organisme instruit les dossiers de surendettement ?", "La CAF~La Banque de France~Le tribunal de commerce~La CNIL", 1,
    "La Banque de France, via ses commissions de surendettement, traite les dossiers."),
 QC("Quel est un coût du crédit à la consommation ?", "La seule durée du prêt~Les intérêts et les frais d'assurance~La valeur du bien acheté~Le salaire de l'emprunteur", 1,
    "Le crédit a un coût financier : intérêts, frais de dossier et assurances éventuelles."),
 QC("Que mesure le taux d'endettement ?", "Le rapport entre mensualités et revenu~Le prix d'un bien~La durée d'un contrat~Le montant de l'épargne", 0,
    "Il rapporte les charges de remboursement au revenu disponible du ménage."),
 QC("Quelle est la première étape face à une difficulté budgétaire ?", "Contracter un nouveau crédit~Recenser dettes, ressources et dépenses~Attendre l'échéance~Vendre tous ses biens", 1,
    "Un état des lieux complet est indispensable avant toute décision."),
 QC("Quel objectif de l'accompagnement budgétaire ?", "Décider à la place de l'usager~Restaurer son autonomie dans la gestion~Supprimer toutes ses dépenses~Annuler ses dettes automatiquement", 1,
    "L'accompagnement vise l'autonomie et la capacité de décision de la personne."),
 QT("Un ménage a 1 800 euros de ressources mensuelles, 700 euros de loyer, 180 euros d'énergie, 250 euros de remboursements de crédit et 450 euros d'alimentation. Calculez le solde et proposez une analyse.",
    "Les dépenses identifiées totalisent 700 + 180 + 250 + 450 = 1 580 euros. Le solde avant autres dépenses est donc de 1 800 − 1 580 = 220 euros. Ce montant doit encore couvrir les transports, les assurances, la santé, les frais de scolarité, la communication et les imprévus, ce qui laisse une marge très faible, voire négative. Le taux d'endettement, calculé sur les seules mensualités de crédit, est de 250 / 1 800 = 13,9 %, ce qui paraît modéré, mais il ne tient pas compte des dépenses contraintes : le loyer et l'énergie représentent à eux seuls 880 euros, soit près de 49 % des ressources. Le ménage est donc exposé à un risque de fragilité plus grande que ne le laisse penser le seul taux d'endettement. L'analyse doit aussi porter sur la nature du crédit : taux, durée restante, assurance, possibilité de report d'échéance. Les pistes d'action consistent à rechercher des aides au logement non demandées, à comparer les offres d'énergie et d'assurance, à renégocier le crédit si cela est possible, à constituer une petite épargne de précaution dès qu'un excédent apparaît, et à construire un budget prévisionnel réaliste. Un professionnel peut aider à dresser ce tableau et à hiérarchiser les priorités, mais il laisse le ménage décider de ses arbitrages.",
    "On attend le calcul du solde (220 euros), celui du taux d'endettement (environ 14 %), l'analyse des dépenses contraintes et des pistes d'action concrètes."),
 QT("Expliquer la différence entre surendettement et simple difficulté de trésorerie, et décrire le parcours de traitement d'un dossier de surendettement.",
    "Une difficulté de trésorerie est un décalage temporaire entre les recettes et les dépenses : le ménage dispose de ressources suffisantes sur la durée, mais un imprévu, une facture inhabituelle ou un retard de paiement crée une tension ponctuelle. Le surendettement est plus grave : il caractérise un ménage qui n'est plus capable de faire face à ses dettes et à ses dépenses essentielles, même en réajustant son budget, et dont la situation risque de s'aggraver. Le dépôt d'un dossier auprès de la Banque de France peut être réalisé par le ménage lui-même ou par un professionnel habilité avec son accord. Le dossier comprend l'identité, les ressources, les charges, la liste des créances, les échéanciers et les pièces justificatives. La commission de surendettement vérifie la recevabilité, puis instruit le dossier : elle peut orienter vers une procédure de rétablissement personnel si la situation est désespérée sans perspective d'amélioration, ou vers un plan conventionnel de redressement négocié avec les créanciers. Ce plan peut rééchelonner les dettes, réduire les taux d'intérêt, voire effacer une partie des créances. Le juge peut être saisi en cas de désaccord. Les effets sont notables : suspension des poursuites, interdiction de nouveaux crédits, inscription au fichier des incidents de paiement. L'accompagnement social reste nécessaire pour traiter les causes et restaurer l'autonomie budgétaire.",
    "On attend la distinction temporelle et de gravité, les étapes du dossier, les types de plan et les effets de la procédure.")],
C("Un budget équilibré repose sur la connaissance des ressources, des dépenses contraintes et du coût réel du crédit.",
  "Solde = ressources − emplois · taux d'endettement = mensualités / revenu",
  "Dépenses contraintes · épargne de précaution · Banque de France · surendettement",
  "Ressources~Revenus du ménage~Salaire, prestations|Emplois~Dépenses et épargne~Loyer, crédit|Solde~Ressources moins emplois~Marge disponible",
  "Recenser les ressources et toutes les dettes|Classer les dépenses par priorité|Calculer le solde et le taux d'endettement|Rechercher aides et renégociations|Construire un budget prévisionnel suivi",
  "Oublier les petites dépenses récurrentes|Confondre trésorerie et surendettement|Souscrire un nouveau crédit pour en rembourser un autre|Négliger l'épargne de précaution",
  "1 800 euros~Ressources~880 euros~Dépenses contraintes~14 %~Taux d'endettement~220 euros~Solde restant",
  "Trésorerie~Décalage temporaire~Surendettement~Incapacité durable de remboursement",
  "Dépense contrainte~Difficile à réduire~Dépense libre~Arbitrage possible"),
UG)

# ============================================================ EC5
add("EC5.", "Emploi, chômage et marché du travail", "Économie", ["BTS1"],
S("Le marché du travail met en relation les entreprises qui demandent du travail et les personnes qui en offrent."
  "|La population active comprend les personnes en emploi et les chômeurs qui recherchent activement un emploi et sont disponibles."
  "|Le taux d'activité rapporte la population active à la population en âge de travailler."
  "|Le taux d'emploi rapporte le nombre de personnes en emploi à la population en âge de travailler."
  "|Le taux de chômage rapporte le nombre de chômeurs à la population active : il ne mesure donc pas la proportion de la population totale sans emploi."
  "|Le chômage conjoncturel résulte d'une insuffisance de la demande globale en période de ralentissement économique."
  "|Le chômage structurel provient d'un décalage durable entre les qualifications disponibles et les emplois proposés, ou d'un coût du travail jugé trop élevé."
  "|Le chômage frictionnel correspond au temps nécessaire à la recherche d'un emploi ou à la transition entre deux employeurs."
  "|Le chômage saisonnier dépend des variations d'activité selon les saisons, notamment dans le tourisme ou l'agriculture."
  "|Le chômage de longue durée touche les personnes sans emploi depuis un an ou plus et expose à un risque de déqualification et d'exclusion."
  "|Les politiques de l'emploi combinent formation professionnelle, accompagnement vers l'emploi, aides à l'embauche et activation des prestations."
  "|France Travail, les missions locales et les structures d'insertion par l'activité économique accompagnent les publics selon leur situation."),
[QC("Qui compose la population active ?", "Tous les habitants~Les personnes en emploi et les chômeurs disponibles~Les seuls salariés~Les retraités", 1,
    "La population active réunit les actifs occupés et les chômeurs au sens du BIT."),
 QC("Quel est le dénominateur du taux de chômage ?", "La population totale~La population en âge de travailler~La population active~Le nombre d'entreprises", 2,
    "Le taux de chômage rapporte les chômeurs à la population active, pas à la population totale."),
 QC("Quel chômage résulte d'un manque de demande globale ?", "Structurel~Conjoncturel~Frictionnel~Saisonnier", 1,
    "Le chômage conjoncturel est lié aux fluctuations de l'activité économique."),
 QC("Que désigne le chômage de longue durée ?", "Moins d'un mois sans emploi~Un an ou plus sans emploi~Un emploi à temps partiel~Une formation en alternance", 1,
    "On parle de chômage de longue durée après un an ou plus sans emploi."),
 QC("Quel organisme accompagne les jeunes vers l'emploi ?", "La CAF~Les missions locales~La CNIL~La Cour des comptes", 1,
    "Les missions locales accueillent et orientent les jeunes de 16 à 25 ans."),
 QC("Quel est un risque du chômage de longue durée ?", "Une augmentation automatique des salaires~La déqualification et l'éloignement du marché du travail~Une promotion garantie~Une formation obligatoire", 1,
    "L'éloignement prolongé de l'emploi entraîne une perte de compétences et de confiance."),
 QC("Quel type de mesure relève de la politique active de l'emploi ?", "Une pension d'invalidité~Une formation professionnelle qualifiante~Un congé parental~Une allocation familiale", 1,
    "La formation vise à améliorer l'employabilité et le retour à l'emploi."),
 QT("Une personne de 52 ans, sans emploi depuis 18 mois, souhaite reprendre une activité. Proposez un diagnostic et un parcours d'accompagnement réalistes.",
    "Le diagnostic porte sur plusieurs dimensions. D'abord, la situation au regard de l'emploi : durée de privation d'emploi, derniers métiers exercés, qualifications, compétences actualisées, prestige et conditions de travail antérieurs. Ensuite, les freins identifiés : mobilité géographique, garde d'enfants ou d'un proche, santé, niveau de maîtrise des outils numériques, découragement, problèmes de logement ou de revenus. Enfin, les atouts : expérience, réseau, motivation, compétences transférables. Le parcours proposé peut comporter cinq étapes : (1) un bilan de compétences approfondi, financé dans le cadre d'une formation ou d'un dispositif d'accompagnement ; (2) une remise à niveau numérique si nécessaire ; (3) une formation qualifiante courte visant un métier demandeur dans le bassin d'emploi local, identifié avec France Travail et les entreprises ; (4) une période de mise en situation en milieu professionnel ou un contrat d'insertion par l'activité économique pour reprendre un rythme de travail ; (5) un suivi après l'embauche pour sécuriser la reprise. Les aides possibles incluent l'allocation de retour à l'emploi, des aides à la formation, une aide au transport ou au déménagement et, si la santé le justifie, une reconnaissance de la qualité de travailleur handicapé. Le professionnel évite de imposer un métier : il construit un parcours avec la personne, en tenant compte de son.expérience et de ses choix.",
    "On attend un diagnostic multidimensionnel, cinq étapes réalistes, des aides identifiées et une posture qui préserve l'autonomie."),
 QT("Expliquer pourquoi le taux de chômage peut baisser sans que le nombre d'emplois augmente, et donner deux exemples de situations correspondantes.",
    "Le taux de chômage est un ratio : il rapporte le nombre de chômeurs à la population active. Son évolution dépend donc du numérateur et du dénominateur. Il peut baisser alors que l'emploi stagne, voire recule, dans plusieurs situations. Premièrement, si des chômeurs cessent de rechercher activement un emploi ou ne sont plus disponibles, ils sortent de la population active au sens statistique : ils ne sont plus comptés comme chômeurs, et le taux diminue mécaniquement, alors qu'aucun emploi n'a été créé. C'est le phénomène des « découragés ». Deuxièmement, si des actifs quittent le marché du travail pour partir à la retraite ou suivre une formation non rémunérée, le dénominateur baisse ; à chômeurs constants, le taux peut se réduire alors que la situation individuelle ne s'améliore pas. Troisièmement, unchômeur qui occupe une heure de travail rémunérée peut être considéré comme employé au sens de l'enquête, ce qui réduit le nombre de chômeurs sans créer un emploi durable. Pour interpréter correctement un taux de chômage, il faut donc le compléter par d'autres indicateurs : taux d'emploi, taux d'activité, nombre d'emplois créés, durée moyenne du chômage, part des contrats courts et taux de chômage des jeunes ou des seniors. Le taux global est un indicateur utile mais insuffisant pour apprécier la santé du marché du travail et l'efficacité des politiques menées.",
    "On attend l'explication du ratio et deux exemples : sortie de la population active et changement de statut statistique, avec des indicateurs complémentaires.")],
C("Le chômage se mesure par un ratio et se décompose en plusieurs types : conjoncturel, structurel, frictionnel, saisonnier.",
  "Taux de chômage = chômeurs / population active",
  "Population active =employés + chômeurs disponibles",
  "Population active~Emploi et recherche~Dénominateur|Chômage conjoncturel~Manque de demande~Cyclique|Chômage structurel~Inadaptation des qualifications~Durable",
  "Définir la situation de la personne au regard de l'emploi|Identifier les freins et les atouts|Choisir une formation ou une mise en situation|Mobiliser les aides disponibles|Assurer un suivi après la reprise",
  "Confondre population active et population totale|Croire qu'un taux en baisse signifie plus d'emplois|Ignorer les freins périphériques comme le logement|Imposer un parcours sans consulter la personne",
  "18 mois~Durée sans emploi~52 ans~Âge de la personne~Un an~Seuil de longue durée~France Travail~Opérateur de l'emploi",
  "Chômage conjoncturel~Ralentissement économique~Chômage structurel~Décalage durable",
  "Taux d'activité~Actifs sur population en âge de travailler~Taux d'emploi~Employés sur population en âge de travailler"),
UG)

# ============================================================ EC6
add("EC6.", "L'action publique et les politiques économiques", "Économie", ["BTS2"],
S("L'action publique vise à corriger les défaillances du marché et à poursuivre des objectifs d'intérêt général."
  "|Les défaillances du marché incluent les externalités, les biens publics, les monopoles et l'asymétrie d'information."
  "|Une externalité est un effet indirect d'une activité économique sur un tiers, positif ou négatif, non intégré dans le prix."
  "|La pollution est une externalité négative ; la vaccination ou l'éducation produisent des externalités positives."
  "|La fiscalité permet de financer les dépenses publiques et d'influencer les comportements, par exemple par une taxe sur les émissions polluantes."
  "|Les dépenses publiques comprennent les dépenses de fonctionnement, d'investissement et les prestations sociales."
  "|La redistribution s'effectue par les prestations sociales, l'impôt progressif et les services publics, afin de réduire les inégalités de revenu."
  "|La politique budgétaire agit par les recettes et les dépenses de l'État ; la politique monétaire agit par les taux et la quantité de monnaie."
  "|En zone euro, la politique monétaire est conduite par la Banque centrale européenne de façon indépendante des gouvernements."
  "|Les multiplicateurs budgétaires désignent l'effet d'une variation des dépenses publiques sur l'activité économique."
  "|L'évaluation des politiques publiques vérifie si les objectifs sont atteints, à quel coût et avec quels effets non prévus."
  "|L'action sociale s'inscrit dans cette logique : elle vise l'accès aux droits, la cohésion sociale et l'accompagnement des publics vulnérables."),
[QC("Quel est un exemple d'externalité négative ?", "La vaccination~La pollution due à une usine~Un service public d'éclairage~Une formation professionnelle", 1,
    "La pollution impose un coût à des tiers qui ne participent pas à la décision de production."),
 QC("Quel est un objectif de la redistribution ?", "Augmenter les inégalités~Réduire les écarts de revenus~Supprimer les impôts~Réduire la dépense publique", 1,
    "La redistribution vise à réduire les inégalités et à garantir un accès minimal à des biens essentiels."),
 QC("Quelle institution conduit la politique monétaire dans la zone euro ?", "La Commission européenne~La Banque centrale européenne~Le Parlement européen~La Banque mondiale", 1,
    "La BCE est indépendante et définit la politique monétaire de la zone euro."),
 QC("Quel outil relève de la politique budgétaire ?", "Le taux directeur~Une variation des dépenses publiques~Le taux de change~La masse monétaire", 1,
    "La politique budgétaire joue sur les recettes et les dépenses du budget public."),
 QC("Pourquoi un bien public justifie-t-il une intervention publique ?", "Parce qu'il est très rentable~Parce que le marché ne le fournit pas spontanément en quantité suffisante~Parce qu'il est interdit~Parce qu'il est rival", 1,
    "L'impossibilité d'exclure les non-payants décourage l'initiative privée : l'État doit intervenir."),
 QC("Que vérifie l'évaluation d'une politique publique ?", "Seulement son coût~Ses effets, son coût et ses éventuels effets non prévus~Le nombre de réunions~L'avis d'un seul ministre", 1,
    "L'évaluation porte sur la pertinence, l'efficacité, l'efficience et les effets indésirables."),
 QC("Quel est un effet possible d'une taxe sur les émissions polluantes ?", "Elle augmente la pollution~Elle incite à réduire les émissions~Elle supprime le marché~Elle est sans effet", 1,
    "En internalisant le coût de la pollution, la taxe modifie les incitations des producteurs."),
 QT("Une collectivité souhaite lutter contre la précarité énergétique. Proposez une analyse en termes de défaillance du marché et d'outils d'action publique.",
    "L'analyse part d'une combinaison de défaillances. Le logement ancien mal isolé produit des externalités négatives : surconsommation d'énergie, émissions de gaz à effet de serre et difficultés de santé pour les occupants, coûts qui ne sont pas supportés par le seul propriétaire. Il existe aussi une asymétrie d'information : le bailleur connaît mal la performance réelle du logement ou le locataire ne dispose pas des données de consommation, ce qui nuit aux arbitrages. Enfin, l'énergie est un bien essentiel dont l'accès inégal soulève une question de redistribution. Les outils publics peuvent être combinés : une aide à la rénovation thermique conditionnée à des travaux, des certificats d'économie d'énergie obligeant les fournisseurs à financer des actions d'efficacité, un tarif social de l'énergie, une régulation des prix ou une intervention de l'État en faveur des ménages modestes, et un accompagnement par les services sociaux pour identifier les situations de précarité. La collectivité peut aussi agir sur la rénovation de son parc social et sur l'information des habitants. L'évaluation doit mesurer non seulement les euros investis, mais la baisse des factures, l'amélioration du confort, la réduction des émissions et l'effet sur les impayés. Une action uniquement financière peut être captée par les ménages les plus à même de faire des travaux : le ciblage et le suivi sont donc essentiels.",
    "On attend l'identification d'externalités et d'asymétries d'information, au moins trois outils publics et des indicateurs d'évaluation."),
 QT("Distinguer politique budgétaire et politique monétaire, puis expliquer pourquoi elles doivent être coordonnées sans être confondues.",
    "La politique budgétaire est menée par l'État et les administrations publiques : elle agit sur les recettes fiscales et les dépenses, par exemple en augmentant les investissements ou en accordant des aides. Elle peut être expansionniste, pour soutenir la demande en période de récession, ou restrictive, pour réduire le déficit public. Ses effets dépendent du multiplicateur budgétaire et des délais de mise en œuvre. La politique monétaire est conduite par la banque centrale, la BCE dans la zone euro : elle agit principalement sur les taux d'intérêt directeurs et sur la quantité de monnaie pour maintenir la stabilité des prix. Une baisse de taux rend le crédit moins cher et stimule l'investissement ; une hausse le renchérit et freine l'inflation. Les deux politiques ne doivent pas être confondues : l'une relève du vote budgétaire et du débat démocratique, l'autre de l'indépendance de la banque centrale, précisément pour éviter que le financement des déficits publics ne provoque de l'inflation. Elles doivent cependant être coordonnées : si la politique budgétaire est expansionniste alors que la politique monétaire est restrictive, les effets peuvent s'annuler partiellement, et les taux élevés peuvent rendre le service de la dette publique plus coûteux. La coordination passe par le dialogue entre les institutions et par une lecture partagée de la situation économique, sans remettre en cause les mandats respectifs.",
    "La réponse doit définir les deux politiques, préciser qui les mène et avec quels outils, puis expliquer l'indépendance de la BCE et la nécessité d'une coordination.")],
C("L'action publique corrige les défaillances du marché et poursuit des objectifs de redistribution, d'efficacité et de cohésion.",
  "Externalité = effet indirect sur un tiers non intégré au prix",
  "Politique budgétaire : recettes et dépenses · politique monétaire : taux et monnaie",
  "Externalité~Effet sur un tiers~Pollution|Dépense publique~Action de l'État~Investissement et prestations|Redistribution~Réduire les inégalités~Impôt et prestations",
  "Repérer la défaillance du marché|Identifier les objectifs d'intérêt général|Choisir les outils adaptés|Prévoir les effets indésirables|Évaluer les résultats avec des indicateurs",
  "Confondre politique budgétaire et monétaire|Ignorer les effets non prévus d'une aide|Croire que toute dépense publique est efficace|Négliger le ciblage des ménages",
  "BCE~Politique monétaire~Externalité négative~Pollution~Tarif social~Accès à l'énergie~Évaluation~Effets et coûts",
  "Politique budgétaire~État et budget~Politique monétaire~Banque centrale et taux",
  "Externalité positive~Effet bénéfique~Externalité négative~Coût pour autrui"),
UG)

# ============================================================ EC7
add("EC7.", "Économie sociale et solidaire et tiers secteur", "Économie", ["BTS2"],
S("L'économie sociale et solidaire (ESS) regroupe des entreprises dont la finalité n'est pas le seul partage du profit."
  "|La loi du 31 juillet 2014 relative à l'ESS définit un ensemble d'entités : coopératives, mutuelles, associations et fondations."
  "|Ces organisations partagent des principes : primauté de l'humain, démocratie ou participation, recherche d'un équilibre entre efficacité économique et utilité sociale."
  "|Une coopérative est possédée et gérée par ses membres, avec une règle générale : une personne, une voix."
  "|Une mutuelle est une association d'assurance à finalité non lucrative, qui mutualise les risques entre ses adhérents."
  "|Une association est un groupement de personnes réuni autour d'un but non lucratif, doté de la personnalité juridique par la loi de 1901."
  "|Une fondation affecte des biens à une œuvre d'intérêt général et est placée sous un contrôle administratif."
  "|Les entreprises de l'ESS exercent des activités économiques : elles vendent des biens ou des services, créent de la valeur et emploient des salariés."
  "|Les bénéfices sont en principe réinvestis dans l'activité ou affectés à la mission sociale, plutôt que distribués à des actionnaires."
  "|L'insertion par l'activité économique (IAE) vise à permettre à des personnes éloignées de l'emploi d'acquérir une expérience professionnelle."
  "|Le commerce équitable, les circuits courts et les services à la personne figurent parmi les secteurs où l'ESS est présente."
  "|Les financements combinent ventes, subventions publiques, dons, adhésions et investissements à impact, ce qui exige une gestion rigoureuse et transparente."),
[QC("Quelle loi cadre définit l'ESS en France ?", "La loi du 6 janvier 1978~La loi du 31 juillet 2014~La loi du 8 août 1998~La loi du 1er juillet 1901", 1,
    "La loi du 31 juillet 2014 relative à l'ESS donne un cadre juridique au secteur."),
 QC("Quel principe caractérise une coopérative ?", "Une action, une voix~Une personne, une voix~Le profit avant tout~La propriété publique", 1,
    "La coopérative repose sur la participation démocratique de ses membres, généralement une personne, une voix."),
 QC("Quelle structure relève de la loi du 1er juillet 1901 ?", "La fondation~L'association~La société anonyme~La mutuelle", 1,
    "La loi de 1901 régit la création des associations à but non lucratif."),
 QC("Que se passe-t-il avec les bénéfices d'une entreprise de l'ESS ?", "Ils sont distribués aux actionnaires~Ils sont réinvestis ou affectés à la mission~Ils sont supprimés~Ils sont versés à l'État", 1,
    "La finalité sociale implique de réaffecter les excédents à l'activité ou à la mission."),
 QC("Quel est un objectif de l'insertion par l'activité économique ?", "Réduire les salaires~Permettre une expérience professionnelle à des personnes éloignées de l'emploi~Supprimer les formations~Remplacer le service public", 1,
    "L'IAE combine activité économique et accompagnement vers l'emploi durable."),
 QC("Quel mode de financement est spécifique aux associations ?", "Les seules ventes~Les dons et les subventions~Les seuls emprunts~Le capital-risque uniquement", 1,
    "Les associations combinent ventes, dons, adhésions et subventions publiques."),
 QC("Quel est un secteur d'activité de l'ESS ?", "Le commerce équitable~La seule administration centrale~Les seules banques de investissement~L'industrie nucléaire", 0,
    "Commerce équitable, circuits courts, services à la personne et insertion sont des domaines de l'ESS."),
 QT("Une association souhaite développer un service de repas à domicile pour des personnes âgées. Expliquez les atouts et les contraintes de ce projet au regard de l'ESS.",
    "Les atouts sont multiples. L'association poursuit une finalité d'intérêt général : maintenir l'autonomie et le lien social des personnes âgées, plutôt que rechercher le seul profit. Son statut lui permet de mobiliser des financements variés : subventions de la collectivité ou du département, dons, adhésions, ventes de prestations et dispositifs d'insertion. Elle peut associer les usagers et les salariés à la réflexion, par exemple par un comité de suivi, ce qui renforce la démocratie interne et l'adéquation du service aux besoins. Enfin, les excédents sont réinvestis dans l'amélioration du service ou dans de nouveaux créneaux. Les contraintes sont cependant réelles. Le modèle économique repose sur un équilibre fragile entre le prix payé par les usagers, souvent modeste, et le coût réel de la prestation ; les subventions sont incertaines et exigent des dossiers et une reddition de comptes. La qualité sanitaire impose des règles strictes : hygiène, formation du personnel, traçabilité des repas, plan de maîtrise sanitaire. L'activité est aussi intensive en main-d'œuvre, avec des difficultés de recrutement et de fidélisation. Enfin, la concurrence avec des prestataires commerciaux peut exercer une pression sur les prix. La démarche recommandée consiste à chiffrer précisément le coût de revient, à tester le service sur un petit périmètre, à formaliser des partenariats avec le CCAS et des financeurs, et à évaluer régulièrement la qualité perçue par les usagers, indicateur central pour une structure de l'ESS.",
    "On attend des atouts liés à la finalité et au modèle associatif, des contraintes économiques et sanitaires, et une démarche de test et d'évaluation."),
 QT("Distinguer ESS et économie marchande traditionnelle, puis expliquer pourquoi une entreprise de l'ESS doit tout de même être performante économiquement.",
    "L'économie marchande traditionnelle a pour objectif principal le profit et la rémunération des apporteurs de capital ; les décisions sont prises selon le poids du capital, et les bénéfices sont distribués sous forme de dividendes. L'ESS poursuit une finalité sociale ou environnementale : les bénéfices sont réinvestis, la gouvernance est souvent démocratique et les parties prenantes, salariés, usagers ou membres, participent aux décisions. Les deux logiques ne s'excluent pas totalement : de nombreuses entreprises classiques poursuivent des objectifs sociaux et des structures de l'ESS exercent des activités très concurrentielles. La différence tient à la priorité donnée à la mission et à l'affectation des excédents. Une structure de l'ESS doit néanmoins être performante économiquement pour trois raisons. D'abord, elle vend des biens ou des services sur un marché : si ses prix ne couvrent pas ses coûts, elle accumule des pertes et disparaît, ce qui prive les usagers de son service. Ensuite, elle emploie des salariés dont elle doit assurer la rémunération, la formation et la sécurité : la qualité sociale de l'emploi suppose des ressources. Enfin, sa crédibilité auprès des financeurs et des collectivités dépend de sa capacité à gérer rigoureusement, à respecter ses engagements et à rendre des comptes. La performance n'est donc pas un objectif rival de l'utilité sociale : elle en est la condition de durabilité. Le défi est de concilier les deux, par exemple en mesurant à la fois le résultat financier et l'impact social.",
    "La réponse doit opposer finalité, gouvernance et affectation des résultats, puis justifier la performance économique par la pérennité, l'emploi et la crédibilité.")],
C("L'ESS concilie activité économique et utilité sociale : coopératives, mutuelles, associations et fondations réinvestissent leurs excédents.",
  "Loi du 31 juillet 2014 · une personne, une voix · excédents réinvestis",
  "Coopérative · mutuelle · association · fondation · insertion par l'activité économique",
  "ESS~Finalité sociale~Quatre familles|Coopérative~Gestion par les membres~Une personne, une voix|Association~But non lucratif~Loi de 1901",
  "Choisir un statut adapté à la mission|Chiffrer le coût de revient du service|Diversifier les financements|Associer usagers et salariés|Mesurer performance économique et impact social",
  "Confondre but non lucratif et absence d'activité économique|Distribuer les excédents comme dividendes|Négliger la reddition de comptes|Croire que les subventions sont permanentes",
  "2014~Loi cadre ESS~1901~Loi sur les associations~Une personne une voix~Règle coopérative~Repas~Service testé",
  "ESS~Utilité sociale d'abord~Entreprise classique~Profit et capital d'abord",
  "Coopérative~Membres propriétaires~Mutuelle~Mutualisation des risques"),
"Loi du 31 juillet 2014 relative à l'économie sociale et solidaire et programmes applicables en BTS, référentiel BTS ESF 2022")

# ============================================================ CT1
add("CT1.", "Les principes comptables et le bilan", "Comptabilité et gestion", ["BTS1"],
S("La comptabilité est un système d'information qui enregistre, classe et restitue les opérations économiques et financières d'une organisation."
  "|Le bilan est un document de synthèse qui décrit la situation patrimoniale de l'entité à une date donnée."
  "|Il se compose de deux parties : l'actif, qui montre ce que l'entreprise possède, et le passif, qui indique comment ces biens sont financés."
  "|L'actif comprend les actifs immobilisés, destinés à être utilisés durablement, et les actifs circulants, transformés rapidement en liquidités."
  "|Le passif distingue les capitaux propres, who appartiennent aux propriétaires, et les dettes envers les tiers."
  "|L'équation comptable fondamentale s'écrit : actif = capitaux propres + dettes."
  "|Le principe de dualité impose que chaque opération modifie au moins deux comptes pour que l'équilibre du bilan soit préservé."
  "|Le principe de prudence interdit de comptabiliser un profit avant sa réalisation et impose d'anticiper les pertes probables."
  "|Le principe de continuité d'exploitation suppose que l'entité poursuivra son activité dans un avenir prévisible."
  "|Le principe d'indépendance des exercices rattache chaque opération à la période au cours de laquelle elle a été réalisée, et non à son paiement."
  "|Le Plan comptable général organise la numérotation des comptes : classe 1 pour les capitaux, 2 pour les immobilisations, 3 à 5 pour les stocks et tiers, 6 et 7 pour les charges et produits."
  "|Le bilan est utilisé par les dirigeants, les financeurs et les partenaires pour apprécier la structure financière et la capacité de remboursement."),
[QC("Que représente l'actif du bilan ?", "Les dettes de l'entité~Les biens et valeurs possédés~Les charges de l'exercice~Les recettes de l'exercice", 1,
    "L'actif décrit les emplois : ce que l'organisation possède et utilise."),
 QC("Quelle est l'équation fondamentale du bilan ?", "Actif = charges + produits~Actif = capitaux propres + dettes~Passif = charges + produits~Dettes = actif + capitaux", 1,
    "Les ressources (capitaux propres et dettes) financent les emplois (actif)."),
 QC("Quel compte relève de la classe 2 du Plan comptable général ?", "Un compte de charge~Un compte d'immobilisation~Un compte de produit~Un compte de trésorerie", 1,
    "La classe 2 enregistre les comptes d'immobilisations corporelles et incorporelles."),
 QC("Quel principe interdit d'enregistrer un profit avant sa réalisation ?", "Continuité~Prudence~Indépendance~Dualité", 1,
    "Le principe de prudence impose de ne pas anticiper les produits et de prévoir les pertes."),
 QC("Qu'est-ce qu'un actif circulant ?", "Un bien destiné à une utilisation durable~Un actif transformé rapidement en liquidités~Une dette à long terme~Une charge de personnel", 1,
    "Les actifs circulants comprennent les stocks, les créances et la trésorerie."),
 QC("Que signifie le principe de dualité ?", "Chaque opération n'utilise qu'un seul compte~Chaque opération modifie au moins deux comptes~Le bilan compte deux parties égales~Il existe deux bilans par an", 1,
    "La double écriture garantit l'équilibre permanent du bilan."),
 QC("Quel principe rattache une opération à son exercice plutôt qu'à son paiement ?", "Dualité~Prudence~Indépendance des exercices~Continuité", 2,
    "L'indépendance des exercices fonde la comptabilité d'engagement."),
 QT("Une association achète du matériel informatique 3 000 euros, payé moitié comptant, moitié par un emprunt bancaire à trois mois. Décrivez les écritures et l'effet sur le bilan.",
    "L'opération est enregistrée à la date d'acquisition, selon la comptabilité d'engagement. On débite le compte 2183 « Matériel informatique » de 3 000 euros : c'est un actif immobilisé, destiné à être utilisé pendant plusieurs exercices. On crédite le compte 512 « Banque » de 1 500 euros pour la part payée comptant, ce qui réduit l'actif circulant. On crédite le compte 401 « Fournisseurs » de 1 500 euros pour la somme restant due, ce qui augmente le passif. L'écriture complète est : 2183 débit 3 000 / 512 crédit 1 500 / 401 crédit 1 500. L'équation comptable reste vérifiée : l'actif total n'augmente finalement que de 1 500 euros (3 000 d'immobilisation moins 1 500 de trésorerie), et le passif augmente de 1 500 euros par la dette. La dualité est respectée : trois comptes sont touchés, mais le total des débits égale le total des crédits. À l'échéance, le remboursement donnera lieu à une nouvelle écriture : débit 401, crédit 512 pour 1 500 euros, sans effet sur le total du bilan puisqu'un passif diminue en même temps que l'actif. Enfin, l'usage du matériel donnera lieu à des dotations aux amortissements dans les exercices suivants, conformément au principe de prudence et à la durée d'utilisation estimée.",
    "On attend les comptes 2183, 512 et 401, les montants, le respect de l'équilibre et la distinction entre achat et règlement."),
 QT("Expliquer pourquoi le bilan ne suffit pas à apprécier la santé financière d'une association et quels autres éléments consulter.",
    "Le bilan est une photographie du patrimoine à une date donnée : il indique ce que l'association possède, ce qu'elle doit et le montant de ses capitaux propres. Il ne montre pas directement si l'activité de l'année a dégagé un excédent ou une perte, ni si la trésorerie permet de faire face aux échéances proches. Pour apprécier la santé financière, il faut lui adjoindre plusieurs documents. Le compte de résultat retrace les produits et les charges de l'exercice et fait apparaître le résultat ; il montre par exemple si les subventions couvrent les charges de fonctionnement. L'annexe précise les méthodes comptables, les dettes, les engagements hors bilan et les événements postérieurs à la clôture. Le tableau de financement et le plan de trésorerie montrent les flux et la capacité à honorer les paiements à venir. Les ratios complètent l'analyse : ratio d'endettement, fonds de roulement, besoin en fonds de roulement et trésorerie nette. Enfin, pour une association, le rapport d'activité et le budget prévisionnel éclairent le lien entre les moyens et la mission sociale. Un bilan peut paraître équilibré alors que la trésorerie est critique, par exemple si les créances sont importantes et les délais de paiement longs. L'analyse doit donc combiner patrimoine, résultat, flux et contexte d'activité.",
    "On attend la limite du bilan comme photographie statique, la mention du compte de résultat, de l'annexe, du plan de trésorerie et de quelques ratios.")],
C("Le bilan décrit le patrimoine à une date : actif = capitaux propres + dettes, dans le respect des principes comptables.",
  "Actif = emplois · passif = ressources",
  "Dualité · prudence · continuité · indépendance des exercices",
  "Actif~Biens possédés~Emplois|Passif~Capitaux et dettes~Ressources|Dualité~Double écriture~Équilibre",
  "Repérer la nature de l'opération|Choisir les comptes du Plan comptable général|Écrire le débit et le crédit|Vérifier l'équilibre du bilan|Contrôler la cohérence avec les principes",
  "Confondre actif et passif|Enregistrer un produit avant sa réalisation|Payer comptant une opération à crédit|Oublier l'annexe lors de l'analyse",
  "3 000 euros~Coût du matériel~1 500 euros~Part comptant et dette~401~Fournisseur~2183~Matériel informatique",
  "Actif immobilisé~Usage durable~Actif circulant~Transformation rapide",
  "Capitaux propres~Ressources propres~Dettes~Ressources empruntées"),
"Plan comptable général et programmes d'enseignement professionnel, référentiel BTS ESF 2022")

# ============================================================ CT2
add("CT2.", "Compte de résultat : charges, produits et résultat", "Comptabilité et gestion", ["BTS1"],
S("Le compte de résultat récapitule les produits et les charges d'une entité sur un exercice, généralement l'année civile."
  "|Il fait apparaître le résultat de l'exercice : lorsque les produits dépassent les charges, il s'agit d'un bénéfice ; dans le cas contraire, d'une perte."
  "|Une charge est une consommation de biens ou de services, ou une diminution d'actif, entraînant une baisse du résultat."
  "|Un produit est une augmentation d'actif ou une diminution de dette, entraînant une hausse du résultat."
  "|Les charges d'exploitation comprennent les achats, les services extérieurs, les impôts et taxes, les charges de personnel et les amortissements."
  "|Les produits d'exploitation comprennent les ventes de biens ou de services et les subventions d'exploitation."
  "|Les charges et produits financiers proviennent des opérations de trésorerie, des emprunts et des placements."
  "|Les charges et produits exceptionnels portent sur des opérations inhabituelles, comme la cession d'un actif ou un litige."
  "|Le résultat d'exploitation mesure la performance de l'activité courante, avant incidence du financement et des éléments exceptionnels."
  "|Le résultat net se calcule après impôt sur les sociétés, lorsque l'entité y est assujettie ; les associations ont un régime particulier."
  "|La marge commerciale correspond à la différence entre le prix de vente et le coût d'achat des biens vendus."
  "|Dans une association, le résultat est souvent appelé excédent ou déficit de fonctionnement et n'est pas distribué : il est affecté aux réserves."),
[QC("Que se passe-t-il si les charges dépassent les produits ?", "L'entité réalise un bénéfice~L'entité enregistre une perte~Le bilan est déséquilibré~La trésorerie augmente automatiquement", 1,
    "Charges supérieures aux produits signifient un résultat négatif, donc une perte."),
 QC("Quel élément est une charge d'exploitation ?", "Une subvention reçue~Le salaire d'un salarié~Un produit de placement~Une vente de service", 1,
    "Les charges de personnel figurent parmi les charges d'exploitation."),
 QC("Que mesure le résultat d'exploitation ?", "Le résultat après impôt~La performance de l'activité courante~Le montant des dettes~La valeur du patrimoine", 1,
    "Il isole le résultat lié à l'activité ordinaire, avant financement et exceptionnel."),
 QC("Quel est un produit exceptionnel ?", "Une vente habituelle~Une subvention d'exploitation~Le produit de cession d'un actif immobilisé~Un loyer courant", 2,
    "La cession d'un actifSortant de l'activité habituelle est un produit exceptionnel."),
 QC("Comment calculer la marge commerciale ?", "Prix de vente moins coût d'achat~Charges moins produits~Produits plus charges~Résultat net divisé par ventes", 0,
    "La marge commerciale est la différence entre prix de vente et coût d'achat des marchandises."),
 QC("Quel est un produit d'exploitation pour une association ?", "Un don affecté aux réserves~Une subvention d'exploitation~Un produit financier~Une vente d'immobilisation", 1,
    "Les subventions d'exploitation financent l'activité courante de l'association."),
 QC("Que devient l'excédent d'une association ?", "Il est distribué aux adhérents~Il est affecté aux réserves ou reporté~Il est versé à l'État~Il disparaît", 1,
    "L'excédent n'étant pas distribuable, il est affecté aux réserves ou reporté sur l'exercice suivant."),
 QT("Un centre social présente les agrégats suivants : produits d'exploitation 480 000 euros, charges d'exploitation 465 000 euros, produit financier 2 000 euros, charge financière 6 000 euros, produit exceptionnel 8 000 euros, charge exceptionnelle 3 000 euros. Calculez les résultats successifs et commentez.",
    "Le résultat d'exploitation s'élève à 480 000 − 465 000 = 15 000 euros : l'activité courante du centre dégage un excédent positif. Le résultat financier vaut 2 000 − 6 000 = −4 000 euros : le coût du financement, probablement des intérêts d'emprunt, pèse sur le résultat. Le résultat courant avant impôt est donc de 15 000 − 4 000 = 11 000 euros. Le résultat exceptionnel vaut 8 000 − 3 000 = 5 000 euros. Le résultat net avant impôt s'établit à 11 000 + 5 000 = 16 000 euros. Pour une association, on parlera d'excédent de l'exercice, qui sera affecté aux réserves ou reporté, et non de bénéfice distribuable. L'analyse montre que le cœur d'activité est positif mais relativement fragile : un excédent d'exploitation de 15 000 euros sur 480 000 euros de produits représente une marge d'environ 3,1 %, ce qui laisse peu de capacité d'autofinancement pour renouveler les équipements. Le résultat exceptionnel, lié à des opérations non répétables, améliore le résultat final mais ne doit pas être pris en compte dans la prévision. Le centre devrait donc surveiller la charge financière et constituer progressivement des réserves pour investissement, tout en maintenant la qualité du service rendu.",
    "On attend le calcul des résultats d'exploitation (15 000), financier (−4 000), exceptionnel (5 000) et net (16 000), avec une interprétation adaptée au statut associatif."),
 QT("Expliquer la différence entre charge et produit, puis montrer pourquoi le résultat comptable n'est pas identique à la trésorerie.",
    "Une charge correspond à une consommation de ressources ou à une augmentation de dette enregistrée au cours de l'exercice, quelle que soit la date de paiement : salaires, achats, amortissements, fournitures. Un produit correspond à une augmentation de ressources ou à une diminution de dette acquise au cours de l'exercice : ventes, subventions, cotisations, produits financiers. La différence entre les produits et les charges donne le résultat comptable, calculé selon la comptabilité d'engagement et le principe d'indépendance des exercices. La trésorerie, elle, mesure les encaissements et décaissements réels pendant la période. Les deux ne coïncident pas pour plusieurs raisons. Une vente peut être comptabilisée en produit dès la livraison alors que le client paiera à trente ou soixante jours : le résultat est positif avant l'encaissement. Un achat peut être enregistré en charge à la réception de la facture, alors que le règlement interviendra plus tard. Les amortissements sont des charges sans décaissement immédiat, puisqu'ils étalent le coût d'un immobilisation sur sa durée d'usage. Inversement, le remboursement d'un emprunt réduit la trésorerie sans être une charge, puisqu'il diminue simultanément une dette. Une association peut donc dégager un excédent comptable tout en ayant des difficultés de paiement, si ses créances sont nombreuses ou ses échéances courtes. Le suivi du plan de trésorerie est indispensable pour compléter le compte de résultat.",
    "On attend la définition des termes, le rôle de la comptabilité d'engagement et au moins trois exemples d'écart avec la trésorerie.")],
C("Le compte de résultat compare produits et charges sur l'exercice : sa différence donne le résultat, distinct de la trésorerie.",
  "Résultat = produits − charges",
  "Exploitation · financier · exceptionnel · impôt",
  "Produit~Augmentation d'actif~Ventes, subventions|Charge~Consommation de ressources~Salaires, achats|Résultat~Différence produits-charges~Bénéfice ou perte",
  "Identifier la nature de chaque agrégat|Classer produits et charges par catégorie|Calculer les résultats intermédiaires|Comparer avec le budget prévisionnel|Analyser l'écart avec la trésorerie",
  "Confondre charge et décaissement|Intégrer un produit exceptionnel dans une prévision|Ignorer les amortissements|Croire qu'un excédent signifie une trésorerie abondante",
  "480 000 euros~Produits d'exploitation~465 000 euros~Charges d'exploitation~15 000 euros~Résultat d'exploitation~16 000 euros~Résultat net",
  "Résultat d'exploitation~Activité courante~Résultat exceptionnel~Opérations inhabituelles",
  "Comptabilité d'engagement~À la date de l'opération~Trésorerie~À la date du paiement"),
"Plan comptable général et programmes d'enseignement professionnel, référentiel BTS ESF 2022")

# ============================================================ CT3
add("CT3.", "Le Plan comptable général et la tenue des comptes", "Comptabilité et gestion", ["BTS1"],
S("Le Plan comptable général (PCG) est un référentiel national qui définit la nomenclature des comptes et les règles de fonctionnement comptable."
  "|Il est mis à jour par l'Autorité des normes comptables et s'applique aux entreprises et aux organismes sans but lucratif, avec des adaptations."
  "|La numérotation en classes distingue : 1 capitaux propres, 2 immobilisations, 3 stocks, 4 tiers, 5 comptes financiers, 6 charges, 7 produits, 8 comptages spéciaux."
  "|Un compte est un outil de classement : son intelligibilité dépend du choix du bon numéro et du respect de la règle de débit et crédit."
  "|Par convention, les comptes d'actif sont débités lors d'une augmentation et crédités lors d'une diminution."
  "|Les comptes de passif, de capitaux propres et de produits sont crédités lors d'une augmentation et débités lors d'une diminution."
  "|Les comptes de charges sont débités lors d'une augmentation et crédités en fin d'exercice lors de la clôture."
  "|La pièce comptable justifie chaque écriture : facture, reçu, bulletin de salaire, relevé bancaire ou contrat."
  "|Le journal enregistre les écritures dans l'ordre chronologique ; le grand livre les reprend compte par compte."
  "|La balance avant clôture vérifie l'égalité des totaux des débits et des crédits, sans garantir l'absence d'erreur de nature."
  "|Les écritures d'inventaire en fin d'exercice comprennent les amortissements, les provisions, les régularisations de charges et de produits."
  "|Une comptabilité fiable est une condition de la transparence vis-à-vis des financeurs, des adhérents et des usagers d'une structure sociale."),
[QC("Quel organisme met à jour le Plan comptable général ?", "La CNIL~L'Autorité des normes comptables~La Banque de France~Le Conseil constitutionnel", 1,
    "L'ANC est responsable de l'évolution du référentiel comptable."),
 QC("Dans quelle classe se range un compte de charge ?", "Classe 2~Classe 5~Classe 6~Classe 7", 2,
    "La classe 6 regroupe les comptes de charges ; la classe 7, les produits."),
 QC("Quand un compte d'actif est-il débité ?", "Lors d'une diminution~Lors d'une augmentation~Jamais~Uniquement en fin d'exercice", 1,
    "Les augmentations d'actif s'enregistrent au débit du compte concerné."),
 QC("Quel document enregistre les écritures dans l'ordre chronologique ?", "Le grand livre~La balance~Le journal~Le bilan", 2,
    "Le journal suit l'ordre des dates ; le grand livre répartit les écritures par compte."),
 QC("Que vérifie une balance avant clôture ?", "La sincérité des pièces~L'égalité des débits et des crédits~La rentabilité de l'activité~La trésorerie disponible", 1,
    "La balance contrôle l'équilibre arithmétique des écritures, pas leur pertinence."),
 QC("Quel est un exemple d'écriture d'inventaire ?", "Une vente comptant~Une dotation aux amortissements~Un encaissement de subvention~Un paiement de fournisseur", 1,
    "Les amortissements, provisions et régularisations sont des écritures d'inventaire."),
 QC("Quel rôle joue la pièce comptable ?", "Elle remplace le compte~Elle justifie l'écriture enregistrée~Elle clôt l'exercice~Elle fixe le résultat", 1,
    "Toute écriture doit reposer sur une pièce justificative datée."),
 QT("Une association reçoit une facture de 1 200 euros HT pour une formation de ses bénévoles, avec TVA 20 %. Le règlement est effectué par virement. Décrivez l'écriture comptable et les contrôles à effectuer.",
    "Le montant TTC s'élève à 1 200 × 1,20 = 1 440 euros. La formation des bénévoles constitue une charge d'exploitation, enregistrée en classe 6, compte 6238 « Divers » ou un compte adapté selon le détail du Plan comptable associatif. La TVA de 240 euros est récupérable si l'association est assujettie et si la dépense relève d'une activité ouvrant droit à déduction ; elle est enregistrée au débit du compte 445662 « TVA déductible sur autres biens et services ». Le règlement par virement est enregistré au crédit du compte 512 « Banque » pour 1 440 euros. L'écriture est donc : débit 6238 pour 1 200 euros, débit 445662 pour 240 euros, crédit 512 pour 1 440 euros. Les contrôles portent sur la conformité de la facture, le calcul de la TVA, l'imputation au bon compte de charge, la disponibilité de la trésorerie au moment du paiement et l'absence de double enregistrement. Il faut aussi vérifier que la dépense est bien prévue au budget et qu'elle se rattache à l'exercice en cours, conformément au principe d'indépendance des exercices. Si l'association n'est pas assujettie à la TVA, la charge est enregistrée TTC et aucun compte de TVA n'est utilisé ; la facture doit alors le mentionner.",
    "On attend le calcul TTC (1 440 euros), la TVA (240 euros), les comptes 6238, 445662 et 512, et les contrôles de pièce, d'imputation et dedouble emploi."),
 QT("Expliquer pourquoi une balance équilibrée ne garantit pas une comptabilité exacte, et donner trois exemples d'erreurs qu'elle ne permet pas de détecter.",
    "La balance vérifie une égalité arithmétique : la somme des débits doit correspondre à la somme des crédits. Cette condition est nécessaire mais non suffisante : une erreur peut être parfaitement équilibrée et pourtant fausse. Premièrement, une erreur de nature ou d'imputation : une facture d'électricité enregistrée au compte « Fournitures de bureau » produit un débit et un crédit équilibrés, mais la charge est classée dans le mauvais compte, ce qui fausse l'analyse par poste. Deuxièmement, une erreur de montant identique des deux côtés : si la facture de 1 200 euros est saisie 1 200 à la banque et 1 200 en charge alors que le montant réel est 2 100 euros, la balance reste équilibrée malgré l'inexactitude, et la trésorerie enregistrée ne correspond pas au relevé bancaire. Troisièmement, un oubli total d'écriture : une recette de subvention non comptabilisée ne déséquilibre rien, puisque ni débit ni crédit n'ont été saisis ; la balance ne peut la révéler. Quatrièmement, une erreur de signe ou de sens sur une opération réelle peut passer inaperçue si elle affecte un compte de la même classe. Pour détecter ces anomalies, il faut rapprocher les pièces comptables, rapprocher la banque avec le relevé, contrôler les comptes par nature, comparer avec le budget et le compte de résultat de l'exercice précédent, et procéder à un inventaire physique. La rigueur documentaire et la séparation des tâches entre l'émetteur et le valideur complètent ces contrôles.",
    "On attend l'explication du caractère arithmétique de la balance et trois exemples : imputation erronée, montant erroné équilibré, omission totale d'écriture.")],
C("La tenue des comptes repose sur un référentiel codifié, des pièces justificatives et une organisation rigoureuse des écritures.",
  "Actif : débit = augmentation · passif et produits : crédit = augmentation",
  "Journal → grand livre → balance → inventaire",
  "PCG~Nomenclature nationale~Classes 1 à 8|Écriture~Débit et crédit~Pièce justificative|Balance~Contrôle arithmétique~Totaux égaux",
  "Classer l'opération dans le bon compte|Vérifier la pièce justificative|Enregistrer débit et crédit|Contrôler la balance|Réaliser les écritures d'inventaire",
  "Imputer une charge au mauvais compte|Croire qu'une balance équilibrée prouve l'exactitude|Oublier d'enregistrer une subvention|Négliger la TVA sur une facture",
  "1 200 euros~Montant HT~240 euros~TVA 20 %~1 440 euros~Montant TTC~Classe 6~Comptes de charges~Classe 7~Comptes de produits",
  "Journal~Ordre chronologique~Grand livre~Ordre par compte",
  "Débit~Augmentation d'actif ou de charge~Crédit~Augmentation de passif ou de produit"),
"Plan comptable général et programmes d'enseignement professionnel, référentiel BTS ESF 2022")

# ============================================================ CT4
add("CT4.", "TVA, facturation et paiements", "Comptabilité et gestion", ["BTS1"],
S("La taxe sur la valeur ajoutée (TVA) est un impôt indirect sur la consommation, perçu à chaque stade de la production et de la distribution."
  "|Le taux normal est de 20 % en France ; des taux réduits de 10 % et 5,5 % s'appliquent à certains biens et services, et un taux de 2,1 % à des opérations particulières."
  "|La TVA due par une entreprise correspond à la TVA collectée sur ses ventes moins la TVA déductible sur ses achats."
  "|La TVA collectée est facturée au client ; la TVA déductible est supportée par l'entreprise sur ses achats, dans les conditions légales."
  "|Une facture doit mentionner l'identité du vendeur et du client, la date, la désignation des biens ou services, le montant HT, le taux et le montant de TVA, le total TTC et les conditions de paiement."
  "|La facture doit être émise dès la réalisation de la vente ou de la prestation : c'est une obligation légale et fiscale."
  "|Un avoir corrige une facture erronée ou annule tout ou partie d'une opération : il reprend les mêmes mentions et le motif de la correction."
  "|Le règlement peut intervenir en espèces, par chèque, par virement, par carte bancaire ou par prélèvement ; chaque mode laisse une trace différente."
  "|Le relevé bancaire doit être rapproché du compte 512 « Banque » : c'est le rapprochement bancaire, qui identifie les écarts de date et les erreurs."
  "|Les délais de paiement sont encadrés : le respect des échéances est un enjeu de trésorerie pour les associations et leurs fournisseurs."
  "|La facturation électronique se généralise progressivement et impose des formats et des obligations de transmission à l'administration."
  "|Dans une structure sociale, une facturation claire et des paiements suivis contribuent à la transparence et à la qualité des relations avec les partenaires."),
[QC("Quel est le taux normal de TVA en France ?", "5,5 %~10 %~20 %~33 %", 2,
    "Le taux normal de la TVA est de 20 % ; 10 % et 5,5 % sont des taux réduits."),
 QC("Comment calculer la TVA due par une entreprise ?", "TVA collectée + TVA déductible~TVA collectée − TVA déductible~Total TTC × 2~Chiffre d'affaires divisé par 2", 1,
    "L'entreprise reverse la différence entre la TVA encaissée et la TVA qu'elle a pu déduire."),
 QC("Quelle mention doit figurer sur une facture ?", "La couleur du logo~Le montant HT, le taux et le montant de TVA~L'avis du client~Le numéro de téléphone du commercial", 1,
    "Les mentions fiscales obligatoires incluent le montant hors taxe, le taux et le montant de TVA."),
 QC("À quoi sert un avoir ?", "À augmenter une facture~À corriger ou annuler une facture~À remplacer un reçu~À accorder une remise future", 1,
    "L'avenant ou avoir rectificatif corrige une opération déjà facturée."),
 QC("Quel compte enregistre les opérations bancaires ?", "401~411~512~706", 2,
    "Le compte 512 « Banque » retrace les mouvements de trésorerie bancaire."),
 QC("Que permet le rapprochement bancaire ?", "De calculer la TVA~D'identifier les écarts entre relevé bancaire et comptabilité~De clore l'exercice~De fixer les prix", 1,
    "Il compare les écritures comptables et les opérations bancaires pour expliquer les différences."),
 QC("Quand doit être émise une facture ?", "À la fin de l'année seulement~Dès la vente ou la prestation~Lors du paiement uniquement~À la demande du client", 1,
    "La facture doit être établie lors de la réalisation de l'opération, même si le paiement est différé."),
 QT("Une structure facture une prestation d'accompagnement 2 500 euros HT avec TVA à 20 %. Le client paie 1 000 euros comptant et le solde à 30 jours. Présentez la facture et les écritures.",
    "La TVA s'élève à 2 500 × 0,20 = 500 euros, soit un total TTC de 3 000 euros. La facture mentionne l'émetteur, le client, la date, la désignation de la prestation, le montant HT de 2 500 euros, le taux de 20 %, le montant de TVA de 500 euros, le total TTC de 3 000 euros, les conditions de paiement (1 000 euros comptant, 2 000 euros à 30 jours) et les coordonnées bancaires. Les écritures sont les suivantes. À la facturation : débit du compte 411 « Clients » pour 3 000 euros, crédit du compte 706 « Prestations de services » pour 2 500 euros et crédit du compte 445200 « TVA collectée » pour 500 euros. À l'encaissement comptant : débit du compte 512 « Banque » pour 1 000 euros, crédit du compte 411 pour 1 000 euros. À l'échéance de 30 jours, si le client paie : débit 512 pour 2 000 euros, crédit 411 pour 2 000 euros. Le solde du compte 411 correspond alors à la créance restante, qui figure à l'actif circulant du bilan. Les contrôles portent sur la numérotation séquentielle des factures, la mention correcte de la TVA, le suivi des échéances et le rapprochement entre le compte Clients et le relevé bancaire. Si le client ne paie pas à échéance, une relance est nécessaire avant toute procédure de recouvrement.",
    "On attend la TVA (500 euros), le TTC (3 000 euros), les comptes 411, 706, 445200 et 512, et le suivi de la créance."),
 QT("Expliquer la différence entre TVA collectée, TVA déductible et TVA due, puis dire pourquoi un organisme non assujetti ne récupère pas la TVA.",
    "La TVA collectée est l'impôt que l'assujetti facture à ses clients lorsqu'il vend un bien ou un service : il l'encaisse pour le compte de l'État. La TVA déductible est celle qu'il a payée à ses fournisseurs sur ses achats de biens et services nécessaires à son activité : il peut en déduire le montant de la TVA collectée, sous réserve de disposer de factures conformes et d'affecter l'achat à une opération ouvrant droit à déduction. La TVA due est la différence entre les deux : TVA due = TVA collectée − TVA déductible. Si le résultat est positif, l'entreprise reverse la somme à l'administration fiscale lors de sa déclaration ; s'il est négatif, elle dispose d'un crédit de TVA reportable sur les déclarations suivantes ou, dans certains cas, remboursable. Un organisme non assujetti à la TVA, parce que son activité est exonérée ou parce qu'il n'effectue pas d'opérations imposables, ne facture pas de TVA à ses clients et ne peut pas déduire celle qu'il supporte sur ses achats : cette TVA devient alors un coût de la charge ou de l'investissement, enregistré TTC dans la comptabilité. C'est le cas de certaines associations dont les recettes sont exclusivement des subventions ou des dons. Cette situation augmente le coût réel de leurs achats et doit être prise en compte dans l'établissement des budgets prévisionnels et dans la comparaison des devis fournisseurs.",
    "On attend les trois définitions, la formule de la TVA due, la notion de crédit de TVA et la conséquence de l'absence d'assujettissement.")],
C("La TVA s'applique à chaque stade de la chaîne : collectée sur les ventes, déductible sur les achats, due au titre de la différence.",
  "TVA due = TVA collectée − TVA déductible",
  "Taux normal 20 % · facture obligatoire · compte 512 pour la banque",
  "TVA collectée~Facturée au client~Impôt encaissé|TVA déductible~Payée sur achats~Récupérable|TVA due~Différence~Versée à l'État",
  "Vérifier l'assujettissement de la structure|Établir une facture conforme|Calculer TVA et total TTC|Enregistrer facturation et encaissement|Suivre les échéances et rapprocher la banque",
  "Oublier le taux de TVA sur une facture|Confondre TVA collectée et TVA due|Enregistrer un règlement avant la facture|Négliger le rapprochement bancaire",
  "2 500 euros~Montant HT~500 euros~TVA 20 %~3 000 euros~Total TTC~30 jours~Délai de paiement",
  "TVA collectée~Sur les ventes~TVA déductible~Sur les achats",
  "Facture~Document obligatoire~Avoir~Document correctif"),
"Code général des impôts et programmes d'enseignement professionnel, référentiel BTS ESF 2022")

# ============================================================ CT5
add("CT5.", "Le budget prévisionnel d'une association", "Comptabilité et gestion", ["BTS2"],
S("Le budget prévisionnel est une estimation chiffrée des recettes et des dépenses d'une organisation pour une période future, généralement l'année à venir."
  "|Il traduit le projet d'activité en termes financiers et sert de référence pour le pilotage et le contrôle."
  "|Il se construit à partir du budget de l'exercice précédent, des objectifs de l'année, des contrats et subventions attendus, et des hypothèses d'activité."
  "|Les recettes comprennent les subventions publiques, les cotisations, les dons, les ventes de prestations et les produits financiers."
  "|Les dépenses incluent les charges de personnel, les frais de fonctionnement, les achats, les travaux et les dotations aux amortissements."
  "|Une recette incertaine ne doit pas être intégrée comme certaine : on distingue les recettes acquises, probables et envisagées."
  "|Le principe de prudence impose de prévoir des dépenses même lorsqu'elles ne sont pas encore facturées, et de ne pas surévaluer les recettes."
  "|Un budget équilibré présente des recettes au moins égales aux dépenses ; un déficit prévisionnel exige de rechercher des financements ou de réduire des postes."
  "|La répartition par destination permet de rattacher chaque dépense à une action ou à un service, ce qui est indispensable pour les financeurs."
  "|Le budget est présenté au conseil d'administration, qui l'approuve avant le début de l'exercice, puis il peut être révisé par un budget modificatif."
  "|Un suivi mensuel compare le réalisé au prévisionnel et met en évidence les écarts, afin d'arbitrer en cours d'année."
  "|Pour une structure sociale, le budget n'est pas un simple document comptable : il exprime les priorités de l'action et la capacité à les financer."),
[QC("Quelle est la finalité première d'un budget prévisionnel ?", "Constater les résultats passés~Traduire le projet d'activité en chiffres~Remplacer la comptabilité~Fixer les salaires uniquement", 1,
    "Le budget est une projection qui traduit les objectifs en moyens financiers."),
 QC("Quel réflexe de prudence s'impose avec une subvention non encore attribuée ?", "L'inscrire comme recette certaine~La classer parmi les recettes envisagées~La supprimer du projet~La doubler", 1,
    "Une recette incertaine doit être distinguée des recettes acquises ou probables."),
 QC("Qui approuve généralement le budget d'une association ?", "Le préfet~Le conseil d'administration~Le comptable seul~Les salariés seuls", 1,
    "Le conseil d'administration arrête le budget avant le début de l'exercice."),
 QC("Que permet la répartition par destination ?", "De calculer la TVA~De rattacher les dépenses à une action~De clore les comptes~De payer les fournisseurs", 1,
    "Elle rend visible le coût de chaque service ou action pour les financeurs."),
 QC("Que faire en cas de déficit prévisionnel ?", "Le masquer~Rechercher des financements ou réduire des postes~Attendre la fin d'année~Augmenter les dépenses", 1,
    "Un déficit annoncé impose des arbitrages ou la Recherche de ressources complémentaires."),
 QC("Quel outil permet d'ajuster le budget en cours d'année ?", "Le bilan de clôture~Le budget modificatif~Le grand livre~La balance", 1,
    "Le budget modificatif révise les prévisions sans attendre l'exercice suivant."),
 QC("Que compare le suivi mensuel ?", "Les salaires et les prix~Le réalisé et le prévisionnel~Les recettes et les dettes~Les deux seuls derniers mois", 1,
    "Le suivi budgétaire mesure les écarts entre prévu et réalisé."),
 QT("Un centre social prévoit 400 000 euros de recettes : 250 000 euros de subventions confirmées, 80 000 euros de prestations vendues, 40 000 euros de cotisations et 30 000 euros de dons espérés. Les dépenses prévues totalisent 415 000 euros. Analysez le budget et proposez des arbitrages.",
    "Les recettes certaines ou très probables s'élèvent à 250 000 + 80 000 + 40 000 = 370 000 euros. Si l'on y ajoute les 30 000 euros de dons espérés, on obtient 400 000 euros, soit toujours 15 000 euros de moins que les 415 000 euros de dépenses prévues. Le budget est donc déficitaire de 15 000 euros même en retenant les dons comme acquis, ce qui est imprudent : si les dons ne sont pas obtenus, le déficit atteint 45 000 euros. La première mesure est de ne pas intégrer les dons espérés dans le budget de base, mais de les inscrire en recettes envisagées avec un plan de collecte. Ensuite, plusieurs arbitrages sont possibles : négocier une subvention complémentaire auprès de la collectivité sur la base du projet d'action ; augmenter modérément les tarifs des prestations ou en développer de nouvelles, après étude de l'impact sur les usagers ; rééchelonner certaines dépenses d'équipement sur l'année suivante ; réduire les frais de fonctionnement non prioritaires ; rechercher des partenariats permettant de mutualiser des coûts. Il est préférable de combiner plusieurs leviers plutôt que de concentrer l'effort sur une seule ligne. Le budget révisé doit être présenté au conseil d'administration avec une note explicitant les hypothèses et les risques. Un suivi mensuel des écarts permettra de déclencher des corrections dès le premier semestre plutôt qu'en fin d'exercice.",
    "On attend le calcul du déficit (15 000 euros avec dons, 45 000 sans), la prudence sur les recettes éventuelles et des arbitrages variés et réalistes."),
 QT("Expliquer en quoi un budget prévisionnel est un outil de pilotage et non seulement un document financier, en montrant son lien avec le projet d'action.",
    "Un budget prévisionnel est d'abord la traduction chiffrée d'un projet : chaque ligne de dépense correspond à une action, à un public, à un objectif pédagogique ou social. Le répartir par destination oblige l'équipe à expliciter ses priorités et à renoncer à certaines dépenses, ce qui est déjà une décision de politique d'action. Il devient ensuite un outil de pilotage parce qu'il sert de référence tout au long de l'exercice : un suivi mensuel compare les dépenses et recettes réelles aux prévisions ; un écart Important signale soit une dérive de gestion, soit une hypothèse initiale erronée, soit une évolution du besoin des usagers. L'analyse de l'écart amène des arbitrages : réallouer des crédits d'une action à une autre, rechercher un financement complémentaire, adapter le calendrier. Le budget facilite aussi le dialogue avec les financeurs : il montre comment les moyens publics sont utilisés et quels résultats sont attendus, ce qui renforce la transparence et la reddition de comptes. Enfin, il contribue à la discipline collective : les équipes savent ce qui est prévu, ce qui engage leur responsabilité et ce qui reste à décider. Un budget trop optimiste ou déconnecté des objectifs pédagogiques perd cette fonction : il devient un document formel, vérifié en fin d'année sans avoir jamais servi à décider. Sa qualité dépend donc autant de la discussion qui le précède que de sa rigueur arithmétique.",
    "On attend le lien entre budget et projet, le rôle de référence pour le suivi, les arbitrages, la reddition de comptes et la dimension collective.")],
C("Le budget prévisionnel traduit le projet en moyens : il doit être prudent, discuté, réparti par action et suivi chaque mois.",
  "Recettes certaines + probables ≥ dépenses prévues",
  "Approbation par le conseil d'administration · budget modificatif · écarts analysés",
  "Recette~Ressource prévue~Subvention, don|Destination~Action financée~Analyse par service|Écart~Réalisé moins prévu~Décision à prendre",
  "Partir des objectifs de l'année|Estimer les recettes avec prudence|Chiffrer les dépenses par destination|Présenter et faire approuver le budget|Suivre les écarts chaque mois",
  "Intégrer des dons espérés comme recettes certaines|Présenter un budget déficitaire sans solution|Attendre la clôture pour réagir|Ignorer les remarques des financeurs",
  "400 000 euros~Recettes prévues~415 000 euros~Dépenses prévues~15 000 euros~Déficit avec dons~45 000 euros~Déficit sans dons",
  "Budget initial~Prévision de départ~Budget modificatif~Prévision révisée",
  "Recette acquise~Décidée et sécurisée~Recette envisagée~Incernaine"),
"Réglementation des associations et programmes d'enseignement professionnel, référentiel BTS ESF 2022")

# ============================================================ CT6
add("CT6.", "Suivi budgétaire, écarts et coûts de revient", "Comptabilité et gestion", ["BTS2"],
S("Le suivi budgétaire compare périodiquement les montants réalisés aux montants prévus afin de piloter l'activité."
  "|Un écart est la différence entre le réalisé et le prévisionnel : il peut être favorable ou défavorable selon la nature de la ligne."
  "|Pour une recette, un écart positif est favorable ; pour une charge, un dépassement est défavorable."
  "|L'analyse d'un écart distingue l'écart de prix et l'écart de volume, qui peuvent se compenser ou s'aggraver mutuellement."
  "|Un écart de prix provient d'une variation du coût unitaire des achats ou du prix de vente."
  "|Un écart de volume provient d'une quantité réalisée différente de la quantité prévue, par exemple plus d'usagers accueillis."
  "|Le coût de revient est le coût complet d'un produit ou d'un service : il inclut les charges directes et une part des charges indirectes."
  "|Les charges directes sont affectées sans ambiguïté à un service, comme les denrées d'un repas ; les charges indirectes sont communes, comme le chauffage du bâtiment."
  "|La répartition des charges indirectes repose sur une clé de répartition : nombre d'heures, nombre d'usagers, surface occupée."
  "|Une clé de répartition pertinente doit être liée à la cause réelle de la consommation de ressources, sinon le coût calculé est trompeur."
  "|Le coût unitaire s'obtient en divisant le coût total par le nombre d'unités produites ou de prestations réalisées."
  "|Connaître le coût de revient permet de fixer un tarif, d'évaluer la rentabilité d'une action et d'arbitrer entre mode interne et externe."),
[QC("Quand un écart de charge est-il défavorable ?", "Quand la charge est inférieure au prévu~Quand la charge est supérieure au prévu~Quand la recette augmente~Quand le budget est modifié", 1,
    "Un dépassement de charge réduit le résultat : l'écart est défavorable."),
 QC("Quel écart provient d'une hausse du prix d'achat unitaire ?", "Écart de volume~Écart de prix~Écart de trésorerie~Écart de bilan", 1,
    "L'écart de prix mesure l'impact de la variation du coût unitaire."),
 QC("Qu'est-ce qu'une charge indirecte ?", "Une charge affectée directement à un service~Une charge commune répartie entre plusieurs services~Une recette~Un produit financier", 1,
    "Les charges indirectes nécessitent une clé de répartition, par exemple le chauffage d'un bâtiment partagé."),
 QC("Quelle clé de répartition est pertinente pour le chauffage de locaux ?", "Le nombre de repas servis~La surface occupée par chaque service~Le nombre de factures~L'âge des salariés", 1,
    "La surface occupée est liée à la consommation de chauffage : c'est une clé causale pertinente."),
 QC("Comment calculer un coût unitaire ?", "Coût total multiplié par le nombre d'unités~Coût total divisé par le nombre d'unités~Recettes moins charges~Charges plus produits", 1,
    "Le coût unitaire est le coût total rapporté au nombre d'unités produites."),
 QC("Que permet la connaissance du coût de revient ?", "D'ignorer les subventions~De fixer un tarif et d'évaluer la rentabilité~De supprimer les charges indirectes~De clore le bilan", 1,
    "Le coût de revient éclaire les décisions de tarification et d'allocation des ressources."),
 QC("Que désigne un écart de volume ?", "Une variation du prix unitaire~Une variation de la quantité réalisée~Une variation du taux de TVA~Une variation de la trésorerie", 1,
    "L'écart de volume résulte d'une différence entre quantité prévue et quantité réalisée."),
 QT("Un service de repas prévoyait 10 000 repas à un coût unitaire de 4,50 euros. Il a réalisé 11 000 repas pour un coût total de 52 800 euros. Calculez les écarts de volume et de prix et interprétez-les.",
    "Le coût prévisionnel total était de 10 000 × 4,50 = 45 000 euros. Le coût réel est de 52 800 euros, soit un écart total défavorable de 7 800 euros. Décomposons-le. L'écart de volume, calculé au coût unitaire prévu, vaut (11 000 − 10 000) × 4,50 = 4 500 euros : l'activité a été plus importante que prévu, ce qui augmente mécaniquement le coût global ; cet écart n'est pas necessarily une mauvaise gestion, il traduit une demande plus forte. Le coût unitaire réel est de 52 800 / 11 000 = 4,80 euros. L'écart de prix vaut (4,80 − 4,50) × 11 000 = 3 300 euros : le coût unitaire a augmenté de 0,30 euro par repas. Total : 4 500 + 3 300 = 7 800 euros. L'analyse doit donc porter principalement sur l'écart de prix : augmentation du prix des denrées, gaspillage, main-d'œuvre supplémentaire ou erreur de calibration initiale. L'écart de volume doit être mis en regard des recettes supplémentaires : si chaque repas est factoré, la hausse d'activité peut être favorable malgré la hausse du coût total. Un suivi mensuel permettrait de détecter la dérive du coût unitaire avant la fin de l'exercice et de renégocier les achats ou d'ajuster les portions.",
    "On attend le coût prévisionnel (45 000), l'écart de volume (4 500), le coût unitaire réel (4,80), l'écart de prix (3 300) et une interprétation distincte des deux."),
 QT("Une association hésite à internaliser le nettoyage de ses locaux ou à le confier à un prestataireexterne. Comment le coût de revient éclaire-t-il cette décision ?",
    "La décision ne doit pas se fonder sur le seul prix affiché par le prestataire. Il faut comparer le coût complet des deux options. Pour l'internalisation, on calcule le coût de revient : salaires et charges sociales des agents, temps de travail, fournitures et matériel, part des charges indirectes (chauffage, eau, espace de stockage), temps de pilotage et de contrôle, ainsi que les coûts de remplacement en cas d'absence. Pour l'externalisation, on ajoute au prix du contrat les coûts de sélection et de suivi du prestataire, les éventuels frais de qualification, le coût du contrôle qualité et les clauses de révision de prix. La comparaison doit porter sur une même base de service : surface nettoyée, fréquence, normes de propreté, horaires et responsabilités. Des éléments qualitatifs comptent aussi : continuité du service, connaissance des lieux, confidentialité, conditions de travail des salariés, cohérence avec le projet de l'association. Si l'externalisation est moins chère à court terme mais dégrade les conditions de travail ou la qualité, le gain peut être annulé par des conséquences sociales et réputationnelles. Inversement, internaliser peut être pertinent si l'association a déjà du personnel et peut répartir la charge sur des plages creuses. Une analyse en coût de revient, complétée par une évaluation qualitative et un test sur quelques mois, permet une décision argumentée et défendable devant le conseil d'administration et les financeurs.",
    "On attend la comparaison des coûts complets, l'égalité de la base de comparaison, l'inclusion des charges indirectes et des critères qualitatifs.")],
C("Le suivi budgétaire décompose les écarts en prix et volume ; le coût de revient rend visible le coût complet d'une prestation.",
  "Écart total = écart de prix + écart de volume",
  "Coût de revient = charges directes + charges indirectes réparties",
  "Écart de prix~Variation du coût unitaire~Achats|Écart de volume~Variation de la quantité~Activité|Coût de revient~Coût complet~Tarification",
  "Comparer réalisé et prévisionnel|Calculer l'écart total|Le décomposer en prix et volume|Rechercher la cause de chaque écart|Décider d'une action correctrice",
  "Confondre hausse de volume et mauvaise gestion|Répartir les charges indirectes avec une clé arbitraire|Oublier les coûts de suivi d'un prestataire|Ne regarder que le coût unitaire affiché",
  "10 000 repas~Volume prévu~11 000 repas~Volume réel~4,50 euros~Coût prévu~4,80 euros~Coût réel~7 800 euros~Écart total",
  "Écart de prix~Coût unitaire~Écart de volume~Quantité réalisée",
  "Charge directe~Affectée au service~Charge indirecte~Répartie par une clé"),
"Contrôle de gestion et programmes d'enseignement professionnel, référentiel BTS ESF 2022")

if __name__ == "__main__":
    valider_et_ecrire(F, "btsesf-mat-part-B.json")
