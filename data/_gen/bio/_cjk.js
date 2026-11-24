const fs = require('fs');
const dir = 'C:/Users/samir/Desktop/ilane bis/nouveau-projet/fichelab/data/_gen/bio';
for (const name of ['A_f2.json', 'D_f4.json']) {
  let s = fs.readFileSync(dir + '/' + name, 'utf8');
  const m = s.match(/[\u4e00-\u9fff]+/g);
  if (m) for (const token of new Set(m)) {
    const i = s.indexOf(token);
    console.log(name, token, JSON.stringify(s.slice(i - 60, i + 60)));
    s = s.split(token).join(token === '比例' ? 'proportion' : 'résultats');
  }
  try { JSON.parse(s); fs.writeFileSync(dir + '/' + name, s, 'utf8'); console.log(name, 'cleaned OK'); }
  catch (e) { console.log('ERR', e.message); }
}
