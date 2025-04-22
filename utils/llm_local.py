from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = Ollama(model="mistral")  # Ou openhermes, llama2...

def analyser_conformite_local(texte):
    prompt = PromptTemplate(
        input_variables=["document"],
        template="""
Tu es un expert conformité bancaire au Luxembourg.

Voici un document client :
\"\"\"{document}\"\"\"

Donne une analyse de conformité :
1. Statut global : Conforme / Non conforme
2. Eléments manquants ou à corriger
3. Résumé structuré des infos extraites (Nom, Date, Adresse, etc.)

Réponds en français.
"""
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    resultat = chain.run(document=texte)
    return resultat
