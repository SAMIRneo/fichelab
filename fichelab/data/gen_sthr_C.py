# -*- coding: utf-8 -*-
"""Generateur sthr-mat-part-C.json — lot C : gestion comptable, droit, marketing,
anglais professionnel hôtelier, environnement et developpement durable.

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
 "CO2": [QC("Quel taux s'applique a la vente de boissons alcoolisees ?", "5,5 %~10 %~20 %~0 %", 2,
            "Les boissons alcoolisees relevent du taux normal de 20 %."),
         QC("Que sont les charges sociales ?", "Des impots sur les benefices~Des cotisations ajoutees au salaire brut~Des taxes de sejour~Des commissions OTA", 1,
            "Les cotisations employeur et salariales s'ajoutent au salaire brut.")],
 "CO3": [QC("Quelle est une charge indirecte ?", "La matiere premiere~Les frais generaux~La main-d'oeuvre directe~Le prix d'achat d'un plat", 1,
             "Les frais generaux sont communs a plusieurs prestations."),
         QC("A quoi sert une cle de repartition ?", "A fixer le prix~A repartir les charges indirectes~A calculer la TVA~A clore les comptes", 1,
            "La cle permet d'affecter les charges indirectes aux centres."),
         QC("Que faut-il comparer au prix de revient ?", "La taxe de sejour~Le prix de vente~Le salaire~Le bilan", 1,
            "La comparaison avec le prix de vente revelle la marge.")],
 "CO4": [QC("Que contient le budget d'investissement ?", "Les seules ventes~Les depenses durables~Les salaires~Les commissions", 1,
             "Il recense les acquisitions de biens durables."),
         QC("Qui propose les besoins dans une demarche participative ?", "Le seul comptable~Les responsables de services~Les clients~Les fournisseurs", 1,
            "Les responsables de services remontent leurs besoins a la direction."),
         QC("Un ecart defavorable signifie que...", "Le realise depasse le budget~Le realise est moins bon que le budget~Le budget est nul~Il n'y a pas d'ecart", 1,
            "Un ecart defavorable traduit une performance inferieure a la prevision.")],
 "CO5": [QC("Que se passe-t-il au-dessus du seuil de rentabilite ?", "Une perte~Un benefice~Un resultat nul~Aucune activite", 1,
             "Au-dela du seuil, les produits depassent les charges."),
         QC("Que divise-t-on par la marge unitaire pour obtenir le seuil ?", "Les ventes~Les charges fixes~Le prix~Le volume", 1,
            "Le seuil en volume vaut charges fixes / marge unitaire."),
         QC("Quel indicateur suit le niveau d'activite d'un hotel ?", "Le nombre d'etoiles~Le taux d'occupation~Le prix du pain~La date", 1,
            "Le taux d'occupation mesure l'utilisation de la capacite.")],
 "DR1": [QC("Quand une licence est-elle transferee ?", "A chaque fin d'annee~Lors d'une vente ou d'un changement d'exploitant~Jamais~A l'ouverture d'une commune", 1,
             "Le transfert accompagne generalement la vente de l'etablissement."),
         QC("Que risque un etablissement qui vend de l'alcool a un mineur ?", "Rien~Une amende et des sanctions~Une reduction de taxe~Un label", 1,
            "La vente d'alcool aux mineurs est un delit.")],
 "DR2": [QC("Quelle periode permet d'evaluer le salarie en debut de contrat ?", "Le preavis~La periode d'essai~Le conge~La formation", 1,
             "La periode d'essai est encadree par la loi et la convention collective."),
         QC("Qui verse les cotisations employeur ?", "Le salarie~L'employeur~Le client~La caisse d'allocations", 1,
            "Les cotisations employeur sont a la charge de l'entreprise."),
         QC("Quel document est remis en fin de contrat ?", "Le contrat de vente~Le certificat de travail~La carte~Le devis", 1,
            "Le certificat de travail fait partie des documents de fin de contrat.")],
 "DR3": [QC("Quel est le role du registre des depots ?", "Fixer le prix~Prouver la remise et le retrait~Remplacer l'assurance~Afficher les tarifs", 1,
            "Le registre est la preuve ecrite du depot et de sa restitution."),
         QC("Qui doit etre prevenu en cas de vol ?", "Personne~La direction et l'assurance~Le fournisseur~Le client suivant", 1,
            "La direction et l'assurance doivent etre informees sans delai."),
         QC("Que peut prevenir un sol glissant ?", "Une erreur de facture~Une chute~Un vol~Une panne informatique", 1,
            "L'entretien des sols est une mesure de prevention des chutes.")],
 "DR4": [QC("Quel service controle les prix et la concurrence ?", "La DREETS~La DGCCRF~La mairie seule~La prefecture seule", 1,
             "La DGCCRF est le service de la concurrence, de la consommation et de la repression des fraudes."),
         QC("A quoi sert le plan d'evacuation ?", "A afficher les prix~A guider l'evacuation~A presenter le menu~A former les cuisiniers", 1,
            "Le plan indique issues et point de rassemblement."),
         QC("Quelle consequence d'une issue de secours condamnee ?", "Aucune~Une infraction~Une remise~Une certification", 1,
            "Condamner une issue est une infraction au reglement de securite.")],
 "DR5": [QC("Quel est le role de la CNIL ?", "Controler les prix~Controler la protection des donnees~Gerer les licences~Former les cuisiniers", 1,
             "La CNIL est l'autorite de controle en matiere de donnees personnelles."),
         QC("Quelle donnee ne doit jamais etre notee sur papier ?", "Le nom~La date de sejour~Le numero complet de carte~Le numero de chambre", 2,
            "Le numero complet de carte est une donnee bancaire sensible."),
         QC("Que signifie la minimisation ?", "Tout collecter~Collecter le necessaire seulement~Ne rien conserver~Vendre les donnees", 1,
            "On limite la collecte aux donnees utiles a la finalite.")],
 "MK1": [QC("Quel critere de segmentation concerne le motif du voyage ?", "Geographique~Comportemental~Demographique~Psychographique", 1,
             "Le motif d'achat et la frequentation sont des criteres comportementaux."),
         QC("Quel outil compare les concurrents sur deux axes ?", "Le budget~La carte de positionnement~La facture~Le plan HACCP", 1,
            "La carte projective place les concurrents sur deux axes choisis."),
         QC("Que doit etre une promesse marketing ?", "Toujours la moins chere~Coherente avec les prestations~Inventee~Identique a celle des concurrents", 1,
            "Une promesse non tenue detruit la confiance du client.")],
 "MK2": [QC("Que designe le produit hotelier ?", "Une seule chambre~Un service composite~Un prix fixe~Un contrat", 1,
             "Le produit hotelier combine chambre, services et experience."),
         QC("Quel est un avantage de la reservation directe ?", "Une commission plus elevee~L'absence de commission~Une taxe supplementaire~Un prix plus eleve", 1,
            "Le canal direct evite la commission des plateformes."),
         QC("Que mesure le RevPAR ?", "Le cout du personnel~La performance par chambre disponible~Le nombre d'etoiles~La duree du sejour", 1,
            "Le RevPAR combine occupation et prix moyen.")],
 "MK3": [QC("Quel canal sert surtout a creer de l'attachement ?", "Le site~Les reseaux sociaux~La facture~Le PMS", 1,
             "Les reseaux sociaux entretiennent la relation et la communaute."),
         QC("Quel contenu est utile sur un site d'hotel ?", "Des textes sans interet~Des photos et avis clients~Des donnees bancaires~Des plannings", 1,
            "Les visuels et les avis aident la decision de reservation."),
         QC("Quel est un risque d'une publicite en ligne mal mesuree ?", "Une baisse des prix~Un cout d'acquisition eleve~Une hausse de la note~Aucun risque", 1,
            "Sans mesure, la publicite peut couter plus cher qu'elle ne rapporte.")],
 "MK4": [QC("Quel indicateur suit la repetition des sejours ?", "Le food cost~Le taux de repetition~La taxe de sejour~Le RevPAR", 1,
             "Le taux de repetition mesure la fidelite des clients."),
         QC("Quand solliciter un avis client ?", "Pendant le repas~Apres le depart~Avant la reservation~Jamais", 1,
            "La demande apres le depart est la plus naturelle."),
         QC("Quel element ne doit pas apparaitre dans une reponse a un avis ?", "Un remerciement~Une donnee personnelle~Une solution~Une excuse", 1,
            "La reponse doit proteger la vie privee du client.")],
 "AH1": [QC("What document is usually asked at check-in ?", "A photo~A valid identity document~A recipe~A newspaper", 1,
             "A valid identity document is required for registration."),
         QC("What does « vacant » mean ?", "Occupied~Available~Closed~Expensive", 1,
            "Vacant means the room is available."),
         QC("How should the receptionist end the check-in ?", "By saying nothing~By wishing a pleasant stay~By asking the guest to leave~By giving the bill", 1,
            "A polite closing wish is standard in professional service.")],
 "AH2": [QC("Which phrase asks for the bill ?", "« Could I have the menu? »~« Could I have the bill, please? »~« Where is the kitchen? »~« What time is it? »", 1,
             "This is the standard polite request for the bill."),
         QC("What is « cutlery » ?", "Plates~Forks, knives and spoons~Glasses~Napkins", 1,
            "Cutlery refers to forks, knives and spoons."),
         QC("What does « a table for two » mean ?", "A table for twenty~A table for two people~Two separate tables~A table near the door", 1,
            "The phrase indicates the number of guests.")],
 "AH3": [QC("What does « I am sorry to hear that » express ?", "A refusal~An apology~A question~A price", 1,
             "It is a standard phrase of apology and empathy."),
         QC("Which subject line is professional ?", "« Problem!!! »~« Your stay - room 214 »~« Help »~« Hello »", 1,
            "A clear subject line identifies the topic and the context."),
         QC("What should the server do if the guest is still unhappy ?", "Ignore the guest~Call a supervisor~Argue~Leave the room", 1,
            "The employee escalates to a supervisor instead of improvising.")],
 "EN1": [QC("Quelle est la finalite d'une ACV ?", "Calculer le prix~Evaluer les impacts du cycle de vie~Fixer la taxe~Compter les clients", 1,
             "L'ACV mesure les impacts environnementaux de la matiere premiere a la fin de vie."),
         QC("Quel est un risque du greenwashing ?", "Une baisse des couts~Une communication trompeuse~Une hausse de l'occupation~Une certification", 1,
            "Le greenwashing presente des engagements non reels."),
         QC("Que contient un plan d'action RSE ?", "Le menu~Des objectifs et indicateurs~La facture~Le planning des conges", 1,
            "Un plan fixe objectifs, indicateurs, responsables et echeances.")],
 "EN2": [QC("Quel equipement reduit la consommation d'eclairage ?", "Les ampoules incandescentes~Les LED et detecteurs de presence~Les radiateurs~Les robinets", 1,
             "Les LED et les detecteurs limitent la consommation."),
         QC("Que faire d'une fuite d'eau ?", "L'ignorer~La detecter et la reparer~Augmenter le debit~La signaler en fin d'annee", 1,
            "Une fuite doit etre traitee des qu'elle est detectee."),
         QC("Quel flux de dechets necessite une filiere specifique ?", "Le papier~Les dechets dangereux~Le verre~Le carton", 1,
            "Les dechets dangereux suivent une filiere dediee et tracee.")],
 "EN3": [QC("Quelle est une consequence de la saisonnalite ?", "Une repartition uniforme~Une concentration des flux~Une baisse permanente des prix~Une capacite illimitEE", 1,
             "Les touristes se concentrent sur quelques mois de l'annee."),
         QC("Qui verifie un label environnemental ?", "L'hotelier~Un organisme tiers~Le client~Le concurrent", 1,
            "Le label implique une verification externe et independante."),
         QC("Que doit-on faire apres l'obtention d'un label ?", "S'arreter~Maintenir et renouveler~Changer de nom~Communiquer sans preuve", 1,
            "La certification doit etre maintenue et renouvelee.")],
}

# ============================================================ CO1
add("CO1", "Comptabilité générale : bilan et compte de résultat", "Économie et gestion hôtelière", ["Terminale"],
S("La comptabilite generale enregistre, classe et restitue les flux economiques de l'etablissement."
  "|Le bilan est un document de synthese qui decrit le patrimoine a une date donnee, generalement la fin de l'exercice."
  "|Le bilan se divise en deux parties : l'actif, qui represente les emplois, et le passif, qui represente les ressources."
  "|L'actif immobilise rassemble les biens durables : materiel, mobilier, constructions et materiel de cuisine."
  "|L'actif circulant comprend les stocks, les creances clients et la tresorerie disponible."
  "|Au passif, les capitaux propres representent les apports des proprietaires et les benefices non distribues."
  "|Les dettes sont classees selon leur echeance : moins d'un an ou plus d'un an."
  "|Le compte de resultat recapitule les produits et les charges sur un exercice, generalement douze mois."
  "|Le resultat est la difference entre les produits et les charges : il peut etre benefice ou perte."
  "|Le plan comptable general organise les comptes en classes numerotees de 1 a 8."
  "|Une ecriture comptable comporte au moins deux comptes : un debit et un credit de montant egal."
  "|Le bilan et le compte de resultat sont completes par une annexe qui precise les methodes, les engagements et les evenements post-cloture."),
[QC("Que decrit le bilan d'un etablissement ?", "Les seules ventes du jour~Le patrimoine a une date donnee~Les salaires~La carte du restaurant", 1,
     "Le bilan est une photographie du patrimoine a une date precise."),
 QC("Comment appelle-t-on la partie du bilan qui contient les dettes ?", "L'actif~Le passif~Le resultat~L'annexe", 1,
     "Les ressources, dont les dettes, figurent au passif."),
 QC("Quel element appartient a l'actif circulant ?", "Le materiel de cuisine~Les stocks~Les capitaux propres~Le mobilier", 1,
     "Les stocks, creances et tresorerie constituent l'actif circulant."),
 QC("Que recapitule le compte de resultat ?", "Le patrimoine~Les produits et les charges de l'exercice~Les seuls stocks~Les seuls salaires", 1,
     "Le compte de resultat mesure l'activite sur une periode."),
 QC("Comment calculer le resultat comptable ?", "Produits plus charges~Produits moins charges~Charges divisées par produits~Actif moins Passif", 1,
     "Le resultat = produits - charges."),
 QC("Combien de classes compte le plan comptable general ?", "5~6~7~8", 3,
     "Les comptes sont repartis en huit classes, de 1 a 8."),
 QC("Quelle regle s'applique a toute ecriture comptable ?", "Un seul compte suffit~Le debit doit egaler le credit~Le credit est toujours plus eleve~Aucune regle", 1,
     "L'equilibre debit/credit est la regle fondamentale de la comptabilite en partie double."),
 QT("Classer les elements suivants : un four, un stock de denrees, une dette fournisseur, les capitaux propres.",
     "Le four est un bien durable : il figure a l'actif immobilise. Le stock de denrees est un bien destine a etre consomme rapidement : il figure a l'actif circulant. La dette envers le fournisseur est une ressource exterieure : elle figure au passif, parmi les dettes a court terme. Les capitaux propres representent les apports et les benefices conserves : ils figurent egalement au passif. On verifie que le total de l'actif egale le total du passif, ce qui traduit l'equilibre du bilan.",
     "On attend classement actif immobilise, actif circulant, dettes et capitaux propres, avec verification de l'equilibre."),
 QT("Expliquer la difference entre le bilan et le compte de resultat et leur complementarite.",
     "Le bilan decrit la situation patrimoniale a un instant donne : ce que l'entreprise possede et comment elle l'a finance. Le compte de resultat decrit l'activite sur une periode : les produits realises, les charges engagees et le benefice ou la perte qui en resulte. Le bilan est une photographie, le compte de resultat est un film. Ils sont lies : le resultat de l'exercice est reporte dans les capitaux propres du bilan, et l'augmentation de la tresorerie ou des creances se retrouve a l'actif. Leur lecture croisee permet de juger a la fois la rentabilite et la structure financiere de l'etablissement.",
     "On attend image instantanee versus flux sur periode, et lien par le resultat et la tresorerie.")],
C("Le bilan photographie le patrimoine, le compte de resultat filme l'activite : tous deux s'equilibrent et se completent.",
  "Resultat = produits - charges · Actif = Passif",
  "Actif = emplois · Passif = ressources · Credit = debit",
  "Bilan~Patrimoine a une date~Actif~Emplois de l'entreprise~Passif~Ressources et dettes~Compte de resultat~Produits et charges~Resultat~Benefice ou perte~Ecriture~Debit et credit",
  "Identifier la nature de chaque element|Classer a l'actif ou au passif|Distinger immobilise et circulant|Relier produits et charges|Verifier les egalites",
  "Confondre actif et passif|Oublier l'annexe|Ecrire une ecriture desequilibree|Lire le bilan comme un flux",
  "Four~Actif immobilise~Stock~Actif circulant~Dette~Passif~12 mois~Duree d'un exercice~8 classes~Plan comptable",
  "Bilan~Photo a une date~Compte de resultat~Film sur une periode",
  "Produits~Ventes et recettes~Charges~Achats et couts"))

# ============================================================ CO2
add("CO2", "TVA et fiscalité de l'établissement", "Économie et gestion hôtelière", ["Terminale"],
S("La taxe sur la valeur ajoutee, ou TVA, est un impot indirect sur la consommation finalement supporte par le client."
  "|Les entreprises assujetties collectent la TVA sur leurs ventes et la reversent a l'Etat, apres deduction de la TVA payee sur leurs achats."
  "|La TVA deduisible est celle qui figure sur une facture conforme au nom et au numero de TVA de l'entreprise."
  "|Le taux normal francais est de 20 % ; des taux reduits de 10 % et 5,5 % s'appliquent a certains produits ou services."
  "|La restauration est generalement soumise au taux de 10 %, tandis que la vente de boissons alcoolisees releve du taux normal."
  "|L'hbergement est soumis a des regles particuliieres : la taxe de sejour est collectee pour le compte de la collectivite."
  "|La taxe de sejour est fixee par la commune ou l'intercommunalite selon une grille de tarifs et la categorie de l'etablissement."
  "|La contribution economique territoriale et la taxe fonciere sont des impots locaux lies aux locaux professionnels."
  "|Les charges sociales, notamment les cotisations URSSAF, s'ajoutent au salaire brut et augmentent le cout de la main-d'oeuvre."
  "|La facture doit mentionner le taux de TVA, le montant de la taxe et le total TTC : c'est une obligation legale."
  "|Une erreur de taux ou une omission de TVA peut entrainer un redressement et des penalities."
  "|La tenue de comptes conformes et le respect des echeances de declaration sont indispensables a la securite juridique de l'etablissement."),
[QC("Qui supporte finalement la TVA ?", "Le fournisseur~Le consommateur final~L'Etat~La banque", 1,
     "La TVA est collectee par l'entreprise mais supportee par le client final."),
 QC("Quel taux normal s'applique en France ?", "5,5 %~10 %~20 %~33 %", 2,
     "Le taux normal de la TVA francaise est de 20 %."),
 QC("Quel taux concerne generalement la restauration ?", "5,5 %~10 %~20 %~0 %", 1,
     "Les prestations de restauration relevent generalement du taux reduit de 10 %."),
 QC("Qui fixe la taxe de sejour ?", "L'hotelier seul~La commune ou l'intercommunalite~Le departement~L'Etat par decret annuel", 1,
     "La collectivite territoriale fixe le montant de la taxe de sejour."),
 QC("Que doit mentionner une facture conforme ?", "Le seul total TTC~Le taux et le montant de la TVA~Le nom du serveur~La date de naissance du client", 1,
     "La facture doit faire apparaitre le detail de la TVA."),
 QT("Un repas est facture 55 € TTC avec une TVA de 10 %. Calculer le montant HT et la TVA.",
     "Le montant TTC represente 110 % du montant HT, donc HT = 55 / 1,10 = 50 €. La TVA est egale a 55 - 50 = 5 €, soit 10 % de 50 €. On peut aussi la calculer directement par 55 × 10/110 = 5 €. La facture doit faire apparaitre les trois montants : base HT de 50 €, TVA de 5 € au taux de 10 %, total TTC de 55 €. Une erreur frequente consiste a calculer 10 % de 55 €, ce qui donnerait 5,50 € et un total incorrect.",
     "On attend HT 50 €, TVA 5 €, et la mise en garde contre 10 % du TTC."),
 QT("Distinguer TVA deductible et taxe de sejour dans la gestion d'un hotel.",
     "La TVA deductible est un impot sur la consommation : l'hotel la collecte sur ses ventes, peut deduire celle qu'il a payee sur ses achats et reverse la difference a l'Etat. Elle est neutre pour l'entreprise si la comptabilite est conforme. La taxe de sejour, elle, est collectee aupres du client pour le compte de la commune : elle ne constitue ni un produit ni une charge pour l'etablissement, mais une somme a reverser. Elle varie selon la categorie de l'hotel et le nombre de nuits. Les deux montants doivent etre distincts sur la facture et dans les comptes, car leur destination et leur regime juridique different.",
     "On attend neutralite de la TVA deductible et nature de collecte pour compte d'autrui de la taxe de sejour.")],
C("La fiscalite d'un etablissement combines TVA, impots locaux et taxes collectees pour le compte d'autrui.",
  "TTC = HT × (1 + taux) · TVA = TTC - HT",
  "TVA deductible · taxe de sejour · charges sociales",
  "TVA~Impot sur la consommation~Deductible~TVA sur achats recuperee~TTC~Toutes taxes comprises~Taxe de sejour~Collectee pour la commune~Taux normal~20 %~Charges sociales~Cotisations employeur",
  "Identifier le regime fiscal applicable|Verifier les taux sur les factures|Calculer la base HT et la taxe|Collecter la taxe de sejour|Reverse et declarer dans les delais",
  "Calculer la TVA sur le TTC~Confondre TVA et taxe de sejour~Omettre la mention sur la facture~Ne pas reverser la taxe collectee",
  "55 €~Prix TTC~50 €~Base HT~5 €~TVA 10 %~20 %~Taux normal~10 %~Taux restauration",
  "TVA~Impot sur la valeur ajoutee~Taxe de sejour~Taxe locale",
  "HT~Avant taxe~TTC~Apres taxe"))

# ============================================================ CO3
add("CO3", "Coûts et calcul du prix de revient d'une prestation", "Économie et gestion hôtelière", ["1re", "Terminale"],
S("Le cout de revient represente l'ensemble des charges necessaires pour realiser une prestation ou un produit."
  "|On distingue les charges directes, affectables sans ambiguite a une prestation, et les charges indirectes, communes a plusieurs prestations."
  "|Les matieres premieres et la main-d'oeuvre directe sont des charges directes."
  "|Les charges indirectes comprennent les frais generaux, l'energie, l'entretien et la supervision."
  "|Le centre de cout est une unité a laquelle on rattache des charges : une cuisine, un etage, un service."
  "|La cle de repartition permet de répartir une charge indirecte entre plusieurs centres, par exemple au prorata de la surface ou des heures."
  "|Le cout unitaire est le cout total divise par le nombre d'unites produites ou de prestations realisees."
  "|Le prix de revient complet inclut une part des charges indirectes, contrairement au cout direct."
  "|Le prix de vente doit etre superieur au prix de revient pour degager une marge."
  "|La marge sur couts variables aide a decider d'une vente supplementaire en periode de faible activite."
  "|Le seuil de rentabilite correspond au volume d'activite ou les produits couvrent exactement les charges."
  "|Une bonne connaissance des couts permet de choisir entre faire realiser une prestation en interne ou la confier a un prestataire externe."),
[QC("Quel element est une charge directe ?", "Le loyer~La matiere premiere de la prestation~L'electricite~Le nettoyage general", 1,
     "La matiere premiere est directement affectee a la prestation."),
 QC("Qu'appelle-t-on un centre de cout ?", "Un client~Une unite a laquelle on rattache des charges~Un fournisseur~Une facture", 1,
     "Le centre de cout peut etre la cuisine, l'etage ou un service."),
 QC("Comment calculer un cout unitaire ?", "Cout total multiplie par le nombre~Cout total divisé par le nombre~Total moins nombre~Nombre moins cout", 1,
     "Le cout unitaire est le cout total divisé par le nombre d'unites."),
 QC("Que comprend le prix de revient complet ?", "Les seules matieres~Les charges directes et indirectes~Le seul salaire~La seule TVA", 1,
     "Le prix de revient complet integre une part des charges indirectes."),
 QT("Une prestation consomme 12 € de matieres, 25 € de main-d'oeuvre directe et se voit appliquer 8 € de frais generaux. Calculer le cout de revient et le prix de vente pour une marge de 15 €.",
     "Le cout direct s'eleve a 12 + 25 = 37 €. En ajoutant les frais generaux de 8 €, on obtient un prix de revient complet de 45 €. Pour dégager une marge de 15 €, le prix de vente hors taxe doit etre de 45 + 15 = 60 €. Le taux de marque est alors de 15 / 60 = 25 % du prix de vente. Ce calcul donne un prix plancher : si le client refuse 60 €, l'entreprise peut eventuellement accepter un prix superieur au cout variable de 37 € en periode creuse, mais elle ne couvrira pas l'ensemble de ses charges.",
     "On attend cout direct 37 €, revient complet 45 €, prix 60 € et marge 15 €."),
 QT("Expliquer pourquoi le choix d'une cle de repartition influe sur le cout affiche d'une prestation.",
     "Les charges indirectes ne peuvent pas etre affectees directement : il faut les repartir selon une cle, par exemple les heures de main-d'oeuvre, la surface occupee ou le nombre de couverts. Le resultat depend du choix de cette cle. Si on repartit l'electricite au prorata des heures, une prestation longue et peu consommatrice d'energie supportera une charge elevee ; avec une cle fondee sur la surface, ce sera l'inverse. La cle doit donc etre pertinente au regard de la cause reelle de la charge et stable dans le temps. Une cle mal choisie fausse le cout de revient, entraine de mauvaises decisions de prix et peut rendre une prestation rentable alors qu'elle ne l'est pas.",
     "On attend lien entre cause de la charge, choix de la cle et consequence sur la decision de prix.")],
C("Le cout de revient agrège charges directes et indirectes : la cle de repartition determine le resultat affiche.",
  "Cout unitaire = cout total / nombre d'unites",
  "Direct = affectable · indirect = repartir · revient complet = direct + indirect",
  "Charge directe~Affectee a une prestation~Charge indirecte~Commune a plusieurs prestations~Centre de cout~Unite de rattachement~Cle de repartition~Regle de partage~Cout unitaire~Cout par unite~Prix de revient~Cout complet",
  "Identifier les charges directes|Choisir les centres de cout|Selectionner une cle pertinenente|Calculer le cout unitaire|Comparer au prix de vente",
  "Oublier les charges indirectes~Choisir une cle arbitraire~Confondre cout et prix~Ne pas mettre a jour les donnees",
  "12 €~Matiere~25 €~Main-d'oeuvre~8 €~Frais generaux~45 €~Prix de revient~60 €~Prix de vente",
  "Charge directe~Sans ambiguite~Charge indirecte~A repartir",
  "Cout de revient~Ce que coute la prestation~Prix de vente~Ce que paie le client"))

# ============================================================ CO4
add("CO4", "Budget prévisionnel et suivi budgétaire", "Économie et gestion hôtelière", ["Terminale"],
S("Le budget previsionnel traduit en chiffres le programme d'action de l'etablissement pour une periode future, generalement un an."
  "|Il comporte un budget d'exploitation, un budget d'investissement et un budget de tresorerie."
  "|Le budget d'exploitation estime les produits, les charges et le resultat attendu."
  "|Les previsions de ventes reposent sur l'historique, le taux d'occupation, le prix moyen et les evenements a venir."
  "|Les charges variables suivent l'activite, tandis que les charges fixes restent relativement constantes."
  "|Le budget d'investissement recense les depenses durables : renovation, equipement de cuisine, systeme informatique."
  "|Le budget de tresorerie anticipe les encaissements et les decaissements mois par mois pour detecter les besoins de financement."
  "|L'elaboration du budget suit une demarche participative : les responsables de services proposent leurs besoins et la direction arbitre."
  "|Le suivi budgetaire compare regulierement les réalisations aux previsionnel, souvent chaque mois."
  "|Un ecart favorable ou defavorable est calcule pour chaque poste et Analyse pour identifier sa cause."
  "|Le budget n'est pas un objectif rigide : il peut etre revoir en cours d'exercice si l'environnement change."
  "|La rigueur budgetaire permet d'anticiper les tensions de tresorerie et de prendre des decisions correctives a temps."),
[QC("Que traduit un budget previsionnel ?", "Le bilan de l'an dernier~Le programme d'action chiffre~La seule tresorerie~La carte des prix", 1,
     "Le budget chiffre les objectifs et les moyens pour la periode a venir."),
 QC("Quel budget anticipe encaissements et decaissements mois par mois ?", "Le budget d'exploitation~Le budget d'investissement~Le budget de tresorerie~Le bilan", 2,
     "Le budget de tresorerie prevoit les flux de liquidites."),
 QC("Quelle charge varie avec le nombre de couverts ?", "Le loyer~Le cout des denrees~L'assurance~L'impot foncier", 1,
     "Le cout des denrees est une charge variable, liee a l'activite."),
 QC("A quelle frequence suit-on generalement le budget ?", "Une fois par an~Chaque mois~Tous les dix ans~Jamais", 1,
     "Un suivi mensuel permet de corriger les ecarts rapidement."),
 QT("Un poste de ventes etait budgete a 80 000 € et realise a 74 000 €. Calculer l'ecart et l'analyser.",
     "L'ecart est de 74 000 - 80 000 = -6 000 €, soit un ecart defavorable de 7,5 % par rapport au budget. Pour l'analyser, on décompose l'ecart : il peut venir d'un taux d'occupation plus bas que prevu, d'un prix moyen plus faible, d'une fermeture pour travaux ou d'une saisonnalite mal anticipe. On compare les volumes et les prix, puis on observe les concurrents et la conjoncture. Si l'ecart est durable, on revoit les previsions et on adapte les charges variables ou l'effort commercial. Si l'ecart est ponctuel, on le note et on poursuit le suivi sans modifier la structure du budget.",
     "On attend ecart -6 000 €, pourcentage -7,5 % et decomposition volume/prix."),
 QT("Pourquoi le budget de tresorerie est-il indispensable meme quand le resultat est beneficiaire ?",
     "Le resultat comptable est calcule selon la convention d'encaissement : il peut etre beneficiaire alors que les clients n'ont pas encore paye et que les fournisseurs doivent etre regles immediatement. La tresorerie mesure les flux reels d'argent. Un etablissement peut donc etre rentable mais avoir un besoin de tresorerie temporaire, notamment en raison des stocks, des creances clients ou d'investissements. Le budget de tresorerie anticipe ces decalages mois par mois et permet de negocier un credit de caisse ou d'etaler les investissements avant la crise. Il complete le compte de resultat, qui donne une vue economique mais non immediate des liquidites.",
     "On attend distinction resultat et tresorerie, decalages et interet de l'anticipation.")],
C("Le budget chiffre une strategie ; son suivi mensuel transforme les ecarts en decisions correctives.",
  "Ecart = realise - budget",
  "Exploitation · investissement · tresorerie",
  "Budget~Programme chiffre~Exploitation~Produits et charges prevus~Investissement~Depenses durables~Tresorerie~Encaissements et decaissements~Ecart~Realise moins prevu~Prevision~Estimation de l'activite",
  "Collecter les donnees historiques|Estimer produits et charges|Construire les trois budgets|Comparer chaque mois|Analyser les ecarts et corriger",
  "Confondre resultat et tresorerie~Ne jamais revoir le budget~Ignorer les ecarts favorables~Oublier les investissements",
  "80 000 €~Budget~74 000 €~Realise~-6 000 €~Ecart defavorable~-7,5 %~Amplitude de l'ecart~12 mois~Periode type",
  "Budget fixe~Figure au depart~Budget revoit~Ajuste en cours d'exercice",
  "Charge variable~Suit l'activite~Charge fixe~Stable"))

# ============================================================ CO5
add("CO5", "Seuil de rentabilité et tableau de bord", "Économie et gestion hôtelière", ["Terminale"],
S("Le seuil de rentabilite est le niveau d'activite pour lequel les produits couvrent exactement l'ensemble des charges."
  "|A ce niveau, le resultat est nul : l'entreprise ne gagne ni ne perd d'argent."
  "|La marge sur couts variables est la difference entre le prix de vente unitaire et le cout variable unitaire."
  "|Le seuil en volume se calcule en divisant les charges fixes par la marge sur couts variables par unite."
  "|Le seuil en chiffre d'affaires s'obtient en multipliant le seuil en volume par le prix de vente unitaire, ou en divisant les charges fixes par le taux de marge sur couts variables."
  "|La marge de securite est la difference entre l'activite reelle ou prevue et le seuil de rentabilite."
  "|Une marge de securite faible signale une fragilite : une petite baisse d'activite suffit a entrainer une perte."
  "|Le point mort est la periode necessaire pour atteindre le seuil, souvent exprimee en mois ou en nombre de nuits."
  "|Le tableau de bord regroupe des indicateurs choisis pour suivre la performance de l'etablissement."
  "|Les indicateurs peuvent etre financiers, comme le RevPAR ou le food cost, ou operationnels, comme le taux d'occupation et le delai de check-in."
  "|Un bon indicateur est fiable, simple a calculer, compare dans le temps et relié a une decision possible."
  "|Le seuil de rentabilite et le tableau de bord aident la direction a arbitrer entre prix, volume et maitrise des charges."),
[QC("Que se passe-t-il au seuil de rentabilite ?", "Le benefice est maximal~Le resultat est nul~Les charges sont nulles~Les ventes sont nulles", 1,
     "Produits et charges s'equilibrent exactement au seuil."),
 QC("Comment calculer la marge sur couts variables unitaire ?", "Prix de vente moins cout variable~Prix de vente plus cout variable~Charges fixes divisées par volume~Produits moins charges", 0,
     "Marge unitaire = prix de vente unitaire - cout variable unitaire."),
 QC("Comment obtenir le seuil en volume ?", "Charges fixes / marge unitaire~Charges fixes × marge unitaire~Ventes / charges~Marge / charges", 0,
     "Le seuil en volume est le quotient des charges fixes par la marge sur couts variables par unite."),
 QC("Que mesure la marge de securite ?", "Le benefice maximum~L'ecart entre activite reelle et seuil~Le montant des charges fixes~Le cout variable", 1,
     "Elle indique de combien l'activite peut baisser avant la perte."),
 QT("Une chambre se vend 120 € avec un cout variable de 40 €. Les charges fixes annuelles sont de 160 000 €. Calculer le seuil en nuits et en chiffre d'affaires.",
     "La marge sur couts variables par chambre est de 120 - 40 = 80 €. Le seuil en volume vaut 160 000 / 80 = 2 000 nuits vendues. Le chiffre d'affaires au seuil est de 2 000 × 120 = 240 000 €. On peut le verifier avec le taux de marge sur couts variables : 80 / 120 = 0,667, puis 160 000 / 0,667 = environ 240 000 €. Si l'hotel dispose de 80 chambres ouvertes 365 jours, le seuil represente un taux d'occupation d'environ 2 000 / 29 200 = 6,8 % : la structure est ici peu risquee, car les charges fixes sont faibles rapportees a la capacite.",
     "On attend marge 80 €, seuil 2 000 nuits, CA 240 000 € et verif ication."),
 QT("Quels indicateurs choisir dans un tableau de bord d'hotel et pourquoi ?",
     "On choisit des indicateurs lies aux decisions a prendre : taux d'occupation pour la politique commerciale, RevPAR pour l'arbitrage prix-volume, prix moyen pour le positionnement, food cost pour la restauration, taux de satisfaction et delai de traitement des reclamations pour la qualite, et taux de rotation du personnel pour les ressources humaines. Chaque indicateur doit avoir une definition ecrite, une periodicite, un responsable et une cible. Il faut eviter l'accumulation : trop d'indicateurs rendent le tableau illisible et diluent l'attention. Enfin, les valeurs doivent etre comparees au budget, a la periode precedente et aux objectifs, pour declencher une action si un ecart significatif apparait.",
     "On attend choix lie aux decisions, definitions claires, periodicite et comparaison.")],
C("Le seuil de rentabilite fixe le point d'equilibre ; le tableau de bord signale les ecarts avant la perte.",
  "Seuil (volume) = charges fixes / marge sur couts variables",
  "Marge de securite = activite - seuil",
  "Seuil de rentabilite~Resultat nul~Marge sur couts variables~Prix moins cout variable~Charges fixes~Independantes du volume~Marge de securite~Marge avant perte~Tableau de bord~Indicateurs de suivi~RevPAR~Indicateur hotelier",
  "Calculer la marge unitaire|Identifier les charges fixes|Calculer le seuil en volume|Comparer a l'activite reelle|Suivre les indicateurs dans le temps",
  "Confondre marge et benefice~Oublier les charges fixes~Multiplier les indicateurs~Ne pas fixer de cible",
  "120 €~Prix de vente~40 €~Cout variable~80 €~Marge unitaire~2 000 nuits~Seuil~240 000 €~CA au seuil",
  "Resultat nul~Seuil~Resultat positif~Au-dessus du seuil",
  "Marge de securite~Protection~Seuil~Point critique"))

# ============================================================ DR1
add("DR1", "Licence IV et réglementation des débits de boissons", "Droit et réglementation", ["Terminale"],
S("La licence est l'autorisation administrative necessaire pour exploiter un debit de boissons a consommer sur place."
  "|La licence de quatrieme categorie, dite licence IV, autorise la vente de toutes les boissons alcoolisees, y compris les spiritueux."
  "|Les licences de premiere, deuxieme et troisieme categorie autorisent des boissons de moins en plus alcoolisees."
  "|La licence IV ne peut plus etre creee librement : le nombre de licences est limite par un contingent par habitant."
  "|Une licence peut etre transferee, avec l'accord de l'autorite administrative, lors de la vente d'un etablissement."
  "|La demande de transfert est adressee a la mairie, qui dispose d'un delai legal pour statuer apres avis de la prefecture et des services de police."
  "|Le titulaire doit respecter les horaires d'ouverture et les jours de fermeture fixes par le departement."
  "|La vente d'alcool aux mineurs de moins de 18 ans est interdite et constituent un delit."
  "|Le refus de servir une personne manifestement ivre est une obligation legale du professionnel."
  "|L'affichage des prix des boissons et de l'interdiction de vente aux mineurs est obligatoire dans l'etablissement."
  "|La publicite pour les boissons alcoolisees est strictement encadree par la loi Evin."
  "|Le non-respect de ces regles peut entrainer des sanctions administratives, des amendes et la fermeture de l'etablissement."),
[QC("Que autorise la licence IV ?", "Les seules boissons sans alcool~Toutes les boissons alcoolisees~Le seul vin~La vente a emporter uniquement", 1,
     "La licence de quatrieme categorite autorise toutes les boissons alcoolisees."),
 QC("Peut-on creer librement une licence IV aujourd'hui ?", "Oui~Non, son nombre est contingent~Oui, apres un an d'activite~Seulement en zone rurale", 1,
     "Le nombre de debitants est limite par un contingent demographique."),
 QC("Qui reçoit la demande de transfert de licence ?", "Le tribunal~La mairie~Le prefet seul~La chambre de commerce", 1,
     "La demande est deposee en mairie, qui instruit le dossier avec les services concernes."),
 QC("Quel age minimal pour acheter une boisson alcoolisee ?", "16 ans~18 ans~21 ans~Aucun age", 1,
     "La vente d'alcool aux mineurs de moins de 18 ans est interdite."),
 QC("Quelle loi encadre la publicite pour l'alcool ?", "La loi Evin~La loi Toubon~La loi RGPD~La loi ALLURES", 0,
     "La loi du 10 janvier 1991, dite loi Evin, encadre la publicite alcoolique."),
 QT("Expliquer la difference entre creation et transfert d'une licence IV.",
     "Une creation de licence augmenterait le nombre de debits de boissons : elle est aujourd'hui presque impossible, car le nombre de licences est contingent par rapport a la population. Un transfert, au contraire, deplace une licence existante d'un etablissement vers un autre, generalement lors d'une vente ou d'un changement d'exploitant. Le nombre total de licences reste identique. Le transfert necessite une demande en mairie, un avis de la prefecture et des services de police, un delai d'instruction et une decision motiv ee. Le dossier doit justifier de la cessation de l'activite precedente et de la capacite du nouveau titulaire a exploiter le debit dans le respect des regles.",
     "On attend contingentement, neutralite du transfert sur le nombre et procedure administrative."),
 QT("Quelles obligations le titulaire d'une licence IV doit-il respecter au quotidien ?",
     "Il doit respecter les horaires d'ouverture et les fermetures hebdomadaires autorisees, afficher les prix et l'interdiction de vente aux mineurs, refuser de servir une personne ivre et verifier l'age en cas de doute. Il doit tenir l'etablissement en etat, garantir la securite et l'hygiene, et respecter la reglementation publicitaire de la loi Evin. Les mentions obligatoires doivent etre visibles et la licence doit etre exploitee personnellement ou par un gerant declare. Enfin, il doit signaler tout changement de situation et cooperer avec les services de police et de la mairie lors des controles.",
     "On attend horaires, affichage, mineurs, ivresse, publicite et cooperation avec les autorites.")],
C("La licence est une autorisation administrative contingentee : son transfert remplace la creation, et son exercice est strictement encadre.",
  "Licence IV = toutes boissons alcoolisees",
  "Transfert en mairie · 18 ans · loi Evin",
  "Licence IV~Quatrieme categorie~Contingent~Limite par habitant~Transfert~Deplacement de licence~Mineur~Interdiction de vente~Ivresse~Refus de service~Loi Evin~Encadrement publicitaire",
  "Verifier l'existence et la categorie de la licence|Demander le transfert en mairie|Respecter horaires et affichages|Controler l'age et refuser l'ivresse|Cooperer en cas de controle",
  "Ouvrir sans licence~Vendre a un mineur~Ignorer une personne ivre~Oublier les affichages obligatoires",
  "4~Quatrieme categorie~18 ans~Age minimal~Loi Evin~1991~Transfert~Sans creation nouvelle",
  "Creation~Augmente le nombre~Transfert~Deplace une licence existante",
  "Licence~Autorisation~Contingent~Quota demographique"))

# ============================================================ DR2
add("DR2", "Contrat de travail et conventions collectives", "Droit et réglementation", ["1re", "Terminale"],
S("Le contrat de travail est une convention par laquelle un salarie s'engage a travailler sous la direction d'un employeur, moyennant un salaire."
  "|Il existe deux grandes formes : le contrat a duree indeterminee, ou CDI, et le contrat a duree determinee, ou CDD."
  "|Le CDD ne peut etre conclu que dans des cas limites precis : remplacement, augmentation temporaire d'activite ou saisonnier."
  "|Le contrat ecrit doit mentionner l'identite des parties, la date de debut, la duree, le poste, le salaire, la duree du travail et le lieu."
  "|La periode d'essai permet a l'employeur d'evaluer le salarie et a celui-ci de tester le poste, dans des limites legales."
  "|La convention collective de la restauration rapide ou de l'hotellerie-restauration complete le code du travail."
  "|Elle fixe notamment les classifications, les salaires minima, la duree du travail et les indemnites de licenciement."
  "|Le salaire net est le salaire brut diminue des cotisations sociales salariales."
  "|Le cout total de la main-d'oeuvre comprend le salaire brut et les cotisations employeur."
  "|Le temps de travail est encadre par la duree legale, les repos quotidiens et hebdomadaires, et les heures supplementaires."
  "|Le licenciement doit respecter une procedure : entretien prealable, notification ecrite et respect d'un preavis."
  "|En restauration, le travail saisonnier, le temps partiel et les horaires decomposes sont frequents et doivent etre encadres par le contrat."),
[QC("Quand peut-on conclure un CDD ?", "Toujours~Dans des cas limites precis~Jamais~Uniquement pour la direction", 1,
     "Le CDD est reserve aux situations prevues par la loi, comme le remplacement ou la saison."),
 QC("Quelle mention doit figurer dans un contrat ecrit ?", "La couleur de la tenue~Le salaire et la duree du travail~Le nom du fournisseur~Le menu du jour", 1,
     "Le salaire, la duree et le poste sont des mentions obligatoires."),
 QC("Quel texte complete le code du travail pour une branche professionnelle ?", "Le reglement interieur~La convention collective~Le plan comptable~Le contrat de vente", 1,
     "La convention collective adapte les regles a la branche d'activite."),
 QC("Comment obtenir le salaire net ?", "Brut plus cotisations~Brut moins cotisations salariales~Brut multiplie par deux~Net = brut", 1,
     "Les cotisations salariales sont deduites du salaire brut."),
 QT("Un salarie est paye 1 800 € brut avec 20 % de cotisations salariales et 42 % de cotisations employeur. Calculer net et cout employeur.",
     "Les cotisations salariales valent 1 800 × 0,20 = 360 €, donc le salaire net est de 1 800 - 360 = 1 440 €. Les cotisations employeur valent 1 800 × 0,42 = 756 €. Le cout total pour l'employeur est de 1 800 + 756 = 2 556 €. L'ecart entre le cout employeur et le net percu par le salarie est important : il traduit le poids des prélèvements sociaux. Ce calcul est essentiel pour etablir un budget de personnel et pour comprendre qu'une augmentation brute a un impact plus que proportionnel sur le cout de l'entreprise.",
     "On attend net 1 440 €, cotisations employeur 756 € et cout 2 556 €."),
 QT("Expliquer les etapes d'un licenciement et les risques d'une procedure incomplete.",
     "Le licenciement commence par un entretien prealable auquel le salarie est convoque par ecrit ; il peut se faire accompagner. L'employeur doit ensuite notifier la decision par lettre recommandee en precisant le motif, qui doit etre reel et serieux. Le preavis doit etre respecte ou indemnifie, et les documents de fin de contrat sont remis : solde de tout compte, certificat de travail et attestation France Travail. Enfin, les indemnites legales et conventionnelles sont verseEs. Une procedure incomplete, un motif insuffisant ou une absence d'entretien exposent l'employeur a des prud'hommes et a des dommages interets. La rigueur administrative protege les deux parties.",
     "On attend entretien, notification motivee, preavis, documents et risques prud'homaux.")],
C("Le contrat de travail encadre la relation salariale ; la convention collective et le code du travail la completent.",
  "Net = brut - cotisations salariales",
  "Cout employeur = brut + cotisations employeur",
  "CDI~Duree indeterminee~CDD~Duree determinee et cas limites~Convention collective~Regles de la branche~Salaire brut~Avant prelevements~Cotisations~Part salariale et employeur~Licenciement~Procedure encadree",
  "Choisir la forme de contrat|Verifier les mentions obligatoires|Appliquer la convention collective|Calculer net et cout employeur|Respecter la procedure en cas de rupture",
  "Recourir a un CDD sans motif~Oublier l'entretien prealable~Confondre brut et net~Ignorer les repos hebdomadaires",
  "1 800 €~Salaire brut~20 %~Cotisations salariales~42 %~Cotisations employeur~1 440 €~Net~2 556 €~Cout employeur",
  "CDI~Stable~CDD~Temporaire et encadre",
  "Brut~Avant deductions~Net~Apres deductions"))

# ============================================================ DR3
add("DR3", "Responsabilité de l'hôtelier et dépôt des bagages", "Droit et réglementation", ["Terminale"],
S("L'hôtelier est un professionnel qui exerce une activite commerciale d'hebergement et qui doit une obligation de securite a ses clients."
  "|Cette obligation porte sur les locaux, les equipements, le personnel et les incidents previsibles."
  "|L'article 1915 du Code civil prevoit un regime particulier pour les objets apportes par le voyageur dans un hotel."
  "|L'hôtelier est responsable des objets déposes entre ses mains, mais il peut apporter la preuve qu'il n'a pas commis de faute."
  "|Pour les bagages simplement arrives dans la chambre, la responsabilite est plus limitee : l'hôtelier n'est pas leur gardien automatique."
  "|Il est donc conseille de proposer un service de bagagerie avec un registre des depots et des retraits."
  "|Le registre mentionne l'identite du client, la description des bagages, l'heure et la signature."
  "|Les objets de valeur doivent faire l'objet d'une declaration speciale et d'une mention ecrite au contrat de sejour."
  "|En cas de vol ou de degat, le client doit signaler les faits des que possible et une main courante peut etre etablie."
  "|L'hôtelier doit disposer d'une assurance responsabilite civile professionnelle pour faire face aux sinistres."
  "|Les clauses limitatives de responsabilite doivent etre porteEs a la connaissance du client de maniere visible."
  "|Une bonne gestion des depots et une documentation precise protegent le client et l'etablissement en cas de litige."),
[QC("Quelle obligation l'hôtelier a-t-il envers ses clients ?", "Une obligation de resultat absolue~Une obligation de securite~Aucune obligation~Une obligation de publicite", 1,
     "L'hôtelier doit assurer la securite des personnes et des locaux."),
 QC("Que prevoit l'article 1915 du Code civil ?", "Le prix des chambres~Un regime de responsabilite pour les objets du voyageur~La duree du sejour~La taxe de sejour", 1,
     "Cet article organise la responsabilite de l'hôtelier pour les effets apportes par le voyageur."),
 QC("Comment limiter les litiges sur les bagages ?", "Refuser tout depot~Tenir un registre des depots et retraits~Les laisser dans le hall~Ne rien ecrire", 1,
     "Le registre constitue une preuve du depot et de son etat."),
 QC("Que faut-il faire avec les objets de valeur ?", "Les ignorer~Les declarer et les mentionner par ecrit~Les laisser a la reception sans trace~Les refuser systematiquement", 1,
     "Une declaration speciale est necessaire pour engager clairement la responsabilite."),
 QT("Un client affirme qu'un objet a disparu de sa chambre. Quelle demarche adopter ?",
     "On ecoute le client, on l'invite a preciser l'objet, le moment et les circonstances, et on verifie s'il a ete declare a l'arrivee. On controle le registre des depots, les acces a la chambre et les temoignages du personnel, puis on etablit si besoin une main courante avec le client. On informe l'assurance et la direction, sans reconnaitre abusivement une responsabilite. Si un vol est confirme, on porte plainte et on indemnise selon les conditions prevues. En parallele, on analyse les mesures de securite : serrure, cles, acces des personnels et video protection, afin d'eviter la repetition.",
     "On attend ecoute, verification des traces, main courante, assurance et analyse des mesures de securite."),
 QT("Pourquoi une assurance responsabilite civile professionnelle est-elle indispensable ?",
     "L'activite hoteliere expose a de nombreux risques : blessure d'un client sur un sol glissant, incendie, degat des eaux, vol ou erreur de service. La responsabilite civile professionnelle prend en charge les dommages causes a autrui dans le cadre de l'activite, dans la limite des garanties souscrites. Elle evite que le reglement d'un sinistre mette en peril la tresorerie de l'entreprise. Elle ne dispense pas de la prevention : l'assurance intervient apres le dommage, alors que la maintenance, la formation et les procedures reduisent la probabilite de survenance. Il faut donc verifier regulierement les plafonds et les exclusions du contrat.",
     "On attend role de l'assurance, exemples de sinistres et rappel de la prevention.")],
C("Responsabilite et depots reposent sur la prevention et la preuve ecrite : le registre protege le client comme l'etablissement.",
  "Article 1915 du Code civil",
  "Securite · registre des depots · assurance RC Pro",
  "Responsabilite~Obligation envers le client~Depot~Remise d'un objet~Registre~Preuve ecrite~Objet de valeur~Declaration speciale~Main courante~Constat des faits~Assurance RC Pro~Garantie des dommages",
  "Informer le client des regles|Enregistrer les depots et retraits|Declarer les objets de valeur|Signaler et documenter tout incident|Verifier les garanties d'assurance",
  "Ne rien tracer lors d'un depot~Promettre une indemnisation avant analyse~Oublier la declaration d'objets de valeur~Negliger l'entretien des locaux",
  "Article 1915~Texte de reference~Main courante~Constat~RC Pro~Assurance professionnelle~Registre~Preuve",
  "Bagage en chambre~Responsabilite limitee~Bagage depose~Responsabilite renforcee",
  "Prevention~Avant le dommage~Assurance~Apres le dommage"))

# ============================================================ DR4
add("DR4", "Réglementation sanitaire, sociale et affichage", "Droit et réglementation", ["1re"],
S("Un etablissement recevant du public, ou ERP, doit respecter des regles de securite et d'accessibilite."
  "|La categorie de l'ERP depend de la nature de l'activite et de la capacite d'accueil : restaurant, hotel ou salle de spectacle."
  "|Le registre de securite mentionne les travaux, les equipements, les exercices d'evacuation et les incidents."
  "|Le plan d'evacuation doit etre affiche et indiquer les issues, les moyens de secours et le point de rassemblement."
  "|Les issues de secours doivent rester accessibles, signalees et non verrouillees pendant l'exploitation."
  "|L'accessibilite aux personnes en situation de handicap est obligatoire dans les ERP, avec des cheminements et des sanitaires adaptes."
  "|La loi handicap du 11 fevrier 2005 fixe les principes de l'accessibilite et de l'egalite des droits."
  "|Les regles d'hygiene alimentaire imposent un plan de nettoyage et une formation du personnel aux bonnes pratiques."
  "|Les prix doivent etre affiches de maniere lisible et visible pour le client, y compris les taxes et les supplements."
  "|L'interdiction de fumer dans les lieux publics couvre les restaurants et les hotels, avec des sanctions en cas de non-respect."
  "|L'affichage des horaires, des informations sur les allergenes et des coordonnees de la direction est attendu dans un etablissement de service."
  "|Le respect de ces obligations est verifie lors des controles de la mairie, de la prefecture, de la DREETS ou de la DGCCRF."),
[QC("Que signifie le sigle ERP ?", "Etablissement de restauration prive~Etablissement recevant du public~Equipement de regulation professionnelle~Entreprise de restauration publique", 1,
     "Les hotels et restaurants sont des etablissements recevant du public."),
 QC("Que doit contenir le registre de securite ?", "La carte des vins~Les travaux, exercices et incidents~Le planning du personnel~Les factures", 1,
     "Le registre de securite consigne les elements relatifs a la securite de l'ERP."),
 QC("Quelle loi a fonde l'obligation d'accessibilite ?", "La loi Evin~La loi du 11 fevrier 2005~La loi Toubon~La loi de 1881", 1,
     "La loi handicap du 11 fevrier 2005 pose le principe d'accessibilite."),
 QC("Les issues de secours doivent-elles etre verrouillees ?", "Oui toujours~Non, elles doivent rester accessibles~Oui la nuit seulement~Peu importe", 1,
     "Une issue condamnee est une infraction grave en cas d'evacuation."),
 QT("Detailler les obligations d'affichage dans un restaurant.",
     "Le client doit pouvoir voir les prix des plats et des boissons, avec les taxes incluses et les eventuels supplements. Le menu doit signaler la presence d'allergenes majeurs ou renvoyer a un document ecrit disponible. L'interdiction de fumer est annoncee par des affiches regullementaires. Le plan d'evacuation et les consignes de securite sont exposes, ainsi que les coordonnees utiles. Si l'etablissement propose une restauration collective ou des formules particulieres, les conditions doivent etre ecrites. Ces affichages ont une double fonction : informer le client et prouver en cas de controle que l'etablissement respecte la reglementation.",
     "On attend prix, allergenes, interdiction de fumer, securite et valeur de preuve."),
 QT("Comment se prepare un controle des autorites dans un etablissement ?",
     "On constitue un dossier administratif complet : autorisations, licence, registre de securite, plan d'evacuation, attestations de formation et contrats d'assurance. On verifie que les plans sont a jour, que les issues sont degagees et que le materiel de secours est accessible. En cuisine, le plan HACCP, les fiches techniques, les registres de temperature et les bons de livraison doivent etre disponibles. En salle, les affichages prix, allergenes et interdiction de fumer sont controles. Enfin, on designe une personne capable de presenter les documents et de repondre aux questions. Une preparation permanente est preferable a une course contre la montre la veille du controle.",
     "On attend dossier complet, verifications terrain, documents HACCP et referent designe.")],
C("La reglementation d'un ERP combine securite, accessibilite, hygiene et transparence envers le client.",
  "ERP = etablissement recevant du public",
  "Registre de securite · accessibilite · affichages",
  "ERP~Etablissement recevant du public~Registre de securite~Suivi des controles~Evacuation~Plan et exercices~Accessibilite~Acces des personnes handicapees~Affichage~Information du client~Controle~Visite des autorites",
  "Determiner la categorie de l'ERP|Tenir le registre de securite|Organiser exercices et entretien|Verifier les affichages|Compiler les documents de controle",
  "Bloquer une issue~Oublier le registre de securite~Ne pas afficher les prix~Ignorer les obligations d'accessibilite",
  "2005~Loi handicap~DREETS~Service de controle~DGCCRF~Controle des prix~Registre~Preuve ecrite~ERP~Etablissement classe",
  "Securite~Proteger les personnes~Accessibilite~Permettre l'acces",
  "Affichage~Informer~Registre~Consigner"))

# ============================================================ DR5
add("DR5", "Données personnelles et moyens de paiement", "Droit et réglementation", ["Terminale"],
S("L'etablissement collecte des donnees personnelles des clients : identite, coordonnees, historique de sejour et preferences."
  "|Ces donnees sont protegees par le reglement general sur la protection des donnees, ou RGPD, applicable depuis 2018."
  "|Toute collecte doit avoir une finalite determinee et explicite, comme la gestion de la reservation ou la fidelisation."
  "|Le principe de minimisation impose de ne collecter que les donnees necessaires a cette finalite."
  "|Le client doit etre informe de maniere claire : finalites, destinataires, duree de conservation et ses droits."
  "|Les droits du client comprennent l'acces, la rectification, l'effacement, la limitation et l'opposition."
  "|Une demande d'acces doit etre traitee dans un delai d'un mois, avec verification de l'identite du demandeur."
  "|Les donnees doivent etre conservees dans des systemes securises, avec des droits d'acces limites aux personnels habilites."
  "|Les plateformes de reservation sont des sous-traitants ou des responsables conjoints : des contrats ecrits doivent cadrer les echanges."
  "|En cas de violation de donnees, la CNIL doit etre notifiee dans les 72 heures si le risque est eleve."
  "|Les paiements par carte bancaire doivent etre traites par des prestataires certifies et respecter la norme PCI DSS."
  "|Le numero complet de carte ne doit jamais etre note sur un papier ou saisi dans un simple fichier texte."),
[QC("Depuis quelle annee le RGPD est-il applicable ?", "2005~2016~2018~2022", 2,
     "Le reglement est applicable depuis le 25 mai 2018."),
 QC("Quel principe limite la collecte aux seules donnees utiles ?", "La minimisation~La conservation illimitee~La transparence inverse~Le partage systematique", 0,
     "La minimisation impose de ne collecter que le necessaire."),
 QC("Quel est le delai de reponse a une demande d'acces ?", "24 heures~Un mois~Six mois~Un an", 1,
     "Le RGPD fixe un delai d'un mois, eventuellement prolonge de deux mois."),
 QC("Qui doit etre notifie en cas de violation de donnees a risque eleve ?", "La CNIL~Le fournisseur de pain~La mairie~Le client seulement", 0,
     "La notification a l'autorite de controle est obligatoire dans les 72 heures."),
 QT("Un client demande l'effacement de ses donnees. Comment traiter la demande ?",
     "On verifie d'abord l'identite du demandeur, puis on identifie toutes les donnees le concernant : PMS, programme de fidelite, messagerie, facturation et plateformes. On applique le droit a l'effacement, sauf si une obligation legale impose la conservation de certaines factures ou donnees de police. On informe les sous-traitants pour qu'ils effacent egalement les donnees, et on confirme par ecrit au client dans le delai d'un mois. On consigne la demande dans un register pour prouver le traitement. Enfin, on vérifie que les sauvegardes sont prises en compte selon la procedure de l'etablissement.",
     "On attend verification d'identite, inventaire des donnees, exceptions legales, sous-traitants et delai."),
 QT("Pourquoi ne faut-il jamais conserver un numero de carte bancaire sur un papier ?",
     "Le numero de carte, avec la date d'expiration et le cryptogramme, constitue une donnee sensible : son vol permet effectuer des paiements frauduleux. Le conserver sur un papier ou dans un fichier non chiffre cree une fuite potentielle et engage la responsabilite de l'etablissement au titre du RGPD et de la norme PCI DSS. Les paiements doivent etre traites par un prestataire certifie qui tokenise la carte : l'etablissement recoit un jeton de paiement et non les donnees bancaires completes. Si une garantie est necessaire, on utilise une preautorisation via le terminal ou la plateforme. En cas de doute, on detruit immediatement le support papier et on forme l'equipe.",
     "On attend risque de fraude, non-conformite RGPD/PCI DSS et solution de tokenisation.")],
C("Donnees et paiements exigent une organisation stricte : finalite, minimisation, securite et droits du client.",
  " RGPD : acces, rectification, effacement, opposition",
  "Notification CNIL : 72 heures · reponse : 1 mois",
  "RGPD~Reglement europeen~Minimisation~Collecte limitee~Droit d'acces~Copie des donnees~CNIL~Autorite de controle~Tokenisation~Remplacement de la carte par un jeton~PCI DSS~Norme de securite bancaire",
  "Inventarier les donnees collectees|Definir les finalites et les durees|Informer le client|Securiser les systemes et les acces|Traiter les demandes dans les delais",
  "Noter un numero de carte sur papier~Collecter des donnees inutiles~Ignorer une demande d'effacement~Ne pas notifier une fuite",
  "2018~Annee d'application~72 heures~Notification CNIL~1 mois~Reponse~PCI DSS~Securite des paiements",
  "Donnee personnelle~Identifie ou identifier~Donnee sensible~Carte bancaire",
  "Collecte~Au depart~Conservation~Dans le temps"))

# ============================================================ MK1
add("MK1", "Segmentation, ciblage et positionnement", "Marketing et communication", ["Terminale"],
S("Le marketing vise a identifier les besoins des clients et a y repondre de maniere plus rentable que la concurrence."
  "|Les besoins du client hotelier varient selon le motif du voyage : affaires, loisirs, evenement ou passage."
  "|La segmentation decompose le marche en groupes homogènes de clients aux besoins proches."
  "|Les criteres de segmentation geographiques, demographiques, psychographiques et comportementaux sont les plus utilises."
  "|Le ciblage consiste a choisir un ou plusieurs segments sur lesquels l'etablissement va concentrer ses efforts."
  "|Le positionnement designe la place que l'etablissement souhaite occuper dans l'esprit du client cible."
  "|Un positionnement clair repond a trois questions : pour qui, pour quel besoin, avec quelle valeur ajoutee."
  "|La differenciation peut porter sur l'emplacement, la qualite du service, le concept, le prix ou l'experience proposee."
  "|Une carte de positionnement compare les etablissements selon deux axes, par exemple prix et niveau de service."
  "|Le positionnement doit etre coherent avec les prestations reelles : une promesse non tenue detruit la confiance."
  "|Les donnees clients, les avis en ligne et les etudes de marche nourrissent la reflexion marketing."
  "|La strategie marketing est revue regulierement car les attentes et la concurrence evoluent."),
[QC("Que designe la segmentation ?", "Le choix d'un prix unique~La division du marche en groupes homogènes~La publicite~La facturation", 1,
     "La segmentation regroupe les clients aux besoins similaires."),
 QC("Quel critere de segmentation concerne l'age ou la profession ?", "Geographique~Demographique~Psychographique~Comportemental", 1,
     "L'age, le revenu et la profession sont des criteres demographiques."),
 QC("Que repond un positionnement clair ?", "Pour qui, pour quel besoin, avec quelle valeur ajoutee~Quel est le prix le plus bas~Quel est le fournisseur~Quel est le menu", 0,
     "Ces trois questions structured le positionnement."),
 QC("Quel axe peut servir a une carte de positionnement ?", "Prix et niveau de service~Couleur et musique~Nombre de chambres et age du directeur~Jour et heure", 0,
     "La carte compare les concurrents sur deux axes pertinents pour le client."),
 QT("Un hotel situe en gare souhaite attirer une clientele d'affaires. Proposer un positionnement et justifier.",
     "Le ciblage retient les voyageurs d'affaires : deplacement frequent, besoin de rapidite, horaires variables et attente de fiabilite. Le positionnement peut etre : « l'hotel de la gare pour les professionnels qui veulent gagner du temps », avec une valeur ajoutee fondee sur l'emplacement, l'enregistrement rapide, le petit-dejeuner tot, le wifi fiable et une facture simplifiee. Ce positionnement est coherent avec les prestations reelles et se distingue d'un hotel de loisirs mise sur le calme et les equipements familiaux. Il doit se traduire dans la communication, la carte des services et les partenariats avec les entreprises.",
     "On attend ciblage, valeur ajoutee, coherence avec les prestations et traduction operationnelle."),
 QT("Pourquoi un positionnement trop large est-il risque ?",
     "Un positionnement qui s'adresse a tout le monde ne dit rien de precis : le client ne retient pas ce qui rend l'etablissement different. Les messages generiques « confort et qualite » sont partages par tous les concurrents et ne creent pas de preference. Un positionnement large entraine aussi des incoherences : vouloir plaire aux familles et aux voyageurs d'affaires peut conduire a des horaires, un mobilier et une carte incompatibles. Il est plus efficace de choisir un segment prioritaire, de construire une promesse claire et de la tenir, puis de developper des offres complementaires pour les autres segments sans diluer le message principal.",
     "On attend absence de differentiation, incoherence des prestations et interet d'un ciblage prioritaire.")],
C("Le marketing part du besoin client : segmenter, choisir une cible puis construire une promesse coherente.",
  "Segmentation → ciblage → positionnement",
  "Positionnement = pour qui + quel besoin + quelle valeur ajoutee",
  "Segmentation~Groupes homogènes~Ciblage~Choix d'un segment~Positionnement~Place dans l'esprit client~Differentiation~Valeur ajoutee~Carte~Comparaison sur deux axes~Avis client~Donnee marketing",
  "Etudier les besoins et les donnees|Choisir des criteres de segmentation|Selectionner un segment cible|Definir la promesse et les preuves|Verifier la coherence des prestations",
  "Vouloir plaire a tout le monde~Promettre ce que l'etablissement ne fournit pas~Ignorer les avis clients~Ne jamais revoir le positionnement",
  "Gare~Emplacement strategique~Affaires~Segment vise~Wifi fiable~Preuve de la promesse~Carte~Outil de comparaison",
  "Segmentation~Decouper le marche~Ciblage~Choisir~Positionnement~Se distinguer",
  "Besoin~Attente du client~Offre~Reponse de l'entreprise"))

# ============================================================ MK2
add("MK2", "Mix marketing et distribution hôtelière", "Marketing et communication", ["1re", "Terminale"],
S("Le mix marketing designe l'ensemble des leviers dont dispose l'entreprise pour agir sur le marche."
  "|Le modèle classique des 4 P comprend le produit, le prix, la place et la promotion."
  "|Le produit hotelier est un service composite : chambre, equipements, service, ambiance et experience."
  "|Le prix doit etre cohérent avec le positionnement, la qualite perçue et la capacite a payer du segment vise."
  "|La place, ou distribution, designe les canaux par lesquels le client trouve et reserve l'etablissement."
  "|Les canaux directs comprennent le site officiel, le telephone et la reception ; les canaux indirects comprennent les OTA et les agences."
  "|La promotion regroupe la publicite, les relations presse, les actions commerciales, les réseaux sociaux et les offres speciales."
  "|Les OTA, ou agences de voyages en ligne, apportent du volume mais prelevent une commission souvent comprise entre 15 et 25 %."
  "|La parite tarifaire impose des prix coherents entre tous les canaux pour ne pas desavantager la reservation directe."
  "|Le cout d'acquisition client designe le cout necessaire pour obtenir une reservation, commission comprise."
  "|Un mix efficace aligne les quatre leviers : une chambre haut de gamme ne peut etre vendue a prix bas sans deteriorer la marque."
  "|La performance du mix se mesure avec le taux d'occupation, le prix moyen, le RevPAR et la part des reservations directes."),
[QC("Que designent les 4 P du mix marketing ?", "Produit, prix, place, promotion~Prix, personnel, publicite, profit~Produit, production, publicite, public~Place, plan, personnel, performance", 0,
     "Les 4 P sont Product, Price, Place, Promotion."),
 QC("Quel canal est un canal indirect ?", "Le site officiel~Une OTA~Le telephone de l'hotel~La reception", 1,
     "Les agences de voyages en ligne sont des canaux indirects."),
 QC("Quelle est une consequence des OTA ?", "Une commission sur chaque reservation~La suppression du prix~Une hausse du cout de production~L'interdiction de la publicite", 0,
     "Les OTA apportent du volume mais prelevent une commission."),
 QC("Que mesure le cout d'acquisition client ?", "Le prix de la chambre~Le cout pour obtenir une reservation~Le salaire du personnel~La taxe de sejour", 1,
     "C'est le cout total necessaire a l'obtention d'une vente."),
 QT("Un hotel vend 2 000 nuits via OTA a 15 % de commission et 1 000 nuits en direct. Quel est l'enjeu de la parite tarifaire ?",
     "Si le meme tarif de 130 € est pratique partout, la commission sur 2 000 nuits represente 2 000 × 130 × 0,15 = 39 000 €. Une reservation directe evite cette commission et rapporte donc 130 € au lieu d'environ 110,50 € net. Si l'hotel affiche un prix plus bas en direct, il respecte les accords de parite mais peut perdre des clients qui comparent ; s'il affiche un prix plus eleve en direct, il detourne la clientele de son propre canal le plus rentable et se prive de marge. La parite protege la crédibilite du tarif et la relation avec les plateformes. L'enjeu est donc de developper la reservation directe par la qualite du site, des avantages competents et la fidelisation, plutôt que par des ecarts de prix contraires aux engagements pris.",
     "On attend calcul de commission, comparaison direct/indirect et justification de la parite."),
 QT("Comment decliner les 4 P pour un hotel de charme ?",
     "Le produit met en avant l'originalite des chambres, l'accueil personnalise et le cadre, avec une attention aux details. Le prix se situe au-dessus de la moyenne locale pour signaler le haut de gamme et financer cette qualite. La place privilégie les canaux directs et quelques partenaires selectifs plutot qu'une distribution massive, afin de controler l'image. La promotion s'appuie sur des photographies soignees, des récits de clients, des collaborations avec des influenceurs locaux et des offres liees a des evenements culturels. Les quatre leviers doivent raconter la meme histoire : une experience rare et attentive. Un desequilibre, comme une forte presence sur des sites de prix bas, affaiblirait le positionnement.",
     "On attend declinaison coherente des quatre leviers et lien avec le positionnement.")],
C("Le mix marketing aligne produit, prix, distribution et promotion au service d'un positionnement unique.",
  "4 P : Produit, Prix, Place, Promotion",
  "Direct sans commission · OTA avec commission · parite tarifaire",
  "Mix marketing~Quatre leviers~Produit~Service et experience~Prix~Coherent avec le positionnement~Place~Canaux de distribution~Promotion~Communication et offres~OTA~Agence en ligne",
  "Definir le positionnement|Adapter le produit et le prix|Choisir les canaux de distribution|Construire le plan de promotion|Mesurer occupation et reservations directes",
  "Deconnecter prix et qualite~Multiplier les OTA sans strategie~Pratiquer des prix incoherents~Ignorer le cout d'acquisition",
  "15 a 25 %~Commission OTA typique~130 €~Tarif~39 000 €~Commission annuelle~4 P~Leviers marketing",
  "Canal direct~Sans commission~Canal indirect~Avec commission",
  "Mix~Ensemble cohere~Prix isole~Decision partielle"))

# ============================================================ MK3
add("MK3", "Communication digitale et réseaux sociaux", "Marketing et communication", ["Terminale"],
S("La communication digitale designe l'ensemble des messages diffusés par l'etablissement sur les canaux numeriques."
  "|Elle inclut le site internet, les réseaux sociaux, les newsletters, les messageries et les annonces sur les plateformes."
  "|Chaque canal a un role : le site presente l'offre et convertit, les réseaux creent l'attachement, la messagerie entretient la relation."
  "|Une ligne editoinelle claire definit les themes, le ton, la frequence et les publics vises."
  "|Le contenu doit etre utile ou inspirant : photos de qualite, conseils de voyage, coulisses du service et temoignages."
  "|Le referencement naturel, ou SEO, vise a apparaitre dans les resultats de recherche grace a des pages claires et des mots-cles pertinents."
  "|La publicite en ligne permet de cibler une audience precise mais represente un cout qu'il faut mesurer."
  "|Les indicateurs de la communication digitale comprennent la portee, l'engagement, le trafic du site et le taux de transformation."
  "|Le taux de transformation rapporte le nombre de reservations au nombre de visiteurs du site."
  "|Une communication responsive s'adapte aux mobiles, car une part croissante des reservations se fait sur telephone."
  "|La protection des donnees et l'autorisation d'utiliser les images de clients sont indispensables."
  "|La regularite et la reponse aux commentaires comptent plus qu'une publication exceptionnelle."),
[QC("Quel est le role principal du site internet d'un hotel ?", "Publier des blagues~Presenter l'offre et convertir les visiteurs~Remplacer le PMS~Stocker les factures", 1,
     "Le site est le support de presention et de reservation directe."),
 QC("Que designe le SEO ?", "La publicite payante~Le referencement naturel~La messagerie instantanee~Le paiement en ligne", 1,
     "Le SEO vise a etre visible dans les resultats non payants des moteurs."),
 QC("Comment calculer le taux de transformation ?", "Reservations / visiteurs~Visiteurs / reservations~Reservations × visiteurs~Prix / visiteurs", 0,
     "C'est le rapport entre reservations obtenues et visiteurs du site."),
 QC("Quel indicateur mesure les réactions aux publications ?", "La portee~L'engagement~Le chiffre d'affaires~La taxe de sejour", 1,
     "L'engagement regroupe mentions j'aime, commentaires et partages."),
 QT("Un site recoit 12 000 visiteurs et genere 360 reservations. Calculer le taux de transformation et proposer une action.",
     "Le taux de transformation vaut 360 / 12 000 = 0,03, soit 3 %. Ce taux signifie que 97 visiteurs sur 100 partent sans reserver : il y a une marge de progression. On peut analyser les etapes du parcours : page d'accueil, fiche chambre, moteur de reservation, paiement. Si le moteur est lent ou peu visible sur mobile, l'amélioration technique peut augmenter le taux. On peut aussi renforcer les preuves de qualite : avis clients, photos, politique d'annulation claire et appels a l'action visibles. Enfin, on teste une modification a la fois et on remesure le taux pour evaluer l'effet reel.",
     "On attend 3 %, analyse du parcours et actions testables."),
 QT("Pourquoi une ligne editoinelle est-elle necessaire sur les réseaux sociaux ?",
     "Sans ligne editoinelle, les publications dependent de l'humeur du moment : les themes se repetent, le ton varie et le public ne reconnait plus l'etablissement. La ligne editoinelle definit les sujets picques, le vocabulaire, le style des images et la frequence. Elle permet a differentes personnes de publier de maniere coherente, ce qui renforce l'identite de la marque. Elle sert aussi a filtrer les opportunites : une tendance qui ne correspond pas au positionnement doit etre ignoree. Enfin, elle facilite l'evaluation : on peut mesurer quels contenus fonctionnent et ajuster la ligne sans perdre la coherence d'ensemble.",
     "On attend definition de la ligne, coherence, filtre des contenus et mesure.")],
C("La communication digitale convertit une attention en reservation : contenu, canaux et indicateurs doivent etre pilotes.",
  "Taux de transformation = reservations / visiteurs",
  "Alerte : portee, engagement, trafic, conversion",
  "Communication digitale~Messages en ligne~Ligne edito~Themes et ton~SEO~Referencement naturel~Engagement~Reactions du public~Conversion~Reservation obtenue~Mobile~Support prioritaire",
  "Definir la ligne editoinelle|Choisir les canaux et les formats|Produire un calendrier de publications|Suivre les indicateurs|Tester et ajuster les actions",
  "Publier sans ligne editoriale~Ignorer le mobile~Ne pas repondre aux commentaires~Mesurer seulement le nombre de likes",
  "12 000~Visiteurs~360~Reservations~3 %~Taux de transformation~SEO~Visibilite naturelle~CTA~Appel a l'action",
  "Portee~Nombre de vues~Engagement~Interactions~Conversion~Reservation",
  "Site~Conversion~Reseaux~Attachement"))

# ============================================================ MK4
add("MK4", "Fidélisation et e-réputation", "Marketing et communication", ["Terminale"],
S("La fidelisation vise a developper la repetition des achats et l'attachement du client a l'etablissement."
  "|Un client fidele coute moins cher a acquerir qu'un nouveau client et il augmente la valeur vie client."
  "|Les leviers de fidelisation comprennent la qualite constante, la personnalisation, les avantages et la reconnaissance."
  "|Un programme de fidelite attribue des points ou des statuts en echange de sejours ou de depenses."
  "|La personnalisation s'appuie sur l'historique : preferences de chambre, anniversaire, motifs de voyage."
  "|L'e-reputation designe l'image de l'etablissement telle qu'elle apparait sur les sites d'avis et les reseaux sociaux."
  "|Les avis influencent la decision de reservation : une note elevee augmente la confiance et le taux de transformation."
  "|Repondre aux avis, positifs et negatifs, montre que l'etablissement ecoute et traite les problemes."
  "|Une reponse aux avis doit etre courtoise, factuelle, personnalisee et eviter les donnees personnelles."
  "|La note moyenne, le volume d'avis et la repartition dans le temps sont les principaux indicateurs de e-reputation."
  "|Solliciter un avis apres le depart augmente le nombre d'avis, mais la demande doit rester simple et non intrusive."
  "|Une e-reputation bien geree constitue un actif immatériel qui contribue a la valeur de l'entreprise."),
[QC("Pourquoi la fidelisation est-elle rentable ?", "Un nouveau client coute moins cher~Un client fidele coute moins cher a acquerir~Les prix sont plus bas~La taxe est reduite", 1,
     "Fideliser evite les couts d'acquisition repetitiones."),
 QC("Que designe la valeur vie client ?", "Le prix d'une nuit~La valeur cumulee des achats d'un client sur la duree de la relation~Le salaire~Le nombre de chambres", 1,
     "C'est la somme des revenus attendus d'un client sur toute la relation."),
 QC("Quel est un levier de personnalisation ?", "L'historique des preferences~Le prix unique~La suppression des avis~Le hasard", 0,
     "Les donnees de sejour permettent d'adapter l'offre et l'accueil."),
 QC("Comment repondre a un avis negatif ?", "Avec agressivite~De maniere courtoise et factuelle~Sans rien écrire~En supprimant l'avis", 1,
     "Une reponse courtoise et concrete montre le serieux de l'etablissement."),
 QT("Comment mettre en place un programme de fidelite simple pour un hotel de 60 chambres ?",
     "On definit d'abord l'objectif : augmenter les sejours repetitiones et la reservation directe. On cree un programme gratuit avec inscription simple, collecte de quelques donnees utiles et compteur de nuits. Les avantages peuvent etre une remise sur le sejour suivant, un surclassement selon disponibilite, un accueil personnalise ou un petit-dejeuner offert apres un certain nombre de nuits. On forme la reception a reconnaitre les membres et a enregistrer les preferences. On informe les clients par email et sur le site, en respectant le RGPD. Enfin, on suit le taux de repetition, le nombre de membres et la part des reservations directes pour mesurer la rentabilite du programme.",
     "On attend objectif, avantages, outil, formation et indicateurs de suivi."),
 QT("Comment piloter son e-reputation au quotidien ?",
     "On surveille regulierement les principales plateformes d'avis et on note la note moyenne, le volume et les themes recurrents. On repond a chaque avis dans un delai court : remerciement pour les avis positifs, excuse et solution concrete pour les negatifs, sans jamais communiquer de donnees personnelles. On extrait des avis les points faibles, comme le bruit ou la lenteur du check-in, et on les transmet aux responsables concernes. On sollicite un avis apres le depart par un message court et unique. On compare enfin sa note avec celle des concurrents et on suit l'effet des actions correctives sur les mois suivants.",
     "On attend surveillance, reponses, analyse des causes et comparaison concurrentielle.")],
C("Fideliser et surveiller sa reputation sont deux faces d'une meme demarche : ecouter, recompenser, corriger et mesurer.",
  "Valeur vie client = cumul des achats sur la relation",
  "Reponse aux avis : courtoise, factuelle, personnalisee",
  "Fidelisation~Relation durable~Valeur vie client~Cumul des achats~Programme~Avantages et points~E-reputation~Image en ligne~Avis~Opinion publiee~Note moyenne~Indicateur de reputation",
  "Connaitre les clients et leurs preferences|Construire des avantages cibles|Former les equipes a la reconnaissance|Surveiller et repondre aux avis|Corriger les defauts recurrents",
  "Ignorer les avis negatifs~Repondre avec agressivite~Collecter des donnees inutiles~Ne jamais mesurer la repetition",
  "60 chambres~Taille de l'etablissement~Points~Avantage fidelite~Note moyenne~Indicateur~RGPD~Cadre legal",
  "Fidelisation~Garder le client~Acquisition~Trouver un nouveau client",
  "Avis positif~Renforce l'image~Avis negatif~Signale un defaut"))

# ============================================================ AH1
add("AH1", "Anglais professionnel : accueil et front office", "Anglais professionnel hôtelier", ["1re", "Terminale"],
S("Professional English in a hotel requires clear, polite and predictable phrases in repeated situations."
  "|The standard welcome begins with « Good morning, welcome to... », followed by the guest's name if known."
  "|At check-in, the receptionist asks for the reservation name, a valid identity document and a credit card for the deposit."
  "|Useful questions include « How may I help you? », « Do you have a reservation? » and « How long will you be staying? »."
  "|The receptionist confirms the room type, the number of nights, the rate and the breakfast time."
  "|If the room is not ready, the staff should apologise and offer an alternative rather than simply saying « no »."
  "|Key vocabulary includes reservation, check-in, check-out, deposit, vacant, available, key card and guest."
  "|Dates should be pronounced and repeated clearly to avoid misunderstanding, for example « the fifteenth of June »."
  "|Numbers such as thirteen and thirty, or fourteen and forty, must be articulated distinctly."
  "|At check-out, the receptionist asks about the stay, checks the bill and thanks the guest by name."
  "|The guest may ask for a late check-out, a taxi, directions or a receipt : the answer should be precise and reassuring."
  "|Written confirmation by email uses a short subject line, a greeting, the details of the booking and a polite closing."
),
[QC("Which phrase is a correct welcome at the front desk ?", "« What do you want? »~« Good morning, welcome to our hotel »~« Wait outside »~« Give me your bag »", 1,
     "A professional welcome uses a greeting and the name of the establishment."),
 QC("What does « deposit » mean in a hotel context ?", "A discount~A guarantee paid or pre-authorised~A room key~A breakfast", 1,
     "A deposit secures the booking or guarantees incidentals."),
 QC("Which question asks about the length of stay ?", "« Where are you from? »~« How long will you be staying? »~« How much is it? »~« What time is it? »", 1,
     "This question asks for the number of nights."),
 QC("What should you do if the room is not ready ?", "Say no and stop~Apologise and propose a solution~Ignore the guest~Ask the guest to wait outside", 1,
     "A service recovery always includes an apology and an alternative."),
 QT("Write a short check-in dialogue between a receptionist and a guest.",
     "Receptionist: « Good afternoon, welcome. Do you have a reservation? » Guest: « Yes, in the name of Mr Smith. » Receptionist: « Thank you. Could I have your passport and a credit card for the deposit, please? » Guest: « Here you are. » Receptionist: « Thank you. I have a double room for three nights, from the tenth to the thirteenth of June. Breakfast is served from seven to ten. Here is your key card, room 412 on the fourth floor. » Guest: « Thank you. » Receptionist: « You are welcome. Enjoy your stay. » The dialogue is polite, confirms the essential details and ends with a clear wish.",
     "On attend formules de politesse, verification de l'identite, details du sejour et remise de la cle."),
 QT("How should a receptionist handle a guest who arrives before check-in time?",
     "The receptionist should first check the room status with the housekeeping department instead of refusing immediately. If a room is clean and available, the guest may be checked in early. If not, the receptionist apologises, explains that the room is being prepared, and offers alternatives: luggage storage, a seat in the lounge, a drink, or an exact time when the room should be ready. The answer must be precise and positive: « I am sorry, the room will be ready at two o'clock; in the meantime, we can keep your luggage. » Repeating the time and thanking the guest for their understanding completes the professional response.",
     "On attend verification, excuses alternatives concretes et formulation polie.")],
C("Front office English is a set of repeatable, polite scripts: welcome, verify, confirm, hand over and thank.",
  "Check-in = welcome + identity + confirmation + key",
  "Apologise and offer an alternative",
  "Welcome~Bonjour et bienvenue~Reservation~Engagement de sejour~Deposit~Garantie~Available~Chambre disponible~Key card~Carte d'acces~Check-out~Depart du client",
  "Greet the guest by name|Ask for the reservation and documents|Confirm dates, rate and services|Hand over the key card|Thank and wish a pleasant stay",
  "Confuse thirteen and thirty~Say no without alternative~Use an over-familiar tone~Forget to repeat the dates",
  "10 June~Dix juin~3 nights~Trois nuits~Room 412~Chambre 412~Deposit~Garantie~Sorry~Formule d'excuse",
  "Check-in~Arrivee~Check-out~Depart",
  "Available~Disponible~Vacant~Libre"))

# ============================================================ AH2
add("AH2", "Anglais professionnel : service en salle et restauration", "Anglais professionnel hôtelier", ["1re", "Terminale"],
S("Restaurant service in English combines technical vocabulary with a sequence of predictable courtesy phrases."
  "|The host greets the guests, asks « How many people? » and checks whether they have a reservation."
  "|Guests may ask for « a table by the window », « a quiet table » or « a table for two at eight »."
  "|The server introduces himself, presents the menu and offers water or a drink before taking the food order."
  "|Useful phrases include « Are you ready to order? », « What would you like? » and « Would you like any dessert? »."
  "|The server should repeat the order to confirm it and mention that dishes contain possible allergens."
  "|Key vocabulary includes starter, main course, dessert, side order, bill, cutlery, napkin and still or sparkling water."
  "|Cooking preferences are expressed as « rare, medium rare, medium, well done » for meat."
  "|If a dish is unavailable, the professional answer is to apologise and propose an alternative."
  "|When clearing the table, the server asks « Have you finished? » before removing any plate."
  "|Payment phrases include « Would you like to pay by cash or card? » and « Here is your receipt »."
  "|The service ends with thanks and a wish such as « Enjoy your meal » or « We hope you enjoyed your evening »."
),
[QC("What does a host ask first at the restaurant entrance ?", "« How old are you? »~« How many people? »~« Where is your car? »~« How much money do you have? »", 1,
     "The host needs to know the size of the party to assign a table."),
 QC("Which phrase introduces the food order ?", "« Are you ready to order? »~« Are you ready to sleep? »~« Where do you work? »~« What time is the train? »", 0,
     "This standard question asks whether the guests have chosen their dishes."),
 QC("What does « well done » mean for meat ?", "Very rare~Medium~Fully cooked~With sauce", 2,
     "« Well done » means the meat is cooked through."),
 QC("What should you say when a dish is unavailable ?", "« No, impossible »~« I am sorry, may I suggest an alternative? »~« Come back later »~« It is your fault »", 1,
     "An apology and a proposal are the professional response."),
 QT("Write a short restaurant service dialogue from the welcome to the bill.",
     "Host: « Good evening. Welcome. Do you have a reservation? » Guest: « Yes, for two, at eight o'clock. » Host: « Of course. This way, please. Would you like a table by the window? » Guest: « Yes, thank you. » Server: « Good evening. Here is the menu. Can I get you something to drink? » Guest: « Still water, please. » Server: « Certainly. Are you ready to order? » Guest: « I would like the grilled salmon. » Server: « Thank you. How would you like your steak, sir? » Guest: « Medium, please. » Server: « Thank you. I will repeat your order to confirm. » At the end: « Would you like to pay by card? Here is your receipt. We hope you enjoyed your evening. »",
     "On attend accueil, proposition de table, boisson, commande, repetition et paiement."),
 QT("How should a server handle a guest who says a dish is cold?",
     "The server should listen without interrupting, apologise sincerely and take the dish back immediately to the kitchen. The plate must be replaced quickly, and the server should check the temperature of the new dish before bringing it to the table. If the kitchen is busy, the server explains the delay honestly and offers a drink while waiting. Details are recorded so the supervisor can identify the cause: a plating delay, a heating problem or a service error. Before leaving, the server asks whether everything is now satisfactory and may propose a complimentary drink or a discount, according to the establishment's policy.",
     "On attend excuser, retirer le plat, verifier le remplacement et tracer l'incident.")],
C("Restaurant English is a sequence of courteous steps: welcome, offer, confirm, serve, clear and pay.",
  "Order = starter + main course + dessert",
  "Apologise + propose an alternative",
  "Reservation~Reservation~Starter~Entree~Main course~Plat principal~Bill~Addition~Allergen~Allergene~Well done~Bien cuit",
  "Greet and check the reservation|Propose a table and present the menu|Offer drinks and take the order|Repeat and serve the order|Clear, present the bill and thank",
  "Remove a plate before asking~Ignore an allergy~Pronounce numbers badly~Forget to repeat the order",
  "Table for two~Table pour deux~By the window~Pres de la fenetre~Medium~A point~Receipt~Recu~Still water~Eau plate",
  "Bill~Addition~Receipt~Recu de paiement",
  "Starter~Entree~Main course~Plat~Dessert~Dessert"))

# ============================================================ AH3
add("AH3", "Anglais professionnel : réclamation et courrier client", "Anglais professionnel hôtelier", ["Terminale"],
S("Complaints in a professional context must be handled with calm, empathy and a clear procedure."
  "|The first phrase is an apology : « I am sorry to hear that », before any explanation or justification."
  "|The employee should let the guest speak and ask precise questions to identify the problem."
  "|Typical problems include a noisy room, a late check-in, a billing error, a cold dish or a missing amenity."
  "|The staff member must check the facts in the system before proposing a solution."
  "|Useful phrases include « Let me check », « What can I do to make things right? » and « Thank you for your patience »."
  "|The solution must be realistic : a room move, a corrected bill, a replacement dish or a gesture of goodwill."
  "|If the employee cannot decide, he or she should call a supervisor rather than improvise a promise."
  "|The incident is recorded with the time, the reason, the action taken and the name of the person in charge."
  "|A professional email begins with a clear subject line and a formal greeting such as « Dear Mr Smith »."
  "|The body of the email states the reason for writing, the facts, the proposed solution and a polite closing."
  "|After the incident, a short follow-up message shows that the establishment cares about the guest's experience."),
[QC("What is the best first reaction to a complaint ?", "Explain the hotel policy~Apologise and listen~Ask the guest to leave~Call the police", 1,
     "An apology and active listening come before any explanation."),
 QC("What does « Let me check » mean ?", "I refuse~I will verify the situation~I do not care~Come back tomorrow", 1,
     "The phrase announces a factual verification."),
 QC("Which is a correct formal email closing ?", "« See you soon guys »~« Kind regards »~« Bye »~« Whatever »", 1,
     "« Kind regards » is a standard professional closing."),
 QC("Why record an incident ?", "To blame someone~To trace the facts and improve the service~To fill time~To avoid answering the guest", 1,
     "Recording allows follow-up and analysis of recurring problems."),
 QT("Write a short email answering a guest who complained about a noisy room.",
     "Subject: Your stay with us - room 214. Dear Mrs Brown, Thank you for taking the time to write to us. I am very sorry to learn that your room was noisy during your stay. I have checked our records and the room is located above the entrance, which can indeed be disturbed in the evening. We should have offered you a quieter room when you booked. As a gesture of goodwill, we would be pleased to offer you a complimentary night in a room on the garden side, subject to availability, or a fifteen percent discount on your next booking. Please let me know which option suits you. Kind regards, The Front Office Manager.",
     "On attend objet formel, excuses, verification, solution concretee et formule de politesse."),
 QT("How should a team learn from a complaint ?",
     "The complaint is first recorded in the logbook with the date, the room, the facts and the action taken. Once a month, the supervisor reviews the logbook to identify patterns: several complaints about noise, slow check-in or billing errors point to a process problem rather than to individual mistakes. The team then discusses the cause and agrees on a corrective action, such as changing the room allocation rule, revising the checklist or adding a verification step on the bill. Staff are trained on the new procedure and the logbook is monitored again to check that the complaints disappear. This turns a negative experience into an improvement of service quality.",
     "On attend tracage, analyse des recurrentes, action corrective et remesure.")],
C("Handling a complaint in English follows a fixed sequence: apologise, check, propose, record and follow up.",
  "Apology + verification + realistic solution",
  "Kind regards · Dear Mr / Mrs · subject line",
  "Complaint~Reclamation~Apology~Excuse~Check~Verification~Solution~Reparation~Logbook~Registre des incidents~Follow-up~Suivi apres incident",
  "Listen and apologise|Ask precise questions|Check the facts in the system|Propose or escalate a solution|Record and follow up",
  "Promise an impossible solution~Justify before apologising~Forget to record~Use a familiar tone in an email",
  "Room 214~Chambre concernee~15 %~Geste commercial~Kind regards~Formule finale~Logbook~Registre",
  "Complaint~Reclamation~Request~Demande simple",
  "Apology~Excuses~Explanation~Explication"))

# ============================================================ EN1
add("EN1", "Démarche RSE et éco-conception de l'établissement", "Environnement et développement durable", ["Terminale"],
S("La responsabilite societale des entreprises, ou RSE, designe la maniere dont une entreprise integre des preoccupations sociales et environnementales dans son activite."
  "|Une demarche RSE repose sur trois piliers : economique, social et environnemental."
  "|Dans l'hotellerie-restauration, les enjeux portent sur l'energie, l'eau, les dechets, l'approvisionnement et les conditions de travail."
  "|L'eco-conception consiste a concevoir des services et des espaces en reduisant leur impact environnemental des la phase de design."
  "|Concretement, cela concerne le choix des materiaux, l'isolation, l'eclairage, la dorure des equipements et la duree de vie du mobilier."
  "|L'analyse du cycle de vie, ou ACV, evalue les impacts d'un produit ou d'un service de l'extraction des matieres a la fin de vie."
  "|Une parties prenantes est un acteur qui influence ou est influence par l'activite : clients, salaries, fournisseurs, collectivites."
  "|La cartographie des parties prenantes aide a prioriser les enjeux et a construire un dialogue."
  "|La materialite, ou double materialite, consistant a retenir les enjeux importants pour l'entreprise et pour la societe."
  "|Un plan d'action RSE fixe des objectifs chiffres, des indicateurs, un calendrier et des responsables."
  "|Le reporting extra-financier rend compte de la demarche dans un rapport developpement durable ou une declaration de performance."
  "|Une demarche credible evite le greenwashing : elle communique uniquement sur des actions reelles et mesurees."),
[QC("Quels sont les trois piliers de la RSE ?", "Economique, social, environnemental~Financier, commercial, publicitaire~Juridique, fiscal, social~Technique, humain, numerique", 0,
     "La RSE articule les dimensions economique, sociale et environnementale."),
 QC("Que designe l'analyse du cycle de vie ?", "L'etude des seuls prix~L'evaluation des impacts de la matiere a la fin de vie~Le bilan comptable~Le plan de marketing", 1,
     "L'ACV consider toutes les etapes de la vie d'un produit ou service."),
 QC("Qu'est-ce qu'une partie prenante ?", "Un client uniquement~Un acteur qui influence ou subit l'activite~Un actionnaire seul~Un fournisseur seul", 1,
     "Salaries, clients, fournisseurs et collectivites sont des parties prenantes."),
 QC("Quel risque correspond au greenwashing ?", "Une communication trop discret~Une communication trompeuse sur l'environnement~Une baisse des prix~Une hausse de l'occupation", 1,
     "Le greenwashing presente des engagements environnementaux non reels."),
 QT("Comment construire un premier plan d'action RSE dans un hotel ?",
     "On commence par un diagnostic : consommations d'energie et d'eau, volume de dechets, pratiques d'achat et conditions de travail. On identifie ensuite les parties prenantes et les enjeux prioritaires par la double materialite. On fixe des objectifs precis et mesurables, par exemple reduire la consommation d'energie de 10 % en deux ans ou obtenir 80 % de fournisseurs locaux pour les fruits et legumes. Chaque action a un responsable, un cout estime et une echeance. On met en place des indicateurs suivis chaque mois et on communique les resultats, y compris les echecs. Enfin, on revise le plan chaque annee a la lumiere des resultats.",
     "On attend diagnostic, parties prenantes, objectifs chiffres, indicateurs et revue annuelle."),
 QT("Expliquer la difference entre eco-conception et compensation carbone.",
     "L'eco-conception agit en amont : elle reduit l'impact des choix des la conception, par exemple en isolant le batiment, en choisissant des equipements peu consommateurs ou en allongeant la duree de vie du mobilier. La compensation intervient en aval : elle finance des actions de reduction ou de sequestration d'emissions ailleurs, comme la plantation d'arbres, pour compenser des emissions non evitees. L'eco-conception est donc preferable, car elle supprime la cause ; la compensation ne doit intervenir qu'en dernier recours apres reduction et substitution. Une communication honnete presente les deux demarches separément et ne presente pas la compensation comme une disparition des emissions.",
     "On attend amont/aval, priorite a la reduction et mise en garde contre le greenwashing.")],
C("La RSE integre economie, social et environnement : la credibilite vient d'objectifs mesures et d'une communication sincere.",
  "3 piliers : economique, social, environnemental",
  "ACV · parties prenantes · double materialite",
  "RSE~Responsabilite societale~Eco-conception~Impact reduit des la conception~ACV~Cycle de vie~Partie prenante~Acteur concerne~Materialite~Enjeux prioritaires~Greenwashing~Communication trompeuse",
  "Realiser un diagnostic|Cartographier les parties prenantes|Prioriser les enjeux|Fixer objectifs et indicateurs|Mesurer, communiquer et reviser",
  "Communiquer sans mesurer~Confondre compensation et reduction~Ignorer les salaries~Fixer des objectifs non chiffres",
  "10 %~Objectif de reduction~2 ans~Echeance~80 %~Fournisseurs locaux~ACV~Analyse du cycle de vie~RSE~Demarche globale",
  "Eco-conception~Agir en amont~Compensation~Agir en aval",
  "Diagnostic~Etat initial~Plan d'action~Engagements futurs"))

# ============================================================ EN2
add("EN2", "Gestion de l'énergie, de l'eau et des déchets", "Environnement et développement durable", ["1re", "Terminale"],
S("Un etablissement hotelier consomme de l'energie pour le chauffage, la climatisation, l'eclairage, l'eau chaude et la cuisine."
  "|Le suivi des consommations s'appuie sur les factures et sur des compteurs separes par usage ou par zone."
  "|Un indicateur courant est la consommation d'energie par nuitee et par metre carre, qui permet les comparaisons dans le temps."
  "|Les actions d'economie concernent l'isolation, les detecteurs de presence, l'eclairage LED, la regulation et l'entretien des equipements."
  "|Le chauffage et la climatisation representent souvent les principaux postes de consommation d'un hotel."
  "|La consommation d'eau depend du nombre de clients, du linge, des sanitaires, de la cuisine et des espaces verts."
  "|Des gestes simples comme le double debit des WC, la detection des fuites et le lavage a pleine charge reduisent la consommation."
  "|Le linge reutilise plutot que change chaque jour est une pratique proposee dans de nombreux hotels."
  "|Les dechets sont tries en plusieurs flux : organiques, emballages, verre, papier, dechets dangereux et ordures menageres."
  "|Le tri a la source est plus efficace lorsqu'il est simple et que les consignes sont affichees pres des points de depôt."
  "|Les dechets dangereux, comme les huiles ou les produits chimiques, suivent une filiere specifique et doivent etre traces."
  "|Le suivi de ces trois ressources permet de reduire les couts, de repondre aux exigences reglementaires et d'alimenter le rapport RSE."),
[QC("Quel est souvent le premier poste energetique d'un hotel ?", "L'eclairage~Le chauffage et la climatisation~Les ordinateurs~L'ascenseur", 1,
     "Le chauffage et la climatisation dominent generalement la consommation."),
 QC("Que mesure une consommation par nuitee ?", "Le cout total~La consommation rapportee a une nuit vendue~Le nombre de clients~La surface du batiment", 1,
     "Cet indicateur permet de comparer des periodes d'activite differentes."),
 QC("Quelle action reduit la consommation d'eau ?", "Changer le linge chaque jour~La reutilisation du linge~Arroser a midi~Laisser couler l'eau", 1,
     "La reutilisation du linge est une mesure classique d'economie d'eau."),
 QC("Comment traiter les huiles de cuisine usees ?", "Les verser dans l'egout~Les melanger aux dechets organiques~Les confier a une filiere specifique tracee~Les bruler en cuisine", 2,
     "Les huiles usees sont des dechets dangereux a filiere dediee."),
 QT("Un hotel passe de 18 000 kWh a 15 300 kWh par an. Calculer la baisse et commenter.",
     "La baisse absolue est de 18 000 - 15 300 = 2 700 kWh. En pourcentage, elle vaut 2 700 / 18 000 = 0,15, soit 15 %. Si le cout du kWh est de 0,18 €, l'economie annuelle est d'environ 486 €. Ce resultat peut venir du remplacement de l'eclairage, d'une meilleure regulation du chauffage ou d'un entretien des equipements. Pour en confirmer l'origine, il faut comparer les memes periodes et tenir compte de la meteo et du taux d'occupation : une annee plus douce ou moins occupee explique une partie de la baisse. On calculera donc aussi la consommation par nuitee.",
     "On attend 2 700 kWh, 15 %,Economie 486 € et prudence sur les facteurs externes."),
 QT("Comment organiser le tri des dechets dans un etablissement de restauration ?",
     "On identifie d'abord les flux produits : dechets organiques, emballages, verre, papier, cartons et dechets dangereux. On place des contenants distincts, identifiables par couleur et par etiquette, aux endroits ou les dechets sont generes : cuisine, plonge, salle et reception. On affiche des consignes simples et on forme les equipes, y compris les nouveaux arrivants et les saisonniers. Les dechets dangereux font l'objet d'un stockage separe et d'un enlevement par une filiere agreee, avec des bords de suivi. On pese regulierement les flux pour mesurer les resultats et on ajuste le dispositif si le tri est insuffisant. Enfin, on valorise les dechets organiques par le compostage ou la methanisation.",
     "On attend flux identifies, contenants, affichage, formation, filiere dangereuse et mesure.")],
C("Energie, eau et dechets se gerent par la mesure, des actions simples et des filieres adaptees.",
  "Baisse % = (avant - apres) / avant",
  "Indicateur = consommation / nuitee",
  "Energie~Consommation du batiment~Par nuitee~Indicateur compare~Eau~Ressource critique~Reutilisation du linge~Economie d'eau~Tri~Separation des flux~Dechet dangereux~Filiere specifique",
  "Mesurer les consommations|Installer des equipements economes|Agir sur les comportements|Organiser le tri a la source|Suivre et comparer les indicateurs",
  "Comparer des periodes non comparables~Negliger les fuites~Melanger les dechets dangereux~Ne pas former les saisonniers",
  "18 000 kWh~Consommation initiale~15 300 kWh~Apres action~-15 %~Baisse relative~486 €~Economie~Tri~Gestion des flux",
  "Consommation~Volume utilise~Indicateur~Rapport a l'activite",
  "Tri~Separer~Valorisation~Reutiliser"))

# ============================================================ EN3
add("EN3", "Tourisme durable, labels et écocertification", "Environnement et développement durable", ["Terminale"],
S("Le tourisme durable vise a satisfaire les besoins des visiteurs tout en preservant les ressources et les territoires pour les generations futures."
  "|Il repose sur trois dimensions : environnementale, socio-culturelle et economique."
  "|Le tourisme de masse peut provoquer une pression sur l'eau, les sols, la biodiversite et le patrimoine."
  "|Une capacite de charge designe le nombre maximal de visiteurs qu'un site peut accueillir sans degradation."
  "|La saisonnalite peut etre attenuee en developpant des offres hors saison et en diversifiant la clientele."
  "|Un label environnemental est une reconnaissance attribuee par un organisme tiers apres verification de criteres."
  "|La certification attribuee par un certificateur accredite apporte une garantie de conformite plus forte qu'une auto-declaration."
  "|L'ecolabel europeen est un label officiel de l'Union europeenne qui couvre notamment les services d'hebergement."
  "|Les criteres portent sur l'energie, l'eau, les dechets, la qualite de l'accueil et l'information des clients."
  "|Les labels comme la cle verte ou Green Key sont des references dans le secteur hotelier."
  "|Obtenir un label demande un diagnostic, des actions correctives, des preuves documentees et un audit."
  "|Le label n'est pas une fin en soi : il doit s'accompagner d'une amelioration continue et d'une communication transparente."),
[QC("Quelles sont les trois dimensions du tourisme durable ?", "Economique, social, environnemental~Prix, qualite, quantite~Public, prive, international~Urbain, rural, littoral", 0,
     "Le developpement durable articule environnement, social et economie."),
 QC("Que designe la capacite de charge ?", "Le nombre maximal de visiteurs sans degradation~Le prix maximum~La duree du sejour~La surface du hotel", 0,
     "C'est la limite d'accueil admissible pour un site."),
 QC("Qui attribue un label environnemental ?", "L'hotelier seul~Un organisme tiers apres verification~Le client~Le fournisseur", 1,
     "Le label implique une verification externe."),
 QC("Quel label est officiel dans l'Union europeenne ?", "Le label macro~L'ecolabel europeen~La cle d'or~Le label bleu", 1,
     "L'ecolabel europeen est le label officiel de l'Union europeenne."),
 QT("Expliquer pourquoi le tourisme durable n'est pas seulement une question environnementale.",
     "Le tourisme durable concerne aussi les dimensions sociale et economique. Sur le plan social, il doit respecter les habitants, les cultures locales et les conditions de travail des salaries, tout en evitant l'eviction des populations par la hausse des prix. Sur le plan economique, il doit assurer des revenus stables aux acteurs locaux et repartir la valeur plutot que la concentrer entre quelques grands groupes. Un hotel peut ainsi former son personnel, acheter localement, proposer des tarifs acessibles hors saison et financer des actions de preservation. Si l'on ne traite que l'environnement, on risque de produire une « green façade » sans benefice reel pour les territoires.",
     "On attend trois dimensions, exemples sociaux et economiques et mise en garde contre le greenwashing."),
 QT("Decrire les etapes pour obtenir un label environnemental dans un hotel.",
     "On choisit d'abord une reference adaptee a la taille et a l'activite de l'etablissement. On realise un diagnostic pour connaitre les consommations et les pratiques actuelles, puis on compare avec le cahier des charges du label. On met en oeuvre les actions necessaires : reduction des consommations, tri des dechets, formation du personnel, information des clients et contractualisation avec les fournisseurs. On constitue un dossier de preuves avec factures, registres et procedures ecrites. Un audit est ensuite realise par l'organisme certificateur, et des corrections peuvent etre demandees. Une fois le label obtenu, il faut maintenir les pratiques, renouveler l'audit et communiquer de maniere precise sur les criteres certifies.",
     "On attend choix de la reference, diagnostic, actions, preuves, audit et maintien.")],
C("Le tourisme durable concilie environnement, societe et economie ; le label certifie des engagements verifies et documentes.",
  "3 dimensions : environnement, social, economique",
  "Capacite de charge · ecolabel · audit",
  "Tourisme durable~Equilibre des trois dimensions~Capacite de charge~Limite d'accueil~Saisonnalite~Concentration des flux~Label~Reconnaissance externe~Ecolabel~Label officiel europeen~Audit~Verification documentaire",
  "Diagnostiquer les impacts|Choisir une reference de label|Mettre en oeuvre les actions|Constituer les preuves|Subir l'audit et maintenir la demarche",
  "Confondre label et publicite~Depasser la capacite de charge~Ignorer les habitants~Ne pas renouveler la certification",
  "3 dimensions~Environnement, social, economie~Ecolabel~Label de l'Union europeenne~Audit~Controle~Capacite~Limite de frequentation",
  "Label~Reconnaissance officielle~Auto-declaration~Sans verification",
  "Diagnostic~Etat des lieux~Certification~Validation externe"))

# FIN DES LOTS
valider_et_ecrire(F, "sthr-mat-part-C.json")
