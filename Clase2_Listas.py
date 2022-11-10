import pandas as pd
import streamlit as st

st.title("Streamlit - Search names")
DATA_URL = "dataset.csv"

@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

@st.cache
def load_data_by_sex(sex, df):
    filtered_data_by_sex = df[df["sex"] == sex]
    return filtered_data_by_sex

data = load_data()
selected_sex = st.selectbox("Select sex:", data["sex"].unique())
Boton_filtered_sex = st.button("Filtered by sex")

if (Boton_filtered_sex):
    filteredbysex = load_data_by_sex(selected_sex, data)
    count_row = filteredbysex.shape[0]
    st.write(f"Total items: {count_row}")
    st.dataframe(filteredbysex)