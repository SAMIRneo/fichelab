# Sciences de l'apprentissage — ce qui est implémenté dans FicheLab

> Recherche menue le 2026-11-22. Objectif : optimiser l'apprentissage, pas seulement stocker des fiches.

## 1. Les deux méthodes les plus efficaces (haut utilité)

**Practice testing / rappel actif** et **distributed practice / espacement** sont classées « high utility » par Dunlosky et al. (2013, *Psychological Science in the Public Interest*) et confirmées par l'UCSD (*How to Effectively Study*).

> « Spaced practice involves *when* you study, retrieval practice involves *how* you study. When you use both, they make a powerful combination. » — UCSD

Implémenté :
- Mode **Quiz** et mode **Examen** avant la relecture systématique.
- Bouton **« Voir mes fiches à revoir »** sur l'accueil, basé sur un planning de répétition espacée.

## 2. Répétition espacée — modèle FSRS simplifié

FSRS modélise chaque carte avec trois variables : **difficulté, stabilité, rétrievabilité** (Anki FAQ, KDD 2022). La stabilité S = délai pour que la probabilité de rappel tombe de 100 % à 90 %. À rétention visée 90 %, l'intervalle ≈ S.

Benchmark ouvert `open-spaced-repetition/srs-benchmark` (août 2026, ~350 M d'avis, 9 999 collections) : FSRS-6 erreur de calibration ~4 points contre 13–15 % pour SM-2, et 20 à 30 % d'avis en moins à rétention égale (simulations).

Implémenté (version simplifiée, transparente et hors ligne) :
- Chaque fiche porte `sr:{S, due, last, reps, lapses}`.
- 4 boutons après retournement de carte : **Encore / Difficile / Bien / Facile**.
- `Encore` réduit S de 60 % et compte un oubli ; `Bien` multiplie S par 2,2 ; `Facile` par 3,5.
- Prochain rappel = aujourd'hui + S jours (rétention cible 90 %).

## 3. Feedback obligatoire

Méta-analyse 2025 (*Retrieval Practice Versus Elaborative Encoding*,Educational Psychology Review) : l'avantage du rappel est **conditionnel au feedback** (g = 0,50). Sans correction, l'élaboration devient plus bénéfique que le test.

Implémenté : toute question donne une correction écrite, QCM comme texte libre.

## 4. Auto-explication et interrogation élaborative

L'**self-explanation effect** (Chi et al. ; Renkl) et l'**elaborative interrogation** sont des techniques d'utilité modérée à élevée : l'apprenant doit expliquer *pourquoi*, avec ses mots.

Implémenté : sur les questions rédactionnelles, le bouton « Voir la correction » est **bloqué** tant que l'utilisateur n'a pas écrit son explication (`Pourquoi ?`).

## 5. Jugement de confiance (métacognition)

Les jugements de confiance améliorent la régulation de l'apprentissage (biwer et al., S2D2 framework, 2023). Savoir qu'on était « sûr » et qu'on s'est trompé crée un signal d'apprentissage puissant.

Implémenté : avant chaque vérification, trois niveaux **Sûr / À peu près / Je devine**. Si l'utilisateur était sûr et s'est trompé, un avertissement explicite s'affiche avec la correction.

## 6. Interleaving (mélange)

Le mélange des catégories surpasse le blocage pour l'apprentissage par similarité, mais le blocage aide pour l'apprentissage de règles (Brunmair & Richter, 2019 ; MDPI 2025). La méta-analyse 2026 (Educational Psychology Review) confirme un bénéfice sur les tests de mémoire.

Implémenté : mode **Mélange** dans l'examen (fiches vérifiées + annales), et possibilité de choisir plusieurs matières dans le questionnaire, ce qui rend le mélange pertinent.

## 7. Desirable difficulties **avec** gestion de la charge cognitive

Les difficultés souhaitables (test, génération, variété) aident à long terme, mais **trop de difficulté sur un matériau à forte interactivité** provoque une surcharge (Pyke et al., 2025 ; Sweller, cognitive load theory).

Implémenté :
- Progression en 3 étapes : **Lire → Cartes → Quiz → Examen** (difficulté croissante).
- Une fiche = 3 à 4 points maximum (découpage, pas de mur de texte).
- Le mode « Lire » affiche un rappel : lire ne suffit pas, il faut se tester.

## 8. Re-apprentissage Successif

Entraînement jusqu'à 100 % de justesse sur plusieurs jours : méthode parmi les plus efficaces pour la rétention à long terme (UCSD, Carpenter et al.).

Implémenté : après un examen, bouton **« Refaire les N questions ratées »** qui relance uniquement les erreurs.

## 9. Ce que la recherche déconseille (et qu'on évite)

- **Relire / surligner / résumer passivement** : faible utilité (Dunlosky 2013). FicheLab ne propose pas de « relecture » comme activité principale.
- **Cramming** (tout la veille) : moins efficace que l'espacement, même à temps égal.
- **Tester sans反馈** : annule le bénéfice du testing.

## Sources

- Dunlosky, Rawson, Marsh, Nathan & Willingham (2013), *Improving Students' Learning With Effective Learning Techniques*, PSPI 14(1).
- Carpenter, Pan & Butler (2022), *The science of effective learning with spacing and retrieval practice*, Nature Reviews Psychology.
- UCSD Psychology, *How to Effectively Study* (mis à jour 2026).
- Méta-analyse 2026, *Retrieval Practice Versus Elaborative Encoding*, Educational Psychology Review (g = 0,14 global ; g = 0,50 avec feedback).
- Méta-analyse 2026, *Effectiveness and Boundary Conditions of Retrieval, Distributed and Interleaved Practice in Authentic Classrooms*, Educational Psychology Review.
- Maye et al. (2026), *Spaced Repetition in Medical Education: systematic review and meta-analysis*, The Clinical Teacher (21 415 apprenants, SMD 0,78).
- Pyke, Lunau & Javadi (2025), *Desirable difficulties vs cognitive load theory*, Quarterly Journal of Experimental Psychology.
- Biwer et al. (2023), *S2D2 framework*, Educational Psychology Review.
- open-spaced-repetition/srs-benchmark (août 2026), Anki FAQ FSRS, Ye et al. (KDD 2022).
- Brunmair & Richter (2019), méta-analyse de l'interleaving, Psychological Bulletin.
