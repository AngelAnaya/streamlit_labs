import streamlit as st
import pandas as pd

st.title("Streamlit con caché")

DATA_URL = "https://raw.githubusercontent.com/AngelAnaya/streamlit_labs/master/dataset.csv?token=GHSAT0AAAAAAB2XZZA34D3WK5YUPLUCWCAAY3NHLFA"

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows = nrows)
    return data

data_load_state = st.text("Loading data...")
data = load_data(1000)
data_load_state.text("Done!")

st.dataframe(data)