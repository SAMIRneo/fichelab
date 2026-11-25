import glob, os
BASE = os.path.dirname(os.path.abspath(__file__))

def fix_q(line):
    s = line.rstrip('\n')
    stripped = s.lstrip()
    if not stripped.startswith('q("'):
        return line
    start = s.index('q("') + 3
    i = start
    while i < len(s):
        if s[i] == '\\':
            i += 2
            continue
        if s[i] == '"':
            break
        i += 1
    if i >= len(s):
        return line
    j = i + 1
    while j < len(s) and s[j] in ' \t':
        j += 1
    if j >= len(s) or s[j] != ',':
        return line
    j += 1
    while j < len(s) and s[j] in ' \t':
        j += 1
    if j < len(s) and s[j] == '"':
        s = s[:i] + ', ["' + s[j + 1:]
    return s + '\n'

for path in glob.glob(os.path.join(BASE, "lead-general-partie-*.py")):
    with open(path, encoding='utf-8') as fp:
        lines = fp.readlines()
    out = [fix_q(l) for l in lines]
    text = ''.join(out).replace('\n]),', '\n])),')
    with open(path, 'w', encoding='utf-8') as fp:
        fp.write(text)
    print('fixed', os.path.basename(path))
