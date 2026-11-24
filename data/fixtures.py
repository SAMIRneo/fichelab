# -*- coding: utf-8 -*-
"""Bibliotheque reutilisable pour decliner le format 'fiche prototype' FicheLab.

Une fiche prototype respecte strictement le modele FICHE_UV de index.html :
  filieres[], annees[], matiere, titre, source,
  points[12], questions[8-10], affichage[7 blocs], schema[2-3 SVG]

Ce module ne contient que de la mecanique : le contenu pedagogique reste dans
les scripts gen_<filiere>_*.py.
"""
import json
import os
import re
import xml.etree.ElementTree as ET

BASE = os.path.dirname(os.path.abspath(__file__))

BLOCS_ATTENDUS = ["intro", "formule", "grille", "liste", "etapes", "attention", "exemples"]


# ---------------------------------------------------------------------------
# Questions
# ---------------------------------------------------------------------------
def qcm(q, options, correct, correction, contexte="", calcul=False):
    out = {"type": "qcm", "q": q, "options": list(options), "correct": correct,
           "correction": correction}
    if contexte:
        out["contexte"] = contexte
    if calcul:
        out["calcul"] = True
    return out


def qt(q, reponse, correction, contexte="", calcul=False):
    out = {"type": "texte", "q": q, "reponse": reponse, "correction": correction}
    if contexte:
        out["contexte"] = contexte
    if calcul:
        out["calcul"] = True
    return out


# ---------------------------------------------------------------------------
# SVG — construits par blocs, jamais de texte qui deborde
# ---------------------------------------------------------------------------
def _esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def _wrap(s, n=30):
    """Decoupe un texte en lignes d'au plus n caracteres, sur les espaces."""
    mots = str(s).split()
    lignes, cur = [], ""
    for m in mots:
        if not cur:
            cur = m
        elif len(cur) + 1 + len(m) <= n:
            cur += " " + m
        else:
            lignes.append(cur)
            cur = m
    if cur:
        lignes.append(cur)
    return lignes or [""]


def _texts(x, y, lignes, size=11, anchor="start", fill="var(--fg)", weight=""):
    w = ' font-weight="%s"' % weight if weight else ""
    return "".join(
        '<text x="%s" y="%s" text-anchor="%s" fill="%s" font-size="%s"%s>%s</text>'
        % (x, y + i * (size + 3), anchor, fill, size, w, _esc(l))
        for i, l in enumerate(lignes)
    )


def svg_debut(titre, hauteur, label):
    return ('<svg viewBox="0 0 660 %d" width="100%%" role="img" aria-label="%s">'
            '<text x="16" y="24" fill="var(--ac)" font-size="14" font-weight="bold">%s</text>'
            % (hauteur, _esc(label), _esc(titre)))


def svg_fin():
    return "</svg>"


def svg_grille(titre, colonnes, lignes):
    """Tableau lisible : colonnes = titres, lignes = listes de cellules."""
    n = len(colonnes)
    widths = [max(70, min(230, int(628 / n)))] * n
    widths[-1] = 628 - sum(widths[:-1])
    h = 40 + 30 * (len(lignes) + 1)
    s = [svg_debut(titre, h, titre)]
    x = 16
    for i, c in enumerate(colonnes):
        s.append('<rect x="%d" y="36" width="%d" height="28" fill="var(--ac)" opacity="0.18"/>'
                 % (x, widths[i]))
        s.append(_texts(x + widths[i] / 2, 55, _wrap(c, 22), 10, "middle", "var(--ac)", "bold"))
        x += widths[i]
    for j, row in enumerate(lignes):
        y = 64 + j * 30
        x = 16
        for i, cell in enumerate(row):
            s.append('<rect x="%d" y="%d" width="%d" height="28" fill="var(--card2)" '
                     'stroke="var(--dim)" stroke-opacity="0.35"/>' % (x, y, widths[i]))
            s.append(_texts(x + 6, y + 18, _wrap(cell, 24)[:1], 10))
            x += widths[i]
    s.append(svg_fin())
    return "".join(s)


def svg_flux(titre, etapes):
    """Chaine lineaire de boites avec fleches. etapes = [(titre, texte), ...]."""
    n = len(etapes)
    dispo = 628
    gap = 14 if n > 1 else 0
    w = int((dispo - gap * (n - 1)) / n)
    h = 48 + max(len(_wrap(t, 13)) for t, _ in etapes) * 13 + 42
    s = [svg_debut(titre, h, "Enchainement : " + titre)]
    x = 16
    for i, (t, d) in enumerate(etapes):
        s.append('<rect x="%d" y="52" width="%d" height="%d" rx="7" fill="var(--card2)" '
                 'stroke="var(--ac)"/>' % (x, w, h - 70))
        s.append(_texts(x + w / 2, 72, _wrap(t, 14)[:2], 11, "middle", "var(--ac)", "bold"))
        s.append(_texts(x + w / 2, 96, _wrap(d, 16)[:3], 9, "middle"))
        if i < n - 1:
            s.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="var(--ac)" '
                     'stroke-width="2" marker-end="url(#fl%s)"/>'
                     % (x + w + 1, 52 + (h - 70) / 2, x + w + gap - 1, 52 + (h - 70) / 2,
                        abs(hash(titre)) % 99999))
        x += w + gap
    s.insert(1, '<defs><marker id="fl%s" markerWidth="9" markerHeight="9" refX="7" refY="3" '
             'orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="var(--ac)"/></marker></defs>'
             % (abs(hash(titre)) % 99999))
    s.append(svg_fin())
    return "".join(s)


def svg_etapes(titre, etapes):
    """Cartes numerotees : etapes = [texte, ...] (3 a 6)."""
    n = len(etapes)
    h = 40 + 34 * n
    s = [svg_debut(titre, h, "Procedure : " + titre)]
    for i, txt in enumerate(etapes):
        y = 36 + i * 34
        s.append('<circle cx="30" cy="%d" r="11" fill="var(--ac)"/>'
                 '<text x="30" y="%d" text-anchor="middle" fill="var(--ac-tx)" '
                 'font-size="11" font-weight="bold">%d</text>' % (y + 13, y + 17, i + 1))
        s.append('<rect x="50" y="%d" width="594" height="28" rx="5" fill="var(--card2)" '
                 'stroke="var(--dim)" stroke-opacity="0.35"/>' % y)
        s.append(_texts(58, y + 18, _wrap(txt, 92)[:1], 10))
    s.append(svg_fin())
    return "".join(s)


def svg_compare(titre, gauche, droite):
    """Deux colonnes opposees : gauche/droite = (titre, [lignes])."""
    lignes = max(len(gauche[1]), len(droite[1]))
    h = 46 + 26 * (lignes + 1)
    s = [svg_debut(titre, h, "Comparaison : " + titre)]
    for x, t, col in [(16, gauche[0], gauche[1]), (338, droite[0], droite[1])]:
        s.append('<rect x="%d" y="34" width="306" height="26" fill="var(--ac)" opacity="0.18"/>'
                 % x)
        s.append(_texts(x + 153, 52, _wrap(t, 30)[:1], 11, "middle", "var(--ac)", "bold"))
        for j, item in enumerate(col):
            y = 60 + j * 26
            s.append('<rect x="%d" y="%d" width="306" height="24" fill="var(--card2)" '
                     'stroke="var(--dim)" stroke-opacity="0.35"/>' % (x, y))
            s.append(_texts(x + 6, y + 16, _wrap(item, 40)[:1], 9))
    s.append(svg_fin())
    return "".join(s)


def diag(titre, svg):
    return {"titre": titre, "svg": svg}


# ---------------------------------------------------------------------------
# Fiche
# ---------------------------------------------------------------------------
def fiche(filieres, annees, matiere, titre, source, points, questions, affichage, schema):
    return {"filieres": list(filieres), "annees": list(annees), "matiere": matiere,
            "titre": titre, "source": source, "points": list(points),
            "questions": list(questions), "affichage": list(affichage), "schema": list(schema)}


def bloc(titre_bloc, texte=None, eq=None, leg=None, items=None, type=None):
    """Cree un bloc en devinant son type depuis son titre, ou via type= explicite."""
    import unicodedata
    t = "".join(c for c in unicodedata.normalize("NFD", titre_bloc.lower())
                if unicodedata.category(c) != "Mn")
    def a(mot):
        return re.search(r"\b" + re.escape(mot) + r"\w*", t) is not None
    if type:
        typ = type
    else:
        typ = next((b for b in BLOCS_ATTENDUS if a(b)), None)
    if typ is None:
        if a("idee") or a("phrase"):
            typ = "intro"
        elif a("formule") or a("eq") or a("loi") or a("regle"):
            typ = "formule"
        elif a("tableau") or a("grille") or a("compar"):
            typ = "grille"
        elif a("etape") or a("protocole") or a("methode"):
            typ = "etapes"
        elif a("piece") or a("attention") or a("piege") or a("erreur"):
            typ = "attention"
        elif a("exemple") or a("chiffre") or a("application"):
            typ = "exemples"
        else:
            typ = "liste"
    b = {"type": typ, "titre": titre_bloc}
    if typ == "formule":
        b["eq"] = eq or ""
        b["leg"] = leg or ""
    elif typ in ("grille", "liste", "etapes", "attention", "exemples"):
        b["items"] = items or []
    else:
        b["texte"] = texte or ""
    return b


# ---------------------------------------------------------------------------
# Validation / audit
# ---------------------------------------------------------------------------
CJK = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff]")
INTERDIT_SVG = re.compile(r"<script|\bon\w+\s*=|javascript:|<foreignObject", re.I)


def valider_fiche(f, idx=0):
    errs = []
    for k in ("filieres", "annees", "matiere", "titre", "source", "points",
              "questions", "affichage", "schema"):
        if k not in f:
            errs.append("fiche %d: champ %s manquant" % (idx, k))
    if errs:
        return errs
    n_pts = len(f["points"])
    if not 10 <= n_pts <= 14:
        errs.append("fiche %d: %d points (attendu 10-14)" % (idx, n_pts))
    n_q = len(f["questions"])
    if not 8 <= n_q <= 10:
        errs.append("fiche %d: %d questions (attendu 8-10)" % (idx, n_q))
    n_qcm = sum(1 for q in f["questions"] if q.get("type") == "qcm")
    n_txt = sum(1 for q in f["questions"] if q.get("type") == "texte")
    if n_qcm < 6 or n_txt < 2:
        errs.append("fiche %d: %d QCM / %d texte (attendu >=6 / >=2)" % (idx, n_qcm, n_txt))
    for j, q in enumerate(f["questions"]):
        if q.get("type") == "qcm":
            if len(q.get("options", [])) < 2:
                errs.append("fiche %d q%d: options" % (idx, j))
            if not isinstance(q.get("correct"), int) or not 0 <= q["correct"] < len(q["options"]):
                errs.append("fiche %d q%d: correct" % (idx, j))
        elif q.get("type") == "texte":
            if not q.get("reponse") or not q.get("correction"):
                errs.append("fiche %d q%d: texte vide" % (idx, j))
        else:
            errs.append("fiche %d q%d: type inconnu" % (idx, j))
        if not q.get("correction"):
            errs.append("fiche %d q%d: correction manquante" % (idx, j))
    types = [b.get("type") for b in f["affichage"]]
    if types != BLOCS_ATTENDUS:
        errs.append("fiche %d: blocs %s" % (idx, types))
    if not 2 <= len(f["schema"]) <= 4:
        errs.append("fiche %d: %d schemas" % (idx, len(f["schema"])))
    for j, sc in enumerate(f["schema"]):
        svg = sc.get("svg", "")
        if INTERDIT_SVG.search(svg):
            errs.append("fiche %d schema %d: SVG interdit" % (idx, j))
        try:
            root = ET.fromstring(svg)
        except ET.ParseError as e:
            errs.append("fiche %d schema %d: SVG invalide %s" % (idx, j, e))
            continue
        vb = [float(x) for x in root.get("viewBox", "0 0 660 100").split()]
        for txt in root.iter("{http://www.w3.org/2000/svg}text"):
            try:
                x = float(txt.get("x", 0)); y = float(txt.get("y", 0))
            except ValueError:
                errs.append("fiche %d schema %d: coordonnee texte" % (idx, j)); continue
            if not (0 <= x <= vb[2] and 0 <= y <= vb[3] + 4):
                errs.append("fiche %d schema %d: texte hors cadre (%s,%s)" % (idx, j, x, y))
    s = json.dumps(f, ensure_ascii=False)
    if CJK.search(s):
        errs.append("fiche %d: artefacts CJK %s" % (idx, CJK.findall(s)[:4]))
    if len(f["titre"]) < 12:
        errs.append("fiche %d: titre trop court" % idx)
    return errs


def valider_et_ecrire(fiches, chemin):
    errs, vus = [], set()
    for i, f in enumerate(fiches):
        errs += valider_fiche(f, i)
        k = f["titre"].strip().lower()
        if k in vus:
            errs.append("fiche %d: doublon titre %s" % (i, f["titre"]))
        vus.add(k)
    if errs:
        print("ERREURS (%d) :" % len(errs))
        for e in errs[:80]:
            print(" -", e)
        raise SystemExit(1)
    with open(os.path.join(BASE, chemin), "w", encoding="utf-8") as fp:
        json.dump({"fiches": fiches}, fp, ensure_ascii=False, indent=2)
    nb_svg = sum(len(f["schema"]) for f in fiches)
    nb_q = sum(len(f["questions"]) for f in fiches)
    print("OK %s : %d fiches, %d points, %d questions, %d SVG" %
          (chemin, len(fiches), sum(len(f["points"]) for f in fiches), nb_q, nb_svg))
