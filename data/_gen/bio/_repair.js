const fs = require('fs');
const dir = 'C:/Users/samir/Desktop/ilane bis/nouveau-projet/fichelab/data/_gen/bio';
for (const name of fs.readdirSync(dir).filter(f => f.endsWith('.json'))) {
  const p = dir + '/' + name;
  let lines = fs.readFileSync(p, 'utf8').split('\n');
  let changed = 0;
  lines = lines.map(line => {
    let inStr = false, opens = 0, closes = 0, lastBracket = -1;
    for (let i = 0; i < line.length; i++) {
      const c = line[i];
      if (inStr) { if (c === '\\') i++; else if (c === '"') inStr = false; continue; }
      if (c === '"') { inStr = true; continue; }
      if (c === '{') opens++;
      if (c === '}') closes++;
      if (c === ']') lastBracket = i;
    }
    if (opens === closes + 1 && lastBracket > 0) {
      // insert a closing brace just before the last ']'
      return line.slice(0, lastBracket) + '}' + line.slice(lastBracket);
    }
    return line;
  });
  const out = lines.join('\n');
  try { const a = JSON.parse(out); console.log(name, 'OK', a.length, changed); fs.writeFileSync(p, out, 'utf8'); }
  catch (e) {
    console.log(name, 'STILL ERR', e.message);
    // show line around error
    const m = e.message.match(/position (\d+)/);
    if (m) { const i = +m[1]; console.log('  context:', JSON.stringify(out.slice(i - 100, i + 60))); }
  }
}
