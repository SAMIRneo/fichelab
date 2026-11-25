const fs = require('fs');
const p = 'C:/Users/samir/Desktop/ilane bis/nouveau-projet/fichelab/data/_gen/bio/C_f1.json';
let lines = fs.readFileSync(p, 'utf8').split('\n');
for (let i = 3; i <= 8; i++) {
  let l = lines[i];
  const m = l.match(/"\]\},\s*$/);
  if (m) {
    lines[i] = l.replace(/"\]\},\s*$/, '"}]},\n');
    console.log('fixed line', i + 1);
  } else {
    console.log('NO MATCH line', i + 1, JSON.stringify(l.slice(-30)));
  }
}
fs.writeFileSync(p, lines.join('\n'), 'utf8');
try { const a = JSON.parse(fs.readFileSync(p, 'utf8')); console.log('PARSE OK', a.length); }
catch (e) { console.log('PARSE ERR', e.message); }
