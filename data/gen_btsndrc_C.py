# -*- coding: utf-8 -*-
"""Generateur btsndrc-mat-part-C.json — lot C.

20 fiches : Droit (5), Économie (5), Maths / stats (5),
Anglais professionnel (3), Français (2). Filiere bts-ndrc, annees BTS1 / BTS2.
Structure 'fiche prototype' copiee sur gen_generale_modele.py : 12 points,
10 questions corrigees (8 QCM + 2 texte), 7 blocs en ordre strict, 3 schemas SVG
construits avec diag().
"""
import ast
import os
import re
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fixtures import (fiche, qcm, qt, diag, svg_grille, svg_flux, svg_etapes,
                      svg_compare, bloc, valider_et_ecrire)

REF = ("Arrêté du 19 février 2018 modifié (NOR ESRS1803333A, BO du 15 mars 2018), BTS "
       "« Négociation et digitalisation de la relation client » (RNCP 38368) · Référentiel "
       "de certification U1 à U6 (annexes I a, I b, II a, II b), arrêtés modificatifs des "
       "13 décembre 2023, 19 mars 2024 et 8 juillet 2024 · éduscol, ressources BTS NDRC")
FIL = ["bts-ndrc"]


def BI(t, x): return bloc(t, texte=x, type="intro")
def BF(t, eq, leg): return bloc(t, eq=eq, leg=leg, type="formule")
def BG(t, items): return bloc(t, items=items, type="grille")
def BL(t, items): return bloc(t, items=items, type="liste")
def BE(t, items): return bloc(t, items=items, type="etapes")
def BA(t, items): return bloc(t, items=items, type="attention")
def BX(t, items): return bloc(t, items=items, type="exemples")


def Q(*items):
    """8 tuples QCM (question, options, index, correction) puis 2 tuples texte."""
    out = []
    for it in items:
        if isinstance(it[1], (list, tuple)):
            out.append(qcm(it[0], it[1], it[2], it[3]))
        else:
            out.append(qt(it[0], it[1], it[2]))
    return out


def add(prefix, titre, mat, ans, pts, qs, blocs,
        st=("Synthèse", "Démarche", "À faire / à éviter")):
    """Ajoute une fiche complete ; les 3 schemas sont derives des blocs."""
    intro, formule, *rest = blocs
    if "|" in intro:
        intro = intro.split("|", 1)[1]
    eq, leg = formule.split("|", 1)
    def parse(s):
        prot = re.sub(r"([A-Za-z])'([A-Za-zÀ-ÿ])",
                      lambda m: m.group(1) + "\u2019" + m.group(2), s)
        return ast.literal_eval(prot)
    grille, liste, etapes, attention, exemples = (parse(s) for s in rest)
    aff = [
        BI("L'idée en une phrase", intro),
        BF("L'essentiel en une formule", eq, leg),
        BG("Tableau de synthèse", grille),
        BL("À retenir", liste),
        BE("Méthode pas à pas", etapes),
        BA("Pièges fréquents", attention),
        BX("Exemples chiffrés", exemples),
    ]
    sch = [
        diag("1 · " + st[0], svg_grille(st[0], grille[0], grille[1:])),
        diag("2 · " + st[1], svg_etapes(st[1], etapes)),
        diag("3 · " + st[2], svg_compare(st[2], ("À faire", etapes[:2]),
                                          ("À éviter", attention[:2]))),
    ]
    F.append(fiche(FIL, ans, mat, prefix + " · " + titre, REF, pts, qs, aff, sch))


F = []

# ============================================================ DR1
add("DR1", "Contrat et obligations dans la relation commerciale", "Droit", ["BTS1"],
[
 "Le contrat est un accord de volontés entre deux ou plusieurs personnes destiné à créer, modifier ou éteindre des obligations (article 1101 du Code civil).",
 "Un contrat est valable si le consentement est sain, la personne a la capacité juridique, le contenu est licite et la forme est respectée quand la loi l'exige.",
 "Le vice du consentement (erreur, dol, violence) peut entraîner l'annulation du contrat ; l'erreur n'est annulable que si elle porte sur une qualité essentielle de la chose.",
 "L'article 1103 pose que les contrats légalement formés tiennent lieu de loi à ceux qui les ont faits : la partie doit exécuter sa prestation.",
 "L'article 1104 impose d'exécuter le contrat de bonne foi : cette obligation s'applique à la négociation, à la formation et à l'exécution.",
 "L'inexécution donne lieu à des sanctions : l'exception d'inexécution (suspendre sa prestation), la résolution (mettre fin au contrat) et les dommages-intérêts.",
 "Les dommages-intérêts visent à réparer intégralement le préjudice prévisible et direct, sans enrichir la victime ni laisser de perte non réparée.",
 "Une clause qui prive une partie de l'essentiel de son engagement est réputée non écrite ; dans un contrat d'adhésion, une clause créant un déséquilibre significatif est également réputée non écrite.",
 "L'article 1195 permet de demander une renégociation en cas de changement de circonstances imprévisible et bouleversant l'équilibre contractuel, puis une résolution ou une adaptation par le juge.",
 "La responsabilité contractuelle suppose une faute, un dommage et un lien de causalité ; le créancier doit prouver le manquement du débiteur.",
 "En prospection et négociation, la bonne foi interdit les fausses promesses et la rétention d'information déterminante dans le consentement du client.",
 "Exemple : un fournisseur qui ne livre pas peut voir le contrat résolu et devoir des dommages-intérêts correspondant au surcoût subi par le client pour se réapprovisionner.",
],
Q(
 ("Quel article du Code civil énonce que le contrat tient lieu de loi aux parties ?", ["L'article 1101", "L'article 1103", "L'article 1195", "L'article 1231-1"], 1,
  "L'article 1103 du Code civil dispose que les contrats légalement formés tiennent lieu de loi à ceux qui les ont faits."),
 ("Quel vice du consentement suppose une fausse représentation de la réalité ?", ["L'erreur", "Le dol", "La violence", "La capacité"], 0,
  "L'erreur est une fausse croyance sur un élément essentiel ; le dol est une manipulation volontaire par manoeuvres ou mensonges."),
 ("Quel principe impose d'exécuter le contrat de bonne foi ?", ["L'article 1104", "L'article 1101", "L'article 1170", "L'article 1217"], 0,
  "L'article 1104 du Code civil impose la bonne foi dans la négociation, la formation et l'exécution du contrat."),
 ("Quelle sanction suspend l'exécution de sa propre prestation ?", ["La résolution", "L'exception d'inexécution", "Les dommages-intérêts", "L'annulation"], 1,
  "L'exception d'inexécution permet au créancier de suspendre sa prestation jusqu'à l'exécution par l'autre partie."),
 ("Que réparent les dommages-intérêts contractuels ?", ["Tous les préjudices même indirects", "Le préjudice direct, certain et légitime", "Les seuls frais de justice", "Le prix du contrat"], 1,
  "La réparation couvre le dommage direct et prévisible, à l'exclusion des préjudices trop indirects ou hypothétiques."),
 ("Que se passe-t-il pour une clause réputée non écrite ?", ["Le contrat est annulé entièrement", "La clause est écartée, le reste subsiste", "La clause devient obligatoire", "Le juge la réduit de moitié"], 1,
  "Une clause réputée non écrite est considérée comme n'ayant jamais existé ; le reste du contrat reste en vigueur."),
 ("Dans quel cas l'article 1195 peut-il jouer ?", ["Un simple changement de prix prévu", "Un bouleversement imprévisible de l'équilibre", "Une erreur dans l'offre", "Un retard de paiement"], 1,
  "L'imprévision exige un changement de circonstances imprévisible qui bouleverse l'économie du contrat."),
 ("Quelle preuve incombe au créancier dans une action en responsabilité ?", ["La preuve de son seul dommage", "Le manquement, le dommage et le lien de causalité", "La preuve de la bonne foi du débiteur", "Aucune preuve"], 1,
  "Le créancier doit établir la faute contractuelle, le dommage subi et le lien de causalité entre eux."),
 ("Distinguer exception d'inexécution et résolution du contrat.",
  "L'exception d'inexécution est une mesure provisoire : le créancier suspend sa propre prestation tant que l'autre partie n'exécute pas, sans rompre le contrat. La résolution met définitivement fin au contrat et dispense les parties de leurs obligations futures, sans préjudice des dommages-intérêts. La première conserve la relation, la seconde l'éteint.",
  "On oppose une suspension temporaire à une extinction définitive du contrat."),
 ("Un fournisseur ne livre pas et le client paie 500 € de plus chez un autre fournisseur. Analyser les sanctions possibles.",
  "Le client peut d'abord invoquer l'exception d'inexécution pour suspendre son paiement. Il peut ensuite demander la résolution du contrat pour inexécution et réclamer des dommages-intérêts. Le préjudice de 500 € correspond au surcoût direct et prévisible lié au réapprovisionnement ; il devra justifier ce montant. La bonne foi impose au fournisseur d'informer rapidement de son incapacité afin de limiter le dommage.",
  "On enchaîne exception, résolution et réparation, puis on vérifie la preuve du préjudice."),
),
(
 "L'idée en une phrase|Un contrat oblige, mais il s'exécute de bonne foi : quand la prestation manque, le droit offre d'abord la suspension, puis la résolution et la réparation.",
 "Sanctions|Exception d'inexécution → résolution → dommages-intérêts|La bonne foi encadre la négociation, la formation et l'exécution.",
 "[['Notion', 'Article', 'Effet'], ['Contrat', '1101', 'Accord de volontes'], ['Loi des parties', '1103', 'Obligation d executer'], ['Bonne foi', '1104', 'Execution loyale'], ['Imprevision', '1195', 'Renegociation'], ['Reparation', '1231-1', 'Dommages-interets']]",
 "['Verifier la validite du contrat', 'Identifier la prestation due', 'Constater le manquement et la mise en demeure', 'Choisir la sanction adaptee', 'Justifier le montant du prejudice']",
 "['Lire les clauses et la forme', 'Determiner les obligations de chaque partie', 'Documenter l inexécution', 'Mettre en demeure avant d agir', 'Estimer le dommage reparable']",
 "['Promettre un avantage que l on sait faux', 'Celer une information determinante', 'Refuser toute renegociation malgre l imprévision', 'Confondre resolution et exception', 'Réclamer un prejudice hypothetique']",
 "['Surcout de 500 € apres defaillance', 'Mise en demeure ecrite avant action', 'Exception = suspension du paiement', 'Resolution = fin du contrat', 'Dommages = prejudice direct et prouve']",
), st=("Notions contractuelles", "Réagir à l'inexécution", "Exécution loyale / fautive"))

# ============================================================ DR2
add("DR2", "Droit de la consommation et pratiques commerciales", "Droit", ["BTS1"],
[
 "Le Code de la consommation protège le consommateur, défini comme toute personne agissant à des fins étrangères à son activité professionnelle.",
 "Avant la conclusion du contrat, le professionnel doit fournir une information claire et lisible sur les caractéristiques du bien, le prix, les frais, le délai de livraison et les garanties.",
 "Les pratiques commerciales trompeuses consistent à induire le consommateur en erreur par des affirmations fausses ou des omissions sur des éléments déterminants (article L. 121-1 et suivants).",
 "Une pratique commerciale agressive exploite une situation de vulnérabilité, une contrainte ou un harcèlement pour obtenir une décision d'achat.",
 "En cas d'achat à distance ou hors établissement, le consommateur dispose en principe d'un délai de rétractation de 14 jours à compter de la livraison ou de la signature.",
 "Le professionnel doit informer le consommateur de ce droit avant la commande et lui fournir un formulaire de rétractation.",
 "Les clauses abusives créent un déséquilibre significatif entre les droits et obligations des parties ; elles sont réputées non écrites (article L. 212-1).",
 "La garantie légale de conformité dure deux ans et s'applique aux biens neufs ; le consommateur peut exiger réparation, remplacement ou, à défaut, remboursement.",
 "La garantie commerciale est une promesse volontaire du vendeur ou du fabricant : elle ne peut pas réduire les droits issus de la garantie légale.",
 "Le prix doit être indiqué de manière lisible et exhaustive : les frais supplémentaires non mentionnés ne peuvent pas être facturés.",
 "En BTS NDRC, le commercial doit présenter l'offre sans optimisation trompeuse, vérifier l'information précontractuelle et connaître le délai de rétractation.",
 "Exemple : afficher 29 € puis ajouter 9 € de frais de dossier au moment du paiement constitue une pratique trompeuse par omission de prix.",
],
Q(
 ("Qui est un consommateur au sens du Code de la consommation ?", ["Toute personne qui achète pour son activité", "Toute personne agissant à des fins étrangères à son activité professionnelle", "Toute entreprise", "Le seul vendeur"], 1,
  "Le consommateur agit à des fins personnelles, étrangères à son activité professionnelle."),
 ("Quel délai de rétractation s'applique en principe à un achat en ligne ?", ["7 jours", "14 jours", "30 jours", "Aucun délai"], 1,
  "Le délai légal de rétractation est de 14 jours pour les contrats à distance et hors établissement."),
 ("Quand doit-on informer le consommateur de son droit de rétractation ?", ["Après la livraison", "Avant la conclusion du contrat", "Uniquement sur demande", "Jamais"], 1,
  "L'information précontractuelle est obligatoire avant la commande, avec un formulaire de rétractation."),
 ("Quelle pratique est trompeuse par omission ?", ["Afficher un prix complet", "Cacher des frais de dossier", "Préciser le délai de livraison", "Mentionner la garantie"], 1,
  "Omettre une information déterminante comme le prix total est une pratique trompeuse."),
 ("Quelle est la durée de la garantie légale de conformité pour un bien neuf ?", ["6 mois", "1 an", "2 ans", "5 ans"], 2,
  "La garantie légale de conformité des biens neufs est de deux ans."),
 ("Une garantie commerciale peut-elle réduire la garantie légale ?", ["Oui, si le contrat le prévoit", "Non", "Uniquement pour les professionnels", "Uniquement après 6 mois"], 1,
  "La garantie commerciale s'ajoute aux droits légaux et ne peut pas les réduire."),
 ("Quel est l'effet d'une clause abusive ?", ["Elle est réputée non écrite", "Elle s'applique malgré tout", "Elle annule tout le contrat", "Elle devient une garantie"], 0,
  "Une clause abusive est réputée non écrite ; le reste du contrat demeure."),
 ("Quel réflexe adopter avant de conclure une vente à distance ?", ["Vérifier l'information précontractuelle et le droit de rétractation", "Omettre les frais", "Accélérer le paiement", "Supprimer la facture"], 0,
  "Le commercial doit s'assurer que le client a reçu les informations obligatoires et connaît son délai de rétractation."),
 ("Distinguer pratique trompeuse et pratique agressive.",
  "Une pratique trompeuse induit le consommateur en erreur par une affirmation fausse ou une omission d'information déterminante, ce qui fausse sa décision. Une pratique agressive obtient la décision par la contrainte, le harcèlement ou l'exploitation d'une situation de vulnérabilité. Les deux sont interdites, mais la première agit sur l'information et la seconde sur la liberté de décision.",
  "On oppose l'atteinte à l'information et l'atteinte à la liberté de choisir."),
 ("Un site affiche 29 € puis ajoute 9 € de frais au paiement, soit 38 €. Qualifier la pratique et indiquer les conséquences.",
  "L'affichage d'un prix incomplet est une pratique commerciale trompeuse par omission d'une information déterminante sur le prix total : le consommateur croit payer 29 € alors qu'il en paie 38, soit une hausse de 31 %. Les frais non annoncés ne peuvent pas être facturés et l'entreprise s'expose à des sanctions administratives ou pénales, à une action du consommateur et à une obligation de mise en conformité. Le prix doit être affiché toutes taxes et frais compris avant la commande.",
  "On qualifie la pratique, on chiffre l'écart et on énonce les conséquences juridiques et commerciales."),
),
(
 "L'idée en une phrase|Informer avant de vendre n'est pas une formalité : c'est la condition d'un consentement valable et d'une relation durable.",
 "Protection du consommateur|Information précontractuelle + rétractation 14 j + garantie 2 ans|Les clauses abusives sont réputées non écrites.",
 "[['Droit', 'Délai / durée', 'Point de vigilance'], ['Information', 'Avant la commande', 'Prix total et frais'], ['Rétractation', '14 jours', 'Formulaire fourni'], ['Conformité', '2 ans', 'Bien neuf'], ['Clause abusive', 'Non écrite', 'Déséquilibre']]",
 "['Verifier les mentions obligatoires', 'Afficher le prix complet', 'Joindre le formulaire de retrait', 'Expliquer la garantie legale', 'Conserver la preuve de l information']",
 "['Rédiger une offre lisible', 'Vérifier prix, frais et délais', 'Mentionner le droit de rétractation', 'Présenter les garanties', 'Conserver une trace de l information']",
 "['Cacher les frais jusqu au paiement', 'Affirmer un avantage faux', 'Presser un client vulnerable', 'Réduire la garantie legale par une clause', 'Omettre le formulaire de retrait']",
 "['29 € affichés + 9 € caches = 38 €', 'Soit + 31 % au moment du paiement', 'Rétractation : 14 jours', 'Garantie légale : 2 ans', 'Clause abusive = non écrite']",
), st=("Droits du consommateur", "Conclure en conformité", "Information claire / trompeuse"))

# ============================================================ DR3
add("DR3", "Concurrence et relations de distribution", "Droit", ["BTS2"],
[
 "Le droit de la concurrence garantit la liberté d'accès au marché et interdit les comportements qui faussent le jeu concurrentiel.",
 "L'article L. 410-1 du Code de commerce pose le principe de la liberté de la concurrence, sous réserve des règles propres à certains secteurs.",
 "Les ententes entre entreprises concurrentes sont interdites lorsqu'elles ont pour objet ou effet de restreindre la concurrence, notamment sur les prix ou la répartition des marchés.",
 "L'abus de position dominante consiste, pour une entreprise puissante, à exploiter sa situation pour écarter des concurrents ou imposer des conditions disproportionnées.",
 "Les pratiques restrictives de concurrence visent notamment le déséquilibre significatif dans un contrat et la rupture brutale d'une relation commerciale établie.",
 "La rupture d'une relation commerciale établie doit être notifiée par écrit avec un préavis tenant compte de l'ancienneté de la relation ; une durée minimale de trois mois est prévue par le texte.",
 "Un fournisseur ne peut pas soumettre l'octroi d'un avantage à l'achat d'un autre produit sans justification : c'est la vente conditionnée, en principe interdite.",
 "Les prix ne peuvent pas être imposés au revendeur par le fournisseur, sauf exception légale : le revendeur fixe librement son prix de revente.",
 "La violation de ces règles peut être sanctionnée par l'Autorité de la concurrence et donner lieu à des dommages-intérêts pour les victimes.",
 "Les contrats de distribution (concession, franchise) organisent la relation entre le fournisseur et le revendeur ; la franchise implique une marque commune et un savoir-faire.",
 "Avant de signer un contrat de franchise, le candidat doit recevoir un document d'information précontractuel suffisamment tôt pour disposer d'un délai de réflexion.",
 "Exemple : un distributeur rompt sans préavis une relation de cinq ans représentant 30 % du chiffre du fournisseur : la rupture est probablement brutale et ouvrira droit à indemnisation.",
],
Q(
 ("Quel principe pose l'article L. 410-1 du Code de commerce ?", ["La liberté de la concurrence", "Le prix imposé", "Le monopole", "La vente conditionnée"], 0,
  "L'article L. 410-1 énonce la liberté de la concurrence, principle fondateur du droit commercial."),
 ("Qu'est-ce qu'une entente entre concurrents ?", ["Un accord sur les prix interdit en principe", "Une vente au détail", "Un contrat de travail", "Une garantie légale"], 0,
  "Un accord entre concurrents sur les prix ou le partage du marché est une entente interdite lorsqu'elle restreint la concurrence."),
 ("Quel préavis minimal s'applique à la rupture d'une relation établie ?", ["Aucun préavis", "Trois mois", "Un an", "Dix ans"], 1,
  "Le texte prévoit un préavis écrit tenant compte de la relation, avec une durée minimale de trois mois."),
 ("Qu'est-ce que la vente conditionnée ?", ["Subordonner un avantage à l'achat d'un autre produit", "Vendre à perte", "Imposer un prix de revente", "Refuser une remise"], 0,
  "La vente conditionnée soumet l'octroi d'un avantage à l'achat d'un autre produit ou service, ce qui est en principe interdit."),
 ("Un fournisseur peut-il imposer un prix de revente ?", ["Toujours", "En principe non", "Uniquement en franchise", "Uniquement en ligne"], 1,
  "Le revendeur fixe librement ses prix ; l'imposition de prix de revente est en principe interdite."),
 ("Quelle autorité sanctionne les pratiques anticoncurrentielles en France ?", ["La CNIL", "L'Autorité de la concurrence", "L'URSSAF", "Le tribunal des affaires de sécurité sociale"], 1,
  "L'Autorité de la concurrence instruit et sanctionne ententes, abus de position dominante et pratiques restrictives."),
 ("Quel document doit recevoir un candidat à la franchise ?", ["Un document d'information précontractuel", "Une facture", "Un bulletin de salaire", "Un avis d'imposition"], 0,
  "La réglementation impose la remise d'un document d'information avant la signature ou le versement de fonds."),
 ("Quel est le risque d'une rupture sans préavis ?", ["Aucun risque", "Une action en dommages-intérêts", "Une hausse de la marge", "Une garantie automatique"], 1,
  "Une rupture brutale d'une relation établie peut être sanctionnée et donner lieu à indemnisation du préjudice."),
 ("Expliquer la différence entre entente et abus de position dominante.",
  "Une entente est un accord ou une concertation entre plusieurs entreprises, généralement concurrentes, pour restreindre la concurrence, par exemple sur les prix. L'abus de position dominante est le comportement unilatéral d'une entreprise détenant un pouvoir de marché, qui exploite cette position pour écarter des rivaux ou imposer des conditions abusives. La première implique plusieurs acteurs, la seconde un seul acteur puissant.",
  "On oppose un accord entre entreprises à un comportement unilatéral d'une entreprise dominante."),
 ("Un fournisseur met fin à une relation de cinq ans sans préavis ; le revendeur réalisait 30 % de son chiffre avec cette marque. Analyser la situation.",
  "La relation étant ancienne et stabilisée, sa rupture totale et immédiate sans préavis écrit constitue probablement une rupture brutale au sens de l'article L. 442-1 du Code de commerce. Le préavis minimal légal est de trois mois et doit tenir compte de l'ancienneté. Le revendeur peut demander des dommages-intérêts correspondant au préjudice subi, par exemple la perte de marge sur la période de préavis et les frais de réorganisation. Le fournisseur doit dokumenter les motifs de la rupture et proposer un préavis adapté.",
  "On qualifie la rupture, on rappelle le préavis et on évalue le préjudice indemnizable."),
),
(
 "L'idée en une phrase|La concurrence protège le jeu du marché : ni accord entre rivaux, ni abus de puissance, ni rupture brutale d'un partenaire.",
 "Interdictions|Ententes · abus de position dominante · ventes conditionnées · rupture brutale|Préavis écrit, au moins trois mois.",
 "[['Pratique', 'Interdiction', 'Sanction'], ['Entente sur les prix', 'Interdite', 'Autorité de la concurrence'], ['Abus dominant', 'Interdit', 'Sanctions et dommages'], ['Vente conditionnee', 'Interdite en principe', 'Action en concurrence'], ['Rupture brutale', 'Préavis requis', 'Dommages-interets']]",
 "['Qualifier la pratique observe', 'Verifier la base legale', 'Evaluer les effets sur le marche', 'Identifier les sanctions possibles', 'Mettre en conformite le contrat']",
 "['Cartographier les relations commerciales', 'Verifier les clauses du contrat de distribution', 'Respecter le preavis ecrit', 'Former les equipes commerciales', 'Documenter les decisions de rupture']",
 "['S aligner sur les prix concurrents par accord', 'Imposer un prix au revendeur', 'Rompre sans preavis ecrit', 'Subordonner une remise a un achat', 'Omettre le document d information en franchise']",
 "['Relation de 5 ans, 30 % du CA du revendeur', 'Preavis minimal : 3 mois', 'Rupture brutale → indemnisation', 'Prix de revente libre', 'Document precontractuel avant signature']",
), st=("Règles de concurrence", "Sécuriser la distribution", "Pratique licite / interdite"))

# ============================================================ DR4
add("DR4", "Droit social et contrat de travail", "Droit", ["BTS2"],
[
 "Le contrat de travail est une convention par laquelle une personne s'engage à travailler pour le compte d'une autre, sous sa direction et son contrôle, moyennant une rémunération.",
 "Trois critères caractérisent le contrat de travail : la prestation de travail, la rémunération et le lien de subordination.",
 "Le CDI est le contrat de droit commun, sans durée déterminée ; le CDD est conclu pour une durée limitée et ne peut répondre qu'à des motifs prévus par la loi.",
 "La période d'essai permet à l'employeur d'évaluer le salarié et à celui-ci de tester l'emploi ; sa durée est limitée et doit être prévue au contrat.",
 "La durée légale du travail est de 35 heures par semaine ; les heures supplémentaires donnent droit à une majoration de salaire ou à un repos compensateur.",
 "Le salaire doit être au moins égal au SMIC et respecter la convention collective applicable ; le principe « à travail égal, salaire égal » s'applique.",
 "Le salarié bénéficie de congés payés, de jours de repos, d'une protection sociale et du droit à la formation professionnelle.",
 "L'employeur doit assurer la sécurité et protéger la santé physique et mentale des travailleurs ; le DUERP recense les risques professionnels.",
 "Le licenciement doit respecter une procédure : convocation à un entretien préalable, entretien, puis notification écrite avec indication du motif.",
 "Un licenciement sans cause réelle et sérieuse expose l'employeur à des dommages-intérêts ; la rupture conventionnelle est une modalité de départ négociée et homologuée.",
 "En management commercial, le responsable doit connaître ces règles pour conduire les entretiens, fixer les objectifs et éviter les pratiques discriminatoires.",
 "Exemple : un commercial recruté en CDD pour remplacer une salariée en congé maternité répond à un motif légal de recours au CDD.",
],
Q(
 ("Quels sont les trois critères du contrat de travail ?", ["Préstation, rémunération, subordination", "Bénéfice, stock, prix", "Client, produit, marché", "Formation, diplôme, âge"], 0,
  "Le contrat de travail suppose une prestation de travail, une rémunération et un lien de subordination."),
 ("Quel est le contrat de droit commun ?", ["Le CDD", "Le CDI", "Le contrat d'apprentissage", "Le contrat saisonnier"], 1,
  "Le CDI est le contrat de droit commun, conclu sans durée déterminée."),
 ("Un CDD peut-il être utilisé pour remplacer une salariée en congé maternité ?", ["Oui, c'est un motif prévu", "Non, jamais", "Oui, sans limite de durée", "Uniquement en CDI"], 0,
  "Le remplacement d'un salarié absent, notamment en congé maternité, est un motif autorisé de CDD."),
 ("Quelle est la durée légale hebdomadaire du travail ?", ["35 heures", "39 heures", "40 heures", "32 heures"], 0,
  "La durée légale est de 35 heures par semaine ; au-delà, les heures supplémentaires sont majorées ou compensées."),
 ("Que garantit le principe « à travail égal, salaire égal » ?", ["Une rémunération identique sans exceptions", "Une égalité de traitement pour un travail de valeur égale", "Le salaire le plus haut", "Une prime automatique"], 1,
  "Il interdit les écarts de rémunération non justifiés entre salariés effectuant un travail de valeur égale."),
 ("Quelle est la première étape d'un licenciement individuel ?", ["La notification écrite", "La convocation à l'entretien préalable", "Le préavis", "Le solde de tout compte"], 1,
  "Le salarié doit d'abord être convoqué à un entretien préalable avant toute notification de licenciement."),
 ("Qu'est-ce que le DUERP ?", ["Un document d'évaluation des risques professionnels", "Un contrat de vente", "Une facture", "Un bulletin de paie"], 0,
  "Le document unique d'évaluation des risques professionnels recense et évalue les risques auxquels les salariés sont exposés."),
 ("Que se passe-t-il en cas de licenciement sans cause réelle et sérieuse ?", ["Rien", "Des dommages-intérêts peuvent être dus", "Le contrat continue automatiquement", "Une amende pour le salarié"], 1,
  "Un licenciement dépourvu de cause réelle et sérieuse peut donner lieu à des dommages-intérêts."),
 ("Expliquer la différence entre licenciement et rupture conventionnelle.",
  "Le licenciement est une rupture décidée unilatéralement par l'employeur, qui doit respecter une procédure et justifier d'une cause réelle et sérieuse. La rupture conventionnelle est un accord entre l'employeur et le salarié sur le principe et les conditions du départ ; elle est homologuée par l'administration et ouvre droit aux indemnités légales. La première est un acte unilatéral encadré, la seconde un accord négocié.",
  "On oppose une décision unilatérale à un départ consenti et homologué."),
 ("Un commercial travaille 42 heures une semaine. Calculer les heures supplémentaires et expliquer les obligations de l'employeur.",
  "Les heures supplémentaires sont de 42 − 35 = 7 heures. L'employeur doit les rémunérer avec la majoration légale de 25 % pour les premières heures (50 % au-delà d'un certain seuil selon la convention collective) ou accorder un repos compensateur équivalent. Il doit les déclarer et respecter les durées maximales de travail et de repos quotidien. Le contrat et le bulletin de salaire doivent refléter ces heures.",
  "On calcule l'écart avec 35 heures, puis on rappelle majoration, compensation et traçabilité."),
),
(
 "L'idée en une phrase|Manager une équipe commerciale, c'est aussi appliquer le droit du travail : contrat, temps, salaire et procédure de départ encadrés.",
 "Contrat de travail|Prestation + rémunération + subordination|35 h, SMIC, congés et sécurité : socle légal et conventionnel.",
 "[['Thème', 'Règle', 'Risque'], ['CDD', 'Motif prevu par la loi', 'Requalification en CDI'], ['Temps de travail', '35 heures legales', 'Heures non payees'], ['Salaire', 'SMIC et convention', 'Inégalite de traitement'], ['Licenciement', 'Entretien puis notification', 'Dommages-interets']]",
 "['Verifier le type de contrat', 'Suivre les heures et les repos', 'Appliquer la convention collective', 'Conduire l entretien selon la procedure', 'Documenter les decisions']",
 "['Rédiger le contrat et la période d essai', 'Organiser le temps de travail', 'Fixer la rémunération selon la grille', 'Assurer la sécurité et la formation', 'Respecter la procédure de rupture']",
 "['Utiliser un CDD sans motif legal', 'Oublier la majoration des heures supplémentaires', 'Fixer un salaire sous le SMIC', 'Licencier sans entretien préalable', 'Ignorer les risques professionnels']",
 "['42 h − 35 h = 7 h supplementaires', 'Majoration legal de 25 %', 'CDD remplacement = motif autorise', 'Preavis et entretien obligatoires', 'DUERP mis a jour chaque annee']",
), st=("Le contrat de travail", "Manager dans la légalité", "Pratique conforme / risquée"))

# ============================================================ DR5
add("DR5", "Responsabilité et protection des données", "Droit", ["BTS2"],
[
 "La responsabilité civile oblige une personne à réparer le dommage causé à autrui, sur le fondement contractuel ou délictuel.",
 "En matière délictuelle, la responsabilité suppose une faute, un dommage et un lien de causalité ; certains régimes spéciaux reposent sur la seule garde de la chose.",
 "La responsabilité du fait des produits défectueux permet d'indemniser le consommateur sans prouver la faute du producteur, mais obligation de prouver le défaut et le dommage.",
 "Le RGPD (règlement UE 2016/679) et la loi Informatique et Libertés encadrent les traitements de données personnelles en France.", "Les données sensibles (santé, opinions, origine, religion, données biométriques) bénéficient d'un régime renforcé et sont en principe interdites de traitement, sauf exception.",
 "Le responsable de traitement doit mettre en oeuvre des mesures techniques et organisationnelles appropriées : chiffrement, contrôle des accès, journalisation et sauvegardes.",
 "Les sous-traitants qui traitent des données pour le compte de l'entreprise doivent être liés par un contrat précisant objet, durée, finalité et obligations de sécurité.",
 "Les sanctions administratives peuvent atteindre 20 millions d'euros ou 4 % du chiffre d'affaires annuel mondial pour les violations les plus graves.",
 "Le délégué à la protection des données conseille l'organisation, surveille la conformité et sert d'interlocuteur avec l'autorité de contrôle.",
 "En cas de violation de données, le responsable doit documenter l'incident et notifier la CNIL dans les 72 heures si un risque existe pour les personnes.",
 "En BTS NDRC, le commercial engage la responsabilité de l'entreprise par ses propos et ses traitements de données : exactitude des informations, réserves sur les promesses et respect des droits.",
 "Exemple : une base de prospects conservée trois ans sans justification ni information expose l'entreprise à une mise en demeure et à une amende.",
],
Q(
 ("Quels éléments caractérisent la responsabilité délictuelle ?", ["Faute, dommage, lien de causalité", "Contrat, prix, livraison", "Client, marge, stock", "Salarie, salaire, primes"], 0,
  "La responsabilité délictuelle repose sur une faute, un dommage et un lien de causalité entre eux."),
 ("Que doit prouver un consommateur dans une action pour produit défectueux ?", ["La faute du producteur", "Le défaut, le dommage et le lien", "Le prix du produit", "La publicité vue"], 1,
  "Ce régime dispense de prouver la faute mais exige de caractériser le défaut, le dommage et le lien de causalité."),
 ("Quelle donnée est sensible au sens du RGPD ?", ["Une adresse e-mail professionnelle", "Une donnée de santé", "Un code postal", "Un numéro de commande"], 1,
  "Les données de santé, d'opinion, d'origine ou biométriques sont sensibles et bénéficient d'un régime renforcé."),
 ("Quelle mesure technique relève de la sécurité des traitements ?", ["Le chiffrement et le contrôle des accès", "La publicité", "Le prix bas", "Le logo"], 0,
  "Le RGPD impose des mesures appropriées comme le chiffrement, la journalisation et la limitation des accès."),
 ("Quel plafond de sanction administrative prévoit le RGPD ?", ["20 000 € ou 1 % du CA", "20 M€ ou 4 % du CA mondial", "500 €", "Aucune limite"], 1,
  "Les violations les plus graves peuvent être sanctionnées jusqu'à 20 millions d'euros ou 4 % du chiffre d'affaires annuel mondial."),
 ("Que doit contenir un contrat de sous-traitance de données ?", ["Le prix uniquement", "L'objet, la durée, la finalité et les obligations de sécurité", "Le nombre de salariés", "La couleur du logo"], 1,
  "Le contrat doit préciser l'objet, la durée, la nature et la finalité du traitement, les types de données et les obligations du sous-traitant."),
 ("Quel est le délai de notification d'une violation à la CNIL ?", ["24 heures", "72 heures", "8 jours", "30 jours"], 1,
  "La notification à l'autorité de contrôle doit intervenir dans les 72 heures lorsqu'il existe un risque pour les personnes."),
 ("Quel est le rôle du DPO ?", ["Vendre les données", "Conseiller et contrôler la conformité", "Remplacer le service juridique", "Fixer les prix"], 1,
  "Le délégué à la protection des données conseille, surveille la conformité et fait le lien avec l'autorité de contrôle."),
 ("Distinguer responsabilité contractuelle et responsabilité délictuelle.",
  "La responsabilité contractuelle s'applique entre parties liées par un contrat : le créancier doit prouver l'inexécution d'une obligation contractuelle. La responsabilité délictuelle s'applique en l'absence de contrat, lorsque la faute de l'auteur cause un dommage à autrui ; elle repose sur faute, dommage et lien de causalité. Le concours des deux responsabilités est exclu entre les mêmes parties pour le même dommage.",
  "On oppose l'inexécution d'un contrat à la faute extracontractuelle."),
 ("Une base de 10 000 prospects est conservée depuis trois ans sans justification ni information des personnes. Analyser le risque.",
  "La conservation illimitée viole le principe de limitation de la conservation des données et, si les personnes n'ont pas été informées, le principe de transparence. Les données sont traitées sans base légale vérifiable pour une prospection ancienne. L'entreprise s'expose à une mise en demeure de la CNIL, à une amende pouvant atteindre 20 M€ ou 4 % du chiffre d'affaires mondial, et à des actions d'exercice des droits (effacement, opposition). La mise en conformité suppose de documenter la finalité, d'informer les personnes, de purger les données obsolètes et de tracer la décision.",
  "On identifie les principes violés, les sanctions encourues et les mesures de remise en conformité."),
),
(
 "L'idée en une phrase|La responsabilité ne s'arrête pas à la vente : elle couvre la qualité de l'information donnée et la garde des données reçues.",
 "Responsabilité et données|Faute + dommage + lien · RGPD : finalité, minimisation, sécurité, droits|Sanction jusqu'à 20 M€ ou 4 % du CA mondial.",
 "[['Domaine', 'Règle clé', 'Risque'], ['Responsabilité', 'Faute, dommage, lien', 'Dommages-intérêts'], ['Produit', 'Defaut sans faute a prouver', 'Rappel et indemnisation'], ['Donnees', 'Finalite et conservation limitee', 'Amende RGPD'], ['Sous-traitance', 'Contrat ecrit obligatoire', 'Responsabilité solidaire']]",
 "['Identifier le fondement de la responsabilité', 'Verifier les obligations de securite', 'Documenter les traitements', 'Traiter les droits des personnes', 'Notifier toute violation sous 72 h']",
 "['Cartographier les donnees collectees', 'Etablir les finalites et bases legales', 'Signer les contrats de sous-traitance', 'Former les equipes commerciales', 'Tester la procedure de notification']",
 "['Conserver une base sans limite de duree', 'Traiter des donnees sensibles sans exception', 'Confier des donnees sans contrat', 'Ignorer une demande d effacement', 'Attendre plus de 72 h pour notifier']",
 "['10 000 prospects × 3 ans sans justification', 'Sanction maximale : 20 M€ ou 4 % du CA', 'Notification CNIL : 72 h', 'Donnees sensibles : regime renforce', 'Contrat de sous-traitance ecrit']",
), st=("Fondements de la responsabilité", "Se conformer au RGPD", "Conformité / sanction"))

# ============================================================ EC1
add("EC1", "Marchés, offre et demande", "Économie", ["BTS1"],
[
 "Un marché est le lieu, physique ou virtuel, où se rencontrent une offre et une demande pour un bien ou un service, et où se forment un prix et une quantité échangée.",
 "La loi de la demande énonce que, toutes choses égales par ailleurs, une baisse de prix entraîne une hausse de la quantité demandée.",
 "La loi de l'offre énonce qu'une hausse de prix incite les producteurs à offrir une quantité plus grande, car la marge potentielle augmente.",
 "Le prix d'équilibre est celui pour lequel la quantité offerte égale la quantité demandée ; il n'y a ni pénurie ni excédent durable.",
 "Une hausse de la demande, à offre constante, fait monter le prix et la quantité échangée ; c'est un déplacement de la courbe de demande.",
 "Une variation de prix provoque un mouvement le long de la courbe, tandis qu'une modification d'un autre facteur (revenu, goût, prix concurrent) déplace la courbe.",
 "L'élasticité-prix de la demande mesure la sensibilité de la quantité demandée à une variation de prix : demande rigide si la valeur absolue est inférieure à 1, élastique si elle est supérieure.",
 "Une demande rigide permet à l'entreprise d'augmenter le prix avec peu de perte de volume ; une demande élastique impose la prudence.",
 "Les biens de première nécessité ont généralement une demande peu élastique ; les biens de luxe ou facilement substituables sont plus élastiques.",
 "La concurrence, le nombre d'acteurs et la différenciation déterminent la structure du marché : concurrence parfaite, monopole, oligopole ou concurrence monopolistique.",
 "En BTS NDRC, comprendre l'élasticité aide à décider d'une remise, d'une hausse de prix ou d'une campagne de fidélisation.",
 "Exemple : si une hausse de prix de 10 % réduit les ventes de 4 %, l'élasticité vaut −0,4 : la demande est rigide et le chiffre progresse d'environ 5,6 %.",
],
Q(
 ("Que se passe-t-il lorsque le prix augmente, toutes choses égales par ailleurs ?", ["La demande augmente", "La demande diminue", "L'offre diminue", "Rien ne change"], 1,
  "Selon la loi de la demande, une hausse de prix réduit la quantité demandée, à facteurs constants."),
 ("Quel est le prix d'équilibre ?", ["Le prix le plus bas possible", "Le prix où offre et demande s'égalisent", "Le prix conseillé par l'État", "Le prix de revient"], 1,
  "À l'équilibre, la quantité offerte est égale à la quantité demandée : le marché est fluide."),
 ("Quelle différence y a-t-il entre mouvement et déplacement de la courbe ?", ["Aucune différence", "Le prix provoque un mouvement, un autre facteur déplace la courbe", "Le déplacement est toujours vers le bas", "Le mouvement change l'offre"], 1,
  "Une variation de prix fait glisser le long de la courbe ; un changement de revenu ou de goût décale la courbe entière."),
 ("Une demande est élastique si…", ["L'élasticité est inférieure à 1", "L'élasticité est supérieure à 1 en valeur absolue", "Le prix est fixe", "L'offre est nulle"], 1,
  "Une demande élastique réagit fortement au prix : la variation de quantité est proportionnellement plus grande que celle du prix."),
 ("Quel bien a généralement une demande rigide ?", ["Un bien de luxe", "Un médicament nécessaire", "Une marque facilement substituable", "Un produit de mode"], 1,
  "Un produit nécessaire ou sans substitut proche est peu sensible au prix : sa demande est rigide."),
 ("Que se passe-t-il si la demande augmente alors que l'offre reste constante ?", ["Le prix et la quantité baissent", "Le prix et la quantité augmentent", "Le prix baisse et la quantité augmente", "Aucun changement"], 1,
  "Le déplacement de la demande vers la droite élève le prix d'équilibre et la quantité échangée."),
 ("Combien d'acteurs caractérise un oligopole ?", ["Un seul", "Quelques-uns", "Un très grand nombre", "Zéro"], 1,
  "L'oligopole est une structure de marché dominée par un petit nombre de producteurs."),
 ("Pourquoi l'élasticité est-elle utile au commercial ?", ["Elle fixe le salaire", "Elle aide à décider d'une hausse ou baisse de prix", "Elle supprime la concurrence", "Elle remplace le contrat"], 1,
  "Connaître la sensibilité de la demande au prix permet d'anticiper l'effet d'une remise ou d'une hausse sur le chiffre."),
 ("Distinguer variation de la demande et déplacement de la courbe de demande.",
  "Une variation de la quantité demandée liée à un changement de prix est un mouvement le long de la courbe. Un déplacement de la courbe intervient lorsqu'un facteur autre que le prix du bien change : revenu des consommateurs, goûts, prix des produits liés, nombre d'acheteurs, attentes. Dans le premier cas, la relation prix-quantité reste la même ; dans le second, elle change à chaque prix.",
  "On oppose le mouvement sur la courbe au déplacement de la courbe entière."),
 ("Une hausse de prix de 10 % fait baisser les ventes de 4 %. Calculer l'élasticité et l'effet approximatif sur le chiffre d'affaires.",
  "Élasticité = −4 % / +10 % = −0,4 ; en valeur absolue elle est inférieure à 1, donc la demande est rigide. Le chiffre d'affaires, prix × quantité, devient 1,10 × 0,96 = 1,056, soit une hausse d'environ 5,6 %. Augmenter le prix accroît donc le chiffre dans ce cas, à condition que la réaction des concurrents et de la fidélité reste limitée.",
  "On calcule l'élasticité, on interprète sa valeur, puis on multiplie prix et quantité pour obtenir l'effet sur le chiffre."),
),
(
 "L'idée en une phrase|Le prix est le point de rencontre de l'offre et de la demande : savoir si les clients sont sensibles au prix décide de la stratégie commerciale.",
 "Équilibre et élasticité|Prix d'équilibre : offre = demande · élasticité = ΔQ% / ΔP%|Une demande rigide supporte mieux une hausse de prix.",
 "[['Situation', 'Effet sur le prix', 'Effet sur la quantité'], ['Demande en hausse', 'Hausse', 'Hausse'], ['Offre en hausse', 'Baisse', 'Hausse'], ['Hausse de prix', 'Mouvement sur la courbe', 'Quantité demandée baisse'], ['Revenu en hausse', 'Courbe déplacée', 'Demande plus forte']]",
 "['Identifier le marche et les acteurs', 'Observer offre et demande', 'Repérer le prix d equilibre', 'Estimer l elasticite', 'Decider de la strategie de prix']",
 "['Définir le produit et le marche pertinent', 'Mesurer les quantités aux differents prix', 'Repérer les facteurs qui decalent la courbe', 'Calculer l elasticite', 'Tester la decision sur une periode courte']",
 "['Confondre mouvement et deplacement', 'Croire qu une hausse de prix augmente toujours le chiffre', 'Oublier les substituts', 'Ignorer la reaction des concurrents', 'Raisonner sans donnees de vente']",
 "['+ 10 % de prix, − 4 % de quantite', 'Elasticite = −0,4 (demande rigide)', 'Chiffre = 1,10 × 0,96 = 1,056', 'Soit + 5,6 % de chiffre', 'Oligopole = quelques acteurs']",
), st=("Offre et demande", "Décider du prix", "Marché équilibré / tendu"))

# ============================================================ EC2
add("EC2", "L'entreprise et son environnement", "Économie", ["BTS1"],
[
 "L'entreprise est une organisation qui combine des facteurs de production (travail, capital, matières) pour produire des biens ou services destinés à un marché.",
 "Son objectif principal est la création de valeur : le chiffre d'affaires doit couvrir les coûts et dégager une marge pour investir et rémunérer les parties prenantes.",
 "Le compte de résultat retrace les produits et les charges d'une période et fait apparaître le résultat ; le bilan décrit l'actif et le passif à une date donnée.",
 "Le seuil de rentabilité est le niveau d'activité pour lequel le résultat est nul ; il dépend des charges fixes et de la marge sur coût variable.",
 "Les parties prenantes sont les salariés, les clients, les fournisseurs, les actionnaires, les pouvoirs publics et la collectivité.",
 "L'environnement macroéconomique comprend la croissance, l'inflation, le chômage et les politiques monétaire et budgétaire.",
 "L'environnement microéconomique comprend les clients, les concurrents, les fournisseurs et les intermédiaires ; c'est le niveau où se joue la stratégie commerciale.",
 "Le PESTEL structure l'analyse externe : Politique, Économique, Social, Technologique, Écologique et Légal.",
 "Les cinq forces de Porter analysent la rivalité entre concurrents, le pouvoir de négociation des clients et des fournisseurs, les menaces de nouveaux entrants et de produits de substitution.",
 "La chaîne de valeur distingue les activités qui créent de la valeur (production, marketing, logistique, service) et les activités de soutien.",
 "En BTS NDRC, le commercial situe son action dans cette chaîne : il contribue directement à la création de valeur par la vente et la relation client.",
 "Exemple : une hausse du coût des matières de 10 % réduit la marge si l'entreprise ne peut pas répercuter cette hausse sur ses prix de vente.",
],
Q(
 ("Quel document retrace produits et charges d'une période ?", ["Le bilan", "Le compte de résultat", "Le plan comptable", "Le procès-verbal"], 1,
  "Le compte de résultat présente les produits et charges de l'exercice et calcule le résultat ; le bilan donne une photographie à une date."),
 ("Que mesure le seuil de rentabilité ?", ["Le chiffre maximal", "Le niveau où le résultat est nul", "La marge nette", "Le stock final"], 1,
  "Au seuil de rentabilité, la marge sur coût variable couvre exactement les charges fixes."),
 ("Parmi ces acteurs, lequel est une partie prenante interne ?", ["Le client", "Le salarié", "Le fournisseur", "La concurrence"], 1,
  "Les salariés sont des parties prenantes internes ; clients, fournisseurs et concurrents appartiennent à l'environnement externe."),
 ("Quel facteur relève de l'environnement macroéconomique ?", ["Le prix du concurrent", "L'inflation", "Le goût du client", "La force de vente"], 1,
  "L'inflation est une variable macroéconomique ; les autres exemples relèvent du niveau microéconomique ou interne."),
 ("Que signifie la lettre T du PESTEL ?", ["Technologique", "Territorial", "Tarifaire", "Temporel"], 0,
  "PESTEL : Politique, Économique, Social, Technologique, Écologique, Légal."),
 ("Quel modèle analyse la rivalité et le pouvoir de négociation ?", ["Les cinq forces de Porter", "Le SWOT", "La courbe de demande", "Le bilan"], 0,
  "Les cinq forces de Porter结构 analysent la concurrence et les rapports de force dans un secteur."),
 ("Que désigne la chaîne de valeur ?", ["Une liste de prix", "Les activités qui créent de la valeur", "Un contrat de travail", "Le bilan comptable"], 1,
  "La chaîne de valeur identifie les activités qui génèrent de la valeur et celles qui les soutiennent."),
 ("Comment une hausse des coûts de 10 % affecte-t-elle la marge sans hausse de prix ?", ["La marge augmente", "La marge diminue", "La marge reste identique", "Le chiffre double"], 1,
  "À prix de vente constant, une hausse de coût réduit directement la marge unitaire."),
 ("Distinguer environnement microéconomique et macroéconomique.",
  "L'environnement microéconomique est constitué des acteurs avec lesquels l'entreprise interagit directement : clients, concurrents, fournisseurs, distributeurs. L'environnement macroéconomique désigne les grandes variables qui affectent toutes les entreprises : croissance, inflation, chômage, taux d'intérêt, politique publique. Le premier est proche et spécifique à l'entreprise, le second est global et la concerne indirectement.",
  "On oppose les relations directes de l'entreprise aux grandes tendances qui l'enveloppent."),
 ("Une entreprise vend 50 € HT un produit coûtant 30 €. Les matières augmentent de 10 %. Calculer la nouvelle marge et la hausse de prix nécessaire pour la maintenir.",
  "Marge initiale = 50 − 30 = 20 €. Le coût passe à 30 × 1,10 = 33 €, la nouvelle marge est de 17 €, soit une baisse de 3 € (15 %). Pour maintenir une marge de 20 €, le prix doit passer à 33 + 20 = 53 €, soit une hausse de 3 € ou 6 % du prix initial. L'entreprise doit vérifier si le marché accepte cette hausse sans perte de volume.",
  "On calcule la marge initiale, le nouveau coût et le prix nécessaire, puis on évoque l'acceptabilité commerciale."),
),
(
 "L'idée en une phrase|L'entreprise crée de la valeur en combinant ses ressources et en s'adaptant à un environnement qu'elle doit analyser en permanence.",
 "Chaîne de valeur|Production · marketing · logistique · service = création de valeur|PESTEL et cinq forces structurent l'environnement.",
 "[['Niveau', 'Acteurs ou variables', 'Outil'], ['Micro', 'Clients, concurrents, fournisseurs', 'Cinq forces'], ['Macro', 'Inflation, croissance, chomage', 'PESTEL'], ['Interne', 'Salaries, capital, procédés', 'Chaine de valeur']]",
 "['Définir le marché pertinent', 'Analyser les acteurs directs', 'Examiner les variables macro', 'Repérer les activités créatrices de valeur', 'Décider des priorités commerciales']",
 "['Cartographier les parties prenantes', 'Réaliser un PESTEL', 'Appliquer les cinq forces', 'Analyser la chaine de valeur', 'Calculer le seuil de rentabilité']",
 "['Confondre micro et macro', 'Ignorer les parties prenantes', 'Réaliser un PESTEL sans donnée', 'Vendre sans couvrir les charges fixes', 'Supposer que la valeur est seulement financière']",
 "['Prix 50 € − coût 30 € = 20 €', 'Coût + 10 % = 33 €', 'Marge réduite à 17 € (− 15 %)', 'Prix maintenu à 53 € pour 20 € de marge', 'Hausse de prix nécessaire : 6 %']",
), st=("L'entreprise", "Analyser l'environnement", "Valeur créée / détruite"))

# ============================================================ EC3
add("EC3", "Conjoncture et croissance économique", "Économie", ["BTS2"],
[
 "La croissance économique est l'augmentation durable de la production de biens et de services d'un pays, mesurée par l'évolution du PIB.",
 "Le PIB (produit intérieur brut) mesure la valeur ajoutée créée sur le territoire national au cours d'une période, généralement un an ou un trimestre.",
 "On distingue la croissance conjoncturelle, variation à court terme, de la croissance potentielle, capacité de production de long terme de l'économie.",
 "Le cycle économique alterne phases d'expansion (production et emploi en hausse) et phases de récession (baisse d'activité et hausse du chômage).",
 "La demande agrégée est la somme de la consommation, de l'investissement, des dépenses publiques et des exportations nettes ; elle tire l'activité à court terme.",
 "L'offre agrégée représente la production totale que les entreprises sont disposées à fournir à différents niveaux de prix.",
 "L'inflation est une hausse généralisée et durable des prix ; elle érode le pouvoir d'achat si les salaires ne suivent pas.",
 "Le chômage mesure la part de la population active qui recherche un emploi et n'en a pas ; il existe un chômage structurel même en pleine activité.",
 "La politique monétaire, menée par la BCE, agit sur les taux d'intérêt et la masse monétaire pour stabiliser les prix.",
 "La politique budgétaire, menée par l'État, agit par les dépenses publiques et la fiscalité pour soutenir ou ralentir l'activité.",
 "Pour une entreprise commerciale, la conjoncture modifie le pouvoir d'achat des clients, le coût du crédit et les perspectives de vente : elle doit adapter ses prévisions et son stock.",
 "Exemple : si le PIB progresse de 1,2 % et l'inflation de 2 %, la croissance en volume est d'environ 1,2 % et la hausse des prix réduit le pouvoir d'achat réel des revenus qui stagnent.",
],
Q(
 ("Comment mesure-t-on la croissance économique ?", ["Par l'évolution du PIB", "Par le nombre d'entreprises", "Par le prix d'un produit", "Par le taux de marge"], 0,
  "La croissance est mesurée par la variation du PIB, en volume de préférence pour éliminer l'effet des prix."),
 ("Que désigne le PIB ?", ["La valeur ajoutée créée sur le territoire national", "Le chiffre d'une entreprise", "Le budget de l'État", "La masse monétaire"], 0,
  "Le PIB additionne les valeurs ajoutées des unités productives résidentes, augmentées des taxes moins les subventions."),
 ("Quelle phase du cycle économique est marquée par la baisse de l'activité ?", ["L'expansion", "La récession", "La reprise", "Le pic"], 1,
  "La récession correspond à une baisse de la production et souvent à une hausse du chômage."),
 ("Quelle composante ne fait pas partie de la demande agrégée ?", ["La consommation", "L'investissement", "Les exportations nettes", "Le stock de capital inutilisé"], 3,
  "La demande agrégée comprend consommation, investissement, dépenses publiques et exportations nettes."),
 ("Quel est l'effet d'une inflation non compensée par les salaires ?", ["Une hausse du pouvoir d'achat", "Une baisse du pouvoir d'achat", "Une baisse des prix", "Une hausse de l'emploi automatique"], 1,
  "Si les prix montent plus vite que les revenus, les ménages peuvent acheter moins de biens et services."),
 ("Quelle institution mène la politique monétaire dans la zone euro ?", ["La BCE", "L'Autorité de la concurrence", "La CNIL", "Le ministère du Travail"], 0,
  "La Banque centrale européenne pilote les taux et la masse monétaire pour la stabilité des prix."),
 ("Quel outil relève de la politique budgétaire ?", ["Le taux directeur", "La fiscalité et les dépenses publiques", "Le taux de change", "La masse monétaire"], 1,
  "La politique budgétaire utilise le budget de l'État : recettes fiscales et dépenses."),
 ("Pourquoi le chômage existe-t-il même en phase d'expansion ?", ["Il est toujours nul", "Il existe un chômage structurel et frictionnel", "Il augmente mécaniquement", "Il dépend uniquement de l'inflation"], 1,
  "Le chômage frictionnel (recherche d'emploi) et structurel (inadéquation des compétences) subsistent même lorsque l'activité est forte."),
 ("Distinguer croissance conjoncturelle et croissance potentielle.",
  "La croissance conjoncturelle est la variation à court terme du PIB, liée au cycle et à l'utilisation des capacités de production existantes. La croissance potentielle est le rythme que l'économie peut soutenir à long terme sans générer d'inflation, compte tenu de ses ressources en travail, en capital et de sa productivité. Une croissance conjoncturelle supérieure au potentiel crée des tensions sur les prix et le marché du travail.",
  "On oppose le court terme cyclique à la capacité durable de production."),
 ("Le PIB progresse de 1,2 % et les prix de 2 %. Que peut-on dire du pouvoir d'achat d'un revenu qui stagne ?",
  "La croissance en volume est de 1,2 %, mais l'inflation de 2 % est supérieure à l'augmentation du revenu, qui est nulle. Le pouvoir d'achat de ce revenu baisse d'environ 2 % : avec le même montant nominal, le ménage achète moins de biens et services. Pour une entreprise, cela signifie une pression sur la demande et sur les prix de vente ; elle peut répondre par une offre moins chère, des promotions ciblées ou une valeur perçue renforcée.",
  "On compare inflation et hausse du revenu, puis on en déduit l'effet sur le pouvoir d'achat et la stratégie commerciale."),
),
(
 "L'idée en une phrase|La conjoncture change le pouvoir d'achat des clients : le commercial doit lire les grands agrégats pour ajuster prix, stock et argumentaire.",
 "PIB et cycle|Croissance = Δ PIB en volume · cycle = expansion / récession|Inflation, chômage, taux et budget forment le cadre.",
 "[['Agrégat', 'Définition', 'Effet sur l'entreprise'], ['PIB', 'Production nationale', 'Demande globale'], ['Inflation', 'Hausse generale des prix', 'Pouvoir d achat'], ['Chomage', 'Recherche d emploi', 'Consommation'], ['Taux', 'Prix de l argent', 'Investissement']]",
 "['Observer les indicateurs macro', 'Evaluer l effet sur les clients', 'Ajuster les prévisions de vente', 'Adapter prix et stock', 'Suivre les résultats']",
 "['Lire les publications de l INSEE', 'Comparer PIB et inflation', 'Analyser le pouvoir d achat de la cible', 'Anticiper le coût du crédit', 'Réviser le plan commercial']",
 "['Confondre PIB nominal et PIB volume', 'Ignorer l inflation dans une prévision', 'Croire que le chômage est toujours nul en expansion', 'Subir la conjoncture sans adaptation', 'Raisonner sur des données anciennes']",
 "['PIB + 1,2 %, prix + 2 %', 'Revenu stagnent → pouvoir d achat − 2 %', 'Demande agrégée = C + I + G + X − M', 'BCE : stabilité des prix', 'Budgétaire : dépenses et fiscalité']",
), st=("Les agrégats", "Lire la conjoncture", "Conjoncture favorable / tendue"))

# ============================================================ EC4
add("EC4", "Commerce international et mondialisation", "Économie", ["BTS2"],
[
 "Le commerce international désigne les échanges de biens et de services entre pays ; il permet de spécialiser les économies et d'élargir les marchés.",
 "La spécialisation repose sur l'avantage comparatif : un pays a intérêt à produire ce qu'il peut fabriquer à moindre coût relatif, même s'il n'est le meilleur nulle part.",
 "Les exportations sont des ventes à l'étranger et les importations des achats en provenance de l'étranger ; la balance commerciale est leur différence.",
 "Un déficit commercial signifie que les importations dépassent les exportations ; un excédent signifie l'inverse.",
 "Le taux de change est le prix d'une monnaie en une autre monnaie : il influence directement le prix des importations et des exportations.",
 "Une appréciation de l'euro rend les importations moins chères et les exportations plus chères pour les acheteurs étrangers.",
 "Les barrières commerciales prennent la forme de droits de douane, de quotas ou de réglementations techniques ; elles protègent des secteurs mais renchérissent les imports.",
 "Le marché unique européen supprime les barrières tarifaires entre États membres et harmonise une partie des règles.",
 "Les chaînes de valeur mondiales fragmentent la production entre plusieurs pays : un produit peut être conçu, fabriqué et assemblé sur trois continents.",
 "La mondialisation accroît la concurrence et les opportunités de marché, mais elle expose les entreprises à des risques logistiques, financiers et géopolitiques.",
 "En BTS NDRC, un commercial peut être amené à prospecter à l'export, à négocier en langue étrangère et à maîtriser les Incoterms et les délais.",
 "Exemple : si l'euro s'apprécie de 10 % face au dollar, une exportation facturée 100 $ ne rapporte plus que 90,9 € environ contre 100 € auparavant, à taux initial de 1.",
],
Q(
 ("Quel est l'intérêt de la spécialisation selon l'avantage comparatif ?", ["Produire absolument tout soi-même", "Produire ce que l'on fait à moindre coût relatif", "Interdire les importations", "Fixer des quotas"], 1,
  "L'avantage comparatif justifie la spécialisation dans les productions relativement les plus efficaces, même sans avantage absolu."),
 ("Comment appelle-t-on la différence entre exportations et importations ?", ["Le taux de change", "La balance commerciale", "Le PIB", "L'inflation"], 1,
  "La balance commerciale est le solde des exportations moins les importations de biens."),
 ("Quel effet a une appréciation de l'euro sur les importations ?", ["Elles deviennent plus chères", "Elles deviennent moins chères", "Elles disparaissent", "Aucun effet"], 1,
  "Une monnaie plus forte achète davantage de monnaie étrangère : les biens importés coûtent moins cher en euros."),
 ("Quel est un droit de douane ?", ["Une taxe sur les importations", "Un quota d'exportation", "Un taux d'intérêt", "Un salaire minimum"], 0,
  "Le droit de douane est une taxe perçue à l'entrée d'un produit sur le territoire douanier."),
 ("Quel bloc supprime les barrières tarifaires entre ses États membres ?", ["Le marché unique européen", "L'ONU", "L'OCDE", "Le FMI"], 0,
  "Le marché unique européen assure la libre circulation des marchandises entre États membres, sous réserve de règles communes."),
 ("Qu'est-ce qu'une chaîne de valeur mondiale ?", ["Une chaîne de magasins", "Une production répartie entre plusieurs pays", "Un contrat de travail", "Une facture en dollars"], 1,
  "La chaîne de valeur mondiale fragmente la conception, la fabrication et l'assemblage entre different pays."),
 ("Quel risque découle d'une forte dépendance aux fournisseurs étrangers ?", ["Une baisse de la concurrence", "Une vulnérabilité logistique et géopolitique", "Une hausse automatique de la marge", "Une disparition du taux de change"], 1,
  "Les chaînes longues exposent aux retards, aux tensions commerciales et aux variations de change."),
 ("Quel outil contractuel précise les responsabilités dans une vente internationale ?", ["Les Incoterms", "Le SMIC", "Le code de la route", "Le plan comptable"], 0,
  "Les Incoterms de la Chambre de commerce internationale définissent les obligations de chacun sur le transport, les risques et les frais."),
 ("Expliquer l'effet d'une variation de change sur les exportations d'une entreprise.",
  "Si l'euro s'apprécie, un prix facturé en euros devient plus cher en monnaie étrangère pour l'acheteur étranger, ce qui peut réduire les commandes ; si l'euro se déprécie, le même produit devient plus compétitif à l'étranger, mais les importations coûtent plus cher en euros. L'entreprise peut protéger sa marge en négociant la monnaie de facturation, en fixant des clauses d'ajustement ou en couvrant son risque de change.",
  "On relie le sens de la variation de change à la compétitivité-prix et aux moyens de couverture."),
 ("À un taux de 1 € = 1 $, une exportation est facturée 100 $. Si l'euro s'apprécie de 10 % (1 € = 1,10 $), combien d'euros l'entreprise reçoit-elle et que faire ?",
  "Avec 1 € = 1,10 $, 100 $ convertis donnent 100 / 1,10 ≈ 90,91 €, contre 100 € au taux initial : perte d'environ 9,1 % en euros. L'entreprise peut facturer en euros, réviser son prix en dollars pour refléter le nouveau change, prévoir une clause d'ajustement ou couvrir le risque à terme. Elle doit aussi vérifier si le marché accepte une hausse de prix avant de décider.",
  "On convertit au nouveau taux, on calcule la perte, puis on propose des moyens de gestion du risque."),
),
(
 "L'idée en une phrase|Le commerce international élargit les marchés mais introduit le change, les barrières et la dépendance : le prix n'est jamais le seul risque.",
 "Solde et change|Balance = exportations − importations · euro fort = imports moins chers, exports plus chers|Incoterms et clauses de change sécurisent la vente.",
 "[['Variable', 'Mouvement', 'Effet'], ['Euro fort', 'Appréciation', 'Imports moins chers, exports plus chers'], ['Droits de douane', 'Hausse', 'Importations renchéries'], ['Chaîne longue', 'Fragmentation', 'Risque logistique'], ['Incoterms', 'Clauses', 'Responsabilités claires']]",
 "['Choisir le marche et la monnaie de facturation', 'Verifier les barrieres et normes', 'Fixer les Incoterms', 'Estimer le risque de change', 'Suivre la balance et les delais']",
 "['Evaluer l avantage comparatif', 'Analyser la balance commerciale', 'Surveiller le taux de change', 'Negocier monnaie et Incoterms', 'Diversifier les fournisseurs']",
 "['Facturer sans tenir compte du change', 'Croire qu un euro fort aide les exportateurs', 'Ignorer les droits de douane', 'Ne pas ecrire les Incoterms', 'Dependre d un seul fournisseur etranger']",
 "['100 $ / 1,10 = 90,91 €', 'Perte de change ≈ 9,1 %', 'Balance commerciale = X − M', 'Incoterms = responsabilites transport et risques', 'Marche unique = libre circulation']",
), st=("Échanges internationaux", "Sécuriser l'export", "Marché ouvert / risqué"))

# ============================================================ EC5
add("EC5", "Économie numérique et plateformes", "Économie", ["BTS2"],
[
 "L'économie numérique désigne l'ensemble des activités de production, de distribution et de consommation fondées sur les technologies de l'information.",
 "Une plateforme est une intermédiaire numérique qui met en relation deux ou plusieurs groupes d'utilisateurs, par exemple acheteurs et vendeurs.",
 "Le modèle économique d'une plateforme repose souvent sur les effets de réseau : sa valeur augmente avec le nombre de participants.",
 "La monétisation peut provenir de commissions sur les transactions, de la publicité, d'abonnements ou de la vente de données d'usage dans un cadre légal.",
 "Le prix affiché à l'utilisateur peut être zéro : le service est financé par une autre face du marché, souvent la publicité.",
 "Les与市场 bilatéraux nécessitent une tarification équilibrée entre les deux groupes : subventionner un côté permet d'attirer l'autre.",
 "Les données massives (big data) et les algorithmes permettent de personnaliser l'offre, mais posent des questions de confidentialité et de biais.",
 "Les plateformes dominantes peuvent concentrer le pouvoir de marché et soulever des enjeux de concurrence, de fiscalité et de souveraineté.",
 "Le travail de plateforme (livraison, covoiturage) s'est développé avec des statuts juridiques variables et des débats sur la protection des travailleurs.",
 "La valeur d'une entreprise numérique tient souvent à ses actifs immatériels : code, données, marque et communauté d'utilisateurs.",
 "En BTS NDRC, le commercial évolue dans cet environnement : il doit comprendre le rôle des plateformes pour conseiller ses clients et choisir ses canaux.",
 "Exemple : une marketplace prélève 12 % de commission sur une vente de 80 €, soit 9,60 € ; le vendeur doit intégrer ce coût dans sa marge.",
],
Q(
 ("Qu'est-ce qu'une plateforme numérique ?", ["Un simple site de présentation", "Un intermédiaire qui met en relation plusieurs groupes d'utilisateurs", "Un logiciel de comptabilité", "Un entrepôt"], 1,
  "Une plateforme organise les interactions entre groupes distincts, par exemple acheteurs et vendeurs."),
 ("Qu'est-ce qu'un effet de réseau ?", ["La hausse de valeur avec le nombre d'utilisateurs", "La baisse du prix à chaque vente", "Le vieillissement du site", "Une publicité obligatoire"], 0,
  "Un service devient plus utile à mesure que ses participants sont nombreux : c'est l'effet de réseau."),
 ("Comment une plateforme peut-elle être gratuite pour l'utilisateur ?", ["Elle est financée par la publicité ou l'autre face du marché", "Elle ne rend aucun service", "Elle est subventionnée indéfiniment par l'État", "Elle vend les données sans cadre légal"], 0,
  "Le modèle multi-faces finance le service par les autres participants, souvent les annonceurs ou les vendeurs."),
 ("Quel actif est immatériel dans une entreprise numérique ?", ["Le bâtiment", "La communauté d'utilisateurs", "Le camion de livraison", "Le stock de pièces"], 1,
  "Code, données, marque et communauté sont des actifs immatériels créateurs de valeur."),
 ("Quel risque concurrentiel pose une plateforme dominante ?", ["Une baisse de la concurrence", "Une hausse automatique de la qualité", "Une disparition des données", "Une baisse des effectifs dans tous les secteurs"], 0,
  "Une position dominante peut conduire à des pratiques anticoncurrentielles et à une concentration du pouvoir de marché."),
 ("Quel problème peuvent poser les algorithmes de recommandation ?", ["Des biais et une opacité dans les propositions", "Une absence totale de données", "Une hausse du coût de l'électricité", "Une interdiction de vendre"], 0,
  "Les algorithmes peuvent renforcer des biais et rendre les choix peu transparents pour l'utilisateur."),
 ("Comment une commission de plateforme de 12 % s'applique-t-elle à une vente de 80 € ?", ["12 €", "9,60 €", "6,40 €", "80 €"], 1,
  "12 % de 80 € = 9,60 € ; le vendeur conserve 70,40 € avant ses autres coûts."),
 ("Que doit faire un vendeur présent sur une marketplace ?", ["Intégrer la commission dans sa marge", "Ignorer la commission", "Vendre à perte systématiquement", "Supprimer les données clients"], 0,
  "La commission est un coût de canal : elle doit être intégrée au calcul de prix et de marge."),
 ("Expliquer le fonctionnement d'un marché biface et l'intérêt d'un prix zéro pour un côté.",
  "Un marché biface met en relation deux groupes dont les utilités sont liées : par exemple des lecteurs et des annonceurs, ou des acheteurs et des vendeurs. Attirer un côté augmente la valeur pour l'autre, ce qui justifie de subventionner le premier en lui offrant un service gratuit, tandis que le second paie une commission ou de la publicité. Le prix zéro n'est donc pas une absence de modèle économique mais un choix de tarification between les deux faces.",
  "On décrit l'interdépendance des deux groupes et le financement croisé."),
 ("Une marketplace prélève 12 % sur une vente de 80 € et le vendeur a un coût d'achat de 50 €. Calculer sa marge et sa part dans le prix, puis commenter.",
  "Commission = 80 × 0,12 = 9,60 €. Marge = 80 − 50 − 9,60 = 20,40 €, soit 25,5 % du prix de vente. Sans marketplace, la marge aurait été de 30 € (37,5 % du prix) : le coût du canal réduit la marge de 9,60 €. Le vendeur doit arbitrer entre le trafic apporté par la plateforme et ce coût, ou développer sa boutique propre pour les clients récurrents.",
  "On calcule commission, marge et taux, puis on compare avec une vente directe."),
),
(
 "L'idée en une phrase|Sur une plateforme, le client n'est pas toujours celui qui paie : comprendre les faces du marché est indispensable pour fixer son prix.",
 "Modèle de plateforme|Effets de réseau + faces subventionnées + commission|La donnée et l'algorithme sont des actifs immatériels.",
 "[['Élément', 'Rôle', 'Risque'], ['Réseau', 'Valeur croissante avec les utilisateurs', 'Concentration'], ['Commission', 'Revenu de la plateforme', 'Marge du vendeur réduite'], ['Algorithme', 'Personnalisation', 'Biais et opacité'], ['Données', 'Actif immatériel', 'Conformité RGPD']]",
 "['Identifier les faces du marche', 'Mesurer les effets de reseau', 'Choisir le mode de monetisation', 'Calculator la marge apres commission', 'Evaluer les risques de conformite']",
 "['Cartographier les acteurs de la plateforme', 'Analyser la structure tarifaire', 'Intégrer la commission au prix', 'Diversifier les canaux de vente', 'Surveiller la concurrence']",
 "['Croire que zéro euro signifie gratuit pour tous', 'Oublier la commission dans la marge', 'Ignorer les biais d algorithme', 'Confondre donnees et propriete privee', 'Dependre d une seule plateforme']",
 "['Commission 12 % × 80 € = 9,60 €', 'Marge = 80 − 50 − 9,60 = 20,40 €', 'Taux de marge = 25,5 %', 'Sans plateforme : 30 € soit 37,5 %', 'Coût du canal = 9,60 €']",
), st=("Fonctionnement des plateformes", "Vendre sur plateforme", "Modèle viable / fragile"))

# --- FIN BLOC ---
valider_et_ecrire(F, "btsndrc-mat-part-C.json")
