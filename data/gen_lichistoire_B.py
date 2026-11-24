# -*- coding: utf-8 -*-
"""Générateur de lichistoire-mat-part-B.json — lot B de la filière Licence Histoire.

20 fiches au format « prototype » :
 - Droit : 7 fiches (DR1. à DR7.)
 - Économie : 7 fiches (EC1. à EC7.)
 - Informatique : 6 fiches (IN1. à IN6.)

Sources : arrêté du 6 avril 2021, BO spécial n° 7 du 17 février 2022,
éduscol, programmes de licence d'histoire et matières de soutien.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fixtures import (fiche, qcm, qt, diag, bloc, valider_et_ecrire,
                      svg_grille, svg_flux, svg_etapes, svg_compare)

FIL = ["lic-histoire"]
L1, L2, L3 = ["L1"], ["L2"], ["L3"]

REF = ("Arrêté du 6 avril 2021 (référence commune des licences FicheLab) "
       "· BO spécial n° 7 du 17 février 2022 · éduscol · programmes de licence d'histoire")
REF_D = REF + " · Code civil, Code pénal, traités européens"
REF_E = REF + " · programmes de sciences économiques · INSEE"
REF_I = REF + " · outils numériques pour l'histoire · CNIL/RGPD"


def Bi(t, x): return bloc(t, texte=x, type="intro")
def Bf(t, e, l): return bloc(t, eq=e, leg=l, type="formule")
def Bg(t, cols, rows): return bloc(t, items=[cols] + list(rows), type="grille")
def Bl(t, items): return bloc(t, items=items, type="liste")
def Be(t, items): return bloc(t, items=items, type="etapes")
def Ba(t, items): return bloc(t, items=items, type="attention")
def Bx(t, items): return bloc(t, items=items, type="exemples")

def SG(t, cols, rows): return diag(t, svg_grille(t, cols, rows))
def SF(t, steps): return diag(t, svg_flux(t, steps))
def SE(t, steps): return diag(t, svg_etapes(t, steps))
def SC(t, g, d): return diag(t, svg_compare(t, g, d))


def build(an, mat, titre, ref, points, qcms, texts,
          idea, formule, leg, grille, etapes, attention, exemples, schemas):
    """15 arguments : le bloc « À retenir » est tire des points 1, 4, 7 et 10."""
    liste = []
    for p in (points[0], points[3], points[6], points[9]):
        liste.append(p if len(p) <= 130 else p[:127].rsplit(" ", 1)[0] + "…")
    aff = [Bi("L'idée en une phrase", idea),
           Bf("La règle à retenir", formule, leg),
           Bg("Tableau de synthèse", grille[0], grille[1]),
           Bl("À retenir", liste),
           Be("Méthode pas à pas", etapes),
           Ba("Pièges fréquents", attention),
           Bx("Exemples d'application", exemples)]
    qs = [qcm(q, o, c, r) for (q, o, c, r) in qcms] + [qt(q, r, c) for (q, r, c) in texts]
    return fiche(FIL, an, mat, titre, ref, points, qs, aff, schemas)


F = []

# =====================================================================
# DROIT — 7 fiches (DR1. à DR7.)
# =====================================================================

F.append(build(
    L1, "Droit", "DR1. · L'État et les institutions en France", REF_D,
    [
        "L'État est une personne morale de droit public qui dispose d'un territoire, d'une population et d'une souveraineté ; l'historien étudie ses formes successives.",
        "La monarchie absolue reposait sur le roi, détenteur du pouvoir ; la Révolution de 1789 instaure une monarchie constitutionnelle puis la République en 1792.",
        "La Déclaration des droits de l'homme et du citoyen de 1789 pose le principe de la souveraineté nationale et la séparation des pouvoirs (art. 16).",
        "Le Directoire (1795-1799), le Consulat et l'Empire (1799-1815) succèdent à la Convention : les régimes se caractérisent par des équilibres institutions différents.",
        "La Restauration (1815-1830), la monarchie de Juillet (1830-1848), la IIᵉ République (1848-1852) et le Second Empire (1852-1870) illustrent la fragilité des régimes au XIXᵉ siècle.",
        "Les lois constitutionnelles de 1875 instaurent la IIIᵉ République : un président, une Chambre des députés et un Sénat ; le régime dure jusqu'en 1940.",
        "La Constitution du 27 octobre 1946 fonde la IVᵉ République, caractérisée par un parlementarisme fort et une instabilité ministérielle.",
        "La Constitution du 4 octobre 1958 institue la Vᵉ République : un président élu, un gouvernement responsable devant l'Assemblée nationale et un Conseil constitutionnel.",
        "L'article 16 de la Constitution de 1958 permet au président de prendre des mesures exceptionnelles en cas de crise grave, comme en 1961 lors du putsch d'Alger.",
        "L'élection présidentielle au suffrage universel direct est instaurée en 1962 et utilisée pour la première fois en 1965.",
        "Le Conseil constitutionnel, créé en 1958, contrôle la conformité des lois à la Constitution ; sa décision de 1971 reconnaît le bloc de constitutionnalité.",
        "Une institution ne s'explique que par son contexte : l'historien doit dater chaque texte et montrer les débats qui ont accompagné son adoption.",
    ],
    [
        ("Quel article de la DDHC de 1789 énonce la séparation des pouvoirs ?",
         ["L'article 1er", "L'article 16", "L'article 17", "L'article 10"], 1,
         "L'article 16 subordonne l'exercice du pouvoir à la volonté générale et exige une organisation des pouvoirs séparés."),
        ("En quelle année la IIIᵉ République est-elle instaurée ?",
         ["1789", "1848", "1875", "1958"], 2,
         "Les lois constitutionnelles de 1875 organisent la IIIᵉ République, proclamée après la guerre de 1870."),
        ("Quel régime succède à la IVᵉ République ?",
         ["La IIIᵉ République", "Le Second Empire", "La Vᵉ République", "La Convention"], 2,
         "La Vᵉ République est fondée par la Constitution du 4 octobre 1958, après la crise algérienne."),
        ("Quel est le rôle du Conseil constitutionnel ?",
         ["Voter les lois", "Contrôler la conformité des lois à la Constitution", "Diriger l'armée", "Nommer les préfets"], 1,
         "Le Conseil constitutionnel vérifie la constitutionnalité des lois et veille au respect du bloc de constitutionnalité."),
        ("L'élection présidentielle au suffrage universel direct date de :",
         ["1848", "1875", "1962", "1981"], 2,
         "La révision constitutionnelle de 1962 instaure l'élection du président au suffrage universel direct ; première élection en 1965."),
        ("Quel régime correspond à la période 1852-1870 ?",
         ["La monarchie de Juillet", "Le Second Empire", "La IIIᵉ République", "Le Directoire"], 1,
         "Napoléon III instaure le Second Empire de 1852 à 1870, avant la défaite de Sedan et la proclamation de la République."),
        ("Quel est un effet de la décision du Conseil constitutionnel de 1971 ?",
         ["La fin de la Vᵉ République", "La reconnaissance du bloc de constitutionnalité", "La suppression du Sénat", "L'instauration du suffrage censitaire"], 1,
         "La décision du 16 juillet 1971 intègre la DDHC et les principes fondamentaux reconnus par les lois de la République au bloc de constitutionnalité."),
        ("Quel est le fruit d'une monarchie constitutionnelle en 1791 ?",
         ["Le roi partage le pouvoir avec une Assemblée", "Le roi est aboli", "Le Directoire", "L'Empire"], 0,
         "La Constitution de 1791 maintient le roi mais limite ses pouvoirs et crée une Assemblée législative élue."),
        ("Pourquoi faut-il dater un texte institutionnel ?",
         ["Pour le rendre plus long", "Parce que son sens dépend du régime et du contexte", "Pour la bibliographie", "Pour le traduire"], 1,
         "Une même expression (« souveraineté », « loi ») n'a pas le même sens sous la monarchie et sous la République."),
    ],
    [
        ("Comment expliquer la fragilité des régimes français au XIXᵉ siècle ?",
         "Entre 1815 et 1870, la France connaît la Restauration, la monarchie de Juillet, la IIᵉ République et le Second Empire. Chaque régime résulte d'une rupture (1830, 1848, 1852, 1870) et se heurte à des tensions entre le pouvoir exécutif et les forces parlementaires, ainsi qu'à la question du suffrage. La stabilité de la IIIᵉ République après 1875 tient à un compromis entre républicains et monarchistes et à une durée institutionnelle plus longue. L'historien doit relier les crises politiques aux transformations sociales et économiques du siècle.",
         "On attend une chronologie des régimes, des causes politiques et sociales et une comparaison des durées."),
        ("Quelle est la différence entre la monarchie constitutionnelle de 1791 et la monarchie absolue ?",
         "La monarchie absolue concentre tous les pouvoirs entre les mains du roi, qui les exerce par délégation. La monarchie constitutionnelle issue de la Constitution de 1791 conserve le roi comme chef de l'État, mais le pouvoir législatif est exercé par une Assemblée élue et le roi voit ses pouvoirs limités par la Constitution et la loi. Cette transformation est l'aboutissement de la Révolution de 1789 et de la DDHC, tout en conservant un roi : elle constitue une solution intermédiaire, renversée en 1792.",
         "On distingue la titularité du pouvoir et son exercice, avec des dates précises."),
    ],
    "Les institutions françaises sont des constructions datées : chaque régime répond à une crise et invente un équilibre des pouvoirs.",
    "Souveraineté → Constitution → organes → contrôle",
    "L'étude d'une institution exige de la dater, d'identifier ses organes et de la replacer dans son contexte de crise.",
    (["Régime", "Dates", "Trait dominant"],
     [["Monarchie absolue", "Avant 1789", "Pouvoir royal"],
      ["Monarchie constitutionnelle", "1791-1792", "Roi + Assemblée"],
      ["IIIᵉ République", "1875-1940", "Parlementarisme"],
      ["Vᵉ République", "Depuis 1958", "Président fort"]]),
    ["Repérer la souveraineté (peuple, roi, Parlement).",
     "Dater la Constitution et ses révisions.",
     "Identifier les organes et leurs pouvoirs respectifs.",
     "Repérer le mécanisme de responsabilité du gouvernement.",
     "Relier l'institution aux crises qui l'ont produite."],
    ["Confondre les régimes successifs du XIXᵉ siècle.",
     "Appliquer un sens moderne au mot « souveraineté ».",
     "Oublier que la Vᵉ République date de 1958 et le suffrage direct de 1962.",
     "Présenter le Conseil constitutionnel comme un organe de 1789.",
     "Expliquer une institution sans la dater."],
    ["<span class=\"cle\">1789</span> → DDHC et souveraineté nationale.",
     "<span class=\"cle\">1875</span> → lois constitutionnelles de la IIIᵉ République.",
     "<span class=\"cle\">1958</span> → Constitution de la Vᵉ République.",
     "<span class=\"cle\">1971</span> → bloc de constitutionnalité."],
    [SG("Les régimes français", ["Régime", "Date", "Pouvoir dominant"],
        [["Monarchie absolue", "Avant 1789", "Le roi"],
         ["IIIᵉ République", "1875", "Le Parlement"],
         ["Vᵉ République", "1958", "Le président"]]),
     SF("D'une crise à une institution",
        [("Crise", "Rupture politique"), ("Débat", "Constitution"),
         ("Organes", "Pouvoirs répartis"), ("Contrôle", "Constitutionnalité")]),
     SC("Parlementarisme / présidentialisme",
        ("IIIᵉ République", ["Gouvernement responsable", "Parlement fort", "Instabilité"]),
        ("Vᵉ République", ["Président élu", "Gouvernement nommé", "Stabilité relative"]))]))

F.append(build(
    L1, "Droit", "DR2. · Personnes, citoyenneté et droits fondamentaux", REF_D,
    [
        "La personnalité juridique est l'aptitude à être titulaire de droits et de devoirs ; elle est reconnue à la personne physique dès sa naissance.",
        "La Déclaration des droits de l'homme et du citoyen de 1789 énonce des droits imprescriptibles : liberté, propriété, sûreté et résistance à l'oppression.",
        "La citoyenneté est une condition juridique et politique : elle donne la qualité de citoyen, couplée à des droits et des devoirs envers la cité.",
        "La Constitution de 1791 distingue les citoyens « actifs », qui paient un cens et votent, des citoyens « passifs » ; le suffrage universel masculin est proclamé en 1848.",
        "Le Code civil de 1804 consacre l'égalité devant la loi, mais il organise une hiérarchie des sexes et distingue les enfants légitimes et naturels.",
        "L'esclavage est aboli en 1794, rétabli en 1802 et définitivement aboli en 1848 : cette chronologie est essentielle pour l'histoire coloniale.",
        "La femme est privée de droits politiques pendant tout le XIXᵉ siècle ; le vote des femmes n'est obtenu qu'en 1944 et exercé en 1945.",
        "Les droits de la personnalité (nom, image, vie privée) sont protégés par l'article 9 du Code civil et par l'article 8 de la CEDH (1950).",
        "La capacité juridique est l'aptitude à exercer ses droits : mineurs et majeurs protégés agissent par un représentant légal.",
        "La nationalité est le lien juridique entre une personne et un État ; le Code civil de 1804 et la loi de 1889 fixent des règles qui ont marqué l'intégration des immigrés.",
        "Les personnes morales (associations, sociétés, collectivités) ont une personnalité distincte de celle de leurs membres et un siège social.",
        "L'historien du droit doit toujours préciser la date du texte : le sens de « citoyen » en 1791 n'est pas celui d'aujourd'hui.",
    ],
    [
        ("Quels droits sont proclamés par la DDHC de 1789 ?",
         ["Liberté, propriété, sûreté, résistance à l'oppression", "Travail, santé, logement", "Paix et commerce", "Souveraineté royale"], 0,
         "L'article 2 de la DDHC énumère les droits naturels et imprescriptibles : liberté, propriété, sûreté, résistance à l'oppression."),
        ("Qui vote sous la Constitution de 1791 ?",
         ["Tous les habitants", "Les citoyens actifs payant un cens", "Les femmes seules", "Le roi seul"], 1,
         "La Constitution de 1791 réserve le vote aux citoyens dits « actifs », assujettis au cens, et exclut les femmes."),
        ("Quelle date correspond à l'abolition définitive de l'esclavage en France ?",
         ["1794", "1802", "1848", "1889"], 2,
         "L'esclavage est aboli en 1794, rétabli par Napoléon en 1802 puis aboli définitivement par le décret du 27 avril 1848."),
        ("Quel article du Code civil protège la vie privée ?",
         ["L'article 1er", "L'article 9", "L'article 544", "L'article 1382"], 1,
         "L'article 9 du Code civil consacre le respect dû à la vie privée et fonde la protection de l'image."),
        ("Quand les femmes obtiennent-elles le droit de vote en France ?",
         ["1848", "1875", "1944", "1965"], 2,
         "L'ordonnance du 21 avril 1944 accorde le vote aux femmes, qui l'exercent pour la première fois en 1945."),
        ("Quand date le Code civil français ?",
         ["1789", "1791", "1804", "1889"], 2,
         "Le Code civil est promulgué en 1804 ; il consacre l'égalité devant la loi mais reflète la société de son époque."),
        ("Comment appelle-t-on l'aptitude à exercer soi-même ses droits ?",
         ["La personnalité juridique", "La capacité juridique", "La citoyenneté", "La nationalité"], 1,
         "La personnalité est la titularité des droits ; la capacité en est l'exercice personnel."),
        ("Que distingue le Code civil de 1804 concernant les naissances ?",
         ["Les enfants légitimes et naturels", "Les garçons et les filles uniquement", "Les citoyens et les étrangers seuls", "Aucune distinction"], 0,
         "Le Code civil distingue les enfants légitimes, nés dans le mariage, et les enfants naturels, dont les droits sont réduits."),
    ],
    [
        ("Comment l'historien doit-il lire une déclaration de droits de 1789 ?",
         "Il doit la situer dans la Révolution, identifier ses auteurs et son public, analyser les articles (souveraineté, liberté, égalité, propriété), puis relever ses limites : le vote censitaire de 1791, l'exclusion des femmes et le maintien de l'esclavage jusqu'en 1794. La DDHC est donc à la fois un texte fondateur et un document daté, dont l'historiographie a montré les usages successifs, y compris coloniaux.",
         "On attend la situation, l'analyse des principes et la critique des exclusions."),
        ("Quelle différence entre nationalité et citoyenneté ?",
         "La nationalité est un lien juridique entre la personne et un État : elle détermine notamment la protection diplomatique et le droit de résidence. La citoyenneté est la qualité de membre de la cité politique, qui confère des droits politiques comme le vote et l'éligibilité. L'histoire montre que ces deux notions ne coïncident pas toujours : au XIXᵉ siècle, des étrangers naturalisés pouvaient voter, tandis que des femmes de nationalité française étaient exclues du vote.",
         "On distingue le lien juridique à l'État des droits politiques, avec des exemples datés."),
    ],
    "Les droits ne sont pas des évidences intemporelles : ils ont une histoire, des dates et des exclusions.",
    "Droits proclamés ↔ droits effectivement exercés",
    "Toute déclaration de droits doit être confrontée aux pratiques et aux exclusions de son époque.",
    (["Droit", "Date clé", "Limite historique"],
     [["Suffrage", "1791/1848/1944", "Cens, femmes excluses jusqu'en 1944"],
      ["Abolition esclavage", "1794, 1848", "Rétablissement en 1802"],
      ["Égalité civile", "Code civil 1804", "Hiérarchie des sexes"],
      ["Vie privée", "Art. 9 C. civ., CEDH 1950", "Protection progressive"]]),
    ["Toujours dater le texte de droit étudié.",
     "Distinguer les droits proclamés de leur exercice réel.",
     "Repérer les exclusions (femmes, esclaves, cens).",
     "Confronter les textes aux pratiques administratives.",
     "Situer les décisions de justice dans leur époque."],
    ["Lire la DDHC avec les catégories d'aujourd'hui sans nuance.",
     "Confondre nationalité et citoyenneté.",
     "Oublier que le Code civil de 1804 est inégalitaire.",
     "Croire que l'esclavage a été aboli une seule fois.",
     "Présenter un droit comme acquis sans dater son acquisition."],
    ["<span class=\"cle\">1789</span> → DDHC, droits naturels et imprescriptibles.",
     "<span class=\"cle\">1804</span> → Code civil et égalité devant la loi.",
     "<span class=\"cle\">1848</span> → abolition définitive de l'esclavage.",
     "<span class=\"cle\">1944</span> → vote des femmes."],
    [SG("Droits et exclusions", ["Droit", "Progrès", "Limite"],
        [["Vote", "1791", "Cens et femmes excluses"],
         ["Abolition", "1794", "Rétabli en 1802"],
         ["Égalité", "1804", "Hiérarchie des sexes"]]),
     SF("Construire un droit",
        [("Revendication", "Débat politique"), ("Texte", "Loi ou déclaration"),
         ("Application", "Pratique administrative"), ("Contrôle", "Justice")]),
     SC("Proclamation / exercice",
        ("Proclamation", ["Texte de principe", "1789, 1848", "Portée symbolique"]),
        ("Exercice", ["Conditions réelles", "Cens, sexe, nationalité", "Pratiques datées"]))]))

F.append(build(
    L1, "Droit", "DR3. · Propriété, biens et patrimoine historique", REF_D,
    [
        "La propriété est le droit de jouir et de disposer d'une chose de la manière la plus absolue, pourvu qu'on n'en fasse pas un usage prohibé (art. 544 du Code civil).",
        "Les trois attributs du propriétaire sont l'usus (usage), le fructus (jouissance des fruits) et l'abusus (pouvoir de disposition).",
        "Au Moyen Âge, la propriété est souvent éclatée entre le seigneur, qui détient la justice et des redevances, et les paysans qui exploitent la terre.",
        "La Révolution abolit les privilèges féodaux en août 1789 et organise la vente des biens nationaux, ce qui transforme le parcellaire français.",
        "Le Code civil de 1804 consacre une propriété individuelle et absolue, opposable à tous ; il reflète la société issue de la Révolution.",
        "Les biens se classent en mobiliers et immobiliers : cette distinction commande les règles de transfert et de publicité foncière.",
        "Le domaine public (routes, fleuves, monuments affectés à l'usage public) est inaliénable et imprescriptible.",
        "L'expropriation pour cause d'utilité publique est prévue par l'article 545 du Code civil : elle exige une indemnité juste et préalable.",
        "L'accession est un mode originaire d'acquisition : le propriétaire du sol devient propriétaire de ce qui s'y joint (alluvions, constructions).",
        "La possession est la détention d'une chose avec intention de s'en comporter comme propriétaire ; elle peut conduire à la prescription acquisitive.",
        "La propriété littéraire et artistique, reconnue par les lois de 1791 et 1793, protège l'auteur ; elle est aujourd'hui encadrée par le Code de la propriété intellectuelle.",
        "L'historien du patrimoine étudie les changements de propriétaire comme des indices de rapports sociaux et de politiques publiques.",
    ],
    [
        ("Quel article du Code civil définit la propriété ?",
         ["L'article 1er", "L'article 544", "L'article 9", "L'article 1101"], 1,
         "L'article 544 définit la propriété comme le droit de jouir et de disposer des choses de la manière la plus absolue."),
        ("Quel attribut du propriétaire consiste à vendre un bien ?",
         ["L'usus", "Le fructus", "L'abusus", "La servitude"], 2,
         "L'abusus est le pouvoir de disposition : vendre, donner, léguer."),
        ("Qu'a fait la Révolution des biens de l'Église ?",
         ["Elle les a rendus au clergé", "Elle les a vendus comme biens nationaux", "Elle les a détruits", "Elle les a donnés aux communes"], 1,
         "La Constitution civile du clergé et la vente des biens nationaux (loi du 2 novembre 1789) ont transféré ces biens à l'État puis à des acheteurs."),
        ("Les biens du domaine public sont :",
         ["Aliénables et prescriptibles", "Inaliénables et imprescriptibles", "Vendables par décret", "Exempts de toute règle"], 1,
         "Le domaine public est inaliénable et imprescriptible tant qu'il reste affecté à l'utilité publique."),
        ("Que exige l'expropriation pour cause d'utilité publique ?",
         ["L'accord du propriétaire", "Une indemnité juste et préalable", "Un référendum local", "Une donation"], 1,
         "L'article 545 C. civ. et l'article 17 de la DDHC imposent une indemnité juste et préalable."),
        ("L'accession est un mode d'acquisition :",
         ["Dérivé", "Originaire", "Contractuel", "Successoral"], 1,
         "L'accession ne suppose aucun transfert volontaire : le propriétaire acquiert ce qui s'unit à son bien."),
        ("Quelles lois reconnaissent la propriété littéraire en 1791 et 1793 ?",
         ["Les lois d'alliance", "Les lois sur la propriété intellectuelle de la Révolution", "Le Code pénal", "La loi de 1889"], 1,
         "Les lois des 13 janvier 1791 et 19 juillet 1793 constituent les premières lois modernes sur le droit d'auteur."),
        ("Comment se divise la propriété au Moyen Âge ?",
         ["Entre seigneur et paysans par des droits superposés", "Entre État et communes uniquement", "Entre hommes et femmes à parts égales", "Elle est absente"], 0,
         "La propriété médiévale est souvent démembrée : le seigneur détient des droits (justice, redevances) et le paysan l'usage de la terre."),
    ],
    [
        ("Comment la vente des biens nationaux a-t-elle transformé la propriété française ?",
         "Confisqués à l'Église puis à des émigrés à partir de 1789, les biens nationaux sont vendus pour financer l'État révolutionnaire. Les acheteurs, souvent des bourgeois et des paysans aisés, constituent une nouvelle couche de propriétaires. Le parcellaire est modifié et la propriété devient plus individuelle, conformément à l'idéal de 1789. L'historien étudie les registres de vente, les cadastriers et les actes notariés pour mesurer cette mutation et ses effets sociaux.",
         "On attend la chronologie, le mécanisme juridique et les effets sociaux documentés."),
        ("Quelle est la différence entre propriété et possession ?",
         "La propriété est un droit réel, opposable à tous, qui permet de jouir et disposer d'un bien. La possession est une situation de fait : la détention d'une chose avec l'intention de se comporter comme propriétaire. La possession est protégée par des actions possessoires indépendantes de la preuve de propriété, et elle peut conduire à la prescription acquisitive après un délai légal. Un fermier peut posséder la terre sans en être propriétaire.",
         "On distingue le droit et le fait, avec les conséquences juridiques et historiques."),
    ],
    "La propriété a une histoire : ses formes révèlent les rapports de force et les politiques d'une époque.",
    "Usus + fructus + abusus = propriété",
    "Les mutations de la propriété s'étudient par les actes, les cadastres et les ventes, pas par des définitions seules.",
    (["Période", "Forme dominante", "Source"],
     [["Moyen Âge", "Droits seigneuriaux superposés", "Chartes, censiers"],
      ["1789-1804", "Biens nationaux et Code civil", "Registres de vente"],
      ["Époque contemporaine", "Propriété individuelle et patrimoine", "Cadastre, lois"]]),
    ["Définir le bien avant d'étudier les droits qui le concernent.",
     "Dater les textes et les mutations de propriété.",
     "Distinguer propriété, possession et usage.",
     "Repérer les limites légales (domain public, expropriation).",
     "Croiser les actes notariés avec les sources fiscales."],
    ["Croire que la propriété a toujours eu le même contenu.",
     "Confondre les attributs usus, fructus et abusus.",
     "Ignorer la spécificité du domaine public.",
     "Oublier l'indemnité préalable en cas d'expropriation.",
     "Présenter la vente des biens nationaux comme un don."],
    ["<span class=\"cle\">544 C. civ.</span> → définition de la propriété.",
     "<span class=\"cle\">1789</span> → vente des biens nationaux.",
     "<span class=\"cle\">1804</span> → Code civil et propriété individuelle.",
     "<span class=\"cle\">1791-1793</span> → premières lois sur le droit d'auteur."],
    [SG("Les attributs du propriétaire", ["Attribut", "Pouvoir", "Exemple"],
        [["Usus", "Usage", "Habiter"],
         ["Fructus", "Fruits", "Louer, récolter"],
         ["Abusus", "Disposition", "Vendre, donner"]]),
     SF("Transmettre un bien",
        [("Origine", "Occupation ou accession"), ("Acte", "Vente ou donation"),
         ("Publicité", "Registre foncier"), ("Limite", "Servitude ou expropriation")]),
     SC("Propriété / possession",
        ("Propriété", ["Droit opposable", "Preuve par titre", "Abusus"]),
        ("Possession", ["Situation de fait", "Protection possessoire", "Prescription"]))]))

F.append(build(
    L2, "Droit", "DR4. · Droit pénal, sanctions et histoire de la justice", REF_D,
    [
        "Le droit pénal définit les infractions et les sanctions : il protège l'ordre public et les personnes par la contrainte étatique.",
        "La loi pénale est d'application stricte : nul ne peut être condamné pour un fait qui n'était pas prévu comme délit au moment où il a été commis.",
        "La Responsabilité pénale suppose un fait matériel, une faute (intention ou négligence) et l'absence de cause d'irresponsabilité.",
        "Les peines se divisent en peines principales (emprisonnement, amende) et complémentaires ; la prison devient le mode de sanction dominant au XIXᵉ siècle.",
        "Le Code pénal de 1810, issu du Code napoléonien, distingue crimes, délits et contraventions selon la gravité et la peine encourue.",
        "La peine de mort est abolie en France en 1981 ; elle a été appliquée pendant la Révolution, au XIXᵉ siècle et jusqu'en 1977.",
        "La procédure pénale oppose la phase d'enquête, l'instruction et le jugement ; le juge d'instruction est créé en 1808.",
        "Les droits de la défense et la présomption d'innocence sont des principes progressivement affirmés, consacrés par la CEDH en 1950.",
        "L'histoire de la justice pénale est aussi celle de la police : la police judiciaire se structure au XIXᵉ siècle avec les brigades mobiles (1902).",
        "Les archives judiciaires (dossiers d'instruction, registres de condamnations) sont des sources précieuses pour l'histoire sociale.",
        "La déportation et les bagnes (Brest, Toulon, Cayenne) ont marqué l'époque moderne et contemporaine ; leur étude relève de l'histoire des peines.",
        "L'historien du pénal doit distinguer la loi, sa mise en œuvre et la pratique des tribunaux : les écarts sont révélateurs.",
    ],
    [
        ("Quel principe interdit de condamner pour un fait non prévu par la loi ?",
         ["La présomption d'innocence", "La légalité des délits et des peines", "Le contradictoire", "L'oralité"], 1,
         "Le principe de légalité exige que l'infraction et la peine soient définies par la loi avant les faits."),
        ("Quel Code pénal est adopté en 1810 ?",
         ["Le Code de 1789", "Le Code pénal napoléonien", "Le Code de 1958", "Le Code de 1994"], 1,
         "Le Code pénal de 1810 organise crimes, délits et contraventions et reste en vigueur jusqu'en 1994."),
        ("Quand la peine de mort est-elle abolie en France ?",
         ["1789", "1848", "1977", "1981"], 3,
         "La peine de mort est abolie par la loi du 9 octobre 1981, après une dernière exécution en 1977."),
        ("Quel est le rôle du juge d'instruction ?",
         ["Condamner directement", "Instruire à charge et à décharge", "Défendre l'accusé", "Appliquer la peine"], 1,
         "Le juge d'instruction, institué en 1808, recherche les preuves à charge et à décharge avant le jugement."),
        ("Que distingue le Code pénal de 1810 ?",
         ["Crimes, délits, contraventions", "Fautes et vertus", "Peines et impôts", "Droits et devoirs seuls"], 0,
         "La hiérarchie des infractions repose sur la gravité et la peine : crime, délit, contravention."),
        ("Quel texte européen consacre les droits de la défense ?",
         ["La CEDH (1950)", "Le Code de 1804", "La loi de 1889", "La DDHC de 1789 seule"], 0,
         "La Convention européenne des droits de l'homme (1950) garantit notamment le procès équitable (art. 6)."),
        ("Que sont les archives judiciaires ?",
         ["Des romans", "Des dossiers d'instruction et registres de condamnations", "Des plans de ville", "Des recettes fiscales"], 1,
         "Les dossiers de procédure et les registres de condamnation sont des sources pour l'histoire de la justice et de la société."),
        ("Que faut-il confronter à la loi pénale ?",
         ["La pratique des tribunaux et les archives", "Le nombre de lois", "La couverture des journaux", "Les seuls discours officiels"], 0,
         "L'historien compare le texte légal, son application et les décisions de justice : les écarts sont significatifs."),
    ],
    [
        ("Comment étudier l'évolution de la peine de mort en France ?",
         "On distingue la période où elle est appliquée (Révolution, XIXᵉ siècle, jusqu'en 1977) des débats parlementaires et des doctrines (Beccaria, Hugo). On consulte les lois, les comptes de la justice, la presse et les archives de grâce. On analyse la distinction entre abolition de droit (1981) et dernier cas d'exécution (1977). On situe enfin cette évolution dans un mouvement européen plus large, la CEDH et le protocole n° 6 (1983).",
         "On attend une chronologie, la distinction droit/pratique et des sources variées."),
        ("Pourquoi les archives d'instruction sont-elles utiles à l'histoire sociale ?",
         "Elles contiennent des témoignages, des interrogatoires et des pièces de procédure qui documentent la vie quotidienne, les conflits de voisinage, les rapports de travail et les formes de violence. Leur lecture exige la critique : le dossier est construit par la police et le juge, il entend suspect et témoins dans une perspective accusatoire. Croisées avec d'autres sources (presse, état civil, registres paroissiaux), elles permettent d'écrire une histoire « par le bas » de la justice.",
         "On valorise la richesse des sources et la nécessité de la critique de leur production."),
    ],
    "Le droit pénal est une institution historique : lois, peines et pratiques judiciaires évoluent ensemble.",
    "Infraction + faute + absence d'excuse = responsabilité pénale",
    "Le droit écrit ne dit pas tout de la justice : les archives et les pratiques sont indispensables.",
    (["Élément", "Définition", "Repère"],
     [["Crime", "Infraction la plus grave", "Code de 1810"],
      ["Délit", "Infraction intermédiaire", "Code de 1810"],
      ["Contravention", "Infraction légère", "Code de 1810"],
      ["Instruction", "Recherche des preuves", "Loi de 1808"]]),
    ["Dater la loi pénale étudiée.",
     "Distinguer crime, délit et contravention.",
     "Vérifier les droits de la défense puisés dans la procédure.",
     "Confronter la loi aux archives des tribunaux.",
     "Situer les peines dans une histoire longue de la sanction."],
    ["Condamner selon une loi postérieure aux faits.",
     "Confondre instruction et jugement.",
     "Oublier que la peine de mort a été abolie en 1981 seulement.",
     "Prendre un dossier d'instruction pour un récit neutre.",
     "Ignorer les sources européennes des droits de la défense."],
    ["<span class=\"cle\">1810</span> → Code pénal napoléonien.",
     "<span class=\"cle\">1808</span> → institution du juge d'instruction.",
     "<span class=\"cle\">1950</span> → CEDH et procès équitable.",
     "<span class=\"cle\">1981</span> → abolition de la peine de mort."],
    [SG("Hiérarchie des infractions", ["Type", "Gravité", "Juridiction"],
        [["Crime", "La plus forte", "Cour d'assises"],
         ["Délit", "Intermédiaire", "Tribunal correctionnel"],
         ["Contravention", "La plus faible", "Tribunal de police"]]),
     SE("Suivre une procédure pénale",
        ["Constater l'infraction", "Enquêter et identifier le suspect",
         "Instruire à charge et à décharge", "Juger en audience publique",
         "Appliquer la peine et le cas échéant l'appel"]),
     SC("Loi / pratique judiciaire",
        ("Loi", ["Texte général", "Définitions abstraites", "Évolution datée"]),
        ("Pratique", ["Dossiers et registres", "Application inégale", "Indices sociaux"]))]))

valider_et_ecrire(F, "lichistoire-mat-part-B.json")