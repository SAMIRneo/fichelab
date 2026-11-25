const fs = require('fs');
const dir = 'C:/Users/samir/Desktop/ilane bis/nouveau-projet/fichelab/data';
const gen = dir + '/_gen/bio';
const groups = {
  A: { fiches: ['A_f1.json', 'A_f2.json'], annales: ['A_an.json'] },
  B: { fiches: ['B_f1.json', 'B_f2.json'], annales: ['B_an.json'] },
  C: { fiches: ['C_f1.json', 'C_f2.json'], annales: ['C_an.json'] },
  D: { fiches: ['D_f1.json', 'D_f2.json', 'D_f3.json', 'D_f4.json'], annales: ['D_an.json'] }
};
const read = f => JSON.parse(fs.readFileSync(gen + '/' + f, 'utf8'));
const allFiches = [], allAnnales = [];
for (const [key, g] of Object.entries(groups)) {
  const fiches = g.fiches.flatMap(read);
  const annales = g.annales.flatMap(read);
  fs.writeFileSync(dir + '/lead-bio-partie-' + key + '.json', JSON.stringify({ fiches, annales }, null, 1) + '\n', 'utf8');
  allFiches.push(...fiches);
  allAnnales.push(...annales);
}
const final = { fiches: allFiches, annales: allAnnales };
fs.writeFileSync(dir + '/lead-bio-final.json', JSON.stringify(final, null, 1) + '\n', 'utf8');

// strict validation
const errors = [];
const FKEYS = ['filieres','annees','matiere','titre','source','points','questions'];
const QKEYS = ['type','q','correction'];
allFiches.forEach((f, i) => {
  FKEYS.forEach(k => { if (!(k in f)) errors.push(`fiche ${i}: missing ${k}`); });
  if (JSON.stringify(f.filieres) !== '["bts-bio"]') errors.push(`fiche ${i}: filieres`);
  if (!Array.isArray(f.annees) || f.annees.length === 0) errors.push(`fiche ${i}: annees`);
  if (f.points.length < 8 || f.points.length > 12) errors.push(`fiche ${i}: points=${f.points.length}`);
  if (f.questions.length < 6 || f.questions.length > 10) errors.push(`fiche ${i}: questions=${f.questions.length}`);
  f.questions.forEach((q, j) => {
    QKEYS.forEach(k => { if (!(k in q)) errors.push(`fiche ${i} q${j}: missing ${k}`); });
    if (!['qcm','rédaction'].includes(q.type)) errors.push(`fiche ${i} q${j}: type=${q.type}`);
    if (q.type === 'qcm') {
      if (!Array.isArray(q.options) || q.options.length < 3) errors.push(`fiche ${i} q${j}: options`);
      if (!Number.isInteger(q.correct) || q.correct < 0 || q.correct >= q.options.length) errors.push(`fiche ${i} q${j}: correct index`);
    }
    if (!q.correction || q.correction.length < 20) errors.push(`fiche ${i} q${j}: correction too short`);
  });
  if (!/Arrêté du 12 mars 2024/.test(f.source)) errors.push(`fiche ${i}: source missing arrete`);
});
allAnnales.forEach((a, i) => {
  ['filieres','annees','titre','matiere','type','contenu','correction'].forEach(k => {
    if (!(k in a)) errors.push(`annale ${i}: missing ${k}`);
  });
  if (JSON.stringify(a.filieres) !== '["bts-bio"]') errors.push(`annale ${i}: filieres`);
  if (a.contenu.length < 300) errors.push(`annale ${i}: contenu too short (${a.contenu.length})`);
  if (a.correction.length < 500) errors.push(`annale ${i}: correction too short (${a.correction.length})`);
});
console.log('FICHES:', allFiches.length, 'ANNALES:', allAnnales.length);
console.log('points min/max:', Math.min(...allFiches.map(f=>f.points.length)), Math.max(...allFiches.map(f=>f.points.length)));
console.log('questions min/max:', Math.min(...allFiches.map(f=>f.questions.length)), Math.max(...allFiches.map(f=>f.questions.length)));
console.log('matieres:', [...new Set(allFiches.map(f=>f.matiere))].join(' | '));
console.log('errors:', errors.length);
errors.slice(0, 30).forEach(e => console.log('  -', e));
