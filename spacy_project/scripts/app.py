import streamlit as st
import spacy

if __name__ == "__main__":

    st.header("Text Klassifikation in spaCy! ✨")
    st.markdown(
        """Mit dieser App kannst du dein trainiertes Modell testen. Im Textfeld kannst du einen beliebigen Kommentar schreiben und ihn dir vom Modell vorhersagen, ob dieser angebracht oder unangebracht ist."""
    )

    st.markdown("""---""")

    if "model" not in st.session_state:
        nlp = spacy.load("training/model-best")
        st.session_state["model"] = nlp

    text = st.text_input("Modell Input")

    if "model" in st.session_state:
        doc = st.session_state["model"](text)

        for cat in doc.cats:
            st.markdown(f"**{cat}** : {round(doc.cats[cat],2)}%")
