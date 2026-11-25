# -*- coding: utf-8 -*-
"""Generateur stl-mat-part-C.json — lot C : qualite, methode, donnees, langues, EMC.

Qualite et securite (5), Methodologie experimentale (5),
Statistiques et traitement des donnees (4), Anglais technique (3), EMC (3).
Chaque fiche : 12 points, 9 questions (7 QCM + 2 texte), 7 blocs, 3 schemas.
Annees : uniquement 1re et Terminale (filtres de l'application).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _stl_common import FIL, REF, S, R, QC, QT, C, build, valider_et_ecrire

F = []


def add(prefix, titre, mat, ans, points, questions, c):
    F.append(build(prefix, titre, mat, ans, points, questions, c))


# ============================================================ QS1
add("QS1", "Hygiène et sécurité au laboratoire", "Qualité et sécurité au laboratoire", ["1re"],
S("La sécurité au laboratoire repose sur l'anticipation des risques et le respect de règles écrites, rappelées au Code du travail."
  "|Les équipements de protection individuelle, ou EPI, comprennent la blouse, les gants, les lunettes et le masque."
  "|La blouse doit être fermée, entretenue régulièrement et retirée avant de quitter la zone de travail."
  "|Les gants sont choisis en fonction du risque : nitrile pour de nombreux solvants, latex pour des manipulations biologiques."
  "|Les lunettes de protection sont obligatoires dès qu'il existe un risque de projection de liquide ou de fragment."
  "|Les cheveux longs doivent être attachés et les bijoux retirés avant toute manipulation."
  "|Il est interdit de manger, boire, fumer ou utiliser un téléphone au poste de travail."
  "|Les réactifs ne doivent jamais être goûtés et leur odeur ne doit pas être respirée directement."
  "|Toute manipulation dangereuse se réalise sous hotte aspirante, en particulier avec des solvants volatils."
  "|Les produits incompatibles doivent être stockés séparément, notamment acides et bases ou oxydants et réducteurs."
  "|Les issues de secours, les extincteurs et les douches doivent rester accessibles à tout moment."
  "|Une bonne sécurité s'appuie aussi sur le travail en binôme et sur la remontée systématique des incidents et presque-accidents."),
[QC("Que désigne le sigle EPI ?", "Equipement de protection individuelle~Eprouvette de précision~Essai de pureté instrumentale~Etiquette de produit important", 0,
     "Les EPI sont les équipements de protection individuelle : blouse, gants, lunettes."),
 QC("Quel réflexe interdit au laboratoire ?", "Attacher ses cheveux~Goûter un réactif~Porter des gants~Lire une FDS", 1,
     "Il est formellement interdit de goûter ou de sentir directement un réactif."),
 QC("Quand porter des lunettes de protection ?", "Uniquement pour les pesées~Dès qu'il y a risque de projection~Jamais si on porte des gants~Uniquement en microbiologie", 1,
     "Toute manipulation présentant un risque de projection impose le port de lunettes."),
 QC("Pourquoi utiliser une hotte aspirante ?", "Pour refroidir les réactifs~Pour évacuer les vapeurs toxiques~Pour peser plus vite~Pour stériliser", 1,
     "La hotte capte les vapeurs et protège l'opérateur des expositions."),
 QC("Comment stocker acides et bases ?", "Ensemble pour gagner de la place~Séparément pour éviter tout contact~Dans le même récipient~Au réfrigérateur", 1,
     "Les produits incompatibles doivent être stockés séparément."),
 QC("Que faut-il faire en cas de presque-accident ?", "Ne rien signaler~Le signaler et l'analyser~Le cacher au responsable~Changer d'activité", 1,
     "La remontée des presque-accidents permet de prévenir les accidents futurs."),
 QC("Quel comportement est correct au poste ?", "Manger un sandwich~Téléphoner~Travailler en binôme~Laisser la blouse ouverte", 2,
     "Le travail en binôme et la blouse fermée font partie des bonnes pratiques."),
 QT("Expliquer pourquoi la blouse de laboratoire ne doit pas être portée dans les zones de vie (cafétéria, bureau).",
    "La blouse peut avoir été contaminée par des gouttelettes de réactifs, des poussières de poudre, des micro-organismes ou des traces de produits toxiques. La porter dans une zone de vie, c'est transporter ces contaminants hors du laboratoire et exposer d'autres personnes, notamment par contact avec les tables, les poignées ou les aliments. Elle peut aussi être ingérée sous forme de poussière ou entrer en contact avec la peau. La règle est donc de la retirer à la sortie de la zone de travail, de la ranger sur un crochet dédié et de la remplacer régulièrement par une blouse propre. C'est un élément simple de prévention du risque chimique et biologique.",
    "On relie la contamination de la blouse au risque de dissémination hors laboratoire."),
 QT("Décrire les vérifications à effectuer avant de commencer une manipulation chimique.",
    "On lit d'abord l'étiquette du réactif et sa fiche de données de sécurité, en repérant les pictogrammes, les mentions de danger et les conseils de prudence. On vérifie la compatibilité des produits, la quantité nécessaire et la présence d'un poste de travail adapté : hotte, plan de travail propre, extincteur et douche accessibles. On enfile les EPI adaptés : blouse fermée, gants choisis pour le produit, lunettes, cheveux attachés. On s'assure que la verrerie est intacte, que leigestes sont en état et qu'un collègue est présent. On prévoit enfin le devenir des déchets et la conduite à tenir en cas de projection avant de démarrer.",
    "On suit l'ordre : information sur le produit, environnement, EPI, matériel, déchets et urgence.")],
C("La sécurité est une discipline quotidienne : on lit, on s'équipe, on anticipe et on signale.",
  "EPI = blouse + gants + lunettes + protection adaptée au risque",
  "hotte · stockage séparé · interdiction de manger · remontée des incidents",
  "EPI~Protection individuelle~Blouse, gants, lunettes~FDS~Information sur le produit~Pictogrammes~Hotte~Evacuation des vapeurs~Stockage~Separe les incompatibles~Asepsie~Evite la contamination~Binome~Surveillance mutuelle~Presque-accident~Signalé et analysé",
  "Lire l'étiquette et la FDS|Choisir les EPI adaptés|Préparer un poste de travail sûr|Manipuler sans manger ni téléphoner|Signaler tout incident ou presque-accident",
  "Goûter ou sentir un réactif|Porter la blouse en cafétéria|Mélanger acides et bases|Travailler seul sur une manipulation à risque|Ignorer les presque-accidents",
  "Blouse fermée~EPI de base~Gants nitrile~Protection chimique~Hotte~Vapeurs toxiques~Douche~Urgence projection~Binome~Sécurité renforcée",
  "Risque chimique~Brûlure, toxicité~Risque biologique~Contamination",
  "Prévention~Agir avant~Protection~Agir pendant"))

# ============================================================ QS2
add("QS2", "Fiches de données de sécurité et étiquetage", "Qualité et sécurité au laboratoire", ["1re"],
S("La fiche de données de sécurité, ou FDS, accompagne tout produit chimique dangereux et comporte seize rubriques normalisées."
  "|Le règlement CLP (UE n° 1272/2008) harmonise la classification, l'étiquetage et l'emballage des substances et mélanges."
  "|Les pictogrammes de danger sont des losanges rouges à symbole noir, par exemple la flamme, la corrosion ou le crâne."
  "|Les mentions de danger, codées H, décrivent la nature du danger : H226 pour un liquide inflammable."
  "|Les conseils de prudence, codés P, indiquent les mesures à prendre : P280 pour porter des gants et une protection des yeux."
  "|Une substance peut être irritante, corrosive, toxique, cancérogène, mutagène ou reprotoxique."
  "|La fiche précise aussi les propriétés physicochimiques, la stabilité, les incompatibilités et les informations toxicologiques."
  "|Elle indique les mesures de premiers secours et les moyens de lutte contre l'incendie adaptés."
  "|Les conditions de stockage et la durée de conservation figurent dans la rubrique correspondante."
  "|L'étiquette du flacon reprend le nom du produit, les pictogrammes, les mentions H et P et les coordonnées du fournisseur."
  "|Un produit périmé ou dont l'étiquette est illisible doit être éliminé selon la filière déchets, jamais transvasé dans un flacon anonyme."
  "|Consulter la FDS avant toute manipulation est une obligation et un réflexe professionnel attendu en STL."),
[QC("Combien de rubriques comporte une FDS normalisée ?", "8~12~16~20", 2,
     "La fiche de données de sécurité est structurée en seize rubriques.",
     ),
 QC("Quel règlement harmonise l'étiquetage des produits chimiques en Europe ?", "REACH~CLP~RGPD~eIDAS", 1,
     "Le règlement CLP n° 1272/2008 fixe classification, étiquetage et emballage."),
 QC("Que désigne une mention de danger codée H ?", "Un conseil de prudence~Une phrase décrivant le danger~Un pictogramme~Un numéro de lot", 1,
     "Les mentions H décrivent la nature et la gravité du danger."),
 QC("Que signifie le conseil P280 ?", "Garder hors de portée des enfants~Porter des gants et une protection des yeux~Ne pas fumer~Éliminer le contenu", 1,
     "P280 prescrit le port d'un équipement de protection adapté."),
 QC("Quel pictogramme indique un produit corrosif ?", "La flamme~Le crâne~Le tube à essai qui attaque une main~L'exclamation", 2,
     "Le pictogramme corrosion montre une main et une surface attaquées."),
 QC("Quelle information ne figure pas sur une FDS ?", "Les premiers secours~Les incompatibilités~Le prix d'achat~Les conditions de stockage", 2,
     "Le prix n'appartient pas aux informations de sécurité."),
 QC("Que faire d'une étiquette illisible ?", "La recopier à la main~Consulter la FDS et éliminer le produit selon la filière~Sentir le produit~Le transvaser sans étiquette", 1,
     "Il faut s'informer puis éliminer le produit correctement, jamais laisser un flacon anonyme."),
 QT("Expliquer la différence entre une mention H et un conseil P et donner un exemple de chaque pour un solvant inflammable.",
    "Une mention H, ou hazard statement, décrit le danger intrinsèque du produit : par exemple H225 « Liquide et vapeurs très inflammables ». Un conseil P, ou precautionary statement, recommande une action pour maîtriser ce risque : P210 « Tenir à l'écart de la chaleur, des étincelles et des flammes nues » ou P280 « Porter des gants et une protection des yeux ». Les mentions H informent sur ce qui peut arriver, les conseils P sur ce qu'il faut faire. Ensemble, avec les pictogrammes, elles rendent l'étiquette compréhensible même sans lire la FDS complète.",
    "On définit les deux codes et on donne un exemple de mention et de conseil cohérents."),
 QT("Décrire la démarche à suivre pour manipuler pour la première fois un réactif inconnu du laboratoire.",
    "On commence par identifier le flacon et lire son étiquette : nom, numéro CAS si présent, pictogrammes, mentions H et P. On consulte ensuite la FDS, en particulier les rubriques danger, premiers secours, manipulations et stockage, incompatibilités et équipements de protection. On vérifie que le produit est dans sa date de validité et que l'emballage est intact. On détermine les EPI nécessaires, la quantité minimale à utiliser et le besoin éventuel d'une hotte. On s'assure que les déchets générés ont une filière d'élimination identifiée. Enfin, on note la date d'ouverture sur le flacon et on range le produit dans les conditions prescrites après usage.",
    "On suit l'ordre : étiquette, FDS, état du flacon, EPI, quantité, déchets et traçabilité.")],
C("L'étiquette donne l'essentiel, la FDS donne le détail : les consulter avant de manipuler est une obligation.",
  "pictogramme + mention H (danger) + conseil P (action)",
  "CLP · 16 rubriques · incompatibilités · premiers secours · stockage",
  "FDS~Fiche de securite~Seize rubriques~Information complete~CLP~Reglement europeen~Etiquetage harmonise~Pictogramme~Losange rouge~Danger visuel~Mention H~Nature du danger~Conseil P~Action a suivre~Incompatibilite~Produits a ne pas melanger~Stockage~Conditions conservees",
  "Lire l'étiquette du flacon|Repérer pictogrammes et mentions H et P|Consulter la FDS et ses rubriques clés|Choisir EPI et conditions de travail|Éliminer les déchets selon la filière prévue",
  "Se fier à la couleur du flacon|Transvaser dans un récipient sans étiquette|Ignorer la date de péremption|Ne lire que le nom du produit|Oublier de consulter les incompatibilités",
  "16 rubriques~Structure de la FDS~H225~Liquide très inflammable~P210~Tenir loin des flammes~CLP~Règlement 1272/2008~Corrosion~Symbole main attaquée",
  "Mention H~Décrit le danger~Conseil P~Prescrit une action",
  "Étiquette~Aperçu rapide~FDS~Informations détaillées"))

# ============================================================ QS3
add("QS3", "Démarche qualité et traçabilité au laboratoire", "Qualité et sécurité au laboratoire", ["Terminale"],
S("La qualité au laboratoire vise à fournir des résultats fiables, reproductibles et conformes aux attentes du commanditaire."
  "|La norme ISO/CEI 17025 fixe les exigences générales de compétence des laboratoires d'essais et d'étalonnage."
  "|Un système qualité repose sur des procédures écrites, appliquées et régulièrement revues."
  "|La traçabilité permet de relier un résultat à l'échantillon, aux réactifs, à l'appareil, à l'opérateur et à la date."
  "|Chaque échantillon reçoit une identification unique dès sa réception, par un numéro ou un code-barres."
  "|Le cahier de laboratoire est un document original, daté, non effacé, où l'on consigne observations et résultats bruts."
  "|Une erreur dans un cahier se corrige en barrant d'un trait et en écrivant la correction à côté, avec la date et la signature."
  "|Les appareils de mesure doivent être étalonnés et vérifiés à des intervalles définis."
  "|Les réactifs sont suivis par leur numéro de lot et leur date de péremption."
  "|Le contrôle qualité interne utilise des échantillons de contrôle, des blancs et des doublons."
  "|La participation à des essais interlaboratoires permet de comparer ses résultats à ceux d'autres laboratoires."
  "|L'amélioration continue s'appuie sur le cycle planifier, faire, vérifier, agir, appelé cycle PDCA."),
[QC("Quelle norme fixe la compétence des laboratoires d'essais ?", "ISO 9001~ISO/CEI 17025~ISO 14001~ISO 27001", 1,
     "L'ISO/CEI 17025 est la norme de référence des laboratoires d'essais et d'étalonnage."),
 QC("Quel est l'objectif principal de la traçabilité ?", "Réduire le coût des analyses~Relier un résultat à toutes ses conditions de production~Accélérer l'incubation~Remplacer le cahier de laboratoire", 1,
     "La traçabilité reconstitue le chemin complet d'un résultat."),
 QC("Comment corriger une erreur dans un cahier de laboratoire ?", "En effaçant avec du correcteur~En barrant d'un trait et en écrivant la correction à côté~En recopiant la page~En déchirant la page", 1,
     "La correction doit rester lisible et la donnée d'origine reste visible."),
 QC("Que faut-il suivre pour un réactif ?", "Sa couleur~Son numéro de lot et sa date de péremption~Son prix~Son fournisseur uniquement", 1,
     "Le lot et la péremption sont essentiels à la traçabilité."),
 QC("Quel est le rôle d'un échantillon de contrôle ?", "Remplacer l'étalonnage~Vérifier que la méthode donne un résultat connu~Diluer les échantillons~Nettoyer les appareils", 1,
     "Le contrôle Quality interne vérifie la justesse et la stabilité de la méthode."),
 QC("Que permettent les essais interlaboratoires ?", "De se comparer à d'autres laboratoires~De supprimer les contrôles internes~De changer de méthode~De former les clients", 0,
     "Ils évaluent la performance du laboratoire par comparaison entre pairs."),
 QC("Que signifie le A du cycle PDCA ?", "Analyser~Agir~Accumuler~Auditer", 1,
     "PDCA : Planifier, Faire, Vérifier, Agir ; le dernier temps met en oeuvre les améliorations."),
 QT("Expliquer pourquoi la traçabilité est indispensable même lorsqu'un résultat semble correct.",
    "Un résultat correct peut être obtenu par hasard ou grâce à une compensation d'erreurs : sans traçabilité, rien ne permet de le savoir. Si un réactif est périmé, un appareil mal étalonné ou un échantillon mal identifié, le résultat peut être faux sans que le chiffre paraisse suspect. La traçabilité documente l'identité de l'échantillon, le lot de réactif, l'appareil utilisé, l'opérateur et la date, ce qui permet de retrouver et de corriger la cause d'une dérive. Elle est aussi exigée par les normes et nécessaire en cas de réclamation ou d'audit : sans elle, le laboratoire ne peut pas démontrer la validité de ses résultats.",
    "On montre qu'un chiffre correct ne prouve pas une méthode maîtrisée et on cite les éléments suivis."),
 QT("Décrire la tenue correcte d'un cahier de laboratoire au cours d'une série d'analyses.",
    "On utilise un cahier relié, paginé, avec une couverture identifiant le laboratoire et l'année. Pour chaque analyse, on inscrit la date, le nom de l'opérateur, l'identifiant de l'échantillon, l'objectif de la manipulation, le protocole suivi ou sa référence, les réactifs avec leurs lots et les appareils avec leurs numéros. On note les observations brutes au fur et à mesure, sans recopier ni effacer, en conservant les unités et les incertitudes. Les calculs et les résultats exploités sont ajoutés après, clairement séparés des données brutes. Une erreur est barrée d'un trait lisible, corrigée à côté, datée et signée. Le cahier reste dans le laboratoire et est archivé selon la durée prévue par la procédure.",
    "On décrit le support, les informations minimales, la saisie des données brutes et la règle de correction.")],
C("La qualité ne se décrète pas : elle se documente, se vérifie et s'améliore sans cesse.",
  "traçabilité = échantillon + réactif + appareil + opérateur + date",
  "ISO/CEI 17025 · cahier de laboratoire · contrôle interne · PDCA",
  "Qualite~Resultats fiables~Norme 17025~Competence du laboratoire~Tracabilite~Lien avec les conditions~Echantillon~Identifiant unique~Cahier~Document original date~Correction~Barrer puis ecrire~Etalonnage~Verifier l'appareil~Controle interne~Blancs et doublons~PDCA~Amelioration continue",
  "Identifier l'échantillon à la réception|Consigner les données brutes dans le cahier|Vérifier lots et étalonnages|Intégrer blancs et contrôles|Analyser les écarts et améliorer la procédure",
  "Recopier les résultats après coup|Effacer une erreur|Oublier le numéro de lot|Ne jamais vérifier les appareils|Ignorer les écarts de contrôle",
  "ISO 17025~Norme de compétence~PDCA~Planifier Faire Vérifier Agir~Lot de reactif~Tracabilite~Blanc~Controle interne~Essai interlaboratoire~Comparaison entre pairs",
  "Traçabilité~Retrouver l'historique~Contrôle qualité~Vérifier la conformité",
  "Données brutes~Premières valeurs~Résultat exploité~Après calcul"))

# ============================================================ QS4
add("QS4", "Risques biologiques et prévention en laboratoire", "Qualité et sécurité au laboratoire", ["1re"],
S("Le risque biologique provient de l'exposition à des micro-organismes, des cellules, des virus ou des toxines."
  "|Les agents biologiques sont classés en quatre groupes selon leur pouvoir pathogène et leur facilité de propagation."
  "|Le groupe 1 regroupe les agents non pathogènes pour l'homme, comme la plupart des bactéries lactiques."
  "|Les groupes 2 à 4 comportent des agents de plus en plus dangereux, nécessitant des mesures de confinement renforcées."
  "|Les principales voies de contamination sont la voie cutanée, les muqueuses, l'inhalation d'aérosols et l'ingestion accidentelle."
  "|La contamination peut aussi résulter d'une piqûre ou d'une coupure avec du matériel souillé."
  "|Le port des EPI, le lavage des mains et l'absence de bouche-à-oreille sur les pipettes sont des règles essentielles."
  "|La décontamination du plan de travail se fait avant et après chaque manipulation avec un désinfectant adapté."
  "|Le matériel piquant et tranchant est déposé immédiatement dans un conteneur étanche et résistant à la perforation."
  "|Les déchets biologiques sont autoclavés avant élimination, puis traités selon la filière déchets dangereux."
  "|Tout incident d'exposition doit être signalé immédiatement et faire l'objet d'un suivi médical."
  "|La vaccination, l'information et la formation complètent les mesures techniques de prévention."),
[QC("Comment classe-t-on les agents biologiques ?", "Par couleur~En quatre groupes de risque croissant~Par taille~Par date de découverte", 1,
     "Les groupes 1 à 4 classent les agents selon leur dangerosité."),
 QC("Quel est un agent biologique du groupe 1 ?", "Le virus de la grippe~Une bactérie lactique~Le bacille de Koch~Le VIH", 1,
     "Les bactéries lactiques utilisées en agroalimentaire ne sont pas pathogènes."),
 QC("Quelle est une voie de contamination fréquente ?", "La lecture d'une FDS~Une piqûre avec du matériel souillé~Le port de gants~Le lavage des mains", 1,
     "Les accidents avec objets piquants sont une cause majeure d'exposition."),
 QC("Que faut-il faire avec une aiguille usagée ?", "La laisser sur le plan de travail~La replacer dans son capuchon~La jeter dans un conteneur adapté~La laver à l'eau", 2,
     "Les objets piquants vont directement dans un conteneur étanche et perforation-résistant."),
 QC("Quand désinfecter le plan de travail ?", "Une fois par semaine~Avant et après chaque manipulation~Seulement en fin de journée~Jamais si on porte des gants", 1,
     "La décontamination avant et après limite les contaminations croisées."),
 QC("Quel geste est interdit avec une pipette ?", "Utiliser une poire~Aspirer à la bouche~Changer de cône~Lire le volume", 1,
     "L'aspiration à la bouche est strictement interdite pour tout liquide de laboratoire."),
 QC("Que faire après une projection de culture sur une muqueuse ?", "Attendre la fin de la séance~Rincer abondamment et signaler l'incident~Essuyer avec un papier~Prendre un antibiotique seul", 1,
     "Le rinçage immédiat et le signalement sont impératifs."),
 QT("Expliquer pourquoi les aérosols sont particulièrement dangereux en microbiologie.",
    "Les aérosols sont de fines gouttelettes suspendues dans l'air, produites par exemple lors d'une centrifugation, d'un vortexage, d'une pipettage énergique ou d'une projection. Ils peuvent rester en suspension et être inhalés, déposant des micro-organismes profondément dans les voies respiratoires. Ils peuvent aussi se déposer sur le plan de travail, le matériel ou les gants et provoquer des contaminations croisées. Les mesures de prévention consistent à travailler en hotte ou en poste de sécurité microbiologique, à éviter les gestes qui génèrent des aérosols, à laisser reposer les tubes après agitation et à désinfecter régulièrement les surfaces.",
    "On relie la taille des gouttelettes à l'inhalation et aux contaminations croisées, puis on cite les mesures."),
 QT("Décrire la chaîne de traitement des déchets biologiques dans un laboratoire.",
    "Les déchets sont d'abord triés à la source : objets piquants dans un conteneur dédié, milieux et cultures dans des sacs ou récipients étanches, liquides dans des flacons résistants. Les déchets potentiellement contaminants sont ensuite décontaminés, le plus souvent par autoclavage à 121 °C pendant au moins 20 minutes, ou par un désinfectant validé pour les liquides. Après décontamination, ils sont étiquetés et stockés dans une zone réservée avant enlèvement par une filière autorisée. Chaque étape fait l'objet d'une traçabilité : date, type de déchet, traitements appliqués et responsable. En cas de doubt sur l'efficacité du traitement, le déchet est traité à nouveau plutôt que risquer une dissémination.",
    "On décrit tri, décontamination, stockage, enlèvement et traçabilité.")],
C("Face au risque biologique, la barrière la plus efficace est la combinaison des EPI, de l'asepsie et de la décontamination.",
  "voies : peau, muqueuses, inhalation, ingestion, piqûre",
  "groupes 1 à 4 · autoclavage · conteneur piquants · signalement",
  "Risque biologique~Micro-organisme pathogene~Groupes 1 à 4~Dangerosite croissante~Aerosol~Gouttelettes en suspension~Contamination~Peau, muqueuse, inhalation~Piquant~Conteneur etanche~Desinfection~Avant et apres~Autoclave~121 °C~Dechets~Filiere autorisee~Signalement~Suivi medical",
  "Évaluer le groupe de risque de l'agent|Choisir les EPI et le confinement|Travailler sans générer d'aérosols|Désinfecter et trier les déchets|Signaler et suivre tout incident",
  "Aspirer à la bouche|Reboucher une aiguille|Jeter une culture dans la poubelle ordinaire|Travailler avec une plaie non protégée|Ignorer une projection",
  "Groupe 1~Non pathogène~Groupe 4~Très dangereux~121 °C~Autoclave~20 min~Durée de décontamination~Aérosol~Inhalation~Conseils~Vaccination et formation",
  "Décontamination~Détruire les germes~Asepsie~Éviter l'apport de germes",
  "Piquant~Conteneur rigide~Autre déchet~Sac étanche"))

# ============================================================ QS5
add("QS5", "Conduite à tenir en cas d'accident au laboratoire", "Qualité et sécurité au laboratoire", ["Terminale"],
S("Une situation d'urgence au laboratoire exige d'abord de protéger les personnes, puis de prévenir et d'alerter."
  "|La priorité est d'éliminer la cause du danger sans mettre en péril sa propre sécurité."
  "|En cas de début d'incendie, on déclenche l'alarme, on coupe si possible l'alimentation et on utilise le moyen d'extinction adapté."
  "|Un extincteur à poudre convient aux feux de solides et de liquides, tandis que le CO₂ est adapté aux feux d'équipements électriques."
  "|Ne jamais utiliser d'eau sur un feu de liquide inflammable ou d'appareil sous tension."
  "|En cas de projection de produit chimique sur la peau ou dans les yeux, le rinçage à l'eau doit durer au moins quinze minutes."
  "|La douche de sécurité et le lave-oeil doivent être accessibles en moins de dix secondes."
  "|Les vêtements contaminés sont retirés sans frotter la peau."
  "|En cas d'inhalation de vapeurs, la personne est amenée à l'air libre, sans que le secouriste entre dans la zone polluée."
  "|En cas de coupure ou de piqûre, on laisse saigner légèrement, on nettoie à l'eau et au savon puis on désinfecte."
  "|Le signalement immédiat au responsable et l'appel des secours internes ou externes sont indispensables."
  "|Après l'urgence, un compte rendu daté et une analyse des causes permettent d'éviter la répétition de l'incident."),
[QC("Quelle est la première priorité en situation d'urgence ?", "Sauver le matériel~Protéger les personnes~Répondre au téléphone~Nettoyer la paillasse", 1,
     "La protection des personnes prime sur celle des biens."),
 QC("Quel extincteur utiliser sur un feu d'origine électrique ?", "L'eau~La poudre~Le CO₂~Le sable uniquement", 2,
     "Le CO₂ ne conduit pas le courant et ne laisse pas de résidu sur les appareils."),
 QC("Combien de temps rincer un oeil contaminé ?", "Une minute~Cinq minutes~Au moins quinze minutes~Une heure", 2,
     "Un rinçage prolongé d'au moins quinze minutes est requis."),
 QC("Que faire en cas d'inhalation de vapeurs toxiques ?", "Entrer dans la zone pour aider~Amener la personne à l'air libre~Donner à boire~La faire asseoir sur place", 1,
     "Il faut d'abord soustraire la victime à l'atmosphère polluée, sans s'exposer."),
 QC("Que faut-il éviter sur un feu de liquide inflammable ?", "La poudre~Le CO₂~L'eau~Le sable", 2,
     "L'eau étale le liquide en flamme et aggrave le feu."),
 QC("Comment traiter une petite plaie par piqûre ?", "La fermer avec du ruban~La laisser saigner un peu, nettoyer puis désinfecter~La brûler~La recouvrir sans nettoyer", 1,
     "Le nettoyage et la désinfection après un léger saignement limitent le risque infectieux."),
 QC("Quelle suite donner à un incident une fois la situation maîtrisée ?", "Oublier l'incident~Rédiger un compte rendu et analyser les causes~Changer de laboratoire~Réduire les formation", 1,
     "Le retour d'expérience est indispensable à la prévention."),
 QT("Décrire l'enchaînement des gestes face à une projection d'acide sur la main et l'avant-bras.",
    "On éloigne immédiatement la personne de la source, on enlève gants et manches ou bijoux contaminés sans frotter, puis on place la zone sous la douche de sécurité ou sous un robinet d'eau tempérée. Le rinçage doit être abondant et durer au moins quinze minutes, en écartant les doigts pour atteindre les plis. On alerte le responsable de sécurité dès le début du rinçage, puis on appelle le SAMU ou le centre antipoison selon la gravité et la nature du produit. On ne frotte pas avec un chiffon, on n'applique ni pommade ni neutralisant. Après rinçage, on couvre la zone avec un pansement stérile et on consigne l'incident avec le nom du produit et l'heure.",
    "On insiste sur le retrait des vêtements, la durée du rinçage, l'alerte et l'absence de neutralisation."),
 QT("Expliquer pourquoi les exercices d'évacuation et la connaissance des extincteurs sont nécessaires en plus des affichages.",
    "Un affichage ne garantit pas qu'une personne stressée saura réagir : en situation d'urgence, le temps de réaction est court et les gestes doivent être automatiques. Les exercices d'évacuation permettent de mémoriser le chemin le plus court, le point de rassemblement et le rôle de chacun, y compris lorsque la fumée ou l'obscurité gênent la lecture des panneaux. La manipulation réelle d'un extincteur, même sur un simulateur, apprend à vérifier la pression, à retirer la goupille et à diriger le jet à la base des flammes. Ces entraînements révèlent aussi les points faibles : issue encombrée, extincteur périmé, matériel inaccessible. Ils transforment une consigne écrite en réflexe professionnel et réduisent le temps perdu au moment critique.",
    "On oppose la théorie affichée au geste automatisé et on cite les bénéfices concrets des exercices.")],
C("En urgence, on protège, on alerte, on secourt et on rapporte : les gestes doivent être connus avant d'en avoir besoin.",
  "protéger → alerter → secourir → signaler",
  "extincteur adapté · rinçage 15 min · air libre · compte rendu",
  "Urgence~Situation dangereuse~Proteger~Securite des personnes~Alerter~Prevenir les secours~Extincteur~Moyen adapte au feu~Rincage~Eau abondante 15 minutes~Douche~Equipement de secours~Air libre~Inhalation~Compte rendu~Analyse des causes~Retour d'experience",
  "Évaluer la situation sans s'exposer|Supprimer la cause si possible|Protéger et alerter|Appliquer le geste de secours adapté|Rapporter et analyser l'incident",
  "Utiliser de l'eau sur un feu électrique|Entrer dans une zone de vapeurs|Ne pas rincer assez longtemps|Ne pas signaler un incident|Courir sans réfléchir",
  "15 minutes~Rinçage minimum~10 secondes~Accès à la douche~CO₂~Feu électrique~Poudre~Feu de liquide~SAMU~Secours externe~Compte rendu~Traçabilité",
  "Incendie~Feu et fumée~Projection~Contact chimique",
  "Prévention~Avant l'incident~Intervention~Pendant~Retour d'expérience~Après"))

# ============================================================ ME1
add("ME1", "Démarche expérimentale et formulation d'hypothèses", "Méthodologie expérimentale", ["1re"],
S("La démarche expérimentale part d'une question scientifique précise issue d'une observation ou d'un problème concret."
  "|Une hypothèse est une proposition explicative temporaire qui doit pouvoir être réfutée par l'expérience."
  "|Une bonne hypothèse est claire, testable et formulée en termes de relations entre variables."
  "|On déduit de l'hypothèse une prédiction : si l'hypothèse est vraie, alors tel résultat doit être observé."
  "|L'expérience est conçue pour tester cette prédiction, avec un protocole et des conditions contrôlées."
  "|Un témoin ou une condition témoin sert de référence pour comparer l'effet étudié."
  "|Les résultats sont comparés à la prédiction : ils peuvent confirmer l'hypothèse sans la prouver définitivement."
  "|Une hypothèse réfutée est abandonnée ou reformulée, ce qui fait progresser la connaissance."
  "|La démarche est itérative : une expérience en appelle souvent une autre plus précise."
  "|La démarche hypothético-déductive alterne ainsi hypothèses, déductions et tests expérimentaux."
  "|Un biais de confirmation consiste à ne retenir que les observations qui arrangent l'hypothèse."
  "|En STL, cette démarche structure les travaux pratiques de chimie, de biologie et de physique."),
[QC("Qu'est-ce qu'une hypothèse scientifique ?", "Une certitude démontrée~Une proposition temporaire testable~Une opinion personnelle~Une conclusion définitive", 1,
     "Une hypothèse est une explication provisoire qui peut être réfutée."),
 QC("Que signifie une hypothèse réfutable ?", "Qu'elle peut être contredite par une expérience~Qu'elle est toujours vraie~Qu'elle ne peut pas être testée~Qu'elle est complexe", 0,
     "La réfutabilité est le critère central d'une hypothèse scientifique."),
 QC("Quel rôle joue le témoin dans une expérience ?", "Il augmente la température~Il sert de référence de comparaison~Il remplace les mesures~Il accélère la réaction", 1,
     "Le témoin permet d'attribuer la différence observée au facteur étudié."),
 QC("Une expérience peut-elle prouver définitivement une hypothèse ?", "Oui, toujours~Non, elle peut seulement la confirmer temporairement~Oui, si elle est répétée~Seulement en biologie", 1,
     "Les résultats confirment ou infirment ; ils ne démontrent pas de façon définitive."),
 QC("Que faire si les résultats contredisent l'hypothèse ?", "Les cacher~Reformuler ou abandonner l'hypothèse~Changer les mesures~Ajouter un biais", 1,
     "La réfutation fait partie du processus scientifique."),
 QC("Comment appelle-t-on le raisonnement hypothèse-prédiction-test ?", "Déductif~Hypothético-déductif~Inductif simple~Analytique", 1,
     "C'est la démarche hypothético-déductive."),
 QC("Quel est un biais de confirmation ?", "Répéter les mesures~Ne retenir que les données favorables à l'hypothèse~Utiliser un témoin~Noter les incertitudes", 1,
     "Ce biais conduit à ignorer les résultats contraires."),
 QT("Formuler une hypothèse testable et sa prédiction pour expliquer qu'une solution d'enzyme perd de l'activité après chauffage.",
    "Hypothèse : l'activité de l'enzyme diminue après chauffage parce que la chaleur dénature sa structure tridimensionnelle, en particulier son site actif. Prédiction : si l'hypothèse est correcte, une solution d'enzyme chauffée dix minutes à 80 °C, puis refroidie, présentera une vitesse de réaction nettement inférieure à celle d'une solution non chauffée maintenue dans les mêmes conditions, et ce de façon irréversible. On testera cette prédiction en mesurant la quantité de produit formé par unité de temps pour les deux solutions, avec un témoin identique non chauffé.",
    "On formule une relation de cause à effet, puis une prédiction mesurable avec un témoin."),
 QT("Expliquer pourquoi une hypothèse confirmée par une seule expérience reste provisoire.",
    "Une seule expérience ne peut pas exclure toutes les causes alternatives : une variable non contrôlée, un défaut de mesure ou une coïncidence peuvent produire le même résultat. La confirmation repose donc sur la répétabilité des essais, sur la variété des conditions testées et sur la confrontation avec d'autres hypothèses. De plus, dans le raisonnement hypothético-déductif, observer la conséquence prédite ne prouve pas logiquement l'hypothèse : d'autres explications peuvent prédire la même conséquence. Une hypothèse gagne en crédibilité lorsqu'elle résiste à de nombreux tests indépendants, mais elle reste révisable si une nouvelle expérience la contredit.",
    "On invoque les causes alternatives, la répétabilité et la distinction entre confirmation et démonstration.")],
C("La démarche expérimentale teste des hypothèses réfutables à l'aide de prédictions, de témoins et de mesures comparables.",
  "si hypothèse vraie, alors prédiction observée",
  "observation · hypothèse · prédiction · expérience · conclusion provisoire",
  "Question~Probleme scientifique~Observation~Point de depart~Hypothese~Explication provisoire~Refutable~Testable par experience~Prediction~Resultat attendu~Temoins~Condition de reference~Test~Mise a l'epreuve~Confirmation~Resultat compatible~Refutation~Hypothese abandonnee~Biais de confirmation~Donnees favorables seulement",
  "Partir d'une question précise|Formuler une hypothèse réfutable|En déduire une prédiction mesurable|Concevoir l'expérience avec un témoin|Comparer résultats et prédiction",
  "Formuler une hypothèse non testable|Oublier le témoin|Chercher seulement des résultats favorables|Confondre confirmation et preuve|Modifier le protocole après coup",
  "Chaleur~Denaturation de l'enzyme~Prediction~Vitesse plus faible~Temoins~Solution non chauffee~Refutation~Reformuler l'hypothese~Biais~Selection des donnees",
  "Hypothèse~À tester~Théorie~Jeu d'hypothèses validées",
  "Confirmation~Compatible~Preuve~Démonstration définitive"))

# ============================================================ ME2
add("ME2", "Concevoir un protocole et identifier les variables", "Méthodologie expérimentale", ["1re"],
S("Un protocole expérimental décrit de façon précise et reproductible les étapes d'une manipulation."
  "|Il indique le matériel, les réactifs, les quantités, les concentrations, les durées et les températures."
  "|La qualité d'un protocole se juge à sa reproductibilité : une autre personne doit obtenir les mêmes résultats."
  "|La variable à tester, ou variable indépendante, est le facteur que l'on fait varier volontairement."
  "|La variable mesurée, ou variable dépendante, est la grandeur que l'on relève pour observer un effet."
  "|Les variables contrôlées sont maintenues constantes pour éviter qu'elles n'influencent le résultat."
  "|Un protocole comporte généralement plusieurs modalités de la variable à tester, dont une condition témoin."
  "|La répétition des essais, appelée réplicats, permet d'estimer la variabilité et de détecter les valeurs aberrantes."
  "|L'ordre des manipulations doit être choisi pour limiter les contaminations et les dérives dans le temps."
  "|Le protocole précise les critères d'arrêt et les mesures de sécurité associées à chaque étape."
  "|Un bon protocole est écrit avant de commencer, puis éventuellement ajusté avec mention de la modification."
  "|Il constitue un document de référence pour le compte rendu et pour la traçabilité des résultats."),
[QC("Qu'est-ce qu'une variable indépendante ?", "La grandeur mesurée~Le facteur que l'on fait varier volontairement~Une constante~Un résultat", 1,
     "C'est le facteur testé, choisi par l'expérimentateur."),
 QC("Quelle variable correspond au résultat relevé ?", "Indépendante~Dépendante~Contrôlée~Constante", 1,
     "La variable dépendante est celle que l'on mesure en fonction du facteur testé."),
 QC("À quoi servent les variables contrôlées ?", "À être modifiées~À rester constantes pour isoler l'effet~À remplacer les témoins~À augmenter le nombre de mesures", 1,
     "Les garder constantes évite les effets de confusion."),
 QC("Comment juge-t-on la qualité d'un protocole ?", "À sa longueur~À sa reproductibilité~Au nombre de schémas~À son prix", 1,
     "Un protocole doit pouvoir être repris tel quel par une autre personne."),
 QC("Que sont des réplicats ?", "Des témoins uniques~Des répétitions de la même condition~Des variables modifiées~Des erreurs de mesure", 1,
     "Les répétitions permettent d'estimer la dispersion des résultats."),
 QC("Quand faut-il écrire le protocole ?", "Après l'expérience~Avant de commencer les manipulations~Pendant le nettoyage~Jamais", 1,
     "Il est écrit avant, puis amendé si besoin en mentionnant les changements."),
 QC("Que doit préciser un protocole en plus des étapes ?", "La couleur des flacons~Les quantités, durées, températures et consignes de sécurité~Le nom du fournisseur~L'heure de repas", 1,
     "Ces détails conditionnent la reproductibilité et la sécurité."),
 QT("Une étude porte sur l'effet de la température sur la vitesse d'une réaction enzyme-substrat. Identifier les variables et décrire le protocole.",
    "La variable indépendante est la température, choisie par exemple à 20, 30, 40, 50 et 60 °C. La variable dépendante est la vitesse de réaction, mesurée par la quantité de produit formé par minute. Les variables contrôlées sont la concentration d'enzyme, la concentration de substrat, le volume total, le pH, la durée d'incubation et la cuve utilisée. Le protocole : préparer des tubes identiques, les placer aux températures choisies, ajouter l'enzyme en dernier pour démarrer la réaction, incuber cinq minutes, doser le produit, répéter trois fois chaque température et inclure un tube témoin sans enzyme. On trace ensuite la vitesse moyenne en fonction de la température.",
    "On identifie les trois types de variables et on décrit un protocole reproductible avec réplicats et témoin."),
 QT("Expliquer pourquoi modifier un protocole en cours d'expérience est problématique et comment le documenter.",
    "Modifier un protocole en cours de série change les conditions entre les premiers et les derniers essais : les résultats ne sont plus comparables et la variable testée n'est plus la seule à avoir varié. Cela introduit un biais qui peut conduire à une fausse conclusion. Si une modification est nécessaire, par exemple une panne de matériel ou une erreur de préparation, il faut l'interrompre, noter précisément la date, la nature du changement et sa raison dans le cahier de laboratoire, puis reprendre l'ensemble des essais avec le protocole corrigé plutôt que de conserver des résultats hétérogènes. Si la reprise est impossible, les résultats obtenus avant et après modification doivent être présentés séparément.",
    "On explique le biais de comparabilité et la nécessité de documenter puis de reprendre les essais.")],
C("Un protocole est la recette reproductible de l'expérience : il distingue ce que l'on change, ce que l'on mesure et ce que l'on garde constant.",
  "variable indépendante → variable dépendante, à autres variables constantes",
  "témoin · modalités · réplicats · critères d'arrêt · sécurité",
  "Protocole~Description reproductible~Variable independante~Facteur teste~Variable dependante~Grandeur mesuree~Variables controlees~Gardees constantes~Modalites~Valeurs du facteur~Temoins~Reference~Replicats~Repetitions~Reproductibilite~Autre personne~Criteres d'arret~Fin de manipulation",
  "Formuler la question et l'hypothèse|Choisir les variables et leurs modalités|Écrire les étapes avec quantités et durées|Prévoir témoins et réplicats|Vérifier la sécurité et les critères d'arrêt",
  "Faire varier plusieurs facteurs à la fois|Oublier le témoin|Ne pas noter les concentrations|Modifier le protocole sans le signaler|Négliger les réplicats",
  "Température~Variable indépendante~Vitesse~Variable dépendante~pH et concentrations~Variables contrôlées~20 à 60 °C~Cinq modalités~Trois répétitions~Réplicats",
  "Variable indépendante~Ce que l'on change~Variable dépendante~Ce que l'on mesure",
  "Protocole~Écrit avant~Compte rendu~Écrit après"))

# ============================================================ ME3
add("ME3", "Échantillonnage et prélèvements", "Méthodologie expérimentale", ["Terminale"],
S("Un échantillonnage consiste à prélever une partie d'une population ou d'un milieu pour l'analyser."
  "|La population cible est l'ensemble sur lequel on souhaite conclure ; l'échantillon en est une fraction."
  "|Un prélèvement est représentatif lorsqu'il reflète la composition et la variabilité de la population cible."
  "|Le tirage aléatoire donne à chaque individu la même probabilité d'être sélectionné et limite le biais de choix."
  "|La stratification découpe la population en sous-groupes homogènes puis prélève proportionnellement dans chacun."
  "|La taille de l'échantillon conditionne la précision : plus elle est grande, plus l'incertitude diminue."
  "|Un prélèvement biaisé invalide les conclusions même si l'analyse en laboratoire est parfaite."
  "|Les conditions de prélèvement, le lieu, la date, l'heure et le nom du préleveur doivent être consignés."
  "|Le contenant doit être propre, adapté à l'analyse et correctement étiqueté avant le remplissage."
  "|La chaîne du froid, l'obscurité ou un fixateur peuvent être nécessaires pour préserver l'échantillon."
  "|Les échantillons doivent être homogénéisés avant de prélever une sous-partie pour l'analyse."
  "|Un échantillon témoin ou un blanc de prélèvement permet de détecter une contamination lors de la manipulation."),
[QC("Qu'est-ce qu'un échantillon représentatif ?", "Un prélèvement pris au hasard près de la porte~Un prélèvement reflétant la population cible~Le plus gros prélèvement possible~Le dernier prélèvement de la journée", 1,
     "La représentativité suppose que les caractéristiques de la population soient retrouvées dans l'échantillon."),
 QC("Que garantit un tirage aléatoire ?", "Une analyse plus rapide~Une probabilité égale pour chaque individu~Un résultat exact~Une taille plus petite", 1,
     "L'aléatoire réduit le biais de sélection, sans garantir à lui seul l'exactitude."),
 QC("En quoi consiste la stratification ?", "À prélever seulement le premier venu~À découper en sous-groupes puis à prélever dans chacun~À mélanger tous les échantillons~À refaire trois fois le même prélèvement", 1,
     "La stratification améliore la représentativité lorsque la population est hétérogène."),
 QC("Quel effet a une augmentation de la taille de l'échantillon ?", "Elle augmente l'incertitude~Elle diminue l'incertitude~Elle n'a aucun effet~Elle supprime les biais", 1,
     "La précision statistique s'améliore avec le nombre d'observations, mais pas l'absence de biais."),
 QC("Pourquoi consigner la date et l'heure du prélèvement ?", "Pour remplir le cahier~Pour assurer la traçabilité et interpréter les variations temporelles~Pour calculer le prix~Pour choisir le contenant", 1,
     "Ces informations font partie de la traçabilité et peuvent expliquer un résultat."),
 QC("À quoi sert un blanc de prélèvement ?", "À remplacer l'échantillon~À détecter une contamination pendant la manipulation~À augmenter la concentration~À réduire le volume", 1,
     "Il subit toutes les étapes sauf le prélèvement réel et révèle les contaminations accidentelles."),
 QC("Pourquoi homogénéiser un échantillon avant analyse ?", "Pour le rendre plus lourd~Pour que la sous-partie analysée représente le tout~Pour le colorer~Pour le stériliser", 1,
     "Sans homogénéisation, la fraction analysée peut ne pas être représentative."),
 QT("Expliquer pourquoi un échantillon biaisé ne peut pas être rattrapé par une analyse très précise au laboratoire.",
    "La précision de l'analyse ne porte que sur la fraction effectivement reçue au laboratoire. Si cette fraction n'est pas représentative, par exemple parce qu'elle provient uniquement de la surface d'un liquide non homogénéisé ou d'un seul point d'un lot, le résultat sera exact pour cette fraction mais faux pour la population cible. Aucune répétition de la mesure, aucun appareil plus précis ne corrige ce défaut : l'erreur est en amont, au moment du prélèvement. C'est pourquoi la stratégie d'échantillonnage, l'homogénéisation et la traçabilité des conditions de prélèvement sont aussi importantes que la qualité de la mesure elle-même.",
    "On sépare l'erreur de prélèvement de l'erreur de mesure et on montre qu'elle est irrécupérable."),
 QT("Décrire la démarche d'échantillonnage d'un lot de matière première pour un contrôle qualité.",
    "On définit d'abord la population cible et la question : lot de 500 flacons, conformité d'un paramètre. On choisit un plan d'échantillonnage : tirage aléatoire simple ou stratification par fournisseur ou par date de production, avec une taille d'échantillon tenant compte de la variabilité et du risque accepté. On prélève ensuite les unités désignées, de façon aléatoire et sans choisir les plus faciles d'accès, en notant lieu, date, heure et identifiant du lot. On étiquette chaque contenant, on respecte les conditions de conservation, puis on homogénéise et on prélève une portion pour l'analyse. On joint un blanc de prélèvement et on consigne toutes les étapes dans le cahier de laboratoire.",
    "On décrit la définition de la population, le plan, la taille, la saisie, l'étiquetage et la traçabilité.")],
C("Un résultat ne vaut que si l'échantillon dont il provient est représentatif et tracé.",
  "échantillon représentatif = tirage aléatoire ou stratifié + taille adaptée",
  "population cible · biais · homogeneous · chaîne du froid · blanc de prélèvement",
  "Population cible~Ensemble etudie~Echantillon~Partie prelevee~Representativite~Reflete la population~Tirage aleatoire~Probabilite egale~Stratification~Sous-groupes~Taille~Precision~Biais~Selection biaisee~Tracabilite~Date, lieu, preleveur~Homogeneisation~Melange avant analyse~Blanc de prelevement~Detection contamination",
  "Définir la population cible et la question|Choisir un plan aléatoire ou stratifié|Déterminer la taille nécessaire|Prélever, étiqueter et conserver|Homogénéiser et joindre un blanc",
  "Choisir les unités les plus accessibles|Négliger l'homogénéisation|Oublier d'étiqueter|Ignorer les conditions de conservation|Croire qu'une analyse précise corrige un biais",
  "Lot de 500~Population cible~Tirage aleatoire~Chaque unité a une chance égale~Strates~Par fournisseur~Blanc~Contamination detectée~Date et heure~Tracabilité",
  "Échantillon~Partie de la population~Population~Ensemble complet",
  "Aléatoire~Limite le biais~Biais~Erreur systématique"))

# ============================================================ ME4
add("ME4", "Observer, mesurer et relever des résultats", "Méthodologie expérimentale", ["1re"],
S("L'observation expérimentale est une description objective et précise de ce qui est vu, entendu ou mesuré."
  "|On distingue l'observation de l'interprétation : la première rapporte un fait, la seconde lui donne un sens."
  "|Une observation fiable est datée, datée du protocole utilisé et exprimée avec des unités."
  "|Les mesures doivent être relevées directement dans le cahier de laboratoire, sans passer par un brouillon volant."
  "|Chaque résultat brut est conservé, même s'il semble aberrant : c'est l'analyse qui décide ensuite de son sort."
  "|Les unités, la résolution de l'appareil et l'incertitude accompagnent systématiquement la valeur."
  "|Un tableau de résultats bien construit porte un titre, les grandeurs avec leurs unités et les conditions de mesure."
  "|Les répétitions sont reportées dans des colonnes distinctes, avec la moyenne et l'écart-type si nécessaire."
  "|Les phénomènes qualitatifs, comme une couleur ou une odeur, sont décrits avec un vocabulaire précis et prudent."
  "|L'odeur ne doit jamais être respirée directement : on utilise la technique du léger éventail, si le protocole l'autorise."
  "|Un schéma légendé complète utilement le texte pour décrire un montage ou une observation microscopique."
  "|La qualité du relevé conditionne toute l'exploitation ultérieure des résultats."),
[QC("Quelle est une observation objective ?", "« La réaction est réussie »~« La solution est devenue bleue en 30 s »~« L'expérience est intéressante »~« Le produit est beau »", 1,
     "Une observation rapporte un fait mesurable ou visible, sans jugement."),
 QC("Que faut-il faire d'une valeur qui semble aberrante ?", "La supprimerimmédiatement~La consigner puis l'analyser~La remplacer par la moyenne~La cacher", 1,
     "On garde la donnée brute et on justifie ensuite son éventuel rejet."),
 QC("Quelles informations accompagnent une mesure ?", "L'heure et la couleur~L'unité et l'incertitude~Le nom de l'élève~La marque de l'appareil", 1,
     "Une mesure sans unité ni incertitude est difficilement exploitable."),
 QC("Où noter les résultats bruts ?", "Sur un post-it~Directement dans le cahier de laboratoire~Sur la paillasse~De mémoire", 1,
     "La saisie directe garantit l'intégrité et la traçabilité des données."),
 QC("Que doit contenir un tableau de résultats ?", "Seulement les nombres~Un titre, les grandeurs, les unités et les conditions~Seulement la moyenne~Les conclusions", 1,
     "Ces éléments rendent le tableau lisible et réutilisable."),
 QC("Comment décrire prudemment une observation qualitative ?", "En utilisant des mots imagés~En décrivant la couleur, l'aspect et l'état avec précision~En donnant une opinion~En devinant la cause", 1,
     "Le vocabulaire doit être factuel et non interprétatif."),
 QC("À quoi sert un schéma légendé ?", "À remplacer les mesures~À décrire un montage ou une observation visuelle~À masquer les erreurs~À accélérer le calcul", 1,
     "Le schéma complète utilement le relevé écrit."),
 QT("Transformer une observation interprétative en observations objectives : « La réaction a bien marché, le précipité est magnifique et le produit est pur. »",
    "On peut écrire : « Après ajout de 2 mL de solution de nitrate de baryum, un solide blanc est apparu en moins de 10 secondes. Le mélange a été filtré ; le résidu recueilli est une poudre blanche. La masse du résidu après séchage est de 0,233 g. » Ces phrases rapportent des faits observables et mesurables : couleur, aspect, délai, masse. Les mots « bien marché », « magnifique » et « pur » sont des jugements ou des conclusions : la pureté devra être démontrée par une mesure, par exemple un point de fusion ou une analyse.",
    "On remplace les jugements par des faits datés, mesurés et décrits avec précision."),
 QT("Décrire la structure d'un tableau de résultats pour une série de titrages répétés trois fois.",
    "Le tableau porte un titre indiquant l'essai réalisé, par exemple « Titrage d'un acide inconnu par la soude 0,100 mol/L ». La première colonne donne l'identifiant de l'essai (1, 2, 3), la deuxième le volume à l'équivalence en mL, la troisième la concentration calculée en mol/L. Une ligne « moyenne » et une ligne « écart-type » ou « écart maximal » complètent le tableau. On fait figurer en légende la date, la température, le nom de l'opérateur et l'indicateur utilisé. Les valeurs sont écrites avec le même nombre de décimales, cohérent avec la résolution de la burette, et les unités figurent dans les en-têtes plutôt que répétées dans chaque cellule.",
    "On décrit les colonnes, les statistiques récapitulatives, la légende et la cohérence des chiffres.")],
C("Observer, c'est décrire des faits ; mesurer, c'est leur associer un nombre, une unité et une incertitude.",
  "observation objective ≠ interprétation",
  "cahier de laboratoire · données brutes · tableau légendé · répétitions · schéma",
  "Observation~Fait constate~Interpretation~Sens donne au fait~Donnee brute~Valeur non traitee~Cahier~Saisie directe~Unite~Indispensable~Incertitude~Precision de la mesure~Tableau~Titre et unites~Repetitions~Essais distincts~Schema~Descriptif et legende",
  "Observer sans juger|Tout noter directement dans le cahier|Indiquer unités et incertitudes|Construire un tableau légendé|Conserver les valeurs brutes avant calcul",
  "Confondre observation et conclusion|Effacer une valeur gênante|Oublier les unités|Recopier les résultats de mémoire|Utiliser des mots subjectifs",
  "Solution bleue~Observation objective~Réaction réussie~Interprétation~0,233 g~Mesure avec unité~3 essais~Répétitions~Titrage~Titre du tableau~Schéma~Montage légendé",
  "Observation~Ce qui est vu~Interprétation~Ce que cela signifie",
  "Donnée brute~Avant traitement~Résultat exploité~Après calcul"))

# ============================================================ ME5
add("ME5", "Compte rendu d'expérience et exploitation des résultats", "Méthodologie expérimentale", ["Terminale"],
S("Le compte rendu d'expérience restitue de structuré la démarche, les résultats et la conclusion d'un travail de laboratoire."
  "|Sa structure classique comprend un titre, une introduction, le protocole, les résultats, une discussion et une conclusion."
  "|L'introduction rappelle le contexte, la question posée et l'hypothèse testée."
  "|Le protocole est décrit de manière suffisamment précise pour être reprise, avec un schéma du montage."
  "|Les résultats sont présentés sous forme de tableaux, de graphiques ou de photographies légendées."
  "|Les données brutes restent disponibles en annexe ou dans le cahier de laboratoire."
  "|La discussion compare les résultats à la prédiction et aux valeurs de référence."
  "|Elle analyse les écarts en distinguant les erreurs aléatoires, systématiques et les limites de la méthode."
  "|La conclusion répond à la question initiale et indique si l'hypothèse est confirmée, infirmée ou à préciser."
  "|Une ouverture propose une amélioration du protocole ou une expérience complémentaire."
  "|Le style est impersonnel, clair et précis : on évite le « je » et les jugements de valeur."
  "|Les références utilisées, normes ou FDS, sont citées en fin de document pour assurer la traçabilité."),
[QC("Quelle est une structure correcte de compte rendu ?", "Conclusion, résultats, protocole~Introduction, protocole, résultats, discussion, conclusion~Résultats seulement~Hypothèse et conclusion uniquement", 1,
     "On suit l'ordre logique de la démarche scientifique."),
 QC("Que contient l'introduction ?", "Le détail des mesures~Le contexte, la question et l'hypothèse~La conclusion~Les références", 1,
     "Elle cadre le travail et annonce l'objectif."),
 QC("Où présente-t-on les données brutes ?", "Uniquement dans la discussion~Dans un tableau ou en annexe~Dans l'introduction~Dans le titre", 1,
     "Les données brutes doivent rester consultables, souvent en annexe."),
 QC("Quel est le rôle de la discussion ?", "Répéter les résultats~Comparer, expliquer les écarts et discuter les limites~Rédiger le protocole~Citer la FDS", 1,
     "La discussion interprète les résultats et analyse les incertitudes."),
 QC("Que doit faire la conclusion ?", "Répondre à la question initiale~Présenter le matériel~Donner toutes les mesures~Remplacer l'introduction", 0,
     "Elle apporte une réponse argumentée et nuancée à la question posée."),
 QC("Quel registre privilégier ?", "Familier~Impersonnel et précis~Ironique~Poétique", 1,
     "Le compte rendu scientifique évite le « je » et les jugements de valeur."),
 QC("Pourquoi citer les références en fin de document ?", "Pour allonger le texte~Pour assurer la traçabilité des méthodes et normes~Pour cacher les erreurs~Pour remplacer les résultats", 1,
     "Les références permettent de vérifier et de reprendre le travail."),
 QT("Rédiger une conclusion de compte rendu pour une expérience où l'hypothèse sur l'effet de la température est confirmée, mais avec une forte dispersion à 60 °C.",
    "Les résultats montrent que la vitesse de réaction augmente entre 20 et 50 °C, puis se stabilise, ce qui confirme l'hypothèse d'une activation thermique de la réaction dans cette gamme. À 60 °C, la dispersion des trois essais est nettement plus grande que dans les autres conditions : l'écart-type atteint 15 % de la moyenne. Cette variabilité peut traduire une dégradation partielle de l'enzyme ou un contrôle thermique insuffisant du bain. L'hypothèse est donc confirmée pour la tendance générale, mais le résultat à 60 °C doit être considéré avec prudence. Une expérience complémentaire avec un bain thermostaté et un temps d'incubation réduit permettrait de préciser la température optimale.",
    "On répond à la question, on nuance selon les données et on propose une ouverture."),
 QT("Expliquer pourquoi les données brutes doivent rester accessibles même après la rédaction du compte rendu.",
    "Le compte rendu présente des résultats traités : moyennes, arrondis, graphiques. Ces traitements reposent sur des choix, par exemple l'exclusion d'une valeur jugée aberrante ou le choix d'une gamme de calibration. Sans les données brutes, un lecteur ne peut pas vérifier ces choix, recalculer un résultat avec une autre méthode statistique ou détecter une erreur de saisie. Les données brutes sont aussi nécessaires en cas de réclamation, d'audit ou de reprise de l'expérience par une autre personne. Elles constituent la mémoire scientifique du travail et doivent être conservées dans le cahier de laboratoire ou dans un fichier non modifiable, avec la date et le nom de l'opérateur.",
    "On relie la disponibilité des données brutes à la vérifiabilité, à la traçabilité et à la réutilisation.")],
C("Un compte rendu est une reconstitution lisible et vérifiable de la démarche : il ne remplace pas les données brutes.",
  "introduction → protocole → résultats → discussion → conclusion",
  "hypothèse · prédiction · écarts · incertitudes · ouverture · références",
  "Compte rendu~Restitution structuree~Introduction~Contexte et question~Protocole~Methode reproductible~Resultats~Tableaux et graphiques~Donnees brutes~Valeurs originales~Discussion~Interpretation des ecarts~Conclusion~Reponse a la question~Ouverture~Piste complementaire~References~Tracabilite",
  "Rédiger l'introduction avec la question et l'hypothèse|Décrire le protocole et schématiser le montage|Présenter les résultats dans des tableaux|Discuter les écarts et les incertitudes|Conclure et proposer une ouverture",
  "Inventer des résultats manquants|Supprimer les valeurs brutes|Confondre discussion et conclusion|Employer un style personnel|Oublier de citer les références",
  "5 axes de température~Protocole~20 à 50 °C~Tendance confirmée~60 °C~Forte dispersion~15 %~Écart-type~Ouverture~Nouveau protocole",
  "Résultats~Ce qui est obtenu~Discussion~Ce que cela signifie",
  "Conclusion~Réponse~Ouverture~Question suivante"))

# ============================================================ ST1
add("ST1", "Traitement graphique des données expérimentales", "Statistiques et traitement des données", ["1re"],
S("Un graphique doit transformer un tableau de mesures en une lecture rapide et fidèle de l'information."
  "|On choisit le type de graphique selon la nature des données : histogramme pour une variable continue, diagramme en bâtons pour une variable discrète."
  "|Le nuage de points convient pour représenter la relation entre deux grandeurs mesurées."
  "|Les axes portent le nom de la grandeur, l'unité et une échelle régulière et lisible."
  "|Les points sont reportés avec précision, sans les relier artificiellement lorsqu'il n'y a pas de relation continue."
  "|Une barre d'erreur indique l'incertitude de mesure sur chaque point."
  "|Une courbe ou une droite de tendance ne doit être tracée que si le modèle est justifié."
  "|Le titre du graphique indique ce qui est représenté et les conditions de mesure."
  "|Une légende est nécessaire lorsque plusieurs séries de données sont superposées."
  "|L'échelle doit commencer à zéro pour les histogrammes afin de ne pas exagérer les différences."
  "|La lecture d'un graphique demande de distinguer la tendance générale, la dispersion et les points particuliers."
  "|Un graphique bien construit accompagne le raisonnement, il ne le remplace pas."),
[QC("Quel graphique convient à une variable quantitative continue ?", "Le camembert~L'histogramme~Le diagramme en bâtons~La flèche", 1,
     "L'histogramme rassemble les valeurs continues par classes."),
 QC("Quel graphique montre la relation entre deux grandeurs mesurées ?", "Le camembert~Le nuage de points~L'histogramme~Le diagramme de flux", 1,
     "Le nuage de points place chaque couple de mesures en abscisse et ordonnée."),
 QC("Que doit porter un axe correctement légendé ?", "Une couleur~Le nom de la grandeur et l'unité~Une flèche seulement~La date", 1,
     "Grandeur et unité sont indispensables à l'interprétation."),
 QC("Quand tracer une droite de tendance ?", "Toujours~Quand un modèle linéaire est justifié~Jamais~Uniquement pour les camemberts", 1,
     "Relier les points sans justification peut suggérer une relation inexistante."),
 QC("Que représente une barre d'erreur ?", "Une faute de calcul~L'incertitude de mesure~Une valeur aberrante~La moyenne", 1,
     "Elle matérialise l'intervalle d'incertitude autour de la valeur."),
 QC("Pourquoi commencer l'échelle d'un histogramme à zéro ?", "Pour économiser de la place~Pour ne pas exagérer les écarts~Pour le rendre plus beau~Ce n'est pas nécessaire", 1,
     "Une échelle tronquée donne une impression trompeuse des différences."),
 QC("Que faut-il prévoir avec plusieurs séries de données ?", "Une couleur différente seulement~Une légende explicite~Un seul axe~Aucun titre", 1,
     "La légende permet d'identifier chaque série."),
 QT("Expliquer les erreurs à éviter lors de la construction d'un graphique de résultats de titrage.",
    "Il faut d'abord porter le volume versé en abscisse et le pH en ordonnée, avec les unités, et choisir une échelle qui occupe toute la zone de tracé sans être tronquée. Il ne faut pas relier les points par des segments droits : une courbe de titrage est continue et se trace au mieux avec une interpolation régulière. Les points expérimentaux doivent rester visibles pour montrer où portent les mesures. Il faut indiquer le volume équivalent et la zone de virage de l'indicateur si elle est connue. Enfin, le titre doit préciser les solutions utilisées : un graphique sans titre ni légende n'est pas réutilisable.",
    "On cite axes et échelles, non-liaison des points, lisibilité des mesures et informations de contexte."),
 QT("Un nuage de points présente une tendance montante avec une forte dispersion et un point très éloigné. Comment l'interpréter prudemment ?",
    "La tendance montante suggère que les deux grandeurs varient dans le même sens, mais la forte dispersion indique que d'autres facteurs influencent le résultat ou que la précision des mesures est limitée. Le point éloigné peut être une valeur aberrante liée à une erreur de manipulation ou de saisie, ou bien une observation réellement particulière. Avant de le exclure, il faut retourner au cahier de laboratoire, vérifier les conditions de mesure de ce point et éventuellement refaire l'essai. On présente ensuite deux interprétations : avec et sans ce point, en justifiant le choix retenu. La conclusion doit rester prudente et mentionner l'incertitude sur la tendance observée.",
    "On distingue tendance, dispersion et point atypique, puis on propose une vérification et une conclusion nuancée.")],
C("Un graphique lisible et honnête montre la tendance, la dispersion et les incertitudes sans suggérer de relation non justifiée.",
  "axes nommés et unités · échelle non tronquée · points visibles",
  "histogramme · nuage de points · barres d'erreur · légende · titre",
  "Graphique~Representation visuelle~Histogramme~Variable continue~Nuage de points~Deux grandeurs~Axe~Grandeur et unite~Echelle~Progressive non tronquee~Barre d'erreur~Incertitude~Tendance~Direction generale~Dispersion~Ecart des points~Legende~Identification des series",
  "Choisir le type de graphique adapté|Étiqueter les axes avec les unités|Reporter les points et leurs barres d'erreur|Ajouter titre et légende|Lire tendance, dispersion et points atypiques",
  "Relier les points sans modèle|Tronquer l'échelle d'un histogramme|Oublier les unités |Masquer la dispersion|Supprimer un point sans justification",
  "Volume versé~Axe des abscisses~pH~Axe des ordonnées~Points~Mesures experimentales~Barres~Incertitude~Volume equivalent~Lecture du graphique",
  "Histogramme~Distribution d'une variable~Nuage de points~Relation entre deux variables",
  "Tendance~Allure generale~Dispersion~Ecart autour de la tendance"))

# ============================================================ ST2
add("ST2", "Validation statistique des résultats", "Statistiques et traitement des données", ["Terminale"],
S("Valider un résultat, c'est vérifier qu'il est cohérent avec les données, la méthode et les exigences de l'analyse."
  "|La moyenne résume la tendance centrale, tandis que l'écart-type mesure la dispersion des répétitions."
  "|L'écart-type réduit, ou écart-type de la moyenne, vaut s/√n et diminue quand le nombre d'essais augmente."
  "|Un intervalle de confiance encadre la valeur vraie probable avec un niveau de confiance choisi, souvent 95 %."
  "|Un résultat aberrant doit être identifié, documenté et justifié avant d'être éventuellement écarté."
  "|Le test de Grubbs permet de détecter une valeur aberrante unique dans une série approximativement normale."
  "|Un résultat peut être précis sans être juste : la comparaison à un matériau de référence vérifie la justesse."
  "|Un écart systématique se met en évidence par une série de résultats tous décalés dans le même sens."
  "|Le contrôle continu de la méthode vérifie que le procédé reste stable dans le temps."
  "|Une carte de contrôle trace la moyenne des essais avec des limites de décision et d'alerte."
  "|La comparaison avec une valeur certifiée permet d'exprimer un biais et une récupération."
  "|La validation se conclut par une décision explicite : résultat conforme, à refaire ou méthode à corriger."),
[QC("Que mesure l'écart-type d'une série ?", "La moyenne~La dispersion autour de la moyenne~Le nombre d'essais~La valeur maximale", 1,
     "L'écart-type quantifie la variabilité des mesures."),
 QC("Que vaut l'écart-type de la moyenne ?", "s × n~s/√n~s + n~s²/n", 1,
     "Il diminue comme la racine du nombre de répétitions."),
 QC("Quel niveau de confiance est couramment utilisé ?", "50 %~90 %~95 %~100 %", 2,
     "Le niveau de 95 % est le plus fréquent dans les laboratoires."),
 QC("Un résultat précis est-il nécessairement juste ?", "Oui~Non~Uniquement en chimie~Seulement avec trois essais", 1,
     "La précision concerne la dispersion, la justesse la proximité de la valeur vraie."),
 QC("Comment détecter un décalage systématique ?", "En augmentant le nombre d'essais~En comparant à une valeur de référence~En arrondissant les résultats~En changeant d'opérateur", 1,
     "Un biais se révèle par comparaison avec une référence ou un matériau certifié."),
 QC("À quoi sert une carte de contrôle ?", "À tracer des courbes de titrage~À suivre la stabilité d'une méthode dans le temps~À calculer une masse molaire~À remplacer les étalonnages", 1,
     "Elle signale les dérives et les changements de niveau du procédé."),
 QC("Que faut-il faire d'une valeur aberrante ?", "La supprimer sans trace~La documenter avant de décider~La remplacer par la moyenne~L'arrondir", 1,
     "Toute exclusion doit être justifiée et tracée."),
 QT("Trois pesées donnent 10,02 ; 10,04 et 10,03 g pour une valeur de référence de 10,00 g. Calculer la moyenne et commenter la justesse.",
    "La moyenne vaut (10,02 + 10,04 + 10,03)/3 = 30,09/3 = 10,03 g. Les écarts à la moyenne sont 0,01 ; 0,01 et 0,00 g : les mesures sont très regroupées, donc la fidélité est bonne. En revanche, la moyenne 10,03 g s'écarte de 0,03 g de la référence 10,00 g, soit un biais relatif de 0,3 %. Les résultats sont donc précis mais pas tout à fait justes : il faut rechercher une cause systématique, par exemple une tare incorrecte ou une dérive de la balance, avant de valider le résultat.",
    "On calcule la moyenne, on apprécie la dispersion puis on compare à la référence pour juger du biais."),
 QT("Expliquer la différence entre une limite d'alerte et une limite de décision sur une carte de contrôle.",
    "La limite d'alerte, souvent placée à deux écarts-types de la moyenne, signale une dérive probable : elle déclenche une surveillance renforcée ou un contrôle supplémentaire, sans arrêter immédiatement la production. La limite de décision, placée à trois écarts-types, indique une situation statistiquement improbable sous l'hypothèse de procédé stable : elle entraîne l'arrêt de l'analyse, la recherche de la cause et la reprise des essais depuis la dernière valeur conforme. Cette gradation permet de réagir tôt sans multiplier les arrêts injustifiés. Les limites doivent être recalculées après tout changement important de méthode, d'appareil ou de lot de réactifs.",
    "On compare le niveau de réaction associé à chaque limite et la conduite à tenir.")],
C("Valider, c'est distinguer dispersion, biais et dérive avant de déclarer un résultat conforme.",
  "écart-type de la moyenne = s/√n · intervalle à 95 %",
  "justesse · fidélité · valeur aberrante · carte de contrôle · biais",
  "Validation~Decision finale~Fidelite~Dispersion faible~Justesse~Proche de la reference~Ecart-type de la moyenne~s sur racine n~Intervalle de confiance~Encadre la valeur vraie~Valeur aberrante~Point suspect~Carte de controle~Suivi dans le temps~Limite d'alerte~Surveillance~Limite de decision~Arret et cause~Biais~Ecart systematique",
  "Calculer moyenne et écart-type|Comparer à la valeur de référence|Repérer les valeurs aberrantes|Suivre la carte de contrôle|Décider conformité ou reprise",
  "Confondre précision et justesse|Exclure une valeur sans justification|Ignorer une dérive lente|Utiliser un intervalle de confiance sans le niveau|Valider sans comparaison à une référence",
  "10,02;10,04;10,03~Moyenne 10,03 g~Référence 10,00 g~Biais 0,3 %~s/√n~Incertitude de la moyenne~95 %~Niveau courant~2σ~Alerte~3σ~Décision",
  "Fidélité~Répétabilité~Justesse~Exactitude",
  "Alerte~Surveiller~Décision~Arrêter"))

# ============================================================ ST3
add("ST3", "Tests statistiques et comparaison de moyennes", "Statistiques et traitement des données", ["Terminale"],
S("Un test statistique permet de décider si une différence observée entre deux séries est significative ou attribuable au hasard."
  "|L'hypothèse nulle H0 suppose qu'il n'y a pas de différence réelle entre les populations comparées."
  "|L'hypothèse alternative H1 suppose l'existence d'une différence."
  "|Le risque de première espèce, noté alpha, est la probabilité de rejeter H0 alors qu'elle est vraie."
  "|Le risque de deuxième espèce, noté bêta, est la probabilité de ne pas rejeter H0 alors qu'elle est fausse."
  "|La p-value est la probabilité d'observer des données au moins aussi extrêmes si H0 est vraie."
  "|Si la p-value est inférieure au seuil alpha, souvent 0,05, on rejette H0."
  "|Ne pas rejeter H0 ne prouve pas qu'elle est vraie : cela signifie seulement que les données ne permettent pas de la rejeter."
  "|Le test t de Student compare deux moyennes lorsque les données sont quantitatives et approximativement normales."
  "|Le test t apparié s'utilise lorsque les mesures sont appariées, par exemple avant et après traitement sur le même échantillon."
  "|Le test du chi-deux compare des fréquences observées à des fréquences attendues."
  "|Un résultat significatif au sens statistique n'est pas forcément pertinent au sens pratique : il faut aussi juger l'ampleur de l'effet."),
[QC("Que suppose l'hypothèse nulle H0 ?", "Qu'il existe une différence~Qu'il n'y a pas de différence réelle~Que les mesures sont fausses~Que le test est invalide", 1,
     "H0 est l'hypothèse de référence : pas d'effet, pas de différence."),
 QC("Que signifie une p-value inférieure à 0,05 ?", "H0 est prouvée vraie~On rejette H0 au seuil 5 %~La différence est impossible~Le test a échoué", 1,
     "Une p-value faible indique des données peu compatibles avec H0."),
 QC("Qu'est-ce que le risque alpha ?", "Rejeter H0 alors qu'elle est vraie~Accepter H1 à tort~Oublier une mesure~Choisir le mauvais test", 0,
     "Alpha est le risque de faux positif, fixé avant le test."),
 QC("Quel test compare deux moyennes de petits échantillons ?", "Le test du chi-deux~Le test t de Student~Le test de Grubbs~La régression", 1,
     "Le test t compare des moyennes sous hypothèse de normalité approximative."),
 QC("Quand utiliser un test apparié ?", "Quand les échantillons sont indépendants~Quand les mesures sont appariées sur les mêmes unités~Quand les données sont qualitatives~Quand on a une seule mesure", 1,
     "L'appariement permet d'éliminer la variabilité entre unités."),
 QC("Que compare le test du chi-deux ?", "Des moyennes~Des fréquences observées et attendues~Des masses~Des températures", 1,
     "Le chi-deux s'applique aux tableaux de contingence et aux ajustements de lois."),
 QC("Une différence significative est-elle forcément importante ?", "Oui~Non, il faut juger l'ampleur de l'effet~Seulement si p < 0,01~Seulement en biologie", 1,
     "La significativité statistique ne mesure pas l'importance pratique."),
 QT("Interpréter le résultat d'un test : p = 0,03 avec un seuil alpha fixé à 0,05.",
    "La p-value de 0,03 est inférieure au seuil de 0,05 : on rejette l'hypothèse nulle au risque de 5 %. Les données observées sont donc peu compatibles avec l'absence de différence, et l'on conclut à une différence statistiquement significative entre les deux séries comparées. Cela ne signifie pas que H0 est fausse avec certitude : il subsiste un risque de première espèce de 5 %, et le résultat doit être confirmé si l'enjeu est important. Il faut également vérifier les conditions d'application du test et préciser l'ampleur de la différence pour juger de son intérêt pratique.",
    "On compare p à alpha, on conclut en termes de rejet de H0 et on rappelle le risque résiduel."),
 QT("Expliquer pourquoi il ne faut pas choisir le seuil alpha après avoir vu les résultats.",
    "Le seuil alpha fixe à l'avance le risque maximal de conclure à tort à une différence. Si on le choisit après coup, par exemple en passant de 0,05 à 0,10 parce que la p-value vaut 0,08, on ajuste la règle au résultat obtenu : le risque réel de faux positif n'est plus maîtrisé et le test perd sa validité. Cette pratique, appelée p-hacking lorsqu'elle est systématique, gonfle le nombre de conclusions fausses dans la littérature scientifique. La bonne démarche consiste à fixer alpha, la taille de l'échantillon et le test avant la collecte ou du moins avant l'analyse, puis à rapporter la p-value exacte pour que le lecteur puisse juger par lui-même.",
    "On relie la fixation préalable du seuil au contrôle du risque et on cite le biais de p-hacking.")],
C("Un test statistique ne prouve rien : il quantifie la compatibilité des données avec une hypothèse de référence.",
  "p < alpha → rejet de H0",
  "H0 · H1 · risques alpha et bêta · p-value · test t · chi-deux",
  "Test~Décision statistique~Hypothese nulle~Pas de difference~Hypothese alternative~Existence d'un effet~Risque alpha~Faux positif~Risque beta~Faux negatif~P-value~Probabilite sous H0~Seuil~Valeur critique fixee~Test t~Compare des moyennes~Chi-deux~Compare des frequences~Effet~Ampleur pratique",
  "Formuler H0 et H1 avant l'analyse|Fixer le seuil alpha|Vérifier les conditions du test|Calculer la statistique et la p-value|Conclure et discuter l'ampleur de l'effet",
  "Choisir le seuil après les résultats|Confondre p-value et probabilité que H0 soit vraie|Conclure que H0 est prouvée|Ignorer les conditions d'application|Oublier l'ampleur de l'effet",
  "p = 0,03~Inférieur à 0,05~Rejet de H0~Alpha 5 %~Risque de faux positif~Test t~Deux moyennes~Chi-deux~Fréquences~Apparié~Avant et après",
  "H0~Pas d'effet~H1~Effet réel",
  "Significatif~Statistiquement~Pertinent~Pratiquement"))

# ============================================================ ST4
add("ST4", "Régression linéaire et modélisation des données", "Statistiques et traitement des données", ["Terminale"],
S("La modélisation consiste à représenter une relation expérimentale par une fonction simple dont les paramètres sont estimés."
  "|Une relation linéaire s'écrit y = a·x + b, avec a la pente et b l'ordonnée à l'origine."
  "|La méthode des moindres carrés choisit la droite qui minimise la somme des carrés des écarts entre points et droite."
  "|Le coefficient de détermination R² indique la part de la variance de y expliquée par la droite."
  "|Un R² proche de 1 signale un bon ajustement, mais ne garantit pas que le modèle linéaire soit le bon."
  "|Il faut toujours examiner les résidus, c'est-à-dire les écarts entre valeurs observées et valeurs prédites."
  "|Des résidus structurés en courbe indiquent qu'un modèle non linéaire serait plus adapté."
  "|La pente s'interprète dans le contexte : elle donne la variation de y pour une augmentation d'une unité de x."
  "|Une régression ne permet pas d'affirmer un lien de causalité : elle décrit une association."
  "|L'extrapolation hors du domaine exploré est risquée car le modèle n'y a pas été validé."
  "|Les incertitudes sur les paramètres renseignent sur la précision de la pente et de l'ordonnée à l'origine."
  "|En chimie analytique, la droite d'étalonnage est un exemple de régression utilisée pour doser un échantillon."),
[QC("Que minimise la méthode des moindres carrés ?", "La somme des valeurs~La somme des carrés des écarts~Le nombre de points~La pente", 1,
     " Elle minimise la somme des résidus au carré."),
 QC("Que vaut la pente d'une droite de régression ?", "La valeur de y pour x = 0~La variation de y pour +1 sur x~Le nombre de points~L'écart-type", 1,
     "La pente a donne la variation de y par unité de x."),
 QC("Qu'indique un R² proche de 1 ?", "Un mauvais ajustement~Une forte part de variance expliquée~Une pente nulle~Des résidus structurés", 1,
     "R² mesure la proportion de variance expliquée par le modèle."),
 QC("Que sont les résidus ?", "Les points de mesure~Les écarts entre observé et prédit~Les erreurs de calcul~Les unités des axes", 1,
     "Un résidu est la différence entre valeur observée et valeur ajustée."),
 QC("Des résidus en forme de courbe indiquent…", "Un ajustement parfait~Qu'un modèle non linéaire serait meilleur~Une erreur de saisie~Une pente négative", 1,
     "Une structure dans les résidus trahit un modèle inadapté."),
 QC("Une corrélation prouve-t-elle la causalité ?", "Oui~Non, elle décrit une association~Oui si R² > 0,9~Seulement en physique", 1,
     "Une variable non mesurée peut expliquer les deux grandeurs."),
 QC("Pourquoi éviter l'extrapolation ?", "Parce que le modèle n'est validé que sur le domaine étudié~Parce que les points sont trop nombreux~Parce que R² est toujours faible~Parce que la pente est nulle", 0,
     "Hors domaine, la relation peut changer de forme."),
 QT("Une droite d'étalonnage a pour équation y = 1250·x + 0,02 avec R² = 0,999. Interpréter la pente, l'ordonnée à l'origine et la qualité de l'ajustement.",
    "La pente 1250 signifie qu'une augmentation de concentration de 1 mol/L augmente le signal de 1250 unités : c'est la sensibilité de la méthode. L'ordonnée à l'origine 0,02 représente le signal résiduel mesuré pour une concentration nulle, c'est-à-dire le fond ou le blanc : il est faible, ce qui est satisfaisant. Le R² de 0,999 indique que 99,9 % de la variance du signal est expliquée par la relation linéaire : l'ajustement est excellent. Il reste néanmoins à vérifier graphiquement que les résidus sont répartis aléatoirement et que la gamme couvre bien la concentration de l'échantillon à doser.",
    "On interprète chaque paramètre dans le contexte et on nuance la qualité du R² par l'examen des résidus."),
 QT("Expliquer pourquoi une forte corrélation entre deux grandeurs ne permet pas de conclure à une relation de cause à effet.",
    "Une corrélation indique que deux grandeurs varient ensemble, mais elle ne dit pas laquelle influence l'autre, ni si une troisième variable est responsable. Par exemple, la quantité de glace vendue et le nombre de noyades augmentent ensemble en été : la chaleur est la cause commune, et non la glace. En laboratoire, une dérive de température peut faire varier simultanément le signal et le temps de mesure, créant une corrélation trompeuse. Pour établir une causalité, il faut un protocole expérimental qui modifie volontairement une seule variable, avec des témoins et des conditions contrôlées. La régression reste un outil de description et de prédiction dans le domaine exploré.",
    "On cite la variable confuse et la nécessité d'une expérience contrôlée pour parler de causalité.")],
C("La régression donne un modèle et des paramètres ; sa validité se juge sur les résidus et le domaine exploré.",
  "y = a·x + b · R² proche de 1 ≠ modèle garanti",
  "moindres carrés · résidus · sensibilité · causalité · extrapolation",
  "Regression~Ajustement d'un modele~Moindres carres~Minimise les ecarts~Pente~Sensibilite~Ordonnee a l'origine~Signal a concentration nulle~R²~Variance expliquee~Residus~Ecarts observes predits~Structure~Modele inadapte~Extrapolation~Hors domaine~Causalite~Relation de cause",
  "Représenter les points et choisir un modèle|Estimer les paramètres par régression|Calculer R²|Examiner les résidus|Interpréter les paramètres dans le contexte",
  "Faire confiance au seul R²|Relier les points expérimentaux|Extrapoler hors gamme|Confondre corrélation et causalité|Ignorer les incertitudes sur les paramètres",
  "pente 1250~Sensibilite~b = 0,02~Signal de fond~R² = 0,999~99,9 % expliquee~Residus~A examiner~Modele lineaire~Domaine valide",
  "Corrélation~Variation ensemble~Causalité~Une variable agit sur l'autre",
  "Interpolation~Dans le domaine~Extrapolation~Hors domaine"))

# ============================================================ AT1
add("AT1", "English vocabulary: laboratory equipment and safety", "Anglais technique", ["1re"],
S("Laboratory vocabulary is essential to follow a procedure and to report results in English; a clear vocabulary reduces the risk of misunderstanding in an international laboratory."
  "|Common glassware includes a beaker, a flask, a test tube, a pipette, a burette and a measuring cylinder."
  "|A balance is used to weigh a sample, while an oven is used to dry a precipitate."
  "|A fume cupboard removes toxic vapours; a safety shower and an eyewash are used in an emergency."
  "|To heat a solution, you can use a water bath, a heating mantle or a hot plate."
  "|The verb 'to dilute' means to add solvent, whereas 'to filter' means to separate a solid from a liquid."
  "|'To titrate' means to add a solution of known concentration until the equivalence point is reached."
  "|A label must include the name of the chemical, the hazard symbols and the date of opening."
  "|The safety data sheet is abbreviated SDS and contains sixteen sections."
  "|Wear a lab coat, gloves and goggles before handling hazardous chemicals."
  "|Never taste a chemical and never pipette by mouth: use a pipette filler instead."
  "|The words 'soluble', 'insoluble', 'volatile' and 'corrosive' describe important properties."),
[QC("Which instrument is used to weigh a sample?", "A burette~A balance~A microscope~A thermometer", 1,
     "A balance measures mass; a burette measures a volume."),
 QC("What is a fume cupboard used for?", "To store chemicals~To remove toxic vapours~To dry glassware~To heat a solution", 1,
     "It extracts vapours and protects the operator."),
 QC("What does 'to dilute' mean?", "To add solvent~To remove water~To mix two solids~To filter a liquid", 0,
     "Dilution adds solvent while keeping the amount of solute constant."),
 QC("Which equipment protects the eyes?", "A lab coat~Goggles~A glove~An oven", 1,
     "Goggles protect against splashes and fragments."),
 QC("What does SDS stand for?", "Standard dilution sheet~Safety data sheet~Sample detection system~Solid delivery system", 1,
     "The SDS provides information on hazards and precautions."),
 QC("Which word describes a substance that easily evaporates?", "Soluble~Volatile~Insoluble~Concentrated", 1,
     "Volatile substances have a high vapour pressure and evaporate easily."),
 QC("What must never be done with a pipette?", "Using a pipette filler~Pipetting by mouth~Rinsing it~Reading the volume", 1,
     "Mouth pipetting is strictly forbidden in every laboratory."),
 QT("Translate these safety instructions into English and explain one of them: 'Porter une blouse et des gants. Ne jamais goûter un réactif. Rincer l'oeil pendant quinze minutes.'",
    "Wear a lab coat and gloves. Never taste a chemical. Rinse the eye for fifteen minutes. The third instruction is a first-aid measure: after a chemical splash, the eye must be rinsed with plenty of water for at least fifteen minutes to remove the product and limit damage. The verb 'rinse' is used for washing with water, and the duration is given with 'for'. These are standard imperatives used in safety procedures.",
    "The translation must use the imperative and the correct vocabulary for protective equipment and first aid."),
 QT("Describe a simple filtration procedure in five English sentences using at least four vocabulary words from this chapter.",
    "Example answer: First, weigh the precipitate on a balance. Then, place a filter paper in a funnel. Next, pour the mixture slowly through the filter. The solid stays on the paper and the liquid is collected in a beaker. Finally, dry the solid in an oven and weigh it again. The answer uses balance, funnel, filter, beaker and oven, and the sequence is introduced by first, then, next and finally.",
    "The five sentences must describe a logical sequence and use precise laboratory vocabulary.")],
C("Laboratory English combines equipment names, action verbs and safety imperatives that must be used precisely.",
  "wear · dilute · filter · titrate · rinse",
  "beaker, burette, balance · SDS · goggles · fume cupboard",
  "Glassware~Beaker, flask, burette~Balance~Weigh a sample~Fume cupboard~Removes vapours~Eyewash~Rinse the eye~Dilute~Add solvent~Filter~Separate solid and liquid~Titrate~Reach equivalence~Lab coat and goggles~Personal protection~SDS~Sixteen sections",
  "Learn the equipment names|Match each verb to its action|Use the imperative for safety rules|Read an SDS in English|Write a short procedure with sequence words",
  "Confusing beaker and flask|Using 'taste' in a procedure|Forgetting the article before a countable noun|Translating 'diluer' as to dissolve|Pipetting by mouth",
  "Balance~Weigh~Burette~Titrate~Fume cupboard~Vapours~SDS~16 sections~Goggles~Eye protection~Volatile~Evaporates easily",
  "To dilute~Ajouter du solvant~To dissolve~Dissoudre",
  "Equipment~Objets~Procedure~Gestes"))

# ============================================================ AT2
add("AT2", "Reading a scientific abstract in English", "Anglais technique", ["Terminale"],
S("A scientific abstract is a short summary of a research paper, usually between 150 and 250 words."
  "|It follows a standard structure: background, aim, methods, results and conclusion."
  "|The background gives the context and states why the question is important."
  "|The aim is often introduced by 'this study investigates', 'the objective of this work is' or 'we aimed to'."
  "|The methods section describes the material, the protocol and the analytical techniques used."
  "|The passive voice is frequent: 'samples were analysed', 'the solution was heated'."
  "|The results are introduced by 'we found that', 'the results show that' or 'it was observed that'."
  "|Typical reporting verbs include indicate, suggest, demonstrate, reveal and confirm."
  "|Numbers are written with a decimal point in English: 0.25, not 0,25."
  "|The conclusion states the main finding and may mention limitations or perspectives."
  "|Hedging verbs such as may, might, appear and seem express appropriate caution."
  "|Reading an abstract efficiently means identifying the aim, the main result and the conclusion before reading the full paper."),
[QC("What are the five parts of a standard abstract?", "Title, index, table, figure~Background, aim, methods, results, conclusion~Introduction, discussion, references~Aim, data, graph, law", 1,
     "The classic structure follows the logical sequence of a scientific article."),
 QC("Which phrase introduces the aim of a study?", "It was observed that~This study investigates~The results indicate~In conclusion", 1,
     "This study investigates introduces the research objective."),
 QC("Which sentence uses the passive voice?", "We heated the solution~The solution was heated~The solution heats~Heating the solution", 1,
     "The passive uses be + past participle: was heated."),
 QC("How is 0,25 written in a scientific English text?", "0,25~0.25~0 25~25.0", 1,
     "English uses a decimal point, not a comma."),
 QC("What does the verb 'suggest' express in an abstract?", "A certain proof~A cautious interpretation~A method~A measurement error", 1,
     "Suggest and indicate introduce an interpretation rather than an absolute proof."),
 QC("Which section describes the protocol?", "The background~The methods~The conclusion~The references", 1,
     "The methods section explains how the study was carried out."),
 QC("What is the purpose of hedging in a scientific text?", "To hide the results~To express appropriate caution~To lengthen the abstract~To avoid numbers", 1,
     "Hedging shows that a conclusion is supported but not absolute."),
 QT("Identify the structure of this abstract extract and translate its main result: 'This study investigates the effect of temperature on enzyme activity. Samples were incubated at 30 °C and 60 °C. The results indicate that activity decreases by 40 % at 60 °C.'",
    "The first sentence states the aim: this study investigates the effect of temperature on enzyme activity. The second sentence belongs to the methods: samples were incubated at two temperatures, in the passive voice. The third sentence gives the result: the results indicate that activity decreases by 40 % at 60 °C. Translated into French : « Cette étude examine l'effet de la température sur l'activité enzymatique. Les échantillons ont été incubés à 30 °C et 60 °C. Les résultats indiquent que l'activité diminue de 40 % à 60 °C. » The verb indicate shows a measured finding without overstating its general scope.",
    "The answer must identify aim, methods and result, and translate the finding accurately."),
 QT("Explain why the passive voice and hedging are common in scientific articles written in English.",
    "The passive voice shifts the focus from the researcher to the experiment and the results: 'samples were analysed' sounds more objective than 'I analysed the samples'. It is also useful when the person who performed the action is irrelevant or when a team carried it out. Hedging with verbs such as suggest, appear or may reflects the provisional nature of scientific knowledge: an experiment provides evidence for an interpretation but rarely proves it universally. Together, these features give a text a neutral and cautious tone, which increases its credibility. A good scientific reader pays attention to them to distinguish a measured fact from an interpretation.",
    "The answer must link passive voice to objectivity and hedging to caution and credibility.")],
C("An abstract condenses a study into aim, methods, results and conclusion, using passive voice and cautious reporting verbs.",
  "aim → methods → results → conclusion",
  "this study investigates · samples were analysed · results indicate",
  "Abstract~Resume court~Aim~Objectif de l'etude~Methods~Protocole et materiel~Results~Resultats mesures~Passive voice~Was analysed~Reporting verb~Indicate, suggest~Decimal point~0.25~Hedging~May, seem~Conclusion~Portee et limites",
  "Read the title and identify the research question|Locate the aim sentence|Identify the methods and the passive constructions|Extract the main result with its number|Summarise the conclusion in one sentence",
  "Translating 0.25 as 0,25|Confusing results and conclusion|Taking suggest as a proof|Ignoring the methods section|Translating word for word",
  "This study investigates~Aim~Samples were incubated~Methods~Results indicate~Finding~40 %~Result value~30 °C~Condition~In conclusion~Conclusion phrase",
  "Active voice~We measured~Passive voice~It was measured",
  "Fact~Measured observation~Interpretation~Suggested meaning"))

# ============================================================ AT3
add("AT3", "Writing a short lab report in English", "Anglais technique", ["Terminale"],
S("A lab report in English follows a fixed structure that makes the work easy to check and to reproduce."
  "|The main sections are title, aim, materials, method, results, discussion and conclusion."
  "|The aim is written in the infinitive or with the present simple: 'To determine the concentration of...' or 'This experiment determines...'."
  "|The materials are listed as a clear list of equipment and reagents, with quantities and concentrations."
  "|The method is usually written in the passive voice and in the past tense: 'The solution was heated for five minutes.'"
  "|Sequence words such as first, then, afterwards and finally guide the reader through the procedure."
  "|The results are stated objectively: 'The absorbance was 0.62 at 540 nm' rather than 'the result was nice'."
  "|Graphs and tables are numbered and referred to in the text: 'as shown in Figure 1'."
  "|The discussion compares the results with the prediction and explains possible sources of error."
  "|Modal verbs express caution: 'the difference may be due to a temperature variation'."
  "|The conclusion answers the initial question and uses phrases such as 'in conclusion' or 'overall'."
  "|Accuracy of vocabulary, correct articles and consistent tenses are assessed in a technical English report."),
[QC("Which tense is typical for the method section?", "Present continuous~Past simple passive~Future simple~Present perfect", 1,
     "The method describes what was done: the solution was heated."),
 QC("How should the aim be written?", "In the first person~With an infinitive or the present simple~In the passive voice only~As a question only", 1,
     "To determine... or This experiment determines... are standard openings."),
 QC("Which phrase introduces a sequence?", "However~Then~Therefore~In conclusion", 1,
     "Then and afterwards mark the order of operations."),
 QC("Which sentence is an objective result?", "The experiment was interesting~The absorbance was 0.62 at 540 nm~The result was beautiful~I liked the colour", 1,
     "Objective results give measurable values with units."),
 QC("How should a figure be mentioned?", "Look at the picture~As shown in Figure 1~See here~The thing above", 1,
     "Figures and tables are numbered and cited explicitly."),
 QC("Which modal expresses cautious interpretation?", "Must~May~Will~Can only", 1,
     "May indicates a possible explanation without certainty."),
 QC("What does the conclusion do?", "Lists the reagents~Answers the initial question~Describes the method~Shows the equipment", 1,
     "It provides a concise answer and may open perspectives."),
 QT("Rewrite this method in a suitable style for a lab report: 'I put 10 mL of acid in a beaker. Then I added the indicator and I heated the solution.'",
    "A suitable version is: '10 mL of the acid solution were placed in a beaker. The indicator was then added and the solution was heated for five minutes.' The subject is the action or the material rather than the person, the verbs are in the past simple passive, the sequence is marked by then, and a duration is added for precision. Articles and quantities are kept: 10 mL of the acid solution. This style is impersonal, reproducible and consistent with the conventions of scientific writing in English.",
    "The rewrite must use past simple passive, sequence words and precise quantities."),
 QT("Write a short discussion of a titration result in English, using one cautious modal and one reference to a table.",
    "Example answer: 'As shown in Table 1, the equivalence volume was 15.0 mL, which gives an acid concentration of 0.075 mol/L. This value is slightly higher than the expected concentration. The difference may be due to an error in reading the burette or to a delayed colour change of the indicator. Repeating the titration three times would improve the reliability of the result.' The answer refers to Table 1, reports a numerical result, uses may for a cautious explanation and suggests an improvement.",
    "The discussion must include a result, a table reference, a hedged explanation and an improvement.")],
C("A technical report in English is impersonal, precise and structured: passive voice for the method, numbers for the results, caution for the discussion.",
  "aim → materials → method → results → discussion → conclusion",
  "was heated · as shown in Figure 1 · may be due to",
  "Lab report~Scientific report~Aim~Objective in infinitive~Materials~Equipment and reagents~Method~Passive past~Results~Objective numbers~Discussion~Interpretation and errors~Conclusion~Answer to the question~Figure~Numbered reference~Hedging~May, might",
  "Write a clear title and aim|List the materials with quantities|Describe the method in past passive|Present the results with numbers and figures|Discuss and conclude with caution",
  "Using I in the method|Writing beautiful instead of a measurement|Forgetting to number figures|Confusing discussion and conclusion|Using must for a hypothesis",
  "10 mL were placed~Past passive~Then heated~Sequence~Absorbance 0.62~Objective result~Figure 1~Reference~May be due to~Cautious explanation~In conclusion~Closing phrase",
  "Method~What was done~Discussion~What it means",
  "May~Possible explanation~Must~Strong obligation"))

# ============================================================ EM1
add("EM1", "La laïcité et les valeurs de la République", "EMC", ["1re"],
S("La laïcité est un principe constitutionnel qui garantit la liberté de conscience et l'égalité de tous devant la loi."
  "|La loi du 9 décembre 1905 sépare les Églises et l'État : la République ne reconnaît ni ne subventionne aucun culte."
  "|L'article 1er de la Constitution de 1958 affirme que la France est une République indivisible, laïque, démocratique et sociale."
  "|La liberté de conscience permet à chacun de croire ou de ne pas croire, sans contrainte ni discrimination."
  "|La laïcité ne signifie pas l'absence de religion, mais la neutralité de l'État et le respect de toutes les convictions."
  "|Le principe de neutralité s'impose aux agents publics dans l'exercice de leurs fonctions."
  "|Les usagers du service public sont traités de manière égale, quelles que soient leurs opinions ou leurs croyances."
  "|À l'école, la laïcité s'applique aux enseignements, aux personnels et aux élèves, avec des règles de tenue et d'expression."
  "|Les signes ou tenues qui manifestent une appartenance religieuse sont interdits aux élèves dans les établissements publics."
  "|La laïcité protège aussi la liberté d'expression, dès lors que celle-ci ne trouble pas l'ordre public."
  "|Le respect d'autrui, le refus des discriminations et lafraternité sont des valeurs indissociables de la laïcité."
  "|Dans un laboratoire, la laïcité se traduit par une attitude professionnelle et respectueuse envers tous les collègues."),
[QC("Que garantit le principe de laïcité ?", "Une religion officielle~La liberté de conscience et l'égalité devant la loi~L'interdiction de toute croyance~La supériorité d'un culte", 1,
     "La laïcité protège la liberté de croire ou de ne pas croire et l'égalité de tous."),
 QC("Quelle loi consacre la séparation des Églises et de l'État en France ?", "La loi du 9 décembre 1905~La Constitution de 1958~La loi Ferry de 1881~Le Code civil de 1804", 0,
     "La loi de séparation est votée le 9 décembre 1905."),
 QC("Que dit l'article 1er de la Constitution de 1958 ?", "La France est une monarchie~La France est une République indivisible, laïque, démocratique et sociale~La France a une religion d'État~La France est fédérale", 1,
     "Cet article définit les caractères de la République."),
 QC("Qui est soumis au principe de neutralité dans le service public ?", "Les seuls élèves~Les agents publics dans l'exercice de leurs fonctions~Tous les citoyens en toute circonstance~Les seuls enseignants", 1,
     "Les agents publics doivent être neutres dans leur activité professionnelle."),
 QC("La laïcité signifie-t-elle l'absence de religion ?", "Oui~Non, elle garantit la liberté de religion dans le respect de la neutralité publique~Oui, dans les écoles seulement~Seulement pour les adultes", 1,
     "Elle organise la coexistence des croyances, sans les interdire."),
 QC("Quel comportement respecte la laïcité à l'école ?", "Imposer sa croyance~Respecter les convictions de chacun~Refuser de travailler avec un camarade~Commenter une tenue religieuse", 1,
     "Le respect d'autrui est au cœur de la laïcité scolaire."),
 QC("Quelle valeur est liée à la laïcité ?", "La discrimination~La fraternité et le refus des exclusions~La hiérarchie sociale~Le prosélytisme", 1,
     "Égalité et fraternité sont des valeurs républicaines indissociables."),
 QT("Expliquer la différence entre la neutralité de l'État et la liberté de conscience des citoyens.",
    "La neutralité de l'État impose aux institutions et à leurs agents de ne pas manifester de préférence religieuse dans l'exercice de leurs fonctions : l'État ne reconnaît ni ne finance de culte et traite tous les usagers de la même manière. La liberté de conscience, elle, appartient à chaque personne : elle peut croire ou ne pas croire, changer de religion ou n'en avoir aucune, exprimer ses convictions dans la vie privée et dans le respect de l'ordre public. La laïcité articule les deux : elle limite l'action publique pour garantir à chacun une liberté égale. Une confusion fréquente consiste à croire qu'elle interdit les religions : elle interdit seulement leur imposition par l'État.",
    "On oppose l'obligation de neutralité des institutions au droit individuel de croire ou non."),
 QT("Comment appliquer le principe de laïcité dans un laboratoire scolaire accueillant des élèves de cultures différentes ?",
    "On applique d'abord les règles communes : respect de tous, absence de propos discriminatoires, même tenue de travail et mêmes consignes de sécurité pour chacun. Les élèves ne portent pas de signes religieux dans l'établissement public, et les personnels restent neutres dans leur façon d'enseigner et d'évaluer. On évite les exemples ou les blagues qui stigmatisent une communauté, et on traite les questions religieuses avec le même respect, que ce soit pour les croyances ou pour l'absence de croyance. Enfin, on veille à ce que l'organisation du travail, les groupes et l'accès au matériel ne créent aucune exclusion : la laïcité est alors une pratique concrète d'égalité et de fraternité.",
    "On relie les règles de tenue, la neutralité des personnels et le refus concret des discriminations.")],
C("La laïcité protège la liberté de chacun en imposant la neutralité de l'État et l'égalité de traitement.",
  "1905 : séparation des Églises et de l'État",
  "liberté de conscience · neutralité · égalité · fraternité · refus des discriminations",
  "Laicite~Principe republicain~Loi 1905~Separation des Eglises et de l'Etat~Article 1er~Republique indivisible~Liberte de conscience~Croire ou ne pas croire~Neutralite~Agents publics~Egalite~Meme traitement~Signes religieux~Interdits a l'ecole publique~Fraternite~Respect d'autrui~Discrimination~Refus",
  "Définir le principe en jeu|Respecter la neutralité du service public|Traiter tous les usagers de la même façon|Refuser tout propos discriminatoire|Expliquer le cadre juridique",
  "Confondre laïcité et interdiction de la religion|Imposer une croyance|Tenir des propos discriminatoires|Mélanger vie privée et action publique|Ignorer la loi de 1905",
  "9 décembre 1905~Loi de separation~Article 1er~Republique laique~Neutralite~Service public~Egalite~Tous les usagers~Fraternite~Valeur republicaine",
  "Neutralité de l'État~Pas de culte officiel~Liberté de conscience~Choix individuel",
  "Laïcité~Cadre commun~Tolérance~Respect des différences"))

# ============================================================ EM2
add("EM2", "Citoyenneté, droits et devoirs dans le travail", "EMC", ["1re"],
S("La citoyenneté est l'appartenance d'une personne à une communauté politique qui lui confère des droits et des devoirs."
  "|En France, la nationalité française donne accès à la citoyenneté, avec le droit de vote et l'éligibilité."
  "|Les droits fondamentaux sont énoncés par la Déclaration des droits de l'homme et du citoyen de 1789 et par la Constitution de 1958."
  "|Parmi ces droits figurent la liberté d'expression, le droit à l'instruction, le droit de propriété et l'égalité devant la loi."
  "|La Déclaration universelle des droits de l'homme de 1948 étend ces principes au niveau international."
  "|Les droits sociaux comprennent le droit au travail, à la protection sociale et à des conditions de travail décentes."
  "|Le Code du travail fixe les règles du contrat de travail, de la durée du travail, du salaire et de la sécurité."
  "|Le droit du travail protège notamment contre le harcèlement, la discrimination et le licenciement abusif."
  "|Les devoirs du salarié incluent l'exécution du contrat, la discrétion professionnelle et le respect des consignes de sécurité."
  "|La liberté d'expression au travail existe mais se limite par le devoir de réserve et le respect d'autrui."
  "|Le comité social et économique, ou CSE, représente les salariés et intervient sur les conditions de travail."
  "|Agir en citoyen au travail, c'est connaître ses droits, respecter ceux des autres et participer à la vie collective."),
[QC("Quel texte de 1789 énonce les droits fondamentaux en France ?", "Le Code du travail~La Déclaration des droits de l'homme et du citoyen~La Charte de 1814~Le traité de Rome", 1,
     "La DDHC du 26 août 1789 est le socle des droits fondamentaux."),
 QC("Quelle déclaration internationale date de 1948 ?", "La Déclaration universelle des droits de l'homme~La Déclaration de 1789~La Constitution de 1958~La Charte sociale européenne", 0,
     "La DUDH est proclamée par l'ONU le 10 décembre 1948."),
 QC("Quel droit permet de participer au choix des représentants politiques ?", "Le droit de propriété~Le droit de vote~Le droit à l'instruction~La liberté d'expression", 1,
     "Le droit de vote est un élément central de la citoyenneté."),
 QC("Que fixe le Code du travail ?", "Les règles du contrat et des conditions de travail~Le budget de l'État~Les traités européens~Les programmes scolaires", 0,
     "Il encadre la relation de travail et protège les salariés."),
 QC("Quel est un devoir du salarié ?", "Refuser les consignes de sécurité~Respecter le contrat et les règles de sécurité~Fixer son salaire~Embaucher des collègues", 1,
     "Exécuter le contrat et appliquer les consignes sont des obligations professionnelles."),
 QC("Quel rôle joue le CSE ?", "Representer les salariés~Remplacer l'employeur~Fixer les prix~Diriger l'entreprise", 0,
     "Le comité social et économique est l'organe représentatif du personnel."),
 QC("La liberté d'expression au travail est-elle absolue ?", "Oui~Non, elle est limitée par le respect d'autrui et le devoir de réserve~Seulement pour les cadres~Uniquement hors du travail", 1,
     "Des limites légales et professionnelles s'appliquent à tous."),
 QT("Distinguer un droit fondamental d'un droit social et donner un exemple de chacun.",
    "Un droit fondamental est une liberté ou une protection reconnue à toute personne par les grands textes, comme la liberté d'expression ou l'égalité devant la loi, énoncées par la DDHC de 1789 et la DUDH de 1948. Un droit social est un droit lié à la situation de travailleur et à la protection sociale : droit au salaire, à la durée légale du travail, aux congés ou à la sécurité au travail, garantis notamment par le Code du travail. Les premiers s'adressent à tous les êtres humains, les seconds aux salariés dans le cadre de leur emploi. Les deux niveaux se complètent : la dignité de la personne fonde les droits sociaux.",
    "On oppose l'universalité des droits fondamentaux à la protection liée au travail, avec un exemple de chaque"),
 QT("Un salarié est témoin de propos harcelants dans son équipe. Que lui permettent ses droits et quels devoirs s'imposent à lui ?",
    "Ses droits : le Code du travail et la loi protègent contre le harcèlement moral ou sexuel ; il peut signaler les faits à son responsable, au service des ressources humaines, au CSE ou à l'inspection du travail, sans crainte de représailles. Le devoir de loyauté ne l'oblige pas à se taire face à une situation illégale. Ses devoirs : décrire les faits de manière précise et factuelle, respecter la procédure interne, ne pas diffuser d'accusation non vérifiée et préserver la confidentialité des informations personnelles. La démarche collective passe aussi par le CSE, qui peut diligenter une enquête. Agir ainsi, c'est exercer sa citoyenneté dans l'entreprise en protégeant la dignité des personnes.",
    "On cite les voies de signalement et l'obligation de factuel, de confidentialité et de respect de la procédure.")],
C("La citoyenneté au travail combine des droits protégés par la loi et des devoirs de respect, de sécurité et de solidarité.",
  "DDHC 1789 · DUDH 1948 · Code du travail",
  "droit de vote · libertés · droits sociaux · CSE · harcèlement · devoir de réserve",
  "Citoyennete~Appartenance politique~Droits~Libertes protegees~Devoirs~Obligations~DDHC~Textes de 1789~DUDH~Declaration 1948~Code du travail~Regles de l'emploi~Droits sociaux~Salaire, conges~CSE~Representation du personnel~Harcement~Atteinte a la dignite~Devoir de reserve~Limite a l'expression",
  "Identifier le droit ou le devoir en jeu|Citer le texte de référence|Respecter la procédure de signalement|Agir avec factuel et confidentialité|Participer à la vie collective via le CSE",
  "Confondre droit fondamental et droit social|Croire que la liberté d'expression est absolue|Ignorer les voies de signalement|Diffuser des rumeurs|Oublier les consignes de sécurité",
  "1789~DDHC~1948~DUDH~Code du travail~Contrat et sécurité~CSE~Représentants du personnel~Harcèlement~Interdit et sanctionné~Salaire~Droit social",
  "Droits~Ce que l'on peut exiger~Devoirs~Ce que l'on doit faire",
  "Liberté d'expression~Droit fondamental~Devoir de réserve~Limite professionnelle"))

# ============================================================ EM3
add("EM3", "Développement durable et responsabilité citoyenne", "EMC", ["Terminale"],
S("Le développement durable répond aux besoins du présent sans compromettre la capacité des générations futures à répondre aux leurs."
  "|Cette définition, popularisée par le rapport Brundtland de 1987, articule trois piliers : économique, social et environnemental."
  "|Les objectifs de développement durable, adoptés par l'ONU en 2015, déclinent ces ambitions en dix-sept objectifs à l'horizon 2030."
  "|La protection de la biodiversité, la lutte contre le changement climatique et la gestion de l'eau figurent parmi les enjeux environnementaux."
  "|La responsabilité sociétale des entreprises, ou RSE, intègre ces préoccupations dans la stratégie et les pratiques de l'organisation."
  "|Au laboratoire, le développement durable se traduit par la réduction des déchets, le tri des solvants et l'économie d'énergie."
  "|Une démarche d'éco-conception vise à réduire l'impact environnemental d'un produit dès sa phase de conception."
  "|Le principe de précaution invite à agir face à un risque grave même si les données scientifiques sont encore incomplètes."
  "|Le principe du pollueur-payeur fait supporter à l'activité économique le coût de la pollution qu'elle génère."
  "|La citoyenneté environnementale passe par l'information, la consommation responsable et la participation à des actions collectives."
  "|Les conflits d'usage de l'eau ou des sols montrent que les choix techniques sont aussi des choix politiques et éthiques."
  "|Un geste professionnel responsable combine efficacité du travail, sécurité des personnes et respect de l'environnement."),
[QC("D'où vient la définition moderne du développement durable ?", "Du rapport Brundtland de 1987~De la loi de 1905~Du traité de Versailles~De la Constitution de 1958", 0,
     "Le rapport « Notre avenir à tous » de la commission Brundtland la popularise en 1987."),
 QC("Combien de piliers comporte le développement durable ?", "Deux~Trois~Quatre~Cinq", 1,
     "Les piliers économique, social et environnemental sont indissociables."),
 QC("Combien d'objectifs de développement durable l'ONU a-t-elle adoptés en 2015 ?", "8~12~17~25", 2,
     "L'agenda 2030 comprend 17 objectifs de développement durable."),
 QC("Quel principe fait supporter le coût de la pollution à son auteur ?", "Le principe de précaution~Le principe du pollueur-payeur~Le principe de prévention~Le principe d'équité", 1,
     "Le pollueur-payeur internalise le coût environnemental dans l'activité économique."),
 QC("Que désigne la RSE ?", "Une norme de sécurité incendie~La responsabilité sociétale des entreprises~Un réseau de santé européen~Une règle de comptabilité", 1,
     "La RSE intègre les impacts sociaux et environnementaux dans la stratégie."),
 QC("Quel geste relève d'un laboratoire durable ?", "Jeter tous les solvants dans l'égout~Trier les déchets et limiter les volumes~Laisser les appareils allumés~Acheter toujours le matériel le moins cher", 1,
     "Le tri, la réduction des volumes et la maîtrise de l'énergie sont des gestes concrets."),
 QC("Le principe de précaution s'applique…", "Uniquement après certification scientifique~Face à un risque grave même avec des données incomplètes~Jamais dans l'industrie~Uniquement pour la biodiversité", 1,
     "Il permet d'agir pour éviter un dommage grave malgré l'incertitude scientifique."),
 QT("Expliquer pourquoi les trois piliers du développement durable doivent être traités ensemble.",
    "Un projet économiquement rentable mais qui détruit la biodiversité ou précarise les travailleurs n'est pas durable : il déplace le coût vers la société ou vers les générations futures. À l'inverse, une mesure environnementale qui rend un procédé inabordable peut être abandonnée et ne produit aucun effet durable. Les trois piliers sont donc interdépendants : la viabilité économique fournit les moyens, l'équité sociale donne l'acceptabilité et la protection environnementale garantit les ressources. Un arbitrage responsable cherche une solution qui ne sacrifie durablement aucun des trois, en explicitant les compromis et en associant les parties prenantes.",
    "On montre l'interdépendance des piliers et la nécessité d'arbitrages explicites et partagés."),
 QT("Un laboratoire doit choisir entre deux solvants : l'un est efficace et peu coûteux mais très toxique, l'autre est plus cher et plus sûr. Comment raisonner en citoyen responsable ?",
    "On commence par comparer les risques pour la santé des utilisateurs, les risques d'accident, la quantité nécessaire, la toxicité et la filière d'élimination de chaque solvant. Le prix d'achat ne doit pas être le seul critère : le coût réel inclut les EPI, la ventilation, le traitement des déchets et les risques d'exposition. On applique le principe de précaution si les données sur la toxicité sont incomplètes, et le principe du pollueur-payeur en internalisant le coût de traitement. On recherche aussi une solution de substitution ou une réduction des volumes. La décision doit être documentée et discutée collectivement, car elle engage à la fois la sécurité des personnes, la responsabilité de l'établissement et l'impact environnemental.",
    "On intègre coût réel, précaution, déchets et décision collective dans le raisonnement.")],
C("Le développement durable arbitre entre efficacité économique, équité sociale et protection environnementale, avec précaution et responsabilité.",
  "Brundtland 1987 · 3 piliers · 17 ODD · agenda 2030",
  "RSE · pollueur-payeur · précaution · éco-conception · citoyenneté",
  "Developpement durable~Besoins presents et futurs~Brundtland~Rapport 1987~Trois piliers~Economique, social, environnemental~ODD~17 objectifs 2030~RSE~Responsabilite des entreprises~Pollueur-payeur~Cout de la pollution~Precaution~Agir malgre l'incertitude~Eco-conception~Impact des la conception~Tri des dechets~Geste concret",
  "Identifier les trois piliers concernés|Évaluer les risques et les coûts réels|Appliquer précaution et pollueur-payeur|Rechercher des solutions de substitution|Documenter et partager la décision",
  "Réduire le développement durable au seul recyclage|Choisir au seul prix d'achat|Ignorer le coût des déchets|Attendre une certitude scientifique absolue|Décider sans consulter les parties prenantes",
  "1987~Rapport Brundtland~3 piliers~Economie, social, environnement~17 ODD~Agenda 2030~RSE~Responsabilite societale~Tri des solvants~Geste durable",
  "Précaution~Agir face au risque~Pollueur-payeur~Assumer le coût",
  "Développement~Croissance~Développement durable~Viability partagée"))

# FIN_PARTIE_3

valider_et_ecrire(F, "stl-mat-part-C.json")
