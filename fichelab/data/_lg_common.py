import json, os
BASE = os.path.dirname(os.path.abspath(__file__))
G = ["generale"]

def q(question, options, correct, correction):
    return {"type": "qcm", "q": question, "options": options, "correct": correct, "correction": correction}

def t(question, reponse, correction):
    return {"type": "texte", "q": question, "reponse": reponse, "correction": correction}

def f(annees, matiere, titre, source, points, questions, filieres=None):
    return {"filieres": filieres or G, "annees": annees, "matiere": matiere,
            "titre": titre, "source": source, "points": points, "questions": questions}

def a(titre, matiere, contenu, correction, annees=None, type="genere", filieres=None):
    return {"filieres": filieres or G, "annees": annees or ["Terminale"],
            "titre": titre, "matiere": matiere, "type": type,
            "contenu": contenu, "correction": correction}

def save(name, fiches, annales):
    path = os.path.join(BASE, name)
    with open(path, "w", encoding="utf-8") as fp:
        json.dump({"fiches": fiches, "annales": annales}, fp, ensure_ascii=False, indent=2)
    return path
