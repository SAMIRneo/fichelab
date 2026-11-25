# -*- coding: utf-8 -*-
"""Lot D — DA3 Gestion opérationnelle (E7) + DA4 Management de l'équipe (E8) + outils numériques."""
import json, os

OUT = os.path.join(os.path.dirname(__file__), "lead-mco-partie-D.json")
SRC7 = "Référentiel BTS MCO (arrêté du 15 octobre 2018 modifié par l'arrêté du 8 juillet 2024, JORF n° 163 du 10 juillet 2024), annexe I a domaine d'activités 3 et annexe I b bloc de compétences 3, unité U7 (épreuve E7, écrit 3 h, coefficient 3) ; code de commerce (LME), plan comptable général ; annales officielles 2021-2026 (mybts.fr, mucadis.fr)."
SRC8 = "Référentiel BTS MCO (arrêté du 15 octobre 2018 modifié par l'arrêté du 8 juillet 2024, JORF n° 163 du 10 juillet 2024), annexe I a domaine d'activités 4 et annexe I b bloc de compétences 4, unité U8 (épreuve E8, CCF ou écrit 2 h 30, coefficient 3) ; code du travail ; Aurlom, référentiel BTS MCO (août 2026)."

def Q(q, opts, ci, corr):
    return {"type": "qcm", "q": q, "options": opts, "correct": ci, "correction": corr}

def T(q, rep, corr):
    return {"type": "texte", "q": q, "reponse": rep, "correction": corr}

def F(matiere, titre, source, points, questions, annees=None):
    return {"filieres": ["bts-mco"], "annees": annees or ["BTS1", "BTS2"],
            "matiere": matiere, "titre": titre, "source": source,
            "points": points, "questions": questions}

fiches = []

fiches.append(F("Gestion opérationnelle", "Chapitre 1 — Documents commerciaux et cycle d'exploitation", SRC7, [
 "Le cycle d'exploitation décrit le déroulement des opérations courantes : commande, livraison, facturation, encaissement et règlement des fournisseurs.",
 "Le bon de commande (BC) est un document commercial par lequel l'acheteur propose l'achat de biens ou services ; il peut valoir offre contractuelle.",
 "Le bon de livraison (BL) atteste de la remise matérielle des marchandises ; sa signature par le client fait preuve de la livraison.",
 "La facture est le document de facturation obligatoire : elle doit mentionner les identités, la date, le numéro, la désignation, les quantités, les prix HT, la TVA, le total TTC et les conditions de paiement.",
 "L'avoir (ou note de crédit) corrige une facture en cas de retour, de remise ou d'erreur ; il est déduit du montant dû.",
 "Les délais de paiement sont encadrés par la loi LME : 30 jours calendaires après réception pour les professionnels, 45 jours fin de mois ou 60 jours calendaires au maximum pour les contrats professionnels, avec des exceptions pour la grande distribution.",
 "Les escomptes de règlement (ex. 2 % 10 jours, net 30 jours) incitent le client à payer rapidement ; il faut comparer leur coût au coût du découvert bancaire.",
 "Les documents de synthèse (journal, grand livre, balance, compte de résultat, bilan) retracent et synthétisent les opérations comptables.",
 "La dématérialisation des documents (facture électronique, signature électronique, archivage) est encadrée : valeur probatoire, conservation et sécurité.",
 "Dans les études de cas E7, la maîtrise des documents commerciaux est indispensable pour calculer les prix, les marges et la trésorerie."
], [
 Q("Quel document atteste de la remise matérielle des marchandises ?", ["Le bon de commande", "Le bon de livraison", "La facture", "L'avoir"], 1, "Le BL constate la livraison ; la facture constate la créance."),
 Q("Quel délai de paiement de droit commun la loi LME fixe-t-elle entre professionnels ?", ["8 jours", "30 jours calendaires", "90 jours", "180 jours"], 1, "Le délai de droit commun est de 30 jours calendaires après réception."),
 Q("À quoi sert un avoir ?", ["À augmenter une facture", "À corriger une facture (retour, remise, erreur)", "À remplacer un bon de commande", "À payer la TVA"], 1, "L'avoir est un document de correction en faveur du client."),
 Q("Quelle mention ne figure pas obligatoirement sur une facture ?", ["Le numéro de facture", "La date", "Le total TTC", "La couleur du papier"], 3, "Les mentions obligatoires sont fixées par le code de commerce et le CGI."),
 T("Quelle est la différence entre bon de commande et facture ?", "Le bon de commande exprime l'intention d'acheter (offre) ; la facture constate la vente réalisée et la créance de prix.", "Le BC peut être une offre, la facture intervient après l'exécution de la prestation."),
 T("Comment un escompte de règlement influence-t-il la trésorerie ?", "Il accélère l'encaissement mais réduit la marge : il est avantageux si son coût est inférieur à celui du financement court terme évité.", "On compare le taux d'escompte annualisé au coût du découvert bancaire.")
]))

fiches.append(F("Gestion opérationnelle", "Chapitre 2 — Approvisionnements, stocks et inventaires", SRC7, [
 "La gestion des approvisionnements vise à assurer la disponibilité des produits au moindre coût, en évitant ruptures et surstocks.", "Le point de commande est le niveau de stock déclenchant une nouvelle commande : stock de sécurité + (consommation moyenne journalière × délai d'approvisionnement).",
 "Le stock de sécurité protège contre les aléas de consommation ou de livraison ; il immobilise du capital et doit être optimisé.",
 "La formule de Wilson détermine la quantité économique de commande en arbitrant entre coût de passation de commande et coût de possession du stock.",
 "Le taux de rotation du stock rapporte le coût des ventes au stock moyen ; la durée moyenne de stockage et le taux de couverture complètent l'analyse.",
 "Les méthodes de valorisation : CUMP (coût unitaire moyen pondéré), PEPS/FIFO (premier entré, premier sorti), DEPS/LIFO (dernier entré, premier sorti, interdit en comptabilité française).",
 "L'inventaire physique annuel est obligatoire ; l'inventaire tournant et l'inventaire permanent permettent un suivi plus régulier.",
 "Les écarts d'inventaire (démarque inconnue : vol, casse, erreur) sont analysés et font l'objet d'actions correctives.",
 "Le juste-à-temps et le cross-docking réduisent les stocks mais augmentent la dépendance à la fiabilité des fournisseurs et à la logistique.",
 "Les indicateurs de gestion des stocks (taux de rupture, couverture, rotation, valeur du stock) alimentent le tableau de bord du manageur commercial."
], [
 Q("Que désigne le point de commande ?", ["Le stock maximum autorisé", "Le niveau de stock déclenchant une commande", "La date de fin d'année", "Le prix d'achat"], 1, "Le point de commande = stock de sécurité + consommation pendant le délai d'approvisionnement."),
 Q("Quelle méthode de valorisation est interdite en comptabilité française ?", ["Le CUMP", "Le PEPS", "Le DEPS/LIFO", "Le coût d'achat"], 2, "Le LIFO n'est pas admis en comptabilité française, mais peut être utilisé en gestion interne."),
 Q("Que mesure le taux de rotation d'un stock ?", ["Le nombre de renouvellements du stock sur une période", "Le prix de vente moyen", "Le nombre de fournisseurs", "La durée du travail"], 0, "Le taux de rotation = coût des ventes / stock moyen."),
 Q("Quel est un inconvénient du juste-à-temps ?", ["Un stock trop élevé", "Une forte dépendance à la fiabilité des livraisons", "Des coûts de stockage élevés", "Une baisse de la rotation"], 1, "Le JAT réduit le stock mais expose à la rupture en cas de retard fournisseur."),
 T("Comment calculer un stock de sécurité ?", "On estime la consommation moyenne journalière, le délai d'approvisionnement et leur variabilité, puis on détermine le niveau permettant d'absorber les aléas sans surstocker.", "Le stock de sécurité est un arbitrage entre coût de rupture et coût de possession."),
 T("Comment expliquer une démarque inconnue ?", "Elle résulte de vols, de casses, d'erreurs d'enregistrement ou de mauvaise traçabilité ; elle se mesure par l'écart entre stock comptable et stock réel.", "La démarque inconnue doit être quantifiée et faire l'objet d'actions de prévention (contrôle, vidéosurveillance, procédures).")
]))

fiches.append(F("Gestion opérationnelle", "Chapitre 3 — Fixation des prix, marges et démarque", SRC7, [
 "Le prix de vente HT s'obtient en appliquant un coefficient multiplicateur au coût d'achat HT : PV HT = CA HT × coefficient.",
 "Le taux de marque rapporte la marge commerciale au prix de vente HT : (PV HT − CA HT) / PV HT ; le taux de marge la rapporte au coût d'achat : marge / CA HT.",
 "Le coefficient multiplicateur = 1 / (1 − taux de marque), ou encore PV HT / CA HT.",
 "La démarque connue correspond aux remises, rabais et ristournes consentis ; la démarque inconnue aux vols, pertes et erreurs.",
 "La marge commerciale = vente de marchandises − achat de marchandises + variation de stock ; c'est le premier solde intermédiaire de gestion.",
 "La revente à perte est interdite en principe (article L. 442-1 du code de commerce), sauf exceptions : soldes, liquidation, produits périssables, alignement légal.",
 "Les prix d'appel, prix psychologique, prix d'écrémage, prix de pénétration et prix dynamique sont des stratégies de fixation du prix.",
 "La remise, le rabais et la ristourne ont des natures différentes : la remise est immédiate, le rabais sanctionne un défaut, la ristourne est différée selon le volume.",
 "L'élasticité-prix mesure la sensibilité de la demande à une variation de prix : une demande élastique rend une hausse de prix risquée.",
 "Les calculs de prix, de TVA et de marge sont au cœur du QCM de l'épreuve E7 et des études de cas officielles (Banse, E.Leclerc, NEWAY, EQUIDAM)."
], [
 Q("Comment calculer le taux de marque ?", ["Marge / coût d'achat", "Marge / prix de vente HT", "Prix de vente / coût d'achat", "Marge / TVA"], 1, "Le taux de marque se calcule sur le prix de vente HT, le taux de marge sur le coût d'achat."),
 Q("Un coût d'achat de 80 € avec un coefficient de 1,5 donne un prix de vente HT de :", ["90 €", "120 €", "100 €", "125 €"], 1, "80 × 1,5 = 120 €."),
 Q("Quelle pratique est en principe interdite ?", ["La remise quantitative", "La revente à perte", "La vente en solde", "Le prix psychologique"], 1, "La revente à perte est interdite sauf exceptions légales."),
 Q("Que désigne la démarque inconnue ?", ["Une remise accordée au client", "Les pertes, vols et erreurs de stock", "Une baisse de prix programmée", "Une ristourne fournisseur"], 1, "La démarque inconnue est l'écart non expliqué entre stock théorique et stock réel."),
 T("Quand une baisse de prix augmente-t-elle le chiffre d'affaires ?", "Quand la demande est élastique : la hausse de quantité vendue compense la baisse de prix unitaire.", "Si la demande est inélastique, une baisse de prix réduit le chiffre d'affaires et la marge."),
 T("Comment choisir entre hausse de prix et baisse de coût pour améliorer la marge ?", "On compare l'impact sur le volume (élasticité) et la faisabilité : une hausse de prix peut réduire les ventes, alors qu'une négociation fournisseur améliore la marge sans effet sur la demande.", "Le prix agit sur le marché ; le coût d'achat agit sur la structure de marge.")
]))

fiches.append(F("Gestion opérationnelle", "Chapitre 4 — Trésorerie, BFR, FRNG et financements courts", SRC7, [
 "Le besoin en fonds de roulement (BFR) correspond aux ressources immobilisées par le cycle d'exploitation : stocks + créances clients − dettes fournisseurs.",
 "Le fonds de roulement net global (FRNG) = ressources stables − emplois stables ; il représente les moyens durables disponibles pour financer l'exploitation.",
 "L'équilibre financier à court terme se lit dans la relation : trésorerie nette = FRNG − BFR.",
 "Une réduction des délais clients et un allongement des délais fournisseurs diminuent le BFR et améliorent la trésorerie, dans les limites légales et contractuelles.",
 "Les moyens de financement court terme : découvert bancaire, escompte d'effets de commerce, affacturage (factoring), crédit de campagne, Dailly (cession de créances).",
 "L'affacturage transfère le recouvrement des créances à un factor contre une commission ; il améliore la trésorerie mais réduit la marge.",
 "Le suivi de trésorerie s'appuie sur un budget de trésorerie (prévision des encaissements et décaissements) et sur des indicateurs de délais de paiement (DSO, DPO).",
 "Les incidents de paiement (impayés, retards) nécessitent une procédure de recouvrement : relance, mise en demeure, action en justice, provision pour créance douteuse.",
 "Le risque client peut être couvert par une assurance-crédit ou un cautionnement.",
 "Les cas officiels (Aux Merveilleux de Fred 2021, CELIO 2022, Manon Martin 2025) comportent systématiquement des calculs de FRNG, BFR et trésorerie."
], [
 Q("Comment calcule-t-on le BFR ?", ["Stocks + créances − dettes fournisseurs", "FRNG − trésorerie", "Ressources stables − emplois stables", "CA − charges"], 0, "BFR = actif circulant d'exploitation − passif circulant d'exploitation."),
 Q("Si le FRNG est inférieur au BFR, la trésorerie nette est…", ["Positive", "Négative", "Nulle", "Égale au BFR"], 1, "Trésorerie nette = FRNG − BFR : si FRNG < BFR, la trésorerie est négative."),
 Q("Que fait l'affacturage ?", ["Il augmente les stocks", "Il transforme des créances en trésorerie immédiate", "Il réduit les ventes", "Il remplace la facture"], 1, "Le factor avance une partie du montant des créances cédées, moyennant commission."),
 Q("Quel indicateur mesure le délai moyen de recouvrement des clients ?", ["Le DSO", "Le DPO", "Le ROI", "Le NPS"], 0, "DSO = Days Sales Outstanding ; DPO = délai de paiement des fournisseurs."),
 T("Comment améliorer la trésorerie sans emprunter ?", "En réduisant les stocks, en accélérant le recouvrement des créances, en négociant les délais fournisseurs et en limitant les immobilisations inutiles.", "Ces leviers agissent directement sur le BFR et donc sur la trésorerie nette."),
 T("Quand recourir à l'escompte plutôt qu'au découvert ?", "Quand le coût annualisé de l'escompte est inférieur à celui du découvert et que le client paie anticipativement.", "La comparaison des coûts de financement est indispensable avant le choix.")
]))

fiches.append(F("Gestion opérationnelle", "Chapitre 5 — Compte de résultat, SIG et seuil de rentabilité", SRC7, [
 "Le compte de résultat retrace les charges et les produits de l'exercice, classés par nature : exploitation, financier, exceptionnel, puis impôt sur les sociétés.",
 "Les soldes intermédiaires de gestion (SIG) sont : marge commerciale, valeur ajoutée, excédent brut d'exploitation (EBE), résultat d'exploitation, résultat courant avant impôts, résultat exceptionnel, résultat net.",
 "La valeur ajoutée = chiffre d'affaires + production immobilisée + subventions − achats consommés − services extérieurs.",
 "L'EBE = valeur ajoutée + subventions d'exploitation − impôts et taxes − charges de personnel ; il mesure la rentabilité opérationnelle avant amortissements.",
 "Le résultat d'exploitation = EBE + transferts de charges − amortissements et provisions.",
 "Les charges fixes ne varient pas avec l'activité (loyer, salaires) ; les charges variables suivent le volume (achats, commissions).",
 "La marge sur coûts variables = chiffre d'affaires − charges variables ; le seuil de rentabilité (point mort) est atteint quand la marge sur coûts variables couvre les charges fixes.",
 "Seuil de rentabilité en valeur = charges fixes / taux de marge sur coûts variables ; en volume = charges fixes / marge sur coûts variables unitaire.",
 "Le ratio de sécurité (ou marge de sécurité) mesure l'écart entre chiffre d'affaires réel et chiffre d'affaires de seuil ; il indique la résistance de l'entreprise à une baisse d'activité.",
 "Les cas E.Leclerc 2023 (mur à jus) et NEWAY 2024 demandent explicitement le calcul du résultat prévisionnel et du seuil de rentabilité."
], [
 Q("Quel SIG mesure la rentabilité opérationnelle avant amortissements ?", ["La marge commerciale", "L'EBE", "Le résultat net", "Le résultat courant"], 1, "L'excédent brut d'exploitation est calculé avant amortissements et provisions."),
 Q("Comment calculer le seuil de rentabilité en valeur ?", ["Charges fixes / taux de marge sur coûts variables", "CA / charges variables", "Charges variables / CA", "Marge / stock"], 0, "Le point mort est atteint lorsque la marge sur coûts variables couvre les charges fixes."),
 Q("Quelle charge est une charge variable ?", ["Le loyer du magasin", "Le salaire fixe du manager", "L'achat de marchandises", "L'assurance multirisque"], 2, "L'achat de marchandises varie avec le volume vendu."),
 Q("Que mesure la marge de sécurité ?", ["L'écart entre CA réel et CA de seuil", "Le bénéfice net", "Le montant des amortissements", "Le taux d'endettement"], 0, "La marge de sécurité indique la marge de manœuvre avant le point mort."),
 T("Comment interpréter un résultat d'exploitation en baisse alors que le CA augmente ?", "Cela signifie que les charges ont crû plus vite que le chiffre d'affaires (achats, personnel, amortissements) : la rentabilité opérationnelle se dégrade malgré l'activité.", "Il faut analyser les SIG pour localiser l'origine de la dégradation."),
 T("Comment le seuil de rentabilité aide-t-il à décider d'une promotion ?", "Il indique le volume additionnel nécessaire pour couvrir le coût de l'opération ; on le compare aux prévisions de ventes pour juger de la rentabilité attendue.", "Un objectif de volume inférieur au seuil de rentabilité de l'opération conduit à une perte.")
]))

fiches.append(F("Gestion opérationnelle", "Chapitre 6 — Budgets, prévisions de ventes et décisions d'investissement", SRC7, [
 "La démarche budgétaire comporte la définition d'objectifs, le chiffrage des prévisions, l'exécution et le contrôle des écarts.",
 "Les principaux budgets : budget des ventes, budget des achats, budget de trésorerie, budget d'exploitation et budget d'investissement.",
 "La prévision des ventes s'appuie sur l'historique, l'analyse de tendance (moyennes mobiles, moindres carrés) et les coefficients saisonniers.", "Un coefficient saisonnier rapporte la valeur d'une période à la moyenne : il permet de corriger les prévisions et de lisser les comparaisons.",
 "Le budget des achats se déduit des ventes prévues, du stock initial et du stock final souhaité : achats = ventes + stock final − stock initial.",
 "L'investissement (corporel, incorporel, financier) engage des flux de trésorerie sur plusieurs exercices ; il se distingue de l'exploitation par sa durée.",
 "Les ressources de financement : autofinancement (CAF), emprunt, crédit-bail, subventions, augmentation de capital.",
 "L'annuité d'un emprunt est calculée à partir du capital, du taux d'intérêt et de la durée ; le tableau d'amortissement détaille capital remboursé et intérêts.",
 "La VAN (valeur actuelle nette) actualise les flux nets de trésorerie au coût du capital : un projet est créateur de valeur si la VAN est positive.",
 "Le TRI (taux de rentabilité interne) est le taux d'actualisation qui annule la VAN ; le délai de récupération indique le temps nécessaire pour retrouver la mise de fonds.",
 "Les cas EQUIDAM 2025 (comparaison de financements, matrice de choix fournisseur) et Gamm Vert 2021 (VAN) illustrent ces calculs."
], [
 Q("Comment calculer les achats prévisionnels ?", ["Ventes + stock final − stock initial", "Ventes − stock final", "Stock initial + stock final", "Ventes × coefficient"], 0, "Achats = ventes prévues + stock final souhaité − stock initial."),
 Q("Quelle décision prendre si la VAN d'un projet est positive ?", ["Rejeter le projet", "Accepter le projet (à rentabilité comparable)", "Annuler les prévisions", "Emprunter systématiquement"], 1, "Une VAN positive signifie que le projet crée de la valeur au regard du coût du capital."),
 Q("Quel outil lisse les variations saisonnières dans une prévision ?", ["Le coefficient saisonnier", "Le seuil de rentabilité", "Le BFR", "Le NPS"], 0, "Le coefficient saisonnier corrige la tendance selon la période."),
 Q("Que représente le TRI ?", ["Le taux qui annule la VAN", "Le taux d'inflation", "La durée de l'emprunt", "Le taux de marge"], 0, "Le TRI est le taux d'actualisation pour lequel VAN = 0."),
 T("Comment élaborer un budget des ventes ?", "On part de l'historique des ventes, on identifie la tendance et la saisonnalité, on intègre les actions commerciales prévues et les hypothèses de prix, puis on chiffre le CA mensuel.", "Le budget des ventes sert de point de départ aux autres budgets."),
 T("Comment comparer deux modes de financement d'un investissement ?", "On calcule le coût total de chaque solution (intérêts, commissions, loyers, fiscalité), on compare l'impact sur la trésorerie et le bilan, puis on intègre les critères qualitatifs (flexibilité, garanties, propriété).", "Le choix ne dépend pas seulement du coût : le crédit-bail évite l'endettement mais ne rend pas propriétaire.")
]))

fiches.append(F("Gestion opérationnelle", "Chapitre 7 — Tableau de bord, indicateurs de performance, reporting et risques", SRC7, [
 "Le tableau de bord est un outil de pilotage qui regroupe des indicateurs sélectionnés, mis à jour régulièrement, avec objectifs, réalisations et écarts.",
 "Les indicateurs commerciaux : chiffre d'affaires, évolution, taux de transformation, panier moyen, fréquentation, taux de rotation, taux de rupture, NPS.",
 "Les indicateurs financiers : marge commerciale, taux de marque, EBE, résultat d'exploitation, BFR, trésorerie nette, seuil de rentabilité.",
 "Un indicateur pertinent est fiable, simple à calculer, compréhensible, actionnable et relié à un objectif ; trop d'indicateurs dilue l'attention.",
 "La construction d'un tableau de bord suit quatre étapes : choisir les indicateurs, fixer les objectifs, collecter les données, analyser les écarts et déclencher des actions.",
 "Le reporting est la remontée structurée d'informations vers la hiérarchie : support écrit ou numérique, périodicité, destinataire, commentaires sur les causes des écarts.",
 "L'analyse d'écarts distingue un écart de volume, de prix, de mix produit et de calendrier ; elle identifie les actions correctrices possibles.",
 "La gestion des risques de l'unité commerciale couvre les risques commerciaux, financiers, humains, informatiques, sanitaires et environnementaux.",
 "Le principe de précaution et la conformité réglementaire (hygiène, sécurité, RGPD, lutte contre le blanchiment) font partie des responsabilités du manageur.",
 "Les études de cas E7 (Ludiklandes 2026, NEWAY 2024, CELIO 2022) demandent systématiquement la réalisation et l'analyse d'un tableau de bord suivie de préconisations."
], [
 Q("Quelle qualité un indicateur de tableau de bord doit-il avoir ?", ["Être le plus nombreux possible", "Être actionnable et fiable", "Être complexe", "Être secret"], 1, "Un bon indicateur est compréhensible, fiable et susceptible de déclencher une action."),
 Q("Que contient un tableau de bord ?", ["Uniquement le CA", "Des indicateurs, objectifs, réalisations et écarts", "Le bilan uniquement", "Les seules prévisions"], 1, "La comparaison objectif/réalisation est au cœur du pilotage par tableau de bord."),
 Q("Quel écart correspond à une modification de la composition des ventes ?", ["Un écart de prix", "Un écart de volume", "Un écart de mix", "Un écart de change"], 2, "L'écart de mix traduit un changement dans la structure des ventes."),
 Q("À quoi sert le reporting ?", ["À remonter l'information vers la hiérarchie", "À remplacer le compte de résultat", "À supprimer les écarts", "À vendre plus cher"], 0, "Le reporting structure la remontée d'informations et le commentaire des écarts."),
 T("Comment analyser un écart de chiffre d'affaires ?", "On le décompose en écart de volume (quantités vendues), écart de prix (tarif, remises) et écart de mix (structure des ventes), puis on identifie les causes et les actions correctrices.", "Cette décomposition permet d'agir précisément au lieu de constater globalement une baisse."),
 T("Quels risques doit surveiller le manageur d'une unité commerciale ?", "Les risques commerciaux (baisse de trafic), financiers (trésorerie, impayés), humains (absentéisme, RPS), informatiques (données, cyber), sanitaires et environnementaux.", "Chaque risque identifié doit faire l'objet d'une évaluation et d'une mesure de prévention ou de couverture.")
]))

fiches.append(F("Management de l'équipe commerciale", "Chapitre 1 — Organiser le travail : besoins en personnel, tâches et plannings", SRC8, [
 "L'organisation du travail commence par l'évaluation des besoins en personnel : volume d'activité, compétences requises, charge de travail et contraintes d'ouverture.",
 "La taille de l'équipe peut être estimée en rapportant le volume d'activité prévisionnel à la productivité moyenne d'un collaborateur, avec une marge pour les absences.",
 "La répartition des tâches distingue les activités permanentes (accueil, vente, caisse) et les missions ponctuelles (inventaire, animation, formation).",
 "Le planning du personnel doit respecter la durée légale du travail (35 heures hebdomadaires), les temps de repos, les jours fériés, les congés et la convention collective.",
 "Les plannings peuvent être hebdomadaires, mensuels ou annuels ; ils doivent être affichés et communiqués dans les délais réglementaires.",
 "L'annualisation et le travail à temps partiel sont encadrés ; les heures supplémentaires ouvrent droit à une majoration ou à un repos compensateur.",
 "Le diagramme de Gantt planifie les tâches dans le temps et visualise les chevauchements et les jalons d'un projet.",
 "L'organisation doit tenir compte de la digitalisation : nouvelle répartition entre vente en ligne, click and collect et conseil en magasin.",
 "Le manageur arbitre entre productivité et qualité de vie au travail : un planning trop serré génère stress, absentéisme et turnover.",
 "Les cas historiques (Leroy Merlin, Chronodrive, Banse) comportent des exercices classiques de planning et de taille d'équipe."
], [
 Q("Quelle est la durée légale hebdomadaire du travail en France ?", ["35 heures", "39 heures", "40 heures", "32 heures"], 0, "La durée légale est de 35 heures par semaine ; les heures au-delà sont des heures supplémentaires."),
 Q("Quel outil visualise les tâches d'un projet dans le temps ?", ["Le diagramme de Gantt", "Le planogramme", "Le bilan fonctionnel", "Le NPS"], 0, "Le Gantt représente les tâches, leurs durées et leurs chevauchements."),
 Q("Quel élément ne doit pas être ignoré dans un planning ?", ["Les préférences de couleur", "Les temps de repos et la convention collective", "La météo", "Le prix des fournitures"], 1, "Le planning est soumis au droit du travail et à la convention collective."),
 Q("Quel risque génère un planning trop chargé ?", ["Une baisse de l'absentéisme", "Du stress et du turnover", "Une hausse de la marge", "Plus de fidélité"], 1, "La surcharge de travail alimente les RPS, l'absentéisme et le départ des salariés."),
 T("Comment estimer le besoin en personnel d'un rayon ?", "On évalue le volume d'activité prévisionnel, on le divise par la productivité moyenne par salarié, puis on ajoute une marge pour les absences et les pics d'activité.", "Cette estimation doit être confrontée aux contraintes réglementaires et à la qualité de service attendue."),
 T("Comment construire un planning équilibré ?", "On recense les besoins horaires par créneau, les compétences et disponibilités de chacun, les contraintes légales, puis on répartit les tâches en prévoyant des marges pour les imprévus.", "Un bon planning concilie efficacité opérationnelle, respect du droit et équité entre salariés.")
]))

fiches.append(F("Management de l'équipe commerciale", "Chapitre 2 — Recruter et intégrer un collaborateur", SRC8, [
 "Le recrutement débute par l'analyse du besoin : profil de poste, compétences techniques et comportementales, expérience, formation et conditions de rémunération.",
 "La fiche de poste décrit l'intitulé, la mission, les activités, les compétences requises, les conditions d'exercice et les relations hiérarchiques et fonctionnelles.",
 "L'annonce doit être attractive, non discriminatoire et diffusée sur les canaux adaptés (site de l'entreprise, réseaux professionnels, agences, écoles).",
 "La présélection compare candidatures et CV aux critères définis ; elle doit rester objective et tracée.",
 "L'entretien de recrutement suit une structure : accueil, présentation du poste et de l'entreprise, questions comportementales et situationnelles, échange sur les attentes du candidat, conclusion.",
 "Les questions doivent être ouvertes et non discriminatoires ; le candidat doit pouvoir poser des questions sur le poste et les conditions de travail.",
 "La grille d'évaluation objective les critères et évite les biais (effet de halo, ressemblance, stéréotypes).",
 "Le coût du recrutement comprend la diffusion de l'annonce, le temps passé, les entretiens, les tests et, le cas échéant, les frais d'agence.",
 "L'intégration (onboarding) comprend l'accueil, la présentation de l'équipe, la formation au poste et aux outils, le tutorat et un suivi à 1, 3 et 6 mois.",
 "Le contrat de travail doit être rédigé conformément au code du travail : type de contrat, durée, temps de travail, rémunération, lieu et fonction."
], [
 Q("Que doit contenir une fiche de poste ?", ["Uniquement le salaire", "La mission, les activités et les compétences requises", "L'avis des concurrents", "Les couleurs de l'enseigne"], 1, "La fiche de poste cadre le recrutement et l'évaluation."),
 Q("Quel type de question privilégier en entretien ?", ["Une question fermée oui/non", "Une question ouverte sur une situation vécue", "Une question sur la vie privée", "Une question discriminatoire"], 1, "Les questions comportementales et situationnelles permettent d'évaluer les compétences."),
 Q("Que vise une grille d'évaluation ?", ["À objectiver les critères de sélection", "À masquer les critères", "À embaucher le premier candidat", "À réduire le nombre d'entretiens"], 0, "La grille limite les biais et sécurise la décision."),
 Q("Quel est un élément du coût de recrutement ?", ["Le temps passé aux entretiens", "Le prix de vente moyen", "Le stock moyen", "Le taux de rotation"], 0, "Le coût inclut diffusion, temps, tests et éventuels frais d'agence."),
 T("Comment conduire un entretien de recrutement efficace ?", "En préparant la fiche de poste et une grille, en alternant présentation et questions ouvertes, en écoutant activement et en laissant le candidat s'exprimer sur ses motivations.", "Un entretien réussi est structuré, respectueux et centré sur les compétences requises."),
 T("Pourquoi soigner l'intégration d'un nouveau collaborateur ?", "Parce qu'un bon recrutement peut échouer si l'accueil, la formation et le suivi sont négligés ; l'intégration réduit le turnover et accélère l'autonomie.", "Le tutorat et les points de suivi à 1, 3 et 6 mois sécurisent la prise de poste.")
]))

fiches.append(F("Management de l'équipe commerciale", "Chapitre 3 — Animer et motiver l'équipe commerciale", SRC8, [
 "L'animation d'équipe vise à créer les conditions de l'engagement : information, participation, reconnaissance et développement des compétences.",
 "La réunion d'équipe (briefing) se prépare : ordre du jour, objectifs, supports, durée, participants ; elle se conduit avec des tours de parole et se clôt par un compte rendu.",
 "Le briefing quotidien ou hebdomadaire permet de diffuser les objectifs, les résultats, les actions du jour et les messages de l'enseigne.",
 "L'entretien individuel (entretien de suivi, de recadrage, annuel) alterne écoute, constat, analyse et engagement sur des actions précises.",
 "Les leviers de motivation : clarté des objectifs, autonomie, feedback régulier, reconnaissance, équité de traitement, formation, challenges et rémunération variable.",
 "Les théories de la motivation utiles au manager : Maslow (besoins), Herzberg (hygiène/motivateurs), Adams (équité), Locke (objectifs).",
 "La fixation d'objectifs efficace respecte la logique SMART : spécifique, mesurable, atteignable, réaliste et temporellement défini.",
 "L'animation commerciale collective (challenge, compétition interne, émission d'idées) doit être encadrée pour éviter la pression excessive et les comportements contraires à l'éthique.",
 "Le manager doit adapter son style (directif, participatif, délégatif) à la situation et à la maturité du collaborateur.",
 "L'épreuve E8 évalue la capacité à concevoir et conduire une réunion ou un entretien, avec une argumentation claire et une attention portée à l'implication de l'équipe."
], [
 Q("Que signifie l'acronyme SMART pour un objectif ?", ["Simple, Moyen, Ambitieux, Rapide, Technique", "Spécifique, Mesurable, Atteignable, Réaliste, Temporel", "Stratégique, Marché, Action, Résultat, Temps", "Social, Motivation, Animation, Réunion, Travail"], 1, "La méthode SMART cadre la fixation des objectifs."),
 Q("Quel est un levier de motivation selon Herzberg ?", ["Le salaire", "La reconnaissance", "Le règlement intérieur", "Le nombre de réunions"], 1, "La reconnaissance et l'accomplissement sont des facteurs de motivation ; le salaire est un facteur d'hygiène."),
 Q("Quelle est la première étape d'une réunion d'équipe ?", ["Rédiger le compte rendu", "Préparer l'ordre du jour et les objectifs", "Donner la parole sans préparation", "Clore immédiatement"], 1, "La préparation détermine l'efficacité de la réunion."),
 Q("Quel style de management délègue le plus d'autonomie ?", ["Directif", "Participatif", "Délégatif", "Autocratique"], 2, "Le style délégatif laisse au collaborateur la responsabilité de la décision."),
 T("Comment conduire un briefing d'équipe efficace ?", "En annonçant l'ordre du jour, en présentant chiffres et objectifs, en donnant la parole à chacun, en reformulant les engagements et en diffusant un compte rendu court.", "Un briefing est court, participatif et orienté vers l'action."),
 T("Comment motiver une équipe après un échec commercial ?", "En analysant les causes sans recherche de culpabilité, en valorisant les efforts, en fixant des objectifs correctifs réalistes et en mettant en place un accompagnement et des actions de formation.", "La reconnaissance du travail accompli et la clarté du plan d'action restaurent la confiance.")
]))

fiches.append(F("Management de l'équipe commerciale", "Chapitre 4 — Évaluer les performances de l'équipe et individualiser la formation", SRC8, [
 "L'évaluation des performances porte sur les résultats individuels et collectifs, les comportements professionnels et les compétences mobilisées.",
 "Le tableau de bord social suit : chiffre d'affaires par vendeur, taux de transformation, panier moyen, objectifs atteints, absentéisme, turnover et formations réalisées.",
 "L'entretien annuel d'évaluation est un temps réglementé et structuré : bilan de l'année, évaluation des compétences, attentes de l'entreprise, souhaits du salarié et engagement sur des actions.",
 "L'évaluation doit être factuelle, fondée sur des données et des exemples, et distinguer la performance de la personne du contexte (affluence, allocation des rayons, formation reçue).",
 "Les écarts de performance appellent un diagnostic : manque de compétence, manque de motivation, objectifs inadaptés, outils défaillants ou problème relationnel.",
 "Le plan d'action individuel précise les actions de formation, le tutorat, les objectifs révisés et les délais de suivi.",
 "La formation peut être collective (plan de formation) ou individualisée : CPF, alternance, VAE, formation interne ou externe.",
 "La montée en compétences est stratégique dans un contexte d'omnicanalité : conseil digital, outils CRM, gestion des réclamations et connaissance produit.",
 "La notation et la rémunération variable doivent être transparentes et perçues comme équitables pour éviter la démotivation.",
 "Le manager rend compte à sa hiérarchie des résultats de l'équipe et des actions d'accompagnement engagées (reporting social)."
], [
 Q("Quel indicateur relève du tableau de bord social ?", ["Le taux d'absentéisme", "Le FRNG", "Le taux de rotation des stocks", "Le seuil de rentabilité"], 0, "L'absentéisme et le turnover sont des indicateurs sociaux."),
 Q("Quelle qualité caractéristique un entretien annuel réussi ?", ["Il est purement financier", "Il est factuel, structuré et tourné vers l'avenir", "Il évite les questions du salarié", "Il dure moins de 5 minutes"], 1, "L'entretien annuel combine bilan factuel et projet de progression."),
 Q("Quelle est une cause possible d'un écart de performance ?", ["Un objectif inadapté", "La couleur du uniforme", "Le nombre de pages du contrat", "La météo"], 0, "Un objectif irréaliste ou mal défini peut expliquer l'écart, tout comme la compétence ou la motivation."),
 Q("Quel dispositif permet à un salarié de financer sa formation ?", ["Le CPF", "Le BFR", "Le NPS", "Le DSO"], 0, "Le compte personnel de formation est utilisable tout au long de la carrière."),
 T("Comment préparer un entretien annuel d'évaluation ?", "En rassemblant les données chiffrées, les exemples concrets, les objectifs de l'année et les besoins de formation, puis en préparant un plan d'action et un temps d'écoute.", "La préparation garantit un entretien factuel et constructif."),
 T("Comment individualiser la formation d'un collaborateur ?", "En identifiant précisément l'écart de compétence, en choisissant le dispositif adapté (CPF, formation interne, tutorat), en fixant des objectifs et en prévoyant une évaluation des acquis.", "La formation individualisée répond à un besoin diagnostiqué plutôt qu'à un catalogue général.")
]))

fiches.append(F("Management de l'équipe commerciale", "Chapitre 5 — Gérer les conflits, les RPS et les situations de crise", SRC8, [
 "Un conflit peut naître d'un désaccord sur les tâches, les objectifs, les valeurs ou les relations interpersonnelles ; il n'est pas forcément négatif s'il est traité.",
 "Les sources fréquentes en unité commerciale : répartition des tâches, plannings, reconnaissance perçue, pression commerciale, changements d'organisation.",
 "La gestion d'un conflit suit une démarche : écouter les parties, reformuler, identifier les intérêts sous-jacents, rechercher une solution acceptable et formaliser l'accord.",
 "Les styles de gestion des conflits (Thomas-Kilmann) : évitement, accommodation, compétition, compromis et collaboration.",
 "Le harcèlement moral ou sexuel est interdit et réprimé pénalement ; l'employeur doit organiser la prévention, signaler et traiter les situations signalées.",
 "Les risques psycho-sociaux (RPS) comprennent le stress, la charge de travail excessive, l'exigence émotionnelle, la violence et le harcèlement ; ils sont évalués dans le DUERP.",
 "Le manager doit repérer les signaux faibles : changement de comportement, absences répétées, baisse de performance, isolement, plaintes.",
 "En situation de crise (incident client grave, rupture de stock majeure, départ brutal d'un collaborateur), il faut contenir l'urgence, informer, décider et communiquer.",
 "Le respect de l'éthique et de la déontologie implique l'égalité de traitement, la lutte contre les discriminations et la protection de la dignité des personnes.",
 "L'épreuve E8 peut demander de préparer un entretien de recadrage ou une médiation entre deux collaborateurs, avec une proposition de suite écrite."
], [
 Q("Quel style de gestion de conflit recherche une solution gagnant-gagnant ?", ["L'évitement", "La compétition", "La collaboration", "L'accommodation"], 2, "La collaboration vise à satisfaire les intérêts légitimes de chaque partie."),
 Q("Quel document recense les risques professionnels, y compris les RPS ?", ["Le DUERP", "Le planogramme", "Le budget des ventes", "La facture"], 0, "Le document unique d'évaluation des risques professionnels est obligatoire."),
 Q("Quel signal faible peut indiquer un RPS ?", ["Une hausse des ventes", "Des absences répétées et un isolement", "Un nouveau fournisseur", "Une baisse des stocks"], 1, "Les changements de comportement et l'absentéisme doivent alerter le manager."),
 Q("Comment qualifier un harcèlement moral ?", ["Une simple remarque occasionnelle", "Des agissements répétés portant atteinte à la dignité ou à la santé", "Une consigne de travail", "Une sanction légale"], 1, "La répétition et l'atteinte à la dignité ou à la santé caractérisent le harcèlement."),
 T("Comment conduire un entretien de recadrage ?", "En décrivant les faits de manière factuelle, en écoutant l'explication, en rappelant les règles et les attentes, puis en définissant avec le salarié des engagements et un suivi.", "Le recadrage n'est pas une sanction déguisée : il vise à restaurer les comportements attendus."),
 T("Que faire face à un conflit entre deux vendeurs ?", "Écouter séparément chaque partie, reformuler les intérêts, organiser une médiation, rechercher une solution partagée (répartition des tâches, horaires) et formaliser l'accord avec un suivi.", "Le manager ne doit pas prendre parti précipitamment : il cherche une solution durable et équitable.")
]))

fiches.append(F("Management de l'équipe commerciale", "Chapitre 6 — Outils numériques du manager et système d'information commercial", SRC8, [
 "Le système d'information commercial (SIC) regroupe les outils qui collectent, traitent et diffusent l'information commerciale : CRM, ERP/PGI, tableaux de bord, messagerie et espaces collaboratifs.",
 "Le CRM (Customer Relationship Management) centralise les données clients, l'historique des contacts, les opportunités et les actions de fidélisation.",
 "L'ERP/PGI intègre les fonctions achats, ventes, stocks, comptabilité et RH dans une base de données commune, ce qui facilite la cohérence des informations.",
 "Les outils de business intelligence (BI) permettent de construire des tableaux de bord interactifs et d'analyser les données de vente.",
 "Les outils collaboratifs (messagerie instantanée, visioconférence, partage de documents, plannings partagés) facilitent le travail d'équipe et le télétravail.",
 "Le manager doit maîtriser les outils de pilotage : suivi des objectifs en temps réel, alertes sur les écarts, export de données pour le reporting.",
 "La qualité des données est une responsabilité managériale : saisie rigoureuse, mise à jour, déduplication et contrôle des accès.",
 "Le RGPD impose une base légale, la minimisation des données, des durées de conservation définies et des mesures de sécurité ; le manager est garant de la conformité des usages de son équipe.",
 "La cybersécurité (mots de passe, authentification à deux facteurs, phishing, sauvegardes) fait partie de la responsabilité du manager d'unité.",
 "Le numérique ne remplace pas le management : il doit être accompagné d'une formation des équipes et d'une clarification des rôles et des processus."
], [
 Q("Quel outil centralise les données et le suivi des clients ?", ["Un ERP", "Un CRM", "Un tableur", "Une messagerie"], 1, "Le CRM est dédié à la relation et à la connaissance client."),
 Q("Quel outil intègre les fonctions achats, ventes, stocks et comptabilité ?", ["Le CRM", "L'ERP/PGI", "Le réseau social", "Le tableur isolé"], 1, "L'ERP (progiciel de gestion intégré) unifie les processus de l'entreprise."),
 Q("Quelle responsabilité incombe au manager en matière de données ?", ["Ignorer le RGPD", "Veiller à la qualité, à la sécurité et à la conformité des usages", "Supprimer toutes les données", "Les publier"], 1, "Le manager est responsable de la conformité des traitements réalisés par son équipe."),
 Q("Quel risque informatique correspond à un email frauduleux demandant un mot de passe ?", ["Le phishing", "Le backup", "Le cloud", "Le CRM"], 0, "Le phishing est une tentative d'hameçonnage d'identifiants."),
 T("Comment le SIC améliore-t-il le pilotage d'une équipe commerciale ?", "Il fournit des données actualisées sur les ventes, les stocks et les clients, permet de suivi des objectifs en temps réel et facilite le reporting vers la hiérarchie.", "Le SIC n'a de valeur que si les données saisies sont fiables et utilisées dans la décision."),
 T("Comment sécuriser l'usage des outils numériques par l'équipe ?", "En formant les collaborateurs, en définissant des droits d'accès adaptés, en imposant des mots de passe robustes et l'authentification à deux facteurs, et en organisant des sauvegardes et la mise à jour des logiciels.", "La sécurité combine mesures techniques, procédures et sensibilisation des utilisateurs.")
]))

annales = []
annales.append({"filieres":["bts-mco"],"annees":["BTS2"],"titre":"Gestion opérationnelle 2026 — Cas national LUDIKLANDES", "matiere":"Gestion opérationnelle","type":"genere",
 "contenu":"Épreuve E7 — Gestion opérationnelle (écrit 3 heures, coefficient 3). Sujet national 2026, d'après le cas officiel LUDIKLANDES (mybts.fr).\n\nCONTEXTE : LUDIKLANDES est une enseigne de distribution de jouets et de loisirs. Le cas porte sur l'analyse des performances commerciales d'un magasin, sur sa situation financière et sur une décision d'investissement.\n\nDOCUMENTS (9 pages) : tableau de bord des ventes par famille, données de fréquentation et de transformation, compte de résultat, bilan fonctionnel, tableau de trésorerie, offres de financement et QCM de calculs commerciaux.\n\nQUESTIONS : 1. Réalisez le tableau de bord du magasin et analysez les écarts par rapport aux objectifs. 2. Analysez la performance commerciale (familles de produits, saisonnalité, taux de transformation, panier moyen) et proposez des actions correctrices. 3. Analysez la situation financière (SIG, FRNG, BFR, trésorerie) et commentez l'équilibre. 4. Étudiez l'opportunité d'un investissement : calculez la VAN et le délai de récupération, comparez les modes de financement et concluez. 5. Traitez le QCM (calculs de prix, TVA, facturation, marges).",
 "correction":"1. Le tableau de bord reprend les indicateurs fournis (CA, évolution, panier moyen, taux de transformation, fréquentation) avec objectifs, réalisations et écarts ; l'analyse hiérarchise les écarts significatifs et propose des pistes d'action par famille de produits.\n\n2. L'analyse commerciale croise la saisonnalité (pic de fin d'année pour les jouets), la performance des familles et les indicateurs de transformation ; les actions portent sur l'assortiment, l'implantation, les animations et la communication locale.\n\n3. L'analyse financière calcule les SIG (marge commerciale, valeur ajoutée, EBE, résultat d'exploitation), le FRNG, le BFR et la trésorerie nette ; elle met en évidence les déséquilibres éventuels et propose des leviers (réduction des stocks, négociation des délais).\n\n4. L'investissement est évalué par l'actualisation des flux nets (VAN), le TRI ou le délai de récupération ; les financements (emprunt, crédit-bail, autofinancement) sont comparés par leur coût total, leur impact sur la trésorerie et le bilan, et leur flexibilité. La conclusion est explicitement donnée.\n\n5. Le QCM teste la maîtrise des calculs commerciaux : prix HT/TTC, coefficient, taux de marque et de marge, escompte, remises et TVA. Chaque réponse est justifiée par le calcul."})
annales.append({"filieres":["bts-mco"],"annees":["BTS2"],"titre":"Gestion opérationnelle 2025 — Cas national EQUIDAM", "matiere":"Gestion opérationnelle","type":"genere",
 "contenu":"Épreuve E7 (3 heures, coefficient 3). Sujet national 2025, d'après le cas officiel EQUIDAM (mybts.fr).\n\nCONTEXTE : EQUIDAM est une entreprise de distribution dont la situation financière, les performances commerciales et les choix d'investissement sont à analyser. Le cas comporte également une matrice de comparaison de fournisseurs et une question sur l'écoulement d'un stock d'invendus.\n\nDOCUMENTS : comptes annuels, tableau de bord trimestriel, grille de notation de quatre fournisseurs, offres de financement, données sur les invendus.\n\nQUESTIONS : 1. Analysez la situation financière de l'entreprise à partir des comptes et calculez les principaux ratios. 2. Comparez deux solutions de financement pour un investissement et argumentez votre recommandation. 3. Analysez les performances commerciales de l'enseigne et les résultats trimestriels. 4. Construisez une matrice de sélection d'un fournisseur à partir des critères fournis et justifiez le choix. 5. Proposez une solution pour écouler le stock d'invendus en comparant coûts, marges et risques. 6. Traitez le QCM de calculs financiers et commerciaux.",
 "correction":"1. L'analyse des comptes conduit au calcul des SIG (marge commerciale, EBE, résultat), du FRNG, du BFR et de la trésorerie nette, ainsi que de ratios (endettement, liquidité, autonomie). Le diagnostic distingue les problèmes de rentabilité et de liquidité.\n\n2. Les solutions de financement (emprunt classique, crédit-bail, autofinancement) sont comparées par le coût total, l'incidence sur le bilan, la capacité de remboursement et le maintien du contrôle.\n\n3. L'analyse commerciale porte sur l'évolution du CA par magasin ou par famille, la saisonnalité, le taux de transformation et le panier moyen ; elle débouche sur des actions correctrices chiffrées.\n\n4. La matrice pondère les critères (prix, qualité, délais, conditions de paiement, services) selon leur importance ; le fournisseur retenu est celui qui obtient le meilleur score pondéré, sous réserve de cohérence avec la stratégie.\n\n5. Les solutions pour les invendus (promotion, lot, vente en ligne, donation, destruction) sont comparées par la marge espérée, le coût induit et l'impact sur l'image.\n\n6. Le QCM porte sur des calculs de prix, de marge, de TVA, de seuil de rentabilité et de point mort."})
annales.append({"filieres":["bts-mco"],"annees":["BTS2"],"titre":"Gestion opérationnelle 2024 — Cas national NEWAY", "matiere":"Gestion opérationnelle","type":"genere",
 "contenu":"Épreuve E7 (3 heures, coefficient 3). Sujet national 2024, d'après le cas officiel NEWAY (mybts.fr).\n\nCONTEXTE : NEWAY est une enseigne spécialisée dans l'équipement de la maison. Le cas est technique : réalisation d'un tableau de bord, prévision des ventes, calculs de prix, rentabilité d'une opération promotionnelle et gestion des commandes.\n\nDOCUMENTS : données mensuelles de vente, listes de prix et remises fournisseurs, coûts de l'opération promotionnelle, tableau de suivi des commandes.\n\nQUESTIONS : 1. Réalisez le tableau de bord demandé et commentez les principaux écarts. 2. Établissez les prévisions de ventes du prochain trimestre en utilisant la tendance et la saisonnalité. 3. Calculez les prix d'achat, les prix de vente et les taux de marge des produits proposés. 4. Déterminez la rentabilité de l'opération promotionnelle et son seuil de rentabilité. 5. Analysez le suivi des commandes et proposez des mesures pour réduire les délais et les ruptures. 6. Traitez le QCM de calculs financiers.",
 "correction":"1. Le tableau de bord intègre CA, évolution, objectifs, écarts, taux de transformation, panier moyen et indicateurs de stock ; le commentaire met en évidence les écarts significatifs et leurs causes possibles.\n\n2. Les prévisions utilisent une moyenne mobile ou une droite de tendance, corrigée par les coefficients saisonniers ; les hypothèses sont explicitées.\n\n3. Les calculs de prix appliquent le coefficient multiplicateur, distinguent taux de marque et taux de marge, et intègrent remises, rabais et TVA.\n\n4. La rentabilité de l'opération se mesure par le CA incrémental, la marge dégagée et le coût de l'action ; le seuil de rentabilité indique le volume minimum nécessaire. La conclusion précise si l'opération doit être menée.\n\n5. L'analyse des commandes identifie les goulets d'étranglement (délais fournisseurs, réception, mise en rayon) et propose : point de commande révisé, stock de sécurité, suivi des livraisons et communication avec les équipes.\n\n6. Le QCM évalue la maîtrise des calculs financiers (VAN, annuités, ratios, seuil de rentabilité)."})
annales.append({"filieres":["bts-mco"],"annees":["BTS2"],"titre":"Sujet type E8 Management — Planification, conflit et animation d'équipe", "matiere":"Management de l'équipe commerciale","type":"genere",
 "contenu":"Épreuve E8 — Management de l'équipe commerciale (CCF ou ponctuel écrit 2 h 30, coefficient 3).\n\nCONTEXTE : une unité commerciale de 800 m² emploie 14 salariés. Le responsable doit préparer les fêtes de fin d'année : pic d'activité attendu de +35 %, deux démissions à pourvoir, des tensions entre vendeurs sur la répartition des tâches et un taux d'absentéisme en hausse. Documents : historique d'activité, contrat de travail et convention collective, plannings des trois derniers mois, grille de salaire, plaintes de collaborateurs.\n\nQUESTIONS : 1. Évaluez les besoins en personnel pour la période de pointe et proposez un effectif réaliste. 2. Construisez un planning respectant la durée du travail, les repos et les contraintes de l'activité. 3. Rédigez une annonce et définissez la grille d'entretien pour le recrutement des deux postes. 4. Analysez les causes des tensions et proposez une méthode de médiation. 5. Concevez un briefing d'équipe de 15 minutes pour mobiliser les collaborateurs autour des objectifs. 6. Définissez trois indicateurs de suivi social et commercial et expliquez comment vous rendrez compte à la direction.",
 "correction":"1. Le besoin se calcule à partir de l'historique d'activité et du pic de +35 %, en divisant la charge prévisionnelle par la productivité moyenne et en intégrant une marge d'absentéisme. On compare avec l'effectif disponible après démissions.\n\n2. Le planning répartit les horaires selon les flux, respecte les 35 heures, les repos quotidiens et hebdomadaires, les jours fériés et la convention collective ; il prévoit des renforts et une rotation des tâches.\n\n3. L'annonce décrit le poste, les compétences, les conditions et reste non discriminatoire ; la grille d'entretien comporte des critères objectifs et des questions comportementales.\n\n4. Les tensions portent sur la répartition des tâches et la reconnaissance perçue ; la médiation consiste à écouter chaque partie, reformuler les intérêts, rechercher une solution équitable (rotation, critères transparents) et formaliser un accord suivi.\n\n5. Le briefing suit un ordre du jour : résultats, objectifs de la période, répartition des rôles, consignes de qualité et de sécurité, temps de questions, engagement de chacun ; un compte rendu court est diffusé.\n\n6. Indicateurs : taux de réalisation des objectifs, absentéisme, taux de rotation, formations réalisées et NPS client ; le reporting à la direction présente les résultats, les écarts et les actions engagées."})

with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"fiches": fiches, "annales": annales}, f, ensure_ascii=False, indent=2)
print("D", len(fiches), len(annales))
