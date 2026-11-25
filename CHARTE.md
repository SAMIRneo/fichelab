# Charte du Microcosme — les règles communes

> Version 1 — à respecter pour **chaque nouvelle appli**.
> But : que mes applis restent indépendantes maintenant, et faciles à centraliser plus tard.

## 1. Structure d'une appli

Une appli = **un dossier**, avec au minimum :

```
nom-appli/
├── index.html          ← TOUT le code (HTML + CSS + JS), zéro dépendance
├── manifest.webmanifest
├── icon.svg
├── sw.js               ← service worker (optionnel mais recommandé)
├── README.md           ← ce que fait l'appli + ce que j'ai appris en la faisant
└── assets/             ← images éventuelles (importées localement)
```

## 2. Données

- **Un seul stockage** : `localStorage`. Pas de backend, pas de compte obligatoire.
- **Préfixe unique par appli** : `mcos-<nom-appli>:` → ex. `mcos-fichelab:data`.
  Ça évite qu'une appli écrase les données d'une autre quand le Launcher les ouvrira toutes.
- **Version de données** : chaque objet stocké contient `v: 1`.
- **Export/import** : format identique pour toutes les applis :

```json
{
  "app": "fichelab",
  "version": 1,
  "exportedAt": "2026-11-22T10:30:00.000Z",
  "data": { ... }
}
```

- **Validation à l'import** : vérifier le format, limiter la taille (2 Mo), ne jamais faire confiance au fichier (cf. `sanitizeData()` dans Élan, ligne 470).

## 3. Design

Reprendre les tokens d'Élan (lignes 18–30 de `index.html`) :

- **2 couleurs seulement** : `--bg` (fond) et `--ac` (actions), tout le reste en est dérivé.
- **Mode clair ET sombre** dès le départ, avec `--ac-text` pour le texte sur fond d'action.
- **Français tutoyé**, court, clair.
- **Cibles tactiles ≥ 44 px**, `:focus-visible`, `aria-*` sur les dialogues.
- `prefers-reduced-motion` respecté.
- Si un service worker existe : **incrémenter `CACHE` à chaque modification** (comme `elan-v54` dans `sw.js` ligne 1).

## 4. Navigation

- Un en-tête avec **le nom de l'appli** et un bouton « ← Microcosme » (même s'il pointe vers `#` au début).
- Une navigation basse si l'appli a plusieurs écrans.
- Aucune dépendance externe : pas de CDN, pas de framework, pas d'API payante.

## 5. Chaque appli doit pouvoir être « lue »

Dans le `README.md` de l'appli, écrire en 5 lignes :

1. Ce que fait l'appli.
2. Où sont stockées les données (la clé exacte).
3. Quelle est la fonction la plus importante (son nom).
4. Ce que j'ai appris en la faisant.
5. Ce que je ne comprends pas encore.

C'est cet exercice — pas le code — qui crée l'autonomie.

## 6. Le fichier d'index (plus tard)

Le Launcher lira un `apps.json` simple :

```json
{
  "apps": [
    {
      "id": "elan",
      "nom": "Élan",
      "desc": "Muscu, cardio, streak",
      "url": "../elan/index.html",
      "icon": "../elan/icon.svg",
      "couleur": "#ccff00"
    }
  ]
}
```

Tant que chaque appli respecte la charte, **ajouter une ligne ici suffit** pour l'intégrer.
