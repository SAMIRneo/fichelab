# -*- coding: utf-8 -*-
"""Génère data/physchim-part-A.json : fiches U4 BTS BIOALC, chapitres 1 à 5.

Modèle strict : FICHE_UV de index.html (points / questions / affichage / schema).
Sources vérifiées : arrêté 12-03-2024 modifié 24-06-2025 (U4), VIM3 JCGM 200:2012,
GUM JCGM 100:2008, IUPAC Gold Book, ISO 648/1042, LibreTexts, Hann (Nernst).
"""
import json
import os
import re

FILIERES = ["bts-bio"]
ANNEES = ["BTS1"]
MATIERE = "Physique-chimie et instrumentation"
REF = "Référentiel BTS BIOALC 2024/2025, U4 (arrêté du 12 mars 2024 modifié par l'arrêté du 24 juin 2025, RNCP38884)"


def qcm(q, options, correct, correction):
    return {"type": "qcm", "q": q, "options": options, "correct": correct, "correction": correction}


def qt(q, reponse, correction):
    return {"type": "texte", "q": q, "reponse": reponse, "correction": correction}


def fiche(titre, source, points, questions, affichage, schema):
    return {
        "filieres": FILIERES,
        "annees": ANNEES,
        "matiere": MATIERE,
        "titre": titre,
        "source": source,
        "points": points,
        "questions": questions,
        "affichage": affichage,
        "schema": schema,
    }


# ===========================================================================
# CHAPITRE 1 — La mesure et les incertitudes
# ===========================================================================
C1 = fiche(
    "Chapitre 1 · La mesure et les incertitudes",
    REF + " · VIM3 JCGM 200:2012 (2.3, 2.13 à 2.16, 2.26, 2.30, 2.35 à 2.38, 2.41) · GUM JCGM 100:2008 · ISO/IEC 17025 · ISO 5725",
    [
        "Une grandeur est une propriété quantifiable (longueur, masse, concentration, pH…). Mesurer, c'est la comparer à une unité de référence : le résultat s'écrit toujours « valeur numérique × unité ». Le mesurande est la grandeur soumise à mesurage (VIM 2.3).",
        "Le SI repose sur 7 grandeurs de base : longueur (mètre m), masse (kilogramme kg), temps (seconde s), courant électrique (ampère A), température thermodynamique (kelvin K), quantité de matière (mole mol) et intensité lumineuse (candela cd). Depuis 2019, les 7 unités sont définies par des constantes fondamentales.",
        "Unités utiles au laboratoire : volume litre (1 L = 10⁻³ m³, unité hors SI acceptée), concentration mol·L⁻¹, masse volumique g·mL⁻¹ (= kg·L⁻¹ = 10³ kg·m⁻³), pression pascal (1 bar = 10⁵ Pa), température T(K) = t(°C) + 273,15. Le degré Celsius est une unité dérivée acceptée avec le SI.",
        "Un résultat complet comprend quatre éléments : la valeur mesurée, l'incertitude, l'unité et les conditions de mesure. Notation normalisée : x = (valeur ± U) unité, avec U = k · u (k = 2 donne un niveau de confiance d'environ 95 % pour une distribution normale).",
        "L'incertitude absolue u(x) a la même unité que la grandeur ; l'incertitude relative (sans unité) vaut uᵣ = u(x)/|x|, souvent exprimée en %. Exemple : V = (10,00 ± 0,02) mL donne uᵣ = 0,02/10,00 = 0,2 %.",
        "Erreur et incertitude ne sont pas synonymes : l'erreur de mesure = valeur mesurée − valeur de référence (elle est signée et généralement inconnue), alors que l'incertitude (VIM 2.26) est un paramètre non négatif qui caractérise la dispersion des valeurs attribuées au mesurande. On ne chiffre pas une erreur inconnue : on chiffre l'incertitude.",
        "La justesse (VIM 2.14) est l'accord entre la moyenne d'une série de résultats et une valeur de référence : elle traduit l'erreur systématique (biais). La fidélité (VIM 2.15) est l'accord entre résultats indépendants : elle traduit l'erreur aléatoire (écart-type). Une mesure peut être très fidèle et pourtant systématiquement fausse ; l'exactitude (VIM 2.13) réunit les deux.",
        "Répétabilité et reproductibilité (ISO 5725) : en répétabilité, mêmes opérateur, appareil, laboratoire et court intervalle de temps ; en reproductibilité, opérateur, appareil ou laboratoire changent. C'est la fidélité intermédiaire qui est ensuite utilisée dans le bilan d'incertitude de la méthode.",
        "Les chiffres significatifs sont tous les chiffres certains plus le premier chiffre incertain. Les zéros entre chiffres non nuls et les zéros à droite de la virgule sont significatifs : 0,00450 possède 3 chiffres significatifs, 10,00 en possède 4. Le résultat s'arrête au rang de l'incertitude (u arrondie à 1 chiffre, ou 2 si son premier chiffre est 1 ou 2).",
        "Arrondis : addition/soustraction → arrondir à la dernière décimale la moins précise (12,1 + 0,236 = 12,3) ; multiplication/division → garder le plus petit nombre de chiffres significatifs ; logarithme → le nombre de décimales du résultat égale le nombre de chiffres significatifs de l'argument ([H₃O⁺] = 5,0 × 10⁻³, soit 2 chiffres, donne pH = 2,30).",
        "Évaluations A et B : l'évaluation de type A utilise la statistique de n mesures répétées (u = s/√n pour l'écart-type de la moyenne) ; l'évaluation de type B utilise d'autres informations (certificat d'étalonnage, résolution, tolérance constructeur). Pour une incertitude bornée à ±a sans autre information (loi uniforme), u = a/√3.",
        "Propagation et bilan (VIM 2.33) : pour une somme, u²c = Σ u²i ; pour un produit ou quotient, uᵣ,c² = Σ u²r,i (grandeurs indépendantes). On calcule ensuite l'incertitude élargie U = k · u_c, puis on exprime le résultat. Traçabilité, étalonnage, matériau de référence certifié et carte de contrôle (ISO/IEC 17025) complètent la démarche qualité.",
    ],
    [
        qcm("Combien de grandeurs de base compose le Système international d'unités ?",
            ["5", "6", "7", "9"], 2,
            "Le SI compte 7 grandeurs de base : m, kg, s, A, K, mol et cd. Toutes les autres unités (L, Pa, mol/L, °C…) en sont dérivées."),
        qcm("Pour V = (10,00 ± 0,02) mL, quelle est l'incertitude relative ?",
            ["0,02 %", "0,2 %", "2 %", "0,002 %"], 1,
            "uᵣ = u/|V| = 0,02/10,00 = 0,002 = 0,2 %. L'incertitude absolue, elle, vaut 0,02 mL."),
        qcm("Un pHmètre donne des lectures très regroupées mais décalées de 0,3 unité par rapport à un tampon certifié. Que dire ?",
            ["La mesure est juste mais peu fidèle", "La mesure est fidèle mais peu juste", "La mesure est exacte", "La fidélité suffit à garantir l'exactitude"], 1,
            "Faible dispersion = bonne fidélité ; biais de 0,3 = mauvaise justesse. Un biais stable se corrige par étalonnage, une dispersion ne se corrige pas."),
        qcm("Combien de chiffres significatifs contient le nombre 0,00450 ?",
            ["2", "3", "4", "5"], 1,
            "Les zéros avant le 4 ne sont pas significatifs ; le zéro final après la virgule l'est : 4, 5 et 0, soit 3 chiffres significatifs."),
        qcm("Quelle est la différence entre incertitude et erreur de mesure ?",
            ["Ce sont deux synonymes", "L'erreur est toujours positive, l'incertitude est signée", "L'erreur compare à la valeur de référence (et reste inconnue), l'incertitude caractérise une dispersion", "L'incertitude mesure le biais"], 2,
            "VIM 2.26 : l'incertitude est un paramètre non négatif de dispersion ; l'erreur (2.16) est la différence avec la valeur de référence, le plus souvent inconnue."),
        qcm("Estimer u par s/√n à partir de n mesures répétées correspond à :",
            ["Une évaluation de type B", "Une évaluation de type A", "Une incertitude élargie", "Un biais de mesure"], 1,
            "Le type A repose sur une analyse statistique de séries de mesurages ; le type B s'appuie sur d'autres informations (certificat, résolution, tolérance)."),
        qt("Écrire correctement le résultat d'une pesée : 5 répétitions donnent une moyenne de 2,0348 g, un écart-type de la moyenne u = 0,0006 g et un facteur k = 2.",
           "m = (2,0348 ± 0,0012) g, avec U = k · u = 2 × 0,0006 = 0,0012 g (niveau de confiance ≈ 95 %).",
           "On arrondit d'abord u à 1 ou 2 chiffres significatifs, puis on calcule U = k·u et on arrondit la valeur au même rang décimal que U."),
        qt("Pourquoi arrondit-on [H₃O⁺] = 5,0 × 10⁻³ mol/L en pH = 2,30 et non 2,3010 ?",
           "Parce que l'argument n'a que 2 chiffres significatifs : le logarithme doit avoir 2 décimales. Les décimales du pH traduisent la précision de la concentration.",
           "Règle des logarithmes : nombre de décimales du résultat = nombre de chiffres significatifs de l'argument."),
    ],
    [
        {"type": "intro", "titre": "L’idée en une phrase",
         "texte": "Mesurer, c’est comparer une grandeur à une unité. Un résultat n’est complet que s’il annonce aussi ce qu’on ne sait pas : son incertitude."},
        {"type": "formule", "titre": "La notation à connaître par cœur",
         "eq": "x = (valeur ± U) unité   ·   U = k · u_c",
         "leg": "u_c : incertitude-type composée · k : facteur d’élargissement (k = 2 → ≈ 95 %) · U : incertitude élargie"},
        {"type": "grille", "titre": "Trois grandeurs à ne pas confondre", "items": [
            ["u(x)", "Incertitude absolue : écart-type ou demi-étendue, dans la même unité que x", "mL, g, mol·L⁻¹…"],
            ["uᵣ = u/|x|", "Incertitude relative : incertitude rapportée à la valeur, sans unité", "sans unité ou %"],
            ["U = k·u_c", "Incertitude élargie : intervalle annoncé avec un niveau de confiance", "même unité que x"]]},
        {"type": "liste", "titre": "Justesse, fidélité, exactitude", "items": [
            "Justesse = accord de la moyenne avec la valeur de référence → erreur systématique (biais)",
            "Fidélité = accord entre mesures répétées → erreur aléatoire (écart-type)",
            "Exactitude = justesse + fidélité : elle ne se chiffre pas, seul le biais ou l’écart-type se chiffrent",
            "Répétabilité : mêmes conditions · reproductibilité : opérateur/appareil/laboratoire différents"]},
        {"type": "etapes", "titre": "Le bilan d’incertitude, pas à pas", "items": [
            "Définir le mesurande et le modèle de mesure (fonction reliant grandeur de sortie et grandeurs d’entrée)",
            "Identifier et quantifier chaque composante : type A (s/√n) ou type B (certificat, résolution, tolérance)",
            "Propager : somme → u²c = Σ u²i ; produit/quotient → u²r,c = Σ u²r,i",
            "Choisir le facteur d’élargissement k (souvent 2) et calculer U = k · u_c",
            "Arrondir u et U puis rédiger : x = (valeur ± U) unité, avec k et le niveau de confiance"]},
        {"type": "attention", "titre": "⚠️ Les pièges classiques", "items": [
            "Confondre erreur (inconnue, signée) et incertitude (dispersion, positive)",
            "Croire qu’une mesure fidèle est automatiquement juste : un biais reste possible",
            "Arrondir trop tôt : on garde des chiffres pendant le calcul, on arrondit à la fin",
            "Oublier l’unité ou le facteur k dans l’expression du résultat",
            "Donner un pH avec trop de décimales par rapport aux chiffres significatifs de [H₃O⁺]"]},
        {"type": "exemples", "titre": "En chiffres (à savoir refaire)", "items": [
            "<span class=\"cle\">10,00 ± 0,02 mL</span> → uᵣ = 0,2 %",
            "<span class=\"cle\">0,00450</span> → 3 chiffres significatifs ; <span class=\"cle\">10,00</span> → 4",
            "<span class=\"cle\">12,1 + 0,236</span> = 12,3 (arrondi à la décimale la moins précise)",
            "<span class=\"cle\">[H₃O⁺] = 5,0 × 10⁻³</span> → pH = 2,30 (2 décimales)",
            "<span class=\"cle\">u = 0,0006 g, k = 2</span> → m = (2,0348 ± 0,0012) g"]}
    ],
    [
        {"titre": "1 · Justesse et fidélité : les quatre cibles", "svg": """<svg viewBox="0 0 660 175" width="100%" role="img" aria-label="Quatre cibles : juste et fidèle, fidèle mais pas juste, juste mais pas fidèle, ni juste ni fidèle">
    <defs><marker id="pc1a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
    <text x="16" y="22" fill="var(--ac)" font-size="14" font-weight="bold">Justesse et fidélité se jugent sur une série de mesures</text>
    <g fill="var(--card2)" stroke="var(--dim)" stroke-width="1.5">
      <circle cx="95" cy="88" r="42"/><circle cx="95" cy="88" r="22"/>
      <circle cx="265" cy="88" r="42"/><circle cx="265" cy="88" r="22"/>
      <circle cx="435" cy="88" r="42"/><circle cx="435" cy="88" r="22"/>
      <circle cx="605" cy="88" r="42"/><circle cx="605" cy="88" r="22"/>
    </g>
    <g fill="var(--warn)"><circle cx="95" cy="88" r="3"/><circle cx="265" cy="88" r="3"/><circle cx="435" cy="88" r="3"/><circle cx="605" cy="88" r="3"/></g>
    <g fill="var(--ac)"><circle cx="88" cy="82" r="3"/><circle cx="100" cy="92" r="3"/><circle cx="92" cy="96" r="3"/>
       <circle cx="250" cy="66" r="3"/><circle cx="258" cy="70" r="3"/><circle cx="254" cy="74" r="3"/>
       <circle cx="408" cy="72" r="3"/><circle cx="462" cy="100" r="3"/><circle cx="420" cy="112" r="3"/>
       <circle cx="578" cy="66" r="3"/><circle cx="632" cy="108" r="3"/><circle cx="590" cy="120" r="3"/></g>
    <g text-anchor="middle" fill="var(--fg)" font-size="11">
      <text x="95" y="146">juste et fidèle</text><text x="265" y="146">fidèle, pas juste</text>
      <text x="435" y="146">juste, pas fidèle</text><text x="605" y="146">ni juste ni fidèle</text>
    </g>
    <line x1="16" y1="160" x2="644" y2="160" stroke="var(--warn)" stroke-width="1" stroke-dasharray="5 4" marker-end="url(#pc1a)"/>
    <text x="16" y="173" fill="var(--dim)" font-size="11">Point rouge = valeur de référence · points bleus = résultats répétés · l’exactitude réunit justesse et fidélité</text>
   </svg>"""},
        {"titre": "2 · Anatomie d’un résultat de mesure complet", "svg": """<svg viewBox="0 0 660 190" width="100%" role="img" aria-label="Détail d'un résultat complet : valeur, incertitude, facteur k, unité et conditions">
    <defs><marker id="pc1b" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
    <rect x="170" y="52" width="320" height="58" rx="10" fill="var(--card2)" stroke="var(--ac)" stroke-width="2"/>
    <text x="330" y="90" text-anchor="middle" fill="var(--fg)" font-size="24" font-weight="bold">10,00 ± 0,02 mL</text>
    <line x1="250" y1="110" x2="196" y2="142" stroke="var(--ac)" stroke-width="1.5" marker-end="url(#pc1b)"/>
    <line x1="330" y1="110" x2="330" y2="142" stroke="var(--ac)" stroke-width="1.5" marker-end="url(#pc1b)"/>
    <line x1="410" y1="110" x2="464" y2="142" stroke="var(--ac)" stroke-width="1.5" marker-end="url(#pc1b)"/>
    <text x="190" y="158" text-anchor="middle" fill="var(--fg)" font-size="11">valeur mesurée</text>
    <text x="190" y="172" text-anchor="middle" fill="var(--dim)" font-size="10">10,00 mL</text>
    <text x="330" y="158" text-anchor="middle" fill="var(--fg)" font-size="11">incertitude absolue</text>
    <text x="330" y="172" text-anchor="middle" fill="var(--dim)" font-size="10">u = 0,02 mL</text>
    <text x="470" y="158" text-anchor="middle" fill="var(--fg)" font-size="11">unité + conditions</text>
    <text x="470" y="172" text-anchor="middle" fill="var(--dim)" font-size="10">20 °C, k = 2</text>
    <text x="16" y="28" fill="var(--ac)" font-size="13" font-weight="bold">uᵣ = u/|x| = 0,02/10,00 = 0,2 %</text>
    <line x1="16" y1="36" x2="150" y2="36" stroke="var(--warn)" stroke-width="1" stroke-dasharray="4 3"/>
    <text x="16" y="48" fill="var(--warn)" font-size="11">U = k · u ≈ 2 u → ≈ 95 %</text>
   </svg>"""},
        {"titre": "3 · Le bilan d’incertitude en 5 étapes", "svg": """<svg viewBox="0 0 660 170" width="100%" role="img" aria-label="Cinq étapes du bilan d'incertitude : modèle, composantes, propagation, élargissement, expression">
    <defs><marker id="pc1c" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
    <g font-size="11" text-anchor="middle">
      <rect x="8" y="48" width="116" height="60" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="66" y="72" fill="var(--ac)" font-weight="bold">1. Modèle</text><text x="66" y="90" fill="var(--fg)">mesurande</text><text x="66" y="104" fill="var(--fg)">+ fonction</text>
      <line x1="126" y1="78" x2="142" y2="78" stroke="var(--ac)" stroke-width="2" marker-end="url(#pc1c)"/>
      <rect x="146" y="48" width="116" height="60" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="204" y="72" fill="var(--ac)" font-weight="bold">2. Composantes</text><text x="204" y="90" fill="var(--fg)">type A : s/√n</text><text x="204" y="104" fill="var(--fg)">type B : a/√3</text>
      <line x1="264" y1="78" x2="280" y2="78" stroke="var(--ac)" stroke-width="2" marker-end="url(#pc1c)"/>
      <rect x="284" y="48" width="116" height="60" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="342" y="72" fill="var(--ac)" font-weight="bold">3. Propagation</text><text x="342" y="90" fill="var(--fg)">u²c = Σ u²i</text><text x="342" y="104" fill="var(--fg)">ou u²r,c = Σ u²r,i</text>
      <line x1="402" y1="78" x2="418" y2="78" stroke="var(--ac)" stroke-width="2" marker-end="url(#pc1c)"/>
      <rect x="422" y="48" width="106" height="60" rx="8" fill="var(--card2)" stroke="var(--ac)"/><text x="475" y="72" fill="var(--ac)" font-weight="bold">4. Élargir</text><text x="475" y="90" fill="var(--fg)">U = k · u_c</text><text x="475" y="104" fill="var(--fg)">k = 2</text>
      <line x1="530" y1="78" x2="546" y2="78" stroke="var(--ac)" stroke-width="2" marker-end="url(#pc1c)"/>
      <rect x="550" y="48" width="102" height="60" rx="8" fill="var(--card2)" stroke="var(--warn)"/><text x="601" y="72" fill="var(--warn)" font-weight="bold">5. Rédiger</text><text x="601" y="90" fill="var(--fg)">valeur ± U</text><text x="601" y="104" fill="var(--fg)">+ unité</text>
    </g>
    <line x1="16" y1="130" x2="644" y2="130" stroke="var(--dim)" stroke-width="1" stroke-dasharray="4 3"/>
    <text x="16" y="150" fill="var(--dim)" font-size="11">Traçabilité : étalonnage · matériau de référence certifié · carte de contrôle · ISO/IEC 17025</text>
    <text x="16" y="166" fill="var(--warn)" font-size="11">Un résultat sans incertitude n’est pas un résultat exploitable en contrôle qualité.</text>
   </svg>"""}
    ]
)


# ===========================================================================
# CHAPITRE 2 — Solutions et concentrations
# ===========================================================================
C2 = fiche(
    "Chapitre 2 · Solutions et concentrations",
    REF + " · IUPAC Gold Book (amount concentration, density, dilution) · ISO 648 et ISO 1042 (verrerie jaugée classe A) · Chimactiv/AgroParisTech et Unisciel (préparation de solutions)",
    [
        "Une solution est un mélange homogène d'un solvant (généralement l'eau) et d'un ou plusieurs solutés. La concentration rapporte la quantité de soluté au VOLUME DE SOLUTION final, et non au volume de solvant : c'est l'erreur la plus fréquente.",
        "Concentration molaire (concentration en quantité de matière) : c = n/V, en mol·L⁻¹ ; n = m/M avec M la masse molaire en g·mol⁻¹. Une mole contient N_A = 6,022 140 76 × 10²³ entités (valeur exacte depuis la redéfinition du SI en 2019).",
        "Concentration massique : C_m = m(soluté)/V(solution) en g·L⁻¹ ; relation c = C_m/M. Une solution à 0,154 mol/L de NaCl (M = 58,44 g/mol) contient 9,0 g/L, soit 0,9 % (m/v).",
        "Masse volumique ρ = m/V : 1 g·mL⁻¹ = 1 kg·L⁻¹ = 10³ kg·m⁻³. L'eau pure a ρ ≈ 1,0000 g·mL⁻¹ à 4 °C et 0,9982 g·mL⁻¹ à 20 °C. Pour 25,0 mL d'éthanol (ρ = 0,789 g/mL), la masse est 19,7 g.",
        "Pourcentages : %(m/m) = m(soluté)/m(solution) × 100 ; %(v/v) = V(soluté)/V(solution) × 100 (exemple : éthanol 70 % vol) ; %(m/v) = m(soluté en g)/V(solution en mL) × 100 (exemple : sérum physiologique 0,9 % m/v = 9 g/L).",
        "Traces : en solution aqueuse diluée, 1 ppm ≈ 1 mg/L (ou 1 mg/kg en masse) et 1 ppb ≈ 1 µg/L ; 1 % = 10 000 ppm. Préciser toujours la base (masse, volume ou molarité) d'un pourcentage.",
        "Dilution : la quantité de soluté ne change pas, seul le volume augmente. Relation C₁V₁ = C₂V₂, avec facteur de dilution F = C₁/C₂ = V₂/V₁. Exemple : 25,0 mL d'une solution à 0,100 mol/L complétés à 250,0 mL donnent 0,0100 mol/L (F = 10).",
        "Dilutions en série : le facteur total est le produit des facteurs successifs (1/10 puis 1/10 = 1/100). Après une mesure (absorbance, conductivité), on multiplie toujours la concentration lue par le facteur de dilution pour retrouver la concentration de l'échantillon initial.",
        "Verrerie jaugée : la fiole jaugée sert à CONTENIR un volume exact (trait sur le col + bouchon), la pipette volumétrique à DÉLIVRER un volume unique (un seul trait), la burette à délivrer un volume variable gradué, l'éprouvette donne une approximation rapide. La classe A est plus précise que la classe B.",
        "Tolérances classe A (ISO 648 / ISO 1042) : pipette 10 mL ± 0,02 mL ; fiole 50 mL ± 0,05 mL ; burette 25 mL ± 0,03 mL. Lire le trait de jauge à hauteur des yeux, le bas du ménisque affleurant le trait pour un liquide aqueux.",
        "Préparer une solution par dilution : pipeter V₁ de solution mère, transvaser dans une fiole jaugée de volume V₂, rincer le bec 2 à 3 fois, compléter avec le solvant jusqu'au trait, boucher et homogénéiser par 8 à 10 retournements. Ne jamais dépasser le trait.",
        "Sécurité et traçabilité : ajouter toujours l'acide dans l'eau (« acid to water »), porter EPI, étiqueter (nom, concentration, date, initiales) et noter le facteur de dilution dans le cahier de laboratoire.",
    ],
    [
        qcm("Dans c = n/V, que représente V ?",
            ["Le volume de solvant ajouté", "Le volume final de solution", "Le volume du récipient vide", "La masse volumique"], 1,
            "V est le volume final de la solution (lu sur la fiole jaugée), pas celui du seul solvant : la dissolution peut changer le volume."),
        qcm("Un sérum physiologique à 0,9 % (m/v) de NaCl contient :",
            ["0,9 g/L", "9 g/L", "90 g/L", "0,09 g/L"], 1,
            "0,9 g pour 100 mL, soit 0,9 × 10 = 9 g/L (c ≈ 0,154 mol/L avec M(NaCl) = 58,44 g/mol)."),
        qcm("Une solution mère à 0,200 mol/L est diluée au 1/20. Quelle est la concentration finale ?",
            ["0,100 mol/L", "0,0200 mol/L", "0,0100 mol/L", "4,00 mol/L"], 2,
            "C₂ = C₁/F = 0,200/20 = 0,0100 mol/L. Le facteur F = V₂/V₁ = C₁/C₂."),
        qcm("Quelle verrerie choisir pour préparer exactement 100,0 mL de solution ?",
            ["Une éprouvette graduée", "Un bécher", "Une fiole jaugée de 100 mL", "Un erlenmeyer"], 2,
            "Seule la fiole jaugée est certifiée pour contenir un volume exact (trait de jauge). L'éprouvette et le bécher sont beaucoup moins précis."),
        qcm("Quelle masse de 25,0 mL d'éthanol (ρ = 0,789 g/mL) mesure-t-on ?",
            ["19,7 mg", "19,7 g", "31,7 g", "0,0317 g"], 1,
            "m = ρ·V = 0,789 × 25,0 = 19,725 g, arrondi à 19,7 g (3 chiffres significatifs)."),
        qcm("Quelle est la tolérance d'une pipette volumétrique classe A de 10 mL (ISO 648) ?",
            ["± 0,002 mL", "± 0,02 mL", "± 0,2 mL", "± 1 mL"], 1,
            "Une pipette jaugée classe A de 10 mL a une tolérance de ± 0,02 mL ; celle d'une fiole de 50 mL est de ± 0,05 mL."),
        qt("10,0 mL d'une solution à 0,150 mol/L sont complétés à 250,0 mL. Calculer C₂ et le facteur de dilution.",
           "F = V₂/V₁ = 250,0/10,0 = 25 ; C₂ = C₁/F = 0,150/25 = 0,00600 mol/L (vérification : C₁V₁ = 0,150 × 0,0100 = 1,50 × 10⁻³ mol = C₂V₂).",
           "La quantité de soluté est conservée : C₁V₁ = C₂V₂. Le résultat est rendu avec 3 chiffres significatifs comme les données."),
        qt("Pourquoi rincer le bec de la pipette et le col de la fiole lors d'une dilution au volume ?",
           "Pour transvaser quantitativement tout le soluté : les gouttes restées sur les parois doivent rejoindre la solution, sinon la concentration finale serait trop faible.",
           "Le rinçage 2 à 3 fois avec le solvant garantit que n est conservé ; c'est une étape critique de la préparation."),
    ],
    [
        {"type": "intro", "titre": "L’idée en une phrase",
         "texte": "Diluer, c’est ajouter du solvant sans toucher à la quantité de soluté : la concentration baisse, le nombre de moles reste le même."},
        {"type": "formule", "titre": "Les deux formules à connaître",
         "eq": "c = n/V = m/(M·V)      et      C₁V₁ = C₂V₂",
         "leg": "c en mol·L⁻¹ · n en mol · V en L · M en g·mol⁻¹ · F = C₁/C₂ = V₂/V₁"},
        {"type": "grille", "titre": "Les 3 façons d’exprimer une concentration", "items": [
            ["c = n/V", "Concentration molaire : nombre de moles par litre de solution", "mol·L⁻¹"],
            ["C_m = m/V", "Concentration massique : masse de soluté par litre de solution", "g·L⁻¹"],
            ["ρ = m/V", "Masse volumique : masse d’un volume de solution (ou de solvant)", "g·mL⁻¹"]]},
        {"type": "liste", "titre": "Verrerie jaugée : contenir ou délivrer", "items": [
            "Fiole jaugée : contient un volume exact, un trait sur le col, avec bouchon (classe A : 50 mL ± 0,05 mL)",
            "Pipette volumétrique : délivre un seul volume exact, un seul trait (10 mL ± 0,02 mL)",
            "Burette : délivre un volume variable gradué (25 mL ± 0,03 mL en classe A)",
            "Éprouvette : lecture rapide et approximative, jamais pour une dilution quantitative"]},
        {"type": "etapes", "titre": "Préparer une dilution, pas à pas", "items": [
            "Calculer V₁ = C₂V₂/C₁ et choisir une fiole de volume V₂",
            "Pipeter V₁ de solution mère (bouche pipetteuse, jamais à la bouche)",
            "Transvaser dans la fiole puis rincer le bec 2 à 3 fois avec le solvant",
            "Compléter au trait de jauge, à hauteur des yeux, puis boucher",
            "Retourner 8 à 10 fois pour homogénéiser et noter le facteur de dilution F"]},
        {"type": "attention", "titre": "⚠️ Erreurs fréquentes", "items": [
            "Confondre volume de solvant et volume final de solution",
            "Lire le ménisque de travers (parallaxe) ou remplir au-dessus du trait",
            "Oublier de multiplier par F après une mesure sur l’échantillon dilué",
            "Mélanger les bases des pourcentages : %(m/m), %(v/v) et %(m/v) ne veulent pas dire la même chose",
            "Verser l’eau dans l’acide concentré : toujours l’acide dans l’eau"]},
        {"type": "exemples", "titre": "Exemples chiffrés", "items": [
            "<span class=\"cle\">25,0 mL × 0,100 mol/L → 250,0 mL</span> : C₂ = 0,0100 mol/L (F = 10)",
            "<span class=\"cle\">0,9 % (m/v) NaCl</span> = 9 g/L = 0,154 mol/L",
            "<span class=\"cle\">ρ(eau) = 0,9982 g/mL</span> à 20 °C (1,0000 g/mL à 4 °C)",
            "<span class=\"cle\">1 ppm</span> ≈ 1 mg/L en solution aqueuse diluée ; 1 % = 10 000 ppm",
            "<span class=\"cle\">N_A = 6,022 140 76 × 10²³ mol⁻¹</span> : 1 mol = 6,022 × 10²³ entités"]}
    ],
    [
        {"titre": "1 · Préparer une dilution à la fiole jaugée", "svg": """<svg viewBox="0 0 660 200" width="100%" role="img" aria-label="Préparation d'une dilution : pipette de solution mère vers fiole jaugée complétée au trait">
    <defs><marker id="pc2a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
    <text x="16" y="26" fill="var(--ac)" font-size="14" font-weight="bold">C₁V₁ = C₂V₂ — on ajoute du solvant, pas de soluté</text>
    <rect x="70" y="52" width="16" height="92" rx="4" fill="var(--card2)" stroke="var(--ac)"/>
    <path d="M78 144 L78 162" stroke="var(--ac)" stroke-width="3"/>
    <rect x="72" y="74" width="12" height="52" fill="var(--dim)"/>
    <text x="44" y="60" fill="var(--fg)" font-size="11">pipette jaugée</text>
    <text x="44" y="76" fill="var(--dim)" font-size="10">V₁ = C₂V₂/C₁</text>
    <line x1="90" y1="164" x2="216" y2="120" stroke="var(--ac)" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#pc2a)"/>
    <path d="M248 48 L248 84 L228 172 Q222 188 240 188 L316 188 Q334 188 328 172 L308 84 L308 48 Z" fill="var(--card2)" stroke="var(--ac)" stroke-width="2"/>
    <rect x="244" y="40" width="68" height="10" rx="3" fill="var(--dim)"/>
    <line x1="231" y1="118" x2="305" y2="118" stroke="var(--warn)" stroke-width="2"/>
    <path d="M234 150 Q278 138 322 150" fill="none" stroke="var(--ac)" stroke-width="1.5"/>
    <text x="336" y="114" fill="var(--warn)" font-size="11">trait de jauge</text>
    <text x="336" y="132" fill="var(--fg)" font-size="11">V₂ = 250,0 mL</text>
    <text x="336" y="150" fill="var(--dim)" font-size="10">bas du ménisque</text>
    <text x="336" y="168" fill="var(--dim)" font-size="10">au trait, œil à niveau</text>
    <rect x="430" y="56" width="210" height="120" rx="8" fill="var(--card2)" stroke="var(--dim)"/>
    <text x="444" y="80" fill="var(--fg)" font-size="12" font-weight="bold">Données</text>
    <text x="444" y="102" fill="var(--fg)" font-size="11">C₁ = 0,100 mol/L</text>
    <text x="444" y="122" fill="var(--fg)" font-size="11">V₁ = 25,0 mL</text>
    <text x="444" y="142" fill="var(--fg)" font-size="11">V₂ = 250,0 mL</text>
    <text x="444" y="164" fill="var(--warn)" font-size="11">C₂ = C₁·V₁/V₂ = 0,0100 mol/L</text>
   </svg>"""},
        {"titre": "2 · La dilution vue comme un partage de particules", "svg": """<svg viewBox="0 0 660 185" width="100%" role="img" aria-label="Avant et après dilution : même nombre de solutés dans un volume plus grand">
    <defs><marker id="pc2b" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
    <text x="16" y="24" fill="var(--ac)" font-size="14" font-weight="bold">Même quantité de soluté, volume multiplié par 10</text>
    <rect x="40" y="52" width="140" height="100" rx="6" fill="var(--card2)" stroke="var(--ac)" stroke-width="2"/>
    <line x1="40" y1="122" x2="180" y2="122" stroke="var(--dim)" stroke-width="1.5"/>
    <g fill="var(--warn)"><circle cx="62" cy="72" r="4"/><circle cx="92" cy="66" r="4"/><circle cx="122" cy="78" r="4"/><circle cx="152" cy="68" r="4"/><circle cx="76" cy="96" r="4"/><circle cx="106" cy="90" r="4"/><circle cx="138" cy="100" r="4"/><circle cx="164" cy="88" r="4"/></g>
    <text x="110" y="170" text-anchor="middle" fill="var(--fg)" font-size="11">Avant : C₁ = 0,100 mol/L</text>
    <text x="110" y="184" text-anchor="middle" fill="var(--dim)" font-size="10">V₁ = 25,0 mL</text>
    <line x1="190" y1="104" x2="260" y2="104" stroke="var(--ac)" stroke-width="2" marker-end="url(#pc2b)"/>
    <text x="225" y="92" text-anchor="middle" fill="var(--ac)" font-size="12">+ solvant</text>
    <rect x="270" y="46" width="220" height="112" rx="6" fill="var(--card2)" stroke="var(--ac)" stroke-width="2"/>
    <g fill="var(--warn)"><circle cx="302" cy="70" r="4"/><circle cx="350" cy="60" r="4"/><circle cx="398" cy="76" r="4"/><circle cx="456" cy="64" r="4"/><circle cx="322" cy="100" r="4"/><circle cx="372" cy="116" r="4"/><circle cx="420" cy="94" r="4"/><circle cx="470" cy="124" r="4"/></g>
    <text x="380" y="170" text-anchor="middle" fill="var(--fg)" font-size="11">Après : C₂ = 0,0100 mol/L</text>
    <text x="380" y="184" text-anchor="middle" fill="var(--dim)" font-size="10">V₂ = 250,0 mL · F = 10</text>
    <rect x="510" y="52" width="134" height="96" rx="8" fill="var(--card2)" stroke="var(--warn)"/>
    <text x="524" y="76" fill="var(--warn)" font-size="12" font-weight="bold">n conservé</text>
    <text x="524" y="98" fill="var(--fg)" font-size="11">C₁V₁ = C₂V₂</text>
    <text x="524" y="120" fill="var(--fg)" font-size="11">1,50 × 10⁻³ mol</text>
    <text x="524" y="140" fill="var(--dim)" font-size="10">des deux côtés</text>
   </svg>"""},
        {"titre": "3 · Verrerie jaugée : contenir ou délivrer", "svg": """<svg viewBox="0 0 660 190" width="100%" role="img" aria-label="Comparaison fiole jaugée, pipette volumétrique et burette avec tolérances classe A">
    <defs><marker id="pc2c" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
    <text x="16" y="24" fill="var(--ac)" font-size="14" font-weight="bold">Verrerie jaugée : la classe A garantit la tolérance</text>
    <path d="M86 46 L86 78 L66 160 Q62 176 80 176 L136 176 Q154 176 150 160 L130 78 L130 46 Z" fill="var(--card2)" stroke="var(--ac)" stroke-width="2"/>
    <rect x="82" y="38" width="52" height="10" rx="3" fill="var(--dim)"/>
    <line x1="71" y1="116" x2="145" y2="116" stroke="var(--warn)" stroke-width="2"/>
    <text x="108" y="196" text-anchor="middle" fill="var(--fg)" font-size="11">Fiole jaugée</text>
    <text x="108" y="210" text-anchor="middle" fill="var(--dim)" font-size="10">contenir · 50 mL ± 0,05 mL</text>
    <line x1="166" y1="100" x2="196" y2="100" stroke="var(--ac)" stroke-width="2" marker-end="url(#pc2c)"/>
    <rect x="222" y="40" width="18" height="130" rx="5" fill="var(--card2)" stroke="var(--ac)" stroke-width="2"/>
    <path d="M231 170 L231 182" stroke="var(--ac)" stroke-width="3"/>
    <line x1="216" y1="70" x2="246" y2="70" stroke="var(--warn)" stroke-width="2"/>
    <text x="270" y="196" text-anchor="middle" fill="var(--fg)" font-size="11">Pipette jaugée</text>
    <text x="270" y="210" text-anchor="middle" fill="var(--dim)" font-size="10">délivrer · 10 mL ± 0,02 mL</text>
    <line x1="320" y1="100" x2="350" y2="100" stroke="var(--ac)" stroke-width="2" marker-end="url(#pc2c)"/>
    <rect x="382" y="34" width="22" height="140" rx="3" fill="var(--card2)" stroke="var(--ac)" stroke-width="2"/>
    <g stroke="var(--dim)" stroke-width="1"><line x1="384" y1="60" x2="398" y2="60"/><line x1="384" y1="80" x2="398" y2="80"/><line x1="384" y1="100" x2="398" y2="100"/><line x1="384" y1="120" x2="398" y2="120"/><line x1="384" y1="140" x2="398" y2="140"/><line x1="384" y1="160" x2="398" y2="160"/></g>
    <path d="M404 152 L404 176" stroke="var(--ac)" stroke-width="2"/>
    <text x="450" y="196" text-anchor="middle" fill="var(--fg)" font-size="11">Burette</text>
    <text x="450" y="210" text-anchor="middle" fill="var(--dim)" font-size="10">délivrer · 25 mL ± 0,03 mL</text>
    <text x="500" y="70" fill="var(--warn)" font-size="11">Lire le bas du ménisque</text>
    <text x="500" y="90" fill="var(--warn)" font-size="11">à hauteur des yeux.</text>
   </svg>"""}
    ]
)


# ===========================================================================
# CHAPITRE 3 — Acides, bases et pH
# ===========================================================================
C3 = fiche(
    "Chapitre 3 · Acides, bases et pH",
    REF + " · IUPAC Gold Book (pH, P04525) et IUPAC Recommendations 2002 (measurement of pH) · Brønsted-Lowry · VIM 2.30 · LibreTexts Chemistry (acids, bases, pH, Kw)",
    [
        "Théorie de Brønsted-Lowry : un acide est un donneur de proton H⁺, une base est un accepteur de proton. Toute réaction acide-base est un transfert de proton entre un couple acide/base conjugué : AH/A⁻ ou BH⁺/B.",
        "Un acide fort se dissocie totalement dans l'eau (HCl + H₂O → H₃O⁺ + Cl⁻). Un acide faible donne un équilibre : AH + H₂O ⇌ A⁻ + H₃O⁺, de constante Ka = [A⁻][H₃O⁺]/[AH]. pKa = −log Ka ; plus Ka est grand (pKa petit), plus l'acide est fort.",
        "Autoprotolyse de l'eau : 2 H₂O ⇌ H₃O⁺ + OH⁻, avec Kw = [H₃O⁺][OH⁻] = 1,0 × 10⁻¹⁴ à 25 °C (pKw = 14). La neutralité correspond à [H₃O⁺] = [OH⁻] = 10⁻⁷ mol/L, soit pH 7 à 25 °C seulement.",
        "Définition IUPAC : pH = −log a(H₃O⁺), où a est l'activité (grandeur sans dimension). En solution diluée, on approxime a ≈ [H₃O⁺]/c°. Le pH se mesure avec une électrode de verre combinée et un pHmètre étalonné par au moins deux tampons certifiés ; la pente de Nernst vaut 59,16 mV par unité de pH à 25 °C.",
        "Échelle logarithmique : pH = −log[H₃O⁺] approché ; 1 unité de pH correspond à un facteur 10 sur la concentration en H₃O⁺. À 25 °C : pH < 7 acide, pH = 7 neutre, pH > 7 basique. Un pH n'a pas d'unité.",
        "Une base faible réagit selon B + H₂O ⇌ BH⁺ + OH⁻ avec Kb = [BH⁺][OH⁻]/[B]. Pour un couple conjugué : Ka(BH⁺) × Kb(B) = Kw, donc pKa + pKb = pKw = 14 à 25 °C.",
        "Acide polyprotonique : il possède autant de constantes que de protons échangeables. Exemples : H₃PO₄ (pKa₁ = 2,15 ; pKa₂ = 7,20 ; pKa₃ = 12,35), acide carbonique H₂CO₃ (6,35 et 10,33), acide citrique (3,13 ; 4,76 ; 6,40).",
        "Relation de Henderson-Hasselbalch : pH = pKa + log([A⁻]/[AH]). Quand [A⁻] = [AH], le logarithme est nul et pH = pKa : c'est le point de demi-équivalence d'un titrage d'acide faible par une base forte.",
        "Diagramme de prédominance du couple AH/A⁻ : un axe gradué en pH, avec AH majoritaire pour pH < pKa et A⁻ majoritaire pour pH > pKa. La frontière des deux zones est à pH = pKa ; à une unité de pH de la frontière, le rapport est 10:1 (espèce dominante ≈ 91 %).",
        "Calculs utiles : acide fort monoprotonique de concentration c → [H₃O⁺] = c et pH = −log c ; base forte → [OH⁻] = c, pOH = −log c puis pH = 14 − pOH ; acide faible peu dissocié → [H₃O⁺] ≈ √(Ka·c).",
        "Indicateur coloré : couple acide/base dont les formes ont des couleurs différentes ; son virage s'étale sur environ 2 unités de pH autour de son pKa. Méthylorange : 3,1–4,4 ; phénolphtaléine : 8,2–10,0 ; bleu de bromothymol : 6,0–7,6.",
        "Au laboratoire BIOALC : contrôle du pH des milieux de culture, tampons et eaux ; rincer l'électrode à l'eau distillée, l'essuyer sans frotter, compenser la température, étalonner quotidiennement et ne jamais laisser l'électrode sécher.",
    ],
    [
        qcm("Selon Brønsted-Lowry, un acide est :",
            ["Un donneur de proton H⁺", "Un accepteur de proton H⁺", "Un donneur d'électron", "Une espèce qui libère toujours OH⁻"], 0,
            "Acide = donneur de proton, base = accepteur de proton. La réaction est un transfert de H⁺ entre les deux couples conjugués."),
        qcm("À 25 °C, Kw = 1,0 × 10⁻¹⁴. Quel est le pH d'une solution de HCl à 0,010 mol/L ?",
            ["1,00", "2,00", "12,00", "0,010"], 1,
            "HCl est un acide fort : [H₃O⁺] = c = 1,0 × 10⁻² mol/L, donc pH = −log(10⁻²) = 2,00."),
        qcm("Quelle est la définition officielle (IUPAC) du pH ?",
            ["pH = −log[H₃O⁺] exactement", "pH = −log a(H₃O⁺), l'activité", "pH = log[H₃O⁺]", "pH = 14 − pOH en toute circonstance"], 1,
            "Le pH est défini par l'activité de l'ion hydrogène. En solution diluée, on approxime par −log[H₃O⁺] ; la mesure par électrode de verre répond à l'activité."),
        qcm("Pour un acide faible de pKa = 4,76, que vaut [A⁻]/[AH] à pH = 4,76 ?",
            ["0,1", "1", "10", "100"], 1,
            "Henderson-Hasselbalch : pH = pKa + log([A⁻]/[AH]) → log = 0 → [A⁻]/[AH] = 1. C'est aussi le point de demi-équivalence."),
        qcm("Sur un diagramme de prédominance du couple AH/A⁻, la frontière entre les deux formes se situe à :",
            ["pH = 0", "pH = 7", "pH = pKa", "pH = 14"], 2,
            "À pH = pKa, [AH] = [A⁻] : chacune représente 50 % de l'espèce totale. En dessous, AH domine ; au-dessus, A⁻ domine."),
        qcm("Quelle est la pente théorique d'une électrode de verre à 25 °C (loi de Nernst) ?",
            ["≈ 29,6 mV/pH", "≈ 59,2 mV/pH", "≈ 118 mV/pH", "≈ 1 V/pH"], 1,
            "RT/F · ln10 = 59,16 mV à 298,15 K pour un échange d'un proton. Le constructeur vérifie cette pente lors de la calibration à deux tampons."),
        qt("Calculer le pH d'une solution de NaOH à 1,0 × 10⁻³ mol/L à 25 °C.",
           "Base forte : [OH⁻] = 1,0 × 10⁻³ mol/L, pOH = 3,00, donc pH = pKw − pOH = 14,00 − 3,00 = 11,00.",
           "Pour une base forte monoprotonique, [OH⁻] = c. On utilise pKw = 14,00 à 25 °C ; à une autre température, pKw change."),
        qt("Pourquoi la neutralité correspond-elle à pH 7 à 25 °C mais pas à 37 °C ?",
           "Parce que Kw dépend de la température : à 37 °C, Kw ≈ 2,4 × 10⁻¹⁴ (pKw ≈ 13,6), donc [H₃O⁺] neutre = √Kw ≈ 1,55 × 10⁻⁷ et pH neutre ≈ 6,8. La neutralité reste [H₃O⁺] = [OH⁻], pas pH = 7.",
           "pH + pOH = pKw ; seul le produit Kw = [H₃O⁺][OH⁻] définit la neutralité, et pKw varie avec T."),
    ],
    [
        {"type": "intro", "titre": "L’idée en une phrase",
         "texte": "Un acide donne un proton, une base en accepte un. Le pH mesure l’activité de H₃O⁺ ; le pKa dit à quel pH une espèce change de forme."},
        {"type": "formule", "titre": "Les relations du chapitre",
         "eq": "pH = −log a(H₃O⁺) ≈ −log[H₃O⁺]     ·     pH + pOH = pKw = 14 (25 °C)",
         "leg": "Ka = [A⁻][H₃O⁺]/[AH] · pKa = −log Ka · Kw = [H₃O⁺][OH⁻] = 1,0 × 10⁻¹⁴ à 25 °C"},
        {"type": "grille", "titre": "Le couple acide-base conjugué", "items": [
            ["AH", "Acide : donneur de proton, présent en dessous de son pKa", "pKa = −log Ka"],
            ["A⁻", "Base conjuguée : accepteur de proton, dominante au-dessus du pKa", "pKb = pKw − pKa"],
            ["H₂O", "Amphotère : donneur ou accepteur selon le partenaire", "autoprotolyse : Kw"]]},
        {"type": "liste", "titre": "Force des acides et des bases", "items": [
            "Acide fort : dissociation totale (HCl, HNO₃, H₂SO₄ pour la 1ʳᵉ dissociation) → [H₃O⁺] = c",
            "Acide faible : équilibre AH + H₂O ⇌ A⁻ + H₃O⁺ → [H₃O⁺] ≈ √(Ka·c) si dissociation faible",
            "Base forte : dissociation totale (NaOH, KOH) → [OH⁻] = c",
            "Polyacide : plusieurs pKa, un par proton échangeable (H₃PO₄ : 2,15 / 7,20 / 12,35)"]},
        {"type": "etapes", "titre": "Mesurer le pH au pHmètre, pas à pas", "items": [
            "Vérifier la date des tampons et la propreté de l’électrode combinée",
            "Rincer à l’eau distillée et essuyer sans frotter la membrane de verre",
            "Étalonner avec deux tampons certifiés encadrant le pH attendu (ex. 4,01 et 7,00)",
            "Rincer, plonger la sonde, attendre la stabilisation (température compensée)",
            "Lire le pH, rincer à nouveau et conserver l’électrode dans sa solution de stockage"]},
        {"type": "attention", "titre": "⚠️ Pièges à éviter", "items": [
            "pH = 7 n’est neutre qu’à 25 °C : ailleurs, la neutralité est [H₃O⁺] = [OH⁻]",
            "Un pH n’a pas d’unité ; le nombre de décimales dépend des chiffres significatifs de [H₃O⁺]",
            "Une électrode sèche ou non calibrée donne un résultat systématiquement faux",
            "Ne pas confondre pKa (constante de l’espèce) et pH (propriété de la solution)",
            "Un acide faible n’est pas « moins dangereux » : la concentration compte aussi"]},
        {"type": "exemples", "titre": "Exemples chiffrés et repères", "items": [
            "<span class=\"cle\">HCl 0,010 M</span> → pH 2,00 ; <span class=\"cle\">NaOH 0,0010 M</span> → pH 11,00",
            "<span class=\"cle\">Kw = 1,0 × 10⁻¹⁴</span> → pKw = 14 à 25 °C",
            "<span class=\"cle\">H₃PO₄</span> : pKa₁ 2,15 · pKa₂ 7,20 · pKa₃ 12,35",
            "<span class=\"cle\">pH = pKa ± 1</span> → rapport [A⁻]/[AH] = 0,1 ou 10 (91 % de la forme dominante)",
            "<span class=\"cle\">Indicateurs</span> : méthylorange 3,1–4,4 · bromothymol 6,0–7,6 · phénolphtaléine 8,2–10,0"]}
    ],
    [
        {"titre": "1 · Transfert de proton et couple conjugué", "svg": """<svg viewBox="0 0 660 160" width="100%" role="img" aria-label="Transfert de proton entre un acide AH et une base H2O, formant A- et H3O+">
    <defs><marker id="pc3a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
    <text x="16" y="24" fill="var(--ac)" font-size="14" font-weight="bold">Réaction acide-base = transfert de H⁺</text>
    <rect x="36" y="54" width="140" height="52" rx="8" fill="var(--card2)" stroke="var(--ac)"/>
    <text x="106" y="76" text-anchor="middle" fill="var(--fg)" font-size="16">AH</text>
    <text x="106" y="94" text-anchor="middle" fill="var(--dim)" font-size="11">acide (donneur)</text>
    <text x="188" y="86" fill="var(--fg)" font-size="15">+</text>
    <rect x="204" y="54" width="140" height="52" rx="8" fill="var(--card2)" stroke="var(--dim)"/>
    <text x="274" y="76" text-anchor="middle" fill="var(--fg)" font-size="16">H₂O</text>
    <text x="274" y="94" text-anchor="middle" fill="var(--dim)" font-size="11">base (accepteur)</text>
    <line x1="356" y1="80" x2="406" y2="80" stroke="var(--ac)" stroke-width="2.5" marker-end="url(#pc3a)"/>
    <line x1="406" y1="88" x2="356" y2="88" stroke="var(--ac)" stroke-width="2.5" marker-end="url(#pc3a)"/>
    <text x="381" y="70" text-anchor="middle" fill="var(--ac)" font-size="11">H⁺</text>
    <rect x="418" y="54" width="140" height="52" rx="8" fill="var(--card2)" stroke="var(--warn)"/>
    <text x="488" y="76" text-anchor="middle" fill="var(--fg)" font-size="16">A⁻</text>
    <text x="488" y="94" text-anchor="middle" fill="var(--warn)" font-size="11">base conjuguée</text>
    <text x="570" y="86" fill="var(--fg)" font-size="15">+</text>
    <rect x="586" y="54" width="60" height="52" rx="8" fill="var(--card2)" stroke="var(--ac)"/>
    <text x="616" y="76" text-anchor="middle" fill="var(--fg)" font-size="14">H₃O⁺</text>
    <text x="616" y="94" text-anchor="middle" fill="var(--dim)" font-size="10">pH</text>
    <line x1="36" y1="126" x2="646" y2="126" stroke="var(--warn)" stroke-width="1" stroke-dasharray="5 4"/>
    <text x="36" y="146" fill="var(--dim)" font-size="11">Ka = [A⁻][H₃O⁺]/[AH] · pKa = −log Ka · à pH = pKa, [AH] = [A⁻]</text>
   </svg>"""},
        {"titre": "2 · Diagramme de prédominance du couple AH/A⁻", "svg": """<svg viewBox="0 0 660 185" width="100%" role="img" aria-label="Diagramme de prédominance : AH avant le pKa, A- après le pKa">
    <defs><marker id="pc3b" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
    <text x="16" y="24" fill="var(--ac)" font-size="14" font-weight="bold">Diagramme de prédominance (ex. acide acétique, pKa = 4,76)</text>
    <line x1="60" y1="120" x2="620" y2="120" stroke="var(--dim)" stroke-width="2" marker-end="url(#pc3b)"/>
    <g fill="var(--dim)" font-size="11" text-anchor="middle">
      <text x="60" y="140">0</text><text x="200" y="140">3</text><text x="330" y="140">5</text><text x="460" y="140">9</text><text x="610" y="140">14</text>
    </g>
    <text x="626" y="124" fill="var(--fg)" font-size="11">pH</text>
    <rect x="60" y="56" width="270" height="48" rx="4" fill="var(--card2)" stroke="var(--ac)"/>
    <text x="195" y="86" text-anchor="middle" fill="var(--fg)" font-size="14">AH majoritaire</text>
    <rect x="330" y="56" width="290" height="48" rx="4" fill="var(--card2)" stroke="var(--warn)"/>
    <text x="475" y="86" text-anchor="middle" fill="var(--fg)" font-size="14">A⁻ majoritaire</text>
    <line x1="330" y1="44" x2="330" y2="128" stroke="var(--warn)" stroke-width="2" stroke-dasharray="5 4"/>
    <text x="340" y="40" fill="var(--warn)" font-size="12">pH = pKa = 4,76</text>
    <text x="195" y="166" text-anchor="middle" fill="var(--dim)" font-size="11">pH &lt; pKa → [AH] &gt; [A⁻]</text>
    <text x="475" y="166" text-anchor="middle" fill="var(--dim)" font-size="11">pH &gt; pKa → [A⁻] &gt; [AH]</text>
    <text x="60" y="182" fill="var(--warn)" font-size="11">À ± 1 unité du pKa : rapport 10:1, espèce dominante ≈ 91 %.</text>
   </svg>"""},
        {"titre": "3 · Échelle des pH et chaîne de mesure", "svg": """<svg viewBox="0 0 660 175" width="100%" role="img" aria-label="Échelle de pH de 0 à 14 et mesure par électrode de verre étalonnée">
    <defs><marker id="pc3c" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
    <text x="16" y="24" fill="var(--ac)" font-size="14" font-weight="bold">Échelle des pH (25 °C) et mesure au pHmètre</text>
    <rect x="30" y="48" width="100" height="34" fill="var(--warn)"/><rect x="130" y="48" width="100" height="34" fill="var(--dim)"/><rect x="230" y="48" width="100" height="34" fill="var(--ac)"/><rect x="330" y="48" width="100" height="34" fill="var(--fg)"/><rect x="430" y="48" width="100" height="34" fill="var(--ac)"/><rect x="530" y="48" width="100" height="34" fill="var(--dim)"/>
    <g fill="var(--card2)" font-size="11" text-anchor="middle"><text x="40" y="70">acide</text><text x="232" y="70">6</text><text x="334" y="70">7 neutre</text><text x="530" y="70">basique</text></g>
    <g fill="var(--fg)" font-size="10" text-anchor="middle"><text x="30" y="96">0</text><text x="230" y="96">5</text><text x="380" y="96">8</text><text x="530" y="96">12</text><text x="630" y="96">14</text></g>
    <line x1="380" y1="40" x2="380" y2="104" stroke="var(--warn)" stroke-width="2" stroke-dasharray="4 3"/>
    <rect x="30" y="116" width="220" height="50" rx="8" fill="var(--card2)" stroke="var(--ac)"/>
    <text x="44" y="136" fill="var(--fg)" font-size="11">Électrode de verre + référence</text>
    <text x="44" y="154" fill="var(--dim)" font-size="10">pente : 59,16 mV/pH à 25 °C</text>
    <line x1="254" y1="141" x2="296" y2="141" stroke="var(--ac)" stroke-width="2" marker-end="url(#pc3c)"/>
    <rect x="300" y="116" width="150" height="50" rx="8" fill="var(--card2)" stroke="var(--ac)"/>
    <text x="314" y="136" fill="var(--fg)" font-size="11">Étalonnage 2 tampons</text>
    <text x="314" y="154" fill="var(--dim)" font-size="10">ex. 4,01 et 7,00</text>
    <line x1="454" y1="141" x2="496" y2="141" stroke="var(--ac)" stroke-width="2" marker-end="url(#pc3c)"/>
    <rect x="500" y="116" width="140" height="50" rx="8" fill="var(--card2)" stroke="var(--warn)"/>
    <text x="514" y="136" fill="var(--fg)" font-size="11">Lecture du pH</text>
    <text x="514" y="154" fill="var(--dim)" font-size="10">sans unité, après stabilisation</text>
   </svg>"""}
    ]
)


# ===========================================================================
# CHAPITRE 4 — Tampons et ampholytes
# ===========================================================================
C4 = fiche(
    "Chapitre 4 · Tampons et ampholytes",
    REF + " · IUPAC Gold Book (buffer solution, isoelectric point) · LibreTexts Biochemistry 26.2 (Henderson-Hasselbalch et pI) · Good's buffers (HEPES, Tris) · IUPAC pH standards",
    [
        "Une solution tampon est un mélange d'un acide faible AH et de sa base conjuguée A⁻ (ou d'une base faible et de son acide conjugué). Elle s'oppose à une variation de pH lors de petits ajouts d'acide/base ou d'une dilution modérée, sans être épuisée.",
        "Équation de Henderson-Hasselbalch : pH = pKa + log([A⁻]/[AH]) = pKa + log(n(A⁻)/n(AH)) si les deux espèces sont dans le même volume. Exemples : acide acétique/acétate (pKa 4,76), H₂PO₄⁻/HPO₄²⁻ (pKa₂ 7,20), Tris/Tris-H⁺ (pKa 8,06 à 25 °C).",
        "Le pH d'un tampon dépend du RAPPORT [A⁻]/[AH] et non de la concentration totale : diluer un tampon ne change pas son pH idéal, mais diminue son pouvoir tampon.",
        "Zone de fonctionnement : tampon efficace pour pH ≈ pKa ± 1, c'est-à-dire lorsque le rapport [A⁻]/[AH] reste entre 0,1 et 10. Le pouvoir tampon est maximal à pH = pKa, où [AH] = [A⁻].",
        "Mécanisme : un ajout de H₃O⁺ est consommé par la base A⁻ (A⁻ + H₃O⁺ → AH + H₂O) ; un ajout de OH⁻ est consommé par l'acide AH (AH + OH⁻ → A⁻ + H₂O). Le tampon cesse de fonctionner si l'une des deux formes est épuisée.",
        "Pouvoir tampon β = dn(base forte)/d(pH) (mol·L⁻¹ par unité de pH). Pour un acide faible monoacide de concentration totale C, β = 2,303·C·Ka·[H₃O⁺]/(Ka + [H₃O⁺])² ; β_max = 2,303·C/4 ≈ 0,576·C à pH = pKa (25 °C). Plus C est grande, plus le tampon est résistant.",
        "Polyacide : chaque pKa définit une zone tampon possible. Pour l'acide phosphorique (pKa 2,15 / 7,20 / 12,35), le couple H₂PO₄⁻/HPO₄²⁻ donne le tampon phosphate utilisé en biologie autour de pH 7,2.",
        "Ampholyte (amphotère) : espèce capable de se comporter comme acide ou comme base selon le milieu. Exemples : H₂PO₄⁻, HCO₃⁻, H₂O, les acides aminés et les protéines. H₂PO₄⁻ peut donner un proton (→ HPO₄²⁻) ou en accepter un (→ H₃PO₄).",
        "Acide aminé : en solution il existe sous forme de zwitterion (⁺H₃N–CHR–COO⁻). En milieu acide, il est cationique (⁺H₃N–CHR–COOH) ; en milieu basique, anionique (H₂N–CHR–COO⁻). Le point isoélectrique pI est le pH où sa charge nette est nulle et où il ne migre pas en électrophorèse.",
        "Pour un acide aminé sans groupement ionisable sur sa chaîne latérale, pI = (pKa₁ + pKa₂)/2. Alanine : pKa₁ = 2,34 (COOH), pKa₂ = 9,69 (NH₃⁺), donc pI ≈ 6,02. Acide aspartique : pI ≈ 3,0 ; lysine : pI ≈ 9,7 (on moyenne les deux pKa qui encadrent le zwitterion).",
        "Préparer un tampon : choisir un pKa proche du pH visé, calculer le rapport [A⁻]/[AH] = 10^(pH − pKa), dissoudre les quantités calculées, ajuster finement au pHmètre avec acide/base dilués, compléter au volume et revérifier. Les pKa dépendent de la température (Tris : ≈ −0,028 unité par °C) et de la force ionique.",
        "Tampons courants : acétate 4,76 ; citrate (pKa₃ 6,40) ; phosphate 7,20 ; HEPES 7,55 à 25 °C ; Tris 8,06 à 25 °C. Tampons d'étalonnage du pHmètre : 4,01 / 6,86 / 7,00 / 9,18 / 10,00. Un tampon périmé, contaminé ou dilué excessivement perd son pouvoir tampon.",
    ],
    [
        qcm("Un acide et sa base conjuguée sont équimolaires. Le pH de la solution vaut :",
            ["pKa − 1", "pKa", "pKa + 1", "7"], 1,
            "Henderson-Hasselbalch : log([A⁻]/[AH]) = log 1 = 0, donc pH = pKa. C'est le pouvoir tampon maximal."),
        qcm("Dans quelle zone un tampon est-il efficace ?",
            ["pH = pKa ± 5", "pH = pKa ± 1", "pH = 7 quoi qu'il arrive", "Uniquement à pH < 2"], 1,
            "Le rapport [A⁻]/[AH] doit rester entre 0,1 et 10, soit pH entre pKa − 1 et pKa + 1. Au-delà, une des formes est épuisée."),
        qcm("On dilue 10 fois un tampon phosphate. Que se passe-t-il (idéalement) ?",
            ["Le pH augmente d'une unité", "Le pH diminue d'une unité", "Le pH ne change pas mais le pouvoir tampon baisse", "Le tampon devient acide"], 2,
            "Le rapport [A⁻]/[AH] est inchangé donc le pH reste le même ; la concentration totale C diminue donc β ≈ 0,576 C diminue aussi."),
        qcm("Quel est le pI de l'alanine (pKa₁ = 2,34 ; pKa₂ = 9,69) ?",
            ["2,34", "6,02", "7,00", "9,69"], 1,
            "Pour un acide aminé sans ionisation latérale, pI = (pKa₁ + pKa₂)/2 = (2,34 + 9,69)/2 = 6,015 ≈ 6,02."),
        qcm("L'ion H₂PO₄⁻ est un ampholyte parce qu'il peut :",
            ["Seulement donner un proton", "Seulement accepter un proton", "Donner ou accepter un proton selon le milieu", "Échanger deux électrons"], 2,
            "H₂PO₄⁻ → HPO₄²⁻ + H⁺ (comportement acide) et H₂PO₄⁻ + H⁺ → H₃PO₄ (comportement base) : c'est un ampholyte."),
        qcm("Quel tampon choisir pour travailler à pH 7,4 en biologie ?",
            ["Acétate (pKa 4,76)", "Phosphate (pKa 7,20)", "Tris (pKa 8,06)", "Citrate (pKa 6,40)"], 1,
            "On choisit le pKa le plus proche du pH visé : le phosphate (7,20) est dans la zone pKa ± 1, comme HEPES (7,55)."),
        qt("Un tampon acide acétique/acétate a pKa = 4,76. Quel rapport [A⁻]/[AH] faut-il pour pH = 5,20 ?",
           "[A⁻]/[AH] = 10^(pH − pKa) = 10^(5,20 − 4,76) = 10^0,44 ≈ 2,75. Il faut environ 2,75 moles d'acétate pour 1 mole d'acide acétique.",
           "Le rapport reste dans la zone 0,1–10 : le tampon est efficace. On peut aussi raisonner en nombres de moles si les espèces sont dans le même volume."),
        qt("Expliquer pourquoi un tampon résiste à l'ajout de quelques gouttes d'acide ou de base.",
           "La base conjuguée A⁻ consomme les H₃O⁺ ajoutés (A⁻ + H₃O⁺ → AH + H₂O) et l'acide AH consomme les OH⁻ ajoutés (AH + OH⁻ → A⁻ + H₂O). Tant que ni AH ni A⁻ n'est épuisé, le rapport [A⁻]/[AH] — donc le pH — ne varie que peu.",
           "Le pouvoir tampon β quantifie cette résistance ; il est maximal lorsque [AH] = [A⁻] = C/2, soit à pH = pKa."),
    ],
    [
        {"type": "intro", "titre": "L’idée en une phrase",
         "texte": "Un tampon contient les deux formes d’un couple acide-base faible : l’une absorbe l’acide ajouté, l’autre absorbe la base ajoutée."},
        {"type": "formule", "titre": "Henderson-Hasselbalch et pouvoir tampon",
         "eq": "pH = pKa + log([A⁻]/[AH])      β_max ≈ 0,576 · C (à pH = pKa)",
         "leg": "Zone efficace : pKa − 1 ≤ pH ≤ pKa + 1 · β en mol·L⁻¹ par unité de pH · C = [AH] + [A⁻]"},
        {"type": "grille", "titre": "Les 3 grandeurs du tampon", "items": [
            ["pKa", "Constante du couple : fixe le centre de la zone tampon", "sans unité"],
            ["[A⁻]/[AH]", "Rapport des formes : fixe le pH du tampon", "sans unité"],
            ["β", "Pouvoir tampon : quantité d’acide/base pour changer le pH d’une unité", "mol·L⁻¹·pH⁻¹"]]},
        {"type": "liste", "titre": "Tampons et ampholytes du laboratoire", "items": [
            "Acétate : pKa 4,76 · citrate : pKa₃ 6,40 · phosphate : pKa₂ 7,20",
            "HEPES : pKa 7,55 à 25 °C · Tris : pKa 8,06 à 25 °C (très sensible à la température)",
            "Ampholytes : H₂PO₄⁻, HCO₃⁻, acides aminés, protéines, eau",
            "Point isoélectrique : pI = (pKa₁ + pKa₂)/2 pour un acide aminé sans chaîne ionisable"]},
        {"type": "etapes", "titre": "Préparer un tampon, pas à pas", "items": [
            "Choisir un couple dont le pKa est proche du pH visé (|pH − pKa| ≤ 1)",
            "Calculer le rapport [A⁻]/[AH] = 10^(pH − pKa) et les masses à dissoudre",
            "Dissoudre dans environ 80 % du volume final, ajuster au pHmètre",
            "Compléter au trait avec de l’eau, homogénéiser et revérifier le pH",
            "Étiqueter (nom, pH, concentration, date) et tenir compte de la température"]},
        {"type": "attention", "titre": "⚠️ Pièges à éviter", "items": [
            "Choisir un tampon dont le pKa est trop éloigné du pH visé : le pouvoir tampon s’effondre",
            "Confondir dilution et changement de pH : la dilution garde le pH mais réduit β",
            "Dépasser la capacité du tampon en ajoutant trop d’acide ou de base",
            "Oublier que le pKa varie avec la température (Tris : −0,028/°C) et la force ionique",
            "Utiliser un tampon périmé ou contaminé : les tampons d’étalonnage doivent être certifiés"]},
        {"type": "exemples", "titre": "Exemples chiffrés", "items": [
            "<span class=\"cle\">pH = pKa = 4,76</span> pour l’acide acétique/acétate équimolaire",
            "<span class=\"cle\">pH 5,20</span> avec pKa 4,76 → [A⁻]/[AH] = 10^0,44 ≈ 2,75",
            "<span class=\"cle\">β_max ≈ 0,576 C</span> : C = 0,1 mol/L → β_max ≈ 0,058 mol/L/pH",
            "<span class=\"cle\">Alanine</span> : pI = (2,34 + 9,69)/2 ≈ 6,02",
            "<span class=\"cle\">Aspartique</span> : pI ≈ 3,0 · <span class=\"cle\">Lysine</span> : pI ≈ 9,7"]}
    ],
    [
        {"titre": "1 · Comment un tampon consomme acide et base", "svg": """<svg viewBox="0 0 660 175" width="100%" role="img" aria-label="Mécanisme tampon : A- consomme H3O+ et AH consomme OH-">
    <defs><marker id="pc4a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
    <text x="16" y="24" fill="var(--ac)" font-size="14" font-weight="bold">Le couple AH/A⁻ joue le rôle d’éponge à protons</text>
    <rect x="222" y="58" width="216" height="66" rx="10" fill="var(--card2)" stroke="var(--ac)" stroke-width="2"/>
    <text x="330" y="84" text-anchor="middle" fill="var(--fg)" font-size="15">AH  /  A⁻</text>
    <text x="330" y="106" text-anchor="middle" fill="var(--dim)" font-size="11">solution tampon · pH = pKa + log([A⁻]/[AH])</text>
    <rect x="16" y="58" width="150" height="66" rx="8" fill="var(--card2)" stroke="var(--warn)"/>
    <text x="91" y="82" text-anchor="middle" fill="var(--warn)" font-size="12">+ H₃O⁺ ajouté</text>
    <text x="91" y="104" text-anchor="middle" fill="var(--fg)" font-size="11">A⁻ + H₃O⁺ → AH</text>
    <line x1="170" y1="92" x2="216" y2="92" stroke="var(--warn)" stroke-width="2" marker-end="url(#pc4a)"/>
    <rect x="494" y="58" width="150" height="66" rx="8" fill="var(--card2)" stroke="var(--ac)"/>
    <text x="569" y="82" text-anchor="middle" fill="var(--ac)" font-size="12">+ OH⁻ ajouté</text>
    <text x="569" y="104" text-anchor="middle" fill="var(--fg)" font-size="11">AH + OH⁻ → A⁻</text>
    <line x1="444" y1="92" x2="488" y2="92" stroke="var(--ac)" stroke-width="2" marker-end="url(#pc4a)"/>
    <line x1="16" y1="144" x2="644" y2="144" stroke="var(--dim)" stroke-width="1" stroke-dasharray="5 4"/>
    <text x="16" y="164" fill="var(--fg)" font-size="11">Tant que AH et A⁻ sont présents, le rapport varie peu : le pH reste quasi constant.</text>
   </svg>"""},
        {"titre": "2 · Zone de fonctionnement et pouvoir tampon", "svg": """<svg viewBox="0 0 660 190" width="100%" role="img" aria-label="Zone tampon pKa plus ou moins un et courbe de pouvoir tampon maximale en pKa">
    <defs><marker id="pc4b" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
    <text x="16" y="24" fill="var(--ac)" font-size="14" font-weight="bold">Zone efficace : pKa ± 1 · pouvoir tampon maximal à pH = pKa</text>
    <line x1="60" y1="150" x2="630" y2="150" stroke="var(--dim)" stroke-width="2" marker-end="url(#pc4b)"/>
    <line x1="60" y1="150" x2="60" y2="44" stroke="var(--dim)" stroke-width="2" marker-end="url(#pc4b)"/>
    <text x="612" y="168" fill="var(--fg)" font-size="11">pH</text><text x="36" y="48" fill="var(--fg)" font-size="11">β</text>
    <path d="M62 148 C140 146 210 132 270 88 C300 65 325 56 345 56 C365 56 390 65 420 88 C480 132 550 146 628 148" fill="none" stroke="var(--ac)" stroke-width="3"/>
    <rect x="230" y="46" width="230" height="100" rx="6" fill="var(--card2)" stroke="var(--warn)" stroke-dasharray="5 4" opacity="0.35"/>
    <line x1="345" y1="44" x2="345" y2="150" stroke="var(--warn)" stroke-width="2" stroke-dasharray="5 4"/>
    <text x="352" y="40" fill="var(--warn)" font-size="11">pKa</text>
    <text x="252" y="170" fill="var(--dim)" font-size="10">pKa − 1</text>
    <text x="424" y="170" fill="var(--dim)" font-size="10">pKa + 1</text>
    <text x="352" y="74" fill="var(--warn)" font-size="11">βmax ≈ 0,576 C</text>
    <text x="60" y="188" fill="var(--dim)" font-size="11">[A⁻]/[AH] = 0,1 à gauche · = 1 au sommet · = 10 à droite</text>
   </svg>"""},
        {"titre": "3 · Ampholyte, zwitterion et point isoélectrique", "svg": """<svg viewBox="0 0 660 180" width="100%" role="img" aria-label="Acide aminé : cation en milieu acide, zwitterion au point isoélectrique, anion en milieu basique">
    <defs><marker id="pc4c" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
    <text x="16" y="24" fill="var(--ac)" font-size="14" font-weight="bold">Ampholyte : la charge dépend du pH (ex. alanine)</text>
    <rect x="16" y="48" width="176" height="82" rx="8" fill="var(--card2)" stroke="var(--warn)"/>
    <text x="104" y="74" text-anchor="middle" fill="var(--warn)" font-size="12">pH &lt; pI</text>
    <text x="104" y="98" text-anchor="middle" fill="var(--fg)" font-size="11">⁺H₃N–CHR–COOH</text>
    <text x="104" y="118" text-anchor="middle" fill="var(--fg)" font-size="12">charge +1 (cation)</text>
    <line x1="196" y1="90" x2="238" y2="90" stroke="var(--ac)" stroke-width="2" marker-end="url(#pc4c)"/>
    <rect x="242" y="48" width="176" height="82" rx="8" fill="var(--card2)" stroke="var(--ac)"/>
    <text x="330" y="74" text-anchor="middle" fill="var(--ac)" font-size="12">pH = pI</text>
    <text x="330" y="98" text-anchor="middle" fill="var(--fg)" font-size="11">⁺H₃N–CHR–COO⁻</text>
    <text x="330" y="118" text-anchor="middle" fill="var(--fg)" font-size="12">zwitterion · charge 0</text>
    <line x1="422" y1="90" x2="464" y2="90" stroke="var(--ac)" stroke-width="2" marker-end="url(#pc4c)"/>
    <rect x="468" y="48" width="176" height="82" rx="8" fill="var(--card2)" stroke="var(--dim)"/>
    <text x="556" y="74" text-anchor="middle" fill="var(--dim)" font-size="12">pH &gt; pI</text>
    <text x="556" y="98" text-anchor="middle" fill="var(--fg)" font-size="11">H₂N–CHR–COO⁻</text>
    <text x="556" y="118" text-anchor="middle" fill="var(--fg)" font-size="12">charge −1 (anion)</text>
    <line x1="16" y1="148" x2="644" y2="148" stroke="var(--warn)" stroke-width="1" stroke-dasharray="5 4"/>
    <text x="16" y="168" fill="var(--fg)" font-size="12">pI = (pKa₁ + pKa₂)/2 = (2,34 + 9,69)/2 ≈ 6,02</text>
   </svg>"""}
    ]
)


# ===========================================================================
# CHAPITRE 5 — Oxydoréduction
# ===========================================================================
C5 = fiche(
    "Chapitre 5 · Oxydoréduction",
    REF + " · IUPAC Gold Book (oxidoreduction, standard electrode potential) · Stockholm/IUPAC sign convention (E = E° − (RT/nF)lnQ) · LibreTexts Analytical Chemistry (Nernst, redox titrations) · Hann (E° values)",
    [
        "Une oxydation est une perte d'électrons, une réduction est un gain d'électrons. Un couple redox Ox/Red réunit les deux formes d'une même espèce liées par une demi-réaction écrite conventionnellement en réduction : Ox + n e⁻ ⇌ Red. L'oxydant accepte les électrons, le réducteur les cède.",
        "La réaction bilan s'obtient en combinant deux demi-réactions après avoir égalisé le nombre d'électrons : ceux-ci disparaissent de l'équation finale. Exemple : 5 Fe²⁺ + MnO₄⁻ + 8 H⁺ → 5 Fe³⁺ + Mn²⁺ + 4 H₂O (1 mol de MnO₄⁻ consomme 5 mol de Fe²⁺).",
        "Le potentiel d'oxydoréduction E (en volts) se mesure entre une électrode indicatrice inerte (platine ou graphite) et une électrode de référence (Ag/AgCl, calomel). E° est le potentiel standard, référence E°(H⁺/H₂) = 0 V par convention (électrode à hydrogène normale). Plus E° est élevé, plus le couple est oxydant.",
        "Équation de Nernst (générale) : E = E° − (RT/nF) ln Q, avec R = 8,314 J·mol⁻¹·K⁻¹, T en kelvin, F = 96 485 C·mol⁻¹ et Q le quotient réactionnel. Pour Ox + n e⁻ ⇌ Red avec des coefficients égaux à 1 : E = E° + (0,05916/n) log([Ox]/[Red]) à 25 °C.",
        "Le facteur 0,05916 V = (RT/F)·ln 10 à 298,15 K ; il se divise par n, nombre d'électrons échangés. Si des H⁺ ou OH⁻ participent à la demi-réaction, E dépend du pH : pour MnO₄⁻/Mn²⁺ (8 H⁺ pour 5 e⁻), la pente est −(8/5) × 0,05916 ≈ −0,095 V par unité de pH.",
        "Thermodynamique : ΔrG° = −n·F·E°(cellule) et E°(cellule) = (0,05916/n) log K à 25 °C. Une réaction redox est spontanée si E°(cellule) > 0, c'est-à-dire si l'oxydant du couple à E° élevé réagit avec le réducteur du couple à E° faible.",
        "Titrage redox : on suit E = f(V du titrant) avec un potentiomètre ; la courbe est sigmoïde et présente un saut de potentiel au point d'équivalence. Pour un titrage simple, E(équivalence) = (n₁E°₁ + n₂E°₂)/(n₁ + n₂).",
        "Détection de l'équivalence : indicateur redox dont la couleur dépend du potentiel (ferroïne, E° ≈ 1,06 V), ou réaction colorée spécifique (amidon + I₂ → complexe bleu). L'équilibre des électrons à l'équivalence donne : n(e⁻ cédés) = n(e⁻ acceptés).",
        "Titrages classiques en BIOALC : permanganatométrie (KMnO₄, E° ≈ 1,51 V, auto-indicateur rose, en milieu H₂SO₄), dichromatométrie (K₂Cr₂O₇, E° ≈ 1,33 V, indicateur ferroïne, dosage de la DCO), iodimétrie/iodométrie (I₂ + 2 S₂O₃²⁻ → 2 I⁻ + S₄O₆²⁻, amidon).",
        "Le potentiel mesuré dépend des concentrations (loi de Nernst), du pH, de la température, de la force ionique (activités) et de la complexation : la complexation du Fe³⁺ par les phosphates diminue le rapport [Fe³⁺]/[Fe²⁺] donc le potentiel apparent du couple.",
        "La chaîne de mesure potentiométrique associe électrode indicatrice, électrode de référence et voltmètre à haute impédance ; E(mesuré) = E(couple) + E(référence) + potentiel de jonction. Le même principe régit la mesure du pH par électrode de verre.",
        "Bonnes pratiques : titrer le KMnO₄ fraîchement (solution non stable), éviter l'acide chlorhydrique avec le permanganate (oxydation des Cl⁻), travailler en milieu sulfurique, lire la burette à hauteur des yeux et attendre la stabilisation du potentiel avant chaque lecture.",
    ],
    [
        qcm("Dans la demi-réaction Ox + n e⁻ ⇌ Red, que représente n ?",
            ["Le nombre de protons échangés", "Le nombre d'électrons échangés", "La charge de l'oxydant", "Le nombre de moles d'oxydant"], 1,
            "n est le nombre d'électrons transférés dans la demi-réaction écrite en réduction ; il apparaît au dénominateur du terme de Nernst."),
        qcm("À 25 °C, quelle est l'équation de Nernst pour Ox + 2 e⁻ ⇌ Red (coefficients 1) ?",
            ["E = E° + 0,05916 log([Ox]/[Red])", "E = E° + (0,05916/2) log([Ox]/[Red])", "E = E° − 0,05916 log([Red])", "E = E° + 0,05916 × 2 log([Ox]/[Red])"], 1,
            "Le terme (RT/nF)ln10 vaut 0,05916/n à 25 °C : ici n = 2, donc 0,02958 V multiplié par log([Ox]/[Red])."),
        qcm("Deux couples ont E° = +1,51 V et E° = +0,77 V. Lequel est le plus oxydant ?",
            ["Celui à +0,77 V", "Celui à +1,51 V", "Les deux sont équivalents", "On ne peut pas le déduire de E°"], 1,
            "Plus E°(réduction) est positif, plus le couple a tendance à être réduit, donc plus son membre oxydé est oxydant (ici MnO₄⁻)."),
        qcm("Combien de moles de Fe²⁺ sont oxydées par 1 mol de MnO₄⁻ en milieu acide ?",
            ["1", "2", "5", "8"], 2,
            "5 Fe²⁺ + MnO₄⁻ + 8 H⁺ → 5 Fe³⁺ + Mn²⁺ + 4 H₂O : 5 électrons sont cédés par 5 Fe²⁺ et acceptés par 1 MnO₄⁻."),
        qcm("Pourquoi le potentiel du couple MnO₄⁻/Mn²⁺ dépend-il fortement du pH ?",
            ["Parce que Mn est un métal", "Parce que 8 H⁺ interviennent dans la demi-réaction à 5 e⁻", "Parce que le platine s'oxyde", "Parce que KMnO₄ est coloré"], 1,
            "Q contient [H⁺]⁸ et n = 5 : la pente est −0,05916 × 8/5 ≈ −0,095 V par unité de pH ; le pouvoir oxydant chute quand le pH monte."),
        qcm("Quelle espèce sert d'auto-indicateur dans un titrage par le permanganate ?",
            ["L'amidon", "La ferroïne", "Le KMnO₄ lui-même (rose/violet)", "Le phénolphtaléine"], 2,
            "L'ion MnO₄⁻ est intensément violet-rose : la première goutte en excès colore la solution, ce qui signale l'équivalence. L'amidon sert pour l'iode, la ferroïne pour le dichromate."),
        qt("Calculer le potentiel du couple Fe³⁺/Fe²⁺ (E° = 0,771 V, n = 1) à 25 °C pour [Fe³⁺] = 0,010 mol/L et [Fe²⁺] = 0,10 mol/L.",
           "E = E° + 0,05916 log([Fe³⁺]/[Fe²⁺]) = 0,771 + 0,05916 log(0,010/0,10) = 0,771 + 0,05916 × (−1) ≈ 0,712 V.",
           "Le rapport vaut 0,1 : le terme de Nernst vaut −0,05916 V. La forme oxydée moins concentrée abaisse le potentiel."),
        qt("Pourquoi l'équation bilan d'une réaction redox ne contient-elle pas d'électrons ?",
           "Parce que les électrons cédés par le réducteur sont exactement consommés par l'oxydant : on multiplie les demi-réactions pour que n(e⁻) soient égaux, puis on les additionne et ils s'annulent. Le bilan ne conserve que les espèces chimiques et la charge globale.",
           "Vérification : dans 5 Fe²⁺ + MnO₄⁻ + 8 H⁺ → 5 Fe³⁺ + Mn²⁺ + 4 H₂O, les charges sont +17 de chaque côté."),
    ],
    [
        {"type": "intro", "titre": "L’idée en une phrase",
         "texte": "Un couple redox échange des électrons : son potentiel E° mesure son pouvoir oxydant, et la loi de Nernst explique pourquoi E change avec les concentrations et le pH."},
        {"type": "formule", "titre": "L’équation de Nernst à connaître",
         "eq": "E = E° − (RT/nF) ln Q  →  E = E° + (0,05916/n) log([Ox]/[Red]) à 25 °C",
         "leg": "R = 8,314 J·mol⁻¹·K⁻¹ · T en K · F = 96 485 C·mol⁻¹ · n = électrons échangés · 0,05916 V = (RT/F)ln10 à 298 K"},
        {"type": "grille", "titre": "Les 3 grandeurs du chapitre", "items": [
            ["E°", "Potentiel standard du couple : référence E°(H⁺/H₂) = 0 V", "V (volt)"],
            ["n", "Nombre d’électrons de la demi-réaction Ox + n e⁻ ⇌ Red", "sans unité"],
            ["Q", "Quotient réactionnel : rapport des activités Red/Ox (et H⁺ si présent)", "sans unité"]]},
        {"type": "liste", "titre": "Couples et titrages à connaître", "items": [
            "MnO₄⁻/Mn²⁺ : E° ≈ 1,51 V · 5 e⁻ · 8 H⁺ → auto-indicateur, milieu H₂SO₄",
            "Cr₂O₇²⁻/Cr³⁺ : E° ≈ 1,33 V · 6 e⁻ → indicateur ferroïne, dosage de la DCO",
            "I₂/I⁻ : E° ≈ 0,54 V · 2 e⁻ → amidon (complexe bleu) ; S₂O₃²⁻ réduit I₂",
            "Fe³⁺/Fe²⁺ : E° = 0,771 V · 1 e⁻ → couple de référence pour les titrages redox"]},
        {"type": "etapes", "titre": "Équilibrer et exploiter un titrage redox", "items": [
            "Écrire les deux demi-réactions en réduction et repérer n pour chacune",
            "Multiplier chaque demi-réaction pour égaliser les électrons, puis additionner",
            "À l’équivalence : n(e⁻ cédés) = n(e⁻ acceptés), donc en déduire le nombre de moles",
            "Suivre E = f(V) au potentiomètre ; le saut de potentiel donne le point d’équivalence",
            "Calculer la concentration cherchée puis la rapporter à l’échantillon initial (dilution)"]},
        {"type": "attention", "titre": "⚠️ Pièges à éviter", "items": [
            "Oublier de diviser le terme 0,05916 par n",
            "Inverser le rapport [Ox]/[Red] : E augmente quand la forme oxydée augmente",
            "Négliger les H⁺ : pour MnO₄⁻, le potentiel chute d’environ 0,095 V par unité de pH",
            "Utiliser HCl avec KMnO₄ : les ions Cl⁻ sont oxydés et consomment le titrant",
            "Lire un potentiel avant stabilisation ou avec une électrode de référence non entretenue"]},
        {"type": "exemples", "titre": "Exemples chiffrés", "items": [
            "<span class=\"cle\">Fe³⁺/Fe²⁺</span> : [Ox]/[Red] = 0,1 → E = 0,771 − 0,05916 ≈ 0,712 V",
            "<span class=\"cle\">MnO₄⁻/Mn²⁺</span> : pente −(8/5)×0,05916 ≈ −0,095 V/pH",
            "<span class=\"cle\">5 Fe²⁺ + MnO₄⁻</span> + 8 H⁺ → 5 Fe³⁺ + Mn²⁺ + 4 H₂O",
            "<span class=\"cle\">I₂ + 2 S₂O₃²⁻</span> → 2 I⁻ + S₄O₆²⁻ (amidon = indicateur)",
            "<span class=\"cle\">ΔG° = −n F E°</span> et <span class=\"cle\">E° = (0,05916/n) log K</span> à 25 °C"]}
    ],
    [
        {"titre": "1 · Couple redox et transfert d’électrons", "svg": """<svg viewBox="0 0 660 185" width="100%" role="img" aria-label="Cellule redox : demi-réactions, transfert d'électrons et pont salin">
    <defs><marker id="pc5a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
    <text x="16" y="24" fill="var(--ac)" font-size="14" font-weight="bold">Deux couples, un transfert d’électrons, un potentiel</text>
    <rect x="36" y="56" width="200" height="96" rx="8" fill="var(--card2)" stroke="var(--ac)"/>
    <text x="136" y="80" text-anchor="middle" fill="var(--fg)" font-size="12">Ox₁ + n e⁻ ⇌ Red₁</text>
    <text x="136" y="102" text-anchor="middle" fill="var(--dim)" font-size="11">couple 1 · E°₁ élevé</text>
    <text x="136" y="124" text-anchor="middle" fill="var(--fg)" font-size="11">reçoit les e⁻ (réduction)</text>
    <rect x="424" y="56" width="200" height="96" rx="8" fill="var(--card2)" stroke="var(--warn)"/>
    <text x="524" y="80" text-anchor="middle" fill="var(--fg)" font-size="12">Ox₂ + n e⁻ ⇌ Red₂</text>
    <text x="524" y="102" text-anchor="middle" fill="var(--dim)" font-size="11">couple 2 · E°₂ faible</text>
    <text x="524" y="124" text-anchor="middle" fill="var(--fg)" font-size="11">cède les e⁻ (oxydation)</text>
    <line x1="424" y1="46" x2="236" y2="46" stroke="var(--ac)" stroke-width="2.5" marker-end="url(#pc5a)"/>
    <text x="330" y="38" text-anchor="middle" fill="var(--ac)" font-size="12">n e⁻</text>
    <rect x="288" y="30" width="84" height="32" rx="6" fill="var(--card2)" stroke="var(--ac)"/>
    <text x="330" y="50" text-anchor="middle" fill="var(--fg)" font-size="11">voltmètre</text>
    <path d="M236 152 Q330 178 424 152" fill="none" stroke="var(--dim)" stroke-width="2"/>
    <text x="330" y="174" text-anchor="middle" fill="var(--dim)" font-size="11">pont salin : équilibre des charges</text>
    <text x="36" y="176" fill="var(--warn)" font-size="11">Électrodes inertes en Pt ; E°(H⁺/H₂) = 0 V par convention.</text>
   </svg>"""},
        {"titre": "2 · Lire l’équation de Nernst", "svg": """<svg viewBox="0 0 660 180" width="100%" role="img" aria-label="Loi de Nernst : le potentiel croît avec le rapport oxydé sur réduit">
    <defs><marker id="pc5b" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
    <rect x="12" y="10" width="470" height="24" rx="6" fill="var(--card2)" stroke="var(--dim)"/>
    <text x="20" y="27" fill="var(--ac)" font-size="15" font-weight="bold">E = E° + (0,05916/n) log([Ox]/[Red])</text>
    <text x="16" y="46" fill="var(--dim)" font-size="11">à 25 °C · n = nombre d’électrons · 0,05916 V = (RT/F)·ln 10</text>
    <line x1="60" y1="132" x2="610" y2="132" stroke="var(--dim)" stroke-width="2" marker-end="url(#pc5b)"/>
    <text x="596" y="152" fill="var(--fg)" font-size="11">[Ox]/[Red]</text>
    <line x1="60" y1="132" x2="60" y2="60" stroke="var(--dim)" stroke-width="2" marker-end="url(#pc5b)"/>
    <text x="38" y="64" fill="var(--fg)" font-size="11">E</text>
    <line x1="335" y1="60" x2="335" y2="132" stroke="var(--warn)" stroke-width="2" stroke-dasharray="5 4"/>
    <text x="345" y="72" fill="var(--warn)" font-size="11">rapport = 1 → E = E°</text>
    <line x1="80" y1="112" x2="590" y2="84" stroke="var(--ac)" stroke-width="3"/>
    <circle cx="335" cy="98" r="4" fill="var(--warn)"/>
    <text x="100" y="100" fill="var(--fg)" font-size="11">[Red] &gt; [Ox] : E &lt; E°</text>
    <text x="420" y="80" fill="var(--fg)" font-size="11">[Ox] &gt; [Red] : E &gt; E°</text>
    <text x="60" y="172" fill="var(--dim)" font-size="11">Si H⁺ intervient : ajouter le terme de pH, ex. MnO₄⁻/Mn²⁺ → −0,095 V par unité de pH.</text>
   </svg>"""},
        {"titre": "3 · Courbe de titrage redox et saut de potentiel", "svg": """<svg viewBox="0 0 660 195" width="100%" role="img" aria-label="Courbe sigmoïde E en fonction du volume de titrant avec saut au point d'équivalence">
    <defs><marker id="pc5c" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>
    <rect x="12" y="8" width="380" height="24" rx="6" fill="var(--card2)" stroke="var(--dim)"/>
    <text x="20" y="25" fill="var(--ac)" font-size="14" font-weight="bold">Suivi potentiométrique d’un titrage redox</text>
    <line x1="60" y1="150" x2="620" y2="150" stroke="var(--dim)" stroke-width="2" marker-end="url(#pc5c)"/>
    <line x1="60" y1="150" x2="60" y2="42" stroke="var(--dim)" stroke-width="2" marker-end="url(#pc5c)"/>
    <text x="600" y="170" fill="var(--fg)" font-size="11">V(titrant)</text><text x="34" y="48" fill="var(--fg)" font-size="11">E (V)</text>
    <path d="M62 140 C150 138 240 134 300 122 C325 116 338 100 346 74 C354 52 370 48 400 46 C460 42 540 40 618 40" fill="none" stroke="var(--ac)" stroke-width="3"/>
    <line x1="346" y1="42" x2="346" y2="150" stroke="var(--warn)" stroke-width="2" stroke-dasharray="5 4"/>
    <text x="352" y="60" fill="var(--warn)" font-size="11">équivalence</text>
    <line x1="300" y1="122" x2="400" y2="122" stroke="var(--warn)" stroke-width="1" stroke-dasharray="3 3"/>
    <text x="356" y="138" fill="var(--warn)" font-size="11">Eéq = (n₁E°₁ + n₂E°₂)/(n₁+n₂)</text>
    <text x="70" y="110" fill="var(--dim)" font-size="11">avant : couple du réducteur</text>
    <text x="420" y="70" fill="var(--dim)" font-size="11">après : couple de l’oxydant</text>
    <text x="60" y="188" fill="var(--dim)" font-size="11">À l’équivalence : n(e⁻ cédés) = n(e⁻ acceptés) · saut de potentiel → détection du virage.</text>
   </svg>"""}
    ]
)


FICHES = [C1, C2, C3, C4, C5]

# ---------------------------- validations ---------------------------------
ORDRE = ["intro", "formule", "grille", "liste", "etapes", "attention", "exemples"]
ids = []
for f in FICHES:
    assert 8 <= len(f["points"]) <= 12, (f["titre"], "points")
    assert 6 <= len(f["questions"]) <= 8, (f["titre"], "questions")
    assert len(f["affichage"]) == 7, (f["titre"], "affichage")
    assert [b["type"] for b in f["affichage"]] == ORDRE, (f["titre"], "ordre des blocs")
    assert 2 <= len(f["schema"]) <= 3, (f["titre"], "schema")
    for q in f["questions"]:
        assert q["correction"], f["titre"]
        if q["type"] == "qcm":
            assert len(q["options"]) == 4 and 0 <= q["correct"] < 4, q["q"]
        else:
            assert q["reponse"], q["q"]
    for s in f["schema"]:
        svg = s["svg"]
        assert svg.strip().startswith("<svg") and svg.strip().endswith("</svg>"), s["titre"]
        assert "viewBox=" in svg, s["titre"]
        for token in ("var(--fg)", "var(--ac)", "var(--dim)", "var(--card2)", "var(--warn)"):
            assert token in svg, (s["titre"], token)
        assert "http://" not in svg and "https://" not in svg, s["titre"]
        ids += re.findall(r'id="([^"]+)"', svg)
assert len(ids) == len(set(ids)), "IDs de markers dupliqués"

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "physchim-part-A.json")
with open(out, "w", encoding="utf-8") as fh:
    json.dump({"fiches": FICHES}, fh, ensure_ascii=False, indent=1)
print("OK", out, len(FICHES), "fiches,", len(ids), "markers uniques")
