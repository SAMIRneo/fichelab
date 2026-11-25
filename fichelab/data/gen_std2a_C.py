# -*- coding: utf-8 -*-
"""Generateur std2a-mat-part-C.json — lot C : techniques et outils, methode, environnement (20 fiches).

Techniques et outils (8), Methodologie de projet de design (5),
Environnement professionnel et deontologie (4), Anglais du design (3).
Chaque fiche : 12 points, 9 questions (7 QCM + 2 texte), 7 blocs, 3 SVG.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _std2a_common import FIL, REF, S, R, QC, QT, C, build, valider_et_ecrire

F = []
T = ["1re", "Terminale"]
TER = ["Terminale"]

def add(prefix, titre, mat, ans, points, questions, c):
    F.append(build(prefix, titre, mat, ans, points, questions, c))

# ============================================================ TO01
add("TO01", "Dessin d'observation : trait, valeur et croquis", "Techniques et outils", T,
S("Le dessin d'observation s'appuie sur la vision et l'analyse de l'objet reel."
  "|On distingue le dessin d'observation, le dessin de memoire et le dessin d'imagination."
  "|Le geste doit rester libre : on commence par des traits legeres avant de renforcer."
  "|La ligne de construction situe les proportions et les axes principaux."
  "|La mise en place consiste a repérer les grands volumes avant les details."
  "|La valeur rend le volume avec les clairs, les demi-teintes et les ombres."
  "|Le trait variable, en epaisseur et en pression, exprime la lumiere et le materiau."
  "|Le croquis est rapide et synthetique : il capte l'essentiel en quelques minutes."
  "|La prise de notes graphiques complete le croquis par des mots et des fleches."
  "|Observer sous plusieurs angles enrichit la comprehension de la forme."
  "|Le carnet de croquis est un outil de memoire et de recherche personnelle."
  "|En STD2A, le dessin constitue le socle de toute pratique de conception."),
[QC("A quoi sert une ligne de construction ?", "A colorer l'objet~A situer proportions et axes~A signer le dessin~A effacer les traits", 1,
     "Les lignes de construction posent la structure avant le dessin definitif."),
 QC("Quelle est la premiere etape d'une mise en place ?", "Dessiner les details~Repérer les grands volumes~Choisir la couleur~Tracer l'ombre", 1,
     "On determine d'abord les volumes et les proportions d'ensemble."),
 QC("Que permet la valeur dans un dessin ?", "De choisir une police~De rendre le volume par les clairs et les ombres~De coter l'objet~De le photographer", 1,
     "Les valeurs clair-sombre construisent l'illusion du volume."),
 QC("Qu'est-ce qu'un croquis ?", "Un dessin technique coté~Un dessin rapide et synthetique~Une photographie~Un plan de fabrication", 1,
     "Le croquis capte l'essentiel rapidement, sans recherche du detail."),
 QC("Quel interet a observer un objet sous plusieurs angles ?", "Changer sa couleur~Mieux comprendre sa forme reelle~Le rendre plus petit~Supprimer les ombres", 1,
     "Les vues successives revelent des faces et des rapports invisibles de face."),
 QC("Quel role joue le carnet de croquis ?", "Remplacer l'atelier~Conserver memoire et recherches~Servir de facture~Imprimer les images", 1,
     "Il garde la trace des observations, des idees et des essais."),
 QC("Quel trait exprime le mieux la lumiere ?", "Un trait uniforme~Un trait variable en epaisseur et pression~Un trait invisible~Aucun trait", 1,
     "La pression et l'epaisseur du trait traduisent l'intensite de la lumiere."),
 QT("Decrire la demarche d'un dessin d'observation d'une chaise en cinq etapes.",
    "On observe d'abord la chaise sous plusieurs angles pour comprendre sa structure. On trace ensuite les lignes de construction : la hauteur totale, la largeur de l'assise et les axes des pieds. On place les grands volumes, le siege et le dossier, en verifiant les proportions. On ajoute les valeurs : les zones claires vers la source de lumiere, les ombres sous l'assise et le long des pieds. On termine par les details, les notes graphiques sur la matiere et un trait plus ferme sur les contours les plus proches. Le dessin est alors a la fois une analyse et une trace personnelle.",
    "On attend observation, construction, volumes, valeurs et details dans cet ordre."),
 QT("Pourquoi le dessin reste-t-il indispensable meme avec les outils numeriques ?",
    "Le dessin a la main entraine l'oeil a observer : proportions, lumiere, matiere et silhouette. Il permet de penser en direct, de tester une forme en quelques secondes et de garder une trace visible du raisonnement. Les outils numeriques sont rapides et precis, mais ils ne remplacent pas la capacite a juger une proportion ou a ressentir un volume. Dans une demarche de design, le croquis sert a communiquer une intention avant toute modelisation : on peut le montrer, le corriger, le superposer. Les deux pratiques sont complementaires : le dessin nourrit l'idee, l'ordinateur la precise et la diffuse.",
    "On doit defendre le role d'observation et de pensee du dessin, sans rejeter le numerique.")],
C("Le dessin d'observation apprend a voir : construction, volumes, valeurs et croquis rendent la forme comprehensible.",
  "Dessin = observation + construction + valeurs + intention",
  "trait · valeur · croquis · carnet · mise en place",
  "Observation~Regarder l'objet~Construction~Axes et proportions~Valeur~Clairs et ombres~Croquis~Trait rapide",
  "Observer sous plusieurs angles|Tracer les axes et les proportions|Placer les grands volumes|Construire les valeurs|Ajouter details et notes",
  "Dessiner de memoire sans regarder|Commencer par les details|Negliger les proportions|Ignorer la source de lumiere",
  "Chaise~Quatre pieds et un dossier~Trait ferme~Contour proche~Ombre~Sous l'assise~Carnet~Trace des idées~Valeur~Relief du volume",
  "Observation~Voir le reel~Imagination~Inventer une forme",
  "Croquis~Rapide et synthétique~Dessin technique~Precis et norme"))

# ============================================================ TO02
add("TO02", "Dessin technique : vues, cotes et convention", "Techniques et outils", T,
S("Le dessin technique transmet des informations precises et normalisees."
  "|Une vue represente l'objet projete selon une direction donnee."
  "|Les vues principales sont la vue de face, la vue de dessus et la vue de cote."
  "|La projection orthogonale conserve les dimensions reelles de l'objet."
  "|Une coupe montre l'interieur apres une section imaginee."
  "|La cotation indique les dimensions avec des unites et des tolerances."
  "|Les lignes ont des roles codifies : visible, cachee, axe, cote."
  "|L'echelle precise le rapport entre le dessin et l'objet reel."
  "|La nomenclature identifie les differentes pieces d'un ensemble."
  "|Le dessin technique sert a la fabrication et au controle."
  "|Il se distingue du croquis par son objectif de precision et de normalisation."
  "|La lecture d'un plan demande de reconstituer mentalement l'objet en trois dimensions."),
[QC("Quel type de projection conserve les dimensions reelles ?", "La perspective centrale~La projection orthogonale~La perspective cavaliere~Le croquis", 1,
     "La projection orthogonale conserve les grandeurs sans deformation liee a la distance."),
 QC("Quelle vue montre l'interieur d'un objet ?", "La vue de face~La coupe~La vue de dessus~L'elevation", 1,
     "La coupe represente ce que l'on verrait apres avoir sectionne l'objet."),
 QC("Quel est le role d'une ligne cachee ?", "Montrer un contour invisible~Indiquer une cote~Representer un axe~Decorer le plan", 0,
     "La ligne cachee, souvent en pointille, represente un contour non visible."),
 QC("Que designe l'echelle d'un dessin ?", "Le prix du plan~Le rapport entre dessin et objet reel~Le nombre de vues~L'epaisseur du papier", 1,
     "Une echelle 1:20 signifie que 1 unite sur le plan represente 20 unites reelles."),
 QC("A quoi sert la nomenclature ?", "A colorer le plan~A identifier les pieces d'un ensemble~A dater le document~A remplacer les cotes", 1,
     "La nomenclature repere chaque element avec un numero et une designation."),
 QC("Quelle information n'est pas donnee par une cote ?", "Une dimension~Une tolerance~Une unite~L'humeur du dessinateur", 3,
     "La cote est une information technique objective."),
 QC("Quel est l'objectif premier du dessin technique ?", "Surprendre le spectateur~Fabrication et controle~Decorer une page~Raconter une histoire", 1,
     "Il sert a definir l'objet pour le fabriquer et le verifier."),
 QT("Expliquer les differences entre un croquis et un dessin technique.",
    "Le croquis est rapide, libre et souvent subjectif : il capte une impression, une proportion ou une intention en quelques traits. Le dessin technique est norme, precis et objectif : il utilise des vues orthogonales, des lignes codifiees, des cotes, une echelle et une nomenclature. Le croquis accompagne la recherche et la communication d'une idee ; le dessin technique accompagne la fabrication et le controle. On peut passer de l'un a l'autre : le croquis explore, le dessin technique fixe. Les deux ont leur place dans un dossier de projet, car l'un montre le cheminement et l'autre la realisation.",
    "On attend l'opposition liberte / normalisation et l'usage respectif des deux dessins."),
 QT("Comment lire un plan comportant trois vues orthogonales ?",
    "On identifie d'abord les vues : la vue de face donne la hauteur et la largeur, la vue de dessus donne la profondeur et la largeur, la vue de cote donne la hauteur et la profondeur. On repere ensuite l'echelle et les axes de symetrie, puis on lit les cotes pour connaitre les dimensions reelles. On confronte les trois vues pour reconstituer mentalement les volumes : une ligne visible dans une vue correspond souvent a une arete dans une autre. Les lignes cachees et les coupes renseignent sur les parties internes. Enfin, on verifie la nomenclature pour associer chaque element a sa designation et a sa quantite.",
    "La demarche attendue : reconnaitre les vues, lire echelle et cotes, reconstituer le volume, utiliser coupes et nomenclature.")],
C("Le dessin technique code l'objet pour le fabriquer : vues, cotes, echelle et nomenclature remplacent l'impression par la precision.",
  "Vue + cote + echelle + nomenclature = plan exploitable",
  "projection orthogonale · coupe · lignes codifiees · tolerance",
  "Vue de face~Hauteur et largeur~Vue de dessus~Profondeur et largeur~Coupe~Voir l'interieur~Cote~Dimension reelle",
  "Identifier les vues et l'orientation|Lire echelle et unites|Decoder les types de lignes|Reconstituer les volumes|Verifier cotes et nomenclature",
  "Confondre vue et coupe|Ignorer l'echelle|Lire une ligne cachee comme un contour visible|Oublier les unites",
  "1:20~1 unite pour 20~Cote 350~Dimension en millimetres~Coupe AA~Section imaginee~Nomenclature~Liste des pieces~Axe~Ligne de symetrie",
  "Croquis~Libre et rapide~Dessin technique~Norme et precision",
  "Ligne visible~Contour apparent~Ligne cachee~Contour masque"))

# ============================================================ TO03
add("TO03", "CAO/DAO : principes et outils du dessin vectoriel", "Techniques et outils", T,
S("La CAO, conception assistee par ordinateur, aide a construire un dessin precis."
  "|Le DAO, dessin assiste par ordinateur, designe plus specialement le trace."
  "|Le dessin vectoriel repose sur des objets geometriques et des equations."
  "|Un vecteur est defini par des points, des segments et des courbes de Bezier."
  "|Contrairement a l'image matricielle, le vectoriel reste net a tout agrandissement."
  "|Les calques permettent de separer les elements et de gerer leur visibilite."
  "|Les styles et les bibliotheques accelerent la realisation et assurent la coherence."
  "|L'accrochage et la grille facilitent un alignement precis."
  "|Les operations booleennes, comme l'union ou la soustraction, combinent des formes."
  "|L'export se fait en formats vectoriels (SVG, PDF, AI, DXF) ou en image."
  "|L'outil informatique ne remplace pas l'intention : il accelere l'exploration."
  "|La maitrise de la CAO/DAO est attendue dans le pole Outils et methodes STD2A."),
[QC("Que signifie CAO ?", "Conception assistee par ordinateur~Copie automatique d'objets~Creation analogue optique~Calcul architectural obligation", 0,
     "CAO signifie conception assistee par ordinateur."),
 QC("Sur quoi repose le dessin vectoriel ?", "Sur des pixels~Sur des objets geometriques et des equations~Sur des couleurs seulement~Sur la photographie", 1,
     "Le vectoriel decrit des formes par des points et des mathematiques."),
 QC("Quel avantage a le vectoriel par rapport au matriciel ?", "Il est toujours plus colore~Il reste net lors d'un agrandissement~Il est toujours plus petit~Il ne peut pas etre imprime", 1,
     "Les courbes vectorielles sont recalculees a la taille d'affichage."),
 QC("Quel element permet de separer les elements d'un dessin ?", "La couleur de fond~Les calques~La resolution~Le format d'export", 1,
     "Les calques organisent et masquent independamment les differents elements."),
 QC("Quel role joue l'accrochage ?", "Colorier les formes~Aligner precisement sur des points ou des objets~Supprimer les calques~Remplacer la grille", 1,
     "L'accrochage magnétique facilite le raccord et l'alignement precis."),
 QC("Quelle operation booleenne permet de retirer une forme d'une autre ?", "L'union~La soustraction~La duplication~La rotation", 1,
     "La soustraction retire la surface d'une forme a une autre."),
 QC("Quel format est vectoriel ?", "JPEG~SVG~BMP~PNG", 1,
     "Le SVG est un format vectoriel ; JPEG, BMP et PNG sont matriciels."),
 QT("Expliquer pourquoi un logo doit etre dessine en vectoriel.",
    "Un logo sert sur des supports tres varies, d'une petite vignette sur un ecran a une grande affiche ou une gravure. En vectoriel, les contours sont decrits par des points et des courbes : le logiciel les recalcule a la taille voulue, ce qui garantit un trait net a tout agrandissement. En matriciel, l'agrandissement rend les pixels visibles et le logo devient flou. Le vectoriel facilite aussi les declinaisons de couleur, les modifications de forme et l'export vers differents formats (SVG pour le web, PDF pour l'impression, DXF pour la découpe). C'est pourquoi les chartes graphiques livrent toujours les fichiers sources vectoriels.",
    "On attend l'independance a la resolution et les avantages pour les declinaisons."),
 QT("Comment organiser un fichier de CAO/DAO pour qu'il reste exploitable ?",
    "On donne des noms clairs aux calques et on les repartit par fonction : construction, contours, texte, cotes, annotations. On utilise des styles enregistres pour les lignes, les couleurs et les typographies, afin d'eviter les variations inutiles. On travaille avec la grille et l'accrochage pour garantir des alignements precis. Les elements repetitifs sont places dans des bibliotheques ou des symboles reutilisables. On classe les objets par ordre logique et on masque les calques de construction avant l'export. Enfin, on enregistre differentes versions datees et on documente les unites et l'echelle dans le fichier. Cette rigueur permet a un autre designer de reprendre le travail.",
    "On attend calques nommes, styles, accrochage, bibliotheques et versions.")],
C("La CAO/DAO rend le dessin precis et reutilisable : vecteurs, calques, styles et accrochage structurent le travail.",
  "Vecteur = points + segments + courbes de Bezier",
  "CAO · DAO · calques · booleens · SVG / PDF / DXF",
  "Vecteur~Points et courbes~Calque~Separation des elements~Accrochage~Alignement précis~Style~Coherence",
  "Definir les unites et la grille|Nommer les calques par fonction|Creer les formes avec les outils vectoriels|Appliquer styles et operations booleennes|Exporter dans le format adapte",
  "Dessiner sans grille ni accrochage|Laisser les calques sans nom|Confondre SVG et JPEG|Ne garder que le fichier final",
  "SVG~Web et vectoriel~PDF~Impression~DXF~Echange technique~Bezier~Courbe souple~Booleen~Union ou soustraction",
  "Vectoriel~Net a tout agrandissement~Matriciel~Depend des pixels",
  "CAO~Concevoir~DAO~Tracer"))

# ============================================================ TO04
add("TO04", "CAO 3D : modelisation, maillage et rendu", "Techniques et outils", ["1re", "Terminale"],
S("La modelisation 3D construit un objet numerique dans un espace a trois dimensions."
  "|La modelisation solide utilise des primitives et des operations booleennes."
  "|La modelisation surfacique travaille sur des surfaces et des courbes de haute qualite."
  "|Le maillage represente l'objet par des faces, souvent triangulaires."
  "|La densite du maillage influe sur la qualite visuelle et le poids du fichier."
  "|Les modificateurs appliquent des transformations non destructives."
  "|Les materiaux numeriques definissent couleur, rugosite, metal et transparence."
  "|L'eclairage et la camera determinent le rendu de l'image."
  "|Le rendu calcule l'image finale a partir de la geometrie, des materiaux et de la lumiere."
  "|L'impression 3D necessite un maillage etanche et une orientation des pieces."
  "|Le fichier est exporte dans un format adapte : STL, OBJ, FBX ou STEP."
  "|La 3D sert au prototype, a la visualisation et a la fabrication numerique."),
[QC("Qu'appelle-t-on un maillage ?", "Un repertoire de couleurs~Une representation de l'objet par des faces~Un type de camera~Un format de texte", 1,
     "Le maillage est un ensemble de sommets, d'aretes et de faces, souvent triangulaires."),
 QC("Quel effet a une densite de maillage elevee ?", "Un fichier plus leger~Une meilleure qualite mais un fichier plus lourd~Aucun effet~Une couleur plus vive", 1,
     "Plus de faces donnent une forme plus lisse mais augmentent le poids du fichier."),
 QC("Quel est l'interet d'un modificateur non destructif ?", "Supprimer les materiaux~Modifier la forme sans perdre la geometrie d'origine~Remplacer la camera~Aplatir l'image", 1,
     "On peut revenir sur le parametre et corriger le modele a tout moment."),
 QC("Que definit un materiau numerique ?", "La seule couleur~Couleur, rugosite, metal, transparence~Le nombre de faces~Le format du fichier", 1,
     "Le materiau regroupe les proprietes visuelles de la surface."),
 QC("Quelle condition pour imprimer un objet en 3D ?", "Un maillage etanche~Une couleur brillante~Une camera reglee~Un fond blanc", 0,
     "Le modele doit etre ferme, sans trou, pour etre interpretable par le slicer."),
 QC("Quel format est courant pour l'impression 3D ?", "JPEG~STL~DOCX~MP3", 1,
     "Le format STL decrit la surface d'un objet par un maillage triangulaire."),
 QC("Quel role joue le rendu ?", "Creer la geometrie~Calculer l'image finale a partir de la scene~Exporter le plan~Mesurer les cotes", 1,
     "Le rendu produit l'image en combinant geometrie, materiaux, lumiere et camera."),
 QT("Comparer modelisation solide et modelisation surfacique.",
    "La modelisation solide manipulate des volumes simples, appelés primitives, que l'on assemble ou que l'on soustrait avec des operations booleennes. Elle est robuste, adaptée aux pieces techniques et a la fabrication, car le resultat est un volume ferme. La modelisation surfacique travaille sur des courbes et des surfaces de haute qualite, souvent avec des points de controle : elle permet de realiser des formes organiques et des carrosseries plus fluides. Elle demande plus de maitrise et peut produire des maillages plus difficiles a reparer. En pratique, un projet altere souvent les deux approches : volumique pour la structure, surfacique pour les formes visibles.",
    "On attend l'opposition primitives et booleens / courbes et surfaces, avec des usages distincts."),
 QT("Expliquer la chaine de travail d'un objet du croquis a l'impression 3D.",
    "On part d'un croquis qui fixe les proportions et l'intention. On construit ensuite le modele 3D avec des primitives ou des surfaces, en gardant des parametres modifiables. On verifie la coherence du maillage : pas de trous, pas de faces inversees, une epaisseur suffisante. On applique les materiaux et on regle l'eclairage pour obtenir un rendu qui montre la forme. Puis on exporte en STL, on importe dans le logiciel de tranchage, on choisit l'orientation, la hauteur de couche et les remplissages. On lance l'impression, on mesure la piece obtenue et on corrige le modele si necessaire. Chaque etape reste documentee dans le dossier de projet.",
    "On attend croquis, modele, verification du maillage, rendu, export, tranchage et controle.")],
C("La CAO 3D passe du volume au maillage puis a l'image : geometrie, materiaux, lumiere et fabrication forment une chaine continue.",
  "Scene 3D = geometrie + materiaux + lumiere + camera",
  "primitives · booleens · maillage · modificateurs · STL",
  "Primitives~Volumes de base~Maillage~Faces et sommets~Materiau~Proprietes de surface~Rendu~Image calculee",
  "Partir du croquis et des proportions|Construire le volume ou la surface|Verifier l'etancheite du maillage|Regler materiaux lumiere et camera|Exporter et controler la piece",
  "Ignorer les trous du maillage|Augmenter le maillage sans besoin|Oublier l'orientation d'impression|Confondre rendu et modele",
  "STL~Impression 3D~STEP~Echange technique~Rugosite~Aspect de surface~Slicer~Preparation d'impression~Booleen~Assembler ou soustraire",
  "Solide~Volumes fermes~Surfaces~Courbes et peaux",
  "Mat~Surface diffusee~Brillant~Reflexion nette"))

# ============================================================ TO05
add("TO05", "Image numérique : pixels, resolution et formats", "Techniques et outils", T,
S("Une image matricielle est composee de pixels disposes sur une grille."
  "|La resolution designe le nombre de pixels, par exemple 3000 sur 2000."
  "|La definition, en points par pouce, determine la qualite a l'impression."
  "|Une image de faible resolution parait pixellisee quand on l'agrandit."
  "|La profondeur de couleur indique le nombre de nuances par pixel, en 8 ou 16 bits."
  "|Les modes de couleur sont RVB pour l'ecran et CMJN pour l'impression."
  "|Les formats courants sont JPEG, PNG, TIFF et GIF, selon l'usage."
  "|La compression peut etre sans perte, comme PNG, ou avec perte, comme JPEG."
  "|Le recadrage et le redimensionnement modifient la resolution utile."
  "|La resolution d'ecran et celle d'impression ne se comparent pas de la meme maniere."
  "|La resolution doit etre choisie selon le support final de diffusion."
  "|Une image bien preparee garde sa qualite du fichier source jusqu'au support."),
[QC("Qu'est-ce qu'un pixel ?", "Un format de fichier~Le plus petit element d'une image matricielle~Une couleur d'encre~Un type de police", 1,
     "Le pixel est l'unite elementaire d'une image matricielle."),
 QC("Que designe une resolution de 3000 × 2000 ?", "Trois mille couleurs~Le nombre de pixels en largeur et en hauteur~La taille du fichier en octets~Le nombre de calques", 1,
     "Elle indique la dimensions de la grille de pixels."),
 QC("Quel format conserve les transitions et la transparence sans perte ?", "JPEG~PNG~BMP~GIF", 1,
     "Le PNG est sans perte et gere la transparence, utile pour le graphisme."),
 QC("Quel mode de couleur utiliser pour l'impression ?", "RVB~CMJN~RVB et CMJN ensemble~Noir et blanc", 1,
     "L'impression utilise les encres cyan, magenta, jaune et noir."),
 QC("Quel phenomene apparait quand on agrandit trop une image ?", "Une pixellisation~Une meilleure nettete~Une augmentation de la saturation~Une disparition des couleurs", 0,
     "Les pixels deviennent visibles et les contours deviennent anguleux."),
 QC("Quelle compression conserve toutes les donnees ?", "JPEG~PNG~MP3~JPG", 1,
     "Le PNG utilise une compression sans perte, contrairement au JPEG."),
 QC("Quel critere determine la resolution a choisir ?", "Le nom du fichier~Le support final de diffusion~L'ordre des calques~La date de creation", 1,
     "Une image web, une affiche et une impression livre n'ont pas les memes besoins."),
 QT("Expliquer la difference entre resolution en pixels et definition en points par pouce.",
    "La resolution en pixels designe le nombre total de points constituant l'image, par exemple 3000 × 2000, soit six millions de pixels. La definition en points par pouce indique la densite avec laquelle ces pixels sont repartis sur une surface physique. Une meme image de six millions de pixels pourra etre imprimee en grande taille a 150 ppp ou en plus petit format a 300 ppp. Pour l'ecran, on raisonne surtout en pixels et en taille d'affichage ; pour l'impression, la densite par pouce determine la finesse du rendu. Une image de qualite doit fournir assez de pixels pour la taille et la destination prevues.",
    "On attend la distinction nombre de pixels / densite d'impression et un exemple."),
 QT("Comment choisir le format d'une image pour un projet de design graphique ?",
    "On se demande d'abord ou l'image sera utilisee. Pour une photographie destinee au web ou a une affiche, le JPEG offre un bon compromis entre qualite et poids, en acceptant une legere perte. Pour un logo, une illustration avec des aplats ou une image necessitant de la transparence, le PNG est preferable car il est sans perte. Pour l'impression de haute qualite et les archives, le TIFF conserve le maximum d'informations, eventuellement avec les profils colorimetriques. Le GIF reste utile pour de simples animations. On garde toujours un fichier source non compresse et on exporte une copie adaptee a chaque support, en controlant la taille finale.",
    "On attend un choix justifie selon l'usage et la preservation d'un fichier source.")],
C("L'image numerique se prepare selon son support : pixels, definition, mode de couleur et format conditionnent sa qualite finale.",
  "Qualite = pixels suffisants + bon format + bon mode de couleur",
  "matriciel · RVB / CMJN · PNG / JPEG / TIFF · compression",
  "Pixel~Unite de l'image~Resolution~Nombre de pixels~Definition~Points par pouce~Format~Extension du fichier",
  "Definir le support final|Verifier la resolution disponible|Choisir le mode de couleur|Selectionner le format adapte|Conserver un fichier source",
  "Agrandir une petite image|Confondre RVB et CMJN|Utiliser JPEG pour un logo avec aplats|Supprimer le fichier source",
  "3000 × 2000~Six megapixels~300 ppp~Impression fine~PNG~Sans perte et transparence~JPEG~Photo web~TIFF~Archive",
  "RVB~Ecran~CMJN~Impression",
  "Sans perte~PNG TIFF~Avec perte~JPEG"))

# ============================================================ TO06
add("TO06", "Retouche d'image : calques, masques et correction", "Techniques et outils", T,
S("La retouche d'image modifie une photographie pour servir un propos precis."
  "|Les calques superposent des elements independamment les uns des autres."
  "|Un masque de calque cache ou revele des parties sans effacer les pixels."
  "|Les outils de selection isolent une zone pour un traitement local."
  "|Les corrections de niveau et de courbes reglent la luminosite et le contraste."
  "|La balance des blancs corrige la temperature de la lumiere."
  "|Le recadrage et la rotation restructurent la composition."
  "|Le clonage et le patch restaurent des zones endommagees."
  "|Les filtres et les styles appliquent des effets, avec moderation."
  "|Le travail non destructif permet de revenir sur chaque correction."
  "|L'ethique de l'image interdit de tromper le public par une retouche dissimulee."
  "|Les fichiers sources et les etapes de retouche doivent etre archives."),
[QC("Quel interet a un masque de calque ?", "Effacer definitivement des pixels~Cacher ou reveler sans detruire~Changer le format~Ajouter du texte", 1,
     "Le masque rend une partie invisible tout en preservant les donnees d'origine."),
 QC("Que permettent les courbes de niveau ?", "De recadrer l'image~De regler luminosite et contraste~De changer de police~De reduire le fichier", 1,
     "Les courbes et niveaux ajustent la repartition des valeurs."),
 QC("Quel outil isole une zone precis pour un traitement local ?", "La selection~Le masque global~La rotation~L'export", 0,
     "La selection limite l'action des outils a une region choisie."),
 QC("Que corrige la balance des blancs ?", "La nettete~La temperature de la lumiere~La resolution~Le nombre de calques", 1,
     "Elle neutralise une dominante chaude ou froide due a l'eclairage."),
 QC("Quel principe guide une retouche professionnelle ?", "Tout modifier sans trace~Travailler de maniere non destructive~Supprimer tous les calques~Utiliser un seul filtre", 1,
     "Le travail non destructif permet de revenir sur chaque decision."),
 QC("Quel risque ethique concerne la retouche ?", "Une image trop nette~Une image trompeuse presentee comme reelle~Un fichier trop leger~Une couleur trop vive", 1,
     "Modifier le reel en le presentant comme tel peut induire le public en erreur."),
 QC("Que faut-il conserver apres une retouche ?", "Seule l'image finale~Le fichier source et l'historique des etapes~Le seul format JPEG~La photographie papier", 1,
     "Les sources et les etapes permettent de reprendre et de justifier le travail."),
 QT("Decrire une methode de retouche non destructive d'une photo de produit.",
    "On importe la photo et on duplique le calque d'origine, qui reste intact. On recadre sur un calque de rotation legerement, puis on regle la balance des blancs et les courbes avec des calques de réglage. On isole le produit avec un outil de selection et on cree un masque pour corriger uniquement les reflets indesirables. Les zones abimees sont restaurees avec un calque vide et l'outil de clonage, sans toucher a la photo d'origine. On nomme chaque calque et on note les operations dans le dossier de projet. On exporte enfin une copie au format demandé, en gardant le fichier multi-calcques comme source.",
    "On attend duplication, calques de reglage, masque, nommage et export final."),
 QT("Ou se situe la limite entre retouche legitime et manipulation trompeuse ?",
    "Une retouche legitime ameliore la lisibilite : recadrage, exposition, contraste, depoussiérage ou suppression d'un reflet gênant, des lors que le produit reste fidele a ce qui sera livre. La manipulation trompeuse ajoute, retire ou modifie un element qui change la perception du produit ou de la realite, puis le presente comme authentique. Par exemple, simuler une fonction inexistante ou masquer un defaut majeur est abusif. La limite est donc liee a l'intention et a la transparence : dans une campagne publicitaire, certaines transformations sont acceptees si elles sont annoncees, mais un documentaire ou une photo de reportage exigent une bien plus grande rigueur. Le designer doit pouvoir justifier chaque intervention.",
    "On attend la notion de fidelite au reel, d'intention et de transparence.")],
C("La retouche doit rester maitrisee et transparente : calques, masques et reglages non destructifs preservent le travail et l'ethique.",
  "Retouche non destructive = calques + masques + reglages",
  "selection · courbes · balance des blancs · clonage · ethique",
  "Calque~Superposition independante~Masque~Cache sans effacer~Selection~Zone isolee~Courbes~Reglage des valeurs",
  "Dupliquer le calque source|Regler exposition et couleur|Isoler les zones avec un masque|Restaurer et nommer les calques|Exporter et archiver le source",
  "Travailler sur l'original|Ignorer les dominantes de couleur|Abuser des filtres|Presente une retouche comme une photo brute",
  "Courbes~Luminosite et contraste~Balance des blancs~Temperature~Clonage~Restauration locale~Masque~Visibilite controlee~Export~Copie finale",
  "Destructive~Modifie l'original~Non destructive~Preserve le source",
  "Retouche~Ameliorer la lisibilite~Manipulation~Tromper le public"))

# ============================================================ TO07
add("TO07", "Prise de vue et cadrage : lumiere et composition", "Techniques et outils", T,
S("La photographie de design sert a documenter et a mettre en valeur un objet."
  "|Le cadrage choisit ce qui est inclus et la place du sujet dans l'image."
  "|La regle des tiers aide a placer le sujet de maniere dynamique."
  "|L'angle de vue modifie la perception de la forme et de l'echelle."
  "|La lumiere naturelle et la lumiere artificielle produisent des ambiances differentes."
  "|La direction de la lumiere modele les volumes et revele les matieres."
  "|L'ouverture, la vitesse et la sensibilite reglent l'exposition."
  "|La profondeur de champ determine la nettete de l'avant et de l'arriere-plan."
  "|Le fond et les accessoires construisent le contexte de l'objet."
  "|La resolution et le format de capture dependent de l'usage final."
  "|La prise de vue multiple facilite le montage et le choix de l'image."
  "|Le photographe et le designer construisent ensemble l'intention de l'image."),
[QC("Quel principe aide a placer le sujet de maniere dynamique ?", "La regle des tiers~La regle des trois couleurs~Le format carre~La symetrie absolue", 0,
     "La regle des tiers place le sujet sur des lignes et intersections imaginaires."),
 QC("Quel effet a la direction de la lumiere ?", "Elle change le prix~Elle modele les volumes et revele les matieres~Elle supprime le fond~Elle reduit la resolution", 1,
     "Une lumiere laterale accentue les reliefs et les textures."),
 QC("Quel reglage determine la nettete de l'arriere-plan ?", "La vitesse~L'ouverture~La sensibilite~Le format du fichier", 1,
     "L'ouverture de l'objectif controle la profondeur de champ."),
 QC("Quel element construit le contexte de l'objet photographie ?", "Le seul objectif~Le fond et les accessoires~Le nom du fichier~La date", 1,
     "Le decor et les accessoires situent l'objet et racontent un usage."),
 QC("Pourquoi realiser plusieurs prises de vue ?", "Pour remplir la carte memoire~Pour disposer de choix au montage~Pour eviter de regler la lumiere~Pour changer de format", 1,
     "Les variations de cadrage et d'exposition offrent plusieurs options."),
 QC("Quel parametre change l'ambiance generale d'une photo ?", "La qualite de la lumiere~Le nombre de pixels~Le nom du dossier~Le logiciel de retouche", 0,
     "La lumiere, naturelle ou artificielle, donne le ton de l'image."),
 QC("Qui defini l'intention d'une photographie de produit ?", "Le seul hasard~Le photographe et le designer ensemble~Le fournisseur~Le format", 1,
     "L'intention se construit en dialogue entre le createur et le photographe."),
 QT("Comment photographier un objet pour montrer a la fois sa forme et sa matiere ?",
    "On choisit d'abord un angle qui revele la silhouette et les plans principaux, souvent legerement au-dessus ou de trois quarts. On installe une lumiere principale laterale pour faire apparaitre les reliefs et les textures, avec une lumiere d'appoint pour eviter les ombres trop dures. On regle l'ouverture pour garder l'objet net tout en adoucissant le fond. On utilise un fond neutre qui ne concurrence pas l'objet, puis on ajoute eventuellement un accessoire pour indiquer l'echelle ou l'usage. On fait plusieurs prises en faisant varier l'angle et l'exposition, puis on selectionne celle qui sert le mieux le message du projet.",
    "On attend angle, direction de la lumiere, profondeur de champ, fond et variantes."),
 QT("Comment la regle des tiers ameliore-t-elle un cadrage ?",
    "La regle des tiers consiste a divider mentalement l'image en trois parties egales, horizontalement et verticalement. Placer le sujet principal sur une de ces lignes ou a leur intersection evite le centre geometrique, souvent plus statique. L'oeil dispose alors d'un espace de respiration devant le regard ou le mouvement du sujet. Pour un objet, on peut aligner un bord important sur une ligne et laisser le vide agir a cote. Ce n'est pas une loi absolue : un cadrage centre peut etre choisi pour une symetrie volontaire. La regle est un outil qui aide a composer, a condition de la mettre au service de l'intention et non de l'appliquer mecaniquement.",
    "On attend l'explication du principe, son effet et la possibilite d'y deroger.")],
C("La prise de vue construit une image : cadrage, lumiere, ouverture et contexte servent l'intention du projet.",
  "Image = cadrage + lumiere + exposition + contexte",
  "regle des tiers · profondeur de champ · direction de la lumiere",
  "Cadrage~Champ de l'image~Regle des tiers~Placement dynamique~Lumiere~Modele et ambiance~Ouverture~Profondeur de champ",
  "Definir l'intention de l'image|Choisir angle et cadrage|Installer et orienter la lumiere|Regler exposition et profondeur|Verifier fond et variantes",
  "Centrer systematiquement le sujet|Eclairer de face sans relief|Negliger le fond|Ne faire qu'une seule prise",
  "Trois quarts~Vue dynamique~Lumiere laterale~Reliefs et matieres~Fond neutre~Objet mis en valeur~Accessoire~Indice d'echelle~Prise multiple~Choix au montage",
  "Lumiere naturelle~Ambiance changeante~Lumiere artificielle~Controle precis",
  "Grande ouverture~Faible profondeur~Petite ouverture~Grande profondeur"))

# ============================================================ TO08
add("TO08", "Mise en page et PAO : grille, colonnes et export", "Techniques et outils", T,
S("La PAO, publication assistee par ordinateur, assemble textes et images."
  "|Une mise en page repose sur une grille et des marges coherentes."
  "|Les colonnes structurent le flux de lecture d'une page ou d'un document."
  "|Les styles de paragraphe assurent la coherence typographique."
  "|Les images sont liees ou integrees, avec une resolution suffisante."
  "|Le texte peut etre compose en flux continu ou en cadres independants."
  "|Les repères et les guides facilitent l'alignement des elements."
  "|La pagination et les pages paralleles doivent etre verifiees."
  "|Les couleurs sont gerees en RVB ou en CMJN selon la destination."
  "|L'export PDF integre les polices et les images pour l'impression."
  "|Un controle avant impression verifie fonds perdus, marges et liens."
  "|La mise en page sert la lecture avant de servir la decoration."),
[QC("Que signifie PAO ?", "Preparation artistique optimum~Publication assistee par ordinateur~Photographie analogique ordinaire~Programme d'analyse optique", 1,
     "PAO signifie publication assistee par ordinateur."),
 QC("Quel role jouent les colonnes ?", "Decorer la page~Structurer le flux de lecture~Remplacer les marges~Reduire le nombre de pages", 1,
     "Les colonnes organisent le texte et guident le parcours du lecteur."),
 QC("Pourquoi utiliser des styles de paragraphe ?", "Pour accelerer la saisie~Pour garantir une coherence typographique~Pour changer de logiciel~Pour supprimer les images", 1,
     "Les styles centralisent les regles et simplifient les modifications globales."),
 QC("Quel risque presente une image liee plutot qu'integree ?", "Elle devient plus nette~Un lien rompu peut rendre l'image absente~Elle change de couleur~Elle occupe moins de place", 1,
     "Si le fichier source est deplace, le document ne retrouve plus l'image."),
 QC("Que controle un fond perdu ?", "La couleur du texte~L'impression jusqu'au bord de la page~Le nombre de colonnes~La resolution de l'ecran", 1,
     "Le fond perdu prevoit une zone au-dela de la coupe pour eviter les liseres blancs."),
 QC("Que doit contenir un PDF destine a l'impression ?", "Les seuls textes~Les polices et les images integrees~Le logiciel source~Les calques ouverts", 1,
     "L'export doit embarquer les polices et les images pour garantir le rendu."),
 QC("Quel principe prime en mise en page ?", "La decoration~La qualite de lecture~Le nombre d'effets~La taille du fichier", 1,
     "La mise en page est d'abord un service rendu a la lecture."),
 QT("Decrire une methode de verification avant l'impression d'une brochure.",
    "On verifie d'abord les marges, les fonds perdus et les pages paralleles, en controlant que les elements importants ne sont pas trop proches de la coupe. On contrôle ensuite que les images ont une resolution suffisante et que les liens sont bien integres. On examine les styles typographiques, les interlignages et les eventuels textes debordants. On passe le document en CMJN si l'impression le demande et on verifie les profils colorimetriques. On genere un PDF avec les polices embarquees, puis on l'ouvre pour verifier la pagination. Une epreuve papier ou un BAT permet de valider le rendu final avant le tirage.",
    "On attend marges, fonds perdus, resolution, couleurs, polices et epreuve."),
 QT("Comment une grille ameliore-t-elle la coherence d'une brochure ?",
    "La grille definit des marges, un nombre de colonnes et un rythme vertical identifies. En plaçant chaque titre, image ou paragraphe sur ces repères, on obtient des alignements coherents d'une page a l'autre. Le lecteur retrouve les memes points de repere, ce qui rend la lecture plus rapide et le document plus professionnel. La grille n'empeche pas la creativite : elle cadre les variations et permet desechappements ponctuels, par exemple une image a cheval sur deux colonnes, a condition que l'ecart reste lisible. Il faut la construire des le debut du projet et la documenter pour que tous les contributeurs l'utilisent.",
    "On attend le role d'alignement, la regularite pour le lecteur et la possibilite de variations maitrisees.")],
C("La PAO assemble les elements dans une grille : styles, images, couleurs et export garantissent un document lisible et imprimable.",
  "Document = grille + styles + images + export PDF",
  "colonnes · fond perdu · RVB / CMJN · polices embarquees",
  "Grille~Marges et colonnes~Style~Regle typographique~Image~Lier ou integrer~Export~PDF final",
  "Construire la grille et les marges|Definir les styles de paragraphe|Placer textes et images|Gerer couleurs et resolution|Verifier et exporter le PDF",
  "Placer les elements sans grille|Laisser des images non integrees|Oublier les fonds perdus|Exporter en RVB pour l'impression",
  "Fond perdu~Au-dela de la coupe~CMJN~Encres d'impression~PDF~Fichier de livraison~BAT~Epreuve de validation~Colonnes~Flux de lecture",
  "Liee~Depend du fichier source~Integree~Contenue dans le document",
  "Ecran~RVB~Papier~CMJN"))

# ============================================================ MP01
add("MP01", "Analyse de la demande : brief, acteurs et contraintes", "Méthodologie de projet de design", T,
S("Le projet de design commence par une demande explicite ou implicite."
  "|Le brief rassemble le contexte, l'objectif, le public et les contraintes."
  "|Le commanditaire est la personne ou l'organisation qui passe commande."
  "|Le destinataire est l'usager final, distinct du commanditaire."
  "|Les acteurs du projet ont des attentes parfois contradictoires."
  "|On distingue les besoins fonctionnels, expressifs et symboliques."
  "|Les contraintes peuvent etre techniques, financieres, reglementaires ou temporelles."
  "|Une bonne question de depart delimite le probleme sans imposer la solution."
  "|L'analyse de l'existant evite de reinventer une solution deja eprouvee."
  "|La reformulation du besoin verifie la comprehension du brief."
  "|Les hypotheses sont notees et hierarchees avant la recherche de formes."
  "|Cette phase conditionne la pertinence de tout le projet."),
[QC("Que contient un brief ?", "Uniquement le prix~Contexte, objectif, public et contraintes~La seule signature~Le nom du designer", 1,
     "Le brief rassemble les informations de depart du projet."),
 QC("Qui est le destinataire d'un projet ?", "Le commanditaire~L'usager final~Le fournisseur~Le correcteur", 1,
     "Le destinataire est la personne qui utilisera le produit ou le service."),
 QC("Quelle question de depart est bien formulee ?", "Comment faire une belle chaise ?~Comment rendre l'attente plus confortable dans une salle d'attente ?~Quelle couleur choisir ?~Combien coute le bois ?", 1,
     "Elle delimite un probleme d'usage sans imposer une solution."),
 QC("Quel besoin concerne l'image et le sens d'un objet ?", "Fonctionnel~Expressif ou symbolique~Technique~Financier", 1,
     "Les besoins expressifs et symboliques portent sur la signification et l'emotion."),
 QC("Laquelle de ces contraintes est reglementaire ?", "Le budget~Une norme de securite~Le gout du client~La couleur du bureau", 1,
     "Une norme de securite est une contrainte reglementaire."),
 QC("A quoi sert l'analyse de l'existant ?", "A copier un concurrent~A eviter de refaire une solution deja eprouvee~A supprimer le brief~A choisir la police", 1,
     "Elle permet d'apprendre des solutions et des erreurs precedentes."),
 QC("Pourquoi reformuler le besoin ?", "Pour rallonger le dossier~Pour verifier la comprehension du brief~Pour changer de client~Pour eviter le dessin", 1,
     "La reformulation triche la lecture du commanditaire et du designer."),
 QT("Reformuler un brief de commanditaire en probleme de design.",
    "Un commanditaire demande « une nouvelle lampe de bureau moderne ». Le designer ne doit pas en deduire directement une forme. Il reformule : « comment concevoir un eclairage de travail qui réduit la fatigue visuelle, s'installe sur un bureau encombre et soit facile a orienter d'une seule main ? » Cette question precise le contexte d'usage, les besoins fonctionnels et les contraintes d'espace. Elle laisse ouvertes les pistes de solution : la lampe pourra etre articulee, fixee au bord du bureau ou equipee d'une lumiere reglable. La reformulation se soumet ensuite au commanditaire pour valider la comprehension commune avant toute recherche formelle.",
    "On attend une question centre sur l'usage et les contraintes, sans solution imposee."),
 QT("Comment identifier et hierarchiser les contraintes d'un projet ?",
    "On rassemble d'abord toutes les contraintes exprimees ou deduites : budget, delai, dimensions, normes de securite, materiaux disponibles, exigences environnementales et attentes culturelles. On les classe ensuite en categories, puis on distingue les contraintes eliminatoires, qui doivent absolument etre respectees, des contraintes souhaitables, qui peuvent faire l'objet d'un compromis. On evalue leur impact sur la solution et leur degree d'incertitude. Les plus structurantes sont placees en tete de cahier des charges et servent de criteres de selection des hypotheses. Enfin, on verifie avec le commanditaire que la hierarchie est partagee, car une contrainte oubliee peut invalider tout le projet.",
    "On attend recensement, classement, distinction eliminatoire/souhaitable et validation.")],
C("L'analyse de la demande transforme une commande en probleme de design : acteurs, besoins et contraintes doivent etre clairs avant toute forme.",
  "Brief = contexte + objectif + public + contraintes",
  "commanditaire · destinataire · besoins · reformulation",
  "Commanditaire~Passe commande~Destinataire~Utilisateur final~Brief~Donnees de depart~Contrainte~Limite au projet",
  "Lire le brief et ecouter le commanditaire|Identifier acteurs et destinataires|Degager les besoins fonctionnels et symboliques|Recenser et hierarchiser les contraintes|Reformuler le probleme et valider",
  "Confondre commanditaire et usager|Proposer une forme avant d'analyser|Ignorer les besoins implicites|Oublier de valider la reformulation",
  "Lampe~Bureau encombre~Besoin~Reduire la fatigue~Contrainte~Espace et budget~Question~Comment orienter d'une main~Validation~Accord du commanditaire",
  "Besoin fonctionnel~Ce que l'objet doit faire~Besoin symbolique~Ce que l'objet signifie",
  "Contrainte eliminatoire~Non negociable~Contrainte souhaitable~Compromis possible"))

# ============================================================ MP02
add("MP02", "Cahier des charges : besoins, criteres et livrables", "Méthodologie de projet de design", T,
S("Le cahier des charges formalise les attentes et les limites du projet."
  "|Il precise le contexte, les objectifs et les destinataires."
  "|Il liste les fonctions attendues et les performances minimales."
  "|Il distingue les contraintes eliminatoires des preferences."
  "|Les criteres d'evaluation doivent etre mesurables ou observables."
  "|Un planning fixe les etapes et les echeances."
  "|Un budget encadre les moyens financiers et les ressources."
  "|Les livrables sont explicitement definis : croquis, plans, maquettes et rapport."
  "|Les responsabilites et les modalites de validation sont indiquees."
  "|Le cahier des charges est un document de reference, evolutif et date."
  "|Il sert a la fois au commanditaire et a l'equipe de conception."
  "|Un cahier des charges clair reduit les malentendus et les reprises."),
[QC("Que formalise un cahier des charges ?", "Le seul style du designer~Les attentes et les limites du projet~Le prix de vente futur~La biography du client", 1,
     "Il fixe les besoins, les contraintes et les modalites du projet."),
 QC("Quel critere est observable ?", "Un objet joli~Une hauteur de 45 centimetres~Un style agréable~Une impression moderne", 1,
     "Une dimension mesurable est un critere observable et verifiable."),
 QC("Quelle difference existe-t-il entre contrainte eliminatoire et preference ?", "La preference est obligatoire~La contrainte eliminatoire doit etre respectee~Elles sont identiques~La contrainte est facultative", 1,
     "Une contrainte eliminatoire conditionne la validite de la solution."),
 QC("Quel element du planning est indispensable ?", "La couleur du tableau~Les etapes et les echeances~Le nom du fournisseur~La taille de la police", 1,
     "Le planning repartit les etapes dans le temps."),
 QC("Qu'appelle-t-on un livrable ?", "Un outil de dessin~Un element attendu en fin d'etape~Un client~Une contrainte", 1,
     "Les livrables designent ce que le designer doit rendre : croquis, plans, maquettes, rapport."),
 QC("Pourquoi dater le cahier des charges ?", "Pour le rendre plus long~Pour suivre les revisions et eviter les confusions~Pour impressionner~Pour changer de client", 1,
     "Les versions datees permettent de savoir quelle reference est en vigueur."),
 QC("A quoi sert la modalite de validation ?", "A supprimer les reunions~A preciser qui valide quoi et comment~A remplacer le budget~A eviter les livrables", 1,
     "Elle definit les points d'accord et les responsables de la decision."),
 QT("Remplir les grandes lignes d'un cahier des charges pour une signaletique de musee.",
    "Contexte : un musee de quartier souhaite renouveler sa signaletique. Objectif : permettre a tous les visiteurs de se repérer seul en moins de deux minutes. Destinataires : familles, seniors, visiteurs allophones et personnes a mobilite reduite. Fonctions : indiquer les salles, les sorties et les services, avec un systeme cohérent. Contraintes eliminatoires : respecter les normes de securite, rester lisible a trois metres et ne pas depasser le budget imparti. Criteres : temps de repérage observe, contraste mesuré, comprehension des pictogrammes. Planning : analyse, propositions, test, livraison sur huit semaines. Livrables : planches de principes, plans d'implantation, maquettes et guide d'usage. Validation : accord du directeur a chaque etape.",
    "On attend contexte, objectif, destinataires, contraintes, criteres, planning, livrables et validation."),
 QT("Comment faire évoluer un cahier des charges sans perdre le fil du projet ?",
    "Le cahier des charges doit rester un document vivant mais controle. Chaque changement est consigne par ecrit avec sa date, son motif et son auteur. On evalue son impact sur les autres elements : une nouvelle contrainte de budget peut obliger a revoir les materiaux, le planning et les livrables. On soumet la modification aux acteurs concernes et on obtient un accord explicite avant de l'appliquer. On conserve les versions precedentes pour pouvoir comparer et comprendre l'historique des decisions. Enfin, on met a jour les criteres de selection si besoin, afin que l'analyse des hypotheses reste coherente avec les exigences revisees. Cette rigueur evite les malentendus et les reprises inutiles.",
    "On attend trace ecrite, evaluation d'impact, accord, conservation des versions et mise a jour des criteres.")],
C("Le cahier des charges est la reference commune : besoins, criteres, planning, budget et livrables rendent le projet verifiable et partage.",
  "Cahier des charges = besoins + contraintes + criteres + livrables",
  "planning · budget · validation · version datee",
  "Cahier des charges~Reference du projet~Besoin~Fonction attendue~Criteres~Ce qui sera evalue~Livrable~Ce qui est rendu",
  "Ecrire contexte et objectifs|Lister fonctions et contraintes|Definir des criteres observables|Fixer planning budget et livrables|Faire valider et dater chaque version",
  "Rester vague sur les livrables|Confondre preference et contrainte|Oublier les modalites de validation|Modifier sans laisser de trace",
  "Criteres~Temps et contraste~Contrainte~Securite et budget~Planning~Huit semaines~Livrables~Plans et maquettes~Validation~Accord a chaque etape",
  "Contrainte eliminatoire~Doit etre respectee~Preference~Peut etre negociee",
  "Cahier des charges~Avant le projet~Dossier de conception~Pendant et apres"))

# ============================================================ MP03
add("MP03", "Ideation et selection : hypotheses, comparaison, choix", "Méthodologie de projet de design", T,
S("L'ideation produit des hypotheses de reponse au probleme pose."
  "|On explore plusieurs pistes avant de se fixer sur une solution."
  "|Chaque hypothese est representee par un croquis, un schema ou une maquette."
  "|La comparaison s'appuie sur des criteres issus du cahier des charges."
  "|Une matrice de selection permet de noter chaque piste objectivement."
  "|Il faut distinguer les criteres necessaires et les criteres souhaitables."
  "|Une hypothese peut etre combinee avec une autre pour en renforcer une troisieme."
  "|La faisabilite technique et le cout doivent etre evalues des cette etape."
  "|Le choix n'est pas seulement esthetique : il doit etre argumente."
  "|Les pistes rejetees sont conservees comme traces de la recherche."
  "|L'analyse comparative est presentee dans le dossier de projet."
  "|La selection prepare la phase de prototype et de test."),
[QC("Quelle est la premiere phase de l'ideation ?", "Choisir une solution~Explorer plusieurs pistes~Fabriquer le produit~Imprimer le rapport", 1,
     "On produit d'abord un large eventail d'hypotheses avant de selectionner."),
 QC("Que permet une matrice de selection ?", "De colorer les croquis~De noter objectivement chaque piste selon des criteres~De remplacer le brief~De reduire le nombre de pages", 1,
     "La matrice rend la comparaison transparente et argumentee."),
 QC("Quel critere est necessaire plutot que souhaitable ?", "Une couleur preferee~Une contrainte de securite a respecter~Un style personnel~Une taille de police", 1,
     "Une contrainte de securite est eliminatoire : sans elle, la solution est refuse."),
 QC("Que faut-il faire des pistes rejetees ?", "Les detruire~Les conserver comme trace de la recherche~Les ignorer~Les donner au client", 1,
     "Elles temoignent du cheminement et de la richesse de l'exploration."),
 QC("A quoi sert de combiner deux hypotheses ?", "A compliquer le projet~A renforcer une troisieme proposition~A supprimer les criteres~A eviter le prototype", 1,
     "La combinaison peut produire une solution plus complete."),
 QC("Quand evaluer la faisabilite technique ?", "Apres la fabrication~Des l'etape de selection~Jamais~A la soutenance seulement", 1,
     "Verifier la faisabilite tot evite de developper une solution impossible."),
 QC("Quel est un critere de choix valide ?", "Le gout du designer seul~Un argument lie au besoin et aux contraintes~Le hasard~La longueur du croquis", 1,
     "Un choix pertinent s'appuie sur des criteres explicites et argumentes."),
 QT("Comment construire une matrice de selection pour trois hypotheses de mobilier ?",
    "On liste d'abord les criteres tires du cahier des charges : reponse au besoin, confort, cout, resistance, facilitatede fabrication et impact environnemental. On distingue les criteres necessaires, qui doivent tous etre satisfaits, des criteres souhaitables que l'on pondere. On place les trois hypotheses en lignes et les criteres en colonnes, puis on attribue une note pour chaque case en justifiant brievement. On calcule une synthese, mais on ne la suit pas aveuglement : une hypothese peut etre retenue pour une qualite non prevue initialement. On conserve la matrice dans le dossier de projet et on l'utilise pour expliquer le choix final a l'oral.",
    "On attend criteres, distinction necessaire/souhaitable, notation et discussion du resultat."),
 QT("Pourquoi ne pas selectionner une seule idee des le debut ?",
    "Une premiere idee est rarement la meilleure : elle souffre souvent d'un manque de recul et d'exploration. Si on s'y arrete, on ne peut plus la comparer a des alternatives et on risque de resoudre un probleme mal defini. Produire plusieurs hypotheses permet de tester differentes interpretations du besoin, de faire emerger des criteres inattendus et de combiner des pistes. Cela rend aussi le projet plus riche a presenter, car on peut montrer un cheminement plutot qu'un resultat impose. Enfin, l'echec d'une piste enseigne autant que la reussite d'une autre : il faut donc documenter les tentatives avant de choisir.",
    "On doit defendre la comparaison, la decouverte de criteres et la valeur des pistes abandonnees.")],
C("L'ideation explore puis selectionne : le choix final resulte d'une comparaison argumentee, pas d'une preference immediate.",
  "Ideation = diverger puis converger selon des criteres",
  "matrice · criteres necessaires / souhaitables · faisabilite · traces",
  "Hypothese~Piste de reponse~Matrice~Comparaison objective~Criteres~Bases du choix~Faisabilite~Possibilite de realisation",
  "Produire plusieurs hypotheses|Les representer par croquis ou maquette|Definir et ponderer les criteres|Remplir la matrice et discuter|Documenter le choix et garder les traces",
  "S'arreter a la premiere idee|Choisir uniquement pour des raisons esthetiques|Jeter les pistes rejetees|Oublier le cout et la faisabilite",
  "Criteres~Confort cout impact~Necessaire~Contrainte eliminatoire~Souhaitable~Preference ponderee~Matrice~Notes comparees~Choix~Argument final",
  "Necessaire~Doit etre satisfait~Souhaitable~Ameliore la solution",
  "Ideation~Produire des pistes~Selection~Choisir et justifier"))

# ============================================================ MP04
add("MP04", "Prototypage et test : iteration et validation", "Méthodologie de projet de design", T,
S("Un prototype est une representation intermediaire destinee a tester une hypothese."
  "|Il peut etre papier, numerique, volumique ou fonctionnel selon le besoin."
  "|La maquette d'etude explore la forme et le volume."
  "|La maquette de presentation communique le projet au commanditaire."
  "|Le prototype rapide permet de se tromper tot et a peu de cout."
  "|Le test observe l'usage reelle dans des conditions proches du contexte final."
  "|On mesure des criteres : comprehension, temps, erreurs et confort."
  "|Les resultats sont notes et classes par gravite."
  "|L'iteration corrige un point a la fois pour identifier la cause des problemes."
  "|Le prototype n'est pas une fin : il sert a apprendre et a decider."
  "|Le projet alterne cycles de prototype, test et ajustement."
  "|La validation finale intervient quand les criteres du cahier des charges sont satisfaits."),
[QC("Quelle est la finalite d'un prototype ?", "Etre le produit final~Tester une hypothese~Decorer le dossier~Remplacer le brief", 1,
     "Le prototype sert a apprendre et a verifier une hypothese avant la realisation."),
 QC("Quel prototype explore la forme et le volume ?", "La maquette de presentation~La maquette d'etude~Le plan de fabrication~Le devis", 1,
     "La maquette d'etude est un outil de recherche sur la forme."),
 QC("Quel avantage a un prototype rapide ?", "Une meilleure finition~Se tromper tot et a peu de cout~Une fabrication industrielle~Un prix de vente plus eleve", 1,
     "Il permet de detecter les erreurs avant qu'elles ne deviennent couteuses."),
 QC("Que mesure un test utilisateur ?", "La couleur preferee~Comprehension, temps, erreurs et confort~Le nombre de pages~Le prix du materiau", 1,
     "Ces indicateurs rendent l'usage observable et comparable."),
 QC("Pourquoi corriger un point a la fois ?", "Pour aller plus vite~Pour identifier la cause du probleme~Pour changer de couleur~Pour eviter les notes", 1,
     "Un changement isole permet de comprendre ce qui a ameliore la situation."),
 QC("Quand intervient la validation finale ?", "Des le premier croquis~Quand les criteres du cahier des charges sont satisfaits~Avant le brief~Apres la soutenance uniquement", 1,
     "La validation confronte le resultat aux exigences definies au depart."),
 QC("Quel statut a le prototype dans le projet ?", "Une fin en soi~Un outil d'apprentissage et de decision~Un document administratif~Une contrainte inutile", 1,
     "Il fait progresser la reflexion et aide a decider."),
 QT("Decrire un cycle de prototypage pour une interface de borne interactive.",
    "On construit d'abord un prototype papier : quelques ecrans dessines a la main suffisent pour tester le parcours. On demande a plusieurs personnes de realiser une tache, par exemple trouver un horaire, en observant leurs hésitations. On note les points de blocage : un bouton trop petit, un libelle ambigu, une etape superflue. On corrige un point precis, par exemple le libelle, puis on refait un test court. Une fois le parcours clair, on passe a un prototype numerique cliquable qui teste les transitions et la lisibilite des couleurs. On termine par une maquette en situation reelle pour verifier la hauteur de l'ecran et la distance de lecture. Chaque cycle est documente.",
    "On attend papier puis numerique, observation, correction isolee et documentation."),
 QT("Pourquoi faut-il tester en conditions proches du contexte reel ?",
    "Un objet peut etre confortable sur un bureau de test et impossible a utiliser dans un atelier bruyant, avec des gants ou sous une lumiere differente. Le contexte modifie la posture, la duree d'attention, les gestes et meme la comprehension des symboles. Tester en situation permet de decouvrir les usages improvises et les contraintes oubliees dans le cahier des charges : encombrement, reach, luminosite, bruit ou presence d'autres personnes. Cela ne remplace pas les tests en laboratoire, qui offrent un controle plus precis, mais les complete. Un bon protocole alterne donc des tests controls et des observations en milieu reel, en notant a chaque fois les conditions de passage.",
    "On attend l'influence du milieu sur les gestes et la complementarite des deux types de tests.")],
C("Le prototype sert a apprendre : on teste tot, on observe, on corrige une cause a la fois, puis on valide au regard du cahier des charges.",
  "Prototype → test → analyse → iteration → validation",
  "maquette d'etude · prototype papier · criteres · gravite · contexte reel",
  "Prototype~Modele intermediaire~Test~Observation d'usage~Iteration~Correction ciblee~Validation~Conformite au besoin",
  "Choisir le type de prototype|Definir le protocole et les criteres|Observer des utilisateurs reels|Classer les problemes par gravite|Corriger et re-tester avant validation",
  "Attendre le produit fini pour tester|Changer plusieurs elements a la fois|Ignorer le contexte reel|Considerer le prototype comme une reussite",
  "Prototype papier~Test rapide du parcours~Maquette d'etude~Travail sur le volume~Maquette de presentation~Communication au client~Test~Tache observee~Validation~Criteres satisfaits",
  "Maquette d'etude~Explorer la forme~Maquette de presentation~Communiquer le resultat",
  "Iteration~Corriger et recommencer~Validation~Arreter les cycles"))

# ============================================================ MP05
add("MP05", "Presentation de projet : soutenance, planche et argumentaire", "Méthodologie de projet de design", TER,
S("La presentation restitue la demarche et les resultats du projet."
  "|Elle s'adapte au public : commanditaire, jury, pair ou grand public."
  "|Une planche de presentation organise image, texte et titre de maniere lisible."
  "|Le fil conducteur suit generalement besoin, recherche, choix et realisation."
  "|Chaque choix est justifie par un argument issu de l'analyse."
  "|Les visuels doivent etre de qualite et legendes."
  "|La soutenance orale s'appuie sur des notes, pas sur la lecture d'un texte."
  "|Le temps imparti impose une selection des informations essentielles."
  "|Les gestes, la voix et le regard participent a la conviction."
  "|La question du jury est une occasion de defendre et de nuancer le projet."
  "|Le dossier de conception complete la presentation par les traces de recherche."
  "|Une presentation reussie rend visible la pensee autant que l'objet final."),
[QC("Quel est le premier critere d'une presentation reussie ?", "Le nombre de diapositives~L'adaptation au public vise~La taille de la police~Le cout de la planche", 1,
     "Un discours efficace tient compte de ceux qui l'ecoutent et de leurs attentes."),
 QC("Quel fil conducteur est couramment utilise ?", "Resultat, besoin, choix, recherche~Besoin, recherche, choix, realisation~Choix, resultat, besoin, recherche~Recherche, resultat, public, besoin", 1,
     "On reconstitue generalement le cheminement dans l'ordre logique du projet."),
 QC("Comment justifier un choix de forme ?", "En disant que l'on aime~En s'appuyant sur un argument issu de l'analyse~En montrant beaucoup d'images~En evitant les questions", 1,
     "La justification relie la decision a un besoin, une contrainte ou un test."),
 QC("Quel role jouent les notes en soutenance ?", "A lire mot pour mot~A guider l'oral sans etre lues~A remplacer les visuels~A impressionner le jury", 1,
     "Elles soutiennent le discours, qui reste adresse a l'auditoire."),
 QC("Quel effet a un temps imparti limite ?", "Il faut tout montrer~Il fautselectionner l'essentiel~Il faut parler plus vite~Il faut supprimer les images", 1,
     "Le temps contraint oblige a hierarchiser le contenu."),
 QC("Que faut-il faire face a une question du jury ?", "Repondre sans ecouter~Ecouter, repondre precisement et nuancer~Refuser de repondre~Changer de sujet", 1,
     "La question est un echange qui permet de defense le projet avec nuances."),
 QC("Que contient le dossier de conception ?", "Seule la photo finale~Les traces de recherche et les etapes~Le seul devis~La liste des fournisseurs", 1,
     "Il documente le cheminement : croquis, tests, matrices, sources et versions."),
 QT("Comment construire une planche de presentation lisible pour un projet de design ?",
    "On choisit un format et une grille, puis on definit une hierarchie claire : un titre court, une image principale, quelques visuels de detail et un texte de synthese. Le texte doit etre bref, avec des phrases complètes et des legendes qui expliquent ce que montre chaque image. Les couleurs restent limitees et coherentes avec l'identite du projet. On aligne les elements sur la grille et on laisse des marges suffisantes pour que la planche respire. On verifie la lisibilite a distance, car une planche est souvent regardee de plusieurs metres. Enfin, on controlle l'impression et les noms de fichiers pour une livraison sans erreur.",
    "On attend grille, hierarchie, textes brefs, legende, coherence et controle final."),
 QT("Comment defendre un projet dont un choix est conteste par le jury ?",
    "On commence par ecouter la question et la reformuler pour etre sur de l'avoir comprise. On repond ensuite en rappelant le besoin et la contrainte qui ont motive le choix, puis les elements de preuve : comparaison de pistes, test utilisateur, analyse de cout ou de materiau. Si la critique est juste, on la reconnait et on explique ce que l'on ferait differemment avec plus de temps ou d'informations. Si l'on n'est pas d'accord, on expose son raisonnement sans se braquer. Dans tous les cas, on reste attentif au regard et au ton. Une bonne defense ne consiste pas a avoir toujours raison, mais a montrer que le projet a ete pense et qu'il peut etre discute.",
    "On attend ecoute, arguments, reconnaissance eventuelle et posture constructive.")],
C("La presentation rend le cheminement visible : adaptée au public, elle articule images, arguments courts et soutenance vivante.",
  "Besoin → recherche → choix → realisation → question",
  "planche · hierarchie · notes · temps · dossier de conception",
  "Planche~Support visuel~Titre~Entree de lecture~Legende~Explication d'image~Soutenance~Oral et regards",
  "Identifier le public et le temps disponible|Construire le fil conducteur|Preparer planches et visuels|Ecrire des notes courtes|Repeter et anticiper les questions",
  "Lire un texte ecrit|Montrer tous les croquis|Negliger les legendes|Eviter les questions du jury",
  "Titre court~Repere immediat~Image principale~Message central~Legende~Sens du visuel~Notes~Guide oral~Dossier~Traces du projet",
  "Planche~Vue synthese~Dossier~Detail du cheminement",
  "Soutenance~Defendre a l'oral~Lecture~Recopier un texte"))

# ============================================================ DP01
add("DP01", "Metiers du design et parcours de formation", "Environnement professionnel et déontologie", T,
S("Le design couvre de nombreux domaines : graphique, produit, espace, mode et service."
  "|Le designer graphique concoit des messages et des identites visuelles."
  "|Le designer produit travaille sur les objets et leur fabrication."
  "|Le designer d'espace intervient sur les lieux de vie et la scenographie."
  "|Le designer de service structure des parcours et des interactions."
  "|Les metiers d'art mobilisent des savoir-faire techniques specifiques."
  "|Les employeurs sont les agences, les bureaux d'etudes, les entreprises et les collectivites."
  "|Le freelance travaille a son compte pour plusieurs clients."
  "|Les formations vont du bac STD2A aux ecoles superieures d'art et de design."
  "|La veille professionnelle permet de suivre les tendances et les outils."
  "|Un portfolio personnel est indispensable pour montrer son travail."
  "|Les competences attendues melangent culture, technique, methode et communication."),
[QC("Quel domaine concoit des identites visuelles ?", "Le design produit~Le design graphique~Le design d'espace~Le design industriel", 1,
     "Le design graphique travaille sur les messages et les identites visuelles."),
 QC("Quel metier intervient sur la scenographie ?", "Designer produit~Designer d'espace~Designer de service~Verrier", 1,
     "Le designer d'espace concoit des lieux de vie, des expositions et des scenes."),
 QC("Qu'est-ce qu'un designer de service ?", "Un vendeur~Un concepteur de parcours et d'interactions~Un architecte~Un imprimeur", 1,
     "Il structure les parcours d'usage et les points de contact avec un service."),
 QC("Quel employeur est typique d'un designer freelance ?", "Un seul employeur salarie~Plusieurs clients pour lesquels il travaille a son compte~L'administration uniquement~Aucun client", 1,
     "Le freelance exerce a son compte et gere plusieurs clients."),
 QC("Quel outil permet de suivre l'evolution des outils et des tendances ?", "Le portfolio~La veille professionnelle~Le devis~La facture", 1,
     "La veille reguliere tient informe des pratiques et des nouveautes."),
 QC("Que montre un portfolio ?", "Les seules notes scolaires~Des projets representatifs du travail du designer~Le salaire souhaite~La liste des clients", 1,
     "Il presente des realisations, la demarche et le role du concepteur."),
 QC("Quelles competences sont attendues chez un designer ?", "Culture, technique, methode et communication~La seule maitrise du dessin~Le seul sens commercial~La seule connaissance des logiciels", 0,
     "Le metier exige un croisement de savoirs et de savoir-faire."),
 QT("Comparer le metier de designer produit et celui de designer d'espace.",
    "Le designer produit intervient sur des objets : il travaille la forme, la fonction, les materiaux et les procedes de fabrication, en tenant compte de la production de serie et de l'usage domestique ou industriel. Le designer d'espace intervient a une echelle plus grande : il organise des lieux de vie, des magasins, des expositions ou des scenes, en considerant les circulations, la lumiere, l'acoustique et les usagers. Les deux partagent une methode : analyser un besoin, produire des hypotheses, prototyper et presenter. Ils se differencient par l'echelle, les contraintes techniques et les livrables : plans et maquettes plutot que dessins de piece et fichiers de fabrication.",
    "On attend la comparaison des objets d'etude, des contraintes et des livrables."),
 QT("Comment construire un portfolio efficace apres une annee de STD2A ?",
    "On selectionne quelques projets representatifs, varies dans leurs domaines, plutot que de tout montrer. Pour chaque projet, on presente le contexte, le besoin, une image finale forte et deux ou trois visuels de recherche qui montrent le cheminement. On ecrit un texte court qui precise son role, les outils utilises et ce que l'on a appris. On soigne la mise en page, la qualite des images et la coherence graphique de l'ensemble. On ajoute une presentation personnelle et un moyen de contact. Enfin, on demande un regard externe, on corrige et on garde une version propre a jour, prete a etre envoyee ou presentee sur tablette.",
    "On attend selection, structure par projet, traces de recherche, texts brefs et mise a jour.")],
C("Les metiers du design partagent une methode mais different par l'echelle, les outils et les livrables : la veille et le portfolio accompagnent le parcours.",
  "Designer = culture + technique + methode + communication",
  "graphique · produit · espace · service · metiers d'art · freelance",
  "Design graphique~Messages et identites~Design produit~Objets et fabrication~Design d'espace~Lieux et scenes~Design de service~Parcours",
  "Explorer les differentes specialites|Identifier les employeurs et les formations|Choisir une veille adaptee|Construire un portfolio|Actualiser regulierement ses presentations",
  "Reduire le design a un seul metier|Ne montrer que des images finales|Negliger la veille|Copier le portfolio d'un autre",
  "Agence~Travail en equipe~Freelance~Plusieurs clients~STD2A~Bac technologique~Ecole superieure~Poursuite d'etudes~Portfolio~Preuve de competence",
  "Produit~Objet et serie~Espace~Lieux et circulation",
  "Salarie~Un employeur~Freelance~Son propre compte"))

# ============================================================ DP02
add("DP02", "Droit d'auteur et propriete intellectuelle", "Environnement professionnel et déontologie", T,
S("Le droit d'auteur protege les oeuvres de l'esprit des leur creation."
  "|Il comprend des droits moraux et des droits patrimoniaux."
  "|Le droit moral assure notamment la paternite et le respect de l'oeuvre."
  "|Les droits patrimoniaux permettent d'autoriser ou d'interdire l'exploitation."
  "|La protection est automatique, sans depot obligatoire."
  "|Le plagiat consiste a s'approprier une oeuvre sans citation ni autorisation."
  "|Une licence definit les conditions d'utilisation d'une oeuvre ou d'un logo."
  "|Les ressources libres et le domaine public ont des regles distinctes."
  "|Les marques protegent les signes distinctifs des produits et services."
  "|Les brevets protegent des inventions techniques sous conditions."
  "|Dans un projet, chaque image, police et son utilise doit etre identifie."
  "|La tracabilite des sources protege le designer et respecte les createurs."),
[QC("Quand le droit d'auteur s'applique-t-il ?", "Apres un depot obligatoire~Des la creation de l'oeuvre~Apres publication seulement~Apres cinq ans", 1,
     "La protection est automatique des la creation, sans formalite de depot."),
 QC("Que garantit le droit moral ?", "Le prix de vente~La paternite et le respect de l'oeuvre~L'exclusivite commerciale~La duree du contrat", 1,
     "Le droit moral protege notamment le nom de l'auteur et l'integrite de l'oeuvre."),
 QC("Quels droits permettent d'autoriser une exploitation ?", "Les droits moraux~Les droits patrimoniaux~Le droit de vote~Le droit de reponse", 1,
     "Les droits patrimoniaux donnent le controle de l'usage economique de l'oeuvre."),
 QC("Quel est un exemple de plagiat ?", "Citer une source~Reprendre une image sans autorisation ni mention~Acheter une licence~Creer une oeuvre originale", 1,
     "Le plagiat s'approprie une creation sans reconnaissances ni autorisation."),
 QC("Que definit une licence ?", "Le prix d'un logo~Les conditions d'utilisation d'une oeuvre~La couleur d'une marque~Le format d'un fichier", 1,
     "La licence precise qui peut utiliser l'oeuvre, comment et pendant combien de temps."),
 QC("Que protege une marque ?", "Une invention technique~Un signe distinctif de produits ou services~Une idee generale~Un sentiment", 1,
     "La marque protege les signes qui distinguent une offre commerciale."),
 QC("Que faut-il identifier dans un projet de design ?", "La seule couleur dominante~Chaque image, police et son utilise~Le nombre de pages~Le nom du client uniquement", 1,
     "Tous les elements empruntes doivent etre reperes et documentes."),
 QT("Expliquer la difference entre droits moraux et droits patrimoniaux.",
    "Les droits moraux sont attaches a la personne de l'auteur : ils garantissent la paternite, le respect de l'oeuvre et le droit de la retrier ou de s'y opposer a certaines modifications. Ils sont en principe incessibles. Les droits patrimoniaux sont de nature economique : ils permettent d'autoriser ou d'interdire la reproduction, la representation, l'adaptation ou la diffusion, et ils peuvent etre cedes ou licenses pour une duree et un territoire determines. Dans une commande de design, le client obtient generalement une licence d'usage et non la totalite des droits : il faut donc ecrire precisement ce qui est autorise dans le contrat.",
    "On attend la distinction personne / economie et la consequence concrete sur une commande."),
 QT("Comment securiser l'usage des images dans un projet d'etudiant ?",
    "On privilégie d'abord ses propres photographies et dessins, qui ne dependent d'aucune autorisation externe. Lorsqu'on utilise une image trouvee, on verifie sa licence, son auteur et les usages autorises : une image gratuite pour un usage personnel ne l'est pas forcement pour une affiche diffusee. On conserve une capture de la page de licence et la date de consultation. On cite l'auteur et le titre dans le dossier de projet et sur la planche lorsque c'est possible. On evite les polices et les musiques sans licence claire. Enfin, on garde un tableau de tracabilite avec la source, le format et les conditions d'usage de chaque element. Cela protege l'etudiant et respecte les createurs.",
    "On attend verification des licences, citations, conservation des preuves et tableau de tracabilite.")],
C("Le droit d'auteur protege automatiquement les creations : identifier les sources, comprendre les licences et tracer les usages est une responsabilite professionnelle.",
  "Droits moraux + droits patrimoniaux = protection de l'oeuvre",
  "plagiat · licence · domaine public · marque · brevet · tracabilite",
  "Droit moral~Paternite et respect~Droits patrimoniaux~Exploitation economique~Licence~Conditions d'usage~Plagiat~Appropriation",
  "Recenser tous les elements empruntes|Verifier l'auteur et la licence|Conserver les preuves de consultation|Citer et tracer les usages|Rediger clairement les autorisations",
  "Croire qu'une image trouvee en ligne est libre|Confondre licence et achat d'oeuvre|Oublier de citer|Utiliser une police sans verifier",
  "Image~A verifier~Police~Licence a controler~Son~Droits a verifier~Domaine public~Sans droits~Marque~Signe distinctif~Brevet~Invention technique",
  "Droit moral~Incessible~Droit patrimonial~Cedable",
  "Plagiat~Sans autorisation~Licence~Autorisation ecrite"))

# ============================================================ DP03
add("DP03", "Ethique, deontologie et responsabilite du designer", "Environnement professionnel et déontologie", T,
S("L'ethique interroge ce qui est juste au-dela de la seule legalite."
  "|La deontologie rassemble les regles de conduite propres a une profession."
  "|Le designer doit respecter la dignite des personnes representees."
  "|Il evite les stereotypes et les representations discriminatoires."
  "|Il est responsable des effets sociaux et environnementaux de ses choix."
  "|Le secret professionnel peut s'appliquer aux informations du commanditaire."
  "|Le conflit d'interets doit etre signale et gere."
  "|La publicite mensongere et le greenwashing sont des pratiques a refuser."
  "|L'accessibilite est une exigence ethique autant que technique."
  "|La transparence sur le processus et les limites du projet est recommandee."
  "|Un refus professionnel peut etre oppose a une demande contraire a l'ethique."
  "|La responsabilite s'exerce devant le client, le public et la societe."),
[QC("Quelle difference existe-t-il entre ethique et deontologie ?", "Elles sont identiques~L'ethique interroge le juste, la deontologie code la profession~La deontologie est une loi~L'ethique est un contrat", 1,
     "L'ethique est une reflexion morale, la deontologie un ensemble de regles professionnelles."),
 QC("Quelle representation doit etre evitee ?", "Une representation diverse~Un stereotype discriminatoire~Une photo de qualite~Une legende claire", 1,
     "Les stereotypes figeant des groupes et peuvent etre discriminatoires."),
 QC("Quel effet environnemental relève de la responsabilite du designer ?", "Le choix des materiaux et des procedes~Le prix de vente~Le nom du client~Le nombre de pages du dossier", 0,
     "Les choix de conception influencent l'impact environnemental du produit."),
 QC("Quand signaler un conflit d'interets ?", "Jamais~Des qu'il apparait~A la fin du projet~Uniquement au tribunal", 1,
     "Le signalement des le debut permet une gestion transparente."),
 QC("Qu'est-ce que le greenwashing ?", "Une certification~Une communication qui surestime l'impact ecologique~Un materiau recycle~Une norme de qualite", 1,
     "Le greenwashing presente une action comme ecologique sans fondement reel."),
 QC("Quelle exigence est a la fois ethique et technique ?", "La vitesse d'execution~L'accessibilite~La couleur de la maquette~Le nombre de logiciels", 1,
     "Rendre un projet accessible est un choix moral et une exigence de conception."),
 QC("Peut-on refuser une demande contraire a l'ethique ?", "Non, jamais~Oui, par un refus professionnel~Seulement si le client est d'accord~Uniquement devant un juge", 1,
     "Le designer peut refuser une demande qui heurte ses principes professionnels."),
 QT("Comment un designer peut-il refuser une demande problematique sans rompre la relation client ?",
    "Il commence par comprendre la demande et les raisons du client, puis il explicite le probleme : par exemple, une image qui caricature un groupe ou une affirmation ecologique non justifiee. Il propose ensuite une alternative qui satisfait l'objectif communicationnel sans le meme risque, en montrant des exemples concrets. Il s'appuie sur des arguments verifiables : droit, reception probable, sensibilite de la cible, impact pour la marque. Si le client maintient sa position, il peut formaliser son refus par ecrit en restant courtois et en rappelant ses obligations deontologiques. Il documente l'echange dans le dossier de projet. Cette posture protege le designer tout en laissant la porte ouverte a une solution plus juste.",
    "On attend comprehension, proposition d'alternative, arguments et refus courtois documente."),
 QT("Pourquoi l'accessibilite est-elle une exigence ethique et pas seulement une norme technique ?",
    "Une norme technique definit des seuils mesurables : contraste, taille de police, navigation au clavier. Mais derriere ces seuils se trouve une question morale : qui peut acceder au message et qui en est exclu ? Une interface illisible pour une personne malvoyante ou un espace inaccessible a une personne a mobilite reduite produit une exclusion reelle. Traiter l'accessibilite comme une simple case a cocher revient a accepter cette exclusion. La consideration des usagers les plus vulnerables ameliore d'ailleurs le projet pour tous, comme les trottoirs abaisses ou les sous-titres. Pour le designer, l'enjeu est de rendre visible cette dimension dans le brief et de la defendre tout au long du projet, y compris face a des arbitrages de cout.",
    "On attend le passage du seuil technique a la question d'inclusion et la defense dans le projet.")],
C("L'ethique depasse la loi : respect des personnes, des sources et de l'environnement, transparence et accessibilite guident la conduite professionnelle.",
  "Ethique = bien agir · Deontologie = regles de la profession",
  "dignite · stereotype · conflit d'interets · greenwashing · secret",
  "Ethique~Justice au-dela de la loi~Deontologie~Regles professionnelles~Dignite~Respect des personnes~Stereotype~Representation fige",
  "Repérer les enjeux ethiques du brief|Verifier les representations et les sources|Evaluer les impacts sociaux et environnementaux|Signaler conflits et limites|Documenter les decisions",
  "Croire que la legalite suffit|Ignorer les stereotypes|Masquer un conflit d'interets|Promettre un impact ecologique non prouve",
  "Greenwashing~Annonce ecologique non fondee~Accessibilite~Inclusion et norme~Conflit d'interets~Interets concurrents~Secret~Information confidentielle~Refus~Posture professionnelle",
  "Ethique~Reflexion morale~Deontologie~Regles ecrites",
  "Legalite~Ce que permet la loi~Ethique~Ce qui est juste"))

# ============================================================ DP04
add("DP04", "Travail en equipe, gestion de projet et relation client", "Environnement professionnel et déontologie", T,
S("Un projet de design se conduit rarement seul."
  "|L'equipe associe designers, techniciens, commerciaux et specialistes divers."
  "|Chaque membre a un role et des responsabilites definies."
  "|La communication interne reguliere evite les malentendus."
  "|Les outils collaboratifs partagent fichiers, versions et commentaires."
  "|La gestion de versions evite d'ecraser le travail d'un collegue."
  "|Le planning repartit les taches selon les dependances entre elles."
  "|Les reunions doivent avoir un ordre du jour et un compte rendu."
  "|La relation client repose sur l'ecoute, la reformulation et la transparence."
  "|Les validations intermediaires securisent la livraison finale."
  "|Un desaccord se traite par l'argument et la recherche d'une solution commune."
  "|La qualite finale depend de la qualite de la collaboration."),
[QC("Pourquoi definir les roles des membres d'une equipe ?", "Pour limiter la creativite~Pour clarifier les responsabilites~Pour reduire le nombre de reunions~Pour eviter les validations", 1,
     "Des roles clairs evitent les doublons et les oublis."),
 QC("Quel risque evite la gestion de versions ?", "La perte de fichiers~L'ecrasement du travail d'un collegue~Le retard d'impression~Le changement de police", 1,
     "Nommer et dater les versions empeche d'ecraser une modification recente."),
 QC("Quel document accompagne une reunion efficace ?", "Un devis~Un ordre du jour et un compte rendu~Une facture~Une licence", 1,
     "Ils cadrent l'ordre du jour et gardent la trace des decisions."),
 QC("Quelle attitude caracterise une bonne relation client ?", "Imposer sa solution~Ecouter et reformuler le besoin~Eviter les questions~Promettre sans verifier", 1,
     "L'ecoute et la reformulation securisent la comprehension mutuelle."),
 QC("A quoi servent les validations intermediaires ?", "A rallonger le projet~A securiser la livraison finale~A supprimer le brief~A remplacer les tests", 1,
     "Elles permettent de corriger la direction avant la livraison."),
 QC("Comment traiter un desaccord en equipe ?", "Par l'autorite seule~Par l'argument et la recherche d'une solution commune~En ignorant le collegue~En arretant le projet", 1,
     "La discussion argumentee permet de construire une decision partagee."),
 QC("Quel outil facilite le travail collaboratif ?", "Un dossier partage avec versions et commentaires~Une cle USB unique~Un fichier sans nom~Un e-mail sans piece jointe", 0,
     "Les plateformes collaboratives centralisent fichiers, versions et retours."),
 QT("Comment organiser le travail d'une equipe de trois designers sur un projet d'identite visuelle ?",
    "On repartit les responsabilites selon les competences : recherche et references pour l'un, systeme graphique et typographie pour le deuxieme, declinaisons et controle des fichiers pour le troisieme. On defini un planning avec des jalons : brief, planches de recherche, premiere proposition, validation, declinaisons, livraison. On utilise un dossier partage avec une convention de nommage et des versions datees. Chaque jour, un point court fait le etat des avancees et des blocages; les decisions sont ecrites dans un compte rendu. Les arbitrages esthetiques se font en confrontant les propositions et en revenant au brief. Enfin, une relecture commune verifie la coherence de l'ensemble avant la presentation au client.",
    "On attend repartition des roles, jalons, versions, points reguliers et relecture finale."),
 QT("Comment gerer un client qui change d'avis a chaque reunion ?",
    "On commence par l'ecouter et par reformuler precisely sa nouvelle demande, pour distinguer un veritable changement de besoin d'une simple hesitation. On confronte ensuite cette demande au brief valide et au planning, en montrant les consequences sur le cout, les delais et la coherence de l'identite. On propose une ou deux options claires avec des avantages et des limites, puis on demande une decision ecrite. Les validations intermediaires servent justement a limiter ces revirements : chaque etape approuvee devient un point de reference. Si les changements se repetent, on les formalise dans un avenant au cahier des charges. La relation reste courtoise, mais le cadre protege l'equipe et la qualite du projet.",
    "On attend reformulation, retour au brief, options, decision ecrite et formalisation.")],
C("La qualite d'un projet depend de la qualite de la collaboration : roles clairs, versions maitrisees, communication reguliere et relation client transparente.",
  "Equipe + planning + versions + validations = projet maitrise",
  "roles · outils collaboratifs · ordre du jour · ecoute · avenant",
  "Equipe~Competences complementaires~Role~Responsabilite definie~Version~Etat date du fichier~Validation~Accord intermediaire",
  "Repartir les roles et les taches|Fixer jalons et planning|Mettre en place un dossier partage|Animer des points reguliers|Formaliser les decisions et les validations",
  "Travailler chacun de son cote|Ecraser un fichier sans verifier|Multiplier les reunions sans compte rendu|Promettre sans cadrer le changement",
  "Brief~Reference commune~Jalon~Etape de validation~Nommage~Convention de fichiers~Compte rendu~Trace des decisions~Avenant~Changement formalise",
  "Reunion~Echange structure~Discussion~Echange informel",
  "Client~Commanditaire~Equipe~Realisateurs"))

# ============================================================ AD01
add("AD01", "Design vocabulary : materials, shapes and processes", "Anglais du design", T,
S("Design English uses precise words for materials, shapes and actions."
  "|Materials : wood, metal, glass, plastic, fabric, leather, cardboard and ceramic."
  "|Shapes : round, square, rectangular, curved, flat, sharp and cylindrical."
  "|Processes : to cut, to fold, to mould, to assemble, to print and to finish."
  "|Properties : light, strong, flexible, transparent, recyclable and durable."
  "'Made of' gives the material ; 'made by' gives the maker or the process."
  "'Used for' describes a common function ; 'designed to' describes an intention."
  "|The passive voice is frequent in technical descriptions."
  "|Comparatives help compare options : lighter, stronger, more sustainable."
  "|Linkers such as 'although' and 'therefore' express contrast and result."
  "|Technical drawings use labels : view, section, scale, dimension and detail."
  "|A technical description prefers short, clear sentences."
  "|A glossary helps keep the same word for the same concept."
  "|A precise vocabulary avoids misunderstandings with an international client."),
[QC("Which phrase gives the material of an object ?", "Made by~Made of~Used for~Designed to", 1,
     "'Made of' is followed by the material: made of wood, made of metal."),
 QC("Which word describes a surface that lets light pass ?", "Opaque~Transparent~Flexible~Durable", 1,
     "Transparent means that light passes through the material."),
 QC("Which verb means 'donner une forme en pressant dans un moule' ?", "To cut~To fold~To mould~To print", 2,
     "To mould means to shape a material in a mould."),
 QC("Which sentence uses the passive voice ?", "It folds easily~It is made of aluminium~It has curved edges~It is very light", 1,
     "'It is made of' is a passive structure."),
 QC("Which linker introduces a contrast ?", "Therefore~Although~In addition~Moreover", 1,
     "Although introduces a contrast or a concession."),
 QC("Which word is a comparative ?", "Strong~Stronger~Strongest~Strength", 1,
     "Stronger is the comparative form of the adjective strong."),
 QC("Which label is used on a technical drawing ?", "Section~Grocery~Holiday~Weather", 0,
     "Section, view, scale and dimension are standard technical labels."),
 QT("Describe a lamp in English using material, shape, property and function.",
    "This lamp is made of brushed metal and frosted glass. It has a cylindrical base and a curved shade. The metal is strong and durable, while the glass is translucent and softens the light. It is designed to give a warm light for reading, and it is used for small desks. Although it is heavier than a plastic lamp, it is more stable and more sustainable because the materials can be recycled.",
    "The answer should include made of, a shape, a property, designed to and a linker."),
 QT("Explain the difference between 'made of', 'made by' and 'used for'.",
    "'Made of' answers the question 'What is it?' and introduces the material: the chair is made of wood. 'Made by' answers 'Who or what produced it?' and introduces the maker or the process: the chair is made by a local workshop. 'Used for' answers 'What is its common function?' and is followed by a noun or a verb in -ing: it is used for reading or for storing books. These three structures give different kinds of information, and a good product description combines them without confusing them.",
    "The expected answer separates material, producer/process and function with examples.")],
C("English design vocabulary separates material, shape, property, process and function: precise words prevent misunderstandings.",
  "Made of + material · Made by + maker · Used for + function",
  "passive voice · comparatives · although / therefore · technical labels",
  "Material~Wood metal glass~Shape~Round curved flat~Property~Light strong recyclable",
  "Name the object|Give the material with made of|Describe shape and properties|Explain function with designed to|Add comparison or reservation",
  "Translate word for word from French|Confuse made of and made by|Forget the passive form|Use vague adjectives",
  "Lamp~Brushed metal~Base~Cylindrical~Glass~Frosted and translucent~Stability~Stronger and more sustainable~Labels~View and section",
  "Made of~Material~Made by~Producer or process",
  "Although~Contrast~Therefore~Result"))

# ============================================================ AD02
add("AD02", "Writing a design brief and a portfolio in English", "Anglais du design", T,
S("A design brief in English follows a clear and predictable structure."
  "|It starts with the context and the name of the client."
  "|The aim states what the project should achieve."
  "|The target audience describes who will use the product."
  "|Requirements list what the solution must do."
  "|Constraints describe the limits : budget, time, materials and regulations."
  "|Deliverables name the expected outputs : sketches, mock-ups and final files."
  "|Short sentences and bullet points improve readability."
  "|A portfolio presents projects with images, a short text and the role of the designer."
  "|Each portfolio entry explains the problem, the process and the result."
  "|Action verbs such as designed, tested and improved show personal involvement."
  "|Proofreading and consistent vocabulary give a professional impression."),
[QC("Which section states what the project should achieve ?", "The context~The aim~The budget~The deliverables", 1,
     "The aim gives the objective of the project."),
 QC("What does 'target audience' mean ?", "The client's name~The people who will use the product~The designer's team~The printing company", 1,
     "The target audience is the group of intended users."),
 QC("Which of these is a constraint ?", "A sketch~A budget limit~A photograph~A title", 1,
     "Budget, time and materials are typical constraints."),
 QC("What are deliverables ?", "The tools used~The expected outputs of the project~The client's employees~The sources of inspiration", 1,
     "Deliverables are what the designer must hand in."),
 QC("Which verb shows personal involvement in a portfolio ?", "To be~To design~To seem~To have", 1,
     "Action verbs such as designed or tested show what the designer did."),
 QC("What improves the readability of a brief ?", "Long paragraphs~Short sentences and bullet points~Many colours~Complex words", 1,
     "Short sentences and bullet points make the document easier to scan."),
 QC("What should a portfolio entry explain ?", "Only the final price~The problem, the process and the result~Only the client's name~Only the tools", 1,
     "It should show the situation, the work done and what was obtained."),
 QT("Write a short design brief in English for a reusable water bottle.",
    "Client: City Sports Club. Context: members need a light bottle for training. Aim: design a reusable bottle that is easy to carry and simple to clean. Target audience: young adults aged 18 to 30. Requirements: capacity of 500 ml, no plastic waste, one-hand opening. Constraints: budget of 15 euros per unit, production of 500 pieces, recycled stainless steel. Deliverables: three sketches, one 3D model, one prototype and a short report. Deadline: six weeks.",
    "The answer should include context, aim, audience, requirements, constraints and deliverables."),
 QT("How should you present a project in a portfolio to show your personal role?",
    "Start with the name of the project and one image that gives the main idea. Then write a short paragraph with the context and the aim. Use action verbs in the first person or in the passive with clarity: 'I analysed the brief', 'I tested three options', 'the final shape was selected after user feedback'. Add one or two process images to show the research and the iterations. Finish with the result and what you learned. Keep the same structure for every project so that the reader can compare them easily. Proofread carefully: spelling mistakes reduce the professional impression, even when the design work is strong.",
    "The expected answer mentions structure, action verbs, process images and proofreading.")],
C("A brief and a portfolio in English rely on a predictable structure and precise vocabulary: context, aim, audience, constraints and deliverables.",
  "Brief = context + aim + audience + requirements + constraints + deliverables",
  "bullet points · action verbs · portfolio entry · proofreading",
  "Aim~Objective of the project~Audience~Intended users~Requirement~What it must do~Constraint~Limit",
  "Write the context and the client|State aim and audience|List requirements and constraints|Name the deliverables|Proofread and keep a consistent structure",
  "Forget the target audience|Mix requirements and constraints|Use only passive sentences|Send an unchecked text",
  "Aim~Reusable bottle~Audience~Young adults~Constraint~Budget and material~Deliverable~Three sketches~Verb~I designed and tested",
  "Requirement~Must be satisfied~Constraint~Limits the solution",
  "Brief~Before the project~Portfolio~After the project"))

# ============================================================ AD03
add("AD03", "Presenting and defending a design project in English", "Anglais du design", TER,
S("A design presentation in English needs a clear structure and simple sentences."
  "|Open with the aim of the project and the name of the client."
  "|Signposting expressions guide the audience through the talk."
  "|Use firstly, then, after that and finally to mark the stages."
  "|Present the research before the final solution."
  "|Explain the choices with because and in order to."
  "|Mention the constraints and how the solution answers them."
  "|Show prototypes and explain what each test revealed."
  "|Use however to introduce a limitation honestly."
  "|Invite questions with 'Do you have any questions?' or 'What do you think?'."
  "|Answer a question by listening first, then answering precisely."
  "|Practise pronunciation and timing before the real presentation."),
[QC("How should a presentation open ?", "With a joke only~With the aim and the client~With the conclusion~With a long biography", 1,
     "Stating the aim and the client gives the audience an immediate frame."),
 QC("Which word is a signposting expression ?", "Firstly~Wooden~Curved~Durable", 0,
     "Firstly, then and finally mark the stages of the talk."),
 QC("Which linker introduces a limitation ?", "Because~However~In order to~Also", 1,
     "However introduces a contrast or an honest limitation."),
 QC("Which sentence explains a purpose ?", "It is made of wood~It is designed in order to reduce waste~It has a round shape~It is very light", 1,
     "In order to + verb expresses the purpose of a choice."),
 QC("When should you show prototypes ?", "Only at the end~During the presentation, with the test results~Never~Instead of the brief", 1,
     "Prototypes and their results support the explanation of choices."),
 QC("How to answer a question from the audience ?", "Interrupt immediately~Listen first, then answer precisely~Ignore it~Read the notes aloud", 1,
     "Listening first avoids answering a different question."),
 QC("Why practise timing ?", "To speak as fast as possible~To fit the allotted time and keep the structure~To avoid using images~To skip the conclusion", 1,
     "Rehearsal ensures that the essential points are presented within the time."),
 QT("Write the opening and the signposting of a short design presentation.",
    "Good morning. My name is Leo and I am going to present a portable lamp for students. The client is a company that wants a light made of recycled materials. My aim today is to show how the brief led to the final shape. Firstly, I will present the context and the constraints. Then I will show two prototypes and explain the tests. After that, I will compare the options and justify the chosen solution. Finally, I will mention the limitations and invite your questions.",
    "The answer should include the aim, the client and at least three signposting expressions."),
 QT("How to defend a design choice in English when a limitation is mentioned ?",
    "Acknowledge the limitation first with a calm phrase such as 'That is a fair point'. Then explain the context: 'We chose this material in order to reduce weight, although it is less resistant than metal.' Give evidence from the process, for example a test result or a comparison between two prototypes. If you agree with the criticism, say what you would improve with more time: 'With a larger budget, I would test a stronger coating.' Finish by linking back to the aim of the project. Keep sentences short, look at the person who asked the question and avoid reading your notes. This structure shows that you can evaluate your work critically rather than simply defend it.",
    "The expected answer uses however or although, evidence, a possible improvement and eye contact.")],
C("Presenting in English means structuring the talk, justifying choices and treating questions as a dialogue.",
  "Aim → research → prototypes → choice → limitations → questions",
  "signposting · because / in order to · however · timing",
  "Aim~Purpose of the talk~Signposting~Firstly then finally~Prototype~Support of a choice~However~Honest limitation",
  "Open with aim and client|Announce the plan with signposting|Present research and prototypes|Justify with because and in order to|Invite and answer questions",
  "Read a full script aloud|Hide the limitations|Skip the rehearsal|Answer before listening",
  "Firstly~First stage~Then~Next stage~However~Limitation~In order to~Purpose~Questions~Dialogue with the audience",
  "Because~Cause~In order to~Purpose",
  "Presentation~Public speaking~Brief~Written document"))

valider_et_ecrire(F, "std2a-mat-part-C.json")
