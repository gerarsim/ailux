import spacy
import re

nlp = spacy.load("fr_core_news_md")  # modèle français de spaCy

def analyser_conformite_avec_ia(texte):
    doc = nlp(texte)

    donnees = {
        "nom_detecté": None,
        "adresse": None,
        "date_naissance": None,
        "pays_detecté": None
    }

    for ent in doc.ents:
        if ent.label_ == "PER":
            donnees["nom_detecté"] = ent.text
        elif ent.label_ == "LOC":
            donnees["adresse"] = ent.text
        elif ent.label_ == "DATE":
            if re.search(r"\d{4}", ent.text):
                donnees["date_naissance"] = ent.text
        elif ent.label_ == "GPE":
            donnees["pays_detecté"] = ent.text

    # Simuler une règle de conformité
    conforme = True
    raisons = []

    if not donnees["nom_detecté"]:
        conforme = False
        raisons.append("Nom non détecté")
    if not donnees["date_naissance"]:
        conforme = False
        raisons.append("Date de naissance manquante")
    if donnees["pays_detecté"] and "Iran" in donnees["pays_detecté"]:
        conforme = False
        raisons.append("Pays non autorisé : Iran")

    return {
        "statut": "Conforme" if conforme else "Non conforme",
        "détails": donnees,
        "raisons": raisons
    }
