const fs = require('fs');
const a = JSON.parse(fs.readFileSync('C:/Users/samir/Desktop/ilane bis/nouveau-projet/fichelab/data/lead-bio-final.json','utf8'));
a.fiches.forEach((f,i)=>console.log(String(i+1).padStart(2), f.annees.join('/'), '|', f.matiere, '|', f.titre));
console.log('--- ANNALES ---');
a.annales.forEach((x,i)=>console.log(String(i+1).padStart(2), x.matiere, '|', x.titre));
