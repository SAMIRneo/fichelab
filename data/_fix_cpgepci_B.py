# -*- coding: utf-8 -*-
import io
p = 'gen_cpgepci_B.py'
s = io.open(p, encoding='utf-8').read()
repl = {
    '\u9a8c\u8bc1': 'V\u00e9rification',
    'notations : modernisme': 'notions : modernisme',
    'la absurdit\u00e9': 'l\u2019absurdit\u00e9',
    'differentes m\u00e9thodes': 'diff\u00e9rentes m\u00e9thodes',
    'effet dominants': 'effet dominant',
    'enannotant': 'en annotant',
    'transitionser': 'transitionner',
    'b\u0142\u0119d': 'erreur',
    'arguements': 'arguments',
    'Unaction': 'Une action',
    'Le doubt': 'Le doute',
    'doubt m\u00e9thodique': 'doute m\u00e9thodique',
    'le doubt': 'le doute',
    'doute cart\u00e9sien': 'doute cart\u00e9sien',
    'doute': 'doute',
    'une questions': 'une question',
    'consid\u00e9rer comme libres': 'consid\u00e9rer comme libres',
    'ne peut \u00eatre ni': 'ne peut \u00eatre ni',
    'non violante': 'non violente',
    'consequences': 'cons\u00e9quences',
    '\u00e0 opposer': '\u00e0 opposer',
    'Le Philosophe': 'Le philosophe',
    '[\" Philosophe\"': '[\"Philosophe\"',
    'd\u00e9fenseur de la tyrannie sans expliquer le contrat': 'd\u00e9fenseur de la tyrannie sans expliquer le contrat',
    'excuses)': 'discutable)',
    'le monde est': 'le monde est',
    'Le texte est': 'Le texte est',
    'le texte': 'le texte',
}
for a, b in repl.items():
    s = s.replace(a, b)
io.open(p, 'w', encoding='utf-8').write(s)
print('OK replace')
