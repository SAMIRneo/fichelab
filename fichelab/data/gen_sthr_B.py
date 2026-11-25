# -*- coding: utf-8 -*-
"""Generateur sthr-mat-part-B.json — lot B : hebergement, restauration, HACCP, approvisionnement.

20 fiches 'prototype' pour la filiere STHR (1re / Terminale) :
12 points de cours, 9 questions corrigees (7 QCM + 2 texte),
7 blocs en ordre strict, 3 schemas via diag().
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sthr_common import S, R, QC, QT, C, build, valider_et_ecrire

F = []

def add(prefix, titre, mat, ans, points, questions, c):
    questions = list(questions) + EXTRA.get(prefix, [])
    F.append(build(prefix, titre, mat, ans, points, questions, c))

EXTRA = {
 "HO1": [QC("Quel service gere la facturation des clients ?", "L'etage~Le front office~La cuisine~La blanchisserie", 1,
            "La reception etablit et regle la facture du sejour.")],
 "HO2": [QC("Quel canal preleve generalement une commission ?", "Le site officiel de l'hotel~La plateforme en ligne~Le telephone~Le mail direct", 1,
            "Les plateformes sont des canaux indirects retribues par commission.")],
 "HO3": [QC("Que remet la reception au client lors du check-in ?", "La facture~La cle de la chambre~Le menu~Le linge", 1,
            "La cle ou le badge est remis apres l'enregistrement.")],
 "HO4": [QC("Qui declare la chambre disponible dans le PMS ?", "Le client~L'etage apres controle~Le fournisseur~La cuisine", 1,
            "L'etage met a jour le statut apres le controle qualite.")],
 "HO5": [QC("Quelle charge est proportionnelle a l'activite ?", "Le loyer~Le cout de nettoyage par chambre~L'assurance~Le personnel permanent", 1,
            "Le cout de nettoyage varie avec le nombre de chambres occupees."),
         QC("Un tarif non remboursable est generalement...", "Plus cher~Moins cher~Identique~Interdit", 1,
            "Moins de risque pour l'hotel justifie un tarif reduit."),
         QC("Que mesure l'elasticite de la demande ?", "La couleur des prix~La reaction des ventes a une variation de prix~Le nombre d'etoiles~La duree du sejour", 1,
            "L'elasticite mesure la sensibilite des ventes au prix."),
         QC("Pourquoi surveiller la parite tarifaire ?", "Pour augmenter les commissions~Pour garder une image coherente entre canaux~Pour changer de clientele~Pour reduire l'occupation", 1,
            "Des prix discordants entre canaux nuisent a la confiance du client.")],
 "HO6": [QC("Quel est le deuxieme temps du traitement d'une reclamtion ?", "Proposer une remise~Reconnaitre le mecontentement~Appeler le directeur~Remplir un formulaire", 1,
            "On reconnait le probleme avant de proposer une solution."),
         QC("Quel outil pilote la fidelisation ?", "Le PMS seul~Le programme de fidelite~Le bon de commande~Le plan de nettoyage", 1,
            "Le programme de fidelite cree des avantages et encourage le retour."),
         QC("Que faut-il faire apres une reclamtion ?", "Classer sans rien dire~Revenir vers le client pour verifier~Ignorer~Changer de sujet", 1,
            "Le suivi confirme que la solution a ete satisfaisante.")],
 "RE1": [QC("Quel type de restauration sert un groupe identifie ?", "La brasserie~La restauration collective~Le restaurant gastronomique~La restauration rapide", 1,
            "La restauration collective dessert entreprises, ecoles ou hopitaux."),
         QC("Que mesure la rotation des tables ?", "Le prix du menu~Le nombre de couverts par place et par service~La duree de cuisson~Le nombre de fournisseurs", 1,
            "La rotation est le nombre de couverts servis par place pendant un service."),
         QC("Qu'est-ce que la marge brute ?", "Prix de vente plus cout~Prix de vente moins cout des matieres~CA divise par couverts~Charges moins recettes", 1,
            "La marge brute est la difference entre vente et cout des denrees.")],
 "RE2": [QC("Qui accueille les clients et distribue les tables ?", "Le commis~Le maitre d'hotel~Le plongeur~Le chef de cuisine", 1,
            "Le maitre d'hotel gere l'accueil et le plan de service."),
         QC("Que faut-il verifier avant le service ?", "Seulement la lumiere~La vaisselle et le linge~Le prix des vins~La facture", 1,
            "Une rupture de vaisselle en service perturbe toute l'equipe."),
         QC("Comment sont transmises les allergies en salle ?", "Oralement au client~Avec la commande en cuisine~Par la publicite~Aucun besoin", 1,
            "L'information doit accompagner la commande transmise en cuisine.")],
 "RE3": [QC("Quelle technique de service est la plus courante ?", "Le gueridon~L'assiette~La russe~Le buffet", 1,
            "Le service a l'assiette domine en restauration commerciale."),
         QC("Par quel cote presente-t-on habituellement un plat ?", "Par la droite~Par la gauche~Par derriere~Par devant", 1,
            "La convention est de servir par la gauche et de debarrasser par la droite."),
         QC("Quel equipement caractérise le service au gueridon ?", "Un four~Une table roulante avec rechaud~Un lave-vaisselle~Une caisse", 1,
            "Le gueridon est une table roulante munie d'un rechaud.")],
 "RE4": [QC("Quelle boisson est servie des le debut du service ?", "Le cafe~L'eau~Le digestif~Le vin", 1,
            "L'eau est generalement proposee des l'arrivee des clients."),
         QC("Quel verre utilise-t-on pour une biere ?", "Verre a pied~Verre a biere~Verre a digestif~Tasse", 1,
            "Chaque boisson a un verre adapte au service."),
         QC("Quelle obligation reglementaire s'applique a l'alcool ?", "Servir sans limite~Refuser de servir une personne ivre~Vendre a tout age~Ne rien signaler", 1,
            "Le professionnel doit refuser de servir une personne manifestement ivre.")],
 "RE5": [QC("Quel evenement peut donner lieu a un banquet ?", "Un mariage~Une livraison~Un inventaire~Une formation", 0,
            "Mariages, congres et seminaires sont des occasions classiques de banquet."),
         QC("Que doit preciser le cahier des charges ?", "La couleur des nappes seulement~Le nombre de convives, le menu et les horaires~Le prix du pain~La recette", 1,
            "Le cahier des charges fixe les attentes et les contraintes du client."),
         QC("Quel document indique les issues en cas d'urgence ?", "Le menu~Le plan d'evacuation~Le devis~La carte des vins", 1,
            "Le plan d'evacuation doit etre affiche et connu de l'equipe.")],
 "HY1": [QC("Quel texte europeen impose la demarche HACCP ?", "Le code civil~Le reglement (CE) 852/2004~Le code de la route~Le reglement RGPD", 1,
            "Le reglement 852/2004 relatif a l'hygiene des denrees est la base de la demarche."),
         QC("A quoi sert la verification dans le systeme HACCP ?", "A vendre plus~A controler l'efficacite globale du systeme~A remplacer la surveillance~A fermer l'etablissement", 1,
            "La verification porte sur l'ensemble du systeme, pas sur un seul point.")],
 "HY2": [QC("Que signifie le sigle DLC ?", "Date de livraison commandee~Date limite de consommation~Date de fabrication~Date de commande", 1,
            "La DLC est la date limite de consommation, au-delà de laquelle le produit ne doit pas etre servi."),
         QC("Comment mesurer la temperature au coeur d'un plat ?", "A l'oeil~Avec un thermometre propre et etalonné~Au toucher~Avec le doigt", 1,
            "Un thermometre propre et etalonné est le seul outil fiable.")],
 "HY3": [QC("Quel produit agit sur les graisses et salissures ?", "Un desinfectant~Un detergent~Un antibiotique~Un conservateur", 1,
            "Le detergent nettoie ; le desinfectant agit ensuite sur les micro-organismes."),
         QC("Que faire apres le nettoyage d'une surface ?", "Rincer immediatement~Desinfecter en respectant le temps de contact~Emballer~Servir", 1,
            "La desinfection n'est efficace que si le temps de contact est respecte."),
         QC("Ou stocker les produits chimiques ?", "En cuisine~Dans un local separe des denrees~Dans le frigo~Sur le plan de travail", 1,
            "Les produits d'entretien ne doivent jamais etre stockes avec les denrees.")],
 "HY4": [QC("A qui l'information sur les allergenes doit-elle etre fournie ?", "Seulement a la cuisine~Au client, avant sa commande~Au fournisseur~Au comptable", 1,
            "Le client doit pouvoir consulter l'information avant de choisir son plat."),
         QC("Que faire si un client presente des symptomes graves ?", "Attendre~Prevenir les secours et arreter le service~Donner un dessert~Changer de table", 1,
            "Une urgence medicale impose d'appeler les secours sans attendre."),
         QC("Que conserver pour assurer la traçabilite ?", "Les menus~Les etiquettes et bons de livraison~Les avis clients~Les plannings seuls", 1,
            "Les documents de reception permettent de retrouver le lot d'un produit.")],
 "HY5": [QC("Quel geste est fondamental contre la contamination ?", "Porter des gants toute la journee~Le lavage des mains~Changer de blouse~Ouvrir les fenetres", 1,
            "Le lavage des mains, repete aux bons moments, reste la premiere barriere."),
         QC("Que faire d'une plaie non protegeable ?", "La panser avec du metal~Continuer avec des gants~Retirer la personne de la manipulation~L'ignorer", 2,
            "Une plaie non protegeable interdit la manipulation de denrees."),
         QC("Qui doit connaitre l'emplacement de la trousse de secours ?", "Le directeur seul~Toute l'equipe~Le fournisseur~Personne", 1,
            "En cas d'urgence, chaque membre doit savoir ou se trouvent les premiers secours.")],
 "AP1": [QC("Quels services expriment le besoin en linge et vaisselle ?", "La comptabilite~L'etage et la salle~Le fournisseur~La direction seule", 1,
            "L'etage demande le linge et la salle demande la vaisselle."),
         QC("Que permet le referencement des fournisseurs ?", "Augmenter les prix~Garantir un niveau de qualite homogene~Supprimer les commandes~Reduire les stocks a zero", 1,
            "La liste des fournisseurs agrees securise la qualite des achats."),
         QC("Que faire d'une facture non conforme ?", "La payer directement~La comparer aux bons et la contester~La jeter~La signer sans lire", 1,
            "Le controle des trois documents permet de detecter et contester l'erreur.")],
 "AP2": [QC("Quel inventaire compte toutes les references en fin d'exercice ?", "L'inventaire tournant~L'inventaire permanent~L'inventaire general~L'inventaire partiel", 2,
            "L'inventaire general est un comptage complet, souvent annuel."),
         QC("Un ecart d'inventaire peut provenir de...", "Une hausse de TVA~Une erreur de saisie~Un nouveau menu~Une formation", 1,
            "Erreurs de saisie, vols et pertes expliquent les ecarts.")],
 "AP3": [QC("Quel taux rapporte la marge au prix de vente ?", "Le taux de marge~Le taux de marque~Le food cost~La rotation", 1,
            "Le taux de marque se calcule sur le prix de vente."),
         QC("Qu'est-ce que le price eating ?", "La baisse des prix~La hausse du prix des matieres~La vente promotionnelle~Le gaspillage", 1,
            "Le price eating designe l'augmentation du cout d'achat des denrees."),
         QC("A quelle frequence suivre le food cost ?", "Une fois par an~Chaque semaine~Tous les dix ans~Jamais", 1,
            "Un suivi hebdomadaire permet de corriger rapidement les derives.")],
 "AP4": [QC("Quelle filiere valorise les dechets organiques ?", "La mise en decharge~Le compostage~L'incineration sans tri~Le stockage", 1,
            "Le compostage et la methanisation valorisent la matiere organique."),
         QC("Quel indicateur mesure le gaspillage ?", "Le nombre de clients~Le poids des dechets~Le prix du menu~La note client", 1,
            "La pesee des dechets est l'indicateur de base."),
         QC("Quel levier reduit les restes d'assiettes ?", "La couleur des assiettes~La taille des portions~Le nombre de serviettes~La musique", 1,
            "Adapter les grammages aux besoins reels limite les restes."),
         QC("A quoi sert la prevision de frequentation ?", "A fixer les horaires~A ajuster les commandes~A changer la carte~A supprimer les stocks", 1,
            "Mieux prevoir permet de commander au plus juste.")],
}

# ============================================================ HO1
add("HO1", "Organisation d'un hôtel et répartition des services", "Sciences et technologies des services", ["1re"],
S("Un etablissement hotelier est une entreprise de service qui fournit un hebergement payant et des prestations associees."
  "|L'organisation repose sur deux grands pôles : l'hebergement, avec la reception et l'etage, et la restauration, avec la cuisine et la salle."
  "|Le directeur d'etablissement dirige l'ensemble, gere le budget, la qualite et la relation avec la propriete."
  "|Le front office assure la reservation, l'accueil, l'enregistrement des arrives, la facturation et le depart des clients."
  "|Le departement de l'etage, ou housekeeping, entretient les chambres et les parties communes selon des normes de proprete."
  "|La cuisine est dirige par le chef de cuisine, qui construit la carte, gere les commandes, la production et l'hygiene."
  "|Le service de salle est dirige par le maitre d'hotel, qui organise le service, les reservations et la relation avec la clientele."
  "|Les services generaux regroupent la maintenance, le nettoyage, la securite, la blanchisserie et la gestion des fournitures."
  "|Les equipes de nuit et le service de reservation assurent la continuite de l'activite hors des horaires habituels."
  "|L'organigramme represente les liens d'autorite, les responsabilites et les circuits de communication entre les services."
  "|La qualite de service depend de la coordination : un retard de nettoyage d'une chambre decale l'arrivee du client suivant."
  "|La classification de 1 a 5 etoiles repond a des criteres normes portant sur le confort, les equipements et les services proposes."),
[QC("Quel departement assure l'enregistrement des arrives ?", "L'etage~Le front office~La cuisine~La maintenance", 1,
     "La reception, ou front office, gere l'arrivee, le sejour et le depart du client."),
 QC("Qui dirige le service de cuisine ?", "Le maitre d'hotel~Le chef de cuisine~Le directeur de la reception~L' intendant", 1,
     "Le chef de cuisine est responsable de la production culinaire et de l'hygiene."),
 QC("Que designe le housekeeping ?", "La comptabilite~L'entretien des chambres~La reservation~Le service des boissons", 1,
     "Le housekeeping est le service d'entretien de l'etage et des parties communes."),
 QC("Que represente un organigramme ?", "Le plan des prix~Les liens d'autorite et de communication~Le menu du jour~Le bilan comptable", 1,
     "L'organigramme represente la structure hierarchique et les relations entre services."),
 QC("Quel service intervient lorsque la climatisation d'une chambre tombe en panne ?", "La reception~La maintenance~La cuisine~La comptabilite", 1,
     "La maintenance, ou service technique, intervient sur les equipements."),
 QC("Combien de niveaux de classification hoteliere existe-t-il en France ?", "3~4~5~6", 2,
     "La classification francaise compte cinq categories, d'une a cinq etoiles."),
 QT("Expliquer pourquoi la coordination entre la reception et l'etage est determining pour la qualite du service.",
     "La reception vend et attribue une chambre, mais c'est l'etage qui la rend disponible et propre. Si l'etage n'est pas informe d'un depart anticipe ou d'une arrivee anticipee, la chambre n'est pas prete a l'heure : le client attend, la reception doit s'excuser et l'image de l'etablissement se degrade. Une bonne coordination repose sur des outils communs : etat des chambres, priorites de nettoyage, communication des arrivals et des departs, et procedures en cas de retard. Elle permet aussi d'optimiser le taux d'occupation en sachant exactement quelles chambres sont commercialisables. La qualite de service n'est donc pas l'affaire d'un seul departement mais d'un processus transversal.",
     "On attend le lien entre vente et disponibilite, les outils de communication et la consequence pour le client."),
 QT("Decrire les principales fonctions d'un hotel et montrer comment elles contribuent a la valeur du sejour.",
     "La reception gere la reservation, l'accueil, l'attribution de la chambre, la facturation et les demandes du client. L'etage assure la propreté et le comfort de la chambre, ce qui est souvent le premier critere de satisfaction. La cuisine et la salle proposent les repas et creent des recettes complementaires. Les services generaux garantissent le fonctionnement technique, la securite et les approvisionnements. Enfin, la direction coordonne les budgets, la qualite et la strategie commerciale. Chaque fonction contribue a la valeur perçue par le client : un sejour reussi resulte de la somme de prestations coherentes et ponctuelles.",
     "On attend l'enumeration des fonctions et le lien explicite avec la valeur et la satisfaction client.")],
C("Un hotel est un systeme de services imbriques : la valeur du sejour depend de la coordination des pôles.",
  "Hotel = hebergement + restauration + services generaux",
  "Front office · housekeeping · cuisine · salle · maintenance",
  "Front office~Accueil et facturation~Reservation~Etage~Entretien des chambres~Proprete~Cuisine~Production des plats~Chef~Salle~Service et relation client~Maitre d'hotel~Maintenance~Technique et securite",
  "Identifier les besoins du client|Repartir les taches entre services|Organiser les flux d'information|Coordonner les plannings|Controler la qualite et corriger",
  "Ignorer le service de nuit|Confondre reception et etage|Ne pas communiquer les arrives|Croire que la qualite depend d'un seul service",
  "5 etoiles~Classification maximale~Check-in~Arrivee du client~Housekeeping~Nettoyage~Organigramme~Structure hierarchique",
  "Reception~Vend la chambre~Etage~Rend la chambre disponible",
  "Cuisine~Produit les plats~Salle~Les sert au client"))

# ============================================================ HO2
add("HO2", "Réservation et gestion des disponibilités", "Sciences et technologies des services", ["1re", "Terminale"],
S("La reservation est un contrat par lequel l'hotel s'engage a mettre une chambre a disposition a une date donnee."
  "|Elle peut etre directe, par telephone, mail ou site de l'hotel, ou indirecte, par une agence ou une plateforme en ligne."
  "|Le canal de reservation determine le cout d'acquisition : une plateforme preleve une commission sur chaque nuit venvue."
  "|Le booking engine est le moteur de reservation en ligne connecte au systeme de gestion de l'etablissement, ou PMS."
  "|Le PMS centralise les disponibilites, les tarifs, les arrives, les departs et la facturation."
  "|Une chambre est disponible lorsqu'elle est propre, non reserve et non bloquee pour maintenance."
  "|Le taux d'occupation rapporte le nombre de chambres occupees au nombre de chambres disponibles sur une periode."
  "|Le RevPAR, ou revenu par chambre disponible, vaut taux d'occupation multiplie par le prix moyen de la chambre."
  "|Le surbooking consiste a vendre plus de chambres que la capacite : il peut etre volontaire mais expose a des refus d'hebergement."
  "|Une reservation garantie exige souvent une carte bancaire ou un depot, ce qui reduit le risque de no-show."
  "|Le no-show designe un client reserve qui ne se presente pas : il entraine une perte de revenu et une chambre inutilisee."
  "|La procedure de reservation comprend la verification des dates, du type de chambre, du tarif, des conditions et de l'identite du client."),
[QC("Quel outil centralise disponibilites et tarifs dans un hotel ?", "Un tableur seul~Le PMS~Le site de la ville~Le registre des clients", 1,
     "Le property management system gere les disponibilites, les reservations et la facturation."),
 QC("Que designe un no-show ?", "Un client qui arrive en avance~Un client reserve qui ne vient pas~Une chambre en reparation~Une reservation annulee la veille", 1,
     "Le no-show est l'absence d'un client ayant reserve."),
 QC("Comment calculer le RevPAR ?", "Taux d'occupation divisé par prix moyen~Taux d'occupation multiplie par prix moyen~Prix moyen moins taux~Chambres occupees plus chambres vides", 1,
     "RevPAR = taux d'occupation × prix moyen de la chambre."),
 QC("Quel risque presente le surbooking ?", "Un prix trop bas~Un refus d'hebergement~Une hausse du RevPAR~Une chambre vide", 1,
     "Vendre plus que la capacite peut obliger a refuser un client."

 ) ,
 QC("Quel moyen reduction le risque de no-show ?", "Une reservation non garantie~Une carte bancaire ou un depot~Un tarif plus bas~Une simple note", 1,
     "Une garantie financiere engage le client et limite l'absence."),
 QC("Quelle est une source de reservation indirecte ?", "Le site officiel de l'hotel~Une plateforme en ligne~Le telephone de la reception~Le mail direct", 1,
     "Les plateformes et les agences sont des canaux indirects, avec commission."),
 QT("Un hotel de 100 chambres vend 72 chambres a 150 € en moyenne. Calculer le taux d'occupation et le RevPAR.",
     "Le taux d'occupation vaut 72 / 100 = 0,72, soit 72 %. Le RevPAR est le produit de ce taux par le prix moyen : 0,72 × 150 = 108 € par chambre disponible et par nuit. Le chiffre d'affaires d'hébergement correspondant est de 72 × 150 = 10 800 €. Ces indicateurs se completent : le taux mesure le volume vendu et le RevPAR mesure la qualite commerciale de la vente, car un hotel peut avoir un fort taux avec un prix trop faible et un RevPAR mediocre.",
     "On attend 72 %, RevPAR 108 € et l'interpretation complementaire des deux indicateurs."),
 QT("DeCrire la procedure de gestion d'une reservation du debut a la fin.",
     "On releve d'abord les dates, le nombre de nuits, le type de chambre, le nombre de personnes et les exigences particulieres. On verifie la disponibilite dans le PMS, on annonce le tarif et les conditions d'annulation, puis on demande une garantie. On enregistre la reservation en indiquant la source du canal, on envoie une confirmation ecrite avec le detail du sejour. La veille de l'arrivee, on controle le depot, l'heure d'arrivee et la préparation de la chambre avec l'etage. Le jour meme, on enregistre le client, on lui attribue la chambre puis on met a jour l'etat des lieux dans le PMS. Enfin, toute modification ou annulation est tracee.",
     "On attend demande, verification, garantie, confirmation, préparation, check-in et traçabilite.")],
C("La reservation est un engagement contractuel gere par le PMS : disponibilite, tarif et garantie determination le revenu.",
  "RevPAR = taux d'occupation × prix moyen",
  "Taux d'occupation = chambres vendues / chambres disponibles",
  "Reservation~Contrat de sejour~PMS~Gestion centralisee~Disponibilite~Chambre propre et libre~Canal direct~Site ou telephone~Canal indirect~Plateforme avec commission~No-show~Absence non annulee",
  "Relever dates et besoins|Verifier la disponibilite|Confirmer tarif et conditions|Prendre une garantie|Envoyer la confirmation et préparer l'arrivee",
  "Vendre sans verifier la disponibilite|Oublier les conditions d'annulation|Confondre occupation et RevPAR|Ne pas tracer les modifications",
  "100 chambres~Capacite~72 vendues~Occupation 72 %~150 €~Prix moyen~108 €~RevPAR",
  "Canal direct~Sans commission~Canal indirect~Avec commission",
  "Taux d'occupation~Volume vendu~RevPAR~Qualite commerciale"))

# ============================================================ HO3
add("HO3", "Accueil, check-in et check-out du client", "Sciences et technologies des services", ["1re"],
S("L'accueil est le premier contact physique ou telephonique entre le client et l'etablissement : il donne le ton du sejour."
  "|Les regles d'accueil imposent une posture professionnelle : se lever, regarder le client, sourire et se presenter."
  "|Le check-in est l'enregistrement de l'arrivee : verification de l'identite, attribution de la chambre et remise de la cle."
  "|Une piece d'identite valide est demandee ; pour un etranger, le passeport et le visa eventuel sont verifies."
  "|La fiche de police, obligatoire dans les hotels francais, doit etre remplie et conservee selon la reglementation."
  "|Le client peut formuler des preferences : chambre calme, lit twin, etage eleve ou arrival anticipatee."
  "|En cas d'arrivee avant l'heure de mise a disposition, la reception doit verifier la disponibilite aupres de l'etage."
  "|Le check-out est la procedure de depart : retour de la cle, verification de la chambre, facture et reglement."
  "|Le depart tardif, ou late check-out, doit etre negocie selon l'occupation du jour et faire l'objet d'une trace."
  "|La facture doit faire apparaitre le detail des prestations, la TVA et le mode de paiement."
  "|Les incidents sont notes dans le PMS et transmis a l'equipe suivante pour assurer la continuite du service."
  "|Un accueil reussi combine efficacite administrative, courtoisie et capacite a traiter les imprévus sans tension."),
[QC("Que faut-il verifier lors du check-in ?", "La couleur de la valise~L'identite du client~Son gout musical~Sa taille", 1,
     "La verification de l'identite est obligatoire avant l'attribution d'une chambre."),
 QC("Quel document est_specifique aux hotels francais ?", "Le passeport~La fiche de police~Le recu de caisse~Le contrat de bail", 1,
     "La fiche de police doit etre remplie pour les clients d'un etablissement hotelier."),
 QC("Que designe un late check-out ?", "Un depart avant l'heure~Un depart apres l'heure prevue~Une arrivee anticipe~Une nuit supplementaire offerte", 1,
     "Le late check-out est un depart tardif accorde selon les disponibilites."),
 QC("Quel element doit figurer sur la facture ?", "Le detail des prestations et la TVA~L'avis Google~La recette du petit-dejeuner~Le planning de l'equipe", 0,
     "La facture est un document legal qui detaille les prestations et la TVA."),
 QC("Comment reagir face a un client arrive avant l'heure ?", "Refuser sans explication~Verifier la disponibilite aupres de l'etage~Donner une chambre sale~Ignorer la demande", 1,
     "On contacte l'etage pour savoir si une chambre est deja prete."),
 QC("A qui transmettons les incidents de reception ?", "Personne~A l'equipe suivante via le PMS~Au fournisseur~Au client suivant", 1,
     "La trace dans le PMS assure la continuite du service."),
 QT("Decrire le deroulement ideal d'un check-in et les points de vigilance.",
     "Le client est accueilli debout, avec un sourire et une formule de bienvenue. On verifie la reservation, l'identite et les documents requis, puis on confirme la duree du sejour, le tarif et les conditions. On propose la chambre en precisant son emplacement et l'heure du petit-dejeuner, on remet la cle ou le badge, et on demande si le client a une question. Les points de vigilance sont : une piece manquante, une arrivée tres tardive, une demande particuliere non satisfaite et une erreur de tarif. Chaque element est trace dans le PMS, et tout probleme est signale a l'etage ou au responsable.",
     "On attend les etapes et les points de vigilance : identite, tarif, disponibilite et traçabilite."),
 QT("Un client souhaite partir a 16 h alors que le depart est fixe a 11 h et que l'hotel est complet. Comment repondre ?",
     "On ne peut pas promettre le maintien de la chambre : comme l'hotel est complet, l'etage doit la preparer pour le prochain arrive. On explique poliment la situation et on propose des solutions : conservation des bagages a la reception, acces a une salle d'eau ou a un espace de travail, ou réservation d'une chambre supplémentaire si elle est disponible. On peut egalement proposer un service payant de depart tardif uniquement si la chambre n'est pas reengagee. La reponse doit rester courtoise, claire et conforme a la realite du planning, afin de ne pas creer d'attente de la part du client.",
     "On attend une reponse polie, la verite sur la disponibilite et des alternatives concretes.")],
C("L'accueil est un processus en deux temps : enregistrer le client a l'arrivee, regler et liberer la chambre au depart.",
  "Check-in = identite + chambre + cle",
  "Check-out = cle + etat des lieux + facture",
  "Accueil~Premier contact~Posture~Debout et souriant~Check-in~Enregistrement arrivee~Fiche de police~Document obligatoire~Check-out~Procedure de depart~Facture~Detail et TVA~Late check-out~Depart tardif",
  "Accueillir et se presenter|Verifier reservation et identite|Attribuer la chambre et remettre la cle|Suivre le client pendant le sejour|Regler et tracer le depart",
  "S'asseoir sans accueillir|Oublier la fiche de police|Promettre une chambre non disponible|Ignorer les incidents dans le PMS",
  "11 h~Heure de depart standard~16 h~Demande tardive~TVA~Mention obligatoire~PMS~Tracabilite",
  "Check-in~Debut du sejour~Check-out~Fin du sejour",
  "Arrivee anticipe~A verifier avec l'etage~Depart tardif~A negocier"))

# ============================================================ HO4
add("HO4", "Entretien des chambres et qualité de l'hébergement", "Sciences et technologies des services", ["1re"],
S("L'entretien des chambres, ou housekeeping, vise a garantir la propreté, le confort et la securite de l'espace de vie du client."
  "|Le planning de l'etage repartit les chambres selon les priorites : departs, arrives, chambres en attente et chambres occupees."
  "|La femme de chambre, ou valet de chambre, nettoie la chambre, change le linge et verifie le bon fonctionnement des equipements."
  "|Le nettoyage suit un ordre logique : haut vers bas, sale vers propre, et fin par la salle de bain."
  "|Le linge propre est stocke a l'ecart du linge sale : cette separation evite les contaminations croisees."
  "|La checklist de chambre recense les points a controler : lit, sanitaires, sol, poubelles, serviettes et amenites."
  "|La durée moyenne de nettoyage d'une chambre conditionne la capacite de l'hotel a accepter des arrives anticipees."
  "|Une chambre est dite « libre propre » lorsqu'elle a ete nettoyee, controlee et declaree disponible dans le PMS."
  "|Le controle qualite est effectue par une responsable d'etage ou par le gestionnaire avant la remise de la chambre."
  "|Les objets oublies par les clients sont enregistres, conserves et restitues selon une procedure precise."
  "|Les produits d'entretien doivent etre conforme aux regles de securite et utilises avec les equipements de protection adapts."
  "|La qualite perçue de l'etage est souvent le premier critere de satisfaction : une chambre propre peut compenser d'autres imperfections."),
[QC("Quel ordre de nettoyage est recommande ?", "Bas vers haut~Haut vers bas~Sale vers propre au hasard~Sans ordre precis", 1,
     "On nettoie du haut vers le bas et du sale vers le propre pour éviter de resalir."),
 QC("Qu'appelle-t-on une chambre « libre propre » ?", "Une chambre vide non nettoyee~Une chambre nettoyee et disponible~Une chambre occupee~Une chambre en panne", 1,
     "Elle est propre, controlee et commercialisable dans le PMS."),
 QC("Qui effectue habituellement le controle qualite d'une chambre ?", "Le client~La responsable d'etage~Le fournisseur~Le comptable", 1,
     "Une responsable d'etage ou un gestionnaire valide la chambre avant sa remise."),
 QC("Comment gerer un objet oublie ?", "Le jeter~L'enregistrer et le conserver selon la procedure~Le garder pour soi~Le donner au client suivant", 1,
     "Les objets trouves sont enregistres, conserves et restitues sur demande."),
 QC("Pourquoi separer linge propre et linge sale ?", "Pour gagner du temps~Pour eviter les contaminations croisees~Pour reduire les couts~Pour changer de couleur", 1,
     "La separation empeche le transfert de salissures et de micro-organismes."),
 QC("Quel document liste les points a controler dans une chambre ?", "La facture~La checklist~Le bilan~La carte", 1,
     "La checklist de chambre est un outil de controle de qualite."),
 QT("Expliquer comment le planning de l'etage influe sur le taux d'occupation et la satisfaction.",
     "Le planning classe les chambres par priorite : departs d'abord, puis arrives, puis chambres en attente. S'il est mal organise, une chambre libre ne sera pas prete a temps, la reception ne pourra pas la vendre et le client devra attendre : cela diminue le revenu et la satisfaction. Un planning precis, mis a jour en temps reel avec le PMS, permet de savoir a chaque instant quelles chambres sont commercialisables. Il faut aussi prevoir les imprévus : depart tardif, panne, chambre supplementaire demandee. Une equipe dimensionnee correctement et une checklist de controle garantissent la qualite sans bloquer les arrives.",
     "On attend le lien planning, disponibilite commerciale et satisfaction client."),
 QT("Detailler les etapes du nettoyage d'une chambre de facon hygiene et methodique.",
     "On commence par aerer et relever les poubelles, puis on degarnit le lit et on retire le linge sale en lePLACant directement dans un sac. On depoussierres les surfaces du haut vers le bas, on nettoie la salle de bain avec les produits adapts, puis on refait le lit avec du linge propre et on dispose les serviettes et amenites. On passe ensuite l'aspirateur et on lave le sol en terminant par la porte. Avant de quitter la chambre, on verifie les equipements, la lumiere, la fermeture des fenêtres et on complete la checklist. Enfin, on declare la chambre propre dans le PMS pour la reception.",
     "On attend ordre methodique, separation du linge, controle final et mise a jour du PMS.")],
C("Le housekeeping est un processus de production de propreté : methode, checklist et communication avec la reception.",
  "Chambre libre propre = nettoyee + controlee + disponible",
  "Haut vers bas · sale vers propre · linge sale separe",
  "Housekeeping~Entretien de l'etage~Checklist~Controle de qualite~Linge sale~Contamination a eviter~PMS~Mise a jour du statut~Priorite~Departs puis arrives~Controle~Validation par la responsable",
  "Consulter le planning des arrives|Trier les chambres par priorite|Nettoyer selon la methode|Controler avec la checklist|Declarer la chambre disponible",
  "Nettoyer dans le désordre|Mélanger linge propre et sale|Oublier la mise a jour du PMS|Ne pas signaler une panne",
  "Haut vers bas~Regle de nettoyage~Sale vers propre~Autre regle~Objet oublie~A enregistrer~Checklist~Outil de controle",
  "Chambre libre sale~A nettoyer~Chambre libre propre~A commercialiser",
  "Nettoyage~Action~Controle qualite~Validation"))

# ============================================================ HO5
add("HO5", "Tarification, yield management et revenu", "Économie et gestion hôtelière", ["1re", "Terminale"],
S("Le prix d'une chambre est une decision economique qui doit couvrir les couts et rester acceptable pour le client."
  "|Le cout fixe par chambre, ou cout marginal, comprend le nettoyage, le linge, les consommables et les charges proportionnelles."
  "|Le seuil de rentabilite d'un hotel correspond au chiffre d'affaires necessaire pour couvrir l'ensemble des charges."
  "|Le yield management ajuste les tarifs en temps reel selon la demande, la disponibilite et l'anticipation de reservation."
  "|Le principe est de vendre la bonne chambre, au bon client, au bon moment et au meilleur prix."
  "|Les tarifs sont souvent differencies par type de chambre, canal de distribution, duree de sejour et condition d'annulation."
  "|Un tarif non remboursable est moins cher car il presente moins de risque pour l'etablissement."
  "|Le prix moyen de la chambre, ou ADR, est le chiffre d'affaires d'hebergement divise par le nombre de chambres occupees."
  "|Le RevPAR combine occupation et prix : il est le principal indicateur de performance commerciale d'un hotel."
  "|Une hausse de prix peut augmenter le RevPAR si la baisse d'occupation reste limitee : c'est l'elasticite de la demande."
  "|La parite tarifaire impose d'aligner les prix sur les differentes plateformes pour eviter le danger du client qui compare."
  "|La tarification doit rester lisible et juste : un client qui découvre un prix plus bas ailleurs perd confiance dans l'etablissement."),
[QC("Que designe l'ADR ?", "Le taux d'occupation~Le prix moyen par chambre occupee~Le chiffre d'affaires total~Le cout de nettoyage", 1,
     "ADR signifie average daily rate : chiffre d'affaires d'hebergement divisé par chambres occupees."),
 QC("Quel est l'objectif du yield management ?", "Vendre toujours moins cher~Adapter le prix a la demande pour maximiser le revenu~Remplir sans tenir compte du prix~Supprimer les reservations", 1,
     "Le yield vise a maximiser le revenu en ajustant prix et disponibilite."),
 QC("Pourquoi un tarif non remboursable est-il moins cher ?", "Il est moins confortable~Il presente moins de risque pour l'hotel~Il est reserve aux groupes~Il inclut le petit-dejeuner", 1,
     "L'absence de droit a l'annulation reduit le risque de perte pour l'etablissement."),
 QT("Un hotel vend 60 chambres a 140 € sur une base de 100 chambres. Calculer l'ADR et le RevPAR.",
     "Le taux d'occupation vaut 60 / 100 = 0,60 soit 60 %. L'ADR est le prix moyen par chambre occupee, ici 140 € puisque toutes les chambres vendues sont au meme tarif. Le RevPAR vaut 0,60 × 140 = 84 € par chambre disponible. Le chiffre d'affaires d'hebergement est de 60 × 140 = 8 400 €. Si le hotel augmente son prix a 150 € et ne vend plus que 56 chambres, le RevPAR devient 0,56 × 150 = 84 € : le gain de prix compense exactement la perte de volume, ce qui illustre le role de l'elasticite.",
     "On attend ADR 140 €, RevPAR 84 € et une discussion sur le compromis prix-volume."),
 QT("Expliquer les limites d'une strategie de yield mal maitrisee.",
     "Une hausse de prix trop aggressive peut decrementer le taux d'occupation, dégrader l'e-réputation et fidéliser moins les clients. A l'inverse, des baisses permanentes augmentent le volume mais réduisent la marge et peuvent installer une image bas de gamme. Le yield repose sur des previsions : si la demande est mal anticipe, l'hotel vend trop tot a bas prix ou trop cher et reste vide. Il faut donc fixer des prix planchers qui couvrent le cout marginal, surveiller les concurrents et les canaux, et garder une cohérence avec la qualite de service promise. Enfin, la parite tarifaire et la transparence sont essentielles pour maintenir la confiance.",
     "On attend risques sur volume, image et marge, importance des previsions et prix plancher.")],
C("Le prix de la chambre est un levier de revenu : le yield arbitre entre occupation et prix moyen.",
  "RevPAR = occupation × ADR",
  "ADR = CA hebergement / chambres occupees",
  "Prix~Decision economique~Yield management~Ajustement temps reel~ADR~Prix moyen~RevPAR~Revenu par chambre disponible~Elasticite~Reaction de la demande~Parite~Coherence des canaux",
  "Connaitre ses couts et son seuil|Estimer la demande a venir|Choisir les niveaux de tarifs|Suivre occupation et ADR|Corriger apres analyse des resultats",
  "Vendre en dessous du cout marginal|Baisser les prix sans objectif|Ignorer les canaux concurrents|Ne pas surveiller le RevPAR",
  "100 chambres~Capacite~60 vendues~Occupation 60 %~140 €~ADR~84 €~RevPAR~8 400 €~CA hebergement",
  "Yield~Prix variable~Tarif fixe~Prix stable toute l'annee",
  "Occupation~Volume vendu~ADR~Niveau de prix"))

# ============================================================ HO6
add("HO6", "Relation client, réclamations et fidélisation", "Sciences et technologies des services", ["Terminale"],
S("La relation client designe l'ensemble des interactions entre l'etablissement et le client avant, pendant et apres le sejour."
  "|Un client satisfait est un client dont l'experience correspond ou depasse les attentes forme es avant l'arrivee."
  "|La qualite perçue depend de elements tangibles : propreté, confort, ponctualite, et d'elements intangibles : accueil, ecoute, empathy."
  "|Une reclamtion est une expression de mecontentement : elle doit etre entendue comme une opportunite d'amelioration."
  "|La procedure de traitement comporte cinq temps : ecouter, reconnaitre, s'excuser, proposer une solution et confirmer la satisfaction."
  "|Il faut eviter de discuter avec le client devant les autres clients : le traitement se fait a l'ecart et avec calme."
  "|Une solution peut consister en un geste commercial : remise, petit-dejeuner offert, surclassement ou nuit offerte."
  "|Toute reclamtion est tracée dans le PMS avec son motif, sa gravite, la solution apportee et le responsable du suivi."
  "|L'analyse des reclamations permet d'identifier les defauts recurrents : bruit, attente, nettoyage insuffisant ou erreur de facture."
  "|La fidélisation vise a transformer un client occasionnel en client habituel grace a la qualite, aux avantages et a la personalisation."
  "|Un programme de fidelite collecte des points, offres des avantages et encourage la reservation directe plutot que les plateformes."
  "|Les avis en ligne font partie de la relation client : repondre de maniere courtoise et factuelle montre le sérieux de l'etablissement."),
[QC("Quelle est la premiere etape du traitement d'une reclamtion ?", "Repondre immediatement~Ecouter le client~Proposer une remise~Appeler le directeur", 1,
     "On ecoute d'abord sans interrompre pour comprendre le motif exact du mecontentement."),
 QC("Ou doit-on traiter une reclamtion ?", "Devant les autres clients~A l'ecart, avec calme~Dans le hall~Sur les reseaux sociaux", 1,
     "Le traitement a l'ecart respecte la dignite du client et evite de propaguer le mecontentement."),
 QC("Que doit contenir la trace d'une reclamtion ?", "Le seul nom du client~Le motif, la gravite et la solution~L'avis d'un collegue~La recette du jour", 1,
     "La traçabilite permet d'analyser les recurrentes et d'ameliorer le service."),
 QC("Quel est un objectif d'un programme de fidelite ?", "Augmenter les prix~Encourager les reservations directes~Remplacer la qualite~Supprimer les avis", 1,
     "Les programmes de fidelite favorisent la reservation directe et la repetition des sejours."),
 QT("Comment traiter une reclamtion pour une chambre bruyante en pleine nuit ?",
     "On ecoute le client sans le contredire, on reconnait le desagrement et on s'excuse. On verifie immediatement les disponibilites : si une chambre calme est libre, on propose un changement avec l'aide d'un personnel pour les bagages. Sinon, on propose des mesures immediates : bouchons d'oreilles, changement d'etage le lendemain, ou geste commercial sur la facture. On note l'incident dans le PMS avec l'heure, le motif et la solution, puis on informe le responsable d'etage et le directeur de permanence. Le lendemain, on prend des nouvelles du client pour confirmer que la situation est resolue et on analyse la cause : chambre mal positionnee, evenement externe ou isolation defective.",
     "On attend procedure en cinq temps, solution concrete, traçabilite et suivi."),
 QT("Pourquoi une reclamtion bien traitee peut-elle favoriser la fidelite ?",
     "Un client mecontent mais bien ecouté voit l'etablissement prendre ses problemes au serieux. Une reponse rapide, courtoise et generateur de solution restaure la confiance et peut laisser une impression plus forte qu'un sejour sans incident : c'est le paradoxe de la recuperation de service. La fidelite se construit ensuite grace au suivi : nouvelle du client, prise en compte de ses preferences, avantage personnelise. A l'inverse, une reclamtion ignoree se transforme en avis negatif en ligne et en perte de client. L'entreprise doit doncconsiderer chaque reclamtion comme une donnee precieuse sur ses processus et non comme une attaque personnelle.",
     "On attend notion de recuperation de service, suivi et lien avec la reputation.")],
C("Une reclamtion est un signal : bien traitee, elle restaure la confiance et alimente l'amelioration continue.",
  "Traitement = ecouter, reconnaitre, s'excuser, resoudre, confirmer",
  "Fidelite = qualite + personnalisation + avantages",
  "Reclamtion~Expression de mecontentement~Ecoute~Premiere etape~Geste commercial~Reparation~PMS~Tracabilite~Fidelisation~Relation durable~Avis en ligne~Reputation numerique",
  "Ecouter sans interrompre|Reconnaitre et s'excuser|Proposer une solution adaptee|Tracer l'incident dans le PMS|Suivre et analyser les recurrentes",
  "Discuter devant les autres clients|Promettre une solution impossible|Oublier le suivi|Ignorer les avis en ligne",
  "Nuit bruyante~Motif frequent~Chambre calme~Solution possible~Geste commercial~Remise ou surclassement~PMS~Suivi",
  "Client satisfait~Attentes respectees~Client fidele~Retour repetitione",
  "Reclamation~Signal negatif~Opportunite~Amelioration possible"))

# ============================================================ RE1
add("RE1", "Types de restauration et modèles économiques", "Sciences et technologies des services", ["1re"],
S("La restauration commerciale comprend les restaurants, brasseries, cafeterias et établissements de restauration rapide."
  "|La restauration collective sert des repas a un groupe identifie : entreprises, ecoles, hopitaux ou collectivites."
  "|La restauration gastronomique mise sur la qualite des produits, le savoir-faire et l'experience du client."
  "|La brasserie propose une carte variee, un service rapide et une large plage horaire."
  "|La restauration rapide reduit le temps de service et simplifie la carte pour augmenter la rotation des tables."
  "|Le chiffre d'affaires d'un restaurant depend du nombre de couverts, du panier moyen et de la rotation."
  "|Le couvert correspond a un client servi ; le nombre de couverts par service depend de la capacite et de la duree moyenne de presence."
  "|Le ticket moyen est le chiffre d'affaires divise par le nombre de couverts : il reflète le positionnement tarifaire."
  "|La marge brute sur les denrees est la difference entre prix de vente et cout des matieres premieres."
  "|Les charges de personnel representent generalement le premier poste de cout d'un restaurant."
  "|Le modèle economique doit tenir compte de la saisonnalite, des horaires de pointe et du cout des locaux."
  "|Le choix du type de restauration determine l'organisation de la cuisine, le service en salle et la politique d'approvisionnement."),
[QC("Quel type de restauration sert les salaries d'une entreprise ?", "Restauration gastronomique~Restauration collective~Brasserie~Restaurant etoile", 1,
     "La restauration collective dessert un groupe identifie, comme une entreprise ou une ecole."),
 QC("Comment calculer le ticket moyen ?", "CA divisé par le nombre de couverts~CA multiplie par le nombre de couverts~Nombre de couverts moins CA~Prix du plat le plus cher", 0,
     "Le ticket moyen est le chiffre d'affaires par couvert."),
 QC("Quel est generalement le premier poste de cout d'un restaurant ?", "Les denrees~Les charges de personnel~L'electricite~La vaisselle", 1,
     "La main-d'oeuvre represente le premier poste de cout en restauration traditionnelle."),
 QC("Quel indicateur mesure la vitesse de rotation des tables ?", "Le ticket moyen~Le nombre de couverts par service~La marge brute~Le food cost", 1,
     "Le nombre de couverts servis par service et par place mesure la rotation."),
 QT("Un restaurant realise 6 000 € de chiffre d'affaires sur 120 couverts. Calculer le ticket moyen et commenter.",
     "Le ticket moyen vaut 6 000 / 120 = 50 € par couvert. Ce niveau situe l'etablissement dans une restauration commerciale de gamme moyenne a superieure : il est nettement superieur a celui d'une restauration rapide et inferieur a celui d'une table gastronomique. Ce chiffre doit etre compare dans le temps et avec les objectifs : une baisse du ticket moyen peut venir d'une carte moins attractive, d'une promotion trop generateuse ou d'une evolution du panier des clients. Il faut le croiser avec le nombre de couverts, car une hausse du ticket peut compenser une baisse de frequentation, ou au contraire masquer une perte de clients.",
     "On attend 50 €, un positionnement et une analyse croisee avec le volume."),
 QT("Comparer restaurant gastronomique et restauration rapide sur trois critères.",
     "Sur le prix, le restaurant gastronomique propose un ticket eleve lie a la qualite des produits et au service, tandis que la restauration rapide mise sur un prix bas et une standardisation. Sur le temps, le premier propose une experience longue avec plusieurs services, le second une rotation rapide et un service simplifie. Sur l'organisation, la cuisine gastronomique travaille a la commande avec une brigade specialisee, alors que la restauration rapide anticipe la production et reduit le nombre de taches. Ces choix entrainent des couts differents : main-d'oeuvre qualifiee et denrees nobles d'un cote, equipements standardises et faible cout unitaire de l'autre.",
     "On attend trois criteres clairement contrastes et un lien avec les couts.")],
C("Le modèle economique d'un restaurant repose sur le couvert, le ticket moyen et la maitrise des couts.",
  "CA = couverts × ticket moyen",
  "Ticket moyen = CA / couverts",
  "Restauration commerciale~Clientele externe~Collective~Groupe identifie~Gastronomique~Produits et savoir-faire~Couvert~Client servi~Ticket moyen~CA par couvert~Rotation~Couverts par service",
  "Choisir le positionnement|Estimer la capacite et la rotation|Construire la carte et les prix|Estimer couts et marge|Suivre les indicateurs chaque service",
  "Confondre couvert et client un autre jour|Ignorer la rotation|Ne pas comparer le ticket moyen|Oublier le cout de la main-d'oeuvre",
  "6 000 €~Chiffre d'affaires~120 couverts~Volume~50 €~Ticket moyen~Point de vente~Capacite d'accueil",
  "Commerciale~Client de passage~Collective~Convives captifs",
  "Rotation rapide~Peu de temps par table~Experience longue~Service etat d'ame"))

# ============================================================ RE2
add("RE2", "Mise en place et organisation du service en salle", "Sciences et technologies des services", ["1re"],
S("La mise en place designe l'ensemble des operations prepareatoires effectuees avant l'ouverture du service."
  "|Elle comprend le nettoyage de la salle, le dressage des tables, la preparation des condiments et le controle des equipements."
  "|Une mise en place reussie repose sur une liste ecrite, ou checklist, et sur la repartition des taches entre les membres de l'equipe."
  "|Le plan de salle definit l'emplacement des tables, les zones de service, les circulations et les issues de securite."
  "|Le chef de rang est responsable d'un secteur, generalement de quatre a six tables, et coordonne le commis de rang."
  "|Le commis de rang aide au debarassage, au nettoyage des tables et a l'approvisionnement en vaisselle et en linge."
  "|Le maxime d'hotel accueille les clients, gere les reservations et distribue les tables selon le plan de service."
  "|Le debarassage doit etre discret et respecter un ordre : verres, vaisselle sale, puis nettoyage de la table."
  "|La vaisselle propre et le linge de table sont verifies avant le service pour eviter les ruptures en pleine periode de pointe."
  "|Les commandes sont transmises en cuisine avec precision : plat, cuisson, allergies et eventuelles modifications."
  "|Le service doit respecter les regles d'hygiene : mains propres, vaisselle saine, aucune manipulation directe des aliments."
  "|Une bonne mise en place reduit le stress en service et ameliore la qualite perçue par le client."),
[QC("Qui est responsable d'un secteur de tables en salle ?", "Le commis de rang~Le chef de rang~Le plongeur~Le client", 1,
     "Le chef de rang dirige un secteur et encadre le commis."),
 QC("Que contient la mise en place ?", "Seulement la vaisselle~Le nettoyage, le dressage et les verifications~Uniquement les reservations~La facturation", 1,
     "La mise en place prepare tous les elements necessaires au service."),
 QC("Quel document definit l'emplacement des tables et des issues ?", "La carte~Le plan de salle~Le bon de commande~La facture", 1,
     "Le plan de salle organise l'espace et les circulations."),
 QC("Dans quel ordre debarrasse-t-on une table ?", "Vaisselle sale, verres, linge~Verres, vaisselle sale, nettoyage~Linge, verres, vaisselle~Au hasard", 1,
     "On retire d'abord les verres, puis la vaisselle sale, puis on nettoie la table."),
 QT("Decrire la mise en place d'un service du midi et son importance.",
     "Avant l'ouverture, on nettoie la salle, on dresse les tables selon le plan, on verifie le linge et la vaisselle, on prepare les condiments, les carafes et les bons de commande. On controle ega element les installations : lumiere, climatisation, caisse et terminal de paiement. Chaque membre de l'equipe recoit une tache precise et une heure de fin de mise en place. On fait ensuite une derniere visite des tables. Cette preparation est determining : si un element manque en plein service, le client attend, le rythme se rompt et l'equipe perd confiance. Une mise en place methodique au contraire rend le service fluide et professionnel.",
     "On attend les operations, la repartition des taches et le lien avec la fluidite du service."),
 QT("Un client signale une assiette sale au moment du service. Que faire ?",
     "On s'excuse immediatement sans discuter, on retire l'assiette et on la remplace par une propre le plus vite possible. On previens le chef de rang pour qu'il verifie le reste du lot de vaisselle : il peut y avoir une erreur de plonge ou une tache non vue lors de la mise en place. On note l'incident pour identifier la cause et on renforce le controle visuel avant le prochain service. Si le plat a touché l'assiette sale, on le refait en cuisine. Enfin, on revient vers le client pour verifier qu'il est satisfait, et on propose un geste commercial si le desagrement a ete important.",
     "On attend retrait et remplacement immediats, recherche de cause et suivi client.")],
C("La mise en place est la preparation invisible du service : elle determine la fluidite et la qualite perçue.",
  "Service fluide = mise en place complete + equipe coordonnee",
  "Plan de salle · chef de rang · checklist · hygiene",
  "Mise en place~Preparation avant service~Plan de salle~Zones et circulations~Chef de rang~Responsable de secteur~Commis~Aide au debarassage~Checklist~Liste de controles~Commande~Transmission en cuisine",
  "Nettoyer la salle|Dresser les tables selon le plan|Verifier vaisselle et linge|Repartir les taches de l'equipe|Controle final avant ouverture",
  "Ouvrir sans controle|Oublier les issues de securite|Mal transmettre une allergie~Laisser manquer des verres",
  "4 a 6 tables~Secteur type~Avant ouverture~Moment de la mise en place~Assiette sale~Incident a corriger~Checklist~Outil de controle",
  "Chef de rang~Encadre un secteur~Commis de rang~Execute les aides",
  "Preparation~Avant service~Service~Pendant le service"))

# ============================================================ RE3
add("RE3", "Techniques de service : assiette, guéridon et buffet", "Sciences et technologies des services", ["1re", "Terminale"],
S("Le service a l'assiette consiste a presenter le plat deja dressé en cuisine directement devant le client."
  "|C'est la technique la plus repandue : elle impose une cuisine organizee et un dressage coherent avec la carte."
  "|Le service au guéridon se deroule devant le client, sur une table roulante ou un réchaud : il est plus spectaculaire."
  "|Le service au guéridon demande une maitrise technique, une bonne coordination avec la cuisine et le respect des regles de securite."
  "|Le service en buffet propose un choix de plats presents sur une table ou un comptoir, en libre-service ou servi par l'equipe."
  "|Le buffet exige une gestion des quantites, un renouvellement frequent et une surveillance des temperatures."
  "|Le service en terrine ou en cocotte permet de presenter un plat commun que le client se sert lui-meme."
  "|Le service a la russe presente les plats successivement sur un plat que le serveur propose au client."
  "|Chaque technique impose un ordre de service : d'abord les enfants et les dames, puis les autres convives, ou selon l'usage de l'etablissement."
  "|Le serveur presente le plat par la gauche, debarasse par la droite, et annonce clairement ce qu'il sert."
  "|La temperature de service est un critere de qualite : un plat chaud doit etre servi chaud, un plat froid jamais a temperature ambiante."
  "|Le choix de la technique depend du type de restaurant, du prix du menu, de l'espace disponible et de la taille de l'equipe."),
[QC("Quelle technique presente le plat deja dresse en cuisine ?", "Le service au gueridon~Le service a l'assiette~Le buffet~Le service a la russe", 1,
     "Le service a l'assiette presente un plat deja dresse devant le client."),
 QC("Quel service se deroule devant le client sur un rechaud ?", "A l'assiette~Au gueridon~En cafeteria~En self-service", 1,
     "Le service au gueridon se fait devant le client sur une table roulante ou un réchaud."),
 QC("Quel risque principal d'un buffet mal surveille ?", "Un prix trop eleve~Une derive de temperature~Un plat trop chaud~Une vaisselle insuffisante", 1,
     "Les plats exposes peuvent sortir de la zone de temperature safe et favorable aux bacteries."),
 QC("Par quel cote debarrasse-t-on generalement le client ?", "Par la gauche~Par la droite~Par devant~Par derriere", 1,
     "La convention traditionnelle est de servir par la gauche et de debarrasser par la droite."),
 QT("Comparer service a l'assiette et service au gueridon en restauration.",
     "Le service a l'assiette est rapide, standardise et adapte a un grand nombre de couverts : la cuisine dresse, le serveur transporte et presente. Il demande moins de competences techniques en salle mais une grande rigueur de timing. Le service au gueridon ajoute une dimension spectacular : le serveur adhere, flambe ou découpe devant le client, ce qui valorise le produit et justifie un prix plus eleve. Il exige une formation solide, un equipement adapte et une attention permanente a la securite, notamment avec les rechauds et l'alcool. Le choix depend donc du positionnement du restaurant et de la qualite de l'equipe.",
     "On attend comparaison sur rapidite, competitences, effet client et contraintes de securite."),
 QT("Quelles regles appliquer pour un buffet en toute securite ?",
     "On controle la temperature des plats chauds et froids avec un thermometre et on respecte la duree d'exposition. Les plats sont couverts, les ustensiles changeS regulierement, et le personnel verifie l'aspect et l'odeur des denrees. On applique la marche en avant : les plats propres ne croisent pas les plats sales, et on ne remedite pas un plat déjà servi. Les allergenes sont indiques par ecrit, et une personne est designee pour surveiller et renouveler le buffet. En fin de service, les restes sont soit consommes immediatement selon la procedure, soit detruits : ils ne sont jamais representes le lendemain.",
     "On attend temperature, duree, protection, allergenes et non-representation des restes.")],
C("Chaque technique de service repond a un positionnement : rapidite, spectacle ou Choix, avec des exigences de securite.",
  "Assiette = dressage en cuisine · gueridon = preparation devant le client",
  "Servir a gauche · debarrasser a droite · surveiller les temperatures",
  "A l'assiette~Plat deja dresse~Rapidite~Au gueridon~Spectacle devant le client~Competence~Buffet~Libre-service~Temperature~Critere de qualite~Allergene~Information obligatoire",
  "Choisir la technique selon le concept|Former l'equipe aux gestes|Organiser l'espace et le materiel|Controler les temperatures|Verifier la satisfaction client",
  "Representer les restes d'un buffet|Ignorer les allergenes|Mal maitriser un rechaud~Servir un plat tiede",
  "Plat chaud~Temperature maintenue~Gueridon~Table roulante~Buffet~RenoUvellement frequent~Allergenes~Etiquetage",
  "A l'assiette~Cuisine dresse~Au gueridon~Salle prepare",
  "Service rapide~Rotation elevee~Service spectaculaire~Valeur ajoutee"))

# ============================================================ RE4
add("RE4", "Service des boissons et accord mets-vins", "Sciences et technologies des services", ["Terminale"],
S("Le service des boissons comprend l'eau, les vins, les bières, les spiritueux, les jus et les boissons chaudes."
  "|La carte des boissons doit etre coherente avec la carte des mets et le positionnement du restaurant."
  "|Le service de l'eau se fait generalement des le debut du service, avec une carafe ou une bouteille presentee au client."
  "|Le vin est presenté avec l'étiquette vers le client, puis ouvert en sa presence pour verification."
  "|La mise en bouche, ou dégustation, permet au client de confirmer le choix avant le service."
  "|Le service du vin suit un ordre precis : presention de la bouteille, ouverture, service d'un petit jeu au commanditaire, puis service des autres convives."
  "|La temperature de service varie selon le type de vin : un vin blanc sec se sert frais, un vin rouge corsé moins frais."
  "|Le verre utilise depend du vin : verre a pied pour le vin, verre a biere pour la biere, et verre a digestif pour les spiritueux."
  "|L'accord mets-vins repose sur l'equilibre des saveurs : un vin acide accompagne un plat gras, un vin sucré un dessert."
  "|Les regles classiques associent le vin au plat dominant, a la sauce et a la texture plutot qu'au seul ingrédient principal."
  "|La vente de boissons represente souvent une part importante du chiffre d'affaires et de la marge d'un restaurant."
  "|La reglementation impose la moderation, l'information sur les allergenes eventuels et le refus de servir une personne ivre."),
[QC("Que fait-on en premier lors du service d'une bouteille de vin ?", "On ouvre la bouteille~On presente l'étiquette au client~On verse directement~On apporte l'addition", 1,
     "La bouteille est d'abord presentee pour confirmation par le client."),
 QC("Quel role joue la mise en bouche ?", "Verifier la temperature~Faire gouter le vin au commanditaire avant le service~Nettoyer le verre~Annuler la commande", 1,
     "Le client goute et confirme que le vin lui convient."),
 QC("Quel vin accompagne classiquement un plat gras ?", "Un vin tres sucre~Un vin acide~Un vin rose~Une biere brune", 1,
     "L'acidite équilibre la gras du plat et nettoie le palais."),
 QC("Quel verre utilise-t-on pour un vin rouge ?", "Verre a biere~Verre a pied~Verre a digestif~Verre a eau", 1,
     "Le verre a pied permet d'observer la robe et de faire tourner le vin."),
 QT("Decrire les etapes du service d'une bouteille de vin a table.",
     "On presente la bouteille, etiquette visible, en annoncant le nom et le millesime ; le client confirme. On ouvre la bouteille devant lui, on retire le bouchon et on le lui presente. On essuie le goulot, on verse un petit jeu au commanditaire pour la dégustation, puis on attend son accord. On sert ensuite les autres convives en respectant l'ordre et en remplissant les verres au tiers ou a la moitie. On pose la bouteille sur la table ou sur un seau a glace selon le type de vin, et on reste disponible pour resservir. Tout au long, on adapte le rythme a celui des convives et on surveille la consommation.",
     "On attend presention, ouverture, dégustation, service des convives et attention a la moderation."),
 QT("Comment construire un accord mets-vins simple et convaincant ?",
     "On identifie d'abord le gout dominant du plat : gras, acide, sale, sucre ou epice. On choisit ensuite un vin qui equilibre ou contraste : l'acidite coupe le gras, le sucre repond au piquant, un vin leger accompagne un poisson delicat et un vin plus structure un plat de viande rouge. On tient compte de la sauce, souvent plus determinante que la viande, et de l'intensite globale du plat : un mets subtil ne doit pas etre écrase par un vin puissant. Enfin, on propose un choix et on explique brievement le accord au client, sans imposer. La temperature de service et le verre utilises completent la qualite de la proposition.",
     "On attend logique d'equilibre, role de la sauce, explanation client et importance du service.")],
C("Le service des boissons allie geste technique, connaissance des produits et vigilance reglementaire.",
  "Accord mets-vins = equilibre des saveurs",
  "Presention · ouverture · dégustation · service",
  "Carte des boissons~Offre coherente~Presention~Etiquette visible~Degustation~Accord du client~Temperature~Qualite de service~Accord mets-vins~Equilibre~Marge~Contribution au CA",
  "Verifier la carte et les stocks|Presenter la bouteille au client|Ouvrir et faire deguster|Servir dans l'ordre|Surveiller consommation et reglementation",
  "Ouvrir avant l'accord du client|Servir un vin a la mauvaise temperature|Ignorer les limites d'age|Omettre l'information allergene",
  "Etiquette~Identite du vin~Mise en bouche~Moment de la dégustation~Verre a pied~Service du vin~Acidite~Equilibre du gras",
  "Vin blanc sec~A servir frais~Vin rouge corse~Moins frais",
  "Service~Geste et produit~Vente~Chiffre d'affaires et marge"))

# ============================================================ RE5
add("RE5", "Banquets, événements et restauration collective", "Sciences et technologies des services", ["Terminale"],
S("Un banquet est un repas organise pour un groupe, souvent a l'occasion d'un evenement : mariage, congrès, anniversaire ou séminaire."
  "|L'organisation d'un banquet suit une procedure commerciale : demande, devis, contrat, preparation, realisation et facturation."
  "|Le cahier des charges precise le nombre de convives, le menu, les horaires, le budget, les contraintes et les responsabilites."
  "|Le devis chiffre les prestations : menu, boissons, location de salle, personnel, décoration et options techniques."
  "|Le contrat fixe les conditions d'annulation, les delais de confirmation du nombre de convives et les modalites de paiement."
  "|Le plan de table et le plan de salle sont construits ensemble pour assurer la circulation et la vue sur la scene."
  "|Le banquet require une coordination precise entre cuisine, salle, technique et direction."
  "|Le service en banquet privilégie souvent le service en buffet ou le service a l'assiette pour servir simultanement un grand groupe."
  "|La restauration collective suit des regles nutritionnelles et d'hygiene specialifiques, notamment le plan de menus et les grammages."
  "|Le plan de menus de la restauration collective doit etre etabli sur une periode et equilibre sur le plan nutritionnel."
  "|Les regles d'hygiene HACCP s'appliquent egalement aux banquets, avec une attention particuliere aux plats prepares a l'avance."
  "|La satisfaction du client evenementiel depend du respect des engagements : ponctualite, quantite, qualite et ambiance."),
[QC("Quel document chiffre les prestations d'un banquet ?", "Le menu~Le devis~La fiche de poste~Le plan de salle", 1,
     "Le devis presente le detail chiffre des prestations avant signature."),
 QC("Que fixe le contrat de banquet ?", "Les seules heures~Les conditions d'annulation et de paiement~La recette~Le plan de table", 1,
     "Le contrat encadre les engagements des deux parties, notamment annulation et paiement."),
 QC("Quel point est particulierement surveille en restauration collective ?", "Le luxe du decor~L'equilibre nutritionnel et les grammages~Le prix du vin~La duree du service", 1,
     "Les menus collectifs doivent respecter des recommandations nutritionnelles."),
 QC("Quelle technique de service est courante pour un grand banquet ?", "Le gueridon~Le service a l'assiette ou le buffet~Le service a la russe~Le service au comptoir", 1,
     "Les grands groupes necessitent un service simultane, assiette ou buffet."),
 QT("Decrire les etapes de l'organisation d'un banquet de 120 personnes.",
     "On recueille d'abord le besoin : date, heure, nombre de convives, type d'evenement, budget et contraintes. On propose ensuite un devis avec menu, boissons, salle, personnel et options, puis on signe un contrat qui precise les delais de confirmation et les conditions d'annulation. On planifie la production : commandes, preparation en cuisine, mise en place de la salle, plan de table et affectation du personnel. Le jour J, on effectue un controle final avant l'arrivee des convives, on coordonne les services avec le deroule de l'evenement et on gere les imprévus. Enfin, on etabli la facture et on demande un retour d'experience au client.",
     "On attend demande, devis, contrat, planification, execution et suivi."),
 QT("Quelles sont les difficultes d'un service pour un grand groupe et comment les anticiper ?",
     "Le principal difficulté est de servir simultanement un grand nombre de convives sans deteriorer la qualite ni la temperature des plats. On anticipe en dimensionnant les equipes, en preparing les assiettes ou les buffets selon un timing precis et en organisant les circuits de vaisselle et de boissons. La deuxieme difficulte concerne les attentes individuelles : allergenes, regimes alimentaires et preferences doivent etre collectes avant l'evenement et transmis a la cuisine. Enfin, le deroule peut prendre du retard : on designe un referent qui coordonne cuisine, salle et organisateur. Une checklist et une reunion de briefing avant le service permettent de reduire les erreurs.",
     "On attend simultaneite, collecte des contraintes alimentaires et coordination par un referent.")],
C("Un banquet est un projet de service : devis, contrat, planification et coordination conditionnent la reussite.",
  "Banquet = groupe + menu + salle + personnel",
  "Devis puis contrat · plan de salle · HACCP",
  "Banquet~Repas de groupe~Devis~Chiffrage~Contrat~Engagements~Plan de table~Disposition des convives~Simultaneite~Servir en meme temps~Collectif~Regles nutritionnelles",
  "Recueillir le besoin|Etablir devis et contrat|Planifier cuisine et salle|Briefier l'equipe et controler|Facturer et demander un retour",
  "Oublier les allergies des convives~Ne pas fixer de delai de confirmation~Sous-estimer le personnel~Ignorer le deroule de l'evenement",
  "120 convives~Groupe important~Contrat~Securite juridique~Allergenes~Contrainte individualisee~HACCP~Hygiene appliquee",
  "Banquet~Evenement prive~Collectif~Repas institutionnalise",
  "Devis~Proposition chiffree~Contrat~Accord signe"))

# ============================================================ HY1
add("HY1", "HACCP : analyse des risques et points critiques", "Sciences et technologies culinaires", ["1re", "Terminale"],
S("Le système HACCP, ou Hazard Analysis and Critical Control Points, est une methode de maitrise sanitaire des aliments."
  "|Il repose sur une analyse des dangers plutot que sur le seul controle du produit final."
  "|Un danger peut etre biologique, chimique ou physique : bacterie, allergene, residue de nettoyant ou corps etranger."
  "|Le code de la sante publique et le reglement (CE) n° 852/2004 imposent aux professionnels une demarche HACCP."
  "|Les sept principes HACCP sont : analyser les dangers, identifier les points critiques, fixer des limites, surveiller, corriger, verifier et documenter."
  "|Un point critique, ou CCP, est une etape ou un controle permet d'eliminer ou de reduire le danger a un niveau acceptable."
  "|Une limite critique est une valeur mesurable, souvent une temperature ou une duree, qui separe le acceptable du non acceptable."
  "|La surveillance consiste a mesurer et a enregistrer la valeur de chaque point critique a une frequence definie."
  "|En cas de depassement, une action corrective est declenchee : isoler le produit, corriger le procede et prévenir la reccurrence."
  "|La verification controlle l'efficacite globale du systeme : audits, analyses microbiologiques et revue des enregistrements."
  "|La traçabilite et la tenue des enregistrements sont obligatoires : « ce qui n'est pas ecrit n'a pas ete fait »."
  "|Le plan HACCP est specifique a chaque etablissement : il doit etre actualise lors d'un changement de carte, de procede ou de materiel."),
[QC("Que signifie le sigle HACCP ?", "Analyse et controle des points critiques~Hygiene et controle de la cuisine~Hazard Analysis and Critical Control Points~Homologation des circuits de production", 2,
     "HACCP correspond a l'anglais Hazard Analysis and Critical Control Points."),
 QC("Quels sont les trois types de dangers alimentaires ?", "Chaud, froid, tieux~Biologique, chimique, physique~Visuel, olfactif, gustatif~Matin, midi, soir", 1,
     "Les dangers sont biologiques, chimiques ou physiques."),
 QC("Qu'est-ce qu'un point critique ?", "Une etape sans importance~Une etape ou un controle maitrise le danger~Un client exigeant~Un simple nettoyage", 1,
     "Le CCP est l'etape ou la maitrise est determining pour la securite."),
 QC("Que faire en cas de depassement d'une limite critique ?", "Rien, si le plat a bonne apparence~Declencher une action corrective et isoler le produit~Vendre plus vite~Changer la carte", 1,
     "Tout depassement impose une action corrective immediate et tracee."),
 QC("Quelle affirma tion est vraie ?", "Le plan HACCP est identique pour tous~Le plan HACCP est propre a chaque etablissement~Il suffit de le rediger une fois~Il remplace le nettoyage", 1,
     "Le plan est specifique et doit etre mis a jour."),
 QT("Expliquer la difference entre maitrise des points critiques et controle final du plat.",
     "Le controle final verifie le produit termine : aspect, gout, temperature. Il intervient trop tard pour empecher une contamination et il ne peut pas tester chaque plat. La demarche HACCP, elle, agit en amont : elle identifie les etapes ou le danger peut apparaitre ou etre maitrise, comme la recepiton, le stockage, la cuisson ou le refroidissement. Pour chacune, on fixe une limite critique et on surveille en continu. Si la surveillance montre un ecart, on corrige avant que le plat ne soit servi. La securite alimentaire est donc construite a chaque etape de la chaine, pas seulement verifiee a la fin.",
     "On attend difference entre action en amont et controle a posteriori, avec exemples."),
 QT("Un thermometre indique 58 °C au coeur d'un plat qui devrait atteindre 63 °C. Que faire ?",
     "La limite critique n'est pas atteinte : le plat ne peut pas etre servi en l'etat. On poursuit la cuisson jusqu'a la temperature requise, on mesure a nouveau au coeur du produit et on enregistre la nouvelle valeur et l'heure. Si le produit a sejourne trop longtemps dans la zone dangereuse, on l'isole et on l'élimine selon la procedure. On recherche la cause : four mal regle, piece trop epaisse, thermometre mal etalonné ou temps de cuisson insuffisant. On corrige le procede, on forme le personnel concerne et on consigne l'action corrective dans le plan HACCP pour éviter que l'ecart se repete.",
     "On attend poursuite de cuisson ou elimination, enregistrement, recherche de cause et action corrective.")],
C("HACCP maitrise les dangers en amont : analyser, surveiller, corriger, verifier et tracer.",
  "7 principes : danger, CCP, limites, surveillance, correction, verification, documents",
  "Dangers : biologique, chimique, physique",
  "HACCP~Methode de maitrise~Danger~Biologique, chimique, physique~CCP~Point critique~Limite critique~Valeur seuil~Surveillance~Mesure et enregistrement~Action corrective~Corriger et tracer",
  "Analyser les dangers de chaque etape|Identifier les points critiques|Fixer les limites et les modes de mesure|Surveiller et enregistrer|Corriger, verifier et mettre a jour",
  "Croire qu'un controle visuel suffit|Ne pas enregistrer les mesures|Laisser un produit douteux en service|Ne jamais actualiser le plan",
  "63 °C~Exemple de limite~Cuisson~Etape critique~Registre~Preuve de surveillance~CCP~Point de maitrise",
  "Controle final~Verifie le produit~HACCP~Maitrise le procede",
  "Danger~Risque possible~Risque~Danger × exposition"))

# ============================================================ HY2
add("HY2", "Chaîne du froid et maîtrise des températures", "Sciences et technologies culinaires", ["1re"],
S("La chaine du froid designe l'ensemble des etapes ou un produit doit etre maintenu a une temperature basse, de la production a la consommation."
  "|Une rupture de la chaine du froid se produit quand un produit depasse la temperature autorisee, même temporairement."
  "|Les bacteries se developpent rapidement dans la zone de danger, generalement entre 10 et 65 °C."
  "|Les produits frais Emballes sont generalement conserves entre 0 et 4 °C ; les produits surgeles a -18 °C ou moins."
  "|La temperature de conservation doit etre mesuree avec un thermometre propre et etalonné, au coeur du produit ou dans l'enceinte."
  "|La date limite de consommation, ou DLC, concerne les produits tres sensibles : apres la date, le produit ne doit plus etre servi."
  "|La date d'utilisation optimale, ou DLUO, concerne des produits moins sensibles : apres la date, la qualite peut diminuer."
  "|Le respect de l'ancienneté s'organise selon la regle FIFO : first in, first out, les premiers entrees sont les premiers utilises."
  "|Le refroidissement rapide d'un plat cuit doit abaisser sa temperature de 63 a 10 °C en moins de deux heures."
  "|Un produit decongelé ne doit jamais etre recongelé cru : il doit etre cuit avant une eventuelle recongelation."
  "|Le stockage respecte la separation des produits crus et cuits pour eviter les contaminations croisees."
  "|Chaque rupture de chaine doit etre enregistree et entrainer une decision de maintien, de cuisson immediate ou d'elimination."),
[QC("Dans quelle plage de temperature les bacteries se developpent-elles le plus ?", "0 a 4 °C~10 a 65 °C~-18 a -10 °C~Au-dessus de 100 °C", 1,
     "La zone de danger se situe approximativement entre 10 et 65 °C."),
 QC("A quelle temperature conserve-t-on un produit surgele ?", "0 a 4 °C~-18 °C ou moins~10 a 15 °C~20 °C", 1,
     "La conservation des surgeles exige -18 °C ou moins."),
 QC("Que signifie FIFO ?", "Premier entre, premier sorti~Dernier entre, premier sorti~Froid important et frais~Formation interne", 0,
     "FIFO organise la rotation des stocks en utilisant d'abord les produits les plus anciens."),
 QC("Peut-on recongeler un produit decongelé cru ?", "Toujours~Jamais, sauf apres cuisson~Seulement le week-end~Oui si la date le permet", 1,
     "La recongelation d'un produit cru decongelé est interdite ; la cuisson au prealable la rend possible."),
 QC("Que faire en cas de rupture de la chaine du froid ?", "Servir rapidement~Enregistrer et decider selon la duree et la temperature~Oublier l'incident~Ajouter du sel", 1,
     "La rupture est tracee et entraine une decision de securite."),
 QT("Expliquer pourquoi la temperature est un point critique de la securite alimentaire.",
     "La temperature controle la vitesse de multiplication des micro-organismes. Dans la zone de danger, entre 10 et 65 °C, certaines bacteries peuvent doubler en une vingtaine de minutes : un plat laisse tieux quelques heures peut devenir dangereux sans changer d'aspect ni d'odeur. Le froid ralentit leur developpement sans le supprimer, et la cuisson a coeur les détruit si la temperature et la duree sont sufisfantes. C'est pourquoi la reception, le stockage, la cuisson, le refroidissement et le maintien au chaud sont des points critiques du plan HACCP, avec des limites chiffrees et des mesures enregistrees.",
     "On attend lien temperature et croissance bacterienne, exemples de points critiques."),
 QT("Un plat cuit doit etre refroidi rapidement. Decrire la procedure et les points de controle.",
     "Des la fin de la cuisson, on mesure la temperature au coeur, puis on transvase le plat dans des recipients peu profonds pour accelerer le refroidissement. On le place sans attendre en cellule de refroidissement rapide ou dans un bain-marie froid, en respectant les regles de propreté et en couvrant les preparations. On vise le passage de 63 a 10 °C en moins de deux heures, puis le stockage a 0-4 °C. On releve les temperatures a des creneaux fixes et on enregistre les valeurs. On verifie ensuite la date limite de consommation et on etique le plat. Si le refroidissement est trop lent, on isole le produit et on applique la procedure d'action corrective.",
     "On attend mesure, transvasement, equipment adapte, delais et enregistrements.")],
C("La temperature est un levier de maitrise : chaque etape de la chaine du froid a une limite et une trace.",
  "Zone de danger : 10-65 °C",
  "Frais 0-4 °C · surgeles -18 °C · refroidissement 63 a 10 °C en 2 h",
  "Chaine du froid~Continuite des temperatures~Zone de danger~10 a 65 °C~FIFO~Rotation des stocks~DLC~Date limite de consommation~Refroidissement~Descriptor~Decongelation~Regle de recongelation",
  "Verifier la temperature a la reception|Ranger selon FIFO et separer cru et cuit|Mesurer au coeur des preparations|Refroidir rapidement et enregistrer|Decider en cas d'ecart",
  "Laisser un plat a temperature ambiante|Recongeler un produit cru|Ignorer la DLC|Melanger produits crus et cuits",
  "0-4 °C~Conservation des frais~-18 °C~Conservation des surgeles~63 a 10 °C~Refroidissement en 2 heures~DLC~Date a respecter",
  "Froid~Ralentit les bacteries~Chaleur~Detroit les bacteries",
  "DLC~Securite~DLUO~Qualite optimale"))

# ============================================================ HY3
add("HY3", "Nettoyage, désinfection et marche en avant", "Sciences et technologies culinaires", ["1re"],
S("Le nettoyage retire les salissures visibles ; la desinfection reduit le nombre de micro-organismes a un niveau acceptable."
  "|Les deux operations sont complementaires : on ne desinfecte correctement qu'une surface prealablement nettoyee."
  "|Le plan de nettoyage et de desinfection, ou PND, precise pour chaque surface le produit, la methode, la frequence et le responsable."
  "|Un produit detergent agit sur les graisses et les salissures ; un desinfectant agit sur les micro-organismes."
  "|Le regime de nettoyage doit respecter les concentrations, les temps de contact et les temperatures indiques par le fabricant."
  "|Les produits chimiques sont etiquetes, stockes a l'ecart des denrees et utilises avec des equipements de protection."
  "|La marche en avant organise les locaux et les flux pour que le propre ne croise jamais le sale."
  "|Le circuit des denrees va de la reception aux stockages, puis a la preparation, a la cuisson et au service."
  "|Le circuit du linge sale et de la vaisselle sale suit un trajet separe de celui des produits propres."
  "|Les planches a decouper et les ustensiles sont distingues par couleur selon les familles de produits : viande, poisson, legumes."
  "|Le lavage des mains est un geste simple et fondamental : avant chaque tache, apres chaque contact avec un produit sale ou un dechet."
  "|Le controle d'efficacite peut reposer sur des tests de surface et sur l'observation quotidienne des equipes."),
[QC("Quelle est la difference entre nettoyage et desinfection ?", "Aucune~Le nettoyage retire les salissures, la desinfection reduit les micro-organismes~La desinfection retire les graisses~Le nettoyage tue tout", 1,
     "On nettoie d'abord, on desinfecte ensuite avec un temps de contact respecte."),
 QC("Que precise le plan de nettoyage et de desinfection ?", "Les seuls horaires~Produit, methode, frequence et responsable~Le menu~Les prix", 1,
     "Le PND organise les operations de nettoyage de facon ecrite et tracable."),
 QC("Que signifie la marche en avant ?", "Avancer rapidement~Le propre ne croise jamais le sale~Nettoyer en reculant~Servir en premier", 1,
     "La marche en avant separe les circuits propres et sales dans l'espace et dans le temps."),
 QC("Comment eviter les contaminations croisees avec les planches ?", "Utiliser une seule planche~Distinguer les planches par familles de produits~Les laver a l'eau froide~Les changer une fois par semaine", 1,
     "Le code couleur distingue viande, poisson, legumes et produits prets a consommer."),
 QT("Expliquer l'interet du plan de nettoyage et de desinfection dans une cuisine.",
     "Sans plan ecrit, le nettoyage depend de la memoire et de la bonne volonté de chacun : certaines surfaces sont oubliees, d'autres nettoyees avec un produit inadapté ou un temps de contact trop court. Le PND definit pour chaque zone ce qui doit etre nettoye, avec quel produit, a quelle frequence et par qui. Il mentionne aussi les moyens de controle et les traces a remplir. Il rend la tache reproductible, facilite la formation des nouveaux salaries et fournit une preuve en cas de controle sanitaire. Enfin, il permet d'adapter la frequence au risque : une planche a viande sera desinfectee plus souvent qu'un plan de travail a legumes.",
     "On attend definition du PND, reproductibilite, formation et preuve de controle."),
 QT("Comment organiser la marche en avant dans une cuisine et un plonge ?",
     "On concoit d'abord les circuits : les denrees entrent par la reception, passent par les stockages secs et froids, puis par la preparation et la cuisson avant d'atteindre le service. Les dechets et le linge sale empruntent un circuit distinct qui ne traverse pas les zones propres. Au plonge, la vaisselle sale entre d'un cote, passe par le debarassage, le lavage, le rinçage, la desinfection et le sechage, puis ressort propre de l'autre cote. Les produits chimiques restent dans un local separe des denrees. On complete l'organisation par des codes couleur pour les planches et des lavages de mains frequents. Enfin, on observe les deplacements reels de l'equipe pour verifier que les flux ne se croisent pas.",
     "On attend separation des flux, organisation du plonge, produits chimiques et verification terrain.")],
C("Nettoyer, desinfecter et separer les flux forment le socle de l'hygiene : le propre ne doit jamais rencontrer le sale.",
  "Nettoyage puis desinfection avec temps de contact",
  "Marche en avant : reception, stockage, preparation, cuisson, service",
  "Nettoyage~Retirer les salissures~Desinfection~Reduire les micro-organismes~PND~Plan ecrit~Marche en avant~Separation propre et sale~Code couleur~Planches et ustensiles~Contamination croisee~Transfer de germes~Lavage des mains~Geste fondamental",
  "Etablir le plan de nettoyage|Former les equipes aux produits et doses|Separer les circuits propres et sales|Appliquer les temps de contact|Controler et tracer les resultats",
  "Desinfecter sans nettoyer|Melanger produits de familles differentes~Stocker les produits chimiques pres des denrees~Oublier le temps de contact",
  "Temps de contact~Condition d'efficacite~Code couleur~Viande, poisson, legumes~PND~Document de reference~Plonge~Circuit de la vaisselle",
  "Nettoyage~Avant~Desinfection~Apres",
  "Propre~Zone sure~Sale~Zone a risque"))

# ============================================================ HY4
add("HY4", "Allergènes, traçabilité et information du client", "Sciences et technologies culinaires", ["Terminale"],
S("Un allergene alimentaire est une substance qui declenche une reaction immunitaire chez certaines personnes."
  "|Les quatorze allergenes majeurs de la reglementation europeenne comprennent les arachides, le lait, les oeufs, le gluten, les fruits a coque, le soja, le poisson et les crustaces."
  "|Le reglement (UE) n° 1169/2011 impose l'information des consommateurs sur la presence d'allergenes dans les denrees."
  "|En restauration, l'information doit etre disponible par ecrit et facilement accessible au client avant sa commande."
  "|Les allergenes peuvent etre presents dans un ingredient mais aussi dans une sauce, une huile ou une farine utilisee en cuisine."
  "|Le risque de contamination croisee existe lorsque plusieurs plats sont prepares dans le meme ustensile ou sur la meme planche."
  "|La fiche technique d'une recette recense les ingredients, les allergenes, les quantites et les modes de preparation."
  "|La traçabilite permet de retrouver l'origine d'un produit, son fournisseur, son lot et sa date de reception."
  "|Les etiquettes et les bons de livraison doivent être conserves pour reconstituer le parcours d'une denree."
  "|En cas de symptome grave, le personnel doit connaitre la procedure : arreter le service, prevenir les secours et conserver les elements d'analyse."
  "|Le client doit pouvoir poser une question et obtenir une reponse claire, sans que le personnel improvise une affirmation hasardeuse."
  "|La mise a jour des fiches est obligatoire des qu'un ingredient, un fournisseur ou une recette change."),
[QC("Quel reglement europeen encadre l'information sur les allergenes ?", "Le reglement 852/2004~Le reglement 1169/2011~Le reglement 178/2002~Le reglement 2016/679", 1,
     "Le reglement (UE) n° 1169/2011 concerne l'information des consommateurs sur les denrees alimentaires."),
 QC("Combien d'allergenes majeurs sont listes par la reglementation europeenne ?", "8~10~14~20", 2,
     "La liste compte quatorze allergenes majeurs."),
 QC("Quel document recense les allergenes d'une recette ?", "La facture~La fiche technique~Le planning~Le contrat", 1,
     "La fiche technique de recette est l'outil de reference en cuisine."),
 QC("Que permet la traçabilite ?", "Vendre plus cher~Retrouver l'origine et le lot d'un produit~Eviter le nettoyage~Remplacer le fournisseur", 1,
     "Elle permet de remonter le parcours d'une denree en cas de probleme."),
 QT("Un client annonce une allergie aux fruits a coque et commande un dessert. Que faire ?",
     "On l'ecoute et on demande des precisions sur la nature exacte de l'allergie et sur les aliments evites. On consulte la fiche technique du dessert et celle des elements associes : sauce, glace, decoration, huile de cuisson. Si un doute subsiste, on refuse le dessert et on propose une alternative sure, preparee avec des ustensiles propres pour eviter la contamination croisee. On previens la cuisine pour qu'elle applique la procedure, et on indique clairement au client ce qui peut ou non etre consomme. On ne doit jamais affirmer qu'un plat est sans allergene sans avoir verifie les fiches. Enfin, on trace la demande et on met a jour l'information ecrite si une erreur a ete detectee.",
     "On attend verification des fiches, gestion du risque de contamination et absence d'improvisation."),
 QT("Expliquer pourquoi la traçabilite est indispensable en cas d'incident alimentaire.",
     "Si un client tombe malade, l'etablissement doit pouvoir identifier rapidement le produit mis en cause, son fournisseur, son lot, sa date de reception et les plats dans lesquels il a ete utilise. Sans traçabilite, il faut suspendre toute la production, ce qui est couteux et inefficace. Les etiquettes, bons de livraison et registres de reception permettent de circonscrire le retrait au seul lot concerne et d'informer les autorites. La traçabilite facilite aussi la recherche de la cause : erreur de etiquetage, rupture de chaine du froid ou contamination a la reception. Enfin, elle constitue une preuve de la diligence de l'entreprise en cas de controle ou de litige.",
     "On attend identification du lot, retrait cible, recherche de cause et valeur de preuve.")],
C("Informer et tracer, c'est proteger le client et l'etablissement : aucune affirmation sur un allergene ne doit etre improvisee.",
  "Information ecrite + fiches techniques + traçabilite",
  "14 allergenes majeurs · contamination croisee · retrait par lot",
  "Allergene~Substance reactive~Information~Obligation legale~Fiche technique~Recette et allergenes~Contamination croisee~Contact avec ustensile sale~Tracabilite~Origine et lot~Reglement 1169~Texte de reference~Urgence~Procedure de secours",
  "Recenser les allergenes de chaque recette|Afficher l'information au client|Verifier les fiches avant chaque commande|Separer les ustensiles a risque|Conserver etiquettes et bons de livraison",
  "Improviser une reponse au client~Oublier la sauce ou la decoration~Melanger les ustensiles~Ne pas conserver les bons de livraison",
  "14 allergenes~Liste europeenne~Fiche technique~Outil de reference~Lot~Identifiant de production~Reglement 1169/2011~Information client",
  "Allergie~Reaction immunitaire~Intolerance~Reaction digestive",
  "Information~Connaitre~Tracabilite~Retrouver"))

# ============================================================ HY5
add("HY5", "Hygiène personnelle, accidents et évacuation", "Sciences et technologies culinaires", ["1re", "Terminale"],
S("L'hygiene personnelle est la premiere barriere contre la contamination des denrees par les micro-organismes du corps humain."
  "|Le lavage des mains doit etre frequent, effectue avec du savon et de l'eau potable, puis seché avec un essuie-main propre."
  "|Les mains sont lavees avant de manipuler des denrees, apres avoir touché des dechets, apres un deplacement aux toilettes et apres un contact avec un produit cru."
  "|La tenue de travail comprend une veste ou une blouse propre, un couvre-chef, des chaussures fermees et des gants si necessaire."
  "|Les bijoux et les ongles longs sont proscrits en cuisine car ils retiennent les salissures et peuvent tomber dans les plats."
  "|Une personne malade, notamment avec des symptomes digestifs ou une infection cutanee, ne doit pas manipuler d'aliments."
  "|Les accidents du travail en restauration sont frequents : coupures, brulures, glissades, chutes et port de charges."
  "|Les equipements de protection individuels, comme les gants de protection ou les lunettes, completent les mesures collectives."
  "|Chaque accident, meme benigne, doit etre signale, consigné et analysé pour prevenir sa repetition."
  "|La trousse de premiers secours est verifiee regulierement et son emplacement est connu de toute l'equipe."
  "|Le plan d'evacuation indique les issues, les points de rassemblement et les roles de chacun en cas d'incendie."
  "|Les exercices d'evacuation et la formation aux gestes de premiers secours sont des obligations de prevention en entreprise."),
[QC("Quand faut-il se laver les mains en cuisine ?", "Une fois par jour~Avant de manipuler et apres contact sale~Seulement apres le repas~Uniquement avec des gants", 1,
     "Le lavage est requis avant chaque manipulation et apres chaque contact a risque."),
 QC("Quel element est deconseille en cuisine ?", "Un couvre-chef~Des bijoux~Une blouse propre~Des chaussures fermees", 1,
     "Les bijoux retiennent les micro-organismes et peuvent tomber dans les plats."),
 QC("Que faire en cas de coupure ?", "Continuer a travailler~Signaler et soigner selon la procedure~Laver le couteau seulement~Attendre la fin du service", 1,
     "Tout accident doit etre signale et traite immediatement."),
 QC("Que contient le plan d'evacuation ?", "Le menu~Les issues et le point de rassemblement~La carte des vins~Le planning des conges", 1,
     "Le plan d'evacuation organise la sortie en securite et le rassemblement."),
 QT("Decrire les regles d'hygiene personnelle applicables en cuisine et en salle.",
     "La tenue doit etre propre et completee par un couvre-chef qui maintient les cheveux. Les mains sont lavees et sechées avant toute manipulation, apres le contact avec un produit cru, un dechet ou un equipement sale. On retire bijoux et montres, on garde les ongles courts et on evite de tousser ou d'éternuer au-dessus des denrees. En cas de blessure, on couvre la plaie avec un pansement étanche et on porte un gant, ou on est retire de la manipulation si la plaie n'est pas protegeable. Tout symptome infectieux est signale au responsable. En salle, les memes regles s'appliquent, avec une attention supplementaire au contact avec la vaisselle propre et les verres.",
     "On attend tenue, lavage des mains, bijoux, plaies et signalement de maladie."),
 QT("Comment l'etablissement doit-il organiser la prevention des accidents et l'evacuation ?",
     "L'employeur evalue les risques dans le document unique : brulures, coupures, glissades, charges et electricite. Il met en place des mesures collectives comme les revetements antiderapants, les garde-corps et l'entretien des equipements, puis des mesures individuelles comme les gants et les chaussures adaptees. Les salaries sont formes et les accidents consignes avec analyse des causes. Pour l'evacuation, des plans sont affiches, les issues restent degagees, un point de rassemblement est defini et des exercices sont organises. Enfin, une trousse de secours et des personnes formees aux gestes de premiers secours sont designees, avec un numero d'urgence affiche.",
     "On attend evaluation, mesures collectives et individuelles, formation et exercices.")],
C("Hygiene personnelle et prevention des accidents protegent le client, le personnel et la continuite du service.",
  "Mains propres + tenue conforme + comportement responsible",
  "DUERP · EPI · plan d'evacuation · premiers secours",
  "Hygiene personnelle~Barriere contre la contamination~Lavage des mains~Geste repetitif~Tenue~Veste et couvre-chef~EPI~Protection individuelle~Accident du travail~Evenement a signaler~Evacuation~Plan et exercices~Trousse de secours~Premiers soins",
  "Evaluer les risques du poste|Appliquer les regles d'hygiene|Utiliser les protections prevues|Signaler tout incident|Participer aux exercices d'evacuation",
  "Travailler avec une plaie non protegee~Porter des bijoux~Bloquer une issue de secours~Ne pas signaler un accident",
  "Savon et eau~Lavage efficace~Pansement etanche~Protection de plaie~Plan~Document affiche~Exercice~Mise en situation",
  "Prevention~Avant l'accident~Secours~Apres l'accident",
  "Risque~Danger potentiel~Accident~Danger realise"))

# ============================================================ AP1
add("AP1", "Approvisionnement et sélection des fournisseurs", "Économie et gestion hôtelière", ["1re"],
S("L'approvisionnement consiste a mettre a disposition de l'etablissement les denrees et les fournitures necessaires a son activite."
  "|Il concerne aussi bien les produits alimentaires que le linge, la vaisselle, les produits d'entretien et le petit equipement."
  "|Le besoin est exprime par les services : cuisine, etage, salle et maintenance."
  "|Le service achats doit arbitrer entre qualite, prix, delai de livraison et fiabilite du fournisseur."
  "|Un fournisseur est evalue sur ses prix, sa regularite, sa qualite, ses certifications et sa capacite a repondre aux urgences."
  "|La liste des fournisseurs agreee, ou référencement, simplifie les commandes et garantit un niveau de qualite homogene."
  "|Le bon de commande est un document ecrit qui precise le produit, la quantite, le prix et la date de livraison souhaitee."
  "|Le bon de livraison accompagne la marchandise et permet de controler la conformite a la commande."
  "|La reception verifie la quantite, la qualite, la temperature, la date limite et l'etat de l'emballage."
  "|Toute non-conformite doit etre signalee au fournisseur et inscrite sur le bon de livraison avec une réserve."
  "|La facture est comparee au bon de commande et au bon de livraison avant paiement : c'est le controle des trois documents."
  "|Un approvisionnement bien gere limite les ruptures, le gaspillage et les couts d'urgence."),
[QC("Quel document precise le produit, la quantite et le prix avant livraison ?", "Le bon de livraison~Le bon de commande~La facture~Le registre", 1,
     "Le bon de commande est etabli avant la livraison ; le bon de livraison l'accompagne."),
 QC("Que verifie-t-on a la reception des denrees ?", "Le seul prix~La quantite, la qualite, la temperature et la date~Le nom du livreur~La couleur de l'emballage", 1,
     "La reception controle la conformite sanitaire et quantitative."),
 QC("Que signifie le referencement d'un fournisseur ?", "Son inscription dans la liste des fournisseurs agrees~Son licenciement~Une remise unique~Un controle fiscal", 0,
     "Le referencement seleccione les fournisseurs autorises a livrer l'etablissement."),
 QC("Que faire en cas de non-conformite a la livraison ?", "Accepter sans rien dire~Emettre une reserve et prevenir le fournisseur~Payer avant de verifier~Renvoyer sans trace", 1,
     "La reserve ecrite sur le bon de livraison constitue une preuve pour le litige."),
 QT("Decrire le circuit complet d'une commande de denrees, de la demande a la facture.",
     "Le service exprime un besoin : la cuisine demande des legumes ou de la viande selon les previsions de repas. L'acheteur verifie le stock disponible, le fournisseur reference et le prix, puis emet un bon de commande. A la livraison, le receptionnaire compare le bon de livraison au bon de commande, controle la quantite, l'aspect, la temperature et les dates, puis emet des reserves si necessaire. Les produits sont rangees selon la regle FIFO et les donnees sont saisies dans le systeme. La facture du fournisseur est ensuite confrontee aux deux bons avant paiement. Enfin, la qualite du fournisseur est evaluee pour mettre a jour la liste des fournisseurs agrees.",
     "On attend besoin, bon de commande, reception, stockage, controle des trois documents et evaluation."),
 QT("Comment choisir un fournisseur pour un hotel-restaurant ?",
     "On definit d'abord les besoins : nature des produits, volumes, frequence et contraintes de conservation. On consulte plusieurs fournisseurs et on compare leurs prix, leurs conditions de livraison, leurs delais, leurs certifications et leur capacite a fournir en haute saison. On demande des echantillons et on verifie les references d'autres etablissements. On prend aussi en compte la proximite geographique, qui reduit les couts et facilite les livraisons urgentes, ainsi que la qualite des emballages. Enfin, on evalue le fournisseur apres quelques livraisons et on documente la decision. Le choix le moins cher n'est pas toujours le plus rentable si la qualite ou la regularite sont insuffisantes.",
     "On attend comparaison multi-criteres, essai, proximite et evaluation apres mise en oeuvre.")],
C("L'approvisionnement est un circuit documente : commander, recevoir, controler, stocker et payer.",
  "Commande → livraison → reception → facture",
  "Controle des trois documents : commande, livraison, facture",
  "Approvisionnement~Mise a disposition des produits~Referencement~Fournisseurs agrees~Bon de commande~Demande ecrite~Bon de livraison~Preuve de reception~Reserve~Anomalie constatee~Controle~Comparaison des documents",
  "Exprimer le besoin|Choisir le fournisseur reference|Emettre le bon de commande|Controler la livraison|Comparer facture et bons avant paiement",
  "Commander sans verifier le stock~Oublier les reserves~Payer une facture non conforme~Garder un fournisseur non fiable",
  "3 documents~Commande, livraison, facture~FIFO~Rotation du stock~Temperature~Critere de reception~Reserve~Preuve d'anomalie",
  "Bon de commande~Avant~Bon de livraison~Pendant~Facture~Apres",
  "Qualite~Conformite du produit~Prix~Cout d'achat"))

# ============================================================ AP2
add("AP2", "Gestion des stocks, inventaires et coût de revient", "Économie et gestion hôtelière", ["1re", "Terminale"],
S("Un stock est un ensemble de biens conserves par l'entreprise pour faire face a sa consommation future."
  "|On distingue les stocks de matieres premires, de produits en cours et de produits finis, ainsi que les fournitures et le linge."
  "|Le stock de securite couvre la consommation pendant le delai de livraison et protege contre les variations de demande."
  "|Le stock minimum declenche une nouvelle commande : c'est le point de commande."
  "|Le stock maximum evite l'immobilisation de capital et les pertes par deterioration ou vol."
  "|La rotation des stocks rapporte le cout de consommation au stock moyen : elle measure la vitesse de renouvellement."
  "|L'inventaire permanent met a jour les quantites apres chaque entree ou sortie, grace au systeme informatique."
  "|L'inventaire tournant compte physiquement une partie des stocks a intervalles reguliers, sans arreter l'activite."
  "|L'inventaire general, souvent annuel, compte l'ensemble des stocks et sert a la clôture des comptes."
  "|Un ecart d'inventaire peut provenir d'une erreur de saisie, d'un vol, d'une deterioration ou d'une consommation non enregistree."
  "|Le cout de revient d'une preparation comprend les matieres premieres, la main-d'oeuvre directe et une part des charges indirectes."
  "|Une bonne gestion des stocks reduit le cout de revient en limitant les pertes et en évitant les achats d'urgence."),
[QC("Que designe le stock de securite ?", "Le stock invite~Un stock tampon contre les variations de demande~Le stock maximum~Le stock des fournitures", 1,
     "Le stock de securite couvre le delai de livraison et les aléas."),
 QC("A quoi sert le point de commande ?", "A fixer le prix~A declencher une nouvelle commande~A fermer l'etablissement~A calculer la TVA", 1,
     "Lorsque le stock atteint le seuil, on passe commande."),
 QC("Quel inventaire compte physiquement une partie des stocks par periode ?", "L'inventaire general~L'inventaire tournant~L'inventaire comptable~Aucun", 1,
     "L'inventaire tournant compte une partie des references sans arreter l'activite."),
 QC("Que comprend le cout de revient d'un plat ?", "Les seules matieres~Matiere, main-d'oeuvre et charges indirectes~Le seul prix de vente~La TVA", 1,
     "Le cout de revient englobe les charges directes et une part des charges indirectes."),
 QC("Quelle cause peut expliquer un ecart d'inventaire ?", "Une commande arrivee~Une erreur de saisie ou un vol~Une hausse de prix~Un nouveau fournisseur", 1,
     "Les ecarts viennent d'erreurs, de vols, de pertes ou de consommations non tracees."),
 QT("Un etablissement consomme 12 000 € de denrees par an pour un stock moyen de 2 000 €. Calculer la rotation et l'interpretation.",
     "La rotation des stocks vaut 12 000 / 2 000 = 6 fois par an. Cela signifie que le stock de denrees est renouvele en moyenne six fois dans l'annee, soit environ tous les deux mois. Une rotation elevee indique une bonne maitrise : peu de capital immobilise et peu de risque de peremption. Une rotation tres faible peut signaler un surstock, des achats excessifs ou des produits peu consommes. Il faut neanmoins la comparer a la rotation habituelle du secteur et au type de produit : le linge et la vaisselle ont une rotation beaucoup plus lente que les denrees fraiches.",
     "On attend 6 fois par an et interpretation nuancese selon la famille de produits."),
 QT("Expliquer la difference entre inventaire permanent et inventaire tournant et leur complementarite.",
     "L'inventaire permanent est une gestion comptable continue : chaque entree ou sortie est enregistree dans le systeme, qui affiche a tout moment le stock theoriique. Il est rapide mais peut s'ecarter de la realite en cas d'erreurs de saisie, de vol ou de pertes non constatees. L'inventaire tournant consiste a compter physiquement une partie des references selon un calendrier, par exemple les produits frais chaque semaine et le linge chaque mois. Il detecte les ecarts sans fermer l'etablissement. Les deux methodes sont complementaires : l'inventaire permanent pilote les commandes au quotidien, tandis que les comptages tournants verifient et corrigent les donnees. L'inventaire general reste necessaire pour la clôture annuelle.",
     "On attend definition des deux methodes et justification de leur complementarite.")],
C("Le stock est un capital immobilise : le piloter, c'est concilier disponibilite et maitrise des couts.",
  "Rotation = consommation / stock moyen",
  "Stock de securite · point de commande · inventaire permanent et tournant",
  "Stock~Bien conserve~Stock de securite~Tampon de protection~Point de commande~Seuil de recommandation~Rotation~Vitesse de renouvellement~Inventaire~Comptage physique~Cout de revient~Matiere, main-d'oeuvre, charges",
  "Classer les produits par famille|Fixer stocks minimum et maximum|Enregistrer entrees et sorties|Planifier les comptages tournants|Analyser les ecarts et corriger",
  "Confondre stock et consommation~Ne jamais compter physiquement~Laisser un surstock perime~Oublier les sorties non facturees",
  "12 000 €~Consommation annuelle~2 000 €~Stock moyen~6 rotations~Renouvellement~Ecart~Difference entre theorie et reel",
  "Inventaire permanent~Theorique et continu~Inventaire tournant~Physique et partiel",
  "Stock minimum~Seuil d'alerte~Stock maximum~Limite d'immobilisation"))

# ============================================================ AP3
add("AP3", "Food cost et calcul du prix de vente", "Économie et gestion hôtelière", ["Terminale"],
S("Le food cost, ou cout des matieres premieres, represente la part du chiffre d'affaires consacree aux denrees."
  "|Il se calcule en divisant le cout d'achat des denrees consommees par le chiffre d'affaires alimentaire hors boissons."
  "|Un food cost de 30 % signifie que 30 € de chaque 100 € de ventes alimentaires servent a payer les denrees."
  "|Le food cost theorique est calcule a partir des fiches techniques et des prix d'achat ; le food cost reel tient compte des pertes."
  "|L'ecart entre food cost reel et theorique revele les gaspillages, les voles, les erreurs de portion ou les erreurs de saisie."
  "|Le prix de vente d'un plat doit couvrir le cout de la matiere, la main-d'oeuvre, les charges et dégager une marge."
  "|Le taux de marque est la marge brute divisée par le prix de vente ; le taux de marge est la marge divisée par le cout d'achat."
  "|Un plat dont la matiere coute 6 € et vendu 20 € degage une marge brute de 14 €, soit un taux de marque de 70 %."
  "|La methode du coefficient multiplicateur consiste a multiplier le cout matiere par un coefficient determine par le food cost vise."
  "|Si le food cost vise est 30 %, le coefficient est 1 / 0,30, soit environ 3,33 ; un cout de 6 € donne un prix de 20 €."
  "|Le price eating designe l'augmentation du prix des matieres : il faut alors ajuster le prix de vente, la recette ou la portion."
  "|Le food cost doit etre suivi chaque semaine et compare aux objectifs du budget pour declencher des actions correctives."),
[QC("Comment calculer le food cost ?", "Denrees / CA alimentaire~CA / denrees~Denrees + CA~Denrees - CA", 0,
     "Le food cost est le rapport entre cout des denrees consommees et chiffre d'affaires alimentaire."),
 QC("Un food cost de 30 % signifie que...", "30 € de benéfice pour 100 €~30 € de denrees pour 100 € de ventes~30 % de marge~30 plats vendus", 1,
     "Il represente la part des ventes consacree aux matieres premieres."),
 QC("Quel est le taux de marque d'un plat achete 6 € et vendu 20 € ?", "30 %~40 %~70 %~233 %", 2,
     "La marge est 14 € et 14/20 = 70 % du prix de vente."),
 QC("Quel coefficient correspond a un food cost vise de 25 % ?", "1,25~2,5~4~0,25", 2,
     "Le coefficient vaut 1 / 0,25 = 4."),
 QT("Un plat coute 7 € en matieres. Quel prix de vente pour un food cost de 35 % ? Quelle marge brute ?",
     "Le coefficient multiplicateur vaut 1 / 0,35, soit environ 2,857. Le prix de vente est donc 7 × 2,857 = 20 € environ. La marge brute est de 20 - 7 = 13 €. Le taux de marque est 13 / 20 = 65 % et le taux de marge sur cout est 13 / 7, soit environ 185,7 %. Ce calcul est une premiere etape : il faut verifier que 20 € correspond au positionnement de la carte, que la portion est acceptable pour le client et que le plat reste competitif par rapport aux autres du menu.",
     "On attend coefficient 1/0,35, prix 20 € et marge 13 € avec verification commerciale."),
 QT("Le food cost reel est superieur au food cost theorique. Quelles causes chercher et quelles actions mener ?",
     "On compare d'abord les fiches techniques aux portions reellement servies : une portion trop generateuse augmente le cout. On verifie ensuite les prix d'achat reels, les pertes a la reception, la peremption, les erreurs de saisie et les plats offerts non enregistres. Les vols ou les consommations du personnel peuvent aussi expliquer l'ecart. On observe les pratiques en cuisine et on organise des comptages. Les actions consistent a corriger les fiches, former les equipes au dosage, ajuster les prix d'achat, renegocier avec les fournisseurs et, si necessaire, reviser le prix de vente. Un suivi hebdomadaire permet de mesurer l'effet des corrections.",
     "On attend recherche des causes, actions correctives et suivi dans le temps.")],
C("Le food cost relie achats et ventes : il pilote le prix de vente et révèle les pertes.",
  "Food cost = cout denrees / CA alimentaire",
  "Coefficient = 1 / food cost vise · marge = prix de vente - cout",
  "Food cost~Part des denrees dans les ventes~Theorique~Calcule par fiches~Reel~Apres pertes et gaspillage~Marge brute~Vente moins cout~Coefficient~Multiplicateur du cout~Price eating~Hausse du prix d'achat~Taux de marque~Marge sur prix de vente",
  "Calculer le cout matiere par fiche|Choisir le food cost objectif|Appliquer le coefficient|Comparer au positionnement de la carte|Suivre l'ecart reel et corriger",
  "Confondre marge et taux de marque~Oublier les pertes dans le calcul~Vendre sous le cout de revient~Ne pas revoir les prix apres hausse",
  "7 €~Cout matiere~35 %~Food cost vise~20 €~Prix de vente~13 €~Marge brute~65 %~Taux de marque",
  "Food cost theorique~Sans pertes~Food cost reel~Avec pertes",
  "Taux de marque~Marge sur vente~Taux de marge~Marge sur cout"))

# ============================================================ AP4
add("AP4", "Lutte contre le gaspillage et valorisation des invendus", "Économie et gestion hôtelière", ["Terminale"],
S("Le gaspillage alimentaire represente les denrees achetees puis jetees sans avoir ete consommees."
  "|En restauration, il provient des surplus de commandes, des portions trop grandes, des pertes de stockage et des restes de clients."
  "|Le gaspillage a un cout direct : il faut racheter ce qui a ete jete, ce qui augmente le food cost reel."
  "|Il a aussi un cout environnemental : production, transport et traitement des dechets consomment des ressources et emettent des gaz."
  "|La premiere etape de la lutte est la mesure : peser les dechets par famille et identifier les moments ou ils apparaissent."
  "|La previsions de frequentation, fondees sur l'historique et les evenements, permettent d'ajuster les commandes."
  "|La gestion des portions et le choix d'un menu plus court reduisent les restes en cuisine et dans les assiettes."
  "|La valorisation des invendus peut passer par la vente a prix reduit, le don a des associations habilitées ou la transformation."
  "|Le don de denrees doit respecter la reglementation sanitaire et une procedure ecrite de collecte et de tracabilite."
  "|Les dechets organiques peuvent etre compostes ou envoyes en methanisation selon les filieres locales."
  "|Les parties non utilisees d'un produit peuvent servir a d'autres preparations : bouillon, sauce, garniture ou personnel."
  "|La reduction du gaspillage est un enjeu economique, social et environnemental qui s'inscrit dans la demarche RSE de l'etablissement."),
[QC("Quelle est la premiere etape pour lutter contre le gaspillage ?", "Jeter moins cher~Mesurer et identifier les dechets~Acheter davantage~Changer de fournisseur", 1,
     "On ne peut agir qu'apres avoir mesure et localise les pertes."),
 QC("Quel effet direct du gaspillage sur le food cost reel ?", "Il le fait baisser~Il le fait augmenter~Il n'a aucun effet~Il le rend negatif", 1,
     "Les denrees jetees sont achetees mais ne generent pas de vente : le food cost augmente."),
 QC("Quelle condition doit respecter le don de denrees ?", "Etre gratuit~Respecter la reglementation sanitaire et etre trace~Etre anonyme~Concerner uniquement les boissons", 1,
     "Le don doit etre securise, conforme et documente."),
 QT("Un restaurant jete 18 kg de dechets alimentaires par semaine pour 6 000 € d'achats. Expliquer l'enjeu et les actions possibles.",
     "D'abord, on quantifie : 18 kg par semaine representent prpres de 940 kg par an. A un cout moyen de 4 € le kilo, cela represente environ 3 760 € d'achats jetes chaque annee, qui rencherissent le food cost. On identifie ensuite les origines : portions trop grandes, commandes excessives avant le week-end, pertes de legumes ou restes de buffet. Les actions consistent a ajuster les previsions grace a l'historique, a revoir les grammages, a mieux stocker selon la regle FIFO, a proposer des portions differentes et a valoriser les invendus conformes par le don ou la vente a prix reduit. On mesure a nouveau apres un mois pour verifier la baisse.",
     "On attend quantification, recherche des causes, actions et remesure."),
 QT("Comment mettre en place une demarche de lutte contre le gaspillage dans un etablissement ?",
     "On commence par une campagne de pesee des dechets sur une periode representatif pour connaitre les volumes et les causes. On fixe ensuite un objectif chiffre, par exemple reduire de 20 % les dechets en six mois, et on designe un responsable. On agit sur les leviers : previsions de commande, taille des portions, rotation des stocks, formation des equipes, affichage des bonnes pratiques et recettes d'utilisation des restes. On organise une filiere de dons avec une association agreee si les conditions sanitaires le permettent, et une filiere de compostage pour les dechets non valorisables. Enfin, on suit des indicateurs, on communique les resultats aux equipes et on integre la demarche dans le plan RSE.",
     "On attend mesure, objectif, actions, filieres de valorisation et suivi.")],
C("Le gaspillage est un cout cache : le mesurer permet d'agir sur les commandes, les portions et les filieres de valorisation.",
  "Gaspillage = achats jetes sans vente",
  "Mesurer · prevoir · doser · valoriser · remesurer",
  "Gaspillage~Denree jetee~Food cost reel~Augmente avec les pertes~Prevision~Estimation de la demande~Portion~Quantite servie~Don~Valorisation solidaire~Compostage~Filiere de dechets",
  "Peser les dechets par famille|Identifier les causes et les moments|Fixer un objectif de reduction|Ajuster commandes et portions|Valoriser et remesurer",
  "Ignorer les pertes~Ne pas tracer les dons~Surcommander par habitude~Jeter des produits encore conformes",
  "18 kg~Dechets hebdomadaires~940 kg~Projection annuelle~20 %~Objectif de reduction~FIFO~Rotation des stocks~RSE~Demarche responsable",
  "Gaspillage~Perte economique~Valorisation~Reutilisation utile",
  "Don~Usage social~Compostage~Usage environnemental"))

# FIN DES LOTS
valider_et_ecrire(F, "sthr-mat-part-B.json")
