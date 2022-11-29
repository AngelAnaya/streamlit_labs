import streamlit as st
import pandas as pd

st.title("Streamlit con caché")

DATA_URL = "uber-raw-data-sep14.csv"
DATE_COLUMN = "Date/Time"

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data = load_data(100)
st.dataframe(data)
st.map(data)