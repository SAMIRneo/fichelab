# -*- coding: utf-8 -*-
"""Générateur de bioalc-mat-part-C.json (matières Biologie moléculaire & Qualité)."""
import json

BIO = 'Biologie moléculaire et cellulaire'
QUA = 'Qualité et gestion du laboratoire'
SRC_BIO = ("Arrêté du 12 mars 2024 modifié par l'arrêté du 24 juin 2025 (BTS BIOALC, U6, RNCP38884) · "
           "Référentiel BTS BioALC (savoirs associés T2.3) · document d'accompagnement UPBM/ac-Toulouse · "
           "Manuel de biologie moléculaire (Sambrook) · Thermo Fisher / NEB / Eurogentec guides qPCR · MIQE guidelines")
SRC_QUA = ("Arrêté du 12 mars 2024 modifié par l'arrêté du 24 juin 2025 (BTS BIOALC, U5, RNCP38884) · "
           "NF EN ISO/IEC 17025:2017 (§4 à 8) · ISO 9000:2015 (7 principes) · Cofrac LAB REF 02 rév.15 / GEN REF 10 · "
           "Guide d'accréditation COFRAC · VIM3 JCGM 200:2012 · ISO 5725")

def qcm(q, options, correct, correction, contexte=None, calcul=False):
    d = {"type": "qcm", "q": q, "options": options, "correct": correct, "correction": correction}
    if contexte:
        d["contexte"] = contexte
    if calcul:
        d["calcul"] = True
    return d

def qt(q, reponse, correction, contexte=None, calcul=False):
    d = {"type": "texte", "q": q, "reponse": reponse, "correction": correction}
    if contexte:
        d["contexte"] = contexte
    if calcul:
        d["calcul"] = True
    return d

def intro(t, x): return {"type": "intro", "titre": t, "texte": x}
def formule(t, eq, leg): return {"type": "formule", "titre": t, "eq": eq, "leg": leg}
def grille(t, items): return {"type": "grille", "titre": t, "items": items}
def liste(t, items): return {"type": "liste", "titre": t, "items": items}
def etapes(t, items): return {"type": "etapes", "titre": t, "items": items}
def attention(t, items): return {"type": "attention", "titre": t, "items": items}
def exemples(t, items): return {"type": "exemples", "titre": t, "items": items}

_sid = [0]
def sc(titre, svg):
    _sid[0] += 1
    return {"titre": titre, "svg": svg.replace("@@", "bioC%d" % _sid[0])}

def mk(annees, matiere, titre, source, points, questions, affichage, schemas):
    return {
        "filieres": ["bts-bio"], "annees": annees, "matiere": matiere,
        "titre": titre, "source": source, "points": points,
        "questions": questions, "affichage": affichage, "schema": schemas
    }

FICHES = []

# ============================================================ FICHE 1
FICHES.append(mk(
    ["BTS1"], BIO, "Chapitre 1 · Structure de l'ADN et de l'ARN", SRC_BIO,
    [
     "L'acide désoxyribonucléique (ADN) est un polynucléotide : chaque nucléotide associe un sucre (le désoxyribose), un groupe phosphate et une base azotée. Les bases sont l'adénine (A) et la guanine (G, purines), la cytosine (C) et la thymine (T, pyrimidines). L'ARN contient du ribose et l'uracile (U) remplace la thymine.",
     "Watson et Crick (1953) décrivent l'ADN comme une double hélice : deux chaînes polynucléotidiques enroulées, reliées par des appariements complémentaires A=T (2 liaisons hydrogène) et G≡C (3 liaisons hydrogène). La complémentarité est la base de la réplication et de la transcription.",
     "Les deux brins sont ANTIPARALLÈLES : l'un est orienté 5' → 3', l'autre 3' → 5'. L'extrémité 5' porte le phosphate, l'extrémité 3' porte un hydroxyle (-OH). Une séquence s'écrit toujours de 5' vers 3'.",
     "La richesse en GC augmente la stabilité de l'hélice (3 liaisons H contre 2 pour AT) et donc la température de fusion Tm. Pour un court oligonucléide, l'approximation de Wallace donne Tm ≈ 2 × (A+T) + 4 × (G+C) en °C.",
     "Le squelette phosphate porte des charges négatives : l'ADN et l'ARN sont des polyanions, ce qui explique leur migration vers l'anode (+) en électrophorèse et leur interaction avec les histones (protéines positives) pour former la chromatine.",
     "L'ARN est généralement monocaténaire et plus court que l'ADN. Trois grands ARN sont à connaître : l'ARN messager (ARNm, copie d'un gène traduite en protéine), l'ARN de transfert (ARNt, porte l'anticodon et l'acide aminé) et l'ARN ribosomal (ARNr, constituant du ribosome).",
     "Différences ADN / ARN : sucre désoxyribose vs ribose, thymine vs uracile, double vs simple brin, grande stabilité vs fragilité (ARNases), localisation noyau/mitochondrie vs noyau/cytoplasme.",
     "Les bases azotées aromatiques absorbent les UV à 260 nm. Un échantillon d'ADN pur a un rapport A260/A280 voisin de 1,8 ; un ARN pur voisin de 2,0. Ces rapports servent au contrôle de pureté après extraction.",
     "Les gènes sont des segments d'ADN portant l'information pour une protéine ou un ARN fonctionnel. Le génome bactérien est généralement circulaire et haploidique ; le génome eucaryote est linéaire, organisé en chromosomes et contient des introns et des exons.",
     "Applications BIOALC : identification d'espèce par séquençage d'un gène marqueur (16S pour les bactéries, ITS pour les champignons, COI pour les animaux), détection d'OGM, diagnostic moléculaire, contrôle d'authenticité des matières premières."
    ],
    [
     qcm("Quelle base remplace la thymine dans l'ARN ?", ["La cytosine", "L'uracile", "La guanine", "L'adénine"], 1,
         "L'ARN utilise l'uracile (U) à la place de la thymine (T) : appariement A=U et G≡C."),
     qcm("Combien de liaisons hydrogène relient la guanine et la cytosine ?", ["1", "2", "3", "4"], 2,
         "G≡C forme 3 liaisons hydrogène, A=T seulement 2 : un riche en GC est plus stable."),
     qcm("Quelle est la complémentaire de la séquence 5'-ATGCGT-3' ?", ["5'-TACGCA-3'", "3'-TACGCA-5'", "5'-UACGCA-3'", "3'-ATGCGT-5'"], 1,
         "Les brins sont antiparallèles : A↔T, T↔A, G↔C, C↔G, G↔C, T↔A, soit 3'-TACGCA-5'."),
     qcm("Quel sucre entre dans la composition de l'ADN ?", ["Le ribose", "Le désoxyribose", "Le glucose", "Le fructose"], 1,
         "L'ADN contient le 2-désoxyribose ; l'ARN contient le ribose (hydroxyle en 2')."),
     qcm("Pourquoi l'ADN migre-t-il vers l'anode en électrophorèse ?", ["Il est positif", "Il est neutre", "Ses phosphates sont négatifs", "Il est fluorescent"], 2,
         "Le squelette phosphate porte une charge négative par nucléotide : l'ADN est un polyanion attiré par le pôle positif."),
     qcm("Quel rapport A260/A280 indique un ADN pur ?", ["≈ 0,6", "≈ 1,0", "≈ 1,8", "≈ 3,0"], 2,
         "Un ADN pur a A260/A280 ≈ 1,8 ; un ARN pur ≈ 2,0. Une valeur plus basse signale une contamination protéique."),
     qcm("Quel ARN porte l'anticodon ?", ["L'ARNm", "L'ARNt", "L'ARNr", "L'ARNsi"], 1,
         "L'ARNt (transfert) porte l'anticodon complémentaire du codon et l'acide aminé correspondant."),
     qt("Expliquer pourquoi un ADN riche en GC a une température de fusion (Tm) plus élevée.",
        "Les paires G≡C sont reliées par 3 liaisons hydrogène contre 2 pour A=T. Il faut donc plus d'énergie (température) pour séparer les deux brins.",
        "La Tm croît avec le %GC : Wallace, Tm ≈ 2(A+T) + 4(G+C) pour un oligo court."),
     qcm("Un oligonucléide de 16 bases contient 4 A, 4 T, 4 G et 4 C. Quelle est sa Tm (Wallace) ?", ["40 °C", "48 °C", "56 °C", "64 °C"], 1,
         "Tm = 2×(4+4) + 4×(4+4) = 16 + 32 = 48 °C.",
         "Contrôle qualité d'une amorce de PCR : le %GC conditionne la température d'hybridation.", True),
     qcm("Une solution d'ADN diluée 1/50 donne A260 = 0,500. Quelle est sa concentration (1 DO = 50 µg/mL) ?",
         ["25 µg/mL", "500 µg/mL", "1 250 µg/mL", "50 µg/mL"], 2,
         "C = 0,500 × 50 × 50 = 1 250 µg/mL dans la solution mère (0,500 × 50 = 25 µg/mL mesurés × facteur 50).",
         "Quantification d'un extrait d'ADN au spectrophotomètre après dilution au 1/50.", True)
    ],
    [
     intro("L'idée en une phrase", "L'ADN est un double brin de nucléotides complémentaires : cette complémentarité permet de copier l'information génétique et de la transmettre intacte."),
     formule("Les appariements à connaître", "A = T (2 liaisons H)  ·  G ≡ C (3 liaisons H)", "Brins antiparallèles 5'→3' / 3'→5' · Tm ≈ 2(A+T) + 4(G+C) pour un oligo court"),
     grille("Les 3 parties du nucléotide", [
         ["Sucre", "Désoxyribose (ADN) ou ribose (ARN)", "pentose"],
         ["Phosphate", "Charge négative, relie les sucres en 3'-5'", "polyanion"],
         ["Base", "A, G, T/C (ADN) · A, G, U, C (ARN)", "absorbe à 260 nm"]]),
     liste("ADN ou ARN ?", [
         "ADN : désoxyribose, A-T/G-C, double hélice, stable, noyau et mitochondries",
         "ARN : ribose, A-U/G-C, généralement simple brin, fragile, noyau et cytoplasme",
         "ARNm = messager · ARNt = transfert (anticodon) · ARNr = ribosome",
         "Bases aromatiques → absorbance maximale à 260 nm (A260/A280 ≈ 1,8 ADN, 2,0 ARN)"]),
     etapes("Lire et compléter une séquence", [
         "Repérer les extrémités : 5' phosphate, 3' hydroxyle",
         "Lire la séquence dans le sens 5' → 3'",
         "Appliquer la complémentarité : A↔T (ou U), G↔C",
         "Inverser l'orientation : la complémentaire de 5'-ATGC-3' est 3'-TACG-5'",
         "Vérifier le %GC pour estimer la stabilité et la Tm"]),
     attention("⚠️ Les pièges classiques", [
         "Oublier l'antiparallélisme : 5'-ATGC-3' ≠ 5'-TACG-3'",
         "Confondre U (ARN) et T (ADN)",
         "Croire que G-C a 2 liaisons H : il en a 3",
         "Réécrire une séquence sans préciser le sens 5'/3'",
         "Oublier que la charge négative vient du phosphate, pas de la base"]),
     exemples("En chiffres (à savoir refaire)", [
         "<span class=\"cle\">5'-ATGCGT-3'</span> → complémentaire 3'-TACGCA-5'",
         "<span class=\"cle\">%GC = (G+C)/(A+T+G+C) × 100</span>",
         "<span class=\"cle\">Tm = 2(A+T)+4(G+C)</span> : 4A 4T 4G 4C → 48 °C",
         "<span class=\"cle\">A260 = 0,5, dilution 1/50</span> → 1 250 µg/mL",
         "<span class=\"cle\">A260/A280 = 1,8</span> → ADN pur ; &lt; 1,8 → protéines"]),
    ],
    [
     sc("1 · Nucléotide et appariements", """<svg viewBox="0 0 660 210" width="100%" role="img" aria-label="Nucléotide et appariements A-T et G-C avec liaisons hydrogène">
      <text x="16" y="24" fill="var(--ac)" font-size="15" font-weight="bold">Du nucléotide à la paire de bases</text>
      <rect x="16" y="44" width="150" height="120" rx="10" fill="var(--card2)" stroke="var(--ac)"/>
      <text x="91" y="64" text-anchor="middle" fill="var(--fg)" font-size="12">Nucléotide</text>
      <circle cx="56" cy="100" r="16" fill="var(--card2)" stroke="var(--dim)"/><text x="56" y="105" text-anchor="middle" fill="var(--fg)" font-size="11">P</text>
      <rect x="88" y="82" width="40" height="36" rx="4" fill="var(--card2)" stroke="var(--dim)"/><text x="108" y="106" text-anchor="middle" fill="var(--fg)" font-size="11">sucre</text>
      <rect x="40" y="132" width="100" height="24" rx="4" fill="var(--card2)" stroke="var(--ac)"/><text x="90" y="149" text-anchor="middle" fill="var(--fg)" font-size="11">base (A, T, G, C)</text>
      <text x="210" y="80" fill="var(--fg)" font-size="13">Adénine A</text><text x="340" y="80" fill="var(--fg)" font-size="13">Thymine T</text>
      <line x1="270" y1="70" x2="270" y2="105" stroke="var(--dim)" stroke-width="1.5" stroke-dasharray="3 3"/><line x1="318" y1="70" x2="318" y2="105" stroke="var(--dim)" stroke-width="1.5" stroke-dasharray="3 3"/>
      <line x1="274" y1="78" x2="314" y2="78" stroke="var(--ac)" stroke-width="2"/><line x1="274" y1="90" x2="314" y2="90" stroke="var(--ac)" stroke-width="2"/>
      <text x="294" y="118" text-anchor="middle" fill="var(--warn)" font-size="10">2 liaisons H</text>
      <text x="210" y="158" fill="var(--fg)" font-size="13">Guanine G</text><text x="340" y="158" fill="var(--fg)" font-size="13">Cytosine C</text>
      <line x1="274" y1="148" x2="314" y2="148" stroke="var(--ac)" stroke-width="2"/><line x1="274" y1="158" x2="314" y2="158" stroke="var(--ac)" stroke-width="2"/><line x1="274" y1="168" x2="314" y2="168" stroke="var(--ac)" stroke-width="2"/>
      <text x="294" y="190" text-anchor="middle" fill="var(--warn)" font-size="10">3 liaisons H → plus stable</text>
      <rect x="420" y="52" width="220" height="120" rx="8" fill="var(--card2)" stroke="var(--dim)"/>
      <text x="434" y="74" fill="var(--ac)" font-size="12" font-weight="bold">Règles</text>
      <text x="434" y="96" fill="var(--fg)" font-size="11">A = T  ·  G ≡ C</text>
      <text x="434" y="116" fill="var(--fg)" font-size="11">Brins antiparallèles</text>
      <text x="434" y="136" fill="var(--fg)" font-size="11">5' → 3' / 3' → 5'</text>
      <text x="434" y="156" fill="var(--dim)" font-size="10">Tm ≈ 2(A+T)+4(G+C)</text>
     </svg>"""),
     sc("2 · La double hélice antiparallèle", """<svg viewBox="0 0 660 190" width="100%" role="img" aria-label="Double hélice avec brins 5 prime 3 prime et appariements">
      <text x="16" y="24" fill="var(--ac)" font-size="15" font-weight="bold">Deux brins complémentaires et antiparallèles</text>
      <path d="M60 50 C150 90 150 130 240 170 C330 130 330 90 420 50" fill="none" stroke="var(--ac)" stroke-width="3"/>
      <path d="M60 170 C150 130 150 90 240 50 C330 90 330 130 420 170" fill="none" stroke="var(--warn)" stroke-width="3"/>
      <g stroke="var(--dim)" stroke-width="1.5" stroke-dasharray="4 3">
        <line x1="95" y1="66" x2="95" y2="156"/><line x1="145" y1="92" x2="145" y2="130"/><line x1="240" y1="50" x2="240" y2="170"/><line x1="335" y1="92" x2="335" y2="130"/><line x1="385" y1="66" x2="385" y2="156"/>
      </g>
      <text x="48" y="44" fill="var(--ac)" font-size="12">5'</text><text x="428" y="44" fill="var(--ac)" font-size="12">3'</text>
      <text x="48" y="186" fill="var(--warn)" font-size="12">3'</text><text x="428" y="186" fill="var(--warn)" font-size="12">5'</text>
      <rect x="452" y="60" width="190" height="104" rx="8" fill="var(--card2)" stroke="var(--dim)"/>
      <text x="466" y="82" fill="var(--fg)" font-size="11">A ↔ T (2 H)</text>
      <text x="466" y="104" fill="var(--fg)" font-size="11">G ↔ C (3 H)</text>
      <text x="466" y="126" fill="var(--fg)" font-size="11">séquence lue 5'→3'</text>
      <text x="466" y="148" fill="var(--dim)" font-size="10">%GC ↑ → Tm ↑</text>
     </svg>"""),
     sc("3 · ADN et ARN : comparaison", """<svg viewBox="0 0 660 180" width="100%" role="img" aria-label="Tableau comparatif ADN et ARN">
      <text x="16" y="24" fill="var(--ac)" font-size="15" font-weight="bold">ADN vs ARN</text>
      <g font-size="12" fill="var(--fg)">
        <rect x="16" y="40" width="628" height="30" fill="var(--card2)" stroke="var(--dim)"/>
        <text x="28" y="60" font-weight="bold">Critère</text><text x="200" y="60" font-weight="bold">ADN</text><text x="420" y="60" font-weight="bold">ARN</text>
        <text x="28" y="88">Sucre</text><text x="200" y="88">désoxyribose</text><text x="420" y="88">ribose</text>
        <text x="28" y="112">Bases</text><text x="200" y="112">A, T, G, C</text><text x="420" y="112">A, U, G, C</text>
        <text x="28" y="136">Structure</text><text x="200" y="136">double hélice</text><text x="420" y="136">souvent simple brin</text>
        <text x="28" y="160">Rôle / stabilité</text><text x="200" y="160">stockage, stable</text><text x="420" y="160">expression, fragile</text>
      </g>
      <line x1="184" y1="40" x2="184" y2="170" stroke="var(--dim)"/><line x1="404" y1="40" x2="404" y2="170" stroke="var(--dim)"/>
     </svg>""")
    ]
))

# ============================================================ FICHE 2
FICHES.append(mk(
    ["BTS1"], BIO, "Chapitre 2 · Réplication, transcription et traduction", SRC_BIO,
    [
     "Le dogme central de la biologie moléculaire décrit le flux de l'information : ADN → ADN (réplication), ADN → ARN (transcription), ARN → protéine (traduction). La réplication est semi-conservative : chaque nouvelle molécule possède un brin ancien et un brin néosynthétisé (expérience de Meselson-Stahl).",
     "La réplication démarre à une origine et progresse en formant une fourche. L'ADN polymérase synthétise le nouveau brin dans le sens 5' → 3' en lisant le brin matrice 3' → 5'. Elle exige une amorce (primer) et ne peut initier sans extrémité 3'-OH libre.",
     "Sur le brin conducteur (leading strand), la synthèse est continue. Sur le brin retardé (lagging strand), elle est discontinue : fragments d'Okazaki. L'ARN polymérase (primase) pose les amorces, la polymérase I les retire, la ligase soude les fragments.",
     "La transcription est réalisée par l'ARN polymérase qui lit le brin matrice 3' → 5' et synthétise un ARN 5' → 3' complémentaire (A=U, G=C). Elle démarre au promoteur et s'arrête au terminateur. Chez les eucaryotes, le transcrit primaire subit épissage (retrait des introns), ajout du chapeau 5' et d'une queue poly-A.",
     "La traduction a lieu sur le ribosome (ARNr + protéines). L'ARNm est lu par codons de 3 nucléotides : 64 codons codent 20 acides aminés, le code est dégénéré. AUG est le codon d'initiation (méthionine) ; UAA, UAG, UGA sont les codons STOP.",
     "L'ARNt, chargé d'un acide aminé, reconnaît le codon par son anticodon complémentaire. La traduction comporte initiation, élongation (formation de liaisons peptidiques) et terminaison. La chaîne d'acides aminés se replie ensuite en protéine fonctionnelle.",
     "Une protéine de n acides aminés est codée par 3n nucléotides (plus le codon STOP, non traduit). Le décalage du cadre de lecture (insertion/délétion d'un nombre non multiple de 3) est une mutation délétère.",
     "Chez les bactéries, transcription et traduction sont couplées dans le cytoplasme ; chez les eucaryotes, la transcription a lieu dans le noyau et la traduction dans le cytoplasme.",
     "La synthèse protéique est ciblée par de nombreux antibiotiques : rifampicine (ARN polymérase bactérienne), tétracyclines (sous-unité 30S), macrolides (50S) — sélectivité liée aux différences de ribosomes.",
     "Applications BIOALC : production de protéines recombinantes (insuline, enzymes), interprétation d'une mutation, RT-PCR (transcription inverse puis PCR de l'ARNm), expression génique et diagnostic moléculaire."
    ],
    [
     qcm("Quelle enzyme réalise la transcription ?", ["L'ADN polymérase", "L'ARN polymérase", "La ligase", "La reverse transcriptase"], 1,
         "L'ARN polymérase transcrit un brin d'ADN en ARN ; la reverse transcriptase copie l'ARN en ADN (RT-PCR)."),
     qcm("Sur le brin retardé, les fragments synthétisés s'appellent :", ["Fragments d'Okazaki", "Introns", "Codons", "Amplicons"], 0,
         "Le brin lagging est synthétisé par fragments d'Okazaki assemblés par la ligase."),
     qcm("Quel codon est un codon d'initiation ?", ["UAA", "AUG", "UGA", "UAG"], 1,
         "AUG code la méthionine et sert de codon d'initiation ; UAA, UAG et UGA sont des codons STOP."),
     qcm("Dans quelle direction l'ADN polymérase synthétise-t-elle ?", ["3' → 5'", "5' → 3'", "Dans les deux sens", "Au hasard"], 1,
         "Toutes les polymérases synthétisent dans le sens 5' → 3' en lisant la matrice 3' → 5'."),
     qcm("Que faut-il pour initier la synthèse d'ADN ?", ["Une amorce à extrémité 3'-OH", "Un codon STOP", "Une queue poly-A", "Un intron"], 0,
         "L'ADN polymérase ne peut allonger qu'à partir d'une amorce portant un 3'-OH libre (posée par la primase)."),
     qcm("Où a lieu la traduction chez un eucaryote ?", ["Dans le noyau", "Dans le cytoplasme", "Dans la mitochondrie uniquement", "Dans le nucléole"], 1,
         "La transcription est nucléaire, la traduction est cytoplasmique (sur les ribosomes)."),
     qt("Pourquoi le code génétique est-il dit dégénéré ?",
        "Parce que 64 codons ne codent que 20 acides aminés : un même acide aminé peut être désigné par plusieurs codons (par exemple la leucine par 6 codons).",
        "La dégénérescence protège contre certaines mutations silencieuses (substitutions qui ne changent pas l'acide aminé)."),
     qcm("Un gène codant compte 903 nucléotides dont le codon STOP. Combien d'acides aminés contient la protéine ?",
         ["903", "301", "300", "302"], 2,
         "903/3 = 301 codons, dont 1 STOP non traduit → 300 acides aminés.",
         "Annotation d'un gène : conversion du nombre de nucléotides en acides aminés.", True),
     qcm("Une protéine de 250 acides aminés est codée par un gène (sans compter le STOP). Quelle est la longueur minimale de la région codante ?",
         ["250 pb", "500 pb", "750 pb", "753 pb"], 2,
         "250 × 3 = 750 nucléotides, soit 750 paires de bases pour l'ADN codant (753 avec le codon STOP).",
         "Dimensionnement d'un amplicone pour un clonage d'expression.", True),
     qcm("Quelle est la séquence d'ARN transcrite à partir du brin matrice 3'-TACGCT-5' ?",
         ["5'-AUGCGA-3'", "3'-AUGCGA-5'", "5'-UACGCT-3'", "5'-ATGCTA-3'"], 0,
         "L'ARN est antiparallèle et complémentaire : A↔U, T↔A, C↔G, G↔C, C↔G, T↔A → 5'-AUGCGA-3'.",
         "Traduction d'une séquence matrice lors d'un exercice de transcription.", True)
    ],
    [
     intro("L'idée en une phrase", "L'ADN se copie, se transcrit en ARN puis se traduit en protéine : trois mécanismes qui lisent toujours la séquence dans un sens précis, 5' vers 3'."),
     formule("Le dogme central", "ADN → ADN → ARN → Protéine", "Réplication · Transcription · Traduction · 1 acide aminé = 1 codon = 3 nucléotides"),
     grille("Les 3 mécanismes", [
         ["Réplication", "ADN polymérase, amorce, leading/lagging", "ADN → 2 ADN identiques"],
         ["Transcription", "ARN polymérase, promoteur, épissage", "ADN → ARNm"],
         ["Traduction", "Ribosome, ARNt, codons", "ARNm → protéine"]]),
     liste("Les points clés", [
         "Semi-conservatif : un brin ancien + un brin neuf à chaque réplication",
         "Polymérases : synthèse 5'→3', lecture de la matrice 3'→5'",
         "64 codons / 20 acides aminés · AUG = initiation · UAA/UAG/UGA = STOP",
         "Eucaryotes : noyau (transcription) → cytoplasme (traduction)"]),
     etapes("De l'ADN à la protéine", [
         "Réplication : ouverture de la fourche, amorces, élongation, ligature",
         "Transcription : fixation de l'ARN polymérase sur le promoteur",
         "Épissage (eucaryotes) : retrait des introns, chapeau 5' et poly-A 3'",
         "Traduction : initiation (AUG), élongation (liaisons peptidiques), STOP",
         "Repliement et modifications post-traductionnelles de la protéine"]),
     attention("⚠️ Les pièges classiques", [
         "Oublier que la polymérase ne synthétise qu'en 5'→3'",
         "Confondre brin matrice (lu 3'→5') et brin codant (identique à l'ARNm, T→U)",
         "Compter le codon STOP comme un acide aminé",
         "Croire que la traduction a lieu dans le noyau chez les eucaryotes",
         "Oublier l'épissage : le gène eucaryote contient des introns"]),
     exemples("En chiffres (à savoir refaire)", [
         "<span class=\"cle\">903 nt / 3 = 301 codons − 1 STOP</span> → 300 AA",
         "<span class=\"cle\">250 AA × 3</span> = 750 pb de région codante",
         "<span class=\"cle\">Matrice 3'-TACGCT-5'</span> → ARNm 5'-AUGCGA-3'",
         "<span class=\"cle\">AUG</span> = Met / initiation",
         "<span class=\"cle\">UAA, UAG, UGA</span> = terminaison"]),
    ],
    [
     sc("1 · Le dogme central", """<svg viewBox="0 0 660 150" width="100%" role="img" aria-label="Dogme central ADN réplication transcription traduction protéine">
      <defs><marker id="@@a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
      <rect x="20" y="50" width="110" height="52" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="75" y="82" text-anchor="middle" fill="var(--fg)" font-size="16" font-weight="bold">ADN</text>
      <path d="M75 46 C55 18 105 18 85 46" fill="none" stroke="var(--warn)" stroke-width="2" marker-end="url(#@@a)"/><text x="118" y="28" fill="var(--warn)" font-size="11">réplication</text>
      <line x1="132" y1="76" x2="232" y2="76" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/><text x="182" y="64" text-anchor="middle" fill="var(--ac)" font-size="11">transcription</text>
      <rect x="236" y="50" width="110" height="52" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="291" y="82" text-anchor="middle" fill="var(--fg)" font-size="16" font-weight="bold">ARNm</text>
      <line x1="348" y1="76" x2="448" y2="76" stroke="var(--ac)" stroke-width="2" marker-end="url(#@@a)"/><text x="398" y="64" text-anchor="middle" fill="var(--ac)" font-size="11">traduction</text>
      <rect x="452" y="50" width="170" height="52" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="537" y="76" text-anchor="middle" fill="var(--fg)" font-size="14" font-weight="bold">Protéine</text><text x="537" y="92" text-anchor="middle" fill="var(--dim)" font-size="10">acides aminés</text>
      <text x="330" y="130" text-anchor="middle" fill="var(--dim)" font-size="11">L'information circule toujours dans le sens 5' → 3'</text>
     </svg>"""),
     sc("2 · La fourche de réplication", """<svg viewBox="0 0 660 200" width="100%" role="img" aria-label="Fourche de réplication avec brin conducteur et fragments d'Okazaki">
      <text x="16" y="24" fill="var(--ac)" font-size="15" font-weight="bold">Réplication semi-conservative à la fourche</text>
      <path d="M120 40 L300 100 L120 160" fill="none" stroke="var(--dim)" stroke-width="3"/>
      <line x1="120" y1="40" x2="500" y2="40" stroke="var(--ac)" stroke-width="3"/><line x1="120" y1="160" x2="500" y2="160" stroke="var(--warn)" stroke-width="3"/>
      <text x="340" y="32" fill="var(--ac)" font-size="11">brin conducteur (continu)</text>
      <g stroke="var(--warn)" stroke-width="3"><line x1="320" y1="160" x2="360" y2="160"/><line x1="370" y1="160" x2="410" y2="160"/><line x1="420" y1="160" x2="460" y2="160"/></g>
      <text x="360" y="182" fill="var(--warn)" font-size="11">fragments d'Okazaki (lagging)</text>
      <rect x="516" y="70" width="130" height="60" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="581" y="92" text-anchor="middle" fill="var(--fg)" font-size="11">Polymérase</text><text x="581" y="110" text-anchor="middle" fill="var(--dim)" font-size="10">5'→3'</text>
      <text x="20" y="120" fill="var(--dim)" font-size="11">ADN parental</text>
      <text x="305" y="120" fill="var(--dim)" font-size="11">fourche</text>
      <text x="330" y="60" fill="var(--dim)" font-size="10">amorce 3'-OH indispensable</text>
     </svg>"""),
     sc("3 · Codon, anticodon et ribosome", """<svg viewBox="0 0 660 170" width="100%" role="img" aria-label="Traduction : codon de l'ARNm reconnu par l'anticodon de l'ARNt sur le ribosome">
      <text x="16" y="24" fill="var(--ac)" font-size="15" font-weight="bold">La traduction : un codon = un acide aminé</text>
      <rect x="16" y="44" width="628" height="44" rx="6" fill="var(--card2)" stroke="var(--dim)"/>
      <text x="60" y="72" fill="var(--fg)" font-size="12">ARNm 5'</text>
      <g fill="var(--ac)" font-size="12"><text x="150" y="72">AUG</text><text x="260" y="72">GCU</text><text x="370" y="72">UUC</text><text x="480" y="72">UAA</text></g>
      <g stroke="var(--warn)" stroke-width="1.5" stroke-dasharray="3 3"><line x1="150" y1="44" x2="150" y2="88"/><line x1="260" y1="44" x2="260" y2="88"/><line x1="370" y1="44" x2="370" y2="88"/><line x1="480" y1="44" x2="480" y2="88"/></g>
      <text x="560" y="72" fill="var(--warn)" font-size="10">STOP</text>
      <rect x="120" y="104" width="300" height="46" rx="22" fill="var(--card2)" stroke="var(--ac)"/>
      <text x="270" y="124" text-anchor="middle" fill="var(--fg)" font-size="12">Ribosome (ARNr + protéines)</text>
      <text x="270" y="140" text-anchor="middle" fill="var(--dim)" font-size="10">anticodon UAC ↔ codon AUG (Met)</text>
      <text x="450" y="120" fill="var(--fg)" font-size="11">ARNt = adaptateur</text>
      <text x="450" y="140" fill="var(--dim)" font-size="10">liaisons peptidiques</text>
     </svg>""")
    ]
))

# Exécution des parties 2 à 5 (elles complètent la liste FICHES)
import os
_HERE = os.path.dirname(os.path.abspath(__file__))
for _part in ('gen_bioalc_mat_c_p2.py', 'gen_bioalc_mat_c_p3.py',
              'gen_bioalc_mat_c_p4.py', 'gen_bioalc_mat_c_p5.py'):
    with open(os.path.join(_HERE, _part), encoding='utf-8') as _fh:
        exec(compile(_fh.read(), _part, 'exec'))

_OUT = os.path.join(_HERE, 'bioalc-mat-part-C.json')
with open(_OUT, 'w', encoding='utf-8') as _fh:
    json.dump({"fiches": FICHES}, _fh, ensure_ascii=False, indent=1)
    _fh.write('\n')
print('Fiches ecrites:', len(FICHES))
for _i, _f in enumerate(FICHES, 1):
    print(_i, _f['matiere'][:6], _f['titre'][:46], 'pts', len(_f['points']),
          'Q', len(_f['questions']), 'calc',
          sum(1 for q in _f['questions'] if q.get('calcul')),
          'ctx', sum(1 for q in _f['questions'] if q.get('contexte')),
          'blocs', len(_f['affichage']), 'svg', len(_f['schema']))
