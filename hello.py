import streamlit as st
import pandas as pd
import os

# Nome do arquivo CSV onde os dados serão armazenados
data_file = "compras.csv"


mercados = [
    "Zona Sul", "Guanabara", "Amazon", "Pão de Açúcar", "Ultra", "FarmaLife"
]

# Criação do formulário
with st.form("dados_enquete", clear_on_submit=True):
    # produto = st.selectbox("Produto", estados)
    produto = st.text_input("Produto")
    preco = st.number_input("Preço")
    mercado = st.selectbox("Mercado", mercados, )
    promocao = st.checkbox("Promoção")
    data = st.date_input("Data da Compra", "today", format="DD/MM/YYYY")

    # Botão para submeter o formulário
    submit_button = st.form_submit_button("Enviar")

# Se o botão foi clicado, salvar os dados no DataFrame e no CSV
if submit_button:
    novo_dado = {
        "Produto": produto,
        "Preço": preco,
        "Mercado": mercado,
        "Promoção": promocao,
        "Data": data
    }
    new_data = pd.DataFrame([novo_dado])

    # Verificar se o arquivo existe antes de tentar ler
    if os.path.exists(data_file):
        existing_data = pd.read_csv(data_file)
        updated_data = pd.concat([existing_data, new_data], axis=0, ignore_index=True)
    else:
        updated_data = new_data
    
    # Salvar os dados no arquivo CSV
    updated_data.to_csv(data_file, index=False)
    st.success("Dados enviados com sucesso!")

st.write("Outside the form")