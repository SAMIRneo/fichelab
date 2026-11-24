# -*- coding: utf-8 -*-
"""Regenere les blocs de donnees inlines de index.html apres ajout d'une filiere.

A n'utiliser qu'apres validation des fichiers generes par valider_et_ecrire().
Trace les remplacements dans data/injection-report.txt.
"""
import glob
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(BASE, "..", "index.html")
REPORT = os.path.join(BASE, "injection-report.txt")

# Nouveaux fichiers de fiches prototype (hors modele et hors catalogue BIOALC deja integre).
NOUVEAUX = sorted(
    p for p in glob.glob(os.path.join(BASE, "*-mat-part-*.json"))
    if not p.endswith("-MODELE.json")
    and not os.path.basename(p).startswith(("bioalc-", "physchim-"))
)


def _filieres_nouvelles():
    """Filieres a convertir : those present in the generated prototype files."""
    out = {"bts-bio"}
    for p in NOUVEAUX:
        with open(p, encoding="utf-8") as f:
            for fc in json.load(f).get("fiches", []):
                out.update(fc.get("filieres", []))
    return sorted(out)


# Si non vide, seules ces filieres sont integrees (utile quand d'autres equipes ecrivent encore).
FILIERES_A_INTEGRER = ["generale", "bts-mco", "pass", "lic-droit"]

PROTO_FILIERES = (sorted({"bts-bio"} | set(FILIERES_A_INTEGRER))
                  if FILIERES_A_INTEGRER else _filieres_nouvelles())


def load(name):
    with open(os.path.join(BASE, name), encoding="utf-8") as f:
        return json.load(f)


def build_extra():
    """Reconstruit exactement la liste d'origine, plus les nouvelles fiches."""
    out = []
    for n in ["agent1-lycee.json", "agent2-commerce.json", "agent3-tech.json",
              "agent4-licences.json", "agent5-lycee-gaps.json", "agent6-sup-gaps.json"]:
        for f in load(n)["fiches"]:
            if not any(x == "bts-bio" for x in f.get("filieres", [])):
                out.append(f)
    for n in ["lead-general-final.json", "lead-mco-final.json"]:
        out += load(n)["fiches"]
    # Les filieres converties ne gardent que leurs fiches prototype dans le catalogue.
    out = [f for f in out if not any(x in PROTO_FILIERES for x in f.get("filieres", []))]
    for p in sorted(glob.glob(os.path.join(BASE, "bioalc-mat-part-*.json")) +
                    glob.glob(os.path.join(BASE, "physchim-part-*.json"))):
        with open(p, encoding="utf-8") as f:
            out += json.load(f)["fiches"]
    nouveaux = []
    for p in NOUVEAUX:
        with open(p, encoding="utf-8") as f:
            fiches = json.load(f)["fiches"]
        if FILIERES_A_INTEGRER:
            fiches = [fc for fc in fiches
                      if any(x in FILIERES_A_INTEGRER for x in fc.get("filieres", []))]
        nouveaux += fiches
    return out, nouveaux


def build_anciens():
    """Cles titre||source des anciennes fiches texte brut, par filiere prototype."""
    map_anciens = {}
    for fil in PROTO_FILIERES:
        keys = set()
        for n in ["agent1-lycee.json", "agent2-commerce.json", "agent3-tech.json",
                  "agent4-licences.json", "agent5-lycee-gaps.json", "agent6-sup-gaps.json",
                  "lead-general-final.json", "lead-mco-final.json", "lead-bio-final.json"]:
            for f in load(n)["fiches"]:
                if fil in f.get("filieres", []):
                    keys.add((f.get("titre", "") or "") + "||" + (f.get("source", "") or ""))
        map_anciens[fil] = sorted(keys)
    return map_anciens


def main():
    with open(APP, encoding="utf-8") as f:
        src = f.read()
    lines = src.split("\n")
    extra, nouveaux = build_extra()
    if not nouveaux:
        raise SystemExit("Aucune nouvelle fiche trouvee : verifier les fichiers generale-mat-part-*.json")
    extra += nouveaux

    # 1. EXTRA_FICHES (ligne unique)
    idx = next(i for i, l in enumerate(lines) if l.startswith("const EXTRA_FICHES = "))
    lignes_json = json.dumps(extra, ensure_ascii=False, separators=(",", ":"))
    lines[idx] = "const EXTRA_FICHES = " + lignes_json + ".map(function(x){"

    # 2. jeu de filieres converties + filtre
    i_est = next(i for i, l in enumerate(lines) if l.startswith("const estPrototype="))
    proto_decl = "const PROTO_FILIERES=new Set(%s);" % json.dumps(PROTO_FILIERES)
    i_proto = next((i for i, l in enumerate(lines) if l.startswith("const PROTO_FILIERES=")), None)
    if i_proto is None:
        lines.insert(i_est + 1, proto_decl)
    else:
        lines[i_proto] = proto_decl
    i_filtre = next((i for i, l in enumerate(lines) if "p.filiere!=='bts-bio'" in l), None)
    if i_filtre is not None:
        lines[i_filtre] = "    .filter(m=>!PROTO_FILIERES.has(p.filiere)||estPrototype(m))"

    # 3. migration : remplace tout le bloc ANCIENS_BIO ... nettoyerBioalc
    i_deb = next((i for i, l in enumerate(lines)
                  if l.startswith("/* Migration BIOALC") or l.startswith("/* Migration prototype")), None)
    if i_deb is None:
        raise SystemExit("Bloc de migration introuvable")
    i_theme = max(i for i, l in enumerate(lines) if "dataset.theme" in l)
    i_fin = i_theme - 1  # ligne "})();" juste avant le theme final
    map_anciens = build_anciens()
    bloc = [
        "/* Migration prototype : retrait des anciennes fiches « texte brut » enregistrees",
        "   pour les filieres converties. Titre ET source doivent correspondre exactement :",
        "   les fiches personnelles ne sont jamais touchees. */",
        "const ANCIENS_PAR_FILIERE=" + json.dumps(map_anciens, ensure_ascii=False,
                                                  separators=(",", ":")) + ";",
        "(function nettoyerPrototypes(){",
        "  Object.keys(ANCIENS_PAR_FILIERE).forEach(function(fil){",
        "    const anciens=new Set(ANCIENS_PAR_FILIERE[fil]);",
        "    const avant=D.fiches.length;",
        "    D.fiches=D.fiches.filter(f=>!(f.filiere===fil&&anciens.has((f.titre||'')+'||'+(f.source||''))));",
        "    if(D.fiches.length!==avant){",
        "      if(D.parcours&&!D.fiches.some(f=>f.id===D.parcours.ficheActive))D.parcours.ficheActive='';",
        "      save();",
        "    }",
        "  });",
        "  (function statutLu(){",
        "    let change=false;",
        "    D.fiches.forEach(f=>{",
        "      if(f.statut==='verifiee'||f.statut==='a-verifier'){f.statut=f.statut==='verifiee'?'lue':'a-lire';change=true}",
        "      (f.points||[]).forEach(pt=>{if(pt.statut==='verifiee'||pt.statut==='a-verifier'){pt.statut=pt.statut==='verifiee'?'lue':'a-lire';change=true}});",
        "    });",
        "    if(change)save();",
        "  })();",
        "  if(D.profil&&PROTO_FILIERES.has(D.profil.filiere)&&D.profil.onboarded){",
        "    const presents=new Set(D.fiches.map(f=>(f.titre||'')+'||'+(f.source||'')));",
        "    const ajoutees=fichesPour(D.profil).filter(f=>!presents.has(f.titre+'||'+f.source));",
        "    if(ajoutees.length){D.fiches.push(...ajoutees);save()}",
        "  }",
        "})();",
    ]
    lines[i_deb:i_fin + 1] = bloc

    with open(APP, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))

    nb_new_proto = sum(1 for f in nouveaux if f.get("affichage") and f.get("schema"))
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write("Fiches totales dans EXTRA_FICHES : %d\n" % len(extra))
        f.write("Nouvelles fiches ajoutees : %d (dont %d prototype)\n" % (len(nouveaux), nb_new_proto))
        f.write("Filieres converties : %s\n" % ", ".join(PROTO_FILIERES))
        f.write("Fichiers sources ajoutes : %s\n" % ", ".join(os.path.basename(p) for p in NOUVEAUX))
        for fil, keys in map_anciens.items():
            f.write("  %s : %d anciennes fiches texte brut retirees a la migration\n" % (fil, len(keys)))
    print(open(REPORT, encoding="utf-8").read())


if __name__ == "__main__":
    main()
