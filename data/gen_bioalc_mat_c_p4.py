# -*- coding: utf-8 -*-
# Fiches 9 à 15 — exécuté depuis gen_bioalc_mat_c.py

# ============================================================ FICHE 9
FICHES.append(mk(
    ["BTS2"], BIO, "Chapitre 9 · Pharmacologie et toxicologie", SRC_BIO,
    [
     "La pharmacologie étudie les interactions entre un médicament et l'organisme. Elle se divise en pharmacodynamie (ce que le médicament fait à l'organisme : mécanisme et effets) et pharmacocinétique (ce que l'organisme fait au médicament : absorption, distribution, métabolisme, excrétion — ADME).",
     "Un médicament est composé d'un principe actif (PA) et d'excipients, présentés sous une forme galénique (comprimé, gélule, solution injectable, pommade). La biodisponibilité mesure la fraction de PA atteignant la circulation systémique sous forme inchangée.",
     "Le principe actif agit le plus souvent en se liant à une cible (récepteur, enzyme, canal ionique). Un agoniste active le récepteur, un antagoniste bloque l'action de l'agoniste. La relation dose-effet est généralement sigmoïde.",
     "Les paramètres de la relation dose-effet sont ED50 (dose produisant 50 % de l'effet maximal) et LD50 (dose létale pour 50 % des individus). L'indice thérapeutique = LD50/ED50 : plus il est grand, plus le médicament est sûr.",
     "Le métabolisme hépatique comporte la phase I (oxydation, réduction, hydrolyse — souvent via les cytochromes P450) et la phase II (conjugaison : glucuronidation, sulfatation). L'élimination se fait principalement par le rein (urine) et la bile.",
     "La toxicologie étudie les effets néfastes des substances. On distingue toxicité aiguë (une exposition unique) et toxicité chronique (expositions répétées). Les effets CMR (cancérogènes, mutagènes, reprotoxiques) sont particulièrement surveillés.",
     "La relation dose-effet toxicologique conduit aux notions de NOAEL (dose sans effet observé) et de LOAEL (dose avec effet observé). La dose journalière admissible (DJA ou ADI) = NOAEL / facteur de sécurité (généralement 100 = 10 pour les espèces × 10 pour les individus).",
     "La pharmacopée définit les prescriptions de qualité des médicaments : identité, pureté, dosage, essais de dissolution, stabilité et limites de contaminants. Les normes sont contraignantes pour les laboratoires de contrôle.",
     "En BIOALC, le contrôle qualité du médicament comprend le dosage du principe actif (HPLC, spectroscopie UV), la recherche d'impuretés, les essais de dissolution et de stérilité, le contrôle des résidus de solvants et la stabilité.",
     "La traçabilité des lots, la maîtrise des références certifiées et l'expression du résultat avec son incertitude sont exigées (ISO/IEC 17025, bonnes pratiques de laboratoire)."
    ],
    [
     qcm("Que signifie le sigle ADME ?", ["Absorption, Distribution, Métabolisme, Excrétion", "Analyse, Dosage, Mesure, Essai", "Acide, Dose, Masse, Équilibre", "Activité, Diffusion, Migration, Élimination"], 0,
         "ADME résume le devenir du médicament dans l'organisme : absorption, distribution, métabolisme et excrétion."),
     qcm("Que mesure l'ED50 ?", ["La dose létale", "La dose donnant 50 % de l'effet maximal", "La dose maximale autorisée", "La concentration plasmatique"], 1,
         "ED50 = dose efficace pour 50 % des individus (ou 50 % de l'effet maximal)."),
     qcm("Comment calculer l'indice thérapeutique ?", ["ED50 / LD50", "LD50 / ED50", "LD50 × ED50", "LD50 − ED50"], 1,
         "Indice thérapeutique = LD50/ED50. Une valeur élevée indique une marge de sécurité large."),
     qcm("À quoi sert la phase I du métabolisme ?", ["À conjuguer le médicament", "À oxyder/hydrolyser le médicament", "À l'excréter", "À le stocker"], 1,
         "La phase I (souvent cytochromes P450) oxyde, réduit ou hydrolyse la molécule ; la phase II la conjugue."),
     qcm("Comment obtenir la dose journalière admissible (DJA) ?", ["NOAEL × 100", "NOAEL / 100", "LD50 / 100", "ED50 × 10"], 1,
         "DJA = NOAEL / facteur de sécurité (généralement 100 : 10 pour les espèces et 10 pour les individus)."),
     qcm("Quel est le rôle d'un antagoniste ?", ["Activer le récepteur", "Bloquer le récepteur", "Dégrader le médicament", "Augmenter l'absorption"], 1,
         "L'antagoniste se lie au récepteur sans l'activer et empêche l'agoniste d'agir."),
     qt("Pourquoi la pharmacopée impose-t-elle des essais de dissolution pour un comprimé ?",
        "Parce que la dissolution du principe actif dans le suc gastrique conditionne son absorption et donc sa biodisponibilité. Un comprimé mal dissous peut être inefficace même si son dosage est correct.",
        "Les essais de dissolution sont des essais de routine obligatoires pour la libération des lots."),
     qcm("Un composé a une NOAEL de 10 mg/kg/j. Quelle est sa DJA pour un adulte de 60 kg (facteur 100) ?",
         ["0,1 mg/j", "6 mg/j", "10 mg/j", "60 mg/j"], 1,
         "DJA = 10/100 = 0,1 mg/kg/j ; pour 60 kg : 0,1 × 60 = 6 mg/j.",
         "Évaluation du risque toxicologique d'un résidu dans un produit.", True),
     qcm("Un médicament a une ED50 de 5 mg et une LD50 de 500 mg. Quel est son indice thérapeutique ?",
         ["10", "50", "100", "500"], 2,
         "IT = LD50/ED50 = 500/5 = 100.",
         "Comparaison de la marge de sécurité de deux candidats médicaments.", True),
     qcm("Une solution de principe actif à 2 mg/mL est diluée au 1/100. Quelle est la concentration finale ?",
         ["0,2 mg/mL", "0,02 mg/mL", "2 µg/mL", "20 mg/mL"], 1,
         "C₂ = C₁/F = 2/100 = 0,02 mg/mL, soit 20 µg/mL.",
         "Préparation d'une solution d'étalonnage pour le dosage d'un principe actif.", True)
    ],
    [
     intro("L'idée en une phrase", "La pharmacologie étudie comment le médicament agit et comment l'organisme le traite ; la toxicologie détermine à partir de quelle dose un produit devient dangereux."),
     formule("Sécurité d'emploi", "Indice thérapeutique = LD50 / ED50   ·   DJA = NOAEL / facteur de sécurité", "Facteur de sécurité usuel = 100 (10 espèces × 10 individus) · DJA en mg/kg/j"),
     grille("Les grandes notions", [
         ["Pharmacodynamie", "effet du médicament sur l'organisme", "ED50, récepteurs"],
         ["Pharmacocinétique", "devenir du médicament (ADME)", "biodisponibilité"],
         ["Toxicologie", "effets nocifs et doses critiques", "NOAEL, DJA, LD50"]]),
     liste("Les 4 étapes ADME", [
         "Absorption : passage dans la circulation (biodisponibilité)",
         "Distribution : transport vers les tissus (volume de distribution)",
         "Métabolisme : phase I (oxydation P450) puis phase II (conjugaison)",
         "Excrétion : rein (urine), bile, poumons — demi-vie d'élimination"]),
     etapes("Évaluer la sécurité d'une substance", [
         "Réaliser des études de toxicité aiguë puis chronique",
         "Déterminer la NOAEL et la LOAEL",
         "Appliquer un facteur de sécurité (souvent 100) pour obtenir la DJA",
         "Comparer exposition estimée et DJA (ou dose de référence)",
         "Contrôler la conformité du produit selon la pharmacopée"]),
     attention("⚠️ Les pièges classiques", [
         "Confondre ED50 (effet) et LD50 (létalité)",
         "Oublier que la DJA est exprimée par kg de masse corporelle",
         "Appliquer le facteur de sécurité dans le mauvais sens (division, pas multiplication)",
         "Croire qu'un dosage correct garantit une bonne biodisponibilité",
         "Négliger l'incertitude et la traçabilité des étalons de dosage"]),
     exemples("En chiffres (à savoir refaire)", [
         "<span class=\"cle\">LD50/ED50 = 500/5</span> = 100 (indice thérapeutique)",
         "<span class=\"cle\">NOAEL 10 mg/kg ÷ 100</span> = 0,1 mg/kg/j",
         "<span class=\"cle\">0,1 × 60 kg</span> = 6 mg/j pour un adulte",
         "<span class=\"cle\">2 mg/mL ÷ 100</span> = 0,02 mg/mL",
         "<span class=\"cle\">Phase I / phase II</span> = oxydation / conjugaison"]),
    ],
    [
     sc("1 · Le devenir du médicament (ADME)", """<svg viewBox="0 0 660 165" width="100%" role="img" aria-label="Quatre étapes pharmacocinétiques absorption distribution métabolisme excrétion">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
      <g font-size="11" text-anchor="middle">
        <rect x="10" y="46" width="142" height="62" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="81" y="70" fill="var(--ac)" font-weight="bold">A · Absorption</text><text x="81" y="90" fill="var(--fg)">biodisponibilité</text>
        <line x1="154" y1="77" x2="170" y2="77" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="174" y="46" width="142" height="62" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="245" y="70" fill="var(--ac)" font-weight="bold">D · Distribution</text><text x="245" y="90" fill="var(--fg)">vers les tissus</text>
        <line x1="318" y1="77" x2="334" y2="77" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="338" y="46" width="142" height="62" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="409" y="70" fill="var(--ac)" font-weight="bold">M · Métabolisme</text><text x="409" y="90" fill="var(--fg)">P450, conjugaison</text>
        <line x1="482" y1="77" x2="498" y2="77" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="502" y="46" width="146" height="62" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="575" y="70" fill="var(--ac)" font-weight="bold">E · Excrétion</text><text x="575" y="90" fill="var(--fg)">rein, bile</text>
      </g>
      <text x="330" y="140" text-anchor="middle" fill="var(--dim)" font-size="11">La demi-vie d'élimination conditionne la fréquence d'administration</text>
     </svg>"""),
     sc("2 · Courbe dose-effet et indice thérapeutique", """<svg viewBox="0 0 660 200" width="100%" role="img" aria-label="Courbes dose-effet et dose-létalité avec ED50 et LD50">
      <line x1="55" y1="170" x2="430" y2="170" stroke="var(--dim)" stroke-width="2"/><line x1="55" y1="170" x2="55" y2="30" stroke="var(--dim)" stroke-width="2"/>
      <text x="30" y="36" fill="var(--fg)" font-size="11">%</text><text x="380" y="188" fill="var(--fg)" font-size="11">dose (log)</text>
      <path d="M70 168 C140 166 180 150 220 110 C260 70 310 45 400 40" fill="none" stroke="var(--ac)" stroke-width="3"/>
      <path d="M160 168 C230 166 270 150 310 110 C350 70 390 45 425 42" fill="none" stroke="var(--warn)" stroke-width="3"/>
      <line x1="215" y1="100" x2="215" y2="170" stroke="var(--ac)" stroke-width="1.5" stroke-dasharray="4 3"/><text x="200" y="188" fill="var(--ac)" font-size="11">ED50</text>
      <line x1="305" y1="112" x2="305" y2="170" stroke="var(--warn)" stroke-width="1.5" stroke-dasharray="4 3"/><text x="292" y="188" fill="var(--warn)" font-size="11">LD50</text>
      <line x1="55" y1="100" x2="215" y2="100" stroke="var(--ac)" stroke-width="1" stroke-dasharray="3 3"/>
      <rect x="452" y="48" width="192" height="120" rx="8" fill="var(--card2)" stroke="var(--dim)"/>
      <text x="466" y="72" fill="var(--ac)" font-size="12" font-weight="bold">Marge de sécurité</text>
      <text x="466" y="98" fill="var(--fg)" font-size="11">IT = LD50 / ED50</text>
      <text x="466" y="122" fill="var(--fg)" font-size="11">500 / 5 = 100</text>
      <text x="466" y="146" fill="var(--dim)" font-size="10">IT élevé = médicament sûr</text>
     </svg>"""),
     sc("3 · De la NOAEL à la DJA", """<svg viewBox="0 0 660 165" width="100%" role="img" aria-label="Calcul de la dose journalière admissible à partir de la NOAEL">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
      <g font-size="11" text-anchor="middle">
        <rect x="14" y="48" width="160" height="58" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="94" y="72" fill="var(--ac)" font-weight="bold">NOAEL</text><text x="94" y="92" fill="var(--fg)">10 mg/kg/j</text>
        <line x1="176" y1="77" x2="222" y2="77" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/><text x="199" y="68" fill="var(--warn)" font-size="10">÷100</text>
        <rect x="226" y="48" width="160" height="58" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="306" y="72" fill="var(--ac)" font-weight="bold">DJA</text><text x="306" y="92" fill="var(--fg)">0,1 mg/kg/j</text>
        <line x1="388" y1="77" x2="434" y2="77" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/><text x="411" y="68" fill="var(--warn)" font-size="10">×60 kg</text>
        <rect x="438" y="48" width="200" height="58" rx="8" fill="var(--card2)" stroke="var(--warn)"/><text x="538" y="72" fill="var(--warn)" font-weight="bold">Dose admissible</text><text x="538" y="92" fill="var(--fg)">6 mg/j</text>
      </g>
      <text x="330" y="138" text-anchor="middle" fill="var(--dim)" font-size="11">Facteur 100 = 10 (variation entre espèces) × 10 (variation entre individus)</text>
     </svg>""")
    ]
))

# ============================================================ FICHE 10
FICHES.append(mk(
    ["BTS2"], BIO, "Chapitre 10 · Physiologie végétale", SRC_BIO,
    [
     "La photosynthèse convertit l'énergie lumineuse en énergie chimique. Bilan : 6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂ (en présence de chlorophylle et de lumière). Elle se déroule dans le chloroplaste, en deux phases.",
     "La phase claire (thylakoïdes) capte la lumière, photolyse l'eau (dégagement d'O₂) et produit ATP et NADPH. La phase sombre ou cycle de Calvin (stroma) fixe le CO₂ grâce à la Rubisco et synthétise les glucides en consommant ATP et NADPH.",
     "La respiration cellulaire est le processus inverse : C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + ATP. Elle a lieu dans les mitochondries et fournit l'énergie nécessaire à la cellule, y compris la nuit.",
     "Le transport des substances repose sur deux tissus : le xylème conduit la sève brute (eau et sels minéraux) des racines vers les feuilles, sous l'effet de la transpiration ; le phloème transporte la sève élaborée (sucres) des sources vers les puits.",
     "Les hormones végétales régulent la croissance et le développement : auxine (élongation, phototropisme), cytokinines (division cellulaire), gibbérellines (germination, élongation), acide abscissique (dormance, fermeture des stomates), éthylène (maturation des fruits).",
     "Le métabolisme secondaire produit des composés spécifiques : polyphénols, flavonoïdes, alcaloïdes, terpènes, pigments (anthocyanes, caroténoïdes). Ce sont souvent des composés d'intérêt pour l'analyse (arômes, antioxydants, principes actifs).",
     "Les facteurs environnementaux (lumière, température, disponibilité en eau, CO₂) modulent la photosynthèse et la croissance. Le stress (sécheresse, froid, UV) déclenche des réponses biochimiques mesurables (accumulation de proline, de polyphénols).",
     "La stœchiométrie de la photosynthèse permet des calculs : 6 mol de CO₂ donnent 1 mol de glucose (180 g) et 6 mol d'O₂ (soit 6 × 22,4 L = 134,4 L dans les conditions normales).",
     "Le dosage des composés végétaux utilise la spectrophotométrie (polyphénols par Folin-Ciocalteu à 765 nm, anthocyanes à 520 nm, chlorophylle à 645/663 nm), la HPLC et les tests d'activité antioxydante (DPPH, ABTS).",
     "Applications BIOALC : contrôle des matières premières végétales, dosage de composés d'intérêt, authentification et traçabilité des espèces, recherche de résidus de pesticides, contrôle des OGM et suivi de la maturation."
    ],
    [
     qcm("Quel est le bilan de la photosynthèse ?", ["6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂", "C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O", "6 O₂ + 6 H₂O → 6 CO₂ + C₆H₁₂O₆", "CO₂ + H₂O → CH₄ + O₂"], 0,
         "La photosynthèse consomme CO₂ et eau pour produire glucose et oxygène, grâce à la lumière et à la chlorophylle."),
     qcm("Où se déroule le cycle de Calvin ?", ["Dans les thylakoïdes", "Dans le stroma du chloroplaste", "Dans la mitochondrie", "Dans le noyau"], 1,
         "Les réactions claires ont lieu dans les thylakoïdes ; le cycle de Calvin (fixation du CO₂) dans le stroma."),
     qcm("Quel tissu conduit la sève brute ?", ["Le phloème", "Le xylème", "L'épiderme", "Le cambium"], 1,
         "Le xylème transporte l'eau et les sels minéraux des racines vers les feuilles ; le phloème transporte les sucres."),
     qcm("Quelle hormone est liée à la maturation des fruits ?", ["L'auxine", "L'éthylène", "L'ABA", "La cytokinine"], 1,
         "L'éthylène, gazeux, accélère la maturation des fruits climactériques."),
     qcm("Quel pigment absorbe la lumière pour la photosynthèse ?", ["L'hémoglobine", "La chlorophylle", "La mélanine", "Le collagène"], 1,
         "La chlorophylle (verte) absorbe surtout le rouge et le bleu, et réfléchit le vert."),
     qcm("Que mesure le test DPPH ?", ["La teneur en protéines", "L'activité antioxydante", "Le pH", "La conductivité"], 1,
         "Le DPPH est un radical libre dont la décroissance d'absorbance mesure le pouvoir antioxydant d'un extrait."),
     qt("Pourquoi la respiration a-t-elle lieu aussi la nuit ?",
         "Parce que la photosynthèse s'arrête en l'absence de lumière, mais la cellule végétale a continuellement besoin d'ATP pour ses fonctions vitales. La respiration, indépendante de la lumière, fournit cet ATP en oxydant les réserves glucidiques.",
         "Le bilan respiratoire est l'inverse du bilan photosynthétique."),
     qcm("Combien de litres de CO₂ sont nécessaires pour former 1 mole de glucose (6 × 22,4 L/mol) ?",
         ["22,4 L", "112 L", "134,4 L", "6 L"], 2,
         "6 mol de CO₂ × 22,4 L/mol = 134,4 L de CO₂ pour 1 mol (180 g) de glucose.",
         "Calcul stœchiométrique du bilan de la photosynthèse.", True),
     qcm("Un dosage de polyphénols donne A = 0,400 avec une droite A = 0,020 × c (c en mg/L), après dilution 1/10. Quelle est la concentration initiale ?",
         ["20 mg/L", "200 mg/L", "2 mg/L", "400 mg/L"], 1,
         "c (dilué) = 0,400/0,020 = 20 mg/L ; concentration initiale = 20 × 10 = 200 mg/L.",
         "Dosage spectrophotométrique des polyphénols d'un extrait végétal (Folin-Ciocalteu).", True),
     qcm("Un extrait est dilué au 1/25 et donne A260 = 0,400. En prenant 40 µg/mL par DO pour l'ARN, quelle est la concentration initiale ?",
         ["400 µg/mL", "40 µg/mL", "1 000 µg/mL", "160 µg/mL"], 0,
         "C = 0,400 × 40 × 25 = 400 µg/mL (facteur de dilution inclus).",
         "Quantification d'un acide nucléique extrait d'un tissu végétal.", True)
    ],
    [
     intro("L'idée en une phrase", "La plante fabrique sa matière organique par photosynthèse, la respire pour obtenir de l'énergie, et transporte l'eau (xylème) et les sucres (phloème) dans tout son organisme."),
     formule("Les bilans", "Photosynthèse : 6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂", "Respiration : C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + ATP · 6 mol CO₂ = 134,4 L (CNTP)"),
     grille("Les deux phases", [
         ["Phase claire", "thylakoïdes, lumière", "ATP, NADPH, O₂"],
         ["Cycle de Calvin", "stroma, Rubisco", "fixation CO₂, glucides"],
         ["Respiration", "mitochondries", "ATP, CO₂, H₂O"]]),
     liste("Hormones et rôles", [
         "Auxine : élongation, phototropisme, dominance apicale",
         "Cytokinines : division cellulaire, levée de dormance",
         "Gibbérellines : germination, élongation des tiges",
         "Acide abscissique : dormance, fermeture des stomates",
         "Éthylène : maturation des fruits, sénescence"]),
     etapes("Analyser un extrait végétal", [
         "Prélever et homogénéiser l'échantillon (feuille, fruit, graine)",
         "Extraire les composés d'intérêt (solvant, ultrasons, macération)",
         "Filtrer, diluer et doser (spectrophotométrie, HPLC)",
         "Corriger par le facteur de dilution et exprimer en mg/g de matière sèche",
         "Comparer à la spécification et tracer les résultats"]),
     attention("⚠️ Les pièges classiques", [
         "Confondre photosynthèse (chloroplaste) et respiration (mitochondrie)",
         "Oublier le facteur de dilution dans un dosage",
         "Croire que la sève élaborée monte dans le xylème",
         "Négliger l'effet du pH et du solvant sur l'absorbance des pigments",
         "Oublier d'exprimer le résultat par gramme de matière sèche"]),
     exemples("En chiffres (à savoir refaire)", [
         "<span class=\"cle\">6 × 22,4 L</span> = 134,4 L de CO₂ / mol de glucose",
         "<span class=\"cle\">A = 0,4, droite 0,020c</span> → 20 mg/L dilué",
         "<span class=\"cle\">20 × 10</span> → 200 mg/L initial",
         "<span class=\"cle\">A260 = 0,4 × 40 × 25</span> → 400 µg/mL",
         "<span class=\"cle\">Folin-Ciocalteu</span> → lecture à 765 nm"]),
    ],
    [
     sc("1 · Photosynthèse et respiration", """<svg viewBox="0 0 660 180" width="100%" role="img" aria-label="Bilan complémentaire photosynthèse et respiration">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
      <text x="16" y="24" fill="var(--ac)" font-size="15" font-weight="bold">Deux bilans complémentaires</text>
      <rect x="16" y="42" width="620" height="52" rx="8" fill="var(--card2)" stroke="var(--ac)"/>
      <text x="30" y="63" fill="var(--ac)" font-size="12" font-weight="bold">Photosynthèse (chloroplaste, lumière)</text>
      <text x="30" y="83" fill="var(--fg)" font-size="13">6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂</text>
      <rect x="16" y="106" width="620" height="52" rx="8" fill="var(--card2)" stroke="var(--warn)"/>
      <text x="30" y="127" fill="var(--warn)" font-size="12" font-weight="bold">Respiration (mitochondrie, nuit et jour)</text>
      <text x="30" y="147" fill="var(--fg)" font-size="13">C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + ATP</text>
      <text x="330" y="176" text-anchor="middle" fill="var(--dim)" font-size="10">6 mol de CO₂ = 6 × 22,4 L = 134,4 L (CNTP)</text>
     </svg>"""),
     sc("2 · Le chloroplaste en deux compartiments", """<svg viewBox="0 0 660 190" width="100%" role="img" aria-label="Chloroplaste avec thylakoïdes phase claire et stroma cycle de Calvin">
      <ellipse cx="180" cy="100" rx="120" ry="62" fill="var(--card2)" stroke="var(--ac)" stroke-width="2"/>
      <g fill="var(--ac)" opacity="0.6"><rect x="110" y="76" width="46" height="16" rx="8"/><rect x="110" y="106" width="46" height="16" rx="8"/><rect x="170" y="76" width="46" height="16" rx="8"/><rect x="170" y="106" width="46" height="16" rx="8"/></g>
      <text x="155" y="66" text-anchor="middle" fill="var(--ac)" font-size="11">thylakoïdes</text>
      <text x="240" y="130" fill="var(--dim)" font-size="11">stroma</text>
      <rect x="330" y="40" width="310" height="66" rx="8" fill="var(--card2)" stroke="var(--ac)"/>
      <text x="344" y="62" fill="var(--ac)" font-size="12" font-weight="bold">Phase claire (thylakoïdes)</text>
      <text x="344" y="84" fill="var(--fg)" font-size="11">lumière + H₂O → O₂ + ATP + NADPH</text>
      <rect x="330" y="118" width="310" height="60" rx="8" fill="var(--card2)" stroke="var(--warn)"/>
      <text x="344" y="140" fill="var(--warn)" font-size="12" font-weight="bold">Cycle de Calvin (stroma)</text>
      <text x="344" y="162" fill="var(--fg)" font-size="11">CO₂ + ATP + NADPH → glucides (Rubisco)</text>
     </svg>"""),
     sc("3 · Xylème et phloème", """<svg viewBox="0 0 660 190" width="100%" role="img" aria-label="Transport de la sève brute par le xylème et de la sève élaborée par le phloème">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
      <text x="16" y="24" fill="var(--ac)" font-size="15" font-weight="bold">Deux réseaux de transport</text>
      <line x1="150" y1="160" x2="150" y2="46" stroke="var(--ac)" stroke-width="8" marker-end="url(#@@a)"/>
      <text x="120" y="100" fill="var(--ac)" font-size="12">XYLÈME</text>
      <text x="40" y="120" fill="var(--fg)" font-size="10">sève brute</text>
      <text x="40" y="138" fill="var(--fg)" font-size="10">eau + sels minéraux</text>
      <line x1="480" y1="46" x2="480" y2="160" stroke="var(--warn)" stroke-width="8" marker-end="url(#@@a)"/>
      <text x="500" y="100" fill="var(--warn)" font-size="12">PHLOÈME</text>
      <text x="520" y="120" fill="var(--fg)" font-size="10">sève élaborée</text>
      <text x="520" y="138" fill="var(--fg)" font-size="10">sucres (sources→puits)</text>
      <text x="150" y="182" text-anchor="middle" fill="var(--dim)" font-size="10">racines → feuilles (transpiration)</text>
      <text x="480" y="182" text-anchor="middle" fill="var(--dim)" font-size="10">feuilles → organes de stockage</text>
      <circle cx="150" cy="165" r="6" fill="var(--dim)"/><circle cx="480" cy="165" r="6" fill="var(--dim)"/>
     </svg>""")
    ]
))

# ============================================================ FICHE 11
FICHES.append(mk(
    ["BTS1", "BTS2"], QUA, "Chapitre 11 · Concepts qualité et norme ISO/IEC 17025", SRC_QUA,
    [
     "La qualité est l'aptitude d'un ensemble de caractéristiques intrinsèques à satisfaire des besoins explicites ou implicites (ISO 9000:2015). Le contrôle qualité vérifie la conformité d'un produit ou d'un résultat ; l'assurance qualité vise à donner la confiance que les exigences seront respectées.",
     "Un système de management de la qualité (SMQ) est l'ensemble des éléments interconnectés qui pilotent la qualité : politique, objectifs, processus, ressources et documents. Il s'appuie sur les 7 principes ISO 9000 : orientation client, leadership, implication du personnel, approche processus, amélioration, prise de décision factuelle, gestion des relations.",
     "La norme NF EN ISO/IEC 17025:2017 (3e édition, confirmée en 2023) fixe les exigences générales de compétence des laboratoires d'essais et d'étalonnage. Elle est la référence pour l'accréditation des laboratoires.",
     "Sa structure comporte 5 chapitres : §4 exigences générales (impartialité, confidentialité), §5 exigences de structure, §6 exigences relatives aux ressources (personnel, installations, équipements, traçabilité métrologique, prestataires), §7 exigences relatives aux processus, §8 exigences du système de management.",
     "Le chapitre 7 couvre la revue des demandes et contrats, le choix et la validation des méthodes, l'échantillonnage, la manipulation des échantillons, les enregistrements techniques, l'incertitude de mesure, la validité des résultats, la communication des résultats, les réclamations et les travaux non conformes.",
     "Le chapitre 8 couvre la documentation du SMQ, la maîtrise des documents et des enregistrements, les risques et opportunités, l'amélioration (8.6), les actions correctives (8.7), les audits internes (8.8) et la revue de direction (8.9).",
     "La norme propose deux options pour le SMQ : l'option A (exigences 8.1 à 8.9 complètes) et l'option B (respect de l'ISO 9001 + paragraphes 8.7 à 8.9 de la 17025).",
     "L'impartialité et l'indépendance du personnel, la confidentialité des informations et la compétence démontrée sont des exigences transversales. La direction est responsable du SMQ et de l'allocation des ressources.",
     "L'accréditation (en France, délivrée par le COFRAC) est la reconnaissance formelle, par un tiers, de la compétence d'un laboratoire pour des essais ou étalonnages donnés, définis dans une portée d'accréditation. Le laboratoire doit prouver sa traçabilité métrologique (§6.5) et participer à des comparaisons interlaboratoires (§7.7).",
     "La fiabilité des résultats repose sur la justesse, la fidélité, la traçabilité, l'incertitude et la maîtrise de toutes les étapes pré-analytique, analytique et post-analytique."
    ],
    [
     qcm("Quelle norme définit les exigences de compétence des laboratoires d'essais ?", ["ISO 9001", "ISO/IEC 17025", "ISO 14001", "ISO 45001"], 1,
         "L'ISO/IEC 17025:2017 est la norme de référence pour l'accréditation des laboratoires d'essais et d'étalonnage."),
     qcm("Combien de chapitres structurants compte l'ISO 17025:2017 ?", ["3", "4", "5", "8"], 2,
         "Les chapitres 4 à 8 : généralités, structure, ressources, processus, système de management."),
     qcm("Quel paragraphe traite des actions correctives ?", ["8.6", "8.7", "8.8", "8.9"], 1,
         "8.7 = actions correctives ; 8.6 = amélioration ; 8.8 = audits internes ; 8.9 = revue de direction."),
     qcm("Que signifie l'option B du SMQ ?", ["ISO 9001 + paragraphes 8.7 à 8.9", "Aucun document", "Audit externe uniquement", "ISO 14001 seule"], 0,
         "L'option B combine la conformité à l'ISO 9001 avec les paragraphes 8.7, 8.8 et 8.9 de l'ISO 17025."),
     qcm("Qui délivre l'accréditation en France ?", ["L'ANSM", "Le COFRAC", "L'INERIS", "La DGCCRF"], 1,
         "Le COFRAC (Comité français d'accréditation) est l'organisme national d'accréditation."),
     qcm("Quel principe ISO 9000 consiste à fonder les décisions sur des données ?", ["Orientation client", "Approche processus", "Prise de décision factuelle", "Leadership"], 2,
         "La prise de décision factuelle repose sur l'analyse et l'évaluation des données et informations."),
     qt("Distinguer contrôle qualité et assurance qualité.",
        "Le contrôle qualité est un ensemble d'opérations visant à vérifier la conformité d'un produit ou d'un résultat (contrôle final). L'assurance qualité est l'ensemble des dispositions mises en œuvre en amont pour donner la confiance que la qualité sera atteinte (prévention, procédures, audits).",
        "Le contrôle détecte les défauts ; l'assurance empêche leur apparition."),
     qcm("Sur 200 analyses réalisées, 12 sont non conformes. Quel est le taux de conformité ?",
         ["88 %", "94 %", "96 %", "12 %"], 2,
         "Conformes = 200 − 12 = 188 ; taux = 188/200 × 100 = 94 %.",
         "Suivi des indicateurs qualité d'un laboratoire accrédité.", True),
     qcm("Une mesure a une incertitude-type u = 0,3 mg/L. Quelle est l'incertitude élargie U pour k = 2 ?",
         ["0,15 mg/L", "0,3 mg/L", "0,6 mg/L", "1,5 mg/L"], 2,
         "U = k × u = 2 × 0,3 = 0,6 mg/L (niveau de confiance d'environ 95 %).",
         "Expression du résultat conformément aux exigences de validité des résultats (§7.6).", True),
     qcm("Un laboratoire réalise 150 essais par semaine et 6 sont refaits. Quel est le taux de reruns ?",
         ["2 %", "4 %", "6 %", "144 %"], 1,
         "Taux de reruns = 6/150 × 100 = 4 %.",
         "Indicateur de pilotage de la productivité et de la qualité des analyses.", True)
    ],
    [
     intro("L'idée en une phrase", "L'ISO/IEC 17025 est la norme qui dit comment un laboratoire doit organiser ses ressources et ses processus pour produire des résultats compétents, impartiaux et traçables."),
     formule("Qualité et risque", "Taux de conformité = conformes / total × 100   ·   U = k × u", "k = 2 → niveau de confiance ≈ 95 % · SMQ = politique + processus + ressources + documents"),
     grille("Les 5 chapitres", [
         ["§4", "généralités", "impartialité, confidentialité"],
         ["§5", "structure", "organisation, responsabilités"],
         ["§6", "ressources", "personnel, locaux, équipements, traçabilité"],
         ["§7", "processus", "contrat, méthodes, échantillons, résultats"],
         ["§8", "SMQ", "documents, risques, audits, amélioration"]]),
     liste("7 principes de management (ISO 9000)", [
         "Orientation client · leadership · implication du personnel",
         "Approche processus · amélioration continue",
         "Prise de décision factuelle · gestion des relations"]),
     etapes("Construire un SMQ conforme", [
         "Définir la politique et les objectifs qualité avec la direction",
         "Cartographier les processus et identifier les exigences (§4 à §8)",
         "Documenter procédures et enregistrements, maîtriser les versions",
         "Maîtriser les risques, former le personnel, qualifier les équipements",
         "Auditer, mesurer les indicateurs et conduire la revue de direction"]),
     attention("⚠️ Les pièges classiques", [
         "Confondre certification ISO 9001 et accréditation ISO 17025",
         "Croire que l'accréditation couvre toute l'activité : elle est limitée à la portée",
         "Oublier l'impartialité et la confidentialité (exigences §4)",
         "Négliger la traçabilité métrologique (§6.5)",
         "Confondre incertitude-type u et incertitude élargie U = k·u"]),
     exemples("En chiffres (à savoir refaire)", [
         "<span class=\"cle\">(200−12)/200</span> = 94 % de conformité",
         "<span class=\"cle\">6/150</span> = 4 % de reruns",
         "<span class=\"cle\">U = 2 × 0,3</span> = 0,6 mg/L",
         "<span class=\"cle\">ISO 17025:2017</span> = 3e édition",
         "<span class=\"cle\">§8.7 / 8.8 / 8.9</span> = correctives / audits / revue"]),
    ],
    [
     sc("1 · Les 5 chapitres de l'ISO 17025", """<svg viewBox="0 0 660 190" width="100%" role="img" aria-label="Structure de la norme ISO 17025 en cinq chapitres">
      <g font-size="11" text-anchor="middle">
        <rect x="12" y="44" width="122" height="72" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="73" y="68" fill="var(--ac)" font-weight="bold">§4 Généralités</text><text x="73" y="88" fill="var(--fg)">impartialité</text><text x="73" y="104" fill="var(--fg)">confidentialité</text>
        <rect x="142" y="44" width="122" height="72" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="203" y="68" fill="var(--ac)" font-weight="bold">§5 Structure</text><text x="203" y="88" fill="var(--fg)">organisation</text><text x="203" y="104" fill="var(--fg)">responsabilités</text>
        <rect x="272" y="44" width="122" height="72" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="333" y="68" fill="var(--ac)" font-weight="bold">§6 Ressources</text><text x="333" y="88" fill="var(--fg)">personnel, locaux</text><text x="333" y="104" fill="var(--fg)">équipements, traçabilité</text>
        <rect x="402" y="44" width="122" height="72" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="463" y="68" fill="var(--ac)" font-weight="bold">§7 Processus</text><text x="463" y="88" fill="var(--fg)">contrat, méthodes</text><text x="463" y="104" fill="var(--fg)">échantillons, résultats</text>
        <rect x="532" y="44" width="116" height="72" rx="8" fill="var(--card2)" stroke="var(--warn)"/><text x="590" y="68" fill="var(--warn)" font-weight="bold">§8 SMQ</text><text x="590" y="88" fill="var(--fg)">documents, risques</text><text x="590" y="104" fill="var(--fg)">audits, amélioration</text>
      </g>
      <text x="330" y="148" text-anchor="middle" fill="var(--dim)" font-size="11">Chaque exigence doit être documentée, mise en œuvre et prouvée par des enregistrements</text>
      <text x="330" y="172" text-anchor="middle" fill="var(--warn)" font-size="11">Accréditation COFRAC = reconnaissance formelle de compétence (portée définie)</text>
     </svg>"""),
     sc("2 · Le cycle PDCA", """<svg viewBox="0 0 660 185" width="100%" role="img" aria-label="Roue de Deming Plan Do Check Act appliquée au SMQ">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
      <path d="M300 40 C420 30 500 60 500 92 C500 130 420 160 320 150" fill="none" stroke="var(--ac)" stroke-width="3" marker-end="url(#@@a)"/>
      <path d="M320 150 C200 160 130 130 130 95 C130 60 200 32 300 40" fill="none" stroke="var(--ac)" stroke-width="3" marker-end="url(#@@a)"/>
      <text x="320" y="26" text-anchor="middle" fill="var(--ac)" font-size="12" font-weight="bold">PLAN — planifier</text>
      <text x="526" y="96" fill="var(--ac)" font-size="12" font-weight="bold">DO — faire</text>
      <text x="320" y="174" text-anchor="middle" fill="var(--ac)" font-size="12" font-weight="bold">ACT — agir</text>
      <text x="16" y="96" fill="var(--ac)" font-size="12" font-weight="bold">CHECK — vérifier</text>
      <text x="320" y="92" text-anchor="middle" fill="var(--dim)" font-size="11">Amélioration continue</text>
      <text x="320" y="112" text-anchor="middle" fill="var(--dim)" font-size="10">objectifs · risques · indicateurs</text>
     </svg>"""),
     sc("3 · Chaîne de confiance du résultat", """<svg viewBox="0 0 660 165" width="100%" role="img" aria-label="Chaîne de confiance : personnel méthodes équipements traçabilité enregistrements">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
      <g font-size="10" text-anchor="middle">
        <rect x="10" y="50" width="112" height="54" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="66" y="74" fill="var(--ac)" font-weight="bold">Personnel</text><text x="66" y="92" fill="var(--fg)">compétence</text>
        <line x1="124" y1="77" x2="144" y2="77" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="148" y="50" width="112" height="54" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="204" y="74" fill="var(--ac)" font-weight="bold">Méthodes</text><text x="204" y="92" fill="var(--fg)">validées</text>
        <line x1="262" y1="77" x2="282" y2="77" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="286" y="50" width="112" height="54" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="342" y="74" fill="var(--ac)" font-weight="bold">Équipements</text><text x="342" y="92" fill="var(--fg)">qualifiés</text>
        <line x1="400" y1="77" x2="420" y2="77" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="424" y="50" width="112" height="54" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="480" y="74" fill="var(--ac)" font-weight="bold">Traçabilité</text><text x="480" y="92" fill="var(--fg)">au SI (§6.5)</text>
        <line x1="538" y1="77" x2="558" y2="77" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="562" y="50" width="88" height="54" rx="8" fill="var(--card2)" stroke="var(--warn)"/><text x="606" y="74" fill="var(--warn)" font-weight="bold">Résultat</text><text x="606" y="92" fill="var(--fg)">+ incertitude</text>
      </g>
      <text x="330" y="140" text-anchor="middle" fill="var(--dim)" font-size="11">Tous les maillons doivent être documentés et maîtrisés pour garantir la validité du résultat</text>
     </svg>""")
    ]
))
