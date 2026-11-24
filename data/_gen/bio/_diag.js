const fs = require('fs');
const p = 'C:/Users/samir/Desktop/ilane bis/nouveau-projet/fichelab/data/_gen/bio/C_f1.json';
const lines = fs.readFileSync(p, 'utf8').split('\n');
lines.forEach((line, i) => {
  const k = line.indexOf('"questions"');
  console.log('LINE', i + 1, 'questions at', k, 'len', line.length);
  if (k > 0) console.log('  context:', line.slice(k - 80, k + 60));
});
for (let i = 1; i <= 9; i++) {
  try { JSON.parse(lines[i - 1]); console.log('line', i, 'OK'); }
  catch (e) { console.log('line', i, 'ERR', e.message); }
}
