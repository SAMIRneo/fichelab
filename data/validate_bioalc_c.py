# -*- coding: utf-8 -*-
import json, re, xml.etree.ElementTree as ET
p = 'bioalc-mat-part-C.json'
d = json.load(open(p, encoding='utf-8'))
fs = d['fiches']
print('fiches:', len(fs))
assert len(fs) == 15
ids = []
for i, f in enumerate(fs, 1):
    for k in ('filieres','annees','matiere','titre','source','points','questions','affichage','schema'):
        assert k in f, (i,k)
    assert f['filieres'] == ['bts-bio']
    assert 8 <= len(f['points']) <= 12, (i,'points',len(f['points']))
    assert len(f['questions']) == 10, (i,'questions')
    assert len(f['affichage']) == 7, (i,'affichage')
    assert 2 <= len(f['schema']) <= 3, (i,'schema')
    calc = [q for q in f['questions'] if q.get('calcul') and q.get('contexte')]
    assert len(calc) >= 2, (i,'calc+ctx',len(calc))
    for q in f['questions']:
        assert q['type'] in ('qcm','texte'), (i,q['type'])
        if q['type']=='qcm':
            assert 0 <= q['correct'] < len(q['options']), (i,'correct')
        else:
            assert q.get('reponse'), (i,'reponse')
    types = [b['type'] for b in f['affichage']]
    assert set(types) == {'intro','formule','grille','liste','etapes','attention','exemples'}, (i,types)
    for s in f['schema']:
        assert s['titre'] and s['svg'].startswith('<svg'), (i,'svg')
        # XML well-formedness
        try:
            ET.fromstring(s['svg'])
        except Exception as e:
            print('XML ERROR fiche',i,s['titre'],e)
            raise
        for m in re.findall(r'\bid="([^"]+)"', s['svg']):
            ids.append(m)
        for ref in re.findall(r'url\(#([^)]+)\)', s['svg']):
            assert ref in re.findall(r'\bid="([^"]+)"', s['svg']), (i,'dangling ref',ref)
print('svg id total:', len(ids), 'uniques:', len(set(ids)))
assert len(ids) == len(set(ids)), 'duplicate SVG ids'
print('bioC ids:', sorted(set(x for x in ids if x.startswith('bioC')))[:8], '...')
from collections import Counter
print('matieres:', Counter(f['matiere'] for f in fs))
print('annees:', Counter(tuple(f['annees']) for f in fs))
print('ALL CHECKS PASSED')
