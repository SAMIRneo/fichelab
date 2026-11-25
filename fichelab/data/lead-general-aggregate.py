import json, os, re
BASE = os.path.dirname(os.path.abspath(__file__))
F, AN = [], []
for p in ['lead-general-partie-A.json', 'lead-general-partie-B.json',
          'lead-general-partie-C.json', 'lead-general-partie-D.json']:
    d = json.load(open(os.path.join(BASE, p), encoding='utf-8'))
    F += d['fiches']
    AN += d['annales']

# Validation
problems = []
cjk = re.compile(r'[\u4e00-\u9fff]')
for i, fc in enumerate(F):
    if not (8 <= len(fc['points']) <= 12):
        problems.append(f"fiche {i} points={len(fc['points'])}")
    if not (6 <= len(fc['questions']) <= 10):
        problems.append(f"fiche {i} questions={len(fc['questions'])}")
    for j, qq in enumerate(fc['questions']):
        if qq['type'] == 'qcm':
            if len(qq.get('options', [])) < 2:
                problems.append(f"fiche {i} q{j} options")
            if not isinstance(qq.get('correct'), int) or not (0 <= qq['correct'] < len(qq['options'])):
                problems.append(f"fiche {i} q{j} correct")
        elif qq['type'] == 'texte':
            if not qq.get('reponse') or not qq.get('correction'):
                problems.append(f"fiche {i} q{j} texte vide")
    for field in ['titre', 'source'] + fc['points']:
        pass
    s = json.dumps(fc, ensure_ascii=False)
    if cjk.search(s):
        problems.append(f"fiche {i} CJK: {cjk.findall(s)[:5]}")
for i, an in enumerate(AN):
    s = json.dumps(an, ensure_ascii=False)
    if cjk.search(s):
        problems.append(f"annale {i} CJK: {cjk.findall(s)[:5]}")
    if len(an.get('contenu', '')) < 150 or len(an.get('correction', '')) < 150:
        problems.append(f"annale {i} trop courte")

print('FICHES:', len(F), 'ANNALES:', len(AN))
print('PROBLEMES:', len(problems))
for p in problems[:40]:
    print(' -', p)

out = os.path.join(BASE, 'lead-general-final.json')
with open(out, 'w', encoding='utf-8') as fp:
    json.dump({'fiches': F, 'annales': AN}, fp, ensure_ascii=False, indent=2)
print('ECRIT:', out, os.path.getsize(out), 'octets')
