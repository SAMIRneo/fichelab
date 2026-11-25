# -*- coding: utf-8 -*-
"""Generateur btssp3s-mat-part-A.json — lot A : Culture générale et expression (7),
Communication (6), Management (7).

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


# ============================================================ CG1
add("CG1", "L'argumentation : thèse, arguments et exemples", "Culture générale et expression", ["BTS1"],
S("L'argumentation vise à convaincre un destinataire en organisant des raisons à l'appui d'une thèse."
  "|La thèse est l'idée principale défendue : elle doit être formulée clairement dès l'introduction."
  "|Une argumentation répond à une question problématisée et non à un simple sujet informatif."
  "|Les arguments sont des raisons de portée générale ; les exemples sont des cas concrets qui les illustrent."
  "|La progression peut être déductive, du général vers le particulier, ou inductive, du particulier vers le général."
  "|Le plan dialectique (thèse, antithèse, synthèse) convient aux sujets qui opposent deux positions."
  "|Le plan thématique ou analytique repose sur des axes qui approfondissent une même idée."
  "|Chaque paragraphe suit le modèle assertion, explication, exemple, transition."
  "|Les connecteurs logiques (donc, or, mais, d'abord, ensuite) rendent le raisonnement lisible."
  "|Les objections sont anticipées puis réfutées, ce qui renforce la crédibilité du propos."
  "|La conclusion répond au problème posé et peut ouvrir sur une prolongation du sujet."
  "|En BTS SP3S, l'argumentation est évaluée en U1 et sert aussi aux notes et comptes rendus professionnels."),
[QC("Quel est l'objet d'une argumentation ?", "Informer sans prendre position~Convaincre à l'aide de raisons~Raconter une histoire~Décrire un lieu", 1,
    "Argumenter, c'est défendre une idée avec des raisons pour convaincre."),
 QC("Qu'appelle-t-on une thèse ?", "Une objection~L'idée principale défendue~Un exemple~La conclusion", 1,
    "La thèse est l'idée centrale que l'auteur s'engage à démontrer."),
 QC("Quelle différence distingue un argument d'un exemple ?", "L'argument est un cas concret et l'exemple une raison générale~L'argument est une raison générale et l'exemple un cas concret~Ils ont exactement le même rôle~L'exemple remplace toujours l'argument", 1,
    "L'argument est une raison de portée générale, l'exemple en est une illustration concrète."),
 QC("Quel plan oppose deux positions successivement ?", "Plan thématique~Plan dialectique~Plan chronologique~Plan par document", 1,
    "Le plan dialectique suit thèse, antithèse puis synthèse."),
 QC("Quel connecteur introduit une objection ?", "Donc~Or ou mais~Ainsi~En effet", 1,
    "« Or » et « mais » marquent une opposition ou une objection."),
 QC("Que contient un paragraphe argumentatif bien construit ?", "Une assertion, une explication, un exemple et une transition~Seulement des chiffres~Une citation sans commentaire~La conclusion générale", 0,
    "Le modèle assertion, explication, exemple, transition structure le paragraphe."),
 QC("À quelle unité du BTS SP3S rattache-t-on l'expression écrite ?", "U1~U2~U3~U6", 0,
    "La culture générale et expression correspond à l'unité U1."),
 QT("Distinguer une argumentation d'une exposition et expliquer le rôle de l'exemple.",
    "L'exposition présente des faits ou des notions en cherchant surtout la clarté et l'exhaustivité, sans prendre position. L'argumentation, elle, part d'une thèse et mobilise des raisons pour obtenir l'adhésion du lecteur ; elle accepte donc la controverse et anticipe les objections. L'exemple n'est pas une preuve autonome : il rend sensible une raison générale en la situant dans un cas concret et daté. Sans explication qui le relie à l'argument, il reste une anecdote ; bien introduit par « par exemple » et commenté, il rend la démonstration crédible et mémorable.",
    "On oppose l'intention informative à l'intention persuasive, puis on précifie que l'exemple illustre l'argument sans le remplacer."),
 QT("Proposer un plan d'argumentation sur la question : « L'accompagnement des usagers peut-il se limiter à une réponse administrative ? »",
    "On choisit un plan dialectique. Premièrement, la réponse administrative est indispensable : elle garantit l'égalité de traitement, l'accès aux droits et la traçabilité des décisions. Deuxièmement, elle ne suffit pas : la demande exprime aussi des besoins psychologiques, sociaux et culturels que la seule procédure ne prend pas en charge ; l'écoute et l'orientation vers des dispositifs adaptés complètent l'action. Troisièmement, la synthèse propose une articulation : la procédure cadre l'action, l'accompagnement personnalisé lui donne sa finalité, sous réserve du secret professionnel et du consentement de la personne. La conclusion répond « non » à la question tout en reconnaissant la nécessité du cadre administratif.",
    "Le plan dialectique doit apparaître avec une synthèse nuancée et un lien explicite avec les exigences déontologiques du secteur.")],
C("Argumenter, c'est défendre une thèse avec des raisons ordonnées, des exemples et la réfutation des objections.",
  "Thèse + arguments + exemples + réfutation → conclusion",
  "Dialectique : thèse / antithèse / synthèse · thématique : axes · paragraphe : assertion-explication-exemple-transition",
  "Thèse~Idée défendue~Introduction~Argument~Raison générale~Corps du texte~Exemple~Cas concret~Illustration",
  "Lire le sujet et le problematiser|Dégager la thèse et les arguments|Distinguer arguments et exemples|Choisir le plan et rédiger|Anticiper les objections et conclure",
  "Confondre argument et exemple|Accumuler les exemples sans les commenter|Omettre les transitions|Introduire un avis personnel non argumenté",
  "Thèse~L'accompagnement dépasse la seule réponse administrative~Argument~La personne a aussi des besoins sociaux et psychologiques~Exemple~Un usager orienté vers un atelier d'insertion~Réfutation~La procédure reste nécessaire pour l'accès aux droits",
  "Argument~Raison abstraite et transfirable~Durée variable du pourquoi~Sert à étayer la thèse~Exemple~Fait concret et précis~Sert à illustrer~Doit être commenté",
  "Plan dialectique~Thèse antithèse synthèse~Sujet opposant deux positions~Conclusion nuancée~Plan thématique~Trois axes parallèles~Sujet à approfondir~Risque de répétition"))

# ============================================================ CG2
add("CG2", "Le commentaire de texte : méthode et axes de lecture", "Culture générale et expression", ["BTS1"],
S("Le commentaire de texte est un exercice d'analyse qui explique un extrait en dégageant son sens et ses procédés d'écriture."
  "|Il s'appuie sur une lecture attentive du texte, sans le résumer ni le remplacer par des connaissances extérieures."
  "|La première lecture identifie le thème, le genre du texte, l'auteur, la date et le destinataire."
  "|La problématique transforme le thème en question : elle guide le commentaire et évite la simple paraphrase."
  "|Les axes de lecture sont des grandes directions de sens, généralement deux ou trois, bien coordonnées à la problématique."
  "|Chaque axe se subdivise en sous-parties où l'on alterne citation courte, explication et analyse du procédé."
  "|Les registres (narratif, argumentatif, lyrique, polémique) orientent l'interprétation du texte."
  "|Les procédés lexicaux, syntaxiques et rhétoriques (métaphore, répétition, antithese) sont nommés puis interprétés."
  "|L'introduction présente le cadre du texte, la problématique et l'annonce du plan."
  "|La conclusion répond à la problématique et peut élargir vers une autre œuvre ou un enjeu du secteur sanitaire et social."
  "|Les transitions assurent le passage d'une partie à l'autre en reliant les idées déjà dites aux idées à venir."
  "|Cet exercice entraîne la lecture critique demandée pour analyser un document professionnel ou un témoignage d'usager."),
[QC("Quel est le premier réflexe devant un texte à commenter ?", "Rédiger immédiatement la conclusion~Lire attentivement et situer le texte~Apprendre le texte par cœur~Chercher des informations extérieures", 1,
    "On lit et on situe le texte avant toute interprétation."),
 QC("Qu'appelle-t-on problématique ?", "Le résumé du texte~Une question qui guide l'analyse~La bibliographie~La dernière phrase", 1,
    "La problématique est la question centrale à laquelle le commentaire répond."),
 QC("Combien d'axes de lecture comporte habituellement un commentaire ?", "Un seul~Deux ou trois~Six~Autant que de paragraphes", 1,
    "Deux ou trois axes suffisent pour construire un plan clair et équilibré."),
 QC("Quel élément ne doit pas dominer dans un commentaire ?", "La citation courte~L'explication du sens~La paraphrase intégrale~L'analyse des procédés", 2,
    "La paraphrase répète le texte sans l'expliquer : elle est à éviter."),
 QC("À quoi sert une transition ?", "À ajouter une citation~À relier deux parties~À remplacer la conclusion~À présenter l'auteur", 1,
    "La transition assure la continuité logique entre les parties."),
 QC("Quel procédé relève du plan lexical ?", "Une métaphore~Une répétition de mot~Une inversion de phrase~Une rime", 1,
    "La répétition est un procédé lexical ; la métaphore relève des images et l'inversion de la syntaxe."),
 QC("Dans quel but analyse-t-on les procédés d'écriture ?", "Pour décorer la copie~Pour expliquer comment le texte produit du sens~Pour allonger le devoir~Pour oublier le thème", 1,
    "Le procédé n'est nommé que s'il aide à interpréter le sens."),
 QT("Expliquer la différence entre paraphrase et commentaire, et donner une méthode pour éviter la première.",
    "La paraphrase reformule le texte avec les mêmes idées dans d'autres mots : elle fait circulariser le propos et n'apporte aucune explication. Le commentaire, lui, s'arrête sur un élément du texte, le cite brièvement, le situe dans son contexte, nomme le procédé si besoin et dégage l'effet de sens produit. Pour éviter la paraphrase, on travaille par citations courtes suivies de verbes d'analyse (« l'auteur souligne », « le terme suggère »), on formule systématiquement un « parce que » après chaque observation et on vérifie que chaque paragraphe répond à la problématique plutôt qu'à un résumé.",
    "La réponse doit opposer reformulation et interprétation et proposer une technique concrète (citation courte + verbe d'analyse + explication)."),
 QT("Comment construire le plan d'un commentaire d'un témoignage d'usager sur son accueil dans un établissement ?",
    "On situe d'abord le document : témoignage, date, contexte d'accueil, destinataire. La problématique peut être : « Comment ce récit transforme-t-il une expérience administrative en expérience relationnelle ? » Le premier axe analyse le vocabulaire de la froideur administrative et les phrases courtes qui traduisent l'attente. Le deuxième axe étudie le basculement : apparition des verbes d'écoute, changement de rythme, mise en avant de la personne. Le troisième axe interroge la portée du témoignage : ce qu'il révèle des attentes des usagers et de la démarche qualité. La conclusion répond à la problématique et relie l'analyse aux exigences d'accueil et d'accompagnement du référentiel BTS SP3S.",
    "On attend une problématique, deux ou trois axes et un dernier axe qui relie le texte aux enjeux professionnels.")],
C("Le commentaire explique comment un texte produit du sens : on cite peu, on analyse beaucoup.",
  "Situation + problématique + axes + citation courte + interprétation",
  "Registre = intention du texte · procédé = moyen employé · effet = sens produit",
  "Situation~Cadre du texte~Introduction~Problématique~Question centrale~Introduction~Axe~Direction de sens~Plan",
  "Situer l'auteur et le document|Identifier le thème et formuler la problématique|Repérer les procédés significatifs|Construire deux ou trois axes|Rédiger avec citations courtes et conclure",
  "Résumer le texte au lieu de l'expliquer|Ne jamais citer|Nommer un procédé sans l'interpréter|Oublier de répondre à la problématique",
  "Citation~Quelques mots entre guillemets~Procédé~Une répétition de terme~Effet~Une attente soulignée~Conclusion~Un lien avec l'accueil",
  "Paraphrase~Redit la même idée~Ne dégage rien de nouveau~Risque de cercle vicieux~Commentaire~Explique le fonctionnement~Nomme et interprète~Produit du sens",
  "Axe~Grande direction de lecture~Doit répondre à la problématique~Sous-partie~Citation et analyse~Équilibre entre les parties"))

# ============================================================ CG3
add("CG3", "La dissertation : plans dialectique et thématique", "Culture générale et expression", ["BTS1"],
S("La dissertation est un devoir personnel qui répond à une question de culture générale par une réflexion organisée et argumentée."
  "|Elle exige une culture large : exemples historiques, littéraires, artistiques ou tirés de l'actualité sanitaire et sociale."
  "|Le travail préparatoire consiste à analyser chaque mot du sujet et à dégager les tensions qu'il contient."
  "|La problématique est la question que le candidat se pose pour traiter le sujet sans le contourner."
  "|Le plan dialectique comporte une thèse, une antithèse et une synthèse qui nuance les deux premières positions."
  "|Le plan thématique répartit l'analyse en trois axes qui traitent la question sous des angles complémentaires."
  "|Le plan choisi dépend du libellé : un sujet opposant deux termes appelle souvent le plan dialectique."
  "|Chaque partie comprend plusieurs paragraphes, chacun appuyé sur un exemple précis et expliqué."
  "|Les exemples doivent être analysés, pas simplement énumérés : on montre en quoi ils répondent à la question."
  "|L'introduction amorce le sujet, le définit, le problématise et annonce le plan."
  "|La conclusion apporte une réponse claire et ouvre le sujet sur un enjeu contemporain ou professionnel."
  "|La maîtrise de la langue et la lisibilité de la copie sont prises en compte dans la notation de l'unité U1."),
[QC("Que demande une dissertation ?", "Un résumé de cours~Une réflexion personnelle organisée et argumentée~Une liste de dates~Une traduction", 1,
    "La dissertation exprime une réflexion personnelle construite à partir de exemples."),
 QC("Quel plan comporte thèse, antithèse et synthèse ?", "Le plan thématique~Le plan dialectique~Le plan chronologique~Le plan par auteur", 1,
    "Le plan dialectique se déroule en trois temps : affirmation, opposition, dépassement."),
 QC("À quoi sert la problématique ?", "À réciter le cours~À guider la réflexion sans contourner le sujet~Décorer l'introduction~Remplacer la conclusion", 1,
    "Elle transforme le sujet en question de manière à organiser la réponse."),
 QC("Quel type de sujet appelle plutôt un plan dialectique ?", "Un sujet qui oppose deux termes~Une simple liste de faits~Une consigne de traduction~Un problème de calcul", 0,
    "L'opposition entre deux positions appelle naturellement le plan dialectique."),
 QC("Comment traiter un exemple en dissertation ?", "Le citer sans commentaire~L'énumérer avec d'autres~L'analyser pour montrer son lien avec la question~Le placer uniquement en conclusion", 2,
    "Un exemple doit être choisi, présenté et analysé au service de l'argument."),
 QC("Quelle partie nuance les deux premières dans le plan dialectique ?", "L'introduction~La thèse~L'antithèse~La synthèse", 3,
    "La synthèse dépasse l'opposition initiale en proposant une position nuancée."),
 QC("Que doit apporter la conclusion ?", "Une nouvelle problématique~Une réponse claire et une ouverture~Des exemples supplémentaires~L'annonce du plan", 1,
    "La conclusion répond au sujet et ouvre sur une prolongation."),
 QT("Comparer les plans dialectique et thématique et indiquer quand les employer.",
    "Le plan dialectique organise le propos selon une opposition : d'abord les raisons qui soutiennent une position, ensuite celles qui la contestent, enfin une synthèse qui dépasse le conflit. Il convient aux sujets formulés autour de deux termes opposés ou d'une question « jusqu'à quel point », « faut-il choisir ». Le plan thématique répartit l'analyse en axes parallèles, par exemple le cadre juridique, l'accompagnement relationnel et l'organisation interne : il convient aux sujets qui demandent d'explorer les dimensions complémentaires d'une même réalité. Le plan dialectique risque le manichéisme s'il n'est pas nuancé ; le plan thématique risque la juxtaposition si les axes ne sont pas reliés par une progression.",
    "On compare les deux structures, on donne un critère de choix et on identifie le principal risque de chacune."),
 QT("Construire un plan de dissertation sur : « La qualité de service dans les établissements sociaux est-elle l'affaire de tous ? »",
    "En plan dialectique : premièrement, la qualité relève d'une organisation formalisée, avec des procédures, des indicateurs et une direction qui définit les orientations. Deuxièmement, elle engage chaque professionnel : l'accueil, l'écoute, la tenue du dossier et le respect du secret professionnel contribuent directement à la perception du service par l'usager. Troisièmement, la synthèse montre que la démarche qualité associe des outils collectifs et des comportements individuels : elle n'est efficace que si les procédures sont comprises et appropriées par les équipes. La conclusion répond que oui, à condition que la direction donne le cadre et que chaque agent s'approprie sa part de responsabilité.",
    "On attend un plan en trois temps, des exemples issus du secteur et une synthèse qui dépasse l'opposition.")],
C("La dissertation est une réflexion personnelle : le plan sert à rendre l'argumentation lisible et progressive.",
  "Sujet → problématique → plan → exemples analysés → réponse",
  "Dialectique : thèse / antithèse / synthèse · thématique : trois axes complémentaires",
  "Sujet~Question posée~Analyse~Mots clés~Problématique~Axe de réflexion~Plan~Structure choisie",
  "Analyser chaque mot du sujet|Formuler la problématique|Choisir le plan adapté|Rassembler des exemples précis|Rédiger puis vérifier la réponse finale",
  "Reciter le cours sans répondre|Énumérer des exemples sans analyse|Choisir un plan par habitude|Oublier de conclure la question",
  "These~La qualité relève de l'organisation~Antithese~Chaque agent y contribue~Synthese~Outils et pratiques sont lies~Exemple~Un accueil respectueux des droits",
  "Dialectique~Opposition en trois temps~Sujet conflictuel~Synthèse nuancée~Thematique~Axes parallèles~Sujet à explorer~Progression à construire",
  "Exemple~Doit être analysé~Énumération~Reste superficielle"))

# ============================================================ CG4
add("CG4", "La synthèse de documents : contraintes et méthode", "Culture générale et expression", ["BTS2"],
S("La synthèse de documents consiste à restituer l'essentiel de plusieurs textes sur un même sujet dans un document nouveau et structuré."
  "|Les documents sont de natures variées : article, extrait d'ouvrage, graphique, texte réglementaire ou témoignage."
  "|La consigne fixed une longueur, un nombre de parties et parfois un destinataire : elle doit être respectée à la lettre."
  "|La lecture active relève pour chaque document la source, la date, l'auteur, la thèse et les arguments principaux."
  "|Le relevé des idées se fait sur une grille commune, en repérant les convergences et les désaccords entre les documents."
  "|Le plan est thématique : on regroupe les idées par thème et non document par document."
  "|Un titre et un sous-titre annoncent la ligne de conduite du document produit."
  "|L'introduction présente le sujet, le corpus et l'annonce du plan, sans avis personnel."
  "|Les références aux documents (« le document 2 précise que… ») garantissent la traçabilité des informations."
  "|Les chiffres, dates et noms propres sont repris exactement, sans approximation."
  "|Le style est impersonnel : on évite le « je », les jugements de valeur et les développements hors sujet."
  "|Cet exercice prépare la rédaction de notes de synthèse et de comptes rendus dans les établissements sanitaires et sociaux."),
[QC("Quelle est la règle fondamentale d'une synthèse ?", "Résumer chaque document séparément~Regrouper les idées par thème~Ajouter son opinion personnelle~Recopier les documents", 1,
    "La synthèse est thématique : elle croise les documents autour d'idées communes."),
 QC("Que doit-on respecter strictement dans une synthèse ?", "La consigne de longueur et de plan~Le style de l'auteur préféré~L'ordre de lecture des documents~Le nombre de paragraphes de chaque texte", 0,
    "La consigne fixe la longueur, les parties et parfois le destinataire."),
 QC("Quel élément ne doit jamais apparaître dans une synthèse ?", "Une référence au document 3~Une date précise~Un avis personnel non demandé~Un chiffre exact", 2,
    "La synthèse restitue objectivement le corpus sans opinion personnelle."),
 QC("À quoi sert la grille de relevé ?", "À décorer la copie~À comparer les idées des documents~À remplacer l'introduction~À mémoriser le texte", 1,
    "La grille met en regard les apports des documents et repère convergences et divergences."),
 QC("Comment citer un document dans une synthèse ?", "Sans préciser la source~En mentionnant le numéro du document~En inventant une référence~Uniquement en conclusion", 1,
    "La mention du document garantit la traçabilité de l'information."),
 QC("Quel style est attendu ?", "Personnel et expressif~Impersonnel et clair~Ironique~Purement oral", 1,
    "On bannit le « je » et les jugements de valeur."),
 QC("Que fait-on des chiffres relevés ?", "On les arrondit librement~On les reprend exactement~On les supprime~On les remplace par des adjectifs", 1,
    "L'exactitude des chiffres et des dates est une exigence de fidélité."),
 QT("Expliquer pourquoi le plan d'une synthèse doit être thématique et non documentaire.",
    "Un plan documentaire traiterait successivement le document 1, puis le 2, puis le 3 : il donnerait une juxtaposition de résumés et manquerait l'essentiel, qui est la confrontation des points de vue sur un même objet. Le plan thématique regroupe ce que les documents disent sur une même question ; il fait apparaître les accords, les nuances et les contradictions, ce qui produit réellement une synthèse. Il oblige aussi le rédacteur à hiérarchiser les informations et à choisir les idées les plus pertinentes au regard de la consigne.",
    "La réponse doit opposer juxtaposition et confrontation, et montrer que le regroupement thématique crée du sens nouveau."),
 QT("Décrire la méthode complète de préparation d'une synthèse de quatre documents en deux heures.",
    "On lit d'abord la consigne et on note les contraintes (longueur, parties, destinataire). On parcourt rapidement les quatre documents pour identifier le thème commun. On revient ensuite sur chacun en remplissant une grille : source, date, idée directrice, arguments, chiffres. On croise les cases pour dégager trois thèmes et on vérifie que chaque thème est alimenté par au moins deux documents. On formule un titre et un sous-titre, puis on rédige une introduction, trois parties et une conclusion neutre. On réserve les dix dernières minutes à la relecture : respect de la consigne, exactitude des chiffres, présence des références et absence d'avis personnel.",
    "On attend les étapes dans l'ordre avec une gestion du temps explicite et une phase de relecture.")],
C("La synthèse croise plusieurs documents autour de thèmes communs : elle est fidèle, impersonnelle et respecte la consigne.",
  "Corpus → relevé → thèmes → titre → rédaction → relecture",
    "Thématique = par idée · documentaire = par texte (à éviter) · référence = numéro du document",
  "Consigne~Contraintes~Relevé~Idées par document~Theme~Regroupement~Reference~Numéro du document",
  "Lire la consigne et ses contraintes|Relever les idées de chaque document|Croiser pour dégager les thèmes|Formuler titre et sous-titre|Rédiger et relire",
  "Procéder document par document|Ajouter son avis personnel|Arrondir les chiffres|Oublier de relire la consigne",
  "Document 2~Statistique d'attente~Document 3~Témoignage d'usager~Theme commun~Qualité de l'accueil~Conclusion~Bilan sans opinion",
  "Plan thematique~Regroupe par idée~Confronte les sources~Plan documentaire~Un texte après l'autre~Risque de simple résumé",
  "Fidelite~Chiffres et dates exacts~Impersonnel~Absence de je"))

# ============================================================ CG5
add("CG5", "L'expression écrite professionnelle : note, mail et compte rendu", "Culture générale et expression", ["BTS2"],
S("L'expression écrite professionnelle produit des documents destinés à une action précise dans une organisation."
  "|La note de synthèse informe une hiérarchie en quelques paragraphes : objet, faits, analyse et recommandation."
  "|Le courriel professionnel comporte un objet explicite, une formule d'appel, un corps structuré et une signature."
  "|Le compte rendu consigne ce qui s'est dit et ce qui a été décidé, avec les responsables et les échéances."
  "|Chaque document s'écrit pour un destinataire identifié dont on adapte le niveau de détail et le ton."
  "|La structure de l'information suit l'ordre : contexte, information principale, conséquence, action à engager."
  "|Les phrases courtes et les paragraphes aérés facilitent la lecture sur écran."
  "|Les faits sont distingués des interprétations : on écrit « il a été constaté » plutôt qu'une affirmation non vérifiée."
  "|Les données personnelles sont traitées avec discrétion, conformément au secret professionnel et au RGPD."
  "|L'orthographe et la ponctuation contribuent à la crédibilité de l'écrit professionnel."
  "|Une relecture finale vérifie le destinataire, la pièce jointe, la date et l'absence de brouillon."
  "|Ces écrits sont quotidiennels dans les services sanitaires et sociaux : transmission, signalement, compte rendu de réunion."),
[QC("Quel document informe une hiérarchie en proposant une recommandation ?", "Un compte rendu~Une note de synthèse~Un agenda~Une facture", 1,
    "La note de synthèse va de l'information à la proposition d'action."),
 QC("Que doit contenir l'objet d'un courriel professionnel ?", "Une formule de politesse~Un indication précise du sujet~La signature~La date de naissance du destinataire", 1,
    "L'objet annonce immédiatement le sujet du message."),
 QC("Quelle information est indispensable dans un compte rendu de réunion ?", "L'avis de chaque participant~Les décisions, responsables et échéances~Le menu de la réunion~La couleur des diapositives", 1,
    "Un compte rendu opérationnel consigne décisions, responsabilités et dates."),
 QC("Comment distinguer un fait d'une interprétation ?", "En utilisant des adjectifs~En formulant « il a été constaté que » et en citant la source~En supprimant les dates~En écrivant au présent", 1,
    "La formulation factuelle et la source permettent de distinguer observation et avis."),
 QC("Quel réflexe s'impose avant l'envoi d'un courriel ?", "Ajouter une pièce jointe au hasard~Relire destinataire, pièce jointe et absence de brouillon~Changer la police~Raccourcir la signature", 1,
    "La relecture finale évite les erreurs de destinataire et les oublis de pièce jointe."),
 QC("Quelle contrainte s'applique aux données personnelles dans un écrit professionnel ?", "Les publier largement~Les traiter avec discrétion selon le secret professionnel et le RGPD~Les supprimer systématiquement~Les anonymiser sans need", 1,
    "Secret professionnel et RGPD encadrent la circulation des données de santé."),
 QC("Quel style est attendu dans une note professionnelle ?", "Littéraire et imagé~Clair, structuré et impersonnel~Ironique~Très long", 1,
    "La clarté et la structure priment sur l'effet littéraire."),
 QT("Rédiger le plan d'une note de synthèse signalant une augmentation des plaintes d'usagers sur l'accueil.",
    "La note s'ouvre sur un objet précis (« Plaintes liées à l'accueil : constat et pistes d'action ») et une phrase de contexte indiquant la période et le service concerné. Une première partie présente les faits : nombre de plaintes, motifs récurrents (attente, absence d'information), sources (registre, fiches de réclamation). Une deuxième partie propose une analyse : ces motifs signalent un écart entre les procédures affichées et les pratiques, et un besoin de clarification des rôles à l'accueil. Une troisième partie formule deux recommandations : afficher les temps d'attente estimés et organiser un temps d'échange hebdomadaire entre accueil et service social. La note se termine par la proposition d'un point de suivi dans un mois.",
    "On attend objet, contexte, faits, analyse, recommandations et une échéance de suivi."),
 QT("Expliquer les différences entre un compte rendu et un procès-verbal et dire quand les utiliser.",
    "Le compte rendu restitue l'essentiel des échanges et surtout les décisions prises, les responsabilités et les échéances ; il est rédigé sous forme synthétique et peut interpréter le sens des discussions. Le procès-verbal suit une forme plus solennelle et souvent plus fidèle à l'ordre des interventions : il constate la tenue de la séance, les présents, les délibérations et les votes, notamment dans les instances officielles. Dans un établissement social, on utilise le compte rendu pour une réunion de service ou de coordination, parce que l'objectif est de faire avancer les actions. Le procès-verbal est réservé aux conseils d'administration, commissions ou assemblées où la trace formelle des décisions est exigée.",
    "La réponse doit opposer synthèse opérationnelle et trace officielle et donner un exemple d'usage pour chacun.")],
C("Un écrit professionnel est un outil d'action : il informe, trace une décision ou déclenche une tâche.",
  "Destinataire + objet + faits + analyse + action",
  "Note : information et recommandation · mail : objet et signature · compte rendu : décisions et échéances",
  "Note~Information et recommandation~Courriel~Objet et signature~Compte rendu~Décisions et échéances",
  "Identifier le destinataire et l'objectif|Rassembler les faits vérifiés|Structurer en trois parties|Rédiger avec des phrases courtes|Relire avant envoi",
  "Confondre fait et interprétation|Oublier le destinataire|Envoyer un brouillon|Diffuser des données personnelles",
  "Plaintes~Nombre et motifs~Analyse~Écart entre procédure et pratique~Action~Afficher les temps d'attente~Suivi~Point dans un mois",
  "Compte rendu~Synthèse opérationnelle~Décisions et actions~Procès-verbal~Trace officielle~Présents et délibérations",
  "Fait~Constat vérifiable~Avis~Interprétation personnelle"))

# ============================================================ CG6
add("CG6", "L'oral professionnel : exposé, entretien et prise de parole", "Culture générale et expression", ["BTS1"],
S("L'oral professionnel mobilise la voix, le corps et le contenu pour transmettre un message en situation réelle."
  "|Un exposé se prépare avec un plan clair : introduction, deux ou trois parties, conclusion."
  "|Les notes doivent être courtes : on prépare des mots clés plutôt qu'un texte lu intégralement."
  "|La voix est posée, le débit adapté et les silences marquent les temps forts."
  "|Le regard circule entre les interlocuteurs et la posture reste ouverte, sans gestes parasites."
  "|L'entretien de recrutement ou de stage suit une logique de questions : on prépare des exemples concrets."
  "|La méthode STAR (Situation, Tâche, Action, Résultat) structure une réponse à une question comportementale."
  "|Un oral de présentation de projet comporte une durée impartie, un support sobre et un temps de questions."
  "|L'écoute des questions de jury fait partie de la note : on reformule avant de répondre si nécessaire."
  "|Le stress se gère par la respiration, la préparation et la répétition à voix haute."
  "|Les technologies (micro, visioconférence, diaporama) doivent être testées avant la prestation."
  "|En BTS SP3S, l'oral intervient en U1 et dans la soutenance du projet tutoré, mais aussi dans les entretiens avec les usagers."),
[QC("Que doit-on préparer pour un exposé ?", "Un texte intégral à lire~Des mots clés et un plan clair~Une liste de blagues~Un diaporama de cent diapositives", 1,
    "Des notes courtes et un plan favorisent une vraie prise de parole."),
 QC("Que signifie la lettre A dans la méthode STAR ?", "Avis~Action~Attente~Annonce", 1,
    "STAR : Situation, Tâche, Action, Résultat."),
 QC("Quel geste accompagne une bonne prise de parole ?", "Regarder ses notes en permanence~Faire circuler le regard~Se voûter~Parler très vite", 1,
    "Le regard circule pour impliquer l'auditoire."),
 QC("Comment gérer le temps pendant un oral de projet ?", "Dépasser largement la durée~Respecter la durée et prévoir la conclusion~Lire chaque diapositive~Ignorer le chronomètre", 1,
    "Le respect de la durée fait partie de l'évaluation."),
 QC("Que faire si une question du jury semble ambiguë ?", "Répondre au hasard~Reformuler la question avant d'y répondre~Refuser de répondre~Changer de sujet", 1,
    "La reformulation sécurise la compréhension et montre l'écoute."),
 QC("Quel moyen permet de réduire le stress avant un oral ?", "Ne jamais répéter~Répéter à voix haute et respirer calmement~Parler très vite~Supprimer la conclusion", 1,
    "La répétition et la respiration sont des leviers simples et efficaces."),
 QC("Quel point technique vérifier avant une visioconférence ?", "La couleur du fond d'écran~Le micro, la caméra et le partage d'écran~Le nombre de fenêtres ouvertes~La taille de la police du navigateur", 1,
    "Tester le matériel évite les incidents pendant la prestation."),
 QT("Expliquer l'intérêt de la méthode STAR pour répondre à une question d'entretien.",
    "La méthode STAR impose quatre temps : la situation est décrite brièvement pour situer le contexte, la tâche précise ce qui était attendu, l'action détaille ce que le candidat a réellement fait, et le résultat mesure l'effet obtenu. Elle évite les réponses générales du type « je suis organisé » en obligeant à apporter une preuve concrète et personnelle. Elle permet aussi de valoriser une réussite collective en précisant sa propre contribution. Dans un entretien pour un stage en établissement social, elle peut servir à raconter la gestion d'une réclamation d'usager, du accueil initial au retour positif, chiffres à l'appui si possible.",
    "On doit citer les quatre étapes et montrer que la méthode transforme une affirmation en preuve."),
 QT("Décrire les étapes de préparation d'un oral de présentation de projet de dix minutes.",
    "On clarifie d'abord l'objectif de la présentation et le public attendu. On construit un plan en trois temps : le contexte et le besoin, la démarche et les résultats, les perspectives. On prépare un support sobre avec une idée par diapositive et des visuels lisibles. On rédige des notes courtes, puis on répète à voix haute en chronométrant, en ajustant le débit pour respecter les dix minutes. On anticipe les questions du jury en préparant trois ou quatre réponses appuyées sur des chiffres. Le jour même, on teste le matériel, on arrive en avance et on commence par une phrase d'introduction qui annonce le plan.",
    "La réponse attendue suit l'ordre : objectif, plan, support, répétition chronométrée, questions, test matériel.")],
C("Réussir un oral, c'est préparer le fond, la forme et le matériel, puis gérer le temps et l'écoute.",
  "Fond + forme + matériel + chronomètre = prestation crédible",
  "STAR : Situation, Tâche, Action, Résultat · débit, regard, silences",
  "Exposé~Plan annoncé~Entretien~Exemples concrets~Notes~Mots clés~Jury~Questions et écoute",
  "Définir l'objectif de la prise de parole|Construire un plan en trois temps|Préparer des notes courtes|Répéter à voix haute en chronométrant|Tester le matériel et gérer les questions",
  "Lire intégralement ses notes|Dépasser le temps imparti|Ignorer les questions|Négliger la vérification du micro",
  "Situation~Une réclamation à l'accueil~Tâche~Répondre dans les délais~Action~Écoute et réorientation~Résultat~Usager satisfait",
  "Oral~Échange immédiat avec le public~Écrit~Trace durable et relisible",
  "Stress~Respiration et répétition~Improvisation~Risque de dispersion"))

# ============================================================ CG7
add("CG7", "Analyser une situation de communication professionnelle", "Culture générale et expression", ["BTS2"],
S("Analyser une situation de communication consiste à identifier les acteurs, les messages, les canaux et les obstacles."
  "|La communication professionnelle est toujours située : elle dépend du service, du public et du cadre réglementaire."
  "|Le modèle de Shannon schématise la chaîne : émetteur, message, canal, récepteur, avec du bruit possible."
  "|Le bruit désigne tout ce qui perturbe la réception : jargon, mauvaise acoustique, émotion ou surcharge d'information."
  "|Une information peut être déformée à chaque transmission : on parle de perte ou de distorsion du message."
  "|La boucle de rétroaction (feedback) permet de vérifier que le message a été compris comme prévu."
  "|La reformulation est l'outil le plus simple de cette vérification dans un entretien d'accueil."
  "|Les codes sociaux et culturels influencent l'interprétation : un même geste peut avoir des sens différents."
  "|La posture professionnelle combine écoute, neutralité et respect de la dignité de la personne."
  "|Le secret professionnel et le RGPD limitent ce qui peut être dit, à qui et par quel canal."
  "|Un désaccord relève souvent d'un problème de représentation plus que d'une mauvaise volonté."
  "|Dans les établissements sanitaires et sociaux, la qualité de la communication conditionne l'accès aux droits."),
[QC("Quels éléments composent la chaîne de communication de Shannon ?", "Émetteur, message, canal, récepteur~Direction, durée, coût, lieu~Texte, image, son, couleur~Recette, produit, marge, stock", 0,
    "Le modèle décrit émetteur, message, canal et récepteur, avec du bruit éventuel."),
 QC("Qu'appelle-t-on bruit dans ce modèle ?", "Un son très fort uniquement~Tout ce qui perturbe la réception du message~Une panne de courant~Un désaccord contractuel", 1,
    "Le bruit recouvre toute perturbation : jargon, émotion, mauvaise acoustique."),
 QC("À quoi sert la boucle de rétroaction ?", "À vérifier la compréhension du message~À augmenter le volume~À supprimer le destinataire~À allonger le message", 0,
    "Le feedback permet de contrôler que le message reçu correspond au message envoyé."),
 QC("Quel outil permet de vérifier la compréhension dans un entretien ?", "La reformulation~Le monologue~Le silence prolongé~La contradiction", 0,
    "Reformuler avec ses propres mots confirme ou corrige la compréhension."),
 QC("Quelle limite s'impose à la communication professionnelle dans le secteur social ?", "Le secret professionnel et le RGPD~L'absence de consigne~Le libre choix du canal~L'interdiction d'écrire", 0,
    "Secret professionnel et RGPD encadrent la circulation des informations."),
 QC("Quel facteur peut modifier l'interprétation d'un même geste ?", "Les codes sociaux et culturels~La couleur du bureau~L'heure de la journée~Le type de papier", 0,
    "Les repères culturels changent le sens attribué aux signes."),
 QC("Quelle est une conséquence de la perte d'information lors des transmissions ?", "Une meilleure décision~Une décision fondée sur des données incomplètes~Une réduction des délais~Une augmentation du budget", 1,
    "Une information déformée conduit à des décisions inadaptées."),
 QT("Analyser un incident de communication : un usager quitte l'accueil en croyant que sa demande sera traitée sous 48 heures, alors que le service a annoncé huit jours. Proposer l'analyse et la correction.",
    "L'émetteur a bien transmis un délai, mais le récepteur a reçu une autre information : il y a eu distorsion du message. Les causes possibles sont un débit trop rapide, l'absence de reformulation, un jargon administratif ou une surcharge d'information au moment de l'annonce. Le bruit ici n'est pas sonore mais cognitif. La correction consiste à répéter le délai de façon explicite, à le faire écrire sur un support remis à l'usager, à demander une reformulation (« pouvez-vous me dire ce que vous avez retenu ? ») et à vérifier que le service dispose bien du dossier complet. On trace ensuite l'incident dans le registre de réclamation pour alimenter la démarche qualité.",
    "On doit mobiliser émetteur, bruit, distorsion, feedback et proposer une correction concrète et tracée."),
 QT("Expliquer comment déterminer le canal de communication adapté dans une structure sanitaire ou sociale.",
    "Le choix du canal dépend de trois critères : la nature de l'information, l'urgence et le caractère confidentiel des données. Une information urgente et simple circule par téléphone ou messagerie interne, avec une confirmation écrite courte. Une décision collective ou un changement de procédure doit être formalisé par un écrit consultable par tous les agents concernés, complété par une réunion pour expliquer le sens du changement. Une donnée de santé ou un dossier d'usager ne peut être transmis que par un canal sécurisé et uniquement aux personnes habilitées. Enfin, le canal doit être accessible au destinataire : un usager en situation de handicap peut avoir besoin d'un support adapté ou d'un accompagnement humain.",
    "La réponse croise nature de l'information, urgence, confidentialité et accessibilité du destinataire.")],
C("Toute communication professionnelle peut être analysée comme une chaîne où un bruit peut déformer le message.",
  "Émetteur → message → canal → récepteur + feedback",
  "Reformulation = vérification · bruit = perturbation · secret = limite",
  "Émetteur~Personne qui envoie~Message~Contenu transmis~Canal~Support utilisé~Récepteur~Personne qui reçoit",
  "Identifier les acteurs et le contexte|Déterminer le message et le canal|Repérer les sources de bruit|Vérifier par reformulation|Tracer l'incident et corriger",
  "Croire que l'envoi garantit la réception|Négliger le feedback|Utiliser un jargon inutile|Diffuser une donnée sur un canal non sécurisé",
  "Incident~Délai mal compris~Bruit~Surcharge d'information~Correction~Reformulation et écrit~Trace~Registre des réclamations",
  "Feedback~Vérifie la compréhension~Bruit~Perturbe la réception",
  "Canal sécurisé~Données confidentielles~Canal ordinaire~Information générale"))

# ============================================================ COM1
add("COM1", "Communication verbale et non verbale : codes et cohérence", "Communication", ["BTS1"],
S("La communication verbale utilise des mots ; la communication non verbale passe par le regard, la posture, les gestes, la voix et l'espace."
  "|Selon les travaux de Mehrabian, dans un message émotionnel, le sens est porté en grande partie par le non verbal et le ton."
  "|Cette proportion ne s'applique pas à tous les messages : elle rappelle surtout que le fond et la forme doivent être cohérents."
  "|Les gestes accompagnent la parole : ils peuvent renforcer le message ou le contredire."
  "|La distance physique est un code : trop proche, elle devient intrusive ; trop lointaine, elle signale le retrait."
  "|Le regard participe à la relation : regarder ses notes en permanence coupe l'échange avec la personne."
  "|La voix porte des informations sur l'émotion et l'assurance : débit, volume, timbre et silences comptent."
  "|L'apparence et le cadre matériel constituent aussi des signaux : un bureau en désordre peut suggérer un manque de rigueur."
  "|Un décalage entre paroles et attitude est perçu comme une incohérence et réduit la confiance."
  "|Les codes varient selon les cultures et les situations : il faut observer avant d'interpréter un geste."
  "|Dans l'accueil d'un usager, la cohérence des signaux est plus importante que la maîtrise d'une technique."
  "|Le référentiel BTS SP3S attend des techniques de communication adaptées au public et au handicap."),
[QC("Quel canal utilise le regard dans une communication ?", "Le canal verbal~Le canal non verbal~Le canal écrit~Le canal réglementaire", 1,
    "Le regard, la posture et les gestes relèvent de la communication non verbale."),
 QC("Que signalent des paroles rassurantes assorties d'une posture fermée ?", "Une parfaite cohérence~Une incohérence qui nuit à la confiance~Une maîtrise technique~Une absence de message", 1,
    "Le décalage entre verbal et non verbal est perçu comme une incohérence."),
 QC("Quel élément relève de la voix plutôt que du geste ?", "La posture~Le débit~La distance~Le regard", 1,
    "Débit, volume et timbre sont des paramètres vocaux."),
 QC("Quelle interprétation faut-il éviter face à un geste dont on ignore le code culturel ?", "L'expliquer immédiatement~Conclure hâtivement à une intention~Le noter comme une faute~Changer de sujet", 1,
    "Il faut observer et demander plutôt que d'interpréter un code inconnu."),
 QC("Quel effet a une distance trop proche dans un entretien d'accueil ?", "Elle rassure toujours~Elle peut être vécue comme intrusive~Elle améliore l'audition~Elle n'a aucun effet", 1,
    "La proxémie varie selon les personnes : trop près, l'espace intime est envahi."),
 QC("Que mesure l'étude de Mehrabian mentionnée en cours ?", "La vitesse de lecture~La part du non verbal et du ton dans un message émotionnel~Le coût d'un entretien~La durée d'une réunion", 1,
    "Elle porte sur la communication émotionnelle, pas sur tous les messages."),
 QC("Quel réflexe professionnel s'impose avant d'interpréter une attitude ?", "Se fier à sa première impression~Observer le contexte et vérifier avec la personne~Répondre par une remarque~Noter un jugement dans le dossier", 1,
    "L'observation contextuelle et la vérification évitent les conclusions hâtives."),
 QT("Expliquer pourquoi la cohérence entre verbal et non verbal est décisive dans un entretien d'accueil.",
    "Une personne qui entend « je vous écoute » mais voit un agent regarder sa montre et garder les bras croisés retient le signal le plus fort : celui de l'impatience ou de la fermeture. Le message verbal est alors discrédité, et la confiance, qui est la condition de l'accès aux droits, s'installe difficilement. La cohérence ne consiste pas à sourire en permanence, mais à aligner posture ouverte, regard disponible, débit calme et paroles claires. Quand un désaccord subsiste, il vaut mieux le nommer avec tact (« je regarde l'heure parce que nous avons rendez-vous dans dix minutes ») que laisser l'autre l'imaginer.",
    "On explique le mécanisme de discrédit du message, puis on donne une conduite professionnelle concrète."),
 QT("Analyser une situation : un usager dit « ça va » en détournant le regard et en serrant ses papiers. Que faire ?",
    "Les signaux sont discordants : le verbal dit que tout va bien, le non verbal exprime une gêne ou une inquiétude. Plutôt que de prendre le « ça va » pour argent comptant, on marque une pause, on garde une posture ouverte et on propose une reformulation ouverte : « Vous dites que ça va, mais j'ai l'impression que quelque chose vous tracasse ; ai-je bien compris ? » On laisse un silence, on écoute sans interrompre et on propose, si la personne le souhaite, un entretien plus au calme. On note ensuite dans le dossier seulement ce qui a été vérifié, pas une hypothèse d'état émotionnel.",
    "La réponse doit détecter la discordance, proposer une vérification bienveillante et distinguer observation et interprétation.")],
C("Le non verbal ne remplace pas les mots : il doit confirmer le message et respecter la distance de l'autre.",
  "Message reçu = mots + ton + posture + contexte",
  "Cohérence = paroles et attitude alignées · proxémie = distance · regard = disponibilité",
  "Verbal~Mots employés~Ton~Voix et débit~Posture~Corps et gestes~Distance~Espace respecté",
  "Observer le contexte|Repérer les signaux|Vérifier la cohérence|Reformuler pour confirmer|Adapter sa posture",
  "Interpréter un geste sans demande|Regarder ses notes en permanence|Imposer une distance|Confondre calme et indifférence",
  "Usager~Dit que ça va~Regard~Détourné~Reformulation~Vérification respectueuse~Trace~Fait vérifié seulement",
  "Verbal~Contenu explicite~Non verbal~Signal relationnel",
  "Cohérence~Renforce la confiance~Discordance~Détruit la crédibilité"))

# ============================================================ COM2
add("COM2", "L'entretien d'accueil : étapes et techniques professionnelles", "Communication", ["BTS1"],
S("L'entretien d'accueil est un temps de relation au cours duquel un professionnel reçoit une personne, écoute sa demande et l'oriente."
  "|Il s'inscrit dans le bloc 1 du référentiel BTS SP3S : accueil et accompagnement de la personne dans son parcours."
  "|La préparation consiste à connaître les prestations de la structure, les circuits d'orientation et les documents utiles."
  "|L'accueil physique commence par une présentation du professionnel et le respect de la dignité de la personne."
  "|La phase d'écoute laisse la personne exposer sa demande dans ses propres mots, sans interruption prématurée."
  "|Les questions ouvertes (« qu'est-ce qui vous amène ? ») favorisent l'expression ; les questions fermées vérifient un point précis."
  "|La reformulation et la synthèse intermédiaire confirment la compréhension de la demande."
  "|La distinction entre la demande exprimée et le besoin sous-jacent est essentielle pour orienter correctement."
  "|L'information donnée est claire, hiérarchisée et vérifiée : on évite de promettre ce qui ne dépend pas du service."
  "|L'orientation vers un autre service ou un partenaire s'accompagne d'une explication et d'une trace écrite."
  "|La fin d'entretien vérifie la compréhension de la personne et les suites prévues, avec leur délai."
  "|Le respect du secret professionnel et la discrétion des locaux accompagnent l'ensemble de l'entretien."),
[QC("Quelle question favorise l'expression libre de la demande ?", "Une question fermée~Une question ouverte~Une question suggestive~Une affirmation", 1,
    "La question ouverte invite la personne à s'exprimer dans ses mots."),
 QC("Quelle distinction est essentielle pour orienter une personne ?", "Demande exprimée et besoin sous-jacent~Nom et prénom~Heure d'arrivée et de départ~Couleur du dossier", 0,
    "La demande formulée ne révèle pas toujours le besoin réel."),
 QC("Quel réflexe sécurise la compréhension pendant l'entretien ?", "Répondre avant d'écouter~Reformuler régulièrement~Changer de sujet~Prendre des notes sans regarder", 1,
    "La reformulation permet de vérifier ce qui a été compris."),
 QC("Que faut-il éviter dans l'information donnée à un usager ?", "Une phrase claire~Une hiérarchie des étapes~Une promesse qui ne dépend pas du service~Une vérification de la source", 2,
    "Promettre un résultat hors de son pouvoir nuit à la confiance."),
 QC("Comment se termine un entretien d'accueil ?", "Par un silence sans consigne~Par une vérification de la compréhension et des suites~Par une question indiscrète~Par le renvoi vers un autre guichet sans explication", 1,
    "On confirme les suites, les responsables et les délais."),
 QC("Quelle contrainte s'applique aux propos entendus ?", "Ils peuvent être répétés à tous~Ils sont couverts par le secret professionnel~Ils doivent être publiés~Ils sont sans importance", 1,
    "Le secret professionnel s'impose aux professionnels du secteur."),
 QC("À quel bloc du référentiel BTS SP3S se rattache l'entretien d'accueil ?", "Bloc 1~Bloc 2~Bloc 3~Bloc 4", 0,
    "Le bloc 1 concerne l'accompagnement et la coordination du parcours de la personne."),
 QT("Décrire les cinq temps d'un entretien d'accueil réussi et préciser l'objectif de chacun.",
    "Le premier temps est la préparation : connaître les prestations, le circuit et les documents pour ne pas donner une information approximative. Le deuxième temps est l'ouverture : se présenter, installer un cadre confidentiel et inviter la personne à parler. Le troisième temps est l'écoute active : laisser exposer la demande, poser des questions ouvertes, reformuler et distinguer demande et besoin. Le quatrième temps est la réponse : expliquer ce qui est possible, ce qui ne l'est pas, et les étapes à venir avec leurs délais. Le cinquième temps est la clôture : vérifier la compréhension, tracer l'entretien dans le dossier ou le registre et orienter si nécessaire avec un contact précis.",
    "On attend les cinq temps dans l'ordre avec un objectif explicite pour chacun et une mention de la traçabilité."),
 QT("Un usager demande une aide financière alors que sa situation relève d'un dispositif d'insertion. Comment conduire l'entretien ?",
    "On commence par écouter sans corriger la demande : la personne formule souvent une attente en termes d'argent alors qu'elle a besoin d'un accompagnement plus large. On reformule : « Si je comprends bien, vous avez besoin de retrouver des ressources rapidement ; est-ce bien cela ? » On pose ensuite des questions ouvertes sur sa situation, son projet et les démarches déjà engagées. On explique ensuite la distinction entre l'aide financière, qui relève d'un autre dispositif, et l'accompagnement à l'insertion proposé par la structure, en présentant les deux circuits sans laisser croire à une promesse. On oriente vers le bon interlocuteur avec un nom, un lieu et une date, puis on trace l'entretien.",
    "La réponse montre le passage de la demande au besoin, la clarification des dispositifs et une orientation concrète.")],
C("L'entretien d'accueil transforme une demande exprimée en besoin identifié, puis en orientation vérifiée.",
  "Préparer · écouter · reformuler · répondre · tracer",
  "Question ouverte = exploration · question fermée = vérification · reformulation = sécurité",
  "Accueil~Ouverture de l'échange~Écoute~Expression de la demande~Reformulation~Vérification~Orientation~Suite donnée",
  "Préparer les informations et les circuits|Se présenter et installer le cadre|Écouter avec des questions ouvertes|Reformuler et clarifier le besoin|Expliquer, orienter et tracer",
  "Interrompre la personne|Promettre un résultat|Confondre demande et besoin|Oublier la trace écrite",
  "Demande~Une aide financière~Besoin~Retrouver des ressources~Réponse~Deux circuits expliqués~Orientation~Interlocuteur et date",
  "Question ouverte~Explore la demande~Question fermée~Vérifie un fait précis",
  "Demande~Ce qui est dit~Besoin~Ce qui est compris"))

# ============================================================ COM3
add("COM3", "Écoute active et reformulation dans la relation d'aide", "Communication", ["BTS1"],
S("L'écoute active est une attitude volontaire qui vise à comprendre le message de l'autre avant d'y répondre."
  "|Elle mobilise l'attention, la patience et la suspension du jugement."
  "|Écouter ne signifie pas approuver : on peut comprendre une position sans la partager."
  "|Les signes d'écoute sont le regard, les hochements de tête, les silences et les notes brèves."
  "|La reformulation consiste à redire avec ses propres mots ce que l'interlocuteur a exprimé."
  "|La reformulation peut être littérale, par paraphrase, ou faire émerger le sentiment sous-jacent."
  "|Elle se formule sur un ton interrogatif pour laisser l'autre corriger : « Ai-je bien compris que… ? »"
  "|La synthèse regroupe plusieurs éléments épars en un point d'étape, utile dans un entretien long."
  "|Les questions ouvertes relancent l'expression ; les questions fermées vérifient un fait ou une décision."
  "|Le silence est un outil : il donne le temps de la réflexion et évite de combler l'espace par des conseils hâtifs."
  "|Les émotions exprimées sont accueillies sans être jugées ni minimisées."
  "|Dans le secteur social, l'écoute active est une technique professionnelle évaluée par les indicateurs de réussite du bloc 1."),
[QC("Quelle est la première condition de l'écoute active ?", "Répondre immédiatement~Suspendre son jugement pour comprendre~Préparer sa réplique~Prendre beaucoup de notes", 1,
    "Comprendre avant de répondre suppose de suspendre son jugement."),
 QC("Comment formuler une reformulation ?", "En répétant mot pour mot sans respiration~Avec ses propres mots et un ton interrogatif~En donnant son avis~En coupant la parole", 1,
    "La paraphrase avec vérification laisse l'autre corriger la compréhension."),
 QC("Quel rôle joue le silence dans l'entretien ?", "Il marque un désaccord~Il laisse le temps de la réflexion~Il remplace l'écoute~Il doit toujours être évité", 1,
    "Le silence est un espace de pensée et d'expression pour la personne."),
 QC("Quelle question vérifie un fait précis ?", "Une question ouverte~Une question fermée~Une question rhétorique~Une question implicite", 1,
    "La question fermée attend une confirmation courte."),
 QC("Faut-il approuver la personne pour montrer qu'on l'écoute ?", "Oui, toujours~Non, compréhension et approbation sont distinctes~Oui, pour éviter le conflit~Non, il faut la contredire", 1,
    "On peut comprendre sans adhérer : la neutralité professionnelle s'impose."),
 QC("Que faire face à une émotion exprimée ?", "La minimiser~L'accueillir sans jugement~La corriger immédiatement~Changer de sujet", 1,
    "L'accueil de l'émotion ne vaut pas approbation de tous les propos."),
 QC("Quelle est la fonction d'une synthèse en cours d'entretien ?", "Clore l'entretien~Regrouper les éléments en point d'étape~Imposer une décision~Remplacer les notes", 1,
    "La synthèse fait le point sur ce qui a été compris avant de poursuivre."),
 QT("Distinguer reformulation, synthèse et interprétation, et donner un exemple de chacune dans un entretien d'accueil.",
    "La reformulation redit brièvement le dernier propos avec d'autres mots : « Vous me dites que vous avez attendu trois semaines sans nouvelle, c'est bien cela ? » La synthèse regroupe plusieurs éléments déjà énoncés : « Nous avons vu ensemble votre situation, le dossier transmis et la réponse attendue ; je fais le point avant de continuer. » L'interprétation va au-delà de ce qui a été dit en supposant un sentiment ou une cause : « Vous êtes sûrement en colère contre le service. » Elle doit rester prudente et proposée comme hypothèse, car elle peut être fausse et blesser. La règle professionnelle est de privilégier reformulation et synthèse, et de ne formuler une hypothèse que pour la soumettre à la personne.",
    "On distingue les trois notions et on donne un exemple pour chacune, avec une règle de prudence."),
 QT("Comment adapter son écoute face à une personne qui parle beaucoup et digresse ?",
    "On ne coupe pas brutalement la parole : on laisse d'abord un espace d'expression, car la digression révèle souvent l'inquiétude réelle. On utilise ensuite une synthèse pour regrouper ce qui a été dit et on propose un recentrage explicite : « Je note plusieurs points importants ; si vous êtes d'accord, reprenons d'abord le dossier déposé la semaine dernière. » Les questions fermées aident à vérifier les faits, les questions ouvertes à préciser le besoin. On garde une posture ouverte et un débit calme, et on confirme à la fin que l'essentiel a été entendu. Si l'entretien est trop long, on propose une suite plutôt que d'imposer une fin brutale.",
    "On attend une technique de recentrage respectueuse, des synthèses intermédiaires et le maintien de la relation.")],
C("L'écoute active comprend avant de répondre : elle reformule, synthétise et laisse un espace à l'autre.",
  "Écoute + reformulation + silence = compréhension vérifiée",
  "Reformulation = paraphrase interrogative · synthèse = point d'étape · silence = temps de pensée",
  "Écoute~Attention suspendue~Reformulation~Paraphrase vérifiée~Synthèse~Point d'étape~Silence~Temps laissé",
  "Se disposer à écouter sans juger|Laisser parler et observer|Paraphraser avec vérification|Synthétiser les points entendus|Recentres et confirmer la suite",
  "Préparer sa réponse pendant qu'on parle|Minimiser une émotion|Interpréter sans vérifier|Remplir le silence à tout prix",
  "Reformulation~Ai-je bien compris~Synthèse~Trois points regroupés~Hypothèse~À soumettre à la personne~Écoute~Dignité respectée",
  "Reformulation~Redit le propos~Interprétation~Suppose au-delà du dit",
  "Question ouverte~Laisse explorer~Question fermée~Confirme un fait"))

# ============================================================ COM4
add("COM4", "Communication non violente et prévention des conflits", "Communication", ["BTS2"],
S("La communication non violente (CNV) est une méthode de relation qui vise à exprimer un besoin sans accuser l'autre."
  "|Elle a été popularisée par Marshall Rosenberg et s'appuie sur quatre étapes : observation, sentiment, besoin, demande."
  "|L'observation décrit un fait vérifiable, sans adjectif moralisateur : « le dossier a été déposé après l'heure »."
  "|Le sentiment nomme ce que l'agent ressent, sans rejeter la faute sur la personne : « je suis inquiet »."
  "|Le besoin rend explicite l'attente professionnelle : « j'ai besoin de disposer des pièces avant l'instruction »."
  "|La demande est précise, réalisable et négociable : « pouvez-vous me transmettre les pièces avant vendredi ? »"
  "|La CNV se distingue de la simple politesse : elle rend le besoin lisible au lieu de le sous-entendre."
  "|Dans un service social, elle sert autant avec les usagers qu'avec les collègues."
  "|Un conflit naît souvent d'un besoin non exprimé ou d'une interprétation erronée du comportement de l'autre."
  "|La prévention repose sur la clarification des rôles, la transmission écrite des décisions et le respect des délais."
  "|En cas de désaccord, on cherche d'abord les faits, puis les besoins, avant de discuter des solutions."
  "|La médiation interne peut faire appel à un tiers lorsque la relation est trop tendue pour être traitée directement."),
[QC("Combien d'étapes comporte le modèle CNV de Rosenberg ?", "Deux~Trois~Quatre~Six", 2,
    "Observation, sentiment, besoin, demande : quatre étapes."),
 QC("Quelle formulation relève d'une observation non violente ?", "Vous êtes toujours en retard~Le dossier a été déposé après l'heure~Vous ne faites jamais attention~C'est votre faute", 1,
    "L'observation décrit un fait daté, sans jugement de valeur."),
 QC("Quel rôle joue l'expression du besoin ?", "Accuser l'autre~Rendre l'attente explicite~Terminer l'échange~Éviter toute demande", 1,
    "Nommer le besoin permet de sortir de l'accusation."),
 QC("Quelle demande est conforme à la CNV ?", "Faites mieux la prochaine fois~Pouvez-vous transmettre les pièces avant vendredi ?~Il faut que vous changiez~Vous devriez avoir honte", 1,
    "La demande est précise, réalisable et négociable."),
 QC("Quelle est une cause fréquente de conflit dans un service ?", "Un besoin non exprimé ou mal compris~Un excès de clarté~Une consigne écrite~Un désaccord jamais évoqué mais supposé", 0,
    "Le besoin tacite et l'interprétation erronée alimentent le conflit."),
 QC("Que faut-il rechercher en premier dans un désaccord ?", "Les responsables~Les faits vérifiables~Les sanctions~Les opinions des tiers", 1,
    "On s'appuie d'abord sur les faits avant les interprétations."),
 QC("Quand recourir à la médiation interne ?", "Dès le premier mot~Quand la relation est trop tendue pour un échange direct~Jamais~Pour les seuls usagers", 1,
    "Un tiers aide à restaurer un dialogue devenu impossible."),
 QT("Appliquer les quatre étapes de la CNV à un retard répété de transmission de dossiers entre deux services.",
    "Observation : « Les trois derniers dossiers transmis par le service d'accueil sont arrivés après midi alors que l'instruction commence à 11 heures. » Sentiment : « Cela m'inquiète parce que nous devons demander des pièces complémentaires en fin de journée. » Besoin : « J'ai besoin de recevoir les dossiers avant 11 heures pour traiter les demandes dans le délai annoncé à l'usager. » Demande : « Pouvez-vous me confirmer ce que vous pouvez changer d'ici la semaine prochaine ? » On écoute ensuite la réponse de l'autre service, car le retard peut venir d'une surcharge ou d'un circuit mal défini. La solution est construite ensemble et formalisée par écrit.",
    "On doit retrouver les quatre étapes dans l'ordre, avec un fait vérifiable et une demande négociable."),
 QT("Expliquer la différence entre prévention et gestion d'un conflit et donner deux actions de prévention dans une équipe.",
    "La prévention agit avant le conflit : elle réduit les causes en clarifiant les rôles, en écrivant les procédures de transmission, en respectant les délais et en organisant des temps d'échange réguliers. La gestion intervient quand le désaccord existe : elle vise à restaurer la communication, à identifier les besoins et à construire un accord, avec recours à un tiers si nécessaire. Deux actions de prévention efficaces sont, d'une part, un tableau de bord partagé des dossiers en attente avec un responsable identifié, et d'autre part, une réunion hebdomadaire courte où les difficultés de circuit sont signalées sans mise en cause personnelle. Ces outils transforment un grief implicite en sujet de discussion traitable.",
    "La réponse distingue l'avant et l'après, et propose deux mesures concrètes et collectives.")],
C("La CNV remplace l'accusation par un fait, un sentiment, un besoin et une demande négociable.",
  "Observation + sentiment + besoin + demande",
  "Fait vérifiable · je ressens · j'ai besoin · pouvez-vous",
  "Observation~Fait daté~Sentiment~Ce que je ressens~Besoin~Attente explicite~Demande~Action négociable",
  "Décrire le fait sans jugement|Nommer son sentiment|Expliciter le besoin|Formuler une demande précise|Écouter la réponse et construire ensemble",
  "Glisser un adjectif moralisateur dans l'observation|Confondre sentiment et accusation|Imposer une solution|Ignorer la cause organisationnelle",
  "Observation~Trois dossiers en retard~Sentiment~Je suis inquiet~Besoin~Recevoir avant 11 heures~Demande~Confirmer un changement",
  "Accusation~Vous êtes négligent~CNV~Le dossier est arrivé après l'heure",
  "Prévention~Agir avant~Gestion~Agir après le conflit"))

# ============================================================ COM5
add("COM5", "Communication adaptée au handicap et accessibilité", "Communication", ["BTS2"],
S("Adapter sa communication, c'est modifier sa manière d'échanger pour que l'information soit réellement reçue par la personne."
  "|Le référentiel BTS SP3S mentionne explicitement les techniques et outils de communication adaptés au handicap."
  "|La première règle est de s'adresser à la personne elle-même, et non à son accompagnant ou à son interprète."
  "|En cas de déficience auditive, on se place en face de la personne, on articule et on utilise des appuis écrits."
  "|En cas de déficience visuelle, on se présente, on décrit les actions accomplies et on propose un appui adapté."
  "|Pour une personne avec des difficultés cognitives, on fragmente l'information et on vérifie la compréhension étape par étape."
  "|Le langage clair et facile à lire et à comprendre (FALC) simplifie la syntaxe sans infantiliser la personne."
  "|Les supports augmentatifs et alternatifs (images, pictogrammes, synthèse vocale) peuvent compléter la parole."
  "|La langue des signes française est une langue à part entière : un interprète facilite l'échange mais ne remplace pas la personne."
  "|L'accessibilité concerne aussi l'espace : cheminement, éclairage, bruit de fond et place de l'accueil."
  "|L'accessibilité numérique impose des documents et des sites utilisables avec des technologies d'assistance."
  "|Le consentement et le respect du rythme de la personne priment sur l'efficacité administrative."),
[QC("À qui s'adresse-t-on en priorité lors d'un entretien avec une personne accompagnée ?", "À l'accompagnant~À l'interprète~À la personne elle-même~Au responsable du service", 2,
    "La personne est l'interlocutrice principale, quel que soit son mode de communication."),
 QC("Quel geste favorise l'échange avec une personne sourde ?", "Parler de dos~Se placer en face et articuler~Écrire très petit~Hausser le ton de façon excessive", 1,
    "La lecture labiale et la visibilité du visage aident à la compréhension."),
 QC("Que signifie FALC ?", "Facile à lire et à comprendre~Formation aux langues de communication~Fiche d'analyse de la communication~Français adapté aux collègues", 0,
    "Le FALC simplifie la forme sans infantiliser le contenu."),
 QC("Quel support peut compléter la parole pour une personne ayant des difficultés de langage ?", "Un jargon technique~Des pictogrammes~Une consigne orale unique~Un document très dense", 1,
    "Les supports augmentatifs et alternatifs facilitent la compréhension."),
 QC("Quel statut a la langue des signes française ?", "Un simple geste~Une langue à part entière~Un code secret~Un dialecte sans grammaire", 1,
    "La LSF possède sa propre grammaire et sa propre syntaxe."),
 QC("Quel élément de l'espace peut gêner la communication ?", "Un éclairage insuffisant~Une chaise confortable~Un accueil à hauteur de regard~Un silence respecté", 0,
    "L'éclairage, le bruit et le cheminement font partie de l'accessibilité."),
 QC("Quel principe prime sur l'efficacité administrative ?", "La rapidité avant tout~Le consentement et le rythme de la personne~La procédure sans exception~Le nombre de dossiers traités", 1,
    "La personne reste actrice de l'échange et de ses choix."),
 QT("Expliquer comment adapter un entretien d'accueil à une personne malvoyante.",
    "On se présente immédiatement par son nom et sa fonction, car la reconnaissance visuelle n'est pas possible. On demande comment la personne souhaite être accompagnée plutôt que de supposer ses besoins. On guide si elle le souhaite en proposant son bras, sans saisir le sien, et on annonce les obstacles ou les changements de direction. Pendant l'échange, on décrit ce que l'on fait (« je vous remets une attestation en deux exemplaires »), on nomme les interlocuteurs présents et on lit à voix haute les informations importantes. On propose les documents sous un format accessible, par exemple en gros caractères ou en version numérique compatible avec une synthèse vocale, et on vérifie la compréhension sans infantiliser.",
    "On attend une présentation, une proposition d'aide consentie, une description des actions et un support accessible."),
 QT("Distinguer accessibilité physique, communicationnelle et numérique dans un établissement social.",
    "L'accessibilité physique concerne les espaces : cheminement sans obstacle, rampe ou ascenseur, éclairage, sièges et hauteur du guichet. L'accessibilité communicationnelle porte sur les échanges : langage clair, reformulation, interprète, supports pictographiques, présence d'une personne ressource. L'accessibilité numérique vise les outils : documents balisés, contrastes suffisants, textes alternatifs, navigation au clavier et compatibilité avec les lecteurs d'écran. Ces trois dimensions sont complémentaires : un usager peut accéder au bâtiment mais renoncer à sa démarche si le formulaire en ligne est illisible par son logiciel. La démarche qualité de l'établissement doit les traiter ensemble et associer les usagers à leur évaluation.",
    "On distingue les trois dimensions et on montre leur complémentarité par un exemple concret.")],
C("Adapter sa communication ne change pas le respect dû à la personne : cela change les moyens utilisés pour être compris.",
  "Personne d'abord + supports adaptés + vérification",
  "FALC = facile à lire et à comprendre · LSF = langue à part entière · consentement = règle d'or",
  "Handicap auditif~Face et articulation~Handicap visuel~Se présenter et décrire~FALC~Phrases courtes~Supports~Pictogrammes",
  "Demander les besoins de la personne|Choisir le mode de communication|Adapter le débit et les supports|Vérifier la compréhension|Tracer l'adaptation retenue",
  "Parler à l'accompagnant à la place de la personne|Infantiliser le vocabulaire|Imposer un rythme|Supposer le besoin sans demander",
  "Usager malvoyant~Se présenter~Document~Gros caractères~LSF~Interprète~Vérification~Question ouverte",
  "Accessibilité physique~Espaces et cheminement~Accessibilité numérique~Documents et outils",
  "Adapter~Changer les moyens~Respecter~Ne pas changer la dignité"))

# ============================================================ COM6
add("COM6", "Réunion de service : préparation, animation et compte rendu", "Communication", ["BTS2"],
S("La réunion de service est un espace collectif de coordination, d'information et de décision dans un établissement."
  "|Elle se prépare avec un ordre du jour écrit, diffusé à l'avance, qui précise l'objet, l'heure, le lieu et les participants."
  "|Chaque point de l'ordre du jour associe un responsable et un temps prévu pour éviter le déroulement sans fin."
  "|Les documents de travail sont envoyés avant la séance pour que les participants puissent prendre connaissance des données."
  "|L'animation alterne temps d'information, temps de discussion et temps de décision."
  "|L'animateur veille à la parole de chacun, au respect des temps et au retour aux points de l'ordre du jour."
  "|Les divergences sont notées avec les arguments, puis les décisions sont formulées : qui fait quoi, pour quand, avec quels moyens."
  "|Les points non traités sont inscrits à une « question diverse » ou reportés avec une échéance."
  "|Le compte rendu est rédigé après la séance et diffusé aux participants et aux absents concernés."
  "|Il distingue les informations, les décisions et les actions, et mentionne la date de la prochaine réunion."
  "|La discrétion s'impose : les situations individuelles d'usagers ne sont évoquées que si le sujet le nécessite et sous forme anonymisée."
  "|Cette compétence relève des techniques d'organisation et d'animation de réunion du bloc 1 du référentiel."),
[QC("Que doit contenir un ordre du jour ?", "Le menu du restaurant~L'objet, l'heure, le lieu et les points traités~Les seules opinions du responsable~La liste des absents", 1,
    "L'ordre du jour cadre la séance et permet la préparation."),
 QC("Comment formuler une décision en fin de réunion ?", "On se contente d'un accord verbal~On précise le responsable, l'action et l'échéance~On laisse chacun interpréter~On la note sans date", 1,
    "Une décision opérationnelle indique qui fait quoi et pour quand."),
 QC("Quel rôle revient à l'animateur de la réunion ?", "Parler le plus longtemps possible~Répartir la parole et respecter l'ordre du jour~Imposer toutes les décisions~Supprimer les discussions", 1,
    "L'animateur facilite la participation et le déroulement."),
 QC("Que faire d'un point non traité à la fin de la séance ?", "L'oublier~Le reporter avec une échéance explicite~Le traiter sans en parler~Le supprimer du relevé", 1,
    "Le report doit être daté pour ne pas être perdu."),
 QC("Quelles informations distingue un bon compte rendu ?", "Cuisine, décor, horaires~Informations, décisions et actions~Blagues et impressions~Seulement les noms des présents", 1,
    "Cette distinction rend le compte rendu utilisable."),
 QC("Comment évoquer une situation d'usager en réunion ?", "Avec son nom complet~Sous forme anonymisée et si le sujet l'exige~Devant tous les services~Sans aucune précaution", 1,
    "Le secret professionnel impose une discrétion stricte."),
 QC("À quel bloc du référentiel se rattache l'animation de réunion ?", "Bloc 1~Bloc 2~Bloc 3~Bloc 4", 0,
    "Les techniques d'organisation et d'animation de réunion figurent au bloc 1."),
 QT("Décrire la préparation complète d'une réunion de service hebdomadaire.",
    "On fixe d'abord l'objectif de la séance : informer sur les arrivées, coordonner les permanences et régler les points bloquants. On rédige un ordre du jour avec trois ou quatre points, un responsable et une durée prévue pour chacun. On rassemble les documents nécessaires, par exemple le tableau des dossiers en attente et le planning de la semaine, et on les diffuse la veille. On réserve la salle, vérifie le matériel de visioconférence si des collègues sont à distance et prévoit un support de projection lisible. On désigne l'animateur et la personne qui tiendra le relevé des décisions. Enfin, on relit l'ordre du jour pour supprimer les points déjà traités par écrit.",
    "La réponse couvre objectif, ordre du jour, documents, logistique, rôles et relecture."),
 QT("Rédiger le compte rendu d'une réunion où une désaccord a porté sur l'ordre de traitement des demandes.",
    "Le compte rendu porte un titre, la date, le lieu, les participants et l'objet de la séance. Une première partie résume les informations partagées : volume des demandes, délais constatés et effectifs disponibles. Une deuxième partie retrace la discussion : deux positions ont été exprimées, l'une priorisant les dossiers les plus anciens, l'autre les situations d'urgence, avec les arguments entendus de part et d'autre. Une troisième partie consigne la décision retenue : un critère combiné est adopté, la responsable du service d'accueil tient la liste quotidienne et un point de situation est prévu dans quinze jours. Le document mentionne les actions, leurs responsables et les échéances, puis la date de la prochaine réunion. Il est diffusé aux participants et aux absents concernés.",
    "On attend les rubriques formelles, une restitution fidèle du désaccord et des actions datées.")],
C("Une réunion utile est préparée, animée et tracée : sans décision écrite, elle ne produit pas d'effet.",
  "Ordre du jour + animation + décisions + compte rendu",
  "Décision = responsable + action + échéance · discrétion = anonymisation",
  "Ordre du jour~Cadre de la séance~Animation~Parole répartie~Décision~Responsable et délai~Compte rendu~Trace écrite",
  "Définir l'objectif et rédiger l'ordre du jour|Diffuser les documents à l'avance|Animer en respectant les temps|Formuler explicitement les décisions|Rédiger et diffuser le compte rendu",
  "Réunir sans ordre du jour|Laisser la discussion dériver|Se contenter d'un accord verbal|Diffuser des données nominatives",
  "Réunion~Point bloquant~Discussion~Deux positions~Décision~Critère combiné~Suivi~Point dans quinze jours",
  "Information~Ce qui est su~Décision~Ce qui est choisi~Action~Ce qui sera fait",
  "Anonymiser~Protéger la personne~Nommer~Identifier un responsable"))

# ============================================================ MG1
add("MG1", "Management d'équipe : rôles, responsabilités et coordination", "Management", ["BTS1"],
S("Le management d'équipe consiste à organiser le travail collectif pour atteindre les objectifs du service."
  "|Il combine trois fonctions souvent attribuées à des personnes différentes : encadrer, coordonner et animer."
  "|L'encadrement porte sur les personnes : affectation, suivi, évaluation et respect des règles collectives."
  "|La coordination porte sur les activités : répartition des tâches, planning, interfaces entre services."
  "|L'animation porte sur la dynamique : communication, motivation, reconnaissance et gestion des tensions."
  "|Le référentiel BTS SP3S place ces compétences dans le bloc 4, consacré à la gestion de la structure et du service."
  "|Un organigramme formalise les responsabilités et les relations hiérarchiques ; un descriptif de poste précise les missions."
  "|La délégation efficace transfère une tâche avec son objectif, ses moyens et un cadre de restitution."
  "|La responsabilité reste celles du responsable même lorsqu'une tâche est déléguée."
  "|La coordination repose sur des outils partagés : planning, tableau de bord, compte rendu et procédure écrite."
  "|Le manager arbitre entre la charge de travail, la qualité du service et le respect des collaborateurs."
  "|Dans le secteur sanitaire et social, il doit aussi garantir la continuité du service et la protection des usagers."),
[QC("Quelle fonction du management porte sur la dynamique collective ?", "L'encadrement~La coordination~L'animation~La comptabilité", 2,
    "L'animation vise la motivation, la communication et la cohésion."),
 QC("Que formalise un organigramme ?", "Les seules horaires~Les responsabilités et relations hiérarchiques~Les comptes bancaires~Les préférences personnelles", 1,
    "L'organigramme représente la structure des rôles et des liens d'autorité."),
 QC("Quel élément doit accompagner une délégation ?", "Un objection~Un objectif, des moyens et un cadre de restitution~Une absence de consigne~Une rémunération immédiate", 1,
    "Déléguer sans cadrer le résultat produit des malentendus."),
 QC("À quel bloc du référentiel BTS SP3S se rattache la gestion d'équipe ?", "Bloc 1~Bloc 2~Bloc 3~Bloc 4", 3,
    "Le bloc 4 concerne la collaboration à la gestion de la structure et du service."),
 QC("Quel outil est utile à la coordination entre services ?", "Un tableau de bord partagé~Une réunion sans compte rendu~Une consigne orale unique~Un dossier personnel clos", 0,
    "Les outils partagés rendent l'avancement visible par tous."),
 QC("La responsabilité du responsable disparaît-elle lors d'une délégation ?", "Oui, toujours~Non, elle demeure~Oui, si la tâche est écrite~Non, sauf le week-end", 1,
    "On délègue l'exécution, pas la responsabilité finale."),
 QC("Quel arbitrage est propre au secteur sanitaire et social ?", "Rendement seul~Charge de travail, qualité de service et protection des usagers~Coût seul~Horaires seuls", 1,
    "Le manager concilie plusieurs exigences, dont la continuité et la sécurité du service."),
 QT("Distinguer encadrement, coordination et animation et donner un exemple concret pour chacune dans un service d'accueil.",
    "L'encadrement s'exerce sur les personnes : le responsable du service d'accueil répartit les plannings, suit les arrivées, valide les congés et conduit les entretiens annuels. La coordination s'exerce sur les activités : il organise la passation entre l'accueil et le service social, tient un tableau des dossiers en attente et planifie les permanences pour éviter les ruptures de service. L'animation s'exerce sur la dynamique : il salue les réussites, organise une réunion courte pour expliquer un changement de procédure et prend en charge une tension entre deux agents. Ces trois fonctions se complètent : un planning sans animation produit de la conformité sans engagement, et une bonne ambiance sans coordination produit du désordre.",
    "On définit les trois fonctions et on donne un exemple pour chacune, puis on montre leur complémentarité."),
 QT("Un service connaît des retards répétés dans la transmission des dossiers. Comment le manager doit-il procéder ?",
    "Il commence par rassembler les faits : dates des retards, services concernés, volume de dossiers et étapes où le blocage se produit. Il distingue ensuite les causes possibles : surcharge, consigne absente, circuit trop long ou désaccord entre services. Il réunit les personnes concernées, présente les données sans mettre en cause individuellement quiconque et cherche avec elles une solution : simplification du circuit, horizon horaire de transmission, responsable identifié par service. Il formalise la nouvelle règle par écrit, la teste pendant deux semaines et mesure le résultat avec le même indicateur. Enfin, il reconnaît l'amélioration et réajuste si nécessaire.",
    "On attend une démarche factuelle, collective, formalisée et mesurée, sans recherche de coupable.")],
C("Manager, c'est articuler les personnes, les activités et la dynamique collective au service de la qualité du service.",
  "Encadrer + coordonner + animer = management opérationnel",
  "Organigramme = rôles · délégation = tâche cadrée · responsabilité = non transférable",
  "Encadrement~Suivi des personnes~Coordination~Répartition des tâches~Animation~Dynamique collective~Responsabilité~Non délégable",
  "Recenser les faits et les blocages|Distinguer les causes|Réunir les acteurs concernés|Décider et formaliser la règle|Mesurer et ajuster",
  "Déléguer sans cadre|Confondre animation et distraction|Rechercher un coupable|Laisser une procédure implicite",
  "Retard~Transmission quotidienne~Cause~Circuit trop long~Décision~Horaires et responsable~Mesure~Deux semaines",
  "Encadrement~Les personnes~Coordination~Les activités",
  "Délégation~Transfère l'exécution~Responsabilité~Reste au responsable"))

# ============================================================ MG2
add("MG2", "Motivation et conduite du changement en équipe", "Management", ["BTS2"],
S("La motivation désigne l'ensemble des facteurs qui poussent un collaborateur à s'engager dans son travail."
  "|La hiérarchie des besoins de Maslow place les besoins physiologiques et de sécurité avant les besoins d'appartenance, d'estime et d'accomplissement."
  "|La théorie des deux facteurs de Herzberg distingue les facteurs d'hygiène, qui évitent l'insatisfaction, et les facteurs de motivation, qui la créent."
  "|Parmi les facteurs d'hygiène figurent la rémunération, les conditions de travail et les relations avec la hiérarchie."
  "|La reconnaissance, la responsabilité et la perception du résultat sont des facteurs de motivation."
  "|Un changement, même bénéfique, provoque souvent une résistance liée à la perte de repères."
  "|La résistance n'est pas de la mauvaise volonté : elle exprime une inquiétude ou un manque d'information."
  "|La conduite du changement commence par le diagnostic et l'explication du pourquoi, avant l'annonce du comment."
  "|La participation des équipes à la conception du changement augmente l'appropriation de la nouvelle situation."
  "|Un planning de communication précise qui informe, quand, avec quel support et comment recueillir les questions."
  "|La formation et l'accompagnement sont nécessaires quand les pratiques ou les outils évoluent."
  "|Le manager suit les indicateurs d'acceptation et ajuste le dispositif plutôt que d'imposer plus fort."),
[QC("Selon Maslow, quels besoins viennent en premier dans la hiérarchie ?", "Estime et accomplissement~Appartenance~Physiologiques et de sécurité~Reconnaissance", 2,
    "Les besoins de base doivent être satisfaits avant les besoins supérieurs."),
 QC("Que distingue la théorie de Herzberg ?", "Salaire et horaires~Facteurs d'hygiène et facteurs de motivation~Hommes et femmes~Débutants et anciens", 1,
    "Les facteurs d'hygiène évitent l'insatisfaction ; les autres créent l'engagement."),
 QC("Quel élément est un facteur de motivation selon Herzberg ?", "La rémunération~Les conditions de travail~La reconnaissance~La politique de l'entreprise", 2,
    "La reconnaissance et la responsabilité sont des facteurs de motivation."),
 QC("Comment interpréter une résistance au changement ?", "Comme de la mauvaise volonté~Comme un signe d'inquiétude ou de manque d'information~Comme une preuve d'incompétence~Comme un refus définitif", 1,
    "La résistance révèle souvent un besoin de sécurité ou de compréhension."),
 QC("Quelle est la première étape d'une conduite du changement ?", "Imposer la nouvelle procédure~Expliquer le pourquoi après le diagnostic~Supprimer les réunions~Changer les horaires", 1,
    "Le diagnostic et l'explication du pourquoi précèdent l'annonce des modalités."),
 QC("Quel effet attendu de la participation des équipes ?", "Une perte de temps systématique~Une meilleure appropriation du changement~Une hiérarchie affaiblie~Une augmentation des conflits", 1,
    "Participer rend le changement plus acceptable et plus durable."),
 QC("Quel indicateur suit le manager pendant un changement ?", "Le seul chiffre d'affaires~L'acceptation et la montée en compétences~La météo~Le nombre de réunions", 1,
    "On mesure l'appropriation et la capacité à appliquer la nouvelle pratique."),
 QT("Expliquer la différence entre facteurs d'hygiène et facteurs de motivation et en tirer une conséquence managériale.",
    "Les facteurs d'hygiène, comme la rémunération, les conditions matérielles ou la qualité des relations hiérarchiques, n'engendrent pas un engagement durable : leur absence crée une insatisfaction, mais leur présence ne suffit pas à motiver. Les facteurs de motivation, comme la reconnaissance, la responsabilité confiée, la variété des tâches et la perception d'un résultat utile, agissent directement sur l'engagement. La conséquence est qu'un manager ne doit pas compter sur une augmentation de salaire ou un nouveau bureau pour redresser une équipe démotivée : il doit agir sur le sens des tâches, donner des responsabilités réelles, reconnaître les réussites et montrer l'effet du travail sur les usagers.",
    "On définit les deux catégories et on en déduit une action managériale concrète, distincte du seul levier financier."),
 QT("Conduire le changement : une structure passe d'un accueil papier à un accueil numérique. Décrire la démarche.",
    "On diagnostique d'abord les usages réels : qui utilise le formulaire papier, quelles données sont redemandées, quels postes sont concernés et quelles compétences numériques existent. On explique ensuite le pourquoi : réduire les délais, sécuriser les données et faciliter le suivi des dossiers. On associe deux agents de l'accueil à la conception du nouveau circuit et on teste le dispositif sur une demi-journée. On organise une formation courte avec un support écrit, on désigne une personne ressource et on prévoit une période de double fonctionnement. On communique un calendrier, un espace de questions et un retour d'expérience hebdomadaire. On mesure enfin le délai de traitement et le taux d'usage du numérique, puis on ajuste la formation si nécessaire.",
    "On attend diagnostic, explication du sens, participation, test, formation, communication et mesure.")],
C("Le changement réussi n'est pas imposé : il est expliqué, co-construit, accompagné et mesuré.",
  "Pourquoi + participation + formation + mesure = appropriation",
  "Hygiène = éviter l'insatisfaction · motivation = créer l'engagement",
  "Maslow~Besoins hiérarchisés~Herzberg~Deux facteurs~Résistance~Inquiétude légitime~Appropriation~Adhésion active",
  "Diagnostiquer les usages|Expliquer le pourquoi|Associer les équipes|Former et tester|Communiquer et mesurer",
    "Imposer sans expliquer|Traiter la résistance comme une faute|Oublier la formation|Ne jamais mesurer l'effet",
  "Changement~Accueil numérique~Participation~Deux agents référents~Formation~Support écrit~Mesure~Délai de traitement",
  "Facteur d'hygiène~Évite l'insatisfaction~Facteur de motivation~Crée l'engagement",
  "Résistance~Signal à écouter~Mauvaise volonté~Interprétation hâtive"))

# ============================================================ MG3
add("MG3", "Délégation, autonomie et responsabilisation des collaborateurs", "Management", ["BTS2"],
S("La délégation est le transfert d'une tâche et de l'autorité nécessaire à sa réalisation, sous le contrôle du responsable."
  "|Elle se distingue du simple transfert d'exécution : elle donne aussi un objectif et une marge de décision."
  "|Une délégation bien conduite précise le résultat attendu, les moyens disponibles, les limites et la date de restitution."
  "|Le responsable reste redevable du résultat final même après délégation."
  "|L'autonomie est la capacité d'un collaborateur à décider et agir dans un cadre défini."
  "|La responsabilisation associe l'autonomie à l'obligation de rendre compte des décisions prises."
  "|Le degré de délégation dépend de la compétence de la personne, de la complexité de la tâche et du risque encouru."
  "|Les tâches routinières se délèguent plus facilement que les décisions engageant la sécurité des usagers."
  "|Une délégation progressive permet de développer les compétences et de préparer une évolution de poste."
  "|Le suivi s'organise avec des points d'étape, pas avec un contrôle permanent qui annule l'autonomie."
  "|Les erreurs sont analysées comme des apprentissages si elles ne mettent pas en cause la sécurité ou le secret professionnel."
  "|Dans les établissements sociaux, la délégation doit rester compatible avec les procédures et les obligations réglementaires."),
[QC("Qu'appelle-t-on délégation ?", "Transférer une tâche avec objectif, moyens et autorité~Donner un ordre sans explication~Supprimer un poste~Reporter une décision", 0,
    "La délégation transfère tâche et autorité dans un cadre défini."),
 QC("Que doit préciser une délégation bien conduite ?", "Le résultat, les moyens, les limites et la restitution~Seulement l'heure de début~Le salaire du collègue~L'avis de tous les services", 0,
    "Un cadre explicite évite les malentendus sur ce qui est attendu."),
 QC("Que reste-t-il au responsable après une délégation ?", "Aucune responsabilité~La responsabilité finale du résultat~La totalité de l'exécution~Le contrôle de chaque geste", 1,
    "On peut déléguer l'exécution, pas la responsabilité."),
 QC("Quel critère limite le degré de délégation ?", "La couleur du dossier~La compétence, la complexité et le risque~L'ancienneté seule~La taille du bureau", 1,
    "Compétence, complexité et risque déterminent le niveau d'autonomie possible."),
 QC("Quel suivi respecte l'autonomie déléguée ?", "Un contrôle permanent~Des points d'étape convenus~Aucun suivi~Une réprimande quotidienne", 1,
    "Les points d'étape permettent de suivre sans étouffer l'autonomie."),
 QC("Quand une erreur peut-elle être traitée comme un apprentissage ?", "Si elle met en cause la sécurité~Si elle reste dans le cadre et n'engage pas la sécurité~Si elle est répétée volontairement~Si elle concerne le secret professionnel", 1,
    "La sécurité et le secret professionnel ne peuvent être traités comme de simples apprentissages."),
 QC("Quelle contrainte spécifique existe dans le secteur social ?", "Aucune~Compatibilité avec les procédures et obligations réglementaires~Interdiction de déléguer~Priorité à la rapidité", 1,
    "Toute délégation doit respecter le cadre réglementaire de la structure."),
 QT("Expliquer la différence entre délégation, autonomie et responsabilisation.",
    "La délégation est un acte du responsable : il confie à une personne une tâche, l'autorité correspondante et un objectif précis. L'autonomie est une propriété de la situation de travail : la personne dispose d'une marge de décision dans un cadre défini, sans demander une validation à chaque étape. La responsabilisation va plus loin : elle attache à cette autonomie l'obligation de rendre compte des choix effectués et de leurs effets. Ainsi, un agent peut être autonome pour préparer un courrier d'orientation, mais il doit rendre compte du choix du dispositif proposé. Les trois notions forment une progression : on délègue, on laisse agir, on demande des comptes sur le résultat.",
    "On distingue l'acte de déléguer, la marge d'action et l'obligation de restitution, avec un exemple."),
 QT("Comment déléguer la tenue du registre des réclamations à un nouvel agent ?",
    "On vérifie d'abord que l'agent connaît les motifs de réclamation, le support utilisé et les règles de confidentialité. On définit le résultat attendu : chaque réclamation est enregistrée le jour même avec la date, le motif, le service concerné et la suite donnée. On précise les moyens : le registre sécurisé, la trame de saisie et la personne à contacter en cas de doute. On fixe les limites : aucun nom d'usager ne figure dans un document diffusé, aucune réponse engageant la structure n'est envoyée sans validation. On convient d'une restitution hebdomadaire et d'un premier point après une semaine. On reste disponible pour les questions, puis on réduit progressivement l'accompagnement.",
    "La réponse comporte objectif, moyens, limites, restitution et accompagnement progressif.")],
C("Déléguer, c'est donner un objectif et une marge d'action tout en gardant la responsabilité finale.",
  "Tâche + autorité + cadre + restitution",
  "Autonomie = marge de décision · responsabilisation = obligation de rendre compte",
  "Délégation~Transfert cadré~Autonomie~Marge de décision~Limites~Sécurité et secret~Restitution~Point d'étape",
  "Évaluer la compétence et le risque|Formuler le résultat attendu|Préciser moyens et limites|Convenir des points de suivi|Analyser le résultat avec l'agent",
  "Déléguer sans objectif|Confondre autonomie et absence de cadre|Contrôler chaque geste|Oublier la responsabilité finale",
  "Registre~Réclamations quotidiennes~Objectif~Saisie le jour même~Limite~Anonymat~Restitution~Point hebdomadaire",
  "Autonomie~Peut décider~Responsabilisation~Doit rendre compte",
  "Déléguer~Transfère l'exécution~Responsable~Répond du résultat"))

# ============================================================ MG4
add("MG4", "Gestion des conflits et médiation dans une équipe", "Management", ["BTS2"],
S("Un conflit d'équipe est un désaccord durable entre personnes ou Services qui perturbe la coopération."
  "|Il peut porter sur les tâches, les rôles, la répartition de la charge ou les valeurs professionnelles."
  "|Tous les conflits ne sont pas négatifs : un désaccord sur une procédure peut améliorer la qualité du service."
  "|Ce qui devient problématique, c'est le conflit personnalisé, répété et non traité."
  "|Le manager distingue d'abord les faits des ressentis, en écoutant chaque partie séparément."
  "|Il identifie les intérêts sous-jacents : besoin de reconnaissance, de clarté ou d'équité."
  "|La médiation fait intervenir un tiers neutre pour rétablir le dialogue sans imposer une solution."
  "|Le médiateur ne juge pas : il organise la parole, reformule et aide à construire des options."
  "|Les règles de la médiation sont le respect de la parole de chacun, la confidentialité et la volonté de trouver un accord."
  "|La solution écrite précise les engagements de chacun, les délais et un moment de réévaluation."
  "|Si le conflit met en cause la sécurité ou la dignité d'une personne, le manager passe à une procédure formelle."
  "|Le suivi après l'accord est indispensable : un conflit éteint en apparence peut ressurgir sans suivi."),
[QC("Quel conflit est réellement problématique dans une équipe ?", "Un désaccord technique ponctuel~Un conflit personnalisé, répété et non traité~Une discussion de procédure~Une question posée en réunion", 1,
    "La personnalisation et la répétition transforment le désaccord en blocage."),
 QC("Que fait le médiateur ?", "Il juge qui a tort~Il organise la parole et aide à construire des options~Il impose une sanction~Il remplace le responsable", 1,
    "La médiation est une facilitation, pas une décision autoritaire."),
 QC("Quelle règle ne s'applique pas à une médiation ?", "Respect de la parole~Confidentialité~Volonté de trouver un accord~Publicité systématique des propos", 3,
    "La confidentialité protège la parole des participants."),
 QC("Quel intérêt sous-jacent peut alimenter un conflit ?", "La couleur du support~Le besoin de reconnaissance ou de clarté~L'heure du déjeuner~Le nombre de dossiers clos", 1,
    "Derrière les positions se trouvent souvent des besoins de reconnaissance ou d'équité."),
 QC("Quand passer à une procédure formelle ?", "Dès le premier désaccord~Quand la sécurité ou la dignité est en cause~Jamais~Après une seule réunion", 1,
    "Les atteintes à la sécurité ou à la dignité ne relèvent pas de la seule médiation."),
 QC("Que doit contenir la solution écrite ?", "Les opinions de chacun~Les engagements, délais et réévaluation~Les seuls faits anciens~Une analyse psychologique", 1,
    "L'écrit rend l'accord vérifiable et évite les interprétations divergentes."),
 QC("Pourquoi prévoir un suivi après l'accord ?", "Pour prolonger le conflit~Pour éviter une rechute silencieuse~Pour changer de responsable~Pour supprimer la procédure", 1,
    "Sans suivi, un accord peut rester théorique et le conflit ressurgir."),
 QT("Décrire la démarche d'un manager face à un conflit entre deux agents à propos de la répartition des permanences.",
    "Le manager entend d'abord chaque agent séparément et note les faits : dates, plannings, échanges écrits, sans retenir les accusations comme des vérités. Il identifie ensuite les intérêts : l'un souhaite des week-ends libres pour des raisons familiales, l'autre estime porter seul les permanences du samedi. Il vérifie la règle collective et constate qu'elle n'est plus adaptée aux effectifs. Il réunit les deux personnes avec un tiers neutre, fait reformuler chaque position et cherche plusieurs options : rotation harmonisée, échange de plages ou compensation. Il retient avec elles une règle révisée, l'écrit dans le planning et prévoit un point après un mois. Si l'un des agents refuse tout échange ou si une pression abusive apparaît, il passe à une procédure formelle avec la direction.",
    "On attend écoute séparée, identification des intérêts, médiation, accord écrit, suivi et limite de la médiation."),
 QT("Distinguer conflit de tâches et conflit relationnel et expliquer comment le second peut nuire à l'accueil des usagers.",
    "Le conflit de tâches porte sur le contenu du travail : la bonne procédure, l'ordre des priorités, la répartition des dossiers. Il peut être utile s'il améliore la qualité des décisions. Le conflit relationnel porte sur les personnes : animosité, soupçon, dévaluation de la compétence de l'autre. Il détourne l'énergie de l'équipe vers la défense de soi et réduit la communication nécessaire à la continuité du service. À l'accueil, deux agents qui ne se parlent plus ne se transmettent pas les consignes, ce qui entraîne des informations contradictoires données à un même usager et une perte de confiance. Le manager doit donc traiter le conflit relationnel rapidement tout en préservant la possibilité de débattre des tâches.",
    "On oppose les deux types de conflit et on montre l'effet concret sur la qualité de l'accueil.")],
C("Un conflit se traite en écoutant les faits, en identifiant les besoins et en écrivant un accord suivi.",
  "Fais + intérêts + médiation + accord + suivi",
  "Conflit de tâches peut être utile · conflit relationnel nuit au service",
  "Fait~Élément vérifiable~Intérêt~Besoin sous-jacent~Médiation~Tiers neutre~Accord~Engagement écrit",
  "Écouter les parties séparément|Distinguer faits et ressentis|Identifier les intérêts|Organiser la médiation|Écrire et suivre l'accord",
    "Prendre parti dès le début|Confondre médiation et sanction|Laisser un accord oral|Oublier le suivi",
  "Plannings~Permanences contestées~Intérêt~Équité des week-ends~Accord~Rotation révisée~Suivi~Point à un mois",
  "Conflit de tâches~Porte sur le travail~Conflit relationnel~Porte sur les personnes",
  "Médiation~Aide à construire~Arbitrage~Impose une solution"))

# ============================================================ MG5
add("MG5", "Qualité de vie au travail et risques psycho-sociaux", "Management", ["BTS2"],
S("La qualité de vie au travail (QVT) désigne l'ensemble des actions qui améliorent les conditions dans lesquelles les salariés exercent leur activité."
  "|Elle concerne aussi bien l'organisation du travail que les relations, la charge et la reconnaissance."
  "|Les risques psycho-sociaux (RPS) sont des risques pour la santé mentale liés à l'organisation et aux conditions de travail."
  "|L'Institut national de recherche et de sécurité identifie notamment l'intensité du travail, les exigences émotionnelles et l'insécurité de l'emploi."
  "|Le manque d'autonomie et la mauvaise qualité des relations de travail figurent également parmi les facteurs de risque."
  "|Les exigences émotionnelles sont particulières dans le secteur social : l'agent doit rester disponible face à la détresse."
  "|Le document unique d'évaluation des risques professionnels doit intégrer les risques psycho-sociaux."
  "|Les signes d'alerte sont la fatigue persistante, le désengagement, l'irritabilité et l'augmentation des arrêts de travail."
  "|Le manager agit en amont : clarification des rôles, planning prévisible, reconnaissance et espaces de parole."
  "|Le droit d'alerte et la remontée d'information doivent être possibles sans représailles."
  "|Un dispositif d'écoute peut associer la direction, les représentants du personnel et un intervenant extérieur."
  "|La QVT contribue à la qualité du service : une équipe épuisée ne peut pas accompagner durablement les usagers."),
[QC("Que désigne la qualité de vie au travail ?", "Les seuls avantages matériels~Les conditions dans lesquelles les salariés exercent leur activité~Les horaires d'ouverture~Le chiffre d'affaires", 1,
    "La QVT couvre organisation, relations, charge et reconnaissance."),
 QC("Quel facteur relève des risques psycho-sociaux ?", "Une intensité de travail excessive~Une couleur de mur~Une police de caractères~Une signalétique claire", 0,
    "L'intensité et les exigences émotionnelles sont des facteurs de RPS identifiés."),
 QC("Quel document doit intégrer les risques psycho-sociaux ?", "Le registre des réclamations~Le document unique d'évaluation des risques professionnels~Le plan de formation~Le budget prévisionnel", 1,
    "Le DUERP recense les risques professionnels, y compris psycho-sociaux."),
 QC("Quel signe peut alerter le manager ?", "Une augmentation des arrêts de travail~Une baisse du nombre de réunions~Un changement de logo~Une nouvelle signalétique", 0,
    "L'augmentation des arrêts et le désengagement sont des signaux d'alerte."),
 QC("Quelle action est préventive plutôt que curative ?", "Attendre le départ d'un agent~Clarifier les rôles et rendre le planning prévisible~Sanctionner les retards~Réduire les espaces de parole", 1,
    "Clarification et prévisibilité agissent en amont du risque."),
 QC("Quelle exigence est propre au secteur social ?", "Une exigence de rentabilité seule~Une exigence émotionnelle face à la détresse~Une absence de contact~Un travail uniquement administratif", 1,
    "La disponibilité émotionnelle est un facteur de risque spécifique."),
 QC("Que doit garantir le droit d'alerte ?", "Une remontée sans représailles~Le silence des agents~Une sanction automatique~Une réunion annuelle unique", 0,
    "La remontée d'information doit être protégée pour être utilisée."),
 QT("Expliquer le lien entre qualité de vie au travail et qualité du service rendu à l'usager.",
    "Les deux qualités sont liées par la capacité des professionnels à être présents et attentifs. Une équipe confrontée à une charge imprévisible, à des rôles flous et à un manque de reconnaissance développe fatigue et désengagement ; elle a alors moins de disponibilité pour écouter une personne en détresse, multiplie les erreurs de transmission et peut adopter des réponses défensives. À l'inverse, un planning lisible, une répartition claire des responsabilités, des temps d'échange et une reconnaissance explicite soutiennent l'attention et la cohérence des pratiques. La QVT n'est donc pas un avantage accessoire : c'est une condition de la qualité de l'accompagnement et de la continuité du service.",
    "On montre le lien causal entre conditions de travail et capacité d'accompagnement, avec un exemple."),
 QT("Comment le manager peut-il prévenir les risques psycho-sociaux dans un service d'accueil très sollicité ?",
    "Il commence par mesurer la charge réelle : nombre d'accueils, durée moyenne, pics d'activité et interruptions. Il organise ensuite la prévisibilité du planning, alterne les tâches d'accueil et les tâches administratives, et clarifie qui prend en charge les situations les plus difficiles. Il instaure un temps court de débriefing après les situations tendues et un espace de parole hebdomadaire, avec une possibilité de signalement anonyme. Il veille à reconnaître explicitement le travail accompli et à donner du sens en montrant les effets positifs pour les usagers. Il inscrit les risques identifiés dans le document unique et suit les indicateurs d'absentéisme et de turnover, en associant les représentants du personnel et, si nécessaire, un intervenant extérieur.",
    "On attend mesure de la charge, organisation, espaces de parole, reconnaissance, DUERP et indicateurs.")],
C("La QVT n'est pas un confort : c'est une condition de la santé des équipes et de la qualité de l'accompagnement.",
  "Organisation + relations + reconnaissance = prévention des RPS",
  "DUERP = recensement des risques · droit d'alerte = remontée protégée",
  "QVT~Conditions de travail~RPS~Risques pour la santé mentale~DUERP~Recensement~Alerte~Remontée protégée",
  "Mesurer la charge réelle|Clarifier rôles et plannings|Instaurer des espaces de parole|Reconnaître et donner du sens|Suivre les indicateurs",
  "Confondre QVT et seuls avantages|Ignorer les signaux faibles|Sanctionner la remontée|Attendre la crise pour agir",
  "Service d'accueil~Pics d'activité~Prévention~Planning lisible~Débriefing~Après situation tendue~Indicateur~Absentéisme",
  "QVT~Agir en amont~Gestion de crise~Agir après le dommage",
  "Exigence émotionnelle~Spécifique au social~Intensité de travail~Facteur de risque"))

# ============================================================ MG6
add("MG6", "Recrutement et intégration d'un collaborateur", "Management", ["BTS2"],
S("Le recrutement est un processus qui vise à pourvoir un poste en reliant les besoins de la structure et les compétences d'un candidat."
  "|Le référentiel BTS SP3S mentionne la participation au recrutement de personnel dans le bloc 4."
  "|La première étape est la définition du besoin : missions, profil, compétences requises et conditions d'exercice."
  "|La fiche de poste décrit les activités, les responsabilités, les relations hiérarchiques et les compétences attendues."
  "|L'annonce diffuse le poste en respectant les règles d'égalité de traitement et de non-discrimination."
  "|La sélection du CV repose sur des critères objectifs définis à l'avance et tracés."
  "|L'entretien de recrutement associe des questions sur le parcours et des mises en situation professionnelles."
  "|La grille d'entretien garantit que tous les candidats sont évalués sur les mêmes critères."
  "|Les questions indiscrètes sur la santé, la grossesse ou les opinions sont interdites."
  "|Le choix est motivé par écrit sans être diffusé aux autres candidats."
  "|L'intégration comprend l'accueil matériel, la présentation de l'équipe, la formation aux procédures et un parrainage."
  "|Un point à trente jours permet de vérifier la compréhension du poste et de corriger les premières difficultés."),
[QC("Quelle est la première étape d'un recrutement ?", "Publier l'annonce~Définir le besoin et le profil~Réunir le jury~Signer le contrat", 1,
    "On ne recrute bien qu'après avoir précisé le besoin et les compétences requises."),
 QC("Quel document décrit les activités et responsabilités du poste ?", "Le bulletin de salaire~La fiche de poste~Le contrat de location~Le registre des réclamations", 1,
    "La fiche de poste cadre les missions et les relations hiérarchiques."),
 QC("À quoi sert une grille d'entretien ?", "À impressionner le candidat~À évaluer tous les candidats sur les mêmes critères~À éviter de prendre des notes~À remplacer la fiche de poste", 1,
    "La grille favorise l'objectivité et la traçabilité de la sélection."),
 QC("Quelle question est interdite en entretien ?", "Quelle est votre expérience de l'accueil ?~Envisagez-vous une grossesse ?~Quelles formations avez-vous suivies ?~Comment gérez-vous un usager mécontent ?", 1,
    "Les questions sur la santé ou la grossesse sont discriminatoires."),
 QC("Que contient une mise en situation ?", "Une devinette~Une tâche proche de celle du poste~Une question d'opinion~Un test de culture générale", 1,
    "Elle observe les compétences professionnelles en action."),
 QC("Quel élément fait partie de l'intégration ?", "L'absence de formation~La présentation de l'équipe et des procédures~Le silence sur les règles~Une évaluation sans retour", 1,
    "L'intégration associe accueil, formation et accompagnement."),
 QC("Pourquoi prévoir un point à trente jours ?", "Pour sanctionner~Pour vérifier la compréhension et corriger les difficultés~Pour prolonger la période d'essai systématiquement~Pour supprimer le parrainage", 1,
    "Le point d'étape sécurise la prise de poste et permet d'ajuster."),
 QT("Construire une grille d'entretien pour un poste d'agent d'accueil dans un établissement social.",
    "La grille comporte d'abord les critères issus de la fiche de poste : écoute et reformulation, connaissance des circuits d'orientation, discrétion professionnelle, gestion d'une réclamation et usage des outils numériques. Chaque critère est décliné en comportements observables : par exemple, pour l'écoute, « laisse la personne terminer avant de répondre » et « reformule la demande ». Chaque candidat reçoit les mêmes questions et la même mise en situation : accueillir une personne mécontente qui attend depuis une heure. Le jury note sur une échelle de quatre niveaux avec des exemples pour chaque niveau, puis consigne une synthèse écrite. Les appréciations portent sur les comportements observés, jamais sur la personnalité supposée.",
    "On attend des critères issus du poste, des comportements observables, une mise en situation identique et une notation tracée."),
 QT("Expliquer la différence entre recrutement et intégration et dire pourquoi la seconde est déterminante.",
    "Le recrutement sélectionne une personne à partir d'un besoin identifié : il produit une décision et un contrat. L'intégration accompagne la personne dans sa prise de fonction : elle produit des compétences opérationnelles et une relation de travail. Un bon recrutement peut échouer si l'intégration est négligée : l'agent arrivé ne comprend pas les circuits, hésite à demander de l'aide et reproduit des erreurs qui affectent l'accueil des usagers. L'intégration réussie associe un accueil matériel, une présentation des missions et des règles, une formation aux outils, un parrainage et des points d'étape. Elle est donc déterminante pour la qualité du service et pour la rétention du personnel.",
    "On distingue sélection et accompagnement, et on explique l'effet de l'intégration sur la qualité du service.")],
C("Le recrutement sélectionne sur des critères objectifs ; l'intégration transforme la sélection en compétence opérationnelle.",
  "Besoin → profil → sélection → décision → intégration",
  "Grille = critères identiques pour tous · intégration = accueil, formation, parrainage",
  "Fiche de poste~Missions et profil~Grille~Critères objectifs~Entretien~Questions et situation~Intégration~Accompagnement",
  "Définir le besoin et rédiger la fiche de poste|Diffuser l'annonce sans discrimination|Évaluer avec une grille commune|Motiver le choix par écrit|Accueillir, former et faire un point à trente jours",
  "Poser une question sur la santé|Modifier les critères entre candidats|Négliger l'accueil matériel|Laisser le nouvel agent sans parrain",
  "Poste~Agent d'accueil~Critère~Reformulation~Situation~Usager mécontent~Intégration~Point à trente jours",
  "Recrutement~Choisir une personne~Intégration~Rendre autonome",
  "Question légitime~Porte sur le poste~Question intrusive~Porte sur la vie privée"))

# ============================================================ MG7
add("MG7", "Entretien annuel et développement des compétences", "Management", ["BTS2"],
S("L'entretien annuel est un temps formalisé d'échange entre un collaborateur et son responsable hiérarchique."
  "|Il est distinct de l'entretien de recrutement et de l'entretien de service : il porte sur une période écoulée et sur les perspectives."
  "|Ses objectifs sont l'évaluation des résultats, l'identification des compétences et la définition des axes de progression."
  "|Il s'appuie sur des faits et des indicateurs : dossiers traités, délais respectés, qualité de l'accueil et participation collective."
  "|La préparation comprend une auto-évaluation du collaborateur et la collecte d'éléments par le responsable."
  "|L'entretien suit une trame : bilan de la période, points forts, difficultés, besoins de formation et objectifs à venir."
  "|Les critiques sont formulées sur des comportements observés, jamais sur la personnalité."
  "|Le collaborateur doit pouvoir s'exprimer et contester une appréciation : l'échange est bidirectionnel."
  "|Le plan de formation traduit les besoins identifiés en actions avec des objectifs, des coûts et des échéances."
  "|Le référentiel BTS SP3S mentionne l'accompagnement de l'évolution des compétences dans le bloc 4."
  "|Le compte rendu d'entretien est signé par les deux parties et verse au dossier professionnel."
  "|Un suivi dans l'année évite que les objectifs annuels restent sans effet sur les pratiques."),
[QC("Quel est l'objet principal de l'entretien annuel ?", "Sanctionner automatiquement~Évaluer la période écoulée et définir des axes de progression~Recruter un collègue~Clore un conflit", 1,
    "L'entretien annuel combine bilan et perspectives de développement."),
 QC("Sur quoi doit s'appuyer une critique professionnelle ?", "Sur une impression~Sur des comportements observés et des faits~Sur une rumeur~Sur l'avis d'un seul collègue", 1,
    "Les faits observables rendent l'appréciation recevable et vérifiable."),
 QC("Qui prépare l'entretien annuel ?", "Le seul responsable~Le responsable et le collaborateur~La direction uniquement~Le service des ressources humaines seul", 1,
    "L'auto-évaluation du collaborateur complète la préparation du responsable."),
 QC("Quelle qualité distingue un entretien réussi ?", "Un monologue du responsable~Un échange bidirectionnel~Une absence de notes~Une durée illimitée", 1,
    "Le collaborateur doit pouvoir s'exprimer et discuter les appréciations."),
 QC("Que contient un plan de formation ?", "Les seuls souhaits du responsable~Des actions avec objectifs, coûts et échéances~La liste des absents~Les horaires d'ouverture", 1,
    "Le plan de formation traduit les besoins en actions programmées."),
 QC("Quel document officialise l'entretien ?", "Un courriel informel~Un compte rendu signé par les deux parties~Une note orale~Le registre des réclamations", 1,
    "La signature des deux parties trace l'accord sur le bilan et les objectifs."),
 QC("Pourquoi prévoir un suivi dans l'année ?", "Pour reporter tous les objectifs~Pour éviter que les objectifs restent sans effet~Pour supprimer le plan de formation~Pour changer de responsable", 1,
    "Le suivi opérationnel donne de l'effet aux objectifs annuels."),
 QT("Décrire le déroulement d'un entretien annuel constructif et préciser le rôle de chaque étape.",
    "La préparation précède l'entretien : le collaborateur remplit une auto-évaluation et le responsable rassemble les faits et indicateurs de la période. L'ouverture rappelle l'objet de l'entretien et installe un cadre confidentiel. Le bilan revient sur les résultats en s'appuyant sur des exemples concrets, ce qui rend l'évaluation justifiable. Les points forts sont nommés explicitement, car la reconnaissance est un levier de motivation. Les difficultés sont analysées comme des situations à comprendre, en distinguant ce qui vient de la personne de ce qui vient de l'organisation. Les besoins sont ensuite traduits en objectifs et en actions de formation. La clôture formalise un compte rendu signé et une date de suivi. Chaque étape sert à rendre l'évaluation compréhensible et l'action engageante.",
    "On attend les étapes dans l'ordre, le rôle de chacune et une mention de la signature et du suivi."),
 QT("Un agent d'accueil commet des erreurs de transmission répétées. Comment conduire l'entretien annuel sans le décourager ?",
    "Le responsable présente d'abord les faits : trois dossiers transmis avec une pièce manquante sur les deux derniers mois, en précisant les dates et les conséquences pour l'usager. Il demande ensuite au collaborateur comment il vit ces situations et ce qui, selon lui, se passe dans le circuit : il peut apparaître une surcharge ou une trame de transmission peu claire. Il distingue ce qui relève de l'attention de l'agent et ce qui relève de l'organisation. Il formule ensuite une critique sur le comportement observé, sans qualifier la personne. Il définit avec lui une action precise : utiliser une checklist avant transmission et demander un contrôle croisé pendant un mois. Il inscrit cette action dans le compte rendu avec une date de point et prévoit, si besoin, une formation courte.",
    "On attend faits datés, écoute, distinction responsabilité individuelle et organisationnelle, action précise et suivi.")],
C("L'entretien annuel est un outil de pilotage : il évalue avec des faits et convertit les besoins en actions.",
  "Préparation + bilan + dialogue + objectifs + suivi",
  "Critique = comportement observé · plan de formation = actions datées · compte rendu signé",
  "Auto-évaluation~Regard du collaborateur~Faits~Éléments vérifiables~Objectifs~Axes de progression~Suivi~Point dans l'année",
  "Préparer avec l'auto-évaluation et les indicateurs|Ouvrir dans un cadre confidentiel|Réaliser le bilan avec exemples|Nommer les points forts et analyser les difficultés|Formaliser objectifs, formation et suivi",
  "Juger la personnalité|Transformer l'entretien en monologue|Laisser les objectifs sans échéance|Ne pas tracer l'entretien",
  "Erreur~Trois dossiers incomplets~Dialogue~Recherche des causes~Action~Checklist de transmission~Suivi~Point à un mois",
  "Entretien annuel~Bilan et perspectives~Entretien de recrutement~Sélection d'un candidat",
  "Fait~Vérifiable et daté~Impression~Interprétation personnelle"))

# APPEND_HERE

valider_et_ecrire(F, "btssp3s-mat-part-A.json")
