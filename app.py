import streamlit as st

from database import connect_to_database, save_product


mercados = [
    "Zona Sul", "Guanabara", "Amazon", "Pão de Açúcar", "Ultra", "FarmaLife"
]

# Criação do formulário
with st.form("dados_enquete", clear_on_submit=True):
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

    conn = connect_to_database()
    save_product(conn, novo_dado)
    conn.close()

    st.success("Dados enviados com sucesso!")
