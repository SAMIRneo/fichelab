const fs = require('fs');
const p = 'C:/Users/samir/Desktop/ilane bis/nouveau-projet/fichelab/data/_gen/bio/C_f1.json';
let s = fs.readFileSync(p, 'utf8');
s = s.replace(/seconde méthode\."\]\}\s*\n\]\s*$/, 'seconde méthode."}]}\n]\n');
fs.writeFileSync(p, s, 'utf8');
try { const a = JSON.parse(s); console.log('PARSE OK', a.length, 'questions:', a.map(x => x.questions.length)); }
catch (e) { console.log('PARSE ERR', e.message); console.log(JSON.stringify(s.slice(-150))); }
