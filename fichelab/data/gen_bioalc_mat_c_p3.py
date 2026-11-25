# -*- coding: utf-8 -*-
# Fiches 5 à 8 — exécuté depuis gen_bioalc_mat_c.py

# ============================================================ FICHE 5
FICHES.append(mk(
    ["BTS1"], BIO, "Chapitre 5 · Électrophorèse des acides nucléiques", SRC_BIO,
    [
     "L'électrophorèse sépare les acides nucléiques selon leur taille. Le squelette phosphate porte des charges négatives : dans un champ électrique, les molécules migrent vers l'anode (+) à travers un gel qui joue le rôle de tamis moléculaire.",
     "Le gel d'agarose est utilisé pour les fragments de 100 pb à 25 kb. Sa concentration détermine le pouvoir de résolution : 0,5 % pour 15–30 kb, 1 % pour 500 pb–8 kb, 2 % pour les fragments < 200 pb. Le polyacrylamide (PAGE) sert aux petits fragments (< 1 kb) et au séquençage.",
     "Plus un fragment est court, plus il migre vite et loin. La distance parcourue est proportionnelle au logarithme décroissant du nombre de paires de bases : c'est cette relation qui permet de déterminer une taille par comparaison à un marqueur (ladder).",
     "Le tampon de migration (TAE : Tris-acétate-EDTA, ou TBE : Tris-borate-EDTA) conduit le courant et maintient le pH vers 8, où les acides nucléiques sont ionisés. Le même tampon doit servir à couler le gel et à remplir la cuve.",
     "Le tampon d'échantillon contient de la glycérine (la densité fait tomber l'échantillon dans le puits) et des colorants de migration : bleu de bromophénol (~300–500 pb) et xylène cyanol (~2–4 kb), qui permettent de suivre l'avancée.",
     "La tension recommandée est de 5 à 10 V/cm de distance entre électrodes. Une tension trop élevée provoque un échauffement, des bandes « sourires » et une mauvaise résolution ; une tension trop faible allonge le temps et diffuse les bandes.",
     "La révélation se fait par intercalation d'un colorant fluorescent : bromure d'éthidium (orange sous UV, mutagène) ou alternatives plus sûres (SYBR Safe, GelRed). Un marqueur de taille déposé dans une piste permet d'estimer la taille des bandes.",
     "La conformation influence la migration : un ADN supercoïlé (covalently closed circular) migre plus vite qu'un ADN linéaire de même taille, lui-même plus vite qu'un ADN nicked (coupé sur un brin).",
     "L'intensité d'une bande donne une estimation semi-quantitative de la quantité d'ADN (à comparer à une gamme). Pour un dosage précis, on préférera la spectrophotométrie ou la fluorimétrie.",
     "Applications BIOALC : contrôle d'un produit de PCR (présence et taille attendues), analyse de profils de restriction, vérification de l'intégrité d'un extrait, purification d'un fragment, identification d'espèce par RFLP."
    ],
    [
     qcm("Vers quel pôle migre l'ADN ?", ["Vers la cathode (−)", "Vers l'anode (+)", "Il ne migre pas", "Vers le puits"], 1,
         "Les phosphates sont négatifs : l'ADN est attiré par l'anode, le pôle positif situé à l'opposé des puits."),
     qcm("Quelle concentration d'agarose pour séparer des fragments de 100–500 pb ?", ["0,5 %", "1 %", "2 %", "5 %"], 2,
         "Plus les fragments sont petits, plus le gel doit être concentré : 2 % pour < 200 pb, 1 % pour 500 pb–8 kb."),
     qcm("Quel tampon est couramment utilisé pour un gel d'agarose ?", ["TAE ou TBE", "Tampon phosphate salin", "Eau pure", "Tampon Tris-HCl seul"], 0,
         "TAE (Tris-acétate-EDTA) et TBE (Tris-borate-EDTA) conduisent le courant et maintiennent un pH ≈ 8."),
     qcm("Que faire pour suivre la migration à l'œil nu ?", ["Ajouter du glycérol seul", "Ajouter un colorant de migration", "Éteindre le courant", "Refroidir le gel"], 1,
         "Les colorants (bleu de bromophénol, xylène cyanol) migrent avec l'ADN et signalent la progression."),
     qcm("Quel est l'effet d'une tension trop élevée ?", ["Meilleure résolution", "Bandes sourires et échauffement", "Migration plus lente", "Aucun effet"], 1,
         "Une tension excessive échauffe le tampon, déforme les bandes (« smiling ») et réduit la résolution."),
     qcm("Quelle est la relation entre distance de migration et taille ?", ["Distance ∝ taille", "Distance ∝ log(taille)", "Distance ∝ −log(taille)", "Aucune relation"], 2,
         "La distance est proportionnelle au logarithme décroissant du nombre de paires de bases."),
     qt("Pourquoi dépose-t-on un marqueur de taille (ladder) sur le gel ?",
        "Parce qu'il contient des fragments de tailles connues. En traçant la courbe log(taille) = f(distance) avec le ladder, on déduit la taille des fragments inconnus de l'échantillon.",
        "Sans marqueur, on ne peut pas convertir une distance de migration en nombre de paires de bases."),
     qcm("La distance entre les électrodes est de 10 cm et le gradient recommandé est 5 V/cm. Quelle tension régler ?",
         ["5 V", "25 V", "50 V", "100 V"], 2,
         "Tension = gradient × distance = 5 V/cm × 10 cm = 50 V.",
         "Paramétrage du générateur avant une migration sur gel d'agarose.", True),
     qcm("Un ladder 100, 200, 400, 800 pb est déposé. Une bande inconnue migre exactement comme la bande de 400 pb. Quelle est sa taille ?",
         ["100 pb", "200 pb", "400 pb", "800 pb"], 2,
         "La comparaison directe avec le marqueur donne 400 pb ; entre deux repères, on interpole sur log(taille).",
         "Lecture d'un gel après électrophorèse d'un produit de PCR.", True),
     qcm("Un gel à 1 % sépare 500 pb–8 kb. Pour un fragment de 150 pb, quelle concentration choisir ?",
         ["0,5 %", "0,8 %", "1,5–2 %", "3 %"], 2,
         "Un gel plus concentré (1,5–2 %) offre des pores plus petits, adaptés aux fragments courts.",
         "Choix de la concentration d'agarose selon la taille attendue de l'amplicon.", True)
    ],
    [
     intro("L'idée en une phrase", "L'ADN est négatif : il migre vers le pôle positif à travers un gel dont les pores retiennent les gros fragments plus que les petits."),
     formule("Migration et tension", "distance ∝ −log(taille en pb)   ·   U = gradient (V/cm) × distance entre électrodes", "Agarose 0,5–2 % · TAE ou TBE · 5–10 V/cm · révélation aux UV"),
     grille("Choisir son gel", [
         ["0,5 %", "15–30 kb", "gros fragments"],
         ["1 %", "500 pb – 8 kb", "usage courant"],
         ["2 %", "&lt; 200 pb", "petits fragments / Page pour &lt; 1 kb"]]),
     liste("Les composants d'une migration", [
         "Gel d'agarose + tampon TAE/TBE (même tampon pour le coulage et la cuve)",
         "Puits près de la cathode ; anode à l'opposé",
         "Tampon d'échantillon : glycérine + bleu de bromophénol / xylène cyanol",
         "Marqueur de taille + colorant fluorescent (BrEt, SYBR Safe, GelRed)"]),
     etapes("Réaliser un gel", [
         "Faire fondre l'agarose dans le tampon, couler avec un peigne, laisser prendre",
         "Mélanger les échantillons au tampon de charge et déposer dans les puits",
         "Régler la tension (5–10 V/cm) et migrer jusqu'à 60–70 % de la longueur",
         "Révéler sous UV (avec protection) et photographier le gel",
         "Comparer aux marqueurs et estimer tailles et quantités"]),
     attention("⚠️ Les pièges classiques", [
         "Inverser les électrodes : l'ADN partirait hors du gel",
         "Utiliser un tampon différent pour le gel et la cuve",
         "Tension trop forte → bandes sourires et échauffement",
         "Bromure d'éthidium = mutagène : gants, écran UV, déchets dédiés",
         "Oublier le marqueur de taille : impossible de quantifier la taille"]),
     exemples("En chiffres (à savoir refaire)", [
         "<span class=\"cle\">5 V/cm × 10 cm</span> = 50 V",
         "<span class=\"cle\">1 % d'agarose</span> → 500 pb–8 kb",
         "<span class=\"cle\">2 % d'agarose</span> → &lt; 200 pb",
         "<span class=\"cle\">bleu de bromophénol</span> ≈ 300–500 pb",
         "<span class=\"cle\">distance ∝ −log(pb)</span> → interpolation au ladder"]),
    ],
    [
     sc("1 · Principe de la migration", """<svg viewBox="0 0 660 180" width="100%" role="img" aria-label="Cuve d'électrophorèse avec puits cathode anode et migration des fragments">
      <rect x="40" y="40" width="480" height="100" rx="6" fill="var(--card2)" stroke="var(--dim)"/>
      <text x="56" y="60" fill="var(--warn)" font-size="12">− Cathode</text><text x="452" y="60" fill="var(--ac)" font-size="12">Anode +</text>
      <g fill="var(--dim)"><rect x="70" y="72" width="12" height="22" rx="2"/><rect x="130" y="72" width="12" height="22" rx="2"/><rect x="190" y="72" width="12" height="22" rx="2"/><rect x="250" y="72" width="12" height="22" rx="2"/></g>
      <g stroke="var(--ac)" stroke-width="2.5"><line x1="76" y1="100" x2="300" y2="100"/><line x1="136" y1="100" x2="430" y2="100"/><line x1="196" y1="100" x2="250" y2="100"/><line x1="256" y1="100" x2="360" y2="100"/></g>
      <text x="150" y="130" fill="var(--dim)" font-size="10">petits fragments → loin</text>
      <text x="320" y="130" fill="var(--dim)" font-size="10">gros fragments → près des puits</text>
      <line x1="300" y1="100" x2="460" y2="100" stroke="var(--warn)" stroke-width="1.5" marker-end="url(#@@a)"/>
      <rect x="540" y="52" width="106" height="76" rx="8" fill="var(--card2)" stroke="var(--ac)"/>
      <text x="593" y="76" text-anchor="middle" fill="var(--ac)" font-size="11" font-weight="bold">Tamis</text>
      <text x="593" y="96" text-anchor="middle" fill="var(--fg)" font-size="10">le gel retient</text>
      <text x="593" y="112" text-anchor="middle" fill="var(--fg)" font-size="10">les gros fragments</text>
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--warn)"/></marker></defs>
     </svg>"""),
     sc("2 · Lecture d'un gel avec marqueur", """<svg viewBox="0 0 660 190" width="100%" role="img" aria-label="Gel d'agarose avec puits, ladder et bandes d'échantillons">
      <text x="16" y="24" fill="var(--ac)" font-size="15" font-weight="bold">Gel révélé : comparer aux marqueurs</text>
      <rect x="30" y="40" width="600" height="120" rx="6" fill="var(--card2)" stroke="var(--dim)"/>
      <g fill="var(--dim)"><rect x="60" y="52" width="40" height="10" rx="2"/><rect x="180" y="52" width="40" height="10" rx="2"/><rect x="300" y="52" width="40" height="10" rx="2"/><rect x="420" y="52" width="40" height="10" rx="2"/></g>
      <g stroke="var(--ac)" stroke-width="4"><line x1="65" y1="78" x2="95" y2="78"/><line x1="65" y1="98" x2="95" y2="98"/><line x1="65" y1="118" x2="95" y2="118"/><line x1="65" y1="142" x2="95" y2="142"/></g>
      <g stroke="var(--warn)" stroke-width="4"><line x1="185" y1="98" x2="215" y2="98"/><line x1="305" y1="118" x2="335" y2="118"/><line x1="425" y1="142" x2="455" y2="142"/></g>
      <g fill="var(--dim)" font-size="10"><text x="100" y="82">800 pb</text><text x="100" y="102">400 pb</text><text x="100" y="122">200 pb</text><text x="100" y="146">100 pb</text></g>
      <text x="200" y="180" fill="var(--warn)" font-size="10">échantillon A</text><text x="320" y="180" fill="var(--warn)" font-size="10">échantillon B</text>
      <text x="440" y="180" fill="var(--warn)" font-size="10">échantillon C</text>
     </svg>"""),
     sc("3 · Courbe taille / distance", """<svg viewBox="0 0 660 190" width="100%" role="img" aria-label="Courbe du logarithme de la taille en fonction de la distance de migration">
      <line x1="60" y1="165" x2="440" y2="165" stroke="var(--dim)" stroke-width="2"/><line x1="60" y1="165" x2="60" y2="30" stroke="var(--dim)" stroke-width="2"/>
      <text x="20" y="36" fill="var(--fg)" font-size="11">log(pb)</text><text x="390" y="183" fill="var(--fg)" font-size="11">distance (cm)</text>
      <line x1="90" y1="50" x2="410" y2="150" stroke="var(--ac)" stroke-width="3"/>
      <g fill="var(--ac)"><circle cx="110" cy="57" r="4"/><circle cx="210" cy="88" r="4"/><circle cx="310" cy="119" r="4"/><circle cx="400" cy="147" r="4"/></g>
      <line x1="260" y1="165" x2="260" y2="104" stroke="var(--warn)" stroke-width="1.5" stroke-dasharray="4 3"/>
      <line x1="60" y1="104" x2="260" y2="104" stroke="var(--warn)" stroke-width="1.5" stroke-dasharray="4 3"/>
      <text x="266" y="100" fill="var(--warn)" font-size="11">taille inconnue</text>
      <rect x="462" y="48" width="184" height="118" rx="8" fill="var(--card2)" stroke="var(--dim)"/>
      <text x="476" y="70" fill="var(--ac)" font-size="12" font-weight="bold">Interpolation</text>
      <text x="476" y="94" fill="var(--fg)" font-size="11">1. tracer log(pb)</text>
      <text x="476" y="116" fill="var(--fg)" font-size="11">2. lire la droite</text>
      <text x="476" y="138" fill="var(--fg)" font-size="11">3. en déduire la taille</text>
      <text x="476" y="158" fill="var(--dim)" font-size="10">R² proche de 1</text>
     </svg>""")
    ]
))

# ============================================================ FICHE 6
FICHES.append(mk(
    ["BTS2"], BIO, "Chapitre 6 · Séquençage des acides nucléiques", SRC_BIO,
    [
     "Le séquençage détermine l'ordre des nucléotides d'une molécule d'ADN. La méthode Sanger (1977), dite « didéoxy », utilise des didéoxynucléotides (ddNTP) qui terminent l'élongation : l'incorporation d'un ddNTP marqué arrête la synthèse.",
     "Les produits sont des fragments de tailles 1, 2, 3… nucléotides, séparés par électrophorèse capillaire. Un laser lit la couleur du marqueur à la sortie : le chromatogramme affiche un pic coloré par base (A, C, G, T). La lecture fiable couvre environ 600–800 pb.",
     "Dans une réaction Sanger « classique », un seul ddNTP par tube ; avec les ddNTP marqués par 4 fluorophores différents, toutes les terminaisons peuvent être lues dans un même tube.",
     "Le séquençage haut débit (NGS) parallélise des millions de réactions. Les technologies courantes : séquençage par synthèse (Illumina, lectures courtes 50–300 pb), nanopore (Oxford Nanopore, lectures longues), Ion Torrent (détection de protons).",
     "Le flux NGS comprend : préparation de la bibliothèque (fragmentation + adaptateurs), amplification clonale ou amplification en émulsion, séquençage cyclique, puis analyse bioinformatique (démultiplexage, alignement sur une référence, appel de variants).",
     "La qualité d'une base est donnée par le score de Phred : Q = −10 × log₁₀(P(erreur)). Un score Q30 correspond à une probabilité d'erreur de 10⁻³, soit 1 erreur pour 1 000 bases ; Q40 → 1 erreur pour 10 000.",
     "La profondeur (couverture) est le nombre moyen de lectures couvrant une position. Une couverture de 30× signifie que chaque base est lue 30 fois en moyenne : elle conditionne la fiabilité de l'appel de variants.",
     "Le nombre total de bases à séquencer = taille du génome × couverture souhaitée. Pour un génome bactérien de 5 × 10⁶ pb à 30×, il faut 1,5 × 10⁸ bases, soit par exemple 1,5 million de lectures de 100 pb.",
     "Comparaison : Sanger = lecture longue, faible débit, idéal pour un gène ; NGS = très haut débit, lectures courtes ou longues, pour génomes complets, métagénomique, RNA-seq. La précision individuelle d'une lecture NGS est plus faible mais compensée par la redondance.",
     "Applications BIOALC : identification d'espèces (codes-barres 16S, ITS, COI), recherche de mutations de résistance, authentification d'une espèce dans un produit alimentaire, détection d'OGM, contrôle de la pureté d'une souche.",
     "La bioinformatique est indispensable : alignement (BLAST), assemblage, bases de données (NCBI GenBank), et interprétation des variants avec des outils validés et tracés."
    ],
    [
     qcm("Quel est le principe de la méthode Sanger ?", ["Des ddNTP terminent l'élongation", "Une sonde fluorescente s'hybride", "Un nanomètre mesure le courant", "Une polymerase chauffe le tube"], 0,
         "Les didéoxynucléitudes n'ont pas de 3'-OH : leur incorporation arrête la synthèse et donne des fragments de tailles successives."),
     qcm("Combien de bases peut-on lire en une réaction Sanger standard ?", ["≈ 50", "≈ 600–800", "≈ 10 000", "≈ 10⁶"], 1,
         "La lecture Sanger fiable porte sur environ 600 à 800 paires de bases."),
     qcm("Quelle technologie donne des lectures longues ?", ["Illumina", "Nanopore", "Ion Torrent", "Sanger seul"], 1,
         "Le séquençage nanopore produit des lectures longes (plusieurs kb), utile pour l'assemblage de génomes."),
     qcm("Quel est le score de Phred Q30 ?", ["1 erreur / 10 bases", "1 erreur / 100 bases", "1 erreur / 1 000 bases", "1 erreur / 10 000 bases"], 2,
         "Q = −10 log₁₀(P) ; Q30 → P = 10⁻³, soit 1 erreur pour 1 000 bases."),
     qcm("Que signifie une couverture de 30× ?", ["30 gènes séquencés", "Chaque base lue 30 fois en moyenne", "30 échantillons", "30 % du génome"], 1,
         "La profondeur de couverture est le nombre moyen de lectures qui recouvrent chaque position."),
     qcm("Quelle étape précède le séquençage NGS ?", ["L'électrophorèse sur gel", "La préparation de la bibliothèque", "La PCR en temps réel", "Le Western blot"], 1,
         "On fragmente l'ADN et on fixe des adaptateurs pour construire la bibliothèque de séquençage."),
     qt("Pourquoi le séquençage Sanger reste-t-il utile malgré le NGS ?",
        "Parce qu'il offre des lectures longues (600–800 pb) et une très bonne précision pour valider une mutation ponctuelle ou séquencer un seul gène, à moindre coût et sans lourde analyse bioinformatique.",
        "Le NGS est plus adapté quand on séquence de très nombreux fragments ou des génomes entiers."),
     qcm("Une base a un score de Phred Q20. Quelle est sa probabilité d'erreur ?",
         ["10⁻¹ (10 %)", "10⁻² (1 %)", "10⁻³ (0,1 %)", "10⁻⁴ (0,01 %)"], 1,
         "P = 10^(−Q/10) = 10⁻² = 0,01, soit 1 erreur pour 100 bases.",
         "Contrôle qualité d'un run de séquençage : interprétation des scores de confiance.", True),
     qcm("Pour séquencer un génome de 5 × 10⁶ pb avec une couverture de 30×, combien de bases faut-il produire ?",
         ["1,5 × 10⁶", "1,5 × 10⁷", "1,5 × 10⁸", "1,5 × 10⁹"], 2,
         "5 × 10⁶ × 30 = 1,5 × 10⁸ bases, soit 1,5 million de lectures de 100 pb.",
         "Dimensionnement d'un run NGS pour le séquençage d'un génome bactérien.", True),
     qcm("Avec des lectures de 150 pb, combien de lectures faut-il pour obtenir 3 × 10⁸ bases ?",
         ["2 × 10⁵", "2 × 10⁶", "2 × 10⁷", "2 × 10⁸"], 1,
         "3 × 10⁸ / 150 = 2 × 10⁶ lectures.",
         "Conversion entre nombre de lectures et nombre total de bases séquencées.", True)
    ],
    [
     intro("L'idée en une phrase", "Séquencer, c'est lire l'alphabet A-C-G-T : Sanger arrête l'élongation pour obtenir toutes les tailles, le NGS lit des millions de fragments en parallèle."),
     formule("Qualité et couverture", "Q = −10 log₁₀(P(erreur))   ·   bases totales = taille × couverture", "Q30 → 1 erreur/1 000 bases · couverture 30× → chaque base lue 30 fois"),
     grille("Sanger vs NGS", [
         ["Sanger", "600–800 pb, faible débit", "1 gène, validation"],
         ["Illumina", "50–300 pb, très haut débit", "génomes, RNA-seq"],
         ["Nanopore", "lectures longues", "assemblage, structure"]]),
     liste("Le flux NGS en 4 étapes", [
         "Bibliothèque : fragmentation + adaptateurs (index pour multiplexer)",
         "Amplification clonale ou pontante selon la plateforme",
         "Séquençage cyclique et acquisition des images/signaux",
         "Bioinformatique : démultiplexage, alignement, appel de variants"]),
     etapes("Séquencer un échantillon", [
         "Vérifier la quantité et la qualité de l'ADN (Qubit, gel, Bioanalyzer)",
         "Construire la bibliothèque avec adaptateurs et index",
         "Lancer le run avec les contrôles (PhiX, témoin positif)",
         "Filtrer les lectures selon le score de Phred et la couverture",
         "Aligner, appeler les variants et valider biologiquement"]),
     attention("⚠️ Les pièges classiques", [
         "Confondre Phred Q20 (1 %) et Q30 (0,1 %)",
         "Oublier que la couverture se calcule sur la taille du génome",
         "Négliger la qualité de l'ADN d'entrée : le séquençage ne corrige pas un mauvais extrait",
         "Comparer des lectures de technologies différentes sans précaution",
         "Oublier la traçabilité des index et des lots de réactifs"]),
     exemples("En chiffres (à savoir refaire)", [
         "<span class=\"cle\">Q30</span> → P = 10⁻³ = 0,1 % d'erreur",
         "<span class=\"cle\">Q20</span> → P = 10⁻² = 1 % d'erreur",
         "<span class=\"cle\">5 × 10⁶ pb × 30×</span> = 1,5 × 10⁸ bases",
         "<span class=\"cle\">3 × 10⁸ / 150 pb</span> = 2 × 10⁶ lectures",
         "<span class=\"cle\">ddNTP</span> = arrêt de l'élongation"]),
    ],
    [
     sc("1 · Principe du séquençage Sanger", """<svg viewBox="0 0 660 190" width="100%" role="img" aria-label="Principe Sanger : ADN polymérase, ddNTP terminateurs et fragments de tailles successives">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
      <text x="16" y="24" fill="var(--ac)" font-size="15" font-weight="bold">Sanger : arrêter l'élongation au bon nucléotide</text>
      <rect x="16" y="44" width="160" height="56" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="96" y="66" text-anchor="middle" fill="var(--fg)" font-size="11">Matrice + amorce</text><text x="96" y="84" text-anchor="middle" fill="var(--dim)" font-size="10">+ dNTP + ddNTP*</text>
      <line x1="180" y1="72" x2="240" y2="72" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
      <rect x="244" y="44" width="150" height="56" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="319" y="66" text-anchor="middle" fill="var(--fg)" font-size="11">Polymérase</text><text x="319" y="84" text-anchor="middle" fill="var(--dim)" font-size="10">incorporation *</text>
      <line x1="398" y1="72" x2="458" y2="72" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
      <rect x="462" y="38" width="182" height="68" rx="8" fill="var(--card2)" stroke="var(--warn)"/>
      <text x="476" y="58" fill="var(--warn)" font-size="11" font-weight="bold">Fragments</text>
      <line x1="476" y1="72" x2="520" y2="72" stroke="var(--ac)" stroke-width="3"/><text x="528" y="76" fill="var(--fg)" font-size="10">1 nt</text>
      <line x1="476" y1="86" x2="556" y2="86" stroke="var(--ac)" stroke-width="3"/><text x="564" y="90" fill="var(--fg)" font-size="10">2 nt</text>
      <line x1="476" y1="100" x2="592" y2="100" stroke="var(--ac)" stroke-width="3"/><text x="600" y="104" fill="var(--fg)" font-size="10">3 nt</text>
      <text x="330" y="136" text-anchor="middle" fill="var(--dim)" font-size="11">Séparation par taille (1 nt d'écart) puis lecture de la couleur du ddNTP</text>
      <text x="330" y="164" text-anchor="middle" fill="var(--warn)" font-size="11">600–800 pb de lecture fiable</text>
     </svg>"""),
     sc("2 · Chromatogramme et lecture", """<svg viewBox="0 0 660 185" width="100%" role="img" aria-label="Chromatogramme avec pics de couleurs et séquence lue">
      <line x1="40" y1="150" x2="620" y2="150" stroke="var(--dim)" stroke-width="2"/>
      <g fill="none" stroke-width="2"><path d="M50 146 L70 60 L90 146 L110 146 L130 92 L150 146 L170 146 L190 45 L210 146 L230 146 L250 88 L270 146" stroke="var(--ac)"/>
      <path d="M110 146 L130 120 L150 146 L230 146 L250 110 L270 146 L290 146 L310 70 L330 146" stroke="var(--warn)"/></g>
      <g font-size="14" font-weight="bold" text-anchor="middle"><text x="70" y="44" fill="var(--ac)">A</text><text x="130" y="80" fill="var(--warn)">C</text><text x="190" y="34" fill="var(--ac)">A</text><text x="250" y="76" fill="var(--warn)">C</text><text x="310" y="58" fill="var(--warn)">C</text></g>
      <text x="350" y="60" fill="var(--fg)" font-size="12">Séquence lue : 5'-ACACG...-3'</text>
      <rect x="350" y="80" width="290" height="66" rx="8" fill="var(--card2)" stroke="var(--dim)"/>
      <text x="364" y="102" fill="var(--ac)" font-size="11" font-weight="bold">Qualité du pic</text>
      <text x="364" y="122" fill="var(--fg)" font-size="10">pic net et séparé → base fiable</text>
      <text x="364" y="140" fill="var(--warn)" font-size="10">pics chevauchés → ambiguïté (N)</text>
     </svg>"""),
     sc("3 · Qualité Phred et couverture", """<svg viewBox="0 0 660 180" width="100%" role="img" aria-label="Score de Phred, probabilité d'erreur et calcul de couverture">
      <text x="16" y="24" fill="var(--ac)" font-size="15" font-weight="bold">Q = −10 log₁₀(P) · bases = taille × couverture</text>
      <g font-size="12" text-anchor="middle">
        <rect x="16" y="44" width="190" height="52" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="111" y="66" fill="var(--fg)">Q20</text><text x="111" y="86" fill="var(--dim)">1 erreur / 100 bases</text>
        <rect x="234" y="44" width="190" height="52" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="329" y="66" fill="var(--fg)">Q30</text><text x="329" y="86" fill="var(--dim)">1 erreur / 1 000 bases</text>
        <rect x="452" y="44" width="190" height="52" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="547" y="66" fill="var(--fg)">Q40</text><text x="547" y="86" fill="var(--dim)">1 erreur / 10 000 bases</text>
      </g>
      <rect x="120" y="116" width="420" height="46" rx="8" fill="var(--card2)" stroke="var(--warn)"/>
      <text x="330" y="136" text-anchor="middle" fill="var(--warn)" font-size="13">5 × 10⁶ pb × 30× = 1,5 × 10⁸ bases</text>
      <text x="330" y="153" text-anchor="middle" fill="var(--dim)" font-size="10">soit 1,5 million de lectures de 100 pb</text>
     </svg>""")
    ]
))

# ============================================================ FICHE 7
FICHES.append(mk(
    ["BTS1", "BTS2"], BIO, "Chapitre 7 · Culture cellulaire et numération", SRC_BIO,
    [
     "La culture cellulaire consiste à maintenir et multiplier des cellules in vitro dans un milieu nutritif stérile. On distingue les cellules adhérentes (qui se fixent au support) et les cellules en suspension, les cultures primaires (issues directement d'un tissu) et les lignées immortalisées.",
     "Le milieu de culture (DMEM, RPMI…) apporte glucose, acides aminés, sels, vitamines et sérum animal (FBS 5–10 %). Les cultures sont incubées à 37 °C, sous 5 % de CO₂ et en atmosphère humide ; le pH est maintenu vers 7,4 par un système tampon bicarbonaté.",
     "Les manipulations se font sous hotte à flux laminaire en asepsie stricte. Les cellules adhérentes sont détachées par trypsine (neutralisée par le sérum), comptées puis repiquées (passage) avant d'atteindre la confluence.",
     "L'hémocytomètre (chambre de Neubauer) permet la numération manuelle. Un grand carré a une surface de 1 mm² et une profondeur de 0,1 mm, soit un volume de 0,1 mm³ = 10⁻⁴ mL.",
     "Formule : concentration (cellules/mL) = nombre moyen de cellules par grand carré × facteur de dilution × 10⁴. Le facteur 10⁴ convertit le volume du carré (10⁻⁴ mL) en 1 mL.",
     "La viabilité s'évalue avec le bleu trypan (0,4 %) : les cellules mortes, dont la membrane est perméable, se colorent en bleu ; les cellules vivantes excluent le colorant. Viabilité (%) = cellules viables / cellules totales × 100.",
     "Pour une numération fiable, on vise 15 à 50 cellules par grand carré (ou ≥ 100 cellules comptées au total) et on applique la règle des bords : compter les cellules sur deux côtés seulement (haut et gauche, ou haut et droite).",
     "La cytométrie en flux (FCM) analyse des cellules en flux unicellulaire : FSC (forward scatter) renseigne la taille, SSC (side scatter) la granularité, et la fluorescence mesure des marqueurs. Le scattergramme sépare les populations (lymphocytes, monocytes, granulocytes).",
     "Le contrôle de qualité d'une culture porte sur la stérilité (absence de bactéries, champignons, mycoplasmes), l'authenticité (profil STR pour les lignées humaines) et la croissance (temps de doublement, morphologie).",
     "Applications BIOALC : production d'anticorps monoclonaux et de vaccins, tests de cytotoxicité, contrôle de stérilité, dosage de facteurs de croissance, étude de l'effet d'un principe actif sur des cellules."
    ],
    [
     qcm("Quel est le volume d'un grand carré de Neubauer ?", ["1 mm³", "0,1 mm³", "0,01 mm³", "1 mL"], 1,
         "1 mm × 1 mm × 0,1 mm = 0,1 mm³ = 10⁻⁴ mL, d'où le facteur 10⁴."),
     qcm("Pourquoi multiplexe-t-on par 10⁴ ?", ["Pour corriger la dilution", "Pour passer de 10⁻⁴ mL à 1 mL", "Pour compter les morts", "Pour mesurer le pH"], 1,
         "Le carré contient 10⁻⁴ mL : 1 / 10⁻⁴ = 10⁴ permet d'exprimer la concentration par mL."),
     qcm("Que colore le bleu trypan ?", ["Les cellules vivantes", "Les cellules mortes", "Les bactéries uniquement", "Le sérum"], 1,
         "Le bleu trypan entre dans les cellules à membrane endommagée : seules les cellules mortes apparaissent bleues."),
     qcm("À quelle température et CO₂ incuber une culture mammifère ?", ["25 °C, 0 % CO₂", "37 °C, 5 % CO₂", "42 °C, 10 % CO₂", "4 °C, 5 % CO₂"], 1,
         "37 °C et 5 % de CO₂ reproduisent les conditions physiologiques et maintiennent le pH avec le tampon bicarbonaté."),
     qcm("Quel axe du scattergramme renseigne la granularité ?", ["FSC", "SSC", "FL1", "Le temps"], 1,
         "SSC (side scatter) reflète la complexité/granularité interne ; FSC reflète la taille relative."),
     qcm("Comment détacher des cellules adhérentes ?", ["Avec de l'éthanol", "Avec de la trypsine", "Avec du bleu trypan", "Par congélation"], 1,
         "La trypsine digère les protéines d'adhésion ; elle est neutralisée par le sérum contenu dans le milieu."),
     qt("Pourquoi réaliser la numération en double et respecter la règle des bords ?",
        "Pour limiter l'erreur de comptage : les doublons réduisent la variabilité, et compter les cellules sur deux côtés seulement évite de comptes deux fois celles qui touchent une ligne.",
        "On vise au moins 100 cellules comptées et 15 à 50 par carré pour une précision acceptable."),
     qcm("Quatre carrés donnent 92, 88, 95 et 85 cellules viables. La suspension a été diluée 1:1 avec du bleu trypan (facteur 2). Quelle est la concentration ?",
         ["9 × 10⁵ cellules/mL", "1,8 × 10⁶ cellules/mL", "3,6 × 10⁶ cellules/mL", "1,8 × 10⁵ cellules/mL"], 1,
         "Moyenne = (92+88+95+85)/4 = 90 ; 90 × 2 × 10⁴ = 1,8 × 10⁶ cellules/mL.",
         "Numération d'une suspension cellulaire à l'hémocytomètre après marquage au bleu trypan.", True),
     qcm("Sur les 4 carrés, on a compté 360 cellules viables et 18 cellules mortes. Quelle est la viabilité ?",
         ["95,2 %", "90,0 %", "98,0 %", "85,0 %"], 0,
         "Viabilité = 360/(360+18) × 100 = 360/378 × 100 ≈ 95,2 %.",
         "Contrôle de la qualité d'une culture avant repiquage.", True),
     qcm("Une suspension à 2 × 10⁶ cellules/mL est diluée au 1/10 pour le comptage. Combien de cellules doit-on compter en moyenne par carré ?",
         ["2 × 10⁵", "20", "200", "2 000"], 1,
         "Concentration diluée = 2 × 10⁵ cellules/mL ; cellules par carré = 2 × 10⁵ / 10⁴ = 20.",
         "Choix de la dilution pour obtenir un nombre de cellules comptables (15–50 par carré).", True)
    ],
    [
     intro("L'idée en une phrase", "Un carré de Neubauer représente 10⁻⁴ mL : compter les cellules puis multiplier par 10⁴ et par la dilution donne la concentration, le bleu trypan donnant la viabilité."),
     formule("Numération", "C (cellules/mL) = N_moyen × facteur de dilution × 10⁴", "Viabilité (%) = cellules viables / (viables + mortes) × 100 · carré = 0,1 mm³ = 10⁻⁴ mL"),
     grille("Les 3 paramètres", [
         ["N moyen", "cellules comptées par grand carré", "15–50 idéalement"],
         ["Dilution", "facteur total (trypan inclus)", "ex. 1:2 ou 1:10"],
         ["10⁴", "conversion 10⁻⁴ mL → 1 mL", "constante"]]),
     liste("Conditions de culture", [
         "Milieu DMEM/RPMI + 5–10 % de sérum (FBS), 37 °C, 5 % CO₂, humidité",
         "Hotte à flux laminaire, asepsie, NSB2 selon l'origine des cellules",
         "Cellules adhérentes détachées à la trypsine neutralisée par le sérum",
         "Contrôles : stérilité, mycoplasmes, authenticité STR, croissance"]),
     etapes("Compter au Neubauer", [
         "Homogénéiser la suspension et la diluer (1:1 avec le bleu trypan)",
         "Déposer ~10 µL sous la lamelle par capillarité (anneaux de Newton)",
         "Compter cellules viables (incolores) et mortes (bleues) dans les carrés",
         "Appliquer la règle des bords et calculer la moyenne par carré",
         "Calculer C et la viabilité, puis nettoyer et tracer le résultat"]),
     attention("⚠️ Les pièges classiques", [
         "Oublier le facteur de dilution, notamment celui du bleu trypan",
         "Compter les cellules sur les quatre bords (double comptage)",
         "Laisser les cellules sédimenter : la suspension doit être homogène",
         "Présence de bulles ou débris : refaire le montage",
         "Bleu trypan mutagène : gants et déchets DASRI"]),
     exemples("En chiffres (à savoir refaire)", [
         "<span class=\"cle\">(92+88+95+85)/4 = 90</span> cellules/carré",
         "<span class=\"cle\">90 × 2 × 10⁴</span> = 1,8 × 10⁶ cellules/mL",
         "<span class=\"cle\">360/378 × 100</span> ≈ 95,2 % de viabilité",
         "<span class=\"cle\">2 × 10⁵ / 10⁴</span> = 20 cellules par carré",
         "<span class=\"cle\">FSC</span> = taille · <span class=\"cle\">SSC</span> = granularité"]),
    ],
    [
     sc("1 · La chambre de Neubauer", """<svg viewBox="0 0 660 190" width="100%" role="img" aria-label="Hémocytomètre de Neubauer avec grille et grand carré de 0,1 millimètre cube">
      <rect x="30" y="36" width="300" height="130" rx="6" fill="var(--card2)" stroke="var(--dim)"/>
      <g stroke="var(--dim)" stroke-width="1"><line x1="105" y1="36" x2="105" y2="166"/><line x1="180" y1="36" x2="180" y2="166"/><line x1="255" y1="36" x2="255" y2="166"/><line x1="30" y1="101" x2="330" y2="101"/></g>
      <rect x="180" y="36" width="75" height="65" fill="none" stroke="var(--ac)" stroke-width="3"/>
      <text x="217" y="72" text-anchor="middle" fill="var(--ac)" font-size="11">grand carré</text>
      <text x="180" y="182" fill="var(--dim)" font-size="11">1 mm × 1 mm × 0,1 mm = 0,1 mm³ = 10⁻⁴ mL</text>
      <rect x="360" y="44" width="284" height="112" rx="8" fill="var(--card2)" stroke="var(--ac)"/>
      <text x="374" y="66" fill="var(--ac)" font-size="12" font-weight="bold">Règle de comptage</text>
      <text x="374" y="90" fill="var(--fg)" font-size="11">Compter 2 bords seulement</text>
      <text x="374" y="112" fill="var(--fg)" font-size="11">(haut + gauche, par exemple)</text>
      <text x="374" y="134" fill="var(--warn)" font-size="11">Vivantes incolores / mortes bleues</text>
     </svg>"""),
     sc("2 · Deux étages de dilution", """<svg viewBox="0 0 660 165" width="100%" role="img" aria-label="Calcul de concentration cellulaire à partir du comptage et du facteur de dilution">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
      <g font-size="11" text-anchor="middle">
        <rect x="12" y="44" width="140" height="60" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="82" y="68" fill="var(--ac)" font-weight="bold">Comptage</text><text x="82" y="88" fill="var(--fg)">90 cellules/carré</text>
        <line x1="154" y1="74" x2="190" y2="74" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="194" y="44" width="140" height="60" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="264" y="68" fill="var(--ac)" font-weight="bold">× dilution</text><text x="264" y="88" fill="var(--fg)">× 2 (trypan)</text>
        <line x1="336" y1="74" x2="372" y2="74" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="376" y="44" width="140" height="60" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="446" y="68" fill="var(--ac)" font-weight="bold">× 10⁴</text><text x="446" y="88" fill="var(--fg)">conversion mL</text>
        <line x1="518" y1="74" x2="554" y2="74" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="558" y="44" width="90" height="60" rx="8" fill="var(--card2)" stroke="var(--warn)"/><text x="603" y="72" fill="var(--warn)" font-weight="bold">C</text><text x="603" y="90" fill="var(--fg)" font-size="10">1,8 × 10⁶</text>
      </g>
      <text x="330" y="136" text-anchor="middle" fill="var(--dim)" font-size="11">C = 90 × 2 × 10⁴ = 1,8 × 10⁶ cellules/mL</text>
     </svg>"""),
     sc("3 · Viabilité et cytométrie", """<svg viewBox="0 0 660 190" width="100%" role="img" aria-label="Viabilité au bleu trypan et scattergramme FSC SSC">
      <text x="16" y="24" fill="var(--ac)" font-size="15" font-weight="bold">Viable / morte et populations cellulaires</text>
      <rect x="16" y="40" width="270" height="130" rx="8" fill="var(--card2)" stroke="var(--dim)"/>
      <text x="30" y="62" fill="var(--fg)" font-size="11">Bleu trypan</text>
      <circle cx="60" cy="100" r="8" fill="none" stroke="var(--ac)" stroke-width="2"/><text x="78" y="104" fill="var(--fg)" font-size="10">vivante (incolore)</text>
      <circle cx="60" cy="135" r="8" fill="var(--warn)"/><text x="78" y="139" fill="var(--fg)" font-size="10">morte (bleue)</text>
      <text x="30" y="162" fill="var(--ac)" font-size="11">360 / 378 = 95,2 %</text>
      <line x1="320" y1="170" x2="320" y2="40" stroke="var(--dim)" stroke-width="2"/><line x1="320" y1="170" x2="620" y2="170" stroke="var(--dim)" stroke-width="2"/>
      <text x="300" y="38" fill="var(--fg)" font-size="10">SSC</text><text x="590" y="186" fill="var(--fg)" font-size="10">FSC</text>
      <g fill="var(--ac)" opacity="0.7"><circle cx="400" cy="120" r="12"/><circle cx="420" cy="110" r="10"/><circle cx="385" cy="135" r="9"/></g>
      <g fill="var(--warn)" opacity="0.7"><circle cx="500" cy="80" r="12"/><circle cx="520" cy="70" r="10"/><circle cx="485" cy="95" r="9"/></g>
      <text x="360" y="155" fill="var(--ac)" font-size="10">lymphocytes</text>
      <text x="470" y="150" fill="var(--warn)" font-size="10">granulocytes</text>
     </svg>""")
    ]
))

# ============================================================ FICHE 8
FICHES.append(mk(
    ["BTS2"], BIO, "Chapitre 8 · Virologie et agents transmissibles non conventionnels", SRC_BIO,
    [
     "Un virus est une particule infectieuse obligatoirement intracellulaire, composée d'un génome nucléique (ADN ou ARN, simple ou double brin) entouré d'une capside protéique. Certains virus possèdent une enveloppe lipidique portant des spicules (glycoprotéines). Leur taille varie de 20 à 300 nm.",
     "Le cycle viral comporte six étapes : adsorption (fixation sur un récepteur), pénétration, désenveloppement, réplication du génome et synthèse des protéines, assemblage (maturation), puis libération par lyse ou bourgeonnement.",
     "Les virus sont cultivés sur cellules permissives, sur œufs embryonnés ou par inoculation à l'animal. La réplication se manifeste par un effet cytopathique (ECP), des plages de lyse ou la production d'antigènes détectables.",
     "Le titre viral exprime la quantité de virus infectieux : en plages, on compte les PFU (plaque forming units) ; en dilution limite (TCID50), on détermine la dilution qui infecte 50 % des cultures. La multiplicité d'infection (MOI) = nombre de particules virales / nombre de cellules.",
     "La détection repose sur la PCR ou la RT-PCR (génome viral), les tests antigéniques (ELISA), la sérologie (anticorps IgM/IgG) et, plus rarement, l'hémagglutination ou l'immunofluorescence.",
     "Les agents transmissibles non conventionnels (ATNC), ou prions, sont des protéines infectieuses dépourvues d'acide nucléique. La protéine normale PrP^C (α-hélicoïdale) se convertit en PrP^Sc (riche en feuillets β), insoluble, résistante aux protéases et aux traitements physiques courants.",
     "Maladies à prions : encéphalopathie spongiforme bovine (ESB), tremblante du mouton, maladie de Creutzfeldt-Jakob (vCJD) chez l'humain, chronic wasting disease chez les cervidés. La période d'incubation est très longue et l'issue est toujours fatale.",
     "L'inactivation des prions est difficile : autoclavage à 134 °C pendant 18 min (ou 121 °C prolongé), traitement à l'hypochlorite de sodium (2 %) ou au NaOH (1 M), incinération des déchets. Les procédés classiques (70 °C, alcool, UV) sont inefficaces.",
     "La biosécurité impose un classement en niveaux de confinement (NSB1 à NSB4), des équipements de protection, des enceintes de sécurité biologique et la gestion des déchets DASRI. Le risque nosocomial et la traçabilité des instruments sont cruciaux.",
     "Applications BIOALC : contrôle de l'absence de virus dans les produits biologiques, diagnostic vétérinaire, contrôle des matières premières d'origine animale, surveillance environnementale et validation des procédés d'inactivation."
    ],
    [
     qcm("Quel est le constituant obligatoire d'un virus ?", ["Une enveloppe lipidique", "Une capside et un génome", "Des ribosomes", "Une paroi cellulaire"], 1,
         "Tout virus possède une capside protéique et un génome ADN ou ARN ; l'enveloppe est facultative."),
     qcm("Quelle étape du cycle viral précède la réplication ?", ["La libération", "Le désenveloppement", "L'assemblage", "La lyse"], 1,
         "Ordre : adsorption → pénétration → désenveloppement → réplication → assemblage → libération."),
     qcm("Que désigne une unité PFU ?", ["Une particule virale totale", "Une unité formant une plage infectieuse", "Un anticorps", "Une cellule infectée"], 1,
         "Le PFU (plaque forming unit) mesure les particules virales infectieuses capables de former une plage de lyse."),
     qcm("Comment appelle-t-on la protéine anormale des prions ?", ["PrP^C", "PrP^Sc", "PrP^A", "PrP^N"], 1,
         "PrP^C est la forme normale, PrP^Sc la forme pathologique, riche en feuillets β et résistante aux protéases."),
     qcm("Quel traitement inactive efficacement les prions ?", ["70 °C 10 min", "Autoclavage 134 °C 18 min", "Éthanol 70 %", "UV 15 min"], 1,
         "Seuls des traitements sévères (134 °C/18 min, NaOH 1 M, hypochlorite 2 %, incinération) réduisent l'infectiosité des prions."),
     qcm("Les prions contiennent-ils de l'acide nucléique ?", ["Oui, de l'ADN", "Oui, de l'ARN", "Non", "Oui, des deux"], 2,
         "Les ATNC sont des protéines infectieuses sans acide nucléique : c'est ce qui les distingue des virus."),
     qt("Pourquoi la maladie de Creutzfeldt-Jakob est-elle particulièrement redoutée en laboratoire ?",
        "Parce que l'agent (prion) résiste aux désinfectants usuels, que la période d'incubation est très longue et qu'il n'existe aucun traitement ni test de routine fiable sur le vivant. Une exposition accidentelle impose un suivi et une traçabilité stricts des instruments.",
        "Le risque est renforcé par la résistance de PrP^Sc aux protéases et à la chaleur modérée."),
     qcm("On obtient 50 plages après dépôt de 0,1 mL d'une dilution 10⁻⁵. Quel est le titre ?",
         ["5 × 10⁵ PFU/mL", "5 × 10⁷ PFU/mL", "5 × 10⁶ PFU/mL", "5 × 10⁸ PFU/mL"], 1,
         "Titre = 50 / (0,1 × 10⁻⁵) = 50 × 10⁶ = 5 × 10⁷ PFU/mL.",
         "Titrage d'un stock viral par la technique des plages de lyse.", True),
     qcm("Pour infecter 10⁶ cellules avec une MOI de 0,1, combien de particules infectieuses faut-il ?",
         ["10⁴", "10⁵", "10⁶", "10⁷"], 1,
         "MOI = particules / cellules → particules = 0,1 × 10⁶ = 10⁵.",
         "Préparation d'une infection virale contrôlée en culture cellulaire.", True),
     qcm("Un traitement réduit la charge virale de 10⁶ à 10² PFU/mL. Quelle est la réduction en log₁₀ ?",
         ["2 log", "3 log", "4 log", "6 log"], 2,
         "log₁₀(10⁶) − log₁₀(10²) = 6 − 2 = 4 log₁₀, soit un facteur 10 000.",
         "Validation de l'efficacité d'un procédé d'inactivation virale.", True)
    ],
    [
     intro("L'idée en une phrase", "Le virus est un parasite intracellulaire avec capside et génome ; le prion est une simple protéine anormale, sans acide nucléique, remarquablement résistante."),
     formule("Titrage et MOI", "Titre (PFU/mL) = plages / (volume déposé × dilution)   ·   MOI = particules / cellules", "Réduction log = log₁₀(titre initial) − log₁₀(titre final)"),
     grille("Virus vs prion", [
         ["Virus", "capside + ADN/ARN, parfois enveloppe", "sensible à la chaleur modérée"],
         ["Prion", "protéine PrP^Sc, aucun acide nucléique", "résistant (134 °C, NaOH, hypochlorite)"],
         ["Détection", "PCR, RT-PCR, ELISA, sérologie", "immunoblot, bio-essai, post-mortem"]]),
     liste("Les 6 étapes du cycle viral", [
         "Adsorption sur un récepteur spécifique → pénétration → désenveloppement",
         "Réplication du génome et synthèse des protéines virales",
         "Assemblage et maturation des nouvelles particules",
         "Libération par lyse cellulaire ou bourgeonnement",
         "Effet cytopathique et plages de lyse comme signes de réplication"]),
     etapes("Maîtriser le risque viral", [
         "Classer l'agent en NSB et choisir le confinement adapté",
         "Travailler en enceinte de sécurité biologique avec EPI",
         "Titrer les stocks (PFU, TCID50) et calculer la MOI",
         "Inactiver selon le type d'agent (prions : protocole renforcé)",
         "Éliminer les déchets en DASRI et tracer chaque manipulation"]),
     attention("⚠️ Les pièges classiques", [
         "Croire que tous les virus ont une enveloppe (non : virus nus)",
         "Confondre PrP^C (normal) et PrP^Sc (pathogène)",
         "Appliquer un protocole d'inactivation standard aux prions",
         "Oublier le facteur de dilution dans le titrage PFU",
         "Négliger la traçabilité des instruments en cas d'exposition"]),
     exemples("En chiffres (à savoir refaire)", [
         "<span class=\"cle\">50/(0,1 × 10⁻⁵)</span> = 5 × 10⁷ PFU/mL",
         "<span class=\"cle\">MOI 0,1 × 10⁶ cellules</span> = 10⁵ particules",
         "<span class=\"cle\">10⁶ → 10²</span> = réduction de 4 log",
         "<span class=\"cle\">134 °C, 18 min</span> = référence prions",
         "<span class=\"cle\">PrP^Sc</span> = feuillets β, résistant aux protéases"]),
    ],
    [
     sc("1 · Structure d'un virus enveloppé", """<svg viewBox="0 0 660 185" width="100%" role="img" aria-label="Structure d'un virus avec enveloppe capside génome et spicules">
      <circle cx="180" cy="95" r="62" fill="var(--card2)" stroke="var(--ac)" stroke-width="2"/>
      <g stroke="var(--warn)" stroke-width="2"><line x1="180" y1="33" x2="180" y2="15"/><line x1="230" y1="55" x2="244" y2="41"/><line x1="242" y1="95" x2="262" y2="95"/><line x1="230" y1="135" x2="244" y2="149"/><line x1="130" y1="55" x2="116" y2="41"/><line x1="118" y1="95" x2="98" y2="95"/><line x1="130" y1="135" x2="116" y2="149"/></g>
      <circle cx="180" cy="95" r="38" fill="none" stroke="var(--dim)" stroke-width="3"/>
      <path d="M162 95 C162 78 198 78 198 95 C198 112 162 112 162 95" fill="none" stroke="var(--ac)" stroke-width="3"/>
      <text x="180" y="178" text-anchor="middle" fill="var(--dim)" font-size="10">enveloppe + spicules · capside · génome (ADN ou ARN)</text>
      <rect x="300" y="40" width="340" height="120" rx="8" fill="var(--card2)" stroke="var(--dim)"/>
      <text x="316" y="62" fill="var(--ac)" font-size="12" font-weight="bold">Deux catégories</text>
      <text x="316" y="86" fill="var(--fg)" font-size="11">Virus nu = capside + génome</text>
      <text x="316" y="110" fill="var(--fg)" font-size="11">Virus enveloppé = + membrane lipidique</text>
      <text x="316" y="134" fill="var(--warn)" font-size="11">Taille : 20–300 nm</text>
      <text x="316" y="152" fill="var(--dim)" font-size="10">Parasite obligatoire de cellule</text>
     </svg>"""),
     sc("2 · Cycle de réplication viral", """<svg viewBox="0 0 660 170" width="100%" role="img" aria-label="Six étapes du cycle viral de l'adsorption à la libération">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
      <g font-size="10" text-anchor="middle">
        <rect x="8" y="48" width="96" height="56" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="56" y="72" fill="var(--ac)" font-weight="bold">1. Adsorption</text><text x="56" y="90" fill="var(--fg)">récepteur</text>
        <line x1="106" y1="76" x2="122" y2="76" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="126" y="48" width="96" height="56" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="174" y="72" fill="var(--ac)" font-weight="bold">2. Pénétration</text>
        <line x1="224" y1="76" x2="240" y2="76" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="244" y="48" width="96" height="56" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="292" y="72" fill="var(--ac)" font-weight="bold">3. Désenvelopp.</text>
        <line x1="342" y1="76" x2="358" y2="76" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="362" y="48" width="96" height="56" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="410" y="72" fill="var(--ac)" font-weight="bold">4. Réplication</text>
        <line x1="460" y1="76" x2="476" y2="76" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="480" y="48" width="80" height="56" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="520" y="72" fill="var(--ac)" font-weight="bold">5. Assemblage</text>
        <line x1="562" y1="76" x2="578" y2="76" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/>
        <rect x="582" y="48" width="68" height="56" rx="8" fill="var(--card2)" stroke="var(--warn)"/><text x="616" y="72" fill="var(--warn)" font-weight="bold">6. Libération</text>
      </g>
      <text x="330" y="136" text-anchor="middle" fill="var(--dim)" font-size="11">Lyse ou bourgeonnement · effet cytopathique (ECP) · plages de lyse</text>
     </svg>"""),
     sc("3 · Prion : PrP^C → PrP^Sc", """<svg viewBox="0 0 660 170" width="100%" role="img" aria-label="Conversion de la protéine prion normale en forme pathologique et résistance">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--warn)"/></marker></defs>
      <rect x="20" y="44" width="200" height="76" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="120" y="70" text-anchor="middle" fill="var(--ac)" font-size="14" font-weight="bold">PrP^C</text><text x="120" y="92" text-anchor="middle" fill="var(--fg)" font-size="11">forme normale</text><text x="120" y="110" text-anchor="middle" fill="var(--dim)" font-size="10">α-hélices, sensible aux protéases</text>
      <line x1="224" y1="82" x2="386" y2="82" stroke="var(--warn)" stroke-width="3" marker-end="url(#@@a)"/><text x="305" y="70" text-anchor="middle" fill="var(--warn)" font-size="11">conversion</text>
      <rect x="392" y="44" width="240" height="76" rx="8" fill="var(--card2)" stroke="var(--warn)"/><text x="512" y="70" text-anchor="middle" fill="var(--warn)" font-size="14" font-weight="bold">PrP^Sc</text><text x="512" y="92" text-anchor="middle" fill="var(--fg)" font-size="11">forme pathologique (ATNC)</text><text x="512" y="110" text-anchor="middle" fill="var(--dim)" font-size="10">feuillets β, insoluble, résistante</text>
      <text x="330" y="148" text-anchor="middle" fill="var(--dim)" font-size="11">Aucun acide nucléique · ESB, tremblante, Creutzfeldt-Jakob · inactivation 134 °C/18 min</text>
     </svg>""")
    ]
))
