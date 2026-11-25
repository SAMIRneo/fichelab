# Top 5 — Dossiers détaillés (novembre 2026)

> Complément de `IDEES.md`. Pour chaque idée : problème chiffré → produit concret → acheteur → prix → faisabilité → acquisition → risques → test sur 7 jours.

---

## 1. MCP-Lint / MCP-Guard — le contrôle de sécurité des agents

### Le problème
MCP est devenu le standard « comment un agent parle à un outil » : **97 M de téléchargements/mois du SDK** (mars 2026), contre 100 000 au lancement. Mais :
- seulement **8,5 % des serveurs MCP implémentent OAuth 2.1** (pourtant obligatoire dans la spec) ;
- seulement **41 % des responsables tech déclarent un usage en prod**, même limité ;
- la **sécurité est le 1ᵉʳ bloquant** au déploiement ;
- la spec 2026-07-28 est passée en *stateless* avec routing par headers (`Mcp-Method`, `Mcp-Name`), HTTP natif, MRTR, listes cachables — donc beaucoup de serveurs sont déjà obsolètes ;
- OWASP a publié le **Top 10 des risques des applications agentiques 2026** ;
- autre angle mort : un serveur avec 100 outils fait payer au modèle toute la surface avant même la première question, et la sélection d'outils se dégrade à mesure que la liste grandit (le roadmap MCP parle de « progressive discovery »).

Traduction : **tout le monde branche des outils, presque personne ne les vérifie ni ne les gouverne.**

### Le produit (deux niveaux)
**A. MCP-Lint — gratuit / open-source, entonnoir d'acquisition**
Tu pointes une URL ou un dépôt, tu obtiens :
- une note sur 100 ;
- les findings : OAuth 2.1 absent, scopes trop larges, trop d'outils exposés, pas de rate limiting, secrets dans la config, pas de journal d'audit, spec obsolète ;
- un rapport HTML lisible + un JSON machine-readable (cf. `cloudflare/security-audit-skill`, +43 k étoiles en 30 j) ;
- un badge « MCP-Lint checked » à mettre dans un README.

**B. MCP-Guard — payant, le vrai business**
Un proxy local qui se place devant n'importe quel serveur MCP :
- règles « qui peut appeler quoi » (par agent, par utilisateur, par outil) ;
- **budget par outil** et arrêt net à la limite ;
- **approbation humaine** obligatoire pour les outils destructifs (remboursement, suppression, envoi d'email) ;
- redaction des champs sensibles dans les réponses ;
- journal d'audit immuable : quoi, quand, pour qui, avec quelle autorisation ;
- routing par headers conforme à la spec 2026-07-28.

### Qui paie et pourquoi
- **Platform teams / AI leads** qui doivent prouver à leur RSSI que les agents sont cadrés.
- **Agences** qui construisent des agents pour des clients et ont besoin d'un argument de confiance.
- **Auteurs de serveurs MCP** qui veulent être « certified » pour être adoptés.
Le budget existe déjà : c'est celui de la sécurité et de la conformité, pas celui de l'innovation.

### Prix
- Lint gratuit (open core).
- Guard : **79 $/mois** équipe, **299 $/mois** organisation (multi-environnements, SSO, audit export).

### Faisabilité
**Moyenne.** TypeScript/Node + SDK MCP 2026-07-28, moteur de règles simple, SQLite pour les logs, CLI + proxy HTTP. Le dur n'est pas le code, c'est de rester compatible avec l'évolution rapide de la spec.

### Acquisition
1. Lancer le lint sur les **100 serveurs MCP les plus populaires**, publier un classement (« 8,5 % sont conformes — devinez qui »). Ça crée du bruit et de la données.
2. Badge + GitHub open core → distribution gratuite.
3. Article : « Votre serveur MCP est probablement non conforme — voici comment le vérifier en 30 secondes ».
4. Product Hunt + communautés MCP/agent.

### Risques / kill condition
- Risque : le standard bouge vite et le proxy devient un produit de compatibilité chronique.
- Risque : les gateways enterprise (IBM watsonx AI Gateway, Cortex AI Gateway) écrasent le marché haut de gamme.
- **Kill** : si après 100 scans et 2 semaines de diffusion, moins de 10 personnes demandent la version payante → arrêter le proxy, garder le lint comme outil gratuit / personal branding.

### Test à 7 jours
Jour 1–2 : version minimale du lint (même une checklist + audits manuels si besoin). Jour 3–4 : scanner 20 serveurs publics. Jour 5 : publier le classement avec un bouton « demander Guard ». Jour 6–7 : compter les demandes et interroger 5 d'entre elles sur leur budget sécurité.

---

## 2. VibeFix — service de secours pour applications « vibe-codées »

### Le problème
Des fondateurs non techniques livrent un MVP avec Lovable / Cursor / Claude, puis **heurtent un mur** : timeouts, logique lourde coincée dans le frontend, aucun test, aucune gestion d'erreurs, des secrets dans le code. Et ils ne peuvent pas le réparer eux-mêmes.
Signal Reddit identifié dans la recherche : *« Rescue service for vibe-coded apps »* — **10 plaintes dont 7 de forte urgence**. Citation clé : « *A hundred tools help you generate an app. Almost nothing audits and hardens the mess afterward for someone who cannot read the code.* »
Ça recoupe les données Jellyfish : les agents touchent 27,7 % des PR mais les humains signent presque tout ; et Gartner : un bon harness réduit de 60 % les défauts post-déploiement.

### Le produit
Ce n'est **pas un logiciel au début, c'est un service productisé** — prix fixe, périmètre fixe, délai fixe.

**Diagnostic — 299 $, 48 h**
- Rapport en langage clair : ce qui est cassé, ce qui est risqué, ce qui coûte de l'argent.
- Score santé avant/après avec preuves (screenshots, commandes, logs).

**Fix — 499 $, 5 jours**
- Le rapport + les corrections : secrets externalisés, auth, gestion d'erreurs, tests critiques, CI minimale, sauvegardes, rate limiting, plafonds de coût API.
- Une vidéo de 30 min qui explique — *sans jargon* — ce qui a été fait et pourquoi.

**Rescue — 999 $**
- Réécriture des parties critiques + transfert de propriété propre (repo, docs, déploiement).

Option : **99 $/mois** de surveillance (monitoring + alertes + 1 correctif/mois).

### Qui paie et pourquoi
- Fondateur solo dont le produit commence à avoir des users et qui casse.
- Indie hacker qui doit pitcher/démo dans 2 semaines et qui a peur que ça tombe.
- Petite agence qui a hérité d'un codebase généré et qui ne sait pas le lire.
L'urgence est **temporelle et émotionnelle** : l'outil casse au mauvais moment. C'est une des rares catégories où le client paie vite.

### Prix
Voir paliers ci-dessus. Le prix fixe est un choix stratégique : avec 51 % des apps qui se font descendre pour des histoires de facturation opaque, afficher 499 $ et « c'est tout » est un argument marketing.

### Faisabilité
**Facile.** Aucun produit à coder au départ. Il faut juste être à l'aise pour lire du code généré et documenter. Le vrai travail est commercial, pas technique.

### Acquisition
1. Répondre aux posts « mon app Lovable bug, HELP » dans les communautés avec une **mini-audit offert** : « envoie le repo, je te dis les 3 plus gros risques en 24 h ».
2. Convertir avec le témoignage : « j'ai trouvé tes clés API en dur dans le frontend, ça fait 3 mois que tu es exposé » → confiance immédiate.
3. Publier des avant/après anonymisés avec screenshots.
4. Partenariat avec des freelances / consultants qui font du growth et qui récupèrent ces dossiers.

### Risques / kill condition
- Risque : glisser vers du sur-mesure infini et devenir une ESN déguisée → **périmètre fixe, zéro support ouvert, limite de 2 tours de corrections**.
- Risque : le client ne comprend pas la valeur d'un rapport et ne veut payer que pour le « fix » → vendre directement le palier 499 $.
- **Kill** : moins de 3 audits payés en 30 jours après 50 conversations → arrêter.

### Test à 7 jours
Zéro code. Jour 1 : landing page avec les 3 paliers + lien Stripe. Jour 2–3 : poster dans 5 communautés. Jour 4–5 : faire 5 audits gratuits contre témoignage. Jour 6–7 : proposer le palier payant aux 5 et mesurer.

---

## 3. CapSwitch — plafond de dépense dur pour agents IA

### Le problème
Le coût des agents en production est **imprévisible**. Reddit : **15 plaintes, dont 11 de forte urgence**, et des équipes qui **codent leur propre plafond** parce qu'elles n'attendent pas un produit. Les outils de tracing existent (Langfuse, LangSmith) mais **le contrôle granulaire n'existe pas** : un plafond dur, par agent, qui coupe/net au moment où la limite est atteinte.
Chiffres à l'appui : factures Claude Code à **252 $/mois/développeur** chez les early adopters ; Gartner : **70 % des entreprises sandboxeront leurs workflows agentiques d'ici 2030** (10 % en 2026) ; et avec AP2 (paiements par agents), les agents vont bientôt **dépenser de l'argent réel**, pas seulement des tokens.

### Le produit
- **Une seule config** (fichier YAML ou dashboard) : limites par agent, par projet, par utilisateur — quotidiennes et mensuelles.
- **Application dure** : un proxy entre l'agent et le fournisseur de modèles. Quand la limite est atteinte, ça renvoie une erreur claire « budget épuisé » et **l'agent s'arrête** — pas un avertissement mou.
- Alertes à 50 / 80 / 100 %, kill switch manuel.
- **Attribution** : quel agent, quelle feature, quel utilisateur a brûlé quoi.
- **Explication** : pourquoi ça a coûté ce prix — tokens, retry, boucles, choix du modèle.
- Fonctionne avec OpenAI, Anthropic, modèles locaux ; **BYOK** (tes propres clés).
- Mode local : le proxy tourne sur ta machine, rien ne part.

### Qui paie et pourquoi
- Équipes qui mettent des agents en prod et qui ont déjà eu une mauvaise surprise.
- Agences avec plusieurs clients : elles doivent répartir le coût et ne pas manger leur marge.
- Devs indie qui ont peur du « runaway loop » à 3 h du matin.
Le lien émotionnel est fort : **« qui paie la note quand l'agent boucle ? »** — et souvent la réponse est « personne ne sait », ce qui est exactement le problème.

### Prix
- Gratuit : 1 agent, plafond 10 $.
- **39 $/mois** équipe.
- **99 $/mois** multi-projets + alertes Slack + export.

### Faisabilité
**Moyenne.** TypeScript, proxy HTTP, SQLite, webhooks. La difficulté technique est dans les détails : streaming, retries, plusieurs providers, erreurs renvoyées à l'agent sans casser son boucle. Prévoir 4–6 semaines pour une version solide.

### Acquisition
1. Capitaliser sur les histoires : « j'ai eu une facture de 400 $ à cause d'un agent qui bouclait » → répondre avec le produit.
2. Se positionner en **complément** de Langfuse, pas en concurrent : « eux te montrent, nous on arrête ».
3. Démo visuelle : un dashboard avec une ligne rouge qui coupe net la dépense. C'est l'image qui vend.
4. Contenu : « 5 façons dont un agent dépense votre budget sans que vous le voyiez ».

### Risques / kill condition
- Risque : les fournisseurs de modèles ajoutent des plafonds natifs → se différencier par le multi-provider et l'explication, pas par le coupe-circuit seul.
- Risque : les gens disent « on le fait avec un cron + un spreadsheet » → c'est un vrai signal faible de paiement.
- **Kill** : si 10 équipes interrogées répondent « on n'a jamais dépassé » ou « le budget est déjà géré en interne et on ne paierait pas pour ça » → abandonner.

### Test à 7 jours
Jour 1 : landing + formulaire « quel est votre pire facture d'agent ? » (le formulaire collecte des histoires = contenu + validation). Jour 2–3 : une vidéo de démo simulée du proxy qui coupe. Jour 4–7 : 10 appels à des équipes qui utilisent des agents en prod. Question unique : « qui paie quand un agent boucle ? » Si la réponse est floue, c'est bon signe.

---

## 4. Dedupe-toi-même — retrouver ta voix dans un monde de slop

### Le problème
Le marché sature de contenu générique et **les audiences fuient** :
- 56 % des consommateurs voient du « AI slop » souvent ou très souvent ;
- **50 % des Gen Z et 44 % des Millennials** ont désabonné / masqué une marque pour cause de slop ;
- 33 % disent que **l'originalité** est le 2ᵉ critère qui fait d'une marque leur préférée ;
- « no ai slop » : **20 → 1 900 recherches/mois en 12 mois (+9 400 %)**, et « lore » a été élu mot de l'année 2026.

Le piège des détecteurs IA classiques : ils se trompent (Kurzgesagt s'est fait classer « AI slop » alors que sa vidéo était animée à la main, et sa portée s'est effondrée — c'est d'ailleurs le déclencheur de la vague de juillet). **Détecter l'IA est un faux problème. Le vrai problème, c'est de sonner comme tout le monde.**

Le No AI Slop Manifesto le formule bien : « *Slop is when we put less effort into producing something than we ask the consumer to spend understanding it.* »

### Le produit
Un **ancrage de style**, pas un détecteur.
1. Tu importes tes **propres** écrits passés (articles, posts, emails, notes). Tout reste en local.
2. L'outil construit une **empreinte de voix** : longueur moyenne des phrases, mots favoris, mots interdits, habitudes de ponctuation, rythme, registre.
3. Tu colles un brouillon — même généré par une IA — et l'outil surligne les phrases génériques et propose des remplacements **tirés de ton propre corpus**.
4. Le score n'est pas « est-ce de l'IA ? » mais **« est-ce que ça sonne comme toi ? »**.
5. Bonus : export d'un **style guide Markdown** que tu peux donner à n'importe quel outil IA pour qu'il écrive dans ta voix.
6. Extension navigateur pour LinkedIn / X / Gmail + app web.

### Qui paie et pourquoi
- Créateurs, fondateurs, consultants, marketers qui publient sous leur nom.
- Agences qui gèrent la voix de marques de plusieurs clients.
Le déclencheur : ils viennent de publier un truc et ils le trouvent « fade » sans savoir pourquoi.

### Prix
- **8 $/mois** particulier, **15 $/mois** créateur pro, **29 $/mois** équipe (profils de voix partagés).

### Faisabilité
**Facile pour le MVP.** Statistiques simples sur le corpus + récupération de phrases similaires (pas besoin de gros modèle), TypeScript, extension navigateur, stockage local. Le vrai défi est l'**activation** : il faut que l'utilisateur importe ses écrits — c'est l'étape où beaucoup abandonnent.

### Acquisition
1. Appliquer l'outil à 20 posts de marques connues et publier les avant/après (« on a passé 50 posts LinkedIn dans un filtre de voix »).
2. Partenariat avec des consultants en brand voice (le skill `brand-voice` existe d'ailleurs dans ton environnement).
3. Contenu : « 12 phrases qui font que votre post sonne comme un robot ».
4. Se présenter explicitement comme **anti-détecteur** : « on ne devine pas si c'est l'IA, on mesure si c'est vous ».

### Risques / kill condition
- Risque : l'IA s'améliore et le « générique » devient plus subtil → le corpus local reste l'avantage.
- Risque : l'activation (importer ses écrits) est trop frictionnelle.
- **Kill** : si 50 inscriptions donnent <10 profils de voix créés, le problème n'est pas l'idée mais l'onboarding → le refaire une fois, puis arrêter si ça ne bouge pas.

### Test à 7 jours
**Sans code.** Demander à 5 personnes 10 de leurs anciens posts, construire manuellement un profil de style dans un tableur, réécrire 3 de leurs posts récents, leur demander « est-ce que tu publierais ça ? ». Si oui → l'outil a de la valeur.

---

## 5. Renewal Radar — ne plus jamais rater une expiration de licence

### Le problème
Des professionnels titulaires d'une licence ou d'une certification **oublient leurs échéances de formation continue (CE) et de renouvellement**, et se retrouvent avec une amende — ou dans l'incapacité de vendre. C'est ennuyeux, **récurrent, et à conséquence financière directe**.
Données :
- outils de conformité (SOC2 / RGPD / réglementaire) : **MRR médian 22 000 $ en année 2**, délai 9–12 mois — la catégorie la plus payante du catalogue ;
- « license / certification renewal tracker » : signal explicite — « *a lapsed license can stop an agency from selling, so the tool becomes insurance against disaster* » ;
- les 4 catégories de problèmes que les gens paient (PainBase) incluent **conformité & risque** au sommet, parce que le coût de l'échec est une amende, un procès, une radiation ;
- langage détecteur : « on doit prouver », « notre auditeur l'exige », « on est responsable si… ».

### Le produit
- Import des licences / certifications (HVAC, immobilier, nursing, cosmétologie, conseillers financiers, etc.).
- Suivi des **crédits de formation continue** requis vs obtenus, des dates de renouvellement, des justificatifs.
- Alertes **SMS + email** à J-90, J-60, J-30, J-7.
- Stockage des PDF de preuve avec date d'expiration.
- Export « **dossier de conformité** » prêt pour un audit.
- Vue équipe : qui est sur le point de perdre sa licence.
- À terme : récupération automatique depuis les sites des ordres professionnels (mais **commencer manuel**, c'est trop fragile).

### Qui paie et pourquoi
- Le professionnel indépendant : **19 $/mois**.
- Le petit cabinet / agence : **49–99 $/mois** par équipe.
- Les revendeurs de formations CE : version white-label.
L'acheteur est souvent le propriétaire ou l'assistant(e) de direction. Le calcul est simple : 500 $/an pour éviter une amende de 5 000 $ ou un mois sans pouvoir vendre.

### Prix
Voir ci-dessus. Le positionnement « assurance » autorise un prix qui ne se discute pas trop.

### Faisabilité
**Facile.** App web, Postgres, cron, Twilio pour les SMS, stockage PDF. 3–4 semaines pour une v1. Le dur n'est pas la technique, c'est la **couverture des règles par profession** — d'où le choix de n'en faire **qu'une seule au début**.

### Acquisition
1. Choisir **une seule profession dans une seule région** (ex. agents immobiliers d'un État, ou chauffagistes d'un département).
2. Posts dans les groupes Facebook / forums de cette profession : « les 5 échéances que tout le monde oublie dans votre métier ».
3. Partenariat avec les **organismes de formation continue** : ils ont intérêt à ce que leurs élèves restent en règle.
4. Témoignage roi : « j'ai évité une amende de X € grâce à l'alerte J-60 ».

### Risques / kill condition
- Risque : l'ordre professionnel envoie déjà de bons rappels → dans ce cas, il n'y a pas de workaround, donc pas de douleur payante.
- Risque : les règles changent souvent et la maintenance devient lourde → commencer avec une seule juridiction.
- **Kill** : si 10 pros interrogés répondent « l'ordre m'envoie un email, je n'ai jamais eu de souci » → passer à une autre profession ou abandonner. Si au contraire tu vois un tableur, un rappel dans le téléphone, ou « je me suis déjà fait avoir » → c'est gagné.

### Test à 7 jours
Jour 1–3 : 10 entretiens avec des pros d'une seule profession. Leur poser une seule question : **« comment sais-tu que ta certification expire ? »** et **demander à voir leur système** (souvent un spreadsheet). Jour 4–5 : vendre manuellement un « setup + première année » à 49 $ avant d'automatiser quoi que ce soit. Jour 6–7 : si au moins 1 personne paie, construire le automate.

---

## La règle commune aux 5

Aucune de ces idées ne se lance en écrivant du code d'abord. La séquence est toujours :

**workaround observable → interview → paiement manuel → automatisation**

Et dans tous les cas : **prix affiché, périmètre fixe, kill condition écrite à l'avance.**
