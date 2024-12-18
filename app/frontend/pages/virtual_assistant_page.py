import streamlit as st


st.sidebar.markdown('Virtual Assistant')
st.title('Virtual Assistant')


pergunta = st.text_input("Digite sua pergunta")

if st.button("Enviar pergunta ao assistente"):
    st.write(pergunta)
