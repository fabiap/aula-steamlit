import streamlit as st
import pandas as pd
import numpy as np

#st.number_input("entra com um numero", min_value=0, max_value=100, value=50)
#st.button("oi")

#configuração da página
st.set_page_config(
    page_title="analise de dados",
    page_icon="📊",
    layout="wide"
)

st.title("teste")

#importação dos dataframe
df = pd.read_csv("database/compostagem_bio.csv", sep=",")

#leitura do dataframe
st.title("analise de dados de compostagem")
st.dataframe(df)

st.markdown("--")

#grafico de linhas desse dataframe
st.subheader("grafico de linhas")

df = pd.DataFrame(
    np.random.randn(20, 3), columns=["nome", "escala", "tipo", "regiao", "quantidade_residuo_kg", "dias_compostagem", "temperatura_media_local"]
)

st.line_chart(
    chart_data,
    x="col1",
    y=["col2", "col3"],
    color=["#FF0000", "#0000FF"],  # Optional
)