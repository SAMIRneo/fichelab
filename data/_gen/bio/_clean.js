const fs = require('fs');
const dir = 'C:/Users/samir/Desktop/ilane bis/nouveau-projet/fichelab/data/_gen/bio';
const reps = [
  ['levures非 Saccharomyces', 'levures non Saccharomyces'],
  ['很好的 présence des ferments', 'bonne présence des ferments'],
  ['léthicine', 'lécithine'],
  ['realiser', 'réaliser'],
  ['en cas de doubt', 'en cas de doute'],
  ['procedes', 'procédés'],
  ['qui抑制 les', 'qui inhibent les'],
  ['deux faces不同的 de chiffon', 'deux faces différentes du chiffon'],
  ['poudre dehydrated', 'poudre déshydratée'],
  ['Any number', "N'importe quel nombre"],
  ['diferents', 'différents'],
  [',非 conforme', ', non conforme'],
  ['alternance des principes actifs,策 de temps de contact', 'alternance des principes actifs, maîtrise du temps de contact'],
  ['contaminations récurrentes,altérations', 'contaminations récurrentes, altérations'],
  ['bâilles', 'bâtonnets'],
  ['procedures', 'procédures'],
  ['ou替代品 plus sûr', 'ou un colorant plus sûr'],
  ['nucléases,Conditions', 'nucléases, conditions'],
  ['la-glycérol', 'le glycérol'],
  ['les idées Rather que les mots', 'les idées plutôt que les mots'],
  ['la these', 'la thèse'],
  ['Interpretation :', 'Interprétation :'],
  ['非 conformité', 'non-conformité'],
  ['coefficient de-determination', 'coefficient de détermination'],
  ["Loi binomiale et计划 d'échantillonnage", "Loi binomiale et plan d'échantillonnage"],
  ['Unealanéique', 'Un camembert'],
  ['rendant le solution', 'rendant la solution'],
  ['la tampon', 'le tampon'],
  ['independamment', 'indépendamment'],
  ['du criticalité', 'de la criticité'],
  ['( ancienne version', '(ancienne version'],
  ['Comment réponse', 'Comment répondre'],
  ['sontPlus importantes', 'sont plus importantes'],
  ['equipement', 'équipement'],
  ['au dessus', 'au-dessus'],
  ['une non conformité', 'une non-conformité']
];
let total = 0;
for (const name of fs.readdirSync(dir).filter(f => f.endsWith('.json'))) {
  const p = dir + '/' + name;
  let s = fs.readFileSync(p, 'utf8');
  for (const [a, b] of reps) {
    if (a === b) continue;
    while (s.includes(a)) { s = s.split(a).join(b); total++; }
  }
  const cjk = s.match(/[\u4e00-\u9fff]+/g);
  if (cjk) console.log('REMAINING CJK in', name, cjk.slice(0, 10));
  try { JSON.parse(s); fs.writeFileSync(p, s, 'utf8'); }
  catch (e) { console.log('PARSE ERROR after clean', name, e.message); }
}
console.log('replacements:', total);
for (const name of fs.readdirSync(dir).filter(f => f.endsWith('.json'))) {
  const a = JSON.parse(fs.readFileSync(dir + '/' + name, 'utf8'));
  console.log(name, a.length);
}
