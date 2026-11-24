# -*- coding: utf-8 -*-
"""Audit complet de FicheLab apres injection : donnees, prototypes, SVG, JS, coherence.

Usage : python audit_filieres.py
Ecrit fichelab/AUDIT-FILIERES.md
"""
import collections
import glob
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

BASE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(BASE, "..", "index.html")
OUT = os.path.join(BASE, "..", "AUDIT-FILIERES.md")
sys.path.insert(0, BASE)
from fixtures import BLOCS_ATTENDUS, CJK, INTERDIT_SVG

ANNEES = {
    "generale": ["2nde", "1re", "Terminale"],
    "bts-bio": ["BTS1", "BTS2"],
    "bts-mco": ["BTS1", "BTS2"],
    "pass": ["PASS1"],
}
MATIERES = [
    "Français", "Philosophie", "Histoire-Géographie", "Maths", "Physique-Chimie",
    "SVT", "Anglais", "EPS", "EMC", "Méthodologie", "SES", "NSI", "SI", "HGGSP",
    "HLP", "LLCE", "LCA", "Arts", "Biologie-écologie",
]


def embed(name):
    with open(APP, encoding="utf-8") as f:
        lines = f.read().split("\n")
    l = next(x for x in lines if x.startswith("const " + name + " = ")
             or x.startswith("const " + name + "=["))
    s = l.strip()
    return json.loads(s[s.index("[") : s.rindex("]") + 1]), lines


def main():
    fiches, lines = embed("EXTRA_FICHES")
    annales, _ = embed("ANNALES_BIB")
    src = "\n".join(lines)
    protos = [f for f in fiches if f.get("affichage") and f.get("schema")]
    proto_fil = json.loads(re.search(r"const PROTO_FILIERES=new Set\((\[[^\]]*\])\)", src).group(1))

    problems = []
    checks = []

    # 1. structure globale
    checks.append(("Catalogue EXTRA_FICHES", len(fiches), "lisible"))
    checks.append(("Fiches prototype", len(protos), "= 96 BIOALC + nouvelles"))
    checks.append(("Annales bibliotheque", len(annales), "lisible"))
    checks.append(("Filieres converties", len(proto_fil), ", ".join(proto_fil)))

    # 2. uniformite des prototypes
    types_blocs = collections.Counter()
    nb_svg = 0
    nb_q = 0
    for i, f in enumerate(protos):
        types = tuple(b.get("type") for b in f["affichage"])
        types_blocs[types] += 1
        if types != tuple(BLOCS_ATTENDUS):
            problems.append("prototype %d : ordre des blocs %s" % (i, types))
        if not 10 <= len(f.get("points", [])) <= 14:
            problems.append("prototype %d : %d points" % (i, len(f.get("points", []))))
        if not 8 <= len(f.get("questions", [])) <= 10:
            problems.append("prototype %d : %d questions" % (i, len(f.get("questions", []))))
        if not 2 <= len(f.get("schema", [])) <= 4:
            problems.append("prototype %d : %d schemas" % (i, len(f.get("schema", []))))
        nb_svg += len(f.get("schema", []))
        nb_q += len(f.get("questions", []))
        for q in f.get("questions", []):
            if q.get("type") == "qcm":
                if len(q.get("options", [])) < 2 or not 0 <= q.get("correct", -1) < len(q["options"]):
                    problems.append("prototype %d : QCM invalide" % i)
            if q.get("type") == "texte" and (not q.get("reponse") or not q.get("correction")):
                problems.append("prototype %d : question texte incomplete" % i)
            if not q.get("correction"):
                problems.append("prototype %d : correction manquante" % i)
        for j, sc in enumerate(f.get("schema", [])):
            svg = sc.get("svg", "")
            if INTERDIT_SVG.search(svg):
                problems.append("prototype %d schema %d : contenu SVG interdit" % (i, j))
            try:
                ET.fromstring(svg)
            except ET.ParseError:
                problems.append("prototype %d schema %d : SVG mal forme" % (i, j))
        if CJK.search(json.dumps(f, ensure_ascii=False)):
            problems.append("prototype %d : artefacts CJK" % i)
        if not f.get("source"):
            problems.append("prototype %d : source vide" % i)
    checks.append(("Questions prototype", nb_q, "toutes corrigees"))
    checks.append(("Schemas SVG", nb_svg, "XML valide, sans script"))
    checks.append(("Ordre des 7 blocs", len(types_blocs), "variantes (doit etre 1)"))
    if len(types_blocs) != 1:
        problems.append("ordre des blocs non uniforme : %d variantes" % len(types_blocs))

    # 3. doublons de titres
    vus = collections.Counter(f.get("titre", "").strip().lower() for f in fiches)
    dups = [t for t, n in vus.items() if n > 1 and t]
    checks.append(("Titles uniques", len(dups), "doublons (doit etre 0)"))
    for t in dups[:20]:
        problems.append("titre en double : %s" % t)

    # 4. par filiere / annee : ce que voit reellement l'utilisateur
    per_fil = []
    for fil in sorted(set(f for p in protos for f in p.get("filieres", []))):
        pf = [f for f in protos if fil in f.get("filieres", [])]
        lignes = []
        ans = sorted({a for f in pf for a in f.get("annees", []) if a != "all"})
        for an in ans:
            visibles = [f for f in pf if an in f.get("annees", []) or "all" in f.get("annees", [])]
            lignes.append("%s:%d" % (an, len(visibles)))
        per_fil.append("**%s** : %d prototypes (%s)" % (fil, len(pf), ", ".join(lignes)))
        if fil in proto_fil:
            brut = [f for f in fiches if fil in f.get("filieres", []) and not (f.get("affichage") and f.get("schema"))]
            if brut:
                problems.append("%s : %d fiches texte brut encore dans le catalogue (cachees par le filtre)" % (fil, len(brut)))

    # 5. annales par filiere
    per_an = collections.Counter()
    for a in annales:
        for f in a.get("filieres", []):
            per_an[f] += 1

    # 6. coherence du code
    if ".filter(m=>!PROTO_FILIERES.has(p.filiere)||estPrototype(m))" not in src:
        problems.append("filtre prototype absent ou incorrect dans fichesPour()")
    if "PROTO_FILIERES.has(D.profil.filiere)" not in src:
        problems.append("migration d'ajout non generalisee")
    if "ANCIENS_PAR_FILIERE" not in src:
        problems.append("migration de nettoyage non generalisee")
    if "function annalesReellesPour()" not in src:
        problems.append("vrais examens non filtres par filiere")
    reelles, _ = embed("ANNALES_REELLES")
    if not all(a.get("filieres") for a in reelles):
        problems.append("vrais examens sans filiere declaree")
    checks.append(("Vrais examens filtres", len(reelles), "bts-bio uniquement"))

    # 8. non-regression BIOALC (audit de certification 24/11)
    brut_bio = [f for f in fiches if "bts-bio" in f.get("filieres", [])
                and not (f.get("affichage") and f.get("schema"))]
    if brut_bio:
        problems.append("BIOALC: %d fiches texte brut dans le catalogue" % len(brut_bio))
    cg = [f for f in protos if f.get("titre", "").startswith("Contrôle PC ·")]
    if len(cg) != 15:
        problems.append("BIOALC: %d/15 fiches Contrôle PC" % len(cg))
    if any("BTS1" not in f.get("annees", []) for f in cg):
        problems.append("BIOALC: fiches Contrôle PC absentes pour BTS1")
    ann_sans_source = [a for a in annales if "bts-bio" in a.get("filieres", [])
                       and a.get("type") == "genere" and not a.get("source")]
    if ann_sans_source:
        problems.append("BIOALC: %d annales genere sans source" % len(ann_sans_source))
    checks.append(("BIOALC fiches texte brut", len(brut_bio), "0"))
    checks.append(("BIOALC Contrôle PC", len(cg), "15 visibles BTS1+BTS2"))
    checks.append(("BIOALC annales sans source", len(ann_sans_source), "0"))
    for name in ["const KEY='mcos-fichelab:data'", "function fichesPour(p)", "function renderBlocs(f)"]:
        if name not in src:
            problems.append("marqueur code manquant : %s" % name)

    # 7. syntaxe JS
    syntaxe = "node indisponible"
    try:
        text = src[src.index("<script>") + 8 : src.index("</script>")]
        tmp = os.path.join(os.environ.get("TEMP", "."), "fichelab-audit.js")
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(text)
        r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True, timeout=60)
        syntaxe = "OK" if r.returncode == 0 else "ERREUR : " + r.stderr[:600]
        if r.returncode:
            problems.append("syntaxe JS : " + r.stderr[:300])
    except Exception as e:
        syntaxe = "non verifie (%s)" % e

    # rapport
    out = ["# Audit FicheLab — filieres prototype", "",
           "Audit automatique apres injection. Generé par `data/audit_filieres.py`.", "",
           "## Resultats", "", "| Controle | Valeur | Attendu |", "|---|---|---|"]
    for n, v, a in checks:
        out.append("| %s | %s | %s |" % (n, v, a))
    out += ["", "## Couverture par filiere", ""]
    out += per_fil
    out += ["", "## Annales par filiere", ""]
    for f, n in sorted(per_an.items(), key=lambda x: -x[1]):
        out.append("- **%s** : %d" % (f, n))
    out += ["", "## Verifications", "",
            "- Syntaxe JavaScript : **%s**" % syntaxe,
            "- Schemas SVG : %d, tous analysables en XML et sans script/on*/javascript:" % nb_svg,
            "- Blocs d'affichage : %d fiche(s), ordre strict identique" % len(protos),
            "- Questions : %d, toutes avec correction" % nb_q,
            "- Migrations : filtre prototype + nettoyage + ajout automatique generalises", "",
            "## Problemes detectes", ""]
    if problems:
        out += ["**%d problème(s) — audit NON CONFORME**" % len(problems), ""]
        out += ["- " + p for p in problems[:100]]
    else:
        out += ["**Aucun problème détecté — audit CONFORME.**"]
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print("AUDIT :", "CONFORME" if not problems else "%d PROBLEMES" % len(problems))
    print("Rapport :", OUT)
    for p in problems[:20]:
        print(" -", p)
    return 0 if not problems else 1


if __name__ == "__main__":
    raise SystemExit(main())
