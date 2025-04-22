import streamlit as st
from utils.analyse import extraire_texte
from utils.llm_local import analyser_conformite_local

st.set_page_config(page_title="Analyse Conformité Bancaire", layout="centered")
st.title("📑 Vérification de Conformité Bancaire – IA locale (Mistral)")

st.markdown(
    """
Cette application permet de vérifier la conformité des documents clients (KYC, AML, etc.)
au Luxembourg à l’aide d’un **LLM local (Mistral via Ollama)**.
"""
)

uploaded_file = st.file_uploader("📤 Téléversez un document (.pdf ou .docx)", type=["pdf", "docx"])

if uploaded_file:
    st.success("✅ Document bien reçu")

    texte = extraire_texte(uploaded_file)

    st.subheader("📝 Texte extrait du document :")
    st.text_area("Contenu brut", texte, height=300)

    if st.button("🔍 Analyser la conformité avec IA locale"):
        with st.spinner("Analyse en cours avec le modèle Mistral local..."):
            resultat = analyser_conformite_local(texte)

        st.subheader("📊 Résultat de l'analyse IA :")
        st.markdown(resultat)
