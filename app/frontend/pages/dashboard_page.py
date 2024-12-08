import streamlit as st
import pandas as pd
import requests

st.sidebar.markdown('Dashboard')
st.title('Dashboard')

response = requests.get("http://backend:8000/buys/")
if response.status_code == 200:
    data = pd.DataFrame(response.json())


grouped_data = data['local_de_compra'].value_counts().reset_index()
grouped_data.columns = ['local_de_compra', 'numero_de_compras']

# Exibir o gráfico de barras
st.bar_chart(grouped_data.set_index('local_de_compra'))