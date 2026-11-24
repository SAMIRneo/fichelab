# -*- coding: utf-8 -*-
"""Generateur btsciel-mat-part-B.json — lot B : Droit (7), Economie (7), Management (6).

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

# ============================================================ DR1
add("DR1", "Cyberdroit : principes juridiques du numérique", "Droit", ["BTS1"],
S("Le cyberdroit est l'ensemble des règles juridiques applicables aux systèmes d'information, aux données et aux usages d'Internet."
  "|Il emprunte au droit civil, au droit pénal, au droit de la propriété intellectuelle et au droit européen, car les faits numériques ne forment pas une branche autonome."
  "|Le Code civil, issu de la réforme du 17 février 2015, consacre la protection de la vie privée et la liberté d'expression, valeurs souvent en tension en ligne."
  "|La loi pour la confiance dans l'économie numérique du 21 juin 2004 (LCEN) organise la responsabilité des hébergeurs et des fournisseurs d'accès."
  "|Les hébergeurs ne sont pas responsables des contenus qu'ils stockent s'ils n'ont pas connaissance de leur caractère illicite et agissent promptement pour les retirer."
  "|La loi du 29 juillet 1881 sur la liberté de la presse encadre la diffamation et l'injure publiques, y compris sur les réseaux sociaux."
  "|Le Code pénal réprime l'accès frauduleux à un système informatique, le maintien dans le système, l'altération de données et l'extorsion."
  "|La CNIL contrôle le respect de la loi Informatique et Libertés et du RGPD ; elle peut mettre en demeure, sanctionner et saisir le parquet."
  "|L'ANSSI agit sur la sécurité des systèmes d'information et la réglementation des activités de sécurité, notamment pour les opérateurs d'importance vitale."
  "|Le droit applicable dépend du lieu de l'acteur, du lieu du serveur et de la localisation des personnes concernées : les conflits de lois sont fréquents."
  "|Le règlement eIDAS (UE n° 910/2014) encadre l'identification électronique, les signatures et les cachets électroniques, avec une valeur juridique équivalente à l'écrit papier."
  "|Pour un technicien CIEL, connaître ces repères permet d'identifier le risque juridique d'une intervention et de documenter les preuves en cas d'incident."),
[QC("La cyberdroit est-il une branche autonome du droit ?", "Oui, avec un code unique~Non, il emprunte à plusieurs branches~Oui, mais seulement en Europe~Non, il n'existe pas", 1,
     "Il croise droit civil, pénal, propriété intellectuelle et droit de l'Union européenne."),
 QC("Quelle loi organisme la responsabilité des hébergeurs en France ?", "La loi du 29 juillet 1881~La LCEN du 21 juin 2004~Le Code de commerce~La loi de 1978 sur les archives", 1,
     "La loi pour la confiance dans l'économie numérique fixe le régime de responsabilité des hébergeurs."),
 QC("Dans quel cas un hébergeur est-il responsable d'un contenu illicite ?", "Dès sa publication~S'il a connaissance du contenu et ne le retire pas~Jamais~Uniquement si le contenu est une image", 1,
     "La LCEN prévoit une obligation de retrait prompt après connaissance effective."),
 QC("Quel texte réprime l'accès frauduleux à un système informatique ?", "Le Code civil~Le Code pénal~Le Code du travail~Le Code de la route", 1,
     "Les atteintes à l'intégrité et à la confidentialité des systèmes sont des délits pénaux."),
 QC("Quelle autorité contrôle la protection des données personnelles en France ?", "L'ANSSI~La CNIL~L'ARCEP~La BCE", 1,
     "La CNIL est l'autorité de contrôle compétente pour le RGPD en France."),
 QC("Quel règlement européen encadre la signature électronique ?", "RGPD~eIDAS~GDPR~RoHS", 1,
     "Le règlement eIDAS n° 910/2014 définit les niveaux de signature électronique et leur valeur juridique."),
 QC("Pourquoi le droit applicable peut-il varier pour un même incident ?", "Parce que le juge choisit au hasard~Parce que lieu de l'acteur, des données et des serveurs peuvent différer~Parce que le droit numérique n'existe pas~Parce que les ordinateurs sont mobiles", 1,
     "La localisation des éléments de l'infraction détermine les règles et les juridictions compétentes."),
 QC("Quel réflexe professionnel attendu d'un technicien face à un incident ?", "Supprimer immédiatement les journaux~Documenter les faits et préserver les preuves~Redémarrer tous les serveurs~Ne rien signaler", 1,
     "La conservation des preuves et la traçabilité sont indispensables à toute action juridique."),
 QT("Expliquer pourquoi un incident de sécurité peut avoir à la fois une dimension pénale et une dimension civile.",
    "Sur le plan pénal, un accès non autorisé, une altération de données ou un déni de service constituent des infractions poursuivies par le parquet, qui peuvent aboutir à une condamnation et à une peine. Sur le plan civil, la même situation peut causer un préjudice à une personne ou à une entreprise : perte de données, interruption d'activité, atteinte à la réputation. La victime peut alors demander réparation en dommages-intérêts sur le fondement de la responsabilité contractuelle ou délictuelle. Les deux voies sont indépendantes et peuvent se cumuler : un même fait déclenche une action publique et une action privée, avec des preuves et des finalités différentes.",
    "On distingue la répression des infractions de la réparation du préjudice, en montrant qu'elles peuvent se cumuler."),
 QT("Un salarié découvre une fuite de données clients. Décrire les bons réflexes juridiques et techniques dans l'immédiat.",
    "Il doit d'abord préserver les éléments de preuve : ne pas effacer les journaux, conserver les captures d'écran et les hashes des fichiers suspects, noter les horaires. Il signale sans délai l'incident au responsable hiérarchique et au délégué à la protection des données, conformément à la procédure interne. Techniquement, il confine la fuite (révocation des accès, isolement du service) sans détruire les traces. Il n'informe pas lui-même les clients ni la presse : la communication est pilotée par l'entreprise et le DPO, qui apprécient la notification à la CNIL dans les 72 heures et l'information des personnes concernées. Enfin, il consigne toutes ses actions dans un compte rendu daté.",
    "On attend : préservation des preuves, signalement interne, confinement, notification pilotée par le DPO et traçabilité.")],
C("Le cyberdroit croise plusieurs branches : pour un incident, il faut identifier les règles applicables, les autorités compétentes et les preuves à conserver.",
  "Responsabilité de l'hébergeur = connaissance + absence de retrait prompt",
  "Code pénal · LCEN 2004 · RGPD · eIDAS · CNIL · ANSSI",
  "Droit civil~Réparation du préjudice~Droit pénal~Répression des infractions~LCEN~Responsabilité des hébergeurs~eIDAS~Signature électronique~CNIL~Contrôle des données",
  "Identifier les faits et les acteurs|Repérer les textes applicables|Préserver les preuves|Signaler aux autorités internes|Documenter chaque action",
  "Supprimer des journaux pour « nettoyer »|Communiquer publiquement sans validation|Ignorer la dimension européenne|Confondre CNIL et ANSSI",
  "72 h~Notification RGPD à la CNIL~Hébergeur~Retrait prompt~eIDAS~Valeur de l'écrit~ANSSI~Sécurité des SI~Code pénal~Délits informatiques",
  "Voie pénale~Sanctionner l'auteur~Voie civile~Réparer la victime",
  "CNIL~Données personnelles~ANSSI~Sécurité des systèmes"))

# ============================================================ DR2
add("DR2", "RGPD : principes, rôles et obligations de conformité", "Droit", ["BTS1"],
S("Le règlement général sur la protection des données (UE 2016/679), applicable depuis le 25 mai 2018, harmonise la protection des personnes physiques dans l'Union européenne."
  "|Il s'applique à tout traitement de données personnelles effectué par un responsable de traitement établi dans l'UE ou ciblant des personnes dans l'UE."
  "|Une donnée personnelle est toute information relative à une personne physique identifiée ou identifiable, directement ou indirectement."
  "|Les principes fondamentaux sont la licéité, la loyauté, la transparence, la limitation des finalités, la minimisation des données, l'exactitude, la limitation de la conservation, l'intégrité et la confidentialité, ainsi que la responsabilité."
  "|Le responsable de traitement détermine les finalités et les moyens ; le sous-traitant agit pour son compte selon un contrat écrit conforme à l'article 28."
  "|Le délégué à la protection des données (DPO) est désigné dans les cas prévus à l'article 37 : secteur public, surveillance régulière et systématique ou traitement de données sensibles à grande échelle."
  "|Les bases légales du traitement sont le consentement, l'exécution du contrat, l'obligation légale, l'intérêt vital, la mission d'intérêt public et l'intérêt légitime."
  "|Les données sensibles (santé, opinions, origine, religion, données biométriques) relèvent d'un régime renforcé, avec une dérogation prévue à l'article 9."
  "|Les personnes disposent de droits : information, accès, rectification, effacement, limitation, portabilité, opposition et droit de ne pas être soumises à une décision automatisée."
  "|Le responsable doit tenir un registre des traitements, réaliser une analyse d'impact (AIPD) pour les traitements à risque élevé et notifier les violations à la CNIL dans les 72 heures."
  "|Par défaut, la protection doit être intégrée dès la conception et la sécurité assurée « by design and by default » (article 25)."
  "|Le non-respect du RGPD expose à des sanctions administratives pouvant atteindre 20 millions d'euros ou 4 % du chiffre d'affaires annuel mondial."),
[QC("Quand le RGPD est-il devenu applicable ?", "25 mai 2018~1er janvier 2016~6 janvier 1978~25 janvier 2023", 0,
     "Le règlement est applicable depuis le 25 mai 2018."),
 QC("Qui détermine les finalités et les moyens d'un traitement ?", "Le sous-traitant~Le responsable de traitement~L'hébergeur~Le fournisseur d'accès", 1,
     "Le responsable de traitement définit le pourquoi et le comment ; le sous-traitant exécute."),
 QC("Quelle base légale repose sur l'accord libre et éclairé de la personne ?", "L'intérêt légitime~Le consentement~L'obligation légale~La mission publique", 1,
     "Le consentement doit être libre, spécifique, éclairé et univoque, et retirable à tout moment."),
 QC("Quel délai pour notifier une violation de données à la CNIL ?", "24 h~72 h~7 jours~1 mois", 1,
     "L'article 33 impose une notification dans les 72 heures suivant la connaissance de la violation."),
 QC("Quel montant maximal de sanction prévoit le RGPD ?", "20 000 €~2 millions d'euros ou 2 %~20 millions d'euros ou 4 %~100 millions d'euros", 2,
     "Le plafond est de 20 M€ ou 4 % du chiffre d'affaires annuel mondial."),
 QC("Qu'est-ce que la minimisation des données ?", "Collecter le maximum d'informations~Limiter la collecte au strict nécessaire~Supprimer toutes les données~Chiffrer les sauvegardes", 1,
     "On ne collecte que les données nécessaires aux finalités déclarées."),
 QC("Quel document contractualise la relation avec un sous-traitant ?", "Un simple courriel~Un contrat conforme à l'article 28~Une note de service~Un devis", 1,
     "L'article 28 impose un contrat ou acte juridique écrit qui encadre le sous-traitant."),
 QC("Quel droit permet d'obtenir une copie de ses données ?", "Droit à l'oubli~Droit d'accès~Droit d'opposition~Droit à la portabilité", 1,
     "Le droit d'accès (article 15) donne communication des données et des informations sur le traitement."),
 QT("Une entreprise veut installer un nouveau logiciel RH qui traite des données de santé des salariés. Décrire les étapes de conformité RGPD.",
    "Elle identifie d'abord le responsable de traitement, les finalités et les catégories de données, puis vérifie la base légale : les données de santé sont sensibles et relèvent de l'article 9, avec une dérogation à documenter. Elle met à jour le registre des traitements et réalise une analyse d'impact (AIPD) car le traitement est sensible et à grande échelle. Elle vérifie le contrat de sous-traitance avec l'éditeur (article 28), la localisation des données et les mesures techniques (chiffrement, contrôle d'accès, journalisation). Elle informe les salariés via une notice claire, limite les accès aux seules personnes habilitées et prévoit la durée de conservation. Enfin, elle teste la gestion des droits (accès, effacement) et la procédure de notification des violations.",
    "On attend : finalités et base légale, registre, AIPD, sous-traitance, information, minimisation, sécurité et droits."),
 QT("Expliquer la différence entre responsable de traitement et sous-traitant, et pourquoi cette distinction est importante.",
    "Le responsable de traitement décide des finalités et des moyens : il porte la responsabilité principale de la conformité et répond de ses choix devant la CNIL et les personnes concernées. Le sous-traitant traite les données pour son compte, uniquement selon ses instructions écrites, avec une obligation de confidentialité et de sécurité. Cette distinction est essentielle car elle détermine qui doit tenir le registre, informer les personnes, réaliser l'AIPD et notifier les violations. Elle encadre aussi le contrat : si le sous-traitant décide lui-même d'une finalité, il devient responsable de traitement et engage sa propre responsabilité.",
    "On oppose la décision des finalités à l'exécution, puis on en déduit les obligations et la responsabilité.")],
C("Le RGPD impose une conformité démontrable : finalités claires, données minimales, droits des personnes et sécurité dès la conception.",
  "Sanction maximale : 20 M€ ou 4 % du CA mondial",
  "Bases légales · registre des traitements · AIPD · DPO · notification 72 h",
  "Responsable~Décide finalités et moyens~Sous-traitant~Agite selon le contrat~DPO~Veille à la conformité~Registre~Inventaire des traitements~AIPD~Analyse d'impact",
  "Recenser les traitements|Vérifier la base légale|Informer les personnes|Encadrer les sous-traitants|Mesurer et documenter la conformité",
  "Collecter « au cas où »|Conserver indéfiniment les données|Consentement coercitif|AIPD réalisée après coup",
  "25 mai 2018~Date d'application~72 h~Notification de violation~20 M€ ou 4 %~Plafond de sanction~Article 28~Contrat de sous-traitance~Article 9~Données sensibles",
  "Responsable de traitement~Porte la responsabilité~Sous-traitant~Exécute sous contrôle",
  "Consentement~Accord éclairé~Intérêt légitime~Base alternative"))

# ============================================================ DR3
add("DR3", "Propriété intellectuelle et logicielle", "Droit", ["BTS1"],
S("La propriété intellectuelle protège les créations de l'esprit : elle se divise en propriété littéraire et artistique, droit d'auteur, et propriété industrielle, brevets et marques."
  "|Le droit d'auteur naît automatiquement de la création d'une œuvre originale, sans formalité : un code source, une documentation ou une interface graphique peuvent être protégés."
  "|L'auteur dispose de droits moraux inaliénables (paternité, intégrité de l'œuvre) et de droits patrimoniaux cessibles (reproduction, représentation, adaptation)."
  "|La durée de protection des droits patrimoniaux est en principe de 70 ans après la mort de l'auteur."
  "|Un logiciel est protégé comme une œuvre littéraire : la protection porte sur l'expression du code, non sur les idées ou algorithmes sous-jacents."
  "|La directive 2009/24/CE couvre la protection juridique des programmes d'ordinateur ; en France, l'article L. 112-2 du Code de la propriété intellectuelle les mentionne."
  "|Un contrat de licence définit les droits d'utilisation : périmètre, nombre d'utilisateurs, durée, territoire et limitations (modification, redistribution, rétro-ingénierie)."
  "| Les licences libres (GPL, MIT, Apache 2.0, AGPL) autorisent l'usage et la modification selon des conditions précises ; la GPL impose la redistribution du code modifié sous licence équivalente."
  "|La licence AGPL étend l'obligation de partage aux services réseau accessibles par un utilisateur, ce qui est critique pour un SaaS."
  "|Le brevet protège une invention technique nouvelle, inventive et industriellement applicable pour 20 ans, mais les logiciels en tant que tels sont généralement exclus."
  "|La marque protège les signes distinctifs ; le secret des affaires protège les informations confidentielles à condition de mesures de protection raisonnables."
  "|Dans un projet CIEL, vérifier la licence des dépendances et tenir une nomenclature (SBOM) évite les risques de contamination et de non-conformité."),
[QC("Le droit d'auteur naît-il d'un dépôt légal ?", "Oui, après dépôt~Non, dès la création originale~Oui, après publication~Oui, après enregistrement INPI", 1,
     "La protection est automatique dès la création d'une œuvre originale."),
 QC("Quelle durée de protection des droits patrimoniaux en principe ?", "20 ans~50 ans~70 ans après la mort de l'auteur~Illimitée", 2,
     "Les droits patrimoniaux durent en principe 70 ans après le décès de l'auteur."),
 QC("Que protège le droit d'auteur dans un logiciel ?", "Les idées~L'expression du code source~Les algorithmes abstraits~Les fonctionnalités seules", 1,
     "Le droit d'auteur protège la forme d'expression, pas l'idée ou l'algorithme."),
 QC("Quelle licence libre impose la redistribution du code modifié sous licence équivalente ?", "MIT~Apache 2.0~GPL~BSD", 2,
     "La GPL est une licence copyleft forte : les œuvres dérivées doivent rester sous GPL."),
 QC("Quelle licence étend l'obligation de partage aux services en réseau ?", "MIT~AGPL~BSD~MPL", 1,
     "L'AGPL couvre l'usage via un réseau, contrairement à la GPL classique."),
 QC("Combien de temps dure un brevet ?", "10 ans~20 ans~70 ans~Illimité", 1,
     "La durée du brevet est de 20 ans à compter du dépôt."),
 QC("Quel document recense les composants logiciels d'un produit et leurs licences ?", "Un SBOM~Un RIB~Un CV~Un SLA", 0,
     "Le SBOM (Software Bill of Materials) inventorie les dépendances et leurs licences."),
 QC("Quel est un droit moral de l'auteur ?", "Le droit de vendre~Le droit de paternité~Le droit de copier~Le droit de facturer", 1,
     "Les droits moraux incluent la paternité et le respect de l'intégrité de l'œuvre."),
 QT("Un développeur intègre une bibliothèque sous GPL dans un logiciel propriétaire destiné à être distribué. Expliquer le risque et la bonne pratique.",
    "La GPL est une licence copyleft forte : si le logiciel est distribué et forme une œuvre dérivée de la bibliothèque, l'ensemble doit être diffusé sous GPL, avec le code source correspondant. Cela peut contrecarrer le modèle propriétaire et imposer la publication de code que l'entreprise voulait garder privé. La bonne pratique est de vérifier les licences en amont, de tenir un SBOM, de choisir une bibliothèque sous licence permissive (MIT, Apache 2.0, BSD) si le modèle propriétaire est visé, ou de faire appel à un conseil juridique pour qualifier le lien entre les composants. Pour un usage uniquement interne sans distribution, l'obligation de redistribution ne joue pas en principe, mais l'AGPL peut s'appliquer via un service réseau.",
    "On explique le copyleft, l'effet sur l'œuvre dérivée distribuée, puis la prévention par audit des licences."),
 QT("Distinguer droit d'auteur, brevet et secret des affaires pour protéger une innovation logicielle.",
    "Le droit d'auteur protège automatiquement l'expression originale du code et de la documentation, sans dépôt, pour 70 ans après la mort de l'auteur. Le brevet protège une invention technique nouvelle et inventive pendant 20 ans, mais il exige un dépôt, une publication et le paiement de redevances ; les logiciels abstraits en sont généralement exclus, sauf si elles produisent un effet technique. Le secret des affaires protège toute information confidentielle ayant une valeur économique, sans durée limitée, à condition de démontrer des mesures de protection raisonnables : accès restreint, chiffrement, clauses de confidentialité. Le choix dépend de la nature de l'innovation et de la stratégie de l'entreprise.",
    "On compare les trois régimes sur l'origine du droit, la durée, les formalités et les conditions de protection.")],
C("La propriété intellectuelle protège l'expression des créations : le droit d'auteur est automatique, la licence définit l'usage et le brevet exige un dépôt.",
  "Droit d'auteur : 70 ans après la mort · brevet : 20 ans",
  "Droits moraux inaliénables · copyleft GPL · SBOM pour les dépendances",
  "Droit d'auteur~Protection automatique~Œuvre originale~Code source~Droits moraux~Paternité et intégrité~Licence~Conditions d'utilisation~Brevet~20 ans",
  "Inventorier les créations et dépendances|Vérifier la licence de chaque composant|Qualifier le modèle de distribution|Documenter les droits cédés|Surveiller les obligations de conformité",
  "Croire qu'une idée est protégeable par le droit d'auteur|Ignorer la licence d'une dépendance|Confondre GPL et licence permissive|Oublier le secret des affaires",
  "GPL~Copyleft fort~MIT~Licence permissive~AGPL~Obligation via réseau~SBOM~Liste des composants~70 ans~Durée des droits patrimoniaux",
  "Droit d'auteur~Expression du code~Brevet~Invention technique",
  "Licence libre~Usage et modification encadrés~Licence propriétaire~Droits limités"))

# ============================================================ DR4
add("DR4", "Droit des technologies et contrats numériques", "Droit", ["BTS2"],
S("Le contrat numérique est un accord électronique portant sur des biens ou des services informatiques : développement, hébergement, maintenance, licences ou prestation de sécurité."
  "|Le Code civil, réformé en 2016, pose les règles générales : consentement, capacité, objet licite et cause, avec une liberté contractuelle encadrée par l'ordre public."
  "|Le contrat doit préciser le périmètre fonctionnel, les livrables, les délais, les conditions de validation, la propriété des résultats et la responsabilité en cas de défaillance."
  "|Un cahier des charges fonctionnel décrit le besoin sans imposer la solution technique ; un cahier des charges technique précise l'architecture et les contraintes."
  "|Les clauses essentielles d'un contrat informatique portent sur la propriété intellectuelle, la confidentialité, la sous-traitance, la réversibilité et l'auditabilité."
  "|La clause de réversibilité organise la restitution des données et des codes sources en fin de contrat : elle est critique pour éviter la dépendance à un fournisseur."
  "|Les niveaux de service (SLA) définissent des engagements mesurables : disponibilité, temps de réponse, délai de rétablissement, avec des pénalités éventuelles."
  "|La clause de confidentialité et le secret professionnel protègent les informations échangées ; les sous-traitants doivent être liés par des engagements équivalents."
  "|La signature électronique qualifiée eIDAS a la même valeur juridique qu'une signature manuscrite, sous réserve de vérification d'identité et d'un certificat qualifié."
  "|La preuve des échanges repose sur les courriels, les comptes rendus, les journaux de version et les outils de gestion de projet : elle est déterminante en cas de litige."
  "|Le droit de la consommation et la directive 2019/770 encadrent les contrats de fourniture de contenus et de services numériques, avec des obligations de mise à jour."
  "|Pour un projet CIEL, savoir lire un contrat et rédiger un compte rendu de recette est aussi utile que maîtriser la technique."),
[QC("Quelles conditions de validité d'un contrat civil ?", "Consentement, capacité, objet licite et cause~Un simple courriel~Une signature scannée~Un accord verbal uniquement", 0,
     "Le Code civil exige consentement, capacité, objet certain et licite, et cause licite."),
 QC("Que décrit un cahier des charges fonctionnel ?", "L'architecture serveur~Le besoin et les fonctions attendues~Le code source~Le prix des licences", 1,
     "Le cahier des charges fonctionnel exprime le besoin, indépendamment des moyens techniques."),
 QC("À quoi sert une clause de réversibilité ?", "À augmenter le prix~À organiser la restitution des données et des livrables en fin de contrat~À supprimer la recette~À prolonger tacitement le contrat", 1,
     "La réversibilité évite la dépendance au fournisseur et sécurise la sortie du contrat."),
 QC("Que définit un SLA ?", "Un type de licences~Des engagements de niveau de service mesurables~Un plan de recrutement~Une clause de confidentialité", 1,
     "Le SLA fixe disponibilité, délais et pénalités éventuelles."),
 QC("Quelle signature a valeur légale équivalente à l'écrit papier ?", "Une simple image de signature~La signature électronique qualifiée eIDAS~Un tampon~Une initiale manuscrite", 1,
     "La signature qualifiée repose sur un certificat qualifié et un dispositif de création sécurisé."),
 QC("Quel document atteste de l'acceptation d'un livrable ?", "Le devis~Le procès-verbal de recette~La facture~Le contrat de maintenance", 1,
     "Le procès-verbal de recette constate la conformité du livrable au besoin."),
 QC("Que doit prévoir une clause de sous-traitance ?", "L'interdiction totale de sous-traiter dans tous les cas~Les conditions d'autorisation et les obligations équivalentes du sous-traitant~Le salaire des développeurs~La couleur du logo", 1,
     "Le contrat doit encadrer le recours à un sous-traitant et la transmission des obligations."),
 QC("Pourquoi conserver les comptes rendus et journaux de version ?", "Pour respecter une mode~Pour apporter la preuve des échanges et des décisions~Pour réduire les temps de compilation~Pour augmenter la durée de garantie", 1,
     "La traçabilité documentaire est déterminante en cas de désaccord ou de litige."),
 QT("Un contrat de maintenance informatique arrive à échéance et le fournisseur refuse de restituer les données. Analyser la situation et les leviers.",
    "Si le contrat comporte une clause de réversibilité, le fournisseur est tenu de restituer les données dans le format et le délai prévus ; son refus constitue un manquement contractuel. Le client doit d'abord mettre en demeure le fournisseur par écrit en invoquant la clause, en conservant les preuves des demandes restées sans réponse. Il peut ensuite saisir le médiateur ou le juge pour obtenir la remise des données et des dommages-intérêts, et signaler le cas échéant une pratique abusive à l'autorité de la concurrence ou à la CNIL si des données personnelles sont concernées. Pour l'avenir, il faut prévoir une clause de réversibilité précise, une pénalité de retard et une sauvegarde indépendante des données en amont.",
    "On s'appuie sur la clause contractuelle, la mise en demeure, les voies de recours et la prévention par sauvegarde."),
 QT("Expliquer les différences entre signature électronique simple, avancée et qualifiée selon eIDAS.",
    "La signature électronique simple est un ensemble de données électroniques utilisées pour signer, sans exigence particulière de vérification d'identité ; sa valeur probante est faible. La signature avancée utilise un certificat lié au signataire, identifie celui-ci et protège les données contre toute modification, avec une valeur probante renforcée. La signature qualifiée répond en plus aux exigences de l'annexe II d'eIDAS : certificat qualifié délivré par un prestataire de confiance, dispositif de création qualifié, vérification d'identité et horodatage qualifié. Elle bénéficie de la présomption de validité et a la même valeur juridique qu'une signature manuscrite, ce qui est déterminant pour les marchés et les actes authentiques.",
    "On distingue les trois niveaux par l'identification, le certificat et la présomption de validité.")],
C("Un contrat numérique sécurise le projet : périmètre, propriété, réversibilité, SLA et preuve des échanges en sont les piliers.",
  "Recette = vérification de la conformité au cahier des charges",
  "Code civil · eIDAS · clause de réversibilité · SLA · procès-verbal de recette",
  "Cahier des charges~Besoins et fonctions~Clause de réversibilité~Restitution en fin de contrat~SLA~Engagements mesurables~Recette~Validation du livrable~Signature qualifiée~Valeur de l'écrit",
  "Rédiger le périmètre et les critères de recette|Encadrer sous-traitance et confidentialité|Préciser propriété et réversibilité|Définir les SLA et pénalités|Consigner les échanges et la recette",
  "Signer sans lire les clauses de propriété|Omettre la réversibilité|Accepter un SLA sans indicateur|Ne pas archiver les comptes rendus",
  "Procès-verbal de recette~Preuve d'acceptation~Mise en demeure~Étape avant recours~SLA~Disponibilité et délai~eIDAS~Signature qualifiée~Réversibilité~Sortie sécurisée",
  "Cahier fonctionnel~Le besoin~Cahier technique~La solution retenue",
  "Signature simple~Faible valeur probante~Signature qualifiée~Valeur de l'écrit papier"))

# ============================================================ DR5
add("DR5", "Responsabilité civile et pénale dans le numérique", "Droit", ["BTS2"],
S("La responsabilité est l'obligation de répondre de ses actes et d'en réparer les conséquences, ou d'en supporter la sanction."
  "|La responsabilité civile vise la réparation d'un dommage : elle peut être contractuelle, lorsque le dommage résulte de l'inexécution d'un contrat, ou délictuelle, en l'absence de contrat."
  "|La responsabilité délictuelle de droit commun repose sur quatre éléments : une faute, un dommage, un lien de causalité et l'absence de cause exonératoire."
  "|La responsabilité contractuelle impose une obligation de moyens ou de résultat : l'obligation de sécurité informatique est généralement une obligation de moyens, dont il faut prouver la mise en œuvre."
  "|La clause limitative de responsabilité peut réduire l'indemnisation, mais elle est inopposable en cas de faute lourde, de dol ou d'atteinte à une obligation essentielle du contrat."
  "|Un prestataire qui n'applique pas les correctifs de sécurité connus commet une faute : l'absence de mise à jour est un élément objectif de négligence."
  "|Sur le plan pénal, l'article 323-1 du Code pénal réprime l'accès frauduleux à un système automatisé de données ; les articles suivants visent l'altération, la destruction et l'entrave."
  "|Le délit de blanchiment, l'escroquerie et l'extorsion avec rançongiciel relèvent d'autres qualifications pénales, souvent avec des peines aggravées."
  "|Une personne morale, comme une entreprise, peut être pénalement responsable des infractions commises pour son compte par ses organes ou représentants."
  "|La responsabilité de l'employeur peut être engagée pour le comportement d'un salarié dans l'exercice de ses fonctions ; la faute lourde et le dol du salarié sont des exceptions."
  "|L'assurance cyber responsabilité couvre tout ou partie des frais de réponse à incident, de notification et de défense, sous réserve des exclusions du contrat."
  "|La documentation des procédures, des journaux et des décisions est la meilleure preuve de la diligence raisonnable en cas de mise en cause."),
[QC("Quels éléments caractérise la responsabilité délictuelle ?", "Faute, dommage, lien de causalité~Contrat, facture, délai~Consentement, capacité, cause~Offre, acceptation, prix", 0,
     "La responsabilité délictuelle exige une faute, un dommage et un lien de causalité."),
 QC("Quel type d'obligation s'applique généralement à la sécurité informatique ?", "Obligation de résultat absolu~Obligation de moyens~Aucune obligation~Obligation de non-faire", 1,
     "On doit démontrer avoir mis en œuvre les moyens appropriés, non garantir une sécurité absolue."),
 QC("Une clause limitative de responsabilité est-elle opposable en cas de faute lourde ?", "Oui, toujours~Non~Oui, si elle est écrite~Seulement entre particuliers", 1,
     "La faute lourde et le dol rendent la clause inopposable."),
 QC("Quel article du Code pénal réprime l'accès frauduleux à un système ?", "Article 323-1~Article 1382~Article L. 112-2~Article 33 du RGPD", 0,
     "L'article 323-1 et les suivants répriment les atteintes aux systèmes automatisés de données."),
 QC("Une entreprise peut-elle être pénalement responsable ?", "Non, jamais~Oui, pour les infractions commises pour son compte~Oui, mais seulement en civil~Seulement si elle est publique", 1,
     "La responsabilité pénale des personnes morales est prévue par le Code pénal."),
 QC("Qu'est-ce qu'une obligation de résultat ?", "Mettre en œuvre des moyens~Garantir un résultat déterminé~Payer une amende~Rédiger un contrat", 1,
     "En obligation de résultat, l'inexécution suffit à engager la responsabilité, sauf force majeure."),
 QC("Que couvre principalement une assurance cyber responsabilité ?", "Les seuls salaires~Les frais de réponse, notification et défense~Les investissements informatiques~Les impôts", 1,
     "Elle prend en charge tout ou partie des coûts liés à un incident, selon les garanties souscrites."),
 QC("Pourquoi documenter les décisions de sécurité ?", "Pour augmenter le débit~Pour prouver la diligence raisonnable en cas de litige~Pour réduire le nombre de serveurs~Pour changer de logiciel", 1,
     "Les traces écrites démontrent les moyens mis en œuvre et la date des décisions."),
 QT("Un prestataire a oublié d'appliquer un correctif critique ; le système est compromis. Analyser sa responsabilité contractuelle et civile.",
    "Le contrat comporte vraisemblablement une obligation de moyens en matière de sécurité : le prestataire doit démontrer qu'il a mis en œuvre une veille et une procédure de correctifs adaptées. L'absence d'application d'un correctif critique connu et disponible constitue une faute caractérisée, surtout si une procédure existait et n'a pas été exécutée. Le client doit établir un dommage (interruption, perte de données, coût de remédiation) et le lien de causalité entre l'omission et le dommage. Une clause limitative de responsabilité ne protégerait pas le prestataire si la faute est lourde ou porte sur une obligation essentielle. Le client peut demander l'exécution, la réparation et, le cas échéant, la résiliation du contrat.",
    "On qualifie l'obligation, on établit faute, dommage et lien, puis on écarte la clause limitative en cas de faute lourde."),
 QT("Expliquer comment la traçabilité des journaux et des décisions protège l'entreprise en cas d'incident de sécurité.",
    "Les journaux établissent la chronologie des faits : date de détection, heure de compromission, actions entreprises, identité des intervenants. Ils permettent de démontrer que l'entreprise avait mis en place une surveillance et qu'elle a réagi dans un délai raisonnable, ce qui est déterminant pour apprécier sa diligence et respecter le délai de notification de 72 heures. Les comptes rendus de décision montrent que les choix ont été faits de manière collégiale et documentée, par des personnes habilitées. En outre, des preuves intègres (horodatage, hashes, conservation) peuvent être produites devant la CNIL, la justice ou l'assureur. À l'inverse, des journaux absents ou modifiés font peser une présomption de négligence et compliquent la défense.",
    "On relie traçabilité, preuve de diligence, notification, et valeur devant les autorités et l'assureur.")],
C("La responsabilité engage la réparation d'un dommage ou la sanction d'une infraction : faute, dommage et lien de causalité sont les mots clés.",
  "Responsabilité délictuelle = faute + dommage + lien de causalité",
  "Obligation de moyens · faute lourde · article 323-1 du Code pénal · assurance cyber",
  "Responsabilité civile~Réparer un dommage~Contractuelle~Inexécution d'un contrat~Délictuelle~Sans contrat~Faute~Manquement à une obligation~Dommage~Préjudice subi",
  "Identifier le fondement contractuel ou délictuel|Établir la faute et le dommage|Montrer le lien de causalité|Vérifier les clauses et exclusions|Consolider les preuves",
  "Affirmer une sécurité absolue|Supprimer les journaux après incident|Invoquer une clause en cas de faute lourde|Oublier que la personne morale peut être poursuivie",
  "Article 323-1~Accès frauduleux~72 h~Notification RGPD~Obligation de moyens~Diligence à prouver~Assurance cyber~Frais de réponse~Dol~Intention de nuire",
  "Obligation de moyens~Mettre en œuvre des actions~Obligation de résultat~Garantir un outcome",
  "Responsabilité civile~Réparer~Responsabilité pénale~Sanctionner"))

# ============================================================ DR6
add("DR6", "Contrats, marchés publics et achats informatiques", "Droit", ["BTS2"],
S("Un marché public est un contrat conclu par une personne publique pour répondre à un besoin de travaux, de fournitures ou de services."
  "|Il relève du Code de la commande publique, entré en vigueur le 1er avril 2019, qui regroupe les anciens codes des marchés publics."
  "|Les principes fondamentaux sont la liberté d'accès, l'égalité de traitement des candidats et la transparence des procédures."
  "|La consultation distingue le marché en procédure adaptée (MAPA), pour les montants modestes, et les procédures formalisées (appel d'offres, dialogue compétitif, marché négocié)."
  "|Le cahier des clauses administratives générales (CCAG) et le cahier des clauses techniques générales (CCTG) encadrent l'exécution des marchés de l'État."
  "|Les critères de sélection portent sur la capacité économique et technique des candidats, puis sur l'offre : prix, qualité, délais, valeur technique et critères environnementaux."
  "|Le CCAP (cahier des clauses administratives particulières) et le CCTP (cahier des clauses techniques particulières) adaptent ces règles à chaque consultation."
  "|La dématérialisation des marchés publics est obligatoire depuis 2018 : les candidats déposent leurs offres sur une plateforme de dématérialisation."
  "|Les clauses d'exclusivité, de sous-traitance et de respiration concurrentielle doivent être justifiées : le Code interdit les clauses discriminatoires."
  "|L'allotissement est le principe : le marché est divisé en lots pour permettre aux PME de candidater, sauf justification contraire."
  "|Le cycle d'achat comprend expression du besoin, consultation, analyse des offres, notification, exécution, recette et règlement."
  "|Dans le secteur privé, les mêmes bonnes pratiques s'appliquent : cahier des charges clair, grille de notation objective et traçabilité des décisions."),
[QC("Quel code régit les marchés publics depuis 2019 ?", "Le Code de commerce~Le Code de la commande publique~Le Code du travail~Le Code civil uniquement", 1,
     "Le Code de la commande publique est entré en vigueur le 1er avril 2019."),
 QC("Quel principe impose l'égalité de traitement des candidats ?", "La liberté d'accès~L'égalité~La transparence~La publicité", 1,
     "L'égalité de traitement est l'un des trois principes fondamentaux avec la liberté d'accès et la transparence."),
 QC("Que signifie MAPA ?", "Marché à procédure adaptée~Marché annuel de prestations~Mission d'audit~Marché à paiement anticipé", 0,
     "Le marché en procédure adaptée concerne les montants inférieurs aux seuils de procédure formalisée."),
 QC("Que contient le CCTP ?", "Les clauses administratives générales~Les prescriptions techniques particulières du besoin~Le prix global~Les seules sanctions", 1,
     "Le cahier des clauses techniques particulières décrit les exigences techniques de la consultation."),
 QC("Quel principe recommande de diviser un marché en plusieurs lots ?", "L'allotissement~La centralisation~L'exclusivité~La négociation directe", 0,
     "L'allotissement favorise l'accès des PME, sauf justification contraire."),
 QC("Depuis quand les marchés publics sont-ils dématérialisés ?", "2010~2014~2018~2023", 2,
     "La dématérialisation des procédures est obligatoire depuis 2018."),
 QC("Quel critère de choix ne doit pas être discriminatoire ?", "La valeur technique~Le prix~Une condition de nationalité non justifiée~Le délai de livraison", 2,
     "Les clauses discriminatoires sont interdites par le Code de la commande publique."),
 QC("Quelle est la dernière étape du cycle d'achat ?", "Expression du besoin~Consultation~Recette~Règlement et archivage", 3,
     "Après la recette, on règle le prestataire et on archive le dossier."),
 QT("Expliquer pourquoi l'allotissement et la dématérialisation sont deux leviers de concurrence dans les marchés publics.",
    "L'allotissement divise un besoin important en lots plus petits, ce qui permet à des PME ou à des entreprises spécialisées de soumissionner alors qu'elles ne pourraient pas répondre à un marché global. Il augmente donc le nombre de candidats potentiels et la pression concurrentielle. La dématérialisation supprime les contraintes matérielles de dépôt, réduit les coûts de participation, rend les échanges horodatés et traçables et permet à un plus grand nombre d'entreprises, y compris éloignées géographiquement, de répondre. Ensemble, ces deux mécanismes renforcent la transparence et l'égalité de traitement, sous réserve que les critères de sélection restent objectifs et proportionnés au besoin.",
    "On relie allotissement et accès des PME, dématérialisation et coût de participation, puis transparence et égalité."),
 QT("Une collectivité veut acheter un système de supervision réseau. Décrire les étapes pour construire une consultation conforme.",
    "Elle formalise d'abord son besoin : périmètre, nombre d'équipements, fonctionnalités de supervision, contraintes d'intégration et exigences de sécurité. Elle vérifie le montant estimé pour choisir entre MAPA et procédure formalisée, et décide de l'allotissement (par exemple supervision et prestations d'intégration). Elle rédige les pièces de la consultation : règlement, CCTP décrivant les exigences fonctionnelles et techniques sans favoriser un éditeur, CCAP avec délais, pénalités et réversibilité, et grille de notation pondérant prix, valeur technique et critères environnementaux. Elle publie l'avis sur la plateforme de dématérialisation, reçoit et analyse les offres avec une grille objective, notifie le titulaire, puis suit l'exécution et prononce la recette avant règlement et archivage.",
    "On attend : besoin, seuil et procédure, allotissement, pièces écrites, grille de notation, dématérialisation, recette.")],
C("Le marché public est encadré par le Code de la commande publique : liberté d'accès, égalité et transparence guident toute la procédure.",
  "Code de la commande publique · 1er avril 2019",
  "MAPA · appel d'offres · allotissement · dématérialisation · CCTP/CCAP",
  "Code de la commande publique~Depuis avril 2019~MAPA~Procédure adaptée~Allotissement~Division en lots~CCTP~Exigences techniques~Dématérialisation~Dépôt en ligne",
  "Expression du besoin|Choix de la procédure et des lots|Rédaction CCTP et CCAP|Publication et analyse des offres|Recette, règlement et archivage",
  "Rédiger un CCTP favorisant un éditeur|Oublier la clause de réversibilité|Ne pas tracer l'analyse des offres|Ignorer les seuils de procédure",
  "1er avril 2019~Entrée en vigueur du code~2018~Dématérialisation obligatoire~CCTP~Besoin technique~CCAP~Règles administratives~Allotissement~Accès des PME",
  "MAPA~Montants modestes~Appel d'offres~Procédure formalisée",
  "CCTP~Spécifications techniques~CCAP~Conditions administratives"))

# ============================================================ DR7
add("DR7", "Réglementation NIS, NIS2 et sécurité des réseaux essentiels", "Droit", ["BTS2"],
S("La directive NIS (Network and Information Security, UE 2016/1148) est entrée en vigueur en 2016 et a été transposée en France par l'ordonnance du 12 décembre 2018."
  "|Elle vise à renforcer la sécurité des réseaux et systèmes d'information des opérateurs de services essentiels et des fournisseurs de services numériques."
  "|Les opérateurs de services essentiels relèvent de secteurs critiques : énergie, transports, santé, eau, finance, télécommunications et infrastructures numériques."
  "|Ils doivent prendre des mesures techniques et organisationnelles appropriées et proportionnées, et notifier les incidents ayant un impact significatif à l'autorité compétente."
  "|En France, l'ANSSI est l'autorité compétente pour la plupart des secteurs et reçoit les notifications d'incidents significatifs."
  "|Les fournisseurs de services numériques, comme les services cloud ou les places de marché, ont des obligations de sécurité et de notification adaptées à leur taille."
  "|La directive NIS2 (UE 2022/2555), entrée en vigueur en janvier 2023, étend le périmètre à davantage de secteurs et de tailles d'entreprises."
  "|NIS2 renforce les exigences de gouvernance : responsabilité des dirigeants, formation, gestion de la chaîne d'approvisionnement et mesures de cyberhygiène."
  "|Elle introduit une notification en deux temps : alerte précoce dans les 24 heures puis notification complète dans les 72 heures."
  "|Les sanctions maximales prévues par NIS2 atteignent 10 millions d'euros ou 2 % du chiffre d'affaires mondial pour les entités essentielles."
  "|La France a transposé NIS2 par la loi du 8 novembre 2024 relative à la sécurité des réseaux et systèmes d'information, qui crée un régime de notifications unifié."
  "|Ces obligations concernent directement les techniciens CIEL : détecter, qualifier et remonter un incident dans les délais fait partie des compétences de cyberdéfense."),
[QC("Quelle directive européenne a introduit la notion d'opérateur de services essentiels ?", "RGPD~NIS (2016/1148)~eIDAS~RoHS", 1,
     "La directive NIS 2016/1148 porte sur la sécurité des réseaux et des systèmes d'information."),
 QC("Quelle autorité reçoit les notifications d'incidents significatifs en France ?", "La CNIL~L'ANSSI~L'ARCEP~Le CNIL", 1,
     "L'ANSSI est l'autorité compétente NIS pour la plupart des secteurs."),
 QC("Quel secteur est concerné par NIS ?", "La restauration~L'énergie~La mode~Le sport amateur", 1,
     "L'énergie figure parmi les secteurs dits essentiels avec la santé, les transports ou les télécommunications."),
 QC("Quand la directive NIS2 est-elle entrée en vigueur ?", "2016~2018~Janvier 2023~Novembre 2024", 2,
     "NIS2 est entrée en vigueur en janvier 2023 ; la transposition française date de 2024."),
 QC("Quel délai d'alerte précoce introduit NIS2 ?", "1 heure~24 heures~72 heures~7 jours", 1,
     "NIS2 prévoit une alerte précoce dans les 24 heures puis une notification complète dans les 72 heures."),
 QC("Quel montant maximal de sanction pour une entité essentielle sous NIS2 ?", "2 millions d'euros~10 millions d'euros ou 2 % du CA~20 millions d'euros~500 000 €", 1,
     "Le plafond est de 10 M€ ou 2 % du chiffre d'affaires annuel mondial."),
 QC("Quelle nouvelle exigence de gouvernance NIS2 impose-t-elle aux dirigeants ?", "Une formation en informatique obligatoire~Une responsabilité explicite de la direction~Un stage en entreprise~Une certification ISO 27001 obligatoire", 1,
     "NIS2 responsabilise les dirigeants et exige notamment leur formation et la supervision des mesures."),
 QC("Que doit faire un technicien qui détecte un incident significatif ?", "Attendre la fin de l'incident~Signaler immédiatement selon la procédure interne~Supprimer les journaux~Prévenir les médias", 1,
     "La remontée rapide permet à l'organisation de respecter les délais de notification."),
 QT("Expliquer la différence entre RGPD et NIS2 et pourquoi les deux peuvent s'appliquer au même incident.",
    "Le RGPD protège les personnes physiques et leurs données personnelles : il impose une notification à la CNIL dans les 72 heures lorsque la violation est susceptible d'engendrer un risque pour les droits et libertés. NIS2 vise la résilience des réseaux et systèmes d'information d'entités importantes ou essentielles : elle impose des mesures de sécurité et une alerte à l'ANSSI dans les 24 heures puis une notification complète dans les 72 heures. Une attaque par rançongiciel contre un hôpital illustre le cumul : des données de patients sont exposées (RGPD) et le service de soins est perturbé (NIS2). Les deux régimes ont des autorités, des délais et des finalités distincts ; la procédure interne doit prévoir les deux notifications et un même dossier de preuves peut être utilisé.",
    "On distingue l'objet (données vs résilience), les autorités et les délais, puis on illustre par un incident cumulé."),
 QT("Un incident perturbe un service essentiel. Décrire la chaîne de remontée et les éléments à réunir pour la notification.",
    "Le technicien détecte et qualifie l'incident : date et heure de survenance, systèmes touchés, nature de l'attaque, nombre d'utilisateurs impactés, durée estimée et gravité. Il alerte immédiatement son responsable et le RSSI, puis l'ANSSI selon la procédure interne, dans les 24 heures pour l'alerte précoce. Il rassemble les éléments factuels : journaux horodatés, captures, hashes, liste des systèmes affectés, mesures de confinement déjà prises, hypothèses sur le vecteur d'entrée et impact sur la continuité de service. Il transmet une notification complète dans les 72 heures avec les informations connues, puis des mises à jour si de nouveaux éléments apparaissent. Toutes les actions sont tracées et le dossier alimente le retour d'expérience.",
    "On attend : qualification, remontée hiérarchique et ANSSI, collecte de preuves, alerte 24 h, notification 72 h et traçabilité.")],
C("NIS et NIS2 imposent une cyber-résilience aux entités critiques : gouvernance, mesures de sécurité et notification rapide des incidents.",
  "NIS2 : alerte 24 h puis notification 72 h",
  "ANSSI · opérateurs de services essentiels · sanctions 10 M€ ou 2 %",
  "Directive NIS~2016/1148~Opérateur essentiel~Secteur critique~ANSSI~Autorité compétente~NIS2~2022/2555~Alerte 24 h~Notification rapide",
  "Déterminer si l'entité est concernée|Identifier les actifs critiques|Mettre en œuvre les mesures de sécurité|Détecter et qualifier l'incident|Notifier ANSSI et tracer",
  "Confondre RGPD et NIS2|Attendre la résolution complète avant d'alerter|Ignorer la chaîne d'approvisionnement|Ne pas documenter l'incident",
  "2016~Directive NIS~Janvier 2023~Entrée en vigueur NIS2~24 h~Alerte précoce~72 h~Notification complète~10 M€ ou 2 %~Plafond NIS2",
  "RGPD~Protège les données~NIS2~Protège la résilience",
  "NIS~Périmètre initial~NIS2~Périmètre élargi"))

# ============================================================ EC1
add("EC1", "Économie du numérique : acteurs, valeurs et modèles", "Économie", ["BTS1"],
S("L'économie numérique désigne l'ensemble des activités de production, de distribution et de consommation fondées sur les technologies de l'information et de la communication."
  "|Elle comprend les équipements (matériels), les logiciels, les services d'hébergement et de cloud, les télécommunications et les contenus numériques."
  "|La valeur d'un service numérique ne se mesure pas seulement à son prix : elle dépend de l'audience, des données collectées et des effets de réseau."
  "|Un effet de réseau existe lorsqu'un service devient plus utile à mesure que ses utilisateurs sont nombreux : c'est le cas des réseaux sociaux et des places de marché."
  "|Les coûts marginaux du numérique sont souvent faibles : produire une copie supplémentaire d'un logiciel coûte presque rien, alors que le développement initial est coûteux."
  "|Cette structure de coûts explique les stratégies de prix agressifs, la gratuité apparente et la concentration sur quelques acteurs dominants."
  "|La donnée est devenue un facteur de production : elle alimente l'amélioration des produits, la publicité ciblée et l'entraînement de modèles d'intelligence artificielle."
  "|Le modèle économique décrit la manière dont une organisation crée, délivre et capte de la valeur : abonnement, transaction, publicité, freemium ou licence."
  "|La chaîne de valeur numérique va du fournisseur d'infrastructure à l'utilisateur final, en passant par les éditeurs, les intégrateurs et les distributeurs."
  "|La souveraineté numérique désigne la capacité d'un État ou d'une organisation à maîtriser ses choix technologiques et ses données."
  "|Le cloud a transformé l'investissement informatique en coût d'exploitation : le paiement à l'usage offre de la souplesse mais crée une dépendance au fournisseur."
  "|Ces notions éclairent les choix d'architecture et d'achat que le technicien CIEL est amené à documenter dans un projet."),
[QC("Quel est un coût caractéristique du numérique ?", "Un coût marginal de copie très faible~Un coût de transport élevé~Un coût de stockage nul~Un coût de main-d'œuvre croissant", 0,
     "Copier un logiciel ou un contenu numérique coûte très peu par rapport à sa création."),
 QC("Qu'appelle-t-on effet de réseau ?", "Un service plus utile quand il a plus d'utilisateurs~Une baisse de la qualité avec le succès~Un réseau physique plus rapide~Une hausse du coût par client", 0,
     "La valeur perçue augmente avec le nombre de participants."),
 QC("Quel modèle de revenus repose sur un paiement récurrent ?", "La vente au acte~L'abonnement~Le don unique~Le troc", 1,
     "L'abonnement (SaaS) génère des revenus récurrents prévisibles."),
 QC("Que désigne le modèle freemium ?", "Un produit gratuit financé par la publicité~Une offre gratuite avec options payantes~Un produit vendu uniquement en entreprise~Un abonnement sans engagement", 1,
     "La version gratuite attire les utilisateurs, les fonctions avancées sont payantes."),
 QC("Quel est un avantage du cloud en paiement à l'usage ?", "Une dépense d'investissement réduite au départ~Une absence totale de coût~Une souveraineté garantie~Une sécurité automatique", 0,
     "Le passage de CapEx à OpEx réduit l'investissement initial et augmente la flexibilité."),
 QC("Quel risque majeur du cloud est lié à la dépendance ?", "Le verrouillage propriétaire (lock-in)~La gratuité des données~L'absence de facturation~La baisse du nombre d'utilisateurs", 0,
     "Le lock-in rend la sortie coûteuse et complexe, d'où l'importance de la réversibilité."),
 QC("Que désigne la souveraineté numérique ?", "La maîtrise de ses choix technologiques et de ses données~Le refus d'Internet~La gratuité des logiciels~Le monopole national", 0,
     " Elle vise l'autonomie de décision et de contrôle sur les actifs numériques."),
 QC("Quel acteur de la chaîne de valeur fournit les ressources de calcul et de stockage ?", "L'éditeur de logiciels~Le fournisseur d'infrastructure cloud~L'utilisateur final~Le régulateur", 1,
     "Les fournisseurs d'infrastructure proposent les ressources de calcul, de stockage et de réseau."),
 QT("Expliquer pourquoi un service numérique peut être proposé gratuitement à l'utilisateur et comment il se rémunère.",
    "La gratuité apparente s'explique par des coûts marginaux très faibles et par un modèle de revenus indirect. Le service peut être financé par la publicité ciblée, qui valorise l'attention et les données d'audience, par la vente d'options payantes (freemium), par un abonnement d'une partie des utilisateurs ou encore par la revente de services dérivés. Dans ce modèle, l'utilisateur n'est pas le client mais la source de valeur : ses données et son attention alimentent l'écosystème. Cela pose des questions de transparence, de consentement et de protection des données, encadrées par le RGPD et le Digital Services Act.",
    "On relie faible coût marginal, revenus indirects, valeur des données et enjeux de protection."),
 QT("Une entreprise hésite entre héberger ses serveurs en interne et migrer vers le cloud. Présenter les arguments économiques des deux options.",
    "L'hébergement interne demande un investissement initial important (CapEx) : serveurs, câblage, salle, climatisation, et mobilise des compétences internes. Il offre un contrôle fort, une prévisibilité des coûts à long terme et une indépendance vis-à-vis d'un fournisseur, mais supporte des coûts fixes même en cas de faible utilisation. Le cloud transforme la dépense en coût variable (OpEx) : on paie à l'usage, on dimensionne rapidement et on accède à des services avancés, ce qui favorise l'innovation. En revanche, le coût peut croître avec l'usage, la sortie est difficile (lock-in) et la souveraineté des données doit être négociée contractuellement. Le choix dépend du profil de charge, des exigences de conformité et de la stratégie de réversibilité.",
    "On compare CapEx et OpEx, contrôle et flexibilité, puis on cite le lock-in et la réversibilité.")],
C("L'économie numérique se caractérise par des coûts marginaux faibles, des effets de réseau et des modèles de revenus indirects.",
  "Valeur = usage + données + effets de réseau",
  "CapEx (interne) contre OpEx (cloud) · gratuité financée par la donnée et la publicité",
  "Coût marginal~Coût d'une unité supplémentaire~Effet de réseau~Valeur croissante avec les usagers~Cloud~Paiement à l'usage~Souveraineté~Maîtrise des choix",
  "Identifier les acteurs de la chaîne de valeur|Analyser la structure des coûts|Comprendre le modèle de revenus|Évaluer flexibilité et dépendance|Décider avec des critères documentés",
  "Croire que gratuit signifie sans coût|Ignorer le coût de sortie du cloud|Confondre valeur d'usage et prix|Négliger la souveraineté",
  "SaaS~Abonnement récurrent~Freemium~Gratuit puis payant~Effet de réseau~Plus d'usagers, plus de valeur~CapEx~Investissement initial~OpEx~Coût d'exploitation",
  "Hébergement interne~CapEx et contrôle~Cloud~OpEx et flexibilité",
  "Donnée~Facteur de production~Attention~Ressource monétisée"))

# ============================================================ EC2
add("EC2", "Coûts, rentabilité et tableau de bord d'un SI", "Économie", ["BTS2"],
S("Le contrôle de gestion d'un système d'information mesure la consommation des ressources et la valeur produite pour aider à la décision."
  "|Un coût direct est affecté sans ambiguïté à un service (licences d'un logiciel dédié) ; un coût indirect, comme l'électricité du centre de données, doit être réparti selon une clé."
  "|Les coûts fixes ne varient pas avec l'activité (loyer, salaires) ; les coûts variables évoluent avec le nombre d'utilisateurs ou de transactions."
  "|Le coût complet intègre les charges directes et la part des charges indirectes : c'est la base d'une décision de tarification interne ou d'externalisation."
  "|Le coût marginal est le coût additionnel d'une unité supplémentaire de service : en cloud, il est souvent proche du coût de l'instance supplémentaire."
  "|Le seuil de rentabilité est le niveau d'activité pour lequel les recettes couvrent exactement les coûts : il se calcule avec la marge sur coûts variables."
  "|La marge sur coûts variables égale recettes moins coûts variables ; elle contribue à couvrir les frais fixes puis à dégager un résultat."
  "|Le retour sur investissement (ROI) rapporte le gain net à l'investissement : ROI = (gains − coûts) / coûts."
  "|Le TCO (coût total de possession) additionne achat, déploiement, exploitation, maintenance, formation et fin de vie sur toute la durée de vie d'un actif."
  "|Un tableau de bord SI suit des indicateurs : taux de disponibilité, coût par ticket, temps moyen de rétablissement, taux d'utilisation des ressources et respect du budget."
  "|La valeur d'un service ne se limite pas à son coût : productivité gagnée, réactivité, conformité et satisfaction utilisateur sont des bénéfices à documenter."
  "|Un bon indicateur est pertinent, fiable, calculable régulièrement et relié à une décision : un tableau de bord trop dense devient inutile."),
[QC("Quel est un coût fixe d'un centre informatique ?", "Le nombre de transactions~Le loyer du local~La consommation électrique par serveur~Les licences à l'utilisateur", 1,
     "Le loyer ne dépend pas du niveau d'activité."),
 QC("Que désigne le coût marginal ?", "Le coût moyen~Le coût d'une unité supplémentaire~Le coût total~Le coût d'acquisition", 1,
     "Le coût marginal mesure l'augmentation de coût liée à une unité de plus."),
 QC("Comment calculer une marge sur coûts variables ?", "Recettes moins coûts fixes~Recettes moins coûts variables~Coûts variables moins recettes~Coûts fixes plus variables", 1,
     "Cette marge contribue à couvrir les frais fixes puis le résultat."),
 QC("Quelle formule donne le ROI ?", "(Gains − coûts)/coûts~Coûts/gains~Gains + coûts~Coûts/(gains−coûts)", 0,
     "Le ROI rapporte le gain net au montant investi."),
 QC("Que comprend le TCO ?", "Le seul prix d'achat~Tous les coûts sur la durée de vie~Le salaire d'un développeur~La seule maintenance", 1,
     "Le coût total de possession inclut achat, exploitation, maintenance, formation et fin de vie."),
 QC("À quoi sert le seuil de rentabilité ?", "À fixer un prix plancher~À déterminer le niveau d'activité où recettes et coûts s'équilibrent~À calculer une durée de vie~À comparer des fournisseurs", 1,
     "C'est le point mort de l'activité."),
 QC("Quel indicateur mesure la réactivité d'une équipe support ?", "Le coût du loyer~Le temps moyen de rétablissement~Le nombre de serveurs~La taille de l'écran", 1,
     "Le MTTR est un indicateur classique de la qualité du support."),
 QC("Quelle qualité a un bon indicateur de tableau de bord ?", "Il doit être le plus nombreux possible~Il doit être relié à une décision et calculable régulièrement~Il doit être complexe~Il doit changer chaque semaine", 1,
     "Un indicateur utile est fiable, compréhensible et actionnable."),
 QT("Un service cloud coûte 2 000 € par mois de frais fixes et 5 € par utilisateur. Le tarif interne est de 15 € par utilisateur. Calculer le seuil de rentabilité et le résultat pour 300 utilisateurs.",
    "La marge sur coûts variables par utilisateur vaut 15 − 5 = 10 €. Le seuil de rentabilité correspond aux frais fixes divisés par cette marge : 2 000 / 10 = 200 utilisateurs. En dessous de 200, le service perd de l'argent ; au-delà, il dégage une marge positive. Pour 300 utilisateurs, les recettes valent 300 × 15 = 4 500 €, les coûts variables 300 × 5 = 1 500 € et les frais fixes 2 000 €, soit un résultat de 4 500 − 1 500 − 2 000 = 1 000 € par mois.",
    "On calcule la marge unitaire, le point mort (200), puis le résultat à 300 utilisateurs."),
 QT("Expliquer pourquoi le TCO est un meilleur critère que le prix d'achat pour choisir entre deux solutions informatiques.",
    "Le prix d'achat ne représente qu'une fraction des dépenses réelles. Une solution moins chère à l'achat peut exiger des licences annuelles élevées, une formation coûteuse, des prestations d'intégration, une maintenance lourde, une consommation électrique importante et un remplacement anticipé. Le TCO agrège toutes ces composantes sur une durée de vie déterminée, par exemple trois ou cinq ans, et permet une comparaison homogène. Il doit être complété par une analyse de la valeur : disponibilité, sécurité, évolutivité et réversibilité. Une solution avec un TCO plus élevé peut être retenue si elle apporte des bénéfices supérieurs en productivité ou en réduction de risque.",
    "On oppose le prix initial au coût complet sur la durée de vie, puis on rappelle que la valeur dépasse le seul coût.")],
C("Le contrôle de gestion d'un SI relie les coûts aux bénéfices : marge, seuil, ROI et TCO éclairent les décisions d'architecture et d'achat.",
  "Seuil = frais fixes / marge sur coûts variables",
  "ROI = (gains − coûts)/coûts · TCO = coût complet sur la durée de vie",
  "Coût direct~Affecté au service~Coût indirect~Réparti par clé~Coût variable~Dépend de l'activité~Marge sur coûts variables~Recettes moins variables~TCO~Coût total de possession",
  "Classer les coûts|Choisir une clé de répartition|Calculer marge et seuil|Suivre les indicateurs|Comparer les scénarios",
  "Raisonner sur le seul prix d'achat|Oublier les coûts de fin de vie|Multiplier les indicateurs sans décision|Confondre coût moyen et coût marginal",
  "2 000 €/mois et 5 €/utilisateur~Seuil à 200 utilisateurs~300 utilisateurs~Résultat 1 000 €~MTTR~Temps moyen de rétablissement~ROI~Gain sur investissement~TCO~Sur trois ans",
  "Coût fixe~Indépendant de l'activité~Coût variable~Proportionnel à l'activité",
  "Seuil de rentabilité~Point mort~Marge~Contribution aux frais fixes"))

# ============================================================ EC3
add("EC3", "Emploi, compétences et formation dans le numérique", "Économie", ["BTS1"],
S("Le secteur numérique emploie des profils variés : développeurs, administrateurs systèmes et réseaux, experts cybersécurité, data analysts, chefs de projet et techniciens de support."
  "|Le BTS CIEL prépare notamment aux métiers d'administrateur réseau, de technicien en cybersécurité, de développeur d'applications et d'ingénieur système junior."
  "|Une compétence est la combinaison de connaissances, de savoir-faire et de savoir-être mobilisés dans une situation professionnelle."
  "|On distingue les compétences techniques (hard skills), comme la configuration d'un firewall, et les compétences comportementales (soft skills), comme la communication ou l'esprit d'équipe."
  "|Le référentiel d'activités du BTS CIEL décrit les situations de travail ; le référentiel de compétences précise ce que le diplômé doit être capable de faire."
  "|Le bloc de compétences n°1 de l'option IR concerne l'étude et la conception de réseaux informatiques, évaluée en unité U4."
  "|Le bloc n°2 porte sur l'exploitation et la maintenance des réseaux (U5), et le bloc n°3 sur la valorisation de la donnée et la cybersécurité (U6)."
  "|Le marché de l'emploi cyber est tendu : la pénurie de professionnels entraîne une hausse des salaires et une forte valeur des certifications."
  "|Les certifications reconnues (Parcours certifiant ANSSI, Security+, CCNA, CISCO, Microsoft, Linux) complètent le diplôme sans le remplacer."
  "|La formation continue est indispensable : l'obsolescence technique rapide impose une veille régulière et une montée en compétences tout au long de la carrière."
  "|Les compétences comportementales sont particulièrement demandées en cybersécurité, car la sensibilisation des utilisateurs et la conduite de crise exigent de la pédagogie et du sang-froid."
  "|Le stage et le projet technique en BTS sont des lieux de professionnalisation : ils permettent de démontrer des compétences dans une situation réelle et documentée."),
[QC("Quel métier relève de l'option IR du BTS CIEL ?", "Technicien de maintenance industrielle~Administrateur réseaux et sécurité~Infirmier~Comptable", 1,
     "L'option Informatique et réseaux prépare aux métiers de l'administration système, réseau et sécurité."),
 QC("Qu'appelle-t-on une compétence technique ?", "La capacité à communiquer~Un savoir-faire professionnel précis~Une qualité personnelle~Une opinion", 1,
     "Les hard skills sont des savoir-faire techniques mesurables."),
 QC("Quelle unité évalue l'exploitation et la maintenance des réseaux en option IR ?", "U1~U3~U5~U6", 2,
     "L'unité U5 correspond au bloc « Exploitation et maintenance de réseaux informatiques »."),
 QC("Que recouvre le bloc n°3 de l'option IR ?", "La conception de cartes électroniques~La valorisation de la donnée et la cybersécurité~La comptabilité~La relation client", 1,
     "Le bloc n°3 est évalué en U6 et porte sur la donnée et la cybersécurité."),
 QC("Pourquoi le marché de l'emploi cyber est-il tendu ?", "Parce que les entreprises ne recrutent plus~Parce que la demande dépasse l'offre de professionnels qualifiés~Parce que les salaires sont bas~Parce que la formation est trop courte", 1,
     "La pénurie de talents crée une forte demande et valorise les compétences cyber."),
 QC("Quel est un rôle des soft skills en cybersécurité ?", "Configurer un routeur~Sensibiliser les utilisateurs et gérer une crise~Écrire du code~Installer des câbles", 1,
     "Pédagogie, communication et gestion du stress sont essentielles dans ces missions."),
 QC("Quelle certification professionnelle est délivrée par l'ANSSI ?", "Le parcours certifiant ANSSI~Le CCNA~Le Security+~Le TOEIC", 0,
     "L'ANSSI certifie des professionnels de la sécurité des systèmes d'information via son parcours."),
 QC("Pourquoi la veille est-elle indispensable dans le numérique ?", "Pour suivre les modes~Pour maintenir ses compétences face à l'obsolescence technique~Pour réduire le nombre de réunions~Pour changer de métier chaque année", 1,
     "Les technologies et les menaces évoluent vite : la formation tout au long de la vie est nécessaire."),
 QT("Décrire les compétences mobilisées par un technicien CIEL lors d'un incident de sécurité en entreprise.",
    "Techniquement, il mobilise la supervision et l'analyse de journaux pour détecter et qualifier l'incident, la connaissance des réseaux et des systèmes pour confiner la menace, la gestion des accès pour révoquer un compte compromis, et la maîtrise des sauvegardes pour restaurer le service. Il doit aussi documenter les preuves avec rigueur, respecter les délais de notification (RGPD, NIS2) et appliquer les procédures de l'organisation. Sur le plan comportemental, il fait preuve de sang-froid, de discernement dans la hiérarchie des priorités, de discrétion sur les informations sensibles et de pédagogie pour expliquer la situation aux utilisateurs. Enfin, il participe au retour d'expérience, ce qui suppose esprit d'équipe et capacité à remettre en question ses propres pratiques.",
    "On articule compétences techniques (détection, confinement, restauration, preuves) et comportementales (calme, pédagogie, discrétion, REX)."),
 QT("Un étudiant en BTS CIEL option IR souhaite se spécialiser en cybersécurité. Proposer une progression de formation cohérente.",
    "Il consolide d'abord les bases du réseau et des systèmes (TCP/IP, Linux, virtualisation) acquises en BTS, puis suit des ressources de veille et des laboratoires pratiques pour comprendre les attaques et les défenses. Il vise ensuite une certification reconnue adaptée à son niveau, par exemple Security+ ou le parcours certifiant ANSSI, en complément du diplôme. Il s'entraîne sur des plateformes de cyberdéfense et participe à des exercices de réponse à incident pour développer la rigueur et le sang-froid. Enfin, il construit un portfolio documenté de projets et de comptes rendus d'incidents, puis envisage une poursuite d'études (but informatique, licence, école d'ingénieur) ou une insertion en SSOC/entreprise, en maintenant une veille permanente sur les menaces et les textes réglementaires.",
    "On propose une progression : bases, pratique, certification, exercices, portfolio et formation continue.")],
C("Le BTS CIEL prépare à des métiers techniques où compétences scientifiques, rigueur et qualités humaines sont complémentaires.",
  "Compétence = connaissances + savoir-faire + savoir-être",
  "Option IR : U4 conception · U5 exploitation · U6 donnée et cybersécurité",
  "Hard skills~Savoir-faire technique~Soft skills~Communication et esprit d'équipe~U4~Étude et conception~U5~Exploitation et maintenance~U6~Donnée et cybersécurité",
  "Identifier les métiers visés|Cartographier ses compétences|Pratiquer en laboratoire|Se certifier et se former en continu|Constituer un portfolio",
  "Négliger la communication|Penser que le diplôme suffit|Ignorer la veille|Oublier de documenter ses projets",
  "U4~Concevoir un réseau~U5~Exploiter et maintenir~U6~Défendre le SI~ANSSI~Certification reconnue~Veille~Mise à jour continue~Portfolio~Preuve des compétences",
  "Compétence technique~Configurer un firewall~Compétence comportementale~Sensibiliser un utilisateur",
  "BTS CIEL~Niveau bac+2~Poursuite d'études~BUT, licence, école"))

# ============================================================ EC4
add("EC4", "Conjoncture, inflation et décisions d'investissement", "Économie", ["BTS2"],
S("La conjoncture désigne l'ensemble des indicateurs qui décrivent la situation économique à court terme : croissance, inflation, emploi et commerce extérieur."
  "|Le produit intérieur brut (PIB) mesure la valeur ajoutée créée sur le territoire national au cours d'une période."
  "|La croissance est le taux de variation du PIB : une croissance positive indique une augmentation de l'activité économique."
  "|L'inflation est une hausse généralisée et durable des prix, mesurée en France par l'indice des prix à la consommation (IPC) de l'Insee."
  "|Le taux d'inflation se calcule par la variation relative de l'indice sur une période, généralement sur un an glissant."
  "|Une inflation imprévue réduit la valeur réelle des investissements et des contrats à prix fixe : le taux réel est approximativement le taux nominal moins l'inflation."
  "|La Banque centrale européenne conduit une politique monétaire visant la stabilité des prix, avec un objectif d'inflation à moyen terme de 2 %."
  "|Une hausse des taux directeurs renforce le coût du crédit et tend à freiner l'investissement des entreprises, notamment dans les projets informatiques."
  "|Le cycle économique alterne phases d'expansion, de ralentissement, de récession et de reprise : le moment du projet influe sur son financement."
  "|Les indicateurs avancés, comme le climat des affaires ou les commandes, aident à anticiper les retournements de conjoncture."
  "|Pour un projet SI, l'inflation pèse sur les coûts de main-d'œuvre, de matériel et d'énergie : le budget doit prévoir une clause de révision ou une provision."
  "|La lecture de la conjoncture permet d'expliquer une hausse des coûts cloud, un allongement des délais d'approvisionnement ou une tension sur les salaires."),
[QC("Quel indicateur mesure l'inflation en France ?", "Le PIB~L'IPC de l'Insee~Le taux de chômage~Le CAC 40", 1,
     "L'indice des prix à la consommation calculé par l'Insee mesure l'inflation."),
 QC("Que mesure le PIB ?", "Le nombre d'entreprises~La valeur ajoutée créée sur le territoire~Le nombre d'habitants~Les seules exportations", 1,
     "Le PIB additionne les valeurs ajoutées des unités résidentes."),
 QC("Quel est l'objectif d'inflation de la BCE à moyen terme ?", "0 %~1 %~2 %~5 %", 2,
     "La BCE vise un taux d'inflation de 2 % à moyen terme."),
 QC("Quel effet a une hausse des taux directeurs ?", "Elle rend le crédit moins coûteux~Elle renchérît le crédit et freine l'investissement~Elle supprime l'inflation~Elle augmente la croissance", 1,
     "Une politique monétaire restrictive augmente le coût du financement."),
 QC("Comment calculer approximativement un taux réel ?", "Taux nominal plus inflation~Taux nominal moins inflation~Inflation divisée par taux nominal~Taux nominal multiplié par inflation", 1,
     "La relation de Fisher approchée donne taux réel ≈ taux nominal − inflation."),
 QC("Quelle phase du cycle succède à l'expansion ?", "La reprise~Le ralentissement~La dépression~La stagnation", 1,
     "Après l'expansion vient généralement un ralentissement, puis une récession."),
 QC("Quel est un indicateur avancé de conjoncture ?", "Le climat des affaires~Le PIB de l'année passée~Le recensement~Le nombre de routes", 0,
     "Les enquêtes de conjoncture comme le climat des affaires précèdent les mouvements d'activité."),
 QC("Pourquoi prévoir une clause de révision dans un contrat informatique long ?", "Pour augmenter le prix sans accord~Pour tenir compte de l'évolution des coûts~Pour éviter la recette~Pour réduire la durée", 1,
     "Une clause de révision permet d'ajuster le prix en cas de variation significative des coûts."),
 QT("Un projet informatique budgété 100 000 € est prévu sur deux ans ; l'inflation annuelle est de 4 %. Montrer pourquoi le budget réel risque d'être insuffisant.",
    "Si les coûts suivent l'inflation, le budget nécessaire en fin de deuxième année devient 100 000 × 1,04² = 108 160 €, soit 8 160 € de plus que le montant initialement prévu. Le budget de 100 000 € correspond à un montant nominal fixe, mais son pouvoir d'achat réel baisse : sa valeur réelle à la fin de la période est d'environ 100 000 / 1,04² ≈ 92 456 € en euros de départ. Pour sécuriser le projet, on peut prévoir une provision pour aléas, une clause de révision indexée sur un indice, ou lisser les achats dans le temps. Le raisonnement vaut aussi pour les coûts de main-d'œuvre interne et l'énergie des centres de données.",
    "On calcule 100 000 × 1,04², on interprète la perte de pouvoir d'achat et on propose clause de révision ou provision."),
 QT("Expliquer comment la conjoncture influence le financement d'un projet de cybersécurité.",
    "En phase d'expansion, les entreprises investissent plus facilement : les budgets sont moins contraints, le coût du crédit est souvent plus bas et les projets de sécurité sont financés comme des investissements de croissance. En phase de ralentissement, les directions financières arbitrent plus strictement, parfois en faveur de dépenses défensives obligatoires (conformité, assurance) au détriment de projets innovants. Une hausse des taux renchérit le financement et augmente le coût du capital, ce qui élève le seuil de rentabilité exigé. Les tensions sur l'emploi peuvent aussi rendre les compétences cyber plus chères. Le responsable de projet doit donc présenter le projet en termes de risque évité et de conformité, avec des scénarios de coûts et une analyse de sensibilité aux taux et à l'inflation.",
    "On relie phases du cycle, coût du capital, tension sur les compétences et argumentaire de décision.")],
C("La conjoncture influe sur le coût et l'opportunité d'un projet SI : inflation, taux et cycle économique doivent être intégrés au budget.",
  "Taux réel ≈ taux nominal − inflation",
  "IPC · PIB · objectif BCE 2 % · clause de révision",
  "PIB~Valeur ajoutée totale~Croissance~Variation du PIB~IPC~Mesure de l'inflation~Taux réel~Nominal moins inflation~BCE~Stabilité des prix",
  "Lire les indicateurs|Mesurer l'écart avec le budget|Estimer l'effet de l'inflation|Prévoir clause ou provision|Réévaluer le financement",
  "Raisonner en euros constants sur un budget nominal|Ignorer la hausse des coûts salariaux|Supposer des taux stables|Omettre la clause de révision",
  "100 000 € à 4 %~108 160 € après 2 ans~2 %~Objectif BCE~Taux réel~Nominal moins inflation~Clause de révision~Ajustement du prix~BCE~Politique monétaire",
  "Inflation~Hausse des prix~Déflation~Baisse des prix",
  "Taux nominal~Chiffre affiché~Taux réel~Pouvoir d'achat"))

# ============================================================ EC5
add("EC5", "Économie des plateformes et modèles multimodaux", "Économie", ["BTS2"],
S("Une plateforme numérique est une infrastructure qui met en relation deux ou plusieurs groupes d'utilisateurs distincts, par exemple acheteurs et vendeurs."
  "|Elle crée de la valeur en réduisant les coûts de recherche, de mise en relation et de confiance entre les participants."
  "|Le modèle est dit multimodal ou multiside : la rentabilité dépend de l'équilibre entre les différents côtés du marché."
  "|Les effets de réseau indirects signifient que plus il y a d'acheteurs, plus la plateforme attire de vendeurs, et réciproquement."
  "|Le subventionnement d'un côté du marché, souvent les utilisateurs grand public, permet d'attirer l'autre côté, par exemple les annonceurs."
  "|Le prix ne reflète pas seulement le coût marginal : il dépend de l'élasticité de la demande de chaque groupe et de la structure de la concurrence."
  "|Une plateforme dominante peut adopter des pratiques anticoncurrentielles : prix prédateurs, exclusive, préférence propre ou verrouillage des données."
  "|Le Digital Markets Act (UE 2022/1925) impose des obligations aux « contrôleurs d'accès » : interopérabilité, portabilité des données et limitation des pratiques favorisant leurs propres services."
  "|Le Digital Services Act (UE 2022/2065) renforce la modération des contenus, la transparence de la publicité et la protection des mineurs."
  "|La donnée accumulée sur les interactions constitue un avantage compétitif durable : elle améliore le ciblage, la recommandation et la tarification."
  "|Pour une entreprise classique, passer par une plateforme donne de la visibilité mais crée une dépendance et une captation de la relation client."
  "|Ces enjeux concernent le technicien CIEL lors du choix d'un service cloud, d'une place de marché de logiciels ou d'une API tierce."),
[QC("Qu'appelle-t-on une plateforme multimodale ?", "Un site de vente classique~Une structure reliant plusieurs groupes d'utilisateurs~Un serveur de base de données~Un réseau local", 1,
     "Elle met en relation des groupes distincts dont les demandes sont interdépendantes."),
 QC("Quel est un effet de réseau indirect ?", "Plus d'utilisateurs attirent plus de vendeurs~Le prix baisse automatiquement~La qualité du réseau baisse~Le serveur chauffe moins", 0,
     "La croissance d'un côté profite à l'autre côté du marché."),
 QC("Pourquoi subventionner un côté du marché ?", "Pour réduire la qualité~Pour attirer l'autre côté et amorcer la croissance~Pour supprimer la publicité~Pour fermer la plateforme", 1,
     "C'est une stratégie d'amorçage classique des plateformes."),
 QC("Quel règlement européen vise les contrôleurs d'accès ?", "RGPD~Digital Markets Act~RoHS~eIDAS", 1,
     "Le DMA (UE 2022/1925) encadre les grandes plateformes structurantes."),
 QC("Quel est l'objet principal du Digital Services Act ?", "La fiscalité~La modération des contenus et la protection des utilisateurs~La formation professionnelle~La sécurité routière", 1,
     "Le DSA porte sur la responsabilité des plateformes en ligne et la sécurité des utilisateurs."),
 QC("Quel risque pour une entreprise qui dépend d'une plateforme ?", "Une baisse de la dépendance~La captation de la relation client et le verrouillage~Une hausse de l'autonomie~Une réduction des données collectées", 1,
     "La plateforme intermédie la relation et peut modifier les règles d'accès."),
 QC("Que désigne un prix prédateur ?", "Un prix très élevé~Un prix temporairement très bas pour éliminer la concurrence~Un prix fixé par la loi~Un prix moyen", 1,
     "C'est une pratique anticoncurrentielle d'élimination des concurrents."),
 QC("Pourquoi la donnée est-elle un avantage compétitif pour une plateforme ?", "Elle réduit le nombre d'utilisateurs~Elle améliore recommandation et ciblage~Elle supprime les coûts~Elle évite la régulation", 1,
     "Les données accumulées rendent le service plus pertinent et plus difficile à copier."),
 QT("Expliquer pourquoi une place de marché peut proposer gratuitement son service aux acheteurs tout en étant rentable.",
    "La place de marché agit comme un intermédiaire entre plusieurs groupes. Les acheteurs bénéficient d'un service gratuit parce que leur présence attire les vendeurs, qui paient des commissions ou des frais de mise en ligne. Les vendeurs acceptent ces frais car ils accèdent à une audience plus large qu'ils ne pourraient atteindre seuls. La plateforme peut également monétiser la publicité et les données d'interaction, sous réserve du RGPD et du DSA. Ce subventionnement d'un côté du marché est une stratégie d'amorçage : une fois la liquidité atteinte, les effets de réseau rendent le service plus attractif et la rentabilité s'améliore, mais elle dépend de l'équilibre entre les groupes.",
    "On explique la subvention croisée, les commissions, la publicité et le rôle des effets de réseau."),
 QT("Un éditeur de logiciels hésite à distribuer son produit uniquement via une place de marché dominante. Analyser les avantages et les risques.",
    "Avantages : accès immédiat à une large audience, simplification de la facturation et des mises à jour, confiance des acheteurs, réduction des coûts de commercialisation. Risques : commission prélevée sur chaque vente, dépendance à des règles de classement et à des conditions unilatérales, captation de la relation client et des données d'usage, difficulté à sortir du modèle (lock-in), exposition à des changements de politique tarifaire. Le DMA peut offrir des garanties d'interopérabilité et de portabilité face à un contrôleur d'accès. Une stratégie prudente consiste à conserver un canal direct, à documenter les données de ses clients et à prévoir une clause de réversibilité dans le contrat de distribution.",
    "On pèse audience et coûts de transaction contre commission, dépendance, données et réversibilité.")],
C("Une plateforme tire sa valeur des interactions entre groupes d'utilisateurs : subventionnement, effets de réseau et données font sa rentabilité.",
  "Valeur de la plateforme = fonction du nombre et de la qualité des participants",
  "DMA · DSA · effets de réseau indirects · subventionnement croisé",
  "Plateforme~Intermédiaire entre groupes~Multimodal~Plusieurs côtés~Effet indirect~Un côté profite à l'autre~DMA~Contrôleurs d'accès~DSA~Modération des contenus",
  "Identifier les groupes d'utilisateurs|Analyser les effets de réseau|Étudier les sources de revenus|Évaluer la dépendance|Vérifier la conformité DMA et DSA",
  "Croire que gratuit signifie sans valeur|Ignorer les pratiques anticoncurrentielles|Négliger la portabilité des données|Dépendre d'un seul canal",
  "Acheteurs~Service gratuit~Vendeurs~Commissions~Publicité~Revenu publicitaire~DMA~Interopérabilité~DSA~Protection des mineurs",
  "Effet de réseau direct~Même groupe~Effet indirect~Groupes différents",
  "Plateforme~Intermédiation~Vendeur classique~Vente directe"))

# ============================================================ EC6
add("EC6", "Commerce électronique et valorisation des données clients", "Économie", ["BTS2"],
S("Le commerce électronique désigne la vente de biens ou de services réalisée par voie électronique, principalement via un site web ou une application."
  "|On distingue les modèles B2C (entreprise vers consommateur), B2B (entreprise vers entreprise), C2C (consommateur vers consommateur) et B2G (vers les administrations)."
  "|La chaîne de valeur du e-commerce comprend la présentation de l'offre, la commande, le paiement, la préparation, la livraison et le service après-vente."
  "|Le panier moyen, le taux de conversion et le taux d'abandon de panier sont des indicateurs clés de performance d'une boutique en ligne."
  "|Le taux de conversion est le nombre de commandes divisé par le nombre de visiteurs uniques sur une période donnée."
  "|La personnalisation de l'offre repose sur l'analyse du comportement de navigation, des achats antérieurs et des données déclaratives, dans le cadre du RGPD."
  "|La publicité en ligne utilise des cookies et des traceurs : le consentement, recueilli via un bandeau, doit être libre, éclairé et documenté."
  "|La protection des données clients impose une politique de confidentialité claire, une durée de conservation définie et un registre des traitements."
  "|Les paiements en ligne s'appuient sur des prestataires certifiés PCI DSS : les données de carte ne doivent jamais être stockées en clair par le marchand."
  "|La logistique du dernier kilomètre est le poste le plus coûteux de la chaîne : le suivi de commande et la gestion des retours influencent la satisfaction."
  "|La cybersécurité du e-commerce protège les données de paiement, les comptes clients et la disponibilité du site : un incident augmente le taux d'abandon et nuit à la marque."
  "|Le technicien CIEL intervient sur la disponibilité, la supervision et la sécurité de ces plateformes, ainsi que sur la conformité des traitements de données."),
[QC("Que signifie B2C ?", "Entreprise vers entreprise~Entreprise vers consommateur~Consommateur vers consommateur~Administration vers entreprise", 1,
     "B2C signifie business to consumer, c'est-à-dire entreprise vers consommateur."),
 QC("Comment calcule-t-on le taux de conversion ?", "Commandes divisées par visiteurs~Visiteurs divisés par commandes~Panier moyen multiplié par visiteurs~Commandes moins visiteurs", 0,
     "C'est le ratio entre le nombre de commandes et le nombre de visiteurs uniques."),
 QC("Quel est un indicateur du e-commerce ?", "Le taux d'abandon de panier~Le nombre de câbles réseau~La superficie de l'entrepôt~Le salaire du dirigeant", 0,
     "Le taux d'abandon de panier mesure les paniers non finalisés."),
 QC("Quelle norme de sécurité concerne les paiements par carte ?", "ISO 9001~PCI DSS~ISO 14001~RGPD", 1,
     "La norme PCI DSS encadre la protection des données de cartes bancaires."),
 QC("Quelles données ne jamais stocker en clair chez le marchand ?", "Les références produits~Les données complètes de carte bancaire~Les avis clients~Les coordonnées postales", 1,
     "Le stockage des données de carte est délégué à un prestataire certifié et tokenisé."),
 QC("Quel est le coût souvent le plus élevé de la logistique e-commerce ?", "La fabrication~Le dernier kilomètre~La location du bureau~La publicité", 1,
     "La livraison finale représente une part majeure du coût logistique."),
 QC("Que impose le RGPD pour un bandeau de cookies ?", "Un simple avertissement~Un consentement libre, éclairé et tracé~Un refus impossible~Une acceptation par défaut", 1,
     "Le consentement doit être explicite, spécifique et aussi facile à refuser qu'à accepter."),
 QC("Quel effet d'une panne du site pendant une campagne publicitaire ?", "Une hausse du taux de conversion~Une perte de commandes et une dégradation de la marque~Une baisse du trafic publicitaire~Une augmentation de la fidélité", 1,
     "L'indisponibilité se traduit par des ventes manquées et une dégradation de la confiance."),
 QT("Un site e-commerce reçoit 20 000 visiteurs, enregistre 600 commandes et 14 000 paniers abandonnés. Calculer le taux de conversion et commenter.",
    "Le taux de conversion vaut 600 / 20 000 = 0,03, soit 3 %. Le taux d'abandon de panier, rapporté aux paniers créés (600 + 14 000 = 14 600), vaut 14 000 / 14 600 ≈ 95,9 %. Ces chiffres montrent que le trafic est relativement bien attiré mais que la finalisation est très faible : l'abandon massif peut venir de frais de livraison révélés tardivement, d'un parcours de paiement trop long, de problèmes techniques ou d'un manque de moyens de paiement. On recommande d'analyser le tunnel de conversion, de tester le parcours sur différents appareils, de clarifier les coûts dès la fiche produit et de mesurer l'effet des corrections.",
    "On calcule 3 % et environ 96 % d'abandon, puis on propose une analyse du tunnel et des causes."),
 QT("Expliquer comment concilier personnalisation de l'offre et protection des données clients.",
    "La personnalisation utilise l'historique d'achat, la navigation et les préférences déclarées pour proposer des produits pertinents. Ces traitements reposent le plus souvent sur le consentement ou l'intérêt légitime, mais ils doivent respecter la minimisation des données, une finalité déterminée et une durée de conservation limitée. Le RGPD impose une information claire, la possibilité de s'opposer au profilage, l'accès et l'effacement des données, ainsi qu'un registre des traitements. Techniquement, on peut pseudonymiser les identifiants, agréger les statistiques, limiter les accès, chiffrer les bases et tracer les consentements. La transparence est aussi un avantage commercial : expliquer pourquoi un produit est recommandé et laisser le contrôle à l'utilisateur renforce la confiance.",
    "On articule bénéfice commercial, bases légales, droits des personnes et mesures techniques de minimisation.")],
C("Le e-commerce combine performance commerciale, logistique et conformité : conversion, paiement sécurisé et données clients sont indissociables.",
  "Taux de conversion = commandes / visiteurs uniques",
  "B2C · B2B · C2C · PCI DSS · RGPD · dernier kilomètre",
  "B2C~Vers le consommateur~Taux de conversion~Commandes sur visiteurs~Panier moyen~Valeur par commande~PCI DSS~Sécurité des paiements~Dernier kilomètre~Coût de livraison",
  "Mesurer le trafic et la conversion|Analyser le tunnel d'achat|Sécuriser le paiement|Respecter les droits des clients|Fiabiliser la livraison et le SAV",
  "Révéler les frais de livraison en fin de parcours|Stocker des données de carte|Consentement cookie implicite|Ignorer les indicateurs d'abandon",
  "20 000 visiteurs et 600 commandes~Conversion 3 %~14 000 paniers abandonnés~Environ 96 % d'abandon~PCI DSS~Jetons de paiement~RGPD~Droits d'accès et d'effacement~Conversion~Indicateur clé",
  "Taux de conversion~Commandes finalisées~Taux d'abandon~Paniers non finalisés",
  "B2C~Consommateur~B2B~Entreprise"))

# ============================================================ EC7
add("EC7", "Financement de l'innovation et arbitrage des projets SI", "Économie", ["BTS2"],
S("Un projet d'innovation informatique mobilise des ressources avant de produire des bénéfices : son financement doit être arbitré comme un investissement."
  "|Les ressources internes (autofinancement, budget de fonctionnement) offrent de l'autonomie mais limitent le montant et exposent l'entreprise au risque du projet."
  "|Le financement externe peut prendre la forme d'un emprunt bancaire, d'une subvention publique, d'un crédit d'impôt, d'une levée de fonds ou d'un crédit-bail."
  "|Le crédit-bail permet d'utiliser un équipement moyennant un loyer, avec une option d'achat en fin de contrat : il préserve la trésorerie."
  "|Les aides publiques, comme le crédit d'impôt recherche ou les dispositifs régionaux, réduisent le coût net mais imposent des justificatifs et un suivi."
  "|Le coût du capital est le rendement minimal exigé par les financeurs : il sert de taux d'actualisation pour évaluer le projet."
  "|Un projet est créateur de valeur si sa valeur actuelle nette est positive au coût du capital, c'est-à-dire si les gains actualisés dépassent l'investissement."
  "|Le rapprochement des flux de trésorerie prévisionnels permet de vérifier que l'entreprise peut faire face aux échéances, même si le projet est rentable à long terme."
  "|Le plan de trésorerie intègre le calendrier des décaissements (achats, développement, formation) et des encaissements (économies, recettes, subventions)."
  "|Le risque technologique est élevé dans les projets innovants : les prototypes, tests et phases pilotes permettent de réduire l'incertitude avant le déploiement."
  "|La méthode des scénarios (optimiste, central, pessimiste) et l'analyse de sensibilité testent la robustesse de la décision face aux hypothèses."
  "|Pour un projet de cybersécurité, le bénéfice est souvent un risque évité : on le documente par des indicateurs de conformité, de disponibilité et de pertes potentielles."),
[QC("Quel mode de financement préserve la trésorerie tout en donnant accès à un équipement ?", "L'autofinancement intégral~Le crédit-bail~L'augmentation de capital~Le prêt à long terme", 1,
     "Le crédit-bail étale la dépense en loyers avec une option d'achat finale."),
 QC("Que désigne le coût du capital ?", "Le prix d'achat d'un serveur~Le rendement minimal exigé par les financeurs~Le salaire du chef de projet~La durée du projet", 1,
     "Il sert de taux d'actualisation dans l'évaluation des investissements."),
 QC("Quand un projet est-il créateur de valeur ?", "Quand sa VAN est positive~Quand son coût est nul~Quand il dure moins d'un an~Quand il n'utilise pas de données", 0,
     "Une VAN positive au coût du capital signifie que le projet dépasse l'exigence de rentabilité."),
 QC("Quel est l'objet d'un plan de trésorerie ?", "Fixer les prix de vente~Suivre les décaissements et encaissements prévisionnels~Recruter~Rédiger le cahier des charges", 1,
     "Il vérifie la capacité à faire face aux échéances de paiement."),
 QC("Que permet la méthode des scénarios ?", "De garantir le succès~De tester la robustesse face à des hypothèses variées~De supprimer les risques~De réduire le nombre de réunions", 1,
     "On compare une situation optimiste, centrale et pessimiste."),
 QC("Quel dispositif public finance la recherche et le développement en France ?", "Le crédit d'impôt recherche~Le SMIC~Le TAEG~Le BFR", 0,
     "Le CIR est un dispositif fiscal de soutien à la recherche et au développement."),
 QC("Comment justifier un projet de cybersécurité dont le bénéfice est un risque évité ?", "En promettant un chiffre d'affaires garanti~En documentant conformité, disponibilité et pertes évitées~En supprimant les indicateurs~En réduisant la durée du projet", 1,
     "La valeur est mesurée par la réduction du risque et de ses impacts potentiels."),
 QC("Que permet une phase pilote ?", "Augmenter le risque technologique~Réduire l'incertitude avant le déploiement~Supprimer la recette~Éviter la formation des utilisateurs", 1,
     "Le prototype et le test valident les hypothèses techniques et organisationnelles."),
 QT("Une entreprise doit choisir entre acheter 50 postes pour 60 000 € ou les louer en crédit-bail pour 1 400 € par mois sur 36 mois. Comparer les deux options et préciser les éléments manquants pour trancher.",
    "L'achat immobilise 60 000 € immédiatement et donne la propriété des postes, avec une valeur de revente en fin de vie et une durée de vie potentiellement supérieure à 36 mois. Le crédit-bail coûte 1 400 × 36 = 50 400 € sur la période, soit moins que le prix d'achat nominal, mais il ne donne pas la propriété immédiate et l'option d'achat finale reste à préciser. Pour trancher, il manque la durée de vie réelle des postes, la valeur résiduelle, le coût de maintenance, le taux d'actualisation, le traitement fiscal et l'impact sur le BFR. Si l'entreprise a une trésorerie tendue, le loyer préserve sa capacité d'investissement ; si elle utilise les postes au-delà de trois ans, l'achat peut devenir plus avantageux.",
    "On compare 60 000 € et 50 400 €, puis on identifie durée de vie, valeur résiduelle, taux et trésorerie comme éléments décisifs."),
 QT("Expliquer pourquoi une analyse de sensibilité est indispensable dans un projet d'innovation informatique.",
    "Les prévisions d'un projet innovant reposent sur des hypothèses incertaines : coût de développement, adoption par les utilisateurs, performance de la technologie, évolution du prix des licences ou du cloud et calendrier de mise en œuvre. Une analyse de sensibilité fait varier chaque hypothèse et observe l'effet sur la VAN, le seuil de rentabilité ou la trésorerie. Elle révèle les variables critiques, celles dont une petite variation change la décision, et permet de concentrer les efforts de réduction du risque sur elles : prototype, clause de révision, pilote ou provision. Elle complète les scénarios optimiste, central et pessimiste et rend la décision transparente pour les financeurs, sans prétendre éliminer l'incertitude.",
    "On relie incertitude des hypothèses, variables critiques, actions de mitigation et transparence de la décision.")],
C("Financer un projet SI, c'est arbitrer entre ressources internes et externes, rentabilité et trésorerie, dans un contexte d'incertitude technologique.",
  "VAN positive au coût du capital = création de valeur",
  "Crédit-bail · CIR · plan de trésorerie · scénarios · analyse de sensibilité",
  "Autofinancement~Ressources internes~Crédit-bail~Loyer et option d'achat~Coût du capital~Taux d'actualisation~VAN~Création de valeur~Trésorerie~Échéances",
  "Estimer investissement et gains|Choisir un mode de financement|Établir le plan de trésorerie|Calculer VAN et seuil|Tester les scénarios et décider",
  "Confondre rentabilité et trésorerie|Ignorer la valeur résiduelle|Oublier le coût du capital|Présenter un seul scénario",
  "60 000 €~Achat de 50 postes~50 400 €~Loyer sur 36 mois~VAN positive~Projet créateur de valeur~CIR~Aide à la R&D~Pilote~Réduction du risque",
  "Achat~Propriété immédiate~Crédit-bail~Usage étalé avec option",
  "Risque évité~Bénéfice des projets de sécurité~Risque pris~Bénéfice attendu"))

# ============================================================ MA1
add("MA1", "Gestion de projet informatique : cycle et pilotage", "Management", ["BTS1"],
S("Un projet est un ensemble d'activités temporaires entreprises pour créer un produit ou un service unique, avec des contraintes de coût, de délai et de qualité."
  "|Le cycle de projet comprend l'initialisation, la planification, l'exécution, le suivi et la clôture."
  "|L'initialisation formalise le besoin, les objectifs, les parties prenantes et la charte de projet qui donne l'autorité au chef de projet."
  "|La planification décrit le périmètre, la structure de découpage du travail (WBS), les tâches, les dépendances, les ressources et le budget."
  "|Le diagramme de Gantt visualise les tâches dans le temps ; le chemin critique identifie la séquence de tâches qui détermine la durée minimale du projet."
  "|La méthode agile (Scrum, Kanban) privilégie les itérations courtes, la collaboration avec le client et l'adaptation aux changements de périmètre."
  "|La méthode cycle en cascade (waterfall) enchaîne des phases séquentielles avec des livrables et des points de validation : elle convient aux besoins stables et réglementés."
  "|Le suivi compare l'avancement réel au plan : indicateurs de coût (CPI), de délai (SPI), charge de travail et respect des jalons."
  "|La gestion des risques identifie, évalue et traite les menaces avec un plan d'action, un responsable et une date d'échéance."
  "|La conduite du changement accompagne les utilisateurs : information, formation, support et recette sont nécessaires à l'adoption d'un nouveau système."
  "|La clôture prononce la recette, archive les livrables, libère les ressources et organise le retour d'expérience."
  "|En option IR, le projet technique évalué en U6 mobilise ces compétences : cahier des charges, planning, suivi, démonstration et soutenance."),
[QC("Quelles sont les contraintes classiques d'un projet ?", "Coût, délai, qualité~Couleur, forme, taille~Prix, marque, publicité~Serveur, réseau, câble", 0,
     "Le triangle d'or du projet articule coût, délai et qualité."),
 QC("Quel document donne l'autorité au chef de projet ?", "Le devis~La charte de projet~La facture~Le contrat de maintenance", 1,
     "La charte de projet légitime le chef de projet et cadre son mandat."),
 QC("Que désigne le WBS ?", "Un réseau sans fil~Le découpage hiérarchique des tâches~Un type de base de données~Un outil de dessin", 1,
     "Le work breakdown structure décompose le périmètre en livrables et tâches."),
 QC("Quel est le rôle du chemin critique ?", "Déterminer la durée minimale du projet~Réduire le coût des salaires~Supprimer les réunions~Fixer le prix de vente", 0,
     "Tout retard sur le chemin critique retarde la date de fin prévue."),
 QC("Quelle méthode privilégie les itérations courtes et l'adaptation ?", "Cycle en cascade~Agile~PDCA~PERT", 1,
     "Les méthodes agiles organisent le travail en sprints avec revues régulières."),
 QC("Que mesure l'indicateur SPI ?", "Le respect du budget~Le respect du calendrier~La qualité du code~La satisfaction client", 1,
     "Le schedule performance index compare avancement prévu et avancement réel."),
 QC("Quelle phase clôture le projet ?", "L'exécution~La planification~La recette et le retour d'expérience~L'initialisation", 2,
     "La clôture comprend recette, archivage et capitalisation."),
 QC("Pourquoi accompagner le changement ?", "Pour augmenter le nombre de serveurs~Pour favoriser l'adoption du système par les utilisateurs~Pour réduire la durée des réunions~Pour supprimer la documentation", 1,
     "La conduite du changement traite la dimension humaine du projet."),
 QT("Un projet de migration de serveurs prend six semaines de retard. Décrire la démarche de pilotage pour analyser et corriger la situation.",
    "On confirme d'abord l'écart avec les indicateurs : jalons non atteints, SPI, avancement des tâches et charge réelle. On identifie ensuite les causes avec l'équipe : dépendance externe non livrée, sous-estimation des temps, ressource absente, périmètre ajouté sans arbitrage ou incident technique. On met à jour le chemin critique pour voir quelles tâches déterminent désormais la fin. On propose alors des actions : renégocier une date, ajouter une ressource sur une tâche critique, réduire le périmètre non prioritaire avec l'accord du commanditaire, ou accepter un décalage du passage en production. On documente la décision, on informe les parties prenantes et on resserre le rythme de suivi jusqu'au retour à la normale.",
    "On suit : mesure de l'écart, recherche de causes, analyse du chemin critique, arbitrage, communication et suivi renforcé."),
 QT("Comparer la méthode agile et le cycle en cascade pour un projet de refonte d'un réseau d'entreprise.",
    "Le cycle en cascade déroule des phases séquentielles : expression du besoin, conception, réalisation, tests, déploiement. Il offre une documentation complète et des points de validation formels, ce qui rassure dans un projet à fortes contraintes de conformité ou de sécurité, mais il réagit mal aux changements tardifs. L'agile découpe le travail en itérations courtes avec des livrables incrémentaux, des revues avec les parties prenantes et une priorisation continue du backlog. Il convient lorsque le besoin évolue et que l'on peut tester progressivement, par exemple sur la supervision ou le portail utilisateur. En pratique, un projet réseau combine souvent les deux : cadrage et architecture en cascade, puis configuration et tests en itérations, avec des fenêtres de maintenance planifiées.",
    "On compare structure, réactivité, documentation et pertinence selon le contexte, puis on propose une approche hybride.")],
C("Piloter un projet informatique, c'est cadrer, planifier, suivre et clôturer en maîtrisant coût, délai, qualité et changement humain.",
  "Projet = temporaire + unique + contraintes coût, délai, qualité",
  "WBS · Gantt · chemin critique · agile ou cascade · SPI/CPI · recette",
  "Initialisation~Charte et parties prenantes~Planification~WBS et Gantt~Exécution~Réalisation des livrables~Suivi~SPI et CPI~Clôture~Recette et REX",
  "Cadrer le besoin et les parties prenantes|Découper les tâches et estimer|Planifier les ressources et le budget|Suivre les indicateurs et arbitrer|Recette, capitalisation et clôture",
  "Ajouter du périmètre sans arbitrage|Ignorer le chemin critique|Négliger la conduite du changement|Clore sans retour d'expérience",
  "Charte~Autorité du chef de projet~Chemin critique~Durée minimale~SPI~Respect du calendrier~Agile~Itérations courtes~Recette~Validation finale",
  "Cycle en cascade~Phases séquentielles~Agile~Itérations et adaptation",
  "SPI~Performance du délai~CPI~Performance du coût"))

# ============================================================ MA2
add("MA2", "Gouvernance de la sécurité des systèmes d'information", "Management", ["BTS1"],
S("La gouvernance de la sécurité des systèmes d'information (SSI) définit qui décide, quelles règles s'appliquent et comment leur respect est contrôlé."
  "|Elle s'appuie sur une politique de sécurité approuvée par la direction, déclinée en procédures, instructions et normes techniques."
  "|La norme ISO/IEC 27001 spécifie les exigences d'un système de management de la sécurité de l'information (ISMS) et repose sur un cycle d'amélioration continue."
  "|L'ISO/IEC 27002 fournit les bonnes pratiques de contrôles : politiques, ressources humaines, gestion des actifs, accès, cryptographie, exploitation, communications et conformité."
  "|La démarche de risque comprend l'identification des actifs, l'évaluation des menaces et vulnérabilités, le calcul du risque et le choix d'un traitement : éviter, réduire, transférer ou accepter."
  "|Un responsable de la sécurité des systèmes d'information (RSSI) pilote la politique, coordonne les actions et rend compte à la direction."
  "|Les rôles et responsabilités doivent être explicites : propriétaire des actifs, responsable applicatif, administrateur, utilisateur et auditeur."
  "|La gestion des accès, la sensibilisation, la gestion des correctifs, les sauvegardes et la réponse à incident sont des processus clés de la gouvernance."
  "|Les indicateurs de sécurité (KPI) mesurent par exemple le taux de correctifs appliqués dans le délai, le nombre d'incidents ou le taux de réussite aux tests de hameçonnage."
  "|La conformité réglementaire (RGPD, NIS2, exigences contractuelles) est intégrée au système de management plutôt que traitée au cas par cas."
  "|Le cycle Plan-Do-Check-Act structure l'amélioration : planifier les contrôles, les appliquer, mesurer leur efficacité puis corriger."
  "|Pour le technicien CIEL, la gouvernance explique pourquoi une procédure existe et pourquoi chaque action doit être tracée."),
[QC("Quelle norme spécifie un système de management de la sécurité de l'information ?", "ISO 9001~ISO/IEC 27001~ISO 14001~PCI DSS", 1,
     "L'ISO/IEC 27001 définit les exigences d'un ISMS."),
 QC("Quel cycle d'amélioration continue sous-tend l'ISO 27001 ?", "PDCA~4P~SMART~SWOT", 0,
     "Plan - Do - Check - Act structure l'amélioration continue."),
 QC("Quel est le rôle du RSSI ?", "Administrer les routeurs~Piloter la politique de sécurité et coordonner les actions~Remplacer la direction~Signer les contrats", 1,
     "Le responsable SSI pilote la politique, les risques et la conformité."),
 QC("Quel traitement du risque consiste à souscrire une assurance cyber ?", "Éviter~Réduire~Transférer~Accepter", 2,
     "Le transfert délège tout ou partie de l'impact financier à un tiers."),
 QC("Quelle est la première étape de la gestion des risques ?", "Acheter un antivirus~Identifier les actifs et les menaces~Supprimer les journaux~Former les utilisateurs", 1,
     "On ne peut évaluer que ce que l'on a identifié au préalable."),
 QC("Quel indicateur mesure la sensibilisation des utilisateurs ?", "Le taux de réussite aux tests de hameçonnage~Le nombre de serveurs~La taille du budget~Le nombre de câbles", 0,
     "Les campagnes de test permettent de mesurer l'efficacité de la sensibilisation."),
 QC("Qui approuve la politique de sécurité ?", "Le seul RSSI~La direction de l'organisation~Le fournisseur d'accès~Chaque utilisateur", 1,
     "La politique SSI doit être portée et approuvée par la direction."),
 QC("Pourquoi intégrer la conformité dans le système de management ?", "Pour éviter toute documentation~Pour traiter les obligations de façon durable et coordonnée~Pour supprimer les audits~Pour réduire le nombre de contrôles", 1,
     "La conformité devient un processus piloté plutôt qu'une réaction ponctuelle."),
 QT("Expliquer les quatre traitements possibles d'un risque de sécurité et donner un exemple pour chacun.",
    "Éviter : supprimer l'activité à l'origine du risque, par exemple interdire l'usage de clés USB non chiffrées. Réduire : mettre en place des contrôles qui diminuent la probabilité ou l'impact, comme la MFA, les correctifs ou la segmentation. Transférer : partager l'impact avec un tiers, par exemple une assurance cyber ou un contrat de sous-traitance avec garanties. Accepter : conserver le risque lorsque son impact est faible ou que le coût du traitement est disproportionné, avec une décision explicite et documentée par la direction. Le choix dépend du niveau de risque résiduel, du coût des contrôles et des obligations réglementaires ; il doit être réévalué régulièrement.",
    "On nomme et illustre les quatre options, puis on rappelle la décision documentée et le réexamen."),
 QT("Une direction demande « d'être conforme ISO 27001 en trois mois ». Expliquer la démarche réaliste et les limites d'un tel objectif.",
    "La certification ISO 27001 suppose la mise en place d'un système de management complet : définition du périmètre et de la politique, inventaire des actifs, analyse des risques et plan de traitement, rédaction des procédures, formation, application des contrôles, audits internes et revue de direction avant un audit de certification. Trois mois peuvent suffire pour une structure très petite et déjà organisée, mais pas pour une organisation complexe : les indicateurs doivent fonctionner sur une période suffisante et les preuves d'application être accumulées. Une approche réaliste consiste à viser d'abord une conformité pragmatique aux contrôles prioritaires, à documenter les écarts et à planifier la certification sur la base d'un calendrier validé. Promettre une certification sans preuves exposerait l'organisation à un échec d'audit et à une perte de crédibilité.",
    "On décrit les étapes ISMS, la nécessité de preuves et de recul, puis on propose une conformité progressive et honnête.")],
C("La gouvernance SSI rend la sécurité pilotable : politique, rôles, risques, contrôles et indicateurs forment un système d'amélioration continue.",
  "Risque = probabilité × impact · PDCA",
  "ISO/IEC 27001 et 27002 · RSSI · traitements : éviter, réduire, transférer, accepter",
  "Politique SSI~Règles approuvées~RSSI~Pilote de la sécurité~ISO 27001~Exigences ISMS~Analyse de risques~Menaces et impacts~PDCA~Amélioration continue",
  "Approuver la politique|Identifier actifs et risques|Choisir les traitements|Appliquer les contrôles|Mesurer et auditer",
  "Confondre RSSI et administrateur|Ignorer les risques résiduels|Ne jamais revoir la politique|Multiplier les contrôles sans indicateur",
  "PDCA~Plan Do Check Act~ISO 27001~Certification ISMS~MFA~Réduction du risque~Assurance cyber~Transfert~KPI~Indicateurs de sécurité",
  "Réduire~Contrôles de sécurité~Transférer~Assurance ou sous-traitance",
  "Politique~Principes directeurs~Procédure~Mode opératoire"))

# ============================================================ MA3
add("MA3", "Management d'une équipe technique et conduite de réunion", "Management", ["BTS1"],
S("Manager une équipe technique, c'est fixer un cap, répartir les tâches, accompagner les compétences et contrôler la qualité du travail réalisé."
  "|Le manager doit articuler les objectifs de l'organisation, les attentes des clients internes et les besoins de développement des collaborateurs."
  "|La fixation d'objectifs SMART rend les attentes mesurables : spécifiques, mesurables, atteignables, pertinentes et temporellement définies."
  "|La répartition des tâches tient compte des compétences, de la charge de travail et de la montée en compétences : elle évite la surcharge d'un expert unique."
  "|La délégation transfère une responsabilité avec les moyens correspondants, tout en conservant un droit de contrôle et un devoir de suivi."
  "|La réunion efficace a un ordre du jour, des participants nécessaires, un animateur, un secrétaire, un temps défini et un compte rendu dacté."
  "|Les points de situation quotidiens (stand-up agile) synchronisent l'équipe : qu'a-t-on fait, que fait-on, quels obstacles rencontre-t-on ?"
  "|Le feedback régulier, positif et correctif, permet d'ajuster les pratiques sans attendre l'entretien annuel."
  "|La gestion de conflits repose sur l'écoute, la reformulation, la recherche d'intérêts communs et, si nécessaire, l'arbitrage du manager."
  "|La motivation repose sur la reconnaissance, l'autonomie, la compréhension du sens et l'équité de traitement, plus que sur la seule rémunération."
  "|Dans une équipe SSI, la culture de la remontée d'incident est essentielle : un collaborateur doit pouvoir signaler une erreur sans crainte de sanction disproportionnée."
  "|Le télétravail et les équipes distribuées imposent des rituels écrits, des outils collaboratifs et une attention particulière à la charge mentale."),
[QC("Que signifie l'acronyme SMART pour un objectif ?", "Simple, Moyen, Ambitieux, Réel, Temps~Spécifique, Mesurable, Atteignable, Pertinent, Temporel~Stratégique, Marché, Action, Résultat, Team~Social, Management, Audit, Risque, Travail", 1,
     "Les cinq critères SMART cadrent un objectif et permettent de le mesurer."),
 QC("Que suppose une délégation réussie ?", "Transférer la tâche sans suivi~Donner responsabilité, moyens et suivi~Contrôler chaque minute~Refuser tout feedback", 1,
     "Déléguer, c'est responsabiliser avec les moyens et garder un contrôle a posteriori."),
 QC("Quel élément n'est pas indispensable à une réunion efficace ?", "Un ordre du jour~Un compte rendu~Un animateur~Une salle de réunion", 3,
     "Une réunion peut être distancielle ; l'ordre du jour et le compte rendu restent nécessaires."),
 QC("Quel est l'objet d'un stand-up quotidien ?", "Faire un rapport annuel~Synchroniser l'équipe et identifier les obstacles~Signer les contrats~Rédiger le cahier des charges", 1,
     "Le rituel court répond à trois questions : fait, à faire, blocages."),
 QC("Quelle attitude favorise la remontée d'incidents ?", "Sanctionner toute erreur~Instaurer une culture de confiance et d'apprentissage~Ignorer les signalements~Reporter la décision", 1,
     "La transparence est indispensable pour traiter les incidents rapidement."),
 QC("Quel levier de motivation est cité en management ?", "La seule augmentation de salaire~La reconnaissance et le sens donné au travail~La réduction du nombre de réunions à zéro~L'absence d'objectifs", 1,
     "Reconnaissance, autonomie et sens sont des moteurs durables de l'engagement."),
 QC("Comment traiter un conflit d'équipe ?", "L'ignorer~Écouter, reformuler puis rechercher un accord ou arbitrer~Changer toute l'équipe~Refuser d'en parler", 1,
     "La méthode alterne écoute, reformulation, recherche d'intérêts communs et arbitrage."),
 QC("Quel outil aide une équipe distribuée ?", "Un tableau Kanban partagé~Une réunion sans ordre du jour~Une absence de documentation~Le silence prolongé", 0,
     "Les outils collaboratifs et les rituels écrits compensent l'absence de contact direct."),
 QT("Un administrateur très compétent accumule les astreintes et devient un point de défaillance unique. Comment le manager doit-il réagir ?",
    "Le manager analyse d'abord la charge réelle et les tâches critiques qui reposent sur cette personne. Il organise ensuite un transfert de compétences : documentation des procédures, binôme, montée en compétence d'un ou deux collègues, tournées d'astreinte équilibrées et révision des processus pour supprimer les tâches inutiles. Il fixe des objectifs SMART de progression pour les autres membres et prévoit un suivi dans le temps. Il doit aussi reconnaître la contribution de l'expert tout en évitant de le enfermer dans un rôle de « héros » : l'objectif est de rendre l'équipe résiliente, pas de sacrifier la performance actuelle. Enfin, il mesure l'effet sur les délais de traitement et la charge d'astreinte.",
    "On diagnostique la charge, on documente et transmet, on équilibre les astreintes, on reconnaît l'expert et on mesure."),
 QT("Expliquer comment conduire une réunion de retour d'expérience après un incident de sécurité.",
    "La réunion se prépare : participants concernés, ordre du jour, faits établis et données collectées. Elle s'ouvre sur un rappel du cadre : l'objectif est d'apprendre, non de chercher un coupable, ce qui favorise la parole. On reconstitue la chronologie à partir des journaux, on identifie ce qui a bien fonctionné et les points de friction, puis on analyse les causes avec la méthode des 5 Pourquoi. On formule des actions correctrices avec un responsable, une échéance et un indicateur de suivi. Le compte rendu est diffusé, les actions sont inscrites dans un tableau de bord et leur réalisation est vérifiée à une date fixée. La confidentialité des informations sensibles reste respectée pendant et après la réunion.",
    "On attend préparation, cadre non culpabilisant, chronologie, causes, actions datées et suivi.")],
C("Manager une équipe technique, c'est donner un cap, répartir la charge, faire grandir les compétences et instaurer une culture de la transparence.",
  "Objectif SMART = spécifique, mesurable, atteignable, pertinent, temporel",
  "Délégation · rituels · feedback · conflits · culture de remontée d'incidents",
  "Objectifs SMART~Cadre mesurable~Délégation~Responsabilité et moyens~Réunion~Ordre du jour et compte rendu~Feedback~Retour régulier~Résilience~Équipe non dépendante d'un expert",
  "Fixer des objectifs|Répartir les tâches et les astreintes|Animer les rituels d'équipe|Accompagner et donner du feedback|Capitaliser après incident",
  "Centraliser toutes les astreintes sur un expert|Réunir sans ordre du jour|Chercher un coupable en REX|Ignorer les signes de surcharge",
  "SMART~Objectif cadré~Stand-up~Synchronisation courte~Kanban~Visualisation des tâches~REX~Retour d'expérience~Astreinte~Disponibilité",
  "Délégation~Responsabilité confiée~Abandon~Responsabilité non assumée",
  "Feedback positif~Reconnaître~Feedback correctif~Ajuster"))

# ============================================================ MA4
add("MA4", "Audit et conformité des systèmes d'information", "Management", ["BTS2"],
S("L'audit informatique est un examen indépendant et objectif visant à évaluer la conformité, l'efficacité et la sécurité d'un système d'information."
  "|On distingue l'audit interne, réalisé par des collaborateurs de l'organisation, et l'audit externe, mené par un cabinet indépendant ou un organisme certificateur."
  "|L'audit de conformité vérifie l'application des textes (RGPD, NIS2) et des normes (ISO 27001, PCI DSS) ; l'audit opérationnel évalue l'efficacité des processus."
  "|L'audit technique contrôle la configuration des équipements, les droits d'accès, les journaux, les sauvegardes et les correctifs."
  "|La planification définit le périmètre, les objectifs, les critères, l'équipe, le calendrier et les documents à fournir."
  "|Les tests peuvent porter sur des échantillons de comptes, de journaux ou de machines : la méthode d'échantillonnage doit être documentée."
  "|Les outils d'audit incluent les scanners de vulnérabilités, les contrôles de configuration, les analyseurs de journaux et les entretiens avec les acteurs."
  "|Un constat d'audit se rédige de façon factuelle : fait observé, critère de référence, écart, impact potentiel et recommandation."
  "|Les écarts sont classés par criticité (majeur, mineur, observation) et donnent lieu à un plan d'action avec responsable et échéance."
  "|Le rapport d'audit distingue les points forts, les non-conformités et les axes d'amélioration ; il est remis à la direction et archivé."
  "|Le suivi des actions est aussi important que l'audit lui-même : sans vérification de la remédiation, la non-conformité persiste."
  "|Pour un technicien CIEL, préparer un audit suppose d'avoir des procédures à jour, des preuves traçables et des accès documentés."),
[QC("Quelle est la première caractéristique d'un audit ?", "Il est confidentiel et secret~Il est indépendant et objectif~Il est réalisé par le fournisseur~Il est gratuit", 1,
     "L'indépendance et l'objectivité sont essentielles à la crédibilité de l'audit."),
 QC("Quel audit vérifie l'application d'une norme ou d'un texte ?", "Audit opérationnel~Audit de conformité~Audit financier~Audit de sécurité physique", 1,
     "L'audit de conformité compare la pratique aux exigences de référence."),
 QC("Que contient un constat d'audit bien rédigé ?", "Une opinion personnelle~Fait, critère, écart, impact et recommandation~Une note chiffrée seule~Une simple photo", 1,
     "La rédaction factuelle permet de comprendre et de traiter l'écart."),
 QC("Quel classement de criticité est courant ?", "Majeur, mineur, observation~Rouge, bleu, vert~A, B, C~Urgent, lent, rapide", 0,
     "Les écarts sont généralement classés en majeurs, mineurs et observations."),
 QC("Que doit prévoir un plan d'action d'audit ?", "Un responsable et une échéance par action~Un simple souhait~Une réunion sans suite~Une sanction automatique", 0,
     "Chaque action doit être attribuée, datée et mesurable."),
 QC("Quel outil permet de vérifier la configuration des équipements ?", "Un scanner de vulnérabilités~Un lecteur de courriels~Un éditeur d'images~Un tableur vide", 0,
     "Les scanners et outils de contrôle de configuration analysent les paramètres et les failles."),
 QC("Pourquoi documenter la méthode d'échantillonnage ?", "Pour augmenter le nombre d'écarts~Pour rendre l'audit reproductible et juste~Pour éviter les entretiens~Pour réduire la durée", 1,
     "La traçabilité de la méthode garantit la fiabilité des conclusions."),
 QC("Quelle est la dernière étape du processus d'audit ?", "La planification~La remise du rapport~Le suivi des actions correctives~La collecte des preuves", 2,
     "Sans suivi de remédiation, l'audit n'apporte pas d'amélioration durable."),
 QT("Un audit révèle que 30 % des comptes d'un annuaire n'ont pas de propriétaire identifié. Rédiger un constat structuré et proposer un plan d'action.",
    "Constat : sur un échantillon de 100 comptes actifs prélevé le 12 novembre dans l'annuaire de production, 30 comptes n'ont aucun propriétaire ou responsable métier renseigné. Critère : la procédure interne de gestion des identités impose que chaque compte soit rattaché à une personne et à un rôle, conformément au référentiel ISO 27002 sur la gestion des accès. Écart : absence d'information de propriété pour 30 % de l'échantillon. Impact : difficulté à révoquer les accès lors d'un départ et risque de comptes orphelins exploitables. Recommandation : lancer une campagne de qualification des comptes, automatiser le champ propriétaire à la création, et intégrer un contrôle mensuel. Plan d'action : responsable désigné, échéance à 30 jours, indicateur de suivi = pourcentage de comptes avec propriétaire, cible 100 %.",
    "On rédige fait, critère, écart, impact et recommandation, puis un plan d'action avec responsable, délai et indicateur."),
 QT("Expliquer la différence entre audit interne et audit externe et pourquoi les deux sont utiles.",
    "L'audit interne est réalisé par des collaborateurs ou par un service d'audit de l'organisation. Il connaît bien le contexte, est moins coûteux et peut être fréquent : il sert à vérifier en continu que les contrôles sont appliqués et à préparer les échéances externes. L'audit externe est mené par un cabinet indépendant ou un organisme certificateur : son regard est libre des habitudes internes, ses conclusions sont crédibles vis-à-vis des clients, des autorités et des assureurs, et il peut conduire à une certification. Sa limite est son coût et son caractère ponctuel. Les deux se complètent : l'audit interne assure la vigilance quotidienne et la remédiation, l'audit externe valide la conformité à un référentiel et apporte une garantie extérieure.",
    "On oppose proximité et coût, indépendance et crédibilité, puis complémentarité et certification.")],
C("L'audit évalue objectivement la conformité et l'efficacité du SI : constats factuels, criticité et suivi des actions en sont le cœur.",
  "Constat = fait observé + critère + écart + impact + recommandation",
  "Audit interne ou externe · ISO 27001/27002 · plan d'action · suivi",
  "Audit interne~Regard interne~Audit externe~Indépendance et certification~Constat~Fait et écart~Criticité~Majeur ou mineur~Plan d'action~Responsable et échéance",
  "Définir périmètre et critères|Collecter les preuves|Réaliser les tests|Rédiger les constats|Suivre la remédiation",
  "Rédiger des constats subjectifs|Oublier le critère de référence|Ne pas classer les écarts|Clore l'audit sans suivi",
  "30 comptes sans propriétaire~Écart documenté~30 jours~Échéance de remédiation~100 %~Cible de l'indicateur~ISO 27002~Référentiel de contrôles~Scanner~Outil d'audit",
  "Audit interne~Fréquent et contextualisé~Audit externe~Indépendant et crédible",
  "Non-conformité~Écart constaté~Observation~Point d'attention"))

# ============================================================ MA5
add("MA5", "Conduite de crise et gestion des incidents cyber", "Management", ["BTS2"],
S("Une crise cyber est un événement perturbateur qui menace la continuité, la réputation ou la conformité de l'organisation et exige une réponse coordonnée."
  "|La cellule de crise réunit la direction, le RSSI, les responsables métiers, la communication, le juridique et les équipes techniques."
  "|Un plan de continuité d'activité (PCA) définit les procédures pour maintenir les fonctions essentielles pendant la perturbation."
  "|Un plan de reprise d'activité (PRA) organise le retour au fonctionnement normal : priorités de restauration, ressources et responsabilités."
  "|Les objectifs clés sont le RTO (temps maximal d'interruption acceptable) et le RPO (perte de données maximale acceptable)."
  "|La première phase de gestion est la qualification : nature de l'attaque, périmètre touché, criticité des systèmes et impact sur les utilisateurs."
  "|Le confinement vise à stopper la propagation : isolement réseau, révocation des accès, désactivation de comptes et arrêt de services compromis."
  "|La communication interne et externe doit être structurée : un seul porte-parole, des messages factuels, une fréquence annoncée et des faits vérifiés."
  "|Les notifications réglementaires (CNIL 72 h, ANSSI en cas d'incident significatif) et les obligations contractuelles doivent être prévues dans la procédure."
  "|Les preuves sont conservées avec horodatage et hashes : elles servent à l'analyse, à l'assurance et aux autorités."
  "|Une crise se clôt par une phase de retour à la normale, puis par un retour d'expérience qui alimente le PCA, le PRA et la formation."
  "|Des exercices réguliers (tabletop, simulations) testent la procédure et révèlent les rôles oubliés ou les contacts obsolètes."),
[QC("Que désigne une cellule de crise ?", "Un serveur de sauvegarde~Le groupe qui coordonne la réponse~Un logiciel d'antivirus~Une salle de réunion vide", 1,
     "La cellule de crise réunit les décideurs et experts nécessaires à la réponse."),
 QC("Quel est l'objet d'un PCA ?", "Maintenir les fonctions essentielles pendant la crise~Réinstaller tous les postes~Rédiger le rapport final~Former les utilisateurs", 0,
     "Le plan de continuité vise à poursuivre l'activité malgré la perturbation."),
 QC("Que signifie RTO ?", "Perte de données acceptable~Temps maximal d'interruption acceptable~Taux de réussite des tests~Rendement du trésorier", 1,
     "Le Recovery Time Objective fixe le délai de rétablissement cible."),
 QC("Quelle est la première phase de la gestion d'un incident ?", "La qualification~La restauration~La communication~La clôture", 0,
     "On ne peut piloter que lorsque l'on a identifié la nature et l'impact de l'événement."),
 QC("Quel est un geste de confinement ?", "Rédiger un communiqué~Révoquer les accès compromis~Attendre le lendemain~Supprimer les journaux", 1,
     "Le confinement stoppe la propagation sans détruire les preuves."),
 QC("Combien de porte-parole faut-il privilégier en crise ?", "Un par service~Un seul, mandaté~Aucun~Tous les techniciens", 1,
     "Un porte-parole unique évite les messages contradictoires."),
 QC("Quel délai de notification RGPD doit être prévu dans la procédure ?", "24 h~72 h~7 jours~1 mois", 1,
     "La notification à la CNIL doit intervenir dans les 72 heures suivant la connaissance de la violation."),
 QC("À quoi servent les exercices de crise ?", "À occuper une journée~À tester la procédure et révéler les points faibles~À remplacer la documentation~À supprimer les sauvegardes", 1,
     "Les simulations améliorent la préparation et la coordination."),
 QT("Une attaque par rançongiciel touche un serveur de production. Décrire les premières actions de la cellule de crise dans l'ordre.",
    "La cellule se réunit immédiatement et nomme un responsable de la coordination. On qualifie l'incident : systèmes touchés, moment de la détection, type de chiffrement, portée réseau et critibilité des données. On isole les machines affectées du réseau, sans les éteindre systématiquement afin de préserver la mémoire et les preuves, puis on révoque les comptes et jetons compromis. On vérifie l'intégrité et la propreté des sauvegardes avant toute restauration. Parallèlement, le juridique et le DPO préparent la notification à la CNIL dans les 72 heures et, si l'activité est essentielle, l'alerte à l'ANSSI. Le porte-parole prépare une communication factuelle. Enfin, on consigne toutes les décisions dans un journal de crise horodaté.",
    "On attend : réunion et coordination, qualification, confinement, preuves, sauvegardes, notifications, communication et journal de crise."),
 QT("Expliquer comment articuler PCA et PRA et pourquoi les exercices sont indispensables.",
    "Le PCA vise à maintenir les services essentiels pendant la crise : bascule vers un site miroir, procédures dégradées, priorisation des applications et travail à distance. Le PRA intervient ensuite pour revenir à un état nominal : restauration des données propres, remise en service des applications, contrôle de sécurité et retour progressif des utilisateurs. Les deux plans reposent sur le RTO et le RPO, qui traduisent l'exigence de l'activité en contraintes techniques. Sans exercices, ces plans restent théoriques : contacts obsolètes, ordre de restauration inadapté, délais irréalistes ou rôles non attribués apparaissent au moment de l'incident. Des tests réguliers, y compris sous forme de simulation, permettent de corriger les procédures et de former les équipes dans un contexte calme.",
    "On distingue maintien et retour à la normale, on cite RTO et RPO, puis on justifie les exercices par la détection des faiblesses.")],
C("Une crise cyber se gère par une coordination, un confinement rapide, des preuves préservées et une communication maîtrisée.",
  "RTO = délai maximal d'interruption · RPO = perte de données maximale",
  "PCA · PRA · cellule de crise · notification 72 h · journal de crise",
  "Cellule de crise~Coordination des acteurs~PCA~Continuité pendant la crise~PRA~Retour à la normale~RTO~Délai cible~RPO~Perte maximale",
  "Réunir la cellule et qualifier|Confiner sans détruire les preuves|Vérifier les sauvegardes|Notifier et communiquer|Restaurer et capitaliser",
  "Éteindre systématiquement les machines|Multiplier les porte-parole|Restaurer sans contrôler les sauvegardes|Oublier la notification réglementaire",
  "72 h~Notification CNIL~RTO~Temps de reprise~RPO~Perte acceptable~Journal de crise~Décisions horodatées~Simulation~Test de procédure",
  "PCA~Pendant la crise~PRA~Après la crise",
  "Confinement~Stopper la propagation~Restauration~Revenir au normal"))

# ============================================================ MA6
add("MA6", "Veille technologique et pilotage des risques émergents", "Management", ["BTS2"],
S("La veille technologique est un processus continu de collecte, d'analyse et de diffusion d'informations sur les évolutions techniques et les menaces."
  "|Elle répond à un besoin de décision : choisir une architecture, anticiper une migration, évaluer une vulnérabilité ou former les équipes."
  "|Les sources fiables incluent les bulletins officiels (ANSSI, CISA, CERT), les avis des éditeurs, les bases CVE et CVSS, les normes et la littérature spécialisée."
  "|Le cycle de veille comprend la définition du besoin, le repérage des sources, la collecte, le filtrage, l'analyse, la diffusion et l'archivage."
  "|La criticité d'une vulnérabilité est appréciée avec le score CVSS et le contexte local : exposition, actifs concernés et existence d'un exploit public."
  "|Le délai entre la publication d'une faille et son exploitation par des attaquants se raccourcit : la priorisation des correctifs est devenue une compétence clé."
  "|La veille sur les menaces (CTI) analyse les tactiques, techniques et procédures des attaquants, notamment via le cadre MITRE ATT&CK."
  "|Les risques émergents concernent notamment l'intelligence artificielle générative, le cloud, l'internet des objets, la cryptographie post-quantique et les chaînes d'approvisionnement logicielles."
  "|La gestion des risques formalise l'identification, l'évaluation, le traitement et le suivi dans un registre des risques."
  "|Chaque risque est caractérisé par sa probabilité, son impact, son propriétaire, son traitement et son indicateur de suivi."
  "|La veille doit être ciblée : trop d'informations non filtrées conduit à l'épuisement de l'attention et à l'absence de décision."
  "|Les résultats sont diffusés sous forme de bulletins courts, d'alertes ou de points en réunion, avec une recommandation et une date de réexamen."),
[QC("Quel est l'objectif principal de la veille technologique ?", "Collecter toutes les actualités~Éclairer une décision technique ou de sécurité~Remplacer la formation~Rédiger des contrats", 1,
     "La veille doit produire de l'information actionnable pour la décision."),
 QC("Quelle source est fiable pour une vulnérabilité ?", "Un forum anonyme~Un bulletin ANSSI ou une fiche CVE~Une publication publicitaire~Un réseau social", 1,
     "Les avis d'autorités et les bases de référence sont privilégiés."),
 QC("Que mesure le score CVSS ?", "Le prix d'un logiciel~La gravité technique d'une vulnérabilité~La taille d'un réseau~La durée d'un contrat", 1,
     "Le Common Vulnerability Scoring System donne une note de sévérité normalisée."),
 QC("Quelle est la dernière étape du cycle de veille ?", "La collecte~Le filtrage~La diffusion et l'archivage~Le repérage des sources", 2,
     "Les informations analysées doivent être diffusées et conservées pour être réutilisées."),
 QC("Que désigne la CTI ?", "Un outil de sauvegarde~Le renseignement sur les menaces~Un type de cloud~Une norme comptable", 1,
     "Cyber Threat Intelligence analyse les menaces et les comportements d'attaquants."),
 QC("Quel cadre cartographie les tactiques des attaquants ?", "ITIL~MITRE ATT&CK~ISO 9001~SMART", 1,
     "MITRE ATT&CK est la matrice de référence des tactiques et techniques adverses."),
 QC("Quels champs contient un registre des risques ?", "Probabilité, impact, propriétaire, traitement~Nom, couleur, taille~Prix, date, facture~Serveur, port, câble", 0,
     "Le registre documente l'évaluation et le suivi de chaque risque."),
 QC("Quel effet d'une veille non filtrée ?", "Une meilleure décision~Une surcharge d'information et une paralysie~Une baisse des coûts~Une sécurité automatique", 1,
     "Sans filtrage ni priorisation, l'information devient du bruit."),
 QT("Une vulnérabilité critique est publiée un vendredi soir pour un logiciel utilisé sur 200 postes. Décrire la démarche de veille et de traitement.",
    "On vérifie d'abord la source et la fiche CVE : score CVSS, versions affectées, existence d'un correctif et d'un exploit public. On identifie ensuite les actifs concernés dans l'inventaire et on évalue l'exposition : postes accessibles depuis Internet, privilèges des utilisateurs, présence de compensations (firewall, MFA). On priorise : correction immédiate pour les systèmes exposés, puis déploiement massif via l'outil de gestion des correctifs, avec un test préalable sur un poste pilote si l'éditeur le recommande. On diffuse une alerte courte aux équipes avec les versions cibles et la date limite, on journalise le nombre de postes corrigés et on prévoit une exception pour les machines indisponibles. Enfin, on archive la fiche de veille et on inscrit le retour d'expérience dans le registre des risques.",
    "On suit : vérification de source, cartographie des actifs, évaluation de l'exposition, priorisation, déploiement, diffusion et suivi."),
 QT("Expliquer comment mettre en place une veille efficace sans saturer l'équipe.",
    "On commence par cadrer le besoin : quelles technologies, quels threats et quelles décisions la veille doit-elle éclairer ? On limite ensuite le nombre de sources à des références fiables (ANSSI, CISA, éditeurs, CVE, MITRE) et on automatise la collecte avec des flux RSS ou des outils de veille. Un filtrage hebdomadaire écarte les informations non pertinentes, et chaque élément retenu est analysé selon son impact local, pas seulement selon son score CVSS. La diffusion se fait sous forme de bulletin court avec trois informations : ce qui change, pourquoi c'est important pour nous, ce qu'on fait. On archive les bulletins pour tracer les décisions et on réévalue périodiquement la pertinence des sources. Enfin, on désigne un responsable par domaine pour éviter que la veille ne repose sur une seule personne.",
    "On préconise cadrage, sources limitées et fiables, automatisation, filtrage, diffusion courte, archivage et responsabilités réparties.")],
C("La veille transforme l'information en décision : sources fiables, filtrage, analyse du contexte local et diffusion courte sont essentiels.",
  "Risque = probabilité × impact · CVSS = gravité technique",
  "ANSSI · CVE · MITRE ATT&CK · registre des risques · veille ciblée",
  "Veille~Collecte et analyse~CVE~Référence des vulnérabilités~CVSS~Score de gravité~MITRE ATT&CK~Tactiques adverses~Registre~Suivi des risques",
  "Cadrer le besoin|Choisir des sources fiables|Collecter et filtrer|Analyser l'impact local|Diffuser et archiver",
  "Suivre trop de sources sans prioriser|Agir sur un score CVSS sans contexte|Ne pas tracer les décisions de veille|Laisser une seule personne porter la veille",
  "Vendredi soir~Publication de faille~200 postes~Périmètre touché~CVE et CVSS~Évaluation initiale~Bulletin court~Diffusion actionnable~Registre~Capitalisation",
  "Score CVSS~Gravité technique~Impact local~Contexte d'exposition",
  "Veille Technologique~Évolutions techniques~CTI~Renseignement sur les menaces"))

# FIN DES LOTS
valider_et_ecrire(F, "btsciel-mat-part-B.json")
