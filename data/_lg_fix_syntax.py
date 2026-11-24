import re, glob, os
BASE = os.path.dirname(os.path.abspath(__file__))

REPL = {
 "子 font": " font",
 "代表 le rêve": "représente le rêve",
 "Honneth分析": "Honneth analyse",
 "comme弹性 de la raison": "comme élasticité de la raison",
 "émouvre": "émouvoir",
 "保护": "protection",
 "grandieure": "grandeur",
 "reception": "réception",
 "progress individualisés": "progrès individualisés",
 "specialité SES": "spécialité SES",
 "progress": "progrès",
 "calculee": "calculée",
 "développe": "développe",
 "On néglige": "On néglige",
 " dum": " du",
 "Une augmentation": "Une augmentation",
 "dépassement (par exemple": "dépassement (par exemple",
 " : ": " : ",
 "1":"1",
}
# suppress no-op entries
REPL = {k: v for k, v in REPL.items() if k != v}

pat = re.compile(r'^(\s*q\(")((?:[^"\\]|\\.)*)(", ")(.*)$')

for path in glob.glob(os.path.join(BASE, "lead-general-partie-*.py")):
    with open(path, encoding="utf-8") as fp:
        lines = fp.readlines()
    out = []
    for line in lines:
        m = pat.match(line.rstrip("\n"))
        if m:
            # malformed qcm: second argument begins with a quote -> insert '['
            line = m.group(1) + m.group(2) + ', ["' + m.group(4) + "\n"
        for k, v in REPL.items():
            line = line.replace(k, v)
        out.append(line)
    with open(path, "w", encoding="utf-8") as fp:
        fp.writelines(out)
    print("fixed", os.path.basename(path))
