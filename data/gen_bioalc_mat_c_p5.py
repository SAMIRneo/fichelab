# -*- coding: utf-8 -*-
# Fiches 12 à 15 — exécuté depuis gen_bioalc_mat_c.py

# ============================================================ FICHE 12
FICHES.append(mk(
    ["BTS1"], QUA, "Chapitre 12 · Documentation, modes opératoires et traçabilité", SRC_QUA,
    [
     "La documentation qualité est organisée en pyramide : manuel qualité (politique et organisation), procédures (qui fait quoi et quand), modes opératoires (comment faire) et enregistrements (preuves). Chaque niveau doit être cohérent avec le précédent.",
     "Le mode opératoire est un document décrivant pas à pas la réalisation d'une tâche. Il précise : objet et domaine d'application, responsabilités, matériel et réactifs, déroulé des opérations, précautions de sécurité, conditions ambiantes, élimination des déchets, références normatives et version.",
     "Un bon mode opératoire est clair, précis, concis, rédigé dans une langue maîtrisée par les utilisateurs, daté, référencé, validé et diffusé. Il est relu périodiquement et modifié par un processus de mise à jour maîtrisé (MJV).",
     "La maîtrise des documents (ISO 17025 §7.5 et §8.2/8.3) impose : approbation avant diffusion, identification (référence, version, date, page), mise à disposition à point d'utilisation, retrait des versions obsolètes et traçabilité des modifications.",
     "Les enregistrements (§7.5, §8.4) sont des preuves d'activité : résultats bruts, conditions de l'essai, identifiants des échantillons, lots de réactifs, maintenances, formations. Ils doivent être lisibles, identifiables, immédiats et conservés pendant une durée définie.",
     "Règle d'or de la correction : une erreur sur un enregistrement papier est barrée d'un trait (lisible), la valeur correcte est inscrite à côté, avec la signature et la date de la personne. Ne jamais gratter, effacer ou recouvrir. En informatique, utiliser un audit trail (piste d'audit) non modifiable.",
     "La traçabilité des échantillons suit tout le parcours : réception et attribution d'un identifiant unique, étiquetage (code-barres), enregistrement des conditions de transport et de conservation, préparation, analyse, résultat, conservation ou élimination. C'est la chaîne de responsabilité (chaîne de custody).",
     "La traçabilité s'étend aux réactifs (fournisseur, lot, date de réception, péremption, ouverture), aux équipements (numéro, étalonnage, maintenance), au personnel (formation, habilitation) et aux méthodes (version du mode opératoire utilisé).",
     "Le cahier de laboratoire doit être relié, paginé, utilisé à l'encre, sans blanc ni rature destructive. Toute page est datée et signée ; les observations brutes y sont notées directement, sans report différé.",
     "Les principes ALCOA+ (Attributable, Legible, Contemporaneous, Original, Accurate, + Complete, Consistent, Enduring, Available) et les outils numériques (LIMS, sauvegardes, contrôle d'accès) garantissent l'intégrité des données."
    ],
    [
     qcm("Quel document décrit comment réaliser une opération ?", ["Le manuel qualité", "La procédure", "Le mode opératoire", "Le rapport d'audit"], 2,
         "Le mode opératoire décrit les gestes et les étapes ; la procédure décrit qui fait quoi et le manuel expose la politique."),
     qcm("Que faut-il faire face à une erreur sur un enregistrement papier ?", ["Gratter la valeur", "Barrer, corriger, signer et dater", "Recomencer la page", "Ignorer l'erreur"], 1,
         "La valeur erronée reste lisible : on la barre, on écrit la bonne valeur à côté et on date et signe la correction."),
     qcm("Comment corriger une erreur dans un système informatique ?", ["Supprimer l'ancienne valeur", "Écraser le fichier", "Conserver une piste d'audit (audit trail)", "Fermer le logiciel"], 2,
         "Le système doit conserver la valeur d'origine, la correction, l'auteur et l'horodatage : c'est l'audit trail."),
     qcm("Quel identifiant doit porter un échantillon dès sa réception ?", ["Le nom du client uniquement", "Un identifiant unique", "La date du jour", "Le numéro de lot du réactif"], 1,
         "Un identifiant unique évite toute confusion et permet de suivre l'échantillon sur tout son parcours."),
     qcm("Quelle est la durée de conservation des enregistrements ?", ["Toujours 1 an", "Définie par la procédure et la réglementation", "Jusqu'à la fin du stage", "Aucune règle"], 1,
         "La durée est fixée par la procédure du laboratoire et les exigences réglementaires ou contractuelles."),
     qcm("Que signifie le A de ALCOA ?", ["Automatique", "Attributable (attribuable)", "Annuel", "Approuvé"], 1,
         "ALCOA : Attributable, Legible, Contemporaneous, Original, Accurate — complété par Complete, Consistent, Enduring, Available."),
     qt("Pourquoi retirer les anciennes versions d'un mode opératoire ?",
        "Pour éviter qu'un opérateur n'utilise une méthode obsolète, source de résultats non conformes. La maîtrise des documents impose de diffuser uniquement la version en vigueur et d'archiver les anciennes versions hors des postes de travail.",
        "La version, la date et la référence doivent être visibles sur chaque page."),
     qcm("Sur 50 enregistrements contrôlés, 5 présentent une date manquante. Quel est le taux de conformité documentaire ?",
         ["5 %", "90 %", "95 %", "45 %"], 1,
         "Conformes = 45 ; taux = 45/50 × 100 = 90 %.",
         "Audit documentaire interne sur les enregistrements d'analyses.", True),
     qcm("Un mode opératoire passe de la version 2.1 à 3.0 après révision majeure, le 15/03. Quelle mention doit apparaître ?",
         ["v2.1, 15/03", "v3.0, 15/03", "Version unique sans date", "Aucune mention"], 1,
         "La version en vigueur (v3.0) et sa date d'application (15/03) doivent être identifiées ; l'ancienne version est retirée.",
         "Maîtrise des documents : identification et diffusion de la version en vigueur.", True),
     qcm("Un échantillon est conservé 3 jours à 4 °C avant analyse, puis 5 ans après. Combien de temps au total doit rester traçable son identifiant ?",
         ["3 jours", "5 ans", "Pendant toute la durée de conservation légale et le temps de conservation des enregistrements", "1 mois"], 2,
         "La traçabilité doit couvrir toute la durée de vie de l'échantillon et se prolonger dans les enregistrements, selon la procédure et la réglementation.",
         "Gestion de la traçabilité et des durées de conservation en laboratoire.", True)
    ],
    [
     intro("L'idée en une phrase", "Un résultat n'est fiable que si l'on peut reconstituer, des années plus tard, qui a fait quoi, avec quelle méthode, quel réactif et quel équipement."),
     formule("Intégrité des données", "ALCOA : Attributable · Legible · Contemporaneous · Original · Accurate", "+ Complete · Consistent · Enduring · Available"),
     grille("Pyramide documentaire", [
         ["Manuel qualité", "politique, organisation", "direction"],
         ["Procédures", "qui / quoi / quand", "responsables"],
         ["Modes opératoires", "comment faire", "opérateurs"],
         ["Enregistrements", "preuves", "traçabilité"]]),
     liste("Contenu d'un mode opératoire", [
         "Objet, domaine, responsabilités, référence et version",
         "Matériel, réactifs, lots et conditions ambiantes",
         "Étapes détaillées, points critiques, précautions de sécurité",
         "Expression des résultats, élimination des déchets, enregistrements"]),
     etapes("Corriger un enregistrement", [
         "Barrer la valeur erronée d'un seul trait (elle reste lisible)",
         "Inscrire la valeur correcte à côté, sans grattage",
         "Signer et dater la correction (ou laisser l'audit trail en informatique)",
         "Conserver l'original et archiver selon la durée définie",
         "Déclarer une non-conformité si l'erreur a affecté un résultat"]),
     attention("⚠️ Les pièges classiques", [
         "Utiliser une ancienne version d'un mode opératoire",
         "Effacer une erreur au correcteur ou supprimer une donnée brute",
         "Noter les résultats de mémoire en fin de journée",
         "Oublier le numéro de lot d'un réactif ou l'identifiant de l'échantillon",
         "Laisser une page blanche non barrée dans un cahier de laboratoire"]),
     exemples("En chiffres (à savoir refaire)", [
         "<span class=\"cle\">45/50</span> = 90 % de conformité documentaire",
         "<span class=\"cle\">v3.0 — 15/03</span> = version identifiée",
         "<span class=\"cle\">ALCOA+</span> = 9 qualités d'une donnée fiable",
         "<span class=\"cle\">Code-barres</span> = identifiant unique de l'échantillon",
         "<span class=\"cle\">Barrer + signer + dater</span> = correction conforme"]),
    ],
    [
     sc("1 · La pyramide documentaire", """<svg viewBox="0 0 660 195" width="100%" role="img" aria-label="Pyramide du manuel qualité aux enregistrements">
      <path d="M330 26 L470 74 L470 78 L190 78 L190 74 Z" fill="var(--card2)" stroke="var(--ac)"/>
      <text x="330" y="60" text-anchor="middle" fill="var(--ac)" font-size="13" font-weight="bold">Manuel qualité</text>
      <rect x="170" y="82" width="320" height="28" fill="var(--card2)" stroke="var(--ac)"/><text x="330" y="101" text-anchor="middle" fill="var(--fg)" font-size="12">Procédures — qui / quoi / quand</text>
      <rect x="130" y="114" width="400" height="28" fill="var(--card2)" stroke="var(--ac)"/><text x="330" y="133" text-anchor="middle" fill="var(--fg)" font-size="12">Modes opératoires — comment faire</text>
      <rect x="90" y="146" width="480" height="28" fill="var(--card2)" stroke="var(--warn)"/><text x="330" y="165" text-anchor="middle" fill="var(--warn)" font-size="12">Enregistrements — preuves et traçabilité</text>
     </svg>"""),
     sc("2 · La chaîne de traçabilité d'un échantillon", """<svg viewBox="0 0 660 175" width="100%" role="img" aria-label="Parcours d'un échantillon de la réception à l'élimination avec identifiant unique">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
      <g font-size="10" text-anchor="middle">
        <rect x="8" y="48" width="98" height="56" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="57" y="70" fill="var(--ac)" font-weight="bold">Réception</text><text x="57" y="88" fill="var(--fg)">ID unique</text>
        <line x1="108" y1="76" x2="126" y2="76" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="130" y="48" width="98" height="56" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="179" y="70" fill="var(--ac)" font-weight="bold">Étiquetage</text><text x="179" y="88" fill="var(--fg)">code-barres</text>
        <line x1="230" y1="76" x2="248" y2="76" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="252" y="48" width="98" height="56" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="301" y="70" fill="var(--ac)" font-weight="bold">Conservation</text><text x="301" y="88" fill="var(--fg)">T°, durée</text>
        <line x1="352" y1="76" x2="370" y2="76" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="374" y="48" width="98" height="56" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="423" y="70" fill="var(--ac)" font-weight="bold">Analyse</text><text x="423" y="88" fill="var(--fg)">lots, MO</text>
        <line x1="474" y1="76" x2="492" y2="76" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="496" y="48" width="98" height="56" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="545" y="70" fill="var(--ac)" font-weight="bold">Résultat</text><text x="545" y="88" fill="var(--fg)">+ archivage</text>
      </g>
      <text x="330" y="140" text-anchor="middle" fill="var(--dim)" font-size="11">Chaque étape est datée, signée et enregistrée : nul maillon ne doit manquer</text>
     </svg>"""),
     sc("3 · Corriger sans effacer", """<svg viewBox="0 0 660 165" width="100%" role="img" aria-label="Exemple de correction conforme d'un enregistrement papier barré signé et daté">
      <text x="16" y="24" fill="var(--ac)" font-size="15" font-weight="bold">Règle : barrer, corriger, signer, dater</text>
      <rect x="16" y="42" width="360" height="96" rx="6" fill="var(--card2)" stroke="var(--dim)"/>
      <text x="34" y="68" fill="var(--fg)" font-size="12">Résultat : <tspan text-decoration="line-through" fill="var(--warn)">12,5</tspan>  <tspan fill="var(--ac)" font-weight="bold">12,8</tspan> mg/L</text>
      <text x="34" y="96" fill="var(--fg)" font-size="11">Correction : M. Martin — 15/03</text>
      <text x="34" y="120" fill="var(--dim)" font-size="10">La valeur d'origine reste lisible</text>
      <rect x="398" y="42" width="246" height="96" rx="8" fill="var(--card2)" stroke="var(--warn)"/>
      <text x="412" y="64" fill="var(--warn)" font-size="12" font-weight="bold">Interdit</text>
      <text x="412" y="88" fill="var(--fg)" font-size="11">✗ gratter / effacer</text>
      <text x="412" y="110" fill="var(--fg)" font-size="11">✗ recouvrir au correcteur</text>
      <text x="412" y="130" fill="var(--fg)" font-size="11">✗ supprimer une donnée brute</text>
     </svg>""")
    ]
))

# ============================================================ FICHE 13
FICHES.append(mk(
    ["BTS2"], QUA, "Chapitre 13 · Qualification et maintenance des équipements", SRC_QUA,
    [
     "Un équipement doit être apte à son emploi et maintenu en état de marche tout au long de sa vie. La qualification est la démonstration documentée qu'un équipement est installé correctement et fonctionne conformément aux exigences attendues.",
     "La qualification suit le modèle des 4 Q : DQ (Design Qualification, conception et cahier des charges), IQ (Installation Qualification, installation conforme), OQ (Operational Qualification, fonctionnement dans la plage prévue) et PQ (Performance Qualification, performance réelle en conditions d'utilisation).",
     "Il ne faut pas confondre qualification, étalonnage et vérification. L'étalonnage compare l'appareil à une référence de plus haute exactitude et fournit les écarts et l'incertitude (traçabilité métrologique, §6.5). La vérification compare les résultats à des exigences spécifiées et rend un verdict conforme/non conforme.",
     "Le programme d'étalonnage (§6.4.6 et 6.4.7) définit les équipements concernés, la méthode, la fréquence, les critères d'acceptation et la conduite à tenir en cas de dépassement. La fréquence dépend de la criticité, de la stabilité dans le temps et des résultats des contrôles précédents.",
     "L'identification et le statut d'étalonnage (§6.4.8) doivent être visibles : étiquette avec la date du dernier étalonnage, la date d'échéance et le statut (vert = utilisable, rouge = hors service, orange = utilisation restreinte).",
     "Les contrôles intermédiaires et valeurs de référence (§6.4.10 et 6.4.11) maintiennent la confiance entre deux étalonnages : témoins, blancs, matériaux de référence certifiés, cartes de contrôle, vérifications journalières (par exemple contrôle de température d'un incubateur).",
     "La maintenance est préventive (planifiée : nettoyage, remplacement de pièces d'usure, vérifications périodiques) ou curative (intervention après panne). Un plan de maintenance et un registre des interventions sont tenus à jour.",
     "Un équipement défectueux (§6.4.9) doit être mis hors service, étiqueté et isolé. Le laboratoire doit évaluer l'incidence sur les résultats déjà produits et, si nécessaire, les invalider et prévenir le client.",
     "La criticité d'un équipement se juge sur son impact sur la validité des résultats : une balance ou un thermocycleur critique sera étalonné plus fréquemment qu'un agitateur simple.",
     "Les enregistrements (§6.4.13) comprennent l'identification de l'équipement, les certificats d'étalonnage, les rapports de qualification, les interventions de maintenance, les pannes et l'historique des températures ou paramètres critiques."
    ],
    [
     qcm("Que signifie le Q de IQ ?", ["Qualité", "Qualification de l'installation", "Quittance", "Quantité"], 1,
         "IQ = Installation Qualification : vérification que l'équipement est installé conformément aux prescriptions."),
     qcm("Quel est l'ordre des 4 Q ?", ["IQ, OQ, DQ, PQ", "DQ, IQ, OQ, PQ", "PQ, OQ, IQ, DQ", "DQ, OQ, IQ, PQ"], 1,
         "Conception → installation → opération → performance : DQ, IQ, OQ, PQ."),
     qcm("Quelle est la différence entre étalonnage et vérification ?", ["Aucune", "L'étalonnage donne écarts et incertitude, la vérification donne un verdict", "La vérification donne l'incertitude", "L'étalonnage est gratuit"], 1,
         "L'étalonnage compare à une référence et quantifie l'écart ; la vérification décide de la conformité à une exigence."),
     qcm("Que faire d'un équipement hors étalonnage ?", ["Le continuer à utiliser", "Le mettre hors service et évaluer l'impact sur les résultats", "Le revendre", "Rien"], 1,
         "Il faut l'isoler, l'étiqueter et analyser l'incidence sur les résultats déjà rendus (§6.4.9)."),
     qcm("Quelle couleur d'étiquette indique un équipement utilisable ?", ["Rouge", "Orange", "Vert", "Blanc"], 2,
         "Vert = conforme/utilisable, rouge = hors service, orange = utilisation restreinte."),
     qcm("Qu'appelle-t-on maintenance préventive ?", ["Une intervention après panne", "Une intervention planifiée avant panne", "Un étalonnage", "Un audit"], 1,
         "La maintenance préventive est planifiée (nettoyage, pièces d'usure, contrôles) ; la maintenance curative intervient après défaillance."),
     qt("Pourquoi fréquencer davantage l'étalonnage d'un équipement critique ?",
         "Parce que sa dérive aurait un impact direct sur la validité des résultats. La fréquence est fixée en fonction de la criticité, de la stabilité observée et des résultats des contrôles intermédiaires, afin de maintenir un risque acceptable.",
         "Un thermocycleur ou une balance critique est étalonné plus souvent qu'un simple agitateur."),
     qcm("Un équipement étalonné le 10/01 avec une fréquence de 12 mois doit être reprogrammé avant quelle date ?",
         ["10/01 de l'année suivante (le jour même)", "10/12 de la même année", "10/02 de l'année suivante", "Aucune échéance"], 0,
         "Échéance = dernière date + intervalle = 10/01 + 12 mois = 10/01 l'année suivante ; il faut le programmer avant cette date.",
         "Gestion du plan d'étalonnage et des échéances.", True),
     qcm("Une balance donne 100,3 mg pour une masse certifiée de 100,0 mg. Quel est l'écart relatif ?",
         ["0,03 %", "0,3 %", "3 %", "0,003 %"], 1,
         "Écart relatif = (100,3 − 100,0)/100,0 = 0,3/100 = 0,003 = 0,3 %.",
         "Interprétation d'un certificat d'étalonnage et comparaison à la tolérance.", True),
     qcm("Sur 40 équipements, 38 ont un étalonnage à jour. Quel est le taux de conformité du parc ?",
         ["38 %", "90 %", "95 %", "2 %"], 2,
         "Taux = 38/40 × 100 = 95 %.",
         "Indicateur de maîtrise du parc d'équipements du laboratoire.", True)
    ],
    [
     intro("L'idée en une phrase", "Un appareil n'est fiable que s'il a été qualifié, étalonné, maintenu et identifié : sans cela, aucun résultat produit n'est réellement valide."),
     formule("Écart et échéance", "Écart relatif = (valeur mesurée − valeur de référence) / valeur de référence", "Échéance = date du dernier étalonnage + intervalle · U = k·u"),
     grille("Qualifier, étalonner, vérifier", [
         ["Qualification", "DQ, IQ, OQ, PQ", "aptitude à la fonction"],
         ["Étalonnage", "comparaison à une référence", "écart + incertitude, traçabilité"],
         ["Vérification", "comparaison à une exigence", "verdict conforme / non conforme"]]),
     liste("Les statuts d'un équipement", [
         "Vert : conforme, utilisable pour les analyses",
         "Orange : utilisation restreinte (plage ou application limitée)",
         "Rouge : hors service, isolé et étiqueté",
         "Chaque étiquette porte la date d'étalonnage et la date d'échéance"]),
     etapes("Qualifier un nouvel équipement", [
         "DQ : rédiger le cahier des charges et choisir le fournisseur",
         "IQ : vérifier la livraison, l'installation et les documents",
         "OQ : tester les fonctions et les plages de fonctionnement",
         "PQ : démontrer la performance en conditions réelles d'analyse",
         "Établir le plan d'étalonnage, de maintenance et les enregistrements"]),
     attention("⚠️ Les pièges classiques", [
         "Confondre étalonnage (écart + incertitude) et vérification (verdict)",
         "Utiliser un appareil dont l'échéance d'étalonnage est dépassée",
         "Oublier d'évaluer l'impact d'une panne sur les résultats antérieurs",
         "Négliger les contrôles intermédiaires entre deux étalonnages",
         "Ne pas tracer les interventions de maintenance"]),
     exemples("En chiffres (à savoir refaire)", [
         "<span class=\"cle\">(100,3−100,0)/100</span> = 0,3 % d'écart",
         "<span class=\"cle\">10/01 + 12 mois</span> → échéance 10/01",
         "<span class=\"cle\">38/40</span> = 95 % d'équipements à jour",
         "<span class=\"cle\">DQ → IQ → OQ → PQ</span> = les 4 Q",
         "<span class=\"cle\">§6.4.9</span> = gestion des équipements défectueux"]),
    ],
    [
     sc("1 · Les 4 Q de la qualification", """<svg viewBox="0 0 660 175" width="100%" role="img" aria-label="Les quatre étapes de qualification DQ IQ OQ PQ">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
      <g font-size="11" text-anchor="middle">
        <rect x="10" y="48" width="140" height="64" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="80" y="72" fill="var(--ac)" font-weight="bold">DQ</text><text x="80" y="90" fill="var(--fg)">conception</text><text x="80" y="105" fill="var(--dim)" font-size="9">cahier des charges</text>
        <line x1="152" y1="80" x2="172" y2="80" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="176" y="48" width="140" height="64" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="246" y="72" fill="var(--ac)" font-weight="bold">IQ</text><text x="246" y="90" fill="var(--fg)">installation</text><text x="246" y="105" fill="var(--dim)" font-size="9">documents, montage</text>
        <line x1="318" y1="80" x2="338" y2="80" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="342" y="48" width="140" height="64" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="412" y="72" fill="var(--ac)" font-weight="bold">OQ</text><text x="412" y="90" fill="var(--fg)">opérationnel</text><text x="412" y="105" fill="var(--dim)" font-size="9">plages de fonctionnement</text>
        <line x1="484" y1="80" x2="504" y2="80" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="508" y="48" width="140" height="64" rx="8" fill="var(--card2)" stroke="var(--warn)"/><text x="578" y="72" fill="var(--warn)" font-weight="bold">PQ</text><text x="578" y="90" fill="var(--fg)">performance</text><text x="578" y="105" fill="var(--dim)" font-size="9">conditions réelles</text>
      </g>
      <text x="330" y="146" text-anchor="middle" fill="var(--dim)" font-size="11">Chaque étape donne un rapport et des enregistrements archivés</text>
     </svg>"""),
     sc("2 · Étiquetage et statut", """<svg viewBox="0 0 660 175" width="100%" role="img" aria-label="Étiquettes de statut d'étalonnage vert orange rouge">
      <text x="16" y="24" fill="var(--ac)" font-size="15" font-weight="bold">Le statut doit être visible sur l'appareil</text>
      <rect x="18" y="44" width="190" height="92" rx="8" fill="var(--card2)" stroke="#2e9e5b" stroke-width="3"/>
      <circle cx="48" cy="74" r="12" fill="#2e9e5b"/><text x="78" y="72" fill="var(--fg)" font-size="12" font-weight="bold">VERT</text>
      <text x="34" y="102" fill="var(--fg)" font-size="11">conforme, utilisable</text><text x="34" y="122" fill="var(--dim)" font-size="10">échéance : 10/01/2027</text>
      <rect x="235" y="44" width="190" height="92" rx="8" fill="var(--card2)" stroke="#e0a021" stroke-width="3"/>
      <circle cx="265" cy="74" r="12" fill="#e0a021"/><text x="295" y="72" fill="var(--fg)" font-size="12" font-weight="bold">ORANGE</text>
      <text x="251" y="102" fill="var(--fg)" font-size="11">usage restreint</text><text x="251" y="122" fill="var(--dim)" font-size="10">plage limitée</text>
      <rect x="452" y="44" width="190" height="92" rx="8" fill="var(--card2)" stroke="#d64545" stroke-width="3"/>
      <circle cx="482" cy="74" r="12" fill="#d64545"/><text x="512" y="72" fill="var(--fg)" font-size="12" font-weight="bold">ROUGE</text>
      <text x="468" y="102" fill="var(--fg)" font-size="11">hors service</text><text x="468" y="122" fill="var(--dim)" font-size="10">isolé + évaluation impact</text>
     </svg>"""),
     sc("3 · Carte de contrôle et dérive", """<svg viewBox="0 0 660 185" width="100%" role="img" aria-label="Carte de contrôle avec limites et dérive détectée">
      <line x1="55" y1="165" x2="620" y2="165" stroke="var(--dim)" stroke-width="2"/><line x1="55" y1="165" x2="55" y2="25" stroke="var(--dim)" stroke-width="2"/>
      <line x1="55" y1="55" x2="620" y2="55" stroke="var(--warn)" stroke-width="1.5" stroke-dasharray="5 4"/><text x="560" y="50" fill="var(--warn)" font-size="10">LCS</text>
      <line x1="55" y1="140" x2="620" y2="140" stroke="var(--warn)" stroke-width="1.5" stroke-dasharray="5 4"/><text x="560" y="154" fill="var(--warn)" font-size="10">LCI</text>
      <line x1="55" y1="97" x2="620" y2="97" stroke="var(--ac)" stroke-width="2"/><text x="560" y="92" fill="var(--ac)" font-size="10">moyenne</text>
      <polyline points="80,95 130,100 180,92 230,105 280,98 330,102 380,95 430,88 480,62 530,50" fill="none" stroke="var(--ac)" stroke-width="2.5"/>
      <g fill="var(--ac)"><circle cx="80" cy="95" r="3"/><circle cx="130" cy="100" r="3"/><circle cx="180" cy="92" r="3"/><circle cx="230" cy="105" r="3"/><circle cx="280" cy="98" r="3"/><circle cx="330" cy="102" r="3"/><circle cx="380" cy="95" r="3"/></g>
      <circle cx="530" cy="50" r="5" fill="var(--warn)"/>
      <text x="360" y="30" fill="var(--warn)" font-size="11">Dérive → alerte avant échéance</text>
      <text x="330" y="182" text-anchor="middle" fill="var(--dim)" font-size="10">contrôles intermédiaires (§6.4.10) entre deux étalonnages</text>
     </svg>""")
    ]
))

# ============================================================ FICHE 14
FICHES.append(mk(
    ["BTS2"], QUA, "Chapitre 14 · Non-conformités et audit interne", SRC_QUA,
    [
     "Une non-conformité (NC) est le non-respect d'une exigence spécifiée (ISO 9000). Elle peut être détectée lors d'un contrôle, d'une réclamation client, d'un audit, d'une dérive d'équipement ou d'une erreur de manipulateur.",
     "L'ISO/IEC 17025 traite les travaux non conformes au §7.10 et les actions correctives au §8.7. Le §7.10 impose : identifier le problème, arrêter le travail si nécessaire, évaluer l'incidence (y compris sur les résultats antérieurs), décider de l'acceptabilité, informer le client si l'écart a une influence notable et enregistrer toutes les décisions.",
     "Le §8.7 structure la réponse : réagir à la NC et la corriger, analyser la cause, déterminer si des NC similaires existent ou pourraient survenir, mettre en œuvre l'action corrective, vérifier son efficacité, mettre à jour les risques et le SMQ, et conserver les enregistrements.",
     "Il faut distinguer correction (traiter le symptôme immédiat), action corrective (éliminer la cause pour éviter la récidive) et action préventive (empêcher une NC potentielle).",
     "La fiche de non-conformité est l'outil de suivi : numéro unique, date, description factuelle, gravité, cause identifiée, action décidée, responsable, échéance, vérification d'efficacité et date de clôture.",
     "La recherche de cause s'appuie sur des outils : les 5 Pourquoi (remonter de l'effet à la cause racine), le diagramme d'Ishikawa (5 M : Méthode, Main-d'œuvre, Matériel, Matière, Milieu), le Pareto (20 % des causes produisent 80 % des effets).",
     "L'audit interne (§8.8) est un examen systématique, indépendant et documenté, réalisé à intervalles planifiés. Il vérifie que le SMQ est conforme aux exigences de la norme, qu'il est effectivement mis en œuvre et qu'il est entretenu.",
     "Le programme d'audit définit la fréquence, les méthodes, les responsabilités, la portée et les critères (ISO 17025, procédures du laboratoire, exigences réglementaires). L'auditeur doit être compétent et indépendant de l'activité auditée pour garantir objectivité et impartialité.",
     "L'audit donne lieu à une fiche d'écart et à un rapport d'audit ; les actions correctives sont mises en œuvre sans délai indu et leur efficacité est vérifiée. On distingue audits internes (1re partie), audits clients (2e partie) et audits de certification/accréditation (3e partie).",
     "La revue de direction (§8.9), au moins annuelle, examine les indicateurs, les résultats des audits, les réclamations et les opportunités d'amélioration, et prend les décisions d'allocation de ressources."
    ],
    [
     qcm("Quel paragraphe de l'ISO 17025 traite des actions correctives ?", ["7.10", "8.6", "8.7", "8.8"], 2,
         "§8.7 = actions correctives ; §7.10 = travaux non conformes ; §8.8 = audits internes."),
     qcm("Que fait-on en premier face à une non-conformité ?", ["On clôt le dossier", "On réagit : corriger et maîtriser la situation", "On informe le client", "On change de méthode"], 1,
         "§8.7 a) : réagir à la NC, prendre action pour la maîtriser et en corriger les effets."),
     qcm("Quelle est la différence entre correction et action corrective ?", ["Aucune", "La correction traite le symptôme, l'action corrective élimine la cause", "La corrective est plus rapide", "La correction est documentée"], 1,
         "Corriger = traiter l'effet ; l'action corrective supprime la cause pour éviter toute récidive."),
     qcm("Quel outil identifie les causes par la technique des 5 Pourquoi ?", ["Ishikawa", "Pareto", "5 Pourquoi", "Carte de contrôle"], 2,
         "Les 5 Pourquoi itèrent la question « pourquoi ? » pour remonter à la cause racine."),
     qcm("Qui doit réaliser un audit interne ?", ["Un auditeur indépendant et compétent", "Le responsable de l'activité auditée", "Le client", "Un fournisseur"], 0,
         "L'objectivité et l'impartialité imposent un auditeur compétent, indépendant de l'activité auditée."),
     qcm("Quelle est la finalité de la revue de direction ?", ["Réaliser les analyses", "Examiner le SMQ et décider des ressources", "Signer les rapports", "Étalonner les appareils"], 1,
         "La revue de direction (§8.9) évalue la pertinence et l'efficacité du SMQ et prend les décisions stratégiques."),
     qt("Pourquoi évaluer l'incidence d'une NC sur les résultats antérieurs ?",
        "Parce qu'une dérive ou une erreur peut avoir affecté des résultats déjà rendus. Le laboratoire doit déterminer si ces résultats restent valides et, le cas échéant, les invalider, informer le client et rappeler les rapports concernés.",
        "C'est une exigence explicite du §7.10 (évaluation de l'importance, y compris l'impact sur les résultats précédents)."),
     qcm("Sur 500 analyses, 12 non-conformités sont relevées. Quel est le taux de NC ?",
         ["0,24 %", "2,4 %", "24 %", "12 %"], 1,
         "Taux de NC = 12/500 × 100 = 2,4 %.",
         "Suivi des non-conformités dans le tableau de bord qualité.", True),
     qcm("Sur 10 actions correctives, 8 sont closes dans le délai imparti. Quel est le taux de respect des délais ?",
         ["8 %", "20 %", "80 %", "12 %"], 2,
         "Taux = 8/10 × 100 = 80 %.",
         "Indicateur de suivi des actions correctives issues d'un audit.", True),
     qcm("Une NC est ouverte le 3/03 et clôturée le 13/03. Quel est le délai de traitement ?",
         ["7 jours", "10 jours", "13 jours", "3 jours"], 1,
         "13 − 3 = 10 jours calendaires entre l'ouverture et la clôture.",
         "Mesure du délai moyen de traitement des non-conformités.", True)
    ],
    [
     intro("L'idée en une phrase", "Une non-conformité n'est vraiment traitée que lorsque la cause a été éliminée et l'efficacité de l'action vérifiée : corriger ne suffit pas."),
     formule("Processus NC", "Correction (symptôme) → Analyse de cause → Action corrective → Vérification d'efficacité", "Outils : 5 Pourquoi · Ishikawa (5 M) · Pareto · Taux de NC = NC / total × 100"),
     grille("Correction / corrective / préventive", [
         ["Correction", "traite l'effet immédiat", "ex. refaire l'analyse"],
         ["Action corrective", "élimine la cause", "ex. former l'opérateur"],
         ["Action préventive", "empêche une NC potentielle", "ex. revoir la maintenance"]]),
     liste("Les étapes du §8.7", [
         "Réagir : maîtriser et corriger la NC, en traiter les conséquences",
         "Analyser : examiner la NC, déterminer les causes et les NC similaires",
         "Agir : mettre en œuvre l'action corrective appropriée",
         "Vérifier : contrôler l'efficacité, actualiser les risques et le SMQ",
         "Enregistrer : nature, causes, actions et résultats (§8.7.3)"]),
     etapes("Conduire un audit interne", [
         "Planifier : programme, critères, portée, auditeur indépendant",
         "Préparer : documents, grille d'audit, annonce à l'équipe",
         "Réaliser : interviews, observations, examen des enregistrements",
         "Rapporter : fiche d'écart, rapport, classement des constats",
         "Suivre : actions correctives, vérification d'efficacité, clôture"]),
     attention("⚠️ Les pièges classiques", [
         "Se contenter de corriger sans chercher la cause",
         "Ne pas vérifier l'efficacité de l'action corrective",
         "Oublier d'évaluer l'impact sur les résultats déjà rendus",
         "Confier l'audit à la personne qui exécute l'activité auditée",
         "Ne pas informer le client alors que son résultat est affecté"]),
     exemples("En chiffres (à savoir refaire)", [
         "<span class=\"cle\">12/500</span> = 2,4 % de non-conformités",
         "<span class=\"cle\">8/10</span> = 80 % d'actions à temps",
         "<span class=\"cle\">13 − 3</span> = 10 jours de délai",
         "<span class=\"cle\">5 M</span> = Méthode, Main-d'œuvre, Matériel, Matière, Milieu",
         "<span class=\"cle\">§7.10 / §8.7 / §8.8</span> = NC travaux / correctives / audits"]),
    ],
    [
     sc("1 · Le processus de traitement d'une NC", """<svg viewBox="0 0 660 190" width="100%" role="img" aria-label="Les étapes du traitement d'une non-conformité selon le paragraphe 8.7">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
      <g font-size="10" text-anchor="middle">
        <rect x="8" y="48" width="112" height="60" rx="8" fill="var(--card2)" stroke="var(--warn)"/><text x="64" y="72" fill="var(--warn)" font-weight="bold">1. Réagir</text><text x="64" y="90" fill="var(--fg)">maîtriser</text>
        <line x1="122" y1="78" x2="140" y2="78" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="144" y="48" width="112" height="60" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="200" y="72" fill="var(--ac)" font-weight="bold">2. Analyser</text><text x="200" y="90" fill="var(--fg)">cause racine</text>
        <line x1="258" y1="78" x2="276" y2="78" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="280" y="48" width="112" height="60" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="336" y="72" fill="var(--ac)" font-weight="bold">3. Décider</text><text x="336" y="90" fill="var(--fg)">action corrective</text>
        <line x1="394" y1="78" x2="412" y2="78" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="416" y="48" width="112" height="60" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="472" y="72" fill="var(--ac)" font-weight="bold">4. Agir</text><text x="472" y="90" fill="var(--fg)">mettre en œuvre</text>
        <line x1="530" y1="78" x2="548" y2="78" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="552" y="48" width="100" height="60" rx="8" fill="var(--card2)" stroke="var(--warn)"/><text x="602" y="72" fill="var(--warn)" font-weight="bold">5. Vérifier</text><text x="602" y="90" fill="var(--fg)">efficacité</text>
      </g>
      <text x="330" y="140" text-anchor="middle" fill="var(--dim)" font-size="11">Évaluer l'impact sur les résultats antérieurs (§7.10) · enregistrer chaque étape (§8.7.3)</text>
      <text x="330" y="166" text-anchor="middle" fill="var(--warn)" font-size="11">Une NC non traitée revient toujours : la cause doit être éliminée</text>
     </svg>"""),
     sc("2 · Le cycle de l'audit interne", """<svg viewBox="0 0 660 180" width="100%" role="img" aria-label="Cycle de l'audit interne planifier réaliser rapporter suivre">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
      <rect x="16" y="50" width="140" height="60" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="86" y="74" text-anchor="middle" fill="var(--ac)" font-weight="bold">Planifier</text><text x="86" y="94" text-anchor="middle" fill="var(--fg)" font-size="10">programme, critères</text>
      <line x1="158" y1="80" x2="196" y2="80" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
      <rect x="200" y="50" width="140" height="60" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="270" y="74" text-anchor="middle" fill="var(--ac)" font-weight="bold">Réaliser</text><text x="270" y="94" text-anchor="middle" fill="var(--fg)" font-size="10">interviews, preuves</text>
      <line x1="342" y1="80" x2="380" y2="80" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
      <rect x="384" y="50" width="140" height="60" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="454" y="74" text-anchor="middle" fill="var(--ac)" font-weight="bold">Rapporter</text><text x="454" y="94" text-anchor="middle" fill="var(--fg)" font-size="10">fiche d'écart, rapport</text>
      <line x1="526" y1="80" x2="564" y2="80" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
      <rect x="568" y="50" width="76" height="60" rx="8" fill="var(--card2)" stroke="var(--warn)"/><text x="606" y="74" text-anchor="middle" fill="var(--warn)" font-weight="bold">Suivre</text><text x="606" y="94" text-anchor="middle" fill="var(--fg)" font-size="10">actions</text>
      <path d="M606 116 C606 152 86 152 86 116" fill="none" stroke="var(--dim)" stroke-width="2" marker-end="url(#@@a)"/>
      <text x="346" y="148" text-anchor="middle" fill="var(--dim)" font-size="11">Auditeur compétent et indépendant · §8.8</text>
     </svg>"""),
     sc("3 · Ishikawa (5 M) et Pareto", """<svg viewBox="0 0 660 190" width="100%" role="img" aria-label="Diagramme d'Ishikawa cinq M et principe de Pareto">
      <line x1="40" y1="170" x2="360" y2="170" stroke="var(--dim)" stroke-width="2"/>
      <line x1="40" y1="170" x2="200" y2="70" stroke="var(--ac)" stroke-width="2"/>
      <line x1="40" y1="170" x2="320" y2="80" stroke="var(--ac)" stroke-width="2"/>
      <g font-size="10" fill="var(--fg)"><text x="80" y="120">Méthode</text><text x="150" y="96">Main-d'œuvre</text><text x="250" y="106">Matériel</text><text x="110" y="160">Matière</text><text x="290" y="160">Milieu</text></g>
      <rect x="200" y="44" width="150" height="34" rx="6" fill="var(--card2)" stroke="var(--warn)"/><text x="275" y="66" text-anchor="middle" fill="var(--warn)" font-size="12" font-weight="bold">Non-conformité</text>
      <line x1="390" y1="170" x2="390" y2="50" stroke="var(--dim)" stroke-width="2"/><line x1="390" y1="170" x2="620" y2="170" stroke="var(--dim)" stroke-width="2"/>
      <rect x="404" y="110" width="40" height="60" fill="var(--ac)"/><rect x="448" y="130" width="40" height="40" fill="var(--ac)"/><rect x="492" y="145" width="40" height="25" fill="var(--ac)"/><rect x="536" y="157" width="40" height="13" fill="var(--ac)"/><rect x="580" y="165" width="40" height="5" fill="var(--ac)"/>
      <text x="400" y="40" fill="var(--ac)" font-size="11" font-weight="bold">Pareto : 20 % des causes → 80 % des effets</text>
     </svg>""")
    ]
))

# ============================================================ FICHE 15
FICHES.append(mk(
    ["BTS2"], QUA, "Chapitre 15 · Indicateurs et amélioration continue", SRC_QUA,
    [
     "Un indicateur est une grandeur ou un paramètre permettant de mesurer l'atteinte d'un objectif. Un KPI (indicateur clé de performance) est un indicateur prioritaire pour le pilotage. Il doit être pertinent, mesurable, périodique et relié à une cible.",
     "On distingue les indicateurs de résultat (lag, qui mesurent le passé, ex. taux de conformité) et les indicateurs de pilotage (lead, qui anticipent, ex. taux d'étalonnages à jour).",
     "Les principaux indicateurs qualité d'un laboratoire : taux de conformité des résultats, taux de non-conformités, taux de reruns (réanalyses), délai moyen de rendu des résultats, taux de réclamations clients, taux de participation et de conformité aux essais interlaboratoires (EEQ/CIQ), taux d'équipements étalonnés à jour.",
     "Les calculs courants : taux de conformité = nombre conforme / total × 100 ; taux de défaut = nombre non conforme / total × 100 ; taux de couverture d'étalonnage = équipements à jour / parc total × 100 ; écart à la cible = valeur mesurée − cible.",
     "Pour les séries de mesures, on calcule la moyenne et l'écart-type (fidélité, ISO 5725). L'incertitude élargie U = k·u avec k = 2 (niveau de confiance ≈ 95 %) accompagne obligatoirement le résultat (§7.6).",
     "Le tableau de bord regroupe les indicateurs sous forme visualisable (jauges, feux tricolores, courbes) avec une périodicité définie (hebdomadaire, mensuelle) et des seuils d'alerte. Il permet de détecter rapidement une dérive.",
     "La carte de contrôle (Shewhart) représente la valeur d'un témoin en fonction du temps, avec une ligne centrale (moyenne) et des limites de contrôle. Le respect des règles de Western Electric (dépassement, tendance, dépassement consécutif) déclenche une alerte avant la non-conformité.",
     "L'amélioration continue s'appuie sur le cycle PDCA (Plan-Do-Check-Act ou roue de Deming) et sur des outils : 5 Pourquoi, Ishikawa, Pareto, 8D, benchmark, analyse des risques.",
     "L'ISO 17025 impose à la fois l'amélioration (§8.6 : identifier les opportunités, recueillir les retours clients positifs et négatifs), les actions correctives (§8.7), les audits internes (§8.8) et la revue de direction (§8.9).",
     "L'objectif final est de réduire la variabilité des processus, de satisfaire le client et de renforcer la confiance dans les résultats, tout en maîtrisant les coûts et les délais."
    ],
    [
     qcm("Que signifie KPI ?", ["Indicateur clé de performance", "Contrôle qualité interne", "Plan d'action", "Certification"], 0,
         "KPI = Key Performance Indicator, indicateur clé de performance pour le pilotage."),
     qcm("Quel est un indicateur de pilotage (lead) ?", ["Le taux de conformité du mois", "Le taux d'étalonnages à jour", "Le nombre de réclamations reçues", "Le chiffre d'affaires"], 1,
         "Le taux d'équipements à jour anticipe un risque ; le taux de conformité mesure un résultat passé (lag)."),
     qcm("Quelle est la formule du taux de conformité ?", ["Non conformes / total × 100", "Conformes / total × 100", "Conformes × total", "Total / conformes"], 1,
         "Taux de conformité = nombre de résultats conformes / nombre total × 100."),
     qcm("Quelle est l'incertitude élargie pour u = 0,4 et k = 2 ?", ["0,2", "0,4", "0,8", "2"], 2,
         "U = k × u = 2 × 0,4 = 0,8 (niveau de confiance ≈ 95 %)."),
     qcm("Que représente la ligne centrale d'une carte de contrôle ?", ["La limite supérieure", "La moyenne du procédé", "La spécification client", "Le résultat le plus récent"], 1,
         "La carte de contrôle comporte une ligne centrale (moyenne) et des limites de contrôle supérieure et inférieure."),
     qcm("Quel outil hiérarchise les causes par importance décroissante ?", ["Ishikawa", "Pareto", "5 Pourquoi", "PDCA"], 1,
         "Le diagramme de Pareto classe les causes par fréquence : environ 20 % d'entre elles génèrent 80 % des effets."),
     qt("Pourquoi utiliser un feu tricolore sur un tableau de bord ?",
         "Parce qu'il donne une lecture immédiate de l'état des indicateurs : vert = objectif atteint, orange = seuil d'alerte atteint, rouge = objectif non atteint nécessitant une action corrective.",
         "Le tableau de bord doit aussi préciser la périodicité, le responsable et la cible de chaque indicateur."),
     qcm("Sur 250 résultats, 238 sont conformes. Quel est le taux de conformité ?",
         ["92,5 %", "95,2 %", "88,0 %", "12,0 %"], 1,
         "Taux = 238/250 × 100 = 95,2 %.",
         "Indicateur mensuel de conformité des analyses d'un laboratoire.", True),
     qcm("Le délai de rendu moyen est de 3,2 jours pour une cible de 2,5 jours. Quel est l'écart à la cible ?",
         ["−0,7 jour", "+0,7 jour", "+1,3 jour", "0,7 %"], 1,
         "Écart = valeur mesurée − cible = 3,2 − 2,5 = +0,7 jour (dépassement).",
         "Pilotage des délais de rendu des résultats (indicateur de processus).", True),
     qcm("Un laboratoire atteint 95,2 % de conformité alors que la cible est 98 %. Quelle action est la plus appropriée ?",
         ["Ne rien faire", "Analyser les causes des 12 non-conformités et engager une action corrective", "Augmenter la cible", "Changer de client"], 1,
         "L'écart à la cible justifie une analyse des causes (5 Pourquoi, Pareto) et une action corrective suivie d'une vérification d'efficacité.",
         "Exploitation d'un tableau de bord qualité et déclenchement du cycle d'amélioration.", True)
    ],
    [
     intro("L'idée en une phrase", "On ne pilote que ce que l'on mesure : les indicateurs détectent la dérive, le cycle PDCA et les actions correctives permettent de la corriger durablement."),
     formule("Indicateurs et incertitude", "Taux = (nombre concerné / total) × 100   ·   Écart à la cible = mesuré − cible", "U = k·u (k = 2 ≈ 95 %) · moyenne et écart-type selon ISO 5725"),
     grille("Les familles d'indicateurs", [
         ["Conformité", "taux de conformité, taux de NC", "résultat (lag)"],
         ["Processus", "délai de rendu, taux de reruns", "pilotage (lead)"],
         ["Ressources", "étalonnages à jour, formations", "pilotage (lead)"],
         ["Clients", "réclamations, satisfaction", "résultat (lag)"]]),
     liste("Les indicateurs incontournables", [
         "Taux de conformité des résultats et des contrôles internes/externes",
         "Taux de non-conformités et de réanalyses (reruns)",
         "Délai moyen de rendu et taux de respect des délais",
         "Taux d'équipements étalonnés à jour et taux de participation aux EEQ",
         "Taux de réclamations clients et retour d'information (§8.6.2)"]),
     etapes("Mettre en œuvre l'amélioration continue", [
         "Définir la cible et l'indicateur, puis collecter les données",
         "Représenter l'indicateur sur un tableau de bord avec des seuils",
         "Détecter une dérive (carte de contrôle, écart à la cible)",
         "Analyser les causes (Pareto, Ishikawa, 5 Pourquoi)",
         "Engager l'action corrective puis vérifier son efficacité (PDCA)"]),
     attention("⚠️ Les pièges classiques", [
         "Suivre un indicateur sans cible ni seuil d'alerte",
         "Confondre un indicateur de résultat (lag) et de pilotage (lead)",
         "Oublier l'incertitude dans l'expression d'un résultat",
         "Réagir à un point isolé sans regarder la tendance",
         "Ne pas vérifier l'efficacité de l'action d'amélioration"]),
     exemples("En chiffres (à savoir refaire)", [
         "<span class=\"cle\">238/250</span> = 95,2 % de conformité",
         "<span class=\"cle\">3,2 − 2,5</span> = +0,7 jour d'écart",
         "<span class=\"cle\">U = 2 × 0,4</span> = 0,8",
         "<span class=\"cle\">20/80</span> = règle de Pareto",
         "<span class=\"cle\">PDCA</span> = Plan, Do, Check, Act"]),
    ],
    [
     sc("1 · Feu tricolore et tableau de bord", """<svg viewBox="0 0 660 185" width="100%" role="img" aria-label="Tableau de bord avec indicateurs et seuils feu tricolore">
      <text x="16" y="24" fill="var(--ac)" font-size="15" font-weight="bold">Tableau de bord qualité — lecture immédiate</text>
      <g font-size="11" fill="var(--fg)">
        <rect x="16" y="40" width="628" height="26" fill="var(--card2)" stroke="var(--dim)"/>
        <text x="28" y="57" font-weight="bold">Indicateur</text><text x="290" y="57" font-weight="bold">Valeur</text><text x="410" y="57" font-weight="bold">Cible</text><text x="520" y="57" font-weight="bold">État</text>
        <text x="28" y="84">Taux de conformité</text><text x="290" y="84">95,2 %</text><text x="410" y="84">98 %</text>
        <text x="28" y="110">Taux de reruns</text><text x="290" y="110">4,0 %</text><text x="410" y="110">&lt; 2 %</text>
        <text x="28" y="136">Étalonnages à jour</text><text x="290" y="136">95 %</text><text x="410" y="136">100 %</text>
        <text x="28" y="162">Délai moyen de rendu</text><text x="290" y="162">3,2 j</text><text x="410" y="162">2,5 j</text>
      </g>
      <circle cx="560" cy="79" r="8" fill="#e0a021"/><circle cx="560" cy="105" r="8" fill="#d64545"/><circle cx="560" cy="131" r="8" fill="#e0a021"/><circle cx="560" cy="157" r="8" fill="#d64545"/>
      <text x="580" y="83" fill="var(--warn)" font-size="10">alerte</text><text x="580" y="109" fill="var(--warn)" font-size="10">action</text>
     </svg>"""),
     sc("2 · Carte de contrôle", """<svg viewBox="0 0 660 185" width="100%" role="img" aria-label="Carte de contrôle avec moyenne limites et alerte sur tendance">
      <line x1="55" y1="165" x2="620" y2="165" stroke="var(--dim)" stroke-width="2"/><line x1="55" y1="165" x2="55" y2="25" stroke="var(--dim)" stroke-width="2"/>
      <line x1="55" y1="48" x2="620" y2="48" stroke="var(--warn)" stroke-width="1.5" stroke-dasharray="5 4"/><text x="556" y="43" fill="var(--warn)" font-size="10">LCS</text>
      <line x1="55" y1="140" x2="620" y2="140" stroke="var(--warn)" stroke-width="1.5" stroke-dasharray="5 4"/><text x="556" y="154" fill="var(--warn)" font-size="10">LCI</text>
      <line x1="55" y1="94" x2="620" y2="94" stroke="var(--ac)" stroke-width="2"/><text x="550" y="89" fill="var(--ac)" font-size="10">moyenne</text>
      <polyline points="80,92 130,96 180,90 230,98 280,94 330,100 380,104 430,112 480,120 530,132" fill="none" stroke="var(--ac)" stroke-width="2.5"/>
      <g fill="var(--ac)"><circle cx="80" cy="92" r="3"/><circle cx="130" cy="96" r="3"/><circle cx="180" cy="90" r="3"/><circle cx="230" cy="98" r="3"/><circle cx="280" cy="94" r="3"/><circle cx="330" cy="100" r="3"/></g>
      <circle cx="530" cy="132" r="5" fill="var(--warn)"/>
      <text x="370" y="32" fill="var(--warn)" font-size="11">Tendance continue → alerte avant la limite</text>
      <text x="330" y="182" text-anchor="middle" fill="var(--dim)" font-size="10">la carte de contrôle détecte la dérive du procédé (Shewhart)</text>
     </svg>"""),
     sc("3 · PDCA et outils d'amélioration", """<svg viewBox="0 0 660 180" width="100%" role="img" aria-label="Roue PDCA associée aux outils d'amélioration continue">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
      <path d="M200 46 C310 34 380 60 380 92 C380 126 310 150 200 138" fill="none" stroke="var(--ac)" stroke-width="3" marker-end="url(#@@a)"/>
      <path d="M200 138 C90 150 40 126 40 92 C40 60 90 34 200 46" fill="none" stroke="var(--ac)" stroke-width="3" marker-end="url(#@@a)"/>
      <text x="210" y="28" text-anchor="middle" fill="var(--ac)" font-size="12" font-weight="bold">PLAN — planifier</text>
      <text x="400" y="96" fill="var(--ac)" font-size="12" font-weight="bold">DO — faire</text>
      <text x="210" y="162" text-anchor="middle" fill="var(--ac)" font-size="12" font-weight="bold">ACT — agir</text>
      <text x="0" y="96" fill="var(--ac)" font-size="12" font-weight="bold">CHECK</text>
      <text x="210" y="84" text-anchor="middle" fill="var(--dim)" font-size="11">Amélioration continue</text>
      <rect x="440" y="34" width="206" height="130" rx="8" fill="var(--card2)" stroke="var(--dim)"/>
      <text x="454" y="56" fill="var(--ac)" font-size="12" font-weight="bold">Outils</text>
      <text x="454" y="80" fill="var(--fg)" font-size="11">5 Pourquoi · Ishikawa</text>
      <text x="454" y="102" fill="var(--fg)" font-size="11">Pareto (20/80) · 8D</text>
      <text x="454" y="124" fill="var(--fg)" font-size="11">Carte de contrôle</text>
      <text x="454" y="146" fill="var(--dim)" font-size="10">ISO 17025 §8.6 à 8.9</text>
     </svg>""")
    ]
))
