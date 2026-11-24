const fs = require('fs');
const p = 'C:/Users/samir/Desktop/ilane bis/nouveau-projet/fichelab/data/_gen/bio/C_f1.json';
const lines = fs.readFileSync(p, 'utf8').split('\n');
for (const n of [2, 3, 4, 5, 6, 7, 8, 9]) {
  const s = lines[n - 1];
  let depth = 0, inStr = false, i = 0;
  const stack = [];
  for (; i < s.length; i++) {
    const c = s[i];
    if (inStr) { if (c === '\\') { i++; continue; } if (c === '"') inStr = false; continue; }
    if (c === '"') { inStr = true; continue; }
    if (c === '{' || c === '[') { stack.push({ c, i }); }
    else if (c === '}' || c === ']') { stack.pop(); }
  }
  console.log('LINE', n, 'stack', stack.map(x => x.c + '@' + x.i).join(' '), 'inStr', inStr);
  if (stack.length) {
    const last = stack[stack.length - 1];
    console.log('   near last:', s.slice(last.i - 120, last.i + 60));
  }
}
