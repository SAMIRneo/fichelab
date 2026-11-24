# FicheLab 📚

Applis de révision du microcosme — **niveau 2 : le brief structuré**.

## Ce que fait l'appli

- **Questionnaire d'accueil** (8 étapes) : prénom, âge, niveau, **46 filières classées par effectifs réels**, **année d'étude sélectionnable** (2nde/1re/Tle, BTS1/2, BUT1/2/3, L1/L2/L3, IFSI1/2/3…), matières adaptées à la filière et à l'année, objectif minutes/jour, méthode de révision, ce qui bloque, contrôles déjà présents.
- **Catalogue de 912 fiches réelles + 60 annales corrigées** : tronc commun lycée, spécialités, séries technologiques, bac pro, BTS les plus demandés (dont **BTS Bioanalyses en laboratoire de contrôle / BIOALC**, référentiel 2024/2025), BUT, licences, CPGE, santé, écoles de commerce. Les 192 dernières fiches sont des **chapitres complets** (10+ points, 6+ questions) produites par des agents responsables de filière. Sources dans [`SOURCES.md`](SOURCES.md).
- **Bibliothèque de fiches** : catalogue de départ adapté au niveau/filière + ajout de ses propres fiches.
- **Règle de vérification** : chaque fiche et chaque info porte un statut `à vérifier` / `vérifiée` et une source. Une fiche générée ne devient vérifiée que si tu la valides explicitement. Les exercices générés n'utilisent que des fiches vérifiées.
- **3 modes de révision** : lire, cartes à retourner, quiz avec correction, plus un espace de **notes personnelles par fiche**.
- **Mode examen** : chrono, note sur 20, correction expliquée, historique des scores. Questions issues de fiches vérifiées, d'annales importées ou d'un mélange.
- **Annales par filière** : vraies sources vérifiées (éduscol, Education nationale, annalesbts.fr, Studyrama, universités de Rennes/Dijon/Paris, Major Droit…) avec bouton « Télécharger / ouvrir », recherche en ligne, import de contrôles et exercices générés hors ligne depuis une fiche vérifiée.
- **Onglet Fiches simple** : les matières s'affichent en puces avec leur nombre de fiches ; les filtres « À lire » / « Lues » séparent les fiches non validées des fiches validées par le Quizz (8/10). Chaque ligne donne le titre, le nombre d'infos et de questions, et les boutons Ouvrir / ✏️ / 🗑. Plus de gros tableau de couverture, plus de double sélecteur matière.
- **Recherche plein texte** : un champ « 🔍 Rechercher un mot ou une phrase… » filtre instantanément les fiches. La recherche porte sur le titre, la matière, la source, tout le cours (points et blocs), les questions et leurs corrections, et les titres des schémas. Elle ignore les accents et la casse ; plusieurs mots doivent tous être présents (ex. `beer lambert` trouve la fiche Beer-Lambert). Un bouton ✕ efface la recherche, qui se combine avec le filtre de matière.
- **Format prototype étendu à 4 filières** : seules les fiches au format prototype (7 blocs de cours + schémas SVG) sont proposées aux profils `bts-bio`, `generale`, `bts-mco` et `pass`. **BTS BIOALC : 96 fiches** (50 en BTS1, 54 en BTS2), référentiel 2024/2025. **Voie générale : 95 fiches** (29 en 2nde, 46 en 1re, 42 en Terminale) — [`GENERALE-PROGRAMME.md`](GENERALE-PROGRAMME.md). **BTS MCO : 82 fiches** (52 en BTS1, 62 en BTS2) — [`BTSMCO-PROGRAMME.md`](BTSMCO-PROGRAMME.md). **Licence PASS : 62 fiches** en PASS1 — [`PASS-PROGRAMME.md`](PASS-PROGRAMME.md). Au total **335 fiches prototype, 969 schémas SVG, 3 121 questions corrigées**. Les anciennes fiches « texte brut » de ces filières restent dans `data/` mais ne sont plus affichées ni importées ; une migration au démarrage les retire du stockage local sans toucher aux fiches personnelles. La bibliothèque contient **23 annales BIOALC** (dont les 2 sujets officiels 2026), **19 annales voie générale** et **18 annales BTS MCO**.
- **Optimisation de l'apprentissage** ([`LEARNING-SCIENCE.md`](LEARNING-SCIENCE.md)) : répétition espacée type FSRS (4 boutons Encore/Difficile/Bien/Facile, prochain rappel calculé), jugement de confiance avant chaque réponse, auto-explication obligatoire avant la correction des questions rédactionnelles, re-apprentissage des questions ratées, mélange des matières.
- **Suivi du temps** : par fiche, par matière, total par jour, objectif quotidien, courbe sur 14 jours.
- **Export/import JSON** au format de la charte, thème clair/sombre, 100 % local et hors ligne.

## Où sont les données

Clé unique : `mcos-fichelab:data` dans le `localStorage`.
Format export : `{ app: "fichelab", version: 1, exportedAt, data }`.

## La fonction centrale

`fichesPour(profil)` — elle choisit les fiches de départ selon le niveau et la filière, et les marque toutes `à vérifier`.

## Limite assumée

L'app stocke et affiche le **nom** d'un PDF/photo importé, mais ne fait pas d'OCR hors ligne. Le bouton **« Extraire le texte avec l'IA »** affiche un prompt à copier dans une IA ; tu colles ensuite le texte vérifié. C'est volontaire : c'est l'exercice du niveau 2 (cadrer l'IA, puis vérifier son résultat).

## Audit et nettoyage (23 novembre 2026)

- **Import JSON sécurisé** : limite de 5 Mo, validation de la structure, SVG nettoyés (scripts, `on…`, `javascript:` supprimés), échec d'écriture signalé au lieu d'un faux « import terminé ».
- **Affichage protégé** : tous les textes des blocs passent par `esc()` ; plus d'injection HTML depuis un fichier importé.
- **Vrais bugs corrigés** : filtre « Maths / Anglais professionnel » qui ne renvoyait rien, fiches sans `points`/`questions` qui pouvaient faire planter l'appli, édition d'une fiche vérifiée qui rechargeait silencieusement les anciens blocs, faux QCM fabriqués avec trois affirmations vraies, tri aléatoire biaisé, localStorage corrompu qui provoquait un écran blanc.
- **Code et données morts retirés** : ancien catalogue `MODELES_OLD`, handlers et CSS inutilisés, 79 anciennes fiches texte brut (433 Ko) remplacées par la simple liste de leurs identifiants pour la migration. `index.html` passe de 4,1 Mo à 3,7 Mo.
- **Vérification finale** : syntaxe JS OK, 96 fiches prototypes / 252 schémas sans chevauchement ni texte coupé, 926 questions, aucune erreur console, navigation et filtres testés dans le navigateur.
- **Extension voie générale (23 novembre 2026)** : 95 fiches prototype générées par 7 agents de matière (`data/gen_generale_A..G.py`) à partir d'une fiche-modèle validée (`data/gen_generale_modele.py`) et de la bibliothèque `data/fixtures.py`. Injection dans `index.html`, filtre prototype et migrations généralisés à toutes les filières converties, vrais examens désormais filtrés par filière. Audit automatique [`AUDIT-FILIERES.md`](AUDIT-FILIERES.md) : **aucun problème détecté**.
- **Interface allégée** : retrait des 197 pictogrammes d'alerte orange (⚠️) dans les fiches et l'interface (migration du stockage local comprise). Plus de notion « fait / pas fait » : il n'y a que **« à lire »** (bandeau gris) et **« lue »** (bandeau vert). Une fiche passe en « lue » **uniquement si le quizz est réussi à 8/10** ; l'examen utilise toutes les fiches, lues ou non.
- **Onglet « Quizz »** (ex-Réviser) : questions posées une par une, bouton « Valider » qui passe automatiquement à la suivante, « Finir » à la dernière. À la fin, une modale donne la note sur 20, le score, et pour chaque question ta réponse, la bonne réponse et l'explication. Les questions rédactionnelles s'auto-évaluent avec « J'avais juste / J'avais tort ». En dessous de 8/10, la fiche reste « à lire » avec un bouton « Réessayer ». Le mode « Cartes » a été supprimé.
- **Onglet Examen en deux rubriques** :
  - **📄 Vrais examens — annales officielles** : **12 sujets** téléchargés et intégrés (E7/E4 2026, U31/U32/U33 et E4 STB 2025, plus 6 sujets btsbioalc.fr : maths 2025/2024, physique-chimie 2019/2018, E4 analyses 2019, E6 relations pro 2026). Énoncé complet consultable avec « Voir le sujet » et corrigé intégral avec « ✅ Corrigé » quand il existe. 88 questions jouables. Attention : les corrigés de btsbioalc.fr portent la mention « corrigé non officiel, rédigé avec l'aide d'outils d'IA » ; pour les 6 sujets officiels Aix-Marseille, les corrections sont indicatives. À vérifier avec ton cours.
  - **🤖 Examens d'entraînement (créés par IA)** : questions tirées des fiches, choisies par matière (12 matières disponibles, 536 questions au total) avec 5, 10 ou 20 questions. Le mode « Toutes matières » mélange les sujets. Chrono, note sur 20, correction détaillée et « Refaire les questions ratées » dans les deux cas.

## Ce que j'ai appris à faire avec l'IA à ce niveau

- Remplir un brief en 5 blocs (rôle, objectif, contexte, contraintes, livrable) au lieu de dire « fais-moi une app ».
- Poser une **règle produit vérifiable** (le statut `à vérifier`) au lieu de faire confiance au résultat.
- Reconnaître une limite technique et demander une solution adaptée (le prompt d'extraction).
- Exiger un format de livrable précis.

## Ce que je ne maîtrise pas encore

- Je n'ai pas écrit le code moi-même.
- Je ne sais pas encore modifier une fonction précise sans casser autre chose.
- Ce sera l'objet d'un niveau suivant, pas de celui-ci.
