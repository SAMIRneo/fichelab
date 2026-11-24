import glob, os
BASE = os.path.dirname(os.path.abspath(__file__))
for path in glob.glob(os.path.join(BASE, "lead-general-partie-*.py")):
    with open(path, encoding="utf-8") as fp:
        lines = fp.readlines()
    out = []
    n = 0
    for line in lines:
        if line.lstrip().startswith('q("'):
            idx = line.find(', ["')
            if idx > 0 and line[idx - 1] != '"':
                line = line[:idx] + '"' + line[idx:]
                n += 1
        out.append(line)
    with open(path, "w", encoding="utf-8") as fp:
        fp.writelines(out)
    print(os.path.basename(path), n)
