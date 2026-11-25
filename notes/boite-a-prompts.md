# ⌨️ Boîte à prompts — mes 6 modèles prêts à copier

> Remplace ce qui est entre crochets `[…]`, puis colle le texte directement dans l'IA (OpenCode, Claude, ChatGPT…).
> Tous les modèles renvoient vers `CHARTE.md` pour garder les applis compatibles entre elles.

---

## Modèle A — Le brief structuré (niveau 2 → FicheLab)

```
RÔLE : Tu es un développeur qui crée des applis web 100 % locales en un seul fichier HTML.

OBJECTIF : Crée [NOM DE L'APPLI] qui sert à [BUT EN UNE PHRASE].

CONTEXTE : Je suis étudiant en BTS bioanalyse en labo de contrôle. Je vais utiliser cette appli pour [SITUATION RÉELLE, ex. : réviser mes fiches entre deux TP]. Elle fait partie de mon microcosme : lis nouveau-projet/CHARTE.md et respecte-la.

CONTRAINTES :
- Un seul fichier index.html, zéro dépendance, zéro CDN
- Données en localStorage avec le préfixe mcos-[app]:
- Export/import JSON au format de la charte
- Deux couleurs seulement (--bg et --ac), mode clair et sombre
- Français tutoyé, cibles tactiles >= 44 px
- Aucun compte obligatoire, ça marche hors ligne

LIVRABLE :
1. Le dossier nouveau-projet/[app]/ avec index.html
2. Un README.md qui dit ce que fait l'appli et la clé de stockage utilisée
3. Une liste de 3 choses que je dois vérifier en testant
```

---

## Modèle B — La spec d'abord (niveau 3 → CheckTP)

```
ÉTAPE 1 — N'écris pas encore de code.
Rédige d'abord la mini-spec de [NOM DE L'APPLI] qui sert à [BUT].
Présente-la en 4 blocs :
- Les données : quels champs, quels types
- Les écrans : 3 maximum, avec ce qu'on voit dessus
- Les règles : 5 règles de fonctionnement
- Les cas limites : 3 situations bizarres à prévoir

Montre-moi cette spec et ATTENDS mon OK. Je la corrigerai avec mes mots de étudiant en bio.

ÉTAPE 2 — Quand j'aurai dit « vas-y », code exactement cette spec en respectant nouveau-projet/CHARTE.md.
```

---

## Modèle C — La boucle de critique (niveau 4 → AgendaUE)

```
Tu viens de coder [NOM DE L'APPLI]. Maintenant, CHANGE DE CASQUETTE.

Tu es un reviewer indépendant et sévère. Ne sois pas gentil.

1. Relis ton propre code et trouve 5 problèmes (bugs, erreurs de calcul, confusion possible pour un étudiant, soucis d'accessibilité).
2. Classe-les par gravité : CRITIQUE / MOYEN / MINEUR.
3. Corrige les 3 plus graves.
4. Rejoue ce scénario de test : [EX. : j'ajoute une note avec un coefficient, je change la note, je vérifie que la moyenne se met à jour].
5. Dis-moi ce qui reste non corrigé et pourquoi.
```

Variante utile : *« Donne-moi 3 versions différentes de l'écran [X]. Explique en une phrase la différence entre les trois, sans choisir à ma place. »*

---

## Modèle D — Le gabarit réutilisable (niveau 5 → CalcLab)

```
Crée un GABARIT DE PROMPT réutilisable pour mon microcosme.

Il doit contenir 4 variables que je remplirai à chaque fois :
[NOM] [BUT] [DONNÉES] [ÉCRANS]

Il doit intégrer en dur toutes les contraintes de nouveau-projet/CHARTE.md (un fichier, préfixe mcos-, export JSON, 2 couleurs, français, accessibilité).

Écris ce gabarit dans nouveau-projet/notes/boite-a-prompts.md sous le nom « Modèle E — gabarit personnel ».

Ensuite, utilise-le en remplissant les 4 variables pour générer CalcLab (une appli de dilutions, concentrations et conversions pour le labo).
```

---

## Modèle E — Gabarit personnel (généré à l'étape 5)

> Laisse cette section vide pour l'instant. Elle sera remplie par l'IA au niveau 5.

---

## Modèle F — L'orchestration (niveau 6 → Launcher)

```
Voici nouveau-projet/CHARTE.md et la liste de mes 5 applis : Élan, FicheLab, CheckTP, AgendaUE, CalcLab.

Je ne te demande plus de coder une appli. Je te demande de piloter le SYSTÈME.

1. Crée le Launcher : une page qui lit apps.json et affiche toutes mes applis avec leur nom, leur description, leur icône et leur couleur.
2. Mets à jour apps.json avec les 5 applis.
3. Écris un guide intitulé « Créer sa propre appli du microcosme en 5 étapes », avec mes modèles de prompts, que je puisse donner à quelqu'un d'autre.
4. Vérifie que chaque appli respecte encore la charte et signale celles qui dévient.
```

---

## Astuces pour tous les niveaux

- **Donne un exemple réel** plutôt qu'un adjectif : « écris comme je parle à un prof » vaut mieux que « sois clair ».
- **Dis ce que tu ne veux pas** : « pas de framework », « pas de credits opaques », « pas de jargon ».
- **Demande des options, pas un choix** : « propose 3 variantes et explique » → tu gardes la main.
- **Quand ça ne convient pas, ne recommence pas from scratch** : dis *« reprends la partie X, elle était bonne, change seulement Y »*.
- **Réutilise toujours le même vocabulaire** d'une appli à l'autre. C'est comme ça que l'IA apprend ton style.
