# -*- coding: utf-8 -*-
"""Generateur pro-gestion-mat-part-C.json — lot C : pratique et environnement (20 fiches).

Pratique professionnelle bureautique et gestion (7), Français professionnel (4),
Langues (4), Environnement professionnel (5).
12 points, 9 questions corrigees (7 QCM + 2 texte), 7 blocs ordonnes, 3 SVG.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _progestion_common import S, R, QC, QT, C, build, valider_et_ecrire

F = []


def add(prefix, titre, mat, ans, points, questions, c):
    F.append(build(prefix, titre, mat, ans, points, questions, c))


# ============================================================ PP1
add("PP1", "Le tableur : formules, références et fonctions", "Pratique professionnelle bureautique et gestion", ["1re pro", "Terminale pro"],
S("Un tableur organise des données en lignes et en colonnes : chaque cellule est repérée par une adresse comme B4."
  "|Une formule commence toujours par le signe égal et peut combiner des valeurs, des opérateurs, des références et des fonctions."
  "|Une référence relative, comme A1, s'ajuste automatiquement lorsqu'on copie la formule vers une autre cellule."
  "|Une référence absolue, notée $A$1, reste fixe lors de la copie : elle est utile pour un taux ou une constante."
  "|Une référence mixte, comme $A1 ou A$1, bloque seulement la colonne ou seulement la ligne."
  "|La fonction SOMME additionne une plage de cellules, par exemple =SOMME(B2:B12)."
  "|La fonction MOYENNE calcule la moyenne arithmétique des valeurs d'une plage."
  "|Les fonctions SI permettent de tester une condition : =SI(B2>=100;\"OK\";\"A contrôler\")."
  "|NB.SI compte les cellules qui répondent à un critère et SOMME.SI additionne selon un critère."
  "|Le format de cellule distingue le texte, le nombre, la date, la devise et le pourcentage sans modifier la valeur."
  "|Un graphique doit être construit à partir d'une plage claire, avec un titre, des axes légendés et une source indiquée."
  "|Avant de diffuser un fichier, on vérifie les formules sur quelques lignes tests, les arrondis et la protection des cellules sensibles."),
[QC("Par quel signe commence une formule de tableur ?", "Le signe plus~Le signe égal~Le signe dollar~Le deux-points", 1,
     "Toute formule débute par = ; le dollar sert aux références absolues."),
 QC("Que se passe-t-il quand on copie une référence relative ?", "Elle reste identique~Elle s'ajuste selon le déplacement~Elle devient une constante~Elle est supprimée", 1,
     "Une référence relative suit le déplacement de la formule."),
 QC("Comment écrit-on une référence absolue sur la cellule A1 ?", "A1~$A$1~A$1~[A1]", 1,
     "Les deux signes dollar bloquent la colonne et la ligne."),
 QC("Que fait la fonction =SOMME(B2:B8) ?", "Elle compte les cellules~Elle additionne les valeurs de B2 à B8~Elle calcule la moyenne~Elle trie la colonne", 1,
     "SOMME additionne toutes les valeurs de la plage indiquée."),
 QC("Quel résultat donne =SI(C4>=10;\"Oui\";\"Non\") si C4 vaut 8 ?", "Oui~Non~8~Erreur", 1,
     "La condition 8 >= 10 est fausse, donc la valeur « Non » est renvoyée."),
 QC("Quelle fonction compte les cellules respectant un critère ?", "MOYENNE~NB.SI~SOMME~ARRONDI", 1,
     "NB.SI compte les cellules qui satisfont le critère ; SOMME.SI les additionne."),
 QC("Pourquoi vérifier les formules avant diffusion ?", "Pour changer les couleurs~Pour détecter les erreurs de référence et d'arrondi~Pour agrandir la police~Pour ajouter des lignes", 1,
     "Une copie de formule ou un arrondi mal placé peut fausser tout un calcul."),
 QT("Dans un tableur, la cellule B2 contient le prix HT et C2 contient =B2*1,2. Que se passe-t-il si l'on copie C2 en C3, puis que l'on veut appliquer un taux fixe de 20 % situé en E1 ?",
     "La copie de C2 en C3 donne automatiquement =B3*1,2 car la référence B2 est relative : elle s'adapte à la nouvelle ligne. Cependant, le taux 20 % est écrit en dur dans la formule, ce qui oblige à modifier toutes les formules si le taux change. Il faut placer le taux dans la cellule E1 et écrire en C2 =B2*(1+$E$1). La référence $E$1 est absolue : lors de la copie vers C3, elle restera E1, tandis que B2 deviendra B3. La formule copiée en C3 sera donc =B3*(1+$E$1).",
     "On explique l'ajustement relatif, le problème du taux en dur et l'usage de $E$1."),
 QT("Décrire la démarche pour produire un tableau de bord fiable avec un tableur.",
     "On commence par structurer les données sources en tableau, avec une ligne d'en-tête, des types cohérents et aucune cellule vide au milieu. On crée ensuite des calculs contrôlés avec des formules simples et des références absolues pour les paramètres. On construit les indicateurs synthétiques, par exemple total, moyenne, écart et pourcentage, puis on les présente avec des graphiques légendés. On vérifie la cohérence des résultats par des contrôles croisés, comme la somme des parties égale le total. Enfin, on protège les cellules de paramètres, on documente la source et la date d'actualisation, et on teste le fichier avec quelques valeurs extrêmes avant de le diffuser.",
     "On attend structure des données, formules contrôlées, indicateurs, graphiques, vérifications et documentation.")],
C("Le tableur calcule à partir de références : la copie des formules et le choix des références déterminent la fiabilité des résultats.",
  "Formule = = + opérandes · référence absolue = $A$1",
  "SOMME · MOYENNE · NB.SI · SOMME.SI · SI",
  "Cellule~Adresse comme B4~Reference relative~S'ajuste a la copie~Reference absolue~Reste fixe~Formule~Commence par egal~Fonction~Calcul predefini",
  "Structurer les données|Écrire la première formule|Tester sur une ligne|Copier avec les références adaptées|Vérifier et documenter",
  "Oublier le signe égal|Copier une référence absolue à la place d'une relative|Écrire un taux en dur|Ne pas vérifier les arrondis",
  "B2*1,2~Copie en B3*1,2~$E$1~Taux fixe~NB.SI~Comptage selon critere~SI~Test de condition",
  "Reference relative~S'ajuste~Reference absolue~Reste fixe",
  "SOMME~Additionne~MOYENNE~Calcule la moyenne"))

# ============================================================ PP2
add("PP2", "Le traitement de texte et la mise en page d'un document", "Pratique professionnelle bureautique et gestion", ["1re pro"],
S("Un traitement de texte permet de saisir, modifier, mettre en forme et imprimer un document écrit."
  "|Les styles appliquent d'un seul geste un ensemble de caractéristiques : police, taille, couleur, espacement."
  "|Les styles de titre hiérarchisent le document et permettent de générer automatiquement une table des matières."
  "|La mise en page définit le format du papier, les marges, l'orientation, les en-têtes et les pieds de page."
  "|Les colonnes, les tableaux et les zones de texte organisent l'information et facilitent la lecture."
  "|Les listes à puces ou numérotées rendent visibles les énumérations et les étapes d'une procédure."
  "|Un saut de page maîtrisé évite qu'un titre se retrouve isolé en bas de page ou qu'un tableau soit coupé."
  "|Les notes de bas de page et les références croisées renvoient à une source ou à une autre partie du document."
  "|La syntaxe des paragraphes impose une hiérarchie claire : un titre principal, des sous-titres, puis des paragraphes courts."
  "|La police doit rester lisible, avec une taille adaptée au support imprimé ou numérique et un contraste suffisant."
  "|Le correcteur orthographique et grammatical aide à la relecture mais ne remplace pas une vérification attentive."
  "|Avant envoi, on vérifie la numérotation des pages, les légendes, les noms propres et l'éventuelle présence de commentaires masqués."),
[QC("Quel outil génère automatiquement une table des matières ?", "La police~Les styles de titre~Le correcteur~Les marges", 1,
     "La table des matières s'appuie sur les niveaux de titres définis par les styles."),
 QC("Que définit la mise en page ?", "Le contenu des paragraphes~Le format papier, les marges et les en-têtes~La grammaire~Les références bibliographiques", 1,
     "La mise en page concerne la présentation générale du document."),
 QC("Quel est l'intérêt d'un style ?", "Changer le sens d'un mot~Appliquer une mise en forme cohérente en une seule action~Supprimer les fautes~Créer un graphique", 1,
     "Le style regroupe des attributs de mise en forme réutilisables."),
 QC("Comment éviter qu'un tableau soit coupé entre deux pages ?", "En reducing la police~En choisissant l'option « ne pas couper » ou un saut de page~En supprimant les marges~En changeant de logiciel", 1,
     "Les options de paragraphe et de tableau permettent de contrôler les coupures."),
 QC("Quel élément figure généralement dans un pied de page ?", "Le titre du chapitre~La numérotation des pages~La table des matières~Les commentaires", 1,
     "Le pied de page contient souvent le numéro de page et parfois le nom du document."),
 QC("Que faut-il vérifier avant l'envoi d'un document ?", "Uniquement la première page~Les noms, les numéros et les commentaires éventuels~La couverture seulement~Le nombre de mots", 1,
     "Les détails et les commentaires masqués sont des sources d'erreur fréquentes."),
 QC("Pourquoi privilégier des paragraphes courts ?", "Pour occuper plus de pages~Pour améliorer la lisibilité~Pour réduire le nombre de styles~Pour supprimer les marges", 1,
     "Un paragraphe court et une idée par paragraphe facilitent la lecture."),
 QT("Expliquer la démarche pour mettre en forme un rapport de dix pages de façon cohérente.",
     "On définit d'abord la mise en page : format A4, marges, interlignage, en-tête avec le nom de l'organisation et pied de page numéroté. On crée ensuite une feuille de style avec un titre principal, des titres de niveau 2 et 3, un style pour le corps du texte et un style pour les citations. On applique ces styles à tous les paragraphes plutôt que de mettre en forme manuellement. Les tableaux reçoivent des légendes numérotées et les figures des titres cohérents. On insère la table des matières générée automatiquement, puis on relit le document pour vérifier les coupures, les renvois et la présence de commentaires. Un dernier contrôle porte sur l'orthographe des noms propres.",
     "On attend mise en page, styles hiérarchiques, légendes, table des matières et relecture finale."),
 QT("Pourquoi le correcteur orthographique ne suffit-il pas à garantir la qualité d'un document professionnel ?",
     "Le correcteur repère les écarts par rapport à un dictionnaire et à quelques règles grammaticales, mais il ne comprend pas le sens. Il ne détecte pas un mot juste orthographié mais inappropriate, comme « a » à la place de « à » dans certains contextes, ni une phrase ambiguë, ni une information obsolète. Il peut aussi proposer une correction qui change le sens voulu ou méconnaître un nom propre, une marque ou un acronyme métier. La relecture humaine porte sur la cohérence du fond, la justesse des chiffres, l'adéquation au destinataire et la clarté de la structure. Le correcteur est donc un outil d'aide, non une garantie de qualité.",
     "On oppose détection mécanique et compréhension du sens, avec des exemples et la relecture humaine.")],
C("Un document professionnel est suspendu à une mise en page claire et à des styles cohérents, pas à des mises en forme manuelles.",
  "Styles de titre → table des matières automatique",
  "Mise en page : format, marges, en-tête, pied de page",
  "Style~Mise en forme reutilisable~Titre~Niveau hierarchique~Mise en page~Format et marges~Pied de page~Numerotation~Legende~Titre d'un tableau",
  "Définir la mise en page|Créer les styles|Rédiger avec les styles|Insérer légendes et table des matières|Relire et nettoyer",
  "Mettre en forme manuellement chaque paragraphe|Oublier les noms propres|Laisser des commentaires|Négliger les coupures de page",
  "Styles de titre~Table automatique~A4 et marges~Mise en page~Pied de page~Numerotation~Legendes~Tableaux identifies",
  "Style~Coherence automatique~Mise en forme manuelle~Risque d'incoherence",
  "En-tete~Haut de page~Pied de page~Bas de page"))

# ============================================================ PP3
add("PP3", "Les diaporamas et la présentation orale", "Pratique professionnelle bureautique et gestion", ["1re pro", "Terminale pro"],
S("Un diaporama est une suite de diapositives destinées à accompagner une présentation orale, pas à la remplacer."
  "|Chaque diapositive doit porter un message principal identifiable en quelques secondes, avec un titre court."
  "|La règle de la charge cognitive recommande peu de texte, des phrases courtes et une hiérarchie visuelle nette."
  "|Un contraste suffisant entre le texte et le fond est indispensable à la lisibilité, sur écran comme sur vidéoprojecteur."
  "|Les polices doivent rester lisibles de loin : une taille minimale d'environ 18 à 24 points pour le corps du texte."
  "|Les couleurs doivent être limitées et cohérentes avec la charte graphique de l'organisation."
  "|Les images, schémas et graphiques appuient le propos : ils doivent être légendés et exempts de distortion."
  "|Les transitions et animations attire l'attention mais ne doivent pas parasite le message."
  "|La structure suit généralement introduction, problématique, parties, synthèse et conclusion avec une diapositive de questions."
  "|Les notes du présentateur permettent de conserver les détails sans surcharger les diapositives."
  "|La présentation orale s'appuie sur un fil conducteur, des connecteurs et un rythme adapté au temps imparti."
  "|Une répétition chronométrée permet de vérifier la durée, la prononciation des termes techniques et la coordination avec le support."),
[QC("Quel est le rôle principal d'un diaporama ?", "Remplacer totalement le discours~Accompagner et illustrer la présentation orale~Rédiger le rapport~Remplacer les notes", 1,
     "Le support visuel appuie le message, il ne se substitue pas à l'oral."),
 QC("Combien d'idée(s) principales faut-il privilégier par diapositive ?", "Une seule~Cinq~Autant que possible~Aucune", 0,
     "Une idée forte par diapositive améliore la compréhension."),
 QC("Quelle taille de police est généralement recommandée pour le corps ?", "8 points~12 points~18 à 24 points~48 points", 2,
     "Une police trop petite devient illisible à distance."),
 QC("À quoi servent les notes du présentateur ?", "À remplacer les diapositives~À garder les détails sans surcharger l'écran~À animer les transitions~À trier les images", 1,
     "Elles restent visibles pour l'orateur seulement."),
 QC("Que faut-il éviter avec les animations ?", "Toute animation~Les animations excessives qui distraient~Les titres~Les légendes", 1,
     "Quelques animations utiles suffisent ; le message reste prioritaire."),
 QC("Quelle structure suit souvent une présentation ?", "Conclusion, parties, introduction~Introduction, problématique, parties, synthèse~Diapositives sans ordre~Une seule diapositive", 1,
     "On annonce le plan, développe, puis synthétise."),
 QC("Que vérifie une répétition chronométrée ?", "La couleur du fond~La durée, la prononciation et le rythme~Le nombre de diapositives seulement~La résolution de l'écran", 1,
     "Elle prépare la qualité de l'oral et le respect du temps."),
 QT("Une diapositive contient quinze lignes de texte en 12 points. Proposer une version améliorée et justifier.",
     "On identifie d'abord le message principal de la diapositive, puis on le reformule en un titre court. Le texte est réduit à trois ou quatre idées en phrases courtes, avec une taille d'au moins 18 points et des puces hiérarchisées. Les détails trop nombreux sont déplacés dans les notes du présentateur ou dans une diapositive complémentaire. On ajoute un schéma ou une image légendée si elle illustre réellement le propos, et on vérifie le contraste avec le fond. Le résultat est une diapositive lisible en quelques secondes, qui laisse l'oral apporter les explications détaillées.",
     "On attend réduction du texte, titre fort, police agrandie, hiérarchie visuelle et déplacement des détails."),
 QT("Expliquer comment adapter une présentation à un public de clients plutôt qu'à un public interne.",
     "Pour un public de clients, on part de leurs besoins et de ce qu'ils attendent de la solution : les exemples concrets, les bénéfices et les preuves priment sur les détails techniques. Le vocabulaire est simplifié ou expliqué, et la durée est souvent plus courte. On soigne particulièrement la première diapositive, qui doit capter l'attention, et la dernière, qui rappelle l'action attendue. Pour un public interne, on peut approfondir les méthodes, les chiffres et les contraintes, utiliser le jargon métier et prévoir un temps d'échange plus long. Dans les deux cas, le plan reste clair et le support reste au service du message.",
     "On oppose bénéfices et preuves pour les clients, technicité pour les internes, avec un plan clair dans les deux cas.")],
C("Une bonne diapositive se lit vite : une idée, un titre, peu de texte, et un support au service de l'oral.",
  "Une diapositive = un message principal",
  "Lisibilité : contraste, police 18-24 pts, peu de texte",
  "Diapositive~Message unique~Contraste~Lisibilite du texte~Police~Taille minimale~Notes~Details pour l'orateur~Transition~Effet de passage",
  "Définir le message de chaque diapositive|Choisir un titre court|Réduire le texte|Ajouter un visuel légendé|Répéter à voix haute",
  "Copier un document entier sur une diapositive|Utiliser des polices minuscules|Multiplier les animations|Lire les diapositives sans regarder le public",
  "15 lignes en 12 points~A reduire~3 idees~Taille 18-24~Notes~Details caches~Repetition chronometree~Respect du temps",
  "Public client~Benedices et preuves~Public interne~Methodes et chiffres",
  "Diaporama~Support visuel~Presentation orale~Message principal"))

# ============================================================ PP4
add("PP4", "Les bases de données et les requêtes", "Pratique professionnelle bureautique et gestion", ["1re pro", "Terminale pro"],
S("Une base de données organise des informations structurées afin de les stocker, les interroger et les mettre à jour efficacement."
  "|Le modèle relationnel représente les données sous forme de tables, aussi appelées relations."
  "|Une table est composée de colonnes, nommées champs ou attributs, et de lignes, nommées enregistrements."
  "|La clé primaire est un champ, ou une combinaison de champs, qui identifie de façon unique chaque enregistrement."
  "|Une clé étrangère est un champ qui référence la clé primaire d'une autre table et crée un lien entre elles."
  "|Les types de données définissent la nature des valeurs : texte, entier, décimal, date, booléen."
  "|Une requête permet d'extraire, de filtrer, de trier ou de calculer des informations à partir d'une ou plusieurs tables."
  "|Le critère de sélection s'exprime avec des opérateurs comme =, <, >, ET, OU et IN."
  "|Une requête de jointure combine les enregistrements de deux tables à partir d'une clé commune."
  "|Une requête de regroupement calcule des totaux ou des moyennes par catégorie, avec des fonctions comme COUNT ou SUM."
  "|Un formulaire facilite la saisie et limite les erreurs grâce à des contrôles, des listes déroulantes et des messages d'aide."
  "|L'intégrité des données suppose d'éviter les doublons, de renseigner les champs obligatoires et de sauvegarder régulièrement la base."),
[QC("Qu'appelle-t-on clé primaire ?", "Un champ qui identifie uniquement chaque enregistrement~Le premier champ de la table~Un mot de passe~Le nom de la base", 0,
     "La clé primaire garantit l'unicité de chaque ligne."),
 QC("Quel est le rôle d'une clé étrangère ?", "Chiffrer la table~Référencer la clé primaire d'une autre table~Trier les données~Supprimer les doublons", 1,
     "Elle établit la relation entre deux tables."),
 QC("Que contient une table dans une base relationnelle ?", "Des diapositives~Des lignes et des colonnes~Des paragraphes~Des graphiques", 1,
     "Les lignes sont des enregistrements et les colonnes des champs."),
 QC("Quel opérateur combine deux conditions qui doivent toutes deux être vraies ?", "OU~ET~NON~IN", 1,
     "ET exige la simultanéité des deux conditions."),
 QC("Que fait une requête de jointure ?", "Elle supprime des lignes~Elle combine des tables via une clé commune~Elle change le type d'un champ~Elle crée un formulaire", 1,
     "La jointure associe les enregistrements correspondants de deux tables."),
 QC("Quelle fonction compte le nombre d'enregistrements ?", "SUM~COUNT~MAX~ROUND", 1,
     "COUNT compte les lignes ; SUM additionne les valeurs."),
 QC("Pourquoi utiliser un formulaire de saisie ?", "Pour compliquer la tâche~Pour limiter les erreurs et guider l'utilisateur~Pour supprimer les requêtes~Pour créer des doublons", 1,
     "Les contrôles de saisie améliorent la qualité des données."),
 QT("Une table CLIENTS contient un champ CodeClient en clé primaire et une table COMMANDES contient CodeClient. Expliquer comment obtenir la liste des commandes avec le nom des clients.",
     "On crée une requête qui combine les deux tables sur le champ commun CodeClient : c'est une jointure. La table CLIENTS fournit le nom du client et la table COMMANDES fournit la date, le montant et le numéro de commande. La condition de jointure s'écrit CLIENTS.CodeClient = COMMANDES.CodeClient. On sélectionne seulement les champs utiles, on trie par date décroissante, puis on exécute la requête. Si un client n'a pas de commande, il n'apparaîtra pas dans une jointure interne ; une jointure externe permettrait de le conserver. La clé primaire garantit que chaque client n'est représenté qu'une fois.",
     "On décrit la jointure sur CodeClient, le choix des champs, le tri et la différence avec une jointure externe."),
 QT("Expliquer la différence entre une requête de sélection et une requête de regroupement, et donner un exemple de chacune.",
     "Une requête de sélection filtre et affiche des enregistrements sans modifier leur nombre : par exemple, afficher les produits dont le prix est supérieur à 50 €. Une requête de regroupement agrège les données pour produire des lignes synthétiques : par exemple, calculer le chiffre d'affaires total par catégorie de produits avec SUM et un regroupement sur la catégorie. La première répond à « quelles lignes ? », la seconde à « combien ou combien par groupe ? ». Les deux peuvent être combinées : on filtre d'abord les lignes, puis on regroupe le résultat. Leur correctitude repose sur des types de champs cohérents et sur des critères explicités.",
     "On oppose lignes détaillées et synthèse agrégée, avec un exemple et des fonctions adaptées.")],
C("Une base de données relationnelle relie des tables par des clés ; les requêtes transforment les données en information.",
  "Clé primaire : identifiant unique · clé étrangère : lien entre tables",
  "Sélection · tri · jointure · regroupement (COUNT, SUM)",
  "Table~Lignes et colonnes~Cle primaire~Identifiant unique~Cle etrangere~Lien entre tables~Requete~Extraire et filtrer~Jointure~Clé commune~Formulaire~Saisie guidée",
  "Repérer les entités et leurs champs|Définir les clés|Créer les relations|Écrire la requête|Contrôler les résultats",
  "Oublier la clé primaire|Confondre clé primaire et étrangère|Multiplier les doublons de saisie|Négliger les types de champs",
  "CLIENTS.CodeClient~Cle primaire~COMMANDES.CodeClient~Cle etrangere~Jointure~Nom et date~COUNT~Nombre de lignes~SUM~Total par categorie",
  "Requete de selection~Lignes detaillees~Requete de regroupement~Synthese agrégée",
  "Cle primaire~Unique dans sa table~Cle etrangere~Reference vers une autre table"))

# ============================================================ PP5
add("PP5", "La messagerie, l'agenda et la gestion du temps", "Pratique professionnelle bureautique et gestion", ["1re pro", "Terminale pro"],
S("La messagerie électronique est le canal de communication écrit dominant dans l'entreprise : elle laisse une trace et permet le classement."
  "|Un objet précis, court et éventuellement préfixé d'une référence, permet de retrouver et de classer un message."
  "|Une boîte de réception saturée doit être traitée par priorité : urgent et important, important non urgent, déléguable, supprimable."
  "|La règle des deux minutes recommande de traiter immédiatement toute tâche qui demande moins de deux minutes."
  "|Les dossiers, dossiers intelligents et étiquettes remplacent le désordre de la boîte de réception par un classement stable."
  "|Les règles de filtrage dirigent automatiquement les messages vers un dossier selon l'expéditeur ou des mots-clés."
  "|L'agenda partagé permet de visualiser les disponibilités, de planifier des réunions et d'éviter les conflits de rendez-vous."
  "|Une invitation de réunion doit préciser l'objet, la date, la durée, les participants, le lieu ou le lien et l'ordre du jour."
  "|Les rappels et les notifications aident à respecter les échéances, à condition de ne pas devenir une source de distraction."
  "|Le temps peut être découpé en blocs dédiés à une activité, avec des plages de concentration sans interruption."
  "|La matrice urgence/importance distingue quatre quadrants : faire, planifier, déléguer et éliminer."
  "|Une bonne gestion du temps comporte un bilan régulier des tâches accompli et une replanification réaliste des charges."),
[QC("Quel critère permet de classer rapidement un e-mail reçu ?", "La couleur du message~L'objet et l'expéditeur~La taille de la pièce jointe~L'heure d'envoi seulement", 1,
     "L'objet explicite et l'expéditeur sont les premiers repères de tri."),
 QC("Que recommande la règle des deux minutes ?", "De supprimer tous les messages~De traiter immédiatement une tâche de moins de deux minutes~De reporter systématiquement~De déléguer sans lire", 1,
     "Un traitement immédiat évite d'accumuler de petites tâches."),
 QC("Quel outil classe automatiquement les messages entrants ?", "Le filigrane~Les règles de filtrage~Le correcteur~La signature", 1,
     "Une règle dirige un message vers un dossier selon des critères définis."),
 QC("Que doit préciser une invitation de réunion ?", "Seulement l'heure~Objet, date, durée, participants et ordre du jour~Le nom du bureau~La couleur de l'agenda", 1,
     "Ces éléments permettent aux participants de se préparer et d'être disponibles."),
 QC("Quel est l'intérêt d'un agenda partagé ?", "Remplacer les e-mails~Visualiser les disponibilités et éviter les conflits~Stocker les fichiers~Calculer la TVA", 1,
     "Les calendriers partagés facilitent la planification collective."),
 QC("Dans la matrice urgence/importance, que faut-il faire d'une tâche urgente mais peu importante ?", "La planifier~La déléguer si possible~L'ignorer~La faire en dernier", 1,
     "Elle peut souvent être confiée ou traitée rapidement sans y consacrer un bloc long."),
 QC("Qu'est-ce qu'un bloc de concentration ?", "Une réunion~Une plage de temps réservée à une activité sans interruption~Une pause café~Un dossier d'archives", 1,
     "Regrouper les tâches similaires limite les coûts de changement de contexte."),
 QT("Un assistant de gestion reçoit chaque matin une cinquantaine de messages. Proposer une méthode de traitement efficace.",
     "Il commence par vider sa boîte par lots : il traite d'abord les messages urgents et importants, puis les tâches de moins de deux minutes, et il reporte ou délègue le reste. Il applique des règles de filtrage pour les newsletters et les notifications afin de les diriger vers un dossier séparé. Chaque message conservé reçoit un objet clair et est classé dans un dossier par projet ou par client. Les demandes qui nécessitent une action sont transformées en tâches datées dans l'agenda. En fin de journée, il parcourt les messages non lus restants et il programme un bilan hebdomadaire pour ajuster ses règles de tri et vérifier qu'aucune échéance n'a été manquée.",
     "On attend tri par priorité, règle des deux minutes, filtres, classement, tâches datées et bilan."),
 QT("Expliquer pourquoi les notifications permanentes nuisent à la gestion du temps et proposer des parades.",
     "Chaque notification interrompt le travail en cours et impose un coût de reconcentration : même une interruption courte peut faire perdre plusieurs minutes de flux. Les notifications créent aussi une réactivité apparente qui pousse à traiter les messages des autres avant ses propres priorités. Pour limiter cet effet, on désactive les alertes non essentielles, on regroupe la consultation de la messagerie en deux ou trois plages horaires, et on réserve des blocs de concentration sans interruption. On définit une procédure d'urgence pour les contacts réellement critiques, afin de ne pas sacrifier la planification à la peur de manquer une information.",
     "On explique le coût de l'interruption, puis on propose désactivation, plages de consultation et procédure d'urgence.")],
C("Gérer sa messagerie et son agenda, c'est transformer un flux d'informations en tâches datées et en priorités claires.",
  "Matrice urgence/importance : faire, planifier, déléguer, éliminer",
  "Règle des deux minutes · objets explicites · blocs de concentration",
  "Messagerie~Flux ecrit trace~Objet~Repere de classement~Filtre~Classement automatique~Agenda~Disponibilites et rendez-vous~Matrice~Priorisation des taches",
  "Trier par priorité|Traiter les tâches rapides|Classer et filtrer|Planifier dans l'agenda|Faire un bilan hebdomadaire",
  "Laisser les notifications actives|Empiler les messages non lus|Envoyer une réunion sans ordre du jour|Confondre urgent et important",
  "50 messages~Traiter par lots~Regle des 2 minutes~Taches immediates~Filtre~Newsletters isolees~Agenda partage~Conflits evites",
  "Urgent et important~A faire~Important non urgent~A planifier",
  "Notification~Interruption~Bloc de concentration~Plage protegee"))

# ============================================================ PP6
add("PP6", "Les outils collaboratifs et le travail en équipe", "Pratique professionnelle bureautique et gestion", ["1re pro", "Terminale pro"],
S("Le travail collaboratif associe plusieurs personnes à la production d'un document ou à la réalisation d'un projet."
  "|Les outils collaboratifs permettent de partager des fichiers, de co-éditer un document, de commenter et de suivre les versions."
  "|Le partage de fichiers s'appuie sur un espace commun en ligne, avec des droits de lecture, de commentaire ou de modification."
  "|La co-édition autorise plusieurs personnes à travailler simultanément sur un même document, avec un suivi des modifications."
  "|Le suivi des versions permet de revenir à un état antérieur et d'identifier qui a modifié quoi et quand."
  "|Les commentaires et les mentions facilitent la demande de validation sans multiplier les messages."
  "|Un espace de travail partagé organise les dossiers par projet, par client ou par étape du processus."
  "|La dénomination des fichiers doit être normée : date, projet, nature du document, version et responsable."
  "|Les réunions en visioconférence nécessitent un ordre du jour, un modérateur, une durée définie et un compte rendu."
  "|La synchronisation entre appareils expose à des risques de conflit si deux personnes modifient le même fichier hors ligne."
  "|Les accès doivent être révoqués lors d'un départ ou d'une fin de mission, conformément à la politique de sécurité."
  "|La collaboration efficace repose autant sur des règles convenues que sur les outils : qui valide, dans quel délai et sous quelle forme."),
[QC("Que permet la co-édition d'un document ?", "De le lire seulement~De modifier simultanément le même fichier à plusieurs~De l'imprimer à distance~De le chiffrer", 1,
     "Plusieurs contributeurs peuvent travailler en parallèle sur le même document."),
 QC("Quel intérêt présente le suivi des versions ?", "Réduire la taille du fichier~Revenir à un état antérieur et identifier les auteurs~Supprimer les commentaires~Changer le format", 1,
     "L'historique sécurise les modifications et facilite la reprise."),
 QC("Quels droits peut-on attribuer sur un fichier partagé ?", "Lecture, commentaire, modification~Impression seulement~Téléchargement seulement~Aucun droit", 0,
     "Les niveaux de droits courants sont lecture, commentaire et modification."),
 QC("Quelle convention de nommage est la plus utile ?", "Document1, Document2~Date, projet, nature, version, responsable~Des noms aléatoires~Le prénom seulement", 1,
     "Un nom normé rend les fichiers trouvables et évite les doublons."),
 QC("Quel élément prépare correctement une visioconférence ?", "Une réunion sans ordre du jour~Un ordre du jour, un modérateur et une durée~Un partage sans invitations~Une durée illimitée", 1,
     "Ces éléments structurent l'échange et permettent un compte rendu."),
 QC("Quel risque présente la synchronisation hors ligne ?", "Une meilleure sécurité~Un conflit de versions~Une baisse des coûts~Une disparition des commentaires", 1,
     "Deux modifications concurrentes peuvent créer des versions divergentes."),
 QC("Que faire lorsqu'un collaborateur quitte le projet ?", "Laisser ses accès~Révoquer ses accès et transférer ses fichiers~Supprimer tout le dossier~Changer le mot de passe général", 1,
     "La révocation des accès est une règle essentielle de sécurité."),
 QT("Une équipe de quatre personnes doit préparer un dossier de réponse à un appel d'offres en cinq jours. Organiser la collaboration.",
     "On crée d'abord un espace de travail commun avec une arborescence claire : pièces administratives, réponse technique, prix et synthèse. On nomme un responsable de dossier qui valide la version finale et on définit les droits de chaque membre. On établit un calendrier avec des échéances intermédiaires et un modèle de fichier unique, pour éviter les versions divergentes. Chacun travaille sur sa partie avec la co-édition, les commentaires servent aux demandes de précision et les mention désignent la personne concernée. Une courte réunion quotidienne fait le point sur les blocages. La veille de la remise, le responsable consolide les parties, vérifie les pièces et les noms de fichiers, puis archive la version définitive.",
     "On attend espace commun, responsable, droits, échéances, co-édition, points réguliers et version finale archivée."),
 QT("Expliquer pourquoi les règles d'équipe comptent autant que les outils dans la collaboration.",
     "Les outils offrent des possibilités techniques, mais ils ne décident pas de qui valide une modification, dans quel délai un commentaire doit être traité ou quelle version fait foi. Sans règles explicites, les contributeurs produisent des fichiers parallèles, les validations se perdent dans les messages et les conflits de versions apparaissent. Un accord simple sur la nomenclature des fichiers, les droits de modification, le circuit de validation et le délai de réponse réduit ces risques. La confiance se construit aussi par la traçabilité : l'historique des modifications permet de comprendre chaque décision. Les outils sont donc utiles à condition d'être encadrés par des règles connues de tous et appliquées de la même manière.",
     "On montre que les outils ne créent pas de règles de validation, puis on cite nomenclature, droits, délais et traçabilité.")],
C("La collaboration réunit des outils partagés et des règles explicites : sans responsable ni convention, les versions divergent.",
  "Espace commun + droits + nomenclature + validation",
  "Co-édition · historique des versions · commentaires · réunion cadrée",
  "Co-edition~Travail simultane~Version~Etat du document~Commentaire~Demande de precision~Espace partage~Dossiers communs~Droit~Niveau d'acces",
  "Créer l'espace commun|Nommer un responsable|Définir droits et nomenclature|Co-éditer avec commentaires|Valider et archiver la version finale",
  "Laisser plusieurs versions concurrentes|Oublier de révoquer un accès|Multiplier les réunions sans ordre du jour|Ne pas nommer les fichiers",
  "4 personnes et 5 jours~Echeances intermediaires~Nomenclature~Date projet version~Commentaires~Validations~Visioconference~Ordre du jour~Acces~Revoque au depart",
  "Co-edition~Modification simultanee~Partage de fichier~Acces a un espace commun",
  "Commentaire~Echange sans message~Validation~Accord sur la version"))

# ============================================================ PP7
add("PP7", "La gestion des fichiers et la sécurité documentaire", "Pratique professionnelle bureautique et gestion", ["Terminale pro"],
S("La gestion documentaire organise la création, le nommage, le classement, la conservation et la destruction des fichiers."
  "|Une arborescence logique repose sur peu de dossiers de premier niveau, par projet, par client ou par nature de document."
  "|Une convention de nommage précise la date au format AAAA-MM-JJ, le projet, le type de document et un numéro de version."
  "|Les extensions de fichier indiquent le format : .docx pour un document, .xlsx pour un tableur, .pdf pour un document figé."
  "|Le format PDF fige la mise en page et facilite la diffusion, mais il rend la modification plus difficile."
  "|Les doublons proviennent de copies successives et entraînent une perte de temps et un risque d'utiliser une ancienne version."
  "|Un système de sauvegarde suit la règle 3-2-1 : trois copies, deux supports différents, une copie hors du site principal."
  "|La sauvegarde n'est utile que si une restauration est testée régulièrement sur un fichier témoin."
  "|Le chiffrement protège la confidentialité des fichiers sensibles, en particulier sur les supports mobiles."
  "|Les droits d'accès doivent suivre le moindre privilège : chaque personne ne voit que les fichiers nécessaires à sa tâche."
  "|Les fichiers temporaires et les anciennes versions inutiles doivent être supprimés selon la politique de conservation."
  "|La piste d'audit consigne qui a consulté, modifié ou supprimé un document, ce qui facilite la recherche en cas d'incident."),
[QC("Que recommande la règle 3-2-1 pour les sauvegardes ?", "3 copies, 2 supports, 1 hors site~3 dossiers, 2 mots de passe, 1 imprimante~3 ans, 2 mois, 1 jour~3 utilisateurs, 2 réunions, 1 validation", 0,
     "Trois copies, sur deux supports distincts, dont une conservée hors du site principal."),
 QC("Quel format privilégier pour diffuser un document figé ?", "DOCX~XLSX~PDF~TXT", 2,
     "Le PDF préserve la mise en page et limite les modifications involontaires."),
 QC("Quel problème posent les doublons de fichiers ?", "Ils réduisent la taille des disques~Ils entraînent un risque d'utiliser une ancienne version~Ils améliorent la sécurité~Ils suppriment les extensions", 1,
     "Le doute sur la bonne version est le principal risque des doublons."),
 QC("Quelle convention de date est recommandée dans un nom de fichier ?", "12/03/2026~2026-03-12~mars 12~12-03", 1,
     "AAAA-MM-JJ permet un tri chronologique automatique."),
 QC("Quand une sauvegarde est-elle réellement fiable ?", "Quand elle est créée~Quand elle est chiffrée~Quand une restauration a été testée~Quand elle est sur le bureau", 2,
     "Seul un test de restauration prouve que la copie est exploitable."),
 QC("Quel principe limite l'accès aux fichiers sensibles ?", "Le moindre privilège~La duplication systématique~Le partage total~L'absence de mot de passe", 0,
     "On n'accorde que les droits strictement nécessaires à la tâche."),
 QC("Que permet une piste d'audit ?", "De réduire la taille des fichiers~De retracer les consultations et modifications~De changement de police~De supprimer les sauvegardes", 1,
     "Elle consigne les actions sur les documents et aide à l'investigation."),
 QT("Une collaboratrice a accidentellement supprimé un dossier partagé contenant des données clients. Décrire la réaction adaptée.",
     "On ne tente pas d'abord de réécrire les fichiers à partir de copies locales, car on risquerait d'écraser des versions plus récentes. On prévient immédiatement le responsable et le service informatique, puis on identifie la date et l'heure de la suppression à partir de la piste d'audit. On restaure le dossier depuis la sauvegarde la plus proche de cet instant, de préférence sur un emplacement temporaire, on vérifie l'intégrité et la fraîcheur des données, puis on remet le dossier en place. On contrôle enfin les droits d'accès, on documente l'incident et on teste à nouveau la procédure de restauration pour éviter une répétition.",
     "On attend prévenption, usage de l'historique, restauration contrôlée, vérification et retour d'expérience."),
 QT("Expliquer comment une bonne convention de nommage et une arborescence claire améliorent la sécurité documentaire.",
     "Une arborescence stable limite le nombre d'endroits où un fichier peut être oublié et facilite l'attribution des droits par dossier. Une convention de nommage avec date, projet, type et version rend immédiatement visible l'ancienneté d'un document et évite de conserver plusieurs copies au nom ambigu. Il devient alors possible d'appliquer une règle de conservation : supprimer les versions intermédiaires, archiver les documents clos et chiffrer les dossiers sensibles. La clarté de l'organisation réduit aussi les erreurs de partage, car on partage un dossier identifié plutôt qu'un fichier isolé dont on ignore le contenu. Enfin, en cas d'incident, la piste d'audit et les noms cohérents accélèrent l'identification des fichiers concernés.",
     "On relie organisation, droits, conservation, réduction des erreurs et réactivité en cas d'incident.")],
C("La sécurité documentaire combine organisation des fichiers, sauvegardes testées,droits mesurés et traçabilité.",
  "Règle 3-2-1 : 3 copies, 2 supports, 1 hors site",
  "Nommer : AAAA-MM-JJ + projet + type + version",
  "Arborescence~Classement des dossiers~Convention de nommage~Date, projet, version~Sauvegarde~Copie restorable~Chiffrement~Confidentialite~Moindre privilege~Droit minimal~Piste d'audit~Tracabilite",
  "Définir l'arborescence|Nommer les fichiers|Attribuer les droits|Prévoir les sauvegardes|Tester la restauration et tracer",
  "Garder toutes les versions|Croire qu'une copie suffit|Partager un dossier entier par défaut|Ne jamais tester la restauration",
  "2026-03-12~Tri chronologique~PDF~Document figé~3-2-1~Trois copies~Restauration~Test régulier~Dossier supprime~Restauration depuis backup",
  "PDF~Mise en page figee~DOCX~Document modifiable",
  "Sauvegarde~Copie de secours~Restauration~Remise en etat verifiee"))

# ============================================================ FP1
add("FP1", "La lettre commerciale et le courrier professionnel", "Français professionnel", ["1re pro", "Terminale pro"],
S("La lettre commerciale est un écrit formel adressé à un client, un fournisseur ou un partenaire dans le cadre d'une relation d'affaires."
  "|Elle respecte une structure codifiée : en-tête de l'expéditeur, date et lieu, destinataire, objet, formule d'appel, corps, formule de politesse et signature."
  "|L'objet annonce en quelques mots le motif de la lettre : devis, commande, réclamation, relance ou remerciement."
  "|La formule d'appel s'adapte au destinataire : « Monsieur le Directeur », « Madame », ou « Mesdames, Messieurs »."
  "|Le corps se compose de trois parties : l'annonce de l'objet, le développement des faits ou arguments, et la conclusion avec l'action attendue."
  "|Un style clair et concis privilégie des phrases courtes, un vocabulaire précis et une seule idée par paragraphe."
  "|Le ton reste courtois et objectif, même dans une lettre de réclamation : on décrit les faits sans jugement de valeur."
  "|Une relance de paiement rappelle la facture, la date d'échéance, le montant dû et les délais avant mise en demeure."
  "|Une lettre de réclamation précise le produit ou la prestation, la date, le problème constaté, les preuves et la solution souhaitée."
  "|Les pièces jointes sont annoncées dans le corps et mentionnées en fin de lettre avec leur nombre."
  "|La signature manuscrite ou électronique, précédée du nom et de la fonction, engage l'expéditeur et l'organisation."
  "|Une relecture vérifie les noms, les dates, les montants, les références et l'absence de fautes avant tout envoi."),
[QC("Quel élément annonce le motif de la lettre ?", "La signature~L'objet~La date~La formule de politesse", 1,
     "L'objet permet de classer et de comprendre immédiatement le motif."),
 QC("Quelle est une formule d'appel formelle ?", "Salut Paul~Madame,~Coucou~À plus tard", 1,
     "« Madame, » convient dans une lettre formelle ; les autres sont familiales."),
 QC("Que contient le développement d'une lettre de réclamation ?", "Des compliments~Les faits, les preuves et la solution attendue~Un devis~Un organigramme", 1,
     "On décrit objectivement le problème et ce que l'on demande."),
 QC("Quel ton adopter dans une relance de paiement ?", "Ironique~Courtois et ferme~Menacant~Familier", 1,
     "On reste professionnel tout en rappelant clairement l'échéance et les suites possibles."),
 QC("Quelles informations doit préciser une relance ?", "La facture, l'échéance et le montant~La couleur du papier~L'heure d'envoi~Le nom du commercial", 0,
     "Ces repères permettent au destinataire d'identifier rapidement la créance."),
 QC("Que faut-il faire avec une pièce jointe ?", "La cacher~L'annoncer dans le corps et la mentionner en fin de lettre~L'envoyer sans prévenir~La remplacer par une phrase", 1,
     "Annoncer les pièces évite les oublis et facilite le traitement."),
 QC("Quel contrôle précède l'envoi ?", "La longueur seulement~Les noms, dates, montants et références~Le nombre de pages~La police uniquement", 1,
     "Les données exactes sont les plus exposées aux conséquences d'une erreur."),
 QT("Rédiger le corps d'une lettre de relance pour une facture de 2 400 € échue le 15 mars, restée impayée le 1er avril.",
     "« Nous nous permettons de vous rappeler que la facture n° 2026-118 d'un montant de 2 400 €, échue le 15 mars, n'a pas encore été réglée à ce jour. Nous vous serions reconnaissants de bien vouloir effectuer le virement sous huit jours, en nous indiquant la date de paiement si celui-ci a déjà été ordonné. Passé ce délai, nous serions amenés à appliquer les intérêts de retard prévus aux conditions générales de vente et à engager une procédure de recouvrement. Nous restons bien entendu à votre disposition pour tout complément d'information. » Le ton est courtois mais ferme, les références sont précises et l'action attendue est claire.",
     "On attend référence de facture, montant, échéance, délai, suites annoncées et ton courtois."),
 QT("Expliquer pourquoi une lettre professionnelle doit rester objective même en cas de désaccord.",
     "Une lettre professionnelle constitue une trace écrite susceptible d'être relue par un responsable, un service juridique ou un juge. Les jugements de valeur et les propos emails nuisent à la crédibilité de l'expéditeur et peuvent être retournés contre lui. Décrire les faits, les dates, les montants et les pièces permet au destinataire de comprendre précisément le litige et d'y répondre. Le ton courtois facilite également une solution amicale et préserve la relation commerciale. La fermeté s'exprime alors par des échéances et des conséquences annoncées clairement, non par l'emportement. Une réclamation bien écrite obtient plus souvent satisfaction qu'une lettre agressive.",
     "On invoque la valeur de preuve, la crédibilité, la résolution du litige et la préservation de la relation.")],
C("La lettre commerciale est un écrit codifié, objectif et actionnable : chaque partie conduit le destinataire à une réponse.",
  "En-tête · date · destinataire · objet · appel · corps · politesse · signature",
  "Corps : annonce → développement → action attendue",
  "Objet~Motif de la lettre~Formule d'appel~Salutation formelle~Corps~Fait et action~Piece jointe~Annoncee dans le texte~Signature~Engagement de l'expediteur",
  "Identifier le destinataire et l'objectif|Rédiger un objet précis|Structurer le corps en trois parties|Annoncer les pièces jointes|Relire les données et signer",
  "Oublier la référence de facture|Employer un ton familier|Ne pas annoncer les pièces jointes||Négliger la relecture des montants",
  "Facture 2026-118~Montant 2 400 euros~Echeance 15 mars~Relance le 1er avril~Sous huit jours~Delai de reglement~Interets de retard~Suite annoncee",
  "Lettre commerciale~Ecrit formel~Courriel professionnel~Format plus court",
  "Rclamation~Facts and preuves~Relance~Echeance et action"))

# ============================================================ FP2
add("FP2", "La note interne et le compte rendu", "Français professionnel", ["1re pro", "Terminale pro"],
S("La note interne est un écrit court diffusé dans l'organisation pour informer, demander ou proposer une action."
  "|Elle comporte un en-tête précisant l'expéditeur, le destinataire, la date et l'objet."
  "|Une note doit répondre à une question claire : qui fait quoi, pourquoi, quand et avec quels moyens."
  "|Le plan type distingue le contexte, le constat ou le problème, les propositions et la conclusion avec une demande de décision."
  "|Le style est direct, impersonnel et concis : on évite les développements littéraires et les opinions non étayées."
  "|Le compte rendu restitue de façon fidèle et structurée ce qui s'est dit ou décidé lors d'une réunion."
  "|Il indique la date, le lieu, les participants, l'ordre du jour et le nom de la personne qui a rédigé le document."
  "|Il distingue les informations, les décisions prises et les actions à engager avec un responsable et une échéance."
  "|La restitution doit être objective : on rapporte les positions sans les commenter et on attribue chaque intervention."
  "|Les décisions sont formulées de manière univoque pour éviter les interprétations divergentes."
  "|Un tableau de suivi des actions, avec responsable, échéance et statut, rend le compte rendu opérationnel."
  "|Le compte rendu est diffusé rapidement aux participants et aux personnes concernées, puis archivé comme preuve des décisions."),
[QC("Quel élément figure dans l'en-tête d'une note interne ?", "La conclusion~Expéditeur, destinataire, date et objet~Le budget~Les pièces jointes seulement", 1,
     "Ces quatre repères identifient immédiatement la note."),
 QC("Quelle question une note doit-elle permettre de trancher ?", "Qui fait quoi, pourquoi et quand ?~Quel est le prix de vente ?~Quelle est la couleur de la charte ?~Combien de pages ?", 0,
     "Une note utile débouche sur une décision ou une action claire."),
 QC("Quel plan convient à une note proposant une action ?", "Contexte, constat, propositions, demande de décision~Introduction, développement, conclusion littéraire~Chronologie des événements~Liste des participants", 0,
     "Ce plan conduit le lecteur du constat à la décision."),
 QC("Quel style adopter dans une note interne ?", "Lyrique et personnel~Direct, impersonnel et concis~Humoristique~Très long", 1,
     "La concision et l'objectivité sont les qualités essentielles."),
 QC("Quel contenu n'est pas un compte rendu ?", "Les décisions prises~Les actions avec responsables~Les opinions personnelles du rédacteur~Les interventions attribuées", 2,
     "Le rédacteur restitue, il ne commente pas."),
 QC("Que doit préciser une action dans un compte rendu ?", "Un responsable et une échéance~Une couleur~Un avis~Une citation littéraire", 0,
     "Sans responsable ni date, l'action reste sans effet."),
 QC("Pourquoi diffuser rapidement un compte rendu ?", "Pour occuper la boîte mail~Pour que chacun connaisse les décisions et agisse~Pour remplacer la réunion~Pour réduire le nombre de participants", 1,
     "La diffusion transforme la décision en action et évite les malentendus."),
 QT("Rédiger une note interne proposant le déplacement d'une réunion hebdomadaire du lundi au mardi, en précisant la raison et la décision attendue.",
     "« Objet : proposition de déplacement de la réunion hebdomadaire. Le créneau du lundi matin entraîne depuis trois semaines des retards liés aux livraisons et réduit la participation des services comptables. Nous proposons de déplacer la réunion au mardi 14 h, dans la même salle, à compter du mois prochain. Ce créneau libère le lundi pour le traitement des flux entrants et ne modifie pas la durée de la réunion. Nous vous remercions de bien vouloir nous indiquer votre accord avant le 20 du mois afin de mettre à jour les invitations et l'ordre du jour. » La note est courte, elle énonce le contexte, la proposition et une décision attendue avec une date.",
     "On attend objet, contexte, proposition précise et demande de décision datée."),
 QT("Expliquer comment transformer une discussion de réunion en compte rendu opérationnel.",
     "Pendant la réunion, on note les interventions en attribuant chaque propos à son auteur, en distinguant les informations, les questions, les décisions et les actions. On relève systématiquement le nom du responsable et l'échéance de chaque action. Après la réunion, on structure le document selon l'ordre du jour, on reformule les décisions de manière univoque et on supprime les digressions. On ajoute un tableau de suivi avec trois colonnes : action, responsable, échéance, complété d'un statut. On relit les montants, les dates et les noms, puis on diffuse rapidement aux participants et on archive le document. Un compte rendu opérationnel permet à chacun de savoir ce qu'il doit faire sans relire la discussion.",
     "On attend collecte attribuée, distinction faits/décisions/actions, reformulation, tableau de suivi, relecture et diffusion.")],
C("La note interne provoque une décision ; le compte rendu fixe ce qui a été décidé et les actions qui en découlent.",
  "Note : contexte → constat → proposition → décision attendue",
  "Compte rendu : informations · décisions · actions (responsable + échéance)",
  "Note interne~Ecrit court et dirige~En-tete~Auteur, destinataire, objet~Constat~Probleme identifie~Compte rendu~Restitution fidèle~Action~Responsable et echeance",
  "Préciser l'objet|Poser le contexte|Énoncer le constat|Proposer une action et une décision|Relire et diffuser",
  "Mélanger faits et opinions|Oublier le destinataire|Laisser une action sans responsable|Diffuser trop tard",
  "Lundi matin~Retards de livraison~Mardi 14 h~Nouveau creneau~Avant le 20~Date de decision~Tableau de suivi~Actions et statuts",
  "Note interne~Demande d'action~Compte rendu~Trace des decisions",
  "Information~Ce qui a ete dit~Decision~Ce qui est retenu"))

# ============================================================ FP3
add("FP3", "Le procès-verbal et le rapport d'activité", "Français professionnel", ["Terminale pro"],
S("Le procès-verbal est un document officiel qui constate de manière authentique un fait ou une délibération, comme une assemblée générale."
  "|Il se distingue du compte rendu par sa valeur juridique : il fait foi jusqu'à preuve contraire."
  "|Un procès-verbal de réunion mentionne le lieu, la date, l'heure, la présidence, les présents, les excusés et l'ordre du jour."
  "|Il relate les débats dans leur ordre, les résolutions mises au vote et les résultats avec le nombre de voix."
  "|Les décisions sont rédigées sous forme de résolutions numérotées, avec un objet et un dispositif clair."
  "|Le procès-verbal est signé par le président de séance et souvent par le secrétaire, puis conservé dans les archives de l'organisation."
  "|Toute correction doit être signalée et paraphée : on ne réécrit pas discrètement un document authentique."
  "|Le rapport d'activité présente de façon structurée ce qu'une équipe ou un service a réalisé sur une période."
  "|Il suit généralement un plan : contexte et objectifs, actions menées, résultats chiffrés, difficultés et perspectives."
  "|Les chiffres doivent être sourcés, cohérents et commentés : un pourcentage sans base de calcul n'a pas de sens."
  "|Le rapport distingue les faits des interprétations etnuance les conclusions en fonction des limites des données."
  "|La synthèse en début de document permet au lecteur pressé de saisir l'essentiel avant de consulter les détails."),
[QC("Quelle est la principale différence entre procès-verbal et compte rendu ?", "Sa longueur~Sa valeur juridique~Sa couleur~Son nombre de pages", 1,
     "Le procès-verbal fait foi jusqu'à preuve contraire, ce qui n'est pas le cas d'un simple compte rendu."),
 QC("Que doit mentionner un procès-verbal de réunion ?", "Les présents, l'ordre du jour et les résolutions~Les opinions personnelles du rédacteur~Le menu~La météo", 0,
     "Ces mentions constituent les éléments authentificateurs du document."),
 QC("Comment sont formulées les décisions dans un procès-verbal ?", "En résolutions numérotées~En questions ouvertes~En citations~En puces informelles", 0,
     "Une résolution numérotée avec dispositif est juridiquement identifiable."),
 QC("Qui signe généralement un procès-verbal ?", "Tous les participants~Le président de séance et le secrétaire~Le comptable~Le fournisseur", 1,
     "Les signatures authentifient le document."),
 QC("Comment corriger un procès-verbal already signé ?", "En le réécrivant discrètement~En signalant et paraphant la correction~En le supprimant~En le remplaçant par un e-mail", 1,
     "La correction doit être visible pour préserver l'authenticité."),
 QC("Quel plan convient à un rapport d'activité ?", "Contexte, actions, résultats, difficultés, perspectives~Objet, formule de politesse, signature~Chronologie pure~Liste des participants", 0,
     "Ce plan suit la logique du diagnostic vers la projection."),
 QC("Pourquoi commenter un pourcentage dans un rapport ?", "Pour le rendre plus long~Parce qu'il faut préciser la base de calcul et l'évolution~Pour cacher les résultats~Pour éviter les graphiques", 1,
     "Sans référence ni base, un pourcentage est trompeur."),
 QT("Décrire la structure d'un procès-verbal d'assemblée générale et expliquer l'importance de chaque mention.",
     "Le document commence par l'identification : nom de l'organisation, date, heure et lieu de la séance. Il indique ensuite le président et le secrétaire, la liste des présents et des représentés, ainsi que le quorum. L'ordre du jour adopté est reproduit, puis chaque point est traité dans l'ordre : exposé, interventions, questions et résolutions mises au vote. Pour chaque résolution, on indique le nombre de voix favorables, contraires et abstentionnées. Le document se termine par la signature du président et du secrétaire. Chaque mention est utile : elle prouve la régularité de la convocation, la validité des délibérations et le résultat des votes, ce qui permet en cas de contestation de vérifier la décision.",
     "On attend identification, quorum, ordre du jour, résolutions, résultats de vote et signatures avec leur utilité."),
 QT("Un rapport indique : « La satisfaction client a augmenté de 10 % ». Expliquer pourquoi cette phrase est insuffisante et la reformuler.",
     "La phrase ne précise ni la période de référence, ni l'enquête utilisée, ni la base de calcul, ni le niveau atteint. Une hausse de 10 % peut signifier un passage de 70 % à 77 % ou de 70 % à 80 % selon qu'il s'agit d'un pourcentage de points ou d'une variation relative. Il faut aussi indiquer la taille de l'échantillon et la méthode, car un sondage de 20 personnes n'a pas la même fiabilité qu'une enquête de 2 000 clients. Une reformulation rigoureuse serait : « Selon l'enquête annuelle menée en décembre auprès de 1 200 clients, le taux de satisfaction est passé de 72 % en 2025 à 79 % en 2026, soit une progression de 7 points. »",
     "On identifie les informations manquantes et on propose une formulation avec période, source, échantillon et base.")],
C("Le procès-verbal authentifie une délibération ; le rapport d'activité documente une performance avec des chiffres sourcés et commentés.",
  "Procès-verbal : mentions légales + résolutions + signatures",
  "Rapport : contexte · actions · résultats · difficultés · perspectives",
  "Proces verbal~Document authentique~Resolution~Decision formelle~Quorum~Nombre de membres requis~Signature~Authentification~Rapport~Bilan d'activite~Resultat~Chiffre sourcé",
  "Vérifier la convocation et le quorum|Noter les interventions|Rédiger les résolutions|Chiffrer les résultats|Signer, dater et archiver",
  "Réécrire discrètement un procès-verbal|Omettre les abstentions|Donner un pourcentage sans base|Confondre compte rendu et procès-verbal",
  "Assemblee generale~Quorum requis~Resolution~Vote et resultat~Signature~President et secretaire~Satisfaction~72 a 79 pour cent",
  "Proces verbal~Valeur juridique~Compte rendu~Restitution simple",
  "Points de pourcentage~Difference de taux~Variation relative~Rapport entre taux"))

# ============================================================ FP4
add("FP4", "Le curriculum vitae et la lettre de motivation", "Français professionnel", ["1re pro", "Terminale pro"],
S("Le curriculum vitae, ou CV, est un document synthétique qui présente le parcours, les compétences et la motivation d'un candidat."
  "|Il doit tenir sur une page pour un débutant, avec une structure claire et une police lisible."
  "|Les rubriques classiques sont l'identité, le titre du poste visé, la formation, l'expérience, les compétences, les langues et les centres d'intérêt."
  "|Les(expériences sont présentées de la plus récente à la plus ancienne, avec les dates, l'entreprise, l'intitulé et deux ou trois réalisations concrètes."
  "|Les verbes d'action et les résultats chiffrés rendent les réalisations plus crédibles que des descriptions générales."
  "|Le CV est adapté à chaque offre : on met en avant les compétences demandées et on utilise les mots-clés du recrutement."
  "|La lettre de motivation complète le CV en expliquant pourquoi le candidat s'intéresse à l'entreprise et au poste."
  "|Elle suit le plan « je vous écris parce que… je peux apporter… je souhaite… » en trois paragraphes courts."
  "|L'entreprise doit être nommément identifiée, avec une information précise qui prouve une recherche réelle."
  "|Le candidat relie ses compétences aux besoins de l'offre plutôt que de simplement répéter son CV."
  "|La mise en page est aérée, sans faute d'orthographe, avec une formule d'appel et une formule de politesse adaptées."
  "|Avant envoi, on relit les dates, les noms d'entreprise, les coordonnées et la cohérence entre le CV et la lettre."),
[QC("Combien de pages doit faire un CV de débutant ?", "Une page~Trois pages~Cinq pages~Dix pages", 0,
     "Une page suffit pour un parcours court et rend le document plus lisible."),
 QC("Dans quel ordre présenter les expériences ?", "De la plus ancienne à la plus récente~De la plus récente à la plus ancienne~Par ordre alphabétique~Au hasard", 1,
     "L'ordre antéchronologique met en avant l'expérience la plus actuelle."),
 QC("Quel élément renforce la crédibilité d'une réalisation ?", "Un adjectif~Un résultat chiffré~Une couleur~Une longue phrase", 1,
     "Un chiffre précis appuie la réalisation et la rend vérifiable."),
 QC("Que doit expliquer la lettre de motivation ?", "La biographie complète~L'intérêt pour l'entreprise et l'apport du candidat~Le salaire souhaité~Les loisirs", 1,
     "Elle établit le lien entre le candidat, le poste et l'organisation."),
 QC("Quel plan suit souvent la lettre de motivation ?", "Pourquoi j'écris / ce que j'apporte / ce que je souhaite~ introduction / anecdote / conclusion~Question / réponse / blague~Titre / signature / date", 0,
     "Ce plan en trois temps construit une argumentation claire."),
 QC("Comment prouver une recherche réelle sur l'entreprise ?", "En citant un fait précis sur l'entreprise~En répétant le nom trois fois~En utilisant un modèle générique~En écrivant une longue phrase", 0,
     "Une information précise montre que le candidat s'est renseigné."),
 QC("Que vérifier avant l'envoi du dossier ?", "Les dates et les coordonnées seulement~La cohérence entre CV, lettre et offre~La couleur du papier~Le nombre de mots", 1,
     "Les deux documents doivent raconter le même parcours et viser le même poste."),
 QT("Réécrire une ligne de CV « J'ai aidé au classement des dossiers » pour la rendre plus parlante.",
     "Une version améliorée pourrait être : « Classement et numérisation de 450 dossiers clients sur trois mois, avec réduction du temps de recherche de 30 % grâce à une nomenclature normalisée. » La ligne précise l'action avec un verbe à l'infinitif ou un participe, la quantité traitée, la durée et le résultat obtenu. Elle montre à la fois la maîtrise d'un outil ou d'une méthode et un effet mesurable, ce qui permet au recruteur de se projeter. Il faut bien sûr que les chiffres soient exacts et que le candidat puisse les expliquer en entretien.",
     "On attend verbe d'action, chiffres, contexte et résultat, avec une mise en garde sur l'exactitude."),
 QT("Expliquer pourquoi un CV et une lettre de motivation doivent être adaptés à chaque offre.",
     "Un recruteur compare les candidats aux besoins précis du poste. Un CV générique dilue les compétences pertinentes au milieu d'informations sans rapport, tandis qu'un CV adapté place en avant les expériences et les mots-clés attendus dans l'offre. La lettre doit montrer que le candidat a compris l'environnement de l'entreprise : secteur, taille, actualité ou valeurs. Cette personnalisation ne signifie pas inventer des compétences : elle consiste à sélectionner et à formuler autrement des éléments réels du parcours. Elle prouve un intérêt sincère et une capacité d'analyse, deux qualités appréciées dans les métiers de la gestion. Un envoi identique à dix entreprises donne l'impression d'une candidature automatique.",
     "On relie adaptation, mots-clés, compréhension de l'entreprise et honnêteté du parcours.")],
C("Le CV montre ce que le candidat sait faire ; la lettre explique pourquoi il veut le faire ici et maintenant.",
  "CV : une page, rubriques claires, expériences antéchronologiques",
  "Lettre : pourquoi j'écris / ce que j'apporte / ce que je souhaite",
  "CV~Parcours et competences~Rubrique~Formation ou experience~Verbe d'action~Realisation concrete~Lettre de motivation~Lien avec l'entreprise~Mots-cles~Termes de l'offre",
  "Analyser l'offre et l'entreprise|Sélectionner les expériences pertinentes|Rédiger des réalisations chiffrées|Construire la lettre en trois paragraphes|Relire les deux documents ensemble",
  "Envoyer le même dossier partout|Inventer des chiffres|Oublier les coordonnées|Répéter le CV dans la lettre",
  "450 dossiers~Quantite traitee~30 %~Temps de recherche reduit~Trois paragraphes~Structure de la lettre~Mots-cles~Alignement avec l'offre",
  "CV~Ce que j'ai fait~Lettre de motivation~Pourquoi je postule ici",
  "Realisation chiffree~Preuve concrete~Description vague~Faible impact"))

# ============================================================ LG1
add("LG1", "L'anglais professionnel à l'écrit", "Langues", ["1re pro", "Terminale pro"],
S("Professional writing in English values clarity, brevity and a tone adapted to the reader."
  "|A business message usually begins with a short subject line and a salutation matched to the level of formality."
  "|The opening sentence states the purpose: « I am writing to confirm the delivery date »."
  "|Short paragraphs and bullet points help the reader identify the request and the deadlines quickly."
  "|Polite requests use modal forms such as could, would and please: « Could you send the file by Friday? »"
  "|Reports and emails should avoid slang, exaggeration and emotional wording."
  "|Figures, dates and units must follow an unambiguous format: 12 May 2026 or 12/05/2026 with a stated convention."
  "|Common connectors structure the text: firstly, however, therefore, in addition and finally."
  "|The past simple is used for finished actions with a time reference, while the present perfect links a past action to the present."
  "|Conditional sentences express hypothetical situations: « If the order is confirmed, we will ship it on Monday »."
  "|A closing formula such as « Kind regards » precedes the full name, job title and company details."
  "|Proofreading checks spelling, verb agreement, the spelling of names and the presence of every promised attachment."),
[QC("Which sentence states the purpose of an email clearly?", "I am writing to confirm the delivery date~It is about that thing~Hello, how are you~The file is there", 0,
     "The opening should announce the reason for writing in one precise sentence."),
 QC("Which form makes a request polite?", "Send me the file~Could you send the file?~You must send the file~Sending the file", 1,
     "Could you is a standard polite request form."),
 QC("Which connector introduces a contrast?", "Firstly~However~Therefore~In addition", 1,
     "However marks a contrast; therefore marks a consequence."),
 QC("Which tense is used with a definite past time such as yesterday?", "Present simple~Past simple~Present perfect~Future", 1,
     "A finished action at a stated past time uses the past simple."),
 QC("What is the function of « If the order is confirmed, we will ship it »?", "A condition and its consequence~A description of the past~A question~An apology", 0,
     "The if-clause states the condition and the main clause the consequence."),
 QC("Which closing suits a neutral professional email?", "Cheers mate~Kind regards~See you soon~Take care", 1,
     "Kind regards is widely accepted in professional correspondence."),
 QC("What must a final proofreading include?", "Only the subject line~Names, dates, agreement and attachments~The font colour~The number of paragraphs", 1,
     "Details such as names, dates and references are the most consequential."),
 QT("Rewrite this informal sentence in a professional register: « Hi, I need the report, give it to me quick. »",
     "A professional version would be: « Dear Ms Smith, I would be grateful if you could send me the monthly report by Thursday 12 May, as I need it for the management meeting. Please let me know if any additional information is required. Kind regards, [Name]. » The rewrite replaces the informal greeting, turns the demand into a polite request with a modal verb, gives a precise deadline and reason, and adds an appropriate closing. The content is unchanged, but the tone now shows respect and makes the action easy to schedule.",
     "On attend registre formel, modale polie, échéance précise et formule de clôture."),
 QT("Explain why dates and figures must follow an explicit convention in international business writing.",
     "The same sequence of digits can be read differently across countries: 03/05/2026 means 3 May in British usage but March 5 in American usage. Such ambiguity can shift a delivery date by two months and cause real financial loss. Professional writing therefore uses an unambiguous format, for example 3 May 2026, or states the convention when numeric dates are required. The same care applies to decimal separators, currencies and units: €1,200.50 and 1 200,50 € should be identified by currency code when needed. Clarity in these details is part of professional responsibility, not mere stylistic preference.",
     "On cite l'ambiguïté des dates, un exemple chiffré et la nécessité d'une convention explicite.")],
C("Professional English writing turns information into action through structure, polite forms and unambiguous details.",
  "Purpose → details → action → closing",
  "Could / would for politeness · however for contrast · if for conditions",
  "Purpose~Reason for writing~Polite request~Could and would~Connector~However and therefore~Condition~If clause~Closing~Kind regards",
  "State the purpose in the first sentence|Use short paragraphs|Choose polite modal forms|Check dates and figures|Proofread names and attachments",
  "Using slang in a business email|Writing an ambiguous date|Forgetting the subject line|Omitting the promised attachment",
  "12 May 2026~Date unambigua~Could you~Demande polie~If confirmed~Condition et consequence~Kind regards~Cloture standarde",
  "Past simple~Action finie et datee~Present perfect~Lien avec le present",
  "Formal~Dear Ms Smith~Informal~Hi or hello"))

# ============================================================ LG2
add("LG2", "L'anglais à l'oral : accueil et rendez-vous", "Langues", ["1re pro", "Terminale pro"],
S("L'anglais à l'oral privilégie des formules courtes, polies et immédiatement compréhensibles."
  "|L'accueil commence par un salut adapté à l'heure, comme « Good morning » ou « Good afternoon »."
  "|Une offre de service simple, « How can I help you? », installe un cadre professionnel et accueillant."
  "|Pour identifier un visiteur, on demande « May I have your name, please? » plutôt qu'une question directe."
  "|Le modal « could » et le mot « please » rendent une demande polie et non autoritaire."
  "|Un rendez-vous doit être confirmé avec un jour et une heure précis, par exemple « Tuesday at 10 »."
  "|« Would you like a seat? » propose poliment un siège et « Would you like a coffee? » une boisson."
  "|« I'm afraid… » permet d'annoncer une absence avec tact, sans donner de détail personnel."
  "|« Could you hold the line, please? » est la formule pour mettre un appelant en attente."
  "|Si la personne est indisponible, on propose une alternative : prendre un message ou rappeler."
  "|On note précisément le nom, le numéro, l'heure et le motif, puis on répète pour vérification."
  "|On termine l'appel par un résumé de l'action et un remerciement, puis on transmet le message rapidement."),
[QC("Quelle formule accueille un client de façon professionnelle ?", "Hi mate~Good morning, how can I help you?~Hey there~What do you want?", 1,
     "Une formule polie et une proposition d'aide installent un accueil professionnel."),
 QC("Comment demander poliment le nom du visiteur ?", "Who are you?~May I have your name, please?~Your name, quickly~Name?", 1,
     "May I… please est la tournure polie adaptée."),
 QC("Que signifie la question « Would you like a seat? » ?", "Voulez-vous partir ?~Souhaitez-vous vous asseoir ?~Avez-vous un rendez-vous ?~Voulez-vous payer ?", 1,
     "On propose poliment un siège au visiteur."),
 QC("Comment confirmer un rendez-vous ?", "Maybe we meet~The appointment is confirmed for Tuesday at 10~We'll see~Perhaps", 1,
     "Une confirmation précise indique le jour et l'heure."),
 QC("Quelle réponse convient si le responsable est absent ?", "He is not here, bye~I'm afraid he is unavailable. Can I take a message?~He is busy, forget it~No idea", 1,
     "On informe avec tact et on propose une solution."),
 QC("Que signifie « Could you hold the line, please? » ?", "Raccrochez~Ne quittez pas, s'il vous plaît~Parlez plus fort~Rappelez plus tard", 1,
     "C'est la formule pour mettre quelqu'un en attente au téléphone."),
 QC("Que faut-il faire à la fin d'un appel professionnel ?", "Raccrocher immédiatement~Résumer l'action et remercier~Répéter son nom~Changer de sujet", 1,
     "Un résumé et un remerciement sécurisent la compréhension."),
 QT("Rédiger un court dialogue d'accueil d'un client qui a rendez-vous avec la responsable commerciale.",
     "« Good morning, welcome. How can I help you? — Good morning. I have an appointment with Ms Martin at 10 o'clock. — May I have your name, please? — Yes, it's Mr Dubois. — Thank you, Mr Dubois. Please take a seat. I'm afraid Ms Martin is running a few minutes late; would you like a coffee while you wait? — Yes, thank you. — I'll let her know you are here. » Le dialogue est courtois, il confirme l'objet de la visite, identifie le client et propose une solution en cas d'attente.",
     "On attend salutation, identification, confirmation du rendez-vous et proposition en cas d'attente."),
 QT("Expliquer comment gérer un appel téléphonique lorsque l'interlocuteur n'est pas disponible.",
     "On répond rapidement en s'identifiant et en saluant. On explique avec tact que la personne est indisponible, sans donner de détail personnel : « I'm afraid Ms Martin is in a meeting at the moment. » On propose ensuite une alternative : prendre un message, proposer un rappel ou indiquer un autre interlocuteur. On note précisément le nom, le numéro, l'heure et le motif du message, puis on répète ces informations pour vérification. On termine par une formule de remerciement et on transmet le message rapidement. Cette méthode montre que l'organisation prend l'appel au sérieux, même en l'absence de la personne demandée.",
     "On attend identification, tact, alternative, relevé précis et confirmation.")],
C("L'accueil téléphonique et en personne combine courtoisie, identification précise et proposition d'une solution concrète.",
  "Greet → identify → clarify → assist → confirm",
  "May I… ? / Would you like… ? / I'm afraid…",
  "Accueil~Saluer et proposer son aide~Identification~Demander le nom poliment~Rendez-vous~Jour et heure confirmes~Message~Nom, numero et motif~Attente~Proposer une alternative",
  "Saluer et s'identifier|Demander le motif de la visite|Confirmer le rendez-vous|Proposer une solution si nécessaire|Résumer et transmettre",
  "Répondre sans saluer|Donner des informations personnelles|Oublier de noter le message|Raccrocher sans résumer",
  "Good morning~Salutation professionnelle~May I have your name~Identification polie~Tuesday at 10~Rendez-vous confirme~Hold the line~Mise en attente",
  "En personne~Accueil visuel~Au telephone~Voix et clarté",
  "Confirm~Confirmer~Suggest~Proposer"))

# ============================================================ LG3
add("LG3", "L'espagnol commercial : salutations et correspondance", "Langues", ["1re pro", "Terminale pro"],
S("La correspondance commerciale en espagnol suit des usages précis, avec des formules de politesse plus développées qu'en français."
  "|L'ouverture d'une lettre emploie fréquemment « Estimado Sr. » ou « Estimada Sra. », suivis du nom de famille."
  "|« Buenos días » s'utilise le matin, « Buenas tardes » l'après-midi et « Buenas noches » le soir ou pour dire bonne nuit."
  "|La formule « ¿Cómo está usted? » s'adresse avec respect à une personne que l'on ne connaît pas bien."
  "|Le tutoiement, « tú », reste réservé aux relations familières ou lorsque l'interlocuteur le propose."
  "|Une demande polie se formule avec « ¿Podría…? » ou « Le agradecería que… », suivis de l'infinitif ou du subjonctif."
  "|Le verbe « necesitar » exprime un besoin, tandis que « querer » exprime un souhait : le ton change selon le contexte."
  "|La clôture formelle utilise « Atentamente » ou « Un saludo cordial », puis le nom et la fonction."
  "|Le numéro de téléphone et l'adresse e-mail se vérifient particulièrement dans les échanges internationaux."
  "|Les montants s'écrivent avec le symbole € placé généralement après le chiffre en espagnol : 1.200 €."
  "|Les dates suivent l'ordre jour/mois/année, par exemple 12 de mayo de 2026, ce qui évite la confusion avec l'anglais."
  "|Une relecture attentive porte sur les accents, car ils changent le sens ou la prononciation : « si » et « sí » ne veulent pas dire la même chose."),
[QC("Quelle formule convient pour s'adresser à un monsieur dans une lettre formelle ?", "Hola tío~Estimado Sr. García~Buenas noches~Ciao", 1,
     "Estimado Sr. suivra du nom est la formelle appropriée."),
 QC("Quand utilise-t-on « Buenas tardes » ?", "Le matin~L'après-midi~La nuit~Uniquement le week-end", 1,
     "Buenas tardes salue l'après-midi ; Buenos días le matin."),
 QC("Comment demander poliment une information ?", "Dime~¿Podría enviarme el documento?~Envíamelo ya~Tú tienes que", 1,
     "¿Podría…? est une tournure polie et respectueuse."),
 QC("Quel est le sens de « ¿Cómo está usted? » ?", "Comment vas-tu ?~Comment allez-vous ?~Qui êtes-vous ?~Où allez-vous ?", 1,
     "C'est la forme de respect avec usted, opposée au tutoiement."),
 QC("Quelle formule clôt une lettre formelle espagnole ?", "Hasta luego~Atentamente~Nos vemos~Chao", 1,
     "Atentamente est une clôture formelle courante."),
 QC("Comment s'écrit généralement un montant en espagnol ?", "€ 1,200.50~1.200 €~1,200€ dollar~1200 pounds", 1,
     "Le symbole € se place généralement après le montant, avec un point comme séparateur de milliers."),
 QC("Pourquoi les accents sont-ils importants en espagnol ?", "Ils sont décoratifs~Ils peuvent changer le sens des mots~Ils remplacent la ponctuation~Ils sont facultatifs", 1,
     "Par exemple, si signifie « si » et sí signifie « oui »."),
 QT("Rédiger une courte demande polie de devis en espagnol et expliquer les choix de formulation.",
     "« Estimado Sr. López: Buenos días. Le agradecería que me enviara un presupuesto para el suministro de material de oficina, según la solicitud que le remití el pasado 12 de mayo. Quedo a la espera de su respuesta antes del viernes. Atentamente, [nom], [fonction]. » Les choix sont formels : Estimado et Buenos días pour l'ouverture, Le agradecería que pour une demande respectueuse, une date précise pour identifier la demande, une échéance claire et Atentamente pour la clôture.",
     "On attend formule d'appel formelle, demande avec agradecería, référence de date, échéance et clôture."),
 QT("Expliquer les différences de registre entre « tú » et « usted » et leurs conséquences professionnelles.",
     "« Usted » est la forme de respect, employée par défaut avec un interlocuteur que l'on ne connaît pas, un client ou une autorité. « Tú » marque la familiarité et suppose une relation déjà établie ou une invitation explicite de l'autre personne. Dans un contexte commercial, utiliser « tú » trop tôt peut paraître intrusif ou irrévérencieux, surtout avec des clients plus âgés ou dans des cultures hispaniques formelles. À l'inverse, un « usted » maintenu après plusieurs échanges peut créer une distance inutile. La règle pratique est de commencer avec « usted » et d'attendre que l'interlocuteur propose le tutoiement. Ce choix influence aussi les formes verbales et les adjectifs possessifs, donc toute la structure de la phrase.",
     "On oppose respect et familiarité, avec une règle pratique et les conséquences grammaticales.")],
C("L'espagnol commercial se distingue par des formules de politesse élaborées et par le choix entre tú et usted.",
  "Estimado Sr./Sra. · Buenos días / Buenas tardes · Atentamente",
  "¿Podría…? / Le agradecería que… · usted = respect",
  "Saludo~Buenos dias o buenas tardes~Tratamiento~Estimado y usted~Peticion~Podria y agradeceria~Despedida~Atentamente~Fecha~Dia, mes y ano",
  "Choisir le registre|Saluer selon l'heure|Formuler la demande poliment|Vérifier dates et montants|Relire les accents",
  "Tutoyer trop tôt|Oublier les accents|Confondre si et sí|Employer une clôture familière",
  "Estimado Sr. Lopez~Appel formel~Le agradeceria~Demande respectueuse~12 de mayo~Date jour mois annee~1.200 euros~Montant apres le chiffre",
  "Tú~Familiarite~Usted~Respect et distance",
  "Buenos dias~Matin~Buenas tardes~Apres-midi"))

# ============================================================ LG4
add("LG4", "L'allemand professionnel : présentation et échanges", "Langues", ["1re pro", "Terminale pro"],
S("L'allemand professionnel privilégie des formules formelles et un registre respectueux lors d'un premier contact."
  "|« Guten Morgen » salue le matin, « Guten Tag » dans la journée et « Gute Nacht » avant de se coucher."
  "|Une lettre formelle s'ouvre avec « Sehr geehrte Frau Mayer » ou « Sehr geehrter Herr Mayer »."
  "|« Auf Wiedersehen » est la formule d'adieu standard ; « Bis bald » reste plus informel."
  "|Le pronom « Sie » marque la politesse et la distance avec un client, un supérieur ou un collègue peu connu."
  "|Le « du » suppose un accord explicite et marque la proximité ; on ne l'emploie pas au premier contact."
  "|« Können » signifie pouvoir et permet une demande polie avec le conditionnel « Könnten Sie…? »."
  "|« Danke schön » remercie et « Bitte » signifie à la fois s'il vous plaît et de rien."
  "|Une présentation indique le nom, la fonction, l'entreprise, le lieu et une activité concrète."
  "|« Freut mich, Sie kennenzulernen » conclut poliment une première rencontre."
  "|Une date allemande s'écrit jour avant mois, par exemple « den 12. Mai 2026 »."
  "|Le choix du pronom entraîne des formes verbales et des possessifs différents : toute la phrase s'en trouve modifiée."),
[QC("Quelle formule salue un interlocuteur le matin en allemand ?", "Guten Tag~Guten Morgen~Gute Nacht~Auf Wiedersehen", 1,
     "Guten Morgen signifie bonjour le matin ; Guten Tag est utilisé dans la journée."),
 QC("Comment s'adresser formellement à une personne dont on connaît le nom ?", "Du~Sehr geehrte Frau Mayer~Hallo~Mayer", 1,
     "Sehr geehrte Frau suivra du nom est la formule formelle écrite."),
 QC("Quel est le sens de « Auf Wiedersehen » ?", "Bonjour~Au revoir~Merci~S'il vous plaît", 1,
     "C'est la formule d'adieu standard."),
 QC("Quel verbe signifie « pouvoir » et sert à une demande polie ?", "müssen~können~wollen~sollen", 1,
     "Können correspond à pouvoir ; müssen exprime une obligation."),
 QC("Comment demander « Pourriez-vous m'aider ? » ?", "Hilf mir!~Könnten Sie mir helfen?~Ich helfe dir~Du hilfst mir", 1,
     "Könnten Sie est le conditionnel poli."),
 QC("Que signifie « danke schön » ?", "Pardon~Merci beaucoup~Bonjour~Attendez", 1,
     "C'est une formule de remerciement courante."),
 QC("Quel est l'ordre des éléments dans une date allemande ?", "Mois/jour/année~Jour/mois/année~Année/mois/jour~Jour seulement", 1,
     "On écrit par exemple den 12. Mai 2026, jour avant mois."),
 QT("Rédiger une courte présentation de soi en allemand pour un premier échange professionnel.",
     "« Guten Tag, ich heiße Marie Dupont. Ich arbeite als Assistentin im Bereich Verwaltung bei der Firma Beispiel GmbH in Lyon. Ich beschäftige mich vor allem mit der Bearbeitung von Rechnungen und der Betreuung von Kunden. Freut mich, Sie kennenzulernen. » Cette présentation indique le nom, la fonction, l'entreprise et le lieu, puis une activité concrète et une formule de politesse. Elle évite le tutoiement et reste dans un registre formel adapté à un premier contact.",
     "On attend nom, fonction, entreprise, activité et formule de politesse avec Sie."),
 QT("Expliquer l'importance du choix entre du et Sie dans les échanges professionnels allemands.",
     "« Sie » est la forme de politesse utilisée par défaut avec les collègues que l'on connaît peu, les clients et les supérieurs. « Du » marque la proximité et suppose généralement un accord explicite entre les personnes, souvent proposé lors d'un moment informel. Dans le monde professionnel allemand, ce choix est plus marqué qu'en français : passer au du sans y être invité peut être perçu comme un manque de respect, en particulier envers un supérieur ou un client plus âgé. Le pronom choisi entraîne aussi des formes verbales et des possessifs différents, donc toute la phrase s'en trouve modifiée. La règle prudentielle est de commencer avec Sie et de laisser l'interlocuteur proposer le passage au du.",
     "On oppose distance respectueuse et proximité, avec une règle pratique et les conséquences grammaticales.")],
C("L'allemand professionnel s'appuie sur des formules formelles et sur le choix du pronom de politesse Sie.",
  "Guten Tag / Guten Morgen · Sehr geehrte Frau… · Auf Wiedersehen",
  "Könnten Sie…? = demande polie · Sie = distance respectueuse",
  "Begrussung~Guten Tag oder Morgen~Anrede~Sehr geehrte Frau~Hoflichkeit~Koennten Sie~Danken~Danke schoen~Verabschiedung~Auf Wiedersehen",
  "Choisir la formule selon l'heure|Employer Sie par défaut|Formuler avec Könnten|Vérifier la date et les noms|Relier la prononciation",
  "Tutoyer sans invitation|Oublier la majuscule des noms|Confondre können et müssen|Employer une formule familière",
  "Guten Tag~Salut dans la journee~Sehr geehrte Frau Mayer~Appel formel~Koennnten Sie~Demande polie~12. Mai 2026~Date jour puis mois",
  "Du~Proximite~Sie~Politesse et distance",
  "Können~Pouvoir~Müssen~Devoir"))

# ============================================================ EP1
add("EP1", "L'entreprise et son environnement économique et juridique", "Environnement professionnel", ["2nde pro", "1re pro"],
S("L'entreprise est une organisation qui mobilise des ressources pour produire des biens ou des services destinés à un marché."
  "|Elle poursuit plusieurs objectifs : créer de la valeur, satisfaire ses clients, assurer sa pérennité et rémunérer ses parties prenantes."
  "|Les parties prenantes sont les salariés, les clients, les fournisseurs, les actionnaires, les collectivités et l'État."
  "|Les grandes fonctions de l'entreprise sont la recherche et développement, la production, les achats, la commercialisation, la finance et les ressources humaines."
  "|Ces fonctions sont interdépendantes : une décision commerciale a des effets sur la production, la trésorerie et les effectifs."
  "|L'entreprise individuelle est créée par une seule personne, qui exerce son activité en son nom propre."
  "|Dans une société à responsabilité limitée, ou SARL, les associés ne répondent des dettes qu'à hauteur de leurs apports."
  "|La société anonyme, ou SA, fait appel à des actionnaires et peut être cotée en bourse lorsqu'elle est ouverte au public."
  "|Le chef d'entreprise doit choisir un statut juridique adapté au nombre d'associés, au niveau de responsabilité et à la fiscalité."
  "|L'environnement proche comprend les clients, les fournisseurs, les concurrents et les partenaires financiers."
  "|L'environnement général regroupe les facteurs économiques, juridiques, sociaux, technologiques et environnementaux, résumés par l'acronyme PESTEL."
  "|L'assistant de gestion doit connaître cet environnement pour situer son organisation et comprendre les décisions prises."),
[QC("Quel est l'objectif principal d'une entreprise ?", "Distribuer des dividendes uniquement~Créer de la valeur et satisfaire ses clients~Réduire ses effectifs~Éviter tout impôt", 1,
     "La création de valeur et la satisfaction client conditionnent la pérennité."),
 QC("Qui fait partie des parties prenantes ?", "Les seuls actionnaires~Les salariés, clients, fournisseurs et collectivités~Le gouvernement seul~Les concurrents seuls", 1,
     "Les parties prenantes sont tous les acteurs qui influencent ou subissent l'activité."),
 QC("Quelle forme juridique limite la responsabilité aux apports ?", "L'entreprise individuelle~La SARL~L'artisanat~La micro-entreprise", 1,
     "En SARL, le patrimoine personnel des associés est protégé, sauf faute de gestion."),
 QC("Quel acronyme résume l'environnement général ?", "SWOT~PESTEL~4P~BFR", 1,
     "PESTEL signifie Politique, Économique, Social, Technologique, Écologique et Légal."),
 QC("Quel acteur appartient à l'environnement proche ?", "Le taux d'inflation~Un fournisseur~La législation du travail~Le climat", 1,
     "Le fournisseur entretient une relation directe avec l'entreprise."),
 QC("Quelle fonction gère les embauches et la paie ?", "La production~Les ressources humaines~Les achats~La commercialisation", 1,
     "Les ressources humaines recrutent, forment et administrent le personnel."),
 QC("Pourquoi les fonctions de l'entreprise sont-elles interdépendantes ?", "Parce qu'elles sont toutes au même étage~Parce qu'une décision en affecte d'autres~Parce qu'elles ont le même budget~Parce qu'elles n'ont aucun lien", 1,
     "Une décision commerciale influence la production et la trésorerie, par exemple."),
 QT("Expliquer le rôle de l'assistant de gestion dans la connaissance de l'environnement de l'entreprise.",
     "L'assistant de gestion reçoit et traite des informations provenant de l'environnement proche : commandes clients, factures fournisseurs, contrats, réclamations et documents sociaux. Il contribue à l'environnement général en suivant les évolutions réglementaires, fiscales ou sociales qui affectent l'activité, par exemple un changement de taux de TVA ou une nouvelle obligation sociale. En consolidant ces informations, il aide le responsable à situer l'organisation face à ses concurrents et à anticiper les échéances. Sa maîtrise des outils bureautiques et de la réglementation lui permet de transformer des données éparses en éléments de décision, tout en respectant la confidentialité.",
     "On relie flux d'information, veille réglementaire, aide à la décision et confidentialité."),
 QT("Une entreprise individuelle se transforme en SARL. Expliquer les conséquences juridiques et pratiques de ce changement.",
     "En entreprise individuelle, le dirigeant engage tout son patrimoine personnel pour les dettes de l'activité. En SARL, il devient associé et sa responsabilité est limitée au montant de ses apports, sauf faute de gestion ou caution personnelle. La transformation impose plusieurs démarches : rédaction des statuts, apport des actifs et passifs à la nouvelle société, immatriculation au registre du commerce, nouvelle comptabilité et information des partenaires. Le régime fiscal et social change également, avec notamment la distinction entre rémunération du dirigeant et bénéfices de la société. Sur le plan pratique, l'entreprise doit adapter ses documents commerciaux, ses comptes bancaires et ses contrats, et informer clients, fournisseurs et salariés.",
     "On attend responsabilité limitée, démarches juridiques, changement fiscal et information des partenaires.")],
C("L'entreprise est un système de fonctions liées, inséré dans un environnement proche et général qu'il faut connaître pour décider.",
  "Fonctions : production, achats, vente, finance, RH",
  "PESTEL : Politique, Économique, Social, Technologique, Écologique, Légal",
  "Entreprise~Organisation et valeur~Partie prenante~Acteur interne ou externe~Fonction~Role specialise~Environnement proche~Clients et fournisseurs~PESTEL~Facteurs generaux~Statut juridique~Responsabilite",
  "Identifier le secteur et le statut|Repérer les fonctions|Cartographier les parties prenantes|Analyser l'environnement PESTEL|Relier aux décisions",
  "Confondre environnement proche et général|Ignorer les autres fonctions|Croire que la responsabilité est toujours illimitée|Oublier la veille réglementaire",
  "SARL~Responsabilite aux apports~PESTEL~Six facteurs generaux~Fournisseur~Environnement proche~Ressources humaines~Embauche et paie~Information~Confidentialite",
  "Environnement proche~Relations directes~Environnement general~Facteurs macroeconomiques",
  "Entreprise individuelle~Responsabilite illimitee~SARL~Responsabilite limitee"))

# ============================================================ EP2
add("EP2", "Le marché du travail, l'emploi et la formation", "Environnement professionnel", ["1re pro", "Terminale pro"],
S("Le marché du travail met en relation une offre de travail, les employeurs, et une demande de travail, les personnes en recherche d'emploi."
  "|Le taux d'activité mesure la part de la population en âge de travailler qui travaille ou cherche un emploi."
  "|Le taux d'emploi rapporte le nombre de personnes occupant un emploi à la population en âge de travailler."
  "|Le taux de chômage est le rapport entre le nombre de chômeurs et la population active, selon les critères de l'Insee et du BIT."
  "|Un chômeur au sens du BIT doit être sans emploi, disponible et avoir recherché activement un emploi au cours des dernières semaines."
  "|Le chômage peut être conjoncturel, lié à la baisse d'activité, structurel, lié à une inadéquation des compétences, ou frictionnel, lié au temps de recherche."
  "|Les secteurs qui recrutent connaissent des tensions when les compétences disponibles ne correspondent pas aux besoins des employeurs."
  "|La formation professionnelle initiale, comme le baccalauréat professionnel, prépare à un métier et favorise l'insertion."
  "|La formation continue permet aux salariés d'actualiser leurs compétences ou de se reconvertir au cours de leur vie professionnelle."
  "|Le contrat d'apprentissage associe une formation en centre et une expérience en entreprise, avec un statut de salarié apprenti."
  "|Pôle emploi, devenu France Travail, accompagne les demandeurs d'emploi et met en relation les offres et les candidats."
  "|Les compétences numériques et la capacité d'adaptation sont aujourd'hui des atouts transversaux dans la plupart des métiers de la gestion."),
[QC("Que mesure le taux d'activité ?", "La part des chômeurs~La part de la population en âge de travailler qui travaille ou cherche~Le nombre d'entreprises~Le salaire moyen", 1,
     "La population active comprend les personnes employées et celles qui recherchent un emploi."),
 QC("Comment calcule-t-on le taux de chômage ?", "Chômeurs / population totale~Chômeurs / population active~Actifs / population totale~Emplois / entreprises", 1,
     "Le dénominateur est la population active, selon les critères officiels."),
 QC("Quel chômage résulte d'une inadéquation entre compétences et besoins ?", "Conjoncturel~Structurel~Frictionnel~Saisonnier", 1,
     "Le chômage structurel vient d'un décalage durable entre offre et demande de compétences."),
 QC("Quel est un critère du chômeur au sens du BIT ?", "Être sans emploi et disponible~Avoir un diplôme~Habiter en ville~Avoir déjà travaillé", 0,
     "Il faut aussi avoir recherché activement un emploi récemment."),
 QC("Quel dispositif associe formation et travail en entreprise ?", "Le CDD~Le contrat d'apprentissage~La retraite~Le stagecourt", 1,
     "L'apprenti est salarié et suit une formation en centre."),
 QC("Quel organisme accompagne les demandeurs d'emploi ?", "La CNIL~France Travail~Le Conseil d'État~L'Insee", 1,
     "France Travail, anciennement Pôle emploi, gère l'accompagnement et la mise en relation."),
 QC("Quelle compétence est transversale dans les métiers de la gestion ?", "La maîtrise du tableur seulement~La capacité d'adaptation et le numérique~La conduite automobile~La langue latine", 1,
     "Les outils numériques et l'adaptation sont utiles dans tous les postes."),
 QT("Un rapport indique un taux de chômage en baisse. Expliquer pourquoi cette baisse ne signifie pas forcément une amélioration de l'emploi.",
     "Le taux de chômage rapporte le nombre de chômeurs à la population active. Il peut baisser parce que davantage de personnes trouvent un emploi, ce qui est une bonne nouvelle, mais aussi parce que des chômeurs quittent la population active : ils décrochent, partent à la retraite, suivent une formation longue ou se découragent et cessent de rechercher. Dans ce second cas, le nombre d'emplois n'a pas augmenté et l'amélioration est purement statistique. Il faut donc compléter le taux de chômage par le taux d'emploi et par l'évolution du nombre d'emplois, en particulier à temps plein, pour porter un jugement sur la situation du marché du travail.",
     "On explique l'effet dénominateur et la nécessité du taux d'emploi et du volume d'emplois."),
 QT("Comparer les apports du baccalauréat professionnel et de la formation continue pour l'insertion professionnelle.",
     "Le baccalauréat professionnel donne une qualification initiale reconnue, associe enseignements généraux et enseignements professionnels et prépare à l'entrée dans un métier, avec la possibilité de poursuivre en BTS. Il structure un socle de compétences et de méthodes. La formation continue s'adresse à des personnes déjà en emploi ou en reconversion : elle actualise des compétences, répond à un besoin précis de l'entreprise ou permet une mutation vers un autre métier. Elle est plus courte et plus ciblée. Les deux sont complémentaires : le diplôme initial ouvre la porte, la formation tout au long de la vie permet de rester employable face aux évolutions technologiques et organisationnelles.",
     "On oppose qualification initiale et adaptation continue, puis leur complémentarité.")],
C("Le marché du travail se lit avec des taux précis ; l'insertion repose sur une qualification initiale et une formation tout au long de la vie.",
  "Taux de chômage = chômeurs / population active",
  "PESTEL : chômage conjoncturel, structurel, frictionnel",
  "Marche du travail~Offre et demande d'emploi~Population active~Travailleurs et chercheurs~Taux de chomage~Chomeurs sur actifs~Chomage structurel~Inadaptation des competences~Apprentissage~Formation et emploi",
  "Définir les indicateurs|Vérifier les définitions officielles|Repérer le type de chômage|Identifier les dispositifs de formation|Analyser les besoins en compétences",
  "Confondre population active et population totale|Croire qu'une baisse du chômage est toujours bonne|Ignorer le chômage structurel|Négliger la formation continue",
  "Population active~Occupes et chercheurs~Taux de chomage~Chomeurs divisés par actifs~Chomage structurel~Competences inadaptees~France Travail~Accompagnement~Apprenti~Salarie et forme",
  "Chomage conjoncturel~Baisse d'activite~Chomage structurel~Desequilibre durable des competences",
  "Formation initiale~Diplome~Formation continue~Mise a jour des competences"))

# ============================================================ EP3
add("EP3", "La qualité et la relation client", "Environnement professionnel", ["1re pro", "Terminale pro"],
S("La qualité est l'aptitude d'un produit ou d'un service à satisfaire les besoins explicites et implicites du client."
  "|La démarche qualité est une organisation méthodique visant à améliorer en continu les processus et la satisfaction."
  "|La norme ISO 9001 définit les exigences d'un système de management de la qualité, applicable à tous les secteurs."
  "|Les sept principes de la qualité incluent l'orientation client, le leadership, l'implication des personnes et l'amélioration continue."
  "|Un processus est un ensemble d'activités qui transforment une entrée en sortie ; il doit être identifié, mesuré et amélioré."
  "|La méthode PDCA, ou roue de Deming, décrit quatre étapes : Planifier, Faire, Vérifier, Agir."
  "|Un indicateur de qualité doit être pertinent, mesurable, disponible à temps et compris par les équipes."
  "|La relation client commence dès l'accueil : identifier le besoin, orienter, informer et confirmer la suite donnée."
  "|La qualité perçue dépend de la conformité du produit mais aussi du comportement des personnes et de la clarté des informations."
  "|Une réclamation est une opportunité d'amélioration : elle doit être enregistrée, qualifiée, traitée et suivie d'une réponse."
  "|La satisfaction se mesure par des enquêtes, des notes, des taux de réachat et le bouche-à-oreille, en précisant l'échantillon."
  "|L'assistant de gestion contribue à la qualité par la fiabilité des données saisies, le respect des procédures et la traçabilité des échanges."),
[QC("Que désigne la qualité selon l'approche client ?", "Le luxe du produit~L'aptitude à satisfaire les besoins du client~Le prix le plus élevé~La publicité", 1,
     "La qualité se juge au regard des attentes du client, pas seulement du prix."),
 QC("Que définit la norme ISO 9001 ?", "Un système de management de la qualité~Le salaire minimum~Le code du travail~Les délais de paiement", 0,
     "ISO 9001 fixe les exigences d'un système de management de la qualité."),
 QC("Que signifie le A de la méthode PDCA ?", "Analyser~Agir~Annoncer~Archiver", 1,
     "PDCA : Planifier, Faire, Vérifier, Agir ; la dernière étape corrige et améliore."),
 QC("Quel est un critère d'un bon indicateur de qualité ?", "Être complexe~Être mesurable et compris~Être secret~Changer chaque jour", 1,
     "Un indicateur utile est mesurable, disponible et partagé."),
 QC("Comment traiter une réclamation ?", "L'ignorer~L'enregistrer, la qualifier, la traiter et répondre~La supprimer~La transmettre sans suite", 1,
     "Le suivi transformation le litige en amélioration."),
 QC("Quel indicateur mesure la fidélité ?", "Le taux de réachat~Le nombre de salariés~Le chiffre d'affaires~Le taux de TVA", 0,
     "Le taux de réachat et l'ancienneté de la relation traduisent la fidélité."),
 QC("Quel rôle l'assistant de gestion joue-t-il dans la qualité ?", "Valider les normes internationales~Fiabiliser les données et respecter les procédures~Fixer les prix~Contrôler la concurrence", 1,
     "La fiabilité des données et la traçabilité sont ses contributions directes."),
 QT("Décrire l'application de la méthode PDCA à un service d'accueil qui reçoit trop de plaintes sur les délais de réponse.",
     "Planifier : on analyse les plaintes, on mesure le délai moyen de réponse et on fixe un objectif, par exemple répondre en moins de deux minutes. Faire : on met en place une procédure d'accueil, une répartition des appels et une formation courte des agents. Vérifier : on relève les nouveaux délais et le nombre de plaintes pendant un mois, et on compare aux objectifs. Agir : si l'objectif n'est pas atteint, on identifie la cause, par exemple un effectif insuffisant aux heures de pointe, on ajuste les plannings et on recommence le cycle. La boucle PDCA rend l'amélioration continue et fondée sur des données plutôt que sur des impressions.",
     "On décrit les quatre étapes appliquées au cas, avec mesure, action et nouveau cycle."),
 QT("Expliquer pourquoi une réclamation bien traitée peut renforcer la relation client.",
     "Un client qui réclame signale un écart entre son attente et ce qu'il a reçu. Si l'entreprise enregistre la réclamation, répond rapidement, explique la cause et propose une solution, elle montre qu'elle prend le client au sérieux. La réparation, même partielle, restaure souvent la confiance mieux qu'une situation sans problème mais sans preuve d'attention. La réclamation fournit aussi une information précieuse sur un défaut de processus : en la traitant en amont, l'entreprise évite qu'il se reproduise. Enfin, le suivi après résolution et la traçabilité de l'échange montrent un professionnalisme qui peut transformer un client mécontent en client fidèle, à condition que les promesses faites soient effectivement tenues.",
     "On relie écoute, réparation, amélioration du processus et fidélisation.")],
C("La qualité est une démarche continue : on mesure, on corrige et on apprend des réclamations pour mieux satisfaire le client.",
  "PDCA : Planifier, Faire, Vérifier, Agir",
  "Qualité = conformité + perception client · indicateurs mesurables",
  "Qualite~Satisfaction des besoins~ISO 9001~Systeme de management~PDCA~Cycle d'amelioration~Indicateur~Mesure et suivi~Reclamation~Opportunite d'amelioration",
  "Écouter le client|Mesurer le délai et la satisfaction|Planifier une action|Vérifier les résultats|Agir et recommencer le cycle",
  "Ignorer les réclamations|Mesurer sans définir d'objectif|Confondre qualité et luxe|Ne pas tenir les promesses faites",
  "Delai de reponse~Objectif moins de 2 minutes~Plaintes~Indicateur de suivi~PDCA~Quatre etapes~Taux de reachat~Fidelite mesuree",
  "Qualite perçue~Conformite et comportement~Qualite conforme~Respect des specifications",
  "Planifier~Definir l'objectif~Agir~Corriger et ameliorer"))

# ============================================================ EP4
add("EP4", "Le développement durable et la responsabilité sociétale", "Environnement professionnel", ["1re pro", "Terminale pro"],
S("Le développement durable répond aux besoins du présent sans compromettre la capacité des générations futures à répondre aux leurs."
  "|Il repose sur trois piliers indissociables : économique, social et environnemental, auxquels s'ajoute souvent une dimension de gouvernance."
  "|La responsabilité sociétale des entreprises, ou RSE, désigne l'intégration par l'entreprise de préoccupations sociales et environnementales dans son activité."
  "|La RSE s'appuie sur une démarche volontaire, complétée par des obligations légales et des normes internationales."
  "|Les objectifs de développement durable, ou ODD, sont dix-sept objectifs définis par l'ONU dans l'agenda 2030."
  "|L'empreinte carbone mesure les émissions de gaz à effet de serre générées par une activité, directement ou indirectement."
  "|Le bilan carbone recense ces émissions par poste : énergie, transport, achats, déchets et déplacements."
  "|L'économie circulaire vise à réduire le gaspillage en allongeant la durée de vie des produits et en recyclant les matières."
  "|L'éco-conception intègre l'impact environnemental dès la phase de conception d'un produit ou d'un service."
  "|Les achats responsables prennent en compte des critères sociaux et environnementaux dans le choix des fournisseurs."
  "|La transparence et le reporting permettent de publier des indicateurs vérifiables plutôt que des déclarations générales."
  "|L'assistant de gestion contribue à la démarche par la fiabilité des données collectées, le suivi des consommations et le respect des procédures."),
[QC("Quels sont les trois piliers du développement durable ?", "Économique, social, environnemental~Politique, militaire, culturel~Social, fiscal, commercial~Numérique, industriel, agricole", 0,
     "Les trois piliers sont économique, social et environnemental."),
 QC("Que signifie le sigle RSE ?", "Réglementation sanitaire européenne~Responsabilité sociétale des entreprises~Réseau social d'entreprise~Réserve de sécurité économique", 1,
     "La RSE intègre des préoccupations sociales et environnementales dans l'activité."),
 QC("Combien d'objectifs de développement durable l'ONU a-t-elle définis ?", "8~10~17~25", 2,
     "L'agenda 2030 comprend 17 objectifs de développement durable."),
 QC("Que mesure l'empreinte carbone ?", "La consommation d'eau~Les émissions de gaz à effet de serre~Le nombre d'employés~Le chiffre d'affaires", 1,
     "Elle quantifie les émissions directes et indirectes de gaz à effet de serre."),
 QC("Quel est l'objectif de l'économie circulaire ?", "Produire toujours plus~Réduire le gaspillage et recycler les matières~Augmenter les déchets~Supprimer les fournisseurs", 1,
     "Elle allonge la durée de vie des produits et favorise le recyclage."),
 QC("Qu'appelle-t-on éco-conception ?", "Concevoir sans tenir compte de l'impact~Intégrer l'impact environnemental dès la conception~Peindre en vert~Réduire le nombre de réunions", 1,
     "L'impact est pris en compte dès la phase de conception du produit."),
 QC("Quel rôle joue la transparence dans une démarche RSE ?", "Cacher les informations~Publier des indicateurs vérifiables~Réduire les impôts~Supprimer les audits", 1,
     "Des données vérifiables distinguent la démarche réelle du discours."),
 QT("Expliquer pourquoi une démarche RSE ne doit pas se limiter à une action de communication.",
     "Une communication environnementale sans résultats concrets expose l'entreprise à une accusation de greenwashing, qui nuit à sa réputation et peut entraîner des sanctions. Une démarche RSE crédible part d'un diagnostic : identifier les impacts significatifs, hiérarchiser les enjeux, fixer des objectifs mesurables et engager des actions sur les processus, les achats, l'énergie ou les conditions de travail. Elle s'appuie sur des indicateurs suivis dans le temps et sur des rapports vérifiables, avec des responsables identifiés. La communication intervient ensuite pour rendre compte de résultats réels, pas pour les remplacer. Les parties prenantes, salariés, clients et collectivités, jugent la cohérence entre les discours et les pratiques.",
     "On évoque greenwashing, diagnostic, objectifs mesurables, indicateurs et cohérence."),
 QT("Comment l'assistant de gestion peut-il contribuer concrètement à une démarche de développement durable dans son service ?",
     "Il peut d'abord fiabiliser les données : relevés de consommation d'électricité, de papier, de carburant ou de déplacements, en vérifiant les unités et les sources. Il participe à la dématérialisation des documents en respectant les règles de conservation et de confidentialité, et il optimise les impressions et les achats de fournitures. Il peut suivre les échéances et les indicateurs RSE dans un tableur, alerter sur les écarts et préparer les éléments du rapport. Il contribue aussi à l'achat responsable en vérifiant les informations fournies par les fournisseurs et en respectant les procédures de l'organisation. Enfin, sa rigueur et sa traçabilité rendent les résultats vérifiables, ce qui est essentiel pour la crédibilité de la démarche.",
     "On attend fiabilité des données, dématérialisation maîtrisée, suivi d'indicateurs, achats responsables et traçabilité.")],
C("Le développement durable articule trois piliers et impose des actions mesurables, pas de simples déclarations.",
  "Piliers : économique · social · environnemental (+ gouvernance)",
  "ODD : 17 objectifs · empreinte carbone · économie circulaire",
  "Developpement durable~Trois piliers~RSE~Responsabilite societale~ODD~Objectifs de l'ONU~Empreinte carbone~Gaz a effet de serre~Economie circulaire~Recyclage",
  "Identifier les impacts significatifs|Fixer des objectifs mesurables|Collecter des données fiables|Mettre en œuvre les actions|Publier des indicateurs vérifiables",
  "Se limiter à une campagne de communication|Publier des chiffres non sourcés|Confondre RSE et obligationOnly|Ignorer le pilier social",
  "17 ODD~Agenda 2030~Bilan carbone~Emissions par poste~Eco-conception~Impact des la conception~Greenwashing~Discours sans preuve~Donnees~Indicateurs verifies",
  "RSE~Demarche volontaire et obligatoire~Rapport~Compte rendu public des actions",
  "Economie lineaire~Produire et jeter~Economie circulaire~Reduire et recycler"))

# ============================================================ EP5
add("EP5", "La santé, la sécurité au travail et les risques professionnels", "Environnement professionnel", ["1re pro", "Terminale pro"],
S("La santé et la sécurité au travail visent à prévenir les accidents du travail et les maladies professionnelles."
  "|L'employeur a une obligation de sécurité : il doit prendre les mesures nécessaires pour protéger la santé et assurer la sécurité de ses salariés."
  "|Le document unique d'évaluation des risques professionnels, ou DUERP, recense les risques et les mesures de prévention prévues."
  "|Un risque professionnel est la combinaison de la probabilité d'un dommage et de sa gravité pour le salarié."
  "|Les risques physiques comprennent les chutes, les coupures, le bruit, les vibrations et les manutentions manuelles."
  "|Les risques chimiques et biologiques proviennent de produits ou d'agents susceptibles de nuire à la santé."
  "|Les risques psychosociaux incluent le stress, la charge de travail excessive, les conflits et le harcèlement."
  "|La prévention suit une hiérarchie : supprimer le risque, le réduire à la source, puis protéger les personnes et former."
  "|Les équipements de protection individuelle, comme les gants ou les lunettes, sont un dernier recours et doivent être adaptés."
  "|Les salariés ont un droit de retrait lorsqu'ils ont un motif raisonnable de penser que leur situation de travail présente un danger grave et imminent."
  "|Le comité social et économique est consulté sur les questions de santé, de sécurité et de conditions de travail."
  "|En cas d'accident du travail, il faut porter secours, prévenir les services d'urgence, déclarer l'accident et conserver les éléments d'analyse pour éviter la répétition."),
[QC("Quelle est l'obligation principale de l'employeur en matière de sécurité ?", "Une obligation de résultat financier~Une obligation de sécurité~Une obligation de confidentialité seulement~Aucune obligation", 1,
     "L'employeur doit prendre les mesures nécessaires pour protéger la santé des salariés."),
 QC("Que contient le document unique d'évaluation des risques ?", "Les salaires~Le recensement des risques et les mesures de prévention~Le chiffre d'affaires~Les horaires de réunion", 1,
     "Le DUERP est un document obligatoire de prévention, mis à jour régulièrement."),
 QC("Quel est un risque psychosocial ?", "Une chute de hauteur~Le stress lié à la charge de travail~Une coupure~Le bruit", 1,
     "Les risques psychosociaux touchent la santé mentale et les relations de travail."),
 QC("Quelle est la première étape de la hiérarchie de la prévention ?", "Distribuer des gants~Supprimer le risque~Former les salariés~Signaler l'accident", 1,
     "On privilégie la suppression du danger avant la protection individuelle."),
 QC("Quand un salarié peut-il exercer son droit de retrait ?", "Dès qu'il est fatigué~En cas de danger grave et imminent~Pour partir en vacances~Sans motif", 1,
     "Le droit de retrait exige un motif raisonnable de danger grave et imminent."),
 QC("Quel est le rôle du CSE en matière de sécurité ?", "Remplacer l'inspecteur du travail~Être consulté sur les conditions de travail~Fixer les prix~Signer les contrats", 1,
     "Le CSE est l'instance représentative consultée sur la santé et la sécurité."),
 QC("Que faut-il faire immédiatement après un accident du travail ?", "Attendre la fin de la journée~Porter secours et prévenir les secours~Remplir le rapport sans agir~Nettoyer la zone sans trace", 1,
     "L'assistance à la victime et l'alerte aux secours priment, puis vient la déclaration."),
 QT("Expliquer la différence entre prévention collective et prévention individuelle, et pourquoi la première est prioritaire.",
     "La prévention collective agit sur le poste ou l'environnement de travail pour tous les salariés : remplacer un produit toxique, installer une protection mécanique, réduire le bruit à la source ou aménager les horaires. La prévention individuelle repose sur un équipement porté par le salarié, comme des gants, un casque ou des lunettes. La prévention collective est prioritaire parce qu'elle supprime ou réduit le danger pour tous, indépendamment du comportement de chacun, alors que l'équipement individuel peut être mal porté, oublié ou inadapté. Le port d'EPI reste nécessaire lorsque le risque ne peut pas être éliminé, mais il doit s'accompagner de formation, de contrôle et de maintien en état.",
     "On oppose action sur le risque et protection de la personne, puis on justifie la priorité."),
 QT("Dans un service administratif, identifier trois risques professionnels probables et proposer des mesures de prévention.",
     "Trois risques sont fréquents. Le travail sur écran prolongé entraîne des troubles musculo-squelettiques et de la fatigue visuelle : on prévoit un poste réglable, des pauses régulières et une formation aux réglages. La manutention de cartons d'archives et les chutes de papier exposent à des douleurs dorsales ou des chutes : on limite le poids des charges, on utilise des chariots et on dégage les circulations. Le stress et la charge de travail, aggravés par les interruptions et les délais, relèvent des risques psychosociaux : on clarifie les priorités, on organise des plages de concentration et on favorise le dialogue avec le responsable. Ces mesures sont consignées dans le DUERP et réévaluées après tout changement d'organisation.",
     "On identifie trois risques distincts, avec une mesure adapted et une inscription dans le DUERP.")],
C("La prévention des risques repose sur une hiérarchie : supprimer, réduire, protéger et former, avec un document unique tenu à jour.",
  "Risque = probabilité × gravité",
  "Supprimer → réduire → protéger → former · DUERP · droit de retrait",
  "Risque professionnel~Probabilite et gravite~DUERP~Evaluation des risques~Prevention collective~Agir sur le poste~EPI~Protection individuelle~Droit de retrait~Danger grave et imminent",
  "Recenser les risques du poste|Évaluer probabilité et gravité|Choisir la mesure de prévention|Former et informer|Mettre à jour le document unique",
  "Distribuer des gants avant de supprimer le danger|Oublier les risques psychosociaux|Ne jamais mettre à jour le DUERP|Ignorer un danger imminent",
  "Travail sur ecran~Fatigue visuelle~Archives~Manutention et chutes~Stress~Risque psychosocial~EPI~Dernier recours~Droit de retrait~Danger grave",
  "Prevention collective~Pour tous les salaries~Prevention individuelle~Equipement porte",
  "Accident du travail~Secours et declaration~Maladie professionnelle~Reconnue officiellement"))

# FIN DES LOTS
valider_et_ecrire(F, "pro-gestion-mat-part-C.json")
