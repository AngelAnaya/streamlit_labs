import pandas as pd
import streamlit as st

st.title("Streamlit - Search names")
DATA_URL = "dataset.csv"

@st.cache
def load_data_by_range(start_id, end_id):
    df = pd.read_csv(DATA_URL)
    filtered_data_byrange = df[(df["index"] >= start_id) & (df["index"] <= end_id)]
    return filtered_data_byrange

start_id = st.text_input("Start ID: ")
end_id = st.text_input("End ID: ")
Boton_range = st.button("Search by range")

if (Boton_range):
    filteredbyrange = load_data_by_range(int(start_id), int(end_id))
    count_row = filteredbyrange.shape[0]
    st.write(f"Total items: {count_row}")
    st.dataframe(filteredbyrange)