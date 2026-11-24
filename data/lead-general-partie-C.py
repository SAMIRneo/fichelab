# PARTIE C — spécialités scientifiques (maths spé, physique-chimie, SVT, NSI, SI, biologie-écologie)
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lg_common import f, q, t, a, save

F, AN = [], []

SMSP1 = "Programme d'enseignement de spécialité de mathématiques de première générale, BO n° 14 du 2 avril 2026, éduscol"
SMSP2 = "Programme d'enseignement de spécialité de mathématiques de terminale générale, BO n° 14 du 2 avril 2026 (application rentrée 2027), éduscol"
SPC1 = "Programme de spécialité physique-chimie de première générale, BO spécial n° 1 du 22 janvier 2019, éduscol"
SPC2 = "Programme de spécialité physique-chimie de terminale générale, BO spécial n° 8 du 25 juillet 2019, éduscol"
SSVT1 = "Programme de spécialité sciences de la vie et de la Terre de première générale, BO spécial n° 1 du 22 janvier 2019, éduscol"
SSVT2 = "Programme de spécialité SVT de terminale générale, BO spécial n° 8 du 25 juillet 2019, éduscol"
SNSI1 = "Programme de spécialité NSI de première générale, arrêté du 17 janvier 2019, BO spécial n° 1 du 22 janvier 2019, éduscol"
SNSI2 = "Programme de spécialité NSI de terminale générale, arrêté du 19 juillet 2019, BO spécial n° 8 du 25 juillet 2019, éduscol"
SSI1 = "Programme de spécialité sciences de l'ingénieur de première générale, BO spécial n° 1 du 22 janvier 2019, éduscol"
SSI2 = "Programme de spécialité sciences de l'ingénieur de terminale générale, BO spécial n° 8 du 25 juillet 2019, éduscol"
SBIO = "Programme de spécialité biologie-écologie, BO spéciaux n° 1 du 22 janvier 2019 et n° 8 du 25 juillet 2019, éduscol"

# ---------------- MATHS SPÉ ----------------
F.append(f(["1re"], "Maths spé", "Chapitre : Nombres et calculs – ensembles, fonctions et inéquations", SMSP1, [
 "Le programme de spécialité mathématiques de première (BO n° 14 du 2 avril 2026, rentrée 2026) s'organise en grands thèmes : nombres et calculs, algèbre, fonctions, géométrie, statistiques et probabilités, algorithmique.",
 "Le chapitre « Nombres et calculs » consolide la maîtrise des ensembles de nombres : ℕ, ℤ, ℚ, ℝ et les notations d'intervalle (ouvert, fermé, semi-ouvert).",
 "Les puissances et les racines obéissent à des règles de calcul précises : a^n · a^m = a^(n+m), (a^n)^m = a^(nm), √(a²) = |a| pour a réel.",
 "La résolution d'inéquations du premier degré repose sur l'ordre compatible avec l'addition et la multiplication par un nombre positif ; multiplier par un négatif inverse le sens.",
 "Une inéquation produit (x – a)(x – b) > 0 se résout par le tableau de signes : le produit est positif à l'extérieur des racines si a < b.",
 "La valeur absolue |x – a| mesure une distance : |x – a| ≤ r équivaut à a – r ≤ x ≤ a + r, ce qui est fondamental pour les intervalles de confiance.",
 "La notion de suite numérique est introduite : une suite est une fonction de ℕ vers ℝ, définie explicitement (u_n = n²) ou par récurrence (u_(n+1) = 3u_n + 1).",
 "Le raisonnement par récurrence permet de démontrer une propriété P(n) pour tout n : initialisation puis hérédité (si P(n) vraie, P(n+1) vraie).",
 "Les exemples de suites arithmétiques (u_(n+1) = u_n + d) et géométriques (u_(n+1) = q·u_n) donnent lieu à des formules explicites à connaître.",
 "La calculatrice et le Python sont des outils de vérification, mais l'exigence du programme porte sur la justification mathématique des résultats."
], [
 q("Que vaut √(a²) pour a réel ?", ["a", "|a|", "a²", "–a"], 1, "La racine carrée de a² est la valeur absolue de a : elle est toujours positive ou nulle."),
 q("Quel ensemble désigne le symbole ℚ ?", ["Les entiers naturels", "Les nombres rationnels", "Les nombres réels", "Les nombres complexes"], 1, "ℚ est l'ensemble des nombres qui s'écrivent sous la forme d'un quotient de deux entiers, dénominateur non nul."),
 q("Que se passe-t-il quand on multiplie une inéquation par un nombre négatif ?", ["Le sens change", "Le sens reste identique", "L'inéquation devient une équation", "On ajoute le nombre"], 0, "Multiplier par un nombre strictement négatif inverse le sens de l'inégalité."),
 q("Que désigne une suite définie par u_(n+1) = q·u_n ?", ["Une suite arithmétique", "Une suite géométrique de raison q", "Une suite constante", "Une suite croissante"], 1, "Chaque terme est obtenu en multipliant le précédent par q : c'est une suite géométrique de raison q."),
 q("Quelles sont les deux étapes d'un raisonnement par récurrence ?", ["Initialisation et hérédité", "Hypothèse et conclusion", "Existence et unicité", "Direct et contraposé"], 0, "On vérifie d'abord P(0) (ou P(1)), puis on montre que P(n) entraîne P(n+1)."),
 t("Comment résoudre une inéquation produit (x – 1)(x – 3) > 0 ?", "En étudiant le signe de chaque facteur : le produit est positif pour x < 1 ou x > 3.", "Le tableau de signes donne les racines 1 et 3 ; le produit est négatif entre elles et positif à l'extérieur, d'où la solution ]–∞ ; 1[ ∪ ]3 ; +∞[."),
 t("Que signifie |x – 2| ≤ 3 ?", "La distance entre x et 2 est au plus 3, soit x appartenant à [–1 ; 5].", "L'inégalité équivaut à 2 – 3 ≤ x ≤ 2 + 3 ; la valeur absolue est un outil de mesure de distance sur la droite réelle."),
 t("Pourquoi la démonstration par récurrence est-elle un outil essentiel ?", "Elle permet d'établir une propriété pour une infinité d'entiers en deux étapes finies.", "Elle repose sur le principe de récurrence de ℕ : si une propriété est vraie au rang initial et se transmet d'un rang au suivant, elle est vraie pour tous les rangs.")
])),

F.append(f(["1re"], "Maths spé", "Chapitre : Fonctions – variations, dérivation et optimisation", SMSP1, [
 "L'étude des fonctions constitue un pilier du programme de spécialité : on analyse leurs variations, leurs extrema et leurs représentations graphiques.",
 "Une fonction f est croissante sur un intervalle I si, pour tous x₁ < x₂ de I, on a f(x₁) ≤ f(x₂) ; elle est strictement croissante si l'inégalité est stricte.",
 "Le taux d'accroissement entre a et b vaut (f(b) – f(a))/(b – a) : il représente la pente de la sécante à la courbe et préfigure la dérivée.",
 "La dérivée f'(a) est la limite du taux d'accroissement quand b tend vers a ; elle donne le coefficient directeur de la tangente en a.",
 "Les dérivées usuelles doivent être connues : (x^n)' = n·x^(n–1), (sin x)' = cos x, (cos x)' = –sin x, (e^x)' = e^x, (ln x)' = 1/x sur ]0 ; +∞[.",
 "La dérivée d'un produit et d'un quotient : (uv)' = u'v + uv' et (u/v)' = (u'v – uv')/v² (v non nul). La dérivée d'une composée est (u∘v)' = u'(v)·v'.",
 "Le théorème des variations relie le signe de la dérivée au sens de variation : si f' > 0 sur I, f est strictement croissante sur I ; si f' < 0, elle est strictement décroissante.",
 "Un extremum local se produit en un point où la dérivée s'annule ou n'existe pas, avec changement de signe de f'. La recherche d'extrema est au cœur des problèmes d'optimisation.",
 "Le théorème de la valeur intermédiaire (fonction continue) et le théorème des extrema sur un segment (continu sur un segment) fondent de nombreuses démonstrations d'existence.",
 "Les applications concrètes (maximisation d'une aire, minimisation d'un coût, modèle de croissance) exigent de modéliser, d'étudier la fonction puis d'interpréter le résultat."
], [
 q("Quelle est la dérivée de ln x sur ]0 ; +∞[ ?", ["x", "1/x", "e^x", "–1/x²"], 1, "La fonction ln est dérivable sur ]0 ; +∞[ et (ln x)' = 1/x."),
 q("Que représente la dérivée f'(a) ?", ["L'aire sous la courbe", "Le coefficient directeur de la tangente en a", "La valeur maximale de f", "La limite de f en a"], 1, "f'(a) est la pente de la tangente à la courbe représentative au point d'abscisse a."),
 q("Quelle est la dérivée du produit uv ?", ["u'v'", "u'v + uv'", "uv", "u'v – uv'"], 1, "La règle du produit donne (uv)' = u'v + uv'."),
 q("Si f' > 0 sur un intervalle I, alors f est…", ["Décroissante sur I", "Croissante sur I", "Constante sur I", "Périodique sur I"], 1, "Le signe positif de la dérivée implique la croissance stricte de la fonction sur l'intervalle."),
 q("Quel théorème garantit qu'une fonction continue sur [a ; b] atteint un maximum ?", ["Le théorème des extrema", "Le théorème de la valeur intermédiaire", "Le théorème de Rolle", "Le principe de récurrence"], 0, "Le théorème des extrema (Weierstrass) énonce qu'une fonction continue sur un segment admet un maximum et un minimum."),
 t("Quelle est la démarche pour étudier les variations d'une fonction ?", "Calculer la dérivée, étudier son signe, puis en déduire le tableau de variations.", "On détermine d'abord le domaine de définition, puis f', ses zéros et son signe, avant de construire le tableau de variations et de tracer la courbe."),
 t("Comment résoudre un problème d'optimisation à l'aide de la dérivation ?", "En exprimant la grandeur à optimiser comme une fonction d'une variable, puis en cherchant ses extrema.", "Il faut modéliser (choix de la variable, domaine), dériver, trouver les points critiques, comparer les valeurs aux bornes et interpréter le résultat dans la situation."),
 t("Pourquoi le taux d'accroissement conduit-il à la dérivée ?", "Parce que la dérivée est la limite du taux d'accroissement lorsque l'intervalle devient infinitésimal.", "Le taux d'accroissement entre a et a+h est [f(a+h) – f(a)]/h ; sa limite quand h tend vers 0 donne la vitesse instantanée de variation.")
])),

F.append(f(["1re"], "Maths spé", "Chapitre : Géométrie dans l'espace et trigonométrie", SMSP1, [
 "Le programme de géométrie de première porte sur la géométrie dans l'espace (vecteurs, droites, plans) et sur la trigonométrie du triangle.",
 "Dans l'espace muni d'un repère orthonormal, un point est repéré par trois coordonnées (x ; y ; z) et un vecteur par trois composantes.",
 "Le produit scalaire de deux vecteurs u et v vérifie u·v = ||u||·||v||·cos(θ), où θ est l'angle entre eux ; il permet de calculer des angles et de tester l'orthogonalité.",
 "Le produit vectoriel u × v donne un vecteur orthogonal à u et à v, de norme ||u||·||v||·sin(θ) ; il est utilisé pour les normales aux plans et les aires de parallélogrammes.",
 "Une droite est définie par un point et un vecteur directeur ; un plan par un point et deux vecteurs directeurs non colinéaires, ou par une équation ax + by + cz + d = 0.",
 "La distance d'un point à un plan et la distance de deux droites non coplanaires se calculent par des formules vectorielles.",
 "En trigonométrie, les fonctions sinus, cosinus et tangente sont définies sur le cercle trigonométrique de rayon 1 ; elles sont périodiques de période 2π (π pour la tangente).",
 "Les relations fondamentales : cos²x + sin²x = 1 et tan x = sin x / cos x (cos x ≠ 0), complétées par les formules d'addition et de duplication.",
 "Dans un triangle, le théorème des sinus (a/sin A = b/sin B = c/sin C = 2R) et le théorème d'Al-Kashi (c² = a² + b² – 2ab cos C) permettent de résoudre tous les triangles.",
 "Les applications (calcul de distances inaccessibles, inclinaison d'un plan, modélisation de phénomènes périodiques) exigent de choisir la bonne relation et de justifier les approximations."
], [
 q("Quel est le produit scalaire de deux vecteurs orthogonaux ?", ["Leur norme", "0", "1", "Leur produit vectoriel"], 1, "Deux vecteurs sont orthogonaux si et seulement si leur produit scalaire est nul."),
 q("Quelle est la norme du produit vectoriel u × v ?", ["||u||·||v||·cos θ", "||u||·||v||·sin θ", "||u|| + ||v||", "0"], 1, "La norme du produit vectoriel vaut ||u||·||v||·sin θ ; elle donne l'aire du parallélogramme construit sur u et v."),
 q("Quelle est la période de la fonction tangente ?", ["2π", "π", "π/2", "4π"], 1, "La tangente est périodique de période π, contrairement au sinus et au cosinus (2π)."),
 q("Que donne l'identité cos²x + sin²x ?", ["0", "1", "tan x", "cos 2x"], 1, "C'est l'identité trigonométrique fondamentale, conséquence du théorème de Pythagore sur le cercle unité."),
 q("Quel théorème généralise le théorème de Pythagore ?", ["Le théorème de Thalès", "Le théorème d'Al-Kashi", "Le théorème de Rolle", "Le théorème de Bayes"], 1, "Al-Kashi (loi des cosinus) : c² = a² + b² – 2ab cos C, qui redonne Pythagore quand C = 90°."),
 t("Comment calculer l'angle entre deux vecteurs ?", "En utilisant la formule cos θ = (u·v)/(||u||·||v||).", "Le produit scalaire permet d'isoler le cosinus de l'angle ; on en déduit θ ∈ [0 ; π] par la fonction arccos."),
 t("Quelle est la différence entre produit scalaire et produit vectoriel ?", "Le produit scalaire donne un nombre et mesure les angles ; le produit vectoriel donne un vecteur orthogonal.", "Le premier est lié au cosinus et à la projection, le second au sinus et à l'aire : ils sont complémentaires en géométrie spatiale."),
 t("Comment modéliser un phénomène périodique avec la trigonométrie ?", "En utilisant une fonction de la forme A·sin(ωt + φ) + B ou A·cos(ωt + φ) + B.", "L'amplitude A, la pulsation ω (période T = 2π/ω), la phase φ et le décalage B permettent d'ajuster le modèle à des données réelles.")
])),

F.append(f(["Terminale"], "Maths spé", "Chapitre : Suites, limites et continuité", SMSP2, [
 "Le programme de spécialité de terminale (BO n° 14 du 2 avril 2026, entrée en vigueur rentrée 2027) approfondit l'analyse : suites, limites, continuité et dérivation.",
 "Une suite (u_n) converge vers L si, pour tout ε > 0, il existe un rang N à partir duquel |u_n – L| < ε : les termes se rapprochent arbitrairement de L.",
 "Une suite croissante et majorée converge ; une suite décroissante et minorée converge : c'est le théorème de convergence monotone, fondamental pour les suites récurrentes.",
 "Les limites usuelles sont indispensables : lim q^n = 0 si |q| < 1, lim n^α / e^n = 0 pour α > 0, lim (ln n)/n = 0 et lim n^(1/n) = 1.",
 "Les opérations sur les limites (somme, produit, quotient sous réserve que la limite du dénominateur soit non nulle) permettent de calculer des limites complexes.",
 "Une fonction f est continue en a si lim_(x→a) f(x) = f(a) : la courbe ne présente pas de rupture en ce point.",
 "Le théorème des valeurs intermédiaires énonce qu'une fonction continue sur [a ; b] prend toutes les valeurs entre f(a) et f(b) : il justifie l'existence de solutions d'équations.",
 "La continuité sur un segment implique l'existence d'un maximum et d'un minimum (théorème des extrema de Weierstrass).",
 "Les suites définies par récurrence u_(n+1) = f(u_n) s'étudient par l'étude de la fonction f : points fixes, variations et convergence.",
 "La maîtrise du langage ε–N et des théorèmes d'existence est exigée dans les épreuves de mathématiques spécialité."
], [
 q("Que signifie « (u_n) converge vers L » ?", ["Les termes sont tous égaux à L", "Pour tout ε > 0, |u_n – L| < ε à partir d'un certain rang", "La suite est croissante", "La suite est bornée"], 1, "La définition ε–N traduit la convergence : les termes finissent par entrer et rester dans tout voisinage de L."),
 q("Quelle suite converge vers 0 ?", ["q^n avec |q| < 1", "q^n avec q > 1", "n²", "(-1)^n"], 0, "Pour |q| < 1, les puissances de q tendent vers 0 ; (-1)^n diverge par oscillation."),
 q("Quel théorème garantit la convergence d'une suite croissante majorée ?", ["Le théorème de convergence monotone", "Le théorème de Rolle", "Le théorème de Bayes", "Le théorème de Pythagore"], 0, "Une suite monotone et bornée est convergente : résultat fondamental de l'analyse réelle."),
 q("Quand une fonction f est-elle continue en a ?", ["Quand f(a) existe", "Quand lim_(x→a) f(x) = f(a)", "Quand f est dérivable en a", "Quand f est croissante"], 1, "La continuité exige l'existence de la limite et son égalité avec la valeur de la fonction au point."),
 q("Que permet le théorème des valeurs intermédiaires ?", ["De calculer une dérivée", "D'affirmer l'existence d'une solution à f(x) = k", "De prouver la convergence d'une suite", "De tracer une asymptote"], 1, "Si f est continue sur [a ; b] et si k est entre f(a) et f(b), alors il existe c avec f(c) = k."),
 t("Comment étudier la convergence d'une suite récurrente u_(n+1) = f(u_n) ?", "En étudiant les variations de f et ses points fixes, puis en comparant u_n à la limite pressentie.", "On recherche les points fixes L = f(L), on étudie le signe de f(x) – x et la monotonie de f pour encadrer la suite et appliquer le théorème de convergence monotone."),
 t("Pourquoi une suite croissante majorée converge-t-elle ?", "Parce que l'ensemble de ses valeurs est majoré et possède donc une borne supérieure, vers laquelle la suite tend.", "La borne supérieure de l'ensemble {u_n} est la limite : pour tout ε, il existe un terme à partir duquel tous les termes dépassent la borne supérieure – ε."),
 t("Quelle est la différence entre continuité et dérivabilité ?", "La dérivabilité implique la continuité, mais une fonction continue n'est pas forcément dérivable.", "Une fonction dérivable en a est continue en a ; l'exemple de la valeur absolue en 0 montre qu'une fonction peut être continue sans avoir de dérivée.")
])),

# ---------------- PHYSIQUE-CHIMIE ----------------
F.append(f(["1re"], "Physique-chimie", "Chapitre : Mouvement et interactions – cinématique et lois de Newton", SPC1, [
 "Le programme de physique-chimie de première organise le chapitre « Mouvement et interactions » autour de la description du mouvement et de l'étude des forces.",
 "Le mouvement d'un point est décrit par sa position, sa vitesse et son accélération, exprimées par des vecteurs dans un repère choisi.",
 "En cinématique, le vecteur vitesse est la dérivée du vecteur position par rapport au temps ; le vecteur accélération est la dérivée du vecteur vitesse.",
 "Un mouvement rectiligne uniforme a une vitesse constante et une accélération nulle ; un mouvement uniformément accéléré a une accélération constante.",
 "La deuxième loi de Newton (principe fondamental de la dynamique) s'écrit ΣF = m·a : l'accélération d'un système est proportionnelle à la somme des forces et inversement proportionnelle à sa masse.",
 "La première loi de Newton (principe d'inertie) énonce qu'un système isolé conserve son vecteur vitesse : il est immobile ou en mouvement rectiligne uniforme.",
 "La troisième loi (action–réaction) précise que si un corps A agit sur B, B agit sur A avec une force opposée, de même intensité et de même ligne d'action.",
 "Les forces usuelles étudiées sont le poids (P = m·g, vertical descendant), la réaction normale, la tension d'un câble et les forces de frottement.",
 "Dans le cadre d'une chute avec frottements fluides, la vitesse tend vers une vitesse limite lorsque la force de frottement compense le poids.",
 "La résolution d'un problème de dynamique exige un schéma des forces, un choix d'axes, l'application de la deuxième loi et une vérification de l'unité des grandeurs."
], [
 q("Quelle est l'expression du principe fondamental de la dynamique ?", ["ΣF = m·a", "F = m·v", "E = m·c²", "P = m·g"], 0, "La deuxième loi de Newton relie la somme des forces, la masse et l'accélération : ΣF = m·a."),
 q("Quel est le principe d'inertie ?", ["Un système isolé reste immobile ou en mouvement rectiligne uniforme", "Tout corps tombe", "Les forces s'annulent toujours", "La masse est constante"], 0, "Le principe d'inertie correspond à la première loi de Newton : sans force nette, le vecteur vitesse est constant."),
 q("Quelle est l'unité SI de l'accélération ?", ["m/s", "m/s²", "kg·m/s", "N"], 1, "L'accélération s'exprime en mètres par seconde carrée (m·s⁻²)."),
 q("Comment s'écrit le poids d'un corps de masse m ?", ["P = m/g", "P = m·g", "P = g/m", "P = m·v"], 1, "Le poids est la force exercée par la gravité : P = m·g, avec g ≈ 9,81 m·s⁻² sur Terre."),
 q("Que se passe-t-il à la vitesse limite d'un objet en chute avec frottements ?", ["L'accélération devient nulle", "Le poids disparaît", "La vitesse augmente encore", "Les forces s'annulent deux à deux"], 0, "À la vitesse limite, la somme des forces est nulle : l'accélération est nulle mais la vitesse reste constante et non nulle."),
 t("Quelle démarche suivre pour résoudre un exercice de dynamique ?", "Faire le schéma des forces, choisir un repère, appliquer ΣF = m·a puis vérifier les unités.", "Cette méthode systématique évite les erreurs de signe et permet de passer du schéma à l'équation du mouvement."),
 t("Quelle est la différence entre masse et poids ?", "La masse est une grandeur intrinsèque (kg), le poids est une force dépendant du champ de gravité (N).", "Un astronaute garde sa masse sur la Lune mais son poids y est six fois plus faible : le poids dépend de g, la masse non."),
 t("Pourquoi la deuxième loi de Newton est-elle une loi vectorielle ?", "Parce que force et accélération ont une direction et un sens : l'accélération est colinéaire à la force résultante.", "On projette la relation sur chaque axe du repère : ΣF_x = m·a_x et ΣF_y = m·a_y, ce qui donne un système d'équations.")
])),

F.append(f(["1re"], "Physique-chimie", "Chapitre : Énergie – transferts, conversions et rendement", SPC1, [
 "La notion d'énergie permet d'unifier l'étude des phénomènes mécaniques, thermiques, électriques et chimiques du programme de première.",
 "L'énergie cinétique d'un corps de masse m et de vitesse v vaut E_c = ½·m·v² ; elle est toujours positive et nulle au repos.",
 "L'énergie potentielle de pesanteur, dans un champ uniforme, vaut E_pp = m·g·h ; elle dépend de l'altitude choisie comme origine.",
 "Le travail d'une force constante est W = F·d·cos α : il est positif si la force favorise le déplacement, négatif si elle s'y oppose.",
 "Le théorème de l'énergie cinétique énonce que la variation d'énergie cinétique est égale à la somme des travaux des forces : ΔE_c = ΣW.",
 "La conservation de l'énergie mécanique (E_m = E_c + E_pp) vaut en l'absence de frottements : l'énergie se transforme mais ne se perd pas.",
 "Avec des frottements, une partie de l'énergie mécanique est convertie en énergie thermique : E_m(initial) = E_m(final) + énergie dissipée.",
 "La puissance est le rapport de l'énergie transférée au temps mis : P = W/Δt, exprimée en watts (1 W = 1 J/s).",
 "Le rendement d'un système est le rapport entre l'énergie utile et l'énergie consommée : η = E_utile / E_fournie, toujours inférieur à 1.",
 "Les applications (freinage d'une voiture, centrale hydroélectrique, moteur) exigent de faire un bilan énergétique et d'identifier les pertes."
], [
 q("Quelle est l'expression de l'énergie cinétique ?", ["m·g·h", "½·m·v²", "F·d", "m·v"], 1, "L'énergie cinétique vaut ½ m v² ; m g h est l'énergie potentielle de pesanteur."),
 q("Dans quelles conditions l'énergie mécanique est-elle conservée ?", ["Toujours", "En l'absence de frottements", "Uniquement au repos", "Quand la vitesse est nulle"], 1, "La conservation de E_m = E_c + E_pp suppose l'absence de forces dissipatives (frottements)."),
 q("Quelle est l'unité de la puissance ?", ["Le joule", "Le watt", "Le newton", "Le pascal"], 1, "La puissance s'exprime en watts : 1 W = 1 J·s⁻¹."),
 q("Quel est le rendement d'un moteur qui restitue 60 J d'énergie utile pour 100 J consommés ?", ["60 %", "40 %", "100 %", "1,67"], 0, "Le rendement vaut 60/100 = 0,6, soit 60 % ; il est toujours inférieur à 1."),
 q("Que devient l'énergie mécanique perdue par frottement ?", ["Elle disparaît", "Elle est convertie en énergie thermique", "Elle est stockée dans le vide", "Elle devient de la masse"], 1, "Les frottements transforment l'énergie mécanique en énergie thermique : c'est une conversion, pas une destruction."),
 t("Comment établir un bilan énergétique ?", "En identifiant les réservoirs d'énergie, les transferts et les conversions, puis en écrivant l'égalité entre énergie reçue et énergie cédée.", "Le bilan est une écriture de la conservation de l'énergie : ce qui est gagné par un système est perdu par un autre, sous forme utile ou dissipée."),
 t("Quelle est la différence entre travail et puissance ?", "Le travail est une énergie transférée ; la puissance est le rythme de ce transfert.", "Un même travail peut être fourni lentement ou rapidement : la puissance distingue ces deux situations par le rapport à la durée."),
 t("Pourquoi le rendement d'un système réel est-il toujours inférieur à 1 ?", "Parce qu'une partie de l'énergie est dissipée, souvent sous forme de chaleur, lors des conversions.", "Le rendement traduit les pertes inévitables liées aux frottements, à la résistance électrique ou aux transferts thermiques.")
])),

F.append(f(["1re"], "Physique-chimie", "Chapitre : Transformations chimiques – acides, bases et réactions", SPC1, [
 "Le programme de première consacre un chapitre aux transformations chimiques, avec l'étude des réactions acide-base et des oxydoréductions.",
 "Un acide est une espèce capable de libérer des ions hydrogène H⁺ (ou H₃O⁺ en solution aqueuse) ; une base peut capter ces ions (définition de Brønsted–Lowry).",
 "Le pH mesure l'acidité d'une solution : pH = –log[H₃O⁺]. Une solution est acide si pH < 7, neutre si pH = 7 et basique si pH > 7 à 25 °C.",
 "L'échelle de pH est logarithmique : une diminution d'une unité de pH multiplie la concentration en ions H₃O⁺ par 10.",
 "Une réaction acide-base est une réaction de transfert de proton : par exemple HCl + H₂O → H₃O⁺ + Cl⁻, où HCl est l'acide et H₂O la base.",
 "Un indicateur coloré (papier pH, phénolphtaléine, bleu de bromothymol) permet de suivre qualitativement le pH ; un pH-mètre donne une mesure quantitative.",
 "Une titration (dosage) consiste à ajouter progressivement une solution de concentration connue à une autre jusqu'à l'équivalence, où les réactifs sont en proportions stœchiométriques.",
 "Une oxydoréduction est un transfert d'électrons : l'oxydant capte des électrons et est réduit, le réducteur cède des électrons et est oxydé.",
 "Le couple oxydant/réductant s'écrit Ox + n e⁻ ⇌ Red ; la réactivité d'un système dépend du potentiel d'oxydoréduction.",
 "Les applications (traitement des eaux, piles, corrosion, digestion) montrent l'importance de ces réactions dans la vie quotidienne et l'industrie."
], [
 q("Quelle est la définition d'un acide selon Brønsted–Lowry ?", ["Une espèce qui capte des électrons", "Une espèce qui cède un proton H⁺", "Une espèce qui libère de l'oxygène", "Une espèce de pH supérieur à 7"], 1, "Un acide est un donneur de proton, une base un accepteur de proton."),
 q("Quelle est la relation entre pH et concentration en H₃O⁺ ?", ["pH = log[H₃O⁺]", "pH = –log[H₃O⁺]", "pH = [H₃O⁺]", "pH = 14 – [H₃O⁺]"], 1, "Le pH est le logarithme décimal négatif de la concentration en ions hydronium."),
 q("Si le pH passe de 3 à 2, la concentration en H₃O⁺ est…", ["Multipliée par 10", "Divisée par 10", "Multipliée par 2", "Inchangée"], 0, "L'échelle étant logarithmique, un écart d'une unité correspond à un facteur 10."),
 q("Que se passe-t-il à l'équivalence d'un dosage ?", ["Les réactifs sont en excès", "Les réactifs sont en proportions stœchiométriques", "Le pH est toujours 7", "La solution devient incolore"], 1, "À l'équivalence, les quantités de réactifs correspondent exactement à l'équation de la réaction ; le pH dépend de la force des espèces."),
 q("Dans une oxydoréduction, que fait l'oxydant ?", ["Il cède des électrons", "Il capte des électrons", "Il reste inchangé", "Il libère un proton"], 1, "L'oxydant capte des électrons et se réduit ; le réducteur cède des électrons et s'oxyde."),
 t("Comment mesurer le pH d'une solution ?", "À l'aide d'un indicateur coloré pour une estimation, ou d'un pH-mètre pour une mesure précise.", "Le pH-mètre, étalonné avec des solutions tampons, donne une valeur quantitative ; les indicateurs changent de couleur sur une plage de pH déterminée."),
 t("Pourquoi l'échelle de pH est-elle logarithmique ?", "Parce que les concentrations en ions H₃O⁺ varient sur plusieurs ordres de grandeur.", "Un pH de 0 à 14 couvre des concentrations de 1 à 10⁻¹⁴ mol/L : le logarithme permet de représenter cette immense plage lisiblement."),
 t("Comment reconnaître une réaction d'oxydoréduction ?", "En comparant les degrés d'oxydation des éléments avant et après la réaction.", "Si un degré d'oxydation augmente, l'élément est oxydé ; s'il diminue, il est réduit. Les deux phénomènes sont simultanés.")
])),

F.append(f(["Terminale"], "Physique-chimie", "Chapitre : Santé, sécurité et développement durable – pollutions et traitement", SPC2, [
 "Le programme de terminale physique-chimie comporte un chapitre « Santé, sécurité et développement durable » qui mobilise les connaissances chimiques sur les pollutions.",
 "Un polluant est une substance présente dans l'environnement en quantité telle qu'elle perturbe un écosystème ou nuit à la santé.",
 "Les principaux polluants de l'air sont les oxydes d'azote (NOₓ), le dioxyde de soufre (SO₂), les particules fines (PM2,5, PM10), le monoxyde de carbone (CO) et les composés organiques volatils.",
 "L'effet de serre est un phénomène naturel dû à des gaz (H₂O, CO₂, CH₄, N₂O) qui absorbent le rayonnement infrarouge émis par la surface terrestre.",
 "Le forçage radiatif mesure l'influence d'un facteur sur le bilan énergétique de la Terre : il s'exprime en W·m⁻² et permet de comparer l'impact de différents gaz ou aérosols.",
 "Le dioxyde de carbone anthropique provient principalement de la combustion des énergies fossiles et de la déforestation ; sa concentration dépasse 425 ppm en 2025 (Mauna Loa).",
 "Les polluants de l'eau comprennent les nitrates (issus des engrais), les phosphates, les métaux lourds et les micropolluants organiques (pesticides, médicaments).",
 "Le traitement des eaux usées comporte des étapes physiques (dégrillage, décantation), biologiques (boues activées) et chimiques (coagulation, désinfection).",
 "Le développement durable vise à concilier efficacité économique, équité sociale et préservation de l'environnement : les indicateurs (empreinte carbone, ACV) permettent de mesurer les impacts.",
 "La démarche d'ingénieur consiste à analyser un problème, modéliser les transferts de matière et d'énergie, puis proposer et évaluer des solutions."
], [
 q("Quel gaz est le principal contributeur au forçage radiatif humain ?", ["Le méthane", "Le dioxyde de carbone", "Le protoxyde d'azote", "La vapeur d'eau"], 1, "Le CO₂ anthropique est le principal facteur du forçage radiatif, devant le méthane et le N₂O."),
 q("Quelles particules sont désignées par PM2,5 ?", ["Des gaz invisibles", "Des particules de diamètre inférieur à 2,5 micromètres", "Des bactéries", "Des gaz à effet de serre"], 1, "PM2,5 désigne les particules fines dont le diamètre aérodynamique est inférieur à 2,5 µm ; elles pénètrent profondément dans les poumons."),
 q("Quelle est une source majeure de nitrates dans l'eau ?", ["Les engrais agricoles", "La combustion du charbon", "Les piles usagées", "Le plastique"], 0, "Le lessivage des engrais azotés est la principale source de pollution nitratée des eaux."),
 q("Quelle unité mesure le forçage radiatif ?", ["Le watt par mètre carré", "Le degré Celsius", "Le ppm", "Le joule"], 0, "Le forçage radiatif s'exprime en W·m⁻² : il quantifie un déséquilibre du bilan énergétique."),
 q("Que désigne l'analyse du cycle de vie (ACV) ?", ["Une méthode de dosage chimique", "L'évaluation des impacts environnementaux d'un produit de l'extraction à la fin de vie", "Une mesure de la qualité de l'air", "Un label alimentaire"], 1, "L'ACV recense les flux de matière et d'énergie et les impacts d'un produit à toutes les étapes de son existence."),
 t("Comment l'effet de serre naturel fonctionne-t-il ?", "Les gaz à effet de serre absorbent le rayonnement infrarouge émis par la Terre et le réémettent vers la surface.", "Sans effet de serre naturel, la température moyenne terrestre serait d'environ –18 °C au lieu de 15 °C : le problème est l'augmentation anthropique de ce phénomène."),
 t("Quelles étapes composent le traitement des eaux usées ?", "Dégrillage et décantation, traitement biologique, puis traitement chimique et désinfection.", "Cette chaîne élimine successivement les déchets grossiers, les matières organiques biodégradables, puis les micropolluants et les pathogènes."),
 t("Comment les indicateurs environnementaux aident-ils à la décision ?", "Ils quantifient les impacts et permettent de comparer des scénarios ou des solutions.", "Empreinte carbone, ACV et indicateurs de toxicité rendent visibles les effets différés ou indirects d'un choix, condition d'une démarche de développement durable.")
])),

F.append(f(["Terminale"], "Physique-chimie", "Chapitre : Modélisation et outils d'analyse – cinétique et équilibres", SPC2, [
 "La physique-chimie de terminale développe la modélisation des systèmes et l'analyse des transformations, notamment la cinétique chimique et les équilibres.",
 "La vitesse de réaction est définie par la variation de concentration d'un réactif ou d'un produit par unité de temps : v = –Δ[R]/Δt = Δ[P]/Δt (à coefficients stœchiométriques près).",
 "Les facteurs qui influencent la cinétique sont la concentration, la température, la présence d'un catalyseur et l'état de division des réactifs.",
 "Selon la théorie des collisions, une réaction a lieu si les particules entrent en collision avec une énergie suffisante (énergie d'activation) et une orientation favorable.",
 "Un catalyseur augmente la vitesse de réaction en abaissant l'énergie d'activation, sans être consommé et sans modifier la position de l'équilibre.",
 "Une réaction réversible peut atteindre un équilibre dynamique où les vitesses aller et retour sont égales : les concentrations restent constantes sans que les réactions s'arrêtent.",
 "L'expression du quotient réactionnel Q_r, comparée à la constante d'équilibre K, permet de prévoir le sens d'évolution d'un système (principe de Le Châtelier).",
 "Une perturbation (changement de concentration, de température ou de pression) déplace l'équilibre dans le sens qui s'oppose à la perturbation, selon Le Châtelier.",
 "Les modèles cinétiques et les lois d'équilibre sont des outils de prévision utilisés en chimie industrielle (synthèse de l'ammoniac, procédé Contact).",
 "La démarche expérimentale (mesures, incertitudes, exploitation) accompagne toujours la modélisation dans le programme de spécialité."
], [
 q("Quel facteur n'influence pas la vitesse d'une réaction ?", ["La température", "La concentration", "La présence d'un catalyseur", "La couleur du réactif"], 3, "La couleur n'est pas un facteur cinétique ; les trois autres modifient la fréquence ou l'énergie des collisions."),
 q("Que fait un catalyseur ?", ["Il est consommé", "Il abaisse l'énergie d'activation", "Il déplace l'équilibre", "Il change l'enthalpie de la réaction"], 1, "Le catalyseur offre un chemin réactionnel de moindre énergie d'activation, sans modifier l'équilibre thermodynamique."),
 q("Qu'est-ce qu'un équilibre dynamique ?", ["Les réactions s'arrêtent", "Les vitesses aller et retour sont égales", "Les concentrations sont nulles", "La température est constante"], 1, "À l'équilibre, les réactions se poursuivent à vitesses égales : les concentrations macroscopiques ne changent plus."),
 q("Que prédit le principe de Le Châtelier ?", ["Le sens de déplacement d'un équilibre après une perturbation", "La vitesse d'une réaction", "Le pH d'une solution", "La masse d'un précipité"], 0, "Le système évolue dans le sens qui s'oppose à la perturbation imposée."),
 q("Quelle grandeur compare-t-on à la constante K pour prévoir le sens d'évolution ?", ["Le quotient réactionnel Q_r", "La température", "La masse molaire", "La pression partielle"], 0, "Si Q_r < K, la réaction évolue dans le sens aller ; si Q_r > K, elle évolue en sens inverse."),
 t("Pourquoi faut-il une énergie d'activation pour qu'une réaction ait lieu ?", "Parce que les molécules doivent franchir une barrière énergétique pour rompre leurs liaisons et en former de nouvelles.", "La théorie des collisions explique que seules les collisions assez énergétiques et bien orientées sont efficaces : la température augmente leur fréquence."),
 t("Comment un catalyseur agit-il sur une réaction réversible ?", "Il accélère également les deux sens de la réaction et ne modifie pas la composition à l'équilibre.", "En abaissant l'énergie d'activation dans les deux directions, il permet d'atteindre plus vite le même équilibre."),
 t("Quelle est la différence entre cinétique et thermodynamique ?", "La cinétique étudie la vitesse des réactions ; la thermodynamique étudie leur faisabilité et leur équilibre.", "Une réaction thermodynamiquement favorable peut être très lente : le catalyseur agit sur la cinétique, pas sur la thermodynamique.")
])),

# ---------------- SVT ----------------
F.append(f(["1re"], "SVT", "Chapitre : Génétique et hérédité – ADN, chromosomes et lois de Mendel", SSVT1, [
 "Le programme de SVT de première commence par la génétique : l'information héréditaire est portée par l'ADN des chromosomes.",
 "L'ADN est une molécule en double hélice, dont le modèle est proposé par Watson et Crick en 1953 à partir des données de Rosalind Franklin ; les brins sont complémentaires (A–T, G–C).",
 "Un gène est un segment d'ADN qui porte l'information nécessaire à la synthèse d'une protéine ; les allèles sont des versions différentes d'un même gène.",
 "Le génome humain comporte 23 paires de chromosomes : 22 paires d'autosomes et une paire de chromosomes sexuels (XX chez la femme, XY chez l'homme).",
 "La réplication semi-conservatrice de l'ADN, confirmée par Meselson et Stahl en 1958, précède la division cellulaire et garantit la fidélité de la copie.",
 "La mitose produit deux cellules filles génétiquement identiques à la cellule mère ; la méiose produit quatre cellules haploïdes génétiquement différentes.",
 "Mendel (1865) énonce la loi de ségrégation des allèles : les deux allèles d'un individu se séparent lors de la formation des gamètes, chacun ayant une probabilité 1/2 d'être transmis.",
 "La loi d'indépendance des caractères précise que les allèles de gènes situés sur des chromosomes différents se répartissent indépendamment dans les gamètes.",
 "Les outils de la génétique (arbre généalogique, tableau de croisement, probabilités) permettent de prévoir la transmission de caractères et d'estimer des risques.",
 "Les mutations, spontanées ou induites, sont des modifications de la séquence d'ADN : elles sont la source de la variabilité génétique et peuvent être neutres, délétères ou bénéfiques."
], [
 q("Qui a proposé le modèle de la double hélice de l'ADN en 1953 ?", ["Mendel et Darwin", "Watson et Crick", "Pasteur et Koch", "Lamarck et Buffon"], 1, "Watson et Crick publient le modèle en 1953, en s'appuyant sur les clichés de cristallographie de Rosalind Franklin."),
 q("Quelles bases s'apparient dans l'ADN ?", ["A–G et T–C", "A–T et G–C", "A–C et G–T", "A–U et G–C"], 1, "L'adénine s'apparie avec la thymine, la guanine avec la cytosine, par liaisons hydrogène."),
 q("Combien de paires de chromosomes possède l'espèce humaine ?", ["22", "23", "46", "48"], 1, "Le caryotype humain compte 23 paires, soit 46 chromosomes, dont une paire de chromosomes sexuels."),
 q("Que produit la méiose ?", ["Deux cellules identiques", "Quatre cellules haploïdes différentes", "Quatre cellules diploïdes identiques", "Deux gamètes"], 1, "La méiose réduit le nombre de chromosomes de moitié et produit quatre cellules haploïdes génétiquement distinctes."),
 q("Quel est l'énoncé de la loi de ségrégation de Mendel ?", ["Les deux allèles se séparent lors de la formation des gamètes", "Les gènes sont sur le même chromosome", "Les caractères acquis sont héréditaires", "Un seul allèle est transmis"], 0, "Chaque gamète reçoit l'un des deux allèles de l'individu, avec une probabilité égale de 1/2."),
 t("Qu'est-ce que la réplication semi-conservatrice ?", "Chaque molécule d'ADN fille contient un brin ancien et un brin nouvellement synthétisé.", "L'expérience de Meselson et Stahl (1958) l'a confirmée en marquant l'ADN avec des isotopes de l'azote."),
 t("Quelle est la différence entre gène et allèle ?", "Le gène est une portion d'ADN ; les allèles en sont les différentes versions.", "Un individu diploïde porte deux allèles pour chaque gène, un sur chaque chromosome homologue ; ils peuvent être identiques (homozygotie) ou différents (hétérozygotie)."),
 t("Pourquoi les mutations sont-elles importantes pour l'évolution ?", "Elles créent la variabilité génétique sur laquelle la sélection naturelle peut agir.", "Sans mutation, toutes les copies seraient identiques et l'évolution des populations par sélection serait impossible.")
])),

F.append(f(["1re"], "SVT", "Chapitre : Biodiversité et évolution des êtres vivants", SSVT1, [
 "Le chapitre « Biodiversité et évolution » articule l'étude de la diversité du vivant avec les mécanismes qui l'ont produite.",
 "La biodiversité (ou diversité biologique) comprend trois niveaux : la diversité génétique, la diversité des espèces et la diversité des écosystèmes (Convention de Rio, 1992).",
 "L'évolution est le changement de la composition génétique des populations au cours des générations : elle se mesure à l'échelle des populations, pas des individus.",
 "Darwin (L'Origine des espèces, 1859) propose la sélection naturelle : les individus porteurs d'une variation héréditaire favorable survivent et se reproduisent davantage.",
 "La sélection naturelle agit sur des variations préexistantes, issues de mutations et de recombinaisons ; elle n'est pas un processus orienté vers un but.",
 "La dérive génétique désigne des changements aléatoires de fréquences alléliques, particulièrement importants dans les petites populations (effet fondateur, goulot d'étranglement).",
 "L'isolement géographique puis reproductif peut conduire à la spéciation : deux populations ne peuvent plus échanger leurs gènes et accumulent des différences.",
 "Les fossiles, l'anatomie comparée, l'embryologie et la biologie moléculaire (comparaison des séquences d'ADN) fournissent des preuves convergentes de l'évolution.",
 "Les arbres phylogénétiques représentent les relations de parenté entre espèces ; ils se construisent à partir de caractères dérivés partagés.",
 "L'érosion actuelle de la biodiversité, liée à la destruction des habitats, à la surexploitation et aux changements climatiques, motive des politiques de conservation."
], [
 q("Qui a publié L'Origine des espèces en 1859 ?", ["Lamarck", "Charles Darwin", "Mendel", "Cuvier"], 1, "Darwin y expose la théorie de la sélection naturelle, fondement de la biologie évolutive moderne."),
 q("Quels sont les trois niveaux de la biodiversité ?", ["Génétique, espèces, écosystèmes", "Cellules, tissus, organes", "Individus, populations, espèces", "Terre, océan, atmosphère"], 0, "La Convention des Nations unies sur la diversité biologique (Rio, 1992) retient ces trois niveaux."),
 q("Sur quoi la sélection naturelle agit-elle directement ?", ["Sur les individus et leurs phénotypes", "Sur les gènes isolés", "Sur les écosystèmes", "Sur les fossiles"], 0, "La sélection agit sur les individus (leur survie et leur reproduction), mais ses effets se mesurent sur les fréquences alléliques des populations."),
 q("Quel mécanisme est aléatoire et plus fort dans les petites populations ?", ["La sélection naturelle", "La dérive génétique", "La mutation dirigée", "La spéciation"], 1, "La dérive génétique modifie les fréquences alléliques par hasard, avec un effet amplifié quand l'effectif est faible."),
 q("Quelle discipline compare les séquences d'ADN pour établir des parentés ?", ["La biologie moléculaire", "La géologie", "La météorologie", "La biochimie uniquement"], 0, "La comparaison des séquences d'ADN ou de protéines permet de construire des arbres phylogénétiques et d'estimer des temps de divergence."),
 t("Comment la sélection naturelle explique-t-elle l'adaptation ?", "Les individus porteurs de variations favorables ont une meilleure survie et transmettent plus leurs allèles.", "L'adaptation n'est pas un but mais un résultat : les fréquences alléliques changent sous l'effet de la sélection, ce qui rend la population mieux adaptée à son milieu."),
 t("Quelle est la différence entre sélection naturelle et dérive génétique ?", "La sélection est déterministe et liée au milieu ; la dérive est aléatoire.", "Les deux font évoluer les fréquences alléliques, mais seule la sélection produit une adaptation au milieu."),
 t("Comment les arbres phylogénétiques sont-ils construits ?", "En comparant des caractères héréditaires et en identifiant les caractères dérivés partagés.", "Ils représentent des hypothèses de parenté, révisables à mesure que de nouvelles données (notamment moléculaires) sont disponibles.")
])),

F.append(f(["Terminale"], "SVT", "Chapitre : Génétique et évolution – du gène à la population", SSVT2, [
 "En terminale SVT, l'étude de la génétique et de l'évolution approfondit les mécanismes moléculaires et populationnels.",
 "Le code génétique est universel et dégénéré : chaque acide aminé peut être codé par plusieurs codons (triplets de nucléotides), mais un codon ne code qu'un acide aminé ou un signal d'arrêt.",
 "La transcription copie un gène en ARN messager ; la traduction, assurée par les ribosomes, convertit la séquence de nucléotides en séquence d'acides aminés.",
 "Une mutation ponctuelle (substitution, insertion, délétion) peut modifier la protéine produite : elle est silencieuse, faux-sens ou non-sens selon son effet.",
 "La recombinaison lors de la méiose (crossing-over et répartition indépendante des chromosomes) crée de nouvelles combinaisons alléliques sans modifier les allèles eux-mêmes.",
 "La structure d'une population se décrit par les fréquences alléliques et génotypiques ; l'équilibre de Hardy–Weinberg (1908) prédit ces fréquences sous des hypothèses idéalisées.",
 "Si les fréquences observées s'écartent de Hardy–Weinberg, cela signale l'action de facteurs évolutifs : sélection, dérive, mutation, migration ou non-panmixie.",
 "La spéciation résulte de l'accumulation de différences génétiques jusqu'à l'apparition de barrières reproductives (pré- ou post-zygotiques).",
 "L'évolution humaine est étudiée à partir des fossiles et des données génétiques : les migrations et les adaptations (peau, digestion du lait, altitude) ont laissé des traces dans le génome.",
 "Les enjeux actuels (résistance aux antibiotiques, biodiversité, évolution des pathogènes) illustrent l'importance de penser l'évolution à l'échelle des populations."
], [
 q("Combien de nucléotides forme un codon ?", ["Deux", "Trois", "Quatre", "Cinq"], 1, "Un codon est un triplet de nucléotides de l'ARN messager, codant pour un acide aminé ou un signal d'arrêt."),
 q("Quel est le rôle de la transcription ?", ["Copier l'ADN en ARN messager", "Synthétiser une protéine", "Répliquer l'ADN", "Détruire l'ARN"], 0, "La transcription produit un ARN messager complémentaire d'un gène ; la traduction le décode en protéine."),
 q("Que prédit l'équilibre de Hardy–Weinberg ?", ["Les fréquences génotypiques à partir des fréquences alléliques", "La vitesse d'une réaction", "Le nombre de mutations", "L'âge d'un fossile"], 0, "Sous des hypothèses idéales, les fréquences génotypiques restent p², 2pq, q² de génération en génération."),
 q("Quel facteur n'est pas une cause d'évolution ?", ["La sélection", "La dérive", "La migration", "L'équilibre de Hardy–Weinberg"], 3, "Hardy–Weinberg décrit une situation sans évolution ; les trois autres sont des facteurs de changement des fréquences."),
 q("Quel est un exemple de barrière reproductive post-zygotique ?", ["L'isolement géographique", "L'hybride stérile", "La parade nuptiale différente", "La saison de reproduction différente"], 1, "Un hybride stérile (comme la mule) est une barrière post-zygotique : la fécondation a lieu mais la descendance est infertile."),
 t("Qu'est-ce que la dégénérescence du code génétique ?", "Plusieurs codons peuvent coder le même acide aminé.", "Cette redondance protège partiellement contre les mutations : une substitution sur la troisième base d'un codon est souvent silencieuse."),
 t("Comment la recombinaison crée-t-elle de la variabilité ?", "En produisant de nouvelles associations d'allèles lors de la méiose.", "Le crossing-over et l'orientation indépendante des chromosomes homologues produisent des gamètes portant des combinaisons inédites, sans créer de nouveaux allèles."),
 t("Comment mesure-t-on l'évolution d'une population ?", "En suivant les variations des fréquences alléliques au fil des générations.", "L'évolution est un changement de la composition génétique d'une population : les outils statistiques (Hardy–Weinberg, tests) permettent de la détecter.")
])),

F.append(f(["Terminale"], "SVT", "Chapitre : Le fonctionnement du système nerveux et la communication cellulaire", SSVT2, [
 "Le programme de terminale étudie la communication nerveuse et hormonale comme modes de coordination des organismes.",
 "Le neurone est une cellule spécialisée dans la transmission du message nerveux : il possède un corps cellulaire, des dendrites et un axone terminé par des synapses.",
 "Au repos, la membrane du neurone est polarisée : il existe une différence de potentiel (environ –70 mV) entre l'intérieur et l'extérieur, entretenue par la pompe sodium-potassium.",
 "Un potentiel d'action est une dépolarisation rapide et transitoire, de même amplitude quel que soit le stimulus (loi du tout ou rien), qui se propage le long de l'axone.",
 "La transmission entre neurones a lieu à la synapse : la libération de neurotransmetteurs dans la fente synaptique provoque une modification du potentiel du neurone postsynaptique.",
 "Les neuromédiateurs (acétylcholine, dopamine, GABA) peuvent être excitateurs ou inhibiteurs ; leur action dépend du récepteur postsynaptique.",
 "Le système nerveux central (encéphale et moelle épinière) traite l'information ; le système nerveux périphérique assure la connexion avec les organes.",
 "Un réflexe est une réponse rapide et stéréotypée à un stimulus, intégrée au niveau de la moelle épinière : l'arc réflexe comprend récepteur, voie afférente, centre, voie efférente et effecteur.",
 "Le système endocrinien utilise des hormones transportées par le sang : leur action est plus lente mais plus durable que celle du message nerveux.",
 "Les drogues et médicaments agissent souvent sur la transmission synaptique : comprendre ces mécanismes est un enjeu de santé publique au programme."
], [
 q("Quel est le potentiel de repos d'un neurone ?", ["0 mV", "+30 mV", "Environ –70 mV", "–120 mV"], 2, "Au repos, l'intérieur du neurone est d'environ 70 mV plus négatif que l'extérieur."),
 q("Quelle est la loi du tout ou rien ?", ["L'amplitude du potentiel d'action est indépendante de l'intensité du stimulus", "Un neurone répond uniquement aux gros stimuli", "La synapse transmet tout le temps", "Le message s'atténue le long de l'axone"], 0, "Le potentiel d'action a toujours la même amplitude ; l'intensité du message est codée par la fréquence des potentiels d'action."),
 q("Quelle cellule transmet le message nerveux ?", ["Le neurone", "L'hématie", "L'ostéocyte", "L'adipocyte"], 0, "Le neurone est la cellule du tissu nerveux spécialisée dans la réception, la conduction et la transmission du message."),
 q("Quel ion est principalement impliqué dans la dépolarisation ?", ["Le potassium", "Le sodium", "Le calcium", "Le chlorure"], 1, "L'entrée d'ions Na⁺ dans la cellule provoque la dépolarisation ; la sortie de K⁺ participe à la repolarisation."),
 q("Quel est le rôle d'un neurotransmetteur ?", ["Transmettre le signal à travers la synapse", "Répliquer l'ADN", "Digérer les protéines", "Porter l'oxygène"], 0, "Libéré par le neurone présynaptique, il se fixe sur des récepteurs du neurone postsynaptique et modifie son potentiel."),
 t("Quelle différence oppose message nerveux et message hormonal ?", "Le message nerveux est rapide et précis ; le message hormonal est plus lent, diffus et durable.", "Le système nerveux agit en millisecondes sur des cibles précises, alors que les hormones circulent dans le sang et agissent sur des organes cibles éloignés."),
 t("Comment se propage un potentiel d'action ?", "Par l'ouverture successive de canaux ioniques le long de l'axone, sans atténuation.", "La dépolarisation d'une zone déclenche celle de la zone voisine : le signal se régénère à chaque segment, ce qui explique l'absence d'atténuation."),
 t("Pourquoi l'arc réflexe est-il rapide ?", "Parce que l'intégration se fait au niveau de la moelle et suit un trajet court, sans passage par le cortex.", "Le réflexe évite le traitement conscient : la réponse est déclenchée avant même la perception de la douleur.")
])),

# ---------------- NSI ----------------
F.append(f(["1re"], "NSI", "Chapitre : Représentation binaire des données – entiers, flottants et caractères", SNSI1, [
 "Le programme NSI de première s'articule autour de huit rubriques, dont « Représentation des données : types et valeurs de base » et les algorithmes classiques.",
 "L'unité minimale d'information est le bit, qui prend deux valeurs (0 ou 1) ; un octet est un groupe de 8 bits.",
 "Un entier positif s'écrit en base 2 ; les bases 2, 10 et 16 sont privilégiées en informatique. Un entier relatif peut être codé en complément à deux.",
 "La taille courante des entiers est de 8, 16, 32 ou 64 bits ; Python utilise des entiers de taille arbitraire, limités seulement par la mémoire.",
 "Les nombres réels sont représentés de façon approchée par des flottants (norme IEEE 754) : 0,2 + 0,1 n'est pas exactement 0,3, ce qui interdit les tests d'égalité directe.",
 "Les caractères sont codés par des tables : ASCII (7 bits), puis Unicode (UTF-8, UTF-16) qui couvre toutes les écritures, dont l'alphabet arabe et les emoji.",
 "Une image est une matrice de pixels ; chaque pixel est codé par trois composantes de couleur (RVB) sur 8 bits chacune, éventuellement avec une composante d'opacité (alpha).",
 "Le codage d'un son repose sur l'échantillonnage (fréquence d'échantillonnage en Hz) et la quantification (nombre de bits par échantillon) : la fidélité dépend de ces paramètres.",
 "La compression (avec ou sans perte) réduit la taille des fichiers : PNG et ZIP sont sans perte, JPEG et MP3 sont avec perte.",
 "Le programme exige de savoir convertir entre bases, manipuler des octets et expliquer pourquoi une représentation binaire est un choix de modélisation."
], [
 q("Quelle est la représentation binaire de l'entier 5 sur 8 bits ?", ["00000101", "00000110", "01010000", "10100000"], 0, "5 = 4 + 1, soit 00000101 en base 2 sur 8 bits."),
 q("Pourquoi ne faut-il pas comparer deux flottants avec == ?", ["Leur représentation binaire est approchée et introduit des erreurs d'arrondi", "Parce que Python interdit ce test", "Parce que les flottants sont des chaînes", "Parce que 0,1 n'existe pas"], 0, "Le programme NSI signale explicitement que 0,2 + 0,1 ≠ 0,3 ; on compare plutôt avec une tolérance."),
 q("Combien de bits contient un octet ?", ["4", "7", "8", "16"], 2, "Un octet (byte) est un groupe de 8 bits, soit 256 valeurs possibles."),
 q("Quel codage couvre toutes les écritures du monde ?", ["ASCII", "Unicode", "Binaire", "Morse"], 1, "Unicode (notamment UTF-8) attribue un code à chaque caractère de toutes les langues, y compris l'arabe."),
 q("Quel format de compression est sans perte ?", ["JPEG", "MP3", "PNG", "MPEG"], 2, "PNG est un format sans perte ; JPEG et MP3 sacrifient une partie de l'information pour réduire la taille."),
 t("Comment coder un entier relatif en complément à deux ?", "En prenant le complément à 1 du nombre positif puis en ajoutant 1.", "Sur n bits, on retourne tous les bits puis on ajoute 1 : le résultat représente l'opposé, et l'addition binaire fonctionne alors normalement."),
 t("Pourquoi 0,2 + 0,1 donne-t-il un résultat imprécis ?", "Parce que ces nombres n'ont pas de représentation binaire finie et sont arrondis.", "Le format flottant IEEE 754 dispose d'une précision limitée (53 bits pour un double) : certains décimales ne peuvent être représentées exactement, d'où une erreur d'arrondi."),
 t("Comment représenter une couleur en RVB ?", "Par trois entiers entre 0 et 255 pour le rouge, le vert et le bleu.", "Chaque composante occupe un octet ; le triplet (255, 0, 0) donne le rouge pur, (255, 255, 255) le blanc et (0, 0, 0) le noir.")
])),

F.append(f(["1re"], "NSI", "Chapitre : Algorithmique – tri, recherche et complexité", SNSI1, [
 "La rubrique algorithmique du programme NSI de première étudie des algorithmes classiques et évalue leur coût sur des données nombreuses.",
 "Un algorithme est une suite finie d'instructions permettant de résoudre un problème ; il est décrit en pseudo-code ou implémenté en Python.",
 "Le tri par insertion construit progressivement un préfixe trié en insérant chaque élément à sa place ; son invariant de boucle garantit que le préfixe reste ordonné.",
 "Le tri par sélection choisit à chaque étape le plus petit élément de la partie non triée et l'échange avec le premier élément de cette partie.",
 "Les deux tris ont un coût quadratique dans le pire cas : O(n²) comparaisons, où n est le nombre d'éléments.",
 "Le tri fusion (diviser pour régner) et le tri rapide ont un coût moyen de O(n log n), bien plus efficace sur de grands tableaux.",
 "La recherche linéaire parcourt le tableau jusqu'à trouver la valeur : son coût est O(n) dans le pire cas.",
 "La recherche dichotomique s'applique à un tableau trié : elle compare la valeur cherchée à l'élément médian et divise l'intervalle par deux à chaque itération ; son coût est O(log n).",
 "L'invariant de boucle est une propriété vraie avant chaque itération : c'est l'outil principal pour démontrer la correction d'un algorithme itératif.",
 "Savoir estimer une complexité permet de choisir l'algorithme adapté à la taille des données, compétence centrale du programme."
], [
 q("Quel est le coût dans le pire cas du tri par insertion ?", ["Linéaire", "Quadratique", "Logarithmique", "Constant"], 1, "Le tri par insertion et le tri par sélection ont un coût en O(n²) dans le pire cas."),
 q("Quelle condition est indispensable pour une recherche dichotomique ?", ["Le tableau doit être préalablement trié", "Le tableau doit être vide", "Les valeurs doivent être toutes égales", "Le tableau doit être trié décroissant uniquement"], 0, "La dichotomie suppose un ordre : elle compare à l'élément médian et réduit l'intervalle de moitié."),
 q("Quelle est la complexité de la recherche dichotomique ?", ["O(n)", "O(n²)", "O(log n)", "O(1)"], 2, "À chaque étape, l'intervalle est divisé par deux : le nombre d'étapes est proportionnel à log₂(n)."),
 q("Quel tri utilise la stratégie « diviser pour régner » ?", ["Le tri par insertion", "Le tri fusion", "Le tri par sélection", "Le tri à bulles"], 1, "Le tri fusion découpe le tableau, trie les moitiés puis les fusionne : coût O(n log n)."),
 q("Qu'est-ce qu'un invariant de boucle ?", ["Une propriété vraie avant chaque itération", "Une variable qui ne change jamais", "Un test d'arrêt", "Une fonction récursive"], 0, "L'invariant, vrai à l'initialisation et préservé par l'itération, permet de démontrer la correction de l'algorithme."),
 t("Comment fonctionne le tri par insertion ?", "On construit un préfixe trié en déplaçant chaque nouvel élément à sa place.", "Pour chaque élément, on le compare aux éléments du préfixe de droite à gauche et on le décale jusqu'à trouver sa position : le préfixe reste trié à chaque étape."),
 t("Pourquoi la dichotomie est-elle plus efficace que la recherche linéaire ?", "Parce qu'elle divise l'espace de recherche par deux à chaque étape au lieu d'examiner chaque élément.", "Pour un tableau d'un million d'éléments, la dichotomie ne demande qu'une vingtaine de comparaisons contre un million dans le pire cas."),
 t("Comment estimer la complexité d'un algorithme ?", "En comptant le nombre d'opérations principales en fonction de la taille n des données et en retenant l'ordre de grandeur.", "On utilise les notations O(1), O(log n), O(n), O(n log n), O(n²) pour comparer l'efficacité des algorithmes indépendamment de la machine.")
])),

F.append(f(["Terminale"], "NSI", "Chapitre : Structures de données – listes, piles, files, arbres et graphes", SNSI2, [
 "En terminale, la rubrique « Structures de données » distingue l'interface (services offerts) de l'implémentation (manière dont ils sont réalisés).",
 "Les listes, piles (LIFO : last in, first out) et files (FIFO : first in, first out) sont des structures linéaires ; le dictionnaire associe une clé à une valeur.",
 "Une pile est utilisée pour la gestion des appels de fonctions (pile d'exécution) et l'annulation (undo) ; une file pour la gestion des tâches ou des messages.",
 "Un arbre binaire est une structure hiérarchique avec une racine, des nœuds, des feuilles et au plus deux sous-arbres par nœud.",
 "Un arbre binaire de recherche (ABR) vérifie que les valeurs du sous-arbre gauche sont inférieures à la racine et celles du sous-arbre droit supérieures : la recherche coûte O(log n) si l'arbre est équilibré.",
 "Un graphe est une structure relationnelle modélisée par des sommets et des arêtes (non orientées) ou des arcs (orientés).",
 "Un graphe se représente par une matrice d'adjacence (case i,j = 1 s'il existe une arête) ou par une liste de successeurs, plus économe en mémoire si le graphe est creux.",
 "Les parcours de graphe en largeur (BFS) et en profondeur (DFS) permettent de visiter tous les sommets ; le BFS donne les plus courts chemins dans un graphe non pondéré.",
 "L'interface décrit les opérations disponibles (empiler, dépiler, insérer, supprimer, rechercher) ; l'implémentation peut être un tableau, une liste chaînée ou un arbre.",
 "Le programme exige de justifier le choix d'une structure en fonction des opérations les plus fréquentes et de leur coût."
], [
 q("Quel principe régit une file (queue) ?", ["LIFO", "FIFO", "LIFO et FIFO", "Aucun des deux"], 1, "Une file fonctionne en FIFO (first in, first out) ; une pile fonctionne en LIFO."),
 q("Quelle structure associe une clé à une valeur ?", ["La pile", "Le dictionnaire", "La file", "L'arbre binaire"], 1, "Le dictionnaire (ou table de hachage) permet un accès rapide à une valeur à partir de sa clé."),
 q("Quelle est la propriété d'un arbre binaire de recherche ?", ["Tous les nœuds sont égaux", "À gauche les valeurs plus petites, à droite les plus grandes", "Il n'a qu'une feuille", "Il est toujours équilibré"], 1, "La propriété ABR permet une recherche efficace par comparaison avec la racine à chaque niveau."),
 q("Quel parcours donne le plus court chemin dans un graphe non pondéré ?", ["DFS", "BFS", "Le tri fusion", "La dichotomie"], 1, "Le parcours en largeur (BFS) explore les sommets par distance croissante depuis la source."),
 q("Quel est l'intérêt d'une liste de successeurs ?", ["Elle est plus économe pour un graphe creux", "Elle est plus rapide pour un graphe dense", "Elle n'utilise pas de mémoire", "Elle interdit les cycles"], 0, "Pour un graphe avec peu d'arêtes, stocker uniquement les voisins de chaque sommet économise de la place par rapport à la matrice."),
 t("Quelle différence y a-t-il entre interface et implémentation ?", "L'interface décrit les opérations disponibles ; l'implémentation décrit comment elles sont réalisées.", "Une même interface (empiler, dépiler) peut être réalisée par un tableau ou une liste chaînée, avec des coûts différents."),
 t("Comment représenter un graphe ?", "Par une matrice d'adjacence ou une liste de successeurs.", "La matrice rend la recherche d'une arête rapide (O(1)) mais occupe O(n²) mémoire ; la liste est plus compacte pour les graphes creux."),
 t("À quoi sert la pile d'exécution ?", "À mémoriser les appels de fonctions en cours et leurs variables locales.", "Chaque appel de fonction crée un cadre empilé ; le retour dépile le cadre et restaure le contexte de l'appelant, ce qui rend la récursion possible.")
])),

F.append(f(["Terminale"], "NSI", "Chapitre : Réseaux, sécurisation et protection des données", SNSI2, [
 "Le programme de terminale NSI comporte la rubrique « Sécurisation des communications » et aborde le fonctionnement des réseaux informatiques.",
 "Un réseau informatique interconnecte des équipements pour partager des ressources ; le modèle OSI et le modèle TCP/IP décrivent les couches de communication.",
 "Le protocole TCP/IP structure l'Internet : IP gère l'adressage et le routage des paquets, TCP garantit la livraison fiable et ordonnée des données.",
 "Une adresse IPv4 est codée sur 32 bits (4 octets) ; l'épuisement des adresses a conduit à l'IPv6 (128 bits).",
 "Le chiffrement symétrique utilise une seule clé partagée pour chiffrer et déchiffrer : il est rapide mais pose le problème de l'échange de la clé.",
 "Le chiffrement asymétrique utilise une paire clé publique / clé privée : ce que l'on chiffre avec la clé publique ne peut être déchiffré que par la clé privée correspondante.",
 "HTTPS combine les deux approches : un protocole asymétrique (TLS) authentifie le serveur et échange une clé symétrique, puis les données sont chiffrées symétriquement pour la performance.",
 "Une fonction de hachage (SHA-256) produit une empreinte de taille fixe d'un document : elle permet de vérifier son intégrité, mais n'est pas réversible.",
 "Les menaces courantes sont l'usurpation d'identité (phishing), l'injection SQL, les logiciels malveillants et les attaques par déni de service.",
 "Les bonnes pratiques (mots de passe longs, double authentification, mise à jour, chiffrement des sauvegardes) font partie des savoirs exigés par le programme."
], [
 q("Quel protocole garantit une livraison fiable des données sur Internet ?", ["IP", "TCP", "HTTP", "SMTP"], 1, "TCP (Transmission Control Protocol) établit une connexion, numérote les paquets et demande les retransmissions nécessaires."),
 q("Sur combien de bits est codée une adresse IPv6 ?", ["32", "64", "128", "256"], 2, "L'IPv6 utilise 128 bits, soit un espace d'adresses considérablement plus vaste que l'IPv4 (32 bits)."),
 q("Quelle est la différence entre chiffrement symétrique et asymétrique ?", ["Le symétrique utilise une clé partagée, l'asymétrique une paire de clés", "Le symétrique est plus lent", "L'asymétrique n'existe que pour les images", "Il n'y a aucune différence"], 0, "Le chiffrement symétrique utilise une clé unique ; l'asymétrique recourt à une clé publique et une clé privée."),
 q("Quel protocole est utilisé pour sécuriser les échanges web (HTTPS) ?", ["TLS", "FTP", "DNS", "DHCP"], 0, "HTTPS est HTTP sur TLS (Transport Layer Security), qui assure authentification, confidentialité et intégrité."),
 q("Quelle propriété une fonction de hachage doit-elle avoir ?", ["Être réversible", "Produire une empreinte de taille fixe et être résistante aux collisions", "Être lente", "Conserver le document"], 1, "Une fonction de hachage est déterministe, non réversible et produit une empreinte de taille fixe ; SHA-256 est utilisée en cryptographie."),
 t("Comment HTTPS combine-t-il les deux types de chiffrement ?", "Le chiffrement asymétrique authentifie le serveur et échange une clé symétrique, puis les données sont chiffrées symétriquement.", "L'asymétrique résout le problème de l'échange de clé mais est coûteux ; le symétrique est rapide mais suppose une clé partagée : TLS tire parti des deux."),
 t("Quel est le rôle du protocole IP ?", "Adresser les machines et router les paquets de données.", "IP découpe les données en paquets, ajoute les adresses source et destination, et les achemine à travers les réseaux, sans garantir la livraison."),
 t("Comment se protéger contre le phishing ?", "En vérifiant l'expéditeur et l'adresse du site, en ne communiquant jamais de mots de passe et en activant la double authentification.", "Le phishing exploite la confiance : une apparence trompante pousse à saisir des identifiants sur un site frauduleux.")
])),

# ---------------- SI ----------------
F.append(f(["1re"], "SI", "Chapitre : Chaînes fonctionnelles et modélisation des systèmes", SSI1, [
 "La spécialité sciences de l'ingénieur (SI) étudie les systèmes techniques en reliant les flux d'énergie, d'information et de matière.",
 "Une chaîne fonctionnelle se décompose en trois fonctions : alimenter, transformer et transmettre (ou distribuer) ; un système est décrit par ses entrées, ses sorties et ses perturbations.",
 "Le schéma fonctionnel est un outil de modélisation : il représente les liaisons entre les éléments d'un système sans entrer dans leur réalisation technique.",
 "Un capteur convertit une grandeur physique (température, position, lumière) en signal, généralement électrique ; un actionneur convertit un signal en action mécanique ou thermique.",
 "La démarche d'ingénieur consiste à analyser un besoin, élaborer un cahier des charges, modéliser, concevoir, réaliser et valider une solution.",
 "Le cahier des charges fonctionnel (CdCF) explicite les fonctions assurées par le produit, les contraintes et les critères de satisfaction.",
 "Les systèmes sont étudiés sous trois aspects complémentaires : la structure (les éléments), le comportement (les relations) et la fonction (le service rendu).",
 "Un système automatisé associe une partie « commande » (traitement de l'information) et une partie « puissance » (action sur la matière ou l'énergie).",
 "La modélisation fait appel à des schémas (blocs fonctionnels, graphes, diagrammes) et à des grandeurs caractéristiques (rendement, temps de réponse, précision).",
 "L'analyse d'un système existant (démarche inverse) permet d'identifier les fonctions et de proposer des améliorations."
], [
 q("Quelle fonction assure un capteur dans une chaîne d'information ?", ["Il convertit un signal électrique en action", "Il convertit une grandeur physique en signal", "Il stocke l'énergie", "Il dissipe la chaleur"], 1, "Le capteur transforme une grandeur physique en signal mesurable, généralement électrique."),
 q("Quelles sont les trois grandes fonctions d'une chaîne fonctionnelle ?", ["Alimenter, transformer, transmettre", "Voir, entendre, toucher", "Concevoir, fabriquer, vendre", "Entrer, sortir, stocker"], 0, "Cette modélisation est commune aux systèmes mécaniques, électriques et thermiques étudiés en SI."),
 q("Que désigne un cahier des charges fonctionnel ?", ["Un plan de fabrication", "L'expression du besoin, des fonctions et des contraintes", "Une facture", "Un rapport de stage"], 1, "Le CdCF définit ce que le système doit faire, sans imposer a priori la solution technique."),
 q("Quelle est la différence entre un capteur et un actionneur ?", ["Le capteur reçoit une grandeur physique, l'actionneur produit une action", "Ils sont identiques", "L'actionneur mesure, le capteur agit", "Le capteur est toujours électrique"], 0, "Le capteur transforme une grandeur physique en signal ; l'actionneur transforme un signal en action sur le système."),
 q("Que représente une perturbation dans un système ?", ["Une grandeur extérieure non désirée qui modifie la sortie", "La sortie attendue", "L'alimentation", "Le schéma"], 0, "La perturbation est une sollicitation non maîtrisée (charge, température, bruit) dont le système doit compenser les effets."),
 t("Quel est l'intérêt du schéma fonctionnel ?", "Il décrit les fonctions et leurs liaisons sans se préoccuper de la réalisation technique.", "Il permet de raisonner sur le service rendu par le système et de repérer les interfaces avant de choisir les composants."),
 t("Comment un système automatisé se divise-t-il ?", "En une partie commande (information) et une partie puissance (énergie et matière).", "La commande traite les consignes et les mesures ; la puissance fournit l'effort et assure la transformation."),
 t("Quelles sont les étapes de la démarche d'ingénieur ?", "Analyser le besoin, modéliser, concevoir, réaliser, valider.", "Cette démarche itérative s'appuie sur des essais et des critères de validation définis dans le cahier des charges.")
])),

F.append(f(["1re"], "SI", "Chapitre : Énergie mécanique, transmissions et cinématique", SSI1, [
 "L'étude des systèmes mécaniques en spécialité SI repose sur les notions de force, de couple, de travail et d'énergie.",
 "L'énergie cinétique d'un corps de masse m animé d'une vitesse v vaut E_c = ½·m·v² ; l'énergie potentielle de pesanteur vaut E_pp = m·g·h.",
 "Le principe de conservation de l'énergie mécanique s'applique aux systèmes sans dissipation : E_c + E_pp reste constant en l'absence de frottements.",
 "Le travail d'une force est le produit de son intensité par le déplacement de son point d'application dans sa direction : W = F·d·cos α.",
 "Une transmission (engrenage, courroie, chaîne) modifie la vitesse et le couple : le rapport de transmission est le quotient des nombres de dents ou des rayons.",
 "Dans un réducteur, la vitesse de sortie diminue tandis que le couple augmente ; dans un multiplicateur, c'est l'inverse.",
 "Le rendement d'une transmission est le rapport entre la puissance reçue en sortie et la puissance fournie en entrée : il est inférieur à 1 à cause des pertes par frottement.",
 "La cinématique décrit les mouvements : translation, rotation autour d'un axe, mouvement hélicoïdal ; chaque liaison mécanique autorise certains mouvements et en interdit d'autres.",
 "Un mécanisme est un ensemble de solides reliés par des liaisons : le nombre de degrés de liberté se détermine par l'analyse cinématique.",
 "Les applications (vérin, moteur, réducteur, système de lever) exigent de relier les grandeurs cinématiques et énergétiques pour dimensionner les composants."
], [
 q("Quelle est l'expression de l'énergie cinétique ?", ["m·g·h", "½·m·v²", "F·d", "m·v"], 1, "L'énergie cinétique vaut ½ m v² ; m g h est l'énergie potentielle de pesanteur."),
 q("Que se passe-t-il dans un réducteur d'engrenages ?", ["La vitesse diminue et le couple augmente", "La vitesse augmente et le couple diminue", "Les deux augmentent", "Les deux diminuent"], 0, "Avec un rapport i = N₁/N₂ > 1, la vitesse est divisée par i et le couple multiplié par i, à rendement égal."),
 q("Quelle est l'unité d'un couple ?", ["Le newton", "Le newton-mètre", "Le watt", "Le joule"], 1, "Un couple (moment de force) s'exprime en N·m : c'est le produit d'une force par un bras de levier."),
 q("Que devient l'énergie mécanique avec des frottements ?", ["Elle est conservée", "Elle est convertie en chaleur", "Elle augmente", "Elle devient nulle"], 1, "Les frottements dissipent une partie de l'énergie mécanique sous forme thermique, ce qui réduit le rendement."),
 q("Qu'est-ce qu'une liaison mécanique ?", ["Un contact entre deux solides qui autorise certains mouvements", "Un moteur", "Une source d'énergie", "Un capteur"], 0, "Une liaison (pivot, glissière, rotule) impose des contraintes et définit les degrés de liberté relatifs de deux solides."),
 t("Comment calculer le rapport de transmission d'un engrenage ?", "Par le quotient du nombre de dents (ou des rayons) des deux roues.", "Le rapport relie les vitesses de rotation et les couples ; il faut préciser la convention utilisée (i = N Entrée/N Sortie ou l'inverse)."),
 t("Quel est l'intérêt d'un réducteur ?", "Il permet d'obtenir un couple important à faible vitesse à partir d'un moteur rapide.", "Les moteurs tournant vite mais développant un faible couple, la réduction adapte la puissance à la charge à entraîner."),
 t("Comment identifier les degrés de liberté d'un mécanisme ?", "En analysant les liaisons entre solides et les mouvements qu'elles autorisent.", "Chaque liaison supprime certaines translations ou rotations ; le nombre de paramètres indépendants restants donne le nombre de degrés de liberté.")
])),

F.append(f(["Terminale"], "SI", "Chapitre : Commande des systèmes et boucles de régulation", SSI2, [
 "En terminale, la spécialité SI approfondit la modélisation et la commande des systèmes automatisés.",
 "Une boucle ouverte agit sans tenir compte du résultat : la commande est déterminée uniquement par la consigne, sans mesure de la sortie.",
 "Une boucle fermée compare la sortie mesurée à la consigne et corrige l'écart (erreur) par un régulateur : c'est la rétroaction (feedback).",
 "Les éléments d'une boucle fermée sont : le comparateur, le régulateur, l'actionneur, le procédé et le capteur de mesure.",
 "Le régulateur PID (proportionnel, intégral, dérivé) combine trois actions : correction proportionnelle à l'erreur, élimination de l'écart statique et anticipation des variations.",
 "Un système asservi doit satisfaire des critères de performance : rapidité (temps de réponse), précision (écart statique) et stabilité (absence d'oscillations divergentes).",
 "La fonction de transfert, en régime linéaire, relie la sortie à l'entrée dans le domaine de Laplace : elle permet d'analyser la stabilité et la réponse du système.",
 "Les capteurs et actionneurs introduisent des limitations : résolution, temps de réponse, saturation et bruit de mesure.",
 "La commande numérique met en œuvre ces principes dans un automate ou un microcontrôleur ; la période d'échantillonnage influence la stabilité.",
 "Les applications (thermostat, régulateur de vitesse, asservissement de position) illustrent l'importance de la boucle fermée dans l'industrie."
], [
 q("Quelle est la différence entre boucle ouverte et boucle fermée ?", ["La boucle fermée mesure la sortie et corrige l'écart", "La boucle ouverte est toujours plus précise", "La boucle fermée n'a pas de capteur", "Il n'y a aucune différence"], 0, "La boucle fermée utilise une rétroaction : la mesure de la sortie est comparée à la consigne pour corriger l'action."),
 q("Que fait l'action intégrale d'un régulateur PID ?", ["Elle élimine l'écart statique", "Elle anticipe les variations", "Elle augmente le bruit", "Elle réduit le temps de calcul"], 0, "L'action intégrale accumule l'erreur : elle annule l'écart statique persistant, au prix d'un risque d'oscillation."),
 q("Quel élément mesure la sortie d'un système asservi ?", ["Le comparateur", "Le capteur", "L'actionneur", "La consigne"], 1, "Le capteur fournit la mesure de la grandeur de sortie, qui est renvoyée au comparateur."),
 q("Quel critère de performance concerne la précision ?", ["Le temps de réponse", "L'écart statique", "La stabilité", "La saturation"], 1, "L'écart statique mesure la différence persistante entre la consigne et la valeur atteinte en régime permanent."),
 q("Comment appelle-t-on le signal qui représente l'écart entre consigne et mesure ?", ["L'erreur", "La consigne", "La perturbation", "Le gain"], 0, "L'erreur (ou écart) est l'entrée du régulateur : sa valeur et son signe déterminent la correction à appliquer."),
 t("Pourquoi une boucle fermée est-elle plus robuste qu'une boucle ouverte ?", "Parce qu'elle compense les perturbations en comparant en permanence la sortie à la consigne.", "Si une charge ou une perturbation modifie la sortie, l'écart détecté par le comparateur déclenche une correction : le système s'auto-ajuste."),
 t("Quel est le rôle de l'action dérivée dans un PID ?", "Elle anticipe les variations de l'erreur et améliore la stabilité.", "La dérivée de l'erreur fournit une information sur sa vitesse de variation, ce qui permet d'amortir les oscillations."),
 t("Comment la période d'échantillonnage influence-t-elle la commande numérique ?", "Une période trop longue dégrade la précision et peut déstabiliser la boucle.", "Le régulateur numérique ne dispose d'informations qu'à chaque échantillon : le choix de la période est un compromis entre charge de calcul et dynamique du système.")
])),

F.append(f(["1re"], "Biologie-écologie", "Chapitre : ADN, gènes et hérédité – les bases moléculaires", SBIO, [
 "La spécialité biologie-écologie approfondit les mécanismes du vivant et les relations entre organismes et environnement.",
 "L'ADN est une molécule à double hélice décrite par Watson et Crick en 1953 ; les gènes sont des segments d'ADN qui portent l'information pour la synthèse de protéines.",
 "La réplication semi-conservatrice de l'ADN précède la division cellulaire ; la mitose distribue deux copies identiques du génome aux cellules filles.",
 "La loi de Mendel sur la ségrégation des allèles explique la transmission des caractères héréditaires : les allèles dominants et récessifs se répartissent selon des proportions prévisibles.",
 "La photosynthèse se déroule dans les chloroplastes : elle utilise l'eau et le dioxyde de carbone pour produire des glucides et du dioxygène (6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂).",
 "L'eau et les sels minéraux sont absorbés par les racines et transportés dans le xylème ; les produits de la photosynthèse circulent dans le phloème.",
 "La respiration cellulaire, inverse de la photosynthèse, libère l'énergie chimique des glucides dans les mitochondries : elle a lieu chez les plantes comme chez les animaux.",
 "Les végétaux réagissent aux stimuli lumineux et gravitationnels grâce aux hormones végétales (auxines, gibbérellines), qui contrôlent la croissance.",
 "Le programme de biologie-écologie associe ces bases à une approche de l'agronomie et du fonctionnement des agrosystèmes.",
 "L'étude expérimentale (microscopie, dosages, suivi de croissance) accompagne l'acquisition des notions et développe la démarche scientifique."
], [
 q("Qui a décrit la structure en double hélice de l'ADN en 1953 ?", ["Watson et Crick", "Mendel et Darwin", "Pasteur et Koch", "Lamarck et Buffon"], 0, "Watson et Crick publient le modèle de la double hélice en 1953 à partir des données de Rosalind Franklin."),
 q("Dans quel organite a lieu la photosynthèse ?", ["La mitochondrie", "Le chloroplaste", "Le noyau", "Le ribosome"], 1, "La photosynthèse se déroule dans les chloroplastes ; la respiration cellulaire a lieu dans les mitochondries."),
 q("Que transporte le xylème ?", ["Les substances organiques", "L'eau et les sels minéraux", "Les hormones", "Le dioxygène"], 1, "Le xylème assure la montée de la sève brute des racines vers les organes aériens ; le phloème transporte la sève élaborée."),
 q("Quel est le rôle de la réplication semi-conservatrice ?", ["Produire deux cellules différentes", "Copier l'ADN avant la division", "Détruire l'ADN endommagé", "Synthétiser des protéines"], 1, "Chaque molécule fille contient un brin ancien et un brin neuf, ce qui assure la fidélité de l'hérédité."),
 q("Qu'appelle-t-on allèles ?", ["Des chromosomes entiers", "Des versions différentes d'un même gène", "Des protéines", "Des cellules"], 1, "Les allèles sont les formes alternatives d'un gène, présentes en deux copies chez un individu diploïde."),
 t("Qu'est-ce que la réplication semi-conservatrice ?", "Chaque molécule d'ADN fille contient un brin ancien et un brin nouvellement synthétisé.", "Le modèle de Meselson et Stahl (1958) l'a confirmé expérimentalement : c'est la base de la fidélité de la transmission génétique."),
 t("Quelle est la différence entre xylème et phloème ?", "Le xylème transporte l'eau et les sels minéraux ; le phloème transporte les substances organiques.", "Ces deux tissus conducteurs forment les vaisseaux des plantes et assurent la circulation de la sève brute et de la sève élaborée."),
 t("Comment les hormones végétales contrôlent-elles la croissance ?", "En régulant l'élongation cellulaire en réponse à la lumière et à la gravité.", "Les auxines, notamment, s'accumulent du côté de l'ombre et provoquent une croissance inégale : la tige se courbe vers la lumière (phototropisme).")
])),

F.append(f(["Terminale"], "Biologie-écologie", "Chapitre : Biodiversité, évolution et écologie des agrosystèmes", SBIO, [
 "Le programme de biologie-écologie de terminale articule évolution, biodiversité et fonctionnement des écosystèmes et des agrosystèmes.",
 "L'évolution est le changement des fréquences alléliques dans les populations au fil des générations ; la sélection naturelle et la dérive en sont les moteurs.",
 "La biodiversité se décline en trois niveaux : diversité génétique, diversité spécifique et diversité des écosystèmes (Rio, 1992).",
 "Un écosystème associe une communauté d'êtres vivants et son environnement physicochimique, reliés par des flux d'énergie et de matière.",
 "Les relations interspécifiques comprennent la prédation, la compétition, le mutualisme, le parasitisme et la symbiose ; elles structurent les réseaux trophiques.",
 "Les chaînes alimentaires se hiérarchisent en niveaux trophiques (producteurs, consommateurs, décomposeurs), avec une perte d'énergie à chaque transfert (rendement d'environ 10 %).",
 "Un agrosystème est un écosystème simplifié et artificialisé, où l'homme sélectionne les espèces cultivées et contrôle les facteurs de production.",
 "La monoculture réduit la diversité biologique et peut fragiliser le système : les stratégies de lutte intégrée et d'agroécologie visent à restaurer la résilience.",
 "L'érosion de la biodiversité contemporaine est liée à la destruction des habitats, à la surexploitation, aux pollutions et aux changements climatiques.",
 "Les politiques de conservation (aires protégées, corridors écologiques, restauration) s'appuient sur des indicateurs scientifiques et une évaluation des enjeux."
], [
 q("Quel mécanisme Darwin propose-t-il pour expliquer l'évolution ?", ["La sélection naturelle", "La génération spontanée", "Le lamarckisme", "Le catastrophisme"], 0, "Darwin propose la sélection naturelle : la survie et la reproduction différentielles des individus selon leurs variations."),
 q("Quels sont les trois niveaux de la biodiversité ?", ["Génétique, espèces, écosystèmes", "Cellule, tissu, organe", "Individu, famille, espèce", "Forêt, champ, ville"], 0, "La Convention des Nations unies sur la diversité biologique (Rio, 1992) retient ces trois niveaux."),
 q("Quel type de relation unit un champignon et une algue dans un lichen ?", ["La symbiose", "La prédation", "Le parasitisme", "La compétition"], 0, "Le lichen est un exemple de symbiose : l'algue photosynthétise et le champignon fournit eau et minéraux."),
 q("Que désigne un agrosystème ?", ["Un écosystème naturel intact", "Un écosystème artificialisé pour la production agricole", "Une forêt primaire", "Un océan"], 1, "L'agrosystème est simplifié et géré par l'homme : la diversité y est réduite et les flux sont orientés vers la récolte."),
 q("Quel rendement énergétique approximatif caractérise un transfert entre niveaux trophiques ?", ["100 %", "50 %", "10 %", "1 %"], 2, "Seule une faible fraction (environ 10 %) de l'énergie est transférée au niveau trophique supérieur ; le reste est dissipé."),
 t("Pourquoi la diversité des espèces renforce-t-elle la stabilité d'un écosystème ?", "Plusieurs espèces peuvent remplir la même fonction : si l'une disparaît, d'autres la remplacent.", "C'est la redondance fonctionnelle : la résilience dépend de la variété des espèces et des interactions qui les relient."),
 t("Quel est l'effet de la monoculture sur la biodiversité ?", "Elle réduit la diversité et augmente la vulnérabilité aux maladies et aux aléas.", "Un agrosystème homogène offre peu de refuges aux auxiliaires et dépend davantage des intrants : l'agroécologie cherche à réintroduire de la diversité."),
 t("Comment évalue-t-on l'érosion de la biodiversité ?", "À l'aide d'indicateurs comme le nombre d'espèces, l'abondance, la richesse spécifique et l'état des habitats.", "Ces indicateurs, suivis dans le temps, permettent de mesurer les tendances et d'orienter les politiques de conservation.")
])),

AN.append(a("Sujet type bac – Spécialité mathématiques : étude de fonction et probabilités", "Maths spé",
 "Sujet type – épreuve de spécialité mathématiques (4 points).\n"
 "Exercice 1. On considère la fonction f définie sur ℝ par f(x) = x·e^(–x).\n"
 "1° Calculer f'(x) et dresser le tableau de variations de f.\n"
 "2° Déterminer le maximum de f et la limite de f en +∞.\n"
 "3° Tracer la courbe et préciser les asymptotes.\n"
 "Exercice 2. Dans une population, 30 % des individus portent un caractère génétique. On prélève un échantillon de 50 individus au hasard.\n"
 "1° Donner la loi de X, nombre d'individus porteurs du caractère. 2° Calculer P(X ≤ 12). 3° Donner un intervalle de confiance à 95 % de la proportion.",
 "Corrigé. Ex. 1 : 1° f'(x) = (1 – x)·e^(–x). Comme e^(–x) > 0, le signe de f' est celui de 1 – x : f croît sur ]–∞ ; 1[ et décroît sur ]1 ; +∞[.\n"
 "2° Le maximum est atteint en x = 1 : f(1) = 1/e ≈ 0,368. En +∞, x·e^(–x) → 0 : la droite y = 0 est asymptote horizontale.\n"
 "3° La courbe passe par (0 ; 0), admet un maximum en (1 ; 1/e) et tend vers 0 en +∞ ; en –∞, f(x) → –∞.\n"
 "Ex. 2 : 1° X ~ B(50 ; 0,3). 2° P(X ≤ 12) = somme de k=0 à 12 de C(50,k)·0,3^k·0,7^(50–k) ≈ 0,81.\n"
 "3° Intervalle à 95 % : 0,3 ± 1,96·√(0,3·0,7/50) ≈ 0,3 ± 0,127, soit [0,173 ; 0,427]."))

AN.append(a("Sujet type bac – Spécialité physique-chimie : bilan d'énergie et cinétique", "Physique-chimie",
 "Sujet type – épreuve de spécialité physique-chimie (4 points).\n"
 "Un chariot de masse 2 kg est lâché sans vitesse initiale au sommet d'une piste inclinée de hauteur h = 1,5 m. On néglige les frottements (g = 9,81 m·s⁻²).\n"
 "1° Calculer l'énergie potentielle de pesanteur initiale (référence : bas de la piste).\n"
 "2° En déduire la vitesse du chariot en bas de la piste.\n"
 "3° On recommence avec des frottements : la vitesse mesurée est 4,5 m/s. Calculer l'énergie dissipée et le rendement.\n"
 "4° La réaction entre l'acide chlorhydrique et le carbonate de calcium dégage du CO₂. Écrire l'équation et proposer un moyen d'en suivre la cinétique.",
 "Corrigé. 1° E_pp = m·g·h = 2 × 9,81 × 1,5 = 29,43 J.\n"
 "2° Conservation de l'énergie mécanique : ½·m·v² = 29,43 ⇔ v = √29,43 ≈ 5,42 m/s.\n"
 "3° E_c(mesurée) = ½ × 2 × 4,5² = 20,25 J. Énergie dissipée = 29,43 – 20,25 = 9,18 J. Rendement η = 20,25/29,43 ≈ 0,69, soit 69 %.\n"
 "4° Équation : CaCO₃ + 2 HCl → CaCl₂ + H₂O + CO₂. Cinétique : suivre la masse du système au cours du temps (perte de masse due au CO₂) ou mesurer le volume de gaz dégagé en fonction du temps ; la pente de la courbe donne la vitesse de réaction."))

AN.append(a("Sujet type bac – Spécialité SVT : génétique et évolution des populations", "SVT",
 "Sujet type – épreuve de spécialité SVT (5 points).\n"
 "Dans une population de 10 000 individus, un gène possède deux allèles A et a. On observe 4 900 AA, 4 200 Aa et 900 aa.\n"
 "1° Calculer les fréquences alléliques p (A) et q (a).\n"
 "2° Vérifier si la population est à l'équilibre de Hardy–Weinberg (effectifs théoriques attendus).\n"
 "3° Un changement environnemental favorise les individus AA. Que peut-on prévoir pour les fréquences sur plusieurs générations ?\n"
 "4° Citez deux autres facteurs pouvant faire évoluer les fréquences alléliques.",
 "Corrigé. 1° p = (2×4900 + 4200)/(2×10000) = 14000/20000 = 0,7 ; q = 1 – p = 0,3.\n"
 "2° Effectifs attendus : AA = p²×10000 = 4900 ; Aa = 2pq×10000 = 4200 ; aa = q²×10000 = 900. Les effectifs observés correspondent exactement aux effectifs attendus : la population est à l'équilibre de Hardy–Weinberg.\n"
 "3° La sélection avantageant AA, la fréquence p augmentera au fil des générations et q diminuera : la population s'adapte (sélection directionnelle).\n"
 "4° D'autres facteurs : la dérive génétique, les mutations, les migrations (flux géniques) et la non-panmixie."))

AN.append(a("Sujet type bac – Spécialité NSI : algorithmique et structures de données", "NSI",
 "Sujet type – épreuve de spécialité NSI (4 points).\n"
 "Exercice 1. On dispose du tableau T = [7, 3, 9, 1, 5].\n"
 "1° Appliquer le tri par insertion et donner les étapes. 2° Donner la complexité dans le pire cas. 3° Rechercher la valeur 9 par dichotomie dans le tableau trié : donner le nombre de comparaisons.\n"
 "Exercice 2. On implémente une file avec une liste Python.\n"
 "1° Quel principe de gestion des éléments faut-il respecter ? 2° Écrire les fonctions empiler et dépiler. 3° Donner un exemple d'utilisation d'une file en informatique.",
 "Corrigé. Ex. 1 : 1° [7, 3, 9, 1, 5] → [3, 7, 9, 1, 5] → [3, 7, 9, 1, 5] → [1, 3, 7, 9, 5] → [1, 3, 5, 7, 9]. À chaque étape, on insère l'élément courant dans le préfixe déjà trié.\n"
 "2° Le coût dans le pire cas est O(n²).\n"
 "3° Tableau trié [1, 3, 5, 7, 9] : comparer à 5 (milieu), puis à 7, puis à 9, soit environ 3 comparaisons (log₂(5) ≈ 2,3).\n"
 "Ex. 2 : 1° FIFO (first in, first out). 2° def empiler(f, x): f.append(x) ; def depiler(f): return f.pop(0) (ou collections.deque pour un coût O(1)).\n"
 "3° Exemples : gestion des impressions, file de messages, parcours en largeur d'un graphe (BFS)."))

AN.append(a("Sujet type bac – Spécialité SI : asservissement d'un régulateur de température", "SI",
 "Sujet type – épreuve de spécialité sciences de l'ingénieur (4 points).\n"
 "On étudie un système de régulation thermique d'une serre. La consigne est de 25 °C. Un capteur mesure la température, un régulateur compare à la consigne et commande un actionneur (chauffage).\n"
 "1° Représenter le schéma fonctionnel de la boucle de régulation en nommant chaque élément.\n"
 "2° Quelle est la différence avec une commande en boucle ouverte ?\n"
 "3° Après une perturbation (ouverture d'une porte), la température revient à 25 °C en 3 minutes avec un léger dépassement. Commenter ces observations à l'aide des critères de performance.\n"
 "4° Quel rôle joue le capteur dans la précision du système ?",
 "Corrigé. 1° Chaîne : consigne (25 °C) → comparateur → régulateur → actionneur (chauffage) → procédé (serre) → sortie (température) ; le capteur renvoie la mesure au comparateur : c'est une boucle fermée (rétroaction négative).\n"
 "2° En boucle ouverte, le chauffage fonctionnerait selon une durée fixe, sans tenir compte de la température réelle : une perturbation modifierait définitivement la sortie. La boucle fermée compense les perturbations.\n"
 "3° Le retour à la consigne après 3 minutes indique un temps de réponse de 3 minutes ; l'absence d'écart statique montre une bonne précision (action intégrale) ; le léger dépassement révèle des oscillations amorties : le système reste stable mais le réglage pourrait être optimisé (action dérivée).\n"
 "4° Le capteur conditionne la qualité de la mesure : sa résolution, sa précision et son temps de réponse limitent la précision globale. Une mesure erronée conduit le régulateur à corriger à tort."))

AN.append(a("Sujet type bac – Spécialité biologie-écologie : fonctionnement d'un agrosystème", "Biologie-écologie",
 "Sujet type – épreuve de spécialité biologie-écologie (4 points).\n"
 "Une parcelle de 1 hectare est cultivée en monoculture de maïs depuis 15 ans. L'agriculteur souhaite diversifier son assolement pour améliorer la durabilité du système.\n"
 "1° Expliquer pourquoi la monoculture réduit la biodiversité et la résilience de l'agrosystème.\n"
 "2° Décrire deux relations interspécifiques utiles à la culture.\n"
 "3° Proposer trois leviers d'agroécologie et expliquer leur effet sur les flux de matière et d'énergie.\n"
 "4° Comment mesurer l'effet de ces pratiques sur la biodiversité ?",
 "Corrigé. 1° La monoculture simplifie la structure de l'écosystème : une seule espèce occupe l'espace, les niches sont rares, les réseaux trophiques sont pauvres. La redondance fonctionnelle est faible : si un ravageur ou une sécheresse frappe, aucune espèce ne prend le relais, d'où une faible résilience et une dépendance aux intrants.\n"
 "2° Mutualisme : les légumineuses associées au maïs fixent l'azote atmosphérique grâce à des bactéries symbiotiques (Rhizobium). Prédation : les coccinelles consomment des pucerons, limitant les ravageurs sans insecticide.\n"
 "3° Rotation : alterner les cultures rompt les cycles des pathogènes et répartit l'usage des nutriments. Couverts végétaux : ils protègent le sol, fixent l'azote et augmentent la matière organique. Lutte intégrée : elle raisonne les interventions en privilégiant les auxiliaires, réduisant les intrants.\n"
 "4° Suivre des indicateurs : richesse spécifique (nombre d'espèces d'insectes, d'oiseaux, de plantes), abondance, diversité des communautés du sol, rendement et qualité du sol (matière organique). Un suivi pluriannuel permet de comparer avant/après."))

save("lead-general-partie-C.json", F, AN)
print("Partie C:", len(F), "fiches,", len(AN), "annales")
