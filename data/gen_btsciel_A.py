# -*- coding: utf-8 -*-
"""Generateur btsciel-mat-part-A.json — lot A : Informatique (12), Maths / stats (8).

20 fiches 'prototype' pour la filiere bts-ciel (BTS1 / BTS2) :
12 points de cours, 10 questions corrigees (8 QCM + 2 texte),
7 blocs en ordre strict, 3 schemas via diag().
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _btsciel_common import FIL, REF, S, R, QC, QT, C, build, valider_et_ecrire

F = []

def add(prefix, titre, mat, ans, points, questions, c):
    F.append(build(prefix, titre, mat, ans, points, questions, c))

# ============================================================ IN1
add("IN1", "Architecture réseau : modèles, topologies et équipements", "Informatique", ["BTS1"],
S("Une architecture réseau décrit la disposition des équipements, des liens physiques ou logiques et des services afin de répondre à un besoin de communication."
  "|Le modèle OSI découpe la communication en sept couches : physique, liaison, réseau, transport, session, présentation, application ; chaque couche rend un service à la couche supérieure."
  "|Le modèle TCP/IP, issu d'Internet, regroupe ces fonctions en quatre couches : accès réseau, Internet, transport et application ; c'est le référentiel pratique de l'option IR."
  "|Le commutateur (switch) relie les machines d'un même réseau local à la couche 2 et commute les trames selon les adresses MAC."
  "|Le routeur interconnecte des réseaux distincts à la couche 3 : il consulte sa table de routage et transmet les paquets vers le saut suivant."
  "|Les topologies courantes sont l'étoile (switch central), le bus, l'anneau et la topologie maillée ; l'étoile est la plus déployée en LAN pour sa facilité de diagnostic."
  "|On distingue le LAN (local), le MAN (métropolitain) et le WAN (étendu), selon l'étendue géographique et le prestataire qui fournit les liens."
  "|Un plan d'adressage assigne les plages IPv4 ou IPv6, les masques et les passerelles ; il évite les collisions et rend la documentation exploitable."
  "|Les VLAN segmentent un réseau physique en réseaux logiques distincts : ils limitent les domaines de diffusion et permettent d'appliquer des politiques de sécurité différentes."
  "|La redondance des liens et des équipements supprime les points de défaillance uniques ; STP/RSTP évite les boucles dans les réseaux commutés redondants."
  "|Le dimensionnement tient compte du débit, de la latence, du nombre de ports, de la croissance prévue et du coût : un excès de capacité coûte cher, un défaut produit des goulots d'étranglement."
  "|La documentation (schéma physique, schéma logique, plan d'adressage, inventaire) est un livrable attendu d'un projet E4 : elle permet l'exploitation et la maintenance en option IR."),
[QC("Combien de couches compte le modèle OSI ?", "4~5~7~9", 2,
     "Le modèle OSI comporte sept couches, de la physique à l'application."),
 QC("À quelle couche OSI le commutateur fonctionne-t-il principalement ?", "Couche 1~Couche 2~Couche 3~Couche 7", 1,
     "Le switch commute des trames à la couche 2 à partir des adresses MAC."),
 QC("Quel équipement interconnecte deux réseaux IP distincts ?", "Le hub~Le routeur~La carte réseau~L'imprimante", 1,
     "Le routeur travaille à la couche 3 et utilise une table de routage."),
 QC("Quelle topologie est la plus courante dans un réseau local moderne ?", "Le bus~L'anneau~L'étoile~La ligne", 2,
     "L'étoile, avec un switch central, facilite le câblage et le diagnostic."),
 QC("Que permet un VLAN ?", "Augmenter la bande passante physique~Segmente logiquement un réseau~Remplacer un routeur~Supprimer les adresses IP", 1,
     "Le VLAN crée des domaines de diffusion logiques indépendants du câblage."),
 QC("Quel protocole évite les boucles dans un réseau commuté redondant ?", "STP~SMTP~SNMP~FTP", 0,
     "STP (Spanning Tree Protocol) bloque les liens redondants pour supprimer les boucles de couche 2."),
 QC("Quelle est la finalité d'un plan d'adressage ?", "Définir les couleurs des câbles~Attribuer de façon unique les plages IP et passerelles~Augmenter le débit~Remplacer le DNS", 1,
     "Un plan d'adressage documente les plages, masques et passerelles et évite les conflits."),
 QC("Quel est un livrable attendu d'un projet d'architecture réseau en option IR ?", "Le seul schéma de câblage~Le schéma logique et le plan d'adressage~Le devis fournisseur~Le procès-verbal de réunion", 1,
     "Les schémas physique et logique, le plan d'adressage et l'inventaire sont des livrables du projet."),
 QT("Expliquer la différence entre le modèle OSI et le modèle TCP/IP et dire lequel sert de référence pratique pour administrer un réseau.",
    "L'OSI est un modèle pédagogique de sept couches qui sépare finement les fonctions (session et présentation comprises). TCP/IP est le modèle concret d'Internet, en quatre couches, directement associé aux protocoles réels (IP, TCP, UDP, HTTP). Pour administrer un réseau, on se réfère à TCP/IP : c'est lui qui décrit les paquets, les ports et les services effectivement observés avec les outils de diagnostic.",
    "On oppose le cadre théorique en sept couches au modèle opérationnel en quatre couches, puis on justifie le choix par les protocoles mis en œuvre."),
 QT("Un site comporte 40 postes, deux serveurs et une liaison WAN. Décrire les étapes de conception d'une architecture répondant au besoin.",
    "On recense les besoins (postes, serveurs, débits, croissance), on choisit une topologie en étoile avec switchs, on définit les VLAN (postes, serveurs, administration), on établit le plan d'adressage et les masques, on place le routeur et le firewall aux points de sortie, on prévoit la redondance des liens critiques avec STP, puis on produit les schémas physique et logique et le plan de tests (connectivité, débit, bascule).",
    "La démarche attendue est : besoins, topologie, segmentation, adressage, équipements de sécurité, redondance, documentation et validation.")],
C("Une architecture réseau est la carte des équipements, des liens et des services : elle se lit avec les modèles OSI ou TCP/IP et se documente avant d'être construite.",
  "Réseau exploitable = équipements + adressage + segmentation + documentation",
  "OSI : 7 couches · TCP/IP : 4 couches · livrables : schémas physique, logique, plan d'adressage",
  "Switch~Couche 2~Adresses MAC~Routeur~Couche 3~Tables de routage~VLAN~Couche 2~Domaines de diffusion",
  "Recenser les besoins et la croissance|Choisir la topologie et les équipements|Définir les VLAN et le plan d'adressage|Prévoir redondance et sécurité|Dessiner les schémas et tester la connectivité",
  "Confondre switch et routeur|Oublier la passerelle par défaut|Nommer les VLAN sans documenter leur usage|Négliger la croissance future du parc",
  "Postes~LAN de 40 machines sur switchs~Serveurs~VLAN dédié avec accès contrôlé~Liaison WAN~Routeur vers le prestataire~Redondance~Deux liens avec STP~Documentation~Schémas et plan IP à jour",
  "OSI~7 couches~Modèle pédagogique~Référentiel d'enseignement~TCP/IP~4 couches~Modèle opérationnel~Protocoles d'Internet",
  "Switch~Couche 2~Même réseau local~Routeur~Couche 3~Entre deux réseaux"))

# ============================================================ IN2
add("IN2", "Protocoles TCP/IP : adressage, encapsulation et diagnostic", "Informatique", ["BTS1"],
S("La suite TCP/IP est un ensemble de protocoles organisés en couches qui permet à des hôtes de communiquer sur un réseau de réseaux."
  "|IPv4 utilise une adresse de 32 bits notée en quatre octets décimaux ; IPv6 utilise 128 bits notés en hexadécimal et offre un espace d'adresses considérablement plus vaste."
  "|Une adresse IP se compose d'une partie réseau et d'une partie hôte ; le masque de sous-réseau détermine la frontière entre les deux."
  "|Le CIDR note le masque par le nombre de bits à 1, par exemple 192.168.10.0/24 correspond à 255.255.255.0."
  "|TCP est un protocole de transport orienté connexion : il établit une connexion en trois échanges (SYN, SYN-ACK, ACK), garantit la livraison et contrôle la congestion."
  "|UDP est sans connexion et sans garantie de livraison ; il est plus léger et adapté au temps réel, à la voix ou au DNS."
  "|Un numéro de port identifie un service applicatif : 80 pour HTTP, 443 pour HTTPS, 22 pour SSH, 53 pour DNS, 3389 pour RDP."
  "|Le protocole ARP associe une adresse IPv4 à une adresse MAC sur un même réseau local ; la table ARP conserve ces correspondances temporairement."
  "|Le protocole ICMP sert au diagnostic : ping teste la joignabilité et traceroute révèle les routeurs traversés."
  "|L'encapsulation ajoute des en-têtes à chaque couche : données, segment TCP, paquet IP, trame Ethernet, bits sur le support."
  "|Le DNS traduit un nom de domaine en adresse IP ; sans résolution DNS, une machine peut être joignable par IP mais pas par son nom."
  "|La capture de trames (Wireshark) et la lecture des en-têtes sont des compétences de diagnostic attendues en exploitation et maintenance (unité U5)."),
[QC("Combien de bits compte une adresse IPv4 ?", "16~32~64~128", 1,
     "IPv4 utilise 32 bits, soit quatre octets ; IPv6 utilise 128 bits."),
 QC("Que signifie le suffixe /24 dans 192.168.10.0/24 ?", "24 hôtes maximum~24 bits de masque à 1~24 routeurs~24 octets", 1,
     "La notation CIDR /24 indique que les 24 premiers bits du masque sont à 1 (255.255.255.0)."),
 QC("Quel protocole de transport garantit la livraison des données ?", "UDP~IP~TCP~ARP", 2,
     "TCP est orienté connexion, accusé réception et contrôle la congestion ; UDP ne garantit rien."),
 QC("Quel port est associé au service HTTPS ?", "22~53~80~443", 3,
     "443 est le port du HTTP sécurisé (TLS) ; le HTTP non chiffré utilise le port 80."),
 QC("À quoi sert le protocole ARP ?", "Traduire un nom en IP~Associer une IPv4 à une adresse MAC~Chiffrer les paquets~Tester la connectivité", 1,
     "ARP résout l'adresse IPv4 en adresse MAC sur le même réseau local."),
 QC("Quel outil permet de visualiser les trames et leurs en-têtes ?", "ping~traceroute~Wireshark~nslookup", 2,
     "Wireshark est un analyseur de protocoles qui capture et décode les trames."),
 QC("Quel protocole est utilisé par la commande ping ?", "ICMP~SMTP~SSH~DHCP", 0,
     "ping envoie des requêtes Echo ICMP et attend des réponses Echo Reply."),
 QC("Dans l'ordre, quelle est la suite d'encapsulation correcte ?", "Trame, paquet, segment, données~Données, segment, paquet, trame~Paquet, trame, segment, données~Données, trame, paquet, segment", 1,
     "Les données sont encapsulées en segment TCP, puis en paquet IP, puis en trame Ethernet."),
 QT("Une machine ping son adresse IP de passerelle avec succès mais n'atteint pas un serveur Internet. Expliquer le diagnostic à conduire.",
    "Le ping de la passerelle valide la couche 2 et le réseau local. On vérifie ensuite la table de routage et la route par défaut, puis le masque et l'adresse du serveur DNS. On teste une adresse IP publique connue pour distinguer une panne de résolution DNS d'une panne de routage ou de firewall. On utilise traceroute pour localiser le saut qui bloque, puis on contrôle les règles de filtration et la connectivité du prestataire.",
    "On procède du local vers le distant : liaison, routage, DNS, puis filtrage, avec traceroute pour isoler le saut fautif."),
 QT("Expliquer pourquoi TCP utilise une connexion en trois temps et ce qui se passe si le troisième message n'arrive pas.",
    "Les trois échanges SYN, SYN-ACK, ACK permettent aux deux hôtes de confirmer leur disponibilité et de synchroniser leurs numéros de séquence avant de transmettre des données. Si l'ACK ne parvient pas, le serveur ne considère pas la connexion comme établie : il attend, puis abandonne après un délai et libère les ressources. Le client peut réémettre le SYN ; c'est ce mécanisme qui évite les connexions fantômes et permet de détecter une erreur de réseau avant l'envoi des données utiles.",
    "La réponse doit citer la synchronisation des séquences et le comportement en cas d'absence de ACK (attente, expiration, libération).")],
C("TCP/IP organise la communication en couches : IP transporte les paquets, TCP ou UDP les ports, et les outils de diagnostic lisent les en-têtes pour localiser une panne.",
  "Adresse IP + masque + passerelle + DNS = connectivité complète",
  "TCP : fiable et orienté connexion · UDP : léger et sans garantie · ICMP : diagnostic",
  "IPv4~32 bits~Notation décimale~IPv6~128 bits~Notation hexadécimale~Masque /24~255.255.255.0~256 adresses",
  "Vérifier l'adresse IP et le masque|Pinger la passerelle|Tester une IP distante|Tester la résolution DNS|Analyser la capture de trames",
  "Oublier le masque dans un plan d'adressage|Confondre port et adresse IP|Cacher les en-têtes lors d'une capture|Croire que ping teste un service applicatif",
  "Ping~Réponse ICMP reçue~Traceroute~Liste des sauts~Wireshark~En-têtes IP et TCP~nslookup~Adresse renvoyée par le DNS~Port 443~Service HTTPS",
  "TCP~Connexion SYN SYN-ACK ACK~Livraison garantie~UDP~Sans connexion~Faible latence",
  "Adresse IP~Identifie une machine~Numéro de port~Identifie un service"))

# ============================================================ IN3
add("IN3", "Sécurité des réseaux : risques, modèles et bonnes pratiques", "Informatique", ["BTS1"],
S("La sécurité des réseaux vise à protéger la confidentialité, l'intégrité et la disponibilité des informations et des services, le modèle dit CID."
  "|Une menace est un événement potentiellement nuisible ; une vulnérabilité est une faiblesse exploitable ; un risque combine la probabilité d'occurrence et l'impact."
  "|La surface d'attaque regroupe tous les points d'entrée possibles : ports ouverts, services exposés, comptes, applications web, périphériques et liens sans fil."
  "|Le modèle de défense en profondeur superpose plusieurs barrières : segmentation, filtrage, authentification, chiffrement, supervision et sauvegarde."
  "|Le principe du moindre privilège accorde à chaque utilisateur ou service uniquement les droits nécessaires à sa tâche."
  "|La segmentation réseau (VLAN, zones DMZ) limite le déplacement latéral d'un attaquant une fois un poste compromis."
  "|Le chiffrement des échanges (TLS, IPsec, WPA2/WPA3) protège les données en transit contre l'écoute et la modification."
  "|Les mises à jour et la gestion des correctifs réduisent l'exposition aux vulnérabilités connues : c'est la remédiation."
  "|Les journaux et la supervision permettent de détecter les comportements anormaux et de reconstituer un incident après coup."
  "|La sauvegarde, testée régulièrement par restauration, est le dernier rempart contre le chiffrement par rançongiciel."
  "|La sensibilisation des utilisateurs traite le facteur humain : hameçonnage, ingénierie sociale et mots de passe faibles restent des vecteurs majeurs."
  "|En option IR, la compétence « Valorisation de la donnée et cybersécurité » (U6) mobilise ces connaissances pour évaluer, durcir et défendre un système."),
[QC("Que désigne le modèle CID ?", "Confidentialité, Intégrité, Disponibilité~Commande, Installation, Audit~Cryptage, Identification, Accès~Contrôle, Inventaire, Analyse", 0,
     "CID est le trio Confidentialité, Intégrité, Disponibilité, pilier de la sécurité de l'information."),
 QC("Qu'appelle-t-on surface d'attaque ?", "La taille du pare-feu~L'ensemble des points d'entrée exploitables~Le nombre d'utilisateurs~La bande passante", 1,
     "La surface d'attaque comprend tous les services, ports, comptes et équipements accessibles."),
 QC("Quel principe limite les droits d'un compte au strict nécessaire ?", "Défense en profondeur~Moindre privilège~Séparation des tâches~Redondance", 1,
     "Le moindre privilège réduit l'impact d'une compromission de compte."),
 QC("Quel mécanisme protège les données en transit sur un réseau sans fil ?", "STP~WPA2 ou WPA3~ARP~DHCP", 1,
     "WPA2/WPA3 chiffre les échanges Wi-Fi ; TLS protège les applications, IPsec les tunnels IP."),
 QC("Que permet la segmentation réseau ?", "Augmenter le débit~Limiter le déplacement latéral~Supprimer les mots de passe~Remplacer les sauvegardes", 1,
     "Des VLAN et une DMZ isolent les zones et freinent la propagation d'une attaque."),
 QC("Quelle mesure traite directement le risque de rançongiciel ?", "Une sauvegarde testée et isolée~Un câble plus court~Un switch supplémentaire~Une adresse IP statique", 0,
     "Une sauvegarde restaurée régulièrement et non accessible depuis le réseau de production permet la reprise."),
 QC("Quel vecteur d'attaque repose sur l'ingénierie sociale ?", "La panne matérielle~Le hameçonnage~L'usure d'un câble~La saturation d'un lien", 1,
     "Le hameçonnage trompe l'utilisateur pour obtenir des identifiants ou déclencher une action."),
 QC("À quelle unité du BTS CIEL se rattache la compétence cybersécurité en option IR ?", "U1~U3~U6~UF1", 2,
     "L'unité U6 correspond au bloc « Valorisation de la donnée et cybersécurité » de l'option A."),
 QT("Définir la relation entre menace, vulnérabilité et risque, puis illustrer avec un poste non mis à jour.",
    "Une menace est un acteur ou un événement hostile (un attaquant, un logiciel malveillant) ; une vulnérabilité est une faiblesse du système (un service non corrigé) ; le risque est la combinaison de la probabilité que la menace exploite la vulnérabilité et de l'impact sur l'organisation. Pour un poste non mis à jour, la menace est un attaquant qui scanne les ports, la vulnérabilité est le correctif absent, et le risque est la prise de contrôle du poste puis le déplacement vers le serveur, avec un impact fort sur la confidentialité et la disponibilité.",
    "La réponse doit séparer les trois notions et montrer leur combinaison dans un exemple concret."),
 QT("Proposer une stratégie de défense en profondeur pour un site de 30 postes avec un serveur de données.",
    "On combinera : segmentation en VLAN (postes, serveurs, administration, invités) et DMZ ; filtrage par firewall avec règles par défaut restrictives ; authentification forte et moindre privilège ; chiffrement TLS/IPsec et WPA3 ; durcissement et correctifs automatiques ; antivirus et contrôle des périphériques ; supervision des journaux avec alertes ; sauvegardes 3-2-1 testées ; sensibilisation des utilisateurs au hameçonnage. Chaque couche compense la défaillance potentielle d'une autre, ce qui réduit le risque résiduel.",
    "On attend plusieurs couches complémentaires et la justification du principe de compensation.")],
C("La sécurité réseau ne repose pas sur un seul outil : elle superpose des barrières techniques et humaines pour réduire le risque résiduel.",
  "Risque = probabilité d'exploitation × impact",
  "CID : confidentialité, intégrité, disponibilité · défense en profondeur · moindre privilège",
  "Menace~Acteur ou événement hostile~Attaquant~Vulnérabilité~Faiblesse exploitable~Correctif absent~Risque~Probabilité × impact~Compromission du serveur",
  "Cartographier les actifs et la surface d'attaque|Évaluer les risques par impact et probabilité|Segmenter et appliquer le moindre privilège|Chiffrer, mettre à jour et superviser|Tester les sauvegardes et sensibiliser",
  "Croire qu'un firewall suffit|Laisser un compte administrateur partagé|Ne jamais tester la restauration|Ignorer le facteur humain",
  "CID~Confidentialité, intégrité, disponibilité~VLAN~Segmentation des flux~MFA~Authentification forte~3-2-1~3 copies, 2 supports, 1 hors site~U6~Valorisation et cybersécurité",
  "Menace~Peut provoquer le dommage~Vulnérabilité~Rend l'attaque possible",
  "Défense en profondeur~Multiplie les barrières~Barrière unique~Une seule défaillance suffit"))

# ============================================================ IN4
add("IN4", "Pare-feu et filtrage : règles, zones et journalisation", "Informatique", ["BTS1"],
S("Un pare-feu (firewall) contrôle les flux réseau selon une politique de sécurité définie : il autorise, refuse ou journalise les connexions."
  "|Le filtrage s'appuie sur des critères dits 5-tuples : adresse IP source, adresse IP destination, port source, port destination et protocole."
  "|Un firewall de couche 3 ou 4 travaille sur les adresses et les ports ; un firewall applicatif (couche 7) inspecte aussi le contenu des requêtes HTTP."
  "|Une règle se lit avec une action (ALLOW ou DENY), un sens (entrant ou sortant), des critères et une priorité d'évaluation."
  "|La politique par défaut doit être restrictive : on refuse tout ce qui n'est pas explicitement autorisé."
  "|Les zones de sécurité (INT, DMZ, EXT) matérialisent les niveaux de confiance ; une DMZ héberge les services exposés à Internet."
  "|Les listes de contrôle d'accès (ACL) sont évaluées de haut en bas : la première règle correspondante s'applique, d'où l'importance de l'ordre."
  "|Le firewall à état (stateful) suit l'état des connexions et autorise automatiquement les réponses à une connexion légitime."
  "|Le NAT (Network Address Translation) traduit les adresses privées en adresse publique et masque la topologie interne."
  "|La journalisation des flux et des refus alimente le SIEM et permet l'analyse forensique après incident."
  "|Les règles doivent être documentées, testées et revues : une règle obsolète élargit inutilement la surface d'attaque."
  "|Un changement de règle suit une procédure : demande, validation, application en fenêtre de maintenance, test puis archivage."),
[QC("Sur quels critères porte le filtrage du 5-tuples ?", "Adresse MAC et couleur du câble~IP source, IP destination, ports et protocole~Nom d'utilisateur et mot de passe~Uniquement le port destination", 1,
     "Le 5-tuples comprend les deux adresses IP, les deux ports et le protocole."),
 QC("Quelle doit être la règle par défaut d'un firewall ?", "Tout autoriser~Refuser tout ce qui n'est pas explicitement autorisé~Autoriser seulement le trafic sortant~Aucune règle par défaut", 1,
     "La politique restrictive « deny by default » limite la surface d'attaque."),
 QC("Que contient une DMZ ?", "Les postes de direction~Les services exposés à Internet~Les sauvegardes hors ligne~Les switchs d'accès", 1,
     "La DMZ isole les serveurs web, mail ou DNS accessibles depuis l'extérieur."),
 QC("Comment sont évaluées les règles d'une ACL ?", "De bas en haut~De haut en bas, première correspondance appliquée~Dans l'ordre alphabétique~Au hasard", 1,
     "L'ordre des règles est déterminant : la première correspondance s'applique."),
 QC("Qu'appelle-t-on firewall stateful ?", "Un firewall qui ne filtre que le HTTP~Un firewall qui suit l'état des connexions~Un firewall sans journalisation~Un firewall physique", 1,
     "Le firewall à état mémorise les connexions et autorise les réponses associées."),
 QC("À quoi sert le NAT ?", "Chiffrer les trames~Traduire des adresses privées en adresse publique~Augmenter le débit~Remplacer le DNS", 1,
     "Le NAT traduit les adresses et dissimule l'adressage interne."),
 QC("Quel protocole de gestion est couramment filtré pour l'administration distante sécurisée ?", "Telnet~SSH~FTP~HTTP", 1,
     "SSH chiffre l'administration ; Telnet et FTP transmettent les identifiants en clair."),
 QC("Pourquoi journaliser les flux refusés par le firewall ?", "Pour calculer la bande passante~Pour détecter les tentatives d'intrusion et reconstituer un incident~Pour réduire la latence~Pour bypasser les règles", 1,
     "Les journaux sont une source essentielle de détection et d'analyse forensique."),
 QT("Une règle autorise tout le trafic entrant vers le port 3389 depuis Internet. Expliquer le risque et la correction à apporter.",
    "Le port 3389 (RDP) expose l'administration à distance à tout attaquant : il permet des tests de mots de passe massifs et, en cas de vulnérabilité, une prise de contrôle du serveur. La correction consiste à supprimer cette règle, à placer l'accès derrière un VPN ou une passerelle d'accès, à limiter les adresses sources autorisées (liste blanche), à exiger une authentification multifacteur et à journaliser les tentatives. On applique la règle en fenêtre de maintenance, puis on teste l'accès légitime et le refus depuis une adresse non autorisée.",
    "On identifie le risque d'exposition, puis on propose filtrage par source, VPN, MFA et journalisation, avec test de la règle."),
 QT("Décrire la démarche de mise en place d'une politique de filtrage pour un site avec une DMZ.",
    "On inventorie d'abord les services et les flux nécessaires (qui parle à qui, sur quel port). On définit des zones (INT, DMZ, EXT) et une politique par défaut restrictive. On rédige les règles avec la règle la plus spécifique en premier, par exemple INT vers DMZ en HTTPS, EXT vers DMZ en 80/443 uniquement, DMZ vers INT interdit, INT vers EXT en HTTP/HTTPS via proxy. On documente chaque règle avec son motif et son responsable. On teste chaque flux autorisé et interdit, on active la journalisation, puis on planifie une revue périodique des règles inutilisées.",
    "La démarche attendue : inventaire des flux, zones, règle par défaut, ordre des règles, test, journalisation et revue.")],
C("Un firewall applique une politique de sécurité aux flux : par défaut on refuse, puis on autorise explicitement les services nécessaires entre zones.",
  "Règle = sens + 5-tuples + action + priorité",
  "Politique restrictive : deny by default · firewall stateful · journalisation des refus",
  "5-tuples~IP source et destination~Port source et destination~Protocole~Zone INT~Réseau interne de confiance~DMZ~Services exposés~Zone EXT~Internet",
  "Inventorier les flux nécessaires|Définir les zones et la politique par défaut|Rédiger les règles du plus spécifique au plus général|Tester autorisations et refus|Journaliser et revoir périodiquement",
  "Placer une règle large avant une règle précise|Autoriser RDP depuis Internet|Oublier de documenter le motif d'une règle|Ne jamais relire les règles obsolètes",
  "HTTPS~Port 443 vers la DMZ~SSH~Port 22 réservé à l'administration~RDP~Port 3389 à n'exposer qu'en VPN~Deny~Action par défaut~Logs~Preuves en cas d'incident",
  "Stateful~Suit l'état des connexions~Réponses autorisées~Stateless~Filtre chaque paquet isolément~Règles de retour nécessaires",
  "DMZ~Services publics~Zone INT~Postes et données internes"))

# ============================================================ IN5
add("IN5", "Réseaux privés virtuels (VPN) : tunnels et chiffrement", "Informatique", ["BTS1"],
S("Un VPN (Virtual Private Network) établit un lien chiffré entre deux points par-dessus un réseau non fiable, généralement Internet."
  "|Le tunneling encapsule les paquets d'origine dans de nouveaux paquets ; l'en-tête extérieur assure le transport, la charge utile est chiffrée."
  "|Le protocole IPsec fonctionne au niveau de la couche réseau : il protège les paquets IP entre hôtes ou entre passerelles avec les modes transport et tunnel."
  "|IPsec combinent AH (authentification et intégrité) et ESP (chiffrement, intégrité, authentification), avec le protocole IKE pour négocier les clés."
  "|Le protocole TLS, utilisé par SSL VPN, fonctionne au niveau applicatif et donne un accès contrôlé à des ressources sans exposer tout le réseau."
  "|OpenVPN et WireGuard sont des implémentations courantes : WireGuard se distingue par un code compact et l'usage de courbes cryptographiques modernes."
  "|Un VPN d'accès distant (remote access) connecte un télétravailleur au réseau de l'entreprise ; un VPN site à site relie deux passerelles permanentes."
  "|L'authentification des pairs s'appuie sur des certificats, des clés pré-partagées ou une authentification à deux facteurs."
  "|La confidentialité des données en transit et l'intégrité des paquets sont les deux garanties principales du tunnel."
  "|Le MTU effectif diminue à cause de l'encapsulation : un réglage inadapté provoque de la fragmentation et des performances dégradées."
  "|Le split tunneling autorise le trafic Internet à sortir directement du poste, ce qui améliore le débit mais réduit le contrôle de la sécurité."
  "|La journalisation des connexions VPN et la révocation des certificats sont nécessaires pour gérer les accès et répondre à un incident."),
[QC("Quel est le rôle principal d'un VPN ?", "Augmenter le débit d'Internet~Chiffrer les communications sur un réseau non fiable~Remplacer le DNS~Supprimer les mots de passe", 1,
     "Le VPN crée un tunnel chiffré entre deux points via un réseau non fiable."),
 QC("Quel protocole VPN travaille au niveau de la couche réseau ?", "TLS~IPsec~HTTP~SSH", 1,
     "IPsec protège directement les paquets IP, en mode transport ou en mode tunnel."),
 QC("Quelle différence essentielle entre AH et ESP en IPsec ?", "AH chiffre, ESP ne chiffre pas~AH authentifie et garantit l'intégrité, ESP chiffre aussi~AH sert au DNS, ESP au HTTP~Il n'y a aucune différence", 1,
     "AH n'assure pas la confidentialité ; ESP fournit chiffrement, intégrité et authentification."),
 QC("Quel protocole sert à négocier les associations de sécurité IPsec ?", "IKE~ARP~STP~SMTP", 0,
     "IKE (Internet Key Exchange) négocie les clés et les paramètres des tunnels IPsec."),
 QC("Qu'appelle-t-on VPN site à site ?", "Un VPN pour un seul poste~Une liaison chiffrée permanente entre deux passerelles~Un VPN sans authentification~Un tunnel HTTP", 1,
     "Le mode site à site relie deux réseaux via leurs passerelles VPN."),
 QC("Quel effet de l'encapsulation sur le MTU ?", "Le MTU augmente~Le MTU effectif diminue~Le MTU disparaît~Aucun effet", 1,
     "Les en-têtes supplémentaires réduisent la taille utile disponible et peuvent provoquer de la fragmentation."),
 QC("Quel est un risque du split tunneling ?", "Une latence plus faible~Le trafic Internet échappe aux contrôles de l'entreprise~Une consommation moindre~Une meilleure authentification", 1,
     "Le trafic direct n'est plus filtré ni supervisé par le réseau de l'entreprise."),
 QC("Quel mécanisme permet de révoquer l'accès d'un utilisateur VPN ?", "Changer le MTU~Révoquer son certificat~Désactiver le DNS~Augmenter le nombre de tunnels", 1,
     "La révocation du certificat ou du compte empêche une nouvelle connexion."),
 QT("Expliquer pourquoi un VPN site à site utilise le mode tunnel plutôt que le mode transport.",
    "En mode transport, seul le payload du paquet IP est protégé et l'en-tête d'origine reste visible : ce mode convient à une communication entre deux hôtes. Dans un VPN site à site, ce sont deux réseaux entiers qui doivent communiquer via Internet : le mode tunnel encapsule le paquet IP d'origine dans un nouveau paquet dont l'adresse destination est la passerelle distante. Les adresses privées internes sont ainsi masquées et transportées intactes à travers le réseau public.",
    "On oppose la protection du seul payload en mode transport à l'encapsulation complète du paquet en mode tunnel."),
 QT("Un télétravailleur se connecte en VPN mais ne peut pas atteindre l'intranet. Décrire les vérifications à effectuer.",
    "On vérifie d'abord l'établissement du tunnel : authentification, certificat valide, journal du client VPN, puis l'adresse IP attribuée au poste et les routes poussées par le serveur. On contrôle que la plage de l'intranet est bien incluse dans les routes du tunnel et qu'il n'y a pas de conflit avec le réseau local du télétravailleur. On teste la résolution DNS interne, puis les règles de filtrage entre le pool VPN et les serveurs. Enfin, on examine le MTU et les journaux du serveur pour détecter une fragmentation ou un rejet de politique.",
    "On suit l'ordre : tunnel, adressage et routes, DNS, filtrage, puis MTU et journaux.")],
C("Le VPN crée un tunnel chiffré à travers un réseau non fiable : IPsec protège les paquets IP, TLS protège les accès applicatifs.",
  "Tunnel = encapsulation + chiffrement + authentification des pairs",
  "IPsec : couche réseau (AH/ESP, IKE) · SSL/TLS VPN : couche applicative",
  "IPsec~Protège les paquets IP~Mode tunnel~Encapsule le paquet entier~Mode transport~Protège le payload~ESP~Chiffrement et intégrité",
  "Choisir le type de VPN|Configurer l'authentification et les certificats|Définir les routes et le pool d'adresses|Régler le MTU et tester le tunnel|Journaliser et gérer les révocations",
  "Utiliser des clés pré-partagées faibles|Oublier les routes vers l'intranet|Négliger le réglage du MTU|Laisser le split tunneling sans politique",
  "Remote access~Poste isolé vers l'entreprise~Site à site~Deux passerelles permanentes~WireGuard~Tunnel léger et rapide~Certificat~Révocable~IKE~Négociation des clés",
  "IPsec~Couche réseau~Tout le trafic IP~TLS VPN~Couche applicative~Accès à des services précis",
  "Tunnel complet~Tout passe par l'entreprise~Split tunneling~Internet sort en direct"))

# ============================================================ IN6
add("IN6", "Systèmes d'exploitation : processus, mémoire et droits", "Informatique", ["BTS1"],
S("Le système d'exploitation (OS) fait l'interface entre le matériel et les applications : il gère les ressources et fournit des services aux programmes."
  "|Le noyau (kernel) est le cœur de l'OS : il gère les processus, la mémoire, les pilotes de périphériques, les systèmes de fichiers et les appels système."
  "|Un processus est une instance d'un programme en cours d'exécution ; il possède un identifiant (PID), un espace d'adressage et un état (prêt, exécution, attente)."
  "|L'ordonnanceur répartit le temps processeur entre les processus selon des priorités et des algorithmes (FIFO, tourniquet, files multiclasses)."
  "|La mémoire virtuelle donne à chaque processus l'illusion d'un espace contigu ; la pagination découpe la mémoire en pages et le TLB accélère la traduction des adresses."
  "|Le swapping déplace des pages sur le disque en cas de manque de mémoire : il améliore la capacité mais dégrade fortement les performances."
  "|Le système de fichiers organise les données en fichiers et répertoires ; NTFS, ext4 et XFS sont des exemples courants, avec des droits et un journal de transactions."
  "|Les comptes et groupes définissent les identités ; les droits d'accès (lecture, écriture, exécution) sont contrôlés par le noyau à chaque appel système."
  "|Le contrôle d'accès discrétionnaire (DAC) laisse le propriétaire décider, tandis que le contrôle mandataire (MAC) applique une politique centrale, comme SELinux."
  "|Les services (daemon sous Unix) sont des processus d'arrière-plan qui attendent des requêtes ; leur durcissement est un axe clé de la sécurité système."
  "|Les journaux système (syslog, Event Viewer) consignent démarrages, erreurs et tentatives d'accès : ils alimentent la supervision et l'analyse d'incidents."
  "|La mise à jour du noyau et des paquets corrige les vulnérabilités : c'est une tâche courante d'exploitation et de maintenance de l'unité U5."),
[QC("Quel est le rôle du noyau d'un système d'exploitation ?", "Afficher l'interface graphique~Gérer les ressources et fournir les appels système~Stocker les mots de passe~Compresser les fichiers", 1,
     "Le noyau gère processus, mémoire, périphériques et systèmes de fichiers via les appels système."),
 QC("Qu'est-ce qu'un processus ?", "Un fichier de configuration~Une instance d'un programme en cours d'exécution~Un périphérique~Une partition disque", 1,
     "Un processus possède un PID, un état et un espace d'adressage propres."),
 QC("Quel composant répartit le temps CPU entre les processus ?", "Le compilateur~L'ordonnanceur~Le pilote réseau~Le défragmenteur", 1,
     "L'ordonnanceur applique une politique de priorité et d'allocation du processeur."),
 QC("À quoi sert la mémoire virtuelle ?", "À supprimer la pagination~À donner un espace d'adressage isolé à chaque processus~À augmenter la taille du disque~À chiffrer les fichiers", 1,
     "La pagination et la traduction d'adresses isolent les processus et optimisent la mémoire."),
 QC("Quel effet principal du swapping ?", "Il accélère les calculs~Il dégrade les performances lorsque le disque est sollicité~Il supprime les virus~Il augmente le débit réseau", 1,
     "Les échanges disque sont beaucoup plus lents que la mémoire vive."),
 QC("Quelle différence entre DAC et MAC ?", "DAC est plus sûr que MAC~DAC laisse le propriétaire décider, MAC applique une politique centrale~DAC concerne le réseau, MAC la mémoire~Il n'y a aucune différence", 1,
     "Le contrôle discrétionnaire dépend du propriétaire ; le contrôle mandataire est imposé par la politique de sécurité."),
 QC("Qu'appelle-t-on un daemon sous Unix ?", "Un utilisateur root~Un processus d'arrière-plan qui rend un service~Un fichier journal~Une commande de compression", 1,
     "Les daemons attendent des requêtes et fournissent des services (sshd, httpd, cron)."),
 QC("Pourquoi mettre à jour régulièrement un système ?", "Pour changer de couleur d'interface~Pour corriger les vulnérabilités connues~Pour augmenter la taille de l'écran~Pour réduire le nombre de processus", 1,
     "Les correctifs de sécurité ferment les failles exploitables par un attaquant."),
 QT("Expliquer la différence entre un processus et un thread, puis dire pourquoi la mémoire de deux processus est protégée.",
    "Un processus est une instance d'un programme avec son propre espace d'adressage et ses ressources. Un thread est un fil d'exécution à l'intérieur d'un processus : plusieurs threads partagent le même espace mémoire et les mêmes ressources, mais ont chacun une pile et un compteur. La mémoire de deux processus est protégée par la traduction d'adresses et les droits du noyau : un processus ne peut pas lire ou écrire l'espace d'un autre sans mécanisme explicite. Cela évite qu'un bug ou un logiciel malveillant corrompe un autre programme, et c'est la base de l'isolation des services.",
    "On oppose l'isolation du processus au partage du thread, puis on justifie la protection par le noyau et la pagination."),
 QT("Un serveur devient très lent et le disque travaille en permanence. Décrire le diagnostic à conduire.",
    "On observe d'abord les indicateurs : charge CPU, occupation mémoire, taux d'E/S disque et nombre de processus (top, perfmon). Si la mémoire est saturée et que le disque est très sollicité, on suspecte du swapping : on vérifie la quantité de mémoire libre et les pages échangées. On identifie ensuite le ou les processus consommateurs, on contrôle leurs journaux et leur historique de mise à jour, puis on compare avec une période normale. On peut alors réduire le nombre de services, ajouter de la mémoire, corriger une fuite mémoire ou limiter un processus, puis on remesure pour valider l'effet de l'action.",
    "La démarche attendue : mesurer, suspecter le swapping, identifier le processus, agir, puis remesurer.")],
C("Le système d'exploitation arbitre l'accès au processeur, à la mémoire et aux fichiers ; le noyau garantit l'isolation et applique les droits.",
  "Processus = programme en cours d'exécution (PID + état + espace mémoire)",
  "Noyau · ordonnanceur · pagination · DAC/MAC · journalisation",
  "Processus~Instance en cours~PID et état~Thread~Fil d'exécution~Mémoire partagée~Ordonnanceur~Priorités et files~Noyau~Appels système",
  "Observer la charge et la mémoire|Identifier les processus consommateurs|Vérifier les journaux et les mises à jour|Agir sur la cause|Remesurer les indicateurs",
  "Confondre processus et thread|Ignorer le swapping|Laisser des services inutiles actifs|Oublier les correctifs de sécurité",
  "PID~Identifiant unique du processus~Swapping~Pages déplacées sur disque~ext4~Système de fichiers journalisé~SELinux~Contrôle mandataire~syslog~Journaux système",
  "DAC~Propriétaire décide~Droits flexibles~MAC~Politique centrale~Sécurité renforcée",
  "Processus~Espace mémoire isolé~Thread~Mémoire partagée"))

# ============================================================ IN7
add("IN7", "Linux : système de fichiers, permissions et administration", "Informatique", ["BTS1"],
S("Linux est un système d'exploitation libre fondé sur le noyau Linux et une distribution qui regroupe noyau, bibliothèques, outils et gestionnaire de paquets."
  "|Les distributions courantes en entreprise sont Debian, Ubuntu, Red Hat Enterprise Linux et SUSE, avec des cycles de maintenance et de support différents."
  "|L'arborescence est unique et hiérarchique : la racine « / » contient /etc pour la configuration, /var pour les données variables, /home pour les utilisateurs et /proc pour l'état du noyau."
  "|Tout est fichier sous Unix, y compris les périphériques (/dev) et les informations sur les processus (/proc)."
  "|Chaque fichier appartient à un utilisateur et à un groupe ; trois catégories de droits (propriétaire, groupe, autres) et trois permissions (lecture r, écriture w, exécution x) s'appliquent."
  "|Les permissions se notent en octal : 755 donne rwx au propriétaire et r-x au groupe et aux autres ; chmod modifie les droits, chown change le propriétaire."
  "|Le compte root possède tous les privilèges : son utilisation doit être exceptionnelle et tracée via sudo, qui journalise les commandes exécutées."
  "|Les commandes essentielles sont ls, cd, cp, mv, rm, grep, find, ps, systemctl, journalctl et ip pour l'administration courante."
  "|Les services sont gérés par systemd : systemctl start, stop, enable et status contrôlent le démarrage et l'état des daemons."
  "|Le gestionnaire de paquets (apt, dnf, yum, pacman) installe et met à jour les logiciels depuis des dépôts signés, ce qui simplifie la remédiation."
  "|Le contrôle d'accès peut être renforcé avec SELinux ou AppArmor, qui appliquent des politiques mandataires au-delà des droits UNIX classiques."
  "|La syntaxe des commandes, la lecture des journaux (/var/log, journalctl) et la rigueur dans les droits sont des compétences pratiques attendues en option IR."),
[QC("Quelle commande affiche les droits d'un fichier sous Linux ?", "dir~ls -l~whoami~pwd", 1,
     "ls -l affiche le type, les permissions, le propriétaire, le groupe et la taille des fichiers."),
 QC("Que signifie le mode 755 ?", "Lecture seule pour tous~rwx propriétaire, r-x groupe et autres~Aucun droit~Exécution interdite", 1,
     "7 = rwx, 5 = r-x : le propriétaire peut tout faire, les autres lire et exécuter."),
 QC("Quelle commande change le propriétaire d'un fichier ?", "chmod~chown~chgrp~touch", 1,
     "chown modifie le propriétaire (et éventuellement le groupe) d'un fichier."),
 QC("Quel répertoire contient les fichiers de configuration système ?", "/home~/etc~/tmp~/dev", 1,
     "/etc regroupe les fichiers de configuration ; /var contient les données variables."),
 QC("Quel mécanisme journalise les commandes exécutées avec des privilèges élevés ?", "su~sudo~root~chmod", 1,
     "sudo trace les commandes dans les journaux, contrairement à une session root directe."),
 QC("Quelle commande consulte les journaux systemd ?", "journalctl~ifconfig~grep~mount", 0,
     "journalctl affiche les journaux collectés par journald."),
 QC("Comment redémarrer un service avec systemd ?", "service restart~systemctl restart~reboot~killall", 1,
     "systemctl restart nom_du_service redémarre le daemon concerné."),
 QC("Quel est l'intérêt d'un gestionnaire de paquets signés ?", "Changer le thème~Vérifier l'origine et l'intégrité des logiciels~Augmenter le débit~Supprimer les journaux", 1,
     "La signature des dépôts garantit que les paquets proviennent d'une source fiable et n'ont pas été modifiés."),
 QT("Un fichier de configuration doit être modifiable par le groupe admin uniquement, avec lecture pour les autres et aucun droit pour les utilisateurs non autorisés. Donner les droits octaux et la commande.",
    "Le propriétaire doit conserver la lecture et l'écriture (6), le groupe admin la lecture et l'écriture (6), et les autres aucun droit (0) : le mode est 660. La commande est chmod 660 nom_du_fichier, complétée si besoin par chown root:admin nom_du_fichier pour positionner le propriétaire et le groupe. On vérifie ensuite avec ls -l que la ligne affiche -rw-rw---- et on teste l'accès avec un compte du groupe puis un compte externe.",
    "On déduit 6/6/0 des besoins exprimés, on donne chmod 660 et on prévoit une vérification par ls -l."),
 QT("Expliquer pourquoi sudo est préférable à une connexion directe en root pour l'administration quotidienne.",
    "sudo exécute une commande précise avec des privilèges élevés, laisse une trace dans les journaux avec l'identité de l'utilisateur et limite les actions autorisées via le fichier sudoers. Une session root permanente expose le système à toutes les erreurs et à tous les programmes lancés pendant la session, sans distinction d'auteur. Avec sudo, on applique le moindre privilège, on peut exiger un mot de passe ou une authentification multifacteur, et on reconstitue a posteriori qui a fait quoi, ce qui est indispensable en cas d'incident de sécurité.",
    "On cite la traçabilité, la limitation des privilèges et la responsabilisation des actions.")],
C("Sous Linux, tout est fichier et chaque fichier porte des droits : la rigueur de l'administration tient à la maîtrise de l'arborescence, des permissions et des journaux.",
  "chmod 755 = rwx r-x r-x · chown = changement de propriétaire",
  "/etc : configuration · /var : données · /proc : état du noyau · sudo : traçabilité",
  "/etc~Configuration~Fichiers système~/var~Données variables~Journaux~/home~Répertoires utilisateurs~Données personnelles",
  "Se connecter avec un compte dédié|Vérifier les droits avec ls -l|Modifier avec chmod ou chown|Gérer le service avec systemctl|Consulter journalctl après l'action",
  "Travailler en root en permanence|Donner 777 « pour que ça marche »|Modifier /etc sans sauvegarde|Ignorer les messages des journaux",
  "chmod 755~Lecture et exécution pour tous~chown root:admin~Propriété et groupe~systemctl restart~Redémarrage de service~journalctl~Lecture des journaux~SELinux~Contrôle mandataire",
  "sudo~Commande ponctuelle tracée~Session root~Privilèges permanents et risqués",
  "chmod~Modifie les permissions~chown~Modifie le propriétaire"))

# ============================================================ IN8
add("IN8", "Virtualisation : hyperviseurs, machines virtuelles et ressources", "Informatique", ["BTS2"],
S("La virtualisation exécute plusieurs systèmes d'exploitation isolés sur une même machine physique grâce à un hyperviseur."
  "|L'hyperviseur de type 1 (bare metal) s'installe directement sur le matériel : VMware ESXi, Microsoft Hyper-V, Proxmox VE ou Xen."
  "|L'hyperviseur de type 2 fonctionne comme une application sur un hôte : VirtualBox, VMware Workstation, adaptés au poste de test et de formation."
  "|Une machine virtuelle (VM) est un ensemble de fichiers : configuration (VMX, XML), disque virtuel (VMDK, QCOW2, VHDX) et états mémoire éventuels."
  "|L'hyperviseur partitionne le processeur, la mémoire, le stockage et le réseau, et médiatise l'accès au matériel."
  "|Le surallocation (overcommitment) permet d'allouer plus de mémoire virtuelle qu'il n'en existe physiquement : utile mais risqué en cas de pointe simultanée."
  "|Le réseau virtuel utilise des commutateurs virtuels (vSwitch) et des VLAN pour connecter les VM entre elles et au réseau physique."
  "|Les instantanés (snapshots) capturent l'état d'une VM à un instant donné : ils facilitent les tests mais ne remplacent pas une sauvegarde."
  "|La migration à chaud (vMotion) déplace une VM entre hôtes sans interruption de service, à condition de partager le stockage et un réseau adapté."
  "|La haute disponibilité (HA) redémarre automatiquement les VM d'un hôte défaillant sur un autre membre du cluster."
  "|Les outils d'administration (vCenter, Proxmox web, PowerShell) centralisent la création, le dimensionnement et la supervision des VM."
  "|La security by design de la virtualisation impose le durcissement de l'hyperviseur, la limitation des privilèges et la séparation des réseaux de management."),
[QC("Quel est un hyperviseur de type 1 ?", "VirtualBox~VMware Workstation~VMware ESXi~Wine", 2,
     "ESXi s'installe directement sur le serveur, sans système hôte classique."),
 QC("Quelle différence entre type 1 et type 2 ?", "Type 1 s'installe sur le matériel, type 2 sur un OS hôte~Type 2 est plus rapide~Type 1 ne gère que le réseau~Il n'y a aucune différence", 0,
     "Le type 1 est « bare metal », le type 2 est une application exécutée sur un hôte."),
 QC("Que contient principalement une machine virtuelle ?", "Un fichier de configuration et un disque virtuel~Uniquement du code machine~Une partition physique~Un câble réseau", 0,
     "Une VM est un ensemble de fichiers : configuration, disque virtuel et éventuels états."),
 QC("Quel risque présente le surallocation de mémoire ?", "Une réduction du nombre de VM~Une saturation mémoire en cas de pointe simultanée~Une augmentation du disque~Une panne du vSwitch", 1,
     "Si toutes les VM utilisent leur mémoire en même temps, l'hôte manque de ressources."),
 QC("Quel rôle joue un vSwitch ?", "Chiffrer les disques~Connecter les VM au réseau virtuel et physique~Remplacer le processeur~Stocker les snapshots", 1,
     "Le commutateur virtuel achemine les trames entre VM et vers les cartes physiques."),
 QC("Un snapshot est-il une sauvegarde ?", "Oui, toujours~Non, il capture un état et dépend du disque de base~Oui, si la VM est éteinte~Oui, pour les seuls fichiers texte", 1,
     "Le snapshot n'est pas une copie indépendante : il doit être complété par une sauvegarde restaurée."),
 QC("Quelle fonction assure le redémarrage automatique des VM d'un hôte en panne ?", "La HA~Le snapshot~Le vMotion~Le NAT", 0,
     "La haute disponibilité relance les VM sur un hôte opérationnel du cluster."),
 QC("Quelle bonne pratique de sécurité concerne l'hyperviseur ?", "Le laisser sans mot de passe~Le durcir et limiter les accès à l'interface de management~Le connecter à Internet~Partager le compte admin", 1,
     "L'hyperviseur est un point de contrôle critique : accès restreint, durcissement et réseau de management isolé."),
 QT("Expliquer pourquoi la virtualisation facilite la mise à jour d'un parc de serveurs tout en exigeant une discipline de test.",
    "Les VM sont des fichiers : on peut les cloner, les instantaner et les restaurer rapidement, ce qui permet de tester une mise à jour sur une copie avant de l'appliquer en production. Le snapshot offre un retour arrière immédiat si l'application ne démarre plus. En revanche, un snapshot n'est pas une sauvegarde, les clones partagent parfois des disques parents et une mise à jour mal testée peut se propager à toutes les copies. Il faut donc documenter l'état de référence, tester sur une VM de recette, sauvegarder avant modification, appliquer, valider les services puis archiver le résultat.",
    "On valorise clonage et retour arrière, puis on rappelle les limites des snapshots et la nécessité d'une procédure de test."),
 QT("Un serveur physique supporte 10 VM et la mémoire est saturée à 95 %. Décrire l'analyse et les pistes d'action.",
    "On relève les indicateurs de l'hôte et de chaque VM : mémoire active, ballon, échange (swap), CPU et E/S. On identifie les VM les plus consommatrices et on vérifie si leur besoin est réel ou lié à une fuite applicative. On peut alors réduire l'allocation excessive, activer le ballonning, déplacer une VM vers un autre hôte avec vMotion, ajouter de la mémoire physique ou étaler les charges. On évite de simplement augmenter le surallocation, qui masquerait le problème. Après chaque action, on remesure sur une période représentative et on met à jour la documentation de dimensionnement.",
    "On attend une mesure par VM, une recherche de cause, des actions de rééquilibrage ou d'ajout de ressources, puis une remesure.")],
C("La virtualisation transforme un serveur en pool de ressources : l'hyperviseur isole les VM, mais sa configuration et ses sauvegardes restent critiques.",
  "VM = configuration + disque virtuel + états",
  "Type 1 sur matériel · type 2 sur OS hôte · HA et snapshots : usages distincts",
  "Hyperviseur~Couche de virtualisation~Type 1 sur matériel~VM~Système isolé~Fichiers de configuration~vSwitch~Réseau virtuel~HA~Redémarrage auto",
  "Dimensionner l'hôte|Créer les VM et les réseaux virtuels|Durcir l'hyperviseur|Configurer sauvegardes et HA|Tester et documenter",
  "Confondre snapshot et sauvegarde|Surallouer la mémoire sans mesure|Exposer l'interface de management|Oublier de tester la restauration",
  "ESXi~Hyperviseur type 1~VirtualBox~Hyperviseur type 2~QCOW2~Format de disque virtuel~vMotion~Migration à chaud~HA~Bascule automatique",
  "HA~Redémarre après panne~vMotion~Déplace sans arrêt~Snapshot~Capture un état",
  "Type 1~Direct sur le matériel~Type 2~Application sur hôte"))

# ============================================================ IN9
add("IN9", "Supervision et exploitation : métriques, alertes et journaux", "Informatique", ["BTS2"],
S("La supervision surveille en continu l'état des systèmes et des réseaux afin de détecter les dysfonctionnements avant qu'ils ne deviennent critiques."
  "|Elle s'appuie sur des indicateurs (métriques) : disponibilité, temps de réponse, charge CPU, mémoire, espace disque, trafic réseau et taux d'erreur."
  "|Les sondes actives testent un service (ping, HTTP, TCP) tandis que les sondes passives observent les flux ou les journaux."
  "|SNMP (Simple Network Management Protocol) interroge les équipements via des OID et reçoit des traps ; les versions 1 et 2c sont peu sûres, la v3 authentifie et chiffre."
  "|Les protocoles de collecte courants incluent SNMP, WMI, agent Zabbix, Prometheus exporter, syslog et IPFIX/NetFlow."
  "|Un seuil d'alerte définit la valeur à partir de laquelle une anomalie est signalée ; un bon seuil évite à la fois les fausses alertes et les alertes manquées."
  "|La corrélation d'événements regroupe les alertes liées pour réduire le bruit et identifier la cause racine plutôt que les symptômes."
  "|Le SIEM (Security Information and Event Management) centralise les journaux de sécurité, les corrèle et conserve les preuves pour l'analyse forensique."
  "|Les tableaux de bord (Grafana, Zabbix) présentent l'état du parc et les tendances ; ils doivent rester lisibles et actionnables."
  "|La disponibilité se mesure souvent en pourcentage mensuel : 99,9 % autorise environ 43 minutes d'interruption par mois."
  "|Un incident suit un processus : détection, qualification, diagnostic, correction, communication et retour d'expérience."
  "|L'exploitation quotidienne combine supervision, gestion des incidents, sauvegardes, mises à jour et documentation, au cœur de l'unité U5 du BTS CIEL."),
[QC("Qu'est-ce qu'une sonde active de supervision ?", "Un journal d'événements~Un test qui interroge directement un service~Un utilisateur~Un câble de mesure", 1,
     "Une sonde active envoie une requête (ping, HTTP, TCP) et mesure la réponse."),
 QC("Quelle version de SNMP authentifie et chiffre les échanges ?", "v1~v2c~v3~v4", 2,
     "SNMPv3 apporte authentification et confidentialité ; v1 et v2c utilisent des communautés en clair."),
 QC("Que désigne un OID en SNMP ?", "Un identifiant d'objet dans l'arbre MIB~Un type de câble~Un port réseau~Un utilisateur", 0,
     "Les OID identifient de manière hiérarchique les objets gérés dans la MIB."),
 QC("Quel outil centralise et corrèle les journaux de sécurité ?", "Grafana~SIEM~Wireshark~Putty", 1,
     "Le SIEM collecte, corrèle et conserve les événements de sécurité."),
 QC("Quel est l'objectif de la corrélation d'événements ?", "Augmenter le nombre d'alertes~Réduire le bruit et trouver la cause racine~Supprimer les journaux~Ralentir la collecte", 1,
     "Elle regroupe les symptômes liés à une même cause pour aider au diagnostic."),
 QC("Combien de minutes d'indisponibilité mensuelle pour 99,9 % ?", "4,3 minutes~43 minutes~7 heures~1 minute", 1,
     "0,1 % d'un mois d'environ 43 200 minutes représente environ 43 minutes."),
 QC("Quelle est la première étape du traitement d'un incident ?", "Redémarrer tous les serveurs~Détecter et qualifier l'incident~Fermer le ticket~Éteindre la supervision", 1,
     "On détecte puis on qualifie la gravité et le périmètre avant toute action."),
 QC("Quel indicateur mesure la qualité perçue d'un service web ?", "Le nombre de câbles~Le temps de réponse et le taux d'erreur~La couleur du logo~Le nombre de VM", 1,
     "Latence, taux d'erreur et disponibilité sont des indicateurs de qualité de service."),
 QT("Expliquer la différence entre supervision technique et supervision métier, et pourquoi les deux sont nécessaires.",
    "La supervision technique surveille l'infrastructure : disponibilité des hôtes, charge CPU, mémoire, liens réseau, services système. La supervision métier surveille les fonctionnalités attendues par les utilisateurs : temps de traitement d'une commande, taux de paiements réussis, nombre de réservations. Un serveur peut être « vert » techniquement alors que l'application métier est en panne fonctionnelle, et inversement une alerte technique peut n'avoir aucun impact utilisateur. Les deux niveaux permettent de prioriser les incidents selon leur impact réel et de communiquer avec les parties prenantes.",
    "On distingue l'infrastructure du service rendu, puis on justifie par la priorisation et la communication."),
 QT("Une alerte « espace disque faible » se répète chaque matin. Décrire la méthode de traitement durable.",
    "On vérifie d'abord la réalité de l'alerte et le seuil configuré, puis on identifie la partition et les répertoires qui croissent (du, outils de rapport). On recherche la cause : journaux non rotatés, fichiers temporaires, sauvegardes locales, pics de traitement. On applique une action immédiate (nettoyage contrôlé, archivage) puis une action durable : rotation des journaux, séparation des données, agrandissement de la capacité, ajustement du seuil et de la période de mesure. On documente l'incident, on met à jour la procédure d'exploitation et on suit l'indicateur pendant plusieurs jours pour confirmer la disparition de l'alerte.",
    "On attend vérification du seuil, recherche de cause, action immédiate et durable, documentation et suivi.")],
C("La supervision transforme des mesures en alertes actionnables : elle repose sur des sondes, des seuils pertinents et une corrélation des événements.",
  "Disponibilité = temps de fonctionnement / temps total",
  "SNMPv3 · SIEM · corrélation · 99,9 % ≈ 43 min/mois",
  "Métrique~Mesure chiffrée~CPU, mémoire~Sonde active~Teste un service~Ping, HTTP~SIEM~Centralise les journaux~Corrélation~Regroupe les alertes",
  "Choisir les indicateurs utiles|Déployer les sondes et fixer les seuils|Centraliser les journaux|Corréler et qualifier les alertes|Traiter et capitaliser",
  "Multiplier les seuils sans priorité|Ignorer les fausses alertes récurrentes|Laisser SNMP v2c en clair|Ne jamais faire de retour d'expérience",
  "99,9 %~Environ 43 min par mois~SNMPv3~Authentification et chiffrement~Syslog~Journaux centralisés~Grafana~Tableaux de bord~MTTR~Temps moyen de rétablissement",
  "Supervision technique~Infrastructure et services~Supervision métier~Fonctions utilisateurs et impact",
  "Sonde active~Envoie une requête~Sonde passive~Observe les flux"))

# ============================================================ IN10
add("IN10", "Cryptographie : chiffrement, hachage et signature", "Informatique", ["BTS2"],
S("La cryptographie protège la confidentialité, l'intégrité et l'authenticité des données à l'aide d'algorithmes et de clés."
  "|Le chiffrement symétrique utilise une même clé secrète pour chiffrer et déchiffrer : AES est le standard actuel, avec des clés de 128, 192 ou 256 bits."
  "|Les modes de chiffrement par blocs diffèrent : ECB est à proscrire car il révèle les répétitions ; CBC et GCM sont préférés, GCM apportant en plus l'authenticité."
  "|Le chiffrement asymétrique repose sur un couple clé publique / clé privée : RSA et ECC (courbes elliptiques) permettent l'échange de clés et la signature."
  "|Une fonction de hachage produit une empreinte de taille fixe ; SHA-256 et SHA-3 sont résistants aux collisions, contrairement à MD5 et SHA-1 désormais déconseillés."
  "|Le hachage avec sel (salt) et étirement (Argon2, bcrypt, PBKDF2) protège les mots de passe stockés contre les attaques par table rainbow et par force brute."
  "|La signature numérique chiffre l'empreinte d'un document avec la clé privée : elle garantit l'authenticité de l'émetteur et l'intégrité du message."
  "|Un certificat X.509 lie une identité à une clé publique ; il est signé par une autorité de certification et vérifiable via une chaîne de confiance."
  "|TLS combine asymétrique (échange de clé, authentification du serveur) et symétrique (chiffrement des données) dans une session négociée."
  "|Une clé secrète doit être générée par un générateur aléatoire cryptographique, stockée dans un coffre ou un HSM, et renouvelée selon une politique."
  "|La force d'un algorithme ne compense pas une mauvaise gestion des clés : la fuite d'une clé privée annule la protection offerte."
  "|La cryptographie post-quantique prépare le remplacement des algorithmes vulnérables à un ordinateur quantique ; la migration doit être anticipée."),
[QC("Quel algorithme symétrique est le standard actuel ?", "MD5~AES~RSA~SHA-1", 1,
     "AES (Advanced Encryption Standard) est le standard de chiffrement symétrique."),
 QC("Pourquoi le mode ECB est-il déconseillé ?", "Il est trop lent~Il révèle les répétitions de blocs~Il ne chiffre que 8 bits~Il exige deux clés", 1,
     "En ECB, un même bloc clair donne toujours le même bloc chiffré, ce qui fuite la structure des données."),
 QC("Combien de clés utilise le chiffrement asymétrique ?", "Une seule~Deux : publique et privée~Trois~Quatre", 1,
     "La clé publique se diffuse, la clé privée reste secrète."),
 QC("Quelle fonction de hachage est aujourd'hui déconseillée ?", "SHA-256~SHA-3~MD5~Argon2", 2,
     "MD5 et SHA-1 sont vulnérables aux collisions et ne doivent plus être utilisés pour la sécurité."),
 QC("À quoi sert le sel dans le stockage des mots de passe ?", "À accélérer le hachage~À rendre les empreintes uniques et contrer les tables rainbow~À chiffrer la base~À remplacer le mot de passe", 1,
     "Le sel aléatoire empêche deux mots de passe identiques de produire la même empreinte."),
 QC("Que garantit une signature numérique ?", "La seule confidentialité~L'authenticité de l'émetteur et l'intégrité du document~La compression du fichier~La vitesse de transmission", 1,
     "La signature chiffrée avec la clé privée prouve l'origine et détecte toute modification."),
 QC("Qui signe un certificat X.509 ?", "Le client~Une autorité de certification~Le routeur~Le DNS", 1,
     "L'autorité de certification signe le certificat et permet de vérifier la chaîne de confiance."),
 QC("Quel mécanisme TLS utilise pour le chiffrement massif des données ?", "Le chiffrement asymétrique sur tous les paquets~Le chiffrement symétrique avec une clé de session~MD5~Le hachage seul", 1,
     "L'asymétrique négocie la clé de session, puis le symétrique chiffre les échanges pour la performance."),
 QT("Expliquer pourquoi il ne faut pas utiliser MD5 pour vérifier l'intégrité d'un logiciel téléchargé.",
    "MD5 produit une empreinte de 128 bits pour laquelle des collisions ont été démontrées : deux contenus différents peuvent partager la même empreinte. Un attaquant peut donc modifier un logiciel malveillant pour qu'il conserve l'empreinte annoncée et tromper la vérification. Pour un contrôle d'intégrité fiable, on utilise SHA-256 ou SHA-3, idéalement accompagnés d'une signature numérique vérifiée via une chaîne de certificats, ce qui apporte aussi l'authenticité de l'éditeur.",
    "On cite la faiblesse des collisions MD5 et on propose SHA-256 avec signature comme remédiation."),
 QT("Une entreprise stocke les mots de passe de ses utilisateurs. Décrire une bonne pratique de stockage et la justifier.",
    "On ne stocke jamais le mot de passe en clair ni un simple SHA-256 rapide. Pour chaque utilisateur, on génère un sel aléatoire unique, on dérive une empreinte avec une fonction lente et paramétrable comme Argon2id, bcrypt ou PBKDF2, puis on enregistre le sel, les paramètres et l'empreinte. Lors de la connexion, on recalcule l'empreinte avec le sel enregistré et on compare en temps constant. Le sel rend les attaques par tables rainbow inutiles et la lenteur ralentit la force brute, tandis que des paramètres ajustables permettent de suivre l'augmentation de la puissance des attaquants.",
    "On attend : sel unique, fonction de dérivation lente, comparaison sûre et justification contre rainbow et force brute.")],
C("La cryptographie combine chiffrement pour la confidentialité, hachage pour l'intégrité et signature pour l'authenticité ; la gestion des clés reste le point faible.",
  "Signature = chiffrement de l'empreinte avec la clé privée",
  "Symétrique : AES · Asymétrique : RSA/ECC · Hachage : SHA-256 · Mots de passe : Argon2",
  "AES~Symétrique rapide~Clé secrète partagée~RSA~Asymétrique~Clé publique et privée~SHA-256~Empreinte 256 bits~HMAC~Authenticité d'un message",
  "Choisir l'algorithme adapté au besoin|Générer des clés aléatoires fortes|Stocker les clés dans un coffre|Signer et vérifier les échanges|Renouveler et révoquer les clés",
  "Utiliser MD5 ou SHA-1|Réutiliser la même clé partout|Stocker une clé privée en clair|Confondre hachage et chiffrement",
  "SHA-256~Empreinte fiable~MD5~Collisions connues~Argon2~Dérivation lente~X.509~Certificat signé~TLS~Session chiffrée",
  "Symétrique~Une clé~Rapide pour les données~Asymétrique~Deux clés~Échange et signature",
  "Hachage~Empreinte irréversible~Chiffrement~Réversible avec la clé"))

# ============================================================ IN11
add("IN11", "Gestion des identités et des accès : IAM, MFA et annuaires", "Informatique", ["BTS2"],
S("La gestion des identités et des accès (IAM) encadre le cycle de vie des comptes : création, attribution des droits, utilisation, modification et suppression."
  "|Une identité désigne un utilisateur, un service ou un équipement ; l'authentification vérifie son identité, l'autorisation détermine ses droits."
  "|Le modèle RBAC (Role Based Access Control) attribue les permissions à un rôle, puis le rôle à l'utilisateur : il simplifie l'administration et les revues."
  "|Le principe du moindre privilège et la séparation des tâches limitent l'impact d'un compte compromis et évitent la concentration des pouvoirs."
  "|L'authentification multifacteur (MFA) combine au moins deux facteurs : quelque chose que l'on sait (mot de passe), que l'on possède (jeton, téléphone) ou que l'on est (biométrie)."
  "|Le SSO (Single Sign-On) authentifie une fois l'utilisateur puis transmet l'identité aux applications via des protocoles comme SAML, OAuth 2.0 ou OpenID Connect."
  "|Un annuaire LDAP ou Active Directory centralise les comptes et les groupes ; il sert de source de vérité pour les applications et les équipements."
  "|Le provisionning automatique crée et révoque les comptes à partir des événements RH (arrivée, mutation, départ) ; c'est un levier majeur contre les comptes orphelins."
  "|Les comptes de service et les clés API doivent être inventoriés, rotatés et limités à leur usage : ce sont des identités non humaines souvent négligées."
  "|Les privilèges temporaires (just-in-time) et les validations réduisent la fenêtre d'exposition d'un compte administrateur."
  "|Les journaux d'authentification et les revues périodiques des droits permettent de détecter les abus et de prouver la conformité lors d'un audit."
  "|En option IR, ces notions sont mobilisées dans le bloc « Valorisation de la donnée et cybersécurité » et dans la gestion sécurisée du système d'information."),
[QC("Quelle est la différence entre authentification et autorisation ?", "L'authentification donne les droits, l'autorisation vérifie l'identité~L'authentification vérifie l'identité, l'autorisation accorde les droits~Ce sont deux mots synonymes~L'autorisation concerne seulement le réseau", 1,
     "On s'identifie d'abord (authentification), puis on détermine ce que l'on peut faire (autorisation)."),
 QC("Quel est l'avantage principal du modèle RBAC ?", "Chaque utilisateur a un mot de passe unique~Les droits sont liés à des rôles, donc plus faciles à administrer~Il supprime les mots de passe~Il chiffre les données", 1,
     "RBAC réduit le nombre d'attributions individuelles et facilite les revues d'accès."),
 QC("Quel est un exemple de facteur « quelque chose que l'on possède » ?", "Un mot de passe~Un jeton matériel ou un téléphone~Une empreinte digitale~Une adresse e-mail", 1,
     "Le jeton ou le téléphone est un facteur de possession ; l'empreinte est un facteur biométrique."),
 QC("Quel protocole est couramment utilisé pour le SSO ?", "FTP~SAML ou OpenID Connect~ARP~SNMP", 1,
     "SAML 2.0, OAuth 2.0 et OpenID Connect transportent l'identité entre le fournisseur d'identité et les applications."),
 QC("Quel rôle joue un annuaire Active Directory ?", "Il chiffre les disques~Il centralise comptes, groupes et stratégies~Il remplace le firewall~Il héberge les sites web", 1,
     "L'annuaire est la source de vérité des identités et des appartenances aux groupes."),
 QC("Qu'est-ce qu'un compte orphelin ?", "Un compte sans mot de passe~Un compte d'un ancien employé resté actif~Un compte administrateur~Un compte de sauvegarde", 1,
     "Un compte non révoqué après un départ reste une porte d'entrée exploitables."),
 QC("Que désigne l'accès just-in-time ?", "Un accès permanent~Un privilège temporaire accordé pour une tâche~Un accès sans authentification~Un accès au seul réseau local", 1,
     "JIT limite la durée d'élévation des privilèges et réduit la fenêtre d'exposition."),
 QC("Pourquoi revvoir périodiquement les droits ?", "Pour augmenter le nombre de comptes~Pour détecter les accès excessifs et répondre aux audits~Pour changer de navigateur~Pour réduire le nombre de mots de passe", 1,
     "La revue d'accès vérifie que chaque droit reste justifié et documente la conformité."),
 QT("Expliquer pourquoi une authentification multifacteur est plus robuste qu'un mot de passe long, et donner ses limites.",
    "Un mot de passe, même long, reste un secret unique : s'il est volé par hameçonnage, par keylogger ou par fuite de base, l'attaquant l'utilise immédiatement. La MFA exige un second facteur distinct, par exemple un jeton ou une validation biométrique, que l'attaquant ne possède pas nécessairement ; elle bloque donc la majorité des accès frauduleux. Ses limites sont le coût et la complexité pour les utilisateurs, la dépendance au téléphone (SIM swapping, fatigue de validation) et le fait qu'elle ne protège pas contre une session déjà volée ou un lien OAuth malveillant. Elle doit s'accompagner de détection et de revue des droits.",
    "On explique la complémentarité des facteurs, puis on mentionne SIM swapping, fatigue MFA et sessions volées."),
 QT("Un employé quitte l'entreprise. Décrire la procédure de révocation d'accès et les points de contrôle.",
    "On déclenche la révocation dès la notification RH : désactivation du compte dans l'annuaire, révocation des certificats et jetons d'accès, fermeture des sessions actives, suppression des clés API et des accès aux coffres de secrets, retrait des abonnements et des appareils mobiles management. On vérifie ensuite les comptes de service partagés auxquels il avait accès et on rotate les secrets concernés. On conserve une trace datée de la procédure, on confirme avec le manager qu'aucun accès métier n'est oublié, et on intégrera un contrôle automatique dans le processus de offboarding pour éviter les comptes orphelins.",
    "On attend : annuaire, certificats, sessions, secrets, comptes partagés, traçabilité et automatisation.")],
C("L'IAM pilote le cycle de vie des identités : authentifier, autoriser, révoquer et tracer sont quatre gestes indissociables.",
  "MFA = savoir + posséder + être (au moins deux facteurs)",
  "RBAC · annuaire LDAP/AD · SSO SAML/OIDC · moindre privilège · revue des droits",
  "Identité~Utilisateur ou service~Compte et annuaire~Authentification~Vérifie l'identité~MFA~Autorisation~Accorde les droits~RBAC et rôles~Révocation~Supprime l'accès~Offboarding",
  "Créer le compte à partir du processus RH|Attribuer les rôles selon le moindre privilège|Activer MFA et SSO|Surveiller les connexions|Révoquer et tracer à la sortie",
  "Laisser des comptes de service sans propriétaire|Partager un compte administrateur|Ignorer les jetons OAuth|Oublier de révoquer les sessions ouvertes",
  "MFA~Deux facteurs minimum~Résiste au vol de mot de passe~SSO~Authentification unique~SAML ou OIDC~RBAC~Droits par rôle~JIT~Privilège temporaire",
  "Authentification~Qui êtes-vous~Mot de passe et MFA~Autorisation~Que pouvez-vous faire~Rôles et droits",
  "Compte orphelin~Ancien employé actif~Compte de service~Identité non humaine"))

# ============================================================ IN12
add("IN12", "Cyberdéfense : détection, réponse à incident et retour d'expérience", "Informatique", ["BTS2"],
S("La cyberdéfense regroupe les mesures de détection, d'analyse et de réponse mises en œuvre face aux attaques informatiques."
  "|Elle complète la prévention : aucune barrière n'étant parfaite, l'organisation doit être capable de détecter rapidement et de limiter l'impact."
  "|Un SOC (Security Operations Center) centralise la collecte, l'analyse et le traitement des alertes de sécurité, avec des analystes et des processus formalisés."
  "|Les sources de détection sont les journaux système et applicatifs, les flux réseau (IDS/NDR), les endpoints (EDR/XDR), les outils d'authentification et la veille sur les menaces."
  "|Un IDS détecte et alerte, un IPS bloque automatiquement l'activité suspecte ; l'EDR instrumente les postes et peut isoler une machine compromise."
  "|Le threat hunting consiste à rechercher activement des indicateurs de compromission (IoC) sans attendre une alerte, à partir d'hypothèses sur les tactiques adverses."
  "|Le cadre MITRE ATT&CK cartographie les tactiques et techniques des attaquants et sert de langage commun pour documenter la détection."
  "|La réponse à incident suit six phases : préparation, identification, confinement, éradication, récupération et retour d'expérience."
  "|Le confinement peut être court-circuiter un compte, isoler un poste du réseau ou bloquer une adresse IP ; il précède l'éradication du logiciel malveillant."
  "|La traçabilité des preuves (horodatage, hashes, chaîne de custody) est indispensable si l'incident peut donner lieu à une plainte ou à une notification réglementaire."
  "|En cas de violation de données personnelles, le RGPD impose une notification à la CNIL dans les 72 heures et l'information des personnes concernées si le risque est élevé."
  "|Le retour d'expérience produit un plan d'action correctif, met à jour les règles de détection et alimente la formation des équipes : c'est l'amélioration continue."),
[QC("Quel est le rôle principal d'un SOC ?", "Développer les applications~Centraliser détection, analyse et traitement des alertes~Administrer les bases de données~Gérer les sauvegardes seules", 1,
     "Le SOC est le centre opérationnel de sécurité qui traite les alertes 24/7 ou selon une plage définie."),
 QC("Quelle différence entre IDS et IPS ?", "IDS bloque, IPS alerte~IDS alerte, IPS bloque~IDS analyze les mots de passe, IPS les chiffre~Il n'y a aucune différence", 1,
     "L'IDS est détectif, l'IPS est également préventif et peut rejeter le trafic suspect."),
 QC("Que désigne un indicateur de compromission (IoC) ?", "Un mot de passe fort~Une trace d'activité malveillante comme une adresse IP ou un hash~Un type de câble~Un utilisateur administrateur", 1,
     "Les IoC sont des artefacts observés (IP, domaine, hash, clé de registre) révélant une intrusion."),
 QC("À quoi sert le cadre MITRE ATT&CK ?", "À chiffrer les disques~À cartographier les tactiques et techniques des attaquants~À gérer les tickets~À rédiger les contrats", 1,
     "MITRE ATT&CK fournit une matrice de référence des comportements adverses."),
 QC("Quelle est la première phase de la réponse à incident ?", "Éradication~Préparation~Récupération~Notification", 1,
     "La préparation (procédures, outils, compétences) précède l'identification et le traitement."),
 QC("Quelle action relève du confinement ?", "Réinstaller le poste~Isoler la machine compromise du réseau~Rédiger le rapport final~Former les utilisateurs", 1,
     "Le confinement stoppe la propagation avant l'éradication et la récupération."),
 QC("Quel délai de notification à la CNIL impose le RGPD en cas de violation de données ?", "24 heures~72 heures~7 jours~30 jours", 1,
     "L'article 33 du RGPD prévoit une notification à l'autorité de contrôle dans les 72 heures suivant la prise de connaissance."),
 QC("Quel est l'objectif du retour d'expérience ?", "Clore le ticket sans action~Tirer des enseignements et nourrir l'amélioration continue~Supprimer les journaux~Changer d'antivirus", 1,
     "Le REX produit des actions correctives, met à jour la détection et améliore la préparation."),
 QT("Décrire la chaîne de traitement d'une alerte de sécurité depuis sa réception jusqu'à sa clôture.",
    "L'alerte est d'abord normalisée et enrichie dans le SIEM ou la plateforme SOC. L'analyste la qualifie : est-ce un vrai positif, un faux positif ou une information complémentaire ? Il évalue la criticité à partir de l'actif touché, de la portée et de la crédibilité de l'indicateur. Si l'incident est confirmé, il ouvre un ticket, applique le confinement (isolement du poste, révocation du compte), documente les preuves avec horodatage et hashes, puis passe à l'éradication et à la restauration. Il vérifie le retour à la normale, notifie les parties prenantes si nécessaire, puis clôt le ticket avec le compte rendu et les actions correctrices issues du retour d'expérience.",
    "On attend : qualification, criticité, confinement, preuves, éradication, récupération, notification et REX."),
 QT("Un poste utilisateur présente un comportement suspect : expliquer comment organiser la collecte de preuves et la réponse.",
    "On isole d'abord le poste du réseau pour stopper les communications avec l'attaquant, sans l'éteindre afin de préserver la mémoire volatile. On collecte ensuite les éléments dans un ordre et avec des outils fiables : liste des processus et connexions, journaux système et de sécurité, capture mémoire si possible, artefacts sur le disque, hashes SHA-256 des fichiers suspects, horodatage et identité de l'opérateur. Chaque élément est consigné dans une chaîne de conservation (qui, quand, quoi, hash) pour garantir son intégrité. On identifie le vecteur d'entrée, on éradique le logiciel malveillant, on réinstalle si nécessaire, puis on remet le poste en service après validation et on alimente le retour d'expérience.",
    "On valorise l'isolement sans extinction, l'ordre de collecte, les hashes et la chaîne de conservation.")],
C("La cyberdéfense part du principe qu'une attaque peut réussir : détecter vite, contenir, éradiquer, récupérer et apprendre.",
  "Réponse à incident : préparation, identification, confinement, éradication, récupération, REX",
  "SOC · EDR/NDR · MITRE ATT&CK · IoC · notification RGPD 72 h",
  "SOC~Centre opérationnel~Collecte et analyse~IDS~Détecte et alerte~IPS~Bloque le trafic~EDR~Instrumente les postes~IoC~Traces d'intrusion",
  "Détecter et qualifier l'alerte|Évaluer la criticité|Confiner sans détruire les preuves|Éradiquer et restaurer|Capitaliser en retour d'expérience",
  "Éteindre immédiatement le poste compromis|Clore une alerte sans qualification|Modifier les fichiers suspects avant hashage|Oublier la notification RGPD",
  "72 h~Notification CNIL~MITRE ATT&CK~Matrice des tactiques~IoC~Adresse IP ou hash~REX~Plan d'action correctif~EDR~Isolation du poste",
  "IDS~Alerte sans blocage~IPS~Blocage automatique~EDR~Réponse sur poste",
  "Faux positif~Alerte sans incident~Vrai positif~Incident confirmé"))

# ============================================================ MS1
add("MS1", "Calcul littéral et algèbre : identités et factorisation", "Maths / stats", ["BTS1"],
S("Le calcul littéral manipule des expressions contenant des variables : on développe, on réduit et on factorise selon des règles exactes."
  "|Le développement distribue un facteur sur une somme : a(b + c) = ab + ac ; la réduction regroupe les termes de même nature."
  "|Les trois identités remarquables sont (a + b)² = a² + 2ab + b², (a − b)² = a² − 2ab + b² et (a + b)(a − b) = a² − b²."
  "|La factorisation transforme une somme en produit : elle sert à résoudre les équations par la règle « un produit de facteurs est nul si et seulement si l'un des facteurs est nul »."
  "|Les méthodes de factorisation sont le facteur commun, les identités remarquables et, pour un trinôme, la recherche de deux nombres dont la somme et le produit sont connus."
  "|Une équation du second degré a(x − x1)(x − x2) = 0 admet pour solutions x1 et x2 ; le discriminant Δ = b² − 4ac donne le nombre de racines de ax² + bx + c = 0."
  "|Si Δ > 0, deux solutions réelles ; si Δ = 0, une solution double ; si Δ < 0, aucune solution réelle."
  "|Les fractions algébriques imposent de vérifier les conditions d'existence : le dénominateur ne doit jamais être nul."
  "|Les puissances suivent des règles : a^m × a^n = a^(m+n), (a^m)^n = a^(mn), a^m / a^n = a^(m−n) avec a non nul."
  "|Les radicaux se simplifient en facteurisant sous la racine : √(a²b) = abs(a) multiplié par √b lorsque b est positif."
  "|Dans un contexte technique, ces outils servent par exemple à exprimer une puissance dissipée P = RI² ou à isoler une variable dans une formule d'électronique."
  "|La maîtrise de l'algèbre est prérequise aux fonctions, aux statistiques et aux calculs de budget de l'unité U3 du BTS CIEL."),
[QC("Que vaut (a + b)² ?", "a² + b²~a² + 2ab + b²~a² − 2ab + b²~a² + ab + b²", 1,
     "Le carré d'une somme comporte le terme croisé 2ab."),
 QC("Combien de solutions réelles pour une équation du second degré si Δ < 0 ?", "0~1~2~Une infinité", 0,
     "Un discriminant négatif signifie qu'il n'existe aucune solution réelle."),
 QC("Quelle est la formule du discriminant ?", "b² + 4ac~b² − 4ac~2ab − c²~a² − 4b", 1,
     "Δ = b² − 4ac pour ax² + bx + c = 0."),
 QC("Comment factorise-t-on a² − b² ?", "(a − b)(a − b)~(a + b)(a − b)~(a + b)²~a(a − b)", 1,
     "C'est la différence de deux carrés."),
 QC("Quelle est la condition d'existence de 1/(x − 2) ?", "x = 2~x ≠ 2~x > 2~Aucune condition", 1,
     "Le dénominateur x − 2 ne doit pas être nul, donc x ≠ 2."),
 QC("Que vaut a^m × a^n ?", "a^(m+n)~a^(mn)~a^(m−n)~a^(m/n)", 0,
     "La multiplication de puissances de même base additionne les exposants."),
 QC("Quelle méthode factorise 3x + 3y ?", "Identité remarquable~Facteur commun 3~Discriminant~Réduction", 1,
     "On met 3 en facteur : 3(x + y)."),
 QC("Pourquoi factoriser avant de résoudre une équation ?", "Pour obtenir une somme~Parce qu'un produit nul implique qu'un facteur est nul~Pour supprimer les variables~Pour arrondir les résultats", 1,
     "La propriété du produit nul donne directement les solutions."),
 QT("Résoudre x² − 5x + 6 = 0 en détaillant la méthode, puis donner les solutions.",
    "On identifie a = 1, b = −5, c = 6. Le discriminant vaut Δ = b² − 4ac = 25 − 24 = 1 > 0. Les solutions sont x = (−b ± √Δ)/(2a) = (5 ± 1)/2, soit x1 = 3 et x2 = 2. On retrouve le même résultat par factorisation : x² − 5x + 6 = (x − 2)(x − 3), et un produit est nul si l'un des facteurs est nul. On vérifie : 9 − 15 + 6 = 0 et 4 − 10 + 6 = 0.",
    "On attend le calcul du discriminant, la formule des racines et une vérification."),
 QT("Développer et réduire A = (2x − 1)² − (x + 3)(x − 3), puis factoriser le résultat.",
    "(2x − 1)² = 4x² − 4x + 1. (x + 3)(x − 3) = x² − 9. Donc A = 4x² − 4x + 1 − x² + 9 = 3x² − 4x + 10. Le discriminant de ce trinôme vaut Δ = (−4)² − 4×3×10 = 16 − 120 = −104 < 0 : il n'est pas factorisable sur ℝ en produit de facteurs du premier degré. L'expression réduite est donc 3x² − 4x + 10, qui reste toujours strictement positive.",
    "On développe avec les identités, on réduit, puis on justifie l'absence de factorisation réelle par le discriminant.")],
C("Le calcul littéral repose sur trois identités remarquables et sur la factorisation, outil central pour résoudre les équations du second degré.",
  "Δ = b² − 4ac · racines = (−b ± √Δ)/(2a)",
  "(a+b)² = a²+2ab+b² · (a−b)² = a²−2ab+b² · (a+b)(a−b) = a²−b²",
  "Développement~a(b+c)=ab+ac~Distribution~Factorisation~Somme transformée en produit~Identités remarquables~Équation~Δ et racines~Deux solutions si Δ>0",
  "Repérer la structure de l'expression|Choisir développement ou factorisation|Appliquer l'identité adaptée|Réduire les termes semblables|Vérifier la solution",
  "Oublier le terme 2ab|Écrire (a+b)² = a²+b²|Négliger les conditions d'existence|Perdre un signe lors de la réduction",
  "(x+2)²~x²+4x+4~x²−9~(x+3)(x−3)~Δ=1~Deux racines~3x+3y~3(x+y)~1/(x−2)~x≠2",
  "Développer~Du produit vers la somme~Règle de distribution~Factoriser~De la somme vers le produit~Règle du produit nul",
  "Δ>0~Deux racines~Δ=0~Racine double"))

# ============================================================ MS2
add("MS2", "Fonctions et représentations graphiques", "Maths / stats", ["BTS1"],
S("Une fonction associe à chaque élément d'un ensemble de définition un unique élément de l'ensemble d'arrivée."
  "|Une fonction affine est de la forme f(x) = ax + b : sa représentation graphique est une droite de pente a passant par (0 ; b)."
  "|Une fonction linéaire est le cas particulier b = 0 : la droite passe par l'origine et traduit une situation de proportionnalité."
  "|Une fonction carrée f(x) = x² a pour courbe une parabole symétrique par rapport à l'axe des ordonnées, de sommet (0 ; 0)."
  "|Une fonction exponentielle f(x) = a^x est croissante si a > 1 et décroissante si 0 < a < 1 ; elle passe toujours par (0 ; 1)."
  "|La fonction logarithme népérien ln est la réciproque de l'exponentielle : ln(e^x) = x et e^(ln x) = x pour x > 0."
  "|Les variations d'une fonction se lisent sur son graphique ou se déduisent du signe de sa fonction dérivée."
  "|Résoudre f(x) = k revient à chercher les abscisses des intersections de la courbe avec la droite horizontale y = k."
  "|Résoudre f(x) ≥ k revient à garder les abscisses pour lesquelles la courbe est au-dessus de la droite y = k."
  "|La composition de fonctions vérifie (g ∘ f)(x) = g(f(x)) ; l'ordre des opérations est déterminant."
  "|Dans un contexte technique, une fonction peut modéliser la tension en fonction du temps, la charge d'une batterie ou le coût en fonction du nombre d'unités."
  "|Savoir lire un graphique, identifier un modèle et interpréter une pente sont des compétences de l'unité U3 du BTS CIEL."),
[QC("Quelle est la représentation graphique d'une fonction affine ?", "Une parabole~Une droite~Une hyperbole~Un cercle", 1,
     "Toute fonction f(x) = ax + b se représente par une droite."),
 QC("Quel est le coefficient directeur de la droite y = −2x + 5 ?", "5~2~−2~−5", 2,
     "Le coefficient de x est la pente, ici −2 ; la droite est décroissante."),
 QC("Par quel point passe toujours la courbe y = e^x ?", "(0 ; 0)~ (1 ; 0)~ (0 ; 1)~ (1 ; 1)", 2,
     "e^0 = 1, donc la courbe passe par (0 ; 1)."),
 QC("Quelle est la réciproque de la fonction exponentielle ?", "La fonction carrée~La fonction logarithme~La fonction affine~La fonction valeur absolue", 1,
     "ln est la réciproque de l'exponentielle de base e."),
 QC("Comment résoudre graphiquement f(x) = 3 ?", "Lire l'ordonnée en x = 3~Chercher les abscisses des points d'intersection avec y = 3~Tracer une droite verticale en y = 3~Additionner les coefficients", 1,
     "On projette les points d'intersection avec la droite horizontale y = 3 sur l'axe des abscisses."),
 QC("Une fonction est croissante si sa dérivée est…", "Négative~Positive~Nulle~Indéfinie", 1,
     "Une dérivée positive sur un intervalle caractérise une fonction strictement croissante."),
 QC("Que vaut (g ∘ f)(x) ?", "g(x) × f(x)~g(f(x))~f(g(x))~f(x) + g(x)", 1,
     "La composition applique d'abord f, puis g au résultat."),
 QC("Quel modèle traduit une situation de proportionnalité ?", "f(x) = ax + b avec b non nul~f(x) = ax~f(x) = x²~f(x) = ln x", 1,
     "La proportionnalité correspond à une fonction linéaire passant par l'origine."),
 QT("Une fonction affine passe par A(1 ; 5) et B(3 ; 11). Déterminer son équation et calculer f(10).",
    "Le coefficient directeur vaut a = (11 − 5)/(3 − 1) = 6/2 = 3. En utilisant A(1 ; 5) : 5 = 3 × 1 + b, donc b = 2. L'équation est f(x) = 3x + 2. On vérifie avec B : 3 × 3 + 2 = 11. Alors f(10) = 3 × 10 + 2 = 32. Graphiquement, la droite coupe l'axe des ordonnées en (0 ; 2) et monte de 3 unités quand x augmente de 1.",
    "On calcule la pente avec les deux points, on isole b, puis on remplace x par 10 et on vérifie."),
 QT("Expliquer comment lire graphiquement l'ensemble des solutions de f(x) > 2 et donner un exemple avec f(x) = x².",
    "On trace la courbe y = f(x) et la droite horizontale y = 2. On repère les abscisses des points d'intersection, puis on garde les portions de courbe situées au-dessus de la droite. Pour f(x) = x², les intersections avec y = 2 ont pour abscisses −√2 et √2. La parabole est au-dessus de la droite en dehors de cet intervalle, donc l'ensemble des solutions est ]−∞ ; −√2[ ∪ ]√2 ; +∞[. On vérifie avec un point de chaque zone, par exemple x = 0 donne 0 < 2 et x = 2 donne 4 > 2.",
    "On décrit la méthode graphique, puis on résout l'exemple de la parabole et on vérifie par un test.")],
C("Une fonction associe une image à chaque antécédent : sa courbe permet de lire variations, solutions et modèle sous-jacent.",
  "f(x) = ax + b · pente a = Δy/Δx",
  "Droite si affine · parabole si carrée · exponentielle croissante si a > 1",
  "Fonction~Antécédent et image~Ensemble de définition~Affine~Droite de pente a~f(x)=ax+b~Carrée~Parabole symétrique~Sommet en 0",
  "Identifier le type de fonction|Repérer le domaine de définition|Tracer quelques points caractéristiques|Lire les intersections avec y=k|Interpréter le résultat dans le contexte",
  "Confondre pente et ordonnée à l'origine|Oublier le domaine de définition|Lire l'abscisse au lieu de l'ordonnée|Croire que x² est croissante sur tout ℝ",
  "A(1;5), B(3;11)~a=3 et b=2~f(x)=3x+2~f(10)=32~x²>2~Solutions hors de l'intervalle~e^0~Vaut 1",
  "Fonction affine~Droite~Pente constante~Fonction carrée~Parabole~Pente variable",
  "Proportionnalité~Droite passant par l'origine~Affine générale~Droite décalée de b"))

# ============================================================ MS3
add("MS3", "Statistiques descriptives : résumer et interpréter un jeu de données", "Maths / stats", ["BTS1"],
S("La statistique descriptive résume un ensemble de données pour en dégager les caractéristiques essentielles sans perdre l'information utile."
  "|Une population est l'ensemble complet des individus étudiés ; un échantillon en est une partie, prélevée pour être représentative."
  "|Les caractères quantitatifs continus ou discrets se traitent par des moyennes et des dispersion ; les caractères qualitatifs par des effectifs et des pourcentages."
  "|Un effectif est le nombre d'individus dans une classe ; l'effectif cumulé additionne les effectifs jusqu'à cette classe."
  "|La fréquence est l'effectif divisé par l'effectif total : elle s'exprime en pourcentage lorsque l'on multiplie par 100."
  "|La moyenne est la somme des valeurs divisée par l'effectif ; elle est sensible aux valeurs extrêmes, contrairement à la médiane."
  "|La médiane est la valeur qui partage la série ordonnée en deux moitiés ; le premier et le troisième quartiles délimitent l'intervalle interquartile."
  "|Le mode est la valeur la plus fréquente : c'est le seul indicateur de position pertinent pour un caractère qualitatif."
  "|L'étendue est la différence entre la valeur maximale et la minimale ; la variance et l'écart-type mesurent la dispersion autour de la moyenne."
  "|L'écart-type est la racine carrée de la variance : il s'exprime dans la même unité que la donnée, ce qui facilite son interprétation."
  "|Les graphiques adaptés sont l'histogramme pour une variable continue, le diagramme en bâtons pour une variable discrète et le camembert pour une répartition."
  "|Une bonne présentation indique la source, la taille de l'échantillon, les unités et le mode de calcul : c'est une exigence de l'unité U3."),
[QC("Quelle mesure de position résiste aux valeurs extrêmes ?", "La moyenne~La médiane~L'écart-type~L'étendue", 1,
     "La médiane dépend du rang des valeurs, pas de leur amplitude."),
 QC("Comment calcule-t-on une fréquence ?", "Effectif multiplié par le total~Effectif divisé par l'effectif total~Total divisé par l'effectif~Valeur maximale moins minimale", 1,
     "La fréquence relative est l'effectif de la classe divisé par l'effectif total."),
 QC("Quel graphique convient à une variable quantitative continue ?", "Le camembert~L'histogramme~Le diagramme en bâtons~Le nuage de points", 1,
     "L'histogramme représente les effectifs par classes de valeurs continues."),
 QC("Que mesure l'écart-type ?", "La tendance centrale~La dispersion autour de la moyenne~Le nombre d'individus~La corrélation", 1,
     "L'écart-type est la racine de la variance ; il quantifie la dispersion."),
 QC("Dans une série ordonnée de 9 valeurs, quelle est la position de la médiane ?", "La 4e valeur~La 5e valeur~La 9e valeur~La moyenne des 4e et 5e", 1,
     "Pour un effectif impair, la médiane est la valeur de rang (n+1)/2, ici 5."),
 QC("Quel indicateur choisir pour un caractère qualitatif ?", "La moyenne~Le mode~L'écart-type~La médiane", 1,
     "Le mode est la seule mesure de position définie pour une variable qualitative."),
 QC("Que désigne l'intervalle interquartile ?", "L'écart entre min et max~L'écart entre Q1 et Q3~La moyenne des quartiles~La somme des effectifs", 1,
     "Il contient la moitié centrale des observations, soit 50 % de la série."),
 QC("Que faut-il toujours indiquer lors d'une présentation statistique ?", "Seulement le titre~La source, l'effectif et les unités~Le nom du logiciel~La couleur des graphiques", 1,
     "La rigueur documentaire (source, taille d'échantillon, unités) est indispensable à l'interprétation."),
 QT("Une série de 5 temps de réponse en millisecondes est : 12, 15, 18, 20, 95. Calculer moyenne, médiane et écart à la médiane. Commenter.",
    "La somme vaut 12 + 15 + 18 + 20 + 95 = 160, donc la moyenne est 160/5 = 32 ms. La série est déjà ordonnée ; avec 5 valeurs, la médiane est la 3e, soit 18 ms. L'écart entre la moyenne et la médiane est de 14 ms, causé par la valeur extrême 95 ms qui tire la moyenne vers le haut. La médiane décrit mieux le temps de réponse typique ; on complétera par l'étendue (95 − 12 = 83 ms) et on investiguera la valeur aberrante avant toute conclusion sur la performance du serveur.",
    "On calcule les deux indicateurs, on explique l'écart par la valeur extrême et on recommande la médiane."),
 QT("Expliquer pourquoi un échantillon représentatif est indispensable avant de généraliser un résultat statistique.",
    "Un échantillon est représentatif lorsque sa composition reflète celle de la population pour les caractéristiques pertinentes. Si le prélèvement est biaisé, par exemple en n'interrogeant que les utilisateurs satisfaits ou seulement une tranche d'âge, les estimateurs (moyenne, fréquence) sont biaisés et toute généralisation est invalide, même avec un grand effectif. Un tirage aléatoire, une stratification et un effectif suffisant réduisent ce risque. On doit aussi indiquer la marge d'incertitude et le niveau de confiance pour quantifier la précision de l'estimation avant de conclure sur l'ensemble de la population.",
    "On relie représentativité et absence de biais, puis on cite tirage aléatoire, stratification et marge d'incertitude.")],
C("La statistique descriptive résume une série par une tendance centrale et une dispersion, en choisissant des indicateurs adaptés au type de donnée.",
  "Fréquence = effectif / effectif total · écart-type = racine de la variance",
  "Moyenne sensible aux extrêmes · médiane robuste · mode pour le qualitatif",
  "Population~Ensemble complet~Échantillon~Partie prélevée~Représentativité~Moyenne~Somme divisée par n~Médiane~Valeur centrale~Écart-type~Dispersion",
  "Définir la population et l'échantillon|Trier et classer les données|Choisir les indicateurs pertinents|Construire le graphique adapté|Interpréter avec source et unités",
  "Utiliser la moyenne avec une valeur aberrante|Confondre effectif et fréquence|Choisir un camembert pour une variable continue|Omettre la taille de l'échantillon",
  "12;15;18;20;95~Moyenne 32 et médiane 18~Q1 et Q3~Moitié centrale~Fréquence~Effectif sur total~Histogramme~Variable continue~Mode~Classe la plus fréquente",
  "Moyenne~Sensible aux extrêmes~Médiane~Résistante aux extrêmes",
  "Effectif~Nombre d'individus~Fréquence~Part du total"))

# ============================================================ MS4
add("MS4", "Probabilités et échantillonnage : modéliser l'aléa", "Maths / stats", ["BTS1"],
S("Une expérience aléatoire est une épreuve dont l'issue est incertaine mais dont l'ensemble des résultats possibles, l'univers, est connu."
  "|Un événement est une partie de l'univers ; sa probabilité est un nombre entre 0 et 1, égale à 1 si l'événement est certain et à 0 s'il est impossible."
  "|Dans un univers fini équiprobable, la probabilité d'un événement est le nombre d'issues favorables divisé par le nombre total d'issues."
  "|La loi de probabilité associe à chaque issue sa probabilité ; la somme de toutes les probabilités vaut 1."
  "|Deux événements incompatibles ne peuvent pas survenir ensemble : P(A ∪ B) = P(A) + P(B)."
  "|Deux événements indépendants vérifient P(A ∩ B) = P(A) × P(B) : la réalisation de l'un n'influence pas l'autre."
  "|La probabilité conditionnelle P(A sachant B) = P(A ∩ B) / P(B) sert à réviser une croyance lorsqu'une information est connue."
  "|Un arbre pondéré représente les étapes successives d'une expérience et permet de calculer les probabilités composées par multiplication le long des branches."
  "|La formule des probabilités totales somme les probabilités conditionnelles pondérées par les probabilités des sous-groupes."
  "|La formule de Bayes inverse une probabilité conditionnelle : elle est utilisée, par exemple, pour interpréter un test de détection d'intrusion."
  "|Une variable aléatoire associe un nombre à chaque issue ; son espérance est la moyenne théorique à long terme."
  "|Les probabilités servent en cybersécurité pour estimer un risque, en qualité pour les plans d'échantillonnage et en gestion pour arbitrer des décisions."),
[QC("Quelle est la probabilité d'un événement impossible ?", "0~0,5~1~2", 0,
     "Un événement impossible a une probabilité nulle."),
 QC("Dans un univers équiprobable, comment calculer une probabilité ?", "Issues favorites multipliées par le total~Issues favorables divisées par le total~Total moins les issues~Une soustraction simple", 1,
     "P(A) = nombre d'issues favorables / nombre total d'issues."),
 QC("Que vérifient deux événements indépendants ?", "P(A ∩ B) = P(A) + P(B)~P(A ∩ B) = P(A) × P(B)~P(A) = P(B)~A et B sont incompatibles", 1,
     "L'indépendance se traduit par la multiplication des probabilités."),
 QC("Quelle est la formule de la probabilité conditionnelle ?", "P(A|B) = P(A)+P(B)~P(A|B) = P(A∩B)/P(B)~P(A|B) = P(B)/P(A)~P(A|B)=P(A)−P(B)", 1,
     "On restreint l'univers à B, d'où la division par P(B)."),
 QC("À quoi sert un arbre pondéré ?", "À trier des données~À représenter des étapes successives et calculer des probabilités composées~À dessiner un histogramme~À résoudre une équation", 1,
     "On multiplie les probabilités le long des branches puis on additionne les chemins favorables."),
 QC("Que donne la somme des probabilités d'une loi de probabilité complète ?", "0~1~L'effectif total~La moyenne", 1,
     "Les probabilités forment une somme égale à 1."),
 QC("Quel théorème permet de calculer P(A) à partir d'une partition de l'univers ?", "Bayes~Probabilités totales~Théorème central limite~Pythagore", 1,
     "Les probabilités totales pondèrent les probabilités conditionnelles par celles des sous-groupes."),
 QC("Que mesure l'espérance d'une variable aléatoire ?", "La valeur maximale~La moyenne théorique à long terme~La variance~Le nombre d'issues", 1,
     "L'espérance est la somme pondérée des valeurs par leurs probabilités."),
 QT("On lance deux dés équilibrés. Calculer la probabilité d'obtenir une somme égale à 7, puis une somme strictement supérieure à 10.",
    "L'univers compte 6 × 6 = 36 issues équiprobables. La somme 7 s'obtient par les couples (1,6), (2,5), (3,4), (4,3), (5,2), (6,1), soit 6 issues : P(somme = 7) = 6/36 = 1/6. Une somme strictement supérieure à 10 correspond à 11 ou 12 : les couples (5,6), (6,5) pour 11 et (6,6) pour 12, donc 3 issues. P(somme > 10) = 3/36 = 1/12. On vérifie que les deux résultats sont compris entre 0 et 1.",
    "On dénombre l'univers (36), les issues favorables (6 puis 3), puis on simplifie les fractions."),
 QT("Un test de détection d'intrusion a une probabilité de 0,99 de déclencher une alerte lors d'une attaque et 0,05 de déclencher à tort en l'absence d'attaque. La probabilité d'attaque est 0,01. Expliquer comment calculer la probabilité qu'une alerte corresponde réellement à une attaque.",
    "On note A l'attaque et S le déclenchement de l'alerte. On connaît P(A) = 0,01, P(S|A) = 0,99 et P(S|non A) = 0,05, donc P(non A) = 0,99. La probabilité totale d'alerte vaut P(S) = 0,99 × 0,01 + 0,05 × 0,99 = 0,0099 + 0,0495 = 0,0594. Par la formule de Bayes, P(A|S) = P(S|A) × P(A) / P(S) = 0,0099 / 0,0594 ≈ 0,167, soit environ 17 %. Malgré un test apparemment fiable, la plupart des alertes sont des faux positifs parce que les attaques sont rares : c'est le paradoxe de la base rate, qui justifie la corrélation et la qualification des alertes en SOC.",
    "On applique probabilités totales puis Bayes, et on interprète le faible résultat par la rareté des attaques.")],
C("Les probabilités modélisent l'aléa : on dénombre les issues, on compose les événements puis on révise les croyances avec Bayes.",
  "P(A|B) = P(A ∩ B) / P(B) · P(A ∩ B) = P(A)P(B) si indépendance",
  "Univers fini équiprobable : issues favorables / issues totales",
  "Univers~Ensemble des issues~Événement~Partie de l'univers~Probabilité~Entre 0 et 1~Indépendance~P(A∩B)=P(A)P(B)~Conditionnelle~P(A sachant B)",
  "Définir l'expérience et l'univers|Recenser les issues équiprobables|Identifier les issues favorables|Composer avec arbre ou formules|Interpréter le résultat",
  "Confondre indépendance et incompatibilité|Oublier que la somme vaut 1|Multiplier au lieu de diviser en conditionnelle|Ignorer la rareté de la base",
  "2 dés~36 issues~Somme 7~6 issues donc 1/6~Somme > 10~3 issues donc 1/12~Alarme~Environ 17 % de vraies attaques",
  "Incompatibles~P(A∪B)=P(A)+P(B)~Indépendants~P(A∩B)=P(A)×P(B)",
  "Probabilité~Avant information~Conditionnelle~Après information"))

# ============================================================ MS5
add("MS5", "Suites numériques et intérêts composés", "Maths / stats", ["BTS2"],
S("Une suite numérique est une famille ordonnée de nombres u0, u1, u2… indexée par les entiers naturels."
  "|Une suite arithmétique vérifie u(n+1) = u(n) + r : la différence entre deux termes consécutifs est constante, égale à la raison r."
  "|Le terme général d'une suite arithmétique est u(n) = u0 + n·r ; sa somme des n premiers termes vaut n(u0 + u(n))/2."
  "|Une suite géométrique vérifie u(n+1) = q·u(n) : le rapport entre deux termes consécutifs est constant, égal à la raison q."
  "|Le terme général d'une suite géométrique est u(n) = u0·q^n ; la somme des n premiers termes vaut u0(1 − q^n)/(1 − q) si q ≠ 1."
  "|Une suite croît si sa raison est positive (arithmétique) ou si q > 1 (géométrique à termes positifs) ; elle décroît si r < 0 ou 0 < q < 1."
  "|Les intérêts simples donnent un capital final C(n) = C0(1 + n·t) avec un taux t par période : l'intérêt est calculé seulement sur le capital initial."
  "|Les intérêts composés capitalisent les intérêts : C(n) = C0(1 + t)^n, ce qui correspond à une suite géométrique de raison 1 + t."
  "|La valeur acquise après n périodes se calcule avec le facteur d'actualisation inverse (1 + t)^(−n) pour comparer des flux à des dates différentes."
  "|Le taux effectif annuel tient compte de la capitalisation : un taux nominal divisé en m périodes donne (1 + i/m)^m − 1."
  "|L'inflation réduit le pouvoir d'achat : le taux réel approché vaut taux nominal moins inflation, le calcul exact utilisant un rapport de facteurs."
  "|Ces outils servent au dimensionnement d'un budget informatique pluriannuel, à l'amortissement d'équipements et à l'évaluation de la rentabilité d'un projet."),
[QC("Quelle est la raison d'une suite arithmétique ?", "Le rapport entre deux termes~La différence constante entre deux termes~Le premier terme~La somme des termes", 1,
     "Dans une suite arithmétique, u(n+1) − u(n) = r est constante."),
 QC("Que vaut u(n) pour une suite géométrique de premier terme u0 et de raison q ?", "u0 + n·q~u0·q^n~n·q~u0·q·n", 1,
     "La progression géométrique est exponentielle : u(n) = u0 q^n."),
 QC("Quelle suite modélise les intérêts composés ?", "Arithmétique~Géométrique~Constant~Alternée", 1,
     "Le capital est multiplié par (1 + t) chaque période : c'est une suite géométrique."),
 QC("Que vaut un capital de 1 000 € à 5 % pendant 2 ans en intérêts composés ?", "1 050 €~1 100 €~1 102,50 €~1 200 €", 2,
     "1000 × 1,05² = 1000 × 1,1025 = 1 102,50 €."),
 QC("Comment appelle-t-on le fait de ramener un flux futur à sa valeur actuelle ?", "Capitalisation~Actualisation~Amortissement~Indexation", 1,
     "L'actualisation divise par (1 + t)^n ; la capitalisation multiplie."),
 QC("Si 0 < q < 1, que fait une suite géométrique positive ?", "Elle croît~Elle décroît vers 0~Elle est constante~Elle diverge", 1,
     "Multiplier par un nombre entre 0 et 1 réduit chaque terme."),
 QC("Quel est le taux effectif d'un taux nominal 12 % capitalisé mensuellement ?", "12 %~Environ 12,68 %~1 %~24 %", 1,
     "(1 + 0,12/12)^12 − 1 ≈ 0,1268, soit 12,68 %."),
 QC("À quoi sert la somme des termes d'une suite arithmétique ?", "À calculer un capital~À totaliser des échéances régulières~À trouver une raison~À arrondir un résultat", 1,
     "Elle additionne des versements ou des coûts constants sur plusieurs périodes."),
 QT("Un serveur acheté 8 000 € perd 20 % de sa valeur chaque année. Donner la suite de valeur et calculer sa valeur après 3 ans.",
    "La valeur forme une suite géométrique de premier terme v0 = 8 000 et de raison q = 1 − 0,20 = 0,80, donc v(n) = 8 000 × 0,8^n. Après 3 ans : v(3) = 8 000 × 0,8³ = 8 000 × 0,512 = 4 096 €. La perte cumulée est donc de 3 904 €. On remarque que l'amortissement est dégressif : la perte de la première année est 1 600 €, celle de la troisième seulement 640 €, car elle s'applique à une valeur déjà réduite.",
    "On identifie la suite géométrique, sa raison 0,8, puis on calcule 8 000 × 0,8³ et on interprète l'amortissement dégressif."),
 QT("Comparer intérêts simples et intérêts composés sur 10 000 € à 4 % sur 5 ans, et expliquer l'écart.",
    "En intérêts simples, le capital final vaut 10 000 × (1 + 5 × 0,04) = 10 000 × 1,20 = 12 000 €, soit 2 000 € d'intérêts. En intérêts composés, il vaut 10 000 × 1,04^5 ≈ 10 000 × 1,21665 = 12 166,53 €, soit environ 166,53 € de plus. L'écart vient de la capitalisation : chaque année, les intérêts de l'année précédente produisent à leur tour des intérêts. Cet effet est d'autant plus sensible que la durée et le taux sont élevés ; il justifie de préciser le mode de calcul dans tout comparatif financier.",
    "On calcule les deux montants, puis on explique l'effet boule de neige de la capitalisation.")],
C("Suites arithmétique et géométrique modélisent des évolutions linéaires ou exponentielles ; intérêts composés et actualisation en sont les applications financières.",
  "C(n) = C0(1 + t)^n · actualisation : C0 = C(n)/(1 + t)^n",
  "Arithmétique : +r · Géométrique : ×q · simple : 1 + nt · composé : (1+t)^n",
  "Suite arithmétique~u(n+1)=u(n)+r~Suite géométrique~u(n+1)=q·u(n)~Intérêts simples~1+nt~Intérêts composés~(1+t)^n",
  "Repérer le type de suite|Identifier le premier terme et la raison|Écrire le terme général|Calculer le terme demandé|Interpréter dans le contexte",
  "Confondre raison additive et multiplicative|Oublier d'expliciter la période|Appliquer des intérêts simples aux composés|Négliger l'inflation",
  "8 000 € à −20 %/an~Valeur après 3 ans : 4 096 €~10 000 € à 4 %~Composés : 12 166,53 €~12 % mensuel~Effectif 12,68 %~Actualisation~Diviser par (1+t)^n",
  "Intérêts simples~Intérêt constant~Intérêts composés~Intérêt croissant",
  "Suite arithmétique~Croissance linéaire~Suite géométrique~Croissance exponentielle"))

# ============================================================ MS6
add("MS6", "Mathématiques financières : emprunts et tableaux d'amortissement", "Maths / stats", ["BTS2"],
S("Un emprunt est un capital prêté à une date initiale et remboursé selon un échéancier : chaque échéance comprend une part d'intérêt et une part de capital."
  "|L'annuité constante est l'échéance versée à chaque période ; elle est calculée avec le facteur d'annuité, qui dépend du taux et du nombre de périodes."
  "|La formule de l'annuité est a = C0 × t / (1 − (1 + t)^(−n)), où C0 est le capital emprunté, t le taux par période et n le nombre d'échéances."
  "|Le tableau d'amortissement détaille pour chaque ligne : capital restant dû, intérêt de la période, annuité, capital remboursé et nouveau capital restant dû."
  "|L'intérêt de la première ligne vaut C0 × t ; le capital remboursé vaut annuité moins intérêt."
  "|Le capital restant dû diminue au fil des échéances, donc la part d'intérêt diminue et la part de capital augmente, à annuité constante."
  "|L'actualisation permet de comparer des projets dont les flux n'interviennent pas aux mêmes dates, en les ramenant à une date de référence."
  "|La valeur actuelle nette (VAN) est la somme actualisée des flux : un projet est généralement accepté si sa VAN est positive au taux d'actualisation choisi."
  "|Le taux interne de rendement (TRI) est le taux d'actualisation qui annule la VAN : on le compare au coût du capital pour décider."
  "|La durée de récupération (payback) donne le temps nécessaire pour retrouver l'investissement initial sans actualisation : c'est un critère simple mais imparfait."
  "|Le coût global d'un crédit comprend les intérêts, les frais de dossier et l'assurance : le taux annuel effectif global (TAEG) les intègre et sert à comparer les offres."
  "|Ces calculs accompagnent les décisions d'investissement informatique : serveurs, licences, migration et projet de sécurité."),
[QC("Que contient une annuité d'emprunt ?", "Uniquement des intérêts~Une part d'intérêt et une part de capital~Uniquement du capital~Des frais de dossier seuls", 1,
     "Chaque échéance paie les intérêts de la période et rembourse une partie du capital."),
 QC("Que désigne le TAEG ?", "Le taux d'intérêt nominal~Le coût global annuel intégrant frais et assurance~La durée du prêt~Le capital restant dû", 1,
     "Le taux annuel effectif global est l'indicateur légal de comparaison des crédits."),
 QC("Dans un tableau d'amortissement, comment évolue la part d'intérêt à annuité constante ?", "Elle augmente~Elle diminue~Elle reste constante~Elle devient négative", 1,
     "Le capital restant dû baisse, donc l'intérêt calculé sur ce capital baisse."),
 QC("Quel est l'intérêt de la première échéance d'un emprunt de 10 000 € à 5 % ?", "50 €~500 €~1 000 €~5 000 €", 1,
     "L'intérêt initial vaut 10 000 × 0,05 = 500 €."),
 QC("Comment décider avec une VAN positive ?", "On refuse le projet~On accepte généralement le projet~On attend l'année suivante~On double le taux", 1,
     "Une VAN positive signifie que le projet crée de la valeur au taux d'actualisation retenu."),
 QC("Que représente le TRI ?", "Le taux qui annule la VAN~Le taux d'inflation~Le taux de la Banque centrale~Le coût de l'assurance", 0,
     "Le taux interne de rendement rend la valeur actuelle nette nulle."),
 QC("Quel critère ne tient pas compte de l'actualisation ?", "La VAN~Le TRI~La durée de récupération~L'actualisation", 2,
     "Le payback somme les flux nominaux sans les actualiser."),
 QC("Pourquoi actualiser des flux futurs ?", "Pour les rendre tous identiques~Pour les comparer à une même date en tenant compte du coût de l'argent~Pour supprimer les intérêts~Pour arrondir les montants", 1,
     "Un euro demain ne vaut pas un euro aujourd'hui : l'actualisation tient compte du taux et du temps."),
 QT("Un emprunt de 10 000 € est remboursé en 5 annuités à 6 %. Calculer l'annuité (facteur donné : 0,2374) et compléter la première ligne du tableau.",
    "L'annuité vaut a = C0 × t / (1 − (1+t)^(−n)) = C0 × facteur = 10 000 × 0,2374 = 2 374 €. Première ligne : capital restant dû initial 10 000 € ; intérêt = 10 000 × 0,06 = 600 € ; annuité = 2 374 € ; capital remboursé = 2 374 − 600 = 1 774 € ; nouveau capital restant dû = 10 000 − 1 774 = 8 226 €. On vérifiera à la dernière ligne que le capital restant dû atteint zéro (aux arrondis près).",
    "On calcule l'annuité avec le facteur, puis intérêt, capital remboursé et solde de la première ligne."),
 QT("Un projet d'investissement coûte 50 000 € et génère 15 000 € par an pendant 5 ans. Expliquer comment décider avec un taux d'actualisation de 8 %.",
    "On calcule la valeur actuelle nette en actualisant chaque flux : VAN = −50 000 + 15 000 × (1 − 1,08^(−5))/0,08. Le facteur d'annuité vaut environ 3,9927, donc la valeur actualisée des recettes est d'environ 59 890 € et la VAN d'environ 9 890 €. Cette VAN positive indique que le projet crée de la valeur au taux de 8 %. On complète l'analyse par le TRI, qui serait ici supérieur à 8 %, et par une analyse de sensibilité sur les hypothèses de recettes et de taux, car une VAN reste une estimation dépendante des prévisions.",
    "On calcule la VAN avec le facteur d'annuité, on interprète le signe et on recommande TRI et sensibilité.")],
C("Un emprunt se décompose en intérêts et en capital ; la VAN et le TRI permettent de comparer des investissements à des dates différentes.",
  "Annuité = C0 × t / (1 − (1+t)^(−n))",
  "VAN = somme des flux actualisés · TRI = taux qui annule la VAN · TAEG = coût global",
  "Capital emprunté~Montant initial~Annuité~Échéance constante~Intérêt~Capital restant dû × taux~Capital remboursé~Annuité moins intérêt~VAN~Valeur actuelle nette",
  "Fixer capital, taux et durée|Calculer l'annuité|Construire le tableau ligne par ligne|Actualiser les flux du projet|Comparer VAN, TRI et TAEG",
  "Confondre taux nominal et taux par période|Oublier les frais dans le TAEG|Additionner des flux non actualisés|Croire qu'une VAN positive supprime tout risque",
  "10 000 € à 6 %~Annuité 2 374 €~Première ligne~Intérêt 600 €, capital 1 774 €~Solde après 1 an~8 226 €~50 000 € et 15 000/an~VAN environ 9 890 €",
  "Annuité constante~Part intérêt décroissante~Part capital croissante~Répartition variable",
  "VAN positive~Projet créateur de valeur~TRI supérieur au coût du capital~Décision favorable"))

# ============================================================ MS7
add("MS7", "Dérivation et optimisation : étude des variations", "Maths / stats", ["BTS2"],
S("La dérivation étudie la variation locale d'une fonction : le nombre dérivé est la limite du taux d'accroissement quand l'intervalle tend vers zéro."
  "|Le nombre dérivé f'(a) est la pente de la tangente à la courbe au point d'abscisse a."
  "|Les dérivées usuelles sont : (x^n)' = n·x^(n−1), (e^x)' = e^x, (ln x)' = 1/x, (sin x)' = cos x et (cos x)' = −sin x."
  "|La dérivée d'un produit vérifie (uv)' = u'v + uv' et celle d'un quotient (u/v)' = (u'v − uv')/v², avec v non nul."
  "|La dérivée d'une composée est (u ∘ v)' = u'(v) × v' : c'est la règle de la chaîne."
  "|Une fonction est strictement croissante sur un intervalle si sa dérivée y est strictement positive, et décroissante si elle y est négative."
  "|Un point critique est une valeur où f'(x) = 0 ou n'existe pas : c'est un candidat à un extremum local."
  "|Le théorème du signe de la dérivée permet de classer un extremum : passage de + à − donne un maximum, passage de − à + un minimum."
  "|Pour trouver un extremum sur un intervalle fermé, on compare les valeurs aux points critiques et aux bornes de l'intervalle."
  "|L'optimisation consiste à modéliser une grandeur à maximiser ou minimiser, puis à appliquer cette méthode : modéliser, dériver, annuler, classer, conclure."
  "|En économie, on optimise un coût, un bénéfice ou un rendement ; en technique, une surface d'échange ou une consommation d'énergie."
  "|Ces outils prolongent l'étude des fonctions de l'unité U3 et servent aux calculs d'élasticité et de rentabilité."),
[QC("Quelle est l'interprétation géométrique du nombre dérivé ?", "L'aire sous la courbe~La pente de la tangente~L'abscisse du sommet~La longueur de la courbe", 1,
     "f'(a) est le coefficient directeur de la tangente en a."),
 QC("Que vaut la dérivée de x³ ?", "3x²~x²~3x~x⁴", 0,
     "La formule (x^n)' = n x^(n−1) donne 3x²."),
 QC("Quelle est la dérivée de e^x ?", "e^x~x·e^x~1/x~−e^x", 0,
     "L'exponentielle népérienne est sa propre dérivée."),
 QC("Comment dérive-t-on un produit uv ?", "u'v'~u'v + uv'~u'v − uv'~u/v", 1,
     "La règle du produit fait intervenir les deux dérivées."),
 QC("Qu'appelle-t-on point critique ?", "Un point où f change de signe~Un point où la dérivée est nulle ou n'existe pas~Une borne du graphique~Un point d'intersection avec l'axe des x", 1,
     "C'est un candidat à un extremum local."),
 QC("Une dérivée négative sur un intervalle indique que la fonction est…", "Croissante~Décroissante~Constante~Maximum", 1,
     "Le signe négatif de la dérivée correspond à une fonction décroissante."),
 QC("Quel changement de signe de f' donne un maximum local ?", "De − à +~De + à −~Toujours positif~Toujours nul", 1,
     "La fonction monte puis descend : c'est un maximum local."),
 QC("Quelle est la dernière étape d'une démarche d'optimisation ?", "Dériver~Annuler la dérivée~Conclure par une interprétation du résultat~Tracer la courbe", 2,
     "Après avoir classé l'extremum, on interprète la solution dans le contexte du problème."),
 QT("Étudier les variations de f(x) = x³ − 3x et déterminer ses extrema locaux.",
    "On dérive : f'(x) = 3x² − 3 = 3(x² − 1) = 3(x − 1)(x + 1). Les points critiques sont x = −1 et x = 1. Le signe de f' est positif sur ]−∞ ; −1[, négatif sur ]−1 ; 1[ puis positif sur ]1 ; +∞[. La fonction est donc croissante, puis décroissante, puis croissante. En x = −1, le signe passe de + à − : maximum local, f(−1) = −1 + 3 = 2. En x = 1, le signe passe de − à + : minimum local, f(1) = 1 − 3 = −2.",
    "On factorise la dérivée, on étudie son signe sur les intervalles, puis on classe les deux extrema."),
 QT("Une entreprise a un coût de production C(x) = x² − 40x + 900 pour x unités. Déterminer la quantité qui minimise le coût et le coût minimal.",
    "On dérive : C'(x) = 2x − 40. Le point critique vérifie 2x − 40 = 0, soit x = 20. La dérivée est négative avant 20 et positive après : le signe passe de − à +, donc x = 20 donne un minimum. Le coût minimal vaut C(20) = 400 − 800 + 900 = 500. La démarche complète est : modéliser le coût, dériver, annuler la dérivée, classer le point critique par le signe, puis interpréter : produire 20 unités minimise le coût à 500 unités monétaires.",
    "On calcule la dérivée, on annule, on classe le minimum par le signe puis on évalue le coût.")],
C("La dérivée donne la pente de la tangente et le signe des variations : annuler la dérivée puis classer le point critique permet d'optimiser.",
  "f'(a) = pente de la tangente en a · (x^n)' = n·x^(n−1)",
  "f' > 0 : croissante · f' < 0 : décroissante · + puis − : maximum",
  "Nombre dérivé~Pente de la tangente~Taux d'accroissement~Dérivée~Fonction dérivée~Règles de calcul~Point critique~f'(x)=0~Extremum~Maximum ou minimum local",
  "Modéliser la grandeur à optimiser|Calculer la dérivée|Résoudre f'(x)=0|Étudier le signe de la dérivée|Conclure et interpréter",
  "Confondre f et f'|Oublier les bornes sur un intervalle fermé|Classer un extremum sans étude de signe|Ne pas interpréter le résultat",
  "x³−3x~f'=3(x−1)(x+1)~x=−1~Maximum local 2~x=1~Minimum local −2~Coût x²−40x+900~Minimum 500 pour x=20",
  "Maximum local~Dérivée de + vers −~Minimum local~Dérivée de − vers +",
  "Croissante~Dérivée positive~Décroissante~Dérivée négative"))

# ============================================================ MS8
add("MS8", "Intervalles de confiance et tests d'hypothèses", "Maths / stats", ["BTS2"],
S("L'inférence statistique utilise un échantillon pour estimer les paramètres d'une population et prendre une décision avec une marge d'incertitude."
  "|Un estimateur est une statistique calculée sur l'échantillon, comme la moyenne empirique, destinée à estimer un paramètre inconnu."
  "|Un estimateur sans biais a une espérance égale au paramètre estimé : la moyenne empirique est un estimateur sans biais de la moyenne de la population."
  "|L'écart-type empirique est calculé avec un dénominateur n−1, appelé correction de Bessel, pour obtenir un estimateur sans biais de la variance."
  "|Un intervalle de confiance donne une plage de valeurs plausibles pour le paramètre, avec un niveau de confiance, souvent 95 %."
  "|Pour une moyenne avec grand effectif, l'intervalle est estimée par m ± z × s/√n, où z vaut environ 1,96 au niveau 95 %."
  "|La largeur de l'intervalle diminue quand n augmente et quand la dispersion s diminue : elle est proportionnelle à 1/√n."
  "|Pour un petit effectif et une variance inconnue, on utilise la loi de Student à n−1 degrés de liberté plutôt que la loi normale."
  "|Pour une proportion, l'intervalle s'appuie sur p̂ ± z × √(p̂(1−p̂)/n)."
  "|Un test d'hypothèse oppose une hypothèse nulle H0 à une hypothèse alternative H1, et fixe un risque de première espèce alpha, souvent 5 %."
  "|La p-value est la probabilité d'observer un résultat au moins aussi extrême si H0 est vraie : si elle est inférieure à alpha, on rejette H0."
  "|Une erreur de première espèce rejette à tort une vraie H0 ; une erreur de deuxième espèce ne rejette pas une H0 fausse : la puissance du test vaut 1 moins ce risque."),
[QC("Que désigne un estimateur sans biais ?", "Un estimateur toujours exact~Un estimateur dont l'espérance égale le paramètre~Un estimateur arrondi~Un estimateur négatif", 1,
     "L'absence de biais porte sur l'espérance, pas sur la valeur d'un échantillon donné."),
 QC("Pourquoi utilise-t-on n−1 dans la variance empirique ?", "Pour simplifier le calcul~Correction de Bessel : rendre l'estimateur sans biais~Pour obtenir un nombre entier~Par convention graphique", 1,
     "La correction de Bessel compense la sous-estimation de la variance par la moyenne empirique."),
 QC("Quelle valeur de z pour un intervalle de confiance à 95 % (grand effectif) ?", "1,28~1,64~1,96~2,58", 2,
     "Le quantile 0,975 de la loi normale centrée réduite vaut environ 1,96."),
 QC("Comment réduire la largeur d'un intervalle de confiance ?", "Diminuer l'effectif~Augmenter l'effectif~Augmenter la dispersion~Changer d'unité", 1,
     "La marge d'erreur est inversement proportionnelle à la racine de n."),
 QC("Quelle loi utiliser pour une petite série à variance inconnue ?", "Loi normale~Loi de Student~Loi de Poisson~Loi binomiale", 1,
     "La loi de Student à n−1 degrés de liberté tient compte de l'estimation de la variance."),
 QC("Que signifie un risque alpha de 5 % ?", "5 % de chances que le test soit faux dans tous les cas~Probabilité de rejeter H0 alors qu'elle est vraie~Probabilité d'accepter H1~Le niveau de confiance", 1,
     "Alpha est le risque de première espèce, fixé avant le test."),
 QC("Quand rejette-t-on H0 avec une p-value ?", "Si p-value > alpha~Si p-value < alpha~Toujours~Jamais", 1,
     "Une p-value faible indique un résultat peu compatible avec H0."),
 QC("Que vaut la puissance d'un test ?", "Alpha~1 moins la probabilité d'erreur de deuxième espèce~La p-value~Le niveau de confiance", 1,
     "La puissance est la probabilité de rejeter H0 lorsque H1 est vraie."),
 QT("Un échantillon de 100 serveurs donne un temps de réponse moyen de 200 ms avec un écart-type de 30 ms. Construire l'intervalle de confiance à 95 % de la moyenne et l'interpréter.",
    "Pour un grand effectif, la marge d'erreur vaut z × s/√n = 1,96 × 30/√100 = 1,96 × 3 = 5,88 ms. L'intervalle de confiance à 95 % est donc [200 − 5,88 ; 200 + 5,88] = [194,12 ; 205,88] ms. Interprétation : si l'on répétait de nombreux échantillons de 100 serveurs et construisait un tel intervalle à chaque fois, environ 95 % de ces intervalles contiendraient la vraie moyenne de la population. On peut dire que 200 ms est notre meilleure estimation, avec une précision d'environ ±6 ms.",
    "On calcule l'erreur standard s/√n, la marge avec z=1,96, l'intervalle, puis on donne une interprétation correcte du niveau de confiance."),
 QT("Expliquer la démarche d'un test d'hypothèse et les deux types d'erreur possibles dans un contexte de supervision.",
    "On formule d'abord H0 (par exemple : le temps de réponse moyen n'a pas changé, il vaut 200 ms) et H1 (il a augmenté), puis on choisit le risque alpha, par exemple 5 %. On calcule la statistique de test à partir de l'échantillon, on en déduit la p-value et on compare : si p-value < alpha, on rejette H0 et on déclenche une alerte. Sinon on ne rejette pas H0, tout en sachant que cela ne prouve pas son exactitude. Une erreur de première espèce est une fausse alerte : on rejette H0 alors que le service va bien. Une erreur de deuxième espèce est un incident manqué : on ne détecte pas une dégradation réelle. La puissance du test mesure sa capacité à détecter une dégradation effectivement présente ; elle dépend de l'effectif et de l'ampleur de l'écart.",
    "On décrit formulation, choix de alpha, p-value, décision, puis on définit faux positif, faux négatif et puissance.")],
C("L'inférence quantifie l'incertitude : un intervalle de confiance estime un paramètre, un test décide entre deux hypothèses avec des risques choisis.",
  "IC à 95 % = moyenne ± 1,96 × s/√n",
  "p-value < alpha : rejeter H0 · erreur de 1re espèce = fausse alerte",
  "Estimateur~Statistique sur échantillon~Sans biais~Espérance égale au paramètre~Intervalle~Plage et niveau de confiance~Marge d'erreur~z fois s sur racine n~Test~H0 contre H1",
  "Formuler l'hypothèse et le risque alpha|Choisir la statistique de test|Calculer la p-value|Comparer à alpha et décider|Interpréter en contexte et documenter",
  "Dire qu'un intervalle à 95 % contient la vraie valeur avec certitude|Confondre p-value et probabilité que H0 soit vraie|Fixer alpha après avoir vu les résultats|Oublier d'indiquer la taille de l'échantillon",
  "100 serveurs~Moyenne 200 ms, s=30~Intervalle~194,1 à 205,9 ms~Alpha 5 %~Seuil de décision~p<0,05~Rejet de H0~Puissance~1 moins bêta",
  "Erreur de 1re espèce~Fausse alerte~Erreur de 2e espèce~Incident manqué",
  "Intervalle de confiance~Estimation~Test d'hypothèse~Décision"))

# FIN DES LOTS
valider_et_ecrire(F, "btsciel-mat-part-A.json")
