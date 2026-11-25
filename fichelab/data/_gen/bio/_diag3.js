const fs = require('fs');
const p = 'C:/Users/samir/Desktop/ilane bis/nouveau-projet/fichelab/data/_gen/bio/C_f1.json';
const s = fs.readFileSync(p, 'utf8').split('\n')[3];
let inStr = false, opens = [], closes = [];
for (let i = 0; i < s.length; i++) {
  const c = s[i];
  if (inStr) { if (c === '\\') i++; else if (c === '"') inStr = false; continue; }
  if (c === '"') { inStr = true; continue; }
  if (c === '{' || c === '[') opens.push(c + ':' + i);
  if (c === '}' || c === ']') closes.push(c + ':' + i);
}
console.log('opens', opens.length, 'closes', closes.length);
console.log('opens tail', opens.slice(-12).join(' '));
console.log('closes tail', closes.slice(-12).join(' '));
// find first mismatch by simulating
let st = [];
for (let i = 0; i < s.length; i++) {
  const c = s[i];
  if (inStr) { if (c === '\\') i++; else if (c === '"') inStr = false; continue; }
  if (c === '"') { inStr = true; continue; }
  if (c === '{' || c === '[') st.push(c);
  else if (c === '}' || c === ']') {
    const top = st.pop();
    const exp = c === '}' ? '{' : '[';
    if (top !== exp) { console.log('MISMATCH at', i, 'got', c, 'top', top, 'context', s.slice(i - 200, i + 20)); break; }
  }
}
