# -*- coding: utf-8 -*-
"""Generateur st2s-mat-part-B.json — lot B : biologie/physiopathologie (11) et SST (9).

ST2S, lycee technologique. 20 fiches prototype : 12 points, 9 questions
(7 QCM + 2 texte), 7 blocs ordonnes, 3 schemas SVG. Aucune integration.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_etapes,
                      svg_compare, bloc, valider_et_ecrire)

FIL = ["st2s"]
REF = (
    "Programmes de la voie technologique ST2S : arrete du 21 juillet 2011 fixant les programmes "
    "d'enseignement du baccalaureat technologique ST2S (Bulletin officiel special n 6 du 29 septembre 2011), "
    "programmes renoves applicables a la rentree 2020 (Bulletin officiel special n 7 du 25 juillet 2019) ; "
    "matieres : Biologie et physiopathologie humaine et Sciences et techniques sanitaires et sociales ; "
    "ressources eduscol (programmes ST2S, accompagnements pedagogiques et fiches de cours)."
)

F = []


def S(x):
    return [p.strip() for p in x.split("|") if p.strip()]


def R(x):
    return [p.strip() for p in x.split("~") if p.strip()]


def Q(question, options, correct, correction):
    return qcm(question, R(options), correct, correction)


def T(question, reponse, correction):
    return qt(question, reponse, correction)


def _grid(x):
    cellules = R(x)
    if "|" not in x:
        return [cellules[i:i + 3] for i in range(0, 9, 3)]
    return [R(ligne) for ligne in S(x)]


def _cmp(x):
    cellules = R(x)
    n = len(cellules) // 2
    return (cellules[0], cellules[1:n]), (cellules[n], cellules[n + 1:])


def C(idea, eq, leg, grid, steps, traps, ex, cmp1, cmp2):
    return {"idea": idea, "eq": eq, "leg": leg, "grid": _grid(grid),
            "steps": S(steps), "traps": S(traps), "ex": [R(e) for e in S(ex)],
            "cmp": (_cmp(cmp1), _cmp(cmp2))}


def add(prefix, titre, matiere, annees, points, questions, c):
    titre_complet = prefix + " · " + titre
    short = titre.split(":")[0].strip()
    aff = [
        bloc("L'idee en une phrase", texte=c["idea"], type="intro"),
        bloc("La notion a maitriser", eq=c["eq"], leg=c["leg"], type="formule"),
        bloc("Tableau de lecture", items=c["grid"], type="grille"),
        bloc("Les points essentiels du chapitre", items=points[1:5], type="liste"),
        bloc("La demarche pas a pas", items=c["steps"], type="etapes"),
        bloc("Pieges et erreurs frequentes", items=c["traps"], type="attention"),
        bloc("En situation : exemples concrets", items=[
            "%s : <span class=\"cle\">%s</span>" % (p[0], p[1]) for p in c["ex"]
        ], type="exemples"),
    ]
    schema = [
        diag("1 · " + short, svg_grille(short, ["Notion", "Definition", "Repere"], c["grid"])),
        diag("2 · Demarche", svg_etapes("Procedure : " + short, c["steps"])),
        diag("3 · A distinguer", svg_compare(short, c["cmp"][0], c["cmp"][1])),
    ]
    assert len(points) == 12, prefix
    assert len(questions) == 9, prefix
    assert sum(1 for q in questions if q.get("type") == "qcm") == 7, prefix
    assert sum(1 for q in questions if q.get("type") == "texte") == 2, prefix
    assert len(aff) == 7 and len(schema) == 3, prefix
    F.append(fiche(FIL, annees, matiere, titre_complet, REF, points, questions, aff, schema))


BIO = "Biologie et physiopathologie humaine"
STT = "Sciences et techniques sanitaires et sociales"

# ============================================================ BIO1
add("ST2S-B-BIO01", "Organisation du corps humain : cellules, tissus et appareils", BIO, ["1re"],
S("Le corps humain est organise en niveaux emboites : cellules, tissus, organes et appareils."
  "|La cellule est l'unite de base ; chez l'humain, elle possede un noyau et des organites specialises."
  "|Un tissu est un ensemble de cellules de meme origine qui assurent une fonction commune."
  "|Les quatre grands tissus sont epithelial, conjonctif, musculaire et nerveux."
  "|Le tissu epithelial recouvre les surfaces et forme des glandes ; il assure protection et absorption."
  "|Le tissue conjonctif comprend le sang, le cartilage, l'os et la graisse : il soutient et relie."
  "|Le tissu musculaire assure le mouvement grace a la contraction des fibres."
  "|Le tissu nerveux transmet des messages sous forme de signaux electriques et chimiques."
  "|Un organe associe plusieurs tissus pour remplir une fonction precise, comme l'estomac ou le poumon."
  "|Un appareil, ou systeme, regroupe des organes qui cooperent : digestif, respiratoire, circulatoire, nerveux."
  "|L'homeostasie est le maintien de constantes internes comme la temperature, le pH et la glycemie."
  "|Cette organisation en niveaux sert de cadre a l'etude de toute pathologie et de tout soin."),
[Q("Quel est le premier niveau d'organisation du corps humain ?", "Le tissu~La cellule~L'organe~L'appareil", 1,
    "La cellule est l'unite structurale et fonctionnelle de base."),
 Q("Combien existe-t-il de grands tissus fondamentaux ?", "Deux~Trois~Quatre~Six", 2,
    "On distingue les tissus epithelial, conjonctif, musculaire et nerveux."),
 Q("Quel tissu assure la transmission des messages nerveux ?", "Epithelial~Conjonctif~Musculaire~Nerveux", 3,
    "Le tissu nerveux est specialise dans la reception et la transmission des signaux."),
 Q("A quel tissu appartient le sang ?", "Epithelial~Conjonctif~Musculaire~Nerveux", 1,
    "Le sang est un tissu conjonctif liquide dont la matrice est le plasma."),
 Q("Quelle est la fonction principale du tissu epithelial ?", "Transmettre des signaux~Recouvrir et proteger les surfaces~Contracturer~Stocker la graisse", 1,
    "Les epitheliums tapissent les surfaces internes et externes et forment des glandes."),
 Q("Quel ensemble forme un appareil ?", "Une seule cellule~Plusieurs organes cooperants~Un seul tissu~Un seul organite", 1,
    "Un appareil associe des organes qui concourent a une meme fonction."),
 Q("Que designe l'homeostasie ?", "Une maladie~Le maintien des constantes internes~Une division cellulaire~Une reaction immunitaire", 1,
    "L'homeostasie maintient la temperature, le pH, la glycemie dans des limites etroites."),
 T("Décrire les niveaux d'organisation qui relient la cellule musculaire a l'appareil locomoteur.",
    "La cellule musculaire, ou fibre musculaire, est specialisee dans la contraction. Un groupe de fibres forme un tissu musculaire, associe a du tissu conjonctif qui apporte sang et nerfs. Plusieurs tissus forment un muscle, qui est un organe. Les muscles, les os et les articulations constituent l'appareil locomoteur, avec le systeme nerveux qui commande le mouvement. Chaque niveau ajoute une propriete nouvelle : contraction, force, deplacement et coordination.",
    "On attend la succession cellule, tissu, organe, appareil et un exemple concret."),
 T("Expliquer pourquoi une perturbation de l'homeostasie peut avoir des consequences graves.",
    "Les enzymes et les proteines ne fonctionnent correctement que dans une plage etroite de temperature et de pH. Si la glycemie devient trop elevee ou trop basse, le cerveau et les autres organes ne recoivent plus l'energie adaptee. Les mecanismes de regulation, comme la transpiration, la soif ou la secretion d'insuline, ramenent les valeurs a la normale. Lorsqu'ils sont depasses, par exemple lors d'un choc ou d'une acidose, les fonctions vitales s'alterent rapidement. C'est pourquoi les parametres vitaux sont surveilles en milieu de soin.",
    "La reponse doit relier homeostasie, enzymes, exemples de constantes et surveillance clinique.")],
C("Le corps est une hierarchie de structures imbriquees, de la cellule a l'appareil, maintenue en equilibre par l'homeostasie.",
  "Cellule -> tissu -> organe -> appareil -> organisme",
  "4 tissus : epithelial, conjonctif, musculaire, nerveux · homeostasie : temperature, pH, glycemie",
  "Cellule~Unite de base~Tissu~Cellules de meme fonction~Organe~Plusieurs tissus~Appareil~Organes cooperants",
  "Identifier le niveau d'organisation|Nommer le tissu implique|Relier la structure a la fonction|Verifier le mecanisme de regulation|Relier a une pathologie ou un soin",
  "Confondre tissu et organe|Classer le sang hors des tissus|Oublier le role du tissu conjonctif|Croire que l'homeostasie est fixe et immuable",
  "Fibre musculaire~Cellule contractile~Sang~Tissu conjonctif liquide~Estomac~Organe~Appareil digestif~Ensemble d'organes",
  "Tissu epithelial~Protection et absorption~Tissu nerveux~Transmission des signaux",
  "Organe~Unite morphologique~Appareil~Ensemble fonctionnel"))

# ============================================================ BIO2
add("ST2S-B-BIO02", "Squelette, articulations et contraction musculaire", BIO, ["1re"],
S("Le squelette humain compte environ 206 os chez l'adulte."
  "|Il assure le soutien du corps, la protection des organes, le mouvement et la production de cellules sanguines."
  "|Les os sont des tissus conjonctifs mineralises, constitues de collagene et de sels de calcium."
  "|Le remodelage osseux associe formation par les osteoblastes et resorption par les osteoclastes."
  "|Une articulation relie deux os : les articulations mobiles sont pourvues de cartilage et d'une capsule."
  "|Les ligaments relient os a os ; les tendons relient muscle a os."
  "|Le cartilage articulaire reduit les frictions et amortit les chocs."
  "|Les muscles squelettiques sont stries et leur contraction est volontaire."
  "|La contraction resulte du glissement des filaments d'actine et de myosine, consommateur d'ATP et de calcium."
  "|Un muscle travaille en antagoniste d'un autre : quand l'un se contracte, l'autre se relache."
  "|Le biceps et le triceps forment un couple antagoniste classique du bras."
  "|La mobilisation et l'activite physique regulent la densite osseuse et la masse musculaire."),
[Q("Combien d'os compte environ le squelette d'un adulte ?", "106~146~206~306", 2,
    "Le squelette adulte compte environ 206 os, contre davantage chez le nourrisson."),
 Q("Quelle cellule construit l'os neuf ?", "L'osteoclaste~L'osteoblast~Le chondrocyte~Le globule rouge", 1,
    "Les osteoblastes forment la matrice osseuse ; les osteoclastes la resorbent."),
 Q("Quel element relie un muscle a un os ?", "Un ligament~Un tendon~Une membrane~Un cartilage", 1,
    "Le tendon relie le muscle a l'os ; le ligament relie deux os."),
 Q("Que reduit le cartilage articulaire ?", "La production de sang~Les frictions et les chocs~La conduction nerveuse~La glycemie", 1,
    "Le cartilage recouvre les surfaces articulaires et amortit les contraintes."),
 Q("Quel type de muscle est sous controle volontaire ?", "Le muscle cardiaque~Le muscle lisse~Le muscle squelettique~Tous les muscles", 2,
    "Les muscles squelettiques stries sont volontaires, contrairement aux muscles lisses et cardiaque."),
 Q("Quelle proteine se lie a la myosine lors de la contraction ?", "L'actine~Le collagene~La keratine~L'hemoglobine", 0,
    "Le glissement des filaments d'actine et de myosine produit la contraction."),
 Q("Comment appelle-t-on deux muscles aux actions opposees ?", "Synergiques~Antagonistes~Identiques~Conjugues", 1,
    "Biceps et triceps sont antagonistes : l'un flechit, l'autre etend le bras."),
 T("Expliquer le mecanisme de la contraction musculaire et le role de l'ATP.",
    "Un influx nerveux arrivant a la fibre musculaire provoque la liberte de calcium dans le cytoplasme. Le calcium permet l'interaction entre l'actine et la myosine. Les tetes de myosine se fixent sur l'actine et tirent les filaments les uns sur les autres : c'est le glissement. L'ATP est necessaire a la fois pour détacher la myosine de l'actine et pour realimenter la pompe qui ramene le calcium dans le reticule. Sans ATP, le muscle reste contracte, comme dans la rigidite cadaverique.",
    "On attend le role du calcium, du glissement actine-myosine et des deux usages de l'ATP."),
 T("Justifier l'importance de l'activite physique pour la sante osseuse et musculaire.",
    "Les contraintes mecaniques apportees par le poids du corps et les efforts stimulent les osteoblastes : l'os se remodele et sa densite augmente. En absence de charge, par exemple lors d'une immobilisation prolongee ou en apesanteur, la resorption depasse la formation et l'os se fragilise. Cote muscle, l'exercice entraine une hypertrophie des fibres et une meilleure endurance mitochondriale. Chez la personne agee, maintenir une activite adaptee reduit le risque de chute et de fracture, tout en preservant l'autonomie.",
    "On attend le lien contrainte-remodelage, les effets de l'immobilisation et la prevention des chutes.")],
C("Le mouvement resulte d'un systeme de leviers osseux mobilises par des muscles antagonistes sous commande nerveuse.",
  "Tension musculaire -> traction sur le tendon -> mobilisation de l'os",
  "Ligament : os-os · tendon : muscle-os · ATP et calcium : contraction",
  "Os~Soutien et protection~Articulation~Jonction mobile~Ligament~Relie deux os~Tendon~Relie muscle et os",
  "Repérer les os et l'articulation|Identifier les muscles antagonistes|Expliquer le glissement des filaments|Relier effort et remodelage osseux|Proposer une prevention des chutes",
  "Confondre ligament et tendon|Croire que la contraction consomme du calcium comme carburant|Oublier le role de l'ATP|Negliger le remodelage osseux",
  "Biceps~Fletchit le bras~Triceps~Etend le bras~Cartilage~Amortit l'articulation~206 os~Squelette adulte",
  "Muscle volontaire~Squelettique strie~Muscle involontaire~Lisse et cardiaque",
  "Osteoblaste~Forme l'os~Osteoclaste~Resorbe l'os"))

# ============================================================ BIO3
add("ST2S-B-BIO03", "Coeur et circulation sanguine : le systeme cardiovasculaire", BIO, ["1re", "Terminale"],
S("L'appareil circulatoire assure le transport du sang entre le coeur, les poumons et les organes."
  "|Le coeur est un muscle creux, le myocarde, divise en quatre cavités."
  "|Les oreillettes recolent le sang ; les ventricules l'eproulent sous pression."
  "|La circulation pulmonaire va du ventricule droit aux poumons et revient a l'oreillette gauche."
  "|La circulation systemique va du ventricule gauche aux organes et revient a l'oreillette droite."
  "|Le sang pauvre en oxygene est veineux dans la circulation systemique et arteriel dans la pulmonaire."
  "|Les arteres conduisent le sang loin du coeur, les veines le ramènent ; les capillaires permettent les echanges."
  "|Les valvules cardiaques imposent un sens de circulation unique et empechent le reflux."
  "|Le rythme cardiaque est commande par le noeud sinusal et module par le systeme nerveux et les hormones."
  "|La pression arterielle s'exprime en millimetres de mercure, avec une valeur systolique et une diastolique."
  "|Le sang transporte oxygene, nutriments, hormones, cellules immunitaires et dechets comme le CO2."
  "|Une obstruction ou une rupture vasculaire peut provoquer un infarctus ou un accident vasculaire cerebral."),
[Q("Combien de cavites possede le coeur humain ?", "Deux~Trois~Quatre~Cinq", 2,
    "Le coeur comprend deux oreillettes et deux ventricules."),
 Q("Quel ventricule envoie le sang vers les organes ?", "Le droit~Le gauche~Les deux~Aucun", 1,
    "Le ventricule gauche propulse le sang dans l'aorte et la circulation systemique."),
 Q("Que transporte une artere ?", "Le sang vers le coeur~Le sang loin du coeur~Seulement de l'oxygene~Seulement du CO2", 1,
    "Les arteres conduisent le sang du coeur vers les tissus, quel que soit son taux d'oxygene."),
 Q("Ou ont lieu les echanges entre sang et tissus ?", "Dans les arteres~Dans les veines~Dans les capillaires~Dans le myocarde", 2,
    "La paroi fine des capillaires permet la diffusion des gaz et des nutriments."),
 Q("Quel element impose le sens unique du flux sanguin dans le coeur ?", "Le myocarde~Les valvules~Le plasma~Les globules rouges", 1,
    "Les valvules s'opposent au reflux du sang."),
 Q("Que mesure la pression systolique ?", "La pression minimum~La pressure maximum lors de la contraction~Le rythme cardiaque~Le debit veineux", 1,
    "La systolique correspond a la pression arterielle maximale pendant la contraction ventriculaire."),
 Q("Quel critere definit le sang veineux dans la circulation systemique ?", "Riche en oxygene~Pauvre en oxygene et riche en CO2~Sans globules rouges~Plus chaud que le sang arteriel", 1,
    "Apres avoir alimente les tissus, le sang systemique est pauvre en O2 et charge de CO2."),
 T("Décrire le trajet d'une goutte de sang depuis l'oreillette droite jusqu'aux organes.",
    "L'oreillette droite recoit le sang veineux provenant des organes par les veines caves. Le sang passe dans le ventricule droit, puis dans l'artere pulmonaire vers les poumons ou il se charge en oxygene. Il revient par les veines pulmonaires dans l'oreillette gauche, passe dans le ventricule gauche, puis dans l'aorte et les arteres systemiques jusqu'aux organes. Les valvules empechent tout retour en arriere a chaque etape.",
    "On attend l'ordre des cavités et la distinction entre circulation pulmonaire et systemique."),
 T("Expliquer pourquoi la pression arterielle doit rester dans une plage etroite.",
    "Une pression trop basse, ou hypotension, ne perfuse pas suffisamment les organes et peut provoquer des etourdissements ou un choc. Une pression trop elevee, ou hypertension, use les parois arterielles et augmente le risque d'accident vasculaire cerebral, d'infarctus et d'insuffisance cardiaque. L'organisme la regule par le debit cardiaque, la resistance des vaisseaux, les reins et le systeme nerveux autonome. Sa mesure fait partie des parametres vitaux et son suivi est un enjeu majeur de prevention.",
    "On attend les risques dans les deux sens et les mecanismes de regulation.")],
C("Le coeur est une pompe a quatre cavités qui entretient deux circulations en serie : pulmonaire et systemique.",
  "Circulation : coeur droit -> poumons -> coeur gauche -> organes",
  "Oreillette : reception · ventricule : propulsion · valvule : sens unique",
  "Oreillette~Reception du sang~Ventricule~Propulsion sous pression~Capillaire~Echanges avec les tissus~Valvule~Anti-reflux",
  "Repérer le sens du flux|Nommer les cavités traversees|Distinguer les deux circulations|Mesurer les parametres cardiaques|Relier une anomalie a un risque",
  "Croire que toutes les arteres contiennent du sang oxygene|Confondre oreillette et ventricule|Oublier les valvules|Mélanger pression systolique et diastolique",
  "Ventricule gauche~Vers l'aorte~Poumons~Charge en O2~Aorte~Distribution systemique~PA~120/80 mmHg environ",
  "Artere~Sang sortant du coeur~Veine~Sang revenant au coeur",
  "Circulation pulmonaire~Coeur droit vers poumons~Circulation systemique~Coeur gauche vers organes"))

# ============================================================ BIO4
add("ST2S-B-BIO04", "Respiration, ventilation et echanges gazeux", BIO, ["1re"],
S("La respiration assure l'apport de dioxygene aux cellules et l'elimination du dioxyde de carbone."
  "|La ventilation pulmonaire est l'entrée et la sortie d'air dans les poumons."
  "|L'inspiration fait intervenir le diaphragme et les muscles intercostaux externes."
  "|A l'inspiration, le volume thoracique augmente et la pression intrapulmonaire diminue."
  "|L'expiration au repos est passive : les muscles se relachent et le volume thoracique diminue."
  "|L'air conduit par la trachee atteint les bronches puis les bronchioles et les alveoles."
  "|Les alveoles sont les unites d'echange : leur paroi fine est entouree de capillaires."
  "|La diffusion de l'oxygene va de l'alveole vers le sang, celle du CO2 du sang vers l'alveole."
  "|L'hemoglobine des globules rouges fixe l'oxygene et augmente la capacite de transport du sang."
  "|La frequence respiratoire au repos est d'environ 12 a 20 mouvements par minute chez l'adulte."
  "|La regulation des gaz du sang fait intervenir des centres nerveux bulbaires sensibles au CO2 et au pH."
  "|Une hypoxie ou une hypercapnie peuvent entrainer une detresse respiratoire et necessiter une prise en charge."),
[Q("Quel muscle principal intervient dans l'inspiration ?", "Le triceps~Le diaphragme~Le myocarde~Le muscle lisse intestinal", 1,
    "Le diaphragme se contracte et s'abaisse lors de l'inspiration."),
 Q("Que se passe-t-il lors de l'inspiration ?", "Le volume thoracique diminue~La pression intrapulmonaire diminue~Les poumons se vident~Le diaphragme se relache", 1,
    "L'augmentation de volume entraine une baisse de pression et l'entree d'air."),
 Q("Ou ont lieu les echanges gazeux ?", "Dans la trachee~Dans les bronches~Dans les alveoles~Dans la plèvre", 2,
    "Les alveoles, entourees de capillaires, sont le siege de la diffusion des gaz."),
 Q("Quelle proteine fixe l'oxygene dans le sang ?", "L'albumine~L'hemoglobine~L'actine~Le collagene", 1,
    "L'hemoglobine des globules rouges transporte l'oxygene sous forme d'oxyhemoglobine."),
 Q("Quel gaz diffuse du sang vers l'alveole ?", "L'oxygene~Le dioxyde de carbone~L'azote~L'helium", 1,
    "Le CO2 produit par les cellules est elimine dans les alveoles."),
 Q("Quelle est la frequence respiratoire habituelle d'un adulte au repos ?", "5 a 8~12 a 20~30 a 40~60 a 80", 1,
    "On compte environ 12 a 20 mouvements respiratoires par minute au repos."),
 Q("Que designe une hypoxie ?", "Un exces de CO2~Un defaut d'oxygene~Une pression arterielle haute~Une glycemie basse", 1,
    "L'hypoxie est une diminution de l'apport en oxygene aux tissus."),
 T("Expliquer le mecanisme de l'inspiration et celui de l'expiration au repos.",
    "A l'inspiration, le diaphragme se contracte et les muscles intercostaux externes soulèvent les cotes. Le volume de la cage thoracique augmente, la pression a l'interieur des poumons devient inferieure a la pression atmospherique et l'air entre. A l'expiration au repos, ces muscles se relachent, le diaphragme remonte, le volume diminue et la pression depasse la pression exterieure : l'air sort passivement. L'expiration forcee, lors d'un effort ou d'une toux, fait intervenir les muscles abdominaux et intercostaux internes.",
    "On attend le role des muscles, les variations de volume et de pression, et la passivite de l'expiration."),
 T("Justifier l'importance de la saturation en oxygene et de la capnie en surveillance clinique.",
    "La saturation en oxygene, mesuree par oxymetre de pouls, indique la proportion d'hemoglobine chargee en O2. Une valeur basse signale une hypoxie, qui peut etre silencieuse avant de provoquer des lesions. La capnie, ou pression partielle en CO2, renseigne sur l'efficacite de la ventilation : un CO2 eleve traduit une hypoventilation et une acidose respiratoire possible. Ces deux mesures, avec la frequence respiratoire, font partie des parametres vitaux. Leur surveillance permet de detecter precocement une detresse et d'adapter l'oxygenotherapie.",
    "La reponse doit distinguer oxygene et CO2 et relier les mesures a la detection d'une detresse.")],
C("La ventilation renouvelle l'air alveolaire ; la diffusion et l'hemoglobine assurent le transport des gaz.",
  "Inspiration : volume thoracique up, pression down, air in",
  "O2 : alveole vers sang · CO2 : sang vers alveole · SpO2 et capnie : surveillance",
  "Alveole~Unite d'echange~Diaphragme~Muscle inspiratoire~Hemoglobine~Transport de O2~Hypoxie~Defaut d'oxygene",
  "Observer les mouvements respiratoires|Expliquer la variation de pression|Localiser les echanges gazeux|Mesurer la frequence et la SpO2|Interpreter une anomalie",
  "Confondre ventilation et respiration cellulaire|Croire que l'expiration est toujours active|Oublier le role de l'hemoglobine|Mélanger hypoxie et hypercapnie",
  "Inspiration~Diaphragme contracte~Expiration~Relachement passif~Alveole~Paroi fine~SpO2~Saturation en oxygene",
  "Ventilation~Mouvements de l'air~Respiration cellulaire~Consommation de O2 par les cellules",
  "Hypoxie~Pas assez de O2~Hypercapnie~Trop de CO2"))

# ============================================================ BIO5
add("ST2S-B-BIO05", "Digestion, absorption et role des nutriments", BIO, ["1re"],
S("La digestion transforme les aliments en nutriments absorbables par l'intestin."
  "|Le tube digestif comprend la bouche, l'oesophage, l'estomac, l'intestin grele et le gros intestin."
  "|La mastication et la salive débutent la digestion mecanique et chimique de l'amidon."
  "|L'estomac malaxe le bol alimentaire et secrete de l'acide chlorhydrique et des enzymes proteolytiques."
  "|Le foie produit la bile, qui emulsifie les lipides et facilite leur digestion."
  "|Le pancreas secrete des enzymes digestives et du bicarbonate qui neutralise l'acidite du chyme."
  "|L'intestin grele est le principal lieu d'absorption grace a ses villosites et microvillosites."
  "|Les glucose et acides amines passes dans le sang rejoignent le foie par la veine porte."
  "|Les lipides sont transportes dans la lymphe sous forme de chylomicrons."
  "|Les glucides fournissent de l'energie rapide, les lipides une energie de reserve et les proteines des acides amines."
  "|Les vitamines et les sels mineraux sont indispensables au metabolisme sans apporter d'energie, et les fibres favorisent le transit et la satiete."
  "|Une digestion ou une absorption perturbee entraine des carences, des diarrhees ou des malnutrition."),
[Q("Quel organe produit la bile ?", "L'estomac~Le foie~Le pancreas~La rate", 1,
    "La bile est sekretee par le foie et stockee dans la vesicule biliaire."),
 Q("Quel est le principal lieu d'absorption des nutriments ?", "L'estomac~L'intestin grele~Le gros intestin~L'oesophage", 1,
    "Les villosites de l'intestin grele offrent une grande surface d'absorption."),
 Q("Quelle enzyme salivary commence la digestion de l'amidon ?", "La pepsine~L'amylase~La lipase~La trypsine", 1,
    "L'amylase salivaire hydrolyse l'amidon en sucres plus simples."),
 Q("Que neutralise le bicarbonate pancreatique ?", "La bile~L'acidite du chyme~Les lipides~Les fibers", 1,
    "Le bicarbonate alcalin neutralise l'acide chlorhydrique gastrique."),
 Q("Comment les lipides absorbes sont-ils transportes ?", "Dans le sang directement~Dans la lymphe sous forme de chylomicrons~Dans la bile~Dans l'urine", 1,
    "Les chylomicrons passent dans les capillaires lymphatiques avant d'atteindre le sang."),
 Q("Quel nutriment fournit une energie rapide ?", "Le glucose~La vitamine C~Le calcium~Les fibres", 0,
    "Le glucose est la source d'energie immediate des cellules."),
 Q("Quel est le role des fibres alimentaires ?", "Apporter de l'energie immediate~Favoriser le transit et la satiete~Synthetiser des hormones~Digérer les lipides", 1,
    "Les fibres augmentent le volume des selles et ralentissent l'absorption des sucres."),
 T("Decrire le parcours d'un repas depuis la bouche jusqu'au sang.",
    "Dans la bouche, la mastication et l'amylase salivaire dechiquetent et commencent a digerer l'amidon. Le bol descend dans l'oesophage puis arrive dans l'estomac, ou l'acide et la pepsine digerent les proteines. Le chyme passe dans le duodenum : la bile emulsifie les lipides et le pancreas fournit enzymes et bicarbonate. Dans l'intestin grele, les villosites absorbent glucose et acides amines vers le sang et les lipides vers la lymphe. Le gros intestin reabsorbe l'eau et forme les selles.",
    "On attend l'ordre des organes, les secretions et la distinction sang et lymphe."),
 T("Expliquer les consequences d'une malabsorption des lipides.",
    "Une malabsorption des lipides, par exemple apres une intervention sur l'intestin ou en cas de defaut de bile, entraine des selles grasses et abondantes, appelees steatorrhee. Elle provoque un deficit energetique car les lipides sont la source la plus concentree d'energie, et une carence en vitamines liposolubles A, D, E et K. La vitamine D etant impliquee dans l'absorption du calcium, une osteoporose peut apparaitre a long terme. La prise en charge repose sur un regime adapte et parfois des suppléments.",
    "On attend steatorrhee, deficit calorique, carences en vitamines liposolubles et consequence osseuse.")],
C("La digestion rend les aliments absorbables ; l'intestin grele transfert les nutriments vers le sang ou la lymphe.",
  "Aliments -> nutriments -> sang / lymphe -> cellules",
  "Bile : lipides · amylase : amidon · pepsine : proteines · villosites : absorption",
  "Bouche~Mastication et amylase~Estomac~Acide et pepsine~Intestin grele~Absorption~Foie~Production de bile",
  "Suivre le trajet des aliments|Identifier les secretions|Localiser l'absorption|Classer les nutriments|Relier une malabsorption a une carence",
  "Croire que la bile digere directement les lipides|Confondre sang et lymphe pour les lipides|Oublier le role des villosites|Negliger les vitamines liposolubles",
  "Amylase~Digere l'amidon~Bile~Emulsifie les lipides~Villosites~Surface d'absorption~Chylomicrons~Transport des lipides",
  "Digestion mecanique~Mastication et malaxage~Digestion chimique~Action des enzymes",
  "Glucose~Energie rapide~Lipides~Reserve energetique"))

# ============================================================ BIO6
add("ST2S-B-BIO06", "Rein, nephron et equilibre hydrique de l'organisme", BIO, ["1re", "Terminale"],
S("Les reins filtrent le sang, eliminent les dechets et maintiennent l'equilibre hydrique et mineral."
  "|Chaque rein contient environ un million de nephrons, unite fonctionnelle du rein."
  "|Le nephron comprend le glomerule, la capsule de Bowman, le tube proximal, l'anse de Henle et le tube distal."
  "|La filtration glomerulaire laisse passer l'eau et les petites molecules, mais retient les cellules et les proteines."
  "|Le filtrat glomerulaire est ensuite modifie par reabsorption et secretion le long du tubule."
  "|L'eau et le glucose sont reabsorpes en grande partie dans le tube proximal."
  "|L'anse de Henle cree un gradient de concentration qui permet de concentrer l'urine."
  "|La regulation du volume urinaire fait intervenir l'hormone antidiuretique et l'aldosterone."
  "|L'ADH augmente la reabsorption d'eau dans le tube collecteur."
  "|L'aldosterone favorise la reabsorption du sodium et l'excretion du potassium."
  "|Les reins participent aussi au maintien du pH sanguin en eliminating les ions H+ et en regenerant des bicarbonates."
  "|Une insuffisance renale entraine une accumulation de dechets, des troubles du potassium et de l'hydratation."),
[Q("Quelle est l'unite fonctionnelle du rein ?", "L'alveole~Le nephron~Le lobule~Le canon", 1,
    "Chaque rein est constitue d'environ un million de nephrons."),
 Q("Qu'est-ce qui est retenu lors de la filtration glomerulaire ?", "L'eau~Le glucose~Les cellules et les proteines~Les ions sodium", 2,
    "La barriere de filtration retient les cellules sanguines et les macromolecules."),
 Q("Ou est reabsorbe la plus grande partie du glucose filtre ?", "Dans le tube proximal~Dans l'anse de Henle~Dans le tube collecteur~Dans la vesicule", 0,
    "Le tube proximal reabsorbe la quasi-totalite du glucose et d'une grande partie de l'eau."),
 Q("Quel role joue l'anse de Henle ?", "Produire de l'urine sans sel~Creer un gradient de concentration~Filtrer les proteines~Synthetiser l'ADH", 1,
    "Le contre-courant de l'anse permet de concentrer l'urine."),
 Q("Que fait l'hormone antidiuretique ?", "Augmente l'excretion d'eau~Augmente la reabsorption d'eau~Diminue le sodium~Stimule la soif uniquement", 1,
    "L'ADH rend le tube collecteur plus permeable a l'eau."),
 Q("Quel ion est reabsorbe sous l'effet de l'aldosterone ?", "Le potassium~Le sodium~Le calcium~Le magnesium", 1,
    "L'aldosterone favorise la reabsorption du sodium et l'excretion du potassium."),
 Q("Quelle consequence d'une insuffisance renale ?", "Une urine tres diluee jamais~Une accumulation de dechets et de potassium~Une glycemie toujours basse~Une disparition de la soif", 1,
    "La reduction du filtration entraine uremie, hyperkaliemie et troubles hydriques."),
 T("Decrire les trois etapes de la formation de l'urine dans le nephron.",
    "La filtration glomerulaire produit un filtrat d'eau et de petites molecules dans la capsule de Bowman, tandis que les cellules et les proteines restent dans le sang. La reabsorption tubulaire recupere l'essentiel de l'eau, du glucose et des ions utiles vers le sang. La secretion tubulaire ajoute au filtrat des substances comme les ions H+, les medicaments ou l'ammoniac. Le liquide final, l'urine, s'ecoule dans le tube collecteur puis vers les ureteres et la vessie.",
    "On attend filtration, reabsorption et secretion dans le bon ordre, avec un exemple pour chacune."),
 T("Expliquer comment les reins contribuent au maintien de l'homeostasie.",
    "Les reins ajustent le volume et la composition du sang : ils eliminent l'urée et la creatinine, regulates l'eau grace a l'ADH, le sodium grace a l'aldosterone et le potassium grace au tube distal. Ils participent a l'equilibre acidobasique en excretant les ions H+ et en regenerant des bicarbonates. Ils interviennent aussi dans la pression arterielle par le systeme renine-angiotensine et dans la production d'erythropoietine, qui stimule la formation des globules rouges. Leurrole est donc central dans l'homeostasie et explique la gravite de l'insuffisance renale.",
    "On attend eau,electrolytes, pH, pression arterielle et erythropoietine.")],
C("Le nephron filtre le sang puis ajuste le filtrat par reabsorption et secretion pour former l'urine.",
  "Filtration + reabsorption + secretion = urine",
  "ADH : eau · aldosterone : sodium · anse de Henle : gradient de concentration",
  "Glomerule~Filtration du sang~Tube proximal~Reabsorption~Anse de Henle~Concentration~ADH~Eau reabsorbe",
  "Repérer les parties du nephron|Depeindre la filtration|Suivre la reabsorption|Identifier les hormones|Relier une insuffisance aux troubles observes",
  "Confondre filtration et reabsorption|Croire que le glucose est excrete normalement|Oublier le role de l'ADH|Negliger le potassium dans l'insuffisance renale",
  "Nephron~Unite du rein~Uree~Dechet azote~ADH~Hormone antidiuretique~Aldosterone~Hormone du sodium",
  "Filtration~Sang vers capsule~Reabsorption~Tubule vers sang",
  "Urine concentree~Beaucoup d'ADH~Urine diluee~Peu d'ADH"))

# ============================================================ BIO7
add("ST2S-B-BIO07", "Systeme nerveux, neurone et transmission du message", BIO, ["1re", "Terminale"],
S("Le systeme nerveux assure la reception, le traitement et la transmission des informations."
  "|Il se divise en systeme nerveux central, encephale et moelle epiniere, et en systeme peripherique."
  "|Le systeme peripherique comprend les nerfs sensitifs, les nerfs moteurs et le systeme nerveux autonome."
  "|Le neurone est la cellule nerveuse, composee d'un soma, de dendrites et d'un axone."
  "|Les dendrites recolent les signaux ; l'axone conduit l'influx vers les cellules cibles."
  "|L'influx nerveux est un potentiel d'action, variation rapide du potentiel electrique de la membrane."
  "|Sa propagation repose sur l'ouverture successive de canaux au sodium puis au potassium."
  "|La gaine de myeline accelere la conduction en permettant une propagation saltatoire."
  "|La synapse est la jonction entre deux neurones ou entre un neurone et un muscle."
  "|Un neurotransmetteur est libere par le neurone presynaptique puis fixe sur des recepteurs postsynaptiques."
  "|L'acetylcholine, la dopamine, le GABA et la serotonine sont des exemples de neurotransmetteurs."
  "|Une lesion localisee du cerveau ou de la moelle entraine des deficits moteurs ou sensitifs precis."),
[Q("Quelle partie du neurone recoit les signaux ?", "L'axone~Les dendrites~La myeline~Le bouton terminal", 1,
    "Les dendrites collectent les messages vers le soma ; l'axone les transmet."),
 Q("Qu'appelle-t-on un potentiel d'action ?", "Un repos membranaire~Une variation rapide du potentiel de membrane~Une secretion hormonale~Une contraction musculaire", 1,
    "Le potentiel d'action est le signal electrique qui se propage le long de l'axone."),
 Q("Quel ion entre dans le neurone au debut du potentiel d'action ?", "Le potassium~Le sodium~Le calcium~Le magnesium", 1,
    "L'ouverture des canaux sodium provoque la depolarisation."),
 Q("Quel role joue la myeline ?", "Freiner la conduction~Accelerer la conduction~Produire des neurotransmetteurs~Stocker l'ATP", 1,
    "La myeline permet une conduction saltatoire, beaucoup plus rapide."),
 Q("Qu'est-ce qu'une synapse ?", "Une cellule du sang~Une jonction entre deux cellules nerveuses~Un muscle~Une glande", 1,
    "La synapse assure la transmission du message d'un neurone a l'autre."),
 Q("Que libere le neurone presynaptique ?", "Un enzyme digestif~Un neurotransmetteur~Une hormone thyroidienne~Un globule rouge", 1,
    "Le neurotransmetteur traverse la fente synaptique et se fixe sur des recepteurs."),
 Q("Quel systeme regule la digestion et la frequence cardiaque sans controle volontaire ?", "Le systeme nerveux central~Le systeme nerveux autonome~Le systeme musculaire~Le systeme osseux", 1,
    "Le systeme nerveux autonome comprend les branches sympathique et parasympathique."),
 T("Decrire le trajet d'un message nerveux depuis une stimulation jusqu'a la reponse musculaire.",
    "Un recepteur sensoriel transforme un stimulus en signal electrique. Ce signal remonte par un nerf sensitif jusqu'a la moelle ou l'encéphale, ou il est traite. Un neurone moteur emet alors un potentiel d'action le long de son axone jusqu'a la synapse neuromusculaire. L'acetylcholine liberee se fixe sur les recepteurs de la fibre musculaire et declenche sa contraction. Le message peut etre module a chaque synapse par des neurotransmetteurs excitateurs ou inhibiteurs.",
    "On attend recepteur, nerf sensitif, centre, nerf moteur, synapse et muscle."),
 T("Expliquer pourquoi la destruction de la myeline perturbe les mouvements.",
    "La myeline isolant l'axone, le potentiel d'action saute d'un noeud de Ranvier a l'autre. Sans myeline, la conduction devient lente, voire s'interrompt, car les canaux ioniques ne sont plus concentres aux bons endroits. Les messages moteurs arrivent tardivement ou pas du tout, ce qui entraine une faiblesse, des tremblements ou une perte de coordination. C'est le mecanisme de la sclérose en plaques, ou la demyelinisation touche le systeme nerveux central.",
    "On attend le lien entre myeline, vitesse de conduction et symptomes moteurs.")],
C("Le systeme nerveux traite l'information grace a des neurones qui communiquent par signaux electriques et chimiques.",
  "Stimulus -> recepteur -> influx -> synapse -> effecteur",
  "Potentiel d'action : Na+ puis K+ · myeline : conduction saltatoire",
  "Neurone~Cellule nerveuse~Axone~Conduit l'influx~Synapse~Jonction chimique~Neurotransmetteur~Messager synaptique",
  "Identifier le type de neurone|Suivre le trajet du message|Depeindre le potentiel d'action|Expliquer le role synaptique|Relier une lesion a un symptome",
  "Confondre dendrites et axone|Croire que l'influx est un courant continu|Oublier le role des neurotransmetteurs|Negliger la myeline",
  "Dendrite~Reception~Axone~Transmission~Acetylcholine~Transmetteur moteur~Myeline~Isolant conducteur",
  "Systeme nerveux central~Encephale et moelle~Systeme peripherique~Nerfs et ganglions",
  "Neurone sensitif~Vers le centre~Neurone moteur~Vers le muscle"))

# ============================================================ BIO8
add("ST2S-B-BIO08", "Systeme endocrinien, hormones et regulation", BIO, ["1re", "Terminale"],
S("Le systeme endocrinien regule de nombreuses fonctions par la secretion d'hormones."
  "|Une hormone est un messager chimique produit par une glande et transporte par le sang."
  "|Les glandes endocrines n'ont pas de canal : elles libèrent leur produit directement dans le sang."
  "|L'hormone agit sur des cellules cibles possedant des recepteurs specifiques."
  "|La reponse d'une cellule cible depend de la concentration de l'hormone et du nombre de recepteurs."
  "|L'insuline, secretee par le pancreas, fait baisser la glycemie en favorisant l'entree du glucose dans les cellules."
  "|Le glucagon, aussi pancreatique, fait monter la glycemie en stimulant la glycogenolyse hepatique."
  "|La thyroidienne thyroxine augmente le metabolisme de base et la production de chaleur."
  "|Le cortisol, secrete par la surrenal, aide a repondre au stress et eleve la glycemie."
  "|L'adrenaline prepar l'organisme a l'effort : augmentation du rythme cardiaque et de la glycemie."
  "|La regulation hormonale fonctionne souvent par retroaction negative, comme un thermostat."
  "|Un deficit ou un exces hormonal provoque une pathologie endocrine, par exemple le diabete ou l'hyperthyroidie."),
[Q("Qu'est-ce qu'une hormone ?", "Un enzyme digestif~Un messager chimique transporte par le sang~Une cellule immunitaire~Un neurotransmetteur de la synapse", 1,
    "L'hormone est secrétée par une glande et agit sur des cellules cibles."),
 Q("Quelle hormone fait baisser la glycemie ?", "Le glucagon~L'insuline~Le cortisol~L'adrenaline", 1,
    "L'insuline favorise le stockage du glucose et son entree dans les cellules."),
 Q("Quel organe secrete l'insuline et le glucagon ?", "Le foie~Le pancreas~La thyroide~La surrenale", 1,
    "Les cellules des ilots de Langerhans pancreatiques secreent ces deux hormones."),
 Q("Que possede une cellule cible d'une hormone ?", "Un noyau supplementaire~Des recepteurs specifiques~Une membrane plus epaisse~Plus de mitochondries", 1,
    "La presence de recepteurs specifiques determine la sensibilite de la cellule."),
 Q("Quel effet a la thyroxine sur l'organisme ?", "Elle abaisse la glycemie~Elle augmente le metabolisme de base~Elle digere les lipides~Elle forme des os", 1,
    "Les hormones thyroidiennes accelerent le metabolisme et la thermogenese."),
 Q("Comment fonctionne le plus souvent la regulation hormonale ?", "Par retroaction positive~Par retroaction negative~Sans controle~Par le seul hasard", 1,
    "Un exces d'hormone inhibe sa propre secretion : c'est une boucle de retroaction negative."),
 Q("Quelle hormone prepare l'organisme a un effort ou un stress immediat ?", "L'insuline~L'adrenaline~La melatonine~La thyroxine", 1,
    "L'adrenaline secretee par la medullosurrenale accelere le coeur et mobilise le glucose."),
 T("Expliquer la regulation de la glycemie par l'insuline et le glucagon.",
    "Apres un repas, la glycemie augmente. Les cellules beta du pancreas secreent de l'insuline, qui favorise l'entree du glucose dans les cellules musculaires et adipeuses et sa transformation en glycogene dans le foie : la glycemie redescend. A jeun, la glycemie baisse et les cellules alpha secreent du glucagon, qui stimule la glycogenolyse et la neoglucogenese hepatiques : la glycemie remonte. Ces deux hormones antagonistes maintiennent la glycemie dans une plage etroite, grâce a une retroaction negative.",
    "On attend les deux hormones antagonistes, leurs effets et le principe de retroaction."),
 T("Distinguer une glande endocrine d'une glande exocrine et donner un exemple de chaque.",
    "Une glande endocrine libere son produit directement dans le sang, sans canal : c'est le cas de la thyroide ou du pancreas endocrine. Une glande exocrine secrete son produit a la surface d'un epithelium ou dans un canal : les glandes salivaires, sudoripares et le pancreas exocrine en sont des exemples. Le pancreas illustre bien la difference : ses ilots endocrines secreent insuline et glucagon dans le sang, tandis que ses cellules acineuses exocrines envoient des enzymes digestives dans le duodenum.",
    "On attend la definition des deux types et un exemple clair, de preference le pancreas.")],
C("Les hormones sont des messagers chimiques du sang ; elles reglent les fonctions par retroaction negative.",
  "Glande endocrine -> hormone -> sang -> cellule cible -> reponse",
  "Insuline : baisse glycemie · glucagon : hausse · thyroxine : metabolisme",
  "Hormone~Messager chimique~Glande endocrine~Secretion dans le sang~Cellule cible~Porteuse de recepteurs~Retroaction negative~Autorregulation",
  "Identifier la glande et l'hormone|Trouver la cellule cible|Decrire l'effet|Verifier la boucle de regulation|Relier un dereglement a une pathologie",
  "Confondre hormone et enzyme|Croire que toutes les glandes ont un canal|Oublier les recepteurs|Mélanger insuline et glucagon",
  "Insuline~Baisse de la glycemie~Glucagon~Hausse de la glycemie~Thyroxine~Metabolisme de base~Cortisol~Reponse au stress",
  "Glande endocrine~Pas de canal~Glande exocrine~Canal ou surface",
  "Retroaction negative~Stabilise~Retroaction positive~Amplifie"))

# ============================================================ BIO9
add("ST2S-B-BIO09", "Immunite, defenses naturelles et acquises", BIO, ["Terminale"],
S("Le systeme immunitaire defend l'organisme contre les agents pathogenes et les cellules anormales."
  "|Les defenses naturelles, ou innees, agissent immediatement et ne sont pas specifiques."
  "|La peau et les muqueuses constituent la premiere barriere physique et chimique."
  "|La flore residente limite l'implantation des microbes pathogenes par concurrence."
  "|Les phagocytes, dont les macrophages, englobent et digerent les particules etrangeres."
  "|L'inflammation est une reaction locale de defense, avec rougeur, chaleur, gonflement et douleur."
  "|Les defenses acquises, ou adaptatives, apparaissent apres un contact avec un antigen."
  "|Les lymphocytes B produisent des anticorps qui reconnaissent specifiquement un antigen."
  "|Les lymphocytes T detectent et eliminent les cellules infectees ou anormales."
  "|La reaction immunitaire secondaire est plus rapide et plus intense grâce aux cellules memoire."
  "|C'est le principe de la vaccination : presenter un antigen sans provoquer la maladie, avec un agent attenue, inactive ou un simple fragment."
  "|Une immunodepression ou une allergy traduisent un dysfonctionnement du systeme immunitaire."),
[Q("Quelle est la premiere barriere contre les agents pathogenes ?", "Le sang~La peau et les muqueuses~Le systeme nerveux~Les muscles", 1,
    "La peau et les muqueuses empechent physiquement et chimiquement l'entree des microbes."),
 Q("Quel cellule realise la phagocytose ?", "Le lymphocyte B~Le macrophage~Le globule rouge~L'osteoblaste", 1,
    "Les macrophages et les polynucleaires englobent et digerent les particules etrangeres."),
 Q("Que produisent les lymphocytes B ?", "Des enzymes digestives~Des anticorps~De l'insuline~Des hormones", 1,
    "Les plasmocytes, issus des lymphocytes B, secretent des anticorps specifiques."),
 Q("Quel role des lymphocytes T ?", "Produire des anticorps~Eliminer les cellules infectees~Transporter l'oxygene~Digérer les lipides", 1,
    "Les lymphocytes T cytotoxiques reconaissent et detruisent les cellules anormales."),
 Q("Qu'appelle-t-on une reaction immunitaire secondaire ?", "La premiere reaction a un antigen~Une reponse plus rapide apres un nouveau contact~Une reaction sans antigen~Une reaction allergique uniquement", 1,
    "Les cellules memoire rendent la deuxieme reponse plus rapide et plus forte."),
 Q("Sur quoi repose le principe de la vaccination ?", "Injecter des anticorps seulement~Presenter un antigen pour creer une memoire immunitaire~Supprimer le systeme immunitaire~Modifier le groupe sanguin", 1,
    "Le vaccin declenche une reponse primaire et laisse des cellules memoire."),
 Q("Quel signe n'appartient pas a l'inflammation ?", "Rougeur~Chaleur~Gonflement~Paleur et froid", 3,
    "L'inflammation associe rougeur, chaleur, gonflement, douleur et parfois perte de fonction."),
 T("Distinguer immunite innée et immunite acquise et expliquer leur complementarite.",
    "L'immunite innée est presente des la naissance : elle agit immediatement, sans specialisation, grace a la peau, aux muqueuses, a la flore et aux phagocytes. L'immunite acquise se developpe apres un contact avec un antigen : elle est specifique et repose sur les lymphocytes B et T. Elle est plus lente la premiere fois mais laisse une memoire immunitaire. Les deux systemes sont complementaires : les cellules innees presentent l'antigene aux lymphocytes et orchestrent la reponse adaptee, qui a son tour renforce la phagocytose.",
    "On attend immediat/specifique, cellules impliquees, memoire et complementarite."),
 T("Expliquer pourquoi un rappel de vaccin est necessaire pour certains agents.",
    "La premiere vaccination cree des cellules memoire et des anticorps, mais leur concentration diminue avec le temps. Un rappel reexpose le systeme immunitaire a l'antigene : la reponse secondaire est alors plus rapide, plus intense et produit des anticorps de meilleure affinite. Pour certains agents, comme le tetanos ou la coqueluche, l'immunite acquise apres la primovaccination s'affaiblit en quelques annees. Les rappels maintiennent un niveau de protection suffisant et protegent aussi les personnes qui ne peuvent pas etre vaccinees grace a l'immunite de groupe.",
    "On attend la baisse des anticorps, la reponse secondaire et la notion d'immunite collective.")],
C("L'immunite combine des barrieres immediates non specifiques et une defense adaptee, specifique et memorisable.",
  "Antigen -> lymphocyte -> anticorps -> elimination",
  "Innee : peau, flore, phagocytes · acquise : lymphocytes B et T, memoire",
  "Phagocyte~Cellule qui englobe~Anticorps~Proteine de reconnaissance~Lymphocyte B~Producteur d'anticorps~Memoire~Reponse secondaire rapide",
  "Distinguer les deux types de defenses|Identifier les cellules impliquees|Expliquer la reconnaissance de l'antigene|Depeindre la reponse secondaire|Justifier la vaccination",
  "Confondre antigen et anticorps|Croire que l'immunite innée est specifique|Oublier les cellules memoire|Mélanger lymphocytes B et T",
  "Vaccin~Antigene sans maladie~Rappel~Reponse secondaire~Macrophage~Phagocytose~Allergie~Reaction excessive",
  "Immunite innée~Immediat et non specifique~Immunite acquise~Lente, specifique et durable",
  "Antigene~Declenche la reponse~Anticorps~Se fixe sur l'antigene"))

# ============================================================ BIO10
add("ST2S-B-BIO10", "Inflammation, infection et fievre : reactions de defense", BIO, ["1re", "Terminale"],
S("Une infection est l'invasion d'un organisme par un microbe pathogene qui s'y multiplie."
  "|Les agents infectieux comprennent les bacteries, les virus, les champignons et les parasites."
  "|Une bacterie est une cellule procaryote, sensible aux antibiotiques."
  "|Un virus n'est pas une cellule : il necessite une cellule hote pour se reproduire."
  "|L'inflammation est une reaction de defense locale a une agression, infectieuse ou non."
  "|Ses signes cardinaux sont rougeur, chaleur, gonflement, douleur et parfois perte de fonction."
  "|Les mastocytes libèrent de l'histamine, qui dilate les vaisseaux et augmente leur permeabilite."
  "|Les phagocytes affluent sur le lieu de l'inflammation et delimitent la zone infectieuse."
  "|La fievre est une elevation de la temperature centrale au-dessus de 38 degres Celsius."
  "|Les cytokines et l'interleukine 1 agissent sur l'hypothalamus, qui eleve le point de consigne thermique."
  "|La fievre est une defense : elle ralentit la multiplication de certains microbes et active l'immunite."
  "|Une fievre prolongee, avec frissons ou signes de gravite, necessite un avis medical et une surveillance."),
[Q("Quel agent infectieux necessite obligatoirement une cellule hote ?", "La bacterie~Le virus~Le champignon~Le parasite", 1,
    "Le virus est un parasite intracellulaire obligatoire : il ne se multiplie que dans une cellule."),
 Q("Quel signe n'est pas un signe cardinal de l'inflammation ?", "Rougeur~Chaleur~Gonflement~Hyperpigmentation", 3,
    "Les signes classiques sont rougeur, chaleur, gonflement, douleur et perte de fonction."),
 Q("Quel mediateur chimique est libere lors de l'inflammation ?", "L'insuline~L'histamine~La thyroxine~L'hemoglobine", 1,
    "L'histamine provoque la dilatation des vaisseaux et l'augmentation de leur permeabilite."),
 Q("A partir de quelle valeur parle-t-on de fievre ?", "37 degres~37,5 degres~38 degres~40 degres", 2,
    "La fievre est definie par une temperature centrale superieure a 38 degres Celsius."),
 Q("Quelle structure du cerveau regle le point de consigne thermique ?", "Le cervelet~L'hypothalamus~La moelle~Le bulbe seul", 1,
    "L'hypothalamus integre les signaux des cytokines et ajuste la temperature cible."),
 Q("Quel est un effet beneficial de la fievre ?", "Elle favourise toutes les bacteries~Elle ralentit certains microbes et active l'immunite~Elle arrete la respiration~Elle augmente la glycemie", 1,
    "Une fievre moderee participe a la defense de l'organisme."),
 Q("Quel antibiotique est actif sur les virus ?", "Aucun~La penicilline~L'amoxicilline~Le metronidazole", 0,
    "Les antibiotiques ciblent des structures bacteriennes : ils sont inactifs sur les virus."),
 T("Distinguer infection, inflammation et fievre a partir d'un exemple de plaie infectee.",
    "L'infection correspond a la penetration et a la multiplication de bacteries dans la plaie. L'inflammation est la reaction locale de l'organisme : les vaisseaux se dilatent, les phagocytes arrivent, d'ou rougeur, chaleur, gonflement et douleur. La fievre est une reaction generale : les cytokines produites localement atteignent l'hypothalamus et elevent la temperature du corps entier. Les trois phenomenes sont lies mais de niveaux differents : local microbien, local reactionnel et general systemique.",
    "On attend la distinction nette entre invasion microbienne, reaction locale et reaction generale."),
 T("Pourquoi ne faut-il pas systematiquement donner un antibiotique en cas de fievre ?",
    "La fievre a de nombreuses causes, notamment virales, contre lesquelles les antibiotiques sont inactifs. Un antibiotique inutile expose a des effets indesirables, perturbe la flore residente et selectionne des bacteries resistantes. La conduite a tenir est d'abord d'evaluer la gravite, d'hydrater, de surveiller les parametres vitaux et de rechercher la cause. L'antibiotique est reserve aux infections bacteriennes probables ou confirmees, apres avis medical et selon les recommandations en vigueur.",
    "On attend l'origine virale possible, l'absence d'effet et le risque d'antibioresistance.")],
C("Infection, inflammation et fievre sont trois niveaux de reponse a une agression : microbien, local et general.",
  "Agression -> inflammation locale -> cytokines -> hypothalamus -> fievre",
  "38 degres : seuil de fievre · histamine : vasodilatation · antibiotique : bacteries uniquement",
  "Infection~Multiplication d'un microbe~Inflammation~Reaction locale de defense~Fievre~Temperature au-dessus de 38~Cytokine~Signal vers l'hypothalamus",
  "Identifier l'agent infectieux|Observer les signes locaux|Mesurer la temperature|Evaluer la gravite|Choisir une conduite a tenir adaptee",
  "Donner un antibiotique pour une fievre virale|Confondre infection et inflammation|Ignorer les signes de gravite|Oublier l'hydratation",
  "Plaie infectee~Bacteries~Rougeur~Inflammation locale~38,5 degres~Fievre~Antibiotique~Active sur bacteries",
  "Bacterie~Cellule procaryote~Virus~Parasite intracellulaire",
  "Inflammation~Reaction locale~Fievre~Reaction generale"))

# ============================================================ BIO11
add("ST2S-B-BIO11", "Cancérogenese, tumeurs et prevention", BIO, ["Terminale"],
S("Un cancer est une proliferation incontrolee de cellules qui echappent aux mecanismes de regulation."
  "|Les cellules cancereuses presentent une croissance autonome et perdent l'inhibition de contact."
  "|Elles perdent aussi la specialisation et deviennent indifferenciees, ou anaplasiques."
  "|Une tumeur benigne reste localisee, ne metastase pas et est generalement peu dangereuse."
  "|Une tumeur maligne est invasive : elle traverse les membranes basales et peut donner des metastases."
  "|Les metastases se forment par dissemination cellulaire via le sang ou la lymphe."
  "|L'ADN des cellules tumorales porte des mutations dans des genes activateurs ou suppresseurs de tumeurs."
  "|Les oncogenes stimulent la proliferation ; les genes suppresseurs, comme p53, freinent la division ou declenchent l'apoptose."
  "|Les carcinogenes favorisent ces mutations : tabac, alcool, rayons ultraviolets, certaines substances chimiques."
  "|Certains virus sont oncogenes, comme le papillomavirus ou le virus d'Epstein-Barr."
  "|Le depistage vise a detecter une lesion avant l'apparition des symptomes."
  "|La prevention repose sur la reduction des expositions, la vaccination et le suivi medical regulier."),
[Q("Quelle est une propriete d'une cellule cancereuse ?", "Elle respecte l'inhibition de contact~Elle prolifere de facon autonome~Elle meurt immediatement~Elle devient un globule rouge", 1,
    "La perte d'inhibition de contact et la croissanceautonome sont des caracteres tumoraux."),
 Q("Quelle differencie une tumeur benigne d'une tumeur maligne ?", "La benigne metastase~La maligne est invasive et peut metastaser~La benigne est toujours mortelle~La maligne ne se divise pas", 1,
    "Le caractere invasif et metastatique definit la malignite."),
 Q("Comment les metastases se disseminent-elles ?", "Par l'air seulement~Par le sang et la lymphe~Par les nerfs uniquement~Par la bile", 1,
    "Les cellules tumorales empruntent les vaisseaux sanguins et lymphatiques."),
 Q("Que fait le gene suppresseur de tumeur p53 ?", "Stimule la division~Frene la division ou declenche l'apoptose~Produit de l'insuline~Repare les os", 1,
    "p53 arrete le cycle cellulaire face a une lesion de l'ADN ou provoque la mort cellulaire."),
 Q("Quel facteur est un carcinogene reconnu ?", "Le tabac~Le sport~Le sommeil~L'eau potable", 0,
    "Le tabac est implique dans de nombreux cancers, notamment du poumon."),
 Q("Quel virus est associe a un risque de cancer du col de l'uterus ?", "Le virus de la grippe~Le papillomavirus~Le virus de la rougeole~Le virus de l'herpes simple", 1,
    "Le papillomavirus humain est a l'origine de la majorite des cancers du col, d'ou la vaccination."),
 Q("Quel est l'objectif d'un depistage ?", "Traiter apres les symptomes~Detectar une lesion avant les symptomes~Eviter tout examen~Remplacer le traitement", 1,
    "Le depistage vise a diagnostiquer precocement une lesion, quand le traitement est plus efficace."),
 T("Expliquer comment une mutation de l'ADN peut conduire a une tumeur maligne.",
    "Une mutation peut toucher un oncogene et le rendre hyperactif, ou un gene suppresseur comme p53 et l'inactiver. Dans les deux cas, le frein a la division cellulaire disparait : la cellule ne repond plus aux signaux d'arret, ignore l'inhibition de contact et continue de se diviser malgre les lesions de son ADN. Les mutations s'accumulent au fil des divisions, ce qui rend la cellule de plus en plus anormale. Elle peut alors traverser la membrane basale, envahir les tissus voisins et former des metastases.",
    "On attend oncogenes, genes suppresseurs, perte de controle et progression vers l'invasion."),
 T("Montrer en quoi la prevention et le depistage sont complementaires dans la lutte contre le cancer.",
    "La prevention agit en amont en reduisant l'exposition aux carcinogenes : arret du tabac, limitation de l'alcool, protection contre les UV, vaccination contre le papillomavirus. Elle diminue le nombre de nouvelles lesions. Le depistage agit en aval : il recherche une lesion chez une personne encore asymptomatique, par exemple par mammographie ou test de depistage du cancer colorectal. Un cancer detecte tot est plus souvent curable et necessite des traitements moins lourds. Les deux approches reduisent la mortalite, mais par des mecanismes differents : eviter la maladie ou la traiter plus tot.",
    "On attend la distinction amont/aval et des exemples concrets de prevention et de depistage.")],
C("Le cancer resulte d'une accumulation de mutations qui liberent la cellule des freins a la division.",
  "Mutation -> proliferation -> invasion -> metastases",
  "Oncogene : accelere · p53 : freine · depistage : diagnostic precoce",
  "Tumeur~Proliferation cellulaire~Metastase~Dissemination a distance~Oncogene~Gene activateur~Depistage~Detection avant symptomes",
  "Identifier le type de lesion|Comparer benigne et maligne|Expliquer le role des genes|Reconnaitre un carcinogene|Proposer une action de prevention",
  "Confondre tumeur benigne et maligne|Croire que tout cancer est hereditaire|Oublier les virus oncogenes|Negliger l'interet du depistage",
  "Tabac~Carcinogene majeur~Papillomavirus~Vaccination~Mammographie~Depistage~p53~Gene suppresseur",
  "Tumeur benigne~Localisee, non metastatique~Tumeur maligne~Invasive et metastatique",
  "Oncogene~Stimule la division~Gene suppresseur~Freine la division"))

# ============================================================ SST1
add("ST2S-B-SST01", "Sante, maladie et approche systemique de la personne", STT, ["1re"],
S("La sante est un etat de complet bien-etre physique, mental et social selon la definition de l'OMS."
  "|La sante ne se limite pas a l'absence de maladie ou d'infirmite."
  "|La maladie est une perturbation de l'equilibre de l'organisme, qui peut etre aigue ou chronique."
  "|Une approche systemique considerela personne comme un ensemble de sous-systemes en interaction."
  "|Les sous-systemes biologique, psychologique et social s'influencent mutuellement."
  "|Un evenement de vie, comme un deuil ou une perte d'emploi, peut modifier l'etat de sante physique."
  "|Une maladie chronique entraine des consequences sur l'autonomie, le travail et les relations."
  "|Le role du soignant est d'accompagner la personne dans sa globalite, pas seulement de traiter un symptome."
  "|La qualite de vie est un indicateur subjectif lie au bien-etre ressenti et aux opportunites disponibles."
  "|L'autonomie designe la capacite de la personne a agir et a decider pour elle-meme."
  "|La dependance est relative : elle varie selon l'environnement, les aides et les appareillages."
  "|Cette approche fonde la notion de projet de soin personnalise, construit avec la personne."),
[Q("Selon l'OMS, la sante est ...", "L'absence de maladie~Un etat de complet bien-etre physique, mental et social~Une simple capacite de travail~Un droit reserve aux adultes", 1,
    "La definition de l'OMS inclut les dimensions physique, mentale et sociale."),
 Q("Quelle est une caracteristique d'une maladie chronique ?", "Elle dure peu et guerit vite~Elle s'inscrit dans la duree avec des consequences fonctionnelles~Elle n'affecte que les enfants~Elle est toujours contagieuse", 1,
    "Une maladie chronique est durable et peut alterer l'autonomie et la qualite de vie."),
 Q("Dans une approche systemique, la personne est ...", "Un ensemble de sous-systemes en interaction~Un organisme isole~Un simple diagnostic~Un dossier medical", 0,
    "Les dimensions biologique, psychologique et sociale sont intertwinees."),
 Q("Quel evenement peut influencer l'etat de sante physique ?", "Un deuil~Une couleur de mur~Une heure de la journee~Un numéro de telephone", 0,
    "Les evenements de vie ont des effets sur la sante mentale et physique."),
 Q("Comment definir l'autonomie ?", "Ne jamais demander d'aide~Capacite d'agir et de decider pour soi~Vivre sans aucune contrainte~Etre toujours independant", 1,
    "L'autonomie est la capacite de choisir et d'agir, meme avec des aides adaptees."),
 Q("La dependance est ...", "Toujours definitive~Relative au contexte et aux aides~Identique pour tous~Impossible a reduire", 1,
    "L'environnement et les appareillages modifient le degre de dependance."),
 Q("Que vise un projet de soin personnalise ?", "Appliquer un protocole identique a tous~Construire une prise en charge avec la personne~Supprimer tout suivi~Remplacer le medecin", 1,
    "Le projet est elabore avec la personne, en tenant compte de ses besoins et de ses choix."),
 T("Distinguer sante, maladie et qualite de vie chez une personne atteint d'une maladie chronique.",
    "La sante, selon l'OMS, est un etat global de bien-etre, pas seulement l'absence de symptomes. La maladie correspond a une perturbation durable de l'equilibre de l'organisme, ici chronique. La qualite de vie est l'evaluation subjective par la personne de son bien-etre et de ses possibilites d'action. Une personne peut vivre avec une maladie chronique et conserver une bonne qualite de vie grace a un traitement efficace, un environnement adapté et le maintien de ses liens sociaux.",
    "On attend les trois definitions et la demonstration qu'elles ne se confondent pas."),
 T("Comment un soignant applique-t-il une approche systemique dans un entretien ?",
    "Il recueille d'abord les donnees biologiques et les symptomes, puis il interroge la personne sur son vécu, ses emotions, ses activites et son entourage. Il observe comment les difficultes physiques retentissent sur la vie sociale et inversement. Il associe la personne, sa famille et les autres professionnels a l'elaboration du projet de soin. Il evite ainsi de reduire la situation a un seul organe ou a un seul symptome et respecte les choix de la personne.",
    "On attend le recueil pluridimensionnel, l'association de la personne et le refus d'une vision reductionniste.")],
C("La personne est un systeme ou le biologique, le psychique et le social interagissent en permanence.",
  "Sante = bien-etre physique + mental + social (OMS)",
  "Approche systemique · autonomie relative · projet de soin personnalise",
  "Sante~Bien-etre global~Maladie~Perturbation de l'equilibre~Autonomie~Capacite de choisir~Qualite de vie~Evaluation subjective",
  "Recueillir les donnees biologiques|Ecouter le vecu et les emotions|Observer le contexte social|Evaluer l'autonomie|Construire le projet avec la personne",
  "Reduire la personne a son diagnostic|Ignorer les facteurs sociaux|Confondre autonomie et independance totale|Imposer un projet sans accord",
  "Maladie chronique~Insuffisance renale~Deuil~Evenement de vie~Qualite de vie~Bien-etre ressenti~Projet de soin~Prise en charge personalisee",
  "Approche systemique~Interactions entre dimensions~Approche biomedicals~Centree sur l'organe",
  "Autonomie~Capacite de decision~Dependance~Besoin d'aide contextuel"))

# ============================================================ SST2
add("ST2S-B-SST02", "Besoins fondamentaux, qualite de vie et accompagnement", STT, ["1re"],
S("La notion de besoin fondamental classe les necessites essentielles de la personne."
  "|Les besoins physiologiques comprennent l'alimentation, l'hydratation, le sommeil et l'elimination."
  "|Les besoins de securite portent sur l'abri, la protection et la stabilite de l'environnement."
  "|Les besoins d'appartenance concernent les liens familiaux, sociaux et affectifs."
  "|Les besoins d'estime de soi et de reconnaissance sont lies a l'image de soi et au role social."
  "|Les besoins de realisation de soi portent sur le developpement des capacites et des projets."
  "|La pyramide des besoins propose une hierarchie, mais les besoins peuvent etre simultanes."
  "|Un besoin non couvert peut entrainer une souffrance et retentir sur la sante."
  "|La qualite de vie depend de la satisfaction des besoins et des possibilites d'action de la personne."
  "|L'accompagnement vise a soutenir la personne sans se substituer a elle."
  "|Faire a la place plutot qu'avec la personne reduced son autonomie."
  "|L'evaluation des besoins doit etre reguliere car ils evoluent avec la maladie et l'age, et leur trace ecrite assure la continuite entre professionnels."),
[Q("Quel besoin appartient aux besoins physiologiques ?", "L'appartenance~Le sommeil~La reconnaissance~La realisation de soi", 1,
    "Le sommeil, comme manger ou boire, est un besoin physiologique fondamental."),
 Q("Quel auteur a propose une pyramide des besoins ?", "Freud~Maslow~Piaget~Erikson", 1,
    "La hierarchie des besoins est une notion developpee par Abraham Maslow."),
 Q("Que designe le besoin d'appartenance ?", "Le besoin de manger~Le besoin de liens avec autrui~Le besoin de dormir~Le besoin de reconnaissance", 1,
    "Il concerne les relations affectives, familiales et sociales."),
 Q("Quel risque a « faire a la place » de la personne ?", "Gain d'autonomie~Reduction de l'autonomie~Meilleure qualite de vie~Aucun effet", 1,
    "Se substituer a la personne diminue ses occasion d'agir et donc son autonomie."),
 Q("Pourquoi reevaluer regulierement les besoins ?", "Parce qu'ils sont figes~Parce qu'ils evoluent avec la maladie et l'age~Parce que la loi l'interdit~Parce que le dossier doit etre rempli", 1,
    "Les besoins changent avec la situation de la personne et necessitent une reevaluation."),
 Q("A quoi sert la trace ecrite des besoins ?", "A occuper le dossier~A assurer la continuite entre professionnels~A remplacer l'entretien~A prouver une prescription", 1,
    "La transmission ecrite garantit la continuite de l'accompagnement."),
 Q("Quelle affirmation est correcte ?", "Les besoins sont toujours successifs~Plusieurs besoins peuvent etre simultanes~Un seul besoin suffit toujours~Les besoins n'ont pas d'importance", 1,
    "La hierarchie est un outil, mais la personne peut avoir plusieurs besoins a la fois."),
 T("Identifier les besoins d'une personne agee apres une chute et proposer des actions adaptees.",
    "Besoins physiologiques : soulager la douleur, assurer le sommeil et l'elimination. Besoins de securite : sécuriser le logement, adapter la lit, eviter une nouvelle chute. Besoins d'appartenance : maintenir les visites familiales et les contacts sociaux. Besoins d'estime de soi : valoriser les gestes qu'elle peut encore accomplir, par exemple se laver partiellement. Besoins de realisation : l'associer aux decisions et a un projet de reeducation. Les actions sont donc celles d'un accompagnement avec la personne, et non a sa place.",
    "On attend une approche multi-niveaux et des actions qui preservent l'autonomie."),
 T("Expliquer la difference entre accompagner et substituer dans la vie quotidienne.",
    "Accompagner, c'est offrir un soutien adapte pour que la personne puisse agir elle-meme : on prepare les objects a portee de main, on encourage, on laisse du temps. Substituer, c'est realiser l'action a sa place, par exemple la habiller entierement sans solliciter sa participation. La substitution peut etre necessaire en cas de deficit majeur, mais elle doit etre temporaire et reevaluee. A long terme, elle entraine une perte des capacites restantes, une baisse de l'estime de soi et une dependance accrue.",
    "On attend la distinction, les effets sur l'autonomie et la possibilite d'une substitution temporaire.")],
C("Identifier les besoins de la personne permet d'adapter l'accompagnement et de preservier son autonomie.",
  "Physiologique -> securite -> appartenance -> estime -> realisation",
  "Accompagner avec la personne, non a sa place · reevaluation reguliere",
  "Besoin physiologique~Manger, dormir~Besoin de securite~Etre protege~Appartenance~Liens sociaux~Estime de soi~Reconnaissance",
  "Observer la situation|Ecouter la personne|Identifier les besoins non couverts|Proposer des actions adaptees|Tracer et reevaluer",
  "Imposer ses propres priorités|Se substituer systematiquement|Oublier les besoins psychosociaux|Ne pas transmettre les informations",
  "Chute~Besoin de securite~Visite familiale~Appartenance~Toilette partielle~Estime de soi~Dossier de suivi~Continuite",
  "Accompagner~Soutenir l'action de la personne~Se substituer~Faire a sa place",
  "Besoins simultanes~Plusieurs niveaux en meme temps~Besoins successifs~Hierarchie theorique"))

# ============================================================ SST3
add("ST2S-B-SST03", "Relation d'aide, ecoute et communication professionnelle", STT, ["1re", "Terminale"],
S("La relation d'aide vise a soutenir une personne dans une situation de difficulté."
  "|Elle repose sur l'ecoute, le respect, la consideration et la non-jugement."
  "|L'ecoute active implique de reformuler, de poser des questions ouvertes et de laisser des silences."
  "|Une question ouverte permet a la personne de developper sa reponse, contrairement a une question fermee."
  "|La reformulation verifie la comprehension et montre que le message a ete entendu."
  "|Le silence respectueux laisse la place a l'expression des emotions."
  "|La congruence entre les paroles, le ton et la posture renforce la credibilite du soignant."
  "|Le langage non verbal comprene le regard, la distance, les gestes et la posture."
  "|Une distance physique adaptee respecte l'intimite sans creer de rejet."
  "|L'empathie consiste a comprendre le vécu de l'autre sans le confondre avec le sien."
  "|La sympathie, a l'inverse, implique un partage emotionnel qui peut nuire a la neutralite professionnelle."
  "|La relation d'aide a des limites : elle ne remplace ni le diagnostic medical ni le soutien de l'equipe."),
[Q("Quel est un outil de l'ecoute active ?", "La reformulation~Le silence absolu~Le conseil immediate~Le jugement", 0,
    "Reformuler permet de verifier la comprehension et de montrer l'ecoute."),
 Q("Qu'est-ce qu'une question ouverte ?", "Une question avec oui ou non~Une question qui invite au developpement~Une question fermee~Une question suggestive", 1,
    "« Comment vous sentez-vous ? » est ouverte, contrairement a « Avez-vous mal ? »."),
 Q("Que designe l'empathie ?", "Eprouver exactement la meme emotion~Comprendre le vecu de l'autre sans se confondre avec lui~Juger la personne~Prendre la decision a sa place", 1,
    "L'empathie est une comprehension respectueuse, distincte de la sympathie."),
 Q("Quel element appartient au langage non verbal ?", "La reformulation~La posture et le regard~La question ouverte~Le compte rendu ecrit", 1,
    "Le non verbal comprend regard, posture, gestes, ton et distance."),
 Q("Quel risque presente la sympathie dans la relation de soin ?", "Aucun~Une perte de distance professionnelle~Une meilleure neutralite~Une augmentation de l'autonomie", 1,
    "Un partage emotionnel trop fort peut nuire a la neutralite et a l'objectivite."),
 Q("Quel est l'effet d'un silence respectueux ?", "Il bloque la conversation~Il laisse la place a l'expression~Il montre le desinteret~Il remplace l'ecoute", 1,
    "Le silence donne a la personne le temps de formuler ce qu'elle ressent."),
 Q("Quelle limite de la relation d'aide est correcte ?", "Elle remplace le medecin~Elle ne remplace pas le diagnostic ni l'equipe~Elle interdit toute emotion~Elle supprime la transmission", 1,
    "La relation d'aide soutient la personne mais s'inscrit dans un travail d'equipe."),
 T("Conduire un court entretien d'aide avec une personne qui dit « Je ne suis plus bonne a rien ».",
    "Le soignant accueille la parole sans la corriger : « Je vous entends, vous vous sentez decouragée en ce moment. » Il reformule pour verifier : « C'est bien de la tristesse que vous ressentez ? » Il pose une question ouverte : « Qu'est-ce qui vous a donne cette impression aujourd'hui ? » Il respecte un silence, observe sa posture et garde une distance adaptee. Il ne dit pas « Ne dites pas cela », qui nierait le vécu, et il ne promet pas une amelioration qu'il ne peut garantir.",
    "On attend accueil, reformulation, question ouverte, silence et absence de jugement."),
 T("Distinguer empathie, sympathie et compassion dans la relation de soin.",
    "L'empathie est la comprehension intellectuelle et emotionnelle du vécu de l'autre, tout en gardant sa propre place. La sympathie est un sentiment de participation affective, ou l'on « entre » dans l'emotion de l'autre, avec un risque de perte de distance. La compassion ajoute a l'empathie une volonte d'aider et de soulager, sans se confondre avec la pitié, qui place l'autre dans une position d'inferiorite. En pratique, le soignant empathique et compatissant reste present, respectueux et capable d'agir avec l'equipe.",
    "On attend trois definitions distinctes et un lien avec la posture professionnelle.")],
C("La relation d'aide soutient la personne par l'ecoute et le respect, sans jugement ni substitution.",
  "Ecoute active = questions ouvertes + reformulation + silences",
  "Empathie : comprendre sans se confondre · silence : laisser la place",
  "Ecoute active~Reformuler et questionner~Empathie~Comprendre le vecu~Question ouverte~Invite au developpement~Non verbal~Regard et posture",
  "Installer un cadre respectueux|Poser une question ouverte|Reformuler le ressenti|Respecter un silence|Fixer les limites de la relation",
  "Repondre par un conseil avant d'ecouter|Confondre empathie et pitié|Juger la personne|Remplacer l'equipe medicale",
  "« Je ne suis plus bonne a rien »~Tristesse exprimee~Reformulation~« Vous vous sentez decouragée »~Silence~Espace d'expression~Posture~Distance respectueuse",
  "Empathie~Comprendre en restant soi-meme~Sympathie~Partager l'emotion de l'autre",
  "Question ouverte~Comment vous sentez-vous ?~Question fermee~Avez-vous mal ?"))

# ============================================================ SST4
add("ST2S-B-SST04", "Observation clinique et parametres vitaux", STT, ["1re", "Terminale"],
S("L'observation clinique est un recueil structure d'informations sur l'etat d'une personne."
  "|Elle associe ce que la personne dit, ce que le soignant voit et ce qu'il mesure."
  "|Les parametres vitaux sont la temperature, la frequence cardiaque, la frequence respiratoire, la pression arterielle et la saturation en oxygene."
  "|La temperature corporelle normale se situe autour de 36,5 a 37,5 degres Celsius."
  "|La frequence cardiaque adulte au repos est d'environ 60 a 100 battements par minute."
  "|La frequence respiratoire adulte au repos est d'environ 12 a 20 mouvements par minute."
  "|La pression arterielle est donnee sous la forme systolique sur diastolique, par exemple 120/80 mmHg."
  "|La saturation en oxygene, ou SpO2, est mesuree avec un oxymetre de pouls."
  "|Une valeur de SpO2 inferieure a 95 % doit alerter et etre signalée."
  "|La douleur est evaluee par une echelle, par exemple de 0 a 10 ou avec une echelle visuelle."
  "|Toute mesure doit etre horodatee, tracée et comparee aux valeurs precedentes."
  "|Une anomalie est transmise rapidement a l'equipe selon la procedure en vigueur, sans retarder l'alerte."),
[Q("Quel parametre ne fait pas partie des parametres vitaux courants ?", "La temperature~La glycemie capillaire systematique~La pression arterielle~La saturation en oxygene", 1,
    "Les cinq parametres vitaux courants sont temperature, pouls, respiration, pression et SpO2."),
 Q("Quelle est une frequence cardiaque adulte normale au repos ?", "30~75~130~180", 1,
    "La plage habituelle est de 60 a 100 battements par minute."),
 Q("Comment ecrire une pression arterielle de 120 sur 80 ?", "120/80 mmHg~80/120 mmHg~120+80 mmHg~200 mmHg", 0,
    "La systolique s'ecrit en premier, puis la diastolique, en millimetres de mercure."),
 Q("Quel appareil mesure la saturation en oxygene ?", "Un stethoscope~Un oxymetre de pouls~Un thermometre~Un tensionmetre", 1,
    "L'oxymetre de pouls mesure la SpO2 par absorption de lumiere."),
 Q("Quelle valeur de SpO2 doit alerter ?", "99 %~95 % et plus~Moins de 95 %~100 %", 2,
    "Une SpO2 inferieure a 95 % est consideree comme anormale chez l'adulte au repos."),
 Q("Comment tracer correctement une mesure ?", "Sans heure~Avec l'heure et la date~Uniquement si elle est anormale~Sur un papier volant", 1,
    "Une mesure est horizontale, datee et inscrite dans le dossier de suivi."),
 Q("Que faire face a une valeur anormale ?", "Attendre la prochaine mesure~Corriger le chiffre~Alerter l'equipe selon la procedure~Ne rien noter", 2,
    "L'anomalie doit etre transmise sans delai, apres verification de la mesure."),
 T("Une personne a une temperature de 38,6 degres, un pouls a 110 et une SpO2 a 93 %. Analyser la situation.",
    "La temperature depasse 38 degres : il y a fievre. Le pouls a 110 depasse la plage 60-100 : il y a tachycardie, possiblement liee a la fievre, a la douleur ou a une hypovolemie. La SpO2 a 93 % est inferieure au seuil de 95 % : il existe une desaturation. L'association de ces trois anomalies constitue un signe de gravite potentielle. Le soignant doit verifier les mesures, observer la personne, la installer confortablement et alerter rapidement l'infirmier ou le medecin en transmettant les chiffres et l'heure, sans attendre une aggravation.",
    "On attend l'interpretation de chaque valeur et la conduite a tenir avec transmission."),
 T("Expliquer l'importance de la trace ecrite et de la comparaison avec les mesures precedentes.",
    "Une mesure isolee ne raconte qu'un instant. La comparaison avec les valeurs precedentes montre une tendance : une temperature qui monte regulierement ou une pression qui baisse est plus significative qu'une valeur limite stable. La trace horodatee permet a tous les professionnels de l'equipe de lire la meme information, d'evaluer l'efficacite d'un traitement et de reconstituer l'historique en cas d'incident. Elle est aussi un element de preuve et de continuite des soins. Une mesure non ecrite est, pour l'equipe, une mesure perdue.",
    "On attend la notion de tendance, de partage d'information et de continuite.")],
C("L'observation clinique combine dire, voir et mesurer ; chaque donnee est tracee et transmise.",
  "Temperature 36,5-37,5 · pouls 60-100 · respiration 12-20 · SpO2 >= 95 %",
  "Toute valeur est horodatee, comparee et signalee si elle est anormale",
  "Parametre vital~Mesure de l'etat~Fievre~Plus de 38 degres~Tachycardie~Pouls au-dessus de 100~SpO2~Saturation en oxygene",
  "Observer et ecouter|Mesurer les parametres|Comparer aux valeurs de reference|Tracer avec l'heure|Signaler toute anomalie",
  "Oublier d'horodater|Ne mesurer qu'un seul parametre|Ne pas alerter par peur de deranger|Corriger une valeur genante",
  "38,6 degres~Fievre~110 bpm~Tachycardie~93 %~Desaturation~Alerte~Transmission a l'equipe",
  "Observation subjective~Ce que dit la personne~Observation objective~Ce que l'on mesure",
  "Mesure isolee~Instant donne~Tendance~Evolution dans le temps"))

# ============================================================ SST5
add("ST2S-B-SST05", "Hygiene, asepsie et prevention des infections associees aux soins", STT, ["1re", "Terminale"],
S("Les infections associees aux soins sont contractees lors d'une prise en charge medicale."
  "|Elles concernent surtout les sites operatoires, les voies urinaires, la peau et les poumons."
  "|La chaine de transmission infectieuse comprend une source, un mode de transmission et une personne recevable."
  "|Les modes de transmission sont directs, par contact, ou indirects, via un objet ou un vecteur."
  "|L'asepsie designe l'ensemble des mesures qui empechent l'introduction de micro-organismes."
  "|L'antisepsie est l'application d'un antiseptique sur un tissu vivant pour reduire la flore."
  "|La desinfection porte sur un objet inanime, la sterilisation detruit toutes les formes microbiennes."
  "|Le lavage des mains est la mesure d'hygiene la plus efficace et la plus simple."
  "|La friction hydro-alcoolique est recommandee quand les mains ne sont pas visiblement sales."
  "|Les gants ne remplacent pas le lavage des mains et doivent etre changes entre deux actes."
  "|Les equipements de protection comprennent gants, masque, blouse et protection des yeux selon le risque."
  "|La tenue, les surfaces et les dispositifs medicals font l'objet de protocoles ecrits et de controles."),
[Q("Quelle mesure est la plus efficace contre la transmission manuportée ?", "Le port de gants permanent~Le lavage ou la friction des mains~Le balayage du sol~Le changement de drap", 1,
    "L'hygiene des mains est la mesure de reference pour rompre la chaine de transmission."),
 Q("Que designe l'asepsie ?", "La destruction de toutes les bacteries sur un objet~L'ensemble des mesures evitant l'introduction de microbes~L'application d'un antiseptique~Le simple nettoyage visible", 1,
    "L'asepsie est une approche globale preventive, avant tout contact."),
 Q("Quelle est la difference entre antiseptique et desinfectant ?", "Aucune~L'antiseptique s'applique sur un tissu vivant, le desinfectant sur un objet~L'antiseptique est plus fort~Le desinfectant s'injecte", 1,
    "Antiseptique : tissu vivant ; desinfectant : surface ou objet inanime."),
 Q("Quand la friction hydro-alcoolique est-elle recommandee ?", "Quand les mains sont souillees~Quand les mains ne sont pas visiblement sales~Apres chaque repas uniquement~Jamais", 1,
    "La friction est adaptee aux mains non visiblement souillees ; sinon, lavage a l'eau et au savon."),
 Q("Les gants remplacent-ils le lavage des mains ?", "Oui toujours~Non, jamais~Seulement en chirurgie~Uniquement la nuit", 1,
    "Le port de gants ne dispense pas de l'hygiene des mains avant et apres l'acte."),
 Q("Quel site est frequemment touché par une infection associee aux soins ?", "Le site operatoire~Les cheveux~Les ongles~La voix", 0,
    "Les infections du site operatoire figurent parmi les plus surveillees."),
 Q("Que permet une chaine de transmission identifiee ?", "Predire le cout~Cibler les mesures de prevention~Supprimer les soins~Remplacer le protocole", 1,
    "Connaitre source, mode et receveur permet de rompre la chaine a chaque maillon."),
 T("Décrire les etapes d'une friction hydro-alcoolique correcte des mains.",
    "On se débarrasse des bijoux et on verify que les mains ne sont pas visiblement sales. On depose une quantite suffisante de produit hydro-alcoolique dans la paume. On frotte paume contre paume, puis le dos des mains, les espaces entre les doigts, les pulpes, les poignets et les ongles, jusqu'a sensibilisation des mains seches, pendant environ 30 secondes. On ne rince pas et on ne sEssuie pas. Cette gestuelle couvre toute la surface cutanee et garantit le temps de contact necessaire a l'action du produit.",
    "On attend la quantite, les differentes zones frottees, la duree et l'absence de rinçage."),
 T("Expliquer pourquoi le port de gants ne dispense pas de l'hygiene des mains.",
    "Les gants peuvent etre contaminés lors de l'enfilage et presenter des microperforations invisibles. Apres un soin, ils sont souilles et peuvent transporter des micro-organismes d'un patient a l'autre si l'on touche ensuite une porte, un clavier ou un autre patient. L'hygiene des mains avant l'enfilage protege le patient ; apres le retrait, elle protege le soignant et l'environnement. Les gants sont donc un complement, lie a un acte precis et a une zone de soin, jamais un substitut au lavage ou a la friction.",
    "On attend la contamination a l'enfilage, les microperforations et le double role avant/apres.")],
C("Rompre la chaine de transmission passe d'abord par l'hygiene des mains, Completee par l'asepsie et les protections.",
  "Source -> mode de transmission -> personne recevable",
  "Antiseptique : tissu vivant · desinfectant : objet · asepsie : ensemble des mesures",
  "Asepsie~Prevention globale~Antisepsie~Tissu vivant~Desinfection~Objet inanime~Friction~Geste d'hygiene des mains",
  "Identifier la source et le mode|Choisir la mesure adaptee|Realiser l'hygiene des mains|Changer les gants entre les actes|Tracer l'application du protocole",
  "Garder les memes gants entre deux patients|Frictionner sur des mains sales|Confondre antiseptique et desinfectant|Oublier les poignets",
  "Friction~30 secondes~Gants~Changer entre deux actes~Site operatoire~Infection surveillee~Blouse~Protection adaptée",
  "Transmission directe~Contact peau a peau~Transmission indirecte~Via un objet ou un vecteur",
  "Asepsie~Empeche l'introduction~Antisepsie~Reduit la flore sur tissu vivant"))

# ============================================================ SST6
add("ST2S-B-SST06", "Securite au travail et risques professionnels en sante", STT, ["1re", "Terminale"],
S("Les professionnels de sante sont exposes a des risques professionnels specifiques."
  "|Les risques biologiques sont lies au contact avec des agents infectieux : sang, secrétions, dechets."
  "|Les accidents d'exposition au sang, ou AES, necessitent une prise en charge immediate et un suivi."
  "|Les risques chimiques concernent les medicaments, les desinfectants et les produits de nettoyage."
  "|Certains medicaments anticancereux sont dangereux a manipuler et exigent des protections particulieres."
  "|Les risques physiques comprennent les chutes, les manutentions, le bruit et les rayonnements."
  "|La manutention de personnes mobilise les membres superieurs et le dos : les gestes et aides techniques reduisent les tensions."
  "|Les risques psychosociaux sont lies a la charge de travail, au stress, aux conflits et aux horaires."
  "|Le document unique d'evaluation des risques professionnels recense les risques et les actions de prevention."
  "|Les equipements de protection individuelle sont adaptees a la tache et verifies regulierement."
  "|La formation, les procedures et les exercices permettent d'appliquer les bons reflexes en situation d'urgence."
  "|Tout accident ou presque-accident doit etre declare et analyse pour eviter sa repetition, et la prevention collective prime sur la protection individuelle."),
[Q("Que designe un accident d'exposition au sang ?", "Une chute dans un couloir~Un contact avec du sang ou un objet piquant contaminé~Une erreur de dosage~Un conflit avec un collegue", 1,
    "L'AES est une effraction cutanee ou une projection de sang ou de liquide biologique."),
 Q("Quel risque est lie a la manipulation d'anticancereux ?", "Un risque biologique~Un risque chimique~Un risque de chute~Un risque de bruit", 1,
    "Ces medicaments sont cytotoxicises et necessitent des circuits dedies et des protections."),
 Q("Que contient le document unique ?", "Les seuls salaires~L'evaluation des risques et les actions de prevention~Les plannings~Les recettes de cuisine", 1,
    "Le DUERP recense les risques par unite et definit les mesures de maitrise."),
 Q("Quel geste reduce les tensions lors d'une manutention de personne ?", "Se pencher le dos rond~Utiliser les jambes et un aide technique~Tirer avec les bras seuls~Tourner le buste brusquement", 1,
    "La manutention adaptee privilégie les jambes, le dos droit et les aides mecaniques."),
 Q("Quel est un risque psychosocial ?", "Le bruit~La charge de travail et le stress~Une coupure~Une projection de produit", 1,
    "Les risques psychosociaux concernent l'organisation, les relations et les conditions de travail."),
 Q("Que faut-il faire apres un presque-accident ?", "Rien, il n'y a pas de blessure~Le declarer et l'analyser~Le cacher~Attendre un accident reel", 1,
    "La declaration permet d'identifier la cause et d'empecher un accident futur."),
 Q("Quel principe est prioritaire en prevention ?", "La protection individuelle seule~La prevention collective~L'attitude individuelle~Le hasard", 1,
    "On supprime ou reduit le risque a la source avant de proteger la personne."),
 T("Depeindre la conduite a tenir immediatement apres un accident d'exposition au sang.",
    "En cas de piqûre ou de projection, on lave immediatement la plaie a l'eau et au savon, puis on desinfecte avec un antiseptique adapte, sans faire saigner. En cas de projection sur les yeux ou les muqueuses, on rince abondamment a l'eau ou au serum physiologique. On signale sans delai a l'encadrant et au service de sante au travail, qui evaluent le risque et decidencent d'un suivi medical et d'une eventuelle prophylaxie. L'accident est ensuite declare et analyse pour corriger la procedure.",
    "On attend lavage, desinfection, rinçage si projection, signalement rapide et declaration."),
 T("Expliquer la difference entre prevention collective et protection individuelle, avec un exemple en milieu de soin.",
    "La prevention collective agit sur la situation de travail : choisir un matériel de sécurité avec aiguille protegee, organiser un circuit des dechets, former les equipes ou adapter les horaires. Elle protege tous les travailleurs sans dependre de leur vigilance. La protection individuelle agit sur la personne : gants, masque, lunettes, blouse. Elle est necessaire mais moins fiable, car elle peut etre mal portee ou oubliee. Dans la hierarchie des mesures, on privilégie d'abord la suppression du risque, puis sa reduction a la source, puis les protections collectives, et enfin individuelles.",
    "On attend la definition des deux approches et un exemple concret pour chacune.")],
C("La securite en sante repose sur l'evaluation des risques et la priorite donnee a la prevention collective.",
  "Risques : biologiques, chimiques, physiques, psychosociaux",
  "AES : laver, desinfecter, signaler · DUERP : evaluer et prevenir",
  "AES~Accident d'exposition au sang~DUERP~Evaluation des risques~Risque biologique~Contact avec un agent infectieux~EPI~Protection individuelle",
  "Repérer la situation a risque|Evaluer la probabilite et la gravite|Choisir la mesure de prevention|Appliquer les procedures|Declarer et analyser tout accident",
  "Se fier uniquement aux gants|Ne pas declarer un presque-accident|Confondre risque chimique et biologique|Negliger les risques psychosociaux",
  "Piqure~AES~Lavage~Eau et savon~Signalement~Encadrant et sante au travail~Manutention~Aide technique",
  "Prevention collective~Agir sur la situation~Protection individuelle~Agir sur la personne",
  "Risque biologique~Micro-organismes~Risque chimique~Produits et medicaments"))

# ============================================================ SST7
add("ST2S-B-SST07", "Demarche de soin, dossier patient et tracabilite", STT, ["1re", "Terminale"],
S("La demarche de soin est une methodique progressive d'analyse d'une situation de soin."
  "|Elle debute par le recueil d'informations aupres de la personne, de la famille et du dossier."
  "|L'analyse distingue les donnees objectives, mesurees, et les donnees subjectives, rapportees."
  "|Un probleme de soin est identifie a partir des donnees et de leur interpretation."
  "|Les objectifs de soin doivent etre precis, realistes, evaluables et limites dans le temps."
  "|Les actions sont choisies en fonction des besoins, des ressources et des choix de la personne."
  "|Leur mise en oeuvre est organizee dans le temps et repartie entre les professionnels."
  "|L'evaluation compare les resultats obtenus aux objectifs fixees initialement."
  "|La demarche est cyclique : l'evaluation conduit a de nouveaux objectifs ou a une reorientation."
  "|Le dossier de suivi regroupe les donnees medicales, les soins realises et les transmissions."
  "|La tracabilite permet de savoir qui a fait quoi, quand et avec quel resultat."
  "|Les transmissions orales et ecrites respectent le secret professionnel et utilisent un langage clair."),
[Q("Quelle est la premiere etape de la demarche de soin ?", "L'evaluation~Le recueil d'informations~La transmission~Le bilan", 1,
    "On recueille d'abord les donnees avant de les analyser et de fixer des objectifs."),
 Q("Qu'est-ce qu'une donnee objective ?", "Ce que la personne ressent~Ce que l'on mesure ou observe directement~Une opinion~Une rumeur", 1,
    "Une donnee objective est verifiable : temperature, pouls, aspect d'une plaie."),
 Q("Quelle qualite doit avoir un objectif de soin ?", "Etre vague~Etre evaluable~Etre illimite~Etre impose par le soignant seul", 1,
    "Un objectif est précis, realiste et evaluable dans un delai defini."),
 Q("A quoi sert l'evaluation dans la demarche de soin ?", "A clore definitivement le dossier~A comparer les resultats aux objectifs~A remplacer le recueil~A supprimer les transmissions", 1,
    "L'evaluation mesure l'ecart entre l'objectif et le resultat obtenu."),
 Q("Que garantit la tracabilite ?", "L'anonymat des soins~La connaissance de qui a fait quoi et quand~La gratuité des soins~L'absence de dossier", 1,
    "La tracabilite identifie les actions, leur auteur, leur date et leur resultat."),
 Q("Quel principle s'applique aux transmissions ?", "La liberte de ton~Le secret professionnel~L'absence d'ecrit~Le seul oral", 1,
    "Les informations sont partagees uniquement avec les professionnels concernes et dans un langage clair."),
 Q("Quel element n'appartient pas au dossier de suivi ?", "Les donnees medicales~Les soins realises~Les transmissions~Les gouts personnels du soignant", 3,
    "Le dossier contient des informations professionnelles, pas des preferences personnelles."),
 T("A partir d'une situation de desnutrition, formulier un objectif de soin evaluable et les actions correspondantes.",
    "Objectif : la personne atteindra une prise alimentaire d'au moins 1500 kcal par jour pendant cinq jours, avec une stabilisation de sa masse corporelle sur une semaine. Les actions comprennent l'evaluation des repas pris, l'adaptation des textures et des horaires, la presentation attractive des plateaux, l'accompagnement lors des repas, la surveillance de la masse et l'information de l'equipe medicale si l'objectif n'est pas atteint. L'evaluation quotidienne des quantites consommees permet de reajuster rapidement les actions.",
    "On attend un objectif precise, mesurable, date et des actions coherentes avec l'objectif."),
 T("Expliquer pourquoi la demarche de soin est cyclique et non lineaire.",
    "Une demarche lineaire s'arreterait apres la mise en oeuvre des actions. En realite, l'evaluation permanente montre si l'objectif est atteint, partiellement atteint ou depasse. Si le resultat est insuffisant, on revient a l'analyse des donnees, on reformule le probleme et on propose de nouveaux objectifs : par exemple une douleur non soulagee impose de revoir l'evaluation et le traitement. L'etat de la personne evolue, donc la demarche doit s'adapter. Ce cycle garantit une prise en charge reactive et personnalisee plutôt qu'un protocole rigide.",
    "On attend le role de l'evaluation, la reorientation et l'adaptation a l'evolution de la personne.")],
C("La demarche de soin est un cycle : recueillir, analyser, fixer des objectifs, agir, evaluer et reajuster.",
  "Recueil -> analyse -> objectifs -> actions -> evaluation",
  "Donnees objectives / subjectives · objectif evaluable · tracabilite des actions",
  "Demarche de soin~Methode progressive~Donnee objective~Faits mesures~Objectif~Cible evaluable~Tracabilite~Suivi des actions",
  "Recueillir les informations|Classer les donnees|Formuler un probleme de soin|Definir des objectifs evaluables|Evaluer et reajuster",
  "Fixer un objectif vague|Confondre donnee subjective et objective|Ne pas tracer les soins|Arreter la demarche apres l'action",
  "Desnutrition~Probleme identifie~1500 kcal~Objectif chiffre~Repas adaptes~Action~Masse stable~Resultat evaluable",
  "Donnee subjective~Ressenti rapporte~Donnee objective~Mesure directe",
  "Demarche lineaire~Sans retour~Demarche cyclique~Evaluation et reajustement"))

# ============================================================ SST8
add("ST2S-B-SST08", "Accompagnement de la personne agee et en situation de handicap", STT, ["Terminale"],
S("Le vieillissement entraine des changements progressifs des capacites physiques et cognitives."
  "|Il est variable selon les personnes et depend fortement des conditions de vie et de sante."
  "|La perte d'autonomie est une reduction des capacites d'action dans les activites de la vie courante."
  "|Les actes de la vie quotidienne comprennent la toilette, l'habillage, l'alimentation et les deplacements."
  "|La dependance peut etre temporaire ou durable, partielle ou importante."
  "|Le handicap resulte d'une interaction entre une alteration et les barrieres de l'environnement."
  "|La classification internationale du fonctionnement distingue alteration, limitation d'activite et restriction de participation."
  "|Les barrieres architecturales, comme les marches, peuvent etre levees par des amenagements."
  "|Les aides techniques, canne, fauteuil, barres ou verticalisateur, compensent les limitations."
  "|Le projet personnalise est construit avec la personne, sa famille et les professionnels."
  "|La bientraitance impose le respect du rythme, du consentement et de la dignite de la personne."
  "|L'accompagnement vise le maintien de l'autonomie et de la participation sociale, pas seulement la securite."),
[Q("Quel facteur influence fortement le vieillissement ?", "L'age seul~Les conditions de vie et de sante~La couleur des yeux~Le groupe sanguin", 1,
    "Le vieillissement est heterogene et depend du mode de vie, des soins et de l'environnement."),
 Q("Quel acte appartient aux activites de la vie quotidienne ?", "La toilette~La lecture d'un article medical~La tarification~La prescription", 0,
    "Toilette, habillage, alimentation et deplacements sont des actes de la vie courante."),
 Q("Selon la classification internationale, que designe une restriction de participation ?", "Une lesion organique~Une difficulté a etre implique dans une situation de vie~Un simple symptome~Un examen", 1,
    "La restriction de participation concerne la vie sociale et les roles de la personne."),
 Q("Que permet un amenagement du logement ?", "Supprimer le handicap~Lever certaines barrieres de l'environnement~Remplacer la personne~Eviter tout accompagnement", 1,
    "L'environnement peut etre rendu accessible par des aménagements et des aides."),
 Q("Quel appareil est une aide technique ?", "Un fauteuil roulant~Un thermometre~Un stethoscope~Une balance", 0,
    "Fauteuil, canne, barres d'appui et verticalisateur compensent les limitations."),
 Q("Qui construit le projet personnalise ?", "Le seul medecin~La personne, sa famille et les professionnels~Le voisinage~Personne", 1,
    "Le projet est elabore de maniere collective avec la personne au centre."),
 Q("Quelle attitude releve de la bientraitance ?", "Imposer un rythme rapide~Respecter le rythme et demander l'accord~Agir sans explication~Decider a la place", 1,
    "La bientraitance respecte le consentement, la dignite et le rythme de la personne."),
 T("Analyser une situation de perte d'autonomie chez une personne agee et proposer un accompagnement adapte.",
    "Une personne de 85 ans qui a du mal a se lever et a faire sa toilette presente une perte d'autonomie partielle. L'analyse distingue ce qui vient de son etat physique, une faiblesse musculaire, et ce qui vient du logement, par exemple une salle de bain sans barres. Les actions consistent a installer des barres et un siege de douche, a prepare le materiel de toilette a portee de main, a proposer son aide sans l'imposer et a laisser la personne faire ce qu'elle peut encore faire. Le projet est reevalue apres quelques jours avec elle et sa famille.",
    "On attend l'analyse des causes, les amenagements, le respect du rythme et la reevaluation."),
 T("Expliquer pourquoi le handicap ne se reduit pas a une alteration du corps.",
    "Une alteration, comme une paralisie des membres inferieurs, ne produira pas les memes effets selon l'environnement. Avec un fauteuil, des rampes et des ascenseurs, la personne peut se deplacer et participer a la vie sociale. Sans ces elements, la meme alteration devient une restriction de participation. Le handicap est donc le resultat d'une interaction entre la personne et son environnement physique et social. C'est pourquoi l'accompagnement travaille autant sur les barrieres que sur les capacites de la personne.",
    "On attend la distinction alteration / limitation / restriction et le role des barrieres.")],
C("Accompagner une personne agee ou en situation de handicap, c'est agir sur ses capacites et sur son environnement.",
  "Alteration -> limitation d'activite -> restriction de participation",
  "Aides techniques + amenagements + projet personnalise + bientraitance",
  "Autonomie~Capacite d'agir~Handicap~Interaction avec l'environnement~Aide technique~Compensation~Projet personnalise~Decision partagee",
  "Evaluer les capacites restantes|Repérer les barrieres de l'environnement|Choisir les aides adaptees|Construire le projet avec la personne|Reevaluer regulierement",
  "Decider sans consulter la personne|Confondre alteration et handicap|Se focaliser sur la securite seule|Imposer un rythme trop rapide",
  "Personne agee~Vieillissement heterogene~Barres d'appui~Amenagement~Fauteuil~Aide technique~Toilette~Acte de la vie courante",
  "Perte d'autonomie~Reduction des capacites~Handicap~Interaction avec barrieres",
  "Bientraitance~Respect du rythme~Maltraitance~Imposition et negligences"))

# ============================================================ SST9
add("ST2S-B-SST09", "Ethique, secret professionnel et bientraitance en soins", STT, ["Terminale"],
S("L'ethique du soin interroge les choix professionnels face a des situations parfois conflictuelles."
  "|La bienfaisance vise a agir pour le bien de la personne ; la non-malfaisance evite de lui nuire."
  "|L'autonomie de la personne implique de respecter ses choix et son consentement libre et eclaire."
  "|La justice impose un traitement equitable et l'absence de discrimination."
  "|Le secret professionnel oblige les professionnels de sante a garder confidentielles les informations recueillies."
  "|Le secret est une obligation legale, mais il a des exceptions prevues par la loi."
  "|Le partage d'informations entre professionnels est autorise si il est necessaire a la prise en charge de la personne."
  "|La personne doit etre informee du partage d'informations et peut s'y opposer dans certains cas."
  "|La bientraitance suppose respect, consideration, ecoute et adapation aux besoins de la personne."
  "|La maltraitance peut etre active, par des gestes ou des paroles, ou passive, par negligence et abandon."
  "|Une situation de conflit d'interets ou de pression hierarchique doit pouvoir etre signalee."
  "|Le questionnement ethique se conduit en equipe, avec les procedures et les codes de deontologie de la profession."),
[Q("Quel principe demande de ne pas nuire a la personne ?", "La bienfaisance~La non-malfaisance~La justice~La liberte d'entreprendre", 1,
    "La non-malfaisance impose d'eviter les actions qui peuvent nuire au patient."),
 Q("Que signifie un consentement libre et eclaire ?", "Un accord donne sous pression~Un accord apres information et sans contrainte~Un silence~Une signature obligatoire", 1,
    "Le consentement est valable si la personne a ete informee et peut choisir librement."),
 Q("Quel est le principe de base du secret professionnel ?", "Tout dire a l'equipe~Ne pas divulguer les informations confidentielles~Publier le dossier~Oublier les donnees", 1,
    "Les informations recueillies dans le cadre du soin sont confidentielles."),
 Q("Dans quel cas le partage d'informations est-il autorise ?", "Pour la curiosite~Lorsqu'il est necessaire a la prise en charge~Pour le reseau social~Jamais", 1,
    "Le partage entre professionnels est permis s'il sert la prise en charge de la personne, dans le respect du secret partage."),
 Q("Quelle est une forme de maltraitance passive ?", "Une insulte~Une negligence ou un abandon de soin~Une gifle~Une menace", 1,
    "La maltraitance passive inclut le manque d'attention, d'hygiene ou de surveillance."),
 Q("Quel comportement releve de la bientraitance ?", "Agir sans expliquer~Respecter le rythme et la dignite~Forcer un soin~Ignorer une demande", 1,
    "La bientraitance associe respect, ecoute, explications et consideration."),
 Q("Que faire face a un conflit d'interets ?", "Le cacher~Le signaler selon la procedure~Le resoudre seul sans trace~Changer de sujet", 1,
    "Le conflit doit etre signale et traite selon les procedures de l'etablissement."),
 T("Une famille demande des informations sur un proche hospitalise. Que peut répondre le soignant dans le respect du secret ?",
    "Le soignant ne communique pas d'information medicale precise sans verification du droit de la famille a etre informee et sans l'accord de la personne, si celle-ci est apte a consentir. Il peut ecouter les inquietudes, expliquer le cadre legal du secret et proposer un entretien avec le medecin ou l'equipe soignante. Le secret medical n'est pas un refus d'ecoute : il protege la personne et sa confiance. Le partage d'informations avec d'autres professionnels est, lui, possible lorsqu'il est necessaire a la prise en charge et trace.",
    "On attend le respect du secret, l'ecoute, l'orientation vers le medecin et la distinction avec le secret partage."),
 T("Distinguer bienfaisance, non-malfaisance et respect de l'autonomie dans une situation de refus de soin.",
    "Un patient refuse une perfusion proposee par l'equipe. La bienfaisance pousse le soignant a rechercher ce qui pourrait aider, par exemple un autre mode d'hydratation ou une explication supplementaire. La non-malfaisance interdit d'imposer un acte contre le gre de la personne si son consentement est valable, car le contrainte est elle-meme un dommage. Le respect de l'autonomie impose de reconnaitre le droit de refuser apres information claire. Les trois principes peuvent entrer en tension : la decision se construit alors par le dialogue, l'evaluation de la capacite de consentement et, si besoin, une concertation en equipe.",
    "On attend les trois principes, la notion de consentement et la gestion d'une tension ethique.")],
C("L'ethique du soin arbitre entre bienfaisance, non-malfaisance, autonomie et justice, sous l'obligation de secret.",
  "Bienfaisance + non-malfaisance + autonomie + justice",
  "Secret professionnel · secret partage si necessaire · bientraitance active et passive",
  "Secret professionnel~Confidentialite obligatoire~Consentement~Accord libre et eclaire~Bientraitance~Respect et consideration~Justice~Egalite de traitement",
  "Identifier les principes en presence|Verifier la capacite de consentement|Respecter le secret|Autoriser un partage si necessaire|Signaler les situations problematiques",
  "Confondre secret et silence absolu|Imposer un soin sans consentement|Ignorer la maltraitance passive|Mélanger bientraitance et pitié",
  "Refus de soin~Autonomie~Entretien avec le medecin~Secret partage~Negligence~Maltraitance passive~Conflit d'interets~Signalement",
  "Bienfaisance~Agir pour le bien~Non-malfaisance~Eviter de nuire",
  "Secret professionnel~Confidentialite~Secret partage~Partage entre professionnels pour le soin"))

valider_et_ecrire(F, "st2s-mat-part-B.json")
