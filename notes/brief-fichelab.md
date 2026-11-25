# Brief structuré — FicheLab (niveau 2)

> Ceci est le **modèle A rempli**. C'est la différence entre « fais-moi une app de fiches » et un vrai brief.

```
RÔLE : Tu es un développeur qui crée des applis web 100 % locales en un seul fichier HTML.
       Tu sais aussi concevoir un parcours d'apprentissage pour lycéens et étudiants.

OBJECTIF : Crée FicheLab, une appli de révision qui rassemble des fiches, pose des questions,
           génère des examens à partir d'annales et mesure le temps de travail.
           L'appli doit convenir à TOUS les types d'élèves / étudiants, pas à une seule personne.

CONTEXTE :
- Je suis étudiant en BTS bioanalyse / labo de contrôle (19 ans), mais l'appli doit
  fonctionner pour le lycée ET les études supérieures.
- Matières à couvrir (exemples, à adapter selon le niveau et la filière) :
  biochimie / analyses, microbiologie, chimie, biologie cellulaire, hématologie,
  immunologie, normes et réglementation, maths / stats / physique, français / anglais / gestion.
- L'appli doit s'adapter à la personne dès l'ouverture via un PETIT QUESTIONNAIRE :
  âge, niveau (lycée / sup), filière, classe, matières suivies, objectif de temps par jour,
  et style de révision (lecture / cartes / quiz). Le reste de l'appli s'adapte aux réponses.
- Je ne révise pas beaucoup moi-même : l'appli doit donc être motivante et utilisable
  par quelqu'un qui part de zéro comme par quelqu'un qui révise déjà beaucoup.
- Sources possibles pour les fiches : PDF / scans, photos, papier manuscrit, ou rien du tout.

FONCTIONNALITÉS ATTENDUES :
1. Un catalogue de fiches de départ, généré par toi, classé par filière → niveau → matière.
2. L'ajout de MES fiches (texte collé, ou photo / PDF gardés comme référence).
3. Une RÈGLE D'OR : chaque information doit être VÉRIFIABLE.
   -> Chaque fiche et chaque point porte un statut : « à vérifier » ou « vérifiée »,
      une source (cours, annale, site, livre) et une date.
   -> Une fiche générée démarre TOUJOURS en « à vérifier » et ne passe en « vérifiée »
      que quand l'utilisateur la valide explicitement.
4. Trois façons de réviser : lire la fiche, retourner des cartes mémoire, répondre à des questions.
5. Un mode EXAMEN : chronomètre, note sur 20, correction expliquée, historique des scores.
   Les questions viennent de trois sources :
   - exercices générés à partir des fiches vérifiées,
   - annales en ligne (liens cherchés selon la matière et le niveau),
   - MES contrôles importés (texte collé + photo / PDF en référence).
6. Suivi du temps : temps par fiche, temps par matière, temps total par jour avec série,
   courbe de progression sur plusieurs semaines.

LIMITE TECHNIQUE À RESPECTER ET À M'EXPLIQUER :
- L'app est un seul fichier HTML, hors ligne, sans backend.
- Elle peut STOCKER et AFFICHER une photo ou un PDF importé, mais elle ne sait pas
  transformer un scan en texte (pas d'OCR hors ligne).
  -> Prévoir un bouton « Extraire le texte avec l'IA » qui affiche un prompt à copier
     dans une IA, puis un champ pour recoller le texte vérifié. C'est cohérent avec mon
     objectif : apprendre à utiliser l'IA.

CONTRAINTES :
- Un seul fichier index.html, zéro dépendance, zéro CDN, zéro backend
- Données en localStorage avec le préfixe mcos-fichelab:
- Export/import JSON au format de la charte (app / version / exportedAt / data)
- Deux couleurs seulement (--bg et --ac), mode clair et sombre
- Français tutoyé, cibles tactiles >= 44 px, :focus-visible, aria-* sur les dialogues
- Aucun compte obligatoire, ça marche hors ligne

LIVRABLE :
1. Le dossier nouveau-projet/fichelab/ avec index.html + manifest + icône + README.md
2. Un README qui dit où sont les données, quelle est la fonction centrale, et ce que je vérifie
3. Mettre à jour apps.json avec FicheLab
4. Une ligne dans notes/journal.md : ce que j'ai appris à faire avec l'IA à ce niveau
```

## Ce que ce brief montre (niveau 2)

Par rapport à un prompt vague, j'ai :
- **donné un rôle** à l'IA (développeur + concepteur pédagogique) ;
- **décrit le contexte réel** (BTS, lycée, sup, mes matières) ;
- **posé une règle produit vérifiable** (le statut « à vérifier ») ;
- **reconnu une limite technique** et demandé une solution adaptée (le prompt d'extraction) ;
- **fixé le format de sortie** (fichiers attendus + mises à jour).

C'est ça, « savoir utiliser l'IA » : cadrer, vérifier, et garder la main.
