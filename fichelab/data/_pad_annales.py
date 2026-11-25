# -*- coding: utf-8 -*-
"""Complète chaque annale pour atteindre 6 questions explicites avec correction."""
import json, os, re

D = os.path.dirname(__file__)
EXTRA = {
"A0": [
("Quel apport le lexique du premier document donne-t-il à la représentation de la maison ?",
 "On relève les termes de l'abri, du calme et de la mémoire : ce lexique transforme un espace matériel en lieu affectif. Le commentaire du champ lexical est évalué, pas son simple relevé."),
("Comment le dossier dépasse-t-il l'opposition entre maison rêvée et maison vécue ?",
 "Les trois documents ne s'excluent pas : la maison reste un ancrage symbolique tout en étant traversée par des usages professionnels et familiaux. Une bonne réponse propose une réconciliation plutôt qu'un rejet."),
],
"A1": [
("Quel est l'apport du document juridique dans le dossier ?",
 "Il montre que la société traduit les enjeux moraux en normes : la protection animale est encadrée par des textes, ce qui relativise l'approche strictement philosophique."),
("Comment analyser une photographie comme un document argumentatif ?",
 "Le cadrage, la lumière, la présence ou l'absence des animaux et le contexte d'élevage industriel produisent un point de vue : l'image prend position, elle ne se contente pas d'illustrer."),
],
"A2": [
("Quels éléments de contexte repérer avant de rédiger le courriel ?",
 "Le destinataire (service client), l'objet (demande de précisions), le rôle du rédacteur (responsable adjoint), l'action proposée (animation locale) et le registre formel attendu."),
("Comment éviter la traduction littérale dans un courriel professionnel ?",
 "En employant des formules anglaises courantes (I am writing to…, Could you please…, We would appreciate…) et des structures propres à la langue, plutôt qu'un calque du français."),
("Quel vocabulaire précis utiliser pour parler de fidélisation ?",
 "loyalty programme, loyalty card, retention, customer data, personalised offers, consent : ces termes remplacent des équivalents approximatifs."),
("Pourquoi le compte rendu doit-il rester objectif ?",
 "Le correcteur évalue la capacité à restituer fidèlement les idées du document ; un jugement personnel n'a pas sa place dans cet exercice de compréhension."),
],
"A3": [
("Quels connecteurs structurent l'analyse en anglais ?",
 "First, then, however, as a result, in conclusion : ils rendent visible la progression du raisonnement et facilitent la compréhension du jury."),
("Comment le jury évalue-t-il la production orale ?",
 "Sur la compréhension restituée, la clarté de l'analyse, la prononciation, l'intonation, la gamme de langue et la pertinence des réponses en interaction."),
("Quelle solution proposer si le stock nécessaire au click and collect manque ?",
 "Informer immédiatement le client, proposer une alternative (livraison, produit de substitution, bon d'achat) et conserver une trace de l'incident pour analyser la cause."),
],
"A4": [
("Quelle règle de politesse appliquer dans la réponse écrite au client ?",
 "S'excuser sincèrement, ne pas rejeter la faute sur un autre service, proposer une réparation précise et conserver un ton neutre et respectueux."),
("Comment vérifier que le briefing a été compris par l'équipe ?",
 "En posant des questions, en demandant à un collaborateur de reformuler la procédure et en diffusant un compte rendu écrit accessible à tous."),
("Quel lien ce cas établit-il entre communication interne et expérience client ?",
 "Un défaut de coordination et de communication interne se répercute directement sur la qualité de la relation client : les deux dimensions sont indissociables."),
],
"A5": [
("Quel temps employer pour décrire une évolution récente aux conséquences présentes ?",
 "Le present perfect : « Sales have increased by 4% ». Avec une date précise, on revient au prétérit : « Sales increased in November »."),
("Comment exprimer une baisse du taux de transformation ?",
 "« The conversion rate fell from 18% to 16% » ou « dropped by 2 percentage points » ; on veille à la différence entre pourcentage et points de pourcentage."),
("Quel indicateur proposer pour le mois suivant ?",
 "Un suivi hebdomadaire du taux de transformation et de la fréquentation, avec un objectif chiffré et un responsable identifié."),
("Pourquoi analyser le panier moyen et la transformation ensemble ?",
 "Un panier moyen en hausse peut masquer une baisse du nombre d'acheteurs : les deux indicateurs donnent une lecture complète de la performance."),
],
"B0": [
("Comment la réglementation européenne sur les cosmétiques affecte-t-elle la stratégie ?",
 "Elle impose des allégations vérifiables et une conformité des étiquettes : elle renforce la différenciation par la transparence mais crée une contrainte de coût et de traçabilité."),
("Quels indicateurs piloter la modernisation numérique ?",
 "Part du chiffre d'affaires en ligne, taux de transformation du site, coût d'acquisition client, délai de livraison, taux de retours et NPS."),
],
"B1": [
("Comment le statut de SARL influence-t-il le financement ?",
 "La responsabilité limitée rassure les associés, mais les parts sont moins faciles à négocier que des actions ; le recours à l'emprunt dépend de la capacité de remboursement et des garanties."),
("Quels indicateurs mesurer l'impact du numérique ?",
 "Trafic du site, taux de transformation, panier moyen, part des commandes en ligne, taux de retour et respect des délais de livraison."),
],
"B2": [
("Quelle compétence devient critique avec la numérisation de l'étude ?",
 "La maîtrise des outils numériques et l'accompagnement des clients dans les nouvelles démarches, sans perdre l'exigence de conseil et de confidentialité."),
("Comment mesurer la qualité de la relation client dans une étude notariale ?",
 "Par des enquêtes de satisfaction, le délai moyen de traitement des dossiers, le taux de réclamation et le nombre de recommandations."),
],
"B3": [
("Quel rôle joue la confiance dans un modèle économique en ligne ?",
 "Les avis clients, les garanties, la sécurité du paiement et la qualité logistique réduisent l'incertitude et favorisent la conversion."),
("Quels critères choisir pour évaluer un partenariat stratégique ?",
 "Complémentarité des ressources, partage des risques, gouvernance claire, compatibilité des cultures et répartition équitable de la valeur créée."),
],
"D0": [
("Quel lien établir entre performance commerciale et situation financière ?",
 "Une baisse du taux de transformation ou une hausse de la démarque réduit la marge commerciale, ce qui se répercute sur l'EBE et la trésorerie : le tableau de bord et les SIG doivent être analysés ensemble."),
],
}

for part in "ABCD":
    p = os.path.join(D, "lead-mco-partie-%s.json" % part)
    with open(p, encoding="utf-8") as f:
        data = json.load(f)
    for i, a in enumerate(data["annales"]):
        key = "%s%d" % (part, i)
        extras = EXTRA.get(key, [])
        if not extras:
            continue
        nums = set(re.findall(r"(?<!\d)([1-9])\.", a["contenu"])) | set(re.findall(r"QUESTION\s*(\d+)", a["contenu"]))
        start = len(nums) + 1
        qs = "\n\nQUESTIONS COMPLÉMENTAIRES :\n" + "\n".join(
            "%d. %s" % (start + j, q) for j, (q, _) in enumerate(extras))
        cs = "\n\nCORRECTIONS COMPLÉMENTAIRES :\n" + "\n".join(
            "%d. %s" % (start + j, c) for j, (_, c) in enumerate(extras))
        a["contenu"] += qs
        a["correction"] += cs
        print(key, "->", len(nums) + len(extras), "questions")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
