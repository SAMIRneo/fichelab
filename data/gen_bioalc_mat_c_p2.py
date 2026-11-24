# -*- coding: utf-8 -*-
# Fiches 3 à 7 — exécuté depuis gen_bioalc_mat_c.py

# ============================================================ FICHE 3
FICHES.append(mk(
    ["BTS1"], BIO, "Chapitre 3 · Extraction d'acides nucléiques", SRC_BIO,
    [
     "Une extraction d'acides nucléiques vise à isoler l'ADN ou l'ARN d'un échantillon en éliminant les protéines, lipides, sels et autres contaminants. Les grandes étapes sont : lyse, séparation/purification, précipitation ou élution, et contrôle qualité.",
     "La lyse rompt les membranes et les parois : détergents (SDS, Triton), agents chaotropiques (guanidine), protéinase K (digestion des protéines). Pour les tissus végétaux et les bactéries à Gram +, une broyage mécanique (billes) est nécessaire.",
     "La séparation repose sur l'extraction organique (phénol-chloroforme : l'ADN reste en phase aqueuse, les protéines en phase organique) ou sur des méthodes solides : colonne de silice, billes magnétiques, précipitation au sel. Les kits commercialisés standardisent ces étapes.",
     "La précipitation utilise l'éthanol ou l'isopropanol en présence de sels : les acides nucléiques précipitent, sont lavés (éthanol 70 %) puis repris dans de l'eau ou un tampon TE (Tris-EDTA).",
     "Quantification par spectrophotométrie : les bases absorbent à 260 nm. 1 unité d'absorbance (DO) correspond à 50 µg/mL d'ADN double brin, 40 µg/mL d'ARN et 33 µg/mL d'ADN simple brin (pour une cuve de 1 cm).",
     "Formule : C = A260 × facteur de conversion × facteur de dilution. La masse totale = C × volume d'élution. Le rendement d'extraction = masse d'acide nucléique obtenue / masse d'échantillon de départ (en µg/g ou ng/mg).",
     "Contrôle de pureté : A260/A280 ≈ 1,8 pour un ADN pur et ≈ 2,0 pour un ARN pur. Un rapport inférieur indique une contamination protéique ou phénolique ; A260/A230 (attendu 2,0–2,2) signale les sels et détergents.",
     "La fluorimétrie (Qubit, kits spécifiques ADN/ARN) est plus sensible et plus spécifique que la spectrophotométrie : elle mesure uniquement l'acide nucléique cible et permet de détecter des concentrations très faibles.",
     "Les ARN sont très sensibles aux ARNases : travailler sur glace, utiliser des tubes et pointes RNase-free, de l'eau traitée DEPC et des gants. La qualité se contrôle par électrophorèse (bandes d'ARNr 28S/18S nettes) ou par indice RIN.",
     "Sécurité et traçabilité : phénol et chloroforme sont corrosifs et toxiques (hotte, gants, lunettes) ; le bromure d'éthidium est mutagène. Noter le numéro de lot du kit, la date, le type d'échantillon et le rendement dans le cahier de laboratoire."
    ],
    [
     qcm("À quelle longueur d'onde dose-t-on les acides nucléiques ?", ["280 nm", "260 nm", "230 nm", "595 nm"], 1,
         "Les bases azotées absorbent maximum à 260 nm ; 280 nm sert à détecter les protéines et 230 nm les sels."),
     qcm("À combien de µg/mL correspond 1 DO à 260 nm pour de l'ADN double brin ?", ["20", "33", "40", "50"], 3,
         "1 DO260 = 50 µg/mL pour l'ADN double brin, 40 µg/mL pour l'ARN, 33 µg/mL pour l'ADN simple brin."),
     qcm("Quel rapport indique un ADN pur ?", ["A260/A280 ≈ 0,8", "A260/A280 ≈ 1,8", "A260/A280 ≈ 2,5", "A260/A230 ≈ 0,5"], 1,
         "Un ADN pur a A260/A280 ≈ 1,8 ; un ARN pur ≈ 2,0. Un rapport plus faible trahit une contamination protéique."),
     qcm("Quel est le rôle de la protéinase K ?", ["Digérer les protéines", "Précipiter l'ADN", "Dénaturer les bases", "Lire l'absorbance"], 0,
         "La protéinase K digère les protéines (notamment les nucléases) au cours de la lyse."),
     qcm("Quelle méthode de quantification est la plus spécifique de l'ADN ?", ["Spectrophotométrie UV", "Fluorimétrie (Qubit)", "Pesée", "Conductimétrie"], 1,
         "La fluorimétrie avec un colorant spécifique ne mesure que l'ADN (ou l'ARN), contrairement à l'UV qui voit aussi les contaminants."),
     qcm("Dans l'extraction au phénol-chloroforme, où se trouve l'ADN ?", ["Dans la phase organique", "À l'interface", "Dans la phase aqueuse", "Dans le culot de débris"], 2,
         "L'ADN, très polaire, reste dans la phase aqueuse supérieure ; les protéines et lipides passent dans la phase organique."),
     qt("Pourquoi manipuler les ARN sur glace et avec du matériel RNase-free ?",
        "Parce que les ARNases (RNases) sont très résistantes et dégradent rapidement l'ARN. Le froid ralentit leur activité et le matériel traité (DEPC, tubes certifiés) évite la contamination.",
        "Un ARN dégradé donne des bandes étalées en électrophorèse et des résultats de RT-qPCR erronés."),
     qcm("Un extrait d'ADN est dilué au 1/50 et donne A260 = 0,200. Quelle est la concentration de la solution mère ?",
         ["100 µg/mL", "250 µg/mL", "500 µg/mL", "1 000 µg/mL"], 2,
         "C = 0,200 × 50 µg/mL × 50 = 500 µg/mL.",
         "Contrôle de qualité d'un extrait d'ADN végétal au spectrophotomètre.", True),
     qcm("Cet extrait (500 µg/mL) est repris dans 50 µL et provient de 100 mg de tissu. Quel est le rendement ?",
         ["25 µg/g", "250 µg/g", "2 500 µg/g", "50 µg/g"], 1,
         "masse = 500 µg/mL × 0,050 mL = 25 µg ; rendement = 25 µg / 0,100 g = 250 µg/g.",
         "Calcul du rendement d'extraction rapporté à la masse de matière première.", True),
     qcm("Un échantillon donne A260/A280 = 1,45. Que conclure ?",
         ["L'ADN est pur", "Il y a une contamination protéique", "Il y a une contamination par l'ARN", "Le dosage est impossible"], 1,
         "Un rapport inférieur à 1,8 signale des protéines (ou du phénol) : il faut repurifier l'extrait.",
         "Interprétation des ratios de pureté après extraction.", True)
    ],
    [
     intro("L'idée en une phrase", "Extraire, c'est libérer les acides nucléiques puis éliminer tout le reste : on juge le résultat à sa concentration, à sa pureté et à son rendement."),
     formule("Quantification et rendement", "C = A260 × 50 × F (ADN ds)   ·   R = (C × V) / m_échantillon", "50 µg/mL par DO pour l'ADN double brin · 40 pour l'ARN · F = facteur de dilution"),
     grille("Les 3 critères de qualité", [
         ["Concentration", "A260 × facteur de conversion × dilution", "ng/µL ou µg/mL"],
         ["Pureté", "A260/A280 ≈ 1,8 (ADN), ≈ 2,0 (ARN)", "sans unité"],
         ["Rendement", "masse obtenue / masse de départ", "µg/g ou ng/mg"]]),
     liste("Les 4 étapes de l'extraction", [
         "Lyse : détergent + protéinase K (+ broyage pour tissus et Gram +)",
         "Séparation : phénol-chloroforme, colonne de silice ou billes magnétiques",
         "Précipitation/élution : éthanol, lavages, reprise dans l'eau ou TE",
         "Contrôle : A260, ratios 260/280 et 260/230, électrophorèse ou Qubit"]),
     etapes("Réussir son extraction", [
         "Homogénéiser l'échantillon et le maintenir au froid",
         "Lyser complètement sans dégrader les acides nucléiques",
         "Éliminer protéines et sels par lavage soigneux",
         "Sécher le culot avant reprise (résidus d'éthanol = inhibition de PCR)",
         "Doser, contrôler la pureté et calculer le rendement"]),
     attention("⚠️ Les pièges classiques", [
         "Oublier le facteur de dilution dans le calcul de concentration",
         "Confondre 50 µg/mL (ADN) et 40 µg/mL (ARN)",
         "Laisser de l'éthanol : la PCR sera inhibée",
         "Manipuler l'ARN à température ambiante sans précautions RNase",
         "Ranger l'échantillon sans identifiant ni numéro de lot"]),
     exemples("En chiffres (à savoir refaire)", [
         "<span class=\"cle\">A260 = 0,2, dilution 1/50</span> → 500 µg/mL",
         "<span class=\"cle\">500 µg/mL × 0,05 mL</span> → 25 µg d'ADN",
         "<span class=\"cle\">25 µg / 0,1 g</span> → 250 µg/g de rendement",
         "<span class=\"cle\">A260/A280 = 1,8</span> → ADN pur",
         "<span class=\"cle\">A260/A230 &lt; 2</span> → sels / détergents résiduels"]),
    ],
    [
     sc("1 · Les étapes de l'extraction", """<svg viewBox="0 0 660 175" width="100%" role="img" aria-label="Quatre étapes de l'extraction d'acides nucléiques">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
      <g font-size="11" text-anchor="middle">
        <rect x="8" y="46" width="140" height="64" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="78" y="70" fill="var(--ac)" font-weight="bold">1. Lyse</text><text x="78" y="88" fill="var(--fg)">détergent + Prot.K</text><text x="78" y="102" fill="var(--dim)">(+ broyage)</text>
        <line x1="150" y1="78" x2="168" y2="78" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="172" y="46" width="140" height="64" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="242" y="70" fill="var(--ac)" font-weight="bold">2. Séparation</text><text x="242" y="88" fill="var(--fg)">phénol / silice</text><text x="242" y="102" fill="var(--dim)">ou billes magnétiques</text>
        <line x1="314" y1="78" x2="332" y2="78" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="336" y="46" width="140" height="64" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="406" y="70" fill="var(--ac)" font-weight="bold">3. Précipitation</text><text x="406" y="88" fill="var(--fg)">éthanol + sels</text><text x="406" y="102" fill="var(--dim)">lavage, reprise</text>
        <line x1="478" y1="78" x2="496" y2="78" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="500" y="46" width="150" height="64" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="575" y="70" fill="var(--ac)" font-weight="bold">4. Contrôle</text><text x="575" y="88" fill="var(--fg)">A260, pureté</text><text x="575" y="102" fill="var(--dim)">rendement</text>
      </g>
      <text x="330" y="142" text-anchor="middle" fill="var(--warn)" font-size="11">ARN : glace + matériel RNase-free · résidus d'éthanol → inhibition de PCR</text>
     </svg>"""),
     sc("2 · Spectre et ratios de pureté", """<svg viewBox="0 0 660 200" width="100%" role="img" aria-label="Spectre d'absorption à 260 280 230 nm et interprétation des ratios">
      <line x1="50" y1="160" x2="380" y2="160" stroke="var(--dim)" stroke-width="2"/><line x1="50" y1="160" x2="50" y2="30" stroke="var(--dim)" stroke-width="2"/>
      <text x="34" y="34" fill="var(--fg)" font-size="11">A</text><text x="350" y="180" fill="var(--fg)" font-size="11">λ (nm)</text>
      <path d="M50 155 C110 150 150 130 185 65 C200 42 215 48 235 90 C255 132 285 150 380 156" fill="none" stroke="var(--ac)" stroke-width="3"/>
      <line x1="200" y1="45" x2="200" y2="160" stroke="var(--warn)" stroke-width="1.5" stroke-dasharray="4 3"/>
      <text x="204" y="44" fill="var(--warn)" font-size="11">260 nm = ADN/ARN</text>
      <text x="252" y="120" fill="var(--dim)" font-size="10">280 nm = protéines</text>
      <text x="86" y="148" fill="var(--dim)" font-size="10">230 nm = sels</text>
      <rect x="404" y="40" width="240" height="130" rx="8" fill="var(--card2)" stroke="var(--dim)"/>
      <text x="418" y="62" fill="var(--ac)" font-size="12" font-weight="bold">Interprétation</text>
      <text x="418" y="86" fill="var(--fg)" font-size="11">260/280 ≈ 1,8 → ADN pur</text>
      <text x="418" y="108" fill="var(--fg)" font-size="11">260/280 ≈ 2,0 → ARN pur</text>
      <text x="418" y="130" fill="var(--warn)" font-size="11">&lt; 1,8 → protéines / phénol</text>
      <text x="418" y="152" fill="var(--warn)" font-size="11">260/230 &lt; 2 → sels, détergents</text>
     </svg>"""),
     sc("3 · Du dosage au rendement", """<svg viewBox="0 0 660 170" width="100%" role="img" aria-label="Calcul de concentration masse et rendement d'extraction">
      <text x="16" y="24" fill="var(--ac)" font-size="15" font-weight="bold">Du signal au rendement</text>
      <rect x="16" y="42" width="180" height="52" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="106" y="64" text-anchor="middle" fill="var(--fg)" font-size="12">A260 = 0,200</text><text x="106" y="82" text-anchor="middle" fill="var(--dim)" font-size="10">dilution 1/50</text>
      <line x1="198" y1="68" x2="236" y2="68" stroke="var(--ac)" stroke-width="2"/><text x="217" y="60" text-anchor="middle" fill="var(--ac)" font-size="10">×50×50</text>
      <rect x="240" y="42" width="180" height="52" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="330" y="64" text-anchor="middle" fill="var(--fg)" font-size="12">C = 500 µg/mL</text><text x="330" y="82" text-anchor="middle" fill="var(--dim)" font-size="10">solution mère</text>
      <line x1="422" y1="68" x2="460" y2="68" stroke="var(--ac)" stroke-width="2"/><text x="441" y="60" text-anchor="middle" fill="var(--ac)" font-size="10">×0,05 mL</text>
      <rect x="464" y="42" width="180" height="52" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="554" y="64" text-anchor="middle" fill="var(--fg)" font-size="12">m = 25 µg</text><text x="554" y="82" text-anchor="middle" fill="var(--dim)" font-size="10">d'ADN extrait</text>
      <rect x="180" y="116" width="300" height="40" rx="8" fill="var(--card2)" stroke="var(--warn)"/>
      <text x="330" y="142" text-anchor="middle" fill="var(--warn)" font-size="13">R = 25 µg / 0,100 g = 250 µg/g</text>
     </svg>""")
    ]
))

# ============================================================ FICHE 4
FICHES.append(mk(
    ["BTS1", "BTS2"], BIO, "Chapitre 4 · PCR et PCR en temps réel (qPCR)", SRC_BIO,
    [
     "La PCR (Polymerase Chain Reaction) amplifie un fragment d'ADN défini par deux amorces. Un cycle comporte trois étapes : dénaturation (94–95 °C, séparation des brins), hybridation (50–65 °C, fixation des amorces) et élongation (72 °C, synthèse par la Taq polymérase).",
     "Le mélange réactionnel contient : ADN matrice, deux amorces (forward et reverse), dNTP, ions Mg²⁺, tampon et une ADN polymérase thermostable (Taq, isolée de Thermus aquaticus). Le thermocycleur répète 25 à 40 cycles.",
     "En théorie, le nombre de copies double à chaque cycle : N = N₀ × 2ⁿ (efficacité 100 %). En pratique, l'efficacité réelle est comprise entre 90 et 110 %. La PCR est exponentielle puis atteint un plateau (épuisement des réactifs).",
     "Les amorces délimitent l'amplicon et conditionnent la spécificité. Leur Tm (Wallace ou formulation plus précise) impose la température d'hybridation. Un contrôle négatif (NTC, sans ADN) et un contrôle positif sont indispensables pour valider un run.",
     "La qPCR (PCR en temps réel) suit la fluorescence à chaque cycle. Deux chimies : colorant intercalant (SYBR Green, non spécifique mais simple) ou sonde (TaqMan : reporter + quencher, spécificité accrue par hydrolyse de la sonde).",
     "Le Ct (ou Cq) est le cycle où la fluorescence franchit le seuil, dans la phase exponentielle. Plus l'échantillon est riche en matrice, plus le Ct est petit : Ct ∝ −log(quantité initiale). Un Ct > 35 évoque une faible charge et se rapproche de la limite de détection.",
     "La courbe d'étalonnage (gamme de dilutions) donne Ct = pente × log(Q) + b. Une efficacité de 100 % correspond à une pente de −3,32 ; l'efficacité se calcule par E = 10^(−1/pente) − 1. On exige une pente entre −3,1 et −3,58 (E = 90–110 %) et un R² ≥ 0,98–0,99.",
     "En quantification relative (Livak), ΔCt = Ct(gène cible) − Ct(gène de référence), ΔΔCt = ΔCt(échantillon) − ΔCt(calibrateur), et l'expression relative vaut 2^(−ΔΔCt). Cette méthode suppose des efficacités proches de 100 % et comparables entre cible et référence.",
     "La RT-qPCR ajoute une transcription inverse de l'ARN en ADN complémentaire (cDNA) avant l'amplification : elle permet d'étudier l'expression génique ou de détecter des virus à ARN.",
     "Bonnes pratiques (MIQE) : planification des contrôles, duplication/triplicats, courbe de fusion pour SYBR, limite de détection et de quantification, traçabilité des lots de réactifs et du thermocycleur."
    ],
    [
     qcm("À quelle température se fait l'hybridation des amorces ?", ["95 °C", "72 °C", "50–65 °C", "37 °C"], 2,
         "Dénaturation 94–95 °C, hybridation 50–65 °C (selon le Tm des amorces), élongation 72 °C."),
     qcm("Quelle enzyme est utilisée en PCR classique ?", ["Une ADN ligase", "La Taq polymérase", "L'ARN polymérase", "La reverse transcriptase"], 1,
         "La Taq polymérase est thermostable : elle résiste aux cycles de dénaturation à 95 °C."),
     qcm("Que signifie un Ct faible en qPCR ?", ["Peu de matrice au départ", "Beaucoup de matrice au départ", "Une contamination", "Une mauvaise sonde"], 1,
         "Le seuil est atteint tôt quand la quantité initiale est élevée : Ct et log(quantité) sont inversement proportionnels."),
     qcm("Quelle est la pente théorique d'une courbe d'étalonnage à 100 % d'efficacité ?", ["−2,00", "−3,32", "−4,00", "−1,00"], 1,
         "Une pente de −3,32 correspond à un doublement par cycle (E = 100 %)."),
     qcm("Quel contrôle détecte une contamination des réactifs ?", ["Le contrôle positif", "Le NTC (contrôle négatif)", "La gamme d'étalonnage", "La courbe de fusion"], 1,
         "Le NTC (no template control) ne contient pas d'ADN : toute amplification signale une contamination."),
     qcm("Que mesure la méthode 2^(−ΔΔCt) ?", ["Une concentration absolue", "Une expression relative", "Une température de fusion", "Une taille d'amplicon"], 1,
         "La méthode comparative de Livak donne un rapport d'expression par rapport à un calibrateur."),
     qt("Pourquoi la qPCR est-elle une méthode quantitative ?",
        "Parce que le Ct dépend de la quantité initiale de matrice : le nombre de cycles nécessaires pour atteindre un seuil de fluorescence est d'autant plus faible que la quantité de départ est grande. Une gamme d'étalonnage permet de convertir le Ct en quantité.",
        "Relation : Ct = −3,32 × log(Q) + b à 100 % d'efficacité."),
     qcm("On part de 10 copies d'ADN et on effectue 30 cycles à 100 % d'efficacité. Combien de copies obtient-on (ordre de grandeur) ?",
         ["≈ 10³", "≈ 10⁶", "≈ 10¹⁰", "≈ 10³⁰"], 2,
         "N = 10 × 2³⁰ ≈ 10 × 1,07 × 10⁹ ≈ 1,07 × 10¹⁰ copies.",
         "Estimation du nombre de copies en fin d'amplification PCR.", True),
     qcm("Une courbe d'étalonnage a une pente de −3,10. Quelle est l'efficacité (E = 10^(−1/pente) − 1) ?",
         ["≈ 90 %", "≈ 100 %", "≈ 110 %", "≈ 120 %"], 2,
         "E = 10^(1/3,10) − 1 ≈ 10^0,3226 − 1 ≈ 2,10 − 1 = 1,10, soit 110 % (limite haute acceptée).",
         "Validation d'une qPCR : l'efficacité doit se situer entre 90 et 110 %.", True),
     qcm("Pour un gène cible, ΔCt = 3 et le calibrateur a ΔCt = 1. Quelle est l'expression relative (2^(−ΔΔCt)) ?",
         ["4 fois plus", "2 fois plus", "4 fois moins", "2 fois moins"], 2,
         "ΔΔCt = 3 − 1 = 2 → 2⁻² = 0,25 : l'expression est 4 fois plus faible que dans le calibrateur.",
         "Analyse d'expression génique par la méthode comparative de Livak.", True)
    ],
    [
     intro("L'idée en une phrase", "La PCR copie un fragment d'ADN de façon exponentielle ; la qPCR ajoute une fluorescence pour compter les copies dès chaque cycle et donc quantifier le départ."),
     formule("Les relations clés", "N = N₀ × (1+E)ⁿ   ·   Ct = −3,32 log(Q) + b   ·   E = 10^(−1/pente) − 1", "2^(−ΔΔCt) = expression relative · pente idéale −3,32 · efficacité acceptée 90–110 %"),
     grille("Les 3 températures du cycle", [
         ["Dénaturation", "94–95 °C", "séparation des deux brins"],
         ["Hybridation", "50–65 °C", "fixation des amorces (Tm)"],
         ["Élongation", "72 °C", "synthèse par la Taq polymérase"]]),
     liste("Les ingrédients indispensables", [
         "ADN matrice + amorces forward/reverse (délimitent l'amplicon)",
         "dNTP, Mg²⁺, tampon, Taq polymérase thermostable",
         "Contrôles : NTC (contamination) et contrôle positif (fonctionnement)",
         "qPCR : SYBR Green (intercalant) ou sonde TaqMan (reporter/quencher)"]),
     etapes("Un run de qPCR bien mené", [
         "Concevoir des amorces avec un Tm adapté et vérifier leur spécificité",
         "Préparer une gamme de dilutions connues pour l'étalonnage",
         "Lancer le programme : dénaturation initiale puis 35–40 cycles",
         "Vérifier Ct, pente, R² et courbe de fusion (SYBR)",
         "Convertir les Ct en quantités et rendre le résultat avec son incertitude"]),
     attention("⚠️ Les pièges classiques", [
         "Oublier le NTC : une contamination passe inaperçue",
         "Accepter une pente hors de −3,1…−3,58 (efficacité invalide)",
         "Comparer des Ct absolus entre deux appareils ou deux chimies différentes",
         "Utiliser 2^(−ΔΔCt) avec des efficacités qui diffèrent de plus de 10 %",
         "Un Ct très tardif (&gt; 35) doit être interprété avec prudence"]),
     exemples("En chiffres (à savoir refaire)", [
         "<span class=\"cle\">10 × 2³⁰</span> ≈ 1,07 × 10¹⁰ copies",
         "<span class=\"cle\">pente −3,32</span> → E = 100 %",
         "<span class=\"cle\">pente −3,10</span> → E ≈ 110 %",
         "<span class=\"cle\">ΔΔCt = 2</span> → 2⁻² = 0,25 (4× moins)",
         "<span class=\"cle\">10× dilution, E=100 %</span> → ΔCt ≈ 3,32"]),
    ],
    [
     sc("1 · Les trois étapes d'un cycle", """<svg viewBox="0 0 660 195" width="100%" role="img" aria-label="Cycle PCR en trois étapes avec températures">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
      <g font-size="11" text-anchor="middle">
        <rect x="16" y="46" width="170" height="70" rx="8" fill="var(--card2)" stroke="var(--warn)"/><text x="101" y="70" fill="var(--warn)" font-weight="bold">1. Dénaturation</text><text x="101" y="90" fill="var(--fg)" font-size="15">94–95 °C</text><text x="101" y="106" fill="var(--dim)" font-size="10">les brins se séparent</text>
        <line x1="188" y1="80" x2="228" y2="80" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="232" y="46" width="170" height="70" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="317" y="70" fill="var(--ac)" font-weight="bold">2. Hybridation</text><text x="317" y="90" fill="var(--fg)" font-size="15">50–65 °C</text><text x="317" y="106" fill="var(--dim)" font-size="10">amorces sur la matrice</text>
        <line x1="404" y1="80" x2="444" y2="80" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="448" y="46" width="196" height="70" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="546" y="70" fill="var(--ac)" font-weight="bold">3. Élongation</text><text x="546" y="90" fill="var(--fg)" font-size="15">72 °C</text><text x="546" y="106" fill="var(--dim)" font-size="10">Taq polymérase 5'→3'</text>
      </g>
      <path d="M620 130 C620 158 40 158 40 130" fill="none" stroke="var(--dim)" stroke-width="2" marker-end="url(#@@a)"/>
      <text x="330" y="152" text-anchor="middle" fill="var(--dim)" font-size="11">25 à 40 cycles · chaque cycle double la quantité (E ≈ 100 %)</text>
      <text x="330" y="182" text-anchor="middle" fill="var(--warn)" font-size="11">N = N₀ × 2ⁿ</text>
     </svg>"""),
     sc("2 · Courbe d'amplification et Ct", """<svg viewBox="0 0 660 210" width="100%" role="img" aria-label="Courbes d'amplification qPCR avec seuil et Ct">
      <line x1="50" y1="180" x2="620" y2="180" stroke="var(--dim)" stroke-width="2"/><line x1="50" y1="180" x2="50" y2="30" stroke="var(--dim)" stroke-width="2"/>
      <text x="32" y="36" fill="var(--fg)" font-size="11">ΔRn</text><text x="590" y="198" fill="var(--fg)" font-size="11">cycles</text>
      <line x1="50" y1="110" x2="620" y2="110" stroke="var(--warn)" stroke-width="1.5" stroke-dasharray="5 4"/>
      <text x="560" y="104" fill="var(--warn)" font-size="10">seuil</text>
      <path d="M50 176 C120 176 160 174 200 168 C240 156 260 130 285 92 C305 62 330 50 380 46 C460 42 540 42 620 42" fill="none" stroke="var(--ac)" stroke-width="3"/>
      <path d="M50 178 C160 178 240 176 300 170 C350 162 380 140 410 106 C440 76 480 56 620 50" fill="none" stroke="var(--dim)" stroke-width="2.5"/>
      <line x1="265" y1="110" x2="265" y2="180" stroke="var(--ac)" stroke-width="1.5" stroke-dasharray="4 3"/><text x="248" y="196" fill="var(--ac)" font-size="11">Ct₁</text>
      <line x1="405" y1="110" x2="405" y2="180" stroke="var(--dim)" stroke-width="1.5" stroke-dasharray="4 3"/><text x="394" y="196" fill="var(--dim)" font-size="11">Ct₂</text>
      <text x="300" y="62" fill="var(--ac)" font-size="11">phase exponentielle</text>
      <text x="470" y="160" fill="var(--dim)" font-size="10">plateau</text>
      <rect x="450" y="120" width="180" height="50" rx="6" fill="var(--card2)" stroke="var(--dim)"/>
      <text x="462" y="140" fill="var(--fg)" font-size="10">Ct petit = beaucoup de matrice</text>
      <text x="462" y="158" fill="var(--fg)" font-size="10">Ct grand = peu de matrice</text>
     </svg>"""),
     sc("3 · Courbe d'étalonnage et efficacité", """<svg viewBox="0 0 660 200" width="100%" role="img" aria-label="Courbe d'étalonnage Ct en fonction du log de la quantité et calcul de l'efficacité">
      <line x1="60" y1="170" x2="440" y2="170" stroke="var(--dim)" stroke-width="2"/><line x1="60" y1="170" x2="60" y2="30" stroke="var(--dim)" stroke-width="2"/>
      <text x="40" y="36" fill="var(--fg)" font-size="11">Ct</text><text x="390" y="188" fill="var(--fg)" font-size="11">log(Q)</text>
      <line x1="90" y1="50" x2="410" y2="150" stroke="var(--ac)" stroke-width="3"/>
      <g fill="var(--ac)"><circle cx="110" cy="57" r="4"/><circle cx="190" cy="83" r="4"/><circle cx="270" cy="110" r="4"/><circle cx="350" cy="136" r="4"/></g>
      <text x="150" y="60" fill="var(--warn)" font-size="11">pente = −3,32 → E = 100 %</text>
      <rect x="462" y="44" width="184" height="126" rx="8" fill="var(--card2)" stroke="var(--dim)"/>
      <text x="476" y="66" fill="var(--ac)" font-size="12" font-weight="bold">Efficacité</text>
      <text x="476" y="90" fill="var(--fg)" font-size="11">E = 10^(−1/pente) − 1</text>
      <text x="476" y="112" fill="var(--fg)" font-size="11">pente −3,10 → 110 %</text>
      <text x="476" y="134" fill="var(--fg)" font-size="11">R² ≥ 0,98 exigé</text>
      <text x="476" y="156" fill="var(--dim)" font-size="10">gamme de 5 dilutions</text>
     </svg>""")
    ]
))
