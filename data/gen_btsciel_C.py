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
add("PF3", "Expression écrite professionnelle : note, courriel et compte rendu", "Français", ["BTS1"],
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

# FIN DES LOTS
valider_et_ecrire(F, "btsciel-mat-part-C.json")
