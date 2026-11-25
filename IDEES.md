# Veille & catalogue d'idées — Novembre 2026

> Recherche menée le 2026-11-22 à partir de sources publiques : Gartner, O'Reilly Radar, InfoQ, Thoughtworks/Databricks, MCP Blog, Product Hunt, GitHub trending, Sprout Social, Indie Hackers, analyses micro-SaaS.
> Objectif : partir des **signaux réels** plutôt que d'une brainstorm générique.

---

## 1. Ce qui se passe vraiment (signaux avec chiffres)

### A. Les agents sont partout… mais le goulot a bougé
- Gartner (nov. 2026) : **70 % des équipes logicielles adopteront une approche « eval-driven » d'ici 2028** (moins de 20 % aujourd'hui).
- Gartner : les organisations avec une infra de *harness* (contexte, standards, garde-fous) auront **60 % de défauts post-déploiement en moins** d'ici 2028. À mesure que les modèles se ressemblent, **le harness compte plus que le modèle**.
- Gartner : **70 % des entreprises sandboxeront leurs workflows agentiques d'ici 2030** (10 % en 2026).
- Thoughtworks/Databricks : les boîtes avec outils d'évaluation mettent **~6× plus de projets IA en prod** ; avec gouvernance, **~12× plus**. Les systèmes multi-agents ont crû de **327 % en 4 mois**.
- Jellyfish : les agents touchent **27,7 % des PR** (médiane, sept. 2026) contre ~2 % en janvier ; mais **0,5 % seulement des PR fusionnées** le sont sur revue IA seule → énorme fosse de confiance.
- GitHub : part des PR **ouvertes par des agents : 17 % en mars → >40 % en septembre 2026**.

### B. MCP est devenu « plumbing », mais très mal sécurisé
- **97 millions de téléchargements/mois du SDK MCP** (mars 2026) vs 100 000 au lancement (×970 en 18 mois).
- Mais seulement **41 % des leaders tech déclarent un usage en prod** (même limité) et **8,5 % des serveurs MCP implémentent OAuth 2.1 obligatoire**.
- La sécurité reste **le premier bloquant** du déploiement enterprise.
- Nouveau standard : version **2026-07-28** (stateless, header-based routing, MRTR, listes cachables). A2A v1.0 + 150 orgs, CP2 (paiements) = le triptyque MCP/A2A/AP2 est stabilisé sous le Linux Foundation (AAIF).
- Traduction : **tout le monde branche des outils, personne ne les gouverne**. C'est le vide.

### C. Fatigue de l'IA / retour de l'humain
- Sprout Social (Q1 2026) : **56 % des consommateurs voient du « AI slop » souvent/très souvent**, 83 % au moins parfois. **50 % des Gen Z et 44 % des Millennials ont désabonné/masqué** une marque pour cause de slop.
- 33 % disent que **l'originalité** est ce qui fait d'une marque leur préférée (2ᵉ critère après la qualité produit).
- Recherches Google « no ai slop » : **20 → 1 900/mois en 12 mois (+9 400 %)**, breakout en juillet 2026. « lore » élu mot de l'année 2026 devant « slop ».
- Adaptavist : **46 % disent que gérer le slop rend leur job moins intéressant**, **42 % passent plus de temps à vérifier l'IA qu'elle ne leur en fait gagner**, 55 % estiment que ça ralentit leur équipe.
- BetterUp/Stanford : **40 % des employés de bureau reçoivent du « workslop »** → des heures perdues et des millions de $ de productivité évaporés.

### D. Local-first / souveraineté
- Retour du **local-first** : CRDT (Automerge, Yjs) matures, ElectricSQL 1.0, on-device AI (Apple Foundation Models ~3B params sur iPhone/Mac, NPU 70+ TOPS).
- VoiceStudio (open-source, alternative locale à ElevenLabs, **646 langues**) a pris ~100k étoiles GitHub en un mois — le positionnement « rien ne sort de chez vous » fait tout le travail.
- principe Ink & Switch : donnée locale = copie authoritative, offline = état normal, le cloud devient optionnel.
- Mais nuance honnête : un senior de Supabase — « local-first n'est pas un défaut, c'est une architecture pour de vrais problèmes » ( Sync engine = 3 mois de dev pour 50 users concurrently = sur-engineering ).

### E. Économie micro-SaaS : où est l'argent (données 2025–2026)
| Catégorie | Prix typique | MRR médian an 2 | Délai |
|---|---|---|---|
| IA verticale (métiers, dentaire, legal) | $99–499/mo | **$18k** | 6–9 mois |
| Conformité / SOC2 / RGPD | $199–499/mo | **$22k** | 9–12 mois |
| Ops creator economy | $19–49/mo | $8k | 4–6 mois |
| Analytics de niche | $29–79/mo | **$11k** (meilleur médian) | 6–9 mois |
| Services productisés (audits) | $199–999 one-off | $15k | 3–6 mois |
| Extensions navigateur B2C | $5–19/mo | $6k | 6–12 mois |
| Outils dev indie (CLI, boilerplates) | $49–299 one-off | **$25k** | 3–6 mois |

- **Piège productivité** : 620 tentatives, 39 gagnants (6,3 %). « AI » : 1 927 entrants, 15,7 % de réussite — être « IA » n'est plus un différenciateur.
- **Ce qui paie le mieux** : conformité, risque, revenue, temps (4 catégories de PainBase). Les problèmes de *pouvoir* (ex. relancer un client qui te doit de l'argent) : 71 threads de plainte, **0 disposition à payer** → à éviter.
- **Pricing trust mort** : 51 % des apps ont une note récente >1 étoile sous leur moyenne historique. Hausses sauvages : Intercom $119→$854, $1 200→$10 000, Vitals $29,99→$155,99. → **prix fixe, transparent, pas de credits opaques = avantage concurrentiel**.
- **Méthode de validation** (Indie Hackers) : ne cherche pas les plaintes, cherche les **workarounds** : « je le fais à la main tous les matins », « mon spreadsheet pour… », « j'exporte en CSV puis… », « j'ai un template pour… ». Ce sont ceux qui paient déjà en temps.

### F. Ce queGitHub starre en ce moment (tendance de fond)
- `morluto/rea` — « reverse engineer anything with agents » : **+155k étoiles en 30 jours**.
- `craft-anything` — comprendre comment n'importe quel logiciel fonctionne et recréer le sien (+37k).
- `cloudflare/security-audit-skill` — audit de sécurité multi-phase, résultats machine-readable (+43k).
- `t3code` — contrôler Claude Code/Codex depuis n'importe quel ordi ou téléphone (+35k).
- `ffmpeg-skill` — éditeur vidéo LOCAL pour agents (42 outils FFmpeg, MCP, sans cloud ni clé API).
- `cleanyourtv` — débloat Android/Google TV (+58k).
- `mattpocock/skills`, `obra/superpowers`, `anthropics/skills` — les « skills » deviennent une forme de distribution.
- Motif : **local, open-source, agent-skills, reverse-engineering, dés-encombrement**.

---

## 2. Audit stratégique — 3 axes à saisir, 3 pièges à éviter

**Axes à saisir**
1. **La couche de confiance des agents** : évals, sandbox, permissions, coûts, audit, identité. Le modèle est commoditisé ; le harness est le nouveau terrain de jeu.
2. **L'anti-slop comme produit** : « fait par un humain », traçabilité, qualité, ralenti volontaire, édition lente. Le manque devient une fonctionnalité.
3. **Le local-first pragmatique** : données chez l'utilisateur, one-time payment, zéro télémétrie, marche hors ligne. Réponse directe à la fatigue des abonnements.

**Pièges**
1. ❌ « Encore une app de productivité IA » — 6,3 % de réussite, gratuit et excellent déjà partout.
2. ❌ « Un wrapper GPT générique » — 1 927 concurrents, l'IA est table stakes.
3. ❌ « Un outil pour un problème dont personne ne paie » — journal, facturation à relancer, plaintes sans workaround = signal mort.

---

## 3. Catalogue — ~50 idées

Légende : **F** = faisable solo en <2 mois · **M** = moyen · **L** = lourd. 💰 = prix indicatif.

### A. Anti-slop / « Humain d'abord » (le filtre 2026)
1. **HumanMade** — label + badge vérifiable « contenuWritten by a human, no LLM » avec preuve de process (brouillons, historique de frappe). 💰$9/mo ou one-time $29. **F**
2. **SlowWrite** — éditeur qui *refuse* de générer : il ne fait que structurer, compter, comparer avec tes brouillons. Anti-complétion. 💰$19 one-time. **F**
3. **SlopDetector pour marques** — analyse un feed et score la « slopabilité » de tes posts avant publication. 💰$29/mo. **F**
4. **Lore not Slop** — plateforme de micro-narratifs de marque : 3 vraies histoires/semaine, pas de contenu « thought leadership ». 💰$49/mo. **M**
5. **Receipt** — outil qui archive la trace humaine d'un article (notes, versions, sources lues) et la publie en annexe. 💰$12/mo. **F**
6. **Dedupe-toi-même** — détecte les phrases AI génériques dans tes propres textes et les remplace par tes tournures habituelles apprises de tes anciens écrits. 💰$15/mo. **F**
7. **NoCred** — annuaire de produits qui *n'utilisent pas* d'IA générative, avec filtres par catégorie. 💰freemium. **F**
8. **HumanRate** — «pourcentage humain» calculé sur un texte, non pas pour détecteur IA mais comme *objectif de style* personnel. 💰$8/mo. **F**
9. **The Edit Room** — service productisé : relecture humaine (toi) de documents IA, facturé $99/document, avec avant/après public. 💰one-off. **F**
10. **Unfollow Shield** — navigateur qui masque automatiquement les marques dont le score originalité est bas, et te montre pourquoi. 💰$5/mo. **M**

### B. Harness, confiance & gouvernance des agents (le gros filon)
11. **CapSwitch** — plafond de dépense **dur** par agent, coupe-net à la limite, avec dashboard « combien ce agent a coûté aujourd'hui ». 💰$39/mo. **M**
12. **TraceWhy** — au lieu de traces, explique *pourquoi* l'agent a pris telle décision, en langage humain, avec le morceau de contexte responsable. 💰$49/mo. **M**
13. **MCP-Lint** — scan d'un serveur MCP : OAuth 2.1 manquant ? outils trop nombreux ? privilèges excessifs ? note de conformité. 💰gratuit → $79/mo. **F**
14. **MCP-Guard** — proxy local qui applique des règles (qui peut appeler quoi, budget, approbation) devant n'importe quel serveur MCP. 💰$99/mo. **M**
15. **EvalKit en boîte** — 20 évals prêtes à l'emploi (exactitude, refus, fuite de données, coût) branchables en 1 ligne sur un agent. 💰$59/mo. **F**
16. **Sandbox-in-a-box** — CLI qui isole un agent dans un conteneur éphémère avec accès réseau contrôlé. 💰$29/mo. **M**
17. **Agent receipts** — chaque action d'un agent produit un reçu signé (quoi, quand, pour qui, avec quelle autorisation). 💰$69/mo. **M**
18. **KillSwitch** — bouton physique/API qui coupe tous les agents d'une org en <1 s, avec journal d'audit. 💰$99/mo. **F**
19. **Prompt diffusion** — un seul endroit pour modifier le contexte de 12 agents différents (le « AI Context Flow » vu sur PH, mais en local-first). 💰$19/mo. **M**
20. **VibeFix** — « service de secours pour app vibe-codée » : audit + durcissement d'un MVP Lovable/Cursor qui ne tient plus. 💰$499 one-off. **F** (service productisé)

### C. Local-first & souveraineté (acheter une fois, garder ses données)
21. **LocalNotes Pro** — carnet de notes chiffré, fichiers Markdown, zéro compte, recherche locale, sync optionnelle via dossier. 💰$29 one-time. **M**
22. **OfflineRAG** — base de connaissances « question-réponse » qui tourne uniquement sur Ollama/LM Studio, avec citations de tes propres fichiers. 💰$39 one-time. **M**
23. **NoCloud Calendar** — agenda local avec sync pair-à-pair entre tes devices, sans Google. 💰$25 one-time. **M**
24. **BringYourOwnModel** — UI unique qui pointe vers ton modèle local, avec comparaison A/B de 2 modèles hors ligne. 💰$19 one-time. **F**
25. **DataExit** — « bouton exporter » universel : transforme les exports de 30 SaaS en archives lisibles et documentées. 💰$19 one-time. **F**
26. **Airgap Wallet** — carnet de mots de passe / notes sensibles sur clé USB, interface web locale, jamais de réseau. 💰$29 one-time. **M**
27. **QuietInbox** — client mail local avec filtre anti-newsletter agressif et « aucun pixel, aucune télémétrie ». 💰$39 one-time. **M**
28. **FamilyMesh** — partage de photos/fichiers entre proches en Bluetooth/Wi-Fi direct (cf. MeshLive sur PH), zéro serveur. 💰$19 one-time. **L**

### D. Micro-SaaS verticaux « ennuyeux » (les mieux payés)
29. **Renewal Radar** — suit les renouvellements de licences / certifications (HVAC, real estate, nursing) et évite les amendes. 💰$49/mo. **F**
30. **Quote→Invoice pour un seul métier** (électriciens / plombiers) — devis accepté = facture planifiée automatiquement. 💰$19/mo. **F**
31. **Field Photo Report** — rapport photo-heavy (inspecteurs, toitures, restauration) en PDF propre. 💰$29/mo. **F**
32. **Shift Handover** — check-in vocal pour relèves de poste (restaurants, terrain), résumé structuré. 💰$39/mo. **F**
33. **Dunning humain** — relance de paiements échoués en message texte, par raison de refus, prix fixe pour indie SaaS. 💰$29/mo. **F**
34. **SEO/AEO visibility** — suit la visibilité dans ChatGPT/Perplexity/AI Overviews (RankAI : $56k MRR / 155 abonnés ≈ $365/mo). 💰$99/mo. **M**
35. **Client report generator** — GA4 + Search Console → PDF de marque en 1 clic pour freelances SEO. 💰$29/mo. **F**
36. **Scope Creep Tracker** — détecte les demandes hors périmètre signé dans un projet agency. 💰$19/mo. **F**
37. **Sermon/voice translator local** — traduction de sermon en direct (Glossa.live : $21k en 30 j), version auto-hébergée. 💰$49/mo. **M**
38. **Campground/RV booking** — cartes d'emplacements, acompte, évite le double-booking. 💰$59/mo. **M**
39. **School-bus route optimizer** — 8–40 bus, arrêts, rapports conformes pour le district. 💰$99/mo. **L**
40. **MedSpa mini-ERP** — $149/mo/location, les EHR génériques sont détestés. 💰$149/mo. **M**
41. **Piano teacher scheduler** — profs de musique indépendants sur Excel. 💰$19/mo. **F**
42. **Solo attorney practice** — $79/mo, trop petit pour Clio. 💰$79/mo. **M**

### E. Objets malins / viraux (faible coût, fort bouche-à-oreille)
43. **Pushback** — « le tracker de vol qui sait quel salon tu peux utiliser » (tel quel sur PH, à réimaginer pour d'autres contextes : quel bagage, quelle salle d'attente). 💰$9/mo. **F**
44. **Console Storage Planner** — « minimum de jeux à supprimer avant ta prochaine install ». 💰$5 one-time. **F**
45. **GhostTunnel** — snaps & chat éphémères peer-to-peer, zéro serveur. 💰gratuit/open-source. **M**
46. **Tamagotchi qui travaille** — compagnon qui exécute de vraies tâches en parallèle en haut de l'écran (Tamekoshi, 100 upvotes). 💰$9/mo. **M**
47. **TeaserKit** — ton coding agent réalise ta vidéo de lancement à partir de templates. 💰$29/mo. **M**
48. **Verge** — swipe d'un coin d'écran = luminosité/volume (mobile). 💰$3 one-time. **F**
49. **Backspin** — apprendre le DJ dans le navigateur sur de vraies platines. 💰$19/mo. **M**
50. **Omi/Voice CLI** — agent de code dans le terminal, 13 modèles au choix. 💰open-source. **M**

### F. Reverse-engineering & compréhension (la mode montante)
51. **ExplainMyApp** — pointe une app, elle te dessert son architecture et ses données (cf. `rea`, +155k étoiles). 💰$49/mo. **L**
52. **Debloat TV** — équivalent cleanyourtv pour Android TV francophone, avec une interface simplifiée. 💰$9 one-time. **M**
53. **Graphify pour ton codebase** — transforme code + docs + schémas SQL en graphe interrogeable, sans vector store. 💰$29/mo. **M**
54. **DiffHumain** — avant de merger : « qu'est-ce qui a changé *vraiment*, et est-ce que c'était demandé ? ». 💰$19/mo. **F**
55. **Legacy Translator** — lit un vieux code, produit une doc vivante + tests de caractérisation. 💰$299 one-off. **M**

---

## 4. Mes 5 coups de cœur (rapport signal / faisabilité)

| # | Idée | Pourquoi | Premier test (7 jours) |
|---|---|---|---|
| 1 | **MCP-Lint / MCP-Guard** | 97M downloads, 8,5 % OAuth, sécurité = 1ᵉʳ bloquant. Douleur *et* budget. | Lancer le lint gratuit sur 10 serveurs MCP publics, publier les résultats, voir qui demande la version payante. |
| 2 | **VibeFix** (audit de MVP vibe-codé) | Service productisé $499, 3–6 mois au MRR médian $15k. Pas de code lourd à écrire. | 10 messages dans des communautés « Lovable/Cursor bloqué » avec offre d'audit gratuit contre témoignage. |
| 3 | **CapSwitch** (plafond de dépense agent) | Threads Reddit : 15 plaintes, 11 haute urgence, gens qui codent leur propre cap. | Poster le concept + pricing $39, demander « qui a déjà dépassé son budget agent ce mois ? ». |
| 4 | **Dedupe-toi-même / HumanMade** | +9 400 % de recherche « no ai slop » ; rupture nette avec le marché. | Écrire l'outil en 48 h, l'appliquer à 20 posts de marques connues, tweet les avant/après. |
| 5 | **Renewal Radar** | Conformité = catégorie au MRR médian le plus élevé ($22k). Douleur récurrente, acheteur identifié. | Interroger 10 pros : « comment tu sais que ta certification expire ? » → si réponse = spreadsheet, c'est gagné. |

---

## 5. La méthode pour choisir (à appliquer avant d'écrire une ligne de code)

1. **Cherche des workarounds, pas des plaintes.** Google / Reddit : `"j'exporte en CSV et puis…"`, `"mon spreadsheet pour…"`, `"je le fais à la main tous les matins"`, `"is there a way to automate…"`.
2. **Vérifie le signal de paiement** : est-ce que la personne dépense déjà du temps, de l'argent, ou perd des revenus à cause du problème ?
3. **Test en 30 jours** : landing page + 20 inscriptions + 10–20 entretiens problème. 20 % des startups Stripe Atlas ont encaissé leur 1ᵉʳ client en 30 jours (8 % en 2020).
4. **Prix transparent, pas de credits opaques.** 51 % des apps se font descendre à cause de la facturation.
5. **Kill condition explicite** : écris à l'avance ce qui te fera arrêter.

---

## Sources (extraites)

- Gartner — Top Strategic Technology Trends in Software Engineering 2026 (17 nov. 2026)
- O'Reilly Radar — Trends to Watch, novembre 2026
- InfoQ — AI, ML and Data Engineering Trends Report 2026 (30 oct. 2026)
- Thoughtworks — State of AI Agents 2026 (Databricks)
- CIOPages — State of Play 2026 : AI Agent Orchestration
- MCP Blog — spec 2026-07-28, feuille de route (août 2026)
- Product Hunt — classements 18–22 nov. 2026
- GitHub trending — Repocharts, GitTrend, MostStarred (nov. 2026)
- Sprout Social — Pulse Surveys Q1/Q3 2026 ; Inc., IT Pro, Nature npj AI, Rising Trends — slop/human
- StartupIdeasDB, DirectoryGems, TrendGap, ZeroRaised, Redwerk, Creatr, BigIdeasDB — données micro-SaaS
- Indie Hackers — analyses 136k et 94k plaintes, « search for workarounds »
