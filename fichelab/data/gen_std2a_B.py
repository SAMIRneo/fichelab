# -*- coding: utf-8 -*-
"""Generateur std2a-mat-part-B.json — lot B : design et arts appliques (20 fiches).

Histoire de l'art et du design (6), Theorie du design (5),
Creation et composition (5), Typographie et couleur (4).
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

# ============================================================ DA01
add("DA01", "Histoire de l'art : de la Renaissance au classicisme", "Histoire de l'art et du design", T,
S("La Renaissance, aux XVe et XVIe siecles, redecouvre l'antiquite et place l'etre humain au centre de la representation."
  "|La perspective lineaire, theorisee par Alberti, organise l'espace autour d'un point de fuite unique."
  "|Le dessin devient un outil d'analyse et de projet chez Leonardo da Vinci, qui mele art et technique."
  "|Les ateliers se professionalisent et le statut de l'artiste passe de l'artisan au createur reconnu."
  "|L'imprimerie diffuse les images, les traites d'architecture et les modeles a travers l'Europe."
  "|Le manierisme joue sur la deformation, l'ele-gance artificielle et la tension des formes."
  "|Le XVIIe siecle classique valorise l'ordre, la symmetrie, la proportion et la raison."
  "|Le classicisme francais s'incarne a Versailles, avec l'architecture et le jardin a la francaise."
  "|Le baroque, contemporain du classicisme, privilegie le mouvement, le clair-obscur et la mise en scene."
  "|Le principe de mimesis, ou imitation du reel, reste central mais s'enrichit d'invention."
  "|Les academies codifient les regles du dessin, de la couleur et de la composition."
  "|Ces reperes permettent au designer de lire une image et de situer ses propres references."),
[QC("A quelle periode se situe la Renaissance ?", "XIIe-XIIIe siecles~XVe-XVIe siecles~XVIIIe siecle~XXe siecle", 1,
     "La Renaissance couvre les XVe et XVIe siecles en Europe."),
 QC("Quel theoricien a codifie la perspective lineaire ?", "Vitruve~Alberti~Vasari~Benjamin", 1,
     "Leon Battista Alberti expose les regles de la perspective dans son traite de la peinture."),
 QC("Quel element structure la perspective centrale ?", "Le point de fuite~La couleur complementaire~Le rythme~La symmetry", 0,
     "Toutes les fuyantes convergent vers le point de fuite situe sur la ligne d'horizon."),
 QC("Quelle valeur est au coeur du classicisme ?", "Le desordre~L'ordre et la proportion~Le hasard~La deformation", 1,
     "Le classicisme recherche l'ordre, la symmetrie et les proportions reglees."),
 QC("Quel courant privilegie le mouvement et le clair-obscur ?", "Le classicisme~Le baroque~Le minimalisme~Le cubisme", 1,
     "Le baroque mise sur le dynamisme, la lumiere et la mise en scene."),
 QC("Que designe le concept de mimesis ?", "L'imitation du reel~La creation ex nihilo~La reaction du public~La copie mecanique", 0,
     "La mimesis est le principe d'imitation de la nature et du reel."),
 QC("Quel role a joue l'imprimerie pendant la Renaissance ?", "Supprimer le dessin~Diffuser images et traites~Interdire la perspective~Remplacer les academies", 1,
     "L'imprimerie a largement diffuse les modeles visuels et les traites techniques."),
 QT("Comparer les principes du classicisme et du baroque dans la maniere de composer une image.",
    "Le classicisme construit une image equilibree autour d'un axe : la symmetrie, la clairete des contours, la proportion des parties et la maitrise de la lumiere traduisent un ideal de raison et d'ordre. Le baroque, sans rejeter ses acquis, prefere la diagonale, le mouvement des formes, les contrastes de lumiere et l'implication du spectateur : la composition deborde vers l'exterieur du cadre. Dans une affiche actuelle, ces deux attitudes subsistent : une mise en page centre et hieratique correspond plutot au classicisme, tandis qu'une diagonale dynamique et un fort clair-obscur relevent d'une culture baroque.",
    "On attend une opposition nette (ordre/symmetrie contre mouvement/clair-obscur) et un exemple de transposition."),
 QT("Expliquer en quoi la perspective a transforme le dessin de projet.",
    "Avant la perspective codifiee, les representations ne rendaient pas compte de la profondeur de facon coherente. La perspective lineaire permet de construire un espace mesurable : les fuyantes convergent vers un point de fuite et les dimensions diminuent selon une loi. Le dessin devient alors un outil de conception et de communication : on peut representer un edifice ou un meuble avant de le fabriquer, verifier ses proportions et le faire comprendre a un commanditaire. C'est cette fonction de projet, plus que la seule imitation, qui fait de la perspective un fondement du dessin technique et du design.",
    "La reponse doit montrer le passage d'une image imitative a un outil de conception et de justification.")],
C("Renaissance et classicisme ont fait du dessin un langage rigoureux : perspective, proportion et regles academiques fondent encore la lecture d'une image.",
  "Perspective : fuyantes + point de fuite + ligne d'horizon",
  "Renaissance : humanisme et dessin-projet · Classique : ordre · Baroque : mouvement",
  "Renaissance~Retour a l'antique~Perspective~Point de fuite~Classicisme~Ordre et proportion~Baroque~Mouvement et lumiere",
  "Situer l'oeuvre dans son siecle|Repérer les regles de composition|Observer le traitement de l'espace|Identifier les references antiques|Relier aux pratiques du design",
  "Reduire une periode a un seul style|Confondre classicisme et baroque|Ignorer le contexte des academies|Copier une perspective sans comprendre la construction",
  "Alberti~Traite de perspective~Leonardo~Dessin et technique~Versailles~Classicisme~Caravage~Clair-obscur baroque~Academie~Codification des regles",
  "Classicisme~Axe et symmetrie~Baroque~Diagonale et mouvement",
  "Mimesis~Imitation du reel~Invention~Transformation du reel"))

# ============================================================ DA02
add("DA02", "Histoire de l'art : modernite et avant-gardes", "Histoire de l'art et du design", T,
S("Au XIXe siecle, l'academisme impose les regles tandis que le romantisme exprime le sentiment et l'imagination."
  "|Le realisme peint la societe contemporaine et le quotidien plutot que les themes heroiques."
  "|L'impressionnisme, dans les annees 1870, etudie la lumiere et la couleur en plein air."
  "|Cezanne construit les volumes par plans et prepare la rupture cubiste."
  "|Le fauvisme libere la couleur pure, independante de la description realiste."
  "|Le cubisme, avec Picasso et Braque, represente plusieurs points de vue sur un meme objet."
  "|Le futurisme celebre la vitesse, le mouvement mecanique et la violence de la modernite."
  "|Dada conteste l'ordre etabli par le hasard, le collage et le ready-made de Duchamp."
  "|Le surrealisme explore l'inconscient, le Reve et les associations inattendues d'images."
  "|L'abstraction, chez Kandinsky ou Mondrian, libere la forme et la couleur de la representation."
  "|Ces avant-gardes nourrissent directement le design : Bauhaus, constructivisme et De Stijl."
  "|Elles remettent en cause le statut de l'oeuvre, de l'auteur et du public."),
[QC("Quel mouvement etudie la lumiere en plein air ?", "Le realisme~L'impressionnisme~Le surrealisme~Le cubisme", 1,
     "Les impressionnistes peignent en exterieur pour capter les variations de la lumiere."),
 QC("Quel artiste est associe au ready-made ?", "Cezanne~Marcel Duchamp~Mondrian~Monet", 1,
     "Duchamp presente des objets du quotidien comme des oeuvres, par exemple la Fontaine."),
 QC("Quelle caracteristique definit le cubisme ?", "Un seul point de vue~Plusieurs points de vue sur un objet~La couleur pure~Le Reve", 1,
     "Le cubisme deconstruit l'objet et montre simultanement differentes faces."),
 QC("Quel courant explore l'inconscient ?", "Le futurisme~Le surrealisme~L'impressionnisme~Le classicisme", 1,
     "Le surrealisme s'inspire des reves et de la psychanalyse."),
 QC("Quel mouvement celebre la vitesse et la machine ?", "Dada~Le futurisme~Le fauvisme~Le realisme", 1,
     "Le futurisme italien fait de la vitesse et de la mecanisation un sujet central."),
 QC("Qui a fonde le mouvement De Stijl avec Mondrian ?", "Gropius~Theo van Doesburg~Duchamp~Le Corbusier", 1,
     "Theo van Doesburg a fonde De Stijl avec Mondrian, promoteur d'une abstraction geometrique."),
 QC("Quel effet les avant-gardes ont-elles eu sur le design ?", "Elles l'ont ignore~Elles ont nourri le Bauhaus et le constructivisme~Elles ont interdit la couleur~Elles ont supprime les ateliers", 1,
     "Les recherches formelles des avant-gardes ont directement influence les ecoles de design."),
 QT("Expliquer la rupture du cubisme par rapport a la perspective classique.",
    "La perspective classique organise l'image autour d'un point de vue unique, comme si le spectateur se tenait a une place fixe. Le cubisme refuse cette convention : il decompose l'objet et montre en meme temps plusieurs faces, le dessus et le cote, comme si l'on tournait autour. L'espace devient peu profond, les plans se chevauchent et la ligne d'horizon disparait souvent. Cette rupture n'est pas seulement stylistique : elle change la maniere de penser la representation, en affirmant que l'objet est plus que l'apparence qu'il offre a un regard unique. Le design graphique et l'Architecture ont recueilli cet heritage dans la mise en page et le dessin technique.",
    "On attend l'opposition point de vue unique / points de vue multiples et la consequence sur l'espace."),
 QT("Comment un designer peut-il s'inspirer de Dada sans simplement copier ses formes ?",
    "Plutot que de reproduire une esthetique de collage, le designer peut retenir la methode : detourner un objet, introduire du hasard, associer des elements sans rapport et contester les habitudes de lecture. Il peut par exemple remplacer une photo de produit par un assemblage insolite, laisser une trace de manipulation dans une mise en page ou faire dialoguer deux typographies contradictoires. L'important est de garder une intention lisible : le detournement doit faire avancer le message, pas seulement surprendre. Il faut aussi verifier les droits des elements empruntes et la maniere dont le public peut recevoir le geste.",
    "La reponse doit passer de la forme a la methode, avec une intention et une prudence juridique.")],
C("Les avant-gardes ont rompu avec la representation unique : couleur, forme, hasard et abstraction ont renouvele le langage visuel.",
  "Impressionnisme : lumiere · Cubisme : multi-vues · Dada : hasard",
  "abstraction · ready-made · futurisme · surrealisme",
  "Impressionnisme~Lumiere et couleur~Cubisme~Plusieurs points de vue~Dada~Hasard et detournement~Surrealisme~Reve et inconscient",
  "Situer le mouvement par rapport a ses predecesseurs|Identifier la rupture formelle|Nommer les artistes representatifs|Relier aux arts appliques|Analyser la reception actuelle",
  "Melanger les mouvements|Reduire Dada au hasard seul|Ignorer le contexte historique|Confondre abstraction et simplification",
  "Monet~Lumiere impressionniste~Picasso~Cubisme~Duchamp~Ready-made~Kandinsky~Abstraction~Mondrian~Geometrie De Stijl",
  "Classique~Point de vue unique~Cubiste~Points de vue multiples",
  "Fauvisme~Couleur libre~Impressionnisme~Couleur et lumiere"))

# ============================================================ DA03
add("DA03", "Histoire du design : Arts and Crafts et Bauhaus", "Histoire de l'art et du design", T,
S("La reaction a l'industrialisation du XIXe siecle critique la mauvaise qualite des objets de serie."
  "|Ruskin et Morris defendent le retour au geste, au materiau et a la qualite artisanale."
  "|Le mouvement Arts and Crafts valorise le travail de l'atelier et le respect des matieres."
  "|L'Art Nouveau, avec Guimard, invente une ligne courbe inspiree de la nature."
  "|Le Deutscher Werkbund cherche a reunir qualite artisanale et production industrielle."
  "|Le Bauhaus est fonde en 1919 a Weimar par Walter Gropius."
  "|Son programme vise l'unite de l'art, de l'artisanat et de la technique."
  "|Le cours preliminaire d'Itten, Klee et Kandinsky explore la couleur, la forme et le movement."
  "|Les ateliers du Bauhaus travaillent le metal, le bois, le textile, la ceramics et la typographie."
  "|Marcel Breuer cree la chaise Wassily en tube d'acier, symbole de la modernite."
  "|Marianne Brandt dessine des objets metaliques fonctionnels et epures."
  "|Ferme en 1933, le Bauhaus disperse ses acteurs et influence durablement l'enseignement du design."),
[QC("Qui a fonde le Bauhaus en 1919 ?", "William Morris~Walter Gropius~Hector Guimard~Dieter Rams", 1,
     "Walter Gropius fonde le Bauhaus a Weimar en 1919."),
 QC("Quel mouvement defendait le retour au geste artisanal face a l'industrie ?", "Le Bauhaus~Arts and Crafts~Le futurisme~De Stijl", 1,
     "Arts and Crafts, avec Ruskin et Morris, valorise le travail manuel et la qualite."),
 QC("Quel materiau caracterise la chaise Wassily de Breuer ?", "Le bois massif~Le tube d'acier~Le verre~Le carton", 1,
     "La chaise Wassily utilise un tube d'acier plie, novateur pour l'epoque."),
 QC("Quel etait l'objectif principal du Bauhaus ?", "Copier l'art ancien~Reunir art, artisanat et technique~Supprimer les ateliers~Produire uniquement du luxe", 1,
     "Le Bauhaus voulait reunifier les disciplines autour de la production et de l'enseignement."),
 QC("Qui a anime le cours preliminaire du Bauhaus ?", "Itten, Klee et Kandinsky~Rams, Bill et Aicher~Morris et Ruskin~Duchamp et Picabia", 0,
     "Itten, Klee et Kandinsky ont marque l'enseignement fondamental du Bauhaus."),
 QC("Quelle designer du Bauhaus a travaille le metal ?", "Marianne Brandt~Coco Chanel~Zaha Hadid~Paula Scher", 0,
     "Marianne Brandt a realise des luminaires et objets en metal dans l'atelier du Bauhaus."),
 QC("Quelle consequence a eu la fermeture du Bauhaus en 1933 ?", "La fin du design moderne~La dispersion de ses acteurs et de ses idees~Le retour a l'academisme~L'interdiction de la couleur", 1,
     "Les enseignants et eleves ont diffuse le modele Bauhaus dans plusieurs pays."),
 QT("Expliquer pourquoi Arts and Crafts et Bauhaus sont deux reponses differentes a l'industrialisation.",
    "Arts and Crafts rejette la production industrielle jugée destructrice du geste et de la qualite : elle revient a l'atelier, au materiau noble et a l'objet unique ou en petite serie. Le Bauhaus, quelques decennies plus tard, accepte la machine et cherche a la maitriser : il veut former des createurs capables de dessiner pour l'industrie tout en gardant une exigence artistique. Les deux mouvements partagent le refus de la mediocrité, mais l'un se replie sur l'artisanat et l'autre invente une culture de production. Cette tension entre geste et industrie traverse encore aujourd'hui les metiers du design et des metiers d'art.",
    "On attend l'opposition rejet / adoption de la machine et une conclusion sur l'heritage contemporain."),
 QT("Comment le cours preliminaire du Bauhaus a-t-il change l'enseignement du design ?",
    "Le cours preliminaire imposait a tous les etudiants une exploration commune de la couleur, de la forme, de la matiere et du rythme avant la specialisation. Il ne s'agissait pas d'apprendre un style, mais de developper une sensibilite et un vocabulaire partages. Klee et Kandinsky analysaient les elements visuels comme une grammaire, tandis qu'Itten travaillait les contrasts et la perception. Cette idée d'un socle commun precedeant l'atelier a profondement transforme les ecoles d'art : on enseigne encore aujourd'hui des principes generaux plutot que la seule imitation de modeles. Pour un eleve de STD2A, elle justifie l'etude simultanee de la theorie, de la couleur et de la pratique.",
    "La reponse doit decrire le socle commun, son contenu et sa consequence pedagogique.")],
C("Arts and Crafts defend le geste contre la machine ; le Bauhaus fait de la machine un outil de creation et invente l'enseignement moderne du design.",
  "Bauhaus 1919 = art + artisanat + technique",
  "Arts and Crafts · Werkbund · ateliers · cours preliminaire · 1933",
  "Arts and Crafts~Retour au geste~Werkbund~Qualite et industrie~Bauhaus~Art et technique~Atelier~Lieu de production",
  "Situer le mouvement face a l'industrie|Identifier les acteurs et les dates|Analyser le programme pedagogique|Observer un objet representatif|Relier a l'enseignement actuel",
  "Confondre les deux mouvements|Ignorer le role des ateliers|Croire que le Bauhaus rejetait la machine|Oublier les femmes designers du Bauhaus",
  "1919~Fondation du Bauhaus~Weimar~Premier siege~Wassily~Tube d'acier~Brandt~Luminaire metal~1933~Fermeture et dispersion",
  "Arts and Crafts~Objet unique~Bauhaus~Prototype pour la serie",
  "Cours preliminaire~Socle commun~Specialisation~Atelier specialised"))

# ============================================================ DA04
add("DA04", "Histoire du design : Le Corbusier, Ulm et le style international", "Histoire de l'art et du design", TER,
S("Le Corbusier formule une architecture fonctionnaliste, resumee par la maison comme machine a habiter."
  "|Le Modulor propose un systeme de proportions base sur le corps humain."
  "|Ses meubles LC2 et LC4 associent acier, cuir et positions du corps."
  "|Les Congres internationaux d'architecture moderne diffusent ces principes en Europe."
  "|L'ecole de design d'Ulm est fondee en 1953 dans la continuite critique du Bauhaus."
  "|Max Bill puis Otl Aicher y developpent une methode de conception rigoureuse et systematique."
  "|Ulm travaille beaucoup sur la typographie, la signaletique et la grille."
  "|La firme Braun, avec Dieter Rams, applique une discipline de simplification extreme."
  "|Rams resume sa posture par la formule « moins, mais mieux »."
  "|Le style international, avec Mies van der Rohe, valorise la structure, le verre et l'epure."
  "|La chaise Barcelona illustre cette recherche de lignes pures et de confort."
  "|Des critiques, comme Robert Venturi, contesteront plus tard la rigueur du fonctionnalisme."),
[QC("Quel systeme de proportions a ete invente par Le Corbusier ?", "Le Modulor~La section d'or~Le module de Gropius~La grille suisse", 0,
     "Le Modulor est une echelle de proportions fondee sur les dimensions du corps humain."),
 QC("Quelle est la maxime de Dieter Rams ?", "Plus, c'est mieux~Moins, mais mieux~La forme suit le désir~Toujours de la couleur", 1,
     "Dieter Rams defense « weniger, aber besser », soit moins mais mieux."),
 QC("Quelle entreprise est associee a Dieter Rams ?", "Braun~Philips~Siemens~Ikea", 0,
     "Rams a travaille pour Braun, ou il a dessine de nombreux appareils."),
 QC("Qui a dirige l'ecole d'Ulm apres Max Bill ?", "Otl Aicher~Walter Gropius~Le Corbusier~Josef Albers", 0,
     "Otl Aicher a marque Ulm, notamment par son approche systematique de la communication visuelle."),
 QC("Quel principe est associe a Mies van der Rohe ?", "Less is more~Form follows fun~More is more~Art for art", 0,
     "Mies van der Rohe a popularise la formule « less is more »."),
 QC("Quel meuble de Mies van der Rohe illustre le style international ?", "La chaise Barcelona~La chaise Wassily~Le fauteuil LC4~La chaise Thunderbolt", 0,
     "La chaise Barcelona, en acier et cuir, est un embleme du style international."),
 QC("Quelle critique a ete adressee au fonctionnalisme ?", "Il etait trop colore~Il ignoreait la complexite et la signification~Il etait trop cher~Il interdisait le metal", 1,
     "Venturi et les postmodernes lui reprochent de simplifier la realite et le sens."),
 QT("Comparer l'apport du Bauhaus et celui de l'ecole d'Ulm au design moderne.",
    "Le Bauhaus a invente une posture : reunir art, artisanat et industrie, et former des creatuteurs polyvalents par un socle de perception et des ateliers. Son approche reste experimentale et optimiste. Ulm, apres 1953, radicalise cette heritage en y ajoutant une exigence de methode : analyse du besoin, systématisation, typographie rigoureuse et signaletique. Là ou le Bauhaus cherchait une unite des arts, Ulm cherche une rationalite de la communication et de l'objet. Braun et Rams en sont l'application industrielle. Les deux ecoles partagent la.refus du decor superficiel, mais Ulm est plus systematique et plus critique vis-a-vis de la simple forme.",
    "On attend la difference experimentale / methodologique et un exemple pour chaque ecole."),
 QT("Le principe « moins, mais mieux » peut-il etre applique a un projet de design graphique ?",
    "Oui, a condition de ne pas le confondre avec une simple suppression. Applique a une affiche ou a une interface, il invite a retirer tout ce qui ne sert ni la comprehension ni l'intention : moins de polices, moins de couleurs, moins de decorations. Mais il exige aussi « mieux » : une hierarchie plus claire, un contraste suffisant, une grille maitrisee et un contenu mieux ecrit. Le risque est de produire un minimalisme froid qui ignore le contexte culturel ou la sensibilite du public. Un bon projet simplifie la forme pour rendre le message plus fort, et non pour eviter de faire des choix.",
    "La reponse doit definir le principe, donner des applications concretes et en souligner le risque.")],
C("Le functionalisme de Le Corbusier, la rigueur d'Ulm et le minimalisme de Rams ont fonde une culture du projet ou la forme doit etre justifiee.",
  "Moins, mais mieux · Less is more · Modulor",
  "Le Corbusier · Ulm (1953) · Braun · Rams · Mies · Venturi",
  "Le Corbusier~Machine a habiter~Modulor~Proportions du corps~Ulm~Methode et systeme~Rams~Moins mais mieux",
  "Situer l'ecole ou le designer|Identifier le principe defendu|Analyser un objet representatif|Comparer avec le Bauhaus|Formuler une critique argumentee",
  "Confondre style international et style personnel|Reduire Rams a l'absence de couleur|Ignorer la critique postmoderne|Copier un meuble sans en comprendre la fonction",
  "LC2~Assise en acier et cuir~LC4~Chaise longue~Ulm~Signaletique~Braun~Appareils epures~Barcelona~Acier et cuir",
  "Bauhaus~Experimentation et atelier~Ulm~Methode et systématisation",
  "Fonctionnalisme~Forme justifiee~Postmodernisme~Complexite et sens"))

# ============================================================ DA05
add("DA05", "Histoire du design graphique : affiche et ecole suisse", "Histoire de l'art et du design", T,
S("L'affiche moderne nait au XIXe siecle avec la lithographie et la publicite de spectacle."
  "|Cheret et Toulouse-Lautrec inventent une image publicitaire forte, coloree et synthétique."
  "|L'Art Nouveau affirme une ligne decorative et des lettrages integres a l'image."
  "|Le constructivisme russe, avec El Lissitzky et Rodtchenko, met la typographie au service de l'ideologie et de la dynamique."
  "|Le De Stijl reduit la composition a des lignes, des plans et des couleurs primaires."
  "|Le Bauhaus, avec Herbert Bayer, definit un alphabet universel en minuscules."
  "|L'ecole suisse, apres 1945, systematise la grille, l'asymetrie et la photographie."
  "|Josef Muller-Brockmann a theorise la grille comme outil de clairete et d'objectivite."
  "|Armin Hofmann travaille le contraste, le regard et la tension entre les elements."
  "|La typographie sans empattement, comme Helvetica, devient un standard international."
  "|Le photomontage et le collage enrichissent les moyens d'expression graphique."
  "|Ces principes structurent encore le design editorial, le web et l'identite visuelle."),
[QC("Quelle technique a permis l'essor de l'affiche au XIXe siecle ?", "La gravure sur bois~La lithographie~La photographie numerique~L'offset numerique", 1,
     "La lithographie permet la reproduction en couleur de grands formats d'affiches."),
 QC("Quel artiste est associe au constructivisme russe ?", "Toulouse-Lautrec~El Lissitzky~Muller-Brockmann~Cheret", 1,
     "El Lissitzky a produit des affiches constructivistes utilisant la diagonale et le photomontage."),
 QC("Quel principe caracterise l'ecole suisse ?", "La grille et l'asymetrie~Le decor floral~Le Baronat~Le hasard total", 0,
     "L'ecole suisse privilegie une grille rigoureuse et une composition asymetrique lisible."),
 QC("Quel typographe a cree un alphabet universel au Bauhaus ?", "Herbert Bayer~Josef Muller-Brockmann~Armin Hofmann~Eric Gill", 0,
     "Herbert Bayer a propose un alphabet reducteur en minuscules pour le Bauhaus."),
 QC("Quelle police est devenue un standard international ?", "Garamond~Helvetica~Didot~Comic Sans", 1,
     "Helvetica, sans empattement, est un embleme du style suisse et international."),
 QC("Quel est le role de la grille selon Muller-Brockmann ?", "Decorer la page~Organiser l'information et rendre le message lisible~Remplacer le texte~Cacher les erreurs", 1,
     "La grille est un outil d'organisation rationnelle au service de la communication."),
 QC("Quel apport d' Armin Hofmann a marque l'ecole suisse ?", "Le seul usage de la couleur~Le travail du contraste et du regard~Le refus de la photographie~La suppression de la grille", 1,
     "Hofmann a explore le contraste, la tension formelle et la direction du regard."),
 QT("Expliquer pourquoi l'ecole suisse est souvent presentee comme un modele de design graphique moderne.",
    "Apres 1945, l'ecole suisse propose une methode reproductible : une grille rigoureuse, une typographie sans empattement, une photographie claire et une composition asymetrique. Cette approche refusait le decor pour rendre l'information immediatement lisible, ce qui repondait aux besoins d'une societe industrielle et internationale. Elle a aussi produit une doctrine pedagogique, avec des livres et des cours qui ont diffuse le modele dans le monde entier. Aujourd'hui, les interfaces numeriques et les identites visuelles utilisent encore ses principes de grille et de hierarchie, meme si on leur reproche parfois leur uniformite et leur manque de singularite culturelle.",
    "On attend les principes formels, la dimension pedagogique et une critique nuancee."),
 QT("Comment une affiche peut-elle employer le contraste pour guider le regard ?",
    "Le contraste peut jouer sur la taille, la valeur clair-sombre, la couleur, la graisse typographique ou la densite des elements. Un titre tres grave sur un fond clair attire d'abord l'oeil ; une image a fort contraste cree un second point d'appel. L'ecart entre ces elements etablit un chemin de lecture : on part du plus fort vers le plus discret. Une grille stable evite que cette tension devienne du desordre. Le designer doit aussi verifier le contraste a differentes distances et pour differentes perceptions visuelles, car un effet saisissant de pres peut devenir illisible en situation reelle d'affichage.",
    "La reponse doit citer plusieurs types de contraste, la hierarchie du regard et la verification en contexte.")],
C("L'affiche et l'ecole suisse ont fait de la grille, de la typographie et du contraste un systeme de communication lisible et transposable.",
  "Grille + asymetrie + sans-serif + photographie",
  "lithographie · constructivisme · Bauhaus · Helvetica · Muller-Brockmann",
  "Affiche~Message public~Grille~Organisation~Asymetrie~Equilibre dynamique~Sans-serif~Lisibilite",
  "Identifier le contexte de diffusion|Choisir une grille adaptee|Hierarchiser titre image et texte|Tester le contraste a distance|Verifier la lisibilité et les droits",
  "Confondre grille et simple decoupage|Utiliser trop de polices|Negliger le format d'affichage|Ignorer l'origine des images",
  "Cheret~Affiche de spectacle~Lissitzky~Constructivisme~Bayer~Alphabet universel~Helvetica~Standard suisse~Grille~Outil de clairete",
  "Grille~Organise l'information~Decor~Ajoute sans fonction",
  "Symmetrie~Equilibre statique~Asymetrie~Equilibre dynamique"))

# ============================================================ DA06
add("DA06", "Histoire du design de mode et des metiers d'art", "Histoire de l'art et du design", T,
S("La mode reflete les transformations sociales, economiques et culturelles de son epoque."
  "|La haute couture se structure au XIXe siecle avec Charles Frederick Worth a Paris."
  "|Paul Poiret libere le corps des corsets et invente une silhouette plus fluide."
  "|Coco Chanel impose le jersey, la simplicité et une allure active."
  "|Le prêt-a-porter se developpe apres 1945 et democratise la mode."
  "|Les annees 1960 voient surgir la minijupe, la mode spatiale et des matieres nouvelles."
  "|Le design de mode travaille la ligne, le volume, la matiere et le mouvement du corps."
  "|Les textiles innovants et les traitements de surface elargissent le champ des possibles."
  "|Les metiers d'art couvrent le verre, la ceramique, le bijou, le livre, le textile et le decor."
  "|Ils articulent savoir-faire artisanal, creation contemporaine et petite serie."
  "|La photographie de mode et le mannequinat construisent une image et un imaginaire."
  "|Les enjeux actuels portent sur la tracabilite, la durabilite et la mode circulaire."),
[QC("Qui a structure la haute couture parisienne au XIXe siecle ?", "Coco Chanel~Charles Frederick Worth~Paul Poiret~Yves Saint Laurent", 1,
     "Worth est considere comme le fondateur de la haute couture moderne."),
 QC("Quel createur a libere le corps du corset au debut du XXe siecle ?", "Poiret~Worth~Dior~Rams", 0,
     "Paul Poiret a impose des silhouettes fluides et abandonne le corset."),
 QC("Quelle matiere est associee a Coco Chanel ?", "La soie epaisse~Le jersey~Le cuir rigide~Le plastique", 1,
     "Chanel a utilise le jersey, etoffe souple et confortable, pour ses creations."),
 QC("Quel evenement a favorise le developpement du pret-a-porter ?", "La Premiere Guerre mondiale~L'apres 1945 et la production de serie~La Renaissance~Le Moyen Age", 1,
     "L'industrialisation et la consommation de masse apres 1945 ont developpe le pret-a-porter."),
 QC("Quel metier d'art travaille le verre ?", "Le relieur~Le verrier~Le bottier~Le graphiste", 1,
     "Le verrier facade, souffle ou taille le verre selon differentes techniques."),
 QC("Quel element n'est pas un composant du langage de la mode ?", "La ligne~Le volume~La matiere~La formule algebrique", 3,
     "La mode travaille la ligne, le volume, la matiere et le mouvement, pas l'equation."),
 QC("Quel enjeu contemporain concerne la mode ?", "La tracabilite et la durabilite~La disparition des tissus~L'interdiction des motifs~Le refus de toute image", 0,
     "La tracabilite, la durabilite et le recyclage sont des enjeux majeurs du secteur."),
 QT("Comment un createur de mode construit-il une silhouette et quels enjeux cela implique-t-il ?",
    "Il part d'un propos ou d'une inspiration, puis travaille la ligne generatrice, les volumes et les proportions par rapport au corps. Il choisit des matieres en fonction de leur tombe, de leur tenue et de leur confort, puis il realise des essayages et des modifications successives. La silhouette n'est donc pas une image plane : elle existe dans le mouvement et dans differentes morphologies. Les enjeux sont multiples : esthetique, technique, economique (cout de la matiere et de la main-d'oeuvre) et symbolique (image du corps vehiculee). Un createur responsable interroge aussi l'impact social et environnemental de ses choix.",
    "On attend la chaine inspiration, ligne, volume, matiere, essayage et les enjeux associes."),
 QT("Quelle difference existe-t-il entre un metier d'art et une production industrielle de mode ?",
    "Le metier d'art repose sur une maitrise technique approfondie et une production souvent unique ou en tres petite serie : le geste de l'artisan laisse une trace et chaque piece peut etre singuliere. La production industrielle de mode vise la repetition, la standardisation des tailles et la reduction des couts grace a la machine. Elle doit neanmoins integrer une phase de design pour que l'objet reste desir et utilisable. Les deux mondes ne s'excluent pas : de nombreux createurs collaborent avec des ateliers, et l'industrie s'inspire des savoir-faire d'art. La question est de savoir ou se situe la valeur : dans le geste, dans le dessin ou dans la diffusion.",
    "La comparaison doit porter sur la serie, le geste, le cout et les collaborations possibles.")],
C("La mode et les metiers d'art conjuguent corps, matiere et geste : le design y est a la fois forme, technique et image sociale.",
  "Silhouette = ligne + volume + matiere + mouvement",
  "haute couture · pret-a-porter · savoir-faire · tracabilite",
  "Haute couture~Piece sur mesure~Pret-a-porter~Production de serie~Metier d'art~Savoir-faire~Silhouette~Ligne et volume~Matiere~Tombe et tenue",
  "Situer la creation dans son epoque|Identifier la ligne et les volumes|Analyser la matiere et sa mise en oeuvre|Observer le rapport au corps|Interroger la production et son impact",
  "Confondre haute couture et pret-a-porter|Ignorer le confort et le mouvement|Reduire la mode a l'image|Oublier les savoir-faire artisanaux",
  "Worth~Haute couture~Poiret~Corps libere~Chanel~Jersey~Verrier~Travail du verre~Mode circulaire~Durabilite",
  "Metier d'art~Piece singuliere~Industrie~Serie et standardisation",
  "Haute couture~Sur mesure~Pret-a-porter~Tailles standard"))

# ============================================================ DT01
add("DT01", "Design et besoin : fonction, usage et signification", "Théorie du design", T,
S("Le designer part d'un besoin qu'il doit identifier avant de proposer une forme."
  "|Le besoin explicite est formule par le commanditaire ; le besoin latent n'est pas encore conscient."
  "|La fonction technique correspond a ce que l'objet doit accomplir."
  "|La fonction d'usage concerne la facon dont l'utilisateur manipule l'objet."
  "|La fonction symbolique ou sociale fait de l'objet un signe d'appartenance ou de statut."
  "|La formule « la forme suit la fonction » a marque le functionalisme, mais elle ne suffit pas toujours."
  "|L'affordance designe les possibilites d'action offertes par la forme de l'objet."
  "|Une contrainte peut etre technique, economique, reglementaire, culturelle ou environnementale."
  "|La valeur d'usage se distingue de la valeur d'echange ou de la valeur de marque."
  "|L'objet communique : sa forme, sa couleur et ses materiaux produisent du sens."
  "|Le contexte d'usage, le lieu et le public determines la pertinence d'une solution."
  "|Un projet de design est une reponse argumentee a un probleme, pas seulement une image attractive."),
[QC("Qu'appelle-t-on un besoin latent ?", "Un besoin formule par le client~Un besoin non encore conscient~Un besoin technique~Un besoin chiffre", 1,
     "Le besoin latent n'est pas explicite : le designer doit le reveler par l'observation."),
 QC("Que designe l'affordance d'un objet ?", "Son prix~Les actions que sa forme rend possibles~Sa couleur~Sa duree de vie", 1,
     "Le terme designe les possibilites d'action percues grace a la forme."),
 QC("Quelle fonction fait d'un objet un signe social ?", "La fonction technique~La fonction symbolique~La fonction d'usage~La fonction de production", 1,
     "La fonction symbolique porte une valeur d'identite, de statut ou d'appartenance."),
 QC("Quel auteur est associe a la formule « la forme suit la fonction » ?", "Le Corbusier~Louis Sullivan~Dieter Rams~Venturi", 1,
     "Louis Sullivan a formule cette maxime, reprise par le functionalisme."),
 QC("Quelle contrainte est liee au budget du projet ?", "Contrainte technique~Contrainte economique~Contrainte semantique~Contrainte culturelle", 1,
     "Le budget et le cout de production relevent des contraintes economiques."),
 QC("Quelle est la difference entre valeur d'usage et valeur d'echange ?", "L'une est technique, l'autre est sensationnelle~L'une sert l'utilisateur, l'autre le marche~Elles sont identiques~L'une est toujours superieure", 1,
     "La valeur d'usage correspond au service rendu, la valeur d'echange a la valeur commerciale."),
 QC("Pourquoi le contexte est-il important en design ?", "Il determine la pertinence de la solution~Il remplace le brief~Il interdit la creativite~Il ne concerne que le prix", 0,
     "Une solution pertinente dans un contexte peut ne pas l'etre dans un autre."),
 QT("Analyser une chaise de bureau sous l'angle des trois fonctions (technique, usage, symbolique).",
    "La fonction technique de la chaise est de soutenir le corps et de resister a une charge donnee, grace a une structure et des materiaux adaptes. Sa fonction d'usage concerne l'assise, le dossier, les accoudoirs, les reglages, la stabilite et la facilite de deplacement : la forme invite a s'asseoir et indique comment le faire. Sa fonction symbolique tient au choix des materiaux, de la couleur et de la ligne : une chaise de direction en cuir signale un statut, tandis qu'une chaise en plastique coloré signale la modernite ou la convivialite. Un bon projet equilibre ces trois dimensions au lieu de sacrifier l'une au profit d'une autre.",
    "On attend une analyse distincte des trois fonctions et des exemples concrets."),
 QT("Comment le designer peut-il reveler un besoin latent chez des utilisateurs ?",
    "Il ne peut pas se contenter de demander aux gens ce qu'ils veulent : ils decrivent souvent des solutions deja connues. Il observe plutot les gestes reels, les hésitations, les contournements et les usages improvises. Il mene des entretiens ouverts, produit des scenarios et des personas, puis confronte ses hypotheses a des prototypes simples. Les situations de frustration sont particulierement riches : un geste repetitif ou un objet detourne signale un besoin non formule. Il doit ensuite distinguer ce qui est general de ce qui est propre a quelques utilisateurs, et verifier que la solution proposee reste viable techniquement et economiquement.",
    "La reponse doit etre methodique : observation, entretiens, prototypes et validation.")],
C("Le design commence par le besoin : une solution pertinente repond a une fonction technique, a un usage et a une attente symbolique dans un contexte donne.",
  "Besoin + contexte + contraintes = probleme de design",
  "affordance · fonctions technique / d'usage / symbolique · valeur d'usage",
  "Besoin explicite~Formule par le client~Besoin latent~A reveler~Fonction technique~Ce que l'objet fait~Fonction d'usage~Comment on s'en sert",
  "Ecouter le commanditaire|Observer les usages reels|Degager les fonctions attendues|Lister les contraintes|Formuler le probleme avant la forme",
  "Proposer une forme avant d'analyser|Confondre besoin et solution|Ignorer la dimension symbolique|Oublier le contexte d'usage",
  "Chaise~Soutenir le corps~Affordance~Inviter a s'asseoir~Symbolique~Cuir et statut~Contrainte~Budget et norme~Contexte~Bureau ou maison",
  "Valeur d'usage~Service rendu~Valeur d'echange~Prix de marche",
  "Forme suit fonction~Functionaliste~Forme et sens~Approche semiotique"))

# ============================================================ DT02
add("DT02", "Ergonomie et design centre utilisateur", "Théorie du design", T,
S("L'ergonomie adapte le produit, l'espace ou l'interface a l'etre humain et a ses capacites."
  "|L'anthropometrie fournit les dimensions du corps : taille, largeur, portee et force."
  "|On raisonne souvent en percentiles : le 5e, le 50e et le 95e de la population."
  "|Concevoir pour le 50e seulement exclut les personnes tres petites ou tres grandes."
  "|La posture et le geste determiment le confort et la fatigue a l'usage."
  "|La charge cognitive designe l'effort mental necessaire pour comprendre et agir."
  "|Une bonne affordance rend l'action possible et visible ; un retour immediat confirme l'action."
  "|L'accessibilite vise a rendre l'objet ou l'interface utilisable par le plus grand nombre."
  "|Les tests utilisateurs observent des personnes reelles accomplissant des taches donnees."
  "|Les personas et les scenarios aident a representer des profils d'utilisateurs types."
  "|L'iteration corrige les defauts repères grace aux tests successifs."
  "|En design d'espace, ergonomie signifie aussi circulation, degagement et confort visuel."),
[QC("Que fournit l'anthropometrie au designer ?", "Des couleurs~Des dimensions du corps~Des prix~Des polices", 1,
     "L'anthropometrie mesure les dimensions et les capacites physiques humaines."),
 QC("Quel percentile correspond a une personne de grande taille ?", "Le 5e~Le 50e~Le 95e~Le 0e", 2,
     "Le 95e percentile represente les personnes de grande taille dans la population consideree."),
 QC("Quel risque presente une conception basee uniquement sur le 50e percentile ?", "Un cout plus eleve~L'exclusion des personnes extremes~Une meilleure ergonomie~Aucun risque", 1,
     "Elle ignore les besoins des personnes tres petites ou tres grandes."),
 QC("Qu'appelle-t-on charge cognitive ?", "Le poids d'un objet~L'effort mental pour comprendre et agir~La force musculaire~La duree de fabrication", 1,
     "C'est l'effort mental mobilise par une tache ou une interface."),
 QC("Quel dispositif confirme a l'utilisateur que son action a fonctionne ?", "Une affordance~Un retour ou feedback~Une contrainte~Un persona", 1,
     "Le feedback signale l'effet de l'action : son, mouvement, changement visuel."),
 QC("Que permet un test utilisateur ?", "De remplacer le designer~D'observer des difficultes reelles~De supprimer les contraintes~De garantir le succes commercial", 1,
     "Le test revelle les problemes d'usage que le concepteur ne voit plus."),
 QC("Quel outil represente un profil d'utilisateur type ?", "Une grille de couleurs~Un persona~Un devis~Une cotation", 1,
     "Le persona est une fiction concrete qui represente un groupe d'utilisateurs."),
 QT("Expliquer la difference entre affordance et feedback dans la conception d'une poignee.",
    "L'affordance est la propriete de la poignee qui suggere l'action : sa forme, sa taille et son emplacement invitent a saisir et a tirer ou a pousser. Elle est percue avant meme l'action. Le feedback, lui, intervient apres ou pendant l'action : la porte s'ouvre, un clic se fait entendre, la poignee revient en position. Une bonne conception relie les deux : la poignee indique quoi faire et confirme que l'action a reussi. Si l'affordance est trompeuse, l'utilisateur essaie une mauvaise manipulation ; si le feedback manque, il doute et recommence. L'ergonomie travaille precisement a rendre ces deux signaux clairs et coherents.",
    "On attend la distinction avant / apres l'action et un exemple concrets."),
 QT("Comment organiser un test utilisateur simple pour une interface de presentation ?",
    "On definit d'abord un objectif precis : verifier que l'utilisateur trouve une information en moins de trente secondes, par exemple. On recrute quelques personnes representant les profils vises, sans leur expliquer la solution. On leur demande d'effectuer une tache reelle pendant qu'on observe leurs gestes, leurs hésitations et leurs commentaires, en notant les points de blocage. On pose ensuite des questions ouvertes sur la comprehension et la satisfaction. On classe les problemes par gravite, on corrige les plus critiques, puis on refait un test court pour verifier l'amelioration. Quelques utilisateurs suffisent pour reperer la majorite des defauts d'ergonomie.",
    "On attend objectif, observation, questions, Priorisation et iteration.")],
C("L'ergonomie rend le projet utilisable par de vraies personnes : dimensions, perception, comprehension et feedback guident la conception.",
  "Concevoir pour 5e, 50e et 95e percentiles",
  "affordance · feedback · charge cognitive · accessibilite · tests",
  "Anthropometrie~Dimensions du corps~Percentile~5e 50e 95e~Affordance~Action suggeree~Feedback~Action confirmee",
  "Definir les utilisateurs et les taches|Choisir les dimensions et les percentiles|Concevoir affordances et retours|Observer des tests reels|Corriger et re-tester",
  "Concevoir pour soi-meme|Negliger les extrema|Confondre affordance et feedback|Croire qu'un seul test suffit",
  "5e percentile~Personne petite~50e percentile~Moyenne~95e percentile~Personne grande~Test~Tache observee~Persona~Profil type",
  "Affordance~Avant l'action~Feedback~Apres l'action",
  "Accessibilite~Tous les usagers~Ergonomie~Confort et efficacite"))

# ============================================================ DT03
add("DT03", "Sémiologie du design : signe, symbole et connotation", "Théorie du design", T,
S("La semiotique etudie la production de sens par les signes, qu'ils soient visuels ou linguistiques."
  "|Selon Saussure, le signe forme un couple entre le signifiant, perceptible, et le signifie, conceptuel."
  "|Le rapport entre signifiant et signifie est conventionnel et varie selon les cultures."
  "|Peirce distingue l'icone, qui ressemble a son objet, l'indice, qui y est relie par une cause, et le symbole, qui repose sur une convention."
  "|La denotation est le sens premier et descriptif d'un signe."
  "|La connotation est le sens second, culturel ou emotionnel, que le signe declenche."
  "|Barthes a applique cette distinction a la publicite et aux images de masse."
  "|Une couleur n'a pas de sens universel : sa signification depend du contexte et de la culture."
  "|La typographie porte aussi du sens : une police serif peut suggerer la tradition, une sans-serif la modernite."
  "|L'image construit un discours par le cadrage, l'angle, la lumiere et la disposition des elements."
  "|Un stereotype est un signe simplificateur qui fige une representation de groupe."
  "|Le designer doit anticiper les lectures possibles et assumer la responsabilite des connotations qu'il mobilise."),
[QC("Quel couple compose le signe chez Saussure ?", "Image et mot~Signifiant et signifie~Forme et couleur~Sujet et objet", 1,
     "Saussure definit le signe par le couple signifiant / signifie."),
 QC("Quel type de signe repose sur une convention ?", "L'icone~L'indice~Le symbole~L'image", 2,
     "Le symbole, comme le drapeau, fonctionne par convention culturelle."),
 QC("Qu'est-ce qu'une connotation ?", "Le sens premier~Un sens second culturel ou emotionnel~Une erreur de lecture~La definition du dictionnaire", 1,
     "La connotation est le sens associe au signe au-dela de sa denotation."),
 QC("Quel auteur a analyse la publicite en termes de connotation ?", "Roland Barthes~Kant~Benjamin~Saussure", 0,
     "Barthes a analyse les images publicitaires dans Mythologies et La Chambre claire."),
 QC("Quel est un indice selon Peirce ?", "Un portrait ressemblant~Une fumee qui indique un feu~Un mot convenu~Une affiche", 1,
     "L'indice est lie a son objet par une relation causale ou physique."),
 QC("Quelle couleur a un sens universel selon la semiotique ?", "Le rouge~Le blanc~Le bleu~Aucune", 3,
     "Le sens d'une couleur depend du contexte culturel : aucune n'a de sens universel garanti."),
 QC("Pourquoi un stereotype est-il problematique en design ?", "Il est trop colore~Il fige une representation simplificatrice~Il coute cher~Il illustre mal", 1,
     "Le stereotype reduit un groupe a des traits simpliflies et peut blesser."),
 QT("Analyser les connotations possibles d'une police de caracteres pour une identite de marque.",
    "Une police avec empattements, comme un Garamond, renvoie a la tradition, au livre, a l'heritage et a une certaine legitimite culturelle. Une sans-serif geomerique, comme une Helvetica, evoque la modernite, la neutralite, l'efficacite et le monde industriel. Une police manuscript ou informelle suggerera la proximite, l'artisanat ou la jeunesse. Ces associations ne sont pas universelles : elles dependent du public, du secteur et des usages precedents de la marque. Le designer doit donc choisir une typographie en fonction du message et verifier qu'elle ne produit pas une connotation contradictoire, par exemple un luxe trop « corporate » pour une marque artisanale.",
    "On attend plusieurs associations culturelles et la prise en compte du contexte."),
 QT("Comment eviter les stereotypes dans une campagne visuelle ?",
    "On commence par identifier les representations dominantes du sujet et les cliches associes. On documente la diversite reelle des personnes et des situations plutot que de se fier aux images toutes faites. On varie les roles, les postures, les corps et les contextes, en evitant de reduire un groupe a un seul symbole. On fait relire les visuels par des personnes concernees et on corrige les signaux ambigus. Enfin, on garde une trace de ces choix dans le dossier de conception, pour pouvoir justifier la representation devant le commanditaire. La vigilance semiotique ne retire pas la creativite : elle rend le message plus juste et plus large.",
    "On attend documenter, diversifier, faire relire et tracer les choix.")],
C("Le design produit du sens : denotation, connotation, icone, indice et symbole permettent de decrire et de maitriser les lectures possibles.",
  "Signe = signifiant + signifie · denotation + connotation",
  "icone / indice / symbole · contexte culturel · stereotype",
  "Signifiant~Perceptible~Signifie~Concept~Icone~Ressemblance~Indice~Lien causal~Symbole~Convention",
  "Inventarier les signes presents|Dechiffrer leur denotation|Identifier les connotations|Verifier les codes culturels|Anticiper les lectures impropres",
  "Croire au sens universel des couleurs|Confondre icone et symbole|Ignorer le contexte de reception|Laisser passer un stereotype",
  "Couleur~Sens contextuel~Serif~Tradition~Sans-serif~Modernite~Cadrage~Discours de l'image~Stereotype~Representation fige",
  "Denotation~Sens premier~Connotation~Sens culturel",
  "Icone~Ressemble~Symbole~Convention"))

# ============================================================ DT04
add("DT04", "Design et développement durable : éco-conception", "Théorie du design", T,
S("Les produits de design consomment des ressources et produisent des dechets a chaque etape de leur vie."
  "|L'analyse du cycle de vie, ou ACV, recense les impacts de l'extraction a la fin de vie."
  "|Le cycle comprend l'extraction des matieres, la fabrication, le transport, l'usage et la fin de vie."
  "|L'eco-conception consiste a reduire ces impacts des la phase de conception."
  "|La regle des 3 R, reduire, reutiliser, recycler, complete aujourd'hui par reparer."
  "|Reduire la matiere, les emballages et les transports diminue directement l'empreinte."
  "|Les materiaux recyclees ou biosources offrent des alternatives aux ressources fossiles."
  "|La durabilite et la reparabilite prolongent la vie utile de l'objet."
  "|L'obsolescence, qu'elle soit technique ou esthetique, raccourcit cette duree de vie."
  "|La modularite permet de remplacer une piece plutot que de jeter l'objet entier."
  "|Le choix d'un approvisionnement local limite les transports et soutient les ateliers proches."
  "|Des reglementations comme la REP ou la loi AGEC obligent les acteurs a mieux gerer les dechets."),
[QC("Que mesure une analyse du cycle de vie ?", "Le cout de vente~Les impacts environnementaux de l'extraction a la fin de vie~La popularite d'un produit~La duree du projet", 1,
     "L'ACV inventorie les impacts environnementaux a toutes les etapes de la vie du produit."),
 QC("Laquelle de ces etapes ne fait pas partie du cycle de vie ?", "L'extraction des matieres~La fabrication~Le transport~La ellection du designer", 3,
     "L'election du designer n'est pas une etape du cycle de vie du produit."),
 QC("Que signifie le R « reparer » dans l'eco-conception ?", "Remplacer l'objet des la panne~Concevoir pour pouvoir remplacer une piece~Jeter plus vite~Emballer davantage", 1,
     "Reparer implique une conception demontable et des pieces disponibles."),
 QC("Quel materiau est biosource ?", "Le plastique issu du petrole~Le bois issu d'une foret geree~L'acier recycle~Le verre fondu", 1,
     "Un materiau biosource provient de la biomasse, comme le bois, le liege ou le chanvre."),
 QC("Quel effet a la modularite sur la duree de vie ?", "Elle la raccourcit~Elle la prolonge en permettant le remplacement d'elements~Elle n'a aucun effet~Elle interdit la reparation", 1,
     "Un objet modular peut etre entretenu et mis a jour sans etre jete."),
 QC("Quel est un risque de l'obsolescence esthetique ?", "Un objet encore fonctionnel est remplace pour des raisons de mode~L'objet devient plus solide~Le prix baisse~La reparation devient inutile", 0,
     "L'obsolescence esthetique pousse au remplacement d'un objet encore utilisable."),
 QC("Quel texte reglementaire francais concerne notamment les dechets et la reparabilite ?", "La loi AGEC~La loi sur laPresse de 1881~Le code civil de 1804~La loi du 9 decembre 1905", 0,
     "La loi AGEC (anti-gaspillage pour une economie circulaire) instaure des obligations de reparabilite et de tracabilite."),
 QT("Expliquer pourquoi l'eco-conception doit intervenir des la phase de croquis.",
    "A la phase de croquis, les choix structurants sont encore ouverts : forme, matiere, assemblage, nombre de pieces, format et emballage. Ces decisions determinent une grande partie des impacts futurs, alors que les modifications coutent peu. Plus on avance dans le projet, plus il devient difficile et couteux de changer de materiau ou de procede. Eco-conceptionner tot, c'est par exemple prevoir un assemblage demontable, reduire le nombre de pieces, choisir une matiere recyclable et limiter les emballages. Ce n'est pas une contrainte ajoutee a la fin : c'est une maniere de poser le probleme des le debut, en reliant la forme a son cycle de vie complet.",
    "On attend l'importance des choix amont, la facilite de modification et des exemples concrets."),
 QT("Comment concilier un objectif esthetique et la sobriete des moyens dans un projet de mobilier ?",
    "On peut d'abord faire de la sobriete un parti pris esthetique : une ligne simple, une matiere unique et un assemblage lisible produisent une qualite visuelle sans surconsommation. Ensuite, on concentre l'effort de design la ou il compte : proportion, finition, toucher et rapport au corps, plutot que dans l'ajout de decor. On choisit des materiaux durables et reparables, on dessine des pieces demontables avec des fixations visibles, et on limite les traitements de surface polluants. On verifie enfin le transport et l'emballage, par exemple en concevant un meuble en kit compact. La contrainte environnementale devient alors un generateur de formes plutot qu'un frein.",
    "On attend des solutions concretes : matiere, assemblage, finition, emballage et esthetique assumee.")],
C("L'eco-conception integre l'impact environnementale des le debut du projet : reduire, reutiliser, recycler, reparer.",
  "ACV : extraction → fabrication → transport → usage → fin de vie",
  "3 R + reparer · biosource · reparabilite · obsolescence · AGEC",
  "ACV~Cycle de vie~Extraction~Debut du cycle~Fabrication~Transformation~Usage~Vie utile~Fin de vie~Dechets",
  "Cartographier le cycle de vie|Repérer les postes d'impact les plus forts|Reduire matiere et emballage|Choisir des materiaux et assemblages reparables|Verifier la reglementation et documenter",
  "Ajouter l'eco-conception en fin de projet|Confondre recyclable et recycle|Ignorer la phase d'usage|Choisir un materiau sans connaitre son origine",
  "Bois~Materiau biosource~Kit~Transport reduit~Vis apparentes~Demontage~Modularite~Remplacement~AGEC~Obligation legale",
  "Recycler~Reprendre la matiere~Reparer~Prolonger l'usage",
  "Obsolescence technique~Pan ou incompatibilite~Obsolescence esthetique~Mode et gout"))

# ============================================================ DT05
add("DT05", "Theorie de la reception : lecture de l'image et du message", "Théorie du design", TER,
S("La reception designe la maniere dont un public comprend et interprete une image ou un objet."
  "|Le sens ne se transmet pas intact de l'auteur au destinataire : il se construit chez le receveur."
  "|Stuart Hall distingue une lecture dominante, une lecture negociee et une lecture opposee."
  "|La lecture dominante accepte le sens propose par le message."
  "|La lecture negociee accepte le cadre mais conteste certains elements."
  "|La lecture opposee rejette le sens propose et en produit un autre."
  "|L'horizon d'attente designe les attentes et les connaissances que le public apporte a la reception."
  "|Un message peut etre lu differemment selon l'age, la culture, le milieu ou le contexte de diffusion."
  "|La rhetorique visuelle organise le regard par la hierarchie, le contraste, le cadrage et la direction des lignes."
  "|Le medium et le support influencent la reception : une meme image ne se lit pas de la meme facon sur une affiche et sur un ecran."
  "|La charge d'attention disponible limite la quantite d'informations reellement percues."
  "|Le designer anticipe les lectures sans pouvoir les controler : il teste, ecoute et ajuste."),
[QC("Quel auteur a propose les trois types de lecture ?", "Roland Barthes~Stuart Hall~Saussure~Benjamin", 1,
     "Stuart Hall a decrit les lectures dominante, negociee et opposee."),
 QC("Quand le public rejette le sens propose par le message, on parle de lecture...", "Dominante~Negociee~Opposee~Neutre", 2,
     "La lecture opposee construit un sens contraire a celui voulu par l'emetteur."),
 QC("Qu'appelle-t-on horizon d'attente ?", "La ligne d'horizon d'une image~Les attentes et connaissances du public~Le cadre de l'affiche~La fin du projet", 1,
     "C'est l'ensemble des repères que le lecteur apporte avant la reception."),
 QC("Quel element n'influe pas sur la reception ?", "Le contexte culturel~Le support de diffusion~L'age du public~Le nombre de vis dans l'atelier", 3,
     "La reception depend du public et du medium, pas d'un element technique sans rapport."),
 QC("Comment le cadrage agit-il sur la lecture d'une image ?", "Il change la couleur~Il oriente l'attention et selectionne ce qui est vu~Il supprime le sens~Il rend l'image plus grande", 1,
     "Le cadrage choisit ce qui entre dans l'image et guide le regard."),
 QC("Quelle consequence a la charge d'attention limitee ?", "Le public lit tout~Trop d'informations peuvent ne pas etre percues~L'image devient inutile~Le message est automatiquement compris", 1,
     "Un public expose a beaucoup d'informations ne traite qu'une partie du message."),
 QC("Que doit faire le designer face a la diversite des lectures ?", "Imposer une seule lecture~Tester et ajuster en ecoutant le public~Supprimer toute image~Ignorer les retours", 1,
     "Il ne controle pas la reception, mais peut l'observer et adapter son projet."),
 QT("Illustrer les trois lectures de Hall avec une affiche de campagne environnementale.",
    "Une affiche montrant une decharge et le slogan « Notre planete merite mieux » peut etre lue de trois facons. La lecture dominante accepte le message : il faut reduire nos dechets. Une lecture negociee approuve l'objectif mais conteste le moyen, par exemple en estimant que la responsabilite individuelle est mise en avant a la place des industriels. Une lecture opposee rejette le message et y voit une campagne culpabilisante ou verte, produisant un sens contraire a celui voulu. Ces trois lectures montrent que le sens ne reside pas entierement dans l'image : il depend aussi des valeurs et des experiences du public.",
    "On attend une situation concrete et trois interpretations distinctes et coherentes."),
 QT("Comment un designer peut-il tester la reception d'une identite visuelle avant sa diffusion ?",
    "Il peut organiser des tests courts avec des personnes representant les publics vises, sans leur expliquer au prealable l'intention de la marque. Il leur demande ce qu'elles voient en premier, quels mots leur viennent, quel univers elles imaginent et si le message leur parait credible. Il compare ensuite ces reponses avec les objectifs du brief et repere les ecarts : une couleur mal lue, un symbole ambigu ou un titre trop discret. Il peut aussi tester le visuel dans ses contextes reels d'affichage, a differentes tailles et sur differents supports. Enfin, il documente les resultats et ajuste les elements qui generent le plus d'incomprehensions, en gardant a l'esprit qu'aucune lecture n'est totalement controllable.",
    "On attend des tests aupres du public, une comparaison avec le brief et des adjustments argumentes.")],
C("La reception construit le sens chez le public : le designer propose une lecture, mais il doit anticiper les autres et tester son message.",
  "Hall : lecture dominante / negociee / opposee",
  "horizon d'attente · rhetorique visuelle · medium · attention",
  "Emetteur~Produit le message~Destinataire~Construit le sens~Dominante~Sens accepte~Negociee~Accord partiel~Opposee~Sens refuse",
  "Formuler l'intention du message|Identifier les publics et leurs attentes|Analyser les signes et leur hierarchie|Tester la reception reelle|Corriger les incomprehensions",
  "Croire que le sens est unique|Ignorer le public reel|Tester uniquement aupres de l'equipe|Confondre attention et comprehension",
  "Affiche~Support public~Ecran~Autre contexte de lecture~Cadrage~Selection du regard~Test~Public interroge~Ajustement~Correction du message",
  "Dominante~Sens voulu~Opposee~Sens inverse",
  "Intention~Ce que veut l'auteur~Reception~Ce que comprend le public"))

# ============================================================ DC01
add("DC01", "Composition : equilibre, hierarchie et rythme", "Création et composition", T,
S("La composition organise les elements visuels sur un support selon une intention precise."
  "|L'equilibre peut etre symetrique et stable, ou asymetrique et dynamique."
  "|Le poids visuel depend de la taille, du contraste, de la couleur et de la position."
  "|Un petit element tres contraste peut equilibrer une grande zone plus claire."
  "|La hierarchie etablie un ordre de lecture : ce qui est vu en premier, puis ensuite."
  "|Le rythme nait de la repetition et de la variation des elements."
  "|La proportion regle les rapports de taille entre les parties et le tout."
  "|L'echelle modifie la perception : un meme motif se lit differemment en grand et en petit."
  "|L'espace negatif, ou vide, est un element actif de la composition."
  "|La grille aide a repartir les elements et a maintenir des alignements."
  "|Les lois de Gestalt expliquent la proximite, la similarite et la continuite des formes."
  "|Une composition reussie sert le message et resiste aux differentes tailles d'affichage."),
[QC("Quel type d'equilibre produit une sensation de dynamisme ?", "L'equilibre symetrique~L'equilibre asymetrique~L'absence d'equilibre~L'alignement strict", 1,
     "L'equilibre asymetrique compense des poids inegaux et crée une tension dynamique."),
 QC("Qu'est-ce qui determine le poids visuel d'un element ?", "Son seul nom~Sa taille, son contraste, sa couleur et sa position~Son prix~Sa date de creation", 1,
     "Plusieurs facteurs visuels contribuent au poids percue d'un element."),
 QC("Quel role joue l'espace negatif ?", "Il doit toujours etre supprime~Il structure et fait respirer la composition~Il remplace le titre~Il camouflle les erreurs", 1,
     "Le vide est un element actif qui met en valeur les formes et organise la lecture."),
 QC("Quelle loi de Gestalt explique que des elements proches soient percus ensemble ?", "La similarite~La proximite~La continuite~La symetrie", 1,
     "La loi de proximite regroupe les elements proches dans la perception."),
 QC("Comment obtenir un rythme visuel ?", "En repetant tous les elements a l'identique~En alternant repetition et variation~En supprimant les couleurs~En utilisant une seule taille", 1,
     "Le rythme vient d'une repetition ponctuee de variations."),
 QC("A quoi sert une grille de composition ?", "A limiter la creativite~A organiser et aligner les elements~A remplacer le message~A cacher le texte", 1,
     "La grille est un outil d'organisation au service de la lisibilite."),
 QC("Pourquoi tester une composition en petit format ?", "Pour gagner du temps~Pour verifier que la hierarchie reste lisible~Pour changer de couleur~Pour supprimer le texte", 1,
     "Une composition doit rester comprehensible a differentes echelles de diffusion."),
 QT("Expliquer comment construire une hierarchie visuelle dans une affiche.",
    "On decide d'abord quelle information doit etre lue en premier, generalement le titre ou l'image principale. On lui donne le plus fort poids visuel par la taille, le contraste ou une couleur accent. Les informations secondaires, comme le sous-titre ou la date, recoivent un poids intermediaire, tandis que les details et les mentions legales restent discrets mais lisibles. On verifie ensuite les espacements et les alignements pour que l'oeil suive un chemin continu. Enfin, on teste l'affiche en petit format et a distance : si la hierarchie s'effondre, il faut renforcer les contrasts plutot que d'ajouter des elements.",
    "On attend une progression nette entre niveaux d'importance et une verification en contexte."),
 QT("Comment l'equilibre asymetrique peut-il etre stable malgre l'absence de symetrie ?",
    "Un grand element clair peut etre compense par un petit element sombre ou tres contraste, car le poids visuel ne depend pas seulement de la surface. La position compte aussi : un element place loin du centre exerce une influence plus forte. On peut encore equilibrer par la direction des lignes, la couleur ou la densite de detail. L'equilibre asymetrique ressemble a une balance ou les plateaux sont differents mais les moments s'equivalent. Il donne une impression de mouvement et de vitalite tout en evitant la chute visuelle, a condition que les rapports de poids soient reellement maitrises.",
    "On doit expliquer la compensation des poids et le role du contraste et de la position.")],
C("La composition rend le message lisible en orchestrant poids, vide, rythme et proportions sur une grille.",
  "Poids visuel = taille × contraste × couleur × position",
  "equilibre symetrique / asymetrique · hierarchie · Gestalt · espace negatif",
  "Equilibre~Repartition des poids~Poids visuel~Taille et contraste~Hierarchie~Ordre de lecture~Rythme~Repetition et variation",
  "Definir l'intention et le message|Choisir les elements a forte valeur|Placer les poids sur une grille|Menager des vides et un rythme|Tester a differentes echelles",
  "Remplir tout l'espace disponible|Multiplier les centres d'interet|Confondre symetrie et equilibre|Ignorer le format de diffusion",
  "Petit element sombre~Compense une grande zone~Grille~Alignement~Vide~Respiration~Gestalt~Proximite~Contraste~Poids fort",
  "Symetrique~Stable et statique~Asymetrique~Dynamique et tendue",
  "Espace positif~Ce qui est occupe~Espace negatif~Le vide actif"))

# ============================================================ DC02
add("DC02", "Ligne, forme et volume : elements du langage visuel", "Création et composition", T,
S("Le point est l'unite minimale du langage visuel et peut devenir ligne par repetition."
  "|La ligne peut etre droite, courbe, oblique, verticale ou horizontale."
  "|Sa direction produit une sensation : stabilite pour la verticale, mouvement pour l'oblique."
  "|Le contour delimite une forme et en fixe la silhouette."
  "|Une forme est geometrique ou organique, simple ou complexe."
  "|La valeur, ou ton, organise les passages du clair au sombre."
  "|La texture apporte une information tactile visuelle : rugueux, lisse ou granuleux."
  "|Le volume se construit par le modelé, les ombres et la lumiere."
  "|La lumiere et l'ombre donnent du relief et situent la source d'eclairage."
  "|Le rapport figure-fond determine ce qui est percu comme sujet ou comme arriere-plan."
  "|L'espace positif occupe la surface tandis que l'espace negatif l'entoure."
  "|Ces elements forment un vocabulaire pour decrire, analyser et justifier une production."),
[QC("Quel element est l'unite minimale du langage visuel ?", "La ligne~Le point~La couleur~Le volume", 1,
     "Le point est l'unite de base ; sa repetition engendre la ligne."),
 QC("Quelle ligne suggere le mouvement ?", "La ligne horizontale~La ligne verticale~La ligne oblique~Le point", 2,
     "La ligne oblique est dynamique, tandis que l'horizontale et la verticale sont plus stables."),
 QC("Qu'est-ce que la valeur d'une forme ?", "Son prix~Son degre de clairete ou d'obscurite~Sa duree~Son nome", 1,
     "La valeur designe le ton clair ou sombre, independamment de la teinte."),
 QC("Quel element donne du relief a un volume dessine ?", "Le titre~L'ombre et la lumiere~La legendre~Le format", 1,
     "Le modelé par les ombres et les lumieres construit l'illusion du volume."),
 QC("Que designe le rapport figure-fond ?", "La couleur dominante~La distinction entre sujet et arriere-plan~Le cadrage~Le contraste", 1,
     "Il s'agit de la perception de ce qui avance ou recule dans l'image."),
 QC("Quelle texture est decrite comme granuleuse ?", "Une surface lisse et brillante~Une surface avec de petits grains~Une surface transparente~Une surface sans relief", 1,
     "Une texture granuleuse presente de petites irregularites visibles et tactiles."),
 QC("A quoi sert ce vocabulaire visuel ?", "A decorer une page~A decrire et justifier des choix de forme~A remplacer le dessin~A accelerer l'impression", 1,
     "Il permet d'analyser et d'argumenter precisement sur une production."),
 QT("Decrire avec precision une forme simple en utilisant le vocabulaire visuel.",
    "On peut decrire une coupelle comme une forme organique a contours courbes, dont le volume est suggere par un modelé clair sur le bord superieur et une ombre portee sous la base. La valeur du fond est plus sombre que celle de la coupelle, ce qui etablit un rapport figure-fond net. La ligne d'horizon n'apparait pas : l'espace negatif autour de l'objet reste neutre et met en valeur sa silhouette. La texture parait lisse et legerement brillante, ce qui indique une surface ceramique emaillee pluto qu'un materiau rugueux. Cette description precis permet de justifier un choix de representation.",
    "On attend l'usage de termes comme contour, valeur, modelé, figure-fond et texture."),
 QT("Comment passer d'un croquis de ligne a une etude de volume ?",
    "On commence par le trait : la ligne exterieure fixe la silhouette et les lignes interieures indiquent les changements de direction. On determine ensuite la source de lumiere, puis on place les zones de valeur : les plus claires vers la source, les plus sombres a l'oppose. On ajoute les ombres portees pour ancrer l'objet sur le support et renforcer sa presence. Les lignes de contour peuvent ensuite s'attenuer la ou la lumiere est forte. On verifie enfin que le rapport figure-fond reste lisible et que le volume parait coherent sous differents angles. Le croquis devient alors une etude de forme plutot qu'un simple dessin de contour.",
    "La demarche attendue : contour, source de lumiere, valeurs, ombres portees et verification.")],
C("Ligne, forme, valeur, texture et volume forment un vocabulaire precis pour voir, dessiner et justifier.",
  "Volume = contour + valeurs + ombres + lumiere",
  "point → ligne → forme → volume · figure-fond · espace negatif",
  "Point~Unite minimale~Ligne~Direction et mouvement~Contour~Silhouette~Forme~Geometrique ou organique",
  "Observer la silhouette|Tracer les lignes de construction|Placer la source de lumiere|Construire les valeurs et ombres|Verifier figure-fond et lisibilité",
  "Dessiner sans observer|Ignorer la source de lumiere|Confondre valeur et couleur|Remplir tout le fond",
  "Oblique~Mouvement~Verticale~Stabilite~Modelé~Relief~Ombre portee~Ancrage~Figure-fond~Lecture du sujet",
  "Geometrique~Cercle carre triangle~Organique~Formes naturelles",
  "Valeur~Clair et sombre~Teinte~Famille de couleur"))

# ============================================================ DC03
add("DC03", "Espace et perspective : codes de representation", "Création et composition", T,
S("Representer l'espace sur une surface plane demande des codes visuels appris et maitrises."
  "|La perspective parallele garde les aretes paralleles et se prete bien a la cotation."
  "|La perspective cavaliere utilise des fuyantes inclinees, souvent a 45 degrees."
  "|La perspective centrale fait converger les fuyantes vers un point de fuite."
  "|La ligne d'horizon se situe a la hauteur de l'oeil de l'observateur."
  "|La perspective a deux points de fuite convient aux vues d'angle d'un objet."
  "|La diminution des tailles avec la distance cree l'illusion de profondeur."
  "|Les ombres portees et l'orientation des plans renforcent la lisibilite de l'espace."
  "|Le cadrage determine ce qui est inclus ou exclu du champ de representation."
  "|Les vues, coupes et elevations sont les codes du dessin technique."
  "|L'axonométrie montre trois dimensions sans deformation liee a la distance."
  "|Le choix du code depend de l'usage : croquis expressif, plan de fabrication ou maquette."),
[QC("Quel code garde les aretes paralleles ?", "La perspective centrale~La perspective parallele~La perspective a deux points~L'axonométrie", 1,
     "En perspective parallele, les aretes paralleles dans la realite restent paralleles sur le dessin."),
 QC("Ou se situe la ligne d'horizon ?", "Au milieu du papier~A la hauteur de l'oeil~Toujours en bas~Au-dessus de l'objet", 1,
     "La ligne d'horizon correspond a la hauteur du regard de l'observateur."),
 QC("Que sont les fuyantes ?", "Des lignes horizontales~Des lignes qui convergent vers un point de fuite~Des ombres~Des cotes", 1,
     "Les fuyantes sont les droites perpendiculaires au plan de l'image qui convergent."),
 QC("Quand utiliser une perspective a deux points de fuite ?", "Pour une vue de face~Pour une vue d'angle d'un objet~Pour un plan coté~Pour une coupe", 1,
     "Une vue d'angle fait converger les aretes vers deux points de fuite distincts."),
 QC("Quel procede renforce l'illusion de profondeur ?", "La diminution des tailles avec la distance~L'augmentation des contrastes uniquement~Le titre~La signature", 0,
     "Les objets eloignes paraitssent plus petits et moins contrastes."),
 QC("Quel code technique represente une coupe d'un objet ?", "La vue de face~La coupe~L'elevation~Le point de fuite", 1,
     "La coupe montre l'interieur de l'objet apres une section imaginee."),
 QC("Quel interet presente l'axonométrie ?", "Elle montre trois dimensions sans deformation de perspective~Elle supprime le volume~Elle est reserve au texte~Elle interdit les ombres", 0,
     "L'axonométrie conserve les paralleles et les proportions, utile pour les vues techniques."),
 QT("Expliquer la difference entre perspective centrale et perspective parallele et leurs usages.",
    "La perspective centrale reproduit la vision humaine : les aretes eloignees convergent vers un point de fuite situe sur la ligne d'horizon, et les tailles diminuent avec la distance. Elle donne une image realistic et est adaptee aux croquis d'ambiance, aux vues d'architecture et aux storyboards. La perspective parallele, elle, garde les aretes paralleles et les proportions ; elle est moins realiste mais permet de mesurer et de coter directement sur le dessin. On l'utilise pour les plans de fabrication, les vues explosees et les schemas techniques. Le choix depend donc de l'objectif : montrer une impression ou transmettre des dimensions fiables.",
    "On attend l'opposition convergence / paralleles et des usages distincts."),
 QT("Comment eviter les erreurs frequentes dans un croquis en perspective ?",
    "La premiere erreur est de placer la ligne d'horizon n'importe ou : elle doit etre a la hauteur du regard et cohérente avec tous les points de fuite. La deuxieme est de melanger les methodes : dans une perspective centrale, toutes les fuyantes d'une meme direction doivent converger vers le meme point. La troisieme est de negliger l'echelle : deux objets de meme taille a des distances differentes ne doivent pas etre dessines de la meme grandeur. On corrige en construisant d'abord une ligne d'horizon et des points de fuite legerement, puis en verifiant chaque arete par rapport a ces reperes. Les ombres portees doivent enfin suivre la meme direction pour ancrer les objets.",
    "La reponse doit citer ligne d'horizon, points de fuite, echelle et ombres coherentes.")],
C("La perspective est un code de representation : le choix entre convergence et paralleles depend de l'usage du dessin.",
  "Point de fuite + ligne d'horizon + fuyantes = perspective centrale",
  "parallele · cavaliere · centrale · axonométrie · coupe",
  "Perspective centrale~Convergence~Point de fuite~Ligne d'horizon~Fuyantes~Vers le point~Axonometrie~Sans deformation",
  "Choisir le code adapte a l'usage|Placer ligne d'horizon et points de fuite|Tracer les fuyantes legerement|Respecter l'echelle et les ombres|Verifier la coherence de l'ensemble",
  "Melanger plusieurs systemes|Placer l'horizon au hasard|Ignorer la diminution des tailles|Oublier la direction des ombres",
  "Horizon~Hauteur de l'oeil~Fuyante~Vers le point de fuite~Cotation~Perspective parallele~Storyboard~Perspective centrale~Coupe~Voir l'interieur",
  "Parallele~Coter et mesurer~Centrale~Rendre la profondeur",
  "Cavaliere~Fuyantes a 45 degrees~Axonometrie~Trois dimensions lisibles"))

# ============================================================ DC04
add("DC04", "Methodes de creativite : divergence et convergence", "Création et composition", T,
S("La creativite n'est pas seulement une inspiration : elle se developpe par des methodes et une posture."
  "|La recherche alterne des phases de divergence et de convergence."
  "|En divergence, on produit un maximum d'idees sans les juger immediatement."
  "|Le brainstorming demande de suspendre le jugement et de viser la quantite."
  "|Le mind mapping developpe des associations a partir d'un mot ou d'une image centrale."
  "|L'analogie et le transfert de solutions venues d'un autre domaine stimulent l'invention."
  "|La methode SCAMPER propose de substituer, combiner, adapter, modifier ou reutiliser."
  "|Le forcing de relations associe deux elements sans rapport pour creer de nouvelles pistes."
  "|La convergence compare et selectionne les idees selon des criteres explicites."
  "|L'experimentation materielle permet de tester une hypothese rapidement en atelier."
  "|Il faut documenter chaque hypothese par des croquis et des notes pour la presenter."
  "|Une posture d'observation active nourrit la creativite pendant tout le projet."),
[QC("Quelle phase vise la quantite d'idees sans jugement ?", "La convergence~La divergence~La validation~La fabrication", 1,
     "La divergence produit un maximum de pistes avant toute selection."),
 QC("Quelle regle est essentielle au brainstorming ?", "Critiquer des le debut~Suspendre le jugement~Travailler seul~Ecrire tres peu", 1,
     "On suspend le jugement pour ne pas bloquer la production d'idees."),
 QC("Que permet le mind mapping ?", "De classer des factures~De developper des associations autour d'un mot central~De coter un plan~De choisir une police", 1,
     "La carte mentale fait rayonner des associations a partir d'un noyau."),
 QC("Que propose la methode SCAMPER ?", "De suppression systematique~De transformer une solution par differentes operations~De dessiner a la regle~De reproduire un modele", 1,
     "SCAMPER est une grille d'actions : substituer, combiner, adapter, modifier, etc."),
 QC("A quoi sert le forcing de relations ?", "A interdire les associations~A creer des pistes inattendues en rapprochant des elements~A choisir une couleur~A terminer le projet", 1,
     "Il force une association inhabituelle pour sortir des habitudes."),
 QC("Sur quoi repose la convergence ?", "Sur le hasard~Sur des criteres explicites de comparaison~Sur le nombre d'idees~Sur l'age du designer", 1,
     "On selectonne les hypothese selon des criteres definis a l'avance."),
 QC("Pourquoi documenter les hypotheses ?", "Pour occuper le dossier~Pour pouvoir les presenter et les defendre~Pour eviter de dessiner~Pour remplacer le prototype", 1,
     "La trace ecrite et graphique rend le cheminement visible et argumentable."),
 QT("Dechiffrer la difference entre divergence et convergence dans une recherche de forme.",
    "En divergence, le designer explore largement : il produit beaucoup de croquis, essaye des materiaux, mobilise des analogies et accepte des pistes improbables. L'objectif est la quantite et la diversite, avec un jugement suspendu. En convergence, il revient sur cette production : il compare les pistes selon des critères comme la reponse au besoin, la faisabilite technique, le cout, l'ergonomie et la qualite formelle. Il en garde quelques-unes, les combine, puis les developpe. Les deux phases sont necessaires : sans divergence, on se fige sur la premiere idee ; sans convergence, le projet reste epars. Un projet de design alterne plusieurs fois ces deux movements.",
    "On attend les objectifs opposes des deux phases et la necessite de leur alternance."),
 QT("Comment conduire une seance de brainstorming utile pour un projet de mobilier ?",
    "On prepare d'abord la question : comment rendre un petit bureau plus confortable pour un usage debout assis ? On forme un groupe varie, on defini une duree courte et on rapelle la regle du suspend du jugement. Chacun propose des idees, evenement farfelues, et on les note toutes visuellement. On anime la seance avec des relances : et si le meuble se pliait, et si le plateau changeait de hauteur, et si le materiau etait souple ? On termine par une convergence rapide : on regroupe les idees par theme et on en retient trois selon des critères simples. On photographie les notes et on les archive dans le dossier de projet pour la soutenance.",
    "On attend preparation, regles, animation, convergence et trace documentaire.")],
C("La creativite se structure en alternant ouverture et selection : produire beaucoup, puis choisir selon des critères.",
  "Divergence = quantite et suspens du jugement · Convergence = criteres",
  "brainstorming · mind mapping · SCAMPER · analogie · forcing",
  "Divergence~Produire beaucoup~Convergence~Choisir selon criteres~Brainstorming~Suspendre le jugement~Mind mapping~Associations",
  "Poser une question ouverte|Produire un maximum de pistes|Relancer avec des analogies|Comparer selon des critères|Documenter et approfondir les choix",
  "Juger des la premiere idee|Confondre nombre et qualite|Ne jamais sortir de sa discipline|Oublier de tracer les pistes abandonnees",
  "SCAMPER~Substituer combiner adapter~Forcing~Rapprocher l'eloigne~Prototype~Test rapide~Observation~Source d'inspiration~Criteres~Faisabilite et besoin",
  "Divergence~Ouvrir le champ~Convergence~Reduire aux meilleures pistes",
  "Analogie~Transfert d'un autre domaine~Copie~Reprise sans transformation"))

# ============================================================ DC05
add("DC05", "Recherche iconographique et planche d'inspiration", "Création et composition", T,
S("Une recherche iconographique precede et nourrit la creation plutot que de la remplacer."
  "|Les sources possibles sont les livres, les musees, le web et la photographie personnelle."
  "|La fiabilite des sources et les droits d'usage doivent etre verifies pour chaque image."
  "|Une planche d'ambiance, ou moodboard, rassemble des references choisies."
  "|Une reference s'analyse : on identifie precisement ce que l'on retient et pourquoi."
  "|Les axes de recherche peuvent porter sur la couleur, la matiere, la forme ou l'atmosphere."
  "|Les croquis d'appropriation transforment la reference au lieu de la copier."
  "|Le classement et la hierarchisation des images rendent la recherche lisible."
  "|Une synthese en planche presente les axes retenus de maniere claire."
  "|Les sources doivent etre citees dans le dossier de projet."
  "|La recherche combine references historiques, contemporaines et observations personnelles."
  "|Cette etape constitue un argumentaire : elle justifie les choix lors de la soutenance."),
[QC("Qu'appelle-t-on une planche d'ambiance ?", "Un plan de fabrication~Un rassemblement de references visuelles choisies~Une facture~Une coupe technique", 1,
     "Le moodboard rassemble des images qui fixent une direction esthetique."),
 QC("Pourquoi verifier les droits d'une image ?", "Pour la rendre plus belle~Pour savoir si elle peut etre utilisee et citee~Pour changer sa couleur~Pour accelerer l'impression", 1,
     "L'usage d'une image est encadre par le droit d'auteur et les conditions de licence."),
 QC("Que faut-il faire d'une reference analysee ?", "La copier a l'identique~Identifier ce que l'on en retient et le transformer~La supprimer~La mettre en titre", 1,
     "L'appropriation consiste a extraire un principle et a le réinterpreter."),
 QC("Quel axe de recherche ne concerne pas le visuel ?", "La couleur~La matiere~L'atmosphere~Le code postal du commanditaire", 3,
     "Le code postal n'est pas un axe de recherche plastique."),
 QC("A quoi sert un croquis d'appropriation ?", "A reproduire une photo~A transformer une reference en piste personnelle~A remplacer la planche~A coter un meuble", 1,
     "Il montre comment un element observe devient une proposition personnelle."),
 QC("Pourquoi classer les images de la planche ?", "Pour occuper la page~Pour rendre la recherche lisible et hierarchisee~Pour augmenter le nombre d'images~Pour eviter les couleurs", 1,
     "Un classement rend visible les axes et les priorites de la recherche."),
 QC("Quel interet a la recherche iconographique pour la soutenance ?", "Elle evite de dessiner~Elle fournit des arguments pour justifier les choix~Elle remplace le prototype~Elle supprime les sources", 1,
     "Elle documente le cheminement et permet de defendre les decisions prises."),
 QT("Comment analyser une reference visuelle sans se contenter de la copier ?",
    "On decompose d'abord la reference : quels sont les dominantes de couleur, les rapports de proportion, la lumiere, les matieres et la composition ? On identifie ensuite le principle sous-jacent, par exemple un contraste de valeur ou une repetition de formes. On se demande enfin ce que ce principle apporte au probleme pose et comment le transposer dans un autre contexte. Un croquis d'appropriation transforme le principle : on garde l'idee mais on change l'echelle, la couleur ou le materiau. On cite la source pour montrer l'origine de la reference. Cette demarche produit une recherche personnelle plutot qu'un plagiat.",
    "On attend decomposition, identification d'un principle, transposition et citation."),
 QT("Comment organiser une planche d'inspiration pour une identite visuelle ?",
    "On part du brief et des mots cles : par exemple sobre, local et durable. On collecte ensuite une vingtaine d'images issues de sources variees, en notant a chaque fois l'origine. On les trie en trois axes : palette de couleurs, ambiances photographiques et exemples de typographies. On elimine les images trop proches ou trop faibles, puis on compose une planche lisible avec des titres d'axes et de breves annotations expliquant ce que chaque image apporte. On ajoute quelques croquis personnels qui montrent deja une transformation. La planche se termine par une synthese ecrite en trois phrases, qui servira d'argument a la presentation orale.",
    "On attend collecte, tri par axes, annotations, appropriation et synthese.")],
C("La recherche iconographique documente, analyse et transforme des references : elle devient un argument de conception.",
  "Reference analysée → principle retenu → croquis d'appropriation",
  "moodboard · droits d'usage · axes · citation des sources",
  "Moodboard~Planche d'ambiance~Reference~Ce que l'on retient~Appropriation~Transformation~Source~A citer~Axe~Theme de recherche",
  "Partir des mots cles du brief|Collecter des images variees|Verifier droits et fiabilite|Trier par axes et annoter|Synthetiser et presenter les choix",
  "Copier une image sans la transformer|Utiliser une source sans citation|Multiplier les images sans tri|Ignorer les droits d'usage",
  "Couleur~Axe de recherche~Matiere~Autre axe~Atmosphere~Ambiance~Croquis~Appropriation~Synthese~Trois phrases",
  "Copier~Reproduire a l'identique~S'inspirer~Extraire un principle",
  "Reference historique~Heritage~Reference contemporaine~Contexte actuel"))

# ============================================================ TP01
add("TP01", "Typographie : familles, corps et interlignage", "Typographie et couleur", T,
S("La typographie est l'art et la technique de la lettre et de sa mise en forme."
  "|Un glyphe est la representation graphique d'un caracter ; une police est un ensemble de glyphes."
  "|Une famille regroupe plusieurs styles d'une meme police, comme regular, bold ou italic."
  "|Les polices avec empattements, ou serif, portent l'heritage du livre imprime."
  "|Les polices sans empattement, ou sans-serif, sont associees a la modernite et a l'ecran."
  "|Le corps designe la taille de la police, exprimee en points pour l'impression."
  "|L'interlignage est la distance entre deux lignes ; il influe directement sur la lisibilite."
  "|La chasse et le crénage reglent l'espace entre les caracteres."
  "|La graisse et l'italique creent des contrasts sans changer de famille."
  "|La longueur de ligne, ou mesure, influe sur le confort de lecture."
  "|Une interlignage adapte est essentiel pour les longs textes."
  "|Le choix typographique doit servir le message, le support et le public."),
[QC("Qu'appelle-t-on un glyphe ?", "Une famille de police~La representation graphique d'un caracter~Un interlignage~Une page", 1,
     "Le glyphe est la forme visuelle d'un caracter dans une police donnee."),
 QC("Quelle police est associee a l'heritage du livre imprime ?", "Une sans-serif~Une serif~Une police monospace~Une police script", 1,
     "Les polices avec empattements, ou serif, viennent de la tradition du livre."),
 QC("Quel mot designe la taille d'une police ?", "La chasse~Le corps~L'italique~La mesure", 1,
     "Le corps est la taille de la police, exprimee en points."),
 QC("Qu'est-ce que l'interlignage ?", "L'espace entre deux caracteres~La distance entre deux lignes~La largeur de la page~Le nombre de familles", 1,
     "L'interlignage est la distance verticale entre les lignes de texte."),
 QC("Que regle le crénage ?", "L'espace entre certaines paires de lettres~La couleur du texte~Le nombre de pages~La resolution", 0,
     "Le crénage ajuste l'espace entre des paires de caracteres comme AV ou To."),
 QC("Quel risque presente une mesure trop longue ?", "Une lecture plus rapide~Une fatigue et une perte de repere en fin de ligne~Un texte plus gros~Aucun risque", 1,
     "Une ligne trop longue rend le retour a la ligne suivante difficile."),
 QC("Quel critere doit guider le choix d'une police ?", "Sa popularity~Le message, le support et le public~Son nombre de glyphes~Sa couleur par defaut", 1,
     "La typographie doit etre adaptee a l'intention et au contexte de lecture."),
 QT("Expliquer la difference entre une famille typographique et un style.",
    "Une famille regroupe un ensemble de polices qui partagent une meme structure de dessin, comme Garamond ou Helvetica. A l'interieur de cette famille, les styles declinent des variantes : regular, gras, italique, gras italique, parfois plusieurs graisses et largeurs. Changer de style permet de creer des contrasts et une hierarchie sans introduire une nouvelle ecriture, ce qui garde une unite visuelle. Changer de famille, au contraire, modifie profondement le ton du message. En pratique, on limite souvent le nombre de familles a deux et on joue surtout sur les styles, les tailles et les espacements pour structurer une page.",
    "On attend la distinction dessin commun / variantes et la consequence pour la mise en page."),
 QT("Comment regler la lisibilite d'un paragraphe de texte courant ?",
    "On choisit d'abord une police confortable a la lecture prolongee, avec des formes ouvertes et un bon contraste entre les caracteres. On fixe un corps suffisant selon le support, par exemple 10 a 12 points pour une impression courante, Davantage pour un ecran consulte a distance. On regle ensuite un interlignage genereusement superieur au corps, souvent autour de 120 a 145 pour cent du corps. La mesure doit rester moderee, environ 60 a 75 caracteres par ligne pour une lecture continue. On verifie enfin le contraste avec le fond, l'alignement a gauche et les espacements entre paragraphes. Une relecture sur le support final permet de corriger les problemes restants.",
    "On attend des recommandations sur corps, interlignage, mesure, contraste et support.")],
C("La typographie se regle avec precision : famille, style, corps, interlignage, chasse et mesure determinent la lisibilite.",
  "Texte lisible = corps adapte + interlignage genereux + mesure moderee",
  "serif / sans-serif · glyphe · police · famille · crénage",
  "Glyphe~Forme d'un caracter~Police~Ensemble de glyphes~Famille~Styles lies~Corps~Taille en points",
  "Choisir la famille selon le ton|Definir les styles et les tailles|Regler interlignage et mesure|Controler crénage et espacements|Tester sur le support final",
  "Multiplier les familles|Confondre corps et interlignage|Negliger la mesure|Choisir une police uniquement par gout",
  "Serif~Tradition du livre~Sans-serif~Modernite et ecran~Corps 11~Texte courant~Interlignage 14~Lecture aisee~Mesure 65~Ligne confortable",
  "Serif~Empattements~Sans-serif~Sans empattements",
  "Corps~Taille verticale~Interlignage~Distance entre lignes"))

# ============================================================ TP02
add("TP02", "Typographie et hierarchie : titre, texte et legende", "Typographie et couleur", T,
S("La hierarchie typographique etablie l'ordre dans lequel le message est lu."
  "|La taille, la graisse, la couleur et l'espacement construisent cette hierarchie."
  "|On distingue le titre, le sous-titre, le corps de texte, la legende et les notes."
  "|Une echelle typographique coherente repose sur un rapport de taille entre les niveaux."
  "|Le contraste typographique rend les niveaux immediatement reconnaissables."
  "|Il est prudent de limiter le nombre de familles, souvent a deux."
  "|La grille de ligne aligne le texte et regle le rythme vertical."
  "|Les marges et la largeur des colonnes determinent la respiration de la page."
  "|Les alignements et les espacements doivent etre coherents d'un element a l'autre."
  "|Les legendes et les annotations restent lisibles meme en petit corps."
  "|L'accessibilite impose un contraste suffisant et une taille minimale."
  "|La maquette doit etre verifiee a l'impression comme a l'ecran avant diffusion."),
[QC("Quel element n construit pas une hierarchie typographique ?", "La taille~La graisse~La couleur~Le nombre de pages du document", 3,
     "La hierarchie joue sur les caracteres visuels, pas sur la pagination."),
 QC("Que designe une echelle typographique ?", "Une regle pour mesurer les marges~Un rapport entre les tailles des niveaux de texte~Une liste de polices~Un format d'impression", 1,
     "L'echelle fixe des relations de taille coherentes entre titre, sous-titre et corps."),
 QC("Combien de familles utilise-t-on generalement dans une maquette sobre ?", "Une seule~Deux environ~Au moins cinq~Autant que de niveaux", 1,
     "Deux familles suffisent generalement a creer du contraste sans desordre."),
 QC("A quoi sert une grille de ligne ?", "A colorer le texte~A aligner le texte et a regler le rythme vertical~A remplacer les marges~A agrandir les images", 1,
     "La grille de ligne assure un rythme vertical et des alignements coherents."),
 QC("Que faut-il verifier pour les legendes en petit corps ?", "Leur couleur uniquement~Leur lisibilite~Leur nombre de mots~Leur police de titre", 1,
     "Une legende doit rester lisible malgre sa petite taille et son contraste adapte."),
 QC("Quelle exigence d'accessibilite concerne le texte ?", "Un contraste suffisant~Une police toujours italique~Un titre enorme~L'absence de marges", 0,
     "Un contraste minimal entre texte et fond est necessaire, notamment selon les recommandations WCAG."),
 QC("Pourquoi verifier la maquette sur le support final ?", "Pour changer le titre~Parce que l'ecran et le papier ne restituent pas identiquement~Pour supprimer les images~Pour ajouter des pages", 1,
     "Les modes de restitution different : il faut controler le resultat reel avant diffusion."),
 QT("Construire une hierarchie typographique simple pour une page de rapport de projet.",
    "On definit quatre niveaux : le titre principal, les titres de parties, le corps de texte et les legendes. On choisit une famille pour les titres et une pour le corps, en fixant une echelle par exemple 24, 16, 11 et 9 points. Le titre principal se distingue par la taille et la graisse, les titres de parties par la graisse et un espacement avant, le corps par un interlignage confortable, et les legendes par une taille reduite et une couleur plus discretes mais suffisamment contrastees. On aligne tous les elements sur une grille de ligne unique et on verifie que l'oeil descend naturellement du titre vers le corps. Une relecture en impression et sur ecran complete la verification.",
    "On attend quatre niveaux distincts, une echelle coherente et une verification finale."),
 QT("Quels problemes surviennent quand une maquette utilise trop de styles typographiques ?",
    " Trop de styles rendent la page bruyante : l'oeil ne sait plus ou se poser et la hierarchie devient ambigue. Les niveaux se confondent, les alignements deviennent incoherents et le lecteur doit fournir un effort pour reconstruire l'ordre du texte. Cela affaiblit aussi l'identite du document, qui parait assemble plutot que concu. La correction consiste a reduire le nombre de familles, a fixer une echelle de tailles et a n'utiliser la graisse ou l'italique que pour des fonctions precises. On documente ensuite ces regles dans une charte pour les appliquer a toutes les pages. La simplicite n'appauvrit pas le message : elle le rend plus audible.",
    "On attend l'analyse des effets sur la lecture et une methode de simplification.")],
C("La hierarchie typographique rend le texte navigable : niveaux, echelle, contraste et grille guident le regard.",
  "Titre > sous-titre > corps > legende > notes",
  "echelle de tailles · deux familles · grille de ligne · contraste · accessibilite",
  "Titre~Niveau le plus fort~Corps~Texte courant~Legende~Annotation discre~Echelle~Rapport entre tailles",
  "Degager les niveaux d'information|Choisir une echelle de tailles|Limiter les familles et les styles|Aligner sur la grille de ligne|Verifier lisibilite et contraste final",
  "Utiliser une police differente par paragraphe|Confondre legende et titre|Negliger le contraste|Verifier uniquement sur ecran",
  "24 pt~Titre principal~16 pt~Titre de partie~11 pt~Corps~9 pt~Legende~Grille~Alignement vertical",
  "Hierarchie~Ordre de lecture~Decor~Effet sans fonction",
  "Ecran~Restitution numerique~Papier~Restitution imprimee"))

# ============================================================ TP03
add("TP03", "Couleur : roue, complementarite et harmonies", "Typographie et couleur", T,
S("La couleur est une perception liee a la lumiere et a l'oeil."
  "|On decrit une couleur par sa teinte, sa saturation et sa luminosite."
  "|La roue chromatique classique des artistes organise les teintes autour de trois couleurs primaires."
  "|Les couleurs secondaires resultent du melange de deux couleurs primaires."
  "|Deux couleurs opposees sur la roue sont dites complementaires."
  "|Le melange additif concerne la lumiere et les ecrans, avec le rouge, le vert et le bleu."
  "|Le melange soustractif concerne les encres d'impression, avec le cyan, le magenta, le jaune et le noir."
  "|Une harmonie monochrome utilise une seule teinte declinee en valeurs."
  "|Une harmonie analogue associe des teintes voisines sur la roue."
  "|Une harmonie triadique utilise trois teintes regulierement espacees."
  "|La temperature d'une couleur, chaude ou froide, modifie la sensation de la composition."
  "|Les associations culturelles des couleurs doivent etre verifiees selon le public vise."),
[QC("Quels sont les trois parametres d'une couleur ?", "Longueur, largeur, hauteur~Teinte, saturation, luminosite~Chaud, froid, neutre~Rouge, vert, bleu", 1,
     "Une couleur se decrit par sa teinte, sa saturation et sa luminosite."),
 QC("Que sont les couleurs complementaires ?", "Deux teintes voisines~Deux teintes opposees sur la roue~Trois teintes espacees~Une seule teinte", 1,
     "Les couleurs complementaires se situent a l'oppose sur la roue chromatique."),
 QC("Quel melange concerne les ecrans ?", "Le melange soustractif~Le melange additif~Le melange par contact~Le melange par absorption", 1,
     "Les ecrans fonctionnent en additif avec le rouge, le vert et le bleu."),
 QC("Quelles encres utilise l'impression courante ?", "RVB~CMJN~Rouge et bleu seulement~Noir et blanc", 1,
     "L'impression utilise cyan, magenta, jaune et noir, soit CMJN."),
 QC("Qu'est-ce qu'une harmonie monochrome ?", "Une seule teinte en valeurs differentes~Deux teintes opposees~Trois teintes espacées~Toutes les teintes", 0,
     "Le monochrome decline une seule teinte par la valeur et la saturation."),
 QC("Quelle harmonie associe des teintes voisines ?", "Complementaire~Analogue~Triadique~Monochrome", 1,
     "L'harmonie analogue utilise des teintes contigues sur la roue."),
 QC("Quel risque presente une association de couleurs non verifiee ?", "Un cout plus eleve~Un contresens culturel~Une impression plus rapide~Aucun risque", 1,
     "Les significations attribuees aux couleurs varient selon les cultures et les contextes."),
 QT("Expliquer la difference entre melange additif et melange soustractif.",
    "Le melange additif additionne des lumieres colorees : plus on ajoute de composantes rouge, vert et bleu, plus le resultat est clair, et leur somme donne du blanc. C'est le principe des ecrans et de la projection. Le melange soustractif, lui, superpose des encres ou des filtres qui absorbent une partie de la lumiere : les encres cyan, magenta et jaune donnent progressivement du sombre, et leur superposition idealisee donne du noir, remplace en pratique par le noir d'impression. C'est le principe de l'impression et de la peinture. Comprendre cette distinction evite les mauvaises surprises entre une maquette ecran et son impression.",
    "On attend l'opposition entre addition de lumieres et absorption par des encres, avec les deux triplets de couleurs."),
 QT("Comment construire une palette harmonieuse pour une identite de marque ?",
    "On part du message et des valeurs de la marque, puis on choisit une dominante colorimetrique. On construit l'harmonie selon une regle simple : monochrome pour la sobriete, analogue pour la douceur, complementaire pour le contraste, triadique pour la vivacite. On decline ensuite cette palette en valeurs et en saturations pour obtenir des fonds, des accents et des textes lisibles. On verifie les contrasts avec le fond, y compris pour les plus petits elements, et on teste en noir et blanc pour s'assurer que la hierarchie ne depend pas uniquement de la teinte. Enfin, on controle le rendu sur ecran et sur papier, car les modes de restitution different.",
    "On attend une regle d'harmonie, des declinaisons et des verifications de contraste.")],
C("La couleur se construit sur une roue : teinte, saturation et valeur permettent de former des harmonies adaptees au message.",
  "Additif RVB (ecrans) · Soustractif CMJN (impression)",
  "complementaire · analogue · monochrome · triadique · temperature",
  "Teinte~Famille de couleur~Saturation~Intensite~Luminosite~Clarte~Roue~Cercle chromatique~Complementaire~Opposition",
  "Definir le message et l'ambiance|Choisir une regle d'harmonie|Decliner la palette en valeurs|Tester contrasts et noir et blanc|Verifier ecran et impression",
  "Choisir les couleurs au hasard|Confondre RVB et CMJN|Ignorer le contexte culturel|Oublier le contraste des textes",
  "RVB~Ecrans et lumiere~CMJN~Encres et papier~Monochrome~Une teinte~Analogue~Teintes voisines~Complementaire~Contraste fort",
  "Additif~Lumiere qui s'ajoute~Soustractif~Encres qui absorbent",
  "Chaud~Presence et energie~Froid~Distance et calme"))

# ============================================================ TP04
add("TP04", "Couleur et perception : contraste, lumiere et nuance", "Typographie et couleur", T,
S("La couleur percue depend de la lumiere qui eclaire l'objet et de son environnement."
  "|Une surface absorbe certaines longueurs d'onde et en reflechit d'autres."
  "|La lumiere incidente et la lumiere reflechie ne donnent pas la meme apparence."
  "|Le contraste simultane designe l'influence d'une couleur sur la couleur voisine."
  "|Deux couleurs complementaires placees cote a cote s'intensifient mutuellement."
  "|La valeur, ou luminosite, suffit a rendre une image lisible en noir et blanc."
  "|La perspective atmospherique attenue les couleurs et les contrastes avec la distance."
  "|La finition d'un materiau, matte ou brillante, modifie la perception de la couleur."
  "|La metamerie designe deux couleurs identiques sous une lumiere et differentes sous une autre."
  "|La perception des couleurs varie selon les individus, notamment en cas de daltonisme."
  "|Les recommandations WCAG imposent un contraste minimal pour les textes."
  "|Les profils colorimetriques et les epreuves controlent la reproduction ecran-imprimerie."),
[QC("De quoi depend la couleur percue d'une surface ?", "De son seul nom~De la lumiere et de ce que la surface reflechit~De sa taille~De son prix", 1,
     "La perception depend de l'eclairage et des longueurs d'onde reflechies."),
 QC("Qu'est-ce que le contraste simultane ?", "Un contraste dans le temps~L'influence d'une couleur sur sa voisine~Un contraste de prix~Une comparaison de tailles", 1,
     "Le contraste simultane decrit l'effet d'une couleur sur celle qui l'entoure."),
 QC("Que permet la valeur en noir et blanc ?", "De changer la teinte~De verifier la lisibilite de l'image~De supprimer les ombres~D'augmenter la saturation", 1,
     "Une image dont les valeurs sont bien hierarchisees reste lisible sans couleur."),
 QC("Quel effet a la perspective atmospherique ?", "Elle augmente les contrastes au loin~Elle attenue couleurs et contrastes avec la distance~Elle supprime le ciel~Elle change la teinte du premier plan", 1,
     "Les elements lointains paraissent plus clairs, plus desatures et moins contrastes."),
 QC("Qu'appelle-t-on metamerie ?", "Une couleur unique~Deux couleurs egales sous une lumiere mais differentes sous une autre~Un defaut d'impression~Une harmonie de teintes", 1,
     "La metamerie depend du spectre de la source lumineuse."),
 QC("Quelle recommandation concerne le contraste des textes ?", "Le contraste doit etre minimal~Les WCAG imposent un ratio minimal de contraste~Le texte doit toujours etre blanc~Le fond doit etre colore", 1,
     "Les WCAG fixent notamment un ratio de 4,5:1 pour le texte courant."),
 QC("A quoi servent les profils colorimetriques ?", "A accelerer l'impression~A controler la reproduction des couleurs entre ecran et papier~A changer la police~A agrandir le fichier", 1,
     "Ils servent a gerer la conversion et la fidélite des couleurs selon le peripherique."),
 QT("Expliquer pourquoi deux couleurs peuvent paraitre identiques en atelier et differentes en magasin.",
    "C'est le phenomene de metamerie : deux surfaces peuvent reflechir des spectres differents tout en produisant la meme sensation sous une source lumineuse donnee, par exemple la lumiere naturelle de l'atelier. Sous un eclairage commercial aux composantes differentes, ces memes surfaces ne renvoient pas les memes longueurs d'onde et leurs couleurs divergent. Le phenomene est accentue par la finition : une surface brillante reflechit davantage la source, ce qui modifie encore l'apparence. Pour limiter ce risque, on valide les couleurs sous plusieurs eclairages et on utilise des echantillons physiques plutôt que le seul ecran. Dans une identite de marque, cette verification evite des ecarts visibles entre les supports.",
    "On attend la definition de metamerie, le role de la source et la solution de validation."),
 QT("Comment verifier la lisibilite d'une image en tenant compte du daltonisme ?",
    "On commence par convertir l'image en niveaux de gris : si les elements importants se confondent, la distinction reposait uniquement sur la teinte. On ajoute alors des differences de valeur, de forme, de motif ou de taille pour porter l'information. On controle les ratios de contraste des textes avec leur fond, notamment pour les petits corps, en visant les seuils recommandes. On utilise ensuite un simulateur de vision pour plusieurs types de daltonisme et on demande un avis a des personnes concernees. Enfin, on evite les couples problematiques comme rouge-vert sur une meme information. Cette demarche ameliore la lisibilite pour tous, pas seulement pour les personnes concernees.",
    "On attend conversion en gris, indices multiples, ratios de contraste et validation.")],
C("La couleur est une perception : lumiere, voisinage, valeur et individus modifient ce que l'on voit vraiment.",
  "Couleur percue = lumiere + surface + contexte + oeil",
  "contraste simultane · metamerie · valeur · WCAG · profils colorimetriques",
  "Lumiere~Source d'eclairage~Reflexion~Longueurs d'onde~Contraste simultane~Influence du voisinage~Valeur~Lisibilite en gris",
  "Observer sous plusieurs eclairages|Verifier la valeur en noir et blanc|Tester les contrasts et les textes|Simuler les troubles de la vision|Valider sur echantillons physiques",
  "Juger une couleur uniquement sur ecran|Confondre teinte et valeur|Ignorer les troubles de la vision|Oublier la finition du materiau",
  "Metamerie~Couleur dependante de la lumiere~WCAG~Ratio 4,5:1~Mat~Surface diffuse~Brillant~Surface reflechissante~Epreuve~Controle final",
  "Valeur~Clarte d'une couleur~Teinte~Famille chromatique",
  "Mat~Reflexion diffuse~Brillant~Reflexion speculaire"))

valider_et_ecrire(F, "std2a-mat-part-B.json")
