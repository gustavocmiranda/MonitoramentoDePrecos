import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout='wide')

st.sidebar.markdown('Operations')
st.title('Operations')

with st.expander('Todas as compras'):
    if st.button("Exibir todas as compras", key='btn_get_all_buys'):
        response = requests.get("http://backend:8000/buys/")

        if response.status_code == 200:
            buys = response.json()
            df = pd.DataFrame(buys)

            st.write(df.to_html(index=False), unsafe_allow_html=True)

with st.expander('Última compra'):
    if st.button("Exibir última compra", key='btn_get_last_buy'):
        response = requests.get("http://backend:8000/last/")

        if response.status_code == 200:
            buy = response.json()
            df = pd.DataFrame([buy])

            st.write(df.to_html(index=False), unsafe_allow_html=True)

with st.expander('Deletar uma compra'):
    buy_id = st.number_input('ID da compra a ser excluída', 1, step=1, format="%d")

    if st.button("Deletar compra", key='btn_delete_buy'):
        response = requests.delete(f"http://backend:8000//buys/{buy_id}")

        st.write(response.status_code)

        if response.status_code == 200:
            st.write('Compra excluída')
