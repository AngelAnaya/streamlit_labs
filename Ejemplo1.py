import streamlit as st
import numpy as np
import pandas as pd

st.title("Título de la página")

sidebar = st.sidebar
sidebar.title("Título de la barra lateral")
sidebar.write("Información de mi sidebar")

st.header("Header de mi app")
st.write("Información de mi app")

if sidebar.checkbox("Mostrar dataframe:"):
    chart_data = pd.DataFrame(np.random.randn(20,3), columns = ["A","B","C"])

    st.dataframe(chart_data)