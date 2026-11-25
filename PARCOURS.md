# Mon plan Microcosme — 5 applis, 6 niveaux d'IA

> Version 2 — remplace l'ancienne version « apprendre à coder ».
> Objectif : **devenir meilleur pour utiliser l'IA** sur mes projets, pas apprendre à coder.
> Règle : **5 applis seulement**. Pas plus. Chaque appli = un niveau de maîtrise de l'IA.

---

## Le principe

Aujourd'hui tu sais déjà faire le niveau 1 : tu donnes une idée, l'IA construit (Élan en est la preuve).

Il existe 6 niveaux. Tu les gravises **une appli à la fois** :

| Niveau | Ce que tu sais faire avec l'IA | Appli associée |
|---|---|---|
| 1 | Donner une idée vague et obtenir quelque chose ✅ **déjà fait avec Élan** | Élan |
| 2 | Écrire un **brief structuré** (rôle / objectif / contexte / contraintes / livrable) | **1. FicheLab** |
| 3 | Faire rédiger une **mini-spec** par l'IA, la corriger, puis seulement la laisser coder | **2. CheckTP** |
| 4 | Lancer une **boucle de critique** : l'IA audite son propre travail, teste, corrige | **3. AgendaUE** |
| 5 | Créer un **gabarit réutilisable** pour générer la suite en une seule commande | **4. CalcLab** |
| 6 | **Orchestrer** : un fichier de config pilote tout, l'IA produit le lanceur et le guide | **5. Launcher** |

À la fin, tu ne sais pas coder — mais tu sais **obtenir exactement ce que tu veux d'une IA**, et tu as un microcosme cohérent.

---

## Les 5 applis

### 1. FicheLab — niveau 2 : le brief structuré
**Ce que fait l'appli :** fiches de révision + annales + cartes mémoire pour ton BTS. C'est ton premier besoin exprimé.

**Ce que tu apprends :** au lieu de dire « fais-moi une app de fiches », tu écris un brief en 5 blocs. Tu verras la différence de résultat immédiatement.

**Le brief à utiliser :** voir `notes/boite-a-prompts.md`, modèle A.

**Compétence acquise :** formuler une demande complète du premier coup.

---

### 2. CheckTP — niveau 3 : la spec avant le code
**Ce que fait l'appli :** checklists de manipulations de labo, avec traçabilité et historique. Ton deuxième besoin exprimé.

**Ce que tu apprends :** tu demandes à l'IA de **rédiger la spec d'abord** (données, écrans, règles, cas limites). Tu la lis, tu la corriges avec tes mots de étudiant en bio, et seulement après tu dis « vas-y ».

**Pourquoi c'est puissant :** c'est là que tu reprends le contrôle. Si la spec est fausse, le code sera faux — tu l'attrapes avant.

**Compétence acquise :** corriger la compréhension de l'IA avant qu'elle ne produise.

---

### 3. AgendaUE — niveau 4 : la boucle de critique
**Ce que fait l'appli :** notes, coefficients, échéances de rendus, moyenne. Utile pour ta discipline.

**Ce que tu apprends :** tu ne acceptes pas le premier résultat. Tu demandes à l'IA de changer de casquette : *« tu es un reviewer sévère, trouve 5 problèmes, classe-les, corrige les 3 pires, puis rejoue le test »*.

**Tu sais déjà faire ça !** Sur Élan, tu avais lancé **5 reviewers** (code, sécurité, UI, QA, perf) et fait corriger les résultats. C'était du niveau 4 sans le savoir. Là, tu le feras volontairement.

**Compétence acquise :** utiliser l'IA comme son propre contrôleur qualité.

---

### 4. CalcLab — niveau 5 : le gabarit réutilisable
**Ce que fait l'appli :** dilutions, concentrations, conversions pour le labo.

**Ce que tu apprends :** tu demandes à l'IA de créer un **modèle de prompt avec des variables** (nom, but, données, écrans) qui contient toutes tes contraintes de la charte. Ensuite, une seule commande suffit pour générer l'appli.

**C'est le moment où tu passes de « je refais le brief à chaque fois » à « j'ai mon système ».**

**Compétence acquise :** industrialiser ta façon de travailler avec l'IA.

---

### 5. Launcher — niveau 6 : l'orchestration
**Ce que fait l'appli :** la page d'accueil du microcosme. Elle lit `apps.json` et affiche toutes tes applis avec leurs icônes.

**Ce que tu apprends :** tu ne parles plus d'une appli, mais du **système entier**. Tu donnes à l'IA la charte + la liste des applis, et elle produit le lanceur **et** le guide « comment créer la suite » — le guide que tu pourras un jour donner à quelqu'un d'autre.

**Compétence acquise :** piloter un ensemble, pas une seule tâche. C'est le premier pas vers « apprendre aux autres à faire leur microcosme ».

---

## Ce qu'on ne fait pas (pour rester léger)

- ❌ Pas d'apprentissage du code, pas d'autopsie de fichiers, pas de leçons de JavaScript.
- ❌ Pas de 12 applis : on s'arrête à **5**.
- ❌ Pas de monétisation maintenant.
- ❌ Pas de « refaire Élan » : il reste comme il est, c'est ton niveau 1.

---

## Livrables de chaque appli

Pour chacune, tu obtiendras :
1. Le dossier de l'appli avec `index.html` + `README.md`.
2. Une ligne ajoutée dans `apps.json` (dès la deuxième).
3. Une entrée dans ton carnet `notes/journal.md` : **« cette fois j'ai appris à … »**.

Le carnet est important : c'est ta preuve de progression, et ce sera un jour ton tutoriel.

---

## Les outils

- `CHARTE.md` : les règles communes (inchangées, elles rendent la centralisation facile).
- `notes/boite-a-prompts.md` : les 6 modèles de prompts, prêts à copier-coller.
- `notes/journal.md` : ton carnet de bord.

**Tu peux simplement copier un modèle de la boîte à prompts et le coller ici, dans notre conversation — c'est moi qui joue l'IA pour construire l'appli avec toi.**
