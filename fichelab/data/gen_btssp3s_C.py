# -*- coding: utf-8 -*-
"""Generateur btssp3s-mat-part-C.json — lot C : Sciences sanitaires et sociales (5),
Techniques de prévention et d'accompagnement (5), Anglais professionnel (5),
Méthodologie de projet (5).

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


# ============================================================ SS1
add("SS1", "Identité sociale et processus de stigmatisation", "Sciences sanitaires et sociales", ["BTS1"],
S("L'identité sociale se construit à partir de l'appartenance à des groupes et à des catégories."
  "|Elle comprend une dimension personnelle et une dimension collective."
  "|Le processus d'identification repose à la fois sur la ressemblance et sur la distinction."
  "|Une catégorie sociale rassemble des personnes qui partagent des caractéristiques communes."
  "|La stigmatisation attribue à une personne une identité dévaluée à partir d'un marqueur."
  "|Le marqueur peut être lié à la santé, au handicap, à l'origine ou à la situation sociale."
  "|La stigmatisation produit une distance sociale et une perte de reconnaissance."
  "|Elle peut conduire à l'exclusion, à la discrimination et à une dégradation de l'état de santé."
  "|Le regard du professionnel peut soit renforcer, soit prévenir la stigmatisation."
  "|L'accompagnement s'appuie sur la reconnaissance de la personne dans sa singularité."
  "|Les représentations sociales orientent les jugements et les pratiques professionnelles."
  "|Le référentiel BTS SP3S associe ces savoirs à l'analyse de la demande et du besoin."),
[QC("Que désigne l'identité sociale ?", "L'appartenance à des groupes et catégories sociaux~Un simple goût personnel~Une donnée purement biologique~Un avis administratif", 0,
    "L'identité sociale se construit par l'appartenance et la distinction entre groupes."),
 QC("Sur quoi repose le processus d'identification ?", "La ressemblance et la distinction~Le hasard seul~La taille du groupe~L'âge uniquement", 0,
     "On se identifie à ce qui ressemble et on se distingue de ce qui diffère."),
 QC("Qu'est-ce qu'un marqueur de stigmatisation ?", "Un signe distinctif qui fonde une catégorisation dévaluée~Une donnée sans conséquence~Une simple mode~Un document administratif", 0,
     "Le marqueur devient stigmatisant lorsqu'il sert à dévaluer la personne."),
 QC("Quelle est une conséquence de la stigmatisation ?", "Une reconnaissance accrue~Une perte de reconnaissance et une exclusion~Une amélioration de la santé~Une promotion automatique", 1,
     "La stigmatisation éloigne la personne et nuit à sa reconnaissance."),
 QC("Quel rôle jouent les représentations sociales ?", "Elles n'ont aucun effet~Elles orientent les jugements et les pratiques~Elles remplacent la loi~Elles sont identiques pour tous", 1,
     "Les représentations influencent la manière de juger et d'agir."),
 QC("Comment un professionnel prévient-il la stigmatisation ?", "En catégorisant systématiquement~En reconnaissant la personne dans sa singularité~En évitant tout échange~En utilisant des étiquettes", 1,
     "La reconnaissance de la singularité est le levier professionnel essentiel."),
 QC("Quel texte porte les savoirs associés de la filière ?", "Le référentiel BTS SP3S, annexe III~Le seul Code du travail~Le seul Code civil~Le programme du lycée", 0,
     "Les savoirs associés figurent à l'annexe III du référentiel BTS SP3S."),
 QT("Expliquer comment une catégorisation peut devenir stigmatisante et quels effets cela produit.",
     "Une catégorisation devient stigmatisante lorsqu'un marqueur, par exemple un diagnostic, un handicap ou une origine, est utilisé pour réduire la personne à une identité dévaluée. Le professionnel ne voit plus une personne singulière mais un membre d'une catégorie supposée, ce qui entraîne une mise à distance : paroles réduites, décisions prises sans elle, évitement du contact. La personne concernée perd reconnaissance et estime de soi, ce qui peut aggraver son état de santé et son exclusion sociale. Les effets sont donc à la fois symboliques, relationnels et concrets : refus de prestation, orientation automatique, difficulté d'accès à l'emploi ou au logement. Prévenir la stigmatisation suppose de repérer le marqueur, de nommer le jugement et de réaffirmer la personne comme sujet de son parcours.",
     "On attend le passage du marqueur à l'identité dévaluée, puis les effets relationnels et sociaux."),
 QT("Un professionnel déclare à propos d'un usager : « c'est encore un cas psychiatrique ». Analyser cette parole et proposer une reformulation professionnelle.",
     "Cette parole réduit la personne à un diagnostic et transforme une situation de santé en étiquette identitaire. Le mot « cas » installe une distance et suggère que la personne est un problème à gérer plutôt qu'un sujet à accompagner. Elle peut être entendue par les collègues et renforcer une représentation collective dévaluée, puis se retrouver dans les transmissions et les décisions. Une reformulation professionnelle décrit un comportement observé et un besoin, sans jugement de valeur : « Madame rencontre des difficultés à gérer son traitement depuis la semaine dernière ; elle a besoin d'un accompagnement pour organiser ses prises et d'un rendez-vous avec l'équipe soignante. » On vérifie ensuite la compréhension de la personne et on trace l'action prévue. La règle est de parler de la situation et du besoin, jamais d'une catégorie censée épuiser l'identité de la personne.",
     "On identifie l'étiquette, ses effets, puis on propose une description factuelle centrée sur le besoin.")],
C("La stigmatisation transforme une différence en infériorité : le professionnel doit reconnaissance et singularité.",
  "Marqueur + catégorisation dévaluée + distance = stigmatisation",
  "Identité sociale · représentations · reconnaissance · singularité",
  "Identité~Appartenance et distinction~Groupe~Ensemble de personnes~Marqueur~Signe de catégorisation~Stigmatisation~Identité dévaluée~Effet~Perte de reconnaissance",
  "Repérer le marqueur à l'origine du jugement|Identifier la catégorie activée|Observer les effets sur la personne|Réaffirmer sa singularité dans l'échange|Vérifier sa propre posture professionnelle",
  "Réduire la personne à un diagnostic|Utiliser des étiquettes devant les collègues|Confondre prévention et simple politesse|Ignorer l'effet des représentations",
  "Marqueur~Handicap visible~Réaction~Mise à distance~Parole~Mot dévalué~Pratique~Reconnaissance de la personne",
  "Regard stigmatisant~Etiquette collective~Distance et silence~Regard respectueux~Personne singulière~Écoute et reformulation",
  "Identité personnelle~Histoire singulière~Projet individuel~Identité sociale~Appartenance au groupe~Catégorisation partagée"))

# ============================================================ SS2
add("SS2", "Contexte socio-démographique et inégalités de santé", "Sciences sanitaires et sociales", ["BTS2"],
S("L'état de santé d'une population dépend de facteurs sociaux, économiques et environnementaux."
  "|Les déterminants sociaux de la santé incluent le revenu, le logement, l'emploi et le niveau d'instruction."
  "|L'espérance de vie varie selon le milieu social et le territoire."
  "|Les inégalités sociales de santé se mesurent par des écarts de morbidité et de mortalité."
  "|Le gradient social montre que la santé s'améliore progressivement avec la position sociale."
  "|La précarité accroît les risques sanitaires et limite l'accès aux soins et à la prévention."
  "|Le renoncement aux soins est plus fréquent lorsque les ressources financières sont faibles."
  "|Le logement insalubre, le chômage et l'isolement sont des facteurs de vulnérabilité."
  "|La démographie régionale influence l'offre de services et les délais d'accès."
  "|Les politiques publiques cherchent à réduire ces écarts par la prévention et l'accès aux droits."
  "|Le professionnel doit adapter son accompagnement aux ressources et aux contraintes de la personne."
  "|Le référentiel BTS SP3S rattache ces savoirs au contexte socio-démographique et à l'analyse du besoin."),
[QC("Qu'appelle-t-on déterminants sociaux de la santé ?", "Des facteurs comme le revenu, le logement et l'emploi~Des seuls germes pathogènes~Des lois uniquement~Des prévisions météo", 0,
     "Les conditions de vie et de travail influencent fortement la santé."),
 QC("Que désigne le gradient social de santé ?", "Une santé identique pour tous~Une amélioration progressive de la santé avec la position sociale~Une baisse avec l'âge seulement~Un écart uniquement géographique", 1,
     "Le gradient décrit des écarts réguliers selon la position sociale."),
 QC("Quel facteur accroît la vulnérabilité sanitaire ?", "Un logement insalubre~Un revenu stable~Un réseau de soutien~Un accès facile aux soins", 0,
     "Les conditions de logement font partie des déterminants de la santé."),
 QC("Qu'est-ce que le renoncement aux soins ?", "Une guérison spontanée~Le fait de ne pas accéder à des soins nécessaires~Un type de prévention~Une obligation légale", 1,
     "Le renoncement traduit un renoncement effectif ou subi à des soins utiles."),
 QC("Comment la démographie influence-t-elle l'accès aux services ?", "Elle n'a aucun effet~Elle modifie l'offre et les délais selon les territoires~Elle supprime les besoins~Elle remplace les politiques", 1,
     "La répartition de la population influe sur l'implantation des services."),
 QC("Quel est l'objectif des politiques de réduction des inégalités ?", "Uniformiser les revenus~Améliorer la prévention et l'accès aux droits~Supprimer les services locaux~Réduire l'espérance de vie", 1,
     "Elles visent à réduire les écarts par l'accès aux droits et à la prévention."),
 QC("Comment adapter l'accompagnement à ces inégalités ?", "En ignorant les contraintes~En tenant compte des ressources et des obstacles de la personne~En imposant une solution unique~En jugeant la personne", 1,
     "L'accompagnement tient compte des ressources réelles de chacun."),
 QT("Expliquer ce que sont les inégalités sociales de santé et comment elles se mesurent.",
     "Les inégalités sociales de santé désignent des écarts systématiques d'état de santé entre groupes sociaux. Elles se mesurent par des indicateurs comme l'espérance de vie, la mortalité, la morbidité ou le recours aux soins, en comparant des catégories socioprofessionnelles, des niveaux de revenu ou des territoires. Le gradient social montre que ces écarts sont progressifs : plus la position sociale est élevée, plus la santé est bonne en moyenne. Ces écarts s'expliquent par les déterminants sociaux : logement, emploi, revenu, instruction, accès aux services et environnement. Ils ne signifient pas que chaque personne est malade ou en bonne santé, mais qu'un risque moyen pèse sur un groupe. Pour le professionnel, ces données servent à repérer les publics vulnérables et à adapter l'action : information sur les droits, accompagnement dans les démarches et travail en réseau avec les acteurs locaux.",
     "On définit les écarts, on cite des indicateurs et on relie aux déterminants sociaux."),
 QT("Une personne renonce à se faire soigner faute de ressources. Comment analyser la situation et orienter l'accompagnement ?",
     "On analyse d'abord la situation sans porter de jugement : quels soins sont nécessaires, quel est le coût restant à charge, quels droits sont ouverts et quels obstacles existent, comme la méconnaissance des dispositifs, les délais ou la peur des démarches. On vérifie la couverture maladie et les aides possibles, puis on oriente vers le bon interlocuteur : service social, travailleur social, médiation ou dispositif local d'accès aux soins. L'accompagnement combine information claire, aide concrète aux démarches et respect du rythme de la personne. On vérifie la compréhension par reformulation et on trace les étapes. En parallèle, on transmet les difficultés structurelles repérées au responsable et aux partenaires, car un renoncement individuel révèle souvent un problème d'accès plus large, qui relève de la veille et de l'action collective.",
     "On attend analyse des obstacles, mobilisation des droits et des partenaires, puis retour collectif.")],
C("La santé n'est pas seulement biologique : les conditions de vie créent des écarts que le professionnel doit repérer.",
  "Revenu + logement + emploi + instruction = déterminants de santé",
  "Gradient social · inégalités · renoncement aux soins · vulnérabilité",
  "Déterminants~Conditions de vie et de travail~Gradient~Écart selon la position~Mesure~Espérance de vie et morbidité~Précarité~Risque accru~Politique~Réduction des écarts",
  "Repérer les conditions de vie de la personne|Identifier les ressources et les obstacles|Vérifier les droits ouverts|Orienter vers les dispositifs adaptés|Tracer et transmettre les difficultés collectives",
  "Juger la personne pour son état de santé~Ignorer le renoncement aux soins~Proposer une solution unique~Confondre pauvreté et absence de besoin",
  "Renoncement~Soin non réalisé~Droit~Couverture et aide~Orientation~Service social~Analyse~Obstacle structurel",
  "Inégalités sociales~Écarts entre groupes~Inégalités territoriales~Écarts entre lieux",
  "Prévention~Agir avant la maladie~Curatif~Agir après le diagnostic"))

# ============================================================ SS3
add("SS3", "Analyse de la demande et du besoin social", "Sciences sanitaires et sociales", ["BTS1"],
S("La demande est ce que la personne exprime directement ; le besoin est ce qui est nécessaire à son accompagnement."
  "|La demande explicite est formulée clairement lors de l'accueil ou de l'entretien."
  "|La demande implicite se déduit d'éléments non dits, de comportements ou de contexte."
  "|Le besoin peut être plus large que la demande : la personne ne formule pas toujours ce dont elle a besoin."
  "|L'analyse de la demande distingue le problème posé, les attentes et les priorités de la personne."
  "|L'écoute active et la reformulation permettent de vérifier la compréhension."
  "|Les questions ouvertes favorisent l'expression, les questions fermées précisent un point."
  "|Le professionnel observe le contexte de vie, les ressources et les difficultés associées."
  "|Il distingue ce qui relève de son rôle et ce qui nécessite un autre partenaire."
  "|Le diagnostic social synthétise les informations recueillies sans étiqueter la personne."
  "|Un plan d'accompagnement est construit avec la personne, pas à sa place."
  "|La réévaluation régulière adapte l'action à l'évolution de la situation."),
[QC("Quelle différence existe entre demande et besoin ?", "Ils sont toujours identiques~La demande est exprimée, le besoin est ce qui est réellement nécessaire~Le besoin est toujours écrit~La demande vient toujours du professionnel", 1,
     "La demande est ce que la personne dit ; le besoin peut être plus large."),
 QC("Qu'est-ce qu'une demande implicite ?", "Une demande non formulée mais déductible du contexte~Une demande écrite~Une demande refusée~Une demande administrative", 0,
     "Elle se déduit de comportements, de silences ou d'éléments de contexte."),
 QC("Quel type de question favorise l'expression libre ?", "La question fermée~La question ouverte~La question suggestive~La question accusatrice", 1,
     "La question ouverte laisse la personne présenter sa situation."),
 QC("À quoi sert la reformulation ?", "À imposer une réponse~À vérifier la compréhension de ce qui a été entendu~À clore l'entretien~À juger la demande", 1,
     "La reformulation valide ou corrige ce que le professionnel a compris."),
 QC("Que contient un diagnostic social ?", "Une étiquette définitive~Une synthèse des informations sans jugement de valeur~Le seul avis du responsable~Une prédiction certaine", 1,
     "Il synthétise les éléments recueillis et reste réversible."),
 QC("Qui construit le plan d'accompagnement ?", "Le professionnel seul~La personne avec le professionnel~La direction seule~Le partenaire uniquement", 1,
     "Le plan est co-construit pour être accepté et suivi."),
 QC("Pourquoi réévaluer régulièrement l'accompagnement ?", "Pour le rendre obligatoire~Pour l'adapter à l'évolution de la situation~Pour supprimer le dossier~Pour éviter tout partenariat", 1,
     "La situation évolue : l'action doit être ajustée."),
 QT("Décrire la démarche d'analyse d'une demande depuis l'accueil jusqu'au plan d'accompagnement.",
     "L'accueil crée un cadre d'écoute : on se présente, on explique le rôle du service et on garantit la confidentialité. On laisse la personne exposer sa situation avec des questions ouvertes, puis on précise les faits avec des questions fermées. On reformule régulièrement pour vérifier la compréhension et on observe le contexte : logement, ressources, entourage, démarches en cours. On distingue alors la demande explicite, les demandes implicites et les besoins qui n'ont pas été formulés. On identifie ce qui relève du service et ce qui doit être confié à un partenaire. Le diagnostic social synthétise ces éléments sans étiquette. Enfin, on construit avec la personne des objectifs réalisables, des actions, des responsables et des échéances. Un rendez-vous de réévaluation est prévu pour ajuster le plan.",
     "On attend accueil, écoute, distinction demande et besoin, diagnostic et plan co-construit."),
 QT("Une personne demande uniquement une aide financière, mais l'entretien révèle un isolement important. Que faire ?",
     "On ne réduit pas la situation à la demande financière, mais on ne l'ignore pas non plus : elle est le point d'entrée et doit être traitée. On poursuit l'entretien avec des questions ouvertes sur les conditions de vie, le réseau de soutien et les difficultés rencontrées, en restant attentif à ne pas imposer son interprétation. On reformule ce qui a été compris et on demande confirmation de l'isolement décrit. On explique ensuite les aides financières possibles et on propose, avec l'accord de la personne, une orientation vers un service ou un partenaire qui travaille sur le lien social. Les objectifs sont hiérarchisés avec elle : urgence financière d'abord, puis accompagnement plus large. On trace les actions et on prévoit une réévaluation, car l'isolement peut évoluer.",
     "On traite la demande tout en explorant le besoin plus large, avec accord et traçabilité.")],
C("Une demande est un point d'entrée : l'accompagnement commence quand on a compris le besoin réel.",
  "Demande exprimée + observation + reformulation = besoin identifié",
  "Écoute active · question ouverte · diagnostic social · co-construction",
  "Demande~Ce que la personne exprime~Besoin~Ce qui est nécessaire~Implicite~Non dit mais déductible~Reformulation~Vérification de la compréhension~Plan~Objectifs et actions",
  "Accueillir et garantir la confidentialité|Laisser exposer avec des questions ouvertes|Préciser les faits et observer le contexte|Reformuler et distinguer demande et besoin|Construire le plan avec la personne",
  "Répondre uniquement à la demande explicite|Imposer son interprétation|Étiqueter la personne dans le dossier|Décider seul des objectifs",
  "Aide financière~Demande formulée~Isolement~Besoin non exprimé~Orientation~Partenaire accepté~Plan~Échéances définies",
  "Question ouverte~Expression libre~Question fermée~Précision d'un fait",
  "Demande~Point d'entrée~Besoin~Ce qui est réellement utile"))

# ============================================================ SS4
add("SS4", "Intégration, exclusion et rupture du lien social", "Sciences sanitaires et sociales", ["BTS2"],
S("L'intégration sociale désigne la participation d'une personne à la vie collective et à des réseaux de soutien."
  "|Elle suppose des liens avec la famille, les pairs, les institutions et le territoire."
  "|L'exclusion sociale résulte d'une accumulation de ruptures et d'accès restreints aux droits."
  "|Elle est un processus progressif, rarement un événement unique."
  "|La rupture du lien social peut suivre un deuil, une maladie, une perte d'emploi ou un déménagement."
  "|Les conséquences concernent la santé mentale, l'estime de soi et l'accès aux soins."
  "|Le travail social vise à restaurer des liens et à réouvrir l'accès aux droits."
  "|La médiation et les groupes de parole sont des dispositifs de reconstruction du lien."
  "|Le partenariat associatif et institutionnel élargit les possibilités d'accompagnement."
  "|La personne reste actrice de son réseau : le professionnel ne substitue pas ses liens."
  "|La mesure de l'exclusion repose sur des indicateurs sociaux et sur l'écoute de la personne."
  "|Le référentiel BTS SP3S lie ces notions à l'identité sociale et à l'analyse du besoin."),
[QC("Qu'est-ce que l'intégration sociale ?", "Le fait de vivre seul~La participation à la vie collective et à des réseaux~Une obligation administrative~Un revenu garanti", 1,
     "L'intégration se mesure aux liens et à la participation."),
 QC("Comment l'exclusion sociale s'installe-t-elle ?", "Toujours brutalement~Progressivement par accumulation de ruptures~Par choix unique~Par une seule décision", 1,
     "C'est un processus qui s'installe dans le temps."),
 QC("Quel événement peut déclencher une rupture du lien social ?", "Une perte d'emploi~Une promotion~Un simple loisir~Une visite familiale", 0,
     "Les transitions difficiles peuvent rompre les réseaux de soutien."),
 QC("Quelle conséquence de l'exclusion sur la santé ?", "Une amélioration automatique~Une dégradation de la santé mentale et de l'estime de soi~Aucun effet~Une guérison", 1,
     "L'isolement et la perte de reconnaissance affectent la santé."),
 QC("Quel dispositif vise à reconstruire le lien ?", "La médiation et les groupes de parole~Le silence et l'évitement~Une décision unilatérale~La fermeture du service", 0,
     "Ces dispositifs recréent des espaces d'échange et de reconnaissance."),
 QC("Quel rôle le professionnel doit-il éviter ?", "Faciliter le réseau de la personne~Substituer ses propres liens à ceux de la personne~Orienter vers un partenaire~Écouter la situation", 1,
     "Il accompagne la personne sans prendre sa place dans son réseau."),
 QC("Comment mesurer l'exclusion sociale ?", "Uniquement par le revenu~Par des indicateurs sociaux et l'écoute de la personne~Par la seule apparence~Par le hasard", 1,
     "Les indicateurs et le récit de la personne se complètent."),
 QT("Expliquer la différence entre intégration et exclusion sociale et montrer leur caractère progressif.",
     "L'intégration sociale désigne la présence de liens et la participation à la vie collective : famille, pairs, travail, institutions et territoire. L'exclusion sociale désigne l'affaiblissement ou la rupture de ces liens, associé à un accès restreint aux droits et aux ressources. Ces deux situations ne sont pas figées : une personne peut être bien intégrée puis perdre progressivement ses soutiens après une maladie, un deuil ou une perte d'emploi. À l'inverse, un accompagnement peut restaurer des liens et rouvrir des droits. Le caractère progressif est important pour l'action professionnelle : repérer les premiers signes de retrait, comme la diminution des sorties ou l'abandon des démarches, permet d'agir avant l'installation d'une exclusion durable. Le travail social vise alors à soutenir les liens existants et à en créer de nouveaux avec l'accord de la personne.",
     "On définit les deux notions et on montre qu'elles évoluent dans le temps."),
 QT("Une personne âgée isolée refuse de participer à un groupe de parole. Comment accompagner sans forcer ?",
     "Le refus est une information : il peut exprimer une peur du regard des autres, une fatigue, une habitude de vie solitaire ou une mauvaise expérience. On ne le traite pas comme un obstacle à surmonter. On commence par écouter les raisons sans les discuter, en reformulant ce qui est compris. On propose des alternatives plus douces : une visite à domicile, un échange téléphonique, une sortie individuelle ou la rencontre d'une seule personne de confiance. On explique le fonctionnement du groupe et la présence d'un animateur pour réduire l'inquiétude. La personne conserve le choix et peut décider plus tard. On suit l'évolution avec elle et on note dans le dossier les propositions faites et sa réponse. On vérifie aussi si d'autres besoins, comme le logement ou la santé, sont prioritaires avant de travailler sur le lien social.",
     "On respecte le refus, on cherche les raisons, on propose des alternatives et on garde la personne actrice.")],
C("L'accompagnement vise à restaurer des liens, jamais à remplacer la personne dans son propre réseau.",
  "Liens + droits + reconnaissance = intégration",
  "Exclusion progressive · rupture · médiation · partenariat",
  "Intégration~Liens et participation~Exclusion~Accumulation de ruptures~Rupture~Événement ou transition~Conséquence~Santé mentale et estime~Réponse~Médiation et partenariat",
  "Repérer l'état du réseau et des liens|Écouter le récit et les ruptures|Identifier les droits non exercés|Proposer des dispositifs adaptés|Respecter le choix et suivre l'évolution",
  "Forcer la participation à un groupe~Confondre solitude et exclusion définitive~Remplacer les liens de la personne~Ignorer les signes de retrait",
  "Refus~Groupe de parole~Écoute~Raison du refus~Alternative~Visite individuelle~Dossier~Choix tracé",
  "Intégration~Présence de liens~Exclusion~Rupture des liens",
  "Médiation~Restaurer l'échange~Substitution~Prendre la place de la personne"))

# ============================================================ SS5
add("SS5", "Parcours de vie, famille et accompagnement social", "Sciences sanitaires et sociales", ["BTS2"],
S("Un parcours de vie est une succession de transitions et d'événements qui marquent l'existence d'une personne."
  "|Les grandes transitions sont l'enfance, la scolarité, l'entrée dans l'emploi, la parentalité et la retraite."
  "|Chaque transition peut être un moment d'opportunité ou de vulnérabilité."
  "|Les parcours sont influencés par les ressources familiales, sociales et territoriales."
  "|La famille constitue un réseau de soutien, mais peut aussi être source de tension."
  "|L'accompagnement tient compte de la place de la personne dans sa famille et de ses responsabilités."
  "|La notion de genre et de génération aide à comprendre les rôles et les attentes."
  "|Les situations de dépendance imposent d'organiser la continuité entre domicile et établissement."
  "|Le projet d'accompagnement s'inscrit dans le parcours et non contre lui."
  "|Les dispositifs coordonnent les interventions de plusieurs professionnels autour de la personne."
  "|La personne conserve la maîtrise de son parcours autant que possible."
  "|Le référentiel BTS SP3S relie ces savoirs à l'identité sociale et à l'analyse de la demande."),
[QC("Qu'est-ce qu'un parcours de vie ?", "Une succession de transitions et d'événements~Un simple dossier administratif~Une décision unique~Une statistique", 0,
     "Le parcours est une trajectoire faite de transitions successives."),
 QC("Quelle transition peut être un moment de vulnérabilité ?", "L'entrée dans l'emploi~Un jour ordinaire~Une lecture~Un repas", 0,
     "Les transitions sont des moments où les ressources peuvent être fragilisées."),
 QC("Quel facteur influence les parcours ?", "Les ressources familiales et sociales~Le seul hasard~La météo~L'avis d'un voisin", 0,
     "Les ressources et le territoire orientent les possibilités."),
 QC("Quel rôle la famille peut-elle jouer ?", "Toujours un soutien~Un soutien ou une source de tension~Aucun rôle~Un rôle uniquement financier", 1,
     "La famille est un réseau ambivalent, à écouter sans présupposé."),
 QC("Que doit respecter un projet d'accompagnement ?", "Le seul avis du professionnel~Le parcours et les attentes de la personne~La procédure sans exception~L'avis de la direction seule", 1,
     "Le projet s'inscrit dans l'histoire de la personne."),
 QC("Pourquoi coordonner plusieurs professionnels ?", "Pour éviter toute transversalité~Pour assurer la continuité entre les interventions~Pour réduire le nombre de dossiers~Pour supprimer le partenariat", 1,
     "La coordination évite les ruptures entre domicile, service et établissement."),
 QC("Quelle posture est attendue face au parcours d'une personne ?", "Décider à sa place~Respecter sa maîtrise autant que possible~Ignorer son histoire~Imposer un modèle unique", 1,
     "La personne reste actrice de son parcours."),
 QT("Expliquer l'intérêt de la notion de parcours de vie dans un accompagnement social.",
     "La notion de parcours de vie permet de comprendre la situation actuelle d'une personne à partir de son histoire et de ses transitions. Elle évite de réduire la personne à un problème immédiat : un besoin d'hébergement, par exemple, s'explique souvent par une succession d'événements, une rupture professionnelle, une séparation ou une perte de soutien familial. Elle aide à repérer les moments où une intervention est pertinente, comme une transition vers la retraite ou l'arrivée d'un enfant, et à identifier les ressources déjà mobilisées. Elle invite aussi à respecter la chronologie et les projets de la personne, plutôt que d'imposer un parcours standard. Enfin, elle facilite la coordination entre professionnels : chacun intervient sur un moment du parcours, avec une lecture commune et un objectif partagé.",
     "On montre que le parcours donne du sens à la situation présente et guide l'action."),
 QT("Une personne doit quitter son domicile pour entrer en établissement. Comment organiser la continuité du parcours ?",
     "On prépare la transition suffisamment à l'avance avec la personne et sa famille, en expliquant les raisons de l'orientation, les modalités d'accueil et les droits conservés. On recueille son histoire, ses habitudes, ses attentes et les personnes importantes pour elle, afin d'éviter une rupture brutale. On organise une visite préalable et un temps d'adaptation progressif si cela est possible. On coordonne les professionnels du domicile et de l'établissement : transmission d'informations utiles, dossier de liaison, médicaments, documents et rendez-vous de suivi. La famille est associée dans la mesure souhaitée par la personne, qui reste décisionnaire. On prévoit un temps d'évaluation après l'arrivée pour ajouter les ajustements nécessaires et vérifier que le projet d'accompagnement respecte le parcours vécu.",
     "On attend préparation, implication de la personne, coordination des acteurs et évaluation après l'admission.")],
C("Un accompagnement réussi s'inscrit dans l'histoire de la personne et coordonne les moments du parcours.",
  "Transitions + ressources + projet = parcours accompagné",
  "Parcours de vie · famille · continuité · coordination",
  "Parcours~Suite de transitions~Transition~Moment de changement~Famille~Soutien et tension~Ressources~Appuis disponibles~Coordination~Continuité des interventions",
  "Recueillir l'histoire et les transitions vécues|Identifier les ressources et les tensions|Écouter les attentes de la famille|Coordonner les professionnels du domicile et de l'établissement|Évaluer après la transition",
  "Réduire la personne à sa situation actuelle~Imposer un parcours standard~Décider à la place de la personne~Négliger la famille sans l'écouter",
  "Domicile~Lieu de vie initial~Établissement~Nouveau cadre~Liaison~Dossier et transmissions~Ajustement~Après l'admission",
  "Continuité~Lien maintenu dans le temps~Rupture~Arrêt brutal du suivi",
  "Projet personnel~Souhait de la personne~Projet institutionnel~Cadre du service"))

# ============================================================ TP1
add("TP1", "Accueil de la personne et logistique administrative", "Techniques de prévention et d'accompagnement", ["BTS1"],
S("L'accueil est le premier contact entre une personne et un service sanitaire ou social."
  "|Il donne une image de l'établissement et conditionne la qualité de la relation."
  "|Les objectifs sont d'informer, d'orienter et de mettre la personne en confiance."
  "|L'accueil physique comporte une présentation, une écoute et une vérification de la compréhension."
  "|L'accueil téléphonique exige une identité du service claire et une attitude attentive."
  "|La posture professionnelle associe disponibilité, neutralité et discrétion."
  "|Les documents d'accueil comprennent le livret, le règlement et les formulaires utiles."
  "|La logistique administrative gère les rendez-vous, les dossiers, les courriers et les archives."
  "|La traçabilité des échanges permet d'assurer la continuité du service."
  "|Les données personnelles collectées doivent être nécessaires et protégées."
  "|Un accueil adapté tient compte du handicap, de la langue et de l'urgence éventuelle."
  "|Le référentiel BTS SP3S place ces techniques dans le domaine 1 de ses activités professionnelles."),
[QC("Quel est le premier objectif de l'accueil ?", "Informer, orienter et mettre en confiance~Remplir tous les formulaires~Contrôler la personne~Clore le dossier", 0,
     "L'accueil crée les conditions de la relation et de l'orientation."),
 QC("Quelle attitude caractérise un accueil professionnel ?", "Disponibilité, neutralité et discrétion~Curiosité et familiarité~Silence total~Jugement immédiat", 0,
     "Ces trois dimensions cadrent la posture professionnelle."),
 QC("Quel document est remis lors de l'accueil ?", "Le livret d'accueil~Le bilan financier~Le rapport annuel~Le registre des achats", 0,
     "Le livret d'accueil informe sur les droits et le fonctionnement."),
 QC("Que comprend la logistique administrative ?", "Les seuls rendez-vous~Les dossiers, courriers, rendez-vous et archives~Le nettoyage des locaux~La cuisine", 1,
     "Elle couvre l'ensemble des supports et circuits administratifs."),
 QC("Quel principe s'applique aux données collectées à l'accueil ?", "Collecter le maximum d'informations~Collecter le nécessaire et protéger les données~Tout noter sans tri~Partager avec tous", 1,
     "La minimisation et la protection des données sont obligatoires."),
 QC("Comment adapter l'accueil à une personne en situation de handicap ?", "En ignorant la différence~En tenant compte de ses besoins de communication et d'accessibilité~En parlant à sa place~En supprimant l'accueil", 1,
     "L'accessibilité et l'adaptation de la communication sont essentielles."),
 QC("Pourquoi tracer les échanges d'accueil ?", "Pour assurer la continuité et le suivi~Pour éviter toute transmission~Pour augmenter les formalités~Pour supprimer le dossier", 0,
     "La trace permet à un autre professionnel de reprendre le suivi."),
 QT("Décrire les étapes d'un accueil physique de qualité dans un service social.",
     "L'accueil commence par une attention à l'environnement : un espace identifiable, propre et accessible. Le professionnel se présente, précise son rôle et laisse la personne exposer sa demande sans l'interrompre. Il écoute, reformule pour vérifier sa compréhension et pose des questions ouvertes puis fermées pour préciser les faits. Il informe sur les prestations du service, les délais, les documents utiles et les droits de la personne, avec un langage clair et adapté. Il vérifie que la personne a compris, notamment en cas de handicap ou de barrière linguistique. Il oriente vers le bon interlocuteur ou prend rendez-vous, puis trace l'échange dans le dossier selon la procédure. Il respecte la confidentialité et évite toute remarque dévaluante. Une attention particulière est portée aux situations d'urgence.",
     "On attend présentation, écoute, information adaptée, orientation et traçabilité."),
 QT("Un usager arrive en colère parce qu'il a déjà appelé trois fois sans réponse. Comment gérer l'accueil ?",
     "On accueille la colère sans la prendre personnellement et sans la minimiser : on écoute jusqu'au bout, avec une posture calme et une attitude ouverte. On reformule le ressenti et les faits : trois appels restés sans réponse et une attente vécue comme injuste. On s'excuse pour la difficulté rencontrée, sans promettre ce qui ne dépend pas de soi. On vérifie le dossier et les traces des appels, puis on explique ce qui s'est passé et ce qui peut être fait maintenant, avec un interlocuteur identifié et une échéance précise. Si la situation dépasse le cadre local, on saisit le responsable selon la procédure. On trace la réclamation et on propose un retour d'information. Enfin, on transmet l'incident en réunion de service pour corriger le circuit, car une plainte répétée révèle souvent une organisation défaillante.",
     "On attend écoute de la colère, faits vérifiés, réponse concrète, trace et correction collective.")],
C("Un bon accueil ne se limite pas à la politesse : il informe, oriente et laisse une trace fiable.",
  "Écoute + information adaptée + orientation + traçabilité = accueil de qualité",
  "Livret d'accueil · neutralité · accessibilité · protection des données",
  "Accueil~Premier contact avec le service~Écoute~Compréhension de la demande~Information~Droits et prestations~Orientation~Vers le bon interlocuteur~Trace~Suivi et continuité",
  "Préparer un espace accessible et identifiable|Se présenter et laisser exposer la demande|Reformuler et préciser les faits|Informer et vérifier la compréhension|Orienter et tracer l'échange",
  "Parler à la place de la personne~Promettre sans vérifier~Laisser une donnée non protégée~Ignorer la colère de l'usager",
  "Appels répétés~Réclamation~Excuse~Reconnaissance du désagrément~Interlocuteur~Réponse identifiée~Circuit~Correction en service",
  "Accueil physique~Présence et échange~Accueil téléphonique~Voix et disponibilité",
  "Information~Comprendre la situation~Orientation~Vers le bon service"))

# ============================================================ TP2
add("TP2", "L'entretien d'accompagnement social", "Techniques de prévention et d'accompagnement", ["BTS2"],
S("L'entretien est un outil central de l'accompagnement social et médico-social."
  "|Il se déroule en trois temps : l'ouverture, le développement et la clôture."
  "|L'ouverture présente le cadre, le rôle du professionnel et les règles de confidentialité."
  "|Le développement laisse la personne présenter sa situation et ses attentes."
  "|Les questions ouvertes favorisent l'expression, les questions fermées précisent les faits."
  "|La reformulation vérifie la compréhension sans imposer une interprétation."
  "|Le silence est un outil : il laisse un temps de réflexion à la personne."
  "|L'observance du cadre comprend la durée, le lieu et le respect du rythme."
  "|La posture professionnelle associe écoute, neutralité et non-jugement."
  "|La clôture résume les points compris et les actions décidées avec la personne."
  "|La note d'entretien trace les éléments utiles, de manière factuelle et confidentielle."
  "|Le référentiel BTS SP3S associe ces techniques à l'accueil et à l'accompagnement de la personne."),
[QC("Quels sont les trois temps d'un entretien ?", "Ouverture, développement, clôture~Accueil, repas, départ~Question, réponse, silence~Lecture, écriture, archive", 0,
     "Le déroulement classique comprend ouverture, développement et clôture."),
 QC("Que précise l'ouverture de l'entretien ?", "Le prix du service~Le cadre, le rôle et la confidentialité~La météo~L'avis du voisin", 1,
     "Le cadre et la confidentialité sont présentés dès le début."),
 QC("Quel type de question laisse la personne présenter librement ?", "La question fermée~La question ouverte~La question suggestive~La question accusatrice", 1,
     "La question ouverte ouvre l'expression sans orienter."),
 QC("À quoi sert la reformulation ?", "À conclure l'entretien~À vérifier la compréhension~À juger la réponse~À remplir le dossier", 1,
     "Elle permet de confirmer ou de corriger ce qui a été compris."),
 QC("Quel est l'effet du silence dans un entretien ?", "Il bloque la parole~Il laisse un temps de réflexion~Il indique un désaccord~Il remplace l'écoute", 1,
     "Le silence respecte le rythme de la personne."),
 QC("Que doit faire la clôture de l'entretien ?", "Résumer les points compris et les actions décidées~Imposer une nouvelle date~Interrompre brutalement~Éviter toute synthèse", 0,
     "La synthèse partagée sécurise la suite de l'accompagnement."),
 QC("Comment rédiger une note d'entretien ?", "Avec des jugements personnels~De manière factuelle et confidentielle~Avec tous les détails entendus~Sans aucune trace", 1,
     "Elle est factuelle, utile et protégée."),
 QT("Expliquer le déroulement d'un entretien d'accompagnement et l'intérêt de chaque temps.",
     "L'ouverture installe le cadre : le professionnel se présente, explique son rôle, la durée prévue et la règle de confidentialité. Ce temps sécurise la personne et évite les malentendus. Le développement est consacré à l'expression : le professionnel écoute, utilise des questions ouvertes, puis des questions fermées pour préciser, et reformule régulièrement pour vérifier sa compréhension. Il respecte les silences et évite les interprétations hâtives. La clôture résume avec la personne les éléments compris, les actions retenues, les responsables et les échéances ; elle vérifie que la personne est d'accord. Une note factuelle est ensuite rédigée et versée au dossier. Cette structure protège la qualité de l'échange et la continuité du suivi.",
     "On attend les trois temps et le rôle de chacun, ainsi que la trace écrite."),
 QT("Pendant un entretien, la personne se tait longuement après une question sur sa famille. Quelle est la bonne attitude ?",
     "Le silence n'est pas un échec : il peut exprimer une émotion, une réflexion ou une difficulté à parler. Le professionnel ne le comble pas immédiatement par une autre question ni par une interprétation. Il garde une posture ouverte, note le non-dit sans en tirer une conclusion et laisse le temps nécessaire. Après un moment, il peut reformuler prudemment ce qu'il a perçu en demandant confirmation : « je sens que ce sujet est difficile pour vous, souhaitez-vous en parler ou passer à autre chose ? ». Il respecte le choix de la personne et peut proposer de revenir sur le sujet lors d'un prochain entretien. Il trace dans la note le fait que le sujet a été abordé et la réponse donnée, sans spéculer sur son contenu.",
     "On respecte le silence, on propose sans forcer et on trace sans interpréter.")],
C("L'entretien est un cadre : il protège la parole de la personne et rend le suivi lisible.",
  "Ouverture + écoute + reformulation + clôture = entretien conduit",
  "Question ouverte · silence · non-jugement · note factuelle",
  "Ouverture~Cadre et confidentialité~Développement~Expression de la personne~Question ouverte~Expression libre~Reformulation~Vérification~Clôture~Synthèse partagée",
  "Présenter le cadre et le rôle|Laisser la personne exposer|Préciser avec des questions fermées|Reformuler et respecter les silences|Résumer et tracer l'entretien",
  "Interrompre un silence trop vite~Interpréter à la place de la personne~Juger les propos entendus~Rédiger une note subjective",
  "Silence~Temps de réflexion~Reformulation~Confirmation demandée~Sujet difficile~Possibilité de différer~Note~Fait constaté",
  "Question ouverte~Laisse l'expression~Question fermée~Précise un fait",
  "Écoute~Compréhension de la personne~Interprétation~Lecture imposée"))

# ============================================================ TP3
add("TP3", "Gestion du dossier usager et circuits administratifs", "Techniques de prévention et d'accompagnement", ["BTS1"],
S("Le dossier usager rassemble les informations utiles à l'accompagnement et au suivi."
  "|Il garantit la continuité entre professionnels et entre services."
  "|Son contenu est défini par la réglementation et par la procédure de l'établissement."
  "|Les pièces courantes sont l'identité, la situation sociale, les prestations et les comptes rendus."
  "|Les informations doivent être exactes, datées et pertinentes pour l'accompagnement."
  "|Le dossier est un outil de travail, pas un fichier de curiosité."
  "|L'accès est limité aux professionnels habilités et à la personne concernée."
  "|La conservation et l'archivage suivent des durées réglementaires."
  "|Les transmissions écrites et orales évitent la duplication et la contradiction."
  "|Le dossier informatisé impose des mots de passe individuels et une traçabilité des accès."
  "|Les erreurs sont corrigées selon la procédure, sans effacer l'historique utile."
  "|Le référentiel BTS SP3S rattache cette gestion à la logistique administrative du domaine 1."),
[QC("Quelle est la fonction principale du dossier usager ?", "Conserver des souvenirs personnels~Assurer la continuité du suivi~Réduire le nombre d'agents~Remplacer l'entretien", 1,
     "Le dossier sert la continuité et la coordination."),
 QC("Qui peut accéder au dossier ?", "Tout le personnel~Les professionnels habilités et la personne concernée~Les voisins~Les fournisseurs", 1,
     "L'accès est strictement limité et justifié."),
 QC("Quelle qualité doit avoir une information versée au dossier ?", "Être drôle~Être exacte, datée et utile~Être secrète même pour l'équipe~Être longue", 1,
     "L'information est fiable, datée et pertinente."),
 QC("Que sont les transmissions ?", "Des échanges entre professionnels pour assurer le suivi~Des repas~Des documents publicitaires~Des sanctions", 0,
     "Elles évitent la rupture entre les équipes."),
 QC("Quelle règle s'applique au dossier informatisé ?", "Un mot de passe partagé~Un mot de passe individuel et des accès tracés~Aucun mot de passe~Un accès public", 1,
     "La sécurité repose sur l'identification de chacun."),
 QC("Que faire en cas d'erreur dans le dossier ?", "Effacer l'historique~Corriger selon la procédure en gardant les éléments utiles~Ignorer l'erreur~Changer de dossier", 1,
     "La correction est tracée et l'historique reste lisible."),
 QC("Que signifie la durée de conservation ?", "Le dossier est gardé éternellement~Une durée réglementaire est fixée pour les archives~Le dossier est détruit immédiatement~La durée dépend du hasard", 1,
     "Les archives ont une durée légale de conservation."),
 QT("Expliquer les règles de tenue d'un dossier usager et leur intérêt pour la continuité.",
     "Un dossier usager est structuré selon les rubriques définies par l'établissement : identité, situation, prestations, comptes rendus et actions. Chaque information est datée, attribuée à son auteur et limitée à ce qui est utile à l'accompagnement. L'accès est réservé aux professionnels habilités, chacun utilisant un identifiant personnel ; les accès informatiques sont tracés. La personne concernée peut exercer ses droits sur les données la concernant. Les transmissions orales et écrites complètent le dossier sans le remplacer et évitent les contradictions entre services. Les durées de conservation sont respectées pour les archives. Ces règles protègent la confidentialité, garantissent la fiabilité des informations et permettent à un professionnel qui reprend le suivi de comprendre l'historique sans interroger à nouveau la personne sur des éléments déjà connus.",
     "On attend structure, exactitude, accès restreint, traçabilité et intérêt pour la continuité."),
 QT("Un collègue vous demande de consulter le dossier d'un usager qu'il ne suit pas, par simple curiosité. Que répondez-vous ?",
     "On refuse sans détour, en rappelant que l'accès au dossier dépend de l'habilitation et de la finalité de l'accompagnement, pas du seul statut de collègue. On propose le circuit prévu : si le collègue a besoin d'une information pour une prise en charge, il formalise sa demande auprès du responsable, qui vérifie la pertinence et autorise la transmission du minimum nécessaire. On peut donner une information générale sur la procédure sans révéler d'élément personnel. On trace la demande inhabituelle selon la règle interne et, si la demande devient insistante ou vise un usage étranger au service, on en réfère au responsable. Le refus est expliqué avec calme, sans accusation : la règle protège la personne et l'ensemble de l'équipe.",
     "On refuse, on propose le circuit habilité, on évite l'accusation et on trace l'incident.")],
C("Le dossier est un outil de continuité et de preuve : son accès est un privilège encadré.",
  "Information exacte + accès habilité + traçabilité = dossier fiable",
  "Transmissions · conservation · mot de passe individuel · droit d'accès",
  "Dossier~Outil de suivi~Contenu~Pièces utiles et datées~Accès~Professionnels habilités~Transmission~Continuité entre équipes~Archive~Durée réglementaire",
  "Vérifier la rubrique et la pertinence de l'information|dater et identifier l'auteur|Limiter l'accès aux personnes habilitées|Tracer les consultations informatiques|Conserver selon la durée prévue",
  "Consulter par curiosité~Partager un mot de passe~Laisser une information contradictoire~Effacer un ancien compte rendu utile",
  "Demande~Curiosité de collègue~Refus~Finalité et habilitation~Circuit~Validation du responsable~Trace~Incident consigné",
  "Dossier papier~Archives physiques~Dossier informatisé~Accès tracé",
  "Transmission~Lien entre professionnels~Isolement~Rupture du suivi"))

# ============================================================ TP4
add("TP4", "Veille documentaire et recherche d'information", "Techniques de prévention et d'accompagnement", ["BTS1"],
S("La veille documentaire consiste à rechercher, sélectionner et suivre des informations utiles."
  "|Elle permet d'actualiser les connaissances professionnelles et de répondre aux besoins d'information."
  "|Les sources utiles sont les textes officiels, les publications professionnelles et les ressources documentaires internes."
  "|La fiabilité d'une source dépend de son auteur, de sa date et de sa finalité."
  "|Une information ancienne peut être caduque,notamment en matière juridique ou sanitaire."
  "|La recherche commence par la définition des mots-clés et du périmètre."
  "|Les moteurs et bases de données donnent des résultats à évaluer, pas à recopier."
  "|La sélection retient les documents pertinents, récents et accessibles."
  "|La synthèse reformule l'essentiel en conservant les références précises."
  "|Le plagiat consiste à reprendre un contenu sans citation : il doit être évité."
  "|Les résultats alimentent le dossier, l'information à la personne et la formation de l'équipe."
  "|Le référentiel BTS SP3S associe la veille au domaine 1 des activités professionnelles."),
[QC("Qu'est-ce que la veille documentaire ?", "Une recherche et un suivi d'informations utiles~Une simple lecture de journaux~Un archivage sans tri~Une réunion de service", 0,
     "La veille combine recherche, sélection et suivi."),
 QC("Quel critère rend une source fiable ?", "Sa couleur~Son auteur, sa date et sa finalité~Sa longueur~Le hasard", 1,
     "L'origine, l'actualité et l'objectif d'une source déterminent sa fiabilité."),
 QC("Par quoi commence une recherche documentaire ?", "Par la copie d'un texte~Par la définition des mots-clés et du périmètre~Par la synthèse~Par l'archivage", 1,
     "Cadrer la recherche évite la dispersion."),
 QC("Que faut-il faire des résultats d'un moteur ?", "Les recopier tels quels~Les évaluer avant de les retenir~Les ignorer~Les supprimer", 1,
     "Un résultat est une piste, pas une vérité établie."),
 QC("Que contient une synthèse de qualité ?", "L'essentiel reformulé avec les références~Tout le document original~Une opinion personnelle~Une liste de mots-clés", 0,
     "La synthèse est courte, fidèle et sourcée."),
 QC("Qu'est-ce que le plagiat ?", "Reprendre un contenu sans citation~Citer une source~Synthétiser un texte~Classer un document", 0,
     "Toute reprise non citée est un plagiat."),
 QC("À quoi sert la veille dans un service ?", "À actualiser les pratiques et informer les usagers~À supprimer les dossiers~À éviter toute formation~À remplacer le responsable", 0,
     "Elle alimente la qualité et l'information des personnes."),
 QT("Décrire une démarche de veille documentaire fiable sur un sujet sanitaire ou social.",
     "On commence par cadrer le besoin : quelle question, quel public et quelle échéance. On définit des mots-clés et un périmètre, puis on identifie les sources pertinentes : textes officiels, circulaires, publications professionnelles, base documentaire interne. On consulte les documents en vérifiant systématiquement l'auteur, la date de publication et la finalité : un texte ancien peut être caduque, notamment en droit ou en santé. On compare plusieurs sources pour repérer les convergences et les divergences. On retient les éléments utiles et on rédige une synthèse courte qui reformule sans recopier, en citant précisément les références. On classe le résultat dans le dossier ou le support d'information de l'équipe, et on prévoit une date de révision. On transmet enfin les points saillants aux collègues concernés.",
     "On attend cadrage, évaluation des sources, synthèse sourcée et diffusion."),
 QT("Un collègue vous transmet un document trouvé en ligne sans date ni auteur. L'utiliserez-vous pour une note d'information ?",
     "On ne l'utilise pas tel quel : l'absence d'auteur et de date empêche d'évaluer la fiabilité et l'actualité du contenu. On tente d'abord de retrouver la source d'origine, par exemple un rapport officiel cité dans le document, et on vérifie la date de publication sur le site de l'organisme. Si l'origine reste incertaine, on recherche un texte officiel ou une publication reconnue sur le même sujet et on s'appuie sur ceux-ci. Si le document apporte une idée intéressante, on peut la mentionner comme piste à vérifier, sans la présenter comme une référence. Dans la note finale, on cite uniquement des sources identifiées et datées, et on indique la date de mise à jour de l'information. On explique au collègue pourquoi la vérification est nécessaire : une information non sourcée peut induire l'équipe ou la personne accompagnée en erreur.",
     "On refuse une source non vérifiable, on recherche une référence fiable et on cite les sources retenues.")],
C("Une information n'est utile que si sa source et sa date sont connues : la veille est un filtre.",
  "Mots-clés + sources fiables + synthèse sourcée = information utilisable",
  "Textes officiels · auteur · date · citation · révision",
  "Veille~Recherche et suivi~Mot-clé~Cadrage de la recherche~Source~Auteur et date~Synthèse~Reformulation sourcée~Révision~Mise à jour prévue",
  "Cadrer la question et le public|Choisir des mots-clés pertinents|Identifier des sources fiables|Évaluer auteur, date et finalité|Synthétiser, citer et diffuser",
  "Recopier un document sans citation~Utiliser une source non datée~Cumuler les résultats sans tri~Oublier de prévoir une révision",
  "Document sans auteur~Source incertaine~Vérification~Recherche de l'origine~Référence~Texte officiel retenu~Note~Information datée",
  "Information récente~Vérifiée et datée~Information ancienne~Potentiellement caduque",
  "Veille~Surveiller et sélectionner~Copie~Reprise sans esprit critique"))

# ============================================================ TP5
add("TP5", "Prévention et gestion des conflits dans l'accompagnement", "Techniques de prévention et d'accompagnement", ["BTS2"],
S("Un conflit oppose deux personnes ou deux groupes autour de besoins, d'intérêts ou de représentations divergents."
  "|Dans un service social, il peut opposer un usager et un professionnel ou deux collègues."
  "|Les sources fréquentes sont le malentendu, la frustration, la fatigue et le manque d'information."
  "|La prévention passe par la clarté des règles, des rôles et des circuits."
  "|Une communication respectueuse et une écoute en amont réduisent les tensions."
  "|Les signes d'escalade sont le ton sec, le retrait, les interruptions et les remarques dévaluantes."
  "|La première réponse consiste à abaisser la tension par une attitude calme et une reformulation."
  "|La médiation fait intervenir un tiers pour restaurer le dialogue, sans juger."
  "|La personne concernée est associée à la recherche de solution, sans être mise en cause."
  "|La violence verbale ou physique impose de protéger les personnes et d'appliquer la procédure."
  "|L'incident est tracé et analysé en équipe pour éviter sa répétition."
  "|Le référentiel BTS SP3S associe ces techniques à la prévention et à la gestion des conflits."),
[QC("Qu'est-ce qu'un conflit dans un service ?", "Une divergence de besoins ou d'intérêts~Un simple silence~Une procédure administrative~Une bonne entente", 0,
     "Le conflit naît d'une divergence de besoins, d'intérêts ou de représentations."),
 QC("Quelle est une source fréquente de conflit ?", "La clarté des règles~Le malentendu et le manque d'information~L'écoute active~La reformulation", 1,
     "Les malentendus et l'information déficiente alimentent les tensions."),
 QC("Quel signe annonce une escalade ?", "Une reformulation calme~Un ton sec et des interruptions~Une question ouverte~Un silence attentif", 1,
     "Ces signes indiquent une montée de la tension."),
 QC("Quelle première réponse adopter face à la tension ?", "Répondre sur le même ton~Rester calme et reformuler~Quitter le service~Imposer une sanction", 1,
     "Le calme et la reformulation désamorcent l'échange."),
 QC("Quel est le rôle du médiateur ?", "Juger qui a tort~Restaurer le dialogue sans juger~Remplacer le responsable~Supprimer la discussion", 1,
     "Le tiers facilite la parole sans prendre parti."),
 QC("Que faire face à une violence physique ?", "Négocier sans limite~Protéger les personnes et appliquer la procédure~Répondre par la force~Ignorer l'incident", 1,
     "La sécurité prime et la procédure est impérative."),
 QC("Pourquoi tracer un incident ?", "Pour punir systématiquement~Pour analyser et éviter sa répétition~Pour supprimer le dossier~Pour éviter tout retour d'expérience", 1,
     "La trace alimente l'analyse et l'amélioration."),
 QT("Expliquer la différence entre prévention des conflits et gestion d'un conflit installé.",
     "La prévention agit en amont : elle rend les règles, les rôles et les circuits lisibles, elle informe les usagers sur les prestations et les délais, et elle forme les professionnels à l'écoute et à la reformulation. Elle réduit les malentendus, qui sont une cause fréquente de tension. La gestion intervient quand le conflit existe : elle vise à abaisser la tension, à écouter chaque partie, à reformuler les positions et à faire émerger un accord acceptable. Elle peut faire appel à un médiateur. Les deux approches se complètent : un conflit bien géré est analysé en équipe, et cette analyse nourrit la prévention en corrigeant une procédure ou un manque d'information. La personne reste associée à la solution et n'est pas réduite au rôle de fautive.",
     "On distingue l'action en amont et l'action pendant le conflit, puis on montre leur lien."),
 QT("Un usager élève la voix dans l'accueil parce qu'il attend depuis une heure. Que faites-vous ?",
     "On ne répond pas sur le même ton. On garde une posture calme, on se place à distance respectueuse et on formule une phrase courte qui reconnaît l'attente : « vous attendez depuis longtemps, je comprends votre agacement. » On écoute sans couper la parole, puis on reformule les faits et le besoin : un rendez-vous dépassé et une information qui a manqué. On vérifie le dossier et on propose une réponse concrète : nouveau créneau, interlocuteur identifié ou explication du délai. On demande confirmation que la solution convient. Si la voix reste agressive ou si la sécurité est menacée, on applique la procédure interne et on appelle le responsable, sans jamais répliquer. Après le départ, on trace l'incident de façon factuelle et on l'analyse en réunion pour corriger la cause organisationnelle.",
     "On attend calme, reconnaissance, faits vérifiés, solution, escalade si nécessaire et trace.")],
C("Un conflit se prévient par la clarté et se gère par l'écoute : la personne n'est jamais l'ennemie.",
  "Règles claires + écoute + médiation + trace = conflit maîtrisé",
  "Escalade · médiation · protection · retour d'expérience",
  "Conflit~Divergence de besoins~Prévention~Règles et information~Escalade~Signes de tension~Médiation~Tiers neutre~Trace~Analyse en équipe",
  "Repérer les signes de tension|Rester calme et reformuler|Écouter chaque partie sans juger|Rechercher une solution partagée|Tracer et analyser l'incident",
  "Répondre sur le même ton~Juger la personne~Forcer un accord rapide~Omettre la trace de l'incident",
  "Attente prolongée~Agacement exprimé~Reconnaissance~Parole entendue~Solution~Créneau proposé~Incident~Correction organisationnelle",
  "Prévention~Agir en amont~Gestion~Agir pendant le conflit",
  "Médiation~Dialogue restauré~Arbitrage~Décision imposée"))

# ============================================================ AN1
add("AN1", "Lexique professionnel de la santé et du social", "Anglais professionnel", ["BTS1"],
S("L'anglais professionnel est une compétence de l'unité U2 du BTS SP3S."
  "|Il permet de comprendre et d'échanger avec des usagers ou des collègues anglophones."
  "|Le lexique de la santé comprend des termes comme care, patient, treatment et appointment."
  "|Le lexique du social comprend des termes comme support, benefit, housing et social worker."
  "|La prononciation et l'orthographe sont vérifiées pour éviter les malentendus."
  "|Les faux amis sont des mots proches en apparence mais de sens différent."
  "|Les acronymes et les abréviations varient selon les pays et les services."
  "|Un glossaire personnel aide à mémoriser les termes utiles au poste."
  "|La compréhension écrite s'entraîne avec des documents simples comme des courriels ou des formulaires."
  "|L'expression écrite privilégie des phrases courtes et un registre poli."
  "|Les nombres, les dates et les heures sont des sources fréquentes d'erreur."
  "|La reformulation et la question de clarification sécurisent la communication."),
[QC("Quelle unité du BTS SP3S concerne l'anglais professionnel ?", "U1~U2~U5~U6", 1,
    "L'unité U2 porte sur la communication en langue vivante étrangère."),
 QC("Quel mot anglais désigne un rendez-vous ?", "Care~Appointment~Benefit~Housing", 1,
    "Appointment signifie rendez-vous."),
 QC("Quel mot désigne un travailleur social ?", "Social worker~Patient~Nurse~Treatment", 0,
    "Social worker est le terme anglais pour travailleur social."),
 QC("Qu'est-ce qu'un faux ami ?", "Un mot proche en apparence mais de sens différent~Un mot introuvable~Un mot toujours faux~Un mot interdit", 0,
    "La ressemblance apparente peut masquer un sens différent."),
 QC("Que faire face à un acronyme inconnu ?", "Deviner le sens~Demander une précision~L'ignorer~Le traduire mot à mot", 1,
    "Demander une précision évite une interprétation erronée."),
 QC("Quelle est une source fréquente d'erreur en anglais professionnel ?", "Les nombres et les dates~Les couleurs~La météo~Le bruit", 0,
    "Les chiffres, dates et heures sont sensibles aux malentendus."),
 QC("Comment vérifier la compréhension d'un échange ?", "Par une question de clarification~En changeant de sujet~En fermant la porte~En traduisant mot à mot", 0,
    "La clarification confirme ou corrige ce qui a été compris."),
 QT("Expliquer l'intérêt d'un glossaire professionnel et la méthode pour le construire.",
     "Un glossaire professionnel rassemble les mots et expressions utiles au poste avec leur traduction et un exemple d'usage. Il évite de rechercher à chaque fois un terme et il réduit les erreurs sur les mots proches, les faux amis et les acronymes. Pour le construire, on part des situations réelles du service : accueil, entretien, courriel, documents remis aux usagers. On note chaque terme avec sa catégorie, sa traduction, sa prononciation approximative et une phrase courte. On vérifie le sens avec une source fiable ou un collègue anglophone, car un acronyme peut changer de sens d'un pays à l'autre. On classe le glossaire par thème, on le met à jour régulièrement et on le partage avec l'équipe. C'est un outil de qualité et de sécurité de la communication.",
     "On attend la finalité du glossaire, sa construction à partir des situations réelles et sa mise à jour."),
 QT("Un courriel professionnel contient un acronyme que vous ne connaissez pas. Que faites-vous ?",
     "On ne devine pas le sens d'un acronyme inconnu, car une interprétation erronée peut modifier une décision ou une information donnée à un usager. On cherche d'abord dans le glossaire du service et dans les documents de référence. Si le terme reste obscur, on demande une précision à l'expéditeur ou à un collègue anglophone, avec une question courte et polie : « Could you clarify what this abbreviation means ? ». On peut formuler une hypothèse de compréhension et demander confirmation plutôt que d'affirmer. On traite le courriel comme confidentiel : on ne le transmet pas à une personne non habilitée pour obtenir une traduction. Une fois le sens vérifié, on ajoute l'acronyme au glossaire avec son contexte et on répond en utilisant le terme complet lors de la première mention.",
     "On refuse de deviner, on vérifie auprès d'une source fiable et on enrichit le glossaire.")],
C("En anglais professionnel, la clarté prime sur la virtuosité : on vérifie le sens des mots et des chiffres.",
  "Lexique + contexte + vérification = communication fiable",
  "U2 · faux amis · acronymes · glossaire · clarification",
  "Care~Prendre soin~Patient~Personne soignée~Appointment~Rendez-vous~Support~Accompagnement~Benefit~Prestation sociale",
  "Identifier les termes utiles au poste|Vérifier le sens dans une source fiable|Noter traduction et exemple courte|Classer par thème dans un glossaire|Demander clarification en cas de doute",
  "Deviner le sens d'un acronyme~Confondre deux mots proches~Oublier de vérifier les dates~Partager un courriel confidentiel",
  "Courriel~Document reçu~Acronyme~Sens à vérifier~Question~Clarification polie~Glossaire~Terme ajouté",
  "Faux ami~Apparence trompeuse~Mot technique~Sens vérifié",
  "Traduction mot à mot~Risque d'erreur~Reformulation~Sens confirmé"))

# ============================================================ AN2
add("AN2", "Accueillir et orienter un usager en anglais", "Anglais professionnel", ["BTS1"],
S("L'accueil en anglais poursuit les mêmes objectifs qu'en français : informer, orienter et rassurer."
  "|Les formules simples comme Hello, Good morning et How can I help you ? suffisent dans la plupart des cas."
  "|Le professionnel se présente clairement en donnant son nom et son service."
  "|La personne peut avoir besoin d'un interprète ou d'un document traduit."
  "|Les phrases courtes et un rythme lent facilitent la compréhension."
  "|Il faut éviter l'argot, les expressions idiomatiques et les plaisanteries."
  "|La reformulation et les questions de clarification vérifient la compréhension."
  "|Les gestes et le langage non verbal restent importants dans l'accueil."
  "|L'orientation prépare les coordonnées, les horaires et les documents utiles."
  "|La confidentialité s'applique aussi aux échanges en langue étrangère."
  "|Les formulaires et les consignes écrites doivent rester accessibles."
  "|Le référentiel BTS SP3S attend une communication adaptée à chaque interlocuteur."),
[QC("Quels sont les objectifs d'un accueil en anglais ?", "Informer, orienter et rassurer~Amuser et divertir~Tester la grammaire~Supprimer les formalités", 0,
     "Les objectifs restent ceux de tout accueil professionnel."),
 QC("Quelle formule est adaptée pour ouvrir l'échange ?", "How can I help you ?~What is your problem exactly ?~Wait outside~Come back later", 0,
     "Une formule polie et ouverte installe la relation."),
 QC("Que faut-il éviter avec un interlocuteur anglophone ?", "Les phrases courtes~L'argot et les expressions idiomatiques~La reformulation~Un rythme lent", 1,
     "Les expressions idiomatiques sont difficiles à comprendre."),
 QC("Quand proposer un interprète ?", "Jamais~Lorsque la compréhension est insuffisante~Toujours et systématiquement~Uniquement par écrit", 1,
     "L'interprète compense une barrière linguistique réelle."),
 QC("Comment vérifier que la personne a compris ?", "En parlant plus fort~En reformulant et en demandant confirmation~En changeant de langue~En s'en allant", 1,
     "La reformulation et la confirmation sécurisent l'échange."),
 QC("Que faut-il préparer pour l'orientation ?", "Les coordonnées et les horaires~Le seul nom du service~Une blague~Un silence", 0,
     "L'orientation suppose des informations concrètes et vérifiées."),
 QC("La confidentialité s'applique-t-elle à un échange en anglais ?", "Non, seulement en français~Oui, dans toutes les langues~Uniquement par écrit~Seulement avec la direction", 1,
     "Le secret professionnel ne dépend pas de la langue employée."),
 QT("Décrire les étapes d'un accueil réussi en anglais avec une personne qui parle peu français.",
     "On commence par un sourire et une formule simple : Good morning, je m'appelle..., je travaille ici. On présente le service avec peu de mots et on demande à la personne comment on peut l'aider. On l'écoute sans l'interrompre, même si la compréhension est partielle, et on note les mots clés. On reformule en phrases courtes : « So you need an appointment with the social worker, is that right ? ». Si la personne ne comprend pas, on propose un document traduit ou un interprète plutôt que de répéter plus fort. On explique la suite : qui va la recevoir, à quelle heure, avec quels documents. On vérifie la compréhension une dernière fois et on trace l'accueil dans le dossier en respectant la confidentialité.",
     "On attend présentation simple, écoute, reformulation, aide à la compréhension et orientation concrète."),
 QT("Une personne anglophone semble perdue et agacée après plusieurs explications. Que changez-vous dans votre pratique ?",
     "On cesse de répéter la même phrase plus fort, car le problème n'est pas le volume mais la clarté. On s'excuse simplement de la difficulté et on change de méthode : phrases plus courtes, un seul idea à la fois, mots clés écrits, éventuellement un document traduit ou un interprète. On demande où la compréhension s'est arrêtée avec une question neutre, puis on reformule depuis le début avec l'accord de la personne. On utilise des gestes et des repères visuels pour l'orientation. On évite toute expression idiomatique. Une fois l'information comprise, on résume par écrit les étapes et on donne un interlocuteur identifié. On trace la difficulté rencontrée pour améliorer les supports d'accueil proposés aux usagers anglophones.",
     "On arrête la répétition, on adapte le support et la formulation, puis on vérifie et on trace.")],
C("Accueillir en anglais, c'est simplifier le langage sans simplifier la personne.",
  "Formules simples + reformulation + support adapté = accueil compris",
  "Phrases courtes · interprète · non verbal · confidentialité",
  "Accueil~Informer et orienter~Formule~Expression polie simple~Reformulation~Vérification du sens~Interprète~Aide à la compréhension~Orientation~Coordonnées et horaires",
  "Se présenter avec une formule simple|Laisser la personne exposer sa demande|Utiliser des phrases courtes et un rythme lent|Reformuler et confirmer la compréhension|Proposer un interlocuteur et tracer l'accueil",
  "Parler plus fort pour être compris~Utiliser des expressions idiomatiques~Deviner le besoin sans demander~Oublier la confidentialité",
  "Personne perdue~Signal d'incompréhension~Changement~Phrases courtes et écrit~Interprète~Aide proposée~Dossier~Accueil tracé",
  "Langage simple~Phrases courtes~Argot~Compréhension difficile",
  "Accueil en français~Expression courante~Accueil en anglais~Formules adaptées"))

# ============================================================ AN3
add("AN3", "Comprendre et rédiger un courriel professionnel en anglais", "Anglais professionnel", ["BTS2"],
S("Le courriel professionnel en anglais suit une structure simple et prévisible."
  "|L'objet du message, ou subject line, annonce le sujet en quelques mots."
  "|La formule d'appel, comme Dear Madame ou Dear Sir, adapte le ton au destinataire."
  "|Le corps du message présente le contexte, la demande et l'action attendue."
  "|Les phrases courtes et un paragraphe par idée améliorent la lisibilité."
  "|Les dates, les heures et les nombres sont écrits sans ambiguïté."
  "|Les pièces jointes sont nommées clairement et mentionnées dans le texte."
  "|La formule de clôture et la signature identifient l'expéditeur et le service."
  "|La relecture vérifie l'orthographe, la grammaire et le destinataire."
  "|Les informations confidentielles ne sont pas envoyées sans habilitation."
  "|La réponse est donnée dans un délai raisonnable ou avec un accusé de réception."
  "|Cette compétence s'inscrit dans l'unité U2 du référentiel BTS SP3S."),
[QC("À quoi sert la subject line ?", "À annoncer le sujet du message~À remplacer la signature~À cacher le destinataire~À allonger le courriel", 0,
     "L'objet permet de classer et de comprendre le message rapidement."),
 QC("Quelle formule d'appel est adaptée à un destinataire identifié ?", "Dear Ms Smith~Hey~To whom it may concern dans tous les cas~Aucune formule", 0,
     "Une formule polie et personnalisée est préférable."),
 QC("Quel contenu va dans le corps du message ?", "Le contexte, la demande et l'action attendue~Uniquement la signature~Les pièces jointes seules~La météo", 0,
     "Le corps porte l'information utile et la demande."),
 QC("Comment éviter une ambiguïté sur une date ?", "En utilisant des chiffres sans précision~En écrivant le mois en toutes lettres~En supprimant la date~En utilisant une abréviation locale", 1,
     "Écrire le mois en toutes lettres évite les confusions de format."),
 QC("Que faut-il faire avec une pièce jointe ?", "La nommer clairement et la mentionner dans le texte~L'envoyer sans prévenir~La cacher~La remplacer par une blague", 0,
     "Une pièce jointe identifiée est plus facile à retrouver."),
 QC("Quel réflexe s'impose avant l'envoi ?", "Relire et vérifier le destinataire~Envoyer immédiatement~Ajouter des acronymes~Supprimer la signature", 0,
     "La relecture évite les erreurs de destinataire et de formulation."),
 QC("Que faire si une réponse demande du temps ?", "Ne jamais répondre~Accuser réception et annoncer une échéance~Répondre par une plaisanterie~Changer d'objet", 1,
     "Un accusé de réception maintient la relation professionnelle."),
 QT("Décrire la structure d'un courriel professionnel clair en anglais et expliquer l'intérêt de chaque partie.",
     "Le courriel commence par un objet précis, par exemple Appointment confirmation, qui permet de classer le message. La formule d'appel est adaptée au destinataire : Dear Ms Smith si la personne est connue, Dear Sir or Madam dans le cas contraire. Le corps se compose d'un paragraphe de contexte, d'un paragraphe de demande et d'un paragraphe sur l'action attendue, avec des phrases courtes. Les dates sont écrites en toutes lettres pour éviter les confusions entre formats. Les pièces jointes sont mentionnées et nommées clairement. La clôture, par exemple Kind regards, et la signature avec le nom et le service, identifient l'expéditeur. Une relecture finale vérifie le destinataire et les informations confidentielles. Cette structure rend le message lisible et évite les échanges superflus.",
     "On attend objet, salutation, corps structuré, dates claires, pièces jointes, signature et relecture."),
 QT("Vous devez relancer un partenaire qui n'a pas répondu. Comment rester professionnel en anglais ?",
     "On commence par une formule polie et on rappelle le contexte en une phrase : « I am writing about the meeting scheduled for... ». On constate l'absence de réponse sans accusation : « I have not yet received your confirmation ». On reformule la demande de façon précise avec une échéance : « Could you send the document before Friday ? ». On propose son aide si une information manque. On termine par une formule de clôture et sa signature. On évite les expressions comme You forgot ou You never answered, qui mettent le destinataire en faute. On relit le message et on vérifie qu'il ne contient aucune donnée confidentielle inutile. Si aucune réponse n'arrive, on passe au téléphone ou au responsable hiérarchique selon la procédure, en gardant une trace des relances.",
     "On rappelle le contexte sans accusation, on précise l'échéance et on garde un ton poli et tracé.")],
C("Un courriel professionnel est un écrit court, structuré et relu : la forme sert la compréhension.",
  "Objet + contexte + demande + signature = message efficace",
  "Subject line · registre poli · dates explicites · relecture",
  "Objet~Sujet du message~Salutation~Formule adaptée~Corps~Contexte et demande~Dates~Écrites sans ambiguïté~Signature~Identité et service",
  "Choisir un objet précis|Adapter la formule d'appel|Rédiger contexte puis demande en phrases courtes|Préciser dates et pièces jointes|Relire et vérifier avant l'envoi",
  "Omettre l'objet~Utiliser un ton accusateur~Écrire une date ambiguë~Envoyer une donnée confidentielle",
  "Absence de réponse~Relance nécessaire~Formulation~Demande polie~Échéance~Date précise~Trace~Relances conservées",
  "Anglais professionnel~Registre simple et clair~Anglais courant~Registre familier",
  "Relance~Demande de suite~Accusé de réception~Confirmation reçue"))

# ============================================================ AN4
add("AN4", "Présenter une structure et ses prestations en anglais", "Anglais professionnel", ["BTS2"],
S("Présenter une structure en anglais consiste à expliquer son rôle, son public et ses prestations."
  "|La présentation commence par le nom de l'établissement et son statut."
  "|La mission est décrite en une phrase avec des verbes simples comme support, welcome et accompany."
  "|Le public accueilli est précisé : children, older people, people with disabilities."
  "|Les prestations sont énumérées avec des termes concrets et vérifiés."
  "|Les horaires, l'adresse et les moyens d'accès sont donnés clairement."
  "|Les nombres et les dates sont énoncés lentement pour éviter les confusions."
  "|Un support écrit ou visuel aide la personne à retenir les informations."
  "|Les acronymes sont explicités lors de la première mention."
  "|La personne est invitée à poser des questions et à reformuler."
  "|La confidentialité des situations individuelles est respectée."
  "|Cette compétence relève de l'unité U2 du référentiel BTS SP3S."),
[QC("Par quoi commence une présentation de structure ?", "Par le nom et le statut de l'établissement~Par une opinion personnelle~Par une plaisanterie~Par le prix d'un repas", 0,
     "Le nom et le statut situent immédiatement le service."),
 QC("Quel verbe simple peut décrire la mission ?", "Support~Perhaps~Anyway~Actually", 0,
     "Support est un verbe concret et compréhensible."),
 QC("Quel public peut être cité dans une présentation ?", "Older people~Le soleil~La météo~Une couleur", 0,
     "Le public accueilli est une information essentielle."),
 QC("Comment présenter les horaires ?", "Avec des chiffres précis et un rythme lent~Avec des approximations~En les supprimant~Avec des expressions idiomatiques", 0,
     "La précision et la lenteur facilitent la compréhension."),
 QC("À quoi sert un support écrit ou visuel ?", "À aider la mémorisation~À remplacer la parole~À cacher les horaires~À éviter les questions", 0,
     "Le support complète l'oral et aide à retenir."),
 QC("Quand expliciter un acronyme ?", "Lors de la première mention~Jamais~À la fin seulement~Uniquement par écrit", 0,
     "La première mention est le bon moment pour définir un acronyme."),
 QC("Que faire après la présentation ?", "Inviter aux questions et vérifier la compréhension~Partir immédiatement~Changer de sujet~Imposer une décision", 0,
     "L'échange de questions confirme la compréhension."),
 QT("Présenter en anglais une structure d'accueil à une personne anglophone, en précisant la méthode.",
     "On commence par se présenter et par donner le nom de la structure : « I work at a social service centre. » On explique le statut et la mission en une phrase courte : « We welcome people who need support in their daily life. » On précise le public, les prestations principales, les horaires et l'adresse, en utilisant des mots concrets et en évitant les acronymes non expliqués. On donne les informations une par une et on s'arrête pour demander si la personne suit : « Is this clear ? ». On propose une brochure ou une note écrite avec les coordonnées. On invite la personne à reformuler ce qu'elle a retenu ou à poser une question. On adapte le niveau de langue si besoin, par exemple avec un interprète. On ne révèle aucune information sur d'autres usagers.",
     "On attend nom, statut, mission, public, prestations, horaires, support et vérification."),
 QT("Un usager anglophone a retenu un horaire erroné après votre présentation. Que faire ?",
     "On ne corrige pas brutalement la personne. On l'invite à redire ce qu'elle a compris, puis on confirme ou on rectifie avec calme : « The centre opens at nine, not at seven. Let me write it down for you. » On écrit l'horaire en toutes lettres et on donne un support avec les coordonnées du service. On vérifie à nouveau la compréhension par une question simple. On s'excuse si la présentation a été trop rapide ou si le support manquait, sans accuser la personne d'erreur. On propose de répéter les informations importantes et de noter un numéro à appeler en cas de doute. On trace la difficulté dans le dossier si elle est utile au suivi et on améliore les supports de présentation pour les prochains usagers anglophones.",
     "On écoute la reformulation, on rectifie sans jugement et on sécurise par écrit.")],
C("Présenter un service, c'est rendre l'information vérifiable par la personne qui la reçoit.",
  "Nom + mission + public + prestations = présentation comprise",
  "Phrases courtes · noms explicites · support écrit · questions",
  "Structure~Nom et statut~Mission~Rôle en une phrase~Public~Personnes accueillies~Prestations~Services proposés~Horaires~Informations précises",
  "Se présenter et nommer la structure|Énoncer la mission en une phrase|Préciser le public et les prestations|Donner horaires et coordonnées par écrit|Inviter aux questions et vérifier",
  "Enchaîner trop vite les informations~Employer des acronymes non expliqués~Révéler un cas individuel~Supprimer le support écrit",
  "Horaire erroné~Compréhension inexacte~Correction~Répétition calme~Support~Information écrite~Vérification~Question simple",
  "Présentation orale~Adaptation à l'auditoire~Présentation écrite~Support durable",
  "Information comprise~Confirmation obtenue~Information supposée~Non vérifiée"))

# ============================================================ AN5
add("AN5", "Conduire un entretien simple en anglais professionnel", "Anglais professionnel", ["BTS2"],
S("Un entretien simple en anglais repose sur les mêmes principes qu'en français."
  "|La préparation définit l'objectif, les questions utiles et les mots clés du thème."
  "|L'ouverture présente le cadre, le rôle du professionnel et la confidentialité."
  "|Les questions ouvertes laissent la personne exposer sa situation."
  "|Les phrases courtes et une formulation neutre évitent d'orienter la réponse."
  "|L'écoute attentive est plus importante que la correction grammaticale."
  "|La reformulation vérifie la compréhension et montre que la personne est entendue."
  "|Le silence est respecté, car la recherche d'un mot peut prendre du temps."
  "|Les chiffres, dates et noms sont notés puis confirmés."
  "|La clôture résume les points compris et les actions prévues."
  "|Un interprète peut être proposé si la compréhension reste insuffisante."
  "|Le référentiel BTS SP3S rattache cet entretien à l'unité U2 et à la communication professionnelle."),
[QC("Que préparer avant un entretien en anglais ?", "L'objectif et les mots clés du thème~Une liste de blagues~Le seul nom de la personne~Rien du tout", 0,
     "La préparation cadre l'échange et sécurise le vocabulaire."),
 QC("Quel type de question laisse la personne exposer librement ?", "La question fermée~La question ouverte~La question suggestive~La question accusatrice", 1,
     "La question ouverte ne contraint pas la réponse."),
 QC("Quelle attitude est prioritaire pendant l'écoute ?", "Corriger la grammaire~Comprendre le sens~Répondre avant la fin~Changer de thème", 1,
     "Le sens prime sur la forme dans un entretien professionnel."),
 QC("Que faire face à un silence ?", "Le combler immédiatement~Le respecter pour laisser chercher les mots~Répéter la question plus fort~Terminer l'entretien", 1,
     "La personne peut avoir besoin de temps pour formuler."),
 QC("Que sont les informations à confirmer ?", "Les chiffres, dates et noms~Les couleurs~La météo~Les goûts personnels", 0,
     "Ces éléments précis sont sources de malentendus."),
 QC("Quel registre adopter ?", "Un registre neutre et simple~Un registre familier~L'humour systématique~L'argot", 0,
     "La neutralité évite d'orienter ou de heurter."),
 QC("Comment clore l'entretien ?", "En résumant les points compris et les actions~En partant sans un mot~En jugeant la personne~En supprimant la trace", 0,
     "La synthèse partagée sécurise la suite."),
 QT("Décrire la conduite d'un entretien simple en anglais avec une personne dont la maîtrise est limitée.",
     "On prépare l'objectif et une liste courte de mots clés. On ouvre en se présentant, en expliquant le cadre et la confidentialité avec des phrases simples. On pose une question ouverte et on écoute sans corriger la grammaire. On note les chiffres, les dates et les noms, puis on les confirme en les répétant. On reformule régulièrement pour vérifier le sens, avec des phrases courtes et un ton neutre. On respecte les silences et on propose un mot ou un support visuel si la personne cherche son expression. On évite les expressions idiomatiques et l'humour. À la fin, on résume les points compris et les actions prévues, on demande confirmation et on trace l'entretien. Si la compréhension reste insuffisante, on propose un interprète pour la suite.",
     "On attend préparation, ouverture cadrée, écoute du sens, reformulation, confirmation et clôture."),
 QT("La personne répond « yes » à toutes vos questions. Comment vérifier qu'elle a réellement compris ?",
     "Un « yes » répété peut être une réponse polie plutôt qu'une compréhension réelle. On ne le traite pas comme une preuve. On pose une question ouverte qui demande une précision concrète : « Can you tell me what happens next ? » ou « When is the appointment ? ». On observe la réponse et on reformule ce qui a été compris en demandant une confirmation nuancée : « So you will come on Monday at ten, is that correct ? ». On propose un support écrit avec les informations essentielles et on invite la personne à le relire avec nous. Si les réponses restent vagues, on suggère un interprète ou un proche de confiance avec l'accord de la personne. On trace la difficulté de compréhension dans la note d'entretien sans juger la personne, afin d'adapter les prochains échanges.",
     "On ne se fie pas au seul « yes », on demande une précision concrète et on propose un support.")],
C("Un entretien en anglais réussi se juge au sens compris, pas à la correction des phrases.",
  "Préparation + écoute + reformulation + confirmation = entretien fiable",
  "Question ouverte · silence · neutralité · interprète",
  "Préparation~Objectif et mots clés~Ouverture~Cadre et confidentialité~Écoute~Sens avant forme~Reformulation~Vérification~Confirmation~Chiffres et dates",
  "Préparer l'objectif et le vocabulaire|Présenter le cadre simplement|Poser une question ouverte et écouter|Reformuler et confirmer les données|Résumer et proposer un interprète si nécessaire",
  "Corriger la grammaire pendant l'échange~Utiliser des expressions idiomatiques~Se fier à un yes répété~Imposer une réponse",
  "Yes répété~Réponse polie~Question concrète~Vérification du sens~Support~Information écrite~Interprète~Aide proposée",
  "Question ouverte~Expression libre~Question fermée~Confirmation d'un fait",
  "Écoute~Compréhension du sens~Correction~Forme grammaticale"))

# ============================================================ MP1
add("MP1", "Diagnostic territorial et définition des objectifs", "Méthodologie de projet", ["BTS2"],
S("Une démarche de projet commence par un diagnostic de la situation et du territoire."
  "|Le diagnostic recense les besoins, les ressources, les acteurs et les contraintes."
  "|Il s'appuie sur des données observables et sur l'écoute des personnes concernées."
  "|L'analyse du besoin distingue ce qui est ressenti, exprimé et observé."
  "|La cartographie des acteurs identifie les partenaires potentiels et leurs rôles."
  "|Le diagnostic évite de confondre une plainte ponctuelle et un besoin structurel."
  "|Les objectifs généraux décrivent le changement visé à terme."
  "|Les objectifs opérationnels sont précis, mesurables et datés."
  "|Ils sont hiérarchisés selon l'urgence, la faisabilité et l'impact attendu."
  "|La concertation avec les équipes et les partenaires renforce l'acceptabilité du projet."
  "|Un écrit de synthèse fixe le diagnostic, les objectifs et les choix retenus."
  "|Le référentiel BTS SP3S place cette démarche dans le bloc 2 de compétences."),
[QC("Par quoi commence une démarche de projet ?", "Par un diagnostic de la situation~Par la rédaction du bilan~Par l'évaluation finale~Par l'archivage", 0,
     "Le diagnostic précède tout choix d'action."),
 QC("Que recense le diagnostic territorial ?", "Les besoins, ressources, acteurs et contraintes~Les seules opinions~Le budget uniquement~La météo", 0,
     "Le diagnostic est une photographie structurée de la situation."),
 QC("Quelle donnée est utile au diagnostic ?", "Une donnée observable et l'écoute des personnes~Une rumeur non vérifiée~Un souhait personnel~Une hypothèse non discutée", 0,
     "Le diagnostic combine faits et paroles des acteurs."),
 QC("Qu'est-ce qu'un objectif opérationnel ?", "Un objectif précis, mesurable et daté~Une intention vague~Une opinion~Une contrainte", 0,
     "Il permet de suivre l'avancement et d'évaluer."),
 QC("Comment hiérarchiser les objectifs ?", "Selon l'urgence, la faisabilité et l'impact~Par ordre alphabétique~Au hasard~Selon la météo", 0,
     "La priorisation est un choix raisonné."),
 QC("Pourquoi associer les partenaires au diagnostic ?", "Pour renforcer l'acceptabilité et la complémentarité~Pour éviter toute réunion~Pour supprimer les données~Pour décider seul", 0,
     "La concertation améliore la qualité et l'adhésion."),
 QC("Que fixe l'écrit de synthèse ?", "Le diagnostic, les objectifs et les choix retenus~Le seul budget~La seule opinion du responsable~Rien de précis", 0,
     "L'écrit rend la démarche traçable et partageable."),
 QT("Expliquer la différence entre objectif général et objectif opérationnel dans un projet social.",
     "L'objectif général décrit le changement visé à terme, par exemple améliorer l'accès aux droits pour un public isolé. Il donne une direction et un sens au projet. L'objectif opérationnel traduit cette direction en une action précise, avec un indicateur, une échéance et un responsable : organiser quatre permanences d'accueil par trimestre et accueillir quarante personnes dans l'année. Les objectifs opérationnels sont hiérarchisés : on traite d'abord l'urgence et les actions les plus faisables, puis celles qui ont le plus d'impact. Ils servent au suivi et à l'évaluation. Un bon objectif est formulé avec les acteurs concernés, car un objectif imposé est rarement suivi. L'écrit de synthèse conserve ce cadre pour que chacun puisse vérifier la cohérence entre les actions et la finalité.",
     "On distingue finalité et action mesurable, puis on explique hiérarchie et traçabilité."),
 QT("Un service constate plusieurs plaintes ponctuelles sur les délais d'accueil. Comment conduit-il le diagnostic ?",
     "On ne transforme pas immédiatement une plainte isolée en problème structurel. On recueille d'abord les faits : nombre de plaintes, dates, motifs, files d'attente observées et ressenti des usagers. On écoute aussi les professionnels pour comprendre les contraintes : effectif, outils, organisation des rendez-vous. On compare ces données avec les indicateurs habituels pour vérifier si les délais ont réellement augmenté. On cartographie les acteurs concernés : accueil, service social, direction et partenaires. On formule ensuite un diagnostic qui distingue une difficulté ponctuelle d'un dysfonctionnement répété. Si le besoin est confirmé, on définit des objectifs opérationnels avec indicateurs et échéances. Le tout est synthétisé par écrit et partagé avec les équipes avant toute action.",
     "On attend collecte des faits, écoute des acteurs, vérification du caractère structurel et objectifs datés.")],
C("Un projet commence par un diagnostic partagé : on ne traite bien que ce que l'on a correctement identifié.",
  "Diagnostic + objectifs mesurables + concertation = projet cadré",
  "Besoins · ressources · acteurs · contraintes · priorisation",
  "Diagnostic~État des lieux~Besoin~Ressenti, exprimé, observé~Acteurs~Partenaires et rôles~Objectif~Changement visé~Indicateur~Mesure du résultat",
  "Recueillir les faits et écouter les personnes|Cartographier les acteurs et les ressources|Identifier les contraintes|Formuler des objectifs généraux puis opérationnels|Synthétiser par écrit et partager",
  "Confondre plainte ponctuelle et besoin structurel~Fixer un objectif vague~Décider sans concertation~Omettre l'écrit de synthèse",
  "Plaintes~Délais d'accueil~Données~Nombre et dates~Diagnostic~Dysfonctionnement confirmé~Objectif~Permanences et indicateur",
  "Objectif général~Finalité du projet~Objectif opérationnel~Action mesurable",
  "Diagnostic~Comprendre avant d'agir~Action directe~Agir sans analyse"))

# ============================================================ MP2
add("MP2", "Planification et conduite d'un projet", "Méthodologie de projet", ["BTS2"],
S("La planification transforme les objectifs en actions datées et réparties."
  "|Un planning précise les tâches, les responsables, les échéances et les dépendances."
  "|Le budget prévisionnel recense les dépenses et les ressources mobilisées."
  "|Les actions sont découpées en étapes pour rendre le suivi possible."
  "|Une réunion de lancement présente le cadre et rôle de chacun."
  "|Un tableau de suivi permet de comparer le prévu et le réalisé."
  "|Les écarts sont analysés et donnent lieu à des ajustements argumentés."
  "|Les risques identifiés sont anticipés avec des mesures simples."
  "|Les réunions de suivi régulières maintiennent la coordination."
  "|Les décisions et modifications sont tracées dans un compte rendu."
  "|Le responsable de projet arbitre les priorités quand les moyens manquent."
  "|Cette conduite de projet relève du bloc 2 du référentiel BTS SP3S."),
[QC("Que contient un planning de projet ?", "Les tâches, responsables et échéances~Les seuls objectifs généraux~La météo~Les opinions personnelles", 0,
     "Le planning rend les actions suivables."),
 QC("À quoi sert le budget prévisionnel ?", "À recenser dépenses et ressources~À supprimer les actions~À remplacer le diagnostic~À éviter tout suivi", 0,
     "Il donne les moyens et les limites du projet."),
 QC("Pourquoi découper les actions en étapes ?", "Pour rendre le suivi possible~Pour compliquer le projet~Pour éviter les réunions~Pour supprimer les responsables", 0,
     "Des étapes identifiables permettent de mesurer l'avancement."),
 QC("Quel est le rôle de la réunion de lancement ?", "Présenter le cadre et les rôles~Clore le projet~Remplacer le planning~Supprimer les partenaires", 0,
     "Elle aligne les acteurs sur les objectifs et les responsabilités."),
 QC("Que fait-on face à un écart constaté ?", "On l'ignore~On l'analyse et on ajuste~On supprime le projet~On change de responsable sans raison", 1,
     "L'écart est une information pour adapter l'action."),
 QC("Quel outil assure la coordination dans le temps ?", "Le tableau de suivi et les réunions régulières~Le silence~Une décision unique~L'absence d'écrit", 0,
     "Le suivi régulier évite la dérive du projet."),
 QC("Que doit contenir un compte rendu de suivi ?", "Les décisions et modifications~Les seules impressions~La météo~Aucune information", 0,
     "Il trace ce qui a été décidé et par qui."),
 QT("Expliquer l'utilité d'un tableau de suivi dans la conduite d'un projet.",
     "Le tableau de suivi compare les actions prévues et les actions réalisées. Il indique pour chaque tâche le responsable, l'échéance, l'état d'avancement et les écarts constatés. Il rend visible ce qui avance, ce qui est en retard et ce qui bloque, sans attendre la réunion suivante. Il facilite la décision : quand une ressource manque, le responsable peut réallouer les efforts vers les actions prioritaires. Il sert aussi de trace pour les partenaires et la direction. Il doit être alimenté régulièrement et rester lisible, avec peu de colonnes et des informations à jour. Les écarts relevés sont discutés en réunion de suivi et donnent lieu à des ajustements expliqués dans le compte rendu.",
     "On attend comparaison prévu et réalisé, visibilité des écarts, aide à la décision et traçabilité."),
 QT("À mi-parcours, une action prend du retard faute de personnel. Comment réagir ?",
     "On vérifie d'abord la réalité du retard avec le tableau de suivi et l'échange avec le responsable de l'action : est-ce un retard réel ou une date trop optimiste ? On identifie la cause : absence de personnel, surcharge, dépendance non respectée ou information manquante. On évalue l'impact sur les objectifs et sur les publics concernés. On propose ensuite des ajustements : réorganiser les tâches, décaler une échéance non urgente, mutualiser des moyens avec un partenaire ou réduire temporairement le périmètre. Toute modification est argumentée et validée par le responsable de projet. On met à jour le planning et le tableau de suivi, on informe les acteurs concernés et on consigne la décision dans un compte rendu. On prévoit enfin une mesure pour éviter que le même blocage se reproduise.",
     "On attend vérification du retard, analyse de la cause, ajustement validé, mise à jour et trace.")],
C("Conduire un projet, c'est comparer régulièrement le prévu et le réalisé, puis décider en connaissance de cause.",
  "Planning + suivi + ajustements + traçabilité = projet piloté",
  "Réunion de lancement · budget · indicateurs · compte rendu",
  "Planning~Tâches et échéances~Budget~Dépenses et ressources~Suivi~Prévu et réalisé~Écart~Signal d'ajustement~Compte rendu~Décision tracée",
  "Élaborer le planning avec les responsables|Prévoir le budget et les moyens|Réunir les acteurs au lancement|Suivre les actions dans un tableau|Analyser les écarts et tracer les décisions",
  "Laisser le planning sans mise à jour~Ignorer un retard~Changer de priorité sans concertation~Omettre le compte rendu",
  "Retard~Action en difficulté~Cause~Personnel manquant~Ajustement~Réorganisation validée~Mise à jour~Planning corrigé",
  "Suivi~Comparer dans le temps~Analyse~Comprendre un écart",
  "Décision~Choix argumenté~Improvisation~Choix sans trace"))

# ============================================================ MP3
add("MP3", "Démarche qualité et amélioration continue", "Méthodologie de projet", ["BTS1"],
S("Une démarche qualité vise à améliorer régulièrement les prestations et le fonctionnement du service."
  "|Elle repose sur des procédures écrites, des indicateurs et des évaluations."
  "|La qualité est appréciée au regard des attentes des usagers et des exigences réglementaires."
  "|Les référentiels et les recommandations de bonnes pratiques servent de repères."
  "|Un audit interne vérifie la conformité des pratiques aux procédures."
  "|L'enquête de satisfaction recueille l'avis des usagers sur l'accueil et les prestations."
  "|Les réclamations sont une source d'information précieuse, pas une nuisance."
  "|Une non-conformité est un écart entre la procédure et la pratique observée."
  "|L'action corrective supprime la cause du problème pour éviter sa répétition."
  "|Le cercle d'amélioration enchaîne constat, analyse, action et vérification."
  "|L'implication des équipes est indispensable : la qualité ne se décrète pas."
  "|Le référentiel BTS SP3S associe cette démarche au bloc 2 de compétences."),
[QC("Quel est l'objectif d'une démarche qualité ?", "Améliorer régulièrement les prestations~Réduire les effectifs~Supprimer les procédures~Éviter tout contrôle", 0,
     "L'amélioration continue est la finalité de la démarche."),
 QC("Quel repère structure la démarche qualité ?", "Les procédures écrites et les indicateurs~Les rumeurs~La seule intuition~Le hasard", 0,
     "Les procédures et indicateurs rendent la qualité mesurable."),
 QC("Que révèle un audit interne ?", "La conformité des pratiques aux procédures~La météo~Le prix des fournitures~L'avis d'un seul agent", 0,
     "L'audit compare le réel et le prévu."),
 QC("À quoi sert une enquête de satisfaction ?", "À recueillir l'avis des usagers~À supprimer les réclamations~À remplacer les procédures~À éviter les réunions", 0,
     "Elle donne la perception des personnes accompagnées."),
 QC("Comment traiter une réclamation ?", "En la discréditant~En l'analysant comme une information~En l'ignorant~En la cachetant", 1,
     "La réclamation révèle un écart à corriger."),
 QC("Qu'est-ce qu'une non-conformité ?", "Un écart entre procédure et pratique~Une amélioration~Une bonne pratique~Un indicateur", 0,
     "La non-conformité désigne un écart constaté."),
 QC("Que fait une action corrective ?", "Elle supprime la cause du problème~Elle cache le problème~Elle remplace l'équipe~Elle supprime le suivi", 0,
     "Agir sur la cause évite la répétition."),
 QT("Expliquer le cercle d'amélioration continue et son intérêt dans un établissement social.",
     "Le cercle d'amélioration comprend quatre temps : constater un écart, analyser sa cause, mettre en œuvre une action et vérifier le résultat. Le constat vient des indicateurs, des réclamations, des audits ou des échanges avec les usagers. L'analyse cherche la cause réelle plutôt qu'un coupable : procédure inadaptée, information manquante, outil défaillant ou charge de travail excessive. L'action corrective est choisie avec les équipes concernées et inscrite dans un plan avec un responsable et une échéance. La vérification compare la situation avant et après avec les mêmes indicateurs. Si l'écart persiste, le cercle recommence avec une analyse approfondie. Cet enchaînement rend la qualité progressive et traçable, et il évite de se contenter de réparer les symptômes.",
     "On attend constat, analyse de cause, action corrective et vérification par indicateurs."),
 QT("Un usager se plaint d'avoir attendu trois semaines une réponse. Comment traiter cette réclamation dans une logique qualité ?",
     "On accueille la réclamation sans la minimiser et on remercie la personne de l'avoir exprimée. On recueille les faits précis : date de la demande, service concerné, délai écoulé et conséquences pour la personne. On apporte une réponse individuelle rapide avec une date de retour et un interlocuteur identifié. En parallèle, on ouvre une analyse : la demande a-t-elle été enregistrée, transférée, oubliée ou bloquée par un manque d'information ? On vérifie les procédures et les indicateurs de délai. On définit une action corrective sur la cause, par exemple une relance automatique ou une clarification des responsabilités, avec responsable et échéance. On informe l'équipe et on consigne la démarche dans le suivi qualité. Enfin, on revérifie les délais quelques semaines plus tard pour confirmer l'amélioration.",
     "On traite la personne et la cause, on trace l'action et on vérifie l'effet dans le temps.")],
C("La qualité n'est pas une conformité figée : c'est un cycle d'observation, d'action et de vérification.",
  "Constat + analyse de cause + action corrective + vérification = amélioration",
  "Procédure · indicateur · audit · réclamation · cercle d'amélioration",
  "Qualité~Prestations et fonctionnement~Procédure~Règle écrite~Indicateur~Mesure~Audit~Vérification~Réclamation~Information précieuse",
  "Constater un écart avec les indicateurs|Analyser la cause sans chercher un coupable|Définir une action corrective responsable|Informer les équipes et la personne|Vérifier le résultat avec les mêmes mesures",
  "Ignorer les réclamations~Corriger le symptôme sans chercher la cause~Imposer une procédure sans concertation~Ne jamais revérifier",
  "Attente de trois semaines~Réclamation~Faits~Dates et service~Action~Relance organisée~Vérification~Délai mesuré",
  "Non-conformité~Écart constaté~Conformité~Pratique attendue",
  "Qualité~Amélioration continue~Quantité~Volume de production"))

# ============================================================ MP4
add("MP4", "Évaluation de projet et indicateurs", "Méthodologie de projet", ["BTS2"],
S("L'évaluation mesure dans quelle mesure un projet a atteint ses objectifs."
  "|Elle distingue le suivi de la mise en œuvre et l'évaluation des résultats."
  "|Les indicateurs quantitatifs comptent des actions, des personnes ou des délais."
  "|Les indicateurs qualitatifs apprécient la satisfaction, la pertinence et les effets."
  "|Un indicateur est défini avant le démarrage du projet pour permettre la comparaison."
  "|Les données proviennent des dossiers, des enquêtes, des entretiens et des observations."
  "|La méthode de recueil doit être stable pour rester comparable dans le temps."
  "|L'évaluation associe les acteurs et les publics concernés."
  "|Elle identifie les résultats, les effets et les limites du dispositif."
  "|Un résultat inattendu peut être positif et mérite d'être capitalisé."
  "|Le rapport d'évaluation présente les données, l'analyse et les recommandations."
  "|Le référentiel BTS SP3S rattache l'évaluation au bloc 2 de compétences."),
[QC("Que mesure l'évaluation d'un projet ?", "L'atteinte des objectifs~Le seul budget dépensé~La météo~L'avis d'une seule personne", 0,
     "L'évaluation juge l'écart entre objectifs et résultats."),
 QC("Quel est un indicateur quantitatif ?", "Le nombre de personnes accueillies~La satisfaction ressentie~La pertinence perçue~Le ton des échanges", 0,
     "Un indicateur quantitatif se compte."),
 QC("Quel est un indicateur qualitatif ?", "La satisfaction des usagers~Le nombre de courriels~Le délai en jours~Le nombre de réunions", 0,
     "Un indicateur qualitatif apprécie un ressenti ou une pertinence."),
 QC("Quand définir les indicateurs ?", "Avant le démarrage du projet~À la fin seulement~Après le rapport~Jamais", 0,
     "Une mesure de départ est nécessaire pour comparer."),
 QC("Quelle condition garantit la comparabilité des données ?", "Une méthode de recueil stable~Un changement de méthode chaque mois~L'absence de données~Une estimation libre", 0,
     "La stabilité de la méthode rend les résultats comparables."),
 QC("Qui associer à l'évaluation ?", "Les acteurs et les publics concernés~Une seule personne~Personne~Les fournisseurs", 0,
     "La pluralité des regards améliore l'analyse."),
 QC("Que contient un rapport d'évaluation ?", "Les données, l'analyse et les recommandations~Une opinion sans donnée~Des promesses~Un simple budget", 0,
     "Le rapport rend l'évaluation lisible et utilisable."),
 QT("Distinguer suivi, évaluation et capitalisation dans une démarche de projet.",
     "Le suivi accompagne la mise en œuvre : il vérifie que les actions sont réalisées, que les échéances sont tenues et que les moyens sont utilisés. Il alimente le pilotage. L'évaluation intervient à des temps définis pour mesurer l'écart entre les objectifs et les résultats, avec des indicateurs quantitatifs et qualitatifs. Elle porte sur les effets du projet pour les publics, pas seulement sur l'activité. La capitalisation consiste à retenir ce qui a fonctionné, ce qui a échoué et pourquoi, afin de le transmettre à d'autres équipes ou de l'intégrer dans une nouvelle action. Elle transforme un résultat en connaissance réutilisable. Ces trois dimensions se succèdent et se nourrissent : un suivi fiable rend l'évaluation possible, et une évaluation bien conduite rend la capitalisation utile.",
     "On définit les trois notions et on montre comment elles s'enchaînent."),
 QT("Un projet affiche un nombre d'actions respecté mais une satisfaction en baisse. Que conclure ?",
     "On ne conclut pas au succès sur le seul volume d'actions. Le respect du calendrier est un indicateur de mise en œuvre, pas de résultat pour les usagers. La baisse de satisfaction invite à analyser la qualité perçue : les actions étaient-elles adaptées au besoin réel, accessibles, expliquées et respectueuses de la parole des personnes ? On croise les données quantitatives et qualitatives, puis on organise des entretiens ou une enquête complémentaire avec les usagers et les professionnels. On identifie les écarts entre objectifs affichés et effets constatés. On formule des recommandations précises : ajuster l'offre, améliorer l'information ou modifier les modalités d'accueil. Le rapport présente ces limites sans masquer les points positifs. On prévoit une nouvelle mesure après les ajustements pour vérifier l'évolution.",
     "On distingue activité et effet, on croise les indicateurs et on recommande des ajustements.")],
C("Évaluer, ce n'est pas compter pour prouver : c'est comprendre l'effet produit pour décider de la suite.",
  "Indicateurs + données + analyse partagée = évaluation utile",
  "Quantitatif · qualitatif · suivi · capitalisation · recommandation",
  "Suivi~Mise en œuvre~Indicateur~Mesure définie~Quantitatif~Nombre et délai~Qualitatif~Satisfaction et pertinence~Rapport~Données et recommandations",
  "Définir les indicateurs avant le démarrage|Recueillir des données avec une méthode stable|Associer acteurs et publics à l'analyse|Comparer résultats et objectifs|Rédiger le rapport et capitaliser",
  "Compter les actions sans regarder les effets~Changer de méthode en cours de route~Masquer les limites~Évaluer sans associer les usagers",
  "Actions respectées~Activité produite~Satisfaction en baisse~Effet insuffisant~Analyse~Entretiens complémentaires~Recommandation~Ajustement prévu",
  "Indicateur quantitatif~Ce qui se compte~Indicateur qualitatif~Ce qui s'apprécie",
  "Évaluation~Mesurer les effets~Suivi~Suivre la mise en œuvre"))

# ============================================================ MP5
add("MP5", "Partenariat et réseau d'acteurs sur un territoire", "Méthodologie de projet", ["BTS1"],
S("Un partenariat associe plusieurs acteurs autour d'un objectif commun."
  "|Il permet de compléter les moyens et les compétences de chaque structure."
  "|Les partenaires peuvent être des services publics, des associations, des collectivités ou des établissements."
  "|La complémentarité des rôles évite les doublons et les oublis."
  "|Une convention écrit les engagements, les responsabilités et les modalités d'échange."
  "|La coordination repose sur des interlocuteurs identifiés et des réunions régulières."
  "|Les échanges d'information respectent le secret professionnel et la finalité."
  "|Une divergence de rôles peut créer des tensions entre partenaires."
  "|La médiation et la clarification des missions restaurent la collaboration."
  "|Le réseau territorial facilite l'orientation des usagers vers le bon service."
  "|L'évaluation partagée mesure l'effet de l'action commune."
  "|Le référentiel BTS SP3S situe ce travail dans la politique de la structure sur le territoire."),
[QC("Pourquoi créer un partenariat ?", "Pour compléter les moyens et compétences~Pour supprimer les autres services~Pour éviter toute réunion~Pour réduire les droits des usagers", 0,
     "Le partenariat mutualise les ressources autour d'un objectif commun."),
 QC("Quel acteur peut être partenaire ?", "Une association locale~La météo~Une couleur~Un objet", 0,
     "Les partenaires sont des structures ou des services du territoire."),
 QC("Que fixe une convention de partenariat ?", "Les engagements et responsabilités~Le seul budget~La météo~Rien de précis", 0,
     "La convention rend les engagements lisibles et traçables."),
 QC("Quel principe limite les échanges d'information ?", "Le secret professionnel et la finalité~La curiosité~L'habitude~L'absence de règle", 0,
     "On ne transmet que ce qui est nécessaire à l'action commune."),
 QC("Quelle cause fréquente de tension entre partenaires ?", "Une divergence de rôles~Une entente parfaite~Un objectif commun clair~Une convention précise", 0,
     "Des missions floues génèrent des chevauchements."),
 QC("Comment orienter un usager dans un réseau ?", "Vers le service adapté à son besoin~Vers le premier service venu~Vers personne~Vers un service au hasard", 0,
     "L'orientation repose sur l'analyse du besoin et la connaissance du réseau."),
 QC("Que mesure une évaluation partagée ?", "L'effet de l'action commune~Le seul nombre de réunions~L'avis d'un seul partenaire~La météo", 0,
     "Elle juge l'effet produit ensemble."),
 QT("Expliquer l'intérêt d'un réseau de partenaires pour l'accompagnement des usagers.",
     "Un réseau de partenaires élargit les possibilités d'accompagnement : chaque structure apporte une compétence, un lieu ou un accès à un droit. Il évite que la personne soit renvoyée d'un service à l'autre sans réponse, car les rôles et les circuits sont clarifiés à l'avance. Il permet aussi une orientation plus juste : le professionnel connaît les dispositifs du territoire et adresse la personne au bon interlocuteur. La convention et les réunions régulières rendent la coopération stable, mais les échanges d'information restent limités à ce qui est nécessaire et couverts par le secret professionnel. Enfin, une évaluation partagée permet de vérifier que l'action commune produit bien l'effet attendu pour les usagers.",
     "On attend complémentarité, orientation, clarification des rôles, confidentialité et évaluation."),
 QT("Deux partenaires revendiquent le suivi du même usager. Comment gérer la situation ?",
     "On ne tranche pas selon le rang des structures mais selon le besoin de la personne et la mission de chacune. On réunit les interlocuteurs concernés et on rappelle les engagements de la convention. On explicite les rôles : qui assure l'accueil, qui suit la démarche administrative, qui intervient sur le logement ou la santé, qui coordonne les échanges. On vérifie avec la personne, si elle est d'accord, qui elle souhaite voir comme interlocuteur principal. On désigne un référent unique pour éviter les contradictions et les transmissions multiples. On formalise la répartition par écrit et on prévoit une réunion de suivi. Les informations échangées sont limitées au nécessaire et tracées. Si la divergence persiste, on recourt au responsable hiérarchique ou à une médiation, toujours dans l'intérêt de l'usager.",
     "On revient aux missions et au besoin, on désigne un référent et on trace l'accord.")],
C("Un réseau ne vaut que par la clarté des rôles et la protection des informations échangées.",
  "Objectif commun + rôles clairs + échange nécessaire = partenariat efficace",
  "Convention · coordination · secret professionnel · orientation",
  "Partenariat~Coopération entre structures~Complémentarité~Rôles distincts~Convention~Engagements écrits~Coordination~Réunions régulières~Orientation~Vers le bon service",
  "Identifier les acteurs du territoire|Clarifier les missions de chacun|Écrire une convention d'engagements|Organiser des échanges réguliers et tracés|Évaluer ensemble l'effet produit",
  "Revendiquer le même usager sans concertation~Transmettre une information non nécessaire~Laisser des rôles flous~Orienter au hasard",
  "Double revendication~Conflit de rôles~Réunion~Missions explicitées~Référent~Interlocuteur unique~Accord~Répartition écrite",
  "Réseau local~Acteurs du territoire~Isolement~Absence de coopération",
  "Information nécessaire~Partage autorisé~Curiosité~Partage interdit"))

valider_et_ecrire(F, "btssp3s-mat-part-C.json")
