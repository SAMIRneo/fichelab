# -*- coding: utf-8 -*-
"""Generateur pro-sante-mat-part-B.json — lot B : sciences et soins (20 fiches).

Biologie et physiologie humaine (8), Sante et soins (7),
Droit et regulation sanitaire et sociale (5).
Chaque fiche : 12 points, 9 questions corrigees (7 QCM + 2 texte),
7 blocs en ordre strict, 3 schemas via diag().
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pro_sante_common import S, R, QC, QT, C, build, valider_et_ecrire

F = []


def add(prefix, titre, mat, ans, points, qcm, txt, c):
    F.append(build(prefix, titre, mat, ans, points, qcm + txt, c))


# ============================================================ BIO1
add("BIO1", "L'organisation du corps humain : cellules, tissus et organes", "Biologie et physiologie humaine", ["2nde pro"],
S("Le corps humain est organise en niveaux emboites : cellules, tissus, organes, systemes et organisme."
  "|La cellule est l'unite de base du vivant : chez l'humain, elle possede une membrane, un cytoplasme et un noyau."
  "|Les tissus sont des ensembles de cellules de meme origine et de meme fonction."
  "|On distingue quatre tissus fondamentaux : epithelial, conjonctif, musculaire et nerveux."
  "|Les tissus epithelials recouvrent les surfaces externes et internes et forment les glandes."
  "|Les tissus conjonctifs assurent le soutien et la liaison : os, cartilage, tendons et sang."
  "|Un organe associe plusieurs tissus pour remplir une fonction precise, comme la peau, le coeur ou le rein."
  "|Un systeme, ou appareil, regroupe des organes qui cooperent : digestif, respiratoire, circulatoire, urinaire."
  "|L'homeostasie designe la capacite de l'organisme a maintenir son milieu interne relativement constant."
  "|La temperature centrale se maintient autour de 37 degres Celsius grace a la thermoregulation."
  "|La glycemie, concentration de glucose dans le sang, est regulée principalement par l'insuline et le glucagon."
  "|Les parametres vitaux traduisent l'homeostasie : temperature, pouls, respiration, pression arterielle et douleur."),
[QC("Quelle est l'unité de base du corps humain ?", "Le tissu~La cellule~L'organe~Le système", 1,
     "La cellule est l'unite structurale et fonctionnelle du vivant."),
 QC("Quel tissu recouvre les surfaces et forme les glandes ?", "Le tissu conjonctif~Le tissu épithélial~Le tissu musculaire~Le tissu nerveux", 1,
     "Les épithéliums tapissent les surfaces et constituent les glandes."),
 QC("Quel est un tissu conjonctif ?", "L'épiderme~Le sang~Le muscle cardiaque~Le nerf", 1,
     "Le sang est un tissu conjonctif liquide, comme l'os ou le cartilage."),
 QC("Quel ensemble d'organes coopèrent pour une fonction commune ?", "Une cellule~Un système~Un tissu~Un organite", 1,
     "Un système ou appareil regroupe des organes qui cooperent."),
 QC("Que désigne l'homéostasie ?", "La croissance cellulaire~Le maintien du milieu interne stable~La digestion~La respiration", 1,
     "L'homeostasie est la stabilite relative du milieu interieur."),
 QC("Quelle est la valeur habituelle de la température centrale ?", "35 °C~37 °C~39 °C~41 °C", 1,
     "La temperature centrale se maintient autour de 37 °C."),
 QC("Quelle hormone fait baisser la glycémie ?", "Le glucagon~L'insuline~L'adrénaline~La thyroxine", 1,
     "L'insuline abaisse la glycemie en favorisant l'entree du glucose dans les cellules.")],
[QT("Expliquer les quatre niveaux d'organisation du corps humain en donnant un exemple à chaque niveau.",
     "Une cellule, par exemple un globule rouge, est l'unite de base. Plusieurs cellules de meme type forment un tissu : les globules rouges appartiennent au tissu sanguin, qui est un conjonctif liquide. Differents tissus s'associent dans un organe : le coeur contient du muscle cardiaque, du tissu conjonctif et des nerfs. Plusieurs organes forment un systeme : le coeur et les vaisseaux constituent le systeme circulatoire, qui transporte le sang dans tout l'organisme. L'organisme entier assure la coordination de tous ces niveaux. Cette hierarchie aide a comprendre qu'une atteinte d'un niveau se repercute sur les niveaux superieurs.",
     "On attend les quatre niveaux, un exemple pour chacun et le lien entre les niveaux."),
 QT("Une personne présente une température de 39,2 °C. Expliquer ce que cela révèle et la conduite à tenir.",
     "Une temperature de 39,2 °C depasse la valeur habituelle de 37 °C : c'est une fievre, qui traduit une reaction de l'organisme a une infection ou a une inflammation. Le corps a releve son point de regulation thermique. Chez une personne agee ou fragile, la fievre peut etre mal toleree et s'accompagner de deshydratation, de confusion ou de chute. La conduite est de prévenir l'infirmier, de mesurer les autres parametres vitaux, de proposer des boissons si la personne peut avaler, de ne pas couvrir excessivement et de surveiller l'evolution. L'aide-soignant n'administre pas d'antipyretique de sa propre initiative : il transmet et applique la prescription. On tracera la mesure et l'heure dans le dossier de suivi.",
     "On attend le lien avec l'homeostasie, les signes associes, la transmission et le respect des competences.")],
C("Le corps est hiérarchisé de la cellule à l'organisme ; l'homéostasie maintient constantes les conditions de vie cellulaire.",
  "cellule → tissu → organe → système → organisme",
  "homéostasie · température centrale ≈ 37 °C · glycémie régulée par insuline et glucagon",
  "Cellule~Unité de base~Membrane et noyau~Tissu~Cellules de même type~Quatre tissus fondamentaux~Organe~Plusieurs tissus~Fonction précise",
  "Repérer le niveau d'organisation~Identifier les tissus en présence~Relier l'organe à sa fonction~Mesurer les paramètres vitaux~Transmettre toute anomalie",
  "Confondre tissu et organe|Oublier que le sang est un tissu|Croire que la température est fixe|Administrer un médicament sans prescription",
  "37 °C~Température centrale~Glucose~Glycémie~Insuline~Hormone qui abaisse~Sang~Tissu conjonctif~Cœur~Organe musculaire",
  "Épithélial~Recouvre les surfaces~Conjonctif~Soutien et liaison",
  "Homeostasie~Milieu interne stable~Dérèglement~Fièvre ou glycémie élevée"))

# ============================================================ BIO2
add("BIO2", "Le squelette et les articulations : anatomie et mobilité", "Biologie et physiologie humaine", ["2nde pro"],
S("Le squelette humain compte environ 206 os chez l'adulte : il assure soutien, protection et mouvement."
  "|Les os sont des tissus conjonctifs mineralises, contenant du collagène et des sels de calcium."
  "|Le squelette se divise en squelette axial — crane, colonne vertebrale, cage thoracique — et squelette appendiculaire — membres."
  "|La colonne vertebrale est formee de vertebres separees par des disques intervertébraux."
  "|Une articulation est une jonction entre deux os : elle peut etre fixe, semi-mobile ou mobile."
  "|Les articulations mobiles sont enveloppees d'une capsule et tapissees d'une membrane synoviale."
  "|Le cartilage articulaire recouvre les extremites osseuses et reduit les frottements."
  "|Les ligaments relient les os entre eux et stabilisent l'articulation."
  "|Les tendons relient les muscles aux os et transmettent la force de contraction."
  "|Les mouvements principaux sont la flexion, l'extension, l'abduction, l'adduction et la rotation."
  "|Avec l'age, la densite osseuse diminue : l'osteoporose augmente le risque de fracture."
  "|Une mobilisation douce et une installation correcte préservent le capital articulaire de la personne accompagnee."),
[QC("Combien d'os compte environ le squelette adulte ?", "106~206~306~406", 1,
     "Le squelette adulte compte environ 206 os ; le nouveau-ne en a davantage."),
 QC("Quel est le rôle des disques intervertébraux ?", "Relier les muscles~Amortir et permettre la flexion de la colonne~Produire du sang~Protéger le crâne", 1,
     "Les disques amortissent les charges et assouplissent la colonne."),
 QC("Qu'est-ce qu'un ligament ?", "Un tissu qui relie un muscle à un os~Un tissu qui relie deux os~Un liquide articulaire~Un type de cartilage", 1,
     "Le ligament unit les os ; le tendon unit le muscle à l'os."),
 QC("Quel mouvement rapproche un membre de l'axe du corps ?", "L'abduction~L'adduction~La rotation~L'extension", 1,
     "L'adduction rapproche, l'abduction éloigne."),
 QC("Quelle membrane tapisse une articulation mobile ?", "La peau~La membrane synoviale~Le péritoine~La plèvre", 1,
     "La membrane synoviale produit le liquide synovial qui lubrifie l'articulation."),
 QC("Que désigne l'ostéoporose ?", "Une inflammation des articulations~Une diminution de la densité osseuse~Une fracture du crâne~Une maladie musculaire", 1,
     "L'osteoporose rend les os plus fragiles et augmente le risque de fracture."),
 QC("Quel geste protège les articulations lors d'un transfert ?", "Tirer brutalement le bras~Accompagner le mouvement sans forcer~Immobiliser complètement le membre~Faire porter le poids sur le cou", 1,
     "Une mobilisation douce et une prise correcte respectent l'amplitude articulaire.")],
[QT("Distinguer un tendon, un ligament et un cartilage, puis expliquer leur rôle dans une articulation.",
     "Le tendon est un cordon de tissu conjonctif qui relie un muscle à un os : il transmet la force de contraction et permet le mouvement. Le ligament relie deux os entre eux : il renforce la capsule articulaire et limite les mouvements excessifs, ce qui stabilise l'articulation. Le cartilage articulaire recouvre les surfaces de contact des os : il est lisse et légèrement élastique, ce qui réduit les frottements et amortit les chocs. Dans une articulation mobile comme le genou, ces trois éléments agissent ensemble : le muscle tire par le tendon, le cartilage protège les surfaces et les ligaments empêchent la luxation.",
     "On attend une définition précise des trois structures et leur rôle complémentaire."),
 QT("Une résidente âgée se plaint de douleurs lombaires lors des transferts. Quels éléments observer et transmettre ?",
     "On observe d'abord la posture et les mouvements : difficulté à se redresser, raideur, boiterie, limitation de l'amplitude. On repère les signes associés : gonflement, rougeur, chaleur, craquements douloureux, ou douleur irradiant dans les jambes. On note le moment d'apparition, le facteur declenchant, l'intensite et la duree de la douleur, ainsi que les gestes qui la soulagent. On verifie l'installation : lit trop haut, fauteuil inadapte, absence d'aide technique. On ne force jamais le mouvement et on prévient l'infirmier pour tout signe inhabituel, notamment en cas de chute ou de fievre. On transmet oralement et par ecrit avec les mots de la personne et l'heure de l'observation.",
     "On attend l'observation des signes, l'analyse de l'installation, l'absence de mobilisation forcée et la transmission.")],
C("Le squelette protège et permet le mouvement ; le bon fonctionnement articulaire repose sur cartilage, ligaments et tendons.",
  "206 os · colonne vertébrale avec disques intervertébraux",
  "ligament = os à os · tendon = muscle à os · cartilage = surface de glissement",
  "Os~Tissu minéralisé~Soutien et protection~Articulation~Jonction entre deux os~Capsule et synoviale~Ligament~Stabilise l'articulation~Tendon~Transmet la force musculaire",
  "Observer la posture~Repérer la zone douloureuse~Vérifier l'installation~Mobiliser sans forcer~Transmettre les observations",
  "Forcer une articulation douloureuse|Confondre tendon et ligament|Oublier d'amortir les transferts|Négliger une douleur persistante",
  "206~Os chez l'adulte~37 °C~Homeostasie~Disque~Amortisseur de la colonne~Synoviale~Liquide lubrifiant~Ostéoporose~Fragilité osseuse",
  "Ligament~Os à os~Stabilité~Tendon~Muscle à os~Mouvement",
  "Flexion~Rapprocher les segments~Extension~Redresser le segment"))

# ============================================================ BIO3
add("BIO3", "Le muscle et le mouvement : physiologie de la contraction", "Biologie et physiologie humaine", ["1re pro"],
S("Les muscles squelettiques sont attaches aux os par des tendons et permettent les mouvements volontaires."
  "|Un muscle est forme de faisceaux de fibres musculaires, elles-memes constituees de myofibrilles."
  "|Les myofibrilles contiennent des filaments d'actine et de myosine, proteines responsables de la contraction."
  "|La contraction résulte d'un raccourcissement des fibres : le muscle se raccourcit, s'epaissit et tire sur l'os."
  "|Un mouvement résulte de l'action de muscles antagonistes : l'un se contracte pendant que l'autre se relache."
  "|Pour la flexion du coude, le biceps se contracte et le triceps se relache."
  "|L'influx nerveux, transmis par un motoneurone, declenche la liberation d'acetylcholine a la jonction neuromusculaire."
  "|L'energie necessaire provient de l'ATP, produit par la respiration cellulaire a partir du glucose et de l'oxygene."
  "|Un effort prolongé consomme davantage d'oxygene et produit du dioxyde de carbone et de l'acide lactique."
  "|La fatigue musculaire se manifeste par une baisse de force et une difficulté a maintenir l'effort."
  "|L'immobilisation prolongée entraine une atrophy musculaire : les fibres diminuent de volume."
  "|Une mobilisation active ou passive, adaptee a la personne, limite cette perte et entretient l'autonomie."),
[QC("Quelles protéines sont responsables de la contraction musculaire ?", "Actine et myosine~Collagène et élastine~Hémoglobine et fer~Insuline et glucagon", 0,
     "Les filaments d'actine et de myosine glissent les uns sur les autres."),
 QC("Que se passe-t-il dans le muscle antagoniste pendant un mouvement ?", "Il se contracte aussi~Il se relâche~Il se déchire~Il devient insensible", 1,
     "Les muscles antagonistes agissent en opposition : l'un se contracte, l'autre se relâche."),
 QC("Quel muscle se contracte lors de la flexion du coude ?", "Le triceps~Le biceps~Le deltoïde~Le quadriceps", 1,
     "Le biceps est flechisseur du coude, le triceps en est l'extenseur."),
 QC("Quel neurotransmetteur agit à la jonction neuromusculaire ?", "La dopamine~L'acétylcholine~La sérotonine~L'adrénaline", 1,
     "L'acetylcholine transmet le signal du nerf au muscle."),
 QC("Quelle molécule fournit l'énergie de la contraction ?", "L'ATP~Le glucose seul~L'eau~Le calcium seul", 0,
     "L'ATP est la source d'energie immediate de la contraction."),
 QC("Qu'est-ce que l'atrophie musculaire ?", "Une augmentation du volume~Une diminution du volume des fibres~Une infection~Une fracture", 1,
     "L'immobilisation prolongée réduit le volume des fibres musculaires."),
 QC("Quel moyen limite l'atrophie chez une personne alitée ?", "L'immobilisation totale~Une mobilisation adaptée~Une sensation de froid~Le silence complet", 1,
     "Une mobilisation active ou passive entretient le muscle.")],
[QT("Expliquer le mécanisme de la contraction musculaire, de l'influx nerveux au mouvement.",
     "Un ordre volontaire prend naissance dans le cortex moteur et descend par la moelle épiniere jusqu'a un motoneurone. L'influx nerveux atteint la jonction neuromusculaire : il provoque la liberation d'acetylcholine, qui se fixe sur le muscle et declenche un potentiel d'action le long de la fibre. Le calcium libere permet aux filaments d'actine et de myosine de glisser les uns sur les autres grace a l'energie de l'ATP. Les myofibrilles se raccourcissent, la fibre se contracte et le muscle tire sur le tendon insere sur l'os. Le muscle antagoniste se relache simultanement, ce qui produit le mouvement. L'energie est renouvelee par la respiration cellulaire du glucose.",
     "On attend la chaine : influx, acetylcholine, actine-myosine, ATP, raccourcissement et antagonisme."),
 QT("Une personne est alitée depuis dix jours après une chute. Expliquer les risques et les actions possibles.",
     "L'immobilisation entraine une atrophy musculaire, surtout au niveau des membres inferieurs, avec une perte de force et de masse. Elle favorise aussi les contractures, les escarres, la thrombose veineuse et la raideur articulaire. Les actions possibles, apres accord de l'equipe soignante, sont des mobilisations passives douces des articulations, des changements de position reguliers, des exercices de respiration et une installation favorisant l'appui. Des aides techniques et un accompagnement progressif vers la verticalisation peuvent etre proposes. On surveille la douleur, la rougeur, la chaleur et la presence d'une zone dure ou gonflee, et on transmet toute anomalie. Le role de l'accompagnant est de maintenir le capital musculaire sans imposer d'effort douloureux.",
     "On attend les risques lies a l'immobilisation et des actions de mobilisation adaptées et supervisees.")],
C("Le mouvement résulte du raccourcissement des fibres musculaires et de l'action coordonnée de muscles antagonistes.",
  "contraction = glissement actine-myosine + ATP",
  "biceps / triceps · acetylcholine · immobilisation = atrophie",
  "Muscle~Faisceaux de fibres~Myofibrilles~Actine et myosine~Filaments contractiles~ATP~Énergie immédiate~Antagoniste~Muscle opposé~Atrophie~Perte de volume",
  "Repérer le muscle concerné~Identifier son antagoniste~Observer l'amplitude du mouvement~Évaluer la force~Mobiliser sans douleur",
  "Confondre tendon et ligament|Forcer un muscle douloureux|Oublier l'antagoniste|Laisser une personne alitée sans mobilisation",
  "Biceps~Fléchisseur du coude~Triceps~Extenseur~Acétylcholine~Jonction neuromusculaire~ATP~Énergie~Immobilisation~Atrophie",
  "Contraction~Raccourcissement~Relâchement~Allongement du muscle opposé",
  "Mobilisation active~La personne agit~Mobilisation passive~Le professionnel aide"))

# ============================================================ BIO4
add("BIO4", "La circulation sanguine et le cœur", "Biologie et physiologie humaine", ["1re pro"],
S("Le systeme circulatoire assure le transport du sang entre le coeur, les poumons et les organes."
  "|Le coeur est un muscle creux, le myocarde, divise en quatre cavités : deux oreillettes et deux ventricules."
  "|Le sang suit deux circuits : la petite circulation vers les poumons et la grande circulation vers les organes."
  "|La petite circulation part du ventricule droit, passe par les arteres pulmonaires et revient au coeur par les veines pulmonaires."
  "|La grande circulation part du ventricule gauche par l'aorte et revient par les veines caves dans l'oreillette droite."
  "|Les arteres transportent le sang sortant du coeur ; les veines le ramènent, les capillaires assurent les echanges."
  "|Les valvules cardiaques empêchent le reflux du sang et imposent un sens de circulation unique."
  "|Un cycle cardiaque comporte une contraction, ou systole, et un relachement, ou diastole."
  "|La frequence cardiaque au repos est d'environ 60 a 100 battements par minute chez l'adulte."
  "|La pression arterielle s'exprime en deux valeurs : la systolique lors de la contraction et la diastolique lors du relachement."
  "|L'hemoglobine des globules rouges fixe l'oxygene dans les poumons et le libere dans les tissus."
  "|La surveillance du pouls, de la tension et de la coloration des teguments fait partie de l'observation de l'etat de la personne."),
[QC("Combien de cavités possède le cœur humain ?", "Deux~Trois~Quatre~Cinq", 2,
     "Le coeur possede deux oreillettes et deux ventricules."),
 QC("Quel vaisseau quitte le ventricule gauche ?", "L'artère pulmonaire~L'aorte~La veine cave~La veine pulmonaire", 1,
     "L'aorte distribue le sang oxygene a la grande circulation."),
 QC("Quel est le rôle des valvules cardiaques ?", "Pomper le sang~Empêcher le reflux~Produire des globules~Réguler la température", 1,
     "Les valvules imposent un sens de circulation unique."),
 QC("Comment appelle-t-on la contraction du cœur ?", "La diastole~La systole~La respiration~La perfusion", 1,
     "La systole est la contraction, la diastole le relachement."),
 QC("Quelle est une fréquence cardiaque de repos normale chez l'adulte ?", "30 battements par minute~70 battements par minute~130 battements par minute~180 battements par minute", 1,
     "La frequence de repos se situe entre 60 et 100 battements par minute."),
 QC("Quelle protéine fixe l'oxygène dans le sang ?", "L'actine~L'hémoglobine~Le collagène~L'insuline", 1,
     "L'hemoglobine des globules rouges transporte l'oxygene."),
 QC("Quel vaisseau assure les échanges avec les tissus ?", "L'aorte~Le capillaire~La veine cave~L'artère pulmonaire", 1,
     "Les capillaires, tres fins, permettent les echanges de gaz et de nutriments.")],
[QT("Décrire le trajet du sang depuis le ventricule droit jusqu'au ventricule gauche.",
     "Le sang pauvre en oxygene est ejecte du ventricule droit vers les arteres pulmonaires, qui le conduisent aux poumons. Dans les capillaires pulmonaires, il libere le dioxyde de carbone et fixe l'oxygene grace a l'hemoglobine. Le sang oxygene revient par les veines pulmonaires dans l'oreillette gauche, puis passe dans le ventricule gauche. Celui-ci le propulse dans l'aorte vers la grande circulation : les arteres, puis les capillaires des organes, ou l'oxygene est libere et le dioxyde de carbone recueilli. Le sang revient alors par les veines caves a l'oreillette droite, puis au ventricule droit. Ce trajet forme une boucle continue en deux etapes.",
     "On attend les quatre cavités, les deux circuits et le role des poumons et des capillaires."),
 QT("Comment mesurer et interpréter le pouls d'une personne accompagnée ?",
     "On choisit un site accessible, le plus souvent le poignet ou le cou, et on utilise l'index et le majeur, jamais le pouce qui a son propre pouls. On compte les battements pendant une minute, ou pendant trente secondes en doublant le resultat, avec une montre. On note la frequence, le rythme — regulier ou irregulier — et la force du pouls, ainsi que l'heure et la position de la personne. Une frequence hors de 60 a 100 battements par minute au repos, un pouls tres faible ou irregulier doit etre signalé a l'infirmier. On observe egalement la coloration des levres et des doigts, la presence d'un essoufflement ou d'une douleur thoracique. On transmet les chiffres exacts plutot qu'une appreciation vague.",
     "On attend la technique de mesure, les critères de normalite et la transmission precise.")],
C("Le cœur est une pompe à quatre cavités qui fait circuler le sang en deux boucles ; le pouls et la tension traduisent son fonctionnement.",
  "petite circulation : cœur droit → poumons → cœur gauche",
  "grande circulation : ventricule gauche → aorte → organes → veines caves",
  "Cœur~Myocarde et quatre cavités~Artère~Sang sortant du cœur~Veine~Sang revenant au cœur~Capillaire~Échanges gazeux~Systole~Contraction cardiaque",
  "Mesurer le pouls~Observer le rythme~Mesurer la tension~Regarder la coloration~Transmettre les valeurs",
  "Confondre artère et veine|Employer le pouce pour prendre le pouls|Oublier l'heure de la mesure|Ignorer un pouls irrégulier",
  "60 à 100~Battements par minute~120/80~Pression artérielle usuelle~Hémoglobine~Transport de l'oxygène~Aorte~Grande circulation~Systole~Contraction",
  "Petite circulation~Vers les poumons~Grande circulation~Vers les organes",
  "Systole~Contraction~Diastole~Relâchement"))

# ============================================================ BIO5
add("BIO5", "La respiration et les échanges gazeux", "Biologie et physiologie humaine", ["1re pro"],
S("La respiration assure l'apport d'oxygene aux cellules et l'elimination du dioxyde de carbone."
  "|On distingue la ventilation pulmonaire, mouvement de l'air, et la respiration cellulaire, production d'energie."
  "|L'air entre par les voies respiratoires : nez, pharynx, larynx, trachee, bronches et bronchioles."
  "|Les poumons contiennent des alveoles, petits sacs ou ont lieu les echanges gazeux."
  "|La paroi des alveoles est tres fine et entouree de capillaires : l'oxygene passe dans le sang, le dioxyde de carbone en sort."
  "|Le diaphragme et les muscles intercostaux commandent l'inspiration et l'expiration."
  "|A l'inspiration, le diaphragme s'abaisse et la cage thoracique se dilate : l'air entre."
  "|A l'expiration, le diaphragme remonte et l'air sort passivement au repos."
  "|La frequence respiratoire au repos est d'environ 12 a 20 mouvements par minute chez l'adulte."
  "|La respiration cellulaire consomme du glucose et de l'oxygene pour produire de l'ATP, de l'eau et du dioxyde de carbone."
  "|Une dyspnee designe une difficulté respiratoire ; une hypoxie correspond a un manque d'oxygene."
  "|Observer la frequence, l'amplitude et les signes associes permet de détecter une détresse respiratoire."),
[QC("Où ont lieu les échanges gazeux ?", "Dans la trachée~Dans les alvéoles pulmonaires~Dans le larynx~Dans les bronches", 1,
     "Les alvéoles, entourées de capillaires, sont le lieu des échanges."),
 QC("Quel muscle principal commande l'inspiration ?", "Le biceps~Le diaphragme~Le triceps~Le quadriceps", 1,
     "Le diaphragme s'abaisse a l'inspiration et remonte a l'expiration."),
 QC("Que passe-t-il à l'inspiration ?", "Le diaphragme remonte~Le diaphragme s'abaisse et l'air entre~La cage se resserre~L'air sort", 1,
     "L'abaissement du diaphragme augmente le volume thoracique et fait entrer l'air."),
 QC("Quelle est une fréquence respiratoire normale au repos ?", "5 par minute~16 par minute~35 par minute~60 par minute", 1,
     "La frequence respiratoire de repos se situe entre 12 et 20 par minute."),
 QC("Qu'est-ce qu'une dyspnée ?", "Une respiration trop lente~Une difficulté respiratoire~Une toux grasse~Une douleur thoracique", 1,
     "La dyspnee est une sensation de difficulté a respirer."),
 QC("Quel gaz est consommé par la respiration cellulaire ?", "Le dioxyde de carbone~L'oxygène~L'azote~La vapeur d'eau", 1,
     "La cellule consomme de l'oxygene et du glucose pour produire de l'ATP."),
 QC("Quel signe évoque une détresse respiratoire ?", "Un teint rose~Des lèvres bleutées et un essoufflement~Une voix claire~Un sommeil calme", 1,
     "La cyanose des levres et l'essoufflement sont des signes d'alarme.")],
[QT("Expliquer la différence entre ventilation pulmonaire et respiration cellulaire.",
     "La ventilation pulmonaire est un mecanisme mecanique : elle fait entrer et sortir l'air des poumons grace au diaphragme et aux muscles intercostaux. Elle amene l'oxygene jusqu'aux alvéoles et elimine le dioxyde de carbone. La respiration cellulaire est un processus biochimique qui a lieu dans les cellules : elle utilise l'oxygene apporte par le sang et le glucose pour produire de l'ATP, de l'eau et du dioxyde de carbone. La ventilation est donc au service de la respiration cellulaire : sans elle, l'oxygene ne parviendrait pas aux cellules et l'ATP ne pourrait etre produit. Ces deux processus sont relies par le sang et l'hemoglobine.",
     "On attend l'opposition mecanique / biochimique et le role du sang comme intermédiaire."),
 QT("Une personne présente une respiration rapide, superficielle et des lèvres bleutées. Que faire ?",
     "Ces signes evoquent une hypoxie et une detresse respiratoire : la frequence est elevee, l'amplitude faible et la cyanose traduit un manque d'oxygene dans le sang. Il faut alerter immediatement l'infirmier ou le medecin, ne pas laisser la personne seule, l'installer en position assuree, par exemple demi-assise si sa pathologie le permet, et degager les voies respiratoires sans forcer. On vérifie que rien n'obstrue la bouche ou le nez, on note l'heure, la frequence et les signes observes, et on rassure la personne en parlant calmement. On n'administre jamais d'oxygene sans prescription et on n'impose pas de position qui accentue la gêne. On transmet les parametres mesures des que possible.",
     "On attend la reconnaissance de l'urgence, l'alerte, l'installation, la surveillance et le respect des competences.")],
C("La respiration relie l'air, le sang et les cellules : la ventilation apporte l'oxygène, la respiration cellulaire le consomme.",
  "ventilation pulmonaire ≠ respiration cellulaire",
  "alvéoles + capillaires · 12 à 20 mouvements/min · dyspnée et hypoxie",
  "Alvéole~Sac d'échange~Capillaire~Réseau de poumons~Diaphragme~Muscle respiratoire~Inspiration~Entrée d'air~Ventilation~Mécanique respiratoire",
  "Observer la fréquence~Apprécier l'amplitude~Repérer la cyanose~Installer la personne~Alerter et transmettre",
  "Confondre ventilation et respiration cellulaire|Ignorer des lèvres bleutées|Administrer de l'oxygène sans prescription|Compter sur trente secondes sans multiplier",
  "12 à 20~Mouvements par minute~Diaphragme~Inspiration~ATP~Énergie cellulaire~Cyanose~Lèvres bleutées~Dyspnée~Gêne respiratoire",
  "Ventilation~Mouvement de l'air~Respiration cellulaire~Production d'ATP",
  "Inspiration~Air entre~Expiration~Air sort"))

# ============================================================ BIO6
add("BIO6", "La digestion et les besoins nutritionnels", "Biologie et physiologie humaine", ["1re pro"],
S("La digestion transforme les aliments en nutriments absorbables par l'intestin."
  "|Elle debute dans la bouche par la mastication et l'action de la salive, puis se poursuit dans l'estomac et l'intestin grele."
  "|Les enzymes digestives decoupent les glucides, les lipides et les proteines en molecules plus simples."
  "|L'estomac malaxe le bol alimentaire et le melange au suc gastrique acide."
  "|Le foie produit la bile, qui facilite la digestion des graisses ; le pancreas secre des enzymes."
  "|L'intestin grele absorbe les nutriments grace aux villosites ; l'eau est absorbee principalement dans le colon."
  "|Les besoins energetiques dependent de l'age, de l'activite physique et de l'etat de sante."
  "|Les macronutriments sont les glucides, les lipides et les proteines ; les micronutriments sont les vitamines et les mineraux."
  "|Une alimentation equilibree associe feculents, legumes, fruits, produits laitiers, proteines et matieres grasses."
  "|Les proteines sont necessaires au renouvellement des tissus, en particulier chez la personne agee."
  "|Une deshydratation peut survenir rapidement chez une personne qui ne percoit plus la soif."
  "|L'accompagnement du repas favorise l'hydratation, verifie la texture proposee et respecte les preferences."),
[QC("Où commence la digestion ?", "Dans l'estomac~Dans la bouche~Dans l'intestin~Dans le foie", 1,
     "La mastication et la salive initient la digestion dans la bouche."),
 QC("Quel organe produit la bile ?", "Le pancreas~Le foie~L'estomac~Le rein", 1,
     "Le foie produit la bile, necessaire a la digestion des lipides."),
 QC("Quel est le rôle des villosités intestinales ?", "Produire de la salive~Augmenter la surface d'absorption~Stocker la bile~Mastiquer", 1,
     "Les villosites augmentent considerablement la surface d'absorption des nutriments."),
 QC("Quels sont les macronutriments ?", "Vitamines, minéraux et eau~Glucides, lipides et protéines~Fer, calcium et iode~Salive et bile", 1,
     "Les macronutriments apportent l'energie et les materiaux de construction."),
 QC("Quel liquide est principalement absorbé dans le côlon ?", "La bile~L'eau~Le suc gastrique~La salive", 1,
     "Le colon reabsorbe l'eau et forme les selles."),
 QC("Quel risque est fréquent chez une personne âgée qui ne boit pas ?", "Une hypoglycémie~Une déshydratation~Une constipation~Une ostéoporose", 1,
     "La diminution de la sensation de soif expose a la deshydratation."),
 QC("Que faut-il vérifier avant de servir un repas à une personne dysphagique ?", "La couleur de l'assiette~La texture adaptée et la position~Le prix du repas~L'heure de la vaisselle", 1,
     "La texture et la position sont essentielles pour prevenir les fausses routes.")],
[QT("Expliquer le parcours des aliments dans le tube digestif et le rôle des principaux organes.",
     "Les aliments sont mastiques dans la bouche et melanges a la salive, qui contient une amylase. Le bol alimentaire descend par l'oesophage jusqu'a l'estomac, ou il est malaxe et melange au suc gastrique acide. Il passe ensuite dans le duodenum, ou la bile du foie et les enzymes du pancreas agissent sur les graisses, les glucides et les proteines. Dans l'intestin grele, les villosites absorbent les nutriments vers le sang et la lymphe. Le residu arrive dans le colon, ou l'eau est reabsorbee, puis est eliminé par le rectum. Chaque etape transforme progressivement le repas en elements utilisables par les cellules.",
     "On attend la successive bouche, oesophage, estomac, intestin grele, colon, et le role du foie et du pancreas."),
 QT("Comment accompagner le repas d'une résidente qui mange lentement et boit peu ?",
     "On installe la personne confortablement, le dos droit et les pieds appuyés, pour faciliter la deglutition et limiter les fausses routes. On respecte son rythme sans la presser : on peut fractionner le repas et proposer de petites bouchées. On propose des boissons a intervalles reguliers, en adaptant la texture si elle a des difficultes a avaler, et on note la quantite réellement bue. On observe les signes de fatigue, de toux pendant le repas ou de refus, et on les transmet. On favorise un moment convivial, avec peu de bruit et une conversation calme, car l'appetit depend aussi du cadre. On ne force jamais a manger et on consigne les apports dans le dossier de suivi pour que l'equipe adapte les portions.",
     "On attend installation, respect du rythme, hydration, observation et traçabilité des apports.")],
C("La digestion transforme les aliments en nutriments ; l'accompagnement du repas protège la nutrition et l'hydratation.",
  "bouche → estomac → intestin grêle → côlon",
  "glucides, lipides, protéines · vitamines et minéraux · eau",
  "Bouche~Mastication et salive~Estomac~Malaxage acide~Intestin grêle~Absorption des nutriments~Foie~Production de bile~Villosités~Surface d'échange",
  "Installer la personne~Vérifier la texture~Respecter le rythme~Proposer à boire~Tracer les apports",
  "Forcer à manger|Presser une personne qui tousse|Oublier de noter les boissons|Ignorer une plainte de soif",
  "Salive~Amylase~Bile~Digestion des graisses~Villosités~Absorption~Eau~Hydratation~Protéines~Renouvellement des tissus",
  "Macronutriments~Énergie et construction~Micronutriments~Vitamines et minéraux",
  "Digestion~Transformation des aliments~Absorption~Passage dans le sang"))

# ============================================================ BIO7
add("BIO7", "Le système nerveux et la perception", "Biologie et physiologie humaine", ["Terminale pro"],
S("Le systeme nerveux assure la reception des informations, leur traitement et l'elaboration d'une reponse."
  "|Il se divise en systeme nerveux central, cerveau et moelle epiniere, et systeme nerveux peripherique, les nerfs."
  "|Le neurone est l'unite fonctionnelle : il possede un corps cellulaire, des dendrites et un axone."
  "|L'influx nerveux se propage le long de l'axone grace a des echanges ioniques et a la gaine de myeline."
  "|Une synapse permet la transmission de l'information entre deux neurones par un neurotransmetteur."
  "|Les recepteurs sensoriels convertissent un stimulus en signal nerveux : vue, ouie, toucher, gout, odorat."
  "|Les informations sensorielles remontent a la moelle puis au cerveau, ou elles sont interpretees."
  "|La reponse motrice part du cerveau, descend par la moelle et atteint le muscle par un motoneurone."
  "|Le cervelet coordonne les mouvements et l'equilibre ; le tronc cerebral regule des fonctions automatiques."
  "|Le systeme nerveux autonome regule la frequence cardiaque, la digestion et la transpiration sans controle volontaire."
  "|La douleur est une perception complexe, influençee par l'attention, l'emotion et le contexte."
  "|L'observation des reactions d'une personne et l'ecoute de sa plainte sont essentielles pour apprecier sa douleur."),
[QC("Quelle est l'unité fonctionnelle du système nerveux ?", "Le muscle~Le neurone~L'os~Le globule rouge", 1,
     "Le neurone recoit, traite et transmet l'information nerveuse."),
 QC("Quel rôle joue la gaine de myéline ?", "Protéger l'os~Accélérer la propagation de l'influx~Produire du sang~Digérer le glucose", 1,
     "La myeline isole l'axone et accelere la conduction de l'influx."),
 QC("Qu'est-ce qu'une synapse ?", "Une cellule musculaire~La jonction entre deux neurones~Un récepteur cutané~Une partie du cervelet", 1,
     "La synapse permet le passage de l'information d'un neurone a l'autre."),
 QC("Quelle partie du cerveau coordonne l'équilibre ?", "Le cervelet~L'hippocampe~Le lobe frontal~La moelle", 0,
     "Le cervelet assure la coordination des mouvements et l'equilibre."),
 QC("Quel système règle la digestion sans volonté ?", "Le système nerveux autonome~Le système musculaire~Le système squelettique~Le système immunitaire", 0,
     "Le systeme nerveux autonome commande les fonctions automatiques."),
 QC("Que convertit un récepteur sensoriel ?", "Un muscle en os~Un stimulus en signal nerveux~Un nutriment en énergie~Un nerf en hormone", 1,
     "Les recepteurs transduisent le stimulus en influx nerveux."),
 QC("Pourquoi la douleur est-elle complexe ?", "Elle dépend uniquement de la blessure~Elle est influencée par l'attention et l'émotion~Elle n'existe pas chez les personnes âgées~Elle est toujours visible", 1,
     "La perception de la douleur est modulee par de nombreux facteurs.")],
[QT("Décrire le trajet d'une information sensorielle puis d'une réponse motrice.",
     "Un recepteur, par exemple dans la peau, detecte un stimulus et le convertit en influx nerveux. Cet influx remonte par un nerf sensitif vers la moelle epiniere, puis vers le cerveau ou l'information est analysee et reconnue. Si une reponse est necessaire, le cortex moteur élabore un ordre qui descend par la moelle et emprunte un motoneurone. L'influx atteint la jonction neuromusculaire, libere de l'acetylcholine et provoque la contraction du muscle. Le cervelet ajuste en continu le mouvement et l'equilibre. Ce circuit illustre la boucle sensori-motrice : recevoir, traiter, decider, agir.",
     "On attend recepteur, nerf sensitif, moelle, cerveau, motoneurone et muscle, avec le role du cervelet."),
 QT("Une personne atteinte de démence exprime une douleur par agitation plutôt que par des mots. Comment l'analyser ?",
     "L'agitation peut etre un mode d'expression de la douleur quand le langage est altere. On recherche les causes possibles : douleur physique, besoin non satisfait, peur, surstimulation, fatigue, ou effet d'un medicament. On observe les signes comportementaux : grimaces, protection d'une zone du corps, refus de mobilisation, troubles du sommeil, et on utilise une grille d'evaluation de la douleur adaptee si elle existe dans l'etablissement. On verifie les elements objectifs : chute recente, constipation, infection urinaire, escarre, position inconfortable. On ne suppose pas que la personne « ne sent rien ». On transmet rapidement a l'infirmier les observations datees et les modifications de comportement, afin qu'une evaluation et une prise en charge soient engagees.",
     "On attend l'agitation comme signe, la recherche de causes, l'usage d'outils adaptes et la transmission.")],
C("Le système nerveux transforme un stimulus en perception puis en action ; la douleur reste une expérience subjective à écouter.",
  "récepteur → nerf sensitif → moelle → cerveau → motoneurone → muscle",
  "neurone · myéline · synapse · cervelet · système autonome",
  "Neurone~Corps et axone~Myéline~Conduction rapide~Synapse~Transmission entre neurones~Récepteur~Conversion du stimulus~Cervelet~Coordination et équilibre",
  "Observer le comportement~Identifier le stimulus possible~Utiliser une grille adaptée~Rechercher une cause organique~Transmettre sans attendre",
  "Ignorer une douleur silencieuse|Croitre que l'agitation est sans cause|Confondre cerveau et cervelet|Remplacer l'évaluation par une supposition",
  "Acétylcholine~Jonction neuromusculaire~Myéline~Vitesse de conduction~Cervelet~Équilibre~Autonome~Fonctions automatiques~Douleur~Perception subjective",
  "Système central~Cerveau et moelle~Système périphérique~Nerfs",
  "Sensoriel~Vers le cerveau~Moteur~Vers le muscle"))

# ============================================================ BIO8
add("BIO8", "Le vieillissement et ses conséquences fonctionnelles", "Biologie et physiologie humaine", ["Terminale pro"],
S("Le vieillissement est un processus progressif qui modifie les structures et les fonctions de l'organisme."
  "|Il ne se ressume pas a la maladie : il s'accompagne de changements physiologiques normaux et variables selon les personnes."
  "|La masse musculaire diminue, entrainant une perte de force et de capacite de marche."
  "|La densite osseuse baisse, notamment chez les femmes apres la ménopause, avec un risque d'osteoporose."
  "|Les articulations deviennent moins souples et le cartilage s'use progressivement."
  "|La capacite respiratoire diminue et l'effort devient plus difficile a soutenir."
  "|Le coeur s'adapte moins bien a l'effort et la regulation de la pression arterielle peut devenir moins souple."
  "|Les reins filtrent moins efficacement : la deshydratation et les erreurs de dosage sont plus frequentes."
  "|La vue, l'ouie et la perception du gout s'attenuent, ce qui modifie la communication et l'alimentation."
  "|La memoire et la vitesse de traitement ralentissent, sans confondre ces changements avec une démence."
  "|La baisse de la sensation de soif et de faim expose a la desnutrition et a la deshydratation."
  "|L'accompagnement vise a compenser ces changements, preserver l'autonomie et respecter le projet de la personne."),
[QC("Quel changement musculaire est lié au vieillissement ?", "Une augmentation de masse~Une diminution de masse et de force~Une disparition des tendons~Un allongement des os", 1,
     "La sarcopenie correspond a la perte de masse et de force musculaire."),
 QC("Qu'est-ce que l'ostéoporose ?", "Une souplesse accrue des os~Une diminution de densité osseuse~Une maladie du muscle~Une inflammation des nerfs", 1,
     "La baisse de densite rend les os plus fragiles."),
 QC("Quel organe filtre moins bien avec l'âge ?", "Le foie~Le rein~La peau~L'estomac", 1,
     "La fonction renale diminue progressivement."),
 QC("Pourquoi la déshydratation est-elle fréquente chez une personne âgée ?", "Elle boit trop~La sensation de soif diminue~Elle transpire davantage~Ses reins produisent plus d'urine concentrée", 1,
     "La diminution de la perception de la soif est un facteur majeur."),
 QC("Quel changement sensoriel peut modifier l'alimentation ?", "Une audition accrue~Une baisse du goût et de l'odorat~Une vue plus nette~Un toucher plus fin", 1,
     "L'attenuation du gout et de l'odorat reduit le plaisir de manger."),
 QC("Faut-il confondre ralentissement de la mémoire et démence ?", "Oui, toujours~Non, ce sont des situations différentes~Uniquement après 80 ans~Seulement en institution", 1,
     "Le ralentissement normal n'est pas une maladie neurocognitive."),
 QC("Quel est l'objectif de l'accompagnement du vieillissement ?", "Ralentir le temps~Préserver l'autonomie et compenser les changements~Supprimer toutes les aides~Imposer le repos total", 1,
     "L'accompagnement vise le maintien de l'autonomie et la qualite de vie.")],
[QT("Expliquer la différence entre vieillissement normal et pathologie, avec deux exemples.",
     "Le vieillissement normal est une evolution physiologique progressive et commune, meme si son rythme varie : la masse musculaire diminue, la vue s'attenue, la marche devient un peu plus lente. La pathologie est une maladie qui survient en plus et qui necessite une evaluation et un traitement : une pneumopathie, une fracture du col du femur ou une maladie neurocognitive. La frontiere n'est pas toujours nette : un ralentissement de la memoire est normal, alors qu'une desorientation persistante et une perte d'autonomie rapide sont pathologiques. Pour l'accompagnant, la distinction est cruciale : il ne doit ni medicaliser un changement normal, ni banaliser un signe d'alarme. Son role est d'observer, de transmettre et de laisser le diagnostic au medecin.",
     "On attend deux exemples de chaque cote et la consequence pour la posture professionnelle."),
 QT("Proposer des adaptations pour une personne âgée qui présente une baisse de la vue et de la force musculaire.",
     "Pour la vue, on ameliore l'eclairage sans eblouissement, on contraste les elements importants, on utilise des lunettes adaptees et on garde les objets a leur place habituelle. Pour la force musculaire, on prévoit des aides techniques : fauteuil adapté, barres d'appui, lève-personne ou drap de glissement selon la situation, et on fractionne l'effort en etapes. On privilégie les deplacements accompagnes plutot que le port de charges. On organise les repas avec des couverts legers et une vaisselle contrastee. On demande toujours a la personne ce qu'elle prefere et on verifie que l'aide ne la remplace pas inutilement. On reevalue régulierement les besoins avec l'equipe pour ajuster les adaptations et eviter la perte d'autonomie.",
     "On attend des adaptations environnementales, des aides techniques et le respect du projet de la personne.")],
C("Le vieillissement modifie progressivement les capacités ; l'accompagnement compense sans se substituer à la personne.",
  "sarcopenie · ostéoporose · baisse de la fonction rénale",
  "soif et appétit atténués · ralentissement cognitif ≠ démence",
  "Sarcopénie~Perte de muscle~Ostéoporose~Fragilité osseuse~Rein~Filtration réduite~Sensoriel~Vue et ouïe~Soif~Sensation diminuée",
  "Observer les changements~Distinguer normal et pathologique~Aménager l'environnement~Proposer des aides adaptées~Réévaluer régulièrement",
  "Médicaliser un changement normal|Ignorer un signe d'alarme|Imposer le repos total|Remplacer la personne au lieu de l'aider",
  "Sarcopénie~Force réduite~Gout~Perception atténuée~Déshydratation~Risque fréquent~Lunettes~Aide visuelle~Barre d'appui~Aide technique",
  "Vieillissement normal~Évolution physiologique~Pathologie~Maladie à traiter",
  "Compensation~Adapter l'environnement~Substitution~Faire à la place"))

# ============================================================ SOIN1
add("SOIN1", "Les soins d'hygiène et de confort : principes et gestes", "Santé et soins", ["2nde pro"],
S("Les soins d'hygiène et de confort visent à maintenir la propreté, le bien-être et la sécurité de la personne."
  "|Ils comprennent la toilette, l'habillage, les soins de la bouche, des cheveux et des ongles, ainsi que les changements de position."
  "|Le confort associe la propreté, l'absence de douleur, une installation adaptée et un environnement calme."
  "|Avant tout soin, on explique le geste a la personne et on demande son accord."
  "|La pudeur et l'intimité sont préservées par un dressing approprié et une porte fermée."
  "|Le lavage des mains précède et suit chaque soin, avec une friction hydro-alcoolique ou un lavage savonneux."
  "|Les gants sont changés entre deux personnes et entre deux gestes sales et propres."
  "|La température de l'eau est vérifiée au thermomètre ou au coude, jamais à la main seule."
  "|Les gestes sont doux, continus et effectués de haut en bas pour respecter la circulation veineuse."
  "|Une peau rouge, une plaie, une douleur ou une odeur inhabituelle doivent etre signalées."
  "|Le material de toilette est personnel et ne doit pas etre partage entre residents."
  "|Chaque soin est trace dans le dossier ou le cahier de suivi avec l'heure et les observations."),
[QC("Que faut-il faire avant un soin d'hygiène ?", "Commencer immédiatement~Expliquer le geste et demander l'accord~Fermer les yeux de la personne~Appeler toute l'équipe", 1,
     "L'information et le consentement precedent le geste."),
 QC("Comment préserver l'intimité pendant la toilette ?", "Laisser la porte ouverte~Utiliser un dressing et fermer la porte~Parler à voix haute~Inviter les autres résidents", 1,
     "Le dressing et la porte fermée protegent la pudeur."),
 QC("Quand faut-il se laver les mains ?", "Une fois par jour~Avant et après chaque soin~Seulement après le repas~Uniquement en cas de souillure", 1,
     "La friction des mains est requise avant et apres chaque soin."),
 QC("Comment vérifier la température de l'eau ?", "Avec la paume de la main~Avec un thermomètre ou le coude~En la goûtant~Avec le dos de la main seulement", 1,
     "Le thermomètre ou le coude permet un controle fiable et hygiénique."),
 QC("Dans quel sens effectue-t-on les gestes de toilette ?", "De bas en haut~De haut en bas~En cercle~Au hasard", 1,
     "Les gestes vont de haut en bas pour respecter la circulation et la propreté."),
 QC("Que faire devant une rougeur persistante ?", "L'ignorer~La signaler à l'infirmier~La recouvrir de poudre~La masser fortement", 1,
     "Toute anomalie cutanee doit etre transmise."),
 QC("Quel matériel doit rester personnel ?", "Le savon du service~Le matériel de toilette de la personne~Les gants de l'équipe~Les draps propres", 1,
     "Le matériel de toilette est individuel pour eviter les contaminations.")],
[QT("Décrire les étapes d'une toilette au lit en respectant la sécurité et la pudeur.",
     "On prépare d'abord le matériel et on vérifie la température de la chambre et de l'eau. On explique le soin à la personne, on obtient son accord et on ferme la porte en installant un dressing. On se lave les mains, on enfile les gants si nécessaire et on dégage les vêtements en gardant une couverture sur les parties non lavées. On commence par le visage, puis le cou, les bras, le thorax, l'abdomen, les jambes et le dos, en changeant l'eau et le linge quand c'est nécessaire. Les gestes sont doux et de haut en bas. On termine par l'habillage, l'installation confortable et la vérification de la peau. On retire les gants, on se lave les mains et on trace le soin avec les observations éventuelles.",
     "On attend préparation, consentement, pudeur, ordre des gestes, hygiène des mains et traçabilité."),
 QT("Une personne refuse le soin d'hygiène. Comment adapter votre pratique ?",
     "On s'arrete immediatement et on demande pourquoi, en utilisant une ecoute calme et des questions ouvertes. Le refus peut exprimer une peur, une douleur, une fatigue, un sentiment d'humiliation ou un desaccord sur l'horaire. On propose de reporter le soin, de le faire en deux temps ou de changer de professionnel si la personne le souhaite. On adapte la maniere : expliquer chaque etape, garder les vetements autant que possible, laisser la personne faire elle-meme ce qu'elle peut. On ne force jamais et on ne punit pas le refus. On transmet l'information a l'equipe et on note les preferences dans le projet individualise. Si le refus se prolonge et entraine un risque pour la sante, l'infirmier ou le medecin est informe pour rechercher une cause, notamment une douleur ou une depression.",
     "On attend arret du geste, recherche des motifs, alternatives, transmission et respect du refus.")],
C("Un soin d'hygiène est un geste technique et relationnel : expliquer, préserver l'intimité, observer et transmettre.",
  "mains lavées avant et après · gants changés entre deux personnes",
  "gestes de haut en bas · eau vérifiée · pudeur et consentement",
  "Toilette~Soin d'hygiène~Consentement~Accord de la personne~Pudeur~Dressing et porte fermée~Eau~Température vérifiée~Observation~Rougeur et douleur",
  "Préparer le matériel~Expliquer le soin~Installer et préserver la pudeur~Réaliser les gestes~Tracer et transmettre",
  "Forcer un soin refusé|Partager le matériel personnel|Oublier de vérifier l'eau|Négliger une rougeur",
  "Gants~Changement entre deux personnes~Eau~Contrôle au coude~Dressing~Respect de l'intimité~Dossier~Trace du soin~Visage~Première zone lavée",
  "Hygiène~Propreté et prévention~Confort~Bien-être et installation",
  "Soin technique~Geste appris~Soin relationnel~Communication et respect"))

# ============================================================ SOIN2
add("SOIN2", "L'hygiène des mains et la prévention des infections", "Santé et soins", ["2nde pro"],
S("L'hygiène des mains est le geste le plus efficace pour prévenir la transmission des micro-organismes."
  "|Les mains peuvent transporter des bacteries, des virus et des champignons provenant de l'environnement ou des personnes."
  "|Une infection associee aux soins est une infection contractee lors d'une prise en charge medicale."
  "|Les micro-organismes se transmettent par contact direct, par les mains, par l'air, par l'eau ou par le matériel."
  "|Le lavage des mains a l'eau et au savon dure au moins trente secondes et suit sept etapes."
  "|La friction hydro-alcoolique dure vingt a trente secondes et recouvre toute la surface des mains."
  "|La solution hydro-alcoolique doit etre appliquee sur des mains visuellement propres et seches."
  "|Les moments de l'hygiene des mains sont : avant un contact, avant un geste aseptique, apres un geste sale et apres un contact."
  "|Le port de gants ne remplace jamais la friction des mains : les gants peuvent etre contaminés et sont changés entre deux actes."
  "|Les bijoux, montres et ongles longs favorisent la retention des micro-organismes."
  "|Les surfaces et le matériel sont nettoyes et desinfectes selon le protocole de bionettoyage."
  "|Une main douloureuse, une plaque rouge ou une fievre apres un soin doit etre signalee rapidement."),
[QC("Quelle est la durée d'un lavage des mains au savon ?", "5 secondes~Au moins 30 secondes~2 minutes~10 minutes", 1,
     "Le lavage au savon dure au moins trente secondes, suivi d'un sechage."),
 QC("Quand utiliser une solution hydro-alcoolique ?", "Sur des mains souillées~Sur des mains visuellement propres et sèches~Après chaque repas seulement~Jamais", 1,
     "La friction hydro-alcoolique necessite des mains visuellement propres."),
 QC("Le port de gants remplace-t-il la friction des mains ?", "Oui, toujours~Non, jamais~Oui pour les soins simples~Seulement la nuit", 1,
     "Les gants complètent mais ne remplacent pas l'hygiène des mains."),
 QC("Quand faut-il changer les gants ?", "Toutes les heures~Entre deux personnes ou deux gestes~Jamais~Une fois par jour", 1,
     "Les gants sont changés entre deux personnes et entre un geste sale et un geste propre."),
 QC("Qu'est-ce qu'une infection associée aux soins ?", "Une infection saisonnière~Une infection contractée lors d'une prise en charge~Une allergie~Une simple rougeur", 1,
     "Ces infections sont aussi appelees infections nosocomiales."),
 QC("Quel élément favorise la rétention des micro-organismes ?", "Des mains sèches~Une montre et des ongles longs~Des gants neufs~Une friction correcte", 1,
     "Bijoux, montres et ongles longs sont des reservoirs potentiels."),
 QC("Quel signe doit alerter après un soin ?", "Une main froide~Une plaque rouge ou une fièvre~Une peau sèche~Une odeur de savon", 1,
     "Rougeur, douleur et fièvre peuvent signaler une infection débutante.")],
[QT("Décrire la technique de friction hydro-alcoolique et expliquer pourquoi elle est préférée au lavage simple dans de nombreux cas.",
     "On verse une dose de solution hydro-alcoolique dans la paume de la main, puis on frotte paume contre paume, le dos des mains, les espaces entre les doigts, les pulpes des doigts, les pouces et les poignets, jusqu'a ce que la peau soit seche, pendant vingt a trente secondes. Les mains doivent etre visuellement propres et seches. La friction est plus rapide, plus accessible au moment du soin et plus efficace sur de nombreux micro-organismes que le simple lavage a l'eau. Elle respecte aussi mieux la peau lorsque le lavage est tres frequemment repeté. Le lavage au savon reste indispensable quand les mains sont souillees ou apres un contact avec des liquides biologiques. Dans tous les cas, le geste est realise avant et apres le contact avec la personne.",
     "On attend les étapes, la durée, les conditions d'usage et le complémentarité avec le lavage."),
 QT("Dans une chambre, vous avez réalisé une toilette puis changé un pansement. Analyser les risques de transmission et les mesures à prendre.",
     "La toilette est un geste sale au sens de la hygiene : les mains ont pu etre contaminées par la peau, les secretions ou le linge. Le changement de pansement est un geste aseptique : il exige des mains propres et des gants adaptes. Entre les deux, il faut impérativement changer de gants et realiser une friction hydro-alcoolique, car le même gant ne peut pas passer d'une zone contaminée a une plaie. On retire les gants apres la toilette, on se frictionne les mains, on enfile des gants propres pour le pansement, puis on recommence apres le geste. On évite de toucher le telephone, la porte ou le dossier avec les gants. On nettoie la surface de soin utilisee selon le protocole. Enfin, on trace les soins et on signale toute rougeur ou tout ecoulement observe.",
     "On attend la distinction geste sale / geste propre, le changement de gants, la friction et le bionettoyage.")],
C("Les mains sont le principal vecteur de transmission : frictionner au bon moment protège la personne, le professionnel et l'environnement.",
  "friction hydro-alcoolique : 20 à 30 secondes · lavage au savon : au moins 30 secondes",
  "avant contact · avant geste aseptique · après geste sale · après contact",
  "Friction~Geste d'hygiène~Mains~Principal vecteur~Gants~Complément obligatoire~Bionettoyage~Nettoyage et désinfection~Infection~Iatrogénie",
  "Se frictionner les mains~Retirer les gants souillés~En changer pour chaque geste~Nettoyer la surface~Tracer les observations",
  "Croire que les gants suffisent|Frictionner sur des mains souillées|Garder les mêmes gants entre deux soins|Oublier les espaces entre les doigts",
  "30 secondes~Durée du lavage~20 à 30~Durée de friction~Gants~Changement systématique~Montre~Réservoir de germs~Sha~Solution hydro-alcoolique",
  "Geste sale~Toilette et linge~Geste propre~Pansement et plaie",
  "Lavage au savon~Mains souillées~Friction~Mains propres et sèches"))

# ============================================================ SOIN3
add("SOIN3", "La toilette de la personne : préparation et déroulé", "Santé et soins", ["1re pro"],
S("La toilette est un soin quotidien qui associe hygiene, confort, surveillance et relation."
  "|Elle peut etre realisee au lavabo, au bain, sous la douche ou au lit selon l'autonomie de la personne."
  "|Le niveau d'autonomie determine le role de l'accompagnant : faire avec, aider ou faire a la place."
  "|La preparation comprend le material, l'eau chaude, les serviettes, les gants et un dressing."
  "|La securite impose un sol non glissant, une temperature adaptee et une surveillance permanente."
  "|La toilette du visage et des mains peut suffire certains jours si la personne est fatiguee."
  "|Un ordre logique va du plus propre au plus sale : visage, haut du corps, bas du corps, zone intime."
  "|Le changement de linge et de draps s'effectue sans decouvrir inutilement la personne."
  "|Chaque etape est l'occasion d'observer la peau, la mobilite, la douleur et l'humeur."
  "|Une douleur lors d'un mouvement peut témoigner d'une contracture, d'une escarre ou d'une articulation atteinte."
  "|La personne est associee aux choix : heure, produit, ordre des gestes et quantite d'aide."
  "|Le soin se termine par une installation confortable, un rangement propre et une transmission ecrite."),
[QC("Quel facteur détermine le mode de toilette ?", "L'heure de la journée~Le niveau d'autonomie de la personne~La couleur de la chambre~Le nombre de soignants", 1,
     "On adapte le soin a ce que la personne peut faire elle-meme."),
 QC("Quel ordre respecte-t-on lors d'une toilette ?", "Du plus sale au plus propre~Du plus propre au plus sale~Du bas vers le haut~Au hasard", 1,
     "On va du plus propre au plus sale pour limiter la contamination."),
 QC("Quel équipement protège la pudeur ?", "Un tablier~Un dressing~Un gant~Un drap de bain uniquement", 1,
     "Le dressing couvre la personne pendant les transferts et les soins."),
 QC("Que faut-il surveiller pendant la toilette ?", "La météo~La peau, la douleur et la mobilité~Le prix du savon~Le nombre de serviettes", 1,
     "La toilette est un moment d'observation clinique privilegie."),
 QC("Quel signe peut évoquer une escarre débutante ?", "Une peau souple~Une rougeur persistante~Une bonne mobilité~Une température normale", 1,
     "Une rougeur qui ne s'efface pas est un signe d'alerte."),
 QC("Qui choisit l'heure et les préférences du soin ?", "Le seul professionnel~La personne accompagnée~La famille toujours~Le médecin uniquement", 1,
     "Le projet individualise recueille les preferences de la personne."),
 QC("Que faire après la toilette ?", "Laisser le matériel sur le lit~Installer, ranger et transmettre~Partir sans rien dire~Fermer la fenêtre", 1,
     "L'installation, le rangement et la trace ecrite completent le soin.")],
[QT("Expliquer comment adapter une toilette selon le niveau d'autonomie, avec trois situations.",
     "Si la personne est autonome, le professionnel prepare le material, assure la securite et reste disponible, mais la personne realise seule les gestes : on favorise l'independance. Si elle est partiellement dependante, on fait avec elle : on l'installe au lavabo, on l'aide a enfiler les vetements et on lave les zones qu'elle ne peut pas atteindre, comme le dos. Si elle est totalement dependante, on realise la toilette au lit, en deux ou trois temps pour eviter la fatigue, avec un dressing et une surveillance permanente. Dans les trois cas, on explique, on demande l'accord, on respecte le rythme et on observe la peau. L'objectif n'est pas de faire vite mais de maintenir la dignite et le confort.",
     "On attend les trois niveaux d'aide, les gestes correspondants et le maintien de l'autonomie."),
 QT("Pendant une toilette, vous constatez une rougeur au talon qui ne s'efface pas. Décrire la conduite à tenir.",
     "On arrete de masser la zone, car le massage d'une rougeur peut aggravar les lesions. On note la localisation exacte, la taille, la couleur, la presence de chaleur, d'une douleur ou d'une plaie. On compare avec les observations precedentes pour savoir si la rougeur est nouvelle ou persistante. On signale immediatement a l'infirmier, oralement puis par ecrit dans le dossier de suivi, en decrivant les faits et non une interpretation. On adapte l'installation pour supprimer la pression sur le talon, par exemple avec un coussin ou un changement de position, sans creer de nouveau point d'appui. On poursuit la toilette en evitant de frotter la zone et on surveille l'evolution. On ne pose pas de pansement ou de creme sans prescription.",
     "On attend l'absence de massage, la description precise, la transmission et la suppression de la pression.")],
C("La toilette est un soin relationnel et d'observation : on adapte l'aide à l'autonomie et on protège la peau.",
  "faire avec · aider · faire à la place",
  "du plus propre au plus sale · rougeur persistante = alerte escarre",
  "Autonomie~Capacité d'agir~Toilette au lit~Pour la personne dépendante~Dressing~Respect de la pudeur~Escarre~Rougeur persistante~Observation~Peau et mobilité",
  "Préparer le matériel~Demander l'accord~Installer en sécurité~Laver du propre au sale~Observer et transmettre",
  "Masser une rougeur|Découvrir la personne inutilement|Forcer un mouvement douloureux|Oublier de noter l'observation",
  "Visage~Première zone~Dos~Zone souvent négligée~Talon~Site d'escarre~Projet individualisé~Préférences de la personne~Dressing~Intimité",
  "Faire avec~Favoriser l'autonomie~Faire à la place~Perte d'initiative",
  "Toilette au lavabo~Personne autonome~Toilette au lit~Personne dépendante"))

# ============================================================ SOIN4
add("SOIN4", "La surveillance de l'état de santé : paramètres et signes", "Santé et soins", ["1re pro"],
S("Surveiller l'état d'une personne, c'est observer des signes et mesurer des paramètres de facon régulière."
  "|Les principaux paramètres vitaux sont la temperature, le pouls, la frequence respiratoire, la pression arterielle, la saturation en oxygene et la douleur."
  "|Le pouls se prend avec deux doigts au poignet ou au cou, pendant une minute."
  "|La frequence respiratoire se compte en observant les mouvements de la poitrine ou du ventre."
  "|La pression arterielle s'exprime en millimetres de mercure, avec une valeur systolique et une valeur diastolique."
  "|La saturation en oxygene se lit avec un oxymetre de pouls, apres mise au repos du doigt."
  "|La douleur est appreciee par l'ecoute et, si possible, par une echelle simple adaptée a la personne."
  "|Les signes generaux a observer sont l'appetit, la soif, le sommeil, les selles, les urines, l'humeur et la mobilite."
  "|Une modification par rapport à l'habitude est plus significative qu'une valeur isolee."
  "|Toute mesure doit etre datee, inscrite et assortie d'un commentaire si elle est inhabituelle."
  "|Le role de l'accompagnant est d'observer et de transmettre, pas de poser un diagnostic ni de modifier un traitement."
  "|Une situation d'urgence impose d'alerter immediatement l'infirmier ou le medecin."),
[QC("Quels sont les paramètres vitaux ?", "Température, pouls, respiration, tension, saturation et douleur~Poids, taille et âge~Nom, prénom et adresse~Repas et boissons seulement", 0,
     "Ces six paramètres sont les principaux indicateurs de l'etat vital."),
 QC("Comment prendre le pouls ?", "Avec le pouce~Avec deux doigts pendant une minute~Avec un stethoscope seulement~En comptant les pas", 1,
     "Le pouce a son propre pouls ; on utilise l'index et le majeur."),
 QC("Comment mesurer la fréquence respiratoire ?", "En écoutant le cœur~En observant les mouvements thoraciques~En prenant la tension~En regardant les yeux", 1,
     "On compte les mouvements de la poitrine ou du ventre pendant une minute."),
 QC("Que signifie la valeur diastolique ?", "La pression lors de la contraction~La pression lors du relâchement~La fréquence cardiaque~La saturation", 1,
     "La diastolique correspond a la pression arterielle minimale, au relachement."),
 QC("Qu'appelle-t-on la saturation en oxygène ?", "La quantité d'air dans la chambre~Le pourcentage d'oxygène fixé par l'hémoglobine~Le nombre de respirations~La température du corps", 1,
     "La SpO2 indique la part d'hemoglobine saturee en oxygene."),
 QC("Pourquoi comparer avec l'habitude de la personne ?", "Parce que chaque personne a des valeurs usuelles~Parce que les appareils sont approximatifs~Parce que c'est plus rapide~Ce n'est pas utile", 0,
     "Une valeur est interpretee par rapport au terrain et aux habitudes de la personne."),
 QC("Quel est le rôle de l'accompagnant face à une anomalie ?", "Poser un diagnostic~Observer, transmettre et alerter~Modifier le traitement~Rassurer sans rien dire", 1,
     "L'accompagnant transmet, il ne diagnostique pas et ne prescrit pas.")],
[QT("Une résidente dit « je ne vais pas bien » mais sourit. Comment conduire votre observation ?",
     "On prend la plainte au serieux, meme si l'apparence est rassurante : les mots et le comportement peuvent etre discordants. On s'installe a sa hauteur, on l'ecoute sans l'interrompre et on reformule pour verifier ce qu'elle ressent. On recherche des signes associes : douleur, fatigue, essoufflement, nausee, fievre, changement d'appetit ou trouble du sommeil. On mesure les parametres vitaux si c'est prevu dans le protocole et on compare avec les valeurs habituelles. On note exactement ses mots, l'heure et les signes observes, puis on transmet a l'infirmier. On ne dit pas « vous n'avez rien » et on ne rassure pas a vide : on explique que l'on va prevenir la personne competente. Une plainte repettee peut annoncer une aggravation, notamment chez une personne qui exprime difficilement sa douleur.",
     "On attend ecoute, signes associes, mesure, transmission fidèle et absence de diagnostic."),
 QT("Expliquer l'importance de la traçabilité des observations dans un dossier de suivi.",
     "La trace ecrite permet a tous les professionnels de connaitre l'etat de la personne, meme en dehors de leur presence. Elle assure la continuite des soins entre les equipes et les services. Elle apporte une preuve datée de ce qui a ete observe et transmis, ce qui est important en cas d'evenement indesirable ou de litige. Enfin, elle permet de suivre l'evolution dans le temps : une valeur isolee est peu informative, mais une courbe ou une succession de mesures revele une tendance. Une bonne transmission est factuelle, concise, datée et signee : on ecrit les chiffres et les mots de la personne, pas une interpretation. On evite les formules vagues comme « va bien » ou « peu bien ». Elle complete, sans la remplacer, la transmission orale a l'equipe.",
     "On attend continuité, preuve, suivi dans le temps et qualites d'une transmission ecrite.")],
C("Surveiller, c'est mesurer et observer par rapport à l'habitude, puis transmettre des faits datés sans diagnostiquer.",
  "température · pouls · respiration · tension · SpO2 · douleur",
  "une modification par rapport à l'habitude est plus significative qu'une valeur isolée",
  "Paramètre~Mesure chiffrée~Observation~Signe perçu~Transmission~Information datée~Alerte~Anomalie à signaler~Douleur~Perception subjective",
  "Installer la personne au repos~Mesurer avec l'appareil adapté~Comparer aux valeurs usuelles~Noter les faits~Alerter si nécessaire",
  "Poser un diagnostic|Modifier une prescription|Écrire une appréciation vague|Oublier la date de la mesure",
  "60 à 100~Pouls au repos~12 à 20~Respirations par minute~37 °C~Température centrale~SpO2~Saturation en oxygène~Douleur~Échelle adaptée",
  "Mesure~Valeur chiffrée~Observation~Signe qualitatif",
  "Transmission orale~Immédiate~Transmission écrite~Datée et factuelle"))

# ============================================================ SOIN5
add("SOIN5", "L'installation et les transferts : sécurité et ergonomie", "Santé et soins", ["1re pro"],
S("Installer et deplacer une personne fait partie des soins quotidiens qui engagent sa securite et son confort."
  "|Un transfert est un deplacement d'un point a un autre : lit vers fauteuil, fauteuil vers lit, ou vers la toilette."
  "|La premiere regle est d'evaluer les capacites de la personne et le poids qu'elle peut porter."
  "|Le principe est de faire le moins possible a la place de la personne et de l'aider au maximum de ses capacites."
  "|Le matériel adapté comprend le lève-personne, le drap de glissement, le disque de transfert et les barres d'appui."
  "|Une bonne ergonomie protege aussi le professionnel : dos droit, genoux plies, charges au plus près du corps."
  "|On explique le transfert avant de le realiser et on demande le consentement."
  "|La hauteur du lit est reglee pour que les pieds de la personne reposent a plat au sol."
  "|Les freins du fauteuil et du lit sont verifies avant chaque mobilisation."
  "|Les tuyaux, fils et objets au sol sont écartés pour eviter les chutes."
  "|Une douleur, un vertige ou une fatigue soudaine interrompent le geste et imposent une evaluation."
  "|Le transfert et les aides utilisees sont traces dans le dossier pour assurer la continuite."),
[QC("Quelle est la première étape avant un transfert ?", "Pousser directement~Évaluer les capacités de la personne~Appeler la famille~Fermer la porte", 1,
     "On evalue ce que la personne peut faire et le materiel necessaire."),
 QC("Quel principe guide l'aide au transfert ?", "Faire toujours à la place~Faire le moins possible à la place et aider au maximum~Ne jamais aider~Laisser la personne seule", 1,
     "On favorise l'autonomie tout en apportant l'aide necessaire."),
 QC("Quel matériel facilite un transfert difficultueux ?", "Un marteau~Un lève-personne~Une balance~Un stethoscope", 1,
     "Le lève-personne permet de deplacer une personne sans effort pour le soignant."),
 QC("Comment protéger votre dos ?", "Pencher le dos en avant~Garder le dos droit et plier les genoux~Porter à bout de bras~Tourner le tronc brusquement", 1,
     "Le dos reste droit, les genoux flechissent et la charge reste proche du corps."),
 QC("Que vérifier sur un fauteuil avant un transfert ?", "Sa couleur~Ses freins~Son prix~Son nombre de roues", 1,
     "Les freins doivent etre serres pour eviter tout deplacement."),
 QC("Quel signe doit interrompre le transfert ?", "Un sourire~Une douleur ou un vertige~Une lumière allumée~Un silence", 1,
     "Douleur, vertige ou fatigue imposent d'arreter et d'evaluer."),
 QC("Que faut-il tracer après un transfert ?", "L'heure uniquement~Le geste, les aides utilisées et les observations~Le nom du médecin~La température de la chambre", 1,
     "La trace assure la continuite entre les professionnels.")],
[QT("Décrire les étapes d'un transfert lit-fauteuil avec une personne partiellement autonome.",
     "On commence par expliquer le transfert et obtenir l'accord de la personne. On evalue sa capacite a se lever et a supporter une partie du poids. On.prepare le fauteuil a angle ouvert du lit, on serre les freins et on regle la hauteur du lit pour que les pieds soient a plat. On degage les obstacles au sol. On installe la personne assise au bord du lit, on lui demande de pencher le tronc vers l'avant et de pousser sur ses jambes. Le professionnel se place a cote, un genou au contact du lit, le dos droit, et accompagne le mouvement en soutenant le bassin ou les bras sans tirer sur les epaules. Une fois assise, on vérifie l'equilibre, on ajuste les pieds et les accoudoirs, puis on trace le transfert et toute remarque de la personne.",
     "On attend préparation, accord, positionnement, technique de levage et traçabilité."),
 QT("Une personne chute dans sa chambre. Quels sont les bons réflexes et ce qu'il ne faut pas faire ?",
     "On ne relève pas immediatement la personne : une chute peut avoir provoque une fracture ou un traumatisme. On reste a cote d'elle, on la rassure et on evalue sa conscience, sa douleur, sa capacite a bouger les membres et l'existence d'une deformation ou d'un saignement. On alerte l'infirmier, qui decidera de la conduite a tenir et de l'appel au medecin ou aux secours. On ne donne ni boisson ni medicament avant l'evaluation. On protege la personne du froid et on note l'heure, le lieu, les circonstances et les signes observes. On ne deplace pas les objets avant que l'equipe ait evalue la situation, car ils peuvent aider a comprendre la chute. Apres la prise en charge, on analyse les causes : sol glissant, lit trop haut, aide technique absente ou trouble de la marche, afin d'adapter l'environnement.",
     "On attend : ne pas relever d'abord, alerter, evaluer, tracer et analyser les causes.")],
C("Un transfert réussi protège la personne et le soignant : évaluer, préparer, accompagner et tracer.",
  "faire le moins possible à la place · aider au maximum des capacités",
  "dos droit · genoux pliés · freins serrés · lit à hauteur adaptée",
  "Transfert~Déplacement de la personne~Autonomie~Capacité d'agir~Aide technique~Lève-personne et drap~Ergonomie~Protection du dos~Chute~Risque à prévenir",
  "Évaluer les capacités~Expliquer et demander l'accord~Préparer le matériel et les freins~Accompagner le mouvement~Tracer et réévaluer",
  "Tirer sur les épaules|Se pencher le dos rond|Oublier les freins|Relever immédiatement après une chute",
  "Freins~Sécurité du fauteuil~Drap de glissement~Aide au transfert~Dos droit~Ergonomie~Chute~Événement à signaler~Douleur~Arrêt du geste",
  "Faire avec~Maintenir l'autonomie~Faire à la place~Risque de perte d'initiative",
  "Transfert actif~La personne participe~Transfert passif~L'aide réalise le geste"))

# ============================================================ SOIN6
add("SOIN6", "L'alimentation et l'hydratation : accompagnement du repas", "Santé et soins", ["Terminale pro"],
S("Accompagner un repas, c'est veiller à la fois à la nutrition, à l'hydratation et au plaisir de manger."
  "|Les besoins energetiques augmentent en cas de maladie, de convalescence ou de trouble de la deglutition."
  "|Une desnutrition se manifeste par une perte de poids, une fatigue et une diminution des apports."
  "|La dehydration se traduit par une bouche seche, une urine foncée, une constipation ou une confusion."
  "|La dysphagie est une difficulté à avaler qui expose aux fausses routes."
  "|Les textures adaptées vont du liquide au mixé, en passant par le mou et le hache menu."
  "|Une personne dysphagique doit etre installée assise, le menton legerement flechi, pendant et apres le repas."
  "|Les bouchées sont petites et le rythme lent : on ne presse jamais la personne."
  "|L'observation des apports — ce qui est reellement mange et bu — est transcrite dans le dossier."
  "|On respecte les preferences alimentaires, les habitudes culturelles et les prescriptions medicales."
  "|Un repas pris dans la bonne humeur et avec peu de bruit favorise l'appetit."
  "|La surveillance apres le repas porte sur la toux, la voix mouillee, la respiration et le bien-etre general."),
[QC("Quel signe évoque une déshydratation ?", "Une urine claire~Une bouche sèche et des urines foncées~Un appétit accru~Une peau humide", 1,
     "Bouche seche, urines foncees et constipation sont des signes classiques."),
 QC("Qu'est-ce qu'une dysphagie ?", "Une difficulté à avaler~Une allergie alimentaire~Un excès d'appétit~Une digestion trop rapide", 0,
     "La dysphagie expose aux fausses routes et necessite une texture adaptee."),
 QC("Comment installer une personne dysphagique pendant le repas ?", "Allongée~Assise, le menton légèrement fléchi~Tête en arrière~Debout", 1,
     "La position assise et le menton flechi protegent les voies respiratoires."),
 QC("Quel est un signe de fausse route ?", "Un sourire~Une toux ou une voix mouillée~Une respiration calme~Un regard vif", 1,
     "Toux, etouffement et modification de la voix doivent alerter."),
 QC("Que faut-il noter dans le dossier après un repas ?", "La couleur de la nappe~Les quantités réellement consommées~Le nombre de couverts~La recette du plat", 1,
     "La traçabilité des apports est essentielle pour adapter l'alimentation."),
 QC("Quel facteur favorise l'appétit ?", "Le bruit et la précipitation~Un cadre calme et convivial~Une lumière très forte~Le silence total", 1,
     "Un environnement agréable et sans pression facilite la prise alimentaire."),
 QC("Qui décide d'un changement de texture ?", "L'accompagnant seul~L'équipe soignante sur prescription ou évaluation~La famille seule~Le voisin de table", 1,
     "La texture est decidée apres evaluation, souvent sur avis medical ou orthophonique.")],
[QT("Décrire l'accompagnement d'un repas pour une résidente présentant une dysphagie.",
     "On vérifie d'abord la texture prescrite et la présence d'un protocole. On installe la personne assise, le dos droit, les pieds appuyés et le menton légèrement fléchi, et on reste a sa hauteur. On propose de petites bouchées, on attend qu'elle avale avant d'en donner une autre et on alterne solide et boisson selon les recommandations. On ne parle pas la bouche pleine et on ne fait pas rire pendant le repas. On surveille la toux, la voix, la respiration et tout signe de gêne. En cas de fausse route, on cesse immédiatement l'alimentation et on alerte l'equipe selon le protocole. On note les quantites consommees, la tolerance et l'heure, puis on laisse la personne au repos en position assise encore quelque temps.",
     "On attend installation, rythme, surveillance, gestion de la fausse route et traçabilité."),
 QT("Une personne mange moins depuis une semaine et a perdu du poids. Quels éléments observer et à qui les transmettre ?",
     "On releve le poids si un protocole de pesée existe et on compare avec les dernières valeurs. On note les repas réellement pris, les quantites, les aliments refuses et les boissons absorbees. On recherche les causes possibles : modification du gout, douleur buccale, dentition defectueuse, difficulté a manger seul, dépression, conflit avec un autre resident ou horaire inadapte. On observe l'appetit, l'humeur, la fatigue et les signes digestifs. On transmet des faits précis a l'infirmier et a l'equipe pluriprofessionnelle, qui pourront demander un avis medical, orthophonique ou dietetique. On adapte dans l'attente les conditions du repas : installation, convivialite, petites portions frequentes et respect des preferences. On ne force jamais a manger et on consigne les observations dans le dossier.",
     "On attend observation quantitative et qualitative, recherche de causes, transmission et adaptations.")],
C("Accompagner le repas, c'est respecter le rythme et la sécurité de la personne tout en mesurant ce qu'elle consomme réellement.",
  "dysphagie → texture adaptée + position assise + petites bouchées",
  "déshydratation : bouche sèche, urines foncées, constipation, confusion",
  "Nutrition~Apports alimentaires~Hydratation~Boissons et eau~Dysphagie~Difficulté à avaler~Texture~Adaptation du repas~Fausse route~Urgence à gérer",
  "Vérifier la prescription~Installer la personne~Proposer de petites bouchées~Surveiller la déglutition~Tracer les apports",
  "Forcer à manger|Donner une bouchée avant que la précédente soit avalée|Ignorer une toux|Noter le repas servi au lieu du repas mangé",
  "Bouche sèche~Signe de déshydratation~Voix mouillée~Signe de fausse route~Texture mixée~Adaptation~Poids~Indicateur nutritionnel~Calme~Favorise l'appétit",
  "Dysphagie~Difficulté à avaler~Fausse route~Passage dans les voies aériennes",
  "Apports servis~Ce qui est proposé~Apports réels~Ce qui est consommé"))

# ============================================================ SOIN7
add("SOIN7", "La bientraitance et la prévention de la maltraitance", "Santé et soins", ["Terminale pro"],
S("La bientraitance est une posture professionnelle qui vise le respect de la personne, de ses droits et de sa dignite."
  "|Elle s'oppose à la maltraitance, qui peut etre physique, verbale, psychologique, sexuelle, financiere ou institutionnelle."
  "|La maltraitance n'est pas toujours intentionnelle : elle peut resulter de l'ignorance, de la fatigue ou d'un fonctionnement défectueux."
  "|La maltraitance institutionnelle se manifeste par des regles rigides qui suppriment toute initiative et toute vie privee."
  "|Les signes d'alerte sont une peur inhabituelle, un retrait, une agression, des hematomes ou une négligence de l'hygiene."
  "|Un changement brutal de comportement doit toujours etre pris au serieux et transmis."
  "|La bientraitance s'appuie sur l'ecoute, l'explication des soins, le respect du rythme et le maintien du lien social."
  "|Elle implique de considerer la personne comme un sujet de droits et un partenaire de son accompagnement."
  "|Le secret professionnel ne doit jamais servir a dissimuler une situation de maltraitance."
  "|Chaque professionnel doit connaitre la procedure interne d'alerte et les interlocuteurs designes."
  "|Un signalement est une protection de la personne, pas une accusation contre un collegue."
  "|La reflexivite, c'est-a-dire la capacite a questionner sa propre pratique, est un levier essential de la bientraitance."),
[QC("Quelle forme de maltraitance concerne des règles rigides qui effacent la personne ?", "Physique~Institutionnelle~Financière~Sexuelle", 1,
     "La maltraitance institutionnelle tient au fonctionnement du service."),
 QC("La maltraitance est-elle toujours intentionnelle ?", "Oui~Non, elle peut être involontaire~Uniquement physique~Seulement en famille", 1,
     "La fatigue, l'ignorance ou l'organisation peuvent produire des situations maltraitantes."),
 QC("Quel signe doit alerter ?", "Un sourire habituel~Un retrait soudain ou une peur inhabituelle~Une tenue propre~Un repas terminé", 1,
     "Un changement brutal de comportement est un signal d'alerte."),
 QC("Que signifie la réflexivité ?", "Répéter toujours le même geste~Questionner sa propre pratique~Refuser tout changement~Travailler seul", 1,
     "La reflexivite est la capacite a prendre du recul sur ses gestes et ses representations."),
 QC("Le secret professionnel peut-il cacher une maltraitance ?", "Oui, toujours~Non, il a des limites et doit céder devant la protection~Seulement en famille~Uniquement pour les médecins", 1,
     "Le secret ne peut pas couvrir une situation ou la personne est en danger."),
 QC("Qu'est-ce qu'un signalement ?", "Une accusation publique~Une alerte selon une procedure pour protéger la personne~Une sanction automatique~Un simple racontar", 1,
     "Le signalement vise la protection et suit une procedure interne."),
 QC("Quel geste relève de la bientraitance ?", "Décider sans expliquer~Expliquer le soin et respecter le rythme~Presser la personne~Parler d'elle sans elle", 1,
     "L'explication et le respect du rythme sont des marques de bientraitance.")],
[QT("Distinguer la maltraitance physique de la maltraitance institutionnelle, avec un exemple pour chacune.",
     "La maltraitance physique est un geste concret qui porte atteinte a l'integrite de la personne : une gifle, un geste brutal lors d'un transfert, une contention injustifiee. La maltraitance institutionnelle est plus diffuse : elle tient a l'organisation du service, par exemple des horaires de lever identiques pour tous, l'interdiction de sortir, l'absence d'espace prive ou des transmissions faites devant la personne. Dans le premier cas, un acte est identifiable ; dans le second, c'est le systeme qui prive la personne de ses droits et de son initiative. Les deux peuvent se combiner. Dans les deux cas, la personne est victime d'une atteinte a sa dignite, et la bientraitance exige de modifier les pratiques et l'organisation.",
     "On attend deux definitions, deux exemples et le lien avec la dignite."),
 QT("Un collègue parle brutalement à une résidente et vous êtes témoin de la scène. Que faites-vous ?",
     "On ne reste pas passif. On s'approche calmement, on interrompt le ton brutal sans agresser le collegue, par exemple en proposant de prendre le relais pour le soin. On rassure la residente et on l'ecoute separement. On note les faits de maniere objective : date, heure, lieu, propos exacts, temoins, reaction de la personne. On informe le cadre de sante ou le referent bientraitance selon la procedure interne, sans transforme le recit en jugement. On ne fait pas de rumeur et on n'expose pas la personne. Si la situation represente un danger immediat, on alerte sans attendre. On peut ensuite echanger avec le collegue dans un cadre approprie pour comprendre sa fatigue ou son manque de formation, car la bientraitance concerne aussi le soutien des professionnels.",
     "On attend intervention calme, ecoute de la personne, faits objectifs, procedure interne et soutien au collegue.")],
C("La bientraitance est une posture quotidienne : elle protège la dignité et repose sur l'écoute, l'explication et la remise en question.",
  "maltraitance : physique · verbale · psychologique · financière · institutionnelle",
  "signaux : peur, retrait, hématomes, négligence · signalement = protection",
  "Bientraitance~Posture professionnelle~Dignité~Respect de la personne~Maltraitance~Atteinte à la personne~Institutionnelle~Dysfonctionnement du service~Signalement~Alerte interne",
  "Repérer un changement~Écouter la personne~Noter les faits objectifs~Alerter selon la procédure~Questionner sa pratique",
  "Rester passif|Confondre secret et dissimulation|Accuser sans preuve|Ignorer la fatigue des professionnels",
  "Propos exacts~Fait à transmettre~Date et heure~Trace indispensable~Référent~Interlocuteur interne~Reflexivité~Recul sur ses gestes~Droits~Fondement de la posture",
  "Maltraitance~Atteinte délibérée ou non~Bientraitance~Respect et écoute",
  "Secret professionnel~Protection des informations~Limite~Danger pour la personne"))

# ============================================================ DR1
add("DR1", "Les droits des patients et la relation de soin", "Droit et réglementation sanitaire et sociale", ["1re pro"],
S("La relation de soin repose sur des droits reconnus a la personne et sur des devoirs pour les professionnels."
  "|La loi du 4 mars 2002 relative aux droits des malades et a la qualite du systeme de sante est un texte de reference."
  "|Toute personne a droit au respect de sa dignite, de son integrite et de sa vie privee."
  "|Le droit a l'information implique une explication claire, compréhensible et adaptee a la situation."
  "|Le consentement aux soins doit etre libre et eclaire ; il peut etre retire a tout moment."
  "|Le medecin doit recueillir le consentement avant un acte medical, sauf urgence."
  "|La personne peut désigner une personne de confiance pour l'accompagner dans ses demarches."
  "|Le dossier medical est confidentiel et la personne a un droit d'acces a ses informations."
  "|Les directives anticipees de fin de vie permettent d'exprimer ses souhaits a l'avance."
  "|Une personne majeure peut refuser un soin : le professionnel doit l'informer des consequences et tracer le refus."
  "|L'enfant mineur et la personne sous protection beneficient de regles particulieres."
  "|L'accompagnant contribue a ces droits en expliquant, en ecoutant et en transmettant les demandes."),
[QC("Quelle loi est un texte de référence pour les droits des malades ?", "La loi du 9 décembre 1905~La loi du 4 mars 2002~La loi du 11 février 2005~La loi de 1898", 1,
     "La loi du 4 mars 2002 est relative aux droits des malades et a la qualite du systeme de sante."),
 QC("Qu'est-ce qu'un consentement éclairé ?", "Un accord donné sans information~Un accord après information comprise~Un accord de la famille~Un accord implicite", 1,
     "Le consentement eclaire suppose une information claire et comprise."),
 QC("Peut-on retirer un consentement ?", "Non, jamais~Oui, à tout moment~Seulement avant l'acte~Seulement avec l'accord du médecin", 1,
     "Le consentement est reellement libre et peut etre retire."),
 QC("Que garantit le droit à l'information ?", "Une explication adaptée et compréhensible~Un silence professionnel~Une décision sans explication~Un document illisible", 0,
     "L'information doit etre claire et adaptee a la personne."),
 QC("Quel est le rôle d'une personne de confiance ?", "Remplacer le médecin~Accompagner la personne dans ses démarches~Payer les soins~Signer les ordonnances", 1,
     "La personne de confiance accompagne et temoigne des souhaits de la personne."),
 QC("Le dossier médical est-il accessible à la personne ?", "Non, jamais~Oui, elle a un droit d'accès~Seulement au médecin~Uniquement après sa sortie", 1,
     "La personne dispose d'un droit d'acces a son dossier medical."),
 QC("Comment tracer un refus de soin ?", "Ne rien écrire~Noter objectivement le refus, l'information donnée et la date~Faire une remarque personnelle~Effacer la mention", 1,
     "La trace doit etre factuelle, datée et mentionner l'information délivrée.")],
[QT("Expliquer la différence entre information et consentement dans une relation de soin.",
     "L'information est une obligation du professionnel : il doit expliquer la nature du soin, son objectif, les benefices, les risques et les alternatives, dans un langage que la personne peut comprendre. Le consentement est la decision de la personne apres avoir recu cette information : elle accepte ou refuse librement. On peut avoir ete parfaitement informe et refuser, ce qui doit etre respecte ; on peut aussi donner un accord qui n'est pas eclaire si l'information etait incomplete. Pour l'accompagnant, la distinction est concrete : il peut participer a l'information en reformulant simplement, mais il ne doit jamais forcer l'accord. Il transmet a l'infirmier les questions et les souhaits exprimes, et il note les decisions dans le respect du cadre de ses competences.",
     "On attend obligation du soignant / decision de la personne et le role de l'accompagnant."),
 QT("Une résidente refuse une prise de sang proposée par l'infirmier. Comment accompagner cette situation ?",
     "On ne la force pas et on ne la juge pas. On l'invite a exprimer les raisons de son refus : peur de la douleur, comprehension insuffisante, perte de confiance, fatigue ou souhait de ne pas etre piquee. On peut proposer que l'infirmier reprenne l'explication avec des mots simples et reponde a ses questions. On respecte une decision libre et eclairee, apres verifier qu'elle a bien compris les consequences du refus. On informe l'equipe et on trace objectivement : date, heure, propos de la personne, information donnee et decision. Si le refus met en jeu sa sante de maniere immediate, l'infirmier en referera au medecin, qui evaluera la situation. On continue d'accompagner la personne sans changer d'attitude ni isoler elle.",
     "On attend respect du refus, information, transmission, evaluation medicale si necessaire et non-jugement.")],
C("La relation de soin est encadrée par des droits opposables : informer, obtenir un consentement libre et respecter les choix.",
  "loi du 4 mars 2002 · consentement libre et éclairé · droit d'accès au dossier",
  "information = obligation du professionnel · consentement = décision de la personne",
  "Droits du patient~Dignité et intégrité~Information~Explication claire~Consentement~Accord libre~Refus~Décision respectée~Dossier~Confidentialité",
  "Expliquer simplement~Vérifier la compréhension~Demander l'accord~Respecter le refus~Tracer la décision",
  "Forcer un soin|Donner une information incomplète|Ignorer une personne de confiance|Écrire un jugement dans le dossier",
  "4 mars 2002~Loi sur les droits des malades~Personne de confiance~Accompagnement~Directives anticipées~Souhaits futurs~Refus~À tracer~Dossier~Accès garanti",
  "Information~Ce que dit le professionnel~Consentement~Ce que décide la personne",
  "Consentement~Accord explicite~Refus~Droit opposables"))

# ============================================================ DR2
add("DR2", "Le secret professionnel et la discrétion", "Droit et réglementation sanitaire et sociale", ["Terminale pro"],
S("Le secret professionnel est une obligation de confidentialite qui pese sur de nombreux professionnels de la sante et du social."
  "|Il est defini par l'article 226-13 du Code penal : sa violation est un delit punissable."
  "|Il couvre toutes les informations apprises dans l'exercice de la profession, y compris ce que l'on a simplement vu ou entendu."
  "|Le secret s'etend aux autres professionnels : on ne transmet qu'a ceux qui ont besoin de l'information pour la prise en charge."
  "|La discrétion professionnelle complete le secret : elle impose une retenue dans les propos et les ecrits."
  "|Un aide-soignant est tenu au secret, comme l'infirmier, le medecin ou le travailleur social."
  "|Le secret n'est pas absolu : la loi prevoit des exceptions, notamment le danger pour la personne ou autrui."
  "|Le signalement d'une situation de maltraitance ou de risque pour un mineur fait partie de ces exceptions."
  "|La transmission interne dans l'equipe est autorisee si elle est necessaire et limitee aux faits utiles."
  "|Les ecrits professionnels doivent rester factuels et eviter les details inutiles sur la vie privee."
  "|Les conversations dans les couloirs, les ascenseurs ou les refectoires sont a proscrire."
  "|Le respect du secret est une condition de la confiance de la personne accompagnee."),
[QC("Quel article du Code pénal définit le secret professionnel ?", "L'article 226-13~L'article 4~L'article 11~L'article 2002", 0,
     "L'article 226-13 du Code penal reprime la violation du secret professionnel."),
 QC("Que couvre le secret professionnel ?", "Uniquement les diagnostics~Toutes les informations apprises dans l'exercice~Seulement les écrits médicaux~Les seules conversations avec le médecin", 1,
     "Il couvre tout ce qui a ete vu, entendu ou appris dans le cadre professionnel."),
 QC("Un aide-soignant est-il tenu au secret ?", "Non~Oui~Seulement s'il a signé un contrat~Seulement en structure", 1,
     "Tout professionnel de sante ou du social est tenu au secret."),
 QC("Quelle est une exception au secret ?", "Une demande de la famille~Un danger pour la personne ou autrui~La curiosité d'un collègue~Une conversation informelle", 1,
     "Le secret cesse devant le danger ou lorsque la loi l'autorise expressement."),
 QC("Comment transmettre une information dans l'équipe ?", "À toute l'équipe~Uniquement aux professionnels concernés et au minimum utile~Par oral dans le couloir~À la famille", 1,
     "La transmission est nécessaire, limitee et destinee aux seuls intervenants concernes."),
 QC("Quel écrit est conforme au secret ?", "Un récit détaillé de la vie privée~Une phrase factuelle et utile à la prise en charge~Une opinion personnelle~Le nom d'un proche sans lien avec le soin", 1,
     "Les ecrits sont factuels, succincts et utiles."),
 QC("Où faut-il éviter de parler d'une personne ?", "Dans le bureau de transmission~Dans un couloir ou un ascenseur~Lors d'un staff~Avec l'infirmier", 1,
     "Les lieux ou l'on peut etre entendu par des tiers sont a eviter.")],
[QT("Expliquer pourquoi le secret professionnel est une condition de la confiance, tout en ayant des limites.",
     "Une personne accepte de parler de sa sante, de sa situation familiale ou de ses difficultés parce qu'elle croit que ces informations ne sortiront pas du cadre de soin. Si elle apprend qu'elles ont ete rapportees dans un couloir ou a des personnes non concernees, elle se taira et la prise en charge perdra son efficacite. Le secret est donc un outil de la relation de soin, pas une simple regle disciplinaire. Mais il n'est pas absolu : lorsqu'une personne est en danger, qu'il s'agit d'un mineur en risque ou d'une maladie a notification obligatoire, la loi autorise ou impose de transmettre a l'autorite competente. Dans ces cas, on respecte la procedure et on limite l'information au strict necessaire. Le professionnel doit toujours savoir distinguer secret, transmission interne nécessaire et exception legale.",
     "On attend le lien avec la confiance, la definition des limites et la procedure."),
 QT("Vous entendez un collègue raconter la situation d'un résident dans l'ascenseur. Que faites-vous ?",
     "J'interromps la conversation sans agresser le collegue, par exemple en rappelant calmement que ces informations ne peuvent pas etre tenues dans un lieu public. Je m'eloigne avec lui si possible pour lui expliquer le risque : des tiers peuvent entendre, et la personne ou sa famille pourrait apprendre la situation par hasard. Je ne repars pas avec l'information et je ne la repet pas a d'autres personnes. Je signale le fait au cadre de sante si la situation se repete, car il s'agit d'une faute professionnelle susceptible de sanctions. Je vérifie egalement ma propre pratique : dans les transmissions ecrites, je m'assure d'avoir note uniquement les faits utiles a la prise en charge. Enfin, je reste attentif au respect de la confidentialite dans les espaces partages, qui sont un lieu de risque frequent.",
     "On attend interruption calme, rappel de la regle, non-propagation, signalement et examen de sa propre pratique.")],
C("Le secret professionnel protège la personne et la confiance ; ses exceptions sont strictement encadrées par la loi.",
  "article 226-13 du Code pénal · violation = délit",
  "secret · discrétion · transmission nécessaire · exceptions légales",
  "Secret~Obligation de confidentialité~Discrétion~Retenue des propos~Transmission~Information limitée~Exception~Danger ou obligation légale~Confiance~Fondement de la relation",
  "Repérer l'information~Évaluer le besoin de transmission~Limiter aux personnes concernées~Écrire de façon factuelle~Alerter si danger",
  "Parler dans un couloir|Transmettre à toute l'équipe|Raconter la vie privée|Confondre secret et dissimulation d'un danger",
  "226-13~Article du Code pénal~Staff~Transmission collective autorisée~Couloir~Lieu à risque~Danger~Exception au secret~Dossier~Écrit factuel",
  "Secret professionnel~Protéger l'information~Discrétion~Ne pas divulguer",
  "Transmission interne~Nécessaire et limitée~Divulgation~Interdite hors cadre"))

# ============================================================ DR3
add("DR3", "Code de la santé publique et loi du 4 mars 2002", "Droit et réglementation sanitaire et sociale", ["Terminale pro"],
S("Le Code de la santé publique regroupe les textes qui organisent la sante, les soins et la protection des personnes."
  "|Il comprend des dispositions relatives aux droits des malades, a la sante publique et aux professions de sante."
  "|La loi du 4 mars 2002 a insere dans ce code plusieurs articles fondamentaux."
  "|L'article L.1110-4 assure a toute personne le respect de sa dignite et de son integrite."
  "|L'article L.1111-2 garantit le droit a l'information sur son etat de sante et les soins proposes."
  "|L'article L.1111-4 organise le consentement aux soins et le droit de refuser."
  "|La loi du 4 mars 2002 a cree la Haute Autorite de sante, chargee notamment de la qualite des soins."
  "|Elle a aussi renforce la representation des usagers dans les etablissements."
  "|Le Code de l'action sociale et des familles organise les etablissements medico-sociaux et les droits des usagers."
  "|Le Code du travail fixe les regles de duree de travail et de protection des salaries du secteur."
  "|Le reglement general de protection des donnees s'applique aux informations de sante, considerees comme sensibles."
  "|Un professionnel doit connaitre ces textes pour agir dans le cadre de ses competences et de la loi."),
[QC("Quel code regroupe les règles organisationnelles de la santé et des soins ?", "Le Code civil~Le Code de la santé publique~Le Code de la route~Le Code de commerce", 1,
     "Le Code de la sante publique contient les dispositions relatives aux droits des malades et a l'organisation des soins."),
 QC("Que garantit l'article L.1110-4 ?", "Le droit au travail~Le respect de la dignité et de l'intégrité~Le droit de vote~La liberté d'entreprise", 1,
     "Cet article assure a toute personne le respect de sa dignite et de son integrite."),
 QC("Quel article organise le consentement aux soins ?", "L.1110-4~L.1111-2~L.1111-4~L.226-13", 2,
     "L'article L.1111-4 traite du consentement et du refus de soins."),
 QC("Quelle institution a été créée par la loi du 4 mars 2002 ?", "La CNIL~La Haute Autorité de santé~L'ANSSI~L'OMS", 1,
     "La Haute Autorite de sante a ete creee par cette loi."),
 QC("Quel code organise les établissements médico-sociaux ?", "Le Code pénal~Le Code de l'action sociale et des familles~Le Code monétaire~Le Code rural", 1,
     "Le CASF régit les etablissements sociaux et medico-sociaux."),
 QC("Comment les données de santé sont-elles qualifiées par le RGPD ?", "Banales~Sensibles~Publiques~Anonymes par défaut", 1,
     "Les donnees de sante sont des donnees a risque eleve, dites sensibles."),
 QC("Que doit faire un professionnel qui ne connaît pas la règle applicable ?", "Agir quand même~Demander conseil et se former~Ignorer le texte~Laisser la famille décider", 1,
     "Il doit se renseigner, se former et agir dans les limites de ses competences.")],
[QT("Expliquer l'apport de la loi du 4 mars 2002 pour les droits des personnes accompagnées.",
     "Avant 2002, la relation de soin etait davantage marquee par le paternalisme medical. La loi du 4 mars 2002 a inverse la logique en affirmant que la personne est un sujet de droits : respect de sa dignite et de son integrite, droit a l'information claire, consentement libre et eclaire, droit de refuser un soin apres information, acces au dossier medical et designa ion d'une personne de confiance. Elle a aussi cree la Haute Autorite de sante pour ameliorer la qualite des soins et renforce la participation des usagers. Pour un accompagnant, cette loi se traduit dans des gestes concrets : expliquer avant d'agir, respecter un refus, transmettre les souhaits et ecrire des faits plutot que des jugements. Elle constitue un cadre de reference pour la bientraitance.",
     "On attend plusieurs apports de la loi et leurs traductions dans la pratique."),
 QT("Dans quel cadre un professionnel peut-il utiliser une information concernant une personne, et quelles précautions prendre ?",
     "L'information ne peut etre utilisee que dans le cadre de la prise en charge de la personne et par les professionnels qui en ont besoin. Les precisions sont : verifier que la personne concernee est bien identifiee, limiter l'information au strict necessaire, ne pas la transmettre a des tiers non autorises, utiliser les outils de l'etablissement et non un support personnel, et tracer les acces lorsque le dossier est informatise. Les donnees de sante etant sensibles au sens du RGPD, leur traitement doit etre justifie, proportionne et securise. En cas de doute sur l'autorisation de transmettre, on demande au responsable ou au delegue a la protection des donnees. Enfin, en dehors du service, on n'en parle pas, y compris avec la famille, sauf accord de la personne ou procedure prevue par la loi.",
     "On attend finalite de soin, minimalisation, securite, traçabilité et recours au responsable.")],
C("Le Code de la santé publique et la loi du 4 mars 2002 constituent le cadre juridique quotidien de l'accompagnement.",
  "L.1110-4 dignité · L.1111-2 information · L.1111-4 consentement",
  "loi du 4 mars 2002 · Haute Autorité de santé · données de santé sensibles",
  "Code de la santé publique~Texte de référence~Loi 2002~Droits des malades~Haute Autorité~Qualité des soins~Consentement~Décision de la personne~Données sensibles~RGPD",
  "Identifier le texte applicable~Repérer l'article concerné~Vérifier les limites de compétence~Agir et tracer~Demander conseil en cas de doute",
  "Ignorer le cadre légal|Se dire que la loi ne concerne pas les aides-soignants|Transmettre à un tiers non autorisé|Confondre code pénal et code de la santé",
  "L.1110-4~Dignité et intégrité~L.1111-2~Droit à l'information~L.1111-4~Consentement~2002~Loi fondatrice~CASF~Établissements médico-sociaux",
  "Code de la santé publique~Soins et droits des malades~Code de l'action sociale~Établissements et usagers",
  "Information~Comprendre pour décider~Consentement~Accepter ou refuser"))

# ============================================================ DR4
add("DR4", "La protection de l'enfance et des personnes vulnérables", "Droit et réglementation sanitaire et sociale", ["1re pro"],
S("La protection de l'enfance vise a garantir la securite, la sante et le developpement de l'enfant."
  "|La loi du 2 janvier 2002 reforme l'action sociale et medico-sociale et renforce les droits des usagers."
  "|Le Code de l'action sociale et des familles organise les mesures de protection de l'enfance."
  "|L'Aide sociale a l'enfance, ou ASE, est un service departemental qui intervient aupres des enfants en difficulté."
  "|Les mineurs peuvent etre confies a une famille d'accueil ou a un etablissement."
  "|Le juge des enfants prend des mesures comme la supervision educative ou le placement."
  "|Toute personne tenant des informations sur un enfant en danger peut faire un signalement au procureur."
  "|Les professionnels soumis au secret sont autorises a transmettre au president du conseil departemental."
  "|L'information preoccupante est un signal d'alerte transmis a la cellule departementale de recueil."
  "|Ne pas signaler une situation de danger peut constituer une faute professionnelle."
  "|Pour les adultes vulnerables, des mesures de protection comme la tutelle ou la curatelle peuvent etre prononcees."
  "|L'accompagnant observe les signes de souffrance et les transmet selon la procedure de l'etablissement."),
[QC("Quel service départemental intervient auprès des enfants en difficulté ?", "L'ASE~La CNIL~L'ANSSI~La CPAM", 0,
     "L'Aide sociale a l'enfance est un service du conseil departemental."),
 QC("Quel juge peut ordonner un placement ?", "Le juge des enfants~Le juge commercial~Le juge administratif~Le juge d'instruction", 0,
     "Le juge des enfants est competence pour les mesures de protection de la jeunesse."),
 QC("Qu'est-ce qu'une information préoccupante ?", "Une rumeur~Un signal d'alerte transmis à la cellule départementale~Un rapport médical~Une décision de justice", 1,
     "L'information preoccupante alerte les services sur une situation de risque pour l'enfant."),
 QC("Un professionnel peut-il transmettre une information sur un enfant en danger ?", "Non, jamais~Oui, dans le cadre légal prévu~Seulement à la famille~Uniquement au médecin", 1,
     "La loi autorise la transmission aux autorites competentes malgre le secret."),
 QC("Quelle mesure concerne un adulte vulnérable ?", "Le placement~La tutelle ou la curatelle~La garde à vue~L'examen", 1,
     "La tutelle et la curatelle sont des mesures de protection civile des majeurs."),
 QC("Que risque un professionnel qui ne signale pas un danger ?", "Rien~Une faute professionnelle et des sanctions possibles~Une récompense~Une promotion", 1,
     "L'absence de signalement peut être fautive lorsque le danger est connu."),
 QC("Quel est le rôle de l'accompagnant face à un signe de souffrance ?", "Faire une enquête~Observer et transmettre selon la procédure~Interroger seul l'enfant~Ignorer le signe", 1,
     "Il observe et alerte, sans mener l'enquete qui revient aux services competents.")],
[QT("Expliquer le parcours d'une information préoccupante et les précautions à prendre.",
     "Un professionnel observe des signes : blessures inexpliquees, négligence, peur, propos inquietants. Il ne mene pas d'enquête et n'interroge pas l'enfant de maniere insistante. Il consigne les faits observes de maniere objective, avec la date, le lieu et les propos exacts, puis il transmet l'information preoccupante a la cellule departementale de recueil, selon la procedure de son etablissement. Il informe son responsable hiearchique. Les services evaluent la situation et decident des mesures adaptées, avec l'intervention eventuelle du juge des enfants. La personne concernee doit etre informee de la transmission, sauf risque particulier. Le secret professionnel ne fait pas obstacle a cette transmission, car la protection de l'enfant est une exception legale. La precaution est de ne pas promettre le secret a l'enfant et de ne pas multiplier les recits entre collègues.",
     "On attend observation objective, procedure, roles respectifs et exception au secret."),
 QT("Dans un service d'accueil, vous remarquez qu'un adolescent est souvent seul, mal vêtu et dit avoir peur de rentrer chez lui. Que faites-vous ?",
     "Je prends la parole au serieux et je choisis un moment calme et prive pour l'ecouter, sans le presser de questions ni promettre de garder le secret. Je note objectivement ce qu'il dit et ce que j'observe : dates, propos exacts, tenue, humeur, presence de blessures. Je ne menace pas la famille et je ne contacte pas les parents de ma propre initiative. J'informe immediatement mon responsable et je transmets une information preoccupante a la cellule departementale selon la procedure, en preciseant l'urgence eventuelle. S'il y a un danger immediat, j'alerte aussi le procureur ou les services d'urgence conformement au protocole. Je reste disponible pour l'adolescent et je consigne les actions engagees. Je ne discute pas du cas avec les autres jeunes ou avec des collegues non concernes.",
     "On attend ecoute, transcription factuelle, procedure interne et autorites competentes.")],
C("Protéger une personne vulnérable, c'est observer, transmettre selon la procédure et laisser l'autorité compétente décider.",
  "ASE · juge des enfants · information préoccupante · signalement",
  "tutelle et curatelle pour les majeurs · secret assorti d'exceptions légales",
  "Protection de l'enfance~Sécurité de l'enfant~ASE~Service départemental~Information préoccupante~Signal d'alerte~Juge des enfants~Mesures de protection~Tutelle~Protection du majeur",
  "Observer les signes~Écouter sans enquêter~Noter les faits objectifs~Informer le responsable~Transmettre selon la procédure",
  "Promettre le secret à l'enfant|Interroger de façon insistante|Contacter la famille seul|Ne rien transmettre par peur",
  "ASE~Aide sociale à l'enfance~Juge~Placement ou supervision~Famille d'accueil~Mode d'accueil~Signalement~Alerte au procureur~Tutelle~Mesure civile",
  "Information préoccupante~Alerte à transmettre~Signalement~Procedure plus formelle",
  "Secret professionnel~Règle générale~Exception~Protection de l'enfant"))

# ============================================================ DR5
add("DR5", "Le cadre des établissements sanitaires et médico-sociaux", "Droit et réglementation sanitaire et sociale", ["Terminale pro"],
S("Les etablissements sanitaires et medico-sociaux accueillent des personnes qui ont besoin de soins, d'aides ou d'un hébergement."
  "|Les EHPAD sont des etablissements d'hebergement pour personnes agees dependantes."
  "|Les ESMS designent l'ensemble des etablissements sociaux et medico-sociaux."
  "|Le Code de l'action sociale et des familles fixe les conditions d'autorisation et de fonctionnement."
  "|Chaque etablissement dispose d'un projet d'etablissement, occasionnellement renouvele et evalue."
  "|Le contrat de sejour decrit les prestations, les droits et les obligations de la personne accueillie."
  "|Le conseil de la vie sociale associe les usagers et leurs proches a la vie de l'etablissement."
  "|La personne accompagnee beneficie d'un projet individualise,Personnalise selon les situations."
  "|Le reglement interieur fixe les regles de vie collective, dans le respect des droits individuels."
  "|La qualite est évaluee par des indicateurs, des audits et les retours d'experience."
  "|La gestion des risques comporte les procedures d'alerte, d'incident et de crise."
  "|L'accompagnant contribue a ce cadre en respectant les procedures et en signalant toute derogation."),
[QC("Que désigne un EHPAD ?", "Un hôpital~Un établissement d'hébergement pour personnes âgées dépendantes~Une crèche~Un centre de jeunesse", 1,
     "EHPAD signifie Etablissement d'hebergement pour personnes agees dependantes."),
 QC("Quel code fixe les conditions de fonctionnement des ESMS ?", "Le Code civil~Le Code de l'action sociale et des familles~Le Code pénal~Le Code du commerce", 1,
     "Le CASF encadre les etablissements sociaux et medico-sociaux."),
 QC("Quel document décrit les prestations d'un établissement pour la personne accueillie ?", "Le projet d'établissement~Le contrat de séjour~Le reglement de copropriété~Le bulletin officiel", 1,
     "Le contrat de sejour precise les prestations, droits et obligations."),
 QC("Quel est le rôle du conseil de la vie sociale ?", "Remplacer la direction~Associer usagers et proches à la vie de l'établissement~Gérer les finances~Prescrire des soins", 1,
     "Le CVS est une instance de participation des usagers."),
 QC("Qu'est-ce qu'un projet individualisé ?", "Un planning unique pour tous~Une réponse adaptée à la personne et à son projet de vie~Un document administratif~Une simple fiche de repas", 1,
     "Le projet individualise tient compte des besoins et des souhaits de la personne."),
 QC("À quoi sert un règlement intérieur ?", "À supprimer les droits individuels~À fixer les règles de vie collective~À remplacer le contrat de séjour~À éviter toute évaluation", 1,
     "Il organise la vie collective dans le respect des droits de chacun."),
 QC("Que fait l'accompagnant face à une dérogation ?", "L'ignore~La signale selon la procédure~La cache~La modifie seul", 1,
     "Toute derogation doit etre signalee selon la procedure de l'etablissement.")],
[QT("Expliquer la différence entre projet d'établissement, contrat de séjour et projet individualisé.",
     "Le projet d'etablissement est un document collectif et pluriannuel qui definit les orientations, les objectifs et l'organisation generale du service. Le contrat de sejour est un document individuel et contractuel : il precise les prestations proposees, les conditions d'hebergement, les droits et les obligations de la personne accueillie et de l'etablissement. Le projet individualise est plus concret encore : il traduit les besoins, les attentes et le projet de vie de la personne en actions quotidiennes, avec des objectifs adaptes et des modalites de suivi. Les trois documents sont emboites : le projet d'etablissement donne le cadre, le contrat de sejour l'engage juridiquement et le projet individualise le rend concret pour chaque personne. L'accompagnant doit connaitre ces documents pour agir dans le cadre et respecter les droits de la personne.",
     "On attend les trois niveaux, leur portee et leur articulation."),
 QT("Comment la démarche qualité contribue-t-elle à la sécurité des personnes accompagnées ?",
     "La demarche qualite identifie les risques et les points faibles de l'organisation, puis met en place des actions correctives. Elle s'appuie sur des procedures ecrites : hygiene des mains, transferts, distribution des repas, transmissions et gestion des incidents. Elle utilise des indicateurs, par exemple le nombre de chutes, d'escarres ou de plaintes, et des audits pour mesurer l'ecart entre les procedures et la pratique reelle. Les retours d'experience apres un evenement indesirable permettent de comprendre les causes plutot que de chercher un coupable. La personne accompagnee et sa famille y participent par le conseil de la vie sociale et les enquetes de satisfaction. Pour l'accompagnant, la qualite n'est pas un document administratif : c'est la rigueur quotidienne dans les gestes, les transmissions et le signalement des anomalies.",
     "On attend procedures, indicateurs, audits, retours d'experience et participation des usagers.")],
C("L'établissement fournit un cadre contractualisé et une organisation de la qualité ; l'accompagnant agit dans ce cadre et le fait vivre.",
  "projet d'établissement · contrat de séjour · projet individualisé",
  "CVS · règlement intérieur · démarche qualité · gestion des risques",
  "Établissement~Structure d'accueil~Contrat de séjour~Engagement réciproque~Projet individualisé~Accompagnement personnalisé~Conseil de la vie sociale~Participation des usagers~Qualité~Amélioration continue",
  "Connaître le cadre~Respecter les procédures~Appliquer le projet individualisé~Signaler les écarts~Participer à l'évaluation",
  "Ignorer le contrat de séjour|Imposer le règlement sans écoute|Ne pas signaler un incident|Confondre projet collectif et projet individuel",
  "EHPAD~Hébergement de personnes âgées~CASF~Code de référence~Contrat~Droits et prestations~CVS~Instance de participation~Indicateur~Mesure de la qualité",
  "Projet d'établissement~Orientation collective~Projet individualisé~Réponse personnelle",
  "Règlement intérieur~Vie collective~Contrat de séjour~Engagement individuel"))

# FIN DES LOTS
valider_et_ecrire(F, "pro-sante-mat-part-B.json")
