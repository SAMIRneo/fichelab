# -*- coding: utf-8 -*-
"""Generateur pro-electricite-mat-part-C.json — lot C : enseignements professionnels (20 fiches).

Pratique professionnelle (8), Économie et gestion (3), Droit (3),
Anglais technique (3), Développement durable (3). Chaque fiche : 12 points,
9 questions (7 QCM + 2 texte), 7 blocs en ordre strict et 3 schemas.
Annees : 2nde pro, 1re pro, Terminale pro.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pro_electricite_common import REF, S, R, QC, QT, C, build, valider_et_ecrire

F = []


def add(prefix, titre, mat, ans, points, questions, c):
    F.append(build(prefix, titre, mat, ans, points, questions, c))


# ============================================================ PR1
add("PE-C01", "Sécurité électrique : risques et barrières", "Pratique professionnelle", ["1re pro"],
    S("La sécurité électrique vise à protéger les personnes contre les risques liés au courant."
      "|Le risque électrique apparaît dès que le corps devient une partie d'un circuit fermé."
      "|Le courant traversant le corps peut provoquer des brûlures, des contractions musculaires ou une fibrillation cardiaque."
      "|La gravité dépend de l'intensité, de la tension, de la durée et du trajet du courant dans le corps."
      "|Le courant alternatif à 50 Hz est particulièrement dangereux pour le cœur."
      "|Un contact direct correspond au contact d'une partie active normalement sous tension."
      "|Un contact indirect résulte d'un défaut d'isolement qui met sous tension une masse accessible."
      "|Les parties actives sont protégées par des enveloppes, des barrières ou des obstacles."
      "|La mise à la terre et le disjoncteur différentiel sont les deux barrières essentielles contre les contacts indirects."
      "|Une installation doit être conçue et vérifiée conformément à la norme NF C 15-100."
      "|Avant toute intervention, on applique la procédure de consignation et de vérification d'absence de tension."
      "|La formation et le respect des consignes comptent autant que les équipements de protection."),
    [QC("Quand le risque électrique apparaît-il ?", "Quand le corps fait partie d'un circuit fermé~Quand la lampe est éteinte~Quand le câble est neuf~Quand la tension est nulle", 0,
        "Le danger apparaît dès que le corps est traversé par un courant."),
     QC("Quel effet du courant sur le corps est le plus grave ?", "Une brûlure légère~Une fibrillation cardiaque~Un simple picotement~Une fatigue passagère", 1,
        "La fibrillation ventriculaire est l'effet le plus dangereux du courant alternatif."),
     QC("Qu'appelle-t-on un contact indirect ?", "Le contact d'un fil sous tension~La mise sous tension d'une masse par défaut d'isolement~Un contact avec la terre~Une décharge statique sans danger", 1,
        "Le contact indirect met en jeu une masse normalement inaccessible devenue conductrice."),
     QC("Quelle protection agit contre les contacts indirects ?", "Une simple gaine isolante~La mise à la terre et le différentiel~Une résistance en série~Un interrupteur", 1,
        "La terre évacue le courant de défaut et le différentiel coupe l'alimentation."),
     QC("Pourquoi le 50 Hz est-il particulièrement dangereux ?", "Il chauffe moins~Il perturbe l'activité électrique du cœur~Il est inodore~Il augmente la résistance", 1,
        "Cette fréquence est proche de celle des signaux physiologiques cardiaques."),
     QC("Quelle norme régit les installations basse tension en France ?", "NF C 15-100~ISO 9001~NF EN 60617~NF S 31-100", 0,
        "La NF C 15-100 fixe les règles de sécurité des installations électriques."),
     QC("Que faut-il faire avant d'intervenir sur une installation ?", "La mettre sous tension pour tester~La consigner et vérifier l'absence de tension~Débrancher seulement la charge~Travailler à deux sans procédure", 1,
        "La consignation et la vérification d'absence de tension sont obligatoires."),
     QT("Expliquer la différence entre contact direct et contact indirect et donner une protection pour chacun.",
        "Le contact direct se produit lorsqu'une personne touche une partie active normalement sous tension, par exemple un conducteur dénudé. La protection repose sur les enveloppes isolantes, les coffrets fermés et les barrières. Le contact indirect se produit lorsqu'une masse métallique normalement sans tension devient conductrice à la suite d'un défaut d'isolement. La protection repose alors sur la mise à la terre de la masse et sur le disjoncteur différentiel qui coupe le courant de fuite. Dans les deux cas, la procédure de consignation protège le personnel qui intervient.",
        "On attend la distinction entre partie active et masse en défaut, avec les protections associées."),
     QT("Un technicien doit remplacer une prise dans une pièce humide. Décrire les précautions à prendre.",
        "Il consigne d'abord le circuit concerné et vérifie l'absence de tension avec un appareil adapté. Il porte des gants isolants et des chaussures de sécurité, et travaille si possible avec un autre technicien. La pièce humide exige un indice de protection adapté et un disjoncteur différentiel de 30 mA en amont. Il contrôle l'état des conducteurs, le repérage du neutre et du conducteur de protection, puis le serrage des bornes. Après remise en place, il vérifie l'absence de court-circuit, la continuité de la terre et le fonctionnement du différentiel avant de remettre sous tension.",
        "La réponse doit citer consignation, EPI, environnement humide, contrôle et remise en service.")],
    C("La sécurité électrique repose sur des barrières techniques et sur le respect strict des procédures.",
      "Contact direct = partie active · contact indirect = masse en défaut",
      "Terre + différentiel + consignation + formation",
      "Contact direct~Partie active touchée~Enveloppe isolante~Contact indirect~Masse sous tension par défaut~Terre et différentiel~Consignation~Hors tension contrôlée~Procédure écrite",
      "Identifier la situation de risque|Consigner et vérifier l'absence de tension|Choisir les protections adaptées|Porter les équipements requis|Contrôler avant remise en service",
      "Toucher un conducteur « pour voir »|Travailler sous tension sans autorisation|Oublier la vérification d'absence de tension|Négliger le différentiel",
      "50 Hz~Risque cardiaque~30 mA~Protection personnes~NF C 15-100~Règle d'installation~Terre~Évacuation du défaut",
      "Contact direct~Partie normalement sous tension~Gaine et coffret~Contact indirect~Masse devenue conductrice~Mise à la terre~Court-circuit~Courant très élevé~Disjoncteur",
      "Risque~Combinaison de danger et d'exposition~Danger~Source potentielle de dommage~Barrière~Moyen de protection"))

# ============================================================ PR2
add("PE-C02", "Consignation et mise hors tension", "Pratique professionnelle", ["Terminale pro"],
    S("La consignation met une installation hors tension et l'empêche d'être réalimentée pendant une intervention."
      "|Elle s'applique avant tout travail sur un circuit, un appareil ou une machine électrique."
      "|La première étape consiste à identifier précisément les circuits concernés sur les schémas."
      "|On coupe l'alimentation en ouvrant les dispositifs de coupure adaptés."
      "|On vérifie l'absence de tension avec un vérificateur de tension conforme et contrôlé."
      "|L'appareil de vérification est testé avant et après la mesure sur une source connue."
      "|On condamne les appareils de coupure en position ouverte avec un dispositif de condamnation."
      "|Des panneaux d'avertissement signalent qu'une intervention est en cours."
      "|Une mise à la terre et une mise en court-circuit sont ajoutées si le risque l'impose."
      "|Les opérations et les responsabilités sont consignées dans un document signé."
      "|La levée de consignation suit une procédure inverse et nécessite une autorisation."
      "|Une consignation incomplète figure parmi les causes principales des accidents électriques."),
    [QC("Quel est l'objectif de la consignation ?", "Augmenter la tension~Empêcher toute réalimentation pendant l'intervention~Remplacer le schéma~Tester la charge", 1,
        "La consignation garantit le maintien hors tension pendant le travail."),
     QC("Quelle est la première étape d'une consignation ?", "Couper directement~Identifier les circuits sur les schémas~Condamner~Signer", 1,
        "Il faut d'abord savoir exactement quel circuit est concerné."),
     QC("Avec quoi vérifie-t-on l'absence de tension ?", "Un tournevis~Un vérificateur de tension contrôlé~Une lampe~Un ohmmètre quelconque", 1,
        "Un vérificateur de tension adapté, contrôlé avant et après, est requis."),
     QC("Que fait-on des appareils de coupure après l'ouverture ?", "On les laisse libres~On les condamne en position ouverte~On les retire~On les verrouille fermés", 1,
        "La condamnation empêche une fermeture accidentelle."),
     QC("À quoi servent les panneaux d'avertissement ?", "À décorer l'armoire~À signaler l'intervention en cours~À remplacer la consignation~À indiquer la tension", 1,
        "Ils informent toute personne de l'interdiction de remettre sous tension."),
     QC("Qui autorise la levée de consignation ?", "N'importe qui~La personne habilitée responsable~Le fournisseur~Le voisin", 1,
        "Seul le responsable habilité peut prononcer la levée, après contrôle."),
     QC("Quand ajoute-t-on une mise à la terre et en court-circuit ?", "Toujours~Lorsque le risque l'impose~Jamais~Uniquement la nuit", 1,
        "Ces mesures complémentaires dépendent de l'analyse du risque."),
     QT("Décrire l'ordre des opérations d'une consignation complète.",
        "On identifie d'abord le circuit sur les schémas et on prévient les personnes concernées. On coupe l'alimentation en ouvrant les dispositifs de coupure. On vérifie l'absence de tension avec un vérificateur adapté, contrôlé avant et après sur une source connue. On condamne les appareils en position ouverte et on pose des panneaux d'avertissement. Si nécessaire, on réalise une mise à la terre et une mise en court-circuit. On consigne toutes ces opérations dans un document signé. À la fin des travaux, on retire les dispositifs, on contrôle l'installation puis on autorise la levée de consignation.",
        "On attend l'ordre : identification, coupure, vérification, condamnation, signalisation, documents et levée."),
     QT("Un collègue tente de refermer un disjoncteur condamné pendant votre intervention. Que faire ?",
        "On l'arrête immédiatement et on lui rappelle que le circuit est consigné et que toute remise sous tension est interdite. On vérifie que le dispositif de condamnation est toujours en place et que les panneaux d'avertissement sont visibles. On signale l'incident au responsable afin qu'il renforce l'information de l'équipe. On contrôle à nouveau l'absence de tension avant de poursuivre le travail, car une tentative de fermeture peut avoir modifié l'état du circuit. On consigne l'événement dans le document de suivi.",
        "La réponse doit inclure l'interruption, le contrôle de la condamnation, le signalement et la revérification.")],
    C("Consigner, c'est couper, vérifier, condamner et documenter pour garantir l'absence de tension.",
      "Coupure → vérification → condamnation → signalisation → documentation",
      "Vérificateur contrôlé avant et après · levée autorisée par le responsable",
      "Identification~Lire les schémas~Circuit concerné~Coupure~Ouvrir les appareils~Séparation électrique~Vérification~Absence de tension~Appareil contrôlé",
      "Analyser le schéma et prévenir l'équipe|Ouvrir les dispositifs de coupure|Vérifier l'absence de tension|Condamner et signaliser|Documenter puis lever la consignation",
      "Se fier à un voyant au lieu du vérificateur|Oublier la condamnation|Laisser le circuit sans signalisation|Lever la consignation sans contrôle",
      "Vérificateur~Contrôlé avant et après~Condamnation~Cadenas ou dispositif~Panneau~Intervention en cours~Document~Signature~Levée~Autorisation",
      "Consignation~Mise hors tension durable~Intervention sûre~Simple coupure~Ouverture sans condamnation~Risque de réalimentation~Mise à terre~Protection complémentaire",
      "Absence de tension~Vérifiée par mesure~Condition de travail~Présence de tension~Interdiction d'intervenir~Consigne de sécurité"))

# ============================================================ PR3
add("PE-C03", "Équipements de protection individuelle et collective", "Pratique professionnelle", ["1re pro"],
    S("Les équipements de protection individuelle, ou EPI, protègent directement le travailleur."
      "|Les protections collectives protègent toutes les personnes présentes, sans action individuelle."
      "|Les EPI courants en électricité sont les gants isolants, les chaussures de sécurité, le casque et les lunettes."
      "|Les gants isolants sont classés selon une tension maximale d'utilisation et doivent être contrôlés."
      "|Les vêtements de travail ne doivent pas comporter de parties métalliques accessibles."
      "|Les lunettes protègent contre les projections lors de perçages ou de manipulations."
      "|Les protections collectives incluent les coffrets fermés, les capots, les barrières et les balisages."
      "|Une protection collective est préférable à une protection individuelle car elle protège tous les intervenants."
      "|Les EPI doivent être adaptés au risque, en bon état et portés correctement."
      "|Leur usage est complété par des consignes de travail et une formation pratique."
      "|Un EPI endommagé doit être retiré du service et remplacé immédiatement."
      "|Le port des EPI est une obligation pour le salarié comme pour l'employeur."),
    [QC("Que désigne un EPI ?", "Une protection qui protège tous les salariés~Un équipement porté par le travailleur~Une consigne écrite~Un extincteur", 1,
        "L'EPI est porté par la personne pour la protéger directement."),
     QC("Quel EPI protège les mains contre le risque électrique ?", "Des gants de jardin~Des gants isolants contrôlés~Des gants de laine~Aucun gant", 1,
        "Les gants isolants sont classés selon une tension maximale et contrôlés régulièrement."),
     QC("Quelle protection est préférable selon le principe général ?", "La protection individuelle~La protection collective~Le bon sens seul~La rapidité", 1,
        "La protection collective protège tous les intervenants sans dépendre de leur comportement."),
     QC("Quel élément est interdit sur un vêtement de travail électrique ?", "Une poche~Une partie métallique accessible~Une manche longue~Une couture", 1,
        "Les parties métalliques peuvent conduire le courant et créer un contact."),
     QC("Que faut-il faire d'un EPI endommagé ?", "Le garder~Le retirer du service et le remplacer~Le réparer avec du ruban~Le prêter", 1,
        "Un EPI détérioré ne garantit plus la protection et doit être remplacé."),
     QC("Quand porte-t-on des lunettes de protection ?", "Toujours~Lors d'un risque de projection~Jamais~Uniquement dehors", 1,
        "Perçage, meulage et manipulation peuvent projeter des débris."),
     QC("Qui est responsable du port des EPI ?", "Le seul salarié~L'employeur et le salarié~Le client~Le fournisseur", 1,
        "L'employeur fournit et forme, le salarié porte et entretient les équipements."),
     QT("Distinguer protection collective et protection individuelle et donner deux exemples de chaque.",
        "Une protection collective agit sur l'environnement de travail et protège toutes les personnes présentes, sans qu'elles aient à Effectuer un geste particulier : par exemple un coffret électrique fermé à clé et une barrière de balisage autour d'une zone sous tension. Une protection individuelle est portée par le travailleur et ne protège que lui : par exemple des gants isolants et des chaussures de sécurité. La protection collective est prioritaire car elle ne dépend pas de la vigilance de chacun, mais les EPI restent nécessaires pour les risques résiduels.",
        "On attend la distinction entre protection de l'environnement et protection portée, avec exemples."),
     QT("Un technicien doit percer un mur près d'une gaine électrique. Quels EPI et quelles précautions ?",
        "Il consigne le circuit concerné après avoir repéré la gaine sur les plans. Il porte des lunettes contre les projections de poussière et de débris, des gants de manutention, des chaussures de sécurité et un casque si la zone est en chantier. Il utilise un détecteur de conducteurs avant de percer et travaille à faible vitesse. Si le doute subsiste, il s'arrête et demande une vérification complémentaire. Après l'opération, il contrôle l'absence de dommage sur la gaine et remet en service le circuit seulement après vérification.",
        "La réponse doit citer détection, consignation, lunettes et autres EPI adaptés, puis contrôle.")],
    C("La protection collective protège tous les intervenants ; les EPI protègent individuellement contre les risques résiduels.",
      "Collective > individuelle · EPI adaptés au risque et contrôlés",
      "Gants isolants · chaussures · casque · lunettes · coffrets et barrières",
      "Protection collective~Protège tous~Coffret et barrière~EPI~Porté par le salarié~Gants et chaussures~Gants isolants~Classe de tension~Contrôle périodique",
      "Analyser le risque et la tâche|Privilégier la protection collective|Choisir les EPI adaptés|Vérifier leur état avant usage|Former et contrôler le port",
      "Croire que des gants suffisent|Utiliser un EPI abîmé|Porter des vêtements métalliques|Ignorer la protection collective",
      "NF C 15-100~Règles d'installation~30 mA~Différentiel~Casque~Protection de la tête~Lunettes~Projections~Gants~Tension maximale",
      "Protection collective~Sans action individuelle~Efficace pour tous~Protection individuelle~Portée par une personne~Efficacité dépendante du port~EPI et formation~Complément nécessaires",
      "Risque résiduel~Reste après protection collective~EPI nécessaires~Suppression du risque~Meilleure solution~Conception sûre"))

# ============================================================ PR4
add("PE-C04", "Câblage et raccordement des conducteurs", "Pratique professionnelle", ["1re pro"],
    S("Le raccordement d'un conducteur doit être mécaniquement solide et électriquement fiable."
      "|La section du câble est choisie selon l'intensité nominale et la longueur de la ligne."
      "|Une section insuffisante provoque un échauffement et une chute de tension."
      "|Le dénudage doit retirer l'isolant sans abîmer les brins du conducteur."
      "|La longueur dénudée correspond à la profondeur de la borne indiquée par le fabricant."
      "|Les conducteurs souples sont sertis avec des embouts pour éviter les brins dispersés."
      "|Le couple de serrage de la borne doit respecter la valeur prescrite."
      "|Un serrage trop faible crée un mauvais contact et un échauffement localisé."
      "|Un serrage trop fort peut écraser le conducteur ou endommager le bornier."
      "|Chaque borne ne reçoit que le nombre de conducteurs autorisé par le constructeur."
      "|Le repérage des conducteurs est conservé jusqu'au bornier pour garantir la traçabilité."
      "|Un contrôle de continuité et d'isolement est réalisé avant la mise sous tension."),
    [QC("Sur quoi choisit-on la section d'un câble ?", "Sa couleur~L'intensité et la longueur de la ligne~Le nombre de spires~Le prix du cuivre", 1,
        "La section dépend du courant à transporter et de la chute de tension admissible."),
     QC("Que risque-t-on avec une section trop faible ?", "Une tension plus élevée~Un échauffement~Une fréquence plus basse~Rien", 1,
        "La résistance augmente et la puissance dissipée R I² échauffe le câble."),
     QC("Que faut-il éviter lors du dénudage ?", "Retirer trop d'isolant~Abîmer les brins~Utiliser un cutter~Mesurer la longueur", 1,
        "Les brins coupés réduisent la section utile et fragilisent la connexion."),
     QC("À quoi sert un embout de sertissage ?", "À colorer le fil~À maintenir les brins d'un conducteur souple~À allonger le câble~À isoler la borne", 1,
        "L'embout empêche les brins de se disperser lors du serrage."),
     QC("Quel est un risque d'un serrage insuffisant ?", "Un court-circuit~Un mauvais contact et un échauffement~Une baisse de section~Une surtension", 1,
        "Le contact résistif dissipe de la chaleur et peut provoquer un départ de feu."),
     QC("Que faut-il respecter au niveau d'une borne ?", "Le couple de serrage prescrit~Le sens de la vis~La couleur du bornier~Le nombre de vis", 0,
        "Le fabricant indique le couple de serrage et le nombre maximal de conducteurs."),
     QC("Quel contrôle précède la mise sous tension ?", "Un test de continuité et d'isolement~Une mesure de fréquence~Un essai de court-circuit~Une pesée", 0,
        "On vérifie la continuité des liaisons et l'isolement des conducteurs."),
     QT("Expliquer pourquoi un mauvais serrage de borne est dangereux.",
        "Une borne insuffisamment serrée présente une résistance de contact élevée. Le courant traversant cette résistance dissipe une puissance égale à R I², ce qui échauffe localement la connexion. La dilatation thermique du métal dessert progressivement la borne, ce qui augmente encore la résistance : un cercle vicieux s'installe. À la longue, l'isolant peut fondre et un départ d'incendie est possible. À l'inverse, un serrage excessif écrase les brins et réduit la section de passage. Le respect du couple de serrage et un contrôle thermique après mise en service sont donc essentiels.",
        "On attend l'explication par la résistance de contact, l'échauffement et le cercle vicieux."),
     QT("Décrire les étapes d'un raccordement correct d'un conducteur souple sur un bornier.",
        "On coupe le câble à la longueur nécessaire en laissant une marge pour le cheminement. On dénude sur la longueur indiquée par le fabricant sans entailler les brins. On sertit un embout adapté à la section du conducteur. On présente le fil dans la borne en respectant son repère et on serre au couple prescrit avec un tournevis ou une clé dynamométrique. On vérifie que tous les brins sont prisonniers de la borne et qu'aucun fil n'est dénudé à l'extérieur. On contrôle ensuite la continuité et l'isolement de la liaison avant de remettre sous tension.",
        "La réponse doit citer dénudage, sertissage, couple, vérification visuelle et contrôle électrique.")],
    C("Un raccordement fiable associe section adaptée, dénudage soigné et serrage au couple prescrit.",
      "Pertes = R contact × I² · couple de serrage = valeur du fabricant",
      "Embout de sertissage · repérage conservé · contrôle continuité et isolement",
      "Section~Choix selon l'intensité~Échauffement si faible~Dénudage~Longueur de la borne~Brins intacts~Serrage~Couple prescrit~Contact fiable",
      "Choisir la section et la longueur|Dénuder sans abîmer les brins|Sertir un embout si besoin|Raccorder au couple prescrit|Contrôler continuité et isolement",
      "Laisser des brins hors de la borne|Serrer « à fond » sans mesure|Changer le repère du fil|Mettre sous tension sans contrôle",
      "Section 2,5 mm²~Courant nominal~Couple~Valeur fabricant~Embout~Conducteur souple~Dénudage~Longueur de borne~Continuité~Contrôle final",
      "Conducteur rigide~Brins uniques~Sertissage rare~Conducteur souple~Multi-brins~Embout nécessaire~Borne~Point de connexion~Couple de serrage",
      "Mauvais contact~Résistance élevée~Échauffement~Bon contact~Faible résistance~Connexion durable~Contrôle~Vérification avant service"))

# ============================================================ PR5
add("PE-C05", "Déroulé d'un chantier d'installation électrique", "Pratique professionnelle", ["Terminale pro"],
    S("Un chantier d'installation électrique suit des étapes ordonnées, de l'étude à la réception."
      "|La phase d'étude analyse le besoin, les plans, la puissance et les contraintes du site."
      "|Un calendrier et une liste des matériels sont établis avant le démarrage."
      "|La préparation comprend la commande des équipements et la vérification des délais."
      "|Sur site, on commence par le repérage des emplacements et le traçage des chemins de câbles."
      "|Les gaines, les boîtes et les coffrets sont posés avant le tirage des conducteurs."
      "|Le tirage des câbles respecte les sections, les couleurs et les rayons de courbure."
      "|Le raccordement est réalisé selon les schémas et les plans de bornier."
      "|Chaque étape fait l'objet d'un contrôle qualité et d'un relevé des écarts."
      "|La sécurité du chantier impose le balisage, la consignation et le port des EPI."
      "|Les essais et la vérification finale précèdent la mise sous tension."
      "|La remise des documents et la formation de l'utilisateur concluent le chantier."),
    [QC("Que fait-on avant le démarrage d'un chantier ?", "On tire les câbles~On réalise l'étude et le planning~On met sous tension~On pose les prises", 1,
        "L'étude du besoin et le calendrier précèdent toute intervention."),
     QC("Quel est le premier travail sur site ?", "Le raccordement~Le repérage et le traçage~La mise en service~La facturation", 1,
        "On repère les emplacements et trace les chemins avant la pose."),
     QC("Que faut-il respecter lors du tirage des câbles ?", "La couleur du mur~Les sections, les repères et les rayons de courbure~Le nombre de vis~La température", 1,
        "Ces paramètres garantissent la durabilité et la conformité de l'installation."),
     QC("Sur quoi se base le raccordement ?", "Sur l'intuition~Sur les schémas et les plans de bornier~Sur la facture~Sur le planning seul", 1,
        "Les documents sont la référence pour chaque connexion."),
     QC("Quand réalise-t-on les essais ?", "Avant la pose~Après le raccordement et avant la mise sous tension~Jamais~Après la facturation", 1,
        "Les vérifications précèdent obligatoirement la mise en service."),
     QC("Quel document conclut le chantier ?", "Une simple note~Le dossier de remise avec schémas et procès-verbal~Un bon de commande~Un devis", 1,
        "Le dossier final contient les schémas mis à jour et le procès-verbal de vérification."),
     QC("Quelle mesure de sécurité concerne le chantier lui-même ?", "Le balisage et la consignation~La hausse de tension~Le retrait des EPI~L'absence de planning", 0,
        "Le chantier doit être balisé et les interventions consignées."),
     QT("Décrire les grandes phases d'un chantier depuis l'étude jusqu'à la remise des documents.",
        "Le chantier débute par l'étude du besoin : puissance, nombre de circuits, contraintes du bâtiment et réglementation. On établit ensuite le planning, la liste des matériels et les schémas. Sur site, on repère les emplacements, on pose les gaines, boîtes et coffrets, puis on tire les câbles en respectant les sections et les repères. On raccorde les conducteurs conformément aux plans de bornier, en contrôlant chaque étape. Après les essais d'isolement, de continuité et de fonctionnement des protections, on met l'installation sous tension. Enfin, on remet les schémas mis à jour, le procès-verbal et les consignes d'utilisation.",
        "On attend l'ordre : étude, planning, pose, câblage, contrôle, mise en service et remise des documents."),
     QT("Un retard de livraison d'un coffret est constaté. Comment organiser la suite du chantier ?",
        "On informe immédiatement le responsable et le client du retard et de son impact sur le calendrier. On identifie les tâches qui peuvent avancer sans le coffret : traçage, pose des gaines, tirage des câbles et préparation des conducteurs. On réorganise l'équipe pour éviter l'immobilité et on met à jour le planning. Si une solution de remplacement temporaire est possible, on la propose avec l'accord du client et du maître d'œuvre. On documente l'écart et on reprend le raccordement dès réception, en vérifiant la conformité du matériel livré.",
        "La réponse doit proposer information, réorganisation des tâches indépendantes et mise à jour du planning.")],
    C("Un chantier électrique progresse par étapes contrôlées, de l'étude du besoin à la remise des documents.",
      "Étude → planning → pose → câblage → essais → mise en service → documents",
      "Conformité NF C 15-100 · balisage · consignation · procès-verbal",
      "Étude~Analyse du besoin~Puissance et contraintes~Planning~Calendrier et matériels~Délais~Pose~Gaines et coffrets~Traçage",
      "Analyser le besoin et les contraintes|Établir le planning et les documents|Repérer et tracer sur site|Poser et câbler en contrôlant|Tester, mettre en service et remettre le dossier",
      "Commencer sans schéma|Négliger le balisage du chantier|Tirer les câbles avant les gaines|Mettre sous tension sans essais",
      "Planning~Délais et tâches~Retard~Impact à documenter~Schémas~Documents de référence~PV~Vérification finale~Essais~Isolement et continuité",
      "Chantier neuf~Installation complète~Documents complets~Rénovation~Installation existante~Contraintes supplémentaires~Maintenance~Intervention ponctuelle",
      "Pose~Gaines et coffrets~Avant câblage~Raccordement~Bornes et repères~Selon les schémas~Vérification~Contrôle qualité"))

# ============================================================ PR6
add("PE-C06", "Mise en service et essais d'une installation", "Pratique professionnelle", ["Terminale pro"],
    S("La mise en service est l'ultime étape qui autorise l'alimentation électrique d'une installation."
      "|Elle n'intervient qu'après la réalisation complète et le contrôle visuel de l'ouvrage."
      "|Le contrôle visuel vérifie le repérage, le serrage des bornes et l'état des isolants."
      "|Le test de continuité vérifie que chaque liaison est correctement établie."
      "|La continuité du conducteur de protection est contrôlée avec une mesure de faible résistance."
      "|Le test d'isolement mesure la résistance entre conducteurs et entre conducteurs et terre."
      "|Une résistance d'isolement trop faible signale un défaut ou une humidité."
      "|Les disjoncteurs et les différentiels sont testés individuellement."
      "|Le test du différentiel vérifie son déclenchement pour un courant de fuite représentatif."
      "|Les circuits sont mis sous tension progressively, un par un, pour limiter le risque."
      "|Les tensions, les intensités et les fonctions sont relevées et comparées aux valeurs attendues."
      "|Les résultats sont consignés dans un procès-verbal de mise en service remis au client."),
    [QC("Quand la mise en service peut-elle avoir lieu ?", "Avant la pose~Après contrôle visuel et essais~Pendant le câblage~Avant les schémas", 1,
        "Tous les contrôles doivent être réalisés avant la mise sous tension."),
     QC("Que vérifie le test de continuité ?", "L'isolement des conducteurs~Que chaque liaison est établie~La tension du réseau~La fréquence", 1,
        "La continuité confirme que le circuit est complet entre deux points."),
     QC("Quelle mesure concerne le conducteur de protection ?", "Une mesure de tension~Une mesure de faible résistance~Une mesure de fréquence~Une mesure de puissance", 1,
        "La continuité de la terre doit présenter une résistance très faible."),
     QC("Que détecte un test d'isolement insuffisant ?", "Une bonne installation~Un défaut d'isolement ou de l'humidité~Une surcharge~Un bon serrage", 1,
        "Une faible résistance d'isolement signale un défaut à rechercher."),
     QC("Que vérifie le test d'un différentiel ?", "Sa couleur~Son déclenchement pour un courant de fuite~Sa taille~Son prix", 1,
        "On simule une fuite pour vérifier la coupure et le temps de réponse."),
     QC("Comment met-on les circuits sous tension ?", "Tous en même temps~Progressivement, un par un~Au hasard~Sans contrôle", 1,
        "Une mise sous tension progressive facilite le diagnostic d'un défaut éventuel."),
     QC("Quel document est remis au client ?", "Un devis~Le procès-verbal de mise en service~Une facture seule~Un plan de bornier seul", 1,
        "Le procès-verbal consigne les contrôles et les résultats."),
     QT("Expliquer l'ordre des essais avant la mise en service d'une installation.",
        "On commence par un contrôle visuel complet : repérage des conducteurs, serrage des bornes, état des isolants et présence des protections. On mesure ensuite la continuité des liaisons, en particulier celle du conducteur de protection. On réalise alors le test d'isolement entre conducteurs et par rapport à la terre, après avoir débranché les appareils sensibles. On teste individuellement les disjoncteurs et les différentiels. Ce n'est qu'après ces contrôles que l'on met progressivement les circuits sous tension et que l'on relève les tensions et courants. Les résultats sont inscrits dans le procès-verbal.",
        "On attend l'ordre visuel, continuité, isolement, protections, tension progressive et documentation."),
     QT("Un test d'isolement donne une résistance très faible sur un circuit d'éclairage. Que faire ?",
        "On ne met pas le circuit sous tension. On isole d'abord les appareils et les lampes qui pourraient influencer la mesure. On vérifie les connexions, les boîtes de dérivation et l'état des gaines à la recherche d'un conducteur pincé ou d'une gaine abîmée. On contrôle l'absence d'humidité dans les boîtes et les coffrets. On recherche un éventuel court-circuit entre neutre et terre ou entre phase et terre. Après correction, on refait le test d'isolement et on ne remet en service que si la valeur est conforme. Le défaut et sa correction sont consignés dans le procès-verbal.",
        "La réponse doit refuser la mise sous tension, proposer une recherche méthodique et documenter la correction.")],
    C("La mise en service valide la conformité par des essais ordonnés avant toute alimentation.",
      "Visuel → continuité → isolement → protections → tension progressive",
      "Terre : faible résistance · isolement : forte résistance · procès-verbal",
      "Contrôle visuel~Repérage et serrage~Avant essais~Continuité~Liaison complète~Faible résistance~Isolement~Séparation des conducteurs~Forte résistance",
      "Inspecter visuellement l'installation|Mesurer la continuité des liaisons|Tester l'isolement|Vérifier les protections|Alimenter progressivement et documenter",
      "Mettre sous tension avant les essais|Débrancher les protections pour le test|Ignorer une valeur d'isolement faible|Oublier le procès-verbal",
      "Faible résistance~Continuité de la terre~Forte résistance~Isolement conforme~Différentiel~Test de fuite~PV~Preuve de conformité~Tension~Valeur relevée",
      "Continuité~Circuit complet~Courant peut circuler~Isolement~Conducteurs séparés~Pas de fuite~Court-circuit~Liaison accidentelle~Défaut à éliminer",
      "Essai~Mesure sur l'installation~Conforme ou non~Mise en service~Autorisation d'alimenter~Procès-verbal~Document final"))

# ============================================================ PR7
add("PE-C07", "Diagnostic de défauts et maintenance", "Pratique professionnelle", ["Terminale pro"],
    S("Le diagnostic électrique recherche la cause d'un dysfonctionnement à partir de symptômes observés."
      "|Une démarche structurée évite les remplacements d'appareils inutiles."
      "|On commence par recueillir les faits : date, circonstances, voyants, bruits et odeurs."
      "|On consulte les schémas et l'historique de l'installation avant toute mesure."
      "|La mesure comparative permet de confronter une valeur relevée à une valeur nominale."
      "|La méthode de substitution remplace temporairement un composant suspect par un composant connu."
      "|La méthode de coupure isolée sectionne progressivement le circuit pour localiser le défaut."
      "|Les mesures de tension, d'intensité et de résistance orientent le diagnostic."
      "|Une absence de tension peut venir d'une protection déclenchée, d'un contact ou d'un conducteur rompu."
      "|Une intensité anormale peut indiquer une surcharge, un court-circuit ou un défaut d'isolement."
      "|La maintenance préventive programme des contrôles avant la panne."
      "|La maintenance corrective intervient après la panne et documente la cause et la réparation."),
    [QC("Quelle est la première étape d'un diagnostic ?", "Remplacer l'appareil~Recueillir les faits et les symptômes~Couper le courant définitivement~Refaire l'installation", 1,
        "On observe et on note les faits avant toute action."),
     QC("Que consiste la méthode de substitution ?", "À couper le courant~À remplacer un composant suspect par un composant connu~À changer le schéma~À augmenter la tension", 1,
        "La substitution teste l'hypothèse en échangeant temporairement l'élément suspect."),
     QC("Que révèle une intensité anormale ?", "Une tension normale~Une surcharge, un court-circuit ou un défaut d'isolement~Une bonne isolation~Une maintenance préventive", 1,
        "Un courant trop élevé signale toujours un défaut à rechercher."),
     QC("Quelle mesure aide à détecter une coupure de conducteur ?", "Une mesure de tension en aval~Une mesure de température~Une mesure de fréquence~Une mesure de puissance", 0,
        "L'absence de tension en aval d'un point indique une interruption."),
     QC("Qu'appelle-t-on maintenance préventive ?", "Une réparation après panne~Des contrôles programmés avant la panne~Un remplacement systématique~Une intervention d'urgence", 1,
        "La maintenance préventive vise à anticiper la défaillance."),
     QC("Que doit contenir le compte rendu d'intervention ?", "La cause, l'action réalisée et les mesures~Seulement l'heure d'arrivée~Le prix des pièces uniquement~Aucune information", 0,
        "La traçabilité permet de comprendre l'historique et d'éviter les récidives."),
     QC("Pourquoi consulter les schémas avant de mesurer ?", "Pour connaître le chemin du courant et les points de mesure~Pour changer la couleur des câbles~Pour augmenter la tension~Pour éviter de porter des EPI", 0,
        "Le schéma oriente le diagnostic et évite des mesures inutiles."),
     QT("Une prise alimentant plusieurs appareils ne fournit plus de tension. Décrire la démarche de diagnostic.",
        "On vérifie d'abord les voyants et le disjoncteur en amont, puis on consulte le schéma pour identifier le circuit. On mesure la tension à l'entrée du disjoncteur, puis à sa sortie, puis aux bornes de la prise. Si la tension disparaît entre deux points, le défaut se situe entre eux : conducteur rompu, borne desserrée ou contact défectueux. On vérifie également le déclenchement éventuel d'un différentiel et l'état des connexions dans la boîte de dérivation. Après réparation, on contrôle la continuité, l'isolement et le fonctionnement sous charge, puis on note l'intervention dans le dossier de maintenance.",
        "On attend une progression le long du circuit et un contrôle final après réparation."),
     QT("Comparer maintenance préventive et maintenance corrective avec un exemple sur un moteur.",
        "La maintenance préventive est programmée : contrôle périodique de l'isolement du moteur, vérification des balais ou des roulements, mesure de la température et graissage. Elle vise à détecter une dérive avant la panne et à planifier l'arrêt de la machine. La maintenance corrective intervient après la panne : par exemple, le moteur ne démarre plus parce qu'un contacteur est collé ou une phase est absente. On diagnostique, on remplace le composant défectueux et on documente l'intervention. Une bonne politique combine les deux : la préventive réduit le nombre de pannes, la corrective reste nécessaire pour les défaillances imprévues.",
        "La réponse doit opposer actions programmées et actions après panne, avec un exemple et un bilan.")],
    C("Le diagnostic procède par observation, hypothèses et mesures ; la maintenance documente les actions.",
      "Faits → schéma → mesures → hypothèse → correction → contrôle",
      "Substitution · coupure isolée · préventive / corrective",
      "Symptôme~Signe observé~Voyant ou bruit~Schéma~Guide de la mesure~Chemin du courant~Substitution~Test par échange~Hypothèse~Cause supposée",
      "Recueillir les faits et consulter les schémas|Mesurer aux points clés du circuit|Formuler une hypothèse et la tester|Corriger la cause identifiée|Contrôler et documenter l'intervention",
      "Remplacer des pièces au hasard|Ignorer les valeurs nominales|Mesurer sans consulter le schéma|Ne pas consigner l'intervention",
      "Absence de tension~Protection ou coupure~Intensité élevée~Surcharge ou court-circuit~Préventive~Contrôle programmé~Corrective~Réparation après panne",
      "Maintenance préventive~Avant la panne~Contrôles périodiques~Maintenance corrective~Après la panne~Restauration du service~Diagnostic~Recherche de la cause",
      "Mesure comparative~Relevé contre nominal~Écart révélateur~Substitution~Échange de composant~Isolement du défaut~Sectionnement progressif"))

# ============================================================ PR8
add("PE-C08", "Réalisation et contrôle d'une armoire électrique", "Pratique professionnelle", ["1re pro"],
    S("Une armoire électrique regroupe les appareils de commande, de protection et de raccordement."
      "|Sa réalisation suit un plan d'implantation et un schéma de câblage validés."
      "|Le châssis et la porte doivent offrir un degré de protection adapté à l'environnement."
      "|Les appareils sont fixés sur le rail ou la plaque selon le plan d'implantation."
      "|Un bornier répartit les liaisons vers l'extérieur de l'armoire."
      "|Les câbles sont cheminés dans des goulottes et attachés à intervalle régulier."
      "|Les circuits de commande et de puissance sont séparés pour limiter les perturbations."
      "|Chaque conducteur porte un repère lisible correspondant au schéma."
      "|La continuité du conducteur de protection entre tous les appareils est vérifiée."
      "|Un contrôle de conformité compare le réaliser au schéma et au cahier des charges."
      "|Un essai sous tension progressively valide les fonctions de commande et de protection."
      "|La porte de l'armoire porte une étiquette d'identification et les avertissements nécessaires."),
    [QC("Quel document donne la position des appareils dans l'armoire ?", "Le schéma de principe~Le plan d'implantation~Le devis~Le procès-verbal", 1,
        "Le plan d'implantation situe physiquement chaque appareil."),
     QC("Que désigne l'indice de protection d'une armoire ?", "Sa couleur~Sa protection contre la poussière et l'eau~Sa puissance~Son prix", 1,
        "L'indice IP caractérise la protection contre les corps solides et les liquides."),
     QC("Pourquoi séparer commande et puissance ?", "Pour utiliser moins de câbles~Pour limiter les perturbations électromagnétiques~Pour augmenter la tension~Pour réduire le nombre de bornes", 1,
        "La séparation réduit les interférences entre circuits."),
     QC("Où sont regroupées les liaisons vers l'extérieur ?", "Sur un bornier~Dans la goulotte~Sur le rail~Dans la porte", 0,
        "Le bornier centralise les entrées et sorties de l'armoire."),
     QC("Que vérifie le contrôle de conformité ?", "La couleur de la porte~La concordance entre le réalisé et les documents~Le poids de l'armoire~La date de livraison", 1,
        "On compare l'installation réelle au schéma et au cahier des charges."),
     QC("Quel repère doit rester lisible sur chaque conducteur ?", "Le numéro de fil~La marque du fabricant~La date~Le prix", 0,
        "Le numéro de fil assure la traçabilité avec le schéma."),
     QC("Que porte la porte de l'armoire ?", "Une étiquette d'identification et des avertissements~Un schéma uniquement~Aucune information~Le devis", 0,
        "L'identification et les avertissements sont indispensables à la sécurité."),
     QT("Décrire les étapes de réalisation d'une armoire de commande.",
        "On étudie d'abord le schéma de principe et le plan d'implantation, puis on vérifie la liste des appareils. On fixe le châssis, les rails et les goulottes sur la plaque de montage. On place les appareils de protection, de commande et les borniers selon le plan. On chemine les câbles en séparant commande et puissance, en respectant les repères et les sections. On raccorde les conducteurs aux bornes au couple prescrit, puis on contrôle la continuité de la terre et l'isolement. On compare le montage au schéma, on étiquette la porte, puis on alimente progressivement pour valider chaque fonction.",
        "On attend étude, montage mécanique, câblage, contrôle électrique, conformité et essais."),
     QT("Lors du contrôle, un appareil ne reçoit pas la tension attendue. Comment procéder ?",
        "On vérifie d'abord que le schéma et le plan de bornier sont bien compris et que le repère du fil est correct. On mesure la tension à l'entrée de l'appareil, puis en amont sur le bornier et sur le contacteur qui commande l'alimentation. On contrôle la continuité du conducteur suspect, le serrage des bornes et l'état des contacts. Si un fil est mal repéré ou mal branché, on le corrige en conservant son numéro d'origine. On refait ensuite le contrôle de continuité et d'isolement, puis on teste la fonction concernée avant de clore le dossier.",
        "La réponse doit suivre un cheminement amont-aval et vérifier repérage, continuité et bornes.")],
    C("Une armoire conforme résulte d'un montage ordonné, d'un repérage strict et d'un contrôle final.",
      "Plan d'implantation + schéma de câblage + cahier des charges",
      "IP adapté · séparation commande/puissance · terre · essais progressifs",
      "Plan d'implantation~Position des appareils~Montage~Schéma de câblage~Liaisons et bornes~Repérage~Bornier~Entrées et sorties~Raccordement extérieur",
      "Étudier les documents|Monter châssis, rails et goulottes|Placer appareils et borniers|Chemins et raccorder les câbles|Contrôler conformité et essayer",
      "Monter sans plan|Mélanger commande et puissance|Changer les numéros de fil|Omettre le contrôle de la terre",
      "Indice IP~Protection poussière et eau~Goulotte~Cheminement des câbles~Repère~Numéro de fil~Couple~Serrage des bornes",
      "Armoire de commande~Appareils de commande et protection~Schéma de câblage~Réalisation~Armoire de distribution~Répartition de l'énergie~Disjoncteurs~Protection des circuits",
      "Montage mécanique~Rails et plaques~Avant câblage~Câblage~Conducteurs et bornes~Selon le plan~Contrôle final~Conformité et essais"))

# ============================================================ EC1
add("PE-C09", "Coût d'une installation et établissement d'un devis", "Économie et gestion", ["1re pro"],
    S("Un devis est un document commercial qui propose un prix et des délais pour une prestation."
      "|Il est établi à partir du cahier des charges et des quantités relevées."
      "|Le prix de revient comprend les fournitures, la main-d'œuvre et les frais généraux."
      "|Les fournitures sont valorisées au prix d'achat, souvent remisé par le fournisseur."
      "|La main-d'œuvre se calcule en multipliant le temps prévu par un taux horaire."
      "|Une marge est ajoutée au prix de revient pour dégager un bénéfice."
      "|La TVA est ensuite appliquée au prix hors taxes pour obtenir le prix toutes taxes comprises."
      "|Un devis doit être clair, daté, signé et valable pendant une durée déterminée."
      "|Il mentionne les quantités, les références des matériels et le détail des opérations."
      "|Une option peut être proposée pour une variante technique ou un complément."
      "|Le client compare plusieurs devis en regardant le prix, les délais et les garanties."
      "|Après acceptation, le devis devient un contrat engageant les deux parties."),
    [QC("Que contient un devis ?", "Un prix et des délais~Seulement le nom du client~La facture déjà payée~Le salaire du technicien", 0,
        "Le devis propose un prix, des prestations et des délais."),
     QC("Comment calculer le coût de la main-d'œuvre ?", "Temps prévu multiplié par le taux horaire~Prix des fournitures divisé par deux~TVA seule~Marge seule", 0,
        "Le coût de la main-d'œuvre dépend du temps passé et du taux horaire."),
     QC("Qu'appelle-t-on prix de revient ?", "Le prix TTC~Fournitures + main-d'œuvre + frais généraux~La marge seule~La TVA", 1,
        "Le prix de revient rassemble les coûts directs et indirects de la prestation."),
     QC("À quoi sert la marge ?", "À payer la TVA~À dégager un bénéfice~À réduire les quantités~À fixer le délai", 1,
        "La marge s'ajoute au prix de revient avant application de la TVA."),
     QC("Quand le devis devient-il un contrat ?", "Dès sa rédaction~Après acceptation par le client~Après la facture~Jamais", 1,
        "L'acceptation du devis engage juridiquement les deux parties."),
     QC("Que doit mentionner un devis clair ?", "Les quantités et les références~Seulement le total~Le prix du concurrent~Une estimation vague", 0,
        "Le détail des prestations et des matériels évite les malentendus."),
     QC("Quel taux de TVA s'applique le plus souvent à une installation électrique en France ?", "5,5 %~10 %~20 %~0 %", 2,
        "Le taux normal de 20 % s'applique à la plupart des prestations d'installation."),
     QT("Une installation nécessite 400 € de fournitures, 12 heures de main-d'œuvre à 45 €/h et 60 € de frais généraux. Calculer le prix de revient hors taxes, puis le prix TTC avec une marge de 15 % et une TVA de 20 %.",
        "La main-d'œuvre coûte 12 × 45 = 540 €. Le prix de revient hors taxes vaut 400 + 540 + 60 = 1000 €. La marge de 15 % ajoute 150 €, ce qui donne un prix hors taxes de 1150 €. La TVA de 20 % représente 230 €, donc le prix toutes taxes comprises est 1380 €. On vérifie l'ordre des calculs : d'abord les coûts, puis la marge, puis la TVA sur le prix hors taxes.",
        "On attend le prix de revient, la marge, puis la TVA appliquée au prix hors taxes."),
     QT("Pourquoi un devis doit-il être détaillé et daté ?",
        "Le détail permet au client de comparer les offres sur une base comparable et d'identifier precisément les prestations incluses. Il protège aussi l'entreprise en cas de désaccord sur l'étendue des travaux. La date fixe la période de validité : les prix des fournitures et les disponibilités peuvent évoluer. Un devis daté, signé et accepté devient un contrat : il définit les obligations de chacun, les délais et les conditions de règlement. Une mention précise des options permet enfin de distinguer le socle des prestations facultatives.",
        "La réponse doit évoquer comparabilité, protection juridique, validité et transformation en contrat.")],
    C("Le devis transforme un besoin en prix structuré : coûts, marge, TVA et engagements.",
      "Prix de revient = fournitures + main-d'œuvre + frais généraux",
      "Prix HT = revient + marge · prix TTC = HT × (1 + TVA)",
      "Devis~Proposition commerciale~Prix et délais~Prix de revient~Coûts directs et indirects~Base du prix~Marge~Bénéfice~Ajout au revient~TVA~Taxe sur le prix HT~Prix final",
      "Relever les quantités sur le cahier des charges|Valoriser fournitures et main-d'œuvre|Ajouter les frais généraux|Appliquer marge et TVA|Rédiger et dater le devis",
      "Oublier les frais généraux|Appliquer la TVA avant la marge|Ne pas dater le devis|Confondre devis et facture",
      "400 € de fournitures~12 h à 45 €~540 € de main-d'œuvre~Revient 1000 €~Marge 15 %~HT 1150 €~TTC 1380 €",
      "Devis~Proposition avant commande~Non engageant jusqu'acceptation~Facture~Demande de paiement~Après exécution~Commande~Acceptation du devis~Contrat",
      "Prix de revient~Coût pour l'entreprise~Interne~Prix de vente~Prix demandé au client~Public~Marge~Différence~Bénéfice"))

# ============================================================ EC2
add("PE-C10", "Gestion des stocks et approvisionnement", "Économie et gestion", ["Terminale pro"],
    S("L'approvisionnement vise à mettre à disposition les matériels nécessaires au bon moment."
      "|Un stock trop important immobilise de la trésorerie et occupe de l'espace."
      "|Un stock insuffisant arrête le chantier et génère des pénalités de retard."
      "|Les articles sont classés par famille : câbles, appareils, connecteurs, outils et consommables."
      "|Une fiche de stock indique la quantité disponible, le seuil et le délai de réapprovisionnement."
      "|Le seuil de commande déclenche une commande avant l'épuisement du stock."
      "|Le stock de sécurité couvre les aléas de livraison et les pics de consommation."
      "|La méthode du premier entré, premier sorti limite le vieillissement des articles."
      "|Un inventaire tournant vérifie régulièrement les quantités physiques."
      "|Les écarts entre stock théorique et stock réel doivent être expliqués et corrigés."
      "|Le choix du fournisseur tient compte du prix, du délai, de la qualité et de la disponibilité."
      "|Un bon de commande trace la commande et sert à la réception des marchandises."),
    [QC("Quel risque presente un stock trop important ?", "Une panne de courant~Une immobilisation de trésorerie~Une meilleure rentabilité~Aucun risque", 1,
        "Le capital engagé dans le stock ne peut pas être utilisé ailleurs."),
     QC("Que déclenche le seuil de commande ?", "Une facture~Une commande de réapprovisionnement~Une remise~Une panne", 1,
        "Le seuil est fixé pour passer commande avant la rupture de stock."),
     QC("À quoi sert un stock de sécurité ?", "À réduire les prix~À couvrir les aléas de livraison~À supprimer les inventaires~À augmenter les délais", 1,
        "Il protège contre les variations de demande et les retards fournisseurs."),
     QC("Que signifie la méthode premier entré, premier sorti ?", "Le dernier acheté est utilisé en premier~Le premier acheté est utilisé en premier~On choisit au hasard~On ne classe rien", 1,
        "Cette méthode limite le vieillissement des pièces en stock."),
     QC("Quel document trace une commande ?", "Le bon de commande~Le plan de câblage~Le procès-verbal~La fiche de paie", 0,
        "Le bon de commande sert de référence à la commande et à la réception."),
     QC("Quel critère ne concerne pas le choix d'un fournisseur ?", "Le délai~La qualité~La disponibilité~La couleur du camion", 3,
        "Les critères pertinents sont prix, délai, qualité et disponibilité."),
     QC("Pourquoi réaliser un inventaire tournant ?", "Pour vérifier les quantités physique progressivement~Pour augmenter le stock~Pour changer de fournisseur~Pour fermer l'entrepôt", 0,
        "L'inventaire tournant détecte les écarts sans interrompre l'activité."),
     QT("Une entreprise consomme 20 boîtiers par semaine. Le délai d'approvisionnement est de 2 semaines et le stock de sécurité de 15 boîtiers. Calculer le seuil de commande.",
        "La consommation pendant le délai de livraison vaut 20 × 2 = 40 boîtiers. En ajoutant le stock de sécurité de 15 boîtiers, on obtient un seuil de commande de 55 boîtiers. Lorsque le stock disponible atteint 55 boîtiers, il faut passer commande. Si les livraisons sont régulières, la commande arrivera juste avant la rupture. Une consommation plus rapide ou un retard du fournisseur sera absorbé par le stock de sécurité.",
        "On attend seuil = consommation × délai + stock de sécurité, soit 55 boîtiers."),
     QT("Comment organiser la réception d'une commande de matériel électrique ?",
        "On rapproche d'abord le bon de commande du bon de livraison pour vérifier les références et les quantités. On contrôle l'état des emballages et la conformité des articles : section des câbles, calibration des disjoncteurs, indice de protection des coffrets. On note les écarts et on réserve le matériel non conforme en attendant une décision du fournisseur. On enregistre ensuite les quantités dans la fiche de stock en appliquant la méthode premier entré, premier sorti. Enfin, on transmet le bon de réception à la comptabilité pour le règlement.",
        "La réponse doit citer bon de commande, contrôle quantité et qualité, enregistrement et transmission.")],
    C("Gérer un stock, c'est concilier disponibilité, coût et traçabilité des matériels.",
      "Seuil = consommation × délai + stock de sécurité",
      "Premier entré premier sorti · inventaire tournant · bon de commande",
      "Stock disponible~Quantité en magasin~Seuil de commande~Déclencheur~Avant la rupture~Stock de sécurité~Marge contre les aléas~Délai de livraison~Attente fournisseur",
      "Classer les articles par famille|Fixer seuil et stock de sécurité|Suivre les entrées et sorties|Réaliser des inventaires tournants|Contrôler la conformité à la réception",
      "Commander trop tard|Immobiliser trop de stock|Mélanger les références|Ignorer les écarts d'inventaire",
      "20 boîtiers par semaine~Délai 2 semaines~Consommation 40~Stock sécurité 15~Seuil 55~Bon de commande~Réception~Contrôle qualité",
      "Stock important~Disponibilité élevée~Coût de immobilisation~Stock faible~Trésorerie préservée~Risque de rupture~Stock de sécurité~Compromis",
      "Inventaire tournant~Vérification progressive~Pas d'arrêt d'activité~Inventaire complet~Arrêt et comptage total~Précision maximale"))

# ============================================================ EC3
add("PE-C11", "Suivi de chantier et suivi financier", "Économie et gestion", ["Terminale pro"],
    S("Le suivi de chantier compare en permanence l'avancement réel au planning prévu."
      "|Un écart de délai ou de coût doit être identifié le plus tôt possible."
      "|Le compte rendu d'activité consigne les heures travaillées, les tâches réalisées et les incidents."
      "|Les heures passées sont comparées aux heures prévues dans le devis."
      "|Un dépassement d'heures réduit la marge prévue et doit être analysé."
      "|Les commandes et les livraisons sont suivies pour anticiper les ruptures."
      "|Les dépenses engagées sont relevées régulièrement dans un tableau de suivi."
      "|Le coût engagé est comparé au budget pour calculer l'écart."
      "|Une situation de travaux permet de facturer les prestations avancées."
      "|La facture finale est établie après la réception et la levée des réserves."
      "|Les pièces justificatives, bons de livraison et comptes rendus sont archivés."
      "|Un bon suivi financier protège la rentabilité de l'entreprise et la relation client."),
    [QC("Que compare le suivi de chantier ?", "L'avancement réel au planning~La couleur des câbles aux schémas~Le prix du cuivre à la TVA~Les heures de nuit aux heures de jour", 0,
        "Le suivi mesure l'écart entre prévu et réalisé."),
     QC("Que consigne un compte rendu d'activité ?", "Les heures, les tâches et les incidents~Seulement la météo~Le prix de vente~Le nom du client", 0,
        "Il retrace l'activité quotidienne du chantier."),
     QC("Quel effet a un dépassement d'heures ?", "Il augmente la marge~Il réduit la marge~Il n'a aucun effet~Il supprime la TVA", 1,
        "Les heures supplémentaires non prévues réduisent le bénéfice."),
     QC("Quand établit-on la facture finale ?", "Au début~Après réception et levée des réserves~Avant le devis~Jamais", 1,
        "La facturation finale suit la réception des travaux."),
     QC("Qu'appelle-t-on une situation de travaux ?", "Une facturation de prestations avancées~Un simple devis~Un bon de commande~Un inventaire", 0,
        "Elle permet de régler les travaux déjà réalisés avant la fin du chantier."),
     QC("Que faut-il archiver ?", "Les pièces justificatives~Les seuls schémas~Rien~Les seules factures", 0,
        "Bons de livraison, comptes rendus et factures constituent le dossier."),
     QC("Pourquoi suivre les dépenses pendant le chantier ?", "Pour détecter un dépassement de budget~Pour augmenter la tension~Pour changer de client~Pour supprimer les documents", 0,
        "Le suivi financier permet d'agir avant la fin du chantier."),
     QT("Un chantier prévoit 80 heures de main-d'œuvre à 50 €/h. Après deux semaines, 50 heures sont consommées pour 60 % des travaux. Analyser la situation.",
        "Le budget de main-d'œuvre prévu est 80 × 50 = 4000 €. Le coût déjà engagé est 50 × 50 = 2500 €. Si 60 % des travaux sont réalisés avec 50 heures, la consommation totale estimée est 50 / 0,6, soit environ 83 heures. Le dépassement prévisible est donc d'environ 3 heures, soit 150 €, ce qui réduit la marge. On doit analyser les causes : difficultés de câblage, attente de matériel ou sous-estimationInitiale. Une action corrective peut être envisagée : réorganiser l'équipe ou récupérer du temps sur les tâches restantes.",
        "On attend le budget, le coût engagé, l'estimation finale et une proposition d'action."),
     QT("Décrire les documents qui constituent le dossier financier d'un chantier.",
        "Le dossier comprend le devis accepté, qui fixe le prix et les délais, les bons de commande adressés aux fournisseurs, les bons de livraison et factures d'achat, les comptes rendus d'activité avec les heures travaillées, les situations de travaux éventuelles et les factures émises, ainsi que le procès-verbal de réception. Ce ensemble permet de reconstituer le coût réel, de justifier les paiements et de répondre à un contrôle ou à un litige. Les documents sont classés par date et conservés pendant la durée légale d'archivage.",
        "La réponse doit citer devis, commandes, livraisons, heures, situations, factures et réception.")],
    C("Le suivi financier compare engagements et réalisations pour préserver la marge du chantier.",
      "Coût engagé = heures × taux + fournitures · écart = prévu - réel",
      "Situation de travaux · facture finale · archivage des pièces",
      "Planning~Prévision des tâches~Avancement réel~Heures travaillées~Comparaison au devis~Dérive~Situation~Facturation intermédiaire~Travaux avancés",
      "Relever les heures et les tâches réalisées|Suivre les commandes et les dépenses|Comparer au budget prévu|Analyser les écarts et agir|Facturer et archiver les documents",
      "Attendre la fin pour voir les dépassements|Oublier de tracer les heures|Négliger les bons de livraison|Facturer sans réception",
      "80 heures prévues~4000 € de budget~50 heures engagées~2500 € dépensés~60 % réalisés~Estimation 83 heures~Dépassement 150 €",
      "Devant situation~Facture intermédiaire~Avant la fin du chantier~Facture finale~Après réception~Solde du prix~Réserve~Défaut constaté à la réception",
      "Coût prévu~Budget du devis~Coût réel~Dépenses engagées~Marge~Différence prix de vente et coût~Écart~Dérive à corriger"))

# ============================================================ DR1
add("PE-C12", "Contrat de travail et sécurité au travail", "Droit", ["1re pro"],
    S("Le contrat de travail peut être un contrat à durée indéterminée ou à durée déterminée."
      "|Le CDI n'a pas de terme fixé, le CDD prend fin à une date ou après une tâche précise."
      "|Le contrat écrit mentionne l'identité des parties, la fonction, la durée, le salaire et le lieu de travail."
      "|La période d'essai permet à l'employeur et au salarié d'évaluer la collaboration."
      "|Le temps de travail est encadré par la loi et par la convention collective."
      "|Les heures supplémentaires sont compensées par un salaire majoré ou un repos compensateur."
      "|L'employeur doit assurer la santé et la sécurité des salariés."
      "|Le salarié doit respecter les consignes de sécurité et porter les équipements fournis."
      "|Le droit de retrait permet de refuser une situation de danger grave et imminent."
      "|Le comité social et économique, ou CSE, représente les salariés dans l'entreprise."
      "|Une faute professionnelle peut entraîner une sanction disciplinaire proportionnée."
      "|Le règlement intérieur précise les règles de vie et de sécurité dans l'entreprise."),
    [QC("Quel contrat n'a pas de date de fin précise ?", "Le CDD~Le CDI~Le contrat de saison~Le contrat d'apprentissage", 1,
        "Le contrat à durée indéterminée n'est pas limité dans le temps."),
     QC("Que doit mentionner un contrat écrit ?", "La couleur du casque~L'identité des parties, la fonction et le salaire~Le prix des câbles~Le planning des congés de tous", 1,
        "Ces mentions essentielles encadrent la relation de travail."),
     QC("Qui doit assurer la santé et la sécurité au travail ?", "Le seul salarié~L'employeur~Le client~Le fournisseur", 1,
        "L'employeur a une obligation de sécurité envers ses salariés."),
     QC("Qu'appelle-t-on droit de retrait ?", "Le droit de partir à l'heure~Le refus d'une situation de danger grave et imminent~Un congé supplémentaire~Une augmentation", 1,
        "Le salarié peut se retirer face à un danger grave et imminent pour sa vie ou sa santé."),
     QC("Que représente le CSE ?", "Un syndicat de clients~Les représentants des salariés~Un service de vente~Un cabinet comptable", 1,
        "Le comité social et économique est l'instance représentative du personnel."),
     QC("Comment compenser les heures supplémentaires ?", "Par un simple merci~Par un salaire majoré ou un repos compensateur~Par une augmentation de tension~Par un changement de poste", 1,
        "La loi prévoit une majoration de salaire ou un repos compensateur."),
     QC("Où trouve-t-on les règles de vie de l'entreprise ?", "Dans le règlement intérieur~Dans le devis~Dans la facture~Dans le schéma électrique", 0,
        "Le règlement intérieur définit les règles générales de discipline et de sécurité."),
     QT("Expliquer les obligations respectives de l'employeur et du salarié en matière de sécurité.",
        "L'employeur doit évaluer les risques, former les salariés, fournir les équipements de protection adaptés, maintenir les lieux et les machines en bon état et organiser les secours. Le salarié doit respecter les consignes, utiliser correctement les équipements fournis, ne pas les détourner et signaler toute situation dangereuse. Le droit de retrait lui permet de refuser un travail comportant un danger grave et imminent. Ces obligations sont complémentaires : la sécurité repose sur l'organisation de l'entreprise et sur le comportement de chacun.",
        "On attend les devoirs de l'employeur, ceux du salarié et le droit de retrait."),
     QT("Un salarié constate un câble dénudé dans une armoire sous tension. Que doit-il faire ?",
        "Il ne touche pas le conducteur, interrompt la tâche et prévient immédiatement son responsable hiérarchique. Il signale précisément le lieu et la nature du danger. S'il existe un risque grave et imminent, il exerce son droit de retrait et quitte la zone dangereuse en attendant une décision. L'employeur fait consigner le circuit par une personne habilitée et organise la réparation. Après remise en état et vérification, le travail reprend. L'incident et les mesures prises sont consignés dans le registre de sécurité.",
        "La réponse doit citer signalement, droit de retrait si nécessaire, consignation et traçabilité.")],
    C("Le contrat de travail encadre la relation ; la sécurité repose sur des obligations partagées.",
      "CDI sans terme · CDD à terme · droit de retrait pour danger grave et imminent",
      "Employeur : former et protéger · salarié : respecter et signaler",
      "CDI~Sans date de fin~Stabilité~CDD~Durée déterminée~Tâche ou date~Droit de retrait~Danger grave et imminent~Protection du salarié",
      "Identifier le type de contrat|Vérifier les clauses essentielles|Respecter les consignes de sécurité|Signaler tout danger|Consigner les incidents",
      "Croire que le salarié supporte seul la sécurité|Ignorer le droit de retrait|Travailler avec un EPI défectueux|Oublier de signaler un danger",
      "CDI~Sans terme~CDD~Avec terme~CSE~Représentation du personnel~Heures supplémentaires~Majoration ou repos~Règlement intérieur~Règles de vie",
      "Sécurité~Obligation de l'employeur~Prévention et formation~Consignes~Devoir du salarié~Application~Droit de retrait~Protection individuelle face au danger",
      "Sanction~Réponse à une faute~Proportionnée~Faute professionnelle~Manquement aux obligations~Procedures disciplinaires"))

# ============================================================ DR2
add("PE-C13", "Responsabilité et assurance dans l'entreprise", "Droit", ["Terminale pro"],
    S("La responsabilité juridique oblige une personne à réparer le dommage qu'elle a causé."
      "|La responsabilité civile concerne les dommages matériels ou corporels subis par autrui."
      "|La responsabilité pénale sanctionne une violation de la loi, même sans dommage important."
      "|Le contrat d'assurance transfère tout ou partie du risque financier à un assureur."
      "|L'assurance responsabilité civile professionnelle couvre les dommages causés dans l'exercice du métier."
      "|La franchise est la somme laissée à la charge de l'assuré lors d'un sinistre."
      "|La prime est le montant payé à l'assureur pour bénéficier de la couverture."
      "|Une déclaration de sinistre doit être faite dans le délai prévu au contrat."
      "|Les exclusions de garantie précisent les situations non couvertes, comme une faute intentionnelle."
      "|Le chef d'entreprise est responsable de l'organisation de la sécurité de son personnel."
      "|Une installation non conforme peut engager la responsabilité de l'entreprise en cas d'accident."
      "|La traçabilité des interventions et des contrôles constitue une preuve en cas de litige."),
    [QC("Que couvre la responsabilité civile ?", "Les seules amendes~Les dommages causés à autrui~Les impôts~Les salaires", 1,
        "La responsabilité civile vise la réparation des dommages subis par un tiers."),
     QC("Que sanctionne la responsabilité pénale ?", "Un dommage matériel seulement~Une violation de la loi~Un retard de livraison~Une hausse de prix", 1,
        "La responsabilité pénale découle d'une infraction, indépendamment de la réparation."),
     QC("Qu'appelle-t-on franchise ?", "La prime payée à l'assureur~La somme restant à la charge de l'assuré~Le montant du sinistre~La durée du contrat", 1,
        "La franchise est la part non remboursée lors d'un sinistre."),
     QC("Que désigne la prime d'assurance ?", "Le montant payé pour être assuré~La franchise~Le plafond de garantie~Le dommage", 0,
        "La prime est la cotisation versée à l'assureur."),
     QC("Dans quel délai déclarer un sinistre ?", "Quand on veut~Dans le délai prévu au contrat~Jamais~Après trois ans", 1,
        "Le contrat fixe un délai de déclaration dont le non-respect peut entraîner un refus de garantie."),
     QC("Quelle situation est souvent exclue d'une garantie ?", "Un accident de chantier~Une faute intentionnelle~Une panne~Un vol", 1,
        "Les fautes intentionnelles sont généralement exclues des contrats d'assurance."),
     QC("Pourquoi documenter les interventions ?", "Pour faire joli~Pour disposer de preuves en cas de litige~Pour augmenter la prime~Pour éviter les contrôles", 1,
        "Les documents et comptes rendus établissent la réalité des faits."),
     QT("Distinguer responsabilité civile et responsabilité pénale à partir d'un exemple de chantier.",
        "Si un technicien provoque un court-circuit qui détruit l'équipement d'un client, la responsabilité civile de l'entreprise est engagée : elle doit réparer le dommage matériel, souvent par l'intermédiaire de son assurance. Si le même chantier révèle que les consignes de consignation n'ont pas été respectées au point de mettre en danger des salariés, une responsabilité pénale peut être recherchée : elle sanctionne la violation des règles de sécurité, indépendamment du montant du dommage. La première vise la réparation, la seconde la sanction d'une faute contre la loi.",
        "On attend l'opposition réparation du dommage et sanction d'une infraction."),
     QT("Un sinistre survient sur un chantier. Décrire la démarche à suivre avec l'assurance.",
        "On sécurise d'abord les lieux et on porte secours aux personnes si nécessaire. On rassemble les preuves : photos, comptes rendus, schémas, factures et témoignages. On déclare le sinistre à l'assureur dans le délai prévu en indiquant les circonstances et le montant estimé. On transmet les pièces demandées et on laisse l'expert examiner le dommage. On vérifie les garanties, la franchise et les éventuelles exclusions du contrat. Après l'indemnisation, on analyse les causes et on met en place des mesures préventives pour éviter une récidive.",
        "La réponse doit citer sécurisation, preuves, déclaration dans les délais, expertise et prévention.")],
    C("La responsabilité engage la réparation ou la sanction ; l'assurance transfère le risque financier.",
      "Civile = réparer · pénale = sanctionner",
      "Prime · franchise · exclusions · déclaration de sinistre · traçabilité",
      "Responsabilité civile~Réparer un dommage~Assurance~Responsabilité pénale~Sanctionner une infraction~Loi~Prime~Cotisation d'assurance~Payée par l'entreprise",
      "Identifier la nature du dommage|Vérifier les garanties du contrat|Sécuriser et documenter le sinistre|Déclarer dans les délais|Analyser les causes et prévenir",
      "Déclarer tardivement|Ignorer la franchise|Croire que tout est assuré|Supprimer les preuves après l'incident",
      "Dommage matériel~Réparation civile~Faute intentionnelle~Exclusion~Franchise~Part à la charge~Expert~Évaluation du sinistre~PV~Preuve",
      "Responsabilité civile~Dommage subi par autrui~Indemnisation~Responsabilité pénale~Violation de la loi~Amende ou sanction~Responsabilité contractuelle~Non-respect du contrat",
      "Assurance~Transfert du risque~Contrat~Garantie~Situation couverte~Franchise~Somme non remboursée~Exclusion~Situation non couverte"))

# ============================================================ DR3
add("PE-C14", "Confidentialité et propriété intellectuelle", "Droit", ["Terminale pro"],
    S("Une information confidentielle ne doit pas être divulguée à des personnes non autorisées."
      "|Dans une entreprise, les schémas, les prix, les plans et les données clients sont sensibles."
      "|L'obligation de confidentialité peut résulter du contrat de travail ou d'un accord spécifique."
      "|Le secret professionnel interdit de révéler des informations apprises dans le cadre du travail."
      "|Un document technique peut être protégé par le droit d'auteur dès sa création."
      "|Le droit d'auteur confère des droits moraux et des droits patrimoniaux à l'auteur."
      "|Une marque protège un signe distinctif utilisé pour identifier un produit ou une entreprise."
      "|Un brevet protège une invention technique nouvelle pendant une durée limitée."
      "|Copier un logiciel propriétaire sans licence constitue une contrefaçon."
      "|Le RGPD encadre le traitement des données personnelles collectées par l'entreprise."
      "|Les données doivent être collectées pour une finalité précise et conservées le temps nécessaire."
      "|La violation de ces règles peut entraîner des sanctions disciplinaires, civiles ou pénales."),
    [QC("Qu'appelle-t-on information confidentielle ?", "Une information publique~Une information réservée aux personnes autorisées~Une information gratuite~Une information obsolète", 1,
        "La confidentialité limite l'accès à un cercle défini de personnes."),
     QC("Dès quand un document est-il protégé par le droit d'auteur ?", "Après publication~Dès sa création~Après trois ans~Après dépôt obligatoire", 1,
        "La protection naît de la création, sans formalité préalable."),
     QC("Que protège une marque ?", "Une invention technique~Un signe distinctif~Une idée abstraite~Un contrat de travail", 1,
        "La marque identifie l'origine commerciale d'un produit ou service."),
     QC("Que protège un brevet ?", "Une marque~Une invention technique nouvelle~Un document administrative~Un salaire", 1,
        "Le brevet confère un monopole temporaire d'exploitation d'une invention."),
     QC("Que constitue la copie d'un logiciel sans licence ?", "Une simple pratique~Une contrefaçon~Une innovation~Une obligation", 1,
        "La reproduction non autorisée d'une œuvre protégée est une contrefaçon."),
     QC("Quel règlement encadre les données personnelles en Europe ?", "Le RGPD~Le Code de la route~La NF C 15-100~Le traité de Rome", 0,
        "Le règlement général sur la protection des données fixe les règles de traitement."),
     QC("Quelle finalité doit avoir une collecte de données ?", "Une finalité précise et légitime~Une finalité vague~Toutes les finalités possibles~Aucune finalité", 0,
        "Le RGPD impose une finalité déterminée, explicite et légitime."),
     QT("Un client vous demande d'envoyer le schéma interne d'une armoire concurrentielle. Comment réagir ?",
        "On refuse de transmettre un document interne sans autorisation de la direction. On vérifie le cadre contractuel et le motif de la demande. Si le client a besoin d'une information technique légitime, on fournit uniquement la documentation publique ou autorisée, par exemple la notice du matériel. On signale la demande au responsable hiérarchique afin qu'il décide d'une éventuelle communication encadrée. On consigne la demande et la réponse dans le suivi du dossier. Une divulgation non autorisée pourrait engager la responsabilité de l'entreprise et du salarié.",
        "La réponse doit refuser la divulgation, vérifier le cadre et signaler la demande."),
     QT("Expliquer pourquoi la durée de conservation des données doit être limitée.",
        "Le RGPD impose que les données personnelles soient conservées pas plus longtemps que nécessaire pour la finalité poursuivie. Conserver des données au-delà de cette durée augmente le risque de fuite, d'utilisation abusive et de non-conformité. Pour un dossier client, on définit une durée selon les besoins de garantie, de facturation et de maintenance, puis on archive ou on supprime les informations. Une politique de conservation claire documente ces durées. En cas de contrôle de la CNIL, l'entreprise doit pouvoir justifier ses choix.",
        "On attend le lien entre finalité, durée minimale, risque de fuite et conformité au RGPD.")],
    C("Confidentialité et propriété intellectuelle protègent les informations et les créations de l'entreprise.",
      "Droit d'auteur dès la création · marque · brevet · RGPD",
      "Finalité précise · durée de conservation limitée · accès restreint",
      "Confidentialité~Accès restreint~Schémas et prix~Droit d'auteur~Protection dès la création~Œuvre~Brevet~Invention technique~Monopole temporaire",
      "Classer les informations selon leur sensibilité|Vérifier les obligations contractuelles|Limiter l'accès aux personnes autorisées|Respecter les durées de conservation|Signaler toute demande suspecte",
      "Envoyer un schéma interne sans accord|Utiliser un logiciel sans licence|Conserver les données indéfiniment|Mélanger données personnelles et données publiques",
      "RGPD~Données personnelles~Finalité~But de la collecte~Durée~Conservation minimale~Marque~Signe distinctif~Contrefaçon~Copie illicite",
      "Information confidentielle~Accès limité~Divulgation interdite~Information publique~Librement accessible~Documentation commerciale~Secret professionnel~Obligation de discrétion",
      "Droit moral~Lien avec l'auteur~Inaliénable~Droit patrimonial~Exploitation de l'œuvre~Transmissible~Licence~Autorisation d'utilisation"))

# ============================================================ EN1
add("PE-C15", "Electrical installation vocabulary in English", "Anglais technique", ["1re pro"],
    S("Technical English uses precise words for components, actions and safety rules."
      "|A cable is an insulated conductor, while a wire is a single conductive core."
      "|A circuit breaker protects a circuit against overload and short circuit."
      "|A residual current device, or RCD, trips when a leakage current is detected."
      "|The earth wire is called the protective conductor in British terminology."
      "|A terminal is the connection point where a conductor is fixed."
      "|To connect means to join two conductors, while to disconnect means to separate them."
      "|A fuse is a protective device that melts when the current is too high."
      "|A socket is a point where an appliance can be plugged in."
      "|A distribution board contains the protective devices of an installation."
      "|The verb to earth means to connect a metal part to the ground."
      "|Knowing these words is necessary to read a manual and write a report."),
    [QC("What device protects against overload and short circuit ?", "A fuse only~A circuit breaker~A socket~A cable", 1,
        "A circuit breaker protects against overload and short circuit."),
     QC("What does an RCD detect ?", "A high voltage~A leakage current~A low frequency~A burnt fuse", 1,
        "A residual current device trips when current leaks to earth."),
     QC("What is a terminal ?", "A type of cable~A connection point for a conductor~A room~A tool", 1,
        "A terminal is where a conductor is fixed."),
     QC("What does 'to disconnect' mean ?", "To join~To separate~To measure~To earth", 1,
        "To disconnect is to separate an electrical connection."),
     QC("What happens to a fuse when the current is too high ?", "It grows~It melts~It glows~It closes", 1,
        "The fuse element melts and interrupts the circuit."),
     QC("What is a distribution board ?", "A box for tools~The panel containing protective devices~A type of socket~A measuring instrument", 1,
        "The distribution board houses circuit breakers and RCDs."),
     QC("What does 'to earth' mean ?", "To connect to the ground~To raise the voltage~To hide a cable~To test a fuse", 0,
        "To earth is to connect a metal part to the ground for safety."),
     QT("Translate these French terms into English : disjoncteur, prise de courant, conducteur de protection, bornier.",
        "Disjoncteur is circuit breaker, prise de courant is socket or outlet, conducteur de protection is protective conductor or earth wire, and bornier is terminal block. Each term names a precise element of an installation. Using the correct word matters in a manual or a report because a wrong term can lead to a wrong action, for example confusing the conductor that carries current with the conductor that provides protection.",
        "The expected answer is circuit breaker, socket, protective conductor, terminal block."),
     QT("Write three short safety sentences using must, must not and a technical word.",
        "You must check the circuit breaker before starting work. You must not touch a live conductor. The protective conductor must be connected to every metal part. These sentences use the modal must for an obligation and must not for a prohibition. The technical words circuit breaker, live conductor and protective conductor make the instruction unambiguous, which is essential in a safety notice.",
        "The answer must include must, must not and at least one precise technical term.")],
    C("Electrical English relies on exact component names and on clear verbs for actions.",
      "Circuit breaker · RCD · terminal block · protective conductor",
      "To connect / to disconnect · to earth · to trip",
      "Circuit breaker~Protection device~Overload and short circuit~RCD~Leakage current~Trips on fault~Terminal~Connection point~Conductor fixed",
      "Learn the component names|Match each word to its function|Use the correct verb for the action|Write a short safety sentence|Check meaning in a manual",
      "Confusing wire and cable|Using 'disconnect' for 'connect'|Forgetting the article|Translating word for word without checking the context",
      "Circuit breaker~Disjoncteur~RCD~Différentiel~Socket~Prise~Earth wire~Conducteur de protection~Terminal block~Bornier",
      "Cable~Several insulated cores~Wire~Single conductive core~Cord~Flexible cable~Conductor~Metal part carrying current~Insulator~Non-conductive material",
      "To connect~Joining conductors~To disconnect~Separating conductors~To earth~Linking to ground~To trip~Cutting the supply automatically"))

# ============================================================ EN2
add("PE-C16", "Reading an English electrical manual and safety notice", "Anglais technique", ["Terminale pro"],
    S("An electrical manual describes how to install, use and maintain a device safely."
      "|A warning notice identifies a hazard and the consequence of ignoring it."
      "|Common signal words are danger, warning and caution, in decreasing order of severity."
      "|Danger indicates an immediate hazard that will cause death or serious injury."
      "|Warning indicates a potential hazard that could cause serious injury."
      "|Caution indicates a hazard that may cause minor injury or equipment damage."
      "|The imperative form gives direct instructions : Isolate the supply before opening the panel."
      "|Must and must not express obligations and prohibitions in safety instructions."
      "|The passive voice focuses on the action : The cable must be checked before use."
      "|Conditions and exceptions are introduced by if, unless and before."
      "|Technical manuals use short sentences and numbered steps to avoid misunderstanding."
      "|A technician working with an English manual must check each step and never guess a meaning."),
    [QC("Which signal word indicates an immediate danger ?", "Caution~Warning~Danger~Note", 2,
        "Danger is used for an immediate hazard with severe consequences."),
     QC("What does a warning indicate ?", "A minor damage only~A potential hazard with serious consequences~Nothing important~A guaranteed success", 1,
        "Warning covers a potential hazard that could cause serious injury."),
     QC("Which verb form gives a direct instruction ?", "Imperative~Passive~Conditional~Perfect", 0,
        "The imperative gives an order : Switch off the supply."),
     QC("What does 'must not' express ?", "An obligation~A prohibition~A possibility~An advice", 1,
        "Must not expresses something that is forbidden."),
     QC("Why use the passive voice in a manual ?", "To hide the action~To focus on the action rather than the person~To add opinions~To shorten the title", 1,
        "The passive puts the focus on what must be done."),
     QC("Which word introduces an exception ?", "And~Unless~Also~Then", 1,
        "Unless introduces a condition or exception : do not open unless authorised."),
     QC("What should a technician do if a word is unclear ?", "Guess quickly~Check and ask for clarification~Ignore the step~Skip the manual", 1,
        "In safety documentation, an unclear word must never be guessed."),
     QT("Explain the difference between danger, warning and caution in a safety notice.",
        "These three signal words class hazards by severity. Danger is used when an immediate hazard will cause death or serious injury if it is not avoided. Warning indicates a potential hazard that could cause serious injury. Caution indicates a hazard that may cause minor injury or damage to equipment. This hierarchy tells the reader how urgent the information is. A technician must read the signal word first, then the instruction that follows, and comply before starting the task.",
        "The answer must give the decreasing order danger, warning, caution and their meanings."),
     QT("Rewrite these French safety rules in English : 'Coupez l'alimentation avant d'ouvrir le coffret. Ne touchez jamais un conducteur sous tension.'",
        "Isolate the supply before opening the panel. Never touch a live conductor. The first sentence uses the imperative for a direct order and the word before to indicate the sequence. The second uses never with the imperative to express an absolute prohibition. A more formal version would be : The supply must be isolated before the panel is opened, using the passive voice to focus on the action. Both versions are correct, but the instructions must remain short and unambiguous.",
        "The expected answer uses an imperative, a sequence word and an absolute prohibition.")],
    C("A safety notice uses signal words, imperatives and modals to give unambiguous instructions.",
      "Danger > warning > caution · must / must not · imperative",
      "Passive voice for procedures · unless for exceptions",
      "Signal word~Level of hazard~Danger warning caution~Imperative~Direct instruction~Switch off~Passive voice~Focus on the action~Must be checked",
      "Read the signal word first|Identify the hazard and its consequence|Apply must or must not as instructed|Follow the numbered steps in order|Ask if a word is unclear",
      "Skipping a warning because it seems repeated|Guessing the meaning of a technical word|Ignoring the word unless|Working without reading the notice",
      "Danger~Immediate severe hazard~Warning~Potential serious hazard~Caution~Minor injury or damage~Unless~Except if~Before~Sequence word",
      "Danger~Immediate hazard~Severe consequences~Warning~Possible hazard~Serious injury~Caution~Limited hazard~Damage to equipment",
      "Must~Obligation~Must not~Prohibition~Should~Recommendation~May~Permission or possibility"))

# ============================================================ EN3
add("PE-C17", "Professional reports and e-mails in English", "Anglais technique", ["Terminale pro"],
    S("A professional e-mail uses a clear subject line and a polite, structured message."
      "|The subject line summarises the purpose in a few words."
      "|A formal greeting uses Dear followed by the person's name."
      "|The opening sentence states the reason for writing."
      "|The body gives facts in a logical order, with short paragraphs."
      "|A maintenance report records the date, the location, the fault and the action taken."
      "|Reported facts use the past simple because the events are finished."
      "|Measurements are given with their units, for example 230 V or 0,3 A."
      "|A closing sentence states the next step or the expected response."
      "|A formal sign-off uses Yours sincerely when the name is known."
      "|Polite requests use could you or would you rather than a bare imperative."
      "|Checking spelling and technical terms avoids confusion and shows professionalism."),
    [QC("What should a subject line contain ?", "The whole message~A short summary of the purpose~Only the date~Nothing", 1,
        "The subject line states the purpose in a few words."),
     QC("Which greeting is formal when the name is known ?", "Hi~Dear Mr Smith~Hello~Hey", 1,
        "Dear followed by the name is the formal greeting."),
     QC("Which tense reports completed facts in a report ?", "Present simple~Past simple~Future~Present continuous", 1,
        "A report relates finished events and uses the past simple."),
     QC("How should measurements be written ?", "With a unit~Without a unit~In words only~With an adjective", 0,
        "A measurement always includes its unit, such as 230 V."),
     QC("Which phrase makes a request polite ?", "Do it now~Could you check~Check~Must check", 1,
        "Could you is a polite request form."),
     QC("What does a maintenance report record ?", "Only the weather~Date, location, fault and action taken~Only the name~Nothing specific", 1,
        "These elements make the report complete and traceable."),
     QC("Which sign-off is formal when the recipient's name is known ?", "Yours sincerely~Bye~See you~Cheers", 0,
        "Yours sincerely is used with a named recipient."),
     QT("Write a short e-mail to a supervisor reporting a faulty circuit breaker.",
        "Subject : Faulty circuit breaker in panel B. Dear Mr Martin, I am writing to report a fault on circuit breaker Q4 in distribution panel B. Yesterday afternoon, the breaker tripped three times without any load change. I isolated the circuit and measured the insulation resistance, which was below the expected value. The cable to socket 7 appears to be damaged. I have not restored power. Could you please confirm whether we should replace the cable or call the supplier? Yours sincerely, Alex Dupont. The message states the purpose, gives facts in order and ends with a polite request.",
        "The answer should include a subject, a greeting, facts in past simple, a polite request and a sign-off."),
     QT("Why is precision important in a written technical report ?",
        "A report may be read by people who were not present on site. Precise dates, locations, component references and measurements allow them to understand what happened and to decide what to do next. Vague words such as something or probably can lead to a wrong decision or to unnecessary work. Precision also protects the company if the report is used as evidence in a dispute. Finally, a clear report supports maintenance history and helps prevent the same fault from happening again.",
        "The answer must mention absent readers, decision-making, traceability and evidence.")],
    C("A professional e-mail and a report state facts precisely, in order and with polite/formal language.",
      "Subject → greeting → reason → facts → request → sign-off",
      "Past simple for facts · units for measurements · could you for requests",
      "Subject line~Purpose in a few words~Greeting~Dear and name~Maintenance report~Date, fault and action~Facts~Past simple and units",
      "Write a clear subject line|State the reason in the first sentence|Give facts in chronological order|Use past simple and exact units|Close with a request or next step",
      "Using vague words|Omitting units|Mixing tenses without reason|Forgetting the name in the sign-off",
      "230 V~Measurement with unit~0,3 A~Current value~Dear Mr Martin~Formal greeting~Could you~Polite request~Yours sincerely~Formal sign-off",
      "E-mail~Fast written communication~Short and structured~Maintenance report~Record of an intervention~Traceable~Memo~Internal note~Concise",
      "Polite request~Could you, would you~Indirect form~Direct order~Imperative~Used for instructions~Formal sign-off~Yours sincerely"))

# ============================================================ DD1
add("PE-C18", "Efficacité énergétique des installations", "Développement durable", ["1re pro"],
    S("L'efficacité énergétique vise à obtenir un service donné en consommant moins d'énergie."
      "|Un bâtiment consomme de l'énergie pour l'éclairage, le chauffage, la ventilation et les équipements."
      "|Un audit énergétique recense les usages et quantifie les gaspillages."
      "|Le diagnostic permet de classer les postes de consommation par ordre d'importance."
      "|Remplacer une lampe incandescente par une LED réduit fortement la consommation d'éclairage."
      "|Une LED consomme moins d'électricité et a une durée de vie plus longue."
      "|L'éclairagenaturel et les détecteurs de présence limitent les heures de fonctionnement."
      "|L'isolation thermique réduit le besoin de chauffage et de climatisation."
      "|La regulation commande le chauffage en fonction de la température et de l'occupation."
      "|Un moteur à haut rendement consomme moins d'électricité pour la même puissance mécanique."
      "|La compensation de l'énergie réactive réduit les pertes dans les câbles et les transformateurs."
      "|Le retour sur investissement compare le coût de l'investissement aux économies annuelles."),
    [QC("Que vise l'efficacité énergétique ?", "À consommer plus~À obtenir le même service avec moins d'énergie~À supprimer l'électricité~À augmenter la facture", 1,
        "L'objectif est de réduire l'énergie nécessaire à un service identique."),
     QC("Que permet un audit énergétique ?", "De recenser les usages et les gaspillages~De changer la tension~De supprimer les schémas~D'augmenter la puissance", 0,
        "L'audit identifie les postes de consommation et les pertes."),
     QC("Quel est l'avantage d'une LED par rapport à une lampe incandescente ?", "Elle chauffe plus~Elle consomme moins et dure plus longtemps~Elle est plus fragile~Elle éclaire moins", 1,
        "La LED a un meilleur rendement lumineux et une longue durée de vie."),
     QC("Comment limiter les heures d'éclairage ?", "Par des détecteurs de présence~En augmentant la puissance~En laissant allumé~En changeant la couleur", 0,
        "Les détecteurs et la commande réduisent le temps de fonctionnement."),
     QC("Que réduit une bonne isolation thermique ?", "La consommation de chauffage~La tension~La fréquence~Le nombre de prises", 0,
        "Moins de pertes thermiques signifie moins de besoins de chauffage."),
     QC("Quel effet a la compensation de l'énergie réactive ?", "Elle augmente les pertes~Elle réduit les pertes dans les câbles~Elle change la fréquence~Elle supprime la terre", 1,
        "Améliorer le cos phi diminue le courant et donc les pertes R I²."),
     QC("Que mesure le retour sur investissement ?", "La couleur de l'équipement~Le temps nécessaire pour rembourser l'investissement par les économies~La tension~La durée du chantier", 1,
        "Il compare le coût initial aux économies annuelles obtenues."),
     QT("Une LED de 10 W remplace une lampe incandescente de 60 W, allumée 4 h par jour. Calculer l'économie annuelle d'énergie et le coût évité à 0,20 € le kWh.",
        "L'écart de puissance vaut 60 - 10 = 50 W, soit 0,05 kW. Sur 4 heures quotidiennes, l'économie est 0,05 × 4 = 0,2 kWh par jour. Sur un an, soit 365 jours, elle atteint 0,2 × 365 = 73 kWh. Au tarif de 0,20 € le kWh, le coût évité est 73 × 0,20 = 14,60 € par an. Si la LED coûte 8 € et dure plusieurs années, le retour sur investissement est court, ce qui justifie le remplacement.",
        "On attend la différence de puissance, la conversion en kWh et le calcul du coût annuel."),
     QT("Proposer une démarche d'amélioration de l'efficacité énergétique pour un atelier.",
        "On réalise d'abord un audit pour mesurer les consommations par poste : éclairage, chauffage, moteurs et outils. On classe les postes par importance et on identifie les gaspillages, comme un éclairage allumé en permanence ou des moteurs surdimensionnés. On met en œuvre les actions les plus rentables : LED, détecteurs de présence, regulation du chauffage, compensation du cos phi et moteurs à haut rendement. On mesure à nouveau les consommations pour vérifier les gains. On calcule le retour sur investissement et on sensibilise les utilisateurs, car leur comportement conditionne les résultats.",
        "La réponse doit proposer audit, priorisation, actions concrètes, mesure et sensibilisation.")],
    C("L'efficacité énergétique réduit les consommations à service égal et diminue les coûts.",
      "Économie = (P ancienne - P nouvelle) × durée",
      "Audit · LED · détecteurs · isolation · cos phi · retour sur investissement",
      "Audit énergétique~Recensement des usages~Gaspillages~Efficacité~Même service moins d'énergie~LED~Faible consommation~Longue durée de vie~Rendement",
      "Mesurer les consommations par usage|Classer les postes les plus coûteux|Choisir des actions rentables|Réaliser les travaux|Remesurer et sensibiliser",
      "Remplacer sans mesurer|Ignorer le comportement des utilisateurs|Confondre puissance et énergie|Oublier le coût réel de l'investissement",
      "60 W vers 10 W~Écart 50 W~4 h par jour~0,2 kWh par jour~73 kWh par an~14,60 € économisés~Retour sur investissement~Coût initial récupéré",
      "Efficacité énergétique~Moins d'énergie pour un service~Sobriété~Réduction des usages~Besoins modérés~Confort maintenu~Audit~Diagnostic chiffré",
      "Puissance~Watt~Énergie~kWh~Facture~Coût de la consommation~Économie~Différence avant après"))

# ============================================================ DD2
add("PE-C19", "Énergies renouvelables et réseaux", "Développement durable", ["Terminale pro"],
    S("Les énergies renouvelables utilisent des sources qui se renouvellent à l'échelle humaine."
      "|Le solaire photovoltaïque convertit directement la lumière du soleil en électricité."
      "|Un module photovoltaïque est constitué de cellules semi-conductrices assemblées."
      "|La puissance d'un module dépend de l'ensoleillement et de sa surface."
      "|Un onduleur convertit le courant continu produit par les panneaux en courant alternatif."
      "|L'énergie éolienne transforme l'énergie cinétique du vent en énergie mécanique puis électrique."
      "|Une éolienne possède un rotor, une nacelle, un mât et un générateur."
      "|La production d'énergie renouvelable est variable et dépend de la météo."
      "|Le stockage par batteries permet de décaler la production et la consommation."
      "|Un réseau intelligent, ou smart grid, pilote les flux grâce à des capteurs et des automatismes."
      "|Le raccordement au réseau impose des règles de qualité et de sécurité strictes."
      "|Le mix énergétique associe plusieurs sources pour garantir la continuité de l'alimentation."),
    [QC("Que convertit un module photovoltaïque ?", "La chaleur en électricité~La lumière en électricité~Le vent en chaleur~L'eau en courant continu", 1,
        "L'effet photovoltaïque convertit directement la lumière en courant continu."),
     QC("Quel appareil convertit le courant continu des panneaux en courant alternatif ?", "Un transformateur~Un onduleur~Un redresseur~Un disjoncteur", 1,
        "L'onduleur assure la conversion continu vers alternatif."),
     QC("Quelle source d'énergie utilise une éolienne ?", "Le soleil~L'énergie cinétique du vent~La chaleur de la Terre~La marée", 1,
        "Le vent met en rotation le rotor qui entraîne le générateur."),
     QC("Quelle est une limite des énergies renouvelables ?", "Elles sont illimitées~Leur production est variable~Elles ne produisent pas d'électricité~Elles sont interdites", 1,
        "L'ensoleillement et le vent varient : la production est intermittente."),
     QC("À quoi sert le stockage par batteries ?", "À augmenter la tension~À décaler production et consommation~À supprimer l'onduleur~À chauffer le bâtiment", 1,
        "Les batteries stockent l'énergie produite pour la restituer plus tard."),
     QC("Qu'appelle-t-on un réseau intelligent ?", "Un réseau sans câbles~Un réseau piloté par capteurs et automatismes~Un réseau de transport~Un réseau fermé", 1,
        "Le smart grid gère les flux en temps réel grâce à l'information."),
     QC("Qu'est-ce qu'un mix énergétique ?", "Une source unique~L'association de plusieurs sources d'énergie~Un seul fournisseur~Une batterie", 1,
        "La combinaison des sources assure la sécurité d'approvisionnement."),
     QT("Expliquer le rôle de l'onduleur dans une installation photovoltaïque.",
        "Les modules photovoltaïques produisent un courant continu dont la tension varie avec l'ensoleillement. Or le réseau public et la plupart des appareils utilisent un courant alternatif à 50 Hz. L'onduleur convertit le courant continu en courant alternatif synchrone avec le réseau. Il règle également la tension et le facteur de puissance, et il coupe la production en cas de défaut ou de coupure du réseau, pour éviter toute réalimentation dangereuse. Il assure enfin le suivi du point de puissance maximale afin d'extraire le plus d'énergie possible des modules.",
        "On attend conversion continu-alternatif, synchronisation, protection et optimisation de la production."),
     QT("Une installation photovoltaïque de 3 kW produit en moyenne 4 heures nominales par jour. Calculer l'énergie produite sur un an et comparer avec une consommation de 2500 kWh.",
        "L'énergie quotidienne vaut 3 kW × 4 h = 12 kWh. Sur une année de 365 jours, la production atteint 12 × 365 = 4380 kWh. Cette production dépasse la consommation annuelle de 2500 kWh, donc l'installation est excédentaire sur l'année. En réalité, la production et la consommation ne coïncident pas : il faut soit stocker l'énergie dans des batteries, soit l'injecter dans le réseau. Le calcul montre l'intérêt d'une gestion intelligente des flux et d'un dimensionnement adapté du stockage.",
        "On attend production journalière, production annuelle et comparaison avec la consommation.")],
    C("Les renouvelables produisent une énergie variable qu'il faut convertir, stocker et piloter.",
      "Photovoltaïque : lumière → continu → onduleur → alternatif",
      "Éolien : vent → rotation → générateur · stockage et smart grid",
      "Photovoltaïque~Lumière en courant continu~Module~Onduleur~Continu vers alternatif~Réseau~Éolienne~Vent en électricité~Rotor et générateur",
      "Évaluer la ressource solaire ou éolienne|Dimensionner les modules|Choisir l'onduleur adapté|Prévoir stockage ou injection|Respecter les règles de raccordement",
      "Croire que la production est constante|Oublier l'onduleur|Ignorer la coupure en cas de défaut réseau|Surdimensionner sans étude",
      "3 kW et 4 h~12 kWh par jour~4380 kWh par an~Consommation 2500 kWh~Excédent~Stockage~Injection au réseau~Smart grid",
      "Énergie renouvelable~Source qui se renouvelle~Solaire et éolien~Énergie fossile~Ressource limitée~Charbon et pétrole~Intermittence~Production variable",
      "Réseau intelligent~Capteurs et pilotage~Smart grid~Réseau classique~Flux unidirectionnel~Distribution simple~Stockage~Décalage dans le temps"))

# ============================================================ DD3
add("PE-C20", "Déchets électriques et recyclage", "Développement durable", ["2nde pro"],
    S("Les déchets électriques et électroniques, ou DEEE, comprennent les appareils et les câbles usagés."
      "|Ils contiennent des matériaux valorisables comme le cuivre, l'aluminium, l'acier et les plastiques."
      "|Certains composants contiennent des substances dangereuses pour la santé et l'environnement."
      "|Une filière de récupération organisée collecte et traite ces déchets séparément des ordures ménagères."
      "|Le principe du pollueur-payeur fait supporter le coût de la gestion des déchets aux producteurs."
      "|Une démarche de responsabilité étendue du producteur oblige le fabricant à organiser la fin de vie."
      "|Le tri à la source facilite le recyclage en séparant les matériaux dès le chantier."
      "|Les câbles sont dénudés ou broyés pour récupérer le cuivre."
      "|Les batteries et les accumulateurs nécessitent une collecte spécifique."
      "|Les lampes contenant du mercure ne doivent pas être jetées avec les déchets ordinaires."
      "|La réduction des déchets commence par une commande ajustée et une découpe optimisée des câbles."
      "|Le suivi des déchets par bordereau permet de tracer leur destination finale."),
    [QC("Que désigne un DEEE ?", "Un déchet de chantier ordinaire~Un déchet électrique ou électronique~Un déchet alimentaire~Un déchet de papier", 1,
        "DEEE signifie déchets d'équipements électriques et électroniques."),
     QC("Quel matériau valorisable contient un câble électrique ?", "Du verre~Du cuivre~Du bois~Du plâtre", 1,
        "Le cuivre du conducteur est récupéré après dénudage ou broyage."),
     QC("Quel principe fait supporter le coût des déchets aux producteurs ?", "Pollueur-payeur~Utilisateur-payeur~Concrete-payeur~Réseau-payeur", 0,
        "Le principe pollueur-payeur internalise le coût environnemental."),
     QC("Pourquoi trier les déchets dès le chantier ?", "Pour augmenter le volume~Pour faciliter le recyclage~Pour éviter les étiquettes~Pour changer la tension", 1,
        "Le tri à la source améliore la qualité des matériaux récupérés."),
     QC("Quel déchet nécessite une collecte spécifique ?", "Un carton~Une batterie~Un morceau de bois~Une vis", 1,
        "Les batteries contiennent des substances dangereuses et doivent être collectées séparément."),
     QC("Comment réduire les déchets de câbles ?", "En commandant trop~En optimisant la découpe et les longueurs~En jetant les chutes~En utilisant plus de gaines", 1,
        "Une découpe raisonnée limite les chutes et les surplus."),
     QC("Que permet un bordereau de suivi ?", "De tracer la destination des déchets~D'augmenter la tension~De supprimer le tri~De remplacer le devis", 0,
        "Le bordereau atteste de la collecte et du traitement des déchets."),
     QT("Expliquer pourquoi les déchets électriques ne doivent pas être mélangés aux ordures ménagères.",
        "Les équipements électriques contiennent des métaux précieux comme le cuivre et l'or, mais aussi des substances dangereuses comme le mercure, le plomb ou certains retardateurs de flamme. Mélangés aux ordures ménagères, ils sont enfouis ou incinérés, ce qui gaspille des ressources et peut libérer des polluants. Une filière dédiée permet de récupérer les matériaux valorisables et de traiter les composants sensibles en toute sécurité. Le tri à la source et le bordereau de suivi garantissent que les déchets arrivent dans une filière autorisée et non dans un circuit illégal.",
        "On attend les risques de pollution, la perte de ressources et l'intérêt d'une filière dédiée."),
     QT("Comment un électricien peut-il réduire les déchets sur un chantier ?",
        "Il commande les matériels au plus juste après avoir relevé les longueurs réelles sur les plans. Il optimise la découpe des câbles en regroupant les longueurs similaires et en réutilisant les chutes exploitables. Il conserve les emballages et les étiquettes pour garantir la traçabilité. Il sépare dès le chantier les métaux, les plastiques, les batteries et les lampes spéciales. Il rapporte les matériels non utilisés au magasin pour les réaffecter. Enfin, il remplit le bordereau de suivi pour prouver que les déchets ont été confiés à une filière autorisée.",
        "La réponse doit citer commande ajustée, découpe optimisée, tri, réutilisation et traçabilité.")],
    C("Un déchet électrique est une ressource mal placée : le trier permet de le valoriser en toute sécurité.",
      "DEEE · pollueur-payeur · responsabilité étendue du producteur",
      "Tri à la source · cuivre récupéré · batteries et lampes en filière dédiée · bordereau",
      "DEEE~Équipements électriques usagés~Filière dédiée~Cuivre~Métal valorisable~Récupération~Tri à la source~Séparation dès le chantier~Recyclage",
      "Estimer les quantités avant commande|Optimiser la découpe des câbles|Trier les matériaux sur site|Confier les déchets à une filière autorisée|Remplir le bordereau de suivi",
      "Jeter les câbles avec les ordures|Mélanger batteries et déchets ordinaires|Commander sans mesurer|Perdre le bordereau de traçabilité",
      "Longueurs relevées~Commande ajustée~Chutes réutilisées~Cuivre~Valorisation~Batterie~Collecte spécifique~Bordereau~Destination tracée",
      "Déchet~Objet destiné à être éliminé~Fin de vie~Ressource~Matériau valorisable~Réintroduction~Filière~Circuit de collecte et de traitement",
      "Pollueur-payeur~Coût supporté par le producteur~Responsabilité étendue~Fabricant responsable de la fin de vie~Tri à la source~Séparation initiale"))

valider_et_ecrire(F, "pro-electricite-mat-part-C.json")
