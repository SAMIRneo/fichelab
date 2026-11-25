# -*- coding: utf-8 -*-
"""Generateur btsciel-mat-part-C.json — lot C : Francais (4), Anglais professionnel (4),
Communication (4), Methodologie (4), Comptabilite et gestion (4).

20 fiches 'prototype' pour la filiere bts-ciel (BTS1 / BTS2) :
12 points de cours, 10 questions corrigees (8 QCM + 2 texte),
7 blocs en ordre strict, 3 schemas via diag().
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _btsciel_common import FIL, REF, S, R, QC, QT, C, build, valider_et_ecrire

F = []

def add(prefix, titre, mat, ans, points, questions, c):
    F.append(build(prefix, titre, mat, ans, points, questions, c))

# ============================================================ PF1
add("PF1", "Synthèse de documents : méthode et restitution", "Français", ["BTS1"],
S("La synthèse de documents consiste à restituer l'essentiel de plusieurs textes portant sur un même sujet, sous forme d'un document nouveau et structuré."
  "|L'unité U1 de culture générale et expression du BTS s'appuie sur l'arrêté du 16 novembre 2006 qui définit les capacités attendues."
  "|Le dossier comprend généralement deux à quatre documents de natures variées : article, extrait d'ouvrage, graphique, texte réglementaire ou témoignage."
  "|La lecture active identifie pour chaque document : la source, la date, l'auteur, le thème, la thèse défendue et les arguments à l'appui."
  "|Le plan de synthèse regroupe les idées par thème et non par document : c'est la règle fondamentale pour éviter la simple juxtaposition des textes."
  "|Un titre et un sous-titre donnent une ligne de conduite ; l'introduction présente le sujet, le dossier et l'annonce du plan, sans développer d'opinion personnelle."
  "|Chaque partie s'appuie sur des idées clés, des exemples précis et des références explicites aux documents (« le document 2 souligne que… »)."
  "|Les chiffres, dates et noms propres doivent être repris exactement : une synthèse est fidèle à ses sources et ne les déforme pas."
  "|La conclusion fait le bilan des apports du dossier et ouvre sur une prolongation du sujet, sans introduire un avis personnel non demandé."
  "|Le style est impersonnel et clair : on évite le « je », les jugements de valeur et les expansions inutiles."
  "|La maîtrise de la langue, l'orthographe et la présentation sont évaluées : une copie lisible et aérée valorise le contenu."
  "|Cet exercice prépare directement à la rédaction de comptes rendus d'incident et de notes de synthèse técnica en entreprise."),
[QC("Quelle est la règle fondamentale d'une synthèse ?", "Résumer chaque document séparément~Regrouper les idées par thème~Ajouter son opinion personnelle~Recopier les documents", 1,
     "La synthèse est thématique, non document par document."),
 QC("Quel arrêté définit la culture générale et expression en BTS ?", "Arrêté du 16 novembre 2006~Arrêté du 25 janvier 2023~Arrêté du 4 juin 2013~Arrêté du 19 février 2018", 0,
     "L'unité U1 renvoie à l'arrêté du 16 novembre 2006."),
 QC("Quel élément ne doit pas apparaître dans une synthèse ?", "Une référence au document 2~Une date précise~Un avis personnel non demandé~Un chiffre exact", 2,
     "La synthèse restitue objectivement le dossier sans opinion personnelle."),
 QC("Que contient l'introduction ?", "Le détail des arguments~La présentation du sujet, du dossier et l'annonce du plan~La conclusion~Une opinion", 1,
     "L'introduction cadre le sujet et annonce le plan en trois parties."),
 QC("Comment citer un document dans une synthèse ?", "Par une note de bas de page obligatoire~En mentionnant le numéro du document et l'idée~Par une photographie~Par une référence Bibliothèque nationale", 1,
     "Les références explicites aux documents sont attendues, sous forme simple."),
 QC("Quel registre de langue privilégier ?", "Familier~Impersonnel et clair~Argotique~Poétique", 1,
     "Le « on » ou le pronom indéfini remplacent le « je »."),
 QC("Que faire d'un chiffre important du dossier ?", "L'arrondir librement~Le reprendre exactement~Le supprimer~Le remplacer par « beaucoup »", 1,
     "Fidélité et exactitude des données sont exigées."),
 QC("Quelle est une suite logique des parties ?", "Elles suivent l'ordre des documents~Elles suivent un plan thématique cohérent~Elles sont indépendantes~Elles sont classées par longueur", 1,
     "Les parties correspondent à des axes de réflexion, pas aux documents."),
 QT("Expliquer pourquoi une synthèse ne doit pas être rédigée document par document et proposer une méthode pour l'éviter.",
    "Rédiger document par document produit une juxtaposition : les idées se répètent, les contradictions ne sont pas traitées et le lecteur ne voit pas les enjeux communs. La synthèse exige un travail de déconstruction puis de reconstruction. La méthode consiste à lire tous les documents, à relever les idées sur des fiches en indiquant la source, à dégager trois ou quatre thèmes transversaux, puis à classer chaque idée sous un thème avant de rédiger. On obtient ainsi un plan thématique où chaque partie confronte les apports de plusieurs documents, avec des références précises et une progression logique.",
    "On explique le risque de juxtaposition et on décrit le classement thématique des idées avant rédaction."),
 QT("Décrire les étapes de préparation d'une synthèse de quatre documents en deux heures.",
    "On consacre environ 25 minutes à une lecture active : identifier source, date, thèse et arguments de chaque document, puis noter les idées et les chiffres clés. On passe 20 minutes à construire un plan thématique en regroupant les idées sous trois axes et en vérifiant que chaque axe est alimenté par plusieurs documents. La rédaction occupe environ 60 minutes : introduction avec annonce du plan, trois parties développées avec références aux documents, conclusion bilan et ouverture. On garde 15 minutes pour relire : orthographe, ponctuation, transitions, reprise exacte des chiffres, présence des références et respect de la longueur demandée. Une copie aérée avec des paragraphes courts est plus lisible pour le correcteur.",
    "On propose une répartition du temps realiste : lecture, plan, rédaction, relecture, avec les vérifications finales.")],
C("La synthèse est un exercice de restructuration : on démonte les documents pour reconstruire un texte thématique, fidèle et impersonnel.",
  "Synthèse = idées regroupées par thème, jamais par document",
  "U1 · arrêté du 16 novembre 2006 · références aux documents · style impersonnel",
  "Lecture active~Source, date, thèse~Fiches~Idées et références~Plan thématique~Trois axes~Rédaction~Impersonnel~Relecture~Exactitude des chiffres",
  "Lire tous les documents|Relever idées et chiffres|Construire un plan thématique|Rédiger avec références|Relire et corriger",
  "Procéder document par document|Ajouter une opinion personnelle|Arrondir les chiffres|Négliger la relecture",
  "4 documents~25 minutes de lecture~3 axes~Plan thématique~60 minutes~Rédaction~15 minutes~Relecture~U1~Culture générale",
  "Plan par document~Juxtaposition~Plan thématique~Synthèse réussie",
  "Introduction~Sujet et annonce du plan~Conclusion~Bilan et ouverture"))

# ============================================================ PF2
add("PF2", "Analyse de situation et argumentation écrite", "Français", ["BTS1"],
S("L'analyse de situation demande de comprendre un problème professionnel, d'identifier les enjeux et de proposer une position argumentée et nuancée."
  "|Le sujet prend appui sur un dossier documentaire ou sur une mise en situation décrivant un contexte d'entreprise."
  "|La première étape est l'analyse : définir les termes du sujet, repérer les acteurs, les faits, les contraintes et la question posée."
  "|Une bonne problématique transforme le sujet en question : quels sont les enjeux, quelles options s'offrent, quel arbitrage privilégier ?"
  "|Le plan dialectique (thèse, antithèse, synthèse) ou le plan thématique structure la réflexion de façon progressive."
  "|Chaque argument s'appuie sur un exemple ou sur un document du dossier : une affirmation sans preuve reste une opinion."
  "|La nuance est essentielle : on reconnaît les limites de sa position et les contre-arguments avant de proposer une synthèse."
  "|La conclusion répond explicitement à la problématique et propose une ouverture opérationnelle, par exemple une recommandation ou une piste d'action."
  "|Dans le contexte BTS CIEL, les sujets portent souvent sur la sécurité, la veille, la gestion de projet ou la relation avec les utilisateurs."
  "|La qualité de la langue, la cohérence des connecteurs logiques et la hiérarchie des idées sont évaluées avec la rigueur de l'écrit professionnel."
  "|Un brouillon de plan, même rapide, évite les répétitions et les digressions pendant la rédaction."
  "|L'argumentation écrite prépare la note de cadrage, le compte rendu d'audit et la soutenance de projet en U6."),
[QC("Qu'est-ce qu'une problématique ?", "Une citation~Une question qui reformule le problème et guide le plan~Une conclusion~Une liste de documents", 1,
     "La problématique est la question centrale à laquelle le devoir répond."),
 QC("Quel plan alterne thèse, antithèse et synthèse ?", "Plan thématique~Plan dialectique~Plan chronologique~Plan comparatif", 1,
     "Le plan dialectique confronte deux positions avant de les dépasser."),
 QC("Qu'est-ce qu'un argument sans preuve ?", "Une démonstration~Une simple opinion~Une référence~Un exemple", 1,
     "Une affirmation doit être étayée par un fait, un document ou un exemple."),
 QC("Que doit faire la conclusion ?", "Introduire un nouveau thème~Répondre à la problématique et ouvrir~Répéter l'introduction~Citer tous les documents", 1,
     "La conclusion apporte une réponse claire et une ouverture opérationnelle."),
 QC("Quel rôle joue la nuance ?", "Affaiblir le devoir~Reconnaître les limites et les contre-arguments~Supprimer les exemples~Éviter la conclusion", 1,
     "La nuance rend l'argumentation crédible et adulte."),
 QC("Quel thème peut illustrer un sujet BTS CIEL ?", "La gestion de la sécurité et la relation utilisateur~La mythologie grecque~La cuisine~Le sport professionnel", 0,
     "Les sujets s'appuient sur des situations professionnelles de la filière."),
 QC("À quoi sert le brouillon de plan ?", "À remplacer la rédaction~À hiérarchiser les idées et éviter les digressions~À allonger la copie~À cacher les références", 1,
     "Le plan garantit la progression et l'absence de répétitions."),
 QC("Quel connecteur introduit une opposition ?", "De plus~Cependant~Ainsi~D'abord", 1,
     "« Cependant », « or », « mais » marquent l'opposition ou la nuance."),
 QT("Un sujet demande : « La sensibilisation des utilisateurs est-elle le meilleur moyen de réduire les risques cyber ? ». Proposer une problématique et un plan d'argumentation.",
    "Problématique : la sensibilisation des utilisateurs est-elle suffisante pour réduire les risques cyber, ou doit-elle s'inscrire dans un dispositif plus large mêlant technologie et organisation ? Plan possible en trois parties : premièrement, la sensibilisation agit sur le facteur humain, vecteur majeur d'attaque (hameçonnage, mots de passe), et elle est peu coûteuse et transversale ; deuxièmement, elle montre ses limites : oubli, fatigue, ingénierie sociale de plus en plus ciblée, et elle ne protège pas contre une faille technique non corrigée ; troisièmement, une synthèse propose de l'articuler avec le moindre privilège, la MFA, la segmentation, la supervision et la mise à jour des correctifs. La conclusion répond que la sensibilisation est indispensable mais non suffisante : elle doit être un volet d'une défense en profondeur pilotée par la gouvernance.",
    "On formule une question, on construit un plan dialectique et on conclut par une synthèse opérationnelle."),
 QT("Expliquer la différence entre un argument, un exemple et une référence documentaire dans un devoir écrit.",
    "L'argument est une affirmation générale qui soutient la thèse, par exemple « la formation réduit le nombre d'incidents liés au hameçonnage ». L'exemple est un cas concret qui l'illustre : « après une campagne de test, le taux de clic sur les courriels frauduleux est passé de 25 % à 8 % dans l'entreprise X ». La référence documentaire situe l'appui dans le dossier : « selon le document 3, la formation est le deuxième investissement le plus rentable après la MFA ». Les trois niveaux sont complémentaires : l'argument donne la structure logique, l'exemple la rend tangible, la référence garantit la fidélité au dossier et permet au correcteur de vérifier la démarche.",
    "On définit chaque notion et on montre leur complémentarité dans un même paragraphe argumenté.")],
C("L'analyse de situation transforme un cas professionnel en une réponse structurée : problématique, arguments appuyés, nuances et recommandation.",
  "Argument + exemple + référence = paragraphe convaincant",
  "Problématique · plan dialectique · nuance · conclusion opérationnelle",
  "Analyse~Faits et acteurs~Problématique~Question centrale~Plan dialectique~Thèse et antithèse~Argument~Affirmation étayée~Nuance~Limites reconnues",
  "Définir les termes du sujet|Repérer acteurs et contraintes|Formuler la problématique|Construire le plan|Rédiger et conclure",
  "Répondre sans analyser|Avancer des opinions sans preuve|Ignorer les contre-arguments|Oublier de répondre à la question",
  "Sensibilisation~Facteur humain~MFA~Mesure technique~Défense en profondeur~Synthèse nuancée~Connecteur~« Cependant »~Conclusion~Recommandation",
  "Argument~Idée générale~Exemple~Cas concret",
  "Thèse~Position défendue~Antithèse~Position adverse"))

# ============================================================ PF3
add("PF3", "Expression écrite professionnelle : note, courriel et compte rendu", "Français", ["BTS2"],
S("L'écrit professionnel vise l'efficacité : transmettre une information exacte, à un destinataire précis, dans un format attendu et dans un délai court."
  "|La note de synthèse ou de cadrage présente une situation, une analyse et des recommandations dans un format court et hiérarchisé."
  "|Le courriel professionnel comporte un objet précis, une formule d'appel, un corps structuré, une demande explicite et une formule de politesse."
  "|L'objet du courriel doit être informatif : il indique le projet, le thème et l'action attendue plutôt qu'un simple « Bonjour »."
  "|Le compte rendu relate objectivement une réunion ou un incident : date, heure, participants, faits constatés, décisions, responsables et échéances."
  "|Dans un compte rendu d'incident, on distingue les faits établis des hypothèses et on horodate chaque observation."
  "|La hiérarchie de l'information passe par des paragraphes courts, des titres, des listes à puces et un résumé en tête de document."
  "|Le registre est courtois, clair et impersonnel : on bannit l'ironie, les jugements hâtifs et les acronymes non définis."
  "|Les pièces jointes sont nommées de façon explicite et mentionnées dans le corps du message."
  "|La relecture vérifie l'orthographe, la ponctuation, les accents, les noms, les dates et l'exactitude des chiffres."
  "|La confidentialité impose de vérifier les destinataires, d'éviter les données superflues et de ne pas transmettre de secrets techniques par courriel non chiffré."
  "|Ces compétences sont mobilisées chaque jour par un technicien CIEL : compte rendu d'astreinte, note d'incident, demande d'accès et rapport de recette."),
[QC("Que doit contenir l'objet d'un courriel professionnel ?", "Un simple « Bonjour »~Le projet, le thème et l'action attendue~Une citation~Le nom du logiciel de messagerie", 1,
     "Un objet informatif permet de classer et de retrouver le message."),
 QC("Quels éléments ne pas confondre dans un compte rendu d'incident ?", "Les faits et les hypothèses~Les dates et les heures~Les responsables et les échéances~Les titres et les puces", 0,
     "Distinguer la observation de l'hypothèse est une exigence de rigueur."),
 QC("Que privilégie un écrit professionnel ?", "Les longues phrases~Des paragraphes courts et une hiérarchie claire~Les acronymes inconnus~Le registre familier", 1,
     "La lisibilité passe par la structure et la concision."),
 QC("Quel contrôle avant l'envoi d'un courriel sensible ?", "Vérifier les destinataires et les pièces jointes~Augmenter la taille de la police~Ajouter des émojis~Raccourcir l'objet", 0,
     "Une erreur de destinataire ou de pièce jointe peut causer une fuite d'information."),
 QC("Comment nommer une pièce jointe ?", "doc1.pdf~De façon explicite avec date et objet~sans titre~avec des espaces vides", 1,
     "Un nom clair facilite l'archivage et évite les confusions."),
 QC("Quel registre adopter ?", "Familier~Courtois et impersonnel~Ironique~Argotique", 1,
     "Le registre courtois et impersonnel convient aux échanges professionnels."),
 QC("Quelle information ne pas mettre dans un compte rendu ?", "La date~Une hypothèse présentée comme un fait~Les décisions~Les responsables", 1,
     "Présenter une hypothèse comme certaine nuit à la fiabilité du document."),
 QC("Quel est un usage courant du compte rendu d'astreinte ?", "Raconter la journée~Consigner incidents, actions et éléments à transmettre~Publier une photo~Rédiger un contrat", 1,
     "Il assure la continuité entre les équipes et les périodes de garde."),
 QT("Rédiger le plan d'un compte rendu d'incident de sécurité destiné à la direction.",
    "Le document commence par un en-tête : titre, date et heure de l'incident, date de rédaction, auteur et destinataires. Un résumé de trois lignes présente la nature de l'incident, l'impact actuel et le niveau de criticité. La première partie relate la chronologie des faits établis avec horodatage : détection, systèmes touchés, mesures de confinement. La deuxième partie présente l'état des connaissances en distinguant faits confirmés et hypothèses en cours de vérification. La troisième partie indique les actions engagées, les responsables, les échéances et l'état des sauvegardes. Une dernière partie précise les notifications effectuées ou à venir (CNIL, ANSSI, assureur) et les points de vigilance. Les pièces jointes (journaux, captures) sont listées et référencées.",
    "On attend en-tête, résumé, chronologie, distinction faits et hypothèses, actions datées, notifications et annexes."),
 QT("Expliquer comment adapter un même information à un courriel destiné à un collègue technique et à une note destinée à la direction.",
    "Pour le collègue technique, le message peut employer les acronymes usuels du service, détailler les commandes exécutées, les journaux consultés et l'état précis des équipements. Il vise l'opérationnel : ce qui a été fait, ce qui reste à faire et les éventuels blocages. Pour la direction, la note doit partir de l'impact métier : service interrompu, nombre d'utilisateurs concernés, risque réglementaire, coût estimé et décision attendue. Le vocabulaire technique est traduit en termes de risque et de continuité, les détails sont renvoyés en annexe, et une recommandation explicite est formulée. Dans les deux cas, les faits, les dates et les chiffres restent identiques : seul le niveau de détail et l'angle d'analyse changent.",
    "On oppose l'angle opérationnel et l'angle décisionnel, en rappelant l'identité des faits et la nécessité d'une recommandation.")],
C("L'écrit professionnel est un outil d'action : objet clair, structure hiérarchisée, faits distincts des hypothèses et vérification avant envoi.",
  "Courriel = objet + appel + corps + demande + politesse",
  "Compte rendu = date, participants, faits, décisions, responsables, échéances",
  "Objet~Informations clés en première ligne~Compte rendu~Facts et décisions~Hiérarchie~Titres et puces~Relecture~Noms et chiffres~Confidentialité~Destinataires vérifiés",
  "Définir destinataire et objectif|Choisir le format adapté|Rédiger avec une structure claire|Vérifier faits et chiffres|Relire avant envoi",
  "Employer un objet vague|Présenter une hypothèse comme un fait|Oublier les pièces jointes|Envoyer sans vérifier les destinataires",
  "Courriel~Échange court~Note~Analyse et recommandation~Compte rendu~Traçabilité~Annexes~Journaux et preuves~Astreinte~Continuité de service",
  "Courriel~Destinataire unique ou multiple~Note~Destinataire hiérarchique",
  "Fait~Observation établie~Hypothèse~À vérifier"))

# ============================================================ PF4
add("PF4", "Culture générale et expression : enjeux numériques et société", "Français", ["BTS2"],
S("La culture générale vise à situer une question technique dans son contexte historique, social, économique et éthique."
  "|Pour un BTS CIEL, les thèmes récurrents concernent la place du numérique, la protection de la vie privée, le travail, la santé et l'environnement."
  "|Une notion comme la confidentialité ne se réduit pas à une règle technique : elle renvoie à la protection de la vie privée, consacrée par l'article 9 de la Déclaration universelle des droits de l'homme et par le Code civil."
  "|La liberté d'expression et la lutte contre les contenus illicites forment une tension classique, illustrée par la loi du 29 juillet 1881 et la LCEN."
  "|La fracture numérique désigne les inégalités d'accès aux équipements, aux réseaux et aux compétences : elle est un enjeu d'inclusion."
  "|L'empreinte environnementale du numérique concerne la fabrication des terminaux, la consommation électrique des centres de données et le cycle de vie des équipements."
  "|L'éthique professionnelle impose la loyauté, la discrétion, la responsabilité et le refus de détourner les outils d'information à des fins personnelles."
  "|Un technicien peut être confronté à un conflit d'intérêts, à une pression hiérarchique ou à la découverte d'une pratique irrégulière : la déontologie donne des repères."
  "|L'analyse d'une citation ou d'un sujet de culture générale exige de définir les termes, de situer la question et de construire une problématique."
  "|Les exemples issus de l'actualité et du référentiel professionnel rendent la réponse concrète et crédible."
  "|La nuance évite les oppositions simplistes : un même outil peut être bénéfique et porteur de risques selon son usage et son encadrement."
  "|Cette culture nourrit la communication avec les clients, la sensibilisation des utilisateurs et la posture d'expert responsable."),
[QC("Quel article de la Déclaration universelle des droits de l'homme protège la vie privée ?", "L'article 1er~L'article 9~L'article 19~L'article 33", 1,
     "L'article 9 consacre le droit à la protection de la vie privée, de la famille, du domicile et de la correspondance."),
 QC("Quelle tension oppose la loi de 1881 et la LCEN ?", "Liberté d'expression et retrait des contenus illicites~Sécurité et performance~Prix et qualité~Cloud et local", 0,
     "La liberté d'expression et la responsabilité des hébergeurs doivent être conciliées."),
 QC("Que désigne la fracture numérique ?", "Une panne de réseau~Des inégalités d'accès et de compétences~Un type de câble~Une faille de sécurité", 1,
     "Elle recouvre les écarts d'accès aux outils, aux usages et aux compétences."),
 QC("Quel est un aspect de l'empreinte environnementale du numérique ?", "La consommation électrique des centres de données~Le nombre de courriels~La couleur des interfaces~La vitesse de la fibre", 0,
     "Fabrication, usage et fin de vie des équipements ont un impact environnemental."),
 QC("Quelle qualité déontologique est attendue d'un technicien ?", "La discrétion~La curiosité indiscrète~La familiarité~L'improvisation", 0,
     "La discrétion et la loyauté sont des devoirs essentiels."),
 QC("Comment traiter un conflit d'intérêts ?", "Le cacher~Le signaler à la hiérarchie et se récuser~En profiter~En parler sur un réseau social", 1,
     "La transparence et la récusation sont les réponses déontologiques attendues."),
 QC("Quelle est la première étape de l'analyse d'une citation ?", "Donner son avis~Définir les termes et situer la question~Chercher la conclusion~Rédiger sans plan", 1,
     "La définition des termes précède la problématisation."),
 QC("Pourquoi nuancer une réponse de culture générale ?", "Pour éviter tout engagement~Pour tenir compte de la complexité et des contextes~Pour allonger la copie~Pour cacher son ignorance", 1,
     "Les réalités sociales et techniques sont rarement binaires."),
 QT("Un supérieur vous demande d'accéder aux journaux d'un collègue sans motif professionnel. Analysez la situation sous l'angle déontologique et proposer une réponse.",
    "La demande porte atteinte à la vie privée du collègue et dépasse le cadre des missions : l'accès aux journaux doit être motivé par un besoin professionnel, tracé et proportionné. La déontologie impose la discrétion, la loyauté et le refus de l'usage détourné des outils de surveillance ; le RGPD ajoute une exigence de finalité et de minimisation. La réponse consiste à demander le motif de l'accès et à le faire confirmer par écrit, à vérifier qu'une procédure existe et à proposer une alternative : extraire uniquement les informations nécessaires à une investigation légitime avec l'accord du responsable de la sécurité. Si la demande reste sans justification, on refuse poliment en expliquant le cadre, on documente le refus et, si la pression se poursuit, on remonte au RSSI ou à la direction des ressources humaines selon la procédure interne.",
    "On qualifie l'atteinte à la vie privée, on cite discrétion et finalité, puis on propose demande de motif, alternative tracée et remontée."),
 QT("Comment construire une réponse nuancée à la question « Le numérique est-il un facteur d'inclusion ou d'exclusion ? ».",
    "On commence par définir les termes : numérique (outils, réseaux, services) et inclusion (accès effectif et capacité d'usage). On situe ensuite le débat : le numérique facilite l'accès à l'information, aux démarches et à l'emploi, mais suppose équipement, connexion et compétences. Une première partie présente les facteurs d'inclusion : services en ligne, télétravail, outils d'accessibilité, formation. Une deuxième expose les facteurs d'exclusion : fracture d'usage, coût, zones mal desservies, interfaces complexes, dépendance aux plateformes. Une troisième propose une synthèse : l'effet dépend des conditions d'accès, de l'accompagnement et des politiques publiques. La conclusion répond que le numérique n'est ni inclusif ni excluant par nature : il amplifie les capacités lorsqu'il est encadré et accessible, et les inégalités lorsqu'il est imposé sans accompagnement.",
    "On définit, on situe, on construit un plan en deux axes plus synthèse, puis on répond sans simplifier.")],
C("La culture générale relie la technique à la société : droits, éthique, inclusion et environnement nourrissent la posture professionnelle.",
  "Vie privée : article 9 de la DUDH · Code civil",
  "LCEN · fracture numérique · empreinte environnementale · déontologie",
  "Culture générale~Society et technique~Droits~Vie privée~Fracture numérique~Inégalités d'accès~Déontologie~Discrétion et loyauté~Nuance~Complexité",
  "Définir les termes|Situer la question|Construire une problématique|Argumenter avec exemples|Nuancer et conclure",
  "Répondre par un avis immédiat|Opposer le monde simple en deux camps|Ignorer le contexte juridique|Confondre curiosité et discrétion",
  "Article 9~Protection de la vie privée~1881 et LCEN~Expression et contenus~Empreinte~Fabrication et usage~Conflit d'intérêts~Signalement et récusation~DUDH~Droits fondamentaux",
  "Inclusion~Accès et compétences~Exclusion~Fracture et dépendance",
  "Déontologie~Devoirs professionnels~Éthique~Valeurs et choix"))

# ============================================================ AN1
add("AN1", "Comprendre un document technique en anglais", "Anglais professionnel", ["BTS1"],
S("L'anglais technique est une langue de spécialité : elle emprunte au vocabulaire courant mais lui donne un sens précis, souvent différent."
  "|L'unité U2 du BTS CIEL renvoie à l'arrêté du 22 juillet 2008 modifié, qui fixe le programme d'anglais des BTS du secteur industriel."
  "|Le niveau visé se situe autour de B1/B2 du Cadre européen commun de référence pour les langues, avec un accent sur la compréhension de documents professionnels."
  "|Un document technique se lit d'abord par ses titres, ses intertitres, sa structure et ses éventuelles figures : on anticipe le contenu avant la lecture détaillée."
  "|La lecture active identifie les mots-clés, les chiffres, les unités, les noms propres et les termes répétés : ils portent l'information essentielle."
  "|Certains faux amis sont fréquents : to suffer signifie subir et non souffrir au sens de tolérer ; actual signifie réel et non actuel ; sensible signifie sensible au sens de perceptible et non raisonnable."
  "|Les verbes à particule (to set up, to shut down, to log in, to back up) sont très fréquents en informatique : leur sens est souvent composé."
  "|Les abréviations courantes sont à connaître : LAN, WAN, VPN, CPU, RAM, OS, DNS, HTTP, FAQ, SLA, PIN et URL."
  "|La voix passive est privilégiée dans les notices : the server is configured, the logs are stored, the access was denied."
  "|Les indications de sécurité (warning, caution, danger, must, must not, do not) imposent une attention particulière : elles expriment une obligation ou un interdit."
  "|Les unités et les formats de date diffèrent : 10/05/2026 peut signifier 10 mai ou 5 octobre selon la convention ; on privilégie la forme ISO 2026-05-10."
  "|La compréhension se vérifie par une restitution fidèle en français : on traduit le sens, pas mot à mot."),
[QC("Que signifie le mot anglais actual dans un document technique ?", "Actuel~Réel, effectif~Ancien~Théorique", 1,
     "Actual signifie réel ou effectif ; le français actuel se traduit par current."),
 QC("Que veut dire to shut down ?", "Démarrer~Arrêter ou éteindre~Sauvegarder~Installer", 1,
     "To shut down signifie éteindre un système ; to shut down a server est une opération courante."),
 QC("Quelle est la bonne traduction de warning ?", "Avertissement~Félicitation~Question~Réponse", 0,
     "Warning signale un avertissement ; caution indique une précaution."),
 QC("Que désigne l'abréviation RAM ?", "Un type de câble~Mémoire vive~Un protocole réseau~Un système d'exploitation", 1,
     "RAM signifie Random Access Memory, la mémoire vive."),
 QC("Comment traduire the access was denied ?", "L'accès a été accordé~L'accès a été refusé~L'accès a été supprimé~L'accès a été modifié", 1,
     "To deny signifie refuser ; le passé composé passif est courant dans les journaux."),
 QC("Quelle est une bonne première étape de lecture d'un document technique ?", "Traduire chaque mot~Observer titres, structure et figures~Chercher un dictionnaire~Lire la dernière phrase", 1,
     "L'anticipation par la structure améliore la compréhension globale."),
 QC("Que signifie faux ami ?", "Un mot qui n'existe pas~Un mot ressemblant au français mais de sens différent~Une faute de frappe~Une abréviation", 1,
     "Actual/current et sensible/raisonnable en sont des exemples classiques."),
 QC("Pourquoi préférer la date ISO 2026-05-10 ?", "Elle est plus courte~Elle évite l'ambiguïté entre formats américain et européen~Elle est obligatoire en grammaire~Elle correspond à l'heure GMT", 1,
     "Le format AAAA-MM-JJ est univoque et recommandé dans les documents techniques."),
 QT("Un mode d'emploi indique : « Do not disconnect the device while the update is running. Failure to comply may result in data loss. » Traduire et expliquer la consigne.",
    "Traduction : « Ne débranchez pas l'appareil pendant la mise à jour. Le non-respect de cette consigne peut entraîner une perte de données. » La consigne comporte deux niveaux : un interdit explicite (do not disconnect) et une conséquence (may result in data loss). While the update is running est une proposition de temps qui précise la période concernée. Failure to comply est une expression nominale fréquente dans les notices pour introduire le risque. Pour un technicien, cette phrase impose d'attendre la fin de la mise à jour et de vérifier l'indicateur de progression avant toute manipulation, car une interruption peut corrompre le micrologiciel.",
    "On traduit fidèlement, puis on relève l'interdit, la temporalité et la conséquence."),
 QT("Expliquer comment lire efficacement une page de documentation technique anglaise de deux pages.",
    "On commence par parcourir les titres, intertitres, listes et figures pour repérer la structure : installation, configuration, dépannage ou sécurité. On identifie ensuite les mots-clés et les abréviations relatifs au sujet, puis on lit chaque section en cherchant la réponse à une question précise, par exemple quels ports ouvrir ou quelles conditions vérifier. Les phrases à la voix passive et les modaux (must, should, may) sont repérés car ils expriment des obligations ou des risques. On note les valeurs numériques, les unités et les avertissements. Enfin, on restitue l'information en français avec ses propres mots et on vérifie que la traduction respecte le sens des termes techniques plutôt que la structure de la phrase anglaise.",
    "On décrit une lecture en trois temps : survol, lecture ciblée, restitution fidèle, avec attention aux modaux et aux chiffres.")],
C("L'anglais technique se lit par la structure et les mots-clés : faux amis, abréviations et modaux demandent une attention particulière.",
  "Faux amis : actual = réel, current = actuel",
  "U2 · arrêté du 22 juillet 2008 · voix passive · unités et dates ISO",
  "Faux ami~Sens différent du français~Abréviation~LAN, VPN, CPU~Modal~Must, should, may~Voix passive~The server is configured~Avertissement~Warning et caution",
  "Survoler titres et figures|Repérer mots-clés et abréviations|Lire chaque section avec une question|Noter chiffres et avertissements|Restituer le sens en français",
  "Traduire mot à mot|Confondre actual et current|Ignorer un avertissement|Interpréter une date ambiguë",
  "Do not disconnect~Interdit explicite~Data loss~Perte de données~SLA~Accord de niveau de service~CPU~Processeur~ISO~Date univoque~U2~Langue vivante",
  "Warning~Avertissement~Caution~Précaution",
  "Actual~Réel~Current~Actuel"))

# ============================================================ AN2
add("AN2", "Lexique technique : réseaux, systèmes et cybersécurité", "Anglais professionnel", ["BTS1"],
S("Le vocabulaire technique anglais est en grande partie normalisé par les RFC, les normes et les documentations des éditeurs."
  "|En réseau, les termes essentiels sont host, router, switch, gateway, subnet mask, packet, frame, bandwidth, latency et throughput."
  "|Un IP address est une adresse IP, a subnet est un sous-réseau, et default gateway désigne la passerelle par défaut."
  "|Le verbe to ping signifie tester la joignabilité ; to trace route ou traceroute permet de suivre le chemin des paquets."
  "|En système, on rencontre process, thread, kernel, file system, permissions, patch, reboot, logs et uptime."
  "|To install, to configure, to deploy, to troubleshoot, to monitor et to back up décrivent les gestes courants d'administration."
  "|En sécurité, les termes clés sont threat, vulnerability, risk, exploit, malware, ransomware, phishing, firewall, encryption et authentication."
  "|The CIA triad correspond en français au modèle CID : confidentiality, integrity, availability."
  "|Un vulnerability scan recherche des failles ; a patch corrige une vulnérabilité ; an incident response plan organise la réponse à incident."
  "|Le verbe to grant accorde un droit, to revoke le retire, to deny le refuse et to escalate transmet à un niveau supérieur."
  "|Les faux amis et les nuances sont fréquents : to manage signifie gérer et non manager au sens français du terme ; a patch est un correctif, pas un pansement."
  "|La maîtrise de ce lexique permet de lire une documentation, un journal en anglais et d'échanger avec un support international."),
[QC("Que signifie default gateway ?", "Passerelle par défaut~Adresse MAC~Masque de sous-réseau~Serveur DNS", 0,
     "La default gateway est le routeur utilisé pour sortir du réseau local."),
 QC("Quel terme désigne un correctif de sécurité ?", "A patch~A packet~A process~A port", 0,
     "A patch est un correctif ; to patch signifie appliquer le correctif."),
 QC("Que signifie to revoke an access ?", "Accorder un accès~Révoquer un accès~Refuser une connexion~Augmenter un privilège", 1,
     "To revoke retire un droit ou un certificat précédemment accordé."),
 QC("Quel mot désigne une menace ?", "A threat~A thread~A throughput~A trace", 0,
     "A threat est une menace ; a thread est un fil d'exécution."),
 QC("Que signifie uptime ?", "Temps d'arrêt~Durée de fonctionnement continu~Temps de réponse~Taux d'erreur", 1,
     "L'uptime indique depuis combien de temps un système fonctionne sans interruption."),
 QC("Quel terme désigne le chiffrement ?", "Bandwidth~Encryption~Latency~Firewall", 1,
     "Encryption est le chiffrement ; decryption est le déchiffrement."),
 QC("Que signifie to troubleshoot ?", "Dépanner~Installer~Configurer~Sauvegarder", 0,
     "To troubleshoot signifie diagnostiquer et résoudre un problème."),
 QC("Dans la triade CID, que signifie availability ?", "Confidentialité~Intégrité~Disponibilité~Authenticité", 2,
     "Availability correspond à la disponibilité du service."),
 QT("Traduire en anglais : « Le serveur a été compromis ; nous avons révoqué les accès et isolé la machine. »",
    "The server was compromised; we revoked the access rights and isolated the machine. On utilise le passif « was compromised » car l'action est subie par le serveur, puis le prétérit actif « revoked » et « isolated » pour les actions de l'équipe. Le vocabulaire clé est to compromise (compromettre), to revoke (révoquer) et to isolate (isoler). Une variante correcte est : The server has been compromised; we have revoked the credentials and isolated the host, avec le present perfect pour souligner le lien avec la situation actuelle.",
    "On propose une traduction correcte avec passif et vocabulaire technique, puis on explique les choix de temps."),
 QT("Expliquer la différence entre a threat, a vulnerability et a risk à partir d'un exemple de poste non mis à jour.",
    "A threat est un acteur ou un événement hostile, par exemple un attaquant qui scanne Internet à la recherche de machines non corrigées. A vulnerability est une faiblesse du système, ici un service dont le correctif de sécurité n'a pas été appliqué. A risk est la combinaison de la probabilité que la menace exploite cette vulnérabilité et de l'impact potentiel, par exemple la prise de contrôle du poste puis le vol de données. En anglais technique, on dit : an attacker exploits a vulnerability, which creates a risk for the organization. Le verbe to exploit est central : il décrit l'action de tirer parti d'une faille.",
    "On définit les trois termes en anglais et on les relie avec le verbe to exploit dans un exemple concret.")],
C("Le lexique technique anglais est normalisé : le maîtriser permet de lire journaux, documentations et avis de sécurité sans ambiguïté.",
  "CIA triad = confidentiality, integrity, availability",
  "to grant / to revoke · patch · threat · vulnerability · risk",
  "Host~Machine connectée~Gateway~Passerelle~Patch~Correctif~Threat~Menace~Vulnerability~Vulnérabilité",
  "Repérer les abréviations|Identifier la famille de mots|Vérifier le sens précis|Noter le verbe et son complément|Réemployer dans une phrase",
  "Confondre threat et thread|Traduire patch par pansement|Ignorer la voix passive|Mélanger grant et revoke",
  "Firewall~Pare-feu~Encryption~Chiffrement~Ransomware~Rançongiciel~Phishing~Hameçonnage~Uptime~Disponibilité continue~Logs~Journaux",
  "To grant~Accorder~To revoke~Révoquer",
  "Threat~Menace externe~Vulnerability~Faiblesse interne"))

# ============================================================ AN3
add("AN3", "Écrire un courriel et un rapport d'incident en anglais", "Anglais professionnel", ["BTS2"],
S("L'écriture professionnelle en anglais privilégie la clarté, la concision et la politesse directe."
  "|Un courriel comprend un objet informatif, une formule d'appel (Dear Mrs Smith, Hi Paul), un corps structuré et une formule de clôture (Kind regards, Best regards)."
  "|L'objet résume l'action attendue : Incident report - server outage - 10 May 2026 est plus efficace que Update."
  "|Les formules de politesse varient selon le degré de formalité : Dear Sir or Madam reste très formel, Hi Paul est adapté à un collègue connu."
  "|Le style anglais évite les longs développements : une phrase par idée, des paragraphes courts, des listes à puces pour les actions."
  "|Les modaux expriment le degré d'obligation : must pour une obligation forte, should pour une recommandation, may pour une possibilité."
  "|Pour décrire un incident, on utilise le prétérit pour les faits datés et le present perfect pour une situation encore en cours : The server crashed at 09:15 ; we have restored the service."
  "|Un rapport d'incident suit un plan : summary, timeline, impact, root cause, actions taken, recommendations."
  "|Les termes précis comptent : outage pour une interruption, breach pour une violation, downtime pour la durée d'indisponibilité, workaround pour un contournement."
  "|La voix passive est courante dans les rapports : The access was revoked at 10:02, The logs were preserved."
  "|La relecture vérifie l'orthographe, la ponctuation, les temps, les noms propres et l'exactitude des chiffres et des heures."
  "|La maîtrise de ces formes permet d'échanger avec un support éditeur, un client international ou une équipe SOC distribuée."),
[QC("Quelle formule de clôture est adaptée à un courriel professionnel courant ?", "See you soon~Kind regards~Bye bye~Take care", 1,
     "Kind regards ou Best regards sont des formules professionnelles standards."),
 QC("Quel objet de courriel est le plus efficace ?", "Update~Hello~Incident report - server outage - 10 May 2026~Urgent!!!", 2,
     "Un objet précis indique le thème, l'action et la date."),
 QC("Quel temps utiliser pour un fait daté dans un rapport ?", "Present perfect~Prétérit~Futur~Présent continu", 1,
     "Le prétérit convient aux événements terminés et datés : the server crashed at 09:15."),
 QC("Que signifie downtime ?", "Temps de réponse~Durée d'indisponibilité~Nombre d'utilisateurs~Taux de réussite", 1,
     "Downtime est la période pendant laquelle le service n'est pas disponible."),
 QC("Que signifie l'expression to escalate ?", "Réduire~Transmettre à un niveau supérieur~Supprimer~Ignorer", 1,
     "To escalate un incident consiste à le remonter à une équipe ou un niveau hiérarchique supérieur."),
 QC("Quel modal exprime une recommandation ?", "Must~Should~Can~Will", 1,
     "Should exprime un conseil ; must marque une obligation."),
 QC("Quel est un plan logique de rapport d'incident ?", "Summary, timeline, impact, actions, recommendations~Bonjour, histoire, fin~Titre, photo, signature~Introduction, blague, conclusion", 0,
     "Le plan standard va du résumé à la chronologie, puis à l'impact et aux actions."),
 QC("Dans The logs were preserved, quelle forme est utilisée ?", "Voix active~Voix passive~Futur antérieur~Conditionnel", 1,
     "La voix passive (were preserved) est fréquente dans les rapports factuels."),
 QT("Rédiger un court courriel en anglais pour signaler une panne de serveur et demander une intervention.",
    "Subject: Server outage - PROD-01 - 10 May 2026. Dear IT Operations Team, We are writing to report a service outage on server PROD-01, detected at 09:15 this morning. The server is currently unreachable and around 40 users are affected. We have isolated the machine and preserved the logs. Could you please investigate as soon as possible and confirm an estimated recovery time? Please let us know if you require additional information. Kind regards, [Name], Network Technician. Ce modèle contient un objet précis, une formule d'appel, les faits essentiels (quand, quoi, impact), les actions déjà prises, une demande explicite et une formule de clôture.",
    "On attend objet informatif, appel, faits datés, impact, actions, demande polie et clôture."),
 QT("Expliquer pourquoi les rapports techniques anglais utilisent fréquemment la voix passive et les modaux.",
    "La voix passive permet de présenter l'action et son résultat sans insister sur l'auteur : The configuration was modified at 14:20 est plus neutre et plus factuel que I modified the configuration. Elle rapproche le texte du style des journaux et des procédures, où l'important est ce qui s'est passé et quand. Les modaux (must, should, may, can) expriment quant à eux le statut de l'information : obligation, recommandation, possibilité ou capacité. They must be applied immédiatement indique une exigence, tandis que A reboot may be required exprime une incertitude. Cette combinaison produit un texte précis, prudent et professionnel, adapté à un contexte où les affirmations doivent être mesurées et traçables.",
    "On explique la neutralité du passif et la fonction des modaux pour nuancer obligations et incertitudes.")],
C("Écrire en anglais professionnel, c'est structurer l'information avec des formules adaptées, des temps corrects et un vocabulaire précis.",
  "Prétérit pour les faits datés · present perfect pour ce qui reste actuel",
  "Summary - timeline - impact - actions - recommendations",
  "Objet~Thème et action attendue~Formule d'appel~Dear ou Hi~Prétérit~Fait daté~Voix passive~The logs were preserved~Modal~Must, should, may",
  "Choisir l'objet et le destinataire|Rédiger les faits dans l'ordre|Utiliser les temps adaptés|Ajouter demande et recommandations|Relire noms, chiffres et heures",
  "Employer un objet vague|Mélanger les temps|Citer une heure sans fuseau|Oublier la formule de clôture",
  "Outage~Interruption~Breach~Violation~Downtime~Indisponibilité~Workaround~Contournement~Escalate~Remonter~Kind regards~Clôture professionnelle",
  "Must~Obligation~Should~Recommandation",
  "Voix active~L'auteur agit~Voix passive~L'action est subie"))

# ============================================================ AN4
add("AN4", "Présentation technique et soutenance en anglais", "Anglais professionnel", ["BTS2"],
S("La présentation technique en anglais vise à faire comprendre un projet, un incident ou une solution à un public international."
  "|La préparation commence par l'analyse du public : collègues techniques, direction ou client externe n'ont pas les mêmes attentes ni le même vocabulaire."
  "|Une structure simple en trois temps est efficace : context, problem, solution, puis éventuellement results et next steps."
  "|Chaque diapositive porte une idée principale, un titre clair et peu de texte : les détails sont apportés à l'oral."
  "|Les verbes de présentation utiles sont to outline, to show, to illustrate, to highlight, to summarise et to conclude."
  "|Les connecteurs de structure guident l'auditoire : first, then, next, finally, on the other hand, as a result, in conclusion."
  "|Les chiffres s'énoncent clairement : 10:02 a.m., forty percent, three out of five servers, an increase of 15 percent."
  "|La prononciation des acronymes est un point de vigilance : on épelle parfois (S-L-A) ou on prononce comme un mot (VPN, DNS, LAN)."
  "|Les expressions de prudence sont importantes : it appears that, we believe that, the data suggests that, we are currently investigating."
  "|La phase de questions-réponses se prépare : on reformule la question, on répond brièvement, puis on propose un complément si nécessaire."
  "|Les techniques de soutenance incluent le contact visuel, un débit modéré, des pauses et l'appui sur des mots-clés plutôt que la lecture intégrale d'un texte."
  "|En BTS CIEL, la soutenance du projet en option IR est un exercice de synthèse orale où la clarté prime sur la virtuosité technique."),
[QC("Quelle structure simple pour une présentation technique ?", "Context, problem, solution~Blague, histoire, conclusion~Détails, code, résultat~Titre, photo, musique", 0,
     "Contexte, problème, solution est une trame claire et facile à suivre."),
 QC("Que signifie to outline ?", "Dessiner~Présenter les grandes lignes~Ignorer~Répéter", 1,
     "To outline signifie donner le plan ou les points principaux."),
 QC("Quel connecteur introduit une conclusion ?", "However~In conclusion~Then~As a result", 1,
     "In conclusion marque la fin de l'exposé ; however marque l'opposition."),
 QC("Comment énoncer 15 % en anglais ?", "Fifteen percent~Fifteen per cent~Fifteen percentage~Fifteen percents", 0,
     "La forme courante est fifteen percent ; per cent s'écrit aussi en deux mots selon les styles."),
 QC("Quelle expression marque la prudence ?", "It is certain that~The data suggests that~We never know~It is obvious that", 1,
     "The data suggests that nuance l'affirmation, ce qui est apprécié dans un rapport technique."),
 QC("Comment gérer une question en fin de présentation ?", "Répondre sans écouter~Reformuler, répondre brièvement, proposer un complément~Refuser de répondre~Lire ses notes", 1,
     "La reformulation vérifie la compréhension et structure la réponse."),
 QC("Quelle est une bonne pratique de diapositive ?", "Beaucoup de texte~Une idée par diapositive et un titre clair~Des paragraphes entiers~Aucun titre", 1,
     "La diapositive soutient le propos, elle ne le remplace pas."),
 QC("Quel est un avantage d'un débit modéré ?", "Il fait paraître le locuteur pressé~Il améliore la compréhension de l'auditoire~Il raccourcit la présentation~Il évite les questions", 1,
     "Un rythme modéré et des pauses facilitent la réception d'une langue étrangère."),
 QT("Préparer une introduction de trois minutes en anglais pour présenter un projet de sécurisation d'un réseau.",
    "Good morning. My name is [Name] and I am a BTS CIEL student. Today I will present a network security project carried out for a small company with forty employees. First, I will describe the context: the company had no network segmentation and shared administrator accounts. Then, I will explain the problem: an attacker could move laterally from a single compromised workstation. Next, I will show the solution: three VLANs, multi-factor authentication, a firewall policy and a monitoring tool. Finally, I will present the results and the lessons learned. I will be happy to answer your questions at the end. Cette introduction situe le contexte, annonce le plan et indique la gestion des questions.",
    "On attend une formule d'accueil, le contexte, une annonce de plan avec connecteurs et une ouverture vers les questions."),
 QT("Expliquer comment adapter une présentation technique à un public de direction plutôt qu'à un public technique.",
    "Pour un public technique, on peut détailler l'architecture, les protocoles, les commandes et les paramètres : l'auditoire comprend les acronymes et attend de la précision. Pour une direction, on part de l'objectif métier : conformité, continuité d'activité, coût et risque. Les acronymes sont définis ou traduits, les détails de configuration sont renvoyés en annexe et les chiffres sont présentés en termes d'impact : nombre d'utilisateurs concernés, perte potentielle, délai de rétablissement et retour sur investissement. Le vocabulaire devient celui de la décision : risk, impact, cost, benefit, compliance. La recommandation doit être explicite avec une date et un responsable. Dans les deux cas, la structure context-problem-solution reste utile, mais le niveau de détail et les indicateurs changent.",
    "On compare vocabulaire, niveau de détail, chiffres et recommandation selon le public.")],
C("Une présentation technique en anglais réussit par une structure claire, des connecteurs, des chiffres lisibles et une gestion maîtrisée des questions.",
  "Context - problem - solution - results - next steps",
  "to outline · to highlight · in conclusion · the data suggests that",
  "Annonce du plan~First, then, finally~Diapositive~Une idée par slide~Chiffre~Forty percent~Prudence~The data suggests~Questions~Reformuler puis répondre",
  "Analyser le public|Construire un plan en trois temps|Préparer des diapositives sobres|Répéter les chiffres et acronymes|Gérer les questions",
  "Lire intégralement ses notes|Multiplier le texte sur les diapositives|Employer un jargon non défini|Improviser la conclusion",
  "Three VLANs~Segmentation~MFA~Authentification forte~15 percent~Pourcentage~In conclusion~Connecteur final~Q and A~Session de questions~Soutenance~Présentation de projet",
  "Public technique~Détails et acronymes~Public direction~Risque et décision",
  "To outline~Donner le plan~To highlight~Mettre en évidence"))

# ============================================================ CO1
add("CO1", "Communication professionnelle et relation client", "Communication", ["BTS1"],
S("La communication professionnelle est un processus d'échange d'informations entre acteurs dans un contexte de travail, avec un objectif et des contraintes."
  "|Le modèle classique de la communication distingue un émetteur, un message, un canal, un récepteur, du bruit et un feedback."
  "|Le bruit désigne tout élément qui perturbe la transmission : jargon, mauvaise connexion, distraction, préjugé ou information manquante."
  "|Une communication efficace adapte le message au destinataire : son niveau technique, ses attentes, son urgence et son contexte culturel."
  "|L'écoute active suppose de reformuler, de poser des questions ouvertes et de différer le jugement pour comprendre le besoin réel de l'interlocuteur."
  "|La relation client technique repose sur la clarification du problème, la transparence sur l'état d'avancement et la tenue des engagements de délai."
  "|Un technicien doit traduire une contrainte technique en langage métier : expliquer pourquoi une maintenance est nécessaire plutôt que citer le numéro de version."
  "|Les niveaux de langage et le ton varient selon le canal : courriel, téléphone, messagerie instantanée, ticket ou réunion."
  "|La politesse et l'empathie ne sont pas des formalités : elles réduisent la tension lorsque l'utilisateur est frustré par une panne."
  "|La traçabilité des échanges dans un ticket permet de reprendre l'historique et d'éviter que l'utilisateur répète son problème."
  "|La promesse doit être mesurée : annoncer un délai réaliste vaut mieux qu'un optimisme qui détruira la confiance."
  "|Ces compétences sont mobilisées au quotidien par le technicien CIEL auprès des utilisateurs, des collègues et des prestataires."),
[QC("Quels éléments du modèle de communication désignent ce qui perturbe le message ?", "Le feedback~Le bruit~Le canal~L'émetteur", 1,
     "Le bruit est tout ce qui interfère avec la transmission ou la réception du message."),
 QC("Que signifie écoute active ?", "Écouter en attendant son tour de parler~Reformuler et poser des questions pour comprendre~Répondre immédiatement~Interrompre l'interlocuteur", 1,
     "L'écoute active implique reformulation, questions ouvertes et suspension du jugement."),
 QC("Comment adapter un message technique à un utilisateur ?", "Employer plus d'acronymes~Traduire la contrainte en termes de service et d'impact~Répondre par un journal de bord~Raccourcir au maximum", 1,
     "L'utilisateur attend de comprendre les conséquences pour son travail."),
 QC("Quel est un risque d'une promesse de délai irréaliste ?", "Une meilleure image~Une perte de confiance lors du retard~Une baisse de la charge~Une augmentation du trafic", 1,
     "Un engagement non tenu détruit la crédibilité du service."),
 QC("Pourquoi tracer les échanges dans un ticket ?", "Pour remplir une statistique~Pour conserver l'historique et éviter les répétitions~Pour supprimer le problème~Pour augmenter le délai", 1,
     "La traçabilité permet la continuité entre intervenants et le suivi de la résolution."),
 QC("Quel canal est adapté à une urgence nécessitant une action immédiate ?", "Le courrier postal~Le téléphone ou l'astreinte~La note annuelle~Le rapport PDF", 1,
     "Un canal synchrone est nécessaire lorsque le temps est critique."),
 QC("Quelle attitude favorise la relation client en situation de panne ?", "L'ironie~L'empathie et la clarté~Le silence~La minimisation du problème", 1,
     "Reconnaître la gêne et expliquer la situation améliore la perception du service."),
 QC("Quel est le rôle du feedback dans le modèle de communication ?", "Renvoyer une information sur la réception du message~Augmenter le bruit~Remplacer le message~Supprimer le récepteur", 0,
     "Le feedback permet à l'émetteur de vérifier que le message a été compris."),
 QT("Un utilisateur se plaint vigoureusement d'une panne qui bloque son travail. Décrire la conduite à tenir en cinq gestes.",
    "On l'écoute sans l'interrompre et on reformule sa plainte pour montrer que l'on a compris : « Si je comprends bien, vous ne pouvez plus accéder à votre application depuis ce matin. » On pose ensuite des questions ouvertes pour préciser le périmètre : depuis quand, sur combien de postes, quels messages d'erreur. On s'engage sur une action immédiate et un délai de retour réaliste, en indiquant ce qui est déjà fait. On informe régulièrement de l'avancement, même s'il n'y a pas de nouveauté, pour éviter le sentiment d'abandon. Enfin, après résolution, on confirme par écrit le problème, la cause et la date de rétablissement, et on ouvre une action de prévention si nécessaire.",
    "On attend écoute et reformulation, questions, engagement crédible, information régulière et clôture écrite."),
 QT("Expliquer pourquoi un même incident ne doit pas être présenté de la même manière à un utilisateur, à un chef de service et à la direction.",
    "L'utilisateur veut savoir quand il pourra retravailler et si ses données sont intactes : on utilise un langage simple et un délai concret. Le chef de service s'intéresse à l'impact sur son équipe, aux contournements possibles et à la charge de travail : on précise le nombre de postes touchés et les solutions temporaires. La direction attend une évaluation du risque, de la durée d'indisponibilité, de l'exposition réglementaire et des décisions à prendre : on parle en termes de criticité, de RTO, de conformité et de coût. Les faits restent identiques, mais le niveau de détail, le vocabulaire et la recommandation changent. Adapter son message n'est pas le déformer : c'est rendre l'information utile à chaque destinataire.",
    "On distingue les attentes des trois publics tout en rappelant l'identité des faits et l'honnêteté de la présentation.")],
C("Communiquer professionnellement, c'est adapter un message fidèle au destinataire, écouter activement et tenir ses engagements.",
  "Émetteur · message · canal · récepteur · bruit · feedback",
  "Écoute active · reformulation · traçabilité · empathie · délai réaliste",
  "Émetteur~Émet le message~Récepteur~Reçoit et interprète~Bruit~Perturbation~Feedback~Retour d'information~Écoute active~Reformulation",
  "Écouter sans interrompre|Reformuler le besoin|Poser des questions ouvertes|S'engager sur un délai réaliste|Informer et tracer",
  "Interrompre l'utilisateur|Promettre une date non vérifiée|Employer du jargon inutile|Laisser le ticket sans réponse",
  "Ticket~Historique des échanges~Astresinte~Canal synchrone~RTO~Délai de reprise~Empathie~Reconnaître la gêne~Feedback~Vérification de la compréhension",
  "Écoute active~Comprendre avant de répondre~Écoute passive~Entendre sans reformuler",
  "Bruit~Perturbation du message~Feedback~Boucle de retour"))

# ============================================================ CO2
add("CO2", "Communication écrite et numérique en équipe", "Communication", ["BTS1"],
S("La communication écrite en équipe technique doit être courte, structurée et consultable par tous les membres concernés."
  "|Les canaux se complètent : le courriel pour les échanges formels et archivés, la messagerie instantanée pour les questions rapides, le ticketing pour le suivi d'incident et la documentation partagée pour les procédures."
  "|Choisir le bon canal évite la dispersion de l'information : une décision importante doit être consignée dans un outil durable, pas seulement dans un message éphémère."
  "|Un message efficace indique le contexte, la demande, l'échéance et, si nécessaire, la personne responsable."
  "|Les listes à puces et les paragraphes courts facilitent la lecture sur écran, notamment sur mobile."
  "|Les accusés de réception et les mentions explicites (« action pour Paul avant vendredi ») réduisent les malentendus sur la responsabilité."
  "|La netiquette impose de respecter les horaires, d'éviter les messages superflus, de ne pas écrire en majuscules et de relire avant l'envoi."
  "|La documentation collaborative (wiki, Owncloud, Notion, Confluence) doit être datée, versionnée et associée à un responsable."
  "|Les canaux numériques créent une trace : les échanges professionnels sont susceptibles d'être consultés, ils doivent rester factuels et courtois."
  "|La surcharge de notifications nuit à la concentration : on privilégie des règles de notification et des plages de travail ininterrompu."
  "|Les équipes distribuées ont besoin de rituels écrits : compte rendu de réunion, tableau de bord et décisions archivées."
  "|La maîtrise de ces usages est un facteur d'efficacité et de sécurité, car elle limite les erreurs de destinataire et les fuites d'information."),
[QC("Quel canal privilégier pour une décision qui doit durer ?", "Un message éphémère~La documentation ou le ticket archivé~Un appel téléphonique~Une conversation de couloir", 1,
     "Une décision doit être consignée dans un outil durable et consultable."),
 QC("Quels éléments contient une demande claire ?", "Contexte, demande, échéance, responsable~Salutation, blague, signature~Titre, image, vidéo~Aucun élément précis", 0,
     "Ces quatre éléments évitent les allers-retours inutiles."),
 QC("Qu'appelle-t-on netiquette ?", "Une règle de réseau~L'ensemble des règles de courtoisie en ligne~Un logiciel de messagerie~Une norme de câblage", 1,
     "La netiquette encadre les comportements dans les échanges numériques."),
 QC("Pourquoi relire avant l'envoi ?", "Pour allonger le message~Pour vérifier destinataire, pièces jointes et faits~Pour ajouter des majuscules~Pour supprimer l'objet", 1,
     "Une erreur de destinataire ou de pièce jointe peut être graves."),
 QC("Quel est un risque de la multiplication des notifications ?", "Une meilleure concentration~Une perte d'attention et de productivité~Une baisse du nombre de messages~Une sécurité renforcée", 1,
     "Le bruit numérique fragmente le travail et augmente la charge mentale."),
 QC("Comment rendre une documentation collaborative fiable ?", "Sans date ni auteur~Avec date, version et responsable identifiés~Avec des acronymes non définis~En la dupliquant", 1,
     "Date, version et responsable permettent de savoir si l'information est à jour."),
 QC("Quel format de message est préférable sur écran ?", "Un long paragraphe~Des paragraphes courts et des listes~Des majuscules continues~Aucune ponctuation", 1,
     "La lecture sur écran favorise les blocs courts et les listes."),
 QC("Pourquoi une équipe distribuée a-t-elle besoin de rituels écrits ?", "Pour remplacer le travail~Pour garder une trace commune des décisions et du suivi~Pour réduire le nombre de réunions à zéro~Pour éviter la documentation", 1,
     "Les rituels écrits compensent l'absence de contact direct et assurent la continuité."),
 QT("Une décision importante a été prise oralement lors d'un appel. Expliquer pourquoi et comment la consigner.",
    "Un accord oral reste fragile : les participants peuvent s'en souvenir différemment, les absents n'y ont pas accès et aucune preuve ne subsiste en cas de litige ou d'audit. Il faut donc rédiger un compte rendu court dès la fin de l'appel : date, participants, décision prise, motifs, actions qui en découlent, responsables et échéances. Le message est envoyé à tous les participants avec un délai pour signaler une erreur ou une objection, puis archivé dans l'outil de ticketing ou la documentation de projet. Les points de désaccord éventuels sont résolus avant application. Cette trace facilite aussi le retour d'expérience et la continuité si un intervenant change de poste.",
    "On justifie la traçabilité, puis on décrit compte rendu, vérification par les participants et archivage."),
 QT("Proposer une organisation des canaux de communication pour une équipe support de six personnes.",
    "Le ticketing est le canal central de toute demande : il porte le contexte, l'historique, la criticité et la clôture. La messagerie instantanée sert aux questions courtes et aux alertes nécessitant une réponse immédiate, avec un canal par thème (incidents, astreinte, projets). Le courriel est réservé aux communications formelles avec les autres services, les fournisseurs et la direction. La documentation collaborative contient les procédures, les schémas et les décisions, avec une date de mise à jour et un responsable. Des rituels complètent le dispositif : point quotidien de dix minutes, compte rendu hebdomadaire et revue mensuelle des procédures. Chaque canal a une finalité et une règle d'archivage, ce qui évite la dispersion et les doublons.",
    "On attribue un rôle à chaque canal et on ajoute des rituels et des règles d'archivage.")],
C("La communication d'équipe repose sur le bon canal, une trace durable et des messages structurés : la netiquette protège la clarté et la sécurité.",
  "Demande = contexte + action + échéance + responsable",
  "Ticketing · messagerie · courriel · documentation datée · netiquette",
  "Ticketing~Suivi des incidents~Messagerie~Questions rapides~Courriel~Échanges formels~Documentation~Procédures datées~Netiquette~Courtoisie en ligne",
  "Choisir le canal selon la finalité|Rédiger une demande structurée|Désigner un responsable|Archer la décision|Limiter les notifications",
  "Prendre une décision seulement à l'oral|Envoyer une demande sans échéance|Multiplier les canaux redondants|Négliger la relecture",
  "6 personnes~Équipe support~Canal central~Le ticket~Rituels~Point et compte rendu~Version~Date de mise à jour~Archivage~Preuve et continuité",
  "Messagerie~Immédiat et éphémère~Documentation~Durable et structurée",
  "Notification~Alerte~Concentration~Travail ininterrompu"))

# ============================================================ CO3
add("CO3", "Animer une réunion et communiquer à l'oral", "Communication", ["BTS2"],
S("Animer une réunion, c'est conduire un groupe vers un résultat déterminé dans un temps défini."
  "|La préparation fixe l'objectif, les participants nécessaires, l'ordre du jour, la durée, les documents à lire et le rôle de chacun."
  "|Un ordre du jour distingue les points d'information, les points de discussion et les points de décision."
  "|L'animateur veille au temps, à la parole de chacun et au retour au sujet ; le secrétaire consigne les décisions et les actions."
  "|Une réunion utile produit des décisions explicites avec un responsable et une date, pas seulement des échanges."
  "|Les techniques d'animation incluent la reformulation, le questionnement, le tour de table, le brainstorming et la synthèse intermédiaire."
  "|La communication orale s'appuie sur une voix claire, un rythme adapté, des pauses et un regard qui balaie l'assemblée."
  "|Les gestes et la posture renforcent le message : éviter les bras croisés, hocher la tête, se tenir droit."
  "|Les supports visuels doivent rester simples : un titre, une idée, un chiffre par diapositive, avec des couleurs lisibles."
  "|Les réunions asynchrones ou distancielles demandent le même niveau de préparation et un partage d'écran maîtrisé."
  "|Le compte rendu diffusé après la réunion reprend les décisions, les actions, les responsables, les échéances et les points en attente."
  "|Pour un technicien CIEL, savoir animer un point d'astreinte ou une revue d'incident est une compétence professionnelle déterminante."),
[QC("Quel est le premier élément à définir avant une réunion ?", "La durée de la pause~L'objectif de la réunion~La couleur des diapositives~Le nombre de chaises", 1,
     "Sans objectif clair, la réunion dérive et ne produit pas de décision."),
 QC("Quel rôle joue le secrétaire de réunion ?", "Animer le débat~Consigner décisions et actions~Prendre la parole en premier~Fixer l'ordre du jour seul", 1,
     "Le secrétaire rédige le compte rendu et suit les actions."),
 QC("Quel type de point appelle une décision ?", "Un point d'information~Un point de décision~Une pause~Une question rhétorique", 1,
     "L'ordre du jour distingue information, discussion et décision."),
 QC("Quelle technique permet de vérifier la compréhension ?", "La reformulation~Le silence absolu~La lecture intégrale~Le monologue", 0,
     "La reformulation confirme ce qui a été compris et corrige les malentendus."),
 QC("Quelle est une bonne pratique de support visuel ?", "Beaucoup de texte~Une idée par diapositive~Des polices minuscules~Des couleurs fluo partout", 1,
     "La simplicité visuelle favorise l'attention et la mémorisation."),
 QC("Que doit contenir le compte rendu ?", "Des anecdotes~Décisions, actions, responsables, échéances~Des photos~Un résumé vague", 1,
     "Le compte rendu est l'outil de suivi des engagements pris."),
 QC("Quel signe non verbal renforce la communication orale ?", "Un regard fuyant~Une posture droite et un regard circulaire~Des bras croisés~Un murmure", 1,
     "La posture et le regard contribuent à la crédibilité de l'orateur."),
 QC("Comment gérer un participant qui monopolise la parole ?", "L'ignorer totalement~Le remercier puis relancer les autres et recentrer~L'interrompre brutalement~Prolonger la réunion", 1,
     "L'animateur recentre le débat avec courtoisie et équité."),
 QT("Préparer l'ordre du jour d'une réunion de revue d'incident d'une heure.",
    "Ordre du jour proposé : 1) Accueil et rappel de l'objectif (5 min) : comprendre l'incident et définir des actions correctrices. 2) Rappel des faits par le responsable d'astreinte (10 min) : chronologie, systèmes touchés, impact. 3) Analyse des causes avec les équipes réseau, système et sécurité (15 min). 4) Points forts et points faibles de la réponse (10 min). 5) Décisions et plan d'action : responsables, échéances, indicateurs (15 min). 6) Tour de table court et clôture (5 min). Les documents à lire avant la séance sont le journal de crise et le compte rendu d'astreinte. Le secrétaire est désigné à l'avance, et le compte rendu sera diffusé dans les 24 heures.",
    "On attend objectif, durées, rôle de chacun, documents préalables et diffusion du compte rendu."),
 QT("Expliquer comment adapter une présentation orale à une salle de vingt personnes et à un comité de trois dirigeants.",
    "Devant vingt personnes, la voix doit porter, les gestes être visibles et les diapositives très lisibles ; on alterne regard circulaire et pauses, on prévoit un temps de questions plus long et on utilise des exemples généraux. Devant un comité restreint, le ton est plus conversationnel, les diapositives peuvent être réduites à quelques chiffres clés, et l'échange est plus direct : on répond individuellement, on reformule les préoccupations et on propose une recommandation explicite. Dans les deux cas, la structure reste context-problème-solution, mais le niveau de détail varie : le grand public technique attend des précisions, la direction attend l'impact, le coût et une décision. La préparation des questions critiques est indispensable dans les deux situations.",
    "On compare voix, supports, interactions et niveau de détail selon la taille et le rôle du public.")],
C("Animer une réunion, c'est préparer un objectif, conduire le temps et la parole, puis tracer des décisions exécutables.",
  "Réunion utile = décisions + responsables + échéances",
  "Ordre du jour · animateur · secrétaire · reformulation · compte rendu",
  "Objectif~Finalité de la réunion~Ordre du jour~Information, discussion, décision~Animateur~Gestion du temps~Secrétaire~Compte rendu~Synthèse~Décisions et actions",
  "Définir l'objectif|Inviter les bons participants|Préparer l'ordre du jour|Animer et reformuler|Diffuser le compte rendu",
  "Réunir sans ordre du jour|Laisser la dérive s'installer|Oublier le responsable d'une action|Tarder à diffuser le compte rendu",
  "Revue d'incident~1 heure~Chronologie~Rappel des faits~5 min~Accueil~15 min~Plan d'action~24 h~Diffusion du compte rendu",
  "Réunion~Décision collective~Brief~Information descendante",
  "Animateur~Conduit l'échange~Secrétaire~Trace les décisions"))

# ============================================================ CO4
add("CO4", "Gestion des conflits et communication de crise", "Communication", ["BTS2"],
S("Un conflit est une opposition d'intérêts, de points de vue ou de besoins entre personnes ou entre services."
  "|Il n'est pas nécessairement négatif : un désaccord technique traité correctement améliore souvent la décision finale."
  "|Les sources fréquentes en équipe informatique sont la charge de travail, la priorisation des incidents, le manque d'information et les différences de culture professionnelle."
  "|La gestion du conflit commence par l'écoute des positions et l'identification des intérêts sous-jacents, distincts des positions affichées."
  "|La reformulation et la recherche de faits communs permettent de dépasser les accusations et de revenir au problème."
  "|Les styles de traitement sont la compétition, l'accommodation, l'évitement, le compromis et la collaboration ; la collaboration est souvent la plus durable."
  "|Le compromis donne une satisfaction partielle à chacun ; la collaboration cherche une solution qui réponde mieux aux intérêts de tous."
  "|Le manager arbitre lorsque le désaccord persiste ou porte sur une décision engageante, en explicitant les critères de sa décision."
  "|Une communication de crise exige un porte-parole unique, des messages factuels, une fréquence annoncée et la distinction entre faits et hypothèses."
  "|Le silence prolongé est interprété comme une dissimulation : mieux vaut annoncer que l'on enquête et donner un prochain rendez-vous."
  "|Les réseaux sociaux et la rumeur interne amplifient les incohérences : une information officielle rapide limite les dégâts réputationnels."
  "|Après la crise, le retour d'expérience traite aussi la dimension humaine : stress, charge de travail et reconnaissance des équipes."),
[QC("Quelle est une source fréquente de conflit en équipe informatique ?", "La couleur des serveurs~La priorisation des incidents et la charge~La taille du bureau~Le nombre de réunions", 1,
     "Les arbitrages de priorité et la charge sont des sources classiques de tension."),
 QC("Quelle distinction est essentielle dans la gestion d'un conflit ?", "Position et intérêt~Voix et geste~Courriel et téléphone~Chef et subordonné", 0,
     "La position est ce que l'on demande ; l'intérêt est la raison profonde de cette demande."),
 QC("Quel style de traitement vise une solution qui satisfait les intérêts de tous ?", "La compétition~La collaboration~L'évitement~L'accommodation", 1,
     "La collaboration cherche une solution gagnant-gagnant durable."),
 QC("Quand le manager doit-il arbitrer ?", "Toujours immédiatement~Quand le désaccord persiste ou engage une décision~Jamais~Uniquement le vendredi", 1,
     "L'arbitrage est nécessaire lorsque le compromis n'est pas trouvé ou que la décision est engageante."),
 QC("Combien de porte-parole faut-il en communication de crise ?", "Autant que de services~Un seul mandaté~Deux pour équilibrer~Aucun", 1,
     "Un porte-parole unique évite les contradictions."),
 QC("Quel risque présente un silence prolongé en crise ?", "Aucun~Il est interprété comme une dissimulation~Il améliore la crédibilité~Il réduit le stress", 1,
     "Une information même partielle doit être donnée avec un prochain rendez-vous."),
 QC("Que faut-il distinguer dans un message de crise ?", "Les faits et les hypothèses~Le passé et le futur~Le prix et la qualité~Le client et le fournisseur", 0,
     "Présenter une hypothèse comme un fait détruit la crédibilité."),
 QC("Que traite le retour d'expérience après une crise ?", "Uniquement les aspects techniques~Les aspects techniques et humains~Les seuls coûts~La seule documentation", 1,
     "Stress, charge et reconnaissance font partie du bilan."),
 QT("Deux techniciens s'opposent sur l'ordre de priorité des correctifs : l'un veut traiter les postes utilisateurs, l'autre les serveurs. Proposer une méthode de résolution.",
    "On réunit les deux personnes et on demande à chacune d'expliquer sa position puis ses intérêts : continuité du travail des utilisateurs pour l'un, protection des services critiques et des données pour l'autre. On revient aux faits : quels systèmes sont exposés, combien d'utilisateurs sont concernés, quels sont les scores CVSS et les délais de déploiement. On construit ensuite une règle commune de priorisation qui combine criticité du système, exposition, nombre d'utilisateurs impactés et existence d'un exploit. Si l'accord reste impossible, le responsable hiérarchique arbitre en explicitant les critères retenus et la date de révision. La décision et son motif sont consignés dans le ticket afin que la règle serve aux incidents suivants.",
    "On passe des positions aux intérêts, aux faits, à une règle commune, puis à l'arbitrage tracé si nécessaire."),
 QT("Expliquer pourquoi une communication de crise doit être honnête sur ce que l'on ne sait pas encore.",
    "En situation d'incident, les informations sont incomplètes et évoluent. Annoncer avec certitude une cause non vérifiée, puis se dédire, détruit la crédibilité de l'organisation et alimente la rumeur. Une communication honnête distingue ce qui est établi, ce qui est probable et ce qui reste à déterminer ; elle indique ce qui est fait pour le savoir et quand une nouvelle information sera donnée. Cette posture protège juridiquement, car elle évite les déclarations inexactes, et elle rassure les parties prenantes : l'auditoire accepte mieux l'incertitude annoncée qu'un optimisme démenti. Elle facilite aussi la coordination interne, car chacun sait ce qui est confirmé et ce qui ne doit pas encore être diffusé.",
    "On relie crédibilité, distinction des niveaux de certitude, protection juridique et coordination interne.")],
C("Conflit et crise se gèrent par l'écoute, les faits, une décision tracée et une communication honnête sur le niveau de certitude.",
  "Intérêt sous-jacent ≠ position affichée",
  "Collaboration · arbitrage · porte-parole unique · faits et hypothèses",
  "Conflit~Opposition d'intérêts~Intérêt~Raison profonde~Collaboration~Solution commune~Arbitrage~Décision hiérarchique~Crise~Communication urgente",
  "Écouter les positions|Identifier les intérêts|Revenir aux faits|Chercher une règle commune|Communiquer et capitaliser",
  "Accuser sans écouter|Présenter une hypothèse comme un fait|Laisser plusieurs porte-parole|Oublier le bilan humain",
  "CVSS~Criticité technique~Exploit~Faille exploitée~Porte-parole~Message unique~Rumeur~Information non officielle~REX~Retour d'expérience~Faits~Éléments confirmés",
  "Compromis~Satisfaction partielle~Collaboration~Solution commune",
  "Position~Demande affichée~Intérêt~Besoin réel"))

# ============================================================ ME1
add("ME1", "Analyser une situation professionnelle : méthode en 4 étapes", "Méthodologie", ["BTS1"],
S("L'analyse de situation est une démarche structurée pour comprendre un problème réel avant de proposer une solution."
  "|La première étape consiste à collecter les faits : qui, quoi, quand, où, combien, dans quel contexte et avec quelles contraintes."
  "|La deuxième étape distingue les faits observés, les hypothèses et les opinions : cette séparation évite de confondre cause et symptôme."
  "|La troisième étape identifie les acteurs, leurs rôles, leurs intérêts et leurs relations : un problème technique est souvent aussi un problème organisationnel."
  "|La quatrième étape formule le problème sous forme de question et détermine les critères de réussite de la solution."
  "|Un arbre des causes ou un diagramme d'Ishikawa permet de classer les causes possibles par famille : méthodes, main-d'œuvre, matériel, milieu, mesures."
  "|La méthode des 5 Pourquoi creuse une cause en répétant la question jusqu'à atteindre une cause racine actionnable."
  "|Le principe de Pareto aide à prioriser : 20 % des causes produisent souvent 80 % des effets."
  "|Une bonne analyse s'appuie sur des données chiffrées : volumes, délais, taux d'erreur, coûts et fréquence des incidents."
  "|La solution proposée doit être réaliste : ressources disponibles, compétences, délai, coût et acceptabilité par les utilisateurs."
  "|La démarche se documente : une note d'analyse retrace le contexte, les faits, les causes retenues, les options et la recommandation."
  "|Cette méthode est transférable à tous les domaines du BTS CIEL : incident réseau, échec de recette, conflit d'équipe ou arbitrage de budget."),
[QC("Quelle est la première étape de l'analyse de situation ?", "Proposer une solution~Collecter les faits~Rédiger la conclusion~Blâmer un acteur", 1,
     "On ne peut analyser qu'à partir de faits établis et documentés."),
 QC("Quel outil classe les causes par familles ?", "Le diagramme d'Ishikawa~Le diagramme de Gantt~Le camembert~La matrice BCG", 0,
     "L'Ishikawa, ou arbre des causes, classe les causes en 5M."),
 QC("Que vise la méthode des 5 Pourquoi ?", "Trouver cinq coupables~Atteindre la cause racine~Remplir un formulaire~Réduire le nombre de réunions", 1,
     "La répétition du questionnement permet de dépasser les symptômes."),
 QC("Que signifie le principe de Pareto ?", "Toutes les causes ont le même poids~Une minorité de causes produit la majorité des effets~Il faut traiter toutes les causes~Les effets sont toujours égaux", 1,
     "La règle 80/20 guide la priorisation des actions."),
 QC("Que faut-il distinguer absolument ?", "Faits, hypothèses et opinions~Jours et mois~Serveurs et postes~Chefs et employés", 0,
     "Cette distinction garantit la rigueur de l'analyse."),
 QC("Quel critère ne concerne pas la faisabilité d'une solution ?", "Le coût~Le délai~Les compétences disponibles~La couleur du diaporama", 3,
     "La faisabilité porte sur les ressources, le temps et l'acceptabilité."),
 QC("Quelles sont les familles de l'Ishikawa ?", "Méthodes, main-d'œuvre, matériel, milieu, mesures~Prix, qualité, délai, marque, service~Ciel, terre, mer, air, feu~Mail, web, réseau, serveur, poste", 0,
     "Les 5M sont la référence classique du diagramme des causes."),
 QC("Que contient une note d'analyse ?", "Contexte, faits, causes, options, recommandation~Seulement une opinion~Des blagues~Une simple signature", 0,
     "La note retrace la démarche et conduit à une recommandation argumentée."),
 QT("Une entreprise constate une hausse des tickets « imprimante hors service ». Appliquer la méthode d'analyse en quatre étapes.",
    "Étape 1, collecte des faits : relever le nombre de tickets par semaine, les modèles concernés, les étages, les heures, les messages d'erreur et les délais d'intervention. Étape 2, distinction : les faits sont les volumes et les codes d'erreur ; l'hypothèse est le manque de toner ; l'opinion est « le matériel est de mauvaise qualité ». Étape 3, acteurs : utilisateurs, service support, fournisseur de cartouches, responsable des achats, chacun avec un rôle et des contraintes. Étape 4, formulation : « Quelle est la cause de la hausse des pannes d'impression et quelle action réduit les tickets de 50 % en un mois ? » avec des critères de réussite chiffrés. On approfondit avec un Ishikawa et un Pareto avant de recommander, par exemple, un contrat de maintenance ou une commande groupée de consommables.",
    "On suit les quatre étapes, on illustre chacune avec des éléments concrets et on formule une question avec critères."),
 QT("Expliquer la différence entre cause et symptôme, et pourquoi la confusion est fréquente dans le support informatique.",
    "Le symptôme est ce que l'on observe : « le poste ne se connecte plus au réseau », « le serveur est lent ». La cause est le mécanisme qui produit le symptôme : câble endommagé, DHCP saturé, processus consommateur de CPU. La confusion est fréquente car le support est sous pression : on applique une action visible qui fait disparaître le symptôme, comme redémarrer le poste, sans chercher pourquoi le problème revient. Le redémarrage traite l'effet, pas la cause. Une démarche structurée avec les 5 Pourquoi et des données chiffrées permet de remonter à la cause racine et d'éviter la récidive, ce qui réduit la charge à long terme même si le diagnostic prend quelques minutes de plus.",
    "On définit les deux notions, on explique la pression du support et l'illusion du redémarrage, puis la valeur de la cause racine.")],
C("Analyser une situation, c'est passer des faits aux causes puis à une recommandation faisable, en séparant observations, hypothèses et opinions.",
  "4 étapes : faits · distinction · acteurs · question et critères",
  "Ishikawa 5M · 5 Pourquoi · Pareto 80/20 · note d'analyse",
  "Faits~Observations vérifiables~Hypothèse~Explication à vérifier~Ishikawa~Causes par familles~5 Pourquoi~Cause racine~Pareto~Priorité 80/20",
  "Collecter les faits chiffrés|Séparer faits et hypothèses|Cartographier les acteurs|Rechercher la cause racine|Formuler et documenter la recommandation",
  "Confondre symptôme et cause|Blâmer un acteur sans preuve|Proposer avant d'avoir analysé|Négliger les critères de réussite",
  "Tickets imprimante~Exemple d'analyse~5M~Familles de causes~50 %~Objectif chiffré~Redémarrage~Traitement du symptôme~Note~Trace écrite",
  "Symptôme~Effet observé~Cause~Mécanisme profond",
  "Fait~Vérifiable~Opinion~Jugement personnel"))

# ============================================================ ME2
add("ME2", "Résolution de problème et outils d'amélioration continue", "Méthodologie", ["BTS1"],
S("La résolution de problème est une démarche itérative qui vise à supprimer durablement un écart entre l'état actuel et l'état souhaité."
  "|Le cycle PDCA structure l'amélioration : Planifier, Faire, Vérifier, Agir, puis recommencer."
  "|Dans sa version étendue DMAIC (Define, Measure, Analyze, Improve, Control), la méthode Six Sigma formalise les étapes d'un projet d'amélioration."
  "|La première étape définit le problème, le périmètre, les parties prenantes et l'objectif chiffré."
  "|La mesure s'appuie sur des données fiables : volumétrie, délais, taux de défaut, coût par incident et satisfaction utilisateur."
  "|L'analyse identifie la cause racine avec l'Ishikawa, les 5 Pourquoi et une validation par les données."
  "|L'amélioration propose une action, la teste à petite échelle puis généralise si les résultats sont concluants."
  "|Le contrôle met en place des indicateurs de suivi et une procédure pour éviter le retour au problème initial."
  "|Un indicateur pertinent est spécifique, mesurable, accessible, régulier et relié à une décision."
  "|La boucle de retour d'expérience transforme l'incident en connaissance : causes, actions, résultats et enseignements sont archivés."
  "|Les outils de la qualité incluent également la fiche de recueil de données, l'histogramme, le diagramme de Pareto et la carte de contrôle."
  "|En informatique, cette démarche s'applique aussi bien à la réduction des incidents qu'à l'amélioration du parcours utilisateur ou de la productivité de l'équipe."),
[QC("Que signifie PDCA ?", "Plan, Do, Check, Act~Plan, Data, Control, Audit~Prepare, Decide, Check, Apply~Projet, Développement, Contrôle, Analyse", 0,
     "PDCA correspond à Planifier, Faire, Vérifier, Agir."),
 QC("Que signifie la lettre A dans DMAIC ?", "Analyse~Améliorer~Auditer~Attendre", 1,
     "DMAIC : Define, Measure, Analyze, Improve, Control ; Improve signifie améliorer."),
 QC("Quel est l'objet de l'étape Mesurer ?", "Proposer une solution~Collecter des données fiables sur le problème~Clore le projet~Former les utilisateurs", 1,
     "On quantifie l'écart avant de chercher des causes."),
 QC("Quel outil valide la cause racine ?", "Une opinion~Les données et un test~Une rumeur~Le hasard", 1,
     "Une cause n'est retenue que si les données et un essai la confirment."),
 QC("Pourquoi tester une action à petite échelle ?", "Pour augmenter le coût~Pour limiter le risque avant généralisation~Pour éviter les indicateurs~Pour supprimer la documentation", 1,
     "Le test pilote permet de vérifier l'effet et d'ajuster avant déploiement."),
 QC("Quel est le rôle de l'étape Contrôle ?", "Oublier le problème~Éviter la réapparition avec des indicateurs~Recommencer à zéro~Supprimer les procédures", 1,
     "Le contrôle institutionnalise la nouvelle méthode et suit les indicateurs."),
 QC("Quelle qualité d'un indicateur est essentielle ?", "Il doit être complexe~Il doit être mesurable et relié à une décision~Il doit changer chaque jour~Il doit être secret", 1,
     "Un indicateur inexploitable ne pilote rien."),
 QC("Quel est l'apport du retour d'expérience ?", "Supprimer les incidents~Transformer l'incident en connaissance réutilisable~Remplacer les procédures~Réduire les effectifs", 1,
     "Le REX capitalise causes, actions et enseignements pour l'avenir."),
 QT("Une équipe support met en place une base de connaissances pour réduire les tickets répétitifs. Décrire la démarche PDCA complète.",
    "Plan : mesurer le nombre de tickets récurrents sur un mois, identifier les dix questions les plus fréquentes, fixer un objectif de baisse de 30 % et désigner un responsable. Do : rédiger dix fiches courtes et validées, les publier dans la base, les lier au ticket et informer l'équipe. Check : après un mois, comparer le volume de tickets récurrents, mesurer le taux de consultation des fiches et recueillir le retour des utilisateurs et des techniciens. Act : corriger les fiches les moins utiles, ajouter de nouveaux sujets, intégrer la mise à jour de la base dans la procédure d'incident et recommencer le cycle avec un nouvel objectif. Les résultats et les décisions sont archivés dans le compte rendu d'amélioration.",
    "On décrit les quatre phases avec objectifs, actions, mesure et capitalisation, avec des indicateurs."),
 QT("Expliquer pourquoi une action correctrice peut échouer malgré une bonne intention.",
    "Une action peut échouer parce qu'elle traite le symptôme plutôt que la cause racine, parce que la cause n'a pas été validée par les données, ou parce que le contexte a changé. Elle peut aussi être inadaptée aux ressources : procédure trop longue, outils manquants, compétences insuffisantes ou charge de travail qui décourage son application. La résistance au changement est un facteur majeur : les utilisateurs reviennent à leurs habitudes si la nouvelle méthode n'est ni expliquée ni soutenue. Enfin, sans indicateur de suivi, on ne détecte pas que l'action ne fonctionne pas et on la maintient malgré les signaux contraires. Le cycle PDCA et un test pilote réduisent ces risques en imposant mesure, ajustement et capitalisation.",
    "On cite cause mal identifiée, ressources, résistance au changement et absence d'indicateurs.")],
C("L'amélioration continue est un cycle : mesurer, analyser, tester, contrôler, puis recommencer avec des preuves et des indicateurs.",
  "PDCA = Plan, Do, Check, Act · DMAIC = Define, Measure, Analyze, Improve, Control",
  "Cause racine · test pilote · indicateur pertinent · retour d'expérience",
  "PDCA~Cycle d'amélioration~DMAIC~Méthode structurée~Mesure~Données fiables~Cause racine~Validation par essai~Contrôle~Indicateurs de suivi",
  "Définir l'écart et l'objectif|Mesurer la situation|Analyser la cause|Test puis généraliser|Contrôler et recommencer",
  "Agir sans mesurer|Confondre cause et symptôme|Généraliser sans test|Ne jamais vérifier l'effet",
  "30 %~Objectif de baisse~10 fiches~Base de connaissances~1 mois~Période de mesure~REX~Capitalisation~Pareto~Priorisation",
  "PDCA~Amélioration itérative~DMAIC~Version détaillée",
  "Action correctrice~Traite la cause~Action palliative~Traite le symptôme"))

# ============================================================ ME3
add("ME3", "Recherche documentaire et évaluation des sources", "Méthodologie", ["BTS2"],
S("La recherche documentaire vise à trouver l'information fiable et pertinente nécessaire à une décision ou à un rapport."
  "|Elle commence par l'analyse du besoin : question précise, mots-clés, période, type de document et niveau de fiabilité requis."
  "|Les sources primaires sont les textes officiels, les données brutes et les témoignages directs ; les sources secondaires les commentent ou les synthétisent."
  "|Pour le BTS CIEL, les sources de référence sont le BO, Légifrance, l'ANSSI, la CNIL, éduscol, les RFC, les normes ISO et les documentations constructeurs."
  "|Un moteur de recherche donne des résultats classés par pertinence, mais le classement n'est pas une garantie de fiabilité."
  "|Les opérateurs de recherche améliorent la précision : guillemets pour une expression exacte, site: pour limiter à un domaine, signe moins pour exclure un terme."
  "|L'évaluation d'une source repose sur quatre critères : autorité, actualité, pertinence et exactitude."
  "|La date de publication et la date de mise à jour sont déterminantes pour les normes, les versions logicielles et les textes réglementaires."
  "|Les réseaux sociaux, forums et blogs peuvent orienter la recherche mais ne constituent pas une preuve : ils doivent être recoupés avec une source officielle."
  "|Le plagiat consiste à reprendre des idées ou des mots sans citation : il doit être évité par une reformulation et une référence explicite."
  "|La bibliographie indique les sources consultées avec leur titre, leur auteur ou organisme, leur date et leur URL."
  "|Une veille efficace limite le nombre de sources à quelques références fiables et organise leur suivi dans le temps."),
[QC("Quel est un exemple de source primaire ?", "Un blog d'opinion~Un texte officiel publié au Journal officiel~Un résumé de cours~Une vidéo humoristique", 1,
     "Les textes officiels et les données brutes sont des sources primaires."),
 QC("Quel opérateur limite une recherche à un site précis ?", "site:~guillemets~moins~ET", 0,
     "L'opérateur site: suivi d'un domaine restreint les résultats."),
 QC("Quels critères évaluent une source ?", "Autorité, actualité, pertinence, exactitude~Longueur, couleur, police, taille~Prix, marque, pays, langue~Auteur, hasard, mode, chance", 0,
     "Ces quatre critères constituent une grille d'évaluation classique."),
 QC("Quelle source est préférable pour une question de sécurité ?", "Un forum anonyme~Un bulletin ANSSI~Une publication publicitaire~Un commentaire isolé", 1,
     "L'ANSSI est une autorité nationale compétente en cybersécurité."),
 QC("Que désigne le plagiat ?", "Citer sa source~Reprendre sans citation~Reformuler en citant~Consulter plusieurs sources", 1,
     "L'absence de citation transforme la reprise en plagiat."),
 QC("Que doit contenir une bibliographie ?", "Titre, auteur ou organisme, date et URL~Une simple liste de noms~Des couleurs~La date du jour uniquement", 0,
     "Ces éléments permettent de retrouver et de dater la source."),
 QC("Pourquoi vérifier la date d'une norme ?", "Les normes changent rarement mais une version obsolète peut être remplacée~Les dates n'ont aucune importance~Pour compléter la bibliographie~Pour choisir une couleur", 0,
     "Une version ancienne peut ne plus être en vigueur."),
 QC("Quel est un rôle des moteurs de recherche ?", "Garantir la vérité~Classer des résultats selon une pertinence calculée~Certifier les sources~Remplacer l'esprit critique", 1,
     "Le classement est une aide, pas une validation de fiabilité."),
 QT("Un étudiant prépare un exposé sur le RGPD en BTS CIEL. Proposer une stratégie de recherche en cinq étapes.",
    "Il définit d'abord sa question : quelles obligations du RGPD concernent une entreprise qui traite des données de salariés ? Il choisit ensuite des mots-clés français et anglais : RGPD, responsable de traitement, sous-traitant, registre, notification 72 heures, article 28. Il limite la recherche à des domaines fiables avec site:legifrance.gouv.fr, site:cnil.fr et site:eduscol.education.fr, puis complète avec un manuel ou une documentation spécialisée. Il évalue chaque source retenue selon l'autorité de l'organisme, sa date de mise à jour et sa pertinence par rapport à sa question, en écartant les blogs non référencés. Enfin, il lit les textes, note les références exactes avec URL et date de consultation, construit son plan et rédige en reformulant avec des citations courtes pour les formules légales.",
    "On attend définition de la question, mots-clés, sources officielles, grille d'évaluation et bibliographie."),
 QT("Expliquer pourquoi un forum peut être utile sans pouvoir servir de preuve dans un rapport technique.",
    "Un forum donne accès à des retours d'expérience concrets, à des messages d'erreur réels et à des pistes de diagnostic que les documentations officielles ne détaillent pas toujours. Il peut orienter la recherche et faire gagner du temps. En revanche, l'information n'y est pas vérifiée : elle peut être obsolète, inexacte, propre à un environnement particulier ou simplement fausse. Un rapport technique engage la responsabilité de son auteur : les affirmations doivent être étayées par des sources vérifiables et à jour. L'usage correct consiste donc à recouper la piste trouvée sur un forum avec une documentation constructeur, une RFC, un avis ANSSI ou un texte réglementaire, puis à citer uniquement la source fiable dans le rapport.",
    "On reconnaît l'intérêt pratique du forum, puis on exige recoupement et citation de sources vérifiables.")],
C("La recherche documentaire combine requêtes précises et esprit critique : autorité, date et recoupement déterminent la fiabilité.",
  "Sources primaires = textes officiels et données brutes",
  "site: · guillemets · ANSSI/CNIL/Légifrance/BO · bibliographie",
  "Besoin~Question et mots-clés~Source primaire~Texte officiel~Source secondaire~Commentaire~Opérateur~site: et guillemets~Autorité~Critère de fiabilité",
  "Analyser le besoin|Choisir mots-clés et opérateurs|Repérer les sources officielles|Évaluer autorité et date|Recouper et citer",
  "Croire le premier résultat|Utiliser un forum comme preuve|Oublier la date de publication|Reprendre un texte sans citation",
  "72 heures~Délai RGPD~Article 28~Sous-traitance~CNIL~Autorité de contrôle~Légifrance~Texte officiel~URL~Référence bibliographique~BO~Bulletin officiel",
  "Source primaire~Document d'origine~Source secondaire~Analyse ou synthèse",
  "Pertinence~Répond à la question~Exactitude~Information vérifiée"))

# ============================================================ ME4
add("ME4", "Préparer et réussir sa soutenance de projet", "Méthodologie", ["BTS2"],
S("La soutenance de projet est un exercice de communication qui évalue la démarche suivie autant que le résultat obtenu."
  "|En option IR du BTS CIEL, l'épreuve E6 évalue la valorisation de la donnée et la cybersécurité à travers un projet technique et sa présentation."
  "|Le dossier de synthèse présente le contexte, le besoin, les choix techniques, la réalisation, les tests et le bilan, avec des annexes lisibles."
  "|L'oral suit généralement une structure : introduction, contexte et besoin, analyse et choix, réalisation, résultats, limites et conclusion."
  "|Le temps est une contrainte forte : il faut répéter avec un chronomètre et prévoir une marge pour les questions du jury."
  "|Un support visuel sobre accompagne le propos : une idée par diapositive, des schémas d'architecture lisibles et des chiffres clés."
  "|Le schéma d'architecture doit montrer les équipements, les liens, les adresses et les flux, avec une légende claire."
  "|La démonstration technique, si elle est prévue, doit être préparée et accompagnée d'un plan B en cas de problème réseau ou matériel."
  "|Le jury attend une explicitation des choix : pourquoi ce protocole, cette topologie, cette règle de sécurité, cette méthode de test ?"
  "|Les limites du projet doivent être assumées : contraintes de temps, de budget, de compatibilité ou de sécurité non traitée."
  "|La gestion du stress repose sur la préparation, la respiration, un débit modéré et l'usage de fiches de mots-clés plutôt que d'un texte intégral."
  "|Une soutenance réussie se conclut par une synthèse courte et une ouverture sur les évolutions possibles du projet."),
[QC("Que privilégie le jury lors d'une soutenance ?", "La seule beauté du diaporama~La démarche, les choix et les résultats expliqués~La longueur de l'oral~Le nombre de diapositives", 1,
     "Le jury évalue la compréhension et la justification de la démarche."),
 QC("Que contient un dossier de synthèse ?", "Contexte, besoin, choix, réalisation, tests, bilan et annexes~Uniquement des photos~Une liste de cours~Le programme de l'année", 0,
     "Le dossier retrace tout le cycle du projet et renvoie aux preuves en annexe."),
 QC("Quelle règle pour un support visuel efficace ?", "Une idée par diapositive~Dix paragraphes par diapositive~Des polices minuscules~Aucun titre", 0,
     "La clarté visuelle permet au jury de suivre sans effort."),
 QC("Quel élément doit apparaître sur un schéma d'architecture ?", "Les équipements, liens, adresses et une légende~Une photo du bâtiment~La liste des étudiants~Le prix des câbles", 0,
     "Un schéma technique lisible est un livrable central du projet IR."),
 QC("Pourquoi prévoir un plan B pour la démonstration ?", "Pour impressionner le jury~Pour faire face à une panne réseau ou matérielle~Pour allonger l'oral~Pour éviter les questions", 1,
     "Une capture ou une vidéo de secours sécurise la démonstration."),
 QC("Quelle question du jury faut-il anticiper ?", "Pourquoi ce choix technique plutôt qu'un autre ?~Quel est votre plat préféré ?~Quelle heure est-il ?~Combien de diapositives avez-vous ?", 0,
     "La justification des choix techniques est au cœur de l'évaluation."),
 QC("Comment gérer le stress avant un oral ?", "Répéter chronométré et préparer des mots-clés~Lire un texte intégral~Ne pas dormir~Éviter toute répétition", 0,
     "La préparation et une bonne respiration réduisent le stress."),
 QC("Que faire de ses fiches de mots-clés ?", "Les lire intégralement~S'en servir comme appui visuel~Les cacher au jury~Les réciter par cœur", 1,
     "Les fiches soutiennent l'oral sans le remplacer."),
 QT("Construire le plan d'un oral de 15 minutes pour un projet de sécurisation d'un réseau d'entreprise.",
    "Introduction (1 min) : présentation, titre du projet et annonce du plan. Contexte et besoin (2 min) : l'entreprise, les 40 postes, les deux serveurs, l'absence de segmentation et les incidents constatés. Analyse et choix (4 min) : risques identifiés, comparaison des solutions envisageables, choix des VLAN, du firewall, de la MFA et de la supervision, avec justification. Réalisation (4 min) : schéma d'architecture, plan d'adressage, configuration, tests de connectivité et de restriction des flux, démonstration courte si possible. Résultats et limites (2 min) : indicateurs de conformité, éléments non traités et contraintes. Conclusion (1 min) : bilan, apports personnels et évolutions possibles. On garde environ cinq minutes pour les questions en prévoyant une marge dans la répétition.",
    "On propose une répartition des 15 minutes avec une place pour la justification, les limites et les questions."),
 QT("Expliquer comment répondre à une question du jury à laquelle on ne connaît pas la réponse.",
    "On commence par reformuler la question pour s'assurer de l'avoir comprise et on garde une posture calme : reconnaître une limite n'est pas un échec. On distingue ensuite ce que l'on sait de ce que l'on ignore : on expose les éléments de réponse solides, les hypothèses raisonnables et la méthode que l'on utiliserait pour vérifier, par exemple consulter la documentation constructeur, tester en laboratoire ou s'appuyer sur une norme. On peut proposer une piste de réponse argumentée en la présentant comme telle, puis indiquer ce que l'on ferait différemment avec plus de temps. Cette honnêteté est appréciée car elle montre l'esprit critique et la rigueur, qualités attendues d'un futur technicien.",
    "On préconise reformulation, distinction entre su et ignoré, méthode de vérification et honnêteté assumée.")],
C("Une soutenance réussie raconte une démarche, justifie des choix, montre des preuves et assume les limites dans un temps maîtrisé.",
  "Oral = contexte · analyse et choix · réalisation · résultats · limites",
  "Dossier de synthèse · schéma d'architecture · démonstration · plan B · gestion du stress",
  "Dossier~Synthèse écrite du projet~Oral~Présentation structurée~Schéma~Architecture et flux~Choix techniques~Justification~Limites~Contraintes assumées",
  "Rédiger le dossier et les annexes|Construire un plan chronométré|Préparer schémas et démonstration|Répéter avec des mots-clés|Anticiper les questions",
  "Lire un texte intégral|Surcharger les diapositives|Ignorer les limites du projet|Improviser la démonstration",
  "15 minutes~Durée d'oral~40 postes~Exemple de contexte~5 minutes~Marge pour les questions~Plan B~Capture de secours~E6~Unité de projet IR",
  "Démonstration~Preuve de fonctionnement~Schéma~Preuve de conception",
  "Chronomètre~Maîtrise du temps~Mots-clés~Appui à l'oral"))

# ============================================================ CG1
add("CG1", "Comptabilité générale : bilan et compte de résultat", "Comptabilité et gestion", ["BTS1"],
S("La comptabilité générale enregistre, classe et synthétise les opérations d'une organisation selon le plan comptable général."
  "|Le bilan décrit à une date donnée l'actif, c'est-à-dire ce que l'entreprise possède, et le passif, c'est-à-dire où elle a trouvé les ressources pour le financer."
  "|L'actif se divise en actif immobilisé (usage durable) et actif circulant (stocks, créances, disponibilités)."
  "|Le passif comprend les capitaux propres, les provisions et les dettes, classées selon leur échéance."
  "|Le principe de dualité impose que chaque opération modifie au moins deux comptes pour un montant égal : l'égalité actif = passif est toujours respectée."
  "|Le compte de résultat retrace les produits et les charges de l'exercice et fait ressortir le résultat : produit = recette, charge = dépense."
  "|Le résultat se calcule par différence entre les produits et les charges ; il est bénéficiaire si les produits l'emportent."
  "|Le plan comptable général organise les comptes en classes : 1 capitaux, 2 immobilisations, 3 stocks, 4 tiers, 5 comptes financiers, 6 charges, 7 produits."
  "|Le principe de indépendance des exercices impose de rattacher chaque opération à la période qui la concerne, quel que soit le paiement."
  "|Les amortissements répartissent la valeur d'une immobilisation sur sa durée d'utilisation : ils représentent l'usure et la perte de valeur."
  "|Les provisions constatent des risques ou des charges probables dont le montant ou l'échéance est incertain."
  "|Pour un projet informatique, distinguer une dépense d'investissement (immobilisation) et une dépense de fonctionnement (charge) est un arbitrage comptable important."),
[QC("Que décrit le bilan ?", "Les seules recettes de l'année~Actif et passif à une date donnée~Les salaires~Les seuls clients", 1,
     "Le bilan est un état patrimonial à une date précise."),
 QC("Quel principe impose l'égalité actif = passif ?", "La dualité~La continuité~La prudence~La régularité", 0,
     "Chaque opération affecte au moins deux comptes pour un montant égal."),
 QC("Dans quelle classe du PCG se trouvent les charges ?", "Classe 1~Classe 4~Classe 6~Classe 7", 2,
     "La classe 6 regroupe les charges ; la classe 7 les produits."),
 QC("Que calcule le compte de résultat ?", "Le résultat de l'exercice~Le nombre de salariés~La valeur des immobilisations~La trésorerie disponible", 0,
     "Il fait ressortir le bénéfice ou la perte par différence produits - charges."),
 QC("Qu'est-ce qu'un amortissement ?", "Un impôt~La répartition de la valeur d'une immobilisation sur sa durée de vie~Une subvention~Une dette", 1,
     "L'amortissement constate l'usure ou l'obsolescence d'un actif immobilisé."),
 QC("Quel est un élément de l'actif circulant ?", "Un terrain~Une créance client~Un brevet~Une immobilisation corporelle", 1,
     "Les créances, stocks et disponibilités forment l'actif circulant."),
 QC("Que constate une provision ?", "Un produit certain~Un risque ou une charge probable~Une recette exceptionnelle~Un capital", 1,
     "La provision répond au principe de prudence."),
 QC("Comment classer l'achat d'un serveur utilisé trois ans ?", "Charge de fonctionnement~Immobilisation amortissable~Produit~Provision", 1,
     "Un équipement durable est immobilisé puis amorti sur sa durée d'utilisation."),
 QT("Une entreprise achète un serveur 12 000 € hors taxes, utilisé pendant trois ans, avec une valeur résiduelle nulle. Expliquer le traitement comptable et calculer l'amortissement annuel en mode linéaire.",
    "Le serveur est une immobilisation corporelle : il est inscrit à l'actif du bilan pour 12 000 € et financé par un compte de dettes ou de trésorerie, ce qui respecte la dualité. Il n'est pas comptabilisé directement en charge car il rend des services sur plusieurs exercices. En mode linéaire, l'amortissement annuel vaut (valeur d'origine − valeur résiduelle) / durée d'utilisation, soit (12 000 − 0) / 3 = 4 000 € par an. Chaque année, une charge d'amortissement de 4 000 € est constatée au compte de résultat et un amortissement cumulé vient réduire la valeur nette comptable au bilan. Après trois ans, la valeur nette est nulle et le serveur peut être sorti de l'actif.",
    "On qualifie l'immobilisation, on rappelle la dualité, puis on calcule 12 000 / 3 = 4 000 € par an."),
 QT("Expliquer la différence entre le résultat comptable et la trésorerie, et pourquoi une entreprise bénéficiaire peut manquer de liquidités.",
    "Le résultat comptable est calculé selon la indépendance des exercices : les produits sont rattachés à la période de la vente, même si le client paie plus tard, et les charges à celle de la consommation, même si le fournisseur n'est pas encore réglé. La trésorerie, elle, enregistre les mouvements d'argent réels. Une entreprise peut donc être bénéficiaire tout en ayant un besoin de trésorerie : ses clients paient à 60 jours alors qu'elle règle ses fournisseurs et ses salaires à 30 jours. Les stocks immobilisent aussi des liquidités, et les investissements génèrent des décaissements immédiats alors que leurs effets s'étalent sur plusieurs années. Le suivi du besoin en fonds de roulement et du plan de trésorerie complète le compte de résultat pour piloter l'entreprise.",
    "On oppose rattachement à l'exercice et mouvements réels, puis on cite délais de paiement, stocks et investissements.")],
C("La comptabilité générale décrit le patrimoine au bilan et l'activité au compte de résultat, selon la dualité et la indépendance des exercices.",
  "Actif = passif · résultat = produits − charges",
  "PCG classes 1 à 7 · amortissements · provisions",
  "Actif~Biens et droits~Passif~Financements~Dualité~Deux comptes par opération~Compte de résultat~Produits et charges~Amortissement~Usure de l'actif",
  "Identifier la nature de l'opération|Choisir les comptes du PCG|Respecter la dualité|Rattacher à la bonne période|Synthétiser dans les états financiers",
  "Confondre charge et immobilisation|Oublier la TVA dans un prix HT|Ignorer la date de rattachement|Croire que bénéfice et trésorerie sont identiques",
  "12 000 €~Coût du serveur~3 ans~Durée d'utilisation~4 000 €~Amortissement annuel~60 jours~Délai client~Classe 6~Charges~Classe 7~Produits",
  "Bilan~Patrimoine à une date~Compte de résultat~Activité sur une période",
  "Amortissement~Perte de valeur progressive~Provision~Risque probable"))

# ============================================================ CG2
add("CG2", "Coûts et contrôle de gestion appliqués à l'informatique", "Comptabilité et gestion", ["BTS1"],
S("Le contrôle de gestion aide les responsables à piloter l'activité en comparant les objectifs et les réalisations."
  "|Un centre de coûts est une unité à laquelle on affecte des charges : un service, un projet, une application ou un site."
  "|Le coût complet d'un service informatique additionne les coûts directs et une part des coûts indirects répartie selon une clé de répartition."
  "|Les clés de répartition courantes sont le nombre d'utilisateurs, le temps de traitement, la surface, le nombre de postes ou le volume de données."
  "|Le coût variable évolue avec l'activité ; le coût fixe reste constant dans une plage d'activité donnée."
  "|Le coût marginal correspond au coût d'une unité supplémentaire de service, par exemple une machine virtuelle de plus."
  "|La marge sur coûts variables aide à décider d'une tarification interne ou d'une externalisation."
  "|Le budget prévisionnel est exprimé en coûts et en volumes : il sert de référence pour mesurer les écarts."
  "|L'analyse des écarts distingue un écart de volume (activité différente du prévu) et un écart de prix ou de coût unitaire."
  "|Un écart défavorable peut venir d'un surcoût de licences, d'une panne prolongée ou d'une sous-estimation du temps de développement."
  "|Les indicateurs de pilotage incluent le coût par ticket, le coût par poste et par an, le taux d'utilisation des ressources et le respect du budget."
  "|Le contrôle de gestion ne vise pas seulement à réduire les coûts : il évalue aussi la valeur produite par le système d'information."),
[QC("Qu'appelle-t-on un centre de coûts ?", "Un service auquel on affecte des charges~Un logiciel de facturation~Un serveur de base de données~Un client important", 0,
     "Le centre de coûts est une unité de suivi des charges."),
 QC("Quelle est une clé de répartition ?", "Le nombre d'utilisateurs~La couleur des bureaux~Le hasard~Le nom du fournisseur", 0,
     "Une clé doit être pertinente et mesurable : utilisateurs, temps, volume ou surface."),
 QC("Que désigne un coût marginal ?", "Le coût moyen~Le coût d'une unité supplémentaire~Le coût total~Le coût fixe", 1,
     "C'est l'augmentation de coût due à une unité de plus."),
 QC("Quel écart est lié à une activité différente du prévu ?", "Un écart de prix~Un écart de volume~Un écart de change~Un écart de qualité", 1,
     "L'écart de volume traduit une différence de quantité d'activité."),
 QC("Quel indicateur mesure le coût de la maintenance ?", "Le coût par ticket~Le nombre de câbles~La taille du bureau~Le nombre de réunions", 0,
     "Le coût par ticket est un indicateur courant du support."),
 QC("Comment calculer un coût complet ?", "Coûts directs seulement~Coûts directs plus part des coûts indirects~Charges futures~Seuls les salaires", 1,
     "Le coût complet inclut les charges directes et une quote-part des charges indirectes."),
 QC("Que permet la marge sur coûts variables ?", "De supprimer les coûts fixes~D'aider à une décision de prix ou d'externalisation~De calculer un amortissement~De rédiger un contrat", 1,
     "Elle indique la contribution de chaque unité à la couverture des frais fixes."),
 QC("Quel objectif dépasse la seule réduction des coûts ?", "Évaluer la valeur produite par le SI~Supprimer tout investissement~Réduire les effectifs à zéro~Ignorer la qualité", 0,
     "Le contrôle de gestion relie coût et valeur pour éclairer la décision."),
 QT("Un service informatique a 120 000 € de coûts indirects à répartir entre trois départements de 40, 60 et 80 utilisateurs. Calculer les quote-parts selon la clé nombre d'utilisateurs.",
    "Le nombre total d'utilisateurs est 40 + 60 + 80 = 180. Le coût par utilisateur est 120 000 / 180 = 666,67 €. Le département A supporte 40 × 666,67 = 26 666,67 €, le département B 60 × 666,67 = 40 000 € et le département C 80 × 666,67 = 53 333,33 €. La somme des trois quote-parts vaut bien 120 000 €. On vérifie que la clé choisie est pertinente : si les coûts sont liés aux licences par utilisateur, cette clé est adaptée ; s'ils viennent surtout de l'énergie des serveurs, une clé fondée sur la consommation de ressources serait plus juste.",
    "On calcule la clé unitaire, les trois quote-parts, on vérifie la somme et on discute de la pertinence de la clé."),
 QT("Expliquer comment analyser un écart de budget sur une année et proposer des actions correctives.",
    "On compare d'abord le budget prévu et le réalisé poste par poste : licences, matériel, prestations, salaires, énergie. On mesure l'écart en valeur et en pourcentage, puis on le décompose : écart de volume, par exemple plus de postes que prévu, et écart de prix, par exemple une hausse du tarif d'hébergement. On identifie ensuite les causes : croissance non budgétée, panne coûteuse, retard de projet, erreur d'estimation ou changement de fournisseur. Les actions correctrices peuvent être une renégociation contractuelle, une optimisation des ressources cloud, un étalement des achats, une révision du périmètre ou une provision complémentaire. On documente l'analyse, on informe la direction et on révise le budget des prochaines années avec des hypothèses plus réalistes.",
    "On décompose l'écart en volume et prix, on cherche les causes, puis on propose et documente des actions.")],
C("Le contrôle de gestion relie coûts et activité : centres de coûts, clés de répartition et analyse des écarts guident la décision.",
  "Coût complet = directs + quote-part des indirects",
  "Centre de coûts · clé de répartition · coût marginal · écart volume/prix",
  "Centre de coûts~Unité de suivi~Coût direct~Affecté au service~Coût indirect~Réparti~Clé~Utilisateurs ou volume~Écart de volume~Activité différente~Écart de prix~Coût unitaire différent",
  "Définir les centres de coûts|Choisir une clé de répartition|Calculer les coûts complets|Comparer prévu et réalisé|Expliquer et corriger les écarts",
  "Répartir au hasard|Confondre écart de prix et de volume|Ne regarder que le total|Oublier de documenter l'analyse",
  "120 000 €~Charges indirectes~180 utilisateurs~Total de la clé~666,67 €~Coût par utilisateur~40/60/80~Quote-parts~Ticket~Indicateur de support",
  "Coût fixe~Constant dans une plage~Coût variable~Dépend de l'activité",
  "Coût complet~Toutes charges~Coût marginal~Une unité de plus"))

# ============================================================ CG3
add("CG3", "Budget prévisionnel et suivi budgétaire d'un projet SI", "Comptabilité et gestion", ["BTS2"],
S("Le budget prévisionnel traduit en chiffres les ressources nécessaires à une activité ou à un projet sur une période donnée."
  "|Il distingue les dépenses d'investissement, comme l'achat de serveurs, et les dépenses de fonctionnement, comme les licences annuelles ou la maintenance."
  "|Un budget se construit à partir d'hypothèses explicites : volumes, prix unitaires,effectifs, durée, taux d'inflation et calendrier."
  "|Le principe de précaution recommande de prévoir une réserve pour imprévus, souvent exprimée en pourcentage du budget total."
  "|Le budget est un outil de prévision mais aussi de contrôle : il sert de référence pour mesurer les écarts en cours de projet."
  "|Le suivi budgétaire compare les dépenses engagées, les dépenses réalisées et le budget consommé à chaque jalon."
  "|Le taux de consommation budgétaire rapporte le montant dépensé au budget prévu à la même date."
  "|Un dépassement peut venir d'un retard, d'une augmentation des prix, d'un périmètre élargi ou d'une sous-estimation initiale."
  "|La règle des 50/50 aide à détecter un dérapage : à 50 % du temps, le projet ne devrait pas avoir consommé plus de 50 % du budget sans résultat correspondant."
  "|Toute révision budgétaire doit être justifiée, validée et tracée : on tient un historique des versions du budget."
  "|Le budget intègre aussi les recettes ou les économies attendues, ce qui permet de calculer une marge prévisionnelle."
  "|Pour le technicien CIEL, savoir lire et alimenter un budget est utile dans la gestion d'un parc, d'un projet de migration ou d'un contrat de maintenance."),
[QC("Quelle dépense est un investissement ?", "L'achat d'un serveur durable~Le loyer du bureau~La facture d'électricité~Un abonnement mensuel", 0,
     "Un équipement durable est immobilisé ; les autres exemples sont des charges de fonctionnement."),
 QC("Quelle hypothèse ne pas expliciter dans un budget ?", "Le nombre de postes~Le prix unitaire~Le taux d'inflation~La couleur du logo", 3,
     "Les hypothèses chiffrées doivent être documentées et vérifiables."),
 QC("À quoi sert une réserve pour imprévus ?", "À masquer les erreurs~À absorber les aléas et risques identifiés~À supprimer le contrôle~À augmenter le résultat", 1,
     "La provision pour imprévus sécurise le budget face à l'incertitude."),
 QC("Comment calculer le taux de consommation ?", "Budget prévu divisé par dépenses~Dépenses divisées par budget prévu~Dépenses plus budget~Budget moins dépenses", 1,
     "C'est le rapport entre montant dépensé et montant budgété à la même date."),
 QC("Que révèle une révision budgétaire non tracée ?", "Une bonne pratique~Un manque de rigueur et de contrôle~Une économie~Une certification", 1,
     "L'historique des versions est indispensable à la traçabilité."),
 QC("Quel est un signe de dérapage ?", "Le budget consommé reste en dessous du jalon~Le budget consommé dépasse nettement l'avancement~Aucun écart~Les jalons sont respectés", 1,
     "Une consommation supérieure à l'avancement signale un risque."),
 QC("Quel indicateur complète le suivi des dépenses ?", "Le nombre de réunions~L'avancement des livrables et les jalons~Le nombre de câbles~La taille de l'équipe", 1,
     "Il faut rapprocher coût et avancement réel pour juger la situation."),
 QC("Pourquoi prévoir des recettes ou économies dans le budget ?", "Pour calculer une marge prévisionnelle~Pour éviter de dépenser~Pour supprimer les impôts~Pour remplacer le bilan", 0,
     "La différence entre recettes et coûts donne la marge attendue du projet."),
 QT("Un projet a un budget de 100 000 € sur 10 mois. À mi-parcours, 65 000 € sont dépensés et 40 % des livrables sont terminés. Analyser la situation.",
    "À 5 mois, l'avancement attendu est d'environ 50 %, mais seulement 40 % des livrables sont terminés : le projet a du retard. Le budget consommé atteint 65 % alors que l'avancement réel est de 40 % : le taux de consommation est très supérieur à la progression, ce qui indique un dérapage financier. Selon la règle des 50/50, à 50 % du temps, la consommation ne devrait pas dépasser 50 % sans résultat correspondant. On recherche les causes : prestataire payé d'avance, achat de licences annuelles au démarrage, sous-estimation des heures de développement ou retard pris sur un livrable critique. Le coût à l'achèvement projeté, si la tendance se maintient, dépasse 100 000 €. Des actions sont nécessaires : rééchelonner les paiements, renégocier une prestation, réduire un périmètre non prioritaire et réviser le budget avec l'accord du commanditaire.",
    "On compare temps, avancement et consommation, on mobilise la règle des 50/50, on cherche les causes et on propose des actions."),
 QT("Expliquer la démarche de construction d'un budget prévisionnel pour la maintenance d'un parc de 200 postes.",
    "On définit d'abord le périmètre : nombre de postes, sites, durée de douze mois et niveau de service attendu. On recense les postes de dépense : licences et abonnements, maintenance matérielle, pièces de rechange, prestations externes, formation, outils de supervision et éventuel renouvellement. Pour chaque poste, on précise l'hypothèse : 200 licences à un tarif unitaire, un coût moyen d'intervention multiplié par un nombre estimé de tickets, une provision pour pannes. On ajoute une réserve pour imprévus de 5 à 10 % et on ventile les montants par mois pour obtenir un calendrier de décaissements. On documente les hypothèses, on fait valider le budget, puis on met en place un tableau de suivi mensuel avec budget, réalisé et écart. Enfin, on prévoit une revue trimestrielle pour ajuster les hypothèses.",
    "On attend périmètre, postes de dépense, hypothèses chiffrées, réserve, ventilation mensuelle, validation et suivi.")],
C("Le budget est une prévision chiffrée et un outil de contrôle : on suit à la fois les dépenses et l'avancement réel.",
  "Taux de consommation = dépenses / budget prévu",
  "Investissement vs fonctionnement · réserve pour imprévus · règle des 50/50",
  "Budget~Prévision chiffrée~Investissement~Dépense durable~Fonctionnement~Dépense courante~Réserve~Provision pour aléas~Suivi~Prévu et réalisé",
  "Définir le périmètre|Chiffrer chaque poste|Prévoir une réserve|Suivre consommation et avancement|Réviser en justifiant",
  "Oublier les hypothèses|Supprimer la réserve|Comparer sans tenir compte du calendrier|Modifier le budget sans trace",
  "100 000 €~Budget sur 10 mois~65 000 €~Dépensé à mi-parcours~40 %~Avancement réel~50/50~Règle d'alerte~200 postes~Exemple de parc",
  "Budget prévu~Référence~Réalisé~Montant dépensé",
  "Écart défavorable~Dépense supérieure au prévu~Écart favorable~Dépense inférieure"))

# ============================================================ CG4
add("CG4", "Analyse financière et indicateurs de performance", "Comptabilité et gestion", ["BTS2"],
S("L'analyse financière interprète les états comptables pour évaluer la santé et la performance d'une organisation."
  "|Le fonds de roulement net global se calcule par ressources durables moins emplois durables : il mesure la marge de sécurité financière à long terme."
  "|Le besoin en fonds de roulement correspond aux ressources immobilisées par le cycle d'exploitation : stocks et créances moins dettes d'exploitation."
  "|La trésorerie nette égale fonds de roulement net global moins besoin en fonds de roulement : elle traduit la capacité à payer à court terme."
  "|Une trésorerie négative signale un risque de cessation de paiements, même si l'entreprise est bénéficiaire."
  "|Le résultat d'exploitation mesure la performance de l'activité courante, hors éléments financiers et exceptionnels."
  "|La marge commerciale et la marge sur coûts variables indiquent la capacité de chaque vente à contribuer aux frais fixes et au résultat."
  "|Le taux de marge se calcule en rapportant la marge au chiffre d'affaires : il s'exprime en pourcentage."
  "|Le seuil de rentabilité correspond au chiffre d'affaires pour lequel le résultat est nul."
  "|Les ratios d'endettement et de couverture des intérêts apprécient la capacité de l'entreprise à honorer ses dettes."
  "|L'analyse doit être comparative : dans le temps, par rapport au budget et par rapport aux entreprises du même secteur."
  "|Les limites du bilan doivent être signalées : les valeurs comptables peuvent différer de la valeur de marché, et les actifs immatériels sont parfois sous-estimés."),
[QC("Comment calculer le fonds de roulement net global ?", "Ressources durables moins emplois durables~Créances moins dettes~Produits moins charges~Actif moins passif", 0,
     "Le FRNG est la différence entre ressources durables et emplois durables."),
 QC("Que mesure le besoin en fonds de roulement ?", "Les ressources immobilisées par l'exploitation~Les seules immobilisations~Le résultat~Les capitaux propres", 0,
     "Le BFR traduit l'écart entre décaissements et encaissements d'exploitation."),
 QC("Quelle formule donne la trésorerie nette ?", "FRNG plus BFR~FRNG moins BFR~BFR moins FRNG~Résultat divisé par CA", 1,
     "La trésorerie nette est la différence entre le fonds de roulement et le besoin en fonds de roulement."),
 QC("Une entreprise bénéficiaire peut-elle être en cessation de paiements ?", "Non, jamais~Oui, si sa trésorerie est insuffisante~Oui, mais seulement en cas de perte~Non, si elle a des clients", 1,
     "Le résultat et la trésorerie sont deux dimensions distinctes."),
 QC("Comment calculer un taux de marge ?", "Marge multipliée par chiffre d'affaires~Marge divisée par chiffre d'affaires~Chiffre d'affaires divisé par marge~Marge plus chiffre d'affaires", 1,
     "Le taux de marge rapporte la marge au chiffre d'affaires."),
 QC("Que représente le seuil de rentabilité ?", "Le chiffre d'affaires où le résultat est nul~Le montant des dettes~La trésorerie minimale~Le budget de maintenance", 0,
     "Au seuil, les recettes couvrent exactement tous les coûts."),
 QC("Quel ratio apprécie la capacité à payer les intérêts ?", "La couverture des intérêts~Le taux de marge~Le BFR~Le chiffre d'affaires", 0,
     "La couverture des intérêts rapporte le résultat d'exploitation aux charges financières."),
 QC("Pourquoi comparer les ratios dans le temps ?", "Pour détecter une tendance et une dégradation~Pour remplacer le bilan~Pour supprimer les charges~Pour augmenter le résultat", 0,
     "L'analyse dynamique révèle les évolutions qu'un chiffre isolé ne montre pas."),
 QT("Une entreprise a des ressources durables de 500 000 €, des emplois durables de 380 000 € et un BFR de 160 000 €. Calculer le FRNG et la trésorerie nette, puis interpréter.",
    "Le fonds de roulement net global vaut 500 000 − 380 000 = 120 000 € : les ressources durables financent les emplois durables avec une marge positive de 120 000 €. La trésorerie nette vaut FRNG − BFR = 120 000 − 160 000 = −40 000 €. Elle est négative : le besoin de financement lié au cycle d'exploitation dépasse la marge de sécurité. L'entreprise devra recourir à des concours bancaires à court terme ou réduire son BFR, par exemple en raccourcissant les délais de paiement clients, en diminuant les stocks ou en négociant ses délais fournisseurs. Une trésorerie négative persistante peut conduire à un risque de cessation de paiements malgré un résultat comptable positif.",
    "On calcule 120 000 € puis −40 000 €, et on propose des pistes de réduction du BFR ou de financement."),
 QT("Expliquer pourquoi l'analyse financière doit être comparative et assortie de limites.",
    "Un ratio isolé n'a guère de sens : une marge de 10 % peut être excellente dans un secteur et insuffisante dans un autre. Il faut comparer les indicateurs dans le temps pour repérer une tendance, par rapport au budget pour mesurer l'écart et par rapport à des entreprises comparables pour se situer. Il faut aussi énoncer les limites : le bilan donne des valeurs historiques et comptables, qui peuvent différer de la valeur actuelle ; les immobilisations sont amorties selon des modalités choisies ; les actifs immatériels comme la marque ou le savoir-faire sont souvent sous-estimés ; enfin, les ratios ne disent rien de la qualité de la relation client ou de la sécurité du système d'information. L'analyse financière est donc un éclairage, pas une vérité complète.",
    "On justifie les comparaisons temporelles, budgétaires et sectorielles, puis on cite les limites comptables et qualitatives.")],
C("L'analyse financière relie FRNG, BFR et trésorerie pour juger la santé de l'entreprise et éclairer ses arbitrages d'investissement.",
  "FRNG = ressources durables − emplois durables",
  "Trésorerie = FRNG − BFR · seuil = CA où résultat = 0",
  "FRNG~Marge de sécurité~BFR~Besoin d'exploitation~Trésorerie~Capacité de paiement~Résultat~Performance~Seuil~Point mort~Ratio~Indicateur comparatif",
  "Calculer les agrégats|Interpréter les soldes|Comparer dans le temps et au budget|Repérer les limites|Éclairer la décision",
  "Confondre résultat et trésorerie|Ignorer un BFR croissant|Lire un ratio sans comparaison|Oublier les limites du bilan",
  "500 000 €~Ressources durables~380 000 €~Emplois durables~120 000 €~FRNG~160 000 €~BFR~−40 000 €~Trésorerie nette~Seuil~Résultat nul",
  "FRNG positif~Marge de sécurité~Trésorerie négative~Risque de paiement",
  "Analyse statique~Photo à une date~Analyse dynamique~Suivi dans le temps"))

# FIN DES LOTS
valider_et_ecrire(F, "btsciel-mat-part-C.json")
