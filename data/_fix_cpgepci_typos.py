# -*- coding: utf-8 -*-
import io
repl_all = {
    'un déplacement ordered de charges': 'un déplacement ordonné de charges',
    'La abondance': 'L\u2019abondance',
    'l\u2019hypothèse nuelle H': 'l\u2019hypothèse nulle H',
    'and causes of the subjunctive-like constructions after « suggest that »':
        'and the subjunctive after expressions such as « suggest that »',
    'Le doutee cartésien': 'Le doute cartésien',
    '( Descartes)': '(Descartes)',
    'les Quartiles': 'les quartiles',
    'un système économique': 'un système économique',
    'Quel est un instrument protectionniste': 'Quel est un instrument protectionniste',
    'Pour une proportion, l\u2019intervalle asymptotique':
        'Pour une proportion, l\u2019intervalle asymptotique',
    'on ne « accepte » jamais': 'on ne « accepte » jamais H₀',
}
for p in ['gen_cpgepci_A.py', 'gen_cpgepci_B.py', 'gen_cpgepci_C.py']:
    s = io.open(p, encoding='utf-8').read()
    for a, b in repl_all.items():
        s = s.replace(a, b)
    # replace accidental double "H₀ H₀" from prior rule
    s = s.replace('on ne « accepte » jamais H₀ H₀', 'on ne « accepte » jamais H₀')
    io.open(p, 'w', encoding='utf-8').write(s)
print('OK typos')
