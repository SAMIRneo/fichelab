# -*- coding: utf-8 -*-
"""Generateur pro-sante-mat-part-C.json — lot C : pratique et environnement (20 fiches).

Pratique professionnelle (8), Economie et gestion (4), Langues (4),
Developpement durable (4). Chaque fiche : 12 points, 9 questions
corrigees (7 QCM + 2 texte), 7 blocs en ordre strict, 3 schemas via diag().
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pro_sante_common import S, R, QC, QT, C, build, valider_et_ecrire

F = []


def add(prefix, titre, mat, ans, points, qcm, txt, c):
    F.append(build(prefix, titre, mat, ans, points, qcm + txt, c))


# ============================================================ PP1
add("PP1", "La posture professionnelle et le savoir-être", "Pratique professionnelle", ["2nde pro"],
S("La posture professionnelle designe la maniere dont un professionnel se comporte dans l'exercice de son role."
  "|Elle associe des savoirs techniques, des savoir-faire et des savoir-etre."
  "|Le savoir-etre comprend le respect, la disponibilite, la patience, la discretion et la rigueur."
  "|Adopter une posture professionnelle, c'est adapter son comportement a la personne et a la situation."
  "|La bienveillance ne suffit pas : elle doit s'appuyer sur les droits et les regles de la profession."
  "|Une attitude respectueuse se manifeste dans le regard, le ton de la voix, la distance et les gestes."
  "|On parle de la personne, pas a son sujet devant elle, et on l'associe aux decisions qui la concernent."
  "|Les limites de competences sont essentielles : on ne remplace ni le medecin ni l'infirmier."
  "|La ponctualite, la tenue vestimentaire adaptee et le respect des procedures font partie de la posture."
  "|Une attitude reflexive permet de questionner ses gestes et de progresser grace au retour de l'equipe."
  "|La fatigue et les emotions personnelles doivent etre reconnues et gerees, sans les reporter sur la personne."
  "|En stage, la posture professionnelle est evaluee autant que la realisation des gestes techniques."),
[QC("Que désigne la posture professionnelle ?", "Une tenue vestimentaire seulement~La manière de se comporter dans son rôle~Un geste technique~Une règle administrative", 1,
     "La posture professionnelle englobe l'ensemble des comportements adoptees dans le travail."),
 QC("Quel élément relève du savoir-être ?", "Une manipulation correcte~La patience et le respect~Une formule de calcul~Un protocole écrit", 1,
     "Le savoir-etre concerne les attitudes et les qualites relationnelles."),
 QC("La bienveillance suffit-elle à garantir une bonne posture ?", "Oui, toujours~Non, elle doit s'appuyer sur les droits et les règles~Oui, si elle est sincère~Uniquement en famille", 1,
     "Une intention gentille ne garantit pas le respect des regles et des droits."),
 QC("Quel geste est respectueux de la personne ?", "Parler d'elle devant elle~L'associer aux décisions qui la concernent~Décider sans l'informer~Presser le soin", 1,
     "Associer la personne est une marque de respect de son autonomie."),
 QC("Que sont les limites de compétences ?", "Des horaires~Le cadre de ce que l'on peut faire et dire~Des interdits de parole~Une simple formalité", 1,
     "Chaque professionnel agit dans un cadre precis qu'il ne doit pas depasser."),
 QC("Qu'est-ce qu'une attitude réflexive ?", "Répéter sans changer~Questionner sa propre pratique~Refuser les conseils~Travailler isolément", 1,
     "La reflexivite est la capacite a prendre du recul sur ses actes."),
 QC("Comment gérer une fatigue personnelle pendant un soin ?", "La cacher totalement~La reconnaître et demander du soutien sans la reporter sur la personne~L'ignorer~S'énerver", 1,
     "La reconnaissance de la fatigue permet de proteger la qualite de l'accompagnement.")],
[QT("Expliquer la différence entre savoir, savoir-faire et savoir-être dans le métier d'accompagnant.",
     "Le savoir correspond aux connaissances : anatomie, physiologie, droit, reglementation. Le savoir-faire correspond aux gestes et aux procedures : realiser une toilette, installer une personne, transmettre une information. Le savoir-etre correspond aux attitudes : respect, ecoute, patience, discretion, ponctualite. Une bonne prise en charge mobilise les trois dimensions en meme temps : un geste techniquement correct mais realise sans explication ni respect blesse la personne, tandis qu'une attitude bienveillante sans competence technique ne garantit pas sa securite. La formation ASSP developpe ces trois dimensions, et l'evaluation en milieu professionnelle porte sur leur articulation.",
     "On attend une definition des trois dimensions et un exemple montrant leur complementarite."),
 QT("Comment adapter sa posture face à une personne qui vous répond brutalement ?",
     "On ne répond pas sur le meme ton et on ne prend pas la remarque personnellement. On s'arrete un instant, on garde une distance calme et on cherche a comprendre : la brutalite peut exprimer une douleur, une peur, une fatigue ou une mauvaise comprehension du soin propose. On reformule ce que l'on a dit et on demande a la personne ce qui la gene, en utilisant des phrases courtes. On continue le geste seulement si elle y consent, sinon on s'ecarte et on revient plus tard. On ne la juge pas et on n'en parle pas avec les autres residents. On transmet l'episode a l'equipe de maniere factuelle pour rechercher une cause, notamment une douleur ou un changement d'etat. La posture professionnelle consiste a garder la maitrise de soi tout en restant attentif a la personne.",
     "On attend maitrise de soi, recherche de cause, reformulation, respect du refus et transmission factuelle.")],
C("La posture professionnelle articule compétences techniques, respect des droits et qualités humaines.",
  "savoir + savoir-faire + savoir-être = posture professionnelle",
  "respect · discrétion · rigueur · limites de compétences · réflexivité",
  "Posture~Manifeste professionnelle~Savoir~Connaissances~Savoir-faire~Gestes et procédures~Savoir-être~Attitudes et respect~Limites~Cadre de compétences",
  "Préparer le soin~Expliquer à la personne~Adapter son comportement~Respecter ses limites~Demander un retour à l'équipe",
  "Confondre bienveillance et respect des droits|Parler de la personne devant elle|Dépasser ses compétences|Réagir sur le même ton",
  "Respect~Attitude quotidienne~Discrétion~Secret et retenue~Ponctualité~Fiabilité~Réflexivité~Recul sur ses actes~Fatigue~À gérer",
  "Savoir~Ce que l'on connaît~Savoir-faire~Ce que l'on sait faire~Savoir-être~La façon d'être avec l'autre",
  "Bienveillance~Intention~Droits~Cadre opposable"))

# ============================================================ PP2
add("PP2", "L'accueil et la communication avec la personne", "Pratique professionnelle", ["2nde pro"],
S("L'accueil est le premier moment de la relation : il donne le ton de toute l'accompagnement."
  "|Il comprend une présentation, un sourire, une posture ouverte et une écoute attentive."
  "|La communication verbale utilise des phrases courtes, claires et adaptées au niveau de compréhension."
  "|La communication non verbale passe par le regard, les gestes, la distance et le ton de la voix."
  "|Se placer à la hauteur de la personne facilite l'échange et réduit le sentiment de domination."
  "|Une consigne donnée en même temps qu'un bruit ou une télévision risque de ne pas être entendue."
  "|La reformulation permet de vérifier que l'on a bien compris le besoin exprimé."
  "|Les questions ouvertes invitent la personne à préciser ; les questions fermées appellent un oui ou un non."
  "|Face à une personne qui ne parle pas, on peut utiliser des images, des gestes ou des objets."
  "|Les troubles cognitifs ou sensoriels imposent de ralentir et de vérifier la compréhension."
  "|Une mauvaise nouvelle ou un refus s'annonce avec des mots simples et un temps de silence."
  "|La qualité de l'accueil est évaluée par le ressenti de la personne et par la clarté des transmissions."),
[QC("Quel élément fait partie de la communication non verbale ?", "Une phrase courte~Le regard et la distance~Une consigne écrite~Un horaire", 1,
     "Le regard, les gestes et la distance sont des canaux non verbaux."),
 QC("Pourquoi se placer à la hauteur de la personne ?", "Pour faire plus grand~Pour faciliter l'échange et réduire la distance symbolique~Pour gagner du temps~Pour éviter de parler", 1,
     "La hauteur et la posture influencent la qualité de la relation."),
 QC("Qu'est-ce qu'une question ouverte ?", "Une question qui appelle oui ou non~Une question qui invite à préciser~Une question fermée~Une simple consigne", 1,
     "Les questions ouvertes commencent souvent par comment, que, pourquoi."),
 QC("À quoi sert la reformulation ?", "À répéter mécaniquement~À vérifier la compréhension~À couper la parole~À conclure l'entretien", 1,
     "La reformulation confirme ou corrige ce que l'on a compris."),
 QC("Quel environnement favorise la compréhension ?", "Une télévision allumée~Un lieu calme et bien éclairé~Un couloir bruyant~Une pièce sombre", 1,
     "Le calme et la lumière facilitent la reception du message."),
 QC("Quel moyen aidera une personne qui ne parle pas ?", "Parler plus fort~Utiliser des images et des gestes~Ignorer sa parole~Répondre à sa place", 1,
     "Les supports visuels et gestuels compensent l'absence de mots."),
 QC("Comment annoncer une information difficile ?", "Très vite et sans pause~Avec des mots simples et un temps de silence~En plaisantant~Devant tout le groupe", 1,
     "La simplicité et le silence laissent le temps d'intégrer l'information.")],
[QT("Décrire les étapes d'un accueil réussi auprès d'une personne qui arrive dans un nouvel établissement.",
     "On se presente avec son nom et sa fonction, on regarde la personne et on se place a sa hauteur. On lui souhaite la bienvenue et on lui laisse un moment pour s'installer, sans multiplier les questions. On adapte le debit de parole et le vocabulaire a ce qu'elle semble comprendre. On lui explique simplement le déroulement de la journée et les personnes qu'elle va rencontrer. On pose des questions ouvertes sur ses habitudes et ses preferences, et on reformule pour verifier. On note les informations importantes dans le projet individualise. On l'accompagne jusqu'a sa chambre et on verifie qu'elle dispose de ce qu'il lui faut. Enfin, on transmet a l'equipe les elements recueillis, en restant discret sur les details inutiles.",
     "On attend presentence, ecoute, questions ouvertes, reformulation, adaptation et transmission."),
 QT("Une personne atteinte de troubles cognitifs ne comprend pas une consigne simple. Comment adapter votre communication ?",
     "On s'approche calmement, on attire son attention en l'appelant par son nom et on se place face a elle, a sa hauteur. On utilise une phrase courte, avec un seul message a la fois, et on accompagne la parole d'un geste ou d'un objet concret. On evite les questions multiples et le jargon professionnel. On laisse un temps de reponse suffisant sans la presser. On verifie la comprehension en demandant une reformulation simple ou en observant son action, plutot qu'en demandant « avez-vous compris ? ». Si la consigne reste incomprise, on propose une demonstration et on demande de l'aide a l'equipe. On note les methodes qui fonctionnent dans le dossier, car chaque personne a ses propres repères. On garde un ton respectueux, sans parler comme a un enfant.",
     "On attend adaptation du message, supports, patience, verification et traçabilité des méthodes efficaces.")],
C("Bien accueillir, c'est adapter le fond et la forme du message à la personne, puis vérifier la compréhension.",
  "messages courts + regard + hauteur adaptée + reformulation",
  "questions ouvertes = préciser · questions fermées = confirmer",
  "Accueil~Premier contact~Communication verbale~Mots et phrases~Communication non verbale~Regard et gestes~Reformulation~Vérification~Écoute~Réception du message",
  "Se présenter~Se placer à hauteur~Parler simplement~Écouter et reformuler~Transmettre les informations utiles",
  "Parler plus fort pour se faire comprendre|Multiplier les consignes|Juger une incompréhension|Oublier de vérifier la réception",
  "Nom~Repère d'identité~Calme~Condition d'écoute~Image~Support visuel~Silence~Temps d'intégration~Question ouverte~Invitation à préciser",
  "Question ouverte~Laisse le choix~Question fermée~Oui ou non",
  "Verbal~Mots et phrases~Non verbal~Regard, gestes et distance"))

# ============================================================ PP3
add("PP3", "L'observation et la transmission d'informations", "Pratique professionnelle", ["1re pro"],
S("L'observation est une attention deliberatee portee sur la personne, son environnement et les evenements du service."
  "|Elle porte sur les parametres vitaux, l'appetit, la mobilite, l'humeur, la douleur et les relations avec les autres."
  "|Une observation utile est precise, datée et decrite avec les mots de la personne."
  "|Il faut distinguer le fait observe de l'interpretation personnelle."
  "|« La personne a refusé de manger » est un fait ; « elle est déprimée » est une hypothèse."
  "|La transmission orale a lieu lors des relèves et des temps d'equipe, avec un ordre clair."
  "|La transmission ecrite est inscrite dans le dossier de suivi ou le cahier de transmission."
  "|Les informations essentielles sont : l'identite, la date, le gesture realise, la reaction observee et l'action a suivre."
  "|Un evenement inhabituel, même anodin, doit etre signale plutot que garde pour soi."
  "|La transmission à l'infirmier est obligatoire pour tout changement d'etat ou toute anomalie."
  "|Le secret professionnel s'applique : on transmet uniquement aux personnes concernees par la prise en charge."
  "|Une bonne transmission permet la continuite des soins et la securite de la personne."),
[QC("Qu'est-ce qu'une observation factuelle ?", "Un jugement personnel~Un fait précis et daté~Une supposition~Une opinion sur la famille", 1,
     "Un fait est observable et verifiable, contrairement a une interpretation."),
 QC("Quelle phrase est une interprétation ?", "Elle a bu un verre d'eau~Elle a refusé la toilette~Elle est déprimée~Elle est sortie à 10 heures", 2,
     "« Elle est déprimée » n'est pas directement observable."),
 QC("Quand transmettre une information à l'infirmier ?", "Une fois par semaine~Dès qu'un changement ou une anomalie est constaté~Jamais~Seulement à la fin du stage", 1,
     "Tout changement d'etat doit etre signale rapidement."),
 QC("Quel élément ne doit pas figurer dans une transmission ?", "La date~L'heure du geste~Une rumeur sur la famille~La réaction de la personne", 2,
     "Les rumeurs n'ont pas leur place dans un dossier professionnel."),
 QC("À qui transmet-on une information concernant une personne ?", "À toute l'équipe~Aux seuls professionnels concernés~Aux voisins~À la famille sans accord", 1,
     "La transmission est limitee au cercle de la prise en charge."),
 QC("Quel support permet la continuité entre les équipes ?", "Un carnet personnel~Le dossier de suivi~Un message sur un réseau social~Une note sur la porte", 1,
     "Le dossier de suivi est le support institutionnel de la continuite."),
 QC("Que signifie une transmission 'utile' ?", "Très longue~Précise, brève et exploitable~Écrite en jargon~Sans date", 1,
     "Une transmission utile est factuelle, concise et datée.")],
[QT("Réécrire une transmission vague en transmission factuelle : « Mme est pas bien ce matin, elle est triste. »",
     "« 24 novembre, 8 h 40 : Madame a pris un petit-déjeuner complet mais a refusé la toilette proposée. Elle a dit : Je n'ai pas envie de me lever aujourd'hui. Elle est restée assise au bord du lit, regard tourné vers la fenêtre. Température 37,1 °C, pouls 76, pas de plainte de douleur exprimée. J'ai prévenu l'infirmière à 8 h 55. À réévaluer après le repas. » Cette version remplace le jugement « triste et pas bien » par des faits observables, des propos exacts, des mesures et une action engagee. Elle permet à l'equipe de suivre l'evolution sans parti pris.",
     "On attend date, faits, propos exacts, mesures, action et absence d'interprétation."),
 QT("Expliquer pourquoi il ne faut pas différer la transmission d'un événement inhabituel.",
     "Un evenement inhabituel peut etre le premier signe d'une complication :une chute sans consequence apparente peut masquer un traumatisme, un refus de manger peut annoncer une douleur buccale, une agitation peut traduire une infection. Si l'information est gardee jusqu'a la fin de service, l'infirmier et le medecin perdent du temps et la personne reste sans prise en charge adaptee. La transmission immediate permet aussi de proteger les autres residents et les professionnels, par exemple en cas de trouble infectieux. Enfin, la trace datee est une preuve en cas d'evenement indesirable. Le role de l'accompagnant n'est pas de decider si l'evenement est grave, mais de le signaler avec les faits observes. C'est le professionnel compet qui evalue la suite a donner.",
     "On attend le lien avec la securite, la rapidite de prise en charge et la responsabilite.")],
C("Observer puis transmettre, c'est remplacer l'impression par des faits datés et utiles à la prise en charge.",
  "fait observé ≠ interprétation",
  "identité · date · geste · réaction · suite à donner",
  "Observation~Attention délibérée~Fait~Élément vérifiable~Interprétation~Hypothèse personnelle~Transmission~Information organisée~Dossier~Support de continuité",
  "Observer avec attention~Distinguer fait et hypothèse~Noter date et heure~Choisir le bon interlocuteur~Vérifier la suite donnée",
  "Écrire une opinion comme un fait|Différer un signalement|Transmettre à toute l'équipe|Oublier la date",
  "8 h 40~Heure de l'observation~Propos exacts~Citation fidèle~Infirmière~Interlocuteur compétent~À réévaluer~Suite à donner~Secret~Limite de transmission",
  "Fait~Ce qui est vu~Interprétation~Ce que l'on suppose",
  "Transmission orale~Relève et staff~Transmission écrite~Dossier de suivi"))

# ============================================================ PP4
add("PP4", "Le projet individualisé et le projet de vie", "Pratique professionnelle", ["1re pro"],
S("Le projet individualisé est une démarche qui adapte l'accompagnement aux besoins et aux attentes de la personne."
  "|Il s'inscrit dans le cadre du projet d'etablissement et du contrat de sejour."
  "|Le projet de vie exprime les souhaits, les habitudes, les valeurs et les objectifs de la personne."
  "|Un projet individualisé se construit avec la personne, pas pour elle."
  "|La personne en situation de handicap ou de dependance reste l'actrice principale de son projet."
  "|La famille et les proches peuvent contribuer, dans le respect de la parole de la personne."
  "|L'equipe pluriprofessionnelle met en commun les regards medical, social, psychologique et educatif."
  "|Le projet identifie des objectifs concrets, des actions, des responsables et des delais de reevaluation."
  "|Il peut concerner l'autonomie, la vie sociale, la sante, l'alimentation ou les loisirs."
  "|Les preferences quotidiennes — horaires, repas, activites — font partie du projet."
  "|Le projet est ecrit, consultable par les professionnels et reevalue regulierement."
  "|L'accompagnant contribue en observant, en ecoutant et en signalant les ecarts entre le projet et la pratique."),
[QC("Qui est l'acteur principal du projet individualisé ?", "La famille~La personne accompagnée~Le médecin~La direction", 1,
     "Le projet se construit avec la personne, qui reste l'actrice principale."),
 QC("Qu'est-ce que le projet de vie ?", "Un planning des soins~L'expression des souhaits et des objectifs de la personne~Un contrat de travail~Une prescription", 1,
     "Le projet de vie exprime les attentes et les valeurs de la personne."),
 QC("Quel est un objectif concret d'un projet individualisé ?", "Être heureux~Se lever à 8 h avec une aide technique adaptée~Aller mieux~Être bien traité", 1,
     "Un objectif opérationnel est precis, observable et evaluable."),
 QC("Qui participe à l'équipe pluriprofessionnelle ?", "Un seul soignant~Des professionnels de plusieurs disciplines~La seule famille~Le voisinage", 1,
     "L'equipe associe des competences medicales, sociales, psychologiques et educatives."),
 QC("Quand réévaluer le projet ?", "Jamais~Régulièrement et à chaque changement de situation~Une fois par an seulement~Après le départ", 1,
     "Le projet est évolutif et doit être reevalue."),
 QC("Quel rôle de l'accompagnant dans le projet ?", "Decider seul~Observer, écouter et signaler les écarts~Remplacer la famille~Écrire le diagnostic", 1,
     "L'accompagnant alimente le projet par son observation quotidienne."),
 QC("Le projet concerne-t-il les préférences quotidiennes ?", "Non, seulement les soins~Oui, y compris les horaires et les repas~Seulement les loisirs~Uniquement la famille", 1,
     "Les habitudes quotidiennes sont au cœur du projet individualise.")],
[QT("Expliquer la différence entre projet de vie et projet individualisé, puis montrer leur articulation.",
     "Le projet de vie est la dimension la plus personnelle : il exprime ce que la personne veut vivre, ses attentes, ses valeurs, ses souhaits pour son avenir et sa qualite de vie. Le projet individualise est l'outil operationnel qui traduit ces souhaits en objectifs concrets, en actions et en modalites de suivi, dans le cadre de l'etablissement. Par exemple, si une personne souhaite continuer a sortir, le projet de vie dit l'importance de cette sortie ; le projet individualise prevoit un accompagnement deux fois par semaine, une aide technique et une reevaluation mensuelle. Les deux se construisent avec la personne et l'equipe. L'articulation evite que le projet devienne un simple document administratif : il reste un outil de vie quotidienne pour les professionnels.",
     "On attend la difference entre souhait et traduction operationnelle, avec un exemple."),
 QT("Une résidente souhaite choisir elle-même son horaire de toilette, ce qui bouscule l'organisation du service. Comment traiter la demande ?",
     "On accueille la demande sans la juger et on cherche a comprendre ce qu'elle exprime : besoin de sommeil, pudeur vis-a-vis de certains soignants, habitude de longue date. On verifie si le projet individualise mentionne deja une preference et on consulte le dossier. On en discute avec l'equipe pour evaluer la faisabilite : effectif present, organisation des lever, autres soins a realiser. On propose une solution concrete, par exemple un créneau plus tardif ou deux temps de toilette, et on l'experimente sur une semaine. On informe la personne de la decision et on note l'accord dans le projet. On reevalue avec elle apres une semaine : si l'organisation ne tient pas, on cherche une autre solution plutot que d'imposer le rythme du service. Le respect du projet individualise suppose de faire negocier l'organisation avec le souhait de la personne, et non l'inverse.",
     "On attend ecoute, verification du projet, concertation, experimentation et reevaluation.")],
C("Le projet individualisé traduit le projet de vie en actions concrètes, avec la personne et l'équipe pluriprofessionnelle.",
  "projet de vie = souhaits · projet individualisé = objectifs et actions",
  "avec la personne, pas pour elle · réévaluation régulière",
  "Projet de vie~Souhaits et valeurs~Projet individualisé~Objectifs concrets~Autonomie~Capacité d'agir~Équipe pluriprofessionnelle~Regards croisés~Réévaluation~Suivi dans le temps",
  "Recueillir la parole~Associer la famille si souhaité~Définir des objectifs~Mettre en œuvre les actions~Réévaluer avec la personne",
  "Décider à la place de la personne|Réduire le projet à un document|Oublier de réévaluer|Ignorer les préférences quotidiennes",
  "Sortie~Objectif de vie~Deux fois par semaine~Action concrète~Horaire~Préférence quotidienne~Contrat de séjour~Cadre collectif~Aide technique~Moyen d'autonomie",
  "Projet de vie~Dimension personnelle~Projet individualisé~Traduction opérationnelle",
  "Avec la personne~Co-construction~Pour la personne~Risque de paternalisme"))

# ============================================================ PP5
add("PP5", "La relation d'aide et l'écoute active", "Pratique professionnelle", ["1re pro"],
S("La relation d'aide est un accompagnement qui vise à soutenir la personne dans l'expression de ses besoins et de ses ressources."
  "|Elle se distingue de la simple conversation par une intention professionnelle et un cadre."
  "|L'écoute active suppose d'être present, de regarder la personne et de suspendre ses propres jugements."
  "|Les techniques principales sont la reformulation, le silence, la clarification et la synthese."
  "|La reformulation renvoie avec ses mots ce que la personne a dit, pour verifier et montrer que l'on ecoute."
  "|Le silence respecte le temps de la personne et laisse venir ce qu'elle a du mal a formuler."
  "|Une question ouverte permet d'explorer ; une question fermée peut etre utile pour confirmer un point precis."
  "|Les emotions exprimees doivent etre accueillies sans etre jugées ni minimisées."
  "|Répondre « ce n'est rien » ferme la communication, alors que « je vous entends » l'ouvre."
  "|Le professionnel ne cherche pas a donner des conseils personnels ni a imposer sa solution."
  "|La relation d'aide a des limites : elle ne remplace pas un accompagnement psychologique specialise."
  "|Les informations recueillies sont traitees dans le respect du secret et transmises si necessaire a l'equipe."),
[QC("Qu'est-ce que l'écoute active ?", "Entendre sans rien faire~Une présence attentive et une reformulation~Donner des conseils~Répondre immédiatement", 1,
     "L'ecoute active engage l'attention, la reformulation et la suspension du jugement."),
 QC("Que signifie une reformulation ?", "Répéter mot pour mot~Renvoyer avec ses mots ce qui a été entendu~Changer de sujet~Donner son avis", 1,
     "La reformulation verifie la comprehension sans imposer d'interpretation."),
 QC("Quel est l'effet d'un silence respectueux ?", "Il bloque la parole~Il laisse le temps d'exprimer ce qui est difficile~Il montre l'indifférence~Il remplace l'écoute", 1,
     "Le silence est un outil de la relation d'aide lorsqu'il est habite."),
 QC("Quelle réponse ouvre la communication ?", "Ce n'est rien~Je vous entends~Vous exagérez~Il faut oublier", 1,
     "Reconnaitre ce qui est dit permet de poursuivre l'echange."),
 QC("Quel est le rôle d'une question ouverte ?", "Confirmer une information~Explorer ce que la personne ressent~Clore l'entretien~Imposer un choix", 1,
     "Les questions ouvertes favorisent l'expression."),
 QC("La relation d'aide remplace-t-elle un suivi psychologique ?", "Oui, toujours~Non, elle a des limites~Oui, si l'on est à l'écoute~Seulement en institution", 1,
     "Elle soutient mais ne remplace pas une prise en charge specialisee."),
 QC("Que faire d'une information confidentielle recueillie ?", "La garder coûte que coûte~La transmettre si nécessaire dans le cadre professionnel~La dire à la famille~L'ignorer", 1,
     "Le secret s'applique, avec des exceptions et des transmissions encadrées.")],
[QT("Décrire une situation où la reformulation a permis de mieux comprendre une personne.",
     "Une residente dit « je n'y arrive plus ». Au lieu de répondre « si, vous pouvez », je reste present et je reformule : « Vous avez l'impression que les gestes sont devenus trop difficiles ? » Elle precise alors qu'elle a peur de tomber lors de la toilette, parce qu'elle a déjà chuté. La reformulation a permis de passer d'une phrase vague à un besoin precis : la peur de la chute. J'ai pu adapter l'installation, proposer une aide technique et en parler à l'infirmier. Sans cette reformulation, j'aurais pu répondre à tort par un encouragement et passer a cote de la cause reelle. Cela montre que la reformulation n'est pas une repetition mecanique mais un outil de compréhension.",
     "On attend le lien entre reformulation, precision du besoin et action adaptée."),
 QT("Expliquer pourquoi il ne faut pas minimiser une émotion exprimée par une personne accompagnée.",
     "Dire « ce n'est rien » ou « vous verrez, ça ira mieux » nie le ressenti de la personne et lui donne le sentiment de ne pas etre entendue. Elle risque alors de se taire, alors que l'expression d'une tristesse, d'une colere ou d'une peur peut révéler un besoin important : douleur non dite, perte de repères, conflit, inquietude pour un proche. Accueillir l'emotion ne signifie pas la partager ni trouver une solution immediate : on nomme simplement ce que l'on percoit avec prudence, on reste present et on laisse du temps. On peut ensuite proposer de voir avec l'equipe ce qui peut aider. La personne se sent reconnue et la relation de confiance se consolide, ce qui facilite les soins ultérieurs.",
     "On attend le risque de rupture de communication, l'information sous-jacente et une alternative concretes.")],
C("La relation d'aide soutient l'expression de la personne : écouter, reformuler et laisser du temps, sans imposer de solution.",
  "reformulation + silence + questions ouvertes + accueil des émotions",
  "elle ne remplace pas un suivi psychologique spécialisé",
  "Relation d'aide~Accompagnement professionnel~Écoute active~Présence attentive~Reformulation~Vérification~Silence~Temps laissé~Émotion~Accueil sans jugement",
  "Se rendre disponible~ Observer sans juger~Reformuler~Laisser le silence~Transmettre si nécessaire",
  "Minimiser une émotion|Donner des conseils personnels|Remplacer un psychologue|Couper la parole",
  "Je vous entends~Accueil de l'émotion~Ce n'est rien~Réponse fermante~Peur de chuter~Besoin précis~Aide technique~Réponse adaptée~Secret~Cadre de l'échange",
  "Écoute active~Attention et reformulation~Écoute passive~Simple présence",
  "Question ouverte~Explorer~Question fermée~Confirmer"))

# ============================================================ PP6
add("PP6", "Le travail en équipe pluriprofessionnelle", "Pratique professionnelle", ["Terminale pro"],
S("Le travail en équipe pluriprofessionnelle associe des professionnels de metiers et de formations differents."
  "|Infirmiers, aides-soignants, medecins, travailleurs sociaux, ergotherapeutes et animateurs y participent selon les structures."
  "|Chaque professionnel apporte un regard et une competence specifiques, dans la limite de son role."
  "|La coordination vise a eviter la dispersion des interventions et les contradictions dans l'accompagnement."
  "|Le staff ou la releve est un temps collectif de transmission et de decision."
  "|Les outils communs sont le dossier de suivi, le cahier de transmission et les projets individualises."
  "|Une communication claire utilise des faits, un vocabulaire partage et des consignes explicites."
  "|Les conflits de points de vue doivent pouvoir s'exprimer dans un cadre respectueux."
  "|La decision finale revient au professionnel compet selon le domaine, souvent le medecin pour le medical."
  "|L'accompagnant contribue par son observation quotidienne, souvent la plus fine des changements."
  "|Travailler en equipe implique de respecter les horaires, les procedures et les signatures de chacun."
  "|La qualite de la coordination se mesure au ressenti de la personne et a la coherence des actions."),
[QC("Quel est l'avantage principal du travail en équipe ?", "Réduire le nombre de professionnels~Croiser les regards et coordonner les actions~Supprimer les transmissions~Décider sans consulter", 1,
     "La pluriprofessionalite enrichit l'analyse et rend les actions coherentes."),
 QC("Quel est un outil commun de coordination ?", "Un carnet personnel~Le dossier de suivi~Une conversation informelle~Un message privé", 1,
     "Le dossier de suivi est partage par les professionnels autorises."),
 QC("Quel rôle revient à l'accompagnant dans l'équipe ?", "Poser des diagnostics~Apporter une observation quotidienne~Prescrire des soins~Signer des ordonnances", 1,
     "Son observation fine des changements est une contribution essentielle."),
 QC("Qui prend une décision médicale ?", "L'accompagnant~La famille~Le professionnel médical compétent~Le voisin", 2,
     "La decision medicale revient au medecin, dans le cadre de ses competences."),
 QC("Comment se déroule une relève ?", "Sans ordre~Avec des transmissions orales structurées~En dehors du service~Par écrit uniquement et sans échange", 1,
     "La releve organise les informations et les actions a suivre."),
 QC("Que faire face à un désaccord dans l'équipe ?", "L'éviter~L'exprimer dans un cadre respectueux~Imposer son point de vue~En parler aux résidents", 1,
     "Le desaccord peut etre constructif s'il est exprime avec respect."),
 QC("Que mesure la qualité de la coordination ?", "Le nombre de réunions~La cohérence des actions et le ressenti de la personne~La taille de l'équipe~Le nombre de dossiers", 1,
     "L'objectif est la coherence au service de la personne.")],
[QT("Expliquer l'apport de chaque professionnel dans un accompagnement auprès d'une personne en perte d'autonomie.",
     "Le medecin etablit le diagnostic et prescrit les soins. L'infirmier assure les soins techniques, evalue l'etat de la personne et coordonne les actes medicals. L'aide-soignant realise les soins d'hygiene et de confort et est souvent le plus attentif aux changements quotidiens. Le travailleur social accompagne les demarches administratives et les relations avec la famille. L'ergotherapeute ou le kinesthesitherapeute travaille sur l'autonomie, la mobilite et les aides techniques. L'animateur propose des activites de vie sociale. Chaque regard complet les autres : la plainte entendue par l'aide-soignant, interpretee par l'infirmier et transmise au medecin, conduit a une decision adaptee. La coordination evite que la personne recoive des messages contradictoires.",
     "On attend plusieurs metiers, leurs roles et l'interet de la coordination."),
 QT("Lors d'un staff, vous estimez qu'une consigne de l'infirmier n'est pas adaptée à ce que vous observez. Comment en parler ?",
     "Je prepare mes elements avant la reunion : faits observes, dates, propos de la personne et consequences de la consigne. Je les presente de maniere factuelle, sans accusation, en disant par exemple : « Depuis deux jours, la personne refuse le lever à 7 h ; elle dit avoir mal au dos. » Je pose une question ouverte : « Peut-on réévaluer l'horaire ? » J'ecoute l'analyse de l'infirmier, qui dispose peut-etre d'elements que je n'ai pas. Si le desaccord persiste, je demande que la decision soit explicitee et tracee, et je sollicite le cadre si necessaire. Une fois la decision prise, je l'applique, meme si elle n'est pas celle que je proposais, tout en continuant à observer et à signaler les changements. Le respect des roles et la qualite de l'echange priment sur le besoin d'avoir raison.",
     "On attend preparation des faits, expression respectueuse, ecoute, decision tracée et application.")],
C("La coordination en équipe pluriprofessionnelle croise les compétences au service d'un accompagnement cohérent.",
  "l'observation de l'un éclaire la décision de l'autre",
  "dossier de suivi · relève · staff · respect des rôles",
  "Équipe pluriprofessionnelle~Métiers complémentaires~Coordination~Cohérence~Dossier de suivi~Outil commun~Relève~Transmission orale~Observation~Contribution quotidienne~Décision~Compétence délimitée",
  "Préparer ses observations~Les transmettre en réunion~Écouter les autres regards~Respecter la décision~Vérifier la cohérence finale",
  "Imposer son point de vue|Ne pas préparer la relève|Décider à la place du médecin|Laisser un désaccord s'installer sans en parler",
  "Staff~Temps collectif~Facts~Éléments objectifs~Médecin~Décision médicale~Cadre~Arbitrage~Projet individualisé~Référent commun",
  "Pluriprofessionnel~Plusieurs métiers~Interprofessionnel~Coopération entre pairs",
  "Observation~Remonter l'information~Décision~Prendre la responsabilité"))

# ============================================================ PP7
add("PP7", "Le bionettoyage et la prévention des risques", "Pratique professionnelle", ["Terminale pro"],
S("Le bionettoyage est une procedure de nettoyage et de desinfection destinee a reduire la charge microbienne d'un environnement."
  "|Il s'applique aux chambres, aux surfaces de soin, aux equipements et aux sanitaires."
  "|Il se distingue du simple nettoyage par l'objectif de maitrise de l'hygiene et par une methodologie precise."
  "|La procedure suit un ordre : débarrasser, depoussiérer, laver, rincer, desinfecter et sécher."
  "|On travaille du plus propre au plus sale et du haut vers le bas."
  "|Le matériel utilise est specifique : chiffons a usage unique ou codes couleur, balais brochés, distributaires fermes."
  "|Les produits sont choisis selon la surface et le niveau de risque : detergent, desinfectant, alcool."
  "|Le temps de contact du produit doit etre respecte pour que la desinfection soit efficace."
  "|Le port de gants et éventuellement d'un tablier protege le professionnel."
  "|Les risques professionnels comprennent les coupures, les projections, les glissades et les troubles musculo-squelettiques."
  "|Les donnees de vigilance et les incidents sont signales selon la procedure de l'etablissement."
  "|Une traçabilité des operations de bionettoyage permet de prouver que la procedure a ete appliquee."),
[QC("Qu'est-ce que le bionettoyage ?", "Un simple dépoussiérage~Une procédure de nettoyage et de désinfection~Une réparation~Une livraison de linge", 1,
     "Le bionettoyage vise a maitriser la charge microbienne par une methode codifiee."),
 QC("Quel ordre respecte-t-on ?", "Du sale vers le propre~Du propre vers le sale~Du bas vers le haut~Au hasard", 1,
     "On va du plus propre au plus sale pour ne pas reparer la contamination."),
 QC("Pourquoi respecter le temps de contact ?", "Pour faire sécher plus vite~Pour que le désinfectant agisse pleinement~Pour économiser l'eau~Pour éviter les odeurs", 1,
     "Un produit mal laisse en contact n'atteint pas son efficacite."),
 QC("Quel risque professionnel est lié au bionettoyage ?", "Une coupure ou une projection~Une brûlure solaire~Une allergie au bruit~Une chute de hauteur seulement", 0,
     "Coupures, projections et glissades sont des risques courants."),
 QC("Quel matériel limite la contamination croisée ?", "Un chiffon unique pour tout~Des chiffons à usage unique ou codés par couleur~Une éponge partagée~Un balai sans brosse", 1,
     "Le code couleur et l'usage unique distingue les zones et evitent les transfers."),
 QC("Que faut-il tracer ?", "L'heure de la pause~Les opérations réalisées et les incidents~Le nom du fournisseur~La météo", 1,
     "La trace prouve l'application de la procedure et permet le suivi."),
 QC("Qui coordonne une équipe de bionettoyage ?", "Le résident~Le coordinateur ou une personne désignée~Le livreur~Le voisin", 1,
     "Une personne designecoordonne les interventions selon les besoins du service.")],
[QT("Décrire la séquence complète d'un bionettoyage de chambre après le départ d'un résident.",
     "On retire et evacaue les dechets et le linge sale avec des gants. On depoussiere les surfaces hautes puis le mobilier, du haut vers le bas, avec un chiffon adapte. On lave les surfaces avec un detergent, du plus propre au plus sale : table, lit, then poignees, sol. On rince si necessaire, on applique le desinfectant sur les surfaces concerns et on respecte scrupuleusement le temps de contact indique. On laisse secher a l'air, sans rajouter de chiffon contaminé. On nettoie les sanitaires en dernier avec un materiel distinct. On retire les gants, on frictionne les mains, on range le materiel propre et on consigne l'operation dans la fiche de traçabilité avec l'heure et les incidents eventuels.",
     "On attend débarrasser, dépoussiérer, laver, rincer, désinfecter, sécher, et la traçabilité."),
 QT("Comment prévenir les troubles musculo-squelettiques lors des tâches de bionettoyage ?",
     "On alterne les taches et les postures pour eviter les gestes repetes. On utilise du materiel leger, manche telescope et balai brosse, sans forcer sur les articulations. On garde le dos droit, on plie les genoux pour ramasser et on rapproche la charge du corps. On évite les movements de torsion du tronc en deplaçant les pieds plutot qu'en tournant le buste. On organise le travail pour limiter les efforts prolonges au-dessus des epaules. On porte les gants adaptes et on signale toute douleur naissante avant qu'elle ne devienne chronique. La formation et les conseils du referent prevention completent ces habitudes. Enfin, on participe a l'analyse des situations a risque dans l'etablissement.",
     "On attend ergonomie, matériel adapté, alternance des tâches et signalement de la douleur.")],
C("Le bionettoyage est une procédure ordonnée qui protège la personne, le professionnel et l'environnement.",
  "débarrasser → dépoussiérer → laver → rincer → désinfecter → sécher",
  "du propre vers le sale · du haut vers le bas · temps de contact respecté",
  "Bionettoyage~Procédure d'hygiène~Désinfection~Réduction des microbes~Ordre~Du propre au sale~Temps de contact~Efficacité du produit~Risques~Coupures et glissades~Traçabilité~Preuve de l'action",
  "Préparer le matériel~Retirer les déchets~Nettoyer du haut vers le bas~Respecter le temps de contact~Tracer l'opération",
  "Utiliser le même chiffon partout|Ignorer le temps de contact|Forcer sur le dos|Ne pas signaler un incident",
  "Code couleur~Différencier les zones~Gants~Protection~Détergent~Nettoyage~Désinfectant~Assainissement~Fiche~Trace datée",
  "Nettoyage~Retirer les salissures~Désinfection~Réduire la charge microbienne",
  "Propre~Zone accueillie~Sale~Zone contaminée"))

# ============================================================ PP8
add("PP8", "L'éducation à la santé : concevoir une action", "Pratique professionnelle", ["Terminale pro"],
S("L'éducation à la santé vise à développer les connaissances et les comportements qui favorisent la sante."
  "|Elle s'adresse à un public cible dans un contexte donne : residents, families, adolescents, professionnels."
  "|Le référentiel ASSP fait de la conception d'une action d'éducation à la santé une unite de competence."
  "|La demarche comporte trois temps : analyser les besoins, concevoir l'action, la mettre en œuvre et l'evaluer."
  "|L'analyse des besoins identifie la problematique, le public, ses representations et les contraintes du lieu."
  "|Un objectif pedagogique est precis, mesurable et adapte au public : savoir, savoir-faire ou savoir-etre."
  "|Le contenu doit etre scientifiquement exact, compréhensible et utilise des sources fiables."
  "|Les supports peuvent etre des affiches, des jeux, des ateliers pratiques, des videos ou des jeux de role."
  "|L'action s'inscrit dans le projet d'etablissement et necessite l'accord de la direction."
  "|L'equipe pluriprofessionnelle est associee, notamment l'infirmier et le medecin pour les aspects medicalux."
  "|L'evaluation porte sur la participation, la comprehension et les changements observes, pas seulement sur le nombre de participants."
  "|Un retour d'experience permet d'ajuster l'action et de la reutiliser aupres d'un autre public."),
[QC("Quelle est la première étape d'une action d'éducation à la santé ?", "Concevoir l'affiche~Analyser les besoins du public~Annoncer les résultats~Acheter le matériel", 1,
     "On identifie d'abord la problematique et le public cible."),
 QC("Quel est un objectif pédagogique précis ?", "Savoir ce qu'est la bientraitance~Être capable de citer trois gestes d'hygiène des mains~Aimer la santé~Bien vivre ensemble", 1,
     "Un objectif operationnel est observable et evaluable."),
 QC("Quel public peut être ciblé ?", "Uniquement les résidents~Les résidents, les familles ou les professionnels~Personne~Seulement les médecins", 1,
     "Le public dépend du contexte et du besoin identifie."),
 QC("Quel critère de fiabilité pour le contenu ?", "Une opinion personnelle~Une source officielle vérifiable~Un souvenir~Une rumeur", 1,
     "Les informations doivent provenir de sources reconnues et datees."),
 QC("Quel support est adapté à un atelier pratique ?", "Un long texte~Une démonstration avec manipulation~Un tableau illisible~Une vidéo sans sous-titres", 1,
     "L'atelier pratique favorise l'appropriation par le faire."),
 QC("Qui faut-il associer à la conception ?", "Personne~L'équipe pluriprofessionnelle et la direction~Un seul collègue~Le fournisseur", 1,
     "L'action s'inscrit dans le projet d'etablissement et mobilise l'equipe."),
 QC("Que mesure l'évaluation d'une action ?", "Le nombre d'affiches~La compréhension et les changements observés~Le prix du matériel~La durée de la réunion", 1,
     "L'evalue porte sur les effets, pas seulement sur la production.")],
[QT("Concevoir en trois étapes une action d'éducation à la santé sur la prévention des chutes en EHPAD.",
     "1) Analyse des besoins : dans l'unite, huit chutes ont ete signalees en trois mois, principalement lors des levers et des transferts vers la salle de bain. Le public est compose de residents de plus de 80 ans, dont une majorite presentent une baisse de la vue et de la force musculaire. Les professionnels ont des pratiques de transfert differentes. 2) Conception : l'objectif est que les residents et les soignants sachent citer trois mesures de prevention et utilisent correctement les aides techniques. L'action combine un atelier de demonstration des transferts avec un lève-personne, une affiche comparee « bonnes et mauvaises installations » et une fiche remise aux familles. La direction valide le calendrier et l'infirmier verifie les contenus. 3) Evaluation : un questionnaire simple avant et apres, l'observation des transferts sur deux semaines et le suivi du nombre de chutes permettent de mesurer l'effet. Un retour d'experience avec l'equipe ajustera les supports.",
     "On attend les trois etapes, un objectif mesurable, des supports adaptes et des criteres d'evaluation."),
 QT("Pourquoi l'évaluation doit-elle porter sur la compréhension plutôt que sur la seule participation ?",
     "Le nombre de participants indique la frequence de l'action mais pas son effet. Une personne peut etre presente sans avoir compris le message, ou comprendre et modifier son comportement plus tard. Pour evaluer la comprehension, on utilise des questions simples, une demonstration ou une mise en situation : on demande par exemple de montrer le geste correct de friction des mains. On observe aussi les changements dans la pratique, comme l'utilisation effective du lave-personne ou la mention d'une preference de la personne dans le projet individualise. On croise les regards de l'equipe, car l'observation quotidienne est plus riche qu'un questionnaire unique. Enfin, on garde une trace de l'evaluation pour nourrir le retour d'experience et adapter l'action suivante.",
     "On attend la distinction participation / comprehension et desModalites d'evaluation concretes.")],
C("Concevoir une action d'éducation à la santé, c'est passer du besoin au projet puis à des effets mesurables.",
  "analyser les besoins → concevoir → mettre en œuvre → évaluer",
  "objectif précis · contenu fiable · supports adaptés · retour d'expérience",
  "Éducation à la santé~Action de prévention~Besoin~Problématique du public~Objectif~Cible mesurable~Support~Atelier ou affiche~Évaluation~Mesure des effets",
  "Identifier le public~Formuler l'objectif~Choisir les supports~Valider avec l'équipe~Évaluer et capitaliser",
  "Confondre présence et compréhension|Utiliser une source non vérifiée|Imposer un contenu sans concertation|Oublier le retour d'expérience",
  "Huit chutes~Besoin identifié~Lève-personne~Aide technique~Affiche~Support visuel~Avant et après~Mesure~Retour d'expérience~Amélioration",
  "Participation~Nombre de personnes~Compréhension~Effet réel de l'action",
  "Projet d'établissement~Cadre collectif~Projet individualisé~Réponse personnelle"))

# ============================================================ EG1
add("EG1", "Budget et gestion des dépenses d'un service", "Économie et gestion", ["1re pro"],
S("Un budget prevoit les recettes et les depenses d'un service sur une periode donnee, generalement un an."
  "|Le budget de fonctionnement couvre les depenses courantes : personnels, fournitures, energie, repas, entretien."
  "|Le budget d'investissement concerne les equipements durables : mobilier, materiel medical, travaux."
  "|Les depenses sont classees par nature et imputees a des comptes selon la nomenclature comptable."
  "|Le suivi budgetaire compare les depenses reelles aux previsions, mois apres mois."
  "|Un ecart favorable signifie une depense inferieure au prevu ; un ecart defavorable signifie un depassement."
  "|La regulisation des depenses engage le responsable du budget, qui doit justifier les ecarts."
  "|Les achats suivent une procedure : expression du besoin, consultation, commande, reception et facturation."
  "|Le respect de la procedure garantit la conformite et permet le controle interne."
  "|Une depense non prevue doit etre signalee et autorisee avant d'etre engagee, sauf urgence."
  "|La qualite de la gestion contribue a la qualite des prestations : les ressources doivent servir la personne."
  "|Un accompagnant peut contribuer en signalant les besoins en materiel et en evitant le gaspillage."),
[QC("Que couvre un budget de fonctionnement ?", "Les seuls travaux~Les dépenses courantes comme le personnel et les fournitures~Les seuls impôts~Les seuls investissements", 1,
     "Le budget de fonctionnement finance les dépenses repetees de l'annee."),
 QC("Quel est un budget d'investissement ?", "Le pain et le linge~Le mobilier et le matériel durable~Les salaires~Le chauffage", 1,
     "Les investissements concernent des biens durables."),
 QC("Que signifie un écart défavorable ?", "Une dépense inférieure au prévu~Un dépassement des prévisions~Une recette imprévue~Un budget équilibré", 1,
     "Un ecart defavorable correspond a une depense superieure au budget."),
 QC("Quelle est la dernière étape d'un achat ?", "La commande~La facturation et le paiement~Le besoin~La consultation", 1,
     "La procedure se termine par la reception, la facturation et le paiement."),
 QC("Que faire devant une dépense non prévue ?", "L'engager sans rien dire~La signaler et demander une autorisation~La cacher~La payer personnellement", 1,
     "Toute depense hors budget doit etre autorisee selon la procedure."),
 QC("À quoi sert le suivi budgétaire ?", "À comparer prévisions et réalisations~À augmenter les prix~À supprimer les contrôles~À changer de nomenclature", 0,
     "Le suivi met en evidence les ecarts et aide a la decision."),
 QC("Quel rôle de l'accompagnant dans la gestion ?", "Signaler les besoins et limiter le gaspillage~Signer les factures~Fixer le budget~Réaliser l'audit", 0,
     "Son observation quotidienne alimente la gestion du service.")],
[QT("Un service prévoit 12 000 € de fournitures pour l'année. Après six mois, 7 200 € ont été dépensés. Analyser la situation.",
     "La depense prevue pour six mois est la moitie du budget annuel, soit 6 000 €. La depense reelle est de 7 200 €, soit un depassement de 1 200 €, ou 20 % du semestre. Si le rythme se poursuit, la depense annuelle atteindra 14 400 €, soit 2 400 € de plus que le budget. Il faut rechercher les causes : hausse des prix, consommation plus importante, achats non prevus ou erreur de saisie. On comparera les postes détailles et on vérifiera les commandes passees. Des mesures correctives peuvent etre proposees : regrouper les commandes, negocier les tarifs, limiter le gaspillage, revoir les quantites. On presentera l'analyse au responsable avec des chiffres precis et des pistes d'action, sans modifier le budget sans accord.",
     "On attend le calcul de l'ecart, la projection annuelle, la recherche de causes et des mesures."),
 QT("Expliquer pourquoi les économies réalisées sur les fournitures ne doivent pas nuire à la qualité de l'accompagnement.",
     "Le budget est un outil au service de la prise en charge, et non une fin en soi. Reduire les depenses en supprimant des gants, du linge ou des produits de bionettoyage peut augmenter les infections, les escarres ou les chutes, et finalement accroitre les couts et la souffrance des personnes. Une gestion responsable cherche aoptimiser, par exemple en evitant le gaspillage, en choisissant des produits adapts et en regroupant les achats, plutot qu'a supprimer le necessaire. L'accompagnant est bien place pour signaler une quantite insuffisante ou un materiel inadapte. Les decisions d'economie doivent etre evaluees au regard de la qualite et de la securite, en lien avec l'equipe pluriprofessionnelle et la direction.",
     "On attend le primat de la qualite, les risques d'une restriction et les economies intelligentes.")],
C("Le budget prévoit et suit les dépenses ; le suivi des écarts permet d'agir sans nuire à la qualité des soins.",
  "fonctionnement = dépenses courantes · investissement = biens durables",
  "écart = réalisé − prévu · achat : besoin, consultation, commande, réception, paiement",
  "Budget~Prévision des dépenses~Fonctionnement~Dépenses courantes~Investissement~Bien durable~Écart~Différence prévu et réel~Achat~Procedure d'achat~Suivi~Contrôle régulier",
  "Prévoir les dépenses~Suivre les réalisations~Calculer les écarts~Rechercher les causes~Proposer des actions correctives",
  "Engager une dépense sans autorisation|Réduire le matériel nécessaire|Confondre investissement et fonctionnement|Ignorer un écart répété",
  "12 000 €~Budget annuel~7 200 €~Dépense semestrielle~1 200 €~Dépassement~14 400 €~Projection annuelle~Gaspillage~Économie possible",
  "Écart favorable~Dépense moindre~Écart défavorable~Dépassement",
  "Budget de fonctionnement~Dépenses de l'année~Budget d'investissement~Équipements durables"))

# ============================================================ EG2
add("EG2", "TVA, prix et facturation", "Économie et gestion", ["1re pro"],
S("La TVA, taxe sur la valeur ajoutee, est un impot indirect applique a la plupart des biens et services."
  "|Elle est collectee par les entreprises pour le compte de l'Etat et reversee periodiquement."
  "|Le taux normal en France est de 20 % ; il existe des taux réduits comme 10 % et 5,5 %."
  "|Un prix hors taxes, ou HT, devient un prix toutes taxes comprises, ou TTC, en ajoutant la TVA."
  "|Prix TTC = prix HT × (1 + taux de TVA)."
  "|Pour calculer le prix HT à partir du TTC, on divise par (1 + taux)."
  "|La marge commerciale est la difference entre le prix de vente HT et le prix d'achat HT."
  "|Le taux de marge se calcule par (marge / prix d'achat HT) × 100."
  "|Une remise est une reduction accordee sur un prix, souvent exprimee en pourcentage."
  "|La facture doit mentionner l'identite du vendeur et du client, la date, la designation, les quantites, les prix HT, le taux et le montant de TVA, et le total TTC."
  "|Dans les etablissements, la facturation des prestations suit des regles propres au secteur medical ou medico-social."
  "|Une facturation exacte est indispensable au suivi budgetaire et au respect de la reglementation."),
[QC("Quel est le taux normal de TVA en France ?", "5,5 %~10 %~20 %~33 %", 2,
     "Le taux normal de la TVA en France est de 20 %."),
 QC("Comment calculer un prix TTC ?", "HT multiplié par (1 + taux)~HT divisé par (1 + taux)~HT moins TVA~HT plus 20 €", 0,
     "On ajoute la TVA au prix HT en multipliant par 1 + taux."),
 QC("Comment retrouver le prix HT à partir du TTC ?", "TTC multiplié par 1,2~TTC divisé par 1,2~TTC moins 20 %~TTC plus 20 %", 1,
     "La division par 1 + taux donne le prix hors taxes."),
 QC("Comment calculer une marge commerciale ?", "Prix de vente HT prix d'achat HT~Prix de vente HT moins prix d'achat HT~Prix TTC moins TVA~Prix d'achat plus TVA", 1,
     "La marge est la difference entre le prix de vente HT et le prix d'achat HT."),
 QC("Sur quoi porte le taux de marge ?", "Le prix de vente TTC~Le prix d'achat HT~Le montant de TVA~Le total de la facture", 1,
     "Le taux de marge se calcule par rapport au prix d'achat HT."),
 QC("Quelle mention doit figurer sur une facture ?", "La couleur du produit~Le montant de TVA et le total TTC~Le nom du livreur~L'heure de livraison", 1,
     "La facture doit notamment indiquer la TVA et le total TTC."),
 QC("Qui collecte la TVA ?", "Le client~L'entreprise vendeuse~La banque~La commune", 1,
     "Le vendeur collecte la TVA puis la reverse a l'Etat.")],
[QT("Un établissement achète des draps à 8 € HT l'unité et les revend 12 € HT. Calculer la marge et le taux de marge.",
     "La marge commerciale unitaire vaut 12 € − 8 € = 4 €. Le taux de marge se calcule par marge divisée par prix d'achat HT, soit 4 / 8 = 0,5, donc 50 %. Si l'etablissement achete 200 draps, la marge totale est de 200 × 4 € = 800 €. La TVA ne rentre pas dans le calcul de la marge, car celle-ci se calcule hors taxes des deux cotes. Le prix TTC de vente avec un taux de 20 % serait de 12 € × 1,2 = 14,40 €. Le taux de marque, different du taux de marge, serait marge sur prix de vente, soit 4 / 12 = 33,3 %.",
     "On attend la marge, le taux de marge sur achat HT et la distinction avec le taux de marque."),
 QT("Une facture indique un total TTC de 480 € avec une TVA à 20 %. Calculer le montant HT et la TVA, puis vérifier le résultat.",
     "Le prix HT s'obtient en divisant le TTC par 1 + taux : 480 / 1,2 = 400 €. La TVA represente 20 % de 400 €, soit 400 × 0,2 = 80 €. La verification consiste a additionner : 400 € + 80 € = 480 €, ce qui redonne bien le total TTC indique. On peut aussi verifier en calculant 480 × (1 − 1/1,2) = 480 × 0,1667, soit environ 80 €. Une erreur freuquente consiste a prelever 20 % sur le TTC, ce qui donnerait 96 € et un HT de 384 €, resultat incorrect car la TVA est assise sur le prix HT.",
     "On attend la division par 1,2, le calcul de la TVA et l'explication de l'erreur frequente.")],
C("La TVA s'ajoute au prix hors taxes ; la marge se calcule hors taxes et rapportée au prix d'achat.",
  "TTC = HT × (1 + taux) · HT = TTC / (1 + taux)",
  "marge = vente HT − achat HT · taux de marge = marge / achat HT × 100",
  "TVA~Taxe sur la valeur ajoutée~Prix HT~Hors taxes~Prix TTC~Toutes taxes comprises~Marge~Différence de prix~Facture~Document de vente~Remise~Réduction",
  "Repérer les montants HT~Appliquer le taux~Calculer la marge~Vérifier la facture~Conserver le document",
  "Calculer la TVA sur le TTC|Confondre marge et taux de marque|Oublier de préciser le taux|Ne pas vérifier le total",
  "8 € HT~Prix d'achat~12 € HT~Prix de vente~4 €~Marge unitaire~50 %~Taux de marge~480 € TTC~400 € HT et 80 € de TVA",
  "Marge~Rapportée à l'achat~Taux de marque~Rapporté à la vente",
  "Prix HT~Avant impôt~Prix TTC~Après impôt"))

# ============================================================ EG3
add("EG3", "Coûts et tarification en établissement", "Économie et gestion", ["Terminale pro"],
S("La tarification d'un etablissement social ou medico-social fixe les recettes necessaires a son fonctionnement."
  "|Les recettes proviennent notamment de l'Assurance maladie, des departements, des residentiels et de subventions."
  "|Les couts se classent en charges directes et charges indirectes, ou en charges fixes et variables."
  "|Les charges de personnel representent généralement la part la plus importante du budget."
  "|Un cout unitaire rapporte une charge au nombre d'actes ou de journees d'hebergement."
  "|Le cout par journee d'hebergement s'obtient en divisant les charges par le nombre de journees realisees."
  "|Le taux d'occupation influence fortement ce cout unitaire : plus il est eleve, plus le cout par journee baisse."
  "|La tarification est encadree par des regles administratives et conventionnelles."
  "|Le budget doit equilibrer les recettes et les charges, tout en respectant la qualite des prestations."
  "|Une analyse des ecarts permet de comprendre les differences entre budget prevu et realise."
  "|Les decisions d'effectif et d'organisation ont un impact direct sur les couts et sur l'accompagnement."
  "|L'accompagnant contribue par la qualite de ses transmissions et par une utilisation raisonnee des ressources."),
[QC("Quelle est généralement la plus importante charge d'un établissement ?", "Les fournitures~Les charges de personnel~L'électricité~Le linge", 1,
     "Les salaires et charges sociales representent la part la plus elevee."),
 QC("Comment calculer un coût par journée d'hébergement ?", "Charges multipliées par le nombre de journées~Charges divisées par le nombre de journées~Charges moins recettes~Recettes divisées par charges", 1,
     "Le cout unitaire rapporte les charges au nombre de journees."),
 QC("Quel est l'effet d'un taux d'occupation plus élevé ?", "Le coût par journée augmente~Le coût par journée diminue~Aucun effet~Les recettes diminuent", 1,
     "Les charges fixes sont réparties sur plus de journees, ce qui reduit le cout unitaire."),
 QC("Qu'appelle-t-on charge directe ?", "Une charge difficile à identifier~Une charge attribuable directement à une activité~Une recette~Un impôt", 1,
     "Une charge directe est rattachee sans ambiguite a une activite."),
 QC("D'où viennent les recettes d'un EHPAD ?", "Uniquement des résidents~De l'Assurance maladie, des départements et des résidents~Des seules subventions~Du seul tourisme", 1,
     "Le financement est multiple et encadre par des regles."),
 QC("Quel est un objectif de l'analyse des écarts ?", "Augmenter les prix~Comprendre les différences entre prévu et réalisé~Supprimer le budget~Cacher les erreurs", 1,
     "L'analyse des ecarts éclaire la gestion et la decision."),
 QC("Quel lien existe-t-il entre organisation et coûts ?", "Aucun~Les choix d'effectifs et d'organisation influencent directement les coûts~Seuls les prix comptent~Les coûts sont fixes par nature", 1,
     "L'organisation du service est un levier de maitrise des couts.")],
[QT("Un établissement a 1 200 000 € de charges annuelles et 30 000 journées d'hébergement. Calculer le coût par journée et expliquer son intérêt.",
     "Le cout par journee vaut 1 200 000 € divisés par 30 000 journees, soit 40 € par journee. Cet indicateur permet de comparer le cout de l'etablissement avec ceux d'une periode precedente ou avec des etablissements similaires. Il sert aussi a la tarification : le tarif journalier doit couvrir ce cout, dans le cadre des regles administratives. Si le taux d'occupation augmente, le nombre de journees augmente et le cout unitaire baisse, car les charges fixes sont etalees. A l'inverse, une baisse d'occupation augmente le cout par journee. Cet indicateur ne dit rien de la qualite de l'accompagnement : il doit etre lu avec des indicateurs de qualite et d'activite.",
     "On attend le calcul, l'interpretation et les limites de l'indicateur."),
 QT("Comment concilier la maîtrise des coûts et la qualité de l'accompagnement ?",
     "On ne confond pas maitrise et restriction : il s'agit d'eviter le gaspillage et d'optimiser les ressources, non de supprimer les moyens necessaires aux soins. On identifie les postes ou des economies sont possibles sans effet sur la personne : regroupement des achats, gestion des stocks, armature des deplacements, choix de produits adapts et durables. On egarderencontre les indicateurs de qualite — chutes, escarres, plaintes, satisfaction — avec les indicateurs financiers pour verifier qu'une economie ne deteriore pas la prise en charge. Les decisions sont prises en equipe, avec la direction, le medecin et les professionnels de terrain. L'accompagnant apporte sa connaissance du quotidien : il sait si un materiel est adapte ou si une quantite manque. La transparence des choix et l'evaluation réguliere permettent de concilier les deux exigences.",
     "On attend distinction maitrise et restriction, exemples d'optimisation et pilotage par indicateurs.")],
C("La tarification finance des prestations dont la qualité doit être préservée ; le coût unitaire aide à piloter sans rogner sur l'essentiel.",
  "coût par journée = charges / nombre de journées",
  "taux d'occupation élevé = coût unitaire plus faible",
  "Tarification~Fixation des recettes~Charge directe~Attribution à une activité~Coût unitaire~Rapport au nombre d'actes~Journée d'hébergement~Unite d'activité~Occupation~Taux de remplissage~Qualité~Objectif prioritaire",
  "Identifier les charges~Décompter les journées~Calculer le coût unitaire~Analyser les écarts~Décider en équipe",
  "Réduire le personnel sans évaluer l'impact|Confondre coût et qualité|Ignorer le taux d'occupation|Ne pas consulter le terrain",
  "1 200 000 €~Charges annuelles~30 000~Journées~40 €~Coût par journée~Charges de personnel~Poste principal~Assurance maladie~Source de recettes",
  "Charge fixe~Indépendante de l'activité~Charge variable~Liée au nombre d'actes",
  "Coût~Ce que dépense l'établissement~Tarif~Ce que facture l'établissement"))

# ============================================================ EG4
add("EG4", "Qualité et évaluation des prestations", "Économie et gestion", ["Terminale pro"],
S("La demarche qualite vise a ameliorer en continu la qualite des prestations rendues aux personnes."
  "|Elle s'appuie sur des normes, des procedures et des indicateurs definis par l'etablissement et les autorites."
  "|La qualite concerne la securite, l'hygiene, la satisfaction, la continuite et l'adaptation des prestations."
  "|Une procedure ecrite decrit les etapes d'un geste et les responsabilites de chacun."
  "|Un indicateur est un outil de mesure : taux d'escarres, nombre de chutes, delai de transmission, taux de satisfaction."
  "|L'audit interne compare la pratique reelle aux procedures et identifie les ecarts."
  "|Les retours d'experience analyzent les evenements indesirables sans rechercher de coupable."
  "|La certification et les evaluations externes constituent des obligations pour les etablissements."
  "|Les usagers et leurs proches participent a l'evaluation, notamment par le conseil de la vie sociale."
  "|Les plaintes et les reclamations sont des sources d'information precieuses pour progresser."
  "|L'amélioration continue suit un cycle : planifier, realiser, verifier, agir."
  "|L'accompagnant contribue en appliquant les procedures, en signalant les ecarts et en participant aux retours."),
[QC("Qu'appelle-t-on un indicateur de qualité ?", "Une opinion personnelle~Un outil de mesure chiffré~Une simple procédure~Un avis de la direction", 1,
     "Un indicateur permet de mesurer et de suivre un aspect de la qualite."),
 QC("Quel est l'objet d'un audit interne ?", "Vendre un service~Comparer la pratique aux procédures~Remplacer le contrôle médical~Éviter les réunions", 1,
     "L'audit identifie les ecarts entre les procedures et la realite."),
 QC("Que vise un retour d'expérience ?", "Trouver un coupable~Comprendre les causes et améliorer~Clore un dossier sans action~Augmenter les sanctions", 1,
     "Le retour d'experience est une analyse collective et non punitive."),
 QC("Qui participe à l'évaluation de la qualité ?", "La seule direction~Les professionnels et les usagers~Les seuls médecins~Personne", 1,
     "L'evaluation associe les equipes, les usagers et les proches."),
 QC("Quel est un indicateur pertinent ?", "La couleur des murs~Le nombre de chutes par mois~Le prix du mobilier~La taille du jardin", 1,
     "Le nombre de chutes est un indicateur de securite et de qualite."),
 QC("Quel est le cycle de l'amélioration continue ?", "Voir, dire, faire~Planifier, réaliser, vérifier, agir~Acheter, vendre, facturer~Écrire, signer, classer", 1,
     "Le cycle PLAN, DO, CHECK, ACT structure la demarche qualite."),
 QC("Que faire d'une réclamation ?", "L'ignorer~L'enregistrer et l'analyser~La rejeter~La cacher", 1,
     "Une reclamation est une source d'information pour progresser.")],
[QT("Expliquer pourquoi les indicateurs doivent être choisis avec soin et non multipliés sans objectif.",
     "Un indicateur utile est lie a un objectif clair, fiable, mesurable dans le temps et exploitable par les equipes. Trop d'indicateurs diluent l'attention et produisent des donnees que personne n'utilise. Certains indicateurs peuvent aussi detourner l'action de leur objectif : si l'on ne mesure que la rapidite des transmissions, on peut perdre en qualite d'observation. Il faut donc choisir quelques indicateurs significatifs, les expliquer aux professionnels et les relier aux actions d'amelioration. Leur lecture doit etre partagee en equipe et croisee avec le ressenti des usagers. Un indicateur n'est pas une fin en soi : il sert a declencher une reflexion et une action concrete, puis a verifier l'effet de cette action.",
     "On attend qualites d'un bon indicateur, risques de la multiplication et lien avec l'action."),
 QT("Après une chute sans gravité, comment conduire un retour d'expérience utile ?",
     "On rassemble les faits : date, heure, lieu, circonstances, etat de la personne, signes observes et actions engagees. On ecoute la personne et les professionnels presents, sans rechercher de responsable. On analyse les facteurs contributifs : etat de la personne, medicaments, installation, lit trop haut, aide technique absente, sol glissant, effectif du moment. On identifie les mesures correctives : regler la hauteur du lit, prévoir une aide technique, adapter la surveillance ou modifier une procedure. On designe un responsable et une echeance pour chaque action, puis on les trace. On informe l'equipe des enseignements et on doit reevaluer l'indicateur de chutes apres quelques semaines. Le retour d'experience doit rester une demarche d'apprentissage collectif, accessible a tous les professionnels.",
     "On attend faits, causes systemiques, actions correctives, responsables et suivi.")],
C("La qualité est une démarche continue : mesurer, comparer, comprendre et améliorer avec les équipes et les usagers.",
  "planifier · réaliser · vérifier · agir",
  "indicateurs · audit interne · retour d'expérience · participation des usagers",
  "Qualité~Niveau de service~Indicateur~Mesure suivie~Audit~Comparaison aux procédures~Retour d'expérience~Analyse sans faute~Usager~Participant à l'évaluation~Amélioration~Action correctrice",
  "Appliquer les procédures~Relever les écarts~Mesurer les indicateurs~Analyser en équipe~Mettre en œuvre et vérifier",
  "Chercher un coupable|Multiplier les indicateurs inutiles|Ignorer une réclamation|Ne pas suivre les actions décidées",
  "Nombre de chutes~Indicateur de sécurité~Audit~Écart identifié~Plan~Étape de la démarche~Action corrective~Amélioration~Conseil de la vie sociale~Parole des usagers",
  "Audit~Vérifier la conformité~Retour d'expérience~Comprendre les causes",
  "Qualité~Conformité et satisfaction~Quantité~Volume d'activité"))

# ============================================================ LA1
add("LA1", "Le lexique professionnel des soins en anglais", "Langues", ["1re pro"],
S("Le lexique professionnel permet de nommer precisement les gestes, les personnes et les situations de soin."
  "|Les verbes de soin courants sont to wash, to dress, to feed, to lift, to check et to record."
  "|Un care assistant accompagne la personne ; un nurse est un infirmier et un carer est un aidant."
  "|Les parties du corps se nomment : head, arm, hand, leg, foot, back et skin."
  "|Les troubles frequents sont pain, fever, cough, rash, dizziness et fatigue."
  "|Les parametres vitaux se disent temperature, pulse, blood pressure et breathing."
  "|Le materiel de soin comprend thermometer, gloves, wheelchair, hoist et dressings."
  "|Les adjectifs utiles sont dry, wet, clean, dirty, calm, painful et comfortable."
  "|La prononciation et l'epellation doivent etre verifiees pour eviter les confusions entre mots proches."
  "|Un lexique personnel classe par situation est plus facile a retenir qu'une liste alphabetique."
  "|La memorisation s'ameliore par des phrases courtes : « I check the temperature. »"
  "|En stage, un lexique fiable permet de comprendre une consigne et de se faire comprendre."),
[QC("Que signifie « to dress » ?", "Laver~Habiler~Nourrir~Soulever", 1,
     "To dress signifie habiller ; to wash signifie laver."),
 QC("Quel mot désigne un infirmier ?", "Carer~Nurse~Resident~Doctor's assistant", 1,
     "Nurse est l'infirmier ; carer est l'aidant ou accompagnant."),
 QC("Comment dit-on « douleur » ?", "Fever~Pain~Rash~Cough", 1,
     "Pain designe la douleur ; fever est la fievre."),
 QC("Quel mot désigne la pression artérielle ?", "Pulse~Blood pressure~Breathing~Temperature", 1,
     "Blood pressure correspond a la tension arterielle."),
 QC("Quel matériel sert à mesurer la température ?", "A hoist~A thermometer~A dressing~A wheelchair", 1,
     "Un thermometre mesure la temperature."),
 QC("Quel adjectif signifie « sec » ?", "Wet~Dry~Dirty~Calm", 1,
     "Dry signifie sec, wet signifie mouille."),
 QC("Quelle phrase est correcte ?", "I check the temperature~I checking the temperature~I am check the temperature~I checked temperature the", 0,
     "Le present simple « I check the temperature » est correct.")],
[QT("Classer douze mots du lexique des soins en quatre catégories : gestes, personnes, symptômes et matériel.",
     "Gestes : to wash, to dress, to check, to lift. Personnes : nurse, carer, resident, doctor. Symptomes : pain, fever, cough, dizziness. Materiel : thermometer, gloves, wheelchair, hoist. Cette classification par situation est plus efficace qu'une simple liste alphabetique, car elle permet de retrouver le mot au moment ou l'on en a besoin. Pour chaque mot, on peut ecrire une phrase courte : « I check the temperature », « The resident has pain », « I use a hoist ». On ajoute la prononciation pour les mots difficiles comme wheelchair ou thermometer. On revisera le lexique avant chaque stage et on l'enrichira avec les mots entendus sur le terrain.",
     "On attend quatre categories, des mots pertinents et des phrases d'exemple."),
 QT("Expliquer pourquoi la précision du lexique est importante dans une situation de soin.",
     "Un mot imprecis peut modifier le sens d'une consigne et mettre en cause la securite de la personne. Confondre dry et wet, ou pain et fever, conduit a une observation erronee. Confondre nurse et carer brouille les responsabilites : l'accompagnant ne doit pas realiser un acte medical relevant de l'infirmier. Une consigne comme « Check the blood pressure before the wash » doit etre comprise exactement, avec le bon parametre et le bon moment. La precision du lexique facilite aussi les transmissions ecrites et orales entre professionnels de langues differentes. Pour l'apprendre, on associe le mot a une image, a un geste et a une phrase, puis on le reutilise regulierement en situation plutot que de le seulement lire.",
     "On attend le lien entre mot juste, securite, responsabilites et qualite de transmission.")],
C("Le lexique des soins s'apprend par situations et sert à comprendre, transmettre et agir avec précision.",
  "to wash · to dress · to check · to lift · to record",
  "nurse / carer · pain / fever · thermometer / hoist",
  "Gestes~Verbes d'action~Personnes~Professionnels et usagers~Symptômes~Signes cliniques~Matériel~Objets de soin~Phrase~Exemple d'usage",
  "Choisir une situation~Lister les mots utiles~Associer image et geste~Écrire une phrase courte~Réviser avant le stage",
  "Apprendre une liste sans contexte|Confondre deux mots proches|Oublier la prononciation|Traduire mot pour mot sans vérifier",
  "To wash~Laver~Nurse~Infirmier~Pain~Douleur~Thermometer~Thermomètre~Blood pressure~Tension",
  "Carer~Accompagnant~Nurse~Infirmier~Resident~Personne accueillie",
  "Pain~Douleur~Fever~Fièvre"))

# ============================================================ LA2
add("LA2", "Lire une notice et un protocole en anglais", "Langues", ["Terminale pro"],
S("Une notice ou un protocole en anglais est un document technique qui decrit une procedure ou un mode d'emploi."
  "|On y trouve des titres, des avertissements, des etapes numerotees et des conditions d'utilisation."
  "|Les mots-cles sont souvent en majuscules : WARNING, CAUTION, DO NOT, BEFORE USE."
  "|« Warning » signale un danger serieuse ; « caution » attire l'attention sur un risque moindre."
  "|« Do not » exprime une interdiction absolue."
  "|« Before use » indique une action a realiser avant l'emploi ; « after use » apres emploi."
  "|Les verbes a l'imperatif decrivent les etapes : open, check, apply, hold, remove, store."
  "|Les units de mesure et les concentrations doivent etre lues avec attention : ml, mg, %, minutes."
  "|Une abbreviation comme « q.d. » ou « b.i.d. » designe une frequence d'administration."
  "|La date de peremption se dit « expiry date » et le numero de lot « batch number »."
  "|Avant d'appliquer un protocole, on verifie qu'il correspond bien au produit et a la situation."
  "|En cas de doute sur la comprehension, on demande confirmation au professionnel responsable avant toute action."),
[QC("Que signifie « WARNING » ?", "Une recommandation~Un avertissement de danger sérieux~Une étape facultative~Une date", 1,
     "Warning signale un risque serieux, plus fort que caution."),
 QC("Quelle expression exprime une interdiction ?", "Before use~Do not~After use~Hold", 1,
     "Do not signifie ne pas faire, de maniere absolue."),
 QC("Que signifie « expiry date » ?", "La date de fabrication~La date de péremption~Le numéro de lot~La date de commande", 1,
     "Expiry date est la date apres laquelle le produit ne doit plus etre utilise."),
 QC("Quel mot désigne une étape du protocole ?", "Apply~Warning~Batch~Expiry", 0,
     "Apply fait partie des verbes d'action a l'imperatif."),
 QC("Que signifie « caution » ?", "Un danger majeur~Une attention particulière~Une interdiction~Une validation", 1,
     "Caution attire l'attention sur un risque ou une precaution."),
 QC("Quelle unité est une concentration ?", "mg~ml~%~minute", 2,
     "Le pourcentage exprime une concentration."),
 QC("Que faire en cas de doute sur une consigne ?", "Appliquer quand même~Demander confirmation avant d'agir~Traduire au hasard~Ignorer le document", 1,
     "La securite impose de faire confirmer par le professionnel responsable.")],
[QT("Traduire et commenter un extrait de notice : « WARNING: Do not use after the expiry date. Store in a dry place, away from direct sunlight. Apply thinly and wash your hands after use. »",
     "« AVERTISSEMENT : ne pas utiliser apres la date de peremption. Conserver dans un lieu sec, a l'abri de la lumiere directe du soleil. Appliquer en couche mince et se laver les mains apres emploi. » Le titre WARNING indique une consigne importante. « Do not use after » est une interdiction liée a la date de peremption. « Store in a dry place » impose une condition de conservation. « Apply thinly » precise la quantite, et « wash your hands after use » rappelle l'hygiene des mains. Chaque information a une consequence pratique : verifier le produit, le ranger correctement, doser et se laver les mains. On ne traduit pas « thinly » par « rapidement » : le mot signifie en fine couche.",
     "On attend la traduction des quatre consignes et l'explication de leur portee pratique."),
 QT("Décrire la méthode de lecture d'un protocole de soin en anglais que l'on ne maîtrise pas entièrement.",
     "On identifie d'abord le titre et l'objet du document pour verifier qu'il concerne bien le produit et la situation. On repere ensuite les termes de sécurité en majuscules : warning, caution, do not. On lit les étapes numérotees dans l'ordre, en soulignant les verbes a l'imperatif et les complements de temps ou de quantite. On releve les unites, les concentrations, la date de peremption et le numero de lot. Les mots inconnus sont recherches dans un dictionnaire professionnel ou verifies aupres d'un collegue, sans deviner. On reformule le protocole en français avec ses propres mots, puis on le fait confirmer par l'infirmier avant toute application. On ne commence jamais un geste sur la personne dans le doute. Enfin, on conserve le document et on signale toute etape incomprehensible.",
     "On attend identification du document, repérage des avertissements, reformulation et confirmation.")],
C("Lire un protocole en anglais, c'est repérer les avertissements, les étapes et les unités avant toute application.",
  "WARNING > CAUTION > DO NOT · before / after use",
  "expiry date · batch number · unités ml, mg, %",
  "Avertissement~Consigne de sécurité~Étape~Action numérotée~Interdiction~Do not~Conservation~Stockage du produit~Péremption~Date limite",
  "Identifier le document~Repérer les avertissements~Lire les étapes~Vérifier les unités~Faire confirmer",
  "Deviner le sens d'un mot|Appliquer un protocole douteux|Confondre warning et caution|Oublier la date de péremption",
  "Warning~Danger sérieux~Caution~Attention~Do not~Interdiction~Expiry date~Péremption~Batch number~Numéro de lot~Apply~Appliquer",
  "Warning~Risque élevé~Caution~Risque moindre",
  "Before use~Avant emploi~After use~Après emploi"))

# ============================================================ LA3
add("LA3", "L'espagnol pour l'accueil des personnes", "Langues", ["2nde pro"],
S("L'espagnol est utile dans de nombreux etablissements francais pour accueillir des personnes hispanophones."
  "|Les formules de politesse de base sont « buenos días », « buenas tardes » et « por favor »."
  "|« ¿Cómo está usted ? » demande des nouvelles de maniere respectueuse."
  "|« ¿Cómo te llamas ? » demande le prenom de maniere familiere."
  "|Le verbe « estar » exprime un etat momentane : « estoy bien », tandis que « ser » exprime une qualite durable."
  "|« Tengo dolor » signifie « j'ai mal » ; on peut preciser la zone avec « aquí »."
  "|Les noms de base sont : agua, comida, cama, baño, médico et enfermera."
  "|« ¿Necesita ayuda ? » propose de l'aide ; « sí, por favor » accepte poliment."
  "|Les nombres et les heures se declinent : « las ocho » pour huit heures."
  "|La prononciation de la « ñ » et de la « j » differencie plusieurs mots."
  "|Un accueil en espagnol, meme simple, rassure la personne et facilite la relation."
  "|Si la comprehension reste incomplete, on fait appel a un collegue ou a un service de traduction."),
[QC("Que signifie « buenos días » ?", "Bonsoir~Bonjour~Merci~Au revoir", 1,
     "« Buenos días » est le salut du matin et de la journee."),
 QC("Comment demander poliment des nouvelles ?", "¿Cómo te llamas ?~¿Cómo está usted ?~¿Qué hora es?~¿Dónde está?", 1,
     "« ¿Cómo está usted ? » utilise le registre respectueux « usted »."),
 QC("Quel verbe exprime un état momentané ?", "Ser~Estar~Tener~Ir", 1,
     "Estar exprime un etat temporaire, ser une qualite durable."),
 QC("Que signifie « tengo dolor » ?", "J'ai faim~J'ai mal~J'ai froid~J'ai le temps", 1,
     "« Tengo dolor » signifie « j'ai mal »."),
 QC("Quel mot désigne l'eau ?", "Comida~Agua~Cama~Baño", 1,
     "Agua signifie eau."),
 QC("Comment proposer de l'aide ?", "¿Necesita ayuda ?~¿Está bien?~¿Qué tal?~¿Cuánto cuesta?", 0,
     "« ¿Necesita ayuda ? » signifie « avez-vous besoin d'aide ? »."),
 QC("Quelle est la forme familière pour demander le prénom ?", "¿Cómo está usted ?~¿Cómo te llamas ?~¿Qué desea?~¿Dónde vive?", 1,
     "« ¿Cómo te llamas ? » emploie le tutoiement.")],
[QT("Rédiger un court dialogue d'accueil en espagnol pour une personne qui arrive dans un service.",
     "Professionnel : « Buenos días. ¿Cómo está usted? » Personne : « Estoy un poco cansada. » Professionnel : « ¿Necesita ayuda? » Personne : « Sí, por favor. Tengo dolor aquí. » Professionnel : « Entiendo. Voy a avisar a la enfermera. ¿Quiere agua? » Personne : « Sí, gracias. » Le dialogue utilise des formules polies, le verbe estar pour l'etat present, la designation d'une douleur avec « aquí » et la proposition d'aide. Il reste simple et respectueux. On evite le tutoiement avec une personne agee que l'on ne connait pas, et on fait appel a un collegue si la personne exprime quelque chose que l'on ne comprend pas.",
     "On attend salutation, question sur l'etat, proposition d'aide, douleur et orientation vers un professionnel."),
 QT("Expliquer l'intérêt d'utiliser quelques mots d'espagnol même lorsque l'on ne parle pas couramment la langue.",
     "Quelques mots simples — bonjour, comment allez-vous, avez-vous besoin d'aide, merci — suffisent souvent a montrer que l'on est attentif a la personne et a son origine. Cela reduce le sentiment d'etrangete et installe un climat de confiance. L'effort porte sur la relation plus que sur la grammaire : une prononciation approximative mais respectueuse est mieux acceptee qu'un silence complet. Cela dit, il ne faut pas surestimer ses competences : pour une information medicale ou une decision importante, on fait appel a un professionnel bilingue ou a un service de traduction, afin d'eviter un malentendu. On peut aussi utiliser des supports visuels et des gestes pour completer les mots.",
     "On attend effet sur la relation, limites et recours à un interprète pour les informations importantes.")],
C("Quelques mots d'espagnol bien choisis humanisent l'accueil ; les informations importantes exigent un interlocuteur compétent.",
  "buenos días · ¿cómo está usted? · ¿necesita ayuda?",
  "estar = état momentané · ser = qualité durable",
  "Salutation~Buenos días~Politesse~Por favor y gracias~État~Estar~Douleur~Tengo dolor~Aide~¿Necesita ayuda?",
  "Saluer~Demander des nouvelles~Proposer de l'aide~Nommer le besoin~Orienter vers le professionnel",
  "Tutoyer une personne âgée|Traduire une information médicale soi-même|Surestimer son niveau|Se taire par timidité",
  "Buenos días~Bonjour~Por favor~S'il vous plaît~Agua~Eau~Enfermera~Infirmière~Aquí~Ici~Gracias~Merci",
  "Estar~État momentané~Ser~Qualité durable",
  "Usted~Vous respectueux~Tú~Tu familier"))

# ============================================================ LA4
add("LA4", "Communiquer avec une personne allophone", "Langues", ["Terminale pro"],
S("Une personne allophone parle une langue differante de celle du service et ne maitrise pas le francais."
  "|La barriere linguistique peutToucher la comprehension des consignes, l'expression de la douleur et les relations sociales."
  "|Le premier réflexe est de verifier les besoins de communication : langue, niveau, lecture et ecriture."
  "|Un interlocuteur bilingue ou un interprète professionnel est preferable a un proche pour les informations medicales."
  "|Recourir a l'enfant ou au conjoint comme interprète pose un probleme de confidentialite et de neutralite."
  "|Les supports visuels — images, pictogrammes, objets — facilitent la comprehension."
  "|La parole doit etre lente, claire et accompagnee de gestes, sans crier."
  "|Les phrases courtes et un seul message a la fois limitent les malentendus."
  "|La confirmation par reformulation ou par demonstration est indispensable avant de conclure."
  "|Certains etablissements disposent de fiches de communication traduites ou de services de teleinterpretation."
  "|La personne doit etre informee de l'utilisation d'un outil de traduction, notamment pour les donnees de sante."
  "|L'objectif n'est pas seulement de comprendre les mots, mais de prevenir l'isolement et de respecter la dignite."),
[QC("Quel interlocuteur est préférable pour une information médicale ?", "Un enfant de la famille~Un interprète professionnel~Un voisin~Le conjoint", 1,
     "L'interprete professionnel garantit la confidentialite et la neutralite."),
 QC("Pourquoi éviter un proche comme interprète ?", "Il parle trop vite~Il peut être gêné et ne pas être neutre~Il ne connaît pas la personne~Il est trop âgé", 1,
     "Le proche est implique emotionnellement et peut filtrer l'information."),
 QC("Quel support facilite la compréhension ?", "Un texte long~Des pictogrammes et des objets~Une consigne orale rapide~Un jargon professionnel", 1,
     "Les supports visuels sont comprehensibles sans maitrise de la langue."),
 QC("Comment parler à une personne qui ne comprend pas ?", "Crier fort~Parler lentement avec des phrases courtes~Répéter le même long discours~Ne rien dire", 1,
     "On ralentit et on fragmente le message, sans elever le ton inutilement."),
 QC("Que faut-il faire après une explication ?", "Partir immédiatement~Vérifier la compréhension~Changer de sujet~Écrire une lettre", 1,
     "La reformulation ou la demonstration confirment la comprehension."),
 QC("Quel service peut aider ?", "Une téléinterprétation~Un service de livraison~Une agence de voyage~Un bureau de change", 0,
     "La teleinterpretation permet d'acceder a un interprete a distance."),
 QC("Quel est l'objectif principal de la communication ?", "Parler vite~Comprendre et éviter l'isolement~Utiliser beaucoup de mots~Éviter les gestes", 1,
     "L'enjeu est la comprehension et le maintien du lien social.")],
[QT("Décrire la conduite à tenir pour expliquer un soin à une personne qui ne parle pas français.",
     "On evalue d'abord ses besoins : langue maternelle, niveau de comprehension, lecture et ecriture. On cherche un interlocuteur adapte : un collegue bilingue pour une information simple, un interprete professionnel ou la teleinterpretation pour une information medicale. On prepare des supports visuels : images du geste, objets utilises, pictogrammes. On se place face a la personne, on parle lentement avec une phrase courte a la fois, en accompagnant la parole d'un geste corresponding. On montre le materiel avant de l'utiliser. On verifie la comprehension en demandant une demonstration ou un signe simple, pas seulement un « oui » reflexe. On respecte un refus ou une hesitation. On note dans le dossier les modalites de communication qui ont fonctionne, afin que l'equipe les reutilise. Enfin, on reste attentif au risque d'isolement et on favorise les moments de contact avec les autres.",
     "On attend évaluation des besoins, interprète adapté, supports, vérification et traçabilité."),
 QT("Expliquer pourquoi le recours à un proche comme interprète est problématique dans un contexte de soin.",
     "Le proche n'est pas neutre : il peut attenuer une information difficile, la reformuler selon ses propres representations, ou eviter d'aborder un sujet delicat devant la personne. La confidentialite est aussi en cause : la personne peut ne pas souhaiter que sa famille connaisse certains elements de sa sante ou de sa vie. Le proche peut etre affectivement implique et avoir du mal a traduire fidèlement des propos douloureux. Enfin, il n'a pas les competences pour rendre des termes medicaux avec precision. Pour ces raisons, on prefere un interprete professionnel, lie par une obligation de confidentialite et forme a la neutralite. Le proche reste bienvenu comme accompagnant, mais pas comme unique canal d'information medicale.",
     "On attend neutralite, confidentialite, fidélité et distinction entre accompagnement et interprétation.")],
C("Communiquer avec une personne allophone demande des supports, un interprète adapté et une vérification systématique.",
  "langue + niveau + lecture + écriture = besoins de communication",
  "interprète professionnel > proche pour les informations médicales",
  "Allophone~Autre langue~Barrière linguistique~Compréhension limitée~Interprète~Médiation professionnelle~Supports~Images et pictogrammes~Vérification~Reformulation~Neutralité~Qualité requise",
  "Évaluer les besoins~Choisir l'interlocuteur~Préparer les supports~Parler lentement~Vérifier et tracer",
  "Crier pour être compris|Utiliser l'enfant comme interprète|Supposer que le oui signifie compris|Ignorer le risque d'isolement",
  "Téléinterprétation~Outil à distance~Pictogramme~Support visuel~Geste~Accompagnement du message~Dossier~Modalités notées~Neutralité~Interprète professionnel",
  "Interprète professionnel~Neutre et confidentiel~Proche~Impliqué émotionnellement",
  "Compréhension~Message reçu~Isolation~Risque à prévenir"))

# ============================================================ DD1
add("DD1", "L'éco-responsabilité dans les soins et le bionettoyage", "Développement durable", ["1re pro"],
S("L'éco-responsabilité consiste a reduire l'impact environnemental des activites quotidiennes."
  "|Dans un etablissement de soins, elle concerne l'eau, l'energie, les produits, les dechets et les achats."
  "|Le secteur de la sante consomme beaucoup de ressources et produit des dechets specifiques."
  "|Le principe est de rationaliser l'usage sans reduire la qualite de l'hygiene et de la securite."
  "|Les produits dilues correctement evitent le gaspillage et limitent les rejets chimiques."
  "|Le dosage doit respecter les recommandations du fabricant : une dose excessive n'ameliore pas la desinfection."
  "|Le bionettoyage peut utiliser des microfibres lavables et des systems de dilution automatises."
  "|L'usage unique reste necessaire pour certains gestes a risque infectieux : la securite prime."
  "|L'eau est une ressource precieuse : on ferme les robinets et on evite les ecoulements inutiles."
  "|Le chauffage et la climatisation sont regles selon les besoins reels des personnes."
  "|Les achats responsables privilégient la durabilite, la reparabilite et des fournisseurs locaux."
  "|Chaque professionnel peut proposer une action d'eco-responsabilite dans son service."),
[QC("Quel principe guide l'éco-responsabilité en milieu de soin ?", "Réduire les coûts sans égard pour l'hygiène~Réduire l'impact sans nuire à la sécurité~Supprimer tout nettoyage~N'acheter que du neuf", 1,
     "L'objectif est de concilier environnement, qualite et securite."),
 QC("Que faut-il faire avec un produit désinfectant ?", "Surdoser pour être sûr~Respecter le dosage recommandé~Le diluer à l'eau claire sans mesure~Le mélanger à un autre produit", 1,
     "Le surdosage gaspille et peut être nocif, sans gagner en efficacite."),
 QC("Quel usage unique est justifié ?", "Un essuyage de table~Un geste à risque infectieux~Un arrosage~Un rangement", 1,
     "La securite infectieuse prime sur l'eco-responsabilite dans ce cas."),
 QC("Comment economiser l'eau ?", "Laisser couler le robinet~Fermer le robinet et éviter les écoulements inutiles~Utiliser l'eau chaude en permanence~Rincer longuement", 1,
     "Les gestes simples sur les robinets reduisent la consommation."),
 QC("Quel critère d'un achat responsable ?", "Le prix le plus bas seulement~La durabilité et la réparabilité~La couleur du produit~L'emballage le plus grand", 1,
     "Un produit durable et reparable limite les dechets a long terme."),
 QC("Que sont les microfibres lavables ?", "Des chiffons à usage unique~Des chiffons réutilisables après lavage~Des produits chimiques~Des gants spéciaux", 1,
     "Les microfibres lavables réduisent les dechets d'essuyage."),
 QC("Qui peut proposer une action d'éco-responsabilité ?", "La direction seulement~Chaque professionnel du service~Le fournisseur seulement~Personne", 1,
     "Les initiatives locales sont encouragees a tous les niveaux.")],
[QT("Expliquer comment concilier l'éco-responsabilité et l'hygiène dans une chambre de soins.",
     "On commence par appliquer la procedure de bionettoyage, qui fixe les gestes indispensables a la securite : nettoyer, desinfecter, respecter le temps de contact. On optimise ensuite les quantites : dosage exact des produits, chiffons microfibres lavables pour les surfaces non critiques, usage unique reserve aux situations a risque infectieux. On evite de multiplier les produits et on verifie leur compatibilite. On ferme le robinet pendant le remplissage et on utilise l'eau froide ou tiede quand c'est possible. On trie les dechets selon les filieres de l'etablissement et on signale les anomalies d'approvisionnement. On ne supprime jamais une etape d'hygiene pour economiser. Enfin, on propose a l'equipe des ajustements simples et on evalue leur effet sur la consommation et sur la qualite du nettoyage.",
     "On attend priorite a la securite, dosage, materiaux reutilisables et propositions d'amelioration."),
 QT("Quels critères utiliser pour choisir un produit de bionettoyage plus responsable ?",
     "On vérifie d'abord l'efficacite prouvee du produit sur les micro-organismes vises : c'est le critere prioritaire en milieu de soin. On regarde ensuite sa composition, la presence d'emballages excessifs, les consignes de dosage et les conditions d'elimination. On prefere un conditionnement concentre ou un systeme de dilution qui reduit les dechets d'emballage. On considere la duree de vie, la possibilite de recharge et la proximite du fournisseur, qui limite les transports. On consulte l'avis de l'equipe hygiene et du responsable achats, car le choix engage la securite de tous. Enfin, on teste le produit sur une petite periode et on compare les resultats de nettoyage avant de generaliser son usage.",
     "On attend efficacite prioritaire, emballage, dosage, transport et validation par l'equipe.")],
C("L'éco-responsabilité optimise les ressources sans jamais sacrifier la sécurité des soins.",
  "qualité de l'hygiène > économie d'étape · dosage exact · usage unique ciblé",
  "eau · énergie · produits · déchets · achats durables",
  "Éco-responsabilité~Impact environnemental~Bionettoyage~Procédure d'hygiène~Dosage~Quantité exacte~Microfibres~Chiffons lavables~Sécurité~Priorité aux soins",
  "Appliquer la procédure~Doser exactement~Choisir le matériel adapté~Trier les déchets~Proposer des améliorations",
  "Supprimer une étape d'hygiène|Surdoser un produit|Mélanger des produits incompatibles|Ignorer le tri des déchets",
  "Dosage~Économie et efficacité~Usage unique~Risque infectieux~Robinet~Consommation d'eau~Recharge~Moins d'emballage~Fournisseur local~Transport réduit",
  "Usage unique~Sécurité infectieuse~Réutilisable~Moins de déchets",
  "Économie~Moins de ressources~Hygiène~Priorité non négociable"))

# ============================================================ DD2
add("DD2", "La gestion des déchets et le tri en établissement", "Développement durable", ["2nde pro"],
S("Un etablissement de soins produit des dechets varies qui necessitent une gestion specifique."
  "|On distingue les dechets assimilables aux ordures menageres, les dechets recyclables et les dechets d'activites de soins."
  "|Les dechets d'activites de soins a risques infectieux sont appeles DASRI."
  "|Les DASRI comprennent les objets piquants ou coupants, les pansements souilles et les dechets contaminés."
  "|Ils sont collectes dans des contenants adaptes : boites a aiguilles, sacs ou futs specifiques."
  "|Ces contenants ne doivent jamais etre remplis au-dela de la limite indiquee et doivent etre fermes et etiquetes."
  "|Un circuit de collecte separe evite le melange avec les dechets ordinaires."
  "|Les entreprises specialisees assurent le transport et le traitement des DASRI."
  "|Une trace de l'enlevement est conservee : c'est le bordereau de suivi."
  "|Les dechets ordinaires sont tries selon les consignes locales : papier, plastique, verre, organique."
  "|Le tri correct reduit les couts de traitement et limite l'impact environnemental."
  "|Une erreur de tri peut exposer le personnel a un risque de blessure ou de contamination."),
[QC("Qu'appelle-t-on DASRI ?", "Des déchets ménagers~Des déchets d'activités de soins à risques infectieux~Des déchets de papier~Des déchets de cuisine", 1,
     "Les DASRI sont les dechets de soins presentant un risque infectieux."),
 QC("Quel contenant est adapté aux aiguilles ?", "Un sac plastique~Une boîte à aiguilles~Une poubelle ordinaire~Un carton ouvert", 1,
     "Les objets piquants vont dans une boite securee et etanche."),
 QC("Que faut-il faire avec un contenant de DASRI plein ?", "Le remplir davantage~Le fermer et le faire enlever selon la procédure~Le vider dans la poubelle~Le laisser ouvert", 1,
     "Le contenant est ferme, etiquete et collecte par une filiere adaptee."),
 QC("Quel document suit l'enlèvement des DASRI ?", "Une facture de repas~Un bordereau de suivi~Un contrat de travail~Une ordonnance", 1,
     "Le bordereau de suivi trace la collecte et le traitement."),
 QC("Quel risque présente une erreur de tri ?", "Une blessure ou une contamination~Une réduction des déchets~Une économie d'énergie~Aucun risque", 0,
     "Le melange avec les ordures expose le personnel et l'environnement."),
 QC("Quels déchets sont recyclables ?", "Les aiguilles~Le papier et le plastique propres~Les pansements souillés~Les liquides biologiques", 1,
     "Les dechets recyclables sont propres et separes des dechets de soins."),
 QC("À quoi sert le tri ?", "À augmenter les déchets~À réduire les coûts et l'impact environnemental~À compliquer le travail~À supprimer les collectes", 1,
     "Le tri optimise le traitement et reduit l'impact environnemental.")],
[QT("Décrire les étapes de la gestion d'un déchet piquant utilisé lors d'un soin.",
     "Des que l'aiguille est utilisee, on ne la recapuchonne pas et on ne la manipule pas a mains nues. On la depose immediatement dans une boite a aiguilles adaptee, placee a proximite du geste, sans la depasser au-dela du trait de remplissage. On referme le couvercle selon le systeme de securite. Lorsque la boite est pleine, on la ferme definitivement, on verifie l'etiquetage avec la date et le service, puis on la place dans le local de stockage des DASRI prevu a cet effet. L'enlevement est assure par une entreprise agre e, et le bordereau de suivi est conserve par l'etablissement. On se lave les mains apres la manipulation et on signale tout incident de piqûre selon la procedure.",
     "On attend dépôt immédiat, contenant adapté, limite de remplissage, collecte et traçabilité."),
 QT("Expliquer pourquoi les déchets de soins ne doivent jamais être mélangés aux ordures ménagères.",
     "Les dechets de soins peuvent contenir des agents pathogenes, du sang, des medicaments ou des objets tranchants. Melanges aux ordures menageres, ils exposent les agents de collecte a des piqures et a des contaminations, et peuvent contaminer les autres dechets. Le traitement des ordures menageres n'est pas adapte : il peut dissoudre des medicaments dans les eaux ou disperser des substances dangereuses. La reglementation impose donc une filiere separee, avec des contenants normalises, un transport par un operateur agree et une trace ecrite. Pour l'accompagnant, la regle est simple : des le doute sur la nature d'un dechet, on le classe dans la filiere de soins et on demande confirmation. Une erreur de tri n'est pas un detail administratif, mais un risque pour la sante publique.",
     "On attend risques pour les personnels, traitement inadapte, obligation reglementaire et prudence.")],
C("La gestion des déchets protège les professionnels et l'environnement : la filière du risque infectieux est strictement séparée.",
  "DASRI = déchets d'activités de soins à risques infectieux",
  "boîte à aiguilles · contenant fermé et étiqueté · bordereau de suivi",
  "DASRI~Déchet à risque infectieux~Contenant~Boîte ou fût adapté~Collecte~Filière séparée~Bordereau~Trace de l'enlèvement~Tri~Sélection par type~Recyclage~Filière de valorisation",
  "Identifier le type de déchet~Utiliser le bon contenant~Fermer sans dépasser la limite~Ranger dans le local~Vérifier la traçabilité",
  "Recapuchonner une aiguille|Dépasser la limite de remplissage|Mélanger les filières|Oublier le bordereau",
  "Boîte à aiguilles~Contenant sécurisé~Pansement souillé~DASRI~Papier~Recyclable~Bordereau~Preuve de collecte~Opérateur agréé~Transport spécialisé",
  "DASRI~Risque infectieux~Ordures ménagères~Déchets ordinaires",
  "Tri~Séparer les flux~Mélange~Risque et coût accru"))

# ============================================================ DD3
add("DD3", "Économie d'énergie et d'eau au quotidien", "Développement durable", ["1re pro"],
S("L'énergie et l'eau sont des ressources consommees en continu dans un etablissement de soins."
  "|Le chauffage, l'eau chaude, l'eclairage, la climatisation et les appareils medicaux representent l'essentiel des usages."
  "|Une consommation excessive augmente les couts et les emissions de gaz a effet de serre."
  "|Le réglage du chauffage doit tenir compte du confort des personnes, en particulier des personnes agees."
  "|Une temperature trop basse favorise les chutes de la thermoregulation et les infections."
  "|L'éclairage peut être limite dans les zones non occupees, sans jamais priver une personne de lumiere utile."
  "|Les robinets a fermeture automatique et les douchettes economes reduisent la consommation d'eau."
  "|Une fuite, meme faible, represente un gaspillage important sur une annee."
  "|Les appareils en veille consomment de l'electricite : on les eteint quand c'est possible."
  "|Le linge peut etre lave a temperature adaptée avec des charges pleines pour optimiser les cycles."
  "|Les donnees de consommation sont relevees et comparees pour detecter les derives."
  "|Chaque geste individuel a un effet collectif lorsqu'il est repete par toute l'equipe."),
[QC("Quel usage consomme le plus d'énergie dans un établissement ?", "L'eclairage de nuit~Le chauffage et l'eau chaude~Les ordinateurs~Les téléphones", 1,
     "Le chauffage et la production d'eau chaude sont les principaux postes."),
 QC("Quel est un risque d'un chauffage trop bas ?", "Une surconsommation~Une baisse de la thermoregulation chez la personne âgée~Une panne de courant~Une odeur de produit", 1,
     "Le froid peut fragiliser les personnes agees et augmenter le risque infectieux."),
 QC("Que faut-il faire face à une fuite d'eau ?", "L'ignorer~La signaler rapidement~La boucher soi-même avec du ruban~Attendre la fin du mois", 1,
     "Une fuite doit etre signalee au service technique."),
 QC("Quel équipement réduit la consommation d'eau ?", "Un robinet toujours ouvert~Une douchette économe~Un robinet à fermeture lente~Un tuyau percé", 1,
     "Les douchettes economes et les fermetures automatiques limitent le debit."),
 QC("Que faire des appareils en veille ?", "Les laisser allumés~Les éteindre lorsque c'est possible~Les débrancher pendant les soins~Les remplacer chaque mois", 1,
     "La veille consomme de l'electricite inutilement."),
 QC("Comment optimiser la lessive ?", "Laver à pleine charge avec une température adaptée~Laver à moitié vide~Toujours à 90 °C~Sans trier le linge", 0,
     "Les charges pleines et une temperature adaptee reduisent l'energie par kilo."),
 QC("À quoi servent les relevés de consommation ?", "À augmenter les factures~À détecter les dérives et à suivre les actions~À supprimer les compteurs~À changer de fournisseur chaque mois", 1,
     "Les donnees permettent de piloter et de verifier les economies.")],
[QT("Expliquer comment réduire la consommation d'eau chaude pendant la toilette sans nuire au confort.",
     "On utilise une douchette a faible debit et on evite de laisser l'eau couler pendant le savonnage : on ouvre pour mouiller, on ferme pendant le lavage, on rouvre pour rincer. On regle la temperature avec le thermometre ou le coude plutot que de faire couler jusqu'a obtenir l'eau chaude. On prepare le materiel avant d'ouvrir l'eau pour eviter les attentes. On limite la duree de la douche tout en respectant le rythme de la personne et son confort : l'objectif n'est pas de presser le soin. On signale une douchette defectueuse ou une fuite au service technique. On peut aussi utiliser des lingettes ou un lavage au gant lorsque la situation clinique le permet et que le protocole l'autorise. Enfin, on note les gestes efficaces pour les partager avec l'equipe.",
     "On attend gestion du robinet, matériel adapté, confort préservé et signalement des fuites."),
 QT("Comment sensibiliser une équipe à l'économie d'énergie sans réduire la qualité de l'accompagnement ?",
     "On part des donnees : releves de consommation et couts, presentes simplement a l'equipe. On identifie ensemble les gestes possibles : eteindre les lumieres dans les zones vides, regler le chauffage sans refroidir les chambres, fermer les portes, eteindre les appareils inutiles, optimiser les cycles de lavage. On explique le lien entre confort des personnes et maitrise : le confort reste prioritaire, notamment pour les residents agees. On propose une action test sur une semaine avec un indicateur simple, puis on observe les resultats et on partage les reussites. On evite le discours moralisateur : chacun peut proposer une idee et l'equipe decide collectivement. On trace les actions retenues dans le projet d'etablissement ou le plan d'amelioration continue.",
     "On donne des données, des gestes concrets, une méthode collective et le primat du confort.")],
C("Économiser l'énergie et l'eau, c'est optimiser les usages tout en préservant le confort et la sécurité des personnes.",
  "chauffage et eau chaude = principaux postes de consommation",
  "robinet fermé · douchette économe · charge pleine · veille éteinte",
  "Énergie~Chauffage et électricité~Eau~Ressource utilisée~Consommation~Volume mesuré~Fuite~Gaspillage à signaler~Confort~Priorité pour la personne~Relevé~Suivi des données",
  "Observer les usages~Repérer les gaspillages~Adopter un geste économe~Préserver le confort~Suivre les consommations",
  "Refroidir une chambre pour économiser|Laisser une fuite sans signalement|Presser la toilette|Tout éteindre sans réfléchir",
  "Douchette~Débit réduit~Thermomètre~Température vérifiée~Pleine charge~Lessive optimisée~Veille~Consommation cachée~Relevé~Pilotage",
  "Économie~Réduction des usages~Gaspillage~Consommation inutile",
  "Confort~Bien-être de la personne~Économie~Objectif secondaire"))

# ============================================================ DD4
add("DD4", "Développement durable et santé environnementale", "Développement durable", ["Terminale pro"],
S("Le developpement durable vise a repondre aux besoins presents sans compromettre la capacite des generations futures."
  "|Il articule trois dimensions : environnementale, sociale et economique."
  "|La sante environnementale etudie l'influence du milieu sur la sante des personnes."
  "|Les polluants de l'air interieur — tabac, produits menagers, moisissures — peuvent aggraver des maladies respiratoires."
  "|Le bruit, la lumiere et la temperature sont des facteurs de confort et de sante."
  "|Une mauvaise qualite de l'air peut favoriser les allergies, l'asthme et les infections."
  "|Le principe de precaution invite a reduire l'exposition aux substances potentiellement nocives."
  "|Les produits de nettoyage doivent etre choisis pour leur efficacite et leur faible impact."
  "|La gestion des dechets et l'economie de ressources contribuent a la qualite de l'environnement de soin."
  "|L'education a la sante peut inclure des informations sur l'environnement et les comportements a adopter."
  "|Les collectivites et les etablissements mettent en place des plans d'action :air, bruit, dechets, energie."
  "|L'accompagnant observe les conditions de vie quotidiennes et signale les situations qui portent atteinte a la sante."),
[QC("Quelles sont les trois dimensions du développement durable ?", "Sociale, économique et environnementale~Politique, juridique et médicale~Technique, financière et commerciale~Individuelle, familiale et scolaire", 0,
     "Les trois piliers sont environnemental, social et economique."),
 QC("Quel polluant intérieur peut aggraver l'asthme ?", "Une plante~La fumée de tabac~Une lumière douce~Un livre", 1,
     "La fumee de tabac est un polluant majeur de l'air interieur."),
 QC("Quel facteur influence le confort d'une chambre ?", "Le nombre de portes~La lumière, le bruit et la température~La couleur du rideau~L'heure de la visite", 1,
     "Lumiere, bruit et temperature sont des determinants du confort."),
 QC("Que recommande le principe de précaution ?", "Attendre la preuve du danger~Réduire l'exposition aux substances potentiellement nocives~Interdire tous les produits~Ignorer les études", 1,
     "Le principe de precaution invite a agir avant la certitude complete."),
 QC("Quel est un objectif de la gestion des déchets ?", "Augmenter les volumes~Limiter l'impact environnemental~Supprimer les soins~Réduire le personnel", 1,
     "Une gestion adaptee reduit les risques et l'impact environnemental."),
 QC("Quel lien entre environnement et éducation à la santé ?", "Aucun~On peut informer sur les comportements qui protègent la santé et l'environnement~L'éducation ne concerne que la famille~Le sujet est interdit", 1,
     "L'education a la sante peut integrer les determinants environnementaux."),
 QC("Que fait l'accompagnant face à une situation nuisible ?", "Rien~Il observe et signale selon la procédure~Il répare lui-même~Il en parle aux seuls résidents", 1,
     "Son rôle est d'observer et d'alerter les services competents.")],
[QT("Expliquer comment la qualité de l'environnement intérieur influence la santé des personnes accompagnées.",
     "L'air interieur d'une chambre peut contenir des polluants : fumee de tabac, produits de nettoyage, poussieres, moisissures. Chez une personne agee ou asthmatique, ces substances peuvent provoquer une toux, une gêne respiratoire ou une crise. Le bruit excessif perturbe le sommeil et augmente l'agitation des personnes presentant des troubles cognitifs. Une lumiere insuffisante favorise les chutes, tandis qu'un eclairage trop brutal peut eblouir. Une temperature trop basse ou trop haute modifie la thermoregulation et le confort. L'accompagnant contribue a la qualite de cet environnement en aérant la chambre, en evitant les melanges de produits, en signalant une odeur de moisissure ou une fuite et en respectant les regles de tabagisme de l'etablissement. Il transmet ses observations a l'equipe.",
     "On attend polluants, effets sur la sante et actions quotidiennes de l'accompagnant."),
 QT("Comment intégrer le développement durable dans une action d'éducation à la santé sur l'hygiène ?",
     "On peut presenter le lavage des mains en montrant a la fois son interet pour la sante et les gestes qui economisent l'eau : ouvrir et fermer le robinet au bon moment, utiliser une solution hydro-alcoolique quand c'est pertinent. On explique le tri des dechets de soins et la difference entre dechets ordinaires et DASRI, en insistant sur la securite. On propose aux residents une activite de fabrication de produits d'entretien simples ou une discussion sur les odeurs et la qualite de l'air. On utilise des supports reutilisables plutot que des flyers a usage unique. Les objectifs restent mesurables : savoir citer deux gestes d'hygiene et deux gestes eco-responsables. On evalue la comprehension par une demonstration et on recueille l'avis des participants. L'action respecte le projet d'etablissement et les regles d'hygiene, qui restent prioritaires.",
     "On attend articulation sante et environnement, supports durables et evaluation.")],
C("La santé environnementale relie la qualité du milieu au bien-être des personnes ; le développement durable guide les choix quotidiens.",
  "environnemental + social + économique = développement durable",
  "qualité de l'air · bruit · lumière · température · principe de précaution",
  "Développement durable~Trois piliers~Santé environnementale~Influence du milieu~Air intérieur~Polluants~Confort~Bruit et lumière~Précaution~Réduction de l'exposition~Qualité de vie~Objectif final",
  "Observer l'environnement~Identifier les sources de nuisance~Agir sur ce qui est possible~Signaler à l'équipe~Éduquer sans culpabiliser",
  "Confondre les trois piliers|Mélanger des produits de nettoyage|Ignorer une odeur de moisissure|Sacrifier la sécurité à l'économie",
  "Tabac~Polluant intérieur~Moisissure~Risque respiratoire~Aération~Geste simple~Tri~Gestion des déchets~Support réutilisable~Moins de déchets",
  "Environnement~Milieu de vie~Santé~État de la personne",
  "Précaution~Agir avant la certitude~Certitude~Preuve complète"))

# FIN DES LOTS
valider_et_ecrire(F, "pro-sante-mat-part-C.json")
