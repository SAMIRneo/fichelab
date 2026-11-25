# -*- coding: utf-8 -*-
"""Générateur btsesf-mat-part-C.json — lot C de la filière bts-esf.

20 fiches 'prototype' (BTS1 / BTS2) : Français (4), Anglais professionnel (4),
Communication (4), Informatique (4), Méthodologie (4).
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

# ============================================================ CF1
add("CF1.", "L'argumentation dans une note sociale", "Français", ["BTS1"],
S("Argumenter, c'est défendre une thèse à l'aide de raisons et d'exemples pour convaincre un lecteur."
  "|Une thèse est l'idée principale que l'on soutient ; elle doit être explicite et concise."
  "|Les arguments sont les raisons qui justifient la thèse : faits, chiffres, textes de loi ou témoignages."
  "|Un exemple illustre un argument et le rend concret, par une situation d'accompagnement vécue par la structure."
  "|La note sociale est un écrit professionnel court, structuré, adressé à un responsable ou à un partenaire."
  "|Elle suit généralement un plan en trois parties : situation constatée, analyse, proposition d'action."
  "|Chaque paragraphe peut suivre le modèle thèse, argument, exemple, conclusion intermédiaire."
  "|Les connecteurs logiques comme car, donc, or ou cependant rendent le raisonnement lisible."
  "|Il faut distinguer un fait, une interprétation et une opinion : leur valeur de preuve n'est pas la même."
  "|Les chiffres doivent être sourcés et datés, notamment dans un contexte d'action sociale."
  "|Une argumentation solide anticipe l'objection et y répond sans disqualifier son interlocuteur."
  "|Dans le secteur social, l'argumentation s'appuie sur le respect de la personne et sur des données fiables."),
[QC("Qu'est-ce qu'une thèse ?", "Une objection~L'idée principale défendue~Un exemple chiffré~Une conclusion", 1,
     "La thèse est l'idée centrale que le texte cherche à démontrer."),
 QC("Quel élément constitue un argument ?", "Une raison qui justifie la thèse~Le titre du document~La signature~La date", 0,
     "Un argument apporte une raison d'admettre la thèse."),
 QC("À quoi sert un exemple ?", "À remplacer l'argument~À illustrer un argument~À conclure le texte~À introduire le sujet", 1,
     "L'exemple rend l'argument concret et vérifiable."),
 QC("Quel connecteur marque l'opposition ?", "Car~Donc~Cependant~Ensuite", 2,
     "Cependant introduit une opposition ou une nuance."),
 QC("Qu'est-ce qu'un fait vérifiable ?", "Une opinion personnelle~Une information confirmable par une source~Un sentiment~Une hypothèse", 1,
     "Un fait peut être confirmé par une source ou une donnée observable."),
 QC("Comment traiter une objection dans une note ?", "L'ignorer~Y répondre avec des éléments précis~La ridiculiser~Changer de sujet", 1,
     "Répondre à l'objection renforce la crédibilité de l'argumentation."),
 QC("Que faire d'un chiffre dans une note sociale ?", "Le citer sans source~Le sourcer et le dater~Le modifier pour convaincre~L'omettre", 1,
     "Un chiffre fiable est accompagné de sa source et de sa date."),
 QT("Vous souhaitez demander un renfort de personnel pour votre service d'accompagnement. Présentez le plan d'une note argumentée et indiquez le type de preuves que vous mobiliserez.",
     "La note commence par une brève situation : le service accueille quarante personnes avec deux professionnels le matin, et le taux d'occupation atteint 95 %. La thèse est explicite : un renfort est nécessaire pour maintenir la qualité de l'accompagnement. Le développement comporte deux parties. La première montre les effets de la charge de travail : trois chutes observes le mois dernier, des transmissions réduites à leur plus simple expression et une difficulté à accompagner les repas dans le respect du rythme de chacun. La deuxième présente les solutions envisageables : une embauche, une redistribution des plannings et le recours ponctuel à une équipe mobile, en indiquant le coût et les conditions de chaque option. Les preuves mobilisées sont des données d'activité datees, le registre des incidents, les observations consignees dans les dossiers et le cadre réglementaire qui fixe les conditions d'encadrement. Une objection est anticipe : le cout du renfort. J'y reponds en montrant que la prévention des chutes et la reduction des arrêts de travail compensent une partie de ce cout. La conclusion reprend la demande et propose une réunion de concertation.",
     "On attend une thèse explicite, deux parties, des preuves sourcées et une objection traitée."),
 QT("Dans un compte rendu, distinguez un fait, une interprétation et une opinion, et expliquez pourquoi cette distinction est importante en action sociale.",
     "Un fait est une information observable et vérifiable : Madame X est tombée le 12 janvier à 8 h 30 dans la salle de bain, et le sol était humide. L'interprétation est une lecture du fait : la chute paraît liée à une humidité du sol après la toilette, ou à une fatigue de la personne. L'opinion est un jugement personnel : l'équipe devrait mieux surveiller les déplacements. Cette distinction est essentielle pour trois raisons. D'abord, elle protège la personne : une interprétation présentée comme un fait peut entraîner une décision injuste, comme limiter sa liberté de circulation. Ensuite, elle améliore la qualité des transmissions : le responsable peut vérifier un fait, discuter une interprétation et respecter une opinion sans la confondre avec une preuve. Enfin, elle engage la responsabilité professionnelle : écrire « la personne est tombée parce qu'elle a mal fait son geste » n'a pas la même portée que « la personne est tombée ; nous vérifierons les causes avec elle et l'équipe ». La bonne pratique consiste à noter les faits avec précision, à signaler explicitement les hypothèses par des formulations prudentes, et à réserver les jugements à un espace d'analyse collective.",
     "On attend une définition des trois notions et un lien avec la qualité des transmissions et la protection de la personne.")],
C("Une note sociale convainc par une thèse claire, des arguments vérifiés et des exemples précis.",
  "thèse + arguments + exemples = argumentation",
  "faits vérifiables · connecteurs logiques · objection · conclusion",
  "Thèse~Idée défendue~Doit être explicite|Argument~Raison invoquée~Fait, chiffre ou texte|Exemple~Illustration concrète~Situation réelle",
  "Définir la thèse~Rechercher des arguments fiables~Choisir des exemples~Ordonner les paragraphes~Répondre aux objections",
  "Confondre opinion et fait~Citer un chiffre sans source~Accumuler les exemples sans lien~Ignorer le point de vue adverse",
  "Une thèse~Le renfort est nécessaire~Un argument~Taux d'occupation de 95 %~Un exemple~Trois chutes en janvier~Une objection~Le coût~Une réponse~Une embauche prévient des arrêts",
  "Fait~Vérifiable par une source~Daté~Indépendant de l'observateur|Interprétation~Donne du sens~Dépend du contexte~Peut être discutée",
  "Argument~Justifie la thèse~Appuyé sur des preuves~Général|Exemple~Illustre l'argument~Situé dans le temps~Particulier"))

# ============================================================ CF2
add("CF2.", "La synthèse de documents en action sociale", "Français", ["BTS1"],
S("La synthèse consistait à restituer l'essentiel de plusieurs documents dans un texte neuf et structuré."
  "|Elle demande de comprendre chaque document avant de les comparer et de dégager un plan."
  "|La consigne fixe la longueur, le nombre de documents, le thème et parfois une problématique."
  "|Il faut d'abord lire les documents sans annoter, puis identifier les idées principales de chacun."
  "|Pour chaque document, on relève l'auteur, la date, la nature du texte et le point de vue défendu."
  "|Les idées communes sont regroupées ; les désaccords constituent souvent les axes du plan."
  "|Un plan en deux ou trois parties doit être équilibré, avec des titres explicites et parallèles."
  "|La rédaction utilise des connecteurs et évite la simple juxtaposition des résumés successifs."
  "|On ne doit ni recopier de longues phrases ni introduire des informations absentes des documents."
  "|Les chiffres et les exemples sont conservés lorsqu'ils éclairent le sujet."
  "|La conclusion répond à la problématique et ouvre sur un enjeu professionnel."
  "|En BTS ESF, la synthèse entraîne la capacité à préparer un dossier ou une réunion de partenaires."),
[QC("Quelle est la première étape d'une synthèse ?", "Rédiger directement~Lire les documents pour les comprendre~Choisir la conclusion~Compter les mots", 1,
     "La lecture attentive précède le plan et la rédaction."),
 QC("Que peut fixer la consigne ?", "La couleur du document~La longueur et le nombre de documents~Le nom de l'établissement~L'heure de la réunion", 1,
     "La consigne précise notamment la longueur, le thème et les documents à utiliser."),
 QC("Comment construire les axes du plan ?", "En suivant l'ordre des documents~En regroupant les idées communes et les désaccords~En choisissant au hasard~En copiant les titres", 1,
     "Les convergences et les oppositions entre documents structurent le plan."),
 QC("Que faut-il éviter dans une synthèse ?", "Les connecteurs~La paraphrase de l'ensemble~Les chiffres utiles~Les titres de parties", 1,
     "Il faut reformuler et éviter la simple suite de résumés."),
 QC("Peut-on ajouter une information personnelle ?", "Oui, toujours~Non, sauf si la consigne l'autorise~Oui, pour faire plus long~Uniquement dans la conclusion", 1,
     "La synthèse s'appuie sur les documents fournis."),
 QC("À quoi sert la conclusion ?", "À présenter les documents~À répondre à la problématique~À lister les auteurs~À répéter le plan", 1,
     "La conclusion apporte une réponse et ouvre la réflexion."),
 QC("Quel titre de partie est correct ?", "Introduction~Premièrement~Les limites du dispositif d'accompagnement~Et ensuite", 2,
     "Un titre de partie est explicite et parallèle aux autres titres."),
 QT("Vous devez rédiger une synthèse de trois documents sur l'accès des personnes âgées aux dispositifs d'aide. Décrivez votre méthode de travail, de la lecture à la relecture.",
     "Je commence par lire la consigne et je repère la problématique, la longueur attendue et les documents imposés. Je lis ensuite chaque document une première fois sans annoter, afin d'en saisir le sens global. À la deuxième lecture, je note pour chacun l'auteur, la date, la nature du texte, les deux ou trois idées essentielles et les chiffres importants. Je construis ensuite un tableau de confrontation : les idées partagées apparaissent dans une même colonne, les oppositions dans une autre. Ce travail fait émerger deux axes, par exemple les conditions d'accès au dispositif et les obstacles rencontrés sur le terrain. Je formule des titres explicites et parallèles, puis je rédige au brouillon en reformulant avec mes mots, en reliant les paragraphes par des connecteurs et en citant les données utiles. Je vérifie que je n'ai rien inventé, que chaque document est utilisé et que l'équilibre entre les parties est respecté. La conclusion répond à la problématique et soulève un enjeu professionnel, comme la nécessité d'adapter l'information aux personnes les plus éloignées des dispositifs. Une dernière relecture porte sur la ponctuation, les accents et la longueur.",
     "On attend les étapes de lecture, de confrontation, de planification, de rédaction et de relecture."),
 QT("Pourquoi la synthèse est-elle un exercice utile pour un futur professionnel de l'action sociale ?",
     "La synthèse entraîne trois compétences directement mobilisées dans le métier. La première est la capacité à lire vite et avec précision des textes variés : un rapport d'activité, une circulaire, une note de service ou un article de recherche. La deuxième est l'esprit de synthèse : un professionnel doit pouvoir expliquer en quelques phrases l'essentiel d'un dossier à un responsable, à un partenaire ou à la personne elle-même, sans perdre les informations décisives. La troisième est l'impartialité : confronter des points de vue opposés oblige à repérer les présupposés de chaque auteur et à ne pas confondre son opinion avec les faits. Dans un service social, ces compétences servent à préparer une réunion de concertation, à rédiger une note de synthèse pour une commission ou à transmettre l'essentiel d'un accompagnement lors d'un changement de professionnel. L'exercice apprend aussi à respecter une contrainte de forme et de longueur, ce qui est fréquent dans les documents professionnels. Il ne s'agit donc pas d'un simple exercice scolaire, mais d'un entraînement à la communication écrite dans un contexte où la clarté et la fiabilité de l'information ont des conséquences concrètes pour les usagers.",
     "On attend le lien avec la lecture professionnelle, la transmission et l'impartialité.")],
C("La synthèse transforme plusieurs documents en un texte neuf, structuré et fidèle aux sources.",
  "lecture → confrontation → plan → rédaction → relecture",
  "problématique · axes équilibrés · reformulation · fidélité",
  "Lecture~Comprendre chaque texte~Repérer l'auteur et la date|Confrontation~Regrouper les idées~Identifier les désaccords|Rédaction~Texte neuf et structuré~Connecteurs et relecture",
  "Lire la consigne~Lire les documents~Relever les idées clés~Construire le plan~Rédiger et relire",
  "Recopier des phrases~Inventer des informations~Suivre l'ordre des documents sans plan~Oublier la consigne",
  "Trois documents~Nombre imposé~Deux axes~Plan équilibré~Quelques chiffres~Données utiles~Une problématique~Question directrice~Une relecture~Vérification finale",
  "Idées communes~Convergences~Regroupées en un axe|Idées opposées~Désaccords~Source d'un second axe",
  "Résumé~Reprendre un texte~Rédaction~Produire un texte neuf"))

# ============================================================ CF3
add("CF3.", "Le compte rendu d'entretien et la note d'observation", "Français", ["BTS1"],
S("Le compte rendu d'entretien restitue de façon factuelle ce qui s'est dit lors d'un échange avec une personne."
  "|La note d'observation décrit ce que le professionnel a vu ou constaté, sans interprétation hâtive."
  "|Les deux écrits sont datés, identifiés et versés au dossier de la personne."
  "|Ils distinguent strictement les propos de la personne, les observations directes et les hypothèses."
  "|Une observation utile est précise : heure, lieu, contexte et comportement observable."
  "|Il faut préférer des verbes neutres comme dire, expliquer, refuser ou demander."
  "|Les jugements de valeur comme difficulté, manque de volonté ou agressivité doivent être évités."
  "|Les propos importants peuvent être cités entre guillemets, avec l'accord de la personne."
  "|La note mentionne les actions engagées et les personnes informées de la situation."
  "|Elle indique les suites prévues : réévaluation, transmission à l'équipe ou contact avec un partenaire."
  "|Le respect du secret professionnel impose de limiter la diffusion aux professionnels concernés."
  "|Une bonne note permet de reconstituer une situation et d'évaluer l'évolution d'un accompagnement."),
[QC("Que doit contenir un compte rendu d'entretien ?", "Des jugements personnels~Les propos et les faits constatés~Des suppositions~Des conseils non demandés", 1,
     "Le compte rendu restitue les propos et les faits, pas les jugements."),
 QC("Comment datée une observation ?", "Avec une date et une heure précises~Avec le jour de la semaine seulement~Avec l'année seule~Avec la date du lendemain", 0,
     "Une observation fiable porte une date et une heure."),
 QC("Quel verbe est neutre ?", "Refuser~Manquer de volonté~Être agressif~Se plaindre sans raison", 0,
     "Refuser décrit un comportement observable, contrairement aux jugements."),
 QC("Peut-on citer les propos d'une personne ?", "Oui, toujours et sans limite~Oui, si c'est utile et avec son accord~Non, jamais~Oui, en les modifiant", 1,
     "Une citation fidèle et acceptée renforce la valeur du compte rendu."),
 QC("Qui peut consulter la note ?", "Tous les professionnels de l'établissement~Les seuls professionnels concernés~Le public~Personne", 1,
     "Le secret professionnel limite la diffusion aux personnes concernées."),
 QC("Que doit indiquer la suite donnée ?", "Le nom du responsable hiérarchique seulement~Les actions engagées et les personnes informées~Une opinion sur la famille~Un chiffre arbitraire", 1,
     "La traçabilité porte sur les actions et leurs destinataires."),
 QC("À quoi sert une note d'observation ?", "À occuper le dossier~À reconstituer une situation et suivre son évolution~À sanctionner~À remplacer l'entretien", 1,
     "La note est un outil de suivi et d'évaluation de l'accompagnement."),
 QT("Rédigez une courte note d'observation à la suite d'un repas au cours duquel une personne a refusé de manger, en distinguant faits, propos et hypothèses.",
     "Le 14 mars à 12 h 15, dans la salle à manger, Madame L. est assise à sa place habituelle. Le repas servi comprend une entrée, un plat et un dessert. Madame L. a regardé son assiette sans la toucher pendant environ cinq minutes. Elle a dit textuellement : « Je n'ai pas faim aujourd'hui, laissez-moi tranquille. » L'accompagnant lui a proposé un autre plat et un verre d'eau ; elle a accepté l'eau et a bu quelques gorgées. Elle a ensuite quitté la table sans finir son repas. Aucun changement de comportement alimentaire n'avait été observe les jours précédents. Hypothèses à vérifier : une douleur non exprimée, une inquiétude liée à une visite prévue cet après-midi, ou une préférence alimentaire non renseignée dans le dossier. Actions engagées : l'accompagnant a prévenu l'infirmière de l'établissement, qui passera voir Madame L. dans l'après-midi ; la quantité d'eau bue a été notée sur la feuille de surveillance. Suite prévue : réévaluation du repas du soir et échange avec la famille pour vérifier les préférences alimentaires. La note est versée au dossier et transmise à l'équipe lors de la transmission de 16 h.",
     "On attend des faits datés, des propos cités, des hypothèses explicites et les suites tracées."),
 QT("Expliquez pourquoi il faut éviter les jugements de valeur dans une note professionnelle.",
     "Un jugement devalue comme « la personne est difficile » ou « elle manque de volonté » donne l'apparence d'une explication alors qu'il ne décrit rien d'observable. Il oriente la lecture des collègues et peut conduire à une prise en charge moins attentive, par exemple en considérant qu'un refus est une mauvaise volonté plutôt qu'un symptôme de douleur ou de peur. Il expose aussi la personne à un risque de stigmatisation : un mot écrit au dossier peut accompagner son parcours pendant des mois et influencer des décisions. Enfin, il affaiblit la qualité juridique du dossier : en cas de contestation, un fait précis avec une date et un témoin est utile, alors qu'une appréciation subjective ne l'est pas. La méthode consiste à décrire le comportement observable, à rapporter les propos dans leur forme exacte, à formuler les hypothèses comme telles et à proposer des vérifications. Si une interprétation est nécessaire, elle doit être clairement identifiée et discutée en équipe. Cette exigence ne supprime pas l'analyse professionnelle : elle la rend explicite, partageable et révisable, ce qui sert la qualité de l'accompagnement.",
     "On attend les risques de stigmatisation, d'erreur d'interprétation et de faiblesse juridique.")],
C("Une note professionnelle dissocie les faits, les propos, les hypothèses et les suites données.",
  "faits + propos + hypothèses explicites + suites = note fiable",
  "neutralité · datation · traçabilité · secret professionnel",
  "Faits~Observables et datés~Heure et lieu|Propos~Rapportés fidèlement~Citation si utile|Hypothèses~À vérifier~Jamais présentées comme certaines",
  "Observer sans interpréter~Noter les propos exacts~Dater la situation~Identifier les suites~Transmettre aux personnes concernées",
  "Écrire un jugement de valeur~Oublier l'heure~Confondre hypothèse et fait~Diffuser la note à toute l'équipe",
  "14 mars~Date de la note~12 h 15~Heure du repas~Refus~Comportement observé~Douleur~Hypothèse à vérifier~Infirmière~Personne informée",
  "Fait~Ce qui s'est passé~Vérifiable|Interprétation~Ce que l'on suppose~À confirmer",
  "Note~Texte factuel~Commentaire~Texte interprétatif"))

# ============================================================ CF4
add("CF4.", "Le courrier et le courriel professionnels en structure sociale", "Français", ["BTS2"],
S("Le courrier professionnel est un écrit formel adressé à une personne, une administration ou un partenaire."
  "|Le courriel est plus rapide mais reste un écrit professionnel soumis aux mêmes règles de clarté."
  "|La structure comprend l'en-tête, l'objet, la formule d'appel, le corps, la formule de politesse et la signature."
  "|L'objet doit être précis : il indique le sujet, la personne concernée et la date si nécessaire."
  "|Le corps se compose de trois temps : rappel du contexte, information ou demande, conclusion."
  "|Les phrases courtes et les paragraphes aérés facilitent la lecture."
  "|Le ton est courtois, même lorsqu'il faut signaler un désaccord ou un retard."
  "|Les données personnelles sont limitées au strict nécessaire dans un courriel."
  "|Il faut relire l'orthographe, les accents, les pièces jointes et le destinataire avant l'envoi."
  "|Une pièce jointe doit être nommée clairement et mentionnée dans le corps du message."
  "|La réponse à un courriel conserve l'historique utile, tout en supprimant les informations superflues."
  "|Un courrier bien rédigé facilite la coopération avec les partenaires et sécurise les démarches de l'usager."),
[QC("Quel objet de courriel est le plus efficace ?", "Bonjour~Demande de rendez-vous pour Madame L. - 14 mars~Urgent~Document", 1,
     "Un objet précis indique le sujet et les repères utiles."),
 QC("Quelle est la première partie du corps du message ?", "La signature~Le rappel du contexte~La formule de politesse~La pièce jointe", 1,
     "On rappelle d'abord le contexte avant la demande ou l'information."),
 QC("Comment nommer une pièce jointe ?", "doc1.pdf~Compte-rendu-entretien-14-03.pdf~fichier.pdf~nouveau.pdf", 1,
     "Un nom explicite permet de retrouver le document."),
 QC("Que faut-il vérifier avant l'envoi ?", "La couleur de la police~Le destinataire et les pièces jointes~L'heure d'envoi seulement~Le nombre de mots", 1,
     "Le destinataire et les pièces jointes sont les vérifications essentielles."),
 QC("Quel ton adopter en cas de désaccord ?", "Ironique~Courtois et ferme~Silencieux~Agressif", 1,
     "La courtoisie permet de désaccord sans dégrader la relation."),
 QC("Que faut-il faire des données personnelles ?", "Les multiplier~Les limiter au strict nécessaire~Les joindre systématiquement~Les ignorer", 1,
     "Le principe de minimisation protège la personne."),
 QC("Que contient la signature professionnelle ?", "Le seul prénom~Le nom, la fonction et la structure~Un slogan~La date de naissance", 1,
     "La signature identifie l'expéditeur et son rôle."),
 QT("Rédigez le plan détaillé d'un courriel adressé à une assistante sociale du conseil départemental pour signaler une situation de précarité et demander un rendez-vous.",
     "L'objet précise : Signalement de situation - Madame L. - demande de rendez-vous. La formule d'appel est « Madame, Monsieur, » ou, si le nom est connu, « Madame X, ». Le premier paragraphe rappelle le contexte : Madame L., 62 ans, est accompagnée par notre service depuis trois mois ; son conjoint est décédé en janvier et ses ressources ont diminué. Le deuxième paragraphe expose les faits utiles et datés : loyer impayé de deux mois, difficulté à régler les frais de chauffage, aucune aide familiale disponible, état de santé fragile signalé par le médecin traitant. La demande est formulée clairement : une évaluation de la situation et un rendez-vous dans les quinze jours, avec la personne et une professionnelle de notre service. Le troisième paragraphe propose les pièces disponibles et indique que la personne a donné son accord pour la transmission. La formule de politesse et la signature complètent le message. Avant l'envoi, je vérifie l'adresse du destinataire, l'absence de données superflues, le nom de la pièce jointe et la reliture orthographique. Une copie du courriel est classée dans le dossier de l'usager.",
     "On attend un objet précis, trois temps, une demande claire et les vérifications avant envoi."),
 QT("Pourquoi un courriel professionnel doit-il être relu avant envoi, et que risque-t-on en négligeant cette étape ?",
     "La relecture sert d'abord à vérifier le fond : le destinataire est-il le bon, la demande est-elle claire, les dates et les chiffres sont-ils exacts, les données personnelles sont-elles limitées au nécessaire ? Une erreur de destinataire peut transmettre des informations de santé à une personne non autorisée, ce qui constitue une violation du secret professionnel et du règlement général sur la protection des données. La relecture sert ensuite à vérifier la forme : une faute d'orthographe, un accent oublié ou une phrase ambiguë nuisent à la crédibilité du service et peuvent modifier le sens d'une consigne. Il faut également contrôler les pièces jointes, souvent oubliées, et leur nom. Enfin, la relecture permet d'adapter le ton : un message rédigé à chaud peut paraître agressif alors que l'intention était seulement de signaler un retard. Dans un contexte d'action sociale, l'écrit engage la structure et peut être produit en cas de litige. Quelques minutes de relecture évitent des malentendus, des délais supplémentaires et des risques juridiques pour les personnes accompagnées.",
     "On attend les risques liés au destinataire, aux données, au sens et à l'image de la structure.")],
C("Un écrit professionnel est clair, courtois, sobre en données et vérifié avant envoi.",
  "contexte + information + demande + politesse = courriel efficace",
  "objet précis · pièce jointe nommée · relecture · minimisation des données",
  "Objet~Sujet précis~Repères utiles|Corps~Contexte puis demande~Paragraphes courts|Signature~Identité et fonction~Coordonnées",
  "Choisir l'objet~Rappeler le contexte~Formuler la demande~Nommer la pièce jointe~Relire avant envoi",
  "Envoyer sans relire~Joindre une donnée superflue~Oublier le destinataire~Utiliser un ton ironique",
  "Madame L.~Personne concernée~Deux mois~Retard de loyer~Quinze jours~Délai demandé~Trois pièces~Justificatifs~Une relecture~Vérification finale",
  "Courrier~Formel et signé~Courriel~Rapide mais structuré",
  "Demande~Attendre une réponse~Information~Transmettre sans attendre"))

# ============================================================ AN1
add("AN1.", "Le lexique de l'action sociale et de l'accompagnement", "Anglais professionnel", ["BTS1"],
S("Un lexique professionnel permet de nommer avec précision les publics, les dispositifs et les gestes de l'accompagnement."
  "|Les publics se disent : the elderly, a person with a disability, a child in care, a homeless person."
  "|Les professionnels se nomment : social worker, care assistant, nurse, educator, mediator."
  "|Les besoins courants sont : food, shelter, hygiene, health, safety, company."
  "|Les actions se disent : to support, to accompany, to listen, to assess, to refer, to follow up."
  "|Un dispositif se dit a service ou a centre : a shelter, a care home, a day centre, a support service."
  "|Les valeurs professionnelles se traduisent par : rights, dignity, privacy, consent, equality."
  "|Les difficultés se nomment : poverty, isolation, illness, addiction, exclusion."
  "|A care plan désigne un projet d'accompagnement et a needs assessment une évaluation des besoins."
  "|La prononciation et l'épellation doivent être vérifiées pour éviter les confusions entre mots proches."
  "|Les mots s'apprennent dans des phrases courtes : I support the resident with her meal."
  "|Un lexique classé par situation est plus utile qu'une liste alphabétique pour retrouver le mot en situation."),
[QC("Que signifie « to support » ?", "Accompagner et soutenir~Remplacer~Ignorer~Critiquer", 0,
     "To support signifie soutenir, accompagner une personne."),
 QC("Quel mot désigne un travailleur social ?", "A carer~A social worker~A patient~A resident", 1,
     "A social worker est le travailleur social ; a carer est un aidant."),
 QC("Comment dit-on « les personnes âgées » ?", "The elderly~The young~The children~The workers", 0,
     "The elderly désigne les personnes âgées."),
 QC("Quel mot désigne un hébergement d'urgence ?", "A day centre~A shelter~A hospital~A school", 1,
     "A shelter est un abri, un hébergement d'urgence."),
 QC("Quel terme correspond à « la dignité » ?", "Poverty~Dignity~Illusion~Safety", 1,
     "Dignity signifie dignité, valeur fondamentale de l'accompagnement."),
 QC("Comment dit-on « l'isolement » ?", "Exclusion~Isolation~Addiction~Poverty", 1,
     "Isolation désigne l'isolement ; exclusion signifie exclusion."),
 QC("Quelle phrase est correcte ?", "I assess the needs~I assessing the needs~I am assess the needs~I assessed needs the", 0,
     "Le présent simple « I assess the needs » est correct."),
 QT("Classez douze mots du lexique social en quatre catégories : publics, professionnels, besoins et actions.",
     "Publics : the elderly, a child in care, a homeless person, a resident. Professionnels : a social worker, a care assistant, a nurse, a mediator. Besoins : food, shelter, hygiene, safety. Actions : to support, to listen, to assess, to refer. Cette classification par situation est plus efficace qu'une liste alphabétique, car elle permet de retrouver le mot au moment où l'on en a besoin. Pour chaque mot, on écrit une phrase courte : « I listen to the resident », « She needs shelter », « We refer the case to the social worker ». On ajoute la prononciation des mots difficiles comme hygiene ou mediator, et on révise le lexique avant chaque stage. On l'enrichit avec les mots entendus sur le terrain, en vérifiant toujours le sens avec un professionnel anglophone.",
     "On attend quatre catégories, des mots pertinents et des phrases d'exemple."),
 QT("Expliquez pourquoi la précision du lexique est importante lors d'un accompagnement en anglais.",
     "Un mot imprécis peut modifier le sens d'une consigne et nuire à la personne. Confondre a care assistant et a nurse brouille les responsabilités : l'accompagnant ne réalise pas un acte médical relevant de l'infirmier. Confondre consent et obligation change la nature de la relation : l'accord de la personne doit être libre et éclairé. Une phrase comme « The resident refuses food » doit être comprise exactement, car elle déclenche une évaluation des besoins et une transmission à l'équipe. La précision du lexique facilite aussi les échanges avec les partenaires anglophones et la rédaction des transmissions. Pour l'apprendre, on associe le mot à une situation, à un geste et à une phrase, puis on le réutilise régulièrement en situation plutôt que de le seulement lire. En cas de doute, on demande confirmation plutôt que de deviner : la sécurité et la dignité de la personne priment sur la fluidité de la conversation.",
     "On attend le lien entre mot juste, responsabilités, consentement et qualité de transmission.")],
C("Le lexique social s'apprend par situations et sert à comprendre, transmettre et respecter la personne.",
  "publics + professionnels + besoins + actions = lexique d'accompagnement",
  "dignity · consent · privacy · assessment · care plan",
  "Publics~Personnes accompagnées~The elderly, a resident|Professionnels~Intervenants~Social worker, nurse|Besoins~Attentes essentielles~Food, shelter, safety",
  "Choisir une situation~Lister les mots utiles~Associer image et geste~Écrire une phrase courte~Réviser avant le stage",
  "Apprendre une liste sans contexte~Confondre deux mots proches~Oublier la prononciation~Traduire mot pour mot sans vérifier",
  "To support~Accompagner~Social worker~Travailleur social~Dignity~Dignité~A shelter~Hébergement~Needs assessment~Évaluation des besoins",
  "Carer~Aidant~Nurse~Infirmier~Mediator~Médiateur",
  "Poverty~Pauvreté~Isolation~Isolement"))

# ============================================================ AN2
add("AN2.", "Lire un formulaire et une notice en anglais", "Anglais professionnel", ["BTS1"],
S("Un formulaire social en anglais recueille des informations sur l'identité, la situation et les besoins d'une personne."
  "|Une notice explique une procédure, un mode d'emploi ou les conditions d'un dispositif."
  "|Les champs courants sont : name, date of birth, address, phone number, email."
  "|Les rubriques sur la situation comprennent : family situation, income, housing, health."
  "|« Please tick the appropriate box » demande de cocher la case correspondante."
  "|« Mandatory fields » désigne les champs obligatoires, souvent signalés par un astérisque."
  "|« Date of birth » est la date de naissance ; « date of application » la date de la demande."
  "|Les avertissements utilisent WARNING pour un danger sérieux et CAUTION pour un risque moindre."
  "|« Do not » exprime une interdiction ; « before use » indique une action préalable."
  "|Les unités et les abréviations comme ml, mg, kg ou b.i.d. doivent être lues avec attention."
  "|En cas de doute sur la compréhension d'un champ, on demande confirmation avant de remplir le document."
  "|Les informations personnelles sont traitées avec discrétion et limitées à ce qui est nécessaire."),
[QC("Que signifie « date of birth » ?", "La date de la demande~La date de naissance~La date d'expiration~La date du jour", 1,
     "Date of birth est la date de naissance."),
 QC("Que demande « please tick the appropriate box » ?", "De signer~De cocher la case correspondante~De dater~De joindre une photo", 1,
     "Tick signifie cocher une case."),
 QC("Qu'appelle-t-on « mandatory fields » ?", "Des champs facultatifs~Des champs obligatoires~Des cases grisées~Des signatures", 1,
     "Mandatory signifie obligatoire."),
 QC("Quel avertissement signale un danger sérieux ?", "CAUTION~WARNING~NOTE~TIP", 1,
     "WARNING signale un risque sérieux, plus fort que CAUTION."),
 QC("Que signifie « do not » ?", "Une recommandation~Une interdiction~Une étape~Une date", 1,
     "Do not exprime une interdiction absolue."),
 QC("Quelle information personnelle faut-il limiter ?", "Toutes les informations disponibles~Celles qui sont nécessaires~Le nom seulement~L'adresse seulement", 1,
     "Le principe de minimisation s'applique aussi aux formulaires."),
 QC("Que faire en cas de doute sur un champ ?", "Deviner~Demander confirmation~Laisser vide sans mention~Remplir au hasard", 1,
     "Il faut demander confirmation avant de transmettre une information incertaine."),
 QT("Vous devez aider une personne à remplir un formulaire d'aide en anglais. Décrivez votre méthode et les précautions à prendre.",
     "Je commence par lire le formulaire en entier pour repérer les rubriques, les champs obligatoires signalés par un astérisque et les consignes particulières. Je traduis chaque champ avec la personne, en utilisant des phrases simples et en vérifiant qu'elle comprend ce qui lui est demandé, notamment pour family situation, income et housing. Je remplis les champs avec elle, en respectant l'ordre du document et le format des dates demandé. Pour chaque information, je demande son accord et je me limite aux données nécessaires à l'instruction de la demande. Je relis ensemble les champs remplis, je vérifie la signature et la date, puis je liste les pièces à joindre. Si un terme me semble ambigu, je ne devine pas : je demande confirmation au responsable anglophone ou au service concerné. Je conserve une copie du formulaire dans le dossier et j'explique à la personne les étapes suivantes et les délais de réponse.",
     "On attend lecture globale, traduction avec la personne, minimisation des données et relecture."),
 QT("Pourquoi faut-il distinguer WARNING et CAUTION dans une notice de soin ou d'accompagnement ?",
     "Ces deux termes n'ont pas la même force. WARNING avertit d'un danger sérieux qui peut entraîner une blessure ou une mise en cause de la santé de la personne ; il exige d'arrêter l'action et de vérifier la procédure. CAUTION attire l'attention sur un risque moindre, une précaution à prendre ou une maladresse possible. Les confondre peut conduire à deux erreurs opposées : traiter un risque mineur comme une urgence, ce qui perturbe l'accompagnement, ou banaliser un avertissement grave et poursuivre une action dangereuse. Dans un service d'accompagnement, ces mentions apparaissent par exemple sur le matériel de levage, les produits d'entretien ou les notices de dispositifs médicaux. La bonne pratique consiste à lire tous les avertissements avant l'action, à traduire fidèlement le terme dans la consigne orale et à demander confirmation en cas de doute. La maîtrise de cette nuance contribue directement à la sécurité des personnes et à la responsabilité professionnelle.",
     "On attend la différence de gravité et les conséquences pratiques pour la sécurité.")],
C("Lire un document anglais suppose de repérer les champs, les consignes et le niveau de risque.",
  "champs + consignes + avertissements = lecture fiable",
  "mandatory fields · tick · warning · caution · do not",
  "Identité~Name, date of birth~Données d'état civil|Situation~Income, housing~Éléments du contexte|Consignes~Tick, sign~Actions à réaliser",
  "Lire le document entier~Repérer les champs obligatoires~Traduire avec la personne~Remplir et relire~Demander confirmation si besoin",
  "Deviner le sens d'un champ~Confondre warning et caution~Transmettre une donnée superflue~Oublier la signature",
  "Date of birth~Date de naissance~Mandatory~Obligatoire~Warning~Danger sérieux~Caution~Précaution~Tick~Cocher",
  "WARNING~Danger sérieux~Arrêter et vérifier|CAUTION~Risque moindre~Agir avec précaution",
  "Champ libre~Réponse rédigée~Case à cocher~Choix proposé"))

# ============================================================ AN3
add("AN3.", "Se présenter et présenter sa structure en anglais", "Anglais professionnel", ["BTS2"],
S("Savoir se présenter en anglais permet d'établir un premier contact clair avec un usager ou un partenaire."
  "|La présentation comprend le nom, la fonction, la structure et le rôle auprès de la personne."
  "|« My name is... » et « I work as a... » sont des formules simples et correctes."
  "|« I am in charge of... » indique une responsabilité précise : I am in charge of the daily activities."
  "|Pour décrire une structure, on utilise : a care home, a day centre, a social service, a non-profit organisation."
  "|Les missions se disent : to welcome, to support, to accompany, to advise, to coordinate."
  "|Le public accueilli se présente avec des expressions comme « we welcome elderly people » ou « we work with families »."
  "|Il faut adapter le niveau de langue à son interlocuteur et éviter le jargon."
  "|Les phrases courtes et le regard facilitent la compréhension, surtout avec une personne âgée."
  "|« Nice to meet you » et « How can I help you ? » sont des formules de politesse utiles."
  "|On vérifie la prononciation du nom de la structure et des mots difficiles avant un échange."
  "|Une présentation réussie respecte la dignité de la personne et ne la réduit pas à sa situation."),
[QC("Comment dire « je travaille comme accompagnant » ?", "I work as a care assistant~I am work care assistant~I working as a care assistant~I am care assistant work", 0,
     "La forme correcte est « I work as a care assistant »."),
 QC("Que signifie « I am in charge of... » ?", "Je suis chargé de~Je suis intéressé par~Je suis en retard~Je suis d'accord", 0,
     "In charge of exprime la responsabilité d'une tâche."),
 QC("Comment dire « centre d'accueil de jour » ?", "A day centre~A night school~A care home~A shelter", 0,
     "A day centre désigne un accueil de jour ; a care home est un établissement d'hébergement."),
 QC("Quelle formule de politesse est correcte ?", "Nice to meet you~Nice meet you~Nice to meeting you~Nice to met you", 0,
     "« Nice to meet you » est la formule correcte."),
 QC("Quel verbe décrit une mission d'accompagnement ?", "To support~To ignore~To sell~To refuse", 0,
     "To support signifie accompagner et soutenir."),
 QC("À quoi faut-il adapter sa présentation ?", "À la couleur de la tenue~À l'interlocuteur et à son niveau de langue~À l'heure~Au nombre de collègues", 1,
     "La clarté de l'échange dépend de l'interlocuteur."),
 QC("Quelle attitude respecte la personne ?", "La définir par sa situation~La présenter comme une personne avant tout~Parler d'elle devant elle~Se présenter sans l'écouter", 1,
     "La personne doit être respectée dans sa dignité, pas réduite à son statut."),
 QT("Préparez une courte présentation en anglais de vous-même et de votre structure lors d'un accueil de jour. Indiquez les phrases que vous utiliserez.",
     "Je commence par une formule simple : « Hello, my name is Sophie. I work as a care assistant at Saint-Exupéry day centre. » Je précise mon rôle : « I am in charge of the morning activities and I support residents during meals. » Je présente ensuite la structure en phrases courtes : « Our centre welcomes elderly people from the neighbourhood. We offer activities, meals and support with daily life. Our team includes carers, a nurse and a social worker. » J'ajoute une phrase d'ouverture : « How can I help you today ? » J'évite les termes techniques et je m'exprime calmement, en regardant la personne et en m'adaptant à sa réaction. Si elle ne comprend pas, je reformule avec des mots plus simples plutôt que de répéter la même phrase. J'ai vérifié avant l'accueil la prononciation du nom du centre, du mot elderly et de l'expression care assistant. Cette présentation reste brève : l'objectif est d'établir un contact respectueux, pas de donner un exposé.",
     "On attend nom, fonction, structure, missions, phrases simples et adaptation à la personne."),
 QT("Pourquoi faut-il éviter le jargon et adapter son niveau de langue avec un usager anglophone ?",
     "Le jargon professionnel, même traduit, crée une distance et exclut la personne de la décision qui la concerne. Une expression comme « we implement a person-centred care plan » peut être comprise littéralement ou pas comprise du tout, alors que « we plan the day with you » est accessible. L'adaptation du niveau de langue est une condition de l'accord éclairé : une personne ne peut donner son consentement que si elle a compris ce qui lui est proposé. Elle concerne aussi la dignité : parler lentement avec des phrases courtes n'est pas infantiliser, c'est rendre l'échange possible ; parler fort ou simplifier excessivement jusqu'à la grossièreté serait en revanche irrespectueux. Enfin, l'adaptation protège la qualité des transmissions : les mots employés doivent pouvoir être repris tels quels par la personne et par les collègues. La bonne pratique consiste à utiliser des phrases courtes, à vérifier la compréhension par une reformulation, à éviter les abréviations et à demander à la personne comment elle préfère qu'on s'adresse à elle.",
     "On attend le lien entre compréhension, consentement, dignité et qualité de l'échange.")],
C("Une présentation réussie est courte, claire, adaptée et respectueuse de la personne.",
  "identité + fonction + structure + missions = présentation",
  "phrases courtes · vocabulaire simple · regard · consentement",
  "Identité~Nom et fonction~My name is|Structure~Établissement~A day centre|Missions~Actions proposées~To support",
  "Préparer ses phrases~Vérifier la prononciation~Se présenter~Présenter la structure~Vérifier la compréhension",
  "Utiliser un jargon incompréhensible~Parler trop vite~Réduire la personne à son statut~Oublier d'adapter son ton",
  "My name is~Formule d'identité~I work as~Formule de fonction~Day centre~Structure~To support~Mission~Nice to meet you~Politesse",
  "Formel~Presentation structurée~Informel~Échange spontané",
  "Se présenter~Donner son identité~Présenter la structure~Expliquer son rôle"))

# ============================================================ AN4
add("AN4.", "Écrire un courriel professionnel en anglais", "Anglais professionnel", ["BTS2"],
S("Un courriel professionnel en anglais suit une structure reconnaissable et des règles de politesse."
  "|L'objet, ou subject, doit indiquer clairement le sujet et les repères utiles."
  "|La formule d'appel utilise Dear Madame X ou Dear Sir or Madam si le nom est inconnu."
  "|Le corps du message suit trois temps : contexte, information ou demande, conclusion."
  "|« I am writing to... » introduit la raison du message : I am writing to request a meeting."
  "|« Could you please... ? » formule une demande polie et « Would you mind... ? » une demande plus douce."
  "|« Thank you for your help » et « I look forward to hearing from you » sont des formules de clôture courantes."
  "|La formule finale utilise Kind regards ou Yours sincerely selon le degré de formalisme."
  "|Les phrases courtes et un vocabulaire précis évitent les malentendus."
  "|Les données personnelles sont limitées au nécessaire, comme dans tout écrit professionnel."
  "|Il faut relire l'orthographe, le destinataire, les pièces jointes et leur nom avant l'envoi."
  "|Un courriel clair facilite la coopération avec les partenaires et sécurise les démarches de l'usager."),
[QC("Quel est l'objet d'un courriel en anglais ?", "Le subject~Le signature~Le greeting~Le closing", 0,
     "Subject désigne l'objet du message."),
 QC("Quelle formule introduit la raison du message ?", "I am writing to...~I am going to...~I was thinking...~I would like yesterday", 0,
     "« I am writing to » est la formule professionnelle adaptée."),
 QC("Comment formuler une demande polie ?", "Give me...~Could you please...?~You must...~Do it", 1,
     "« Could you please » est une demande polie."),
 QC("Quelle formule de clôture est correcte ?", "Kind regards~Kind regard~Kindly regards~Kinds regards", 0,
     "« Kind regards » est la formule correcte."),
 QC("Que signifie « I look forward to hearing from you » ?", "J'attends de vos nouvelles~Je vous remercie~Je m'excuse~Je refuse", 0,
     "Cette formule exprime l'attente d'une réponse."),
 QC("Quel élément faut-il vérifier avant l'envoi ?", "La couleur du texte~Le destinataire et les pièces jointes~L'heure~La taille de la police", 1,
     "Le destinataire et les pièces jointes sont essentiels."),
 QC("Que faut-il faire des données personnelles ?", "Les détailler toutes~Les limiter au nécessaire~Les supprimer du dossier~Les envoyer à tous", 1,
     "Le principe de minimisation s'applique au courriel."),
 QT("Rédigez le plan d'un courriel en anglais demandant un rendez-vous à une assistante sociale pour une situation d'hébergement, puis donnez les phrases clés.",
     "L'objet est : Request for appointment - housing situation - Madame L. La formule d'appel est « Dear Madame X, ». Le premier paragraphe rappelle le contexte : « I am writing to ask for an appointment concerning Madame L., who has been supported by our service for three months. » Le deuxième paragraphe expose les faits utiles : « She has been unable to pay her rent for two months and she has no family support nearby. » La demande est claire : « Could you please arrange a meeting within the next two weeks? We can attend with the person concerned. » Le troisième paragraphe mentionne les pièces disponibles et l'accord de la personne : « She has agreed to share the relevant documents. » La clôture est « Thank you for your help. I look forward to hearing from you. » puis « Kind regards » et la signature avec le nom, la fonction et la structure. Avant l'envoi, je vérifie l'adresse, les pièces jointes nommées clairement, l'absence de données superflues et l'orthographe.",
     "On attend un objet précis, trois temps, une demande polie et les vérifications."),
 QT("Quels risques évite la relecture d'un courriel professionnel en anglais ?",
     "La relecture évite d'abord une erreur de destinataire, qui pourrait transmettre des informations de santé ou de situation sociale à une personne non autorisée. Elle permet de vérifier que les dates, les chiffres et les noms sont exacts, car une faute sur une date de rendez-vous ou sur un montant peut retarder une aide. Elle corrige les fautes qui rendent la phrase ambiguë, par exemple l'oubli d'une négation ou d'un accord, et qui peuvent modifier le sens d'une consigne. Elle vérifie enfin les pièces jointes : un document oublié ou mal nommé oblige à un nouvel échange et ralentit la démarche de l'usager. Le ton est également contrôlé : une formulation trop directe peut paraître brutale, alors que les formules de politesse anglaises sont attendues dans un échange professionnel. Dans un service social, l'écrit engage la structure et peut être versé à un dossier. Quelques minutes de relecture protègent la personne, la structure et la qualité de la coopération avec les partenaires.",
     "On attend les risques de diffusion, d'erreur factuelle, d'ambiguïté et d'omission de pièce.")],
C("Un courriel anglais efficace est structuré, poli, sobre en données et relu avant envoi.",
  "subject + appel + trois temps + clôture = courriel professionnel",
  "politeness · clarity · data minimisation · proofreading",
  "Subject~Objet précis~Repères et date|Body~Contexte puis demande~Paragraphes courts|Closing~Remerciement et signature~Kind regards",
  "Choisir l'objet~Rédiger le contexte~Formuler la demande~Nommer la pièce jointe~Relire et envoyer",
  "Oublier le destinataire~Traduire mot pour mot~Joindre une donnée superflue~Négliger la politesse",
  "Subject~Request for appointment~Could you please~Demande polie~Kind regards~Clôture~Two weeks~Délai~Documents~Pièces jointes",
  "Dear Sir or Madam~Nom inconnu~Dear Madame X~Nom connu",
  "Formal~Ton formel~Direct~Ton simple et clair"))

# ============================================================ CM1
add("CM1.", "L'entretien d'aide : écoute et reformulation", "Communication", ["BTS1"],
S("L'entretien d'aide est un temps d'échange centré sur la personne et sur ce qu'elle exprime."
  "|Il ne s'agit ni d'un interrogatoire ni d'un conseil imposé, mais d'un accompagnement de sa parole."
  "|L'écoute active mobilise l'attention, le regard, les gestes et le silence."
  "|La reformulation consiste à redire avec ses propres mots ce que la personne vient d'exprimer."
  "|Elle permet de vérifier la compréhension et de montrer que l'on a entendu."
  "|Les questions ouvertes invitent au développement : Comment vivez-vous cette situation ?"
  "|Les questions fermées appellent une réponse courte et sont utiles pour préciser un fait."
  "|Il faut éviter les questions suggestives qui orientent la réponse de la personne."
  "|Le silence est un outil : il laisse le temps de chercher les mots et de poursuivre."
  "|Les émotions exprimées sont accueillies sans être jugées ni minimisées."
  "|La posture professionnelle respecte la distance, la confidentialité et le rythme de la personne."
  "|L'entretien se clôt en récapitulant les points essentiels et les suites convenues avec elle."),
[QC("Qu'est-ce que la reformulation ?", "Répéter mot pour mot~Redire avec ses mots ce que la personne a exprimé~Corriger la personne~Changer de sujet", 1,
     "La reformulation restitue le sens avec ses propres mots."),
 QC("Quel est un exemple de question ouverte ?", "Avez-vous mal ?~Comment vivez-vous cette situation ?~Est-ce que vous êtes d'accord ?~Oui ou non ?", 1,
     "La question ouverte invite à un développement libre."),
 QC("Quel rôle joue le silence dans l'entretien ?", "Il faut l'éviter~Il laisse le temps à la personne~Il marque le désaccord~Il remplace l'écoute", 1,
     "Le silence respecte le rythme de la parole."),
 QC("Comment accueillir une émotion ?", "La minimiser~L'accueillir sans jugement~La corriger~La discuter avec les collègues", 1,
     "L'émotion est accueillie, pas jugée."),
 QC("Qu'est-ce qu'une question suggestive ?", "Une question neutre~Une question qui oriente la réponse~Une question fermée~Une question de vérification", 1,
     "La question suggestive suggère la réponse attendue."),
 QC("Comment clore un entretien d'aide ?", "En donnant un conseil autoritaire~En récapitulant et en convenant des suites~En quittant brutalement~En jugeant la situation", 1,
     "La clôture récapitule les points essentiels et les suites."),
 QC("Quelle posture est professionnelle ?", "Parler de la personne devant elle~Respecter sa distance et sa confidentialité~Répondre à sa place~Imposer son rythme", 1,
     "La posture respecte la distance, le rythme et la confidentialité."),
 QT("Vous accompagnez une personne qui dit : « Depuis que mon fils est parti, je ne vois plus personne. » Proposez trois reformulations et expliquez leur intérêt.",
     "Première reformulation, centrée sur le ressenti : « Vous ressentez de la solitude depuis le départ de votre fils. » Deuxième reformulation, centrée sur le changement de situation : « Son départ a modifié vos repères quotidiens. » Troisième reformulation, ouverte sur les ressources : « Vous aimeriez peut-être retrouver des contacts, est-ce bien cela ? » Ces reformulations ont trois intérêts. Elles montrent à la personne que son propos a été entendu, ce qui installe la confiance. Elles vérifient l'interprétation : si la personne corrige ma formulation, j'apprends quelque chose de plus juste sur sa situation. Enfin, elles ouvrent la suite de l'échange sans imposer de solution. La troisième formulation reste prudente, car elle propose une piste sous forme de question et laisse la personne libre de la refuser. J'évite absolument les réponses automatiques comme « il reviendra » ou « il faut sortir davantage », qui nient le vécu exprimé. Si la tristesse paraît importante, je le note dans le dossier et j'en parle avec l'équipe, avec l'accord de la personne.",
     "On attend trois reformulations fidèles et l'explication de leur fonction."),
 QT("Expliquez la différence entre écoute active et conseil, et dites quand le conseil peut intervenir.",
     "L'écoute active vise à comprendre le vécu de la personne : on observe, on reformule, on pose des questions ouvertes et on laisse des silences. Elle ne cherche pas à résoudre immédiatement. Le conseil, lui, propose une solution ou une orientation ; il vient d'une expertise professionnelle et peut être utile, mais il risque de court-circuiter l'autonomie de la personne s'il arrive trop tôt. Dans un accompagnement social, le conseil intervient à trois conditions. D'abord, après avoir suffisamment écouté pour comprendre la demande réelle, qui n'est pas toujours celle qui est formulée en premier. Ensuite, avec l'accord de la personne : on peut demander « Souhaitez-vous que je vous propose des pistes ? ». Enfin, en présentant plusieurs options et leurs conséquences, plutôt qu'une solution unique, afin de préserver le choix de la personne. Par exemple, face à une difficulté de loyer, on ne se contente pas de dire « demandez une aide » : on présente les dispositifs possibles, les démarches et les délais, puis on accompagne la décision. L'écoute active reste la base : sans elle, le conseil risque d'être adapté à une situation imaginée plutôt qu'à la situation réelle.",
     "On attend la distinction, les conditions du conseil et le respect de l'autonomie.")],
C("L'entretien d'aide avance par écoute, reformulation et questions ouvertes, sans imposer de solution.",
  "écoute + reformulation + questions ouvertes = entretien d'aide",
  "silence · non-jugement · confidentialité · autonomie",
  "Écoute~Attention et silence~Laisse la parole|Reformulation~Redit le sens~Vérifie la compréhension|Question~Ouverte ou fermée~Fait avancer l'échange",
  "Installer un cadre~Écouter sans interrompre~Reformuler~Poser une question ouverte~Récapituler les suites",
  "Donner un conseil trop tôt~Poser une question suggestive~Remplir le silence par habitude~Juger le vécu exprimé",
  "Une reformulation~Vous ressentez de la solitude~Une question~Comment vivez-vous cela~Un silence~Quelques secondes~Une suite~Un rendez-vous~Un accord~La personne décide",
  "Question ouverte~Laisse le choix~Question fermée~Vérifie un fait",
  "Écoute~Comprendre~Conseil~Proposer une piste"))

# ============================================================ CM2
add("CM2.", "Communiquer avec des publics en situation de vulnérabilité", "Communication", ["BTS1"],
S("La vulnérabilité peut être liée à l'âge, à un handicap, à la maladie, à la précarité ou à l'isolement."
  "|Communiquer avec une personne vulnérable exige d'adapter sa forme sans réduire ses droits."
  "|La première règle est de s'adresser à la personne elle-même, même si un proche est présent."
  "|Il faut se placer à sa hauteur, regarder la personne et utiliser un ton calme."
  "|Les phrases courtes, une seule idée à la fois et des mots concrets facilitent la compréhension."
  "|Il faut vérifier la compréhension par une reformulation, sans faire répéter la personne."
  "|Les consignes sont données dans l'ordre chronologique, avec des repères visuels si besoin."
  "|Une personne atteinte de troubles cognitifs peut avoir besoin de plus de temps pour répondre."
  "|Le refus ou l'agitation expriment souvent une douleur, une peur ou une mauvaise compréhension."
  "|Il ne faut jamais parler de la personne comme si elle n'était pas là."
  "|La communication doit préserver la dignité, l'intimité et le consentement de la personne."
  "|En cas de difficulté persistante, on fait appel à un collègue ou à un outil de communication adapté."),
[QC("À qui faut-il s'adresser en premier ?", "Au proche accompagnant~À la personne elle-même~Au responsable~Au médecin", 1,
     "La personne reste le premier interlocuteur, même accompagnée."),
 QC("Quel ton adopter ?", "Un ton rapide et ferme~Un ton calme et respectueux~Un ton ironique~Un ton très fort", 1,
     "Le calme facilite la compréhension et rassure."),
 QC("Quand faut-il vérifier la compréhension ?", "Jamais~Après avoir expliqué, par une reformulation~Avant de parler~Uniquement à la fin de la journée", 1,
     "La reformulation vérifie le sens sans mettre la personne en difficulté."),
 QC("Que peut exprimer une agitation soudaine ?", "Toujours une mauvaise volonté~Une douleur, une peur ou un incompris~Un caprice~Rien de particulier", 1,
     "L'agitation est souvent un signe de détresse ou d'incompréhension."),
 QC("Que faut-il éviter avec une personne présente ?", "La regarder~Lui parler directement~Parler d'elle comme si elle n'était pas là~Lui laisser du temps", 2,
     "Parler de la personne en sa présence est irrespectueux."),
 QC("Comment donner une consigne complexe ?", "En une seule longue phrase~En étapes ordonnées et courtes~En criant~En écrivant des mots difficiles", 1,
     "Les étapes courtes et ordonnées sont comprises plus facilement."),
 QC("Que faire en cas de difficulté persistante ?", "Abandonner l'échange~Faire appel à un collègue ou à un outil adapté~Insister avec la même phrase~Parler plus fort", 1,
     "Il existe des outils et des collègues ressources."),
 QT("Une résidente atteinte de troubles de la mémoire refuse de se laver en répétant : « Je ne veux pas, laissez-moi. » Comment communiquez-vous avec elle ?",
     "Je m'arrête immédiatement et je ne force pas le geste. Je me place à sa hauteur, je la regarde et je lui parle avec une voix calme : « Madame, vous ne voulez pas continuer maintenant, j'ai bien compris. » Je reformule pour vérifier : « C'est la douche qui vous inquiète ou le moment chosen ? » Je laisse un silence et j'observe sa réaction, son regard et sa posture. Si elle ne répond pas, je propose un choix simple et limité : « Préférez-vous que l'on revienne dans un quart d'heure ou que je vous aide à vous laver les mains seulement ? » J'utilise une seule idée à la fois et des mots concrets. Je vérifie aussi les éléments du contexte : heure, douleur, luminosité, présence d'un autre résident, et je regarde si un changement récent a pu la troubler. Je n'insiste pas si le refus persiste : je note l'épisode de façon factuelle, j'en parle avec l'équipe et je proposerai un autre moment. Le refus est une information sur son état, pas un obstacle à contourner par la force.",
     "On attend arrêt du geste, reformulation, choix simple, recherche de cause et transmission."),
 QT("Montrez en quoi le respect de la dignité et l'adaptation de la communication sont liés.",
     "Adapter sa communication n'est pas une technique de plus : c'est une condition du respect de la dignité. Une personne qui ne comprend pas une consigne et qui est obligée d'obéir perd la maîtrise de ce qui lui arrive ; elle peut vivre l'accompagnement comme une contrainte subie. À l'inverse, des phrases courtes, un regard à sa hauteur, le temps de répondre et une vérification de la compréhension lui permettent de participer à la décision. Le lien est particulièrement visible avec le consentement : une personne ne peut consentir librement à un geste de soin que si elle a compris ce qu'on lui propose et qu'elle peut refuser sans pression. L'adaptation concerne aussi la pudeur : expliquer chaque étape avant de déshabiller une personne, fermer la porte et éviter les commentaires devant les autres sont des gestes de dignité. Enfin, s'adresser à la personne plutôt qu'à son proche affirme qu'elle reste le sujet de son accompagnement. La forme de la communication produit donc des effets concrets sur l'autonomie et le respect de la personne.",
     "On attend le lien avec le consentement, la pudeur et le statut de sujet de la personne.")],
C("Communiquer avec une personne vulnérable, c'est adapter la forme sans jamais réduire la personne.",
  "s'adresser à la personne + adapter + vérifier = communication respectueuse",
  "dignité · consentement · pudeur · temps de réponse",
  "Forme~Phrases courtes et calme~Facilite la compréhension|Vérification~Reformulation~Sans faire répéter|Respect~Dignité et pudeur~Consentement libre",
  "Se placer à hauteur~S'adresser à la personne~Expliquer en étapes~Laisser du temps~Vérifier et transmettre",
  "Parler du proche à la place~Parler de la personne devant elle~Forcer une réponse~Multiplier les consignes",
  "À hauteur~Poste de l'accompagnant~Une idée~Phrase courte~Un quart d'heure~Proposition de délai~Un refus~Information à transmettre~Une équipe~Ressource mobilisée",
  "Refus~Peut exprimer une douleur~Agitation~Peut exprimer une peur",
  "Adapter~Changer la forme~Renoncer~Ne pas accompagner"))

# ============================================================ CM3
add("CM3.", "La médiation et la gestion des conflits en établissement", "Communication", ["BTS2"],
S("Un conflit oppose deux personnes ou deux groupes dont les besoins ou les représentations divergent."
  "|Dans un établissement social, les conflits peuvent opposer usagers, professionnels, familles ou partenaires."
  "|La médiation est une méthode de résolution qui fait intervenir un tiers neutre et indépendant."
  "|Le médiateur n'impose pas de solution : il organise l'échange et aide les parties à trouver une issue."
  "|La première étape est de séparer les personnes et de garantir la sécurité de chacun."
  "|Il faut ensuite écouter chaque partie sans prendre parti ni interrompre."
  "|Les faits sont distingués des ressentis et des interprétations."
  "|Le médiateur reformule les positions et cherche les intérêts sous-jacents."
  "|Un conflit de surface cache souvent un besoin de reconnaissance, d'information ou d'équité."
  "|Les règles de l'échange sont rappelées : parler à son tour, ne pas insulter, rester dans le sujet."
  "|La recherche de solutions propose plusieurs options et aboutit à un accord écrit si nécessaire."
  "|Le suivi de l'accord et la transmission à l'équipe évitent la reprise du conflit."),
[QC("Qui intervient dans la médiation ?", "Le directeur seul~Un tiers neutre et indépendant~La famille~Un autre usager", 1,
     "Le médiateur est un tiers neutre, sans intérêt direct dans le conflit."),
 QC("Quelle est la première priorité ?", "Trouver un coupable~La sécurité et la séparation des personnes~Rédiger un rapport~Informer la presse", 1,
     "La sécurité prime sur toute autre démarche."),
 QC("Que faut-il distinguer ?", "Les faits, les ressentis et les interprétations~Les horaires et les salaires~Les âges et les noms~Les couleurs et les lieux", 0,
     "La distinction permet de sortir de l'accusation mutuelle."),
 QC("Quel est un besoin sous-jacent fréquent ?", "Le besoin de reconnaissance~Le besoin de silence~Le besoin de changement de nom~Le besoin de changer de rythme", 0,
     "La reconnaissance, l'information et l'équité sont des besoins fréquents."),
 QC("Le médiateur doit-il imposer une solution ?", "Oui, toujours~Non, il organise l'échange~Oui, si le directeur le demande~Non, sauf pour les usagers", 1,
     "La médiation vise une solution construite par les parties."),
 QC("Que faire après un accord ?", "Rien~Suivre l'accord et transmettre à l'équipe~Oublier l'incident~Changer de médiateur", 1,
     "Le suivi évite la reprise du conflit."),
 QC("Quelle règle d'échange est utile ?", "Parler en même temps~Parler à son tour sans insulter~Interrompre pour convaincre~Refuser d'écouter", 1,
     "Les règles de parole protègent la qualité de l'échange."),
 QT("Deux résidents se disputent l'usage du salon télévision. Décrivez votre démarche de médiation étape par étape.",
     "Je commence par intervenir calmement pour garantir la sécurité : je sépare les deux personnes, je baisse le ton et je demande aux témoins de s'éloigner. Je vérifie qu'il n'y a pas de blessure et je rassure chacun. Je préviens le responsable de l'étage si l'agitation persiste. Je propose ensuite un échange en deux temps, avec un médiateur qui n'est pas impliqué dans le service. J'écoute chaque résident à son tour, sans prendre parti, en reformulant : « Vous avez l'habitude de regarder ce programme à cette heure et vous vous sentez délogé. » Je sépare les faits, l'heure et le programme, des ressentis, comme le sentiment d'être ignoré. Je cherche les intérêts sous-jacents : l'un a besoin de calme et de continuité, l'autre a besoin de reconnaissance et de compagnie. Je propose alors plusieurs options : un planning d'usage affiché, le prêt d'un casque, une autre pièce pour l'un, ou un programme choisi ensemble deux fois par semaine. Les résidents retiennent le planning et le casque. Je consigne l'accord de façon factuelle, je l'affiche dans le salon et je prévois un point après une semaine pour vérifier qu'il tient. Je transmets l'épisode à l'équipe sans jugement de valeur.",
     "On attend sécurité, écoute séparée, distinction faits/ressentis, options et suivi."),
 QT("Pourquoi vaut-il mieux chercher les intérêts sous-jacents plutôt que de trancher entre les positions ?",
     "Les positions sont ce que les personnes disent vouloir : « je veux la télévision à 18 heures ». Les intérêts sont les raisons plus profondes : le besoin de repères, de compagnie, de calme ou de reconnaissance. Trancher entre les positions revient à désigner un gagnant et un perdant ; le perdant reste frustré et le conflit peut reprendre dès que l'occasion se présente. Chercher les intérêts permet au contraire de trouver des solutions qui satisfont les deux parties, par exemple un planning et un casque plutôt que l'interdiction pour l'un. Cela respecte aussi la dignité des personnes : on ne les traite pas comme des obstacles, mais comme des sujets dont les besoins sont légitimes. Enfin, cette démarche est plus durable, car elle construit une règle de vie collective que les usagers peuvent s'approprier. Elle demande du temps et une neutralité réelle de la part du médiateur. Dans un établissement social, elle contribue aussi à la qualité de vie : un conflit réglé par la recherche d'intérêts communs renforce l'appartenance au groupe plutôt que la rivalité.",
     "On attend la distinction positions/intérêts et les effets sur la durabilité et la dignité.")],
C("La médiation ne cherche pas un coupable : elle organise l'écoute et construit une règle acceptable.",
  "sécurité + écoute + intérêts + accord = médiation",
  "neutralité · faits et ressentis · options · suivi",
  "Sécurité~Séparer et rassurer~Priorité|Écoute~Chaque partie à son tour~Reformulation|Accord~Plusieurs options~Suivi et transmission",
  "Intervenir calmement~Écouter séparément~Distinguer faits et ressentis~Proposer des options~Suivre l'accord",
  "Prendre parti~Rechercher un coupable~Imposer une solution~Oublier le suivi de l'accord",
  "Deux résidents~Parties au conflit~18 heures~Fait~Reconnaissance~Intérêt~Un planning~Option retenue~Une semaine~Délai de suivi",
  "Position~Ce qui est demandé~Intérêt~La raison profonde",
  "Médiation~Solution construite~Arbitrage~Solution imposée"))

# ============================================================ CM4
add("CM4.", "Les transmissions entre professionnels", "Communication", ["BTS2"],
S("Les transmissions sont des échanges d'informations entre professionnels pour assurer la continuité de l'accompagnement."
  "|Elles ont lieu à chaque changement d'équipe, de service ou de professionnel référent."
  "|Une transmission utile est orale, écrite ou les deux, selon les procédures de l'établissement."
  "|Elle porte sur les faits récents, les changements observés, les décisions prises et les suites à venir."
  "|La règle est de distinguer les faits constatés des hypothèses et des interprétations."
  "|Les informations sont classées par ordre d'importance, en commençant par l'essentiel."
  "|Les données de santé et les informations sensibles sont transmises uniquement aux professionnels concernés."
  "|Le secret professionnel s'applique, sauf dans les cas prévus par la loi."
  "|Une transmission orale réussie est courte, structurée et laisse un temps de questions."
  "|La transmission écrite est datée, signée et versée au dossier de la personne."
  "|Il faut signaler ce qui n'a pas été fait et pourquoi, afin d'éviter les malentendus."
  "|Une bonne transmission protège la personne et évite la répétition d'entretiens inutiles."),
[QC("Quand les transmissions sont-elles nécessaires ?", "Une fois par an~À chaque changement d'équipe ou de référent~Uniquement en cas d'urgence~Jamais", 1,
     "La continuité exige une transmission à chaque relais."),
 QC("Que faut-il transmettre en priorité ?", "Les faits récents et les suites à venir~Des rumeurs~Des opinions personnelles~La vie privée du voisin", 0,
     "L'essentiel concerne les faits, les décisions et les suites."),
 QC("Comment distinguer les hypothèses ?", "En les présentant comme des faits~En les signalant explicitement comme telles~En les supprimant~En les écrivant en majuscules", 1,
     "Une hypothèse doit être identifiée comme telle."),
 QC("À qui transmettre une donnée de santé ?", "À toute l'équipe~Aux seuls professionnels concernés~À la famille~À un autre service sans raison", 1,
     "La diffusion est limitée aux professionnels concernés."),
 QC("Quelle est une qualité d'une transmission orale ?", "La longueur~La structuration et un temps de questions~Le jargon~L'absence de dates", 1,
     "Une transmission courte et structurée est plus efficace."),
 QC("Que doit contenir une transmission écrite ?", "Une date et une signature~Une opinion sans date~Un nom seulement~Une phrase sans contexte", 0,
     "La trace écrite est datée et signée."),
 QC("Pourquoi signaler ce qui n'a pas été fait ?", "Pour accuser un collègue~Pour éviter les malentendus sur les suites~Pour remplir le dossier~Pour ne rien dire", 1,
     "L'explication des actions non réalisées sécurise le relais."),
 QT("Préparez le contenu d'une transmission orale de fin de service pour une personne âgée dont l'état a changé dans la journée.",
     "Je commence par l'identité et le contexte : Madame R., 84 ans, accompagnée depuis six mois, présente ce jour une fatigue inhabituelle. Je donne les faits dans l'ordre : ce matin, elle a pris son petit déjeuner normalement ; à 10 h, elle a refusé la marche quotidienne en disant avoir des courbatures ; à 12 h, elle a mangé la moitié de son repas ; à 15 h, l'infirmière a relevé une température de 38,1 °C. Je précise les décisions prises : l'infirmière a prévenu le médecin traitant, une surveillance de la température et des boissons est mise en place, et la sortie de l'après-midi est annulée. Je signale explicitement une hypothèse : le médecin évoque une infection urinaire, sans confirmation à ce stade. Je mentionne ce qui n'a pas été fait : le bilan sanguin demandé n'a pas encore été réalisé, le laboratoire passant demain matin. Je termine par les suites : vérifier la température à 20 h et à 6 h, surveiller les boissons, prévenir le médecin si la température dépasse 38,5 °C. Je laisse un temps de questions à la relève et je demande une confirmation de bonne réception. Une trace écrite reprend les mêmes éléments dans le dossier.",
     "On attend identité, chronologie, décisions, hypothèse signalée, suites et temps de questions."),
 QT("Expliquez le lien entre qualité des transmissions, secret professionnel et protection de la personne.",
     "Une transmission de qualité et le secret professionnel ne s'opposent pas : ils poursuivent le même objectif de protection. Transmettre correctement, c'est donner à la relève les informations nécessaires pour éviter une erreur de soin, une consigne contradictoire ou un entretien répété inutilement. C'est donc protéger la continuité et la sécurité de la personne. Mais transmettre trop, c'est exposer sa vie privée : une information de santé, un conflit familial ou une situation de précarité n'ont pas à être connus de tous les professionnels de l'établissement. Le secret professionnel impose de limiter la diffusion aux personnes qui ont besoin de l'information pour leur mission, et de choisir le canal adapté : oral dans un espace confidentiel, écrit dans un dossier accessible aux seuls autorisés. La personne doit aussi pouvoir savoir qui détient quelles informations et exercer ses droits d'accès et de rectification. La bonne pratique consiste à transmettre le minimum utile, de façon factuelle et datée, en signalant les hypothèses et en traçant les destinataires. C'est à ce prix que la continuité de l'accompagnement reste à la fois efficace et respectueuse.",
     "On attend le lien entre continuité, sécurité, minimisation et droits de la personne.")],
C("Une transmission fiable est factuelle, datée, limitée aux professionnels concernés et orientée vers la suite.",
  "faits + décisions + suites + traçabilité = transmission",
  "secret professionnel · minimisation · continuité · hypothèses signalées",
  "Faits~Chronologie et données~Observables|Décisions~Actions prises~Professionnels informés|Suites~À faire par la relève~Échéances",
  "Identifier la personne~Raconter les faits dans l'ordre~Annoncer les décisions~Signaler les hypothèses~Confirmer la réception",
  "Transmettre une rumeur~Confondre fait et hypothèse~Diffuser à toute l'équipe~Oublier les actions non réalisées",
  "84 ans~Âge de la personne~38,1 °C~Température relevée~Demain matin~Échéance~Médecin~Professionnel informé~Une trace écrite~Trace dans le dossier",
  "Oral~Échange direct~Écrit~Trace durable et datée",
  "Continuité~Éviter la rupture~Secret~Limiter la diffusion"))

# ============================================================ IN1
add("IN1.", "Le système d'information social et la donnée usager", "Informatique", ["BTS1"],
S("Un système d'information social regroupe les outils qui collectent, stockent et restituent les données des usagers."
  "|Il comprend le dossier informatisé, les logiciels métier, les bases de données et les outils de partage."
  "|La donnée usager peut être administrative, sociale, financière ou de santé."
  "|Chaque donnée doit avoir une finalité précise, liée à l'accompagnement de la personne."
  "|La qualité d'une donnée repose sur son exactitude, sa date et sa traçabilité."
  "|Le dossier informatisé retrace les entretiens, les décisions, les prestations et les évaluations."
  "|Les droits d'accès sont attribués selon les missions : chacun ne voit que ce dont il a besoin."
  "|Les modifications sont tracées pour savoir qui a changé une information et quand."
  "|La personne dispose d'un droit d'accès, de rectification et d'effacement de ses données."
  "|Un logiciel métier ne remplace pas le jugement professionnel : il organise l'information."
  "|Les données doivent être mises à jour régulièrement, sinon le suivi devient fiable en apparence seulement."
  "|La maîtrise du système d'information contribue à la continuité et à la sécurité de l'accompagnement."),
[QC("Qu'est-ce qu'un système d'information social ?", "Un logiciel de dessin~Un ensemble d'outils de collecte et de restitution des données~Un réseau social~Une base de données publicitaire", 1,
     "Il regroupe les outils qui gèrent l'information des usagers."),
 QC("Quelle donnée relève du dossier social ?", "Une donnée de santé transmise à tort~Un entretien et son compte rendu~Une information commerciale~Un avis personnel", 1,
     "Le dossier retrace les éléments utiles à l'accompagnement."),
 QC("Quelle qualité est attendue d'une donnée ?", "Elle peut être ancienne~Elle est exacte, datée et tracée~Elle est secrète pour tous~Elle est modifiable par tous", 1,
     "Exactitude, date et traçabilité sont essentielles."),
 QC("Comment attribuer les accès ?", "À tous les salariés~Selon les missions de chacun~Au responsable seulement~À personne", 1,
     "Le principe du besoin d'en connaître limite les accès."),
 QC("Quel droit ne concerne pas la personne ?", "Droit d'accès~Droit de rectification~Droit d'effacement~Droit de modifier le logiciel", 3,
     "La personne ne modifie pas le logiciel, mais exerce des droits sur ses données."),
 QC("Pourquoi tracer les modifications ?", "Pour augmenter le nombre de champs~Pour savoir qui a changé quoi et quand~Pour rendre le logiciel plus rapide~Pour supprimer les anciennes données", 1,
     "La traçabilité est une condition de la fiabilité du dossier."),
 QC("Le logiciel métier remplace-t-il le professionnel ?", "Oui, toujours~Non, il organise l'information~Oui, pour les décisions~Non, sauf le week-end", 1,
     "L'outil aide mais ne décide pas à la place du professionnel."),
 QT("Vous constatez qu'une information importante du dossier d'un usager n'a pas été mise à jour depuis trois mois. Décrivez votre démarche.",
     "Je vérifie d'abord la nature de l'information et sa date de dernière modification dans l'historique du dossier. Je compare avec les éléments connus de l'équipe et avec les documents sources, par exemple un compte rendu de réunion ou une notification de prestation. Je contacte le professionnel référent pour comprendre pourquoi la donnée n'a pas été actualisée, sans supposer une négligence : il peut manquer une pièce ou attendre une décision. Je fais corriger l'information par la personne habilitée, en ajoutant une mention datée qui explique la régularisation, car je ne modifie pas un historique sans trace. Je vérifie ensuite que les autres champs du dossier concernés par la même situation sont cohérents. J'informe la responsable du service si le retard révèle une difficulté dans l'usage de l'outil ou dans les procédures de saisie. Enfin, je propose une vérification périodique des dossiers actifs et une formation courte à la saisie pour l'équipe. L'objectif n'est pas de sanctionner, mais de rendre le dossier fiable, car une donnée ancienne peut conduire à une décision inadaptée pour l'usager.",
     "On attend vérification de l'historique, correction tracée, information du responsable et amélioration de la procédure."),
 QT("Expliquez le lien entre qualité des données et continuité de l'accompagnement.",
     "La continuité suppose que chaque professionnel qui prend le relais dispose d'une image fiable et récente de la situation. Si les données sont incomplètes ou périmées, la relève doit reposer sur des souvenirs ou reposer la même question à la personne, ce qui est fatigant et parfois blessant. Une donnée exacte et datée permet au contraire de reprendre l'accompagnement au bon point, de respecter une décision déjà prise et d'éviter des démarches redondantes. La traçabilité joue un rôle analogue : elle permet de comprendre l'origine d'une information et d'en discuter la pertinence avec l'équipe. La qualité des données protège aussi la personne, car une information erronée sur sa situation peut entraîner un refus de prestation ou une orientation inadaptée. Enfin, elle facilite l'évaluation de l'action sociale : on ne peut mesurer l'évolution d'un accompagnement que si les éléments de départ et les étapes sont correctement renseignés. La saisie n'est donc pas une tâche administrative secondaire, mais une part de la qualité professionnelle.",
     "On attend le lien entre fiabilité, relais, protection de la personne et évaluation.")],
C("Le système d'information social fiabilise le suivi à condition que les données soient exactes, datées et tracées.",
  "collecte + stockage + restitution = système d'information",
  "finalité · exactitude · accès selon les missions · droits de la personne",
  "Données~Administratives et sociales~Finalité précise|Accès~Selon les missions~Besoin d'en connaître|Traçabilité~Qui et quand~Historique des modifications",
  "Identifier la donnée utile~Vérifier sa date~Saisir avec exactitude~Tracer la modification~Restituer à la personne concernée",
  "Saisir une information sans date~Donner tous les accès à tous~Modifier sans historique~Conserver une donnée obsolète",
  "Trois mois~Ancienneté de la donnée~Une correction~Régularisation tracée~Une formation~Action d'amélioration~Un référent~Personne contactée~Un historique~Trace des changements",
  "Dossier papier~Trace physique~Dossier informatisé~Trace structurée",
  "Exactitude~Donnée correcte~Actualité~Donnée récente"))

# ============================================================ IN2
add("IN2.", "Les outils bureautiques pour le suivi des accompagnements", "Informatique", ["BTS1"],
S("Les outils bureautiques aident à organiser, suivre et restituer les informations d'accompagnement."
  "|Le tableur permet de construire des tableaux de suivi, des plannings et des indicateurs."
  "|Une cellule contient une valeur, une formule ou du texte ; les références rendent les calculs réutilisables."
  "|Les formules doivent être vérifiées, car une erreur de référence fausse tous les résultats."
  "|Le traitement de texte sert à rédiger comptes rendus, notes et courriers avec une mise en forme sobre."
  "|Les styles de titre facilitent la navigation et la mise à jour d'un document long."
  "|La présentation assistée construit un support de réunion lisible, avec peu de texte par diapositive."
  "|Les noms de fichiers doivent être explicites et suivre une convention du service."
  "|Les fichiers sont enregistrés dans un espace partagé et structuré, accessible aux seuls autorisés."
  "|Un classeur de suivi contient idéalement une feuille de saisie et une feuille de restitution."
  "|Les données personnelles ne doivent pas être diffusées dans un document de présentation."
  "|Une sauvegarde régulière protège le travail et la continuité du suivi."),
[QC("À quoi sert une référence de cellule dans un tableur ?", "À colorier la cellule~À réutiliser la valeur d'une autre cellule~À fermer le fichier~À imprimer la feuille", 1,
     "La référence permet d'utiliser le contenu d'une cellule dans un calcul."),
 QC("Que faut-il vérifier après une formule ?", "La police du texte~Le résultat et les références~La couleur de fond~Le nombre de pages", 1,
     "Une erreur de référence fausse le résultat."),
 QC("Quel est un bon nom de fichier ?", "doc_final_v2.pdf~Suivi-accompagnement-2026-03.pdf~untitled.pdf~nouveau2.pdf", 1,
     "Un nom explicite indique le contenu et la date."),
 QC("Comment construire une diapositive lisible ?", "Beaucoup de texte~Peu de texte et des titres clairs~Des paragraphes denses~Des phrases longues", 1,
     "La sobriété facilite la lecture pendant une réunion."),
 QC("Où enregistrer un fichier de suivi ?", "Sur le bureau de chacun~Dans un espace partagé et structuré~Dans un courriel personnel~Sur une clé non chiffrée", 1,
     "L'espace partagé structuré garantit l'accès et la traçabilité."),
 QC("Peut-on mettre des données personnelles dans une présentation ?", "Oui, si le public est restreint~Non, sauf nécessité et avec précaution~Oui, toujours~Uniquement le nom", 1,
     "La présentation doit éviter la diffusion inutile de données."),
 QC("À quoi sert une sauvegarde ?", "À rendre le document plus beau~À protéger le travail et le suivi~À augmenter le nombre de feuilles~À supprimer les anciennes versions", 1,
     "La sauvegarde protège la continuité du travail."),
 QT("Vous devez suivre mensuellement les indicateurs d'un service d'accueil. Décrivez l'organisation d'un classeur simple et les vérifications à prévoir.",
     "Le classeur comporte deux feuilles. La première, nommée Saisie, contient une ligne par mois avec les colonnes suivantes : nombre de personnes accueillies, nombre d'entretiens, nombre de demandes satisfaites, délai moyen de réponse et date de saisie. Les données sont saisies une fois par mois à partir des dossiers et du registre d'accueil. La deuxième feuille, nommée Restitution, affiche les totaux et les pourcentages calculés par formules, par exemple le taux de demandes satisfaites rapporté au nombre de demandes. J'utilise des références absolues pour les seuils de référence afin de pouvoir recopier les formules sans erreur. Je vérifie chaque mois que la somme des lignes correspond au registre, que les pourcentages restent entre 0 et 100 et que la date de saisie est renseignée. Je protège les cellules de calcul contre la modification accidentelle. Le classeur est enregistré dans l'espace partagé du service avec un nom explicite incluant l'année. Je n'y inscris aucun nom d'usager : seuls des chiffres agrégés figurent dans le suivi d'activité. Une copie de sécurité est effectuée chaque mois.",
     "On attend deux feuilles, des formules vérifiées, des contrôles et l'absence de données nominatives."),
 QT("Pourquoi la sobriété de la mise en forme est-elle une exigence professionnelle dans les documents sociaux ?",
     "Une mise en forme sobre sert d'abord la lisibilité : un responsable ou un partenaire doit repérer immédiatement l'essentiel d'une note, surtout lorsqu'il consulte plusieurs dossiers. Les titres, les paragraphes courts et les espacements réguliers permettent une lecture rapide sans perte d'information. Ensuite, l'apparence d'un document communicate une image de la structure : des couleurs voyantes, des polices multiples ou des effets inutiles donnent une impression d'amateurisme et détournent l'attention du fond. La sobriété protège aussi la neutralité du propos : dans un contexte social, le document ne doit pas exprimer une opinion par des moyens visuels. Enfin, un document sobre est plus facile à réutiliser, à imprimer et à archiver : il reste lisible en noir et blanc et sur différents supports. Cela ne signifie pas renoncer à toute hiérarchie visuelle : les styles de titre, les listes et les tableaux bien construits rendent le texte plus clair. La règle est simple : chaque élément de mise en forme doit avoir une fonction précise, sinon on le supprime.",
     "On attend lisibilité, image professionnelle, neutralité et réutilisation du document.")],
C("Les outils bureautiques servent le suivi à condition d'être structurés, vérifiés et sobres.",
  "saisie + calcul + restitution = classeur de suivi",
  "références vérifiées · noms explicites · données agrégées · sauvegarde",
  "Saisie~Données mensuelles~Une ligne par période|Calcul~Formules et seuils~Références vérifiées|Restitution~Indicateurs lisibles~Sans données nominatives",
  "Définir les colonnes~Saisir les données~Vérifier les formules~Contrôler les résultats~Enregistrer et sauvegarder",
  "Oublier la date de saisie~Laisser une référence erronée~Mettre des noms d'usagers dans un indicateur~Négliger la sauvegarde",
  "Deux feuilles~Saisie et restitution~Un pourcentage~Indicateur calculé~Chaque mois~Rythme de saisie~Zéro nom~Anonymat~Une sauvegarde~Sécurité",
  "Tableur~Calcul et suivi~Traitement de texte~Rédaction structurée",
  "Sobriété~Lisibilité~Ornement~Distraction"))

# ============================================================ IN3
add("IN3.", "Sécurité informatique et protection des données", "Informatique", ["BTS2"],
S("La sécurité informatique protège la confidentialité, l'intégrité et la disponibilité des données."
  "|La confidentialité interdit l'accès aux personnes non autorisées."
  "|L'intégrité garantit que les données ne sont ni modifiées par erreur ni altérées."
  "|La disponibilité assure que les données sont accessibles quand le service en a besoin."
  "|Un mot de passe est personnel, long et unique ; il ne doit jamais être partagé."
  "|L'authentification à deux facteurs ajoute une protection contre le vol d'identifiants."
  "|Les courriels suspects peuvent contenir des pièces jointes infectées ou des liens frauduleux."
  "|Le chiffrement rend les données illisibles pour une personne qui n'a pas la clé."
  "|Une sauvegarde régulière permet de restaurer les données après une panne ou une attaque."
  "|Le règlement général sur la protection des données impose une base légale et une minimisation des données."
  "|Toute violation de données doit être signalée rapidement selon la procédure de la structure."
  "|Un professionnel de l'action sociale traite les informations avec discrétion, y compris sur les outils numériques."),
[QC("Que protège la confidentialité ?", "La couleur de l'écran~L'accès réservé aux personnes autorisées~La vitesse du logiciel~Le nombre de fichiers", 1,
     "La confidentialité empêche l'accès non autorisé."),
 QC("Qu'est-ce qu'un bon mot de passe ?", "Court et partagé~Long, unique et personnel~Écrit sur un post-it~Identique pour tous les outils", 1,
     "Un mot de passe personnel, long et unique est indispensable."),
 QC("Que faire d'un courriel suspect ?", "Ouvrir la pièce jointe~Signaler sans cliquer sur les liens~Répondre à l'expéditeur~Transférer à tous les collègues", 1,
     "Il faut signaler sans interagir avec le message."),
 QC("Quel est l'effet du chiffrement ?", "Rendre les données plus rapides~Rendre les données illisibles sans clé~Supprimer les sauvegardes~Augmenter les accès", 1,
     "Le chiffrement protège les données au repos et en transit."),
 QC("À quoi sert une sauvegarde ?", "À décorer le bureau~À restaurer les données après un incident~À créer des doublons inutiles~À supprimer les anciennes versions", 1,
     "La sauvegarde est le remède contre la perte de données."),
 QC("Que impose la minimisation des données ?", "Collecter le maximum d'informations~Collecter seulement ce qui est nécessaire~Ne rien collecter~Tout conserver indéfiniment", 1,
     "La minimisation limite la collecte au strict nécessaire."),
 QC("Que faire en cas de violation de données ?", "Attendre la prochaine réunion~Signaler rapidement selon la procédure~Supprimer les traces~En parler sur un réseau social", 1,
     "Le signalement rapide est une obligation."),
 QT("Une collègue a reçu un courriel demandant son mot de passe pour une mise à jour urgente. Que lui répondez-vous et quelles vérifications faites-vous ?",
     "Je lui dis immédiatement de ne pas répondre, de ne pas cliquer sur le lien et de ne pas ouvrir la pièce jointe. Je lui rappelle qu'un service informatique ne demande jamais un mot de passe par courriel et que l'urgence est un motif classique d'escroquerie. Je lui demande de signaler le message au service informatique ou au référent sécurité, en transférant le courriel comme pièce jointe si la procédure le prévoit, sans le diffuser aux collègues. Je vérifie avec elle si elle a saisi des identifiants : si oui, nous changeons le mot de passe depuis un autre appareil et prévenons le référent, car la compilation de l'identifiant doit être traitée comme une violation potentielle. Je contrôle l'adresse de l'expéditeur et l'adresse du lien en survolant sans cliquer, afin de documenter l'incident. Je l'invite à vérifier que son mot de passe est unique et à activer l'authentification à deux facteurs. Enfin, je note l'incident dans le registre prévu par la structure et je propose une courte information à l'équipe sur les courriels frauduleux.",
     "On attend non-interaction, signalement, vérification des identifiants et remédiation."),
 QT("Pourquoi la sécurité informatique est-elle une question d'éthique professionnelle et pas seulement une affaire de technique ?",
     "Les données détenues par un service social concernent des personnes souvent vulnérables : leur santé, leurs ressources, leur situation familiale ou leur hébergement. Une fuite ou une consultation abusive n'est pas une simple panne : elle peut exposer une personne à un risque concret, porter atteinte à sa dignité et détruire la confiance nécessaire à l'accompagnement. L'éthique professionnelle impose donc la discrétion sur les outils numériques comme dans les échanges oraux. Le mot de passe partagé, le fichier envoyé à la mauvaise personne ou l'ordinateur laissé ouvert sont des gestes qui engagent la responsabilité de chacun, même lorsqu'aucun pirate n'est impliqué. La technique fournit des outils, chiffrement, sauvegardes, contrôle des accès, mais leur efficacité dépend de l'usage quotidien. Enfin, la sécurité contribue à l'exigence de minimisation : ne pas collecter ni conserver une donnée inutile, c'est déjà protéger la personne. Un professionnel qui maîtrise ces règles ne protège pas seulement un système : il protège les droits des personnes accompagnées.",
     "On attend le lien entre données sensibles, discrétion, responsabilité et droits des personnes.")],
C("La sécurité informatique protège des personnes avant de protéger des machines.",
  "confidentialité + intégrité + disponibilité = sécurité",
  "mot de passe · chiffrement · sauvegarde · minimisation",
  "Confidentialité~Accès autorisés~Discrétion|Intégrité~Données non altérées~Historique et contrôles|Disponibilité~Accès au bon moment~Sauvegardes",
  "Repérer le risque~Ne pas interagir~Signaler au référent~Changer les identifiants~Documenter l'incident",
  "Partager son mot de passe~Ouvrir une pièce jointe suspecte~Conserver trop de données~Ne rien signaler",
  "Deux facteurs~Protection supplémentaire~Une sauvegarde~Restauration~Une violation~Incident à signaler~Un mot de passe~Secret personnel~Une équipe~Personnes informées",
  "Confidentialité~Secret~Intégrité~Exactitude",
  "Sécurité~Protection active~Négligence~Risque pour la personne"))

# ============================================================ IN4
add("IN4.", "La veille documentaire et les ressources numériques sociales", "Informatique", ["BTS2"],
S("La veille documentaire consiste à rechercher, sélectionner et suivre les informations utiles à sa pratique."
  "|Elle porte sur les textes réglementaires, les dispositifs, la recherche et les bonnes pratiques."
  "|Une recherche efficace commence par des mots-clés précis et des synonymes."
  "|Les opérateurs de recherche permettent de combiner ou d'exclure des termes."
  "|Il faut vérifier la source d'un document : auteur, date, institution et caractère officiel."
  "|Un texte ancien peut encore être en vigueur, tandis qu'un texte récent peut être abrogé."
  "|Les sites officiels sont à privilégier pour les textes de loi et les circulaires."
  "|Les réseaux sociaux relaient vite l'information, mais ne garantissent pas sa fiabilité."
  "|La veille évite de refaire une recherche déjà réalisée par un collègue."
  "|Les références trouvées sont classées dans un outil de gestion documentaire ou un dossier partagé."
  "|Chaque référence utile est accompagnée d'une courte note sur son intérêt pour le service."
  "|Le partage de la veille en équipe contribue à la qualité et à l'actualisation des accompagnements."),
[QC("Quelle est la première étape d'une recherche ?", "Ouvrir un réseau social~Choisir des mots-clés précis~Copier un lien trouvé~Demander à un collègue", 1,
     "Des mots-clés bien choisis conditionnent la pertinence des résultats."),
 QC("Quel critère vérifier sur une source ?", "La couleur de la page~L'auteur, la date et l'institution~Le nombre de mentions~La longueur du texte", 1,
     "L'identité de la source et sa date sont essentielles."),
 QC("Quel site est à privilégier pour un texte de loi ?", "Un forum~Un site officiel~Un blog personnel~Une vidéo", 1,
     "Les sites officiels publient les textes authentiques."),
 QC("Un texte récent est-il forcément en vigueur ?", "Oui, toujours~Non, il peut être abrogé ou modifié~Oui, s'il est sur internet~Non, seulement s'il est ancien", 1,
     "La date ne garantit pas à elle seule la validité d'un texte."),
 QC("Quel est un limite des réseaux sociaux ?", "Ils sont trop lents~Ils ne garantissent pas la fiabilité~Ils interdisent les liens~Ils sont réservés aux juristes", 1,
     "La rapidité de diffusion ne fait pas la fiabilité."),
 QC("Pourquoi classer ses références ?", "Pour occuper un dossier~Pour retrouver et partager l'information~Pour impressionner~Pour augmenter le nombre de fichiers", 1,
     "Le classement permet de réutiliser la veille."),
 QC("Que faut-il ajouter à une référence classée ?", "Une note sur son intérêt pour le service~Un avis personnel sans lien~Une copie de tout le site~Une photographie", 0,
     "Une courte note explique l'utilité du document."),
 QT("Vous devez préparer une veille sur l'évolution des dispositifs d'accompagnement des personnes âgées. Décrivez votre démarche et les critères de sélection des sources.",
     "Je commence par définir le besoin : connaître les dispositifs applicables dans notre département et leurs conditions d'accès. Je choisis des mots-clés comme personnes âgées, maintien à domicile, allocation personnalisée d'autonomie et établissement d'hébergement, puis j'ajoute des synonymes et le nom du département. Je consulte en priorité les sites officiels : légifrance pour les textes, le site du ministère chargé des affaires sociales pour les circulaires, le site du conseil départemental pour les règles locales et un organisme professionnel reconnu pour les bonnes pratiques. Pour chaque document retenu, je note l'auteur, la date de publication, la date d'entrée en vigueur, l'existence d'une version consolidée et un résumé de deux ou trois lignes sur son intérêt pour notre service. Je écarte les contenus sans source identifiable, les articles anciens dont la validité n'est pas confirmée et les rumeurs diffusées sur les réseaux sociaux. Je classe les références dans le dossier partagé du service, avec un titre explicite et la date de consultation. Je prévois une revisite mensuelle des sources officielles et je partage les résultats en réunion d'équipe, en signalant ce qui change pour les usagers.",
     "On attend mots-clés, sources officielles, vérification des dates, classement et partage."),
 QT("Pourquoi la veille documentaire est-elle une responsabilité collective dans un service social ?",
     "Un dispositif social évolue par des textes, des circulaires et des pratiques locales. Si un seul professionnel suit ces changements, l'information reste fragile : en cas d'absence ou de départ, le service peut continuer à appliquer une règle obsolète et orienter les usagers vers des dispositifs fermés ou modifier leurs droits à tort. La veille collective répartit la charge entre les membres de l'équipe et permet de confronter les lectures d'un même texte. Elle évite aussi les recherches redondantes : ce qui a été trouvé par l'un doit être documenté et accessible à tous. Le partage des références contribue à la traçabilité des décisions : lorsqu'une orientation est contestée, on peut montrer sur quel texte elle reposait et à quelle date. Enfin, la veille collective protège la qualité de l'accompagnement, car elle permet d'actualiser les informations données aux personnes et aux partenaires. Elle suppose une organisation simple : un dossier partagé, des noms de fichiers explicites, une date de consultation et un temps régulier de restitution en équipe. C'est une pratique professionnelle au même titre que la tenue du dossier usager.",
     "On attend continuité, partage, traçabilité et actualisation de l'information.")],
C("La veille documentaire transforme une recherche individuelle en connaissance partagée et actualisée.",
  "mots-clés + sources fiables + vérification + classement = veille",
  "source officielle · date de validité · référence commentée · partage",
  "Recherche~Mots-clés et synonymes~Combine et exclut|Source~Auteur et institution~Date et validité|Classement~Référence commentée~Dossier partagé",
  "Définir le besoin~Choisir les mots-clés~Vérifier les sources~Commenter les références~Partager en équipe",
  "Se fier à une rumeur~Oublier la date de consultation~Conserver un texte abrogé~Garder la veille pour soi",
  "Trois mots-clés~Début de recherche~Une circulaire~Source officielle~Un résumé~Note d'intérêt~Chaque mois~Rythme de revisite~L'équipe~Destinataire du partage",
  "Site officiel~Source fiable~Réseau social~Information rapide mais à vérifier",
  "Veille~Recherche active~Hasard~Information subie"))

# ============================================================ MT1
add("MT1.", "La démarche d'accompagnement : évaluation, projet, suivi", "Méthodologie", ["BTS1"],
S("La démarche d'accompagnement organise l'action du professionnel autour de la personne."
  "|Elle se déroule en quatre temps : accueil et écoute, évaluation, construction du projet, suivi et réévaluation."
  "|L'évaluation identifie les besoins, les ressources, les attentes et les freins de la personne."
  "|Elle repose sur des entretiens, des observations et des documents, avec l'accord de l'intéressé."
  "|Le diagnostic ne doit pas réduire la personne à ses difficultés : ses compétences comptent aussi."
  "|Le projet d'accompagnement fixe des objectifs concrets, réalisables et évaluables."
  "|Les objectifs sont formulés avec la personne, pas à sa place, pour préserver son autonomie."
  "|Chaque objectif s'accompagne d'actions, de responsables, de délais et d'indicateurs de suivi."
  "|Le projet est écrit, daté et révisé lors des points de suivi."
  "|Le professionnel référent coordonne les interventions des différents intervenants."
  "|La réévaluation permet d'adapter le projet quand la situation change."
  "|Une démarche bien conduite rend la personne actrice de son parcours et sécurise l'action de l'équipe."),
[QC("Quels sont les temps de la démarche ?", "Accueil, évaluation, projet, suivi~Commande, paiement, facture~Lecture, écriture, oral~Recrutement, formation, sanction", 0,
     "La démarche suit l'accueil, l'évaluation, le projet et le suivi."),
 QC("Que comprend une évaluation sociale ?", "Les seuls revenus~Les besoins, les ressources et les attentes~Le seul âge~Le seul avis du médecin", 1,
     "L'évaluation est globale et associe la personne."),
 QC("Comment formuler un objectif ?", "De façon vague~Concrète, réalisable et évaluable~En termes médicaux uniquement~Sans délai", 1,
     "Un objectif opérationnel est précis et vérifiable."),
 QC("Qui construit le projet ?", "Le seul professionnel~La personne et le professionnel ensemble~Le directeur seul~La famille seule", 1,
     "Le projet est co-construit avec la personne."),
 QC("Que contient un projet écrit ?", "Des opinions~Des actions, des responsables et des délais~Des rumeurs~Des chiffres sans contexte", 1,
     "Le projet opérationnel précise qui fait quoi et quand."),
 QC("À quoi sert la réévaluation ?", "À clore le dossier sans discussion~À adapter le projet si la situation change~À punir la personne~À augmenter le nombre de rendez-vous", 1,
     "Le projet est vivant et suit l'évolution de la situation."),
 QC("Quel est le rôle du référent ?", "Remplacer tous les intervenants~Coordonner les interventions~Décider seul~Ne rien transmettre", 1,
     "Le référent assure la coordination et la cohérence."),
 QT("Une personne en situation de précarité vous est orientée pour un accompagnement. Décrivez les étapes de votre démarche et les précautions à respecter.",
     "Je commence par l'accueil : je me présente, j'explique le cadre de notre intervention, la confidentialité et la possibilité pour la personne de refuser ou d'interrompre l'accompagnement. J'écoute sa demande dans ses mots avant de poser des questions précises. L'évaluation porte sur plusieurs dimensions : situation administrative et ressources, logement, santé, famille, emploi, compétences et projets. Je m'appuie sur l'entretien, sur les documents qu'elle accepte de montrer et sur les observations, en distinguant les faits des hypothèses. Je synthétise cette évaluation avec elle et je lui demande ce qu'elle retient de mes conclusions, car mon regard professionnel ne remplace pas le sien. Nous formulons ensemble deux objectifs concrets : par exemple, constituer un dossier de demande d'aide avant la fin du mois et prendre un rendez-vous avec un service d'insertion. Le projet écrit précise les actions, les responsables, les échéances et les indicateurs de suivi. Je prévois un point à un mois pour réévaluer, avec la possibilité de modifier les objectifs si sa situation a changé. Je transmets les informations utiles aux partenaires concernés, avec son accord et dans le respect du secret professionnel.",
     "On attend les quatre temps, la co-construction, des objectifs opérationnels et le consentement."),
 QT("Expliquez pourquoi un projet d'accompagnement doit être réévalué régulièrement plutôt que considéré comme terminé une fois écrit.",
     "La situation d'une personne n'est pas figée : un emploi peut être trouvé, un état de santé peut évoluer, un proche peut partir ou une prestation peut être accordée. Un projet écrit une fois pour toutes risque alors de proposer des actions devenues inutiles ou inadaptées, et de passer à côté de nouveaux besoins. La réévaluation sert aussi à vérifier si les objectifs initiaux étaient réalistes : un objectif trop ambitieux décourage la personne, tandis qu'un objectif trop modeste ne la fait pas progresser. Elle permet enfin de mesurer l'effet de l'accompagnement et de décider d'une orientation, d'une modification ou d'une clôture. La réévaluation n'est pas un contrôle : c'est un temps d'échange où la personne peut dire ce qui lui convient et ce qui ne lui convient pas. Elle renforce son autonomie, car elle l'associe aux décisions qui la concernent. Pour l'équipe, elle est une source d'apprentissage collectif : comprendre pourquoi un objectif n'a pas été atteint aide à améliorer la pratique. Le projet est donc un outil de pilotage vivant au service de la personne, pas un document administratif figé.",
     "On attend l'évolution de la situation, l'ajustement des objectifs et la participation de la personne.")],
C("La démarche d'accompagnement est un cycle : écouter, évaluer, projeter, suivre et réévaluer avec la personne.",
  "évaluation + projet co-construit + suivi = accompagnement",
  "autonomie · objectifs opérationnels · référent · réévaluation",
  "Évaluation~Besoins et ressources~Avec la personne|Projet~Objectifs et actions~Écrit et daté|Suivi~Points réguliers~Ajustement possible",
  "Accueillir et écouter~Évaluer la situation~Formuler les objectifs~Écrire le projet~Suivre et réévaluer",
  "Décider à la place de la personne~Fixer un objectif vague~Oublier les délais~Ne jamais réévaluer",
  "Quatre temps~Structure de la démarche~Deux objectifs~Exemple opérationnel~Un mois~Délai de suivi~Un référent~Coordination~Un accord~Consentement de la personne",
  "Besoin~Ce qui manque~Ressource~Ce qui aide",
  "Projet~Démarche prospective~Bilan~Regard rétrospectif"))

# ============================================================ MT2
add("MT2.", "L'analyse de la demande et le diagnostic social", "Méthodologie", ["BTS1"],
S("La demande explicite est ce que la personne formule au premier abord."
  "|La demande sous-jacente concerne souvent un besoin plus profond, parfois difficile à exprimer."
  "|Une demande peut être multiple, ambiguë ou contradictoire : il faut la clarifier sans l'imposer."
  "|Le diagnostic social synthétise les informations recueillies pour comprendre une situation."
  "|Il distingue les faits établis, les propos de la personne et les hypothèses professionnelles."
  "|Il examine plusieurs dimensions : sociale, familiale, financière, de santé, de logement et d'accès aux droits."
  "|Les ressources de la personne et de son entourage sont étudiées autant que les difficultés."
  "|Le diagnostic ne doit pas se transformer en jugement moral ou en étiquette."
  "|Il tient compte du contexte institutionnel et des dispositifs réellement accessibles."
  "|Les informations sont recueillies avec l'accord de la personne et limitées au nécessaire."
  "|Le diagnostic est partagé avec elle pour vérifier la justesse de la lecture proposée."
  "|Il débouche sur des pistes d'action discutées, et non sur une décision unilatérale."),
[QC("Qu'est-ce qu'une demande sous-jacente ?", "La demande écrite~Un besoin plus profond que la demande formulée~Une consigne du responsable~Un document administratif", 1,
     "La demande sous-jacente dépasse ce qui est dit spontanément."),
 QC("Comment clarifier une demande ambiguë ?", "En décidant à la place de la personne~En posant des questions ouvertes et en reformulant~En la refusant~En la transmettant sans échange", 1,
     "Le questionnement et la reformulation permettent de préciser."),
 QC("Que contient un diagnostic social ?", "Des faits, des propos et des hypothèses distincts~Des opinions personnelles~Des rumeurs~Des chiffres inventés", 0,
     "La distinction des sources d'information est essentielle."),
 QC("Quelles dimensions sont examinées ?", "Sociale, familiale, financière, santé et logement~Seulement financière~Seulement la santé~Seulement la famille", 0,
     "Le diagnostic est global et multidimensionnel."),
 QC("Que faut-il étudier autant que les difficultés ?", "Les ressources de la personne~Les critiques des collègues~Les prix du marché~Les horaires du service", 0,
     "Les ressources et compétences sont essentielles."),
 QC("Quel risque faut-il éviter ?", "La nuance~Le jugement moral et l'étiquette~La prudence~La vérification", 1,
     "Un diagnostic n'est pas un jugement de valeur."),
 QC("À quoi débouche le diagnostic ?", "À une décision unilatérale~À des pistes d'action discutées avec la personne~À un rapport public~À une sanction", 1,
     "Les pistes sont construites avec la personne."),
 QT("Une personne dit : « J'ai besoin d'aide pour payer mon loyer. » Montrez comment analyser cette demande sans s'arrêter à sa formulation.",
     "Je prends la demande au sérieux, sans la réduire à sa dimension financière. Par des questions ouvertes et des reformulations, je cherche à comprendre la situation : depuis quand les difficultés existent-elles, quelles sont les ressources, y a-t-il eu un événement récent, la personne a-t-elle déjà engagé des démarches, quelles sont ses attentes au-delà du paiement ? La demande sous-jacente peut concerner la peur d'une expulsion, l'isolement, une perte d'emploi ou une difficulté à accéder à ses droits. Je recueille les éléments factuels avec son accord : montant du loyer, montant des ressources, échéances, situation familiale, Charges, existence d'une assurance ou d'une aide familiale. Je distingue ce qu'elle affirme, ce que les documents confirment et ce que je suppose. J'examine aussi ses ressources : compétences administratives, réseau de soutien, motivation à chercher une solution. Je formule ensuite une synthèse courte et je la lui soumets : « Si je comprends bien, la question n'est pas seulement le loyer de ce mois, mais la crainte de ne pas pouvoir le payer les prochains mois. Est-ce exact ? » Nous dégageons ensemble des pistes : demande d'aide au logement, médiation avec le bailleur, accompagnement budgétaire et éventuel recours au CCAS.",
     "On attend distinction demande explicite et sous-jacente, dimensions multiples et synthèse partagée."),
 QT("Pourquoi un diagnostic social doit-il être partagé avec la personne concernée ?",
     "Le partage du diagnostic est d'abord une exigence de respect : la personne est le sujet de sa situation, pas un objet d'étude. Elle peut corriger une information inexacte, apporter un élément que le professionnel ignore et préciser ce qu'elle attend réellement. C'est aussi une condition d'efficacité : un diagnostic construit sans elle risque de proposer des actions qu'elle refusera ou qu'elle ne pourra pas mener. Le partage permet enfin de vérifier l'absence de jugement : une formulation comme « elle ne gère pas son budget » peut être entendue comme une accusation, alors que « les dépenses dépassent les ressources depuis trois mois » décrit une situation. Concrètement, on présente la synthèse avec des phrases simples, on demande ce qui est juste et ce qui ne l'est pas, on note les corrections et on reformule le projet en conséquence. Le diagnostic reste une hypothèse de travail, révisable à mesure que de nouveaux éléments apparaissent. Cette pratique renforce l'alliance professionnelle et la possibilité pour la personne de devenir actrice de son accompagnement.",
     "On attend respect, correction des erreurs, efficacité et évitement du jugement.")],
C("Le diagnostic social est une hypothèse de travail construite avec la personne, jamais une étiquette.",
  "demande explicite + demande sous-jacente + ressources = diagnostic",
  "faits · propos · hypothèses · partage avec la personne",
  "Demande~Ce qui est formulé~Peut être ambiguë|Diagnostic~Synthèse multidimensionnelle~Hypothèse révisable|Pistes~Actions discutées~Avec la personne",
  "Écouter la demande~Clarifier par des questions~Recueillir les faits~Synthétiser sans juger~Partager et réviser",
  "Se limiter à la demande explicite~Confondre hypothèse et fait~Étiqueter la personne~Décider sans elle",
  "Loyer~Demande formulée~Expulsion~Inquiétude sous-jacente~Trois mois~Ancienneté des difficultés~CCAS~Partenaire possible~Une synthèse~Outil de partage",
  "Demande explicite~Ce qui est dit~Demande sous-jacente~Ce qui est cherché",
  "Diagnostic~Compréhension de la situation~Jugement~Évaluation morale"))

# ============================================================ MT3
add("MT3.", "Le travail en équipe pluridisciplinaire", "Méthodologie", ["BTS2"],
S("Une équipe pluridisciplinaire réunit des professionnels de formations et de missions différentes."
  "|Elle peut associer travailleur social, éducateur, infirmier, psychologue, médecin et personnel administratif."
  "|La diversité des regards enrichit la compréhension d'une situation."
  "|Le travail en équipe exige un objectif commun et une répartition claire des responsabilités."
  "|Le professionnel référent assure la cohérence de l'accompagnement et le lien avec la personne."
  "|Les réunions de synthèse permettent de partager les observations et de décider des suites."
  "|Chaque intervenant apporte son regard sans empiéter sur les compétences des autres."
  "|Le secret professionnel est partagé : les informations circulent uniquement entre professionnels concernés."
  "|Les décisions collectives sont tracées, datées et communiquées à la personne si elle est concernée."
  "|Les désaccords sont nécessaires à la qualité de l'analyse, à condition d'être exprimés respectueusement."
  "|La charge de travail et les tensions doivent être abordées pour préserver la qualité de l'accompagnement."
  "|Une équipe qui fonctionne bien protège la personne des contradictions et des oublis."),
[QC("Qu'est-ce qu'une équipe pluridisciplinaire ?", "Une équipe d'un seul métier~Des professionnels de formations et de missions différentes~Une réunion de famille~Un service administratif seul", 1,
     "La pluridisciplinarité associe des regards professionnels variés."),
 QC("Quel est le rôle du référent ?", "Décider seul de tout~Assurer la cohérence et le lien avec la personne~Remplacer les autres métiers~Ne pas transmettre", 1,
     "Le référent coordonne sans se substituer aux autres."),
 QC("À quoi sert une réunion de synthèse ?", "À répartir les tâches commerciales~À partager les observations et décider des suites~À sanctionner~À occuper une salle", 1,
     "La synthèse construit une décision collective et tracée."),
 QC("Comment gérer un désaccord professionnel ?", "L'éviter systématiquement~L'exprimer avec respect et arguments~Imposer son avis par l'ancienneté~En parler à la personne sans précaution", 1,
     "Le désaccord argumenté améliore l'analyse."),
 QC("Que faut-il tracer après une décision collective ?", "Le nom du plus ancien~La décision, sa date et sa communication~Le nombre de participants~La durée de la réunion seulement", 1,
     "La traçabilité porte sur la décision et sa date."),
 QC("Le secret professionnel s'applique-t-il en équipe ?", "Non, plus rien n'est secret~Oui, avec diffusion limitée aux professionnels concernés~Oui, mais seulement au directeur~Non, sauf pour la santé", 1,
     "Le secret reste collectif et la diffusion reste limitée."),
 QC("Quel risque évite une équipe coordonnée ?", "La diversité des regards~Les contradictions et les oublis~La réunion~La transmission", 1,
     "La coordination protège la continuité de l'accompagnement."),
 QT("Lors d'une réunion de synthèse, le psychologue propose une piste que l'éducateur conteste. Comment conduisez-vous l'échange ?",
     "Je rappelle d'abord le cadre : nous parlons de la situation de la personne, avec pour objectif commun la qualité de son accompagnement, et non de la valeur des intervenants. Je donne la parole à chacun sans interrompre et je demande des exemples concrets plutôt que des affirmations générales. Je reformule les deux positions : « Le psychologue observe une souffrance qui nécessite un accompagnement spécialisé ; l'éducateur craint qu'une nouvelle intervention ne disperse la personne et ne fragilise ses repères. » Je distingue les faits observés des hypothèses et je vérifie si les deux lectures sont réellement incompatibles. Je propose ensuite de préciser la question avec la personne elle-même, car son avis est décisif. Nous convenons d'une décision progressive : un entretien exploratoire avec le psychologue, puis un point en équipe avant toute nouvelle orientation. Je fais consigner la décision, sa date, les responsables et le délai de réévaluation. Je communique à la personne, avec tact, ce qui a été décidé et je recueille son accord. Enfin, je vérifie que le désaccord exprimé n'a pas laissé de tension non traitée dans l'équipe.",
     "On attend cadre commun, écoute, reformulation, distinction faits/hypothèses, décision tracée et accord de la personne."),
 QT("Pourquoi la diversité des regards est-elle un atout, et quelles conditions la rendent utile ?",
     "Chaque professionnel observe la même situation depuis sa formation et sa mission : l'infirmier repère un signe clinique, l'éducateur une évolution comportementale, le travailleur social une difficulté d'accès aux droits, l'agent administratif un retard de pièce. La confrontation de ces regards permet d'éviter une lecture unique et de comprendre la complexité de la situation. Mais cette diversité n'est utile que si certaines conditions sont réunies. Il faut d'abord un objectif partagé : sans lui, les interventions se juxtaposent. Il faut ensuite une répartition claire des rôles, pour éviter que deux professionnels fassent le même entretien ou que personne ne suive un point important. Il faut enfin un espace de parole où les désaccords peuvent être exprimés respectueusement et où les décisions sont tracées. Sans ces conditions, la pluridisciplinarité peut produire de la confusion pour la personne, qui entend des discours différents. Bien organisée, elle devient au contraire une garantie de cohérence et de qualité pour l'accompagnement.",
     "On attend la richesse des regards et les conditions : objectif commun, rôles clairs, dialogue et traçabilité.")],
C("L'équipe pluridisciplinaire produit une lecture plus riche à condition d'être coordonnée et respectueuse.",
  "regards divers + objectif commun + décisions tracées = cohérence",
  "référent · synthèse · secret partagé · désaccord argumenté",
  "Regards~Formations et missions variées~Richesse de l'analyse|Coordination~Référent et synthèse~Évite les contradictions|Traçabilité~Décisions datées~Communication à la personne",
  "Rappeler l'objectif commun~Écouter chaque intervenant~Distinguer faits et hypothèses~Construire une décision~Tracer et communiquer",
  "Imposer son avis par ancienneté~Empiéter sur les compétences des autres~Diffuser une information à tort~Laisser un désaccord non traité",
  "Trois métiers~Diversité des regards~Une synthèse~Décision collective~Un délai~Réévaluation prévue~Une personne~Centre de l'échange~Une trace~Décision datée",
  "Pluridisciplinaire~Plusieurs métiers~Uniprofessionnel~Un seul métier",
  "Désaccord~Argument utile~Conflit~Tension non traitée"))

# ============================================================ MT4
add("MT4.", "L'évaluation de l'action sociale et l'amélioration continue", "Méthodologie", ["BTS2"],
S("Évaluer une action sociale consiste à mesurer ses effets au regard des objectifs fixés."
  "|L'évaluation ne se limite pas à un contrôle : elle sert à apprendre et à améliorer."
  "|On distingue l'évaluation de processus, qui examine la façon dont l'action est menée, et l'évaluation de résultats."
  "|Les indicateurs sont des mesures simples : nombre d'accompagnements, délai de réponse, taux de satisfaction."
  "|Un indicateur pertinent est lié à un objectif, fiable, régulier et exploitable."
  "|Trop d'indicateurs dispersent l'attention et produisent des données inutiles."
  "|Les données proviennent des dossiers, des registres, des enquêtes et des échanges avec les usagers."
  "|La parole des usagers est une source essentielle, aux côtés des chiffres et de l'avis des professionnels."
  "|Les résultats sont analysés en équipe, en cherchant les causes plutôt qu'un responsable."
  "|La démarche d'amélioration suit un cycle : planifier, réaliser, vérifier, agir."
  "|Chaque action correctrice comporte un responsable, une échéance et un moyen de vérifier son effet."
  "|L'évaluation renforce la qualité de l'accompagnement et la transparence envers les partenaires et les usagers."),
[QC("À quoi sert une évaluation ?", "À sanctionner~À mesurer les effets et à améliorer l'action~À remplir un dossier~À supprimer des postes", 1,
     "L'évaluation est un outil d'apprentissage et d'amélioration."),
 QC("Qu'est-ce qu'un indicateur pertinent ?", "Un chiffre choisi au hasard~Une mesure liée à un objectif et exploitable~Le plus grand nombre possible~Une opinion isolée", 1,
     "Un bon indicateur est utile à la décision."),
 QC("Quelle source ne doit pas être négligée ?", "La parole des usagers~La couleur des locaux~Le nombre de réunions~Le prix du mobilier", 0,
     "Le point de vue des usagers complète les données chiffrées."),
 QC("Quel cycle structure l'amélioration continue ?", "Voir, dire, faire~Planifier, réaliser, vérifier, agir~Acheter, vendre, facturer~Écrire, signer, classer", 1,
     "Le cycle PLAN, DO, CHECK, ACT est la référence."),
 QC("Comment analyser un écart ?", "En cherchant un coupable~En recherchant les causes avec l'équipe~En l'ignorant~En changeant de logiciel", 1,
     "La recherche de causes est collective et non punitive."),
 QC("Que doit comporter une action correctrice ?", "Un responsable et une échéance~Une seule phrase~Une réunion sans suite~Un chiffre isolé", 0,
     "Une action correctrice est responsabilisée et datée."),
 QC("Quel risque présente une multiplication des indicateurs ?", "Une meilleure lisibilité~Une dispersion de l'attention~Une évaluation plus juste~Plus de transparence", 1,
     "Trop d'indicateurs rendent le suivi illisible."),
 QT("Un service constate une hausse du nombre de réclamations d'usagers. Décrivez la démarche d'évaluation et d'amélioration que vous proposez.",
     "Je commence par préciser le constat : nombre de réclamations par mois, motifs, services concernés et période. Je vérifie la fiabilité des données : une hausse peut venir d'un nouveau mode de collecte plutôt que d'une dégradation réelle. J'analyse ensuite les causes avec l'équipe, sans rechercher de responsable : délai d'attente, information insuffisante, difficulté à joindre un professionnel, changement de procédure ou charge de travail. Je croise les chiffres avec la parole des usagers, par exemple par des entretiens courts ou une boîte à suggestions, et avec le regard des professionnels. Je formule une hypothèse prioritaire, par exemple le manque d'information sur les délais, et je définis une action correctrice : afficher les délais dans l'accueil, prévoir un appel de confirmation et former l'équipe à une phrase d'explication commune. Je désigne un responsable, une échéance d'un mois et un indicateur de vérification, comme le nombre de réclamations liées aux délais. Après un mois, je compare les résultats, j'observe ce qui a fonctionné et j'ajuste l'action si nécessaire. Je restitue les résultats à l'équipe et aux usagers pour montrer que leurs remarques ont été prises en compte.",
     "On attend vérification des données, recherche de causes, action responsabilisée et cycle de vérification."),
 QT("Pourquoi associer les usagers à l'évaluation d'un service social ?",
     "Les chiffres décrivent l'activité, mais pas toujours l'expérience vécue. Un service peut respecter ses délais tout en laissant les personnes dans l'incompréhension ou l'inconfort. La parole des usagers révèle ce que les indicateurs ne mesurent pas : la qualité de l'écoute, le sentiment d'être respecté, la clarté des informations, la possibilité de refuser. Elle permet aussi de détecter des effets inattendus d'une procédure pensée pourtant avec de bonnes intentions. Associer les usagers renforce leur statut de sujet de l'accompagnement et la transparence du service. Cela suppose des modalités adaptées : entretiens individuels, questionnaires courts, groupes de parole, avec une information claire sur l'usage des réponses et la possibilité de ne pas participer. Il faut ensuite rendre des comptes : une collecte sans restitution génère de la frustration et discrédite la démarche. Enfin, les retours d'usagers doivent être confrontés aux autres sources, sans être traités comme des plaintes à écarter ni comme des vérités uniques. Leur contribution rend l'évaluation plus complète et l'amélioration plus pertinente.",
     "On attend apport de l'expérience vécue, statut de sujet, modalités adaptées et restitution.")],
C("L'évaluation est un cycle d'apprentissage collectif qui associe chiffres, professionnels et usagers.",
  "planifier + réaliser + vérifier + agir = amélioration continue",
  "indicateurs utiles · parole des usagers · causes systémiques · actions tracées",
  "Mesure~Indicateurs liés aux objectifs~Données fiables|Analyse~Causes et points de vue~Sans recherche de faute|Action~Correctrice et datée~Responsable et vérification",
  "Choisir peu d'indicateurs~Collecter les données~Écouter les usagers~Rechercher les causes~Décider et vérifier l'effet",
  "Multiplier les indicateurs~Chercher un coupable~Ignorer la parole des usagers~Ne pas restituer les résultats",
  "Un mois~Période d'observation~Une hausse~Signal à vérifier~Un responsable~Pilote de l'action~Un indicateur~Mesure de l'effet~Une restitution~Retour à l'équipe",
  "Processus~Comment l'action est menée~Résultat~Ce que l'action produit",
  "Contrôle~Vérifier la conformité~Apprentissage~Comprendre et améliorer"))

valider_et_ecrire(F, "btsesf-mat-part-C.json")
