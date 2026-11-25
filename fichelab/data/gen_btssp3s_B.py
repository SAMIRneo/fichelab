# -*- coding: utf-8 -*-
"""Generateur btssp3s-mat-part-B.json — lot B : Droit (7), Économie (6),
Santé publique et environnement professionnel (7).

20 fiches 'prototype' pour la filiere bts-sp3s (BTS1 / BTS2) :
12 points de cours, 9 questions corrigees (7 QCM + 2 texte),
7 blocs en ordre strict, 3 schemas via diag().
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _btssp3s_common import S, R, QC, QT, C, build, valider_et_ecrire

F = []


def add(prefix, titre, mat, ans, points, questions, c):
    F.append(build(prefix, titre, mat, ans, points, questions, c))


# ============================================================ DR1
add("DR1", "Droits des usagers et libertés fondamentales", "Droit", ["BTS1"],
S("Les droits des usagers encadrent la relation entre une personne accompagnée et un établissement sanitaire ou social."
  "|La loi du 2 janvier 2002 rénovant l'action sociale et médico-sociale a renforcé ces droits et la place de la personne."
  "|La loi du 4 mars 2002 relative aux droits des malades et à la qualité du système de santé a consacré le consentement et l'information."
  "|Le Code de l'action sociale et des familles contient les dispositions applicables aux établissements et services sociaux."
  "|La charte des droits et libertés de la personne accueillie, fixée par arrêté, affirme la dignité, l'égalité et la neutralité."
  "|Le droit à l'information implique une information claire, accessible et adaptée à la situation de la personne."
  "|La continuité de l'accompagnement interdit toute interruption injustifiée de la prise en charge."
  "|Le respect de la vie privée et de l'intimité s'impose dans les actes quotidiens comme dans les dossiers."
  "|La personne participe aux décisions qui la concernent : elle est actrice de son parcours."
  "|Le livret d'accueil, le règlement de fonctionnement et le contrat de séjour sont des documents obligatoires."
  "|Le conseil de vie sociale et les dispositifs de médiation permettent d'exprimer une difficulté et de la traiter."
  "|Le référentiel BTS SP3S place les droits des usagers parmi les savoirs associés du bloc 3."),
[QC("Quelle loi a rénové l'action sociale et médico-sociale en 2002 ?", "La loi du 2 janvier 2002~La loi du 4 mars 2002~La loi du 6 janvier 1978~La loi du 29 juillet 2015", 0,
    "La loi du 2 janvier 2002 rénovant l'action sociale et médico-sociale est le texte de référence."),
 QC("Quel principe est affirmé par la charte des droits et libertés de la personne accueillie ?", "La seule efficacité administrative~La dignité et l'égalité de traitement~La priorité aux plus anciens~La discrétion du service", 1,
    "Dignité, égalité, neutralité et continuité sont des principes fondamentaux."),
 QC("Quel document est remis à la personne à son arrivée dans un établissement ?", "Le livret d'accueil~Le bilan comptable~Le plan de formation~Le registre des achats", 0,
    "Le livret d'accueil informe la personne de ses droits et du fonctionnement du service."),
 QC("Qu'appelle-t-on continuité de l'accompagnement ?", "Une présence permanente d'un seul agent~L'absence d'interruption injustifiée de la prise en charge~Une réunion quotidienne~Un accueil sans rendez-vous", 1,
    "La continuité protège la personne d'une rupture de prise en charge."),
 QC("Quel dispositif permet d'exprimer une difficulté collective ?", "Le conseil de vie sociale~Le conseil d'administration seul~Le service comptable~La direction générale uniquement", 0,
    "Le conseil de vie sociale est un espace d'expression et de médiation des usagers."),
 QC("Quelle attitude respecte la vie privée d'un usager ?", "Évoquer sa situation dans un couloir~Éviter toute mention inutile dans les échanges~Raconter son histoire aux collègues~Exposer son dossier sur un écran partagé", 1,
    "La discrétion s'impose dans les paroles, les écrans et les documents."),
 QC("Dans quel bloc du référentiel BTS SP3S figurent les droits des usagers ?", "Bloc 1~Bloc 2~Bloc 3~Bloc 4", 2,
    "Le bloc 3 traite de la politique de la structure sur le territoire et inclut les droits des usagers."),
 QT("Expliquer la différence entre droit à l'information et consentement et montrer leur lien dans un accompagnement.",
    "Le droit à l'information impose au professionnel de transmettre des éléments clairs, compréhensibles et adaptés sur la situation, les prestations possibles, les délais et les alternatives. Le consentement est l'accord libre et éclairé de la personne à une action ou à une prestation : il suppose une information préalable, une capacité de compréhension et l'absence de pression. Le lien est direct : sans information de qualité, le consentement n'est pas éclairé et n'a donc pas de valeur réelle. Dans un accompagnement, on présente les options, on vérifie la compréhension par reformulation, on laisse un temps de réflexion et on recueille l'accord avant d'engager la démarche. Le refus doit être respecté et tracé, sauf situation d'urgence prévue par la loi.",
    "On définit les deux droits et on montre que l'information est la condition d'un consentement valable."),
 QT("Un usager se plaint d'avoir été transféré d'un service à l'autre sans explication. Quels droits sont en cause et comment y répondre ?",
    "Plusieurs droits sont engagés : le droit à l'information, car les motifs et les circuits n'ont pas été expliqués ; la continuité de l'accompagnement, car le parcours a été rompu ; et le respect de la dignité, car la personne a été traitée comme un dossier qui circule. La réponse commence par une écoute sans mise en cause de l'usager, puis par une restitution factuelle du parcours : qui a décidé le transfert, pourquoi et avec quelles suites prévues. On propose un interlocuteur unique, une explication écrite et, si nécessaire, l'intervention du conseil de vie sociale ou d'un médiateur. On trace la réclamation dans le registre et on l'analyse en réunion de service pour améliorer le circuit, car un droit non respecté révèle souvent une organisation défaillante.",
    "On identifie les droits, on propose une réponse individuelle et une correction collective tracée.")],
C("Les droits des usagers transforment la personne en actrice de son parcours et obligent le service à la transparence.",
  "Dignité + information + participation + continuité",
  "Loi 2 janvier 2002 (social) · loi 4 mars 2002 (santé) · charte · livret d'accueil",
  "Loi 2002-2~Action sociale~Loi 2002-303~Droits des malades~Charte~Droits et libertés~Livret~Information",
  "Repérer le droit en cause|Écouter la personne sans la juger|Restituer les faits et les circuits|Proposer un interlocuteur et une trace|Corriger collectivement le dysfonctionnement",
  "Répondre par une consigne administrative sèche|Transférer sans explication|Évoquer le cas dans un couloir|Ignorer le registre des réclamations",
  "Réclamation~Transfert sans explication~Droit~Information et continuité~Réponse~Interlocuteur unique~Correction~Analyse en service",
  "Information~Comprendre la situation~Consentement~Accepter librement",
  "Dignité~Respect de la personne~Efficacité~Seule négligée"))

# ============================================================ DR2
add("DR2", "Secret professionnel et partage d'informations", "Droit", ["BTS1"],
S("Le secret professionnel est une obligation de confidentialité qui s'impose à certaines professions, dont celles du secteur sanitaire et social."
  "|L'article 226-13 du Code pénal réprime la divulgation d'une information confidentielle par une personne tenue au secret."
  "|Le secret couvre ce qui a été confié, vu ou entendu dans l'exercice de la profession."
  "|Il s'impose aussi hors du service et après la fin de la relation de travail."
  "|Le secret est une protection de la personne, pas un outil de dissimulation de la part du professionnel."
  "|L'article 226-14 du Code pénal prévoit des exceptions, notamment le partage entre professionnels pour la prise en charge."
  "|Le partage doit se limiter aux informations nécessaires aux personnes qui participent à l'accompagnement."
  "|Un danger pour la santé ou la sécurité peut justifier une information à une autorité habilitée."
  "|Le secret professionnel est distinct du devoir de réserve et du secret des affaires."
  "|La tenue du dossier, les transmissions écrites et les échanges oraux sont tous soumis à la même exigence."
  "|Les écrans, les courriels et les documents papier doivent être protégés contre les regards non autorisés."
  "|Le référentiel BTS SP3S associe ce savoir au cadre juridique de la communication professionnelle et à l'éthique."),
[QC("Quel article du Code pénal réprime la violation du secret professionnel ?", "L'article 1240~L'article 226-13~L'article L1111-2~L'article 226-14", 1,
    "L'article 226-13 du Code pénal définit et réprime la violation du secret professionnel."),
 QC("Que couvre le secret professionnel ?", "Seules les paroles écrites~Ce qui a été confié, vu ou entendu dans l'exercice professionnel~Les seules données de santé~Les seuls échanges avec la direction", 1,
    "Le secret porte sur toute information appréhendée dans l'exercice de la profession."),
 QC("Quel partage est autorisé par l'exception de l'article 226-14 ?", "Raconter un dossier à un ami~Transmettre les éléments utiles aux professionnels qui assurent la prise en charge~Publier un témoignage~Informer tous les services sans sélection", 1,
    "Le partage entre professionnels est autorisé dans la mesure nécessaire à la prise en charge."),
 QC("Le secret cesse-t-il à la fin de la relation de travail ?", "Oui, immédiatement~Non, il demeure~Oui, après un an~Oui, si l'agent démissionne", 1,
    "L'obligation survit à la fin de l'activité professionnelle."),
 QC("Quelle pratique protège la confidentialité sur un poste de travail ?", "Laisser l'écran ouvert~Verrouiller l'écran et limiter les impressions~Écrire les noms sur un post-it~Partager un mot de passe", 1,
    "Verrouillage et limitation des supports réduisent les accès indiscrètes."),
 QC("Quelle situation peut justifier une information à une autorité ?", "Une simple curiosité~Un danger pour la santé ou la sécurité d'une personne~Une demande d'un collègue curieux~Un pari entre agents", 1,
    "La protection contre un danger est une exception légalement encadrée."),
 QC("Quel principe limite le partage même lorsqu'il est autorisé ?", "La rapidité~La stricte nécessité des informations transmises~La quantité de détails~L'habitude du service", 1,
    "On transmet seulement ce qui est utile à ceux qui participent à l'accompagnement."),
 QT("Expliquer pourquoi le secret professionnel protège la personne plutôt que le professionnel.",
    "Le secret garantit que ce qu'une personne révèle dans un cadre d'aide ne sera pas diffusé au-delà de ce qui est nécessaire à son accompagnement. C'est cette garantie qui rend possible la confiance et donc l'expression de la demande réelle : sans elle, la personne se tait et l'accompagnement devient inefficace. Le secret n'autorise pas le professionnel à taire une situation qu'il a lui-même mal traitée : il ne couvre ni la faute, ni l'absence de transmission interne prévue par la procédure. Il impose une discipline de parole, d'écriture et de stockage, et il survit à la fin du service. Ainsi, la confidentialité est un droit de la personne et une obligation du professionnel, non un privilège personnel.",
    "On montre le lien entre confidentialité, confiance et efficacité de l'accompagnement, et on précise les limites."),
 QT("Un collègue d'un autre service demande des détails sur la situation familiale d'un usager sans lien avec sa prise en charge. Que faire ?",
    "On ne répond pas à la demande, même si le collègue est habilité dans son propre service : le secret s'apprécie au regard de la finalité de l'information, pas du seul statut de la personne qui demande. On peut répondre de manière générale sur la procédure à suivre sans révéler d'élément personnel, et orienter le collègue vers le circuit prévu : demande écrite motivée, validation du responsable et transmission du minimum nécessaire. On rappelle avec tact la règle applicable au service, sans accuser le collègue de mauvaise intention. Si la demande devient insistante ou vise un usage étranger à l'accompagnement, on en réfère au responsable hiérarchique et on trace l'incident selon la procédure interne.",
    "On refuse sans détour, on propose le circuit légal, on évite l'accusation et on sait escalader.")],
C("Le secret professionnel garantit la confiance de la personne : on ne transmet que le nécessaire, aux seuls professionnels concernés.",
  "Secret = protection de la personne · partage = nécessité et finalité",
  "Code pénal 226-13 : violation · 226-14 : exceptions encadrées",
  "Secret~Obligation de confidentialité~Confiance~Condition de l'aide~Exception~Partage nécessaire~Danger~Information autorisée",
  "Repérer la finalité de la demande|Vérifier l'habilitation du destinataire|Transmettre le minimum utile|Protéger les supports|Tracer les demandes inhabituelles",
  "Raconter un dossier par habitude|Confondre collègue et finalité de soin|Laisser un écran ouvert|Invoquer le secret pour taire une faute",
  "Demande~Détails familiaux~Réponse~Refus motivé~Circuit~Validation du responsable~Trace~Incident consigné",
  "Secret professionnel~Protège la personne~Secret des affaires~Protège l'organisation",
  "Partage autorisé~Nécessaire à la prise en charge~Curiosité~Jamais autorisée"))

# ============================================================ DR3
add("DR3", "Information et consentement de la personne accompagnée", "Droit", ["BTS2"],
S("L'information et le consentement sont deux droits étroitement liés pour toute personne accompagnée par un service social ou médico-social."
  "|La loi du 4 mars 2002 et le Code de la santé publique imposent une information claire sur l'état, les prestations et les risques."
  "|L'article L1111-2 du Code de la santé publique précise le contenu de l'information due à la personne."
  "|Le consentement doit être libre, éclairé et révocable : la personne peut revenir sur son accord."
  "|Un consentement éclairé suppose que la personne ait compris les alternatives et les conséquences prévisibles."
  "|La personne de confiance, désignée par écrit, peut accompagner les démarches et être consultée."
  "|Les directives anticipées expriment à l'avance les souhaits relatifs à des situations futures."
  "|L'information est adaptée au niveau de compréhension, au handicap éventuel et à la langue de la personne."
  "|Le professionnel vérifie la compréhension par reformulation plutôt que par une simple question « avez-vous compris ? »."
  "|Un refus doit être entendu et tracé, sans pression ni représailles."
  "|En situation d'urgence, la loi autorise des interventions impossibles à différer, dans l'intérêt de la personne."
  "|Le référentiel BTS SP3S rattache ces savoirs à la relation d'accompagnement et au bloc 3."),
[QC("Quelles qualités doit avoir un consentement valable ?", "Rapide, oral et implicite~Libre, éclairé et révocable~Écrit, public et collectif~Permanent et irréversible", 1,
    "Le consentement est libre, éclairé et peut être retiré."),
 QC("Que prévoit l'article L1111-2 du Code de la santé publique ?", "Le budget des hôpitaux~Le contenu de l'information due à la personne~Le recrutement des agents~Les horaires d'accueil", 1,
    "Cet article définit les informations à communiquer à la personne."),
 QC("Quel rôle a la personne de confiance ?", "Remplacer le médecin~Accompagner la personne et être consultée~Signer à la place de l'usager~Décider seule", 1,
    "Elle accompagne et est consultée, sans se substituer à la personne."),
 QC("À quoi servent les directives anticipées ?", "À organiser le budget~À exprimer à l'avance des souhaits pour des situations futures~À nommer un responsable~À remplacer le consentement", 1,
    "Elles font connaître les volontés de la personne pour une situation ultérieure."),
 QC("Comment vérifier la compréhension d'une information ?", "En demandant « avez-vous compris ? »~En demandant une reformulation par la personne~En parlant plus fort~En donnant plus de documents", 1,
    "La reformulation par la personne révèle ce qui a réellement été compris."),
 QC("Quelle suite donner à un refus de la personne ?", "Le contourner~Le respecter et le tracer~Le faire valider par la famille~Le transformer en accord", 1,
    "Le refus est un droit qui doit être consigné et respecté."),
 QC("Que permet la situation d'urgence ?", "Toutes les dérogations sans limite~Une intervention impossible à différer dans l'intérêt de la personne~Le retrait du consentement systématique~L'absence de traçabilité", 1,
    "L'urgence est une exception strictement encadrée."),
 QT("Expliquer la chaîne qui va de l'information au consentement et identifier les points où le professionnel doit vérifier la compréhension.",
    "La chaîne comporte cinq maillons. D'abord, le professionnel identifie les informations utiles : situation, prestations envisageables, alternatives, délais et risques. Ensuite, il les transmet dans un langage accessible, avec des supports adaptés si nécessaire. Troisièmement, il vérifie la compréhension en demandant à la personne de reformuler ce qu'elle a retenu, plutôt que de poser une question fermée. Quatrièmement, il laisse un temps de réflexion et recueille l'accord sans pression, en présence de la personne de confiance si elle le souhaite. Cinquièmement, il trace l'accord ou le refus dans le dossier. La vérification intervient donc après chaque information importante et avant la décision, car un consentement donné sur une compréhension erronée n'est pas valable.",
    "On décrit la chaîne étape par étape et on place les vérifications aux bons endroits."),
 QT("Une personne âgée refuse une orientation proposée par le service alors que la famille insiste. Comment le professionnel doit-il agir ?",
    "Le professionnel considère d'abord que la personne est titulaire de ses droits : le refus d'une orientation lui appartient, même si la famille est inquiète. Il vérifie que l'information délivrée était complète et comprise, en proposant un entretien de reprise avec des mots simples et, si la personne le souhaite, sa personne de confiance. Il explore les raisons du refus : peur du changement, méconnaissance du dispositif ou préférence pour rester à domicile. Il peut proposer des alternatives moins engageantes, sans chercher à obtenir l'accord par pression. Il trace le refus et l'information délivrée dans le dossier. Il informe la famille du cadre légal sans révéler d'éléments couverts par le secret professionnel. Si la sécurité de la personne est en cause, il suit la procédure d'alerte prévue par l'établissement.",
    "On affirme la primauté du consentement de la personne, on vérifie la compréhension, on trace et on gère la famille dans le respect du secret.")],
C("Informer, c'est rendre la personne capable de choisir ; consentir, c'est choisir librement après avoir compris.",
  "Information comprise + temps de réflexion + accord libre = consentement valable",
  "Libre · éclairé · révocable · tracé · personne de confiance · directives anticipées",
  "Information~Éléments transmis~Compréhension~Reformulée~Consentement~Accord libre~Refus~Droit tracé",
  "Identifier les informations utiles|Adapter le langage et les supports|Vérifier par reformulation|Laisser un temps de réflexion|Recueillir et tracer l'accord ou le refus",
  "Poser une question fermée de compréhension|Presser la personne|Confondre accord de la famille et consentement|Oublier de tracer le refus",
  "Personne âgée~Refus d'orientation~Vérification~Information reprise~Alternative~Accompagnement à domicile~Trace~Décision inscrite",
  "Information~Donner à comprendre~Consentement~Décider librement",
  "Consentement~Révocable~Directives anticipées~Pour une situation future"))

# ============================================================ DR4
add("DR4", "Protection des données personnelles et RGPD", "Droit", ["BTS2"],
S("Le Règlement général sur la protection des données (RGPD) est le règlement européen 2016/679 applicable depuis 2018."
  "|Il est complété en France par la loi Informatique et Libertés du 6 janvier 1978, modifiée en 2018."
  "|Une donnée personnelle est toute information relative à une personne physique identifiée ou identifiable."
  "|Les données de santé sont des catégories particulières de données, protégées plus strictement."
  "|Les principes clés sont la licéité, la finalité, la minimisation, l'exactitude et la limitation de la conservation."
  "|La minimisation impose de ne collecter que les données nécessaires à la finalité déclarée."
  "|La base légale du traitement doit être identifiée : consentement, obligation légale, intérêt vital ou mission d'intérêt public."
  "|Les personnes disposent de droits : accès, rectification, effacement, limitation, opposition et portabilité."
  "|Le délégué à la protection des données veille au respect des règles et conseille l'organisation."
  "|Le registre des traitements documente les finalités, les catégories de données et les destinataires."
  "|Une violation de données doit être notifiée à la CNIL dans les soixante-douze heures lorsqu'elle présente un risque."
  "|Le référentiel BTS SP3S associe ces règles à la protection de l'information et aux enjeux du numérique professionnel."),
[QC("Quel texte européen régit la protection des données depuis 2018 ?", "La directive 2002-2~Le RGPD (règlement 2016/679)~La loi du 4 mars 2002~Le Code du travail", 1,
    "Le RGPD est le règlement européen 2016/679, applicable depuis mai 2018."),
 QC("Quelle donnée est une catégorie particulière protégée plus strictement ?", "Une adresse e-mail professionnelle~Une donnée de santé~Un numéro de poste~Une couleur de dossier", 1,
    "Les données de santé figurent parmi les catégories sensibles du RGPD."),
 QC("Quel principe impose de ne collecter que le nécessaire ?", "La conservation illimitée~La minimisation~La publicité systématique~Le partage maximal", 1,
    "La minimisation limite la collecte aux données utiles à la finalité."),
 QC("Quel droit permet à une personne d'obtenir une copie de ses données ?", "Le droit d'opposition~Le droit d'accès~Le droit à l'oubli uniquement~Le droit de rectification seul", 1,
    "Le droit d'accès permet d'obtenir une copie et des informations sur le traitement."),
 QC("Qui conseille l'organisation sur la protection des données ?", "Le comptable~Le délégué à la protection des données~Le responsable des achats~Le secrétaire de direction", 1,
    "Le DPO veille à la conformité et conseille les responsables du traitement."),
 QC("Quel délai s'impose pour notifier une violation présentant un risque à la CNIL ?", "Vingt-quatre heures~Soixante-douze heures~Une semaine~Un mois", 1,
    "La notification à l'autorité de contrôle intervient dans les 72 heures."),
 QC("Quelle base légale peut fonder un traitement de données de santé par un établissement social ?", "Le seul caprice du responsable~Une obligation légale ou une mission d'intérêt public~Une publicité commerciale~Un usage non déclaré", 1,
    "Le traitement doit reposer sur une base légale identifiée et documentée."),
 QT("Expliquer la différence entre secret professionnel et RGPD et montrer comment ils se complètent.",
    "Le secret professionnel est une obligation de confidentialité personnelle : il interdit à une personne habilitée de divulguer ce qu'elle a appris dans l'exercice de son métier, y compris après la fin de son activité. Le RGPD est un cadre juridique organisationnel : il impose à la structure de définir les finalités des traitements, de limiter les données collectées, de sécuriser les supports, de documenter les accès et de respecter les droits des personnes. Le secret répond surtout à la question « qui peut dire quoi à qui », tandis que le RGPD répond à « comment les données sont collectées, conservées et protégées ». Ils se complètent : une donnée de santé peut être traitée légalement au titre du RGPD mais rester couverte par le secret professionnel dans les échanges entre agents.",
    "On distingue l'obligation individuelle de confidentialité du cadre organisationnel de conformité, puis on montre leur complémentarité."),
 QT("Une clé USB contenant des dossiers d'usagers est perdue. Décrire la réaction conforme au RGPD.",
    "On identifie d'abord la nature des données et le nombre de personnes concernées, puis on évalue le risque : des données de santé non chiffrées exposent les personnes à un risque élevé. On prévient immédiatement le responsable du traitement et le délégué à la protection des données. On vérifie si un chiffrement rend les données inintelligibles, car cela peut réduire l'obligation de notification. Si le risque reste réel, on notifie la CNIL dans les soixante-douze heures et on informe les personnes concernées sans délai lorsque le risque est élevé. On documente l'incident dans le registre des violations, on prend les mesures conservatoires : révocation des accès, vérification des copies, diffusion d'une consigne sur l'usage des supports amovibles. Enfin, on analyse la cause et on forme les équipes pour éviter la récidive.",
    "On attend évaluation du risque, DPO, notification à 72 heures, information des personnes, registre et mesures correctives.")],
C("Le RGPD organise la collecte et la sécurité des données ; le secret professionnel limite leur divulgation.",
  "Licéité + finalité + minimisation + sécurité + droits",
    "DPO · registre des traitements · notification CNIL 72 h · données de santé = catégorie sensible",
  "RGPD~Règlement européen~Minimisation~Données nécessaires~DPO~Conseil et contrôle~CNIL~Notification à 72 h",
  "Identifier la finalité du traitement|Vérifier la base légale|Limiter les données collectées|Documenter et sécuriser les accès|Notifier et tracer tout incident",
  "Collecter « au cas où »|Partager un mot de passe|Ignorer une violation|Conserver les dossiers indéfiniment",
  "Clé USB~Perte de support~Risque~Données de santé~Action~Notification CNIL~Prévention~Chiffrement et consigne",
  "Secret professionnel~Obligation individuelle~RGPD~Cadre organisationnel",
  "Droit d'accès~Obtenir une copie~Droit d'effacement~Supprimer les données"))

# ============================================================ DR5
add("DR5", "Responsabilité civile et professionnelle du personnel", "Droit", ["BTS2"],
S("La responsabilité civile oblige une personne à réparer le dommage causé à autrui par sa faute."
  "|L'article 1240 du Code civil pose le principe de la responsabilité du fait personnel : toute faute qui cause un dommage oblige son auteur à le réparer."
  "|La responsabilité contractuelle s'applique lorsqu'un contrat existe, par exemple entre un établissement et un usager."
  "|La responsabilité du fait des choses, prévue à l'article 1242, s'applique quand un objet sous notre garde cause un dommage."
  "|En établissement, la responsabilité de l'employeur peut être engagée pour les actes de ses salariés dans l'exercice de leurs fonctions."
  "|Une faute professionnelle est un manquement aux obligations du poste : erreur de transmission, négligence ou refus de procédure."
  "|La faute grave peut entraîner une sanction disciplinaire distincte de la réparation civile."
  "|L'assurance responsabilité civile professionnelle couvre les dommages causés dans l'exercice du métier, selon les garanties souscrites."
  "|La souscription d'une assurance ne supprime pas l'obligation de prudence et de diligence."
  "|La prévention des dommages passe par des procédures écrites, des transmissions tracées et la formation."
  "|En cas d'incident, les faits sont consignés sans déguisement : une documentation fidèle protège la personne et le professionnel."
  "|Le référentiel BTS SP3S rattache ces notions au cadre juridique de la communication et à la qualité du service."),
[QC("Quel article du Code civil pose la responsabilité du fait personnel ?", "L'article 1240~L'article 226-13~L'article L1111-4~L'article 1101", 0,
    "L'article 1240 du Code civil est le fondement de la responsabilité délictuelle."),
 QC("Quand s'applique la responsabilité contractuelle ?", "Lorsqu'aucun lien n'existe~Lorsqu'un contrat existe entre les parties~Uniquement en cas d'urgence~Uniquement entre collègues", 1,
    "La responsabilité contractuelle découle de manquements à un contrat."),
 QC("Quel article concerne la responsabilité du fait des choses ?", "1240~1242~1384~226-14", 1,
    "L'article 1242 du Code civil vise les dommages causés par une chose dont on a la garde."),
 QC("Quand la responsabilité de l'employeur peut-elle être engagée ?", "Pour les actes personnels du salarié hors service~Pour les actes du salarié dans l'exercice de ses fonctions~Jamais~Uniquement le week-end", 1,
    "L'employeur répond des actes de ses salariés accomplis dans le cadre de leurs fonctions."),
 QC("Quel élément constitue une faute professionnelle ?", "Une erreur de transmission sans conséquence et non tracée~Un manquement aux obligations du poste~Une opinion personnelle~Une demande de formation", 1,
    "Le manquement à une obligation professionnelle caractérise la faute."),
 QC("Que couvre l'assurance responsabilité civile professionnelle ?", "Tous les dommages sans limite~Les dommages causés dans l'exercice du métier selon les garanties~Les seuls dommages corporels~Les seuls conflits entre collègues", 1,
    "La couverture dépend des garanties souscrites et de l'activité exercée."),
 QC("Quel geste contribue à la prévention des dommages ?", "Laisser une procédure implicite~Tracer les transmissions et former les équipes~Supprimer les écrits~Éviter les réunions", 1,
    "Procédures écrites, traçabilité et formation réduisent le risque de faute."),
 QT("Distinguer responsabilité civile et responsabilité disciplinaire à propos d'une erreur de transmission.",
    "La responsabilité civile vise la réparation d'un dommage subi par autrui : si une erreur de transmission entraîne un retard de prise en charge et un préjudice pour l'usager, la personne ou l'établissement peut être condamné à réparer ce dommage. La responsabilité disciplinaire est interne : elle sanctionne le manquement du salarié à ses obligations professionnelles, indépendamment de l'existence d'un dommage réparable, et peut aller de l'avertissement à la exclusion définitive selon la gravité. Les deux procédures sont distinctes et peuvent se cumuler : un agent peut être sanctionné par son employeur et l'établissement peut devoir réparer le préjudice. Dans les deux cas, la qualité de la documentation des faits est essentielle, car elle permet d'établir ce qui s'est réellement passé.",
    "On sépare réparation du dommage et sanction interne, et on montre qu'elles peuvent se cumuler."),
 QT("Un dossier est transmis avec une pièce manquante et l'usager perd un rendez-vous. Quelle est la démarche professionnelle ?",
    "On constate d'abord les faits : quelle pièce manquait, qui devait la transmettre, à quelle heure et avec quelle consigne. On prévient le responsable hiérarchique sans chercher à masquer l'erreur, on informe l'usager avec franchise et on lui propose une nouvelle date dans les plus brefs délais, en prenant en charge les démarches supplémentaires. On consigne l'incident dans le registre prévu et dans le dossier, en distinguant les faits des hypothèses. On analyse ensuite la cause : pièce non réclamée dans la checklist, circuit trop rapide ou consigne ambiguë. On propose une mesure corrective, par exemple une liste de contrôle avant transmission, et on la formalise. Si un préjudice est établi, l'assurance responsabilité civile professionnelle est saisie selon la procédure de l'établissement.",
    "On attend une transmission honnête, la réparation concrète pour l'usager, la trace écrite et l'analyse de cause.")],
C("La responsabilité n'est pas évitée par une assurance : elle se prévient par la prudence, les procédures et la trace écrite.",
  "Faute + dommage + lien de causalité = réparation",
  "Code civil 1240 et 1242 · responsabilité contractuelle · assurance RC Pro",
  "Faute~Manquement au poste~Dommage~Préjudice subi~Réparation~Rétablir la situation~Assurance~Garanties souscrites",
  "Constater les faits sans les déguiser|Prévenir la hiérarchie|Réparer le préjudice pour l'usager|Consigner et analyser la cause|Formaliser la mesure corrective",
  "Masquer l'erreur|Compter sur l'assurance pour ne rien changer|Écrire une version favorable|Laisser la procédure implicite",
  "Erreur~Pièce manquante~Dommage~Rendez-vous perdu~Correctif~Checklist~Assurance~Déclaration interne",
  "Responsabilité civile~Réparer autrui~Responsabilité disciplinaire~Sanctionner l'agent",
  "Prévention~Agir avant~Réparation~Agir après le dommage"))

# ============================================================ DR6
add("DR6", "Cadre juridique des établissements sanitaires et sociaux", "Droit", ["BTS2"],
S("Les établissements sanitaires, sociaux et médico-sociaux exercent dans un cadre légal et réglementaire précis."
  "|La loi du 2 janvier 2002 organise l'autorisation de création et de fonctionnement de ces établissements."
  "|L'autorisation est délivrée par l'agence régionale de santé, qui contrôle également la qualité et la sécurité des prestations."
  "|Les établissements peuvent être publics, associatifs ou privés commerciaux, avec des statuts et des règles de gestion différents."
  "|Le projet d'établissement définit les orientations, les prestations et les objectifs de la structure."
  "|Le règlement de fonctionnement précise les règles de la vie collective et les droits et obligations de chacun."
  "|Le livret d'accueil et le contrat de séjour informent la personne accompagnée de ses droits et des prestations proposées."
  "|Le conseil de vie sociale associe les usagers et leurs représentants à la vie de l'établissement."
  "|Les inspections et contrôles vérifient la conformité des locaux, des personnels et des pratiques."
  "|Les conventions avec les autorités et les partenaires définissent les missions et les financements."
  "|Les normes d'hygiène et de sécurité s'imposent à tous les services, y compris aux services administratifs."
  "|Le référentiel BTS SP3S attend la connaissance des établissements, réseaux et dispositifs aux différents échelons."),
[QC("Quelle autorité délivre l'autorisation de fonctionnement des établissements sociaux et médico-sociaux ?", "La mairie~L'agence régionale de santé~La chambre de commerce~Le tribunal administratif seul", 1,
    "L'ARS est l'autorité qui autorise et contrôle ces établissements."),
 QC("Quel document définit les orientations et objectifs de la structure ?", "Le projet d'établissement~Le bon de commande~Le planning de permanences~Le registre des réclamations", 0,
    "Le projet d'établissement fixe les orientations et les prestations."),
 QC("Quel document précise les règles de la vie collective ?", "Le contrat de travail~Le règlement de fonctionnement~Le budget prévisionnel~La fiche de poste", 1,
    "Le règlement de fonctionnement organise la vie collective et les obligations de chacun."),
 QC("Qu'appelle-t-on conseil de vie sociale ?", "Un organe de direction seul~Une instance qui associe les usagers à la vie de l'établissement~Un service comptable~Une réunion du personnel", 1,
    "Le conseil de vie sociale est une instance de participation des usagers."),
 QC("Quel contrôle porte sur la conformité des pratiques ?", "Le contrôle qualité interne uniquement~L'inspection des autorités de tutelle~Le sondage auprès des fournisseurs~La réunion de service", 1,
    "Les autorités de contrôle vérifient la conformité aux textes."),
 QC("Quel point est commun à tous les types d'établissements ?", "Le statut associatif~Les normes d'hygiène et de sécurité~Le financement identique~La même direction", 1,
    "Hygiène et sécurité s'imposent quel que soit le statut."),
 QC("À quoi servent les conventions de partenariat ?", "À définir missions et financements entre acteurs~À remplacer le projet d'établissement~À supprimer les contrôles~À choisir les horaires", 0,
    "Les conventions formalisent les engagements entre la structure et ses partenaires."),
 QT("Expliquer la complémentarité du projet d'établissement, du règlement de fonctionnement et du contrat de séjour.",
    "Ces trois documents agissent à des niveaux complémentaires. Le projet d'établissement est un document stratégique : il définit les orientations, les publics accueillis, les prestations et les objectifs de la structure sur plusieurs années. Le règlement de fonctionnement est un document collectif : il organise la vie quotidienne, les règles de cohabitation, les horaires, la sécurité et les obligations de chacun dans l'établissement. Le contrat de séjour est un document individuel : il engage la structure envers une personne précise en précisant les prestations dispensées, les conditions de l'accompagnement et les modalités d'évolution. Le premier donne le cap, le deuxième cadre la vie commune, le troisième protège la personne dans son parcours individuel.",
    "On distingue les niveaux stratégique, collectif et individuel, et on montre leur complémentarité."),
 QT("Un établissement associatif souhaite ouvrir un nouveau service d'accueil. Quelles démarches et quels documents sont à prévoir ?",
    "On vérifie d'abord la compatibilité du projet avec les orientations de l'établissement et les besoins identifiés sur le territoire. On prépare une demande d'autorisation auprès de l'agence régionale de santé, avec un dossier décrivant le public, les prestations, les locaux, les personnels, le budget prévisionnel et les mesures d'hygiène et de sécurité. On actualise le projet d'établissement et on rédige le règlement de fonctionnement adapté au nouveau service. On prévoit le livret d'accueil et le contrat de séjour, ainsi que les modalités de participation des usagers, par exemple un conseil de vie sociale dédié. On négocie les conventions avec les partenaires et les financeurs, puis on organise la formation des agents avant l'ouverture. Enfin, on se prépare aux contrôles de conformité en constituant le dossier documentaire complet.",
    "On attend autorisation ARS, documents internes, participation des usagers, conventions et préparation aux contrôles.")],
C("Un établissement sécurise son action par des documents obligatoires et par le contrôle de l'autorité publique.",
  "Autorisation ARS + projet + règlement + contrat de séjour",
  "Loi 2 janvier 2002 · ARS · conseil de vie sociale · inspection",
  "ARS~Autorisation et contrôle~Projet~Orientations de la structure~Règlement~Vie collective~Contrat de séjour~Engagement individuel",
  "Vérifier la compatibilité du projet|Préparer le dossier d'autorisation|Actualiser les documents internes|Organiser la participation des usagers|Constituer le dossier de conformité",
  "Ouvrir sans autorisation|Négliger le règlement de fonctionnement|Ignorer les normes d'hygiène|Laisser les usagers sans instance de participation",
  "Nouveau service~Projet d'établissement~Autorisation~Dossier ARS~Contrat~Séjour individualisé~Contrôle~Dossier complet",
  "Projet d'établissement~Niveau stratégique~Contrat de séjour~Niveau individuel",
  "Public~Établissement public~Associatif~Statut privé à but non lucratif"))

# ============================================================ DR7
add("DR7", "Droits sociaux et principales prestations", "Droit", ["BTS2"],
S("Les droits sociaux sont des droits accordés par la loi pour garantir des ressources, une couverture de santé et un accompagnement."
  "|Ils relèvent de plusieurs branches : sécurité sociale, aide sociale, logement, emploi et handicap."
  "|La sécurité sociale comprend l'assurance maladie, l'assurance vieillesse, les prestations familiales et l'assurance accidents du travail."
  "|Le revenu de solidarité active est une prestation sociale destinée aux personnes sans ressources suffisantes."
  "|L'allocation aux adultes handicapés est versée aux personnes handicapées qui remplissent des conditions d'incapacité et de ressources."
  "|L'allocation de solidarité aux personnes âgées garantit un revenu minimum aux personnes âgées disposant de faibles ressources."
  "|La complémentaire santé solidaire permet à des personnes aux revenus modestes d'accéder à une couverture complémentaire."
  "|Les aides au logement sont versées par la caisse d'allocations familiales sous conditions de ressources."
  "|La maison départementale des personnes handicapées instruit les demandes liées au handicap et à la prestation de compensation."
  "|Chaque prestation possède ses propres conditions : âge, ressources, situation familiale, incapacité ou résidence."
  "|Le professionnel facilite l'accès aux droits sans se substituer à la personne ni garantir une décision favorable."
  "|Le référentiel BTS SP3S attend la connaissance des politiques sanitaires et sociales et des dispositifs aux différents échelons."),
[QC("Quelle caisse verse les prestations familiales et les aides au logement ?", "La CPAM~La CAF~La CARSAT~La MSA", 1,
    "La caisse d'allocations familiales gère les prestations familiales et les aides au logement."),
 QC("Quel organisme instruit les demandes liées au handicap ?", "La MDPH~La CPAM~Le conseil départemental seul~La CAF exclusivement", 0,
    "La maison départementale des personnes handicapées est le guichet unique des demandes liées au handicap."),
 QC("Quelle prestation garantit un revenu aux personnes âgées ayant peu de ressources ?", "Le RSA~L'AAH~L'ASPA~Les APL", 2,
    "L'ASPA est l'allocation de solidarité aux personnes âgées."),
 QC("Quelles conditions sont courantes pour l'attribution d'une prestation ?", "Le seul âge~Ressources, situation et résidence~La couleur du dossier~L'avis du voisin", 1,
    "Les conditions varient mais portent notamment sur ressources, situation et résidence."),
 QC("Quel rôle revient au professionnel d'accueil ?", "Garantir l'octroi de la prestation~Faciliter l'accès aux droits sans promettre la décision~Décider à la place de la caisse~Refuser les dossiers incomplets sans explication", 1,
    "Il informe et oriente, sans se substituer à l'organisme décisionnel."),
 QC("Que permet la complémentaire santé solidaire ?", "Une dispense de soins~Une couverture complémentaire à faible coût~Un revenu de remplacement~Un logement automatique", 1,
    "Elle aide les personnes aux revenus modestes à accéder à une complémentaire santé."),
 QC("Quel ensemble appartient à la sécurité sociale ?", "RSA, AAH et APL~Assurance maladie, vieillesse, prestations familiales et accidents du travail~Seuls les impôts~Les seules aides municipales", 1,
    "La sécurité sociale comprend ces quatre branches traditionnelles."),
 QT("Expliquer la différence entre un droit social et une prestation et donner un exemple de chacun dans le domaine du handicap.",
    "Un droit social est une faculté juridiquement reconnue à la personne, par exemple le droit à l'égalité de traitement et à l'accessibilité, ou le droit à une compensation du handicap. Une prestation est l'application concrète de ce droit : elle correspond à un versement ou à une aide accordée après instruction d'une demande, comme la prestation de compensation du handicap ou l'allocation aux adultes handicapés. Le droit existe même lorsqu'aucune demande n'a été faite ; la prestation nécessite un dossier, des conditions et une décision de l'organisme compétent. Le professionnel doit donc expliquer le droit, accompagner la demande et préparer les pièces, sans laisser croire que le versement est automatique.",
    "On sépare le principe juridique de sa traduction financière ou matérielle et on donne un exemple pour chacun."),
 QT("Un usager estime qu'il a « droit au RSA » alors qu'il travaille à temps partiel. Comment conduire l'entretien ?",
    "On accueille l'affirmation sans la contredire brutalement et on demande ce qu'il entend par ce droit : a-t-il déjà fait une demande, a-t-il reçu une réponse, quelles sont ses ressources et sa situation familiale ? On explique ensuite que le revenu de solidarité active est soumis à des conditions de ressources et d'activité, et que le travail à temps partiel peut être pris en compte selon les règles applicables, sans donner une décision qui ne relève pas du service. On l'oriente vers la caisse compétente avec une liste précise des pièces et un accompagnement pour constituer le dossier. On vérifie également d'autres droits possibles, comme une aide au logement ou une complémentaire santé solidaire, car une demande refusée peut être remplacée par une autre aide. On trace l'entretien et le conseil donné.",
    "On clarifie la demande, on informe sans promettre, on oriente avec des pièces précises et on vérifie les autres droits.")],
C("Accéder aux droits suppose de connaître les dispositifs, leurs conditions et le bon interlocuteur.",
  "Droit reconnu + conditions vérifiées + dossier instruit = prestation",
  "CAF · CPAM · MDPH · RSA · AAH · ASPA · Complémentaire santé solidaire",
  "Sécurité sociale~Branches et prestations~CAF~Famille et logement~MDPH~Guichet handicap~Prestation~Droit appliqué",
  "Écouter la demande et les ressources|Identifier le dispositif compétent|Expliquer les conditions sans promettre|Préparer les pièces et orienter|Tracer le conseil donné",
  "Promettre une prestation|Se tromper d'organisme|Refuser un dossier sans explication|Oublier les autres droits possibles",
  "Usager~Demande de RSA~Condition~Ressources et activité~Orientation~CAF et pièces~Alternative~APL ou CSS",
  "Droit social~Principe reconnu~Prestation~Aide accordée après instruction",
  "Sécurité sociale~Assurance maladie et vieillesse~Aide sociale~Prestations complémentaires"))

# ============================================================ EC1
add("EC1", "Économie de la santé et du social : acteurs et financement", "Économie", ["BTS1"],
S("L'économie de la santé et du social étudie la production, le financement et la consommation de prestations de santé et d'accompagnement."
  "|Les acteurs sont nombreux : établissements publics, associations, cliniques privées, professionnels libéraux et collectivités."
  "|L'État définit les politiques nationales et finance une partie des dispositifs par le budget de la santé."
  "|L'agence régionale de santé répartit les moyens sur le territoire et autorise les établissements."
  "|Les départements financent l'aide sociale, l'action sociale et une part des dispositifs médico-sociaux."
  "|L'assurance maladie rembourse les soins et finance des établissements selon des modalités propres."
  "|Les usagers participent par des tickets modérateurs, des franchises ou des forfaits selon leur situation."
  "|Les mutuelles et assurances complémentaires prennent en charge une partie des restes à charge."
  "|Le financement des établissements sociaux repose notamment sur des dotations globales ou des prix de journée."
  "|La dépense de santé augmente avec le vieillissement, l'innovation et l'extension des attentes de la population."
  "|La question de l'allocation efficace des ressources est centrale : on cherche à améliorer le service à coût maîtrisé."
  "|Le référentiel BTS SP3S attend la connaissance de l'organisation et du financement des prestations proposées."),
[QC("Quel acteur répartit les moyens de santé sur le territoire ?", "La CAF~L'agence régionale de santé~La chambre régionale des comptes~Le tribunal administratif", 1,
    "L'ARS adapte l'offre de santé aux besoins régionaux et finance des actions."),
 QC("Quel niveau collectivité finance l'aide sociale et l'action sociale ?", "La commune seule~Le département~L'Europe uniquement~La CPAM seule", 1,
    "Le département est un acteur majeur de l'action sociale et médico-sociale."),
 QC("Quel mode de financement concerne fréquemment les établissements médico-sociaux ?", "Le seul prix de vente libre~La dotation globale ou le prix de journée~Le ticket modérateur seul~La redevance unique", 1,
    "Dotation globale et prix de journée sont des modes de financement du médico-social."),
 QC("Qu'est-ce qu'un reste à charge ?", "La part remboursée par l'assurance maladie~La part non couverte restant à la charge de l'usager~Le budget de l'établissement~La dotation de l'État", 1,
    "Le reste à charge est la somme que l'usager doit supporter après remboursement."),
 QC("Quel facteur contribue à la croissance des dépenses de santé ?", "Le vieillissement de la population~La baisse du nombre de malades~La suppression des innovations~La réduction des attentes", 0,
    "Vieillissement et innovation sont des facteurs de croissance des dépenses."),
 QC("Quel rôle joue une complémentaire santé ?", "Remplacer l'assurance maladie~Prendre en charge une partie du reste à charge~Supprimer les tickets modérateurs~Financer les hôpitaux", 1,
    "Elle complète les remboursements de l'assurance maladie obligatoire."),
 QC("Quel objectif exprime l'allocation efficiente des ressources ?", "Dépenser le maximum~Améliorer le service à coût maîtrisé~Réduire tous les soins~Supprimer les contrôles", 1,
    "On recherche le meilleur résultat pour un coût donné."),
 QT("Expliquer pourquoi le financement du secteur sanitaire et social fait intervenir plusieurs niveaux de collectivités et d'organismes.",
    "Parce que les prestations répondent à des besoins de natures différentes et relèvent de compétences réparties. L'État définit les orientations nationales, les lois et une partie du financement de la santé. L'agence régionale de santé adapte l'offre aux besoins du territoire et contrôle les établissements. Le département finance l'action sociale, l'aide sociale et accompagne les personnes âgées ou handicapées. L'assurance maladie rembourse les soins et finance des structures selon des règles qui lui sont propres. Les mutuelles couvrent une part du reste à charge et les usagers supportent une partie des frais. Cette multiplicité permet de mutualiser les risques mais rend la lecture du financement complexe : un même usager peut être concerné par plusieurs financeurs et plusieurs guichets, ce qui justifie le rôle d'orientation du technicien supérieur.",
    "On répartit les rôles entre État, ARS, département, assurance maladie, complémentaires et usagers, et on explique la conséquence pour l'accompagnement."),
 QT("Un établissement médico-social voit ses recettes stagner alors que les besoins augmentent. Quelles pistes d'analyse économique proposer ?",
    "On analyse d'abord les recettes : dotation globale, prix de journée, participations des usagers et financements complémentaires, en vérifiant si des conventions ont évolué. On examine ensuite les dépenses : personnel, locaux, fournitures, énergie et prestations externes, en identifiant ce qui augmente le plus. On compare l'activité réelle à l'activité financée : nombre de places occupées, durée des accompagnements et besoins non couverts. On étudie ensuite les possibilités d'optimisation sans dégrader la qualité : mutualisation des achats avec d'autres services, réorganisation des plannings, recherche de financements complémentaires et renforcement des partenariats avec le département ou l'ARS. Enfin, on présente ces éléments à la direction avec des indicateurs chiffrés et une proposition hiérarchisée, en gardant la qualité de l'accompagnement comme critère de décision.",
    "On attend analyse des recettes et dépenses, comparaison activité et financement, pistes d'optimisation et restitution chiffrée.")],
C("Le financement du sanitaire et du social est pluriel : chaque acteur finance une part du parcours de la personne.",
  "Besoins + offres + financeurs + coûts = système économique",
  "État · ARS · département · assurance maladie · complémentaires · usagers",
  "État~Orientations nationales~ARS~Répartition territoriale~Département~Aide sociale~Assurance maladie~Remboursements",
  "Repérer les financeurs concernés|Analyser recettes et dépenses|Comparer activité réelle et financée|Chercher des optimisations sans réduire la qualité|Restituer avec des indicateurs",
  "Confondre financeur et prestataire|Réduire la qualité pour économiser|Ignorer les coûts cachés|Ne pas chiffrer les propositions",
  "Établissement~Recettes stagnantes~Besoin~Accompagnement accru~Piste~Mutualisation des achats~Critère~Qualité du service",
  "Dotation globale~Financement forfaitaire~Prix de journée~Financement à l'acte",
  "Reste à charge~Part de l'usager~Remboursement~Part de l'assurance"))

# ============================================================ EC2
add("EC2", "Sécurité sociale et couverture maladie", "Économie", ["BTS1"],
S("La sécurité sociale est un système de protection sociale qui couvre les risques de la vie contre des cotisations et des impôts."
  "|Elle repose sur le principe de la mutualisation : les cotisations de tous financent les prestations de chacun."
  "|L'assurance maladie prend en charge les soins, avec des taux de remboursement variables selon les actes."
  "|Le ticket modérateur est la part des dépenses laissée à la charge de l'assuré après remboursement."
  "|Les franchises médicales et la participation forfaitaire sont des sommes déduites des remboursements."
  "|La carte Vitale facilite la transmission des informations entre professionnels de santé et organismes d'assurance maladie."
  "|Le tiers payant dispense l'usager d'avancer la part remboursable dans certains cas."
  "|L'assurance vieillesse verse les pensions de retraite ; les prestations familiales sont gérées par les caisses d'allocations familiales."
  "|Les accidents du travail et les maladies professionnelles relèvent d'une branche spécifique."
  "|Les régimes de base sont complétés par des régimes complémentaires et des mutuelles."
  "|La complémentaire santé solidaire aide les personnes aux ressources modestes à accéder à des soins."
  "|Le technicien supérieur accompagne l'usager dans la compréhension de ses droits sans se substituer aux organismes."),
[QC("Quel principe fonde la sécurité sociale ?", "La capitalisation individuelle~La mutualisation des risques~Le financement uniquement par l'usager~L'absence de cotisations", 1,
    "Les cotisations de tous financent les prestations de chacun."),
 QC("Qu'appelle-t-on ticket modérateur ?", "La somme remboursée~La part restant à la charge de l'assuré~Le salaire du médecin~La cotisation employeur", 1,
    "Le ticket modérateur est la part non remboursée de la dépense."),
 QC("Quel document facilite les échanges avec l'assurance maladie ?", "La carte Vitale~Le livret de famille~Le contrat de séjour~Le bulletin de salaire", 0,
    "La carte Vitale contient les droits et permet la télétransmission."),
 QC("Quel système dispense l'usager d'avancer la part remboursable ?", "Le ticket modérateur~Le tiers payant~La franchise~La participation forfaitaire", 1,
    "Le tiers payant évite l'avance de la part prise en charge."),
 QC("Quelle branche couvre les accidents du travail ?", "L'assurance vieillesse~Les prestations familiales~La branche accidents du travail et maladies professionnelles~La mutualité seule", 2,
    "Les AT/MP constituent une branche spécifique de la sécurité sociale."),
 QC("Quel organisme gère les prestations familiales ?", "La CPAM~La CAF~L'ARS~La CNIL", 1,
    "Les caisses d'allocations familiales versent les prestations familiales."),
 QC("Quel dispositif aide les personnes aux faibles ressources à accéder à une complémentaire ?", "La carte Vitale seule~La complémentaire santé solidaire~Le ticket modérateur~La pension de retraite", 1,
    "La complémentaire santé solidaire est un dispositif d'accès à la complémentaire."),
 QT("Expliquer le mécanisme du tiers payant et ses effets pour l'usager et pour le professionnel.",
    "Le tiers payant est un mécanisme de dispense d'avance de frais : le professionnel de santé ou l'établissement est payé directement par l'organisme d'assurance maladie pour la part remboursable, et l'usager ne règle que la part restant à sa charge, le cas échéant complétée par sa mutuelle. Pour l'usager, cela réduit le risque de renoncer à des soins faute de trésorerie et simplifie les démarches. Pour le professionnel, cela impose de vérifier les droits, d'utiliser la carte Vitale et de télétransmettre les actes, ce qui augmente la charge administrative mais sécurise le recouvrement. Le tiers payant ne supprime ni le ticket modérateur ni les franchises : il change seulement le mode de règlement.",
    "On explique le mécanisme, ses bénéfices pour l'usager et les obligations administratives du professionnel."),
 QT("Un usager ne comprend pas pourquoi une consultation ne lui a été remboursée qu'en partie.Comment lui expliquer ?",
    "On commence par écouter ce qu'il a compris et par vérifier le décompte de remboursement. On explique ensuite les composantes du montant : la base de remboursement de l'acte, le taux applicable, le ticket modérateur qui reste à sa charge, et les éventuelles franchises ou participations forfaitaires déduites. On distingue clairement ce que l'assurance maladie obligatoire prend en charge et ce qui peut relever de sa complémentaire santé. On vérifie avec lui si une mutuelle est déclarée sur sa carte Vitale et, si ce n'est pas le cas, on l'oriente pour la faire enregistrer. On évite de garantir un montant futur : les règles dépendent de l'acte et de la situation de chacun. On remet un document écrit et on propose, si besoin, un rendez-vous avec un conseiller de l'organisme.",
    "On décompose le remboursement, on distingue obligatoire et complémentaire et on oriente sans promettre.")],
C("La sécurité sociale mutualise les risques ; le reste à charge dépend des règles de remboursement et de la complémentaire.",
  "Cotisations + impôts → prestations · remboursement = base × taux − franchises",
  "Ticket modérateur · tiers payant · carte Vitale · complémentaire santé solidaire",
  "Mutualisation~Solidarité entre assurés~Ticket modérateur~Part à charge~Tiers payant~Pas d'avance de frais~Carte Vitale~Droits et télétransmission",
  "Vérifier les droits de l'usager|Expliquer la base et le taux|Identifier ticket modérateur et franchises|Vérifier la complémentaire|Orienter sans promettre un montant",
  "Garantir un remboursement précis|Confondre ticket modérateur et franchise|Oublier de vérifier la mutuelle|Remplacer l'organisme de décision",
  "Consultation~Décompte incompris~Explication~Base, taux et franchise~Solution~Enregistrer la mutuelle~Document~Note écrite",
  "Ticket modérateur~Reste à charge~Tiers payant~Mode de règlement",
  "Assurance maladie~Régime obligatoire~Mutuelle~Complément volontaire"))

# ============================================================ EC3
add("EC3", "Tarification et budget d'un établissement médico-social", "Économie", ["BTS2"],
S("La tarification est le mode de calcul des recettes d'un établissement social ou médico-social pour une période donnée."
  "|Le prix de journée correspond à un montant par jour de présence de l'usager, complété selon les prestations."
  "|La dotation globale de financement attribue une enveloppe annuelle à l'établissement pour assurer ses missions."
  "|Les forfaits et les dotations peuvent être modulés selon l'activité réelle et les besoins des publics accompagnés."
  "|Le budget prévisionnel présente les recettes et les dépenses attendues de l'exercice à venir."
  "|Les recettes comprennent les dotations, les participations des usagers et des ressources complémentaires."
  "|Les dépenses se répartissent notamment entre personnel, charges immobilières, fournitures, alimentation et prestations externes."
  "|Le personnel représente généralement la part la plus importante des dépenses de fonctionnement."
  "|Le suivi budgétaire compare périodiquement les réalisations aux prévisions et identifie les écarts."
  "|Un écart peut venir d'une sous-activité, d'une hausse des prix ou d'une dépense non prévue."
  "|La qualité de l'accompagnement est un critère de décision : une économie qui dégrade le service n'est pas une solution."
  "|Ces notions relèvent de l'appui à la logistique financière du bloc 4 du référentiel BTS SP3S."),
[QC("Qu'appelle-t-on prix de journée ?", "Le prix d'un repas~Un montant par jour de présence et de prestation~La pension de l'agent~Le loyer du bâtiment", 1,
    "Le prix de journée est calculé à partir du nombre de journées réalisées."),
 QC("Quel mode de financement attribue une enveloppe annuelle globale ?", "Le prix de journée~La dotation globale de financement~Le ticket modérateur~La franchise", 1,
    "La dotation globale fixe une enveloppe annuelle pour les missions de l'établissement."),
 QC("Quel document présente les recettes et dépenses prévues de l'exercice ?", "Le budget prévisionnel~Le livret d'accueil~Le contrat de séjour~Le plan de formation", 0,
    "Le budget prévisionnel est le document de prévision financière de l'exercice."),
 QC("Quel poste représente généralement la plus grande part des dépenses ?", "Les fournitures~Le personnel~L'électricité~L'assurance", 1,
    "Les charges de personnel sont le principal poste de dépense des établissements."),
 QC("Quel objet a le suivi budgétaire ?", "Comparer réalisations et prévisions pour repérer les écarts~Remplacer le contrôle de l'ARS~Supprimer les dépenses de personnel~Éviter toute réunion de service", 0,
    "Le suivi budgétaire mesure les écarts entre prévu et réalisé."),
 QC("Quelle cause peut expliquer un écart défavorable ?", "Une sous-activité ou une hausse des prix~Une augmentation des recettes~Une baisse des charges~Une prévision trop prudente", 0,
    "Sous-activité, hausse de prix et dépenses non prévues créent des écarts défavorables."),
 QC("Quel critère doit limiter une mesure d'économie ?", "La rapidité~La qualité de l'accompagnement~L'avis d'un seul service~La taille du bâtiment", 1,
    "On ne doit pas réduire la qualité du service pour économiser."),
 QT("Distinguer prix de journée et dotation globale et expliquer les effets de chacun sur la gestion d'un établissement.",
    "Le prix de journée est un financement à l'activité : l'établissement perçoit un montant par journée d'accueil et par prestation réalisée. Il incite à remplir les places et à tracer précisément l'activité, mais il crée une incitation à augmenter le nombre de journées et rend les recettes sensibles aux absences. La dotation globale de financement verse une enveloppe annuelle pour des missions définies : elle donne une visibilité pluriannuelle et laisse plus de liberté dans la répartition des moyens, mais elle exige une bonne prévision et un suivi rigoureux pour ne pas dépasser l'enveloppe. Dans les deux cas, l'établissement doit produire des données d'activité fiables et rendre des comptes à l'autorité de contrôle, tout en préservant la qualité de l'accompagnement.",
    "On compare les deux modes, leurs incitations et leurs contraintes de gestion."),
 QT("Le budget d'un service présente un écart défavorable de 8 % sur les charges de personnel. Comment analyser et proposer ?",
    "On vérifie d'abord la nature de l'écart : heures supplémentaires non prévues, remplacements prolongés, revalorisation salariale ou erreur de prévision. On confronte ensuite les données d'activité : pic d'accueil, absence de personnels, durée des accompagnements et taux d'occupation. On distingue ce qui est ponctuel de ce qui est structurel, car un remplacement temporaire ne se traite pas comme une augmentation durable de l'effectif. On propose ensuite des mesures sans dégrader le service : meilleure anticipation des plannings, mutualisation des interventions entre services, formation polyvalente et recherche de financements complémentaires. On chiffre chaque piste et on présente à la direction un tableau comparatif avec les effets attendus sur la qualité et les délais. Enfin, on inscrit les mesures retenues dans le budget révisé et on suit l'écart le mois suivant.",
    "On attend une analyse des causes, une distinction ponctuel et structurel, des mesures chiffrées et un suivi.")],
C("La tarification détermine les recettes ; le budget prévisionnel et le suivi des écarts permettent de piloter la structure.",
  "Recettes prévues − dépenses prévues = résultat attendu",
  "Prix de journée · dotation globale · charges de personnel · écart = réalisé − prévu",
  "Tarification~Mode de calcul des recettes~Dotation~Enveloppe annuelle~Budget~Prévisions de l'exercice~Écart~Réalisé moins prévu",
  "Choisir le mode de tarification|Prévoir recettes et dépenses|Suivre les réalisations mensuellement|Analyser les écarts et leurs causes|Proposer des mesures sans nuire à la qualité",
  "Remplir les places pour augmenter les recettes sans égard au besoin|Réduire les effectifs coûte que coûte|Ignorer les écarts jusqu'à la fin d'exercice|Ne pas chiffrer les pistes",
  "Écart~8 % sur le personnel~Cause~Remplacements prolongés~Mesure~Planning anticipé~Critère~Qualité maintenue",
  "Prix de journée~Financement à l'activité~Dotation globale~Enveloppe annuelle",
  "Prévu~Budget initial~Réalisé~Chiffres constatés"))

# ============================================================ EC4
add("EC4", "Achats et marchés publics dans le secteur sanitaire et social", "Économie", ["BTS2"],
S("Les achats d'un établissement portent sur des fournitures, des prestations, des équipements et des travaux."
  "|Les marchés publics sont les contrats par lesquels des organismes publics ou assimilés achètent des biens ou des services."
  "|Ils sont soumis à des règles de publicité, de mise en concurrence et de transparence."
  "|L'objectif est d'obtenir le meilleur rapport qualité-prix tout en garantissant l'égalité de traitement entre candidats."
  "|Les seuils financiers déterminent la procédure applicable : marché adapté, procédure adaptée ou appel d'offres."
  "|Le cahier des charges décrit précisément le besoin, les critères de sélection et les conditions d'exécution."
  "|Les critères d'attribution peuvent inclure le prix, la qualité technique, les délais et la valeur environnementale."
  "|L'achat durable intègre la durée de vie, la réparabilité et l'impact environnemental des produits."
  "|Le service achat vérifie le besoin exprimé avant de lancer la consultation pour éviter les gaspillages."
  "|La réception des fournitures donne lieu à un contrôle de conformité et à une trace écrite."
  "|La facture est contrôlée par rapport à la commande avant son paiement."
  "|Ces compétences relèvent de l'appui à la logistique financière et de la maîtrise des coûts dans le bloc 4."),
[QC("Quel principe s'impose dans un marché public ?", "Le choix du fournisseur habituel sans consultation~La publicité et la mise en concurrence~L'absence de cahier des charges~Le paiement avant livraison", 1,
    "Publicité, mise en concurrence et transparence sont des principes fondamentaux."),
 QC("Quel document décrit précisément le besoin et les critères ?", "Le cahier des charges~Le bulletin de paie~Le livret d'accueil~Le registre des réclamations", 0,
    "Le cahier des charges cadre la consultation et l'exécution du marché."),
 QC("Quel critère peut être retenu pour attribuer un marché ?", "La seule couleur du logo~Le prix et la qualité technique~Le hasard~L'ancienneté du fournisseur seule", 1,
    "Les critères sont objectifs et annoncés à l'avance, prix et qualité notamment."),
 QC("Quel seuil détermine la procédure applicable ?", "La surface du bâtiment~Le montant estimé du marché~Le nombre d'agents~La date de l'achat", 1,
    "Les seuils financiers déclenchent des procédures différentes."),
 QC("Que vérifie la réception d'une commande ?", "Le seul prix~La conformité aux specifications du cahier des charges~L'avis d'un collègue~La publicité faite", 1,
    "On contrôle la conformité aux spécifications, à la qualité et aux quantités, puis on trace."),
 QC("Quand la facture doit-elle être contrôlée ?", "Avant le paiement~Après le paiement systématiquement~Jamais~Uniquement en fin d'année", 0,
    "Le contrôle avant paiement évite de régler une facture non conforme."),
 QC("Quel achat est durable ?", "Le moins cher immédiatement~Un équipement réparable et de longue durée~Un produit jetable~Le plus grand stock possible", 1,
    "L'achat durable considère durée de vie, réparabilité et impact environnemental."),
 QT("Expliquer l'intérêt de la mise en concurrence et les limites du seul critère du prix le plus bas.",
    "La mise en concurrence permet à des fournisseurs différents de proposer leurs offres sur la base d'un même cahier des charges. Elle favorise l'égalité de traitement, la transparence et l'obtention d'un meilleur rapport qualité-prix pour la collectivité. Elle réduit aussi le risque de dépendance à un seul prestataire. Mais retenir uniquement le prix le plus bas peut conduire à des fournitures de mauvaise qualité, des délais non respectés, une maintenance absente ou des conditions de travail dégradées chez le fournisseur. C'est pourquoi le cahier des charges peut prévoir des critères de qualité technique, de délai de livraison, de service après-vente et d'impact environnemental, pondérés à l'avance. Le choix final doit être motivé et vérifiable.",
    "On cite les bénéfices de la concurrence puis les risques du prix seul, avec des critères de substitution."),
 QT("Un service souhaite acheter de nouveaux fauteuils pour l'accueil. Décrire la démarche d'achat conforme et responsable.",
    "On commence par préciser le besoin : nombre de fauteuils, usagers concernés, contraintes d'espace, normes de sécurité et critères de confort et d'accessibilité. On vérifie le budget disponible et on compare avec le parc existant pour éviter un achat inutile. On rédige un cahier des charges avec les caractéristiques techniques, les quantités, les délais, les garanties et des critères d'attribution incluant durabilité et réparabilité. Selon le montant estimé, on lance une consultation adaptée ou un appel d'offres, en respectant les règles de publicité. On analyse les offres avec une grille de notation établie à l'avance. À la réception, on contrôle la conformité et on trace la mise en service. La facture est vérifiée par rapport à la commande avant paiement, et les anciens fauteuils suivent une filière de reprise ou de don si possible.",
    "On attend besoin, budget, cahier des charges, consultation, notation objective, réception et contrôle de facture.")],
C("Un achat public est encadré : il part d'un besoin réel, se déroule en concurrence et se termine par une réception contrôlée.",
  "Besoin + cahier des charges + concurrence + attribution + réception",
  "Égalité de traitement · transparence · prix et qualité · achat durable",
  "Besoin~Prestation attendue~Cahier des charges~Critères et conditions~Concurrence~Offres comparées~Réception~Conformité vérifiée",
  "Vérifier le besoin et le budget|Rédiger le cahier des charges|Respecter la procédure selon le seuil|Noter les offres avec une grille|Contrôler la réception et la facture",
  "Choisir à l'avance son fournisseur|Ne retenir que le prix|Oublier le contrôle à la réception|Payer avant vérification",
  "Fauteuils~Renouvellement du parc~Critère~Accessibilité et durabilité~Consultation~Offres comparées~Réception~Conforme",
  "Prix~Critère financier~Qualité~Critère technique",
  "Marché public~Règles de concurrence~Achat direct~Usage strictement encadré"))

# ============================================================ EC5
add("EC5", "Coût, productivité et analyse de la valeur", "Économie", ["BTS2"],
S("Le coût d'une prestation est la somme des consommations de ressources nécessaires pour la produire."
  "|On distingue les coûts directs, imputables à une prestation, et les coûts indirects, partagés entre plusieurs activités."
  "|Les coûts fixes ne varient pas avec l'activité, comme le loyer ; les coûts variables suivent l'activité, comme les fournitures."
  "|Le coût complet ajoute aux coûts directs une part des frais généraux de la structure."
  "|La productivité mesure le rapport entre les résultats obtenus et les moyens consommés."
  "|Dans un service d'accueil, on peut suivre le nombre de dossiers traités par agent et par jour, sans sacrifier la qualité."
  "|L'analyse de la valeur cherche à assurer une fonction requise au coût le plus faible possible, sans réduire la qualité utile."
  "|La démarche compare ce que le service apporte à l'usager (valeur fonctionnelle) et ce qu'il coûte (valeur économique)."
  "|Une fonction inutile ou redondante peut être supprimée : c'est une source d'économie sans perte de service."
  "|Le coût de la non-qualité regroupe les reprises, les erreurs de transmission, les réclamations et les délais supplémentaires."
  "|Réduire la non-qualité est souvent plus efficace que réduire les moyens à la source."
  "|Ces outils soutiennent la participation à la démarche qualité et à l'amélioration du service rendu."),
[QC("Quel coût ne varie pas avec l'activité ?", "Le coût variable~Le coût fixe~Le coût direct~Le coût d'achat", 1,
    "Le loyer ou l'assurance sont des coûts fixes, indépendants du niveau d'activité."),
 QC("Quel coût est partagé entre plusieurs activités ?", "Le coût direct~Le coût indirect~Le coût variable~Le coût de fourniture", 1,
    "Les frais généraux sont des coûts indirects répartis entre les activités."),
 QC("Que mesure la productivité ?", "Le rapport entre résultats et moyens consommés~Le nombre de réunions~Le prix de vente seul~La durée du contrat", 0,
    "La productivité est un rapport entre output et input."),
 QC("Quel indicateur peut suivre un service d'accueil ?", "Le nombre de dossiers traités par agent et par jour~La couleur des chemises~La taille du hall~Le nombre de fauteuils", 0,
    "On mesure l'activité par des indicateurs simples, tout en contrôlant la qualité."),
 QC("Quel est l'objet de l'analyse de la valeur ?", "Réduire tous les coûts sans distinguer la qualité~Assurer la fonction requise au moindre coût~Supprimer les usagers les plus coûteux~Augmenter les prix", 1,
    "L'analyse de la valeur concilie fonction et coût, sans dégrader l'utile."),
 QC("Qu'appelle-t-on coût de la non-qualité ?", "Le coût des fournitures~Les reprises, erreurs et réclamations~Le loyer~Les salaires", 1,
    "Les gaspillages liés aux erreurs et reprises coûtent cher et sont évitables."),
 QC("Quelle piste est préférable à une réduction brute des moyens ?", "Réduire la non-qualité~Supprimer les formations~Fermer l'accueil~Reporter les démarches", 0,
    "Agir sur les erreurs et reprises améliore le service et diminue les coûts."),
 QT("Expliquer pourquoi une hausse de productivité peut dégrader la qualité du service si elle est mal pilotée.",
    "Une hausse de productivité signifie que l'on traite plus d'activité avec les mêmes moyens. Si l'on obtient ce résultat en réduisant le temps consacré à chaque usager, en supprimant les vérifications ou en pressionnant les agents, le nombre de dossiers traités augmente mais les erreurs, les réclamations et les reprises augmentent aussi. Le service paraît plus efficace à court terme alors que le coût de la non-qualité progresse et que la confiance des usagers diminue. Un pilotage sain associe toujours un indicateur de volume et un indicateur de qualité : délai de réponse, taux de dossiers complets, satisfaction ou nombre de réclamations. La productivité n'est utile que si elle améliore la valeur rendue à la personne.",
    "On montre le risque d'un indicateur unique et la nécessité de coupler volume et qualité."),
 QT("Appliquer l'analyse de la valeur à la tenue du registre des réclamations.",
    "On identifie d'abord la fonction à assurer : enregistrer chaque réclamation avec les éléments utiles, permettre son suivi et alimenter l'amélioration du service. On recense ensuite les moyens mobilisés : support papier ou numérique, temps de saisie, double lecture, relance et classement. On compare la valeur fonctionnelle apportée à l'usager, qui est de voir sa demande traitée, et la valeur économique consacrée à la tenue du registre. Si l'on constate une double saisie dans deux outils différents, on supprime cette fonction redondante sans rien perdre pour l'usager. Si une relance systématique est faite alors que le circuit est déjà informatisé, on la remplace par une alerte automatique. On conserve en revanche la vérification de la qualité de l'information, car elle évite les erreurs coûteuses. La solution retenue est validée par les agents concernés et un indicateur de suivi est mis en place.",
    "On attend fonction, moyens, comparaison valeur et suppression d'une fonction redondante sans perte pour l'usager.")],
C("Piloter les coûts, ce n'est pas couper : c'est supprimer ce qui ne sert pas et préserver la valeur pour l'usager.",
  "Valeur = fonction rendue / coût consommé",
  "Coûts fixes et variables · productivité · non-qualité · analyse de la valeur",
  "Coût direct~Imputable à la prestation~Coût indirect~Partagé entre activités~Productivité~Résultats sur moyens~Valeur~Fonction et coût",
  "Identifier la fonction à assurer|Recenser les moyens mobilisés|Comparer valeur utile et coût|Supprimer les redondances|Vérifier la qualité après changement",
  "Réduire les moyens sans regarder la qualité|Se fier à un seul indicateur de volume|Ignorer le coût des erreurs|Supprimer la vérification utile",
  "Registre~Tenue quotidienne~Redondance~Double saisie~Amélioration~Alerte automatique~Indicateur~Réclamations traitées",
  "Coût fixe~Indépendant de l'activité~Coût variable~Suite à l'activité",
  "Qualité~Valeur pour l'usager~Non-qualité~Reprises et erreurs"))

# ============================================================ EC6
add("EC6", "Numérique et transformation des services sanitaires et sociaux", "Économie", ["BTS2"],
S("La transformation numérique modifie les outils, les circuits et les relations de travail dans les établissements sanitaires et sociaux."
  "|Elle ne se limite pas à remplacer le papier par un écran : elle change l'organisation des informations et des décisions."
  "|Les dossiers usagers informatisés facilitent le partage entre professionnels habilités, sous réserve du secret et du RGPD."
  "|La télétransmission avec les organismes sociaux réduit les délais et les doubles saisies."
  "|Les outils de planification et de messagerie coordonnent les équipes et les rendez-vous."
  "|La dématérialisation des démarches peut améliorer l'accessibilité, mais elle exclut les personnes sans équipement ou sans compétence."
  "|Le référentiel BTS SP3S mentionne l'accompagnement à la digitalisation et l'enjeu des nouvelles technologies."
  "|La sécurité des accès repose sur des identifiants personnels, des droits adaptés aux rôles et une journalisation."
  "|La formation des agents est un facteur clé : un outil non approprié génère des erreurs et un surcroît de travail."
  "|Le coût de la transformation comprend le matériel, les licences, la maintenance, la formation et l'accompagnement au changement."
  "|Les gains attendus sont le temps gagné, la fiabilité des données et la qualité du suivi des parcours."
  "|Une évaluation après déploiement permet de vérifier ces gains et de corriger les usages inadaptés."),
[QC("Que désigne la transformation numérique d'un service ?", "Le seul achat d'ordinateurs~Une modification des outils, circuits et relations de travail~La suppression des usagers~Le déménagement du service", 1,
    "La transformation dépasse l'outil : elle concerne l'organisation et les pratiques."),
 QC("Quel risque social de la dématérialisation faut-il anticiper ?", "Une exclusion des personnes sans équipement ou sans compétence~Une réduction du nombre d'écrans~Une baisse du prix du papier~Une augmentation des réunions", 0,
    "L'accessibilité numérique est un enjeu majeur pour les publics accompagnés."),
 QC("Quel principe d'accès s'impose à un dossier informatisé ?", "Un mot de passe partagé~Des droits adaptés aux rôles et des identifiants personnels~Un accès ouvert à tous~Une absence de journalisation", 1,
    "Identifiants personnels, droits par rôle et traces d'accès protègent les données."),
 QC("Quel coût est souvent oublié dans un projet numérique ?", "Le matériel~La formation et l'accompagnement au changement~La licence~Le câble réseau", 1,
    "La formation et l'accompagnement conditionnent l'appropriation de l'outil."),
 QC("Quel gain est attendu de la télétransmission ?", "Une double saisie systématique~Une réduction des délais et des ressaisies~Une augmentation du papier~Une perte des données", 1,
    "La télétransmission fluidifie les échanges avec les organismes."),
 QC("Quel rôle a l'évaluation après déploiement ?", "Supprimer la formation~Vérifier les gains et corriger les usages~Remplacer le RGPD~Interdire les outils", 1,
    "On mesure les effets réels et on ajuste les pratiques."),
 QC("Quel est un effet d'un outil non approprié par les agents ?", "Un gain de temps immédiat~Des erreurs et un surcroît de travail~Une autonomie totale~Une baisse des réclamations", 1,
    "Sans appropriation, l'outil ajoute de la charge au lieu de la réduire."),
 QT("Expliquer pourquoi un projet numérique dans un établissement social doit associer usagers et professionnels.",
    "Un outil conçu sans les agents qui l'utilisent ne correspond pas aux situations réelles : il manque des informations nécessaires, propose des étapes inutiles et crée des contournements hors outil, ce qui détruit la fiabilité des données. Les usagers, de leur côté, sont les premiers concernés par l'accessibilité : un parcours dématérialisé peut être impossible pour une personne sans connexion, sans lecture aisée ou sans maîtrise de la langue. Associer les deux groupes dès la conception permet de choisir des fonctionnalités utiles, de prévoir des alternatives humaines et de tester l'outil dans des situations réelles d'accueil. Cela augmente l'appropriation, réduit la résistance au changement et améliore la qualité du service rendu.",
    "On justifie la participation des agents et des usagers par la fiabilité des données et l'accessibilité du service."),
 QT("Une structure passe au dossier informatisé. Décrire les précautions à prendre avant la mise en service.",
    "On vérifie d'abord la base légale et les finalités des traitements, puis on met à jour le registre des traitements et les mentions d'information destinées aux usagers. On paramètre des profils d'accès par rôle, avec des identifiants personnels, une authentification robuste et une journalisation des consultations. On contrôle la qualité des données migrées : doublons, champs vides, informations obsolètes, et on corrige avant bascule. On organise une formation pratique avec des cas réels d'accueil, on désigne une personne ressource et on prévoit une période de double fonctionnement. On prévoit une alternative humaine pour les usagers qui ne peuvent pas utiliser le numérique. Enfin, on planifie un retour d'expérience après un mois pour mesurer les délais, les erreurs et la satisfaction, puis on ajuste les paramètres.",
    "On attend conformité RGPD, profils d'accès, qualité des données, formation, alternatives et évaluation.")],
C("Le numérique n'est utile que s'il sert le parcours de la personne et reste accessible, sécurisé et approprié.",
  "Outil + organisation + compétences + sécurité = service amélioré",
  "Droits par rôle · journalisation · formation · alternatives humaines",
  "Dossier informatisé~Partage encadré~Profil d'accès~Droits par rôle~Formation~Appropriation~Alternative~Accompagnement humain",
  "Vérifier finalités et bases légales|Paramétrer les profils d'accès|Contrôler la qualité des données migrées|Former avec des cas réels|Évaluer après déploiement",
  "Partager un identifiant|Migrer des données non vérifiées|Supprimer l'accueil physique|Ne jamais évaluer l'outil",
  "Dossier~Bascule numérique~Risque~Perte d'accessibilité~Précaution~Accompagnement humain~Mesure~Satisfaction à un mois",
  "Dématérialisation~Supprime le papier~Inclusion numérique~Maintient l'accès à tous",
  "Gain~Temps et fiabilité~Coût caché~Formation et accompagnement"))

# ============================================================ SP1
add("SP1", "Santé publique : définitions, déterminants et politiques", "Santé publique et environnement professionnel", ["BTS1"],
S("La santé publique vise à améliorer la santé des populations par la prévention, l'organisation des soins et les politiques sanitaires."
  "|L'OMS définit la santé comme un état de bien-être physique, mental et social, et non comme la seule absence de maladie."
  "|La santé publique agit sur des groupes et des territoires, tandis que la médecine individuelle agit sur une personne."
  "|Les déterminants de santé sont les facteurs qui influencent l'état de santé : revenu, logement, travail, éducation, lien social et environnement."
  "|Les inégalités sociales de santé traduisent l'impact de ces déterminants sur l'espérance de vie et l'accès aux soins."
  "|La promotion de la santé développe les compétences et les environnements favorables à la santé."
  "|La prévention agit avant la survenue du dommage ; le soin intervient après."
  "|Les politiques publiques se déclinent à l'échelle nationale, régionale et locale."
  "|Les plans nationaux de santé publique fixent des objectifs et des indicateurs de résultat."
  "|L'agence régionale de santé pilote les actions régionales et coordonne les acteurs."
  "|La veille sanitaire surveille l'évolution des risques pour la population."
  "|Le professionnel du social contribue à ces politiques en identifiant les besoins des publics sur son territoire, compétence du bloc 3."),
[QC("Quelle définition de la santé est donnée par l'OMS ?", "La seule absence de maladie~Un état de bien-être physique, mental et social~La durée de vie~Le nombre de médecins", 1,
    "L'OMS inclut les dimensions physique, mentale et sociale du bien-être."),
 QC("Sur quoi agit la santé publique ?", "Sur un seul patient~Sur des populations et des territoires~Sur les seuls hôpitaux~Sur le budget d'un seul service", 1,
    "La santé publique a une dimension collective et territoriale."),
 QC("Quel élément est un déterminant de santé ?", "La couleur des murs~Le logement et le niveau de revenu~La marque du fauteuil~La taille du bureau", 1,
    "Revenu, logement, travail et éducation influencent la santé des populations."),
 QC("Que désignent les inégalités sociales de santé ?", "Des différences de prix des médicaments~L'impact des conditions de vie sur la santé et l'accès aux soins~Une préférence de couleur~Le nombre de pharmacies", 1,
    "Les conditions de vie produisent des écarts de santé et d'accès aux soins."),
 QC("Quel acteur pilote les actions de santé au niveau régional ?", "La mairie~L'agence régionale de santé~Le conseil d'administration d'un établissement~La CNIL", 1,
    "L'ARS est le pilote régional de la politique de santé."),
 QC("Quel outil fixe des objectifs de santé publique à l'échelle nationale ?", "Le plan national de santé publique~Le budget d'un service~Le contrat de séjour~Le règlement intérieur", 0,
    "Les plans nationaux définissent des objectifs et des indicateurs."),
 QC("Quel rôle revient au technicien supérieur face aux politiques publiques ?", "Les remplacer~Identifier les besoins des publics sur le territoire~Les contester systématiquement~Les ignorer", 1,
    "Le bloc 3 attend l'identification des besoins et la place de la structure dans les politiques."),
 QT("Expliquer la différence entre promotion de la santé et prévention et donner un exemple de chacune.",
    "La prévention vise à éviter la survenue d'un problème de santé ou à en limiter les conséquences : dépistage, vaccination, information sur les risques ou aménagement sécurisé des lieux. La promotion de la santé est plus large : elle vise à créer des conditions et des compétences qui permettent aux personnes de prendre soin d'elles-mêmes et de choisir des modes de vie favorables. Par exemple, organiser un dépistage du diabète dans un centre social relève de la prévention ; animer un atelier de cuisine et d'activité physique avec les habitants, adapter les espaces et rendre l'information lisible relève de la promotion. Les deux démarches sont complémentaires et s'inscrivent dans les politiques sanitaires locales.",
    "On distingue éviter le risque et créer des capacités, avec un exemple pour chacune."),
 QT("Comment un établissement social peut-il contribuer à une politique de santé sur son territoire ?",
    "Il contribue d'abord par la connaissance du terrain : les agents recueillent et analysent les besoins et demandes des publics, repèrent les publics éloignés des soins et signalent les difficultés d'accès aux droits. Il participe ensuite aux réseaux et partenariats locaux avec l'ARS, le département, les centres de santé et les associations. Il met en œuvre des actions de prévention adaptées à son public : ateliers d'information, accompagnement aux rendez-vous médicaux et médiation. Il rend des données d'activité exploitables pour évaluer les effets de ces actions. Enfin, il fait remonter les obstacles rencontrés, car une politique publique s'ajuste à partir des observations faites sur le terrain par les professionnels et les usagers.",
    "On attend identification des besoins, partenariats, actions de prévention, données et remontée d'obstacles.")],
C("La santé publique agit sur les populations et leurs conditions de vie, pas seulement sur les maladies individuelles.",
  "Déterminants + prévention + promotion + politiques",
  "OMS · inégalités sociales de santé · ARS · plans nationaux",
  "Santé publique~Dimension collective~Déterminant~Facteur d'influence~Inégalité~Écart de santé~Politique~Action publique",
  "Identifier les besoins du public|Repérer les déterminants défavorables|Agir en prévention et promotion|Travailler en réseau|Remonter les obstacles observés",
  "Réduire la santé à l'absence de maladie|Ignorer les inégalités sociales|Agir sans partenaires|Ne jamais remonter les difficultés",
  "Centre social~Public éloigné des soins~Action~Atelier de prévention~Partenaire~ARS et département~Remontée~Obstacles d'accès",
  "Prévention~Éviter le risque~Promotion~Créer des capacités",
  "Santé individuelle~Soigner une personne~Santé publique~Agir sur une population"))

# ============================================================ SP2
add("SP2", "Prévention primaire, secondaire et tertiaire", "Santé publique et environnement professionnel", ["BTS1"],
S("La prévention est l'ensemble des actions qui visent à éviter une maladie, un accident ou une situation de dépendance."
  "|La prévention primaire agit avant l'apparition du problème, en supprimant les causes ou en renforçant les facteurs protecteurs."
  "|La vaccination, l'information sur les risques et l'aménagement sécurisé des locaux relèvent de la prévention primaire."
  "|La prévention secondaire intervient à un stade précoce, avant les symptômes ou au début de la maladie."
  "|Le dépistage organisé et le repérage précoce des difficultés sont des exemples de prévention secondaire."
  "|La prévention tertiaire intervient après la maladie ou l'accident pour limiter les complications et la dépendance."
  "|La réadaptation, l'accompagnement à l'autonomie et le suivi après hospitalisation relèvent de la prévention tertiaire."
  "|Ces trois niveaux sont complémentaires et s'appliquent aussi aux risques psycho-sociaux."
  "|Un établissement social agit souvent en prévention tertiaire auprès de publics déjà affectés par une pathologie."
  "|Il agit aussi en prévention primaire en développant des actions de promotion de la santé."
  "|Le repérage précoce suppose des indicateurs simples et une formation des professionnels de première ligne."
  "|Le référentiel BTS SP3S attend la connaissance des répercussions sanitaires et sociales des pathologies des personnes accompagnées."),
[QC("Quand intervient la prévention primaire ?", "Après la maladie~Avant l'apparition du problème~Au stade des complications~Uniquement à l'hôpital", 1,
    "La prévention primaire agit en amont, avant que le dommage existe."),
 QC("Quel exemple relève de la prévention secondaire ?", "La vaccination~Un dépistage organisé~La réadaptation~Un plan d'évacuation", 1,
    "Le dépistage repère précocement une maladie avant les symptômes."),
 QC("Quel est l'objet de la prévention tertiaire ?", "Supprimer les causes~Limiter les complications après la maladie~Informer le grand public~Organiser les urgences", 1,
    "La prévention tertiaire réduit les conséquences d'une maladie déjà installée."),
 QC("Quelle action relève de la prévention primaire dans un établissement ?", "Un suivi après hospitalisation~Un aménagement sécurisé des locaux~Une rééducation~Un accompagnement à la fin de vie", 1,
    "Sécuriser les lieux supprime un risque avant qu'il ne produise un accident."),
 QC("Quel niveau concerne le plus souvent un établissement social accompagnant des personnes malades ?", "Primaire~Secondaire~Tertiaire~Aucun", 2,
    "L'accompagnement de publics déjà touchés relève largement du tertiaire, sans exclure les autres niveaux."),
 QC("Quel outil favorise le repérage précoce ?", "Un indicateur simple et une formation des agents~Une attente sans évaluation~Un délai allongé~Une absence de consigne", 0,
    "Des repères simples et des agents formés permettent de détecter tôt les difficultés."),
 QC("Comment articuler les trois niveaux de prévention ?", "En choisissant un seul niveau~En les combinant selon le cycle de la maladie~En les appliquant dans l'ordre inverse~En les réservant à l'hôpital", 1,
    "Les trois niveaux se complètent tout au long du parcours de santé."),
 QT("Illustrer les trois niveaux de prévention à propos des chutes chez les personnes âgées accompagnées.",
    "En prévention primaire, on agit avant la chute : éclairage suffisant, sols non glissants, barres d'appui, chaussures adaptées et Information de la personne sur les risques. En prévention secondaire, on repère précocement les signes de fragilité : difficulté à se lever, trouble de l'équilibre, peur de marcher, et on propose une évaluation et une rééducation avant la première chute grave. En prévention tertiaire, après une chute, on organise le suivi médical, la réadaptation, l'adaptation du logement et l'accompagnement pour retrouver l'autonomie et éviter une nouvelle chute. Ces trois niveaux se succèdent dans le temps mais doivent être engagés ensemble dans le projet d'accompagnement de la personne.",
    "On classe correctement les actions dans les trois niveaux et on montre leur continuité."),
 QT("Expliquer le rôle du professionnel social dans le repérage précoce d'une situation de dépendance.",
    "Le professionnel voit la personne dans la durée et dans ses actes quotidiens, ce que les services médicaux ne voient pas toujours. Il repère les changements : négligence de l'hygiène, difficulté à gérer les papiers, perte de poids, isolement, refus de sortir ou répétition des mêmes demandes. Il note ces observations comme des faits, sans poser un diagnostic, et les transmet au responsable et, avec l'accord de la personne, aux professionnels concernés. Il propose un échange pour comprendre ce que la personne vit et évite de la stigmatiser. Son rôle est d'alerter tôt, d'orienter vers une évaluation adaptée et de soutenir l'acceptation de l'aide, car un repérage précoce réduit le risque de crise et de perte d'autonomie.",
    "On décrit le repérage par les faits, la transmission encadrée et l'orientation précoce sans diagnostic.")],
C("Les trois niveaux de prévention couvrent l'avant, le début et l'après du problème de santé.",
  "Primaire = éviter · secondaire = repérer tôt · tertiaire = limiter les suites",
  "Vaccination · dépistage · réadaptation · prévention des chutes",
  "Primaire~Supprimer la cause~Secondaire~Repérer précocement~Tertiaire~Limiter les suites~Repérage~Observation des changements",
  "Agir sur les causes et les facteurs protecteurs|Mettre en place des repères de détection|Transmettre les observations sans diagnostic|Orienter vers une évaluation|Accompagner le suivi dans la durée",
  "Poser un diagnostic médical|Se limiter à la prévention primaire|Noter une impression comme un fait|Ignorer les signes discrets",
  "Chute~Risque identifié~Avant~Sol et éclairage~Début~Repérage de fragilité~Après~Réadaptation",
  "Prévention~Agir avant le dommage~Soin~Agir après le dommage",
  "Observation~Fait noté~Diagnostic~Acte médical réservé"))

# ============================================================ SP3
add("SP3", "Veille sanitaire, signalement et gestion d'alerte", "Santé publique et environnement professionnel", ["BTS2"],
S("La veille sanitaire est la surveillance continue de l'état de santé de la population et des risques qui la menacent."
  "|Elle repose sur la collecte, l'analyse et l'interprétation de données provenant de nombreuses sources."
  "|Les signalements d'agents sanitaires, les données de mortalité et les données de consommation de soins alimentent cette surveillance."
  "|Santé publique France est l'agence nationale qui anime la veille, l'expertise et la communication en santé publique."
  "|Les agences régionales de santé relaient les alertes et organisent les actions locales."
  "|Un signalement est une transmission d'information sur un événement qui peut présenter un risque pour la santé."
  "|Certaines maladies et certains événements indésirables font l'objet d'une déclaration obligatoire."
  "|Un professionnel qui repère un risque doit suivre la procédure de l'établissement et informer son responsable."
  "|La notification interne ne doit pas être bloquée par la crainte de déranger ou d'être critiqué."
  "|La traçabilité du signalement est essentielle : date, faits observés, personne informée et suite donnée."
  "|L'alerte peut concerner un risque collectif, comme une épidémie, ou un risque individuel grave."
  "|Le référentiel BTS SP3S rattache ces savoirs à la santé publique et à la démarche qualité de la structure."),
[QC("Quel organisme anime la veille sanitaire au niveau national ?", "La CAF~Santé publique France~La CNIL~Le conseil départemental", 1,
    "Santé publique France est l'agence nationale de santé publique chargée de la veille."),
 QC("Quelle source alimente la veille sanitaire ?", "Les seules réunions de service~Les signalements et données de santé~La météo~Les prix des fournitures", 1,
    "Signalements, mortalité et consommation de soins sont des sources de données."),
 QC("Qu'appelle-t-on signalement ?", "Une simple rumeur~Une transmission d'information sur un risque potentiel~Une facture~Un contrat de travail", 1,
    "Le signalement transmet une information sur un événement pouvant présenter un risque."),
 QC("Que doit faire un professionnel qui repère un risque dans son service ?", "Attendre une confirmation totale~Suivre la procédure interne et informer son responsable~En parler uniquement à un collègue~Ne rien noter", 1,
    "La procédure interne et l'information hiérarchique s'imposent sans délai."),
 QC("Quel élément doit être tracé dans un signalement ?", "La seule opinion de l'agent~Date, faits, personne informée et suite donnée~L'heure du déjeuner~La météo", 1,
    "La traçabilité rend le signalement vérifiable et permet le suivi."),
 QC("Quel type de risque peut déclencher une alerte ?", "Uniquement individuel et bénin~Collectif comme une épidémie ou individuel grave~Seulement administratif~Aucun risque", 1,
    "Les alertes peuvent concerner la collectivité ou une personne en danger grave."),
 QC("Quelle attitude favorise la remontée des alertes ?", "Critiquer les signaleurs~Protéger la remontée et documenter la suite~Ignorer les petits signaux~Reporter systématiquement", 1,
    "Une culture de la remontée protège la sécurité des personnes et du service."),
 QT("Décrire la chaîne d'un signalement depuis l'observation d'un agent jusqu'à l'action correctrice.",
    "L'agent observe un fait : plusieurs usagers présentent les mêmes symptômes après un repas, ou un équipement présente un défaut. Il consigne les faits avec la date, le lieu, les personnes concernées, sans interpréter ni diffuser d'hypothèse non vérifiée. Il informe immédiatement son responsable hiérarchique selon la procédure interne. Le responsable évalue la gravité, prévient la direction et, si le risque dépasse le cadre local, déclenche les notifications prévues auprès des autorités sanitaires. Une cellule de crise peut être réunie pour décider des mesures : retrait d'un produit, information des usagers, renforcement des précautions. Toutes les décisions sont tracées avec leurs horaires et leurs responsables. Après l'épisode, une analyse permet de comprendre la cause et d'améliorer la procédure de veille.",
    "On attend observation factuelle, remontée hiérarchique, évaluation, notification, mesures, traçabilité et retour d'expérience."),
 QT("Expliquer la différence entre veille sanitaire et démarche qualité dans un établissement.",
    "La veille sanitaire regarde vers l'extérieur et vers la population : elle surveille l'apparition de risques pour la santé, reçoit les alertes des autorités et contribue à la protection collective. La démarche qualité regarde vers le fonctionnement interne : elle vise à améliorer les prestations, à réduire les écarts entre les procédures et les pratiques et à satisfaire les usagers. Elles se rejoignent sur la gestion des risques : un événement indésirable grave dans un établissement est à la fois un sujet de qualité interne et, s'il révèle un danger pour la santé, un signalement à remonter. Un bon dispositif combine les deux : la procédure interne traite l'incident et la veille sanitaire vérifie s'il dépasse le cadre local.",
    "On distingue surveillance externe et amélioration interne, puis on montre leur point de convergence.")],
C("Un signalement efficace est factuel, rapide, tracé et protégé : il permet d'agir avant la généralisation du risque.",
  "Observation + remontée + évaluation + action + retour d'expérience",
  "Santé publique France · ARS · déclaration obligatoire · traçabilité",
  "Veille~Surveillance continue~Signalement~Information sur un risque~Alerte~Réaction rapide~Trace~Suivi vérifiable",
  "Consigner les faits observés|Informer le responsable sans délai|Évaluer la gravité et la portée|Appliquer les mesures décidées|Analyser l'épisode après coup",
  "Diffuser une hypothèse comme un fait|Attendre une certitude absolue|Ne rien tracer|Critiquer la personne qui alerte",
  "Symptômes~Repérés chez plusieurs usagers~Signalement~Date et faits~Décision~Mesures immédiates~Retour~Procédure améliorée",
  "Veille sanitaire~Protection de la population~Démarche qualité~Amélioration du service",
  "Signalement~Alerter~Rumeur~Non vérifiée"))

# ============================================================ SP4
add("SP4", "Risques professionnels et document unique", "Santé publique et environnement professionnel", ["BTS1"],
S("Le document unique d'évaluation des risques professionnels recense les risques auxquels les salariés sont exposés."
  "|Sa tenue est une obligation légale pour les employeurs, quel que soit l'effectif."
  "|Il est mis à jour au moins une fois par an et à chaque changement important de situation."
  "|L'évaluation consiste à identifier les dangers, les personnes exposées et les situations à risque."
  "|Un danger est un élément susceptible de nuire ; le risque est la combinaison de la probabilité et de la gravité du dommage."
  "|Les grands domaines de risques sont les risques physiques, chimiques, biologiques, psycho-sociaux et liés au milieu."
  "|Dans le secteur social, on retrouve le port de charges, les expositions biologiques et la violence des usagers."
  "|La matrice de risque croise la fréquence d'exposition et la gravité pour classer les priorités d'action."
  "|Les mesures de prévention suivent une hiérarchie : supprimer le risque, le remplacer, agir collectivement, puis protéger individuellement."
  "|Le port d'équipements de protection individuelle est le dernier recours, pas la première réponse."
  "|Les salariés et leurs représentants sont associés à l'évaluation et à l'actualisation du document."
  "|Le référentiel BTS SP3S attend la connaissance de la typologie des principaux risques professionnels."),
[QC("Quelle est la périodicité minimale de mise à jour du document unique ?", "Une fois par an~Une fois tous les cinq ans~Uniquement après un accident~Une fois par trimestre", 0,
    "Le document unique est révisé au moins annuellement et lors de tout changement important."),
 QC("Quelle différence distingue danger et risque ?", "Ils sont identiques~Le danger est une source possible de dommage, le risque combine probabilité et gravité~Le danger est toujours individuel~Le risque n'existe qu'après l'accident", 1,
    "Le risque apprécie la probabilité et la gravité du dommage lié à un danger."),
 QC("Quel risque est fréquent dans le secteur social ?", "La violence d'un usager~La seule routine administrative~L'absence de public~Le prix du papier", 0,
    "Les risques psycho-sociaux et la violence font partie des risques du secteur."),
 QC("Que permet une matrice de risque ?", "De classer les priorités d'action~De supprimer tous les risques~De remplacer l'évaluation~De calculer le salaire", 0,
    "Le croisement fréquence et gravité hiérarchise les actions de prévention."),
 QC("Quelle est la première mesure de prévention dans la hiérarchie ?", "Distribuer des gants~Supprimer le risque à la source~Former après l'accident~Signaler sans agir", 1,
    "La suppression du danger vient avant les protections individuelles."),
 QC("Quel statut a l'équipement de protection individuelle ?", "La première solution~Le dernier recours de la hiérarchie~Une obligation inutile~Un remplacement de la formation", 1,
    "Les EPI protègent lorsque les mesures collectives ne suffisent pas."),
 QC("Qui doit être associé à l'évaluation des risques ?", "La direction seule~Les salariés et leurs représentants~Les seuls fournisseurs~Personne", 1,
    "La participation des travailleurs améliore la pertinence de l'évaluation."),
 QT("Expliquer la démarche d'évaluation d'un risque dans le document unique et montrer l'intérêt de la hiérarchie des mesures.",
    "On identifie d'abord le danger : par exemple, un usager agité dans un accueil sans séparation. On détermine ensuite qui est exposé, à quelle fréquence et dans quelles circonstances. On estime la probabilité et la gravité pour classer le risque dans la matrice, ce qui donne une priorité d'action. On applique ensuite la hiérarchie des mesures : peut-on supprimer le risque en réorganisant l'accueil, par exemple en installant un espace d'attente séparé et un dispositif d'appel ? Peut-on le remplacer par une organisation différente ? Vient ensuite la protection collective, comme une formation des agents et une procédure d'escalade. Les équipements individuels et les consignes ne viennent qu'en dernier. Cette hiérarchie évite de dépenser en protections individuelles ce qui devrait être investi dans l'organisation du travail.",
    "On décrit identification, exposition, cotation et hiérarchie des mesures avec un exemple du secteur."),
 QT("Un agent se blesse en manipulant un usager à mobilité réduite. Comment analyser l'événement dans une logique de prévention ?",
    "On recueille d'abord les faits : lieu, heure, geste réalisé, personnel présent, formation reçue et conséquences pour l'agent et l'usager. On identifie le danger : le port de charge humaine sans aide technique. On évalue l'exposition : fréquence des manipulations, absence de lève-personne disponible, effectif insuffisant au moment du geste. On cotte le risque et on inscrit l'analyse dans le document unique, en actualisant la rubrique concernée. On applique la hiérarchie : former au geste est utile mais insuffisant si aucun matériel n'est disponible ; la première mesure est d'équiper le service et de réorganiser les interventions à deux. On définit une procédure claire, une responsibility identifiée et une date de mise en œuvre. Enfin, on informe les salariés des modifications et on suit les indicateurs d'accidents et de plaintes.",
    "On attend analyse factuelle, actualisation du DUERP, mesures hiérarchisées et suivi.")],
C("Le document unique n'est pas un classeur administratif : c'est un outil de décision pour protéger les salariés.",
  "Danger + exposition + probabilité + gravité = risque coté",
  "Hiérarchie : supprimer · remplacer · protéger collectivement · protéger individuellement",
  "Danger~Source possible de dommage~Risque~Probabilité et gravité~Matrice~Priorisation~DUERP~Obligation annuelle",
  "Identifier les dangers et les exposés|Coter fréquence et gravité|Classer les priorités d'action|Appliquer la hiérarchie des mesures|Actualiser et informer les équipes",
  "Remplir le document une seule fois|Se contenter des EPI|Ignorer les risques psycho-sociaux|Ne pas associer les salariés",
  "Manipulation~Usager à mobilité réduite~Risque~Port de charge~Mesure~Lève-personne et formation~Suivi~Indicateur d'accidents",
  "Danger~Peut nuire~Risque~Probabilité multipliée par gravité",
  "EPI~Dernier recours~Protection collective~Priorité supérieure"))

# ============================================================ SP5
add("SP5", "Hygiène et asepsie : prévention des infections en établissement", "Santé publique et environnement professionnel", ["BTS2"],
S("Les infections associées aux soins sont contractées au cours d'une prise en charge sanitaire ou sociale."
  "|On distingue les infections nosocomiales et les infections liées aux actes de soins ou à l'environnement."
  "|Une infection résulte d'une chaîne qui associe une source, un mode de transmission et une personne réceptive."
  "|Les principaux modes de transmission sont le contact direct, les gouttelettes respiratoires et l'air."
  "|L'hygiène des mains est la mesure de prévention la plus efficace et la plus accessible."
  "|La friction hydro-alcoolique est privilégiée lorsque les mains ne sont pas visiblement souillées."
  "|Le lavage au savon et à l'eau est requis en cas de souillure visible ou après un passage aux toilettes."
  "|L'Organisation mondiale de la santé identifie cinq moments clés où l'hygiène des mains est indispensable."
  "|L'asepsie désigne l'ensemble des mesures qui évitent l'introduction de micro-organismes lors d'un geste."
  "|Gants, masque, tenue et protection des surfaces complètent l'hygiène des mains sans la remplacer."
  "|Le nettoyage et la désinfection du matériel et des surfaces suivent une procédure écrite et tracée."
  "|La surveillance et le signalement des infections permettent d'évaluer la prévention et de la renforcer."),
[QC("Qu'est-ce qu'une infection associée aux soins ?", "Une infection contractée lors d'une prise en charge~Une infection toujours d'origine alimentaire~Une infection héréditaire~Une infection qui ne peut pas se transmettre", 0,
    "L'infection associée aux soins est liée à la prise en charge, quel que soit le lieu."),
 QC("Quelle est la mesure de prévention la plus efficace contre les infections ?", "L'hygiène des mains~Le port de gants en permanence~La fermeture des fenêtres~L'usage de parfum", 0,
     "La friction ou le lavage des mains rompt la chaîne de transmission."),
 QC("Quand privilégier la friction hydro-alcoolique ?", "Lorsque les mains sont visiblement souillées~Lorsque les mains ne sont pas visiblement souillées~Après un repas seulement~Jamais", 1,
     "Une souillure visible impose un lavage au savon et à l'eau."),
 QC("Combien de moments de l'hygiène des mains l'OMS identifie-t-elle ?", "Trois~Cinq~Sept~Dix", 1,
     "Les cinq moments de l'OMS couvrent les situations clés des gestes de soin."),
 QC("Que désigne l'asepsie ?", "Des mesures qui évitent l'introduction de micro-organismes~Un simple nettoyage visuel~Une méthode de cuisson~Un type de gant particulier", 0,
     "L'asepsie est un ensemble de mesures de prévention de la contamination."),
 QC("Dans la chaîne de transmission, quelle part représente une personne non immunisée ?", "La source~Le mode de transmission~La personne réceptive~Le vecteur", 2,
     "La personne réceptive est celle qui peut contracter l'infection."),
 QC("Pourquoi signaler une infection nosocomiale ?", "Pour la dissimuler~Pour analyser la situation et améliorer la prévention~Pour changer de service~Pour supprimer les procédures", 1,
     "Le signalement alimente l'analyse et l'amélioration des pratiques."),
 QT("Expliquer la chaîne de transmission d'une infection et montrer comment l'hygiène des mains la rompt.",
     "La chaîne de transmission comporte trois éléments : une source de micro-organismes, un mode de transmission et une personne réceptive. La source peut être un usager, un professionnel, un objet ou un environnement contaminé. Le mode de transmission est le contact direct, les gouttelettes émises lors de la parole ou de la toux, ou l'air pour certaines infections. La personne réceptive est exposée à un moment du soin. L'hygiène des mains agit sur le mode de transmission : en frictionnant ou en lavant les mains avant le contact, entre deux gestes et après le contact, on supprime le transport des micro-organismes d'un support à une personne. Les gants ne remplacent pas ce geste : ils se contaminent aussi et doivent être changés entre deux usagers. Rompre la chaîne à ce niveau protège à la fois l'usager, le professionnel et les autres personnes présentes.",
     "On attend les trois éléments de la chaîne et l'explication du rôle de l'hygiène des mains."),
 QT("Un professionnel enchaîne plusieurs accompagnements en gardant les mêmes gants. Analyser la situation et proposer une correction.",
     "Cette pratique contamine le gant au contact du premier usager puis le transporte vers le suivant : le gant devient un vecteur et la chaîne de transmission reste active. Elle donne aussi une fausse impression de sécurité, car le port de gants est souvent perçu comme une protection suffisante. La correction consiste à changer de gants entre deux usagers et à se frictionner les mains à chaque changement, conformément aux moments prévus. On rappelle que les gants sont un complément et non un substitut de l'hygiène des mains, et qu'ils doivent être retirés avant de toucher des surfaces propres, un clavier ou un dossier. La démarche qualité prévoit une formation des équipes, l'affichage de la procédure dans les postes de soin et un contrôle régulier des pratiques par les responsables.",
     "On identifie le risque de transmission, on propose le changement de gants et l'hygiène des mains, puis un encadrement collectif.")],
C("Prévenir les infections, c'est rompre la chaîne de transmission par des gestes simples et rigoureux.",
  "Source + mode de transmission + personne réceptive = infection évitable",
  "Friction hydro-alcoolique · lavage au savon · asepsie · nettoyage · signalement",
  "IAS~Infection liée aux soins~Transmission~Contact, air, gouttelettes~Hygiène des mains~Friction ou lavage~Asepsie~Mesures sans apport microbien~Surveillance et signalement",
  "Repérer la source et le mode de transmission|Se frictionner les mains aux moments prévus|Laver au savon si les mains sont souillées|Appliquer l'asepsie et les protections adaptées|Nettoyer, désinfecter et signaler",
  "Garder les mêmes gants entre deux usagers|Frictionner des mains visiblement souillées|Confondre nettoyage et désinfection|Omettre le signalement d'une infection",
  "Friction~Geste avant chaque contact usager~Souillure~Lavage au savon et à l'eau~Gants~Changement entre deux personnes~IAS~Signalée puis analysée",
  "Transmission directe~Contact peau à peau~Gouttelettes respiratoires~Transmission indirecte~Objets et surfaces contaminés~Mains non lavées",
  "Hygiène des mains~Friction hydro-alcoolique~Lavage au savon~Port de gants~Pas de port permanent~Changement systématique"))

# ============================================================ SP6
add("SP6", "Surveillance médicale du travail et maintien en emploi", "Santé publique et environnement professionnel", ["BTS2"],
S("La surveillance médicale des travailleurs est une obligation qui incombe à l'employeur."
  "|Elle vise à prévenir les atteintes à la santé liées aux conditions de travail."
  "|La visite d'information et de prévention est organisée lors de l'embauche."
  "|Elle est renouvelée selon une périodicité définie, renforcée pour les postes exposés à des risques."
  "|Le médecin du travail exerce sa mission dans l'indépendance vis-à-vis de l'employeur."
  "|Il conseille l'employeur, les salariés et les représentants du personnel sur la prévention."
  "|Une inaptitude peut être constatée après examens, étude du poste et échange avec le salarié."
  "|L'avis d'inaptitude précise les restrictions et les capacités conservées."
  "|La recherche d'un reclassement précède toute rupture du contrat de travail."
  "|Les maladies professionnelles sont reconnues et réparées selon des tableaux réglementaires."
  "|Un suivi post-professionnel peut être prévu après certaines expositions dangereuses."
  "|La traçabilité des expositions, des visites et des avis est un outil de prévention durable."),
[QC("Qui organise la surveillance médicale des salariés ?", "Le salarié seul~L'employeur~Le client de la structure~Le fournisseur", 1,
     "La surveillance médicale est une obligation de l'employeur."),
 QC("Quand la visite d'information et de prévention est-elle réalisée ?", "À l'embauche puis selon une périodicité définie~Uniquement avant un départ~Une fois par carrière~Jamais", 0,
     "La visite est organisée à l'embauche et renouvelée selon la périodicité prévue."),
 QC("Quel principe caractérise l'action du médecin du travail ?", "Il dépend de l'employeur~Il agit dans l'indépendance~Il décide des sanctions~Il remplace le responsable hiérarchique", 1,
     "L'indépendance du médecin du travail garantit la qualité de son conseil."),
 QC("Que doit contenir un avis d'inaptitude ?", "Seulement la date de la visite~Les restrictions et les capacités conservées~Le salaire du salarié~L'avis des collègues", 1,
     "L'avis précise ce que le salarié peut et ne peut plus faire."),
 QC("Quelle démarche précède une rupture liée à l'inaptitude ?", "Le licenciement immédiat~La recherche d'un reclassement~La démission du salarié~Aucune démarche", 1,
     "L'employeur doit rechercher un reclassement avant la rupture."),
 QC("Comment les maladies professionnelles sont-elles reconnues ?", "Par une simple déclaration verbale~Selon des tableaux réglementaires~Par décision du seul employeur~Par le client", 1,
     "Les tableaux de maladies professionnelles encadrent la reconnaissance."),
 QC("À quoi sert la traçabilité des expositions ?", "À augmenter les effectifs~À documenter les risques et le suivi~À supprimer les visites~À éviter tout signalement", 1,
     "La traçabilité permet de relier une exposition à un risque et à un suivi."),
 QT("Expliquer le rôle du médecin du travail dans la prévention et le maintien en emploi.",
     "Le médecin du travail contribue à la protection de la santé des salariés. Il réalise la visite d'information et de prévention, examine les capacités de la personne au regard du poste et repère les risques auxquels elle est exposée. Il informe le salarié sur les précautions adaptées et conseille l'employeur sur l'aménagement du poste, l'organisation du travail et les mesures collectives de prévention. Il travaille avec les représentants du personnel et peut proposer des actions sur l'ensemble de la structure. Lorsque l'état de santé ne permet plus d'occuper le poste, il motive un avis d'inaptitude en précisant les restrictions et les capacités restantes, ce qui oriente la recherche de reclassement. Son indépendance est essentielle : son avis ne doit ni satisfaire l'employeur ni éviter la difficulté, mais refléter la réalité médicale et les exigences du poste.",
     "On attend visite, conseil, prévention collective, avis d'inaptitude motivé et indépendance."),
 QT("Un salarié du secteur social présente des douleurs liées au port de charges répété. Comment organiser la suite ?",
     "On recueille d'abord les faits : nature des gestes, fréquence, matériel disponible, ancienneté de la douleur et conséquences sur l'activité. On informe le responsable et on consigne la situation dans le document unique et le registre des accidents ou incidents. Le salarié est orienté vers le médecin du travail, qui évalue la capacité et propose des restrictions adaptées si nécessaire. En parallèle, l'employeur analyse le poste avec le service prévention : achat d'un lève-personne, travail à deux, formation aux gestes et réorganisation des interventions. On recherche un reclassement temporaire ou définitif si le poste ne peut pas être aménagé. On suit ensuite l'évolution avec des indicateurs : douleurs déclarées, arrêts de travail et incidents de manipulation.",
     "On attend recueil des faits, avis médical, aménagement du poste, reclassement éventuel et suivi.")],
C("La surveillance médicale ne se limite pas à un examen : elle oriente la prévention et le maintien en emploi.",
  "Visite + examen + avis + aménagement = maintien en emploi",
  "Visite d'information et de prévention · inaptitude · reclassement · tableaux de maladies professionnelles",
  "Visite~Information et prévention~Médecin~Indépendance et conseil~Inaptitude~Restrictions et capacités~Reclassement~Recherche avant rupture~Maladie professionnelle~Reconnaissance par tableau",
  "Organiser la visite à l'embauche|Repérer les expositions et les risques|Évaluer la capacité au poste|Conseiller l'aménagement et la prévention|Suivre l'avis et tracer les actions",
  "Confondre visite et simple formalité|Laisser le médecin décider seul du licenciement|Ignorer les restrictions|Omettre la recherche de reclassement",
  "Embauche~Visite d'information et de prévention~Douleur~Exposition au port de charge~Avis~Restrictions motivées~Poste~Aménagement et suivi",
  "Médecin du travail~Indépendant et conseil~Employeur~Responsable de la prévention",
  "Inaptitude~Capacités réduites~Aptitude~Poste compatible")
)

# ============================================================ SP7
add("SP7", "Sécurité alimentaire et hygiène en restauration collective", "Santé publique et environnement professionnel", ["BTS1"],
S("La restauration collective sert des publics qui peuvent être fragiles, comme les personnes âgées ou les enfants."
  "|L'hygiène alimentaire vise à prévenir les toxi-infections alimentaires collectives."
  "|La réglementation impose des règles d'hygiène et la traçabilité des denrées."
  "|La chaîne du froid doit être maintenue à toutes les étapes, du stockage au service."
  "|La date limite de consommation et la date de durabilité minimale n'ont pas la même signification."
  "|La préparation respecte la séparation des aliments crus et des aliments cuits."
  "|Une cuisson à cœur suffisante détruit la plupart des micro-organismes pathogènes."
  "|Le nettoyage et la désinfection des plans de travail et du matériel sont planifiés."
  "|Les allergènes sont identifiés et signalés aux usagers avant le service."
  "|Un plan de contrôle et des autocontrôles structurent la démarche hygiénique."
  "|En cas de suspicion de toxi-infection, les portions et les échantillons sont conservés."
  "|Le signalement aux autorités sanitaires est obligatoire pour certaines toxi-infections."),
[QC("Quel public est particulièrement exposé en restauration collective ?", "Les personnes âgées et les enfants~Les seuls adultes actifs~Le personnel de cuisine uniquement~Les fournisseurs", 0,
     "Les publics fragiles sont plus sensibles aux infections alimentaires."),
 QC("Que désigne une toxi-infection alimentaire collective ?", "Une maladie transmise par l'air~Une infection liée à l'ingestion d'un aliment contaminé~Une allergie saisonnière~Une fracture", 1,
     "La contamination se fait par ingestion d'aliments ou de boissons."),
 QC("Quelle règle s'impose pour la chaîne du froid ?", "La rompre régulièrement~La maintenir en toutes circonstances~La remplacer par le congélateur seulement~L'ignorer", 1,
     "Une rupture de la chaîne du froid favorise la multiplication des bactéries."),
 QC("Quelle différence existe entre date limite de consommation et date de durabilité minimale ?", "Elles sont identiques~La première est sanitaire, la seconde concerne la qualité~La seconde est sanitaire, la première concerne le goût~Elles ne concernent que les boissons", 1,
     "La date limite de consommation est une limite de sécurité sanitaire."),
 QC("Comment éviter la contamination croisée en cuisine ?", "Mélanger cru et cuit~Séparer les aliments crus et cuits~Réchauffer sans contrôle~Laisser les surfaces sales", 1,
     "La séparation des aliments crus et cuits est une règle fondamentale."),
 QC("Pourquoi signaler les allergènes aux usagers ?", "Pour respecter la réglementation et protéger la santé~Pour augmenter le prix du repas~Pour changer la carte~Pour éviter les contrôles", 0,
     "L'information sur les allergènes est une obligation et une mesure de protection."),
 QC("Que faire en cas de suspicion de toxi-infection alimentaire ?", "Jeter tous les éléments~Conserver portions et échantillons et signaler~Continuer le service normalement~Ne rien noter", 1,
     "La conservation des éléments permet l'enquête et le signalement."),
 QT("Expliquer les principales règles d'hygiène qui préviennent une toxi-infection alimentaire collective.",
     "La prévention repose sur la maîtrise de la chaîne du froid, la séparation des aliments crus et cuits et une cuisson à cœur suffisante. Les denrées sont stockées selon leur température et leur date limite, avec traçabilité des lots. Les plans de travail, les ustensiles et les équipements sont nettoyés puis désinfectés selon une fréquence définie, en évitant tout contact entre une surface souillée et un aliment prêt à consommer. Le personnel applique une hygiène des mains rigoureuse et porte une tenue adaptée. Les allergènes sont recensés et communiqués aux usagers avant le service. Des autocontrôles réguliers vérifient les températures, le nettoyage et le respect des procédures. Si des signes d'infection apparaissent chez plusieurs convives, on conserve les portions et les échantillons, on isole les denrées suspectes et on signale sans délai selon la procédure.",
     "On attend chaîne du froid, séparation cru et cuit, nettoyage, allergènes, autocontrôles et signalement."),
 QT("Un service distribue un repas à des résidents âgés et plusieurs personnes présentent des troubles digestifs. Que faire ?",
     "On recueille d'abord les faits : heure du repas, plats servis, nombre de personnes atteintes, symptômes et état de santé des résidents. On prévient immédiatement le responsable et le service soignant, car les personnes âgées sont plus fragiles. On conserve les restes des plats, les portions non servies et les échantillons prélevés lors de la préparation, en respectant la chaîne du froid, et on suspend la distribution des denrées suspectes. On nettoie et désinfecte les zones concernées sans détruire les éléments utiles à l'enquête. Le signalement aux autorités sanitaires est effectué selon la procédure, car une toxi-infection alimentaire collective est concernée. On informe les familles dans le cadre prévu et on analyse le circuit pour identifier une rupture de la chaîne du froid, une erreur de cuisson ou une contamination croisée.",
     "On attend recueil des faits, protection des personnes, conservation des preuves, signalement et analyse.")],
C("Une hygiène alimentaire rigoureuse protège des publics fragiles et repose sur des contrôles simples et répétés.",
  "Chaîne du froid + séparation des aliments + cuisson + nettoyage = repas sûr",
  "Traçabilité · dates limites · allergènes · autocontrôles · signalement",
  "Denrées~Traçabilité et dates~Froid~Chaîne non rompue~Préparation~Cru et cuit séparés~Cuisson~Température à cœur~Service~Allergènes signalés",
  "Vérifier les dates et la chaîne du froid|Séparer les aliments crus et cuits|Cuire à température suffisante|Nettoyer et désinfecter les surfaces|Conserver les preuves et signaler",
  "Réchauffer sans mesure de température|Mélanger aliments crus et cuits|Ignorer les allergènes|Jeter les échantillons avant enquête",
  "Contrôle~Température des réfrigérateurs~Rupture~Risque de multiplication~Echantillon~Conservé au froid~Signalement~Autorité sanitaire",
  "Date limite de consommation~Sécurité sanitaire~Date de durabilité minimale~Qualité gustative",
  "Restauration collective~Publics fragiles~Restauration commerciale~Public varié"))

valider_et_ecrire(F, "btssp3s-mat-part-B.json")
